---
name: setup-pstack
description: "Configure pstack for native Codex skills, agent roles, and a project-scoped workflow budget. Use when explicitly asked to set up pstack."
---

Read the [Codex runtime contract](../../docs/runtime.md) before following this workflow.

# Set up pstack for Codex

1. Inspect the project instructions, installed skills, available spawn tools,
   and existing `.codex/pstack.toml`. Do not dump credentials or unrelated user
   configuration. Model availability comes from the live host, not a hardcoded list.
2. Use the bundled `scripts/install.py --target <project>` if repository skill
   discovery is wanted. A marketplace installation already supplies skills;
   use `--agents-only` when adding just the native agent definitions. Preview
   with `--dry-run`; never replace conflicting skills or agent files.
3. Default to inheriting the current model and effort. If the user wants a
   workflow budget, offer small, medium, or large. These control review breadth
   and candidate count, not model entitlements, reasoning effort, or permissions.
4. For an explicit request to configure pstack, write `.codex/pstack.toml` with
   `version = 1`, `budget = "medium"`, and `model_policy = "inherit-parent"`, or
   the user's chosen budget. Preserve unrelated tables and existing preferences.
   Read this file at the start of pstack tasks; it is application configuration,
   not a Codex rule or a `config.toml` replacement.
5. Configure an available model or effort only when requested, using the host's
   supported spawn fields or native `.codex/agents/<role>.toml` fields. Never
   fabricate a model identifier, translate vendor slugs, or silently select a
   different model after rejection. Report the limitation and use the parent
   model only if that fallback satisfies the requested task.
6. Tell the user which paths changed and to start a new session for discovery.
   Verify visibility in that session before claiming activation. If no runtime
   proof harness exists, suggest `$create-verification-skill` when it would help.
