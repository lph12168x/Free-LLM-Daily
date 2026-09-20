# 免费大模型日报 · 2026-09-20（周日）

> 🤖 AI 每日免费情报 · 全网挖掘 · [在线版 HTML](daily-free-llm-2026-09-20.html)

**今日四个关键数字**

| 数字 | 含义 |
| --- | --- |
| **$0** | 「不聊天的模型」也能免费了：**TypeSafe `Jev`** 进 Zen 免费池（`jev-1.13-free`），同周被 **9B 开源模型两天复现** |
| **24** | OpenRouter 今日零价 **24 款**（`:free` 21 款）；**两天前刚上的 1M 免费券 `deepseek-v4-flash-0731:free` 已下架** |
| **Omni + 2.8T** | 9/19 国产双响：千问首款 Agent 多模态 **Qwen3.8-Omni-Flash**（音视频）+ **Kimi K3 上架 Amazon Bedrock** |
| **9/20** | 智谱「Flash × ZCode」夜间免费**今天最后一天**；千问办公 × 杭州 Token 卡**今天起**向 35 家创业园发放 |

---

## 🔥 今日头条 · 三条主线

### ① 新物种｜「不聊天」的模型也能免费了：TypeSafe `Jev` 登陆 OpenCode Zen 免费池，开源侧 9B 两天复现

**Jev 是本周最不像「大模型」的一个模型**——它**不生成文字**，只输出「**带概率的类型化决策**」。你给它一段状态（工单 / 邮件 / trace）和一组问题，它返回 Choice / Score / Boolean 加**校准概率**，**70–500 毫秒出结果**，而不是把一段 JSON 一个字符一个字符拼出来。今天它正式进入 OpenCode Zen 免费池。

| 项目 | 内容 |
| --- | --- |
| 🆕 `jev-1.13-free`（Zen） | 完全 **$0** 的免费 ID；同页还有付费版 `jev-1.13`——输入 **$0.042 / 百万 token**、**输出 $0**（官方话术「too cheap to meter，便宜到不值得计量」）。端点走 `/zen/v1/systemone`，是**独立协议、不是常规 chat** |
| 定价与定位 | TypeSafe AI **9/15 出隐身**，**$4,000 万种子轮由 DCVC 领投**；官方自称输入比 Claude Fable 5.1 **便宜约 238×**，并坦承这个价**可能被补贴**。上下文 32K / 64K，**选项上限 255**，**保证不出现 schema 之外的字段**（但仍可能「选错」） |
| 开源侧两条线（同周） | Browser Use 开源 `jev-ultrafast`：基于 Jev 的浏览器 agent，Google Flights 苏黎世→伦敦 **7.1 秒 / $0.0039**；Bespoke Labs 用 **Qwen3.5-9B 做 LoRA 微调（2 天、2,676 条样本）**，在 324 题内部评测上 **90.12%**（Jev 93.21%、原始 Qwen 66%），H100 上 **100ms** |
| ⚠️ 两个提醒 | 有观察者指出 Bespoke Nimble **绕过了 Jev 的使用条款**；且这一类模型**没有公认基准**，跨评测集不可直接比较。Zen 的免费档与付费 ID 是**两条独立条目**，额度规则不同 |

**为什么值得记一笔**：它把「分类、路由、打分、门禁」这类**输出本就是有限集合**的任务，从「让聊天模型拼 JSON」里拆了出来——**成本降 2–3 个数量级、延迟降一个数量级**。如果你 Agent 里一大半调用其实在「五选一」，这是本周最值得做的一次架构自检。

**三个坑**：① 它**不能写代码、不能答开放题**（这是设计，不是缺陷）；② `jev-1.13-free` 与 `jev-1.13` 是**两个 ID**，别混用；③ 输出 token **免费但仍在计用量**，别把 `output_tokens` 当解码速度读。

---

### ② 免费池｜OpenRouter 零价池 25 → 24：`deepseek-v4-flash-0731:free`（1M 上下文）两天即下架，Zen 同步摘掉 `union-alpha`

今天这一条，正好把「免费券」的短命演示了一遍：**9/18 日报的头条新进项 `deepseek/deepseek-v4-flash-0731:free`，今天整个 ID 从目录里消失了**。

