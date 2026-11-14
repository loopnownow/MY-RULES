# MY-RULES

运营规则 SSOT，两层结构：**L0 常驻**（`My rule.md`，每次开工必读）+ **L1 专题**（按需读取）。专业技能正文在 `{SKILLS}`（L2），可运行代码在 `{code_root}`。

入口永远是 `My rule.md` §5 路由表：先认触发，再读专题。三仓互指只用别名，不复制正文。

## 文件结构（10 个）

| 文件 | 层 | 做什么 | 边界 |
|---|---|---|---|
| `My rule.md` | L0 | 裁决顺序、硬闸、交付落点、路由第一跳、QC 频率 | 不写领域细节 / 步骤 / 史 |
| `workspace-layout.md` | L1 | 盘面、阶段夹、家族桶、`_share`、`_db`、冷库、accepted 收工 | `{DEL}` → `del-and-harvest.md`；稿名 → `project-ref-layout.md` |
| `project-ref-layout.md` | L1 | 项目 `ref\` 地图、稿名、手改识别、幂等 | 落点总则 → `My rule.md` §3；版式 → 技能 |
| `del-and-harvest.md` | L1 | `{DEL}` 三档、harvest 去向、活依赖、新建禁区全文 | 扫描实现 → `_Docs\test\`；何时清 → `QC.md` |
| `library-taxonomy.md` | L1 | 库分类 L1/L2、三库分工、批件 / 期刊池契约 | 归并脚本 → 技能 `db-library` |
| `network-security.md` | L1 | 网段红线、敏感外发、代理、留痕 | 不写执行步骤 |
| `skills.md` | L1 | 技能仓读边界、按需加载、演进、MY-SKILLS PR | fine-id 路由在技能仓，不在此 |
| `README.md` | 支撑 | 本文件：仓地图与维护入口 | 不承载规则正文 |
| `QC.md` | 支撑 | 规则门 R1–R10、频率、失败处置、豁免 | 技能树 QC → `skills.md` §6 |
| `aliases.yaml` | 档案 | 旧名 → 现行名（机器可读） | 不是规则 |

## 三仓分工

| 仓 | 放什么 | 不放什么 |
|---|---|---|
| **MY-RULES**（本仓） | 运营政策：布局、落点、新建禁区、网络红线、技能库契约、`ref/` 地图 | 专业技能正文、可运行代码 |
| **MY-SKILLS** | 专业技能：`NN_slug/base/` + `advanced/` + `qc/`（正文 SSOT） | 重分析 / 清洗 / 建模代码；患者数据 |
| **MY-CODES** | 可运行代码：`modules/` + `model-validation/` + `tools/` | 技能正文；课题配置；患者数据 |

判据：**经常用的运营规则进 RULES，专业技能进 SKILLS，能跑的脚本进 MY-CODES。**
一句话以上、每次开工都要看的写 RULES；只在特定席位上展开的写法写 SKILLS；要 `python` 跑起来的进 MY-CODES。

## 维护

- 改规则：本地分支 + 测试 → 出示完整变更清单 → 批准开 PR → 不直推 `main` → 用户说「合」「和」「推合」才 merge（`My rule.md` §6）。
- 提交前跑 `python -B check_paths.py --check`；规则门与频率见 `QC.md`。
- `aliases.yaml` 是旧名唯一来源，正文不写旧名；变更理由写进 PR 正文，仓内不留史。
- 技能侧英文镜像只作运行期读本，冲突以本仓中文版为准。

## 开发辅助（`tools/`）

只读、不联网、不进交付物：`grepfile.py`、`scope_check.py`、`extract_inline.py`、`check_html.py`、`smoke_page.js`、`sync_project_page.py`、`fill_start_placeholders.py`。用哪个、何时跑 → `tools/README.md`。

改 `modules/console/project.html` 后固定四步：`extract_inline.py` → `node --check` → `smoke_page.js` → `check_html.py`，再 `sync_project_page.py` 同步课题页。

## Local check (E3)

```bash
python -B check_paths.py --check   # R4：{SKILLS} 席位/文件存在 + 退役路径 live 引用
python -B qc_rules.py              # R1–R3、R5–R7、R9、R10：路由闭合、正文无史、旧名唯一、无副本、头字段、行长、节号、指针壳
python -B -m pytest -q tests       # 门的负向用例（改规则时必跑）
```

`check_paths.py` 缺技能根默认 fail loud（exit 1），除非 `--allow-missing-skills`；`qc_rules.py` 的判据与豁免见 [QC.md](<QC.md>)。
