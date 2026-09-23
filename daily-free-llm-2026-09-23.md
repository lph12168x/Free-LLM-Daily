# 免费大模型日报 · 2026-09-23（周三）

> 🤖 AI 每日免费情报 · 全网挖掘 · [在线版 HTML](daily-free-llm-2026-09-23.html)

**今日四个关键数字**

| 数字 | 含义 |
| --- | --- |
| **1 亿** | 国产新贵 **Atria Dawn** 开放托管 API：**注册即送 1 亿 token**，744B MoE / 激活 40B / **三协议全通**——今天量大能用的一条硬货 |
| **腰斩** | 9/22 一日双发：**GPT-6 Sol / Luna** 降价 **50%**、**Claude Opus 5.5** 标价降 20%；**Luna 进了 ChatGPT 免费桌面端** |
| **24 / 21** | OpenRouter 零价 **24 款**（`:free` 21）**连续四期零变**；Zen **79 款**、免费 ID **9 个**，今日新增三条全在付费侧 |
| **3 个** | 今天新挖到 **Kilo Code**（10 款免费 / 200 请求每小时）、**FreeRide v3**（跨 5 家免费档自动切换）、**FreeTheAi**（宣称 1.6 万款 $0） |

---

## 🔥 今日头条 · 三条主线

### ① 今日新挖掘｜`Atria Dawn` 开放托管 API：**注册即送 1 亿 token**，744B MoE，**三种协议实测全通**

**今天最值得薅的是它——不是折扣券，是直接给量。** 上海人工智能实验室（InternLM 团队）的 **Atria Dawn** 此前以「**先放权重、后开发布会**」的反常规方式开源（**9/11 上权重卡 + 9/12 FP8 量化版 + 9/14 提交 arXiv 论文**），现在 **托管 API 正式开放，新注册账号直接到账 1 亿可用 token**。实测者把三种接口各打了一遍：**Chat Completions、Responses、Anthropic Messages 全部 HTTP 200**。

| 项目 | 内容 |
| --- | --- |
| 🧩 规格 | 基于 **Z.ai 的 744B 参数 MoE 基座**（即 GLM-5.2 系），**每 token 激活约 40B**，官方文档给 **256K 上下文**，**仅文本输入**（不支持图像 / 音频 / 视频）。训练走名为「**可验证经验流水线**」的路线：把 agent 轨迹绑到可执行环境 + 外部可核验的结果上，而非自评分——目标是长程科研与工程任务里的**工具调用、环境交互、失败恢复** |
| 🏆 能力定位 | 第三方 LLM Stats 综合分 **50.1 ~ 52.1**，排 **#10 ~ #13** 区间，与 Hy4 preview（50.4）、Qwen3.8 Max（50.2）同档；**落后 Claude Opus 5.5（57.9）与 GPT-6 Astra（57.4）约 6 分**。强项很偏「检索与工程」：**DeepSearchQA 96.0、BrowseComp 92.5、CyberGym 86.5、MLE-Bench Lite 86.2、WideSearch 81.9**。**短板同样明显：Terminal-Bench 2.1 只有 78.3**（Opus 5.5 为 89.9）。**注意：论文自评 16 项基准里 5 项第一，但至今无独立复现** |
| 🎁 免费怎么拿 | ① 去 **Atria 开放平台注册**（论文与模型卡均未列托管服务商，属官方自营）；② 创建 key；③ 直接用 OpenAI / Anthropic 任一 SDK 指向官方 base_url 调用。文档标注 **60 RPM**，实测者压力测试时服务端实际按 **50 RPM** 限流——**按 50 规划并发**。**1 亿 token 按主流旗舰 $3~$5/百万输入的量级折算，约值数十到数百美元** |
| ⚠️ 三个坑 | ① **上下文口径打架**：技术论文/模型卡写 **1M（1,048,576）**，托管 API 文档写 **256K**——**按 256K 规划，别按 1M 堆提示词**。② **纯文本模型**：有图片需求的工作流不能迁过来。③ **MIT 权重 ≠ MIT 托管服务**：权重可自由商用，但托管 API 的服务条款、数据是否用于训练**尚未明确披露** |

**为什么值得单独上一条头条**：它同时满足三件事——**量大**（1 亿 token）、**能用**（744B 级、三协议、50 RPM）、**先进**（开源第一梯队、检索与工程类基准很硬）。**今天就去注册占额度**。

**和 Zen / OpenRouter 的关系**：Atria Dawn **未上 OpenRouter 零价池，也未进 OpenCode Zen 免费名单**——所以它**不在今天的 24 款 / 9 个 ID 统计里**，是独立于聚合站之外的官方直供入口。**这正是「不要只看聚合榜」的又一例证**。

