# tools/ —— 开发辅助脚本（不是交付代码）

这些是**排错/质检用的一次性工具**，跑在本机、只读文件或写临时产物，不进任何课题交付物。
原先散在 `D:\0del\_by-function\...`，2026-11-04 固化到这里（城城点名「固化进 rules」）。

约定：
- **不联网**、不改业务代码、不写课题目录；输出只看 stdout。
- 多数是**只读**分析工具；写盘例外：`sync_project_page.py` / `fill_start_placeholders.py`（写目标 html）、`extract_inline.py`（写 `<out.js>`）。
- 需要 Python 3.10+；`smoke_page.js` / `extract_inline.py` 的用法需要 Node（`node --check` / `node`）。

| 脚本 | 用途 | 用法 |
|---|---|---|
| `grepfile.py` | 按正则递归 grep 文件（本机 grep 偶发吞输出时用它） | `python -B grepfile.py <dir> <regex> [ext...]`；⚠️ 正则里别用 `|`（PowerShell 传参会出问题），分开跑 |
| `scope_check.py` | AST 作用域自查：找「用了 `pd.`/`np.` 但该作用域没 import」这类 `NameError` 隐患 | `python -B scope_check.py <dir> [别名…]`（默认 `pd np plt os sys json re`） |
| `extract_inline.py` | 把 html 里的内联 `<script>` 抽成 `.js`，便于 `node --check` | `python -B extract_inline.py <in.html> <out.js>` |
| `check_html.py` | 标签配平检查（返回 `OK [] []` 或缺失/多余列表） | `python -B check_html.py <file.html>` |
| `smoke_page.js` | **假 DOM 跑页面顶层脚本**：抓「删了声明忘了引用」这类让页面初始化中断、按钮全点不动的错误（如 `go is not defined`） | `node smoke_page.js <inline.js>`（先 `extract_inline.py`；`__MODULES_DEFAULT__` 会自动替换成空串） |
| `sync_project_page.py` | 金版 `project.html` → 课题起始页：注入 `__MODULES_DEFAULT__`；token **只写 meta 标签**（传空串 = 保持未登记），两处 JS 哨兵保持 `__CONSOLE_TOKEN__` 占位符；写盘固定 LF；页面顶部插一行 `<!-- console-build: gold=… commit=… synced=… -->` 版本戳，`--ini` 把同组版本写进该课题 `ref/settings.ini` 的 `[console]` 段（写前 `.bak`）。用法末尾可加 `[--ini <ref/settings.ini>] [--stats-root <MY-CODES 根>] [--apply]`，**默认 dry-run** | `python -B sync_project_page.py <gold.html> <dest.html> <token\|""> <modules_dir>` |
| `fill_start_placeholders.py` | **只补**起始页里未替换的 `__MODULES_DEFAULT__`（不动版式与 token）；漏替会让整页脚本首行 `ReferenceError`、按钮全失效 | `python -B fill_start_placeholders.py <page.html> <modules_dir>`（dry-run）→ 加 `--apply` 写盘 |

## 什么时候跑

- 改了 `modules/console/project.html`：`extract_inline.py` → `node --check` → `smoke_page.js` → `check_html.py` → `sync_project_page.py`（同步课题页；**默认 dry-run**，确认后加 `--apply`；要同时写 ini 版本台账加 `--ini <ref/settings.ini>`）。
- 前两步是**语法**，第三步才是**行为**：`node --check` 抓不到 `ReferenceError`，2026-11-04 那次「起始页点不动」就是漏了第三步。
- **起始页点不动 / 标题不是项目名 / 课题栏空**：先查占位符——`python -B grepfile.py <page 所在目录> "__MODULES_DEFAULT__" html`。`fill_start_placeholders.py` dry-run 确认计数 1，再 `--apply`，然后**真浏览器复核**（`firefox --headless --screenshot <png> file:///<page>`，标题应等于项目名）。2026-11-05 那次 41 个课题页「开启服务」全无反应，就是批量拷金版漏替 `__MODULES_DEFAULT__`；`smoke_page.js` 把这个占位符自动换成空串，所以四步全绿也照样是死页。
- 改 Python 判定/删函数后：`scope_check.py` 扫一遍。
