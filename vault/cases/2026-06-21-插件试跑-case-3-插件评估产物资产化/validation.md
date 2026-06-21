---
type: validation
status: planned
updated_at: 2026-06-21
gate: passed
---

# 验证计划

## 验证对象

验证产物类插件能否把插件审计结果生成可检查资产。

## 验证方式

1. 运行工作簿生成脚本，输出 `.xlsx`、PNG preview、inspect。
2. 生成 Data Visualization HTML 汇总页。
3. 运行 DOCX 生成脚本，检查段落、标题、表格。
4. 运行 PDF 生成脚本，检查页数、文本抽取和标题。
5. 运行 PPTX 生成脚本，检查 slides、chart、table、PNG、montage。
6. 运行 HyperFrames lint，记录 error/warning 和导出限制。

## 执行结果

- Spreadsheets：通过。
- Data Visualization：文件级通过，浏览器级未通过。
- Documents：结构检查通过。
- PDF：生成与文本抽取通过，Poppler 渲染缺依赖。
- Presentations：通过。
- HyperFrames：lint error 为 0，warning 为 2，缺 `ffmpeg` 未导出视频。

## 成功标准

- 每个产物都有实际文件路径。
- 每个产物都有质量检查或明确限制。
- 不把“生成文件”写成“正式发布/用户验证”。

## 本轮 gate

`passed-with-dependencies-gap`。资产化能力成立，但正式交付前要补齐 LibreOffice/Poppler/ffmpeg 或接受降级。
