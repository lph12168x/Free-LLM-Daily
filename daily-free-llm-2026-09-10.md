# 免费大模型日报 · 2026-09-10（周四）

> 聚焦「量大能用的先进模型」· 覆盖 40+ 国内外平台 · [在线阅读 HTML 版](./daily-free-llm-2026-09-10.html)

## 📌 本期焦点

1. **🆕 头号新闻：DeepSeek V4.1 Flash 今日正式发布，V4 Pro 流量自动按 Flash 价计费** —— DeepSeek 官网今日（9/10）公告：**V4.1 Flash 计划于北京时间 9 月 10 日前后正式发布**，官方称「经内部、外部多方测试，**V4.1 Flash 在性能、费用、速度、总用时等各项指标上已全面超越 V4 Pro**」。更关键的一句：**V4.1 Flash 上线后、V4.1 Pro 上线前，DeepSeek 会把对 V4 Pro 的请求全部路由到 V4.1 Flash，并按 V4.1 Flash 单价计费**——不用改一行业务代码，原本按 Pro 价付费的流量自动按更便宜的 Flash 价结算，等于一次隐形的全员降价。内测实测：全新模型结构、**原生多模态**、平均输出超 300 tokens/s、**峰值 507 tokens/s**，视觉 Agent Benchmark 接近 Claude Opus 4.8。⚠️ 生产上线前请自行复现长上下文、工具调用与峰值成本。

2. **💰 DeepSeek flash 系列今日 12:00 起降价，缓存命中最高降 60%** —— 闲时（每百万 Token）：输入缓存命中 **0.05 → 0.02 元（-60%）**、缓存未命中 **1.5 → 1 元（-33%）**、输出 **4.5 → 4 元（-11%）**；高峰时段为闲时 2 倍（0.04 / 2 / 8 元），适用 `deepseek-v4-flash` 与 `deepseek-v4-flash-vision-exp`。峰谷时段：工作日 9:00–12:00、14:00–18:00 为高峰，周六周日全天低谷价。开发者按自身 Agent 工作流估算综合成本**可能下降约 40%**。⚠️ 这次是「部分回调」而非回到 8 月涨价前：输出价仍是涨价前（2 元）的两倍。

3. **⏰ 腾讯混元 Hy4 preview 限免今晚 23:59 截止，9/11 起转新规则** —— 腾讯 WorkBuddy 9/9 官宣：Hy4 preview（**770B 总参 / 49B 激活**）限免将于 **9 月 10 日 23:59 结束**。9/11–10/10 规则：**已体验过的老用户仅闲时夜间 23:00–次日 8:00 免费**；新用户及此前未体验过的老用户，**10 月 10 日 23:59 前首次开启，从首开当天起往后 14 天有每日免费额度**。**Hy3 免费期延至 9 月 30 日**，无缝衔接。⚠️ 限免是 WorkBuddy / CodeBuddy 客户端内的额度，**不等于 API 免费**，不可用于自动化脚本；生图 / 视频会切多模态模型并按正常规则扣积分。OpenRouter 30 日榜：Hy3 以 29.9T token 排第 3（+77%）、Hy4 preview 24.5T 排第 6。

4. **⏰ B.AI 延长 GLM-5.3-Flash 免费至 9/12 09:59 SGT** —— Z.ai 官方 5 折已在 9/9 24:00 到期（`$0.075/$0.25` 恢复 `$0.15/$0.50`），但 **B.AI 宣布把 GLM-5.3-Flash 的零成本窗口延长到 9 月 12 日 09:59（SGT）**。GLM-5.3-Flash：**320B 总参 / 18B 激活** MoE、**1M 上下文**、MIT 许可，B.AI 平台上用量最高的模型。**Qwen3.8 Flash、Hy3、MiMo V2.5 在 B.AI 上继续 100% 免费**。其他零成本通道：OrcaRouter 免费档（1M）、智谱 ZCode 夜间 23:00–09:00 额度归零（至 9/20，限付费套餐）、Merge Gateway 1 折至 9/30（$0.012/$0.04）、开源权重自部署（Apple M5 Mac Studio 实测约 45 tok/s）。⚠️ 平台补贴非 Z.ai 官方条款，务必留备选。

