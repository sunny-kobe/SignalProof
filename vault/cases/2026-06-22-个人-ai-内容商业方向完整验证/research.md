---
type: research
status: completed
updated_at: 2026-06-22
gate: medium
---

# 研究

## 要回答的问题

- 个人 AI 内容商业项目第一阶段到底应该做什么方向？
- “中文 AI coding / 独立开发者”是否应该成为唯一定位？
- 哪些方向只是流量热，无法沉淀可复利资产？
- 哪个方向最适合用 SignalProof + Codex + HyperFrames / html-video 做 7 天到 30 天验证？

## 已确认事实

- 用户已明确删除“AI coding 工作流诊断/搭建服务”作为默认商业方向。
- 当前商业项目默认属于 AI 内容商业化：用 HyperFrames / html-video 作为内部生产引擎，把海外 AI / 编程 / Agent / GitHub / 工作流信号转成中文图文、短视频、公众号笔记和资料包。
- 用户修正了初始假设：不能预设为“面向中文 AI coding / 独立开发者，用海外 AI 编程项目实测内容”。
- 本 case 是 full case，需要覆盖研究、反方、判断、验证计划、产物、反馈、决策、资产、流程自检和工具账本。

## 调研过程

- 读取本仓库 `AGENTS.md`、repo `signalproof` skill、`docs/protocol.md`、`docs/research-quality-gate.md`、模板和前序 lite case。
- 读取 `ai-content-commerce` 和 `personal-opportunity-os` skill，确认方向边界：账号验证优先，SaaS 后置，HyperFrames / html-video 只是生产引擎。
- 运行 `python3.14 /Users/rust/.agents/skills/last30days/scripts/last30days.py --diagnose`，确认可用来源包括 Reddit、TikTok、Instagram、X、YouTube、HN、Polymarket、GitHub、Perplexity、Threads；X backend 为 `xurl`，但实际检索返回 `CreditsDepleted`。
- 运行近 30 天 query 1：`AI content creators workflow monetization`，保存原始结果到 `vault/runs/2026-06-22-content-commerce-direction/ai-content-creators-workflow-monetization-raw-content-workflow.md`。
- 运行近 30 天 query 2：`AI search visibility GEO content marketing`，保存原始结果到 `vault/runs/2026-06-22-content-commerce-direction/ai-search-visibility-geo-content-marketing-raw-ai-search-geo.md`。
- 使用 web 搜索补充中国 AI 应用、creator economy、B2B content marketing、developer AI trust、AIGC 标识和 GenAI consumer apps 等外部资料。

## 来源覆盖表

| 来源类型 | 候选能力 | 当前状态 | 结果质量 | 缺口 |
| --- | --- | --- | --- | --- |
| 公开讨论 | last30days / Reddit / X / YouTube / TikTok / Instagram / HN | 已覆盖部分 | medium | Reddit 有目标讨论，X 因 credits depleted 缺失，TikTok/Instagram/Threads/HN 本轮有效命中少，YouTube 评论 402。 |
| 项目和数据 | GitHub / QuestMobile / Stack Overflow / a16z / IAB / CMI | 已覆盖 | medium | 能证明趋势和工作流痛点，但不能证明用户自己的账号会成功。 |
| 官方和一手资料 | 网信办 / 平台规则 / 官方报告 | 已覆盖部分 | medium | 已覆盖国家级 AIGC 标识要求，平台细则仍需在发布前逐平台复核。 |
| 反证和替代方案 | Reddit / HN / AI slop 讨论 / 竞品和替代内容形态 | 已覆盖 | medium | 反证足以阻止泛 AI 内容工厂和直接 SaaS，但不足以判定方向失败。 |

## 交叉验证

- 谁在说：近 30 天有效讨论主要来自 r/content_marketing、r/marketing、r/NewTubers、r/ChatGPT、r/ArtificialInteligence，以及 GitHub issues；这些人群覆盖内容营销者、创作者、AI 用户和工具开发者。
- 说什么：讨论集中在 AI visibility reports 怎么转成实际工作、AI detection reports 进入内容交付、Google/AI 搜索改变流量入口、AI summarization 对内容创作者的破坏、AI slop 造成信任问题。
- 在哪里说：近 30 天结果保存在 `vault/runs/2026-06-22-content-commerce-direction/`；公开 web 来源覆盖 QuestMobile、CMI、IAB、Stack Overflow、a16z、网信办。
- 有没有反证：有。泛 AI 工具测评和 AI 批量内容竞争拥挤，AI slop 降低信任；YouTube/短视频“AI 自动赚钱”叙事存在高噪音；GEO/AEO 是热词，但很多内容已经被工具商和 agency 抢占。
- 能支持什么结论：支持“收窄后做低成本公开/半公开实验”；不支持“需求已验证”“可以产品化”“可以做 SaaS”。

