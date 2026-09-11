# 免费大模型日报 · 2026-09-11（周五）

> 🤖 AI 每日免费情报 · 全网挖掘 · [HTML 版](daily-free-llm-2026-09-11.html) | [返回目录](index.html)

**今日速览**：V4.1 Flash 权重开源上 HF（MIT），HuggingChat 已免费可聊 · Nebius 免费 AI Builder Program 上线（$400+ 额度）· B.AI 的 GLM-5.3-Flash 免费 9/12 09:59 SGT 截止 · OpenRouter 免费池 18→19

---

## 🔥 今日头条

### 1. 🆕 DeepSeek V4.1 Flash 权重开源落地，HuggingChat 已免费可聊：MIT 协议，零部署白嫖旗舰

昨天（9/10）刚发的 V4.1 Flash，今天权重已挂上 Hugging Face（**MIT 许可**），并直接进 HuggingChat——**有 HF 账号就能免费用，不用本地部署、不用 API Key**。

- **架构**：全新 Causal Encoder-Decoder（20 层因果编码器 + 20 层解码器），**552B 主干 + 196B Engram 条件记忆**，384 路由专家 + 1 共享专家、每 token 激活 6 个；**prefill 仅激活 8B、decode 激活 16B**；原生多模态视觉理解，**1M 上下文**。
- **杀招**：FP4 KV cache + CSA2，**全局 KV cache 每 token 仅 890 字节**（约 V4-Flash 的 1/4、初代 V1 的 **1/437**），HBM / SSD 需求降至上一代 **1/4 和 1/8**；完整 1M 上下文缓存不到 1GB。
- **跑分**：GPQA Diamond **90.9**、Codeforces Rating **3471**、Terminal-Bench 2.1 **90.6**、DeepSWE v1.1 **74.2**；官方称性能 / 费用 / 速度 / 总用时**全面超越 V4 Pro**。
- **零成本路径**：① HuggingChat 网页直聊（本期新增）；② OpenCode Zen `deepseek-v4-flash-free`（20 RPM / 200 RPD）；③ NVIDIA NIM `deepseek-ai/deepseek-v4-flash-0731`（免费 / 1.3M / 40 RPM）；④ Ollama Cloud 免费档；⑤ chat.deepseek.com 网页端免费无公开上限；⑥ MIT 权重自部署。
- **生态**：硅基流动 Day 0 上线；WorkBuddy / CodeBuddy / OpenCode 官方合作伙伴全量接入（WorkBuddy 赠两周试用）；同时开源 `deepseek-recipe`、`DeepSelect`（TopK 内核快 **2–20 倍**）、`DeepJIT` 三个部署仓库。

⚠️ 两条硬时间点：**9/14 12:00（北京时间）起所有 `deepseek-v4-pro` 请求强制路由到 V4.1 Flash 按 Flash 价计费**；新价虽降（闲时缓存命中 0.02 / 未命中 1.0 / 输出 4.0 元），但**输出价仍是 8 月涨价前的两倍**，属部分回调。

### 2. 💰 Nebius 免费 AI Builder Program 上线：$400+ 额度横跨六层开源栈

Nebius（阿姆斯特丹 AI 云）9/10 推出**完全免费**的常设社区计划——不是新用户试用金，而是面向开发者的长期计划，**把一整条开源 AI 技术栈的额度打包给你**。

- **权益**：**$400+ 额度与折扣**（Nebius Token Factory 推理 / LangChain / Toloka 标注 / Tavily 搜索等）；cookbook 可运行代码；**Nebius Academy + NVIDIA 免费课程**；**$1 成员价认证**；工程师 office hours 与社区。
- **生态**：开源模型 **NVIDIA Nemotron / Qwen / MiniMax**；编码 Agent **Cognition / OpenHands**；框架 LangChain；搜索 Tavily；基建 Composio；数据 / 评测 / 可观测 **Toloka / LangSmith**；后训练 **Prime Intellect / HF OpenEnv**。
- **区别**：OpenRouter / Zen / NIM 给的是「按请求限速的模型额度」，Nebius 给的是**云额度**——可跑训练、微调、自部署端点。

