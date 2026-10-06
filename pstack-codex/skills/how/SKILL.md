---
name: how
description: "Trace and explain how a subsystem behaves, with code and runtime evidence. Use for walkthroughs, grounding, or how a feature works."
---

Read the [Codex runtime contract](../../docs/runtime.md) before following this workflow.

# How a subsystem works

1. Name the question and scope. Identify entry points, data, state ownership,
   calls, boundaries, failure paths, and the observable end state.
2. Read relevant code and run the smallest useful observation. Do not substitute
   filenames for a traced behavior model.
3. For independent subsystems, delegate to `pstack-explorer` with
   `references/explorer-prompt.md`, scoped file pointers, and the question.
   Use the live spawn interface. For a small scope or unavailable delegation,
   explore directly. Explorers make no repository or external writes.
4. Synthesize using `references/explainer-prompt.md`. An independent explorer
   may verify the synthesis when the task warrants it. Models inherit by default.
5. Explain the actual flow in plain language, citing files, symbols, and observed
   behavior. State uncertainty and checks that were unavailable. Distinguish
   observed behavior from conclusions inferred from source.
