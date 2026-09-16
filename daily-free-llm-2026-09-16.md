# 免费大模型日报 · 2026-09-16（周三）

> 🤖 AI 每日免费情报 · 全网挖掘 · [在线版 HTML](daily-free-llm-2026-09-16.html)

**今日四个关键数字**

| 数字 | 含义 |
| --- | --- |
| **23** | OpenRouter 今日零价模型 23 款（`:free` 20 款），新增 `z-ai/glm-5.2:free` |
| **4.4 个月** | Mozilla：美国前沿闭源与中国头部开源的能力差距已缩到约 4.4 个月 |
| **9B** | 紫东太初 ZDTaichu5.0-9B 开源，9 项空间理解基准拿下 8 项组别第一 |
| **6 条** | 今天可直接接上的「$0 / 极低价」API 通道（Zen · OpenRouter · OrcaRouter · Nous · Command Code · OVHcloud） |

---

## 🔥 今日头条 · 三条主线

### ① 免费池｜OpenRouter 上新 `z-ai/glm-5.2:free`：零价模型 22→23 款

本期脚本清点（`:free` 后缀 且 `pricing.prompt == '0'`）：**免费池 20 款**（9/15 为 19 款），实时**零价模型总数 23 款**（9/15 为 22 款），**净增 1、零下架**。新增的唯一一条是智谱旗舰 `z-ai/glm-5.2:free`——这款在 OpenCode Zen 上还挂着 **$1.40 / $4.40** 的付费价，现在 OpenRouter 免费区可以直接调。

- **口径打架**：接口元数据里 `z-ai/glm-5.2:free` 的 **context_length = 32,768**，但模型简介写的是「**1M-token context window**」。**以接口元数据为准，按 32K 规划**，别拿它跑长上下文批处理。
- **三个「零价但非 `:free`」**：`google/lyria-3-clip-preview`、`google/lyria-3-pro-preview`（各 1M 上下文、**输出音频**，音乐生成）与 `openrouter/free`（200K，官方自动路由免费池）。这三条不被 `:free` 统计口径覆盖，容易漏看。
- **目录净变化**：全量模型 **445 → 443**：新增 1 条（glm-5.2:free），下架 3 条 `:batch` 批处理变体（`google/gemma-4-31b-it:batch`、`openai/gpt-oss-20b:batch`、`thinkingmachines/inkling-small:batch`）。
- **1M 免费档**：免费池里 1M 上下文仍是 **4 款**：`nvidia/nemotron-3-ultra-550b-a55b:free`、`nvidia/nemotron-3.5-lightning:free`、`thinkingmachines/inkling:free`、`thinkingmachines/inkling-small:free`。

**OpenRouter 周榜（截至 9/15）里的免费信号**

| 指标 | 数值 |
| --- | --- |
| DeepSeek V4.1 Flash 本周 tokens | **8.02T**，空降周榜第 5（标记 new） |
| Nemotron 3 Ultra (free) | **3.41T**，周榜第 9，**前十唯一免费模型** |
| Hermes Agent（Nous 开源 Agent） | **1.61T**，应用榜第一，远超 Claude Code 的 791B |

### ② 为什么｜Mozilla《State of Open Source AI》：中美开源差距缩到 4.4 个月

9/15 发布的这份报告，是今天最该被记住的一条——它把「要不要用免费/开权重模型」这个问题，从情绪争论换成了**成本曲线的算术题**。

**报告口径：美国前沿闭源模型 与 中国头部开源模型 的能力差距已缩小到约 4.4 个月；Kimi K3 在 Artificial Analysis Intelligence Index 上仅落后 Anthropic 的 Claude Fable 5 三分，而成本约为后者的 30%。**

