# SignalProof 插件漂移检查

生成日期：2026-07-01

## 对比对象

- 锁定清单插件数：36
- 安装脚本插件数：36
- 当天状态快照脚本插件数：36
- 当天状态快照已安装插件数：8
- 当前 `codex plugin list` 已安装插件数：8

## 结论

状态：failed

### 错误

- 状态快照显示部分锁定插件未安装启用: airtable@openai-curated, amplitude@openai-curated, box@openai-curated, brand24@openai-curated, build-web-data-visualization@openai-curated, canva@openai-curated, cloudflare@openai-curated, codex-security@openai-curated, datadog@openai-curated, deepnote@openai-curated, dovetail@openai-curated, figma@openai-curated, github@openai-curated, google-drive@openai-curated, hugging-face@openai-curated, hyperframes@openai-curated, jam@openai-curated, linear@openai-curated, mem@openai-curated, mixpanel@openai-curated, netlify@openai-curated, notion@openai-curated, openai-developers@openai-curated, posthog@openai-curated, readwise@openai-curated, record-and-replay@openai-bundled, scite@openai-curated, semrush@openai-curated, sentry@openai-curated, similarweb@openai-curated, superpowers@openai-curated, vercel@openai-curated, zotero@openai-curated
- 当前 Codex 环境缺少锁定插件: airtable@openai-curated, amplitude@openai-curated, box@openai-curated, brand24@openai-curated, build-web-data-visualization@openai-curated, canva@openai-curated, cloudflare@openai-curated, codex-security@openai-curated, datadog@openai-curated, deepnote@openai-curated, dovetail@openai-curated, figma@openai-curated, github@openai-curated, google-drive@openai-curated, hugging-face@openai-curated, hyperframes@openai-curated, jam@openai-curated, linear@openai-curated, mem@openai-curated, mixpanel@openai-curated, netlify@openai-curated, notion@openai-curated, openai-developers@openai-curated, posthog@openai-curated, readwise@openai-curated, record-and-replay@openai-bundled, scite@openai-curated, semrush@openai-curated, sentry@openai-curated, similarweb@openai-curated, superpowers@openai-curated, vercel@openai-curated, zotero@openai-curated

### 警告

- 状态快照存在未写入锁定清单的已安装插件: documents@openai-primary-runtime, pdf@openai-primary-runtime, presentations@openai-primary-runtime, spreadsheets@openai-primary-runtime, template-creator@openai-primary-runtime
- 当前 Codex 环境存在未写入锁定清单的已安装插件: documents@openai-primary-runtime, pdf@openai-primary-runtime, presentations@openai-primary-runtime, spreadsheets@openai-primary-runtime, template-creator@openai-primary-runtime

## 边界

- 本检查只证明插件安装和记录没有漂移。
- 本检查不证明外部账号已授权，也不证明 connector 能读取真实数据。
- 本检查不支持市场验证、产品化或 SaaS 结论。
