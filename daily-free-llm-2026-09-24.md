# 免费大模型日报 · 2026-09-24（周四）

> 🤖 AI 每日免费情报 · 全网挖掘 · [在线版 HTML](daily-free-llm-2026-09-24.html)

**今日四个关键数字**

| 数字 | 含义 |
| --- | --- |
| **1 周** | 匿名隐身模型 **Space Bunny Alpha** 昨晚双平台空降：**1M 上下文 + 图文视频三模态 + 超快推理**，OpenRouter 免费、Zen **限时免费一周**——社区指纹指向 **MiniMax M3.1** |
| **24 / 20** | OpenRouter 零价池**质地换血**：`ling-3.0-flash-vl:free` 如预判到期下架、`nex-n2.5` 付费 SKU 消失；总数 457 款（+3），零价仍 24 但 `:free` **21 → 20** |
| **$2.8 / $4** | 国产双「Prime」高吞吐 SKU 上架：**GLM-5.3-Prime** $2.80/$8.80、**Qwen3.8 Max Prime** $4/$12——**把「更快」卖成溢价，两条都无免费入口** |
| **60 款** | 新挖 **AIHubMix** 免费池：**60 款 $0 模型**（含新进的 `agents-a1-free` 上海 AI Lab 35B Agent），**$1 充值即转每日 1M token 额度** |

---

## 🔥 今日头条 · 三条主线

### ① 昨夜空降｜匿名模型 `Space Bunny Alpha` 双平台上架：**1M + 三模态 + 超快推理，免费一周**——**社区指纹指向 MiniMax M3.1**

**又是 stealth 池，但这次的规格比前两代高一个档。** 9 月 23 日晚间，OpenRouter 上架匿名模型 **`stealth/space-bunny-alpha`**，OpenCode Zen 几乎同时上架 **`space-bunny-free`**。官方描述是「**推理极快、编码能力强、原生多模态输入**」，OpenRouter 侧**免费**（**注意：这条 ID 不带 `:free` 后缀**），Zen 侧明确写了**「限时免费，为期一周」**。上线过程中曾因上游供应商问题被**临时下架**，现已恢复。

| 项目 | 内容 |
| --- | --- |
| 🐰 规格 | **1,000,000 token 上下文**（1M）、输入支持 **文本 + 图像 + 视频**、输出文本；支持**可调 reasoning effort**。对比前两代：**ox-alpha**（1M、编码/长程 agent）只活了 **6 天**；**union-alpha**（262K）活了**不到 2 天**就被流量打爆提前关闭，随后揭晓真身是 unbiased.ai 的 **Pareto 26.9**（现价 $2.50/$7.50）。**这一代直接把上下文拉到 1M 并叠加视频输入**，是三代里规格最高的一条 |
| 🚀 实测性能 | OpenRouter 实时监控（近 3 天）：**模型可达率 99.08%、实际可用率 97.27%**，单 provider 可用率 **96.09%**；**吞吐 68 tok/s（P50，全站最优）**、**延迟 0.91s（P50，全站最优）**；**缓存命中率 94.66%**；**工具调用错误率 3.29%**。上线不到一天就吃掉 **169B 输入 / 2.61B 输出 token**，流量前五全是编码类 agent：**Cline 65.6B、Claude Code 56.8B、Hermes Agent 34.9B、DeepSeek Harness 33.6B、Kilo Code 33.4B** |
| 🔍 身份线索 | 社区做了三件事的交叉验证：**① 分词器指纹**、**② 异常 token 行为**、**③ 报错信息样式**——三项都显示与 MiniMax 系列**高度相似**。更硬的旁证是：**MiniMax 官方开源的 MiniMax Code 仓库里，提前出现了 `MiniMax-M3.1` 的踪迹**，其测试代码中同时包含 **1M 上下文**与 **low / high / max 三档推理强度**开关——**与 Space Bunny 公布的能力项几乎一一对应**。另有探针用中文提问时模型自称「我是 MiniMax 的模型」，**但这只能算传闻，不构成证据**。**截至本页生成，MiniMax 官方未确认，OpenRouter 也未披露开发者身份** |
| 🔐 数据政策 | OpenRouter 侧条款：**「供应商可保留 prompt 与补全内容，但不用于训练」**，其余适用 OpenRouter 的 Stealth Model Terms。Zen 侧更进一步：**明确写「提供商遵循零保留政策，不使用你的数据训练模型」**——**这与同页的 Big Pickle、MiMo 系（免费期数据可能用于改进模型）完全不同**。**这是 Zen 免费名单里数据条款最友好的一条**，但仍需注意：**「不训练」不等于「不留存」，也不等于「可提交机密」** |

**⚠️ 三个必须知道的坑**：① **「免费一周」是计划不是承诺**——stealth 池的窗口由负载决定：union-alpha 原计划一周，实际不到 2 天就关。② **OpenRouter 这条 ID 不带 `:free`**，写代码时别习惯性加后缀（加了会 404）。③ **身份未确认 + 无独立跑分**：官方只公布「编码强、推理快」两句描述，此前流出的 79.96% / 71.47% 两个分数**未说明是什么基准**，**不可当评测结论用**。

