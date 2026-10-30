# MY-RULES

规范 GitHub 仓为权威源。`{RULES}`=`D:\0Grok\0doc\GitHub\MY-RULES`（绝对路径见 `My rule.md` §1；若本机仍有 `Documents\Cline\Rules` junction，仅服务 Cursor IDE 内 Cline 插件读规则，勿再维护第二份副本；bot 外挂只交 Cursor）。先改本仓再经 PR；勿在多处冲突改文。

核心 `My rule.md`；现行专题：`skills.md`、`workspace-layout.md`、`network-security.md`、`project-ref-layout.md`。

## 三仓分工（2026-10-27 站立）

| 仓 | 放什么 | 不放什么 |
|---|---|---|
| **MY-RULES**（本仓） | 站立运营政策：本机布局、交付落点、新建禁区、网络红线、技能库契约、`ref/` 地图 | 专业技能正文、可运行代码 |
| **MY-SKILLS** | 专业技能：`NN_slug/base/` 能力正文 + `advanced/` 个人层 + `qc/` 门控标准，全部 prose | 分析/清洗代码；患者数据 |
| **stats-analysis** | 可运行代码：`modules/` 算法库 + `model-validation/` CLI，即 02 席位的脚本半 | skill 正文；课题配置；患者数据 |

判据：**经常用的运营规则进 RULES，专业技能进 SKILLS，能跑的脚本进 stats-analysis。**
一句话以上、每次开工都要看的写 RULES；只在特定席位上展开的写法写 SKILLS；要 `python` 跑起来的进 stats-analysis。
三仓互指只用路径别名（`{RULES}` / `{SKILLS}` / `{code_stats}`），不复制正文。

## 迁移对照（2026-10-18）

| 旧文件 | 现在去哪 |
|---|---|
| `manuscript-and-review.md` | `{SKILLS}\05_manuscript\qc\`（正文禁令/版式）+ `{SKILLS}\06_review\advanced\`（批注/修订）+ `{SKILLS}\07_response\advanced\`（回信） |
| `routing.md` | `{SKILLS}\00_orchestrator\references\ownership-contract.md`（座位/派单）+ `handoff-monitor.md`（盯梢） |
| `engineering-decision.md` | `My rule.md` §6（R1–R6 + 大变更门） |

## Local check (E3)

`ash
python -B check_paths.py --check
`

Verifies Rules docs cite live MY-SKILLS seats/files when the sibling clone is present. Cross-repo layout/retired-id checks live in MY-SKILLS 	ests/test_cross_repo_contract.py.
