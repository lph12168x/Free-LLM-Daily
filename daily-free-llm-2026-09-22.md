# 免费大模型日报 · 2026-09-22（周二）

> 🤖 AI 每日免费情报 · 全网挖掘 · [在线版 HTML](daily-free-llm-2026-09-22.html)

**今日四个关键数字**

| 数字 | 含义 |
| --- | --- |
| **46 分** | 小米 **MiMo-V2.6** 今天发布并开源：Pro **1.02T/42B**、1M、原生全模态，**AA 智能指数全球开源第一**；Zen 同步上**全免费** `mimo-v2.6-flash-free` |
| **5 亿** | 智谱 **AutoClaw 中秋充能季**：9/21 领 2 亿 + **今天领 3 亿** GLM-5.3-Flash Token，**当天 24 点作废** |
| **24 / 10** | OpenRouter 今日零价 **24 款**（`:free` 21）连续三期零变；Zen 免费 ID **9 → 10 个** |
| **$2 / $6** | **Grok 4.7**（9/21）同价同速落地：50 万 ctx、四档推理强度，**Grok Build 浏览器免费试用** |

---

## 🔥 今日头条 · 三条主线

### ① 今日开源｜小米 `MiMo-V2.6`：**AA 46 分登顶全球开源第一**，API 不涨价，**Zen 当天挂出全免费 Flash**

**今天最值得薅的不是折扣券，是一整个新世代开源模型。** 9 月 22 日北京时间，小米正式发布并开源 **MiMo-V2.6** 系列——Pro 与 Flash 两款**原生全模态**模型，外加 Pro 的 **UltraSpeed** 超高速模式（官方标称最高 **20 倍**输出速度）与 **MiMo Desktop 正式版 + 会员订阅**。上一次更新**架构与参数量没动**，全部增益来自**把强化学习算力堆上去**。

| 项目 | 内容 |
| --- | --- |
| 🧩 规格 | **Pro**：稀疏 MoE，总参 **1.02 万亿**、每 token 激活 **420 亿**；**Flash**：**3,090 亿 / 150 亿激活**。两者均支持 **1M 上下文**与**文本 / 图像 / 视频 / 音频**四类输入，输出上限约 128K。**价格相同**——默认用 Flash，只在难题上换 Pro |
| 🏆 跑分 | AA 智能指数 **46 分**，**全球开源模型与国产模型第一**（超 Kimi K3、Qwen3.8 Max、GLM-5.3），与同期发布的 **Grok 4.7（46.4）基本同档**，离闭源顶配 Fable 5.1 / GPT-6 Astra（53.x）仍差 **约 7 分**；**每项智能指数任务约 $0.13**。细分：**DeepSWE v1.1 71.9**（Opus 5 74.0 / GPT-5.6 Sol 73.0 / Fable 5 70.0）、**AutomationBench 53.1 反超 Opus 5 的 50.3**、Agents' Last Exam 31.6 与 Opus 5 打平、OSWorld-Verified 82.0；**短板在 Terminal-Bench 4.0（34.9）与最难的竞赛编程 / 攻防安全** |
| 📺 训练是「直播做的」 | 9/17 起公开直播 6 天 RL 后训练，连 OOM、节点掉线、重跑都写在看板上：Flash 与 Pro 各 **30 步**、累计约 **75 万条轨迹**，成本分别约 **85 万**与 **262 万美元**（Pro 预算约 43.8% 花在生成候选解、12.7% 花在打分，**过半预算用于「练习与批改」**）。样本外 DeepSWE v1.1：**Flash 48.8 → 65.68、Pro 58.4 → 72.57** |
| 🎁 免费四条路 | ① **OpenCode Zen `mimo-v2.6-flash-free`：定价页四列全 Free，今天新增**；② **小米开放平台新用户注册即送免费体验额度**（`api.xiaomimimo.com/v1`，兼容 OpenAI 与 Anthropic 协议）；③ **Vercel AI Gateway 免费账号每 30 天 $5 额度**，可直调 `xiaomi/mimo-v2.6-flash`；④ **MIT 权重自部署**（HF 有 Pro-RL / Flash-RL / Distill-Qwen-9B，附技术报告 + 7,000+ RL 任务环境 + 端到端 RL 框架 + mini-harness） |

**API 价格（没涨）**：Flash **$0.14 / $0.28**（缓存命中 **$0.0028**，即 **99% 折扣**）、Pro **$0.435 / $0.87**、UltraSpeed **$4.35 / $8.70**；国内口径 Flash **¥1 / ¥2**、Pro **¥3 / ¥6** 每百万 token。官方称同等智能水平下成本约为海外同类模型的 **1/20 ~ 1/60**。