⚠️ 官方只写「$400+ credits and discounts」，**未逐家披露分配与有效期**；MiniMax 虽列名参与但双方未披露商业合同，不要假设其模型直接出现在托管推理目录。

### 3. 🆓 Cognition 发布 SWE-2 编程模型：基于 Kimi K3 后训练，订阅用户一个月免费

Devin 母公司 Cognition 9/10 发布自研编程模型 **SWE-2**，**Pro / Max / Teams 订阅用户未来一个月内免费**（Devin Desktop / CLI 已上线，Web / Fusion 灰度中）。

- **能力**：底子是**月之暗面 2.8T 参数的 Kimi K3**；FrontierCode 1.1 Main 得分 **50.0%**，与 Fable 5.1 差距 1 分内、**成本低 64%**；首次把 RL 扩展到**多万亿参数规模**，单次运行训出 medium / high / max 全部推理力度档位。
- **背景**：同日被曝完成 **20 亿美元 E 轮、估值 480 亿美元**（四个月前 260 亿）；「免费模型做基建、付费 Agent 做交付」的分层正在成型。
- **顺带**：Cognition 研究员用 Devin 完成 **RSA-260（862 bit）因式分解**（约 4900 GPU 天、40 万美元），打破保持六年半的公开纪录。

⚠️ 「一个月免费」是**订阅内的加赠**；没有订阅的话走 Kimi K3 免费通道（NVIDIA NIM / HF Router / 商汤 Token Plan）更实际。

---

## 🌤️ 次要更新

- **📈 OpenRouter 周榜（截至 9/10）**：Hy4 preview **19.1T 霸榜 +74%**、GPT-5.6 Luna 14.2T、DeepSeek V4 Flash 0731 12.4T、GLM 5.3 Flash 12.3T、MiMo-V2.5 5.15T、DeepSeek V4 Flash 0423 4.76T、**Nemotron 3 Ultra（free）3.63T（前十唯一免费模型）**、Hy3 3.34T、GLM 5.3 3.06T、**Gemini 3.8 Flash 2.6T（+691%）空降第 10**。信号：① Hy4 限免结束后用量反冲 19.1T（限免期用户集中消耗），转夜间窗口后大概率回落；② MiniMax M3（free）已跌出前十。
- **🔎 平台快照**：OpenRouter 437 款中 **19 款 `:free`（净 +1，零下架）**——新增 **`inclusionai/ling-3.0-flash-vl:free`**（262K，原生多模态）；1M 上下文免费 4 款（nemotron-3-ultra、nemotron-3.5-lightning、inkling、inkling-small）。Zen 70 款 / **7 个 `-free` ID 零增减**，GPT-5.6 Sol 5 折至 9/18。freellm.net **469+ 模型 / 31 平台 / 314 免信用卡**（小幅回落属波动），核验榜榜首 Ollama Cloud deepseek-v4-pro（94 分）。
- **🎁 「近乎无限」编码额度盘点**（社区热帖）：**Muse Spark 1.3 Contributor 在 OpenCode Zen 免费**；**GLM-5.3-Flash 在 Chutes 每日 17:00 起连续 10 小时不限量**（限付费套餐）；**Codex 每日 3 次重置**（可直接建 GitHub PR）；**Hy3 多平台免费**。建议按「Zen 免费档 + 一个平台夜间窗口 + 一个每日重置」三路叠加。
- **🆕 Cohere 开源 North Small Translate**：250 亿激活 / 2180 亿总参 MoE，50 语种，WMT 均分 **83.6 超 DeepL 与 Google Translate**，提供 BF16 / FP8 / NVFP4 量化。⚠️ **CC BY-NC 4.0 非商业许可**。
- **🎨 其他限免**：Arena **限时免费开放 GPT-Image-2.5 Sunburst**；Google Labs **Dreambeans 向全美免费开放**；ICLR 2027 **Gemini Paper Assistant 9/11–9/18** 免费向投稿人开放；字节 **TraeCode Seed 系列限时一折**。
- **🇨🇳 杭州 × 智谱「全城 Coding 计划」**（9/10 起）：个人季卡 **-44%**、年卡 **-51%**（需社保证明 / 学籍验证，每人限 1 次）；上城区企业年卡 **-55%**（单家上限 100 万元）。需在 BigModel 实名认证申请。
- **⚠️ 合规风险升级**：9/8 美国 NSA / CISA 联合公告（AA26-251A）点名 DeepSeek、月之暗面、阿里、MiniMax、阶跃星辰、智谱六家「工业化蒸馏」；9/10 Anthropic 报告指控累计近 **2 亿次**蒸馏交互（最大一笔归阿里：5–7 月 1.51 亿次 / 约 3500 账号）。有报道称美方要求美企**识别中国用户并静默降级模型**——跨境调用国产免费 API 的关键链路建议加「模型能力回归检测」。

