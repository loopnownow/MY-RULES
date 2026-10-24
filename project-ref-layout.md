# 项目 `ref/` 布局（ledger + 产物）

**负责人：** `00_orchestrator`。
**读者：** 任何把 QC、引用、Word、门控或执行产物写入项目 `ref/` 的技能。
**EXECUTION / 收工时间戳：** Asia/Shanghai (UTC+08:00)。

本文是**文件夹地图与跳过/幂等契约**。不编造临床数字。文件名与 ledger 行除课题科学所需（路径、DOI、citekey）外，不含 PII。

## 根目录不变量（勿挪位）

以下必须留在 **`ref/` 根**（技能与约定硬性要求）：

| 路径 | 作用 |
|---|---|
| `ref/settings.ini` | 仅 RAD / 流水线配置。勿随意覆盖；勿存密钥。 |
| `ref/manuscript-revision.md` | 只追加的主变更 ledger（主人要求 + 代码/结果/Word）。05/06 Word 轮次后在此追加（`06_review/personal/word-edit.md`）。**已登记段落勿再抛光**，除非上游数字变了、主人点名、或未解决批注已授权。 |

根上可选（若已在用）：`ref/project-state.yaml`（来自 `00_orchestrator/templates/project-state.yaml`）。在未来契约另有规定前，优先留在根。

## 子文件夹地图

| 子文件夹 | 放这里 | 不放这里 |
|---|---|---|
| `ref/review/` | 每轮 `changelog.md` / `CHANGELOG_*.md`；审稿交接 YAML；Lee 轮次笔记 | 主 Word 变更 ledger（仍用 `manuscript-revision.md`） |
| `ref/citation/` | `CITATION_AUDIT.json`（或 `.jsonl`）；引用 README / 跳过说明；期刊/引用日志（`ref_journal_log.txt`、`CITATION*`） | 完整 PDF 语料库 |
| `ref/gates/` | `GATE*_report.md`、数字锁定、输入/输出哈希报告 | 现役 `settings.ini` |
| `ref/code/` | 脚本/路径说明、补丁指针（无密钥、无 token） | 原始凭据 |
| `ref/results/` | 表/图锁定说明与内容哈希 | 大型二进制数据集（留在 derivatives）；终表/终稿放**子工程根**（**不建** `0result\`） |
| `ref/exec/` | 可选 `EXECUTION.md` 收工记录；非审稿轮次的运维笔记 | 面向主人的 ACCEPT 报告（除非主人要求） |
| `ref/tmp/` | 课题本地**中间** Word/PDF/草稿（Claude diff、被替代的 TC、`-copy`、合并草稿），保留到主人说清理/收工 | 当前终稿（留在课题根）；已关闭轮次 changelog（`review/`）；citation/gates ledger；密钥 |

### `ref/tmp/` 清理

- 首次需要时创建（与其它子夹一样 copy-on-need）。
- 助手可将中间件暂存于此，避免散落在 `ref/` 根或课题根。
- **禁止**静默删除。主人说清理 / 收工时，把整个 `ref/tmp/` 树（或点名文件）移入 `D:\0del\_by-project\<project>\`（跨课题则 `_by-function`），有用时保留相对名。
- 清理后留下空的 `ref/tmp/` 或下次写入时再建；勿在此编造临床内容。

项目一旦采用本布局，另备一份简短 **`ref/README.md`** 地图（见模板）。

## 跳过 / 幂等规则（再跑前先读 ledger）

助手在**再次**跑同一门控或层之前，**必须**先读 `ref/manuscript-revision.md` 与引用 ledger。无 ledger 理由的静默跳过禁止（见保证六态：`NOT_APPLICABLE` ≠ 静默跳过）。

| 领域 | 何时跳过 | 否则 |
|---|---|---|
| 文献 / 引用 L4 | 同键（`DOI` **或** citekey）+ 同 **layer** + 同 **fine_id**（或技能 id）已在 `ref/citation/CITATION_AUDIT.json`（或 `.jsonl`）记为 PASS/KEEP，且输入哈希未变 | 重跑；追加/更新条目；给出六态 verdict |
| Word / 抛光 | 段落或区间已在 `ref/manuscript-revision.md` 记为已改或仅审阅 | 追加新行；勿静默再抛光 |
| 审稿轮次 | `ref/review/changelog.md` 已标完成（Implemented / Not implemented 已关） | 开新轮文件或追加；无主人要求勿改写已关闭轮次 |
| 门控 / 保证 | 同 gate id + 匹配的 `audited_input_hashes` 已在要求保证级别 PASS | 哈希过期或保证升级则重跑（`submission` / `conference-ready` 禁止静默跳过） |

引用 ledger 键形（内部；非对外口号）：`DOI|citekey` + `layer` + `fine_id`。优先 JSON 数组或 `{"entries":[]}` 信封 — 见模板。

交叉链接：

- 引用 L4 / 三轴 + 六态 → `05_manuscript/qc/citation-audit-gate.md`
- 保证六态 → `00_orchestrator/qc/assurance-verdicts.md`
- Word 追加规则 → `06_review/personal/word-edit.md` + `05_manuscript/SKILL.md`
- 交付落点 → `00_orchestrator/references/standing-delivery.md`

## 本契约**不做**的事

- 不在空课题上批量预建空文件夹，直到首次写入产物（模板供 copy-on-need）。
- 不移动 ethics 锁定树，不写 `personal/`。
- 不安装 ARIS runtime。

## 模板

按需拷贝树：[`project-ref-template/`](project-ref-template/)。

## 编辑前原件（`-org`）（2026-10-19）

- 名为 `*-org` / `*org*` 的文件（如 `comments-org.docx`、`SARC_CT_MRI_manuscript-org.docx`）是**编辑前原件**。留在课题内——通常 `ref/review/`。
- 主人收工/清理时：**勿丢弃** `-org` 原件。只把真正的中间件从 `ref/tmp/` 移到 `D:\0del\_by-project\<project>\`。若 `-org` 曾停在 `tmp/`，清理前先提升到 `ref/review/`（或留在根）。
