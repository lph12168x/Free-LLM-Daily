# -*- coding: utf-8 -*-
"""为 2026-08-03 日报补充「蚂蚁百灵 Ling-3.0-flash 今晚 23:00 限免截止」内容"""
import io, sys, os

P = r"C:\Users\liuph216\WorkBuddy\automation-2026-06-08-11-21-56\daily-free-llm-2026-08-03.html"

with io.open(P, "r", encoding="utf-8") as f:
    html = f.read()

edits = []


def rep(old, new, label):
    global html
    n = html.count(old)
    if n != 1:
        edits.append((label, "FAIL count=%d" % n))
        return
    html = html.replace(old, new, 1)
    edits.append((label, "OK"))


# ---------- 1) 焦点段：新增「今日必须今天做的一件事」+ 倒计时 ----------
old_cd = '      倒计时：<span class="countdown">8/5 腾讯 Hy3 限免截止（仅剩 2 天）</span> · 9/30 腾讯混元旧平台停服'
new_cd = (
    '      <b>今日必须今天做的一件事</b>：<span class="hl" style="color:var(--accent-4);font-weight:800;">'
    '蚂蚁百灵 Ling-3.0-flash 的限时免费 API 今晚 23:00（北京时间）准点关闭</span>。'
    '这颗 7/24 发布的模型总参 124B、单 Token 仅激活 5.1B，却在 34 个评测维度拿下 15 个第一、19 个第二，'
    '<b>综合均分与 DeepSeek-V4-Flash 并列第一</b>，领先自家万亿旗舰 Ring-2.6-1T（59.7 分）近 8 分，'
    'SWE-Bench Pro 56.6% 为参测模型第一；原生 256K 上下文、最高可扩至 1M，支持思考 / 非思考双模式。'
    '发布 5 天内它在 OpenRouter 的 Token 调用量就从第 9 冲到第 6，7/29 单日调用量仅比 DeepSeek V4-Pro 低 0.5%——'
    '这是本周被低估得最厉害的一档免费额度。<b>免费期结束后官方将正式开源权重</b>，'
    '所以今天该做两件事：白天把要跑的评测 / 对比一次性跑完，之后转为等权重开源本地部署。<br><br>\n'
    '      倒计时：<span class="countdown">今晚 23:00 蚂蚁百灵 Ling-3.0-flash 限免截止（今日最后窗口）</span>'
    ' · <span class="countdown">8/5 腾讯 Hy3 限免截止（仅剩 2 天）</span> · 9/30 腾讯混元旧平台停服'
)
rep(old_cd, new_cd, "焦点段+倒计时")

# ---------- 2) Top10 区：在 Hy3 场外卡之前插入 Ling-3.0-flash 卡 ----------
anchor_hy3 = (
    '      <div class="model-card">\n'
    '        <div class="rank-badge rank-other">场外 · 限免</div>'
)
ling_card = (
    '      <div class="model-card">\n'
    '        <div class="rank-badge rank-other">⏰ 场外 · 今晚 23:00 截止</div>\n'
    '        <div class="model-head">\n'
    '          <div class="score"><div class="num">⏰</div><div class="unit">今日最后</div></div>\n'
    '          <div>\n'
    '            <div class="model-name">Ling-3.0-flash</div>\n'
    '            <div class="model-provider">蚂蚁百灵 · OpenRouter</div>\n'
    '          </div>\n'
    '        </div>\n'
    '        <div class="model-meta">\n'
    '          <span class="meta-pill">124B / 5.1B 激活</span>\n'
    '          <span class="meta-pill">256K 可扩 1M</span>\n'
    '          <span class="meta-pill">限免至今晚 23:00</span>\n'
    '          <span class="meta-pill">之后开源权重</span>\n'
    '        </div>\n'
    '        <div class="model-desc">⏰ <span class="hl" style="color:var(--accent-4);font-weight:800;">'
    '限时免费今晚 23:00（北京时间）截止，是今天最紧急的一个窗口</span>：蚂蚁集团百灵大模型 7/24 发布的原生混合推理模型，'
    '总参 124B、单 Token 激活仅 5.1B（分别为上一代万亿旗舰 Ring-2.6-1T 的 12.4% 和 8.1%），'
    '采用 5:1 交替堆叠 KDA 与 MLA 的原生混合线性注意力 + 1/64 稀疏 MoE。'
    '<b>34 个评测维度拿下 15 个第一、19 个第二，综合均分与 DeepSeek-V4-Flash 并列第一</b>，'
    '12 项基准中 11 项优于 Ring-2.6-1T；<b>SWE-Bench Pro 56.6% 位居参测模型第一</b>；'
    '智能密度 0.5、智效比 13.2 双双登顶。接入 SGLang HiCache + Mooncake 分级缓存后，长输入首 Token 时间降低 60%–80%。'
    '发布 5 天内 OpenRouter Token 调用量从第 9 升至第 6。<b>免费期结束后官方将正式开源权重</b>，'
    '届时零成本路径转为自部署。⚠️ 今晚 23:00 后 OpenRouter 与百灵官方平台的免费调用同时关闭。</div>\n'
    '        <a class="model-link" href="https://openrouter.ai/models?q=ling-3.0-flash" target="_blank">'
    '前往 OpenRouter 抢用最后几小时 →</a>\n'
    '      </div>\n'
    '\n'
)
rep(anchor_hy3, ling_card + anchor_hy3, "Ling 模型卡")

