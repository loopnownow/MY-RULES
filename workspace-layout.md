---
name: workspace-layout
description: 本机布局与子工程短针。落点见 My rule.md §5。
---

# 本机布局与子工程

路径别名见 `My rule.md` §1。代码路径别名（`{code_root}`、`{code_modules}`、`{code_stats}`、`{code_data_processing}`）见 skills `lab-paths.yaml`。工作区只有一层（`D:\0Grok\<stage>\<project>`）；不再有 A/B 双工作区。

## 一行布局

| 根 | 角色 |
|---|---|
| `D:\00db`（`{RAW}`） | 已组织的原始库；只读除非点名 |
| `D:\0del`（`{DEL}`） | AI 可操作临时/移出区（`_by-project` / `_by-function`） |
| `D:\0Grok\0doc` | 语料 + 可复用代码；live tops：`_library`（含 `references` 文献全文、`lit-bank` 书目、`journals` 期刊池与选刊侧私有、`ethics\approvals` 批件、`lab-ref-ranges`） / `_bank` / `_code` / `templates` / `mem` / `GitHub` / `test` / `skill-harvest`（+ 根 md） |
| `D:\0Grok\0doc\mem` | bot 记忆导出/更新落点（城城 2026-10-25）；**仅隐私** + 可变数据 SSOT（如 find-journal JCR xlsx）；站立政策不进 mem |
| `D:\0Grok` | 分阶段子工程工作区（阶段夹见下节） |

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

## 文件落点

交付表权威 → `My rule.md` §5。`ref/` 子目录 → 同仓 `project-ref-layout.md`。

