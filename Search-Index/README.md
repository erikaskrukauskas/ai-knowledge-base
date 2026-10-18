---
title: Search index
tags: [retrieval, search]
status: verified
updated: 2026-10-17
---

# Search index

Phase 1 retrieval is keyword search over the markdown in this repo. It uses the Python standard library and does not need PostgreSQL, an embedding model, or a running server.

Semantic search and hybrid ranking belong with the MCP service in Phase 2. See [MCP-Server/README.md](../MCP-Server/README.md).

## Commands

From the repo root:

```powershell
python Search-Index/search.py --list
python Search-Index/search.py "lesson status"
python Search-Index/search.py --tag security
python Search-Index/search.py --status verified "retrieval"
```

`--list` prints every document's path, status, and tags. A query requires every keyword to appear in the file. `--tag` and `--status` filter YAML frontmatter.

The script skips `.git`, virtual environments, and this `Search-Index` folder.

## How to think about a miss

A miss means no page used those words. Try the terms from the task (`verification`, `mcp`, `scope`) or list the catalog and open the closest title. Add the missing words to the page that should have matched, or write the page if the topic is new.

## What this search will not do

- It does not search sibling domain repos.
- It does not search the web or official docs.
- It does not rank by meaning. A synonym that never appears in the file will not hit.