| 项目 | 内容 |
| --- | --- |
| 🆓 今日清点 | 446 款中零价 **24 款**（`:free` **21 款**），比 9/18 的 25 款（`:free` 22）**净减 1**。口径：`pricing.prompt == '0' 且 completion == '0'` |
| ❌ 退出 | `deepseek/deepseek-v4-flash-0731:free`（1,048,576 ctx / 384K 输出 / 结构化输出）——**连付费条目 `deepseek/deepseek-v4-flash-0731` 都还在架，只有 `:free` 变体没了**。这是「老模型发免费券」类的典型死法：**预算停了就悄无声息下架，不留公告** |
| 🆕 新增（均为付费） | `z-ai/glm-5.3-flashx`（**1M** / text+image+video→text，$0.37 / $1.25 / 缓存读 $0.075）、`prism-ml/ternary-bonsai-2-27b`（262K / text+image，**三值（ternary）量化模型**，$0.075 / $0.50） |
| 🧹 同步下架 | Zen 侧 `union-alpha` 已从 74 款目录中移除——**两代 stealth（`ox-alpha` 6 天 → `union-alpha` 不到 2 天）现在在两个平台都归零** |

**零价池近四期流水**

| 清点日 | 零价总数 | 其中 `:free` | 关键进出 |
| --- | --- | --- | --- |
| 9/15 | 19 | 19 | 零增减 |
| 9/17 | 24 | 20 | 进 nex-n2.5 双条 |
| 9/18 | 25 | 22 | 进 `deepseek-v4-flash-0731:free` + `qwen3.8-27b:free`；出 `union-alpha` |
| **9/20（今天）** | **24** | **21** | **出 `deepseek-v4-flash-0731:free`（1M）**；无新进零价 |

> ⚠️ **口径冲突（今天实测）**：freellm.net 今天仍把 `DeepSeek V4 Flash 0731 (free)` 标为 **Online（周用量 1.1T）**，但 OpenRouter 官方接口已经查不到它。**这就是第三方聚合站的典型滞后**——判定「是否免费」一律回官方接口，别信二手清单。

**1M 免费档还剩 6 条**：`nemotron-3-ultra-550b-a55b:free`、`nemotron-3.5-lightning:free`、`thinkingmachines/inkling:free`、`inkling-small:free`，外加两条**输出音频**的 `google/lyria-3-pro-preview` / `lyria-3-clip-preview`。（昨天是 7 条，少的就是今天下架的那条。）

**读法**：**免费券的寿命已经实测短到 2 天以内**，而且这次是「来源 A 老模型发券」也没撑住——说明**「老模型 = 稳定」这个直觉也不再成立**。任何依赖单条 `$0` 通道的链路，都必须有一条可切换的备线。

---

### ③ 国产｜9/19 双发：千问首款 Agent 多模态 `Qwen3.8-Omni-Flash`（音视频，定价不到 Gemini 两成）+ `Kimi K3` 上架 Amazon Bedrock

周日不静——**9 月 19 日国内两条主线同时落地**，一条在「多模态 Agent 定价」，一条在「开源模型进场云平台」。

| 项目 | 内容 |
| --- | --- |
| 🆕 `Qwen3.8-Omni-Flash`（9/19） | 千问首款**面向 AI 智能体**的多模态模型：**音频 + 视频同步处理**，1M 上下文，可自主调用工具完成 **vlog 剪辑、短视频翻译、影视内容摘要**。已通过 **Qwen Studio / Qwen Cloud / 官方 API** 开放 |
| 💵 定价（对比 Gemini） | API **$0.15 输入 / $0.47 输出**（每百万）。对标 Gemini 3.8 Flash 的 **$0.75 / $3.75**——**不到两成**，且 Gemini 该价 **2027/1/1 起还要翻倍**。音频输入**每小时 < $0.01**；带音轨 720p 视频按每秒 1 帧采样 ≈ **$0.20** |
| 🆕 配套开源 | **Qwen-MM-Plugins**：给 Claude Code / Gemini CLI / Qwen Code 补上**视频剪辑、说话人识别、PDF 视频笔记、可复用工作流**；**Qwen-Live Harness**：可调摄像头与麦克风做实时交互。**都是免费开源组件** |
| ☁️ `Kimi K3` 上 Bedrock（9/19） | **2.8 万亿参数**，官方称「首个达 3T 量级的开源模型」；原生视觉、**1M 上下文**、相对 K2 **约 2.5× 扩展效率**（896 专家 / 每 token 激活 16，Stable LatentMoE + Kimi Delta Attention）。**首个支持显式提示缓存的 Bedrock 开源权重模型**（前缀 ≥1024 token，缓存保留 ≥30 分钟） |

