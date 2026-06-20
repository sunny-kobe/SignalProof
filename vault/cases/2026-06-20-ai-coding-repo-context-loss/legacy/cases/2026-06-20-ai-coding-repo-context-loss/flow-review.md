---
type: flow_review
status: completed
updated_at: 2026-06-20
case_stage: assumption-based-next-phase
---

# 流程自检

## 本次审计对象

- case：AI coding repo context loss
- run：`/Users/rust/Documents/Codex/2026-06-19/new-chat-3/outputs/signalproof-rerun-2026-06-20`
- 旧 demo：`/Users/rust/Documents/Codex/2026-06-20/personal-opportunity-os-signalproof-codex-protocol-2/outputs/signalproof-vault`
- 阶段：Signal / Research / Debate / Thesis / Validation / Artifact / Feedback / Decision / Asset / Flow Review

## 用户问题回答

### 这套流程是否已经记下来

已经在本地 SignalProof skill 和本轮 vault 中记录。当前还会继续反补 skill，让后续触发 `personal-opportunity-os` 时自动检查：

- 工具是否使用；
- 工具结果是否有效；
- last30days 是否噪音过高；
- 子线程是否有回执；
- 是否把 synthetic demo 误写成真实反馈；
- 是否有真实反馈才能推进成功决策。

### 执行之后怎么判断流程对不对

不靠感觉，靠五个门：

1. 阶段门：Signal 到 Asset 是否真的走完。
2. 证据门：事实、推断、缺口是否分开，是否有真实用户原话。
3. 工具门：相关工具是否用了，用完是否有效，失败是否记录。
4. 协作门：子线程是否有明确输出、回执和源线程验收。
5. 资产门：产物是否能被复用、发布、反馈，而不是只是一篇内部笔记。

### Day 1 是否用了 last30days

旧 Day 1 synthetic demo 没有使用 `last30days`。当时重点是搭 vault 和做 synthetic before/after，这不是致命错误，但进入市场判断前必须补。

本轮 rerun 已使用 `last30days`，但结果质量弱：只有 GitHub 和 Reddit 有效，X 因 `CreditsDepleted` 失败，HN/YouTube/TikTok/Instagram/Perplexity 等为 0，且大量结果是 `entity-miss demotion` 和泛 AI 噪音。因此它只能算弱证据和流程优化样本，不能算市场验证。

### Codex Pro 插件和搜索/调研能力是否应该用

应该用，但不能迷信“用了工具就等于证据强”。SignalProof 后续规则是：

- AI 工具、市场热度、真实讨论、开源项目冒头：默认候选 `last30days`。
- Codex / OpenAI 能力边界：默认查官方 Codex manual / OpenAI docs。
- 技术库和框架：默认查官方文档或 Context7。
- 公开采用和开发者信号：默认查 GitHub / HN / Web / RSS。
- demo 或网页：默认做浏览器验收。
- 多视角或并行任务：用子线程/子代理，但必须有回执和源线程验收。

## 阶段完整性

| 阶段 | 状态 | 评价 |
| --- | --- | --- |
| signal | passed | 已记录信号和个人匹配度。 |
| research | weak | 官方文档强，市场证据弱，last30days 噪音高。 |
| debate | passed | 已完成严格反方裁决。 |
| thesis | passed | 结论是收窄后继续。 |
| validation | running | GitHub repo 已发布，等待私聊和反馈回收。 |
| artifact | published | Day 2 GitHub repo 已发布。 |
| feedback | assumption-medium | 公开任务征集 issue 已创建，真实反馈为空；用户授权采用中等假设评价继续推进。 |
| decision | assumption-based-continuation | 不写验证成功，继续推进 SignalProof Protocol MVP。 |
| asset | published-not-validated-assumption-continued | GitHub repo 已发布，作为协议化示例资产继续沉淀。 |

## 工具覆盖审计

| 能力 | 是否相关 | 是否使用 | 结果或原因 |
| --- | --- | --- | --- |
| Web / 搜索 | 是 | 部分 | 用于方向核验，但原始 web 结果未完整留档。 |
| 官方文档 / 技术文档 | 是 | 是 | Codex manual 支撑 Skill、Plugin、AGENTS.md、Subagents 判断。 |
| last30days | 是 | 是 | 已跑，但结果弱相关，不能当强需求证据。 |
| GitHub / HN / RSS | 是 | 部分 | GitHub CLI 搜索 issue 结果为空；HN/RSS 未独立补强。 |
| 浏览器验收 | 否 | 未用 | 当前没有网页/demo 交互要验收。 |
| 子会话 / 多代理委派 | 是 | 是 | 已完成 opposition-review、artifact-plan、process-qa，并回执源线程。 |
| 本地文件检查 | 是 | 是 | 已检查 run 目录、case、subtasks、旧 demo 资产。 |
| OpenAI Docs skill | 是 | 是 | 已按 Codex self-knowledge 路线读取 manual。 |

