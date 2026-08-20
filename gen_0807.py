#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate daily-free-llm-2026-08-07.html from 8/6 template with targeted replacements."""
import io, os, re, sys

base = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(base, "daily-free-llm-2026-08-06.html")
DST = os.path.join(base, "daily-free-llm-2026-08-07.html")

with io.open(SRC, encoding="utf-8") as f:
    html = f.read()

def rep(old, new):
    global html
    n = html.count(old)
    if n != 1:
        raise SystemExit(f"[FAIL] expected 1 occurrence, found {n} for:\n{old[:160]}")
    html = html.replace(old, new, 1)

def rep_re(pattern, repl):
    global html
    new, n = re.subn(pattern, repl, html, count=1)
    if n != 1:
        raise SystemExit(f"[FAIL] regex expected 1 occurrence, found {n} for:\n{pattern[:160]}")
    html = new

# R1 title
rep_re(r'<title>[^<]*</title>',
       '<title>免费大模型日报 · 2026-08-07 · Free LLM Daily</title>')

# R2 meta description
rep_re(r'<meta name="description" content="[^"]*">',
       '<meta name="description" content="2026年8月7日免费大模型日报：聚焦量大能用的先进模型。🔥 今日双响炮——智谱 GLM-5.3 官宣「发布在即」（万亿参数·史诗级 plus·业内推算有望追平 Kimi K3），Qwen3.8-Max 2.4T 权重 8/10 当周开源倒计时；叠加中国开源模型累计下载破 100 亿次（HuggingFace 占比 41% 首超美国）的生态里程碑。同期限免续命的腾讯 Hy3 仍可免费用到 8/31；AirLLM 让 4GB 显卡跑 2.8T 的 Kimi K3。">')

# R3 date-chip
rep_re(r'<div class="date-chip">[^<]*</div>',
       '<div class="date-chip">📅 2026 年 8 月 7 日 · 周五</div>')

# R4 tagline
NEW_TAGLINE = ('<p class="tagline">聚焦「量大能用的先进模型」· 覆盖 30+ 国内外平台 · 本期主线：'
               '<b>国产开源「双响炮」——智谱 GLM-5.3 官宣「发布在即」（万亿参数·史诗级 plus·有望追平 Kimi K3）、'
               'Qwen3.8-Max 2.4T 权重 8/10 当周开源倒计时</b>；叠加<b>中国开源模型累计下载破 100 亿次'
               '（HF 占比 41% 首超美国）</b>的生态里程碑；评分数据来自 freellm.net 实时实测'
               '（首页 424+ 免费模型、30 家供应商、248 款经实时 API 验证、284+ 无需信用卡，8/6 刷新），'
               '并经智谱官方 8/7 确认、唐杰社交平台回应、阿里通义千问官方发布、Hugging Face 2026 春季报告、'
               '工信部数据、央视财经报道、Ollama 官方文档、NVIDIA 官方基准卡、OpenRouter 官方定价页、'
               '腾讯云 TokenHub、中国移动云帮助中心、国家超算互联网 SCNet、智谱 ZCode 泄露页面、'
               'AirLLM 开源仓库多源交叉验证</p>')
rep_re(r'<p class="tagline">[\s\S]*?</p>', NEW_TAGLINE)

