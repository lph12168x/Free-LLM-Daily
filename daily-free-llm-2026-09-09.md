# 免费大模型日报 · 2026-09-09

> 每日自动更新 · 覆盖 30+ 国内外平台 · 永久免费 / 大额免费 / 限时活动 / 零成本组合方案

📅 **2026 年 9 月 9 日 · 周三**

## 今日头条 · 三条主线

### 🆕 蚂蚁开源 Ling-3.0-flash-VL：原生多模态 + 视觉反馈闭环，今日头条 #1

蚂蚁集团今日（9/9）正式发布并开源百灵系列首个原生多模态模型 **`Ling-3.0-flash-VL`**：**124B 总参 / 5.5B 激活** 的 MoE、**256K 上下文**、原生支持图像 / 文本 / 视频输入，核心创新是「**观察 → 行动 → 验证 → 修正**」的视觉反馈闭环 —— 不再是「看图一次出结果」，而是能拿渲染结果对比自我修正。

- **技术亮点**：任意分辨率视觉编码器 + VideoRoPE；语言主干 42 层混合架构（KDA 与 Gated MLA 按 5:1 交替）。
- **跑分**：Artificial Analysis 智能指数 v4.1.1 比纯文本版 +4 分；**Image-to-WebDev Arena 官方评测得分高于 GPT-5.4**（代号 linthium）；医疗报告解读支持跨文档数据整合与风险标识。
- **怎么白嫖**：① **Ling Studio 已上线并免费体验**；② **BF16 / FP8 权重已开源**到 Hugging Face 与 ModelScope（FP4 / INT4 待发布）。
- **为什么值得关注**：Ling 文本版 `inclusionai/ling-3.0-flash-fin:free` / `ling-3.0-flash-sante:free` 已在 OpenRouter 免费池；VL 版开源后大概率补齐到同一批通道。

⚠️ 目前「免费」= Ling Studio 体验 + 开源权重自部署；API 免费档还要等上架。

### ⏰ GLM-5.3-Flash 官方 5 折今晚 24:00 到期，但 B.AI 承诺继续零成本

两个方向相反的消息撞在同一天。**Z.ai 官方发布期 5 折今晚 24:00（UTC+8）结束**：`$0.075/$0.25` 恢复 `$0.15/$0.50`。但 **B.AI 于 9/8 明确公告：折扣到期后仍向全球开发者零成本提供 GLM-5.3-Flash**，用户习惯不受上游调价影响。

- **分量**：GLM-5.3-Flash 是 B.AI 平台上用量最大的模型 —— 320B 总参 / 18B 激活、1M 上下文、MIT 许可。
- **涨价后的账**：即便回到原价，仍是同智能档位最便宜的选择；**Merge Gateway 1 折（$0.012/$0.04，至 9/30）反而成了更便宜的口子**。
- **免费路径清点**：① B.AI 100% 免费；② OrcaRouter 免费档（1M 上下文）；③ 智谱 ZCode 夜间 23:00–09:00 额度归零（至 9/20）；④ 华为码道 / 商汤 Token Plan 国内直连；⑤ 开源权重自部署。
- **动作建议**：走 B.AI 什么都不用改；走官方 API 的今晚前锁量或改走 Merge 1 折。

⚠️ B.AI 的「继续免费」属平台补贴承诺，**不是 Z.ai 官方条款**，务必留备选通道。

### 🇨🇳 商汤 SenseNova Token Plan 升级：6 万积分 / 5 小时，20 款模型进通用积分池

商汤日日新 Token Plan 公测档完成一轮扩容，**Free 档 ¥0/月、6 万积分 / 5 小时滚动刷新 + 60 万积分 / 周**，不绑卡、不充值，一个账号最多 20 个 API Key。

- **Free 档原生模型**：`sensenova-6.8-flash-lite`（轻量多模态智能体：图像理解 / OCR / 图表）、`sensenova-u1-fast`（图文生成、信息图 / PPT）、新增 `sensenova-u1.5-lite`（新一代图片创作，生成编辑一体、支持参考图）。
- **通用积分池可跑**：**Kimi K3**（1M）、**DeepSeek V4 Pro/Flash**、**GLM-5.2/5.3**、**MiniMax M3**（1M）、**Qwen3.8 Max**、Kimi K2.7 Code、GLM-5.1、MiniMax M2.5/2.7 等共 **20 款**。
- **接入方式**：Base URL 换 `https://token.sensenova.cn/v1`，模型名填对应 ID（如 `kimi-k3`）。
- **为什么是今日头条**：国内直连通道里**「先进模型覆盖最全 + 滚动额度最大」**的一条 —— Kimi K3、GLM-5.3、MiniMax M3 这三款旗舰同池，5 小时一刷，无需申请评审。

