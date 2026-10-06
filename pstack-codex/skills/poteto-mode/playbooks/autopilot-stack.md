### Autopilot stack

Build an ordered branch/PR stack for review. Default to leaving it merge-ready.

1. Scope one behavior and its acceptance criteria per unit. Record parent branch,
   parent SHA, owned paths, proof, and operator review gates.
2. Implement in order or parallelize only independent units with isolated write
   ownership. Use native workers and actual provisioned workspaces.
3. Verify each unit before using it as a dependency. Create PRs when requested,
   targeting the parent branch for a stack child. Follow project draft conventions.
4. Record the exact reviewed heads and patch identity. Restacking must preserve
   behavior; rerun affected proof when a conflict or changed patch invalidates it.
5. Review the whole contiguous stack for integration failures. Stop where a unit
   fails, needs user input, or lacks required independent evidence.
6. Return the stack order, SHAs, evidence, and unresolved gates. Land it only when
   separately authorized, through the shipping playbook. No scheduler or merge
   authority is implied by the word autopilot.
