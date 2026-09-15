# 免费大模型日报 · 2026-09-15（周二）

> 🤖 AI 每日免费情报 · 全网挖掘 · [HTML 版](daily-free-llm-2026-09-15.html) | [返回目录](index.html)

**今日速览**：Bolt Forge 上线——开权重模型（GLM / DeepSeek / Kimi）给个人 Pro 用户 50 倍用量、免费到 10/14（代价是共享匿名 build session）· 云知声 U2-Flash 今日发布：266B 总参只激活 10B，DeepSWE v1.1 拿 64.6，9/15–9/30 新老用户各领 1 亿 Tokens · GPT-6 Astra 定价 $10/$50 反而验证开权重够用（V4.1 Flash 每任务 $0.07）· xAI Grok Build 开源免费 · 智谱夜免实测速度只有 DeepSeek 的 1/3

---

## 🔥 今日头条

### 1. 🎁 Bolt Forge 上线：开权重模型吃到 50 倍用量、免费到 10/14——代价是把 build session 交给 Arcee AI 训练

9/14 Bolt.new 上线 **Bolt Forge**，一个**只跑开权重模型**的第三个 agent（与 Standard / Max 并列）。

- **额度**：每个**个人 Bolt Pro 套餐**在 Forge 上获得**最高 50 倍用量、零额外费用，有效期到 2026-10-14**；用量走**单一每月额度条、无日限额**、100% 硬停。
- **模型阵容**：默认 **GLM 5.3 Flash**；并列可选 **GLM 5.3**；实验位放 **Kimi K3** 与 **DeepSeek v4 Pro**。注意 **Kimi K3 与 DeepSeek v4 Pro 的额度消耗比 GLM 系更快**。
- **能力差多少**：Bolt 自家 **Bolt Build Index**——Forge 开权重堆 **92.2** vs 顶配付费模型（Claude Opus 5）**101.0** → 官方口径 **91% 能力平价**。差 9 分，换 50 倍用量。
- **真实对价**：切进 Forge 时**每次弹一次一跳确认**——你 opt-in 共享**匿名化** build session（去密钥、去个人信息），交给 **Arcee AI**（美国开权重实验室，Trinity 系列作者，签数据处理协议）训练一个**万亿参数级**开权重模型，训练出的权重**公开发布、人人可下载**。Standard / Max 永不用你的数据训练；**Teams / Enterprise 完全排除在 Forge 与数据采集之外**。
- **限制（先看再切）**：① 需要**个人 Bolt Pro 订阅**，不是零门槛；② Forge 仍是**实验特性**，官方建议**先把正经项目复制一份再切**；③ **暂不支持 PDF 上传**；④ 10/14 后 **50× 额度结束**，Forge 本身继续作为常态化开权重 agent 存在。
- **为什么值得记**：这是「**免费的真实对价 = 数据**」的又一实证（前有 Meta Muse Spark 1.3 Contributor Free）。更值得注意的是：**开权重模型第一次被做成产品级 agent 的默认候选**，而不是 BYOK 玩票路线。Bolt 顺带给了个论点——AI 推理成本 18 个月降了约 280 倍，才让这种额度在财务上成立。

⚠️ 别只看「50×」：**要用 Pro 订阅换，且要以匿名 build session 换**。有代码保密要求、或工作区属于 Teams / Enterprise 的，直接跳过。另外 Bolt 没有公布 50× 的**绝对额度上限**，重度使用前先在自己账号里看一次实际数字。

### 2. 🆕 云知声 U2-Flash 今日（9/15）发布：266B 总参只激活 10B，DeepSWE v1.1 拿 64.6，新老用户各领 1 亿 Tokens

港股 **09678** 今日发布自愿公告并同步上线模型：**U2-Flash**——基于 U2 通用基座强化后训练的「高密度智能」主力模型，**盘中一度涨超 9%**。最关键的一条不是跑分，而是额度：**2026-09-15 至 09-30，新用户注册与老用户均可领取 1 亿 Tokens 体验额度**，同时 API 限时六折。

