---
name: My rule
description: L0 常驻层：裁决顺序、硬闸、授权矩阵、交付落点、路由第一跳、QC。
routes: [workspace-layout.md, zone-del.md, zone-database.md, db-schema.md, db-gates.md, zone-docs.md, library-taxonomy.md, zone-projects.md, project-ref-layout.md, manuscript-docx.md, project-fact-lookup.md, execution.md, network-security.md, skills.md, local-overlay.md, QC.md, README.md]
owns: [W1, W2, W3, W4, W5, X1, P1, S1, S2]
---

# 0 阅读顺序与层级契约
- 本文件 = **L0 常驻层**，每次开工必读。细则按 §5 路由读 L1 专题；做法按派单挂到 MY-SKILLS（L2）。
- **课题事实：** 开工、改稿、内审须先查 `project-fact-lookup.md`（通讯作者、伦理号、扫描序列、实验室范围）；挂载不等于已查。
- 层级契约：L0 只写裁决、授权、落点、路由、门；L1 只写「放哪 / 什么算对 / 何时停」；L2 不碰授权、落点、网络、PR、别名、路由。L1 只能收紧硬闸，不能放宽。
- 生效对象：Aitor、子代理、本机 DSH、Cline、Cloud Agent，一律遵守，无例外、无需再问。云端 prompt 必须写明 `{RULES}`；Skills 按本次任务写入。云端 = Grok Bot 的 box；本地 = 城城本机（盘面见 §4），勿对调。
- 工作区只有一层 → `workspace-layout.md`。
- 席位分工与一任务一执行方 → `execution.md`。

