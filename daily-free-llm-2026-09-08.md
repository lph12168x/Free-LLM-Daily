# 免费大模型日报 · 2026-09-08（周二）

> 聚焦「量大能用的先进模型」· 覆盖 40+ 国内外平台 · [在线阅读 HTML 版](./daily-free-llm-2026-09-08.html)

## 📌 本期焦点

1. **🆕 头号新闻：Merge Gateway 把 GLM-5.3-Flash 打到 1 折，是 AA 57 分区间全球最低价** —— 新进视野的聚合网关 **Merge Gateway**（`https://api-gateway.merge.dev/v1/ai-sdk`，托管 **180 款**模型）放出限时促销：**GLM-5.3-Flash 直降 90%**，输入 **$0.012 / 1M**、输出 **$0.04 / 1M**、缓存读取 **$0.003 / 1M**，有效期至 **2026 年 9 月 30 日**。这个价格的分量：GLM-5.3-Flash 在 Artificial Analysis 智能指数上拿 **57 分**（对标 Claude Opus 4.8、高于 DeepSeek V4 Pro），Merge 这档是**所有 55 分以上模型里的全球最低价**——比 Z.ai 官方 5 折价（$0.075/$0.25）还便宜 6 倍，比明天恢复原价后（$0.15/$0.50）便宜 12 倍。同网关 180 款里真正标 **$0** 的只有 1 款：`nvidia/nemotron-3.5-lightning-30b-a3b`，**1M 上下文**。⚠️ 注意：这是**折扣不是免费**，要花钱，只是便宜到接近白送；第三方网关的可用性与限流需自行压测。

2. **🆕 OrcaRouter 免费档换将（9/7）：Qwen3.8-27B → GLM-5.3 Flash** —— 聚合网关 **OrcaRouter**（117 款模型、免费档 5 款）于 9 月 7 日把免费档主力从 `qwen/qwen3.8-27b-free` 换成 **`z-ai/glm-5.3-flash`**，老用户**必须改模型名**。规格：320B 总参 / 18B 激活 MoE、45 层、**1,048,576 token 上下文**、MIT 许可、30T token 多模态语料、文本 / 图像 / 视频输入。这笔账：质量分 **4 → 8 分**（OrcaRouter 自测）、上下文 **262K → 1M**、付费定价 **$0.33/$2.40 → $0.075/$0.25**。**代价是速度**：7 天实测首字延迟 **1.96s → 7.66s**（3.9 倍）、生成 **196 → 74.2 tok/s**（2.6 倍）。免费档全量 5 款：`deepseek-v4-flash-free`（1M）、GLM-5.3 Flash、`hy3-free`（256K）、`orcarouter/auto`（128K）、`orcarouter/free`（65K）。⚠️ 额度不公开，从没充过值的账号日额度更小；429 带 `Retry-After` 是分钟 / 日窗口满，不带则是单条 prompt 超长；免费与付费容量隔离，不会静默回落。官方明说这是 best-effort，不能当生产容量。

3. **⚠️ OpenRouter 免费池 18 → 16：MiniMax 双模型免费版下架** —— 脚本清点 `https://openrouter.ai/api/v1/models`：今日 **428 款**模型中 **16 款** `prompt` 与 `completion` 同时为 $0，昨日（9/7）为 18 款。**换出的是 `minimax/minimax-m3:free` 与 `minimax/minimax-m2.7:free`，换入 0 款。** 这次掉的分量不轻：MiniMax M3 免费版在 9/6 快照里**周吞吐 5.02T token、全站第 6 名、66.5M 次请求**，是免费池里跑量最大的几款之一；第 29 名的 M2.7 同时消失。免费池近期轨迹：9/3 十八款 → 9/4 十八款 → 9/7 十八款 → **9/8 十六款**，稳定四天后第一次净减。**MiniMax 免费通道现状**：GMI Cloud 那条 9/6 已到期，OpenRouter 这两条今天也撤了，还剩 **Ollama Cloud**（freellm.net 核验 86 分、1M 上下文）与 **NVIDIA NIM**（84 分、40 RPM、512K 输出）。⚠️ 免费池日内会波动，16 款是脚本清点时刻的快照，不代表全天稳定值。

4. **⏰ 明天 9/9：GLM-5.3-Flash 官方 5 折窗口到期** —— Z.ai 发布期折扣由 **$0.075/$0.25** 恢复 **$0.15/$0.50**。想锁低价的今天动手，或者干脆转 Merge Gateway 的 1 折（更便宜、还多 20 天窗口）。

