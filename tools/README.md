# tools/ —— 开发辅助脚本（不是交付代码）

本目录分两支，不进课题交付物。需要 Python 3.10+；`extract_inline.py` 与 `smoke_page.js` 还需要 Node。

- **只读检查器**（`qc/`）：不联网、不写盘。
- **生成器**（`gen/`）：写盘，受 §W1 约束，须当轮点名。默认 dry-run 的脚本须加 `--apply` 才落盘。

下列用法均从仓根执行。

## 只读检查器（`tools/qc/`）

| 脚本 | 用途 | 用法 |
|---|---|---|
| `grepfile.py` | 按正则递归 grep 文件（本机 grep 偶发吞输出时用它） | `python -B tools/qc/grepfile.py <dir> <regex> [ext...]`；正则里不要写交替符（PowerShell 传参会出问题），分开跑 |
| `scope_check.py` | AST 作用域自查：找「用了 `pd.`/`np.` 但该作用域没 import」这类 `NameError` 隐患 | `python -B tools/qc/scope_check.py <dir> [别名…]`（默认 `pd np plt os sys json re`） |
| `check_html.py` | 标签配平检查（返回 `OK [] []` 或缺失/多余列表） | `python -B tools/qc/check_html.py <file.html>` |
| `smoke_page.js` | **假 DOM 跑页面顶层脚本**：抓「删了声明忘了引用」这类让页面初始化中断、按钮全点不动的错误（如 `go is not defined`） | `node tools/qc/smoke_page.js <inline.js>`（先 `tools/gen/extract_inline.py`；`__MODULES_DEFAULT__` 会自动替换成空串） |

`smoke_page.js` 只用 `fs.readFileSync` 读入待测脚本，不写盘；`fetch` 被替换为立即拒绝（`smoke: no network`），不发起网络请求。

## 生成器（`tools/gen/`）

| 脚本 | 用途 | 用法 |
|---|---|---|
| `extract_inline.py` | 把 html 里的内联 `<script>` 抽成 `.js`，便于 `node --check` | `python -B tools/gen/extract_inline.py <in.html> <out.js>`（写 `<out.js>`） |
| `fill_start_placeholders.py` | **只补**起始页里未替换的 `__MODULES_DEFAULT__`（不动版式与 token）；漏替会让整页脚本首行 `ReferenceError`、按钮全失效 | `python -B tools/gen/fill_start_placeholders.py <page.html> <modules_dir>`（dry-run）→ 加 `--apply` 写盘 |
| `sync_project_page.py` | 金版 `project.html` → 课题起始页：注入 `__MODULES_DEFAULT__`；token **只写 meta 标签**（传空串 = 保持未登记），两处 JS 哨兵保持 `__CONSOLE_TOKEN__` 占位符；写盘固定 LF；页面顶部插一行 `<!-- console-build: gold=… commit=… synced=… -->` 版本戳；`--ini` 把同组版本写进该课题 `ref/settings.ini` 的 `[console]` 段（写前 `.bak`）。可加 `[--ini <ref/settings.ini>] [--stats-root <MY-CODES 根>] [--apply]`，**默认 dry-run** | `python -B tools/gen/sync_project_page.py <gold.html> <dest.html> <token\|""> <modules_dir>` |

## 改 `project.html` 固定四步

改了 `modules/console/project.html` 之后，按这次序从仓根跑（前两步是语法，第三步才是行为：`node --check` 抓不到 `ReferenceError`）：

1. `python -B tools/gen/extract_inline.py <gold.html> <out.js>`
2. `node --check <out.js>`
3. `node tools/qc/smoke_page.js <out.js>`
4. `python -B tools/qc/check_html.py <gold.html>`

再同步课题页：`python -B tools/gen/sync_project_page.py <gold.html> <dest.html> <token|""> <modules_dir>`（**默认 dry-run**，确认后加 `--apply`；要同时写 ini 版本台账加 `--ini <ref/settings.ini>`）。

## 起始页占位符与冒烟

`<project>/<project>.html` 由金版 `modules/console/project.html` 派生时：

- `__MODULES_DEFAULT__`（算法库路径）**必须替换**。漏替 → 内联脚本首行 `ReferenceError`、整页按钮全失效（「开启服务」没反应）。
- `__CONSOLE_TOKEN__` 只在 `<meta name="console-token">` 一处写 token，另外 **2 处 JS 哨兵必须留占位符**（写死具体 token 之后 `register --rotate` 只能改 meta，页面会留下上一枚旧 token）。
- 生成用 `python -B tools/gen/sync_project_page.py`（token 传空串 = 保持未登记），或从 `http://127.0.0.1:<port>/start.html` 另存；只补 `__MODULES_DEFAULT__` 用 `python -B tools/gen/fill_start_placeholders.py`（先 dry-run，确认计数为 1 再 `--apply`）。
- `smoke_page.js` 会把占位符换成空串，因此 **`node --check` / `smoke_page.js` 全绿也可能是死页**。改完必须真浏览器复核（`firefox --headless --screenshot`，标题=项目名）。
- 排查起始页点不动 / 标题不是项目名 / 课题栏空：先 `python -B tools/qc/grepfile.py <page 所在目录> "__MODULES_DEFAULT__" html`，再按上款补占位符并做真浏览器复核。

改 Python 判定或删函数后：用 `tools/qc/scope_check.py` 扫一遍。
