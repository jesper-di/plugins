# Pstack for Codex

A native Codex edition of [pstack](../pstack/README.md), preserving its grounding,
design, review, and verification workflows. The original Cursor package remains
in `pstack/`. See [UPSTREAM.json](UPSTREAM.json) for the pinned source revision
and [LICENSE](LICENSE) for upstream attribution.

## Install into a project

From a checkout of this fork:

```sh
python pstack-codex/scripts/install.py --target /absolute/path/to/project --dry-run
python pstack-codex/scripts/install.py --target /absolute/path/to/project
```

The installer links skill directories under the project's `.agents/skills/` and
writes four standalone native agent definitions under `.codex/agents/`. It
preserves existing instructions and configuration, rejects conflicts before
writing, and does not change permissions, model settings, or global config.
Keep this checkout available: the skill links point to it.

Start a new Codex session in the target project and confirm skill visibility.
Then invoke:

```text
$setup-pstack
$poteto-mode implement the requested change and verify the real behavior.
$interrogate review this branch against its base.
```

Use the skill picker or explicit name if your client does not accept dollar
syntax. Installation in an execution environment does not automatically update
the skill catalog of a running cloud chat.

## Install as a native plugin

Clients supporting local or Git marketplaces can use this repo's native catalog:

```sh
codex plugin marketplace add jesper-di/plugins --ref codex/pstack-native
codex plugin add pstack-codex@jesper-codex-plugins
```

Use `/plugins` in the interactive CLI if your version provides a browser instead
of `plugin add`. Start a new session after installing. For local development,
register the repository root with `codex plugin marketplace add /path/to/plugins`.

Marketplace skills are namespaced. For that installation, invoke
`$pstack-codex:setup-pstack`, `$pstack-codex:poteto-mode`, or
`$pstack-codex:interrogate`. Project-linked skills use the short names above.

The plugin supplies skills. To add custom agents to a target project separately:

```sh
python pstack-codex/scripts/install.py --target /absolute/path/to/project --agents-only
```

Do not use both marketplace installation and project skill links for the same
skills in one session; use `--agents-only` with a marketplace installation.

## What's native

- 51 adapted upstream skills, plus `create-skill`, `deslop`, `control-cli`, and
  `control-ui` to replace host-specific dependencies.
- 23 playbooks with native delegation, lifecycle, and authorization guidance.
- TOML definitions for `poteto-agent`, `comment-sicko`, `pstack-reviewer`, and
  `pstack-explorer`. Models and effort inherit by default.
- Explicit-only skill invocation uses `agents/openai.yaml`.
- Optional project workflow preferences live in `.codex/pstack.toml`.
- Existing PR watcher, orchestration ledger, plan validator, and decision-log
  tools remain ordinary local tools. They do not create agents or schedules.
- Benny's optional issue-triage pack uses configured connectors and an actual
  dispatcher; it does not fabricate a native automation backend.

Read the [runtime contract](docs/runtime.md) and [porting notes](docs/porting.md)
for platform limits. Native agent definitions depend on current client support;
skills can follow the same roles sequentially when custom agents are unavailable.

## Verify the package

```sh
cd pstack-codex
python scripts/validate.py
python -m unittest discover -s tests
node --test tests/check-plan.test.mjs
cd skills/poteto-mode/scripts
bun install --frozen-lockfile
bun test orch watch-pr
bun run typecheck
```

Static checks and tool tests establish package integrity and local behavior.
They do not prove that every connector, client, cluster, or workflow is available.
