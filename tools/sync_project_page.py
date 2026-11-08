"""把金版 project.html 同步成课题页：注入 modules 默认路径 + build 戳，token 只写 meta。

用法:
    python -B sync_project_page.py <gold.html> <dest.html> <token|""> <modules_dir>
        [--ini <ref/settings.ini>] [--stats-root <MY-CODES 根>] [--apply]

默认 dry-run：只打印将写什么；加 `--apply` 才落盘（批量改写前先试跑）。
token 传空串 = 保持未登记（meta 留 `__CONSOLE_TOKEN__` 占位符，等 register 注入）。
JS 里那两处 `__CONSOLE_TOKEN__` 是「本页未注入」的哨兵，两个占位符都**不能**改成
具体 token，否则后续 rotate 改不到它，页面会拿旧 token 当有效值。

页面头顶插一行 build 戳（幂等替换）：
    <!-- console-build: gold=<金版 sha256 前 12> commit=<MY-CODES 短 SHA> synced=<ISO+08:00> token=injected|placeholder -->
`--ini` 把同一组信息写进该课题 `ref/settings.ini` 的 `[console]` 段
（CONSOLE_GOLD_COMMIT / CONSOLE_GOLD_SHA12 / CONSOLE_PAGE_SHA12 / CONSOLE_SYNCED_AT），
写前备份 `.bak`；`--stats-root` 缺省取 `<modules_dir>` 的父目录。
"""
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

META_TOKEN_RE = r'(<meta\s+name="console-token"\s+content=")[^"]*(")'
BUILD_RE = re.compile(r"<!--\s*console-build:.*?-->")
TZ = timezone(timedelta(hours=8))


def sha12(data: bytes) -> str:
    """内容 sha256 前 12 位，用来判断「是不是同一版」。"""
    return hashlib.sha256(data).hexdigest()[:12]


def now_iso() -> str:
    return datetime.now(TZ).replace(microsecond=0).isoformat()


def gold_commit(stats_root: Path) -> str:
    """取 MY-CODES 的短 commit；工作树有未提交改动时加 `+dirty`。取不到就报错退出，不猜。"""
    proc = subprocess.run(
        ["git", "-C", str(stats_root), "rev-parse", "--short", "HEAD"],
        capture_output=True, text=True, encoding="utf-8", check=False,
    )
    if proc.returncode != 0 or not proc.stdout.strip():
        print(f"取不到 {stats_root} 的 git commit: {proc.stderr.strip()}")
        raise SystemExit(1)
    sha = proc.stdout.strip()
    dirty = subprocess.run(
        ["git", "-C", str(stats_root), "status", "--porcelain"],
        capture_output=True, text=True, encoding="utf-8", check=False,
    )
    if dirty.returncode == 0 and dirty.stdout.strip():
        return sha + "+dirty"
    return sha


def with_build_stamp(html: str, stamp: str) -> str:
    """幂等插戳：已有 build 戳则替换，没有就插在 <!doctype html> 之后。"""
    if BUILD_RE.search(html):
        return BUILD_RE.sub(stamp, html, count=1)
    match = re.search(r"<!doctype html>", html, re.IGNORECASE)
    if not match:
        print("金版缺 <!doctype html>，无法插 build 戳")
        raise SystemExit(1)
    return html[: match.end()] + "\n" + stamp + html[match.end():]


def stamp_ini(ini_path: Path, values: dict[str, str], stats_root: Path, apply: bool) -> list[str]:
    """把版本戳写进 ini 的 [console] 段；返回变更的键。需 stats_root 里能 import modules。"""
    sys.path.insert(0, str(stats_root))
    from modules.config.ini_io import read_ini, write_ini

    cur = read_ini(ini_path)
    changed = sorted(k for k, v in values.items() if cur.get(k) != v)
    if not changed:
        return []
    if apply:
        shutil.copy2(ini_path, ini_path.with_suffix(ini_path.suffix + ".bak"))
        cur.update(values)
        write_ini(ini_path, cur)
    return changed


