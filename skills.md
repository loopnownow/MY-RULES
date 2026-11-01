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

先读 `<skill>/SKILL.md` 再只读其引用；路由 `00` → `02` → `03` → `05` → `06` → `07` → `00` QC（`01_skill-integration` 已于 2026-10-25 并入 `00_orchestrator`；粗 ID = 执行座位）。细则→`00` `SKILL.md`。**索引边界（2026-10-26）**：技能正文一律用 `{SKILLS}\…` 绝对路径直读；`D:\0Grok\0doc\.cursorignore` 排除 `GitHub\`，故不得依赖 Cursor 索引去「找」技能。

运行时只按 fine id（如 clean-data）选型；path 与 slug 仅用于定位实体；入口文件名固定为 SKILL.md；不得把目录名或展示名当作第二套运行时键。

## 3 演进提案（propose only）

- **只提案，不直接改** live 技能正文（部署同步见 §1b）。
- 默认证据 **E4**（同类重复用户纠正）；单次事件不演进。
- **delete** 须显式批准。正文→`{SKILLS}\00_orchestrator\references\skill-evolution.md`。
- **Harvest 任务流程**由 skill-00 管理（`{SKILLS}\00_orchestrator\references\skill-evolution.md`「Harvest 任务流程」）；收集标准 SSOT→`{doc_root}\skill-harvest\HARVEST-STANDARD.md`。改 live 技能须城城点名「进skills」（extract ≠ promote）；propose-only 仍适用；不另开 evolution 技能树。

## 4 单一技能源（勿重建第二条树）

Live bodies SSOT = MY-SKILLS in-repo `NN_slug/base/`。不得在别处再建第二棵技能树、挂载缓存树或整树副本；
禁止对任何旧缓存路径 `robocopy /MIR` 或重建包字节。缓存边界→`{SKILLS}\00_orchestrator\references\lifecycle-cache.md`。


**写作语料席位（证据，非判据）**：`GLOSSARY_ROOT` = `0doc\_library\glossary`。口径与 glossary README 对齐为 **四层**（`words` / `sentences` / `paragraphs` + `sections` 指针页）+ `index.csv`；`banks\` 只作证据。判据 SSOT 在 `{SKILLS}\05_manuscript\base\vocab\`（+ 具名 advanced，如 `preferred-advanced.md` / `ai_patterns.md` / de-AI lexicons）。Rules 只写短指针；细则与路由见 MY-SKILLS `05_manuscript/SKILL.md`。

## 5 MY-SKILLS 仓流程

本地分支+测试 → PR 前完整变更清单 → 不直推 main → 用户同意后 merge。「直接做」不跳过清单与 merge 确认。merge 后按 §1b 同步。

## 6 QC、精简与 skip/archived / 退役仅指针（2026-10-26；t1432u 2026-10-30；t1463u 2026-10-31；t1520u 2026-11-01；t1559u 2026-11-01）

**QC 精简（站立）**：能合并的合并、能删除的删除、去重、去旧、尽量精简。删除的字节进 `{DEL}`（本机 `D:\0del`，保留相对路径）；不得只改标签继续堆在 live 树。

**0del 三档落点（站立）**：park / harvest-park / harvested 的落点与可弃度 → `My rule.md` §5.3（本条不复写；harvested 只由城城手动清）。

**QC 处置（站立）**：对文件 / 技能树 / 文档做 QC 时，**不得**以 skip / skipped / archive / archived / 已归档（及同名文件夹、标签、路径段）作为「暂不处理」的停放处。合法处置只有：**合并**、**删除**、**就地改写**。QC **禁止**新造 skip 或 archive 停放位；已存在的 skipped / archived 残留一律视为**清理对象**（删 live 引用；若仍有字节则移入 `{DEL}`，保留相对路径），不是可继续堆问题的合法落点。

**QC 不得 ignore / 跳过（t1559u）**：质控发现的问题不得用 ignore、skip、exclude、allowlist「先放行」、假绿、注释掉断言、降级为 warning 不报等方式躲过。必须修到过门，或改写规则/门禁本身（城城点头后）再合；禁止为了绿而扩 ignore。

**凡标 skip / skipped / archived / 已归档 / page not on disk 的技能树、文件或指针，在 QC 时一律删除或并入现行能力**（删引用；若仍有字节则移入 `{DEL}`），**禁止**只改标成 skipped / archived 继续留在 live 正文或 SOP 调度表。

**退役且仅剩指针 = QC 清理对象（t1520u）**：能力已并入现行座位 / fine-id / 路径后，live 树只剩「已退役→见某某」、空 README、SUPERSEDED / retired / page-not-on-disk 等**无实现字节**的壳或单向指针时，与 skip/archived **同档 P0/P1**：删壳、删活引用；必要的一句并入现行文档；若仍有字节则移 `{DEL}`（保相对路径）。**禁止**新造「仅指针」壳当停放。**不算壳（勿误清）**：`legacy_aliases.yaml` 路由表；现行契约指针（如 `DOI_*.md`→`_library/references`、批件指针、`journals.csv`）；`HISTORIC` 审计记录（只标历史、不新建活链到 `{DEL}`）。

- 退休 fine-id **只**保留在 `{SKILLS}\00_orchestrator\legacy_aliases.yaml` → 现行 id；live 路由 / workflow / advanced 只写现行 fine-id 与现存路径。
- 发现 skip / skipped / archived / 已归档 /「archived … (page not on disk)」等残留 = QC **P0/P1**：当场删除、合并或改写为现行能力，不得再扩散 skipped / archived 标签。
- 合并优先于新开：重复能力 / 重复座位 / 重复说明先并入现行 fine-id 或现行座位，再删壳。
- 去旧：过时路由、已退役座位话术（如 enter/Re-enter 01）、已删除 CI / 外部 fine-id 模型等不得作为当前流程再写。
- 互指：`{SKILLS}` `INTEGRATION_MAP.md` / `00_orchestrator/references/skill-evolution.md`（outcome：keep / revise / rollback / merge·simplify / delete；不再以 skip / archive 为可停留态）。


