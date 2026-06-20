---
type: debate
status: debated
updated_at: 2026-06-20
gate: weak-but-actionable
---

# 辩论

## 当前裁决

收窄后继续。

这个机会不能被包装成“AI coding 上下文平台”，也不能现在做 Codex Plugin、Web App、SaaS 或自动扫描器。现有证据只支持一个很窄的公开验证：

```text
Repo AI Context Audit Checklist
+ 瘦身版 AGENTS.md / CLAUDE.md 模板
+ synthetic before/after demo
+ 72 小时真实失败任务征集
```

## 正方：为什么值得继续

- 用户个人能力高度匹配：长期用 Codex、Claude Code、MCP、本地工具链和真实复杂 repo，能判断 AI 写偏不是简单 prompt 问题。
- 官方机制存在：Codex 支持 `AGENTS.md`，Claude Code 有项目记忆和 `CLAUDE.md`，说明 repo-level guidance 是真实入口，不是幻想。
- 低成本可验证：不用先做产品，只要 checklist、模板、demo、私聊脚本和真实失败任务征集。
- 资产化路径清楚：即使市场验证失败，也能沉淀成用户自己的 AI coding 工作流资产。
- 反方也能转化为资产：如果发现上下文文件无效，也能形成“不要把 AGENTS.md 写成第二份 README”的反常识内容。

## 反方：为什么可能不成立

- 官方文档已经覆盖基础用法，单纯模板不稀缺。
- 本轮 `last30days` 证据弱且噪音高，不能证明近期市场热度。
- GitHub issue 搜索没有找到直接需求，说明公开开发者信号很薄。
- 旧 demo 是 synthetic demo，不是真实用户反馈。
- 上下文文件可能越写越长，反而污染 agent 判断。
- 用户可能真正需要的是需求澄清、测试环境、代码审查或工作流诊断，不是 repo context audit。

## 产品视角

如果产品化过早，会变成用户看不懂的“AI coding context system”。当前更像一个公开验证包，而不是产品：

- 输入：一个真实 AI 写偏任务。
- 过程：审计现有 `AGENTS.md` / `CLAUDE.md`，删除泛规则，保留高频失败约束。
- 输出：before/after 和 checklist 改进。
- 验证：目标用户是否愿意提交任务、复制模板、提出具体反对意见。

## 商业视角

现在不能谈 SaaS。最多只能保留未来三条可能：

- 资料包：checklist、模板、prompt、SOP。
- 服务：3 到 5 天 repo AI context audit。
- 开源：repo/gist 收集真实失败任务和模板迭代。

商业化要等至少 1 个真实 before/after 和 3 个 A/B 级反馈后再谈。

## 执行视角

72 小时内可以完成最小验证：

- 发布 GitHub repo 或 gist。
- 私聊 5 个 AI coding 高频用户。
- 收集 1 个真实失败任务。
- 做一次 before/after。
- 输出继续、收窄、暂停或放弃决策。

不需要做 Web UI、插件、自动扫描或 dashboard。

## 开源视角

开源空位不是 `AGENTS.md` 模板，而是“验证账本”：

- 公开 checklist。
- 公开 synthetic demo。
- 公开反馈字段。
- 公开真实任务脱敏 before/after。
- 公开哪些规则有效、哪些规则无效。

如果 repo 只放模板，没有真实任务，会很容易淹没。

## 个人优势视角

这件事贴合用户的长期方向：通过 Codex 把外部信号变成证据、判断、实验、产物、反馈、决策和资产。它不是公司中后台需求优化，而是个人可移动、可复利的 AI coding 工作流能力。

## 最可能失败的 10 个原因

1. 把方法论切口包装成产品，导致用户一眼看不懂。
2. 目标用户过宽，最后写成普通 AI coding 教程。
3. 只做 `AGENTS.md` 模板，被官方文档和博客替代。
4. 继续完善 synthetic demo，却没有真实失败任务。
5. 上下文文件越写越长，反而拖慢或误导 agent。
6. checklist 太像工程规范，不够贴近“AI 实际写偏”的场景。
7. 发布文案夸大成成功案例，引发信任损耗。
8. 过早做插件、CLI、Web UI、自动扫描器，维护成本压过验证价值。
9. 真实用户不愿意暴露私有 repo 或失败任务，导致案例素材不足。
10. 用户真正需要的是“AI coding 工作流诊断”，不是“repo context audit”这个窄概念。

## 必须砍掉的范围

- AI coding context platform。
- Personal Opportunity OS 对外产品。
- Web App。
- SaaS。
- dashboard。
- 自动 repo 扫描器。
- Obsidian 插件。
- Codex Plugin 发布包。
- n8n / Dify / Langflow 集成。
- 多模型、多工具、大而全 AI coding guide。
- “保证 AI 理解项目”的承诺。
- 真实反馈为空时的成功案例包装。

## 什么证据会改变判断

转向暂停或放弃：

- 5 个目标用户里 4 个以上明确说不需要。
- 72 小时只有泛点赞，没有任务提交或具体问题。
- 真实 before/after 没有改善，甚至更差。
- 用户反馈主要问题不是上下文，而是模型能力、权限、测试环境或需求不清。

转向继续扩展：

- 至少 3 个 A/B 级反馈。
- 至少 1 个真实失败任务。
- 至少 1 个 before/after 有可观察改善。
- 有用户主动要求审计自己的 repo context。
- GitHub repo/gist 出现 issue、PR、fork 或明确改进建议。