**该不该用 / 怎么用**：**该用，但只当「试用通道」用。**它同时满足「量大（1M、免费、除限流外不限量）、能用（编码 + 多模态 + 工具调用）、先进（疑似 M3.1，未发布的新一代）」三条，**很适合拿来跑本周的编码 agent 与长文档任务**。但请遵守两条：**不要写进长期依赖**（一周后大概率转付费或消失）；**不要用 OpenRouter 与 Zen 之外的入口**（聚合站已有滞后记录）。**顺手把 `inkling:free` 或 `nemotron-3-ultra-550b-a55b:free` 配成备线。**

---

### ② 免费池体检｜零价池**总量持平但质地换了**：一条如预判到期、一条付费 SKU 退场、一条新的隐身模型补位

**昨天我们预判 `ling-3.0-flash-vl:free` 会掉，今天它掉了——但不是因为下架，是因为上游免费窗口真的过期了。** OpenRouter 目录从 **454 涨到 457 款（+3）**，零价池**依然 24 款**，但这一期的「24」和上一期的「24」**不是同一批模型**。

**📤 出：三条退场，两条是「免费券到期」**

- **① `inclusionai/ling-3.0-flash-vl:free`（零价池唯一退出项）**——上游 Novita 官方标定的免费窗口是 **2026-09-23 02:30 UTC**，昨天我们抽查时它还在「超期续命」，**今天终于从零价池消失**。**这是本页连续两天预警的兑现：限时免费券的实际寿命以窗口为准，不以聚合站状态为准。**
- **② `nex-agi/nex-n2.5-mini` / `nex-n2.5-pro`（付费 SKU）**——两条**付费条目整体下架**，但**对应的 `:free` 版本仍在架**。**这是个反向信号：厂商撤掉收费版、只留免费版，通常意味着测试期结束而正式定价未定。**
- **③ `mistralai/devstral-2512`**——Mistral 的编码模型被移除。

**📥 进：一条零价 + 六条付费**

零价侧唯一新进的是 **`stealth/space-bunny-alpha`**（见头条①）。付费侧新增六条：**`z-ai/glm-5.3-prime`**（$2.80/$8.80）、**`qwen/qwen3.8-max-prime`**（$4/$12）、**`aion-labs/aion-3.5`** 与 **`aion-3.5-mini`**（AionLabs 的 GLM 系角色扮演/叙事系统）、**`upstage/solar-mini4`**（35B/A3B、524K，单价极低 **$0.05/$0.20**）、**`openai/gpt-oss-120b:batch`**。**注意这六条一条免费都没有——本期「增量全给付费」的结构延续了。**

**🔬 口径变化：零价 24 不变，但 `:free` 从 21 降到 20**

原因很简单也很容易被忽略：**新进的 space-bunny-alpha 虽然是 $0/$0，但它的 ID 不带 `:free` 后缀**，而退出的 ling-vl 是带后缀的。所以四个数字同时成立：**零价池 24 → 24（持平）、`:free` 后缀 21 → 20（减 1）、带后缀之外的零价条目 3 → 4（增 1）、目录总量 454 → 457（增 3）**。

**教训：只盯「零价池总数」会漏掉成分变化。真正影响你代码的是「`:free` 后缀有几条」**——因为不带后缀的零价条目（`google/lyria-3-*`、`openrouter/free`、现在的 space-bunny-alpha）**随时可能直接转付费价**。

**⚠️ 聚合站滞后：今天两处新实证**

- **① freellm.net 仍然把 `inclusionai/ling-3.0-flash-vl:free`、`nex-agi/nex-n2.5-pro:free` 标为 Online**（其 OpenRouter Provider 页最后更新写 2026-09-23）——**而 OpenRouter 官方目录里前者已从零价池消失、后者付费版已下架**。
- **② AIHubMix 免费池里仍把 `union-alpha-free` 标为「New」**——**但 union-alpha 早在 9/18 就已随 Pareto 揭晓而下线**，这是滞后整整 6 天的一条。

**本页的结论不变：聚合站用来「发现」，官方目录用来「确认」，两者不可互相替代。**

**零价池近五期流水（脚本口径：输入与输出同时为 $0）**

| 日期 | 目录总量 | 零价池 | 其中 `:free` | 零价净增减 |
| --- | --- | --- | --- | --- |
| 9/20 | 446 | 24 | 21 | — |
| 9/21 | 446 | 24 | 21 | +0 / −0 |
| 9/22 | 445 | 24 | 21 | +0 / −0 |
| 9/23 | 454 | 24 | 21 | +0 / −0 |
| **9/24（今天）** | **457** | **24** | **20** | **+1 / −1** |

**1M 上下文且 $0 的条目（今天是 7 条）**：`stealth/space-bunny-alpha`（1,000,000，新）、`nvidia/nemotron-3.5-lightning:free`（1,000,000）、`nvidia/nemotron-3-ultra-550b-a55b:free`（1,000,000）、`thinkingmachines/inkling:free`（1,048,576）、`thinkingmachines/inkling-small:free`（1,048,576）、`google/lyria-3-pro-preview`（1,048,576，**音频输出**）、`google/lyria-3-clip-preview`（1,048,576，**音频输出**）。**前五条是文本可用，后两条不是——统计 1M 免费时别把音频算进去。**

---

### ③ 定价新趋势｜国产双「Prime」上架：**GLM-5.3-Prime $2.80/$8.80**、**Qwen3.8 Max Prime $4/$12**——**「更快」开始单独卖钱**

