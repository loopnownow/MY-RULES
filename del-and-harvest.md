---
name: del-and-harvest
description: L1 专题：{DEL} 三档落点、harvest 前后去向、活依赖与离场判据、新建禁区全文。
up: My rule.md §2（写盘总闸与新建禁区）
owns: [X2, N1]
---
# 0 定位与边界
- 管：`{DEL}` 三档怎么落、harvest 前后怎么走、活依赖怎么解、旧件何时算离场、旧稿落点（§X2）、新建例外（§N1）。
- 不管：编辑授权（→ `My rule.md` §2）、harvest 怎么做（→ `{SKILLS}\00_orchestrator\harvest\SKILL.md`）、扫描脚本实现（→ `{doc_root}\test\cleanup_scan.py`）、归并（→ `db-library`）、何时清（→ `QC.md`）。

# 1 `{DEL}` 三档
| 档 | 判据 | 可弃度 | 处置 |
|---|---|---|---|
| `park` | 未定归属、待分流的旧件 | 可弃 | 定期清，或按 §2 分流 |
| `harvest-park` | 可能抽出 how-to 的批次 | 条件可弃 | 抽完或判 H2 后移 `harvested` |
| `harvested` | 已抽完 / 不需要抽的剩余件 | 可弃 | 达保留期由城城手动清 |