---

### ② 昨夜晚间｜OpenAI 与 Anthropic 同日双发：**GPT-6 Sol / Luna 价格腰斩**、**Claude Opus 5.5 降价 20%**——**Luna 进了免费桌面端**

**9 月 22 日，两家在两小时内先后发新模型，且都选择降价而不是抬性能上限。** Anthropic **16:31 UTC** 发 **Claude Opus 5.5**，OpenAI **18:12 UTC** 发 **GPT-6 Sol 与 GPT-6 Luna**——距离两位 CEO（10 天前）联署呼吁「放慢前沿 AI 发展」不到两周。**对免费用户的直接好处只有一条：GPT-6 Luna 已开放给 ChatGPT 免费版与 Go 用户在桌面端使用**，这是目前零成本摸到 GPT-6 系的唯一入口。

| 项目 | 内容 |
| --- | --- |
| 💵 GPT-6 新价格（永久价） | **Sol `$2 / $10`**（缓存读 $0.20）— 对比 GPT-5.6 Sol 的 `$4 / $20`；**Luna `$0.10 / $0.50`**（缓存读 $0.01）— 对比 GPT-5.6 Luna 的 `$0.20 / $1.20`，**输出实际降了 58%**。**旗舰 Astra 价格完全不动（`$10 / $50`）**。Batch 与 Flex 在上述已砍半的价上**再打 5 折**（Sol batch 输出 $5 / Luna batch 输出 $0.25）。**⚠️ 计价陷阱：单次提示超过 272K 输入 token 时，输入按 2 倍、输出按 1.5 倍计费** |
| 📐 规格 | 两者共享 **1.05M 上下文 / 922K 输入上限 / 128K 输出上限**，文本 + 图像输入、文本输出，**六档 reasoning effort（none → max）** |
| 🏆 厂商自评跑分 | **DeepSWE v1.1 Sol 68.8% / Luna 66.6%**（Fable 5 为 69.9%）；**OSWorld 2.0 Sol 60.5% 略超 Opus 5 的 60.3%**；**Agents' Last Exam Sol 56.4% vs Opus 5 的 55.9%**；**FrontierCode 1.1 Sol 49.3% 反超 Fable 5.1 的 48.7%**；**AutomationBench 33.2%（xhigh）单任务 $0.27** |
| 🔍 独立评测说了不一样的话 | Artificial Analysis 口径更保守：**Sol 在 Coding Agent Index 上比 GPT-5.6 Sol 高 2 分**是真的（**Terminal-Bench 4.0 43% vs 37%、SWE-Atlas-QnA 58% vs 54%**），单任务成本约**半价**。**但 Luna 反而低了 2 分**——**SWE-Atlas-QnA 44% vs 49%、DeepSWE v1.1 64% vs 66%**，即使单任务成本降了约 **60%**。**结论：Sol 是真升级，Luna 是「降价换微退」，别把 Luna 当同等能力的便宜版用** |
| 🟣 Claude Opus 5.5 | **`$4 / $20`**（缓存读 $0.20）——标价比 Opus 5 降 **20%**，Anthropic 自称典型负载运行成本降 **40%**、输出速度提升 **30%+**，多数任务达到旗舰 **Fable 5.1 水平**。安全侧宣称突破边界的尝试次数**比 Opus 5 / Claude Mythos 5.1 减少 85%**，发布前经 **METR 与 Frontier Design** 外部评估。案例：早期测试者**不到一天完成 68 万行代码迁移**、网页加载优化**40 次尝试成功 39 次**。**Sonnet 5.5 与 Haiku 5.5 将在未来几周推出**。**⚠️ Anthropic 没有任何永久免费 API 档** |

**同步到聚合平台了吗**：OpenRouter 一口气上了 **`openai/gpt-6-sol`、`gpt-6-sol-pro`、`gpt-6-luna`、`gpt-6-luna-pro`**（各含 `:batch` 变体）与 **`anthropic/claude-opus-5.5`**（含 `:batch`）；OpenCode Zen 同日也上了 **`gpt-6-sol` / `gpt-6-luna` / `claude-opus-5-5`**——**但全部落在付费侧，零价池一条没动**。

**怎么读这一波**：竞争轴线正从「谁的旗舰更强」转向「谁的单位成本更低」——两家把 Astra / Fable 5.1 的部分能力**下沉到更便宜的档位**。对开发者的实际影响：① 之前因为贵而没敢用的编码 agent，现在可以按 token 预算重新评估；② **Luna 进免费桌面端意味着零成本试用窗口打开**，但**只限桌面 App、只限对话，不是 API 免费**；③ 长上下文（>272K）有 2 倍输入加价，**做成本模型时务必算进去**。

