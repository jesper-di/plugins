---
name: automate-me
description: "Capture explicitly requested working preferences in a native Codex skill or scoped AGENTS.md guidance."
---

Read the [Codex runtime contract](../../docs/runtime.md) before following this workflow.

# Capture a working style

1. Read the current conversation, authorized examples, and existing project
   skills. Do not mine unrelated private sessions. Identify repeated preferences,
   corrections, and successful workflows; distinguish habits from one-off needs.
2. For a new skill, use `.agents/skills/<handle>-mode/SKILL.md`. Preserve an
   existing skill's path when updating it. Ask only for missing preferences that
   materially change the result; use reasonable defaults for routine choices.
3. Use `$create-skill` to write the workflow and `$unslop` to tighten it. Use
   `agents/openai.yaml` with `allow_implicit_invocation: false` when invocation
   should be explicit. Do not emit Cursor mode metadata or `.mdc` rules.
4. If persistence across tasks was requested, add concise scoped guidance to the
   project's `AGENTS.md`, preserving existing instructions. A skill still loads
   on demand; do not claim every file is always in context.
5. Validate the file and a representative task or example. Report what was
   inferred, where it was saved, and how to invoke it in a new Codex session.
