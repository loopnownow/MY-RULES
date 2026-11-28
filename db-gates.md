---
name: db-gates
description: L1 子页：库门禁码表 D1–D99（手写口径；D95 / D96 / D98 已入 gates.py；D93 / D94 / D97 / D99 仍 report-only）。
up: My rule.md §5
generated: false
---

# 库门禁码表
- 管：D 码表（D1–D99）的口径记录。
- 不管：表结构与入表清洗（→ `db-schema.md`）；机器实现（`verify_db.py` / `gates.py`，判级以脚本为准）。

### 库门禁码表（D1–D99；D76–D86 判级以 `gates.py` 为准）

- **现行码（core-6t）**：`verify_db.py` 实有 `D1`–`D9`、`D19`–`D22`；判级细节以脚本为准，本表只记口径。
- **`D10`–`D18` 不存在**：总览里的 `D10` / `D12` / `D13` / `D14` 是人工注记码，脚本无实现；新码从 `D23` 起编，**不回填**旧号。
- **`D21` 为 P0**：明文 PHI **只许出现在家族库**，子库任何位置命中即 P0（`D28` / `D44`）。
- **分派**：旧 core-6t 库跑 `D1`–`D9`、`D19`–`D22`；5t 库按 `meta.schema_version` 跑 `D23`–`D99`（其中 D95 / D96 / D98 已机器化；D93 / D94 / D97 / D99 仍 report-only）。同一库不得混跑两套。

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
| D51 | 特征名折叠后同名多值 | P0 | `*_value.feature` 全小写、去尾点、`Shape.`→`shape_` 后不得再出现同名 |
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
| D87 | `id` / `clin` 结构指纹 | P1（先 report-only） | 指纹是**列名 + 列序**，不是行数：`id` 24 列、`clin` 头 11 列按名按序逐字比对（`SELECT name FROM pragma_table_info`），`clin.schema_block` 须为 `clin-v2`。列序不符即「物理序没重建」，靠 `ADD COLUMN` 加出来的库一律中招 |
| D88 | `dict` 覆盖与登记完整 | P1 | `id` / `clin` / `_modules_*` 每列须有 `dict` 行且 `full_name` 非空；定性列须有 `value_map`，数值列须有 `unit`。`clin` 一个 176 列的库只登记 30 行是常态，判据按「列 − 已登记」报数，不按比例 |
| D89 | 列名缩写合规 | P1 | 正则 `^[a-z][a-z0-9_]{1,30}$`；命中中文 / 大写 / `_\d+$` 后缀族 / SQL 保留字即报；`*_raw` 无 `*_canon` 配套只报数。缩写须在 `dict.full_name` 给全称，不靠猜 |
| D90 | 空值不挪位 | P2（`subject_label` 越界升 P1） | 统计占位词（`无` / `/` / `-` / `NA` / `?` / `0` 填充）与真 NULL 并存即报；`id.subject_label` 出现迁移后新写的号码或姓名升 P1。**空与「填了个占位词」在库里同形**，与 D44 / D52 同一类陷阱 |
| D91 | 病理长文本不得入 `clin` | P2 | 除 `path_dx` / `path_other` / `ihc_panel_raw` 外，`clin` 任一 TEXT 列 max 长度 >200 即报；`path_dx` >1000 字须有 `qc(PATH_DX_LONG)`。只报数：先把长列点出来，再决定拆哪一列 |
| D92 | 入表清洗残留 | P2 | 值内嵌单位（`\d+\s*(mm|cm|%)`）、`值+单位` 与 `号+名` 拼接串、全角数字、`#VALUE!` / `#N/A` 公式残值、行内换行、首尾空白；逐列报数。实测 `lvsi0` 里 108 个 `#VALUE!` 与 `g分级` 的 `I/高/1/0` 混装都属此类 |
| D93 | 参考区间软门 | 只报数（尚未机器化） | 对 `ri_normal` 软判：`OUT_OF_RI` / `UNIT_SUSPECT` / `IMPLAUSIBLE`。单侧区间不得判单位。基线不是失败阈值：121 列 pass 27 / OUT_OF_RI 61 / IMPLAUSIBLE 5 列 71 值。 |
| D94 | qc.code 受控 | report-only | `qc.code` 须在 `{code_root}\tools\db-library\db5t\qc_codes.tsv`（code/severity/meaning/since）登记。2026-11-28 词表落地 42 码；未登记码只报数、不判级（翻 P1 前先把码补齐）。旧库 190 码中与清洗无关的历史码不强制入表。 |
| D95 | dict 覆盖契约 | P1（默认 report-only，`--strict` 转 P1） | 物理列（除 `meta` / `dict`）须在 `{RAW}\Family\dict.db` 有行；`dtype` 与存储域不矛盾；scope 解析顺序见 `db-build-contract.md` 契 3。 |
| D96 | 计数守恒 | P1（默认 report-only，`--strict` 转 P1） | `Σ clin.merged_n = Σ src.rows`（`src.status='active'`）。 |
| D97 | 列格式纯度 | 尚未机器化 / report-only | 按域判混合；禁 `typeof` 四类占比（曾误报 32 列）。基线：真混合 0 列。 |
| D98 | 命名与外置单位 | P1（默认 report-only，`--strict` 转 P1） | 标识与业务字符串须 ASCII（律 1）；列名不得内嵌单位。基线：中文列名 379、大写 124、单位内嵌 194、值内糊单位 4 处（见契约）。 |
| D99 | 枚举值域 | 尚未机器化 / report-only | 取值须落在 dict `enum_values`。基线：`id.sex` 41,060 NULL 且 8 种写法混装（细分见契约），入库时归一。 |

- **机器点**：`D1`–`D22` 在 `verify_db.py`（`{code_root}\tools\db-library\verify_db.py`）；`D23`–`D99` 的 5t 实现落 `{code_root}\tools\db-library\db5t\gates.py`（跨库项用只读 `ATTACH` / `file:?mode=ro` 打开家族库），判据用的 SCHEMA / 全局 dict 由 `db5t\paths.py` 解析（`DB5T_BATCH` / `DB5T_ROOT` / `DB5T_SCHEMA` / `DB5T_DICT`）。**文档编号与代码输出必须逐条对应**（已入 `gates.py` 的码）。`D95` / `D96` / `D98` 代码已入，判级为 P1 但**默认 report-only**（输出 `· 待修(report-only)`，`--strict` 或 `DB5T_GATES_STRICT=1` 才写 `!! P1`），过渡期与翻级条件见 `db-build-contract.md`「过渡期口径」；`D93` / `D94` / `D97` / `D99` 恒 report-only，不是已生效 P1。
- **`D76`–`D86` 未入表**：`D76`–`D79`（模块派生句 / 旧库迁移句）、`D80`（PHI 拼接串）、`D81`、`D82`（`dict.source` 债）已在 `gates.py` 实现并出报告，本表只记到这里；新码从 `D87` 起编，**不回填** `D76`–`D86` 行，免得文档与脚本各写一套口径。
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

