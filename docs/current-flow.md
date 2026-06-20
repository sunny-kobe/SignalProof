# 当前执行流程

这份文档记录 SignalProof 现在每个流程是怎么跑的，以及本轮新增的 Codex 自带插件接入点。

## 1. 能力诊断

命令：

```bash
python3 scripts/signalproof.py diagnose
```

作用：

- 记录本机 Python 版本；
- 检查 `last30days` 脚本是否存在；
- 尝试运行 `last30days --diagnose`；
- 输出到 `vault/runs/<date>-capability-snapshot.json`。

当前边界：

- 这是环境诊断，不代表研究证据合格。
- 如果某个来源失败，只能写成能力缺口，不能写成反证。

## 2. Codex 能力矩阵

命令：

```bash
python3 scripts/signalproof.py capabilities
```

作用：

- 检测本机可用的 Codex 自带插件；
- 输出阶段到插件的能力矩阵；
- 写入 `vault/runs/<date>-codex-capability-matrix.md`。

本轮新增的插件候选：

- Browser；
- Chrome；
- Computer Use；
- Record & Replay；
- Documents；
- PDF；
- Spreadsheets；
- Presentations；
- Data Visualization；
- HyperFrames。

使用原则：

- 不默认全跑；
- 只在能改变判断、减少不确定性或验收产物时调用；
- 使用、跳过、失败都写入 `tool-ledger.md`。

## 3. 创建 Case

命令：

```bash
python3 scripts/signalproof.py init-case "<title>"
```

作用：

- 从 `templates/case/` 创建完整 case 文件；
- 必需文件包括 `signal.md`、`research.md`、`debate.md`、`thesis.md`、`validation.md`、`artifact.md`、`feedback.md`、`decision.md`、`asset.md`、`flow-review.md`、`tool-ledger.md`、`process-log.md`、`report.md`。

当前边界：

- `init-case` 只生成结构，不自动判断证据；
- 是否调用插件由阶段能力计划决定。

## 4. Seed 示例案例

命令：

```bash
python3 scripts/seed_cases.py
```

作用：

- 生成 5 个差异化内部案例；
- 每个案例都带工具账本、流程自检和过程日志；
- 真实反馈和发布渠道保持为空。

当前边界：

- seed 只证明内部协议闭环，不证明市场需求。
- seed 内容会覆盖对应 case 的顶层文件，不覆盖 legacy 目录。

## 5. Case 自检

命令：

```bash
python3 scripts/signalproof.py check-all
```

作用：

- 检查必需文件是否存在；
- 检查真实反馈为空时是否过度声称；
- 检查 `tool-ledger.md` 是否覆盖关键能力和结果质量；
- 检查 `process-log.md` 是否包含迭代、命令、自检和优化。

当前边界：

- 它是结构和风险语言检查；
- 不替代真实市场验证。

## 6. 导出报告

命令：

```bash
python3 scripts/signalproof.py export-all
```

作用：

- 把每个 case 导出到 `vault/reports/*.md`；
- 生成 `vault/reports/index.md` 和 `vault/reports/index.html`。

当前边界：

- HTML 报告索引可以用 Browser 验收；
- 当前脚本只做文件级导出，不做视觉渲染判断。

## 7. MVP 目标检查

命令：

```bash
python3 scripts/signalproof.py check-goal --min-cases 5
```

作用：

- 检查至少 5 个 case；
- 检查报告索引；
- 检查能力快照；
- 检查 Codex 能力矩阵；
- 检查 legacy 迁移；
- 检查插件 marketplace；
- 检查每个 case 的反馈边界、工具账本和优化记录。

当前边界：

- 通过表示内部协议 MVP 成立；
- 不表示真实反馈、真实发布或市场验证成立。

## 下一步增量

下一步不应该一次性接入所有插件，而是选一个真实 case 做单点验证：

1. 用 Browser 验收 `vault/reports/index.html`；
2. 把结果写回 `flow-review.md` 和 `tool-ledger.md`；
3. 再考虑 Documents/PDF/Spreadsheets/Presentations 这类产物插件。
