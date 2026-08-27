#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Assemble today's (2026-08-24) Free LLM Daily report from part files,
# reusing verified CSS/JS from the latest existing report, then sync index.html.
import os, re

base = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(base, "daily-free-llm-2026-08-21.html")
out = os.path.join(base, "daily-free-llm-2026-08-24.html")

with open(src, encoding="utf-8") as fh:
    src_html = fh.read()

m_style = re.search(r"<style>(.*?)</style>", src_html, re.S)
style_css = m_style.group(1)
m_script = re.search(r"<script>(.*?)</script>", src_html, re.S)
script_js = m_script.group(1)

# Body parts
parts = []
for i in range(1, 5):
    with open(os.path.join(base, f"part{i}.txt"), encoding="utf-8") as fh:
        parts.append(fh.read())
body = "\n".join(parts)

TITLE = "免费大模型日报 · 2026-08-24 · Free LLM Daily"
DESC = ("2026年8月24日免费大模型日报：聚焦量大能用的先进模型。🔥 今日头号新发现——CommandCode 提供真免费模型（Laguna S 2.1 Free / Ling 3.0 Flash 免费 / Ox Alpha 隐身免费，无需信用卡，OpenAI 兼容）；freellm.net 目录刷新至 450+ 模型 / 258 活体验证（8/22-23）；Gemini 3.7 Flash 复测升至 86（纠正早期 45 误判）；新增常驻免费层 Cloudflare Workers AI（1 万 Neurons/天）+ Vercel AI Gateway（月额度）；GLM-5.3 权重 8/28 开源倒计时（剩 4 天）；Qwen3.8-27B 已开源（freellm 84）。免费先进榜：kimi-k3（98）蝉联第一，GLM-5.2（NIM 93-94）量大冠军。")

html = f"""<!DOCTYPE html>
<html lang="zh-CN" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{TITLE}</title>
<meta name="description" content="{DESC}">
<style>{style_css}</style>
</head>
<body>

<button class="theme-toggle" onclick="toggleTheme()" title="切换亮色/暗色主题" aria-label="主题切换"><span id="theme-icon">☀️</span></button>
<button class="scroll-top" id="scrollTop" onclick="window.scrollTo({{top:0,behavior:'smooth'}})" aria-label="回到顶部">↑</button>

<div class="container">
{body}
</div>

<script>{script_js}</script>
</body>
</html>
"""

with open(out, "w", encoding="utf-8") as fh:
    fh.write(html)
print("Wrote", out, "size", len(html))

# ---------------------------------------------------------------------------
# Sync index.html
# ---------------------------------------------------------------------------
idx_path = os.path.join(base, "index.html")
with open(idx_path, encoding="utf-8") as fh:
    idx = fh.read()

# 1) Latest report CTA
idx = idx.replace(
    'href="daily-free-llm-2026-08-21.html">📅 查看最新日报',
    'href="daily-free-llm-2026-08-24.html">📅 查看最新日报'
)

# 2) Stats count
idx = idx.replace('<div class="stat-num">441+</div>', '<div class="stat-num">450+</div>')

# 3) Prepend a new report-item to the history list
new_item = '''<a class="report-item" href="daily-free-llm-2026-08-24.html">
          <div class="report-date">
            <div class="day">24</div>
            <div class="month">2026.08</div>
          </div>
          <div class="report-info">
            <h3>🔥 今日新发现：CommandCode 真免费模型（Laguna S 2.1 Free / Ling 3.0 Flash 免费 / Ox Alpha 隐身免费，无需信用卡）· freellm.net 目录刷新至 450+ 模型 / 258 活体验证（8/22-23）· Gemini 3.7 Flash 复测升至 86（纠正早期 45 误判）· 新增常驻免费层 Cloudflare Workers AI（1 万 Neurons/天）+ Vercel AI Gateway（月额度）· GLM-5.3 权重 8/28 开源倒计时（剩 4 天）· Qwen3.8-27B 已开源（freellm 84）</h3>
            <p>🔥 头号新发现：CommandCode（commandcode.ai）除 $1 Go / $10 GOAT（70 额度）订阅外，还提供三款<b>真免费</b>模型——Laguna S 2.1 Free（256K，容量内免费）、Ling 3.0 Flash（免费）、Ox Alpha（隐身预览免费），OpenAI 兼容、无需信用卡，是编码 Agent 之外又一个免费 API 入口。💎 freellm.net 目录刷新至 2026-8-22/23——450+ 免费模型 / 31 家 / 258 活体验证；⚠️ 关键纠偏：Gemini 3.7 Flash 早期 45 分为评测不充分，复测已升至 86，可正常当主力。🌐 新增常驻免费层：Cloudflare Workers AI（1 万 Neurons/天、gpt-oss 系列、免卡）、Vercel AI Gateway（每月刷新额度）。📊 免费榜：kimi-k3（98）蝉联第一，GLM-5.2（NIM 93-94）量大冠军；Kimi K3 已上 NVIDIA NIM（90·1M）；DeepSeek V4 Pro 0813 / Qwen3.8-27B 经 ModelScope 免费（84）。⏳ GLM-5.3 权重 8/28 才开源（剩 4 天），当下付费；Hy3 限免 8/31 截止（剩 7 天）。</p>
          </div>
          <div class="report-arrow">→</div>
        </a>
'''

idx = idx.replace('<div class="report-list">\n', '<div class="report-list">\n' + new_item, 1)

with open(idx_path, "w", encoding="utf-8") as fh:
    fh.write(idx)
print("Updated index.html (CTA + stats + new report item)")

# Cleanup part files
for i in range(1, 5):
    p = os.path.join(base, f"part{i}.txt")
    if os.path.exists(p):
        os.remove(p)
print("Cleaned up part files")
