---
name: db-schema
description: L1 子页：家族库 / 子库表结构、id v2、clin v2、病理段、入表清洗、DICOM 映射（P2、P3）。
up: My rule.md §5
owns: [P2, P3]
---

# 库表结构与 DICOM 映射
- 管：项目业务表、`id` v2、`clin` v2、病理段、入表前清洗、DICOM 来源的 PHI 映射（§P2）、伪匿名标识（§P3）。
- 不管：PII 总闸（→ `My rule.md` §P1）；D 码与门禁码表（→ `db-gates.md`）；家族桶与 `_PHI` 落点（→ `zone-database.md`）。

### 项目业务表（`clin` + `_modules_<mod>` + `qc`；不再按长/宽各一限表）

- **范围**：约束的是每个**子工程库**的业务表，不是家族库骨架。家族库只存身份、号、字典与子库登记（`id` / `id_number` / `dict` / `ref_project`），不存项目业务表。子库业务表 = `clin` 一张 + `_modules_<mod>` N 张（每模态/特征域一张，须在 `dict` 登记）+ `qc` 一张；`person` 是占位表，不是业务表。「每项目至多长表与宽表各一」不再适用。
- **现行源文件**：每个叶只保留一份现行源文件，且须是一份工作簿，不得长表、宽表各放一个文件。该文件内为长表与宽表；无内容的一侧省略，空席不垫。现行骨架仍是本文件的 5t（家族五表 / 子库 `clin` / `_modules_<mod>` / `qc` 等），不得用精简登记册或 blob 库骨架替换。每张表最多 5 个工作单；工作单名可用 `clin` / `_modules_<mod>` / `qc` / `analysis`，入子库后固定落到 `clin` / `_modules_<mod>` / `qc`，**不得按工作单另开表**。
- **表族三组、各管一段**：`clin` 是唯一「人 × 时点」主表；`_modules_<mod>` 只收不宜拉长的矩阵（组学 / 谱图 / ICC / 相关矩阵 / 影像组学）；`qc` 只收门禁结果与人工裁决。三组之外要建表，先在本节登记再建，不靠临时命名。
- **表名与语义固定**：临床特征表名 `clin`（`cln` 只作别名，不建表）；`_modules_<mod>` 收计算测量（影像、影像组学、谱图、连接 / 网络指标、代谢组）；`<mod>_val` 是 values 长表（`exam_uid` / `entity` / `feature` / `value` / `unit`），与 `_modules_<mod>` 的「一次检查一行」配对，**不是验证子集**——删 `*_val` 等于删全部模块测量值（实测 EC `radi_val` 568,106 行、全库 `*_val` 6,775,401 行），禁止。
- **量表进 `clin`，指标进模块**：问卷 / 量表 / 认知条目（PSQI、PQSI、TST、SE、SOL 等）是「人 × 时点」临床特征，落 `clin` 列；由影像或信号算出的标量指数（ALPS 等）落 `_modules_<mod>`。同一源表两类列并存时按语义拆表，不混表、不两边并存。
- **验证组是列不是表**：训练 / 验证划分落 `clin` 的 `group_v`（或 `cohort` / `group_raw` / `group_canon`）列，须在 `dict` 登记 `role='group'`；不建队列表、不删数据、不以文件名区分。
- **拆表留痕**：按语义拆表须在 `dict` 逐表登记列，并在子库 `meta.business_tables` 列全表名；`src` 源行保留。
- **`clin` 的派生句窄例外**：`clin` 默认要求 `dict.source` 可追原件（`blob:` 形态）；由行序 / 行号 / 计数 / 归一等得到的**结构派生列**（如 `visit_no` / `row_ix` / `group_raw` / `dx_n`）允许写 `派生：…` 句，但句内必须点名依据（源表 / 源列 / 行序 / 条数 / 归一 / 重编码）；泛泛的「派生：见源表」仍按债计。门禁只报数（D82 输出「clin 结构派生 N 行」），不判债。
- **`clin` 旧库迁移列**：家族确有迁移前旧库快照（`{DEL}\_by-function\<批次>\_work\...\ledger8\backup\<日期>\<FAM>db`）时，某列若只能定位到「旧库迁入」、列级原件未登记，允许写 `派生：旧库迁移——家族自 <FAM>db@<日期> 迁入，列级原件未登记（待回原件核对）`；句内必须点名快照库与日期，且只在该快照确实存在时允许；点名了具体工作簿的列不得用此句。门禁只报数（D82 输出「clin 旧库迁移 N 行」），不判债。
- **模块表正文列的派生句**：`_modules_<mod>` 不是 `clin`，但它的**正文列**若由 `clin` 列整理（合并 / 归并 / 重编码）、或由迁移前旧库 blob 而来，允许写 `派生：由 clin.<列> 整理（…）` / `派生：由 blob:<地址> 迁移（…）`；句内必须点名来源列或 blob 地址，泛泛的「派生：见源表」仍按债计。门禁只报数（D82 输出「模块正文派生 N 行」），不判债。
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

