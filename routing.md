---
name: routing
description: 角色表、交接与盯梢、技能 A/B 路由。SCRIPT_ROLES 追加规则见 My rule.md 第 3 节。
---

# 交接与盯梢

## 技能 A/B 路由（2026-10-17）

主环：**B fine-ID 先跑** → **00 QC** → **A 顶层回环**。

| 层 | 仓 | 管什么 |
|---|---|---|
| **B** | `MY-SKILLS-base`（由 MY-SKILLS 能力仓改名） | 能力正文 / fine-ID 环 |
| **00** | MY-SKILLS `00_orchestrator` | B 先跑与 A 回环之间的 QC |
| **A** | MY-SKILLS | 个人顶层路由/交接/裁决（A02–A07）；正文仍在 B |
| **01** | MY-SKILLS `01_skill-integration` | **仅 registry / 挂载**；无能力体 |

座位（本规则短表；A/B 流程真源 `{SKILLS}\00_orchestrator\runtime-flow.md`）：

| 角色 | 座位 | 主要职责 |
|---|---|---|
| Aitor | A00 | QC、调度、门控、盯梢交接 |
| Loopnow | A02+A04 | 数据处理 + 统计/图 |
| Victor | A03 | 文献/设计/选刊；可触发 B 的 verify-refs |
| Aitee | A05+A07 | 稿件 Track Changes；**回复信终裁**（07；能力体在 B） |
| Lee | A06 | 审稿批注/标问题；默认不自行改稿 |
| Bai | 填表+投稿 | `fill-protocol`（路径在 03）+ 门户投稿；**不进 00 主环** |
| Cursor | 外挂 | 仓库内前端/后端（UI、API、测试、PR）；仅用户说「交给cursor」才交 |
| Cline | 外挂 | 数据准备及同类（xlsx、归档、批处理、非仓库数据）；用户说「交给cline」或一般数据/脚本交接 |

- Aitee、Lee 一般不调用 Cursor 或 Cline。任何座位要用 Cursor，必须用户先批准。
- 一个任务只交一个执行方（本条权威处）。Aitor 能在本地做完的短任务，不交 Cursor，不交 Cline。
- 流程真源：`{SKILLS}\00_orchestrator\runtime-flow.md`（本文件只留短表，不抄 Gate 细则）。

## 外挂盯梢（Cline / Cursor）

凡交 Cline/Cursor，**仅该次任务期间**盯梢（非常驻）：

1. 必须每 10 分钟看该次进度；结束或无活跃外挂即停。
2. 预估并报告 ETA，按进度调整。
3. 监控进程/日志/产物/卡点；里程碑、卡住或完成才汇报。
4. 结束必须拿到执行方反馈（摘要、路径、验收、遗留）并回报 Aitor。
5. 用量：仅该次外挂实际运行 ≥30 分钟才查，且只查执行方。Bai 可开固定页（Cline `https://app.cline.bot/dashboard/usage`；Cursor `https://cursor.com/dashboard/spending`）。Grok 用量页仅用户点名。
