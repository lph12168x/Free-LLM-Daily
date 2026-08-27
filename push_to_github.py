#!/usr/bin/env python3
"""Push files to GitHub using local PAT git push.

Uses the fine-grained PAT stored in ~/.git-credentials.
Git push approach — simpler and faster than Contents API.
"""
import os, re, subprocess, datetime, sys

# ── Config ──
cred_path = os.path.expanduser("~/.git-credentials")
with open(cred_path) as f:
    line = f.read().strip()
m = re.search(r"https://[^:]+:([^@]+)@github\.com", line)
TOKEN = m.group(1)
USER = "lph12168x"
REPO = "Free-LLM-Daily"
REMOTE_URL = f"https://{USER}:{TOKEN}@github.com/{USER}/{REPO}.git"

base = os.path.dirname(os.path.abspath(__file__))
os.chdir(base)

today = datetime.date.today().isoformat()

# 0. Always regenerate the prev/next/latest navigation bar on every daily page
#    BEFORE staging. This self-heals the "previous page's Next button not updated"
#    bug: add_nav.py recomputes nav from the actual sorted file list, so adding a
#    new newest report automatically fixes the previous one's "next" link.
print("Regenerating page navigation bars (add_nav.py)...")
subprocess.run([sys.executable, "add_nav.py"], capture_output=True)

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"  ERROR: {r.stderr.strip()}")
    return r.returncode == 0

# 1. Make sure remote is set with PAT
subprocess.run(["git", "remote", "set-url", "origin", REMOTE_URL], capture_output=True)

# 2. Stage all relevant files
for f in ["index.html", "README.md", ".gitignore"]:
    p = os.path.join(base, f)
    if os.path.exists(p):
        subprocess.run(["git", "add", f], capture_output=True)

# Add all daily HTML files
for f in os.listdir(base):
    if f.startswith("daily-free-llm-") and f.endswith(".html"):
        subprocess.run(["git", "add", f], capture_output=True)

# 3. Check if there's anything to commit
r = subprocess.run(["git", "diff", "--cached", "--name-only"], capture_output=True, text=True)
staged = r.stdout.strip()
if not staged:
    print("Nothing to push — all files already up to date.")
else:
    print(f"Staged files:\n{staged}")
    # 4. Commit & push
    if run(["git", "commit", "-m", f"daily: {today} 免费大模型日报"]):
        if run(["git", "push", "origin", "main"]):
            print(f"\nPushed! https://github.com/{USER}/{REPO}")
        else:
            print("\nPush failed.")
    else:
        print("\nCommit failed.")
