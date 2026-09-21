# 免费大模型日报 · 2026-09-21（周一）

> 🤖 AI 每日免费情报 · 全网挖掘 · [在线版 HTML](daily-free-llm-2026-09-21.html)

**今日四个关键数字**

| 数字 | 含义 |
| --- | --- |
| **$5** | 「不聊天」的 **Jev 今天全员开放**：注册即送 **$5 额度 ≈ 1.2 亿 token**，输入 $0.042/百万、**输出 $0** |
| **44 分** | 阶跃 **Step 5 Preview**（600B/27B、1M、AA 全球开源前三）API 已开放，新用户**最高 75 天免费** |
| **10 天+** | DeepSeek **9/20–10/10 超十天半价**：调休周末与法定节假日全天按低谷计费 |
| **24 / 9** | OpenRouter 今日零价 **24 款**（`:free` 21）零变；Zen 免费 ID **9 个**（含 `deepseek-v4-flash-free`） |

---

## 🔥 今日头条 · 三条主线

### ① 全民免费｜「不聊天」的 `Jev` **今天全员开放**：注册即送 **$5 ≈ 1.2 亿 token**，三条免费通道同时开门

**上周那个「一句话都不会说」的模型，今天把门槛拆了**——TypeSafe AI 宣布 `Jev` **面向所有用户开放、无需候补名单**，且**所有注册用户赠送 $5 额度，约等于 1.2 亿 token**。因为它**不生成文本**、输出只有几个 token 宽度的结论，Token 消耗远低于一般大模型，所以这份额度「能蹬很久」。

| 项目 | 内容 |
| --- | --- |
| 🆕 今日新增量 | 此前 Jev 只有 early access 候补名单（9/15 出隐身）；**今天起注册即用**——入口 `console.typesafe.ai`。定价仍是输入 **$0.042 / 百万 token**、**输出 $0**（官方话术「too cheap to meter」），单次响应 **70–500 毫秒** |
| ⚡ 现在有三条免费通道并存 | ① **TypeSafe 官方**：全员 $5（≈1.2 亿 token）；② **Vercel AI Gateway**：`typesafe-ai/jev` 标 Free，**促销价 2026-09-25 结束**（32K 上下文、零数据留存、不用于训练）；③ **OpenRouter beta**（9/18 官宣）+ **OpenCode Zen** `jev-1.13-free`（9/20 起）。**四条路都能走，按你要不要自建 key 挑** |
| 📈 采用速度（Vercel 官方数据） | 上线**第一天即触达约 13% 的付费团队**——是 GPT-5.6 家族的 **2 倍**、Claude Fable 5.1 的 **6 倍**；冲到 10% 只用了 **18 小时**。OpenRouter 侧，`Jev 1.13` 在近 7 天变幅榜上从 245B 涨到 **464B tokens**，稳在第 3 |
| 🧰 一周长出来的生态（都能直接用） | **Needle**（Apache-2.0 Chrome 扩展：不生成答案，只按「意图」给页面原句打分并高亮）；**pg-jev**（Postgres 扩展，`WHERE jev(people, 'the name is European')`）；**fast-jev-compaction**（用 Jev 挑出还需保留的工具调用，**Claude Code 会话 token 最高砍 90%**，失败自动回退内置摘要）；**jev-voice-browser**（把语音中间结果持续喂给 Jev，**约 300ms** 内可决策）；Browser Use 的 `jev-ultrafast` |

**为什么值得今天就试**：把 Agent 里「**分类 / 路由 / 打分 / 门禁**」这类**输出本就是有限集合**的调用整体搬过来即可——你给它一段状态和若干**带类型的问题**（boolean / choice / score），它**并行**返回答案与校准概率，而不是逐 token 生成。**成本降 2–3 个数量级、延迟降一个数量级**。有位排上候补的开发者估算，自己管线里 **40%–70% 的 LLM 调用**可以换成决策调用。

**⚠️ Vercel 免费层有个反直觉的坑**：官方定价文档原文——**「Once you purchase credits, your account transitions to the paid tier and the monthly free credit no longer applies.」**——**你一旦充值，每月那 $5 免费额度就永久失效**；且 **BYOK 在免费层不可用**（那是付费层功能）。正确策略：**先把免费 $5 跑够，真不够再充**。

**⚠️ 三个边界**：① Jev **不会写字**——问它「帮我写个周报」是没有用的，它只做判断；② Vercel 官方给 Jev 的示例只有 AI SDK 的 `experimental_evaluate`，它是**判别式接口**，**别想当然塞进 `chat/completions`**；③ 这类模型**没有公认基准**，「类型安全」不等于「事实正确」——格式合法但内容错的输出照样存在。

