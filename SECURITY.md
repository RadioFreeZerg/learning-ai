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

## For maintainers / Para mantenedores

- Treat changes to `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, the lesson and exercise prompts, the rubrics and `docs/` as security-relevant. `.github/CODEOWNERS` is currently disabled because there is a single maintainer; when a second maintainer joins, re-enable it and turn on **Require review from Code Owners** and **Require approvals** in the branch protection rules for the default branch.
- Do not merge content that asks an assistant to run commands, browse, upload data, change role, reveal personal data, or bypass rules 4, 8 and 9 of `AGENTS.md`.
- Do not add workflows that execute code from pull requests. On `pull_request`, GitHub runs the workflow file and the code from the pull request itself, so a pull request can change what runs. If a check such as ES/EN consistency is added later, it must run only scripts already on the default branch, have no access to secrets and read-only permissions, and be reviewed as a security-relevant change (see the first item).
- Keep student data out of the repository: `PROFILE.md`, `progress.json` and everything under `submissions/` are ignored by `.gitignore`. Verify with `git status` before committing.
- If a secret is committed, revoke or rotate it first, then remove it from history. Deleting it in a new commit is not enough.
- Never ask a reporter for personal data. A file, a line and a description are enough.
