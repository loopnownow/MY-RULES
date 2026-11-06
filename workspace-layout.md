---
name: workspace-layout
description: 本机布局与子工程短针。落点见 My rule.md §5。
---

# 本机布局与子工程

路径别名见 `My rule.md` §1。代码路径别名（`{code_root}`、`{code_modules}`、`{code_stats}`、`{code_data_processing}`）见 skills `lab-paths.yaml`。工作区只有一层（`D:\0Grok\<stage>\<project>`）；不再有 A/B 双工作区。

## 一行布局

| 根 | 角色 |
|---|---|
| `D:\00db`（`{RAW}`） | 已组织的原始库（大体量影像等按 slug）；只读除非点名；细则见下节 |
| `D:\0del`（`{DEL}`） | AI 可操作临时/移出区（`_by-project` / `_by-function`） |
| `D:\0Grok\0doc` | 语料 + 可复用代码；live tops：`_library`（含 `references` 文献全文、`lit-bank` 书目、`journals` 期刊池与选刊侧私有、`ethics\approvals` 批件、`lab-ref-ranges`、`glossary` 自有语料+四层（words/sentences/paragraphs + sections 指针页；`GLOSSARY_ROOT`）） / `templates` / `mem` / `GitHub` / `test` / `skill-harvest`（+ 根 md；`_bank` 2026-11-01 并入 `_library\glossary`，`_code` 2026-11-01 退役） |
| `D:\0Grok\0doc\mem` | bot 记忆导出/更新落点（城城 2026-10-25）；**仅隐私** + 可变数据 SSOT（如 find-journal JCR xlsx）；站立政策不进 mem |
| `D:\0Grok` | 分阶段子工程工作区（阶段夹见下节） |
| `D:\0Grok\R&P`（formerly `proposal`） | 申请/立项及相关材料包；**非**稿件阶段夹（见下「兄弟根」） |

### `{RAW}` = `D:\00db`（原始库契约 · t1705u）