- **只收原始行列数据**：入库的只是原始矩形数据（行 × 列）。论文统计与作图结果、伦理材料、通讯录、汇报稿、方法说明及其他非原始数据不进库。相关分析系数 / p 值 / 模型指标 / 作图数据等可复现统计内容写 `{DEL}` 交接文档（脚本入口一并登记），不进库、不占 `_modules_<mod>`；库内只留原始测量值与 `dict.source` 派生句（D82）。**`dict`（变量字典）与 `qc`（门禁日志）自 5t 起是正式表，不受「不得占用第三张库内表」限制**；但只登记字典与门禁结果，不得借道塞业务数据。伦理材料仍不进库（旧 core-6t 由 D19 拦；5t 库里伦理材料不得进入 `dict.source` / `ref_project.slug` / 子库 `src.rel_path`）。
- **版本链**：计算 / 校正 / old / copy 等版本只把现行 `clin` / `_modules_<mod>` 纳入定稿，其余留子库 `src.kind='workbook'` 的源表（保留 `rel_path` + `sha256`）。
- **角色与源表**：5t 子库 `src.kind` 只许 `old_db`、`workbook`、`archive_member`，保留 `rel_path` + `sha256`，不得删除 `src` 行。冻结旧库的 `src.role`（兼容视图 `sheet.role`）仍只许 `raw` / `curated` / `derived`，定稿标 `curated`、来源留 `raw`、`derived` 只留 blob 不写 `val` / `fact`（`verify_db` D22，仅旧库适用）。
- **写库**：把 `clin` / `_modules_<mod>` 写入子库（身份字段写家族库 `id` / `id_number`）或 `{RAW}`，以及 `--apply` / `--move`，须当轮点名；缺省 dry-run。写盘总闸见 `My rule.md` §2。
- **外发边界**：家族库含 PHI，**一律不得外发**；子库在 D28「零 PHI」通过后才可单独外发。业务表中的敏感字段与记录键不得写入聊天、记忆、备忘录、规则正文或回执（见 `My rule.md` §1.2）。

### 身份表与病理段（`id` v2 · 病理拆分 · 入表前清洗）

家族库 `_PHI\<FAM>db` 仍是五表（`meta` / `id` / `id_number` / `dict` / 家族级 `ref_*`），**不因病理信息加表**：D23 与结构体检按五表校验，加第六表须先改门禁与 SCHEMA，不能顺手建。

#### `id` v2：24 列、物理列序固定

| # | 列 | 类型 | 口径 |
|---|---|---|---|
| 01 | `family_uid` | TEXT PK | `^[A-Z0-9_]+-\d{6}$`（D24） |
| 02 | `patient_id` | TEXT | 家族内业务主键，一人一号、终身不变；不对外、不作 join 键 |
| 03 | `subject_label` | TEXT | **原样兼容列**：只留迁移时的原值，**不再写新值**，不得承载姓名或新号码 |
| 04 | `name` | TEXT | 中文姓名，形态见「入表前清洗」 |
| 05 | `name_pinyin` | TEXT | 大写、单空格分隔；`1-CAO-YAN` 这类「序号-姓名」串拆开，序号进 `patient_id` |
| 06 | `sex` | TEXT | `M` / `F` / `U`（`男`/`1`→`M`，`女`/`2`→`F`） |
| 07 | `birth_date` | TEXT | ISO 8601；只有年月写 `YYYY-MM` 并在 `note` 记精度 |
| 08 | `id_card` | TEXT | 脱敏：前 3 + 11 个 `*` + 后 4；末位 `X` 大写；**不存明文** |
| 09 | `phone` | TEXT | 脱敏：前 3 + `****` + 后 4；13 位「区号-号码」先规范化再脱敏 |
| 10 | `address` | TEXT | 只到区 / 县，不存门牌 |
| 11–18 | `inpatient_no` / `outpatient_no` / `mrn` / `imaging_no` / `pathology_no` / `sample_no` / `study_uid` / `misc_id` | TEXT | 一人一号一位；同种多号、多 issuer 一律进 `id_number`（D25 / D75） |
| 19 | `id_status` | TEXT | `keyed_full` / `keyed_partial` / `label_only` / `label_only_omics`（沿用 D63 三元） |
| 20 | `identity_state` | TEXT | `resolved` / `unresolved` |
| 21 | `source` | TEXT | 本条身份的来源登记（`blob:` 或表名 + 日期） |
| 22–23 | `created_on` / `updated_on` | TEXT | `YYYY-MM-DD HH:MM:SS` |
| 24 | `note` | TEXT | 别名、精度、迁移说明；不放业务信息 |

