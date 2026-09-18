# 免费大模型日报 · 2026-09-18（周五）

> 🤖 AI 每日免费情报 · 全网挖掘 · [在线版 HTML](daily-free-llm-2026-09-18.html)

**今日四个关键数字**

| 数字 | 含义 |
| --- | --- |
| **Pareto 26.9** | 昨天还在猜名字的匿名模型 **Union Alpha** 今天揭晓 = **unbiased.ai**；免费窗口**不到 2 天**被流量打爆，已转付费 |
| **25** | OpenRouter 今日零价模型 **25 款**（`:free` 22 款），新进 2 条重量级、下架 1 条 |
| **9/30** | 阿里 Qoder：**Qwen3.8-Flash 调用不扣 Credits，免费到 9/30**，另加每日登录领 **100 通用 Credits** |
| **29B + 560B** | 国产开源双发 —— 中电信 **星辰 Xing4.0**（全栈国产算力训练）+ 美团 **LongCat-Flash-Chat** |

---

## 🔥 今日头条 · 三条主线

### ① 揭晓｜谜底开了：`Union Alpha` = **unbiased.ai 的 Pareto 26.9**，免费窗口不到 2 天就被流量打爆

9/16 晚间空降、昨天还在猜「是不是智谱 GLM」的那个匿名模型，**今天答案出来了**：它就是 **unbiased.ai 的新模型 `Pareto 26.9`**。官方解释得很清楚——匿名发布是想**先看真实用户的反应**，摸清规模扩大后会踩哪些坑，再把这些反馈带进 **2026 年 10 月 10 日的正式发布**。

但真实反应比预想猛烈得多：官方 X 账号在试用期发帖说模型当时**每分钟要处理 10 亿个 token**，还顺带喊话「谁手里有闲置 GPU、知道去哪儿找我们」。**在 AWS 协助下一夜把处理能力提升 3 倍，仍然接不住**——原计划一周的免费窗口，**实际只过了一天就提前结束**，转向付费访问。

| 项目 | 内容 |
| --- | --- |
| 已下架 | OpenRouter 上 `stealth/union-alpha` **整个 ID 连付费条目一起消失**（按 union / alpha 全目录扫描零命中）。这解释了昨天免费池为什么凭空少了一条——**不是转付费，是直接没了** |
| 以新名义回归 | 同一个模型现在以 `unbiased/pareto` 在架：**262,144 上下文**、text+image→text、定位「研究 / 编码 / Agent 工作流」的多模态复合模型；除 OpenRouter 外**也在 Cloudflare 上公开** |
| 转付费价格 | 输入 **$2.50** / 缓存读 **$0.25** / 输出 **$7.50**（每百万 token）。官方自称「**不到 Astra 定价的四分之一**」——按 Astra 的 $10 / $50 算这个对比站得住（约 1/4 与 1/6.7）。**但它已经不是免费入口了** |
| 两代 stealth 寿命 | `stealth/ox-alpha`（8/21 上线、8/27 下架）活了 **6 天**；`stealth/union-alpha` 活了 **不到 2 天**。不是「质量变差」，而是**免费策略越来越短命**——只要流量打爆，厂商就有充分理由提前收摊 |

> ⚠️ **最值得抄走的一句话：stealth 池里的「免费一周」是计划，不是承诺。** 昨天日报里我们把它的窗口按「一周」推算到 ≈9/23，今天就被现实推翻了——**决定它何时消失的不是日历，是负载**。所以对这类通道的正确用法只有一种：**当成一次免费压测机会，用完即弃；绝不写进 CI、生产链路或任何需要稳定性的地方**。顺带一个反向收获：官方明说「反馈会带到 10/10 正式发布」，也就是说 **10/10 值得盯一下**——这可能是它最后一次带免费额度回场。

---

### ② 免费池｜OpenRouter 零价池 24 → 25：两条重量级 `:free` 变体新进——1M 上下文与多模态各一条

