# 怎样执行一次可复查的查新

在研究项目里给每次查新建目录，保留查询输出、筛选理由、原文证据和审查者的实际回复。下面的 `<skill>` 是本技能安装目录，`<case>` 是本次工作的目录。命令需要 Python 3.9 或以上。可用项目既有的学术 API、浏览器、图书馆接口或 ARIS 原工具完成检索与查证，按同一规则记账。

## 从公开术语开始检索

```text
python "<skill>/scripts/check_dossier.py" init "<case>/dossier.json"
python "<skill>/scripts/search_papers.py" search --public-query "sea surface slope uplink optical propagation" --source both --limit 10 --output "<case>/query-01.json"
python "<skill>/scripts/search_papers.py" verify --id 10.3390/s25041239 --title "Modeling and Performance Analysis of Uplink Laser Transmission Across Sea Surfaces: A Channel Characterization Study" --source both --output "<case>/id-01.json"
```

第二条命令分别检索 Crossref 和 OpenAlex。一次请求两个索引仍只用了一种问法。用关键动作、同机制的别名及旧称另外检索，再用 `--from-date YYYY-MM-DD --until-date YYYY-MM-DD` 单查最近六个月。另查专业出版源、预印本和前后向引文。进入论文正文定位足以改变判断的证据。两个索引共享部分题录，搜索结果要去重。检索时只向公共服务传入公开术语或已发表文献的标识符。

## 填实际发生的记录

`init` 创建空骨架并保留已有文件。档案采用 UTF-8 JSON。下面列的是关键字段的填写方式。短编号在同一次查新和后续增量复检中保持稳定。

| 区块 | 要填写的内容 |
| --- | --- |
| `as_of` | 文献覆盖截止日，格式为 YYYY-MM-DD，默认为本次检索当日。历史查新可在此日期之后运行，须按指定日期过滤并核对上线时间。 |
| `queries[]` | 每个索引的每个实际请求一行。填 `id, claims, source, channel, formulation, query, status, date, from, to, total, screened, trace_file`。同一索引保持同一名字。channel 可填 index、specialist、preprint、online_first 或 citation。近期预印本或在线首发要用相应渠道实查。formulation 填动机，如“同机制旧称”。query 填真正发出的查询。from/to 是出版日期边界，无限制时填 null。请求有返回填 ok，分页中断且已筛过部分结果填 partial，完全无法执行填 unavailable，后两者填写 error。只有数据库确实报告零命中时 total 才填 0。不知道总数填 null。screened 只算实际查看的记录。将搜索返回及实际查阅范围写入相对路径 trace_file。 |
| `papers[]` | 为每篇关键前作填 `id, title, identifier, identity, reading, locator, evidence_file`。identifier 用可回查的 DOI、arXiv 编号或官方稳定地址。identity 取 verified 或 unverified。reading 取 original、abstract 或 metadata。locator 写精确节、式、图、页或补充材料位置。在 evidence_file 中记版本与核准来源、观察、适用条件及其排除的强主张；可为同篇不同结论保存多处证据。 |
| `claims[]` | 填 `id, text, falsifier, verdict, reason, papers, comparisons`。papers 列出会改变本项判断的前作编号。comparisons 以这些编号为键，每一项有 relation 和 basis。relation 取 direct、partial、neighbor 或 unknown。basis 写出相同和不同的具体操作、条件与结果。verdict 取 covered、partial、no_direct_match 或 insufficient。 |
| `scope` | seed_check 写种子或独立挑战样本如何找回；citation_chase 写沿哪篇前作向前、向后追到哪里；stop_reason 给出停止的实质理由；critical_gaps 列出仍可能翻转判定的问题，无则填空数组。materials 中 protocol、recall、inventory、screening 分别指检索协议、召回检查、去重文献表和纳排记录，可指向同一份有对应分节的文件。把会左右结论的额外记录也列入 materials，例如书目核验输出。 |
| `review` | 在证据冻结后填 kind、reviewer、evidence_digest、trace_file。把实际审完的主张编号写入 reviewed_claims，complete 只在收到完整回复时填 true。kind 取 different_family（需另填 author_family 和 reviewer_family 两个实际家族名）、independent_human、same_family_fresh、self 或 unavailable。记录审查者的实际身份或可追溯代号，保留实际输入、原始回复与处理意见。 |

一条逐主张对照可以这样写。此例只演示该行格式，正式档案中的论文、查询和审查记录要逐项补入。

```json
{
  "id": "C1",
  "text": "首次在水下到空气的上行链路中数值比较空间和统计海面给出的接收功率空间分布。",
  "falsifier": "已发表论文在同一传输方向下用两类海面模型模拟并对照接收平面的功率分布。",
  "papers": ["P1"],
  "comparisons": {
    "P1": {"relation": "direct", "basis": "Gao 等的图 6 同时给出两类海面的接收平面功率图，图 7 对照截面分布。"}
  },
  "verdict": "covered",
  "reason": "P1 已执行这项比较，应撤回这句首次声明。"
}
```

## 冻结证据、送审并交付

1. 执行 `python "<skill>/scripts/check_dossier.py" fingerprint "<case>/dossier.json"`。再执行同一路径的 `brief` 命令生成移除了作者判词和初评矩阵的审查清单。把清单、对应的中性原文摘录、实查记录和[审查提示词](aris-review.md)一起交给审查者。核对附件中是否提前写入作者建议。只把审查者实际收到的版本写进 review.evidence_digest，保留原始意见文件。记录实际可用的审查方式。外部审查者只接收获准共享的材料。
2. 按意见核实反例。若修改了主张、查询、前作卡、原文解读、纳排表或结论，重新计算指纹，列明变化，请审查者核准新版本。保留双方对一项证据的不同解读。直接复制新指纹不能替代重审。
3. 执行 `python "<skill>/scripts/check_dossier.py" check "<case>/dossier.json"`。退出码 0 表示记录满足结构与证据门槛，1 表示现有记录只支持受限结论，2 表示档案无效或附件不可读。按输出补材料、缩小主张或说明哪项结论仍然成立。向用户提供报告与证据路径。

遇到配套检索脚本的 JSON 原始返回，程序还会对照真实渠道、查询词、日期过滤、命中总数和导出的候选数量。程序会查编号交叉引用、各主张已执行的不同查询和来源数、近期和不限年检索、直接反例、原文阅读层级、关键缺口及审查版本。独立专家或可确认的跨家族审查是最高验收等级的条件。同家族新上下文的有效反证照常采用，并如实标注。程序无法判断两个术语在物理上是否等价、依据文字是否读对、来源是否伪装成两个索引、审查者是否具有所填身份。执行者和审查者须回到原始材料核实。
