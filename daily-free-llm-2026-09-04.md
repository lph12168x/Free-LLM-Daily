# 免费大模型日报 · 2026-09-04（周五）

> 聚焦「量大能用的先进模型」· 覆盖 36+ 国内外平台 · [在线阅读 HTML 版](./daily-free-llm-2026-09-04.html)

## 📌 本期焦点

1. **🆕 头号新闻：AMD 入局，Radeon Cloud Token Factory 免费开放 4 款模型 API** —— AMD 中国开发者站上线 **Token Factory**（BETA），Public Free Model APIs 专区现有 4 款：`DeepSeek-V4-Flash-0731`（284B MoE、**1,048,576 上下文**、流式 / 工具调用 / 思考模式）、`DeepSeek-V4-Flash-Vision-Exp`（1M 上下文视觉版，标注 **Limited Free**）、`Qwen3.8-Flash-Next`（256K）、`MiniCPM5-1B`（OpenBMB，128K）。它罕见地同时凑齐三件事：**国内直连、免绑信用卡、每天重置额度**——邮箱 / 手机号 / GitHub / CSDN / 魔搭一键登录，不用翻墙。Base URL `https://developer.amd.com.cn/radeon/api/v1`，Key 以 `rc-` 开头，**4 款免费模型共用同一个 Key**。原生双协议：一套 Key 同时兼容 OpenAI `/chat/completions` 与 Anthropic `/messages`。**OpenCode 已集成**，Claude Code（CC Switch）、Cline、Continue、Cherry Studio、LangChain、Cursor 实测都能填；⚠️ **ZCode 目前会报参数错误，暂不支持**。

2. **💰 AMD 额度必须自己查，别信教程里的数字** —— 官方 Usage API 文档示例写的是 `daily_cost_limit_usd: 10`，但**近期多个实测反馈新账号看到的是每天 1 美元**，官方也明说不同账户额度可能不同、以后可能调整。额度**每天早上 8 点重置**。按官方积分规则（输入 0.14 pts / 百万、输出 0.28、缓存读取 0.0028）折算，1 美元/天约合 **650 万 tokens**，10 美元档约 6500 万。限速：单 Key 30 RPM、单 IP 120 RPM、**单 Key 并发 8**、账户网关 20 RPM。查询命令见文末。⚠️ **Daily budget 从早期 10 美元调到 1 美元，这个信号值得警惕。**

3. **🆕 智谱「Flash × ZCode」夜间畅用：9/3–9/20，每晚 23:00–09:00 完全免费** —— GLM Coding Plan 推出夜间畅用活动，付费套餐用户无需手动开启、系统自动生效。规则两条：① 通过官方工具 **ZCode** 调用 GLM-5.3-Flash，**额度消耗为 0，等于完全免费**；② 通过套餐支持的其他 Agent 调用，**可用额度翻倍（×2）**。⚠️ 仅限 GLM-5.3-Flash，选 GLM-5.3 仍按标准规则扣；且**前提是 GLM Coding Plan 付费套餐用户**，这是给已付费用户的夜间加成，不是面向所有人的白嫖。GLM-5.3-Flash：320B-A18B、1M 上下文、AA 智能指数 57（对标 Claude Opus 4.8）、定价仅 GLM-5.2 的 1/10。

4. **🆕 商汤 Token Plan 把智谱旗舰 GLM-5.2 纳入免费公测** —— 入口 `sensenova.cn/token-plan`，Base URL `https://token.sensenova.cn/v1`，OpenAI 兼容，手机号 + 实名认证。额度是 **5 小时滚动刷新**——SenseNova 系列通常 1500 次 / 5 小时。和 AMD「每天一桶」相比，商汤是「每 5 小时一小桶」，**持续高强度使用时更抗造**。隐藏细节：控制台余量页**可能看不到 GLM-5.2 字样**，但直接切 `glm-5.2` 能成功调用。