今天一进一退，进来的两条**反而是老面孔、真本事**，出去的那条才是昨天的新消息。

| 新增条目 | 规格 | 付费版对照 |
| --- | --- | --- |
| `deepseek/deepseek-v4-flash-0731:free` | 上下文 **1,048,576（1M）** / 最大输出约 **384K**；纯文本；支持 `reasoning_effort` / `structured_outputs` / `response_format` | `deepseek/deepseek-v4-flash-0731`：输入 **$0.06** / 输出 **$0.12** |
| `qwen/qwen3.8-27b:free` | 上下文 **262,144** / 最大输出约 **230K**；输入 **text + image + video** → 输出 text；端点可用率约 **98.15%**（30 分钟口径 99.92%） | `qwen/qwen3.8-27b`：输入 **$0.214** / 输出 **$2.55** |

**它们是「老模型 + 新发免费券」**：两条的 `created` 分别是 **2026-07-31** 与 **2026-08-14**，**都不是今天**——模型本身早已在架，今天新增的只是带 `:free` 后缀的免费变体。历史快照核对过：9/01–9/17 的每次采样里这两条 `:free` 都从未出现过，所以「今天新进」站得住。

**把这一进一退摆在一起，正好照出免费池里两种完全不同的来源：**

| 维度 | A · 老模型发免费券 | B · 匿名 stealth 试验田 |
| --- | --- | --- |
| 出现在目录的时机 | 任何一天，无预告 | 某天突然出现，上线即 $0 |
| 寿命驱动因素 | **服务商促销预算**——预算停了就悄悄下架 | **厂商预览期安排**——可随时终止、不留痕迹 |
| 已观测寿命 | 数周至数月 | **6 天 → 不到 2 天** |
| 数据条款 | 与付费版一致 | 提示词与补全**可能被提供方保留**，从严处置 |
| 能不能上生产 | **可以，但要留 fallback** | **不可以** |
| 今天的例子 | `deepseek-v4-flash-0731:free`、`qwen3.8-27b:free` | `stealth/union-alpha` 已下架 |

**✅ 好消息**：`z-ai/glm-5.2:free` **端点健康度恢复**——连续第二天 `status = 0`，近 1 天可用率 **81.8% → 99.69%**（30 分钟口径 99.74%）。按 9/16 定的判据，**可以摘掉「降级不可用」标签了**。不过它**不支持工具调用、上下文只有 32,768**——能用了，但别当主力。

**⚠️ 三个坑（今天实测）**

1. `:free` 是**独立 model id**，漏写后缀会调到付费版并扣钱，写代码时把它当常量提出来。
2. **50 次/天是整个免费池共享**，不是每个模型 50 次——「多进两条」不等于「每天多 100 次」。
3. **别用 `stealth/` 命名空间做生产依赖**，两代实测 6 天与不到 2 天。

**1M 免费档盘点**：零价池里 1M 上下文共 **7 条**——`deepseek-v4-flash-0731:free`、`nemotron-3-ultra-550b-a55b:free`、`nemotron-3.5-lightning:free`、`thinkingmachines/inkling:free`、`inkling-small:free`，以及**输出音频**的 `google/lyria-3-pro-preview` / `lyria-3-clip-preview`。

---

### ③ 平台｜阿里 Qoder：`Qwen3.8-Flash` 今天 10:00 起调用不扣 Credits，免费到 9/30，再送每日 100 Credits

阿里 Qoder 今天宣布：**从 9 月 18 日 10:00 起，`Qwen3.8-Flash` 的计费系数由 0.1× 降至 0.0×**——活动期间**每次调用都不扣 Credits**，**免费到 9 月 30 日 23:59:59**。无需领取资格、无需先领那 100 Credits，打开 Qoder 桌面端在模型选择器里选中它即可。

