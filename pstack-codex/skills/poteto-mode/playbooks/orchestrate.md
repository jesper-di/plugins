### Orchestrate

Coordinate a standing program with explicit unit ownership, durable artifacts,
and verification at each frontier. The runtime contract governs capabilities.

1. Fix the goal, authorized operations, stop conditions, review gates, target
   repository, and actual base branch. Record standing orders in a task-specific
   state directory chosen within the authorized workspace.
2. Decompose into units with dependencies, owned paths, exact input SHAs, pass
   predicates, evidence destinations, and output branches. Keep one writer for
   overlapping code, Git state, and each ledger. Prefer fewer broader units over
   unnecessary coordinator layers.
3. Use `scripts/orch/orch.ts` as a local ledger when useful. It records state;
   it does not spawn, wake, isolate, or schedule agents. Read its CLI help before
   invoking it. Maintain briefs and decision evidence alongside the ledger.
4. Dispatch through native agent tools within live concurrency and depth limits.
   Each brief includes the original task, subsequent corrections, standing orders,
   role, scope, workspace, validation, and authorization limits. Workers inherit
   the parent model unless an available override was explicitly configured.
5. Drain completed work without busy polling. Review actual diffs and receipts.
   An independent reviewer checks each substantial unit at its exact SHA. Missing
   independent verification is an open condition, not a passing verdict.
6. Drive dependencies only from verified artifacts. Keep PR creation, merge,
   deployment, and cleanup within separately authorized operations. A program
   handed over for implementation does not imply permission to merge.
7. Use available agent-status tools and real artifact progress for liveness. On
   a stuck worker, preserve its work, stop overlapping writers, and replace it
   with a consolidated brief if supported. Never infer liveness from file mtime.
8. Checkpoint before session limits or pauses. Durable re-entry needs a configured
   dispatcher; otherwise report the resume recipe and stop at a recoverable point.
   After restart, reconstruct from SHAs, branches, ledgers, and live checks rather
   than reusing stale session IDs.

Report verified units, current frontier, evidence, unresolved gates, and the
next concrete action. Send external status messages only when authorized.