5. **✅ B.AI 收缩已落地，4 款仍 100% 免费** —— 9 月 3 日 17:00（SGT）起 `DeepSeek-V4-Flash` 与 `V4-Flash-Vision-Exp` 结束免费档，转对齐官方峰谷定价：工作日 09:00–12:00、14:00–18:00（SGT）高峰 **5 折**，其余工作日时段与周末 **7.5 折**。**GLM-5.3-Flash、Qwen3.8-Flash、腾讯 Hy3、小米 MiMo-V2.5 继续保持 100% 免费。** 平台同时披露：累计 Token 吞吐 **超 10.9 万亿**、**8956 万次 API 调用**、**23.9 万新注册用户**（其中 23.5 万是 API 开发者）。

6. **🔎 数据核对：OpenCode Zen 定价页 Free 行 6 → 7 款** —— 新增 `muse-spark-1.3-contributor-free`。接口 `/zen/v1/models` 实拉 66 款，识别出 **9 个免费 ID**（定价页 7 款 + 接口额外 `deepseek-v4-flash-free`、`laguna-s-2.1-free`）。

7. **🔎 数据校正：OpenRouter 免费池 21 款，与 9/3 存档快照零增减** —— 9/4 脚本清点 427 款模型中 21 款 prompt 与 completion 同时为 0。⚠️ 昨日日报正文记录的 18 是当日盘中快照，现已回补至 21。免费池是动态的，别写死单一 ID。

8. **📉 免费午餐正在一张张收走** —— 美团 LongCat 2.0 免费已停；B.AI 的 DeepSeek V4 Flash 双模型退场；OpenCode 免费池收缩到 MiMo 2.5 等少数几款；GitHub Models（HTTP 410）、Cerebras（需绑卡）、SambaNova 与 Together（`PAYMENT_METHOD_REQUIRED`）四家老牌免费层已全部失效。八月底像是个分水岭——看到真免费、免绑卡、能持续用的，先领到手。

---

## 🏆 量大能用的先进模型 · Top 12

| # | 模型 | 平台 / 免费入口 | 关键规格 | 综合分 |
|---|------|----------------|---------|--------|
| 1 | **GLM-5.3-Flash（Ox Alpha）** | B.AI / 智谱 ZCode（夜间免费）/ 华为码道 / AIHubMix | 320B-A18B · 原生全模态 · 1M 上下文 · MIT 开源 · 国产芯片承载 | 96 |
| 2 | **DeepSeek-V4-Flash** | 🆕 **AMD Radeon Cloud** / 华为码道 / 商汤 Token Plan | 284B MoE · 1,048,576 上下文 · **国内直连免绑卡** | 94 |
| 3 | **GLM-5.2** | 🆕 **商汤 Token Plan（免费公测）** / OpenRouter `:free` | 1M 无损上下文 · 128K 输出 · **5 小时滚动刷新** | 92 |
| 4 | **Qwen3.8-Flash-Next** | 🆕 **AMD Radeon Cloud** / Empero / HF 公共端点 | 262K 上下文 · 训练成本 -90% · 开源权重 | 91 |
| 5 | **MiniMax M3** | OpenRouter / GMI / Ollama Cloud / AIHubMix | 1M 上下文 / 943K 输出 · 文图视频 · **9/6 到期** | 90 |
| 6 | **Nemotron 3 Ultra 550B-A55B** | NVIDIA NIM / OpenRouter `:free` / AIHubMix | 550B-A55B · 1M 上下文 · 常驻免费档 · 权重开源 | 89 |
| 7 | **Kimi K3** | NVIDIA NIM（freellm 89 分）/ AIHubMix / Zen | 1.05M 上下文 · 文本/视觉/视频 · 62.4 tok/s | 88 |
| 8 | **Muse Spark 1.3** | Meta Model API / Muse Code / OpenCode Zen | 工具调用 -20% · token -25% · **数据换免费** | 87 |
| 9 | **Hy3（腾讯混元）** | B.AI 100% 免费 / AIHubMix `hy3-free` | 256K 上下文 · 请求量榜第 2 · B.AI 保留免费 | 86 |
| 10 | **Inkling / Inkling Small** | OpenRouter `:free` | 1M 上下文 · 推理型 · 支持工具调用 | 85 |
| 11 | **MiMo V2.5（小米）** | B.AI / Zen `mimo-v2.5-free` | 256K · 推理/代码/数学 · B.AI 保留免费 | 84 |
| 12 | **MiniCPM5-1B（OpenBMB）** | 🆕 **AMD Radeon Cloud** | 1B 极致轻量 · 131K 上下文 · 首字延迟极低 | 82 |

