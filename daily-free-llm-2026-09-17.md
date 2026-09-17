# 免费大模型日报 · 2026-09-17（周四）

> 🤖 AI 每日免费情报 · 全网挖掘 · [在线版 HTML](daily-free-llm-2026-09-17.html)

**今日四个关键数字**

| 数字 | 含义 |
| --- | --- |
| **Union Alpha** | 新隐身模型同时空降 **OpenRouter** 与 **OpenCode Zen**，262K 上下文 + 图片输入 + 工具调用，**免费一周** |
| **74%** | Cline 快测 DeepSWE 74%，与 GPT-6 Astra / Opus 5 同档，预期成本约 **1/18**，当前 $0 |
| **24** | OpenRouter 今日零价模型 **24 款**（`:free` 20 款），净增 1、零下架 |
| **6 → 0** | B.AI 免费档 **30 天归零**：最后三款 9/16 17:00 起统一转 1 折 |

---

## 🔥 今日头条 · 三条主线

### ① 免费池｜隐身模型 `Union Alpha` 双平台空降：262K + 图片 + 工具调用，免费一周

9/16 晚间 OpenRouter 上悄悄挂出新模型 `stealth/union-alpha`——没有厂牌、没有模型卡、没有权重，价格栏直接 **$0**；相隔 4 分钟 **OpenCode 同步上线**同一款（Zen 里 ID 是 `union-alpha`，显示名 **Union Alpha Free**）。两家官方口径一致：**免费一周、面向 Agent 编程、不用于模型训练**。

**规格（OpenRouter `/v1/models` 一手）**

| 项目 | 内容 |
| --- | --- |
| 上下文 / 最大输出 | **262,144 / 131,072** |
| 模态 | 输入 **text + image** → 输出 text |
| 支持参数 | `tools` / `tool_choice` / `response_format`（无 JSON-schema 强制） |
| 是否审核 | `is_moderated = false` |
| 价格 | OpenRouter **prompt 0 / completion 0**；Zen 定价页 **四列全 Free**（输入 / 输出 / **缓存读** / **缓存写**），走 `/zen/v1/messages`（Anthropic 协议） |

**跑分与成本**

- Cline 快测 **DeepSWE 74%**：GPT-6 Astra 74%（≈$6.50）、Opus 5 74%（≈$11.80）、**Union Alpha 73–74%（预期成本约 $0.65，现在免费）**、GLM-5.3 69%（$4.00）、DeepSeek V4 Pro 63%（$1.65）。
- 官方称在 **Terminal-Bench 2.1 与 SWE-Bench Verified 超过 GPT-5.6 Sol**；Artificial Analysis Terminal-Bench v4.0 约 **55%**、预期定价约 **$1/任务**，而 GPT-6 Astra (high) 约 58% / **$4/任务**、Claude Fable 5.1 高配约 57% / **$30/任务**。
- Cline 的口径：**接近 GPT-6 Astra 与 Opus 5 的表现，预期成本低约 18 倍**。

**容量与流量**

- **OpenCode 官方：目前容量 5 万亿 tokens/天，后面还可能再涨。**
- OpenRouter **首日约 19.6 亿 tokens**；主要流量来自 `omp`（209 亿）、Hermes Agent、Cline、Claude Code、ZCode——**全是 Agent 类客户端**，说明它主打的确实是编程与 agentic 任务。

**身份仍是谜（三条证据在打架）**

- 有人给它下「只回 OK」的系统指令再发一个字母，模型把内心戏打了出来，写着「**I'm GLM, made by Z.ai**」，还点评说让自己假装匿名算一种欺骗。
- 但独立指纹工具与探针显示，它的文本词表更像 **Llama-3 的 128K 那套**，与 GLM / Qwen / DeepSeek 常用词表都对不上（不过 Hermes、部分 Nemotron 也复用这套公开词表）。
- **官方身份是匿名第三方，别提前写成 GLM-5.4 / 5.5。**
- **历史参照**：上一款 stealth 模型 `stealth/ox-alpha`（8/21 上线进免费池、**8/27 整体下架，只活了 6 天**）事后被证实是智谱 GLM-5.3-Flash。