**这一波的重点不是新模型，而是新的定价方式。** 9 月 23 日，智谱与阿里几乎同时把旗下旗舰的**高吞吐版本**单独做成 SKU 上架 OpenRouter：**`z-ai/glm-5.3-prime`** 与 **`qwen/qwen3.8-max-prime`**——**基座能力不变，卖点只有「输出更快」，而价格比基座更高。**

| 项目 | 内容 |
| --- | --- |
| ⚡ GLM-5.3-Prime | **$2.80 / $8.80**（缓存读 $0.56）；**1M 上下文 / 最高 128K 输出**；官网称继承 GLM-5.3 **全部能力**，通过推理加速把**输出吞吐提升 1.5 ~ 2 倍**。目标场景：**长程多轮 agent 编排、实时对话、流式代码生成**。**⚠️ 一个反直觉设计：推理（reasoning）强制开启、不可关闭**，支持 **low / high / max 三档，且 max 是默认值**——**意味着它默认就走最贵最慢的思路，想省钱必须显式调低**。实测：单 provider（Alibaba Cloud Int.）**可用率 100%**、吞吐 **70 tok/s**、延迟 **1.09s**、工具调用错误率 3.77%、**缓存命中率 79.35%** |
| ⚡ Qwen3.8 Max Prime | **$4 / $12**（缓存读 $0.50）；**2.4 万亿参数 MoE 架构**（Vercel 文档口径），**1M 上下文 / 131K 最大输出**，输入支持**文本 + 图像 + 视频**；官方定位同样是「**吞吐提升 1.5 ~ 2 倍**」，面向**编码、办公自动化、长周期 agent 工作流**，宣称支持「**多天自主开发**」。实测：单 provider（Alibaba Cloud Int.）可用率 **98.09%**、吞吐 **66 tok/s**、延迟 **1.52s**、**缓存命中率 88.3%**。**价格比基座 Qwen3.8 Max 更高，且明显贵于 GLM-5.3-Prime** |
| 💰 该看加权实付价 | 因为有缓存，客户实际支付远低于标价：**GLM-5.3-Prime 的加权平均输入价只有 $0.72/百万**（标价 $2.80，**缓存命中率 92.8%**）；**Qwen3.8 Max Prime 加权输入 $0.91/百万**（标价 $4，缓存命中率 88.3%）。**读法：在这类「前缀高度重复」的 agent 场景里，缓存命中率直接决定真实成本，差距能到 3~4 倍。**选型时把「缓存读写单价」和「支持前缀缓存的最小长度」一起对比，**只看输入标价会得出错误结论** |
| 🧭 对免费用户意味着什么 | **没有直接好处——两条 Prime 都没有任何免费入口，也都没进任何免费池。**但它解释了一件更重要的事：**厂商正在把「延迟」变成可以单独收费的商品**，而不是把更快的推理免费送给用户。**所以免费档的定位会更清晰：拿能力基线，不拿吞吐。**如果你的免费通道跑得慢，**别指望厂商会免费提速，那部分能力已经被产品化卖掉了**——正确的应对是把免费档用在**对延迟不敏感**的批处理、离线分析、长文档摘要上。**顺带澄清一个常见混淆：AIHubMix 上的 `coding-glm-5.3-free` 是 GLM-5.3 基座的免费版，不是 Prime。**两者的免费/付费关系不可互推 |

**为什么值得单独立一条**：因为它标志着**国产厂商的定价策略从「降单价」转向「按吞吐分层」**。过去三个月我们看到的是持续降价（GPT-6 Luna 输出降 58%、MiMo 号称 99% off、DeepSeek 低谷价），**而 Prime 这一档第一次明确说：同样的模型，更快的那份要加钱**。**对做成本模型的人，这是必须记进去的一条新维度。**

---

## 🌤️ 次要更新 · 值得记一笔

### 🌐 今天新挖到：AIHubMix 免费池 60 款，$1 换每日 1M token

**这是一个此前没记入本页的聚合网关，今天的免费阵容相当厚：60 款模型全部 $0/百万，覆盖 16 个模型作者。**机制分两档：**① 注册即送 10 次试用调用，免绑卡，永不过期**；**② 一次性充值任意金额（最低 $1）后永久切换到每日额度——100 请求/日、10 请求/分钟、共享 1M tokens/日，每日重置**。**三种协议都支持**：Chat Completions、Messages（Anthropic）、Responses。

**今天标记为 New 的几条**：**`agents-a1-free`**（**上海 AI Lab 的 35B MoE Agent 模型**，262K，文本 + 视觉，主打长程任务——不靠堆参数、靠扩展「Agent 视野」，在多步搜索与长指令遵循上接近万亿参数模型）、`coding-glm-5.3-free`（1.05M）、`coding-glm-5.3-flash-free`（1M，文本+视觉+视频）、`gemini-3.8-flash-free`（1.05M）、`hy3-free`（256K）、`minimax-m2.7-free`、`xiaomi-mimo-v2.6-flash-free` / `-pro-free`（均 1.05M 全模态）。

**⚠️ 两点注意**：① 免费池里**仍挂着 `union-alpha-free` 并标为 New**，**但该模型 9/18 就已下线**——**这是聚合滞后 6 天的实证**；② 官方明确说明「**用量由配额限制而非账单**」，超出配额直接返回 429，**不会自动切付费**（这点比多数网关友好）。**适合：拿 $1 换一条稳定的每日额度池，作为免费档的第二备线。**