---

### ③ 免费池体检｜零价池**连续四期零变**，但今天有一条**到期的免费券仍在超期运行**

**今天的免费池很安静，安静到要提醒你风险在哪。** OpenRouter 目录从 445 涨到 **454 款（+9）**，但**新增的 15 条全在付费侧**；零价池依然是 **24 款（`:free` 21 款）**——**从 9/20 到今天，连续四期一条没进、一条没出**。这种「静止」通常不是稳定，而是**平台在等下一波促销换血**。

| 项目 | 内容 |
| --- | --- |
| ⚠️ 今天最该警惕的一条 | **`inclusionai/ling-3.0-flash-vl:free`** 的免费服务由上游 **Novita 提供，官方文档白纸黑字写着「免费到 2026 年 9 月 23 日 02:30 UTC」**——**就是今天凌晨，这个窗口已经过期了**。脚本在 **约 05:10 UTC** 抽查端点，结果是：**Novita 仍在服务、status 正常、30 分钟可用率 99.99%、$0 / $0、262K**——**也就是说它在「超期续命」**。**行动建议：今天可以继续白嫖，但绝对不要写进任何长期依赖或生产链路**；迁移成本最低的替代是 `thinkingmachines/inkling:free`（同样 1M 多模态）或 Zen 的 `mimo-v2.6-flash-free`（全模态且 9/22 刚上架） |
| 🔬 端点抽查：四条全绿 | `ling-3.0-flash-vl:free` — Novita，**99.99%**；`nemotron-3-ultra-550b-a55b:free` — Nvidia，**99.70%**；`inkling:free` — Thinking Machines，**99.98%**；`glm-5.2:free` — Decart，**99.94%**。四条 status 均为 0（正常），**价格全部 $0 / $0**。**读法提醒：可用率是「运营状况」不是「政策承诺」** |
| 🔧 OpenCode Zen | `/zen/v1/models` 返回 **79 款**（9/22 是 76），新增 **`gpt-6-sol`、`gpt-6-luna`、`claude-opus-5-5`** ——**全是昨夜的新模型，也全是付费行**。带免费标记的 ID 仍是 **9 个**。**官方定价页 Free 行是 8 款**，另有 **Jev 1.13 输出列 Free**（输入 $0.042）。**两个口径差 1 条（`deepseek-v4-flash-free`），按平台惯例以定价页为准** |
| 📊 freellm.net | **503+ 款 / 31 家平台 / 241 款通过实时 API 验证 / 416+ 款免绑卡**（9/22 是 503+ / 31 / 243 / 413+）——**live 数降 2、免绑卡数升 3**，属日内波动。榜首仍是 **NVIDIA NIM `z-ai/glm-5.3`（97 分，1.3M 上下文、40 RPM）**，第二 **`z-ai/glm-5.3-flash`（96）**，第三 **OpenRouter `Ling 3.0 Flash Sante (free)`（95）**。**前十里有 3 条是 OpenRouter 的免费档** |

**零价池近四期流水**（脚本口径：输入与输出同时为 $0）：

| 日期 | 目录总量 | 零价池 | 其中 `:free` | 净增减 |
| --- | --- | --- | --- | --- |
| 9/20 | 446 | 24 | 21 | — |
| 9/21 | 446 | 24 | 21 | +0 / -0 |
| 9/22 | 445 | 24 | 21 | +0 / -0 |
| **9/23（今天）** | **454** | **24** | **21** | **+0 / -0** |

目录总量四期涨了 **8 款**，零价池**纹丝不动**——**平台把增量全给了付费模型**。这是本周读供给结构最重要的一张表。

**别只看聚合榜**：今天最典型的例子就是 **Atria Dawn 官方 1 亿 token 免费额度，在 OpenRouter / Zen / freellm.net 三处都查不到**——它只在官方开放平台注册时出现。**聚合站的价值是「发现存量」，官方直营的价值是「拿到增量」**，两边都得看。

---

## 🌤️ 次要更新 · 值得记一笔

### 🌐 今天新挖到的三个免费入口

**① Kilo Code 网关**（`https://api.kilo.ai/api/gateway`）——面向编码 agent 的专用网关（VS Code / JetBrains / CLI 三端），**免费档 10 款模型、200 请求/小时、免绑卡、GitHub 账号直接登录**。免费阵容：`tencent/hy3:free`（262K）、`nvidia/nemotron-3-ultra-550b-a55b:free`（1M）、`stepfun/step-3.7-flash:free`、`nvidia/nemotron-3.5-lightning:free`（1M）、`poolside/laguna-s-2.1:free`、`laguna-xs-2.1:free`、`cohere/north-mini-code:free`、`nvidia/nemotron-3-nano-omni...:free`、`liquid/lfm-2.5-2.6b:free`、`nvidia/nemotron-3-super-120b-a12b:free`。**⚠️ 它在路由上是黑盒——你不能指定模型，网关自己挑**；另 llmpricing.dev 标它有 26 款 $0（含 OpenRouter 透传条目），**与 freellm.net 的 10 款口径不一致，取保守值**。