**三个坑**

1. **ID 不带 `:free` 后缀**——写 `stealth/union-alpha:free` 会直接 404（stealth 系列老坑）。
2. **慢**——P50 延迟 8.7–12.8 秒、吞吐 17–24 tok/s；有用户吐槽发一句「你好」等了两分钟。
3. **会断**——免费流量一冲，长任务常见中途掐断；模型页 24 小时可用率 **95.26%**。

**怎么用**：① 网页 `openrouter.ai/stealth/union-alpha` → Playground 选 `stealth/union-alpha`；② 终端 OpenCode 里 `/models` 选 Union Alpha，或 Cline 模式选 Free；③ 代码走 OpenAI 兼容接口，`model` 填 `stealth/union-alpha`。

**⚠️ 数据条款两家不一样**：OpenCode 另有**零保留**说明；OpenRouter 官方原文是「Prompts and completions **may be retained** by the provider but are **not used for training**」——**「不用于训练」不等于「没人看得到」，更不等于「不会留下」**，而且提供方匿名，出事你连找谁负责都找不到。原则：**当成一台放在公共区域的公用电脑——可以用，但别在上面登录任何东西。**

### ② 平台｜B.AI 免费档 30 天归零：最后三款 9/16 17:00 起统一转 1 折

B.AI「活动与调整公告」页已写明：**现有免费活动于 2026-09-16 17:00（新加坡时间 UTC+8）调整为限时 1 折**；自生效起 `Qwen3.8-Flash` / `Hy3` / `MiMo-V2.5` 在 **API 和 Chat 中**均按标准参考价的 10% 结算。分三批、每次只关一点：

| 时间 | 动作 | 还按 0 元结算的款数 |
| --- | --- | --- |
| 8/31 | 首次收录「6 款国产模型 0 Credits 限时促销」 | 6 |
| 9/03 17:00 | DeepSeek-V4-Flash / V4-Flash-Vision-Exp 转「限时 5 折」（**先关调用量最大的**） | 4 |
| 9/12 10:00 | GLM-5.3-Flash 转「低至标准价 1 折」（**再关能力最强的**） | 3 |
| 9/16 17:00 | Qwen3.8-Flash / Hy3 / MiMo-V2.5 三款一起转 1 折（**最后清场**） | **0** |

**1 折后实际价格**（官方标准价 × 10%，每百万 token，输入 / 缓存读 / 输出）

| 模型 | 输入 | 缓存读 | 输出 | 当前档位 |
| --- | --- | --- | --- | --- |
| Qwen3.8-Flash | $0.016 | $0.0016 | $0.047 | 1 折（9-16 起） |
| Hy3 | $0.0132 | $0.0033 | $0.0528 | 1 折（9-16 起） |
| MiMo-V2.5 | $0.014 | $0.00028 | $0.028 | 1 折（9-16 起） |
| GLM-5.3-Flash | $0.015 | $0.003 | $0.05 | 1 折（9-12 起） |
| DeepSeek-V4.1-Flash（闲时） | $0.015 | $0.0003 | $0.06 | 1 折（9-12 起） |
| GLM-5.2 | $0.84 | $0.168 | $2.64 | 6 折 |
| GLM-5.3 | $1.26 | $0.252 | $3.96 | 9 折 |

**真正的问题不是「贵了」，是性质变了**：从「**额度**」变成了「**余额**」。B.AI 是预付费制，得先充值才拿到 Credits；官方明写**赠送的 Credits 自发放日起 30 天内有效，过期自动失效**。

**⚠️ 三个官方页面口径不一致**（必须记住）

- 「**活动与调整公告**」页 = **唯一权威**（写明转 1 折）；
- 「**定价与用量**」页的价格总表**永远只显示标准参考价**，页顶小字已声明，**不能用来判断还免不免费**；
- 个别模型详情页可能还留着上一轮促销的旧文案；
- **最终凭证只能看你账户里的 Usage 用量页**（逐条给创建时间、模型、token 用量、消耗 Credits）。

