# 来源与流程对照

每条来源固定到选入时的 Git 提交。下表列出原入口中的操作、在此技能中的处理与执行位置。配套项单列关键模板、提示或判据入口，便于复查。各流程提示以中文重新编写。

本版共 21 个直接来源，保留原清单的 20 个入口，增加 ARIS 原版。新增的流程与来处见[独立复核手册](aris-review.md)及[第 21 个入口](#s423)。

## 从流程查来源

- [立项与范围](../SKILL.md)　[research-novelty-review](#s714)、[research-systematic-literature-review](#s3197)、[research-question-validator](#s692)、[novelty-check](#s686)、[idea-novelty-auditor](#s431)、[hypothesis-stress-test](#s732)、[literature-review-master](#s2755)、[research-idea-forge](#s416)
- [检索与补检](search.md)　[research-systematic-literature-review](#s3197)、[idea-novelty](#s723)、[research-question-validator](#s692)、[novelty-assessment](#s432)、[Novelty Check](#s746)、[literature-search](#s747)、[literature-search](#s719)、[hypothesis-stress-test](#s732)、[systematic-literature-review](#s771)、[novelty-check](#s720)、[lit-positioning](#s433)、[literature-review](#s2959)、[research-idea-forge](#s416)
- [召回、筛选与更新](search.md)　[research-systematic-literature-review](#s3197)、[idea-novelty](#s723)、[paper-novelty-check](#s708)、[Novelty Check](#s746)、[literature-search](#s747)、[literature-search](#s719)、[literature-review](#s2959)
- [原文、版本及矩阵](comparison.md)　[research-novelty-review](#s714)、[idea-novelty](#s723)、[novelty-check](#s686)、[positioning-engine](#s693)、[related-work-positioning](#s687)、[literature-search](#s719)、[systematic-literature-review](#s771)、[novelty-check](#s720)、[literature-review-master](#s2755)、[lit-positioning](#s433)、[literature-review](#s2959)
- [反方质询与等价性](extended-review.md)　[novelty-assessment](#s432)、[positioning-engine](#s693)、[related-work-positioning](#s687)、[idea-novelty-auditor](#s431)、[hypothesis-stress-test](#s732)、[novelty-check](#s720)、[lit-positioning](#s433)、[research-idea-forge](#s416)
- [判定与交付](report.md)　[research-novelty-review](#s714)、[research-systematic-literature-review](#s3197)、[idea-novelty](#s723)、[research-question-validator](#s692)、[novelty-assessment](#s432)、[paper-novelty-check](#s708)、[Novelty Check](#s746)、[novelty-check](#s686)、[positioning-engine](#s693)、[related-work-positioning](#s687)、[idea-novelty-auditor](#s431)、[literature-search](#s747)、[hypothesis-stress-test](#s732)、[systematic-literature-review](#s771)、[novelty-check](#s720)、[literature-review-master](#s2755)、[literature-review](#s2959)、[research-idea-forge](#s416)

## 从来源查具体操作

<a id="s714"></a>

### research-novelty-review · yananlong/codex-skills

[固定版本原文](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-novelty-review/SKILL.md)

| 原文位置 | 转成什么操作 | 去向 |
| --- | --- | --- |
| [Decompose the claim](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-novelty-review/SKILL.md#L104) | 把主张写成可搜单元，并预写足以推翻它的观测。 | [立项与范围](../SKILL.md) |
| [Build the prior-art matrix](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-novelty-review/SKILL.md#L126) | 将最强重合工作放在矩阵第一行，给出来源位置。 | [原文、版本及矩阵](comparison.md) |
| [Decide and position narrowly](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-novelty-review/SKILL.md#L145) | 先回应反方，再给最宽和最窄两版定位，证据弱时压低确信程度。 | [判定与交付](report.md) |

配套定位：[adversarial-query-patterns.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-novelty-review/references/adversarial-query-patterns.md) · [overlap-scoring-rubric.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-novelty-review/references/overlap-scoring-rubric.md) · [prior-art-matrix-template.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-novelty-review/references/prior-art-matrix-template.md) · [reviewer-objection-rubric.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-novelty-review/references/reviewer-objection-rubric.md) · [novelty_assurance.py](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-novelty-review/scripts/novelty_assurance.py) · [decision-scale.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-novelty-review/references/decision-scale.md)

<a id="s3197"></a>

### research-systematic-literature-review · yananlong/codex-skills

[固定版本原文](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-systematic-literature-review/SKILL.md)

| 原文位置 | 转成什么操作 | 去向 |
| --- | --- | --- |
| [Build coverage map](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-systematic-literature-review/SKILL.md#L134) | 用已知种子与独立挑战样本验证查询覆盖。 | [立项与范围](../SKILL.md) |
| [Repair search](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-systematic-literature-review/SKILL.md#L160) | 诊断种子遗漏的原因并重跑；系统复核可请独立者审查检索式。 | [检索与补检](search.md) |
| [freeze the candidate corpus](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-systematic-literature-review/SKILL.md#L169) | 冻结本轮文献集合，记录版本、年份、重叠报告和排除理由。 | [召回、筛选与更新](search.md) |
| [Synthesize and grade](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-systematic-literature-review/SKILL.md#L195) | 分别报告证据、分歧、负结果和渠道限制。 | [判定与交付](report.md) |

配套定位：[recall-assurance-contract.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-systematic-literature-review/references/recall-assurance-contract.md) · [claim-cards-and-source-ladder.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-systematic-literature-review/references/claim-cards-and-source-ladder.md) · [prisma-core-checklist.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-systematic-literature-review/references/prisma-core-checklist.md) · [search_log_rules.py](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-systematic-literature-review/scripts/search_log_rules.py)

<a id="s723"></a>

### idea-novelty · Giovanni-Sforza/idea-survey-pipeline_claude

[固定版本原文](https://github.com/Giovanni-Sforza/idea-survey-pipeline_claude/blob/7fa71ad0ef6dedcb5271c6bf69c343dddbc5a237/.claude/skills/idea-novelty/SKILL.md)

| 原文位置 | 转成什么操作 | 去向 |
| --- | --- | --- |
| [Per-Claim Competitive Search](https://github.com/Giovanni-Sforza/idea-survey-pipeline_claude/blob/7fa71ad0ef6dedcb5271c6bf69c343dddbc5a237/.claude/skills/idea-novelty/SKILL.md#L249) | 按每个声称的新意并行找最强竞争工作，分开记录线索。 | [检索与补检](search.md) |
| [PDF Vision Manifest](https://github.com/Giovanni-Sforza/idea-survey-pipeline_claude/blob/7fa71ad0ef6dedcb5271c6bf69c343dddbc5a237/.claude/skills/idea-novelty/SKILL.md#L634) | 图像或公式承载关键证据时核图、表、页和 TeX；把缺页标作未知。 | [原文、版本及矩阵](comparison.md) |
| [Paper Card Distillation](https://github.com/Giovanni-Sforza/idea-survey-pipeline_claude/blob/7fa71ad0ef6dedcb5271c6bf69c343dddbc5a237/.claude/skills/idea-novelty/SKILL.md#L874) | 同论文复用卡片，以版本与新主张决定是否补读。 | [原文、版本及矩阵](comparison.md) |
| [Named-Baseline Refinement](https://github.com/Giovanni-Sforza/idea-survey-pipeline_claude/blob/7fa71ad0ef6dedcb5271c6bf69c343dddbc5a237/.claude/skills/idea-novelty/SKILL.md#L1047) | 沿最近似工作中的基准名和引用再扩一轮，并为增量轮次留预算。 | [召回、筛选与更新](search.md) |
| [Report Writing](https://github.com/Giovanni-Sforza/idea-survey-pipeline_claude/blob/7fa71ad0ef6dedcb5271c6bf69c343dddbc5a237/.claude/skills/idea-novelty/SKILL.md#L1512) | 汇总保存证据与原文；人员分工按运行环境而定。 | [判定与交付](report.md) |

配套定位：[IDEA_NOVELTY_TEMPLATE.md](https://github.com/Giovanni-Sforza/idea-survey-pipeline_claude/blob/7fa71ad0ef6dedcb5271c6bf69c343dddbc5a237/templates/IDEA_NOVELTY_TEMPLATE.md) · [PAPER_CARD_SCHEMA.md](https://github.com/Giovanni-Sforza/idea-survey-pipeline_claude/blob/7fa71ad0ef6dedcb5271c6bf69c343dddbc5a237/templates/PAPER_CARD_SCHEMA.md) · [survey-fanout-protocol.md](https://github.com/Giovanni-Sforza/idea-survey-pipeline_claude/blob/7fa71ad0ef6dedcb5271c6bf69c343dddbc5a237/.claude/skills/shared-references/survey-fanout-protocol.md) · [paper-card-contract.md](https://github.com/Giovanni-Sforza/idea-survey-pipeline_claude/blob/7fa71ad0ef6dedcb5271c6bf69c343dddbc5a237/.claude/skills/shared-references/paper-card-contract.md)

<a id="s692"></a>

### research-question-validator · stephenturner/skill-research-question-validator

[固定版本原文](https://github.com/stephenturner/skill-research-question-validator/blob/06fe29a993a3553e8948a6c98f4eb81c1fc60ddf/SKILL.md)

| 原文位置 | 转成什么操作 | 去向 |
| --- | --- | --- |
| [Parse the Research Question](https://github.com/stephenturner/skill-research-question-validator/blob/06fe29a993a3553e8948a6c98f4eb81c1fc60ddf/SKILL.md#L76) | 分解问题、方法、条件和输出；只使用本次实际获取的结果。 | [立项与范围](../SKILL.md) |
| [Consensus Searches Sequentially](https://github.com/stephenturner/skill-research-question-validator/blob/06fe29a993a3553e8948a6c98f4eb81c1fc60ddf/SKILL.md#L95) | 快速模式以四至五次互补查询覆盖直接前作、邻域与反证。 | [检索与补检](search.md) |
| [Generate the .docx](https://github.com/stephenturner/skill-research-question-validator/blob/06fe29a993a3553e8948a6c98f4eb81c1fc60ddf/SKILL.md#L169) | 把拥挤程度、依据和推荐下一步浓缩为可分享短报；Word 为可选载体。 | [判定与交付](report.md) |

<a id="s432"></a>

### novelty-assessment · muye1112/skill

[固定版本原文](https://github.com/muye1112/skill/blob/fa7df033b3d51e2f8774f51a83e91b5aeecd4e55/skills/novelty-assessment/SKILL.md)

| 原文位置 | 转成什么操作 | 去向 |
| --- | --- | --- |
| [Multi-Round Literature Search](https://github.com/muye1112/skill/blob/fa7df033b3d51e2f8774f51a83e91b5aeecd4e55/skills/novelty-assessment/SKILL.md#L41) | 每轮根据最近似论文生成下一条查询，最多十轮是原配置。 | [检索与补检](search.md) |
| [Harsh Critic Persona](https://github.com/muye1112/skill/blob/fa7df033b3d51e2f8774f51a83e91b5aeecd4e55/skills/novelty-assessment/SKILL.md#L59) | 让反方寻找可替代解释和重合处，显式记录缺口。 | [反方质询与等价性](extended-review.md) |
| [Make Decision](https://github.com/muye1112/skill/blob/fa7df033b3d51e2f8774f51a83e91b5aeecd4e55/skills/novelty-assessment/SKILL.md#L49) | 将原二元判定改作与证据范围相符的四种状态。 | [判定与交付](report.md) |

配套定位：[assessment-prompts.md](https://github.com/muye1112/skill/blob/fa7df033b3d51e2f8774f51a83e91b5aeecd4e55/skills/novelty-assessment/references/assessment-prompts.md)

<a id="s708"></a>

### paper-novelty-check · AlexYangge/paper-research-skills

[固定版本原文](https://github.com/AlexYangge/paper-research-skills/blob/cc96a465c52525e9912f5a6e57e87de0c6064fdf/paper-novelty-check/SKILL.md)

| 原文位置 | 转成什么操作 | 去向 |
| --- | --- | --- |
| [加载文献台账](https://github.com/AlexYangge/paper-research-skills/blob/cc96a465c52525e9912f5a6e57e87de0c6064fdf/paper-novelty-check/SKILL.md#L36) | 从旧台账恢复标识与去重键，保留之前的排除决定。 | [召回、筛选与更新](search.md) |
| [去重比对](https://github.com/AlexYangge/paper-research-skills/blob/cc96a465c52525e9912f5a6e57e87de0c6064fdf/paper-novelty-check/SKILL.md#L59) | 对 DOI、题名、第一作者与版本依次核对，保存新增、高相关和重复的统计。 | [召回、筛选与更新](search.md) |
| [新颖性判定](https://github.com/AlexYangge/paper-research-skills/blob/cc96a465c52525e9912f5a6e57e87de0c6064fdf/paper-novelty-check/SKILL.md#L93) | 区分问题与方法的重合，把变化写回原主张和台账。 | [判定与交付](report.md) |

配套定位：[dedupe.py](https://github.com/AlexYangge/paper-research-skills/blob/cc96a465c52525e9912f5a6e57e87de0c6064fdf/paper-novelty-check/scripts/dedupe.py)

<a id="s746"></a>

### Novelty Check · sacrrie/skill-novelty-checker

[固定版本原文](https://github.com/sacrrie/skill-novelty-checker/blob/d981b166d56813dcd4426d757b1b69615504169e/SKILL.md)

| 原文位置 | 转成什么操作 | 去向 |
| --- | --- | --- |
| [novelty_check.py](https://github.com/sacrrie/skill-novelty-checker/blob/d981b166d56813dcd4426d757b1b69615504169e/SKILL.md#L20) | 使用 OpenAlex 等可访问索引分页筛候选，用问题和多组查询携带匹配目标。 | [检索与补检](search.md) |
| [Configuration](https://github.com/sacrrie/skill-novelty-checker/blob/d981b166d56813dcd4426d757b1b69615504169e/SKILL.md#L64) | 缓存请求、预算、错误与早停原因；服务可用性单独检查。 | [召回、筛选与更新](search.md) |
| [Interpreting Output](https://github.com/sacrrie/skill-novelty-checker/blob/d981b166d56813dcd4426d757b1b69615504169e/SKILL.md#L83) | 将模型检测到的威胁保留为待核候选，人工核实决定性前作后再判定。 | [判定与交付](report.md) |

配套定位：[novelty_check.py](https://github.com/sacrrie/skill-novelty-checker/blob/d981b166d56813dcd4426d757b1b69615504169e/scripts/novelty_check.py) · [test_setup.py](https://github.com/sacrrie/skill-novelty-checker/blob/d981b166d56813dcd4426d757b1b69615504169e/scripts/test_setup.py)

<a id="s686"></a>

### novelty-check · sunnnybala/rstack

[固定版本原文](https://github.com/sunnnybala/rstack/blob/3cf7ac1edaf6bcfc5c05f86a7d4bbcc2ed99f9ec/novelty-check/SKILL.md)

| 原文位置 | 转成什么操作 | 去向 |
| --- | --- | --- |
| [Load Context](https://github.com/sunnnybala/rstack/blob/3cf7ac1edaf6bcfc5c05f86a7d4bbcc2ed99f9ec/novelty-check/SKILL.md#L119) | 优先复用上轮综述，无资料时转初筛。 | [立项与范围](../SKILL.md) |
| [Paper-by-Paper Comparison](https://github.com/sunnnybala/rstack/blob/3cf7ac1edaf6bcfc5c05f86a7d4bbcc2ed99f9ec/novelty-check/SKILL.md#L126) | 分列问题、路径、贡献与适用范围的重合。 | [原文、版本及矩阵](comparison.md) |
| [Idea Refinement](https://github.com/sunnnybala/rstack/blob/3cf7ac1edaf6bcfc5c05f86a7d4bbcc2ed99f9ec/novelty-check/SKILL.md#L158) | 同步修订假设、评估计划、风险与下一步。 | [判定与交付](report.md) |
| [Human Checkpoint](https://github.com/sunnnybala/rstack/blob/3cf7ac1edaf6bcfc5c05f86a7d4bbcc2ed99f9ec/novelty-check/SKILL.md#L189) | 只在维持、改变或放弃研究目标的选择处交还用户。 | [判定与交付](report.md) |

<a id="s693"></a>

### positioning-engine · TobiasBlask/open-paper-machine

[固定版本原文](https://github.com/TobiasBlask/open-paper-machine/blob/160df4d13d266411f0850c4de7ecdbd93e8b40be/skills/positioning-engine/SKILL.md)

| 原文位置 | 转成什么操作 | 去向 |
| --- | --- | --- |
| [Closest Competitors](https://github.com/TobiasBlask/open-paper-machine/blob/160df4d13d266411f0850c4de7ecdbd93e8b40be/skills/positioning-engine/SKILL.md#L48) | 按接近程度选直接竞争者、潜在经典前驱与新近变体。 | [原文、版本及矩阵](comparison.md) |
| [Dimension Selection](https://github.com/TobiasBlask/open-paper-machine/blob/160df4d13d266411f0850c4de7ecdbd93e8b40be/skills/positioning-engine/SKILL.md#L116) | 按实际争议选比较维度，填写同条件下的实质差异。 | [原文、版本及矩阵](comparison.md) |
| [Positioning Patterns](https://github.com/TobiasBlask/open-paper-machine/blob/160df4d13d266411f0850c4de7ecdbd93e8b40be/skills/positioning-engine/SKILL.md#L157) | 检查差异来自机制、情境、理论还是增量改善。 | [反方质询与等价性](extended-review.md) |
| [Positioning Paragraph Template](https://github.com/TobiasBlask/open-paper-machine/blob/160df4d13d266411f0850c4de7ecdbd93e8b40be/skills/positioning-engine/SKILL.md#L176) | 从差异矩阵写出定位和审稿人最可能指出的漏洞。 | [判定与交付](report.md) |

<a id="s687"></a>

### related-work-positioning · UCL-ERL/skills

[固定版本原文](https://github.com/UCL-ERL/skills/blob/9d50603850b661a1da175ef3e330ba0b52e3efe9/skills/writing/related-work-positioning/SKILL.md)

| 原文位置 | 转成什么操作 | 去向 |
| --- | --- | --- |
| [Workflow](https://github.com/UCL-ERL/skills/blob/9d50603850b661a1da175ef3e330ba0b52e3efe9/skills/writing/related-work-positioning/SKILL.md#L18) | 按任务、方法、数据、理论或系统角色建立前作分组，注明覆盖边界。 | [原文、版本及矩阵](comparison.md) |
| [Novelty Claim Map](https://github.com/UCL-ERL/skills/blob/9d50603850b661a1da175ef3e330ba0b52e3efe9/skills/writing/related-work-positioning/SKILL.md#L37) | 每项新意绑定来源，标记主张缺哪类证据。 | [反方质询与等价性](extended-review.md) |
| [Rewrite](https://github.com/UCL-ERL/skills/blob/9d50603850b661a1da175ef3e330ba0b52e3efe9/skills/writing/related-work-positioning/SKILL.md#L41) | 仅在原稿有问题的句子上作证据限定；保留已支持的结论。 | [判定与交付](report.md) |

配套定位：[positioning-checks.md](https://github.com/UCL-ERL/skills/blob/9d50603850b661a1da175ef3e330ba0b52e3efe9/skills/writing/related-work-positioning/references/positioning-checks.md)

<a id="s431"></a>

### idea-novelty-auditor · yujie-jason-zhang/polish_skill

[固定版本原文](https://github.com/yujie-jason-zhang/polish_skill/blob/9b2a86ca6ac88879a3d3490fecdb909673fd1562/idea-novelty-auditor/SKILL.md)

| 原文位置 | 转成什么操作 | 去向 |
| --- | --- | --- |
| [Verification Mode](https://github.com/yujie-jason-zhang/polish_skill/blob/9b2a86ca6ac88879a3d3490fecdb909673fd1562/idea-novelty-auditor/SKILL.md#L23) | 已有定位句时切成核验模式，保留写得准确的部分。 | [立项与范围](../SKILL.md) |
| [Workflow](https://github.com/yujie-jason-zhang/polish_skill/blob/9b2a86ca6ac88879a3d3490fecdb909673fd1562/idea-novelty-auditor/SKILL.md#L41) | 还原旧方法的操作含义，再用经典模型和朴素基线质询新名称。 | [反方质询与等价性](extended-review.md) |
| [Output Format](https://github.com/yujie-jason-zhang/polish_skill/blob/9b2a86ca6ac88879a3d3490fecdb909673fd1562/idea-novelty-auditor/SKILL.md#L72) | 短报告保留危险基线、可辩护的主张、最小判别试验和残余风险。 | [判定与交付](report.md) |

配套定位：[idea_novelty_risk_audit.md](https://github.com/yujie-jason-zhang/polish_skill/blob/9b2a86ca6ac88879a3d3490fecdb909673fd1562/idea-novelty-auditor/references/idea_novelty_risk_audit.md)

<a id="s747"></a>

### literature-search · wangsir1214/my-claude-skills

[固定版本原文](https://github.com/wangsir1214/my-claude-skills/blob/629ec90a474c5a73d78cfbe71d6f97fb2285ec69/skills/literature-search/SKILL.md)

| 原文位置 | 转成什么操作 | 去向 |
| --- | --- | --- |
| [Decompose the query](https://github.com/wangsir1214/my-claude-skills/blob/629ec90a474c5a73d78cfbe71d6f97fb2285ec69/skills/literature-search/SKILL.md#L22) | 列通行词、同义词和限制，再按问题组合查询。 | [检索与补检](search.md) |
| [Triage and rank](https://github.com/wangsir1214/my-claude-skills/blob/629ec90a474c5a73d78cfbe71d6f97fb2285ec69/skills/literature-search/SKILL.md#L52) | 以正式记录检验题录，合并版本，按科学相关性排序。 | [召回、筛选与更新](search.md) |
| [Output format](https://github.com/wangsir1214/my-claude-skills/blob/629ec90a474c5a73d78cfbe71d6f97fb2285ec69/skills/literature-search/SKILL.md#L65) | 未核实的字段与真实引用分列，可沿用用户 BibTeX 格式。 | [判定与交付](report.md) |

<a id="s719"></a>

### literature-search · dynamor2019/xiao-jia-ai-paper-writing-platform

[固定版本原文](https://github.com/dynamor2019/xiao-jia-ai-paper-writing-platform/blob/9cd68c1368e84b7ff6838a2446cc9e29a0302b2b/.dsh/skills/literature-search/SKILL.md)

| 原文位置 | 转成什么操作 | 去向 |
| --- | --- | --- |
| [关键词设计](https://github.com/dynamor2019/xiao-jia-ai-paper-writing-platform/blob/9cd68c1368e84b7ff6838a2446cc9e29a0302b2b/.dsh/skills/literature-search/SKILL.md#L15) | 围绕概念、方法、应用、综述与时间建立五类查询。 | [检索与补检](search.md) |
| [多轮联网检索](https://github.com/dynamor2019/xiao-jia-ai-paper-writing-platform/blob/9cd68c1368e84b7ff6838a2446cc9e29a0302b2b/.dsh/skills/literature-search/SKILL.md#L23) | 沿高相关论文追踪引用与被引用的工作。 | [召回、筛选与更新](search.md) |
| [知识卡片提取](https://github.com/dynamor2019/xiao-jia-ai-paper-writing-platform/blob/9cd68c1368e84b7ff6838a2446cc9e29a0302b2b/.dsh/skills/literature-search/SKILL.md#L29) | 逐篇保存核心问题、方法、发现与局限再横向综合。 | [原文、版本及矩阵](comparison.md) |

<a id="s732"></a>

### hypothesis-stress-test · Aditya-Tandon/claude-research-skills

[固定版本原文](https://github.com/Aditya-Tandon/claude-research-skills/blob/4664d1ca1c90f89a835457b83446b52a969c87c2/skills/hypothesis-stress-test/SKILL.md)

| 原文位置 | 转成什么操作 | 去向 |
| --- | --- | --- |
| [Formalize the hypothesis](https://github.com/Aditya-Tandon/claude-research-skills/blob/4664d1ca1c90f89a835457b83446b52a969c87c2/skills/hypothesis-stress-test/SKILL.md#L58) | 写出可失败的机制主张和边界。 | [立项与范围](../SKILL.md) |
| [Generate counterarguments](https://github.com/Aditya-Tandon/claude-research-skills/blob/4664d1ca1c90f89a835457b83446b52a969c87c2/skills/hypothesis-stress-test/SKILL.md#L68) | 区分混杂、替代解释、反例的影响严重性。 | [反方质询与等价性](extended-review.md) |
| [contradictory evidence](https://github.com/Aditya-Tandon/claude-research-skills/blob/4664d1ca1c90f89a835457b83446b52a969c87c2/skills/hypothesis-stress-test/SKILL.md#L83) | 查反方证据并核对本地已有资料。 | [检索与补检](search.md) |
| [Suggest experiments](https://github.com/Aditya-Tandon/claude-research-skills/blob/4664d1ca1c90f89a835457b83446b52a969c87c2/skills/hypothesis-stress-test/SKILL.md#L114) | 用成本最低且能改变判定的验证解开最大疑点。 | [判定与交付](report.md) |

<a id="s771"></a>

### systematic-literature-review · bytedance/deer-flow

[固定版本原文](https://github.com/bytedance/deer-flow/blob/a9b5dd80f8a52d1d6e66d6462d2635f7ca91d76f/skills/public/systematic-literature-review/SKILL.md)

| 原文位置 | 转成什么操作 | 去向 |
| --- | --- | --- |
| [Search arXiv](https://github.com/bytedance/deer-flow/blob/a9b5dd80f8a52d1d6e66d6462d2635f7ca91d76f/skills/public/systematic-literature-review/SKILL.md#L45) | 将近期预印本作为定向补检，并写清检索范围。 | [检索与补检](search.md) |
| [Extract evidence](https://github.com/bytedance/deer-flow/blob/a9b5dd80f8a52d1d6e66d6462d2635f7ca91d76f/skills/public/systematic-literature-review/SKILL.md#L77) | 按问题、方法、关键结果与局限分批提取。 | [原文、版本及矩阵](comparison.md) |
| [Synthesize and format](https://github.com/bytedance/deer-flow/blob/a9b5dd80f8a52d1d6e66d6462d2635f7ca91d76f/skills/public/systematic-literature-review/SKILL.md#L120) | 跨文献合并主题、差异和矛盾，报告实际覆盖。 | [判定与交付](report.md) |

配套定位：[arxiv_search.py](https://github.com/bytedance/deer-flow/blob/a9b5dd80f8a52d1d6e66d6462d2635f7ca91d76f/skills/public/systematic-literature-review/scripts/arxiv_search.py) · [bibtex.md](https://github.com/bytedance/deer-flow/blob/a9b5dd80f8a52d1d6e66d6462d2635f7ca91d76f/skills/public/systematic-literature-review/templates/bibtex.md)

<a id="s720"></a>

### novelty-check · rrrrrick741/academic-writing-skills

[固定版本原文](https://github.com/rrrrrick741/academic-writing-skills/blob/e03430faefd678e57a103e80c8ee186abdb08fe2/skills/novelty-check/SKILL.md)

| 原文位置 | 转成什么操作 | 去向 |
| --- | --- | --- |
| [检索已有工作](https://github.com/rrrrrick741/academic-writing-skills/blob/e03430faefd678e57a103e80c8ee186abdb08fe2/skills/novelty-check/SKILL.md#L12) | 既检索直接前作，也检查已有综述如何给方法分类。 | [检索与补检](search.md) |
| [相似度评估](https://github.com/rrrrrick741/academic-writing-skills/blob/e03430faefd678e57a103e80c8ee186abdb08fe2/skills/novelty-check/SKILL.md#L17) | 逐项标相似、不同和发表时间。 | [原文、版本及矩阵](comparison.md) |
| [新颖性评分](https://github.com/rrrrrick741/academic-writing-skills/blob/e03430faefd678e57a103e80c8ee186abdb08fe2/skills/novelty-check/SKILL.md#L23) | 分开方法、问题、发现和组合；分数只作候选排序。 | [反方质询与等价性](extended-review.md) |
| [改进建议](https://github.com/rrrrrick741/academic-writing-skills/blob/e03430faefd678e57a103e80c8ee186abdb08fe2/skills/novelty-check/SKILL.md#L31) | 重定义假设、约束或比较，并说明新增证据是什么。 | [判定与交付](report.md) |

<a id="s2755"></a>

### literature-review-master · franklee16/academic-research-skills

[固定版本原文](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/SKILL.md)

| 原文位置 | 转成什么操作 | 去向 |
| --- | --- | --- |
| [Top-level modes](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/SKILL.md#L33) | 选关键前作、构想验证、理论可行性或引文审核入口。 | [立项与范围](../SKILL.md) |
| [Citation evidence gate](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/SKILL.md#L82) | 先固定主张，再做出处核验与主张支持核验。 | [原文、版本及矩阵](comparison.md) |
| [Verdict system](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/SKILL.md#L106) | 对决定性论文解释为何应维持、收窄或放弃特定主张。 | [判定与交付](report.md) |

配套定位：[05-killer-paper-protocol.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/references/05-killer-paper-protocol.md) · [06-framework-vs-cosmetic-test.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/references/06-framework-vs-cosmetic-test.md) · [07-three-pass-reading.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/references/07-three-pass-reading.md) · [13-bias-and-known-unknowns.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/references/13-bias-and-known-unknowns.md) · [14-rolling-update.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/references/14-rolling-update.md) · [24-claim-citation-evidence-gate.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/references/24-claim-citation-evidence-gate.md) · [numerical_table_verification_agent.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/agents/numerical_table_verification_agent.md)

<a id="s433"></a>

### lit-positioning · juanmontiz/peper-skills-suite

[固定版本原文](https://github.com/juanmontiz/peper-skills-suite/blob/3a62d5afb9745a272e9d7f4c4b90ffb08ebc0f67/lit-positioning/SKILL.md)

| 原文位置 | 转成什么操作 | 去向 |
| --- | --- | --- |
| [Map the landscape](https://github.com/juanmontiz/peper-skills-suite/blob/3a62d5afb9745a272e9d7f4c4b90ffb08ebc0f67/lit-positioning/SKILL.md#L15) | 从最接近的若干工作扩到经典、竞争与新近路线。 | [检索与补检](search.md) |
| [Verify every reference](https://github.com/juanmontiz/peper-skills-suite/blob/3a62d5afb9745a272e9d7f4c4b90ffb08ebc0f67/lit-positioning/SKILL.md#L34) | 同时验证文献身份和内容支持力度。 | [原文、版本及矩阵](comparison.md) |
| [Position the result](https://github.com/juanmontiz/peper-skills-suite/blob/3a62d5afb9745a272e9d7f4c4b90ffb08ebc0f67/lit-positioning/SKILL.md#L50) | 把复现、拓展、反驳分开。 | [反方质询与等价性](extended-review.md) |
| [Conceptual mapping](https://github.com/juanmontiz/peper-skills-suite/blob/3a62d5afb9745a272e9d7f4c4b90ffb08ebc0f67/lit-positioning/SKILL.md#L69) | 类比须写明结构对应和断裂处。 | [反方质询与等价性](extended-review.md) |

配套定位：[citation_integrity.md](https://github.com/juanmontiz/peper-skills-suite/blob/3a62d5afb9745a272e9d7f4c4b90ffb08ebc0f67/lit-positioning/references/citation_integrity.md) · [conceptual_mapping.md](https://github.com/juanmontiz/peper-skills-suite/blob/3a62d5afb9745a272e9d7f4c4b90ffb08ebc0f67/lit-positioning/references/conceptual_mapping.md) · [positioning_playbook.md](https://github.com/juanmontiz/peper-skills-suite/blob/3a62d5afb9745a272e9d7f4c4b90ffb08ebc0f67/lit-positioning/references/positioning_playbook.md) · [verify_refs.py](https://github.com/juanmontiz/peper-skills-suite/blob/3a62d5afb9745a272e9d7f4c4b90ffb08ebc0f67/lit-positioning/scripts/verify_refs.py)

<a id="s2959"></a>

### literature-review · pinshuai/literature-review-skill

[固定版本原文](https://github.com/pinshuai/literature-review-skill/blob/ed62a2899202707b58e87e4cd6ae45792772fe58/SKILL.md)

| 原文位置 | 转成什么操作 | 去向 |
| --- | --- | --- |
| [Systematic Literature Search](https://github.com/pinshuai/literature-review-skill/blob/ed62a2899202707b58e87e4cd6ae45792772fe58/SKILL.md#L97) | 跨库形成搜索轮次，日志保留每次的渠道与式子。 | [检索与补检](search.md) |
| [Screening and Selection](https://github.com/pinshuai/literature-review-skill/blob/ed62a2899202707b58e87e4cd6ae45792772fe58/SKILL.md#L175) | 预设纳排，去重和版本归并后记录筛选结果。 | [召回、筛选与更新](search.md) |
| [Quality Assessment](https://github.com/pinshuai/literature-review-skill/blob/ed62a2899202707b58e87e4cd6ae45792772fe58/SKILL.md#L220) | 按主题对照数据质量和证据适用性。 | [原文、版本及矩阵](comparison.md) |
| [Citation Verification](https://github.com/pinshuai/literature-review-skill/blob/ed62a2899202707b58e87e4cd6ae45792772fe58/SKILL.md#L280) | 把 DOI 核对与内容核对分开；高引与发表场所只协助发现。 | [判定与交付](report.md) |

配套定位：[review_template.md](https://github.com/pinshuai/literature-review-skill/blob/ed62a2899202707b58e87e4cd6ae45792772fe58/assets/review_template.md) · [verify_citations.py](https://github.com/pinshuai/literature-review-skill/blob/ed62a2899202707b58e87e4cd6ae45792772fe58/scripts/verify_citations.py)

<a id="s416"></a>

### research-idea-forge · ppsdk/research-idea-forge

[固定版本原文](https://github.com/ppsdk/research-idea-forge/blob/48494d8eb553b704f3a02882686ba49551a5521f/research-idea-forge/SKILL.md)

| 原文位置 | 转成什么操作 | 去向 |
| --- | --- | --- |
| [恢复研究契约](https://github.com/ppsdk/research-idea-forge/blob/48494d8eb553b704f3a02882686ba49551a5521f/research-idea-forge/SKILL.md#L52) | 锁定主张的范围与资源，不因检索结果擅自更换目标。 | [立项与范围](../SKILL.md) |
| [用文献收窄差异](https://github.com/ppsdk/research-idea-forge/blob/48494d8eb553b704f3a02882686ba49551a5521f/research-idea-forge/SKILL.md#L68) | 检索同机制异名、近邻、来源机制和失败证据。 | [检索与补检](search.md) |
| [完成入口契约](https://github.com/ppsdk/research-idea-forge/blob/48494d8eb553b704f3a02882686ba49551a5521f/research-idea-forge/SKILL.md#L74) | 明确迁移保留的结构、数学操作改动和组合的增量。 | [反方质询与等价性](extended-review.md) |
| [检查自洽](https://github.com/ppsdk/research-idea-forge/blob/48494d8eb553b704f3a02882686ba49551a5521f/research-idea-forge/SKILL.md#L84) | 用极限、反例和最小实验说明如何证伪残余差异。 | [判定与交付](report.md) |

配套定位：[mechanism-transfer.md](https://github.com/ppsdk/research-idea-forge/blob/48494d8eb553b704f3a02882686ba49551a5521f/research-idea-forge/references/mechanism-transfer.md) · [mathematical-construction.md](https://github.com/ppsdk/research-idea-forge/blob/48494d8eb553b704f3a02882686ba49551a5521f/research-idea-forge/references/mathematical-construction.md) · [novelty-and-coherence.md](https://github.com/ppsdk/research-idea-forge/blob/48494d8eb553b704f3a02882686ba49551a5521f/research-idea-forge/references/novelty-and-coherence.md) · [validation-and-feasibility.md](https://github.com/ppsdk/research-idea-forge/blob/48494d8eb553b704f3a02882686ba49551a5521f/research-idea-forge/references/validation-and-feasibility.md)

<a id="s423"></a>

### novelty-check · wanshuiyin/Auto-claude-code-research-in-sleep（ARIS 原版）

[固定版本原文](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/4ba94ae2a1c1fbbb14858750dd8764cabf6c28bd/skills/novelty-check/SKILL.md)

| 原文位置 | 转成什么操作 | 去向 |
| --- | --- | --- |
| [Phase A](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/4ba94ae2a1c1fbbb14858750dd8764cabf6c28bd/skills/novelty-check/SKILL.md#L32) | 分拆新方法、发现和条件；给每项写出足以推翻它的前作。 | [主张与查询](aris-review.md) |
| [Phase B](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/4ba94ae2a1c1fbbb14858750dd8764cabf6c28bd/skills/novelty-check/SKILL.md#L40)、[近期更新](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/4ba94ae2a1c1fbbb14858750dd8764cabf6c28bd/skills/novelty-check/SKILL.md#L150) | 每项主张至少三种不同问题导向的查询，覆盖适用数据库与截止日前六个月的近期成果，同时查早期工作。 | [查询与检索日志](aris-review.md) |
| [文献核验](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/4ba94ae2a1c1fbbb14858750dd8764cabf6c28bd/skills/novelty-check/SKILL.md#L151) | 核实身份并打开原文判重合；保留待核、服务暂不可用及手工核实的不同状态。 | [身份与近邻](aris-review.md) |
| [Phase C](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/4ba94ae2a1c1fbbb14858750dd8764cabf6c28bd/skills/novelty-check/SKILL.md#L55)、[裁决边界](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/4ba94ae2a1c1fbbb14858750dd8764cabf6c28bd/skills/novelty-check/SKILL.md#L83) | 将无预设结论的材料包交给独立评审，优先跨家族；按真实身份、返回及范围定性。 | [评审包及提示词](aris-review.md) |
| [Phase D](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/4ba94ae2a1c1fbbb14858750dd8764cabf6c28bd/skills/novelty-check/SKILL.md#L108)、[Review Tracing](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/4ba94ae2a1c1fbbb14858750dd8764cabf6c28bd/skills/novelty-check/SKILL.md#L153) | 以具体前作支持撤回，明确有争议的差异、并行工作与可保留的发现；留存审查依据。 | [复核与报告](aris-review.md) |

本条为第 21 个直接来源。原清单中的 Giovanni-Sforza 亦保留为独立来源，该仓库作者另已说明其项目从 ARIS 发展而来。[衍生项目的来源声明](https://github.com/Giovanni-Sforza/idea-survey-pipeline_claude/blob/7fa71ad0ef6dedcb5271c6bf69c343dddbc5a237/README.md#L3)

各来源的配套文件及其用途另见[配套材料与方法索引](component-index.md)。
