### Feature

1. Trace affected behavior with `$how` and rationale with `$why` when relevant.
2. Name the data shape, its owner, and public usage. Use `$architect` for changes
   spanning interfaces and `$arena` when independent alternatives are worthwhile.
3. Record blocking prerequisites, independent workstreams, shared-state boundaries,
   and checks. Mark genuinely inapplicable dimensions with a reason.
4. Implement within the requested scope. Use native workers for disjoint units
   when supported; keep one writer for overlapping files and branch state. If
   delegation is unavailable, implement directly and report the missing independent
   review rather than pretending a second agent participated.
5. Verify the real resulting behavior and relevant failure paths. Use the project
   harness or `$control-cli`/`$control-ui`. Match tests to meaningful behavior,
   and run performance checks when the change makes a performance claim or risk.
6. Review the artifact, fix confirmed defects, and report evidence and limitations.
   Follow opening-a-pr only when that output is requested or authorized.
