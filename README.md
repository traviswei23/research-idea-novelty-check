# 科研构想查新

已有一个想法，最担心别人做过。这个技能会实际检索、定位最近似论文的原文，逐条回答哪些主张已被覆盖，哪些差异仍值得验证。默认执行正式查新。明确要求“先初筛”“只对照这篇论文”时，按指定范围交付。

将仓库放入项目的 `.agents/skills/research-idea-novelty-check/`。例如可以这样调用。

> 用 $research-idea-novelty-check 核查我的想法。我的核心主张是……，研究条件是……，我最担心这篇论文已经做过……。请给我最能推翻它的论文和原文位置，再说清还有哪些差异值得做。

正式报告包含逐条判断、原文对照、实际查询记录与独立审查情况。配套的 Python 3.9+ 工具可检索公开学术索引、核对书目身份并检查查新档案。搜索故障、缺失的全文和缺席的独立审查都会影响结论。配套工具、指令原文和测试均随仓库提供。

[技能入口](SKILL.md) · [执行与查验说明](references/runbook.md) · [ARIS 如何进入查新流程](references/aris-review.md) · [21 个既有来源](references/source-map.md) · [新增 5 个工作流与轮次对比工具](references/research-loop.md) · [上游固定版本及可用附件](references/source-availability.md)