**⚠️ 旧版有一条硬截止**：**`mimo-v2.5-pro` 与 `mimo-v2.5` 将于北京时间 2026 年 10 月 21 日 10:00 下线**——这意味着 Zen 上现在的 `mimo-v2.5-free` 也在受影响范围内，**今天就把调用切到 `mimo-v2.6-flash-free`**，别等它某天 404。

**⚠️ 透明度提醒**：这次开源范围很大（权重 / 技术报告 / RL 环境 / 训练框架），但第三方指出小米**没有发布系统卡、没有具名红队合作方、也没有公布训练数据截止时间**——披露厚度弱于 OpenAI / Anthropic / Google 的旗舰发布。**合规敏感场景先自己评估，别只看开源这一点。**

### ② 今天领 3 亿｜智谱 `AutoClaw` 中秋充能季：两天合计 **5 亿 GLM-5.3-Flash Token**

这是本周**门槛最低的一笔大额度**：智谱 9/21 上线中秋活动「**AutoClaw Token 充能季**」，**所有登录用户**（不分付费免费）分两天领取，**合计 5 亿 GLM-5.3-Flash Token**。

| 项目 | 内容 |
| --- | --- |
| 🎯 第一阶段 | **9/21 领 2 亿**（约 2 万积分）、**9/22（今天）领 3 亿**（约 3 万积分）。**关键约束：赠送的 Token 当天 24:00 前作废，不能攒着**——今天就得用掉。`AutoClaw`（「澳龙」）是智谱官方桌面 AI Agent，跑 GLM-5.3-Flash，内置 50+ 技能，可对接飞书 / 企业微信 / Slack / Telegram |
| 👤 新用户另算 | 注册登录直接送 **1 亿 GLM-5.3-Flash Token**（国内标约 ¥60 / 海外约 $12）——**长期新人礼、不是限时活动**。另：把 GLM Coding Plan 接到 AutoClaw 上**限时享 150% 额度加成**；每月登录还能领积分（Lite 5,000 / Pro 1 万 / Max 2.6 万） |
| 💳 第二阶段 | **9/23 – 9/27**，每天 0 点登录领积分，仅**付费套餐会员**可领。**免费用户的有效窗口就是今天** |
| 🌩️ 背景与收口 | 福利发出当天技术社区分成两派（一派去领、一派以「谁让他偷我代码」拒用），起因是 9 月 18 日前后多名用户称编程工具 **ZCode 未经许可上传开发数据**。**今天官方把这件事收口了**：ZCode 已开源（Apache-2.0）并宣布完成安全整改——**移除 Repo Wiki 入口与本地仓库快照的生成 / 上传链路**，称数据未留存也未用于训练，**中国信通院与绿盟科技评估确认**。仓库覆盖桌面端 / 浏览器工作台 / 后端服务 / Agent CLI 等，但**没有原始提交记录、关闭了 issue 与 PR**，且注明**开源版不享受 GLM Coding Plan 相关额度活动权益** |

**读法**：额度是真的、门槛是真的低，**代价落在数据上**——这类活动的对价从来不是钱。建议划一条线：**公共项目、开源代码、非敏感任务随便跑；公司代码、客户数据、内部文档别碰**。同样的判断标准也适用于 Zen 上那几条 Contributor / Free 档。

**⚠️ 操作细节**：① 额度**当天过期**，先想好要跑什么再领，别领完就放着；② 「150% 额度加成」限时且**需手动把 GLM Coding Plan 接到 AutoClaw 上**，不是自动生效；③ 若你选择用开源版 ZCode，**注意它不继承官方产品的额度活动**。

### ③ 同价同速｜xAI `Grok 4.7`（9/21）：2.1T 参数、50 万 ctx，**Grok Build 免费试用**

昨天下午 xAI 发布 **Grok 4.7**——官方话术是「**同价同速的代际跃升**」。在「先涨价再打折」成为常态的 9 月，**新旗舰维持上一代定价**本身就是一条值得记的信息。

