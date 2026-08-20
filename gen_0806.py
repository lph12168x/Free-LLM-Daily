#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate daily-free-llm-2026-08-06.html from 8/5 template with targeted replacements."""
import io, sys

SRC = "daily-free-llm-2026-08-05.html"
DST = "daily-free-llm-2026-08-06.html"

with io.open(SRC, encoding="utf-8") as f:
    html = f.read()

def rep(old, new):
    global html
    n = html.count(old)
    if n != 1:
        raise SystemExit(f"[FAIL] expected 1 occurrence, found {n} for:\n{old[:120]}")
    html = html.replace(old, new, 1)

# R1 title
rep('<title>免费大模型日报 · 2026-08-05 · Free LLM Daily</title>',
    '<title>免费大模型日报 · 2026-08-06 · Free LLM Daily</title>')

# R2 meta description
rep('<meta name="description" content="2026年8月5日免费大模型日报：聚焦量大能用的先进模型。🔥 剧情反转——本该今日（8/5）零点关闭的腾讯 Hy3 限免，8/4 官宣再次延长至 8 月 31 日，续命 26 天；Kimi K3（98分）蝉联 freellm.net 免费榜第一，GLM-5.2（95）、Gemini 3.6 Flash（91）紧随；新增国家超算互联网 6000万 Token、移动云 MoMA 2500万 Token 两个量大免费入口。">',
    '<meta name="description" content="2026年8月6日免费大模型日报：聚焦量大能用的先进模型。🔥 今日主线——免费先进模型的「容量陷阱」：DeepSeek V4-Flash 官方 API 因流量爆炸一天数次 503 崩溃（并发上限 2500、单日调用数万亿 Token、周调用 70.22 万亿），提醒别把生产链路压在单一免费端点；同期限免续命的腾讯 Hy3 仍可免费用到 8/31；智谱 GLM-5.3 曝光（新用户 300 万 Token/天免费额度）预告下一波红利；AirLLM 让 4GB 显卡跑 2.8T 的 Kimi K3。">')

# R3 date-chip
rep('<div class="date-chip">📅 2026 年 8 月 5 日 · 周三</div>',
    '<div class="date-chip">📅 2026 年 8 月 6 日 · 周四</div>')

# R4 tagline
rep('<p class="tagline">聚焦「量大能用的先进模型」· 覆盖 30+ 国内外平台 · 本期主线：<b>剧情反转——腾讯 Hy3 限免不但没在今天关闭，反而延长到 8/31</b>；同时挖出两个被忽略的超大额免费入口（国家超算互联网 6000 万 Token、移动云 MoMA 2500 万 Token）· 评分数据来自 freellm.net 实时实测（首页 424+ 免费模型、30 家供应商、247 款经实时 API 验证、284+ 无需信用卡，8/4 刷新），并经腾讯 WorkBuddy / CodeBuddy 官方公告、腾讯云开发者社区、阿里通义千问官方发布、Ollama 官方文档、NVIDIA 官方基准卡、OpenRouter 官方定价页、中国移动云帮助中心多源交叉验证</p>',
    '<p class="tagline">聚焦「量大能用的先进模型」· 覆盖 30+ 国内外平台 · 本期主线：<b>免费先进模型的「容量陷阱」——DeepSeek V4-Flash 官方 API 8/4 因流量爆炸一天数次 503 崩溃，提醒别把生产链路压在单一免费端点</b>，多入口分流才是正解；同时预告两条利好：<b>智谱 GLM-5.3 曝光（新用户 300 万 Token/天免费额度）、AirLLM 让 4GB 显卡跑 2.8T Kimi K3</b>；评分数据来自 freellm.net 实时实测（首页 424+ 免费模型、30 家供应商、248 款经实时 API 验证、284+ 无需信用卡，8/5 刷新），并经 DeepSeek 官方状态页、OpenCode 披露数据、腾讯 WorkBuddy / CodeBuddy 公告、智谱 ZCode 泄露页面、Ollama 官方文档、NVIDIA 官方基准卡、OpenRouter 官方定价页、腾讯云 TokenHub、中国移动云帮助中心、国家超算互联网 SCNet 多源交叉验证</p>')

