"""一次性检索工具：在某目录的文件里按正则找行（只打印，不改任何文件）。

用法:
    python -B grepfile.py <dir> <regex> [ext1 ext2 ...]

参数:
    dir    要扫描的目录（递归）
    regex  Python 正则（区分大小写）
    ext    限定扩展名（不带点），省略则扫 .py/.js/.html/.css/.ini/.md
"""
import os
import re
import sys

DEFAULT_EXT = ("py", "js", "html", "css", "ini", "md")
SKIP_DIR = {".git", "__pycache__", ".pytest_cache", ".ruff_cache", "node_modules"}


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    root = sys.argv[1]
    pat = re.compile(sys.argv[2])
    exts = tuple(sys.argv[3:]) or DEFAULT_EXT
    hits = 0
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in SKIP_DIR]
        for name in sorted(fn):
            if exts and not name.endswith(tuple("." + e for e in exts)):
                continue
            path = os.path.join(dp, name)
            try:
                with open(path, encoding="utf-8", errors="replace") as fh:
                    for i, line in enumerate(fh, 1):
                        if pat.search(line):
                            print(f"{os.path.relpath(path, root)}:{i}: {line.rstrip()}")
                            hits += 1
            except OSError as exc:
                print(f"!! {path}: {exc}")
    print(f"-- {hits} hit(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
