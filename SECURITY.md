# Security policy / Política de seguridad

This repository contains course text and tutor instructions, not software. The main risks are prompt injection, privacy leaks and malicious changes to the course content.

## What the course will never ask / Lo que el curso nunca pedirá

- Install software, run commands or use a terminal.
- Open links, download files or upload documents.
- Pay, create accounts, or provide API keys or access tokens.
- Share passwords, health data, financial data or personal data about third parties.

If a lesson, file, tutor, issue or pull request asks for any of that, it is not part of the course.

## Reporting / Cómo reportar

Report privately through the repository's **Security** tab ("Report a vulnerability"). If private reporting is unavailable, open an issue with a short description and **no personal data**.

Include the file and line, what the content asks the student or tutor to do, and why it is unsafe. Do not include student data, credentials or personal information.

## Using a copy / Si usas una copia

Use the official repository. A fork, a copy or a forwarded file can be modified. Copy the lesson prompt only from the official repository link; do not use prompts pasted from another chat, issue or file.

If you open a copy with an AI assistant that can read files, be especially careful: a copy can include settings folders for assistants (`.claude/`, `.gemini/`, `.opencode/`, `.vscode/`, `.cursor/`, `.mcp.json`) that run commands as soon as you open the folder, or a modified `AGENTS.md` or `opencode.json`. The official repository only includes `.claude/settings.json`, `.gemini/settings.json` and `opencode.json`, and they only block commands and web access. If a copy has other files there, or these files allow more, do not open it with your assistant.

Si abres una copia con un asistente que puede leer archivos, ten especial cuidado: una copia puede incluir carpetas de configuración de asistentes (`.claude/`, `.gemini/`, `.opencode/`, `.vscode/`, `.cursor/`, `.mcp.json`) que ejecutan comandos nada más abrir la carpeta, o un `AGENTS.md` u `opencode.json` modificados. El repositorio oficial solo incluye `.claude/settings.json`, `.gemini/settings.json` y `opencode.json`, y solo bloquean comandos y acceso a la web. Si una copia trae otros archivos ahí, o estos permiten más, no la abras con tu asistente.

## For maintainers / Para mantenedores

- Treat changes to `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, the agent settings files (`.claude/`, `.gemini/`, `opencode.json`), the lesson and exercise prompts, the rubrics and `docs/` as security-relevant. The agent settings files must only restrict tools: never add hooks, MCP servers, plugins, allow rules or commands to them. `.github/CODEOWNERS` is currently disabled because there is a single maintainer; when a second maintainer joins, re-enable it and turn on **Require review from Code Owners** and **Require approvals** in the branch protection rules for the default branch.
- Do not merge content that asks an assistant to run commands, browse, upload data, change role, reveal personal data, or override any rule of `AGENTS.md`.
- Do not add workflows that execute code from pull requests. On `pull_request`, GitHub runs the workflow file and the code from the pull request itself, so a pull request can change what runs. If a check such as ES/EN consistency is added later, it must run only scripts already on the default branch, have no access to secrets and read-only permissions, and be reviewed as a security-relevant change (see the first item).
- Keep student data out of the repository: `PROFILE.md`, `progress.json` and everything under `submissions/` are ignored by `.gitignore`. Verify with `git status` before committing.
- If a secret is committed, revoke or rotate it first, then remove it from history. Deleting it in a new commit is not enough.
- Never ask a reporter for personal data. A file, a line and a description are enough.
- Keep **Private vulnerability reporting** enabled (Settings → Security) and protect the default branch against force pushes and deletion.