| 项目 | 内容 |
| --- | --- |
| 📐 规格 | 基座从 Grok 4.6 的 1.5 万亿放大到 **2.1 万亿参数**（+40%），并混入 **SpaceX 的工程数据**（星链遥测、制造记录、工程失效日志）。上下文 **50 万 token**，支持文本 + 图片输入、文本输出（不设固定上限），推理强度可选 **low / medium / high / xhigh** 四档。官方称在「需要数小时完成」的长任务上做了更长 RL，并强化了自我检查 |
| 💰 价格 | 提示词 **≤20 万 token：输入 $2 / 缓存输入 $0.50 / 输出 $6** 每百万；**>20 万 token 后为 $4 / $1 / $12**。与 Grok 4.6 完全一致。另有 **Grok 4.7 Fast**：**约 2 倍输出速度换 2 倍单价**（输入仍是 $2），**仅 Cursor 与 Grok Build 提供、不进公开 API** |
| 🏆 跑分 | AA 智能指数 **46.4**（紧邻 MiMo-V2.6-Pro 的 46.3）；**CursorBench 4.0 xHigh 46.3%**（4.6 为 40.4%、GPT-5.6 Sol Max 41.7%、Fable 5.1 Max 51.8%）；**DeepSWE v1.1 71.0%**；**EEBench 电气工程 64.0% 四家对比全场第一**；Terminal-Bench 4.0 从 20.3% 跳到 **38.0%**；GDPval Elo **1,695**（较 4.6 +90）；**Harvey Legal 法律 Agent 19.6%，是 GPT-5.6 Sol 2.5% 的约 8 倍**。短板：**Terminal-Bench 仍落后 Fable 5.1 的 57.9%**，HealthBench Professional 56.7% 落后顶尖约 4–5 个点 |
| 🎁 免费入口 | 只有一条但要紧：**`x.ai/build`（Grok Build）支持在浏览器里免费试用 Grok 4.7**——注意 **Fast 变体不含在 Build 免费档内**，且这不等于「全部 Grok 应用无限免费」。付费侧已在 **OpenCode Zen**（`grok-4.7`，$2/$6）、**OpenRouter**（`x-ai/grok-4.7`）、Vercel AI Gateway、Cloudflare、Cursor 与 xAI API 上架 |

**读法**：xAI 自己也没把 4.7 说成「打榜第一」——独立基准显示它在 GDPval 与 AA-Briefcase 上**均列第二**（第一是 Claude Fable 5.1）。它的价值在**用 $2/$6 拿到接近前沿的编码与长时办公分数**。真要用，**先在 Cursor / Grok Build 里用免费额度跑你自己的任务集**，别按官网表格下结论。

**⚠️ 两个提醒**：① **Fast 不免费、也不进公开 API**，只在 Cursor 与 Grok Build 里选；② 这类「延时发布」的模型（Musk 从 7 月底起至少推后 5 次）**上线首周服务容量通常不稳**，生产流量先留好 fallback。

---

## 🌤️ 次要更新 · 值得记一笔

### 🆓 OpenCode Zen 免费池 **9 → 10 个**：`mimo-v2.6-flash-free` 全 Free 新增

今天 Zen 的免费阵容多了一条：**`mimo-v2.6-flash-free`**（小米新旗舰 Flash，**定价页四列全 Free**）。现在带免费标记的 ID 共 **10 个**：`big-pickle`、`jev-1.13-free`、**`mimo-v2.6-flash-free`（新）**、`mimo-v2.5-free`、`ling-3.0-flash-fin-free`、`nemotron-3-ultra-free`、`nemotron-3.5-lightning-free`、`muse-spark-1.3-contributor-free`、`muse-spark-1.2-contributor-free`；`grok-4.7` 今日一并上架（**付费**）。

**⚠️ 官方文档把免费档的「代价」写得很直白，三类不一样**：① **Big Pickle / MiMo / Ling**——免费期收集的数据**可能用于改进模型**；② **Nemotron 3 Ultra / 3.5 Lightning**——NVIDIA 试用端点，明确要求**「不要提交个人或机密数据」**；③ **Muse Spark Contributor Free**——用免费换 **Meta 拿你的提示词与补全训练模型**。

另一个高频踩坑：**控制台右上角的「启用计费」按钮不要点**——免费模型**不需要绑定任何支付方式**，点了反而给自己开了付费通道。

### 🌐 新网关 `Requesty` 免费层

`router.requesty.ai/v1` 免费档提供 $0 模型：**NVIDIA Nemotron 3 Ultra / Super / Nano**、**Poolside Laguna**、**Google Gemma 4**、**Mistral Leanstral**，以及一个 Nemotron 内容安全模型。额度口径清晰：**新组织 200 请求/天 + 20 RPM（全部免费模型共享）**，**转为付费组织后升到 1,000/天 + 60 RPM**，**免信用卡**。官方文档说明这些模型「目前免费，若定价变化会在 changelog 公告」。**读法：这类网关的价值不在单个模型，而在「一个 key + 一条 base_url 就能把多家免费额度串起来」，适合做兜底或 A/B 对比。**