顺带一条：价格总表单位已从「Credits per Token」改成「**美元 / 每百万 token**」，页内明示 **1 USD = 1,000,000 Credits**。

**一条可抄走的经验**：聚合平台的免费档，**看它降价的批次间隔就知道还剩多久——批次之间越密，越接近清场**。

### ③ 观察｜免费的两笔账：24 款零价池端点体检，`z-ai/glm-5.2:free` 可摘「不可用」标签

今天第一次把免费池里**全部 24 个零价条目**的端点接口逐个查了一遍：

| 条目 | status | uptime_last_1d | 读法 |
| --- | --- | --- | --- |
| `stealth/union-alpha` | 0 | **99.99%** | 新上线，端点健康（模型页 24h 可用率 95.26%） |
| `dots-studio/dots-3-note-preview:free` | 0 | 100% | 512K 视觉笔记模型，稳 |
| `poolside/laguna-s-2.1:free` | 0 | 99.99% | 262K 代码模型，稳 |
| `thinkingmachines/inkling:free` | 0 | 99.97% | 1M 全模态，稳 |
| `z-ai/glm-5.2:free` | **0** | **98.86%** | **9/16 是 -2 / 81.8%，今天回到 0 / 98.86%（30 分钟口径 97.56%）→ 可摘掉「不可用」标签** |
| `nvidia/nemotron-3.5-lightning:free` | 0 | 98.43% | 1M，稳 |
| `nex-agi/nex-n2.5-mini:free` | -2 | 78.38% | 这档暂时别当主力 |
| `nvidia/nemotron-3-super-120b-a12b:free` | -2 | 97.33% | 瞬时抖动 |
| `nvidia/nemotron-3-ultra-550b-a55b:free` | -5 | 98.27% | 同上，榜上仍是前十唯一免费 |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | -5 | 81.86% | 波动偏大 |

**关键提醒：status 和 uptime 是每天波动的运营量，不是平台政策。** 上面四条负值不代表哪家厂商变卦了，只代表那几分钟那几台机器不健康（有几条 1 天可用率仍在 97% 以上）。**看到负值别当成「变动」转发，它只回答「现在这一秒能不能用」。**

今天两个变动方向正好相反：**B.AI 在收（向你要钱），OpenRouter 在放（向你要数据）**。把它们摆在一起看，说的是同一件事——**免费从来不是一个产品层，而是一笔获客成本；既然是成本，迟早要结账，结账方式只有两种：向你收钱，或者向你要别的东西**。

所以拿到任何一条「免费」，先问三个问题：**免费的实际成本 = 钱（0）+ 数据（你的 prompt 进了谁的口袋）+ 稳定性（随时可能消失）**。三个都便宜，那是真免费；只要有一个贵，就得看那个贵的你付不付得起。

---

## 🌤️ 次要更新 · 值得记一笔

