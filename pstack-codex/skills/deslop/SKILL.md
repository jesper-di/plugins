---
name: deslop
description: "Review a scoped code diff before commit for accidental complexity, redundant checks, dead paths, and unsupported abstractions."
---

Read the [Codex runtime contract](../../docs/runtime.md) before following this workflow.

# Clean a code diff

Read the requested diff and surrounding contracts. Remove dead paths, one-use
wrappers that obscure flow, redundant validation inside trusted boundaries,
unused imports, and speculative abstractions when that improves the actual
behavior. Preserve security boundary checks and public compatibility requirements.
Prefer domain structures over branching patches. For a review-only task, report
findings without applying them. For requested cleanup, make the smallest scoped
change and run behavior checks appropriate to it. Do not disable hooks, erase
unrelated edits, or add broad formatting churn.
