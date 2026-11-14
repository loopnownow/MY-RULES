---
name: My rule
description: L0 常驻层：裁决顺序、硬闸、交付落点、路由第一跳、QC 频率。
routes: [workspace-layout.md, project-ref-layout.md, del-and-harvest.md, library-taxonomy.md, network-security.md, skills.md, QC.md]
---

# 0 本仓与阅读顺序
- 本文件 = **L0 常驻层**，每次开工必读。细则按 §5 路由读 L1 专题；做法按派单挂到 MY-SKILLS（L2）。
- 层级契约：L0 只写裁决、授权、落点、路由、门；L1 只写「放哪 / 什么算对 / 何时停」；L2 不碰授权、落点、网络、PR、别名、路由。L1 只能收紧硬闸，不能放宽。
- 生效对象：Aitor、子代理、本机 DSH、Cline、Cloud Agent，一律遵守，无例外、无需再问。云端 prompt 必须写明 `{RULES}`；Skills 按本次任务写入。云端 = Grok Bot 的 box；本地 = 城城本机（`D:\`、Downloads），勿对调。
- 工作区只有一层（`D:\MyProjects\<stage>\<project>`）；不设 A/B 双工作区或挂载缓存树。
- 一任务一执行方：编码 / 脚本 / MY-CODES → Loopnow（粗席位 `02_data-processing`）；整理 / 提取 / 填写 / 本机 IDE → 本机 DSH 或 Cline（点名或批准时）；盯梢 → `{SKILLS}\00_orchestrator\references\handoff-monitor.md`。选模型用客户端当前配置，不在此指定。

# 1 权威与硬闸
## 1.1 裁决顺序
用户当轮 > 硬闸 > L1 领域契约 > 本文件一般条款 > 子工程内约定 > 技能默认写法。只有用户当轮能放宽硬闸；L1 更具体，可以压 L0 的一般条款，但压不了硬闸。
- **Rules 必须挂载并遵守；Skills 仅在派具体 fine id / 工作包时附加。**「Skills 未挂载」不是跳过 Rules 的理由；冲突裁决 Rules > Skills。
- 单项目约定写在子工程内（`<project>\_Docs\` / `ref\`），不写全局 `{RULES}` / `{SKILLS}`。

## 1.2 硬闸五类
1. **写盘授权**：只读不用授权；任何写盘先获当轮点名（§2）。
2. **禁删**：清理只移 `{DEL}` 并保相对路径（§2）。
3. **新建禁区**：默认只许 `{DEL}`（§2；全文 `del-and-harvest.md`）。
4. **网络红线**：禁止网段默认拒绝；敏感外发先说明再获同意（`network-security.md`）。
5. **三仓写边界**：`{RULES}` / `{SKILLS}` 只读，变更走 PR；可写代码只在 `{code_root}`。

另有 **PII 边界**：姓名 / 电话只可写本机 `_DataBase` 家族 SQLite（`<family>db`，不进 GitHub）；身份证与地址默认不进，除非当轮新授权；均不得写进任何仓、回执或聊天。

# 2 写盘与授权
**总闸：只读不用授权；任何新建 / 编辑 / 覆盖 / 移动 / 删除前，须用户当轮点名该项或明确同意；未获授权即停，不静默落盘。**
- **授权按项按轮**：点名 A 只授权 A 的该处；「继续」「好」「你看着办」不等于写盘许可。须问条款（D-1 移底表、网络、MY-SKILLS PR/merge、Word 城城已改先问）继续有效。
- **禁删**：旧稿 / 旧产物移入 `{DEL}`（`_by-project` / `_by-function`），保留相对路径；禁止静默永久删除。
- **新建**：默认只许 `{DEL}`；常设例外仅限 bot 记忆导出（`_Docs\mem\`）、子工程 `ref\tmp\`、用户当轮同意；例外只是新建路径，不构成编辑许可。一次性脚本 / 小补丁只落 `{DEL}`，不进主目录、`.grok\tmp`、课题根。
- 默认禁止直接改 `{RULES}`、`{SKILLS}`、`_Docs`、子工程已有文件；**改已有文件同样须当轮点名**，含 `_Docs\harvest\*`、`_Docs\mem\*`、已有稿（含 Track Changes）。
- 默认禁在 `{doc_root}` 下 mkdir；目录名一律 ASCII 英文，中文只进索引列。
- **后果性操作**（投稿 Approve、付费、改稿开跑、接审）与**开工**（目标与验收、假设 ≤3、取舍、谁执行）都先出计划等「同意」；「直接做」不跳过 PR/merge 确认与须批网络。
## 2.1 盘问 / grill-me（SSOT；技能只指针）
- 何时：多节点、新能力、高风险、或用户说 `grill-me` /「盘问」；单节点且无关键未知 → 不问。
- 一轮批处理；问题编号 + 每题推荐默认；可多选，不限 5 题；能查文件 / 网页的先查再问。
- 通过后出 Plan card（节点顺序、风险门），等明确点头再派单；`{SKILLS}\00_orchestrator\references\plan-and-grilling.md` 只留 Plan card / Q0–Q3 / 流程图并指回本条。

# 3 交付与清理
子工程**没有** `0result\`：最终交付 → 子工程根；中间 → `ref\` 地图（`project-ref-layout.md`）；子工程内临时 / 中间 → `ref\tmp\`（非默认 `{DEL}`）；无子工程的一次性件 → `{DEL}`；Downloads 仅当轮点名。

| 产物 | 落点 |
|---|---|
| 最终交付（稿件 / 终表 / 报告） | 子工程根；无子工程且点名下载 → Downloads；否则 `{DEL}` |
| 报告 / QC（HTML，中间） | 子工程 `ref\` 或阶段夹；否则 `{DEL}` |
| DOCX 稿件 / XLSX 终表 | 子工程根；稿名见 `project-ref-layout.md`「SCI 稿件文件名」 |
| 文献全文（PDF / HTML） | `{doc_root}\_library\references\<L1>\<L2>\`；子工程 `ref\refer\` 只留 `DOI_*.md` 指针 |
| 期刊池 / 批件 | `_library\journals\index.csv`；`_library\ethics\approvals\<L1>\<L2>\`（口径 `library-taxonomy.md`） |

- **单档 ≤1 GiB**；预计超限直接分 900 MiB 字节卷 + `分卷说明.md`，不先造大档再拆（细则 `workspace-layout.md`）。
- **Word / 稿件**：未当轮点名禁改 `.docx` / `.pdf` 版式；改文字用 Track Changes，禁大段覆盖；城城已改先问，禁覆盖或改回（手改识别 → `project-ref-layout.md`）；**无稿不造空件**（无 docx 就记「无 docx」）。
- 同一分析 `Results*.html` 与 `.xlsx` 冲突 → 以 HTML 为准并写明；清理旧稿 → `{DEL}` 保相对路径，不静默删除；长表 → `{SKILLS}\00_orchestrator\references\standing-delivery.md`。

# 4 别名
| 别名 | 值 |
|---|---|
| `{RULES}` | `D:\MyProjects\_Docs\GitHub\MY-RULES` |
| `{SKILLS}` | `D:\MyProjects\_Docs\GitHub\MY-SKILLS` |
| `{code_root}` / `{code_stats}` | `D:\MyProjects\_Docs\GitHub\MY-CODES` |
| `{RAW}` | `D:\MyProjects\_DataBase`（除 `_index.csv` / `_diseases.csv` 只读） |
| `{DEL}` | `D:\MyProjects\.Del` |
| `{doc_root}` / `{lab_root}` | `D:\MyProjects\_Docs` / `D:\MyProjects` |

旧名一律不写进正文，映射见 `aliases.yaml`。术语：`A`=批注作者；`00`–`07`=技能层。

# 5 路由表（第一跳）
| 触发 | 读 | 挂 |
|---|---|---|
| 盘面 / 阶段夹 / 家族桶 / `_share` / `_db` / 冷库 / accepted 收工 | `workspace-layout.md` | `db-library` |
| 项目 `ref\` 地图 / 稿名 / 手改识别 / 幂等 | `project-ref-layout.md` | — |
| `{DEL}` / harvest / 清理 / 活依赖 | `del-and-harvest.md` | `00_orchestrator` harvest |
| 网络 / 敏感外发 / 代理 / 留痕 | `network-security.md` | — |
| 技能库 / PR 同步 / 演进 | `skills.md` | `skills` |
| 库分类 L1–L2 / 三库 / 批件 / 期刊池 | `library-taxonomy.md` | `find-journal` |
| 规则 QC / 清理判据 / 门 | `QC.md` | — |
| 三仓分工 / 内容该放哪 | `README.md` | — |
| 派单 / 盯梢 | `{SKILLS}\00_orchestrator\references\ownership-contract.md` / `handoff-monitor.md` | `00_orchestrator` |
| 盘问 / Plan card | 本文件 §2.1 | `00_orchestrator` |
| 稿件禁令 | `{SKILLS}\05_manuscript\qc\manuscript-local-qc.md` | `05_manuscript` |
| 文献 / 选刊 / 统计 / 建模 | — | `03_research` / `find-journal` / `02_data-processing` |

# 6 QC
- **频率**：改规则跑 `python -B check_paths.py --check` + `python -B qc_rules.py`（R1–R3 / R5–R7；负向用例 `python -B -m pytest -q tests`）；每轮收工跑 `_Docs` 清理扫描；每季度清一次史。
- **规则门 R1–R8**（判据 / 豁免 / 失败处置）→ `QC.md`；QC 不得 ignore / skip / 假绿，skip / archived / 退役仅指针不是停放位（技能树 → `skills.md` §6）。
- **三仓流程**：本地分支 + 测试 → 出示完整变更清单 → 批准开 PR → 不直推 main → 用户说「合」「和」「推合」才 merge；默认 QC 由 Aitor 本人做（点名除外）；MY-SKILLS 细则 → `skills.md` §5。

# 7 执行准则
- **编程**：简单优先、外科手术式、模块化、不写回退（失败要响）；新脚本 Python 3.13.9；PowerShell 不用 `&&`；配置置顶；注释只写配置含义与运行方式。
- **流程**：先测 → 再跑 → 核查 → 验收；批量写盘先 dry-run，显式 `--execute` 才落盘；断点续传不整段重算。
- **验证**：优先 diff；lint / 测试后交终稿；**不编造**事实 / 数字 / 文献 / DOI / 路径，找不到写「未找到」。
- **科研**：文献只引真实来源；统计不为跑通改 outcome / 纳入 / cutoff / 协变量 / 缺失 / 模型（细则 → `{SKILLS}\02_data-processing\qc\`）。
- **工程决策** R1 需求优先 · R2 证据排错 · R3 有序简化 · R4 风险比例 · R5 保护不变量 · R6 闭环验证；**重大变更门**（改结构 / 改 ID / 删目录）先给假设清单与影响并获批。
- 细节（模板、阶梯、docstring、断点做法）→ `{SKILLS}\02_data-processing\advanced\coding.md`。

# 8 汇报
- 说明 / QC 中文；期刊英文稿英文；时区 `Asia/Shanghai`；「；」=两任务，「|」=同任务并列；状态用表格或列表。
- **标点**：允许 U+2212 `−`；禁 em dash 与 spaced `--`（仅英文稿件 / 对外英文；中文「——」不受限）；STE → `{SKILLS}\05_manuscript\base\vocab\L3\lab-ste.md`。
- **mem**：bot 记忆只放隐私与可变 SSOT（如 JCR xlsx）；运营口径进本仓，技能口径进 `{SKILLS}`；导出落 `{doc_root}\mem\`。
