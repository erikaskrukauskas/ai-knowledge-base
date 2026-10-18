---
title: Consultation protocol
tags: [agents, retrieval, workflow]
status: verified
updated: 2026-10-17
---

# Consultation protocol

Paste this into a project's `AGENTS.md`, Codex global instructions, or `CLAUDE.md`. Adjust the path.

```markdown
## AI knowledge base

Shared AI practices live in `<path-to-ai-knowledge-base>`.
Domain practices live in that domain's repo. Project decisions stay in this project.

Before a significant change:

1. Name the technologies, constraints, and the decision to make.
2. If the question is how to brief, search, compare, verify, or record AI-assisted work, search the AI knowledge base:
   `python "<path-to-ai-knowledge-base>\Search-Index\search.py" "<keywords>"`
3. If the question is domain design, search that domain's knowledge repo.
4. Read current official documentation when the answer depends on a product version.
5. For a significant design choice, compare the real options, then implement one.
6. Verify with the check named in the task.
7. Record a reusable AI-tooling lesson in the AI knowledge base. Record domain findings in the domain or project repo.
```

Significant means an architecture choice, a public interface, a security boundary, or a workflow other sessions will repeat. A narrow local fix can proceed from the code at hand.

Apply a lesson only when its status is `verified` and its environment still matches. Confirm product behavior against current docs when a lesson and the docs disagree.
