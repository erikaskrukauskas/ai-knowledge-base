---
name: add-uncovered-ai-topic
description: >-
  Add a missing AI-engineering topic to this knowledge base after confirming
  no page covers it. Use when the user asks to document, add, or update the
  AI knowledge base on a topic it does not yet cover, or to write a new
  practice or lesson for an uncovered agent, MCP, prompting, or verification
  topic.
---

# Add an uncovered AI topic

Add one new topic to this library. If a page already covers it, update that page instead of creating a second one.

## Decide where it goes

Read [SCOPE.md](../../../SCOPE.md). Add the topic here only when a future agent in an unrelated project could reuse the AI working method.

Leave data engineering, data science, application development, and CI/CD to their own repos. Leave one project's requirements and environment in that project. If the user asks for an out-of-scope topic, name the repo that should own it and stop.

## Confirm it is uncovered

```bash
python Search-Index/search.py --list
python Search-Index/search.py "topic words"
```

Search `Best-Practices/`, `Agent-Instructions/`, `Lessons-Learned/`, and `Official-Documentation/`. A hit that answers the question means the topic is covered. Edit that page, or follow [review-covered-ai-topics](../review-covered-ai-topics/SKILL.md) when the task is to refresh it from current sources.

A near match is still covered when the missing part is a paragraph, not a new decision. Add the paragraph there.

## Research before writing

Open a primary source with WebSearch or WebFetch and read the page that supports the rule. Primary sources are the official docs and changelogs in [sources.md](../check-ai-work-updates/sources.md). Stack Overflow and Reddit are leads. Confirm a community claim on a primary page before writing it as a practice.

Quote only the sentence needed, with the URL. Do not paste a manual, book, or release note into the repo.

## Write one page

Follow [Write retrievable knowledge](../../../Best-Practices/09-write-retrievable-knowledge.md).

| Kind of knowledge | Where to put it |
| --- | --- |
| Stable rule for every agent | Next numbered file in `Best-Practices/`, and a row in its README |
| Rule for one product | The matching file in `Agent-Instructions/` |
| Finding from a tested session | Next `LL-####` file, using `Lessons-Learned/_template.md` |

Set `status` to `verified` when a primary source you opened supports the rule. Set `candidate` when the only support is a community post. Do not mark a lesson `verified` unless the check named in the lesson was run in this environment.

One topic per page. Link related pages. Set `updated` to the day you write it.

## Report

```markdown
# Topic added
- Page:
- Why it was uncovered:
- Primary source: [title](url)
- Status:
```

If you refused the topic, say where it belongs.