# R5 Focus banner (regex block replace)
NEW_FOCUS = '''  <div class="focus">
    <h2>📌 本期焦点：国产开源「双响炮」——智谱 GLM-5.3 官宣「发布在即」（万亿参数·史诗级 plus）、Qwen3.8-Max 2.4T 权重 8/10 当周开源；叠加中国开源模型累计下载破 100 亿次（HF 占比 41% 首超美国）</h2>
    <p>
      <b>今日头号（对「量大能用」最有引爆力）</b>：8 月 7 日，智谱创始人唐杰在社交平台回应确认 <span class="hl">GLM-5.3「发布在即」</span>——虽未给具体日期，但时间节点已临近。关键信息：参数从 GLM-5.2 的 7400 亿级<b>跃升至万亿以上</b>，官方将此次升级定义为「<b>史诗级 plus</b>」，业内按 artificialanalysis（GLM-5.2 得 52 分）推算若综合提升约 5 分，<b>有望追平 Kimi K3</b>、冲击 60 分大关。命名曾传 GLM-5.5，最终落定 GLM-5.3。这是国产先进模型继 Kimi K3、DeepSeek V4-Flash 之后又一枚「量大能用」的重磅棋子。<br><br>
      <b>第二响：Qwen3.8-Max 开源倒计时</b>：阿里 8/3 发布的 <span class="hl">Qwen3.8-Max（2.4T / 95B 激活 / 1M 上下文）计划 8/10 当周开源完整权重</span>，同步开源 Qwen3.8-27B——这是 Qwen-Max 级旗舰首次开源。对免费用户而言，<b>27B 版本才是个人机器真正跑得动的那一个</b>，值得提前把本地部署环境备好。<br><br>
      <b>第三重背景：中国开源模型累计下载破 100 亿次</b>：工信部披露我国开源大模型全球累计下载量<b>突破 100 亿次</b>；Hugging Face 2026 春季报告显示<b>中国研发开源模型占平台下载量 41%，超越美国居全球第一</b>（全球每 10 次开源下载约 4 次指向中国模型）。Kimi K3（2.8T）7/27 发布一小时登顶 HF 趋势榜、Qwen 系列累计超 10 亿次居国产榜首。⚠️ 但请始终记住：<b>下载量高 ≠ 你能免费调</b>——权重开源、工具链开源、免费 API 是三件不同的事。<br><br>
      倒计时：<span class="countdown">8/31 腾讯 Hy3 限免截止（还有 24 天）</span> · 本周待兑现：Qwen3.8-Max 权重开源（8/10 当周） · 已发生：8/7 GLM-5.3 官宣在即、8/4 DeepSeek V4-Flash 容量崩溃（已恢复）、8/3 Ling-3.0-flash 限免关闭并开源、MiniMax H3 权重开源 · 远期：9/30 腾讯混元旧平台停服、10/21 Google Cloud 16 个开源模型端点退役、12/31 腾讯云 TokenHub 与移动云 MoMA 新人活动结束。
    </p>
  </div>'''
rep_re(r'  <div class="focus">[\s\S]*?\n  </div>\n', NEW_FOCUS)

# R6 Hot card (regex block replace)
NEW_HOT = '''  <div class="hot">
    <span class="flag">🔥 今日重磅 · 智谱 GLM-5.3 官宣「发布在即」：万亿参数 + 史诗级 plus，国产先进模型再添一员大将</span>
    <h2>从 7400 亿到万亿参数，唐杰 8/7 确认 GLM-5.3 临近发布——业内推算有望追平 Kimi K3</h2>
    <div class="sub">智谱创始人唐杰社交平台回应（8/7）· 参数 7400 亿 → 万亿以上 · 官方定义「史诗级 plus」· artificialanalysis GLM-5.2 52 分 · 命名落定 GLM-5.3（曾传 5.5）</div>
    <p>
      <b>① 发生了什么</b>：8 月 7 日，智谱 AI 创始人<b>唐杰在社交平台回应网友，明确确认 GLM-5.3「发布在即」</b>，虽未给出精确日期，但时间节点已临近。此前 8/3 GLM-5.3 曾短暂出现在 GitHub 与智谱官网，随即被下架——侧面证实核心研发与内部验证已完成，只待敲定正式发布窗口。<br><br>
      <b>② 升级幅度有多大</b>：GLM-5.2（6/13 发布）是智谱迄今最强开源模型、国内首个编程能力比肩美国前沿者，在 artificialanalysis 得 <b>52 分</b>（略高于 DeepSeek V4-Flash、低于 Kimi K3）。GLM-5.3 参数从 7400 亿级<b>跃升至万亿以上</b>，官方将升级形容为「<span class="hl">史诗级 plus</span>」。业内按此推算：若综合提升约 5 分，则<b>有望追平 Kimi K3</b>；若提升更大，可狙击 GPT-5.6 / Opus 5。冲击 60 分大关具备现实基础。<br><br>
      <b>③ 对免费用户的真正价值（也是本期主线）</b>：GLM-5.3 尚未公布模型卡、价格、API 与权重，<span class="hl">「能免费调」要等正式发布</span>。但 8/3 泄露的「首发权益」写明<b>新用户 300 万 Token/天 + GLM-5-turbo 200 万/天、订阅用户「闲时任务免费执行」</b>——这是泄露口径、非官方承诺，若正式版延续，它将是下一波<b>量大能用的免费先进模型</b>。策略：先把它加入「待发布观察」，正式发布后第一时间蹲守免费额度；当下能立即白嫖的旗舰仍是 GLM-5.2（95 分·NVIDIA NIM 永久免费）。
    </p>
    <div class="hot-grid">
      <div class="hot-item"><div class="k">确认时间</div><div class="v">8/7 唐杰回应</div></div>
      <div class="hot-item"><div class="k">参数跃升</div><div class="v">7400亿 → 万亿+</div></div>
      <div class="hot-item"><div class="k">官方定义</div><div class="v">史诗级 plus</div></div>
      <div class="hot-item"><div class="k">对标推算</div><div class="v">有望追平 K3</div></div>
      <div class="hot-item"><div class="k">当前状态</div><div class="v">未发布·无 API</div></div>
      <div class="hot-item"><div class="k">泄露免费额度</div><div class="v">300万/天(待定)</div></div>
    </div>
    <a class="hot-link" href="https://www.zhipuai.cn" target="_blank">查看智谱官网 →</a>
  </div>'''
