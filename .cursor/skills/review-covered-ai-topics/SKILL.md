---
name: review-covered-ai-topics
description: >-
  Review Cursor, OpenAI, Anthropic, Claude, Codex, MCP, Stack Overflow, and
  Reddit for changes to AI topics this knowledge base already documents, then
  update those pages. Use when the user asks to review covered topics, refresh
  existing practices against current sources, or check whether documented
  guidance is outdated.
---

# Review covered topics

Start from the pages already in this repo. Check whether current sources still agree with them. This is not a scan for brand-new topics. New topics use [add-uncovered-ai-topic](../add-uncovered-ai-topic/SKILL.md). A time-window scan of every feed uses [check-ai-work-updates](../check-ai-work-updates/SKILL.md).

## List the covered topics

```bash
python Search-Index/search.py --list
```

Review pages in `Best-Practices/`, `Agent-Instructions/`, and verified files in `Lessons-Learned/`. Skip `Lessons-Learned/_template.md`, files with `status: superseded`, and files in `Official-Documentation/updates/`.

For each page, note the claim a source could invalidate: a product default, a file name, a tool behavior, or a rule presented as current.

## Check sources for those claims

Use the primary URLs in [sources.md](../check-ai-work-updates/sources.md). Search or fetch the official page for that product, then read the section that matches the claim.

Use Stack Overflow and Reddit only as leads. A community post does not change a practice page. Confirm it on a primary source first.

A feed item that does not touch a covered claim is out of this review.

## Update the page

Edit the existing page when a primary source contradicts or extends that claim. Set `updated` to today. Keep `status` unless the page is wrong enough to mark `superseded`, with `superseded_by` pointing at the replacement.

Do not add a new topic while reviewing. Do not paste release notes into the repo. Quote only the sentence needed, with the URL.

A changelog is not a lesson. Add a lesson only when this environment was tested against the change.

## Report

Write the report to `Official-Documentation/updates/YYYY-MM-DD-covered-topics.md` with frontmatter `title`, `tags: [documentation, updates]`, `status: verified`, and `updated`. Put the same report in the chat:

```markdown
# Covered topic review
Checked: YYYY-MM-DD

## Updated
- **Page** — what the source changed — [url](url)

## Still current
- Page — source checked

## Unconfirmed
- Page — claim that could not be checked, and which source failed
```
