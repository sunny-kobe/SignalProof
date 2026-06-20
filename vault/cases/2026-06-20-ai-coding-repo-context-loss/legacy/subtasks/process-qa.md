---
type: subtask_report
task_name: SignalProof rerun - process QA and skill improvement
status: completed
source_thread_id: 019ee024-6ff0-73a0-8311-7a22b9602945
updated_at: 2026-06-20
output_path: /Users/rust/Documents/Codex/2026-06-19/new-chat-3/outputs/signalproof-rerun-2026-06-20/subtasks/process-qa.md
---

# SignalProof 重跑流程验收与 Skill 反补建议

## 结论

这次重跑的方向是对的，但流程还没有闭环。当前只能判定为：

```text
Signal / Research / Thesis 已启动，证据层偏弱，后续 Debate / Validation / Artifact / Feedback / Decision / Asset 仍未完成。
```

`last30days` 不是没用，而是用了以后暴露出查询策略和质量门不足：它实际只产出 GitHub + Reddit 两类有效来源，大量结果是泛 AI 噪音，且多处出现 `fallback-local-score` 和 `entity-miss demotion`。所以它不能被当成“市场有需求”的强证据，只能被记录为一次弱相关扫描和流程优化样本。

本次最重要的流程教训是：SignalProof 不能只检查“有没有调用某个工具”，还要检查“工具结果是否足够相关、来源覆盖是否合格、失败源是否记录、是否需要补跑更窄查询”。

## 审计对象

- 新 run 路径：`/Users/rust/Documents/Codex/2026-06-19/new-chat-3/outputs/signalproof-rerun-2026-06-20`
- 证据文件：`/Users/rust/Documents/Codex/2026-06-19/new-chat-3/outputs/signalproof-rerun-2026-06-20/assets/research/ai-coding-repo-context-agents-md-claude-code-memory-codex-raw-signalproof-rerun.md`
- 当前 case：`/Users/rust/Documents/Codex/2026-06-19/new-chat-3/outputs/signalproof-rerun-2026-06-20/cases/2026-06-20-ai-coding-repo-context-loss`
- 当前 skill：`/Users/rust/.codex/skills/personal-opportunity-os/SKILL.md`
- 当前模板：`/Users/rust/.codex/skills/personal-opportunity-os/references/templates.md`

## 阶段审计

### 1. 建目录

已完成基础 vault 结构：

- `cases/2026-06-20-ai-coding-repo-context-loss/`
- `assets/research/`
- `assets/templates/`
- `assets/prompts/`
- `assets/sops/`
- `assets/repos/`
- `assets/articles/`
- `assets/services/`
- `reports/`
- `subtasks/`

评价：目录结构基本符合 SignalProof 当前设想，能承接研究、产物、报告和子任务。

缺口：

- 当前 case 只看到 `signal.md`、`research.md`、`thesis.md`。
- `debate.md`、`validation.md`、`artifact.md`、`feedback.md`、`decision.md`、`asset.md`、`flow-review.md`、`report.md` 尚未形成。
- `subtasks/` 原本预留了反方裁决、发布产物方案和流程 QA，但当前只有本文件会落地，其他子任务结果尚未出现在 vault 内。

### 2. Signal

`signal.md` 基本合格。它把机会定义为 `AI coding repo context loss`，并且没有误扩成平台、SaaS 或自动 repo 理解系统。

亮点：

- 用户画像和机会匹配写得清楚。
- 已经把方向收窄到 repo context audit、`AGENTS.md` / `CLAUDE.md` 模板、before/after 对比。
- 明确承认旧 demo 是 synthetic demo，不等于真实反馈。

缺口：

- 原始 signal 仍偏“个人经验 + 推断”，缺少一条强一手用户原话作为起点。
- 后续需要补“真实失败任务样本”，例如某个 AI coding 用户提交的具体写偏任务。

### 3. last30days

已使用。计划文件为：

- `assets/research/last30days-plan-ai-coding-context.json`

原始输出为：

