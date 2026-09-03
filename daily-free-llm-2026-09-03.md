# 免费大模型日报 · 2026-09-03（周四）

> 聚焦「量大能用的先进模型」· 覆盖 35+ 国内外平台 · [在线阅读 HTML 版](./daily-free-llm-2026-09-03.html)

## 📌 本期焦点

1. **⚠️ B.AI 免费阵容今晚收缩（9/3 17:00 SGT）** —— `DeepSeek-V4-Flash` 与 `DeepSeek-V4-Flash-Vision-Exp` 结束免费档，转 DeepSeek 官方峰谷定价的 5 折 / 7.5 折。**同一份公告明确：GLM-5.3-Flash、Qwen3.8-Flash、Hy3、MiMo V2.5 保持 100% 免费。** 手里还有 DeepSeek V4 Flash 批量任务的，今天之内跑完。

2. **🔎 Ox Alpha 真身揭晓 = GLM-5.3-Flash** —— 匿名刷榜、6 天狂揽 42 万亿 Token 的神秘模型，官方确认是智谱 GLM-5.3-Flash：320B 总参 / 18B 激活，GLM-5 系列首个**原生全模态**（文本 / 图像 / 视频），1M 上下文，稀疏 + 线性混合注意力（注意力计算降 3 倍、KV 缓存降 4.4 倍），**MIT 开源**，AA 智能指数 57（对标 Claude Opus 4.8）。最关键：**全部推理流量由约 10 万卡国产 AI 芯片承载**。B.AI 标 FREE & UNLIMITED。

3. **🆕 Meta Muse Spark 1.3 今日发布** —— Muse Code 与 Meta Model API 同日上线。相比 1.2：工具调用减少约 20%、token 消耗降低约 25%，支持单线程内长周期多工作流。**OpenCode Zen 上已有 `muse-spark-1.3-contributor-free`** —— 但免费以「授权用你的 prompt/completion 训练未来 Meta 模型」为代价。

4. **🆕 新平台发现：AIHubMix，56 款免费模型** —— 注册无需信用卡，先送 10 次试用调用（永不过期）；**一次性充值任意金额（最低 $1）后全部 56 款永久切换为日配额：100 请求/天 · 10/分钟 · 1M tokens/天，每日重置**。三种协议全支持。近 30 天真实跑量 33.2B tokens / 265K 请求。

5. **🆕 华为云码道体验版套餐 9/1 上线** —— ¥0 免费、500 万 Tokens/月、50 席位，个人试用无需付费与实名。与「码力续航计划」每日 1000 万免费 tokens 叠加，8/31 福利池新增 GLM-5.3-Flash。

6. **🆕 开源三连发** —— GLM-5.3 全量开源（753B / 756GB，1-bit GGUF 约 217GB）、Qwen3.8-Flash（125B-A6B，训练成本降 90%）、腾讯 Hy4 Preview（770B-A49B，Apache 2.0，1-bit GGUF 约 229GB）。本地部署门槛已降到 2–3 张高端卡。

7. **📉 OpenRouter 免费池 21 → 18** —— 424 款模型中 18 款 prompt/completion 同时为 0，3 天内净减 3 款。免费池正在动态出清。

---

## 🏆 量大能用的先进模型 · Top 12