## 来源覆盖

| 来源 | 状态 | 结论影响 |
| --- | --- | --- |
| Codex manual | 强 | 支撑 Skill/Plugin/AGENTS.md/Subagents 架构判断。 |
| last30days Reddit | 弱 | 有结果但泛 AI 噪音高。 |
| last30days GitHub | 弱 | 多为 bot/tool traces，不代表用户主动需求。 |
| X | 失败 | `CreditsDepleted`，不能当作无人讨论。 |
| HN | 缺口 | 本轮为 0，需窄查询补跑。 |
| YouTube/TikTok/Instagram/Threads/Perplexity | 缺口 | 本轮为 0，暂不支撑结论。 |
| GitHub issue search | 弱反证 | 直接 query 为空，说明公开 issue 证据薄。 |

## 证据质量

- 已确认事实：Codex 支持 `AGENTS.md`、Skills、Plugins、Subagents；本轮 `last30days` 来源覆盖弱；旧 demo 是 synthetic。
- 关键推断：痛点可能真实，但公开证据不足；机会在审计和验证，不在发明上下文文件。
- 证据缺口：真实用户原话、真实失败任务、真实 before/after、公开反馈。
- 是否有真实用户原话：没有。
- 是否有真实反馈：没有。
- 是否有假设反馈：有，用户授权采用“中等评价”继续推进。
- 假设输入边界：可用于下一阶段协议化和内部 MVP，不可用于验证成功或商业化判断。

## 反方强度

最强反对意见：

```text
官方机制已经存在，公开市场证据弱，synthetic demo 不能证明需求；如果没有真实任务，这只是一个漂亮的 AI coding 模板。
```

是否影响当前结论：影响。它把结论从“继续做产品”压成“收窄后继续验证”。

## 产物边界

- 产物是否可公开：可以，但必须标注验证中。
- 是否存在 synthetic demo：存在。
- 是否误写成真实反馈：当前没有。
- 是否过早产品化：已压住，不做 Web App / SaaS / dashboard / Plugin。

## 流程问题

- 漏用的能力：旧 Day 1 没用 last30days；本轮 HN/Web/GitHub 原始结果留档不足。
- 过度生产的部分：旧 demo 可以演示，但不能继续无限打磨。
- 判断过快的部分：不能从个人经验直接跳到市场成立。
- 需要补跑的任务：窄 query 的 last30days / GitHub / HN / Web 搜索，真实用户私聊。
- 新增协作问题：Day 2 审计子线程完成后没有落目标文件，源线程必须以文件存在和内容满足验收标准为准，而不是只看线程状态。

## 阶段评分

| 维度 | 分数 | 理由 | 必须补强 |
| --- | ---: | --- | --- |
| 阶段完整性 | 4 / 5 | 主链路文件和 GitHub repo 已发布，但真实反馈未回收。 | 私聊验证和反馈回填。 |
| 证据质量 | 2 / 5 | 官方文档强，市场证据弱。 | 真实用户任务和窄查询。 |
| 工具覆盖 | 3 / 5 | 已用 last30days、官方文档、GitHub、子线程。 | 保存 Web/HN/GitHub 原始结果。 |
| 协作闭环 | 4 / 5 | 三个子任务已落文件并回执。 | 增加子任务台账常规化。 |
| 资产化清晰度 | 4 / 5 | 本地发布包已生成，真实反馈尚未回填。 | 发布后记录反馈。 |

## 质量门结论

- 能否进入下一阶段：可以进入 Day 2 私聊验证和反馈回收。
- 允许带缺口推进的缺口：市场证据弱、真实反馈为空。
- 必须先补的缺口：私聊 5 个目标用户，获得至少 1 个真实失败任务。
- 不能包装成事实的推断：不能说“市场已验证”“用户已需要”“可以产品化”。
- 新决策：在用户授权中等假设评价后，可以进入 SignalProof Protocol MVP 设计，但不能进入商业化或产品化承诺。

## 下次优化

- 保留：反方裁决、artifact plan、process QA、completion receipt。
- 删除：大而全 query 和过早产品化。
- 补强：真实用户任务、72 小时反馈、before/after 结果。
- 补强：Day 2 执行账本、真实反馈门、子线程文件验收门。
