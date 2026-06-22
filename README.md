# SignalProof

SignalProof 是一个本地优先的个人证据协议，用来把外部信号压成可审计证据、明确决策和可复用资产。

`Personal Opportunity OS` 只是长期背景叙事，不是当前执行范围。V0.2 的执行名是 `SignalProof 个人证据协议`：它不是 Web App、SaaS dashboard、workflow builder、通用知识库、自动雷达或插件平台。

当前范围：

- Codex 是主执行界面。
- SignalProof 提供协议、模板、本地 vault 结构、脚本和后续插件包骨架。
- 事实来源是 `vault/` 的 Markdown 和 `scripts/` 的确定性检查。
- 插件只是候选能力，只有在改变判断、减少不确定性或验收产物时才进入 case。

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

## Case Mode

新外部机会默认从 `case_mode: lite` 开始。lite case 只用于快速判断是否继续、收窄、暂停、放弃或升级，不代表完整 proof。

`case_mode: full` 是有硬条件的升级事件，不能为了“流程完整”默认创建。外部机会升级为 full 前必须同时满足：

- `research.md` 的 `evidence_grade` 至少为 `medium`；
- 有明确外部动作：发布、访谈、私信测试、下载页、表单回收或真实目标人反馈；
- 至少有一个可登记资产候选；
- `decision.md` 写明为什么需要 full。

internal-audit / plugin-test / external-opportunity 必须在 `signal.md` 的 `case_type` 或正文中分清。内部流程反馈、synthetic demo、assumed feedback 和 published-not-validated 都不能写成市场验证。

## 常用命令

```bash
python3 scripts/signalproof.py diagnose
python3 scripts/signalproof.py capabilities
python3 scripts/signalproof.py list
python3 scripts/signalproof.py check-all
python3 scripts/signalproof.py check-assets
python3 scripts/signalproof.py export-all
```

本地自动化使用 Python 3.9+ 即可。本机运行 `last30days` 时使用 `python3.14`。

## 当前边界

这个仓库能证明本地个人证据协议是否更可执行。只有收集到真实发布、真实用户反馈和真实 before/after 证据后，才能进入外部验证判断；插件安装数量、报告导出数量或 case 文件完整度都不能替代证据质量。

## 流程说明

- 当前执行流程：[docs/current-flow.md](docs/current-flow.md)
- Codex 自带插件接入计划：[docs/codex-plugin-flow.md](docs/codex-plugin-flow.md)
