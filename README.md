# Free-LLM-Daily

> 每日免费大模型日报 · 自动更新

🌐 **在线访问**：[https://lph12168x.github.io/Free-LLM-Daily/](https://lph12168x.github.io/Free-LLM-Daily/)

每天自动搜集并整理可免费使用的国内外大模型信息，生成精美 HTML 报告。

## 📰 今日摘要（2026-09-04）

🆕 **头号新闻：AMD 入局，Radeon Cloud Token Factory 免费开放 4 款模型 API** —— AMD 中国开发者站（`developer.amd.com.cn`）上线 **Token Factory**（BETA），Public Free Model APIs 专区现有 4 款：`DeepSeek-V4-Flash-0731`（284B MoE、**1,048,576 上下文**、支持流式 / 工具调用 / 思考模式）、`DeepSeek-V4-Flash-Vision-Exp`（1M 上下文视觉版，标注 **Limited Free** 限量免费）、`Qwen3.8-Flash-Next`（256K）、`MiniCPM5-1B`（OpenBMB，128K，首字延迟极低）。它罕见地同时凑齐三件事：**国内直连、免绑信用卡、每天重置额度**——邮箱 / 手机号 / GitHub / CSDN / 魔搭一键登录，不用翻墙。Base URL `https://developer.amd.com.cn/radeon/api/v1`，Key 以 `rc-` 开头，**4 款免费模型共用同一个 Key**，切 `model` 即可。更特别的是**原生双协议**：一套 Key 同时兼容 OpenAI `/chat/completions` 与 Anthropic `/messages`，不用自己搭转换层。**OpenCode 已原生集成**，实测 Claude Code（CC Switch）、Cline、Continue、Cherry Studio、LangChain、Cursor 都能直接填；⚠️ **ZCode 目前会报参数错误，暂不支持**。

💰 **AMD 额度必须自己查，别信教程里的数字** —— 官方 Usage API 文档示例写的是 `daily_cost_limit_usd: 10`，但**近期多个实测反馈新注册账号看到的是每天 1 美元**，官方也明说不同账户额度可能不同、以后可能调整。额度**每天早上 8 点重置**。按官方积分规则（输入 0.14 pts / 百万、输出 0.28、缓存读取 0.0028）折算，1 美元/天约合 **650 万 tokens**，10 美元档约 6500 万，命中 KV Cache 还能更多。限速：单 Key 30 RPM、单 IP 120 RPM、**单 Key 并发 8**、账户网关 20 RPM。查询：`curl "https://radeon-global.anruicloud.com/api/profile/model-usage?include_recent=true" -H "Authorization: Bearer rc-你的Key"`，看 `daily_cost_limit_usd` 与 `daily_cost_remaining_usd`。⚠️ **Daily budget 从早期的 10 美元调到 1 美元，这个信号值得警惕。** 两个短板：首字延迟实测约 **22 秒**、输出 **28–30 tok/s**，明显慢于官方付费接口；并发必须自己控队列并对 429 做退避。

🆕 **智谱「Flash × ZCode」夜间畅用：9/3–9/20，每晚 23:00–09:00 完全免费** —— 智谱 9/3 深夜宣布，GLM Coding Plan 推出夜间畅用活动：**每晚 23:00 至次日 09:00（北京时间 UTC+8，含周末及公共假日）**，付费套餐用户无需手动开启、系统自动生效。规则两条：① 通过官方编程工具 **ZCode** 调用 GLM-5.3-Flash，**额度消耗为 0，等于完全免费畅用**；② 通过套餐支持的其他 Agent 调用，**可用额度翻倍（×2）**。⚠️ 仅限 GLM-5.3-Flash，错峰时段选 GLM-5.3 仍按套餐标准规则扣；且**前提是 GLM Coding Plan 付费套餐用户**——这是给已付费用户的夜间加成，不是面向所有人的白嫖。GLM-5.3-Flash 规格：**320B 总参 / 18B 激活**，GLM-5 系列首个原生多模态（文本 / 图像 / 视频），**1M 上下文**，AA 智能指数 57 分（与 Claude Opus 4.8 持平），定价仅为 GLM-5.2 的 **1/10**（0.4 / 1.4 元每百万，半价至 9/9 24:00）。它此前的匿名身份是 `Ox Alpha`，揭晓后已跃居 OpenRouter 排行榜首位。

🆕 **商汤 Token Plan：把智谱旗舰 GLM-5.2 纳入免费公测** —— 入口 `sensenova.cn/token-plan`，Base URL `https://token.sensenova.cn/v1`，标准 OpenAI 兼容，手机号 + 实名认证后建 Key。额度是 **5 小时滚动刷新**——SenseNova 系列通常 1500 次 / 5 小时，DeepSeek 与 GLM-5.2 也有充足额度。和 AMD「每天一桶」相比，商汤是「每 5 小时一小桶」，**持续高强度使用时更抗造**。⚠️ 隐藏细节：控制台「当前窗口调用余量」页面**可能看不到 GLM-5.2 字样**（只显示 SenseNova 和 DeepSeek），但直接在模型列表里切 `glm-5.2` 是能成功调用的，底层已全量支持，只是前端展示低调。

✅ **B.AI 收缩已落地，但 4 款仍 100% 免费** —— 昨天预告的调整已于 **9 月 3 日 17:00（SGT）** 生效：`DeepSeek-V4-Flash` 与 `DeepSeek-V4-Flash-Vision-Exp` 结束免费档，转为对齐 DeepSeek 官方峰谷定价——工作日 09:00–12:00、14:00–18:00（SGT）高峰 **5 折**，其余工作日时段与整个周末 **7.5 折**。**GLM-5.3-Flash、Qwen3.8-Flash、腾讯 Hy3、小米 MiMo-V2.5 继续保持 100% 免费。** 平台同时披露了这次免费活动的量级：累计 Token 吞吐 **超 10.9 万亿**、**8956 万次 API 调用**、**23.9 万新注册用户**（其中 23.5 万是 API 开发者），单日吞吐一度破 1.33 万亿 Token。

🔎 **数据核对：OpenCode Zen 定价页 Free 行 6 → 7 款** —— 新增 `muse-spark-1.3-contributor-free`。定价页 7 款为：Big Pickle、MiMo-V2.5 Free、Ling 3.0 Flash Fin Free、Nemotron 3 Ultra Free、Nemotron 3.5 Lightning Free、Muse Spark 1.3 / 1.2 Contributor Free。接口 `/zen/v1/models` 实拉 66 款，共 **9 个免费 ID**（定价页 7 款 + 接口额外的 `deepseek-v4-flash-free`、`laguna-s-2.1-free`）。⚠️ **全部为「数据换免费」**，涉及客户代码只用后两个。

🔎 **数据校正：OpenRouter 免费池 21 款，与 9/3 快照零增减** —— 9/4 脚本清点 427 款模型中 **21 款** `prompt` 与 `completion` 同时为 0，与 9/3 存档快照一致。⚠️ 昨日日报正文记录的 **18 是当日盘中快照**，现已回补至 21。免费池在 18–21 之间来回波动，别把单一 ID 写死。

🏆 **量大能用的先进模型 Top 12（9/4）**：① GLM-5.3-Flash / Ox Alpha（B.AI / ZCode 夜间免费，96）；② DeepSeek-V4-Flash（🆕 AMD，284B MoE / 1M 上下文 / 国内直连免绑卡，94）；③ GLM-5.2（🆕 商汤 Token Plan，1M 无损上下文 / 5 小时滚动刷新，92）；④ Qwen3.8-Flash-Next（🆕 AMD，262K / 训练成本 -90% / 开源，91）；⑤ MiniMax M3（1M 上下文 / 943K 输出，**9/6 到期**，90）；⑥ Nemotron 3 Ultra 550B（NIM 唯一推荐，89）；⑦ Kimi K3（freellm 89 分 / 62.4 tok/s，88）；⑧ Muse Spark 1.3（Zen 新增免费 ID，87）；⑨ Hy3 腾讯混元（86）；⑩ Inkling / Inkling Small（1M 推理型，85）；⑪ MiMo V2.5 小米（84）；⑫ MiniCPM5-1B（🆕 AMD，1B 轻量 / 高频流水线，82）。

⏰ **本周到期红线**：**9/6（剩 2 天）** MiniMax × GMI Cloud 14 天不限量窗口结束，同日 Vercel AI Gateway `minimax/minimax-m3-free` 预计停用；**9/9 24:00** GLM-5.3-Flash 半价到期（0.4/1.4 → 0.8/2.8 元）；**9/10 23:59** 腾讯 Hy4 Preview 限免结束；**9/20** 智谱夜间畅用窗口结束；**9/24** 百度 Comate 限免第二弹；**9/30** 腾讯 Hy3 限免结束、火山方舟 Q3 普惠 500 万/天结束、Dots3-Note Preview `:free`（512K）下线。

⚠️ **风险提醒**：**AMD 的「免费」有每日预算上限且口径不一**——官方示例 $10/天，实测不少新账号只有 $1/天，Daily budget 从 10 美元调到 1 美元这个信号值得警惕，别照抄教程数字，自己拉 Usage API；**AMD 慢、NIM 更慢**——AMD 首字约 22 秒 / 28–30 tok/s，NIM 上 Kimi K3 62.4、Gemma 4 31B 50.9、DeepSeek V4 Flash 仅 27.3 tok/s（Groq 约 500），别把免费端点当主力链路；**智谱夜间免费是付费套餐的加成，不是白嫖**，且仅限 GLM-5.3-Flash；**GMI Cloud 的「免费」只有 4 个模型**，其余 80+ 全部返回 `402`；**免费午餐正在一张张收走**——美团 LongCat 2.0 免费已停，八月底是个分水岭；**火山方舟免费额度没有熔断开关**，超用直接出账单。

## 📰 今日摘要（2026-09-03）

⚠️ **今日最紧急：B.AI 免费阵容今晚收缩——DeepSeek-V4-Flash 双模型 9/3 17:00 SGT 退出免费档**：平台公告确认 `DeepSeek-V4-Flash` 与 `DeepSeek-V4-Flash-Vision-Exp` 结束免费，改为对齐 DeepSeek 官方峰谷定价——工作日 09:00–12:00、14:00–18:00（SGT）高峰 **5 折**，其余工作日时段与整个周末 **7.5 折**。**同一份公告明确：GLM-5.3-Flash、Qwen3.8-Flash、Hy3、MiMo V2.5 保持 100% 免费。** 挂在这两个模型上的批量任务或定时脚本，今天之内跑完或改路由。

🔎 **Ox Alpha 真身揭晓 = 智谱 GLM-5.3-Flash——当前免费档的能力天花板**：此前在 OpenRouter / OpenCode 匿名刷榜、**6 天狂揽 42 万亿 Token** 调用的神秘模型 `Ox Alpha`，官方确认就是 GLM-5.3-Flash。规格：**320B 总参 / 18B 激活**，GLM-5 系列**首个原生全模态模型**（文本 / 图像 / 视频），**1M 上下文**，稀疏 + 线性混合注意力（注意力计算量降 3 倍、KV 缓存需求降 4.4 倍），引入流形约束超连接（mHC），预训练 30T 多模态 Token，**MIT 协议开源**。AA 智能指数 57、官方口径与 Claude Opus 4.8 持平，Z.ai Code Bench 29.0（Opus 4.8 为 29.5）。最关键的一点：**全部推理流量由约 10 万卡国产 AI 芯片（华为 / 海光 / 摩尔线程）承载**。B.AI 上直接标注 **FREE & UNLIMITED**；BigModel 限时半价 0.4/1.4 元每百万 tokens（9/9 24:00 恢复 0.8/2.8）。

🆕 **Meta Muse Spark 1.3 今日发布，Zen 上免费 ID 同步上架**：已在 Muse Code 与 Meta Model API 上线，主打 agentic 与 coding。相比 1.2：**工具调用减少约 20%、token 消耗降低约 25%**，支持单线程内跑更长周期的多工作流任务，会主动追问澄清、卡住时上报、关键操作前确认。官方称成本 "almost too cheap to meter"，扎克伯格预告开放权重。OpenCode Zen 上 `muse-spark-1.3-contributor-free` 立即可用——⚠️ 但 Contributor 版明码标价是「授权用你的 prompt 与 completion 训练未来 Meta 模型」，且仅对 Meta 允许的地区开放。

🆕 **新平台发现：AIHubMix，56 款免费模型，$1 充值解锁永久日配额**：本期挖到的性价比最高的一站式免费网关。注册无需信用卡，**先送 10 次试用调用且永不过期**；一次性充值任意金额（最低 $1）后，**全部 56 款永久切换为日配额：100 请求/天 · 10 请求/分钟 · 1M tokens/天，每日重置**。三种协议全支持（Chat Completions / Messages / Responses），一个 Key 打通，Cursor / Cline / Cherry Studio / LiteLLM 改 base_url 即用。近 30 天真实跑量 **33.2B tokens / 265K 请求 / 56 款全部在用**，用量 Top4：coding-glm-5.3-free（28.2%）、coding-glm-5.3-flash-free（20.8%）、coding-glm-5.2-free（13.5%）、coding-kimi-k3-free（5.5%）。⚠️ 注意 1M tokens/天是 **56 款共用一个池子**，不是每款各 1M。

🆕 **华为云码道体验版套餐 9/1 正式上线：¥0 / 500 万 Tokens 月 / 50 席位**：个人试用无需付费、无需实名。与「码力续航计划」**每日 1000 万免费 tokens**（当日清零、次日满血重置，总池价值 100 万元发完即止）叠加，8/31 起福利模型池新增 GLM-5.3-Flash。⚠️ 硬限制：只能在码道 IDE / 插件 / CLI 内消费，**不可导出 API Key**。

🆕 **开源三连发，本地部署门槛降到 2–3 张高端卡**：**GLM-5.3 全量开源**——753B 参数、权重约 756GB，社区 1-bit GGUF 压到约 217GB；**Qwen3.8-Flash**——125B 总参 / 仅 6B 激活，Qwen4 架构先导，GDNQSA 混合注意力 + 51B N-gram Embedding 外挂记忆库，训练成本较前代**下降 90%**，1-bit GGUF 约 72.5GB（单张 RTX 6000 可装）；**腾讯 Hy4 Preview**——770B 总参 / 49B 激活，Apache 2.0，1-bit GGUF 约 229GB。

🆕 **两个零门槛免费端点（Qwen3.8-Flash-Next，FP8）**：① Empero 实验室 `https://free.empero.org/v1`，API Key 填 `free`，4×B200 集群、官方称无限 Token；② HuggingFace 公共端点 `https://pnywsahxhac1qjbo.us-east-2.aws.endpoints.huggingface.cloud/v1`，API Key 填 `none`，模型名 `Qwen/Qwen3.8-Flash-Next`，262K 上下文、支持视觉多模态与工具调用、实测 >100 tok/s。⚠️ 这类免费公共端点通常只存活几天，请勿压测。

📉 **OpenRouter 免费池收缩 21 → 18**：424 款模型中 prompt/completion 同时为 0 的 **18 款**，而 9/2 两轮清点均为 21 款，3 天内**净减 3 款**。1M 上下文档位仍在：inkling、inkling-small、minimax-m3、nemotron-3.5-lightning、nemotron-3-ultra-550b。未充值账户仅 50 请求/天。

🏆 **量大能用的先进模型 Top 12（9/3）**：① GLM-5.3-Flash / Ox Alpha（B.AI，96）；② Muse Spark 1.3（Meta / Zen，95）；③ MiniMax M3（1M 上下文 / 943K 输出，9/6 到期，93）；④ Qwen3.8-Flash（125B-A6B，92）；⑤ GLM-5.3（BigModel 限时免费，91）；⑥ DeepSeek-V4-Pro / V4-Flash（华为码道每日 1000 万，90）；⑦ Nemotron 3 Ultra 550B（89）；⑧ Kimi K3（1.05M 上下文，88）；⑨ Hy3 腾讯混元（87）；⑩ MiMo V2.5 小米（86）；⑪ Inkling / Inkling Small（1M 推理型，85）；⑫ Gemini 3.8 Flash（四模态 1M，84）。

⏰ **本周到期红线**：**9/3 17:00 SGT（今天）** B.AI 的 DeepSeek-V4-Flash 与 V4-Flash-Vision-Exp 退出免费档；**9/6** MiniMax × GMI Cloud 14 天不限量窗口结束（M3 / M2.7 / Speech 2.8 / Music 3.0），同日 Vercel AI Gateway `minimax/minimax-m3-free` 预计停用；**9/9 24:00** GLM-5.3-Flash 半价到期（$0.075/$0.25 → $0.15/$0.50）；**9/10 23:59** 腾讯 Hy4 Preview 限免结束；**9/30** 火山方舟 Q3 普惠 500 万/天结束、腾讯 Hy3 限免结束、Dots3-Note Preview `:free`（512K）下线。

⚠️ **风险提醒**：**GMI Cloud 的「免费」只有 4 个模型**——零余额下其余 80+ 模型（含 GLM-5.3-Flash、GPT-5.5、DeepSeek、Kimi K3）全部返回 `402 Insufficient balance`，图像生成与 MiniMax-H3 也不在免费范围，网上「80+ 模型免费」是误读；**四家老牌免费层已确认失效**——GitHub Models 7/30 退役返回 HTTP 410、Cerebras 8 月起需绑卡（$5 / 30 天）、SambaNova 与 Together AI 返回 `PAYMENT_METHOD_REQUIRED`；**火山方舟免费额度没有熔断开关**，超用直接按量出账单，务必自设 Token 熔断（网传「9 月免费额度已结束」经核实是误传）；**Zen 的 8 个免费 ID 全部是「数据换免费」**，涉及客户代码只用 `laguna-s-2.1-free` 或 `deepseek-v4-flash-free`。

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
