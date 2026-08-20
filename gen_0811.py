#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate daily-free-llm-2026-08-11.html by adapting the 8/10 template.
Stable sections (Top10, platforms, combos, risks, CSS) are kept verbatim.
Only date-specific hero/focus/hot-cards/footer are refreshed.
"""
import os, re

base = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(base, "daily-free-llm-2026-08-10.html")
dst = os.path.join(base, "daily-free-llm-2026-08-11.html")

with open(src, encoding="utf-8") as f:
    html = f.read()

# ---- 1. Title ----
html = html.replace(
    "<title>免费大模型日报 · 2026-08-10 · Free LLM Daily</title>",
    "<title>免费大模型日报 · 2026-08-11 · Free LLM Daily</title>",
    1,
)

# ---- 2. Meta description ----
NEW_META = ('<meta name="description" content="2026年8月11日免费大模型日报：聚焦量大能用的先进模型。'
    "🔥 本期主线——阿里 Qwen3.8-Max（2.4T）与 Qwen3.8-27B 开源权重进入「本周（8/10 起）落地窗口」，全球开发者蹲守 HuggingFace + ModelScope——千问 Max 级旗舰首次开源；下载前必读四件事：许可证未定（或含地域限制）、Max 需约 20 张 H100、27B 才是个人机器跑得动的、社区量化要等 1–2 周；"
    "OpenAI 8/6 对 GPT-5.6 Luna 降价 80% 是本轮开源竞赛的导火索，ChatGPT 免费档本周取消文本条数限制；免费先进模型格局稳定（Kimi K3 98 蝉联第一）。\">")
html = re.sub(r'<meta name="description" content="[^"]*" ?>', NEW_META, html, count=1)

# ---- 3. Date chip ----
html = html.replace(
    '<div class="date-chip">📅 2026 年 8 月 10 日 · 周一</div>',
    '<div class="date-chip">📅 2026 年 8 月 11 日 · 周二</div>',
    1,
)

# ---- 4. Tagline ----
NEW_TAGLINE = ('<p class="tagline">聚焦「量大能用的先进模型」· 覆盖 30+ 国内外平台 · 本期主线：'
    '<b>阿里 Qwen3.8-Max（2.4T）与 Qwen3.8-27B 开源权重进入「本周（8/10 起）落地窗口」，全球开发者蹲守 HuggingFace + ModelScope——千问 Max 级旗舰首次开源</b>；'
    '<b>下载前必读四件事</b>：许可证未定（或含地域限制）、Max 需约 20 张 H100、27B 才是个人机器跑得动的、社区量化要等 1–2 周；'
    '<b>OpenAI 8/6 对 GPT-5.6 Luna 降价 80% 是导火索</b>，ChatGPT 免费档本周取消文本条数限制；免费先进模型格局稳定（Kimi K3 98 蝉联第一）。</p>')
html = re.sub(r'<p class="tagline">.*?</p>', NEW_TAGLINE, html, count=1, flags=re.S)

# ---- 5. Focus banner ----
NEW_FOCUS = '''  <div class="focus">
    <h2>📌 本期焦点：Qwen3.8 开源权重进入「本周落地窗口」（8/10 起当周）· 下载前必读四件事（许可证 / 硬件 / 量化时间表 / 自测基准）· OpenAI 8/6 对 GPT-5.6 Luna 降价 80% 是导火索 · ChatGPT 免费档本周取消文本条数限制 · 免费先进模型格局稳定（Kimi K3 98 蝉联第一）</h2>
    <p>
      <b>今日主线（对「量大能用」最有引爆力）</b>：阿里 Qwen3.8-Max（2.4T / 约 95B 激活 / 1M 上下文 / 原生多模态）与 Qwen3.8-27B 的开源权重，已确认<b>「本周（8/10 起当周）」通过 HuggingFace 与 ModelScope 公开</b>——这是千问 Max 级旗舰首次开源，全球开发者正蹲守 org 页面等上传。<br><br>
      <b>为什么是现在（战略信号）</b>：OpenAI 8/6 对 GPT-5.6 Luna <b>降价 80%</b>，阿里判断「靠定价在闭源世界竞争不可持续」，<b>转而用开源权重抢开发者生态</b>——这是本轮国产开源军备竞赛最直接、也最明确的导火索。<br><br>
      <b>下载前必读四件事（避免踩坑）</b>：① <span class="hl">先读 LICENSE</span>——Qwen 历史多为 Apache 2.0，但 Qwen3.8 可能走 Tongyi Qianwen Licence（商用需 1 亿 MAU 阈值触发商务洽谈），在仓库里亲眼看 LICENSE 之前别集成进产品；② <span class="hl">Max 是数据中心玩法</span>——2.4T 全精度约 1.63TB、需约 20 张 H100，个人 / 小团队这周根本部署不了；③ <span class="hl">你能跑的是 27B</span>——4-bit 14–16GB（单卡 RTX 4090 可）、FP8 约 27GB（单卡 L40S）；④ <span class="hl">社区量化要等</span>——GGUF / AWQ 通常晚 1–2 周，vLLM / SGLang 首日支持，Ollama 要等 GGUF 就绪。<br><br>
      <b>冷静三点</b>：① 所有基准（SWE-bench Pro 67.7、OSWorld-Verified 86.1、PaperBench 93.0）均来自<b>阿里 8/3 自测表，尚无第三方独立评测</b>；② 当前 API 仍付费（$2 / $6）、<b>暂无 :free 层</b>；③ 真实工程编程（SWE-bench Pro 67.7）仍落后 Claude Fable 5 的 80.0 超过 12 分。请始终分清「开源红利」与「当下可用免费入口」——<b>当下能立即白嫖的旗舰仍是 K3 / GLM-5.2 / Gemini 3.6 Flash / DeepSeek V4-Flash / MiniMax M3 / Hy3</b>（见下方 Top10）。<br><br>
      倒计时：<span class="countdown">8/31 腾讯 Hy3 限免截止（还有 20 天）</span> · 本周待兑现：Qwen3.8-Max / 27B 权重开源 · 已发生：8/6 OpenAI 降价 / 8/6 DeepSeek 涨价公告 · 近期：智谱 GLM-5.3 万亿参数「发布在即」· 远期：9/30 腾讯混元旧平台停服、10/21 GCP 16 端点退役、12/31 腾讯云 TokenHub 与移动云 MoMA 新人活动结束。
    </p>
  </div>'''
html = re.sub(r'<div class="focus">.*?</div>\n\n  <!-- Hot featured 1', NEW_FOCUS + '\n\n  <!-- Hot featured 1', html, count=1, flags=re.S)

# ---- 6. Hot card 1 + Hot card 2 ----
NEW_HOT1 = '''  <!-- Hot featured 1: Qwen3.8 open weights -->
  <div class="hot">
    <span class="flag">🔥 本周落地窗口 · 阿里 Qwen3.8-Max（2.4T）与 Qwen3.8-27B 开源权重「这周（8/10 起）」上 HuggingFace + ModelScope——千问 Max 级旗舰首次开源</span>
    <h2>2.4 万亿参数 + 1M 上下文 + 原生多模态，阿里把旗舰权重向社区公开；27B 才是个人机器真正跑得动的那一个</h2>
    <div class="sub">阿里 8/3 发布 · 权重「本周（8/10 起当周）开源」· HF + ModelScope · 2.4T / 激活 95B · 1M 上下文 · 原生文本/图像/视频</div>
    <p>
      <b>① 发生了什么</b>：8 月 3 日阿里发布 Qwen3.8-Max，并承诺<b>本周（8/10 起当周）开源完整权重</b>——这是 Qwen-Max 级超大杯首次开源，此前一直仅通过 API 提供。同步开源更轻盈的 <b>Qwen3.8-27B</b>。全球开发者正蹲守 HuggingFace / ModelScope 等上传。<br><br>
      <b>② 为什么是现在（战略信号）</b>：OpenAI 8/6 对 GPT-5.6 Luna <b>降价 80%</b>，阿里判断「靠定价在闭源世界竞争不可持续」，<b>用开源权重抢开发者生态</b>成为本轮国产开源军备竞赛最直接的导火索；SCMP 称 Qwen3.8-Max「仅次于 Claude Fable 5」，对标意味明显。<br><br>
      <b>③ 下载前必读四件事</b>：<span class="hl">① 先读 LICENSE</span>：Qwen 历史多为 Apache 2.0，但 Qwen3.8 可能走 Tongyi Qianwen Licence（商用需 1 亿 MAU 阈值触发商务洽谈），在仓库亲眼看 LICENSE 之前别集成进产品；<span class="hl">② Max 是数据中心玩法</span>：2.4T 全精度约 1.63TB、需约 20 张 H100，个人 / 小团队这周部署不了；<span class="hl">③ 你能跑的是 27B</span>：4-bit 14–16GB（单卡 RTX 4090 可）、FP8 约 27GB（单卡 L40S）；<span class="hl">④ 量化要等</span>：社区 GGUF / AWQ 通常晚 1–2 周，vLLM / SGLang 首日支持，Ollama 要等 GGUF。<br><br>
      <b>④ 冷静三点</b>：所有基准（SWE-bench Pro 67.7、OSWorld-Verified 86.1、PaperBench 93.0）均来自<b>阿里 8/3 自测表，无第三方独立评测</b>；当前 API 仍付费（海外 $2 / $6、国内 12 / 36 元每百万 Token，缓存命中 1.5 元）、<b>暂无 :free 层</b>；真实工程编程（SWE-bench Pro 67.7）仍落后 Claude Fable 5 的 80.0 超过 12 分。策略：本周重点蹲守 27B 权重与最终 LICENSE；当下能立即白嫖的旗舰仍是 GLM-5.2（95 分·NIM 永久免费）。
    </p>
    <div class="hot-grid">
      <div class="hot-item"><div class="k">开源时间</div><div class="v">本周 8/10 起</div></div>
      <div class="hot-item"><div class="k">总参 / 激活</div><div class="v">2.4T / 95B</div></div>
      <div class="hot-item"><div class="k">上下文</div><div class="v">1M Token</div></div>
      <div class="hot-item"><div class="k">本地可跑</div><div class="v">27B 版本</div></div>
      <div class="hot-item"><div class="k">当前 API</div><div class="v">付费 $2/$6</div></div>
      <div class="hot-item"><div class="k">最大风险</div><div class="v">许可证未定</div></div>
    </div>
    <a class="hot-link" href="https://qwen.ai/blog?id=qwen3.8" target="_blank">查看千问官方技术博客 →</a>
  </div>'''

NEW_HOT2 = '''  <!-- Hot featured 2: OpenAI free-side shift -->
  <div class="hot">
    <span class="flag">🌍 今日专题 · OpenAI 8/6 对 GPT-5.6 Luna 降价 80% + ChatGPT 免费档本周取消文本条数限制——闭源免费侧也在「卷」，开源与闭源免费边界正在模糊</span>
    <h2>GPT-5.6 Luna 降价 80%、ChatGPT 免费文本「不限条数」——免费可用的大模型不只有开源 / API 免费层，闭源聊天产品也在放开</h2>
    <div class="sub">OpenAI 8/6 降价 · ChatGPT 免费档 week of 8/10 取消文本条数限制 · GPT-5.6 Luna 成免费档默认模型 · 免费 chatbot 格局生变</div>
    <p>
      <b>① 闭源侧也在卷免费</b>：OpenAI 8/6 对 GPT-5.6 Luna <b>降价 80%</b>，并于 8/6 起把免费 ChatGPT 默认模型切到 Luna；更关键的是，<b>从 8/10 当周起，ChatGPT 免费档取消文本聊天的条数上限</b>（图片 / 文件 / 语音 / 生图仍各自有限额）——这是闭源厂商对开源免费浪潮的直接回应。<br><br>
      <b>② 对「免费可用大模型」榜单的含义</b>：免费阵营不止 API 免费层（K3 / GLM / Gemini / DeepSeek）与开源权重，<b>闭源聊天产品（ChatGPT 免费档 Luna、Claude 免费档 Sonnet 5、Gemini 免费档 3.6 Flash、Kimi 免费档 K3、Copilot 免费档）也是「当天可免费使用」的先进模型入口</b>。本报告 Top10 聚焦 API / 自部署免费先进模型；聊天产品作为日常零成本入口，二者互补。<br><br>
      <b>③ 理性边界</b>：ChatGPT 免费档「不限条数」仅覆盖文本，文件 / 图像 / 语音 / 生图仍各自限额；Claude 免费档约 15–40 条 / 5 小时滚动窗口；Kimi 免费 Adagio 档含联网与 1M 上下文但重度 / 智能体用法计费。⚠️ 闭源免费档普遍把你的对话用于改进产品（除非付费），敏感数据勿走免费层。<br><br>
      <b>④ 战略信号</b>：阿里用开源权重回应 OpenAI 降价，OpenAI 用免费档放开回应开源——<b>「量大能用的先进模型」正从「付费专属」走向「免费普惠」</b>，无论开源还是闭源，对用户都是利好；但请始终分清「聊天产品免费」与「API 可白嫖」与「权重可自部署」这三件事。
    </p>
    <div class="hot-grid">
      <div class="hot-item"><div class="k">GPT-5.6 Luna</div><div class="v">8/6 降价 80%</div></div>
      <div class="hot-item"><div class="k">ChatGPT 免费</div><div class="v">本周取消文本限</div></div>
      <div class="hot-item"><div class="k">免费默认</div><div class="v">Luna（8/6 起）</div></div>
      <div class="hot-item"><div class="k">闭源免费档</div><div class="v">ChatGPT/Claude/Gemini/Kimi</div></div>
      <div class="hot-item"><div class="k">仅文本不限</div><div class="v">文件/图/音仍限</div></div>
      <div class="hot-item"><div class="k">战略信号</div><div class="v">开源闭源同卷免费</div></div>
    </div>
    <a class="hot-link" href="https://chat.openai.com" target="_blank">前往 ChatGPT 免费档 →</a>
  </div>'''

html = re.sub(
    r'  <!-- Hot featured 1:.*?\n  <!-- Top advanced free models -->',
    NEW_HOT1 + "\n" + NEW_HOT2 + "\n\n  <!-- Top advanced free models -->",
    html, count=1, flags=re.S,
)

# ---- 7. Footer ----
NEW_FOOTER = '''  <div class="footer">
    <p>📅 下次更新：明日 09:30 · 数据来源：freellm.net 实时实测目录（首页 424+ 免费模型、30 家供应商、316 款 Free &amp; Online、244 款经实时 API 验证、最新刷新 2026-8-7/8-8；本期读数 Kimi K3 98（Ollama Cloud）/ GLM-5.2 95（NVIDIA NIM）/ Gemini 3.6 Flash 91（AI Studio）/ DeepSeek V4-Flash 91（OpenRouter 免费层）·90（Ollama）·88（NIM）/ MiniMax M3 91（OpenRouter 免费层）·89（NIM）/ Tencent Hy3 90（WorkBuddy/CodeBuddy 限免至 8/31，OpenRouter 已转 Paid）/ Gemini 3.5 Flash 88 / DeepSeek V4-Pro 85（NIM·Ollama）/ Nemotron 3 Ultra 85（OpenRouter）/ Kimi K2.6 83（NIM）/ Agnes 2.0 Flash 81 / Gemini 3.5 Flash-Lite 81）、阿里通义千问官方发布与技术博客（Qwen3.8-Max 2.4T / 95B 激活 / 1M 上下文 / 本周 8/10 起开源权重 + Qwen3.8-27B / 海外 $2·$6、国内 12·36 元每百万、PaperBench 93.0 / SWE-bench Pro 67.7）、byteiota / frontiernews / cnblogs / SCMP（Qwen3.8 开源「本周落地」+ 下载前必读四件事：LICENSE 未定可能走 Tongyi Qianwen Licence、Max 需 ~20 H100、27B 4-bit 跑 RTX 4090、社区量化晚 1–2 周）、OpenAI 官方与 felloai（8/6 GPT-5.6 Luna 降价 80%、ChatGPT 免费档 week of 8/10 取消文本条数限制）、HuggingFace（MiniMax H3 开源 3 天登顶全球热度榜首）、经济日报 8/10 专题「中国开源 AI 惠及全球」（下载占全球 41% 第一）、腾讯官方（8/4 Hy3 限免延长至 8/31）、智谱官方 8/7 确认（GLM-5.3 发布在即·万亿参数·史诗级 plus）、DeepSeek 开放平台 8/6 公告（计划大幅上调 API 定价、峰谷定价）、NVIDIA 官方 GLM-5.2 基准卡与 build.nvidia.com（141 模型 77 永久免费）、OpenRouter 官方定价页（50 次/天账户级、充 $10 升 1000 次/天）、腾讯云 TokenHub、中国移动云 MoMA、国家超算互联网 SCNet、阿里云百炼、美团 LongCat、火山引擎、硅基流动、魔搭 ModelScope</p>
    <p style="margin-top:8px;">⚠️ 免费额度可能随时间调整，请以各平台官网最新政策为准 | 评分数据来自 freellm.net 实时实测，不同供应商托管同一模型分数不同，已分别标注平台 | 本期主线：阿里 Qwen3.8-Max（2.4T）/ Qwen3.8-27B 开源权重进入「本周（8/10 起）落地窗口」+ 下载前必读四件事（许可证/硬件/量化/自测基准）+ OpenAI 8/6 对 GPT-5.6 Luna 降价 80% 触发开源竞赛 + ChatGPT 免费档本周取消文本条数限制 + 免费先进模型格局稳定（Kimi K3 98 蝉联第一）</p>
    <p style="margin-top:8px;">⭐ <a href="https://github.com/lph12168x/Free-LLM-Daily" target="_blank">lph12168x/Free-LLM-Daily</a> · 🤖 由 WorkBuddy 自动化生成</p>
  </div>'''
html = re.sub(r'<div class="footer">.*?</div>\n\n</div>', NEW_FOOTER + '\n\n</div>', html, count=1, flags=re.S)

with open(dst, "w", encoding="utf-8") as f:
    f.write(html)

# ---- Validation ----
open_count = html.count("<div")
close_count = html.count("</div>")
print(f"Written: {dst}")
print(f"div open={open_count} close={close_count} balanced={open_count==close_count}")
print(f"U+FFFD (mojibake) count = {html.count(chr(0xFFFD))}")
# sanity: ensure key marks present
for marker in ["2026-08-11", "本周（8/10 起）", "GPT-5.6 Luna", "page-nav"]:
    print(f"  contains '{marker}': {marker in html}")
