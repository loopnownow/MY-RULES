---
name: zone-projects
description: L1 专题：子工程区，阶段夹、closeout、accepted 收工、archived 冷库、项目内落点、子工程约定。
up: My rule.md §5
owns: [Z1, Z2]
---

# 子工程区
- 管：阶段夹与课题名、阶段库管理、closeout、accepted 收工、archived 冷库（仍是冷库，不进阶段别名）、项目内文件落点、子工程约定、`settings.ini` 与 codes / skills 的调用口径。
- 不管：`ref\` 地图（→ `project-ref-layout.md`）；稿件硬闸（→ `manuscript-docx.md`）。

## 阶段夹与课题名

课题路径：`D:\MyProjects\<stage>\<project>`。

| 阶段 | 含义 |
|---|---|
| `drafting` | 选题 / 数据 / house 稿 |
| `pre-submit` | 投目标刊前打磨 |
| `reviewing` | 已投 / 在审 / 修回再投（收到审稿意见是事件，不是阶段） |
| `accepted` | 接收 / 校样 |

- 已有文件夹若仍用旧名 → 按 `aliases.yaml`（`kind: stage`）阅读；**不改写**、**勿重建**。**不新建** `DER` 阶段夹或根目录（`DER` 仅是 `_diseases.csv` 的家族码，不是阶段 / 工作区）。

课题夹名：`lowercase_UPPERCASE`（如 `fyh_CAC`、`xlm_LG`）。禁止 `CAC_fyh`、`lung_xlm` 这类写法。

**命名：** `<prefix>_<suffix>`——`<prefix>` = sub-PI 小写拼音首字母（如 `lxf`），`<suffix>` = 项目短码（大写或约定写法，如 `RC`/`CID`）。一人多题、一题多人都不改名；同后缀多例加 `_1`/`_2`（如 `llj_OV_1`）。中文人名只进台账（`_Docs\mem\people.csv`），路径与正文不写中文名。

### 阶段库管理规则（工程库）

| 事项 | 规则 |
|---|---|
| 谁能动 | 阶段夹内的搬件/改名/删只由该项目 owner 发起，或 owner 当轮点名；QC 只报不擅动，修复须授权（`My rule.md` §2）。 |
| 进场 | 新课题先建 `ref\` 四件（`settings.ini` / `README.md` / `manuscript-revision.md` + `ref\`），`INPUT` 必须可解析；空 `INPUT` 视为未开跑。 |
| 出场 | 阶段推进靠事件（开跑 / 投稿 / 接收 / 校样），不靠目录名；`accepted` 收工按本文件「accepted 收工」四落点分流。 |
| 痕迹 | 版本推进、搬件、改名、`.bak` 处置都写 `ref\manuscript-revision.md`；台账追加，不覆盖。 |
| 判据 | 骨架 / 命名 / 数据口径 → `{doc_root}\test\STAGE-QC-STANDARD.md`；机器门 S32–S34（`structure_check.py`）每轮 QC 必跑。 |

**`archived` 不是第五阶段：** 不进上表、不进 `study_folder_stage_aliases`；见本文件「archived 冷库」。关系总图 → §Z1、§Z2、§Z3。

## 工作区关系：阶段 · 分流 · harvest · 冷库

主人确认的工作区关系总图。细则清单仍见本文件「accepted 收工」「archived 冷库」；本节约束**关系**与授权，不复写硬留字节表。

### **§Z1** 两层：活阶段 vs 分流落点

- **四阶段 = 活课题生命周期：** `drafting` / `pre-submit` / `reviewing` / `accepted`。路径 `D:\MyProjects\<stage>\<prefix_suffix>\`。
- **分流落点（非阶段）：** `_DataBase` / `_Docs` / `.Del` / `archived`。`archived` **不是**第五阶段（见本文件「archived 冷库」；不进阶段表、不进 `study_folder_stage_aliases`）。

### closeout（物理落点；绑 accepted 流程结束）

**closeout = 收工搬盘**：精简活树后把字节落到分流落点。绑在 `accepted` 该稿流程结束之后；细节见本文件「accepted 收工」。概要：

1. 可复用语料 / 批件 / 模板 → `_Docs`（默认 `_library`；须当轮点名「放 _Docs」）
2. raw / 不可复现图 / `R*`/`P*` 包 / 难再算中间件 → `_DataBase\<family>\<prefix_suffix>\`（≥20 散文件先压，沿用现条）
3. 可脚本重生图 / 热副本 / 过期草稿 → `.Del`
4. 硬留：终稿 Word + `FinalData_`（或钉死 data）+ 可选 `settings.ini` → `archived\<family>\<prefix_suffix>\` + `ARCHIVED.md`（四条件齐仍有效）

### **§Z2** harvest（抽取）≠ closeout（搬盘）

- **harvest：** 抽「怎么做」→ `_Docs\harvest`；仅当主人说「进skills」才进 MY-SKILLS（extract ≠ promote；流程与纳入门禁见 `{SKILLS}\00_orchestrator\harvest\SKILL.md`，00 只调度/门禁/复核；指针见 `skills.md` §3）。
- **closeout：** 物理落点与精简；**不是** harvest 的替代步骤。
- **harvest 也不代替搬盘：** 抽完仍须按 closeout 把字节落到 `_DataBase` / `_Docs` / `.Del` / `archived`。
- **harvest 剩余件 / 先判 H1–H4 / 轮次去留** → `zone-del.md` §1 / §2 与 `zone-docs.md` §1（本文件不复写判据）。
- 关系总图 / harvest 授权 → §Z1、§Z2、§Z3。harvest 技能只抽「怎么做」；closeout 是落点；勿把 closeout 写成 harvest 步骤。

## accepted 收工

**目标：** 按 closeout 精简 `accepted\<prefix_suffix>\`，再搬进 `archived\<family(suffix)>\<prefix_suffix>\` + `ARCHIVED.md`。accepted 不长期堆满。本条是**落点契约**（closeout）；关系与 harvest 授权 → §Z1、§Z2、§Z3。harvest ≠ closeout。

### 课题树精简后硬留
1. 终稿两份：`Manuscript_<slug>_clean.docx` 与最新的 `Manuscript_<slug>_{V|R|P}…[_tracked].docx`（旧名先问再改名；旧版→`ref/tmp/`）。根上只留这两份**文件**，不要把整夹 `R*` / `P*` 留在根。
2. 复现 SSOT：`FinalData_<slug>.xlsx`（或 `ref/README` 钉死的现用 data.xlsx）。
3. 可选：`ref/settings.ini` 指到 `_DataBase\<family>\<prefix_suffix>\`（影像 raw 不进课题树）。

### R*/P* 整夹进 `_DataBase`
课题树内名为 `R*` / `P*` 的夹（修订包、投稿包，如 R1/R2/P1/P1.1）收工时**整夹**进 `_DataBase\<family>\<prefix_suffix>\`。若夹内单独文件 ≥20 或明显小文件堆，先 7z/zip + `.files.txt`（见 `zone-database.md`「进 `_DataBase` 多文件先压缩」）。校验通过后，原夹移 `D:\MyProjects\.Del\_by-project\<slug>\`。根上终稿仍只留 `_clean` 与最新带号稿两份**文件**（不是把整夹留在根）。

### 图分流
可复现图 → `.Del\_by-project\<slug>\`；不可复现 → `_DataBase`。

### 其它
- 其它 csv/xlsx：去重合并→DB；移删先问（D-1）。
- 脚本：仅用一次的留指针；功能相近且多次使用的先作 harvest 对象，可复用提案 MY-CODES（权威 → `zone-docs.md` §1 / §3）。
- THESIS/行政（伦理·科教科·财务）与单篇 SCI 分轨。
- 四条件齐再 archived（含 skill_ref 或 none）；更新 `_DataBase\_index.csv`、`mem\people.csv`（见本文件「archived 冷库」）。
- syn 口径 → `workspace-layout.md`。
- 关系总图 / harvest 授权 → §Z1、§Z2、§Z3。harvest 技能只抽「怎么做」；closeout 是落点；勿把 closeout 写成 harvest 步骤。

## archived 冷库

`D:\MyProjects\archived` 放**已完结**项目：`D:\MyProjects\archived\<family>\<prefix_suffix>\`（L1=`<family>` **家族根**短码；`<family>` 取自 `_diseases.csv` 的 `family` 列，与 `_DataBase\<family>\<prefix_suffix>\` 同桶；第二层 = 完整课题夹名）。不按年份分层。

- **L1 = 家族根：** 冷库按疾病家族/文档类型分桶，桶名 = `_diseases.csv` 的 `family` 列（留空 = 自家族，即基码本身；挂靠按同源聚合，见 `zone-database.md`「同源聚合」）。例：`archived\EGVB\js_CN`、`archived\MHE\ly_SCH_HE`、`archived\OTHERS\lxj_BMP6`。
- **叶夹名后缀 = 病种基码：** `archived\<family>\<prefix>_<suffix>[_<n>]\`；`<suffix>` 仍是基码（去末尾 `_\d+`；`SSD_DKI`、`SCH_HE` 等语义复合整段保留），实例号只留在叶子夹名（例 `archived\CC\fyh_CAC_1\`）。
- **两树同构：** `_DataBase` 与 `archived` 都用同一个 `<family>` 桶；靠 `_diseases.csv` 的 `suffix`/`family` 对应，S23 同时校验两树桶名与叶后缀。家族桶 `_PHI` / `__zip` / `_thesis` 与 `_lab` 仅存在于 `_DataBase`，冷库不设。
- **疾病短码 SSOT：** `_DataBase\_diseases.csv`（UTF-8；列 `suffix,name_en,name_zh,l1,l2,aliases,family`）。`suffix` = 基码；`family` = 家族根（留空 = 自家族）；编号形式进 `aliases`（如 `SSD_1`）。中英文全称**只**进本表（及 `_index.csv` 可抄空值）；路径规则不写长病名。
- **ethics / references** 仍用 library L1/L2（`library-taxonomy.md`）；靠 `_diseases.csv` 的 `suffix`↔`l1`/`l2` 对照，不另造路径层。

- **进场（四条全满足）：** ① 在 `accepted` 且该稿流程结束（接收/校样完成）；② skill 已提取或已按 `skills.md` §3 提案（`harvest` 有记录，无则记 `none`）；③ rule 候选已提交（无则记 `none`）；④ `_DataBase\_index.csv` 行与 `_Docs\mem\people.csv` 行已更新。
- **历史旧论文（如 `000-vip\科研\文章`）：** 先进 `accepted`，按 `<prefix>_<suffix>` 建项目；抽取（skill/rule/_DataBase/_Docs）完成后再按上条进冷库。**先 accepted，后 archived**，不直进冷库。
- **`ARCHIVED.md`（每个项目根一份）：** `archived_on`、`from_stage`、`slug`、`family`、`skill_ref`、`rule_ref`、`index_row`、`note`；缺项不进。
- **非阶段：** 不进阶段表、不进 `study_folder_stage_aliases`；`project-state.yaml` 的 `stage` 保持 `accepted`（不加 `archived` 枚举，避免 MY-SKILLS PR）。
- **与 QC 禁令消歧：** `My rule.md` §6 与 `skills.md` §6 的 skip/archived 禁令只约束**技能树/文档 QC**，**不适用**项目冷库；冷库 = 已完成，不是未处理。
- **只读默认：** 冷库不参与日常检索/改写；解冻 = 移回对应阶段夹 + 移除 `ARCHIVED.md`（须当轮点名）。
- **命名：** `name_zh → prefix` 进 `D:\MyProjects\_Docs\mem\people.csv`（`/mem/` 已 gitignore、_Docs 仓无 remote）。
- 不预建空夹；同一 `<prefix_suffix>` 不重复。

## 文件落点
交付表权威 → `My rule.md` §3。`ref\` 子目录 → 同仓 `project-ref-layout.md`。本表只补项目内差异，不复写 L0 落点表。

| 种类 | 落点 |
|---|---|
| 草稿 / 旧稿 / 一次性脚本 | → §X2。值得长期保留的不放 `{DEL}`。 |
| 共享统计库 | `{code_modules}`。入口：`PYTHONPATH={code_stats}` 后 `python -m modules.pipeline`。课题只指向该树，不在课题内再放 `modules\`。未点名则不改该库。技能正文在 `{SKILLS}\02_data-processing\`；本仓只管代码。 |
| 02 运维（整理 / 清洗 / 同步） | `{code_stats}\tools\`（`{code_stats}` + `tools/<fine-id>/`；席位夹名不镜像 `02-…`/`03-…`）。统计引擎与建模 CLI 在 `{code_root}`。 |
| 参考包 / 锁定笔记 | 课题 `ref\`。运行键只在 `ref\settings.ini`。可选 `ref\project-state.yaml` 只记设计与稿件进度。 |
| 现行分析数字 | `<project>/<endpoint>/`；成对比较再套 `<positive_display>_vs_<negative_display>/`。稿件活数字只来自该处 `Results*.html`（新写 `Results{subproject}.html`）。旧 `{endpoint}-results.html`、`results.html` 仍可读取。与 `.xlsx` 冲突以 HTML 为准（`My rule.md` §3）。**结果 HTML 不提升到子工程根**。 |
| 课题 QC | 主 QC：`<project>/ref/qc.html`。外部 QC：`<project>/ref/qc-ext-*.html`（文件名不用 `qc.html`）。 |

同夹多份稿件：留与当前 HTML 相符的最新一份；其余仅当用户要求才移入 `{DEL}`。


## 控制台与 `ref/settings.ini`

- 课题侧运行配置只留 console（`{project}.html`）与 `ref/settings.ini`。
- **起始页占位符**：`<project>/<project>.html` 由金版 `modules/console/project.html` 派生时，`__MODULES_DEFAULT__`（算法库路径）**必须替换**；`__CONSOLE_TOKEN__` 只在 `<meta name="console-token">` 一处写 token，另外 **2 处 JS 哨兵必须留占位符**（写死具体 token 之后 `register --rotate` 只能改 meta，页面会留下上一枚旧 token）。
- 漏替 `__MODULES_DEFAULT__` → 内联脚本首行 `ReferenceError`、整页按钮全失效（「开启服务」没反应）。
- 生成用 `{RULES}\tools\sync_project_page.py`（token 传空串 = 保持未登记），或从 `http://127.0.0.1:<port>/start.html` 另存；只补该占位符用 `{RULES}\tools\fill_start_placeholders.py`。
- 因为 `smoke_page.js` 会把占位符换成空串，**`node --check`/`smoke_page.js` 全绿也可能是死页**——改完必须真浏览器复核（`firefox --headless --screenshot`，标题=项目名）。
- 算法只来自 `{code_modules}`。不留课题内 `modules\`，不留长期 `config\settings.py`。
- `MODULES_DIR` 必须指向已存在的目录。空或不是目录时，console 与 `import modules` 明确报错，不回退到默认或旧路径。
- `{project}.html` 当次可覆盖 ini；写回更新 `ref/settings.ini`。无覆盖的命令行只读 ini。

## 子工程约定

- 写入 `_Docs\`须用户点名「放 _Docs」。
- 最终 / 中间 / 临时落点与备忘录查阅入口 → `My rule.md` §3；旧版稿与中间件 → §X2。
- 可复用脚本 → 统计引擎与建模 CLI 在 `{code_stats}`（`modules/` + `model-validation/`），运维/加工脚本在 `{code_stats}\tools\<fine-id>\`（壳与索引在 `{DEL}`）。长期规则/语料 → `_Docs` 相应层。
- 根不留临时/草稿/一次性中间件（例外：现行在改稿 / 现行 `Vn`）。旧版稿与中间件落点 → §X2。`_Docs\GitHub\MY-CODES\modules\`增改移须先同意。
- 数据课题根可留：`rawdata`、`derivatives`、`atlases`、索引/manifest、`ref`。`_Docs` 仅当点名「放 _Docs」。默认从 `derivatives` 拷出要用的结果，原件留在原处。最终交付与不建 `0result\` → `My rule.md` §3。禁止再建 `0script\`（→ 总图退役禁建表）。
- 同键终表合并为一张（一段说明，值列加前缀）。把原件移出子工程根须先同意。
- 移脚本或文档前先搜 `import` / `addpath` / `settings.ini` / README。仍有未改引用则不移。移完后改路径与 `_Docs` 示例再测。
- **改名 / 搬迁后的旧路径门**（与 `QC.md` R11 同方向，范围扩到项目数据件）：先扫描影响面，再定「改引用 / 留史证 / 回滚」，不允许先改目录、引用以后再说。数据件（csv / tsv / ini / py 等）当批改值，改前备份；活文档改指向，不留旧值；史证（交接单 / MOVED 台账 / changelog）可留旧值，但同句必须带标记词（`史证` / `旧布局` / `MOVED` / `已退役`）。通过标准：命中清单里只剩带标记词的史证行。
- 课题索引用 `.xlsx`，说明用 `.md`。不用 `*.tsv` 当课题索引。
- 02 整理 / 清洗 / 同步 / 抽取 → `{SKILLS}\02_data-processing\advanced\route.md`（编码 `coding.md`，抽取 `extract.md`）。表先于统计、`exc`、假分类、控制台键位与界面不在本文件展开 → 同目录 `coding.md` / `extract.md`，以及 `{SKILLS}\02_data-processing\advanced\analysis\pipeline.md`。
- **`ref/` 子目录** → 同仓 `project-ref-layout.md`；技能正文 `{SKILLS}\00_orchestrator\references\project-ref-layout.md`。

- **工程入口不用 `.bat`**：课题工程根不建、不复制入口 `.bat`；已有的移 `{DEL}` 并留台账。同步入口 `D:\MyProjects\syn.bat` 不在此列。
