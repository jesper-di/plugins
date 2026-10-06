# Benny for Codex

An optional report-triage and issue-reproduction operations pack. Start with
[FOR_AGENTS.md](FOR_AGENTS.md) and [setup](skills/setup-benny/SKILL.md).

The two operational workflows and their reference templates are adapted from
upstream pstack. They require configured read/write capabilities, source routing,
verification controls, and an actual dispatcher. No scheduling or webhook backend
is provided by this plugin. Do not register this entire directory as a skill
root; a configured job reads its exact operational instruction file.

Activation, messaging, tracker mutations, and unattended runs require explicit
authorization. Keep configuration and secrets separate from the copied pack.
