---
name: skills
description: 技能库契约、按需加载、演进门、PR 与合并后部署同步。
---

# 技能库（契约 · 演进 · 同步）

对所有使用 `{SKILLS}` 的执行方生效（绝对路径仅见 `My rule.md` §1）。

## 1 只读与写边界

**(a)** 禁止 agent 直接改 `{SKILLS}` 技能树任何文件。内容变更只经主人或 GitHub MY-SKILLS PR/merge（§5）。发现缺失/过时：只报告 + 按 §3 提案。

**(b) 合并后部署同步**：`{SKILLS}` = GitHub 克隆 `D:\0Grok\0doc\GitHub\MY-SKILLS`（与 `{skills_runtime}`/`{skills_git}` 同一棵树；旧 `.grok\skills` 已于 2026-10-23 退役）。merge 后对该克隆 `git pull`；禁止再拷到第二棵 runtime 树；禁止整树盲盖。细则→`{SKILLS}\01_skill-integration\references\lifecycle-cache.md`。

## 2 按需使用

先读 `<skill>/SKILL.md` 再只读其引用；路由 `00`→`01`→`02`–`07`→`00` QC。细则→`00`/`01` `SKILL.md`。

## 3 演进提案（propose only）

- **只提案，不直接改** live 技能正文（部署同步见 §1b）。
- 默认证据 **E4**（同类重复用户纠正）；单次事件不演进。
- **delete** 须显式批准。正文→`{SKILLS}\00_orchestrator\references\skill-evolution.md`。
- **Harvest 任务流程**由 skill-00 管理（同文件「Harvest 任务流程」）；收集标准 SSOT→`{doc_root}\skill-harvest\HARVEST-STANDARD.md`。propose-only 仍适用；不另开 evolution 技能树。

## 4 mounts（已退役）

`{MOUNTS}` / mounts-cap **已退役**（2026-10-20）：不再维护挂载缓存树；禁止对该路径 `robocopy /MIR` 或重建包字节。Live bodies SSOT = MY-SKILLS in-repo `NN_slug/base/`。缓存边界→`lifecycle-cache.md`。

## 5 MY-SKILLS 仓流程

本地分支+测试 → PR 前完整变更清单 → 不直推 main → 用户同意后 merge。「直接做」不跳过清单与 merge 确认。merge 后按 §1b 同步。
