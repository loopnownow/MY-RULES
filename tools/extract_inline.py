"""把 html 里的内联 <script> 抽成 .js，便于 node --check。

用法:
    python -B extract_inline.py <input.html> <output.js>
"""
import re
import sys


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    src = open(sys.argv[1], encoding="utf-8").read()
    blocks = re.findall(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", src, re.S)
    if not blocks:
        print("没有内联 script")
        return 1
    with open(sys.argv[2], "w", encoding="utf-8") as fh:
        fh.write("\n;\n".join(blocks))
    print(f"{len(blocks)} block(s) -> {sys.argv[2]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
