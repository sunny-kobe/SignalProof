# SignalProof 协议 MVP

## 定位

SignalProof 在第一阶段是 Codex 协议和未来插件包，不是独立 App。

```text
Codex = 主界面、执行者、研究者、写作者、验收者
SignalProof = 协议、模板、vault、脚本、能力账本
其他 skills/plugins = 分阶段调用的能力
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

Codex 插件不是默认全跑能力。每个 case 先看阶段目标，再按 [`docs/codex-plugin-flow.md`](codex-plugin-flow.md) 选择能改变判断、减少不确定性或验收产物的插件。

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