### 📌 Dots3-Note Preview 免费期明确到 9/30（还剩 6 天）

小红书 **Dots Studio** 的开源多模态模型 **`dots-3-note-preview`**（**280B 总参 / 16B 激活 MoE、512K 上下文、图文输入**）在 OpenRouter 与官方平台同步免费，**免费档明确标注有效期至 2026-09-30**，**只剩 6 天**。两条获取路径：官方 `studio.dots.ai` 注册建 key，或用 OpenRouter 的 `dots-studio/dots-3-note-preview:free`。**实测口碑不错（200–300B 级里表现好），且支持 tools / structured_outputs / response_format，可当轻量多模态 agent 的底座。建议：如果它在你的候选里，本周之内跑完评估——9/30 之后大概率转付费。**

### 🧭 OrcaRouter / Nous / CommandCode 这几家的最新动态

- **① OrcaRouter**（零加价网关，此前免费档轮换 GLM-5.3 Flash / DeepSeek V4 Flash / 腾讯 Hy3，10 RPM / 50 RPD）本周把重心放在了**可观测性**上：推出 **OrcaReplay**（Apache-2.0，给 Claude Code / Codex / Grok CLI / Hermes 录制「模型调用 + shell 命令 + 文件变更」时间线，可离线重放、也可从任意步骤分叉到另一个模型）、**orca push / orca pull**（把 agent 执行记录在本地与云端之间搬运），以及 **Orca AI Incident Archive**（9/23 上线，354 条 AI agent 安全事件记录，CC BY 4.0，明确区分「真实事故」与「研究演示」）。
- **② Nous Portal**：免费档仍**只含免费模型**，Plus $20 / Super $100 / Ultra $200 对应 $22 / 更高 credits；**其 Hermes Agent 今天仍是 OpenRouter 应用榜第一（1.65T tokens）**——**自研 agent + 免费模型组合是目前最省钱的本地化方案**。
- **③ CommandCode**：Go 档 $1/月换 $10 credits（约 15,000 请求），**但仅限官方 CLI，走 Provider API 会返回 `upgrade_required`**——**想用它的免费额度必须用它的客户端**。

### 📈 OpenRouter 榜单：free 档仍在两个前十榜单里

- **周榜（截至 9/23）**：**GLM 5.3 Flash 19T（+69%）登顶**、**DeepSeek V4.1 Flash 18.4T（+79%）第 2**、Hy4 preview 13T、GPT-5.6 Luna 8.74T、DeepSeek V4 Flash 0731 8.49T、MiMo-V2.5 5.66T、**Nemotron 3 Ultra (free) 5.02T（+44%）第 7——前十唯一的免费档**；Hy3 3.91T、DeepSeek V4 Flash 0423 3.46T、GLM 5.3 3.05T。
- **日榜**：DeepSeek V4.1 Flash 2.81T 第 1（GLM 5.3 Flash −24% 退居第 2）；**MiMo-V2.6-Flash 567B 暴涨 283% 进第 6**。
- **月榜**：GLM 5.3 Flash 54.4T 与 Hy4 preview 52.7T 双双 new 登顶；**Nemotron 3 Ultra (free) 18.1T 第 9，仍是月榜前十唯一免费**。
- **变幅榜**：**Jev 1.13 1.39T new 第 1**、**DeepSeek V4 Flash 0731 (free) 1.09T new 第 2**、MiMo-V2.6-Flash 719B new 第 3。
- **作者份额（9/14 起那周）**：deepseek **25.4%（+9%）**、google 18.6%、openai 17.0%（**−30%**）、z-ai 9.4%（+31%）、qwen 6.7%（+25%）、tencent 6.4%。
- **应用榜**：Hermes Agent 1.65T、Claude Code 1.16T、Kilo Code 483B、Cline 437B、pi 401B、omp 312B(new)、Codex 225B、OpenHands 210B、OpenClaw 201B、DeepSeek Harness 170B(new)。
- **AA 智能指数**：Claude Opus 5.5 **57.6**、Fable 5.1 53.4、**Qwen3.8 Max 53.4**、GPT-6 Astra 52.7、Opus 5 50.8、Grok 4.7 46.4、**MiMo-V2.6-Pro 46.3**。

---

## 🧾 今日免费入口速查 · 先进 + 量大优先

### 今天最值得上的七条（按「量大 + 能用」排序）

