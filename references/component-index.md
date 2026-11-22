# 配套材料与方法索引

逐来源列出技能入口、所在技能目录内的材料，以及正文引用到的配套文件。链接固定到当时的提交。相邻技能的入口只用于确定交接；仓库总目录、第三方库和与本任务无关的项目文档不作为研究方法。各组的处理说明可点击回到相应的中文手册。原文章节中的具体操作见[方法对照](source-map.md)。

## novelty-check · ARIS 原版（第 21 个直接来源）

原精选 20 项之外，新增本条。固定到同一提交的 8 个文件及其用途如下。独立技能执行[本地复核规程](aris-review.md)；表中的上游工具未随包复制。

| 固定版本文件 | 整合用途 |
| --- | --- |
| [查新入口](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/4ba94ae2a1c1fbbb14858750dd8764cabf6c28bd/skills/novelty-check/SKILL.md) | 主张拆分、逐项多式检索、近六个月、独立复核及去留报告。 |
| [引文与核实](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/4ba94ae2a1c1fbbb14858750dd8764cabf6c28bd/skills/shared-references/citation-discipline.md) | 文献身份、版本和具体主张的证据须分别核实。 |
| [配套工具解析](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/4ba94ae2a1c1fbbb14858750dd8764cabf6c28bd/skills/shared-references/integration-contract.md) | 已安装上游时识别受信任的脚本；不可用则明确标记。 |
| [评审后端](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/4ba94ae2a1c1fbbb14858750dd8764cabf6c28bd/skills/shared-references/reviewer-backends.md) | 核对真实模型、是否完成、审查范围与返回证据。 |
| [评审记录规范](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/4ba94ae2a1c1fbbb14858750dd8764cabf6c28bd/skills/shared-references/review-tracing.md) | 记录真实请求及反馈，完整、元数据或关闭留存按用户设置。 |
| [论文核验实现](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/4ba94ae2a1c1fbbb14858750dd8764cabf6c28bd/tools/verify_papers.py) | 按标识符查询 arXiv、Crossref 或 Semantic Scholar，区分未匹配和暂时故障。 |
| [评审路由实现](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/4ba94ae2a1c1fbbb14858750dd8764cabf6c28bd/tools/reviewer_route.py) | 选取可用后端；请求的模型不能代替实际身份。 |
| [留痕实现](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/4ba94ae2a1c1fbbb14858750dd8764cabf6c28bd/tools/save_trace.sh) | 按实际调用保存请求、结果与元数据。 |

## research-novelty-review · yananlong/codex-skills