- **规格**：稀疏 MoE，**总参约 266B、单次推理仅激活约 10B（不足总参数 4%）**；**TTFT 平均控制在 3 秒以内**，峰值输出吞吐最高 **300 tokens/s**；具备**隐式思考与连续状态推理**，推理强度封装为**四档可控接口**（高强度档输出完整可读推理链）。已完成**主流国产算力平台**系统性适配，部分场景接近 NVIDIA GPU 方案。
- **跑分（官方自测同图对比）**：**DeepSWE v1.1 64.6**（较前代 U2 翻倍，超 GLM-5.3-Flash 与 DeepSeek-V4-Pro-0813）；**TerminalBench 3.0 24.3**（超 K3 等万亿参数级）；**SWE-Bench Pro 61.6**（+10.5）；知识向 GPQA-Diamond 90.9、IMOAnswerBench 97.1、HMMT Feb 2026 91。
- **效率**：Agent 任务**迭代步数 −20%~30%**、**执行周期 −35%**、**Token 消耗 −20%~30%**。以 10B 激活规模去换 266B 的能力，单位成本锚在**激活规模而非总参数**。
- **训练（RSI 第一步）**：模型**深度参与自身训练闭环**——生成训练数据、分析执行轨迹、巡检并修复训练系统；自主构建**近 10 万条**高质量 SWE 任务集。配套异步 Agent RL（并行 Worker 沙盒 + GRPO）、多教师在线策略蒸馏、自适应动态任务生成 → **有效训练轨迹 +60%、训练步数 −55%**。官方强调这是**有边界、沙盒内、可回滚**的自我改进。
- **免费 / 价格**：**限时六折** 输入 **0.6 元** / 输出 **1.2 元** / 缓存命中 **0.12 元**（每百万 token）。**9/15–9/30 新老用户各领 1 亿 Tokens**。已上 MaaS：`maas.unisound.com/models/u2-flash`。

⚠️ 两条要核实：① 官方只写「限时体验活动」，**没有公布 1 亿 Tokens 的有效期与是否分模型池**；② 公告**完全没提开源**——目前是纯 API 额度，**不要假定有可自部署权重**。另外所有跑分都是官方自测同图对比，**尚无独立第三方复现**。

### 3. 💰 GPT-6 Astra 把价格拉到 $10/$50，反而验证了「开权重已经够用」

- **价格信号是分裂的**：OpenAI **GPT-6 Astra** API 定价 **$10 / $50 每百万 token**（约前代 2.5 倍），1.05M 上下文 / 128K 输出；而同一周 **GPT-5.6 Luna 降价 80%，用量直接跳 10 倍**（OpenAI 官方口径）。
- **Agent Arena 同榜（每任务中位成本）**：**DeepSeek V4.1 Flash (Max)** +4.87% 净提升 / **$0.07**（开权重第 3、总榜第 12）；**Hy4 preview** +4.96% / **$0.22**；**Kimi K3 (Max)** +6.39% / **$0.77**。
- **榜单换血**：Artificial Analysis 用新的私有评测替换 τ³ 后发布 **Intelligence Index v4.3**，**DeepSeek V4.1 Flash 直接第一**。
- **独立复测（更扎心）**：Entelligence 用 50 个真实 PR（Cal.com / Sentry / Discourse / Keycloak / Grafana）横评——**Astra 确认 92 个 bug vs Luna 69 个**，但 **Luna 用约 3.6% 的成本抓到了 75% 的已确认 bug**。贵 27 倍的模型多找出 33% 的 bug。
- **今天新增的两个免费入口**：① 🆓 **xAI Grok Build**——Grok 4.6 驱动的编码 agent，**一条 `curl` 装好、免费试用且已开源**，内置 AGENTS.md、plugins、hooks、MCP 与 `/skillify`。② 🧰 **Cline Desktop**——**100% 开源**工作区，**内置免费 DeepSeek-V4.1-Flash**，也可 BYOK，支持并行 agent 与定时任务。

✅ **正确的读法**：**「免费」的真正来源是开权重的成本曲线，不是厂商的慷慨**。判断一个「免费」值不值得花时间，要看它是不是**先进模型 + 量大**，而不是看它写了多少 0。

---

## 🌤️ 次要更新

