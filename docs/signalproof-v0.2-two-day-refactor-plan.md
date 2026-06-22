# SignalProof V0.2 两天收缩改造计划

生成日期：2026-06-22

## 目标

两天内完成《SignalProof 深度研究与反方审查》里对当前仓库最关键、可落地的改造，把 SignalProof 从“完整个人机会 OS 叙事”收缩为“个人证据协议 / 机会审计协议 / 判断与资产沉淀协议”。

本轮不是做 Web App、SaaS dashboard、workflow builder、通用知识库、自动雷达或插件平台。改造目标是让本地 Markdown vault、模板和脚本更强地约束三件事：

- 真实外部反馈优先于流程完整。
- 证据有效性优先于工具调用记录。
- 资产复用优先于资产命名。

## 两天完成定义

两天后必须满足：

- 协议文档明确 `SignalProof = 个人证据协议`，并把 `Personal Opportunity OS` 降为背景叙事，不作为当前执行口号。
- 新 case 默认从 `lite` 开始，`full` 变成有硬条件的升级事件。
- lite case 的文件数可以暂时遵守现有 AGENTS 规则，但每个文件必须变短、变硬、少重复。
- 研究质量门从“关键词存在检查”升级为“结构化字段 + 数量门槛 + 结论许可检查”。
- 反馈状态从自然语言散落收敛为枚举字段。
- 资产 registry 从目录表升级为复用账本。
- `check-all` 顶层状态不再只有全绿语义，必须暴露 warning 总量和 `passed-with-warnings`。
- 新增或增强资产检查，能看见 `reuse_count=0` 或 `last_used_by=none` 的资产比例。
- 更新 repo skill / plugin skill / AGENTS / docs / templates / scripts，使新窗口和后续 Codex 都按同一套规则执行。
- 创建一个 internal-audit full case 记录本轮改造，并通过 strict 检查。
- 运行并记录验证命令，无法通过的项必须明确原因和修复建议。

## 关键判断

报告总体采纳，但按仓库现实分层执行。

采纳：

- 继续做 SignalProof，但收缩为个人证据协议。
- 真实外部反馈是最大缺口。
- full case 当前太重，必须从默认动作降级为稀缺升级。
- 研究质量门必须比关键词检查更硬。
- 资产 registry 必须记录复用，而不只是登记。
- 插件治理降级，插件只在改变判断、减少不确定性或验收产物时使用。
- 内容商业方向只作为 SignalProof 压力测试场，不是 SignalProof 定义本身。

改写后采纳：

- 不要第一步就强删 lite 的 `debate.md`，因为当前 `AGENTS.md` 明确 lite 至少包含 `signal.md`、`research.md`、`debate.md`、`decision.md`、`asset.md`。
- 本轮先把 `debate.md` 压成短反方块模板；若两天后脚本和文档一致，再决定是否把 lite 改成 4 文件。
- `report.md` 暂不从 full 必需文件里直接删除，先改成“自动导出优先，手写 report 只保留最小摘要”；否则会和 AGENTS / script / export 规则同时冲突。

不采纳：

- 不在两天内做独立 UI、SQLite、插件市场、自动雷达、n8n/Dify、Notion/Obsidian 集成。
- 不在两天内证明市场验证成立。
- 不把内部流程反馈、synthetic demo、published-not-validated 写成真实反馈。

## Day 1：收缩协议、模板和状态字段

### 1. 冻结范围和当前状态

先运行：

```bash
cd /Users/rust/Documents/SignalProof
git status --short
python3 scripts/signalproof.py check-all
python3 scripts/signalproof.py check-plugin-drift --no-codex
```

记录：

- 当前 dirty files，避免误改用户已有变更。
- `check-all` 的 warning 数量。
- plugin drift 是否失败；如果失败，判断是快照过期、安装列表漂移，还是脚本/lock 不一致。

### 2. 更新定位文档

改这些文件：

- `README.md`
- `docs/protocol.md`
- `docs/current-flow.md`
- `AGENTS.md`
- `.agents/skills/signalproof/SKILL.md`
- `plugins/signalproof/skills/signalproof/SKILL.md`

