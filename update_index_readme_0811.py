#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update index.html (CTA + new history entry + footer date) and README.md
(今日摘要 date + summary body + file list row) for 2026-08-11."""
import os, re

base = os.path.dirname(os.path.abspath(__file__))

# ===================== index.html =====================
idx = os.path.join(base, "index.html")
with open(idx, encoding="utf-8") as f:
    ih = f.read()

# 1) CTA button -> 8/11
ih = ih.replace(
    '<a class="cta" href="daily-free-llm-2026-08-10.html">📅 查看最新日报</a>',
    '<a class="cta" href="daily-free-llm-2026-08-11.html">📅 查看最新日报</a>',
    1,
)

# 2) Prepend new report-item for 8/11 before the 8/10 item
NEW_ITEM = '''        <a class="report-item" href="daily-free-llm-2026-08-11.html">
          <div class="report-date">
            <div class="day">11</div>
            <div class="month">2026.08</div>
          </div>
          <div class="report-info">
            <h3>🔥 阿里 Qwen3.8-Max（2.4T）与 Qwen3.8-27B 开源权重进入「本周（8/10 起）落地窗口」· 下载前必读四件事（许可证/硬件/量化/自测基准）· OpenAI 8/6 对 GPT-5.6 Luna 降价 80% 触发开源竞赛 · ChatGPT 免费档本周取消文本条数限制 · 免费先进模型格局稳定（Kimi K3 98 蝉联第一）</h3>
            <p>🔥 今日主线：阿里 Qwen3.8-Max（2.4T / 约 95B 激活 / 1M 上下文 / 原生多模态）与 Qwen3.8-27B 的开源权重已确认「本周（8/10 起当周）」通过 HuggingFace + ModelScope 公开——千问 Max 级旗舰首次开源，全球开发者蹲守等上传。战略信号：OpenAI 8/6 对 GPT-5.6 Luna 降价 80%，阿里用开源权重抢开发者生态；ChatGPT 免费档本周取消文本条数限制。下载前必读四件事：① 先读 LICENSE（或走 Tongyi Qianwen Licence 含 1 亿 MAU 阈值）；② Max 需约 20 张 H100；③ 你能跑的是 27B（4-bit 单卡 RTX 4090）；④ 社区量化晚 1–2 周。免费先进模型格局稳定：Kimi K3（Ollama·98）蝉联第一、GLM-5.2（NIM·95）第二、Gemini 3.6 Flash（91）第三；freellm.net 424+ 免费模型 / 30 家供应商。</p>
          </div>
          <div class="report-arrow">→</div>
        </a>
'''
anchor = '<a class="report-item" href="daily-free-llm-2026-08-10.html">'
assert anchor in ih, "8/10 report-item anchor not found in index.html"
ih = ih.replace(anchor, NEW_ITEM + anchor, 1)

# 3) Footer data-source date 8/7 -> 8/11
ih = ih.replace("、246 款经实时 API 验证、8/7 刷新）", "、244 款经实时 API 验证、8/11 更新）", 1)

with open(idx, "w", encoding="utf-8") as f:
    f.write(ih)
print("index.html updated. CTA->8/11:", "daily-free-llm-2026-08-11.html" in ih,
      "| new item present:", "2026-08-11.html" in ih)

# ===================== README.md =====================
rm = os.path.join(base, "README.md")
with open(rm, encoding="utf-8") as f:
    rh = f.read()

# 1) Header date
rh = rh.replace("## 📰 今日摘要（2026-08-10）", "## 📰 今日摘要（2026-08-11）", 1)

# 2) Replace summary body up to "## 内容覆盖"
NEW_SUMMARY = '''## 📰 今日摘要（2026-08-11）

🔥 **阿里 Qwen3.8-Max（2.4T）与 Qwen3.8-27B 开源权重进入「本周（8/10 起）落地窗口」——千问 Max 级旗舰首次开源**：Qwen3.8-Max（2.4T / 约 95B 激活 / 1M 上下文 / 原生多模态）与 27B 同步开源，全球开发者蹲守 HuggingFace + ModelScope 等上传。⚠️ 下载前必读四件事：① 先读 LICENSE（或走 Tongyi Qianwen Licence，商用需 1 亿 MAU 阈值）；② Max 需约 20 张 H100，个人部署不了；③ 你能跑的是 27B（4-bit 单卡 RTX 4090）；④ 社区量化晚 1–2 周。当前 API 付费（$2/$6）、暂无 :free 层；所有基准来自阿里 8/3 自测表，无第三方独立评测。

🌍 **OpenAI 8/6 对 GPT-5.6 Luna 降价 80% + ChatGPT 免费档本周取消文本条数限制**：闭源免费侧也在卷，开源与闭源免费边界模糊；免费可用大模型不只有 API 免费层，闭源聊天产品（ChatGPT/Claude/Gemini/Kimi 免费档）也是「当天可免费使用」的先进模型入口。⚠️ 闭源免费档普遍用对话改进产品，敏感数据勿走免费层。

💎 **高分免费模型 Top 3**：Kimi K3（98 分 / Ollama Cloud 免费层 + 开源，蝉联第一）、GLM-5.2（95 分 / NVIDIA NIM 永久免费 + 开源，第二）、Gemini 3.6 Flash（91 分 / AI Studio 免费层，第三）；场外：腾讯 Hy3（90 分 / 限免至 8/31，OpenRouter 已转 Paid）、智谱 GLM-5.3（万亿参数「发布在即」、API 未开放）。

🎁 **大额每日刷新（10 家量大平台）**：国家超算互联网 SCNet（最高 6000 万 / 90 天）、移动云 MoMA（2500 万 / 30 天）、Ollama Cloud、NVIDIA NIM（141 模型、77 款永久免费端点）、阿里云百炼（每模型 100 万）、美团 LongCat（500 万/天起）、火山引擎（200 万/天）、硅基流动 / 魔搭、腾讯云 TokenHub（每模型 100 万）、OpenRouter（50 次/天、充 $10 升 1000）。⚠️ **容量提醒**：DeepSeek V4-Flash 官方 API 并发上限仅 2500、易 503，生产请用多入口分流；DeepSeek 8/6 宣布大幅涨价（高峰 9:00–12:00、14:00–18:00 翻倍）。

🆕 **今日新增关注**：Qwen3.8-Max / Qwen3.8-27B 开源权重进入「本周落地窗口」、OpenAI 免费侧剧变（Luna 降价 80% + ChatGPT 取消文本限）。✅ **已开源观察**：Kimi K3、GLM-5.2、MiniMax H3、蚂蚁百灵 Ling-3.0-flash 权重均已开源；⏳ **即将开源**：Qwen3.8-Max（8/10 当周）。⚠️ **风险提醒**：DeepSeek 大涨价格局、Hy3 限免仅剩 20 天（8/31 截止）、Qwen3.8-Max/H3/Ling 的 API 当前付费或暂无 :free 层且许可证待核实、Ollama 免费额度数值未公开、GLM-5.3 官宣但 API 未开放别赌生产、OpenRouter 仅 50 次/天、腾讯混元旧平台 9/30 停服、GCP 16 个端点 10/21 退役。

'''
rh = re.sub(r'## 📰 今日摘要（2026-08-11）.*?\n\n## 内容覆盖',
            NEW_SUMMARY + '\n## 内容覆盖', rh, count=1, flags=re.S)

# 3) Prepend file-list row for 8/11
FILE_ROW = "| 2026-08-11 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-08-11.html) | [HTML](daily-free-llm-2026-08-11.html) |\n"
rh = rh.replace("| 2026-08-10 |", FILE_ROW + "| 2026-08-10 |", 1)

with open(rm, "w", encoding="utf-8") as f:
    f.write(rh)
print("README.md updated. summary date 8/11:", "今日摘要（2026-08-11）" in rh,
      "| file row present:", "daily-free-llm-2026-08-11.html" in rh)