| 项目 | 内容 |
| --- | --- |
| 🆕 每日登录奖励 | 每天 **10:00 开放新一轮**，次日 10:00 前可领，**每账号每轮 100 通用 Credits**；**每笔自领取日起 30 天有效，可累积**，今天没用完能留到后面。官方明说 **「暂时没有结束时间」**——这比限时免费更值钱 |
| 谁能参加 | 国际版：**体验版（免费）/ Pro 试用期 / Pro / Pro+ / Ultra**；CN 版：**体验版 / 专业版 / 高级版 / 旗舰版 / 会员卡**——**包含免费和试用期用户**，新老个人用户都有份 |
| Credit 能在哪用 | 计入 **Add-on Credits（资源包）**，同一账号可在 **Qoder / Qoder IDE / JetBrains 插件 / Qoder CLI / QoderWake / Qoder Cloud Agents / 移动端 / 网页版**使用；**套餐内额度与每天领的奖励可以留给其他模型** |
| 模型本身 | `Qwen3.8-Flash` 是千问**开源权重的多模态 MoE**，擅长**代码编写、长文档处理、图像理解、工具调用**；免费期结束后**按届时公示系数恢复计费** |

**同日呼应**：OpenRouter 今天也把 `qwen/qwen3.8-27b:free` 加进了免费池（262K、多模态）——**Qwen3.8 系列今天在「平台内免费」和「公开 API 免费」两条线上同时开门**。

**怎么读这条**：它和 B.AI 那类「额度型促销」是**两种物种**——B.AI 是把免费**收回**（先关调用量最大的、再关能力最强的、最后清场），Qoder 是把免费**放出来**换取桌面端的使用习惯。对使用者来说，**「限时免费」用来试，「每日可领、30 天有效、暂不设截止」的那部分用来长期兜底**——后者才是这次活动的真正价值。

---

## 🌤️ 次要更新 · 值得记一笔

**⏰ OpenCode Zen：`GPT 5.6 Sol` 五折今天最后一天** — 定价页明写「Prices shown include a 50% discount through September 18, 2026.」折后（≤272K）**输入 $2.00 / 输出 $10.00 / 缓存读 $0.20**；超 272K 翻倍。同期 `GPT 5.6 Luna`（≤272K）只要 **$0.20 / $1.20**——任务不重的话 Luna 性价比更高。**要用 Sol 的今天之内用完。**

**🇨🇳 中电信开源 星辰 Xing4.0-29B-A4B：国内首个「全栈国产算力 + 国产框架训练」的百亿参数模型** — 9/17 开源，**MoE 总参 29B / 激活仅 4B**，原生 **256K（可扩 512K）**，mHC + MLA + MTP，面向多步规划、工具调用与复杂推理。关键一句：**全程基于昇腾 910C 芯片与 MindSpore 框架训练完成，训练吞吐较开箱状态提升约 96%**。「能推理」与「能训练」隔着整套软件生态，这个数字说明的是**框架层 + 算子层的调优能力**。低比特量化后**消费级显卡即可本地运行**；已上 GitHub / Hugging Face / Gitee / 魔搭 / 魔乐。**权重免费下载，本地跑就是 $0。**

**🐱 美团开源 LongCat-Flash-Chat 560B：27B 激活打出 SWE-bench-V 60.4** — MoE **总参 560B / 单 token 平均激活 27B**（18.6–31.3B），靠「**零计算专家**」按上下文动态分配算力，训练用 PID 控制器把激活参数稳定在 27B。成绩：ArenaHard-V2 **86.50（第二）**、MMLU 89.71、CEval 90.44、τ²-Bench 工具使用超越更大规模模型、TerminalBench **39.51（第二）**、**SWE-Bench-Verified 60.4**、**IFEval 89.65（第一）**、VitaBench **24.30（第一）**。H800 上**单用户 100+ tokens/秒**，输出成本**低至 5 元/百万 token**。权重、代码与技术文档已在 GitHub / Hugging Face 开源。

