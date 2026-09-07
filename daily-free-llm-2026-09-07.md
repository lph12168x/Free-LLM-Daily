# 免费大模型日报 · 2026-09-07（周一）

> 聚焦「量大能用的先进模型」· 覆盖 38+ 国内外平台 · [在线阅读 HTML 版](./daily-free-llm-2026-09-07.html)

## 📌 本期焦点

1. **🆕 头号新闻：科大讯飞今日正式发布星火 X2.5（293B）基座模型** —— 9 月 7 日，科大讯飞发布 **星火 X2.5（293B）**，升级重点在**代码生成与智能体能力**，官方定位为「基于全国产算力的全新主力通用大模型」，落地时间比此前流传的 1024 开发者节更早。对免费党真正有意义的是配套动作：**9 月 1 日已开源的 X2.5-4B 与 X2.5-1.7B 端侧模型**，是业界首个原生支持最长 **100 万 token 上下文**的端侧模型，权重 / 代码 / 文档同步上线 Hugging Face 与魔搭，**免费、免授权、可商用**，兼容 llama.cpp / vLLM / SGLang，可用 Ollama、LM Studio 一键部署，对应 API 已在**讯飞星辰 MaaS 平台限时免费**开放。⚠️ 注意：4B/1.7B 是端侧、293B 是云端基座，293B 的免费额度官方尚未公布。

2. **🆕 蚂蚁 Ling 3.0 Flash Sante 医疗版上架 OpenRouter 免费区** —— `inclusionai/ling-3.0-flash-sante:free` 于 9 月 4 日进入 OpenRouter 目录，**输入与输出均标价 $0**。基于 Ling 3.0 Flash 微调的稀疏 MoE：**总参数 124B、激活仅 5.1B**，上下文 262,144、最大输出 32,768，`tools` / `tool_choice` / `reasoning` / `logprobs` / `seed` 参数齐全，可直接挂函数调用做 Agent。榜单：**DiagnosisArena-MCQ（临床诊断）第一**，MedXpertQA-Text 仅次于 GPT-5.6 Sol 与 Gemini 3.6 Flash，HealthBench Professional 仅次于 GLM-5.3-Flash，MedEthicAlign 82.06 分。这是 Ling 3.0 Flash 系列**两天内第二个垂直版本**（9/3 金融版 Fin、9/4 医疗版 Sante），同一套 124B/5.1B 底座、同样免费定价。**⚠️ 唯一硬伤：不支持图片输入**，病历 / 报告扫描件需另配视觉模型预处理。

3. **⏰ MiniMax × GMI Cloud 免费窗口 9/6 到期 —— 已确认下线** —— 8/24–9/6 的 14 天不限量窗口（M3、M2.7、Speech 2.8、Music 3.0）已于 **9 月 6 日结束**，官方 deals 页与 GMI Cloud 活动页双方确认 9/6 起模型下线，需切回付费版。这条路既不承诺零数据留存、也没有不训练保证，**强制 ZDR 的会话本来就用不了**。替代路径仍在：OpenRouter 免费池中 `minimax/minimax-m3:free` 与 `minimax/minimax-m2.7:free` 依然在列（1M 上下文，免费档约 200 req/day），Ollama Cloud 的 minimax-m3 也还在线（freellm.net 评分 86）。

4. **✅ B.AI 日吞吐 1.33 万亿 Token，4 款仍 100% 免费** —— 平台披露：用户破 **230 万**，15 天累计 **8.19 万亿 token**，新增 **22 万 API 用户**，单日吞吐一度破 1.33 万亿。收缩后仍 100% 免费的四款：**GLM-5.3-Flash（Ox Alpha）、Qwen3.8-Flash、腾讯 Hy3、小米 MiMo-V2.5**；DeepSeek V4 Flash 双模型转折扣（工作日高峰 5 折、闲时 2.5 折）。免费档能撑到这个体量才开始收口，本身说明这波窗口期是真的在一点点关上。

5. **🔎 数据核对：OpenRouter 免费池 21 款（换血）** —— 9/7 脚本清点 **430 款**模型中 **21 款** `prompt` 与 `completion` 同时为 0。与 9/4 存档快照比对：**换入** `inclusionai/ling-3.0-flash-sante:free`，**换出** `z-ai/glm-5.2:free`，总数持平。懒人首选 `openrouter/free` 路由器，自动挑当前可用免费模型并按需过滤视觉 / 工具调用 / 结构化输出。

