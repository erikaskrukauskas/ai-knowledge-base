---
title: Cap a hook that continues the agent
tags: [practices, hooks, automation]
status: verified
updated: 2026-10-18
---

# Cap a hook that continues the agent

A hook may send the agent back to work. It must stop. Do not remove the cap.

Cursor's stop hook can submit a follow-up message when the loop ends. The default limit is 5 follow-ups per script. `loop_limit` set to `null` removes that cap. See [Hooks](https://cursor.com/docs/hooks). Claude Code stops a Stop hook after it blocks eight times in a row with no tool call in between. See [Automate actions with hooks](https://code.claude.com/docs/en/hooks-guide).

## Use a continuing hook when

- The follow-up is a check with a pass or fail, such as a test command.
- You can name the condition that means stop.

## Do not

- Set the limit to unlimited so a failing check retries forever.
- Let the hook invent a new task. The follow-up is the check you already named. See [Schedule only a reliable workflow](20-schedule-only-a-reliable-workflow.md).

A hook that must block a dangerous command is a different setting: fail closed. See [Use a hook to enforce](11-use-a-hook-to-enforce.md).