**📖 书生 InternLM：不看促销周期的那条线——每月 1.8 亿 tokens，无明确到期日** — 今天免费池进出这么勤，正好提醒：**你需要一条不看促销周期的兜底线**。书生**每月固定 1.8 亿 Tokens（输入 90M + 输出 90M），无明确到期日**；限速 **30 RPM / 300K TPM**；模型含 `intern-latest`（→397B，256K）、`intern-s2-preview-397b` / `-35b`、`intern-s1-pro`（**内置联网搜索**）、多模态 `internvl3.5-241b-a28b`。**注册即可、无需信用卡**，额度可线上申请提额，走 OpenAI 兼容接口。**它不便宜在单价，便宜在不用每天盯着它会不会消失。**

**🌐 Google 开源 TranslateGemma：55 种语言、可完全离线运行** — 基于 Gemini 训练、Gemma 3 系 12B：覆盖 **55 种语言**，支持**完全离线运行**，面向端侧与边缘设备；量化后约 **7.2GB，普通 CPU 服务器即可流畅跑**，并且是**图文双模态**（能识别图片里的文字再翻译）。同周 Google 还发布了 **Gemini 3.8 Live / 3.8 Live Extended Thinking** 近实时语音模型，并称语言技术已覆盖 **300+ 种语言、全球 86% 人口**。做本地化 / 多语言工单 / 无网部署的团队，这是**零 API 成本**的一条路。

**🍎 Meta Muse for Mac 上线：个人智能体进桌面，免费额度没变** — Meta 于 9/17 晚间推出 **Muse for Mac**：在用户**明确授权**下可直接在电脑上干活——整理下载文件夹、查找丢失文件、总结消息笔记。**注意免费额度没有变**，仍是每周最高 **1 亿 token**，另有 **$20 / $100** 两档订阅。边界：**美国区、Mac 端**。一句话——**这不是「新增免费额度」，是 Muse 从网页/手机产品变成了桌面产品**。

**🏢 Salesforce × NVIDIA Koa：拿免费池里的 `Nemotron 3 Super` 做成了企业产品** — 发布 CRM 领域专用推理模型 **Koa**，**基于 Nemotron 3 Super 深度定制**，针对销售话术、客户分析、工单处理、销售预测优化，可直接部署进 Salesforce 现有产品体系。值得注意的不是 CRM，而是信号：**本周 OpenRouter 免费池里那条 `nemotron-3-super-120b-a12b:free`，底座正在被做成企业级付费产品**——**免费开放权重 → 别人拿它做垂直产品**，这条链今年越来越短。

**🔢 Stable AI × 清华 LimiX-2：400M 表格数据基础模型，三个榜单自报第一** — **400M 参数**的结构化 / 表格数据基础模型，采用 **Contextual Mechanism Networks**。**一个 checkpoint、一次前向**就同时完成分类、回归与缺失值填补，不需按任务微调。自报 Elo：**TabArena 1935 / BCCO 1432 / TALENT 1506，三项均称第一**。权重与推理代码在 Hugging Face `stable-ai/LimiX-2`。**做数据分析 / 异质表批处理的，值得先在自己的 schema 上做 holdout 验证再替换现有 AutoML 管线。**

---

## 🧾 今日免费入口速查 · 先进 + 量大优先

