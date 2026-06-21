---
type: flow_review
status: completed
updated_at: 2026-06-21
case_stage: full-internal-loop
gate: passed
---

# 流程自检

## 阶段完整性

| 阶段 | 状态 | 说明 |
| --- | --- | --- |
| signal | passed | 已记录原始信号。 |
| research | weak | `last30days` 有真实外部来源，但覆盖缺口明显。 |
| debate | passed | 已记录正反方。 |
| thesis | passed | 已明确继续内部验证。 |
| validation | passed | 已定义自检方式。 |
| artifact | passed | 已保存 `last30days` 原始输出和中文判断。 |
| feedback | weak | 真实反馈为空。 |
| decision | passed | 未过度声称。 |
| asset | passed | 已沉淀内部资产。 |

## 证据质量

- 中：Reddit/YouTube/GitHub 有真实命中，能提示方向和痛点。
- 弱：X/HN/短视频缺失，且多条结果是泛 AI coding 噪音。
- 失败/阻塞：X 额度耗尽、YouTube 评论 402、Reddit public API 403 fallback。

## 过度声称检查

没有把真实反馈为空写成验证成功。

## 插件结论

`last30days` 应进入 SignalProof 调研阶段默认候选，但必须加质量门：来源不足、query 跑偏或关键渠道失败时，只能写 `weak`，不能推进到“已验证需求”。

## 优化空间

- 下一轮用更窄 query 补跑，例如 `AI coding agent ignores repo instructions`、`Claude Code project context stale`。
- 对 X/HN 缺失单独走 GitHub/HN/RSS 或浏览器补查，而不是把缺失当作没人讨论。
- 如果出现具体候选项目，再用 GitHub、Hugging Face 或官方文档做项目级验证。