5. **🆕 蚂蚁开源 Ling-3.0-flash-VL：124B-A5.5B 原生多模态，Apache 2.0 可商用** —— 蚂蚁 9/9 发布并开源百灵系列首个**原生多模态**模型：总参 124B、单次激活约 5.5B，**原生支持图像 / 文本 / 视频输入**，上下文 256K，**Hugging Face 与 ModelScope 已上线 Apache 2.0 权重，可直接商用**。核心机制「视觉反馈闭环」：观察 → 行动 → 验证 → 修正，官方称加入视觉后文本智能反而提升（AA v4.1.1 +4 分），Image-to-WebDev Arena 得分高于 GPT-5.4。免费通道：Ling Studio 免费体验；同系列 `inclusionai/ling-3.0-flash-fin:free` 与 `ling-3.0-flash-sante:free` 在 OpenRouter 免费池、`ling-3.0-flash-fin-free` 在 Zen 免费档。

6. **🆕 面壁开源 MiniCPM5-2B：2B 参数拿下 AA 4B 以下第一** —— 9/8 发布，Artificial Analysis 综合指数 **23 分位列 4B 以下开源第一**，**Agentic Index 达 20 分**（同级普遍低于 10），同步开源训练配方与 RL 框架 Meshy，面向手机 / PC / 车机本地部署。

7. **🎬 SkyProduction 限免第二期：MiniMax H3 768P 免费用至 9/14** —— 天工工作台 9/9–9/14 开放 MiniMax H3 768P 限时免费：9/9 当天新老会员用指定 H3 生成视频**不消耗积分**；9/10–9/14 转为「首开会员按档位赠限免天数 + 老会员买积分赠天数」。⚠️ 这是视频生成模型不是 LLM，纯白嫖只有 9/9 一天。

8. **📉 阿里云百炼免费额度集中到期：9/14 与 9/15 两批** —— **kimi-k2.7-code 与 qwen3.5-ocr 9/14 到期**、**glm-5.2 9/15 到期**（qwen3.7-plus 已于 9/1、qwen3.7-max-2026-06-08 已于 9/8 到期）。手头有额度的这两天优先烧掉。免费 Token 仅限中国内地节点。

9. **📊 OpenRouter 用量榜：国产模型占据前列，免费档 Nemotron 3 Ultra 排第 9** —— 30 日 token 榜前 10：DeepSeek V4 Flash 0731（50.7T，+400%）、GPT-5.6 Luna（35.5T）、**Hy3（29.9T，+77%）**、MiMo-V2.5（27.3T）、Ox Alpha（27.2T）、**Hy4 preview（24.5T）**、**GLM 5.3 Flash（22.2T）**、DeepSeek V4 Flash 0423（22T）、**Nemotron 3 Ultra（free，16.9T，+49%）**、GLM 5.2（13.8T）。应用侧 **Hermes Agent（Nous Research）以 11.4T 排第一**，压过 Claude Code（5.19T）。Nous 的 Hermes Agent v0.21.0 是 MIT 开源 agent runtime，官方教程即「指向 OpenRouter 免费模型跑」：硬性要求 **tool calling + 上下文 ≥ 64K**，当前 18 款免费模型里 17 款支持工具调用；限制在请求数不在 token——免费档 20 RPM / 50 RPD，累计充值过 $10 后升 1000 RPD。

