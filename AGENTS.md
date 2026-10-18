---
title: Agent rules for this repository
tags: [agents, governance]
status: verified
updated: 2026-10-17
---

# Agent rules

You are in the AI knowledge base. Other projects consult this repo for AI engineering practices. Domain knowledge has its own repos.

## While editing this repo

- Add or update AI-tooling knowledge only. Read [SCOPE.md](SCOPE.md) before creating a document.
- Put stable guidance in `Best-Practices/`. Put session findings in `Lessons-Learned/`.
- Give every document YAML frontmatter with `title`, `tags`, `status`, and `updated`.
- Keep one canonical copy of a practice. Link to it from agent-specific files.
- Do not commit secrets, credentials, copyrighted books, or verbatim official documentation.
- Do not present an untested fix as `verified`. Use the lifecycle in [Lessons-Learned/README.md](Lessons-Learned/README.md).
- When a newer document replaces an older one, set the old document to `superseded` and point `superseded_by` at the replacement.

## Status values

`candidate` → `tested` → `verified`

Use `superseded` when a newer document replaces this one. Keep the old file so past references still resolve.

## Knowledge maintenance

- A topic this repo does not yet cover: `.cursor/skills/add-uncovered-ai-topic/SKILL.md`
- Whether pages already here still match current sources: `.cursor/skills/review-covered-ai-topics/SKILL.md`
- What changed recently across Cursor, OpenAI, Anthropic, Claude, Codex, ChatGPT, MCP, Stack Overflow, or Reddit: `.cursor/skills/check-ai-work-updates/SKILL.md`

## Before you finish a documentation change

Search for an existing page on the same topic:

```powershell
python Search-Index/search.py --list
python Search-Index/search.py "your topic"
```

Update the existing page when the topic already exists.
