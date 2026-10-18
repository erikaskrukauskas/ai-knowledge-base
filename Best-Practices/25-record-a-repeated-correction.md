---
title: Record a repeated correction
tags: [practices, instructions, lessons]
status: verified
updated: 2026-10-17
---

# Record a repeated correction

When you correct the same agent mistake twice, write the correction into the instruction file. Do not keep retyping it in the chat.

Codex’s best-practices guide says: "When Codex makes the same mistake twice, ask it for a retrospective and update `AGENTS.md`." Claude Code’s memory docs say to treat `CLAUDE.md` as "the place you write down what you’d otherwise re-explain." See [Best practices](https://developers.openai.com/codex/learn/best-practices) and [How Claude remembers your project](https://code.claude.com/docs/en/memory).

## Write it down when

- The same constraint was missing in two sessions.
- The correction is true for every task in that project, or for every project.

## Where it goes

- Every project: this library, with a short pointer from the global instruction file. See [One library, several agents](08-one-library-several-agents.md).
- One project: that project’s `AGENTS.md` or `CLAUDE.md`.
- One kind of task: a skill, not the always-on file. See [Choose a rule or a skill](13-choose-a-rule-or-a-skill.md).

A correction you have not checked stays a candidate lesson, not a verified practice. See [Verify and record](05-verify-and-record.md). An instruction file still does not block a tool. See [Use a hook to enforce](11-use-a-hook-to-enforce.md).
