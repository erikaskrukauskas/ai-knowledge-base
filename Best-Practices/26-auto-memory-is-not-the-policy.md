---
title: Auto memory is not the policy
tags: [practices, memory, instructions]
status: verified
updated: 2026-10-17
---

# Auto memory is not the policy

Write behavior you intend in the instruction file. Treat auto memory as notes the agent took, not as a rule you approved.

Claude Code’s memory docs say `CLAUDE.md` is where you guide behavior, and auto memory is how Claude learns from corrections without manual effort. Both load at the start of a conversation. "Claude treats them as context, not enforced configuration." See [How Claude remembers your project](https://code.claude.com/docs/en/memory).

## Promote a note when

- You want the next session to follow it even if auto memory is off or wrong.
- It contradicts another note. An instruction file you review beats a note you have not read. See [Record a repeated correction](25-record-a-repeated-correction.md).

## Leave it as memory when

- It is a tentative observation from one session.
- You have not checked it. See [Context and retrieval](03-context-and-retrieval.md).

To stop an action no matter what the notes say, use a permission rule or a hook. See [Use a hook to enforce](11-use-a-hook-to-enforce.md).