- **落点：** 大体量原始文件放 `D:\00db\<slug>\`（`<slug>` 与课题夹名一致）：DICOM 序列、NIfTI/NII.GZ、未处理的 4D/导出包、按序列存的影像树等。
- **子工程只留指针：** 在 `ref/settings.ini` 写 data path；**不要**把原始体拷进 `D:\0Grok\…` 或三仓（MY-RULES / MY-SKILLS / MY-CODES）。
- **衍生件仍在课题侧：** 衍生物 / 图 / 表按本文件与 `project-ref-layout.md` 落在子工程；勿塞进 `00db`。
- **临床底表 ≠ 影像 raw：** Excel/CSV 底表仍落 `ref/` 或 `ref/data/`（D-1：移动前先问）。**不要**把所有「data」都倒进 `00db`。
- **现行名只写 `00db`；活 `00ds` = QC 对象：** `D:\00ds` / 夹名 `00ds` 已退役。任何活路径、夹名、过滤器/默认项仍写 `00ds` 的，视为 QC 发现，**必须更正为 `00db`**；**不要**在活 allowlist/filter 里把 `00ds` 留作「legacy」。changelog 里「曾用/原 `00ds`」的历史叙述可留。不另造第三个 raw 根。**更正活引用 ≠ 搬迁磁盘树**；本票不 bulk 迁移 `D:\00ds` / `D:\00db`（两边若都在，维持原状，等主人另批搬迁）。
- **禁止进 git：** 原始影像二进制**不要**进 git（含 Git LFS）或任何 GitHub remote（DICOM 头含 PHI；二进制无有效 delta）。可选轻量清单（相对路径 + 大小 + SHA-256 + 入库日）可放子工程 `ref/pipeline/`（同 `hashes.tsv` / `MANIFEST.md` 思路）。该清单若需版本，可用**无 remote 的本地 git**；备份 = 拷到另一块盘，不是 git。
- **只读默认：** `{RAW}` 只读，除非主人点名写入。**不预建空夹**（用到再拷 / copy-on-need）。

**云端 / 本地：** 云端 = Grok Bot box；本地 = 城城本机。详见 `My rule.md` §1。

可选：数据课题也可在上述子工程树内自建文件夹；约定写在该子工程内，不进全局 rules/skills。

## 阶段夹与课题名

课题路径：`D:\0Grok\<stage>\<project>`。

| 阶段 | 含义 |
|---|---|
| `drafting` | 选题 / 数据 / house 稿 |
| `pre-submit` | 投目标刊前打磨 |
| `in-review` | 已投 / 在审 / 修回再投（收到审稿意见是事件，不是阶段） |
| `accepted` | 接收 / 校样 |

已有文件夹若仍用旧名，按下表阅读。**不改写**这些夹。**不新建** `DER`。

旧阶段夹名仅作别名阅读；**勿重建** `preparing`/`polishing`/`submitting`/`reseived`。

| 旧名 | 读作 |
|---|---|
| `preparing` | `drafting` |
| `polishing` | `pre-submit` |
| `submitting` | `in-review` |
| `reseived`、`received` | `accepted` |

别名表在 `{SKILLS}\00_orchestrator\templates\project-state.yaml` 的 `study_folder_stage_aliases`（路径段别名，不是 `pipeline.stage`）。

课题夹名：`lowercase_UPPERCASE`（如 `fyh_CAC`、`xlm_LG`）。旧式 `CAC_fyh`、`lung_xlm` 已退休。

## 兄弟根：`R&P`（非阶段）

`D:\0Grok\R&P`（formerly `proposal`）存放 grants / proposals / related packets。**不是**稿件流水线的第五阶段：不要写入上方 `drafting` / `pre-submit` / `in-review` / `accepted` 阶段表，也不进 `study_folder_stage_aliases`。路径写作 `R&P`（含 `&`）；历史叙述可写「was / formerly proposal」。

## 文件落点

交付表权威 → `My rule.md` §5。`ref/` 子目录 → 同仓 `project-ref-layout.md`。

| 种类 | 落点 |
|---|---|
| 草稿 / 旧稿 / 一次性脚本 | 子工程内临时/中间/旧版稿 → `ref/tmp/`（非默认 `{DEL}`；t1450u）。跨课题或无子工程一次性 → `{DEL}` 的 `_by-project\` / `_by-function\`。`{DEL}` 定期清空，值得长期保留的不放这里。细则 → `My rule.md` §5 / `project-ref-layout.md`。 |
| 共享统计库 | `{code_modules}`（`D:\0Grok\0doc\GitHub\MY-CODES\modules`）。入口：`PYTHONPATH={code_stats}` 后 `python -m modules.pipeline`。课题只指向该树，不在课题内再放 `modules\`。未点名则不改该库。技能正文（怎么用、按什么规则）在 `{SKILLS}\02_data-processing\`；本仓只管代码。 |
| 02 运维（整理 / 清洗 / 同步） | `D:\0Grok\0doc\GitHub\MY-CODES\tools\`（`{code_stats}` + `tools/<fine-id>/`；席位夹名不镜像 `02-…`/`03-…`）。统计引擎与建模 CLI 在 `D:\0Grok\0doc\GitHub\MY-CODES`（2026-10-25 起独立主库；2026-11-01 由 `stats-analysis` 更名）。 |
| 参考包 / 锁定笔记 | 课题 `ref/`。运行键只在 `ref/settings.ini`。可选 `ref/project-state.yaml` 只记设计与稿件进度。 |
| 文献全文（PDF/HTML） | `D:\0Grok\0doc\_library\references\<L1>\<L2>\`（一文一文件，名用 DOI；t1455u）；子工程 `ref/refer\` 只写 `DOI_*.md` 指针；书目进 `_library\lit-bank`（不存 PDF） |
| 期刊池 / 批件 | `_library\journals\index.csv`（单表，2026-10-31 起不再留 xlsx）；`_library\ethics\approvals\<L1>\<L2>\` + `approvals-index.xlsx`（t1458u）；子工程候选刊只写 `ref\citation\journals.csv` + `_notes.md`。口径 → `library-taxonomy.md` |
| 现行分析数字 | `<project>/<endpoint>/`；成对比较再套 `<positive_display>_vs_<negative_display>/`。稿件活数字只来自该处 `Results*.html`（新写 `Results{subproject}.html`）。旧 `{endpoint}-results.html`、`results.html` 仍可读取。与 `.xlsx` 冲突以 HTML 为准（`My rule.md` §5）。**结果 HTML 不提升到子工程根**（t1660u；`false_classification*` 同落该结果夹 → `project-ref-layout.md`）。 |
| 课题 QC | 主 QC：`<project>/ref/qc.html`。外部 QC：`<project>/ref/qc-ext-*.html`（文件名不用 `qc.html`）。 |

同夹多份稿件：留与当前 HTML 相符的最新一份；其余仅当用户要求才移入 `{DEL}`。

## 控制台与 `ref/settings.ini`

- 课题侧运行配置只留 console（`{project}.html`）与 `ref/settings.ini`。
- **起始页占位符（2026-11-05）**：`<project>/<project>.html` 由金版 `modules/console/project.html` 派生时，`__MODULES_DEFAULT__`（算法库路径）**必须替换**；`__CONSOLE_TOKEN__` 只在 `<meta name="console-token">` 一处写 token，另外 **2 处 JS 哨兵必须留占位符**（写死具体 token 之后 `register --rotate` 只能改 meta，页面会留下上一枚旧 token）。漏替 `__MODULES_DEFAULT__` → 内联脚本首行 `ReferenceError`、整页按钮全失效（「开启服务」没反应）。生成用 `{RULES}\tools\sync_project_page.py`（token 传空串 = 保持未登记），或从 `http://127.0.0.1:<port>/start.html` 另存；只补该占位符用 `{RULES}\tools\fill_start_placeholders.py`。因为 `smoke_page.js` 会把占位符换成空串，**`node --check`/`smoke_page.js` 全绿也可能是死页**——改完必须真浏览器复核（`firefox --headless --screenshot`，标题=项目名）。
- 算法只来自 `{code_modules}`。不留课题内 `modules\`，不留长期 `config\settings.py`。
- `MODULES_DIR` 必须指向已存在的目录。空或不是目录时，console 与 `import modules` 明确报错，不回退到默认或旧路径。
- `{project}.html` 当次可覆盖 ini；写回更新 `ref/settings.ini`。无覆盖的命令行只读 ini。

## 子工程约定

- 写入 `0doc\` 须用户点名「放 0doc」。
- **最终**→子工程根；**中间**→`ref/` 地图；**无** `0result\`；子工程内临时 → `ref/tmp/`（非默认 `{DEL}`）；无子工程/跨课题临时进 `{DEL}`；Downloads 仅当点名。权威 → `My rule.md` §5。
- 可复用脚本 → 统计引擎与建模 CLI 在 `{code_stats}`（`modules/` + `model-validation/`），运维/加工脚本在 `{code_stats}\tools\<fine-id>\`（`_code` 已于 2026-11-01 整层退役：脚本在 MY-CODES，壳与索引移至 {DEL}）。`0script\` 已退休，不在课题根重建。长期规则/语料 → `0doc` 相应层。
- 根不留临时/草稿/一次性中间件（例外：现行在改稿 / 现行 `Vn`）。旧版稿与中间件进 `ref/tmp/`，不进 `{DEL}`（除非过后清理先问）。`0doc\GitHub\MY-CODES\modules\` 增改移须先同意。
- 数据课题根可留：`rawdata`、`derivatives`、`atlases`、索引/manifest、`ref`。`0doc` 仅当点名「放 0doc」。默认从 `derivatives` 拷出要用的结果，原件留在原处；终稿落子工程根。不建 `0result\`，不重建 `0script\`。
- 同键终表合并为一张（一段说明，值列加前缀）。把原件移出子工程根须先同意。
- 移脚本或文档前先搜 `import` / `addpath` / `settings.ini` / README。仍有未改引用则不移。移完后改路径与 `0doc` 示例再测。
- 课题索引用 `.xlsx`，说明用 `.md`。不用 `*.tsv` 当课题索引。
- 02 整理 / 清洗 / 同步 / 抽取 → `{SKILLS}\02_data-processing\advanced\route.md`（编码 `coding.md`，抽取 `extract.md`）。表先于统计、`exc`、假分类、控制台键位与界面不在本文件展开 → 同目录 `coding.md` / `extract.md`，以及 `{SKILLS}\02_data-processing\advanced\analysis\pipeline.md`。
- **`ref/` 子目录** → 同仓 `project-ref-layout.md`；技能正文 `{SKILLS}\00_orchestrator\references\project-ref-layout.md`。

## 新建文件夹 / 新建文件

只许建在 `{DEL}` / `D:\0del\` 的 `_by-project\`、`_by-function\`。权威与例外 → `My rule.md` §5.1（含 `0doc` 默认禁止 mkdir、**改已有文件须当轮点名或先问**（§2 总闸 t1672u）、一次性脚本不进主目录 / `.grok\tmp` / 课题根）。本段不复写。bot mem 落点例外（`D:\0Grok\0doc\mem\`）→ `My rule.md` §1 + §5.1。

**目录命名（t1458u）**：`0doc` 下目录一律 ASCII 英文（`approvals` / `journals` / `jcr`）；中文目录发现即当轮 rename，并在 `_library\MOVED-FROM.md` 记一行。库分类与 L1/L2 → `library-taxonomy.md`。

**0del 内部三档**（park / harvest-park / harvested，原 junk）与落 harvested 前的 grep 要求 → `My rule.md` §5.3。