## 关键证据

1. 中国 AI 应用进入大规模使用阶段。QuestMobile 2026 Q1 报告显示，中国 AI 原生 App 月活用户规模达到 4.4 亿，豆包、千问、DeepSeek 月活分别达到 3.45 亿、1.66 亿和 1.27 亿。这个证据支持“AI 信息入口和 AI 工具使用已是大众级变化”，但不直接证明你的内容账号会成功。来源：https://www.questmobile.com.cn/research/report/2046482337382842370/

2. AI 应用的强场景不只在开发者。QuestMobile 2025 报告把创作设计、综合助手、效率办公列为较高占比方向，并指出这些场景需求明确、变现路径相对清晰。推断：只锁定 AI coding 会漏掉更大的“创作/办公/决策”需求。来源：https://www.questmobile.com.cn/research/report/2028739596590878721/

3. B2B 内容团队已经在用 AI，但信任和流程整合不足。CMI 2025 B2B 内容营销研究显示，51% 的受访者认为生成式 AI 减少 tedious tasks，45% 认为 workflow 更高效；但 CMI 统计页同时显示只有 19% B2B marketers 把 AI 整合进日常流程，只有 4% 高度信任生成式 AI 输出。推断：机会不在“AI 自动写内容”，而在“可信来源 + 人工判断 + 工作流交付”。来源：https://contentmarketinginstitute.com/b2b-research/b2b-content-marketing-trends-research-2025 和 https://contentmarketinginstitute.com/content-marketing-strategy/content-marketing-statistics

4. Creator economy 有钱，但不等于个人账号立刻能变现。IAB 2025 Creator Economy Ad Spend & Strategy Report 预计美国 creator ad spend 2025 年达到 370 亿美元，同比增长 26%。这个证据证明创作者商业化是大市场，但不能说明你的切口、平台和语言市场已经验证。来源：https://www.iab.com/insights/2025-creator-economy-ad-spend-strategy-report/

5. 开发者方向有真实信任缺口，但它更适合作为题材垂类。Stack Overflow 2025 Developer Survey 显示，开发者 AI 工具采用高，但对准确性的信任不足：46% 不信任，33% 信任，只有 3.1% 高度信任。推断：AI coding / Agent / GitHub 项目实测是有价值题材，但不一定是整个商业定位。来源：https://survey.stackoverflow.co/2025/

6. AI 视频和内容生产工具在用户注意力中很强，但会放大低质量内容。a16z 2026 第 6 版 GenAI Consumer Apps 榜单显示，AI video、image、search、learning、productivity 和 creation apps 继续占据用户注意力，Sora 2 独立 App 快速达到百万下载级别。推断：HyperFrames / html-video 作为表达引擎有价值，但“AI 视频”本身不是第一产品。来源：https://a16z.com/100-gen-ai-apps-6/

7. 近 30 天 last30days query 1 命中“Google 的 summarize this video 功能对 YouTube 创作者有破坏性”“AI slop 造成内容信任问题”“客户要求 AI detection reports”等信号。这说明创作者/内容营销人群的真实问题不是“怎么生成更多内容”，而是“AI 改变分发、信任和交付后，内容如何仍然有价值”。

8. 近 30 天 last30days query 2 命中“how are marketers turning ai visibility reports into actual work?”、“Google search is a nightmare because of AI?”、“Clients are now asking for AI detection reports with content delivery”。这说明 AI search / GEO / AI visibility 方向有明确讨论，但互动量不高，证据仍偏早期。

9. 中国《人工智能生成合成内容标识办法》要求 AI 生成合成内容涉及显式和隐式标识，平台需要提供声明功能，用户发布生成合成内容时也应主动声明。这个证据提高了“原创判断 + 来源透明 + AIGC 标识”的重要性。来源：https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm

## 候选方向评分

评分 1-5，越高越好；风险分越高代表风险越低。

| 候选方向 | 用户匹配 | 市场反馈入口 | 差异化 | 资产化 | 风险 | 总分 | 判断 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| A. 面向中文 AI 实践型创作者/知识型自媒体/小团队的“海外 AI 信号到中文内容资产” | 5 | 4 | 5 | 5 | 3 | 22 | 推荐主方向。最贴合 SignalProof、Codex、HyperFrames 和账号验证。 |
| B. AI search / GEO / AI visibility 到内容动作的情报包 | 4 | 3 | 4 | 5 | 3 | 19 | 推荐作为第一批主题之一。更接近付费痛点，但证据早期且工具商噪音多。 |
| C. AI coding / Agent / GitHub 项目实测避坑内容 | 5 | 3 | 4 | 4 | 3 | 19 | 推荐作为稳定题材垂类，不推荐作为唯一定位。 |
| D. 泛 AI 工具测评与教程 | 3 | 5 | 2 | 3 | 2 | 15 | 可借流量，不作为核心方向。 |
| E. AI 视频/虚拟人/剧情短片制作教程 | 3 | 4 | 3 | 3 | 1 | 14 | 暂不主攻。制作成本、合规和信任风险高。 |
| F. 泛海外资讯翻译/搬运 | 2 | 3 | 1 | 2 | 1 | 9 | 放弃。版权、同质化、付费理由弱。 |