| 入口 | 能调到的先进模型 | 额度 / 价格 | 门槛 |
| --- | --- | --- | --- |
| **OpenRouter**（今日 +2 / −1） | 今日新增 `deepseek/deepseek-v4-flash-0731:free`（**1M / 384K 输出 / 结构化输出**）与 `qwen/qwen3.8-27b:free`（262K、**text+image+video**）；零价池 **25 款**（`:free` 22 款），1M 档 7 条；另有 `nemotron-3-ultra-550b-a55b:free`（1M）、`thinkingmachines/inkling:free`（1M 全模态）、`ling-3.0-flash-vl:free`（视觉+视频）、`nex-n2.5-pro:free`（262K） | **$0**；`:free` 约 **20 RPM / 50 RPD（全池共享）**，累计充值满 $10 后升到 **1000 RPD**；另有自动路由池 `openrouter/free`（200K） | 注册即可，免信用卡 |
| **阿里 Qoder**（今日新增） | `Qwen3.8-Flash`（开源权重多模态 MoE，擅长代码 / 长文档 / 图像理解 / 工具调用），**计费系数 0.1× → 0.0×** | **$0 至 9/30 23:59**（调用不扣 Credits）；**每日登录再领 100 通用 Credits，30 天有效、可累积、暂不设截止** | 注册即用；国际版 / CN 版个人用户全覆盖 |
| **OpenCode Zen**（今日 −1） | `nemotron-3-ultra-free`（1M）、`nemotron-3.5-lightning-free`（1M）、`mimo-v2.5-free`、`ling-3.0-flash-fin-free`、`muse-spark-1.3-contributor-free`、`big-pickle`（隐身）；**⚠️ Union Alpha 的免费窗口已提前结束** | **$0**；定价页 Free 行 **7 款，全部 limited time**；同页 **GPT-5.6 Sol 五折今天（9/18）最后一天** | 登录拿 Key，客户端内直接选 |
| **NVIDIA NIM**（量大） | `z-ai/glm-5.3`（1.3M，评分 **97**）、`glm-5.3-flash`（1.3M / 944K 输出）、`Kimi K3`（1M，多模态）、`deepseek-ai/deepseek-v4-flash-0731`（1.3M）等 100+ 款开源模型 | **$0**；**约 40 RPM 且调用量不设上限**（单看「量大」最优） | 注册 + **手机号验证**；部分端点标注 Trial only |
| **书生 InternLM**（稳定兜底） | `intern-latest`（→397B，256K）、`intern-s2-preview-397b` / `-35b`、`intern-s1-pro`（**内置联网搜索**）、多模态 `internvl3.5-241b-a28b` | **每月 1.8 亿 Tokens**（输入 90M + 输出 90M）；**30 RPM / 300K TPM**；**无明确到期日**，可线上申请提额 | 注册即可，**免信用卡** |
| **Google AI Studio**（多模态） | `Gemini 3.8 Flash`（1M / 66K 输出、视觉+音频、评分 83）；开源侧 `TranslateGemma`（55 语言、可离线、CPU 可跑） | 免费档 **15 RPM / 1,500 RPD**；TranslateGemma 权重开源、本地跑 $0 | Google 账号，免信用卡 |
| **Nous Portal**（Agent 免费） | Hermes Agent（MIT）可白嫖；Portal 免费档只给**免费模型**；付费档打包 **300+ 模型 + Tool Gateway** | **$0**（免费档）→ Plus **$20**（$22 credits）/ Super $100 / Ultra $200 | 注册；Hermes Cloud 需 $2 credit 起 |
| **国内直供**（额度大） | **火山引擎**豆包 2.1 Pro / DeepSeek 系；**智谱** GLM-4.7-Flash（永久免费 200K）+ GLM-5.3 × ZCode 每天 1 亿（**9/20 结束**）；**硅基流动** 100+ 模型；**腾讯 TokenHub** 混元；**本地**星辰 Xing4.0 / LongCat 权重 | 火山 **200 万 Tokens/天**（零点刷新不累积）；TokenHub 每模型 **100 万 / 1 年**；硅基流动新用户约 **2000 万**；百炼每模型 100 万 | 需实名；**⚠️ 腾讯老混元平台 2026 年 9 月底停服，新项目直接上 TokenHub** |