- 三档一律**平铺**，不再新增层级；旧档名映射见 `aliases.yaml`（`kind: del_tier`）。harvest 轮次夹是三档下的分类目录，不是新的可弃度档。
- **harvest 剩余件**：一次 harvest 之后应进 `{DEL}` 的剩余件一律落 `harvested`，含原可进 `_by-project` 或 `harvest-park` 的收尾件；非 harvest 的三档落点不变。
- **禁止活指针引用 `{DEL}`**：不得留 junction / link / 写死路径指向 `{DEL}` 内文件（实例：DSH profile `link:` 项指向 `.Del\_by-function\…\bundle`）。
- **只能主人清空**：`{DEL}`（含就地 `_Del`）只能由主人手动清空；执行方不得清空、批量删除或「压缩后删除」。主人逐项点名删除时，须先备份台账与报告。
- **空目录**：确认目录内文件已全部落位、文件数为 0 后，才可移除该空目录。
- **大数据盘就地隔离**：影像 / 数据盘上的淘汰件落该盘自己的 `_Del\_by-function\<批次>\`，不跨盘复制到系统盘 `{DEL}`；该 `_Del` 同样只能主人清空。不把外机盘符写进本仓。

# 2 先判 harvest 再定落点（H1–H4）
| 类 | 判据 | 动作 |
|---|---|---|
| H1 可复用 how-to | 有步骤 / 陷阱 / 判据，值得进技能或规则 | 抽完即搬 `harvested` |
| H2 不需要 harvest | 数据、原始件、PHI、第三方源码、构建产物、浏览器配置、仅用一次的一次性修补脚本、日志截图 | 不进队列，核对后直接 `harvested` |
| H3 活依赖 | 脚本 / 配置 / link 仍引用该路径 | 先解依赖（§4）再搬；可先瘦身留台账 |
| H4 课题件 | 属某课题的中间件或旧稿 | 落 `_by-project\<slug>\` |

- **多次使用的一次性脚本：** 功能相近、已被多次使用的一次性脚本视为 harvest 对象，按 H1 抽可复用做法、接口与陷阱，并提案进 MY-CODES；不得因文件名或落点是「一次性」就直接判 H2。仅用一次、不再重复的修补脚本仍属 H2。
- `park` **不是长期仓**，禁止积压；批次进 park 当轮就要分到 H1–H4。
- 已 promote 或判 H2 的轮次不留活层：整轮从 `{DEL}\harvest-park\rounds\<round>\` 移 `harvested\rounds\<round>\`，`{doc_root}\harvest\LEDGER.tsv` 只留一行。内容已进规则 / 技能后，这些轮次目录可由主人删除。

# 3 落 `harvested` 前三查
1. **无活引用**：grep 字面路径、`DEL_ROOT`、`DEFAULT_BATCH`、`--del-root`、`link:`，确认无命中。
2. **依赖已改写**：改指向后复测；不能改的复制到稳定位置，原件再清。
3. **台账已记**：sha256、原路径、去向、日期。

# 4 活依赖
- 定义：脚本 / 配置按写死路径读 `{DEL}` 内文件，或 DSH / Cline 的 `link:` 指向 `{DEL}`。
- 处理顺序：改指向 → 复制到稳定位置并改引用 → 瘦身保留（去大件留入口）→ 都不行则**不搬**。
- 记忆点位：`My rule.md` §2 新建禁区、本文件 §1 禁活指针、`QC.md` §5 清理扫描。

# 5 耐久层 vs 瞬态
- **耐久**：成品稿、批件、索引、可复用数据 → 按 `My rule.md` §3 落点表，不进 `{DEL}`。
- **瞬态**：日志、截图、构建产物、缓存、仅用一次的一次性脚本 → 直接 `harvested`。功能相近且多次使用过的一次性脚本先按 §2 / §6 作 harvest 对象，抽完剩余件再进 `harvested`。
- **指针壳（stub / redirect）属瞬态**：移动后若无活引用（脚本 / 配置 / 技能正文 / 外部 README 按旧路径打开），直接 absent，不留 stub，也不在 `{DEL}` 留副本；`MOVED.md` 只是惯例不是命名契约；确需保留时 ≤3 行，只写「旧路径 → 新位置」，并接受 `QC.md` §5 的 C11 扫描。
- 判据：能否用现有材料 30 分钟内重建；能否用一段文字复述。二者皆可 → 瞬态。

# 6 harvest 对象与布局
- **三类对象**：过程 how-to、判据 / 阈值、模板片段；不含未发表全文、含姓名表、PHI。
- **城城标记：** Word 中作者标记 **Adm** 下的订正和批注是重要 harvest 对象（只抽标记，不抽全文）。助手作者 **A** 不是城城本人，不当作业主标记来抽。
- **多次使用的一次性脚本：** 功能相近、已被多次使用的一次性脚本是重要 harvest 对象（抽可复用做法、接口与陷阱，提案进 MY-CODES，不把整树脚本写入技能）。仅用一次、无复用价值的修补脚本不当对象。
- **三桶**：规则候选、技能候选、不抽（→ `harvested`）。
- fine-id 只作 lane，不预先定技能；抽与 promote 分离，promote 走 `skills.md` §5。
- **快照不保留**：只收正文 + `MANIFEST.tsv` + `evidence\` + `tools\`；实体镜像不进 `{doc_root}`。
- **轮次工作目录**落 `{DEL}\harvest-park\rounds\<YYYYMMDD><letter>-<slug>\`（必含 `HARVEST-*.md` / `INDEX.md` / `MANIFEST.tsv` / `evidence\`；`tools\` 可选）。不在 `{doc_root}\harvest\` 下建 `rounds\` 或 lane 活层，也不把 `harvest\rounds` + `by-fine-id` 写成活 SSOT。一次 harvest 一个 lane；lane = `registry.yaml` 里的现行 fine id，只作分类列与文件名，不建目录。
- 收集标准仍是 `{doc_root}\harvest\HARVEST-STANDARD.md`；轮次台账 `{doc_root}\harvest\LEDGER.tsv`（一行一轮，属耐久层，不进 `{DEL}`）。`by-fine-id` 笔记只落 `{DEL}`（§7）。内容进规则 / 技能后，轮次目录可由主人删除。

# 7 附录：新建禁区（原 standing 正文并入）
**§N1** **新建**（本条为定义；所有写盘另须 §W1）：
1. 全部新建默认只许 `{DEL}` 的 `_by-project\` / `_by-function\`。
2. 显式例外四类：bot 记忆导出（`_Docs\mem\`）、子工程 `ref\tmp\`、`My rule.md` §3 落点表所列的当轮点名交付落点（含子工程根与 `ref\` 各子夹）、用户当轮明确同意的其他路径。
   例外只开放新建路径，不构成编辑许可。不得把未点名的文件写到子工程根。
   一次性脚本 / 小补丁只落 `{DEL}`，不进主目录、`.grok\tmp`、课题根。
3. **改已有文件同问**：`{RULES}` / `{SKILLS}` / `_Docs\harvest\*` / `_Docs\mem\*` / 子工程已有稿（含 Track Changes）都不是自由编辑区。
4. `{doc_root}` 默认禁 mkdir；唯一例外是用户当轮明确同意。目录名 ASCII 英文。
5. ACCEPT 备注、digest、by-fine-id lane、笔记只落 `{DEL}`；子工程内旧版稿与中间件落点 → §X2。
6. 优先 patch 已有文件；不新建 `ACCEPT.md`；不在课题根 / 主目录新建未点名的文件。
7. 用户点名的终稿落点仍按 `My rule.md` §3（优先改已有终稿）；该落点属于第 2 条第三类例外。

# 8 与 QC 的分工
- **何时清**：用户点名或季度巡检时扫 `_Docs`（`QC.md` §5）；扫描实现 `cleanup_scan.py` → `cleanup_move.py`。
- **永不自动清名单**（`_library`、期刊池、批件、`mem`、harvest 台账）在 `QC.md` 维护。
- 本文件只定**落点与离场条件**，不定清理频率。

# **§X2** 旧稿与中间件落点
- 子工程内的旧版稿与中间件 → `ref\tmp\`，保相对路径，不进 `{DEL}`。
- 离开子工程的清理件和无子工程的一次性件 → `{DEL}` 的 `_by-project` / `_by-function`，保相对路径。
- 任何情形都不静默永久删除（§X1）。过后把子工程内旧件清出 `ref\tmp\`、移入 `{DEL}`，须当轮先问。
