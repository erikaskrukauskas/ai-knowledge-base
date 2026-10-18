---
title: Use a hook to enforce
tags: [practices, hooks, security, agents]
status: verified
updated: 2026-10-17
---

# Use a hook to enforce

Use a hook when a check has to run even if the agent ignores its instructions. Use a rule or `AGENTS.md` when the guidance is a preference the agent can follow. Claude Code treats `CLAUDE.md` as context, not as a control: "To block an action regardless of what Claude decides, use a PreToolUse hook instead." See [How Claude remembers your project](https://code.claude.com/docs/en/memory). Cursor's hardening guide says rules are for steering and are non-deterministic, and that critical hooks should fail closed. See [Security and Privacy Hardening](https://cursor.com/docs/enterprise/security-hardening).

Cursor's hooks docs say hooks "run before or after defined stages of the agent loop and can observe, block, or modify behavior." A permission hook that returns invalid output, or exits with code 2, blocks the action. Other exit codes fail open: the action proceeds. See [Hooks](https://cursor.com/docs/hooks).

## Use a hook when

- A secret, credential, or private file must not be sent or read.
- A destructive or remote command must be denied before it runs.
- A formatter, audit script, or policy check must run after an edit, including when the agent is a cloud agent.

## Do not use a hook when

- The instruction is a working habit, such as searching this library first. Put that in `AGENTS.md`. See [One library, several agents](08-one-library-several-agents.md).
- The action is one repeatable procedure. Use a skill.
- The work is a long investigation. See [Delegate to a subagent](10-delegate-to-a-subagent.md).

## Fail closed on purpose

Write the deny path so it exits 2 or returns `permission: "deny"`. Do not rely on a crash, a missing script, or a timeout to stop the action. Those fail open.

Keep the hook in the project when the policy belongs to that repository. A hook in the user home directory does not travel to a cloud agent. See [Security and data separation](07-security-and-data-separation.md).
