---
name: workspace-layout
description: 本机布局与子工程短针。落点见 My rule.md §3。
---

# 本机布局与子工程

路径别名见 `My rule.md` §4。代码路径别名（`{code_root}`、`{code_modules}`、`{code_stats}`、`{code_data_processing}`）见 skills `lab-paths.yaml`。工作区只有一层（`D:\MyProjects\<stage>\<project>`）；不再有 A/B 双工作区。

## 一行布局

| 根 | 角色 |
|---|---|
| `D:\MyProjects\_DataBase`（`{RAW}`） | 课题原始件（`<family>\<prefix_suffix>`，家族桶；身份桶 `<family>\_PHI\`、原始件池 `<family>\__zip\`、学位桶 `<family>\_thesis\`）+ `_` 非课题归档分支 + `_lab` 历史档只读；除 `_index.csv`/`_diseases.csv` 外只读除非点名；细则见下节 |
| `D:\MyProjects\.Del`（`{DEL}`） | AI 可操作临时/移出区（`_by-project` / `_by-function`）；**syn 不同步**（`/XD .Del`） |
| `D:\MyProjects\_Docs` | 语料 + 可复用代码；live tops：`_library`（含 `references` 文献全文、`lit-bank` 书目、`journals` 期刊池与选刊侧私有、`ethics\approvals` 批件、`lab-ref-ranges`、`glossary` 自有语料+四层（words/sentences/paragraphs + sections 指针页；`GLOSSARY_ROOT`）） / `templates` / `mem` / `GitHub` / `test` / `harvest` / `harvest-sources-park`（已瘦身：方法原文 6 件 + 入口散件；抢救文本已退役）（+ 根 md；`_bank` 已并入 `_library\glossary`，`_code` 已退役） |
| `D:\MyProjects\_Docs\mem` | bot 记忆导出/更新落点（城城）；**仅隐私** + 可变数据 SSOT（如 find-journal JCR xlsx）；站立政策不进 mem；查阅授权 → `My rule.md` §2 |
| `D:\MyProjects` | 分阶段子工程工作区（阶段夹见下节） |
| `D:\MyProjects\archived` | 已完结项目冷库（`archived\<family>\<prefix_suffix>\`；L1=疾病家族短码，与 `_DataBase\<family>` 同桶；叶夹名后缀仍是基码；全称见 `_diseases.csv`）；**非**阶段夹 |
| （无活兄弟根 `R&P`） | 申请包 → `_DataBase\_grants\`；评阅他人稿 → `_DataBase\_reviews\`；`R&P` 已退役 |

### 同步
- `syn.bat`：`D:\MyProjects` → **`E:\Aitor`**（镜像到 Aitor **根**；**不是** `E:\Aitor\MyProjects`）。
- `/XD .Del`：不同步 `.Del`；`_DataBase` 随主树同步。
- 同步入口只有 `D:\MyProjects\syn.bat`（E 侧镜像 `E:\Aitor`）；无其它同步脚本或快捷方式。

### `{RAW}` = `D:\MyProjects\_DataBase`

- **落点：** `D:\MyProjects\_DataBase\<family>\<prefix_suffix>\`（`<family>` 取自 `_diseases.csv` 的 `family` 列；按家族分桶）存放该 MyProjects 子工程的**原始数据与原始影像**：DICOM 树、未压缩导出、作为源数据的原始照片、NIfTI/NII.GZ、未处理的 4D/导出包等。衍生图/表/统计仍在课题侧（见下条）。
- **子工程只留指针：** 在 `ref/settings.ini` 写 data path；**不要**把原始体拷进 `D:\MyProjects\…` 或三仓（MY-RULES / MY-SKILLS / MY-CODES）。
- **衍生件仍在课题侧：** 衍生物 / 图 / 表按本文件与 `project-ref-layout.md` 落在子工程；勿塞进 `_DataBase`。
- **临床底表 ≠ 影像 raw：** Excel/CSV 底表仍落 `ref/` 或 `ref/data/`（D-1：移动前先问）。**不要**把所有「data」都倒进 `_DataBase`。
- **现行名只写 `_DataBase`；活 `00ds` = QC 对象：** `D:\00ds` / 夹名 `00ds` 已退役。
  - 任何活路径、夹名、过滤器 / 默认项仍写 `00ds` 的，视为 QC 发现，**必须更正为 `_DataBase`**；**不要**在活 allowlist / filter 里把 `00ds` 留作「legacy」。
  - 不另造第三个 raw 根。**更正活引用 ≠ 搬迁磁盘树**：不 bulk 迁移旧根；两边若都在，维持原状，等主人另批搬迁。
- **禁止进 git：** 原始影像二进制**不要**进 git（含 Git LFS）或任何 GitHub remote（DICOM 头含 PHI；二进制无有效 delta）。可选轻量清单（相对路径 + 大小 + SHA-256 + 入库日）可放子工程 `ref/pipeline/`（同 `hashes.tsv` / `MANIFEST.md` 思路）。该清单若需版本，可用**无 remote 的本地 git**；备份 = 拷到另一块盘，不是 git。
- **进 `_DataBase` 多文件先压缩：** 进 `D:\MyProjects\_DataBase\…`（或其 E 镜）时，若某目录内「单独文件」≥20，或明显是大量小文件堆（DICOM 序列、切片导出、逐例中间件、碎日志），先压成**一个**归档再入库；单文件或本来就少的目录不压。
  - **格式与落点：** 优先 `7z`（`-mx=5`；固态 DICOM 可 `-m0=LZMA2`）；无 7z 用 `zip`。归档名=`<原目录名>.7z`，**唯一落点 = `<family>\__zip\<leaf>\`**（叶内与家族根禁归档，见「`__zip` 原始件池」）；`<名>.files.txt`（相对路径清单）**随档同放** `__zip\<leaf>\`。
  - **原目录：** 压缩校验通过（文件数/抽样 hash）后，原散目录移入 `D:\MyProjects\.Del`；不要两边长期并存。工作中的热数据先不压；定稿/冷存再压。
  - **例外不压：** 根上索引与表（`settings.ini`、`*.xlsx`、`console.html`、README）；已是单一大文件（`.nii.gz`、整包 `.dcm`、现成 `.7z/.zip`）；主人点名要随时打开的活数据集。
  - **单元粒度：** 优先按 subject / session / modality（或一次采集单元）一档，**不要**整 slug 打成一个 mega-zip。
  - **值得 deflate：** 未压缩 DICOM 夹、未压缩 `.nii`、BMP/TIFF 栈。已压缩对象（JPEG/JPEG-LS/JPEG2000 DICOM、PNG 等）若只需容器，用 zip **store**（不二次压缩）；避免 zip-in-zip。
  - **归档后：** 不要在 `_DataBase` 或 `D:\MyProjects` 下再留第二份解压树。处理仍走 copy-on-need：需要时抽到工作区，**不要**长期解压在 archive 旁。
  - **清单：** `__zip\<leaf>\` 内 `<名>.files.txt` 为相对路径清单，随档同放；课题 `ref/pipeline/` 可选再记 archive（相对路径 + 大小 + SHA-256 + 入库日）。
  - 归档只是打包，**不是**加密；DICOM 头 PHI 与禁止进 git/LFS 仍适用。**不**强制密码。本条为**今后入库闸**；本票不 bulk 转换已有解压树。
  - **syn：** 压完后 `_DataBase` 仍随主树同步；`syn` 仅 `/XD .Del`。
- **单档 ≤1 GiB / 分卷：** 进 `{RAW}`、交付或归档打包时，**单个文件 ≤1 GiB（1,073,741,824 B）**；预计超限就**先分卷**，不要造出大档再拆。
  - **分卷：** 命名 `<原名>.001/.002/…`（900 MiB = 943,718,400 B 字节卷，末卷可小）；`split -b 943718400 -d -a 3 --numeric-suffixes=1 <档> <档>.`；同夹写 `分卷说明.md`（拆自档 + 原字节 + 原 sha256 + 卷表 + 还原/校验命令）。
  - **还原：** Windows `copy /b a.001+a.002+a.003 a`；Linux/macOS `cat a.0* > "a"`；拼接后 sha256 须等于记录值，再 `zstd -t` / `unzip -t` / `7z t` 验档。
  - **存量超限：** 已入库的 >1 GiB 单档同法拆分；拼接逐字节校验通过后原档才移 `{DEL}`（禁删）+ 台账（原路径 / 字节 / sha256 / 卷数）。
  - **例外：** `{DEL}` 下临时件、正在写/正在压的在途中间件不拆；归档预计超 1 GiB 时按本条**入库即分卷**（与压缩闸叠加：先压一个归档，超限再分卷）。**不** bulk 重拆 `{DEL}` 历史件。
- **只读默认：** `{RAW}` 只读，除非主人点名写入。**不预建空夹**（用到再拷 / copy-on-need）。

### 数据角色与单向流（抽象，不改本机盘符）

四个角色单向流转、不回写。本机落点仍按上文 `{RAW}` 与阶段工程根；不把外机盘符写进本仓。

| 角色 | 放什么 | 不放什么 |
|---|---|---|
| 原始影像 | 原始 DICOM；由 DICOM 转出的 NIfTI **视同原始件**（不算处理后图像） | 定位像 / 二次重建、处理后图像、流水线中间件、文本、代码；同一病例 DICOM 与 nii 不得双留 |
| 处理后 | 处理后图像（ROI 外扩、掩膜、配准后、生境掩膜）与流水线 `01–03` / checkpoints / 模型 | 原始影像、整理后的文本（表 / 文档 / 结果 `04–06` / 代码） |
| 归档 | 整理后的文本、数据表、`ref\`、结果 `04–06`、代码仓 | 原始影像、处理后图像、`01–03` 大件 |
| 备份 | 归档侧的单向镜像（排除隔离区） | 把备份当工作盘或数据源，或在备份盘上直接改稿 |

- 转换完成后：nii 留在原始影像侧，原 DICOM 同批移 `{DEL}` 并留台账，不双留。
- 派生图只许新增，禁止覆盖源 seg（输出路径等于输入路径即中止）；写原始盘先 `--dry-run`，经主人点头再执行。

### `{RAW}` 非课题分支与家族分桶
`D:\MyProjects\_DataBase`内存三类：① 课题原始件（按家族分桶）；② `_lab`；③ `_` 开头的非课题归档分支（新件落这里；**留根**、不分桶）。
- **按家族分桶：** 课题原始件路径为 `_DataBase\<family>\<prefix_suffix>\`（例 `SCH\lxf_RC`、`EGVB\js_CN`、`MHE\ly_SCH_HE`）。
  - `<prefix>` = sub-PI 缩写；`<family>` = `_diseases.csv` 的 `family` 列（留空 = 该基码即家族根）。
  - `<prefix_suffix>` 的**后缀仍是基码**（剥末尾 `_\d+` 实例；语义复合如 `SCH_HE` / `SSD_DKI` 整段保留），实例号只在叶子夹名。
  - 家族根本身必须在 `suffix` 列有行，清单一律由 `_diseases.csv` 决定，不另设 allowlist。
  - 存量编号桶（`SSD_1\`、`LUNG2\`、`MHE1\`、`SHE\` 等）已批量归并为家族桶；DB 与 archived 用同名家族桶（含 `OTHERS` 兜底），`_Docs/test/structure_check.py` S23 守门。
- **同源聚合：** `<family>` 按**同源数据**聚合，不是按病名近义随便并。
  1. 同一影像/队列母集、同一纳排、或多篇稿共用一批 raw/底表 → 同一 `family`。
  2. 同病但非同源（独立采集 / 独立伦理 / raw 不可互指）→ 可自家族；若仅临床谱系同桶仍分叶，**文件不得跨叶混放**。
  3. 叶夹仍是 `<prefix_suffix>`。共用 raw **只存一份**：优先 `_DataBase\<family>\__zip\`（或钉死的主叶）；其它课题经 `ref/settings.ini`（或 README）指针；禁止整树复制进多叶。
  4. **`__zip` 原始件池：** 课题的原始数据 / 原始记录 / 原始图片一律进 `<family>\__zip\`，不再按叶分散。
     - **各类固定**（自各桶起 ≤2 层，D1 最终口径）：`__zip\<leaf>\<文件>` 放该叶原始件压缩档（`tar.zst` 原样，**不就地解压**，解压树用完即移 `{DEL}`）；`_thesis\<slug>__<文件>` 放学位论文 / 博士后材料。
     - **一级结构：** 仅上述三桶（`_PHI` / `__zip` / `_thesis`）+ `目录说明.md`（`__zip` 存在必须自带 `__zip\目录说明.md`；无叶家族例外 `__zip\<family>\` 直放，须在家族 `目录说明.md` 登记）；其下**一层平铺**，不建 `raw\` / `cohort\` 子夹。
     - **家族根：** `<family>` 根放 `目录说明.md` 记件清单 / 使用者 / PHI；搬入前先 grep 全库按路径引用；迁移记 `MOVED-*.tsv`（件数 / 字节 / sha 校验），原叶留指针；压缩档与解压树并存时**只留档**（先验档为解压树超集再移树）。
     - **唯一落点与层级：** `__zip` 为压缩档唯一落点（收的是原始件压缩档；档内表格按「家族库 `_PHI\`」条解出入库，原档仍留 `__zip`），叶内与家族根不得留任何归档；`__zip` 下文件层级 ≤2（`__zip\<类>\<文件>`），不再加中间夹。
     - **存量：** 首个实例 = `_DataBase\ACN\__zip\`（`人-血浆-171 - 0.7z`、`2026碳纤维部数据-- (3).xls`）；20 个家族已建 `__zip\`（伦理 48 项 + 学位论文 7 项 + 原始件档 13 个）。叶内非表格 raw 按一级目录 / loose 单元压 `<PREFIX>__<leaf>__<unit>-raw-<YYYY-MM-DD>.tar.zst` 上收 `__zip\<leaf>\`（不整叶 mega-zip）；原件移 `{DEL}\_by-function\<batch>\originals\<code>\<family>\<leaf>\`，写 tsv（相对路径 / 字节 / sha256），叶 `目录说明.md` 记「raw→档」映射。
  5. SSOT = `_diseases.csv` 的 `family` 列（L1 桶名以此为准；`family` 留空 = 该基码即自家族）；改挂靠先改表再搬盘；`OTHERS` 仅兜底。`_PHI` / `__zip` / `_thesis` 为保留名（下划线前缀），与 `_lab` 同类例外：`structure_check.py` S23 **已实现**桶内 `_` / `.` 前缀叶跳过叶后缀校验。
  6. **短码夹层级：** 短码夹位于 `_DataBase\<family>\<prefix_suffix>`（自 `_DataBase` 起总深 3）；**叶内目录 ≤3 层**，超深链条按 `<父>_<子>` 合并为单层名（实例：`DER\zyx_H`，原 8 层 / 1,188 个超深目录 → 3 层）；派生件（期刊成图 / 投稿包 / 汇报稿）不进叶内 raw，`_未标天数` 这类纯归档中间层不保留；表格入库后叶内只留 `目录说明.md`（见「家族库 `_PHI\`」）。
  7. 与 archived 同构：冷库 L1 仍跟同一 `family`；本条**不**改 accepted 收工硬留清单。
- **文档支：** 学位论文 / 标书 / 伦理申请材料不建 `_DataBase` 顶层 `_thesis`、`_grants\_misc`、`_ethics\_misc` 三夹；改落家族池 `<family>\_thesis\<slug>__<文件>`，标书原件归 `_DataBase\_grants\<year>\`；伦理申请材料不进 `_DataBase`，按「伦理材料留存」归 `_Docs\_library\ethics\`。原三夹已解散（`_grants\_misc` 移 `{DEL}`）；遗留例外：`_grants\2025\_ethics-forms\` 不重建（申报随附伦理表，随清理批次移 `{DEL}`）。


### 伦理材料留存

伦理材料落点 = `_Docs\_library\ethics\`（申请包 / 方案 → `sections\protocol`，知情同意 → `sections\icf`，写作模式提取物 → `extract\briefs` / `extract\phrases`，批件 PDF → `approvals\<L1>\<L2>\`）。`_DataBase` 侧不设伦理夹：抽完写作模式即退役，剩余件按 harvest 流程走 `harvest-park` → `harvested`。本条定**留存口径**；盘面大搬由 Bai 执行，本票（Rules encode）**不**搬盘。

1. **批件原件**：仅保留**日期 ≥ 2023-11-10** 的进 `_Docs\_library\ethics\approvals\<L1>\<L2>\`，并在 `approvals-index.xlsx` 登记。日期取批件批准日 / 文件标注日（能确定者）；**早于 2023-11-10** 的批件原件 → `{DEL}`。分类口径见 `library-taxonomy.md` §3，本条不另造 approvals 路径。
2. **临床研究方案 + 知情同意书**：**全部保留**，方案 → `_Docs\_library\ethics\sections\protocol\`，知情同意 → `sections\icf\`，**无**日期下限；文件名保留 `<CODE>__` 前缀便于回溯。
3. **`_DataBase\_lab\ethics` 废弃**：该树不再作为活伦理落点；内容进 `.Del`（搬迁由 Bai 执行）。`_lab` 根其它历史档只读口径不变，唯 ethics 子树按本条退役。

挂靠：短码 ↔ 家族靠 `_diseases.csv`；ethics/references 的 library L1/L2 对照不变。

| 分支 | 放 | 不放 |
|---|---|---|
| `_teach\<topic-slug>\` | 教学语料（课件/病例/试题/模板）；slug 用英文小写连字符 | 课题原始影像 |
| `_med\{gcp,meeting,year-end,rules}\` | 医疗行政 | 科研数据 |
| `_books\<year>\` | 书稿/章节 | 课题原稿 |
| `_grants\<year>\` | 课题申请包（进行中与已结题；原 `R&P` 申请侧） | 本组期刊稿（走四阶段） |
| `_reviews\{peer,grants,thesis}\<year>\` | 他人稿 / 标书 / 毕业论文评阅（原 `R&P` 评阅侧） | 本组稿件（走四阶段） |
| `_personal\` | 个人材料（进修/签证） | 任何课题数据 |

- **硬规则：** 课题原始数据不得进 `_` 分支；`_` 分支不得被课题 `ref/settings.ini` 当数据源。
- **`目录说明.md`：** 每个 `_` 分支根与 `_lab` 根必须有（放什么、谁维护、更新日）；它是**活文档**——正文里作现行指令的路径与计数须与实盘一致，史证须同句带标记词，搬件 / 改名 / 计数变化当轮同步（门 → `QC.md` R11）。
- **`D:\MyProjects\_DataBase\_diseases.csv`：** 列 `suffix,name_en,name_zh,l1,l2,aliases,family`；`suffix`=基码（无 `_\d+` 实例）；`family`=该基码所属家族根（留空=自家族；家族根必须在 `suffix` 列有本人行，如 `MHE`、`SCC`、`EC`、`THESIS`、`OTHERS`）；编号形式进 `aliases`；library `l1`/`l2` 对照 ethics/references。全称不进路径规则。`_diseases.csv` 复核：`RI` 挂 `SCH`（IR 数据随 SCH 队列）；`SCH\ly_RI` 只留 `目录说明.md` 为最终态（archived 同挂 SCH 口径）。
- **`D:\MyProjects\_DataBase\_index.csv`（唯一可写台账）：** 一行一个 slug/分支，列 `kind,slug,prefix,suffix,title,l1,l2,stage,owner,indexed_on,note`；新建/改名当轮更新。
- **只读不变：** 除 `_index.csv` 外 `_DataBase` 默认只读；新建分支/子夹属写盘，须当轮点名（`My rule.md` §2 不豁免）。
- 不预建空夹。

**云端 / 本地：** 云端 = Grok Bot box；本地 = 城城本机。详见 `My rule.md` §0。

可选：数据课题也可在上述子工程树内自建文件夹；约定写在该子工程内，不进全局 rules/skills。

### 家族桶三类落点（`_PHI` / `__zip` / `_thesis`）

- **一句话**：一个家族 = 身份桶 `_PHI\` + 原始件池 `__zip\` + 学位桶 `_thesis\` + 每个子工程叶内一个子库 `<slug>db`；三桶与叶同在 `<family>\` 下，自 `_DataBase` 起总深 3。
- **`<family>\_PHI\`（唯一 PHI 落点）**：放家族库 `<family>db`（`meta` / `id` / `id_number` / `dict` / `ref_project` 五表 = 身份与各类号、变量词典、子库登记）、冻结旧库 `<family>db_6t`、`目录说明.md`、可重建预览页；**不存业务表**。整桶不得外发、不得进任何仓、不得压包外送；外发只走子库（D28 零 PHI 通过后）。
- **`<family>\__zip\`（原始件池）**：按子工程分夹 `<family>\__zip\<leaf>\`，放该叶原始件压缩档与随档清单 `<名>.files.txt`；随档非表格件（原始图 / 扫描记录 / 说明）同夹一层平铺，不建 `raw\` / `cohort\` 子夹。档内表格解出按「散表归并」入库，原档留本桶；桶根须自带 `目录说明.md`。
- **伦理材料不进 `_DataBase`**：申请包 / 方案 / 知情同意 / 批件按「伦理材料留存」归 `_Docs\_library\ethics\`；写作模式抽完后 `_DataBase` 侧不留伦理原件，剩余件随 harvest 进 `{DEL}`，本树不设伦理桶。
- **`<family>\_thesis\<slug>\`**：学位论文 / 博士后 / 汇报稿原件。
- **越界即 P1**：库文件出现在 `__zip` / `_thesis` 或叶根散落归档；PHI 出现在 `_PHI` 以外的落点；`_PHI` 里的家族库出现 `clin` / `qc` / `_modules_<mod>` 业务表。
- **写侧只认本节桶名**：不设兼容分支、不按别名兜底。旧桶名与旧表前缀出现在盘面或库内即 **P1 QC 发现**，按清理对象处理；`aliases.yaml` 的映射只用于识别与清理，不是读侧开关。
- **迁移先试点一个家族**：首批 `ACN`（压缩档与非归档件同时在册、`src` 表路径耦合最多）。单家族搬完 → 重写库内字面路径 → 复算 `src.sha256` → `gates.py <family> --cutover` 与 `align_check.py` 全 PASS → 台账登记（`family` / 桶 / 完成日 / 门禁结果 / 回滚点）→ 再按家族铺开；试点未过不批量搬。
- **库内路径随桶改名同批改**：`src.rel_path`（`blob:<family>/<桶>/…`）、`meta.source_db`、`meta.excluded_columns.source_sheet` 存的是字面路径，改名后须同批重写并复算 `src.sha256`；只搬目录不改这些值 = 悬挂引用（P0）。

### 家族库 `_PHI\\` 与子工程库（1+N）

- **位置（1+N，三层）**：家族库 `_DataBase\\<family>\\_PHI\\<family>db`；子工程库 `_DataBase\\<family>\\<slug>\\<slug>db`（**扁平**，不建 `<slug>\\_PHI\\` 或 `<family>\\_PHI\\<short_code>\\` 子夹）。自 `_DataBase` 起两者总深 3；根级 `_DataBase` 下不设库桶。
- **目录内容**：`_PHI` 内放家族库 `<family>db`、并存期冻结旧库 `<family>db_6t`、`目录说明.md`，以及常驻、可重建的预览页；子工程叶内放 `<slug>db`、`目录说明.md`，同样允许可重建预览页。两处都不建 `raw\\` / `originals\\` / 日期子夹；并存期结束、旧库归档后，回到「库 + 说明 + 可重建预览」。预览页由库重生成，不是第二份库，也不得代替库文件；改库后必须重生成，否则页面数字是旧账。预览若含本地文件名或姓名，只留本机并标明禁止外发；不因页面做了脱敏开关就认为库已脱敏。
- **构建收尾与边车**：缺 `目录说明.md` = 构建未完成，不是可选项；build 脚本收尾按模板写骨架（家族库写管什么 / 五表 / PHI 只在此处；子库写零 PHI / 时点口径 / 可选模态）。SQLite 边车 `<库>db-wal` 与 `-shm` 同在 = 库正被打开 / 未 checkpoint（构建中，放行）；只有 `-wal` 无 `-shm`、跨一次构建仍在 = 上次写坏残留，记 **P1**（S25/S26）。
- **1+N：一库一工程**：每家族恰一个家族库 `<family>db`；每个子工程恰一个子库 `<slug>db`。短码 = 子工程 slug，靠 `ref_project` 与子库 `src` 区分，只表示项目归属，不是个体主索引；家族拆分时整树随 `<family>` 走。
- **可独立处理**：家族库与子库可分别备份 / VACUUM；子库在 D28「零 PHI」通过后可单独外发，家族库含 PHI 一律不得外发。
- **跨库唯一引用**：只靠 `family_uid`（形如 `ACN-000137`）。SQLite 无跨库外键，父子一致性由 `verify_db` 的 ATTACH 检查（D27/D34）承担。
- **现役骨架（5t）**：家族库实表 `meta` / `id` / `id_number` / `dict` / `ref_project`（五张）；子库实表 `meta` / `src` / `person` / `clin` / `_modules_<mod>`（有模态数据则 ≥1 张）/ `qc`（六类）。`id` / `id_number` 是唯一 PHI 落点；`person` 是**无 PHI 占位表**（`family_uid` / `subject_label` / `id_status`），不存姓名 / 身份证 / 电话 / 地址。
- **家族库五表口径**：`id` 存姓名 / 电话 / 身份证 / 地址 / `family_uid`（`^[A-Z0-9_]+-\\d{6}$`）；各类号走 `id_number(kind, value)`（住院号 / 门诊号 / 影像号 / 病理号 / 样本号）；`dict` 登记变量（`role='phi'` 只许 `scope='family'`）；`ref_project` 登记子库清单与 `db_rel_path` / `built_at` / `sha256`。
- **`ref_project` 四个计数**：`person_count`（person 行数，含占位）/ `clin_person_n`（有 ≥1 条 clin 行的人数 = **队列人数口径**）/ `longitudinal_n`（有 ≥2 个不同 `period_month` 的人数）/ `multi_record_n`（有 >1 条 clin 行的人数）。四列由门禁实时重算比对，任一不等即 **P0**（D35）；**对外只报 `clin_person_n`**。
- **家族级人数不报**：`id` 行数 ≠ 患者数，`person_count` 也不是队列人数。跨子库未解析时只报项目级 `clin_person_n`；`id` 行数只允许作「身份行数」出现在方法学附注（D36）。试点实测：LC 家族库 `id` 3,050 行，四个项目 `clin_person_n` 合计 2,234 人；非姓名证据判同一人为 0，故不提供家族级合计。
- **冻结旧库（core-6t）**：旧七表 `meta` / `project` / `src` / `item` / `val` / `person` / `person_key` 与兼容视图 `doc` / `sheet` / `sheet_dup` / `entity` / `fact` 只在 `<family>db_6t` 内保留，**只读**，供迁移对账；不得在旧库继续建表 / 改数，也不再按此骨架新建库。旧库 `meta.source_db` + `sha256` 须指向原始旧库并校验（D33）。
- **命名**：库文件 `<family>db` / `<slug>db`（均无扩展名；实例 `MHE_ANdb`、`lxj_ACNdb`）；冻结旧库 `<family>db_6t`（同目录、无扩展名、只读）。`_PHI` 与子工程叶内放「库文件 + `目录说明.md` + 可重建预览页」；说明须含口径 / 表结构 / 查询示例 / 重建步骤 / 限制 / `source_db` 对应关系（旧库名 + sha256）。
- **只收表格（去重合并结果）**：xlsx / xls / csv 等可解析的原始行列数据入库；入库即按「散表归并」去重合并（文件 sha → 整表 → 行级），同格式多份并入对应子库（`src.rel_path` + `src.sha256` 区分）；非原始数据不入库，口径 → 见「项目业务表（`clin` + `_modules_<mod>` + `qc`）」。库不是散表仓，不存原件、不存合并中间簿。**压缩档内的表格同样入库**：解出到 staging 后按同一条去重合并，档本身仍归 `__zip`。
- **压缩档本身不进 db、不留叶**：`*.tar.zst`、`7z`、`zip`、`gz`、`rar` 等归档一律进 `<family>\__zip\`（归位见「`__zip` 原始件池」）；**档内表格文件须解出、按「散表归并」入库**，档内非表格件（原始图 / 记录 / 文档）不入库；解包树校验后移 `{DEL}`，readme / 移动台账记「档→表」映射。
- **叶内只留 readme + 子库**：原表入库并校验后，叶内只留 `<slug>db` 与 `目录说明.md`（写入库日 / 项目 slug / 原件去向 / 未入库例外 / `source_db`+sha256）；不得留散表。未入库件（PHI 花名册、模板、解析失败件）留叶并在 readme 写明原因，不得另存副本；**PHI 花名册只作迁移证据，不得并入子库**（迁移后按 D28 复核）。
- **原件留痕**：建库并校验通过后，原件移 `{DEL}\_by-function\<batch>\originals\<code>\<family>\<leaf>\`，写 `*-MOVED-YYYYMMDD.tsv`（相对路径 / 字节 / sha256）；原件不回流。
- **门禁**：`_PHI` 是 `_` 前缀桶，不参与 S23 桶/叶后缀校验。`structure_check.py` **S25** 校验家族库/子库落点与库文件（`<family>db` / `<slug>db` / 冻结 `<family>db_6t`、库头 SQLite、按 `meta.kind` + `schema_version` 分派 5t 家族五表 / 子库六类表、根级 `_DataBase` 下不得出现库桶）；**S26** 允许叶内 `<slug>db`；**S27** 确认 `__zip` 不收库文件。`verify_db.py` 先按 `schema_version` 分派：旧 core-6t 仍跑 D1–D22，5t 跑 D23–D45（含跨库 ATTACH）。建库 / 迁移前后仍须全门 PASS。
- 细则（去重层级、5t/6t schema、`family_uid` 分配、QA 清单、重建命令、旧库对账）→ skill `db-library`。

### 散表归并与表格入库

- **触发**：家族根 / 叶根散落表格（同项目多份、`(n)` 版本、一簿多 sheet）需要「去重 → 对齐 → 合并成一个 Excel」或「入 `_PHI`」时。
- **项目粒度 = 叶 slug**；合并产物 `<项目名>_merged_YYYYMMDD.xlsx` **不落**叶根 / 家族根：同格式多份直接入库对应子库 `<slug>\\<slug>db`（家族级身份映射另登记家族库 `id` / `id_number`），确需中间簿只暂存 `{DEL}\\_by-function\\<batch>\\`；`__zip\\` 内不动。
- **去重三层**：① 文件级 sha256；② 整表级（表头 + 行哈希集合全等 = 重复；真子集 = subset，只记边、不存第二份字节）；③ 行级 / 实体级（自然键整行全等才去重；跨项目映射只人工建）。
- **对齐**：列名词典 + 表头驱动解析；**不按 mtime 判新旧**（迁移会刷新 mtime，本轮 239/258 张挤在 13 个分钟桶）；版本簇（`(n)` / `copy`）只作线索，须开表核对。
- **去重合并**：行名或行键一致时按列合并去重，以较新数据为准，旧表独有列回填，不得编造数值或列名。列名一致时按行合并去重，以较新数据为准，旧表独有行保留。较新指同一版本链中较后的来源（版本标记、`(n)`、`copy`、新旧线索）；mtime 判定 → 见上「对齐」。
- **合并冲突**：若较后的表明显更小、覆盖会缩小队列，则保留更完整的表，较小者只记 subset，不得覆盖。新旧无法判定时，重叠行保留非空单元格最多的一行，并列时取原行序更前的；被丢行只回填空位。表头缺失、双层或把数据行误当表头时，须先修好再合并。
- **留痕**：原件移 `{DEL}\_by-function\<batch>\originals\<code>\<family>\<leaf>\`，写 `*-MOVED-YYYYMMDD.tsv`（件数 / 字节 / sha256 100% 核验）；结果与限制写叶 / 家族 `目录说明.md` 追加段 + `_index.csv` note；批次报告 `<batch>-REPORT.md`。
- **闸**：改动前后 `structure_check.py` 全门 PASS；手工删除 / 清除须主人确认后写 `REVOKED-YYYYMMDD.tsv`，不得静默。
- 策展后每叶只留一份现行源文件，内含长表与宽表（每表最多 5 个工作单）；子库内 `clin` 一张 + `_modules_<mod>` 按模态/特征域各一张（逐张登记 `dict`）+ `qc` 一张，口径见「项目业务表（`clin` + `_modules_<mod>` + `qc`）」。
- 细则（三类型判定、表头驱动解析、坑位清单、合并簿 sheet 约定）→ skill `db-library`。

### 项目业务表（`clin` + `_modules_<mod>` + `qc`；不再按长/宽各一限表）

- **范围**：约束的是每个**子工程库**的业务表，不是家族库骨架。家族库只存身份、号、字典与子库登记（`id` / `id_number` / `dict` / `ref_project`），不存项目业务表。子库业务表 = `clin` 一张 + `_modules_<mod>` N 张（每模态/特征域一张，须在 `dict` 登记）+ `qc` 一张；`person` 是占位表，不是业务表。「每项目至多长表与宽表各一」不再适用。
- **现行源文件**：每个叶只保留一份现行源文件，且须是一份工作簿，不得长表、宽表各放一个文件。该文件内为长表与宽表；无内容的一侧省略，空席不垫。现行骨架仍是本文件的 5t（家族五表 / 子库 `clin` / `_modules_<mod>` / `qc` 等），不得用精简登记册或 blob 库骨架替换。每张表最多 5 个工作单；工作单名可用 `clin` / `_modules_<mod>` / `qc` / `analysis`，入子库后固定落到 `clin` / `_modules_<mod>` / `qc`，**不得按工作单另开表**。
- **表族三组、各管一段**：`clin` 是唯一「人 × 时点」主表；`_modules_<mod>` 只收不宜拉长的矩阵（组学 / 谱图 / ICC / 相关矩阵 / 影像组学）；`qc` 只收门禁结果与人工裁决。三组之外要建表，先在本节登记再建，不靠临时命名。
- **横断面一张、纵向按波次分张**：横断面研究 `clin` 一张。纵向研究若各波次变量集不同或列不能对齐，按波次分表 `clin_t0` / `clin_t1` …，序号按时间先后；模块同法 `_modules_<mod>_t<k>`。变量集相同、只是采集时间不同 → **仍是一张长表**加 `period_month`，不按波次拆。
- **波次须显式登记**：分波次时子库 `meta` 记 `clin_layout='wave'`、`wave_map`（`{"t0": {"period_from": "...", "period_to": "...", "crf": "...", "src_id": 1}}`）、`business_tables`（数组，列全部业务表名）。校验按 `business_tables` 枚举，**不得**用 `_t\d+` 或 `_1` / `_2` 猜表名、猜波次；同一张表用后缀列（`var_1` / `var_2`）承载不同波次同样禁止。
- **一人一波一行**：第 `k` 波次表一行 = 一个受试者 × 该波次一次采集；同一人跨波各一行，靠 `family_uid` + 波次号对齐，不得把两个波次的列并进同一行。
- **长表与宽表**：

| 表 | 内容 |
|---|---|
| `clin` | 一行一条「受试者 × 时点 × visit」记录（`family_uid` / `period_month` / `month_ix` / `visit_ix`）。随访与结局叠入本表并带时点或拆分列，不单立第三张表。临床敏感字段可留；**姓名 / 身份证 / 电话 / 地址只进家族库 `id`，`clin` 不得出现**（D28）。 |
| `_modules_<mod>` | 不宜强行拉长的矩阵（组学 / 影像组学 / 谱图 / ICC 或相关矩阵）按模态或特征域建表，如 `_modules_radiomics` / `_modules_us` / `_modules_mri`。组学走 `_modules_radiomics(exam_uid, roi, feature, value)` 长表，**不建千列宽表**。 |
| `qc` | 门禁结果与人工裁决（`scope` / `code` / `severity` / `status`）；是正式表，不是业务数据表。 |

- **「不收」要分层登记，不许静默丢**：整张工作单不入库 → `meta.excluded_sheets`，每条结构化 `{slug, src_id, rel_path, sheet, rows, cols, reason}`，`reason ∈ {no_individual_key, empty, duplicate, phi_only, title_page}`；**每一行必须能唯一定位到一条 `src_id`**（否则十几张同名的 `Sheet1` 无法查证，登记表只是清单不是账）。
- 「重复」（`duplicate`：同一份数据的另一种切法、0 个新列）与「没键」（`no_individual_key`：数据无法归人）是两件事，写错会让后来的人以为被标 `duplicate` 的表还有独立数据。
- 单列不入库 → `meta.excluded_columns`（`{column, reason, source_sheet, rows_nonnull}`）。两者之外还要留「扫过」的证据（如 `qc(TEXT_SCANNED)`）——**零命中与没扫过在库里长得一样**。
- **粒度必须与表对应**：`clin` 一行 = 一个受试者 × 一个月。exam 级数据（一次检查 / 一个样本 / 一张谱）**不得进 `clin`**，只能进 `_modules_<mod>`，或按 `meta.modules_exam_policy='deferred_until_requested'` 显式声明延后建表。keyless 宽表（有数据、无个体键）整表进 `excluded_sheets`，**不许把行号当身份塞进 `clin`**——实测一张 906 行的 `clin` 里 269 行是 exam 占位，报告里的「442 人」因此不是真人数（真数 173）。

- **时点粒度（`period_unit`）**：以月为原子，`period_month` = `YYYY-MM`，`month_ix` = year*12+month-1，`bin_ix` = `month_ix` // `period_unit`（派生不落盘）。三种情形：① 源表无日期 → `period_unit` 为 `NULL`，`clin` 全 `UNK`；② 有日期且能连成序列 → 声明 `1` / `3` / `6`。
- **有日期但逐人归组未定**（如 `qrx_LUNG_his`：808 行中 253 行带日期、每人仅 1 行）→ 照常声明粒度，并记 `qc(LONGITUDINAL_UNAVAILABLE)`（P2）+ `identity_state='unresolved'`。`NULL` 只表示「库里没有时间」，**不得**表示「有时间但连不成序列」（D37/D38）；`unknown` 不得有 `month_ix`，也不得用假日期填充（D29）。

- **只收原始行列数据**：入库的只是原始矩形数据（行 × 列）。论文统计与作图结果、伦理材料、通讯录、汇报稿、方法说明及其他非原始数据不进库。**`dict`（变量字典）与 `qc`（门禁日志）自 5t 起是正式表，不受「不得占用第三张库内表」限制**；但只登记字典与门禁结果，不得借道塞业务数据。伦理材料仍不进库（旧 core-6t 由 D19 拦；5t 库里伦理材料不得进入 `dict.source` / `ref_project.slug` / 子库 `src.rel_path`）。
- **版本链**：计算 / 校正 / old / copy 等版本只把现行 `clin` / `_modules_<mod>` 纳入定稿，其余留子库 `src.kind='workbook'` 的源表（保留 `rel_path` + `sha256`）。
- **角色与源表**：5t 子库 `src.kind` 只许 `old_db`、`workbook`、`archive_member`，保留 `rel_path` + `sha256`，不得删除 `src` 行。冻结旧库的 `src.role`（兼容视图 `sheet.role`）仍只许 `raw` / `curated` / `derived`，定稿标 `curated`、来源留 `raw`、`derived` 只留 blob 不写 `val` / `fact`（`verify_db` D22，仅旧库适用）。
- **写库**：把 `clin` / `_modules_<mod>` 写入子库（身份字段写家族库 `id` / `id_number`）或 `{RAW}`，以及 `--apply` / `--move`，须当轮点名；缺省 dry-run。写盘总闸见 `My rule.md` §2。
- **外发边界**：家族库含 PHI，**一律不得外发**；子库在 D28「零 PHI」通过后才可单独外发。业务表中的敏感字段与记录键不得写入聊天、记忆、备忘录、规则正文或回执（见 `My rule.md` §1.2）。

### 库门禁码表（D1–D70）

- **现行码（core-6t）**：`verify_db.py` 实有 `D1`–`D9`、`D19`–`D22`；判级细节以脚本为准，本表只记口径。
- **`D10`–`D18` 不存在**：总览里的 `D10` / `D12` / `D13` / `D14` 是人工注记码，脚本无实现；新码从 `D23` 起编，**不回填**旧号。
- **`D21` 判级已升为 P0**：明文 PHI 不再只是提示；**PHI 只许出现在家族库**，子库任何位置命中即 P0（`D28` / `D44`）。
- **分派**：旧 core-6t 库跑 `D1`–`D9`、`D19`–`D22`；5t 库按 `meta.schema_version` 跑 `D23`–`D70`。同一库不得混跑两套。

| 码 | 名称 | 判级 | 判据摘要 |
|---|---|---|---|
| D1 | 库可打开 / 完整性 | 沿用现行 | `PRAGMA integrity_check`；打不开即 FAIL |
| D2 | 骨架与 schema | 沿用现行 | 按 profile 判定 7t / 6t，表与索引齐 |
| D3 | 行数自洽 | 沿用现行 | `val` / `fact` / `entity` 计数互证 |
| D4 | `meta` 必填键 | 沿用现行 | 缺键或值为空 |
| D5 | 孤儿行 | 沿用现行 | 子表引用父表不存在的键 |
| D6 | `doc.n_sheets` | 沿用现行 | 与 `sheet` 实际行数不符 |
| D7 | `entity` 覆盖 | 沿用现行 | 无实体行比例；>5% 升 P0 |
| D8 | 移动台账 | 沿用现行 | `*-MOVED-*.tsv` 与原件去向 |
| D9 | 叶 / `__zip` 落点 | 沿用现行 | 库文件与 `目录说明.md` 位置 |
| D19 | 伦理材料不进库 | P0 | `doc.rel_path` / `project.slug,leaf` / `sheet.name` 命中伦理词 |
| D20 | 表头契约 | P1 | 表头与固定列 / `dict` 一致 |
| D21 | 明文 PHI | **P0** | 手机 / 身份证正则命中且不在家族库 `id` / `id_number`；越界即 P0 |
| D22 | `sheet.role` 值域 | P2 | 只许 `raw` / `curated` / `derived`；`derived` 不写 `val` / `fact` |
| D23 | 落点与骨架 | P0 | 家族库 / 子库路径、库头 SQLite、五表 / 六类表齐 |
| D24 | `family_uid` 格式与唯一 | P0 | 正则 `^[A-Z0-9_]+-\d{6}$`；家族库内唯一、非空 |
| D25 | `id_number` 号种 | P1 | `kind` 落白名单；同 `(kind, value)` 不重复、不裸号连接 |
| D26 | `dict` 与 PHI 越界 | P0 | `role='phi'` 只许 `scope='family'`；子库 `dict` 不得出现 PHI 列 |
| D27 | 子库 `person` ⊆ 家族 `id` | P0 | ATTACH 家族库，`person.family_uid` 必须命中 `id` |
| D28 | 子库零 PHI | P0 | 列名与内容扫姓名 / 身份证（18 位）/ 手机（11 位）/ 地址 |
| D29 | 时点合法 | P0（行级 P1） | `month_ix` 与 `period_month` 一致；`unit ∈ {1,3,6}`；`unknown` 无 `month_ix` |
| D30 | `dict` 列覆盖率 | P1 | `clin` / `_modules_*` 每列在 `dict` 登记，覆盖率须 100% |
| D31 | `_modules_*` 主键与 FK | P0 / P1 | `exam_uid` 唯一为 P0；`radiomics` 长表孤儿为 P1 |
| D32 | 最新 `qc` 无未决 P0 | P0 | 每库最新一轮 `qc` 不得留 `status='open'` 的 P0 |
| D33 | 旧库并存留痕 | P1 | 新库 `meta` 记 `source_db` 路径 + `sha256`，且与旧库实算一致 |
| D34 | `ref_project` 双向登记 | **P0** | 两个方向都查：① 每个含 `<slug>db` 的目录在 `ref_project` 必须有行；② `ref_project` 每行必须有对应库文件。任一方向缺即 P0，输出 `ref_project_missing.md`。镜像门只遍历「已有的行」时，少写一行会让其余计数照样自洽、全门绿——**缺席比错值更难发现**，与「blob 指针指空不报错」同型 |
| D35 | `ref_project` 四计数镜像 | P0 | `person_count` / `clin_person_n` / `longitudinal_n` / `multi_record_n` 与子库实时重算逐一相等 |
| D36 | 身份行数不得作样本量 | P0（文档级） | 报告 / 说明不得用 `id` 行数当患者数；家族级人数默认不报 |
| D37 | 无日期 ⇒ `period_unit` NULL | P0 | 无日期列必须 `NULL` 且 `clin` 全 `UNK`；反之亦然 |
| D38 | 有日期 ≠ 有纵向 | P1 | `longitudinal_n=0` 而库内有日期时须有 `qc(LONGITUDINAL_UNAVAILABLE)` |
| D39 | 同人多条无日期记录 | P1 | `multi_record_n>0` 且全 `UNK` 须有 `qc(UNK_MULTI_RECORD)` 定性 |
| D40 | 裸号 join 禁止 | P0 | 按号关联必须 `(kind, number)` 成对，不得单号跨命名空间连接 |
| D41 | 姓名不是键 | P0 | 不得用姓名合并身份行；匿名占位符须置 `NULL` |
| D42 | 全空列留痕 | P2 | 源列 100% 空时逐列记 `qc(COLUMN_EMPTY)` |
| D43 | sheet 重复视图三条件 | P1 | 行数同 + 列集为子集 + 共有列逐格相等，缺一不得标 `dup_of` |
| D44 | PHI 写前拦截 | P0 | `qc(PHI_COLUMN)` 与值级扫描 0 命中两条都要有 |
| D45 | 普查覆盖 `src.blob` 宽表 | P0（口径级） | `is_wide=1` 的表不进 EAV，普查只扫行即无效 |
| D46 | 身份不可得显式声明 | P2 | `id` 0 行时 `meta.identity_state='unavailable'` + `qc(IDENTITY_UNAVAILABLE)`；不得与 `unresolved` 混用 |
| D47 | `exam_uid` ≠ 一次检查 | P1 | 模态表一行 = 一个病灶 / 一次检测，报告不得称「一次检查 / 一次随访」 |
| D48 | `clin` 无后缀族 | P0 | 列名禁 `_\d+$`；同义多列先映射规范名再合并 |
| D49 | 同一人多行须证明是多个事件 | P1 | 三支：① 同人同月多行 → P1；② 半套变量拆两行（四条件同时成立）→ P1，须合并；③ 其余 → P2 报数并写 `meta.multi_record_reason`。半套变量的四条件是：同一人同时存在有日期行与 `UNK` 行；任两行各自非空变量 ≥20；交集/较小侧 <30%；两行非空列不带互不相同的 `prefix__` 命名块（`ct1__` vs `mrfinal__` 是不同测量矩阵，不算拆行）。单用「交集低即 P1」会误报重复检查（实测误报 1,533 + 46 人） |
| D50 | `Σmerged_n` 守恒 | P1 | 必须等于实际取出的源记录数，差一条都要定位 |
| D51 | 特征名折叠后同名多值 | P0 | `*_val.feature` 全小写、去尾点、`Shape.`→`shape_` 后不得再出现同名 |
| D52 | 被排除列留痕 | P2 | `meta.excluded_columns` 结构化（列/原因/源表/非空行数），且不得再现于任何表 |
| D53 | 占位行静默清空 | P1 | 占位 `uid` 对应源行有非空值而 `clin` 值列全空 ⇒ 写库时丢值 |
| D54 | 子库 PHI 按行级对齐判 | P0 | 某格值 == **本行 `family_uid` 名下**的 `id_number.value`／`id.phone`/`id_card`/`address` ⇒ **P0（1 格也算）**；等于**别人**的号码 ⇒ P2 只计数。泄漏本质是跟着人走，不是值出现几次——按「值出现 ≥2 次」判会两头都错（真泄漏可只 1 格；`age=60` 撞某人住院号 `60` 出现百次仍是巧合）。键列从 `dict.role='key'` 读，**不许写死列名**；`dict` 的 `family` 与 `proj:` 两种 scope 必须一起读（只读一种会造假 P0）。须自带正反 fixture |
| D55 | 相对时间须有零点 | P1 | 相对列缺 `dict.unit` 或 `time_origin` → P1；声明「只有相对量」却给非 `UNK` 的 `period_month` → P0 |
| D56 | DICOM 头 PHI 只进家族库 | P0 | `PatientName`/`PatientID`/`OtherPatientIDs`/`AccessionNumber`/`PatientBirthDate`/`PatientAddress`/`PatientTelephoneNumbers` 只许落 `id` / `id_number`；子库出现即 P0 |
| D57 | DICOM 伪匿名与身份冲突 | P1 | `name_quality='pseudonymized'`（`ANON*`/`XXX`/`TEST`/纯数字/单字符重复）不得当真名；一 ID 多姓名或一姓名多 ID 各建身份并记 qc，禁合并 |
| D58 | 结局未产生不得预建 | P2（文档级） | `meta.outcome_status ∈ not_collected / collected`；未产生时不建结局列、`dict` 不出现 `role='outcome'`；结局到来另建表，不追加进 `clin` |
| D59 | 批次可追溯 | P1 | 每行 `_modules_*` 必须经 `batch_id` 定到一台设备：家族库 `ref_batch(batch_id, vendor, model, field_strength, kvp, kernel, slice_thickness, site, n_series, date_from, date_to)`；`batch_id` 悬空或设备字段全空即 P1 |
| D60 | 特征抽取参数不一致不得并池 | P0 | 同一 `feature` 在不同批次登记了不同抽取参数（bin width / resample / 软件与版本 / ROI 来源）却同表并存，即 P0；参数逐批次落 `ref_batch.extraction_params` |
| D61 | 批次混杂须报 | P2 | 含 `batch_id` 的库须给 `batch × 结局/关键协变量` 交叉表；某批次独占某一结局水平时须写明「无法分离设备效应」，不得直接 ComBat 后当作校正完成 |
| D62 | 跨族 blob 指针自带容器身份 | P1 | `src.rel_path` 形如 `blob:<容器库文件名>@<构建日>:src_id=<旧 src_id>#<sheet>`，`src.sha256` 等于容器内该 sheet 实际哈希；容器在盘、`src_id` 可查、sha 相符，任一不满足即 P1。切库日旧库改名 `<family>db_6t`，只写路径的老式指针会**指空且不报错**；放宽只限「原件确已不在磁盘」，且逐行记 `qc(SOURCE_SNAPSHOT_ONLY,P2)`；**原件在盘而 sha 不符仍 P0**。容器整体丢失（如旧库被误覆盖、无备份）时，须逐条落 `qc(SNAPSHOT_CONTAINER_LOST)`（`scope='src'`、`column_name='<src_id>'`）显式记账，记账后该指针只报数、不判 P1——**允许损失，不允许无声损失** |
| D63 | 身份段位 ↔ 类型 ↔ 状态三元一致 | P1 | `family_uid` 段：`0xxxxx` 人真实身份（`keyed_full`/`keyed_partial`）、`8xxxxx` 动物真实受试者（`keyed_animal`）、`9xxxxx` 占位（`label_only`/`label_only_omics`）；`meta.uid_ranges` 须为结构化 JSON。三元不一致即 P1；写成一个三元检查，不拆两条（两条会各自漂移） |
| D64 | 表头行位置按需登记 | P1 | `src.header` 为空 / 含 `#n` / 含 `__nohdr__`，或 `note` 记「表头行丢失」「首行即数据」时，必须有 `meta.header_rows[("<src_id>#<sheet>")] = <1 基行号>`；`src` 无 `header` 列的老库不判。「说了已记但键不存在」是实测事故，交付须附该 meta 键的查询输出 |
| D65 | 有日期但不知是哪件事必须可数 | 只报数 | `period_month <> 'UNK' AND period_origin IS NULL` 的行数逐项目进报告。`period_source`（`exact/approx/unknown`）= 有多准，`period_origin`（`exam_date/surgery_date/admission_date/report_date/derived/unknown`）= 是哪件事；两列不可合并，否则下游按它算随访间隔必然混 |
| D66 | 两侧人数相等却无共享键 | P2 | 某项目 `clin_person_n` 与某模态 exam 数**恰好相等**且两者无任何共享键列 ⇒ `qc(KEY_ABSENT_EQUAL_N,P2)`。按行序对齐会整表挂错人，而人数、外键、PHI、dict 全通过——专挡「看起来能连」 |
| D67 | `VALUE_CONFLICT` 未持久化须标红 | 换库前必修 | 存在 `meta.value_conflict_state='not_persisted'` 时报告标红并列入换库前必修；重建须逐格写 `qc(VALUE_CONFLICT)`。零冲突与「根本没记」在库里同形，照写「冲突 0」会被读成「没有冲突」（同 D44/D52「没扫过与零命中同形」） |
| D68 | `period_month` 不得溯源自 `src.mtime` | P0 | `period_month` 可追溯到文件 mtime ⇒ P0。实测 EC 77 张表 mtime 全在同一天、LC 只有 2 天：mtime 是「拷入本机的日子」，写进时点会让整批人落在同一个月且库里看不出是假的。mtime 只进 `meta.ingest_batch` 且只用于查重；估算日期进 `period_month_est` + `period_source='approx'` |
| D69 | 同批重复副本须留痕 | P2 | 同 `ingest_batch` 内两表列名重叠 ≥50%、**共有列 ≥5**、行可匹配 ⇒ `qc(DUP_BATCH_SUSPECT,P2)`；共有列 <5 的判据全是噪声（`ID/group/result` 三列表两两都「重叠 100%」）。重跑前先删旧 qc 行，否则重复叠加 |
| D70 | 库内表结构须与 SCHEMA 一致 | P0 | 把 SCHEMA 两段 DDL 在空内存库执行一遍取 `pragma table_info`，与目标库逐表比：缺表 / 缺列 / 类型不符即 P0。**不许手写解析 DDL 文本**（会被散文行与注释骗）。实测某库缺 `dict.aliases`、`src.status`、`clin.cohort`：建得出来、门禁也过，只在按 `status` 过滤时崩 |
| D71 | 9 段纯度（只对患者级种类提示） | 只报数 | 9 段（`9xxxxx`）是「无患者级号码」的占位段；若其中某身份持有 `kind ∈ {inpatient, outpatient, mrn, pathology}` 的号码，则两者矛盾，提示「若该号唯一指向一人，可升 0 段」。**不判失败**：SCHEMA 的 8.1 节明文允许 9 段带 `sample` 等样本级号（样本号不识别到人），判红等于罚自己的条文 |
| D72 | 身份段位 ↔ 粒度相容 | P1 | 每个项目必须在 `meta.identity_grain` 声明 `person` / `specimen` / `exam` / `sample` / `label` / `mixed`。`person` ⇒ **有姓名或有患者级号码**的身份必须在 0/8 段，9 段只许「既无姓名也无号」的占位（`mixed` 需 `grain_note`，只报数；非 person 粒度下 0 段有名身份只报数）。判据是**粒度**不是「有没有名字」：SCC 一个身份就是一个病理标本，标本行当然带病人姓名——实测 11,724 个 9 段身份里 8,502 个有姓名，按「9 段=无姓名」判会把整个标本级队列判成全错。缺声明即 P1 |
| D73 | `id.name` 不得是合成标签 | 只报数 | 姓名格出现 `subject/sub/case/sample/patient/pt/p/s/mice/rat/no` + 数字（`Subject1`、`Sample_03`）即提示：**有人名 ≠ 有身份**，把工具标签写进姓名字段，报告里会出现「患者 Subject1」这种假人。只报数不判级——标签本身可以合法存在，只是不该叫 `name` |
| D74 | 家族库 `meta` 必备键 | 只报数 | 家族库 `meta` 须有 `schema_version` / `family` / `built_at`；缺则列名。三键是「这个库按哪版 SCHEMA、属于哪家、什么时候建的」的唯一答案，缺了只能靠文件名猜 |
| D75 | 号码三元唯一性 | P0 | `id_number` 按 `(kind, issuer, value)` 三元判唯一：同一三元被 ≥2 个 `family_uid` 持有 ⇒ 号码冲突。`issuer` 是**命名空间**（`lxj_ACN\|体检编号`），同号在不同命名空间是不同号；`issuer` 为空的号码单独计数（裸号 join 的前置风险）。占位段（`9xxxxx`）共享号码只报数 |