5. **🔎 数据核对：OpenCode Zen 70 款 / 8 个 `-free` ID，连续两日零增减** —— 免费 ID：`big-pickle`、`deepseek-v4-flash-free`、`mimo-v2.5-free`、`ling-3.0-flash-fin-free`、`nemotron-3-ultra-free`、`nemotron-3.5-lightning-free`、`muse-spark-1.3-contributor-free`、`muse-spark-1.2-contributor-free`。⚠️ 官方定价页 Free 行只列 **6 款**，与 API 差 2 款——这类「API 有、文档没有」的通常是灰度或即将回收的产物，以 API 为准但要打折看。

6. **🏆 freellm.net 今日核验榜：Kimi K3 以 92 分登顶** —— 全站第一，比第二名 Gemini 3.8 Flash（86）高出 6 分。1M 上下文、最大输出 131K、视觉 + 推理，NVIDIA NIM 免费通道 40 RPM。⚠️ 注意 ModelScope 上同名条目评测分只有 65、上下文显示 8K——那是另一条质量差很多的通道，别选错。全站规模：**453+ 模型 / 31 家平台 / 291 款免信用卡**。

7. **✅ B.AI 日吞吐 1.33 万亿 Token，4 款仍 100% 免费** —— 用户破 **230 万**、15 天累计 8.19 万亿 token、新增 22 万 API 用户。仍 100% 免费的四款：**GLM-5.3-Flash（Ox Alpha）、Qwen3.8-Flash、腾讯 Hy3、小米 MiMo-V2.5**。

8. **📉 免费池开始净减，MiniMax 是最响的一记警钟** —— 一周内 MiniMax 的免费通路从「不限量 + 聚合双通道」塌到「只剩云厂商体验额度」。**结论：任何单一免费通道都不该成为生产依赖**，主力模型至少要配两条不同厂商的通道。同时，**免费档换强模型几乎必然伴随降速**——OrcaRouter 是活样本，能力上去的部分一定在别处找回来。

---

## 🗞️ 9/5–9/8 全网挖掘 · 当日动态

| 时间 | 平台 / 来源 | 动态 | 免费性质 |
|------|------------|------|---------|
| 9/8 | **Merge Gateway** | GLM-5.3-Flash 限时 1 折至 9/30：**$0.012 / $0.04 / $0.003**；网关共 180 款，1 款真 $0（Nemotron 3.5 Lightning 30B A3B，1M） | 折扣·近免费 |
| 9/7 | **OrcaRouter** | 免费档主力由 Qwen3.8-27B 换成 **GLM-5.3 Flash**，1M 上下文、MIT 权重；老集成需改模型名 | 真免费 $0 |
| 9/8 | **OpenRouter** | 免费池 **18 → 16** 款，MiniMax M3 / M2.7 `:free` 双双下架，无新增补位 | 缩水 |
| 9/9（明天） | **Z.ai 官方** | GLM-5.3-Flash 发布期 **5 折窗口到期**：$0.075/$0.25 → $0.15/$0.50 | 涨价倒计时 |
| 9/7 | **Hugging Face / OpenBMB** | MiniCPM5-2B 开放权重，AA 智能指数 15 分，**4B 以下开源模型最高分** | 开源权重 |
| 9/8 | **Google** | Gemini Student：**学生可领一年免费**（含 Gemini Live / Omni 视频生成、400GB 存储、更高限额） | 限人群免费 |
| 9/8 | **H Company** | 开源 NeoMME 多模态编码器（260M / 800M），ColPali 式免 OCR 页面检索，260M 版对标 3.75B ColQwen2.5 | 开源权重 |
| 9/7 | **腾讯** | Hy4 preview（770B-A49B、1M 上下文、开源）**OpenRouter 周吞吐 14.7T 升至全站第 1**；编码 / 工作台平台两周免费试用 | 限免 |
| 9/3–9/20 | **智谱 ZCode** | 「Flash × ZCode」每晚 **23:00–09:00** ZCode 内 GLM-5.3-Flash 额度消耗**归零**、其他 Agent 翻倍 | 限时免费 |
| 持续 | **B.AI** | 日吞吐 **1.33 万亿** token、15 天累计 8.19 万亿、用户破 **230 万**；4 款仍 100% 免费 | 真免费 |
| 9/8 | **OpenCode Zen** | 目录 70 款、**8 个 `-free` ID**，与 9/7 完全一致（官价页 Free 行列 6 款） | 零增减 |
| 9/7 | **freellm.net** | 核验榜：**Kimi K3（92 分）登顶**；453+ 模型 / 31 家平台 / 291 款免信用卡 | 榜单 |