**K3 定价与免费入口**：Bedrock 定价缓存命中 **$0.30** / 未命中 **$3.00** / 输出 **$15.00**。**⚠️ K3 在 Zen 也是付费（$3 / $15）——它当前唯一的免费入口是 NVIDIA NIM（1M 上下文，40 RPM 不限量）。** 同日消息：月之暗面已递交港股 IPO 方案。

**顺带第三条 `Atria Dawn`**：上海 AI Lab（InternLM 团队）——**744B MoE、基于 GLM-5.2 基座、256K、MIT 许可**，提供 **FP8 与昇腾 w8a8** 量化权重（HF 显示 artifact ≈753B）。定位科学研究 / 工程 / 网络安全等智能体工作流。**「拿别人的前沿基座做智能体特化」正在变成开源主流打法**——本周第三个重量级。

**读法**：这三条合起来是一个信号——**能力在往「多模态 + Agent + 长上下文」压，而价格在往「不到闭源两成」压**。做音视频 / 长文档 Agent 的，本周值得把 **Qwen Studio 的免费档**和 **NIM 上的 K3** 都跑一遍再决定后端。

---

## 🌤️ 次要更新 · 值得记一笔

### 🎁 Meta `Muse Spark 1.3 Contributor Free` 登陆 Zen：用你的提示词换免费

Zen 免费池里现在挂着 Meta 的 Contributor 档：**免费，代价是提示词与补全会被用于训练 Meta 未来的模型**。规格很硬——**1,048,576 上下文、text+image+video→text**；官方自报 **DeepSWE 75.4（高于 Opus 5 的 74）、MRCR 98.5**；社区实测 Zen 上 **206.3 tok/s**，high quality 下体验「接近 Opus 5」。标准档是 **$1.25 / $4.25**，Contributor 直连档 **$0.10 / $0.20**，Zen 上目前是 **$0**。同页还有 `muse-spark-1.2-contributor-free`。**边界很硬：不要把机密代码、个人信息、生产客户数据放进去**；公司禁用「训练条款」的请用标准档。

### ⏰ 智谱「Flash × ZCode」夜间免费今天（9/20）最后一天；ZCode 爆隐私争议

夜免窗口——**每晚 23:00–09:00（北京时间）**，ZCode 内 `GLM-5.3-Flash` **额度消耗为 0**，其他支持的 Agent **额度翻倍**——**今天就是最后一天**，仅限付费 GLM Coding Plan 用户。同时 ZCode 冲上热搜：**默认开启的仓库索引会把整个项目快照（含完整 Git 提交历史）上传云端、界面无一键关闭**。官方已致歉，称云端生成后即销毁不留存，**已关闭该默认配置**，并计划**开源代码库 + 引入第三方安全审计 + 给全体用户重置一次周额度**。**涉及涉密 / 商业源码的项目，用之前先评估数据风险。**

### 🆕 千问办公 × 杭州：9/20 起向 35 家创业园发 Token 卡，每张约 500 元额度

杭州「千问办公」联名 Token 卡**今天（9/20）起**向 **35 家创业园**发放，**每张约等于 500 元额度**。配合杭州此前 44%–55% 的 Coding 补贴，**本地创业团队值得今天去园区问一句发放口径与领取条件**（一般需企业 / 园区资质）。另有一条面向企业的：**珠海算力券**——企业向、**每年最高 200 万**，**申报截止 10/14**。这两条都不是「模型额度」，而是**直接抵现金的算力补贴**，量级远超一般的免费 token 活动。

