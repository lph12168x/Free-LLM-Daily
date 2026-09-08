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


# ---------------------------------------------------------------------------
# 柔和配色覆盖层 (soft palette)
# ---------------------------------------------------------------------------
# 问题：早期模板把一批高饱和荧光色写死进 CSS，且不区分主题：
#   * --accent-3 = #f093fb（亮粉）被用作 .focus h2 / .hot .sub / .plat-name
#     的标题色 —— 在亮色主题下白底浅粉，对比度不足 1.6:1，根本读不清；
#   * .warn-line / .ok-line / .drop-line 直接写死 #f5576c / #34d399 / #ef4444
#     （为暗色底调的值），亮色底上刺眼、暗色底上又发灰；
#   * --hot-bg 用「红 + 紫」双色叠加，与全站紫粉主色互相打架。
# 方案：追加一段同优先级、位置更靠后的变量 + 规则覆盖，全部按主题分别定义，
# 全部走低饱和、低不透明度的「色纸」思路，不再用纯色块硬撞。
# 由于选择器优先级与模板一致、位置更靠后，天然胜出；带 marker 可重复执行。

SOFT_BEGIN = "/* === soft-palette:v1 begin === */"
SOFT_END = "/* === soft-palette:v1 end === */"

SOFT_CSS = SOFT_BEGIN + u"""
  :root {
    --accent-1: #a78bfa;
    --accent-2: #f0abfc;
    --accent-3: #c9bdfb;
    --accent-4: #f6a9a9;
    --gradient-title: linear-gradient(135deg, #f7f5ff 0%, #c9bdfb 55%, #a78bfa 100%);
    --gradient-badge: linear-gradient(90deg, #a78bfa, #f0abfc);
    --gradient-date: linear-gradient(135deg, #8b5cf6, #c084fc);
    --stat-num-gradient: linear-gradient(90deg, #c9bdfb, #f0abfc);
    --badge-text: #2a2154;
    --hot-bg: linear-gradient(120deg, rgba(139,92,246,0.10), rgba(236,72,153,0.07));
    --hot-border: rgba(167,139,250,0.26);
    --hl-bg: rgba(139,92,246,0.13);
    --soft-ok: #7ddcae;
    --soft-warn: #f2cd7a;
    --soft-bad: #f4a3a3;
    --soft-info: #9ec2f7;
    --soft-mute: #97a3b8;
    --soft-ok-bg: rgba(16,185,129,0.13);
    --soft-warn-bg: rgba(217,119,6,0.16);
    --soft-bad-bg: rgba(220,38,38,0.14);
    --soft-info-bg: rgba(59,130,246,0.14);
    --rank-other-bg: rgba(139,92,246,0.5);
    --gold-border: rgba(251,191,36,0.34);
  }

  [data-theme="light"] {
    --accent-1: #7c3aed;
    --accent-2: #c026d3;
    --accent-3: #6d28d9;
    --accent-4: #b05252;
    --gradient-title: linear-gradient(135deg, #4c1d95 0%, #7c3aed 50%, #a78bfa 100%);
    --gradient-badge: linear-gradient(90deg, #7c3aed, #c026d3);
    --gradient-date: linear-gradient(135deg, #6d28d9, #a855f7);
    --stat-num-gradient: linear-gradient(90deg, #6d28d9, #b4536f);
    --badge-text: #ffffff;
    --hot-bg: linear-gradient(120deg, rgba(124,58,237,0.06), rgba(192,38,211,0.045));
    --hot-border: rgba(124,58,237,0.20);
    --hl-bg: rgba(124,58,237,0.075);
    --soft-ok: #0f7a5f;
    --soft-warn: #a2670a;
    --soft-bad: #b45252;
    --soft-info: #245cc4;
    --soft-mute: #6b7280;
    --soft-ok-bg: rgba(5,150,105,0.10);
    --soft-warn-bg: rgba(202,138,4,0.10);
    --soft-bad-bg: rgba(200,60,60,0.075);
    --soft-info-bg: rgba(37,99,235,0.075);
    --rank-other-bg: #8b5cf6;
    --gold-border: rgba(202,138,4,0.34);
  }

  /* 徽标：改用柔和紫粉渐变，并按主题切换文字色 */
  .badge, .hot .flag {
    background: var(--gradient-badge);
    color: var(--badge-text);
    box-shadow: 0 2px 10px rgba(124,58,237,0.16);
  }
  .date-chip { box-shadow: 0 4px 14px rgba(124,58,237,0.20); }

  /* 焦点 / 热点区块：去掉红紫撞色，统一为低透明度紫色纸 */
  .focus { background: var(--hl-bg); border-color: var(--border-accent); }
  .hot { background: var(--hot-bg); border-color: var(--hot-border); }
  .focus h2, .hot .sub, .plat-name { color: var(--accent-3); }
  .focus .countdown, .risk-item h4 { color: var(--accent-4); }
  .risk-item { border-left-color: var(--accent-4); }
  .model-card.top { border-color: var(--gold-border); background: linear-gradient(160deg, var(--soft-warn-bg), var(--bg-card)); }

  /* 状态色文字：改为主题感知的低饱和色 */
  .warn-line { color: var(--soft-warn); }
  .ok-line { color: var(--soft-ok); }
  .drop-line { color: var(--soft-bad); }
  .done-line { color: var(--soft-mute); }

  /* 胶囊标签 */
  .pill.green { background: var(--soft-ok-bg); color: var(--soft-ok); }
  .pill.orange { background: var(--soft-warn-bg); color: var(--soft-warn); }
  .pill.red { background: var(--soft-bad-bg); color: var(--soft-bad); }
  .combo-card .cost { background: var(--soft-ok-bg); color: var(--soft-ok); }
  .tag.ok { background: var(--soft-ok-bg); color: var(--soft-ok); }
  .tag.warn { background: var(--soft-warn-bg); color: var(--soft-warn); }
  .tag.bad { background: var(--soft-bad-bg); color: var(--soft-bad); }

  /* 表格行状态：用淡底 + 左侧细色条，不再整行压深色 */
  .tbl-wrap tbody tr.new-row { background: var(--hl-bg); }
  .tbl-wrap tbody tr.urgent-row { background: var(--soft-bad-bg); }
  .tbl-wrap tbody tr.urgent-row td:first-child { box-shadow: inset 3px 0 0 var(--soft-bad); }
  .tbl-wrap tbody tr.done-row { opacity: 0.58; }

  /* 名次徽章 */
  .rank-other { background: var(--rank-other-bg); }

  /* 内联 code：降低存在感，只做轻声标注 */
  .hot p code, .focus p code, .section p code, .tbl-wrap code { background: var(--hl-bg); color: var(--accent-3); }
""" + SOFT_END + "\n"


def apply_soft_palette(html):
    """Insert (or refresh) the soft-palette override block before </style>."""
    if SOFT_BEGIN in html and SOFT_END in html:
        new, n = re.subn(re.escape(SOFT_BEGIN) + r".*?" + re.escape(SOFT_END),
                         lambda m: SOFT_CSS.rstrip("\n"), html, count=1, flags=re.S)
        return new, ("soft palette refreshed" if n else "soft palette kept")
    if "</style>" not in html:
        return html, "no </style> found, palette skipped"
    return html.replace("</style>", SOFT_CSS + "</style>", 1), "soft palette injected"


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

    # 4) Soft palette override (idempotent, marker based).
    html, note = apply_soft_palette(html)
    if note not in ("soft palette kept",):
        changed.append(note)

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