| 入口 | 免费额度 | 模型量级 | 状态 / 注意 |
| --- | --- | --- | --- |
| **Space Bunny Alpha**（OpenRouter / Zen · 昨夜新增） | **$0 / $0**；Zen 标注**限时一周** | **1M** / 文本+图+视频；疑似 MiniMax M3.1 | **吞吐 68 tok/s、延迟 0.91s（全站最优）**；可用率 97.27%；**ID 不带 `:free`** |
| **AIHubMix**（今日新挖） | **60 款 $0**；$1 充值 → 100/日 · 1M token/日 | 含 `agents-a1` 35B Agent 与 GLM-5.3 1.05M 档 | **三协议全支持**；免卡 10 次试用；**超配额只回 429 不转付费** |
| **OpenRouter** `nemotron-3-ultra-550b-a55b:free` | $0 / $0（200 请求/日） | 550B / 激活 55B；**1M** | Nvidia 端点；**周榜 5.02T 第 7、月榜 18.1T 第 9，两个榜单前十唯一免费** |
| **OpenCode Zen** `mimo-v2.6-flash-free` | 四列全 Free（限时） | 310B / 激活 15B；**1M + 全模态** | 稳定在架多期；**免费期数据可能用于改进模型** |
| **Dots3-Note Preview**（9/30 到期，剩 6 天） | $0 / $0（至 2026-09-30） | 280B / 激活 16B；512K / 图文 | 支持 tools / structured_outputs；**本周跑完评估** |
| **NVIDIA NIM**（长期兜底） | 40 RPM；**不限调用量** | 含 `glm-5.3` 1.3M 与 Kimi K3 1M | freellm.net 榜首来源（97 分）；**需手机验证** |
| **智谱 z.ai**（永久免费档） | **输入输出全 Free**；无到期日 | `GLM-4.7-Flash` 等；国内直连 | **唯一可以写进长期依赖的一类**；注意与 Prime 付费档区分 |

### 长期兜底组合（无到期日那一类）

- **智谱 z.ai** — `GLM-4.7-Flash` / `GLM-4.5-Flash` / `GLM-4.6V-Flash` **输入输出全 Free，无到期日**（国内直连）。
- **书生 InternLM** — **1.8 亿 tokens/月、免信用卡、无明确到期日**。
- **美团 LongCat** — **每天 5,000 万 token**。
- **Cerebras** — **每天 100 万 token**；**Cloudflare Workers AI** — **每天 1 万 neurons**。
- **OVHcloud AI Endpoints** — **匿名免注册 9 款**，2 RPM。
- **Pollinations** — **免 key 即用**，适合临时脚本。

**组合建议**：**主力**用一条稳的（NIM / 智谱永久免费档），**兜底**用无到期日的（LongCat / InternLM），**试用**用 stealth 与限时券（Space Bunny / Dots3），**临时**用免 key 的（Pollinations）。**四类分开管理，别混在一条配置里。**

---

## 🔎 平台盘点 · 今日快照

### 📊 OpenRouter：**457 款中 24 款零价**（`:free` 20 款）

- 脚本清点时刻：**457 款（较昨日 +3）**，其中**输入与输出同时为 $0 的共 24 款**（带 `:free` 后缀 **20 款**，较昨日 −1）。
- **零价池进出各一条**：进 `stealth/space-bunny-alpha`；出 `inclusionai/ling-3.0-flash-vl:free`（**上游 Novita 免费窗口 9/23 02:30 UTC 到期，如昨日预警兑现**）。
- **付费侧下架两条 nex-agi SKU**（`nex-n2.5-mini` / `nex-n2.5-pro`）——**其 `:free` 版本保留在架**；另下架 `mistralai/devstral-2512`。
- **四条「零价但不带 `:free`」**：`stealth/space-bunny-alpha`（**新增，1M 三模态**）、`google/lyria-3-pro-preview`、`google/lyria-3-clip-preview`（**后两条输出音频**）、`openrouter/free`（200K **自动路由池**）。**写代码漏写 `/free` 会按付费价扣款；这四条则相反，随时可能直接转付费价。**
- **今日新增六条全在付费侧**：`z-ai/glm-5.3-prime`、`qwen/qwen3.8-max-prime`、`aion-labs/aion-3.5` 与 `-mini`、`upstage/solar-mini4`、`openai/gpt-oss-120b:batch`。

### 🆓 零价池近五期流水（输入与输出同时为 $0 的口径）

| 日期 | 目录总量 | 零价池 | 其中 `:free` | 零价净增减 |
| --- | --- | --- | --- | --- |
| 9/20 | 446 | 24 | 21 | — |
| 9/21 | 446 | 24 | 21 | +0 / −0 |
| 9/22 | 445 | 24 | 21 | +0 / −0 |
| 9/23 | 454 | 24 | 21 | +0 / −0 |
| **9/24（今天）** | **457** | **24** | **20** | **+1 / −1** |

五期里目录总量涨了 **11 款**，零价池**净增为 0**；今天第一次出现**「零价持平但 `:free` 后缀减 1」**的结构性变化——**因为补位进来的 space-bunny-alpha 不带后缀。只盯总数的监控会漏掉这个变化。**

### 🔧 OpenCode Zen：**79 → 80 款**（+`space-bunny-free`），免费 ID **11 个**

