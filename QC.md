---
name: rules-qc
description: L1 支撑：规则仓与 _Docs 盘面的判据（R1–R17）、频率、失败处置、豁免。
up: My rule.md §6
---
# 0 定位与边界
- 管：规则仓与 `{doc_root}` 盘面的判据、频率、失败处置、豁免。
- 不管：技能树 QC（→ `skills.md` §6）、harvest 纳入门禁（→ `{SKILLS}\00_orchestrator\harvest\`）、库结构门（→ `{doc_root}\test\structure_check.py`）、归并（→ `db-library`）。`{DEL}` 落点、离场条件与新建禁区 → `zone-del.md`；harvest 对象与布局 → `zone-docs.md`。何时清与扫描实现见 §5；永不自动清名单 → `zone-del.md` §6。
- 原则：**fail-loud**；能机器判的不靠人记；不得 ignore / skip / 假绿。

# 1 频率
| 时点 | 跑什么 | 失败怎么办 |
|---|---|---|
| 每次改规则 | `python -B check_paths.py --check` | 阻断 merge，不推 |
| 每次 PR | R1–R10、R13–R17 脚本全绿 + R11、R12 用 `{doc_root}\test\structure_check.py` 全绿 + `tests/` 通过；R8 人门 | 不开 PR |
| 每季度 | 史清理、别名合并、路由表复核 | 出清单，批准后做 |

# 2 规则门 R1–R17
| 编号 | 判据 | 机器点 | 现状 |
|---|---|---|---|
| R1 路由闭合 | 每个 live md 在 L0 路由表或 `routes:` 出现；目标文件存在 | `qc_rules.py` | 已机器 |
| R2 正文无史 | 不得出现变更日期、`t<数字>` 变更号、「此前 / 曾用 / 更名 / formerly / 已瘦身 / 已退休 / 已卸 / 已并入 / 已拆出」；「不再」不入词表；数据阈值日期（如批件 ≥ 2023-11-10）除外 | `qc_rules.py` | 已机器 |
| R3 旧名唯一 | `aliases.yaml` 里作者登记的 `tokens:` 不得出现在正文；「勿再新建 / 已退役 / 原 `」禁名行豁免 | `qc_rules.py` | 已机器 |
| R4 指针可解析 | `{RULES}` / `{SKILLS}` 路径与 seat 存在 | `check_paths.py` | 已机器 |
| R5 无副本 | 归一化后 ≥30 字、相似度 ≥0.80 的句子只允许一处；委派指针豁免收窄为：≤60 字且同时含 `→` 与 §ID（D-5） | `qc_rules.py` | 已机器 |
| R6 头字段 | L1 必含 `name` / `description`；L0 必含 `routes:` | `qc_rules.py` | 已机器 |
| R7 行长 | 单行 ≤400 字符；表格行与代码块除外 | `qc_rules.py` | 已机器 |
| R8 变更留痕 | PR 必含：改前 `--check` 与 `qc_rules.py` 输出、正文 why（≤3 行）、改名同步 `aliases.yaml` | PR 模板 | 已建 |
| R9 节号锚点 | `§N` 必须命中目标文件的编号标题；裸 `§N` 继承同行的文件名，否则指本文件；`§A–B` 两端都校验 | `qc_rules.py` | 已机器 |
| R10 指针壳 | live 文件正文（去 frontmatter 与标题）非空行 ≤5 且只含 move/pointer 线索，或正文为空 → 立刻删；不接受 stub 长期存在 | `qc_rules.py` | 已机器 |
| R11 活文档不陈旧 | `_DataBase` / `_Docs` 的 `目录说明.md` 与 README 里作为现行指令的绝对路径必须可解析（无停用根、无失效阶段指针）；计数与日期主张须与实盘一致；史证须同句带标记词 | `{doc_root}\test\structure_check.py` S30 + `audit_readme_counts.py` | 已机器（_Docs 侧）+ H2 人门 |
| R12 备份垃圾不进阶段工程 | `*.bak` / `*.bk` / `~$*` / `- copy` / `副本` 不得留在阶段工程；旧配置与旧稿移 `ref\tmp\` 或 `{DEL}`，移动留台账 | `{doc_root}\test\structure_check.py` S32 | 已机器 |
| R13 体量计量 | 计量 L0 ≤6000、其余 L1 ≤12000、总图 `workspace-layout.md` ≤3000（python `len`，全文）。`generated: true` 与 `aliases.yaml` 不计。输出始终打印字数表。现行已超目标的文件（C8 基线：`My rule.md`、`zone-database.md`）只报告、不令三门变红（D-8：体量是目标，略超不删实质，不假标 `generated: true`、不扩 ignore、不擅自抬高硬限）。此落地方式待主人确认。新的非豁免超限仍失败。 | `qc_rules.py` | 已机器 |
| R14 锚点闭合 | 字母节号 `§W1` 等须有唯一 `**§ID**` 定义且与该文件 `owns:` 一致；形如某 md 加书名号标题、或「本文件」加书名号标题，须为对端标题；`up:` 可解析（文件名可含空格）；`routes:` 与 L0 §5 表「读」列本地 md 一致 | `qc_rules.py` | 已机器 |
| R15 术语表 | L0 §4 必须有术语表（含「术语」及 `A` / `Adm` / `00`）。**不设「主人」失败门，不整词替换「主人」**（D-3，异于计划原文）。`aliases.yaml` 的 `terms:` 是词表不是禁用表。 | `qc_rules.py` | 已机器 |
| R16 路径写法 | 代码块、URL、`file:///` 之外不得写正斜杠形式的 ref 路径（应写反斜杠）；盘符字面量仅出现在 L0 §4、`local-overlay.md`、`aliases.yaml` | `qc_rules.py` | 已机器 |
| R17 D 码表自洽 | `db-gates.md` 手写（`generated: false`）。表内 D 码唯一、完整、与表头声明的覆盖范围及排除项一致。不绑定未提交或跨仓的 `gates.py`（D-6）；跨仓集合差异不在本门失败。 | `qc_rules.py` | 已机器 |

