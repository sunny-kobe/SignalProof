---
type: process_log
status: completed
updated_at: 2026-06-21
gate: passed
---

# 过程日志

## Iteration / 迭代 1：确认规则

Command / 命令：

```bash
sed -n '1,240p' .agents/skills/signalproof/SKILL.md
sed -n '1,220p' /Users/rust/.codex/skills/user-working-profile/SKILL.md
sed -n '1,220p' AGENTS.md
```

结果：

- 确认本仓库事实来源是 `vault/` Markdown 和 `scripts/` 确定性检查。
- 确认每个 case 需要 13 个必需文件。
- 确认文档默认中文，真实反馈为空也必须写清楚。

## Iteration / 迭代 2：读取流程文档

Command / 命令：

```bash
sed -n '1,260p' docs/protocol.md
sed -n '1,260p' docs/research-quality-gate.md
sed -n '1,260p' docs/codex-plugin-flow.md
sed -n '1,260p' docs/codex-plugin-status-and-migration.md
```

结果：

- 确认插件不是默认全跑。
- 确认研究质量门要求来源覆盖、交叉验证、反证、证据等级、结论许可和用户授权缺口。
- 确认插件迁移要区分 repo 资产、本机配置、缓存和外部凭据。

## Iteration / 迭代 3：运行诊断

Command / 命令：

```bash
python3 scripts/signalproof.py diagnose
python3 scripts/signalproof.py capabilities
python3 scripts/signalproof.py plugin-status
python3.14 /Users/rust/.agents/skills/last30days/scripts/last30days.py --diagnose
```

结果：

- `diagnose` 成功。
- `capabilities` 成功生成阶段能力矩阵。
- `plugin-status` 成功生成插件状态快照。
- `last30days --diagnose` 成功，但 X / bird 侧不是完整授权态。

## Iteration / 迭代 4：运行当前目标检查

Command / 命令：

```bash
python3 scripts/signalproof.py check-all
python3 scripts/signalproof.py check-goal --min-cases 5
```

结果：

- `check-all` 对 11 个旧 case 返回 failures 0。
- 多个旧 case 出现研究质量门 warning。
- `check-goal` 通过，报告索引存在。

## Iteration / 迭代 5：创建自审 case

Command / 命令：

```bash
python3 scripts/signalproof.py init-case "SignalProof 当前工作流自审"
```

结果：

```text
vault/cases/2026-06-21-signalproof-当前工作流自审/
```

## Self-check / 自检

本轮自检问题：

- 是否把内部流程反馈写成外部反馈？没有。
- 是否把插件安装写成 connector 可读？没有。
- 是否把 X 侧缺口写成“没有需求”？没有。
- 是否把 `check-all` 通过写成所有 case 质量满分？没有。
- 是否默认全跑插件？没有。

## Optimization / 优化记录

第一轮没有立刻修改脚本新增命令，因为先要证明现有工作流能完成自审。

二次验收后已经完成两项优化：

- 增加 `check-plugin-drift`，把插件锁定清单、安装脚本、当天状态快照和当前安装列表的漂移检查脚本化。
- 增加 `check-case <case-slug> --strict`，让新 case 可以把 warning 当成失败，减少研究质量门只靠人工记忆的问题。

剩余优化候选：

- 给内部审计类 case 增加更合适的默认模板。
- 对一个真实 connector 做只读探针。
- 选择一个真实外部机会 case，补完整来源覆盖。