- **一列一号、余号进 `id_number`**：`id` 每类号只放一个，其余全部落 `id_number(family_uid, kind, issuer, value)`；`kind` 白名单随 v2 扩为 `inpatient` / `outpatient` / `mrn` / `imaging` / `pathology` / `sample` / `study` / `other`（`other` 是既有主力号种，实测 8,588 行，**不得改名**；`misc` 只作列名，不作 `kind`）。同号在不同 `issuer` 是不同号（D75）。
- **`subject_label` 是兼容列不是键空间**：EC 实测 1,447 个非空值里拼音 747、号名混装 326、纯数字 9、其他 365；**禁止**回填、禁止据此 join（D90 兜底）。
- **只许重建、不许 `ALTER` 改序**：`ADD COLUMN` 只能追加到末尾，物理序 24 列只能靠 `CREATE TABLE id_v2(…)` → `INSERT … SELECT` → 换名 → 重建 `id_number` 外键；动土前 `VACUUM INTO` 全库备份、`PRAGMA integrity_check`、落盘后逐列核行数与空值数（空值数变化 = 搬串列了）。

#### `clin` v2：头 11 列与 legacy 三元组

- **头 11 列固定、按名按序**（D87）：`family_uid` / `observed_on` / `period_month` / `cohort` / `group_v` / `subgroup` / `src_id` / `src_row` / `merged_n` / `unk_seq` / `schema_block`（取值 `clin-v2`）。其后是 legacy 三元组 `month_ix` / `period_source` / `period_origin`，再后才是变量列（小写缩写、按字母序）。
- **legacy 三元组留在变量区、不删**：`month_ix` 撑着 `ix_clin_month` 与 D29；`period_source` 记时间来源（迁移时放开 `NOT NULL`）；`period_origin` 是唯一证据（OTHERS `ybc_BONETUMOR` 5,052 行 `'0'` 占位，清洗成 NULL 前不得删列）。
- **`group_v` / `subgroup` 由变量列升为头列**：迁移时同名旧列并值进头列（头列统一 TEXT，`0.0` 记 `'0'`，类型转换行数记 `meta.clin_v2_type_cast`），旧列不再保留；旧 `schema_block` 值被吸收。
- **15 个 `path_*` 列在重建时一次建空列**，不二次重建宽表；`ihc_*` / `ihc_panel_raw` 待拆列时 `ALTER ADD` 到表尾，不触动头 11 列。
- **只许重建、不许 `ALTER` 改序**（同 `id` v2）：旧头 → v2 头只能 `CREATE TABLE clin__v2(…)` → `INSERT … SELECT` → 换名 → 重建索引 / 触发器；头列与变量列的顺序漂移由 D87 报数。

#### 病理段：拆分入表，原文不入库

