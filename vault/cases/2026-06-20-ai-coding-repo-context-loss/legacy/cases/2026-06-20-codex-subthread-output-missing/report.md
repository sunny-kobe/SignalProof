# SignalProof Case Report: Codex 子线程完成但未落目标文件

## Signal

子线程显示完成，但没有生成委派任务要求的目标文件。

## Research

内部证据确认：线程状态不能替代文件级验收。

## Debate

这不是独立产品机会，但对 SignalProof Protocol 的可靠性很关键。

## Thesis

继续，沉淀为子线程文件级验收门。

## Validation

源线程发现目标文件缺失、接管补齐，并把失败写入台账和 skill。

## Artifact

已形成规则：completion receipt 中的 `files` 必须逐个验收。

## Feedback

内部 A 级流程反馈，不是外部市场反馈。

## Decision

作为 SignalProof Protocol 的强制质量门保留。

## Asset

可复用资产：子线程文件级验收门。后续可扩展为 `audit_subtasks.py`。
