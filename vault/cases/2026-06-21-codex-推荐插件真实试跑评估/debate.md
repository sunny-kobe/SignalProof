---
type: debate
status: completed
updated_at: 2026-06-21
gate: passed
---

# 辩论

## 正方

- 插件试跑能让 SignalProof 不再只靠泛化 prompt，而是按阶段调用真实工具。
- GitHub、last30days、Record & Replay、Spreadsheets、Data Visualization、Documents/PDF/Presentations/HyperFrames 已经证明能把信号、调研、验证、产物、资产化串起来。
- App connector 类插件虽然当前受阻，但一旦授权，能把 Readwise、Scite、PostHog、Sentry 等私有/实时证据接入 case。

## 反方

- 插件越多，越容易让流程从“判断机会”变成“为了调用而调用”。
- 很多调研/反馈插件依赖账号授权和真实数据源；没有授权时，安装本身没有任何证据价值。
- Browser 有历史失败记录，Computer Use 读取具体 App 仍受权限影响，如果强行作为默认验收，会降低流程稳定性；后续按具体网页验收目标重新做只读探针。
- 产物类插件容易制造漂亮文件，但不一定改变决策。

## 最强反对意见

“全部推荐插件都装上并调用一次”不是好目标。真正目标应该是识别哪些插件能降低不确定性、改变判断或沉淀资产。

## 收窄后的判断

继续插件化，但只保留三层策略：默认用、条件用、暂不默认。没有授权或真实数据源的插件不进入默认流程。