---

## 🏆 量大能用的先进模型 · Top 12

| # | 模型 | 平台 / 免费入口 | 关键规格 | 综合分 |
|---|------|----------------|---------|--------|
| 1 | **GLM-5.3-Flash（Ox Alpha）** | 🆕 Merge Gateway（1 折）/ B.AI / 智谱 ZCode（夜间）/ 🆕 OrcaRouter（免费）/ 华为码道 | 320B-A18B · MIT · 1M 上下文 · 全模态 · **5 条免费路径** | 96 |
| 2 | **DeepSeek-V4-Flash** | NVIDIA NIM / 商汤 / AMD Radeon Cloud / 🆕 OrcaRouter（免费）/ Zen / B.AI | 284B-A13B · 1M 上下文 · **六条通道** | 93 |
| 3 | **Kimi K3** | NVIDIA NIM（免费）/ 阿里云百炼 / OpenCode Go | 1M 上下文 · 131K 输出 · 视觉 + 推理 · **今日榜首 92** | 92 |
| 4 | **Nemotron 3.5 Lightning（30B-A3B）** | 🆕 Merge Gateway（**$0**）/ OpenRouter `:free` / Zen | 1M 上下文 · **三通道同时免费** | 89 |
| 5 | **Gemini 3.8 Flash** | Google AI Studio（永久免费） | 1M 上下文 · 全模态 · 15 RPM / 1,500 RPD | 88 |
| 6 | **Nemotron 3 Ultra（550B-A55B）** | OpenRouter `:free` / Zen / NIM / Ollama Cloud | 550B-A55B · 1M 上下文 · 周吞吐 3.64T | 87 |
| 7 | **Qwen3.8-Flash / Qwen3.8-27B** | B.AI（100% 免费）/ ModelScope（88 分）/ 百炼 / Merge（$0.022） | 125B-A6B · Apache 2.0 · 国内直连 | 86 |
| 8 | **MiniMax M3** | ⚠️ OpenRouter 已下架 · Ollama Cloud（86）/ NIM（84） | 1M 上下文 · 文本 / 图像 / 视频 · 512K 输出 | 85 |
| 9 | **腾讯 Hy3 / Hy4 preview** | B.AI（100% 免费）/ 🆕 OrcaRouter `hy3-free` / WorkBuddy（限免至 9/30） | 256K 上下文 · 国内直连 | 84 |
| 10 | **Ling 3.0 Flash Sante / Fin** | OpenRouter `:free`（双款）/ Zen / Kilo Gateway | 124B-A5.1B · 262K · 工具调用 · **不支持图片** | 83 |
| 11 | **MiMo-V2.5（小米）** | B.AI（100% 免费）/ Zen `mimo-v2.5-free` | 代码 / 推理 · 国内直连 | 82 |
| 12 | **Muse Spark 1.3（Meta）** | Zen / Go / Command Code | 工具调用 -20% · token -25% · 1M 上下文 | 80 |

---

## 🔌 API 提供商免费额度总览（9/8 核对）

