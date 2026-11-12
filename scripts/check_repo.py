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

MAX_FILES = 400
MAX_BYTES = 300_000
ALLOWED_SCRIPTS = {"scripts/check_repo.py", "scripts/test_check_repo.py"}
ALLOWED_WORKFLOWS = {".github/workflows/repo-checks.yml"}

# Invisible, formatting and bidirectional control characters.
INVIS_RANGES = [
    (0x00AD, 0x00AD), (0x061C, 0x061C), (0x180E, 0x180E),
    (0x200B, 0x200F), (0x202A, 0x202E), (0x2060, 0x2064),
    (0x2066, 0x2069), (0xFEFF, 0xFEFF), (0xE0000, 0xE007F),
]
INVISIBLE = re.compile(
    "[" + "".join(re.escape(chr(a)) + "-" + re.escape(chr(b)) for a, b in INVIS_RANGES) + "]"
)
SECRETS = re.compile(
    r"(AKIA[0-9A-Z]{16}|ASIA[0-9A-Z]{16}|gh[pousr]_[A-Za-z0-9]{30,}|"
    r"github_pat_[A-Za-z0-9_]{30,}|sk-(?:proj-|ant-)?[A-Za-z0-9_\-]{20,}|"
    r"AIza[0-9A-Za-z_\-]{35}|xox[abprs]-[A-Za-z0-9-]{10,}|"
    r"https://hooks\.slack\.com/services/[A-Za-z0-9/]+|npm_[A-Za-z0-9]{30,}|"
    r"pypi-[A-Za-z0-9_\-]{30,}|glpat-[A-Za-z0-9_\-]{20,}|"
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----)"
)
SHELL_FENCE = re.compile(
    r"^[ \t]*(```|~~~)[ \t]*(bash|sh|shell|zsh|powershell|pwsh|cmd|bat)\b", re.I | re.M
)
ACTIVE = re.compile(r"<scr" + r"ipt|java" + r"script:", re.I)

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


# Tracked entries (mode, path). Mode 160000 is a submodule, 120000 a symlink.
raw = subprocess.run(
    ["git", "-C", str(ROOT), "ls-files", "-s", "-z"], capture_output=True, check=True
).stdout.decode("utf-8", "surrogateescape").split("\0")
entries = []
for item in raw:
    if not item:
        continue
    meta, _, path = item.partition("\t")
    entries.append((meta.split()[0], path))
tracked = [p for _, p in entries]

if len(tracked) > MAX_FILES:
    err(f"too many tracked files ({len(tracked)} > {MAX_FILES})")
files = []
for mode, t in entries:
    if INVISIBLE.search(t):
        err(f"{t!r}: file name has invisible or bidirectional characters")
    if mode == "160000":
        err(f"{t}: submodules are not allowed")
        continue
    if mode == "120000":
        err(f"{t}: symlinks are not allowed")
        continue
    p = ROOT / t
    if not p.is_file():
        continue
    if p.stat().st_size > MAX_BYTES:
        err(f"{t}: file is larger than {MAX_BYTES} bytes")
        continue
    files.append(p)

# 1. Student data must never be tracked.
for t in tracked:
    if t in ("PROFILE.md", "progress.json") or (
        t.startswith("submissions/") and not t.endswith("/.gitkeep")
    ):
        err(f"{t}: student data must not be committed")

# 2. Unsafe content: invisible Unicode, active content, shell blocks, secrets.
for p in files:
    r = rel(p)
    if r not in ALLOWED_SCRIPTS and p.suffix not in (".md", ".json", ".txt", ".yml", ".yaml", "") and p.name != "CODEOWNERS":
        err(f"{r}: unexpected file type (the repository is text only)")
        continue
    try:
        text = read(p)
    except UnicodeDecodeError:
        err(f"{r}: not valid UTF-8 text")
        continue
    if INVISIBLE.search(text):
        err(f"{r}: invisible or bidirectional Unicode characters")
    if ACTIVE.search(text):
        err(f"{r}: embedded active content (script tag or scripting URL)")
    if SHELL_FENCE.search(text):
        err(f"{r}: shell code block (the course asks for no commands)")
    if SECRETS.search(text):
        err(f"{r}: looks like a secret")