# R5 Focus banner
OLD_FOCUS = '''  <div class="focus">
    <h2>📌 本期焦点：今天本该是腾讯 Hy3 限免的最后一天——结果昨日官宣<span class="hl">再延长到 8 月 31 日</span>，白嫖窗口凭空多出 26 天</h2>
    <p>
      <b>今日头号（对「免费」最有实操价值）</b>：我们连续多期在倒计时的那条死线，今天出现了反转。<span class="hl">8 月 4 日，腾讯 CodeBuddy 与 WorkBuddy 联合公告：Hy3 模型调用限时免费活动，从原定的 8 月 5 日延长至 <b>2026 年 8 月 31 日</b></span>。这已经是该活动的<b>第三次延期</b>——7 月 6 日 Hy3 发布并开源时首发限免两周（7/6–7/22），7 月 20 日腾讯公关总监张军宣布应用户「再来两周」的呼声延至 8/5，如今再顺延至月底。对免费用户来说，这意味着<b>原本只剩几小时的评估窗口，一下子变成了完整的 26 天</b>——足够把 Hy3 真正放进一条生产链路里跑，而不只是做个 demo。<br><br>
      <b>但延期公告里还藏着两条必须看清的细则</b>：① <span class="hl">Hy3 是<b>纯语言模型，暂不具备多模态能力</b></span>——当你让它去做视频、图像生成时，系统会自动切换到对应的多模态模型完成，<b>这部分会按正常规则照常扣积分</b>，不在限免范围内（这是最容易踩的「积分刺客」）；② 因为参与热度过高，官方对<b>每日免费额度做了分配，当日资源繁忙时会进入排队</b>，页面会提示恢复时间。官方同时给了一条很实用的建议：<b>每晚 23:00 至次日 8:00 的错峰时段资源更充足</b>——批量任务、长文档处理排到夜里跑，体感会好很多。<br><br>
      <b>免费榜本身格局未变</b>：freellm.net 8/4 刷新后追踪 <b>424+ 免费模型 / 30 家供应商 / 247 款经实时 API 验证 / 284+ 完全不需要信用卡</b>。<span class="hl">Kimi K3（Ollama Cloud·98）继续蝉联全部免费模型第一</span>，GLM-5.2（NVIDIA NIM·95，周调用 2.9T）第二、Gemini 3.6 Flash（AI Studio·91）第三。另一条本周待兑现的伏笔：阿里 <b>Qwen3.8-Max（2.4T）已于 8/3 发布并承诺「下周开源权重」</b>（同步开源 Qwen3.8-27B），是 Qwen 家族首个开源的 Max 级旗舰，值得盯紧。<br><br>
      倒计时：<span class="countdown">8/31 腾讯 Hy3 限免截止（延长后剩 26 天）</span> · 本周待兑现：Qwen3.8-Max 权重开源 · 已发生：8/3 Ling-3.0-flash 限免关闭并开源、MiniMax H3 权重开源 · 远期：9/30 腾讯混元旧平台停服、10/21 Google Cloud 16 个开源模型端点退役、12/31 腾讯云 TokenHub 与移动云 MoMA 新人活动结束。
    </p>
  </div>'''

