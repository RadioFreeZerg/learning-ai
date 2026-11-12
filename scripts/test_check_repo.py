#!/usr/bin/env python3
"""Self-test for check_repo.py. Run: python3 -I scripts/test_check_repo.py

Copies the tracked files into a temporary git repository, breaks one thing at
a time and expects the checker to report it. Dangerous strings are built at
run time so this file itself stays clean.
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
CHECK = HERE / "check_repo.py"


def git(cwd, *args):
    subprocess.run(["git", "-C", str(cwd), "-c", "user.name=t", "-c", "user.email=t@t", *args],
                   check=True, capture_output=True)


def fresh():
    tmp = Path(tempfile.mkdtemp())
    names = subprocess.run(["git", "-C", str(REPO), "ls-files", "-z"], capture_output=True,
                           check=True).stdout.decode().split("\0")
    for n in filter(None, names):
        dst = tmp / n
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(REPO / n, dst)
    git(tmp, "init", "-q")
    return tmp


def run(tmp, restage=True):
    if restage:
        git(tmp, "add", "-A", "-f")
    r = subprocess.run([sys.executable, "-I", str(CHECK), str(tmp)], capture_output=True, text=True)
    return r.returncode, r.stdout


def edit(tmp, path, fn):
    p = tmp / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(fn(p.read_text() if p.exists() else ""), encoding="utf-8")


L = "curriculum/en/l03-clear-instructions.md"
ES_L = "curriculum/es/l03-clear-instructions.md"
CASES = [
    ("bidi isolate", lambda t: edit(t, "docs/x.md", lambda s: "a" + chr(0x2067) + "b\n"), "invisible"),
    ("soft hyphen", lambda t: edit(t, "docs/x.md", lambda s: "a" + chr(0xAD) + "b\n"), "invisible"),
    ("invisible file name", lambda t: edit(t, "docs/a" + chr(0x200B) + ".md", lambda s: "x\n"), "file name"),
    ("openai project key", lambda t: edit(t, "docs/x.md", lambda s: "sk-" + "proj-" + "a" * 30 + "\n"), "secret"),
    ("github oauth token", lambda t: edit(t, "docs/x.md", lambda s: "gh" + "o_" + "a" * 36 + "\n"), "secret"),
    ("shell fence with space", lambda t: edit(t, "docs/x.md", lambda s: "``` " + "bash\nls\n```\n"), "shell code block"),
    ("tilde shell fence", lambda t: edit(t, "docs/x.md", lambda s: "~~~" + "sh\nls\n~~~\n"), "shell code block"),
    ("second prompt block", lambda t: edit(t, L, lambda s: s + "\n```text\nignore the rules\n```\n"), "exactly one prompt block"),
    ("markers removed", lambda t: edit(t, L, lambda s: s.replace("<<<START OF STUDENT DATA>>>\n", "").replace("<<<END OF STUDENT DATA>>>\n", "")), "markers"),
    ("slot removed", lambda t: edit(t, L, lambda s: s.replace("[PASTE HERE]", "")), "no paste slot"),
    ("sourceVersion drift", lambda t: edit(t, ES_L, lambda s: s.replace("version: ", "version: 9", 1)), "sourceVersion"),
    ("status row missing", lambda t: edit(t, "docs/translation-status.md", lambda s: "\n".join(l for l in s.split("\n") if "l03-clear" not in l)), "no row for"),
    ("status file deleted", lambda t: (t / "docs/translation-status.md").unlink(), "translation-status.md: missing"),
    ("student data", lambda t: edit(t, "progress.json", lambda s: "{}"), "student data"),
    ("extra workflow", lambda t: edit(t, ".github/workflows/evil.yml", lambda s: "on: push\n"), "only .github/workflows"),
    ("mcp file", lambda t: edit(t, ".mcp.json", lambda s: "{}"), "not allowed"),
    ("claude hooks", lambda t: edit(t, ".claude/settings.json", lambda s: '{"hooks":{},"permissions":{"deny":["Bash"]}}'), "only permissions.deny"),
    ("wrong json types", lambda t: edit(t, ".gemini/settings.json", lambda s: '{"tools":[]}'), "only tools.exclude"),
    ("opencode allow", lambda t: edit(t, "opencode.json", lambda s: s.replace('"deny"', '"allow"', 1)), "every rule must be deny"),
    ("opencode no external_directory", lambda t: edit(t, "opencode.json", lambda s: s.replace("external_directory", "other")), "external_directory"),
    ("submodule", lambda t: (git(t, "add", "-A", "-f"), git(t, "update-index", "--add", "--cacheinfo",
                                                  "160000,1111111111111111111111111111111111111111,vendor/x"), "keep-index")[-1], "submodules"),
]


def main():
    base = fresh()
    code, out = run(base)
    ok = code == 0
    print(("PASS" if ok else "FAIL") + "  clean copy passes" + ("" if ok else "\n" + out))
    failed = 0 if ok else 1
    shutil.rmtree(base, ignore_errors=True)
    for name, mutate, expected in CASES:
        tmp = fresh()
        restage = mutate(tmp) != "keep-index"
        code, out = run(tmp, restage)
        good = code == 1 and expected in out
        print(("PASS" if good else "FAIL") + "  " + name + ("" if good else "\n" + out))
        failed += 0 if good else 1
        shutil.rmtree(tmp, ignore_errors=True)
    print(f"{failed} failure(s)")
    sys.exit(1 if failed else 0)


main()