---

## 🗞️ 当日新增动态

| 时间 | 动态 | 对「免费党」的实际意义 |
|------|------|---------------------|
| **9/4** | **AMD Radeon Cloud Token Factory 上线 Public Free Model APIs**：DeepSeek-V4-Flash-0731（1M）、Vision-Exp（Limited Free）、Qwen3.8-Flash-Next（256K）、MiniCPM5-1B（128K） | **本期头号**：国内直连 + 免绑卡 + 每日重置，一套 Key 走双协议，OpenCode 已集成 |
| **9/3 深夜** | **智谱「Flash × ZCode」夜间畅用**：至 9/20，每晚 23:00–09:00，ZCode 内 GLM-5.3-Flash 额度消耗 0，其他 Agent ×2 | 夜间跑批的黄金时段；但仅限 GLM Coding Plan 付费套餐用户 |
| **9/3 17:00 SGT** | **B.AI 调整正式生效**：DeepSeek-V4-Flash / Vision-Exp 转 5 折 / 7.5 折；4 款保留免费 | 6 款免费缩到 4 款；累计吞吐 10.9 万亿 Token、8956 万次调用 |
| **本周** | **商汤 Token Plan 把 GLM-5.2 纳入免费公测**：5 小时滚动刷新、1500 次/5 小时 | 与 AMD「每天一桶」互补；控制台可能不显示 GLM-5.2，但直接调可用 |
| **9/4** | **OpenCode Zen 定价页 Free 行 6 → 7 款**：新增 `muse-spark-1.3-contributor-free` | Muse Spark 1.3 免费档上线；代价是授权用你的数据训练未来 Meta 模型 |
| **9/4** | **OpenRouter 脚本清点**：427 款中 21 款为 0，与 9/3 快照零增减 | **数据校正**：9/3 正文的 18 是盘中快照，现已回补至 21 |
| **近期** | **美团 LongCat 2.0 免费已停**；OpenCode 免费池收缩到 MiMo 2.5 等少数几款 | 八月底是分水岭，厂商公测预算烧完开始算账 |
| **8/24–9/6** | **MiniMax × GMI Cloud 14 天无限量**：M3 / M2.7 / Speech 2.8 / Music 3.0 | ⚠️ **剩 2 天**；零余额下其余 80+ 模型一律返回 402 |

---

## 🔌 API 提供商免费额度总览（9/4 核对）