- `assets/research/ai-coding-repo-context-agents-md-claude-code-memory-codex-raw-signalproof-rerun.md`

本次查询主题：

```text
AI coding repo context AGENTS.md Claude Code memory Codex
```

本次结果摘要：

- 日期范围：2026-05-21 到 2026-06-20。
- 有效来源：2 个，GitHub 和 Reddit。
- 总证据：18 条。
- Reddit：13 条，3,496 upvotes，1,296 comments。
- GitHub：5 条，22 reactions，216 comments。
- HN、X、YouTube、TikTok、Instagram、Perplexity、Threads 均为 0。
- 多数结果出现 `fallback-local-score` 和 `entity-miss demotion`。

评价：调用是对的，但结果质量不合格，不能作为强市场证据。

主要问题：

- Query 太宽，把 `AI coding`、`repo context`、`AGENTS.md`、`Claude Code memory`、`Codex` 混在一起，导致检索既像工具生态，又像 AI 新闻，又像 local model 讨论。
- Reddit 结果被 r/singularity、r/LocalLLaMA 这类泛 AI 高热内容污染。
- GitHub 结果多为 bot 评论、AI review 工具痕迹或配置 bundle，不代表用户主动表达需求。
- 直接命中 `repo context audit checklist` 或“我愿意用这个工作流”的证据很弱。
- 结果中相关性最高的 `A Context Brain for you (and your AI Agent)`、`What real projects have you shipped using AI coding tools?` 也只是弱相关，不能证明机会成立。

下一版查询策略：

不要再用一个大 query 扫全场，改成三到五个窄查询，每个查询回答一个问题。

建议第一组：失败模式查询。

```text
AI coding agent ignores project conventions
Claude Code wrong repo context
Codex ignores existing API contract
Cursor agent wrong file structure
```

目标：找真实抱怨，而不是找 `AGENTS.md` 方案。

建议第二组：上下文文件查询。

```text
AGENTS.md repo instructions Codex
CLAUDE.md project memory Claude Code
project instructions coding agent
agent instructions repository conventions
```

目标：找用户如何维护 `AGENTS.md` / `CLAUDE.md` / repo instructions，以及限制在哪里。

建议第三组：验证产物查询。

```text
repo context audit checklist AI coding
AI coding checklist project context
coding agent onboarding checklist
AI coding workflow repo setup
```

目标：判断 checklist / audit / template 这类资产有没有真实需求。

建议第四组：目标人群查询。

```text
site:reddit.com/r/ClaudeAI AGENTS.md
site:reddit.com/r/ChatGPTCoding repo context
site:news.ycombinator.com Claude Code memory
site:news.ycombinator.com coding agent project instructions
```

目标：不要让泛 AI 社区稀释目标用户。

建议第五组：替代品和反证查询。

```text
AGENTS.md not useful
CLAUDE.md too long context
AI coding instructions don't work
long agent instructions reduce performance
```

目标：主动找“写更多上下文文件也没用”的反证。

下一版质量门：

- 如果有效来源少于 3 个，标记为来源覆盖不足。
- 如果 X/HN/YouTube 等源为 0，必须记录是工具失败、额度问题、无结果，还是查询不匹配。
- 如果结果中超过一半是 `entity-miss demotion` 或 `fallback-local-score`，必须补跑更窄查询。
- 如果没有真实用户原话，不能把结论写成“用户有需求”，只能写成“有待验证的机会假设”。

### 4. 官方文档

已使用 OpenAI Codex manual，且方向正确。

已支撑的事实：

- Codex Skills 是 reusable workflow 的 authoring format，Plugins 是 installable distribution unit。
- `AGENTS.md` 是 Codex 的持久项目指令入口。
- Codex 会在工作前读取 `AGENTS.md`，并支持全局、项目、子目录层级。
- 项目指令默认有 32 KiB 左右的大小限制，说明“越长越好”不是正确方向。
- Codex 官方建议先用 local skill 迭代个人工作流，要分享、绑定 app/MCP/hooks 或发布稳定包时再做 plugin。
- Subagents 适合并行复杂任务，但需要显式请求，且会带来额外成本。

