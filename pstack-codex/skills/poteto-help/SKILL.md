---
name: poteto-help
description: "Explain the native Codex pstack workflows, setup, invocation, capabilities, and limitations. Use when explicitly asked for pstack help."
---

Read the [Codex runtime contract](../../docs/runtime.md) before following this workflow.

# Pstack help

Find out what the user is trying to accomplish. Read the relevant skill and
playbook before describing it. Point to the installed file or the fork's public
copy, not an upstream Cursor guide that describes another host.

- Setup and model policy: `$setup-pstack` and `docs/runtime.md`.
- Full engineering workflow: `$poteto-mode` and its `playbooks/` index.
- Behavior and rationale: `$how`, `$why`, and `$teach`.
- Design alternatives: `$architect` and `$arena`.
- Independent review: `$interrogate`; parallel partitions: `$swarm`.
- Proof harness: `$create-verification-skill`, `$control-cli`, `$control-ui`.
- Cleanup: `$deslop`, `$no-comments`, `$unslop`.
- Lessons and context: `$reflect`, `$recall`, `$correct`, `$automate-me`.
- Durable decision trail: `$show-me-your-work`.

Give a concrete prompt appropriate to the task. Native examples use `$skill-name`
or the skill picker; no assumed slash command, custom mode, or persistent loop.
Models inherit unless explicitly configured from available choices. Background
work, schedules, connector access, and custom agents depend on the actual host.
Explain those limits before promising the corresponding capability.
