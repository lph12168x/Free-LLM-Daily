# Free-LLM-Daily

> 每日免费大模型日报 · 自动更新

🌐 **在线访问**：[https://lph12168x.github.io/Free-LLM-Daily/](https://lph12168x.github.io/Free-LLM-Daily/)

每天自动搜集并整理可免费使用的国内外大模型信息，生成精美 HTML 报告。

## 📰 今日摘要（2026-09-02）

🔥 **华为码道 CodeArts「码力续航计划」每日白送 1000 万 tokens——单日额度最大的零门槛免费，9/1 上新 GLM-5.3-Flash**：注册华为云账号并开通码道体验版后**登录即每日领 1000 万 tokens**，额度当天有效、0 点清零不累计，**不用绑信用卡、不用邀请裂变**，第一期总池价值 100 万元 tokens 先到先得。福利模型池当前含 `deepseek-v4-pro-0813`、`deepseek-v4-flash-0731`，并于 **9/1 新上 `glm-5.3-flash`**；体验版另含每天可用的 4 个内置免费模型（GLM-5.2 / OpenPangu-2.0-Flash / GLM-4.7-ArkTS-SPARK / OpenPangu-2.0-Pro）。⚠️ **硬限制：tokens 只能在码道 IDE / VS Code 插件 / JetBrains 插件 / CLI 内消费，不能导出成自己的 API Key 接外部系统**——这是它和自购额度最大的区别。同期还送 720 核时免费云开发环境与免费 AI Shell。

🆕 **智谱 BigModel 6 款旗舰实测限时免费（含 GLM-5.3，不扣资源包额度）**：9/1 用真实 API Key 实测，`GLM-5.3`、`GLM-5.3-Flash`、`GLM-5.2`、`GLM-5.1`、`GLM-4.5-Air`、`GLM-4.6V-FlashX` 六款**调用成功且不扣赠送资源包**——等于在新用户 2000 万 tokens 之外多出一整层旗舰额度。GLM-5.3 的 Artificial Analysis 智能指数 **59.5，国内厂商第二**（Kimi K3 为 59.7），原价 ¥8 输入 / ¥28 输出每百万 tokens。⚠️ 页面未标截止日期、随时可能恢复收费，**不要设计进生产关键路径**；长期兜底用永久免费不限量的 `glm-4.7-flash` / `glm-4.6v-flash`。另 ZCode 下载送 3 亿 tokens、GLM Coding Plan 每天限量 1 万张体验卡。

🆕 **DeepSeek 8/31 开源 V4-Flash-Vision-Exp（MIT）**：V4 系列首款原生多模态，305B 总参 / 每 token 仅激活 13B（**激活率 4.6%**，比 Hy4 的 6.4% 更激进），1M 上下文、最大输出约 384K。ApexBench 36.5、ZeroBench 35 反超 Claude Opus 4.8，DeepSWE 59.3% 登顶、TerminalBench 83.9，纯文本推理与 Agent 能力完整保留。**成本侧最狠：单张图压缩到约 384 token、一次请求可塞 600 张，视觉与文本同价，没有 vision 溢价档**。⚠️ 标注 Exp 实验版，官方定位为架构验证载体，建议按自身负载实测再上生产。

⚠️ **数据打假：OpenCode Zen 官方只有 6 款免费，不是第三方站标的 30 款**：llmpricing.dev 标称 OpenCode Zen 有 30 款 $0 模型，但官方定价页明确 Free 的只有 6 款——`big-pickle`（隐匿模型）、`mimo-v2.5-free`、`ling-3.0-flash-fin-free`、`nemotron-3-ultra-free`、`nemotron-3.5-lightning-free`、`muse-spark-1.2-contributor-free`。榜单上的 `kimi-k2.5-free`、`minimax-m2.5-free` 早在 8/5 弃用，`glm-5-free` 5/14 弃用。直接拉官方 `/v1/models` 接口也只得到 7 个带 free 标记的 ID。**规则：第三方站用来发现线索，官方定价页 / 接口用来下决策。**

💎 **量大能用的先进模型 Top 12（9/2）**：① DeepSeek-V4-Pro/V4-Flash（华为码道，每日 1000 万 tokens）；② GLM-5.3（BigModel 限时免费，智能指数 59.5）；③ MiniMax M3（1M 上下文 / 943K 输出 / 多模态 / 周调用 4.54T，9/5–9/6 到期）；④ Nemotron 3 Ultra 550B-A55B（周调用 4.96T 居免费模型之首，三处免费不共享额度）；⑤ DeepSeek-V4-Flash-Vision-Exp（305B/13B、MIT）；⑥ Inkling 975B-A41B（免费池参数天花板，支持音频输入）；⑦ Gemini 3.6 Flash（freellm 实测 90 分全站最高，全模态 1M）；⑧ Kimi K3（智能指数 59.7 国内第一，NVIDIA NIM）；⑨ Nemotron 3.5 Lightning（30B/3B 激活、1M 上下文、高吞吐）；⑩ GLM-5.2（230K 输出上限）；⑪ LongCat-2.0（1.6T 总参 / 48B 激活、5 万张国产算力卡全流程、MIT）；⑫ Laguna S 2.1（Terminal-Bench 70.2%，CommandCode 常驻免费）。

🔌 **新入口 / 免费 API 提供商**：OmniRoute（MIT 开源网关，单端点连 268 个提供商、50+ 免费层、约 **16 亿免费 tokens/月**、11 家永久免费无需信用卡含 LongCat / Kiro / Pollinations，内置 RTK 压缩省 15–95% tokens）；LongCat（美团 1.6T 总参 / 48B 激活、30 万亿 token 预训练、原生 1M 上下文、MIT，官方 longcat.chat）；FreeTheAi（50+ 模型、OpenAI 兼容、Discord 领 key、**无需信用卡**，但未公开速率限制）；讯飞星辰 MaaS（星火 X2.5 API 限时免费，端侧首个原生 1M 上下文）；华为其他三条并行额度（MaaS 免费服务页签 200 万 tokens / AgentArts 200 万 / OfficeAce 每日 1000 次）。

⏰ **本周到期红线**：**9/5** CommandCode 的 `minimax-m3-free` / `minimax-m2.7-free`；**9/6** MiniMax × GMI Cloud 联合活动（M3 / M2.7 / Speech 2.8 / Music 3.0 不设使用量限制、不绑卡）；**9/9 24:00** GLM-5.3-Flash 半价到期（$0.075/$0.25 → $0.15/$0.50）；**9/10 23:59** 腾讯 Hy4 preview 限免结束（Hy3 延至 9/30 23:59）；**9/30** OpenRouter `dots-3-note-preview:free`（512K 上下文）下线。

⚠️ **风险提醒**：Cerebras 官方 FAQ 确认**已取消永久免费层**（$5 credits、30 天过期、需先绑卡）；Google Gemini 自 4/1 起**所有 Pro 档免费层移除**，仅 Flash / Flash-Lite 保留，且免费资格由自动系统判定（部分项目直接提示需绑卡）；Groq 免费层 **TPM 8000**，实际可用工作集仅约 7000 token，需要 64K+ 上下文的 Agent 框架直接跑不了，且 413 常被 harness 误报成「上下文溢出」；OpenCode Zen 的 Big Pickle / MiMo / Ling 免费期内数据可用于改进模型，Muse Spark 明确用于训练未来 Meta 模型，两个 Nemotron 走 NVIDIA 试用端点禁提交机密数据。

## 📰 今日摘要（2026-08-20）

🔥 **百度文心快码 Comate 限免第二弹（不限量 Token·新发现）+ LobsterAI 延长至 8/31 + 千问下载 30 亿登顶全球**：🔵 8/19 百度开发者中心悄然上线文心快码 Comate 测试版限免第二弹——主打「不限量 Token」，覆盖 Ernie 4.5T/X1T/DeepSeek 等 9 款模型，注册登录立得 7 天、每邀请 1 好友再得 3 天（最高叠 37 天），活动截止 2026-09-24，目前少有博主写、属「小漏网」级白嫖窗口（注意它是 IDE 编程助手形态、非裸 API）。🟢 LobsterAI 5000 积分活动「反转」：原 8/20 截止延长至 8/31 并加码（邀请最高 4000+每日签到 100+上线 DeepSeek Harness），顺手登录领取即可。

🌏 **千问全球下载破 30 亿登顶第一（Google 7×、Meta 13×）+ Qwen3.8-27B 本地部署提速 + DeepSeek Harness 开源**：阿里千问系列全球累计下载超 30 亿次（Google 4.18 亿、Meta 2.27 亿），累计开源 460+ 模型、衍生超 30 万；Qwen3.8-27B（Apache 2.0）两天下载破百万、衍生 15 万+，社区让本地门槛再降——Unsloth 高精度 GGUF（8GB RAM 可跑）、M5 Max 达 70 tok/s，被称「本地 Opus 4.6」。🐙 DeepSeek 开源 Harness v0.1（MIT，模型/工具/沙箱/编排全插件化 Agent 框架）。

💎 **高分免费模型 Top 3**：kimi-k3（98 分 / Ollama Cloud 免费层 + 全球最大开源权重 2.8T，蝉联第一，但 session/weekly 限额）、GLM-5.2（93 分 / NVIDIA NIM 永久免费 + 开源，量大能用最稳冠军）、Gemini 3.6 Flash（90 分 / AI Studio 免费层）；场外：DeepSeek V4 Flash（88·多入口免费）、MiniMax M3（88·多模态）、Gemini 3.5 Flash（88）、Ling-3.0-flash（85）、Nemotron 3 Ultra（84）、Kimi K2.6（82）、Step-3.7-Flash（75）。⚠️ 🆕 Gemini 3.7 Flash（8/16 上线）实测仅 45 分偏弱、暂不建议当主力；GLM-5.3（8/19 API 上线·AA Index 60）当下付费、权重 8/28 才开源；Tencent Hy3 限免 8/31 截止（剩 11 天）、OpenRouter 已转 Paid。

⌨️ **新入口 / 免费 API 提供商（不止 FreeLLM 类网站）**：OpenCode Zen（DeepSeek V4 Flash Free、MiniMax M3 Free、Nemotron 3 Ultra Free、Big Pickle、MiMo-V2.5 Free、North Mini Code Free、🆕 Nemotron 3.5 Lightning Free，Base URL https://opencode.ai/zen/v1）；OpenRouter（Nemotron 3 Ultra、Gemma 4、Step-3.7-Flash、Ling-3.0-flash 等 25+，50 次/天、充 $10 升 1000）；Nous Portal（Solar Pro 4 / Hy3 / Step-3.7-Flash / Laguna S·XS 免费，20% off 延长）；火山引擎方舟（每日 200 万 Token 免费含 V4 Pro）；NVIDIA NIM（77 款永久免费、40 RPM 无日限额）；🆕 百度文心快码 Comate（IDE 内不限量 Token 限免第二弹）；CommandCode（免费档含 Laguna S 2.1 FREE、GOAT $10→$70 额度覆盖 33+ 模型）。

🎁 **大额每日刷新（11 家量大平台）**：阿里云百炼（70+ 模型每款 100 万 Token）、NVIDIA NIM（125 模型、77 款永久免费）、OpenCode Zen（多款 -Free 限时免费）、百度文心快码 Comate（不限量 Token·9 款模型·9/24 截止）、美团 LongCat（500 万/天）、火山引擎（200 万/天）、Groq（14400 次/天）、硅基流动（新用户 2000 万）、腾讯云 TokenHub（每模型 100 万）、OpenRouter（25+ 免费、50 次/天、充 $10 升 1000）、Nous Portal（多款免费）、网易 LobsterAI（5000 积分·8/31）。

🆕 **今日新增关注**：百度文心快码 Comate 限免第二弹（不限量 Token）、LobsterAI 延长至 8/31、Gemini 3.7 Flash 上线（实测 45 偏弱）、OpenCode Zen Nemotron 3.5 Lightning Free、DeepSeek Harness v0.1 开源。✅ 已开源：Kimi K3、GLM-5.2、MiniMax M3、Ling-3.0-flash、Nemotron 3 Ultra、Qwen3.8-27B、DeepSeek V4 系列。⏳ 即将开源：GLM-5.3 权重（8/28）。⚠️ 风险提醒：Comate 是 IDE 助手非裸 API、LobsterAI 延长至 8/31、GLM-5.3 当下付费（等 8/28 权重）、Qwen3.8-Max License 非 Apache 2.0、OpenCode Zen 限时免费+数据用于训练、OpenRouter 免费层 50 次/天账户级、腾讯混元旧平台 9/30 停服、GCP 16 端点 10/21 退役、Hy3 限免 8/31 截止（剩 11 天）。

## 📰 今日摘要（2026-08-19）

🔥 **智谱 GLM-5.3 API 8/19 凌晨上线——743B、AA Index 60 并列开源第一，付费 API 但权重 8/28 开源进 NIM 免费层**：GLM-5.3 沿用 GLM-5.2 底座、全部提升来自后训练缩放，在 Artificial Analysis Intelligence Index 取得 60 分，与 Kimi K3 并列开源模型第一、与 Claude Fable 5 / GPT-5.6 Sol 同档。Terminal-Bench 3.0 由 4.6 升至 28.3、DeepSWE v1.1 66.9、Agents' Last Exam 28.5、白盒漏洞发现 CyberGym 84.5%（高于 Mythos 5 的 83.8%）。API 定价与 GLM-5.2 持平（腾讯云 输入 8 / 输出 28 / 缓存命中 2 元每百万），权重计划下周五（8/28）开源——届时进 NVIDIA NIM 永久免费层。⚠️ 当下免费入口仍是 GLM-5.2（NVIDIA NIM 94 分、1M 上下文、40 RPM 无日限额、永久免费）。

🌏 **中国开源 AI 成美国大模型「底座」：Qwen3.8-27B 登顶 HF 趋势榜、两天下载破百万、衍生 15 万+**：Hugging Face《开源模型现状：2026 夏季观察》显示中国实验室月度最大开源模型规模（7540 亿–2.78 万亿）持续领先美国，部分美国千亿级模型以中国模型为底座。Qwen3.8-27B（Apache 2.0、24GB 显卡可跑）开源两天下载破 100 万次、衍生模型超 15 万个居全球第一。DeepSeek Harness（DSH）8/13 开放预览，三天 GitHub Star 超 13 万。

💎 **高分免费模型 Top 3**：kimi-k3（98 分 / Ollama Cloud 免费层 + 开源，登顶第一，但 session/weekly 限额）、GLM-5.2（94 分 / NVIDIA NIM 永久免费 + 开源，量大能用最稳冠军）、Gemini 3.6 Flash（91 分 / AI Studio 免费层，第三）；场外：DeepSeek V4 Flash（90·多入口免费）、MiniMax M3（89·多模态多入口）、Nemotron 3 Ultra（85）、Ling-3.0-flash（87）。⚠️ Tencent Hy3（90）经 WorkBuddy/CodeBuddy 限免至 8/31（剩 13 天）仍可用、OpenRouter 已转 Paid；GLM-5.3 为付费 API、权重 8/28 开源后才进免费层。

⌨️ **新入口 / 免费 API 提供商（不止 FreeLLM 类网站）**：OpenCode Zen（DeepSeek V4 Flash Free、MiniMax M3 Free、Nemotron 3 Ultra Free、Big Pickle、MiMo-V2.5 Free 等限时免费，Base URL https://opencode.ai/zen/v1）；OpenRouter（Nemotron 3 Ultra、Gemma 4、gpt-oss、Ling-3.0-flash 等 25+，50 次/天、充 $10 升 1000）；Nous Portal（Step-3.7-Flash / Nemotron-3-Ultra / Owl-Alpha 3 款免费，OAuth device-code 登录）；火山引擎方舟（每日 200 万 Token 免费含 V4 Pro）；NVIDIA NIM（77 款永久免费端点、40 RPM 无日限额）。

🎁 **大额每日刷新（10 家量大平台）**：火山引擎方舟（200 万/天、含 V4 Pro）、阿里云百炼（70+ 模型每款 100 万 Token）、NVIDIA NIM（125 模型、77 款永久免费、40 RPM 无日限额）、OpenCode Zen（多款 -Free 限时免费）、美团 LongCat（500 万/天起）、Groq（14400 次/天）、硅基流动（新用户 2000 万）、腾讯云 TokenHub（每模型 100 万）、OpenRouter（25+ 免费、50 次/天、充 $10 升 1000）、Nous Portal（3 款新免费）。

🆕 **今日新增关注**：智谱 GLM-5.3 API 上线（AA Index 60 并列开源第一，付费但权重 8/28 开源）、中国开源成美国「底座」（Qwen3.8-27B 登顶 HF 趋势榜）。✅ 已开源：Kimi K3、GLM-5.2、MiniMax M3、Ling-3.0-flash、Nemotron 3 Ultra、Qwen3.8-27B、DeepSeek V4 系列。⏳ 即将开源：GLM-5.3 权重（8/28）。⚠️ 风险提醒：DeepSeek 官方 API 8/17 峰谷涨价（免费党转火山/NIM/Zen/Nous）、GLM-5.3 当前付费（等 8/28 权重）、Qwen3.8-Max License 非 Apache 2.0 大规模商用需授权、OpenCode Zen 限时免费+数据用于训练、腾讯混元旧平台 9/30 停服、GCP 16 个端点 10/21 退役、OpenRouter 免费层 50 次/天账户级、Hy3 限免至 8/31（剩 13 天）。

## 📰 今日摘要（2026-08-18）

🔥 **DeepSeek 官方 API 8/17 峰谷涨价 + 火山引擎方舟 8/18 每日 200 万 Token 免费含 V4 Pro**：DeepSeek 官方 API 分时定价 8/17 生效——V4 Pro 高峰缓存命中输入 0.025→0.30 元/百万（+1100%）、输出 6→27 元/百万（+350%），低谷半价；纯 API 免费党受冲击。补偿方案：火山引擎方舟 8/18 起开放每日 200 万 Token 免费额度（含 V4 Pro），需手动设 190 万 Token 熔断防超额；另有 OpenCode Zen 的 DeepSeek V4 Flash Free（1M 上下文）、NVIDIA NIM 永久免费模型。🆕 Nous Portal 新提供 3 款免费模型（Step-3.7-Flash / Nemotron-3-Ultra / Owl-Alpha），OpenAI 兼容、OAuth device-code 登录。

💎 **高分免费模型 Top 3**：kimi-k3（98 分 / Ollama Cloud 免费层 + 开源，登顶第一，但 session/weekly 限额）、GLM-5.2（95 分 / NVIDIA NIM 永久免费 + 开源，量大能用最稳冠军）、Gemini 3.6 Flash（91 分 / AI Studio 免费层，第三）；场外：DeepSeek V4 Flash（90·多入口免费）、MiniMax M3（89·多模态多入口）、Nemotron 3 Ultra（85）、Ling-3.0-flash（87）。⚠️ Tencent Hy3（90）经 WorkBuddy/CodeBuddy 限免至 8/31（剩 13 天）仍可用、OpenRouter 已转 Paid；DeepSeek 官方 API 8/17 涨价，免费党建议改走火山引擎方舟 / NVIDIA NIM。

⌨️ **新入口 OpenCode Zen 限时免费模型**：OpenCode 官方模型网关，GitHub/Google 免信用卡即领 Key，OpenAI 兼容（Base URL https://opencode.ai/zen/v1）；带「Free」标签的 DeepSeek V4 Flash Free（1M 上下文 / 384K 输出）、MiniMax M2.5 Free、Nemotron 3 Ultra Free、Big Pickle、MiMo-V2.5 Free、North Mini Code Free、Hy3 preview 限时免费。⚠️ 限时免费、数据可能用于改进模型，敏感数据勿走免费档；早前 qwen3.6-plus-free 已下架，用前先 `opencode models` 看当前可用。

🎁 **大额每日刷新（9 家量大平台）**：阿里云百炼（70+ 模型每款 100 万 Token、总额 7000 万）、NVIDIA NIM（125 模型、77 款永久免费、40 RPM 无日限额）、OpenCode Zen（多款 -Free 限时免费）、美团 LongCat（500 万/天起、最高 1.2 亿）、火山引擎（200 万/天）、Groq（14400 次/天）、硅基流动（新用户 2000 万）、腾讯云 TokenHub（每模型 100 万）、OpenRouter（25+ 免费、50 次/天、充 $10 升 1000）。

🆕 **今日新增关注**：火山引擎方舟每日 200 万 Token 免费（含 V4 Pro）、Nous Portal 3 款免费模型、DeepSeek V4 Flash Free（OpenCode Zen）。✅ 已开源：Kimi K3、GLM-5.2、MiniMax H3/M3、Ling-3.0-flash、Nemotron 3 Ultra、Qwen3.8-27B、DeepSeek V4 系列。⚠️ 风险提醒：DeepSeek 官方 API 8/17 涨价（免费党转火山/NIM）、Qwen3.8-Max License 非 Apache 2.0 大规模商用需授权、OpenCode Zen 限时免费+数据用于训练、腾讯混元旧平台 9/30 停服、GCP 16 个端点 10/21 退役、OpenRouter 免费层 50 次/天账户级、Hy3 限免至 8/31（剩 13 天仍可用）。


## 内容覆盖

- 永久免费大模型（DeepSeek、智谱GLM、百度千帆、硅基流动等）
- 大额免费平台（火山引擎、阿里百炼、Groq、Mistral、Cerebras等）
- 限时免费 / 新发布模型
- 零成本组合方案（日常 / 编程 / 开发者 / 图像生成）
- 即将下线与价格调整风险提醒

## 文件列表

| 日期 | 在线查看 | 源文件 |
|------|---------|--------|
| 2026-08-20 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-08-20.html) | [HTML](daily-free-llm-2026-08-20.html) |
| 2026-08-19 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-08-19.html) | [HTML](daily-free-llm-2026-08-19.html) |
| 2026-08-18 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-08-18.html) | [HTML](daily-free-llm-2026-08-18.html) |
| 2026-08-17 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-08-17.html) | [HTML](daily-free-llm-2026-08-17.html) |
| 2026-08-14 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-08-14.html) | [HTML](daily-free-llm-2026-08-14.html) |
| 2026-08-13 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-08-13.html) | [HTML](daily-free-llm-2026-08-13.html) |
| 2026-08-12 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-08-12.html) | [HTML](daily-free-llm-2026-08-12.html) |
| 2026-08-11 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-08-11.html) | [HTML](daily-free-llm-2026-08-11.html) |
| 2026-08-10 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-08-10.html) | [HTML](daily-free-llm-2026-08-10.html) |
| 2026-08-07 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-08-07.html) | [HTML](daily-free-llm-2026-08-07.html) |
| 2026-08-06 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-08-06.html) | [HTML](daily-free-llm-2026-08-06.html) |
| 2026-08-04 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-08-04.html) | [HTML](daily-free-llm-2026-08-04.html) |
| 2026-08-03 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-08-03.html) | [HTML](daily-free-llm-2026-08-03.html) |
| 2026-07-31 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-07-31.html) | [HTML](daily-free-llm-2026-07-31.html) |
| 2026-07-30 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-07-30.html) | [HTML](daily-free-llm-2026-07-30.html) |
| 2026-07-29 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-07-29.html) | [HTML](daily-free-llm-2026-07-29.html) |
| 2026-07-28 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-07-28.html) | [HTML](daily-free-llm-2026-07-28.html) |
| 2026-07-27 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-07-27.html) | [HTML](daily-free-llm-2026-07-27.html) |
| 2026-07-26 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-07-26.html) | [HTML](daily-free-llm-2026-07-26.html) |
| 2026-07-25 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-07-25.html) | [HTML](daily-free-llm-2026-07-25.html) |
| 2026-07-24 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-07-24.html) | [HTML](daily-free-llm-2026-07-24.html) |
| 2026-07-23 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-07-23.html) | [HTML](daily-free-llm-2026-07-23.html) |
| 2026-07-22 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-07-22.html) | [HTML](daily-free-llm-2026-07-22.html) |
| 2026-07-21 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-07-21.html) | [HTML](daily-free-llm-2026-07-21.html) |
| 2026-07-20 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-07-20.html) | [HTML](daily-free-llm-2026-07-20.html) |
| 2026-07-19 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-07-19.html) | [HTML](daily-free-llm-2026-07-19.html) |
| 2026-07-18 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-07-18.html) | [HTML](daily-free-llm-2026-07-18.html) |
| 2026-07-17 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-07-17.html) | [HTML](daily-free-llm-2026-07-17.html) |
| 2026-07-16 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-07-16.html) | [HTML](daily-free-llm-2026-07-16.html) |
| 2026-07-15 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-07-15.html) | [HTML](daily-free-llm-2026-07-15.html) |
| 2026-07-14 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-07-14.html) | [HTML](daily-free-llm-2026-07-14.html) |
| 2026-07-13 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-07-13.html) | [HTML](daily-free-llm-2026-07-13.html) |
| 2026-07-12 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-07-12.html) | [HTML](daily-free-llm-2026-07-12.html) |
| 2026-07-11 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-07-11.html) | [HTML](daily-free-llm-2026-07-11.html) |
| 2026-07-10 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-07-10.html) | [HTML](daily-free-llm-2026-07-10.html) |
| 2026-07-09 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-07-09.html) | [HTML](daily-free-llm-2026-07-09.html) |
| 2026-07-08 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-07-08.html) | [HTML](daily-free-llm-2026-07-08.html) |
| 2026-07-07 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-07-07.html) | [HTML](daily-free-llm-2026-07-07.html) |
| 2026-07-06 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-07-06.html) | [HTML](daily-free-llm-2026-07-06.html) |
| 2026-07-05 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-07-05.html) | [HTML](daily-free-llm-2026-07-05.html) |
| 2026-07-04 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-07-04.html) | [HTML](daily-free-llm-2026-07-04.html) |
| 2026-07-03 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-07-03.html) | [HTML](daily-free-llm-2026-07-03.html) |
| 2026-07-02 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-07-02.html) | [HTML](daily-free-llm-2026-07-02.html) |
| 2026-07-01 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-07-01.html) | [HTML](daily-free-llm-2026-07-01.html) |
| 2026-06-30 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-06-30.html) | [HTML](daily-free-llm-2026-06-30.html) |
| 2026-06-29 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-06-29.html) | [HTML](daily-free-llm-2026-06-29.html) |
| 2026-06-26 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-06-26.html) | [HTML](daily-free-llm-2026-06-26.html) |
| 2026-06-25 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-06-25.html) | [HTML](daily-free-llm-2026-06-25.html) |
| 2026-06-24 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-06-24.html) | [HTML](daily-free-llm-2026-06-24.html) |
| 2026-06-23 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-06-23.html) | [HTML](daily-free-llm-2026-06-23.html) |
| 2026-06-22 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-06-22.html) | [HTML](daily-free-llm-2026-06-22.html) |
| 2026-06-18 | [📖 查看日报](https://lph12168x.github.io/Free-LLM-Daily/daily-free-llm-2026-06-18.html) | [HTML](daily-free-llm-2026-06-18.html) |

## GitHub Pages 配置

仓库根目录的 `index.html` 为 GitHub Pages 首页，自动展示最新日报导航。

启用方式：Settings → Pages → Source: Deploy from a branch → Branch: `main` / `(root)`

## 数据来源

freellm.net、llm-stats.com、lmmarketcap.com、知乎、CSDN、博客园、各大模型官方平台。

## 更新机制

由 WorkBuddy 自动化任务每日 09:30 自动生成并推送。
