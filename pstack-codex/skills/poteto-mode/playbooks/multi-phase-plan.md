### Multi-phase plan

The deliverable is a plan; do not implement unless that was also requested.

1. Ground the requirement, actual architecture, constraints, and target behavior.
   Use `$how`, `$why`, and a focused prototype when an observation can resolve a
   question. Ask only for missing product choices that affect the plan.
2. Divide into units with dependencies, owned paths, concrete behavior, acceptance
   criteria, evidence, and authorization gates. Scale unit count to the change.
3. Use the skeleton below. Keep the exact unit headings and nonempty checklist
   sections so the plan validator can check coverage. A verification dimension
   that does not apply needs an explicit `N/A` reason grounded in the change.
4. Include a recoverable active-session or `scheduled audit` recipe. Scheduling
   requires a real configured dispatcher; otherwise describe manual re-entry.
5. Run the installed `scripts/check-plan.mjs <plan.md>` and fix reported gaps.
   Return the plan path, validation result, and decisions still required.

```markdown
# <Program> plan

## Goal
<Concrete resulting behavior and scope.>

## Execution
<Playbook, base branch, ownership, authorization, checkpoint, and resume recipe.>

## Unit 1: <Outcome>

### Depends on
<No dependencies, or prior units and input artifacts.>

### Files
- [ ] <Owned paths and boundaries.>

### Build
- [ ] <Concrete implementation step.>

### Acceptance
- [ ] <Observable behavior and pass predicate.>

### Verify
- [ ] Unit: <Relevant behavior check or N/A with reason.>
- [ ] Live: <Actual surface proof or N/A with reason.>
- [ ] Perf: <Comparable metric/probe/budget or N/A with reason.>

### Review and delivery
- [ ] <Independent review where needed, user gates, and authorized output.>

## Risks
<Unresolved choices, capabilities, recovery, and evidence gaps.>
```