6. **🔎 数据核对：OpenCode Zen 目录 66→70 款，免费 ID 8→7** —— 新增 `gpt-6-astra`、`muse-spark-1.3`、`deepseek-v4-flash-vision-exp`、`glm-5.3`、`glm-5.3-flash`；**`laguna-s-2.1-free` 已下架**，7 个 `-free` ID + `big-pickle` = 8 款 $0。官方定价页 Free 行仍为 6 款（Big Pickle、MiMo-V2.5、Ling 3.0 Flash Fin、Nemotron 3 Ultra、Nemotron 3.5 Lightning、Muse Spark 1.3 Contributor）。config 中格式为 `opencode/<model-id>`。

7. **📉 免费额度的规律已经很清楚了：额度变大、窗口变短、频率变高** —— 智谱三轮 Weekend Build 是最好的样本：第一轮 1 亿 token / 仅新用户 / 61 小时窗口，第三轮（9/5 09:00–9/6 23:00）3 亿 token / 全体用户 / **仅 38 小时**，缩水 23 小时；ZCode 闪送更夸张，9/1 晚发 1 亿、9/2 上午 10 点清零。**结论：看到能领的当天就点掉，收藏起来「有空再看」基本都会过期。** 这波设计的就是让你无法囤。

8. **🌍 生态观察：CNBC 命名「model fatigue（模型疲劳）」** —— 9/1–9/3 的 72 小时内 Anthropic（Fable 5.1 / Mythos 5.1）、Meta（Muse Spark 1.3）、Google（Gemini 3.8 Flash）、OpenAI（GPT-6 Astra）集体发版。Runpod CEO 称这个节奏让 IT 团队「迷失方向」、被迫不断重新基准测试。对免费党反而是好事——**每次旗舰迭代，上一代都会加速下放到免费档**。

---

## 🏆 量大能用的先进模型 · Top 12

| # | 模型 | 平台 / 免费入口 | 关键规格 | 综合分 |
|---|------|----------------|---------|--------|
| 1 | **GLM-5.3-Flash（Ox Alpha）** | B.AI（100% 免费）/ 智谱 ZCode（夜间）/ 华为码道 / 商汤 Token Plan | 320B-A18B · 原生全模态 · 1M 上下文 · MIT 开源 | 96 |
| 2 | **DeepSeek-V4-Flash** | NVIDIA NIM（40 RPM）/ 商汤 Token Plan / AMD Radeon Cloud | 284B-A13B · 1M 上下文 · 开源权重 | 93 |
| 3 | **Kimi K3** | NVIDIA NIM（免费）/ 阿里云百炼 / OpenCode Go | 2.8T-A104B · 1M 上下文 · 视觉 + 推理 | 91 |
| 4 | **Gemini 3.8 Flash** | Google AI Studio（永久免费） | 1M 上下文 · 全模态 · 15 RPM / 1,500 RPD | 89 |
| 5 | **Ling 3.0 Flash Sante（医疗）** | 🆕 OpenRouter `:free` / Kilo / Vercel Gateway | 124B-A5.1B · 262K · 工具调用 · **不支持图片** | 88 |
| 6 | **MiniMax M3** | OpenRouter `:free` / Ollama Cloud / NIM（GMI 已下线） | 1M 上下文 · 文本 / 图像 / 视频 | 87 |
| 7 | **Qwen3.8-Flash** | B.AI（100% 免费）/ 阿里云百炼 / OpenCode Zen | 125B-A6B · 开源 · 量化后单卡可装 | 86 |
| 8 | **腾讯 Hy3** | B.AI（100% 免费）/ WorkBuddy（限免至 9/30） | Agent 优化 · 国内直连 | 85 |
| 9 | **星火 X2.5-4B / 1.7B** | 🆕 讯飞星辰 MaaS（限时免费）/ HF / 魔搭 / Ollama | 原生 1M 上下文 · 免费商用 · 免授权 | 84 |
| 10 | **Nemotron 3 Ultra（550B）** | OpenRouter `:free` / OpenCode Zen / NVIDIA NIM | 550B-A55B · 1M 上下文 · 周用量 2.3T | 83 |
| 11 | **MiMo-V2.5（小米）** | B.AI（100% 免费）/ OpenCode Zen `mimo-v2.5-free` | 代码 / 推理 · 国内直连 | 82 |
| 12 | **Muse Spark 1.3（Meta）** | OpenCode Zen / Go / Command Code | 工具调用 -20% · token -25% · 长周期工作流 | 80 |

---

## 🔌 API 提供商免费额度总览（9/7 核对）

