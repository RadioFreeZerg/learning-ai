#!/usr/bin/env python3
"""Consistency and safety checks for the course repository.

Usage: python3 -I scripts/check_repo.py <path-to-repo-checkout>

Standard library only. It reads files as data and never executes them.
Exit code 1 if any check fails.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

if len(sys.argv) != 2:
    sys.exit("usage: check_repo.py <repo-dir>")
ROOT = Path(sys.argv[1]).resolve()
errors = []


def err(msg):
    errors.append(msg)


def rel(p):
    return str(p.relative_to(ROOT))


def frontmatter(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    out = {}
    if m:
        for line in m.group(1).splitlines():
            k, sep, v = line.partition(":")
            if sep and not line.startswith(" "):
                out[k.strip()] = v.strip()
    return out


def prompt_blocks(text):
    return re.findall(r"```text\n(.*?)```", text, re.S)


def read(p):
    return p.read_text(encoding="utf-8")


# Tracked files only: untracked local files are not part of the repository.
tracked = subprocess.run(
    ["git", "-C", str(ROOT), "ls-files", "-z"], capture_output=True, check=True
).stdout.decode().split("\0")
tracked = [t for t in tracked if t]
files = [ROOT / t for t in tracked if (ROOT / t).is_file() and not (ROOT / t).is_symlink()]
for t in tracked:
    if (ROOT / t).is_symlink():
        err(f"{t}: symlinks are not allowed")

# 1. Student data must never be tracked.
for t in tracked:
    if t in ("PROFILE.md", "progress.json") or (
        t.startswith("submissions/") and not t.endswith("/.gitkeep")
    ):
        err(f"{t}: student data must not be committed")

# 2. Unsafe content: invisible Unicode, scripts, shell fences, secrets.
INVISIBLE = re.compile("[​-‏‪-‮⁠-⁤﻿\U000e0000-\U000e007f]")
SECRETS = re.compile(
    r"(AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|"
    r"sk-[A-Za-z0-9]{20,}|AIza[0-9A-Za-z_\-]{35}|xox[bp]-[A-Za-z0-9-]{10,}|"
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----)"
)
for p in files:
    if rel(p) != "scripts/check_repo.py" and p.suffix not in (".md", ".json", ".txt", ".yml", ".yaml", "") and p.name != "CODEOWNERS":
        err(f"{rel(p)}: unexpected file type (the repository is text only)")
        continue
    try:
        text = read(p)
    except UnicodeDecodeError:
        err(f"{rel(p)}: not valid UTF-8 text")
        continue
    if INVISIBLE.search(text):
        err(f"{rel(p)}: invisible or bidirectional Unicode characters")
    if re.search(r"<script|javascript:", text, re.I):
        err(f"{rel(p)}: script or javascript: URL")
    if re.search(r"```(bash|sh|shell|zsh|powershell|cmd|bat)\b", text, re.I):
        err(f"{rel(p)}: shell code block (the course asks for no commands)")
    if SECRETS.search(text):
        err(f"{rel(p)}: looks like a secret")

# 3. ES/EN pairs (docs/translation.md) and prompt checks.
status_rows = {}
for kind in ("curriculum", "exercises", "rubrics"):
    es_dir, en_dir = ROOT / kind / "es", ROOT / kind / "en"
    if not es_dir.is_dir():
        continue
    es_names = {p.name for p in es_dir.glob("*.md")}
    en_names = {p.name for p in en_dir.glob("*.md")}
    for name in sorted(es_names ^ en_names):
        err(f"{kind}/{name}: missing in one language")
    for name in sorted(es_names & en_names):
        es, en = es_dir / name, en_dir / name
        fes, fen = frontmatter(read(es)), frontmatter(read(en))
        slug = name[:-3]
        if fes.get("slug") != slug or fen.get("slug") != slug:
            err(f"{rel(es)} / {rel(en)}: slug does not match the file name")
        if fes.get("lang") != "es" or fen.get("lang") != "en":
            err(f"{kind}/{name}: wrong lang field")
        if fen.get("translationOf") != f"{kind}/es/{name}" or not (ROOT / fen.get("translationOf", "x")).exists():
            err(f"{rel(en)}: translationOf is wrong or points to a missing file")
        if fen.get("sourceVersion") != fes.get("version"):
            err(f"{rel(en)}: sourceVersion {fen.get('sourceVersion')} != ES version {fes.get('version')}")
        status_rows[slug] = (fes.get("version"), fen.get("sourceVersion"))

        if kind == "rubrics":
            continue
        for lang, path in (("es", es), ("en", en)):
            blocks = prompt_blocks(read(path))
            if not blocks:
                err(f"{rel(path)}: no prompt block")
                continue
            prompt = max(blocks, key=len)
            words = len(prompt.split())
            if words > 1200:
                err(f"{rel(path)}: prompt has {words} words (limit 1,200)")
            rule5 = "datos, no como instrucciones" if lang == "es" else "data, not instructions"
            if rule5 not in prompt:
                err(f"{rel(path)}: prompt is missing rule 5 ({rule5})")
            has_slot = re.search(r"\[(PEGA|PASTE)\b", prompt)
            start = "<<<INICIO DE DATOS DEL ALUMNO>>>" if lang == "es" else "<<<START OF STUDENT DATA>>>"
            end = "<<<FIN DE DATOS DEL ALUMNO>>>" if lang == "es" else "<<<END OF STUDENT DATA>>>"
            if has_slot:
                i, j = prompt.find(start), prompt.find(end)
                slot = re.search(r"\[(PEGA|PASTE)\b", prompt)
                if i < 0 or j < 0 or not (i < slot.start() < j):
                    err(f"{rel(path)}: paste slot is not between the student data markers")

# 4. translation-status.md matches the files.
sp = ROOT / "docs" / "translation-status.md"
if sp.exists():
    for line in read(sp).splitlines():
        m = re.match(r"\| ([\w-]+) \| (\d+) \| (\d+) \|", line)
        if m and m.group(1) in status_rows:
            if (m.group(2), m.group(3)) != status_rows[m.group(1)]:
                err(f"docs/translation-status.md: {m.group(1)} row does not match the files")

# 5. Agent settings may only restrict tools.
for forbidden in (".mcp.json", ".vscode/tasks.json", ".vscode/settings.json"):
    if forbidden in tracked:
        err(f"{forbidden}: not allowed in this repository")
for t in tracked:
    if t.startswith((".cursor/", ".opencode/", ".claude/hooks", ".claude/commands", ".claude/agents", ".claude/skills")):
        err(f"{t}: not allowed in this repository")


def load(path):
    p = ROOT / path
    if not p.exists():
        err(f"{path}: missing")
        return None
    try:
        return json.loads(read(p))
    except json.JSONDecodeError as e:
        err(f"{path}: invalid JSON ({e})")
        return None


s = load(".claude/settings.json")
if s is not None:
    if set(s) - {"$schema", "permissions"} or set(s.get("permissions", {})) != {"deny"}:
        err(".claude/settings.json: only permissions.deny is allowed")
    for tool in ("Bash", "WebFetch", "WebSearch"):
        if tool not in s.get("permissions", {}).get("deny", []):
            err(f".claude/settings.json: {tool} must stay denied")
g = load(".gemini/settings.json")
if g is not None:
    if set(g) != {"tools"} or set(g["tools"]) != {"exclude"}:
        err(".gemini/settings.json: only tools.exclude is allowed")
    for tool in ("run_shell_command", "web_fetch", "google_web_search"):
        if tool not in g.get("tools", {}).get("exclude", []):
            err(f".gemini/settings.json: {tool} must stay excluded")
o = load("opencode.json")
if o is not None:
    if set(o) - {"$schema", "permissions"}:
        err("opencode.json: only permissions is allowed")
    rules = o.get("permissions", [])
    if any(r.get("effect") != "deny" for r in rules):
        err("opencode.json: every rule must be deny")
    denied = {r.get("action") for r in rules}
    for a in ("shell", "execute", "webfetch", "websearch"):
        if a not in denied:
            err(f"opencode.json: {a} must stay denied")

if errors:
    print(f"{len(errors)} problem(s) found:")
    for e in errors:
        print(f" - {e}")
    sys.exit(1)
print(f"OK: {len(tracked)} tracked files checked")
