---
name: no-comments
description: "Review scoped comments and suppressions using the native comment-sicko role, preserving public contracts and correctness constraints."
---

Read the [Codex runtime contract](../../docs/runtime.md) before following this workflow.

# Review comments

1. Select the caller's files or diff against the actual base branch.
2. Ask the native `comment-sicko` reviewer to identify redundant narration,
   commented-out code, and suppressions. The reviewer is read-only and returns
   findings; it does not remove comments. Use the role's instructions directly
   if custom agents are unavailable.
3. Read surrounding code before accepting a deletion. Preserve license headers,
   public API contracts, substantiated platform constraints, and issue/RFC links
   that explain behavior code cannot express. Uncertainty is a reason to
   investigate, not authorization to delete a safety constraint.
4. Trace correctness-related suppressions to root causes. Use `$how`, `$why`,
   and `$architect` when needed. Apply only authorized, in-scope fixes and
   verify changed behavior. A review-only request remains review-only.
5. Report accepted and rejected findings, edits, validation, and unresolved
   constraints. Do not broaden the task into unrelated refactoring.