### 🔌 `Albedo` Agent API 免费开放

**Albedo 的 Agent API 宣布免费开放**，给到**标准配额的 10 倍、每 24 小时重置一次**。接口侧同时支持 **OpenAI / Anthropic / Responses 三种 wire format**，文档称 key 可**直接塞进 Claude Code、Codex、Copilot、Cursor、ACP**；**用 GitHub 登录即可生成具名 key**。**⚠️ 这类新服务的生命周期与稳定性都还没被验证过——可以试，不要写进生产链路，同时注意它是否要求你的代码 / 会话数据用于训练。**

### 🔎 OpenRouter：目录 **446 → 445**，零价池 **24 连续三期持平**

脚本清点（口径 `prompt == '0' 且 completion == '0'`）：**零价 24 款**（其中 `:free` 结尾 **21 款**），**连续第三期零新进、零退出**。目录总数 **446 → 445（−1）**，变动全在付费侧：新增 **`x-ai/grok-4.7`**、**`xiaomi/mimo-v2.6-flash` / `-pro` / `-pro-ultraspeed`**，以及 `nex-agi/nex-n2.5-mini` / `-pro` 的**付费版本**（原有 `:free` 两条仍在架）；下架 **7 个 `:batch` 变体**与 `anthropic/claude-opus-4`。1M 上下文免费档仍 **6 条**。**读法：今天 OpenRouter 侧没有新的「白嫖」增量，值得记的是两个新旗舰都已进场——付费版上架后，免费版通常还要等。**

### 🔌 硅基流动上线中电信 `Xing4.0-29B-A4B` 并**开放免费调用**

**29B 总参 / 4B 激活**，原生支持 **256K 上下文、可扩展至 512K**，主要面向**复杂工程、代码生成与长程 Agent 任务**；官方说明其基于**国产算力与国产框架**完成训练，并已针对 **Claude Code** 等工具适配。**这条对国内团队特别实用：不用解决网络问题、免绑卡、OpenAI 兼容，且模型本身可自部署。**

### 📊 freellm.net：目录 **503+ 款 / 31 平台 / 243 live**；免绑卡 **413+**

榜单前十：**NIM `z-ai/glm-5.3` 97**（1.3M / 131K 输出 / 40 RPM）→ `glm-5.3-flash` 96（1.3M / text+image+video+pdf）→ **OpenRouter `Ling 3.0 Flash Sante (free)` 95** → `Qwen3.8 27B (free)` 93 → Ollama Cloud `deepseek-v4-pro` 92 → `deepseek-v4-flash` 91 → **NIM `Kimi K3` 91** → LLM7.io `GLM-5.3-Flash` 90 → **OpenCode Zen `GLM-5.3` 88** → Gemini `3.8 Flash` 82。

**⚠️ 今日又抓到一处聚合滞后实证**：freellm.net 的 OpenRouter 免费池列表里**仍挂着 `stealth/union-alpha` 并标 Online**，而官方接口里它**已经整体下架**（9/18 揭晓为 unbiased.ai 的 Pareto 后即撤）。**「是否免费」一律回官方接口判定。**

---

## 🧾 今日免费入口速查 · 先进 + 量大优先