NEW_FOCUS = '''  <div class="focus">
    <h2>📌 本期焦点：免费先进模型的「容量陷阱」——DeepSeek V4-Flash 一天数次 503 崩溃，结论是「多入口分流，别把生产压在单一免费端点」</h2>
    <p>
      <b>今日头号（对「量大能用」最有警示价值）</b>：8 月 4 日，<span class="hl">DeepSeek V4-Flash 官方 API 因前所未有的访问量出现性能下降，用户侧多次遇到 503 / 报错，上午几乎不可用</span>，与 Kimi K3 刚发布时的过载高度相似。规模有多大？OpenCode 披露 V4-Flash 单日 Token 调用量达<b>数万亿</b>、周调用 <b>70.22 万亿 Token</b>；官方端点并发上限为 <b>2500（Flash）</b>。DeepSeek 官方当日确认并已修复、服务恢复正常。但<span class="hl">这件事暴露了一个结构性现实：越是「量大、免费/低价」的先进模型，越容易在爆火后被容量拖垮</span>，免费先进模型的可用性不是理所当然的。<br><br>
      <b>对免费用户的实操结论——三句话</b>：① <span class="hl">不要只依赖一个官方端点</span>——同一模型在 NVIDIA NIM（约 40 RPM、无固定日额度）、腾讯云 TokenHub（每模型 100 万 Token）、Ollama Cloud、阿里云百炼都能跑，把其中一个当主、其余当备；② <b>生产链路把模型名抽象成环境变量</b>，哪边 429 就切哪边，5 分钟搞定；③ <b>把对延迟/可用性敏感的实时服务，留给付费档或 NIM 这类有 SLA 的免费托管</b>，免费层只承接批处理与评估。<br><br>
      <b>两条仍在发酵的利好（今日预告）</b>：① <span class="hl">智谱 GLM-5.3 意外曝光</span>——8/3 ZCode 页面闪现约一小时、Bing 收录、Java SDK 新增 glm-5.3，泄露的「首发权益」写明<b>新用户 5 天免费体验、GLM-5.3 300 万 Token/天 + GLM-5-turbo 200 万/天、订阅用户「闲时任务免费执行」</b>，能力对标 Fable、仍在训练中，是下一波可白嫖的先进模型；② <span class="hl">AirLLM 开源</span>——用「逐层加载 + MoE expert streaming」把 2.8T 的 Kimi K3 压进 <b>3.72GB 显存</b>（4GB 显卡即可跑），个人开发者自部署顶级开源模型的门槛大幅降低。<br><br>
      倒计时：<span class="countdown">8/31 腾讯 Hy3 限免截止（还有 25 天）</span> · 本周待兑现：Qwen3.8-Max 权重开源（8/3 发布·下周开源） · 已发生：8/4 DeepSeek V4-Flash 容量崩溃（已恢复）、8/3 Ling-3.0-flash 限免关闭并开源、MiniMax H3 权重开源 · 远期：9/30 腾讯混元旧平台停服、10/21 Google Cloud 16 个开源模型端点退役、12/31 腾讯云 TokenHub 与移动云 MoMA 新人活动结束。
    </p>
  </div>'''
rep(OLD_FOCUS, NEW_FOCUS)

# R6 Hot card
OLD_HOT = '''  <div class="hot">
    <span class="flag">🔥 今日重磅 · 腾讯 Hy3 限免第三次延期，直接续到 8 月 31 日</span>
    <h2>死线反转：295B 国产旗舰的免费窗口，从「今天到期」变成「还有 26 天」</h2>
    <div class="sub">CodeBuddy / WorkBuddy 官方 8/4 公告 · Hy3 实测 91 分 · MoE 295B / 激活 21B / 256K 上下文 / Apache 2.0 开源 · 错峰时段 23:00–次日 8:00 资源最充足</div>
    <p>
      <b>① 延期本身：三度续命，这次给到月底</b>。腾讯 8 月 4 日公告，CodeBuddy 和 WorkBuddy 中 Hy3 模型调用的限时免费活动延长至 <b>2026 年 8 月 31 日</b>。时间线复盘：<b>7/6</b> Hy3 发布并开源、WorkBuddy 首发接入，首轮限免两周；<b>7/20</b> 张军微博宣布应用户呼声延至 <b>8/5</b>；<b>8/4</b> 再次延长至 <b>8/31</b>。官方给出的理由是「用户群体持续扩大、使用热度不断攀升」——换句话说，这是被真实使用量推着走的延期，而不是一次性的营销噱头。对我们这个日报的读者而言，最直接的含义是：<b>过去两周里被反复标注「最香却最短暂」的那个入口，现在变成了本月最值得深度使用的免费先进模型</b>。<br><br>
      <b>② Hy3 到底值不值得花这 26 天</b>：MoE 架构、<b>总参 295B / 激活 21B</b>、最大 <b>256K</b> 上下文、<b>Apache 2.0 开源</b>，核心设计是「快慢双思考融合」——简单任务直接快答，复杂推理自动切深度思考模式逐步拆解并验证推理链。腾讯云公布的办公场景数据：<b>任务成功率从 72% 提升至 90%，平均耗时缩减 34%</b>。freellm.net 此前实测 <b>91 分</b>，若按这个分数放进今天的免费榜，可以排到第 3。它此前在 OpenRouter 上一度是无限免费（周调用 52.6 万亿 Token 登顶），但那个窗口早在 7/21 就关闭并转为付费档，<b>目前唯一稳定的零成本入口就是 WorkBuddy / CodeBuddy 内嵌调用</b>。<br><br>
      <b>③ 三条实操建议（也是三个坑）</b>：<span class="hl">🚫 别用它跑视频 / 图像生成</span>——Hy3 无多模态能力，这类请求会自动路由到对应多模态模型，<b>照常扣积分</b>，限免不覆盖，这是最常见的「误以为免费结果掉积分」场景；<span class="hl">⏰ 把重任务排到 23:00–次日 8:00</span>——官方明说错峰时段资源更充足，白天高峰期可能排队，页面会提示重置时间；<span class="hl">📦 现在就规划落地场景</span>——26 天足够做完一轮完整的「评估 → 试点 → 迁移」，别再当成临时体验。9/1 之后的备选路径：微信「成长计划」10 亿混元 Token（6 个月有效）、腾讯云 TokenHub 新人每模型 100 万 Token，再往后按输入 1 元 / 输出 4 元每百万 Token 计费。
    </p>
    <div class="hot-grid">
      <div class="hot-item"><div class="k">新截止日</div><div class="v">8/31 · +26 天</div></div>
      <div class="hot-item"><div class="k">延期次数</div><div class="v">第 3 次</div></div>
      <div class="hot-item"><div class="k">模型规格</div><div class="v">295B / 激活 21B</div></div>
      <div class="hot-item"><div class="k">上下文</div><div class="v">256K · Apache 2.0</div></div>
      <div class="hot-item"><div class="k">办公任务成功率</div><div class="v">72% → 90%</div></div>
      <div class="hot-item"><div class="k">错峰时段</div><div class="v">23:00–次日 8:00</div></div>
    </div>
    <a class="hot-link" href="https://github.com/Tencent-Hunyuan/Hy3" target="_blank">查看 Hy3 官方开源仓库 →</a>
  </div>'''