- **核心建议**：报告明确建议**多数组织把开源模型作为日常工作的默认选项**；只有在**专家级专业工作、高强度检索、长上下文**这三类场景，才值得付闭源模型的差价。
- **为什么值得看**：这是「中国开源模型」第一次**以成本曲线的方式影响全球选型**。如果企业按这个逻辑采购，闭源模型的定价权会被从下游撬动——对每天盯着免费额度的我们，这是最硬的论据。
- **同日佐证**：同一天 **Fireworks 上线 DeepSeek-V4.1-Flash**：DeepSWE **74.34% pass@1**、每任务 **$0.43**，与 GPT-6 Astra 落在同一精度区间但成本约 **1/15**；**DeepSeek-V4.1-Flash (Max) 进入 Agent Arena 开源模型第 3**，每任务中位成本 **$0.07**。

### ③ 自部署｜开源三连发：紫东太初 9B 空间模型 + 小红书 Iris + 硅基流动 Hy4 preview

今天「免费能用」的另一半，是**权重直接给你、算力自备**这条路。9/15 一天里国内至少三组开源落地，而且都不再是「又一个大聊天模型」，各自卡在一个具体赛道上。

- **🧠 ZDTaichu5.0-9B** — 紫东太初（中科院自动化所 / 武汉人工智能研究院体系）：参数约 **9B**，支持单图、多图、**长序列视频**与**任意分辨率**视觉输入，主打真实物理场景的**空间感知、跨视角变换、具身任务规划**。**9 项国际基准拿下 8 项组别第一**。权重、**数据生产方案与训练过程一并开源**（Hugging Face / ModelScope / GitHub）。9B 意味着可以端侧、可以在机器人计算单元上跑。
- **🔎 小红书 Iris** — AllSpark 团队开源 **Search Agent** 模型 Iris，**35B 与 397B 两个版本**同量级成绩领先，权重与评测代码已公开，数据与训练配方将陆续公布。
- **⚡ 硅基流动 Hy4 preview** — 官方上线开源模型 **Hy4 preview**：**770B 总参数、1M 上下文**，可直接在硅基流动平台调用。
- **🎙️ 顺带** — 阶跃星辰 9/15 发布 **StepAudio 3 系列五款**语音模型（Realtime / ASR / TTS / Gen / Music）：Realtime 在 AA Conversational Dynamics 榜 **98.9% 全球第一**，ASR 非流式错误率 **1.7% 并列第一**。语音赛道的免费额度窗口通常很短，值得留意。

---

## 🌤️ 次要更新 · 值得记一笔

### 🔌 你点名的两家：Nous 与 Command Code 的真实免费边界

**Nous Research**：真正免费的是 **Hermes Agent（MIT）**，GitHub **244,938 stars**（9/13 数据），Agent 本身零成本。但「**Nous Portal 免费档（$0）只有免费模型**」，付费从 Plus **$20**（给 $22 credits）/ Super **$100** / Ultra **$200** 起，各档都多给 10% credit。Portal 的卖点是**一个订阅打包 300+ 模型 + Tool Gateway**（网页搜索、抓取、图像生成、浏览器自动化、语音），按次从同一余额扣。**Hermes Cloud** 常驻实例需要 $2 credit 起，Medium 实例运行 $0.56/天、停止 $0.03/天，模型与工具费另计。

### 💵 Command Code Go：$1/月 换 $10 credits，约 15000 次请求

订阅分四档 **Go / GOAT / Pro / Max**。**Go 档 $1/月（约 ¥7）给 $10 额度，官方估算约 15,000 次请求**，是目前终端编码 agent 里最便宜的入口。**关键限制**：Go 档**只能在官方 CLI 里用**（`npm i -g command-code`）；想用 OpenAI 兼容的 Provider API 必须升级到付费的 **Provider 计划**，否则上游直接返回 `upgrade_required`。社区有非官方桥接把 Go 档接到 OpenCode / Claude Code（走 `/alpha/generate`），但**官方明确说这不是公开 API、可能随时封号**——要用就自己承担风险。

### 🧭 OrcaRouter 免费四路：3 个直给 + 1 个自动池（9/15 复核）