---

## 🎯 今日可用通道清单（量大且先进）

| 平台 / 通道 | 可白嫖的先进模型 | 额度与限制 | 状态 |
|---|---|---|---|
| **HuggingChat** (huggingface.co/chat) | **DeepSeek V4.1 Flash**（552B MoE / 1M / 多模态，MIT） | HF 账号即可，网页直聊零部署零 Key | 🆕 本期新增 |
| **Nebius AI Builder** (nebius.com) | Nemotron / Qwen / MiniMax（Token Factory 托管） | **$400+ 额度与折扣** + 免费课程 + $1 认证 | 🆕 免费社区 |
| **NVIDIA NIM** (build.nvidia.com) | **Kimi K3**（1M）、DeepSeek V4 Flash 0731（1.3M）、V4 Pro、MiniMax M3、GLM-5.2 等 **99 款 $0** | 40 RPM、TPD 不限；需手机号（+86 可收），免信用卡 | ✅ 长期稳定 |
| **Ollama Cloud** (ollama.com) | deepseek-v4-pro（1M，94 分）、v4-flash（1M）、Kimi K3、GLM-5.3 系列 | 1 实例 / 5h 会话 / 7 天周额度 | ✅ 榜首 |
| **B.AI** | **GLM-5.3-Flash**（320B-A18B / 1M）、Qwen3.8 Flash、Hy3、MiMo V2.5 | GLM-5.3-Flash 免费至 **9/12 09:59 SGT（明天）**；其余 3 款 100% 免费 | ⛔ 明天截止 |
| **OpenCode Zen** | 7 个 `-free` ID（DeepSeek V4 Flash、MiMo-V2.5、Ling Fin、Nemotron Ultra / Lightning、**Muse Spark 1.3**）；GPT-5.6 Sol 5 折至 9/18 | 30 RPM / 500 RPD / 100 万 TPD | ✅ 零增减 |
| **OpenRouter :free** | **19 款**（新增 ling-3.0-flash-vl）；1M 免费款 4 个 | 20 RPM / 50 RPD；充 $10 升 1000 RPD | ✅ 19 款 +1 |
| **Google AI Studio** | Gemini 3.8 / 3.7 / 3.6 / 3.5 Flash（1M）、Gemma 4 | 15 RPM、1500 RPD，免信用卡 | ✅ 长期稳定 |
| **商汤 Token Plan** (token.sensenova.cn) | Kimi K3、DeepSeek V4 Pro/Flash、GLM-5.2/5.3、MiniMax M3、Qwen3.8 Max 等 **20 款** | Free 档 ¥0/月：6 万积分 / 5h 滚动 + 60 万/周 | ✅ 国内直连 |
| **WorkBuddy / CodeBuddy** | Hy4 preview、Hy3 | Hy4 老用户仅 23:00–08:00 免费 / 新用户 10/10 前首开享 14 天；Hy3 至 9/30 | ⚠️ 已收窄 |
| **智谱 ZCode / BigModel** | GLM-5.3-Flash 等 8 款 | ZCode 夜间 23:00–09:00 消耗 0（至 9/20，限付费）；杭州补贴 44–55% | ⚠️ 限时 |
| **ModelScope / HF Router** | DeepSeek V4 系列、Kimi K3/K2.6/K2.7-Code、Qwen3-Coder-Next | ModelScope 100–200 RPD；HF Router $0.10/月额度 | ✅ 稳定 |
| **阿里云百炼** | kimi-k2.7-code、qwen3.5-ocr、glm-5.2 等 | **9/14 / 9/15 到期**；限中国内地节点 | ⛔ 即将到期 |
| **DeepSeek 官方** | V4.1 Flash（1M / MIT） | 付费（闲时 0.02/1/4 元）；网页端免费无公开上限 | ⚠️ 降价但付费 |

