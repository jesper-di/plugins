---
name: control-ui
description: "Verify a real browser or native UI through available browser, screenshot, accessibility, or simulator tools."
---

Read the [Codex runtime contract](../../docs/runtime.md) before following this workflow.

# Verify a UI

Identify the actual surface and available control tools. Use a project harness,
browser automation, accessibility actions, or simulator tools supported by the
host. Launch the app using its documented setup and isolated data. Exercise the
changed user flow, observe the end state, and capture relevant screenshots,
console errors, and state evidence. For regressions or visual parity, compare
base and head under the same conditions. If the required surface cannot be driven,
report the gap and provide a reproducible check; never claim UI proof from a
source inspection or unrelated screenshot. Do not assume browser tools exist.
