#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate daily-free-llm-2026-08-13.html by adapting the 8/12 template.
Stable sections (Top10, platforms, combos, risks, CSS) are kept verbatim.
Only date-specific hero/focus/hot-cards/footer are refreshed.
"""
import os, re

base = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(base, "daily-free-llm-2026-08-12.html")
dst = os.path.join(base, "daily-free-llm-2026-08-13.html")

with open(src, encoding="utf-8") as f:
    html = f.read()

# ---- 1. Title ----
html = html.replace(
    "<title>免费大模型日报 · 2026-08-12 · Free LLM Daily</title>",
    "<title>免费大模型日报 · 2026-08-13 · Free LLM Daily</title>",
    1,
)

# ---- 2. Meta description ----
NEW_META = ('<meta name="description" content="2026年8月13日免费大模型日报：聚焦量大能用的先进模型。'
    "🔥 本期主线——阿里千问 Qwen3.8-2.4T-A95B 开源权重正式落地（8/12 深夜上线 HuggingFace + ModelScope，千问首次开放 Max 级旗舰权重；自定义 Qwen3.8-Max License 非 Apache 2.0，大规模商用需授权；文本-only + 强制思考；2.4T/95B、262K→1M 上下文；27B 仍未放出）；"
    "DeepSeek V4 Pro 正式版（DeepSeek-V4-Pro-0813）8/13 凌晨上线 API，Agent 能力大增（Responses API + Codex），定价 3/6 元每百万（缓存命中 0.025），较 Flash 明显涨价——8/6 预告的涨价落地；"
    "免费先进榜格局稳定（Kimi K3 98 蝉联第一）。\">")
html = re.sub(r'<meta name="description" content="[^"]*" ?>', NEW_META, html, count=1)

# ---- 3. Date chip ----
html = html.replace(
    '<div class="date-chip">📅 2026 年 8 月 12 日 · 周三</div>',
    '<div class="date-chip">📅 2026 年 8 月 13 日 · 周四</div>',
    1,
)

# ---- 4. Stats number (freellm.net grew to 431+; refresh for consistency) ----
html = html.replace(
    '<div class="stat-num">378+</div>',
    '<div class="stat-num">431+</div>',
    1,
)

# ---- 5. Section title date stamp ----
html = html.replace(
    "量大能用的先进模型 · Top 10（freellm.net 8/12 刷新实测）",
    "量大能用的先进模型 · Top 10（freellm.net 8/13 刷新实测）",
    1,
)

# ---- 6. Tagline ----
NEW_TAGLINE = ('<p class="tagline">聚焦「量大能用的先进模型」· 覆盖 30+ 国内外平台 · 本期主线：'
    '<b>阿里千问 Qwen3.8-2.4T-A95B 开源权重正式落地（8/12 深夜上线 HuggingFace + ModelScope，千问首次开放 Max 级旗舰权重；自定义 Qwen3.8-Max License 非 Apache 2.0，大规模商用需授权；文本-only + 强制思考；2.4T/95B、262K→1M 上下文；27B 仍未放出）</b>；'
    '<b>DeepSeek V4 Pro 正式版（DeepSeek-V4-Pro-0813）8/13 凌晨上线 API，Agent 能力大增（Responses API + Codex），定价 3/6 元每百万、较 Flash 明显涨价——8/6 预告的涨价落地</b>；'
    '<b>免费先进榜格局稳定（Kimi K3 98 蝉联第一）</b>。</p>')
html = re.sub(r'<p class="tagline">.*?</p>', NEW_TAGLINE, html, count=1, flags=re.S)

# ---- 7. Focus banner ----
NEW_FOCUS = '''  <div class="focus">
    <h2>📌 本期焦点：Qwen3.8-2.4T-A95B 开源权重正式落地（8/12 深夜上线 HF + ModelScope，千问首次开放 Max 级旗舰权重，自定义 Qwen3.8-Max License 非 Apache 2.0）· DeepSeek V4 Pro 正式版（0813）8/13 上线 API、Agent 大增但明显涨价（3/6 元每百万）· 免费先进榜稳定（Kimi K3 98 蝉联第一）</h2>
    <p>
      <b>今日主线（对「量大能用」最有引爆力）</b>：8 月 12 日深夜，阿里千问正式开放 <b>Qwen3.8-2.4T-A95B</b> 模型权重，上线 HuggingFace 与 ModelScope——这是<b>千问首次开放 Max 级旗舰权重</b>（2.4T 总参 / 95B 激活 / 512 专家 MoE / 多步 MTP）。与云端 API（qwen3.8-max：多模态、默认 1M、内置工具、$2/$6）不同，开源权重是<b>文本-only、强制思考、262K 原生可扩至 1M</b>，走自定义 Qwen3.8-Max License（非 Apache 2.0）。<br><br>
      <b>许可证要点（商用前必读）</b>：自定义 Qwen3.8-Max License——① 保留版权与许可声明；② 若商业产品 &gt;1 亿 MAU 或月营收 &gt;2000 万美元，需在 UI 显著标注模型名；③ 若 MaaS / AI 工作助手类业务滚动 12 个月营收 &gt;5000 万美元，需向 Qwen 另行取得授权；④ 内部使用（不对外暴露模型/输出/能力）有豁免。Reuters 此前报道阿里将对大型商业用户设额外收费/授权——<span class="hl">「开放权重」≠「可免费商用」</span>。<br><br>
      <b>你能跑吗</b>：全精度约 4.9TB；Unsloth AI 动态 1-bit 分层量化压到 <b>397GB（减 91%）</b>，Unsloth-Desktop 需设备内存+显存 ≥410GB 本地运行；<b>27B 仍未放出</b>，蹲守中。SGLang / vLLM / TokenSpeed / Transformers 均可部署。<br><br>
      <b>DeepSeek 侧（同日另一件大事）</b>：8/13 凌晨 V4 Pro 从预览转正，版本号 <b>DeepSeek-V4-Pro-0813</b>，调用名不变，Agent 能力大增（支持 Responses API 与 Codex 接入），Terminal-Bench 2.1 达 <b>87.9</b> 逼近 Fable 5 的 88.0，CyberGym / AutomationBench 反超；定价 <b>3/6 元每百万（缓存命中 0.025）</b>，较 V4-Flash（1/2 元）明显涨价——这是 8/6 预告的涨价正式落地。提醒：免费先进榜里的 <b>DeepSeek V4-Flash</b> 仍是性价比之选，V4-Pro 已非「免费」定位。<br><br>
      <b>冷静三点</b>：① Qwen3.8-Max 基准（Terminal-Bench 2.1 86.6、PaperBench 93.0、OSWorld-Verified 86.1）多项超 Fable 5 / GPT-5.6 Sol，但 SWE-bench Pro 67.7 仍落后 Fable 5 的 80.0、Claude Opus 4.8 的 69.2；② 当前 API 仍付费（$2/$6），<b>暂无 :free 层</b>；③ 自部署要自备 GPU——<b>当下开箱即用的先进免费 API 仍是 K3 / GLM-5.2 / Gemini 3.6 Flash / DeepSeek V4-Flash / Hy3</b>（见下方 Top10）。<br><br>
      倒计时：<span class="countdown">8/31 腾讯 Hy3 限免截止（还有 18 天）</span> · 8/12 已发生：Qwen3.8-Max 开源权重落地 · 8/13 已发生：DeepSeek V4 Pro 正式版 API · 近期：Qwen3.8-27B 在路上、智谱 GLM-5.3 万亿参数「发布在即」· 远期：9/30 腾讯混元旧平台停服、10/21 GCP 16 端点退役、12/31 腾讯云 TokenHub 与移动云 MoMA 新人活动结束。
    </p>
  </div>'''
html = re.sub(r'<div class="focus">.*?</div>\n\n  <!-- Hot featured 1', NEW_FOCUS + '\n\n  <!-- Hot featured 1', html, count=1, flags=re.S)

# ---- 8. Hot card 1 + Hot card 2 ----
NEW_HOT1 = '''  <!-- Hot featured 1: Qwen3.8-2.4T-A95B open weights landed -->
  <div class="hot">
    <span class="flag">🔥 正式落地 · 8/12 深夜阿里千问开放 Qwen3.8-2.4T-A95B 权重（HuggingFace + ModelScope）——千问首次开放 Max 级旗舰权重，自定义许可证非 Apache 2.0</span>
    <h2>2.4 万亿参数 + 95B 激活 + 自定义 License：千问 Max 级旗舰首次可下载，但「开放权重」≠「可免费商用」，文本-only + 强制思考</h2>
    <div class="sub">阿里 8/12 深夜开源 · HF + ModelScope 已上线 · 2.4T / 激活 95B / 512 专家 MoE · 262K→1M 上下文 · 文本-only + 强制思考 · 自定义 Qwen3.8-Max License</div>
    <p>
      <b>① 发生了什么</b>：8 月 12 日深夜，阿里「魔搭 ModelScope 社区」宣布正式开放 <b>Qwen3.8-2.4T-A95B</b> 模型权重，同步上线 HuggingFace（huggingface.co/Qwen/Qwen3.8-2.4T-A95B）与 ModelScope（modelscope.cn/models/Qwen/Qwen3.8-2.4T-A95B）。这是千问 <b>Max 级旗舰首次开源权重</b>：2.4T 总参、每 token 激活 95B、512 专家（每 token 选 10 路由 + 1 共享）、多步 MTP。<br><br>
      <b>② 开源版 ≠ 云端版</b>：云端 qwen3.8-max 仍多模态（图/视频）、默认 1M、可关思考、内置工具、$2/$6；开源权重是<b>文本-only、262K 原生（可扩 1M）、强制思考不可关</b>、走自定义 License——两者同源不同交付。<br><br>
      <b>③ 许可证是关键（商用前必读）</b>：自定义 <b>Qwen3.8-Max License</b> 非 Apache/MIT：保留版权声明；商业产品 &gt;1 亿 MAU 或月营收 &gt;2000 万美元需在 UI 显著标注模型名；MaaS / AI 工作助手类业务滚动 12 个月营收 &gt;5000 万美元需向 Qwen 另行取得授权；内部使用（不对外暴露）有豁免。Reuters 此前报道阿里将对大型商业用户设额外收费——<span class="hl">「开放权重」≠「可免费商用」</span>。<br><br>
      <b>④ 你能跑吗</b>：全精度约 4.9TB；Unsloth AI 动态 1-bit 分层量化压到 <b>397GB（减 91%）</b>，Unsloth-Desktop 需设备内存+显存 ≥410GB 本地运行；<b>27B 仍未放出</b>，蹲守中。SGLang / vLLM / TokenSpeed / Transformers 可部署。<br><br>
      <b>⑤ 基准与冷静</b>：Terminal-Bench 2.1 86.6（逼近 Fable 5 的 88.0）、PaperBench 93.0、OSWorld-Verified 86.1、参数化 CAD 91.5 多项超 Fable 5；但 SWE-bench Pro 67.7 仍落后 Fable 5 的 80.0、Claude Opus 4.8 的 69.2。策略：自部署要自备 GPU；当下开箱即用的先进免费 API 仍是 GLM-5.2（94 分·NIM 永久免费）。
    </p>
    <div class="hot-grid">
      <div class="hot-item"><div class="k">开源时间</div><div class="v">8/12 深夜</div></div>
      <div class="hot-item"><div class="k">总参/激活</div><div class="v">2.4T / 95B</div></div>
      <div class="hot-item"><div class="k">上下文</div><div class="v">262K→1M</div></div>
      <div class="hot-item"><div class="k">模态/思考</div><div class="v">文本-only·强制思考</div></div>
      <div class="hot-item"><div class="k">许可证</div><div class="v">自定义(非Apache)</div></div>
      <div class="hot-item"><div class="k">最大风险</div><div class="v">商用需授权</div></div>
    </div>
    <a class="hot-link" href="https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B" target="_blank">查看 HuggingFace 模型主页 →</a>
  </div>'''

NEW_HOT2 = '''  <!-- Hot featured 2: DeepSeek V4 Pro GA with price hike -->
  <div class="hot">
    <span class="flag">💰 8/13 上线 · DeepSeek V4 Pro 正式版（DeepSeek-V4-Pro-0813）从预览转正，Agent 能力大增（Responses API + Codex），定价 3/6 元每百万——8/6 预告的涨价正式落地</span>
    <h2>DeepSeek V4 Pro 正式版 API 8/13 上线：Terminal-Bench 87.9 逼近 Fable 5，Agent 能力大增，但定价较 Flash 明显上涨（3/6 元每百万）</h2>
    <div class="sub">DeepSeek 8/13 凌晨转正 · 版本号 DeepSeek-V4-Pro-0813 · 调用名不变 · 支持 Responses API + Codex · 输入(缓存命中)0.025/未命中3/输出6 元每百万</div>
    <p>
      <b>① 发生了什么</b>：8 月 13 日凌晨，DeepSeek 开放平台将 V4 Pro 从预览版正式转正，版本号更新为 <b>DeepSeek-V4-Pro-0813</b>，API 调用模型名不变。新版本大幅增强 Agent 能力，支持 <b>Responses API 与 Codex 接入</b>。<br><br>
      <b>② 定价（涨价的落地）</b>：每 1M token——输入缓存命中 <b>0.025 元</b>、缓存未命中 <b>3 元</b>、输出 <b>6 元</b>。对比 V4-Flash（0.02/1/2 元），V4-Pro 贵了约 3 倍。这正是 8/6 公告「计划大幅上调 API 定价」的兑现——提醒：<span class="hl">免费先进榜里的 DeepSeek V4-Flash 仍是性价比之选，V4-Pro 已非「免费」定位</span>。<br><br>
      <b>③ 性能</b>：Terminal-Bench 2.1 <b>87.9</b>，逼近 Fable 5 的 88.0；在 AI 安全智能体 CyberGym 与高难 Agent AutomationBench 上甚至<b>反超 Fable 5</b>；较预览版能力提升显著。<br><br>
      <b>④ 对「免费可用」的含义</b>：DeepSeek 的免费入口仍是 <b>V4-Flash</b>（OpenRouter 免费层 / Ollama / NIM 等），V4-Pro 走付费 API。请分清「免费 Flash」与「付费 Pro」——别把 Pro 的强能力误当成可白嫖。<br><br>
      <b>⑤ 策略</b>：重度 Agent / 长链路任务可上 V4-Pro（逼近 Fable 5 的 Agent 表现）；日常白嫖继续用 V4-Flash。⚠️ 注意 DeepSeek 8/6 起的峰谷定价与涨价趋势，长期成本需评估。
    </p>
    <div class="hot-grid">
      <div class="hot-item"><div class="k">版本</div><div class="v">V4-Pro-0813</div></div>
      <div class="hot-item"><div class="k">上线</div><div class="v">8/13 凌晨</div></div>
      <div class="hot-item"><div class="k">Agent</div><div class="v">Responses API+Codex</div></div>
      <div class="hot-item"><div class="k">定价</div><div class="v">3/6 元每百万</div></div>
      <div class="hot-item"><div class="k">Terminal-Bench</div><div class="v">87.9(逼Fable5 88.0)</div></div>
      <div class="hot-item"><div class="k">定位</div><div class="v">付费Pro(非免费)</div></div>
    </div>
    <a class="hot-link" href="https://platform.deepseek.com" target="_blank">前往 DeepSeek 开放平台 →</a>
  </div>'''

html = re.sub(
    r'  <!-- Hot featured 1:.*?\n  <!-- Top advanced free models -->',
    NEW_HOT1 + "\n" + NEW_HOT2 + "\n\n  <!-- Top advanced free models -->",
    html, count=1, flags=re.S,
)

# ---- 9. Footer ----
NEW_FOOTER = '''  <div class="footer">
    <p>📅 下次更新：明日 09:30 · 数据来源：freellm.net 实时实测目录（431+ 免费模型、30 家供应商、251 款经实时 API 验证、最新刷新 2026-8-12；本期读数 Kimi K3 98（Ollama Cloud）/ GLM-5.2 94（NVIDIA NIM）/ Gemini 3.6 Flash 91（AI Studio）/ DeepSeek V4-Flash 91（OpenRouter 免费层）·89（Ollama）·88（NIM）/ MiniMax M3 90（OpenRouter）·88（Ollama）·87（NIM）/ Tencent Hy3 90（OpenRouter，WorkBuddy/CodeBuddy 限免至 8/31）/ Gemini 3.5 Flash 87 / Ling-3.0-flash 87（OpenRouter）·85（Kilo Code）/ DeepSeek V4-Pro 84（Ollama）·85（OpenRouter/NVIDIA）/ Nemotron 3 Ultra 85（NVIDIA）/ Kimi K2.6 83（NVIDIA））、阿里通义千问官方与魔搭 ModelScope 8/12 深夜（Qwen3.8-2.4T-A95B 开源权重落地 HF+ModelScope·千问首次开放 Max 级旗舰权重·2.4T/95B/512专家 MoE/262K→1M·文本-only+强制思考·自定义 Qwen3.8-Max License 非 Apache 2.0·全精度 4.9TB、Unsloth 量化压至 397GB·27B 仍未放出）、llm-stats.com 8/12 研究（Qwen3.8-Max License 商用阈值：>1 亿 MAU 或 >2000 万美元月营收需标注、MaaS/>5000 万美元 TTM 需授权、内部使用豁免；$2/$6 API·2M TPM/15K RPM；Terminal-Bench 2.1 86.6、SWE-bench Pro 67.7、PaperBench 93.0）、36氪/IT之家/网易 8/13（Qwen3.8-Max 开源·性能比肩 Fable 5·OSWorld-Verified 86.1 第一·参数化 CAD 91.5 超 Fable 5）、DeepSeek 开放平台 8/13 凌晨（V4 Pro 正式版 DeepSeek-V4-Pro-0813 上线 API·Responses API+Codex·3/6 元每百万·缓存命中 0.025·Terminal-Bench 87.9 逼 Fable 5 88.0·CyberGym/AutomationBench 反超）、科创板日报/财联社/新浪 8/13、Reuters（阿里对大型商业用户设 Qwen3.8-Max 额外收费/授权）、腾讯 2026 Q2 财报（Hy3 上线一周调用量较上代增 68 倍·Hy4 计划近期发布）、智谱官方（GLM-5.3 发布在即·万亿参数）、NVIDIA 官方 GLM-5.2 基准卡与 build.nvidia.com（141 模型 77 永久免费）、OpenRouter 官方定价页（免费层 200 次/天账户级、充 $10 升 1000 次/天）、腾讯云 TokenHub、中国移动云 MoMA、国家超算互联网 SCNet、阿里云百炼、美团 LongCat、火山引擎、硅基流动、魔搭 ModelScope</p>
    <p style="margin-top:8px;">⚠️ 免费额度可能随时间调整，请以各平台官网最新政策为准 | 评分数据来自 freellm.net 实时实测，不同供应商托管同一模型分数不同，已分别标注平台 | 本期主线：Qwen3.8-2.4T-A95B 开源权重正式落地（千问首次开放 Max 级旗舰权重·自定义 License 非 Apache 2.0·文本-only+强制思考·27B 仍未放出）+ DeepSeek V4 Pro 正式版（0813）上线 API、Agent 大增但 3/6 元每百万明显涨价（8/6 预告落地）+ 免费先进榜稳定（Kimi K3 98 蝉联第一）</p>
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
for marker in ["2026-08-13", "Qwen3.8-2.4T-A95B", "DeepSeek-V4-Pro-0813", "page-nav"]:
    print(f"  contains '{marker}': {marker in html}")
