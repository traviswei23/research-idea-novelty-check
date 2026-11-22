# 查新的来源可用性

本阶段的 20 份技能入口均已取得。每份入口按原清单指定的 GitHub 提交核对。连同直接讲解方法的文档、提示词、模板、脚本及重定位的关联材料，归集 183 个不同的仓库文件。同一文件只在本阶段计一次。文件数量仅用于复查来源。

以下记录影响复查的缺件、路径调整和容易误当原始资料的示例。每个入口的完整方法对应关系见本技能的来源对照。

| 上游入口 | 待核项目 | 核查结果与影响 |
|---|---|---|
| [positioning-engine](https://github.com/TobiasBlask/open-paper-machine/blob/160df4d13d266411f0850c4de7ecdbd93e8b40be/skills/positioning-engine/SKILL.md) | 检索脚本 academic_search.py | 配套 paper-machine.md 指示调用 search_all()。固定提交中找不到该文件。能读到逐篇比较、建立维度矩阵与定位结论的步骤；原脚本的检索实现无法核验。实际检索应使用明确可用的数据库并记录查询。 |
| [idea-novelty](https://github.com/Giovanni-Sforza/idea-survey-pipeline_claude/blob/7fa71ad0ef6dedcb5271c6bf69c343dddbc5a237/.claude/skills/idea-novelty/SKILL.md) | 论文证据卡与重试片段 | 论文卡 schema 已从同一仓库根目录 templates/PAPER_CARD_SCHEMA.md 取回。模板中还引用 templates/_partials/retry_block.md，固定提交无该文件；上游的这段重试提示词无法核验。证据卡、比较步骤和最终报告模板仍可核查。 |
| [research-idea-forge](https://github.com/ppsdk/research-idea-forge/blob/48494d8eb553b704f3a02882686ba49551a5521f/research-idea-forge/SKILL.md) | 其他仓库的评价维度 | 贡献比较附录列出 Supervisor-Skills 的评价文字作为出处。已能在本次收录的 idea-evaluator 固定版本中追查其维度和风险模块。该处属于方法来源，单独的文件并非原技能包内置。 |
| [literature-review](https://github.com/pinshuai/literature-review-skill/blob/ed62a2899202707b58e87e4cd6ae45792772fe58/SKILL.md) | 可选绘图依赖 | 上游明示当前环境跳过 generate_schematic.py。检索、筛选、证据表和全文比较均有公开流程；不以是否能生成流程图判断查新覆盖。 |

原文中同名的项目输入、生成文件、个人机器路径与学术书目的作用各异。凡无法从公开材料确认的指令，不以推测补写为上游原话。
