---
name: skills-contract
description: ~/.grok/skills 只读契约与用法。原 Grok Build AGENTS.md 技能条款已并入此处；Grok 仅留指针。
---

# 技能目录契约（原 Grok Global Rules — Skills Contract）

对所有会使用 `C:\Users\loopn\.grok\skills\` 的执行方生效（含 Grok Build、Cursor、Cline、Grok Bot）。

## 1. 技能目录只读（用户所有）— READ-ONLY

`C:\Users\loopn\.grok\skills\` 是用户的私人技能库，**整棵树对所有 agent 只读**。

- 禁止在技能目录内创建、编辑、重命名、移动或删除任何文件或文件夹。
- 明确包含（但不限于）：`SKILL.md`、`registry.yaml`、`sources/`、`mounts/`、`mounts-cap/`、`personal/`、`references/`、`scripts/`、`docs/`、`_medical-research-meta/`、`ARCHITECTURE.md`、`README.md`、`MOUNTED_SKILLS.md`。
- 技能内容由**用户本人**修改与更新。技能演进不是 agent 的工作。
- 如果发现某技能缺失、过时或有问题：**只报告 + 给出建议**，绝不直接改。按技能自带流程走 `skill-harvest` 提案，最终由用户批准并亲手写入。

## 2. 如何使用这些技能（USE, not edit）

- 按需加载：先读对应 `<skill>/SKILL.md`，再只读它引用的文件；不要整树批量加载。
- 遵守技能定义的路由与 QC：`00_orchestrator` → `01_skill-discovery-integration`（每次运行选 fine id）→ `02`–`06` 领域层 → `00` 的 QC 门。
- 技能文本 = 流程事实来源；已执行的产物（如 `*-results.html`） = 数字事实来源。
- 技能产出写回项目/工作区，**不写回技能目录**。
- 挂载包按 `C:\Users\loopn\.grok\skills\01_skill-discovery-integration\SKILL.md` 的 fine id 逐个选。禁止整包批量克隆（bulk-clone packs）。

## 3. 技能发现位置

- 首选：`C:\Users\loopn\.grok\skills\`（用户级技能）
- 兼容：`~/.claude/skills/`

## 4. 冲突处理

- 当挂载来源的建议与实验室规则 / `My rule.md` / `network-security.md` 冲突：在批注/报告里写清楚冲突 + 修改方案，**由用户决定**；不要静默采用外挂。
- 需要修改技能才能解决的，一律停下来问用户。

## 5. 与 MY-SKILLS 仓的关系

- 开 PR、merge、同步进 `.grok\skills`：见 `My rule.md` 第 9 节（`my-skills-repo.md` 为指针）。
- 本文件只管「怎么用 / 不许改技能树」；仓流程以第 9 节为准。