- **🆓 xAI 开源 Grok Build**：安装只要**一条 `curl`**，**免费可试且代码已开源**，内置 AGENTS.md、plugins、hooks、MCP 与 `/skillify`。⚠️ 同期流出的 Grok 4.7/4.8/4.9 与 Grok 5 参数描述**均未获官方证实**。
- **🧰 Cline Desktop**：面向**开权重模型**的桌面工作区，**100% 开源**；开箱**内置免费 DeepSeek-V4.1-Flash**，可 BYOK，支持**并行 agent** 与**定时任务**。对「不想为 coding agent 再付订阅」的人门槛最低。
- **🔬 NVIDIA 开源 FlashREINFORCE**：面向 agentic 语言模型的**无 critic、单 rollout、异步** RL 框架。要解决的问题是长程 rollout 时长不规则、而 group-relative 方法（如 GRPO）需要同 prompt 的**兄弟 rollout** 互相等待；做法是 **One-Batch REINFORCE**（每 prompt 只跑一次），报告达成 **6000+ 次稳定更新**。
- **🤝 OpenRouter Forge**：与 **Arcee AI、Microsoft、Vercel** 合作，主题是**把开权重模型推向能力前沿**。与 Bolt Forge 同日进入视野，指向同一个判断。
- **🇨🇳 国内免费额度速记（9/15 核实）**：
  - **阿里云百炼**：Night Plan **每日 22:00–次日 08:00 折扣，Qwen3.8-Max / Flash 低至 4 折**（自动生效）；**AI 焕新季满减券 9/30 截止**（满 20 减 10 / 99 减 15 / 199 减 35，领后 14 天有效）；**OPC 创新助力计划** 1000 元–100 万元 Token 补贴、先用后返；新客 1 亿 Tokens（90 天）+ 每模型各 100 万。
  - **智谱**：ZCode 夜间免费 **23:00–09:00，到 9/20**；开放平台 GLM 系 8 款 Flash 模型仍标免费。
  - **讯飞**：Spark-X2.5-1.7B 长期免费、**X2.5-4B 限时免费**（原生 1M 上下文）；星辰 MaaS 同款 0 元。
  - **商汤 SenseNova**：Free 公测档，通用积分池 **6 万 / 5 小时滚动 + 60 万 / 周**，不绑卡。
  - **腾讯云 TokenHub**：语言与多模态理解模型**各 100 万 Tokens，有效期 1 年**（活动至 12/31）。
  - **华为**：ModelArts 首次开通**每模型 200 万 tokens**；码道签到活动到 12/31。
  - **书生 Intern AI**：**每月 9000 万输入 + 9000 万输出 tokens**（自然月刷新，默认 30 RPM）——单看月度额度是国内公开口径天花板最高的一档。
  - **快手万擎 StreamLake**：KAT-Coder-Air-V1 与 KAT-Coder-Exp-72B-1010 输入输出全免费（新版 Air-V2.5 已转收费）。
- **💰 智谱夜免的成本真相**：同一真实 Agent 任务，**DeepSeek V4 Flash 4 分钟 vs GLM 5.3 Flash 14 分钟**（3.5 倍）；推理速度 **约 150 tok/s vs 不到 50 tok/s**（DeepSeek V4.1 Flash 发布后实测 420–507 tok/s）。智谱的口径（成本降 80%、性能比基线提升 3 倍）**都是跟自己比**。同期 Coding Plan **Pro 版从 149 元涨到 538 元**。读法：**免费额度跑闲时低成本算力，付费套餐才是正价高优先级资源**——免费窗口别排交互式 / 长链 Agent。
- **📌 顺手记**：Claude Fable 5.1 在无人干预循环里用 44 分钟 / 176k tokens 破解 370 年的 Urquhart 密码，并领跑 AA Capability Index 全部 6 个领域；有报道称「放缓即抽梯子」的舆论与跨境模型隔离传闻在发酵（**含未证实内容，仅作背景**，跨境调用注意静默降级与合规风险）。

---

## 🧾 今日免费入口速查（先进 + 量大优先）