| 入口 | 能调到的先进模型 | 额度 / 价格 | 门槛 |
| --- | --- | --- | --- |
| **OpenCode Zen**（今日新增） | **`mimo-v2.6-flash-free`**（小米 MiMo-V2.6 Flash，309B/15B、**1M、全模态**）、`nemotron-3-ultra-free`（1M / 550B）、`nemotron-3.5-lightning-free`（1M）、`jev-1.13-free`、`ling-3.0-flash-fin-free`、`muse-spark-1.3-contributor-free` 等共 **10 个 ID** | **$0**；定价页 Free 行 **8 款**，均标注 **limited time** | 登录拿 Key；**别点「启用计费」** |
| **智谱 AutoClaw**（今天领 3 亿） | **GLM-5.3-Flash**（1M）；桌面 Agent 内置 50+ 技能，可对接飞书 / 企业微信 / Slack / Telegram | **9/22 登录领 3 亿 Token**（约 3 万积分，**当天 24 点作废**）；新用户另送 **1 亿**（长期） | 注册登录即可；⚠️ 免费期数据可能被用于改进模型 |
| **小米 MiMo 开放平台** | **`mimo-v2.6-pro`** / **`-flash`** / **`-pro-ultraspeed`**：1.02T/42B 或 309B/15B、**1M、文本+图像+视频+音频**、AA **46 分** | **新用户注册即送免费体验额度**；Flash $0.14/$0.28（缓存 $0.0028）、Pro $0.435/$0.87；MIT 权重可自部署 | 需小米账号；兼容 OpenAI 与 Anthropic 两种协议 |
| **Grok Build** | **`Grok 4.7`**：2.1T、50 万 ctx、四档推理强度；EEBench 64.0% 全场第一、Harvey Legal 19.6% | **浏览器内免费试用**；API $2 / $6（≤20 万 token），>20 万为 $4 / $12；**Fast 变体不免费** | `x.ai/build` 直接打开；**Fast 仅 Cursor 与 Build 可用** |
| **OpenRouter** | 零价池 **24 款**（`:free` 21）；1M 档 `nemotron-3-ultra-550b-a55b:free`、`nemotron-3.5-lightning:free`、`thinkingmachines/inkling:free`；多模态 `qwen3.8-27b:free`（262K / text+image+video） | **$0**；`:free` 约 **20 RPM / 50 RPD（全池共享）**，累计充值满 $10 后升到 **1000 RPD**；另有自动路由池 `openrouter/free`（200K） | 注册即可，**免信用卡** |
| **NVIDIA NIM** | `z-ai/glm-5.3`（1.3M，评分 **97**）、`glm-5.3-flash`（1.3M / 944K 输出）、**`Kimi K3`（1M，K3 当前主要免费入口）**、`deepseek-ai/deepseek-v4-flash-0731`（1.3M）等 100+ 款 | **$0**；**约 40 RPM 且调用量不设上限**（单看「量大」最优） | 注册 + **手机号验证**；部分端点 Trial only，**勿传敏感数据** |
| **Requesty** | Nemotron 3 Ultra / Super / Nano、Poolside Laguna、Google Gemma 4、Mistral Leanstral | **$0**；**200 请求/日 + 20 RPM**；付费组织 1,000/日 + 60 RPM | 注册即可，**免信用卡** |
| **硅基流动** | **`Xing4.0-29B-A4B`**（中电信开源，29B/4B、256K→512K）；另有 DeepSeek / Qwen / GLM 系列 | **免费调用**；新用户注册 + 实名另有赠送额度 | 国内直连；**已适配 Claude Code** |
| **国内直供** | **智谱** GLM-4.7-Flash（永久免费 200K）+ AutoClaw 新人 1 亿；**阿里 Qoder** Qwen3.8-Flash（**免费至 9/30**）；**腾讯**混元 Hy3（免费至 9/30）；**火山引擎**豆包 Lite（永久免费）；**阿里百炼** 每模型 100 万 tokens | Qoder **系数 0 + 每日 100 Credits**；火山 **200 万 Tokens/天**；百炼约 **7,000 万 tokens** 新人额度 | 多需实名；⚠️ 腾讯老混元平台 9 月底停服 |

**一句话选型**：想**今天就用上「开源第一」**，走 Zen 的 **`mimo-v2.6-flash-free`**；想在**桌面 Agent 里把额度当水电用**，今天就把 AutoClaw 的 **3 亿**领掉（**先想好跑什么**）；想要**接近前沿的编码模型但只花零头**，先在 **Grok Build** 里免费试 Grok 4.7；想要**1M + 多模态且长期免费**，走 OpenRouter 的 **`nemotron-3-ultra-550b-a55b:free`** 或 Zen 的 **Nemotron 双条**；想**批量任务省钱**，把负载排进 **DeepSeek 9/20–10/10 低谷窗口**；想**长期不担心额度**，走 **NVIDIA NIM** 或 **书生 InternLM**。**本页统计的免费券寿命已多次实测短到 2 天以内——别写死、别上生产、永远留一条 fallback。**

---

## 🔎 平台盘点 · 今日快照

### 📊 OpenRouter：445 款中 24 款零价（`:free` 21 款），连续三期零变

