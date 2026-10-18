---
title: Delegate to a subagent
tags: [practices, agents, context, subagents]
status: verified
updated: 2026-10-17
---

# Delegate to a subagent

Hand a slice of the task to a subagent when the parent conversation should stay small. Keep a single-purpose action in a skill.

Cursor's subagent docs state the split: use a subagent for context isolation, parallel work, multi-step expertise, or an independent check. Use a skill when the task is single-purpose and finishes in one shot, such as generating a changelog or formatting imports. Each subagent runs in its own context window and returns a result to the parent. See the [Cursor subagent docs](https://cursor.com/docs/subagents).

## Use a subagent when

- The investigation would fill the parent conversation with files that the final change does not need.
- Two or more parts of the task can proceed at the same time.
- You want a separate pass to verify the parent's work.
- The work needs a specialist prompt across many steps.

## Use a skill instead when

- The action is one repeatable procedure.
- The result should land in the same conversation.
- A separate context window would throw away the details the parent still needs.

## Where the definition lives

Project subagents stay in that project. A subagent you want in every project belongs in the user directory. Cursor checks `.cursor/agents/`, and also `.claude/agents/` and `.codex/agents/` for compatibility. Project files win when names collide. See the [file locations](https://cursor.com/docs/subagents).

Write the description as the routing rule. A vague description makes the parent guess.

## After the subagent returns

Treat the result as input, not as a finished change. The parent still runs the check named in the task. See [Verify and record](05-verify-and-record.md).

A subagent that only returns a summary can share the parent's checkout. Subagents that edit at the same time need separate checkouts, or they overwrite each other. See [Isolate parallel edits](19-isolate-parallel-edits.md).

Long research belongs in the subagent so the parent can follow [Context and retrieval](03-context-and-retrieval.md) and load only the slice that decides the change.
