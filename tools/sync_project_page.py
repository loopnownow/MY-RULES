"""把金版 project.html 同步成课题页：注入 token 与 modules 默认路径。

用法:
    python -B sync_project_page.py <gold.html> <dest.html> <token> <modules_dir>
"""
import json
import sys


def main() -> int:
    if len(sys.argv) < 5:
        print(__doc__)
        return 2
    gold, dest, token, modules_dir = sys.argv[1:5]
    src = open(gold, encoding="utf-8").read()
    out = src.replace("__CONSOLE_TOKEN__", token).replace(
        "__MODULES_DEFAULT__", json.dumps(modules_dir)
    )
    left = [p for p in ("__CONSOLE_TOKEN__", "__MODULES_DEFAULT__", "__PROJECT__") if p in out]
    if left:
        print("占位符未替换干净:", left)
        return 1
    with open(dest, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(out)
    print(f"written {dest} ({len(out)} chars, token={token[:6]}…, modules={modules_dir})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
