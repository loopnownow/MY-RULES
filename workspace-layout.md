---
name: workspace-layout
description: 本机布局与子工程短针（无 A/B 类）。落点见 My rule.md §5。
---

# 本机布局与子工程

路径别名见 `My rule.md` §1。**不再使用** A/B 工作区、`{WORK_A}` / `{WORK_B}`。

## 一行布局

| 根 | 角色 |
|---|---|
| `D:\00db`（`{RAW}`） | 已组织的原始库；只读除非点名 |
| `D:\0del`（`{DEL}`） | AI 可操作临时/移出区（`_by-project` / `_by-function`） |
| `D:\0Grok\0doc` | 语料 + 可复用代码（`_library` / `_corpus` / `_code` 等） |
| `D:\0Grok` | 分阶段子工程工作区（如 `drafting` / `pre-submit` / `in-review` / `accepted` 下的课题夹） |

可选：数据课题也可在上述子工程树内自建文件夹；约定写在该子工程内，不进全局 rules/skills。

## 子工程约定

- 写入 `0doc\` 须用户点名「放 0doc」。
- 产出落点权威在 `My rule.md` §5：**最终**→子工程根；**中间**→`ref/` 地图；**无** `0result\`；临时进 `{DEL}`；Downloads 仅当点名。
- 可复用脚本 → `D:\0Grok\0doc\_code`（`{code_root}`，见 skills `lab-paths.yaml`）；长期规则/语料 → `0doc` 相应层。
- 根不留临时/草稿/一次性中间件（例外：当前在改稿）。`0doc\_code\04-analysis\stats-analysis\modules\` 增改移须先同意。
- 数据处理细则 → `{SKILLS}\02_data-processing\personal\workspace.md`。
- **`ref/` 子目录** → 同仓 `project-ref-layout.md`；技能正文 `{SKILLS}\00_orchestrator\references\project-ref-layout.md`。

## 新建文件夹 / 临时（2026-10-19）

- 未经同意，**禁止**在 `{DEL}` 外新建文件夹。
- Grok / Cursor / Cline **只许**在 `D:\0del\`（`_by-project\` / `_by-function\`）下建夹。
- 一次性脚本、commit/PR 说明、非课题补丁只进 `{DEL}`——不进主目录、不进 `.grok\tmp`、不进课题根。
