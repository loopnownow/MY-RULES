# MY-RULES

规范 GitHub 仓为权威源。`{RULES}`=`D:\0Grok\0doc\GitHub\MY-RULES`（绝对路径见 `My rule.md` §1；若本机仍有 `Documents\Cline\Rules` junction，仅服务 Cursor IDE 内 Cline 插件读规则，勿再维护第二份副本）。先改本仓再经 PR；勿在多处冲突改文。**派工默认 Loopnow**（编码 / 脚本 / MY-CODES → 粗席位 `02_data-processing`）；外部 Cursor IDE 仅在城城批准或说「交给cursor」时使用（t1595u）。

核心 `My rule.md`；现行专题：`skills.md`、`workspace-layout.md`、`network-security.md`、`project-ref-layout.md`、`library-taxonomy.md`（库分类 L1/L2 + 三库契约，t1458u）。

## 三仓分工（2026-10-27 站立）

| 仓 | 放什么 | 不放什么 |
|---|---|---|
| **MY-RULES**（本仓） | 站立运营政策：本机布局、交付落点、新建禁区、网络红线、技能库契约、`ref/` 地图 | 专业技能正文、可运行代码 |
| **MY-SKILLS** | 专业技能：`NN_slug/base/` 能力正文 + `advanced/` 个人层 + `qc/` 门控标准（正文 prose SSOT）；席位 `**/scripts/` 与 `00_orchestrator/scripts/` 可放轻量 helper | 重分析/清洗/建模代码（→ MY-CODES / `{code_root}`）；患者数据 |
| **MY-CODES** | 可运行代码：`modules/` 算法库 + `model-validation/` CLI + `tools/`，即 02 席位的脚本半（**编码默认席位 = Loopnow（`02_data-processing`）**，t1595u） | skill 正文；课题配置；患者数据 |

判据：**经常用的运营规则进 RULES，专业技能进 SKILLS，能跑的脚本进 MY-CODES。**
一句话以上、每次开工都要看的写 RULES；只在特定席位上展开的写法写 SKILLS；要 `python` 跑起来的进 MY-CODES。
三仓互指只用路径别名（`{RULES}` / `{SKILLS}` / `{code_stats}`），不复制正文。

## 迁移对照（2026-10-18）

| 旧文件 | 现在去哪 |
|---|---|
| `manuscript-and-review.md` | `{SKILLS}\05_manuscript\qc\`（正文禁令/版式）+ `{SKILLS}\06_review\advanced\`（批注/修订）+ `{SKILLS}\07_response\advanced\`（回信） |
| `routing.md` | `{SKILLS}\00_orchestrator\references\ownership-contract.md`（座位/派单）+ `handoff-monitor.md`（盯梢） |
| `engineering-decision.md` | `My rule.md` §6（R1–R6 + 大变更门） |

## 开发辅助脚本（`tools/`，2026-11-04 固化）

排错/质检用的小工具（只读、不联网、不进交付物）：`grepfile.py`（正则 grep）、`scope_check.py`（AST 作用域自查，抓 `NameError` 隐患）、`extract_inline.py`（html 内联 JS 抽出）、`check_html.py`（标签配平）、`smoke_page.js`（假 DOM 跑页面顶层脚本，抓「删了声明忘了引用」导致整页点不动）、`sync_project_page.py`（金版 → 课题起始页注入 token/modules）。

用哪个、什么时候跑 → `tools/README.md`。
**改 `modules/console/project.html` 后固定四步**：`extract_inline.py` → `node --check` → `smoke_page.js` → `check_html.py`，再 `sync_project_page.py` 同步课题页。
（本仓其余仍是政策正文；这些脚本属于「开发辅助」，不是交付代码，也不是可复用算法库——算法/清洗脚本仍进 MY-CODES。）

## Local check (E3)

```bash
python -B check_paths.py --check
```

Verifies Rules docs cite live MY-SKILLS seats/files when MY-SKILLS is present (sibling or `SKILLS_ROOT` / `MY_SKILLS`). Missing skills root fails loud (exit 1) unless `--allow-missing-skills`. Also scans Rules MD for stale live path claims (DEL SSOT / retired stats path). Cross-repo layout/retired-id checks live in MY-SKILLS `tests/test_cross_repo_contract.py`.