- `/zen/v1/models` 返回 **80 款**（较 9/23 的 79 款 +1，**零下架**），唯一新增 **`space-bunny-free`**。
- 带免费标记的 ID 共 **11 个**：`big-pickle`、`space-bunny-free`、`jev-1.13-free`、`deepseek-v4-flash-free`、`mimo-v2.6-flash-free`、`mimo-v2.5-free`、`ling-3.0-flash-fin-free`、`nemotron-3-ultra-free`、`nemotron-3.5-lightning-free`、`muse-spark-1.3-contributor-free`、`muse-spark-1.2-contributor-free`。
- 官方**定价页 Free 行 8 款**（Big Pickle、Space Bunny、MiMo-V2.6-Flash、MiMo-V2.5、Ling 3.0 Flash Fin、Nemotron 3 Ultra、Nemotron 3.5 Lightning、Muse Spark 1.3 Contributor），外加 **Jev 1.13 Free**（缓存写列无标价）= **9 款**。**接口名单比定价页多 `deepseek-v4-flash-free` 与 `muse-spark-1.2-contributor-free`，按惯例以定价页为准。**
- 📖 **数据条款四类必须分清**：**Space Bunny = 零保留、不用于训练**（最干净）；**Big Pickle / MiMo / Ling = 免费期数据可能用于改进模型**；**Nemotron 两条 = NVIDIA 试用端点，勿提交个人或机密数据**；**Muse Spark Contributor = 以折扣价换 Meta 训练权**。**控制台的「启用计费」按钮不要点。**
- ⏰ 旧版下线提醒：**小米 `mimo-v2.5-pro` / `mimo-v2.5` 将于 10/21 10:00 下线**，`mimo-v2.5-free` 受此影响——**尽快切 `mimo-v2.6-flash-free`**。

### 🌐 freellm.net：**502+ 款 / 31 家平台 / 240 款实时验证 / 416+ 免绑卡**

- 核验时间 2026-09-24。榜首仍是 **NVIDIA NIM `z-ai/glm-5.3`（97 分，1.3M、40 RPM、周吞吐 177.7B）**，第二 **`z-ai/glm-5.3-flash`（96 分，1.3M、图文视频 PDF）**。
- **今天新进榜的 `Space Bunny Alpha` 直接拿到 71 分**，周吞吐 **288.0B**（可视作昨日上线首日的量）；**Dots3-Note Preview (free) 70 分、周吞吐 686.9B**。
- **⚠️ 该站 OpenRouter 页最后更新仍标 2026-09-23**，把 `ling-3.0-flash-vl:free`、`nex-agi/nex-n2.5-pro:free` 列为 Online ——**与官方目录不符，属滞后。**
- **用法建议**：把它当「**发现新模型与新平台**」的入口（它的收录广度确实是全网最好的之一），**但任何关于「是否还在免费」的判断，一律回官方定价页或官方 API 复核**。本页已累计记录 **5 处以上**它滞后于官方目录的实例。

---

## 📅 到期日历 · 别踩空

### 眼前这一周

- **9/24（今天）** — **文心快码 Comate 测试版限免结束**；**字节 TraeCode Seed 系列 1 折结束**
- **9/25（明天）** — **Jev 在 Vercel AI Gateway 的免费促销结束**（官方原文「Promotional pricing ends on September 25, 2026」）；**Jev 在 OpenRouter beta 与 Zen `jev-1.13-free` 的免费档是否同步收紧，建议明天复看**
- **9/27** — 智谱 AutoClaw 中秋充能季第二阶段结束（付费会员专享）
- **9/30** — **Dots3-Note Preview 免费档到期（还剩 6 天）**；**阿里 Qoder Qwen3.8-Flash 免费用结束**；**腾讯 Hy3 / 文心 4.0 全系列免费期结束**；Merge Gateway GLM-5.3-Flash 1 折结束
- **约 9/30（约一周）** — **Space Bunny Alpha 的「限时免费一周」窗口**（按 9/23 起算；**stealth 池历史上常提前关闭，不要等最后一天**）

### 10 月及以后

- **10/10** — **DeepSeek 低谷价窗口结束**；**腾讯混元 Hy4 preview**（老用户夜间免费）结束；unbiased.ai Pareto 正式发布（即 union-alpha 的真身）
- **10/14** — 珠海算力券申报截止（企业向）
- **10/15** — **阶跃 Step 5 Preview 释放完整 BF16 权重**（许可证待公布）
- **10/21（10:00）** — **小米 `mimo-v2.5-pro` / `mimo-v2.5` 正式下线**，Zen 的 `mimo-v2.5-free` 受影响
- **11/7** — MiniMax 开放平台 M3 / M2 免费试用到期（**已从更早日期延期到 11/7**）
- **12/31** — 腾讯云 TokenHub / 华为云码道 / 移动云 MoMA 年度额度截止；微信小程序成长计划二期报名截止

---

## 🧭 今天该怎么动

### ① 现在就做（5 分钟内）

**把 Space Bunny Alpha 接到你正在跑的编码 agent 上试一次。**它今天同时满足量大（1M）、能用（编码 + 工具调用 + 三模态）、先进（疑似未发布的 M3.1）三条，而且**吞吐 68 tok/s、延迟 0.91s 是全站最优档**——**这是近期少有的「免费档比付费档还快」的窗口**。接法很简单：OpenRouter 用 `stealth/space-bunny-alpha`，Zen 用 `space-bunny-free`；**注意 OpenRouter 那条不要加 `:free` 后缀**。

**顺手做一件防呆的事：检查你所有配置里写死的免费模型名。**今天这次换血给出了一个很干净的教材——`ling-3.0-flash-vl:free` 在「下游窗口已过期」的状态下又活了整整一天才消失，**而聚合站到现在还标着 Online**。**如果你的生产链路里有任何一条写死的 $0 通道，今天就是加备线的好日子。**

### ② 今天之内

