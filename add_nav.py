#!/usr/bin/env python3
# Add / regenerate prev/next/home/latest navigation bar on ALL daily-free-llm-*.html pages.
#
# Idempotent & self-healing: it recomputes prev/next/latest for EVERY file on each run
# from the actual sorted file list, so adding a new newest report automatically fixes the
# previous newest report's "next" link (the bug this guards against). It also refreshes the
# "latest" pointer everywhere. CSS is injected only once (guarded by a marker comment).
import os, re, glob

base = os.path.dirname(os.path.abspath(__file__))
pat = re.compile(r"daily-free-llm-(\d{4})-(\d{2})-(\d{2})\.html$")

entries = []
for f in glob.glob(os.path.join(base, "daily-free-llm-*.html")):
    m = pat.search(f)
    if m:
        d = (int(m.group(1)), int(m.group(2)), int(m.group(3)))
        entries.append((d, os.path.basename(f)))
entries.sort()
names = [e[1] for e in entries]
print(f"Found {len(names)} daily reports; latest = {names[-1]}")

nav_css = '''
  /* Page navigation bar (prev / home / latest / next) */
  .page-nav {
    position: fixed; top: 16px; left: 12px; z-index: 1000;
    display: flex; gap: 6px; padding: 6px; border-radius: 30px;
    background: var(--bg-card); border: 1.5px solid var(--border-card);
    backdrop-filter: blur(10px); box-shadow: 0 4px 20px rgba(0,0,0,0.12);
    max-width: calc(100vw - 90px); flex-wrap: wrap; align-items: center;
  }
  .page-nav a, .page-nav span.nav-disabled {
    padding: 7px 13px; border-radius: 20px; font-size: 13px; font-weight: 600;
    text-decoration: none; color: var(--text-primary); white-space: nowrap;
    border: 1px solid var(--border-card); transition: all 0.25s; line-height: 1.3;
  }
  .page-nav a:hover { border-color: var(--accent-1); background: var(--bg-card-hover); color: var(--accent-1); }
  .page-nav a.nav-home { color: var(--accent-2); }
  .page-nav a.nav-latest { color: var(--accent-1); }
  .page-nav span.nav-disabled { color: var(--text-muted); opacity: 0.4; cursor: not-allowed; }
  @media (max-width: 640px) {
    .page-nav { top: 10px; left: 8px; gap: 4px; padding: 5px; max-width: calc(100vw - 70px); }
    .page-nav a, .page-nav span.nav-disabled { padding: 5px 9px; font-size: 11.5px; }
  }
'''

css_marker = "Page navigation bar (prev / home / latest / next)"
nav_div_re = re.compile(r'<div class="page-nav">.*?</div>\n?', re.S)

changed = 0
for i, name in enumerate(names):
    path = os.path.join(base, name)
    with open(path, encoding="utf-8") as fh:
        html = fh.read()

    prev = names[i-1] if i > 0 else None
    nxt = names[i+1] if i < len(names)-1 else None
    latest = names[-1]
    home = "index.html"

    items = []
    items.append(f'<a href="{prev}" title="上一篇日报">← 上一个</a>' if prev
                 else '<span class="nav-disabled">← 上一个</span>')
    items.append(f'<a class="nav-home" href="{home}" title="返回首页">🏠 主页</a>')
    items.append(f'<a class="nav-latest" href="{latest}" title="最新日报">⭐ 最新</a>')
    items.append(f'<a href="{nxt}" title="下一篇日报">下一个 →</a>' if nxt
                 else '<span class="nav-disabled">下一个 →</span>')

    nav_html = '<div class="page-nav">' + "".join(items) + '</div>\n'

    original = html

    # 1) Inject CSS once (guarded by marker).
    if css_marker not in html:
        html = html.replace("</style>", nav_css + "</style>", 1)

    # 2) Replace existing nav div if present, else inject at anchor.
    if 'class="page-nav"' in html:
        html = nav_div_re.sub(nav_html, html, count=1)
    elif 'class="back-home"' in html:
        html = re.sub(r'<a class="back-home"[^>]*>[^<]*</a>', nav_html.strip(), html, count=1)
    elif '<div class="container">' in html:
        html = html.replace('<div class="container">', nav_html + '<div class="container">', 1)
    else:
        print(f"  WARN: no anchor found in {name}")
        continue

    if html != original:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(html)
        changed += 1
        tag = "regenerated" if 'class="page-nav"' in original else "added"
        print(f"  {tag}: {name}  (prev={'Y' if prev else 'N'} next={'Y' if nxt else 'N'} latest={latest})")
    else:
        print(f"  unchanged: {name}")

print(f"Done. {changed} file(s) updated.")
