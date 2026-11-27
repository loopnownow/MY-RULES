---
name: zone-docs
description: L1 专题：_Docs 区，harvest 对象与布局、H1–H4、harvest 授权、_Docs 分桶、目录命名（N2）。
up: My rule.md §5
owns: [Z3, N2]
---

# `_Docs` 区
- 管：`_library`、`mem`、glossary 入口、`_Docs` 分桶、harvest 对象与布局、H1–H4、harvest 授权（§Z3）、ASCII 目录命名（§N2）。
- 不管：批件与期刊池契约（→ `library-taxonomy.md`）；`{DEL}` 三档与新建禁区（→ `zone-del.md`）。

# 1 先判 harvest 再定落点（H1–H4）
| 类 | 判据 | 动作 |
|---|---|---|
| H1 可复用 how-to | 有步骤 / 陷阱 / 判据，值得进技能或规则 | 抽完即搬 `harvested` |
| H2 不需要 harvest | 数据、原始件、PHI、第三方源码、构建产物、浏览器配置、仅用一次的一次性修补脚本、日志截图 | 不进队列，核对后直接 `harvested` |
| H3 活依赖 | 脚本 / 配置 / link 仍引用该路径 | 先解依赖（`zone-del.md` §3）再搬；可先瘦身留台账 |
| H4 课题件 | 属某课题的中间件或旧稿 | 落 `_by-project\<slug>\` |

- **多次使用的一次性脚本：** 功能相近、已被多次使用的一次性脚本视为 harvest 对象，按 H1 抽可复用做法、接口与陷阱，并提案进 MY-CODES；不得因文件名或落点是「一次性」就直接判 H2。仅用一次、不再重复的修补脚本仍属 H2。
- `park` **不是长期仓**，禁止积压；批次进 park 当轮就要分到 H1–H4。
- 已 promote 或判 H2 的轮次不留活层：整轮从 `{DEL}\harvest-park\rounds\<round>\` 移 `harvested\rounds\<round>\`，`{doc_root}\harvest\LEDGER.tsv` 只留一行。内容已进规则 / 技能后，这些轮次目录可由主人删除。

# 2 耐久层 vs 瞬态
- **耐久**：成品稿、批件、索引、可复用数据 → 按 `My rule.md` §3 落点表，不进 `{DEL}`。
- **瞬态**：日志、截图、构建产物、缓存、仅用一次的一次性脚本 → 直接 `harvested`。功能相近且多次使用过的一次性脚本先按 §1 / §3 作 harvest 对象，抽完剩余件再进 `harvested`。
- **指针壳（stub / redirect）属瞬态**：移动后若无活引用（脚本 / 配置 / 技能正文 / 外部 README 按旧路径打开），直接 absent，不留 stub，也不在 `{DEL}` 留副本；`MOVED.md` 只是惯例不是命名契约；确需保留时 ≤3 行，只写「旧路径 → 新位置」，并接受 `QC.md` §5 的 C11 扫描。
- 判据：能否用现有材料 30 分钟内重建；能否用一段文字复述。二者皆可 → 瞬态。

# 3 harvest 对象与布局
- **三类对象**：过程 how-to、判据 / 阈值、模板片段；不含未发表全文、含姓名表、PHI。
- **城城标记：** Word 中作者标记 **Adm** 下的订正和批注是重要 harvest 对象（只抽标记，不抽全文）。助手作者 **A** 不是城城本人，不当作业主标记来抽。
- **多次使用的一次性脚本：** 功能相近、已被多次使用的一次性脚本是重要 harvest 对象（抽可复用做法、接口与陷阱，提案进 MY-CODES，不把整树脚本写入技能）。仅用一次、无复用价值的修补脚本不当对象。
- **三桶**：规则候选、技能候选、不抽（→ `harvested`）。
- fine-id 只作 lane，不预先定技能；抽与 promote 分离，promote 走 `skills.md` §5。
- **快照不保留**：只收正文 + `MANIFEST.tsv` + `evidence\` + `tools\`；实体镜像不进 `{doc_root}`。
- **轮次工作目录**落 `{DEL}\harvest-park\rounds\<YYYYMMDD><letter>-<slug>\`（必含 `HARVEST-*.md` / `INDEX.md` / `MANIFEST.tsv` / `evidence\`；`tools\` 可选）。不在 `{doc_root}\harvest\` 下建 `rounds\` 或 lane 活层，也不把 `harvest\rounds` + `by-fine-id` 写成活 SSOT。一次 harvest 一个 lane；lane = `registry.yaml` 里的现行 fine id，只作分类列与文件名，不建目录。
- 收集标准仍是 `{doc_root}\harvest\HARVEST-STANDARD.md`；轮次台账 `{doc_root}\harvest\LEDGER.tsv`（一行一轮，属耐久层，不进 `{DEL}`）。`by-fine-id` 笔记只落 `{DEL}`（§N1）。内容进规则 / 技能后，轮次目录可由主人删除。

# 4 **§Z3** harvest 授权范围

- 可在 `drafting` / `pre-submit` / `reviewing` / `accepted` / `archived` / `.Del` **任一侧**进行。
- **每次须主人当轮授权**；不因阶段自动触发。
- `archived` 默认只读：从冷库抽也要当轮点名；不解冻整夹除非另批。
- **QC 分工：** 库形/完整性→本地库门（`{doc_root}\test\structure_check.py` + `STRUCTURE.md`；`_DataBase` 根说明 + `DB-QC-STANDARD.md`）；纳入门禁→harvest 技能；00 复核通过后才候纳入。指针 → `skills.md` §3。

### 不进 harvest / 慎进 `_Docs` 公开层

填好知情、含姓名表、未发表全文、PHI：不进 harvest；慎进 `_Docs` 公开层（与 `zone-projects.md`「accepted 收工」同口径）。

# 5 `_Docs` 分桶
须当轮点名「放 _Docs」才写；默认禁 mkdir，`mem` 例外（`My rule.md` §2）。
- `templates\`：空白伦理/SCI骨架/清单/金样/brand
- `_library\ethics\approvals\`：已批批件 PDF+索引
- `_library\references\`：文献全文；课题 `ref/refer` 只 DOI 指针
- `_library\lit-bank` / `journals\`：书目、期刊池、投稿 prior
- `harvest\`：可复用写法/方法句（「进skills」再进 MY-SKILLS）
- `mem\`：people.csv、JCR 可变、证件/签名（不进 skill 正文）

填好知情、含姓名表、未发表全文不进 harvest；慎进 `_Docs` 公开层。

# 6 **§N2** 目录命名
`_Docs` 下目录一律 ASCII 英文（`approvals` / `journals` / `jcr`）；中文目录发现即当轮 rename，并在 `_library\MOVED-FROM.md` 记一行。库分类与 L1/L2 → `library-taxonomy.md`。