def main() -> int:
    ap = argparse.ArgumentParser(
        description="金版 project.html → 课题起始页（注入 modules 路径 + build 戳；token 只写 meta）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("gold", help="金版 project.html 路径")
    ap.add_argument("dest", help="目标课题页（如 D:\\MyProjects\\drafting\\zyj_OV\\zyj_OV.html）")
    ap.add_argument("token", help='控制台 token；传空串 "" = 保持未登记')
    ap.add_argument("modules_dir", help="共享算法库 modules 目录（写进页面的默认路径）")
    ap.add_argument("--ini", default="", help="顺带把版本戳写进该课题 ref/settings.ini 的 [console] 段")
    ap.add_argument(
        "--stats-root", default="",
        help="MY-CODES 根（取 git commit、import modules）；缺省取 modules_dir 的父目录",
    )
    ap.add_argument("--apply", action="store_true", help="真正写盘；不加则 dry-run")
    args = ap.parse_args()

    gold = Path(args.gold)
    dest = Path(args.dest)
    stats_root = Path(args.stats_root) if args.stats_root else Path(args.modules_dir).parent
    if not gold.is_file():
        print(f"金版不存在: {gold}")
        return 1
    if not Path(args.modules_dir).is_dir():
        print(f"modules_dir 不存在: {args.modules_dir}")
        return 1

    gold_bytes = gold.read_bytes()
    out = gold_bytes.decode("utf-8").replace("__MODULES_DEFAULT__", json.dumps(args.modules_dir))
    if "__PROJECT__" in out:
        print("占位符未替换干净: ['__PROJECT__']")
        return 1
    if "__MODULES_DEFAULT__" in out:
        print("占位符未替换干净: ['__MODULES_DEFAULT__']")
        return 1
    if args.token:
        if not re.search(r'<meta\s+name="console-token"', out):
            print("金版缺 console-token meta 标签")
            return 1
        out = re.sub(
            META_TOKEN_RE, lambda m: m.group(1) + args.token + m.group(2), out, count=1
        )
        meta_state = f"token={args.token[:6]}…"
    else:
        meta_state = "token=占位符（未登记）"
    sentinels = out.count("__CONSOLE_TOKEN__")
    if sentinels != 2 and args.token:
        print(f"JS 哨兵数量异常: {sentinels}（期望 2）")
        return 1

    values = {
        "CONSOLE_GOLD_COMMIT": gold_commit(stats_root),
        "CONSOLE_GOLD_SHA12": sha12(gold_bytes),
        "CONSOLE_SYNCED_AT": now_iso(),
    }
    stamp = (
        f"<!-- console-build: gold={values['CONSOLE_GOLD_SHA12']} "
        f"commit={values['CONSOLE_GOLD_COMMIT']} "
        f"synced={values['CONSOLE_SYNCED_AT']} "
        f"token={'injected' if args.token else 'placeholder'} -->"
    )
    out = with_build_stamp(out, stamp)
    page_bytes = out.encode("utf-8")
    values["CONSOLE_PAGE_SHA12"] = sha12(page_bytes)

    if args.apply:
        dest.write_bytes(page_bytes)
    print(
        f"{'written' if args.apply else 'dry-run'} {dest} ({len(out)} chars, {meta_state}, "
        f"sentinels={sentinels}, modules={args.modules_dir})"
    )
    print(f"build stamp: {stamp}")

    if args.ini:
        ini_path = Path(args.ini)
        if not ini_path.is_file():
            print(f"--ini 指向的文件不存在: {ini_path}")
            return 1
        changed = stamp_ini(ini_path, values, stats_root, args.apply)
        state = "已是同一版本戳" if not changed else "改 " + ", ".join(changed)
        print(f"{'written' if args.apply else 'dry-run'} {ini_path} [console]: {state}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