# 1 裁决与硬闸
## 1.1 裁决顺序
用户当轮 > 硬闸 > L1 领域契约 > 本文件一般条款 > 子工程内约定 > 技能默认写法。只有用户当轮能放宽硬闸；L1 更具体，可以压 L0 的一般条款，但压不了硬闸。
- 多机位可另设本机覆盖层：只收紧、不放宽；路径与授权分工、冲突先报再执行 → `local-overlay.md`。不得用本机表覆盖本文件 §4 别名。
- **Rules 必须挂载并遵守；Skills 仅在派具体 fine id / 工作包时附加。**「Skills 未挂载」不是跳过 Rules 的理由；冲突裁决 Rules > Skills。
- 单项目约定写在子工程内（`<project>\_Docs\` / `ref\`），不写全局 `{RULES}` / `{SKILLS}`。

## 1.2 硬闸五类
1. **写盘授权**：只读不用授权（`{doc_root}\mem\` 除外，见 §2）；任何写盘先获当轮点名（§2）。
2. **禁删**：清理只移不删，保相对路径（§X1）；旧稿落点 → §X2。
3. **新建禁区**：默认只许 `{DEL}`（§N1）。
4. **网络红线**：禁止网段默认拒绝；敏感外发先说明再获同意（`network-security.md`）。
5. **§S1** **三仓写边界**：`{RULES}` / `{SKILLS}` 只读，变更走 PR；可写代码只在 `{code_root}`。

**§P1** 另有 **PII 边界**：姓名 / 电话 / 身份证 / 地址只许落本机 `_DataBase\<family>\_PHI\<family>db` 的 `id` 表（不进 GitHub）；子工程库 `<slug>\<slug>db` 零 PHI；有 PHI 家族跨库引用一律用 `family_uid`，不以姓名为键。身份证与地址一并允许落家族库 `id` 表；PHI 不得写进任何仓、回执或聊天；无 PHI 家族不建身份表，家族级登记与跨库引用改用家族编码（`meta.family_code`），PHI 永不下沉子库。DICOM 来源的 PHI、伪匿名标识与冲突判级 → §P2、§P3（`db-schema.md`）。

# 2 写盘与授权
**§W1** **总闸：只读不用授权（`{doc_root}\mem\` 查阅见下条）；任何新建 / 编辑 / 覆盖 / 移动 / 删除前，须用户当轮点名该项或明确同意；未获授权即停，不静默落盘。** 下表只回答「这个位置允许做什么」；所有写盘另须本条。
- **§W3** **mem 查阅：** 未经当轮点名，`{doc_root}\mem\` 下只许读 `README.md` 与 `SENSITIVE.md`；其余文件与子夹（含列出、打开、检索）即使只读，也须用户当轮点名该文件、路径或该项任务。写盘仍按本条总闸，须当轮点名。
- **§W2** **授权按项按轮**：点名 A 只授权 A 的该处；「继续」「好」「你看着办」不等于写盘许可。须问条款（D-1 移底表、网络、MY-SKILLS PR/merge、Word 城城已改先问、稿件回滚须授权）继续有效。
- **§X1** **禁删**：清理只移不删，保留相对路径；禁止静默永久删除。旧稿与中间件落点 → §X2。 `{DEL}` 只能由主人手动清空（空目录、就地 `_Del` 等细则 → `zone-del.md` §1）。
- **新建**默认只许 `{DEL}`；显式例外与细则 → §N1。
- **§W4** 默认禁止直接改 `{RULES}`、`{SKILLS}`、`_Docs`、子工程已有文件；**改已有文件同样须当轮点名**，含 `_Docs\harvest\*`、`_Docs\mem\*`、已有稿（含 Track Changes）。
- 目录名一律 ASCII 英文，中文只进索引列；`{doc_root}` 下 mkdir 见下表。
- **§W5** **后果性操作**（投稿 Approve、付费、改稿开跑、接审）与**开工**（目标与验收、假设 ≤3、取舍、谁执行）都先出计划等「同意」；「直接做」不跳过 PR/merge 确认与须批网络。
- 盘问 / grill-me（§W6）→ `execution.md`。

| 位置 | 新建 | 编辑已有 | 移动 / 覆盖 | 删除 |
|---|---|---|---|---|
| `{DEL}` | 允许（默认唯一落点） | 须当轮点名 | 移入须当轮点名 | 禁止；只由主人手动清空 |
| 子工程 `ref\tmp\` | 允许（常设例外） | 须当轮点名 | 须当轮点名 | 禁止；移入 `{DEL}` 须当轮先问（§X2） |
| `{doc_root}\mem\` | 允许（bot 记忆导出） | 须当轮点名 | 须当轮点名 | 禁止 |
| `{doc_root}` 其余 | 禁止，除非当轮点名「放 _Docs」或用户当轮明确同意；默认禁 mkdir | 须当轮点名 | 须当轮点名 | 禁止 |
| 子工程根与 `ref\` 其余子夹 | 仅限 §3 落点表所列交付，且须当轮点名 | 须当轮点名 | 须当轮点名；把原件移出子工程根须先同意 | 禁止 |
| `.docx` / `.pdf` 稿件 | 无稿不造空件（§M4） | 须当轮点名；只许 Track Changes 增量（§M1） | 覆盖禁止；回滚须当轮点名（§M3） | 禁止 |
| `{RAW}` | 默认只读，`_index.csv` 与 `_diseases.csv` 除外；其余须当轮点名 | 须当轮点名 | 须当轮点名 | 禁止 |
| `{RULES}`、`{SKILLS}` | 只读 | 只读 | 只读 | 只读；变更走 PR（§S1、§S2） |
| `{code_root}` | 允许写代码；`{code_modules}` 增改移须先同意 | 同左 | 同左 | 禁止 |

# 3 交付落点
子工程**没有** `0result\`：最终交付 → 子工程根；中间 → `ref\` 地图（`project-ref-layout.md`）；子工程内临时 / 中间 / 旧版稿，以及无子工程的一次性件，落点 → §X2；把原件放入 Downloads 仍须当轮点名。

| 产物 | 落点 |
|---|---|
| 最终交付（稿件 / 终表 / 报告） | 子工程根；无子工程且点名下载 → Downloads；否则 `{DEL}` |
| 需查看件 / 在做项目的查阅入口 | `{memo_dir}` 不放 `.lnk`；查阅入口与原件不搬家、不另存 → `execution.md` |
| 报告 / QC（HTML，中间） | 子工程 `ref\` 或阶段夹；否则 `{DEL}` |
| DOCX 稿件 / XLSX 终表 | 子工程根；稿名见 `project-ref-layout.md`「SCI 稿件文件名」 |
| 文献全文（PDF / HTML） | `{lib_root}\references\<L1>\<L2>\`；子工程 `ref\refer\` 只留 `DOI_*.md` 指针 |
| 期刊池 / 批件 | `{lib_root}\journals\index.csv`；`{lib_root}\ethics\approvals\<L1>\<L2>\`（口径 `library-taxonomy.md`） |
| 扫描参数 / 实验室参考范围 | `{lib_root}\scanner-registry\`；`{lib_root}\lab-ref-ranges\`（查找口径 `project-fact-lookup.md`） |

- **单档 ≤1 GiB**；预计超限直接分 900 MiB 字节卷 + `分卷说明.md`，不先造大档再拆（细则 `zone-database.md`）。
- **稿件硬闸**：未当轮点名禁改 `.docx` / `.pdf` 版式；助手改稿、手改后禁止重标、回滚、无稿不造空件 → §M1–§M4（`manuscript-docx.md`）。
- 备忘录夹与备忘录正文 → `execution.md`。
- 同一分析 `Results*.html` 与 `.xlsx` 冲突 → 以 HTML 为准并写明；清理旧稿 → §X2，长表口径见 `{SKILLS}\00_orchestrator\references\standing-delivery.md`。

# 4 别名与术语
| 别名 | 值 |
|---|---|
| `{RULES}` | `D:\MyProjects\_Docs\GitHub\MY-RULES` |
| `{SKILLS}` | `D:\MyProjects\_Docs\GitHub\MY-SKILLS` |
| `{code_root}` / `{code_stats}` | `D:\MyProjects\_Docs\GitHub\MY-CODES` |
| `{code_modules}` | `{code_root}\modules` |
| `{RAW}` | `D:\MyProjects\_DataBase`（除 `_index.csv` / `_diseases.csv` 只读） |
| `{DEL}` | `D:\MyProjects\.Del` |
| `{doc_root}` / `{lab_root}` | `D:\MyProjects\_Docs` / `D:\MyProjects` |
| `{lib_root}` | `{doc_root}\_library` |
| `{memo_dir}` | `C:\Users\loopn\Downloads\备忘录` |

机位差异（`{RULES}` / `{SKILLS}` / `{code_root}` 的实际盘面、`{AITOR}`、盘位与只读口径）由 `local-overlay.md` §1 承接；上表为 SSOT 默认值。

旧名一律不写进正文，映射见 `aliases.yaml`。术语：`A`=助手批注/修订作者；`Adm`=城城本人的修订与批注作者标记（其下订正和批注是重要 harvest 对象）；`00`–`07`=技能层。

角色（草稿，本轮不替换现行用词）：主人 / 城城 = 所有者（点名授权、批准、手改、手动清空 `{DEL}`、说「合」）；Aitor = 总调度（派单、开子代理）；用户 = 当轮发话者（只有「用户当轮」能放宽硬闸）。

# 5 路由表（第一跳）
| 触发 | 读 | 挂 |
|---|---|---|
| 盘面 / 根目录总图 / 退役禁建 | `workspace-layout.md` | — |
| `{DEL}` / 三档 / 新建禁区 / 旧稿落点 | `zone-del.md` | — |
| `_DataBase` / 家族桶 / `_PHI` / `__zip` / 家族库 / 子库 | `zone-database.md` | `db-library` |
| `id` 表 / 病理段 / 入表清洗 / DICOM 映射 | `db-schema.md` | `db-library` |
| D 码 / 库门禁 | `db-gates.md` | `db-library` |
| `_Docs` / harvest / `mem` / `_library` | `zone-docs.md` | `00_orchestrator` harvest |
| 库分类 L1–L2 / 批件 / 期刊池 | `library-taxonomy.md` | `find-journal` |
| 阶段夹 / closeout / accepted 收工 / archived / 子工程约定 | `zone-projects.md` | — |
| 项目 `ref\` 地图 / 稿名 / 幂等 | `project-ref-layout.md` | — |
| Track Changes / 手改 / 回滚 / 无稿不造空件 | `manuscript-docx.md` | `05_manuscript` |
| 通讯作者 / 伦理号 / 扫描序列 / 实验室范围 | `project-fact-lookup.md` | — |
| 执行准则 / 汇报 / 备忘录 / 盘问 / 长任务交接 | `execution.md` | `00_orchestrator` |
| 网络 / 敏感外发 / 代理 / 留痕 | `network-security.md` | — |
| 技能库 / PR 同步 / 演进 | `skills.md` | `skills` |
| 本机覆盖层 | `local-overlay.md` | — |
| 规则 QC / 门 | `QC.md` | — |
| 三仓分工 / 内容该放哪 | `README.md` | — |
| 派单 / 盯梢 | `{SKILLS}\00_orchestrator\references\ownership-contract.md` / `handoff-monitor.md` | `00_orchestrator` |
| 稿件禁令 | `{SKILLS}\05_manuscript\qc\manuscript-local-qc.md` | `05_manuscript` |
| 文献 / 选刊 / 统计 / 建模 | — | `03_research` / `find-journal` / `02_data-processing` |

# 6 QC 与三仓流程
- **频率**：改规则跑 `python -B check_paths.py --check` + `python -B qc_rules.py`（R1–R3 / R5–R7 / R9 / R10；负向用例 `python -B -m pytest -q tests`；R11 活文档门在 `{doc_root}\test\structure_check.py` S30 与本仓 `audit_readme_counts.py` 同侧）；每季度清一次史。
- **规则门 R1–R12**（判据 / 豁免 / 失败处置）→ `QC.md`；QC 不得 ignore / skip / 假绿，skip / archived / 退役仅指针不是停放位（技能树 → `skills.md` §6）。
- **§S2** **三仓流程**：本地分支 + 测试 → 出示完整变更清单 → 批准开 PR → 不直推 main → 用户说「合」「和」「推合」才 merge；默认 QC 由 Aitor 本人做（点名除外）；MY-SKILLS 细则 → `skills.md` §5。
