---
title: MCP server design
tags: [mcp, retrieval, roadmap]
status: candidate
updated: 2026-10-17
---

# MCP server

Phase 2 adds a local MCP server so Codex and Claude can search this library from any project. Phase 1 uses [Search-Index/search.py](../Search-Index/search.py) instead. This page is the contract to build against. The server is not implemented yet.

## Why a server later

Keyword search already works on one machine. An MCP server is worth adding when agents in other projects should call a tool instead of remembering a Python path. PostgreSQL and pgvector are worth adding when keyword search misses useful pages often enough to matter.

## Proposed tools

| Tool | Purpose |
| --- | --- |
| `search_knowledge` | Hybrid search later; keyword search first. Returns paths, titles, status, and a short snippet. |
| `get_document` | Return one markdown file by repo-relative path. |
| `list_lessons` | Filter lessons by status, tag, and environment. |
| `record_lesson` | Create a `candidate` lesson from the template. It must not set `verified` by itself. |

Tools read and write only this repository. They do not search domain repos unless a later, explicit tool is added for that.

## Deployment order

1. Local process on this PC, started by the agent client, with the repo path as configuration.
2. Optional Docker or WSL2 packaging after the tools are stable.
3. Authenticated remote access only after you decide which documents may leave the machine.

ChatGPT does not automatically see a local MCP server. Remote access is a separate phase and needs an approved connector. See [ChatGPT](../Agent-Instructions/chatgpt.md).

## Data rules the server must keep

- Do not index `.env` files, PDFs, or anything outside the markdown library.
- Return `superseded` documents only when the query asks for them.
- Include `status` in every hit so the agent can prefer `verified`.
- Refuse to store secret-shaped values in `record_lesson`.

## Open choices

- Embedding model and whether pgvector runs locally.
- Whether `record_lesson` commits the new file or only writes it for review.
- The auth design for any future remote API.

Resolve those when Phase 2 starts, using the lessons collected from Phase 1 search.
