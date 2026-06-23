# SignalProof 个人证据协议

## 定位

SignalProof 当前执行名是 `SignalProof 个人证据协议`。它是本地 Markdown vault + Python 标准库脚本 + Codex 执行习惯组成的个人判断协议，不是独立 App、SaaS dashboard、workflow builder、通用知识库、自动雷达或插件平台。

`Personal Opportunity OS` 是长期背景叙事，只解释为什么要把信号、证据、决策和资产放在同一条链路里；它不作为 V0.2 的执行口号，也不扩展当前仓库范围。

```text
Codex = 主界面、执行者、研究者、写作者、验收者
SignalProof = 个人证据协议、模板、vault、脚本、资产复用账本
其他 skills/plugins = 分阶段调用的候选能力
用户 = 判断者、发布者、最终拍板者
```

## 工作流

1. 捕捉一个信号。
2. 研究信号，并区分事实、推断和缺口。
3. 做一次真实的反方审查。
4. 给出判断：继续、收窄、暂停或放弃。
5. 创建验证计划。
6. 生产产物。
7. 记录反馈。这个 MVP 里真实反馈可以为空，但必须明确写出。
8. 基于证据强度做决策。
9. 把有效输出沉淀成可复用资产。
10. 做流程自检并更新工具账本。

资产沉淀不只是在 `asset.md` 写“可复用”。真正可复用的资产必须登记到 `vault/assets/registry.md`，并在后续 case 使用时更新 `last_used_by`，否则只能算资产候选。

## Case 类型

默认 case 类型是 `external-opportunity`，用于真实外部机会初筛。内部流程审计、工作流优化、插件流程复核和二次审视类任务使用：

```bash
python3 scripts/signalproof.py init-case "<标题>" --case-type internal-audit
```

`internal-audit` 只能支持本地机制改进和流程决策，不能写成外部市场验证。`plugin-test` 只能证明插件调用路径、授权缺口或产物验收能力。`external-opportunity` 才能进入外部机会判断，但也必须区分 published、observed feedback 和 validated。

## Case Mode

SignalProof 分两种 case mode：

- `lite`：新外部机会的默认模式，用于信号初筛、快速反方判断和资产候选登记。只要求 `signal.md`、`research.md`、`debate.md`、`decision.md`、`asset.md`。lite 的目标是判断是否继续、收窄、暂停、放弃或升级，不代表完整 proof。
- `full`：有硬条件的升级事件。只有当证据等级至少为 `medium`、存在明确外部动作、至少有一个可登记资产候选，并且 `decision.md` 说明为什么需要 full 时，外部机会才升级为 full。internal-audit 可以使用 full 来记录完整机制改造，但不能写成市场验证。

lite case 的资产可以被发布，但发布 URL 只说明外部动作发生，不自动构成 full proof。发布后先在发布资产、发布台账、`asset.md` 或 `decision.md` 记录 `validation_status=published`、`feedback_status=published-no-feedback` 或真实反馈状态；只有满足 full 升级硬条件时，才补齐 `feedback.md`、`validation.md`、`artifact.md`、`flow-review.md`、`tool-ledger.md`、`process-log.md` 和 `report.md`。

创建轻量 case：

```bash
python3 scripts/signalproof.py init-case "<标题>" --case-mode lite
```

创建完整内部审计 case：

```bash
python3 scripts/signalproof.py init-case "<标题>" --case-type internal-audit --case-mode full
```

已有内部工作流优化和插件试跑 case 属于个人工作流测试样本，可以保留；它们证明机制改进，不证明外部机会成立。

## Gate 状态

```text
not-started / running / weak / passed / blocked
```

弱证据可以让 case 进入低成本内部实验，但不能证明需求成立，不能支持产品化，也不能支持 SaaS 结论。

## 研究准确性质量门

研究阶段必须按 [`docs/research-quality-gate.md`](research-quality-gate.md) 执行。最低要求不是“跑过搜索”或“跑过插件”，而是记录：

- 来源覆盖：公开讨论、项目和数据、官方和一手资料、反证和替代方案；
- 交叉验证：谁在说、说什么、在哪里说、有没有反证、能支持什么结论；
- 证据等级：strong / medium / weak / blocked；
- 结论许可：继续研究、低成本实验、暂停或放弃。

如果研究证据只有 weak 或 blocked，后续只能进入补研究或低成本内部实验，不能写成真实需求成立。

新 case 完成前建议运行严格检查：

```bash
python3 scripts/signalproof.py check-case <case-slug> --strict
```

严格检查会把 warning 也当成失败，用于防止新 case 把研究质量门缺口留给人工记忆。历史 case 可以继续由 `check-all` 保持 warning，以免一次性破坏旧材料。

严格检查同时会识别未完成占位标记，例如 `TODO`、`TBD`、`待补`、`待定` 和未替换的 `{{变量}}`。这些标记可以出现在模板和历史材料中，但不能留在声称完成的新 case 里。

## 必需审计文件

`tool-ledger.md` 记录：

- 候选能力；
- 实际使用情况；
- 结果质量；
- 跳过能力和原因；
- 下一次要尝试的能力。

`process-log.md` 记录：

- 使用过的命令和工具；
- 迭代过程；
- 自检结果；
- 优化记录。

`flow-review.md` 记录：

- 阶段完整性；
- 证据质量；
- 过度声称风险；
- 下一次流程改进。

## 插件和可迁移性

Codex 插件在 V0.2 降级为候选能力。每个 case 先看阶段目标，再按 [`docs/codex-plugin-flow.md`](codex-plugin-flow.md) 选择能改变判断、减少不确定性或验收产物的插件。插件安装数量、marketplace 可见性和状态快照都不能证明工具可用、账号已授权或证据成立。

判断插件是否装好、为什么界面里看不到、以及哪些部分能随 SignalProof 仓库迁移时，执行：

```bash
python3 scripts/signalproof.py plugin-status
```

并以 [`docs/codex-plugin-status-and-migration.md`](codex-plugin-status-and-migration.md) 和 [`docs/codex-plugin-lock.md`](codex-plugin-lock.md) 为准。当前规则是：repo skill、repo plugin、repo marketplace、模板、文档、vault、插件锁定清单和重装脚本可以迁移；本机 `~/.codex/config.toml`、官方插件缓存、OAuth、浏览器 cookie 和 API key 不随仓库迁移。

后续新增/移除插件，或某个插件从“条件触发”变成“默认候选”时，必须同步更新：

- `docs/codex-plugin-lock.md`
- `scripts/install-codex-plugins.sh`
- `docs/codex-plugin-status-and-migration.md`
- 当天的 `python3 scripts/signalproof.py plugin-status` 快照
