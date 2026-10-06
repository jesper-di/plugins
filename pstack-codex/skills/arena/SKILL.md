---
name: arena
description: "Compare independent candidate solutions, select a base, and integrate justified improvements. Use for design or implementation alternatives."
---

Read the [Codex runtime contract](../../docs/runtime.md) before following this workflow.

# Arena

1. Frame the artifact and a concrete rubric with three to six criteria. Read the
   grounding evidence. Update the plan before launching work.
2. Request at least two structurally distinct candidates. Use `poteto-agent` for
   builders and explicit output paths. Each candidate gets the same task and
   grounding. Inherit the parent model unless the user configured available
   alternatives. Multiple runs of one model are independent attempts, not a
   multi-model panel.
3. Isolate writes using disjoint output directories or operator-provisioned
   workspaces. Never assume a spawn creates a worktree, VM, or container.
   Respect the host's concurrency cap and collect all outcomes, including failures.
4. After candidates stop writing, have a `pstack-reviewer` score them against
   the rubric. The parent also reads every candidate. If delegation is unavailable,
   generate and compare sequential candidates and state that limitation.
5. Choose the strongest base; record criterion scores and rejected alternatives.
   Integrate only justified improvements from other candidates; preserve a coherent
   design rather than averaging incompatible approaches.
6. Validate the final artifact against the actual requirement. Record the base,
   grafts, rejections, dropouts, and evidence in a synthesis note.
