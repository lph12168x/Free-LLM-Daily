#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update index.html (CTA + new 0819 history entry + footer date) and README.md
(0819 summary + file row). Also backfills nothing else; 0818 entries already exist."""
import os, re

base = os.path.dirname(os.path.abspath(__file__))

# ===================== index.html =====================
idx = os.path.join(base, "index.html")
with open(idx, encoding="utf-8") as f:
    ih = f.read()

# 1) CTA button -> 8/19
ih = ih.replace(
    '<a class="cta" href="daily-free-llm-2026-08-18.html">📅 查看最新日报</a>',
    '<a class="cta" href="daily-free-llm-2026-08-19.html">📅 查看最新日报</a>',
    1,
)

# 2) Prepend new report-item for 8/19 before the 8/18 item
NEW_ITEM = '''        <a class="report-item" href="daily-free-llm-2026-08-19.html">
          <div class="report-date">
            <div class="day">19</div>
            <div class="month">2026.08</div>
          </div>
          <div class="report-info">
            <h3>🔥 智谱 GLM-5.3 API 8/19 凌晨上线（743B·AA Index 60 并列开源第一·与 Kimi K3 并列·付费 API 但权重 8/28 开源进 NIM 免费层）· 中国开源 AI 成美国大模型「底座」（Qwen3.8-27B 登顶 HF 趋势榜、两天下载破百万、衍生 15 万+）· DeepSeek Harness 三天 13 万 Star · freellm.net 442+ 模型</h3>
            <p>🔥 今日头号：智谱 8/19 凌晨上线 GLM-5.3 API——743B、沿用 GLM-5.2 底座经后训练缩放，AA Intelligence Index 60 分，与 Kimi K3 并列开源第一、与 Claude Fable 5 / GPT-5.6 Sol 同档；Terminal-Bench 3.0 28.3、DeepSWE v1.1 66.9、CyberGym 84.5%；定价同 GLM-5.2（腾讯云 输入8/输出28/缓存2 元每百万），权重下周五（8/28）开源。⚠️ 当下免费入口仍是 GLM-5.2（NVIDIA NIM 94 分、1M 上下文、40 RPM 永久免费）。同期中国开源 AI 成美国大模型「底座」：Qwen3.8-27B 登顶 HuggingFace 趋势榜、开源两天下载破 100 万次、衍生模型超 15 万居全球第一；DeepSeek Harness 三天 GitHub Star 超 13 万。freellm.net 目录扩至 442+ 模型 / 31 供应商；kimi-k3（98）蝉联免费榜第一。</p>
          </div>
          <div class="report-arrow">→</div>
        </a>
'''
anchor = '<a class="report-item" href="daily-free-llm-2026-08-18.html">'
assert anchor in ih, "8/18 report-item anchor not found in index.html"
ih = ih.replace(anchor, NEW_ITEM + anchor, 1)

# 3) Footer data-source date/count 8/15 -> 8/19, 424+ -> 442+
ih = ih.replace(
    "freellm.net 实时实测目录（424+ 免费大模型、30 家供应商、316 款在线、API Key 索引更新至 8/15）",
    "freellm.net 实时实测目录（442+ 免费大模型、31 家供应商、329 款在线、API Key 索引更新至 8/19）",
    1,
)

with open(idx, "w", encoding="utf-8") as f:
    f.write(ih)
print("index.html updated. CTA->8/19:", "daily-free-llm-2026-08-19.html" in ih,
      "| new item present:", "2026-08-19.html" in ih,
      "| footer date:", "8/19" in ih)

# ===================== README.md =====================
rm = os.path.join(base, "README.md")
with open(rm, encoding="utf-8") as f:
    rh = f.read()

# 1) Prepend 0819 summary before 0818 summary header
NEW_SUMMARY = '''## 📰 今日摘要（2026-08-19）

🔥 **智谱 GLM-5.3 API 8/19 凌晨上线——743B、AA Index 60 并列开源第一，付费 API 但权重 8/28 开源进 NIM 免费层**：GLM-5.3 沿用 GLM-5.2 底座、全部提升来自后训练缩放，在 Artificial Analysis Intelligence Index 取得 60 分，与 Kimi K3 并列开源模型第一、与 Claude Fable 5 / GPT-5.6 Sol 同档。Terminal-Bench 3.0 由 4.6 升至 28.3、DeepSWE v1.1 66.9、Agents' Last Exam 28.5、白盒漏洞发现 CyberGym 84.5%（高于 Mythos 5 的 83.8%）。API 定价与 GLM-5.2 持平（腾讯云 输入 8 / 输出 28 / 缓存命中 2 元每百万），权重计划下周五（8/28）开源——届时进 NVIDIA NIM 永久免费层。⚠️ 当下免费入口仍是 GLM-5.2（NVIDIA NIM 94 分、1M 上下文、40 RPM 无日限额、永久免费）。

🌏 **中国开源 AI 成美国大模型「底座」：Qwen3.8-27B 登顶 HF 趋势榜、两天下载破百万、衍生 15 万+**：Hugging Face《开源模型现状：2026 夏季观察》显示中国实验室月度最大开源模型规模（7540 亿–2.78 万亿）持续领先美国，部分美国千亿级模型以中国模型为底座。Qwen3.8-27B（Apache 2.0、24GB 显卡可跑）开源两天下载破 100 万次、衍生模型超 15 万个居全球第一。DeepSeek Harness（DSH）8/13 开放预览，三天 GitHub Star 超 13 万。

💎 **高分免费模型 Top 3**：kimi-k3（98 分 / Ollama Cloud 免费层 + 开源，登顶第一，但 session/weekly 限额）、GLM-5.2（94 分 / NVIDIA NIM 永久免费 + 开源，量大能用最稳冠军）、Gemini 3.6 Flash（91 分 / AI Studio 免费层，第三）；场外：DeepSeek V4 Flash（90·多入口免费）、MiniMax M3（89·多模态多入口）、Nemotron 3 Ultra（85）、Ling-3.0-flash（87）。⚠️ Tencent Hy3（90）经 WorkBuddy/CodeBuddy 限免至 8/31（剩 13 天）仍可用、OpenRouter 已转 Paid；GLM-5.3 为付费 API、权重 8/28 开源后才进免费层。

⌨️ **新入口 / 免费 API 提供商（不止 FreeLLM 类网站）**：OpenCode Zen（DeepSeek V4 Flash Free、MiniMax M3 Free、Nemotron 3 Ultra Free、Big Pickle、MiMo-V2.5 Free 等限时免费，Base URL https://opencode.ai/zen/v1）；OpenRouter（Nemotron 3 Ultra、Gemma 4、gpt-oss、Ling-3.0-flash 等 25+，50 次/天、充 $10 升 1000）；Nous Portal（Step-3.7-Flash / Nemotron-3-Ultra / Owl-Alpha 3 款免费，OAuth device-code 登录）；火山引擎方舟（每日 200 万 Token 免费含 V4 Pro）；NVIDIA NIM（77 款永久免费端点、40 RPM 无日限额）。

🎁 **大额每日刷新（10 家量大平台）**：火山引擎方舟（200 万/天、含 V4 Pro）、阿里云百炼（70+ 模型每款 100 万 Token）、NVIDIA NIM（125 模型、77 款永久免费、40 RPM 无日限额）、OpenCode Zen（多款 -Free 限时免费）、美团 LongCat（500 万/天起）、Groq（14400 次/天）、硅基流动（新用户 2000 万）、腾讯云 TokenHub（每模型 100 万）、OpenRouter（25+ 免费、50 次/天、充 $10 升 1000）、Nous Portal（3 款新免费）。

🆕 **今日新增关注**：智谱 GLM-5.3 API 上线（AA Index 60 并列开源第一，付费但权重 8/28 开源）、中国开源成美国「底座」（Qwen3.8-27B 登顶 HF 趋势榜）。✅ 已开源：Kimi K3、GLM-5.2、MiniMax M3、Ling-3.0-flash、Nemotron 3 Ultra、Qwen3.8-27B、DeepSeek V4 系列。⏳ 即将开源：GLM-5.3 权重（8/28）。⚠️ 风险提醒：DeepSeek 官方 API 8/17 峰谷涨价（免费党转火山/NIM/Zen/Nous）、GLM-5.3 当前付费（等 8/28 权重）、Qwen3.8-Max License 非 Apache 2.0 大规模商用需授权、OpenCode Zen 限时免费+数据用于训练、腾讯混元旧平台 9/30 停服、GCP 16 个端点 10/21 退役、OpenRouter 免费层 50 次/天账户级、Hy3 限免至 8/31（剩 13 天）。

'''
rh = rh.replace("## 📰 今日摘要（2026-08-18）", NEW_SUMMARY + "## 📰 今日摘要（2026-08-18）", 1)

# 2) Prepend file-list row for 8/19
FILE_ROW = "| 2026-08-19 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-08-19.html) | [HTML](daily-free-llm-2026-08-19.html) |\n"
rh = rh.replace("| 2026-08-18 |", FILE_ROW + "| 2026-08-18 |", 1)

with open(rm, "w", encoding="utf-8") as f:
    f.write(rh)
print("README.md updated. summary 8/19:", "今日摘要（2026-08-19）" in rh,
      "| file row present:", "daily-free-llm-2026-08-19.html" in rh)