> **一句话选型**：想今天就把「先进模型 + 零成本」拿到手，走 **OpenRouter 新进的 `deepseek-v4-flash-0731:free`（1M + 结构化输出）** 和 **Qoder 的 `Qwen3.8-Flash`**（0 系数 + 每日 100 Credits）；想要**长期不担心额度**，走 **NVIDIA NIM**（40 RPM 不限量）或 **书生 InternLM**（1.8 亿/月、无到期日）；想要**本地零成本**，今天有 **Xing4.0-29B（消费级显卡）** 和 **TranslateGemma（CPU 可跑）**；**匿名 stealth 通道的窗口期已证明可以短到 2 天以内——别写死、别上生产。**

---

## 🔎 平台盘点 · 今日快照

**📊 OpenRouter：446 款中 25 款零价（`:free` 22 款），净增 1、下架 1**

- 脚本口径 `pricing.prompt == '0' 且 pricing.completion == '0'`：**25 款**（9/17 为 24）；id 以 `:free` 结尾的 **22 款**（9/17 为 20）。**进 2、出 1，净增 1。**
- 新增 2 条零价：`deepseek/deepseek-v4-flash-0731:free`（1M / 384K 输出 / 结构化输出）、`qwen/qwen3.8-27b:free`（262K / text+image+video）。
- 退出 1 条零价：`stealth/union-alpha`——整个 ID 从目录中消失（非转付费）。
- 目录总数 **444 → 446**（+2）：除两条 `:free` 外，新进 `unbiased/pareto`（Union Alpha 转付费后的正式条目，$2.50 / $7.50 / 262K）、`openrouter/pareto-code`（Pareto 动态路由）。
- 1M 上下文免费档共 **7 条**；另有零价但非 `:free` 的自动路由入口 `openrouter/free`（200K）。
- ⚠️ 免费池**日内会波动**，25/22 是脚本清点时刻的快照，不代表全天稳定值。已留 `or_models_0918.json` 供次日 diff。

**🏆 OpenRouter 周榜（截至 9/17）：GPT-5.6 Luna 15.8T 居首，`Nemotron 3 Ultra (free)` 前十唯一免费**

1. GPT-5.6 Luna **15.8T** · 2. **DeepSeek V4.1 Flash 11.8T**（跃升）· 3. Hy4 preview **11.6T**（+39%）· 4. GLM 5.3 Flash **11.4T**（+7%）· 5. DeepSeek V4 Flash 0731 **10.6T**（+14%）
6. MiMo-V2.5 **7.52T**（+46%）· 7. Hy3 **4.69T**（+40%）· 8. DeepSeek V4 Flash 0423 **4.09T**（+14%）· **9. `Nemotron 3 Ultra (free)` 3.64T（前十唯一免费）** · 10. GLM 5.3 **2.56T**（+16%）
- 应用榜：**Hermes Agent 1.78T 第一**、Claude Code 996B、**draco-cascade-bench 861B（新进第 3）**、Kilo Code 583B、Cline 439B、**omp 389B**、pi 369B、Codex 237B、**DeepSeek Harness 194B（新）**、OpenClaw 185B。
- AA Intelligence Index 前五：**Claude Fable 5.1 / Qwen3.8 Max 并列 53.4** → GPT-6 Astra (max) 52.8 → Claude Opus 5 50.7 → Fable 5 49.7；**开权重最好的仍是 `GLM-5.3 (max)` 44.9**、`Kimi K3 (max)` 43.8。

**🔧 OpenCode Zen：71 款零增减；API 免费 ID 9 个 vs 定价页 Free 行 7 款**

- `/zen/v1/models` 返回 **71 款**，与 9/17 **零增减**。
- 带免费标记的 ID 共 **9 个**：`big-pickle`、`union-alpha`、`deepseek-v4-flash-free`、`mimo-v2.5-free`、`ling-3.0-flash-fin-free`、`nemotron-3-ultra-free`、`nemotron-3.5-lightning-free`、`muse-spark-1.3-contributor-free`、`muse-spark-1.2-contributor-free`。
- 官方**定价页 Free 行**是 **7 款**——**与端点 9 个仍不一致**（差的是 `deepseek-v4-flash-free` 与 `muse-spark-1.2-contributor-free`，这两条在定价页走付费价）。**按平台一贯口径，以定价页为准。**
- ⚠️ **注意 Zen 的 Union Alpha 页面仍在架**，但 OpenRouter 侧已下架、并转付费——两个平台的免费窗口并不同步，**要用先自己探活**。
- ⏰ 同页提示 **GPT 5.6 Sol 价格含 50% 折扣，到 2026-09-18**——**今天最后一天**。

