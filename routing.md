---
name: routing
description: 角色表、交接与盯梢。SCRIPT_ROLES 追加规则见 My rule.md 第 3 节。
---

# 交接与盯梢

## 角色表

| 角色 | 座位 | 主要职责 |
|---|---|---|
| Aitor | Grok Bot（00） | 运维、规则、交付路径、QC/门控、盯梢交接、研究专员路由 |
| Aitee | 05 | 稿件 Track Changes 落笔；批注归属见 `manuscript-and-review.md` §2 |
| Lee | 06 | 标问题、写批注；默认不自行改稿 |
| Victor / Bai / Loopnow | 专员 | 默认可调用 Cline；Bai 可开用量固定页 |
| Cursor | 外挂 | 仓库内前端/后端（UI、API、测试、PR）；仅用户说「交给cursor」才交 |
| Cline | 外挂 | 数据准备及同类（xlsx、归档、批处理、非仓库数据）；用户说「交给cline」或一般数据/脚本交接 |

- Aitee、Lee 一般不调用 Cursor 或 Cline。任何座位要用 Cursor，必须用户先批准。
- 一个任务只交一个执行方（本条权威处）。Aitor 能在本地做完的短任务，不交 Cursor，不交 Cline。

## 外挂盯梢（Cline / Cursor）

凡交 Cline/Cursor，**仅该次任务期间**盯梢（非常驻）：

1. 必须每 10 分钟看该次进度；结束或无活跃外挂即停。
2. 预估并报告 ETA，按进度调整。
3. 监控进程/日志/产物/卡点；里程碑、卡住或完成才汇报。
4. 结束必须拿到执行方反馈（摘要、路径、验收、遗留）并回报 Aitor。
5. 用量：仅该次外挂实际运行 ≥30 分钟才查，且只查执行方。Bai 可开固定页（Cline `https://app.cline.bot/dashboard/usage`；Cursor `https://cursor.com/dashboard/spending`）。Grok 用量页仅用户点名。
