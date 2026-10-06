---
name: swarm
description: "Partition independent work into a coverage matrix and coordinate native Codex workers. Use for parallel review, exploration, races, or disjoint implementation."
---

Read the [Codex runtime contract](../../docs/runtime.md) before following this workflow.

# Swarm

1. Define the goal and a coverage matrix. Each lane has an owner, scope, input
   artifact or exact SHA, pass predicate, and evidence destination.
2. Choose the smallest useful fan-out within the live host's limits. The default
   budget is medium: two review/candidate lanes when multiple views are needed.
   A named coverage matrix retains every required lane, processing in waves if
   necessary. Budget never removes a required acceptance criterion.
3. Use `pstack-explorer`, `pstack-reviewer`, or `poteto-agent` as appropriate.
   Send the full task plus corrections and repository instructions. Specify
   disjoint writer ownership. A shared workspace must have only one writer for
   any overlapping files, branch, or runtime state.
4. Spawn through available Codex tools, track returned IDs, wait without busy
   polling, and collect failures as well as successes. Models inherit by default.
   Do not pass Cursor-specific background or environment fields.
5. Review every output and artifact. Verify claims against evidence, deduplicate
   findings, resolve conflicts, and return one integrated report. The parent owns
   the result, including unverified lanes and dropped workers.

If delegation is unavailable, perform lanes sequentially and disclose that
there was no independent review. A role instruction is not a sandbox boundary.