### 💰 Command Code `GOAT`：$10 换 $70 额度（7×），OpenCode Go 的正面竞品

Command Code 是一个编程 Agent 框架，订阅以**永不过期的 credits** 计量；**七档覆盖 $1–$200/月**，另有**零加价的 Provider API 附加项**。招牌 **GOAT 档 $10 换 $70 额度（7×，活动后 >10×）**，覆盖 **48 款开源与闭源模型**。同价位对比：**OpenCode Go $10/月**（含 Muse Spark 1.3 Contributor；DeepSeek V4.1 Flash 当前 75% 折扣，即 4× 用量）。**性价比属第一梯队，但都是付费订阅——不是免费额度。**

### 🧰 两条「几乎全免费」的聚合路线：`9Router`（开源）与 `OrcaRouter`

**9Router**：MIT 开源的本地路由，免费 Provider 组合——**iFlow 8 款不限量 + Qwen 3 款不限量 + Kiro 的 Claude Sonnet 4.5 / Haiku 4.5（AWS Builder ID）+ Gemini CLI 每月 18 万次**，官方 FAQ 直接写「**只用免费 Provider 可以永远免费编码**」。**OrcaRouter**：DeepSeek V4 线免费 ID（`deepseek/deepseek-v4-flash-free`、`deepseek/deepseek-v4-pro-free`）+ **`orcarouter/free` 难度路由**（按难度自动挑免费模型、绝不碰钱包）；免费模型需**有历史的 GitHub 账号**，另有 voucher / 学生 / hackathon 额度。两条都**零成本、可自托管或免卡注册**。

### 📊 freellm.net：目录涨到 503+ 款 / 31 平台；榜首仍是 NIM `z-ai/glm-5.3`（97）

站内计数 **503+ 模型 / 31 家平台 / 244 款经 live API 实测**；榜单前五：**NIM `z-ai/glm-5.3` 97** → `glm-5.3-flash` 96 → **OpenRouter `Ling 3.0 Flash Sante (free)` 95** → `Qwen3.8 27B (free)` 93 → `DeepSeek V4 Flash 0731 (free)` 93。⚠️ 注意：**榜上第 5 那条其实已在 OpenRouter 下架**（见头条②）——这正是「聚合榜滞后于官方目录」的现场样本。参考项：Agnes AI `agnes-2.0-flash` 87（256K / 30 RPM）、Google `Gemini 3.8 Flash` 83（1M / 15 RPM / 1500 RPD）。

---

## 🧾 今日免费入口速查 · 先进 + 量大优先

按「能直接调、模型够先进、额度够大」三条筛过一遍：

