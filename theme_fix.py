# -*- coding: utf-8 -*-
"""Repair the theme / scroll-top JavaScript in a generated daily report.

Why this exists
---------------
The shared HTML template inherited from earlier reports ships a theme-toggle
button and a scroll-top button, but contains NO <script> at all:

  * <html> hardcodes data-theme="dark", so every page renders dark and the
    toggle button does nothing (toggleTheme() is never defined).
  * .scroll-top is hidden by default and only becomes usable via a `.visible`
    class that nothing ever adds.

This module fixes both, and is safe to re-run (it is idempotent).

Usage
-----
    python theme_fix.py daily-free-llm-YYYY-MM-DD.html
"""
import io
import re
import sys

# A sun / moon glyph pair written as raw characters so we never have to deal
# with UTF-16 surrogate-pair escapes inside Python string literals.
ICON_DARK = "\U0001F319"   # moon
ICON_LIGHT = "☀"           # sun (+ optional variation selector appended in JS)

HEAD_JS_TEMPLATE = u"""<script>
(function () {
  var KEY = 'fllm-daily-theme';
  var root = document.documentElement;
  var stored = null;
  try { stored = localStorage.getItem(KEY); } catch (e) {}
  if (stored !== 'light' && stored !== 'dark') {
    stored = (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) ? 'dark' : 'light';
  }
  root.setAttribute('data-theme', stored);

  function syncIcon() {
    var icon = document.getElementById('theme-icon');
    if (icon) icon.textContent = (root.getAttribute('data-theme') === 'dark') ? '__ICON_DARK__' : '__ICON_LIGHT__';
  }

  window.toggleTheme = function () {
    var next = (root.getAttribute('data-theme') === 'dark') ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem(KEY, next); } catch (e) {}
    syncIcon();
  };

  document.addEventListener('DOMContentLoaded', function () {
    syncIcon();
    var st = document.getElementById('scrollTop');
    if (st) {
      var onScroll = function () { st.classList.toggle('visible', window.scrollY > 400); };
      window.addEventListener('scroll', onScroll, { passive: true });
      onScroll();
    }
  });
})();
</script>
"""


def fix(path, date_str=None):
    html = io.open(path, encoding="utf-8").read()
    changed = []

    # 1) No-JS fallback should be light, not dark (matches the IDE theme).
    if '<html lang="zh-CN" data-theme="dark">' in html:
        html = html.replace('<html lang="zh-CN" data-theme="dark">',
                            '<html lang="zh-CN" data-theme="light">')
        changed.append("html[data-theme] dark -> light")

    # 2) Correct the <title> date to the report's own date.
    if date_str:
        new_title = u"免费大模型日报 · %s · Free LLM Daily" % date_str
        html, n = re.subn(r"免费大模型日报 · \d{4}-\d{2}-\d{2} · Free LLM Daily",
                          lambda m: new_title, html, count=1)
        if n:
            changed.append("title -> %s" % date_str)

    # 3) Inject the head script exactly once, right after </style>.
    if "fllm-daily-theme" not in html:
        js = (HEAD_JS_TEMPLATE
              .replace("__ICON_DARK__", ICON_DARK)
              .replace("__ICON_LIGHT__", ICON_LIGHT))
        html = html.replace("</style>", "</style>\n" + js, 1)
        changed.append("head script injected")

    if changed:
        io.open(path, "w", encoding="utf-8").write(html)

    return changed


if __name__ == "__main__":
    target = sys.argv[1]
    # Date can be passed explicitly; otherwise derive it from the filename.
    if len(sys.argv) > 2:
        d = sys.argv[2]
    else:
        m = re.search(r"(\d{4}-\d{2}-\d{2})", target)
        d = m.group(1) if m else None
    result = fix(target, d)
    print(target, "->", result if result else "no changes (already patched)")
