# 报告

## 摘要

`SignalProof 工作流优化二次审视` 已跑完 SignalProof 内部协议闭环。

## 本次判断

原自审报告基本准确，但不是完整闭环。

- 准确：它判断当前流程是 `passed-with-gaps`，并正确区分插件安装、工具暴露、账号授权和证据质量。
- 准确：它没有把真实反馈为空写成市场验证。
- 准确：它已把 `check-plugin-drift` 和 `check-case --strict` 落到脚本，不是只写复盘。
- 不足：它没有把内部审计 case 类型落到 `init-case`，也没有让 strict 识别 `待补`、`待定` 和未替换模板变量。

## 实际改进

- `scripts/signalproof.py` 新增未完成占位标记检查。
- `scripts/signalproof.py` 的 `init-case` 新增 `--case-type internal-audit`。
- `templates/case/` 按 case 类型渲染，不再让内部审计默认套外部机会验证话术。
- `AGENTS.md`、repo skill、`docs/protocol.md`、`docs/research-quality-gate.md` 同步写入新规则。

## 仍待验证

- 真实外部反馈为空。
- 调研增强 connector 仍未在具体 case 中证明可读。
- 旧 case 的历史 warning 和占位痕迹未批量修复。
- 本轮不证明市场需求、用户采用、产品化或 SaaS 可行。

## 边界

本报告只证明内部工作流机制完成一次优化，不证明外部用户需求、市场采用或产品化可行性。

## 下一步

运行：

```bash
python3 scripts/signalproof.py check-all
python3 scripts/signalproof.py export-all
```