[原文章节与操作](source-map.md#s714)。下列 19 份可读文件按用途归并。

- **原始技能入口**　入口的操作与取舍按原文章节逐项对应。 [整合位置](source-map.md)
  [SKILL.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-novelty-review/SKILL.md)
- **检索设计、术语、召回与来源选择**　将数据库的查询、覆盖与失败条件用于检索记录。 [整合位置](search.md)
  [references/adversarial-query-patterns.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-novelty-review/references/adversarial-query-patterns.md) · [references/search-log-template.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-novelty-review/references/search-log-template.md)
- **判断、报告及更新**　整理结论、证据指向、未决点和增量修订，格式按本次交付选用。 [整合位置](report.md)
  [references/decision-scale.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-novelty-review/references/decision-scale.md) · [references/paper-review-integration.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-novelty-review/references/paper-review-integration.md) · [research/research-pipeline-planner/references/suite-contract.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-pipeline-planner/references/suite-contract.md)
- **比较矩阵、跨领域定位与信息综合**　以相同尺度对照机制、条件和结果，保留分歧与边界。 [整合位置](comparison.md)
  [references/domain-adapters.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-novelty-review/references/domain-adapters.md) · [references/prior-art-matrix-template.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-novelty-review/references/prior-art-matrix-template.md)
- **重合、等价、反例和数值检验**　复原最不利证据、实际操作和成立条件，检查反例能否消解主张。 [整合位置](extended-review.md)
  [references/literature-assurance-contract.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-novelty-review/references/literature-assurance-contract.md) · [references/novelty-checklist.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-novelty-review/references/novelty-checklist.md) · [references/overlap-scoring-rubric.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-novelty-review/references/overlap-scoring-rubric.md) · [references/reviewer-objection-rubric.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-novelty-review/references/reviewer-objection-rubric.md) · [scripts/claim_trajectory.py](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-novelty-review/scripts/claim_trajectory.py) · [scripts/init_novelty_pack.py](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-novelty-review/scripts/init_novelty_pack.py) · [scripts/novelty_assurance.py](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-novelty-review/scripts/novelty_assurance.py) · [scripts/validate_novelty_pack.py](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-novelty-review/scripts/validate_novelty_pack.py) · [research/research-pipeline-planner/references/epistemic-assurance-contract.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-pipeline-planner/references/epistemic-assurance-contract.md) · [research/research-systematic-literature-review/scripts/paper_context_artifacts.py](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-systematic-literature-review/scripts/paper_context_artifacts.py)
- **去重、版本、全文和论文卡**　保留来源身份、读到的位置与文献版本，比较强候选时回到原文。 [整合位置](comparison.md)
  [writing/technical-writing-drafter/references/drafting-contract.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/writing/technical-writing-drafter/references/drafting-contract.md)

## research-systematic-literature-review · yananlong/codex-skills

[原文章节与操作](source-map.md#s3197)。下列 21 份可读文件按用途归并。

- **原始技能入口**　入口的操作与取舍按原文章节逐项对应。 [整合位置](source-map.md)
  [SKILL.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-systematic-literature-review/SKILL.md)
- **重合、等价、反例和数值检验**　复原最不利证据、实际操作和成立条件，检查反例能否消解主张。 [整合位置](extended-review.md)
  [references/adversarial-literature-checklist.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-systematic-literature-review/references/adversarial-literature-checklist.md) · [references/claim-cards-and-source-ladder.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-systematic-literature-review/references/claim-cards-and-source-ladder.md) · [references/domain-adapters.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-systematic-literature-review/references/domain-adapters.md) · [references/evidence-table-template.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-systematic-literature-review/references/evidence-table-template.md) · [scripts/paper_context_artifacts.py](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-systematic-literature-review/scripts/paper_context_artifacts.py)
- **判断、报告及更新**　整理结论、证据指向、未决点和增量修订，格式按本次交付选用。 [整合位置](report.md)
  [references/paper-context-template.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-systematic-literature-review/references/paper-context-template.md) · [references/report-template.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-systematic-literature-review/references/report-template.md)
- **比较矩阵、跨领域定位与信息综合**　以相同尺度对照机制、条件和结果，保留分歧与边界。 [整合位置](comparison.md)
  [references/prisma-core-checklist.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-systematic-literature-review/references/prisma-core-checklist.md)
- **检索设计、术语、召回与来源选择**　将数据库的查询、覆盖与失败条件用于检索记录。 [整合位置](search.md)
  [references/protocol-template.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-systematic-literature-review/references/protocol-template.md) · [references/recall-assurance-contract.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-systematic-literature-review/references/recall-assurance-contract.md) · [references/search-strategy-template.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-systematic-literature-review/references/search-strategy-template.md) · [scripts/init_review_pack.py](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-systematic-literature-review/scripts/init_review_pack.py) · [scripts/search_log_rules.py](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-systematic-literature-review/scripts/search_log_rules.py)
- **去重、版本、全文和论文卡**　保留来源身份、读到的位置与文献版本，比较强候选时回到原文。 [整合位置](comparison.md)
  [references/screening-template.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-systematic-literature-review/references/screening-template.md) · [scripts/bib_inventory.py](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-systematic-literature-review/scripts/bib_inventory.py) · [writing/technical-writing-drafter/references/drafting-contract.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/writing/technical-writing-drafter/references/drafting-contract.md)
- **输入输出、格式及接口**　沿用完成本阶段判断所需的字段与边界；工具特定的存储和界面是可选实现。 [整合位置](../SKILL.md)
  [scripts/prisma_flow_md.py](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-systematic-literature-review/scripts/prisma_flow_md.py) · [scripts/review_pack_coverage.py](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-systematic-literature-review/scripts/review_pack_coverage.py) · [scripts/validate_review_pack.py](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-systematic-literature-review/scripts/validate_review_pack.py) · [research/research-zotero/references/zotero-artifact-contract.md](https://github.com/yananlong/codex-skills/blob/a9bad384ae7e04eea38ab5efb13529ae4b664575/research/research-zotero/references/zotero-artifact-contract.md)

## idea-novelty · Giovanni-Sforza/idea-survey-pipeline_claude

[原文章节与操作](source-map.md#s723)。下列 18 份可读文件按用途归并。

- **原始技能入口**　入口的操作与取舍按原文章节逐项对应。 [整合位置](source-map.md)
  [SKILL.md](https://github.com/Giovanni-Sforza/idea-survey-pipeline_claude/blob/7fa71ad0ef6dedcb5271c6bf69c343dddbc5a237/.claude/skills/idea-novelty/SKILL.md)
- **判断、报告及更新**　整理结论、证据指向、未决点和增量修订，格式按本次交付选用。 [整合位置](report.md)
  [.claude/skills/shared-references/output-language.md](https://github.com/Giovanni-Sforza/idea-survey-pipeline_claude/blob/7fa71ad0ef6dedcb5271c6bf69c343dddbc5a237/.claude/skills/shared-references/output-language.md) · [tools/wait_for_outputs.py](https://github.com/Giovanni-Sforza/idea-survey-pipeline_claude/blob/7fa71ad0ef6dedcb5271c6bf69c343dddbc5a237/tools/wait_for_outputs.py)
- **去重、版本、全文和论文卡**　保留来源身份、读到的位置与文献版本，比较强候选时回到原文。 [整合位置](comparison.md)
  [.claude/skills/shared-references/paper-card-contract.md](https://github.com/Giovanni-Sforza/idea-survey-pipeline_claude/blob/7fa71ad0ef6dedcb5271c6bf69c343dddbc5a237/.claude/skills/shared-references/paper-card-contract.md) · [templates/PAPER_CARD_SCHEMA.md](https://github.com/Giovanni-Sforza/idea-survey-pipeline_claude/blob/7fa71ad0ef6dedcb5271c6bf69c343dddbc5a237/templates/PAPER_CARD_SCHEMA.md) · [templates/PAPER_DEEP_ANALYSIS_TEMPLATE.md](https://github.com/Giovanni-Sforza/idea-survey-pipeline_claude/blob/7fa71ad0ef6dedcb5271c6bf69c343dddbc5a237/templates/PAPER_DEEP_ANALYSIS_TEMPLATE.md) · [tools/image_preprocessor.py](https://github.com/Giovanni-Sforza/idea-survey-pipeline_claude/blob/7fa71ad0ef6dedcb5271c6bf69c343dddbc5a237/tools/image_preprocessor.py) · [tools/paper_analyzer_orchestrator.py](https://github.com/Giovanni-Sforza/idea-survey-pipeline_claude/blob/7fa71ad0ef6dedcb5271c6bf69c343dddbc5a237/tools/paper_analyzer_orchestrator.py) · [tools/papers_pool.py](https://github.com/Giovanni-Sforza/idea-survey-pipeline_claude/blob/7fa71ad0ef6dedcb5271c6bf69c343dddbc5a237/tools/papers_pool.py) · [tools/pdf_figure_extractor.py](https://github.com/Giovanni-Sforza/idea-survey-pipeline_claude/blob/7fa71ad0ef6dedcb5271c6bf69c343dddbc5a237/tools/pdf_figure_extractor.py) · [tools/pdf_vision_parser.py](https://github.com/Giovanni-Sforza/idea-survey-pipeline_claude/blob/7fa71ad0ef6dedcb5271c6bf69c343dddbc5a237/tools/pdf_vision_parser.py)
- **输入输出、格式及接口**　沿用完成本阶段判断所需的字段与边界；工具特定的存储和界面是可选实现。 [整合位置](../SKILL.md)
  [.claude/skills/shared-references/survey-fanout-protocol.md](https://github.com/Giovanni-Sforza/idea-survey-pipeline_claude/blob/7fa71ad0ef6dedcb5271c6bf69c343dddbc5a237/.claude/skills/shared-references/survey-fanout-protocol.md) · [tools/latex_source_parser.py](https://github.com/Giovanni-Sforza/idea-survey-pipeline_claude/blob/7fa71ad0ef6dedcb5271c6bf69c343dddbc5a237/tools/latex_source_parser.py) · [tools/pdf_full_parser.py](https://github.com/Giovanni-Sforza/idea-survey-pipeline_claude/blob/7fa71ad0ef6dedcb5271c6bf69c343dddbc5a237/tools/pdf_full_parser.py)
- **重合、等价、反例和数值检验**　复原最不利证据、实际操作和成立条件，检查反例能否消解主张。 [整合位置](extended-review.md)
  [templates/IDEA_NOVELTY_TEMPLATE.md](https://github.com/Giovanni-Sforza/idea-survey-pipeline_claude/blob/7fa71ad0ef6dedcb5271c6bf69c343dddbc5a237/templates/IDEA_NOVELTY_TEMPLATE.md)
- **检索设计、术语、召回与来源选择**　将数据库的查询、覆盖与失败条件用于检索记录。 [整合位置](search.md)
  [tools/arxiv_fetch.py](https://github.com/Giovanni-Sforza/idea-survey-pipeline_claude/blob/7fa71ad0ef6dedcb5271c6bf69c343dddbc5a237/tools/arxiv_fetch.py) · [tools/research_wiki.py](https://github.com/Giovanni-Sforza/idea-survey-pipeline_claude/blob/7fa71ad0ef6dedcb5271c6bf69c343dddbc5a237/tools/research_wiki.py) · [tools/semantic_scholar_fetch.py](https://github.com/Giovanni-Sforza/idea-survey-pipeline_claude/blob/7fa71ad0ef6dedcb5271c6bf69c343dddbc5a237/tools/semantic_scholar_fetch.py)

## research-question-validator · stephenturner/skill-research-question-validator

[原文章节与操作](source-map.md#s692)。下列 1 份可读文件按用途归并。

- **原始技能入口**　入口的操作与取舍按原文章节逐项对应。 [整合位置](source-map.md)
  [SKILL.md](https://github.com/stephenturner/skill-research-question-validator/blob/06fe29a993a3553e8948a6c98f4eb81c1fc60ddf/SKILL.md)

## novelty-assessment · muye1112/skill

[原文章节与操作](source-map.md#s432)。下列 2 份可读文件按用途归并。

- **原始技能入口**　入口的操作与取舍按原文章节逐项对应。 [整合位置](source-map.md)
  [SKILL.md](https://github.com/muye1112/skill/blob/fa7df033b3d51e2f8774f51a83e91b5aeecd4e55/skills/novelty-assessment/SKILL.md)
- **重合、等价、反例和数值检验**　复原最不利证据、实际操作和成立条件，检查反例能否消解主张。 [整合位置](extended-review.md)
  [references/assessment-prompts.md](https://github.com/muye1112/skill/blob/fa7df033b3d51e2f8774f51a83e91b5aeecd4e55/skills/novelty-assessment/references/assessment-prompts.md)

## paper-novelty-check · AlexYangge/paper-research-skills

[原文章节与操作](source-map.md#s708)。下列 3 份可读文件按用途归并。

- **原始技能入口**　入口的操作与取舍按原文章节逐项对应。 [整合位置](source-map.md)
  [SKILL.md](https://github.com/AlexYangge/paper-research-skills/blob/cc96a465c52525e9912f5a6e57e87de0c6064fdf/paper-novelty-check/SKILL.md)
- **去重、版本、全文和论文卡**　保留来源身份、读到的位置与文献版本，比较强候选时回到原文。 [整合位置](comparison.md)
  [scripts/dedupe.py](https://github.com/AlexYangge/paper-research-skills/blob/cc96a465c52525e9912f5a6e57e87de0c6064fdf/paper-novelty-check/scripts/dedupe.py)
- **检索设计、术语、召回与来源选择**　将数据库的查询、覆盖与失败条件用于检索记录。 [整合位置](search.md)
  [paper-topic-selection/references/search-strategies.md](https://github.com/AlexYangge/paper-research-skills/blob/cc96a465c52525e9912f5a6e57e87de0c6064fdf/paper-topic-selection/references/search-strategies.md)

## Novelty Check · sacrrie/skill-novelty-checker

[原文章节与操作](source-map.md#s746)。下列 8 份可读文件按用途归并。

- **原始技能入口**　入口的操作与取舍按原文章节逐项对应。 [整合位置](source-map.md)
  [SKILL.md](https://github.com/sacrrie/skill-novelty-checker/blob/d981b166d56813dcd4426d757b1b69615504169e/SKILL.md)
- **案例、领域示范或测试**　用于检查边界和取舍；案例里的数据、领域偏好和预期效果不作为通用规则。 [整合位置](source-map.md)
  [examples/computer_vision_journals.csv](https://github.com/sacrrie/skill-novelty-checker/blob/d981b166d56813dcd4426d757b1b69615504169e/examples/computer_vision_journals.csv) · [examples/demo_novelty_check.py](https://github.com/sacrrie/skill-novelty-checker/blob/d981b166d56813dcd4426d757b1b69615504169e/examples/demo_novelty_check.py) · [examples/multidisciplinary_journals.csv](https://github.com/sacrrie/skill-novelty-checker/blob/d981b166d56813dcd4426d757b1b69615504169e/examples/multidisciplinary_journals.csv) · [examples/remote_sensing_journals.csv](https://github.com/sacrrie/skill-novelty-checker/blob/d981b166d56813dcd4426d757b1b69615504169e/examples/remote_sensing_journals.csv) · [examples/simple_journal_list.csv](https://github.com/sacrrie/skill-novelty-checker/blob/d981b166d56813dcd4426d757b1b69615504169e/examples/simple_journal_list.csv)
- **重合、等价、反例和数值检验**　复原最不利证据、实际操作和成立条件，检查反例能否消解主张。 [整合位置](extended-review.md)
  [sample_config.yaml](https://github.com/sacrrie/skill-novelty-checker/blob/d981b166d56813dcd4426d757b1b69615504169e/sample_config.yaml) · [scripts/novelty_check.py](https://github.com/sacrrie/skill-novelty-checker/blob/d981b166d56813dcd4426d757b1b69615504169e/scripts/novelty_check.py)

## novelty-check · sunnnybala/rstack

[原文章节与操作](source-map.md#s686)。下列 1 份可读文件按用途归并。

- **原始技能入口**　入口的操作与取舍按原文章节逐项对应。 [整合位置](source-map.md)
  [SKILL.md](https://github.com/sunnnybala/rstack/blob/3cf7ac1edaf6bcfc5c05f86a7d4bbcc2ed99f9ec/novelty-check/SKILL.md)

## positioning-engine · TobiasBlask/open-paper-machine

[原文章节与操作](source-map.md#s693)。下列 12 份可读文件按用途归并。

- **输入输出、格式及接口**　沿用完成本阶段判断所需的字段与边界；工具特定的存储和界面是可选实现。 [整合位置](../SKILL.md)
  [.claude-plugin/plugin.json](https://github.com/TobiasBlask/open-paper-machine/blob/160df4d13d266411f0850c4de7ecdbd93e8b40be/.claude-plugin/plugin.json) · [paper/paper.tex](https://github.com/TobiasBlask/open-paper-machine/blob/160df4d13d266411f0850c4de7ecdbd93e8b40be/paper/paper.tex)
- **重合、等价、反例和数值检验**　复原最不利证据、实际操作和成立条件，检查反例能否消解主张。 [整合位置](extended-review.md)
  [agents/idea-critic.md](https://github.com/TobiasBlask/open-paper-machine/blob/160df4d13d266411f0850c4de7ecdbd93e8b40be/agents/idea-critic.md) · [outputs/revision_log_r1.md](https://github.com/TobiasBlask/open-paper-machine/blob/160df4d13d266411f0850c4de7ecdbd93e8b40be/outputs/revision_log_r1.md) · [simulated_reviews.md](https://github.com/TobiasBlask/open-paper-machine/blob/160df4d13d266411f0850c4de7ecdbd93e8b40be/simulated_reviews.md)
- **检索设计、术语、召回与来源选择**　将数据库的查询、覆盖与失败条件用于检索记录。 [整合位置](search.md)
  [agents/paper-machine.md](https://github.com/TobiasBlask/open-paper-machine/blob/160df4d13d266411f0850c4de7ecdbd93e8b40be/agents/paper-machine.md) · [principles/research-strategy.md](https://github.com/TobiasBlask/open-paper-machine/blob/160df4d13d266411f0850c4de7ecdbd93e8b40be/principles/research-strategy.md) · [writing_analysis.md](https://github.com/TobiasBlask/open-paper-machine/blob/160df4d13d266411f0850c4de7ecdbd93e8b40be/writing_analysis.md)
- **判断、报告及更新**　整理结论、证据指向、未决点和增量修订，格式按本次交付选用。 [整合位置](report.md)
  [outputs/orchestration_log.md](https://github.com/TobiasBlask/open-paper-machine/blob/160df4d13d266411f0850c4de7ecdbd93e8b40be/outputs/orchestration_log.md)
- **比较矩阵、跨领域定位与信息综合**　以相同尺度对照机制、条件和结果，保留分歧与边界。 [整合位置](comparison.md)
  [outputs/revision_letter.md](https://github.com/TobiasBlask/open-paper-machine/blob/160df4d13d266411f0850c4de7ecdbd93e8b40be/outputs/revision_letter.md)
- **去重、版本、全文和论文卡**　保留来源身份、读到的位置与文献版本，比较强候选时回到原文。 [整合位置](comparison.md)
  [scripts/md_to_latex.py](https://github.com/TobiasBlask/open-paper-machine/blob/160df4d13d266411f0850c4de7ecdbd93e8b40be/scripts/md_to_latex.py)
- **原始技能入口**　入口的操作与取舍按原文章节逐项对应。 [整合位置](source-map.md)
  [SKILL.md](https://github.com/TobiasBlask/open-paper-machine/blob/160df4d13d266411f0850c4de7ecdbd93e8b40be/skills/positioning-engine/SKILL.md)

## related-work-positioning · UCL-ERL/skills

[原文章节与操作](source-map.md#s687)。下列 2 份可读文件按用途归并。

- **原始技能入口**　入口的操作与取舍按原文章节逐项对应。 [整合位置](source-map.md)
  [SKILL.md](https://github.com/UCL-ERL/skills/blob/9d50603850b661a1da175ef3e330ba0b52e3efe9/skills/writing/related-work-positioning/SKILL.md)
- **比较矩阵、跨领域定位与信息综合**　以相同尺度对照机制、条件和结果，保留分歧与边界。 [整合位置](comparison.md)
  [references/positioning-checks.md](https://github.com/UCL-ERL/skills/blob/9d50603850b661a1da175ef3e330ba0b52e3efe9/skills/writing/related-work-positioning/references/positioning-checks.md)

## idea-novelty-auditor · yujie-jason-zhang/polish_skill

[原文章节与操作](source-map.md#s431)。下列 2 份可读文件按用途归并。

- **原始技能入口**　入口的操作与取舍按原文章节逐项对应。 [整合位置](source-map.md)
  [SKILL.md](https://github.com/yujie-jason-zhang/polish_skill/blob/9b2a86ca6ac88879a3d3490fecdb909673fd1562/idea-novelty-auditor/SKILL.md)
- **重合、等价、反例和数值检验**　复原最不利证据、实际操作和成立条件，检查反例能否消解主张。 [整合位置](extended-review.md)
  [references/idea_novelty_risk_audit.md](https://github.com/yujie-jason-zhang/polish_skill/blob/9b2a86ca6ac88879a3d3490fecdb909673fd1562/idea-novelty-auditor/references/idea_novelty_risk_audit.md)

## literature-search · wangsir1214/my-claude-skills

[原文章节与操作](source-map.md#s747)。下列 1 份可读文件按用途归并。

- **原始技能入口**　入口的操作与取舍按原文章节逐项对应。 [整合位置](source-map.md)
  [SKILL.md](https://github.com/wangsir1214/my-claude-skills/blob/629ec90a474c5a73d78cfbe71d6f97fb2285ec69/skills/literature-search/SKILL.md)

## literature-search · dynamor2019/xiao-jia-ai-paper-writing-platform

[原文章节与操作](source-map.md#s719)。下列 1 份可读文件按用途归并。

- **原始技能入口**　入口的操作与取舍按原文章节逐项对应。 [整合位置](source-map.md)
  [SKILL.md](https://github.com/dynamor2019/xiao-jia-ai-paper-writing-platform/blob/9cd68c1368e84b7ff6838a2446cc9e29a0302b2b/.dsh/skills/literature-search/SKILL.md)

## hypothesis-stress-test · Aditya-Tandon/claude-research-skills

[原文章节与操作](source-map.md#s732)。下列 3 份可读文件按用途归并。

- **判断、报告及更新**　整理结论、证据指向、未决点和增量修订，格式按本次交付选用。 [整合位置](report.md)
  [references/vault-conventions.md](https://github.com/Aditya-Tandon/claude-research-skills/blob/4664d1ca1c90f89a835457b83446b52a969c87c2/references/vault-conventions.md)
- **比较矩阵、跨领域定位与信息综合**　以相同尺度对照机制、条件和结果，保留分歧与边界。 [整合位置](comparison.md)
  [references/writing-guide.md](https://github.com/Aditya-Tandon/claude-research-skills/blob/4664d1ca1c90f89a835457b83446b52a969c87c2/references/writing-guide.md)
- **原始技能入口**　入口的操作与取舍按原文章节逐项对应。 [整合位置](source-map.md)
  [SKILL.md](https://github.com/Aditya-Tandon/claude-research-skills/blob/4664d1ca1c90f89a835457b83446b52a969c87c2/skills/hypothesis-stress-test/SKILL.md)

## systematic-literature-review · bytedance/deer-flow

[原文章节与操作](source-map.md#s771)。下列 6 份可读文件按用途归并。

- **输入输出、格式及接口**　沿用完成本阶段判断所需的字段与边界；工具特定的存储和界面是可选实现。 [整合位置](../SKILL.md)
  [skills/public/github-deep-research/scripts/github_api.py](https://github.com/bytedance/deer-flow/blob/a9b5dd80f8a52d1d6e66d6462d2635f7ca91d76f/skills/public/github-deep-research/scripts/github_api.py)
- **原始技能入口**　入口的操作与取舍按原文章节逐项对应。 [整合位置](source-map.md)
  [SKILL.md](https://github.com/bytedance/deer-flow/blob/a9b5dd80f8a52d1d6e66d6462d2635f7ca91d76f/skills/public/systematic-literature-review/SKILL.md)
- **检索设计、术语、召回与来源选择**　将数据库的查询、覆盖与失败条件用于检索记录。 [整合位置](search.md)
  [scripts/arxiv_search.py](https://github.com/bytedance/deer-flow/blob/a9b5dd80f8a52d1d6e66d6462d2635f7ca91d76f/skills/public/systematic-literature-review/scripts/arxiv_search.py)
- **判断、报告及更新**　整理结论、证据指向、未决点和增量修订，格式按本次交付选用。 [整合位置](report.md)
  [templates/apa.md](https://github.com/bytedance/deer-flow/blob/a9b5dd80f8a52d1d6e66d6462d2635f7ca91d76f/skills/public/systematic-literature-review/templates/apa.md) · [templates/bibtex.md](https://github.com/bytedance/deer-flow/blob/a9b5dd80f8a52d1d6e66d6462d2635f7ca91d76f/skills/public/systematic-literature-review/templates/bibtex.md) · [templates/ieee.md](https://github.com/bytedance/deer-flow/blob/a9b5dd80f8a52d1d6e66d6462d2635f7ca91d76f/skills/public/systematic-literature-review/templates/ieee.md)

## novelty-check · rrrrrick741/academic-writing-skills

[原文章节与操作](source-map.md#s720)。下列 1 份可读文件按用途归并。

- **原始技能入口**　入口的操作与取舍按原文章节逐项对应。 [整合位置](source-map.md)
  [SKILL.md](https://github.com/rrrrrick741/academic-writing-skills/blob/e03430faefd678e57a103e80c8ee186abdb08fe2/skills/novelty-check/SKILL.md)

## literature-review-master · franklee16/academic-research-skills

[原文章节与操作](source-map.md#s2755)。下列 58 份可读文件按用途归并。

- **作者环境、包装与发布**　保留与工具可用性有关的前提；安装、调度、遥测、发布约定留给原项目。 [整合位置](../SKILL.md)
  [QUICK_START.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/QUICK_START.md) · [QUICK_START_CN.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/QUICK_START_CN.md)
- **原始技能入口**　入口的操作与取舍按原文章节逐项对应。 [整合位置](source-map.md)
  [SKILL.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/SKILL.md)
- **判断、报告及更新**　整理结论、证据指向、未决点和增量修订，格式按本次交付选用。 [整合位置](report.md)
  [agents/citation_verification_agent.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/agents/citation_verification_agent.md) · [agents/source_only_verification_agent.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/agents/source_only_verification_agent.md) · [database/citation_status_schema.json](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/database/citation_status_schema.json) · [docs/DETAILED_USAGE_GUIDE.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/docs/DETAILED_USAGE_GUIDE.md) · [references/12-citation-verification.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/references/12-citation-verification.md) · [references/14-rolling-update.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/references/14-rolling-update.md) · [references/15-reviewer-attack-defence.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/references/15-reviewer-attack-defence.md) · [references/26-source-only-verification.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/references/26-source-only-verification.md) · [templates/agent_task_board_template.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/templates/agent_task_board_template.md) · [templates/mode0_meta_decision_template.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/templates/mode0_meta_decision_template.md) · [templates/modeA_exploration_template.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/templates/modeA_exploration_template.md) · [templates/modeB_idea_validation_template.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/templates/modeB_idea_validation_template.md) · [templates/modeC_literature_tree_template.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/templates/modeC_literature_tree_template.md) · [templates/modeE_citation_verification_template.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/templates/modeE_citation_verification_template.md) · [templates/modeF_rolling_update_template.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/templates/modeF_rolling_update_template.md) · [templates/modeG_reviewer_attack_template.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/templates/modeG_reviewer_attack_template.md) · [templates/modeI_systematic_review_template.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/templates/modeI_systematic_review_template.md) · [templates/source_only_verification_template.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/templates/source_only_verification_template.md)
- **去重、版本、全文和论文卡**　保留来源身份、读到的位置与文献版本，比较强候选时回到原文。 [整合位置](comparison.md)
  [agents/claim_extraction_agent.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/agents/claim_extraction_agent.md) · [agents/corpus_triage_agent.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/agents/corpus_triage_agent.md) · [agents/deep_reading_agent.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/agents/deep_reading_agent.md) · [references/07-three-pass-reading.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/references/07-three-pass-reading.md) · [references/08-corpus-triage.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/references/08-corpus-triage.md) · [references/09-paper-note-protocol.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/references/09-paper-note-protocol.md) · [references/17-systematic-review-mode.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/references/17-systematic-review-mode.md) · [references/23-claim-extraction-protocol.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/references/23-claim-extraction-protocol.md) · [templates/claim_extraction_table_template.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/templates/claim_extraction_table_template.md) · [templates/corpus_log_template.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/templates/corpus_log_template.md) · [templates/paper_note_template.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/templates/paper_note_template.md)
- **重合、等价、反例和数值检验**　复原最不利证据、实际操作和成立条件，检查反例能否消解主张。 [整合位置](extended-review.md)
  [agents/evidence_gate_agent.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/agents/evidence_gate_agent.md) · [agents/killer_paper_agent.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/agents/killer_paper_agent.md) · [agents/literature_orchestrator_agent.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/agents/literature_orchestrator_agent.md) · [references/00-mode-router.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/references/00-mode-router.md) · [references/02-no-data-theory-simulation-filter.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/references/02-no-data-theory-simulation-filter.md) · [references/05-killer-paper-protocol.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/references/05-killer-paper-protocol.md) · [references/06-framework-vs-cosmetic-test.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/references/06-framework-vs-cosmetic-test.md) · [references/20-parallel-agent-workflow.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/references/20-parallel-agent-workflow.md) · [references/24-claim-citation-evidence-gate.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/references/24-claim-citation-evidence-gate.md) · [scripts/make_claim_citation_map.py](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/scripts/make_claim_citation_map.py) · [templates/citation_evidence_gate_template.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/templates/citation_evidence_gate_template.md) · [templates/claim_citation_map_template.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/templates/claim_citation_map_template.md)
- **比较矩阵、跨领域定位与信息综合**　以相同尺度对照机制、条件和结果，保留分歧与边界。 [整合位置](comparison.md)
  [agents/gap_hunter_agent.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/agents/gap_hunter_agent.md) · [references/04-gap-taxonomy.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/references/04-gap-taxonomy.md) · [references/10-cross-paper-synthesis.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/references/10-cross-paper-synthesis.md) · [references/18-theory-only-gap-viability.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/references/18-theory-only-gap-viability.md) · [templates/gap_matrix_template.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/templates/gap_matrix_template.md) · [templates/modeJ_theory_gap_template.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/templates/modeJ_theory_gap_template.md)
- **输入输出、格式及接口**　沿用完成本阶段判断所需的字段与边界；工具特定的存储和界面是可选实现。 [整合位置](../SKILL.md)
  [agents/no_data_viability_agent.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/agents/no_data_viability_agent.md) · [agents/red_team_literature_reviewer_agent.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/agents/red_team_literature_reviewer_agent.md) · [references/13-bias-and-known-unknowns.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/references/13-bias-and-known-unknowns.md) · [references/22-lesson-log.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/references/22-lesson-log.md)
- **检索设计、术语、召回与来源选择**　将数据库的查询、覆盖与失败条件用于检索记录。 [整合位置](search.md)
  [agents/search_query_architect_agent.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/agents/search_query_architect_agent.md) · [references/01-search-scope-ladder.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/references/01-search-scope-ladder.md)
- **案例、领域示范或测试**　用于检查边界和取舍；案例里的数据、领域偏好和预期效果不作为通用规则。 [整合位置](source-map.md)
  [examples/modeB_parallel_example.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/examples/modeB_parallel_example.md) · [examples/modeE_citation_evidence_gate_example.md](https://github.com/franklee16/academic-research-skills/blob/9a4b2db21fc4b217136ae4a0e6faad42d179ca03/lit-review/literature-review-master-main/examples/modeE_citation_evidence_gate_example.md)

## lit-positioning · juanmontiz/peper-skills-suite

[原文章节与操作](source-map.md#s433)。下列 5 份可读文件按用途归并。

- **原始技能入口**　入口的操作与取舍按原文章节逐项对应。 [整合位置](source-map.md)
  [SKILL.md](https://github.com/juanmontiz/peper-skills-suite/blob/3a62d5afb9745a272e9d7f4c4b90ffb08ebc0f67/lit-positioning/SKILL.md)
- **去重、版本、全文和论文卡**　保留来源身份、读到的位置与文献版本，比较强候选时回到原文。 [整合位置](comparison.md)
  [references/citation_integrity.md](https://github.com/juanmontiz/peper-skills-suite/blob/3a62d5afb9745a272e9d7f4c4b90ffb08ebc0f67/lit-positioning/references/citation_integrity.md) · [scripts/verify_refs.py](https://github.com/juanmontiz/peper-skills-suite/blob/3a62d5afb9745a272e9d7f4c4b90ffb08ebc0f67/lit-positioning/scripts/verify_refs.py)
- **比较矩阵、跨领域定位与信息综合**　以相同尺度对照机制、条件和结果，保留分歧与边界。 [整合位置](comparison.md)
  [references/conceptual_mapping.md](https://github.com/juanmontiz/peper-skills-suite/blob/3a62d5afb9745a272e9d7f4c4b90ffb08ebc0f67/lit-positioning/references/conceptual_mapping.md) · [references/positioning_playbook.md](https://github.com/juanmontiz/peper-skills-suite/blob/3a62d5afb9745a272e9d7f4c4b90ffb08ebc0f67/lit-positioning/references/positioning_playbook.md)

## literature-review · pinshuai/literature-review-skill

[原文章节与操作](source-map.md#s2959)。下列 10 份可读文件按用途归并。

- **原始技能入口**　入口的操作与取舍按原文章节逐项对应。 [整合位置](source-map.md)
  [SKILL.md](https://github.com/pinshuai/literature-review-skill/blob/ed62a2899202707b58e87e4cd6ae45792772fe58/SKILL.md)
- **判断、报告及更新**　整理结论、证据指向、未决点和增量修订，格式按本次交付选用。 [整合位置](report.md)
  [assets/review_template.md](https://github.com/pinshuai/literature-review-skill/blob/ed62a2899202707b58e87e4cd6ae45792772fe58/assets/review_template.md) · [references/citation_styles.md](https://github.com/pinshuai/literature-review-skill/blob/ed62a2899202707b58e87e4cd6ae45792772fe58/references/citation_styles.md) · [scripts/verify_citations.py](https://github.com/pinshuai/literature-review-skill/blob/ed62a2899202707b58e87e4cd6ae45792772fe58/scripts/verify_citations.py)
- **案例、领域示范或测试**　用于检查边界和取舍；案例里的数据、领域偏好和预期效果不作为通用规则。 [整合位置](source-map.md)
  [examples/wildfire-streamflow/sources/search_log.md](https://github.com/pinshuai/literature-review-skill/blob/ed62a2899202707b58e87e4cd6ae45792772fe58/examples/wildfire-streamflow/sources/search_log.md) · [examples/wildfire-streamflow/wildfire_streamflow_review.md](https://github.com/pinshuai/literature-review-skill/blob/ed62a2899202707b58e87e4cd6ae45792772fe58/examples/wildfire-streamflow/wildfire_streamflow_review.md) · [examples/wildfire-streamflow/wildfire_streamflow_review_citation_report.json](https://github.com/pinshuai/literature-review-skill/blob/ed62a2899202707b58e87e4cd6ae45792772fe58/examples/wildfire-streamflow/wildfire_streamflow_review_citation_report.json)
- **检索设计、术语、召回与来源选择**　将数据库的查询、覆盖与失败条件用于检索记录。 [整合位置](search.md)
  [references/database_strategies.md](https://github.com/pinshuai/literature-review-skill/blob/ed62a2899202707b58e87e4cd6ae45792772fe58/references/database_strategies.md) · [scripts/search_databases.py](https://github.com/pinshuai/literature-review-skill/blob/ed62a2899202707b58e87e4cd6ae45792772fe58/scripts/search_databases.py)
- **输入输出、格式及接口**　沿用完成本阶段判断所需的字段与边界；工具特定的存储和界面是可选实现。 [整合位置](../SKILL.md)
  [scripts/generate_pdf.py](https://github.com/pinshuai/literature-review-skill/blob/ed62a2899202707b58e87e4cd6ae45792772fe58/scripts/generate_pdf.py)

## research-idea-forge · ppsdk/research-idea-forge

[原文章节与操作](source-map.md#s416)。下列 11 份可读文件按用途归并。

- **原始技能入口**　入口的操作与取舍按原文章节逐项对应。 [整合位置](source-map.md)
  [SKILL.md](https://github.com/ppsdk/research-idea-forge/blob/48494d8eb553b704f3a02882686ba49551a5521f/research-idea-forge/SKILL.md)
- **输入输出、格式及接口**　沿用完成本阶段判断所需的字段与边界；工具特定的存储和界面是可选实现。 [整合位置](../SKILL.md)
  [assets/idea-card.zh.md](https://github.com/ppsdk/research-idea-forge/blob/48494d8eb553b704f3a02882686ba49551a5521f/research-idea-forge/assets/idea-card.zh.md) · [references/candidate-operators.md](https://github.com/ppsdk/research-idea-forge/blob/48494d8eb553b704f3a02882686ba49551a5521f/research-idea-forge/references/candidate-operators.md) · [references/validation-and-feasibility.md](https://github.com/ppsdk/research-idea-forge/blob/48494d8eb553b704f3a02882686ba49551a5521f/research-idea-forge/references/validation-and-feasibility.md)
- **作者环境、包装与发布**　保留与工具可用性有关的前提；安装、调度、遥测、发布约定留给原项目。 [整合位置](../SKILL.md)
  [references/contribution-and-selection.md](https://github.com/ppsdk/research-idea-forge/blob/48494d8eb553b704f3a02882686ba49551a5521f/research-idea-forge/references/contribution-and-selection.md)
- **重合、等价、反例和数值检验**　复原最不利证据、实际操作和成立条件，检查反例能否消解主张。 [整合位置](extended-review.md)
  [references/intake-and-evidence.md](https://github.com/ppsdk/research-idea-forge/blob/48494d8eb553b704f3a02882686ba49551a5521f/research-idea-forge/references/intake-and-evidence.md) · [references/mathematical-construction.md](https://github.com/ppsdk/research-idea-forge/blob/48494d8eb553b704f3a02882686ba49551a5521f/research-idea-forge/references/mathematical-construction.md) · [references/mechanism-transfer.md](https://github.com/ppsdk/research-idea-forge/blob/48494d8eb553b704f3a02882686ba49551a5521f/research-idea-forge/references/mechanism-transfer.md) · [references/novelty-and-coherence.md](https://github.com/ppsdk/research-idea-forge/blob/48494d8eb553b704f3a02882686ba49551a5521f/research-idea-forge/references/novelty-and-coherence.md)
- **判断、报告及更新**　整理结论、证据指向、未决点和增量修订，格式按本次交付选用。 [整合位置](report.md)
  [references/output-and-routing.md](https://github.com/ppsdk/research-idea-forge/blob/48494d8eb553b704f3a02882686ba49551a5521f/research-idea-forge/references/output-and-routing.md)
- **案例、领域示范或测试**　用于检查边界和取舍；案例里的数据、领域偏好和预期效果不作为通用规则。 [整合位置](source-map.md)
  [references/worked-examples.md](https://github.com/ppsdk/research-idea-forge/blob/48494d8eb553b704f3a02882686ba49551a5521f/research-idea-forge/references/worked-examples.md)
