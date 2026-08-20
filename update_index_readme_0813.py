#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update index.html (CTA + new history entry + footer date) and README.md
(今日摘要 date + summary body + file list row) for 2026-08-13."""
import os, re

base = os.path.dirname(os.path.abspath(__file__))

# ===================== index.html =====================
idx = os.path.join(base, "index.html")
with open(idx, encoding="utf-8") as f:
    ih = f.read()

# 1) CTA button -> 8/13
ih = ih.replace(
    '<a class="cta" href="daily-free-llm-2026-08-12.html">📅 查看最新日报</a>',
    '<a class="cta" href="daily-free-llm-2026-08-13.html">📅 查看最新日报</a>',
    1,
)

# 2) Prepend new report-item for 8/13 before the 8/12 item
NEW_ITEM = '''        <a class="report-item" href="daily-free-llm-2026-08-13.html">
          <div class="report-date">
            <div class="day">13</div>
            <div class="month">2026.08</div>
          </div>
          <div class="report-info">
            <h3>🔥 阿里千问 Qwen3.8-2.4T-A95B 开源权重正式落地（8/12 深夜上线 HF + ModelScope，千问首次开放 Max 级旗舰权重；自定义 Qwen3.8-Max License 非 Apache 2.0，大规模商用需授权；文本-only + 强制思考；2.4T/95B、262K→1M 上下文；27B 仍未放出）· DeepSeek V4 Pro 正式版（DeepSeek-V4-Pro-0813）8/13 凌晨上线 API，Agent 能力大增（Responses API + Codex），定价 3/6 元每百万、较 Flash 明显涨价（8/6 预告落地）· 免费先进榜稳定（Kimi K3 98 蝉联第一）</h3>
            <p>🔥 今日主线一（开源落地）：8/12 深夜阿里千问正式开放 Qwen3.8-2.4T-A95B 权重，上线 HuggingFace 与 ModelScope——千问首次开放 Max 级旗舰权重（2.4T 总参 / 95B 激活 / 512 专家 MoE）。开源版文本-only + 强制思考 + 262K→1M 上下文，走自定义 Qwen3.8-Max License（非 Apache 2.0）：>1 亿 MAU 或月营收 >2000 万美元需 UI 标注、MaaS/>5000 万美元 TTM 需授权、内部使用豁免；Reuters 称阿里将对大型商业用户设额外收费——「开放权重」≠「可免费商用」。Unsloth 量化压至 397GB（需 ≥410GB 内存+显存本地跑），27B 仍未放出。</p>
            <p>💰 今日主线二（涨价落地）：8/13 凌晨 DeepSeek V4 Pro 从预览转正（DeepSeek-V4-Pro-0813），支持 Responses API 与 Codex，Terminal-Bench 2.1 达 87.9 逼近 Fable 5 的 88.0；定价 3/6 元每百万（缓存命中 0.025），较 V4-Flash（1/2 元）贵约 3 倍——8/6 预告的涨价正式落地，免费入口仍是 V4-Flash。免费先进榜：Kimi K3（98·Ollama）第一、GLM-5.2（94·NIM）第二、Gemini 3.6 Flash（91）第三；freellm.net 431+ 免费模型 / 30 家供应商。</p>
          </div>
          <div class="report-arrow">→</div>
        </a>
'''
anchor = '<a class="report-item" href="daily-free-llm-2026-08-12.html">'
assert anchor in ih, "8/12 report-item anchor not found in index.html"
ih = ih.replace(anchor, NEW_ITEM + anchor, 1)

# 3) Footer data-source date 8/12 -> 8/13
ih = ih.replace(
    "freellm.net 实时实测目录（378+ 免费大模型、30 家供应商、8/12 刷新）",
    "freellm.net 实时实测目录（431+ 免费大模型、30 家供应商、251 款经实时 API 验证、8/13 更新）",
    1,
)

with open(idx, "w", encoding="utf-8") as f:
    f.write(ih)
print("index.html updated. CTA->8/13:", "daily-free-llm-2026-08-13.html" in ih,
      "| new item present:", "2026-08-13.html" in ih,
      "| footer date:", "8/13 更新" in ih)

# ===================== README.md =====================
rm = os.path.join(base, "README.md")
with open(rm, encoding="utf-8") as f:
    rh = f.read()

# 1) Header date
rh = rh.replace("## 📰 今日摘要（2026-08-12）", "## 📰 今日摘要（2026-08-13）", 1)

# 2) Replace summary body up to "## 内容覆盖"
NEW_SUMMARY = '''## 📰 今日摘要（2026-08-13）

🔥 **Qwen3.8-2.4T-A95B 开源权重正式落地（8/12 深夜上线 HF + ModelScope）——千问首次开放 Max 级旗舰权重**：2.4T 总参 / 95B 激活 / 512 专家 MoE / 262K→1M 上下文；开源版文本-only + 强制思考，走自定义 Qwen3.8-Max License（非 Apache 2.0）。⚠️ 商用前必读许可证：>1 亿 MAU 或月营收 >2000 万美元需 UI 标注、MaaS/>5000 万美元 TTM 需授权、内部使用豁免；Reuters 称阿里将对大型商业用户设额外收费——「开放权重」≠「可免费商用」。全精度 4.9TB、Unsloth 量化压至 397GB（需 ≥410GB 内存+显存本地跑）；27B 仍未放出。API 仍付费（$2/$6）、暂无 :free 层。

💰 **DeepSeek V4 Pro 正式版（DeepSeek-V4-Pro-0813）8/13 凌晨上线 API——Agent 能力大增但明显涨价**：支持 Responses API 与 Codex 接入，Terminal-Bench 2.1 87.9 逼近 Fable 5 的 88.0，CyberGym / AutomationBench 反超；定价 3/6 元每百万（缓存命中 0.025），较 V4-Flash（1/2 元）贵约 3 倍——8/6 预告的涨价正式落地。⚠️ 免费入口仍是 V4-Flash，V4-Pro 已非「免费」定位。

💎 **高分免费模型 Top 3**：Kimi K3（98 分 / Ollama Cloud 免费层 + 开源，蝉联第一）、GLM-5.2（94 分 / NVIDIA NIM 永久免费 + 开源，第二）、Gemini 3.6 Flash（91 分 / AI Studio 免费层，第三）；场外：腾讯 Hy3（90 分 / 限免至 8/31，OpenRouter 已转 Paid）、DeepSeek V4-Flash（91·OpenRouter 免费层）、智谱 GLM-5.3（万亿参数「发布在即」、API 未开放）。

🎁 **大额每日刷新（10 家量大平台）**：国家超算互联网 SCNet、移动云 MoMA、Ollama Cloud、NVIDIA NIM（141 模型、77 款永久免费端点）、阿里云百炼、美团 LongCat、火山引擎、硅基流动 / 魔搭、腾讯云 TokenHub、OpenRouter（200 次/天账户级、充 $10 升 1000）。⚠️ 容量提醒：DeepSeek V4-Flash 官方 API 并发上限 2500、易 503，生产用多入口分流；DeepSeek 8/6 起大幅涨价（高峰翻倍）。

🆕 **今日新增关注**：Qwen3.8-2.4T-A95B 开源权重正式落地（千问首次开放 Max 级旗舰权重）、DeepSeek V4 Pro 正式版（0813）上线 API 并涨价。✅ 已开源：Kimi K3、GLM-5.2、MiniMax H3、Ling-3.0-flash、Muse Glimmer、Nemotron 3.5 Lightning、Qwen3.8-2.4T-A95B。⏳ 即将开源：Qwen3.8-27B（在路上）。⚠️ 风险提醒：DeepSeek V4-Pro 涨价、Hy3 限免仅剩 18 天（8/31 截止）、Qwen3.8-Max License 非 Apache 2.0 大规模商用需授权、本地开源≠API 免费、Ollama 额度未公开、GLM-5.3 未开放、OpenRouter 仅 200 次/天、腾讯混元旧平台 9/30 停服、GCP 16 个端点 10/21 退役。

'''
rh = re.sub(r'## 📰 今日摘要（2026-08-13）.*?\n\n## 内容覆盖',
            NEW_SUMMARY + '\n## 内容覆盖', rh, count=1, flags=re.S)

# 3) Prepend file-list row for 8/13
FILE_ROW = "| 2026-08-13 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-08-13.html) | [HTML](daily-free-llm-2026-08-13.html) |\n"
rh = rh.replace("| 2026-08-12 |", FILE_ROW + "| 2026-08-12 |", 1)

with open(rm, "w", encoding="utf-8") as f:
    f.write(rh)
print("README.md updated. summary date 8/13:", "今日摘要（2026-08-13）" in rh,
      "| file row present:", "daily-free-llm-2026-08-13.html" in rh)