| # | 模型 | 平台 / 免费入口 | 关键规格 | 综合分 |
|---|------|----------------|---------|--------|
| 1 | **GLM-5.3-Flash（Ox Alpha）** | B.AI / BigModel / AIHubMix / 开源权重 | 320B-A18B · 原生全模态 · 1M 上下文 · MIT 开源 · 国产芯片承载 | 96 |
| 2 | **Muse Spark 1.3** | Meta Model API / Muse Code / OpenCode Zen | 今日发布 · 工具调用 -20% · token -25% | 95 |
| 3 | **MiniMax M3** | OpenRouter / GMI / Vercel Gateway / AIHubMix | 1M 上下文 / 943K 输出 · 文图视频 · **9/6 到期** | 93 |
| 4 | **Qwen3.8-Flash** | B.AI / 阿里百炼 / 两个免费公共端点 | 125B-A6B · Qwen4 架构先导 · 训练成本 -90% · 开源 | 92 |
| 5 | **GLM-5.3** | 智谱 BigModel（实测限时免费） | 智能指数 59.5 · 1.3M 上下文 · 753B 已开源 | 91 |
| 6 | **DeepSeek-V4-Pro / V4-Flash** | 华为码道 CodeArts | 每日 1000 万 + 体验版 500 万/月 · **B.AI 通道今晚退场** | 90 |
| 7 | **Nemotron 3 Ultra 550B-A55B** | OpenRouter `:free` / AIHubMix | 550B · 1M 上下文 · 常驻免费档 | 89 |
| 8 | **Kimi K3** | AIHubMix / OpenCode Zen | 1.05M 上下文 · 文本/视觉/视频 · 100 次/天 | 88 |
| 9 | **Hy3（腾讯混元）** | B.AI 100% 免费 / AIHubMix `hy3-free` | 256K 上下文 · 请求量榜第 2 | 87 |
| 10 | **MiMo V2.5（小米）** | B.AI / Zen `mimo-v2.5-free` | 256K · 推理/代码/数学 · B.AI 保留免费 | 86 |
| 11 | **Inkling / Inkling Small** | OpenRouter `:free` | 1M 上下文 · 推理型 · 支持工具调用 | 85 |
| 12 | **Gemini 3.8 Flash** | AIHubMix `gemini-3.8-flash-free` | 1M 上下文 · 文/图/音/视频四模态 | 84 |

---

## 🔌 API 提供商免费额度总览（15 家重点 · 9/3 核对）

| 平台 | 免费额度 | 关键限制 |
|------|---------|---------|
| 🇨🇳 **华为云码道 CodeArts** | 每日 1000 万 tokens + 体验版 500 万/月 | 体验版 ¥0 / 50 席位 / 9-01 上线；当日清零不累计；**仅限 IDE / 插件内消费，不可导出 API Key** |
| 🆕 **AIHubMix** | 56 款免费 · $1 解锁 1M tokens/天 | 未充值仅 10 次试用；充值后 100 请求/天 · 10/分钟；**56 款共用同一个 1M tokens/天池子** |
| 🌐 **B.AI** | 4 款 100% 免费 | GLM-5.3-Flash / Qwen3.8-Flash / Hy3 / MiMo V2.5；**DeepSeek 双模型今晚 17:00 SGT 退场** |
| 🧠 **智谱 BigModel** | 6 款旗舰实测免费 + 2000 万 tokens | 旗舰无官方截止日；`glm-4.7-flash` / `glm-4.6v-flash` 永久免费不限量；并发约 1 |
| 🔀 **OpenRouter** | 18 款 `:free`（较 9/2 净减 3） | 未充值 50 请求/天，充值 $10 后 1000 请求/天 |
| ⚡ **OpenCode Zen** | 8 个在架免费 ID | **全部为「数据换免费」**；隐私负载只用 `laguna-s-2.1-free` 或 `deepseek-v4-flash-free` |
| 🔥 **火山方舟（豆包）** | 200 万/天 + 代码场景 500 万/天 | 三套账叠加；**额度无熔断开关，超用直接出账单**；Q3 普惠至 9/30 |
| 🚀 **Groq** | 30 RPM · 14,400 请求/天 | 实测 527 tok/s（第 2 名的 3 倍）；无需信用卡；**TPM 8000 墙，不适合 Agent** |
| 💎 **GMI Cloud** | MiniMax 4 款 · 至 9/6 | 零余额下仅 M3 / M2.7 / Speech 2.8 / Music 3.0，**其余 80+ 模型一律 402** |
| 🧩 **Vercel AI Gateway** | $5/月 网关额度 | 只收网关费；`minimax/minimax-m3-free` 预计 9/6 后停用 |
| 💻 **硅基流动 SiliconFlow** | 新用户 2000 万 tokens | 一个 Key 聚合 100+ 模型；9B 以下永久免费；**额度消耗速度跟模型绑定** |
| ☁️ **阿里云百炼** | 每模型 100 万 tokens（可叠加） | **90 天有效期，过期作废**，别囤着 |
| 🔧 **CommandCode / OpenCode Go** | $1/月 → $10 credits | **订阅制不是真免费**；旗舰档（Kimi K3 / Qwen3.8 Max / Grok 4.6）月额度仅 $15 |
| 🇨🇳 **百度千帆 / 讯飞星火** | 永久免费，但慢 | 千帆 ERNIE-Speed QPS 50；讯飞 Spark Lite **QPS 仅 2** |
| 🤗 **HuggingFace / Empero 端点** | Qwen3.8-Flash-Next · 零门槛 | Empero Key 填 `free`；HF 端点 Key 填 `none`；**这类端点通常只存活几天** |