**📈 freellm.net：榜首 `z-ai/glm-5.3` 97 分；目录 484 款 / 31 平台**

- 站内计数：**484 款模型 / 31 家平台 / 226 款经 live API 实测 / 390+ 款全程免绑卡**，最近更新 **2026-09-18**。
- 前五：**NVIDIA NIM `z-ai/glm-5.3` 97**（1.3M / 944K 输出 / 40 RPM）→ NIM `glm-5.3-flash` 96 → **OpenRouter `Qwen3.8 27B (free)` 94**（**今日新进免费池**，周用量 448.8M）→ Ollama Cloud `deepseek-v4-pro` 93 → **OpenRouter `DeepSeek V4 Flash 0731 (free)` 93**（周用量 4.1T）。
- 值得注意：**今天新进免费池的两条，直接空降榜单第 3 与第 5**——说明榜单是按真实可用性 + 能力复核的，不只是收录列表。

---

## 📅 到期日历 · 别踩空

**眼前这一周**

- **9/18（今天）** — OpenCode Zen **GPT-5.6 Sol 五折最后一天**（定价页口径）
- **9/20** — 智谱「Flash × ZCode」夜间畅用（23:00–09:00）结束，**还剩 2 天**
- **已发生 ✖** — **Union Alpha 免费窗口已提前关闭**：原按「一周」推算到 ≈9/23，实际 **9/17–9/18 之间就被负载打爆收场**

**9 月下旬及以后**

- **9/30** — **阿里 Qoder Qwen3.8-Flash 免费用结束**；云知声 U2-Flash 1 亿 Tokens 与六折价结束；腾讯 **Hy3 免费期**结束；Merge Gateway GLM-5.3-Flash 1 折结束；**腾讯老混元平台停服**
- **10/10** — **unbiased.ai `Pareto` 正式发布日**（官方称匿名试用的反馈会带进这一天，值得盯是否重启免费额度）；WorkBuddy Hy4 preview 新用户「首开享 14 天」的最后首开日
- **10/14** — **Bolt Forge 50× 用量预览期结束**；**OpenAI 从全计划下线 GPT-5.5**（Codex 用户需迁到 GPT-5.6 Sol 或 GPT-6 Astra）
- **12/31** — 腾讯云 TokenHub / 华为云码道「码力续航计划」/ 移动云 MoMA 活动截止

---

## 🧭 今天该怎么动

**① 现在就做（5 分钟内）**

**清一下你的配置**：凡是写过 `stealth/union-alpha` 的地方**今天就删掉**——ID 已整体 404，留着只会在生产里报错。想继续用同一个模型的，注意它现在叫 `unbiased/pareto`、价格是 **$2.50 / $7.50**，**先想清楚值不值再换**。
**想白嫖 1M 上下文**：把 `deepseek/deepseek-v4-flash-0731:free` 接进你的 OpenAI 客户端跑一次长文档通读——**记得模型名一定要带 `:free`**，漏写后缀会按付费价 $0.06/$0.12 计费。

**② 今天之内**

**打开 Qoder**：模型选择器切到 `Qwen3.8-Flash`（0 系数、免费到 9/30），顺手点左下角用量面板的 🎁 **把今天的 100 Credits 领掉**——这一轮奖励**每天 10:00 开放、次日 10:00 前有效，错过不补**，而且 **30 天有效可累积**，领到就是净赚。
**还在用 `z-ai/glm-5.2:free` 黑名单的**：放出来重测一次，端点状态已连续两天回到 0、可用率 99.69%。
**想省钱的 Sol 用户**：五折今天到期，把今天的重活先跑完。

