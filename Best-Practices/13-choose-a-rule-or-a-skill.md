---
title: Choose a rule or a skill
tags: [practices, rules, skills, agents]
status: verified
updated: 2026-10-18
---

# Choose a rule or a skill

Put an instruction in a rule or `AGENTS.md` when it must be present for the files it covers. Put it in a skill when the agent should load it only for a matching task.

Cursor discovers skills and "the agent is presented with available skills and decides when they are relevant based on context." Skills "load resources on demand." Rules that are always applied, or that match file globs, are a different mechanism: Cursor does not convert those into skills, because their trigger is explicit. See [Agent Skills](https://cursor.com/docs/skills).

## Use a rule or `AGENTS.md` when

- Every task in the project should follow it, such as the consultation protocol.
- It applies only while the agent is in certain files. Scope it with a path or a nested `AGENTS.md`.
- It is short. Claude Code's memory docs say to target under 200 lines per `CLAUDE.md`. Longer files cost context and are followed less consistently. A rule that matters for only some files belongs in a path-scoped rule, which loads when those files are used. See [How Claude remembers your project](https://code.claude.com/docs/en/memory) and [Context and retrieval](03-context-and-retrieval.md).

## Use a skill when

- The steps are a procedure the agent needs for some tasks and not others.
- The procedure includes a script, a template, or a reference that should load only when used.
- You want to invoke it yourself with `/skill-name`. Set `disable-model-invocation: true` so the agent does not apply it on its own. Use that for a workflow with side effects, such as creating a pull request.

Write the description as the routing test: what the skill does and when to use it. A vague description makes the agent load it at the wrong time. Put the decision and the stop condition at the top. Compaction keeps the start of a skill and drops the rest. See [Explore the context window](https://code.claude.com/docs/en/context-window).

## Other surfaces

A check that must run even if the instruction is ignored is a hook. See [Use a hook to enforce](11-use-a-hook-to-enforce.md). Work that needs its own context window is a subagent. See [Delegate to a subagent](10-delegate-to-a-subagent.md). Shared habits for every project stay in this library, with a short pointer from `AGENTS.md`. See [One library, several agents](08-one-library-several-agents.md).