rep_re(r'  <div class="hot">[\s\S]*?\n  </div>\n', NEW_HOT)

# R7 section title
rep('<div class="section-title"><span class="ico">🏆</span>量大能用的先进模型 · Top 10（freellm.net 8/5 刷新实测）+ 场外限免 + 待发布 / 待开源观察</div>',
    '<div class="section-title"><span class="ico">🏆</span>量大能用的先进模型 · Top 10（freellm.net 8/6 刷新实测）+ 场外限免 + 待发布 / 待开源观察</div>')

# R8 GLM-5.3 card: rank-badge + provider + meta-pills + desc
rep('        <div class="rank-badge rank-other">🆕 待发布观察 · 免费额度已曝光</div>',
    '        <div class="rank-badge rank-other">🆕 官宣在即 · 万亿参数旗舰</div>')
rep('            <div class="model-provider">ZCode 泄露 · 尚未正式发布</div>',
    '            <div class="model-provider">智谱官方 8/7 确认 · 发布在即</div>')
rep('          <span class="meta-pill">对标 Fable</span>',
    '          <span class="meta-pill">有望追平 K3</span>')
rep('          <span class="meta-pill">仍在训练</span>',
    '          <span class="meta-pill">万亿参数</span>')
OLD_GLM_DESC = '        <div class="model-desc">8/3 意外曝光（ZCode 页面闪现约 1 小时、Bing 收录、Java SDK 新增 glm-5.3）。泄露的「首发权益」写明：<b>新用户 5 天免费体验、GLM-5.3 300 万 Token/天 + GLM-5-turbo 200 万/天</b>，订阅用户还能「闲时任务免费执行」（算力富余时段排队免费跑，不消耗套餐额度）。爆料称其「还在训练中、能力对标 Fable」。⚠️ <b>模型尚未正式发布、API 也未必开放</b>，当前属于「下一波免费红利预告」，正式上线后大概率走 ZCode / 智谱开放平台，值得持续盯。同门 GLM-5.2（95 分·NIM 免费）仍是当下可立即使用的免费旗舰。</div>'
NEW_GLM_DESC = '        <div class="model-desc">🔥 <b>8/7 重大更新：智谱创始人唐杰在社交平台回应确认 GLM-5.3「发布在即」</b>，虽未给具体日期，但时间节点已临近。要点：① 参数从 GLM-5.2 的 7400 亿级<b>跃升至万亿以上</b>，官方将此次升级定义为「<b>史诗级 plus</b>」；② 业内按此推算若综合提升约 5 分（GLM-5.2 在 artificialanalysis 得 52 分），<b>有望追平 Kimi K3</b>，冲击 60 分大关；③ 命名曾传 GLM-5.5，最终落定 GLM-5.3，延续 5 系列编号。⚠️ 仍需冷静：<b>官方尚未公布模型卡、价格、API 与权重</b>，8/3 短暂现身 GitHub 与官网后已下架，「能免费调」要等正式发布。若延续 8/3 泄露的「新用户 300 万 Token/天 + GLM-5-turbo 200 万/天」首发权益，将是下一波量大能用的免费先进模型——值得蹲守。同门 GLM-5.2（95 分·NIM 永久免费）当下即可用。</div>'
rep(OLD_GLM_DESC, NEW_GLM_DESC)

