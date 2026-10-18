---
title: Instructions hold what the code does not show
tags: [practices, instructions, context]
status: verified
updated: 2026-10-18
---

# Instructions hold what the code does not show

Put a line in the project instruction file only when the agent would get it wrong without that line. Leave out anything the agent can read from the code.

Claude Code's best-practices guide says to ask, for each line, whether removing it would cause mistakes. If not, cut it. Include commands the agent cannot guess, style that differs from the language default, test commands, repo etiquette, architecture choices, environment quirks, and gotchas. Exclude standard conventions, file-by-file tours, tutorials, and facts that change often. "Bloated CLAUDE.md files cause Claude to ignore your actual instructions." See [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices).

## Keep

- The build, test, and lint commands. See [Specify the task](02-specify-the-task.md).
- A constraint that is easy to violate and is not obvious from one file.

## Cut

- "Write clean code" and other lines every model already knows.
- A copy of a manual. Link the page. See [Context and retrieval](03-context-and-retrieval.md).
- A rule you have marked urgent on every line. If many lines are emphasized, none of them stands out.

A procedure for one kind of task belongs in a skill, not in the file that loads every session. See [Choose a rule or a skill](13-choose-a-rule-or-a-skill.md).
