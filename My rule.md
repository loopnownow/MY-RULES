---
name: My rule
description: Aitor（AA）科研与编程全局规则。
license: MIT
---

# 1 适用范围与优先级

- 对 Grok Bot/Aitor、子代理、本机 DeepSeek（DSH）与 Cline 生效（本机编码入口默认 **Loopnow**（`02_data-processing`）；整理 / 提取 / 填写 / 本机 IDE 作业改走 **本机 DeepSeek（DSH）** 或 **Cline**（桌面应用或 Cline CLI），在城城说「交给 DS / DeepSeek / Cline」或批准使用时调度；Cursor IDE 已卸载，不再把任务派给 Cursor IDE，也不再用「交给cursor」作为路由触发；bot **可以**调用本机 DSH 与 Cline）。
- **数据底表移动（D-1 · 2026-10-29 · t1309s6268）：** 原始/预清洗数据底表默认落 `ref/` 根（或 `ref/data/`）。**移动底表前必须先问城城**（D-1）；勿静默挪走。布局说明见 `project-ref-layout.md`。

- **裁决顺序**：用户当轮表述 > 专题文件 > 本文件 > 子工程内约定。
- **别名**：`{RULES}`=`D:\MyProjects\_Docs\GitHub\MY-RULES`；`{SKILLS}`=`D:\MyProjects\_Docs\GitHub\MY-SKILLS`；`{RAW}`=`D:\MyProjects\_DataBase`（已组织的原始库 = 课题原始件 + `_` 非课题归档分支；除 `_index.csv` 外只读；`00ds`/旧 `00db` 为旧名/QC 对象——活路径·夹名·filter 一律更正为 `_DataBase`，勿当 legacy 保留；细则 → `workspace-layout.md`「`{RAW}` = `D:\MyProjects\_DataBase`」）；`{DEL}`=`D:\MyProjects\.Del`（旧名 **0del** / `D:\0del` = `.Del`）。
- **本机布局（一行）**：`D:\MyProjects\_DataBase`（organized raw） / `D:\MyProjects\.Del`（AI 可操作临时区；旧名 **0del**） / `D:\MyProjects\_Docs`（语料 + 可复用代码） / `D:\MyProjects`（分阶段子工程工作区；阶段含 `reviewing`，旧名 `in-review`） / `D:\MyProjects\archived`（已完结冷库 `archived\<family>\…`，**非**阶段）。申请包 `_DataBase\_grants\`；评阅他人稿 `_DataBase\_reviews\`（`R&P` 已退役）。细则 → `workspace-layout.md`。
- **根路径更名（t1791u / t1794u / t1796u / 2026-11-08）：** 工程根 `D:\MyProjects`（原 `D:\0Grok`）；文档库 `D:\MyProjects\_Docs`（旧名 **0doc** = `_Docs`）；原始库 `{RAW}`=`D:\MyProjects\_DataBase`（旧名 **00db** = `_DataBase`）；移出区 `{DEL}`=`D:\MyProjects\.Del`（旧名 **0del** / `D:\0del`）。**syn 镜像目标 = `E:\Aitor` 根**（不是 `E:\Aitor\MyProjects`）。课题原始件按家族分桶：`_DataBase\<family>\<prefix_suffix>\`（`<family>`=`_diseases.csv` 的 `family` 列）；`_lab` 与其他 `_` 非课题分支留 `_DataBase` 根。冷库 `D:\MyProjects\archived\<family>\<prefix_suffix>\`（与 DB 同家族桶；进场条件见 `workspace-layout.md`）。同步：唯一入口 `D:\MyProjects\syn.bat`：`D:\MyProjects` → `E:\Aitor`，`/XD .Del`（**不同步** `.Del`；`_DataBase` 随主树同步）；无其它同步脚本或快捷方式（2026-11-08 实测）。
- **进 `_DataBase` 多文件先压缩（t1800u）：** 入库时若目录单独文件 ≥20 或明显小文件堆，先压成一个归档再入库；细则 → `workspace-layout.md`「进 `_DataBase` 多文件先压缩」。
- **单档 ≤1 GiB / 超限分卷（2026-11-09）：** 入库、交付、归档的**单个文件一律 ≤1 GiB**（1,073,741,824 B）；预计超限时直接分卷（900 MiB 字节卷，`<原名>.001`…，同夹 `分卷说明.md`），不要先造大档再拆；存量超限档按同法拆分，拼接 sha256 校验通过后原档才移 `{DEL}` 并记台账（禁删）。例外：`{DEL}` 临时件、在途中间件。细则 → `workspace-layout.md`「单档 ≤1 GiB / 分卷」。
- **accepted 收工（t1806u / t1809u / t1817u）：** harvest 后精简 `accepted\` 再进 `archived\<family>\…`；硬留终稿 + FinalData；课题树 `R*` / `P*` 整夹进 `_DataBase`（校验后原夹→`.Del\_by-project`）；细则 → `workspace-layout.md`「accepted 收工」。
- **疾病短码 / 家族桶 L1（t1821u / t1822u / t1825u / t1829u）：** `_DataBase\_diseases.csv` 为短码+家族 SSOT（列含 `suffix,...,family`）；`archived` 与 `_DataBase` 的 L1=`<family>`（`family` 列；留空=自家族基码）；叶后缀仍用基码（剥末尾 `_\d+` 实例；语义复合整段保留）；实例号只在叶子 `<prefix_suffix>`；全称只进表；ethics/references 仍用 library L1/L2。**同源聚合**：同影像/队列母集或共用 raw → 同 `family`；非同源可自家族；共用 raw 只存一份（优先家族原始件池 `_DataBase\<family>\_share\`——2026-11-09 起亦收原始数据/原始记录/原始图片、伦理申请材料、学位论文；或主叶 + 指针）；表格去重合并入 `<family>\_db\<family>db`，叶内只留 `目录说明.md`，压缩档（非表格）只进 `_share\`，档内表格解出入库（2026-11-09）。细则 → `workspace-layout.md`「按家族分桶」/「同源聚合」/「家族库 `_db\`」/「archived 冷库」。
- **伦理材料留存（t1849u）：** 批件原件仅日期 ≥ 2023-11-10 进 `_DataBase\<family>\_share\ethics\`；临床研究方案 + 知情同意书全留同夹；`_DataBase\_lab\ethics` 废弃 → `.Del`（盘面由 Bai）。细则 → `workspace-layout.md`「伦理材料留存（t1849u）」。
- **库分类（t1458u）**：L1/L2 与三库分工的权威正文 → `library-taxonomy.md`。`_library` 下 `references`（全文实体）/ `lit-bank`（书目，无 PDF）/ `journals`（期刊池，含选刊侧私有 `whitelist-submitted.csv` / `submission-prior.jsonl`）/ `ethics\approvals`（批件）；不设 radiology 一级，按临床专科归类。
- **术语**：作者字段 `A`=批注作者；`00`–`07`=技能层；派单→`{SKILLS}\00_orchestrator\references\ownership-contract.md`。工作区只有一层；不再有 A/B 双工作区或挂载缓存树。
- **技能 ID**：选型只按 fine id；细则 → `skills.md` §2；`{SKILLS}\00_orchestrator\references\id-rules.md`。
- **一任务一执行方（t1595u / t1960u）**：**编码 / 脚本 / MY-CODES 工作交给 Loopnow**（粗席位 `02_data-processing`；`{code_root}` / `{code_stats}` 落码）。整理 / 提取 / 填写 / 本机 IDE 作业改走 **本机 DeepSeek（DSH）** 或 **Cline**（桌面应用或 Cline CLI）；城城说「交给 DS / DeepSeek / Cline」或批准使用时调度。Cursor IDE 已卸载，不再把任务派给 Cursor IDE，也不再用「交给cursor」作为路由触发。bot **可以**调用本机 DSH 与 Cline。盯梢→`{SKILLS}\00_orchestrator\references\handoff-monitor.md`。
- **选模型（本机 DSH / Cline；2026-10-30 · t1452u；t1960u）**：调用本机 DSH 时用该 profile 当前默认模型；调用 Cline 时用 Cline 当前配置的模型。
- **Rules 必须挂载并必须遵守；Skills 仅在派工时附加（t1397u；t1595u 强化）**：`{RULES}`＝`D:\MyProjects\_Docs\GitHub\MY-RULES`（本文件 `My rule.md` + 专题文件）。**Aitor 与全部专员 bot（Loopnow / Victor / Aitee / Lee / Bai 等）以及云端 Cursor / CloudAgent 一律必须遵守**，无例外、无需再问。**派子 bot/专员或云端执行时默认携带 `{RULES}`**；**仅当派具体 fine id / 工作包时，才附加 `{SKILLS}`**（相关 fine id / 路径，或整库 SSOT）。冲突裁决：**Rules > Skills**。**「Skills 未挂载」不得作为跳过 Rules 的理由**（Skills 缺省只影响该任务能否用该技能，不影响 Rules 生效）。CloudAgent prompt **必须写明 Rules 路径**；Skills 按本次任务写入，勿假设云端已挂载。
- **云端 / 本地（术语，2026-10-25）：** **云端** = Grok Bot 的 box 计算机（`/workspace` 等）；**本地** = 城城本机（如 `D:\`、Downloads）。二者勿对调。
- **mem 落盘：** bot 记忆导出/更新落在本地 `D:\MyProjects\_Docs\mem`（城城指定；非默认进 `{DEL}`）。mem **仅保留隐私**与可变数据 SSOT（如 JCR xlsx）；站立运营政策进 `{RULES}`，专业技能进 `{SKILLS}`。bot 站立记忆正文也只保留敏感信息（称呼、Vault 条目名、账号与本机路径指针、lit-bank 个人过滤）；运营与技能口径不进记忆。
- **本机库可写字段（t2033u）：** 姓名、电话可写入本机 `_DataBase` 家族 SQLite（`<family>db`，不进 GitHub）。不得写入 MY-RULES、MY-SKILLS、MY-CODES、skill-harvest、回执或聊天。身份证与地址默认不进该库，除非城城当轮新授权。
- **单项目约定**写在该**子工程文件夹**内（如子工程 `_Docs\` 或 `ref\`），**不**写入全局 `{RULES}` / `{SKILLS}`。须用户点名「放 0doc」/「放 _Docs」才写 `_Docs\`（旧名 0doc）。
- **交付落点**：子工程**没有** `0result\` 文件夹。**最终**交付物 → 该子工程**根目录**（`D:\MyProjects\<project>` 下）；**中间**产物 → 按 `project-ref-layout.md` 的 `ref/` 子文件夹地图（`review/` / `citation/` / `refer/`（文献+写作参考 pptx/doc/docx） / `code-gates/` / `tmp/` + 根上 tables/figures/pipeline；**hashes/MANIFEST/pipeline_run.log 在 `ref/pipeline/`**；`submission-*`、底表；分析 `false_classification*` 落**当次结果夹** `<project>/<endpoint>/`（**非**子工程根，亦不进 `ref/`；详图与 Cleanup 两档见 `project-ref-layout.md`；已退役 `analysis/`/`materials/`/`results/`/`exec/`/`code/`/`gates/`/`writing-refs/`/`raw-pre/`））；**子工程内临时/中间默认 `ref/tmp/`**（**非**默认 `{DEL}`；旧版 `Manuscript_*_V*` 亦然，现行 `Vn` 在根；详 → `project-ref-layout.md`）；无子工程或不属课题树的临时进 `{DEL}`；Downloads **仅当**当轮点名「下载」或「Downloads」。**文献全文（PDF/HTML）SSOT = `D:\MyProjects\_Docs\_library\references\<L1>\<L2>\`**（t1455u）：子工程 `ref/refer/` 只留 `DOI_*.md` 指针 + NLM/摘要 + 写作参考，不再存第二份全文；`_library\lit-bank` 只存书目。

# 2 开工前确认

- **写盘总闸（t1672u）：只读不用授权；任何写盘先问。**除非城城 / owner**当轮明确要求**该项改动（点名文件 / 路径 / 任务，或对该项工作说「改 / 写 / 更新 / 修 / 推合 / 直接做」），agent 在**新建、编辑、覆盖、移动、删除任何文件**前必须**先问并等到「是」**；未获授权即停，不静默落盘。范围覆盖全部 bot / CloudAgent / 本机 DSH / Cline，及 `{RULES}` / `{SKILLS}` / MY-CODES / `_Docs` / 子工程 / `{DEL}` / mem 等任何位置。
- **授权按项按轮（t1672u）**：当轮点名目标的授权**只覆盖该项**（如「改 A 第 3 节」只授权 A 的该处）；「直接做」只授权当轮那件事。**「继续」/ 未点名写盘的泛泛「好」≠ 写盘许可**，不得当全库放行。既有须问条款（D-1 移底表先问；网络须批；MY-SKILLS PR/merge 确认；Word「城城已改先问」）**继续有效**；本条是**所有**写盘的默认线。
- **禁删**；移出只进 `{DEL}` 并保留相对路径。**旧稿清理**＝移入 `{DEL}` / `D:\MyProjects\.Del`（可按 `_by-project` / `_by-function`），禁止静默永久删除。
- 确认：目标与验收；假设≤3；取舍；谁执行。
- 「直接做」可不逐项确认（**写盘仍只限该项**，见上条 t1672u），但不跳过 MY-SKILLS PR/merge（`skills.md`）与须批网络（`network-security.md`）。「继续」≠网络同意。
- **后果性操作（t2033u）：** 投稿 Approve、付 APC、改稿开跑、接审等，先出计划，等城城明确「同意」再执行。
- **三仓 QC（t2033u）：** 默认由 Aitor 本人做；城城点名交给其他 bot 时除外。
- **三仓改动流程（t2033u）：** 全部改动先在本地分支完成（测试通过），出示完整变更清单，再请城城批准开 PR；禁止未完成就分段开 PR。仅当城城说「合」「和」或「推合」时才 merge。MY-SKILLS 细则 → `skills.md` §5；MY-RULES / MY-CODES 同样遵守。
- 网络红线→`network-security.md`（含本机出站代理常设 `127.0.0.1:10808`；DSH 禁公网隧道、Cloud Agent 区域模型、机构库检索同文件）。

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
- **必须写 docstring / help（t1622u）**：新写或改动的可调用面（模块、函数/方法、CLI 入口）须带 docstring；有命令行入口的还须有可用的 `--help` / argparse help 文本。docstring/help 写清做什么、怎么调（参数/返回/异常或用法）；**不写**长业务「为什么」。与上条「仅注释配置和脚本运行说明」并存：行内注释仍只覆盖配置含义与运行说明，接口说明走 docstring/help。既有 MATLAB `.m` 用同等 help 头注释。
- **不写回退**：禁止 fallback / 静默降级（勿用 try-except 吞失败后走默认路径）；失败要响，暴露错误。
- **可以写多模块并配置可选**：允许多模块；模块可用配置开关可选启用。
- **dry-run**：批量 IO / 写盘前先试跑，打印将执行的操作供确认；默认 dry-run，显式 `--execute` / `--apply` 才落盘。
- **测试→运行→核查→验收**：所有脚本先测试再运行，最后核查，再验收。顺序固定：(1) 先测（unit/smoke/dry-run 视情）；(2) 再跑正式任务；(3) 核查结果；(4) 验收通过后再宣告完成。
- **断点续传**：已处理结果跳过；以中间文件或完成标记续跑，勿整段重算。

细节（模板、阶梯、QC）→`{SKILLS}\02_data-processing\advanced\coding.md`。

# 4 执行与验证

优先 diff；lint/测试后交终稿。**不编造**事实/数字/文献/DOI/路径。稿件禁令→`{SKILLS}\05_manuscript\qc\manuscript-local-qc.md`。技能树 QC：**禁止 skip/archived 停放**；skipped/archived 与**退役仅指针壳**均为清理对象→`skills.md` §6（t1520u）。**QC 不得 ignore / 跳过**→`skills.md` §6（t1559u）。脚本站立流程见 §3「测试→运行→核查→验收」。

# 5 交付与清理

**禁删**；子工程内临时/中间默认 `ref/tmp/`（非默认 `{DEL}`）；无子工程或跨课题一次性临时进 `{DEL}\<任务>\`。旧稿/旧产物清理＝移入 `{DEL}`，不静默永久删。子工程**不建** `0result\`。

| 产物 | 格式 | 落点 |
|---|---|---|
| 最终交付（稿件/终表/最终报告等） | 依类型 | **子工程根目录**；无子工程且点名「下载/Downloads」→Downloads；否则→`{DEL}` |
| 中间产物（QC/ledger/门控/草稿等） | 依类型 | 有子工程→按 `project-ref-layout.md` 的 `ref/` 地图（`review/`/`citation/`/`refer/`（含写作参考）/`code-gates/`/`tmp/` + tables/figures/pipeline；locks 在 `ref/pipeline/`；`submission-*`；`false_classification*` 在 `<project>/<endpoint>/` 结果夹（**非**子工程根；详图见 `project-ref-layout.md`））；否则→`{DEL}` |
| 报告/QC（中间） | HTML | 有子工程→该子工程 `ref\`（或阶段夹如 `reviewing\`）；无子工程且点名 Downloads→Downloads；否则→`{DEL}` |
| 稿件/TC（最终） | DOCX | 子工程**根**；否则仅当点名 Downloads，否则 `{DEL}` |
| SCI 稿件文件名 | DOCX（md/pdf 同 stem） | **`Manuscript_` / `Comments_` / `Response_` / `Supplementary_`** + `_<子项目名>_` + `V主.次` 或 `R轮.次`（校样可选 `P1`）；小数不补零、按数值排；投稿前与投后未审用 V，收到意见后用 R，换阶段夹不改号，不发明 R0；Comments/Response 与同轮 R 同号；现行版在子工程根、旧版 `ref/tmp/`（t1694u，覆盖 2026-11-05 纯 V 映射）。权威 → `project-ref-layout.md`「SCI 稿件文件名」；技能指针 → `{SKILLS}\05_manuscript\advanced\Aitor-format.md` / `handoff.md`、`06_review\advanced\handoff.md`、`07_response\advanced\handoff.md`（t1428u/t1429u/t1430u） |
| 数据表（最终） | XLSX | 子工程**根**（不建 `0result\`）；其余同稿件 |
| 文献全文（PDF/HTML） | PDF/HTML | **`D:\MyProjects\_Docs\_library\references\<L1>\<L2>\`**（一文一物理文件，名用 DOI；t1455u）。子工程 `ref/refer\` 只写 `DOI_*.md` 指针；书目仍进 `_library\lit-bank`（不存 PDF） |
| 期刊池 / 批件 | CSV/XLSX/PDF | `_library\journals\index.csv`（单表，2026-10-31 起不再留 xlsx）；`_library\ethics\approvals\<L1>\<L2>\` + `approvals-index.xlsx`（t1458u）。子工程候选刊只写 `ref\citation\journals.csv` + `_notes.md`；批件只挂指针。口径 → `library-taxonomy.md` |

同一分析若 `Results*.html`（或已执行产物 HTML）与 `.xlsx` 数字冲突：以 HTML 为准，并在汇报里写明冲突与所采用源。

**结果 HTML 落点（t1660u）**：分析结果 HTML 只落该次结果夹 `<project>/<endpoint>/`（或解析出的 OUT_DIR / `SUBPROJECT_BY_OUTCOME` 夹），文件名 `Results*.html`（见 `workspace-layout.md`）。**不**把 `{slug}_results.html`、旧 `{endpoint}-results.html` / `results.html` 提升到子工程根；子工程根上已有的旧结果 HTML 属错位，后续整理时先问再移入 `{DEL}`。

「放 0doc」才写 `_Docs\`。长表→`{SKILLS}\00_orchestrator\references\standing-delivery.md`。

# 5.1 Word / 审稿回复 / 本机目录（2026-10-19）

- **Word/PDF 格式**：未经当轮点名，禁止改 `.docx`/`.pdf` 版式；改文字用修订模式。词/句级修订，禁止大段覆盖。细则→`{SKILLS}\06_review\advanced\word-edit.md`。
- **城城已改先问（全局停）**：若 Word/手稿正文与城城（用户）已编辑文本不同（修订痕迹 / 已知本人改动），**必须先问再改**，禁止擅自覆盖或改回。技能须指针本条，勿只埋在 revise。→`word-edit.md`；`writing-rules-hard.md`；`07_response` revise。（2026-10-24）
- **城城手改识别（版本号抬升 · t1757u）**：子工程根最新 `Manuscript_*_V/R/P` 若版本号**大于**上次助手落地版 → 视为城城手改 live 稿；**禁**从 bak/`-org`/collapsed 整文件还原或覆盖；只许 Track Changes（作者 A）增量；不降号；**不**另建 `OWNER.md` / `.owner.docx` / lock 标记。权威 → `project-ref-layout.md`「城城手改识别」。小改不升号与未升号不得反推「不是手改」→ 同文件「SCI 稿件文件名」与「城城手改识别」（t1946u）。
- **无稿不造空件（t2033u）：** 子工程若无稿件 docx，记「无 docx」，不得为交差创建空稿。
- **统一版式**：手稿、审稿意见、审稿回复同一套——正文 Times New Roman 12、1.5 倍行距、段前后 0、两端对齐、LTR、特殊格式无；**表格单元格 12 pt**；**图内文字 Arial**（与正文双轨）；**流程图首选 PDF**。→`{SKILLS}\05_manuscript\advanced\Aitor-format.md`；`word-edit.md`；`draw-flowchart`。（2026-10-24）

- **图表编号（C-1 · 指针，2026-10-29 · t1309s6268）：** Table 1 = 基线；**不**单独放 logistic 系数表或 score-correlation 表（Aitor-format §209）；ROC 操作特性作表；图按适用放 workflow / US / heatmap / nomogram+校准 / ROC / DCA。细则勿在本文件复写，指针 → `{SKILLS}\05_manuscript\advanced\Aitor-format.md` §200 / §209 / §213。
- **批注英文建议句**：单独成句，以 `Suggested …` 起首。字面模板技能落点→`{SKILLS}\06_review\advanced\word-edit.md`。`manuscript-and-review.md` 已于 2026-10-18 按 README 迁入 `05_manuscript` / `06_review` / `07_response`。
- **审稿回复**：保留完整原始 comments；不简化；不擅自加小标题；不自创信函格式。→`{SKILLS}\07_response\advanced\response.md`。
- **新建文件/文件夹（权威；合并 t1098u/t1107u/t1240 · 2026-10-30 · t1442u/t1450u）**：默认只能在 `{DEL}` / `D:\MyProjects\.Del`（`_by-project` / `_by-function`）新建文件与文件夹；路径 SSOT 为 `D:\MyProjects\.Del`（旧名 `D:\0del`；非 `D:\MyProjects\0del`）。在其他位置新建前必须本轮明确问城城并获准。**常设例外（仅限新建）**：(1) bot 记忆导出/更新可在 `D:\MyProjects\_Docs\mem\` 内新建（§1「mem 落盘」）；(2) 子工程内 `ref/tmp/` 按需写入临时/中间（含旧版稿；详 → `project-ref-layout.md`）。以上只是**新建路径**的例外，**不是编辑许可**：这些位置已有文件的编辑 / 覆盖 / 移动仍按 §2 写盘总闸，须当轮点名或先问（t1672u）。**改已有文件同样先问（t1672u）**：`{RULES}` / `{SKILLS}` / `_Docs\harvest\*` / `_Docs\mem\*` / 子工程已有稿（含 Track Changes）**均不豁免**——除非城城当轮已点名要改该文件 / 该处，否则先问再改，不得以「属可改区」为由静默编辑。默认禁止在 `D:\MyProjects\_Docs` 下 mkdir（除 mem 例外与本轮明确同意）。新草稿、ACCEPT、digest、by-fine-id lane、笔记、中间件、临时/scratch、ACCEPT 备注 → 只进 `{DEL}`。审稿交付：优先修订现有评审意见 `.docx`（Track Changes），禁止另存新稿名、禁止在子工程下新建夹。用户本轮点名的终稿落点仍按 §5（优先改已有终稿）。短针→`workspace-layout.md`（不复写）；mem→`D:\MyProjects\_Docs\mem\README.md`；全文→`{RULES}\standing\STANDING-no-new-files-outside-Del.md` 与 `{RULES}\standing\STANDING-docs-no-new-folder.md`（2026-10-31 从 0del 移入本仓；**0del 不再承载任何全文/指针**）。
- **一次性脚本/说明/小补丁**（非课题交付）：只落 `{DEL}`，禁止丢进用户主目录、`.grok\tmp`、或课题根。
- **_Docs 目录名英文化（t1458u）**：`_Docs` 下新建目录一律 ASCII 英文（如 `approvals` / `journals` / `jcr` 这类英文短名）；发现中文目录当轮 rename，并在 `_library\MOVED-FROM.md` 记一行。文件名可保留中文原名，但须在对应索引列留映射（如 `original_name_zh`）。库分类口径 → `library-taxonomy.md`。



## 5.2 每轮 QC 必清 _Docs（2026-10-27）

- **每轮质控必须跑一次无用件清理**（`D:\MyProjects\_Docs`）：`python -B test\cleanup_scan.py --tsv <清单>` → 人工确认 → `python -B test\cleanup_move.py --plan <清单> --apply`，移入 `{DEL}\_by-function\0doc-qc-clean\<YYYYMMDD>\`，保相对路径并落 `MOVED.tsv`。
- **判据只有三条**：有没有入口 / 有没有真实落点 / 能不能再生。「看起来旧」不是理由；只剩历史价值 → 留档并标注，不计清理成绩。
- **默认分级**：字节码缓存、垃圾文件名、空目录、历史结构快照、被同名无日期版取代的副本 → 可直接移；重复件、无入口脚本、无读者台账、孤立 `.md`、占位壳 → 出清单等点头；断链与「文中路径全失效」→ 只修指针或就地标注，**不搬**（历史档合法引用过去落点）。
- **永不自动清**：`_library\glossary\banks`（含 `glossary.db`）、`mem\`、`_library\ethics\`，以及历史档 `MIGRATION.md`、`ACCEPT-*`、`_library\former-*`、`harvest\PLAN-*`。
- 移出即记台账；收工报告须给「一条命令还原」的路径映射。分类说明→`_Docs\test\README.md`。
- **skip / archive / 退役仅指针 不是停放位**：口径见 §4 与 `skills.md` §6（t1463u；t1520u；**t1559u 不得 ignore/跳过假绿**）；_Docs 侧由 `test\structure_check.py` S4 与 `test\cleanup_scan.py` C2 强制，**无存档例外**（年报/年表同样移 `{DEL}`，见 `_Docs\STRUCTURE.md` §7）。


## 5.3 `.Del` 三档（旧名 0del · 2026-10-31；路径 t1794u）

`{DEL}` 内移出件按可弃度分三档，**不得混放**；每档一个落点，搬移必留 `MOVED.tsv` 并保相对路径。

| 档 | 落点 | 判据 | 处置 |
|---|---|---|---|
| park | `_by-function\<批次>\` / `_by-project\<课题>\` | 有活指针、台账价值，或一次任务的全套件（旧稿、ACCEPT 回执、`MOVED.tsv`） | 留到城城点名；**不得**整夹清 |
| harvest-park | `_by-function\harvest-docs-<YYYYMMDD>\<原相对路径>` | `_Docs` 新建件的收尾归档（草稿已「进skills」收编，或已过时） | 留档；下次 QC 复核后再定留或降 harvested |
| harvested | `harvested\`（平铺，不建日期子夹；原 `junk\`，2026-10-31 改名） | 一次性批次、字节码/缓存、拼写错件、本机配置备份、Downloads 残留、**无任何文本引用**的产物 | **只由城城手动清**；bot 不清、不代清 |

- **课题件优先** `_by-project\<slug>\`（park）；**_Docs 收尾件**（草稿已收编进 skills、或已过时）才进 harvest-park。两档不得互替堆放。一次 harvest 之后应进 `{DEL}` 的剩余件除外，见下条 t1950u。
- **harvest 剩余件落 harvested（t1950u）：** 一次 harvest（抽「怎么做」）之后，凡按分流应进 `{DEL}` / `D:\MyProjects\.Del` 的剩余件（含原可进 `_by-project` 或 harvest-park 的收尾件），一律落 `harvested\`（平铺，不建日期子夹）。抽出的 how-to 仍进 `_Docs\harvest`；进 `_DataBase` / `_Docs` 活库 / `archived` 的分流不变。非 harvest 的 `.Del` 落点不变（如 closeout 可复现图、入库后原散目录、课题 park、Downloads 残留等仍按本条 park / harvest-park / harvested 三档）。落 `harvested` 前仍须：① 全库 grep 无活文本引用（有活指针先改指针或仍留 park，不得带着活引用进 harvested）；② 同名异字节不覆盖（文件名加 slug 或当轮 id 区分，不建日期子夹）；③ 写 `harvested\MOVED.tsv`。清空口径不变：`harvested` 只由城城手动清，bot 不清、不代清；park / harvest-park 仍不得整夹清。
- 落 harvested 前必须：① 全库 grep 确认无活文本引用（`_Docs` + `D:\MyProjects` 课题树）；② 同名异字节不覆盖；③ 写 `harvested\MOVED.tsv`。
- **harvested 是唯一的终弃档，且只由城城手动清空**（bot 不清、不代清、不自作主张）；park / harvest-park 不得整夹清。
- `_Docs` 侧的判定与落盘仍由 `test\cleanup_scan.py`（判据）与 `test\cleanup_move.py --dest <落点>`（落点）负责；本条只定**落点与可弃度**，不另造脚本。
- **禁止活指针引用 `{DEL}`（2026-10-31）**：`{RULES}` / `{SKILLS}` / `_Docs` 文档与脚本**不得**把 `D:\MyProjects\.Del\...`（或旧字面 `D:\0del\...`）当作当前落点或路径解析目标（0del 会周期性清空）。需要长期存在的全文/台账/脚本一律放耐久位置（`{RULES}` / `{SKILLS}` / `_Docs` / `project root`）；历史记录里的 0del 路径由 `test\path_audit.py` 归 `HISTORIC`，但**不得新增**活指针；要清空 `.Del` 前先把活指针重指。
- **整理 `.Del`（旧 0del）前先 grep 活路径**：`_code` 多个脚本把输出写死到 `{DEL}\<子夹>` / `D:\MyProjects\.Del\<子夹>`（一律在 `harvested\` 下：`smoke`、`modules_bak`、`cln_fill_supplement`、`yt_RDL`、`batch_rerun_status.json`、`batch_rerun.log`；t1490u），这些不是移出件，搬走即破坏脚本；新增写死路径须同轮补入本节清单。
- **`{DEL}` 外还有一类活依赖：本机 DSH profile 的 `link:` 依赖（t20261113i）**：`D:\DS\.dsh\profiles\<profile>\package.json` 的 `dependencies` 可直接 `link:` 到 `{DEL}` 下插件源码（2026-11-13 实例：`dsh-ds-pricing` → `.Del\_by-function\dsh-plugin-ds-pricing\bundle`）；整理 `.Del` 前同轮 grep 配置文件里的 `.Del` 字面。解依赖：插件源码迁耐久位 `D:\DS\.dsh\local-plugins\<plugin>\`、改 link、`pnpm install --offline`；运行中的 DSH 仍持有旧目录句柄（目录 rename 报 WinError 5/32），旧副本须等 DSH 重启后再搬。

### 5.3.1 先判 harvest 需求，再定落点（t1951u）

批次进 `_by-function` / `_by-project` 后**先分四类**，再谈落点。**不需要 harvest 的内容不进 harvest 队列，核对后直接落 `harvested\`**。

| 类 | 判据 | 要不要 harvest | 落点 |
|---|---|---|---|
| **H1 可复用 how-to** | 规程 / 口径 / 决策理由 / 踩坑 / 验证法 / 清单或报表格式 | **要**（HARVEST-STANDARD §7 三桶） | 抽进 `_Docs\harvest`；**抽完即搬** `harvested\` |
| **H2 不需要 harvest** | 数据底表/导出、原始件、PHI 或伦理相邻件、第三方源码树、构建产物、浏览器/探针配置、一次性台账修补脚本、日志截图、缓存 | **不抽**（不进 harvest） | 核对唯一副本后**直接落** `harvested\`，不停 park |
| **H3 活依赖** | 被活代码当输入/默认路径（`DEL_ROOT` / `DEFAULT_BATCH` / `--del-root`），或被活文档给出可运行绝对路径 | 含 how-to 的先抽（H1）；本体**先解依赖再搬** | 解依赖前留 park；解完落 `harvested\` |
| **H4 课题件** | 单课题中途/收尾件、旧稿、投稿包、课题专用脚本 | 按需 | `_by-project\<slug>\`，**不进** `harvested\` |

- **park 不是长期仓**：`_by-function` / `_by-project` 常态应为空。批次完成即按 H1–H4 分流，禁止积压（2026-11-10 实测一处积压 239 项 / 45.9 GB，即反例）。
- **H2 没有「等下次 harvest」这一步**：不抽 how-to 的件不需要排队，也不必等「确认无用」——只做三查（唯一副本已在他处 / 同名异字节不覆盖 / 写 `MOVED.tsv`）即可落 `harvested\`。
- **H3 解依赖两条标准路径**：① **代码侧**——把写死的输入改指耐久位或 `harvested\`（例：`DEL_ROOT` / `DEFAULT_BATCH` / `--del-root` 默认值），跑一次门禁与单测后再搬；② **文档侧**——把活指针改成「历史落点」或指向耐久副本，再搬。两条都做不了（或缺授权）→ 留 park，并在该批次 `目录说明.md` 写明阻塞原因与解除条件。
- **H3 优先瘦身，别整批压着**：活脚本只吃少数文件时，先搬大件、留必需件在批次根。实例：`verify_db.py` 的台账 glob 是**一层深**（`*/*MOVED*.tsv`，即 `<batch>\*.tsv`），故可留 `*.tsv` + `目录说明.md` 在批次根、把 `originals/`、`staging/`、`backup-*/` 等搬走；不得为保脚本把 10 GB 级批次长期占着 park。搬前须查该批 `--from-originals` 这类重建路径是否仍需要。
- **工作夹：耐久层 vs 瞬态（t1951u）**：判据是「后人能否**复算**该数字/结论」。能 → 耐久；只是本次执行过程 → 瞬态。
  - **耐久层 = 活层三件**：`rounds\LEDGER.tsv`（一轮一行：round / 日期 / 来源 / lane 数 / promote PR / 离场日期 / `{DEL}` 落点 / owner 口径 / retro）+ `by-fine-id\<fine-id>.md`（累积草稿，promote 后不清空，下轮追加）+ `HARVEST-STANDARD.md`。
  - **瞬态 = 轮次夹 `_Docs\harvest\rounds\<round>\`**（只存在到 promote 前），固定形态：`HARVEST-*.md`（三桶正文）/ `INDEX.md`（来源·覆盖·分流）/ `MANIFEST.tsv`（逐件 sha256 + 决策）/ **`evidence\`**（判定证据：`dir-agg.tsv`、`proc-candidates.tsv`、`delta.tsv`、`moves-plan.tsv` + 门禁日志）/ `tools\`（可复用扫描·分档脚本）。**不放实体镜像**（源在库内，正文用 `MANIFEST.tsv` 的 `relpath` 指路）。正文引证据用 `evidence\...` 相对路径。
  - **瞬态工作夹 = `.Del\_<task>-<YYYYMMDD>\`**（下划线前缀工作夹，与 `_by-function` / `_by-project` / `harvested` 并列）：试跑输出、草稿 `*.new.md`、已有耐久副本的脚本体、临时 dump、探针日志。
  - **抽走即离场**：该轮内容 promote 进 live（或判 H2 不抽）后，整轮移 `{DEL}\harvested\rounds\<round>\`，活层不留轮次夹、只留 LEDGER 一行；抽走前把可复算证据摘要写进 PR 说明。
  - **探针/一次性脚本**（不进 harvest 的 H2 件）**不要**为「可能有用」在 `_Docs` 建夹存盘；要么进该轮 `tools\`，要么随工作夹落 `harvested\`；工作夹**不得**长期留在 `.Del` 根（会被当移出件误清）。

### 5.3.2 harvest 对象范围与产物形态（t1952u）

1. **对象三类**：`.Del` 移出件、`_library` 机器库（references / lit-bank / journals / ethics / glossary / lab-ref-ranges / scanner-registry）、`_DataBase` 原始库（`<family>\_db` / `_share` / 叶 `ref\settings.ini` / `目录说明.md`）。**fine-id 不是对象来源，而是 lane 坐标系**（现行 22 个，见 `{SKILLS}\\NN_slug\base\`）。
2. **抽什么**：能跨课题重放的**动作 / 判据 / 格式 / 踩坑**（三桶）。**不抽**数据本体：影像与 DICOM、文献 PDF 全文、批件 PDF、PHI（含 ICF/方案正文）、未发表全文、期刊全量行、glossary `banks\` 证据库。
3. **lane 只用现行 fine-id**；跨切面进该席位 `advanced\`；纯规则进 `{RULES}`。**禁止自造 lane**（2026-11-10 实测一轮 harvest 里 6 节有 5 节用了不存在的 lane，全部返工）。
4. **快照不保留**：`harvest` 只收「正文 + `MANIFEST.tsv` + `evidence\` + `tools\`」；**实体镜像（`from-by-*`）不进 `_Docs`**。移出前须证「每个镜像都有同 sha 对应件在库内」（2026-11-10 实测 414 件镜像 0 孤本），移出照 §5.3 进 `harvested\` 并记台账。
5. **布局固定**：`README.md`（一页索引）/ `HARVEST-STANDARD.md` / `by-fine-id\<fine-id>.md` / `rounds\<YYYYMMDDx-round>\`（瞬态，promote 后离场）+ `{doc_harvest_sources}`（= `_Docs\harvest-sources-park`，耐久 park，非草稿；2026-11-14 从 `harvest\sources\` 整棵迁出）。一次性批次并入草稿后原夹移 `harvested\`，**不新造平级夹**。

# 6 工程决策

- R1 需求优先 · R2 证据排错 · R3 有序简化 · R4 风险比例 · R5 保护不变量 · R6 闭环验证。
- **重大变更门**：改结构/改 ID/删目录 → 假设清单、影响、用户批准。

# 7 科研

文献只引真实来源（找不到写「未找到」）。统计不为跑通改 outcome/纳入/cutoff/协变量/缺失/模型。细则→`{SKILLS}\02_data-processing\qc\`（`method-validation-gate.md` / `report-checks.md` / `html-results.md`）。

# 8 语言与汇报

说明/QC 中文；期刊英文稿英文。汇报时区 Asia/Shanghai (UTC+08:00)。「；」=两任务；「|」=同任务并列。STE→`{SKILLS}\05_manuscript\base\vocab\L3\lab-ste.md`。
写作证据席位：`GLOSSARY_ROOT`=`_Docs\_library\glossary`（**四层** md + `index.csv`；`banks\` 只作证据）。判据 SSOT = `{SKILLS}\05_manuscript\base\vocab\`（+ 具名 advanced）；`rule_ptr` 指回技能，不复制规则正文。
标点：允许 Unicode minus U+2212 `−`（负号/有符号数/如 Q3−Q1）；ASCII `-` 与 en dash U+2013 `–` 仍可用。仍禁 em dash U+2014 `—` 与 spaced `--`；`≈` 仍禁。**作用域：** 该禁只针对英文稿件/对外英文文本；中文行文「——」不受限；spaced `--` 同理只限英文。细则 → `{SKILLS}\05_manuscript\base\vocab\L1\ban-phrases.md`（owner t1761u / 2026-11-07）。

# 9 按需文件

| 触发 | 读 |
|---|---|
| 网段/敏感外发 / 本机出站代理 | `network-security.md` |
| 技能/PR 同步 | `skills.md` |
| 本机布局 / 子工程 | `workspace-layout.md`（见 §1 一行布局） |
| 冷库 / `_DataBase` 非课题分支 | `workspace-layout.md`（「archived 冷库」+「`{RAW}` 非课题分支」） |
| 散表归并 / 建库 `_db` / 叶 readme / 压缩档 `_share` / DB 台账 | `workspace-layout.md`（「散表归并与表格入库」「家族库 `_db`」「`_share` 家族原始件池」） |
| accepted 收工 | `workspace-layout.md`（「accepted 收工」） |
| 工作区关系 / harvest↔closeout | `workspace-layout.md`（「工作区关系：阶段 · 分流 · harvest · 冷库」） |
| 三仓分工 / 某内容该放哪 | `README.md`（RULES=运营规则，SKILLS=专业技能，MY-CODES=脚本） |
| 派单/盯梢 | `{SKILLS}\00_orchestrator\references\ownership-contract.md`；`{SKILLS}\00_orchestrator\references\handoff-monitor.md` |
| _Docs 文档库查找 | Bai → `{SKILLS}\03_research\advanced\docs-db.md`；派单 SSOT → ownership-contract §_Docs |
| 技能演进 | `{SKILLS}\00_orchestrator\references\skill-evolution.md`（门在 `skills.md`） |
| harvest 任务流程 / 纳入门禁 | `{SKILLS}\00_orchestrator\harvest\SKILL.md`（00 只调度/门禁/复核；收集标准 `{doc_root}\harvest\HARVEST-STANDARD.md`） |
| 稿件禁令 | `{SKILLS}\05_manuscript\qc\manuscript-local-qc.md`；`{SKILLS}\05_manuscript\base\vocab\L1\ban-phrases.md` |
| 项目 `ref/` 布局 / ledger 再跑 | `project-ref-layout.md`；`{SKILLS}\00_orchestrator\references\project-ref-layout.md` |
| 伦理材料留存 / `_lab\ethics` 退役 | `workspace-layout.md`（「伦理材料留存（t1849u）」） |
| 库分类 / L1-L2 / 三库(references·lit-bank·journals·ethics) / 批件与期刊池 | `library-taxonomy.md` |
| 盘问 / Plan card | 本文件 §2.1；技能 `plan-and-grilling.md`（指针） |

Cursor User Rules 只一行指向本文件。Cursor IDE 已卸载，该入口不再维护；规则仍以本仓为准。「记住」：总则→本文件；专题→专题；项目→子工程约定；技能→提案；敏感→mem（禁写入 MY-RULES/MY-SKILLS）。
