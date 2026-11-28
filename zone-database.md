---
name: zone-database
description: L1 专题：_DataBase 区，{RAW} 落点、家族分桶、_PHI / __zip（学位改挂 __zip\thesis）、Family 目标树、家族库与子库 1+N、散表归并、_grants / _reviews。
up: My rule.md §5
---

# `_DataBase` 区
- 管：`{RAW}` 落点、家族分桶、`_PHI` / `__zip`（学位目标落点 `__zip\thesis`）、`Family` 目标树、家族库与子库 1+N、散表归并、`_DataBase` 可收、`_grants` / `_reviews`。
- 不管：表结构与 DICOM 映射（→ `db-schema.md`）；D 码（→ `db-gates.md`）；伦理材料留存（→ `library-taxonomy.md` §3）。

## 1 `{RAW}`

- **落点：** `{RAW}\<family>\<prefix_suffix>\`（`<family>` 取自 `_diseases.csv` 的 `family` 列；按家族分桶）存放该 MyProjects 子工程的**原始数据与原始影像**：DICOM 树、未压缩导出、作为源数据的原始照片、NIfTI/NII.GZ、未处理的 4D/导出包等。衍生图/表/统计仍在课题侧（见下条）。
- **子工程只留指针：** 在 `ref\settings.ini` 写 data path；**不要**把原始体拷进 `{lab_root}\…` 或三仓（MY-RULES / MY-SKILLS / MY-CODES）。
- **衍生件仍在课题侧：** 衍生物 / 图 / 表按本文件与 `project-ref-layout.md` 落在子工程；勿塞进 `_DataBase`。
- **临床底表 ≠ 影像 raw：** Excel/CSV 底表仍落 `ref\` 或 `ref\data/`（D-1：移动前先问）。**不要**把所有「data」都倒进 `_DataBase`。
- **现行名只写 `_DataBase`；活 `00ds` = QC 对象：** 禁止再建（→ 总图退役禁建表）。
  - 任何活路径、夹名、过滤器 / 默认项仍写 `00ds` 的，视为 QC 发现，**必须更正为 `_DataBase`**；**不要**在活 allowlist / filter 里把 `00ds` 留作「legacy」。
  - 不另造第三个 raw 根。**更正活引用 ≠ 搬迁磁盘树**：不 bulk 迁移旧根；两边若都在，维持原状，等主人另批搬迁。
- **禁止进 git：** 原始影像二进制**不要**进 git（含 Git LFS）或任何 GitHub remote（DICOM 头含 PHI；二进制无有效 delta）。可选轻量清单（相对路径 + 大小 + SHA-256 + 入库日）可放子工程 `ref\pipeline/`（同 `hashes.tsv` / `MANIFEST.md` 思路）。该清单若需版本，可用**无 remote 的本地 git**；备份 = 拷到另一块盘，不是 git。
- **进 `_DataBase` 多文件先压缩：** 进 `{RAW}\…`（或其 E 镜）时，若某目录内「单独文件」≥20，或明显是大量小文件堆（DICOM 序列、切片导出、逐例中间件、碎日志），先压成**一个**归档再入库；单文件或本来就少的目录不压。
  - **格式与落点：** 优先 `7z`（`-mx=5`；固态 DICOM 可 `-m0=LZMA2`）；无 7z 用 `zip`。归档名=`<原目录名>.7z`，**唯一落点 = `<family>\__zip\<leaf>\`**（叶内与家族根禁归档，见本节「`__zip` 原始件池」）；`<名>.files.txt`（相对路径清单）**随档同放** `__zip\<leaf>\`。
  - **原目录：** 压缩校验通过（文件数/抽样 hash）后，原散目录移入 `{DEL}`；不要两边长期并存。工作中的热数据先不压；定稿/冷存再压。
  - **例外不压：** 根上索引与表（`settings.ini`、`*.xlsx`、`console.html`、README）；已是单一大文件（`.nii.gz`、整包 `.dcm`、现成 `.7z/.zip`）；主人点名要随时打开的活数据集。
  - **单元粒度：** 优先按 subject / session / modality（或一次采集单元）一档，**不要**整 slug 打成一个 mega-zip。
  - **值得 deflate：** 未压缩 DICOM 夹、未压缩 `.nii`、BMP/TIFF 栈。已压缩对象（JPEG/JPEG-LS/JPEG2000 DICOM、PNG 等）若只需容器，用 zip **store**（不二次压缩）；避免 zip-in-zip。
  - **归档后：** 不要在 `_DataBase` 或 `{lab_root}` 下再留第二份解压树。处理仍走 copy-on-need：需要时抽到工作区，**不要**长期解压在 archive 旁。
  - **清单：** `__zip\<leaf>\` 内 `<名>.files.txt` 为相对路径清单，随档同放；课题 `ref\pipeline/` 可选再记 archive（相对路径 + 大小 + SHA-256 + 入库日）。
  - 归档只是打包，**不是**加密；DICOM 头 PHI 与禁止进 git/LFS 仍适用。**不**强制密码。本条为**今后入库闸**；本票不 bulk 转换已有解压树。
  - **syn：** 压完后 `_DataBase` 仍随主树同步；`syn` 仅 `/XD .Del`。
- **单档 ≤1 GiB / 分卷：** 进 `{RAW}`、交付或归档打包时，**单个文件 ≤1 GiB（1,073,741,824 B）**；预计超限就**先分卷**，不要造出大档再拆。
  - **分卷：** 命名 `<原名>.001/.002/…`（900 MiB = 943,718,400 B 字节卷，末卷可小）；`split -b 943718400 -d -a 3 --numeric-suffixes=1 <档> <档>.`；同夹写 `分卷说明.md`（拆自档 + 原字节 + 原 sha256 + 卷表 + 还原/校验命令）。
  - **还原：** Windows `copy /b a.001+a.002+a.003 a`；Linux/macOS `cat a.0* > "a"`；拼接后 sha256 须等于记录值，再 `zstd -t` / `unzip -t` / `7z t` 验档。
  - **存量超限：** 已入库的 >1 GiB 单档同法拆分；拼接逐字节校验通过后原档才移 `{DEL}`（禁删）+ 台账（原路径 / 字节 / sha256 / 卷数）。
  - **例外：** `{DEL}` 下临时件、正在写/正在压的在途中间件不拆；归档预计超 1 GiB 时按本条**入库即分卷**（与压缩闸叠加：先压一个归档，超限再分卷）。**不** bulk 重拆 `{DEL}` 历史件。
- **只读默认：** `{RAW}` 只读，除非主人点名写入。**不预建空夹**（用到再拷 / copy-on-need）。

## 2 `{RAW}` 非课题分支与家族分桶
`{RAW}`内存三类：① 课题原始件（按家族分桶）；② `_lab`；③ `_` 开头的非课题归档分支（新件落这里；**留根**、不分桶）。
- **按家族分桶：** 课题原始件路径为 `_DataBase\<family>\<prefix_suffix>\`（例 `SCH\lxf_RC`、`EGVB\js_CN`、`MHE\ly_SCH_HE`）。
  - `<prefix>` = sub-PI 缩写；`<family>` = `_diseases.csv` 的 `family` 列（留空 = 该基码即家族根）。
  - `<prefix_suffix>` 的**后缀仍是基码**（剥末尾 `_\d+` 实例；语义复合如 `SCH_HE` / `SSD_DKI` 整段保留），实例号只在叶子夹名。
  - 家族根本身必须在 `suffix` 列有行，清单一律由 `_diseases.csv` 决定，不另设 allowlist。
  - 存量编号桶（`SSD_1\`、`LUNG2\`、`MHE1\`、`SHE\` 等）已批量归并为家族桶；DB 与 archived 用同名家族桶（含 `OTHERS` 兜底），`_Docs/test/structure_check.py` S23 守门。
- **同源聚合：** `<family>` 按**同源数据**聚合，不是按病名近义随便并。
  1. 同一影像/队列母集、同一纳排、或多篇稿共用一批 raw/底表 → 同一 `family`。
  2. 同病但非同源（独立采集 / 独立伦理 / raw 不可互指）→ 可自家族；若仅临床谱系同桶仍分叶，**文件不得跨叶混放**。
  3. 叶夹仍是 `<prefix_suffix>`。共用 raw **只存一份**：优先 `_DataBase\<family>\__zip\`（或钉死的主叶）；其它课题经 `ref\settings.ini`（或 README）指针；禁止整树复制进多叶。
  4. **`__zip` 原始件池：** 课题的原始数据 / 原始记录 / 原始图片一律进 `<family>\__zip\`，不再按叶分散。
     - **各类固定**（自各桶起普通叶 ≤2 层，D1 最终口径）：`__zip\<leaf>\<文件>` 放该叶原始件压缩档（`tar.zst` 原样，**不就地解压**，解压树用完即移 `{DEL}`）；学位论文 / 博士后 / 汇报稿原件目标落点 `__zip\thesis\<slug>\<文件>`（`__zip` 下 thesis 支为层级例外；勿再新建 `<family>\_thesis`）。
     - **一级结构：** 仅 `_PHI` / `__zip` 两桶 + `目录说明.md`（`__zip` 存在必须自带 `__zip\目录说明.md`；无叶家族例外 `__zip\<family>\` 直放，须在家族 `目录说明.md` 登记）；其下**一层平铺**，不建 `raw\` / `cohort\` 子夹。勿再新建 `_thesis` 桶。
     - **家族根：** `<family>` 根放 `目录说明.md` 记件清单 / 使用者 / PHI；搬入前先 grep 全库按路径引用；迁移记 `MOVED-*.tsv`（件数 / 字节 / sha 校验），原叶留指针；压缩档与解压树并存时**只留档**（先验档为解压树超集再移树）。
     - **唯一落点与层级：** `__zip` 为压缩档唯一落点（收的是原始件压缩档；档内表格按「家族库 `_PHI\`」条解出入库，原档仍留 `__zip`），叶内与家族根不得留任何归档；`__zip` 下普通叶文件层级 ≤2（`__zip\<leaf>\<文件>`）；`__zip\thesis\<slug>\<文件>` 为学位支例外，不再加其它中间夹。
     - **存量：** 首个实例 = `_DataBase\ACN\__zip\`（`人-血浆-171 - 0.7z`、`2026碳纤维部数据-- (3).xls`）；20 个家族已建 `__zip\`（伦理 48 项 + 学位论文 7 项 + 原始件档 13 个）。叶内非表格 raw 按一级目录 / loose 单元压 `<PREFIX>__<leaf>__<unit>-raw-<YYYY-MM-DD>.tar.zst` 上收 `__zip\<leaf>\`（不整叶 mega-zip）；原件移 `{DEL}\_by-function\<batch>\originals\<code>\<family>\<leaf>\`，写 tsv（相对路径 / 字节 / sha256），叶 `目录说明.md` 记「raw→档」映射。
  5. SSOT = `_diseases.csv` 的 `family` 列（L1 桶名以此为准；`family` 留空 = 该基码即自家族）；改挂靠先改表再搬盘；`OTHERS` 仅兜底。`_PHI` / `__zip` 为保留名（下划线前缀），与 `_lab` 同类例外：`structure_check.py` S23 **已实现**桶内 `_` / `.` 前缀叶跳过叶后缀校验。勿再新建 `_thesis`；现存 `_thesis` 夹仍受该下划线前缀跳过，实体改挂待另点名。
  6. **短码夹层级：** 目标态位于 `{RAW}\Family\<family>\<prefix_suffix>`。层深见 `db-build-contract.md` 契 10。**2026-11-28 已迁入**：26 个家族（VEGF 只有家族库）已在 `{RAW}\Family\<family>\`，`_DataBase` 根只留非家族夹。**叶内目录 ≤3 层**，超深链条按 `<父>_<子>` 合并为单层名（实例：`DER\zyx_H`，原 8 层 / 1,188 个超深目录 → 3 层）；派生件（期刊成图 / 投稿包 / 汇报稿）不进叶内 raw，`_未标天数` 这类纯归档中间层不保留；表格入库后叶内只留 `目录说明.md`（见「家族库 `_PHI\`」）。
  7. 与 archived 同构：冷库 L1 仍跟同一 `family`；本条**不**改 accepted 收工硬留清单。
- **文档支：** 学位论文 / 标书 / 伦理申请材料不建 `_DataBase` 顶层 `_thesis`、`_grants\_misc`、`_ethics\_misc` 三夹；勿再新建家族 `_thesis`，论文目标落点 `<family>\__zip\thesis\<slug>\`（目标态家族在 `Family\<family>\`）。标书原件归 `_DataBase\_grants\<year>\`；伦理材料不进 `_DataBase`：批件与写作模式提取物归 `_Docs\_library\ethics\`，方案与知情同意随家族退役进 `{DEL}`。禁止再建 `_grants\2025\_ethics-forms\`（申报随附伦理表，清理时移 `{DEL}`）。

## 3 非课题 `_` 分支与台账
| 分支 | 放 | 不放 |
|---|---|---|
| `_teach\<topic-slug>\` | 教学语料（课件/病例/试题/模板）；slug 用英文小写连字符 | 课题原始影像 |
| `_med\{gcp,meeting,year-end,rules}\` | 医疗行政 | 科研数据 |
| `_books\<year>\` | 书稿/章节 | 课题原稿 |
| `_grants\<year>\` | 课题申请包（进行中与已结题；活兄弟根 `R&P` 禁止再建，→ 总图退役禁建表） | 本组期刊稿（走四阶段） |
| `_reviews\{peer,grants,thesis}\<year>\` | 他人稿 / 标书 / 毕业论文评阅（原 `R&P` 评阅侧） | 本组稿件（走四阶段） |
| `_personal\` | 个人材料（进修/签证） | 任何课题数据 |

- **硬规则：** 课题原始数据不得进 `_` 分支；`_` 分支不得被课题 `ref\settings.ini` 当数据源。
- **`目录说明.md`：** 每个 `_` 分支根与 `_lab` 根必须有（放什么、谁维护、更新日）；它是**活文档**——正文里作现行指令的路径与计数须与实盘一致，史证须同句带标记词，搬件 / 改名 / 计数变化当轮同步（门 → `QC.md` R11）。
- **`{RAW}\_diseases.csv`：** 列 `suffix,name_en,name_zh,l1,l2,aliases,family`；`suffix`=基码（无 `_\d+` 实例）；`family`=该基码所属家族根（留空=自家族；家族根必须在 `suffix` 列有本人行，如 `MHE`、`SCC`、`EC`、`THESIS`、`OTHERS`）；编号形式进 `aliases`；library `l1`/`l2` 对照 ethics/references。全称不进路径规则。`_diseases.csv` 复核：`RI` 挂 `SCH`（IR 数据随 SCH 队列）；`SCH\ly_RI` 只留 `目录说明.md` 为最终态（archived 同挂 SCH 口径）。
- **`{RAW}\_index.csv`（唯一可写台账）：** 一行一个 slug/分支，列 `kind,slug,prefix,suffix,title,l1,l2,stage,owner,indexed_on,note`；新建/改名当轮更新。
- **只读不变：** 除 `_index.csv` 外 `_DataBase` 默认只读；新建分支/子夹属写盘，须当轮点名（`My rule.md` §2 不豁免）。
- 不预建空夹。
可选：数据课题也可在上述子工程树内自建文件夹；约定写在该子工程内，不进全局 rules/skills。

## 4 家族桶落点（`_PHI` / `__zip`）

- **一句话（目标态，已落地）**：课题家族进 `{RAW}\Family\<family>\`。一个家族 = 身份桶 `_PHI\` + 原始件池 `__zip\` + 每个子工程叶内一个子库 `<slug>db`。全局词典唯一落点 `{RAW}\Family\dict.db`。学位原件目标落点 `__zip\thesis\<slug>\`；勿再新建 `_thesis`。`_PHI` 只放身份。非家族目录（`_grants` / `_lab` / `_med` / `_reviews` / `_teach` 等）留 `_DataBase` 根，不进 `Family\`；**`_work` 类工作区不再新建**，临时件一律落 `{DEL}`。
- **现行盘面（2026-11-28 已转正）**：26 个家族已在 `{RAW}\Family\<family>\`；`VEGF` 仅有家族库（`meta.no_data=1`，无子库）；`dict.db` 在 `{RAW}\Family\dict.db`。旧家族树已整体移入 `{DEL}\_by-function\db5t-build-20261128\retired-20261128\`；论文实体改挂 `__zip\thesis` 仍待另点名。
- **`<family>\_PHI\`（唯一 PHI 落点）**：放家族库 `<family>db`（有 PHI 家族：`meta` / `id` / `id_number` / `ref_project` 及既有 `ref_*`；**不留 `dict` 表**，格式真源改读全局 `{RAW}\Family\dict.db`）、冻结旧库 `<family>db_6t`、`目录说明.md`、可重建预览页；**不存业务表**。整桶不得外发、不得进任何仓、不得压包外送；外发只走子库（D28 零 PHI 通过后）。现行 D23 / S25 仍按旧五表（含家族 `dict`）做机器校验，待另批改 MY-CODES。
- **`<family>\__zip\`（原始件池）**：按子工程分夹 `<family>\__zip\<leaf>\`，放该叶原始件压缩档与随档清单 `<名>.files.txt`；随档非表格件（原始图 / 扫描记录 / 说明）同夹一层平铺，不建 `raw\` / `cohort\` 子夹。档内表格解出按「散表归并」入库，原档留本桶；桶根须自带 `目录说明.md`。
- **伦理材料不进 `_DataBase`**：申请包 / 方案 / 知情同意 / 批件按「伦理材料留存」归 `_Docs\_library\ethics\`；`_DataBase` 侧不设伦理桶：原件整夹退役进 `{DEL}`（带 sha256 台账），写作模式入库 `_Docs\_library\ethics\`。
- **勿再新建 `_thesis`**：学位论文 / 博士后 / 汇报稿原件目标落点 `<family>\__zip\thesis\<slug>\`；实体改挂待另点名。
- **越界即 P1**：库文件出现在 `__zip`（含 `thesis` 支）或叶根散落归档；PHI 出现在 `_PHI` 以外的落点；`_PHI` 里的家族库出现 `clin` / `qc` / `_modules_<mod>` 业务表。新建 `_thesis` 亦为越界。
- **写侧只认本节桶名**：不设兼容分支、不按别名兜底。旧桶名与旧表前缀出现在盘面或库内即 **P1 QC 发现**，按清理对象处理；`aliases.yaml` 的映射只用于识别与清理，不是读侧开关。
- **迁移先试点一个家族**：首批 `ACN`（压缩档与非归档件同时在册、`src` 表路径耦合最多）。单家族搬完 → 重写库内字面路径 → 复算 `src.sha256` → `gates.py <family> --cutover` 与 `align_check.py` 全 PASS → 台账登记（`family` / 桶 / 完成日 / 门禁结果 / 回滚点）→ 再按家族铺开；试点未过不批量搬。
- **库内路径随桶改名同批改**：`src.rel_path`（`blob:<family>/<桶>/…`）、`meta.source_db`、`meta.excluded_columns.source_sheet` 存的是字面路径，改名后须同批重写并复算 `src.sha256`；只搬目录不改这些值 = 悬挂引用（P0）。

## 5 家族库 `_PHI\\` 与子工程库（1+N）

- **位置（1+N，目标态）**：家族库 `{RAW}\Family\<family>\_PHI\<family>db`；子工程库 `{RAW}\Family\<family>\<slug>\<slug>db`（**扁平**，不建 `<slug>\_PHI\` 或 `<family>\_PHI\<short_code>\` 子夹）。层深见 `db-build-contract.md` 契 10。根级 `_DataBase` 与 `Family\` 下不设散落库桶。2026-11-28 已迁入 `Family\`（见上条「现行盘面」）。
- **目录内容**：`_PHI` 内放家族库 `<family>db`、并存期冻结旧库 `<family>db_6t`、`目录说明.md`，以及常驻、可重建的预览页；子工程叶内放 `<slug>db`、`目录说明.md`，同样允许可重建预览页。两处都不建 `raw\\` / `originals\\` / 日期子夹；并存期结束、旧库归档后，回到「库 + 说明 + 可重建预览」。预览页由库重生成，不是第二份库，也不得代替库文件；改库后必须重生成，否则页面数字是旧账。预览若含本地文件名或姓名，只留本机并标明禁止外发；不因页面做了脱敏开关就认为库已脱敏。
- **构建收尾与边车**：缺 `目录说明.md` = 构建未完成，不是可选项；build 脚本收尾按模板写骨架（家族库写管什么 / 身份与登记表且不留 dict，无 PHI 家族写 `meta` / `ref_project` 且不留 dict / PHI 只在此处；子库写零 PHI / 时点口径 / 可选模态）。SQLite 边车 `<库>db-wal` 与 `-shm` 同在 = 库正被打开 / 未 checkpoint（构建中，放行）；只有 `-wal` 无 `-shm`、跨一次构建仍在 = 上次写坏残留，记 **P1**（S25/S26）。
- **1+N：一库一工程**：每家族恰一个家族库 `<family>db`；每个子工程恰一个子库 `<slug>db`。短码 = 子工程 slug，靠 `ref_project` 与子库 `src` 区分，只表示项目归属，不是个体主索引；家族拆分时整树随 `<family>` 走。
- **可独立处理**：家族库与子库可分别备份 / VACUUM；子库在 D28「零 PHI」通过后可单独外发，家族库含 PHI 一律不得外发。
- **跨库唯一引用（有 PHI 家族）**：只靠 `family_uid`（形如 `ACN-000137`）。SQLite 无跨库外键，父子一致性由 `verify_db` 的 ATTACH 检查（D27/D34）承担。
- **现役骨架（5t，有 PHI 家族，目标态）**：家族库实表 `meta` / `id` / `id_number` / `ref_project`（及既有 `ref_study` / `ref_batch` 若已建）；**不留 `dict` 表**，格式真源改读 `{RAW}\Family\dict.db`。子库实表 `meta` / `src` / `person` / `clin` / `_modules_<mod>`（有模态数据则 ≥1 张）/ `qc`（六类）不变。`id` / `id_number` 是唯一 PHI 落点；`person` 是**无 PHI 占位表**（`family_uid` / `subject_label` / `id_status`），不存姓名 / 身份证 / 电话 / 地址。
- **机器门仍待另批**：现行 D23 / S25 仍按旧五表（含家族 `dict`）校验，本批不改 `gates.py` / `structure_check`。
- **家族库表口径**：`id` 存姓名 / 电话 / 身份证 / 地址 / `family_uid`（`^[A-Z0-9_]+-\d{6}$`）；各类号走 `id_number(kind, value)`（住院号 / 门诊号 / 影像号 / 病理号 / 样本号）；变量词典改挂全局 `{RAW}\Family\dict.db`（`role='phi'` 只许 `scope='family'`，细则 `db-build-contract.md`）；`ref_project` 登记子库清单与 `db_rel_path` / `built_at` / `sha256`。
- **无 PHI 家族用家族编码：** 家族库无 PHI 不建 `id` / `id_number` 身份表，家族库只留 `meta` / `ref_project`（不留 `dict`）；家族级登记改用家族编码（family code）+ `ref_project` 映射，子库在 `meta.family_code` 记所属家族编码，跨库引用用家族编码而非 `family_uid`；PHI 永不下沉子库。`id` / `id_number` / `family_uid` 及依赖它们的 D24 / D27 / D54 / D63 / D75 只约束有 PHI 家族。
- **汇编族（`OTHERS`）保留家族库、PHI 按子工程放置：** `OTHERS` 跨项目汇编，按有 PHI 家族对待：`_PHI\OTHERSdb` 保留 `id` / `id_number`，是 PHI 唯一落点，身份表不拆进子库；但身份不合并到家族级——每个 uid 恰属一个子工程（归属由子库 `person.family_uid` 唯一决定），不做跨子工程去重 / crosswalk / 统一主索引。家族库 `meta` 记 `family_code='OTHERS'`、`phi_layout='by_project'` 与子工程清单；子库在 `meta.family_code='OTHERS'` 记归属并保持零 PHI。「子库自带身份表、家族库退役」的判据（D86）不适用，与「PHI 永不下沉子库」冲突。
- **`ref_project` 四个计数**：`person_count`（person 行数，含占位）/ `clin_person_n`（有 ≥1 条 clin 行的人数 = **队列人数口径**）/ `longitudinal_n`（有 ≥2 个不同 `period_month` 的人数）/ `multi_record_n`（有 >1 条 clin 行的人数）。四列由门禁实时重算比对，任一不等即 **P0**（D35）；**对外只报 `clin_person_n`**。
- **家族级人数不报**：`id` 行数 ≠ 患者数，`person_count` 也不是队列人数。跨子库未解析时只报项目级 `clin_person_n`；`id` 行数只允许作「身份行数」出现在方法学附注（D36）。试点实测：LC 家族库 `id` 3,050 行，四个项目 `clin_person_n` 合计 2,234 人；非姓名证据判同一人为 0，故不提供家族级合计。
- **冻结旧库（core-6t）**：旧七表 `meta` / `project` / `src` / `item` / `val` / `person` / `person_key` 与兼容视图 `doc` / `sheet` / `sheet_dup` / `entity` / `fact` 只在 `<family>db_6t` 内保留，**只读**，供迁移对账；不得在旧库继续建表 / 改数，也不再按此骨架新建库。旧库 `meta.source_db` + `sha256` 须指向原始旧库并校验（D33）。
- **命名**：库文件 `<family>db` / `<slug>db`（均无扩展名；实例 `MHE_ANdb`、`lxj_ACNdb`）；冻结旧库 `<family>db_6t`（同目录、无扩展名、只读）。`_PHI` 与子工程叶内放「库文件 + `目录说明.md` + 可重建预览页」；说明须含口径 / 表结构 / 查询示例 / 重建步骤 / 限制 / `source_db` 对应关系（旧库名 + sha256）。
- **只收表格（去重合并结果）**：xlsx / xls / csv 等可解析的原始行列数据入库；入库即按「散表归并」去重合并（文件 sha → 整表 → 行级），同格式多份并入对应子库（`src.rel_path` + `src.sha256` 区分）；非原始数据不入库，口径 → 见 `db-schema.md`。库不是散表仓，不存原件、不存合并中间簿。**压缩档内的表格同样入库**：解出到 staging 后按同一条去重合并，档本身仍归 `__zip`。
- **压缩档本身不进 db、不留叶**：`*.tar.zst`、`7z`、`zip`、`gz`、`rar` 等归档一律进 `<family>\__zip\`（归位见「`__zip` 原始件池」）；**档内表格文件须解出、按「散表归并」入库**，档内非表格件（原始图 / 记录 / 文档）不入库；解包树校验后移 `{DEL}`，readme / 移动台账记「档→表」映射。
- **叶内只留 readme + 子库**：原表入库并校验后，叶内只留 `<slug>db` 与 `目录说明.md`（写入库日 / 项目 slug / 原件去向 / 未入库例外 / `source_db`+sha256）；不得留散表。`map.csv` 属台账例外。未入库件（PHI 花名册、模板、解析失败件）留叶并在 readme 写明原因，不得另存副本；**PHI 花名册只作迁移证据，不得并入子库**（迁移后按 D28 复核）。
- **原件留痕**：建库并校验通过后，原件移 `{DEL}\_by-function\<batch>\originals\<code>\<family>\<leaf>\`，写 `*-MOVED-YYYYMMDD.tsv`（相对路径 / 字节 / sha256）；原件不回流。
- **门禁**：`_PHI` 是 `_` 前缀桶，不参与 S23 桶/叶后缀校验。`structure_check.py` **S25** 校验家族库/子库落点与库文件（`<family>db` / `<slug>db` / 冻结 `<family>db_6t`、库头 SQLite、按 `meta.kind` + `schema_version` 分派 5t 家族表 / 子库六类表、根级 `_DataBase` 下不得出现库桶（目标态不留 `dict`，机器门待另批））；**S26** 允许叶内 `<slug>db`；**S27** 确认 `__zip` 不收库文件。`verify_db.py` 先按 `schema_version` 分派：旧 core-6t 仍跑 D1–D22，5t 跑 D23–D45（含跨库 ATTACH）。建库 / 迁移前后仍须全门 PASS。
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
- 策展后每叶只留一份现行源文件，内含长表与宽表（每表最多 5 个工作单）；子库内 `clin` 一张 + `_modules_<mod>` 按模态/特征域各一张（逐张登记 `dict`）+ `qc` 一张，口径见 `db-schema.md`。
- 细则（三类型判定、表头驱动解析、坑位清单、合并簿 sheet 约定）→ skill `db-library`。

## 6 `_DataBase` 可收
（≥20 散文件或小文件堆先 7z/zip + `.files.txt`，校验后散目录→`.Del`；见 §1（多文件先压缩）。）
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

## 7 `_grants` / `_reviews` 落点
- **课题申请包** → `_DataBase\_grants\<year>\`
- **评阅他人稿**（peer / grants / thesis）→ `_DataBase\_reviews\{peer,grants,thesis}\<year>\`
二者不是稿件流水线阶段：不要写入 `drafting` / `pre-submit` / `reviewing` / `accepted` 阶段表，也不进 `study_folder_stage_aliases`。本组期刊草稿 / R&R / 校样仍走四阶段夹（→ `zone-projects.md`）。`R&P` 活兄弟根禁止再建（→ 总图退役禁建表）。



## 8 台账落点（契约与回填）

建库产生的契约与台账，一律不进库内表。路径按目标态书写；建库过程中的临时台账落 `{DEL}\_by-function\<batch>\`（如 `db5t-build-20261128`），不留在家族目录。**库根与家族目录下不得新建 `_work`**：台账开工落批次目录，收口时只有 `map.csv` 随库进叶（叶内仍只留 `<slug>db`、`map.csv`、`目录说明.md`）。

| 台账 | 落点 | 谁写 | 谁读 |
|---|---|---|---|
| `map.csv` | 开工 `{DEL}\_by-function\<batch>\_work\<slug>\map.csv`；收口后随库到 `<family>\<slug>\map.csv` | 建库人 | `fill` / D95 |
| `qc_codes.tsv` | `{DEL}\_by-function\<batch>\_work\<family>\qc_codes.tsv` | 建库人 | D94 |
| `REVIEW-QUEUE.csv` | `{DEL}\_by-function\<batch>\_work\<family>\REVIEW-QUEUE.csv` | 停列时自动追加 | 用户 / D94 |
| `dict.db` | `{RAW}\Family\dict.db`（全局唯一） | 建库人 | 所有门禁与脚本 |
| `schema.sql` | `{code_root}\tools\db-library\db5t\schema.sql`（由 `schema-v1.md` 反编译，随代码仓提交） | `mkschema.py` | `newdb.py` |

规则：中文映射、单位换算系数、枚举对照只许出现在 `map.csv` 与 `qc_codes.tsv`，不得写进 `dict` / `qc`（`db-build-contract.md` 律 1）。`qc_codes.tsv` 已落盘 `{code_root}\tools\db-library\db5t\qc_codes.tsv`（2026-11-28，189 码），退役库 190 个历史码的去向记同目录 `qc_codes_retired.tsv`（`superseded_by` / `retired`）；新增码先登记再写库（`db-build-contract.md` 契 11.3）。
