#!/usr/bin/env python3
"""Read-only worktree inventory; no global transcript scans or deletion."""

import argparse
from pathlib import Path
import json
import subprocess


def git(repo, *args, required=True):
    result = subprocess.run(["git", "-C", str(repo), *args], capture_output=True)
    if required and result.returncode:
        raise ValueError(result.stderr.decode(errors="replace").strip())
    return result.stdout.decode(errors="replace") if result.returncode == 0 else None


def audit(repo, base=None, transcripts=None):
    repo = Path(repo).resolve(strict=True)
    if base is None:
        base = git(repo, "symbolic-ref", "--quiet", "refs/remotes/origin/HEAD", required=False)
        base = base.strip() if base else None
    base_sha = git(repo, "rev-parse", "--verify", base + "^{commit}", required=False) if base else None
    history = Path(transcripts).resolve(strict=True) if transcripts else None
    if history and not history.is_dir():
        raise ValueError("Transcript path must be an explicitly authorized directory")
    rows = []
    for block in git(repo, "worktree", "list", "--porcelain", "-z").split("\0\0"):
        fields = dict(field.split(" ", 1) if " " in field else (field, True)
                      for field in block.split("\0") if field)
        if "worktree" not in fields:
            continue
        path = Path(fields["worktree"])
        status = git(path, "status", "--porcelain=v1", "-z", required=False)
        head = git(path, "rev-parse", "HEAD", required=False)
        merged = None
        if base_sha and head:
            result = subprocess.run(["git", "-C", str(repo), "merge-base", "--is-ancestor",
                                     head.strip(), base_sha.strip()], capture_output=True)
            merged = result.returncode == 0 if result.returncode in (0, 1) else None
        chats = []
        if history:
            for chat in history.rglob("*.jsonl"):
                if chat.is_symlink():
                    continue
                try:
                    text = chat.read_text(errors="replace")
                    if str(path) + "/" in text or str(path) + '"' in text:
                        chats.append(str(chat))
                except OSError:
                    continue
        rows.append({"path": str(path), "head": head.strip() if head else None,
                     "branch": fields.get("branch"), "dirty": bool(status) if status is not None else None,
                     "ancestor_of_base": merged, "base": base,
                     "matching_transcripts": chats,
                     "recommendation": "hold" if status or status is None else "review"})
    return rows


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", nargs="?", default=".")
    parser.add_argument("--base", help="Explicit base ref; defaults to local origin/HEAD when known")
    parser.add_argument("--transcripts", help="Explicitly authorized transcript directory; omitted by default")
    args = parser.parse_args()
    try:
        print(json.dumps(audit(args.repo, args.base, args.transcripts), indent=2))
    except (ValueError, OSError) as exc:
        parser.exit(1, str(exc) + "\n")
