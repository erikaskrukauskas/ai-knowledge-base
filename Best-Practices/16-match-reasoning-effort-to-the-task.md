---
title: Match reasoning effort to the task
tags: [practices, models, prompting]
status: verified
updated: 2026-10-17
---

# Match reasoning effort to the task

Start from the reasoning effort the client uses by default. Raise it when the task is ambiguous, multi-step, or hard to verify. Lower it when the change is small and the done check is obvious.

Codex's best-practices guide groups effort this way: low for faster, well-scoped tasks; medium or high for complex changes or debugging; extra high for long, agentic, reasoning-heavy tasks. Use the stronger model your plan actually offers, and keep the default effort until a result shows you need more. See [Best practices](https://developers.openai.com/codex/learn/best-practices).

## Raise effort when

- The task has more than one reasonable design. See [Compare, then implement](04-compare-then-implement.md).
- A wrong edit is expensive to unwind.
- The first attempt missed the done check in [Specify the task](02-specify-the-task.md).

## Keep or lower effort when

- The edit is local and you have made this kind of change before.
- You are in a read-only pass. Extra effort does not replace a missing file. See [Answer without editing](14-answer-without-editing.md).

Check the model picker before you write a saved default. A changelog can retire a model for some sign-in methods while other docs still name it. See [Codex](../Agent-Instructions/codex.md).