免费名单：`z-ai/glm-5.3-flash-free`、`deepseek/deepseek-v4-flash-free`、`tencent/hy3-free`，外加 `orcarouter/free` 自动路由池（声明这个模型名，它自己从免费名单里挑）。三条都是 **$0 每 token**，没有试用倒计时。**硬门槛**：免费层统一 **10 次/分钟、50 次/天**；账户**累计付费满 $20 后升到 20 次/分钟、800 次/天**；另外**要求绑定有一定历史的 GitHub 账号**（新注册小号基本要等）。还有一个「免费优先」开关，免费额度扛不住才动钱包。

### 🇪🇺 OVHcloud AI Endpoints：匿名免注册就能调的 9 款免费模型

欧洲托管的免费推理端点，**匿名档连注册都不需要，直接发请求**（2 RPM），注册后限额更高，**不要求信用卡、不要求手机号**。9 款模型在线，上下文 32K–262K，覆盖 `Qwen3.5-397B-A17B`、`Qwen3-Coder-30B-A3B-Instruct`（262K）、`qwen2.5-vl-72b-instruct`、`Mistral-Small-3.2-24B`、`meta-llama-3_3-70b` 等，兼容 OpenAI SDK。代价是**匿名档速率极低且有冷启动（首个请求 5–10s）**，欧洲以外延迟偏高——适合当「第三条 fallback」，不适合当主力。

### ⚠️ Meta One 全球上线：AI 用量正式进订阅包，免费边界在收窄

9/15 起 **Meta One 订阅全球上线**，分个人 / 创作者 / 企业多档，把 Facebook、Instagram、WhatsApp 的高级功能与**额外的 Meta AI 使用量**打包，并计划逐步纳入 Edits、AI 眼镜。Meta 强调 App 与 Meta AI 的**核心体验仍然免费**，单独订阅也保留。这是把 AI 从「免费功能」改造成「收费商品」的结构性动作——对靠免费额度吃饭的人，是**需要提前记一笔的方向性变化**。

### 🎁 Inception Mercury 2：新号一次性 1 亿 tokens，免卡（9/15 复核仍在）

每个**新 Inception 账号**可领**一次性 1 亿 API tokens**，**不需要任何支付信息**，额度在 Mercury 2 与 Mercury Edit 2 之间**共享**（不是每模型各给）。Mercury 2 支持推理、工具调用与结构化输出，兼容 OpenAI API。免费档速率上限写得很清楚：**1000 请求/分钟、100 万输入 tokens/分钟、10 万输出 tokens/分钟**。额度用完后单价 $0.25 / $0.025（缓存输入）/ $0.75 per 1M。

### 📊 freellm.net 核验榜：478+ 模型 / 31 平台 / 332 免信用卡

15 个聚合来源里唯一逐条 live 验证的：本次快照 **478+ 模型、31 家平台、332 款免信用卡**，其中 **235 款通过实时 API 验证**（9/15 为 479+，属日内波动）。榜首仍是 **NVIDIA NIM 的 `z-ai/glm-5.3-flash`（96 分，1.3M 上下文，636.4M/周）**；其后是 Ollama Cloud 的 `deepseek-v4-pro`（93）、`deepseek-v4-flash`（92）、NVIDIA NIM 的 Kimi K3（91）。榜单前列的 `Ling 3.0 Flash VL / Sante (free)` 周用量分别是 **268.2B / 348.3B**。

### 🧰 一个新发现的额度追踪站：china-ai-arbitrage.xyz

社区维护的「AI Token 免费领取」地图，首页按平台列免费额度入口，当前标记 **29 个在领 + 2 个即将上线**（含 NVIDIA NIM、阿里云百炼、AMD Token Factory、B.AI、百度千帆、Cerebras、Cline、**Command Code**、DeepSeek、DevEco Code、Freebuff、Groq、讯飞星火、Kimi、Mistral、Modal、ModelScope、Nebius Token Factory、OpenRouter、Ox Alpha、Peezy、商汤 Token Plan、硅基流动、腾讯混元、TokenRhythm、TokenRouter、火山引擎、xAI Grok、智谱 AI，即将：StepFun 阶跃星辰）。可当成 freellm.net 之外的第二信源交叉核对。

