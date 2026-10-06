# Porting notes

The source revision and version are pinned in `UPSTREAM.json`. The 51 original
skill concepts remain, with rewritten host-dependent workflows and four bundled
skills replacing external authoring, cleanup, and control dependencies.

| Upstream element | Native replacement |
| --- | --- |
| Plugin installation command | Native marketplace manifest and Codex plugin commands, or project installer. |
| Slash skill commands | Explicit skill requests and `$name` examples. |
| Custom-mode metadata | Explicit-only policy in `agents/openai.yaml`; no persistent mode claim. |
| Always-applied model rule | `.codex/pstack.toml` workflow preferences, read by skills. |
| Vendor model routing | Parent inheritance or explicitly configured available models. |
| Markdown named subagents | Standalone native TOML agents in project `.codex/agents/`. |
| Background/environment spawn fields | Actual exposed Codex spawn API; shared-state ownership rules. |
| Built-in authoring and team-kit dependencies | Bundled authoring, code cleanup, CLI, and UI skills. |
| Persistent loop and automation editor | Active-session supervision or an explicitly configured external dispatcher. |
| Global transcript layout | Only host-exposed or supplied in-scope transcripts, with conversation-digest fallback. |

Comment review now returns read-only findings and preserves uncertain safety
constraints while investigating them. Reflection respects the task's existing
authorization and does not automatically file external backlog issues. Reviewers
do not claim that multiple parent-model instances constitute a multi-model panel.

The PR watcher, ledger, and decision-log tools retain their upstream algorithms
and meaningful tests. Bugbot author recognition remains compatible with GitHub
bot accounts; those account names are data, not a dependency on a particular IDE.
The plan validator checks scoped units, acceptance criteria, and evidence or
justified non-applicability instead of imposing a fixed lane count and unavailable
loop command. Worktree audit accepts an explicit transcript directory and otherwise
skips history scanning. It performs no network fetches or deletions and handles
Git worktree paths containing spaces.

Benny remains an optional operations pack, separate from plugin skill discovery.
Issue connectors and event/job dispatch must actually exist before activating it.
Likewise, `make-bot-ui` requires a real configured webhook contract.

## Validation boundaries

Package checks cover manifests, skill metadata, local references, agent TOML,
installer safety, and forbidden host-specific execution instructions. Runtime
tool tests exercise the actual local ledger and watcher logic using their fakes.
Client marketplace loading is checked separately. No cross-model task, live
GitHub watcher, Slack automation, browser session, or unattended overnight run is
claimed from static checks.

## Primary references

- [Native plugin packaging](https://developers.openai.com/plugins/build/plugins).
- [Codex skills](https://developers.openai.com/codex/skills).
- [Custom agents and permission inheritance](https://developers.openai.com/codex/subagents).
- [Plugin installation](https://developers.openai.com/codex/plugins).
