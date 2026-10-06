#!/usr/bin/env bash
# Read-only inventory. History scanning requires an explicit authorized path.
set -euo pipefail
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$script_dir/worktree_audit.py" "$@"
