---
title: Reproduce before you fix
tags: [practices, debugging, verification]
status: verified
updated: 2026-10-18
---

# Reproduce before you fix

When the cause is not obvious from the code, get runtime evidence before editing. A guess that happens to compile is not a diagnosis.

Cursor's Debug mode docs say to use it when you can reproduce a bug but cannot see the cause, and for races, performance problems, and regressions. The sequence is: explore and state hypotheses, add instrumentation, reproduce the bug, read the logs, make a targeted fix, then verify and remove the instrumentation. See [Debug Mode](https://cursor.com/docs/agent/debug-mode).

## Do this when

- The failure depends on timing, data, or a step you have not watched.
- Reading the code produced two plausible causes and the wrong edit is expensive.
- Something used to work and the diff that broke it is not obvious.

## Skip it when

- The task is a known local edit with one obvious change.
- You cannot reproduce the bug. Say so, and do not invent a fix from a hypothesis. See [Verify and record](05-verify-and-record.md).

Describe the expected behavior and the actual behavior, including the error text. Follow the reproduction steps the same way each time. When you can express the bug as a test, write the failing test first, then fix the product code. After the fix works, remove the logs you added to observe it. Do not silence the check. See [Do not suppress a failing check](31-do-not-suppress-a-failing-check.md).
