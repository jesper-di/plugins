#!/usr/bin/env python3
"""Install native project skills and agents without replacing existing files."""

import argparse
from pathlib import Path
import json
import os
import sys


PACKAGE = Path(__file__).resolve().parents[1]


def plan_install(target, package=PACKAGE, agents_only=False):
    target = Path(target).resolve(strict=True)
    package = Path(package).resolve(strict=True)
    if not target.is_dir():
        raise ValueError(f"Not a project directory: {target}")
    items = []
    if not agents_only:
        for skill in sorted((package / "skills").iterdir()):
            if (skill / "SKILL.md").is_file():
                items.append(("link", target / ".agents/skills" / skill.name, skill))
    for source in sorted((package / "agents").glob("*.toml")):
        content = source.read_text()
        # Give installed roles a concrete package pointer without changing policy.
        marker = 'developer_instructions = """\n'
        content = content.replace(marker, marker + f"Pstack package root is {json.dumps(str(package))}.\n", 1)
        items.append(("file", target / ".codex/agents" / source.name, content))
    conflicts = []
    pending = []
    for kind, dest, value in items:
        for parent in dest.parents:
            if parent == target:
                break
            if parent.is_symlink() or (parent.exists() and not parent.is_dir()):
                conflicts.append(f"Unsafe parent path: {parent}")
                break
        else:
            conflicts.append(f"Destination outside target: {dest}")
        if dest.is_symlink():
            if kind == "link" and dest.resolve() == value.resolve():
                continue
            conflicts.append(f"Existing symlink differs: {dest}")
        elif dest.exists():
            if kind == "file" and dest.is_file() and dest.read_text() == value:
                continue
            conflicts.append(f"Existing path differs: {dest}")
        else:
            pending.append((kind, dest, value))
    if conflicts:
        raise ValueError("Installation refused before writing:\n" + "\n".join(sorted(set(conflicts))))
    return pending


def install(target, package=PACKAGE, agents_only=False, dry_run=False):
    pending = plan_install(target, package, agents_only)
    if dry_run:
        return [str(dest) for _, dest, _ in pending]
    created = []
    try:
        for kind, dest, value in pending:
            dest.parent.mkdir(parents=True, exist_ok=True)
            # Recheck containment and use exclusive creation for races/conflicts.
            if not dest.parent.resolve().is_relative_to(Path(target).resolve()):
                raise ValueError(f"Destination parent escaped target: {dest.parent}")
            if kind == "link":
                os.symlink(value, dest, target_is_directory=True)
            else:
                with dest.open("x") as stream:
                    stream.write(value)
            created.append(dest)
    except BaseException:
        for dest in reversed(created):
            dest.unlink()
        raise
    return [str(dest) for dest in created]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path, required=True)
    parser.add_argument("--agents-only", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        paths = install(args.target, agents_only=args.agents_only, dry_run=args.dry_run)
    except (ValueError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print(json.dumps({"dry_run": args.dry_run, "paths": paths}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