---

### ② 国产旗舰｜阶跃星辰 `Step 5 Preview`：600B/27B、1M 上下文、**AA 44 分全球开源前三**，单任务成本约 Opus 5 的 1/8，**新用户最高 75 天免费**

9 月 20 日，上海阶跃星辰发布新一代旗舰基座模型 **`Step 5 Preview`**：**发布当日 API 全量开放**，**10 月 15 日释放完整 BF16 权重**。这不是一次增量迭代——它**跳过了 Step 4.x 直接进 Step 5**。

| 项目 | 内容 |
| --- | --- |
| 🧩 规格（把「贵」的地方都改掉了） | 稀疏 MoE：总参 **6,000 亿**、每个 token 只激活 **270 亿**（约 4.5%）；**92 层「窄而深」Transformer**（用深度换多跳推理的信息通路）；**1M 上下文**；原生 **文本 + 视觉**。长上下文成本用 **Sparse GQA + 块级 token 合并**压下来，官方称索引与 top-k 开销**降到稠密基线的约 1/8**；工程侧还有 FP8 MoE、MTP-3 投机解码、KV-cache offload |
| 🏆 跑分与单位成本 | Artificial Analysis 智能指数 **44 分**，**全球开源模型前三**——同一区间里 GLM-5.3 (max) 44.8、Kimi K3 (max) 43.6；**软件工程 67.7**，仅次 GPT-6 Astra 与 Claude Opus 5，领先 Kimi K3、GLM-5.3；**FrontierFinance 66.4，全球第二**（含 220 道专业金融题、11,543 项评估标准）。**每完成一项智能指数任务约 $0.71**，约为 Claude Opus 5 的 **1/8**，也低于 Kimi K3 Max 的约 $2；输出速度约 **100 tok/s** |
| 🕒 长周期任务才是它想证明的 | 一次 24 小时无人干预实验中，它自主优化一组 H100 GPU 内核（改代码 → 跑测试 → 比结果 → 迭代），约 **22 小时达到 508 TFLOPS**——同一实验中 **Claude Opus 5 为 493 TFLOPS**。另一次 24 小时运行中，它自己设计并训练数据，把 **Qwen3-30B-A3B 在 AIME24 上从 53.3% 提到 60%**，与 Opus 5 持平而标注 token 更少 |
| 🎁 免费怎么拿（最高 75 天） | 列表价：**¥7 / 百万输入**（缓存命中 **¥0.35**）、**¥20 / 百万输出**。免费额度是**拼出来的**：注册送 **¥99 礼包** → 每日登录 **+15 天** → 完成首次调用 **+15 天** → 每邀请 1 位好友注册，**双方各 +15 天（最多 3 位 = +45 天）**，合计**最高 75 天** |

**读法**：这条与「开源 = 便宜但弱」的旧印象正相反——**同样的智能，成本更低**。AA 指数上它和 Kimi K3 Max 同分，但单任务成本只有后者的约 1/3、Opus 5 的约 1/8——**「智能效率」这条路线在 9 月被国产旗舰明确讲了一次**。对成本敏感的编程 Agent、批量文档处理、金融研究，值得纳入候选。

**⚠️ 三个提醒**：① **权重 10/15 才开，许可证尚未公布**——现在只能走 API / Studio，别按「已可自部署」做规划；② **实际速度一般**，免费用户一多会进一步变慢，别按 100 tok/s 做实时业务的容量估算；③ 它是 **Preview**，基准分数与定价都可能随正式版调整，生产环境请先用自己的任务集实测。

---

### ③ 直达降价｜DeepSeek 峰谷口径澄清：**9/20–10/10 超十天全天低谷价**，调休周末与法定节假日都按半价算

今天最「量大能用」的一条不是新模型，是**一张更清楚的价目表**。9 月 19 日，DeepSeek 就峰谷计价发补充说明：原先「工作日高峰价为低谷 2 倍、周末按低谷价」的规则里，**「调休上班的周末」一直处于灰区**——现在这个灰区被封掉了。

