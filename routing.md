---
name: routing
description: 交接、盯梢与执行方路由全文。SCRIPT_ROLES 追加规则见 My rule.md 第 3 节。
---

# 交接与盯梢

- `SCRIPT_ROLES.md` 只追加一行：见 `My rule.md` 第 3 节。

- **交接（2026-10-13，用户确认）**：用量池已合并。一个任务只交一个执行方。Aitor 能在本地做完的短任务，不交 Cursor，不交 Cline。
- **Cursor**：仓库内前端与后端（UI、API、测试、PR）。仅当用户说「交给cursor」才交。
- **Cline**：数据准备及同类（xlsx 填写、归档、批处理脚本、非仓库数据工作）。用户说「交给cline」，或一般数据/脚本交接，交 Cline。
- **专员外挂工具（2026-10-14）**：各 bot 均可调用 Cline。常规：Victor、Bai、Loopnow 默认用 Cline；Aitee、Lee 一般不调用 Cursor 或 Cline。任何座位要用 Cursor，须用户先批准（含「交给cursor」本条仍适用）。
- **Aitor（Grok Bot，00）**：运维、规则、交付路径、QC 与门控、盯梢交接、研究专员路由。
  稿件 Track Changes 与批注的归属见 `manuscript-and-review.md` §2。
- **Grok Build（已停用，2026-10-13）**：不再新开 Grok Build 任务。Aitor 不启动 `grok`。上文「`AGENTS.md` 只放指针」仍然有效。用户若自行手动运行 `grok`，属可选、仅手动，不是交接路径。原「代理 + `grok` 启动」与「每 10 分钟 Grok 盯梢」作废，不再执行。
- **外挂盯梢（Cline / Cursor，2026-10-14）**：凡把任务交给 Cline 或 Cursor Agent，**仅在该次任务进行期间**，执行该外挂的 bot 与 Aitor 都必须盯梢（**不是**常驻例行 / 全天候 cron）：
  1. **强制每 10 分钟**查看一次**该次**任务进度（勿等用户问）；任务结束或无活跃外挂时停止盯梢并保持安静。
  2. 按工作量预估完成时间，并向用户报 ETA；过程中按实际进度**实时调整** ETA。
  3. 监控运行：进程是否活着、日志/产物是否推进、卡点与阻塞；有里程碑、卡住或完成时才向用户汇报。
  4. 结束时必须拿到执行方反馈（结果摘要、改了哪些路径、是否验收通过、遗留项），并回报 Aitor。
  5. token / 额度：仅当该次外挂任务**实际运行 ≥ 30 分钟**才查用量；且**只查执行该任务的那一家**（Cline 或 Cursor）。不查 Grok Build。不足 30 分钟不查。查时可由 Bai 打开对应固定页（Cline `https://app.cline.bot/dashboard/usage`；Cursor `https://cursor.com/dashboard/spending`），报告已用、剩余与下次重置。不做成例行 routine。Grok 用量页（`https://grok.com/?_s=usage`）仅当用户明确要求时才打开，不作为交接默认。