- **🔌 Kimi K3 进入 NVIDIA NIM 目录**：注册后可通过 OpenAI 兼容接口**免费调用**，支持多模态、流式输出与推理强度设置。NIM 的免费档是「**约 40 RPM、调用量不设上限**」——单看「量大」这一条它最不需要算计。注意 NIM **要求手机号验证**，部分端点标注「Trial use only，不要提交个人或机密数据」。榜单侧：freellm.net 上 NIM 的 `z-ai/glm-5.3` **97 分**登顶、`glm-5.3-flash` 96 分、`Kimi K3` 91 分。
- **🆕 Agnes AI `agnes-2.5-flash`：输入输出双 $0**，512K 上下文 / 66K 最大输出，text + image 输入，**带推理与工具调用**，权重不公开；同族 `agnes-2.0-flash` 在 freellm.net 上 88 分、256K / 64K、**30 RPM**。这类「小厂免费双 0」通道的典型风险是**随时改价**——适合进 fallback 链，不适合当唯一主力。
- **💵 TypeSafe AI `Jev`：输出 Token 完全免费**，输入 **$0.042 / 百万 token**。它输出的是**带校准概率的判断**而不是文本。如果你的场景是**大量判断 / 分类 / 打分**而非长文生成，这个成本结构可能比有 RPM 天花板的免费档更划算。属早期产品，先当候选。
- **🔁 Oxlo.ai：按「请求次数」而不是按 Token 计价**。兼容 OpenAI 客户端（`https://api.oxlo.ai/v1`）；**免费档 60 请求/天，覆盖 16+ 模型，并附 7 天全量试用**；付费 Pro 1000 请求/天、Premium 5000 请求/天（带优先队列）。官方卖点很具体：**长上下文灌文档、Agent 工具循环、批量推理这三类场景，按请求算比按 token 算便宜 10–100 倍**，因为 token 计费会对你每一轮追加的上下文反复收费。这类「**计价单位套利**」值得进选型清单，但要先在自己的真实任务上测一轮。
- **🧩 OpenCode 订阅结构变清楚了**：开源 BYO Key **免费** / **Go $10/月** / Workspaces（团队）免费。Go 不是按请求或按天给额度，而是**按「美元用量」给每个模型设限**：**5 小时窗口 = 月额度 20%、周 = 50%、月 = 100%**；截至 9/15，各模型月额度分 **$15 / $30 / $60** 三档，官方提醒「用量上限可能随早期反馈调整」。授权边界也写清了：**ChatGPT Plus/Pro 与 GitHub Copilot 可零配置接入，Claude Pro / Max 不行**（Anthropic 明确禁止，OpenCode 自 1.3.0 起不再内置相关插件）。
- **🇨🇳 智谱：GLM-5.3 × ZCode 每天 1 亿 Token 免费额度，第二批已开（ZCode 限量 5 万份）**。注意：① 这是**真实可调的 API 额度**，不是只能网页聊天；② ZCode 以 CLI 运行，**不依赖本机显卡**；③ 规则与领取门槛**以官方页面为准**，活动限时。并行的「Flash × ZCode」**夜间畅用（23:00–09:00）到 9/20 结束**。
- **🎨 腾讯混元 3D 3.0：建模精度 ×3，面向用户免费开放**。9/16 腾讯全球数字生态大会发布：几何分辨率 **1536³**、支持 **36 亿体素**，首创 3D-DiT 分级雕刻（先搭结构再精修），人物五官告别「抽象脸」；**已集成进混元 3D AI 创作引擎面向用户免费开放**并上线腾讯云 API；专业级 **混元 3D Studio 启动邀请制内测**。混元 3D 系列社区下载量已超 **260 万**。对做视频 / 游戏 / 电商素材的人是**真·零成本**的生产捷径。
- **🎬 MiniMax H3 Max：速度近 2 倍，本周内 5 折**；**33B 全模态版本同步登陆 Together AI**（4–15 秒、最高 2K、原生立体声）。开源社区一周爆发：ComfyUI 团队把 AdaLN 调制权重剪掉换查找表 + int8 量化，**显存从 123.6GB 压到 42.5GB（RTX 3060 就能跑）**；魔搭 DiffSynth-Studio 的 NF4 版把最低显存压到 8GB。

---

## 🧾 今日免费入口速查 · 先进 + 量大优先