- **机器点**：`D1`–`D22` 在 `verify_db.py`（`{code_root}\tools\db-library\verify_db.py`）；`D23`–`D75` 的 5t 实现落 `{code_root}\tools\db-library\db5t\gates.py`（跨库项用只读 `ATTACH` / `file:?mode=ro` 打开家族库），判据用的 SCHEMA 由 `db5t\paths.py` 解析（`DB5T_BATCH` / `DB5T_ROOT` / `DB5T_SCHEMA` 三个环境变量）。**文档编号与代码输出必须逐条对应**：同一含义两个号、或代码打了文档里不存在的号，等于门禁与条文各说各话（本轮修过一次：结构漂移曾被代码叫 D58、文档叫 D70）。
- **判级**：P0 阻断（退出码 1），P1 应修，P2 提示；同一问题按最高级只报一次。

**建库工程约束**（每条都对应一次实测事故，改门禁或写 build 时逐条对照）：

1. **改判据必须自带正反 fixture**：改动门禁判据时同批提两张最小库（该报的、不该报的），否则「改完变绿」分不清是修对了还是判据失效。
2. **门禁只读、先写完库再算 sha**：`mode=ro` 打开，跑完不得写任何东西；`meta` / `sha256` 在最后一次写库之后计算，且连跑两遍结果不变（幂等）。
3. **计数一律 SQL 现算**：`meta` 与 `ref_project` 的人数/行数不得用「总数 − 已知数」构造（`7,656 − 210` 这类减法在两个库上各错 5 与 1）。
4. **清值 / 删行先 dry-run**：先把将被改动的行导出 csv 再执行；判据按该 `kind` 的合法形态写，禁「长度 < 4 当垃圾」这种复用 PHI 阈值的规则（曾删掉 8 家 357 条合法短号）。
5. **`src_row` 只在同一 `src_id` 内唯一**：`UPDATE … WHERE src_row = ?` 会跨表命中，必须带 `src_id`。
6. **DDL 逐字读时只剥行首注释符**：含 `**` 的散文行曾被整行吃掉，导致 `ref_project` 少一列而门禁全绿。
7. **`entity` / `feature` 一维一字段**：不许把两个维度拼进一个字符串（`<样本>|<靶标>`）；拼接后的同名重复会被主键 `INSERT OR REPLACE` 静默吃掉（实测 16,586 格塌成 5,436 格）。
8. **不是身份键的正确落点是「换一张表」**：从 `id_number` 撤下的号码进 `clin` 的 `*_seq_no` / `label_id` 等 `role='aux'` 列并留痕，**不删**——删把已知变未知，而库最贵的是还能查回去。