## 推荐方向定义

推荐方向不是“AI coding 实测号”，也不是“AI 工具搬运号”，而是：

> 面向中文 AI 实践型创作者、知识型自媒体和小团队，把海外 AI 信号筛选、验证、解释并转换为可发布、可复用、可售卖的中文内容资产。

第一轮内容主题建议使用三条栏目线：

- `AI search / GEO / AI visibility`：适合产品、运营、市场和内容团队，付费潜力更靠前。
- `AI content workflow / creator workflow`：适合知识型自媒体和小团队，能自然产出模板、流程和资料包。
- `AI coding / Agent / GitHub 项目实测`：利用用户已有工程判断力，作为高信任题材垂类。

## 反证和替代方案

- 泛 AI 工具测评已拥挤，头部账号和搬运号很多；如果没有一手来源、实测、反方和资产化，内容会被视为二手总结。
- AI 视频/虚拟人方向虽然热，但会面临 AIGC 标识、信任、制作成本和审美同质化问题，不适合第一阶段主攻。
- AI search / GEO 是热词，但工具商和 agency 正在快速包装概念；如果只做“GEO 教程”，很容易变成营销术语搬运。
- AI coding 方向有信任缺口，但人群更窄，内容可能进入技术圈自嗨；应作为题材而不是总定位。
- 用户当前没有真实账号数据；没有收藏、评论、私信、下载和付费意向前，不能声明商业成立。

## 证据等级

当前证据等级：medium。

- strong：趋势存在。AI 应用规模、创作者经济、B2B 内容 AI 化、开发者 AI 信任缺口、AIGC 标识合规都由外部来源支持。
- medium：方向选择。证据足以支持 7 天低成本实验和 30 天账号验证。
- weak：真实付费。没有用户自己的账号数据、私信、下载、付费意向或真实复用行为。
- blocked：X/Twitter 近 30 天讨论缺失，因为 xurl 返回 `CreditsDepleted`；YouTube 评论 enrichment 返回 HTTP 402；TikTok/Instagram/Threads 本轮没有有效命中。

## 结论许可

结论许可：低成本实验。

允许：

- 做 7 天最小内容资产实验。
- 产出小红书图文、公众号长笔记、60 秒短视频脚本和免费资料包样例。
- 如果用户授权发布，记录真实反馈。

不允许：

- 声称市场已验证。
- 做 SaaS、Web App、workflow builder。
- 把内部生产顺畅当成需求成立。
- 把 AI coding / Agent 直接写成唯一商业方向。

## 需要用户授权或开通

- X/Twitter：当前 `last30days` 的 X backend 为 `xurl`，但两次 query 均返回 `CreditsDepleted`。如果后续要判断 KOL 扩散和早期趋势，需要补 X credits 或降级为 web/HN/Reddit/GitHub。
- YouTube 评论：HTTP 402，无法获取观众评论，降低“真实观众反应”证据质量。
- 平台发布：若要发布小红书、公众号、视频号、B站或抖音，需用户确认账号、平台、是否公开发布、AIGC 标识和素材版权边界。
- Chrome 登录态：只有在用户授权查看后台数据、评论、私信或发布页时才使用。

## 证据缺口

- 真实用户原话不足，尤其是中文目标用户。
- 真实账号表现为空。
- 真实下载、私信、付费意向为空。
- 平台级 AIGC 细则没有逐平台复核。
- 还没有真实内容样例发布后的反馈。

## 下一步补证

进入 7 天验证实验：

1. 选 5 个海外 AI 信号，覆盖 AI search / GEO、AI content workflow、AI video/content、AI coding / Agent、AI app adoption。
2. 每个信号跑 SignalProof lite 初筛，保留来源、反方、判断和内容价值。
3. 选 3 个信号生成内容样例：小红书图文、公众号长笔记、60 秒短视频脚本。
4. 生成 1 个免费资料包样例：《海外 AI 信号到中文内容资产样例包》。
5. 若用户授权发布，记录 72 小时反馈；不发布则只能记为内部产物验证。