必须写清：

- 当前执行名：`SignalProof 个人证据协议`。
- 上位叙事 `Personal Opportunity OS` 只作为长期背景，不作为本轮执行范围。
- V0.2 不做 Web App、SaaS dashboard、workflow builder、通用知识库、自动雷达。
- 默认所有新外部机会 case 用 `case_mode: lite`。
- full 升级硬条件：
  - `evidence_grade` 至少为 `medium`；
  - 有明确外部动作：发布、访谈、私信测试、下载页、表单回收或真实目标人反馈；
  - 至少有一个可登记资产候选；
  - `decision.md` 写明为什么需要 full，而不是为了完整而完整。
- internal-audit / plugin-test / external-opportunity 三类 case 必须在 `signal.md` frontmatter 或正文里清楚区分。
- 插件默认降级为候选能力，不再用插件矩阵制造“系统 ready”的错觉。

### 3. 更新模板

改这些文件：

- `templates/case/signal.md`
- `templates/case/research.md`
- `templates/case/debate.md`
- `templates/case/decision.md`
- `templates/case/feedback.md`
- `templates/case/asset.md`
- `templates/case/tool-ledger.md`
- `templates/case/flow-review.md`
- `templates/case/process-log.md`
- `templates/case/report.md`

`signal.md` frontmatter 增加或统一：

```yaml
case_mode: lite
case_type: external-opportunity
protocol_scope: personal-evidence-protocol
```

`research.md` frontmatter 增加：

```yaml
evidence_grade: weak
permission: continue-research
source_types_covered: 0
primary_source_count: 0
external_quote_count: 0
counterevidence_count: 0
independent_source_count: 0
```

`feedback.md` frontmatter 增加：

```yaml
feedback_status: none
validation_status: none
real_feedback_count: 0
paid_signal_count: 0
published_url_count: 0
```

允许值：

```text
feedback_status:
none / internal / synthetic-demo / assumed / published-no-feedback / qualitative-real / quantitative-real / paid-signal

validation_status:
none / artifact-built / published / externally-observed / repeated
```

`asset.md` frontmatter 增加：

```yaml
asset_status: candidate
registry_required: true
reuse_count: 0
proof_of_reuse: none
```

允许值：

```text
asset_status:
none / candidate / registered / reused / retired
```

模板压缩原则：

- lite 的 `debate.md` 只保留强反方、替代方案、kill 条件，不写长篇辩论。
- `thesis.md` 和 `decision.md` 减少重复；`thesis.md` 只放暂定判断，最终动作放 `decision.md`。
- `report.md` 改成最小摘要，不重复导出报告全文。
- `tool-ledger.md` 记录“候选、实际使用、结果质量、是否改变判断”，不要复制大段插件矩阵。

### 4. 更新资产账本

改 `vault/assets/registry.md`。

新增列：

```text
reuse_count
proof_of_reuse
reuse_cost_minutes
preconditions
public_or_private
supersedes
owner_scope
```

迁移现有行：

- `last_used_by=none` 的资产，`reuse_count=0`。
- 已被模板、脚本或后续 case 使用的资产，给出可复查路径。
- 不确定的值不要编造，用 `unknown` 或 `none`。

### Day 1 验收

运行：

```bash
python3 scripts/signalproof.py check-all
git diff --check
```

Day 1 不要求所有历史 warning 清零，但要求：

- 新模板没有未替换 `{{变量}}` 除模板本身必要占位。
- 新文档不再鼓励 full 默认化。
- `SignalProof 个人证据协议` 的定位贯穿 README / protocol / skill / AGENTS。

## Day 2：脚本门槛、审计 case 和验证闭环

### 5. 修改 `scripts/signalproof.py`

优先改这些能力：

1. `check-all` 汇总状态

当前 `check-all` 只返回 failures，容易让 warning 被理解为全绿。改成输出：

```text
Checked N case(s), failures: X, warnings: Y
Overall status: passed / passed-with-warnings / failed
```

返回码建议：