---

## 🧾 今日免费入口速查 · 先进 + 量大优先

按「能直接调、模型够先进、额度够大」三条筛过一遍：

| 入口 | 能调到的先进模型 | 额度 / 价格 | 门槛 |
| --- | --- | --- | --- |
| **OpenRouter**（今日 +1） | 免费池 **20 款**，含 `nemotron-3-ultra-550b-a55b:free`（1M）、`thinkingmachines/inkling:free`（1M）、`ling-3.0-flash-vl:free`（视觉+视频）、`nex-n2.5-pro:free`（262K）；**今日新增 `z-ai/glm-5.2:free`（32K）** | **$0**；`:free` 约 **20 RPM / 50 RPD**，累计充值满 $10 后升到 **1000 RPD** | 注册即可，免信用卡 |
| **OpenCode Zen**（开权重） | `nemotron-3-ultra-free`（1M）、`nemotron-3.5-lightning-free`（1M）、`mimo-v2.5-free`、`ling-3.0-flash-fin-free`、`muse-spark-1.3-contributor-free`、`big-pickle`（隐身模型） | **$0**；定价页 Free 行 **6 款，全部 limited time**；同页 **GPT-5.6 Sol 五折到 9/18** | 登录拿 Key，客户端内直接选 |
| **OrcaRouter**（聚合） | `z-ai/glm-5.3-flash-free`、`deepseek/deepseek-v4-flash-free`、`tencent/hy3-free`，加 `orcarouter/free` 自动路由池 | **$0**；**10 RPM / 50 RPD**，累计付费满 $20 → **20 RPM / 800 RPD** | 需绑定**有一定历史的 GitHub 账号** |
| **Nous Portal**（Agent 免费） | Hermes Agent（MIT，244,938 stars）可白嫖；Portal 免费档只给**免费模型**；付费档打包 **300+ 模型 + Tool Gateway** | **$0**（免费档）→ Plus **$20**（$22 credits）/ Super $100 / Ultra $200 | Nous 账号；Hermes Cloud 需 $2 credit 起 |
| **Command Code**（极低价） | 官方 CLI 可选的编码模型目录（Go 档） | **$1/月**（约 ¥7）给 **$10 credits ≈ 15,000 次请求**；Provider API 需升级付费档 | `npm i -g command-code`；Go 档仅 CLI |
| **OVHcloud**（免注册） | `Qwen3.5-397B-A17B`、`Qwen3-Coder-30B-A3B`（262K）、`qwen2.5-vl-72b`、`Llama-3.3-70B`、Mistral 系，共 9 款 | **$0**；**匿名档 2 RPM**（注册更高），免信用卡免手机号 | 匿名直连，连注册都不用 |
| **NVIDIA NIM** | `z-ai/glm-5.3-flash`（1.3M，榜分 96）、`moonshotai/kimi-k3`（1M）、`deepseek-ai/deepseek-v4-flash-0731`（1.3M / 944K 输出） | 免费档**最高 40 RPM**，部分模型 TPD 不设限 | 需邮箱 + **手机号验证** |
| **Google AI Studio** | Gemini 3.8 / 3.7 / 3.6 / 3.5 Flash（1M，多模态） | **15 RPM / 1500 RPD**（Flash-Lite 500 RPD） | Google 账号，免信用卡 |
| **自部署**（今日开源） | **ZDTaichu5.0-9B**（空间/具身）、**小红书 Iris** 35B / 397B（Search Agent）、**Hy4 preview** 770B / 1M | 权重 **$0**，成本=自己的算力 | Hugging Face / ModelScope 下载 |

---

## 🔎 平台盘点 · 今日快照

### 📊 OpenRouter：443 款中 23 款零价（`:free` 20 款），净增 1

