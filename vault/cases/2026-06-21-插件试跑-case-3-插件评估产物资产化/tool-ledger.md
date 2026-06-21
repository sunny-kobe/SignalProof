---
type: tool_ledger
status: completed
updated_at: 2026-06-21
gate: passed
---

# 工具账本

## 候选能力账本

| 能力 | 是否相关 | 是否使用 | 结果质量 | 说明 | 下次动作 |
| --- | --- | --- | --- | --- | --- |
| Skill: signalproof | 是 | 是 | 中 | repo 级 skill 提供本地流程规则。 | 保留。 |
| Skill: personal-opportunity-os | 是 | 是 | 中 | 提供长期方向和流程边界。 | 保留为上层方法论。 |
| Skill: last30days | 否 | 否 | not-needed | 本 case 是产物资产化，不做趋势调研。 | 调研类见 case 1。 |
| Browser | 是 | 否 | failed-upstream | 主 case 已记录 Browser setup 失败，本 case 未做浏览器级验收。 | 修复后补 HTML 截图。 |
| Computer Use | 低 | 否 | failed-upstream | 主 case 已记录 Computer Use 失败，本 case 不需要 GUI。 | GUI-only 验收时再用。 |
| Documents | 是 | 是 | 中 | 生成 `plugin-eval-brief.docx`，结构检查通过。 | 正式交付前补 LibreOffice 渲染。 |
| PDF | 是 | 是 | 中 | 生成 `plugin-eval-brief.pdf`，文本抽取和标题检查通过。 | 补 Poppler 后做图片渲染。 |
| Spreadsheets | 是 | 是 | 强 | 生成 `.xlsx`、PNG preview、inspect。 | 默认用于工具账本和反馈台账。 |
| Presentations | 是 | 是 | 强 | 生成 PPTX、slide PNG、montage、inspect；包含 chart 和 table。 | 适合复盘/分享场景。 |
| HyperFrames | 是 | 是 | 中 | HTML composition lint `ok=true`；缺 `ffmpeg` 未导出视频。 | 补 ffmpeg 后再输出 mp4。 |
| Data Visualization | 是 | 是 | 中 | 生成 HTML 汇总页；Browser 验收失败。 | 默认文件级资产，浏览器修复后补截图。 |
| Plugin | 是 | 是 | 中 | 已建立插件草案骨架。 | 后续安装测试。 |
| MCP | 中 | 否 | 弱 | 可接 OpenAI Docs、Context7、GitHub 等，但本轮先记录映射。 | 后续按阶段接入。 |
| Hooks | 中 | 否 | 弱 | 可用于强制 check-case。 | 后续加入。 |
| Automation | 中 | 否 | 弱 | 可用于 72h 反馈复查。 | 等发布渠道恢复后启用。 |

## 阶段能力计划

运行：

```bash
python3 scripts/signalproof.py capabilities
```

然后把本 case 各阶段真正考虑过的 Codex 自带插件记录到这里：

| 阶段 | 候选 Codex 插件 | 是否使用 | 结果质量 | 跳过或失败原因 | 下一步 |
| --- | --- | --- | --- | --- | --- |
| signal | Browser / Chrome / Record & Replay | 否 | not-needed | 信号来自用户要求。 | 保留候选。 |
| research | Documents / PDF / Spreadsheets / Data Visualization | 部分 | 中 | 研究对象是产物能力，读取生成结果和 inspect。 | 有外部资料再用。 |
| debate | Documents / PDF | 否 | not-needed | 本 case 不需要外部长文档反证。 | 保留候选。 |
| validation | Documents / PDF / Spreadsheets / Presentations / HyperFrames | 是 | passed-with-gap | 多格式生成成功；渲染依赖缺口已记录。 | 补依赖后增强验收。 |
| artifact | Documents / PDF / Spreadsheets / Presentations / HyperFrames / Data Visualization | 是 | 强 | 已生成多格式资产。 | 按场景启用，不全部默认。 |
| publication | Browser / Chrome | 否 | historical-risk | 未发布；Browser 有历史失败记录，本 case 没有重新做网页发布探针。 | 发布时再启用并重新只读验证。 |
| feedback | Spreadsheets / Record & Replay | 部分 | 中 | 工作簿可做反馈台账模板；无真实反馈。 | 有反馈后填入。 |
| asset | Documents / PDF / Spreadsheets / Presentations / HyperFrames / Data Visualization | 是 | 强 | 已沉淀多格式资产包。 | 建议纳入总报告。 |
| flow-review | Browser / Computer Use / Documents / PDF / Spreadsheets / Presentations | 是 | 中 | 文件级和 inspect 通过；Browser/GUI 未通过。 | 补浏览器/GUI验收。 |

## 能力结论

本 case 证明产物类插件能显著提升资产化表达，但不应每个 case 全量默认跑；按交付场景启用最稳。