## 阶段夹与课题名

课题路径：`D:\MyProjects\<stage>\<project>`。

| 阶段 | 含义 |
|---|---|
| `drafting` | 选题 / 数据 / house 稿 |
| `pre-submit` | 投目标刊前打磨 |
| `reviewing` | 已投 / 在审 / 修回再投（收到审稿意见是事件，不是阶段） |
| `accepted` | 接收 / 校样 |

- 已有文件夹若仍用旧名 → 按 `aliases.yaml`（`kind: stage`）阅读；**不改写**、**勿重建**。**不新建** `DER` 阶段夹或根目录（`DER` 仅是 `_diseases.csv` 的家族码，不是阶段 / 工作区）。

课题夹名：`lowercase_UPPERCASE`（如 `fyh_CAC`、`xlm_LG`）。旧式 `CAC_fyh`、`lung_xlm` 已退休。

**命名：** `<prefix>_<suffix>`——`<prefix>` = sub-PI 小写拼音首字母（如 `lxf`），`<suffix>` = 项目短码（大写或约定写法，如 `RC`/`CID`）。一人多题、一题多人都不改名；同后缀多例加 `_1`/`_2`（如 `llj_OV_1`）。中文人名只进台账（`_Docs\mem\people.csv`），路径与正文不写中文名。