| 平台 | 免费额度 | 要点 |
|------|---------|------|
| 🆕 **AMD Radeon Cloud** | 4 款免费 · 每日重置 · 免绑卡 | Token Factory（BETA）：DeepSeek-V4-Flash-0731（1M）、Vision-Exp（Limited Free）、Qwen3.8-Flash-Next（256K）、MiniCPM5-1B（128K）。`rc-` Key 四款通用，**OpenAI + Anthropic 双协议**，OpenCode 已集成。额度每日 8 点重置（官方示例 $10，实测不少新账号为 $1）。单 Key 30 RPM / 并发 8。**短板：首字约 22 秒、28–30 tok/s** |
| 🆕 **商汤 Token Plan** | 5 小时滚动刷新 · 1500 次/5 小时 | GLM-5.2 纳入免费公测，比 AMD 更抗持续高强度调用。Base URL `https://token.sensenova.cn/v1`，模型名 `glm-5.2` / `deepseek-v4-flash` / `sensenova-6.7-flash-lite`。手机号 + 实名 |
| **华为云码道 CodeArts** | 每日 1000 万 tokens + 体验版 500 万/月 | 体验版 ¥0、50 席位、无需实名。码力续航当日清零、不绑卡不裂变，总池 100 万元先到先得，8/31 新增 GLM-5.3-Flash。**仅限 IDE / 插件内消费，不可导出 API Key** |
| **B.AI** | 4 款 100% 免费（9/3 起） | GLM-5.3-Flash、Qwen3.8-Flash、Hy3、MiMo-V2.5 保持免费；DeepSeek 双模型已转折扣。OpenAI + Anthropic 双兼容 |
| **智谱 BigModel / ZCode** | 夜间免费（23:00–09:00，至 9/20） | 付费套餐在 ZCode 内调 GLM-5.3-Flash 额度消耗 0，其他 Agent ×2。非套餐用户走新人 2000 万 token 或 `glm-4.7-flash` 永久免费 |
| **OpenRouter** | 21 款 `:free`（427 款中） | 与 9/3 存档快照零增减。1M 上下文档：inkling、inkling-small、minimax-m3、nemotron-3.5-lightning、nemotron-3-ultra-550b。未充值 50 请求/天，充值 $10 后 1000/天 |
| **OpenCode Zen** | 定价页 7 款 Free · 接口 9 个免费 ID | Free 行 6 → 7（新增 Muse Spark 1.3 Contributor）。接口额外有 `deepseek-v4-flash-free`、`laguna-s-2.1-free`。**全部为「数据换免费」** |
| **NVIDIA NIM** | 1000 credits（可申请到 5000）· 40 RPM | credits 不过期、不按 token 计费，160+ 模型。**只推荐 `nemotron-3-ultra-550b-a55b`**——Kimi K3 62.4 tok/s、Gemma 4 31B 50.9、DeepSeek V4 Flash 仅 27.3，对比 Groq 约 500 差一个数量级 |
| **GMI Cloud** | MiniMax 4 款 · 至 9/6 | 零余额下 M3 / M2.7 / Speech 2.8 / Music 3.0 免费。**其余 80+ 模型一律返回 402** |
| **Groq** | 30 RPM · 14,400 请求/天 | 实测 527 tok/s，是第二名（Mistral 167）的 3 倍多。**避坑：TPM 8000 墙** |
| **火山方舟（豆包）** | 200 万/天 + 代码场景 500 万/天 | 三套账叠加，Q3 普惠至 9/30。**额度无熔断开关，超用直接出账单**。网传「9 月已结束」是误传 |
| **AIHubMix** | 56 款免费 · $1 解锁 1M tokens/天 | 一次性充值 $1 后全部转永久日配额：100 请求/天 · 10/分钟 · 1M tokens/天。三种协议全支持。30 天实测 33.2B tokens |
| **硅基流动 SiliconFlow** | 新用户 2000 万 tokens | 一个 Key 聚合 100+ 模型，**9B 以下永久免费**，国内延迟 <100ms |
| **阿里云百炼 / 腾讯云 TokenHub** | 每模型 100 万 tokens（可叠加） | 百炼 90 天有效、过期作废；腾讯云 TokenHub 活动到 **12/31** |
| **CommandCode / OpenCode Go** | $1/月 → $10 credits | 严格说是低价订阅。GOAT $10/月给 $70（30+ 模型、每模型独立额度池）。**旗舰档杠杆只有 1.5 倍** |
| **百度千帆 / 讯飞星火** | 永久免费，但慢 | 千帆 ERNIE-Speed 永久免费 **QPS 50**（免费档并发最慷慨）；讯飞 Spark Lite 永久免费但 **QPS 仅 2** |
| **Ollama Cloud / Kilo Code** | `:cloud` 模型 · 按会话/周限 | Ollama `:cloud` 后缀模型跑云端不占本地显存；Kilo Code 个人版 MIT 免费、支持 500+ 模型 BYOK |

---

## ⏰ 到期红线