| 入口 | 能调到的先进模型 | 额度 / 价格 | 门槛 |
|---|---|---|---|
| **OpenCode Zen** | `nemotron-3-ultra-free`（1M）、`nemotron-3.5-lightning-free`（1M）、`mimo-v2.5-free`、`ling-3.0-flash-fin-free`、`muse-spark-1.3-contributor-free`、`big-pickle` | **$0**；定价页 Free 行 6 款，全部 **limited time** | 登录拿 Key，客户端内直接选 |
| **OpenRouter** | 免费池 19 款，含 `nemotron-3-ultra-550b-a55b:free`（1M）、`thinkingmachines/inkling:free`（1M）、`nemotron-3.5-lightning:free`（1M）、`ling-3.0-flash-vl:free`、`nex-n2.5-pro:free` | **$0**；`:free` 约 20 RPM / 50 RPD，**充值满 $10 后升到 1000 RPD** | 注册即可，免信用卡 |
| **NVIDIA NIM** | `z-ai/glm-5.3-flash`（1.3M，榜分 96）、`moonshotai/kimi-k3`（1M）、`deepseek-ai/deepseek-v4-pro-0813`（1M，384K 输出） | 免费档 **最高 40 RPM**，部分模型 TPD 不设限 | 需邮箱 + **手机号验证** |
| **Ollama Cloud** | `deepseek-v4-pro`（1M，93 分）、`deepseek-v4-flash`（1M，92 分） | 免费层 starter 用量，按 token 计量、月重置 | 注册即可；本地跑完全免费 |
| **云知声 MaaS**（今日新增） | **U2-Flash**（266B-A10B，DeepSWE v1.1 64.6） | **9/15–9/30 新老用户各领 1 亿 Tokens**；限时六折 输入 0.6 / 输出 1.2 元 | 注册 + 实名 |
| **Google AI Studio**（额度收紧） | Gemini 3.8 / 3.7 / 3.6 / 3.5 Flash（1M，多模态） | Flash 系**每天仅约 20 RPD**；**Flash-Lite 500 RPD**；15 RPM | Google 账号，免信用卡 |
| **书生 Intern AI** | Intern 全系（含科学多模态线） | **每月 9000 万输入 + 9000 万输出 tokens**，30 RPM | 注册；按自然月刷新 |
| **Bolt Forge**（需 Pro） | **GLM 5.3 Flash** / GLM 5.3 / Kimi K3 / DeepSeek v4 Pro | **最高 50× 用量、零额外费用，至 10/14** | 个人 Bolt Pro 订阅 + **opt-in 共享匿名数据** |

排序原则：**先进模型 > 额度大小 > 门槛**。同一档里优先选「1M 上下文 + $0 + 免绑卡」的组合——今天的免费池里，`nemotron-3-ultra`、`nemotron-3.5-lightning`、`thinkingmachines/inkling`、`inkling-small` 是仅有的四款「1M + $0」，其中两款在 OpenRouter 与 Zen **双通道都免费**。

---

## 🔎 平台盘点 · 今日快照

- **OpenRouter**：目录 **445 款**，`pricing.prompt == '0'` 且 `:free` 结尾 **19 款**，与 9/14 **完全一致**（无新增、无下架）。新增两个别名条目 `~deepseek/deepseek-flash-latest`、`~deepseek/deepseek-pro-latest`（**都不是免费项**），下架 `google/gemini-2.5-pro-preview-05-06` 与 `openai/gpt-4-turbo-preview`。1M 上下文免费 **4 款**。⚠️ 免费池**日内会波动**，19 是脚本清点时刻的快照；已留 `or_models_0915.json` 供次日 diff。
- **OpenCode Zen**：`/zen/v1/models` 返回 **70 款**，与 9/14 一致。带免费标记的 ID **8 个**：`big-pickle`、`deepseek-v4-flash-free`、`mimo-v2.5-free`、`ling-3.0-flash-fin-free`、`nemotron-3-ultra-free`、`nemotron-3.5-lightning-free`、`muse-spark-1.3-contributor-free`、`muse-spark-1.2-contributor-free`。官方**定价页** Free 行是 **6 款**（Big Pickle / MiMo-V2.5 / Ling 3.0 Flash Fin / Nemotron 3 Ultra / Nemotron 3.5 Lightning / Muse Spark 1.3 Contributor），**全部写 limited time 且无到期日**。⚠️ **官方两个文档页名单不一致**——以定价页为准做预算、以端点为准做可用性探测。⏰ **Zen 的 GPT-5.6 Sol 50% 折扣 9/18 到期**。
- **freellm.net**：较 9/14 的 **476+ / 31 / 318** 全线上涨至 **479+ 模型 / 31 平台 / 332 款免信用卡**；其中 **237 款经 live API 核验**。榜首仍是 **NVIDIA NIM 的 `z-ai/glm-5.3-flash`（96 分，1.3M、40 RPM、周用量 597.1M）**，其后 Ollama Cloud `deepseek-v4-pro`（93）、`deepseek-v4-flash`（92）、NIM `Kimi K3`（92）、NIM `deepseek-v4-pro-0813`（92）。OpenRouter 侧榜分最高的是 `ling-3.0-flash-vl:free`（86 分，周用量 184.4B）。

---

## 📅 到期日历

**眼前这一周**

