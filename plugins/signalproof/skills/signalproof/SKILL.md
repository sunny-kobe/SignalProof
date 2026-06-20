---
name: signalproof
description: 运行 SignalProof 信号到资产证明案例，维护工具账本、过程日志、流程自检，并导出报告。用于个人机会工作流验证和 Codex 协议审计。
---

# SignalProof Plugin Skill

SignalProof 是一套 Codex 优先的工作流协议。

调用时，创建或更新一个本地 case，并覆盖：

- 信号捕捉；
- 研究；
- 反方审查；
- 判断；
- 验证计划；
- 产物；
- 反馈边界；
- 决策；
- 资产；
- 流程自检；
- 工具账本；
- 过程日志。

除非存在真实用户反馈，否则不要声称市场验证。

每个阶段开始前，先用能力矩阵判断是否需要 Codex 自带插件：

- Browser / Chrome：网页、登录态页面、发布页和报告预览；
- Computer Use：只能通过 GUI 操作或验收的流程；
- Record & Replay：用户演示的真实流程，需要沉淀成 Skill；
- Documents / PDF / Spreadsheets / Presentations：对应格式的资料包、报告、表格和演示文稿；
- Data Visualization / HyperFrames：研究数据可视化或传播型网页/视频表达。

不要默认全跑插件。只在它能改变判断、减少不确定性或验收产物时调用，并把候选、使用、结果质量、跳过原因写入 `tool-ledger.md`。
