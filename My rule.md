---
name: My rule
description: Aitor（AA）科研与编程全局规则。
license: MIT
---

# 1 适用范围与优先级

- 对 Grok Bot/Aitor、子代理、Cursor、Cline 生效。
- **裁决顺序**：用户当轮表述 > 专题文件 > 本文件 > 子工程内约定。
- **别名**：`{RULES}`=`D:\0Grok\0doc\GitHub\MY-RULES`；`{SKILLS}`=`D:\0Grok\0doc\GitHub\MY-SKILLS`；`{RAW}`=`D:\00db`（已组织的原始库，只读除非点名；原 `00ds` 已迁此）；`{DEL}`=`D:\0del`。
- **本机布局（一行）**：`D:\00db`（organized raw） / `D:\0del`（AI 可操作临时区） / `D:\0Grok\0doc`（语料 + 可复用代码） / `D:\0Grok`（分阶段子工程工作区）。细则 → `workspace-layout.md`。
- **术语**：作者字段 `A`=批注作者；`00`–`07`=技能层；派单→`{SKILLS}\00_orchestrator\references\ownership-contract.md`。**不再使用** A/B 工作区、`{WORK_A}`/`{WORK_B}`、`{MOUNTS}`（mounts 已退役）。
- **一任务一执行方**；外挂（Cursor/Cline）须用户批准。盯梢→`{SKILLS}\00_orchestrator\references\handoff-monitor.md`。
- **云端 / 本地（术语，2026-10-25）：** **云端** = Grok Bot 的 box 计算机（`/workspace` 等）；**本地** = 城城本机（如 `D:\`、Downloads）。二者勿对调。
- **mem 落盘：** bot 记忆导出/更新落在本地 `D:\0Grok\0doc\mem`（城城指定；非默认进 `{DEL}`）。mem **仅保留隐私**与可变数据 SSOT（如 JCR xlsx）；站立运营政策进 `{RULES}`，专业技能进 `{SKILLS}`。
- **单项目约定**写在该**子工程文件夹**内（如子工程 `0doc\` 或 `ref\`），**不**写入全局 `{RULES}` / `{SKILLS}`。须用户点名「放 0doc」才写 `0doc\`。
- **交付落点**：子工程**没有** `0result\` 文件夹。**最终**交付物 → 该子工程**根目录**（`D:\0Grok\<project>` 下）；**中间**产物 → 按 `project-ref-layout.md` 的 `ref/` 子文件夹地图（`review/` / `citation/` / `gates/` / `code/` / `results/` / `exec/` / `tmp/`）；其余临时/非交付进 `{DEL}`；Downloads **仅当**当轮点名「下载」或「Downloads」。

# 2 开工前确认

- 只读不用授权；改/移须先授权。
- **禁删**；移出只进 `{DEL}` 并保留相对路径。**旧稿清理**＝移入 `{DEL}` / `D:\0del`（可按 `_by-project` / `_by-function`），禁止静默永久删除。
- 确认：目标与验收；假设≤3；取舍；谁执行。
- 「直接做」可不逐项确认，但不跳过 MY-SKILLS PR/merge（`skills.md`）与须批网络（`network-security.md`）。「继续」≠网络同意。
- 网络红线→`network-security.md`。

## 2.1 盘问 / grill-me（SSOT；技能只指针）

本条为 grilling 权威正文。`{SKILLS}\00_orchestrator\references\plan-and-grilling.md` 只保留 Plan card / Q0–Q3 / 流程图，并**指向本条**；勿在技能里复写全文。

- **何时**：多节点任务、新能力、高风险、或用户说 `grill-me` / 「盘问」。单节点且无关键未知 → 不问（对齐技能 Q0）。
- **一轮批处理**：合并成**一轮**澄清，不要连环单问。
- **编号 + 默认**：问题编号列出；每题给推荐默认（用户可回「默认」/空确认）。
- **多选（组合）；不限 5 题**：向城城提问可用多选/组合选项（若干答案可并用）；问题数量**不限于 5 个**——需要时可超过 5 题（可用多步卡片 / 连续 widget）。此为城城偏好；平台单卡选项上限另论，勿称平台已抬高硬上限。
- **先查后问**：文件或网页能答的，先自己查；查不到再问（对齐技能 Q3）。
- **然后出 Plan**：澄清通过后再给计划卡（节点顺序、风险门），等明确点头再派单。
- 流程图批准、N1–N4 决策点仍由 `plan-and-grilling.md` 管；本条不管挂载包（mounts 已退役）。

# 3 编程准则

简单优先；外科手术式；软编码；模块化；**不写回退**；新脚本 Python 3.13.9；PowerShell 不用 `&&`。

- **配置置顶**：脚本顶部先放配置/常量块（路径、开关、参数），再写逻辑。
- **仅注释配置和脚本运行说明**：注释只写 (a) 配置字段含义；(b) 如何运行该脚本。不对业务逻辑写长文注释；**不写业务「为什么」**（2026-10-24 裁决维持现行）。
- **不写回退**：禁止 fallback / 静默降级（勿用 try-except 吞失败后走默认路径）；失败要响，暴露错误。
- **可以写多模块并配置可选**：允许多模块；模块可用配置开关可选启用。
- **dry-run**：批量 IO / 写盘前先试跑，打印将执行的操作供确认；默认 dry-run，显式 `--execute` / `--apply` 才落盘。
- **测试→运行→核查→验收**：所有脚本先测试再运行，最后核查，再验收。顺序固定：(1) 先测（unit/smoke/dry-run 视情）；(2) 再跑正式任务；(3) 核查结果；(4) 验收通过后再宣告完成。
- **断点续传**：已处理结果跳过；以中间文件或完成标记续跑，勿整段重算。

细节（模板、阶梯、QC）→`{SKILLS}\02_data-processing\personal\coding.md`。

# 4 执行与验证

优先 diff；lint/测试后交终稿。**不编造**事实/数字/文献/DOI/路径。稿件禁令→`{SKILLS}\05_manuscript\qc\manuscript-local-qc.md`。技能树 **archived → QC 时删除**（不留 archived 标签）→`skills.md` §6。脚本站立流程见 §3「测试→运行→核查→验收」。

# 5 交付与清理

**禁删**；临时只进 `{DEL}\<任务>\`。旧稿/旧产物清理＝移入 `{DEL}`，不静默永久删。子工程**不建** `0result\`。

| 产物 | 格式 | 落点 |
|---|---|---|
| 最终交付（稿件/终表/最终报告等） | 依类型 | **子工程根目录**；无子工程且点名「下载/Downloads」→Downloads；否则→`{DEL}` |
| 中间产物（QC/ledger/门控/草稿等） | 依类型 | 有子工程→按 `project-ref-layout.md` 的 `ref/` 地图（`review/`/`citation/`/`gates/`/`code/`/`results/`/`exec/`/`tmp/`）；否则→`{DEL}` |
| 报告/QC（中间） | HTML | 有子工程→该子工程 `ref\`（或阶段夹如 `in-review\`）；无子工程且点名 Downloads→Downloads；否则→`{DEL}` |
| 稿件/TC（最终） | DOCX | 子工程**根**；否则仅当点名 Downloads，否则 `{DEL}` |
| 数据表（最终） | XLSX | 子工程**根**（不建 `0result\`）；其余同稿件 |

同一分析若 `Results*.html`（或已执行产物 HTML）与 `.xlsx` 数字冲突：以 HTML 为准，并在汇报里写明冲突与所采用源。

「放 0doc」才写 `0doc\`。长表→`{SKILLS}\00_orchestrator\references\standing-delivery.md`。

# 5.1 Word / 审稿回复 / 本机目录（2026-10-19）

- **Word/PDF 格式**：未经当轮点名，禁止改 `.docx`/`.pdf` 版式；改文字用修订模式。词/句级修订，禁止大段覆盖。细则→`{SKILLS}\06_review\personal\word-edit.md`。
- **城城已改先问（全局停）**：若 Word/手稿正文与城城（用户）已编辑文本不同（修订痕迹 / 已知本人改动），**必须先问再改**，禁止擅自覆盖或改回。技能须指针本条，勿只埋在 revise。→`word-edit.md`；`writing-rules-hard.md`；`07_response` revise。（2026-10-24）
- **统一版式**：手稿、审稿意见、审稿回复同一套——正文 Times New Roman 12、1.5 倍行距、段前后 0、两端对齐、LTR、特殊格式无；**表格单元格 12 pt**；**图内文字 Arial**（与正文双轨）；**流程图首选 PDF**。→`{SKILLS}\05_manuscript\personal\Aitor-format.md`；`word-edit.md`；`draw-flowchart`。（2026-10-24）
- **批注英文建议句**：单独成句，以 `Suggested …` 起首。字面模板技能落点→`{SKILLS}\06_review\personal\word-edit.md`。`manuscript-and-review.md` 已于 2026-10-18 按 README 迁入 `05_manuscript` / `06_review` / `07_response`。
- **审稿回复**：保留完整原始 comments；不简化；不擅自加小标题；不自创信函格式。→`{SKILLS}\07_response\personal\response.md`。
- **新建文件夹（2026-10-24 · t1107u/t1108u/t1109u）**：助手需要的**全部新文件夹**只许建在 `{DEL}` / `D:\0del\`（`_by-project` / `_by-function`）。**默认禁止**在 `D:\0Grok\0doc` 下 mkdir；**唯一例外**：城城**本轮明确同意**才可在 0doc 建新夹。可改已有文件。临时/scratch → `{DEL}`。ACCEPT 备注只落 `{DEL}`。正文以本条为准；短针→`workspace-layout.md`（不复写）。mem→`D:\0Grok\0doc\mem\README.md`；全文→`D:\0del\_by-function\encode-0doc-folder-ban-20261024\STANDING-0doc-no-new-folder.md`。
- **新建文件（2026-10-24 · t1098u）**：AI/助手**不得**在 `{DEL}` / `D:\0del` 以外**新建**文件；**可改**已有文件（含 `{RULES}` / `{SKILLS}` / `0doc\skill-harvest\*` / `0doc\mem\*` / 子工程已有稿）。**唯一例外**：bot 记忆导出/更新可在 `D:\0Grok\0doc\mem\` 内新建（§1「mem 落盘」城城指定）；mem 以外仍禁。新草稿、ACCEPT、digest、by-fine-id lane、笔记、中间件 → 只进 `{DEL}\_by-function\…` 或 `{DEL}\_by-project\…`。优先 patch 已有；用户本轮点名的终稿落点仍按 §5（优先改已有终稿）。全文→`D:\0del\_by-function\encode-0del-standing-20261024\STANDING-no-new-files-outside-0del.md`；mem→`D:\0Grok\0doc\mem\README.md`。
- **一次性脚本/说明/小补丁**（非课题交付）：只落 `{DEL}`，禁止丢进用户主目录、`.grok\tmp`、或课题根。

# 6 工程决策

- R1 需求优先 · R2 证据排错 · R3 有序简化 · R4 风险比例 · R5 保护不变量 · R6 闭环验证。
- **重大变更门**：改结构/改 ID/删目录 → 假设清单、影响、用户批准。

# 7 科研

文献只引真实来源（找不到写「未找到」）。统计不为跑通改 outcome/纳入/cutoff/协变量/缺失/模型。细则→03/04 `qc/`。

# 8 语言与汇报

说明/QC 中文；期刊英文稿英文。汇报时区 Asia/Shanghai (UTC+08:00)。「；」=两任务；「|」=同任务并列。STE→`{SKILLS}\05_manuscript\base\vocab\L3\lab-ste.md`。

# 9 按需文件

| 触发 | 读 |
|---|---|
| 网段/敏感外发 | `network-security.md` |
| 技能/PR 同步 | `skills.md` |
| 本机布局 / 子工程 | `workspace-layout.md`（无 A/B 类；见 §1 一行布局） |
| 派单/盯梢 | `{SKILLS}\00_orchestrator\references\ownership-contract.md`；`{SKILLS}\00_orchestrator\references\handoff-monitor.md` |
| 0doc 文档库查找 | Bai → `{SKILLS}\03_research\personal\0doc-db.md`；派单 SSOT → ownership-contract §0doc |
| 技能演进 | `{SKILLS}\00_orchestrator\references\skill-evolution.md`（门在 `skills.md`） |
| 稿件禁令 | `{SKILLS}\05_manuscript\qc\manuscript-local-qc.md`；`{SKILLS}\05_manuscript\base\vocab\L1\ban-phrases.md` |
| 项目 `ref/` 布局 / ledger 再跑 | `project-ref-layout.md`；`{SKILLS}\00_orchestrator\references\project-ref-layout.md` |
| 盘问 / Plan card | 本文件 §2.1；技能 `plan-and-grilling.md`（指针） |

Cursor User Rules 只一行指向本文件。「记住」：总则→本文件；专题→专题；项目→子工程约定；技能→提案；敏感→mem（禁写入 MY-RULES/MY-SKILLS）。