| 种类 | 落点 |
|---|---|
| 草稿 / 旧稿 / 一次性脚本 | 子工程内临时/中间/旧版稿 → `ref/tmp/`（非默认 `{DEL}`；t1450u）。跨课题或无子工程一次性 → `{DEL}` 的 `_by-project\` / `_by-function\`。`{DEL}` 定期清空，值得长期保留的不放这里。细则 → `My rule.md` §5 / `project-ref-layout.md`。 |
| 共享统计库 | `{code_modules}`（`D:\0Grok\0doc\GitHub\stats-analysis\modules`）。入口：`PYTHONPATH={code_stats}` 后 `python -m modules.pipeline`。课题只指向该树，不在课题内再放 `modules\`。未点名则不改该库。技能正文（怎么用、按什么规则）在 `{SKILLS}\02_data-processing\`；本仓只管代码。 |
| 02 运维（整理 / 清洗 / 同步） | `D:\0Grok\0doc\_code\02-data-processing\`（`{code_data_processing}`；其下无 `base\`）。统计引擎与建模 CLI 在 `D:\0Grok\0doc\GitHub\stats-analysis`（2026-10-25 起独立主库）。 |
| 参考包 / 锁定笔记 | 课题 `ref/`。运行键只在 `ref/settings.ini`。可选 `ref/project-state.yaml` 只记设计与稿件进度。 |
| 文献全文（PDF/HTML） | `D:\0Grok\0doc\_library\references\<L1>\<L2>\`（一文一文件，名用 DOI；t1455u）；子工程 `ref/refer\` 只写 `DOI_*.md` 指针；书目进 `_library\lit-bank`（不存 PDF） |
| 期刊池 / 批件 | `_library\journals\index.csv`（单表，2026-10-31 起不再留 xlsx）；`_library\ethics\approvals\<L1>\<L2>\` + `approvals-index.xlsx`（t1458u）；子工程候选刊只写 `ref\citation\journals.csv` + `_notes.md`。口径 → `library-taxonomy.md` |
| 现行分析数字 | `<project>/<endpoint>/`；成对比较再套 `<positive_display>_vs_<negative_display>/`。稿件活数字只来自该处 `Results*.html`（新写 `Results{subproject}.html`）。旧 `{endpoint}-results.html`、`results.html` 仍可读取。与 `.xlsx` 冲突以 HTML 为准（`My rule.md` §5）。 |
| 课题 QC | 主 QC：`<project>/ref/qc.html`。外部 QC：`<project>/ref/qc-ext-*.html`（文件名不用 `qc.html`）。 |

同夹多份稿件：留与当前 HTML 相符的最新一份；其余仅当用户要求才移入 `{DEL}`。

## 控制台与 `ref/settings.ini`

- 课题侧运行配置只留 console（`{project}.html`）与 `ref/settings.ini`。
- 算法只来自 `{code_modules}`。不留课题内 `modules\`，不留长期 `config\settings.py`。
- `MODULES_DIR` 必须指向已存在的目录。空或不是目录时，console 与 `import modules` 明确报错，不回退到默认或旧路径。
- `{project}.html` 当次可覆盖 ini；写回更新 `ref/settings.ini`。无覆盖的命令行只读 ini。

## 子工程约定

- 写入 `0doc\` 须用户点名「放 0doc」。
- **最终**→子工程根；**中间**→`ref/` 地图；**无** `0result\`；子工程内临时 → `ref/tmp/`（非默认 `{DEL}`）；无子工程/跨课题临时进 `{DEL}`；Downloads 仅当点名。权威 → `My rule.md` §5。
- 可复用脚本 → `D:\0Grok\0doc\_code\`（`{code_root}`）；统计引擎与建模 CLI → `{code_stats}`。`0script\` 已退休，不在课题根重建。长期规则/语料 → `0doc` 相应层。
- 根不留临时/草稿/一次性中间件（例外：现行在改稿 / 现行 `Vn`）。旧版稿与中间件进 `ref/tmp/`，不进 `{DEL}`（除非过后清理先问）。`0doc\GitHub\stats-analysis\modules\` 增改移须先同意。
- 数据课题根可留：`rawdata`、`derivatives`、`atlases`、索引/manifest、`ref`。`0doc` 仅当点名「放 0doc」。默认从 `derivatives` 拷出要用的结果，原件留在原处；终稿落子工程根。不建 `0result\`，不重建 `0script\`。
- 同键终表合并为一张（一段说明，值列加前缀）。把原件移出子工程根须先同意。
- 移脚本或文档前先搜 `import` / `addpath` / `settings.ini` / README。仍有未改引用则不移。移完后改路径与 `0doc` 示例再测。
- 课题索引用 `.xlsx`，说明用 `.md`。不用 `*.tsv` 当课题索引。
- 02 整理 / 清洗 / 同步 / 抽取 → `{SKILLS}\02_data-processing\advanced\route.md`（编码 `coding.md`，抽取 `extract.md`）。表先于统计、`exc`、假分类、控制台键位与界面不在本文件展开 → 同目录 `coding.md` / `extract.md`，以及 `{SKILLS}\02_data-processing\advanced\analysis\pipeline.md`。
- **`ref/` 子目录** → 同仓 `project-ref-layout.md`；技能正文 `{SKILLS}\00_orchestrator\references\project-ref-layout.md`。

## 新建文件夹 / 新建文件

只许建在 `{DEL}` / `D:\0del\` 的 `_by-project\`、`_by-function\`。权威与例外 → `My rule.md` §5.1（含 `0doc` 默认禁止 mkdir、可改已有文件、一次性脚本不进主目录 / `.grok\tmp` / 课题根）。本段不复写。bot mem 落点例外（`D:\0Grok\0doc\mem\`）→ `My rule.md` §1 + §5.1。

**目录命名（t1458u）**：`0doc` 下目录一律 ASCII 英文（`approvals` / `journals` / `jcr`）；中文目录发现即当轮 rename，并在 `_library\MOVED-FROM.md` 记一行。库分类与 L1/L2 → `library-taxonomy.md`。

**0del 内部三档**（park / harvest-park / junk）与落 junk 前的 grep 要求 → `My rule.md` §5.3。
