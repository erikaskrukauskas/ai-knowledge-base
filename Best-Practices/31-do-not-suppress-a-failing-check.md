---
title: Do not suppress a failing check
tags: [practices, verification, debugging]
status: verified
updated: 2026-10-18
---

# Do not suppress a failing check

When a check fails, fix the cause. Do not mute the check so the task can be called done.

Claude Code's best-practices guide says to address the root cause and not suppress the error. See [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices).

## Fix the cause

- A failing test means the behavior or the test's expectation is wrong. Change the product code when the test describes the behavior the task asked for.
- A failing build, type check, or lint run is a signal. Do not hide it with a skip, a broad ignore, or a catch that discards the error.
- Show the command and the output. A sentence that says the check passed is not the result. See [Verify and record](05-verify-and-record.md).

## Change the check only when

- The check encoded the bug, and the task says the new behavior is correct.
- You say that in the same change, and you replace it with a check that would fail if the bug returned.

If you cannot reproduce the failure, stop and say so. See [Reproduce before you fix](22-reproduce-before-you-fix.md).
