# 库分类与三库契约（L1/L2 SSOT）

**范围**：`D:\0Grok\0doc\_library` 下的 `references`（全文）、`lit-bank`（书目）、`journals`（期刊池）、

`ethics`（批件/提取），以及子工程 `ref\citation` / `ref\refer` 的分工。2026-10-31（t1458u）站立。

权威顺序：用户当轮 > 本文件 > `project-ref-layout.md` > `workspace-layout.md`。

## 1 共用临床 L1/L2（references / ethics / journals 三处共用）

| L1 | L2 |
|---|---|
| `obgyn` | ovary, endometrium, cervix, gestation, **gyn-oncology**（跨器官妇科肿瘤/AI，2026-10-31） |
| `hepatology` | MHE-HE, portal-hypertension, schistosomiasis, NAFLD-fibrosis, liver-tumor |
| `neuropsych` | cognitive, SSD, WML, gut-brain, **pain**（神经痛）, **cerebral-ischemia**, **neurotoxicity**（2026-10-31） |
| `oncology` | breast, lung, GI, pancreas, renal, head-neck, skin, soft-tissue |
| `nephrology` | CKD-ESRD |
| `cardio-vascular` | coronary, vascular, **cardiac**（结构/心耳等非冠脉非血管病变，2026-10-31） |
| `gastro` | UGIB, GI-non-tumor |
| `guidelines` | hepatology, neuropsych, obgyn, other |
| `other` | methods, **dermatology**, **occupational**, **chest**（2026-10-31） |

归类规则：

1. **不设 radiology 一级**；按研究问题所属临床专科归类，不按影像方法。
2. 妇科肿瘤进 `obgyn`，不进 `oncology`。
3. 纯方法学（无病种）进 `other\methods`；指南按「来源指南所属 L1」进 `guidelines\<L1|other>`。
4. 一文/一件只存一个物理文件；跨主题按主专科归一类，次主题写进索引的 `notes`。
5. L2 无法判定时：目录落 `<L1>\_unmapped\`，索引 `needs_owner=l2_unmapped`；**不硬凑**。
6. 新增 L1/L2 须主人点名；不得在子工程自造同名变体。

## 2 三库分工

| 库 | 放 | 不放 |
|---|---|---|
| `_library\references\<L1>\<L2>\` | 文献全文实体（PDF/HTML），一文一文件，文件名用 DOI（`/` -> `_`）；`index.csv` 记 `doi,pmid,l1,l2,rel_path,sha256,source_project,fetched_at,notes` | 书目卡片、批件、稿件、第二份副本 |
| `_library\lit-bank\` | 书目 SSOT：`index.csv`（NLM 引用 + 结论 + 主题），**无 PDF** | 全文实体 |
| `_library\journals\` | 期刊池 `index.csv`（单表；2026-10-31 起不再留 xlsx）/ `l1-l2-map.csv` / 选刊侧私有 `whitelist-submitted.csv` + `submission-prior.jsonl`（旧表按年重建时移 `{DEL}`，不留 `archive\`） | 全文、`submission-urls.csv`、名单本体 |
| `_library\ethics\` | `approvals\<L1>\<L2>\` 批件 PDF + `approvals-index.xlsx` + `extract\`（briefs/phrases/doc-role/held-out 提取层） + **`sections\`**（2026-11-01：按伦理表格 section 的分节取用层，`protocol\`/`icf\` 细、`other\` 粗；生成物） | 已填申请材料原件（在 `D:\00db\_lab\ethics\raw-20261023\`，只读）、第二份全文副本 |
| `_library\glossary\`（2026-11-01，原 `0doc\_bank`） | **自有写作语料 + 三层条目** `words\` / `sentences\` / `paragraphs\` + `sections\*.md` **指针页**（无正文）+ `index.csv`（**13 列**，含 `sections` 列，**由 md 生成**）；证据层 `banks\`（jsonl + `glossary.db`，gitignore；`GATES.md` 已清） | **他人文献**（不进 `references`/`lit-bank`）、L1/L2 归类、规则/词表本体（判据在 `{SKILLS}\05_manuscript\base\vocab\`，此处只放实例 + `rule_ptr`） |

子工程侧：`ref\refer\` 只放**文献指针**（`DOI_*.md`，`fulltext:` 指向 `_library\references`）+ NLM 引用与摘要列表 + 写作参考；
`ref\citation\` 放**审计台账 + 期刊/候选刊**（见 `project-ref-layout.md`）。

## 3 ethics 批件契约

- 路径：`_library\ethics\approvals\<L1>\<L2>\<approval_id>_<year>_<slug>.pdf`；照片件 slug 加 `-photo`。
- `approval_id`：批号规范化（空格 -> `-`，去「编号未知」段）；确缺时 `NOID` / `<机构>-<year>-NOID`。
- `year`：批准日期年 > 批号内年份 > `NOYEAR`。
- 索引 `approvals-index.xlsx` 19 列：`seq,l1,l2,approval_id,id_year,approval_date,valid_until,project_title,institution,file_name,rel_path,pages,size_kb,sha256,archive_name,original_name_zh,id_source,needs_owner,note`。
- `approval_date` 与 `valid_until`（**批件有效期**）必录；扫描件无文本层时用本机 OCR 出候选 + **人工确认**，只补空、不覆盖人工值。
- 子工程只挂指针（批号 + 路径），不存批件副本。
- 0doc 目录名一律 ASCII 英文；中文原名只留索引列。

## 4 journals 契约

- `_library\journals\index.csv` 列见该库 `README.md`（单表，2026-10-31 起不再派生 xlsx）；关键：`jcr_year`（版本年）、`metric_year`（指标年）、`layer`、`l1/l2`、`whitelist`（含 `bmc`）、`queried_at`。
- **每年跨年后 7 月**按新 JCR 年版整表重建一次；旧表连同压缩前分层 CSV 移 `{DEL}`（2026-10-31 起不再保留 `archive\<year>\`），不逐行手改。
- 选刊侧私有数据（投过白名单 `whitelist-submitted.csv`、投稿先验 `submission-prior.jsonl`）打平在 `journals\` 内，**不建年夹**（2026-10-31 裁定；原 `jcr\<year>\` 层级取消，别名校验见 `lab-paths.yaml`）。
- 名单本体（blacklist/graylist/whitelist-bmc/submission-urls）仍在 MY-SKILLS `find-journal/data\<year>\`。
- 子工程候选刊**只用 csv/xlsx**：`ref\citation\journals.csv` + 合并笔记 `ref\citation\_notes.md`；被替代原稿进 `ref\tmp\`。

## 5 索引与巡检（harvest-watch）

`_library\INDEX.md` 的 Harvest watch 段是**索引清单**：只列路径、形态、计数、复查节奏
（`lit-bank/index.csv`、`references/index.csv`、`journals/index.csv`、`journals/l1-l2-map.csv`、`journals/whitelist-submitted.csv`、`journals/submission-prior.jsonl`、`ethics/approvals-index.xlsx`、`glossary/index.csv` + `glossary/banks/` 的 jsonl 与 `glossary.db`）。

**禁止**把 PDF 全文、批件扫描、期刊全量行抽进技能正文；技能只引用路径与列名。

## 6 迁移与临时件

- 库内改名/移动：保留 `MOVED-FROM.md` 记录；被替代原件进 `D:\0del\_by-project\<task>\superseded\`。
- 未进 `accepted\` 前，子工程的临时/中间/旧版/试跑一律 `ref\tmp\`；**禁止自动进 0del、禁止自动删**。