10. **🔎 平台盘点快照** —— **OpenRouter**：430 款中 **18 款 `:free`**（与 9/9 零增减）。分布：NVIDIA 5、Google 2、nex-agi 2、inclusionAI 2、poolside 2、Thinking Machines 2、cohere 1、dots-studio 1、liquid 1；**1M 上下文的有 4 款**（nemotron-3-ultra-550b-a55b、nemotron-3.5-lightning、inkling、inkling-small）。**OpenCode Zen**：70 款、**7 个 `-free` ID**（deepseek-v4-flash-free、mimo-v2.5-free、ling-3.0-flash-fin-free、nemotron-3-ultra-free、nemotron-3.5-lightning-free、muse-spark-1.3/1.2-contributor-free），官方定价页 Free 行 6 款（多一个 stealth 模型 `big-pickle`），零增减。**freellm.net**：453+ 增至 **475+ 模型 / 31 家平台 / 321 款免信用卡**，239 款经实时核验；核验榜榜首 **Ollama Cloud deepseek-v4-pro（95 分）**，其后 deepseek-v4-flash 94、NVIDIA NIM deepseek-v4-pro-0813 93、**Kimi K3 92**。

---

## 🎯 今日可用通道清单（量大且先进）

| 平台 / 通道 | 可白嫖的先进模型 | 额度与限制 | 状态 |
|------------|----------------|-----------|------|
| **NVIDIA NIM**（build.nvidia.com） | DeepSeek V4 Flash 0731（1.3M）、**Kimi K3**（1M）、DeepSeek V4 Pro、MiniMax M3、GLM-5.2、Nemotron 3 Ultra、Qwen3-Coder 480B 等 **99 款 $0** | 最高 40 RPM，TPD 不设上限；+86 手机号可验证，无需信用卡 | ✅ 长期稳定 |
| **Ollama Cloud** | deepseek-v4-pro（1M，核验 95 分）、deepseek-v4-flash、Kimi K3、GLM-5.3/5.3-Flash、MiniMax M3 | 1 实例 / 5 小时会话 / 7 天周额度；GPT-OSS 120B 免费档实测 317 tok/s | ✅ 榜首 |
| **B.AI** | **GLM-5.3-Flash**（320B-A18B / 1M）、Qwen3.8 Flash、Hy3、MiMo V2.5 | GLM-5.3-Flash 免费至 **9/12 09:59 SGT**；其余 3 款 100% 免费 | ⚠️ 2 天后到期 |
| **WorkBuddy / CodeBuddy** | Hy4 preview（770B-A49B）、Hy3 | Hy4 限免**今晚 23:59 结束**；之后老用户仅 23:00–08:00 / 新用户 14 天；Hy3 至 9/30 | 🔴 今日截止 |
| **OpenCode Zen** | 7 个 `-free` ID：DeepSeek V4 Flash、MiMo-V2.5、Ling 3.0 Flash Fin、Nemotron 3 Ultra / 3.5 Lightning、Muse Spark 1.3/1.2 | 30 RPM / 500 RPD / 100 万 TPD；免费期数据可用于改进模型 | ✅ 零增减 |
| **OpenRouter `:free`** | 18 款：nemotron-3-ultra-550b-a55b（1M）、inkling（1M）、nemotron-3.5-lightning（1M）、nex-n2.5-pro/mini、ling-3.0-flash-fin/sante、gemma-4-31b、north-mini-code 等 | 20 RPM / 50 RPD；累计充值 $10 后升 1000 RPD | ✅ 18 款 |
| **Google AI Studio** | Gemini 3.8/3.7/3.6/3.5 Flash（均 1M）、Gemma 4 31B/26B | 15 RPM、1,500 RPD；无需信用卡；免费档数据可能用于产品改进 | ✅ 长期稳定 |
| **商汤 Token Plan**（token.sensenova.cn） | Kimi K3、DeepSeek V4 Pro/Flash、GLM-5.2/5.3/5.3-Flash、MiniMax M3、Qwen3.8 Max 等 **20 款** | Free 档 ¥0/月：**6 万积分 / 5 小时滚动 + 60 万 / 周**，不绑卡 | ✅ 国内直连 |
| **智谱 ZCode / BigModel** | GLM-5.3-Flash、GLM-4.7-Flash（200K）等 8 款 | ZCode 夜间 **23:00–09:00 额度消耗 0**（至 9/20，限付费套餐） | ⚠️ 限时 |
| **ModelScope / HF Router** | DeepSeek V4 Pro/Flash、Kimi K3/K2.6/K2.7-Code、Qwen3-Coder-Next、GLM-5.2 | ModelScope 100–200 RPD；HF Router 免费账户 $0.10/月额度 | ✅ 稳定 |
| **阿里云百炼** | kimi-k2.7-code、qwen3.5-ocr、glm-5.2 等（每模型 100 万 tokens） | **9/14 与 9/15 集中到期**；限中国内地节点 | 🔴 即将到期 |
| **DeepSeek 官方** | V4 Pro（1M）、V4 Flash（1M，今日起降价） | **付费**：闲时缓存命中 0.02 元 / 未命中 1 元 / 输出 4 元；网页端 chat.deepseek.com 免费无公开上限 | ⚠️ 降价但付费 |