**② FreeRide v3**（`free-ride.xyz`）——本地 OpenAI 兼容网关，**把 OpenRouter / Groq / NVIDIA NIM / Cloudflare Workers AI / HuggingFace 五家免费档串成一条链，命中限流自动切换**，一键绑定 Aider / Continue / Hermes / OpenClaw。安装：`curl -sSL https://api.free-ride.xyz/install.sh | sh`，然后指向 `http://localhost:11343/v1`。**这是今天最实用的一个工程件——它直接解决「免费档限流打断工作流」这个真痛点。**

**③ FreeTheAi**（`api.freetheai.xyz/v1`）——宣称 **16,248 款模型、$0、无日限额、不存 prompt**，同时提供 OpenAI（`/v1/chat/completions`）与 Anthropic（`/v1/messages`）协议，还带图像生成与编辑接口。领取方式是 **Discord 频道内 `/signup`**。**⚠️ 三个硬伤：key 走 Discord 社交渠道、上游供应商完全不透明、没有任何 SLA 或主体信息——只适合玩具项目与试验，别放进生产。**

### 📉 一条重要纠错：硅基流动小模型免费已取消

多个第三方清单与「老攻略」仍在写「**硅基流动 9B 以下小模型永久免费**」——**这已经失效了**。现在的实际情况是：**只有 embedding、语音、OCR、翻译、Kolors 图像这几类免费，对话类模型需要付费**。**凡是从聚合站或博客抄来的免费清单，使用前一律回官方定价页复核一遍**——这类「过期攻略」是本期发现的第二处聚合站滞后。

### 🔒 Yandex 开源 `AliceAI-Foundation-80B-A3B-Base`（但别急着用）

俄罗斯 Yandex（当地「谷歌」）在 Hugging Face 发布 **AliceAI-Foundation-80B-A3B-Base**：**80B 总参、每 token 激活约 3B 的 MoE**，自称**从零自研**（而非在现有模型上魔改），定位对标 DeepSeek 与 Qwen 的免费开源路线。**⚠️ 但它是 base 模型——没人教过它对话、遵循指令或拒绝不当请求，是「给开发者的原料」不是「能直接用的产品」。** 另外**不支持 llama.cpp**，想本地跑得换推理框架。数据合规与信任问题也需自行评估。**记一笔就好，暂时不用上。**

### 🎁 两条仍然便宜的国产兜底线

**① 小米 MiMo-V2.6 的免费路今天仍在跑**：OpenCode 官方明确 **MiMo-V2.6 Flash 免费一周**；另有 **AI Studio 在线调用**（Pro 与 Flash 均已上线）、**mimo.xiaomi.com 网页端**注册即用、**MiMo Desktop 正式版**桌面客户端。配合 Zen 的 `mimo-v2.6-flash-free`，**今天至少四条零成本通道**。

**② 智谱官方永久免费兜底**：**GLM-4.7-Flash、GLM-4.5-Flash、GLM-4.6V-Flash 的输入、缓存输入、输出全列为 Free**（z.ai 开放平台），**「永久免费 + 无到期日」这一类才是真正可以写进长期链路的**——和限时券分开管理。

---

## 🧾 今日免费入口速查 · 先进 + 量大优先

### 今天最值得上的七条（按「量大 + 能用」排序）

| 入口 | 免费额度 | 模型量级 | 状态 / 注意 |
| --- | --- | --- | --- |
| **Atria Dawn 官方 API**（今日新挖掘） | **注册送 1 亿 token** | 744B MoE / 激活 40B、256K / 纯文本 | **三协议实测全通**；50 RPM（文档写 60）；**ctx 口径按 256K 算** |
| **OpenCode Zen** `mimo-v2.6-flash-free` | 四列全 Free（限时） | 310B / 激活 15B、**1M + 全模态** | 今天仍是最优选之一；**免费期数据可能用于改进模型** |
| **ChatGPT 桌面端 + Luna**（昨夜新增） | Free / Go 可用（仅对话） | GPT-6 系、1.05M ctx | **GPT-6 唯一免费入口**；**不是 API 免费、不开放给第三方** |
| **OpenRouter** `nemotron-3-ultra:free` | $0 / $0（200 请求/日） | 550B / 激活 55B、**1M** | Nvidia 端点可用率 **99.70%**；**大批量任务首选 $0 通道** |
| **OpenRouter** `inkling:free` | $0 / $0（200 请求/日） | MoE 激活 41B、**1M + 多模态** | 可用率 **99.98%**；可作 `ling-vl` 的迁移目标 |
| **Kilo Code 网关** | 10 款免费、**200 请求/小时** | 64K ~ 1M | **今天新挖**；免卡、GitHub 登录；**路由黑盒不可指定模型** |
| **NVIDIA NIM**（长期兜底） | 40 RPM、**不限调用量** | 含 `glm-5.3` 1.3M 与 Kimi K3 1M | freellm.net 榜首来源；**需手机验证** |