- 有 error 返回 1；
- 只有 warning 仍返回 0，兼容历史 case；
- 但 stdout 必须明确 `passed-with-warnings`。

2. 结构化 frontmatter 检查

新增轻量 frontmatter parser，只用标准库即可。

检查 `research.md`：

- `evidence_grade` 必须是 `strong / medium / weak / blocked`。
- `permission` 必须是 `continue-research / low-cost-experiment / pause / abandon`。
- 如果 `permission` 是 `low-cost-experiment`，则 `source_types_covered >= 2` 且 `counterevidence_count >= 1`。
- 如果 `evidence_grade` 是 `strong`，则 `source_types_covered >= 3` 且 `primary_source_count + external_quote_count >= 1`。
- 如果字段缺失，在 strict 下失败；非 strict 下 warning。

检查 `feedback.md`：

- `feedback_status` 必须在允许值内。
- `validation_status` 必须在允许值内。
- 如果 `feedback_status` 是 `none / internal / synthetic-demo / assumed / published-no-feedback`，则 `decision.md` 不得出现 `市场已验证`、`已验证需求`、`可以产品化`、`可以做 SaaS` 等过度声称。
- 如果 `validation_status=published`，不能自动等于 `externally-observed`。

检查 `asset.md`：

- `asset_status` 必须在允许值内。
- 如果 `asset_status=reused`，则 `reuse_count >= 1` 且 `proof_of_reuse != none`。
- 如果 `asset_status=registered` 或 `reused`，必须能在 `vault/assets/registry.md` 找到对应资产标题或 id。

3. 新增 `check-assets`

输出：

```text
registered_assets: N
reused_assets: X
candidate_assets: Y
zero_reuse_assets: Z
zero_reuse_ratio: P%
status: passed / passed-with-warnings / failed
```

最低规则：

- registry 不存在：failed。
- 有 `last_used_by=none` 或 `reuse_count=0`：warning，不默认失败。
- `strength=strong` 但 `reuse_count=0`：strict 下失败。

4. 可选增强 `check-case --strict`

strict 下把结构化字段 warning 升级为 failure，继续保留历史 case 宽容策略。

### 6. 创建本轮 internal-audit case

运行：

```bash
python3 scripts/signalproof.py init-case "SignalProof V0.2 两天收缩改造" --case-type internal-audit --case-mode full
```

填好这个 case，至少要记录：

- 报告结论哪些采纳、哪些改写采纳、哪些不采纳。
- 修改了哪些文件。
- 哪些脚本 gate 新增或增强。
- 为什么真实反馈仍为空。
- 为什么本 case 只能证明内部机制优化，不证明外部市场验证。
- `tool-ledger.md` 记录使用的技能、命令和工具结果质量。
- `flow-review.md` 记录剩余风险。

### 7. 更新导出和报告

运行：

```bash
python3 scripts/signalproof.py export-all
```

检查：

- `vault/reports/index.md`
- `vault/reports/index.html`
- 新 internal-audit case 的导出报告

如脚本导出仍重复太多，先记录为下一轮风险，不要在 Day 2 末尾大改导出器。

### 8. 最终验证命令

两天改造结束前运行：

```bash
python3 scripts/signalproof.py check-case 2026-06-22-signalproof-v0-2-两天收缩改造 --strict
python3 scripts/signalproof.py check-assets
python3 scripts/signalproof.py check-all
python3 scripts/signalproof.py export-all
python3 scripts/signalproof.py check-plugin-drift --no-codex
git diff --check
git status --short
```

如果 slug 不完全匹配，用：

```bash
python3 scripts/signalproof.py list
```

找到真实 case slug 后再运行 strict check。

## 两天内不做事项

- 不重写全部历史 case。
- 不强行清零所有历史 warning。
- 不引入 SQLite 或数据库。
- 不引入新的 Python 依赖。
- 不把 `report.md` 立刻从 AGENTS full 必需文件中删除，除非同步改完模板、脚本、导出和 skill。
- 不把内容商业实验写成 SignalProof 本体。
- 不把 `HyperFrames` 设成协议必需依赖。
- 不把插件安装数量写成能力或证据成立。
- 不把 `published` 写成 `validated`。
- 不因为完成 internal-audit case 就声称市场验证。

