### Worktree cleanup

1. Run `scripts/worktree-audit.sh <repo>` for a read-only inventory. It uses Git's
   actual worktree paths, including paths with spaces. No transcript scan occurs
   unless an authorized directory is supplied explicitly.
2. Inspect dirty files, untracked work, unique commits, branch relationships, and
   associated PR state. An ancestor relationship is one signal, not proof that
   retained work is disposable. Missing evidence means hold for review.
3. Propose candidates and explain what would be lost. Remove only worktrees or
   caches covered by the user's cleanup authorization. Never use force removal
   to discard dirty or untracked work implicitly.
4. Verify retained work and the resulting Git inventory. Do not broaden a worktree
   task into deletion of simulator data, application profiles, or unrelated caches.
