# SignalProof

SignalProof 是一套 Codex 优先的个人工作流协议，用来把机会信号转成可复用的证明资产。

当前范围：

- Codex 是主执行界面。
- SignalProof 提供协议、模板、本地 vault 结构、脚本和后续插件包骨架。
- 本轮内部 MVP 故意跳过真实外部反馈和发布渠道。

## 仓库内容

```text
docs/                         协议说明和能力地图
scripts/signalproof.py         可重复运行的本地自动化脚本
templates/case/                case 文件模板
vault/cases/                   证明案例
vault/assets/                  case 产出的可复用资产
vault/reports/                 导出的案例报告和审计
vault/runs/                    run 级过程日志
.agents/skills/signalproof/    repo 级 Codex skill
plugins/signalproof/           Codex 插件草案包
```

## 案例生命周期

```text
信号 -> 研究 -> 辩论 -> 判断 -> 验证计划 -> 产物 -> 反馈 -> 决策 -> 资产 -> 流程自检
```

每个 case 还必须包含：

- `tool-ledger.md`：候选能力覆盖和结果质量。
- `process-log.md`：执行步骤、自检和优化记录。
- `report.md`：简洁的导出报告。

## 常用命令

```bash
python3 scripts/signalproof.py diagnose
python3 scripts/signalproof.py capabilities
python3 scripts/signalproof.py list
python3 scripts/signalproof.py check-all
python3 scripts/signalproof.py export-all
```

本地自动化使用 Python 3.9+ 即可。本机运行 `last30days` 时使用 `python3.14`。

## 当前边界

这个仓库能证明内部协议闭环已经跑通。只有收集到真实发布、真实用户反馈和真实 before/after 证据后，才能进入市场验证判断。

## 流程说明

- 当前执行流程：[docs/current-flow.md](docs/current-flow.md)
- Codex 自带插件接入计划：[docs/codex-plugin-flow.md](docs/codex-plugin-flow.md)
