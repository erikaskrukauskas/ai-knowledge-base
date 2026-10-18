---
title: Prefer the service CLI
tags: [practices, tools, context]
status: verified
updated: 2026-10-18
---

# Prefer the service CLI

When a service already has a command-line tool, tell the agent to use that tool. Do not paste the API manual into the prompt, and do not add an MCP server for the same job.

Claude Code's best-practices guide says CLI tools "are the most context-efficient way to interact with external services." See [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices).

## Use the CLI when

- The tool is installed and authenticated the way a person on that project already works.
- The task is a lookup or a change the CLI already supports, such as reading a pull request.

## Add an MCP server when

- The fact changes often and there is no CLI for it.
- The server removes a manual loop the CLI does not cover. See [Connect only the tools the task needs](15-connect-only-the-tools-the-task-needs.md).

Point the agent at `--help` for a CLI it has not used. Do not paste a tutorial. See [Instructions hold what the code does not show](34-instructions-hold-what-the-code-does-not-show.md).
