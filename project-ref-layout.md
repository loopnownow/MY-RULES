# 项目 `ref/` 布局（ledger + 产物）

**负责人：** `00_orchestrator`。
**读者：** 任何把 QC、引用、Word、门控或执行产物写入项目 `ref/` 的技能。
**EXECUTION / 收工时间戳：** Asia/Shanghai (UTC+08:00)。

本文是**文件夹地图与跳过/幂等契约**。不编造临床数字。文件名与 ledger 行除课题科学所需（路径、DOI、citekey）外，不含 PII。

**SSOT：** 本文件为**权威中文版**。技能侧镜像（英文）`{SKILLS}\00_orchestrator\references\project-ref-layout.md` 只作运行期读本；两版冲突以本文件为准（2026-10-29；t1303s6243：`writing-refs/` + `raw-pre/` 合并为 `materials/`；保留 `review/` 与 `citation/` 分夹；t1300u：去 `exec/`，`code`+`gates` 合并为 `code-gates/`；Cleanup 两档，非「除 results 外全清」）。

## 根目录不变量（勿挪位）

以下必须留在 **`ref/` 根**（技能与约定硬性要求）：

| 路径 | 作用 |
|---|---|
| `ref/settings.ini` | 仅 RAD / 流水线配置。勿随意覆盖；勿存密钥。 |
| `ref/manuscript-revision.md` | 只追加的主变更 ledger（主人要求 + 代码/结果/Word）。05/06 Word 轮次后在此追加（`{SKILLS}\06_review\advanced\word-edit.md`）。**已登记段落勿再抛光**，除非上游数字变了、主人点名、或未解决批注已授权。 |

根上可选（若已在用）：`ref/project-state.yaml`（来自 `{SKILLS}\00_orchestrator\templates\project-state.yaml`）。在未来契约另有规定前，优先留在根。

## 子文件夹地图

尽量少的 `ref/` 子夹。现用地图（按需创建，**不预建空夹**）：

