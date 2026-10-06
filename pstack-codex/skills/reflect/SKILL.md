---
name: reflect
description: "Extract durable lessons from the current authorized conversation and propose or make requested improvements to skills and structural checks."
---

Read the [Codex runtime contract](../../docs/runtime.md) before following this workflow.

# Reflect

1. Use the current conversation or a user-supplied, authorized transcript. Do not
   search unrelated sessions or guess a global transcript path. If no transcript
   is exposed, write a concise digest from available conversation context.
2. Review judgment, tooling, and alternative explanations using
   `references/judgment-reviewer.md`, `references/tooling-reviewer.md`, and
   `references/divergent-reviewer.md`. Independent `pstack-reviewer` tasks may
   handle these lenses; otherwise work sequentially and disclose the limit.
3. Synthesize with `references/synthesizer.md` into Accepted / Rejected / Backlog.
   Prefer a type, lint, script, or runtime check over repeated instructions.
4. For a reflection request, deliver proposals. If the user already requested
   applying the lessons, make scoped reversible changes without an extra approval
   ceremony. Use `$create-skill` for substantial skill edits. External issue filing
   or team messaging requires its own authorization.
5. Validate touched skills and report changes, evidence, rejected ideas, and
   remaining work. Never claim to mine a transcript that was not available.
