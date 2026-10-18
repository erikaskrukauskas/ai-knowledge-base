---
title: Audit instructions when they go stale
tags: [practices, instructions, maintenance]
status: verified
updated: 2026-10-17
---

# Audit instructions when they go stale

Check instruction files when the model, the commands, or the repo layout changes. An old line is still loaded, and the agent may follow it.

Claude Code’s `/doctor prompt-audit` looks for instructions written for older models, references to files or commands that do not exist, and files that contradict each other. It reports proposed edits and changes nothing until you apply them. It needs Claude Code v2.1.283 or later. See [How Claude remembers your project](https://code.claude.com/docs/en/memory).

## Audit when

- A product changelog retires a model, a flag, or a file name this library or the project mentions.
- A command in `AGENTS.md` or `CLAUDE.md` fails because the path or the tool moved.
- Two files disagree. See [Closer instructions are read last](28-closer-instructions-are-read-last.md).

## After the audit

- Apply only the edits you agree with.
- Update `updated` on a page in this library when the product fact changed.
- Prefer the current official page over an old lesson when they disagree. See [Context and retrieval](03-context-and-retrieval.md).

Target under 200 lines in a project `CLAUDE.md`. Longer files cost context and are followed less consistently. Move a rule that applies to one path into a path-scoped rule or a skill. See [Choose a rule or a skill](13-choose-a-rule-or-a-skill.md).
