---
name: recall
description: "Rebuild working context from authorized conversation history, Git state, and available shared evidence before resuming work."
---

Read the [Codex runtime contract](../../docs/runtime.md) before following this workflow.

# Recall

1. Fix the topic, project, and time scope. Prefer a supplied state capsule or the
   current conversation. Read only transcript paths explicitly exposed by the
   host or supplied for the task; never search global histories across projects.
2. Extract goals, decisions, corrections, unfinished work, branches, and artifacts.
   Cite available message IDs or transcript references. If history is missing,
   state that and reconstruct from repository state instead.
3. Use `$why` for shared evidence around a named subsystem or recurring bug.
   Skip unavailable connectors and report the resulting gaps.
4. Verify branches, commits, PRs, and issues against live state. Use focused
   explorers for a large authorized corpus, with scoped file pointers.
5. Return a short capsule, per-thread status, recurring problems, and the next
   concrete move. Distinguish merged, open PR, in flight, verified/uncommitted,
   reverted, and planned work. Exclude adjacent topics unless they block the task.
