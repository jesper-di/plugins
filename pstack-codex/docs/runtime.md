# Codex runtime contract

Every pstack skill reads this contract before running. It supplements the actual
host's instructions; it cannot override them or authorize external actions.

## Discovery and context

Skills are discovered from native plugin packages or `.agents/skills/`. Their
metadata is discoverable; the full body and references load when relevant.
Use `$skill-name`, the picker, or an explicit request. Read referenced leaves
before relying on their instructions. Resolve paths relative to the installed
skill or package, not a presumed `pstack-codex/` directory in the target project.
Examples using that prefix describe this fork's checkout layout.

Native plugin skills are namespaced, for example `$pstack-codex:poteto-mode`.
Project-linked skills use `$poteto-mode`. Short skill names inside this package
refer to its own leaves; resolve them through the live catalog, using the plugin
namespace when present, rather than invoking an unrelated same-name skill.

Repository-wide instructions come from the target project's `AGENTS.md`.
Nested instructions apply within their scope. Installing a plugin does not
automatically import its `AGENTS.md` into another repository's root context.

## Native agents and tool APIs

Use exposed Codex tools for spawning, waiting, steering, and stopping agents.
Inspect the actual schema; do not pass Cursor background/environment parameters.
Custom standalone agents live in the target `.codex/agents/` directory and define
`name`, `description`, and `developer_instructions`. Installation of a skills
plugin alone is not a promise of custom-agent discovery.

When native roles are unavailable, include their scoped instructions in a
supported generic spawn or perform the workflow directly. Delegate only when
the user or applicable instructions call for it and the host permits it.
State when required independent review could not be performed.

Parent-model and reasoning-effort inheritance is the default. No vendor-specific
model names or budget-to-model guesses are supplied. Use overrides only when
explicitly configured and available in the live host. Multiple same-model
attempts are independent attempts, not model diversity. Rejected model requests
are reported, not silently switched to an invented equivalent.

## Permissions and shared state

Use the host's permission model and existing authorization. Do not disable
sandboxing, request broader permissions by default, or treat the plugin as
permission to post messages, merge, deploy, purge data, or force-push shared work.
Honor already authorized actions without redundant approval requests.

Agent role files can request read-only execution, but live parent overrides and
host behavior determine effective enforcement. Read-only roles also prohibit
external writes in their instructions; filesystem restrictions alone cannot
restrict connector mutations. Never describe role text as a security boundary.

Agents may share one filesystem and branch. One writer owns each overlapping
file, branch, or runtime state. Disjoint output paths or separately provisioned
workspaces are required for independent writing. Spawning is not a promise of
a new VM, worktree, container, Kubernetes namespace, or durable remote job.

## Budgets, plans, and progress

Read optional `.codex/pstack.toml` at task start. Version 1 supports `budget`
(`small`, `medium`, `large`) and `model_policy = "inherit-parent"`. Small favors
a direct pass, medium uses two candidates/reviewers when worthwhile, large uses
more independent coverage within host limits. Budgets never remove required
checks or configure model effort or access.

Use the exposed plan tool instead of a presumed todo API. Communicate meaningful
findings and decisions regularly. Watchers are ordinary bounded processes; keep
the parent responsive and use resumable waits rather than long blocking sleeps.

No persistent loop is assumed. A long task runs while its session is active.
Durable re-entry requires an available, explicitly configured scheduler or job
runner. If absent, checkpoint and explain the missing capability. A restarted
session reconstructs state from artifacts and live checks, not stale agent IDs.

## Evidence and unavailable integrations

Use actual shell, browser, simulator, connector, or project harness tools.
Missing tools are reported validation gaps, not successful checks. Access a
transcript only when the host exposes an authorized path or the user supplies it;
otherwise use conversation context. Never scan unrelated global histories.

For legacy playbooks, references to cloud workers, ten live lanes, trunk reads,
or external status messages are requirements to adapt to the task and host.
Use the actual base branch and installed package path; do not assume plugin files
are committed in the target repository. Scope runtime/performance checks to the
change, and record an evidence-based not-applicable reason for dimensions that
do not apply. Never fake a baseline, screenshot, independent reviewer, scheduler,
or merged state merely to fill a checklist.
