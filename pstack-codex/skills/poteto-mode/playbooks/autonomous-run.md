### Autonomous run

1. Define done as an observable predicate and record the authorized scope.
2. Drive the smallest evidence-backed change, then verify it. Keep successful
   units and remove failed experiments without disturbing unrelated work.
3. For an external condition, use an available bounded watcher and resumable
   process waits. Keep the user updated; avoid long blocking sleeps. Without an
   external dispatcher, supervision lasts only while the session is active.
4. Address in-scope blockers. Record unrelated discoveries as follow-up work;
   do not silently widen scope or perform unauthorized external writes.
5. Log decisions with `$show-me-your-work`. Checkpoint changes, commands,
   evidence, and the next step before a pause or session boundary.
6. Stop when the predicate is met, the user stops the task, or a real blocker
   requires unavailable input or capabilities. Never relax the predicate to
   claim success. Configure durable scheduling only when explicitly requested
   and actually supported by the host or an external job service.
