# Sources for AI work updates

The fetch script reads the `sources` block. `feed` entries are RSS or Atom. `page` entries have no feed; open them with WebFetch during the check.

`primary` sources can change a practice page after you read the linked item. `community` sources are leads. Confirm a community claim on a primary page before editing `Best-Practices/` or `Agent-Instructions/`.

```sources
feed	Cursor changelog	https://cursor.com/changelog/rss.xml	primary
feed	Cursor release notes	https://cursor.com/docs/release-notes/rss.xml	primary
feed	OpenAI developers	https://developers.openai.com/rss.xml	primary
feed	Codex changelog	https://developers.openai.com/codex/changelog/rss.xml	primary
feed	OpenAI news	https://openai.com/news/rss.xml	primary
feed	Claude Code changelog	https://code.claude.com/docs/en/changelog/rss.xml	primary
feed	MCP releases	https://github.com/modelcontextprotocol/modelcontextprotocol/releases.atom	primary
page	Anthropic newsroom	https://www.anthropic.com/news	primary
page	MCP draft changelog	https://modelcontextprotocol.io/specification/draft/changelog	primary
page	OpenAI release notes	https://openai.com/products/release-notes/	primary
feed	Stack Overflow	https://stackoverflow.com/feeds/tag?tagnames=openai+or+claude+or+anthropic+or+chatgpt+or+codex+or+model-context-protocol&sort=newest	community
feed	Reddit r/cursor top week	https://www.reddit.com/r/cursor/top/.rss?t=week	community
feed	Reddit r/ClaudeAI top week	https://www.reddit.com/r/ClaudeAI/top/.rss?t=week	community
feed	Reddit r/OpenAI top week	https://www.reddit.com/r/OpenAI/top/.rss?t=week	community
feed	Reddit r/ChatGPTCoding top week	https://www.reddit.com/r/ChatGPTCoding/top/.rss?t=week	community
```

Add a line to the block when a new official changelog appears. Keep domain product docs out of this list.

Stack Overflow is the newest questions on those AI-agent tags. Treat them as community leads, the same way as Reddit. Confirm a claim on a primary page before editing a practice.

Reddit often refuses the RSS URL. When a community feed fails, search the web for that subreddit's recent posts about agent workflows instead of treating the source as empty.