### 长期兜底组合（无到期日那一类）

- **智谱 z.ai** — `GLM-4.7-Flash` / `GLM-4.5-Flash` / `GLM-4.6V-Flash` **输入输出全 Free，无到期日**（国内直连）。
- **书生 InternLM** — **1.8 亿 tokens/月、免信用卡、无明确到期日**，国内可直连。
- **美团 LongCat** — **每天 5,000 万 token**。
- **Cerebras** — **每天 100 万 token**；**Cloudflare Workers AI** — **每天 1 万 neurons**。
- **OVHcloud AI Endpoints** — **匿名免注册 9 款**，2 RPM。
- **Pollinations** — **免 key 即用**，适合临时脚本。

**组合建议**：**主力**用一条稳的（NIM / 智谱永久免费档），**兜底**用无到期日的（LongCat / InternLM），**临时**用免 key 的（Pollinations）——**别把全部调用压在同一个免费档上**。

---

## 🔎 平台盘点 · 今日快照

### 📊 OpenRouter：**454 款中 24 款零价**（`:free` 21 款），**连续四期零变**

- 脚本清点时刻：**454 款（较昨日 +9）**，其中**输入与输出同时为 $0 的共 24 款**（带 `:free` 后缀 21 款）。**零价池与昨日完全一致——一条没进、一条没出。**
- **1M 上下文且 $0 的有 6 条**：`nvidia/nemotron-3.5-lightning:free`（1,000,000）、`nvidia/nemotron-3-ultra-550b-a55b:free`（1,000,000）、`thinkingmachines/inkling:free`（1,048,576）、`thinkingmachines/inkling-small:free`（1,048,576）、`google/lyria-3-pro-preview`（1,048,576）、`google/lyria-3-clip-preview`（1,048,576）——**后两条是音频输出，不是文本**。
- **三条「零价但不带 `:free`」**：两条 Google Lyria（输出音频）+ `openrouter/free`（200K **自动路由池**）。**写代码时漏写 `/free` 会按付费价扣款**。
- **今日新增 15 条全在付费侧**：`anthropic/claude-opus-5.5`（+`:batch`）、`openai/gpt-6-sol` / `-sol-pro` / `-luna` / `-luna-pro`（各含 `:batch`）、`qwen/qwen3.8-omni-flash`、`cohere/command-a-plus`、`moonshotai/kimi-k3:batch`、`deepseek/deepseek-v4.1-flash:batch`、`openai/gpt-oss-20b:batch`。
- **今日下架**：`kwaipilot/kat-coder-pro-v2` 与 6 个 `:batch` 变体（deepseek / meta / z-ai 系）。**注意 `:batch` 的频繁上下架属正常现象，只有带 `:free` 的消失才影响免费用量。**

### 🔧 OpenCode Zen：**76 → 79 款**，免费 ID **9 个**

- `/zen/v1/models` 返回 **79 款**（较 9/22 的 76 款 +3，**零下架**）。三条新增**全是昨夜发布的付费模型**。
- 免费 ID 共 **9 个**——**连续多期维持在这个数量**，说明 Zen 的免费供给本身比较稳定。
- 官方**定价页 Free 行 8 款**，另有 **`Jev 1.13` 输入 $0.042 / 输出 Free**（走 `/zen/v1/systemone` 独立协议，非 chat）。**两处口径差 1 条（`deepseek-v4-flash-free`），按惯例以定价页为准。**
- 📖 数据条款仍需分清：**Big Pickle / MiMo / Ling 免费期数据可能用于改进模型**；**Nemotron 两条是 NVIDIA 试用端点，明确要求勿提交个人或机密数据**；**Muse Spark Contributor Free 以折扣换 Meta 训练权**。**控制台的「启用计费」按钮不要点。**
- ⏰ 旧版下线提醒：**小米 `mimo-v2.5-pro` / `mimo-v2.5` 将于 10/21 10:00 下线**，`mimo-v2.5-free` 受此影响——**尽快切 `mimo-v2.6-flash-free`**。

