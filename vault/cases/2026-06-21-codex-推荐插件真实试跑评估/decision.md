---
type: decision
status: accepted-internal
decision: continue-internal-protocol-validation
updated_at: 2026-06-21
gate: passed
---

# 决策

## 决策

插件不是越多越好。当前推荐插件应分三层使用：

| 层级 | 插件 | 决策 |
| --- | --- | --- |
| 默认进入 SignalProof 流程 | GitHub、Record & Replay、Spreadsheets、Data Visualization、OpenAI Docs、SignalProof skill | 确实能提升流程质量，直接保留 |
| 真实趋势 case 默认候选 | last30days | 能补最近真实讨论，但必须记录来源缺口和证据强度 |
| 条件进入专项 case | Hugging Face、Zotero、Documents、PDF、Presentations、HyperFrames、Sentry、PostHog、Mixpanel、Amplitude、Datadog、Semrush、Similarweb、Brand24、Readwise、Scite、Dovetail、Mem、Notion、Google Drive、Airtable、Linear、Figma、Canva、Vercel、Netlify、Cloudflare | 有潜力，但需要账号、授权、真实数据源、交付场景、依赖补齐或新线程工具暴露 |
| 暂不设为默认依赖 | Browser、Computer Use | Browser 当前环境调用失败；Computer Use 入口可响应但读取具体 App 可能受权限影响，先作为条件候选，不作为完成验收的硬依赖 |

## 为什么不是“全部默认用”

- App connector 类插件大多依赖账号授权和外部数据源，没有授权时不能提供证据。
- Browser 当前实际调用失败；Computer Use 需要先确认目标 App 权限，如果写成默认硬依赖会让流程不稳定。
- 对 SignalProof 来说，插件必须改变判断、降低不确定性或生成可复用资产；只增加炫技调用没有价值。

## 下一步

- 真实市场/趋势 case：优先用 `last30days` + GitHub + Browser/公开网页，必要时再加 Semrush/Similarweb/Brand24。
- 真实产品反馈 case：只有接入 PostHog/Mixpanel/Amplitude/Sentry/Datadog 后再启用反馈插件。
- 用户演示流程：优先用 Record & Replay 录制，再沉淀为 Skill。
- 文件资产化：默认使用 Spreadsheets/Data Visualization；Documents/PDF/Presentations 在需要正式交付件时启用，HyperFrames 在需要短视频或动态叙事时启用。

## 边界

本轮是真实插件试跑评估，不是市场验证。真实反馈为空，不能声称需求已验证。
