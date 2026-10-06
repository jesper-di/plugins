# Validation of version 0.1.0

Validated in the authoring environment with Codex CLI
`0.159.0-alpha.3`, Python `3.12.14`, Node `24.19.0`, and Bun `1.3.11`.

- Package validation passed for manifests, 55 plugin skills, optional operations
  skill metadata, four native agent definitions, local links, and host dependencies.
- Six Python checks passed, exercising project discovery paths, installer
  idempotence, dry runs, agents-only mode, conflict preservation, unsafe parent
  symlinks, and worktree paths/data retention.
- Five Node checks passed for concrete plan acceptance and rejection of missing
  evidence, unexplained non-applicability, placeholders, and fenced-only examples.
- All 52 inherited orchestration/PR-watcher tests passed. The watcher's strict
  TypeScript check passed using the pinned dependency lockfile.
- Native local-marketplace installation succeeded. A fresh read-only app-server
  `skills/list` request discovered all 55 namespaced skills, enabled, with no
  package parsing errors. No model task or subagent was launched for that check.

The remote catalog was unavailable in this environment; local installation and
discovery were checked using explicit per-command marketplace configuration.
Live connector workflows, custom-agent execution, browser verification,
cross-model review, and durable unattended scheduling were not exercised.
Installing in this execution environment does not refresh this conversation's
already supplied skill catalog or install anything on the user's computer.
