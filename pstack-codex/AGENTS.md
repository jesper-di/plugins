# Working on pstack for Codex

Read `README.md`, `docs/runtime.md`, and `docs/porting.md` before editing.
This directory is the Codex edition; preserve the original `../pstack/` package.

Keep skills native to the actual host. Do not reintroduce vendor-specific model
slugs, presumed spawn parameters, rule formats, or unimplemented scheduler APIs.
Agent instructions do not grant credentials, privileges, or kernel isolation.
Check `.agents/plugins/marketplace.json` at the repository root after manifest
changes. Preserve upstream license attribution and `UPSTREAM.json` provenance.

Run `python scripts/validate.py` and `python -m unittest discover -s tests` from
this directory after package or installer changes. Also run
`node --test tests/check-plan.test.mjs` after plan-validator changes. Run the bundled runtime tool
tests after editing those tools. Report static validation separately from client
activation and live integration checks.