**给免费档按「数据条款」而不是按「价格」分一次类。**今天 Zen 上同时摆着四类完全不同的免费：**零保留不训练**（Space Bunny）、**可用于改进模型**（Big Pickle / MiMo / Ling）、**明确仅供试用、勿传机密**（Nemotron 两条）、**用数据换折扣**（Muse Spark Contributor）。**四类的价格都是 $0，但能放的内容天差地别。**把这条标签补进你的配置注释里，成本几乎为零，收益是避免一次真实的数据事故。

**如果你的任务对延迟敏感，今天适合做一次「免费 vs Prime」的对照实验**：用 `coding-glm-5.3-free`（AIHubMix 或 Zen）与 `glm-5.3-prime`（付费）跑同一个任务集，量出**吞吐差（1.5~2 倍）与成本差（标价 $2.80 但加权实付 $0.72）**。**这会直接告诉你「哪些任务值得为速度付溢价」——这个结论会跟着你很久。**

### ③ 本周之内

- **① 给 stealth 类模型定一条纪律**：只用于试用与评估，**永不进依赖链**。三代 stealth 的寿命摆在眼前——ox-alpha 6 天、union-alpha <2 天、Space Bunny 计划一周。**正确做法：把它当「提前摸到下一代模型」的福利，用它的结论去决定要不要迁移到正式模型，而不是把工作流建在它上面。**
- **② 把「缓存命中率」纳入选型表**：今天两条 Prime 的加权实付价（$0.72 / $0.91）只有标价（$2.80 / $4）的 **1/4 左右**，差别全在缓存。**如果你的负载是前缀重复度高的 agent 场景，缓存策略本身就是降本手段，优先级不低于换模型。**
- **③ 盯四个日期**：**9/25**（Jev 在 Vercel 免费促销截止）、**9/30**（Dots3 与一批国产免费期集中到期）、**10/15**（阶跃 Step 5 权重开源，许可证是变量）、**10/21**（小米 MiMo-V2.5 全线下线）。
- **④ 留意 MiniMax M3.1 的正式发布**：如果 Space Bunny 的身份被证实，**那意味着 M3.1 快来了，且它大概率会带着新的免费/低价窗口**——在它正式发布前，先把评估框架准备好。

---

## 📋 数据来源