| 日期 | 对象 | 内容 |
|------|------|------|
| **9/6** | MiniMax × GMI Cloud | **剩 2 天**：M3 / M2.7 / Speech 2.8 / Music 3.0 不限量窗口结束 |
| **9/6** | Vercel AI Gateway | `minimax/minimax-m3-free` 预计停用 |
| **9/9 24:00** | GLM-5.3-Flash 半价 | 0.4 / 1.4 元每百万 → 恢复 0.8 / 2.8 元 |
| **9/10 23:59** | 腾讯 Hy4 Preview | WorkBuddy 限免结束（Hy3 已延期至 9/30） |
| 9/18 | Zen GPT 5.6 Sol 五折 | 付费通道折扣到期 |
| 9/20 | 智谱夜间畅用 | GLM Coding Plan「Flash × ZCode」全免费窗口结束 |
| 9/24 | 百度 Comate 限免第二弹 | 测试版不限量 token 到期 |
| 9/30 23:59 | 腾讯 Hy3 | 限免结束（已延期一次） |
| 9/30 | 火山方舟 Q3 普惠 | 代码调试每日 500 万 tokens 窗口结束 |
| 9/30 | Dots3-Note Preview `:free` | 512K 上下文免费端点下线 |
| 11/8 | 火山方舟 Coding Plan | 2.5 折优惠到期 |
| 12/31 | 腾讯云 TokenHub / 微信小程序成长计划 | 新人最高 100 万 token；小程序计划 10 亿 token + 10 万张生图 |

---

## ⚠️ 风险提醒

- **💰 AMD 的「免费」有每日预算上限，而且口径不一**。官方 Usage API 文档示例是 `daily_cost_limit_usd: 10`，但**近期多个实测反馈新账号看到的是每天 1 美元**，官方也明说不同账户额度可能不同、以后可能调整。**Daily budget 从 10 美元调到 1 美元，这个信号值得警惕。** 不要照抄教程里的数字，自己拉一次 `/api/profile/model-usage`。AMD 是芯片厂商做生态，战略性补贴通常比纯 API 厂商公测持久，但绝不是永久承诺。
- **🐢 AMD 慢、NIM 更慢：别把免费端点当主力链路**。AMD 实测首字延迟约 **22 秒**、输出 **28–30 tok/s**，单 Key 并发只有 8。NVIDIA NIM 更夸张：Kimi K3 62.4 tok/s、Gemma 4 31B 50.9、**DeepSeek V4 Flash 仅 27.3**，而 Groq 约 500。结论：AMD 适合写稿、测提示词、代码 Review、小规模 RAG；NIM 只推荐 Nemotron 3 Ultra 一款。接进 Agent 务必自建队列、并发控在 8 以内、对 429 做退避重试。
- **🔒 免费 = 数据换免费：Zen 的 7 款 Free 全部有附加条件**。Big Pickle / MiMo-V2.5 / Ling 3.0 Flash Fin 免费期内数据可能用于改进模型；Nemotron 走 NVIDIA 试用端点，禁提交个人或机密数据、会话被记录（不与身份关联）；Muse Spark 1.2 / 1.3 Contributor 明确「以提示词和补全用于训练未来 Meta 模型」换取极低折扣，且仅对 Meta 允许的地区开放。**涉及客户代码或业务数据，只用 `laguna-s-2.1-free` 或 `deepseek-v4-flash-free`**——注意这两个 ID 只在接口里、定价页没列，属于「隐性可用」，随时可能消失。
- **📉 免费午餐正在一张张收走**。本周实证：美团 LongCat 2.0 免费已停；B.AI 的 DeepSeek V4 Flash 双模型 9/3 退场；OpenCode 免费池收缩到 MiMo 2.5 等少数几款；GitHub Models（7/30 退役、HTTP 410）、Cerebras（取消免卡免费档）、SambaNova 与 Together（`PAYMENT_METHOD_REQUIRED`）四家老牌免费层此前已全部失效。
- **🎁 智谱夜间免费是「付费套餐的加成」，不是白嫖**。前提是 **GLM Coding Plan 付费套餐用户**，没订阅拿不到这个 0 消耗。且**仅限 GLM-5.3-Flash**，错峰时段选 GLM-5.3 仍按标准规则扣额度。非套餐用户走 BigModel 新人 2000 万 token 或 `glm-4.7-flash` 永久免费档更实际。
- **💳 GMI Cloud 的「免费」只有 4 个模型，其余全 402**。零余额下只有 M3、M2.7、Speech 2.8、Music 3.0 可用，其余 80+ 模型（含 GLM-5.3-Flash、GPT-5.5、DeepSeek、Kimi K3）全部返回 `402 Insufficient balance`。网上「80+ 模型免费」是误读。窗口 9/6 结束。
- **🔓 免费公共端点寿命以「天」计**。Empero 与 HuggingFace 的 Qwen3.8-Flash-Next 端点是好心人自掏算力，通常只存活几天。**好消息是 Qwen3.8-Flash-Next 现在有了 AMD 这个官方通道，别再压测私人端点。**
- **🔥 火山方舟免费额度没有熔断开关，超用直接出账单**。三套账叠加，最大坑是超出部分直接按量计费、不会先停你。用之前务必自设 Token 熔断（如当日累计 190 万触发断路）并挂余额预警。网传「9 月免费额度已结束」经核实是误传。