- 脚本清点（`pricing.prompt == '0' 且 pricing.completion == '0'`）：**24 款**；其中 id 以 `:free` 结尾的 **21 款**。**目录总数 446 → 445（−1），零价 24 → 24，零新进零退出。**
- 三条「零价但不带 `:free` 后缀」仍在：`google/lyria-3-pro-preview`、`lyria-3-clip-preview`（1M，**输出音频**）、自动路由池 `openrouter/free`（200K）。
- 1M 上下文免费档共 **6 条**。
- 端点体检（随机抽查）：`z-ai/glm-5.2:free` **status 0 / uptime 100%**、`thinkingmachines/inkling:free` 99.99%、`qwen/qwen3.8-27b:free` 99.87%、`nex-agi/nex-n2.5-pro:free` 99.68%。**四条全绿。**
- ⚠️ 免费池**日内会波动**，24 / 21 是脚本清点时刻的快照。已留 `or_models_0922.json` 供次日 diff。

**零价池流水**

| 清点日 | 零价总数 | 其中 `:free` | 关键进出 |
| --- | --- | --- | --- |
| 9/18 | 25 | 22 | 进 `deepseek-v4-flash-0731:free` + `qwen3.8-27b:free` |
| 9/20 | 24 | 21 | 出 `deepseek-v4-flash-0731:free` |
| 9/21 | 24 | 21 | 零新进、零退出 |
| **9/22（今天）** | **24** | **21** | **连续三期持平；新增全在付费侧（grok-4.7 / mimo-v2.6 三款 / nex-agi 付费版）** |

### 🏆 OpenRouter 榜单（数据截至 9/21）

- **周榜**：**1** `DeepSeek V4.1 Flash` **16.9T**（+172%）· **2** `GLM 5.3 Flash` **16.9T**（+45%）· 3 `Hy4 preview` 12.7T · 4 `DeepSeek V4 Flash 0731` 8.91T · 5 `GPT-5.6 Luna` 8.48T · 6 `MiMo-V2.5` 6.9T · **7 `Nemotron 3 Ultra (free)` 4.78T（+39%）= 前十唯一免费** · 8 `Hy3` 4.51T · 9 `DeepSeek V4 Flash 0423` 3.65T · 10 `GLM 5.3` 3.23T。
- **日榜**：`GLM 5.3 Flash` **4.36T**（+73%）第一。**月度榜**：`GPT-5.6 Luna` **50.3T**（+208%）第一，**`Nemotron 3 Ultra (free)` 18.6T 排第 10，是月度前十唯一免费**。
- **近 7 天变幅榜**：1 `DeepSeek V4 Flash 0731 (free)` 1.09T（new）· 3 `Jev 1.13` **752B** · 4 `GLM 5.3 FlashX` 49.8B · **5 `MiMo-V2.6-Pro` 17.4B（new）**。⚠️ 变幅榜是「过去 7 天」累计量，会滞后于下架动作。
- **作者份额**（week of 9/14）：**deepseek 25.4%（+9%）第一** · google 18.6% · openai 17.1%（**−30%**）· z-ai 9.4%（+31%）· qwen 6.7%（+25%）· tencent 6.4%（−14%）· anthropic 2.7% · **xiaomi 1.9%**。
- **应用榜**：**Hermes Agent 1.63T 第一** · Claude Code 678B · Kilo Code 538B · Cline 438B · pi 380B · **omp 277B（新）** · Codex 198B · OpenClaw 194B · **DeepSeek Harness 139B（新）** · OpenHands 131B。
- **AA 智能指数榜**：Fable 5.1 **53.4** · Qwen3.8 Max 53.4 · GPT-6 Astra (max) 52.7 · Opus 5 50.8 · Fable 5 49.6 · GPT-5.6 Sol (max) 47.0 · **Grok 4.7 (xhigh) 46.4** · **MiMo-V2.6-Pro 46.3** · Qwen3.8 Max (0902) 45.4 · GLM-5.3 (max) 44.8。

### 🔧 OpenCode Zen：74 → 76 款；免费 ID 10 个 vs 定价页 Free 行 8 款

- `/zen/v1/models` 返回 **76 款**（较 9/21 的 74 款 +2，零下架）。带免费标记的 ID 共 **10 个**（清单见上）。
- 官方**定价页 Free 行**是 **8 款**——**比 models 端点少 2 条**：`deepseek-v4-flash-free` 与 `muse-spark-1.2-contributor-free` 在定价页走付费价。**按平台一贯口径，以定价页为准。**
- 付费侧今日新增 **`grok-4.7`**（$2 / $6，>20 万 token 为 $4 / $12）；定价页同时列出 **`Jev 1.13` = 输入 $0.042 / 输出 Free**。
- ⏰ 旧版下线提醒：小米 `mimo-v2.5-pro` / `mimo-v2.5` 将于 **10/21 10:00** 下线。

### 🌐 免费路由生态：把「几十家免费额度」聚成一条链