- 脚本清点 `pricing.prompt == '0' 且 pricing.completion == '0'`：**23 款**（9/15 为 22）；其中 id 以 `:free` 结尾的 **20 款**（9/15 为 19）。
- **新增 1 条**：`z-ai/glm-5.2:free`（元数据 32,768 上下文、纯文本）。**无下架**。
- 另有两个别名情况需注意：`lyria-3-clip-preview` / `lyria-3-pro-preview` 是**音频输出**模型（1M），`openrouter/free` 是官方自动路由池（200K），三者零价但不带 `:free`。
- 目录总数 **445 → 443**，减少的 3 条全是 `:batch` 批处理变体；1M 上下文的免费模型仍为 **4 款**。
- ⚠️ 免费池**日内会波动**，23/20 是脚本清点时刻的快照，不代表全天稳定值。已留 `or_models_0916.json` 供次日 diff。

### 🔧 OpenCode Zen：70 款 / 8 个免费 ID，零增减；GPT-5.6 Sol 五折到 9/18

- `/zen/v1/models` 返回 **70 款**，与 9/15 一致。
- 带免费标记的 ID 共 **8 个**：`big-pickle`、`deepseek-v4-flash-free`、`mimo-v2.5-free`、`ling-3.0-flash-fin-free`、`nemotron-3-ultra-free`、`nemotron-3.5-lightning-free`、`muse-spark-1.3-contributor-free`、`muse-spark-1.2-contributor-free`。
- 官方**定价页**的 Free 行仍是 **6 款**（Big Pickle / MiMo-V2.5 / Ling 3.0 Flash Fin / Nemotron 3 Ultra / Nemotron 3.5 Lightning / Muse Spark 1.3 Contributor），**全部 limited time 且无到期日**。
- 两个官方文档页名单依旧不一致（models 端点 8 个 vs 定价页 6 个）——**以定价页为唯一可信源**。
- ⏰ 同页提示：**GPT 5.6 Sol 价格含 50% 折扣，到 2026-09-18 结束**（付费模型，但窗口很短）。
- ⚠️ Muse Spark 1.3 Contributor Free 的对价写得很直白：**用你的 prompt 和 completion 去训练 Meta 未来的模型**换折扣。

### 🗺️ freellm.net：478+ 模型 / 31 平台 / 332 免信用卡（235 款 live 验证）

- 快照日期 **2026-09-15**；**478+ 模型、31 家平台、332 款无需信用卡**，其中 **235 款通过实时 API 验证**（9/15 日报曾记 479+，属日内波动）。
- 榜首：**NVIDIA NIM / `z-ai/glm-5.3-flash`**，96 分，1.3M 上下文 / 131K 输出，最高 40 RPM，636.4M/周。
- 其后：Ollama Cloud `deepseek-v4-pro`（93）、`deepseek-v4-flash`（92）、NVIDIA NIM `Kimi K3`（91，1M）、`deepseek-v4-flash-0731`（90，1.3M / 944K 输出）。
- OpenRouter 免费模型里周用量最高的是 `Ling 3.0 Flash Sante (free)` **348.3B/周** 与 `Ling 3.0 Flash VL (free)` **268.2B/周**。
- 📌 交叉核对提醒：本期新增的 `z-ai/glm-5.2:free` 尚未出现在 freellm.net 榜上，**聚合站滞后于官方接口是常态**，以脚本清点为准。

---

## 📅 到期日历 · 别踩空

**眼前这一周**

- **9/17** — GPT-6 Astra Challenge 投稿截止（前五名各 1 万美元额度）
- **9/18** — OpenCode Zen **GPT-5.6 Sol 50% 折扣到期**
- **9/20** — 智谱「Flash × ZCode」夜间畅用（23:00–09:00）结束
- **9/30** — 云知声 U2-Flash 1 亿 Tokens 活动与六折价结束

**9 月下旬及以后**

- **9/30** — 腾讯 **Hy3 免费期**结束（OrcaRouter 的 `tencent/hy3-free` 同步观察）；**Merge Gateway GLM-5.3-Flash 1 折**结束；阿里云 AI 焕新季满减券截止
- **10/10** — WorkBuddy Hy4 preview 新用户「首开享 14 天」的最后首开日
- **10/14** — **Bolt Forge 50× 用量预览期结束**（Forge 本身继续保留）
- **12/31** — 腾讯云 TokenHub / 华为云码道「码力续航计划」/ 移动云 MoMA 活动截止