**③ 本周之内**

1. **把「免费来源分类」变成习惯**：看到新的 $0 条目先问一句——**它是「老模型发免费券」（来源 A，可当日常后端但要留 fallback）还是「匿名 stealth 试验田」（来源 B，用完即弃）**？判据只有两个：`created` 是否早于今天、付费版是否一直在架。
2. **给免费模型留 fallback**：今天的教训是**窗口可以短到 2 天以内**，所以任何依赖单条免费通道的链路都应有一条可切换的备线（NIM / InternLM 是最稳的两条）。
3. **把「兜底线」配好**：书生 **1.8 亿 tokens/月、无到期日、免信用卡**——注册一次，以后每天的新免费额度都当增量，而不是主粮。
4. **本地零成本**值得试：**星辰 Xing4.0-29B**（消费级显卡可跑、256K）和 **TranslateGemma**（CPU 可跑、55 语言）今天都能下载。

---

**数据来源**：OpenRouter `/api/v1/models`（9/18 脚本清点，446 款中 25 款 $0 / 22 款 `:free`，已留 `or_models_0918.json`）· OpenRouter 模型页与 Rankings（截至 9/17 的周榜与 Apps 榜）· OpenCode Zen `/zen/v1/models`（71 款）与官方定价页（Free 行 7 款 + GPT-5.6 Sol 五折至 9/18）· Union Alpha 身份与转付费定价（unbiased.ai Pareto 26.9、每分钟 10 亿 token、AWS 扩容 3 倍仍不足、$2.50/$0.25/$7.50、10/10 正式发布）——163 网易号《匿名AI模型上线1天就被挤爆》9/18 10:52 报道 · OpenRouter 免费池端点体检与《每日免费API资讯 2026-09-18》口径核对 · 阿里 Qoder 官方活动页（9/18 10:00 起 Qwen3.8-Flash 系数 0.1×→0.0×、免费至 9/30、每日 10:00 领 100 通用 Credits）与 IT之家 / 新浪 / 网易 / 腾讯新闻同日报道 · 中电信人工智能公司 Xing4.0-29B-A4B 开源（9/17，昇腾 910C + MindSpore、吞吐 +96%、256K/512K）· 美团 LongCat-Flash-Chat 560B 开源（9/17）· Google TranslateGemma 开源与 Gemini 3.8 Live 发布 · Meta Muse for Mac 上线（9/17 晚间）· Salesforce × NVIDIA Koa（基于 Nemotron 3 Super）· Stable AI × 清华 LimiX-2 · 书生 InternLM 官方额度口径（1.8 亿 tokens/月）· NVIDIA NIM 模型目录与 freellm.net 核验榜（484 款 / 31 平台 / 226 live / 390+ 免绑卡）· Nous Portal / Oxlo.ai / TypeSafe AI 官方定价说明 · pricepertoken.com 模型发布流 · OpenRouter Free Router 官方行为说明。

⚠️ 免费额度可能随时调整，请以各平台官网最新政策为准。本页所有「免费」判定均以官方接口或官方定价页为准；涉及额度的具体数字请自行调用官方 Usage API 或查看控制台确认。OpenRouter 免费池日内会波动，25 款 / 22 款是脚本清点时刻的快照，不代表全天稳定值。**隐身 / stealth 模型的窗口期与身份以官方口径为准，本页涉及的推测均已标注来源，请勿据此做采购或宣传结论。**「开源」指权重公开，不代表可自由商用，商用前请逐条核对许可证（尤其 LongCat、Kimi、GLM、MiniMax 的 Model-as-a-Service 条款）。

📅 生成时间：2026-09-18 · 本页由自动化任务每日生成
