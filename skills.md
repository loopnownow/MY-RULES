---
name: skills
description: 技能库契约、按需加载、演进门、PR 与合并后部署同步。
---

# 技能库（契约 · 演进 · 同步）

对所有使用 `{SKILLS}` 的执行方生效（绝对路径仅见 `My rule.md` §1）。

## 1 只读与写边界

**(a)** 禁止 agent 直接改 `{SKILLS}` 技能树任何文件。内容变更只经主人或 GitHub MY-SKILLS PR/merge（§5）。发现缺失/过时：只报告 + 按 §3 提案。

**(b) 合并后部署同步**：`{SKILLS}` = GitHub 克隆 `D:\0Grok\0doc\GitHub\MY-SKILLS`（与 `{skills_runtime}`/`{skills_git}` 同一棵树；旧 `.grok\skills` 已于 2026-10-23 退役）。merge 后对该克隆 `git pull`；禁止再拷到第二棵 runtime 树；禁止整树盲盖。细则→`{SKILLS}\00_orchestrator\references\lifecycle-cache.md`。

## 2 按需使用

先读 `<skill>/SKILL.md` 再只读其引用；路由 `00`→`02`–`07`→`00` QC（`01_skill-integration` 已于 2026-10-25 并入 `00_orchestrator`；粗 ID = 执行座位）。细则→`00` `SKILL.md`。**索引边界（2026-10-26）**：技能正文一律用 `{SKILLS}\…` 绝对路径直读；`D:\0Grok\0doc\.cursorignore` 排除 `GitHub\`，故不得依赖 Cursor/Cline 索引去「找」技能。

## 3 演进提案（propose only）

- **只提案，不直接改** live 技能正文（部署同步见 §1b）。
- 默认证据 **E4**（同类重复用户纠正）；单次事件不演进。
- **delete** 须显式批准。正文→`{SKILLS}\00_orchestrator\references\skill-evolution.md`。
- **Harvest 任务流程**由 skill-00 管理（`{SKILLS}\00_orchestrator\references\skill-evolution.md`「Harvest 任务流程」）；收集标准 SSOT→`{doc_root}\skill-harvest\HARVEST-STANDARD.md`。改 live 技能须城城点名「进skills」（extract ≠ promote）；propose-only 仍适用；不另开 evolution 技能树。

## 4 单一技能源（勿重建第二条树）

Live bodies SSOT = MY-SKILLS in-repo `NN_slug/base/`。不得在别处再建第二棵技能树、挂载缓存树或整树副本；
禁止对任何旧缓存路径 `robocopy /MIR` 或重建包字节。缓存边界→`{SKILLS}\00_orchestrator\references\lifecycle-cache.md`。

## 5 MY-SKILLS 仓流程

本地分支+测试 → PR 前完整变更清单 → 不直推 main → 用户同意后 merge。「直接做」不跳过清单与 merge 确认。merge 后按 §1b 同步。

## 6 QC 与 archived（2026-10-26 站立）

**凡标 archived / 已归档 / page not on disk 的技能树或指针，在 QC 时一律删除**（删引用；若仍有字节则移入 `{DEL}` 并保留相对路径），**禁止**只改标成 archived 继续留在 live 正文或 SOP 调度表。

- 退休 fine-id **只**保留在 `{SKILLS}\00_orchestrator\legacy_aliases.yaml` → 现行 id；live 路由 / workflow / advanced 只写现行 fine-id 与现存路径。
- 发现「archived … (page not on disk)」残留 = QC **P0/P1**：当场删除或改写为现行能力，不得再扩散 archived 标签。
- 互指：`{SKILLS}` `INTEGRATION_MAP.md` / `00_orchestrator/references/skill-evolution.md`（outcome 不再以 archive 为可停留态）。