| 平台 | 免费额度 | 要点 |
|------|---------|------|
| 🆕 **讯飞星辰 MaaS** | 限时免费 · 端侧模型免费商用 | X2.5-4B / 1.7B 原生 1M 上下文、权重全开、免费商用；293B 基座额度待公布 |
| ✅ **B.AI** | 4 款 100% 免费 | 日吞吐 1.33 万亿、用户 230 万；GLM-5.3-Flash / Qwen3.8-Flash / Hy3 / MiMo-V2.5 |
| 🔎 **OpenRouter** | 21 款 `:free` · 约 200 req/day | 换入 Sante、换出 GLM-5.2；`openrouter/free` 自动路由 |
| 🔎 **OpenCode Zen** | 8 款 $0（70 款中） | 新增 gpt-6-astra 等 5 款；`laguna-s-2.1-free` 下架 |
| 🆓 **NVIDIA NIM** | 40 RPM · 82 款 | Kimi K3（评分 88）、DeepSeek-V4-Flash（87）；速度是硬伤 |
| 🆓 **Google AI Studio** | 1,500 RPD · 17 款 · 永久免费 | 无信用卡，最可靠的兜底链路 |
| 🇨🇳 **智谱 BigModel / ZCode** | 夜间畅用至 9/20 | 每晚 23:00–09:00 ZCode 内额度归零；GLM-4.7-Flash 永久免费 |
| 🇨🇳 **华为云码道** | 每日 1000 万 tokens | VS Code 插件直装，国内直连；几轮对话就没了 |
| 🇨🇳 **商汤 Token Plan** | 每 5 小时 1500 次 ×2 + 150 次 | 不绑卡不充值，OpenAI 兼容，最多 20 个 Key |
| 🇨🇳 **阿里云百炼 / 权益中心** | 每模型 100 万 tokens | 9/3 整合，覆盖 Qwen3.8-Max / DeepSeek / GLM-5.2 / Kimi-K3 |
| 🇨🇳 **火山方舟（高校师生）** | 每人最高 1 亿 Tokens | 需学信网 / 教师资格认证 |
| 🌐 **Pollinations** | 免 API Key · 无限量 | GPT-4o / Gemini 2.0 Flash / Mistral；无 SLA |
| 🌐 **Cloudflare Workers AI** | 每日 1 万 Neurons | 50+ 开源模型，按 Neurons 计费 |
| 🌐 **Groq / Cerebras** | 1,000 RPD / 100 万 tokens 每天 | 速度双雄；Groq 有 TPM 8000 墙 |
| 🌐 **AgentRouter / Freebuff** | 约 $100 额度 / 每日 5–6 session | 前者无公开 SLA，后者用广告补贴、prompts 可能被用 |

---

## ⏰ 到期红线（按时间排序）

| 日期 | 对象 | 内容 |
|------|------|------|
| **9/9 24:00** | GLM-5.3-Flash 半价 | 剩 2 天：0.4 / 1.4 元每百万 → 9/10 恢复 0.8 / 2.8 元 |
| **9/9–9/10** | 中国联通 1000 亿词元 | 上海世博中心**现场**派送，先到先得，**无线上通道** |
| **9/10 23:59** | 腾讯 Hy4 Preview 限免 | WorkBuddy / CodeBuddy 内免费结束；Hy3 已延期至 9/30 |
| 9/14 | Claude Code 周限额 | 官方确认下调 17% 生效 |
| 9/20 | 智谱夜间畅用 | 「Flash × ZCode」每晚 23:00–09:00 全免费窗口结束 |
| 9/24 | 百度 Comate 限免第二弹 | 测试版 9 款模型不限 token |
| 9/30 | 文小言 / 腾讯 Hy3 | 文心 4.0 全系列免费；Hy3 在 WorkBuddy 内免费 |
| ~~9/6~~ | MiniMax × GMI Cloud | **已结束**：M3 / M2.7 / Speech 2.8 / Music 3.0 下线 |

---

## ⚠️ 风险提醒

- **免费额度规律：额度变大、窗口变短、频率变高** —— 智谱三轮 Weekend Build 从 61 小时缩到 38 小时，ZCode 闪送 12 小时清零。看到能领的当天就点掉，别想着囤。
- **Ling Sante 是「免费 + 专业」，但有致命缺口** —— DiagnosisArena-MCQ 第一很亮眼，但它完全不支持图片输入；真实医疗场景里病历、检验报告、影像基本都是图片。找视觉模型预处理会吃掉它 124B-A5.1B 的成本优势。
- **免费不等于零风险，四类数据条款要分清** —— ① NVIDIA 免费端点注明「仅限试用，勿提交个人或机密数据」；② Muse Spark Contributor 版以免费换取「用你的 prompts 与 completions 训练未来 Meta 模型」的授权；③ Freebuff 用广告补贴，prompts 可能用于广告个性化；④ MiniMax × GMI 那路不承诺 ZDR 也不承诺不训练（已下线）。涉及商业代码或敏感数据，只走有明确隐私条款的通道。
- **免费端点速度差一个数量级，别拿它跑交互链路** —— NIM 上 DeepSeek V4 Flash 仅 27.3 tok/s、Gemma 4 31B 50.9、Kimi K3 62.4，而 Groq 约 500；AMD 首字约 22 秒、输出 28–30 tok/s、并发 8。免费端点适合批处理、写稿、跑批测试。
- **别信「兑换码」** —— 腾讯、阿里、百度、字节、智谱、月之暗面、MiniMax 从未发过通用 CDKey / 官方兑换码。网上「AI 新人激活码」「内部福利码」基本是引流甚至钓鱼。

