---
type: artifact
status: created
updated_at: 2026-06-21
gate: passed
---

# 产物

## 本轮产物

| 产物 | 路径 | 用途 |
| --- | --- | --- |
| 插件评估工作簿 | `vault/assets/plugin-test/workbook/outputs/plugin-eval-workbook.xlsx` | 用表格形式沉淀插件组、证据、影响等级和建议 |
| 工作簿预览图 | `vault/assets/plugin-test/workbook/outputs/plugin-eval-workbook-preview.png` | 验证表格可读性 |
| 工作簿 inspect | `vault/assets/plugin-test/workbook/outputs/inspect.ndjson` | 保存 Spreadsheets runtime 的结构化检查结果 |
| 插件评估 HTML | `vault/assets/plugin-test/visual/plugin-eval-summary.html` | 用 Data Visualization 思路展示试跑结果 |
| `last30days` 原始调研输出 | `vault/cases/2026-06-21-插件试跑-case-1-ai-coding-repo-context-loss-调研验证/evidence/ai-coding-repo-context-loss-raw-plugintrial.md` | 保存调研类能力真实输出和来源缺口 |
| DOCX 简报 | `vault/assets/plugin-test/document/outputs/plugin-eval-brief.docx` | 验证 Documents 产物能力 |
| PDF 简报 | `vault/assets/plugin-test/pdf/outputs/plugin-eval-brief.pdf` | 验证 PDF 生成和文本抽取 |
| PPTX 演示稿 | `vault/assets/plugin-test/presentation/outputs/plugin-eval-deck.pptx` | 验证 Presentations 分享资产能力 |
| PPTX 预览图和 montage | `vault/assets/plugin-test/presentation/outputs/slide-01.png`、`slide-02.png`、`slide-03.png`、`plugin-eval-deck-montage.webp` | 验证演示稿可视化导出 |
| HyperFrames HTML | `vault/assets/plugin-test/hyperframes/index.html` | 验证网页视频/视觉叙事源文件能力 |
| HyperFrames lint | `vault/assets/plugin-test/hyperframes/outputs-lint.json` | 记录 0 error、2 warning 和视频导出缺口 |
| 原始证据目录 | `vault/cases/2026-06-21-codex-推荐插件真实试跑评估/evidence/` | 保存插件列表、GitHub、Hugging Face、Zotero 等原始输出 |
| manifest 能力表 | `vault/cases/2026-06-21-codex-推荐插件真实试跑评估/evidence/plugin-manifest-capabilities.csv` | 保存 40 个推荐插件的 Skill/App/MCP 数量 |
| app-only 阻塞说明 | `vault/cases/2026-06-21-codex-推荐插件真实试跑评估/evidence/plugin-app-only-blockers.md` | 解释账号类插件为什么当前不能算实际调用 |
| 重启后新线程探针回执 | `evidence/restart-thread-plugin-deepcheck-receipt.md`、`tool-ledger.md`、`process-log.md` | 保存新线程 `019ee803-b71e-7b01-a7b6-1608b91e9916` 的只读探针结果 |

## 已验证的产物质量

- 工作簿已成功导出 `.xlsx`。
- 工作簿已成功渲染 PNG 预览，肉眼检查可读，无空白页或明显错位。
- HTML 汇总页已写入本地文件；Browser 插件验收失败，因此只算文件级产物通过，不算浏览器级验收通过。
- DOCX 已生成，结构检查包含标题、段落和表格。
- PDF 已生成并完成文本抽取，`contains_title=True`。
- PPTX 已生成，inspect 显示 3 张 slides、1 个 chart、1 个 table，并导出 PNG/montage。
- HyperFrames lint `ok=true`、0 error；由于缺 `ffmpeg`，未导出 mp4。
- 新线程探针返回 completion receipt，确认更多 Skills 可见，但 app connector 工具仍未自动暴露。

## 产物边界

这些产物证明“插件试跑记录可以沉淀为资产”，但不证明外部用户需求成立。DOCX/PDF/视频类正式交付前还需要补齐本机渲染依赖。