NEW_HOT = '''  <div class="hot">
    <span class="flag">🔥 今日重磅 · 免费先进模型的「容量警告」：DeepSeek V4-Flash 一天数次 503，爆火的另一面</span>
    <h2>数万亿 Token/日的免费先进模型，上午几乎跑不动——容量规划仍是低价前沿端点的硬约束</h2>
    <div class="sub">DeepSeek 官方状态页 + OpenCode 披露（8/4）· V4-Flash 并发上限 2500（Flash）· 单日调用数万亿 Token · 周调用 70.22 万亿 · 官方已恢复</div>
    <p>
      <b>① 发生了什么</b>：8 月 4 日上午，大量开发者反馈 <span class="hl">DeepSeek V4-Flash 官方 API 可用性极差、大部分时段无法正常调用</span>，报错集中在 503 / 限流。海外开源 AI 编码 Agent 平台 OpenCode 率先披露：V4-Flash 因「前所未有的访问量」出现容量不足；DeepSeek 官方随后确认「今日上午 V4-Flash API 确实发生性能下降」并已修复、服务恢复正常。社区普遍认为<b>这与 Kimi K3 刚发布时的过载如出一辙</b>——国产先进模型的能力追上了，但算力储备与高并发稳定性还差一口气。<br><br>
      <b>② 规模有多大</b>：V4-Flash-0731 构建于 7/31 发布（后训练强化 Agent 能力、架构不变，284B 总参 / 13B 激活、1M 上下文、缓存未命中 $0.14 / 输出 $0.28 每百万 Token）。OpenCode 数据显示，更新后几天 V4-Flash 单日 Token 量达<b>数万亿</b>，在 OpenCode 观测流量中拿下多数份额；整体周调用约 <b>70.22 万亿 Token</b>。官方端点 Flash 并发上限 <b>2500</b>，峰值时仍会临时不可用。<br><br>
      <b>③ 对免费用户的真正教训（也是本期主线）</b>：DeepSeek V4-Flash 在 freellm.net 免费榜排第 4（90 分·Ollama / 88 分·NIM），是性价比最高的编程 / Agent 主力之一，<span class="hl">但它的「官方免费/低价端点」会在爆火时塌方</span>。所以策略不是「别用」，而是「<b>别只用一个端点</b>」：<b>NVIDIA NIM 的 V4-Flash（88 分、约 40 RPM、393K 输出、无需信用卡）</b>、<b>腾讯云 TokenHub（每模型 100 万 Token）</b>、<b>Ollama Cloud（90 分）</b> 都能跑同一模型，互为备份；生产链路把模型名抽成环境变量，哪里 429 切哪里；实时敏感服务留给 NIM 这类有容量保障的托管，免费层只接批处理。DeepSeek 的快速恢复说明 API 仍是可用的——只是别把鸡蛋放一个篮子。
    </p>
    <div class="hot-grid">
      <div class="hot-item"><div class="k">事件</div><div class="v">8/4 上午 503 频发</div></div>
      <div class="hot-item"><div class="k">并发上限</div><div class="v">2500 (Flash)</div></div>
      <div class="hot-item"><div class="k">单日调用</div><div class="v">数万亿 Token</div></div>
      <div class="hot-item"><div class="k">周调用</div><div class="v">70.22 万亿</div></div>
      <div class="hot-item"><div class="k">状态</div><div class="v">官方已恢复</div></div>
      <div class="hot-item"><div class="k">对策</div><div class="v">多入口分流</div></div>
    </div>
    <a class="hot-link" href="https://status.deepseek.com" target="_blank">查看 DeepSeek 服务状态 →</a>
  </div>'''