---

## 📌 到期与风险日历

- **今天 9/11**：Hy4 preview 限免已结束（昨夜 23:59）→ 老用户仅夜间 / 新用户 10/10 前首开 14 天；V4.1 Flash 权重开源 + HuggingChat 免费开放；ICLR 2027 论文反馈窗口开启（至 9/18）
- **9/12 09:59 SGT**：B.AI **GLM-5.3-Flash** 免费结束（最后一天）
- **9/14 12:00**：DeepSeek **V4 Pro 强制路由**到 V4.1 Flash；百炼 kimi-k2.7-code / qwen3.5-ocr 到期；SkyProduction H3 限免结束
- **9/15**：百炼 glm-5.2 到期
- **9/18**：Zen GPT-5.6 Sol 5 折结束
- **9/20**：智谱 ZCode 夜间畅用结束
- **9/30**：Hy3 免费结束；Merge Gateway GLM-5.3-Flash 1 折结束
- **10/10**：WorkBuddy Hy4 新用户「首开享 14 天」最后首开日

---

## 🧭 今天该怎么动

1. **现在（10 分钟）**：打开 HuggingChat 用 HF 账号试 **DeepSeek V4.1 Flash**，拿自己最长的文档压一遍 1M 上下文。
2. **今天**：走 B.AI 的立刻切备选（明天 09:59 SGT 到期）——Qwen3.8 Flash 同平台免费，或 NVIDIA NIM 的 DeepSeek V4 Flash；确认业务里有没有 `deepseek-v4-pro` 调用（9/14 强制改路由）。
3. **本周**：有落地项目的去领 **Nebius $400+ 额度**；烧掉百炼 9/14、9/15 到期额度；跨境调用国产免费 API 的关键链路加能力回归检测。

---

*数据来源：OpenRouter `/api/v1/models` 与 `/rankings`（9/11 脚本清点，榜单截至 9/10）· OpenCode Zen `/zen/v1/models` 与官方定价页 · Hugging Face / DeepSeek 官方公告与技术报告 · nebius.com 官方博客 · Cognition 官方博客 · Cohere 官方博客 · 智谱 BigModel 文档 · 腾讯新闻 AI 行业日报 / AI 早报 · 观察者网 / 网易 · freellm.net 核验榜 · CISA 公告 AA26-251A 与 Anthropic 威胁情报报告。*

*⚠️ 免费额度可能随时调整，以各平台官网最新政策为准。OpenRouter 免费池日内波动，19 款为脚本清点时刻快照。Nebius 额度为合并口径未逐项披露；SWE-2 免费前提是已有订阅；Chutes 不限量限付费套餐；B.AI 免费为平台补贴承诺；WorkBuddy 限免是客户端额度而非 API 免费，不可用于自动化脚本。*

© [lph12168x/Free-LLM-Daily](https://github.com/lph12168x/Free-LLM-Daily) · 🤖 由 WorkBuddy 自动化生成 · 2026-09-11
