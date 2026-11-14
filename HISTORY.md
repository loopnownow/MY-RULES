# HISTORY — 规则仓沿革（非规则正文）

> **定位：** 只回答「何时、为什么改、取代了什么」。
> **不是判据：** 现行规则只读 `My rule.md` 与专题文件；引用本文件只能写「背景见 HISTORY §x」，不得当作规则依据。
> **分工：** 正文零 t-id、零日期、零旧名叙述；日期 / 票据号 / 旧名故事 / 裁决理由全部收在本文件。旧名映射（机读）在 `aliases.yaml`。
> **维护：** 只追加，不改写既有条目。每条格式：`日期 · 变更 · 依据 · 取代/废止`。
> **覆盖起点：** 2026-10-18（README 首次出现「迁移对照」）。更早的 0doc 时代记录在 `_Docs/STRUCTURE.md` §0.x，不并入本文件。

---

## A 根与盘面

- **2026-10-18 · 三仓分工站立 + 旧文件迁出。** `manuscript-and-review.md` 拆入 `{SKILLS}\05_manuscript\qc\`（禁令/版式）、`06_review\advanced\`（批注/修订）、`07_response\advanced\`（回信）；`routing.md` 拆入 `00_orchestrator\references\ownership-contract.md`（座位/派单）与 `handoff-monitor.md`（盯梢）；`engineering-decision.md` 并入 `My rule.md` §6（R1–R6 + 重大变更门）。依据：README 迁移对照；GitHub `loopnownow/MY-RULES` 首次提交。
- **2026-10-23 · `.grok\skills` 退役。** 技能运行期只认 MY-SKILLS 克隆（`{SKILLS}` = `{skills_runtime}` = `{skills_git}`），禁止再拷第二棵 runtime 树。依据：`skills.md` §1b。
- **2026-10-24 · 两条 STANDING 立规。** ① 禁止在 `{DEL}` 以外新建文件（t1098u）；② `_Docs` 默认禁止 mkdir，唯一例外是当轮明确同意（t1107u/t1108u/t1109u）。两份全文最初在 `0del`，2026-10-31 移入本仓 `standing/`，P2 起并入 `del-and-harvest.md` §7。依据：`del-and-harvest.md` §7；`My rule.md` §2。
- **2026-10-30 · 新建禁区合并。** t1098u/t1107u/t1240 三处同义条款合并为一条「新建文件/文件夹（权威）」，并补「改已有文件同样先问」（t1672u 总闸）。依据：t1442u/t1450u。
- **2026-11-01 · `_Docs` 顶层收缩。** `_bank` 并入 `_library\glossary`；`_code` 整层退役（脚本 → MY-CODES，壳与索引 → `{DEL}`）；`0script\` 退休；代码仓 `GitHub\stats-analysis` 更名 MY-CODES，旧路径只作历史。依据：`workspace-layout.md` 布局表；`check_paths.py` 的 `retired_stats` / `renamed_codes_repo` 检查项。
- **2026-11-08 · 根路径更名（t1791u / t1794u / t1796u）。** `D:\0Grok` → `D:\MyProjects`；`0doc` → `_Docs`；`00db` → `_DataBase`（`00ds` 为曾用/QC 对象，不是可保留的 legacy）；`0del` / `D:\0del` → `.Del`。同步唯一入口 = `D:\MyProjects\syn.bat` → `E:\Aitor` 根（不是 `E:\Aitor\MyProjects`），`/XD .Del`；实测无其它同步脚本或快捷方式。依据：t1791u/t1794u/t1796u。
- **2026-11-08 · 命名收紧。** 课题夹 `CAC_fyh` / `lung_xlm` 式旧序退休，改 `<prefix>_<suffix>`（`lxf_PP`）；中文人名只进 `_Docs\mem\people.csv`，路径与正文不写中文名。依据：`workspace-layout.md`「命名」。
- **2026-11-09 · 家族桶与 `_share`。** `_DataBase\<family>\<prefix_suffix>\` 取代扁平 `<suffix>` 桶与 `<slug>` 夹；`_share` 定为原始数据/原始记录/原始图片 + `ethics\` + `thesis\` 三类池（自 `_share` 起 ≤2 层）；`_thesis` / `_grants\_misc` / `_ethics\_misc` 三夹解散（遗留：`_grants\2025\_ethics-forms\`）。依据：t1821u/t1822u/t1825u/t1829u。
- **2026-11-14 · harvest 源仓迁出。** `_Docs\harvest\sources\` 整棵迁至 `_Docs\harvest-sources-park`（耐久 park，非草稿层）；`_Docs\harvest` 只留正文 + `MANIFEST.tsv` + `evidence\` + `tools\`。依据：`My rule.md` §5.3.2 第 5 条。
- **2026-11-14 · 规则仓分层重构启动（本文件建立）。** 旧问题：L0 里同时装了 L1 领域契约与 L2 做法，正文混排 t-id / 日期 / 旧名（t-id 90 处、史标记 49 行、最长单行 1,366 字符），同一规则在 2–6 个文件各存一份。处理：正文 → 两层 + 路由；史 → 本文件；旧名 → `aliases.yaml`；QC → `QC.md`。依据：本轮 P1（分支 `rules/p1-archive-layer`）。

## B 阶段与冷库

- **四阶段定型：** `drafting` / `pre-submit` / `reviewing` / `accepted`；`archived` 是分流落点，**不是**第五阶段。旧阶段夹 `preparing` → `drafting`、`polishing` → `pre-submit`、`submitting` / `in-review` → `reviewing`、`reseived` / `received` → `accepted`，只作别名阅读，勿重建。别名机读副本在 `{SKILLS}\00_orchestrator\templates\project-state.yaml` 的 `study_folder_stage_aliases`。
- **`DER` 只是家族码**，不是阶段、不是工作区；不建 `DER` 阶段夹。
- **2026-11-08 · `R&P` 退役（t1813 / t1815 / t1817u）。** 活兄弟根 `R&P`（formerly `proposal`）退役，磁盘 stub 已移 `.Del`，勿重建；申请包 → `_DataBase\_grants\<year>\`，评阅他人稿 → `_DataBase\_reviews\{peer,grants,thesis}\<year>\`。两者都不是稿件流水线阶段。
- **2026-11-08 · accepted 收工（t1806u / t1809u / t1817u）。** 先 harvest 再精简 `accepted\`，`R*` / `P*` 整夹进 `_DataBase\<family>\<prefix_suffix>\`，校验后原夹 → `.Del\_by-project\<slug>\`，最后进 `archived\<family>\<prefix_suffix>\` + `ARCHIVED.md`。hard-keep：终稿一份 + `FinalData_<slug>.xlsx`（或 `ref/README` 钉死的 data.xlsx）。

## C `.Del` 与 harvest

- **2026-10-31 · `.Del` 三档。** `park` / `harvest-park` / `harvested`，不得混放；`junk\` 更名 `harvested\`（平铺，不建日期子夹）；`harvested` 是唯一终弃档，**只由城城手动清**，bot 不清、不代清。依据：t1794u（路径）、2026-10-31 裁定。
- **2026-10-31 · 禁止活指针指 `{DEL}`。** `.Del` 会周期性清空；要长期存在的字节放耐久位。历史 0del 路径由 `_Docs\test\path_audit.py` 归 `HISTORIC`，但不得新增活链。
- **2026-10-31 前 · 活依赖清单（t1490u）。** `_code` 多个脚本把输出写死到 `.Del\harvested\<子夹>`（`smoke`、`modules_bak`、`cln_fill_supplement`、`yt_RDL`、`batch_rerun_status.json`、`batch_rerun.log`）；搬走即破坏脚本，新增写死路径须同轮补清单。
- **2026-11-10 · H1–H4 分流（t1951u）。** 先判 harvest 需求再定落点；`park` 不是长期仓（实测一处积压 239 项 / 45.9 GB 即反例）；H2 件不做「等下次 harvest」，三查后直接落 `harvested\`。
- **2026-11-10 · harvest 教训两条。** ① 一轮 harvest 里 6 节有 5 节用了不存在的 lane，全部返工 → lane 只用现行 fine-id；② 414 件实体镜像 0 孤本 → 快照不保留，`_Docs\harvest` 只收正文 + `MANIFEST.tsv` + `evidence\` + `tools\`（t1952u）。
- **2026-11-13 · 第二类活依赖：DSH profile `link:`（t20261113i）。** `D:\DS\.dsh\profiles\<profile>\package.json` 的 `dependencies` 可直接 `link:` 到 `.Del` 下插件源码（实例：`dsh-ds-pricing` → `.Del\_by-function\dsh-plugin-ds-pricing\bundle`）；整理 `.Del` 前须 grep 配置里的 `.Del` 字面。解依赖：源码迁 `D:\DS\.dsh\local-plugins\<plugin>\`、改 link、`pnpm install --offline`；运行中的 DSH 仍持旧句柄，需重启后再搬。
- **落 harvested 三查：** 全库 grep 无活引用；同名异字节不覆盖；写 `harvested\MOVED.tsv`。

## D 项目 `ref/` 布局

- **2026-10-29 · SSOT 声明。** `project-ref-layout.md` 为权威中文版；技能侧英文镜像 `{SKILLS}\00_orchestrator\references\project-ref-layout.md` 只作运行期读本，冲突以本仓为准。同日立 D-1：移动数据底表前必须先问城城（t1309s6268）。
- **布局演化（时间序）：** `results/` → `analysis/`（t1309s6268）→ 取消标准壳 `analysis/` 与 `materials/`，表图抬到 `ref/tables|figures/`（t1316u）→ 锁定件 `hashes.tsv` / `MANIFEST.md` / `pipeline_run.log` 落 `ref/pipeline/`，写作参考可进 `ref/refer/`（t1321u/t1322u）→ 临时/中间默认 `ref/tmp/`，旧版稿同落（t1450u）→ 文献全文实体 SSOT = `_library\references\<L1>\<L2>\`，`ref/refer/` 只留 `DOI_*.md` 指针（t1455u）→ `ref/citation/` 收 `journals.csv` + `_notes.md`（t1458u）→ `false_classification*` 与同类 ASL 临时表改落当次结果夹 `<project>/<endpoint>/`，结果 HTML 同夹为 `Results*.html`，不提升到子工程根（t1660u，2026-11-05，取代 t1321u/t1322u 的「留子工程根」半句）。
- **已退役夹（勿再新建）：** `ref/analysis/`、`ref/materials/`、独立 `ref/exec/`、`ref/code/`、`ref/gates/`、`ref/writing-refs/`、`ref/raw-pre/`、`ref/results/`。旧树去向：`analysis/` 子项 → `ref/` 根；`materials/` 内 lit / `citation` / `参考文献` → `refer/`，其余 → `ref/` 根；空壳 → `.Del`。
- **2026-11-09 · `ref/figures-orig/` 登记**为允许夹（投稿图原始可编辑件 .ai/.psd/.pptx 原始 .tif），与终图 `figures/` 分工。

## E 稿件命名

- **2026-11-05 · 纯 V 阶段映射（已废止）。** 旧口径 `V2`=投后未审、`V3`=第 1 轮回复、`V4`=第 2 轮、`V9`=校样。
- **2026-11-06 · V/R 双前缀（t1694u，现行）。** 取代上述纯 V 映射：`V`=投稿前及投出后未收意见；`R`=收到意见后的修回（`R轮.次`）；`P`=接收后校样（可选）。不发明 `R0`；换刊重写仍用 `V`；小数不补零、按数值排序；Comments/Response 与同轮 R 同号；换阶段夹不改号。
- **t1946u · 小改不升号。** 错字、标点、纯改字、只加/改批注、不改结论或结构 → 就地改现行文件名，不 `+0.1`、不另存新号。未升号不得反推「不是城城手改」。

## F 技能与入口

- **2026-10-25 · `01_skill-integration` 并入 `00_orchestrator`。** 路由链变为 `00 → 02 → 03 → 05 → 06 → 07 → 00 QC`。
- **2026-10-26 · 技能 QC 站立。** 精简、去重、去旧；skip / archived / 退役仅指针均为清理对象；QT 不得 ignore / 假绿（后续 t1432u / t1463u / t1520u / t1559u 逐步收紧）。
- **Cursor 退役。** Cursor IDE 已卸载；不再把任务派给 Cursor IDE，不用「交给 cursor」作路由触发；`Cursor User Rules` 只留一行指向本仓，该入口不再维护。`mounts` / 挂载缓存树同时退役。
- **2026-11-14 · DSH 适配层转 shim。** `$DSH_HOME\AGENTS.md` 原 74 行复述 L0 正文（别名、写盘闸、网络、三仓、技能 junction、本机事实），与 `{RULES}` 形成第三份副本；改为只留挂载点 + 权威顺序 + 硬闸摘要 + 指针。改动不在本仓 git，独立于规则仓 PR。

## G 事故与裁决留痕

- **2026-10-24 · 注释口径裁决。** 注释只写「配置字段含义」与「如何运行」，不写业务「为什么」；接口说明走 docstring / `--help`（t1622u）。
- **2026-11-05 · 起始页占位符事故（lya_CTA）。** 金版两处占位符 `__CONSOLE_TOKEN__` / `__MODULES_DEFAULT__`；漏替后者使内联脚本首行 `ReferenceError`，整页无响应（一次 41 个课题页全中）。同轮：token 只写 `<meta name="console-token">`，JS 哨兵必须保留占位符；`sync_project_page.py` 写盘用 `newline="\n"`（原 Windows 文本模式写 CRLF，与金版 LF 不一致）。
- **2026-11-05 · 核查必须真浏览器。** `node --check` / `smoke_page.js` 抓不到占位符未替（smoke 会把占位符换成空串）。
- **2026-11-14 · 计数口径统一。** 规则正文 = 11 个文件（L0 1 + L1 专题 6 + 支撑 4：README / QC / HISTORY / aliases）。此前「6 个」指 L1 专题，「8 个」是表格行口径（HISTORY 与 aliases 合一行）。

## H 未完成 / 待批

- **`00ds` 磁盘树**与 `_DataBase` 若并存，维持原状，等城城另批搬迁（t1705u 明确「更正活引用 ≠ 搬迁磁盘树」）。
- **`_grants\2025\_ethics-forms\`** 为 `_grants\_misc` 解散后的遗留例外，未定去向。
- **正文清理**：P4（2026-11-14）已完成，五个专题的 t-id / 决策日期 / 旧名括注已清，见 §I。
- **旧阶段夹**若仍在盘上，只作别名阅读，勿重建、勿改写。

## I 2026-11-14 分层重构日志

- **P1 档案层**（PR #140 → `12db2e4`）：新增 `HISTORY.md` 与 `aliases.yaml`（38 条旧名映射），7 个规则正文 0 行改动。
- **P2 L0**（PR #141 → `1d063fc`）：`My rule.md` 210 → 101 行，改为常驻层；拆出 `del-and-harvest.md`（66 行）与 `QC.md`（57 行）；`standing/` 两份并入后删除（副本留 `{DEL}`）；`project-ref-layout.md` 的 1,366 字「此前」段迁入本文件 §D；旧阶段别名表改为 `aliases.yaml` 指针。
- **P3 DSH 适配层**：`$DSH_HOME\AGENTS.md` 74 → 55 行，只留挂载与指针；`$DSH_HOME\skills\state.json` 移除把 MY-RULES 当技能源的 git root（`git-55875fa9`），否则规则 md 会被当技能加载。
- **P4 清史**（PR #142 → `a576b63`）：workspace / project-ref / library / skills / network 五个专题删除 t-id、决策日期与旧名括注；只保留数据阈值日期（批件 ≥ 2023-11-10）与「勿再新建」禁名清单。
- **P5 规则门**（PR #143 → `fd879db`）：新增 `qc_rules.py`（R1–R3 / R5–R7）与 `tests/test_rules_qc.py`（22 用例）；R4 仍由 `check_paths.py`；`My rule.md` §6、`README.md` E3、`QC.md` §1/§2/§7 同步回写。
- **P6 收尾**（分支 `rules/p6-closeout`）：`QC.md` §5 标题去掉「原 My rule §5.2 迁入」史括注；R2 扩到「原 §x / 旧 §x」类段号引用（新增 1 个负向用例，共 23 个）；建 `.github/pull_request_template.md` 把 R8 做成勾选项；跑完首轮季度清史（9 个 live 文件正文史标记 0 处，`aliases.yaml` 38 条无合并项）。技能侧引用同步改指新节：MY-SKILLS #357 → `cae43b1`，英文镜像 `project-ref-layout.md` 降为索引页。
- **P7 节号锚点门 + 停每轮清理**（分支 `rules/p7-section-gate`）：新增 R9——`§N` 必须命中目标文件的编号标题，裸 `§N` 继承同行文件名、否则指本文件，`§A–B` 两端都校验；抓出并修掉 4 处本仓断链（`workspace-layout.md` 的裸 §2/§3/§4）；按用户要求取消「每轮收工扫 `_Docs`」，改为按需（点名 / 季度巡检），`QC.md` §1/§5、`del-and-harvest.md`、`My rule.md` §6 同步。
- **P8 语料 park 瘦身**（2026-11-14，主人授权）：`_Docs\harvest-sources-park` 四个子档移入 `{DEL}\_by-function\harvest-park-retired-20261114\`（`doc-salvage` 48 件 / `library-ftp` 22 件 / `0doc-base-absorbed` 7 件 / `library-figures` 1 件）；`library-methods\lab-ste`（16 件）**并入技能仓** `{SKILLS}\05_manuscript\advanced\lab-ste`（`_library\lab-ste` 只放 `MOVED.md` 指针，S14 只许 stub）；park 只留 `library-methods` 6 件 + 散件 10 件。依据：主人 2026-11-14「db 中有这些内容，可以删」；核对确认 15 份 `.doc` 抽取文本的原件都在 `_DataBase\_lab\doc-word\`，grant 正文亦在 `0doc-corpus.db`。技能侧引用改指 `{doc_grants}` / `{doc_lab_ste}` / 吸收页 digest。
- **P9 stub 政策**（2026-11-14，主人授权）：`MOVED.md` 类指针壳定为瞬态——无活引用即 absent，不留 stub、不在 `{DEL}` 留副本；`del-and-harvest.md` §5、`QC.md` §5 写入口径，`cleanup_scan.py` C11 由「<300B」放宽为「正文 ≤5 行且含路径 / moved to」的 pointer-only 判定；`_library\lab-ste\MOVED.md` 已移入 `{DEL}\_by-function\stub-retired-20261114\`。

