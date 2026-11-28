---
name: project-ref-layout
description: 项目 ref\ 地图、稿名与文件命名、幂等；落点总则见 My rule.md §3；稿件硬闸与手改识别见 manuscript-docx.md。
---

# 项目 `ref\` 布局（ledger + 产物）

**负责人：** `00_orchestrator`。
**读者：** 任何把 QC、引用、Word、门控或执行产物写入项目 `ref\` 的技能。
**EXECUTION / 收工时间戳：** Asia/Shanghai (UTC+08:00)。

本文是**文件夹地图与跳过/幂等契约**。不编造临床数字。文件名与 ledger 行除课题科学所需（路径、DOI、citekey）外，不含 PII。

**SSOT：** 本文件为**权威中文版**；技能侧英文镜像 `{SKILLS}\00_orchestrator\references\project-ref-layout.md` 只作运行期读本，冲突以本文件为准。旧夹名映射见 `aliases.yaml`。

## 根目录不变量（勿挪位）

以下必须留在 **`ref\` 根**（技能与约定硬性要求）：

| 路径 | 作用 |
|---|---|
| `ref\settings.ini` | 仅 RAD / 流水线配置。勿随意覆盖；勿存密钥。 |
| `ref\manuscript-revision.md` | 只追加的主变更 ledger（主人要求 + 代码/结果/Word）。05/06 Word 轮次后在此追加（`{SKILLS}\06_review\advanced\word-edit.md`）。**已登记段落勿再抛光**，除非上游数字变了、主人点名、或未解决批注已授权。 |
| `ref\README.md` | 采用本布局时的短地图（见下节）。 |
| `ref\qc.html` | QC 报告（若已在用）留在**根**，不进子夹。 |

根上可选（若已在用）：`ref\project-state.yaml`（来自 `{SKILLS}\00_orchestrator\templates\project-state.yaml`）。

另：统计**表图**（原 `analysis/` / 更早 `results/`）落 `ref\tables/` `ref\figures/`；流水线夹 `ref\pipeline/`。**锁定件** `hashes.tsv` `MANIFEST.md` `pipeline_run.log` 必须在 **`ref\pipeline/`**（勿放 ref 根）。**写作参考**（pptx/doc/docx 等用作参照的稿件/幻灯/申请书）可进 **`ref\refer/`**（与文献/NLM 列表同夹；勿再造 `writing-refs/` 或 `materials/`）。未被接受投稿包（`submission-*`）、数据底表可在 `ref\` 根或 `data/` / `submission-<标识>/`；优先扁平，仅撞名时加前缀或子夹。

## 子文件夹地图

尽量少的 `ref\` 子夹。标准夹：`review/` `citation/` `refer/` `code-gates/` `tmp/`（按需创建，**不预建空夹**）；另登记 `figures-orig/`（图件原始可编辑件，QC；与终图 `figures/` 分工见下表）。**勿再新建** `analysis/` 或 `materials/` 壳。

| 子文件夹 | 放这里 | 不放这里 |
|---|---|---|
| `ref\review/` | 每轮 `changelog.md` / `CHANGELOG_*.md`；审稿交接 YAML；Lee 轮次笔记 | 主 Word 变更 ledger（仍用 `manuscript-revision.md`） |
| `ref\citation/` | **审计台账 + 期刊/候选刊**：`CITATION_AUDIT.json`（或 `.jsonl`）；引用 README / 跳过说明；**期刊/候选刊只用 `journals.csv`（或 `.xlsx`）** + 合并笔记 `_notes.md`；期刊/引用日志（`ref_journal_log.txt`、`CITATION*`） | NLM+摘要列表与文献正文（见 `refer/`）；写作参考草稿；**期刊信息的散装 md/json/html**（合并进 `_notes.md`，被替代原稿进 `ref\tmp/`） |
| `ref\refer/` | **文献指针 + NLM 引用与摘要列表**：每篇一个 `DOI_*.md`（`fulltext:` 指向 `_library\references`）；文献清单（原「参考文献」/ `materials/citation` / `materials/refer`）；**亦可**放写作参考 pptx/doc/docx（课题申请书/汇报幻灯/三线表等） | 文献全文实体；审计台账（`CITATION_AUDIT` 等仍在 `citation/`）；**期刊/候选刊**；勿把 locks（hashes/MANIFEST/log）放这里 |
| `ref\code-gates/` | 脚本/路径说明、补丁指针（无密钥）；`GATE*_report.md`、数字锁定、输入/输出哈希报告 | 现役 `settings.ini`；原始凭据。**`code/` 与 `gates/` 禁止分夹**，统一用本夹 |
| `ref\figures-orig/` | 投稿图**原始可编辑件**（`.ai` `.psd` `.pptx` 原始 `.tif`、未标题导出等）；**QC 登记为允许夹**，按课题保留原形（不改名、不合并、不压包） | 终图（`ref\figures/`）；被替代的旧图件（→ `ref\tmp/`） |
| `ref\tmp/` | 子工程内**临时/中间**默认落点（**非**先丢 `{DEL}`）：中间 Word/PDF/草稿（Claude diff、被替代的 TC、`-copy`、合并草稿）；**旧版 SCI 稿与非最新 tracked**（如 `Manuscript_<slug>_V1.docx` / 旧 `_tracked` 稿）、根上的 PDF 导出；被合并的期刊/引文散装原稿（如 `journal-archive-<YYYYMMDD>/`）；保留到主人说清理/收工。**未进 `accepted\` 前的临时/中间/旧版/试跑一律留此**：禁止自动进 `{DEL}`、禁止自动删；进 `accepted` 须主人另批 | 根上现行的 `_clean` 与最新带版本号稿（子工程根）；已关闭轮次 changelog（`review/`）；citation / code-gates ledger；密钥 |

课题根或 `ref\` 下的旧分析壳与并列夹禁止再建（→ 总图退役禁建表）。

### 三区 / 临时结果区

- **站立：** 子工程内临时与中间文件默认进 `ref\tmp/`，**不**默认进 `{DEL}`。过后清理（先问）再移 `{DEL}`。
- **分析临时结果**（`ASL/`、`DKI/`、`DTI_IVIM/` 等）落**当次结果夹** `<project>/<endpoint>/`（或解析出的 OUT_DIR / `SUBPROJECT_BY_OUTCOME` 夹），**不在子工程根**，也**不进 `ref\`**。
- 面向稿件/门控的统计**表图**在 `ref\tables/` `ref\figures/`；**锁定件** `hashes.tsv` `MANIFEST.md` `pipeline_run.log` 在 **`ref\pipeline/`**；**勿**与 `ASL/` 等分析树合并。
- **分析错分/临时表**：`false_classification*` 与同类 ASL 分析临时表落**当次结果夹** `<project>/<endpoint>/`（或解析出的 OUT_DIR / `SUBPROJECT_BY_OUTCOME` 夹），**不在子工程根**，也**不进 `ref\`**。结果 HTML 同落该结果夹为 `Results*.html`（见 `workspace-layout.md`）；**不**把 `{slug}_results.html` 或旧结果 HTML 提升到子工程根——根上已有的旧副本属错位。
- **文献全文：** PDF/HTML 实体一律进 `{doc_root}\_library\references\<L1>\<L2>\`（命名、索引、指针契约见该库 `README.md`）；子工程 `ref\refer/` 只写 `DOI_*.md` 指针，`ref\citation/` 不放全文，`_library\lit-bank` 只存书目。
- **终稿 / 控制台终表**留在子工程根。查阅入口用备忘录 HTML 的 `file:///` 链接（`My rule.md` §3）；`{memo_dir}` 不放快捷方式。不另存一份。
- **已接受**的最终通稿（无刊名短码）留在子工程根；按刊格式化的再投稿不放根上，进 `ref\submission-*`（见 `manuscript-docx.md`「投稿包」「目标刊格式版」）。主人点名时，中间 xlsx 也可留在子工程根，勿擅自挪走。