- OpenRouter `/api/v1/models`（9/24 脚本清点，457 款中 24 款 $0、其中 20 款带 `:free` 后缀；已留 `or_models_0924.json`、`zen_0924.json` 供次日 diff）
- OpenRouter 模型页与端点接口（**Space Bunny Alpha**：Uptime 3d 99.08% / Availability 97.27% / 单 provider 96.09%、吞吐 68 tok/s P50、延迟 0.91s、缓存命中 94.66%、工具调用错误率 3.29%、Token 量 Prompt 169B / Completion 2.61B、上线首日 9/23；流量来源 Cline 65.6B、Claude Code 56.8B、Hermes Agent 34.9B、DeepSeek Harness 33.6B、Kilo Code 33.4B）
- **Space Bunny Alpha 身份线索**（分词器指纹 + 异常 token + 报错样式三项交叉验证指向 MiniMax 系；MiniMax Code 开源仓库提前出现 `MiniMax-M3.1` 且测试代码含 1M 上下文与 low/high/max 三档推理强度；探针自称 MiniMax；**官方未确认**）—— lookonchain.com / agihunt.info / tpsreport.news / clawpit.io
- **GLM-5.3-Prime**（$2.80/$8.80、缓存读 $0.56、1M ctx / 128K 输出、reasoning 强制开启、low/high/max 且 max 默认、吞吐 70 tok/s、延迟 1.09s、可用率 100%、缓存命中 79.35%、加权实付输入 $0.721）—— OpenRouter / Z.ai
- **Qwen3.8 Max Prime**（$4/$12、缓存读 $0.50、2.4T MoE、1M ctx / 131K 输出、文本+图像+视频、吞吐 66 tok/s、延迟 1.52s、缓存命中 88.3%、加权实付输入 $0.911）—— OpenRouter / Vercel AI Gateway / LM Market Cap
- **AIHubMix 免费池**（60 款 $0 / 16 位作者 / 免卡 10 次试用 / $1 充值后 100 请求·日 + 10 请求·分 + 1M token·日，三协议全支持；New 项含 `agents-a1-free`（上海 AI Lab 35B MoE Agent，262K，文本+视觉）、`coding-glm-5.3-free`（1.05M）、`coding-glm-5.3-flash-free`（1M）、`gemini-3.8-flash-free`、`hy3-free`、`minimax-m2.7-free`、`xiaomi-mimo-v2.6-flash-free` / `-pro-free`；**仍挂已下线的 `union-alpha-free` 并标 New**）—— aihubmix.com/models/free
- **Agents-A1**（上海 AI Lab 35B MoE 长程 Agent，arXiv 2606.30616，三阶段训练：全领域 SFT → 领域教师 → 多教师 on-policy 蒸馏）—— 上海 AI Lab / 网易智能
- **Dots3-Note Preview**（小红书 Dots Studio，280B / 激活 16B MoE，512K，图文输入，免费档至 2026-09-30，支持 tools / structured_outputs / response_format，官方 `studio.dots.ai`）
- OpenCode Zen `/zen/v1/models`（80 款、免费 ID 11 个）与官方定价页（Free 行 8 款 + Jev 1.13 Free = 9 款；Space Bunny 标注「限时免费」且遵循零保留政策；Big Pickle / MiMo / Ling 免费期数据可能用于改进模型；Nemotron 两条仅限试用；Muse Spark 1.3 Contributor 以折扣换 Meta 训练权）
- freellm.net 核验榜（2026-09-24：502+ 款 / 31 家平台 / 240 款实时验证 / 416+ 免绑卡；榜首 NIM `z-ai/glm-5.3` 97、次 `z-ai/glm-5.3-flash` 96；新进 `Space Bunny Alpha` 71 分 288.0B·周、`Dots3-Note Preview (free)` 70 分 686.9B·周；**其 OpenRouter 页仍标 ling-vl 与 nex-n2.5-pro 为 Online，属滞后**）
- **OpenRouter 榜单**（数据截至 9/23）：周榜 GLM 5.3 Flash 19T(+69%) / DeepSeek V4.1 Flash 18.4T(+79%) / Hy4 preview 13T / GPT-5.6 Luna 8.74T / DeepSeek V4 Flash 0731 8.49T / MiMo-V2.5 5.66T / Nemotron 3 Ultra (free) 5.02T(+44%) / Hy3 3.91T / DeepSeek V4 Flash 0423 3.46T / GLM 5.3 3.05T；日榜 DeepSeek V4.1 Flash 2.81T 第一、MiMo-V2.6-Flash 567B(+283%)；月榜 GLM 5.3 Flash 54.4T 与 Hy4 preview 52.7T、Nemotron 3 Ultra (free) 18.1T 第 9；变幅榜 Jev 1.13 1.39T new / DeepSeek V4 Flash 0731 (free) 1.09T new / MiMo-V2.6-Flash 719B new；作者份额 deepseek 25.4%(+9%) / google 18.6% / openai 17.0%(−30%) / z-ai 9.4%(+31%) / qwen 6.7%(+25%) / tencent 6.4%；应用榜 Hermes Agent 1.65T / Claude Code 1.16T / Kilo Code 483B / Cline 437B / pi 401B / omp 312B / Codex 225B / OpenHands 210B / OpenClaw 201B / DeepSeek Harness 170B；AA 智能指数 Claude Opus 5.5 57.6 / Fable 5.1 53.4 / Qwen3.8 Max 53.4 / GPT-6 Astra 52.7 / Opus 5 50.8 / Grok 4.7 46.4 / MiMo-V2.6-Pro 46.3
- **OrcaRouter**（OrcaReplay Apache-2.0 录制与重放 / orca push·pull / Orca AI Incident Archive 9/23 上线 354 条记录 CC BY 4.0）
- **Nous Portal**（免费档只含免费模型，Plus $20 / Super $100 / Ultra $200；Hermes Agent 荣登应用榜第一）
- **CommandCode**（Go $1/月 = $10 credits ≈ 15,000 请求，仅限官方 CLI，Provider API 返回 `upgrade_required`）
- 国内临期清单（文心快码 Comate 与 TraeCode Seed 1 折至 9/24；文心 4.0 全系列与腾讯混元 Hy3 至 9/30；阿里 Qoder × Qwen3.8-Flash 至 9/30；腾讯 Hy4 preview 至 10/10；MiniMax M3/M2 延至 11/7；微信小程序成长计划二期至 12/31）
- 智谱 z.ai 开放平台永久免费档（`GLM-4.7-Flash` / `GLM-4.5-Flash` / `GLM-4.6V-Flash` 输入、缓存输入、输出均为 Free）
- 小米 MiMo-V2.6 免费通道与旧版下线（Zen `mimo-v2.6-flash-free`、AI Studio、mimo.xiaomi.com、MiMo Desktop；`mimo-v2.5-pro` / `mimo-v2.5` 10/21 10:00 下线）

---

⚠️ 免费额度可能随时调整，请以各平台官网最新政策为准。本页所有「免费」判定均以官方接口或官方定价页为准；涉及额度的具体数字请自行调用官方 Usage API 或查看控制台确认。OpenRouter 免费池日内会波动，457 款 / 24 款零价 / 20 款 `:free` 是脚本清点时刻的快照，不代表全天稳定值。

**`stealth/space-bunny-alpha`（Zen 侧 `space-bunny-free`）为匿名第三方供应商运营，OpenRouter 与 OpenCode 仅负责路由，不承担其开发者/所有者/运营者角色；其「限时免费一周」是当前公告而非承诺，stealth 类模型历史窗口常因负载提前关闭，请勿作为长期依赖，且其身份指向 MiniMax M3.1 属社区推测、官方未确认。**

**第三方聚合榜（freellm.net / AIHubMix / llmpricing.dev 等）与官方目录存在滞后与计数差，本页已记录多处实证（下架模型仍标 Online、已停用模型仍标 New、免费范围变更未反映），请勿单独据其做采购或宣传结论。**

「开源」指权重公开，不代表可自由商用，商用前请逐条核对许可证（尤其 Kimi、GLM、Qwen、MiniMax、Step、MiMo 系列的 Model-as-a-Service 与许可条款）。**Contributor / 试用 / 训练条款类免费档：不要把机密代码、个人信息或生产客户数据放进去。**本页提及的 Prime 类高吞吐 SKU 均为付费档，与同名基座的免费版本不是同一商品，请勿互推。

📅 生成时间：2026-09-24 · 本页由自动化任务每日生成
