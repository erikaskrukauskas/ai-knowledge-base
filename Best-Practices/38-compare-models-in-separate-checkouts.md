---
title: Compare models in separate checkouts
tags: [practices, models, worktrees]
status: verified
updated: 2026-10-18
---

# Compare models in separate checkouts

To compare models on one task, give each run its own checkout. Pick one result. Do not merge them together.

Cursor's worktree docs say `/best-of-n` runs the same task across models, and each run gets its own worktree so the candidates stay isolated from each other and from the main checkout. It compares runs only. It does not merge the changes back for you. See [Worktrees](https://cursor.com/docs/configuration/worktrees).

## Use it when

- The task is hard enough that a second model might choose a better approach.
- You can judge the candidates with the same check. See [Verify and record](05-verify-and-record.md).

## After you pick

- Bring back one result, or commit from that worktree.
- Discard the others. Two half-applied designs are worse than the weaker candidate. See [Compare, then implement](04-compare-then-implement.md).

Raising reasoning effort on one model is a different decision. See [Match reasoning effort to the task](16-match-reasoning-effort-to-the-task.md). Parallel agents that are not a comparison still need separate checkouts when they edit. See [Isolate parallel edits](19-isolate-parallel-edits.md).