| 项目 | 内容 |
| --- | --- |
| 📌 新口径（一句话） | **任何周末（即使是调休上班日）与所有法定节假日，全天按低谷时段计费**。此前没有明确归属的 9/20（周日，调休上班）与 10/10（周六，调休上班）现在都算低谷 |
| 📅 覆盖窗口 | **9/20 – 10/10 连续超十天低谷价**，含 **中秋 9/25–27**、**国庆 10/1–7**，外加两个调休周末。官方口径是**年内最集中的一段折扣期**——把批量任务排到这里，等于白省一半 |
| 💰 具体价格 | 工作日高峰（**9:00–12:00、14:00–18:00**）为低谷 **2 倍**；低谷减半。**V4.1 Flash 低谷：缓存命中输入 ¥0.02 / 百万 token、输出 ¥4 / 百万 token**（具体单价请以官方定价页为准） |
| 🧠 配套的能力底座 | 这条降价要配合 **`deepseek-v4.1-flash`** 看才有意义：**552B MoE、非对称架构**（prefill 激活 8B / decode 16B）、**1M 上下文**、FP4 KV cache（约 890 B/token），多项基准超过 V4 Pro；**权重已于 9/11 在 Hugging Face 以 MIT 开源**——想彻底归零 token 成本可以直接自部署 |

**为什么这是「量大能用」最实在的一条**：不用换平台、不用注册新账号、不用抢券——**只是把批量负载挪到低谷时段，成本直接砍一半，而且这个窗口一次给足十天以上**。适合：夜间跑批、大规模评测、长文档批处理、数据合成。

**⚠️ 三个坑**：① **工作日 9–12 点与 14–18 点是双倍价**，白天实时业务别按低谷价做预算；② 计价按**小时切分**，长任务跨过 18:00 会**分段计价**，跑批前先算时间窗；③ 「半价」是相对高峰价的表述，**绝对单价以官方定价页为准**，云端会随版本调整。

---

## 🌤️ 次要更新 · 值得记一笔

- 🚪 **新网关 `Tokenator`：把免费旗舰模型塞进「付费 key」的第三种免费形态** —— 今天新出现的一类 API 网关 **Tokenator**（`api.tokenator.cloud`）在免费档挂了四条真旗舰：**`free-gpt-6-astra`**（1M / 输出 128K / 支持图片输入）、**`free-claude-opus-5`**（1M，标注 **Unstable**）、**`free-glm-5.3-flash`**（1M）、**`free-gemini-3.8-flash`**（1M）。机制是：免费模型**不消耗你付费包的 token 额度**（不套 multiplier），但**每模型每天固定 2M tokens + 30 请求**，**00:00 UTC 重置**——用超了只返回 `429 free_model_daily_limit`，**不会自动转成付费计费**；剩余额度可查 `/v1/tokens`。门槛是**需要一把已经付费的 key**（上游为第三方 LimitedAI，GPT-6 Astra 该条标 6× multiplier）。协议侧同时兼容 `/v1/chat/completions`、`/v1/responses`、`/v1/messages`，可接 Claude Code / Codex CLI / Cursor / Cline 等。**读法：这是「免费」的第三种形态——不花钱买 token，但要用「已付费的账号」换资格**；适合低成本摸一下旗舰、不打算长期订阅的人，**别把 2M/天当产能**。

- 🖼️ **通义千问开源 `Qwen-Image-2.1`：7B「生成 + 编辑」一体，原生 RGBA 透明图层** —— 千问 9/20 发布 **`Qwen-Image-2.1`** 并**开放权重**：采用**生成与编辑一体化的 7B 轻量架构**，定位 Qwen-Image 系列里「均衡且高性价比」的一档，推理速度表现优异。它**原生支持生成与编辑 RGBA 透明图层**，可做无缝合成与**透明图像内的文字编辑**；编辑侧支持**最多 10 张参考图 + 精确局部控制**，对肖像与产品保持严格保真度；擅长全景图、信息图、虚拟试穿等场景。已在 **GitHub / ModelScope / Hugging Face** 上线——**本地跑就是 $0**。

- 📚 **微信 AI 团队开源 `WeKnora` 0.8.0：把知识变成「可验证结果」** —— 微信 AI 团队开源知识管理框架 **`WeKnora`**（0.8.0 全面开放，**MIT 许可、可商用**，架构模块化）。它针对「大模型落地时知识难以转化为可验证结果」这个痛点，三个核心点：**① anydoc 解析 + Wiki 模式**（多格式文档直接导入并自动整理为结构化知识体系）；**② GraphRAG**（抽取实体与关系构建图谱，提升关联类问题的检索可靠性）；**③ Skill Sandbox Runtime**（把知识封装为技能，在 Docker 等沙箱环境中**安全执行并返回可验证结果**）。配合长期记忆，形成「解析 → 组织 → 检索 → 执行 → 记忆」的完整链路。

