---
type: validation
status: planned
updated_at: 2026-06-21
gate: passed
---

# 验证计划

## 验证对象

验证 `docs/codex-plugin-audit.md` 中的 A 级推荐插件能否真实服务 SignalProof，而不是只停留在候选清单。

## 多 case 试跑设计

| 子 case | 目标 | 覆盖插件 | 成功标准 |
| --- | --- | --- | --- |
| Case A：安装与官方口径 | 验证推荐插件是否装好、官方如何定义插件能力 | `codex plugin list`、OpenAI Docs、plugin manifests | 能区分 Skill / App / MCP / runtime |
| Case B：调研类公开只读 | 验证调研插件是否能拿到真实外部信号 | GitHub、Hugging Face、Zotero、Readwise/Scite/Semrush 等 | 至少有公开只读成功或明确 auth/tool 阻塞 |
| Case C：验证类插件 | 验证页面/GUI/录制类能力是否可作为默认验收 | Browser、Computer Use、Record & Replay | 成功调用或记录失败错误 |
| Case D：产物类插件 | 验证插件能否生成可复用资产 | Spreadsheets、Data Visualization、Documents、PDF、Presentations、HyperFrames | 至少生成一个可检查产物并记录依赖缺口 |
| Case E：反馈/数据类插件 | 验证产品分析/运行态插件是否可用 | PostHog、Mixpanel、Amplitude、Sentry、Datadog | 有数据源则读取；无授权则标阻塞 |

## 本轮执行结果

- Case A：通过。36 个 marketplace 插件已安装启用，4 个 runtime 插件可用。
- Case B：部分通过。GitHub、Hugging Face 公开只读可用；`last30days` 成功补到 GitHub/Reddit/YouTube 证据但来源缺口明显；Zotero 本地 App 未运行；Readwise/Scite/Semrush/Similarweb/Brand24 当前无 connector 工具入口。
- Case C：部分通过。Record & Replay 状态查询成功；Browser setup 失败；Computer Use 的 `list_apps` 成功，但具体 App 状态读取曾因 macOS 权限失败，不能作为默认硬验收。
- Case D：通过但有依赖缺口。Spreadsheets、Data Visualization、Documents、PDF、Presentations、HyperFrames 均已生成实际产物；缺 LibreOffice/Poppler/ffmpeg 导致部分渲染或视频导出未完成。
- Case E：阻塞。PostHog/Mixpanel/Amplitude/Datadog/Sentry 缺少当前线程 app 工具或 API key。

## 成功标准

- 不能把“已安装”写成“已产生证据”。
- 每个插件组必须给出结果：默认用、条件用、暂不默认。
- 对 auth/tool 缺失写明阻塞原因，不当作 0 结果。
- 运行 `python3 scripts/signalproof.py check-all` 和 `python3 scripts/signalproof.py export-all`。