---

## ⏰ 到期红线

| 日期 | 对象 | 内容 |
|------|------|------|
| **9/3 17:00 SGT** | B.AI · DeepSeek-V4-Flash 系列 | **今天**：退出免费档，转官方峰谷价 5 折 / 7.5 折 |
| **9/6** | MiniMax × GMI Cloud | M3 / M2.7 / Speech 2.8 / Music 3.0 不限量窗口结束 |
| 9/6 | Vercel AI Gateway | `minimax/minimax-m3-free` 预计停用 |
| 9/6 | MiniMaxathon 创作赛 | 提交截止，奖池 $1,500 GMI 额度 |
| **9/9 24:00** | GLM-5.3-Flash 半价 | $0.075/$0.25 → $0.15/$0.50 |
| 9/10 23:59 | 腾讯 Hy4 Preview | WorkBuddy 限免结束 |
| 9/18 | Zen GPT 5.6 Sol 五折 | 付费通道折扣到期 |
| 9/24 | 百度 Comate 限免第二弹 | 测试版不限量 token 到期 |
| 9/30 23:59 | 腾讯 Hy3 | 限免结束（已延期一次） |
| 9/30 | 火山方舟 Q3 普惠 | 代码调试每日 500 万 tokens 窗口结束 |
| 9/30 | Dots3-Note Preview `:free` | 512K 上下文免费端点下线 |
| 11/8 | 火山方舟 Coding Plan | 2.5 折优惠到期 |
| 12/31 | 腾讯云 TokenHub | 新人最高 100 万 token |

---

## ⚠️ 风险提醒

- **⏰ 今日最紧急：B.AI 的 DeepSeek 双模型今晚退场**。9/3 17:00 SGT 起 V4-Flash 与 V4-Flash-Vision-Exp 转 5 折 / 7.5 折；GLM-5.3-Flash、Qwen3.8-Flash、Hy3、MiMo V2.5 不受影响。挂在这两个模型上的脚本今天内改路由。
- **🔒 Zen 的 8 个免费 ID 全部有附加条件**：Big Pickle / MiMo-V2.5 / Ling 3.0 Flash Fin 免费期内数据可用于改进模型；Nemotron 走 NVIDIA 试用端点禁提交机密数据；Muse Spark Contributor 明确用于训练未来 Meta 模型。
- **💳 GMI Cloud 的「免费」只有 4 个模型**：零余额下其余 80+ 模型（含 GLM-5.3-Flash、GPT-5.5、DeepSeek、Kimi K3）全部返回 `402 Insufficient balance`，图像生成与 MiniMax-H3 也不在免费范围。
- **🚫 四家老牌免费层已失效**：GitHub Models 7/30 退役返回 HTTP 410；Cerebras 8 月起需绑卡（$5 / 30 天）；SambaNova 与 Together AI 返回 `PAYMENT_METHOD_REQUIRED`。
- **🔓 免费公共端点寿命以「天」计**：Empero 与 HuggingFace 的 Qwen3.8-Flash-Next 端点是好心人自掏算力，请勿压测、不要放生产。
- **💰 AIHubMix 的 $1 门槛要算清**：不充值只有 10 次试用；充值后 1M tokens/天是 **56 款共用一个池子**，且部分模型请求权重更高（`gpt-4.1-free`、`gpt-4o-free` 仅 20 次/天）。
- **🔥 火山方舟免费额度没有熔断开关**：超用直接按量出账单，务必自设 Token 熔断。网传「9 月免费额度已结束」经核实是误传。
- **📉 OpenRouter 免费池 3 天净减 3 款**：别把免费 ID 写死，做成可配置路由表并定期回源核对。