- ⏰ **讯飞 `AStudio` 星火 X2.5 限免只剩两天（9/23 00:00 截止）** —— 科大讯飞桌面 AI 工作台 **AStudio**（Windows / Mac）里，旗舰 **Spark X2.5 在限免期内调用消耗标为 0 积分**——复杂任务随便跑不扣分。入口 **agent.xfyun.cn** 下载客户端，**国内网络直连**；手机验证码或微信扫码登录，**新用户登录即送 1000 积分**（官方称约够 150 个日常轻量任务）。⚠️ 用法有个必须做的动作：在输入框右下角的模型选择器里**勾选带「七天限免」角标的 Spark X2.5**——这一步别跳，不勾就走正常扣分。工作台里聚合的 **GLM-5.2、DeepSeek V4 Pro / Flash 不参与限免**，那 1000 积分留着试它们。截止 **9/23 00:00**（不是当天走完）；体验版本体免费，限免结束后工具仍可用，只是开始扣积分。

- 🎁 **智谱双份补给：`AutoClaw` 新人 1 亿 GLM-5.3-Flash tokens + ZCode 全员周额度已重置** —— ① **`AutoClaw`**（社区叫「澳龙」，智谱桌面端 AI 智能体客户端）：官网首页明确写着**新用户注册登录即领 1 亿 GLM-5.3-Flash tokens，官方标注价值 ¥60**，入口 **autoclaw.zhipuai.cn**——属**长期新人礼**而非限时活动。② **ZCode 隐私事件的补偿已落地**：官方就「Repo Wiki 生成 Wiki 页面时触发仓库数据上传」公开致歉，说明数据云端生成后立即销毁、**问题已完成修复并关闭相关默认配置**，并计划**开源代码库 + 邀请第三方独立审查**；同时**为全体 ZCode 用户额外重置一次周额度**（已于说明发布当日发放）。③ 提醒：**ZCode 夜间免费（9/3–9/20，每晚 23:00–09:00）已于 9/20 归档结束**，之后按常规规则计费。

- 📊 **freellm.net：目录 502+ 款 / 31 平台 / 243 live；免绑卡 412+；榜首 NIM `z-ai/glm-5.3`（97）** —— 站内计数 **502+ 款模型 / 31 家平台 / 243 款经 live API 实测 / 412+ 款免绑卡**，最近更新 **2026-09-21**（较昨日 503+ / 244 略降）。榜单前十：**NIM `z-ai/glm-5.3` 97**（1.3M / 131K 输出 / 40 RPM）→ `glm-5.3-flash` 96（1.3M / text+image+video+pdf）→ **OpenRouter `Ling 3.0 Flash Sante (free)` 95** → `Qwen3.8 27B (free)` 93 → Ollama Cloud `deepseek-v4-pro` 92 → `deepseek-v4-flash` 91 → **NIM `Kimi K3` 91** → LLM7.io `GLM-5.3-Flash` 90 → NIM `deepseek-v4-flash-0731` 89 → **OpenCode Zen `GLM-5.3` 88**。⚠️ 口径提醒：freellm.net 的 Provider 页把 OpenRouter 记为「**25 款免费模型**」，而官方接口同刻是 **24 款零价 / 21 款 `:free`**——**聚合站与官方目录存在计数差，判定「是否免费」一律回官方接口**。

---

## 🧾 今日免费入口速查 · 先进 + 量大优先

按「能直接调、模型够先进、额度够大」三条筛过一遍，今天最值得先试的是这几条：

