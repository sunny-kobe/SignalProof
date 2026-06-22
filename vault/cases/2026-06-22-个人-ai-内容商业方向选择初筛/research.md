---
type: research
status: completed
updated_at: 2026-06-22
gate: medium
---

# 研究

## 要回答的问题

- 个人 AI 内容商业项目第一阶段到底应该选哪个细分方向？
- 是否必须从“中文 AI coding / 独立开发者”起步？
- 哪些方向只是流量热，不能支撑可复利资产？
- 哪个方向最适合用 SignalProof + Codex + HyperFrames/html-video 做 30 天实验？

## 已确认事实

- 用户明确删除“AI coding 工作流诊断/搭建服务”作为默认商业方向。
- 当前商业项目默认是 AI 内容商业化：用 HyperFrames / html-video 作为内部生产引擎，把海外 AI / 编程 / Agent / GitHub / 工作流信号转成中文图文、短视频、公众号笔记和资料包。
- 用户进一步修正：不应预设为“面向中文 AI coding / 独立开发者，用海外 AI 编程项目实测内容”，需要先研究方向。
- SignalProof 适合把这个问题处理成方向选择，而不是直接进入内容生产。

## 调研过程

- 读取 `AGENTS.md`、repo `signalproof` skill、`ai-content-commerce` skill、`personal-opportunity-os` skill 和历史 memory。
- 使用 web 搜索补充 2025-2026 年 AI 应用、内容创作者、开发者 AI 信任、B2B 内容营销、AI 短视频和合规资料。
- 本轮没有运行 `last30days` 引擎：当前问题是方向分层和候选切口，不是某个明确话题的近 30 天舆情验证。等方向收窄到 1-2 个候选题后，再用 `last30days` 对具体 query 做来源覆盖。

## 来源覆盖表

| 来源类型 | 候选能力 | 当前状态 | 结果质量 | 缺口 |
| --- | --- | --- | --- | --- |
| 中国 AI 应用和入口变化 | QuestMobile / 36氪 / web | 已覆盖 | medium | 数据能证明 AI 入口迁移和高信息决策场景增长，但不能直接证明你的账号会成功。 |
| 创作者和内容商业 | IAB / CMI / 36氪 / Digiday / web | 已覆盖 | medium | 能证明 creator economy、AI 内容流程和 AI 博主赛道存在，但缺少你自己账号的真实反馈。 |
| 开发者和 AI coding | Stack Overflow / web | 已覆盖 | medium | 能证明开发者有 AI 信任缺口，但不能证明这是最优内容商业起点。 |
| 合规和反证 | AI 标识法规 / AI slop 讨论 / HN / Reddit | 已覆盖 | medium | 能证明纯 AI 批量内容和虚拟人有信任风险，但仍需平台级规则复核。 |

## 交叉验证

- QuestMobile 2026 Q1 数据显示，中国 AI 原生 App 月活用户规模已达 4.4 亿，豆包、千问、DeepSeek 月活分别为 3.45 亿、1.66 亿和 1.27 亿；AI 使用正从认知普及进入能力执行和商业价值阶段。来源：https://www.questmobile.com.cn/research/report/2046482337382842370/
- QuestMobile 2025 应用层报告显示，创作设计、综合助手、效率办公是 AI 应用中占比较高的方向，原因是需求明确、变现路径清晰，但也意味着竞争激烈。来源：https://www.questmobile.com.cn/research/report/2028739596590878721/
- 36氪转述 QuestMobile 信源偏好研究：AI 原生 App 正在重构信息获取和决策路径，在线旅游、拍摄美化、汽车资讯、教育学习等高信息整理/高决策链路场景渗透明显。来源：https://36kr.com/p/3825497154196353
- 36氪分析“小红书是否被 AI 替代”时指出，小红书强场景中的旅游、美妆、技能学习与 AI 高渗透场景重叠。推断：如果只做小红书内内容，不考虑 AI 搜索/AI 答案信源，会错过新的信息入口。来源：https://36kr.com/p/3826839508210560
- IAB 2025 creator economy 报告显示，美国 creator ad spend 预计 2025 年达 370 亿美元，同比增长 26%，creator 已成为品牌连接消费者的重要渠道。来源：https://www.iab.com/insights/2025-creator-economy-ad-spend-strategy-report/
- Content Marketing Institute 2025 B2B 研究显示，B2B marketers 使用生成式 AI 后，51% 感到 tedious tasks 减少，45% 认为 workflow 更高效，56% 将 AI-powered automation 作为高/中优先级。来源：https://contentmarketinginstitute.com/b2b-research/b2b-content-marketing-trends-research-2025
- 同一研究的统计页显示，只有 19% B2B marketers 把 AI 整合进日常流程，只有 4% 高度信任生成式 AI 输出。推断：机会不在“教你用 AI 写内容”，而在“可信来源 + 工作流化 + 人工判断”的组合。来源：https://contentmarketinginstitute.com/content-marketing-strategy/content-marketing-statistics
- Stack Overflow 2025 Developer Survey 显示，开发者 AI 工具采用高，但对准确性信任不足：46% 不信任，33% 信任，只有 3.1% 高度信任。推断：开发者方向确实有“验证/实测/避坑”需求，但这只是候选方向之一。来源：https://survey.stackoverflow.co/2025
- a16z 2026 年第 6 版 Gen AI Consumer Apps 排名显示，AI 视频、图像、搜索、学习、生产力和创作类应用继续占据大量用户注意力，Sora 2 独立 App 曾快速达到 100 万下载。来源：https://a16z.com/100-gen-ai-apps-6/
- 36氪对 AI 博主的分类包含 AI 工具测评与科普、AIGC 创作、虚拟人/数字人、硬核技术与开发；其中 AI 工具测评与科普最常见、起量快、变现相对稳。来源：https://36kr.com/p/3814685114195721
- 36氪关于 AI 短视频博主的报道显示，AI 视频能快速涨粉，但商业化不自动成立，创作者仍需要脚本、镜头、转场和选题能力。来源：https://36kr.com/p/3381205512760068
- 中国《人工智能生成合成内容标识办法》要求 AI 生成合成内容涉及显式和隐式标识；内容传播平台也需要提供声明功能，用户发布生成合成内容时应主动声明。来源：https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm

