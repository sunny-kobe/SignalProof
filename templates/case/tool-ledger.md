---
type: tool_ledger
status: completed
updated_at: {{created_at}}
gate: passed
---

# 工具账本

## 候选能力账本

| 能力 | 候选原因 | 是否使用 | 结果质量 | 是否改变判断 | 下次动作 |
| --- | --- | --- | --- | --- | --- |
{{candidate_capability_rows}}

## 研究准确性账本

按 `docs/research-quality-gate.md` 记录研究阶段是否真的能支持结论，必须覆盖来源覆盖、交叉验证、反证、证据等级、结论许可和用户授权缺口：

| 检查项 | 是否覆盖 | 证据等级 | 说明 | 下一步 |
| --- | --- | --- | --- | --- |
{{tool_research_rows}}

## 阶段能力计划

运行：

```bash
python3 scripts/signalproof.py capabilities
```

然后把本 case 各阶段真正考虑过的 Codex 自带插件记录到这里：

| 阶段 | 候选 Codex 插件 | 实际使用 | 结果质量 | 是否改变判断 | 跳过或失败原因 |
| --- | --- | --- | --- | --- | --- |
{{stage_plugin_rows}}

## 能力结论

只有工具结果改变判断、减少不确定性或验收产物时，才算对本 case 有实质贡献。插件安装数量、候选数量或调用次数不能写成证据合格。
