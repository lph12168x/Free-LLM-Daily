#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate daily-free-llm-2026-08-18.html (backfill, missing from prior run)
and daily-free-llm-2026-08-19.html (today) from the 08-17 template.
Stable sections (Top10 grid, platforms, combos, risks, CSS) kept verbatim;
only date-specific hero/focus/hot-cards/footer/nav/stats are refreshed.
"""
import os, re

base = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(base, "daily-free-llm-2026-08-17.html")
dst18 = os.path.join(base, "daily-free-llm-2026-08-18.html")
dst19 = os.path.join(base, "daily-free-llm-2026-08-19.html")

with open(src, encoding="utf-8") as f:
    tpl = f.read()

# ----------------------------------------------------------------------
# Shared helpers
# ----------------------------------------------------------------------
def build(html, date_tag, date_chip, title, meta, nav, tagline, stat_models,
          stat_label, focus_block, hot_block, footer_block):
    html = html.replace(
        '<title>免费大模型日报 · 2026-08-17 · Free LLM Daily</title>',
        f'<title>免费大模型日报 · {date_tag} · Free LLM Daily</title>', 1)
    html = re.sub(r'<meta name="description" content="[^"]*"?>', meta, html, count=1)
    html = html.replace(
        '<div class="page-nav"><a href="daily-free-llm-2026-08-14.html" title="上一篇日报">← 上一个</a><a class="nav-home" href="index.html" title="返回首页">🏠 主页</a><a class="nav-latest" href="daily-free-llm-2026-08-18.html" title="最新日报">⭐ 最新</a><a href="daily-free-llm-2026-08-18.html" title="下一篇日报">下一个 →</a></div>',
        nav, 1)
    html = html.replace(
        '<div class="date-chip">📅 2026 年 8 月 17 日 · 周一</div>',
        f'<div class="date-chip">📅 {date_chip}</div>', 1)
    html = html.replace(
        '<p class="tagline">聚焦「量大能用的先进模型」· 覆盖 30+ 国内外平台 · 评分数据来自 freellm.net 实时实测（424+ 免费模型、30 家供应商，目录更新于 2026-8-8、API Key 索引更新至 8/15），并经阿里千问官方开源公告、OpenCode Zen 官方文档、NVIDIA 官方基准卡、OpenRouter / Google AI Studio / Groq 官方限额页、Hugging Face 与 ModelScope 趋势榜、Artificial Analysis 多源交叉验证</p>',
        f'<p class="tagline">{tagline}</p>', 1)
    html = html.replace('<div class="stat-num">424+</div>', f'<div class="stat-num">{stat_models}</div>', 1)
    html = html.replace('免费大模型（freellm.net 实测 · 316 在线）', stat_label, 1)
    html = html.replace('GLM-5.2 稳居 95', 'GLM-5.2 稳居 94', 1)
    # Focus block: from <!-- Focus banner --> up to (not incl) <!-- Hot featured -->
    html = re.sub(r'  <!-- Focus banner -->.*?  <!-- Hot featured -->',
                  focus_block + '\n  <!-- Hot featured -->', html, count=1, flags=re.S)
    # Hot block: from <!-- Hot featured --> up to (not incl) <!-- Top advanced free models -->
    html = re.sub(r'  <!-- Hot featured -->.*?  <!-- Top advanced free models -->',
                  hot_block + '\n  <!-- Top advanced free models -->', html, count=1, flags=re.S)
    # Footer
    html = re.sub(r'  <div class="footer">.*?</div>\n\n</div>',
                  footer_block + '\n\n</div>', html, count=1, flags=re.S)
    return html

# ======================================================================
# 2026-08-18 (backfill)
# ======================================================================
NAV18 = ('<div class="page-nav"><a href="daily-free-llm-2026-08-17.html" title="上一篇日报">← 上一个</a>'
         '<a class="nav-home" href="index.html" title="返回首页">🏠 主页</a>'
         '<a class="nav-latest" href="daily-free-llm-2026-08-19.html" title="最新日报">⭐ 最新</a>'
         '<a href="daily-free-llm-2026-08-19.html" title="下一篇日报">下一个 →</a></div>')

META18 = ('<meta name="description" content="2026年8月18日免费大模型日报：聚焦量大能用的先进模型。'
    '🔥 今日主线——火山引擎方舟 8/18 起开放每日 200 万 Token 免费额度（含 DeepSeek V4 Pro），作为 DeepSeek 官方 API 8/17 峰谷涨价的补偿；'
    'DeepSeek 官方 API 8/17 起分时定价：V4 Pro 高峰缓存命中输入 0.025→0.30 元/百万（+1100%）、输出 6→27 元/百万（+350%），低谷半价；'
    'Nous Portal 新提供 3 款免费模型（Step-3.7-Flash / Nemotron-3-Ultra / Owl-Alpha），OpenAI 兼容、OAuth device-code 登录。'
    '免费先进榜格局稳定（Kimi K3 98 蝉联第一）。">')

TAGLINE18 = ('聚焦「量大能用的先进模型」· 覆盖 30+ 国内外平台 · 本期主线：'
    '<b>火山引擎方舟 8/18 起每日 200 万 Token 免费（含 V4 Pro）——DeepSeek 官方 API 8/17 峰谷涨价后的补偿方案</b>；'
    '<b>DeepSeek 官方 API 8/17 分时定价生效：V4 Pro 高峰输入 0.30 / 输出 27 元每百万，低谷半价</b>；'
    '<b>Nous Portal 新上 3 款免费模型（Step-3.7-Flash / Nemotron-3-Ultra / Owl-Alpha）</b>；'
    '<b>免费先进榜稳定（Kimi K3 98 蝉联第一）</b>。')

FOCUS18 = '''  <!-- Focus banner -->
  <div class="focus">
    <h2>📌 本期焦点：火山引擎方舟 8/18 每日 200 万 Token 免费（含 V4 Pro）——DeepSeek 官方 API 8/17 峰谷涨价后的补偿；DeepSeek 官方 API 8/17 起分时定价（V4 Pro 高峰输入 0.30 / 输出 27 元每百万，低谷半价）；Nous Portal 新提供 3 款免费模型（Step-3.7-Flash / Nemotron-3-Ultra / Owl-Alpha）· 免费先进榜稳定（Kimi K3 98 蝉联第一）</h2>
    <p>
      <b>今日头号（对「免费党」最直接）</b>：8 月 18 日起，<b>火山引擎方舟</b>开放<b>每日 200 万 Token 的免费额度</b>，且<b>包含 DeepSeek V4 Pro</b>——这正是对 8/17 DeepSeek 官方 API 峰谷涨价的补偿。⚠️ 实操提醒：免费额度按账号每日刷新，建议在控制台手动设置 <span class="hl">190 万 Token 熔断</span>，避免超额后被计费；V4 Pro 免费档速度/并发弱于付费，重度任务仍会受限。<br><br>
      <b>今日次条（看清涨价）</b>：DeepSeek 官方 API 自 8/17 起启用<b>分时定价</b>：以 V4 Pro 为例，<b>高峰</b>缓存命中输入 <b>0.025→0.30 元/百万（+1100%）</b>、输出 <b>6→27 元/百万（+350%）</b>；<b>低谷半价</b>。纯 API 免费党受到直接冲击——这也是为什么免费入口要转向<b>火山引擎方舟 / NVIDIA NIM / OpenCode Zen</b> 等仍免费的通道。提醒：<span class="hl">免费先进榜里的 DeepSeek V4-Flash 仍是性价比之选</span>，V4-Pro 已非「免费」定位。<br><br>
      <b>新入口：Nous Portal</b>：Nous 社区新提供 <b>3 款免费模型</b>——<b>Step-3.7-Flash / Nemotron-3-Ultra / Owl-Alpha</b>，OpenAI 兼容、<b>OAuth device-code 登录</b>（无需信用卡）。这是继 OpenCode Zen、OpenRouter 之后又一条「开箱即用的免费 API」路径，适合快速接入任意 OpenAI 兼容客户端。<br><br>
      <b>榜单变化</b>：<span class="hl">kimi-k3（Ollama Cloud）以 98 分登顶 freellm.net 全部免费模型</span>（但为 session/weekly 限额）；<b>GLM-5.2（NVIDIA NIM 实测 94、1M 上下文、40 RPM 无固定日额度）仍是「量大能用」最稳冠军</b>。Gemini 3.6 Flash（91）、DeepSeek V4 Flash（Ollama 90 / NIM 88）、MiniMax M3（89）紧随其后。Tencent Hy3 经 WorkBuddy/CodeBuddy 限免至 8/31（剩 13 天）仍可用，OpenRouter 已转 Paid。<br><br>
      倒计时：<span class="countdown">8/20 LobsterAI 网易 5000 积分活动截止</span> · <span class="countdown">8/31 腾讯 Hy3 限免截止（剩 13 天）</span> · <span class="countdown">9/30 腾讯混元旧平台停服</span> · <span class="countdown">10/21 Google Cloud 16 个 MaaS 端点退役</span>。
    </p>
  </div>'''

HOT18 = '''  <!-- Hot featured 1: Volcano Engine 2M free -->
  <div class="hot">
    <span class="flag">🎁 8/18 上线 · 火山引擎方舟每日 200 万 Token 免费额度（含 DeepSeek V4 Pro）——DeepSeek 官方 API 8/17 峰谷涨价后的补偿方案，需手动设 190 万 Token 熔断</span>
    <h2>火山引擎方舟每日 200 万 Token 免费（含 V4 Pro）：DeepSeek 涨价后的「白嫖」出口，但记得设熔断</h2>
    <div class="sub">火山引擎 8/18 起 · 每日 200 万 Token 免费 · 含 V4 Pro · 建议手动设 190 万 Token 熔断防超额 · OpenAI 兼容 · 需登录火山账号</div>
    <p>
      <b>① 发生了什么</b>：8 月 18 日起，火山引擎方舟（Volcano Engine Ark）开放<b>每日 200 万 Token 的免费额度</b>，且覆盖 <b>DeepSeek V4 Pro</b>。这正好对冲 8/17 DeepSeek 官方 API 的分时涨价——把原本要付费的 V4 Pro 调用，部分转移到火山方舟的免费额度。<br><br>
      <b>② 怎么用才不踩坑</b>：免费额度<b>按账号每日刷新</b>，建议在控制台为免费应用手动设置 <span class="hl">190 万 Token 的用量熔断</span>，避免超出免费额度后被按付费单价计费；V4 Pro 免费档的并发与速度弱于付费，长链路 / 高并发任务要预留降级方案。<br><br>
      <b>③ 与其他免费通道的关系</b>：免费党的「先进模型」入口现在形成三足——<b>火山引擎方舟（200 万/天，含 V4 Pro）</b>、<b>NVIDIA NIM（40 RPM 无日限额、77 款永久免费端点）</b>、<b>OpenCode Zen（多款 -Free 限时免费）</b>。按需分流：要 V4 Pro 走火山，要 GLM-5.2 / DeepSeek V4-Flash 走 NIM，要编码 Agent 走 Zen。<br><br>
      <b>④ 冷静一点</b>：免费 ≠ 无限。火山方舟免费档有速率与模型范围限制；DeepSeek 官方 API 高峰价已是低价的 4–12 倍（8/17 起），长期重度使用务必成本评估。
    </p>
    <div class="hot-grid">
      <div class="hot-item"><div class="k">免费额度</div><div class="v">200 万 Token/天</div></div>
      <div class="hot-item"><div class="k">含模型</div><div class="v">DeepSeek V4 Pro</div></div>
      <div class="hot-item"><div class="k">建议熔断</div><div class="v">190 万 Token</div></div>
      <div class="hot-item"><div class="k">兼容</div><div class="v">OpenAI 兼容</div></div>
      <div class="hot-item"><div class="k">定位</div><div class="v">涨价补偿·限时免费</div></div>
      <div class="hot-item"><div class="k">最大风险</div><div class="v">超额计费</div></div>
    </div>
    <a class="hot-link" href="https://www.volcengine.com/product/ark" target="_blank">前往火山引擎方舟 →</a>
  </div>

  <!-- Hot featured 2: DeepSeek peak/valley pricing + Nous Portal -->
  <div class="hot">
    <span class="flag">💰 8/17 生效 · DeepSeek 官方 API 分时定价：V4 Pro 高峰输入 0.30 / 输出 27 元每百万（低谷半价）；同期 Nous Portal 新上 3 款免费模型（Step-3.7-Flash / Nemotron-3-Ultra / Owl-Alpha），OpenAI 兼容、OAuth device-code 登录</span>
    <h2>DeepSeek 官方 API 峰谷涨价 + Nous Portal 3 款免费模型上新：免费党换道，开箱即用再添一条</h2>
    <div class="sub">DeepSeek 8/17 起 · V4 Pro 高峰缓存命中输入 0.025→0.30 元/百万(+1100%)、输出 6→27 元/百万(+350%)、低谷半价 · Nous Portal：Step-3.7-Flash / Nemotron-3-Ultra / Owl-Alpha，OAuth device-code 登录免卡</div>
    <p>
      <b>① DeepSeek 峰谷定价（涨价的落地）</b>：自 8/17 起，DeepSeek 官方 API 启用<b>分时定价</b>。以 V4 Pro 为例：<b>高峰</b>缓存命中输入 <b>0.025→0.30 元/百万（+1100%）</b>、输出 <b>6→27 元/百万（+350%）</b>；<b>低谷时段半价</b>。V4-Flash 同样受影响但幅度较小。这正是此前预告的涨价兑现——<span class="hl">免费党请改走火山引擎方舟 / NVIDIA NIM / OpenCode Zen</span>。<br><br>
      <b>② Nous Portal 免费模型上新</b>：Nous 社区新提供 <b>3 款免费模型</b>——<b>Step-3.7-Flash</b>（阶跃星斗）、<b>Nemotron-3-Ultra</b>（NVIDIA 550B 推理）、<b>Owl-Alpha</b>，全部 <b>OpenAI 兼容</b>，通过 <b>OAuth device-code 登录</b>（无需信用卡）。这是继 OpenCode Zen、OpenRouter 后又一条开箱即用的免费 API，适合快速接入任意 OpenAI 兼容客户端。<br><br>
      <b>③ 免费通道总览（截至 8/18）</b>：OpenRouter（Nemotron 3 Ultra、Gemma 4、gpt-oss、Ling-3.0-flash 等 25+，50 次/天、充 $10 升 1000）；OpenCode Zen（DeepSeek V4 Flash Free、MiniMax M3 Free、Nemotron 3 Ultra Free、Big Pickle、MiMo-V2.5 Free 等限时免费）；NVIDIA NIM（77 款永久免费端点、40 RPM 无日限额）；火山引擎方舟（200 万/天，含 V4 Pro）；Nous Portal（3 款新免费）；Google AI Studio（Gemini 3.6 Flash 1500 次/天）；Groq（14400 次/天）。<br><br>
      <b>④ 策略</b>：日常白嫖继续用 <b>GLM-5.2（NIM 94 分永久免费）</b> 与 <b>kimi-k3（Ollama 98 分，限额）</b>；要 V4 Pro 走火山方舟免费档；编码 Agent 走 OpenCode Zen；都别把免费档用于敏感/客户数据（部分端点用于训练）。
    </p>
    <div class="hot-grid">
      <div class="hot-item"><div class="k">V4 Pro 高峰输入</div><div class="v">0.30 元/百万</div></div>
      <div class="hot-item"><div class="k">V4 Pro 高峰输出</div><div class="v">27 元/百万</div></div>
      <div class="hot-item"><div class="k">低谷</div><div class="v">半价</div></div>
      <div class="hot-item"><div class="k">Nous 免费款</div><div class="v">3 款</div></div>
      <div class="hot-item"><div class="k">Nous 登录</div><div class="v">OAuth device-code</div></div>
      <div class="hot-item"><div class="k">免费入口</div><div class="v">火山/NIM/Zen/Nous</div></div>
    </div>
    <a class="hot-link" href="https://platform.deepseek.com" target="_blank">查看 DeepSeek 官方定价 →</a>
  </div>'''

FOOTER18 = '''  <div class="footer">
    <p>📅 下次更新：明日 09:30 · 数据来源：freellm.net 实时实测目录（424+ 免费模型、30 家供应商，目录更新于 2026-8-17；Top10 评分 kimi-k3 98 / GLM-5.2 94 / Gemini 3.6 Flash 91 / DeepSeek V4 Flash 90 / MiniMax M3 89 / Gemini 3.5 Flash 88 / Nex-N2-Pro 88 / Nemotron 3 Ultra 85 / Ling-3.0-flash 87 / Kimi K2.6 84）、DeepSeek 官方 API 公告（8/17 峰谷分时定价：V4 Pro 高峰缓存命中输入 0.025→0.30、输出 6→27 元/百万，低谷半价）、火山引擎方舟官方文档（8/18 起每日 200 万 Token 免费、含 V4 Pro、建议 190 万熔断）、Nous Portal 官方（Step-3.7-Flash / Nemotron-3-Ultra / Owl-Alpha 3 款免费、OAuth device-code 登录）、NVIDIA 官方 GLM-5.2 基准卡与 build.nvidia.com（125 模型、77 永久免费）、OpenCode Zen 官方文档（Base URL https://opencode.ai/zen/v1）、OpenRouter 官方定价页（免费层 50 / 1000 次每天）、Google AI Studio 与 Groq 官方限额页、阿里千问官方开源公告（Qwen3.8-27B Apache 2.0）、Hugging Face 与 ModelScope 趋势榜、Artificial Analysis</p>
    <p style="margin-top:8px;">⚠️ 免费额度可能随时间调整，请以各平台官网最新政策为准 | 评分数据来自 freellm.net 实时实测，不同供应商托管同一模型分数不同，已分别标注平台 | 本期主线：火山引擎方舟每日 200 万 Token 免费（含 V4 Pro，涨价补偿）+ DeepSeek 官方 API 8/17 峰谷涨价（V4 Pro 高峰输入 0.30/输出 27 元每百万，低谷半价）+ Nous Portal 3 款免费模型（Step-3.7-Flash / Nemotron-3-Ultra / Owl-Alpha）+ 免费先进榜稳定（Kimi K3 98 蝉联第一）</p>
    <p style="margin-top:8px;">⭐ <a href="https://github.com/lph12168x/Free-LLM-Daily" target="_blank">lph12168x/Free-LLM-Daily</a> · 🤖 由 WorkBuddy 自动化生成</p>
  </div>'''

html18 = build(tpl, "2026-08-18", "2026 年 8 月 18 日 · 周二", "2026-08-18",
               META18, NAV18, TAGLINE18, "424+",
               "免费大模型（freellm.net 实测 · 316 在线）",
               FOCUS18, HOT18, FOOTER18)
with open(dst18, "w", encoding="utf-8") as f:
    f.write(html18)

# ======================================================================
# 2026-08-19 (today)
# ======================================================================
NAV19 = ('<div class="page-nav"><a href="daily-free-llm-2026-08-18.html" title="上一篇日报">← 上一个</a>'
         '<a class="nav-home" href="index.html" title="返回首页">🏠 主页</a>'
         '<a class="nav-latest" href="daily-free-llm-2026-08-19.html" title="最新日报">⭐ 最新</a>'
         '<span class="nav-disabled" title="已是最新">下一个 →</span></div>')

META19 = ('<meta name="description" content="2026年8月19日免费大模型日报：聚焦量大能用的先进模型。'
    '🔥 今日头号——智谱 GLM-5.3 API 8/19 凌晨正式上线：743B 参数、沿用 GLM-5.2 底座经后训练缩放，AA Intelligence Index 60 分，与 Kimi K3 并列开源第一、与 Claude Fable 5 / GPT-5.6 Sol 同档；Terminal-Bench 3.0 28.3（从 4.6 升）、DeepSWE v1.1 66.9、Agents’ Last Exam 28.5、CyberGym 84.5%；定价与 GLM-5.2 持平（腾讯云 输入 8 / 输出 28 / 缓存命中 2 元每百万），权重下周五（8/28）开源。'
    '同期——中国开源 AI 成美国大模型「底座」：Qwen3.8-27B 登顶 HuggingFace 趋势榜、开源两天下载破 100 万次、衍生模型超 15 万居全球第一；DeepSeek Harness 三天 GitHub Star 超 13 万。'
    '免费先进榜格局稳定（Kimi K3 98 蝉联第一）。">')

TAGLINE19 = ('聚焦「量大能用的先进模型」· 覆盖 30+ 国内外平台 · 本期主线：'
    '<b>智谱 GLM-5.3 API 8/19 凌晨上线（743B、AA Index 60 并列开源第一，付费 API 但权重 8/28 开源进 NIM 免费层；当下免费仍是 GLM-5.2·NIM 94）</b>；'
    '<b>中国开源 AI 成美国大模型「底座」：Qwen3.8-27B 登顶 HF 趋势榜、两天下载破百万、衍生 15 万+</b>；'
    '<b>DeepSeek Harness 三天破 13 万 Star</b>；'
    '<b>freellm.net 扩至 442+ 免费模型 / 31 家供应商</b>；'
    '<b>免费先进榜稳定（Kimi K3 98 蝉联第一）</b>。')

FOCUS19 = '''  <!-- Focus banner -->
  <div class="focus">
    <h2>📌 本期焦点：智谱 GLM-5.3 API 8/19 凌晨上线——743B、AA Index 60 并列开源第一（与 Kimi K3）、与 Claude Fable 5 / GPT-5.6 Sol 同档，付费 API 但权重下周五（8/28）开源；同期中国开源 AI 成美国大模型「底座」：Qwen3.8-27B 登顶 HF 趋势榜、两天下载破百万、衍生 15 万+；DeepSeek Harness 三天破 13 万 Star · 免费先进榜稳定（Kimi K3 98 蝉联第一）</h2>
    <p>
      <b>今日头号（对「开源前沿」最有冲击力）</b>：8 月 19 日凌晨，智谱（Z.ai）正式上线新一代基座模型 <b>GLM-5.3</b> 的 API。它<b>沿用 GLM-5.2 底座、全部提升来自后训练缩放</b>，在 Artificial Analysis Intelligence Index 取得 <b>60 分</b>，<b>与 Kimi K3 并列开源模型第一</b>，并进入全球前沿模型区间，与 <b>Claude Fable 5、GPT-5.6 Sol</b> 等闭源旗舰处于同一水平。编程与长程 Agent 能力大幅跃升：Terminal-Bench 3.0 由 4.6 升至 <b>28.3</b>、DeepSWE v1.1 <b>66.9</b>、Agents’ Last Exam <b>28.5</b>、白盒漏洞发现 CyberGym <b>84.5%</b>（高于 Mythos 5 的 83.8%）。<br><br>
      <b>免费角度（关键）</b>：GLM-5.3 当前是<b>付费 API</b>（腾讯云报价 输入 8 / 输出 28 / 缓存命中 2 元每百万，与 GLM-5.2 持平），<b>权重计划于下周五（8/28）以负责任方式开源</b>——届时将可本地部署并有望进入 NVIDIA NIM 永久免费层。⚠️ 所以「今日免费入口」仍是 <span class="hl">GLM-5.2（NVIDIA NIM 实测 94 分、1M 上下文、40 RPM 无日限额、永久免费）</span>；GLM-5.3 标记为「即将免费（8/28 开源权重）」，等权重落地再切。<br><br>
      <b>同期大事：中国开源成美国「底座」</b>：Hugging Face《开源模型现状：2026 夏季观察》显示，中国实验室月度最大开源模型规模（7540 亿–2.78 万亿）持续领先美国，<b>部分美国千亿级模型以中国模型为底座</b>。具体到本期：<b>Qwen3.8-27B 登顶 HF 趋势榜</b>，开源两天<b>下载破 100 万次</b>、衍生模型超 <b>15 万个居全球第一</b>（Apache 2.0，24GB 显卡即可本地跑）。开源生态的「量变」正在转化为影响力。<br><br>
      <b>生态侧</b>：DeepSeek Harness（DSH）8/13 开放预览，三天 GitHub Star <b>超 13 万</b>、Fork 近 1.4 万，社区涌现近 6000 个 dsh-plugin 仓库——开源 Agent 工具链热度印证「免费 + 开源」路线的爆发。<br><br>
      <b>榜单变化</b>：<span class="hl">kimi-k3（Ollama Cloud）以 98 分登顶 freellm.net 全部免费模型</span>（但为 session/weekly 限额）；<b>GLM-5.2（NVIDIA NIM 94 / 1M / 40 RPM）仍是「量大能用」最稳冠军</b>；Gemini 3.6 Flash（91）、DeepSeek V4 Flash（Ollama 90 / NIM 88）、MiniMax M3（89）紧随。场外 Tencent Hy3 经 WorkBuddy/CodeBuddy 限免至 8/31（剩 13 天）仍可用，OpenRouter 已转 Paid。<br><br>
      倒计时：<span class="countdown">8/20 LobsterAI 网易 5000 积分活动截止</span> · <span class="countdown">8/28 GLM-5.3 权重开源（还有 9 天）</span> · <span class="countdown">8/31 腾讯 Hy3 限免截止（剩 13 天）</span> · <span class="countdown">9/30 腾讯混元旧平台停服</span> · <span class="countdown">10/21 Google Cloud 16 个 MaaS 端点退役</span>。
    </p>
  </div>'''

HOT19 = '''  <!-- Hot featured 1: Zhipu GLM-5.3 API live -->
  <div class="hot">
    <span class="flag">🔥 今日上线 · 智谱 GLM-5.3 API 8/19 凌晨正式开放——743B、AA Index 60 并列开源第一（与 Kimi K3），与 Claude Fable 5 / GPT-5.6 Sol 同档；付费 API，权重下周五（8/28）开源进 NIM 免费层</span>
    <h2>智谱 GLM-5.3 API 上线：AA Index 60 并列开源第一、编程/安全能力翻倍，但当下免费入口仍是 GLM-5.2（NIM 永久免费）</h2>
    <div class="sub">智谱 8/19 凌晨 · 743B 沿用 GLM-5.2 底座、后训练缩放 · AA Index 60（开源并列第一）· Terminal-Bench 3.0 28.3 / DeepSWE v1.1 66.9 / Agents’ Last Exam 28.5 / CyberGym 84.5% · 定价同 GLM-5.2（输入8/输出28/缓存2 元每百万）· 权重 8/28 开源</div>
    <p>
      <b>① 发生了什么</b>：8 月 19 日凌晨，智谱（Z.ai）正式上线 <b>GLM-5.3</b> API。它<b>沿用 GLM-5.2 的架构与 743B 参数规模</b>，全部能力跃升来自后训练（数十倍扩充的长程任务环境、IndexShare / SAO / 新一代 Slime 框架强化学习）。在 AA Intelligence Index 取得 <b>60 分</b>，<b>与 Kimi K3 并列开源第一</b>，并进入全球前沿模型区间，与 Claude Fable 5、GPT-5.6 Sol 同档——以更小参数规模、更低单任务成本把「智能—成本」帕累托前沿显著推进。<br><br>
      <b>② 能力亮点</b>：终端操作与长程 Agent 任务领先 Kimi K3（Terminal-Bench 3.0 <b>28.3 对 17.4</b>）；自研 Z.ai CodeBench High 档准确率 31.4%、每任务输出约 5 万 tokens，优于 Claude Opus 4.8（29.5% / 约 12 万 tokens）；网络安全能力加速涌现，白盒漏洞发现 CyberGym <b>84.5%</b>（高于 Mythos 5 的 83.8%）。已通过 ZCode、GLM Coding Plan 等向开发者提供服务，支持 1M 上下文、128K 最大输出。<br><br>
      <b>③ 免费角度（务必看清）</b>：GLM-5.3 当前是<b>付费 API</b>（腾讯云 输入 8 / 输出 28 / 缓存命中 2 元每百万，与 GLM-5.2 持平），<b>权重计划下周五（8/28）开源</b>。届时本地部署 + 上 NVIDIA NIM 免费层才真正「免费」。⚠️ 所以今天要白嫖先进模型，<span class="hl">首选仍是 GLM-5.2（NVIDIA NIM 94 分、1M 上下文、40 RPM 无日限额、永久免费）</span>；GLM-5.3 标为「即将免费」，等 8/28 权重落地再切。<br><br>
      <b>④ 策略</b>：重度编码/Agent 任务若愿付费，GLM-5.3 是当下开源第一梯队（接近 Fable 5）；日常零成本继续用 GLM-5.2（NIM）/ kimi-k3（Ollama，限额）/ Gemini 3.6 Flash（AI Studio）/ DeepSeek V4-Flash（NIM/Ollama）。蹲 8/28 GLM-5.3 权重开源，预计将直接进 NIM 免费层。
    </p>
    <div class="hot-grid">
      <div class="hot-item"><div class="k">参数</div><div class="v">743B（沿用5.2底座）</div></div>
      <div class="hot-item"><div class="k">AA Index</div><div class="v">60（开源并列第一）</div></div>
      <div class="hot-item"><div class="k">Terminal-Bench 3.0</div><div class="v">28.3（从4.6升）</div></div>
      <div class="hot-item"><div class="k">API 定价</div><div class="v">8/28/2 元每百万</div></div>
      <div class="hot-item"><div class="k">权重开源</div><div class="v">8/28（还有 9 天）</div></div>
      <div class="hot-item"><div class="k">当下免费替代</div><div class="v">GLM-5.2 (NIM 94)</div></div>
    </div>
    <a class="hot-link" href="https://z.ai" target="_blank">前往智谱 Z.ai / GLM-5.3 →</a>
  </div>

  <!-- Hot featured 2: China open-source as US base + Qwen3.8-27B tops HF -->
  <div class="hot">
    <span class="flag">🌏 生态爆发 · 中国开源 AI 成美国大模型「底座」：Qwen3.8-27B 登顶 HuggingFace 趋势榜、开源两天下载破 100 万次、衍生模型超 15 万居全球第一；DeepSeek Harness 三天 GitHub Star 超 13 万</span>
    <h2>中国开源成美国「底座」：Qwen3.8-27B 登顶 HF 趋势榜、两天下载破百万、衍生 15 万+——开源免费生态的量变到质变</h2>
    <div class="sub">HF《开源模型现状：2026 夏季观察》· 中国月度最大开源模型 7540 亿–2.78 万亿持续领先美国 · 部分美国千亿级模型以中国模型为底座 · Qwen3.8-27B Apache 2.0、24GB 显卡可跑 · DSH 三天 13 万+ Star</div>
    <p>
      <b>① Qwen3.8-27B 登顶 HF 趋势榜</b>：阿里千问的 <b>Qwen3.8-27B</b>（Apache 2.0、27B 原生多模态稠密、262K/YaRN 1M、4-bit 约 17GB 即 24GB 显卡可跑）开源后<b>两天下载破 100 万次</b>，衍生模型超 <b>15 万个、居全球第一</b>。这是目前对个人开发者最友好的「先进模型零成本本地部署」选择——完全商用自由、无收入阈值。<br><br>
      <b>② 中国开源成美国「底座」</b>：Hugging Face《开源模型现状：2026 夏季观察》显示，中国实验室月度最大开源模型规模（7540 亿–2.78 万亿参数）持续领先美国，<b>部分美国千亿级模型已以中国模型为底座</b>。Counterpoint 指出：若西方巨头只顾封闭「围墙花园」，开发者与企业自然转向中国开放权重模型。开源≠免费 API，但本地部署的零成本路径正被中国模型主导。<br><br>
      <b>③ 工具链热度</b>：DeepSeek Harness（DSH）8/13 开放预览，<b>三天 GitHub Star 超 13 万</b>、Fork 近 1.4 万，社区涌现近 6000 个 dsh-plugin 仓库——印证「免费 + 开源 + Agent 工具链」路线的爆发。⚠️ 官方治理仍缺位、Discussion 区被广告攻占，深度适配存 Bug，生产接入需谨慎。<br><br>
      <b>④ 对「免费可用」的含义</b>：免费先进模型的供给端正在快速扩张——kimi-k3、GLM-5.2、Qwen3.8-27B、MiniMax M3、Ling-3.0-flash、Nemotron 3 Ultra 等开放权重 + 多家云厂商常驻免费层，叠加 OpenCode Zen / OpenRouter / Nous Portal / 火山引擎方舟等多条开箱即用免费 API。<span class="hl">「量大能用的先进模型」从未像今天这样唾手可得</span>。
    </p>
    <div class="hot-grid">
      <div class="hot-item"><div class="k">Qwen3.8-27B 下载</div><div class="v">2 天破 100 万</div></div>
      <div class="hot-item"><div class="k">衍生模型</div><div class="v">15 万+（全球第一）</div></div>
      <div class="hot-item"><div class="k">许可</div><div class="v">Apache 2.0</div></div>
      <div class="hot-item"><div class="k">DSH Star</div><div class="v">3 天 13 万+</div></div>
      <div class="hot-item"><div class="k">中国开源规模</div><div class="v">7540亿–2.78万亿</div></div>
      <div class="hot-item"><div class="k">趋势</div><div class="v">量变→质变</div></div>
    </div>
    <a class="hot-link" href="https://huggingface.co/Qwen" target="_blank">查看 Qwen 官方权重 →</a>
  </div>'''

FOOTER19 = '''  <div class="footer">
    <p>📅 下次更新：明日 09:30 · 数据来源：freellm.net 实时实测目录（442+ 免费模型、31 家供应商、329 免费在线、283 免信用卡，目录更新于 2026-8-17/18；Top10 评分 kimi-k3 98 / GLM-5.2 94 / Gemini 3.6 Flash 91 / DeepSeek V4 Flash 90 / MiniMax M3 89 / Gemini 3.5 Flash 88 / Nex-N2-Pro 88 / Nemotron 3 Ultra 85 / Ling-3.0-flash 87 / Kimi K2.6 84）、智谱 Z.ai 官方（8/19 GLM-5.3 API 上线·743B·AA Index 60·Terminal-Bench 3.0 28.3·DeepSWE v1.1 66.9·Agents’ Last Exam 28.5·CyberGym 84.5%·定价同 GLM-5.2·权重 8/28 开源）、腾讯云 GLM-5.3 报价（输入8/输出28/缓存2 元每百万）、Hugging Face《开源模型现状：2026 夏季观察》（中国开源规模 7540 亿–2.78 万亿领先美国、部分美国模型以中国模型为底座）、Qwen3.8-27B 登顶 HF 趋势榜（2 天下载破百万、衍生 15 万+）、DeepSeek Harness（DSH 三天 13 万+ Star）、NVIDIA 官方 GLM-5.2 基准卡与 build.nvidia.com（125 模型、77 永久免费）、OpenCode Zen 官方文档（Base URL https://opencode.ai/zen/v1）、OpenRouter 官方定价页（免费层 50 / 1000 次每天）、火山引擎方舟（每日 200 万 Token 免费含 V4 Pro）、Nous Portal（Step-3.7-Flash / Nemotron-3-Ultra / Owl-Alpha 3 款免费）、Google AI Studio 与 Groq 官方限额页、阿里千问与 ModelScope 开源公告、Artificial Analysis</p>
    <p style="margin-top:8px;">⚠️ 免费额度可能随时间调整，请以各平台官网最新政策为准 | 评分数据来自 freellm.net 实时实测，不同供应商托管同一模型分数不同，已分别标注平台 | 本期主线：智谱 GLM-5.3 API 8/19 上线（743B·AA Index 60 并列开源第一·付费 API 但权重 8/28 开源进 NIM 免费层）+ 中国开源 AI 成美国大模型「底座」（Qwen3.8-27B 登顶 HF 趋势榜、两天下载破百万、衍生 15 万+）+ DeepSeek Harness 三天 13 万 Star + freellm.net 442+ 免费模型 + 免费先进榜稳定（Kimi K3 98 蝉联第一）</p>
    <p style="margin-top:8px;">⭐ <a href="https://github.com/lph12168x/Free-LLM-Daily" target="_blank">lph12168x/Free-LLM-Daily</a> · 🤖 由 WorkBuddy 自动化生成</p>
  </div>'''

html19 = build(tpl, "2026-08-19", "2026 年 8 月 19 日 · 周三", "2026-08-19",
               META19, NAV19, TAGLINE19, "442+",
               "免费大模型（freellm.net 实测 · 329 在线）",
               FOCUS19, HOT19, FOOTER19)
with open(dst19, "w", encoding="utf-8") as f:
    f.write(html19)

# ---- Validation ----
for tag, html in [("0818", html18), ("0819", html19)]:
    oc = html.count("<div"); cc = html.count("</div>")
    mojibake = html.count(chr(0xFFFD))
    print(f"[{tag}] open={oc} close={cc} balanced={oc==cc} mojibake={mojibake}")
    for m in ["2026-08-19", "GLM-5.3", "Qwen3.8-27B", "page-nav", "class=\"footer\""]:
        print(f"  contains '{m}': {m in html}")