| 入口 | 能调到的先进模型 | 额度 / 价格 | 门槛 |
| --- | --- | --- | --- |
| **阶跃星辰**（今日上线） | **`step-5-preview`**：600B/27B 稀疏 MoE、92 层窄深、**1M 上下文**、文本+视觉；AA 智能指数 **44**、软件工程 67.7、FrontierFinance 66.4 | 新用户**最高 75 天免费**（¥99 礼包 + 登录 15 天 + 首调 15 天 + 邀请 3×15 天）；列表价 **¥7 / 百万输入**（缓存 ¥0.35）、**¥20 / 百万输出** | 注册即用；**权重 10/15 开源** |
| **TypeSafe Jev**（今日全员开放） | **`jev`**：System One 决策模型，返回 boolean / choice / score + **校准概率**，**70–500ms**、32K、选项上限 255；**不生成文本** | 全员 **$5 ≈ 1.2 亿 token**；输入 **$0.042 / 百万**、**输出 $0**；另 **Vercel AI Gateway 免费至 9/25**、OpenRouter beta、Zen `jev-1.13-free` | `console.typesafe.ai` 注册即用（**已无需候补**） |
| **OpenCode Zen**（免费 ID 9 个） | **`deepseek-v4-flash-free`**（**接口在架、定价页未列**）、`nemotron-3-ultra-free`（1M）、`nemotron-3.5-lightning-free`（1M）、`muse-spark-1.3-contributor-free`（1M 全模态）、`mimo-v2.5-free`、`ling-3.0-flash-fin-free`、`jev-1.13-free`、`big-pickle`（隐身，200K） | **$0**；定价页 Free 行 **7 款**，**均标注 limited time**；免费期数据可能用于改进模型 | 登录拿 Key，客户端内直接选 |
| **OpenRouter**（$0） | 零价池 **24 款**（`:free` 21）；1M 档 `nemotron-3-ultra-550b-a55b:free`、`nemotron-3.5-lightning:free`、`thinkingmachines/inkling:free`（全模态）；多模态 `qwen3.8-27b:free`（262K / text+image+video） | **$0**；`:free` 约 **20 RPM / 50 RPD（全池共享）**，累计充值满 $10 后升到 **1000 RPD**；另有自动路由池 `openrouter/free`（200K） | 注册即可，**免信用卡** |
| **NVIDIA NIM**（量大） | `z-ai/glm-5.3`（1.3M，评分 **97**）、`glm-5.3-flash`（1.3M / 944K 输出）、**`Kimi K3`（1M，K3 当前唯一免费入口）**、`deepseek-ai/deepseek-v4-flash-0731`（1.3M）等 100+ 款开源模型 | **$0**；**约 40 RPM 且调用量不设上限**（单看「量大」最优） | 注册 + **手机号验证**；部分端点标注 Trial only，**勿传敏感数据** |
| **DeepSeek 官方**（半价窗口） | `deepseek-v4.1-flash`（552B MoE、1M、权重 MIT 已开源）、`deepseek-v4-pro`、V4 Flash | **9/20–10/10 全天低谷价**（含中秋 9/25–27、国庆 10/1–7、调休周末）；V4.1 Flash 低谷**缓存命中输入 ¥0.02 / 百万、输出 ¥4 / 百万** | 注册；想彻底归零可自部署（MIT） |
| **书生 InternLM**（稳定兜底） | `intern-latest`（→397B，256K）、`intern-s2-preview-397b` / `-35b`、`intern-s1-pro`（**内置联网搜索**）、多模态 `internvl3.5-241b-a28b` | **每月 1.8 亿 Tokens**（输入 90M + 输出 90M）；**30 RPM / 300K TPM**；**无明确到期日**，可线上申请提额 | 注册即可，**免信用卡** |
| **国内直供**（额度大） | **智谱** AutoClaw 新人 1 亿 GLM-5.3-Flash + GLM-4.7-Flash（永久免费 200K）；**讯飞**星火 X2.5（**限免至 9/23**）；**阿里 Qoder** Qwen3.8-Flash（**免费至 9/30**）；**腾讯**混元 Hy3（免费至 9/30）；**火山引擎**豆包 2.1 Pro / DeepSeek 系 | AutoClaw **1 亿 tokens**（长期新人礼）；讯飞限免期 **0 积分**；Qoder **Qwen3.8-Flash 系数 0 + 每日 100 Credits**；火山 **200 万 Tokens/天**（零点刷新不累积） | 需实名；**⚠️ 腾讯老混元平台 9 月底停服，新项目直接上 TokenHub** |

**一句话选型**：想**现在就用上旗舰级开源**，走阶跃的 **`step-5-preview`**（最高 75 天免费，1M + 视觉）；想把 **Agent 里的判断类调用**整体降本，走 **Jev**（官方 $5 额度，或 Vercel Gateway 免费到 9/25）；想要 **1M + 多模态且长期免费**，走 OpenRouter 的 **`nemotron-3-ultra-550b-a55b:free`** 或 **`inkling:free`**；想**批量任务省钱**，把负载排进 **DeepSeek 9/20–10/10 低谷窗口**；想**长期不担心额度**，走 **NVIDIA NIM**（40 RPM 不限量）或 **书生 InternLM**（1.8 亿/月、无到期日）。**免费券寿命已实测短到 2 天以内——别写死、别上生产、永远留一条 fallback。**

---

## 🔎 平台盘点 · 今日快照

### 📊 OpenRouter：446 款中 24 款零价（`:free` 21 款），**连续两期零变**

- 脚本清点 `pricing.prompt == '0' 且 pricing.completion == '0'`：**24 款**；其中 id 以 `:free` 结尾的 **21 款**。**目录总数 446 → 446，零价 24 → 24，进 0 / 出 0**。
- 三条「零价但不带 `:free` 后缀」仍在：`google/lyria-3-pro-preview`、`lyria-3-clip-preview`（1M，**输出音频**）、自动路由池 `openrouter/free`（200K）。
- 1M 上下文免费档共 **6 条**：`nemotron-3.5-lightning:free`、`nemotron-3-ultra-550b-a55b:free`、`thinkingmachines/inkling:free` / `inkling-small:free`，加两条 `lyria-3-*`（音频输出）。
- ⚠️ 免费池**日内会波动**，24 / 21 是脚本清点时刻的快照。已留 `or_models_0921.json` 供次日 diff。

