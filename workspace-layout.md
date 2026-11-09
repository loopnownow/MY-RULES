---
name: workspace-layout
description: 本机布局与子工程短针。落点见 My rule.md §5。
---

# 本机布局与子工程

路径别名见 `My rule.md` §1。代码路径别名（`{code_root}`、`{code_modules}`、`{code_stats}`、`{code_data_processing}`）见 skills `lab-paths.yaml`。工作区只有一层（`D:\MyProjects\<stage>\<project>`）；不再有 A/B 双工作区。

## 一行布局

| 根 | 角色 |
|---|---|
| `D:\MyProjects\_DataBase`（`{RAW}`；旧名 00db） | 课题原始件（`<family>\<prefix_suffix>`，家族桶；家族原始件池 `<family>\_share\`（`ethics\` / `thesis\` / 原始件档））+ `_` 非课题归档分支 + `_lab` 历史档只读；除 `_index.csv`/`_diseases.csv` 外只读除非点名；细则见下节 |
| `D:\MyProjects\.Del`（`{DEL}`；旧名 **0del** / `D:\0del`） | AI 可操作临时/移出区（`_by-project` / `_by-function`）；**syn 不同步**（`/XD .Del`） |
| `D:\MyProjects\_Docs` | 语料 + 可复用代码；live tops：`_library`（含 `references` 文献全文、`lit-bank` 书目、`journals` 期刊池与选刊侧私有、`ethics\approvals` 批件、`lab-ref-ranges`、`glossary` 自有语料+四层（words/sentences/paragraphs + sections 指针页；`GLOSSARY_ROOT`）） / `templates` / `mem` / `GitHub` / `test` / `skill-harvest`（+ 根 md；`_bank` 2026-11-01 并入 `_library\glossary`，`_code` 2026-11-01 退役） |
| `D:\MyProjects\_Docs\mem` | bot 记忆导出/更新落点（城城 2026-10-25）；**仅隐私** + 可变数据 SSOT（如 find-journal JCR xlsx）；站立政策不进 mem |
| `D:\MyProjects` | 分阶段子工程工作区（阶段夹见下节） |
| `D:\MyProjects\archived` | 已完结项目冷库（`archived\<family>\<prefix_suffix>\`；L1=疾病家族短码，与 `_DataBase\<family>` 同桶；叶夹名后缀仍是基码；全称见 `_diseases.csv`）；**非**阶段夹 |
| （无活兄弟根 `R&P`） | 申请包 → `_DataBase\_grants\`；评阅他人稿 → `_DataBase\_reviews\`；`R&P` 已退役（t1813/t1815；见下「R&P 退役」） |

### 同步（t1794u / t1796u / 2026-11-08）
- `syn.bat`：`D:\MyProjects` → **`E:\Aitor`**（镜像到 Aitor **根**；**不是** `E:\Aitor\MyProjects`）。
- `/XD .Del`：不同步 `.Del`（旧 0del）；`_DataBase` 随主树同步（t1796u 取消 /XD `_DataBase`）。
- 同步入口只有 `D:\MyProjects\syn.bat`（E 侧镜像 `E:\Aitor`）；无其它同步脚本或快捷方式（2026-11-08 实测）。

### `{RAW}` = `D:\MyProjects\_DataBase`（原始库契约 · t1705u；ZIP/进库压缩 t1719u/t1800u；根更名+家族分桶 t1791u/t1825u；旧名 **00db**）

- **落点：** `D:\MyProjects\_DataBase\<family>\<prefix_suffix>\`（`<family>` 取自 `_diseases.csv` 的 `family` 列；2026-11-09 t1825u 起按家族分桶，旧 `<suffix>` 桶与扁平 `\<slug>\` 均已退役）存放该 MyProjects 子工程的**原始数据与原始影像**：DICOM 树、未压缩导出、作为源数据的原始照片、NIfTI/NII.GZ、未处理的 4D/导出包等。衍生图/表/统计仍在课题侧（见下条）。
- **子工程只留指针：** 在 `ref/settings.ini` 写 data path；**不要**把原始体拷进 `D:\MyProjects\…` 或三仓（MY-RULES / MY-SKILLS / MY-CODES）。
- **衍生件仍在课题侧：** 衍生物 / 图 / 表按本文件与 `project-ref-layout.md` 落在子工程；勿塞进 `_DataBase`。
- **临床底表 ≠ 影像 raw：** Excel/CSV 底表仍落 `ref/` 或 `ref/data/`（D-1：移动前先问）。**不要**把所有「data」都倒进 `_DataBase`。
- **现行名只写 `_DataBase`（旧名 00db）；活 `00ds` = QC 对象：** `D:\00ds` / 夹名 `00ds` 已退役。任何活路径、夹名、过滤器/默认项仍写 `00ds` 的，视为 QC 发现，**必须更正为 `_DataBase`**；**不要**在活 allowlist/filter 里把 `00ds` 留作「legacy」。changelog 里「曾用/原 `00ds`」的历史叙述可留。不另造第三个 raw 根。**更正活引用 ≠ 搬迁磁盘树**；本票（t1705u 叙述）不 bulk 迁移 `D:\00ds`；磁盘根更名见 t1791u（两边若都在，维持原状，等主人另批搬迁）。
- **禁止进 git：** 原始影像二进制**不要**进 git（含 Git LFS）或任何 GitHub remote（DICOM 头含 PHI；二进制无有效 delta）。可选轻量清单（相对路径 + 大小 + SHA-256 + 入库日）可放子工程 `ref/pipeline/`（同 `hashes.tsv` / `MANIFEST.md` 思路）。该清单若需版本，可用**无 remote 的本地 git**；备份 = 拷到另一块盘，不是 git。
- **进 `_DataBase` 多文件先压缩（t1800u；入库闸；承接 t1719u）：** 进 `D:\MyProjects\_DataBase\…`（或其 E 镜）时，若某目录内「单独文件」≥20，或明显是大量小文件堆（DICOM 序列、切片导出、逐例中间件、碎日志），先压成**一个**归档再入库；单文件或本来就少的目录不压。
  - **格式：** 优先 `7z`（`-mx=5`；固态 DICOM 可 `-m0=LZMA2`）；无 7z 用 `zip`。归档名=`<原目录名>.7z`，放在该 `prefix_suffix` 桶内；旁路留 `<名>.files.txt`（相对路径清单）。
  - **原目录：** 压缩校验通过（文件数/抽样 hash）后，原散目录移入 `D:\MyProjects\.Del`；不要两边长期并存。工作中的热数据先不压；定稿/冷存再压。
  - **例外不压：** 根上索引与表（`settings.ini`、`*.xlsx`、`console.html`、README）；已是单一大文件（`.nii.gz`、整包 `.dcm`、现成 `.7z/.zip`）；主人点名要随时打开的活数据集。
  - **单元粒度（t1719u 仍有效）：** 优先按 subject / session / modality（或一次采集单元）一档，**不要**整 slug 打成一个 mega-zip。
  - **值得 deflate：** 未压缩 DICOM 夹、未压缩 `.nii`、BMP/TIFF 栈。已压缩对象（JPEG/JPEG-LS/JPEG2000 DICOM、PNG 等）若只需容器，用 zip **store**（不二次压缩）；避免 zip-in-zip。
  - **归档后：** 不要在 `_DataBase` 或 `D:\MyProjects` 下再留第二份解压树。处理仍走 copy-on-need：需要时抽到工作区，**不要**长期解压在 archive 旁。
  - **清单：** 桶内 `<名>.files.txt` 为相对路径清单（t1800u 必留）；课题 `ref/pipeline/` 可选再记 archive（相对路径 + 大小 + SHA-256 + 入库日）。
  - 归档只是打包，**不是**加密；DICOM 头 PHI 与禁止进 git/LFS 仍适用。**不**强制密码。本条为**今后入库闸**；本票不 bulk 转换已有解压树。
  - **syn：** 压完后 `_DataBase` 仍随主树同步；`syn` 仅 `/XD .Del`（与 t1796u 一致）。
- **只读默认：** `{RAW}` 只读，除非主人点名写入。**不预建空夹**（用到再拷 / copy-on-need）。

### `{RAW}` 非课题分支与家族分桶（t1791u / t1822u / t1825u / t1829u）
`D:\MyProjects\_DataBase`（旧名 **00db**）内存三类：① 课题原始件（按后缀分桶）；② `_lab`（历史档，**只读**，不再新增；**留根**、不分桶）；③ `_` 开头的非课题归档分支（新件落这里；**留根**、不分桶）。
- **按家族分桶（t1791u → t1825u）：** 课题原始件路径为 `_DataBase\<family>\<prefix_suffix>\`（例 `SCH\lxf_RC`、`EGVB\js_CN`、`MHE\ly_SCH_HE`）。`<prefix>` = sub-PI 缩写；`<family>` = `_diseases.csv` 的 `family` 列（留空 = 该基码即家族根）；`<prefix_suffix>` 的**后缀仍是基码**（剥末尾 `_\d+` 实例；语义复合如 `SCH_HE`/`SSD_DKI` 整段保留），实例号只在叶子夹名。家族根本身必须在 `suffix` 列有行，清单一律由 `_diseases.csv` 决定，不另设 allowlist。2026-11-08 t1824u 已把存量编号桶（`SSD_1\`、`LUNG2\`、`MHE1\`、`SHE\` 等）批量归并；2026-11-09 t1825u 把 DB 与 archived 收成同名家族桶（含 `OTHERS` 兜底），`_Docs/test/structure_check.py` S23 守门。
- **同源聚合（t1829u）：** `<family>` 按**同源数据**聚合，不是按病名近义随便并。
  1. 同一影像/队列母集、同一纳排、或多篇稿共用一批 raw/底表 → 同一 `family`。
  2. 同病但非同源（独立采集 / 独立伦理 / raw 不可互指）→ 可自家族；若仅临床谱系同桶仍分叶，**文件不得跨叶混放**。
  3. 叶夹仍是 `<prefix_suffix>`。共用 raw **只存一份**：优先 `_DataBase\<family>\_share\`（或钉死的主叶）；其它课题经 `ref/settings.ini`（或 README）指针；禁止整树复制进多叶。
  4. **`_share` 家族原始件池（2026-11-09 主人裁定；取代同日试点「≥2 课题引用」建夹条件）：** 课题的原始数据 / 原始记录 / 原始图片一律进 `<family>\_share\`，不再按叶分散。固定三类：`_share\<leaf>\` 放该叶原始件压缩档（`tar.zst` 原样，**不就地解压**，解压树用完即移 `{DEL}`）；`_share\ethics\<CODE>\` 放伦理申请材料 / 原始件（**批件仍归** `_Docs\_library\ethics\approvals\`）；`_share\thesis\<slug>\` 放学位论文 / 博士后材料。`_share` 一级仅上述三类 + `目录说明.md`；其下**一层平铺**，不建 `raw\` / `cohort\` 子夹；`<family>` 根放 `目录说明.md` 记件清单 / 使用者 / PHI；搬入前先 grep 全库按路径引用；迁移记 `MOVED-*.tsv`（件数/字节/sha 校验），原叶留指针；压缩档与解压树并存时**只留档**（先验档为解压树超集再移树）。首个实例 = `_DataBase\ACN\_share\`（`人-血浆-171 - 0.7z`、`2026碳纤维部数据-- (3).xls`）；2026-11-09 全库重组后 20 个家族已建 `_share\`（伦理 48 项 + 学位论文 7 项 + 原始件档 13 个）。存量叶内 raw **不强制上收**（本轮未动）。
  5. SSOT = `_diseases.csv` 的 `family` 列（L1 桶名以此为准；`family` 留空 = 该基码即自家族）；改挂靠先改表再搬盘；`OTHERS` 仅兜底。`_share` 为保留名（下划线前缀），与 `_lab` 同类例外：`structure_check.py` S23 **已实现**桶内 `_` / `.` 前缀叶跳过叶后缀校验（2026-11-09）。
  6. **短码夹层级（2026-11-09 主人裁定）：** 短码夹位于 `_DataBase\<family>\<prefix_suffix>`（自 `_DataBase` 起总深 3）；**叶内目录 ≤3 层**，超深链条按 `<父>_<子>` 合并为单层名（实例：`DER\zyx_H`，原 8 层 / 1,188 个超深目录 → 3 层）；派生件（期刊成图 / 投稿包 / 汇报稿）不进叶内 raw，`_未标天数` 这类纯归档中间层不保留。
  7. 与 archived 同构：冷库 L1 仍跟同一 `family`；本条**不**改 accepted 收工硬留清单。
- **文档支（t1825u；2026-11-09 退役）：** 学位论文 / 标书 / 伦理申请材料不再设 `_DataBase` 顶层 `_thesis`、`_grants\_misc`、`_ethics\_misc` 三夹；改落家族池 `<family>\_share\thesis\<slug>\` 与 `<family>\_share\ethics\<CODE>\`，标书原件归 `_DataBase\_grants\<year>\`。原三夹已于 2026-11-09 解散（`_grants\_misc` 移 `{DEL}`）；遗留例外：`_grants\2025\_ethics-forms\`（申报随附伦理表）。

| 分支 | 放 | 不放 |
|---|---|---|
| `_teach\<topic-slug>\` | 教学语料（课件/病例/试题/模板）；slug 用英文小写连字符 | 课题原始影像 |
| `_ethics\<code>\` | 伦理申报包与表格原件 | 批件 PDF（实体在 `_library\ethics\approvals`，只挂指针） |
| `_med\{gcp,meeting,year-end,rules}\` | 医疗行政 | 科研数据 |
| `_books\<year>\` | 书稿/章节 | 课题原稿 |
| `_grants\<year>\` | 课题申请包（进行中与已结题；原 `R&P` 申请侧） | 本组期刊稿（走四阶段） |
| `_reviews\{peer,grants,thesis}\<year>\` | 他人稿 / 标书 / 毕业论文评阅（原 `R&P` 评阅侧） | 本组稿件（走四阶段） |
| `_personal\` | 个人材料（进修/签证） | 任何课题数据 |

- **硬规则：** 课题原始数据不得进 `_` 分支；`_` 分支不得被课题 `ref/settings.ini` 当数据源。
- **`目录说明.md`：** 每个 `_` 分支根与 `_lab` 根必须有（放什么、谁维护、更新日）。
- **`D:\MyProjects\_DataBase\_diseases.csv`（疾病短码 + 家族桶 SSOT · t1821u / t1822u / t1825u / t1829u）：** 列 `suffix,name_en,name_zh,l1,l2,aliases,family`；`suffix`=基码（无 `_\d+` 实例）；`family`=该基码所属家族根（留空=自家族；家族根必须在 `suffix` 列有本人行，如 `MHE`、`SCC`、`EC`、`THESIS`、`OTHERS`）；编号形式进 `aliases`；library `l1`/`l2` 对照 ethics/references。全称不进路径规则。
- **`D:\MyProjects\_DataBase\_index.csv`（唯一可写台账）：** 一行一个 slug/分支，列 `kind,slug,prefix,suffix,title,l1,l2,stage,owner,indexed_on,note`；新建/改名当轮更新。
- **只读不变：** 除 `_index.csv` 外 `_DataBase` 默认只读；新建分支/子夹属写盘，须当轮点名（§5.1 不豁免）。
- 不预建空夹。

**云端 / 本地：** 云端 = Grok Bot box；本地 = 城城本机。详见 `My rule.md` §1。

可选：数据课题也可在上述子工程树内自建文件夹；约定写在该子工程内，不进全局 rules/skills。

### 家族库 `_db\`（2026-11-09 主人裁定 · t1842u）

- **位置（三层）**：`_DataBase\<family>\_db\<family>db`。自 `_DataBase` 起总深 3；`_DataBase\_db\` 已退役，也不建 `<family>\_db\<short_code>\` 子夹。
- **一族一库**：同家族全部短码共用一个 `<family>db`；短码靠 `project` 表与 `doc.rel_path` 区分；家族拆分时整库随 `<family>` 走。
- **命名**：库文件 `<family>db`（无扩展名；实例 `MHEdb`）；同目录只放 `目录说明.md`（口径 / 表结构 / 查询示例 / 重建步骤 / 限制）。
- **只收表格**：xlsx / xls / csv 等可解析表格入库；压缩档（`*.tar.zst`、`7z`、`zip`）不入库、不移动，原地留叶。
- **原件留痕**：建库并校验通过后，原件移 `{DEL}\_by-function\<batch>\originals\<family>\`，写 `*-MOVED-YYYYMMDD.tsv`（相对路径 / 字节 / sha256）；原件不回流。
- **门禁**：`_db` 是 `_` 前缀桶，不参与 S23 桶/叶后缀校验；`structure_check.py` S25 校验落点与库文件（`<family>db` + `目录说明.md`、库头 SQLite、核心表齐、`_DataBase\_db` 不复活）；建库 / 迁移前后仍须全门 PASS。
- 细则（去重层级、schema、QA 清单、重建命令）→ skill `db-library`。

### 散表归并与表格入库（2026-11-09 主人裁定 · t1842u）

- **触发**：家族根 / 叶根散落表格（同项目多份、`(n)` 版本、一簿多 sheet）需要「去重 → 对齐 → 合并成一个 Excel」或「入 `_db`」时。
- **项目粒度 = 叶 slug**（家族根直放的用家族名）；合并产物 `<项目名>_merged_YYYYMMDD.xlsx` 落回该叶根 / 家族根；`_share\` 内不动。
- **去重三层**：① 文件级 sha256；② 整表级（表头 + 行哈希集合全等 = 重复；真子集 = subset，只记边、不存第二份字节）；③ 行级 / 实体级（自然键整行全等才去重；跨项目映射只人工建）。
- **对齐**：列名词典 + 表头驱动解析；**不按 mtime 判新旧**（迁移会刷新 mtime，本轮 239/258 张挤在 13 个分钟桶）；版本簇（`(n)` / `copy`）只作线索，须开表核对。
- **留痕**：原件移 `{DEL}\_by-function\<batch>\originals\<项目>\`，写 `*-MOVED-YYYYMMDD.tsv`（件数 / 字节 / sha256 100% 核验）；结果与限制写叶 / 家族 `目录说明.md` 追加段 + `_index.csv` note；批次报告 `<batch>-REPORT.md`。
- **闸**：改动前后 `structure_check.py` 全门 PASS；手工删除 / 清除须主人确认后写 `REVOKED-YYYYMMDD.tsv`，不得静默。
- 细则（三类型判定、表头驱动解析、坑位清单、合并簿 sheet 约定）→ skill `db-library`。

## 阶段夹与课题名

课题路径：`D:\MyProjects\<stage>\<project>`。

| 阶段 | 含义 |
|---|---|
| `drafting` | 选题 / 数据 / house 稿 |
| `pre-submit` | 投目标刊前打磨 |
| `reviewing` | 已投 / 在审 / 修回再投（收到审稿意见是事件，不是阶段） |
| `accepted` | 接收 / 校样 |

已有文件夹若仍用旧名，按下表阅读。**不改写**这些夹。**不新建** `DER` 阶段夹或根目录（`DER` 仅是 `_diseases.csv` 的家族码，不是阶段/工作区）。

旧阶段夹名仅作别名阅读；**勿重建** `preparing`/`polishing`/`submitting`/`reseived`。

| 旧名 | 读作 |
|---|---|
| `preparing` | `drafting` |
| `polishing` | `pre-submit` |
| `submitting` | `reviewing` |
| `in-review` | `reviewing`（历史别名；活路径只写 `reviewing`） |
| `reseived`、`received` | `accepted` |

别名表在 `{SKILLS}\00_orchestrator\templates\project-state.yaml` 的 `study_folder_stage_aliases`（路径段别名，不是 `pipeline.stage`）。

课题夹名：`lowercase_UPPERCASE`（如 `fyh_CAC`、`xlm_LG`）。旧式 `CAC_fyh`、`lung_xlm` 已退休。

**命名（2026-11-08）：** `<prefix>_<suffix>`——`<prefix>` = sub-PI 小写拼音首字母（如 `lxf`），`<suffix>` = 项目短码（大写或约定写法，如 `RC`/`CID`）。一人多题、一题多人都不改名；同后缀多例加 `_1`/`_2`（如 `llj_OV_1`）。中文人名只进台账（`_Docs\mem\people.csv`），路径与正文不写中文名。

**`archived` 不是第五阶段：** 不进上表、不进 `study_folder_stage_aliases`；见「archived 冷库」。关系总图见下「工作区关系：阶段 · 分流 · harvest · 冷库」。

## 工作区关系：阶段 · 分流 · harvest · 冷库（t1840u）

主人确认的工作区关系总图。细则清单仍见「accepted 收工」「archived 冷库」；本节约束**关系**与授权，不复写硬留字节表。

### 两层：活阶段 vs 分流落点

- **四阶段 = 活课题生命周期：** `drafting` / `pre-submit` / `reviewing` / `accepted`。路径 `D:\MyProjects\<stage>\<prefix_suffix>\`。
- **分流落点（非阶段）：** `_DataBase` / `_Docs` / `.Del` / `archived`。`archived` **不是**第五阶段（见「archived 冷库」；不进阶段表、不进 `study_folder_stage_aliases`）。

### closeout（物理落点；绑 accepted 流程结束）

**closeout = 收工搬盘**：精简活树后把字节落到分流落点。绑在 `accepted` 该稿流程结束之后；细节见下节「accepted 收工」。概要：

1. 可复用语料 / 批件 / 模板 → `_Docs`（默认 `_library`；须当轮点名「放 _Docs」）
2. raw / 不可复现图 / `R*`/`P*` 包 / 难再算中间件 → `_DataBase\<family>\<prefix_suffix>\`（≥20 散文件先压，沿用现条）
3. 可脚本重生图 / 热副本 / 过期草稿 → `.Del`
4. 硬留：终稿 Word + `FinalData_`（或钉死 data）+ 可选 `settings.ini` → `archived\<family>\<prefix_suffix>\` + `ARCHIVED.md`（四条件齐仍有效）

### harvest（抽取）≠ closeout（搬盘）

- **harvest：** 抽「怎么做」→ `_Docs\skill-harvest`；仅当主人说「进skills」才进 MY-SKILLS（extract ≠ promote；流程见 `skills.md` §3 / skill-evolution「Harvest 任务流程」）。
- **closeout：** 物理落点与精简；**不是** harvest 的替代步骤。
- **harvest 也不代替搬盘：** 抽完仍须按 closeout 把字节落到 `_DataBase` / `_Docs` / `.Del` / `archived`。
- 关系总图 / harvest 授权 →「工作区关系：阶段 · 分流 · harvest · 冷库」。harvest-skill-library 只抽「怎么做」；closeout 是落点；勿把 closeout 写成 harvest 步骤。

### harvest 授权范围

- 可在 `drafting` / `pre-submit` / `reviewing` / `accepted` / `archived` / `.Del` **任一侧**进行。
- **每次须主人当轮授权**；不因阶段自动触发。
- `archived` 默认只读：从冷库抽也要当轮点名；不解冻整夹除非另批。

### 不进 harvest / 慎进 `_Docs` 公开层

填好知情、含姓名表、未发表全文、PHI：不进 harvest；慎进 `_Docs` 公开层（与「accepted 收工」同口径）。

## accepted 收工（精简后进 archived · t1806u / t1809u / 2026-11-08）

**目标：** 按 closeout 精简 `accepted\<prefix_suffix>\`，再搬进 `archived\<family(suffix)>\<prefix_suffix>\` + `ARCHIVED.md`。accepted 不长期堆满。本条是**落点契约**（closeout）；关系与 harvest 授权见上「工作区关系：阶段 · 分流 · harvest · 冷库」。harvest ≠ closeout。

### 课题树精简后硬留
1. 终稿一份：`Manuscript_<slug>_{V|R|P}…`（旧名先问再改名；旧版→`ref/tmp/`）。根上只留这份**文件**，不要把整夹 `R*` / `P*` 留在根。
2. 复现 SSOT：`FinalData_<slug>.xlsx`（或 `ref/README` 钉死的现用 data.xlsx）。
3. 可选：`ref/settings.ini` 指到 `_DataBase\<family>\<prefix_suffix>\`（影像 raw 不进课题树）。

### R*/P* 整夹进 `_DataBase`（修订包 / 投稿包 · t1809u）
课题树内名为 `R*` / `P*` 的夹（修订包、投稿包，如 R1/R2/P1/P1.1）收工时**整夹**进 `_DataBase\<family>\<prefix_suffix>\`。若夹内单独文件 ≥20 或明显小文件堆，先 7z/zip + `.files.txt`（见上节「进 `_DataBase` 多文件先压缩」）。校验通过后，原夹移 `D:\MyProjects\.Del\_by-project\<slug>\`。根上终稿仍只留一份现行 `Manuscript_*_{V|R|P}…`**文件**（不是把整夹留在根）。

### `_DataBase` 可收
（≥20 散文件或小文件堆先 7z/zip + `.files.txt`，校验后散目录→`.Del`；见上节「进 `_DataBase` 多文件先压缩」。）
- 课题树 `R*` / `P*` 整夹（修订包 / 投稿包；见上节 t1809u）
- raw 影像/数据
- 不可复现资料图
- 去重合并底表 `MergedTables_*.xlsx`、纳排日志（非 FinalData）
- 难再算中间产物（手工 ROI/掩膜、半自动分割、radiomics 大表、外验导出、第三方一次性结果）
- 影像旁路元数据（DICOM 头汇总、序列清单、质控截图栈、扫描仪参数快照；整库登记仍可在 `_Docs\_library\scanner-registry`）
- 不可再采过程件（知情扫描、纸质 CRF 扫描、科教科/财务回执扫描、唯一仪器打印；PHI 敏感不进 skill 正文）
- 可选投稿锁定包（终版图+表压缩包）
- 外部数据快照（公开库某日下载、合作方移交盘、不可再拉 API dump）

**不进 DB：** 终稿 Word、glossary/期刊池/文献全文、可脚本重生图、热分析工作副本。

### `_Docs` 分桶
须当轮点名「放 _Docs」才写；默认禁 mkdir，`mem` 例外（§5.1）。
- `templates\`：空白伦理/SCI骨架/清单/金样/brand
- `_library\ethics\approvals\`：已批批件 PDF+索引
- `_library\references\`：文献全文；课题 `ref/refer` 只 DOI 指针
- `_library\lit-bank` / `journals\`：书目、期刊池、投稿 prior
- `skill-harvest\`：可复用写法/方法句（「进skills」再进 MY-SKILLS）
- `mem\`：people.csv、JCR 可变、证件/签名（不进 skill 正文）

填好知情、含姓名表、未发表全文不进 harvest；慎进 `_Docs` 公开层。

### 图分流
可复现图 → `.Del\_by-project\<slug>\`；不可复现 → `_DataBase`。

### 其它
- 其它 csv/xlsx：去重合并→DB；移删先问（D-1）。
- 脚本：一次性留指针；可复用提案 MY-CODES。
- THESIS/行政（伦理·科教科·财务）与单篇 SCI 分轨。
- 四条件齐再 archived（含 skill_ref 或 none）；更新 `_DataBase\_index.csv`、`mem\people.csv`（见「archived 冷库」）。
- syn：`D:\MyProjects`→`E:\Aitor` 仅 `/XD .Del`。
- 关系总图 / harvest 授权 →「工作区关系：阶段 · 分流 · harvest · 冷库」。harvest-skill-library 只抽「怎么做」；closeout 是落点；勿把 closeout 写成 harvest 步骤。

## archived 冷库（非阶段；2026-11-08；t1821u / t1822u / t1825u / t1829u）

`D:\MyProjects\archived` 放**已完结**项目：`D:\MyProjects\archived\<family>\<prefix_suffix>\`（L1=`<family>` **家族根**短码；`<family>` 取自 `_diseases.csv` 的 `family` 列，与 `_DataBase\<family>\<prefix_suffix>\` 同桶；第二层 = 完整课题夹名）。不按年份分层。

- **L1 = 家族根（t1825u / t1829u）：** 冷库按疾病家族/文档类型分桶，桶名 = `_diseases.csv` 的 `family` 列（留空 = 自家族，即基码本身；挂靠按同源聚合，见上文「同源聚合」）。例：`archived\EGVB\js_CN`、`archived\MHE\ly_SCH_HE`、`archived\OTHERS\lxj_BMP6`。
- **叶夹名后缀 = 病种基码（t1822u 不变）：** `archived\<family>\<prefix>_<suffix>[_<n>]\`；`<suffix>` 仍是基码（去末尾 `_\d+`；`SSD_DKI`、`SCH_HE` 等语义复合整段保留），实例号只留在叶子夹名（例 `archived\CC\fyh_CAC_1\`）。
- **两树同构（t1825u）：** `_DataBase` 与 `archived` 都用同一个 `<family>` 桶；靠 `_diseases.csv` 的 `suffix`/`family` 对应，S23 同时校验两树桶名与叶后缀。家族池 `_share\` 与 `_lab` 仅存在于 `_DataBase`，冷库不设。
- **疾病短码 SSOT：** `_DataBase\_diseases.csv`（UTF-8；列 `suffix,name_en,name_zh,l1,l2,aliases,family`）。`suffix` = 基码；`family` = 家族根（留空 = 自家族）；编号形式进 `aliases`（如 `SSD_1`）。中英文全称**只**进本表（及 `_index.csv` 可抄空值）；路径规则不写长病名。
- **ethics / references** 仍用 library L1/L2（`library-taxonomy.md`）；靠 `_diseases.csv` 的 `suffix`↔`l1`/`l2` 对照，不另造路径层。

- **进场（四条全满足）：** ① 在 `accepted` 且该稿流程结束（接收/校样完成）；② skill 已提取或已按 `skills.md` §3 提案（`skill-harvest` 有记录，无则记 `none`）；③ rule 候选已提交（无则记 `none`）；④ `_DataBase\_index.csv` 行与 `_Docs\mem\people.csv` 行已更新。
- **历史旧论文（如 `000-vip\科研\文章`）：** 先进 `accepted`，按 `<prefix>_<suffix>` 建项目；抽取（skill/rule/_DataBase/_Docs）完成后再按上条进冷库。**先 accepted，后 archived**，不直进冷库。
- **`ARCHIVED.md`（每个项目根一份）：** `archived_on`、`from_stage`、`slug`、`family`、`skill_ref`、`rule_ref`、`index_row`、`note`；缺项不进。
- **非阶段：** 不进阶段表、不进 `study_folder_stage_aliases`；`project-state.yaml` 的 `stage` 保持 `accepted`（不加 `archived` 枚举，避免 MY-SKILLS PR）。
- **与 QC 禁令消歧：** `My rule.md` §4 与 `skills.md` §6 的 skip/archived 禁令只约束**技能树/文档 QC**，**不适用**项目冷库；冷库 = 已完成，不是未处理。
- **只读默认：** 冷库不参与日常检索/改写；解冻 = 移回对应阶段夹 + 移除 `ARCHIVED.md`（须当轮点名）。
- **命名：** `name_zh → prefix` 进 `D:\MyProjects\_Docs\mem\people.csv`（`/mem/` 已 gitignore、_Docs 仓无 remote）。
- 不预建空夹；同一 `<prefix_suffix>` 不重复。

## R&P 退役（t1813 / t1815 / t1817u）

活兄弟根 `D:\MyProjects\R&P`（formerly `proposal`）**已退役**：磁盘 stub 已移 `.Del`（t1815）；勿重建。材料落点改为：
- **课题申请包** → `_DataBase\_grants\<year>\`
- **评阅他人稿**（peer / grants / thesis）→ `_DataBase\_reviews\{peer,grants,thesis}\<year>\`

二者**不是**稿件流水线阶段：不要写入上方 `drafting` / `pre-submit` / `reviewing` / `accepted` 阶段表，也不进 `study_folder_stage_aliases`。本组期刊草稿 / R&R / 校样仍走四阶段夹。历史叙述可写「was / formerly proposal / R&P」。

## 文件落点

交付表权威 → `My rule.md` §5。`ref/` 子目录 → 同仓 `project-ref-layout.md`。

| 种类 | 落点 |
|---|---|
| 草稿 / 旧稿 / 一次性脚本 | 子工程内临时/中间/旧版稿 → `ref/tmp/`（非默认 `{DEL}`；t1450u）。跨课题或无子工程一次性 → `{DEL}` 的 `_by-project\` / `_by-function\`。`{DEL}` 定期清空，值得长期保留的不放这里。细则 → `My rule.md` §5 / `project-ref-layout.md`。 |
| 共享统计库 | `{code_modules}`（`D:\MyProjects\_Docs\GitHub\MY-CODES\modules`）。入口：`PYTHONPATH={code_stats}` 后 `python -m modules.pipeline`。课题只指向该树，不在课题内再放 `modules\`。未点名则不改该库。技能正文（怎么用、按什么规则）在 `{SKILLS}\02_data-processing\`；本仓只管代码。 |
| 02 运维（整理 / 清洗 / 同步） | `D:\MyProjects\_Docs\GitHub\MY-CODES\tools\`（`{code_stats}` + `tools/<fine-id>/`；席位夹名不镜像 `02-…`/`03-…`）。统计引擎与建模 CLI 在 `D:\MyProjects\_Docs\GitHub\MY-CODES`（2026-10-25 起独立主库；2026-11-01 由 `stats-analysis` 更名）。 |
| 参考包 / 锁定笔记 | 课题 `ref/`。运行键只在 `ref/settings.ini`。可选 `ref/project-state.yaml` 只记设计与稿件进度。 |
| 文献全文（PDF/HTML） | `D:\MyProjects\_Docs\_library\references\<L1>\<L2>\`（一文一文件，名用 DOI；t1455u）；子工程 `ref/refer\` 只写 `DOI_*.md` 指针；书目进 `_library\lit-bank`（不存 PDF） |
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

- 写入 `_Docs\`（旧名 **0doc**）须用户点名「放 0doc」/「放 _Docs」。
- **最终**→子工程根；**中间**→`ref/` 地图；**无** `0result\`；子工程内临时 → `ref/tmp/`（非默认 `{DEL}`）；无子工程/跨课题临时进 `{DEL}`；Downloads 仅当点名。权威 → `My rule.md` §5。
- 可复用脚本 → 统计引擎与建模 CLI 在 `{code_stats}`（`modules/` + `model-validation/`），运维/加工脚本在 `{code_stats}\tools\<fine-id>\`（`_code` 已于 2026-11-01 整层退役：脚本在 MY-CODES，壳与索引移至 {DEL}）。`0script\` 已退休，不在课题根重建。长期规则/语料 → `_Docs` 相应层。
- 根不留临时/草稿/一次性中间件（例外：现行在改稿 / 现行 `Vn`）。旧版稿与中间件进 `ref/tmp/`，不进 `{DEL}`（除非过后清理先问）。`_Docs\GitHub\MY-CODES\modules\`（旧盘符叫法 `0doc\GitHub\...`）增改移须先同意。
- 数据课题根可留：`rawdata`、`derivatives`、`atlases`、索引/manifest、`ref`。`_Docs` 仅当点名「放 0doc」/「放 _Docs」。默认从 `derivatives` 拷出要用的结果，原件留在原处；终稿落子工程根。不建 `0result\`，不重建 `0script\`。
- 同键终表合并为一张（一段说明，值列加前缀）。把原件移出子工程根须先同意。
- 移脚本或文档前先搜 `import` / `addpath` / `settings.ini` / README。仍有未改引用则不移。移完后改路径与 `_Docs` 示例再测。
- 课题索引用 `.xlsx`，说明用 `.md`。不用 `*.tsv` 当课题索引。
- 02 整理 / 清洗 / 同步 / 抽取 → `{SKILLS}\02_data-processing\advanced\route.md`（编码 `coding.md`，抽取 `extract.md`）。表先于统计、`exc`、假分类、控制台键位与界面不在本文件展开 → 同目录 `coding.md` / `extract.md`，以及 `{SKILLS}\02_data-processing\advanced\analysis\pipeline.md`。
- **`ref/` 子目录** → 同仓 `project-ref-layout.md`；技能正文 `{SKILLS}\00_orchestrator\references\project-ref-layout.md`。

## 新建文件夹 / 新建文件

只许建在 `{DEL}` / `D:\MyProjects\.Del\` 的 `_by-project\`、`_by-function\`。权威与例外 → `My rule.md` §5.1（含 `_Docs`（旧名 0doc）默认禁止 mkdir、**改已有文件须当轮点名或先问**（§2 总闸 t1672u）、一次性脚本不进主目录 / `.grok\tmp` / 课题根）。本段不复写。bot mem 落点例外（`D:\MyProjects\_Docs\mem\`）→ `My rule.md` §1 + §5.1。

**目录命名（t1458u）**：`_Docs` 下目录一律 ASCII 英文（`approvals` / `journals` / `jcr`）；中文目录发现即当轮 rename，并在 `_library\MOVED-FROM.md` 记一行。库分类与 L1/L2 → `library-taxonomy.md`。

**`.Del` 内部三档**（旧名 0del）（park / harvest-park / harvested，原 junk）与落 harvested 前的 grep 要求 → `My rule.md` §5.3。
