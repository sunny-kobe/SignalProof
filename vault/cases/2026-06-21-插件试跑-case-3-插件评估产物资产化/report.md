# 报告

## 摘要

`插件试跑 case 3：插件评估产物资产化` 已生成多格式产物，验证了 Documents、PDF、Spreadsheets、Presentations、Data Visualization、HyperFrames 的实际资产化价值。

## 结果

- Spreadsheets：生成工作簿、预览图和 inspect，强增益。
- Data Visualization：生成 HTML 汇总页，中到强增益，但 Browser 验收待修。
- Documents：生成 DOCX，适合正式交付件。
- PDF：生成 PDF 并完成文本抽取，缺 Poppler 图片渲染。
- Presentations：生成 PPTX、slide PNG、montage、inspect，强增益。
- HyperFrames：HTML/lint 通过，缺 ffmpeg 未导出视频。

## 结论

产物类插件能让 SignalProof 从“只有 Markdown 记录”升级为“可交付资料包”。但默认策略不应全量生成，而是按 case 需要启用。

## 边界

真实反馈和发布渠道本轮跳过，因此该 case 不能证明市场需求。

## 下一步

补齐 LibreOffice、Poppler、ffmpeg 后做完整渲染/视频导出验收。
