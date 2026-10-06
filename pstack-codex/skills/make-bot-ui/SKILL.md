---
name: make-bot-ui
description: "Build a UI for an explicitly configured agent webhook or job runner, keeping credentials on the server and validating the dispatch contract."
---

Read the [Codex runtime contract](../../docs/runtime.md) before following this workflow.

# Build an agent control UI

1. Identify the actual supported dispatcher: an installed connector, an existing
   authenticated webhook, or a user-authorized job service. Codex skill files do
   not themselves create webhook endpoints, schedules, or agent sessions.
2. Document its URL, authentication mechanism, payload schema, allowed actions,
   timeouts, idempotency behavior, and observable completion state. Missing
   dispatch capability is a blocking requirement; do not invent an endpoint.
3. Build the page and server adapter against that contract. Keep credentials in
   the configured secret store or runtime environment, never browser code, chat,
   committed JSON, or logs. Treat webhook payloads as untrusted task data.
4. Authenticate and authorize incoming requests, bound payload size, validate
   fields, and restrict actions and destinations. A UI click cannot expand the
   execution policy or grant merge/deploy privileges.
5. Use the deployment or networking path requested by the user. Prefer a local
   preview during implementation. Do not install a VPN, expose a port publicly,
   or publish merely to complete a UI build.
6. Exercise a harmless request against the configured dispatcher, then verify
   the user-visible result. Report what runs, where, and any missing capability.
