---
type: validation
status: completed
updated_at: 2026-06-21
gate: passed
---

# 验证计划

## 验证对象

SignalProof 是否能把“报告里发现的缺口”升级成脚本、模板或文档中的可复用机制。

## 验证方式

1. 复核最近自审 case 和报告。
2. 修改 `scripts/signalproof.py`、模板、协议或 skill。
3. 新建或更新本次内部审计 case。
4. 运行 `python3 scripts/signalproof.py check-plugin-drift`。
5. 运行 `python3 scripts/signalproof.py check-case <case-slug> --strict`。
6. 运行 `python3 scripts/signalproof.py export-all`、`check-all`、`check-goal --min-cases 5` 和 `git diff --check`。

## 跳过项

- 真实外部反馈：本轮跳过。
- 发布渠道：本轮跳过。
- Browser / Chrome / Computer Use / Record & Replay：本轮没有网页、登录态、GUI 或录制验收目标。
- Documents / PDF / Spreadsheets / Presentations：本轮交付物是 Markdown、模板和 Python 脚本，不需要格式插件验收。

## 成功标准

自检通过，并且流程自检能指出至少一个下一轮优化点。

## 已完成验证

| 验证项 | 结果 | 判断 |
| --- | --- | --- |
| Python 语法检查 | `python3 -m py_compile scripts/signalproof.py` 通过 | passed |
| 新 case 类型生成 | `init-case ... --case-type internal-audit --force` 生成完整 case | passed |
| 占位 strict 检查 | 第一次 strict 抓到 `待定` 残留，修正模板后通过 | passed |
| 原报告复核 | 确认原报告部分准确，但内部审计模板和占位检查仍未落地 | passed-with-gaps |
| 插件调用质量 | 本轮未调用外部 connector；原因是不会改变内部脚本判断，不能写成插件证据 | passed |

## 最终验证命令

最终验证以本 case 完成后的命令输出为准：

```bash
python3 scripts/signalproof.py check-plugin-drift
python3 scripts/signalproof.py check-case 2026-06-21-signalproof-工作流优化二次审视 --strict
python3 scripts/signalproof.py export-all
python3 scripts/signalproof.py check-all
python3 scripts/signalproof.py check-goal --min-cases 5
git diff --check
```

## 最终验证结果

| 命令 | 结果 | 说明 |
| --- | --- | --- |
| `python3 scripts/signalproof.py check-plugin-drift` | passed | 锁定清单 36、安装脚本 36、当天状态快照脚本 36、当天状态快照已安装 36、当前 `codex plugin list` 已安装 36，全部一致。 |
| `python3 scripts/signalproof.py check-case 2026-06-21-signalproof-工作流优化二次审视 --strict` | passed | 本次 case 无 warning，无未完成占位标记。 |
| `python3 scripts/signalproof.py export-all` | passed | 导出 13 份报告并更新报告索引。 |
| `python3 scripts/signalproof.py check-all` | passed-with-warnings | 13 个 case，failures 0；旧 case 暴露历史占位和研究质量门 warning。 |
| `python3 scripts/signalproof.py check-goal --min-cases 5` | passed | cases: 13；报告索引存在。 |
| `git diff --check` | passed | 无空白错误。 |

## 验证解释

这些命令证明本轮内部工作流机制已落地并通过本地检查；它们不证明外部账号授权成功，也不证明 connector 可读取真实数据，更不证明市场需求成立。