| 入口 | 能调到的先进模型 | 额度 / 价格 | 门槛 |
| --- | --- | --- | --- |
| **OpenCode Zen**（今日 +3 / −1） | **今日新增 `jev-1.13-free`**（决策层模型，**输出 typed decisions + 校准概率**）；另新增付费 `deepseek-v4.1-flash`、`qwen3.8-flash`；免费池还有 `muse-spark-1.3-contributor-free`（1M 全模态）、`nemotron-3-ultra-free`（1M）、`nemotron-3.5-lightning-free`（1M）、`mimo-v2.5-free`、`ling-3.0-flash-fin-free`、`big-pickle`（隐身）。**⚠️ `union-alpha` 已下架** | **$0**；定价页 Free 行 **7 款**、**全部 limited time**；`jev-1.13-free` 与 `muse-spark-1.3-contributor-free` 是当前最值得试的两条 | 登录拿 Key，客户端内直接选 |
| **Qwen 千问**（今日新增） | **`Qwen3.8-Omni-Flash`**（音视频 Agent，1M 上下文，可剪辑 / 翻译 / 摘要）+ 开源组件 `Qwen-MM-Plugins` / `Qwen-Live Harness` | Qwen Studio / Qwen Cloud **免费体验档**；API **$0.15 / $0.47**（不到 Gemini 3.8 Flash 两成） | 注册即用 |
| **OpenRouter**（今日 −1） | 零价池 **24 款**（`:free` 21）；1M 档 `nemotron-3-ultra-550b-a55b:free`、`nemotron-3.5-lightning:free`、`thinkingmachines/inkling:free`（全模态）；多模态 `qwen3.8-27b:free`（262K/text+image+video）、`ling-3.0-flash-vl:free`。**⚠️ `deepseek-v4-flash-0731:free` 已下架** | **$0**；`:free` 约 **20 RPM / 50 RPD（全池共享）**，累计充值满 $10 后升到 **1000 RPD**；另有自动路由池 `openrouter/free`（200K） | 注册即可，免信用卡 |
| **NVIDIA NIM**（量大） | `z-ai/glm-5.3`（1.3M，评分 **97**）、`glm-5.3-flash`（1.3M / 944K 输出）、**`Kimi K3`（1M，K3 当前唯一的免费入口）**、`deepseek-ai/deepseek-v4-flash-0731`（1.3M）等 100+ 款开源模型 | **$0**；**约 40 RPM 且调用量不设上限**（单看「量大」最优） | 注册 + **手机号验证**；部分端点标注 Trial only |
| **书生 InternLM**（稳定兜底） | `intern-latest`（→397B，256K）、`intern-s2-preview-397b` / `-35b`、`intern-s1-pro`（**内置联网搜索**）、多模态 `internvl3.5-241b-a28b` | **每月 1.8 亿 Tokens**（输入 90M + 输出 90M）；**30 RPM / 300K TPM**；**无明确到期日**，可线上申请提额 | 注册即可，**免信用卡** |
| **Command Code**（付费超值） | `GOAT` 档覆盖 **48 款开源与闭源模型**；Provider API 附加项零加价 | 七档 **$1–$200/月**；招牌 **$10 换 $70 额度（7×）**，credits 永不过期 | 注册；**付费订阅** |
| **国内直供**（额度大） | **智谱** GLM-4.7-Flash（永久免费 200K）+ GLM-5.3 × ZCode 每天 1 亿（**9/20 结束**）；**火山引擎**豆包 2.1 Pro / DeepSeek 系；**讯飞**星火 X2.5（**限免到 9/23**）；**腾讯**混元 Hy3（免费至 9/30）；**本地** Atria Dawn（744B/256K/MIT，需大集群） | 火山 **200 万 Tokens/天**（零点刷新不累积）；讯飞**限免期 0 积分**；硅基流动新用户约 **2000 万**；百炼每模型 100 万 | 需实名；**⚠️ 腾讯老混元平台 2026 年 9 月底停服，新项目直接上 TokenHub** |

> **一句话选型**：想体验「新物种」，走 Zen 的 **`jev-1.13-free`**（决策层，做路由 / 分类 / 门禁）；想要 **1M + 多模态**，走 OpenRouter 的 **`nemotron-3-ultra-550b-a55b:free`** 或 **`inkling:free`**；想做**音视频**，走 Qwen Studio 的 **`Qwen3.8-Omni-Flash`**；想要**长期不担心额度**，走 **NVIDIA NIM**（40 RPM 不限量）或 **书生 InternLM**（1.8 亿/月、无到期日）；想**零成本本地编码**，试试开源的 **9Router** 多 Provider 组合。**1M 免费券已实测只活 2 天——别写死、别上生产。**

---

## 🔎 平台盘点 · 今日快照

### 📊 OpenRouter：446 款中 24 款零价（`:free` 21 款），净减 1

- 脚本清点 `pricing.prompt == '0' 且 pricing.completion == '0'`：**24 款**（9/18 为 25）；其中 id 以 `:free` 结尾的 **21 款**（9/18 为 22）。**零新进、退 1。**
- **退出 1 条零价**：`deepseek/deepseek-v4-flash-0731:free`——只删了 `:free` 变体，**付费条目 `deepseek/deepseek-v4-flash-0731` 仍在架**。
- 目录总数 **446 → 446**（净 0）：新增 `z-ai/glm-5.3-flashx`（1M / text+image+video）、`prism-ml/ternary-bonsai-2-27b`（262K / 三值模型）；下架 `mistralai/mistral-large-2512` 与那条免费券。
- 1M 上下文免费档共 **6 条**（4 条文本 / 多模态 + 2 条**输出音频**的 `google/lyria-3-*`）；零价但非 `:free` 的自动路由入口 `openrouter/free`（200K）仍在。
- ⚠️ 免费池**日内会波动**，24 / 21 是脚本清点时刻的快照。已留 `or_models_0920.json` 供次日 diff。