评价：官方文档这一部分是本次最扎实的证据。它能证明 SignalProof 适合先做 Skill / Protocol / Vault，再考虑 Plugin，而不是先做独立平台。

缺口：

- 当前 vault 只保存了研究结论，没有把官方文档的来源路径、章节和行号整理成可复查证据清单。
- 如果引用 Claude Code memory / `CLAUDE.md` 相关事实，需要把 Claude 官方文档或可复查来源也保存到 `assets/research/`，不能只写在总结里。

### 5. GitHub / HN / Web

当前 `research.md` 写了已使用 GitHub CLI 搜索和 web search，但 vault 内没有看到独立保存的 GitHub / HN / Web 原始结果文件。

评价：从流程审计角度，不能只说“用过”，还要留下可复查的查询和结果。

缺口：

- 没有 `github-search-*.md` 或 `web-search-*.md` 之类的原始证据文件。
- HN 在 `last30days` 里是 0，但没有单独补 HN 搜索。
- Web 搜索如果用于“反证”或“已有方案”，需要保存链接、标题、日期、摘录和判断。
- GitHub 结果里 bot 噪音较多，应区分“工具痕迹”和“用户主动采用”。

建议补强：

- 保存 `assets/research/github-search-ai-coding-context.md`。
- 保存 `assets/research/hn-search-ai-coding-context.md`。
- 保存 `assets/research/web-official-and-alternatives.md`。
- 每条证据标注：事实 / 用户原话 / 工具痕迹 / 推断 / 弱相关 / 反证。

### 6. Fork 协作

当前 README 预留了三类子任务：

- 反方裁决：`subtasks/opposition-review.md`
- 发布产物方案：`subtasks/artifact-plan.md`
- 流程验收和 skill 优化：`subtasks/process-qa.md`

本文件完成第三项。

评价：子线程协作方向正确，符合 Codex 作为主战场、SignalProof 作为协议层的定位。

缺口：

- vault 内缺少子任务索引，无法一眼看到每个子任务分配给哪个 thread、状态是什么、产物路径是什么、是否已验收。
- 委派回执还没有形成统一字段，例如 tool coverage、source failures、是否需要补跑。
- 如果子线程没有主动反推回执，源线程仍可能漏掉结果。

建议：

- 新增 `subtasks/index.md` 或在 `flow-review.md` 中增加“委派任务台账”。
- 所有委派 prompt 必须带：源线程、目标线程、任务名、输出路径、验收标准、完成回执字段。
- 源线程收到回执后必须检查文件存在性，不只相信最终文字。

### 7. 后续回写

当前已有回写：

- `signal.md`
- `research.md`
- `thesis.md`

未完成回写：

- `debate.md`
- `validation.md`
- `artifact.md`
- `feedback.md`
- `decision.md`
- `asset.md`
- `flow-review.md`
- `report.md`

评价：当前不能声称 SignalProof 全链路已跑完，只能说前半段已经启动，且产生了一个重要流程发现：研究工具必须有质量门。

## 流程评分

| 维度 | 分数 | 理由 |
| --- | ---: | --- |
| 阶段完整性 | 2 / 5 | 目录和前三个阶段已形成，但 debate、validation、artifact、feedback、decision、asset、flow-review、report 均未闭合。 |
| 证据质量 | 2 / 5 | 官方文档证据较强，但市场/用户证据弱；last30days 结果噪音高，缺少真实用户原话和真实反馈。 |
| 工具覆盖 | 3 / 5 | 已覆盖 last30days、Codex manual、部分 GitHub/Web 和子线程思路；但 HN/Web/GitHub 原始结果未保存，X/YouTube 等失败未形成结构化 failure log。 |
| 协作闭环 | 2 / 5 | 已有子任务设计和本次 process QA，但子任务台账、完成回执、源线程验收和回写机制还不够硬。 |
| 资产化清晰度 | 2 / 5 | 已明确 checklist、模板、before/after demo、72 小时验证，但实际 artifact/asset 文件尚未生成，真实反馈为空。 |

