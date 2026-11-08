"""HTML 标签配平检查（开发辅助，不是交付代码）。

逐个文件扫描开始/结束标签，打印一行：
    <file> OK [] []
    <file> ERRORS [错误...] [未闭合标签...]
按目录配平判断，不校验证式 HTML，也不改文件。

用法:
    python -B check_html.py <file.html> [more.html ...]
    python -B check_html.py --help

退出码: 0 = 全部通过; 1 = 存在配平错误或读取失败; 2 = 用法错误（未给文件）。
"""
import argparse
from html.parser import HTMLParser

VOID = {
    "area",
    "base",
    "br",
    "col",
    "embed",
    "hr",
    "img",
    "input",
    "link",
    "meta",
    "param",
    "source",
    "track",
    "wbr",
}


class P(HTMLParser):
    """收集结束标签不匹配与未闭合的开始标签。"""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.err = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.err.append(f"extra </{tag}> at {self.getpos()}")
            return
        t, pos = self.stack.pop()
        if t != tag:
            self.err.append(f"mismatch </{tag}> at {self.getpos()} closes <{t}> from {pos}")


def check_file(path: str) -> tuple[list[str], list[str]]:
    """返回（错误列表, 未闭合标签名列表）。"""
    p = P()
    with open(path, encoding="utf-8") as fh:
        p.feed(fh.read())
    return p.err, [tag for tag, _ in p.stack]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="HTML 标签配平检查：逐个文件报 OK 或 ERRORS。",
    )
    ap.add_argument("files", nargs="*", help="要检查的 .html 文件（可多个）")
    args = ap.parse_args(argv)
    if not args.files:
        ap.print_help()
        return 2
    bad = False
    for path in args.files:
        try:
            err, left = check_file(path)
        except OSError as exc:
            print(f"{path} ERROR {exc}")
            bad = True
            continue
        print(path, "ERRORS" if (err or left) else "OK", err[:3], left[:5])
        if err or left:
            bad = True
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