- **今天新增的两条**：**Requesty**（200 请求/日 + 20 RPM，免绑卡）与 **Albedo Agent API**（10× 配额、24h 重置、三协议）。
- **一直在架但常被忽略的**：**OrcaRouter**（Hacker 档永久免费，免费阵容轮换 GLM-5.3 Flash / DeepSeek V4 Flash / 腾讯 Hy3 / 自家 OrcaVerify Text 1.0，**10 RPM / 50 RPD**，累计付费满 $20 后升到 800 RPD，**零加价**）；**OmniRoute**（MIT，单端点接 **260+ 家**，约 **16 亿免费 token/月**）；**Free Claude Code**（本地代理，覆盖 **27 家**）；**Pollinations**（**免 key 即用**）；**美团 LongCat**（**每天 5,000 万 token**）；**Cerebras**（**每天 100 万 token**）；**Cloudflare Workers AI**（每天 1 万 neurons）；**OVHcloud AI Endpoints**（**匿名免注册 9 款**，2 RPM）。
- **组合建议**：**主力**用一个稳的（NIM / 硅基流动），**兜底**用一个常驻免费的（LongCat / InternLM / Requesty），**临时**用免 key 的（Pollinations）——**别把所有调用压在一个免费档上**。

---

## 📅 到期日历 · 别踩空

**眼前这一周**

- **9/22（今天）** — **智谱 AutoClaw 最后一次全员发放：登录领 3 亿 Token（当天 24 点作废）**；**小米 MiMo-V2.6 发布并开源**；DeepSeek 低谷价窗口第 3 天
- **9/23（00:00）** — **讯飞 AStudio 星火 X2.5 限免结束**；**WorkBuddy / CodeBuddy 的 DeepSeek V4.1 Flash 0.03× 折扣结束**；**AutoClaw 进入付费会员专属阶段**
- **9/24** — **文心快码 Comate** 测试版限免结束；**字节 TraeCode Seed 系列 1 折**结束
- **9/25** — **Jev 在 Vercel AI Gateway 的免费促销结束**

**9 月下旬及以后**

- **9/27** — AutoClaw 中秋充能季第二阶段结束（付费会员专享）
- **9/30** — **阿里 Qoder Qwen3.8-Flash 免费用结束**；**腾讯 Hy3 / 文心 4.0 免费期结束**；Merge Gateway GLM-5.3-Flash 1 折结束；**腾讯老混元平台停服**
- **10/10** — **DeepSeek 低谷价窗口结束**；**腾讯混元 Hy4 preview**（老用户夜间免费）结束
- **10/14** — 珠海算力券申报截止（企业向，每年最高 200 万）
- **10/15** — **阶跃 Step 5 Preview 释放完整 BF16 权重**（许可证待公布）
- **10/21（10:00）** — **小米 `mimo-v2.5-pro` / `mimo-v2.5` 正式下线**，**Zen 的 `mimo-v2.5-free` 受此影响**
- **10/31** — WorkBuddy 学生积分截止 · **11/7** MiniMax 开放平台 M3 / M2 免费试用到期 · **12/31** 腾讯云 TokenHub / 华为云码道 / 移动云 MoMA 截止

---

## 🧭 今天该怎么动

**① 现在就做（5 分钟内）**

- **把 Zen 的默认模型换成 `mimo-v2.6-flash-free`**——今天刚上架、四列全 Free，而且旧版 `mimo-v2.5-*` 有 10/21 硬下线日期，**现在切等于零成本升级，还顺手躲开一次未来的 404**。
- **智谱用户立刻去 AutoClaw 领今天的 3 亿 Token**——**当天 24 点作废，先想好要跑什么再领**（浏览器自动化、批量表格处理、报告生成最划算）。

**② 今天之内**

- **用你自己的任务集验证 MiMo-V2.6**：把「长上下文 + 多轮工具调用」的真实任务分别丢给 `mimo-v2.6-flash-free` 与你现在的主力，对照**完成率、返工次数、单任务成本**。
- **去 `x.ai/build` 免费摸一下 Grok 4.7**：一个真实 bug 修复 + 一份长文档任务，**三个任务就够判断要不要换默认**。
- **Requesty 注册一个免费 key**（免绑卡，2 分钟），挂在兜底位置。

**③ 本周之内**