### 🌐 免费路由生态：把「几十家免费额度」聚成一条链

- **今天新的两条**：**Kilo Code 网关**（10 款免费 / **200 请求每小时** / 免卡 / GitHub 登录，编码专用）与 **FreeRide v3**（本地网关，**跨 5 家免费档自动 failover**，一条命令装好）。
- **此前已在架、仍然值得配的**：**OrcaRouter**（永久免费档，阵容轮换 GLM-5.3 Flash / DeepSeek V4 Flash / 腾讯 Hy3，**10 RPM / 50 RPD**，满 $20 后 800 RPD，零加价）；**OmniRoute**（MIT 开源，单端点接 **260+ 家**，约 **16 亿免费 token/月**）；**Free Claude Code**（本地代理，覆盖 **27 家**）；**FreeLLMAPI**（自托管路由，把 NVIDIA NIM 等免费档收成一个 key）。
- **诚实评价 FreeTheAi 这类「1.6 万款 $0」的站**：技术上是把上游免费端点批量透传，**能跑通不等于能用**——上游随时变性、没有配额承诺、没有主体与 SLA。**拿来试模型可以，拿来跑业务不行。**
- **组合建议**：**主力**用一条稳的（NIM / 智谱永久免费档），**兜底**用无到期日的（LongCat / InternLM），**临时**用免 key 的（Pollinations）。**再加一层自动切模型（FreeRide / OmniRoute），才算把免费档用成生产力。**

---

## 📅 到期日历 · 别踩空

### 眼前这一周

- **9/23（今天，已过）** — **讯飞 AStudio 星火 X2.5 限免已于 00:00 结束**；**WorkBuddy / CodeBuddy 的 DeepSeek V4.1 Flash 0.03× 折扣约今天到期**；**`ling-3.0-flash-vl:free` 上游 Novita 免费窗口 02:30 UTC 已到期（OpenRouter 端仍在超期运行，随时掉）**
- **9/24（明天）** — **文心快码 Comate 测试版限免结束**；**字节 TraeCode Seed 系列 1 折结束**
- **9/25** — **Jev 在 Vercel AI Gateway 的免费促销结束**（官方原文「Promotional pricing ends on September 25, 2026」）
- **9/27** — 智谱 AutoClaw 中秋充能季第二阶段结束（付费会员专享）

### 9 月下旬及以后

- **9/30** — **阿里 Qoder Qwen3.8-Flash 免费用结束**；**腾讯 Hy3 / 文心 4.0 全系列免费期结束**；Merge Gateway GLM-5.3-Flash 1 折结束
- **10/10** — **DeepSeek 低谷价窗口结束**；**腾讯混元 Hy4 preview**（老用户夜间免费）结束
- **10/14** — 珠海算力券申报截止（企业向）
- **10/15** — **阶跃 Step 5 Preview 释放完整 BF16 权重**（许可证待公布）
- **10/21（10:00）** — **小米 `mimo-v2.5-pro` / `mimo-v2.5` 正式下线**，Zen 的 `mimo-v2.5-free` 受影响
- **11/7** — MiniMax 开放平台 M3 / M2 免费试用到期（**已从更早日期延期到 11/7**）
- **12/31** — 腾讯云 TokenHub / 华为云码道 / 移动云 MoMA 年度额度截止；微信小程序成长计划二期报名截止（10 亿 Token + 10 万张生图）

---

## 🧭 今天该怎么动

### ① 现在就做（5 分钟内）

**去注册 Atria Dawn 官方平台，先把 1 亿 token 拿到手**——这是本期体量最大、且完全不需要绑卡的一条。注册完别急着压任务，**先用一个真实的中等难度任务测三件事：响应速度、工具调用稳定性、长上下文是否真的到 256K**。

**顺手检查你有没有在依赖 `ling-3.0-flash-vl:free`**（或任何下游用了 Novita 免费通道的地方）——它今天已经过了官方标定的免费截止时间，**现在还在跑只是运气**。提前把配置里的模型名换成 `inkling:free` 或 Zen 的 `mimo-v2.6-flash-free`，**留着随时可以切，比临时救火便宜得多**。

### ② 今天之内

**用 ChatGPT 桌面端把 Luna 摸一遍**：它是目前 GPT-6 系唯一的零成本入口，**重点是感受「六档 reasoning effort」在真实任务上的区别**——同一个任务分别用 none 和 max 各跑一次，**你会对「什么任务值得开高推理档」建立直觉**，这个判断迁移到 API 上直接省钱。

