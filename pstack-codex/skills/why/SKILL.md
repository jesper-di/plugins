---
name: why
description: "Investigate why a design exists using source control and available read-only evidence sources. Use for design rationale, regressions, or historical constraints."
---

Read the [Codex runtime contract](../../docs/runtime.md) before following this workflow.

# Why a design exists

1. Frame the concrete question. Read the code and trace behavior with `$how`
   when needed. Identify the current design and its alternatives.
2. Inspect available read-only sources: Git history, PRs, issues, documentation,
   incident records, and connected services. Consult `references/source-playbook.md`
   and the relevant `references/sources/` guides. Missing connectors are missing
   evidence; do not invent MCP servers or enumerate private credential files.
3. Use one `pstack-explorer` per independent source when delegation is supported
   and worthwhile. Use `references/investigator-prompt.md`. Inherit the parent
   model and live permissions; no claim that read-only mode removes MCP tools.
4. Synthesize with `references/synthesizer-prompt.md` and apply
   `references/epistemics.md`. Ground every factual rationale in a citation;
   distinguish documented intent, observed behavior, and inference.
5. Return the explanation, sources consulted, gaps, and Preserve / Change /
   Avoid / Risk constraints when the answer will guide a code change.

Connector access is read-only for this investigation. Finding a chat source does
not authorize messaging it or filing issues.
