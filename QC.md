---
name: rules-qc
description: L1 支撑：规则仓与 _Docs 盘面的判据（R1–R8）、频率、失败处置、豁免。
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
| 每次 PR | R1–R8（P5 起进脚本） | 不开 PR |
| 每轮任务收工 | `_Docs` 清理扫描（§5） | 当轮移 `{DEL}` 或记待办 |
| 每季度 | 史清理、别名合并、路由表复核 | 出清单，批准后做 |
| 每年 | `HISTORY.md` 归档评估（只追加，不重写） | 记入待批 |

# 2 规则门 R1–R8
| 编号 | 判据 | 机器点 | 现状 |
|---|---|---|---|
| R1 路由闭合 | 每个 live md 在 L0 路由表出现且仅一次；目标文件存在；`routes:` 数 = live md 数 | `qc_rules.py` | 待建（P5） |
| R2 正文无史 | live md 正文不得出现变更日期、`t<数字>` 变更号、「此前 / 曾用 / 更名」叙述；数据阈值日期（如批件 ≥ 2023-11-10）与「勿再新建」禁名清单除外 | `check_paths.py` 扩展 | 待建 |
| R3 旧名唯一 | 旧名 token 只允许在 `aliases.yaml` / `HISTORY.md`；「勿再新建」清单豁免 | 现有 `STALE_RULES` 上下文扫描扩展 | 部分 |
| R4 指针可解析 | `{RULES}` / `{SKILLS}` 路径与 seat 存在 | `check_paths.py` | **已机器** |
| R5 无副本 | 归一化（去标点空白）后 ≥40 字且相似度 ≥0.9 的句子只允许出现在一处 | `qc_rules.py` | 待建（P5） |
| R6 头字段 | L1 必含 `name` / `description` / `up`；L0 必含 `routes:` | `qc_rules.py` | 待建（P5） |
| R7 行长 | 单行 ≤300 字符；单条 ≥2 层括注告警 | `qc_rules.py` | 待建（P5） |
| R8 变更留痕 | PR 必含：改前 `--check` 输出、史迁 `HISTORY.md`、改名同步 `aliases.yaml` | PR 模板 | 待建（P5） |

# 3 失败处置
- 先修到过门；不能过门就改规则，但**须用户点头**。
- 不得用 skip / archived 绕过，不得把未跑说成通过；报绿必须附命令与输出。
- 同一门连续两轮失败 → 列入口头汇报待办，不静默挂账。

# 4 豁免
- `HISTORY.md`（史）、`aliases.yaml`（旧名）、`rules-qc`（本文件）不受 R2 / R3 约束。
- 「勿再新建」行、已退役夹禁止清单保留原名，不算 R3 的旧名。
- 引用史只写「背景见 `HISTORY.md` §x」，不作判据。
- 技能正文里的英文镜像（如 `{SKILLS}\00_orchestrator\references\project-ref-layout.md`）不参与 R5 副本判定，冲突以 `{RULES}` 为准。

# 5 `_Docs` 每轮清理（原 My rule §5.2 迁入）
- 流程：`cleanup_scan.py` 出候选 → 人工确认 → `cleanup_move.py` 移 `{DEL}`。
- 三条判据：**过期**（>90 天未被引用）、**重复**（同内容多份）、**无主**（无项目 / 无索引指向）。
- 默认分级：A 可直接移、B 需确认、C 永不自动清。
- **永不自动清名单**：`_library`、期刊池、批件、`mem`、harvest 台账。
- 清理保相对路径；删除字节归 `{DEL}`（`del-and-harvest.md`）。

# 6 与 `skills.md` §6 的分工
- 技能树的精简 / skip / archived / 退役仅指针 → `skills.md` §6。
- 规则仓、`_Docs` 盘面、规则 PR 门 → 本文件。

# 7 P5 待建清单
- `qc_rules.py`（R1 / R2 / R5 / R6 / R7）+ `tests/` 负向用例。
- `check_paths.py`：把 `HISTORY.md`、`aliases.yaml`、`del-and-harvest.md`、`QC.md` 显式纳入扫描与豁免。
- PR 模板（R8）；本地无 GitHub Actions，门在提交前跑。
