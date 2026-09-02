# 免费大模型日报 · 2026-09-02（周三）

> 聚焦「量大能用的先进模型」· 覆盖 33+ 国内外平台 · [在线阅读 HTML 版](./daily-free-llm-2026-09-02.html)

## 📌 本期焦点

1. **🆕 华为码道 CodeArts「码力续航计划」每日白送 1000 万 tokens** —— 单日额度最大的零门槛免费。注册开通体验版后登录即领，0 点清零不累计，不用绑卡不裂变，福利池含 `deepseek-v4-pro-0813`、`deepseek-v4-flash-0731`，9/1 新上 `glm-5.3-flash`。**硬限制：只能在码道 IDE / 插件 / CLI 内消费，不能导出 API Key。**

2. **🆕 智谱 BigModel 6 款旗舰实测限时免费** —— GLM-5.3 / 5.3-Flash / 5.2 / 5.1 / GLM-4.5-Air / GLM-4.6V-FlashX 经 9/1 真实 API Key 验证可调且不扣资源包额度。GLM-5.3 智能指数 59.5 国内第二。**页面未标截止日期，随时可能恢复收费。**

3. **🆕 DeepSeek-V4-Flash-Vision-Exp 8/31 开源（MIT）** —— 305B 总参 / 13B 激活（4.6%），1M 上下文，单图仅 384 token、一次可塞 600 张，视觉与文本同价。ApexBench 36.5、DeepSWE 59.3% 登顶。标注 Exp 实验版。

4. **⚠️ 数据打假：OpenCode Zen 官方只有 6 款免费** —— 第三方站标的 30 款是过期数据，`kimi-k2.5-free` 8/5 已弃用、`glm-5-free` 5/14 已弃用。

5. **⏰ 本周到期红线** —— MiniMax M3 免费窗口 9/5–9/6 密集到期；GLM-5.3-Flash 半价 9/9；Hy4 限免 9/10。

---

## 🏆 量大能用的先进模型 · Top 12

| # | 模型 | 平台 / 免费入口 | 关键规格 | 综合分 |
|---|------|----------------|---------|--------|
| 1 | **DeepSeek-V4-Pro / V4-Flash** | 华为码道 CodeArts | 每日 1000 万 tokens · 1M 上下文 · 不绑卡 | 96 |
| 2 | **GLM-5.3** | 智谱 BigModel（限时免费） | 智能指数 59.5（国内第 2）· 1.3M 上下文 · 周调用 1.46T | 94 |
| 3 | **MiniMax M3** | OpenRouter / GMI / Ollama / CommandCode | 1M 上下文 / 943K 输出 · 文图视频 · GPQA 92.9 | 92 |
| 4 | **Nemotron 3 Ultra 550B-A55B** | OpenRouter / Zen / NIM（三处） | 550B/55B 激活 · 1M · 周调用 4.96T（免费模型第一） | 91 |
| 5 | **DeepSeek-V4-Flash-Vision-Exp** | DeepSeek 开源 MIT | 305B/13B（4.6%）· 1M · 单图 384 token | 90 |
| 6 | **Inkling 975B-A41B** | OpenRouter `:free` | 975B 总参（参数天花板）· 1M · 含音频输入 | 89 |
| 7 | **Gemini 3.6 Flash** | Google AI Studio | freellm 实测 90 分（全站最高）· 全模态 · 1M | 90 |
| 8 | **Kimi K3** | NVIDIA NIM | 智能指数 59.7（国内第 1）· 1M · 131K 输出 | 89 |
| 9 | **Nemotron 3.5 Lightning** | OpenRouter / Zen / NIM | 30B/3B 激活 · 1M · 高吞吐 | 87 |
| 10 | **GLM-5.2** | OpenRouter `:free` / BigModel | 230K 输出上限 · 周调用 2.83T | 86 |
| 11 | **LongCat-2.0** | 美团 longcat.chat / OmniRoute | 1.6T 总参 / 48B 激活 · 5 万张国产算力卡 · MIT | 85 |
| 12 | **Laguna S 2.1** | CommandCode（常驻免费）/ OpenRouter | 118B/8B · Terminal-Bench 70.2% | 84 |

---

## 🔌 API 提供商免费额度总览（33 家 · 9/2 核对）