⚠️ Free 档为「限时放量」公测，付费 Lite / Pro 档即将上线，免费额度可能收缩。

## 其他重点动态

- **Inception Mercury 2.5 上线 OpenRouter**（9/8）：扩散式 LLM、并行生成 token、260K 上下文、$0.04 / 1M 输入；新号送 1 亿 tokens 一次性额度（Mercury 2）。
- **NVIDIA 以 129.3 亿美元收购 Hugging Face**（9/9 官宣）：承诺平台保持开放、不强制 NVIDIA 算力；关注 HF Router $0.10/月免费额度与开源权重分发走向。
- **星火 X2.5-4B 登顶 HF Trending 第一**（9/9）：端侧唯一 1M 上下文、Apache-2.0 免费商用、昇腾全流程训练；星辰 MaaS 限时免费。
- **Meta Muse 个人 Agent 上线**（9/8）：主打订餐 / 购物代办；需开放大量个人数据权限，隐私争议较大。
- **OpenRouter 免费池 18**（NVIDIA 5 / Google 4 / inclusionAI 2 / nex-agi 2 / poolside 2 / Thinking Machines 2 / cohere 1 / dots-studio 1 / liquid 1），较昨日净增 2 款 Nex-N2.5 Mini / Pro。
- **OpenCode Zen 70 款 / 8 个 `-free` ID**，连续三日零增减。
- **freellm.net 核验榜 Kimi K3 92 分继续登顶**（453+ 模型 / 31 家平台 / 291 款免信用卡）。

## 量大能用的先进模型 · Top 12

1. **GLM-5.3-Flash**（95）—— B.AI 继续免费 + Merge 1 折 + OrcaRouter + 智谱 ZCode 夜间 + 商汤 Token Plan，320B-A18B、1M、MIT。
2. **Kimi K3**（93）—— NVIDIA NIM 免费 + 商汤 Token Plan 通用池 + 阿里云百炼，~2.8T-A104B、1M。
3. **Ling-3.0-flash-VL**（91）—— 蚂蚁今日开源 + Ling Studio 免费体验，124B-A5.5B、256K、图文视频。
4. **DeepSeek-V4-Flash**（89）—— NVIDIA NIM / 商汤 / AMD Radeon / OrcaRouter / Zen 六通道，284B-A13B、1M。
5. **Nex-N2.5 Mini / Pro**（88）—— 今日新免费，262K、agentic coding、工具调用。
6. **Gemini 3.8 Flash**（88）—— Google AI Studio 永久免费，1M、全模态。
7. **Qwen3.8-Flash / 27B**（87）—— B.AI 100% 免费 + ModelScope 88 分 + 商汤 Qwen3.8 Max。
8. **Nemotron 3.5 Lightning 30B-A3B**（86）—— Merge $0 + OpenRouter :free + Zen 三通道，1M。
9. **MiniMax M3**（85）—— OpenRouter 已下架；Ollama Cloud + NVIDIA NIM + 商汤 Token Plan 三通道。
10. **Nemotron 3 Ultra 550B-A55B**（84）—— OpenRouter :free + Zen，1M，周吞吐 3.64T。
11. **星火 X2.5-4B**（82）—— HF Trending 第一，端侧 1M，Apache-2.0，昇腾。
12. **Thinking Machines Inkling**（80）—— OpenRouter :free，1M 上下文，开放权重多模态 MoE。

## 到期红线（按时间排序）

- **9/9 24:00（今晚）** Z.ai 官方 GLM-5.3-Flash 5 折结束（$0.075/$0.25 → $0.15/$0.50）—— 走 B.AI 不用动；走官方 API 的改 Merge Gateway 1 折。
- **9/10 前后** 腾讯 Hy4 preview 两周免费试用到期。
- **9/14** 阿里云百炼 `kimi-k2.7-code` 100 万 tokens 到期。
- **9/15** 阿里云百炼 `glm-5.2` 100 万 tokens 到期。
- **9/18** OpenCode Zen GPT-5.6 Sol 5 折结束。
- **9/20** 智谱 ZCode 夜间畅用结束。
- **9/30** Merge Gateway 1 折到期 + 腾讯 Hy3 国内通道限免。
- **已过期**：阿里云百炼 `qwen3.7-plus`（9/1）、`qwen3.7-max-2026-06-08`（9/8）；MiniMax × GMI Cloud（9/6）；OpenRouter MiniMax 免费版（9/8）。

