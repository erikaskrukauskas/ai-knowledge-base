---
title: Security and data separation
tags: [practices, security, privacy]
status: verified
updated: 2026-10-17
---

# Security and data separation

This library is for reusable engineering knowledge. It is not a secrets store and it is not a dump of company data.

## Never commit

- API keys, tokens, passwords, connection strings, or private certificates.
- Live `.env` files. `.env.example` with placeholder names is enough when a sample is useful.
- Customer data, internal datasets, or unpublished company documents.
- Copyrighted books, full PDFs, or verbatim copies of official manuals.

`.gitignore` ignores `.env` files and `*.pdf` so a local paper or export is harder to commit by accident. The ignore rule is a backstop. The rule is still: do not add those files.

## Separate stores

| Kind of information | Store |
| --- | --- |
| Reusable AI practices and verified tooling lessons | This repo |
| Personal notes that are not ready to share | A personal store you control |
| Proprietary company information | An approved company system with the right permissions |
| Project secrets | The project's secret manager or local ignored env files |

Personal knowledge and company knowledge use different storage, permissions, and AI processing approvals. Do not mix them in one index and assume a later filter will sort it out.

## Before remote access

A local checkout can stay on one machine. A remote API or ChatGPT connector needs authentication, an explicit allow-list of documents, and a decision about whether company content is in that index at all. See [MCP-Server/README.md](../MCP-Server/README.md).

## Agent behavior

Do not ask an agent to paste secrets into a lesson so the next session can "just work." Point to the secret's name and the approved place it is loaded from.