| 平台 | 免费额度 | 关键限制 |
|------|---------|---------|
| **华为码道 CodeArts** | 每日 1000 万 tokens | 当日清零；仅 IDE/插件内消费，不可导出 API Key；总池 100 万元发完即止 |
| **智谱 BigModel** | 6 款旗舰实测免费 + 2000 万 tokens（新用户） | 旗舰免费无官方截止日；`glm-4.7-flash` / `glm-4.6v-flash` 永久免费不限量 |
| **OpenRouter** | 21 款 `:free`（较 9/1 零增减） | 免费池动态上下线；速率因模型而异 |
| **NVIDIA NIM** | 99 款 $0 · 40 RPM | 试用性质，禁提交个人/机密数据；需手机号验证 |
| **Google AI Studio** | 15 RPM / 1500 RPD · 1M 上下文 | 4/1 起 Pro 档免费层全移除；部分模型日配额仅 20 次 |
| **OpenCode Zen** | **6 款**（非 30） | 免费期内数据可能用于改进模型；Muse Spark 用于训练 Meta 模型 |
| **CommandCode** | `laguna-s-2.1-free` 常驻免费 | minimax-m3/m2.7 free 只到 9/5；Go $1/月起 |
| **MiniMax × GMI Cloud** | 不设使用量限制 | **9/6 截止**；不用绑卡 |
| **LongCat（美团）** | 1.6T 总参 · MIT | 官方 longcat.chat；OmniRoute 列为永久免费提供商 |
| **OmniRoute** | 约 16 亿 tokens/月 | MIT 开源网关，需自建本地端点；内置 15–95% token 压缩 |
| **Ollama Cloud** | starter 模型小额月度额度 | 8/31 改版；Pro $20 含 $60 用量 |
| **腾讯 WorkBuddy** | Hy4 至 9/10 · Hy3 至 9/30 | 每日有限额度；Hy4 暂不支持多模态生成 |
| **DeepSeek 开放平台** | MIT 全系开源 | V4-Flash-Vision-Exp 为 Exp 实验版 |
| **讯飞星辰 MaaS** | X2.5 API 限时免费 | 端侧首个原生 1M 上下文；9/7 发布 293B 基座 |
| **Groq** | 30 RPM / 1000 RPD | **TPM 8000**，实际工作集仅约 7000 token |
| **ModelScope 魔搭** | 2000 次 API/日 | 控制台侧上下文标 8K / 输出 4K |
| **阿里云百炼** | 1 亿+ 免费 tokens | 仅华北 2 地域；不抵扣 Batch / 调优 / 部署 |
| **FreeTheAi** | 50+ 模型 | Discord 领 key，无需信用卡；未公开速率限制 |

---

## ⏰ 到期红线（按时间排序）

| 日期 | 对象 | 内容 |
|------|------|------|
| **9/5** | MiniMax M3 / M2.7（CommandCode） | `minimax-m3-free`、`minimax-m2.7-free` 免 credits |
| **9/6** | MiniMax × GMI Cloud | M3 / M2.7 / Speech 2.8 / Music 3.0 不设使用量限制 |
| **9/9 24:00** | GLM-5.3-Flash 半价 | $0.075/$0.25 → $0.15/$0.50 |
| **9/10 23:59** | 腾讯 Hy4 Preview | WorkBuddy 限免结束 |
| **9/30 23:59** | 腾讯 Hy3 | 限免结束（已延期） |
| **9/30** | Dots3-Note Preview `:free` | 512K 上下文免费端点下线 |

---

## ⚠️ 风险提醒

- **Cerebras 已无永久免费层**：官方 FAQ 确认，新账号 $5 credits、30 天过期，且需先绑定已验证支付方式。
- **Google Gemini 免费层 4/1 大幅缩水**：所有 Pro 档转付费，仅 Flash / Flash-Lite 保留；免费资格由自动系统判定，部分项目直接提示需绑卡。
- **Groq 隐性 TPM 墙**：免费层 TPM 8000，实际工作集约 7000 token，需 64K+ 上下文的 Agent 框架（如 Hermes）跑不了；413 常被误报为「上下文溢出」。
- **OpenCode Zen 隐私换免费**：Big Pickle / MiMo / Ling 免费期内数据可用于改进模型；Muse Spark 明确用于训练 Meta 模型；两个 Nemotron 走 NVIDIA 试用端点禁提交机密数据。
- **智谱旗舰免费无官方截止日**：随时可能恢复收费，不要设计进生产关键路径。
- **DeepSeek-V4-Flash-Vision-Exp 是实验版**：官方定位架构验证载体，建议实测后再上生产。

---

## 🎯 按身份挑一条

- **个人开发者 / 学生**：华为码道（每日 1000 万）+ 智谱 BigModel（GLM-5.3 跑重活、`glm-4.7-flash` 兜底）+ OpenRouter `dots-3-note-preview:free`（512K，9/30 前用完）。月成本 ¥0。
- **小团队 / 初创**：OmniRoute 开源网关（16 亿 tokens/月）+ CommandCode Go $1/月。涉及客户代码时绕开 Zen 的 Big Pickle / MiMo / Ling / Muse Spark。月成本约 ¥7–70。
- **研究者 / 最大参数**：Inkling（975B）+ LongCat-2.0（1.6T，MIT）+ Nemotron 3 Ultra（550B）。
- **Agent / 长程任务**：避开 Groq；改用 GLM-5.2（230K 输出）、MiniMax M3（943K 输出）、Nemotron 3.5 Lightning（高吞吐）、Laguna S 2.1（终端操作）。

---

**数据来源**：freellm.net 实时实测目录（452+ 免费模型 / 31 家供应商 / 235 款经活体 API 验证）、OpenRouter `/api/v1/models`（9/2 脚本清点 419 款中 21 款 $0）、opencode.ai/docs/zen 官方定价页与 `/v1/models` 接口、华为云开发者联盟 CSDN、mianfeisuanli.com、IT之家 / 腾讯新闻、HuggingNews / Pandaily、whatstrending.ai 调用量榜、toolfreebie.com 9/1 实测、aipricing.guru、llmpricing.dev / traktoken.com。

⚠️ 免费额度可能随时间调整，请以各平台官网最新政策为准。

⭐ [lph12168x/Free-LLM-Daily](https://github.com/lph12168x/Free-LLM-Daily) · 🤖 由 WorkBuddy 自动化生成