## 新窗口执行提示

复制下面整段给新 Codex 窗口：

```text
你现在在 /Users/rust/Documents/SignalProof 工作。请使用 signalproof、user-working-profile、session-handoff 相关规则，并先读取：

- /Users/rust/Documents/SignalProof/AGENTS.md
- /Users/rust/Documents/SignalProof/docs/signalproof-v0.2-two-day-refactor-plan.md
- /Users/rust/Documents/SignalProof/.agents/skills/signalproof/SKILL.md
- /Users/rust/.codex/skills/user-working-profile/SKILL.md

任务：按 docs/signalproof-v0.2-two-day-refactor-plan.md 在两天范围内完成 SignalProof V0.2 收缩改造。不要停在建议，直接修改仓库文件。

硬边界：

- 不做 Web App、SaaS dashboard、workflow builder、通用知识库、自动雷达、n8n/Dify、Notion/Obsidian 集成。
- 不重写全部历史 case，不强行清零历史 warning。
- 不把内部流程反馈、synthetic demo、assumed feedback、published-not-validated 写成市场验证。
- 不把插件安装数量等同于工具可用或证据成立。
- 保持本地 Markdown vault + Python 标准库脚本路线。

执行顺序：

1. 运行并记录：
   cd /Users/rust/Documents/SignalProof
   git status --short
   python3 scripts/signalproof.py check-all
   python3 scripts/signalproof.py check-plugin-drift --no-codex

2. 更新 README.md、docs/protocol.md、docs/current-flow.md、AGENTS.md、.agents/skills/signalproof/SKILL.md、plugins/signalproof/skills/signalproof/SKILL.md，使当前定位变成“SignalProof 个人证据协议”，full 变成有硬条件的升级事件，插件治理降级为候选能力。

3. 更新 templates/case/ 下的 signal/research/debate/decision/feedback/asset/tool-ledger/flow-review/process-log/report 模板，加入结构化 frontmatter 字段：research evidence fields、feedback_status、validation_status、asset_status、reuse_count 等。

4. 更新 vault/assets/registry.md，把它从资产目录升级为复用账本，新增 reuse_count、proof_of_reuse、reuse_cost_minutes、preconditions、public_or_private、supersedes、owner_scope。不要编造未知数据。

5. 修改 scripts/signalproof.py：
   - check-all 输出 failures/warnings 和 Overall status: passed / passed-with-warnings / failed。
   - check-case 支持结构化 frontmatter 检查。
   - strict 下结构化字段 warning 升级失败。
   - 新增 check-assets 命令，统计资产复用情况。

6. 创建并填写 internal-audit full case：
   python3 scripts/signalproof.py init-case "SignalProof V0.2 两天收缩改造" --case-type internal-audit --case-mode full

7. 运行最终验证：
   python3 scripts/signalproof.py list
   python3 scripts/signalproof.py check-case <真实case-slug> --strict
   python3 scripts/signalproof.py check-assets
   python3 scripts/signalproof.py check-all
   python3 scripts/signalproof.py export-all
   python3 scripts/signalproof.py check-plugin-drift --no-codex
   git diff --check
   git status --short

最终回复请给：

- 改了哪些文件；
- 新增了哪些脚本 gate；
- 哪些验证通过；
- 哪些仍是 warning 或历史债；
- 是否有用户已有 dirty changes 需要注意；
- 下一步是否可以开始跑 5 个 lite 外部信号实验。
```

## 验收口径

成功不是“所有历史 warning 清零”，而是：

- 新规则已经进入 docs、skills、templates、scripts。
- 新 strict case 能防止伪完成。
- `check-all` 不再给认知上的假全绿。
- `check-assets` 能暴露资产复用不足。
- 新 internal-audit case 记录了本轮改造边界。
- 任何真实反馈为空的状态都没有被写成市场验证。

## 交接提醒

当前工作树可能已有用户或其他线程改动。新窗口必须先看 `git status --short`，只改本计划相关文件，不回滚不相关变更。