## 反证和替代方案

- 泛 AI 工具测评已经拥挤。36氪列出的 AI 工具测评与科普类账号能起量，但头部账号已形成强势心智，后入者如果没有实测深度、来源质量或独特人设，很容易变成二手搬运。
- 纯 AI 短视频/虚拟人赛道有增长，但信任风险高、合规要求上升、制作成本并不低。Business Insider 2026 年案例显示 AI 长视频可能需要多周制作和上千美元成本；这说明“AI 视频很容易”是错误假设。来源：https://www.businessinsider.com/quit-job-now-makes-ai-videos-youtube-earns-more-money-2026-6
- AI slop 讨论在 HN、Reddit 和媒体中持续出现，用户反感的是缺少真实判断、重复、未标识和无原创价值的内容。推断：你的方向必须把“真人判断 + 一手来源 + 实测/证据”放在中心，而不是批量生成。
- 开发者方向有信任缺口，但如果只做 AI coding 工具实测，会陷入窄技术内容竞争；它更适合作为第一批内容主题之一，而不是整个商业项目的唯一定位。

## 证据等级

当前为 medium：

- strong：可以证明 AI 应用、AI 内容、创作者商业、B2B 内容工作流和开发者 AI 信任缺口都是真实存在的外部趋势。
- medium：可以支持方向初筛和 30 天低成本账号实验。
- weak：不能证明某个具体账号定位必然成功，也不能证明用户愿意付费。
- blocked：没有。当前不需要先做 SaaS、Web App 或自动化内容工厂。

## 结论许可

当前许可：收窄后继续低成本实验。不得写成市场已验证、可以产品化或可以做 SaaS。

## 候选方向评分

评分 1-5，越高越好。

| 候选方向 | 用户匹配 | 市场反馈入口 | 差异化 | 资产化 | 风险 | 总分 | 判断 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| A. 面向中文 AI 内容创作者/知识型自媒体的小型“海外 AI 信号到内容资产”工作流 | 5 | 4 | 5 | 5 | 3 | 22 | 第一优先级。最贴合 SignalProof、Codex、HyperFrames 和账号验证。 |
| B. 面向产品/运营/市场小团队的“AI 工具/案例/工作流可信情报包” | 4 | 3 | 4 | 5 | 3 | 19 | 第二优先级。更靠 B2B 和付费，但反馈周期更慢。 |
| C. 面向中文 AI coding / Agent / GitHub 项目关注者的实测避坑内容 | 5 | 3 | 4 | 4 | 3 | 19 | 可作为主题垂类，不宜先当唯一人群。 |
| D. 泛 AI 工具测评与科普账号 | 3 | 5 | 2 | 3 | 2 | 15 | 可借流量题材，不适合作为核心定位。 |
| E. AI 视频/虚拟人/剧情短片制作教程 | 3 | 4 | 3 | 3 | 1 | 14 | 热，但成本、合规和信任风险高，不建议第一阶段主攻。 |
| F. 泛海外资讯翻译/搬运 | 2 | 3 | 1 | 2 | 1 | 9 | 放弃。版权、同质化和付费理由都弱。 |

## 方向定义

推荐方向不是“AI coding 实测号”，也不是“AI 工具搬运号”，而是：

> 面向中文 AI 实践型创作者、知识型自媒体和小团队，把海外 AI 信号筛选、验证、解释并转换为可发布、可复用、可售卖的中文内容资产。

第一轮内容主题可以包含 AI coding / Agent / GitHub 项目，但主题服务于上层承诺：帮用户更快把海外高价值 AI 信号变成可信判断和内容资产。

## 需要用户授权或开通

- 下一阶段如要验证候选方向 A，需要运行 `last30days` 或 web/HN/Reddit/GitHub 搜索，找 5-10 个最近海外 AI 信号。
- 如要测试小红书/公众号发布，用户需要提供账号边界、可发布平台和是否接受 AI 标识。
- 不需要先开 Semrush、Similarweb、Brand24；当前不是品牌监测阶段。

## 证据缺口

- 真实用户原话为空。
- 真实发布反馈为空。
- 真实账号表现为空。
- 真实下载、私信、付费意向为空。

## 下一步补证

- 选方向 A 进入 7 天微实验。
- 产出 3 条小红书图文草稿 + 1 篇公众号长笔记 + 1 个免费资料包样例。
- 记录每条内容的来源、判断、素材复用和生产耗时。
- 如果可以发布，记录收藏、评论、私信、下载和关注；如果暂不发布，只能算内部产物验证。