---

## 🎯 按身份挑一条

- **个人开发者 / 学生**：华为码道体验版（¥0 / 500 万 tokens 月 / 50 席位）+ 码力续航计划（每日 1000 万）打底，智谱 `glm-4.7-flash` 兜底长期低频、GLM-5.3 跑重活，再挂 B.AI 免费用 GLM-5.3-Flash 与 Qwen3.8-Flash。**月成本 ¥0。**
- **小团队 / 初创**：AIHubMix（$1 一次性充值 → 56 款、1M tokens/天）+ FreeLLMAPI 自建网关（635 端点收敛到一个 `/v1`）+ CommandCode Go $1/月。涉及客户代码时改用 `laguna-s-2.1-free`。**月成本约 ¥7–70。**
- **研究者 / 最大参数**：GLM-5.3（753B / 756GB，1-bit GGUF 约 217GB）、腾讯 Hy4 Preview（770B-A49B，Apache 2.0，约 229GB）、Qwen3.8-Flash（125B-A6B，约 72.5GB，单张 RTX 6000 可装）。云端看 Nemotron 3 Ultra（550B）与 Inkling（975B）。
- **Agent / 长程任务**：首选 Muse Spark 1.3（工具调用 -20%、token -25%，注意数据授权条款）；追求隐私用 GLM-5.2（230K 输出）或 Nemotron 3.5 Lightning（1M 高吞吐）。**避开 Groq（TPM 8000 墙）**。MiniMax M3 还有 3 天。

---

## 🆕 两个零门槛免费端点（Qwen3.8-Flash-Next）

```bash
# ① Empero 实验室 — FP8 量化，4×B200，官方称无限 Token
curl https://free.empero.org/v1/chat/completions \
  -H "Authorization: Bearer free" -H "Content-Type: application/json" \
  -d '{"model":"Qwen3.8-Flash-Next","messages":[{"role":"user","content":"你好"}]}'

# ② HuggingFace 公共端点 — 262K 上下文、视觉多模态、工具调用、>100 tok/s
curl https://pnywsahxhac1qjbo.us-east-2.aws.endpoints.huggingface.cloud/v1/chat/completions \
  -H "Content-Type: application/json" -H "Authorization: Bearer none" \
  -d '{"model":"Qwen/Qwen3.8-Flash-Next","messages":[{"role":"user","content":"Hello!"}]}'
```

---

**数据来源**：OpenRouter `/api/v1/models`（9/3 脚本清点，424 款中 18 款 $0）· OpenCode Zen `/zen/v1/models`（66 款，8 个免费 ID）与官方定价页 / Privacy 段 · AIHubMix 免费模型目录与 30 天用量统计 · B.AI 官方公告 · 华为云开发者联盟与帮助中心最新动态 · free-llm.com · freellm.net · mianfeisuanli.com · toolfreebie.com（8/31 实测基准）· 稀土掘金 · NodeLoc · FreeLLMAPI 开源仓库。

⚠️ 免费额度可能随时间调整，请以各平台官网最新政策为准。本页所有「免费」判定均以官方接口或官方定价页为准。

⭐ [lph12168x/Free-LLM-Daily](https://github.com/lph12168x/Free-LLM-Daily) · 🤖 由 WorkBuddy 自动化生成
