---
name: My rule
description: Aitor（AA）科研与编程全局规则。
license: MIT
---

# 1 适用范围与优先级

- 对 Grok Bot/Aitor、子代理、Cursor 生效（本机编码入口仅 Cursor IDE；其中 Cline 为 IDE 插件，由城城自用，bot 不单独调用 Cline）。
- **数据底表移动（D-1 · 2026-10-29 · t1309s6268）：** 原始/预清洗数据底表默认落 `ref/` 根（或 `ref/data/`）。**移动底表前必须先问城城**（D-1）；勿静默挪走。布局说明见 `project-ref-layout.md`。

- **裁决顺序**：用户当轮表述 > 专题文件 > 本文件 > 子工程内约定。
- **别名**：`{RULES}`=`D:\0Grok\0doc\GitHub\MY-RULES`；`{SKILLS}`=`D:\0Grok\0doc\GitHub\MY-SKILLS`；`{RAW}`=`D:\00db`（已组织的原始库，只读除非点名；原 `00ds` 已迁此）；`{DEL}`=`D:\0del`。
- **本机布局（一行）**：`D:\00db`（organized raw） / `D:\0del`（AI 可操作临时区） / `D:\0Grok\0doc`（语料 + 可复用代码） / `D:\0Grok`（分阶段子工程工作区）。细则 → `workspace-layout.md`。
- **库分类（t1458u）**：L1/L2 与三库分工的权威正文 → `library-taxonomy.md`。`_library` 下 `references`（全文实体）/ `lit-bank`（书目，无 PDF）/ `journals`（期刊池，含选刊侧私有 `whitelist-submitted.csv` / `submission-prior.jsonl`）/ `ethics\approvals`（批件）；不设 radiology 一级，按临床专科归类。
- **术语**：作者字段 `A`=批注作者；`00`–`07`=技能层；派单→`{SKILLS}\00_orchestrator\references\ownership-contract.md`。工作区只有一层；不再有 A/B 双工作区或挂载缓存树。
- **技能 ID**：选型只按 fine id；细则 → `skills.md` §2；`{SKILLS}\00_orchestrator\references\id-rules.md`。
- **一任务一执行方**；外挂仅 **Cursor**（须用户批准或说「交给cursor」）。bot **不得**再派「交给cline」/独立 Cline CLI。盯梢→`{SKILLS}\00_orchestrator\references\handoff-monitor.md`。
- **选模型（Cursor；2026-10-30 · t1452u）**：经 bot 调用 **Cursor** 时，默认 **composer**。
- **Rules 默认挂载；Skills 派工附加（t1397u）**：凡派子 bot/专员（Lee/Victor/Aitee/Bai/Loopnow 等）或云端 Cursor / CloudAgent，**默认携带 {RULES}**（本文件 My rule.md）。**派具体工时再附加 {SKILLS}**（相关 fine id / 路径，或整库 SSOT）。冲突时 Rules > Skills。CloudAgent prompt 须写明 Rules 路径；Skills 按本次任务写入，勿假设云端已挂载。
- **云端 / 本地（术语，2026-10-25）：** **云端** = Grok Bot 的 box 计算机（`/workspace` 等）；**本地** = 城城本机（如 `D:\`、Downloads）。二者勿对调。
- **mem 落盘：** bot 记忆导出/更新落在本地 `D:\0Grok\0doc\mem`（城城指定；非默认进 `{DEL}`）。mem **仅保留隐私**与可变数据 SSOT（如 JCR xlsx）；站立运营政策进 `{RULES}`，专业技能进 `{SKILLS}`。
- **单项目约定**写在该**子工程文件夹**内（如子工程 `0doc\` 或 `ref\`），**不**写入全局 `{RULES}` / `{SKILLS}`。须用户点名「放 0doc」才写 `0doc\`。
- **交付落点**：子工程**没有** `0result\` 文件夹。**最终**交付物 → 该子工程**根目录**（`D:\0Grok\<project>` 下）；**中间**产物 → 按 `project-ref-layout.md` 的 `ref/` 子文件夹地图（`review/` / `citation/` / `refer/`（文献+写作参考 pptx/doc/docx） / `code-gates/` / `tmp/` + 根上 tables/figures/pipeline；**hashes/MANIFEST/pipeline_run.log 在 `ref/pipeline/`**；`submission-*`、底表；分析 `false_classification*` 留子工程根（详图与 Cleanup 两档见 `project-ref-layout.md`；已退役 `analysis/`/`materials/`/`results/`/`exec/`/`code/`/`gates/`/`writing-refs/`/`raw-pre/`））；**子工程内临时/中间默认 `ref/tmp/`**（**非**默认 `{DEL}`；旧版 `Manuscript_*_V*` 亦然，现行 `Vn` 在根；详 → `project-ref-layout.md`）；无子工程或不属课题树的临时进 `{DEL}`；Downloads **仅当**当轮点名「下载」或「Downloads」。**文献全文（PDF/HTML）SSOT = `D:\0Grok\0doc\_library\references\<L1>\<L2>\`**（t1455u）：子工程 `ref/refer/` 只留 `DOI_*.md` 指针 + NLM/摘要 + 写作参考，不再存第二份全文；`_library\lit-bank` 只存书目。

# 2 开工前确认

- 只读不用授权；改/移须先授权。
- **禁删**；移出只进 `{DEL}` 并保留相对路径。**旧稿清理**＝移入 `{DEL}` / `D:\0del`（可按 `_by-project` / `_by-function`），禁止静默永久删除。
- 确认：目标与验收；假设≤3；取舍；谁执行。
- 「直接做」可不逐项确认，但不跳过 MY-SKILLS PR/merge（`skills.md`）与须批网络（`network-security.md`）。「继续」≠网络同意。
- 网络红线→`network-security.md`。

## 2.1 盘问 / grill-me（SSOT；技能只指针）

本条为 grilling 权威正文。`{SKILLS}\00_orchestrator\references\plan-and-grilling.md` 只保留 Plan card / Q0–Q3 / 流程图，并**指向本条**；勿在技能里复写全文。

- **何时**：多节点任务、新能力、高风险、或用户说 `grill-me` / 「盘问」。单节点且无关键未知 → 不问（对齐技能 Q0）。
- **一轮批处理**：合并成**一轮**澄清，不要连环单问。
- **编号 + 默认**：问题编号列出；每题给推荐默认（用户可回「默认」/空确认）。
- **多选（组合）；不限 5 题**：向城城提问可用多选/组合选项（若干答案可并用）；问题数量**不限于 5 个**——需要时可超过 5 题（可用多步卡片 / 连续 widget）。此为城城偏好；平台单卡选项上限另论，勿称平台已抬高硬上限。
- **先查后问**：文件或网页能答的，先自己查；查不到再问（对齐技能 Q3）。
- **然后出 Plan**：澄清通过后再给计划卡（节点顺序、风险门），等明确点头再派单。
- 流程图批准、N1–N4 决策点仍由 `plan-and-grilling.md` 管；本条不管挂载包（mounts 已退役）。

# 3 编程准则

简单优先；外科手术式；软编码；模块化；**不写回退**；新脚本 Python 3.13.9；PowerShell 不用 `&&`。

- **配置置顶**：脚本顶部先放配置/常量块（路径、开关、参数），再写逻辑。
- **仅注释配置和脚本运行说明**：注释只写 (a) 配置字段含义；(b) 如何运行该脚本。不对业务逻辑写长文注释；**不写业务「为什么」**（2026-10-24 裁决维持现行）。
- **不写回退**：禁止 fallback / 静默降级（勿用 try-except 吞失败后走默认路径）；失败要响，暴露错误。
- **可以写多模块并配置可选**：允许多模块；模块可用配置开关可选启用。
- **dry-run**：批量 IO / 写盘前先试跑，打印将执行的操作供确认；默认 dry-run，显式 `--execute` / `--apply` 才落盘。
- **测试→运行→核查→验收**：所有脚本先测试再运行，最后核查，再验收。顺序固定：(1) 先测（unit/smoke/dry-run 视情）；(2) 再跑正式任务；(3) 核查结果；(4) 验收通过后再宣告完成。
- **断点续传**：已处理结果跳过；以中间文件或完成标记续跑，勿整段重算。

细节（模板、阶梯、QC）→`{SKILLS}\02_data-processing\advanced\coding.md`。

# 4 执行与验证

优先 diff；lint/测试后交终稿。**不编造**事实/数字/文献/DOI/路径。稿件禁令→`{SKILLS}\05_manuscript\qc\manuscript-local-qc.md`。技能树 QC：**禁止 skip/archived 停放**；skipped/archived 与**退役仅指针壳**均为清理对象→`skills.md` §6（t1520u）。**QC 不得 ignore / 跳过**→`skills.md` §6（t1559u）。脚本站立流程见 §3「测试→运行→核查→验收」。

# 5 交付与清理

**禁删**；子工程内临时/中间默认 `ref/tmp/`（非默认 `{DEL}`）；无子工程或跨课题一次性临时进 `{DEL}\<任务>\`。旧稿/旧产物清理＝移入 `{DEL}`，不静默永久删。子工程**不建** `0result\`。

| 产物 | 格式 | 落点 |
|---|---|---|
| 最终交付（稿件/终表/最终报告等） | 依类型 | **子工程根目录**；无子工程且点名「下载/Downloads」→Downloads；否则→`{DEL}` |
| 中间产物（QC/ledger/门控/草稿等） | 依类型 | 有子工程→按 `project-ref-layout.md` 的 `ref/` 地图（`review/`/`citation/`/`refer/`（含写作参考）/`code-gates/`/`tmp/` + tables/figures/pipeline；locks 在 `ref/pipeline/`；`submission-*`；`false_classification*` 在子工程根（详图见 `project-ref-layout.md`））；否则→`{DEL}` |
| 报告/QC（中间） | HTML | 有子工程→该子工程 `ref\`（或阶段夹如 `in-review\`）；无子工程且点名 Downloads→Downloads；否则→`{DEL}` |
| 稿件/TC（最终） | DOCX | 子工程**根**；否则仅当点名 Downloads，否则 `{DEL}` |
| SCI 稿件文件名 | DOCX（md/pdf 同 stem） | **`Manuscript_` / `Comments_` / `Response_` / `Supplementary_`** + `_<子项目名>_V<n>`；版本与对应修回轮次一致。**现行 `Vn` → 子工程根**；**旧版 → `ref/tmp/`**（t1450u）。权威 → `project-ref-layout.md`「SCI 稿件文件名」；技能指针 → `{SKILLS}\05_manuscript\advanced\Aitor-format.md` / `handoff.md`、`06_review\advanced\handoff.md`、`07_response\advanced\handoff.md`（t1428u/t1429u/t1430u） |
| 数据表（最终） | XLSX | 子工程**根**（不建 `0result\`）；其余同稿件 |
| 文献全文（PDF/HTML） | PDF/HTML | **`D:\0Grok\0doc\_library\references\<L1>\<L2>\`**（一文一物理文件，名用 DOI；t1455u）。子工程 `ref/refer\` 只写 `DOI_*.md` 指针；书目仍进 `_library\lit-bank`（不存 PDF） |
| 期刊池 / 批件 | CSV/XLSX/PDF | `_library\journals\index.csv`（单表，2026-10-31 起不再留 xlsx）；`_library\ethics\approvals\<L1>\<L2>\` + `approvals-index.xlsx`（t1458u）。子工程候选刊只写 `ref\citation\journals.csv` + `_notes.md`；批件只挂指针。口径 → `library-taxonomy.md` |

同一分析若 `Results*.html`（或已执行产物 HTML）与 `.xlsx` 数字冲突：以 HTML 为准，并在汇报里写明冲突与所采用源。

「放 0doc」才写 `0doc\`。长表→`{SKILLS}\00_orchestrator\references\standing-delivery.md`。

# 5.1 Word / 审稿回复 / 本机目录（2026-10-19）

- **Word/PDF 格式**：未经当轮点名，禁止改 `.docx`/`.pdf` 版式；改文字用修订模式。词/句级修订，禁止大段覆盖。细则→`{SKILLS}\06_review\advanced\word-edit.md`。
- **城城已改先问（全局停）**：若 Word/手稿正文与城城（用户）已编辑文本不同（修订痕迹 / 已知本人改动），**必须先问再改**，禁止擅自覆盖或改回。技能须指针本条，勿只埋在 revise。→`word-edit.md`；`writing-rules-hard.md`；`07_response` revise。（2026-10-24）
- **统一版式**：手稿、审稿意见、审稿回复同一套——正文 Times New Roman 12、1.5 倍行距、段前后 0、两端对齐、LTR、特殊格式无；**表格单元格 12 pt**；**图内文字 Arial**（与正文双轨）；**流程图首选 PDF**。→`{SKILLS}\05_manuscript\advanced\Aitor-format.md`；`word-edit.md`；`draw-flowchart`。（2026-10-24）

- **图表编号（C-1 · 指针，2026-10-29 · t1309s6268）：** Table 1 = 基线；**不**单独放 logistic 系数表或 score-correlation 表（Aitor-format §209）；ROC 操作特性作表；图按适用放 workflow / US / heatmap / nomogram+校准 / ROC / DCA。细则勿在本文件复写，指针 → `{SKILLS}\05_manuscript\advanced\Aitor-format.md` §200 / §209 / §213。
- **批注英文建议句**：单独成句，以 `Suggested …` 起首。字面模板技能落点→`{SKILLS}\06_review\advanced\word-edit.md`。`manuscript-and-review.md` 已于 2026-10-18 按 README 迁入 `05_manuscript` / `06_review` / `07_response`。
- **审稿回复**：保留完整原始 comments；不简化；不擅自加小标题；不自创信函格式。→`{SKILLS}\07_response\advanced\response.md`。
- **新建文件/文件夹（权威；合并 t1098u/t1107u/t1240 · 2026-10-30 · t1442u/t1450u）**：默认只能在 `{DEL}` / `D:\0del`（`_by-project` / `_by-function`）新建文件与文件夹；路径 SSOT 为 `D:\0del`（非 `D:\0Grok\0del`）。在其他位置新建前必须本轮明确问城城并获准。**常设例外**：(1) bot 记忆导出/更新可在 `D:\0Grok\0doc\mem\` 内新建（§1「mem 落盘」）；(2) 子工程内 `ref/tmp/` 按需写入临时/中间（含旧版稿；详 → `project-ref-layout.md`）。**可改**已有文件（含 `{RULES}` / `{SKILLS}` / `0doc\skill-harvest\*` / `0doc\mem\*` / 子工程已有稿含 Track Changes）。默认禁止在 `D:\0Grok\0doc` 下 mkdir（除 mem 例外与本轮明确同意）。新草稿、ACCEPT、digest、by-fine-id lane、笔记、中间件、临时/scratch、ACCEPT 备注 → 只进 `{DEL}`。审稿交付：优先修订现有评审意见 `.docx`（Track Changes），禁止另存新稿名、禁止在子工程下新建夹。用户本轮点名的终稿落点仍按 §5（优先改已有终稿）。短针→`workspace-layout.md`（不复写）；mem→`D:\0Grok\0doc\mem\README.md`；全文→`{RULES}\standing\STANDING-no-new-files-outside-0del.md` 与 `{RULES}\standing\STANDING-0doc-no-new-folder.md`（2026-10-31 从 0del 移入本仓；**0del 不再承载任何全文/指针**）。
- **一次性脚本/说明/小补丁**（非课题交付）：只落 `{DEL}`，禁止丢进用户主目录、`.grok\tmp`、或课题根。
- **0doc 目录名英文化（t1458u）**：`0doc` 下新建目录一律 ASCII 英文（如 `approvals` / `journals` / `jcr` 这类英文短名）；发现中文目录当轮 rename，并在 `_library\MOVED-FROM.md` 记一行。文件名可保留中文原名，但须在对应索引列留映射（如 `original_name_zh`）。库分类口径 → `library-taxonomy.md`。



## 5.2 每轮 QC 必清 0doc（2026-10-27）

- **每轮质控必须跑一次无用件清理**（`D:\0Grok\0doc`）：`python -B test\cleanup_scan.py --tsv <清单>` → 人工确认 → `python -B test\cleanup_move.py --plan <清单> --apply`，移入 `{DEL}\_by-function\0doc-qc-clean\<YYYYMMDD>\`，保相对路径并落 `MOVED.tsv`。
- **判据只有三条**：有没有入口 / 有没有真实落点 / 能不能再生。「看起来旧」不是理由；只剩历史价值 → 留档并标注，不计清理成绩。
- **默认分级**：字节码缓存、垃圾文件名、空目录、历史结构快照、被同名无日期版取代的副本 → 可直接移；重复件、无入口脚本、无读者台账、孤立 `.md`、占位壳 → 出清单等点头；断链与「文中路径全失效」→ 只修指针或就地标注，**不搬**（历史档合法引用过去落点）。
- **永不自动清**：`_library\glossary\banks`（含 `glossary.db`）、`mem\`、`_library\ethics\`，以及历史档 `MIGRATION.md`、`ACCEPT-*`、`_library\former-*`、`skill-harvest\PLAN-*`。
- 移出即记台账；收工报告须给「一条命令还原」的路径映射。分类说明→`0doc\test\README.md`。
- **skip / archive / 退役仅指针 不是停放位**：口径见 §4 与 `skills.md` §6（t1463u；t1520u；**t1559u 不得 ignore/跳过假绿**）；0doc 侧由 `test\structure_check.py` S4 与 `test\cleanup_scan.py` C2 强制，**无存档例外**（年报/年表同样移 `{DEL}`，见 `0doc\STRUCTURE.md` §7）。


## 5.3 0del 三档（2026-10-31）

`{DEL}` 内移出件按可弃度分三档，**不得混放**；每档一个落点，搬移必留 `MOVED.tsv` 并保相对路径。

| 档 | 落点 | 判据 | 处置 |
|---|---|---|---|
| park | `_by-function\<批次>\` / `_by-project\<课题>\` | 有活指针、台账价值，或一次任务的全套件（旧稿、ACCEPT 回执、`MOVED.tsv`） | 留到城城点名；**不得**整夹清 |
| harvest-park | `_by-function\harvest-0doc-<YYYYMMDD>\<原相对路径>` | `0doc` 新建件的收尾归档（草稿已「进skills」收编，或已过时） | 留档；下次 QC 复核后再定留或降 harvested |
| harvested | `harvested\`（平铺，不建日期子夹；原 `junk\`，2026-10-31 改名） | 一次性批次、字节码/缓存、拼写错件、本机配置备份、Downloads 残留、**无任何文本引用**的产物 | **只由城城手动清**；bot 不清、不代清 |

- **课题件优先** `_by-project\<slug>\`（park）；**0doc 收尾件**（草稿已收编进 skills、或已过时）才进 harvest-park。两档不得互替堆放。
- 落 harvested 前必须：① 全库 grep 确认无活文本引用（`0doc` + `D:\0Grok` 课题树）；② 同名异字节不覆盖；③ 写 `harvested\MOVED.tsv`。
- **harvested 是唯一的终弃档，且只由城城手动清空**（bot 不清、不代清、不自作主张）；park / harvest-park 不得整夹清。
- `0doc` 侧的判定与落盘仍由 `test\cleanup_scan.py`（判据）与 `test\cleanup_move.py --dest <落点>`（落点）负责；本条只定**落点与可弃度**，不另造脚本。
- **禁止活指针引用 `{DEL}`（2026-10-31）**：`{RULES}` / `{SKILLS}` / `0doc` 文档与脚本**不得**把 `D:\0del\...` 当作当前落点或路径解析目标（0del 会周期性清空）。需要长期存在的全文/台账/脚本一律放耐久位置（`{RULES}` / `{SKILLS}` / `0doc` / `project root`）；历史记录里的 0del 路径由 `test\path_audit.py` 归 `HISTORIC`，但**不得新增**活指针；要清空 0del 前先把活指针重指。
- **整理 0del 前先 grep 活路径**：`_code` 多个脚本把输出写死到 `D:\0del\<子夹>`（一律在 `harvested\` 下：`smoke`、`modules_bak`、`cln_fill_supplement`、`yt_RDL`、`batch_rerun_status.json`、`batch_rerun.log`；t1490u），这些不是移出件，搬走即破坏脚本；新增写死路径须同轮补入本节清单。

# 6 工程决策

- R1 需求优先 · R2 证据排错 · R3 有序简化 · R4 风险比例 · R5 保护不变量 · R6 闭环验证。
- **重大变更门**：改结构/改 ID/删目录 → 假设清单、影响、用户批准。

# 7 科研

文献只引真实来源（找不到写「未找到」）。统计不为跑通改 outcome/纳入/cutoff/协变量/缺失/模型。细则→`{SKILLS}\02_data-processing\qc\`（`method-validation-gate.md` / `report-checks.md` / `html-results.md`）。

# 8 语言与汇报

说明/QC 中文；期刊英文稿英文。汇报时区 Asia/Shanghai (UTC+08:00)。「；」=两任务；「|」=同任务并列。STE→`{SKILLS}\05_manuscript\base\vocab\L3\lab-ste.md`。

# 9 按需文件

| 触发 | 读 |
|---|---|
| 网段/敏感外发 | `network-security.md` |
| 技能/PR 同步 | `skills.md` |
| 本机布局 / 子工程 | `workspace-layout.md`（见 §1 一行布局） |
| 三仓分工 / 某内容该放哪 | `README.md`（RULES=运营规则，SKILLS=专业技能，MY-CODES=脚本） |
| 派单/盯梢 | `{SKILLS}\00_orchestrator\references\ownership-contract.md`；`{SKILLS}\00_orchestrator\references\handoff-monitor.md` |
| 0doc 文档库查找 | Bai → `{SKILLS}\03_research\advanced\0doc-db.md`；派单 SSOT → ownership-contract §0doc |
| 技能演进 | `{SKILLS}\00_orchestrator\references\skill-evolution.md`（门在 `skills.md`） |
| 稿件禁令 | `{SKILLS}\05_manuscript\qc\manuscript-local-qc.md`；`{SKILLS}\05_manuscript\base\vocab\L1\ban-phrases.md` |
| 项目 `ref/` 布局 / ledger 再跑 | `project-ref-layout.md`；`{SKILLS}\00_orchestrator\references\project-ref-layout.md` |
| 库分类 / L1-L2 / 三库(references·lit-bank·journals·ethics) / 批件与期刊池 | `library-taxonomy.md` |
| 盘问 / Plan card | 本文件 §2.1；技能 `plan-and-grilling.md`（指针） |

Cursor User Rules 只一行指向本文件。「记住」：总则→本文件；专题→专题；项目→子工程约定；技能→提案；敏感→mem（禁写入 MY-RULES/MY-SKILLS）。
