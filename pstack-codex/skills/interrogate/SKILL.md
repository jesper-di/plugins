---
name: interrogate
description: "Adversarially review a scoped change with independent Codex reviewers and synthesize evidence-backed findings without auto-applying edits."
---

Read the [Codex runtime contract](../../docs/runtime.md) before following this workflow.

# Interrogate

1. Identify the requested files or diff and exact base/head. Include working-tree
   changes when they are in scope. State the intended behavior in one paragraph.
2. Fill `references/reviewer-prompt.md` with the intent, relevant context,
   `references/rubric.md`, and `references/code-quality-review.md`.
3. Send the same packet to independent `pstack-reviewer` tasks. Default to two
   reviewers for a substantial change, within host limits. Inherit the parent
   model; use user-configured alternatives only if available. Never claim model
   diversity from two instances of one model. Reviewers make no writes.
4. Deduplicate findings, inspect evidence and disputed claims, and spot-check
   against the artifact. Independent agreement is a signal, not proof.
5. Return Critical, Concerns, Noted, and Dismissed findings with locations,
   rationale, validation limits, and an agreement map. Use
   `references/lead-judgment.md` when resolving tradeoffs.

The deliverable is a review. Do not auto-apply fixes or post review comments to
external services unless requested. If delegation is unavailable, review directly
and label the missing independent second opinion.