rep(OLD_HOT, NEW_HOT)

# R7 section title
rep('<div class="section-title"><span class="ico">🏆</span>量大能用的先进模型 · Top 10（freellm.net 8/4 刷新实测）+ 场外限免 + 待开源观察</div>',
    '<div class="section-title"><span class="ico">🏆</span>量大能用的先进模型 · Top 10（freellm.net 8/5 刷新实测）+ 场外限免 + 待发布 / 待开源观察</div>')

# R8 Insert GLM-5.3 card before Qwen3.8-Max card
OLD_ANCHOR = '''        <a class="model-link" href="https://cloud.tencent.com/developer/article/2720820" target="_blank">查看官方延期公告 →</a>
      </div>

      <div class="model-card">
        <div class="rank-badge rank-other">🆕 待开源观察 · 本周兑现</div>'''

GLM53_CARD = '''      <div class="model-card">
        <div class="rank-badge rank-other">🆕 待发布观察 · 免费额度已曝光</div>
        <div class="model-head">
          <div class="score"><div class="num">300万</div><div class="unit">TOKEN/天</div></div>
          <div>
            <div class="model-name">智谱 GLM-5.3</div>
            <div class="model-provider">ZCode 泄露 · 尚未正式发布</div>
          </div>
        </div>
        <div class="model-meta">
          <span class="meta-pill">对标 Fable</span>
          <span class="meta-pill">仍在训练</span>
          <span class="meta-pill">新用户 5 天免费</span>
          <span class="meta-pill">300万/天 免费额度</span>
        </div>
        <div class="model-desc">8/3 意外曝光（ZCode 页面闪现约 1 小时、Bing 收录、Java SDK 新增 glm-5.3）。泄露的「首发权益」写明：<b>新用户 5 天免费体验、GLM-5.3 300 万 Token/天 + GLM-5-turbo 200 万/天</b>，订阅用户还能「闲时任务免费执行」（算力富余时段排队免费跑，不消耗套餐额度）。爆料称其「还在训练中、能力对标 Fable」。⚠️ <b>模型尚未正式发布、API 也未必开放</b>，当前属于「下一波免费红利预告」，正式上线后大概率走 ZCode / 智谱开放平台，值得持续盯。同门 GLM-5.2（95 分·NIM 免费）仍是当下可立即使用的免费旗舰。</div>
        <a class="model-link" href="https://www.zhipuai.cn" target="_blank">查看智谱官网 →</a>
      </div>

'''

NEW_ANCHOR = '''        <a class="model-link" href="https://cloud.tencent.com/developer/article/2720820" target="_blank">查看官方延期公告 →</a>
      </div>

''' + GLM53_CARD + '''      <div class="model-card">
        <div class="rank-badge rank-other">🆕 待开源观察 · 本周兑现</div>'''
rep(OLD_ANCHOR, NEW_ANCHOR)

# R9 tag-row: add GLM-5.3 + AirLLM tags after the Ling tag
rep('      <span class="tag">Ling-3.0-flash(已开源)</span>',
    '      <span class="tag">Ling-3.0-flash(已开源)</span><span class="tag">🆕 GLM-5.3(300万/天免费·待发布)</span><span class="tag">🆕 AirLLM(4GB跑K3)</span>')

# R10 AirLLM note in 高频 combo
rep('OpenRouter 免费层仅 50 次/天，重度用户建议充 $10 换 20 倍日额度。</p>',
    'OpenRouter 免费层仅 50 次/天，重度用户建议充 $10 换 20 倍日额度。🆕 <b>本地部署新解法</b>：AirLLM 用「逐层加载 + MoE expert streaming」把 2.8T 的 Kimi K3 压进 <b>3.72GB 显存</b>（4GB 显卡即可跑），首次运行需约 1.6TB 硬盘分片、依赖 flash-attn / CUDA 12 / transformers 4.56.x；适合低频推理与体验，不适合高并发生产，是「先免费用上」的过渡方案。</p>')