- **9/15（今天）** — 云知声 U2-Flash **1 亿 Tokens 活动开始**（到 9/30）；阿里云百炼 **glm-5.2** 免费额度今天到期
- **9/15 22:00** — 通义灵码 6 项商品**停止新购**
- **9/17** — GPT-6 Astra Challenge 投稿截止（前五名各 1 万美元额度）
- **9/18** — OpenCode Zen **GPT-5.6 Sol 50% 折扣到期**
- **9/20** — 智谱「Flash × ZCode」夜间畅用（23:00–09:00）结束

**9 月下旬及以后**

- **9/30** — 云知声 U2-Flash **1 亿 Tokens 活动 + 六折价**结束；腾讯 **Hy3 免费期**结束；**Merge Gateway GLM-5.3-Flash 1 折**结束；阿里云 **AI 焕新季满减券**截止
- **10/10** — WorkBuddy Hy4 preview 新用户「首开享 14 天」的最后首开日
- **10/14** — **Bolt Forge 50× 用量预览期结束**（Forge 本身继续保留）
- **12/31** — 腾讯云 TokenHub / 华为云码道「码力续航计划」/ 移动云 MoMA 活动截止

---

## 🧭 今天该怎么动

**① 现在就做（5 分钟内）**：去**云知声 MaaS 把 1 亿 Tokens 领了**（`maas.unisound.com/models/u2-flash`，9/15–9/30 窗口），领完先在控制台确认**额度有效期与是否分模型池**；另外**今天就把百炼的 `glm-5.2` 额度烧掉**。

**② 今天之内**：**想扩量**的——若是个人 Bolt Pro 用户且能接受匿名数据共享，切一次 **Bolt Forge**（先复制项目再切，实测 50× 在你账号上的绝对额度）；**不想花钱**的——直接上 **OpenCode Zen 的 `nemotron-3-ultra-free`** 或 **OpenRouter 的 `nvidia/nemotron-3-ultra-550b-a55b:free`**（1M + $0）；**写代码**的——装 **Grok Build**（一条 curl）或 **Cline Desktop**（内置免费 V4.1-Flash）。

**③ 本周之内**：① 把 **Zen 的 6 款 Free** 接进 fallback 链第二位（第一位给 NIM 的 `glm-5.3-flash`），它们全部 **limited time 且无到期日**，随机会消失；② 长上下文批处理放**智谱夜间 23:00–09:00**（免费到 9/20）或**百炼 22:00–08:00**（4 折），但**都别排交互式任务**；③ 周额度吃紧时重算成本——**Luna 降价 80% 后，3.6% 的成本能抓到 75% 的已确认 bug**，多数场景继续堆 Astra 未必划算。

---

⚠️ 免费额度可能随时调整，请以各平台官网最新政策为准。本页所有「免费」判定均以官方接口或官方定价页为准。
**Bolt Forge 的「免费」需个人 Pro 订阅且需 opt-in 共享匿名 build session**，不是无条件免费，其 50× 绝对额度上限官方未公布。
**云知声 U2-Flash 的 1 亿 Tokens 活动**官方未公布有效期细节，公告未提开源（目前为纯 API 额度），且跑分**尚无独立第三方复现**。
OpenRouter 免费池日内会波动，19 款是**脚本清点时刻的快照**；Zen 的 6 款 Free **全部标注 limited time 但无具体到期日**，且官方两个文档页名单不一致。
智谱夜间免费**限付费套餐且仅限 ZCode 客户端内**；Google Gemini Flash 系免费额度已收紧至约 **20 RPD**。

**数据来源**：OpenRouter `/api/v1/models`（9/15 脚本清点）· OpenCode Zen `/zen/v1/models` 与官方定价页 · Bolt.new 官方博客与 BusinessWire 新闻稿（9/14）· AGI Hunt 日报 2026-09-15 · 云知声港交所自愿公告（2026091500089）与 MaaS 平台页 · Artificial Analysis Intelligence Index v4.3 · freellm.net 核验榜 · 阿里云开发者社区百炼文档与优惠页 · 今日头条《智谱夜免活动送额度，速度只有竞品三分之一》· 各厂商官方额度页 · costgoat.com / aimcp.info OpenRouter 免费模型追踪。

© [lph12168x/Free-LLM-Daily](https://github.com/lph12168x/Free-LLM-Daily) · 🤖 由 WorkBuddy 自动化生成 · 2026-09-15