---

## 🧩 按场景选路

- **日常编码 / 主力链路**：首选 B.AI 的 GLM-5.3-Flash（Ox Alpha）——100% 免费且已被 1.33 万亿日吞吐验证；夜间 23:00–09:00 切智谱 ZCode，额度消耗归零（至 9/20）；备选 Qwen3.8-Flash（可本地部署）。
- **长上下文 / 研究型**：1M 上下文免费档三个选择——Kimi K3（NIM 评分 88）、Nemotron 3 Ultra 550B（OpenRouter / Zen 双通道 $0）、MiniMax M3（OpenRouter `:free`）；要永久稳定走 Google AI Studio；端侧用讯飞 X2.5-4B（数据不出本地）。
- **垂直领域**：医疗走 Ling 3.0 Flash Sante、金融走 Ling 3.0 Flash Fin，均 262K + 工具调用，但**都不支持图片**；OCR 与图表理解用商汤 `sensenova-6.7-flash-lite`（每 5 小时 1500 次）。
- **Agent / 长程任务**：首选 Muse Spark 1.3 Contributor（Zen $0，工具调用 -20%、token -25%，注意数据授权条款）；高频轻活交给本地 X2.5-1.7B 或 MiniCPM5-1B。
- **国内直连 / 免代理**：华为云码道每日 1000 万 tokens → 商汤 Token Plan 每 5 小时刷新 → 智谱 GLM-4.7-Flash 永久免费 → 阿里云百炼每模型 100 万 tokens；高校师生务必申请火山方舟 1 亿 tokens。
- **零配置 / 临时起意**：Pollinations（免 Key，URL 直拼）或 OpenRouter `openrouter/free` 自动路由。

---

## 📊 本轮数据核对方法

- **OpenRouter** `/api/v1/models` 脚本清点（430 款模型，21 款 `prompt` 与 `completion` 同时为 0；与 9/4 存档快照比对，换入 `ling-3.0-flash-sante:free`、换出 `z-ai/glm-5.2:free`）
- **OpenCode Zen** `/zen/v1/models` 接口实拉 70 款（9/4 为 66 款），识别 7 个 `-free` ID，与 `opencode.ai/docs/zen` 官方定价页 Free 行（6 款 + big-pickle）与 Privacy 段逐条比对
- **讯飞官方公告**（X2.5 293B 发布时间、X2.5-4B / 1.7B 开源条款，经 Odaily、格隆汇、腾讯新闻、DEV 日报交叉验证）
- **OpenRouter 模型页**（Ling 3.0 Flash Sante 参数、上下文、上架时间）与第三方实测基准
- **智谱官方公告**（Flash × ZCode 夜间畅用、Weekend Build 第三轮，经今日头条、新浪财经、什么值得买交叉验证）
- **B.AI 官方数据**（1.33 万亿日吞吐、230 万用户、4 款保留免费，经 Fintech Fetch、深潮 TechFlow 交叉验证）
- **freellm.net** 9/5–9/6 核验榜单（454+ 模型 / 31 家提供商 / 234 款实接口验证）
- **阿里云开发者社区**（权益中心整合，9/3 官方文章）
- **什么值得买** 国内一线实测与额度横评 · **AGI Hunt / CNBC / DEV** 海外一线动态

---

**数据来源**：OpenRouter `/api/v1/models`（9/7 脚本清点，430 款中 21 款 $0）· OpenCode Zen `/zen/v1/models`（70 款，7 个 `-free` ID）与官方定价页 / Privacy 段 · 科大讯飞官方公告（X2.5 293B 发布、X2.5-4B / 1.7B 开源）· OpenRouter Ling 3.0 Flash Sante 模型页与第三方基准实测 · 智谱官方公告 · B.AI 官方数据 · 商汤日日新平台文档 · 阿里云开发者社区 · freellm.net 9/5–9/6 核验榜单 · 什么值得买 · AGI Hunt · CNBC · DEV Community · FreeLLMAPI 开源仓库。

⚠️ 免费额度可能随时间调整，请以各平台官网最新政策为准。本页所有「免费」判定均以官方接口或官方定价页为准。讯飞 X2.5（293B）的免费额度尚未公布，本文不作承诺。

⭐ [lph12168x/Free-LLM-Daily](https://github.com/lph12168x/Free-LLM-Daily) · 🤖 由 WorkBuddy 自动化生成