**零价池近四期流水**

| 清点日 | 零价总数 | 其中 `:free` | 关键进出 |
| --- | --- | --- | --- |
| 9/17 | 24 | 20 | 进 `nex-n2.5` 双条 |
| 9/18 | 25 | 22 | 进 `deepseek-v4-flash-0731:free` + `qwen3.8-27b:free` |
| 9/20 | 24 | 21 | 出 `deepseek-v4-flash-0731:free` |
| **9/21（今天）** | **24** | **21** | **零新进、零退出（连续两期持平）** |

### 🏆 OpenRouter 榜单（数据截至 9/20）：**DeepSeek V4.1 Flash 周榜登顶**；作者份额 **deepseek 25.4% 第一**

- **周榜（Top 10）**：**1** `DeepSeek V4.1 Flash` **15.8T**（+219%）· **2** `GLM 5.3 Flash` 14.1T（+18%）· **3** `Hy4 preview` 12.5T（+26%）· **4** `GPT-5.6 Luna` 9.72T（+47%）· **5** `DeepSeek V4 Flash 0731` 9.44T（+18%）· 6 `MiMo-V2.5` 7.07T · 7 `Hy3` 4.78T · **8 `Nemotron 3 Ultra (free)` 4.49T（+26%）= 前十唯一免费** · 9 `DeepSeek V4 Flash 0423` 3.77T · 10 `GLM 5.3` 3T。
- **日榜**：`GLM 5.3 Flash` **2.52T** 第一 · `DeepSeek V4.1 Flash` 2.49T · `Hy4 preview` 1.97T（+40%）。**月度榜**：`GPT-5.6 Luna` **49.4T**（+209%）第一 · `DeepSeek V4 Flash 0731` 48.5T（+61%）。
- **近 7 天变幅榜**：**1** `DeepSeek V4 Flash 0731 (free)` **1.09T**（new）· **2** `Union Alpha` 977B（new）· **3 `Jev 1.13` 464B（new，较昨日 245B 继续翻倍）** · 4 `GLM 5.3 FlashX` 26.2B · 5 `Qwen3.8 27B (free)` 12B。**⚠️ 前两名都已经不是（或不再是）在架免费——榜单是「过去 7 天」的累计量，滞后于下架动作**。
- **作者份额**（文本请求，week of 9/14）：**deepseek 25.4%（+9%）首次登顶** · google 18.6%（−3%）· openai 17.0%（**−30%**）· z-ai 9.4%（+31%）· qwen 6.7%（+25%）· tencent 6.4%（−14%）· anthropic 2.7%（+3%）· mistralai 2.6%（+11%）· xiaomi 1.9%。
- **应用榜**：**Hermes Agent 1.44T 第一**（Nous 开源自改进 Agent）· Claude Code 505B · Kilo Code 493B · Cline 412B · pi 305B · **omp 202B（新）** · OpenClaw 166B · Codex 150B · **DeepSeek Harness 131B（新）** · Freebuff 130B。
- **AA 智能指数榜**（可拿来给 Step 5 定位）：Claude Fable 5.1 **53.4** · Qwen3.8 Max 53.4 · GPT-6 Astra (max) 52.7 · Claude Opus 5 50.8 · GPT-5.6 Sol (max) 47.0 · GLM-5.3 (max) **44.8** · Grok 4.6 (high) 44.3 · Kimi K3 (max) **43.6** —— **Step 5 Preview 的 44 分正落在这一档**。

### 🔧 OpenCode Zen：**74 款**零增减；免费 ID **9 个** vs 定价页 Free 行 **7 款**