# R11 Insert new risk item (DeepSeek collapse) after first risk-item
OLD_RISK1 = '''      <div class="risk-item">
        <span class="icon">🎉</span>
        <div>
          <h4>【今日头号 · 好消息但有坑】Hy3 限免延至 8/31 — 但视频 / 图像任务照常扣积分，不在限免范围</h4>
          <p>腾讯 8/4 公告：CodeBuddy 与 WorkBuddy 中 Hy3 模型调用限时免费<b>延长至 2026 年 8 月 31 日</b>（第三次延期，此前分别是 7/22、8/5）。好消息之外必须看清三条：① <b>Hy3 是纯语言模型，暂不具备多模态能力</b>——当你用它执行视频、图像生成任务时，系统会切换到相应多模态模型完成，<b>这部分按正常规则消耗积分</b>，是最容易「以为在白嫖结果掉积分」的场景；② 因参与热度过高，官方<b>对每日免费额度做了分配，当日资源繁忙时会进入排队</b>，页面会提示重置恢复时间；③ 官方建议 <b>每晚 23:00 至次日 8:00 错峰使用，资源更充足</b>。另注意 OpenRouter 上的 Hy3 早在 7/21 转为付费档，别混淆入口。</p>
        </div>
      </div>'''

NEW_RISK1 = OLD_RISK1 + '''
      <div class="risk-item">
        <span class="icon">🚨</span>
        <div>
          <h4>【今日头号 · 容量警告】DeepSeek V4-Flash 官方 API 爆火崩溃——别把生产链路压在单一免费/低价端点</h4>
          <p>8 月 4 日，DeepSeek V4-Flash 官方 API 因前所未有的访问量出现性能下降，用户侧多次遇到 503 / 报错，上午几乎不可用（与 Kimi K3 刚发布时过载如出一辙）；OpenCode 披露单日 Token 调用量达数万亿、周调用 70.22 万亿，官方端点并发上限 2500（Flash），峰值仍会临时不可用。DeepSeek 当日已修复恢复，但教训是结构性的：<b>越是「量大 + 免费/低价」的先进模型，越容易在爆火后被容量拖垮，可用性不是理所当然的</b>。对策三句话：① 同一模型在 NVIDIA NIM（约 40 RPM、无固定日额度）、腾讯云 TokenHub（每模型 100 万）、Ollama Cloud、阿里云百炼都能跑，互为备份；② 生产链路把模型名抽象成环境变量，哪边 429 切哪边；③ 实时敏感服务留给 NIM 这类有容量保障的托管，免费层只接批处理与评估。</p>
        </div>
      </div>'''
rep(OLD_RISK1, NEW_RISK1)

# R12 footer targeted updates
rep('247 款经实时 API 验证', '248 款经实时 API 验证')
rep('（首页 424+ 免费大模型、30 家供应商、248 款经实时 API 验证、284+ 无需信用卡，8/4 刷新；',
    '（首页 424+ 免费模型、30 家供应商、248 款经实时 API 验证、284+ 无需信用卡，8/5 刷新；')
rep('本期主线：腾讯 Hy3 限免第三次延期至 8/31 + 新增国家超算互联网与移动云两大免费入口',
    '本期主线：免费先进模型的容量陷阱（DeepSeek V4-Flash 崩溃）+ 多入口分流策略 + 智谱 GLM-5.3 免费额度曝光 + AirLLM 部署突破')
rep('魔搭 ModelScope</p>',
    '魔搭 ModelScope、DeepSeek 官方状态页与 OpenCode 披露数据（8/4 V4-Flash 容量崩溃与恢复、并发上限 2500）、智谱 ZCode 泄露页面（GLM-5.3 曝光·新用户 300 万 Token/天免费）、AirLLM 开源仓库（4GB 显存跑 2.8T Kimi K3）</p>')

# remove the stale 8/5 page-nav so add_nav.py will regenerate cleanly (optional; add_nav replaces it anyway)
# (left as-is; add_nav.py will overwrite)

with io.open(DST, "w", encoding="utf-8") as f:
    f.write(html)

print("Wrote", DST, "length", len(html))
