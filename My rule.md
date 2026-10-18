---
name: My rule
description: Aitor（AA）科研与编程全局规则。
license: MIT
---

# 1 适用范围与优先级

- 对 Grok Bot/Aitor、子代理、Cursor、Cline 生效。
- **裁决顺序**：用户当轮表述 > 专题文件 > 本文件 > 项目 `0doc\`。
- **别名**：`{RULES}`=`C:\Users\loopn\Documents\Cline\Rules`；`{SKILLS}`=`C:\Users\loopn\.grok\skills`；`{WORK_A}`=`L:\00used`；`{WORK_B}`=`D:\0Grok`；`{RAW}`=`D:\00ds`（只读除非点名）；`{DEL}`=`D:\0del`；`{MOUNTS}`=`D:\0Grok\0doc\04-lab-reference\mounts-cap`
- **工作区**：A=`{WORK_A}\<项目>\`；B=`{WORK_B}\<子项目>\`；细则 `workspace-layout.md` + `{SKILLS}\02_data-processing\personal\workspace.md`。
- **术语**：A/B=工作区类型；作者字段 `A`=批注作者；`00`–`07`=技能层；派单→`{SKILLS}\00_orchestrator\references\ownership-contract.md`。
- **一任务一执行方**；外挂（Cursor/Cline）须用户批准。盯梢→`{SKILLS}\00_orchestrator\references\handoff-monitor.md`。
- 单项目约定写 `0doc\`（须「放 0doc」）。

# 2 开工前确认

- 只读不用授权；改/移须先授权。
- **禁删**；移出只进 `{DEL}` 并保留相对路径。
- 确认：目标与验收；假设≤3；取舍；谁执行。
- 「直接做」可不逐项确认，但不跳过 MY-SKILLS PR/merge（`skills.md`）与须批网络（`network-security.md`）。「继续」≠网络同意。
- 盘问/grill-me → `{SKILLS}\00_orchestrator\references\plan-and-grilling.md`。网络红线→`network-security.md`。

# 3 编程准则

简单优先；外科手术式；软编码；模块化；**不写回退**；新脚本 Python 3.13.9；PowerShell 不用 `&&`。细节→`{SKILLS}\02_data-processing\personal\coding.md`。

# 4 执行与验证

优先 diff；lint/测试后交终稿。**不编造**事实/数字/文献/DOI/路径。稿件禁令→`{SKILLS}\05_manuscript\qc\manuscript-local-qc.md`。

# 5 交付与清理

**禁删**；临时只进 `{DEL}\<任务>\`。

| 产物 | 格式 | 落点 |
|---|---|---|
| 报告/QC | HTML | A→`ref\`；B→子项目/`submitting\`；无→Downloads。`0result\` 只放终表 |
| 稿件/TC | DOCX | 子工程或 Downloads |
| 数据表 | XLSX | A 终表→`0result\`；其余同稿件 |

「放 0doc」才写 `0doc\`。长表→`{SKILLS}\00_orchestrator\references\standing-delivery.md`。

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
| A·B 目录 | `workspace-layout.md` |
| 派单/盯梢 | `{SKILLS}\00_orchestrator\references\ownership-contract.md`；`{SKILLS}\00_orchestrator\references\handoff-monitor.md` |
| 技能演进 | `{SKILLS}\00_orchestrator\references\skill-evolution.md`（门在 `skills.md`） |
| 稿件禁令 | `{SKILLS}\05_manuscript\qc\manuscript-local-qc.md`；`{SKILLS}\05_manuscript\base\vocab\L1\ban-phrases.md` |

Cursor User Rules 只一行指向本文件。「记住」：总则→本文件；专题→专题；项目→`0doc\`；技能→提案；敏感→mem（禁写入 MY-RULES/MY-SKILLS）。