### 阶段库管理规则（工程库）

| 事项 | 规则 |
|---|---|
| 谁能动 | 阶段夹内的搬件/改名/删只由该项目 owner 发起，或 owner 当轮点名；QC 只报不擅动，修复须授权（`My rule.md` §2）。 |
| 进场 | 新课题先建 `ref\` 四件（`settings.ini` / `README.md` / `manuscript-revision.md` + `ref\`），`INPUT` 必须可解析；空 `INPUT` 视为未开跑。 |
| 出场 | 阶段推进靠事件（开跑 / 投稿 / 接收 / 校样），不靠目录名；`accepted` 收工按「accepted 收工」四落点分流。 |
| 痕迹 | 版本推进、搬件、改名、`.bak` 处置都写 `ref\manuscript-revision.md`；台账追加，不覆盖。 |
| 判据 | 骨架 / 命名 / 数据口径 → `{doc_root}\test\STAGE-QC-STANDARD.md`；机器门 S32–S34（`structure_check.py`）每轮 QC 必跑。 |

**`archived` 不是第五阶段：** 不进上表、不进 `study_folder_stage_aliases`；见「archived 冷库」。关系总图见下「工作区关系：阶段 · 分流 · harvest · 冷库」。

## 工作区关系：阶段 · 分流 · harvest · 冷库

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

- **harvest：** 抽「怎么做」→ `_Docs\harvest`；仅当主人说「进skills」才进 MY-SKILLS（extract ≠ promote；流程与纳入门禁见 `{SKILLS}\00_orchestrator\harvest\SKILL.md`，00 只调度/门禁/复核；指针见 `skills.md` §3）。
- **closeout：** 物理落点与精简；**不是** harvest 的替代步骤。
- **harvest 也不代替搬盘：** 抽完仍须按 closeout 把字节落到 `_DataBase` / `_Docs` / `.Del` / `archived`。
- **harvest 剩余件 / 先判 H1–H4 / 轮次去留** → `del-and-harvest.md` §1–§3（本文件不复写判据）。
- 关系总图 / harvest 授权 →「工作区关系：阶段 · 分流 · harvest · 冷库」。harvest 技能只抽「怎么做」；closeout 是落点；勿把 closeout 写成 harvest 步骤。

### harvest 授权范围

- 可在 `drafting` / `pre-submit` / `reviewing` / `accepted` / `archived` / `.Del` **任一侧**进行。
- **每次须主人当轮授权**；不因阶段自动触发。
- `archived` 默认只读：从冷库抽也要当轮点名；不解冻整夹除非另批。
- **QC 分工：** 库形/完整性→本地库门（`{doc_root}\test\structure_check.py` + `STRUCTURE.md`；`_DataBase` 根说明 + `DB-QC-STANDARD.md`）；纳入门禁→harvest 技能；00 复核通过后才候纳入。指针 → `skills.md` §3。

### 不进 harvest / 慎进 `_Docs` 公开层

填好知情、含姓名表、未发表全文、PHI：不进 harvest；慎进 `_Docs` 公开层（与「accepted 收工」同口径）。

## accepted 收工

**目标：** 按 closeout 精简 `accepted\<prefix_suffix>\`，再搬进 `archived\<family(suffix)>\<prefix_suffix>\` + `ARCHIVED.md`。accepted 不长期堆满。本条是**落点契约**（closeout）；关系与 harvest 授权见上「工作区关系：阶段 · 分流 · harvest · 冷库」。harvest ≠ closeout。

### 课题树精简后硬留
1. 终稿一份：`Manuscript_<slug>_{V|R|P}…`（旧名先问再改名；旧版→`ref/tmp/`）。根上只留这份**文件**，不要把整夹 `R*` / `P*` 留在根。
2. 复现 SSOT：`FinalData_<slug>.xlsx`（或 `ref/README` 钉死的现用 data.xlsx）。
3. 可选：`ref/settings.ini` 指到 `_DataBase\<family>\<prefix_suffix>\`（影像 raw 不进课题树）。

### R*/P* 整夹进 `_DataBase`
课题树内名为 `R*` / `P*` 的夹（修订包、投稿包，如 R1/R2/P1/P1.1）收工时**整夹**进 `_DataBase\<family>\<prefix_suffix>\`。若夹内单独文件 ≥20 或明显小文件堆，先 7z/zip + `.files.txt`（见上节「进 `_DataBase` 多文件先压缩」）。校验通过后，原夹移 `D:\MyProjects\.Del\_by-project\<slug>\`。根上终稿仍只留一份现行 `Manuscript_*_{V|R|P}…`**文件**（不是把整夹留在根）。

### `_DataBase` 可收
（≥20 散文件或小文件堆先 7z/zip + `.files.txt`，校验后散目录→`.Del`；见上节「进 `_DataBase` 多文件先压缩」。）
- 课题树 `R*` / `P*` 整夹
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
须当轮点名「放 _Docs」才写；默认禁 mkdir，`mem` 例外（`My rule.md` §2）。
- `templates\`：空白伦理/SCI骨架/清单/金样/brand
- `_library\ethics\approvals\`：已批批件 PDF+索引
- `_library\references\`：文献全文；课题 `ref/refer` 只 DOI 指针
- `_library\lit-bank` / `journals\`：书目、期刊池、投稿 prior
- `harvest\`：可复用写法/方法句（「进skills」再进 MY-SKILLS）
- `mem\`：people.csv、JCR 可变、证件/签名（不进 skill 正文）

填好知情、含姓名表、未发表全文不进 harvest；慎进 `_Docs` 公开层。

### 图分流
可复现图 → `.Del\_by-project\<slug>\`；不可复现 → `_DataBase`。

### 其它
- 其它 csv/xlsx：去重合并→DB；移删先问（D-1）。
- 脚本：仅用一次的留指针；功能相近且多次使用的先作 harvest 对象，可复用提案 MY-CODES（权威 → `del-and-harvest.md` §2 / §6）。
- THESIS/行政（伦理·科教科·财务）与单篇 SCI 分轨。
- 四条件齐再 archived（含 skill_ref 或 none）；更新 `_DataBase\_index.csv`、`mem\people.csv`（见「archived 冷库」）。
- syn：`D:\MyProjects`→`E:\Aitor` 仅 `/XD .Del`。
- 关系总图 / harvest 授权 →「工作区关系：阶段 · 分流 · harvest · 冷库」。harvest 技能只抽「怎么做」；closeout 是落点；勿把 closeout 写成 harvest 步骤。

## archived 冷库

`D:\MyProjects\archived` 放**已完结**项目：`D:\MyProjects\archived\<family>\<prefix_suffix>\`（L1=`<family>` **家族根**短码；`<family>` 取自 `_diseases.csv` 的 `family` 列，与 `_DataBase\<family>\<prefix_suffix>\` 同桶；第二层 = 完整课题夹名）。不按年份分层。

- **L1 = 家族根：** 冷库按疾病家族/文档类型分桶，桶名 = `_diseases.csv` 的 `family` 列（留空 = 自家族，即基码本身；挂靠按同源聚合，见上文「同源聚合」）。例：`archived\EGVB\js_CN`、`archived\MHE\ly_SCH_HE`、`archived\OTHERS\lxj_BMP6`。
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

## R&P 退役

活兄弟根 `D:\MyProjects\R&P`**已退役**：勿重建。材料落点改为：
- **课题申请包** → `_DataBase\_grants\<year>\`
- **评阅他人稿**（peer / grants / thesis）→ `_DataBase\_reviews\{peer,grants,thesis}\<year>\`

二者**不是**稿件流水线阶段：不要写入上方 `drafting` / `pre-submit` / `reviewing` / `accepted` 阶段表，也不进 `study_folder_stage_aliases`。本组期刊草稿 / R&R / 校样仍走四阶段夹。历史叙述只在 changelog 写，不进活规则。

## 文件落点

交付表权威 → `My rule.md` §3。`ref/` 子目录 → 同仓 `project-ref-layout.md`。

| 种类 | 落点 |
|---|---|
| 草稿 / 旧稿 / 一次性脚本 | 子工程内临时/中间/旧版稿 → `ref/tmp/`。跨课题或无子工程一次性 → `{DEL}` 的 `_by-project\` / `_by-function\`。`{DEL}` 定期清空，值得长期保留的不放这里。细则 → `My rule.md` §3 / `project-ref-layout.md`。 |
| 共享统计库 | `{code_modules}`（`D:\MyProjects\_Docs\GitHub\MY-CODES\modules`）。入口：`PYTHONPATH={code_stats}` 后 `python -m modules.pipeline`。课题只指向该树，不在课题内再放 `modules\`。未点名则不改该库。技能正文（怎么用、按什么规则）在 `{SKILLS}\02_data-processing\`；本仓只管代码。 |
| 02 运维（整理 / 清洗 / 同步） | `D:\MyProjects\_Docs\GitHub\MY-CODES\tools\`（`{code_stats}` + `tools/<fine-id>/`；席位夹名不镜像 `02-…`/`03-…`）。统计引擎与建模 CLI 在 `D:\MyProjects\_Docs\GitHub\MY-CODES`。 |
| 参考包 / 锁定笔记 | 课题 `ref/`。运行键只在 `ref/settings.ini`。可选 `ref/project-state.yaml` 只记设计与稿件进度。 |
| 文献全文（PDF/HTML） | `D:\MyProjects\_Docs\_library\references\<L1>\<L2>\`；子工程 `ref/refer\` 只写 `DOI_*.md` 指针；书目进 `_library\lit-bank`（不存 PDF） |
| 期刊池 / 批件 | `_library\journals\index.csv`（单表，不再留 xlsx）；`_library\ethics\approvals\<L1>\<L2>\` + `approvals-index.xlsx`；子工程候选刊只写 `ref\citation\journals.csv` + `_notes.md`。口径 → `library-taxonomy.md` |
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
- **最终**→子工程根；**中间**→`ref/` 地图；**无** `0result\`；子工程内临时 → `ref/tmp/`（非默认 `{DEL}`）；无子工程/跨课题临时进 `{DEL}`；把原件放入 Downloads 仍须点名；`{memo_dir}` 不放快捷方式；备忘录 HTML 条目用 `file:///` 链接指向原件。权威 → `My rule.md` §3。
- 可复用脚本 → 统计引擎与建模 CLI 在 `{code_stats}`（`modules/` + `model-validation/`），运维/加工脚本在 `{code_stats}\tools\<fine-id>\`（壳与索引已移 `{DEL}`）。`0script\` 已退休，不在课题根重建。长期规则/语料 → `_Docs` 相应层。
- 根不留临时/草稿/一次性中间件（例外：现行在改稿 / 现行 `Vn`）。旧版稿与中间件进 `ref/tmp/`，不进 `{DEL}`（除非过后清理先问）。`_Docs\GitHub\MY-CODES\modules\`增改移须先同意。
- 数据课题根可留：`rawdata`、`derivatives`、`atlases`、索引/manifest、`ref`。`_Docs` 仅当点名「放 _Docs」。默认从 `derivatives` 拷出要用的结果，原件留在原处；终稿落子工程根。不建 `0result\`，不重建 `0script\`。
- 同键终表合并为一张（一段说明，值列加前缀）。把原件移出子工程根须先同意。
- 移脚本或文档前先搜 `import` / `addpath` / `settings.ini` / README。仍有未改引用则不移。移完后改路径与 `_Docs` 示例再测。
- **改名 / 搬迁后的旧路径门**（与 `QC.md` R11 同方向，范围扩到项目数据件）：先扫描影响面，再定「改引用 / 留史证 / 回滚」，不允许先改目录、引用以后再说。数据件（csv / tsv / ini / py 等）当批改值，改前备份；活文档改指向，不留旧值；史证（交接单 / MOVED 台账 / changelog）可留旧值，但同句必须带标记词（`史证` / `旧布局` / `MOVED` / `已退役`）。通过标准：命中清单里只剩带标记词的史证行。
- 课题索引用 `.xlsx`，说明用 `.md`。不用 `*.tsv` 当课题索引。
- 02 整理 / 清洗 / 同步 / 抽取 → `{SKILLS}\02_data-processing\advanced\route.md`（编码 `coding.md`，抽取 `extract.md`）。表先于统计、`exc`、假分类、控制台键位与界面不在本文件展开 → 同目录 `coding.md` / `extract.md`，以及 `{SKILLS}\02_data-processing\advanced\analysis\pipeline.md`。
- **`ref/` 子目录** → 同仓 `project-ref-layout.md`；技能正文 `{SKILLS}\00_orchestrator\references\project-ref-layout.md`。

- **工程入口不用 `.bat`**：课题工程根不建、不复制入口 `.bat`；已有的移 `{DEL}` 并留台账。同步入口 `D:\MyProjects\syn.bat` 不在此列。

## 新建文件夹 / 新建文件

只许建在 `{DEL}` / `D:\MyProjects\.Del\` 的 `_by-project\`、`_by-function\`。权威与例外 → `My rule.md` §2（含 `_Docs`默认禁止 mkdir、**改已有文件须当轮点名或先问**、一次性脚本不进主目录 / `.grok\tmp` / 课题根）。本段不复写。bot mem 落点例外（`D:\MyProjects\_Docs\mem\`）→ `My rule.md` §2 写盘与授权 + §4 别名。

**目录命名**：`_Docs` 下目录一律 ASCII 英文（`approvals` / `journals` / `jcr`）；中文目录发现即当轮 rename，并在 `_library\MOVED-FROM.md` 记一行。库分类与 L1/L2 → `library-taxonomy.md`。

**`.Del` 内部三档**（park / harvest-park / harvested）与落 harvested 前的 grep 要求 → `del-and-harvest.md`。