**组合建议**：主力用 NVIDIA NIM 的 DeepSeek V4 Flash / Kimi K3（40 RPM、TPD 不限、免信用卡）；长上下文与国产需求挂商汤 Token Plan（5 小时一刷、20 款旗舰同池）；夜间大任务走 WorkBuddy Hy3 至 9/30 或智谱 ZCode 23:00–09:00；自建智能体用 Hermes Agent + OpenRouter 17 款支持工具调用的免费模型。

---

## 📅 到期与风险日历

- **今天 9/10**：`23:59` 腾讯 **Hy4 preview** 限免结束（之后转夜间 + 新用户 14 天规则）；`12:00` DeepSeek flash 系列降价生效；**今日前后** DeepSeek **V4.1 Flash** 正式发布。
- **本周内**：`9/12 09:59 SGT` B.AI **GLM-5.3-Flash** 免费窗口结束；`9/14` 阿里云百炼 **kimi-k2.7-code / qwen3.5-ocr** 到期；`9/14` SkyProduction MiniMax H3 限免活动结束；`9/15` 百炼 **glm-5.2** 到期。
- **9 月下旬**：`9/18` Zen GPT-5.6 Sol 5 折到期；`9/20` 智谱 ZCode 夜间畅用结束；`9/30` 腾讯 **Hy3** 免费期结束、Merge Gateway GLM-5.3-Flash 1 折结束。

---

## 🧭 今天该怎么动

1. **现在就做**：把 Hy4 preview 的大任务挪到今晚 23:59 前跑完，或改到 23:00–08:00 夜间窗口；未体验过 Hy4 的账号可以攒到 10/10 前再首开，白拿 14 天每日额度。
2. **今天之内**：走 B.AI 的立刻准备一条备选通道（Qwen3.8 Flash 同平台免费，或 NVIDIA NIM 的 DeepSeek V4 Flash）；走 DeepSeek 官方 API 的确认业务已切闲时并打开缓存命中策略——这次 60% 的降幅主要吃在缓存上。
3. **本周之内**：烧掉阿里云百炼 9/14、9/15 到期的额度；把 Hermes Agent 指向 OpenRouter 免费模型试跑一次，验证 tool calling + 64K 上下文两条硬门槛。

---

*数据来源：OpenRouter `/api/v1/models` 与 `/rankings`（9/10 脚本清点）· OpenCode Zen `/zen/v1/models` 与官方定价页 · DeepSeek 开放平台公告 · TechWeb / 凤凰网科技 / 新浪科技 · KuCoin / ChainCatcher · 腾讯新闻 AI 行业日报 · 网易 / 今日头条 · freellm.net 核验榜 · llmpricing.dev · pinggy.io · ollamatps.com。*

*⚠️ 免费额度可能随时调整，请以各平台官网最新政策为准。OpenRouter 免费池日内波动，18 款为脚本清点时刻快照。B.AI「继续免费」为平台补贴承诺、非 Z.ai 官方条款。WorkBuddy 的 Hy4/Hy3 限免是客户端额度而非 API 免费。*

*[© lph12168x/Free-LLM-Daily](https://github.com/lph12168x/Free-LLM-Daily) · 🤖 由 WorkBuddy 自动化生成 · 2026-09-10*
