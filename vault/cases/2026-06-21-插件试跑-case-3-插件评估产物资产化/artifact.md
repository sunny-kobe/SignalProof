---
type: artifact
status: created
updated_at: 2026-06-21
gate: passed
---

# 产物

## 产物

本 case 的产物是一组插件评估资产，用于验证非 Markdown 交付能力。

## 文件

| 产物 | 路径 | 状态 |
| --- | --- | --- |
| 工作簿 | `vault/assets/plugin-test/workbook/outputs/plugin-eval-workbook.xlsx` | 生成成功 |
| 工作簿预览图 | `vault/assets/plugin-test/workbook/outputs/plugin-eval-workbook-preview.png` | 生成成功 |
| Data Visualization HTML | `vault/assets/plugin-test/visual/plugin-eval-summary.html` | 文件级生成成功 |
| DOCX | `vault/assets/plugin-test/document/outputs/plugin-eval-brief.docx` | 生成成功 |
| PDF | `vault/assets/plugin-test/pdf/outputs/plugin-eval-brief.pdf` | 生成成功 |
| PDF 文本抽取 | `vault/assets/plugin-test/pdf/outputs/plugin-eval-brief.text.txt` | 抽取成功 |
| PPTX | `vault/assets/plugin-test/presentation/outputs/plugin-eval-deck.pptx` | 生成成功 |
| PPTX montage | `vault/assets/plugin-test/presentation/outputs/plugin-eval-deck-montage.webp` | 生成成功 |
| slide PNG | `vault/assets/plugin-test/presentation/outputs/slide-01.png`、`slide-02.png`、`slide-03.png` | 生成成功 |
| HyperFrames HTML | `vault/assets/plugin-test/hyperframes/index.html` | 生成成功 |
| HyperFrames lint | `vault/assets/plugin-test/hyperframes/outputs-lint.json` | `ok=true` |

## 产物边界

- DOCX 未做 LibreOffice 页面渲染，因为本机缺 `soffice/libreoffice`。
- PDF 未做 Poppler PNG 渲染，因为本机缺 `pdftoppm/pdfinfo`。
- HyperFrames 未导出视频，因为本机缺 `ffmpeg`。
- 这些产物证明资产化能力，不证明外部用户需求。
