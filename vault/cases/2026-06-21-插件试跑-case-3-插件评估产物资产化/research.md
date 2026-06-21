---
type: research
status: completed
updated_at: 2026-06-21
gate: weak
---

# 研究

## 要回答的问题

- 产物类插件是否能把插件评估结果转成可复用资产，而不是只留 Markdown？
- Documents、PDF、Presentations、Spreadsheets、Data Visualization、HyperFrames 各自适合默认使用还是按场景使用？
- 哪些本机依赖缺口会影响正式交付？

## 已确认事实

- Spreadsheets 已生成 `.xlsx`、PNG 预览和 inspect 文件。
- Data Visualization 已生成 HTML 汇总页，但 Browser 验收失败，只能算文件级通过。
- Documents 已生成 DOCX，并通过结构检查：标题存在、段落和表格存在。
- PDF 已生成并可抽取文本；当前缺 `pdftoppm/pdfinfo`，不能完成 Poppler PNG 渲染。
- Presentations 已生成 PPTX、三张 slide PNG、montage 和 inspect 文件。
- HyperFrames 已生成 HTML composition，lint `ok=true`，但本机缺 `ffmpeg`，没有导出 mp4。

## 本机依赖缺口

```text
soffice not found
libreoffice not found
pdftoppm not found
pdfinfo not found
ffmpeg not found
```

## 证据质量

| 能力 | 结果质量 | 判断 |
| --- | --- | --- |
| Spreadsheets | 强 | 默认进入工具账本、反馈台账、证据矩阵。 |
| Data Visualization | 中 | 适合报告页，但浏览器验收失败时只算文件级通过。 |
| Documents | 中 | 适合正式交付件，但本轮未做 DOCX 页面渲染。 |
| PDF | 中 | 生成和文本抽取通过；缺 Poppler 渲染依赖。 |
| Presentations | 强 | PPTX、PNG、montage、inspect 均生成，适合分享型产物。 |
| HyperFrames | 中 | HTML/lint 通过；缺 ffmpeg，不能完成视频导出。 |

## 当前判断

产物类插件确实能提高 SignalProof 的资产化能力，但不应每个 case 全部默认跑。默认保留 Spreadsheets 和 Data Visualization；Documents/PDF/Presentations/HyperFrames 在需要正式交付或传播资产时启用。