| 入口 | 能调到的先进模型 | 额度 / 价格 | 门槛 |
| --- | --- | --- | --- |
| **OpenRouter**（今日 +1） | **新增 `stealth/union-alpha`**（262K、图片输入、工具调用、**免费一周**）；零价池 **24 款**（`:free` 20 款），1M 上下文 4 款 + 音频输出 2 款；含 `nemotron-3-ultra-550b-a55b:free`、`thinkingmachines/inkling:free`（均 1M）、`ling-3.0-flash-vl:free`（视觉+视频）、`nex-n2.5-pro:free`（262K） | **$0**；`:free` 约 **20 RPM / 50 RPD**，累计充值满 $10 后升到 **1000 RPD**；**⚠️ `stealth/union-alpha` 不带 `:free` 后缀** | 注册即可，免信用卡 |
| **OpenCode Zen**（今日 +1） | **新增 `union-alpha`**（Union Alpha Free，走 Anthropic 协议 `/zen/v1/messages`）；另有 `nemotron-3-ultra-free`、`nemotron-3.5-lightning-free`（均 1M）、`mimo-v2.5-free`、`ling-3.0-flash-fin-free`、`muse-spark-1.3-contributor-free`、`big-pickle` | **$0**；定价页 Free 行 **7 款，全部 limited time**；同页 **GPT-5.6 Sol 五折到 9/18**；OpenCode 称 Union Alpha **容量 5 万亿 tokens/天** | 登录拿 Key，客户端内直接选 |
| **NVIDIA NIM**（量大） | **新上 `Kimi K3`**；另有 `z-ai/glm-5.3`（1.3M，97 分）、`glm-5.3-flash`（1.3M / 944K 输出）、`deepseek-ai/deepseek-v4-flash-0731`（1.3M）等 100+ 款 | **$0**；**约 40 RPM 且调用量不设上限**（单看「量大」最优） | 注册 + **手机号验证**；部分端点 Trial only |
| **Agnes AI**（双 $0） | `agnes-2.5-flash`（512K / 66K 输出、text+image、带推理与工具调用）；`agnes-2.0-flash`（256K，88 分） | **输入 $0 / 输出 $0**；`agnes-2.0-flash` 约 **30 RPM** | 注册即可；小厂通道注意改价 |
| **Oxlo.ai**（新玩法） | 16+ 模型，按「**请求次数**」计价，兼容 OpenAI 客户端 | **免费 60 请求/天 + 7 天全量试用**；Pro 1000 请求/天、Premium 5000 请求/天 | 注册；长上下文 / Agent 循环优势最大 |
| **Nous Portal**（Agent 免费） | Hermes Agent（MIT）可白嫖；Portal 免费档只给**免费模型**；付费档打包 **300+ 模型 + Tool Gateway** | **$0**（免费档）→ Plus **$20**（$22 credits）/ Super $100 / Ultra $200 | 注册；Hermes Cloud 需 $2 credit 起 |
| **TypeSafe AI**（输出免费） | `Jev`——输出带校准概率的判断而非文本 | 输入 **$0.042/百万 token**、**输出 Token 完全免费** | 早期产品，先当候选 |
| **国内直供**（额度大） | **火山引擎**豆包 2.1 Pro / DeepSeek 系；**智谱** GLM-4.7-Flash（永久免费 200K）+ GLM-5.3 × ZCode 每天 1 亿；**硅基流动** 100+ 模型；**腾讯 TokenHub** 混元；**书生 Intern AI** | 火山 **200 万 Tokens/天**（零点刷新不累积）；TokenHub 每模型 **100 万 / 1 年**；硅基流动新用户约 **2000 万**；百炼每模型 100 万 | 需实名；**⚠️ 腾讯老混元平台 2026 年 9 月底停服，新项目直接上 TokenHub** |

**一句话选型**：想今天就把「先进模型 + 零成本」同时拿到，走 **OpenCode Zen / OpenRouter 的 Union Alpha**（免费一周，262K + 图片 + 工具调用）；想要**长期不担心额度**，走 **NVIDIA NIM**（40 RPM 不限量，还新上了 Kimi K3）；想省钱省在计价方式上，试 **Oxlo.ai 的按请求**；**敏感代码别进匿名通道，别写进 CI / 生产链路**。

---

## 🔎 平台盘点 · 今日快照