综合判断：

```text
流程方向成立，但当前 run 不是完成态；下一步应该补强研究质量门和子任务回执门，然后继续推进到真实验证产物。
```

## Skill 需要反补的具体条目

### 1. 新增规则：工具调用不等于证据有效

建议加入 `SKILL.md`：

```text
如果某个阶段调用了 last30days、搜索、GitHub/HN/Web 或官方文档，Codex 必须同时审计结果质量。工具被调用只能说明覆盖了动作，不能自动说明证据有效。若结果来源少、相关性弱、失败源多或大量出现 fallback / entity-miss，应标为弱证据，并补跑更窄查询或降级结论。
```

### 2. 新增规则：last30days 质量门

建议加入 `SKILL.md`：

```text
使用 last30days 时必须保存 query plan、raw output、source coverage、失败源、相关性判断和是否补跑。若有效来源少于 3 个，或超过半数结果明显弱相关，或出现大量 entity-miss / fallback-local-score，不能把结果当作强需求证据，必须补跑更窄 query 或在 research.md 标记为证据缺口。
```

### 3. 新增规则：研究查询必须分层

建议加入 `SKILL.md`：

```text
深度研究不能只跑一个大而全 query。至少拆成：失败模式、已有方案、目标用户讨论、反证、可验证产物五类查询。每类查询回答一个问题，并记录到 research.md。
```

### 4. 新增规则：官方文档证据清单

建议加入 `SKILL.md`：

```text
凡是用官方文档支撑 Codex、Skill、Plugin、AGENTS.md、Subagents、MCP、Hooks 等机制判断时，必须在 research.md 保存来源路径或 URL、章节、行号或可复查锚点，以及该来源支撑的具体 claim。
```

### 5. 新增规则：GitHub / HN / Web 原始结果必须留档

建议加入 `SKILL.md`：

```text
如果结论依赖 GitHub、HN、Web 搜索或 RSS，必须在 assets/research/ 保存原始搜索摘要，包含 query、时间、来源、链接、标题、摘录、相关性等级和用于结论的方式。不能只在 research.md 写“已使用搜索”。
```

### 6. 新增规则：子任务必须有台账和回执

建议加入 `SKILL.md`：

```text
每次跨线程委派都必须写入子任务台账，记录任务名、source_thread_id、target_thread_id、输出路径、状态、验收标准和回执状态。子线程完成后必须反推 completion receipt；源线程必须检查文件存在性并回写 case。
```

### 7. 新增规则：未反馈不得决策成功

建议加入 `SKILL.md`：

```text
如果没有真实发布链接、真实用户反馈或真实 before/after 结果，feedback.md 必须写“真实反馈为空”，decision.md 不能写“继续产品化”或“验证成功”，只能写“继续验证 / 收窄 / 暂停 / 放弃”。
```

### 8. 新增规则：每个阶段必须有状态门

建议加入 `SKILL.md`：

```text
每个 case 阶段必须有 gate 状态：not-started / running / weak / passed / blocked。只有上一个阶段 passed 或明确允许带缺口推进时，才能进入下一个阶段。弱证据可以推进实验，但不能推进成功结论。
```

## 模板字段反补建议

### research.md 增补

建议增加：

```md
## 查询计划

| 查询层 | query | 目标问题 | 预期来源 | 实际来源 | raw 文件 |
| --- | --- | --- | --- | --- | --- |

## 来源覆盖

| 来源 | 是否相关 | 是否成功 | 结果数量 | 失败原因 | 是否需要补跑 |
| --- | --- | --- | ---: | --- | --- |

## 工具失败记录

| 工具 | 时间 | 失败类型 | 错误信息 | 对结论影响 | 补救动作 |
| --- | --- | --- | --- | --- | --- |

## 证据相关性

- 强相关：
- 中相关：
- 弱相关：
- 噪音：

## 研究质量门

- 是否有至少 3 类来源：
- 是否有真实用户原话：
- 是否有反证：
- 是否保存 raw evidence：
- 是否需要补跑：
- 当前研究状态：weak / passed / blocked
```

