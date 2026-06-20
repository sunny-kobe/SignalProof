---
type: asset
status: reusable
updated_at: 2026-06-20
gate: passed
---

# 资产

## 可复用资产名称

SignalProof 插件实际调用验证循环。

## 资产内容

```text
能力矩阵
-> 选择阶段候选插件
-> 读取对应 Skill
-> 真实调用插件
-> 记录原始结果
-> 判断结果质量
-> 记录失败和影响
-> 选择降级路径
-> 更新 tool-ledger.md
-> 更新 flow-review.md
-> 进入下一轮优化
```

## 可复用 prompt

```text
请按 SignalProof 的插件实际调用流程推进这个案例：
1. 先运行 capabilities，列出本阶段候选 Codex 插件；
2. 只选择一个会改变判断或验收结果的插件；
3. 读取该插件对应 Skill 后真实调用；
4. 把成功、失败、错误信息、结果质量和降级动作写入 tool-ledger.md；
5. 在 flow-review.md 写清楚这次工具覆盖是否足够，以及下次要补跑什么；
6. 真实反馈为空时，不要写成外部需求已被证实。
```

## 适用场景

- Browser 验收本地 HTML 或公开页面。
- Computer Use 读取本机图形界面状态。
- Chrome 读取用户已登录页面。
- Documents、PDF、Spreadsheets、Presentations 验收非 Markdown 产物。
- Record & Replay 沉淀用户演示流程。

## 不适用场景

- 单纯写 Markdown 文件。
- 不需要工具证据的纯判断。
- 外部市场反馈为空但想快速包装对外说法。

## 维护方式

每新增一个插件真实调用案例，就把本资产里的步骤和失败分类补充一次。