| 平台 | 免费额度 | 要点 |
|------|---------|------|
| 🆕 **Merge Gateway** | 180 款 · 1 款真 $0 · GLM-5.3-Flash 1 折至 9/30 | 唯一 $0：`nvidia/nemotron-3.5-lightning-30b-a3b`（1M）；GLM-5.3-Flash $0.012/$0.04 |
| 🆕 **OrcaRouter** | 117 款 · 5 款 $0 | 免费与付费同权重；今日换入 GLM-5.3 Flash；额度不公开，429 规则明确 |
| 🔎 **OpenRouter** | **16 款** `:free`（昨 18）· 约 200 req/day | 换出 MiniMax M3 / M2.7，换入 0 款；`openrouter/free` 自动路由 |
| 🔎 **OpenCode Zen** | 8 款 $0（70 款中） | 连续两日零增减；官价页只列 6 款 |
| 🆓 **NVIDIA NIM** | 40 RPM · 1M 上下文 | 榜首 Kimi K3（92）；MiniMax 下架后成其最稳免费门 |
| 🆓 **Google AI Studio** | 1,500 RPD · 17 款 · 永久免费 | 无信用卡；今日新增 Gemini Student 学生一年免费 |
| ✅ **B.AI** | 4 款 100% 免费 | 日吞吐 1.33 万亿、用户 230 万 |
| 🇨🇳 **智谱 BigModel / ZCode** | 夜间畅用至 9/20 | 23:00–09:00 额度归零；6 款旗舰实测不扣资源包（无截止日） |
| 🇨🇳 **商汤 Token Plan** | 每 5 小时刷新 · 20 个 Key | flash-lite 1500 次 / 5h、u1-fast 1500 次 / 5h、deepseek-v4-flash 150 次 / 5h |
| 🇨🇳 **AMD Radeon Cloud** | 4 款免费 · 免绑卡 | 完整 1M 上下文、Points 不产生账单；约 28–30 tok/s |
| 🇨🇳 **华为云码道 / 阿里云百炼** | 码道每日 1000 万 tokens · 百炼每模型 100 万 | 国内直连；码道适合短任务 |
| 🌐 **Ollama Cloud** | 会话 / 周限额（未公开） | 今日重要性上升：MiniMax M3（86 分）最稳免费门 |
| 🌐 **Cloudflare Workers AI** | 每日 1 万 Neurons · 50+ 模型 | 按 Neurons 计费，需自行换算 |
| 🌐 **Groq / Cerebras** | Groq 1,000 RPD · Cerebras 100 万 tokens/天 | 速度双雄；Groq 有 TPM 8000 硬墙 |
| 🌐 **Pollinations / AgentRouter** | 免 Key 无限量 / 约 $100 额度 | 零配置；AgentRouter 无公开 SLA |

---

## ⏰ 到期红线

| 到期日 | 平台 / 模型 | 内容 | 建议动作 |
|--------|------------|------|---------|
| **9/9（明天）** | Z.ai 官方 GLM-5.3-Flash | 5 折结束：$0.075/$0.25 → $0.15/$0.50 | 今天锁量；或改用 Merge Gateway 1 折（更便宜、多 20 天） |
| 9/10 前后 | 腾讯 Hy4 preview | WorkBuddy / CodeBuddy 两周免费试用 | 想跑 770B-A49B 长上下文的抓紧 |
| 9/20 | 智谱 ZCode 夜间畅用 | 23:00–09:00 额度归零 + 其他 Agent 翻倍 | 限付费套餐；批处理挪到夜间 |
| 9/30 | Merge Gateway GLM-5.3-Flash | 1 折到期，恢复 $0.015/$0.05 | 还有 22 天，本期性价比最高、窗口最长的口子 |
| 9/30 | 腾讯 Hy3（WorkBuddy / CodeBuddy） | 国内通道限免 | B.AI 通道不受影响 |
| ~~已到期~~ | MiniMax × GMI Cloud | 9/6 到期 | 改走 Ollama Cloud 或 NVIDIA NIM |
| ~~已下架~~ | OpenRouter MiniMax 免费版 | 今日清点已消失 | 同上，换通道不换模型 |

---

## ⚠️ 风险提醒

- **📉 免费池开始净减，MiniMax 是最响的一记警钟** —— 连续四天 18 款之后今天第一次净减到 16 款，掉的还是跑量最大的两款（M3 周吞吐 5.02T、全站第 6；M2.7 第 29）。任何单一免费通道都不该成为生产依赖，主力模型至少要配两条不同厂商的通道。
- **🆓 官方口径与 API 口径不一致时，以 API 为准但要打折看** —— Zen 的 API 返回 8 个 `-free` ID，官方定价页只列 6 款。这类「API 有、文档没有」的通常是灰度或即将回收的产物。反过来也成立——第三方聚合站的免费清单普遍滞后甚至虚高（9/2 已实证 llmpricing.dev 把 Zen 标成 30 款免费、实际官方只有 6 款）。
- **🐢 免费档换强模型几乎必然伴随降速** —— OrcaRouter 换将后：质量分 4→8、上下文 262K→1M，但首字 1.96s→7.66s、生成 196→74.2 tok/s。交互类应用受影响最大，批处理与长文档任务几乎无痛。
- **🔒 免费不等于零风险：四类数据条款要分清** —— ① NVIDIA 免费端点「仅限试用，勿提交机密数据」；② Muse Spark Contributor 版以免费换「用你的 prompts 做训练」；③ Zen 免费模型可能收集数据用于改进；④ Ox Alpha 匿名期曾出现「不用于训练但会保留 prompt」的条款区分——保留与训练是两件事。涉及客户数据或商业机密的任务，一律走付费或本地权重。
- **🎣 别信「兑换码」** —— 追踪一个多月的结论：腾讯、阿里、百度、字节、智谱、月之暗面、MiniMax 从未发过通用 CDKey / 官方兑换码。网上那些「AI 新人激活码」基本是聚合站引流甚至钓鱼。