## 风险提醒

1. **「平台补贴的免费」不等于「官方的免费」**：B.AI「继续零成本」是它自己贴钱吸收上游成本波动；主力模型务必再留一条不同厂商的通道。
2. **新模型免费期「不说什么时候结束」**：Nex-N2.5 Mini / Pro 今天以 $0 上架 OpenRouter，官方既没公布免费期结束时间，也没给后续定价。想评测就现在，别写进生产依赖。
3. **官方口径与 API 口径不一致时，以 API 为准但要打折看**：Zen API 返回 8 个 `-free` ID，官方定价页只列 6 款；第三方聚合站（llmpricing.dev 等）免费清单普遍滞后甚至虚高。
4. **免费不等于零风险**：① NVIDIA 免费端点注明「勿提交机密数据」；② Muse Spark Contributor 版以免费换训练授权；③ Meta Muse Agent 需开放大量个人数据；④ Zen / Google AI Studio 免费档可能收集 prompt 用于产品改进。商业机密数据一律走付费或本地权重。
5. **NVIDIA 收购 Hugging Face：开源权重的分发层换了东家**：129.3 亿美元买下的是整个开放权重生态的分发入口；建议重要权重在本地或 ModelScope 留一份镜像。
6. **别信「兑换码」**：主流厂从未发过通用 CDKey。

## 按场景选路

- **日常编码 / 主力链路**：B.AI 的 GLM-5.3-Flash（继续零成本）→ Merge 1 折（$0.012/$0.04）→ Nex-N2.5 Mini/Pro（OpenRouter 免费）。
- **长上下文 / 研究型任务**：Kimi K3（NIM / 商汤）→ Nemotron 3.5 Lightning（Merge $0）→ Thinking Machines Inkling（1M）。
- **Agent / 长程任务**：Nex-N2.5 Pro、Poolside Laguna S 2.1、GLM-5.3-Flash、DeepSeek-V4-Flash。
- **多模态 / 图文生成**：Ling-3.0-flash-VL（今日开源）、Gemini 3.8 Flash（永久免费）、SenseNova U1 Fast / U1.5 Lite（商汤 5 小时 1500 次）、MiniMax M3。
- **国内直连 / 免代理**：商汤 Token Plan（升级 6 万积分/5h）→ 华为云码道 → AMD Radeon Cloud → 阿里云百炼（注意 9/14、9/15 到期）。
- **端侧 / 离线部署**：星火 X2.5-4B（HF Trending 第一）、Qwen3.8-Flash（量化后单张 RTX 6000 可装）、Ling-3.0-flash-VL（FP4/INT4 待发布）。
- **零配置 / 临时起意**：Pollinations（免 Key，URL 直拼）→ OpenRouter `openrouter/free` → OrcaRouter `orcarouter/free`。

## 数据核对方法

- OpenRouter `/api/v1/models`（9/9 脚本清点，431 款中 18 款 `:free` 且 `prompt` 为 0；与 9/8 存档 `or_models_0908.json` 逐 ID 求差集，换入 Nex-N2.5 Mini/Pro 2 款、换出 0 款）
- OpenCode Zen `/zen/v1/models`（70 款，8 个 `-free` ID，与 9/8 零增减）+ 官方定价页
- IT 之家 / DoNews 9/9（蚂蚁 Ling-3.0-flash-VL 开源）
- KuCoin / ChainCatcher / Odaily 9/8（B.AI 继续免费提供 GLM-5.3-Flash）
- DEV Community 9/8（GLM-5.3-Flash 5 折到期与 9 月价格战全景）
- 商汤官方文档 / 控制台（Token Plan 积分规则、模型 ID、base_url）+ llmpricing.dev 20 款模型价目
- myaiguide 9/8 日报（Nex-N2.5 + Inception Mercury 2.5）
- freetokens.custats.info（Inception 100M 免费 tokens）
- aitoolsrecap 9/9（NVIDIA × HF 收购）
- 雪球 / 科大讯飞 9/9（星火 X2.5-4B 登顶 HF Trending）
- freellm.net 9/5–9/7 核验榜
- 什么值得买 9/3 / 9/6（国内免费权益清单）

---

© [lph12168x/Free-LLM-Daily](https://github.com/lph12168x/Free-LLM-Daily) · 🤖 由 WorkBuddy 自动化生成 · 2026-09-09
