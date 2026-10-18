---
title: AI Knowledge Base
tags: [overview, agents, scope]
status: verified
updated: 2026-10-17
---

# AI Knowledge Base

This repository is the shared library for **AI engineering knowledge**: how agents should research, implement, verify, and record work. Other projects consult it for practices that transfer across codebases.

Data engineering, data science, application development, and CI/CD keep their own repositories. This repo stores the AI working method, not those domains.

## What belongs here

- Practices for Codex, Claude, Cursor, and ChatGPT.
- Instructions agents should follow before changing code.
- Lessons learned about using AI tools, after they have been tested.
- Pointers to official AI product documentation.
- Notes and citations for AI references. Full copyrighted books and PDFs stay out of git.

## How another project uses it

1. Point that project's agent instructions at this checkout. Copy the snippet from [Agent-Instructions/consultation-protocol.md](Agent-Instructions/consultation-protocol.md).
2. Search before significant AI-workflow decisions:

```powershell
python Search-Index/search.py "verify before finishing"
python Search-Index/search.py --tag lessons
python Search-Index/search.py --list
```

3. Apply what is reusable. Leave project requirements, environment details, and domain design in the project repo.
4. After a verified AI-tooling lesson, add a file under `Lessons-Learned/` using the template.

Domain questions belong in that domain's knowledge repo.

## Layout

| Path | Role |
| --- | --- |
| `Best-Practices/` | Stable practices for AI-assisted engineering |
| `Lessons-Learned/` | Session findings and their validation state |
| `Agent-Instructions/` | Snippets for Codex, Claude, Cursor, and ChatGPT |
| `Official-Documentation/` | Links to current product docs |
| `Books/` | Citation and notes policy for references |
| `Search-Index/` | Local keyword search over this repo |
| `MCP-Server/` | Design for a later shared retrieval service |
| `AGENTS.md` | Rules for agents editing this repo |
| `SCOPE.md` | Boundary between this repo and sibling repos |

## Roadmap

| Phase | Outcome | State |
| --- | --- | --- |
| 1. Foundation | Folder layout, practices, lessons template, keyword search | In this repo |
| 2. MCP | Local MCP tools so Codex and Claude can search from any project | Designed, not built |
| 3. Lessons memory | Validation workflow, superseding, retrieval of verified lessons | Template and rules are in place |
| 4. Remote access | Authenticated API or connector for ChatGPT | Later, after a local workflow is proven |

Estimates in the original proposal are planning ranges, not delivery dates.

## Principles

- Retrieve a relevant slice. Do not load the whole library into an agent context.
- Record a lesson after it is tested. Mark replacements as superseded.
- Keep one copy of each practice. Agent-specific files link to it.
- Keep personal notes and proprietary company information in approved stores, separate from each other.
