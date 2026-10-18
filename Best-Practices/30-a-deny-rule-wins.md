---
title: A deny rule wins
tags: [practices, security, permissions]
status: verified
updated: 2026-10-17
---

# A deny rule wins

Write a deny rule for the action that must not happen. Do not add a narrower allow rule and expect it to poke a hole in that deny.

Claude Code evaluates permission rules as deny, then ask, then allow. "An allow rule can’t carve an exception out of a deny rule." A broad deny such as `Bash(aws *)` blocks a call that also matches a narrower allow. Instructions in the prompt or `CLAUDE.md` do not change what the permission system allows. See [Configure permissions](https://code.claude.com/docs/en/permissions).

## Deny when

- The command can destroy data, push, or reach a system the task does not need.
- A tool should disappear from the model’s context. A bare tool name such as `Bash` removes that tool. A scoped rule such as `Bash(rm *)` leaves the tool and blocks matching calls.

## Allow when

- You have read the exact command and want that command to skip a prompt.
- The allow is narrower than "any shell." A saved "don’t ask again" for a shell command is kept for the repository, including worktrees. A file-edit approval lasts only until the session ends.

`bypassPermissions` skips prompts, including writes to protected paths. Use it only in an isolated environment such as a container or VM. See [Keep approval tight by default](18-keep-approval-tight-by-default.md). A hook is the other way to block an action the model still tries. See [Use a hook to enforce](11-use-a-hook-to-enforce.md).
