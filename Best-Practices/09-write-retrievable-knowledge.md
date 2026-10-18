---
title: Write retrievable knowledge
tags: [practices, retrieval, writing]
status: verified
updated: 2026-10-17
---

# Write retrievable knowledge

Write so a later search can find the page and a later agent can apply it without the original session.

## Frontmatter

Every markdown document starts with:

```yaml
---
title: Short specific title
tags: [practices, retrieval]
status: verified
updated: 2026-10-17
---
```

Lessons also include `id`, `environment`, and `superseded_by` as in the template.

Tags are lowercase words a search would use: `retrieval`, `lessons`, `mcp`, `security`, `prompting`, `verification`.

## One topic per page

Split a note that answers two unrelated questions. A search hit should be something you can apply, not a journal of the whole day.

## Shape

- Open with the rule or the result.
- Name the situation where it applies.
- Give the steps or the decision test.
- Name the evidence: command, doc, or review.
- Link the canonical related page instead of copying it.

## Titles

Use the words a future agent will search. "Verify and record" is retrievable. "Thoughts" is not.

## Maintenance

When you change product behavior guidance, update `updated` and re-check the official documentation named in the page. When you replace a page, mark the old one `superseded` and set `superseded_by` to the new path.
