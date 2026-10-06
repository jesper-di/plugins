---
name: create-skill
description: "Author or revise a native Codex skill with concrete triggers, focused workflow instructions, and validated support files."
---

Read the [Codex runtime contract](../../docs/runtime.md) before following this workflow.

# Author a native Codex skill

1. Define the user's recurring task, when the skill should trigger, and its
   deliverable. Inspect nearby conventions and existing skills first.
2. Create `.agents/skills/<kebab-name>/SKILL.md` with YAML frontmatter containing
   `name` and `description`. Keep the name equal to the directory name.
3. Write a focused workflow. Keep long references in `references/` and reusable
   executable tools in `scripts/`. Use relative links that stay in the package.
4. For explicit-only invocation, add `agents/openai.yaml` containing
   `policy: {allow_implicit_invocation: false}`. Do not emit custom-mode metadata.
5. Ground the workflow in actual tools and capabilities. Preserve host instruction
   precedence, authorization, secret handling, and repository boundaries.
6. Validate metadata, links, scripts, and a representative usage example. Check
   discovery in a fresh client session separately from static validation.
