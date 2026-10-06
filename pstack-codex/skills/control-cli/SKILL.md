---
name: control-cli
description: "Exercise a real CLI or TUI through available shell or terminal tools and capture exit status, output, and relevant state changes."
---

Read the [Codex runtime contract](../../docs/runtime.md) before following this workflow.

# Verify a CLI

Identify the built artifact, supported commands, and isolated test data. Run the
actual user flow through available shell tools; use a PTY only when interaction
requires it. Capture exit status, output, and observable state changes. Test the
changed success and failure paths against explicit expectations. For regressions,
compare base and head under comparable conditions. Bound processes and clean up
only resources created for this verification. Do not substitute compilation for
runtime evidence or require an unavailable control tool by name.