| 子文件夹 | 放这里 | 不放这里 |
|---|---|---|
| `ref/review/` | 每轮 `changelog.md` / `CHANGELOG_*.md`；审稿交接 YAML；Lee 轮次笔记 | 主 Word 变更 ledger（仍用 `manuscript-revision.md`） |
| `ref/citation/` | `CITATION_AUDIT.json`（或 `.jsonl`）；引用 README / 跳过说明；期刊/引用日志（`ref_journal_log.txt`、`CITATION*`） | 完整 PDF 语料库；写作参考草稿与预清洗表（见 `materials/`） |
| `ref/code-gates/` | 脚本/路径说明、补丁指针（无密钥）；`GATE*_report.md`、数字锁定、输入/输出哈希报告 | 现役 `settings.ini`；原始凭据。**原并列的 `code/` 与 `gates/` 不再分夹** |
| `ref/results/` | 表/图锁定说明与内容哈希（稿件/门控用） | 大型二进制数据集（留在 derivatives）；分析临时结果树（见下「三区」）；终表/终稿放**子工程根**（**不建** `0result\`） |
| `ref/materials/` | 写作参考草稿/PDF（论文分件、丁*、QIANG* 等 refs 版本）**以及**本子工程预清洗/导入表（xls/xlsx/csv）。可用文件名或可选松散子夹区分两类；不强制子夹。移动时保留人类可读文件名；去标识后缀 `_noName` / `_deid` 可保留 | **当前**正文稿（留在子工程根）；citation PDF 语料库（`citation/` 只放 audit/日志）；大体量已整理 raw（留在 `{RAW}`=`D:\00db`） |
| `ref/tmp/` | 课题本地**中间** Word/PDF/草稿（Claude diff、被替代的 TC、`-copy`、合并草稿），保留到主人说清理/收工 | 当前终稿（留在课题根）；已关闭轮次 changelog（`review/`）；citation / code-gates ledger；密钥 |

**已退役（勿再新建）：** 独立 `ref/exec/`、`ref/code/`、`ref/gates/`、`ref/writing-refs/`、`ref/raw-pre/`。旧树若仍存在，按主人点名迁入 `code-gates/` 或 `materials/`，或走 Cleanup；本轮**不**自动迁 live 文件。

### 三区 / 临时结果区

- **分析临时结果**（`ASL/`、`DKI/`、`DTI_IVIM/` 等）放在**子工程根旁**，**不进 `ref/`**。
- `ref/results/` = 面向稿件/门控的锁定说明与哈希；**勿**与 `ASL/` 等分析树合并。
- **终稿 / 控制台终表**留在子工程根。

### Cleanup（过后可清；两档，非「除 results 外全清」）

**禁止**静默删除。清理时**先问城城再移**；优先移入 `D:\0del\_by-project\<project>\`（跨课题则 `_by-function`），有用时保留相对名。**不要**把「除 `results/` 以外的整棵 `ref/`」一律清掉。

**默认可清 → 0del**（先问再移）：

- `ref/tmp/`（整树或点名文件）
- 已废的 `materials/` 旧写作参考 / 过期预清洗表
- 合并前残留的独立 `exec/` / `code/` / `gates/` / `writing-refs/` / `raw-pre/` 空壳（迁并完成后的空目录）

**默认保留：**

- `ref/results/`
- 仍在用的 `ref/citation/`
- `ref/code-gates/`
- 当前仍在用的 `materials/`
- 根上 `settings.ini` / `manuscript-revision.md` / `README.md`（及仍在用的 `project-state.yaml`）
- `ref/review/` 中未关闭或主人未点名丢弃的轮次材料；`-org` 编辑前原件（见下节）
- ASL 类分析树（在子工程根，不在 `ref/`）：默认保留；仅当城城点名整树时再清

首次需要时创建子夹（copy-on-need）；清理后可留空 `ref/tmp/` 或下次写入时再建；勿在此编造临床内容。

### `ref/README.md`（采用本布局时）

项目一旦采用本布局，在 `ref/` 根备一份简短 **`ref/README.md`**，至少各用一行写明：

- `materials/`：写作参考草稿/PDF + 本子工程预清洗/导入表（原 `writing-refs/` + `raw-pre/`）；用文件名或可选子夹区分；大体量 raw 在 `{RAW}`。
- `code-gates/`：脚本说明 + 门控/哈希报告（原 `code/`+`gates/`）。
- 并注明：「分析临时结果在子工程根 `<Modality>/`，不在 ref」。

## 跳过 / 幂等规则（再跑前先读 ledger）

助手在**再次**跑同一门控或层之前，**必须**先读 `ref/manuscript-revision.md` 与引用 ledger。无 ledger 理由的静默跳过禁止（见保证六态：`NOT_APPLICABLE` ≠ 静默跳过）。

| 领域 | 何时跳过 | 否则 |
|---|---|---|
| 文献 / 引用 L4 | 同键（`DOI` **或** citekey）+ 同 **layer** + 同 **fine_id**（或技能 id）已在 `ref/citation/CITATION_AUDIT.json`（或 `.jsonl`）记为 PASS/KEEP，且输入哈希未变 | 重跑；追加/更新条目；给出六态 verdict |
| Word / 抛光 | 段落或区间已在 `ref/manuscript-revision.md` 记为已改或仅审阅 | 追加新行；勿静默再抛光 |
| 审稿轮次 | `ref/review/changelog.md` 已标完成（Implemented / Not implemented 已关） | 开新轮文件或追加；无主人要求勿改写已关闭轮次 |
| 门控 / 保证 | 同 gate id + 匹配的 `audited_input_hashes` 已在 `ref/code-gates/` 要求保证级别 PASS | 哈希过期或保证升级则重跑（`submission` / `conference-ready` 禁止静默跳过） |

引用 ledger 键形（内部；非对外口号）：`DOI|citekey` + `layer` + `fine_id`。优先 JSON 数组或 `{"entries":[]}` 信封。

交叉链接：

- 引用 L4 / 三轴 + 六态 → `{SKILLS}\05_manuscript\qc\citation-audit-gate.md`
- 保证六态 → `{SKILLS}\06_review\qc\assurance-verdicts.md`
- Word 追加规则 → `{SKILLS}\06_review\advanced\word-edit.md` + `{SKILLS}\05_manuscript\SKILL.md`
- 交付落点 → `{SKILLS}\00_orchestrator\references\standing-delivery.md`

## 本契约**不做**的事

- 不在空课题上批量预建空文件夹，直到首次写入产物（按需创建子夹 copy-on-need）。
- 不移动 ethics 锁定树，不写 `advanced/`。
- 不安装 ARIS runtime。
- 本轮不迁 live 子工程里的旧 `code/`/`gates/`/`exec/`/`writing-refs/`/`raw-pre/` 树；不预建 `materials/` 空夹。

## 编辑前原件（`-org`）（2026-10-19）

- 名为 `*-org` / `*org*` 的文件（如 `comments-org.docx`、`SARC_CT_MRI_manuscript-org.docx`）是**编辑前原件**。留在课题内 (通常 `ref/review/`)。
- 主人收工/清理时：**勿丢弃** `-org` 原件。只把真正的中间件从 `ref/tmp/` 移到 `D:\0del\_by-project\<project>\`。若 `-org` 曾停在 `tmp/`，清理前先提升到 `ref/review/`（或留在根）。