| 平台 | 今日快照 |
| --- | --- |
| **OpenRouter** | 目录 **444 款**，零价 **24 款**（`:free` **20 款**），**净增 1、零下架**（新增 `stealth/union-alpha`）。1M 上下文免费 **6 条**：`nemotron-3-ultra-550b-a55b:free`、`nemotron-3.5-lightning:free`、`thinkingmachines/inkling:free`、`thinkingmachines/inkling-small:free`，以及**输出音频**的 `google/lyria-3-pro-preview` / `lyria-3-clip-preview`。另有易漏的零价入口 `openrouter/free`（200K 自动路由池）。⚠️ 免费池日内会波动，24/20 是脚本清点时刻快照；已留 `or_models_0917.json` 供次日 diff |
| **OpenRouter 周榜**（截至 9/16） | **1** GPT-5.6 Luna **17.3T**（+34%）· **2** Hy4 preview **12T**（+39%）· **3** GLM 5.3 Flash **11.3T**（+9%）· **4** DeepSeek V4 Flash 0731 **11.2T**（+9%）· **5** DeepSeek V4.1 Flash **10.3T**（**new**）· **6** MiMo-V2.5 **7.83T**（**+87%**，涨幅最大）· **7** Hy3 4.47T · **8** DeepSeek V4 Flash 0423 4.24T · **9 `Nemotron 3 Ultra (free)` 3.49T（前十唯一免费）** · **10** GLM 5.3 2.46T。应用榜：**Hermes Agent 1.71T 第一**、Claude Code 959B、Kilo Code 508B、Cline 410B、pi 340B、**omp 281B（新进第 6）**、Codex 225B、OpenClaw 186B、DeepSeek Harness 160B（新）、draco-cascade-bench 136B（新）。AA Intelligence Index 榜首 **Claude Fable 5.1 / Qwen3.8 Max 并列 53.4**，开权重最好的 `GLM-5.3 (max)` 44.9 |
| **OpenCode Zen** | **71 款**（9/16 为 70），**唯一新增 `union-alpha`**，无下架。带免费标记的 ID **8 个** + `union-alpha`；官方**定价页 Free 行是 7 款**——**与 models 端点的免费 ID 名单仍不一致，以定价页为准**。定价页对 Union Alpha 特别注明「**提供方遵循零保留政策、不使用你的数据训练模型**」（big-pickle 只写「收集反馈改进模型」）。⏰ **GPT-5.6 Sol 五折到 2026-09-18（明天到期）** |
| **freellm.net** | 站内计数在 **484+ / 490+** 之间波动，同一口径下 **31 家平台**、约 **228–233 款经 live API 实测**、**396+ 款全程免绑卡**。榜首易主：**NVIDIA NIM `z-ai/glm-5.3` 97 分**（1.3M / 944K 输出 / 40 RPM）→ NIM `glm-5.3-flash` 96（周用量 **904.6M**）→ Ollama Cloud `deepseek-v4-pro` 93（1M）→ Ollama Cloud `deepseek-v4-flash` 92 → NIM `Kimi K3` 91；其后 `deepseek-v4-flash-0731` 90、ModelScope `GLM-5.3-Flash` 90、Agnes AI `agnes-2.0-flash` 88、ModelScope `Qwen3.8-Flash-Next` 87、Google `Gemini 3.8 Flash` 83 |

---

## 📅 到期日历 · 别踩空

**眼前这一周**

- **9/17（今天）** — GPT-6 Astra Challenge 投稿截止（前五名各 1 万美元额度）
- **9/18** — OpenCode Zen **GPT-5.6 Sol 50% 折扣到期**
- **9/20** — 智谱「Flash × ZCode」夜间畅用（23:00–09:00）结束
- **≈9/23** — **Union Alpha 免费窗口**按「一周」口径推算前后结束（官方未写明确日期；上一款 stealth 只活了 6 天）

**9 月下旬及以后**

- **9/30** — 云知声 U2-Flash 1 亿 Tokens 与六折价结束；腾讯 **Hy3 免费期**结束；Merge Gateway GLM-5.3-Flash 1 折结束；阿里云 AI 焕新季满减券截止；**腾讯老混元平台停服**
- **10/10** — WorkBuddy Hy4 preview 新用户「首开享 14 天」的最后首开日
- **10/14** — **Bolt Forge 50× 用量预览期结束**；**OpenAI 从全计划下线 GPT-5.5**（Codex 用户需迁到 GPT-5.6 Sol 或 GPT-6 Astra）
- **12/31** — 腾讯云 TokenHub / 华为云码道「码力续航计划」/ 移动云 MoMA 活动截止

---

## 🧭 今天该怎么动

**① 现在就做（5 分钟内）**

在 **OpenCode 里把模型切到 Union Alpha**，拿一个真实但**非敏感**的仓库跑一次多文件重构——它是这周唯一「先进 + $0 + 262K + 图片 + 工具调用」四件齐备的通道。**记住模型名不要加 `:free` 后缀**（写 `stealth/union-alpha:free` 会 404）。同时把 `z-ai/glm-5.2:free` **从「不可用」黑名单里放出来重测一次**——端点状态已从 -2 回到 0、1 天可用率 98.86%。

