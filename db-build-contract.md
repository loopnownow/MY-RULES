---
name: db-build-contract
description: L1 子页：建库契约（契 1–10、律 1–5）、全局 dict、新库目录目标态。
up: My rule.md §5
---

# 建库契约（契 1–10）

- 管：新库从零建的硬约束（契 1–10、律 1–5）、全局 `{RAW}\Family\dict.db`、目录目标态、决策基线。
- 不管：既有表结构细目与 DICOM 映射（→ `db-schema.md`）；D 码正文（→ `db-gates.md`，D93–D99 尚未机器化）；家族桶与台账落点（→ `zone-database.md`）；做法（→ `{SKILLS}\02_data-processing\base\db-library\references\load-pipeline.md`）。
- 分工：本节说必须怎样，门禁说怎么判，流水线说怎么做。D93–D99 只在 `db-gates.md` 写判据，本节只引用编号。

本节约束「新库从零建」。现行盘面的家族树、家族库 `dict` 表与 `_thesis` 夹，在另点名搬迁 / 重建之前可以仍在旧位；本文件不把搬盘或重建写成已执行。

## 决策基线

本轮给定，作新库口径；不在本文件改 `id_number.kind`，也不把试点重建写成已做：

| # | 口径 |
|---|---|
| 1 | 多时点白名单只有 `SCH/js_SCH`、`PAH/lxf_PAH`；`zjl_RDL` 数据不动，另加 meta 例外位。不得由任意库自行设 `multi_visit_exempt=1`。 |
| 2 | `ybc_BONETUMOR` 与 `ybc_STWZ` 零交集（3,422 vs 590 人），不是同一队列；改名归档 `ybc_BONETUMOR_screen`，标 `kind=screen_pool`，不删。 |
| 3 | 不设同月多次检查；随访按「间隔 ≥6 个月一次」；术前 / 术后按实际时间。 |
| 4 | `dict` / `qc` 不放映射（中文）；映射在入库前解决（`map.csv` 台账）。 |
| 5 | 「列名与值语义不符」算停列第 6 类。 |
| 6 | 目标态：`dict` 升级为全局单表 `{RAW}\Family\dict.db`；28 个家族进 `{RAW}\Family\`。搬目录与建该库待另点名。 |
| 7 | 试点重建现库、开工前备份（不用影子库）是待另点名的操作口径；本批未备份、未重建、未改现行家族 `.db`。 |
| 8 | DB 数据按实际填写，参考区间只是软门（D93 基线数字只报数，不是失败阈值）。 |
| 9 | `NLR` / `PLR` 要有 `canonical_id`（`lab.nlr` / `lab.plr`，`role=derived`，`unit=ratio`）。 |
| 10 | `dict` 重构，新增 `canonical_id` / `unit_si` / `enum_values` 三列。 |
| 11 | `id_number.kind` 增加 `accession` 为单独一批，本文件与本批不改 kind 白名单。 |
| 12 | `sex` 值域在入库时处理。 |
| 13 | 枚举值域门禁单开 D99（尚未机器化，report-only）。 |
| 14 | 家族库不留 `dict` 表；目录保持双下划线 `__zip`；勿再新建 `_thesis`，论文目标落点 `__zip\thesis\<slug>\`。实体改挂待另点名。 |
| 15 | `_PHI` 只放身份；`clin` / `_modules_*` / `qc` 零 PHI，用 `family_uid` 引用。 |

## 契 1 三份契约先于第一个字节

新建一个子库，先冻结三份契约，缺一不许建表、不许导数据：

1. **`<slug>.map.csv`**：源列 → 目标列的逐列契约，13 列固定（见下表）。
2. **`qc_codes.tsv`**：`qc.code` 受控词表，家族级台账，新增码必须先在词表登记。
3. **`schema.sql`**：结构唯一真源，由 `schema-v1.md` 反编译生成；手工改库不算建库。

| 列 | 必填 | 含义 |
|---|---|---|
| `src_file` | 是 | 源文件名（不含路径） |
| `src_sheet` | 是 | sheet 名或 `-` |
| `src_header_row` | 是 | 表头所在行号（1 起）；多行表头写起始行 |
| `src_header` | 是 | 源列名原文（允许中文，**这是唯一允许中文的地方**） |
| `src_column` | 否 | 多行表头拼接后的子列定位，如 `行1\|行2` |
| `target_table` | 是 | `clin` / `person` / `_modules_<mod>` / `<mod>_val` |
| `target_column` | 是 | 目标列名，ASCII snake_case |
| `dtype` | 是 | `REAL` / `INTEGER` / `TEXT` / `DATE` / `enum` |
| `unit` | 否 | 目标单位代码（外置，不写进列名）；无单位写 `-` |
| `enum_values` | 否 | 英文枚举，竖线分隔（如 `M\|F\|U`）；非枚举写 `-` |
| `missing_rule` | 是 | `null` / `na` / `pending` |
| `transform` | 否 | 声明式变换，见契 2；无变换写 `-` |
| `expect_rows` | 是 | 该源列期望落库的非空行数，收口时对账用（契 6） |

`map.csv` 是入库前的台账，不是库内表：中文映射、枚举对照、单位换算系数都写在这里，永不写进 `dict` 或 `qc`（律 1）。台账落点 → `zone-database.md` §8。

`qc_codes.tsv` 口径：以首发 16 码为底（清单见 `{SKILLS}\02_data-processing\base\db-library\references\load-pipeline.md` §1.2），旧 190 码按 `superseded_by` 归一。完整词表文件待另文件落盘，本文件不编造 190 码对照表。

## 契 2 五条硬律

### 律 1 仅英文

库内一切可读标识与取值必须是 ASCII：

- 表名、列名、枚举值、单位代码、`qc.code`、`meta` 的键与值、文件名：ASCII snake_case。
- 业务表字符串值：100% ASCII。病理 / 量表原文不入库；需要保留原文时，靠 `src_id` + `src_row` 回指源文件。
- 中文原名只出现在两处：源文件本身、`map.csv` 的 `src_header`。
- 违反即 P1（D98；该码尚未机器化，report-only）。

### 律 2 单一格式

一个目标列只放一个域：numeric（`REAL` / `INTEGER`）/ text / date / enum。
判据：该列非空值里同时出现「可转数值」与「不可转数值」即违规；`INTEGER` 与 `REAL` 混在同一 numeric 列合规；`NULL` 不参与判定。
「数值列里塞 `1.2 (3)` 这种带注释的字符串」属违规，注释拆到 `*_note` 列。

### 律 3 列内禁混

同一目标列内禁止混：语言、单位、尺度、编码、时点。粒度是**列**，不是库——跨批次、跨来源可以进同一个库，只要同一目标列不混。
同一列出现两种单位且无法声明换算（如 DDimer `mg/L DDU` 与 `mg/L FEU`）→ 停列送审，不许自行换算。

### 律 4 dict 是格式真源

`{RAW}\Family\dict.db` 的 `dict` 表是唯一格式真源。目标列的 `dtype` / `unit` / `unit_si` / `enum_values` / `missing_rule` / `canonical_id` 以 dict 为准：

- `map.csv` 与 dict 不一致 → 停，先裁决改哪边。
- dict 里没有该列 → 不许 ALTER，先补 dict 行。
- dict 行通过 `source='map:<slug>#<n>'` 指回 map.csv 行号。

建该全局库与让既有脚本改读它，待另批改 MY-CODES；本批只定文档口径。

### 律 5 不可决即问（六类停列）

命中任一类，**停该列**并做三件事：写 `qc(code='PENDING_REVIEW', status='open')`、在 `REVIEW-QUEUE.csv` 加一行、当轮问用户。禁止猜默认值、取中位、先到者胜、写 NULL 掩盖、按姓名合并。

1. 枚举值在词表里找不到对应英文；
2. 单位不可换算或换算系数随试剂变化；
3. 同一人同一变量两值不等（同人同变量，不是同人不同时点）；
4. 字段语义不明（不知道这一列代表什么）；
5. 时点不明（有值无日期、日期与检查不符、`period_month` 与 `observed_on` 矛盾）；
6. 列名与值语义不符（典型：列名是 `tp`，值是病理类型文本）。

## 契 3 dict 表结构（全局唯一）

```sql
CREATE TABLE dict (
  scope        TEXT NOT NULL,   -- 'stage' | 'family' | 'proj:<slug>'
  table_name   TEXT NOT NULL,
  column_name  TEXT NOT NULL,
  role         TEXT,            -- key / outcome / value / score / derived / id
  dtype        TEXT,            -- REAL / INTEGER / TEXT / DATE / enum
  aliases      TEXT,            -- 英文别名，竖线分隔；禁中文（律 1）
  unit         TEXT,
  unit_si      TEXT,
  enum_values  TEXT,            -- M|F|U
  canonical_id TEXT,            -- 对齐 lab-ref-ranges，如 lab.creatinine / lab.nlr
  source       TEXT,            -- 'map:<slug>#<row>'
  missing_rule TEXT,            -- null / na / pending
  description  TEXT,
  added_on     TEXT,
  PRIMARY KEY (scope, table_name, column_name)
);
```

- `scope` 三级，解析优先级 `proj:<slug>` → `family` → `stage`。
- `stage` 放所有子库共有的骨架列（`clin` 11 个头列 + 15 个 `path_*`、`person` / `qc` / `src` 全列）。
- 家族库不再有 `dict` 表；目标态下 D88 / D95 与脚本读全局表（`DB5T_DICT`）。现行 `gates.py` 尚未改读该表。

## 契 4 每格可回溯

每个业务表行必须能指回源文件的具体格子：`src_id`（`src` 表主键）+ `src_row`（源行号，1 起）。

- 多行表头：还要能指到子列（`src_column` 记 `行1|行2`）。
- 人工勘误：原值永不改，clin 取最后修订版，指到该单元格；修订过程记 `qc(code='SUPERSEDED')` + 台账。
- 拼表 / 合并产生的行：`merged_n` 记来源行数，Σ`merged_n` = 源记录数（契 6）。

## 契 5 身份先于值

先建身份、再填值。顺序不可颠倒：身份聚类错，后面所有值都挂错人。

- 身份键只认 `id_number`（`kind` 白名单见 `db-schema.md` 身份表节）；姓名只进 `id.name`，不参与判重（D41）。
- 伪匿名编号不得当真名；9 段占位可多人共用，不判冲突。
- `id.sex` / `id.birth_date` 入库时归一：`M` / `F` / `U`，日期 ISO。非 `M` / `F` / `U` 的 `sex` 一律停列送审（D99，尚未机器化）。

**PHI 边界（硬）**：`_PHI\<FAM>db` 的 `id` / `id_number` 是唯一允许放姓名、电话、身份证、地址的表；子库 `clin` / `_modules_*` / `qc` / `*_val` 一律零 PHI，跨表引用只用 `family_uid`。

## 契 6 计数守恒

收口时必须满足：`Σ clin.merged_n` = `Σ src.rows`（`src.status='active'` 的行）。
不等就是丢行或多行，先查清再收口，不许用「大致相等」放行。判据见 D96（尚未机器化，report-only）。

## 契 7 冲突一律停列

同一目标列的来源之间出现分歧（值不等、单位不同、编码不同、时点不同），不许在库内择一：

1. 该列停止回填；
2. `qc(code='PENDING_REVIEW', status='open', note=冲突摘要)`；
3. `REVIEW-QUEUE.csv` 一行：`review_id, family, slug, uid, column, src_a_src_id, src_a_row, src_a_value, src_b_src_id, src_b_row, src_b_value, rule, raised_at, resolution`；
4. 当轮问用户。

## 契 8 三类「没有」必须可分

| 情形 | `clin` 表现 | `missing_rule` |
|---|---|---|
| 未采集 | 该人无对应行 | — |
| 采了但缺 | 有行、该列 `NULL` | `null` |
| 不适用 | 有行、该列 `NULL` 且 `missing_rule='na'` | `na` |

禁止用 `0` / `未知` / `空字符串` 冒充缺失。插补只在分析层做，库内不填。

## 契 9 时点模型

`meta.period_unit` 三值，建库时必填：

| 值 | 含义 | 判据 |
|---|---|---|
| `singleton` | 单一时点（默认） | 一人一行 |
| `followup_6m` | 随访，间隔 ≥6 个月 | 相邻两次 `period_month` 月差 ≥6；首次基线可任意 |
| `peri_op` | 术前 / 术后 | 一人最多两行，`visit_kind` ∈ `preop` / `postop`，按 `observed_on` 排序 |

- **不设同月多次检查**：同一人同一月出现两行 → 停列送审，不许自行合并。
- `visit_kind` ∈ `single` / `preop` / `postop` / `followup`；`visit_no` 为随访序号（1 起）。
- `month_ix` 停用（保留列但不再写入语义）；`period_source` ∈ `exact` / `approx` / `unknown`。
- **多时点白名单写死**：仅 `SCH/js_SCH`、`PAH/lxf_PAH` 可走 `followup_6m`；`zjl_RDL` 数据不动，只在 `meta` 记例外位（只报数、不判 P0）。其它库不得自行写 `multi_visit_exempt=1`。
- 新库时点模型与现行 D29 的 `unit ∈ {1,3,6}` 并存，至门禁另批升级。

## 契 10 目录契约

目标态（只改文档，不搬盘、不建 `dict.db`、不把论文实体改挂）：

```
_DataBase\
├─ Family\
│  ├─ dict.db                 ← 全局字典（唯一）
│  ├─ <FAM>\
│  │  ├─ _PHI\<FAM>db         ← 身份：id / id_number / ref_project / 既有 ref_* / meta；不留 dict
│  │  ├─ __zip\<leaf>\        ← 源压缩包（双下划线，不改名）
│  │  ├─ __zip\thesis\<slug>\ ← 论文原件目标落点（勿再新建 _thesis）
│  │  └─ <slug>\<slug>db      ← 子工程库：clin / person / qc / src / _modules_* / *_val
│  └─ …共 28
└─ _grants\ _lab\ _med\ _reviews\ _teach\ _work\
```

- 家族库与子库文件名必须等于所在目录名 + `db`。
- 勿再新建 `_thesis`；论文目标落点 `__zip\thesis\<slug>\`；实体改挂待另点名。
- 非家族目录留 `_DataBase` 根，不搬进 `Family\`。
- `__zip` 下普通叶仍 ≤2 层（`__zip\<leaf>\<文件>`）；`__zip\thesis\<slug>\<文件>` 是学位支例外。
- 自 `_DataBase` 起：`Family` 深 1，家族深 2，叶深 3，子库文件深 4。现行盘面在迁入 `Family\` 之前仍为 `{RAW}\<family>\...`（自 `_DataBase` 起总深 3）。

## D93–D99 实测基线

下列数字在 `{RAW}` 量得，写入口径时照抄，不作二次估算。判级与摘要以 `db-gates.md` 码表为准；本节只补该表写不下的细分。

- **D93**：软判三级为 `OUT_OF_RI`（疾病合法偏离，只报数）/ `UNIT_SUSPECT`（出区间且按已知因子反算落回）/ `IMPLAUSIBLE`（越过硬上限）。具体计数与「是否失败阈值」以码表 D93 为准。
- **D94**：80 库 190 个不同 code / 6,100 行（`VALUE_DIRTY` 5,054 最多）。首发 16 码为底，旧 190 码按 `superseded_by` 归一；完整词表待另文件落盘。
- **D97**：禁止用 `typeof` 四类占比判混合（会把 `INTEGER`+`REAL` 误报 32 列）。基线：真混合 0 列。
- **D98** 值内糊单位 4 处：`OTHERS/ybc_STWZ.pain_duration`=`300d`、`SLE/mlh_SLE.disease_course`=`<9w`、`HZ/lln_HZ.pain_maximum`=`第一周`、`EGVB/js_TIPS_his.timing_raw`=`After`。另有中文列名 379 个、大写 124、单位内嵌 194 列。
- **D99** `id.sex`：41,060 NULL + 男1,349 女1,039 男性447 M225 女性212 F211 m15（8 种写法混装，入库时归一）。