# ---------- 3) 标签行 ----------
rep(
    '<span class="tag">MiniMax H3(待开源)</span>',
    '<span class="tag">Ling-3.0-flash(今晚23:00截止)</span><span class="tag">MiniMax H3(待开源)</span>',
    "标签行",
)

# ---------- 4) 风险提醒：置顶新增 ----------
anchor_risk = (
    '    <div class="risk-list">\n'
    '      <div class="risk-item">\n'
    '        <span class="icon">🦙</span>'
)
ling_risk = (
    '    <div class="risk-list">\n'
    '      <div class="risk-item">\n'
    '        <span class="icon">⏰</span>\n'
    '        <div>\n'
    '          <h4>【今晚 23:00 死线】蚂蚁百灵 Ling-3.0-flash 限时免费 API 今天到点关闭 — 今日最紧急的一个窗口</h4>\n'
    '          <p>官方口径明确：<b>OpenRouter 与百灵官方平台的 Ling-3.0-flash 免费调用，免费期截至 2026 年 8 月 3 日 23:00（北京时间）</b>，'
    '也就是今晚。这不是「大概率会延长」的那类活动——官方同时说明<b>免费期结束后即正式开源权重</b>，'
    '说明这是一次有明确交接安排的限时开放。它的实力不该被忽略：124B 总参 / 5.1B 激活，'
    '34 个评测维度 15 个第一、19 个第二，综合均分与 DeepSeek-V4-Flash 并列第一，SWE-Bench Pro 56.6% 参测第一，'
    '原生 256K 上下文可扩至 1M。<b>今天要做的：</b>① 把想跑的评测、对比、Agent 流程在 23:00 前一次性跑完并存好结果；'
    '② 不要把线上服务临时切到它上面——今晚断供后会直接失败；③ 之后关注权重开源，转为本地或第三方托管部署。</p>\n'
    '        </div>\n'
    '      </div>\n'
    '      <div class="risk-item">\n'
    '        <span class="icon">🦙</span>'
)
rep(anchor_risk, ling_risk, "风险提醒置顶项")

# ---------- 5) 页脚数据源 ----------
rep(
    '、TII Falcon H1R 7B、',
    '、TII Falcon H1R 7B、蚂蚁百灵官方发布与 OpenRouter 模型页（Ling-3.0-flash 124B/5.1B、限时免费至 8/3 23:00、期满开源权重）、',
    "页脚数据源",
)

# ---------- 6) 顶部 tagline 补一句 ----------
rep(
    '并经 Ollama 官方定价页、',
    '并经蚂蚁百灵官方发布、Ollama 官方定价页、',
    "tagline 数据源",
)

with io.open(P, "w", encoding="utf-8") as f:
    f.write(html)

for k, v in edits:
    print("%-20s %s" % (k, v))
print("FFFD count:", html.count("\ufffd"))