### flow-review.md 增补

建议增加：

```md
## 阶段评分

| 维度 | 分数 | 理由 | 必须补强 |
| --- | ---: | --- | --- |
| 阶段完整性 |  |  |  |
| 证据质量 |  |  |  |
| 工具覆盖 |  |  |  |
| 协作闭环 |  |  |  |
| 资产化清晰度 |  |  |  |

## 质量门结论

- 能否进入下一阶段：
- 允许带缺口推进的缺口：
- 必须先补的缺口：
- 不能包装成事实的推断：
```

### completion receipt 增补

建议回执字段变成：

```md
## Completion Receipt

- 委派任务名称：
- 状态：completed / blocked / needs-review
- source_thread_id：
- target_thread_id：
- 输出路径：
- 新增文件：
- 更新文件：
- 核心结论：
- 明确边界：
- 工具覆盖：
- 工具失败：
- 来源覆盖：
- 证据强度：weak / medium / strong
- 需要补跑：
- 需要源线程验收：
- 需要用户拍板：
- 下一步：
```

### subtasks/index.md 新模板

建议新增：

```md
# 子任务台账

| 任务 | target_thread_id | 状态 | 输出路径 | 回执 | 源线程已验收 | 下一步 |
| --- | --- | --- | --- | --- | --- | --- |
```

## 对当前流程是否“对”的判断方式

这套流程以后不能靠感觉判断，而要靠五个门：

1. 阶段门：Signal 到 Asset 是否真的走完，还是只停在研究。
2. 证据门：事实、推断、缺口是否分开，是否有真实用户原话。
3. 工具门：相关工具是否用了，用完是否有效，失败是否记录。
4. 协作门：子线程是否有明确输出、回执和源线程验收。
5. 资产门：产物是否能被复用、发布、反馈，而不是只是一篇内部笔记。

当前这次 run 的判断：

```text
流程框架是对的，但执行质量还不够硬；特别是 last30days 查询策略、原始证据留档、子任务台账和真实反馈门，需要立刻反补。
```

## 建议下一步

1. 补跑更窄的 `last30days` 查询，不再使用一个大 query。
2. 保存 GitHub / HN / Web 原始搜索证据。
3. 让反方裁决和发布产物方案两个子任务也落文件。
4. 创建 `flow-review.md`，把本报告核心评分和缺口回写进去。
5. 再推进 `validation.md` 和 `artifact.md`，但仍然不要写“验证成功”。
6. 找 5 个真实 AI coding 高频用户，拿真实写偏任务挑战 checklist。

## 反推回源线程 Completion Receipt

- 委派任务名称：SignalProof rerun - process QA and skill improvement
- 状态：completed
- source_thread_id：019ee024-6ff0-73a0-8311-7a22b9602945
- 输出文件：`/Users/rust/Documents/Codex/2026-06-19/new-chat-3/outputs/signalproof-rerun-2026-06-20/subtasks/process-qa.md`
- 关键结论：本次流程方向正确但未闭环；`last30days` 已使用但查询太宽、来源覆盖不足、相关性弱，不能当强市场证据；需要把“工具质量门、失败记录门、子任务回执门、研究质量门”反补进 skill 和模板。
- 明确边界：本报告只做流程验收和 skill 优化建议，没有修改 skill 文件；当前 run 不能包装成完整验证案例或成功案例。
- 工具覆盖：已审计 `personal-opportunity-os`、`user-working-profile`、`last30days`、OpenAI Codex manual、当前 vault 文件和模板。
- 工具失败/缺口：X/HN/YouTube/TikTok/Instagram/Perplexity 在本次 `last30days` 输出中均为 0；GitHub/HN/Web 原始搜索结果未在 vault 内独立留档；其他子任务产物尚未落入 `subtasks/`。
- 下一步：源线程应读取本报告，补 `flow-review.md`，再决定是否把新增规则合并进 `SKILL.md` 和 `references/templates.md`。