### 🏆 OpenRouter 周变幅榜：Jev 1.13 空降第 3；作者份额腾讯 +105%

- **周环比变幅榜**：**1** `DeepSeek V4 Flash 0731 (free)` **1.08T**（new）· **2** `Union Alpha` stealth **977B**（new）· **3 Jev 1.13** **245B**（new）· **4** `GLM 5.3 FlashX` 15.3B（new）· **5** `Qwen3.8 27B (free)` 6.96B（new）。
- 前三名里两条已经或即将不再是免费——**「上榜即巅峰、随即退场」是 stealth 与免费券的共同节奏**。
- **作者份额**（按文本请求）：openai **23.6%**（+28%）· deepseek **22.6%**（+3%）· google **18.6%**（+2%）· **tencent 7.2%（+105%）** · z-ai 7.0%（−22%）· qwen 5.2%（+1%）· anthropic 2.5%（−5%）。
- **应用榜**：**Hermes Agent 1.49T 第一**（Nous 开源自改进 Agent）· Claude Code 917B · Kilo Code 568B · Cline 395B · OpenClaw 163B（新）。

### 🔧 OpenCode Zen：71 → 74 款；免费 ID 9 个 vs 定价页 Free 行 7 款

- `/zen/v1/models` 返回 **74 款**（9/18 为 71）。**新增**：`deepseek-v4.1-flash`、`qwen3.8-flash`、`jev-1.13`、`jev-1.13-free`；**下架**：`union-alpha`。
- 带免费标记的 ID 共 **9 个**：`big-pickle`、`jev-1.13-free`、`deepseek-v4-flash-free`、`mimo-v2.5-free`、`ling-3.0-flash-fin-free`、`nemotron-3-ultra-free`、`nemotron-3.5-lightning-free`、`muse-spark-1.3-contributor-free`、`muse-spark-1.2-contributor-free`。
- 官方**定价页 Free 行**是 **7 款**（Big Pickle / MiMo-V2.5 / Ling 3.0 Flash Fin / Nemotron 3 Ultra / Nemotron 3.5 Lightning / **Muse Spark 1.3 Contributor** / **Jev 1.13 Free**）——**与 models 端点的 9 个仍不一致**（差 `deepseek-v4-flash-free` 与 `muse-spark-1.2-contributor-free`，这两条在定价页走付费价）。**按平台一贯口径，以定价页为准。**
- ⏰ 同页提示：**GPT 5.6 Sol 的五折已于 9/18 到期**，现价回到 $4.00 / $20.00（≤272K）。

### 📈 freellm.net：目录 503+ 款 / 31 平台 / 244 live；榜首 `z-ai/glm-5.3` 97

- 站内计数：**503+ 款模型 / 31 家平台 / 244 款经 live API 实测 / 免绑卡条目持续增长**，最近更新 **2026-09-20**。
- 榜单前五：**NIM `z-ai/glm-5.3` 97**（1.3M / 944K 输出 / 40 RPM）→ NIM `glm-5.3-flash` 96（1.3M）→ **OpenRouter `Ling 3.0 Flash Sante (free)` 95**（262K）→ `Qwen3.8 27B (free)` 93 → `DeepSeek V4 Flash 0731 (free)` 93。
- 其后：Ollama Cloud `deepseek-v4-pro` 93（1M）· `deepseek-v4-flash` 91 · NIM `Kimi K3` 91（1M）· NIM `deepseek-v4-flash-0731` 90 · LLM7.io `GLM-5.3-Flash` 90。
- ⚠️ **第 5 名那条其实已在 OpenRouter 下架**——聚合站与官方目录之间有滞后，**本页头条②已核**。用它做选型时，务必回官方接口确认在架状态。

---

## 📅 到期日历 · 别踩空

**眼前这一周**

