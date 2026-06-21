# 用户授权和 API 开通清单

这份清单只记录当前 SignalProof 研究准确性流程真正需要用户本人处理的授权项。外部反馈、批量分发和产品行为数据暂时不做。

## A. 现在最该处理

| 优先级 | 项目 | 当前状态 | 为什么重要 | 用户需要做什么 | 页面或入口 |
| --- | --- | --- | --- | --- | --- |
| A1 | macOS Full Disk Access | done | `last30days --diagnose` 已不再输出 Safari cookie permission denied | 暂不需要处理 | `python3.14 .../last30days.py --diagnose` 已验证 |
| A3 | GitHub | done | 当前活跃账号是 `sunny-kobe`，权限覆盖 repo/workflow/gist/read:org | 暂不需要处理 | `gh auth status` 已验证 |

## B. 研究增强，按 case 开通

| 项目 | 适用场景 | 当前处理方式 | 页面 |
| --- | --- | --- | --- |
| Readwise | 需要把历史阅读、高亮、Reader 收藏变成研究证据 | 用户已网页登录；当前 Codex 工具面未暴露直接 connector，需具体 case 做只读探针 | <https://readwise.io/> |
| Scite | 关键论断需要论文支持或反证 | 用户已网页登录；当前 Codex 工具面未暴露直接 connector，需具体 case 做只读探针 | <https://scite.ai/> |
| Semrush | 内容选题、关键词、SEO、竞品站点热度 | 用户已网页登录；当前 Codex 工具面未暴露直接 connector，需具体域名/关键词 case 做只读探针 | <https://www.semrush.com/> |
| Similarweb | 竞品站点流量、访问来源、市场侧证 | 用户已网页登录；当前 Codex 工具面未暴露直接 connector，需具体域名 case 做只读探针 | <https://www.similarweb.com/> |
| Brand24 | 品牌/关键词公开提及和情绪 | 用户已网页登录；当前 Codex 工具面未暴露直接 connector，需具体关键词 case 做只读探针 | <https://brand24.com/> |
| Zotero | 论文和引用型资料管理 | 本地资料库存在时使用；不强制开通 | <https://www.zotero.org/> |

## C. 暂不必处理

| 项目 | 原因 |
| --- | --- |
| PostHog / Mixpanel / Amplitude | 属于产品行为反馈；当前外部反馈暂停，没有真实产品数据源。 |
| Sentry / Datadog | 属于运行态和错误反馈；当前没有线上实验需要查日志。 |
| Notion / Google Drive / Airtable / Deepnote | 只有当资料已经在这些系统里，或 Markdown vault 不够用时才接入。 |
| Vercel / Netlify / Cloudflare | 属于发布部署；当前批量分发和外部反馈暂停。 |
| 抖音 / TikTok / B 站 | 需要先设计批量分发工作流；当前不进入本轮。 |
| X API credits | X OAuth 已通，但搜索 credits 用尽；它只影响实时讨论和早期热度雷达，不阻断 SignalProof 主流程。后面只有当某个 case 明确依赖 X 讨论热度、KOL 转发或实时争议时，再提醒用户补 credits。 |

## D. Codex 可代做和不能代做

Codex 可以：

- 打开登录页面或系统设置页；
- 跑 `diagnose`、`capabilities`、`check-all`、`check-goal`；
- 做只读探针；
- 把授权成功或失败写入 `tool-ledger.md`；
- 在具体 case 中按研究质量门补证。

Codex 不能替你完成：

- macOS 权限开关；
- X、Readwise、Scite、Semrush、Similarweb、Brand24 等账号登录；
- 付费订阅开通；
- 二次验证、短信、邮箱验证码；
- 把未授权或 0 结果写成“没有需求”。

## E. 最新复核结果

复核时间：2026-06-21。

- GitHub：`sunny-kobe` 是当前活跃账号，状态 `done`。
- Full Disk Access：`last30days --diagnose` 已无 Safari cookie permission denied，状态 `done`。
- X / xurl：`xurl whoami` 成功返回 `sunnykobe183863`，OAuth 状态 `done`；`xurl search` 返回 `CreditsDepleted`，搜索状态标记为 `暂缺但非阻断`。当前不建议为它单独付费，后续遇到高度依赖 X 实时讨论的 case 再提醒用户补 credits。
- last30days：可用来源仍包含 X，但实际 X 检索会因 credits 返回 0，研究时必须标成来源缺口。
- Readwise / Scite / Semrush / Similarweb / Brand24：网页登录由用户完成；当前会话没有暴露可直接调用这些 app connector 的工具入口，只有插件清单。必须在具体研究 case 中做只读探针，成功后才写入证据链。
- Chrome 标签页复查：Codex Chrome 插件层当前只枚举到 1 个相关标签页，即 GitHub `sunny-kobe/BestBlogs`；本机 Chrome 窗口清单能看到 X Premium 和 Readwise Quick，但没有看到 Scite、Semrush、Similarweb、Brand24 当前打开页。结论仍是：网页登录完成不等于 Codex connector 已可稳定读取。