---

## 🧭 今天该怎么动

**① 现在就做（5 分钟内）**

去 **OpenRouter 把 `z-ai/glm-5.2:free` 加进你的 fallback 链试一次**——今天唯一的新增免费项，先确认它在你账号上的实际响应与限速；但**注意它只有 32K 上下文**，别往里塞长文档。同时去 **OVHcloud AI Endpoints 匿名档**发一个 `Qwen3.5-397B-A17B` 的请求——**连注册都不用**，2 RPM 虽然慢，但作为「第三条 fallback」的边际成本是零。

**② 今天之内**

**想扩量的**：今天性价比最高的一组是 **OrcaRouter 免费四路**——GLM-5.3-Flash、DeepSeek V4 Flash、腾讯 Hy3 加上自动池，全是 $0，代价只是 10 RPM / 50 RPD 和有历史的 GitHub 账号。**想极致省钱的**：**Command Code Go**，$1/月约 15000 次请求，但记住**只能在官方 CLI 里用**，别指望 Provider API。

**③ 本周之内**

1. 把 **Mozilla 报告的结论落到选型上**：日常任务默认走开权重 / 免费档，只在**专家级专业工作、高强度检索、长上下文**三类场景留闭源——这份报告是目前最有说服力的内部说服材料；
2. 把 **ZDTaichu5.0-9B** 拉下来试一下空间 / 具身场景，9B 的可端侧部署量级是它真正的价值，**顺带把它的数据生产方案存一份**（这类全栈开源很少见）；
3. 提醒自己：**Inception 的 1 亿 tokens 是一次性额度**，别当长期池子用；**Muse Spark 1.3 Contributor Free 的代价是训练数据授权**，涉密或商业敏感的 prompt 不要走这两个通道。

---

**数据来源**：OpenRouter `/api/v1/models`（9/16 脚本清点，443 款中 23 款 $0 / 20 款 `:free`）· OpenRouter Rankings（截至 9/15 周榜与 Apps 榜）· OpenCode Zen `/zen/v1/models` 与官方定价页 · Mozilla《State of Open Source AI》(2026-09-15, stateofopensource.ai) 与 Ars Technica 独家报道 · 紫东太初 ZDTaichu5.0-9B 官方 Blog 与 Hugging Face / ModelScope / GitHub（9/15 开源）· 阶跃星辰 StepAudio 3 系列官方发布（9/15）· 小红书 AllSpark Iris 开源公告 · 硅基流动 Hy4 preview 上线公告 · Fireworks DeepSeek-V4.1-Flash 上线说明与 Agent Arena 开源榜 · freellm.net 核验榜 · Nous Research 官方 Hermes 定价页与 Hermes Atlas 指南 · Command Code 官方档位说明与社区桥接仓库 · OrcaRouter 官网优惠活动页（9/15 复核）· OVHcloud AI Endpoints 官方端点与 freellm.net 提供商页 · Inception 官方定价与额度说明（9/15 复核）· Meta 官方公告《Introducing Meta One subscription service》(9/15) · china-ai-arbitrage.xyz 免费额度地图 · costgoat.com 与 aimcp.info 的 OpenRouter 免费模型追踪 · AI HOT 每日精选 2026-09-16。

⚠️ 免费额度可能随时调整，请以各平台官网最新政策为准。本页所有「免费」判定均以官方接口或官方定价页为准；涉及额度的具体数字请自行调用官方 Usage API 或查看控制台确认。OpenRouter 免费池日内会波动，23 款 / 20 款是脚本清点时刻的快照，不代表全天稳定值。「开源」指权重公开，不代表可自由商用，商用前请逐条核对许可证（尤其 Kimi、GLM、MiniMax 的 Model-as-a-Service 条款）。

📅 生成时间：2026-09-16 · 本页由自动化任务每日生成
