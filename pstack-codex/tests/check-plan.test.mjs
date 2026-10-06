import assert from "node:assert/strict";
import test from "node:test";
import { checkPlan } from "../skills/poteto-mode/scripts/check-plan.mjs";

const plan = `# Workspace lifecycle
## Goal
Retain checkout data after stop.
## Execution
Implement on the feature branch. Return a reviewed patch without merging.
## Unit 1: Stop execution and retain storage
### Depends on
No dependencies.
### Files
- [ ] Own lifecycle controller and status types.
### Build
- [ ] Stop execution before marking the workspace stopped.
### Acceptance
- [ ] Restart reads the retained checkout.
### Verify
- [ ] Unit: Assert transition ordering and retry behavior.
- [ ] Live: Stop and restart a workspace, then read the saved file.
- [ ] Perf: N/A because this changes control-plane lifecycle semantics.
### Review and delivery
- [ ] Independent review of retention and credential revocation.
## Risks
Storage backend recovery needs cluster integration testing.
`;

test("accepts a concrete plan with scoped evidence", () => assert.deepEqual(checkPlan(plan), []));
test("rejects missing runtime evidence", () => assert.ok(checkPlan(plan.replace(/- \[ \] Live:.*\n/, "")).some(p => /lacks Live/.test(p.message))));
test("rejects unexplained not-applicable evidence", () => assert.ok(checkPlan(plan.replace(/Perf: N\/A.*\n/, "Perf: N/A\n")).some(p => /needs a reason/.test(p.message))));
test("rejects an unfilled unit template", () => assert.ok(checkPlan(plan.replace("Restart reads the retained checkout.", "<pass predicate>")).some(p => /placeholder/.test(p.message))));
test("does not count fenced examples as real units", () => assert.ok(checkPlan("# Example\n```markdown\n" + plan + "```\n").some(p => /No implementation units/.test(p.message))));
