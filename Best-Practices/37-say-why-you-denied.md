---
title: Say why you denied
tags: [practices, permissions, workflow]
status: verified
updated: 2026-10-18
---

# Say why you denied

When you deny an action, say what was wrong. A bare denial stops the turn and teaches the agent nothing.

Claude Code's permission docs say that choosing No without a comment, on a prompt from the main conversation, stops the turn. A comment on No is sent as the reason, and the agent continues. See [Configure permissions](https://code.claude.com/docs/en/permissions).

## Include in the reason

- The constraint the action violated.
- The narrower action that is allowed, if there is one.

Do not approve a command you have not read in order to avoid typing the reason. See [A deny rule wins](30-a-deny-rule-wins.md). If the same denial happens twice, put the constraint in the instruction file or in a deny rule. See [Record a repeated correction](25-record-a-repeated-correction.md).
