### Autopilot full

Use for independently deliverable units driven through verification. Merging is
included only when explicitly authorized; otherwise stop at merge-ready output.

1. Define unit outcomes, dependencies, ownership, authorization, and acceptance
   criteria. Use the actual base branch and available forge integration.
2. Give each native worker a bounded unit and separately provisioned workspace
   or disjoint write scope. Do not assume a cloud VM or branch is created by spawn.
3. Owners build in verifiable steps, perform self-proof, review with `$deslop`
   and `$no-comments` where appropriate, and record exact SHAs and evidence.
4. At each substantial code-ready head, independent reviewers challenge behavior,
   security, and proof. Validate runtime and performance only where relevant.
   Record missing or inapplicable checks explicitly rather than fabricating proof.
5. Resolve findings against the same artifact. Changed behavior invalidates
   affected evidence. Keep required CI, operator gates, and authorization distinct
   from reviewer approval.
6. Create or update PRs only within the request. Use project conventions for
   draft/ready status. If merge is authorized, verify the latest head and merge
   requirements before landing; otherwise return the reviewed result.
7. Maintain checkpoints and a decision trail. Active-session audits are not
   durable scheduled jobs. A `scheduled audit` requires a configured dispatcher.