### 投稿包（未被接受 vs 已接受）

定义、落点（`ref\submission-*`、通稿留子工程根）与清理 → `manuscript-docx.md`「投稿包」。

### SCI 稿件文件名（Manuscript / Comments / Response / Supplementary）

Stem、V/R/P 版本规则、根上两份现行稿与旧版进 `ref\tmp/` → `manuscript-docx.md`「SCI 稿件文件名」。

### 目标刊格式版（母本不动，按刊另存）

母本不动、按刊另存至 `ref\submission-<刊名短码>/` → `manuscript-docx.md`「目标刊格式版」。

### 非契约编辑后缀稿（登记保留 · QC）

中间件后缀的登记、落点与清理 → `manuscript-docx.md`「非契约编辑后缀稿」。


### 城城手改识别

手改识别与修订模式 → `manuscript-docx.md`「城城手改识别」（§M1–§M3）。

### 数据底表（D-1）

- 原始/预清洗数据底表可落在 `ref\` 根或 `ref\data/`（撞名或更清晰时保留 `data/`）。
- **今后移动底表前必须先问城城**（D-1）；本契约迁移轮次已获准将原 `materials/` 内容上抬时除外。勿静默挪走。
- 大体量影像 raw（DICOM/NIfTI 等）≠ 本条底表：落 `{RAW}\<family>\<prefix_suffix>\`，见 `zone-database.md`。

### accepted 收工硬留

硬留清单、`R*` / `P*` 整夹与图分流 → `zone-projects.md`「accepted 收工」。关系 / harvest 授权 → §Z1、§Z2、§Z3。

### Cleanup（过后可清；两档）

**禁止**静默删除。清理时**先问城城再移**；优先移入 `{DEL}\_by-project\<project>\`（跨课题则 `_by-function`），有用时保留相对名。

**默认可清 → `{DEL}`**（= `{DEL}`；先问再移）：

- `ref\tmp/`（整树或点名文件）
- 已废的旧写作参考 / 过期预清洗表（现位于 `ref\refer/` 或曾在 `ref\` 根者）
- **未被接受**的投稿包（`submission-*` 等；先问再移）
- 合并后残留的空壳：`analysis/`、`materials/`、以及更早的 `exec/` / `code/` / `gates/` / `writing-refs/` / `raw-pre/` / `results/`

**默认保留：**

- 当前终表终图（`ref\tables/` `ref\figures/`）与 **`ref\pipeline/`** 内锁定件（`hashes*` `MANIFEST*` `pipeline_run.log`）及仍在用的 `ref\refer/` 写作参考/文献、底表、`submission-*`
- 仍在用的 `ref\citation/`（审计台账）与 `ref\refer/`（文献 + 写作参考）
- `ref\code-gates/`
- 根上 `settings.ini` / `manuscript-revision.md` / `README.md` / `qc.html`（及仍在用的 `project-state.yaml`）
- `ref\review/` 中未关闭或主人未点名丢弃的轮次材料；`-org` 编辑前原件（见下节）
- ASL 类分析树（在当次结果夹 `<project>/<endpoint>/`，不在 `ref\`）：默认保留；仅当城城点名整树时再清

首次需要时创建子夹（copy-on-need）；清理后可留空 `ref\tmp/` 或下次写入时再建；勿在此编造临床内容。

### `ref\README.md`（采用本布局时）

项目一旦采用本布局，在 `ref\` 根备一份简短 **`ref\README.md`**，至少各用一行写明：

- `refer/`：文献**指针**（每篇 `DOI_*.md`，`fulltext:` 指向 `_library\references`）+ NLM 引用与摘要列表（原「参考文献」/ materials/citation）；**亦可**写作参考 pptx/doc/docx；与 `citation/` 审计台账分夹；全文实体在 `_library\references`。
- `citation/`：仅 `CITATION_AUDIT*` / 跳过说明 / 期刊引用日志。
- `code-gates/`：脚本说明 + 门控/哈希报告（原 `code/`+`gates/`）。
- 根上 `tables/` `figures/` `pipeline/`：统计表图与流水线夹；**hashes / MANIFEST / pipeline_run.log 在 `ref\pipeline/`**（原 `analysis/`/`results/` locks）；`qc.html` 仍在 `ref\` 根。
- 写作参考（可在 `refer/`）、`submission-*`、数据底表：原 `materials/` 子项（D-1：今后移底表先问）。
- 并注明：「分析错分/临时表 `false_classification*` 与结果 HTML（`Results*.html`）落当次结果夹 `<project>/<endpoint>/`（或 OUT_DIR / `SUBPROJECT_BY_OUTCOME`），不在子工程根，也不在 ref」
- 课题事实指针：伦理批件行、扫描参数登记表行、涉及的实验室检验项（查找与禁补编 → `project-fact-lookup.md`）；通讯作者邮箱不写进 README。亦可追加到 `manuscript-revision.md`。

## 跳过 / 幂等规则（再跑前先读 ledger）

助手在**再次**跑同一门控或层之前，**必须**先读 `ref\manuscript-revision.md` 与引用 ledger。无 ledger 理由的静默跳过禁止（见保证六态：`NOT_APPLICABLE` ≠ 静默跳过）。

| 领域 | 何时跳过 | 否则 |
|---|---|---|
| 文献 / 引用 L4 | 同键（`DOI` **或** citekey）+ 同 **layer** + 同 **fine_id**（或技能 id）已在 `ref\citation/CITATION_AUDIT.json`（或 `.jsonl`）记为 PASS/KEEP，且输入哈希未变 | 重跑；追加/更新条目；给出六态 verdict |
| Word / 抛光 | 段落或区间已在 `ref\manuscript-revision.md` 记为已改或仅审阅 | 追加新行；勿静默再抛光 |
| 审稿轮次 | `ref\review/changelog.md` 已标完成（Implemented / Not implemented 已关） | 开新轮文件或追加；无主人要求勿改写已关闭轮次 |
| 门控 / 保证 | 同 gate id + 匹配的 `audited_input_hashes` 已在 `ref\code-gates/` 要求保证级别 PASS | 哈希过期或保证升级则重跑（`submission` / `conference-ready` 禁止静默跳过） |

引用 ledger 键形（内部；非对外口号）：`DOI|citekey` + `layer` + `fine_id`。优先 JSON 数组或 `{"entries":[]}` 信封。

交叉链接：

- 引用 L4 / 三轴 + 六态 → `{SKILLS}\05_manuscript\qc\citation-audit-gate.md`
- 保证六态 → `{SKILLS}\06_review\qc\assurance-verdicts.md`
- Word 追加规则 → `{SKILLS}\06_review\advanced\word-edit.md` + `{SKILLS}\05_manuscript\SKILL.md`
- 子工程交付落点（备忘录查阅、终稿留根）权威页 → `{SKILLS}\00_orchestrator\references\standing-delivery.md`，细则不在本文件展开。

## 本契约**不做**的事

- 不在空课题上批量预建空文件夹，直到首次写入产物（按需创建子夹 copy-on-need）。
- 不移动 ethics 锁定树，不写 `advanced/`。
- 不安装 ARIS runtime。
- 不静默删除；空壳只移 `{DEL}`。

## 编辑前原件（`-org`）

- 名为 `*-org` / `*org*` 的文件（如 `comments-org.docx`、`SARC_CT_MRI_manuscript-org.docx`）是**编辑前原件**。留在课题内 (通常 `ref\review/`)。
- 主人收工/清理时：**勿丢弃** `-org` 原件。只把真正的中间件从 `ref\tmp/` 移到 `{DEL}\_by-project\<project>\`。若 `-org` 曾停在 `tmp/`，清理前先提升到 `ref\review/`（或留在根）。
