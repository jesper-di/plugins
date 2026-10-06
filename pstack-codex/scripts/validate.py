#!/usr/bin/env python3
"""Validate native package metadata, local references, and host dependencies."""

from pathlib import Path
import json
import re
import sys
import tomllib


PACKAGE = Path(__file__).resolve().parents[1]
EXCLUDED = {"node_modules", "__pycache__", ".git"}
FORBIDDEN = re.compile(
    r"\.cursor/|pstack-models\.mdc|\b(?:grok|claude)-(?:\d|opus|sonnet)|"
    r"\bsubagent_type\b|\brun_in_background\b|\bAskQuestion\b|\bTodoWrite\b|"
    r"/loop\b|/add-plugin\b|/automate\b|api2\.cursor\.sh"
)


def validate(package=PACKAGE):
    package = Path(package)
    errors = []
    def files(pattern):
        return (p for p in package.rglob(pattern) if not EXCLUDED.intersection(p.relative_to(package).parts))
    def require(condition, message):
        if not condition:
            errors.append(message)
    manifest = json.loads((package / "plugin.json").read_text())
    legacy = json.loads((package / ".codex-plugin/plugin.json").read_text())
    require(manifest["name"] == legacy["name"] == "pstack-codex", "Manifest name mismatch")
    require(manifest["version"] == legacy["version"], "Manifest version mismatch")
    require(manifest["license"] == "MIT", "Missing upstream license")
    require((package / "LICENSE").is_file(), "Missing LICENSE")
    require((package / legacy["skills"]).is_dir(), "Missing skills directory")
    for key in ["logo"]:
        value = manifest["extensions"]["com.openai"]["interface"][key]
        require((package / value).is_file(), f"Missing asset: {value}")
    marketplace = json.loads((package.parent / ".agents/plugins/marketplace.json").read_text())
    entry = next(p for p in marketplace["plugins"] if p["name"] == manifest["name"])
    require((package.parent / entry["source"]["path"]).resolve() == package.resolve(), "Marketplace path mismatch")
    names = set()
    for path in files("SKILL.md"):
        text = path.read_text()
        front = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
        require(bool(front), f"Missing frontmatter: {path}")
        if not front:
            continue
        name = re.search(r"^name: ([a-z0-9-]+)$", front[1], re.M)
        desc = re.search(r"^description: (.+)$", front[1], re.M)
        require(bool(name) and len(name[1]) <= 64 and name[1] == path.parent.name, f"Invalid skill name: {path}")
        require(bool(desc), f"Missing skill description: {path}")
        if desc:
            try:
                description = json.loads(desc[1])
                require(isinstance(description, str) and 0 < len(description) <= 1024, f"Invalid description: {path}")
            except json.JSONDecodeError:
                errors.append(f"Description must be a JSON-compatible YAML string: {path}")
        if path.parent.parent == package / "skills" and name:
            require(name[1] not in names, f"Duplicate skill: {name[1]}")
            names.add(name[1])
        require("Codex runtime contract" in text, f"Missing runtime contract: {path}")
    require(len(names) == 55, f"Expected 55 plugin skills, found {len(names)}")
    agents = []
    for path in (package / "agents").glob("*.toml"):
        data = tomllib.loads(path.read_text())
        for key in ["name", "description", "developer_instructions"]:
            require(bool(data.get(key)), f"Missing agent {key}: {path}")
        require("model" not in data and "model_reasoning_effort" not in data, f"Unexpected model override: {path}")
        agents.append(data["name"])
    require(set(agents) == {"poteto-agent", "comment-sicko", "pstack-reviewer", "pstack-explorer"}, "Missing native agents")
    for path in files("*.md"):
        text = path.read_text()
        # Ignore fenced example links; validate actual Markdown document references.
        outside_code = re.sub(r"(?m)^(`{3,}|~{3,}).*?^\1\s*$", "", text, flags=re.S)
        for target in re.findall(r"\]\(([^)\s]+)\)", outside_code):
            if ":" in target or target.startswith("#") or "<" in target:
                continue
            require((path.parent / target.split("#")[0]).exists(), f"Broken link: {path.relative_to(package)} -> {target}")
        for match in FORBIDDEN.finditer(text):
            errors.append(f"Unsupported host dependency: {path.relative_to(package)} -> {match[0]}")
    for path in files("*.sh"):
        require(not FORBIDDEN.search(path.read_text()), f"Unsupported script dependency: {path}")
    for path in files("*.yaml"):
        require(not FORBIDDEN.search(path.read_text()), f"Unsupported config dependency: {path}")
    return errors


if __name__ == "__main__":
    errors = validate()
    for error in errors:
        print(error, file=sys.stderr)
    if not errors:
        print("Validated manifests, 55 plugin skills, optional operations skills, four native agents, and local references.")
    sys.exit(bool(errors))
