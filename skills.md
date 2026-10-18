---
name: skills
description: 技能库契约、按需加载、演进提案、PR 与合并后部署同步（含 mounts-cap）。
---

# 技能库（契约 · 演进 · 同步）

对所有使用 `{SKILLS}` 的执行方生效（绝对路径仅见 `My rule.md` §1）。

## 1 只读与写边界

**(a) 技能内容修改**：`{SKILLS}` 内技能正文/结构（含 `SKILL.md`、`registry.yaml`、`sources/`、`mounts/`、`personal/`、`references/`、`scripts/`、`docs/`、`ARCHITECTURE.md`、`README.md`、`MOUNTED_SKILLS.md` 等）禁止 agent 直接创建、编辑、重命名、移动或删除。内容变更只经主人亲手改，或经 GitHub MY-SKILLS 的 PR/merge（§5）。发现缺失/过时：只报告 + 建议；按 §3 提案。

**(b) 合并后部署同步（部署例外）**：MY-SKILLS merge 之后，允许把**本次变更文件**从 GitHub 工作副本 `D:\0Grok\0doc\GitHub\MY-SKILLS` **覆盖同步**到 `{SKILLS}`。白名单=该工作副本中本次已 merge 的路径；禁止整树盲盖、禁止借同步改未改技能。验收：目标路径存在 + 抽查文件 hash（或等价校验）与工作副本一致。此例外是部署，不是「改技能内容」。

**(c) INTEGRATION_MAP 例外**：仅当用户明确要求记录有意义演进证据时，可向 `{SKILLS}\_medical-research-meta\INTEGRATION_MAP.md` 追加一行。月度 `history\` 已迁 `{DEL}\00_orchestrator_reorg_20261017\_medical-research-meta_history\`；若需新归档，在该 0del 树追加或按需重建 `history\`，禁止在 live 技能树另建 `evolution-log.md`。除此之外 `_medical-research-meta\` 仍按 (a)。

## 2 按需使用（USE, not edit）

- 先读 `<skill>/SKILL.md`，再只读其引用文件；禁止整树批量加载。
- 路由与 QC：`00` → `01`（每次选 fine id）→ `02`–`06` → `00` QC 门。
- 技能文本=流程事实源；已执行产物（如 `*-results.html`）=数字事实源。产出写回项目，**不写回技能目录**（部署同步除外，见 §1b）。
- 挂载包按 `{SKILLS}\01_skill-integration\SKILL.md` 的 fine id 逐个选；禁止整包批量克隆。兼容：`~/.claude/skills/`。
- 与 `My rule.md` / `network-security.md` 冲突时写明冲突与方案，由用户决定；不静默采用外挂。

## 3 演进提案（propose only）

对 `00`–`06`：**只提案，不自动决定/修改技能正文**（部署同步见 §1b）。Mount 归 `01`；门控归 `00`。不新建 `07_*`。

| → Skill | → Memory |
|---|---|
| 稳定、跨任务、程序性方法 | 项目事实、一次性偏好 |
| 重复用户证据 | 临时约束、未确认观察 |

- **保留**须同时：已重复或锁定；将用于未来项目；属方法/命名/布局/校验/卫生（非 n/AUC/伦理 ID）；别处无 SSOT。
- **跳过**：一次性路径；SSOT 重复；厂商生产脚本；长人类档案（只指针）；口味；单项目数字/ID。外挂包吸收进已有层，不新建顶层。
- 反扩张：不为病种/器官/包/章节/检验/指标建新顶层；一事一权威家。改动尽量小。每条提案须回答：防什么复发、如何知有效。预算：≤1 核心行为变更、≤3 新规则、无重复、无擅自扩边界。
- 证据：默认 **E4**（同类重复用户纠正）才提案；有金标测试可更高。**单次事件不演进。** 优先级：用户改交付物 > 显式纠正 > 点名问题 > 观察 > 自省。（未达 E4 不提案。）
- 结局提案：keep / revise / rollback / merge·simplify / archive / delete（delete 须显式批准）。Rollback：恢复到已记录 git 点；不对回归自动叠第二次演进。

## 4 `{MOUNTS}`

Live capability bodies SSOT = MY-SKILLS in-repo `NN_slug/base/` (remote MY-SKILLS-base retired 2026-10-17). Former `{MOUNTS}/b/` B byte cache is obsolete for live mounts.

SSOT=`{MOUNTS}`（`D:\0Grok\0doc\04-lab-reference\mounts-cap`）。禁止在 MY-SKILLS 或 `{SKILLS}\mounts-cap` 另留缓存。禁止对该树 `robocopy /MIR`、`git clean -xdf`；未经 owner 命令不提交 remote packs。禁止把 pack 字节当清理抹掉；禁止为清孤儿抹 `STATE.yaml`——改为文档说明。

## 5 MY-SKILLS 仓流程

- 本地分支做完并测试 → 开 PR 前给完整变更清单 → 不零散 PR → 不直推 main → 用户明确同意后才 merge。「直接做」不跳过清单与 merge 确认。
- merge 后按 §1b 做部署同步（工作副本 → `{SKILLS}`）；禁止整树盲盖。
- `{WORK_B}\0script` 与 `{WORK_B}\0doc` 不进仓；技能只写路径指针。`stats-analysis\modules\` 改动见 `workspace-layout.md`，须先同意。
- 只读检查可直接做；改/移/改 ID 仍按 `My rule.md` §2 授权。禁止删除。`gh` 未登录先认证。PC 连不上 GitHub 时从可联网环境推送，再用 git bundle 同步。
