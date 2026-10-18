---
title: Consult before building
tags: [practices, retrieval, workflow]
status: verified
updated: 2026-10-17
---

# Consult before building

Search existing knowledge before significant work. The search target depends on the question.

## Choose the library

| Question | Search |
| --- | --- |
| How should the agent brief, verify, retrieve, or record work? | This repo |
| How should this technology be designed or operated? | That domain's knowledge repo |
| What did this project already decide? | That project's docs and history |

A new project does not need a private copy of this repo's practices. It needs a pointer to this checkout and a habit of searching it.

## Sequence

1. Name the technologies, constraints, and the decision you are about to make.
2. Search this repo for an AI-working practice that applies.
3. Search the domain repo for product and engineering guidance.
4. Read the matching official documentation when behavior depends on a current product version.
5. Compare viable approaches when the change is significant. See [Compare, then implement](04-compare-then-implement.md).
6. Implement and verify. See [Verify and record](05-verify-and-record.md).
7. Record a lesson when the finding will help a later session.

## What counts as significant

Search and compare when the work chooses an architecture, a public interface, a data model, a security boundary, or a workflow other sessions will repeat.

A narrow, local fix with an obvious edit can proceed from the code in front of you. Record a lesson afterward if the diagnosis was hard to find.

## Enforcement

Global instructions ask agents to do this. A project-start checklist is stronger because it is explicit. Use the checklist in [Agent-Instructions/project-start-checklist.md](../Agent-Instructions/project-start-checklist.md) when a project should require the search, not only encourage it.