- `/zen/v1/models` 返回 **74 款**（与 9/20 持平，零增减）。带免费标记的 ID 共 **9 个**：`big-pickle`、`jev-1.13-free`、**`deepseek-v4-flash-free`**、`mimo-v2.5-free`、`ling-3.0-flash-fin-free`、`nemotron-3-ultra-free`、`nemotron-3.5-lightning-free`、`muse-spark-1.3-contributor-free`、`muse-spark-1.2-contributor-free`。
- 官方**定价页 Free 行**是 **7 款**（Big Pickle / MiMo-V2.5 / Ling 3.0 Flash Fin / Nemotron 3 Ultra / Nemotron 3.5 Lightning / Muse Spark 1.3 Contributor / Jev 1.13 Free）——**与 models 端点的 9 个仍不一致**：差的是 **`deepseek-v4-flash-free`** 与 `muse-spark-1.2-contributor-free`（这两条在定价页走付费价）。**按平台一贯口径，以定价页为准**。
- 定价页里 **`Jev 1.13` 付费行 = 输入 $0.042 / 输出 Free**（即输出 token 不计费），走 `/zen/v1/systemone` 独立协议；免费版用 `jev-1.13-free`。
- 📖 官方文档口径：**免费模型多为「limited time」**，且 Big Pickle / MiMo-V2.5 / Ling 3.0 Flash Fin **免费期数据可能用于改进模型**；Nemotron 两条是 **NVIDIA 试用端点，明确要求不要提交个人或机密数据**；Muse Spark Contributor Free 以免费换 Meta 用提示词与补全训练模型。
- ⏰ 同页提示：**GPT 5.6 Sol 的五折已于 9/18 到期**，现价回到 $4.00 / $20.00（≤272K）。

### 🌐 免费路由生态：把「几十家免费额度」聚成一条链

- **两条「几乎全免费」的本地路由**：**OmniRoute**（MIT 开源，把单个本地端点接到 **260+ 家** AI 供应商，公开免费档去重后官方称约 **16 亿免费 token / 月**，**11 家永久免卡**），与 **Free Claude Code**（本地代理，把 Claude Code 的请求转发到 NIM / OpenRouter / DeepSeek / Groq / Mistral / 本地 llama.cpp 等，覆盖 **27 家**）。
- **常被忽略的几条永久免费档**：**Pollinations**（**免 key 即用**，适合临时起意）；**美团 LongCat**（`LongCat-Flash-Lite` **每天 5,000 万 token**，量大杂活兜底）；**Cerebras**（Qwen3-235B / GPT-OSS-120B，**每天 100 万 token**，超长上下文与批处理友好）；**Cloudflare Workers AI**（50+ 开源模型，**每天 1 万 neurons**）；**Qoder**（Kimi-K2 / DeepSeek-R1 / Qwen3-Coder，**额度不限**）。
- **组合建议**：**主力**用一个稳的（Qoder / NIM），**兜底**用一个常驻免费的（LongCat / InternLM），**临时**用免 key 的（Pollinations）——**别把所有调用压在一个免费档上，它随时可能限流**。

---

## 📅 到期日历 · 别踩空

**眼前这一周**

- **9/21（今天）** — **Jev 全员开放**（$5 ≈ 1.2 亿 token）；**DeepSeek 低谷价窗口**第 2 天；千问办公 × 杭州 Token 卡持续发放中
- **9/23（00:00）** — **讯飞 AStudio 星火 X2.5 限免结束**；**WorkBuddy / CodeBuddy 的 DeepSeek V4.1 Flash 0.03× 折扣结束**
- **9/24** — **文心快码 Comate** 测试版限免结束；**字节 TraeCode Seed 系列 1 折**结束
- **9/25** — **Jev 在 Vercel AI Gateway 的免费促销结束**（官方原话「Promotional pricing ends on September 25, 2026」）

**9 月下旬及以后**

- **9/30** — **阿里 Qoder Qwen3.8-Flash 免费用结束**；**腾讯 Hy3 / 文心 4.0 免费期结束**；Merge Gateway GLM-5.3-Flash 1 折结束；WorkBuddy 教师积分；**腾讯老混元平台停服**
- **10/10** — **DeepSeek 低谷价窗口结束**；**腾讯混元 Hy4 preview**（老用户夜间免费）结束；**unbiased.ai `Pareto` 正式发布日**
- **10/14** — 珠海算力券申报截止（企业向，每年最高 200 万）
- **10/15** — **阶跃 Step 5 Preview 释放完整 BF16 权重**（许可证待公布，届时可自部署）
- **10/31** — WorkBuddy 学生积分截止
- **11/7** — MiniMax 开放平台 M3 / M2 免费试用延长到期
- **12/31** — 腾讯云 TokenHub / 华为云码道「码力续航计划」/ 移动云 MoMA 截止

---

## 🧭 今天该怎么动

**① 现在就做（5 分钟内）**

- 去 `console.typesafe.ai` 注册一个 Jev 账号，把那 $5（≈1.2 亿 token）领掉——今天起不用候补名单了，这是当前最便宜的「决策层」入口。
- 顺手把「批量任务」挪进 DeepSeek 低谷窗口：9/20–10/10 全天低谷，把夜间跑批、评测、数据合成的任务改到 18:00 之后触发即可，成本直接砍半。

**② 今天之内**

