"""补起始页里未替换的 `__MODULES_DEFAULT__` 占位符（只补这一处，不动版式与 token）。

金版 `MY-CODES/modules/console/project.html` 带
`const DEFAULT_MODULES = __MODULES_DEFAULT__;`。课题页若是直接拷金版而没替换，
内联脚本第一行就 `ReferenceError: __MODULES_DEFAULT__ is not defined`，
整页初始化中断——所有按钮（含「开启服务」）点了没反应，看着像服务起不来。
`smoke_page.js` 会把这个占位符自动换成空串，所以抓不到这个错，必须真浏览器复核。

用法:
    python -B fill_start_placeholders.py <page.html> <modules_dir>            # dry-run
    python -B fill_start_placeholders.py <page.html> <modules_dir> --apply    # 写盘

参数:
    page.html    课题起始页（`<project>/<project>.html`）
    modules_dir  算法库路径，写进 `DEFAULT_MODULES`（如 <GROK_ROOT>\\0doc\\GitHub\\MY-CODES\\modules）

退出码: 0 = 已替换或 dry-run 通过；1 = 占位符不是恰好 1 处（须人工看）；2 = 参数不足。
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

PLACEHOLDER = "__MODULES_DEFAULT__"


def main(argv: list[str]) -> int:
    args = [a for a in argv if not a.startswith("--")]
    apply = "--apply" in argv
    if len(args) < 2:
        print(__doc__)
        return 2
    page = Path(args[0])
    modules_dir = args[1]
    text = page.read_text(encoding="utf-8")
    count = text.count(PLACEHOLDER)
    # 只在占位符恰好一处时动手：0 处=已修过，>1 处=不是起始页，都要人工确认。
    if count != 1:
        print(f"{page.name}: placeholder count = {count}; nothing to do"
              if count == 0 else
              f"{page.name}: placeholder count = {count}; expected 1 — 人工确认")
        return 1
    literal = json.dumps(modules_dir)
    out = text.replace(PLACEHOLDER, literal)
    if PLACEHOLDER in out:
        print(f"{page.name}: placeholder still present after replace")
        return 1
    # `__CONSOLE_TOKEN__` 在 JS 里也作为哨兵字符串出现，只能查 meta 标签。
    # meta 仍是占位符 = 本页未登记项目（另一步：登记项目 / radconsole://register），不影响补 MODULES。
    unregistered = 'name="console-token" content="__CONSOLE_TOKEN__"' in out
    print(f"{page.name}: {PLACEHOLDER} -> {literal}"
          + ("  (note: 本页未登记项目，meta token 仍是占位符)" if unregistered else ""))
    if not apply:
        print("dry-run; add --apply to write")
        return 0
    page.write_text(out, encoding="utf-8", newline="\n")
    print(f"written {page} ({len(out)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