# 3. ES/EN pairs (docs/translation.md) and prompt checks.
status_rows = {}
for kind in ("curriculum", "exercises", "rubrics"):
    es_dir, en_dir = ROOT / kind / "es", ROOT / kind / "en"
    if not es_dir.is_dir():
        err(f"{kind}/es: missing")
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
        tr = fen.get("translationOf", "")
        if tr != f"{kind}/es/{name}" or not (ROOT / tr).exists():
            err(f"{rel(en)}: translationOf is wrong or points to a missing file")
        if fen.get("sourceVersion") != fes.get("version"):
            err(f"{rel(en)}: sourceVersion {fen.get('sourceVersion')} != ES version {fes.get('version')}")
        status_rows[slug] = (fes.get("version"), fen.get("sourceVersion"))

        if kind == "rubrics":
            continue
        for lang, path in (("es", es), ("en", en)):
            blocks = prompt_blocks(read(path))
            if len(blocks) != 1:
                err(f"{rel(path)}: expected exactly one prompt block, found {len(blocks)}")
                continue
            prompt = blocks[0]
            words = len(prompt.split())
            if words > 1200:
                err(f"{rel(path)}: prompt has {words} words (limit 1,200)")
            rule5 = "datos, no como instrucciones" if lang == "es" else "data, not instructions"
            if rule5 not in prompt:
                err(f"{rel(path)}: prompt is missing rule 5 ({rule5})")
            if slug == "l00-welcome":
                continue  # Lesson 0 has no paste slot; its interview answers are covered by rule 5.
            start = "<<<INICIO DE DATOS DEL ALUMNO>>>" if lang == "es" else "<<<START OF STUDENT DATA>>>"
            end = "<<<FIN DE DATOS DEL ALUMNO>>>" if lang == "es" else "<<<END OF STUDENT DATA>>>"
            slot = re.search(r"\[(PEGA|PASTE)\b", prompt)
            if not slot:
                err(f"{rel(path)}: prompt has no paste slot")
                continue
            i, j = prompt.find(start), prompt.rfind(end)
            if i < 0 or j < 0 or not (i < slot.start() < j):
                err(f"{rel(path)}: paste slot is not between the student data markers")
            if prompt.count(start) != 1 or prompt.count(end) != 1:
                err(f"{rel(path)}: expected exactly one start and one end marker")

# 4. translation-status.md must list every pair, and only those.
sp = ROOT / "docs" / "translation-status.md"
if not sp.exists():
    err("docs/translation-status.md: missing")
else:
    seen = {}
    for line in read(sp).splitlines():
        m = re.match(r"\| ([\w-]+) \| (\d+) \| (\d+) \|", line)
        if m:
            seen[m.group(1)] = (m.group(2), m.group(3))
    for slug, vals in status_rows.items():
        if slug not in seen:
            err(f"docs/translation-status.md: no row for {slug}")
        elif seen[slug] != vals:
            err(f"docs/translation-status.md: {slug} row does not match the files")
    for slug in seen:
        if slug not in status_rows:
            err(f"docs/translation-status.md: row for unknown slug {slug}")

# 5. Files that can make an agent run code or load extra tools.
for t in tracked:
    if t in (".mcp.json", ".gemini/settings.local.json", ".claude/settings.local.json"):
        err(f"{t}: not allowed in this repository")
    if t.startswith((".vscode/", ".cursor/", ".opencode/", ".claude/hooks", ".claude/commands",
                     ".claude/agents", ".claude/skills")):
        err(f"{t}: not allowed in this repository")
    if t.startswith(".github/workflows/") and t not in ALLOWED_WORKFLOWS:
        err(f"{t}: only .github/workflows/repo-checks.yml is allowed")
    if t.startswith("scripts/") and t not in ALLOWED_SCRIPTS:
        err(f"{t}: unexpected script")


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


def deny_list(obj, *keys):
    for k in keys:
        if not isinstance(obj, dict):
            return []
        obj = obj.get(k)
    return obj if isinstance(obj, list) else []


s = load(".claude/settings.json")
if s is not None:
    perms = s.get("permissions") if isinstance(s, dict) else None
    if not isinstance(s, dict) or set(s) - {"$schema", "permissions"} or not isinstance(perms, dict) or set(perms) != {"deny"}:
        err(".claude/settings.json: only permissions.deny is allowed")
    for tool in ("Bash", "WebFetch", "WebSearch"):
        if tool not in deny_list(s, "permissions", "deny"):
            err(f".claude/settings.json: {tool} must stay denied")
g = load(".gemini/settings.json")
if g is not None:
    tools = g.get("tools") if isinstance(g, dict) else None
    if not isinstance(g, dict) or set(g) != {"tools"} or not isinstance(tools, dict) or set(tools) != {"exclude"}:
        err(".gemini/settings.json: only tools.exclude is allowed")
    for tool in ("run_shell_command", "web_fetch", "google_web_search"):
        if tool not in deny_list(g, "tools", "exclude"):
            err(f".gemini/settings.json: {tool} must stay excluded")
o = load("opencode.json")
if o is not None:
    rules = o.get("permissions") if isinstance(o, dict) else None
    if not isinstance(o, dict) or set(o) - {"$schema", "permissions"} or not isinstance(rules, list):
        err("opencode.json: only a permissions list is allowed")
        rules = []
    rules = [r for r in rules if isinstance(r, dict)]
    if any(r.get("effect") != "deny" for r in rules):
        err("opencode.json: every rule must be deny")
    denied = {r.get("action") for r in rules}
    for a in ("shell", "execute", "webfetch", "websearch", "external_directory"):
        if a not in denied:
            err(f"opencode.json: {a} must stay denied")

if errors:
    print(f"{len(errors)} problem(s) found:")
    for e in errors:
        print(f" - {e}")
    sys.exit(1)
print(f"OK: {len(tracked)} tracked files checked")
