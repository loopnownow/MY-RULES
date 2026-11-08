"""静态作用域自查：找出「用了某别名但该作用域没绑定」的 NameError 隐患。

口径：模块级只认顶层 import / 顶层赋值；函数级只认本函数（不含内层函数）里的
import / 参数 / 赋值。内层函数的 import 不会让外层函数"看得见"。

用法:
    python -B scope_check.py <dir> [alias1 alias2 ...]
例:
    python -B scope_check.py D:/MyProjects/_Docs/GitHub/MY-CODES/modules pd np plt os sys json re

退出码: 0 = 无隐患; 1 = 有隐患（或语法/读取错误）; 2 = 用法错误。
"""
import argparse
import ast
import os

DEFAULT_ALIASES = ("pd", "np", "plt", "os", "sys", "json", "re")
SKIP_DIR = {".git", "__pycache__", ".pytest_cache", ".ruff_cache"}


class _Scan(ast.NodeVisitor):
    """收集「本层作用域绑定的名字」与「本层用到的 别名.属性」。"""

    def __init__(self) -> None:
        self.bound: set[str] = set()
        self.used: list[tuple[str, int]] = []

    def visit_Import(self, node: ast.Import) -> None:
        for a in node.names:
            self.bound.add(a.asname or a.name.split(".")[0])

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        for a in node.names:
            self.bound.add(a.asname or a.name)

    def visit_arg(self, node: ast.arg) -> None:
        self.bound.add(node.arg)

    def visit_Name(self, node: ast.Name) -> None:
        if isinstance(node.ctx, ast.Store):
            self.bound.add(node.id)

    def visit_Attribute(self, node: ast.Attribute) -> None:
        if isinstance(node.value, ast.Name):
            self.used.append((node.value.id, node.lineno))
        self.generic_visit(node)

    def _nested(self, node) -> None:
        name = getattr(node, "name", "")
        if name:
            self.bound.add(name)  # 名字本身绑在父作用域
        # 不进内层函数体：内层 import 对外层不可见

    def visit_Lambda(self, node) -> None:
        pass

    visit_FunctionDef = _nested
    visit_AsyncFunctionDef = _nested
    visit_ClassDef = _nested


class _DefFinder(ast.NodeVisitor):
    """找本层里的函数定义（不进内层函数体，便于逐层下钻）。"""

    def __init__(self) -> None:
        self.found: list = []

    def visit_FunctionDef(self, node) -> None:
        self.found.append(node)

    def visit_AsyncFunctionDef(self, node) -> None:
        self.found.append(node)

    def visit_Lambda(self, node) -> None:
        pass


def _scan_level(nodes, inherited: set) -> tuple[set, list, list]:
    """扫一层：返回（本层绑定, 本层用到的别名, 本层直接嵌套的函数）。"""
    scan = _Scan()
    for node in nodes:
        scan.visit(node)
    finder = _DefFinder()
    for node in nodes:
        finder.visit(node)
    return scan.bound, scan.used, finder.found


def _check(nodes, inherited: set, aliases: set, label: str, out: list) -> None:
    bound, used, defs = _scan_level(nodes, inherited)
    visible = inherited | bound
    for alias, lineno in used:
        if alias in aliases and alias not in visible:
            out.append(f"{label}:{lineno}: {alias}. 作用域未绑定")
    for fn in defs:
        _check(fn.body, visible, aliases, f"{label}::{fn.name}", out)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="静态作用域自查：找出「用了某别名但该作用域没绑定」的 NameError 隐患。",
        epilog="例: python -B scope_check.py D:/MyProjects/_Docs/GitHub/MY-CODES/modules pd np plt",
    )
    ap.add_argument("dir", nargs="?", help="要递归扫描的目录（必填）")
    ap.add_argument(
        "aliases",
        nargs="*",
        help="别名列表；省略则用默认 pd np plt os sys json re",
    )
    args = ap.parse_args(argv)
    if not args.dir:
        ap.print_help()
        return 2
    root = args.dir
    if not os.path.isdir(root):
        print(f"!! not a directory: {root}")
        return 2
    aliases = set(args.aliases or DEFAULT_ALIASES)
    total = 0
    had_error = False
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in SKIP_DIR]
        for name in sorted(fn):
            if not name.endswith(".py"):
                continue
            path = os.path.join(dp, name)
            try:
                with open(path, encoding="utf-8", errors="replace") as fh:
                    src = fh.read()
            except OSError as exc:
                print(f"!! read {path}: {exc}")
                had_error = True
                continue
            try:
                tree = ast.parse(src, filename=path)
            except SyntaxError as exc:
                print(f"!! syntax {path}: {exc}")
                had_error = True
                continue
            out: list[str] = []
            rel = os.path.relpath(path, root)
            _check(tree.body, set(), aliases, rel, out)
            for line in out:
                print(line)
            total += len(out)
    print(f"-- {total} 处隐患")
    return 1 if (total or had_error) else 0


if __name__ == "__main__":
    raise SystemExit(main())