- **9/20（今天）** — 智谱「Flash × ZCode」夜间免费（23:00–09:00）**最后一天**；智谱 AutoClaw 新用户注册送 1 亿的窗口；**千问办公 × 杭州 Token 卡今天起发**
- **9/23** — **讯飞星火 X2.5 限免结束**（00:00）；**WorkBuddy / CodeBuddy 的 DeepSeek V4.1 Flash 0.03× 折扣结束**
- **9/24** — **文心快码 Comate** 测试版限免结束；**字节 TraeCode Seed 系列 1 折**结束

**9 月下旬及以后**

- **9/30** — **阿里 Qoder Qwen3.8-Flash 免费用结束**；**腾讯 Hy3 / 文心 4.0 免费期结束**；WorkBuddy 教师积分；Merge Gateway GLM-5.3-Flash 1 折结束；**腾讯老混元平台停服**
- **10/10** — **腾讯混元 Hy4 preview**（老用户夜间免费）结束；**unbiased.ai `Pareto` 正式发布日**
- **10/14** — **珠海算力券申报截止**（企业向，每年最高 200 万）
- **10/31** — WorkBuddy 学生积分截止
- **11/7** — **MiniMax 开放平台 M3 / M2 免费试用延长**到期
- **12/31** — 腾讯云 TokenHub / 华为云码道「码力续航计划」/ 移动云 MoMA 截止

---

## 🧭 今天该怎么动

**① 现在就做（5 分钟内）**

清一下你的配置：把 `deepseek/deepseek-v4-flash-0731:free` 从代码里删掉——**它已下架，留着只会 404**；Zen 侧的 `union-alpha` 也一并清掉。1M 上下文的需求换成 `nemotron-3-ultra-550b-a55b:free`（1M）或 `thinkingmachines/inkling:free`（1M 全模态）。**顺手把「单点依赖」改掉**：任何写死单条 `$0` 通道的地方，今天加一条 fallback（NIM 或 InternLM）。

**② 今天之内**

- **夜免最后一天**：智谱 ZCode 在 **23:00–09:00** 内把今天剩下的重活跑完（GLM-5.3-Flash 额度消耗为 0）。
- **杭州的团队**：去园区问一句 **Token 卡（≈500 元/张）**的发放口径——今天就开始了。
- **想试新物种**：把 Zen 的 `jev-1.13-free` 接进来，拿一个「本来就是五选一」的小任务（工单分类、日志分诊、危险命令拦截）跑一遍，感受一下 70–500ms 的决策延迟。

**③ 本周之内**

1. **做一次「决策拆解」自检**：把 Agent 里**分类 / 路由 / 打分 / 门禁**的调用从大模型拆出来，换成决策模型（Jev 或自训 Nimble 式 9B LoRA）——**成本能降 2–3 个数量级**，这是本周最值得做的一次架构优化。
2. **音视频任务试 `Qwen3.8-Omni-Flash`**：$0.15 / $0.47，不到 Gemini 3.8 Flash 的两成，先用 Qwen Studio 免费档验证效果。
3. **配好兜底线**：**NVIDIA NIM**（40 RPM 不限量，也是 K3 唯一的免费入口）+ **书生 InternLM**（1.8 亿 tokens/月、无到期日、免信用卡）——两条都注册一次，以后每天的新免费额度都当增量，而不是主粮。
4. **本地零成本**可关注：**Atria Dawn**（744B / 256K / MIT，需大集群）与开源的 **9Router** 多 Provider 组合。

---

> ⚠️ 免费额度可能随时调整，请以各平台官网最新政策为准。本页所有「免费」判定均以官方接口或官方定价页为准。OpenRouter 免费池日内会波动，24 款 / 21 款是脚本清点时刻的快照，不代表全天稳定值。**第三方聚合榜与官方目录存在滞后，本页已标注一处今日实证。**「开源」指权重公开，不代表可自由商用，商用前请逐条核对许可证。**Contributor / 训练条款类免费档：不要把机密代码、个人信息或生产客户数据放进去。**
>
> 📅 生成时间：2026-09-20 · 本页由自动化任务每日生成 · [在线版 HTML](daily-free-llm-2026-09-20.html)
