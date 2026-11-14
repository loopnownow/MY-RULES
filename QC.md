---
name: rules-qc
description: L1 支撑：规则仓与 _Docs 盘面的判据（R1–R9）、频率、失败处置、豁免。
up: My rule.md §6
---
# 0 定位与边界
- 管：规则仓（`{RULES}`）与 `{doc_root}` 盘面的判据、频率、失败处置、豁免。
- 不管：技能树 QC（→ `skills.md` §6）、harvest 纳入门禁（→ `{SKILLS}\00_orchestrator\harvest\`）、库结构门（→ `{doc_root}\test\structure_check.py`）、归并（→ `db-library`）。
- 原则：**fail-loud**；能机器判的不靠人记；不得 ignore / skip / 假绿。

# 1 频率
| 时点 | 跑什么 | 失败怎么办 |
|---|---|---|
| 每次改规则 | `python -B check_paths.py --check` | 阻断 merge，不推 |
| 每次 PR | R1–R9 脚本全绿 + `tests/` 通过；R8 人门 | 不开 PR |
| 每季度 | 史清理、别名合并、路由表复核 | 出清单，批准后做 |
| 每年 | `HISTORY.md` 归档评估（只追加，不重写） | 记入待批 |

# 2 规则门 R1–R9
| 编号 | 判据 | 机器点 | 现状 |
|---|---|---|---|
| R1 路由闭合 | 每个 live md 在 L0 路由表或 `routes:` 出现；目标文件存在 | `qc_rules.py` | 已机器 |
| R2 正文无史 | 不得出现变更日期、`t<数字>` 变更号、「此前 / 曾用 / 更名 / formerly」；数据阈值日期（如批件 ≥ 2023-11-10）除外 | `qc_rules.py` | 已机器 |
| R3 旧名唯一 | `aliases.yaml` 里作者登记的 `tokens:` 不得出现在正文；「勿再新建 / 已退役 / 原 `」禁名行豁免 | `qc_rules.py` | 已机器 |
| R4 指针可解析 | `{RULES}` / `{SKILLS}` 路径与 seat 存在 | `check_paths.py` | 已机器 |
| R5 无副本 | 归一化后 ≥40 字、相似度 ≥0.92 的句子只允许一处；委派指针句（`→` + 见 / 同文件 / 细则 / 权威 / 指针 / 落点）除外 | `qc_rules.py` | 已机器 |
| R6 头字段 | L1 必含 `name` / `description`；L0 必含 `routes:` | `qc_rules.py` | 已机器 |
| R7 行长 | 单行 ≤400 字符；表格行与代码块除外 | `qc_rules.py` | 已机器 |
| R8 变更留痕 | PR 必含：改前 `--check` 与 `qc_rules.py` 输出、史迁 `HISTORY.md`、改名同步 `aliases.yaml` | PR 模板 | 已建 |
| R9 节号锚点 | `§N` 必须命中目标文件的编号标题；裸 `§N` 继承同行的文件名，否则指本文件；`§A–B` 两端都校验 | `qc_rules.py` | 已机器 |

# 3 失败处置
- 先修到过门；不能过门就改规则，但**须用户点头**。
- 不得用 skip / archived 绕过，不得把未跑说成通过；报绿必须附命令与输出。
- 同一门连续两轮失败 → 列入口头汇报待办，不静默挂账。

# 4 豁免
- `HISTORY.md`（史）、`aliases.yaml`（旧名）、`rules-qc`（本文件）不受 R2 / R3 约束。
- 「勿再新建」行、已退役夹禁止清单保留原名，不算 R3 的旧名。
- 引用史只写「背景见 `HISTORY.md` §x」，不作判据。
- 技能正文里的英文镜像（如 `{SKILLS}\00_orchestrator\references\project-ref-layout.md`）不参与 R5 副本判定，冲突以 `{RULES}` 为准。

# 5 `_Docs` 清理（按需）
- **触发**：用户点名，或季度巡检时一并跑；不再每轮收工自动跑。
- 流程：`cleanup_scan.py` 出候选 → 人工确认 → `cleanup_move.py` 移 `{DEL}`。
- 三条判据：**过期**（>90 天未被引用）、**重复**（同内容多份）、**无主**（无项目 / 无索引指向）。
- 默认分级：A 可直接移、B 需确认、C 永不自动清。
- **永不自动清名单**：`_library`、期刊池、批件、`mem`、harvest 台账。
- 清理保相对路径；删除字节归 `{DEL}`（`del-and-harvest.md`）。

# 6 与 `skills.md` §6 的分工
- 技能树的精简 / skip / archived / 退役仅指针 → `skills.md` §6。
- 规则仓、`_Docs` 盘面、规则 PR 门 → 本文件。

# 7 实施状态

- **已机器**：R1–R7（`qc_rules.py` + `tests/test_rules_qc.py`，22 个用例；R4 在 `check_paths.py`）。
- **R8 已建**：`.github/pull_request_template.md` 把四件事做成勾选项（门全绿 / 史进 HISTORY / 改名更新 aliases / 新 L1 同步路由与必检）。
- **季度**：首轮 2026-11-14 已跑——9 个 live 文件正文史标记 0 处、`aliases.yaml` 38 条无合并项、路由表 12 行与文件一一对应；记录见 `HISTORY.md` §I。