- **做一次「免费档数据条款」清点**：把在用的每条免费通道按「是否可用于训练 / 是否仅限试用 / 是否要求付费资格」打标签——Zen 的 **Nemotron 两条明确要求勿传机密**、**Muse Spark 换训练权**、**AutoClaw 免费期数据可用于改进模型**，这三类别混在一起用。
- **配好兜底线**：**NVIDIA NIM**（40 RPM 不限量）+ **书生 InternLM**（1.8 亿 tokens/月、无到期日、免信用卡）+ **硅基流动 `Xing4.0-29B-A4B`**（国内直连、已适配 Claude Code）。
- **别把「在架免费」当稳定**：本页统计的 `:free` 券寿命已多次实测短到 2 天以内，任何写死单条 `$0` 通道的地方，本周加一条可切换的备线。
- **盯两个日期**：**10/15** 阶跃 Step 5 权重开源（许可证是变量）、**10/21** 小米 MiMo-V2.5 全线下线。

---

## 📋 数据来源

OpenRouter `/api/v1/models`（9/22 脚本清点，445 款中 24 款 $0 / 21 款 `:free`，已留 `or_models_0922.json`）· OpenRouter Rankings（数据截至 9/21：周榜 / 日榜 / 月榜 / 近 7 天变幅榜 / 作者份额 week of 9/14 / Apps 榜 / AA 智能指数榜）· 小米 `MiMo-V2.6`（9/22 发布并开源；AA 46、DeepSWE v1.1 71.9、AutomationBench 53.1、OSWorld-Verified 82.0；6 天 Live RL 85 万 / 262 万美元 × 30 步；Flash $0.14/$0.28、Pro $0.435/$0.87；MIT 权重 + 技术报告 + 7,000+ RL 环境 + RL 框架；MiMo Desktop 与会员；旧版 10/21 下线）——小米技术官方发布 / 小米 MiMo 开放平台文档 / 太平洋电脑网 / Artificial Analysis / Vercel AI Gateway 模型页 · 智谱 `AutoClaw` 中秋「Token 充能季」（9/21 领 2 亿、9/22 领 3 亿当天作废；9/23–27 付费会员专属；新用户 1 亿长期新人礼；150% 加成；每月登录积分 Lite 5,000 / Pro 1 万 / Max 2.6 万）· 智谱 `ZCode` 开源与安全整改（移除 Repo Wiki 入口与本地仓库快照上传链路，中国信通院 + 绿盟确认，Apache-2.0，开源版不享受 GLM Coding Plan 额度活动）· xAI `Grok 4.7`（9/21 发布：2.1T、50 万 ctx、SpaceX 数据；$2/$6；Fast 仅 Cursor 与 Grok Build；CursorBench 4.0 xHigh 46.3%、DeepSWE 71.0%、EEBench 64.0%、Terminal-Bench 4.0 38.0%、GDPval 1,695、Harvey Legal 19.6%；x.ai/build 免费试用）——x.ai 官方 / Decrypt / kingy.ai · OpenCode Zen `/zen/v1/models`（76 款）与官方定价页 · 中电信 `Xing4.0-29B-A4B` 上架硅基流动并开放免费调用 · 新网关 **Requesty** 免费层 · **Albedo** Agent API 免费开放——AGI Hunt · 免费路由生态——dev.to 免费 Provider 横评 9/21 · freellm.net 核验榜（503+ 款 / 31 平台 / 243 live / 413+ 免绑卡，榜首 NIM `z-ai/glm-5.3` 97）。

> ⚠️ 免费额度可能随时调整，请以各平台官网最新政策为准。本页所有「免费」判定均以官方接口或官方定价页为准；具体数字请自行调用官方 Usage API 或查看控制台确认。OpenRouter 免费池日内会波动，24 款 / 21 款是脚本清点时刻的快照。智谱 AutoClaw 赠送 Token **当天 24 点作废**，请先规划任务再领取。**第三方聚合榜（freellm.net / costgoat 等）与官方目录存在滞后与计数差，本页已标注一处今日实证（stealth/union-alpha），请勿单独据其做采购或宣传结论。** 「开源」指权重公开，不代表可自由商用，商用前请逐条核对许可证（尤其 Kimi、GLM、Qwen、MiniMax、Step、MiMo 系列的 Model-as-a-Service 与许可条款）。**Contributor / 试用 / 训练条款类免费档：不要把机密代码、个人信息或生产客户数据放进去。** Grok 4.7 的 Fast 变体不在公开 API、也不含在 Grok Build 免费档内，接入前请先读官方文档。

---

📅 生成时间：2026-09-22 · 本页由自动化任务每日生成 · 亮色 / 暗色主题可点击 HTML 版右上角切换
