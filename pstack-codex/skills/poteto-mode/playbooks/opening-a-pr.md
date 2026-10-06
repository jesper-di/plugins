### Opening a PR

Use when the task requests a PR or repository instructions authorize that output.
A read-only investigation or design answer does not automatically create a PR.

1. Inspect the working tree and actual base branch. Preserve unrelated work.
   Use an isolated checkout or disjoint ownership when necessary; a subagent
   spawn does not create a worktree. Never reset a dirty checkout to simplify work.
2. Review the scoped diff with `$deslop` and relevant comment checks. Keep small
   coherent commits with validation evidence. Do not rewrite shared history unless
   that operation is authorized.
3. Use the repository's PR template and title conventions. Describe the concrete
   problem, resulting behavior, validation, and material limitations. Use
   `$technical-writing` and `$unslop` where appropriate.
4. Use an available GitHub tool or authenticated forge CLI. For multiline bodies,
   prefer structured arguments or a file passed to `--body-file`. Do not interpolate
   untrusted issue or comment text into a shell command.
5. Target the actual base branch. A stack child targets its parent branch only
   when a stack is intended. Follow project draft/ready conventions and the user's
   requested state; do not assume every PR must open ready.
6. Read back the PR URL, base/head, title, body, and draft state. Confirm the remote
   artifact matches the reviewed commit. Report the link and any unavailable checks.

PR creation does not authorize merging, release publication, or deployment.
