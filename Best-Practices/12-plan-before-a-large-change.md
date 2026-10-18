---
title: Plan before a large change
tags: [practices, planning, workflow]
status: verified
updated: 2026-10-18
---

# Plan before a large change

Use Plan mode when the change has more than one reasonable approach, touches many files, or the requirements are still unclear. For a small change you have made before, stay in Agent mode and edit.

Cursor's Plan mode docs say it "creates detailed implementation plans before writing any code." It fits complex features, tasks that touch many files or systems, unclear requirements, and architectural decisions. "For quick changes or tasks you've done many times before, jumping straight to Agent mode is fine." See [Plan Mode](https://cursor.com/docs/agent/plan-mode).

## Before building

1. Switch to Plan mode and answer the clarifying questions.
2. Read the plan against the task's done condition. See [Specify the task](02-specify-the-task.md).
3. If more than one design would work, name the constraint that decides. See [Compare, then implement](04-compare-then-implement.md).
4. Approve the plan, then implement that plan.

## When the build misses

Revert the changes and edit the plan. Do not keep prompting the same implementation until it drifts. The docs say going back to the plan is often faster than fixing an in-progress agent.

Save the plan in the project when later sessions or other people need it. Leave a one-off plan in the home directory. After the plan is specific, start a fresh session to implement it so the exploration does not crowd the edit. See [One chat per outcome](17-one-chat-per-outcome.md).