- 试一次 Step 5 Preview：把手上一个「长上下文 + 多轮工具调用」的真实任务丢给 `step-5-preview`，和 Kimi K3 / DeepSeek V4.1 Flash 跑同一个任务集对比——**它主打的就是「同智能、1/8 成本」，要用自己的任务集验证而不是看榜单**。
- 讯飞用户：限免只剩两天（9/23 00:00），今天把复杂任务跑掉；**记得在模型选择器里勾带「七天限免」角标的 Spark X2.5**。
- 智谱用户：去 ZCode 客户端确认本周额度是否已被重置；**去 AutoClaw 把新人 1 亿 tokens 领了**（长期有效）。

**③ 本周之内**

- **做一次「决策拆解」自检（第二次提醒）**：把 Agent 里分类 / 路由 / 打分 / 门禁的调用从聊天模型拆出来交给 Jev 这类决策模型——**成本降 2–3 个数量级**，且今天有了「免注册候补、送 1.2 亿 token」的低门槛入口，试验成本几乎为零。
- **配好兜底线**：NVIDIA NIM（40 RPM 不限量，也是 K3 唯一免费入口）+ 书生 InternLM（1.8 亿 tokens/月、无到期日、免信用卡）+ DeepSeek 官方（低谷价 + MIT 权重可自部署）。
- **别把「在架免费」当稳定**：本页统计的两条 1M 免费券寿命已实测短到 2 天以内；任何写死单条 `$0` 通道的地方，本周加一条可切换的备线。
- **留意 10/15**：阶跃 Step 5 权重开源当天再评估一次自部署可行性（许可证是变量）。

---

## 📋 数据来源

OpenRouter `/api/v1/models`（9/21 脚本清点，446 款中 24 款 $0 / 21 款 `:free`，已留 `or_models_0921.json`）· OpenRouter Rankings（数据截至 9/20：周榜 / 日榜 / 月榜 / 近 7 天变幅榜 / 作者份额 week of 9/14 / Apps 榜 / AA 智能指数榜）· TypeSafe `Jev`（9/21 全面开放、全员 $5 ≈1.2 亿 token、输入 $0.042/百万、输出 $0、70–500ms、32K；Vercel AI Gateway `typesafe-ai/jev` 免费促销至 2026-09-25、ZDR、不用于训练；Vercel 免费层「充值即失去每月 $5 额度」原文；生态：Needle / pg-jev / fast-jev-compaction / jev-voice-browser / Browser Use jev-ultrafast）——36 氪 9/21、unwind ai、Vercel 官方模型页与定价文档 · 阶跃星辰 `Step 5 Preview`（9/20 发布；AA 44、软件工程 67.7、FrontierFinance 66.4、约 $0.71/任务、100 tok/s；24h 自主优化 H100 内核 508 TFLOPS；¥7/百万输入、¥20/百万输出；最高 75 天免费；10/15 释放 BF16 权重）——StepFun 官方发布页 / 网易 / 上观新闻 / Pandaily / DataLearner / ai-damn · DeepSeek 峰谷定价补充说明（9/19）——太平洋电脑网 / ai-damn / 官方公告 · OpenCode Zen `/zen/v1/models`（74 款）与官方定价页 · 通义千问 `Qwen-Image-2.1`（9/20 开放权重）——AI HOT · 微信 AI 团队 `WeKnora` 0.8.0——AIBase 9/20 · 讯飞 `AStudio` · 智谱 `AutoClaw` 与 ZCode 说明 · 千问办公 × 杭州 Token 卡 · 珠海算力券 · Tokenator 免费档——tokenator.cloud · 免费路由生态——dev.to 免费 Provider 清单 · freellm.net 核验榜（502+ 款 / 31 平台 / 243 live / 412+ 免绑卡）。

> ⚠️ 免费额度可能随时调整，请以各平台官网最新政策为准。本页所有「免费」判定均以官方接口或官方定价页为准；具体数字请自行调用官方 Usage API 或查看控制台确认。OpenRouter 免费池日内会波动，24 款 / 21 款是脚本清点时刻的快照。**第三方聚合榜（freellm.net / costgoat 等）与官方目录存在滞后与计数差，请勿单独据其做采购或宣传结论。** 「开源」指权重公开，不代表可自由商用，商用前请逐条核对许可证（尤其 Kimi、GLM、Qwen、MiniMax、Step 系列的 Model-as-a-Service 与许可条款）。**Contributor / 训练条款类免费档：不要把机密代码、个人信息或生产客户数据放进去。** Jev 是判别式模型，不生成文本；Vercel 官方示例为 AI SDK `experimental_evaluate`，接入前请先读官方文档。

---

📅 生成时间：2026-09-21 · 本页由自动化任务每日生成 · 亮色 / 暗色主题可点击 HTML 版右上角切换