---

## 🎯 按身份挑一条

- **🎓 个人开发者 / 学生（零成本）**：**今天新增三张卡，建议都领**：① **AMD Radeon Cloud**——国内直连免绑卡，DeepSeek-V4-Flash 1M 上下文，跑 Coding Agent 主力；② **商汤 Token Plan**——GLM-5.2，5 小时滚动刷新，AMD 额度见底就切它；③ **华为码道**——每日 1000 万 tokens 打底（限 IDE 内）。再挂 B.AI 免费用 GLM-5.3-Flash 与 Qwen3.8-Flash。**月成本 ¥0。**
- **👥 小团队 / 初创**：AIHubMix（$1 一次性充值 → 56 款模型、1M tokens/天，一个 Key 打通三种协议）+ AMD（4 款、双协议）+ CommandCode Go $1/月。涉及客户代码时绕开 Zen 的 Big Pickle / MiMo / Ling / Muse Spark，改用 `laguna-s-2.1-free`。有 ZCode 工作流的，把重活排到 23:00–09:00 跑 GLM-5.3-Flash。**月成本约 ¥7–70。**
- **🔬 研究者 / 最大参数**：云端优先 **Nemotron 3 Ultra 550B**（NIM 免费档里唯一速度能打的，1M 上下文、SWE-Bench Verified 70.7）与 **Inkling**（975B、1M）。本地部署看开源三连发：GLM-5.3（753B / 756GB，1-bit GGUF 约 217GB）、腾讯 Hy4 Preview（770B-A49B，Apache 2.0，约 229GB）、Qwen3.8-Flash（125B-A6B，约 72.5GB，单张 RTX 6000 可装）。
- **🤖 Agent / 长程任务**：首选 **Muse Spark 1.3**（工具调用 -20%、token -25%，专为长周期多工作流设计，注意 Contributor 版的数据授权条款）；要 1M 上下文就走 AMD 的 DeepSeek-V4-Flash 或 MiniMax M3（剩 2 天）。**避开 Groq（TPM 8000 墙）与 NIM 的非 Nemotron 模型（<63 tok/s）**；Laguna S 2.1 是终端操作场景唯一常驻免费档。高频轻活交给 MiniCPM5-1B。

---

## 🔧 上手：AMD Radeon Cloud 三步接入

```bash
# ① 拿 Key：developer.amd.com.cn/radeon/tokenfactory → Login → 点任意免费模型卡片
#    Key 以 rc- 开头，4 款免费模型共用同一个
export AMD_API_KEY="rc-你的Key"

# ② 验证连通（OpenAI 协议）
curl https://developer.amd.com.cn/radeon/api/v1/chat/completions \
  -H "Authorization: Bearer $AMD_API_KEY" -H "Content-Type: application/json" \
  -d '{"model":"DeepSeek-V4-Flash","messages":[{"role":"user","content":"写一个 Go 实现的 LRU Cache"}]}'

# ③ 查自己账号的真实额度（重点看 daily_cost_limit_usd / daily_cost_remaining_usd）
curl "https://radeon-global.anruicloud.com/api/profile/model-usage?include_recent=true" \
  -H "Authorization: Bearer $AMD_API_KEY"

# 附：查看当前可用模型列表
curl https://developer.amd.com.cn/radeon/api/v1/models -H "Authorization: Bearer $AMD_API_KEY"
```