**给编码 agent 加一条免费备线**：如果你在用 Claude Code / Cursor / Cline，**今天适合装 FreeRide v3 或配 Kilo Code 网关**——一条命令的事，收益是**限流时工作流不再中断**。这是本周性价比最高的一次工程投入。

**如果你想做成本对比，今天的素材很齐**：GPT-6 Sol（$2 / $10）、Luna（$0.10 / $0.50）、Opus 5.5（$4 / $20）、MiMo-V2.6 Flash（$0.14 / $0.28）、Atria Dawn（免费 1 亿）——**五条不同价位、拿来跑同一个任务集，够你定出今年的默认选型了**。

### ③ 本周之内

① **做一次「免费档数据条款」清点**：把在用的每条免费通道按「可用于训练 / 仅限试用 / 需付费资格 / 条款未披露」四类打标签——**Atria Dawn 属「条款未披露」、Zen 的 Nemotron 两条属「仅限试用」、Muse Spark 属「换训练权」、AutoClaw 免费期属「可用于改进模型」，这四类不该混着用。**

② **把「限时券」和「永久免费」分开管理**：智谱 `GLM-4.7-Flash` 系列、书生 InternLM 这类无到期日的是**可以写进长期配置的**；Atria 的 1 亿、MiMo 的一周免费、Qoder 的 9/30 截止属于**试用性质，不能进依赖链**。

③ **别把「在架 $0」当稳定**：本页已多次实测 `:free` 券寿命短到 2 天以内（9/18 上线 9/20 下架即为实例）。**任何写死单条 $0 通道的地方，本周加一条可切换的备线。**

④ **盯三个日期**：**9/25**（Jev 在 Vercel 的免费促销截止）、**10/15**（阶跃 Step 5 权重开源，许可证是变量）、**10/21**（小米 MiMo-V2.5 全线下线）。

---

## 📋 数据来源

OpenRouter `/api/v1/models`（9/23 脚本清点，454 款中 24 款 $0 / 21 款 `:free`，已留 `or_models_0923.json`）· OpenRouter `/api/v1/models/{id}/endpoints` 端点抽查（`ling-3.0-flash-vl:free` — Novita 99.99%；`nemotron-3-ultra-550b-a55b:free` — Nvidia 99.70%；`inkling:free` — Thinking Machines 99.98%；`glm-5.2:free` — Decart 99.94%，四条均 status 正常、$0/$0）· **Atria Dawn** 开放 API 免费额度（新注册 1 亿 token；Atria-Dawn-Preview 基于 744B MoE / 激活约 40B / 托管 API 256K / 纯文本；Chat Completions、Responses、Anthropic Messages 三协议实测 HTTP 200；文档 60 RPM、实测限流 50 RPM；LLM Stats 综合 50.1~52.1 排 #10~#13；DeepSearchQA 96.0 / BrowseComp 92.5 / CyberGym 86.5 / MLE-Bench Lite 86.2 / WideSearch 81.9、Terminal-Bench 2.1 78.3；9/11 上卡 + 9/12 FP8 + 9/14 arXiv，MIT 权重）——Shanghai AI Laboratory / Hugging Face InternLM / ai.jp.net 实测评测 / agihunt.info / llm-stats.com · **GPT-6 Sol / Luna**（9/22 发布：Sol $2/$10 缓存 $0.20、Luna $0.10/$0.50 缓存 $0.01、Astra 维持 $10/$50；Batch 与 Flex 再 5 折；1.05M ctx / 922K 输入 / 128K 输出；六档 reasoning effort；>272K 输入按 2 倍入 1.5 倍出计费；DeepSWE v1.1 Sol 68.8% / Luna 66.6%、OSWorld 2.0 Sol 60.5%、Agents' Last Exam Sol 56.4%、FrontierCode 1.1 Sol 49.3%、AutomationBench 33.2% @$0.27/任务；Artificial Analysis 独立口径 Sol 于 Coding Agent Index +2 分（Terminal-Bench 4.0 43% vs 37%、SWE-Atlas-QnA 58% vs 54%）约半价、Luna -2 分（SWE-Atlas-QnA 44% vs 49%、DeepSWE 64% vs 66%）成本降约 60%；Free 与 Go 用户可在桌面端体验 Luna）——OpenAI 官方 / Yahoo Finance / explainx.ai / geniusfirms.com / 腾讯新闻 · **Claude Opus 5.5**（9/22 16:31 UTC：$4/$20/缓存读 $0.20，标价降 20%、运行成本降 40%、输出速度 +30%，多数任务达 Fable 5.1 水平；突破边界尝试较 Opus 5 与 Mythos 5.1 减少 85%；METR 与 Frontier Design 外部评估；68 万行代码迁移不到一天、网页优化 40 次成功 39 次；Sonnet 5.5 与 Haiku 5.5 未来几周）——Anthropic 官方 / 腾讯新闻 / llm-stats.com · OpenCode Zen `/zen/v1/models`（79 款）与官方定价页（Free 行 8 款 + Jev 1.13 输出 Free、免费模型 limited time 与隐私条款说明、「启用计费」提示）· freellm.net 核验榜（503+ 款 / 31 家平台 / 241 live / 416+ 免绑卡；榜首 NVIDIA NIM `z-ai/glm-5.3` 97、`z-ai/glm-5.3-flash` 96、OpenRouter `Ling 3.0 Flash Sante (free)` 95）与 Kilo Code Provider 页（10 款免费 / 200 请求每小时 / base `https://api.kilo.ai/api/gateway`）· **FreeRide v3**（本地 OpenAI 兼容网关，跨 OpenRouter / Groq / NVIDIA NIM / Cloudflare Workers AI / HuggingFace 五家免费档自动 failover，`http://localhost:11343/v1`，支持 Aider / Continue / Hermes / OpenClaw，MIT）· **FreeTheAi**（`api.freetheai.xyz/v1`，宣称 16,248 款模型 / $0 / 无日限额 / 不存 prompt，OpenAI 与 Anthropic 双协议，Discord `/signup` 领 key）· 硅基流动免费范围变更（仅 embedding / 语音 / OCR / 翻译 / Kolors 免费，对话模型已收费）· Yandex `AliceAI-Foundation-80B-A3B-Base`（Hugging Face，80B/激活 3B MoE，从零自研，base 模型未做对话与指令微调，不支持 llama.cpp）· 国内临期清单（讯飞 AStudio 星火 X2.5 至 9/23 00:00；WorkBuddy / CodeBuddy DeepSeek V4.1 Flash 0.03× 约至 9/23；文心快码 Comate 与 TraeCode Seed 1 折至 9/24；文心 4.0 全系列与腾讯混元 Hy3 至 9/30；阿里 Qoder × Qwen3.8-Flash 至 9/30；腾讯 Hy4 preview 至 10/10；MiniMax M3/M2 延至 11/7；微信小程序成长计划二期至 12/31）——什么值得买「全网 AI 产品免费权益清单（截至 2026.09.21）」· 智谱 z.ai 开放平台永久免费档（`GLM-4.7-Flash` / `GLM-4.5-Flash` / `GLM-4.6V-Flash` 输入、缓存输入、输出均为 Free）· 小米 MiMo-V2.6 免费通道（OpenCode 官方 MiMo-V2.6 Flash 免费一周、AI Studio 在线调用、mimo.xiaomi.com 网页端、MiMo Desktop 正式版；旧版 10/21 10:00 下线）。

