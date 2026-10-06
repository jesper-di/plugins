# Benny entry point for Codex

This optional operations pack triages reports and reproduces confirmed issues.
Read the package runtime contract and `skills/setup-benny/SKILL.md` first.
This directory is not part of registered plugin skill discovery.

Use only configured issue/chat connectors and an actual authorized dispatcher.
Copy the pack into `.codex/automations/benny/` only when requested; preserve local
changes and keep user-owned configuration outside it, for example `.codex/benny/`.
Keep secrets in the runtime secret manager. Skill files do not create webhooks,
automation jobs, or connector permissions. Do not activate external messaging,
tracker writes, or recurring jobs without authorization for those operations.

The triage and reproduction workflows retain upstream source-coordinate,
deduplication, routing, and evidence rules. Never mistake prompt constraints for
enforced connector write isolation. If workers cannot be restricted appropriately,
keep the work with one coordinator and the permitted tool surface.
