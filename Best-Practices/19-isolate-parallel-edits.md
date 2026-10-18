---
title: Isolate parallel edits
tags: [practices, agents, worktrees]
status: verified
updated: 2026-10-17
---

# Isolate parallel edits

Give each agent that will edit files its own checkout. A separate context window does not give it a separate working tree.

Cursor's worktree docs say: "Use worktrees when you want to start several agents on the same repo without conflicts." Each task gets its own files and changes, and the main checkout stays untouched. See [Worktrees](https://cursor.com/docs/configuration/worktrees).

Subagents are the opposite by default. They share the parent checkout, and "when several subagents edit files at once, they can overwrite each other's changes." Ask for an isolated environment when they must edit in parallel. See [Subagents](https://cursor.com/docs/subagents) and [Delegate to a subagent](10-delegate-to-a-subagent.md).

## Use a separate checkout when

- Two agents will change files at the same time.
- You want to compare two implementations of the same task.
- Installs, builds, or a risky refactor should not touch the branch you have open.

## Stay in the main checkout when

- One agent is doing the only edit.
- The other workers only read or return a summary.
- You are answering a question. See [Answer without editing](14-answer-without-editing.md).

Review the isolated result before you bring it back. Do not merge two worktrees by hand in the main checkout while an agent is still writing there.