**② 今天之内**

**还在用 B.AI 的**：打开账户左侧的 **Usage 用量页**逐条核对——公告页与定价页口径不一致，只有用量页是最终凭证；同时算一下**赠送 Credits 的 30 天有效期**会不会让你白白损失。**想扩量的**：把 **NVIDIA NIM 的 Kimi K3** 加进池子（40 RPM 不限量）；**想省在计价方式上的**：去 **Oxlo.ai** 用 7 天全量试用跑一遍你的长上下文任务，验证「按请求」到底省多少。

**③ 本周之内**

1. **Union Alpha 别写进 CI / 生产链路、别写死模型名**——上一款 stealth 只活了 6 天，退池没有预告期；**涉密与商业敏感的 prompt 不要进匿名通道**（「不用于训练」≠「不会被保留」）。
2. **把「免费实际成本 = 钱 + 数据 + 稳定性」当成选型公式**：B.AI 贵在钱（1 折后仍很便宜），Union Alpha 贵在数据和稳定性（钱是零）——**没有一种免费是错的，错的是拿错了用途**。
3. 顺手把这周三件「额度型」福利登记好：智谱 **GLM-5.3 × ZCode 每天 1 亿 token（第二批限 5 万份）**、**腾讯混元 3D 3.0 免费开放**（做素材的直接省一笔）、**Agnes AI 双 $0** 放进 fallback。

---

**数据来源**：OpenRouter `/api/v1/models`（9/17 脚本清点，444 款中 24 款 $0 / 20 款 `:free`，已留 `or_models_0917.json`）· OpenRouter 模型页与 Rankings（截至 9/16 的周榜与 Apps 榜）· OpenCode Zen `/zen/v1/models`（71 款）与官方定价页（Free 行 7 款 + GPT-5.6 Sol 五折至 9/18）· OpenRouter 官方公告（9/16 stealth/union-alpha 上线、零价、262K、prompts 不用于训练）· OpenCode 官方公告（9/16 免费一周、零保留、容量 5 万亿 tokens/天）· Cline / Artificial Analysis 第三方快测（DeepSWE 74%、Terminal-Bench v4.0 ~55%）· HuggingNews、新浪财经（9/17）、今日头条中文报道与社区指纹分析 · B.AI「活动与调整公告」页与「定价与用量」页（9/16 17:00 转 1 折、1 USD = 1,000,000 Credits）· 《每日免费API资讯 2026-09-17》免费池端点体检 · NVIDIA NIM 模型目录与 freellm.net 核验榜（484–490 / 31 平台 / 228–233 live / 396+ 免绑卡）· Agnes AI 与 allaimodel 定价库（agnes-2.5-flash 双 $0）· Oxlo.ai 官方免费档说明 · TypeSafe AI Jev 定价 · OpenCode 官方订阅与 Workspaces 说明（含 Claude Pro/Max 授权边界）· 智谱 GLM-5.3 × ZCode 活动页 · 腾讯全球数字生态大会混元 3D 3.0 发布（9/16）· MiniMax H3 Max 与 ComfyUI / DiffSynth 开源优化 · AI 日报 2026-09-16（AI HOT 精选）。

⚠️ 免费额度可能随时调整，请以各平台官网最新政策为准。本页所有「免费」判定均以官方接口或官方定价页为准；涉及额度的具体数字请自行调用官方 Usage API 或查看控制台确认。OpenRouter 免费池日内会波动，24 款 / 20 款是脚本清点时刻的快照，不代表全天稳定值。**隐身 / stealth 模型的身份未经官方确认，本页写的「疑似身份」均为社区推测，请勿据此做采购或宣传结论。**「开源」指权重公开，不代表可自由商用，商用前请逐条核对许可证（尤其 Kimi、GLM、MiniMax 的 Model-as-a-Service 条款）。

📅 生成时间：2026-09-17 · 本页由自动化任务每日生成