- **落点**：病理与免疫组化结论进子库 `clin` 的 `path_*` / `ihc_*` 列；**病理号进 `id.pathology_no`**（多号进 `id_number`）；报告原件与扫描件留 `__zip\<FAM>\<叶>\`，不拆句进库。家族库不加表（见上）。
- **原文为什么不留库**：① 家族库五表不动（D23）；② 子库零 PHI（D28）——EC `EC病理.zip` 508 个成员中 499 张 jpg 的文件名带人名；③ 长文本正是现有门禁的盲区：D54 只比「整格 == 某个号」，D80 只认 ≤60 字的「姓名(号码)」拼接串，**1,200 字的报告全文两边都漏**；④ 全文不可分析，只增加查找负担。回溯靠 `clin` 头已有的 `src_id` + `src_row`，不靠另存一列。
- **列族（小写 ASCII，按字母序）**：一人多份报告取最近一次进 `clin`，历史份不进库、留原件。

| 列 | 值域 | 说明 |
|---|---|---|
| `path_kind` | `curettage` / `surgery` / `biopsy` / `review` | 诊刮 / 手术 / 活检 / 复核 |
| `path_on` | ISO 日期 | 报告日期（**不是**手术日；手术日另列 `surgery_on`） |
| `path_histology` | enum | 内膜样腺癌 / 浆液性 / 透明细胞 / 黏液性 / 癌肉瘤 / 其他；源文本映射进 `dict.value_map` |
| `path_grade` | 1 / 2 / 3 | 组织学分级，源里 `I` / `II` / `高分化` / `1` 一律映射；诊刮与手术分级不一致时并存 `path_grade_curettage` / `path_grade_surgery`，不取其一 |
| `path_mi` | 0 / 1 / 2 | 无 / 浅（<1/2）/ 深（≥1/2）；毫米值另列 `path_mi_mm` |
| `path_lvsi` | 0 / 1 | 脉管癌栓 |
| `path_csi` | 0 / 1 | 宫颈间质浸润 |
| `path_ln_pos` / `path_ln_total` / `path_lnm` | int / int / 0-1 | 阳性数 / 检出数 / 是否转移；`path_lnm` 必须与 `path_ln_pos > 0` 一致 |
| `path_eu` | 0 / 1 | 宫外转移（附件 / 腹膜 / 大网膜 / 膀胱直肠） |
| `path_figo` | `IA` / `IB` / `II` / `IIIA` … | 病理分期；临床分期另列 `clin_figo`，不得同列混装 |
| `path_dx` | TEXT ≤1000 | **清洗后的诊断结论句**（去姓名 / 号码 / 医师 / 日期）；不是报告全文，超长须继续拆字段并记 `qc(PATH_DX_LONG)` |
| `path_other` | TEXT ≤200 | 拆不动的合并发现（肌瘤 / 腺肌病 / 囊肿）；不得装大体描述或镜下描述 |
| `ihc_<marker>` | 0-3 或 `neg` / `pos` | ER / PR / P53 / Ki-67 / P16 / CK7 / Vimentin / MLH1 / MSH2 / MSH6 / PMS2 / PTEN；强度 0-3，百分比进 `ihc_<marker>_pct`，P53 野生 / 突变 / 缺失进 `ihc_p53_state` |
| `ihc_panel_raw` | TEXT ≤300 | 原始半定量串（如 `CK7(+)/ER(90% 强)/PR(-)`），**只作溯源**；必须有对应 `ihc_*` 列，不得只有它不拆 |

#### 入表前清洗（`id` 与 `clin` 同规）

- **值先归位、再入库**：入表前逐列过「形态 → 枚举 / 数值 / 空」；形态不合法即 NULL + `qc(VALUE_DIRTY, P2)`，不许原样入库等下游猜。EC 实证脏值：`g分级` 混 `I` / `II` / `III` / `高` / `1` / `0`；`lvsi0` 有 `#VALUE!` 108 个与句子碎片；`诊刮` 有 `/`、`无`、`0` 与自由句。
- **数值列不带单位**：单位进 `dict.unit`，不得写进列名或值；「值 + 单位」拼接串按 D92 报数。
- **定性列不留自由文本**：值域须在 `dict.value_map` 有映射；映射不上的不许自造枚举，宁可 NULL 并记 `qc(VALUE_UNMAPPED)`。
- **空值不挪位**：空就是 NULL，不写 `0` / `无` / `/` / `-`，不把 A 列缺失挪进 B 列（D90 从 `id` 扩到 `clin` 全表）。
- **同义列先归一**：全库 103 个病理同义列（`figo_raw` / `figo_canon` / `figo_stage` / `FIGO stage`、`mi` / `nmi` / `smi` / `肌层1`、`p53` / `p53_status`、`ki67` / `Ki67` / `ki67_status` …）入表前映射到规范名；`*_raw` 只作溯源列，必须有 `*_canon` 配套。
- **列名规范**：`^[a-z][a-z0-9_]{1,30}$`；禁中文列名、禁 `_数字` 后缀族（D48）、禁 SQL 保留字（D89）。
- **`dict` 全覆盖**：每列入 `dict`（全称 / 单位 / 参考范围 / 值域 / `source`），缺行即 D88。

#### 门禁

D87 标准指纹 / D88 `dict` 覆盖 / D89 缩写合规 / D90 空值不挪位 / D91 病理长文本报数 / D92 入表清洗报数。初版一律 **report-only**，跑满一个批次无新债后再转 P1。

# DICOM 与伪匿名
**§P2** **DICOM 来源的 PHI**：以 DICOM 头为源，只进家族库——`PatientName`→`id.name`、`PatientID` / `OtherPatientIDs` / `AccessionNumber`→`id_number`、`PatientBirthDate`→`id.birth_date`、`PatientSex`→`id.sex`、`PatientAddress`→`id.address`、`PatientTelephoneNumbers`→`id.phone`。
- `InstitutionName` / `ReferringPhysicianName` / `OperatorsName` 不进子库；子库只留模态、扫描参数与 UID。
- **§P3** 伪匿名标识（`ANON*` / `XXX` / `TEST` / 纯数字 / 单字符重复）不得当真名、不得据此合并身份；一头多姓名或一姓名多头各建身份并记 qc，不合并。
- 像素内烧入的文字属无法自动剥离的 PHI，外发前须人工复核。
- DICOM 头与院内名单冲突时以头为准并记 `qc(DICOM_NAME_CONFLICT)`。判级见 `db-gates.md` D56–D58。