项目数据件（csv / tsv / ini / py 等）的旧路径门与 R11 同方向，范围见 `zone-projects.md` 子工程约定中的旧路径门；R11 机器点仍只覆盖 `_DataBase` / `_Docs` 的说明与 README。

# 3 失败处置
- 先修到过门；不能过门就改规则，但**须用户点头**。
- 不得用 skip / archived 绕过，不得把未跑说成通过；报绿必须附命令与输出。
- 同一门连续两轮失败 → 列入口头汇报待办，不静默挂账。

# 4 豁免
- `aliases.yaml`（旧名）与 `rules-qc`（本文件）不受 R2 / R3 约束。
- 「勿再新建」行、已退役夹禁止清单保留原名，不算 R3 的旧名。
- 技能正文里的英文镜像（如 `{SKILLS}\00_orchestrator\references\project-ref-layout.md`）不参与 R5 副本判定，冲突以 `{RULES}` 为准。

# 5 `_Docs` 清理（按需）
- **触发**：用户点名，或季度巡检时一并跑；不再每轮收工自动跑。
- 流程：`cleanup_scan.py` 出候选 → 人工确认 → `cleanup_move.py` 移 `{DEL}`。
- 三条判据：**过期**（>90 天未被引用）、**重复**（同内容多份）、**无主**（无项目 / 无索引指向）。
- **指针壳（stub / redirect）**：正文 ≤5 行且含盘符路径或 `moved to` / `已移至` / `→` 的 `.md` 归 pointer-only；零入向引用即候选，不设 90 天门槛（stub 本就不该长期存在）；不校验其命名与正文，R5 / R6 / R9 不覆盖。
- 默认分级：A 可直接移、B 需确认、C 永不自动清（名单 → `zone-del.md` §6）。
- 清理保相对路径；删除字节归 `{DEL}`（`zone-del.md`）。

# 6 与 `skills.md` §6 的分工
- 技能树的精简 / skip / archived / 退役仅指针 → `skills.md` §6。
- 规则仓、`_Docs` 盘面、规则 PR 门 → 本文件。
