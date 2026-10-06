### Shipping

Use only for an explicit request to merge or otherwise publish the reviewed work.
Deployment requires authorization covering the destination and operation.

1. Resolve the actual repository, base branch, forge, requested output, and
   authorized action. Inspect current heads, CI, reviews, and required gates.
2. Verify every substantial unit at its exact head using independent review and
   relevant runtime proof. CI green alone is not independent verification.
3. Record artifact SHAs, patch identity, evidence, dependencies, and verdicts.
   Do not transfer evidence across changed patches or materially different bases
   without checking whether the original proof still applies.
4. Land only the contiguous authorized verified prefix. Obey repository protections
   and project merge strategy. Do not force-push shared branches, disable checks,
   or bypass an operator gate to make progress.
5. If using the bundled PR watcher, read its help and set a bounded watch. Treat
   wake events as prompts to re-read live state. Queued or READY is not merged;
   confirm `mergedAt` or the forge's equivalent before advancing dependencies.
6. Report what actually landed and what remains. Stop on failed required checks,
   uncertain authorization, changed evidence, or an unresolved review gate.