---

## 🧩 按场景选路

- **💻 日常编码 / 主力链路** —— 首选 B.AI 的 GLM-5.3-Flash（100% 免费、1.33 万亿日吞吐验证）；次选 Merge Gateway 同款 1 折（花几分钱换不限流）；备选 Qwen3.8-Flash。
- **🔬 长上下文 / 研究型任务** —— Kimi K3（NIM，92 分）、Nemotron 3.5 Lightning 30B-A3B（Merge $0 / OpenRouter / Zen 三通道）、Nemotron 3 Ultra 550B（OpenRouter / Zen 双通道 $0）。
- **🤖 Agent / 长程任务** —— Muse Spark 1.3 Contributor（Zen $0，工具调用 -20%、token -25%）；需要 1M 上下文走 GLM-5.3-Flash（Merge 1 折或 B.AI 免费）。
- **🎨 多模态 / 图像视频** —— MiniMax M3 换门继续用（Ollama Cloud 86 分 / NIM 84 分）；图像理解走商汤 `sensenova-6.7-flash-lite`（1500 次 / 5h）；通用视觉走 Gemini 3.8 Flash（AI Studio 永久免费）。
- **🏥 垂直领域** —— 医疗 Ling 3.0 Flash Sante、金融 Ling 3.0 Flash Fin（均 OpenRouter `:free`，262K + 工具调用，均不支持图片）。
- **🇨🇳 国内直连 / 免代理** —— 华为云码道（每日 1000 万 tokens）、商汤 Token Plan、AMD Radeon Cloud（4 款免费、完整 1M 上下文）、阿里云百炼（每模型 100 万 tokens）。
- **🚀 零配置 / 临时起意** —— Pollinations（免 Key，URL 直拼）；或 `openrouter/free` / `orcarouter/free` 自动路由。

---

## 📊 本轮数据核对方法

本期全部数字均来自**今日实时抓取**与官方页面，不做推测：

- **OpenRouter `/api/v1/models`**（9/8 脚本清点，428 款中 16 款 `prompt` 与 `completion` 同时为 0；与 9/7 存档 `or_models_0907.json` 逐 ID 求差集，得出换出 2 款、换入 0 款）
- **OpenCode Zen `/zen/v1/models`**（70 款，8 个 `-free` ID，与 9/7 零增减）与官方定价页
- **AGI Hunt 2026-09-08 日报**（Merge Gateway 促销条款、MiniCPM5-2B、NeoMME、Gemini Student，经 llmpricing.dev 交叉验证 180 款 / 1 款 $0）
- **RuntimeWire 9/7**（OrcaRouter 换将，含 7 天实测延迟与吞吐数据）
- **llmpricing.dev**（OrcaRouter 117 款 / 5 款 $0、Merge Gateway 180 款 / 1 款 $0 的完整价目）
- **freellm.net** 9/5–9/7 核验榜（453+ 模型 / 31 家平台 / 291 款免信用卡）
- **dailyai.report** 9/6 快照（OpenRouter 真实吞吐排行，用于判断 MiniMax M3 下架的分量）
- **B.AI 官方数据**（1.33 万亿日吞吐、230 万用户、4 款保留免费）
- **智谱官方公告**（Flash × ZCode 夜间畅用、Weekend Build）
- **什么值得买 / IT 之家 / 阿里云开发者社区 / CSDN**（国内一线实测与额度横评）

---

<sub>⚠️ 免费额度可能随时调整，请以各平台官网最新政策为准。OpenRouter 免费池日内会波动，16 款是脚本清点时刻的快照。Merge Gateway 的 1 折为付费折扣而非免费，请按自身预算评估。</sub>

<sub>© [lph12168x/Free-LLM-Daily](https://github.com/lph12168x/Free-LLM-Daily) · 🤖 由 WorkBuddy 自动化生成 · 2026-09-08</sub>
