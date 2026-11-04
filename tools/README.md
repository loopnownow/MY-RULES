# tools/ —— 开发辅助脚本（不是交付代码）

这些是**排错/质检用的一次性工具**，跑在本机、只读文件或写临时产物，不进任何课题交付物。
原先散在 `D:\0del\_by-function\...`，2026-11-04 固化到这里（城城点名「固化进 rules」）。

约定：
- **不联网**、不改业务代码、不写课题目录；输出只看 stdout。
- 都是**只读**分析工具（`sync_project_page.py` 例外：它写目标 html）。
- 需要 Python 3.10+；`smoke_page.js` / `extract_inline.py` 的用法需要 Node（`node --check` / `node`）。

| 脚本 | 用途 | 用法 |
|---|---|---|
| `grepfile.py` | 按正则递归 grep 文件（本机 grep 偶发吞输出时用它） | `python -B grepfile.py <dir> <regex> [ext...]`；⚠️ 正则里别用 `|`（PowerShell 传参会出问题），分开跑 |
| `scope_check.py` | AST 作用域自查：找「用了 `pd.`/`np.` 但该作用域没 import」这类 `NameError` 隐患 | `python -B scope_check.py <dir> [别名…]`（默认 `pd np plt os sys json re`） |
| `extract_inline.py` | 把 html 里的内联 `<script>` 抽成 `.js`，便于 `node --check` | `python -B extract_inline.py <in.html> <out.js>` |
| `check_html.py` | 标签配平检查（返回 `OK [] []` 或缺失/多余列表） | `python -B check_html.py <file.html>` |
| `smoke_page.js` | **假 DOM 跑页面顶层脚本**：抓「删了声明忘了引用」这类让页面初始化中断、按钮全点不动的错误（如 `go is not defined`） | `node smoke_page.js <inline.js>`（先 `extract_inline.py`；`__MODULES_DEFAULT__` 会自动替换成空串） |
| `sync_project_page.py` | 金版 `project.html` → 课题起始页：注入 `__CONSOLE_TOKEN__` / `__MODULES_DEFAULT__`，并检查占位符 0 残留 | `python -B sync_project_page.py <gold.html> <dest.html> <token> <modules_dir>` |

## 什么时候跑

- 改了 `modules/console/project.html`：`extract_inline.py` → `node --check` → `smoke_page.js` → `check_html.py` → `sync_project_page.py`（同步课题页）。
- 前两步是**语法**，第三步才是**行为**：`node --check` 抓不到 `ReferenceError`，2026-11-04 那次「起始页点不动」就是漏了第三步。
- 改 Python 判定/删函数后：`scope_check.py` 扫一遍。
