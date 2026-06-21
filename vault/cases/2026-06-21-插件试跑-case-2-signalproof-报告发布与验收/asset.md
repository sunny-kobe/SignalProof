---
type: asset
status: reusable-internal
created_at: 2026-06-21
gate: passed
---

# 资产

## 资产名称

SignalProof 报告/页面验收降级策略

## 资产类型

验证插件使用规则 + 失败降级路线。

## 可复用内容

- Record & Replay 可作为“用户演示 -> Skill”默认候选。
- GitHub CLI 可作为公开仓库入口和 issue 反馈检查。
- Browser/Computer Use 失败时，先用文件级检查、runtime inspect、导出图片或人工复核降级。
- 不能把“文件存在”写成“浏览器验收通过”。

## 可复用边界

只适用于当前环境。修复 Browser/Computer Use 权限后，需要重新跑视觉/GUI 验收。
