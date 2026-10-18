---
title: Answer without editing
tags: [practices, agents, workflow]
status: verified
updated: 2026-10-17
---

# Answer without editing

When the task is a question, use a read-only mode. Do not leave the agent in a mode that can edit files or run writes.

Cursor's CLI docs describe Ask mode as "Read-only exploration without making changes." The agent can search the codebase and answer. It does not edit files. Switch with `/ask` or start with `--mode=ask`. See [Cursor CLI](https://cursor.com/docs/cli/overview).

## Use read-only when

- You need an explanation, a file map, or a risk list before deciding.
- The session must not change the tree, such as a review of someone else's branch.
- You are still gathering the slice of context the decision needs. See [Context and retrieval](03-context-and-retrieval.md).

## Switch modes when the task changes

A question that becomes a design goes to Plan mode. See [Plan before a large change](12-plan-before-a-large-change.md). A question that becomes an approved edit goes to Agent mode.

Do not rely on a sentence in the prompt ("do not write any code") as the only guard when a read-only mode exists. The mode removes the edit. The sentence does not.
