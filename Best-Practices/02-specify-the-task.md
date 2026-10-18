---
title: Specify the task
tags: [practices, prompting, workflow]
status: verified
updated: 2026-10-17
---

# Specify the task

An agent does better work from a bounded task than from a topic. Write the outcome, the constraints, and how you will know it is done.

## Include

- The result a user or caller can observe.
- The files, modules, or documents in scope.
- Constraints that are easy to violate: public API, data shape, supported runtime, files to leave alone.
- The check that defines done: a test, a command, a document review, a query result.
- Relevant versions when product behavior matters.

## Leave out

- A tour of unrelated history.
- Instructions that conflict with the project rules already in `AGENTS.md` or `CLAUDE.md`.
- Copies of entire standards. Point to the canonical page.

## Size the change

Ask for one outcome at a time when the steps depend on each other. A single request that mixes research, a large refactor, and a new subsystem is harder to verify and easier to half-finish.

## Revision

When the result misses the mark, add the missing constraint to the task. Changing the prompt without saying what was wrong produces another broad attempt.

## For knowledge work in this repo

A documentation task names the decision, the audience (agents in other projects), and the page to update. New pages are for new topics. Existing topics get edited in place.