**OpenCode 配置**（`~/.config/opencode/opencode.json`，Windows 在 `%APPDATA%/opencode/opencode.json`）：

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "amd": {
      "npm": "@ai-sdk/openai",
      "name": "AMD Radeon Cloud",
      "options": {
        "baseURL": "https://developer.amd.com.cn/radeon/api/v1",
        "apiKey": "rc-你的Key"
      },
      "models": {
        "DeepSeek-V4-Flash": { "name": "DeepSeek V4 Flash (1M)", "limit": { "context": 1048576, "output": 16384 } },
        "Qwen3.8-Flash-Next": { "name": "Qwen3.8 Flash Next", "limit": { "context": 262144, "output": 16384 } },
        "MiniCPM5-1B": { "name": "MiniCPM5 1B", "limit": { "context": 131072, "output": 8192 } }
      }
    }
  },
  "model": "amd/DeepSeek-V4-Flash"
}
```

> ⚠️ 任何支持自定义 Base URL 的客户端都能直接填这三样：Base URL `https://developer.amd.com.cn/radeon/api/v1`、API Key `rc-` 开头那串、模型名 `DeepSeek-V4-Flash` 或 `Qwen3.8-Flash-Next`。实测可用：OpenCode、Claude Code（CC Switch）、Cline、Continue、Cherry Studio、LangChain、Cursor。**ZCode 暂不支持，会报参数错误。**

---

## 📊 本轮数据核对方法

本期为 9 月 4 日全网挖掘，所有关键数字均回源核对：

- **OpenRouter `/api/v1/models`** 脚本清点（427 款模型，其中 21 款 `prompt` 与 `completion` 同时为 0，与 9/3 存档快照**零增减**）
- **OpenCode Zen `/zen/v1/models`** 接口实拉 66 款、识别出 9 个免费 ID，并与 **opencode.ai/docs/zen** 官方定价页 Free 行（**7 款**）与 Privacy 段逐条比对
- **AMD Radeon Cloud Token Factory** 官方页面与 Usage API 文档（Base URL、Key 格式、限速、积分规则、4 款模型清单）
- **智谱官方公告**（Flash × ZCode 夜间畅用，经 IT之家、钛媒体、界面新闻交叉验证）
- **B.AI 官方公告**（经 WEEX、KuCoin Flash、深潮 TechFlow 转述交叉验证）
- **商汤日日新平台文档**（Token Plan、5 小时窗口、模型 ID）
- **freellm.net** 9/3 核验榜单（452+ 模型 / 31 家提供商 / 234 款实接口验证）
- **华为云开发者联盟 + 帮助中心「最新动态」**
- **稀土掘金 / 什么值得买 / 微信公众号** 国内一线实测与额度横评

---

**数据来源**：OpenRouter `/api/v1/models`（9/4 脚本清点，427 款中 21 款 $0）· OpenCode Zen `/zen/v1/models`（66 款，9 个免费 ID）与官方定价页 / Privacy 段 · AMD Radeon Cloud Token Factory 官方页面与 Usage API 文档 · 智谱官方公告（9/3 夜间畅用）· B.AI 官方公告（9/3 17:00 SGT 生效）· 商汤日日新平台文档 · freellm.net 9/3 核验榜单 · 华为云开发者联盟与帮助中心最新动态 · free-llm.com · mianfeisuanli.com · 稀土掘金 · 什么值得买 · FreeLLMAPI 开源仓库。

⚠️ 免费额度可能随时间调整，请以各平台官网最新政策为准。本页所有「免费」判定均以官方接口或官方定价页为准；涉及额度的具体数字（如 AMD 每日预算）请自行调用官方 Usage API 确认。

⭐ [lph12168x/Free-LLM-Daily](https://github.com/lph12168x/Free-LLM-Daily) · 🤖 由 WorkBuddy 自动化生成
