## What does this change?

## Security checklist

- [ ] I did not add student data, credentials or personal information.
- [ ] If this changes `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, a lesson or exercise prompt, or a rubric: I did not add instructions to run commands, browse, open links, upload data, change the tutor's role, or bypass the privacy and free-tier rules. The only web reading allowed is the read-only reading of the official course in `AGENTS.md` rule 12.9 and the lesson prompts' "COURSE PAGES" paragraph; I did not widen it.
- [ ] If this changes `.claude/` or `.gemini/`: it only restricts tools and adds no hooks, MCP servers, plugins, allow rules or commands.
- [ ] If this changes `opencode.json`: it adds no hooks, MCP servers, plugins, allow rules or commands. The schema-only file is intentional so OpenCode can read the course.
- [ ] I did not add `.mcp.json`, `.vscode/`, `.cursor/` or `.opencode/`.
- [ ] If this adds a link, a tool or an external resource: it is optional and does not require payment, an account or a paid feature.
- [ ] I kept the Spanish original and the English translation in sync (`docs/translation.md`).
- [ ] `git status` shows no `PROFILE.md`, `progress.json` or `submissions/` content.

## How was it checked?