# R9 Qwen3.8 badge + provider + desc + tags
rep('        <div class="rank-badge rank-other">🆕 待开源观察 · 本周兑现</div>',
    '        <div class="rank-badge rank-other">🆕 即将开源 · 8/10 当周</div>')
rep('            <div class="model-provider">阿里通义千问 · 权重「下周开源」</div>',
    '            <div class="model-provider">阿里通义千问 · 权重「8/10 当周开源」</div>')
rep('「下周开源完整权重」', '「8/10 当周开源完整权重」')
rep('<span class="tag">Qwen3.8-Max(下周开源)</span><span class="tag">Qwen3.8-27B(下周开源)</span>',
    '<span class="tag">Qwen3.8-Max(8/10当周开源)</span><span class="tag">Qwen3.8-27B(8/10当周开源)</span>')
rep('<span class="tag">🆕 GLM-5.3(300万/天免费·待发布)</span>',
    '<span class="tag">🆕 GLM-5.3(官宣在即·300万/天)</span>')

# R10 Insert new risk item (GLM-5.3 官宣在即) before the Ollama risk-item
OLD_ANCHOR = '      <div class="risk-item">\n        <span class="icon">🦙</span>'
NEW_RISK = '''      <div class="risk-item">
        <span class="icon">🔮</span>
        <div>
          <h4>【今日头号 · 利好但要冷静】GLM-5.3 官宣「发布在即」——但「能免费调」要等正式发布，别把生产赌在它上面</h4>
          <p>8/7 智谱创始人唐杰在社交平台回应确认 GLM-5.3「发布在即」（万亿参数、官方称「史诗级 plus」、业内推算有望追平 Kimi K3），是今日最大利好。但必须分清三件事：① <b>截至今日，GLM-5.3 没有模型卡、没有价格、没有公开 API、没有权重</b>——8/3 短暂现身 GitHub 与官网后已下架，真正「能免费调」要等正式发布；② 若延续 8/3 泄露的「新用户 300 万 Token/天 + GLM-5-turbo 200 万/天」首发权益，它将是下一波量大能用的免费先进模型，但这是<b>泄露口径、非官方承诺</b>；③ 同期的「中国开源模型累计下载破 100 亿次、HF 占比 41% 首超美国」是生态里程碑，<b>下载量高 ≠ 你能免费调</b>——权重开源、工具链开源、免费 API 是三件不同的事（详见 Qwen3.8 / H3 / Ling 提醒）。当下能立即白嫖的旗舰仍是 GLM-5.2（95 分·NVIDIA NIM 永久免费）。</p>
        </div>
      </div>
'''
rep(OLD_ANCHOR, NEW_RISK + OLD_ANCHOR)

# R11 Footer updates
rep('、284+ 无需信用卡，8/5 刷新；',
    '、284+ 无需信用卡，8/6 刷新；')
rep('、智谱 ZCode 泄露页面（GLM-5.3 曝光·新用户 300 万 Token/天免费）、AirLLM 开源仓库（4GB 显存跑 2.8T Kimi K3）</p>',
    '、智谱官方 8/7 确认（GLM-5.3 发布在即·万亿参数·史诗级 plus·有望追平 Kimi K3）、智谱 ZCode 泄露页面（GLM-5.3 曝光·新用户 300 万 Token/天免费）、AirLLM 开源仓库（4GB 显存跑 2.8T Kimi K3）、Hugging Face 2026 春季报告（中国开源模型下载占比 41% 首超美国）、工信部数据（国产开源大模型累计下载破 100 亿次）、央视财经报道（中国开源模型全球下载破百亿·Kimi K3 2.8T 一小时登顶 HF 趋势榜）</p>')
rep('本期主线：免费先进模型的容量陷阱（DeepSeek V4-Flash 崩溃）+ 多入口分流策略 + 智谱 GLM-5.3 免费额度曝光 + AirLLM 部署突破',
    '本期主线：智谱 GLM-5.3 官方确认「发布在即」（万亿参数·史诗级 plus·有望追平 Kimi K3）+ Qwen3.8-Max 2.4T 权重 8/10 当周开源倒计时 + 中国开源模型累计下载破 100 亿次（HF 占比 41% 首超美国）+ AirLLM 部署突破')

with io.open(DST, "w", encoding="utf-8") as f:
    f.write(html)

print("Wrote", DST, "length", len(html))