> ⚠️ 免费额度可能随时调整，请以各平台官网最新政策为准。本页所有「免费」判定均以官方接口或官方定价页为准；涉及额度的具体数字请自行调用官方 Usage API 或查看控制台确认。OpenRouter 免费池日内会波动，24 款 / 21 款是脚本清点时刻的快照，不代表全天稳定值。**`inclusionai/ling-3.0-flash-vl:free` 的上游 Novita 免费窗口官方标注为 2026-09-23 02:30 UTC 截止，本页抽查时仍在服务但已属超期运行，请勿作为长期依赖。** Atria Dawn 的上下文长度存在口径差异（技术论文与模型卡标 1M，托管 API 文档标 256K），**请按 256K 规划**；其托管服务的服务条款与数据使用政策尚未明确披露，**请勿提交机密代码、个人信息或生产客户数据**。**第三方聚合榜（freellm.net / llmpricing.dev / aimodelsmap 等）与官方目录存在滞后与计数差，本页已标注两处实证（下架模型仍标 Online、硅基流动免费范围已变更），请勿单独据其做采购或宣传结论。** 「开源」指权重公开，不代表可自由商用，商用前请逐条核对许可证（尤其 Kimi、GLM、Qwen、MiniMax、Step、MiMo 系列的 Model-as-a-Service 与许可条款）。**Contributor / 试用 / 训练条款类免费档：不要把机密代码、个人信息或生产客户数据放进去。** FreeTheAi 一类免注册或社交渠道领 key 的网关，上游供应商不透明且无 SLA，仅建议用于试验，不要投入生产。GPT-6 Luna 的免费层只存在于 ChatGPT 桌面应用对话场景，**不构成 API 免费额度**。

---

📅 生成时间：2026-09-23 · 本页由自动化任务每日生成 · 亮色 / 暗色主题可点击 HTML 版右上角切换
