---
name: del-and-harvest
description: L1 专题：{DEL} 三档落点、harvest 前后去向、活依赖与离场判据、新建禁区全文。
up: My rule.md §2（写盘总闸与新建禁区）
---
# 0 定位与边界
- 管：`{DEL}` 三档怎么落、harvest 前后怎么走、活依赖怎么解、旧件何时算离场。
- 不管：新建 / 编辑授权（→ `My rule.md` §2）、harvest 怎么做（→ `{SKILLS}\00_orchestrator\harvest\SKILL.md`）、扫描脚本实现（→ `{doc_root}\test\cleanup_scan.py`）、归并（→ `db-library`）、何时清（→ `QC.md`）。

# 1 `{DEL}` 三档
| 档 | 判据 | 可弃度 | 处置 |
|---|---|---|---|
| `park` | 未定归属、待分流的旧件 | 可弃 | 定期清，或按 §2 分流 |
| `harvest-park` | 可能抽出 how-to 的批次 | 条件可弃 | 抽完或判 H2 后移 `harvested` |
| `harvested` | 已抽完 / 不需要抽的剩余件 | 可弃 | 达保留期由城城手动清 |

- 三档一律**平铺**，不再新增层级；旧档名映射见 `aliases.yaml`（`kind: del_tier`）。
- **harvest 剩余件**：一次 harvest 之后应进 `{DEL}` 的剩余件一律落 `harvested`，含原可进 `_by-project` 或 `harvest-park` 的收尾件；非 harvest 的三档落点不变。
- **禁止活指针引用 `{DEL}`**：不得留 junction / link / 写死路径指向 `{DEL}` 内文件（实例：DSH profile `link:` 项指向 `.Del\_by-function\…\bundle`）。

# 2 先判 harvest 再定落点（H1–H4）
| 类 | 判据 | 动作 |
|---|---|---|
| H1 可复用 how-to | 有步骤 / 陷阱 / 判据，值得进技能或规则 | 抽完即搬 `harvested` |
| H2 不需要 harvest | 数据、原始件、PHI、第三方源码、构建产物、浏览器配置、一次性修补脚本、日志截图 | 不进队列，核对后直接 `harvested` |
| H3 活依赖 | 脚本 / 配置 / link 仍引用该路径 | 先解依赖（§4）再搬；可先瘦身留台账 |
| H4 课题件 | 属某课题的中间件或旧稿 | 落 `_by-project\<slug>\` |

- `park` **不是长期仓**，禁止积压；批次进 park 当轮就要分到 H1–H4。
- 已 promote 或判 H2 的轮次不留活层：整轮移 `harvested\rounds\<round>\`，台账只留一行。

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
- **瞬态**：日志、截图、构建产物、缓存、一次性脚本 → 直接 `harvested`。
- **指针壳（stub / redirect）属瞬态**：移动后若无活引用（脚本 / 配置 / 技能正文 / 外部 README 按旧路径打开），直接 absent，不留 stub，也不在 `{DEL}` 留副本；`MOVED.md` 只是惯例不是命名契约；确需保留时 ≤3 行，只写「旧路径 → 新位置」，并接受 `QC.md` §5 的 C11 扫描。
- 判据：能否用现有材料 30 分钟内重建；能否用一段文字复述。二者皆可 → 瞬态。

# 6 harvest 对象与布局
- **三类对象**：过程 how-to、判据 / 阈值、模板片段；不含未发表全文、含姓名表、PHI。
- **三桶**：规则候选、技能候选、不抽（→ `harvested`）。
- fine-id 只作 lane，不预先定技能；抽与 promote 分离，promote 走 `skills.md` §5。
- **快照不保留**：只收正文 + `MANIFEST.tsv` + `evidence\` + `tools\`；实体镜像不进 `{doc_root}`。
- 布局固定：`{doc_root}\harvest\<lane>\`；一次 harvest 一个 lane，不跨 lane 合并。

# 7 附录：新建禁区（原 standing 正文并入）
1. 全部新建只许 `{DEL}` 的 `_by-project\` / `_by-function\`。
2. 例外仅限：bot 记忆导出（`_Docs\mem\`）、子工程 `ref\tmp\`、用户当轮明确同意。
3. **改已有文件同问**：`{RULES}` / `{SKILLS}` / `_Docs\harvest\*` / `_Docs\mem\*` / 子工程已有稿（含 Track Changes）都不是自由编辑区。
4. `{doc_root}` 默认禁 mkdir；唯一例外是用户当轮明确同意。目录名 ASCII 英文。
5. ACCEPT 备注、digest、by-fine-id lane、笔记、中间件只落 `{DEL}`。
6. 优先 patch 已有文件；不新建 `ACCEPT.md`，不在课题根 / 主目录新建 `文件`。
7. 用户点名的终稿落点仍按 `My rule.md` §3（优先改已有终稿）。

# 8 与 QC 的分工
- **何时清**：用户点名或季度巡检时扫 `_Docs`（`QC.md` §5）；扫描实现 `cleanup_scan.py` → `cleanup_move.py`。
- **永不自动清名单**（`_library`、期刊池、批件、`mem`、harvest 台账）在 `QC.md` 维护。
- 本文件只定**落点与离场条件**，不定清理频率。
