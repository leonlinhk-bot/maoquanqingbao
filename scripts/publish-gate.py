#!/usr/bin/env python3
"""发布分级闸门 —— 放行日常数据增补，拦截结构 / 文案 / 口径改动。

分级依据（2026-10-27 用户拍板）：
  🟢 放行：只加条目、rebuild 派生物（items/core/stats/feed），事后留日志
  🔴 须确认：改结构/阈值/分类/文案/品牌口径，或**删除条目**（删数据）
  —— 对应「对外发消息」硬闸门：站是对外可见的。

用法：
  python3 scripts/publish-gate.py              # exit 0 放行 / 3 需确认 / 1 出错
  python3 scripts/publish-gate.py --explain    # 只打印分级，不判定

批准方式（二者其一）：
  HKII_PUBLISH_APPROVED=1 python3 scripts/publish-gate.py
  echo "$(date +%F)" > data/.publish-approved   # 当日有效
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
APPROVAL_FILE = REPO / "data" / ".publish-approved"

# rebuild / 采集管道派生物：每跑一次都会变，不算「人工改动」
DERIVED_EXACT = {
    "data/items.json",
    "data/core.json",
    "data/stats.json",
    "data/last-check.json",  # 采集检查点（纯遥测，站点不读，每天必然变）
}
# `data/_*` 是仓库既有约定：下划线前缀 = 瞬态产物（_raw / _staging / _feed-*）
# `scripts/insert-*`：采集器每次跑都会写的一次性入库脚本（2026-11 已有 80 个），
# 不是人工改脚本 —— 不排除掉的话，日常采集每天都会被本闸门误拦。
DERIVED_PREFIX = ("feed/", "posters/", "data/_", "scripts/insert-")

# live-items.json 里 rebuild 会自动同步的 meta 字段（其余 meta 改动视为口径变更）
META_VOLATILE = {"windowNote", "itemCount", "generatedAt"}

# live-items.json 整段由 rebuild 自动聚合（非手工口径）：按新条目重算，必然变
VOLATILE_SECTIONS = {"digests"}

# 条目内由 enrich/重建自动派生、每次增补都会重排的字段（只改这些不算口径改动）
ITEM_DERIVED_FIELDS = {"clusterId", "clusterCount", "summaryShort"}

# index.html 每次 rebuild 都会改 app.js / styles.css 的版本号（cache-busting）。
# 只允许「版本号变化」，其余 HTML 改动仍算结构改动。
VERSION_ONLY_FILES = {"index.html"}
VERSION_PAT = re.compile(
    r'(?:app\.js|styles\.css)\?v=[0-9A-Za-z._\-]+'
    r'|HKII_VER\s*=\s*"[0-9A-Za-z._\-]+"'
)



def sh(*args: str) -> str:
    return subprocess.run(args, cwd=REPO, capture_output=True, text=True, check=False).stdout


def changed_paths() -> list[str]:
    """工作区 + 暂存区相对 HEAD 的改动文件。"""
    out = sh("git", "status", "--porcelain")
    paths = []
    for line in out.splitlines():
        if not line.strip():
            continue
        p = line[3:].strip()
        if " -> " in p:  # rename
            p = p.split(" -> ", 1)[1]
        paths.append(p.strip('"'))
    return paths


def head_json(rel: str):
    raw = sh("git", "show", f"HEAD:{rel}")
    if not raw.strip():
        return None
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return None


def version_only_diff(rel: str) -> bool:
    """文件相对 HEAD 的改动是否只涉及 asset 版本号（cache-busting）。"""
    raw = sh("git", "diff", "-U0", "HEAD", "--", rel)
    if not raw.strip():
        return False
    changed = [
        ln for ln in raw.splitlines()
        if ln[:1] in ("+", "-") and not ln.startswith(("+++", "---"))
    ]
    return bool(changed) and all(VERSION_PAT.search(ln) for ln in changed)


def strip_auto_stats(sec):
    """stats 段里由 rebuild 自动重算的部分（generatedAt / intelligence 计数）摘掉再比。"""
    if not isinstance(sec, dict):
        return sec
    out = dict(sec)
    out.pop("generatedAt", None)
    out.pop("intelligence", None)
    return out


def classify() -> tuple[list[str], list[str], dict]:
    """→ (结构改动, 数据改动, 统计)"""
    structural: list[str] = []
    data_touched: list[str] = []
    stats = {"added": 0, "modified": 0, "enriched": 0, "deleted": [], "meta_changed": []}

    for p in changed_paths():
        if p in DERIVED_EXACT or p.startswith(DERIVED_PREFIX):
            continue  # 派生物，忽略
        if p in VERSION_ONLY_FILES and version_only_diff(p):
            continue  # 只有版本号变化 = rebuild cache-busting，不是文案改动
        if p == "data/live-items.json":
            data_touched.append(p)
            continue
        if p.endswith(".md") and p.startswith("docs/"):
            structural.append(p)
            continue
        structural.append(p)

    # live-items.json 逐字段比对
    if "data/live-items.json" in data_touched:
        old = head_json("data/live-items.json") or {}
        try:
            new = json.loads((REPO / "data/live-items.json").read_text(encoding="utf-8"))
        except Exception as e:  # noqa: BLE001
            structural.append(f"data/live-items.json（无法解析：{e}）")
            return structural, data_touched, stats

        old_items = {i["id"]: i for i in old.get("items", []) if "id" in i}
        new_items = {i["id"]: i for i in new.get("items", []) if "id" in i}

        stats["added"] = len(new_items.keys() - old_items.keys())
        stats["deleted"] = sorted(old_items.keys() - new_items.keys())
        for iid in old_items.keys() & new_items.keys():
            o, n = old_items[iid], new_items[iid]
            if o == n:
                continue
            # 只有 enrich 派生字段变化（clusterId 重排等）→ 不算口径改动
            if {f for f in set(o) | set(n) if o.get(f) != n.get(f)} <= ITEM_DERIVED_FIELDS:
                stats["enriched"] += 1
                continue
            stats["modified"] += 1

        # 非 items 段：stats / boards / deepCards / sourcesCatalog 改动 = 口径变更
        for k in set(old) | set(new):
            if k == "items":
                continue
            if k == "meta":
                om, nm = old.get("meta", {}) or {}, new.get("meta", {}) or {}
                for mk in set(om) | set(nm):
                    if mk in META_VOLATILE:
                        continue
                    if om.get(mk) != nm.get(mk):
                        stats["meta_changed"].append(f"meta.{mk}")
                continue
            if k in VOLATILE_SECTIONS:
                continue
            if k == "stats" and strip_auto_stats(old.get(k)) == strip_auto_stats(new.get(k)):
                continue
            if old.get(k) != new.get(k):
                stats["meta_changed"].append(k)

    return structural, data_touched, stats


def approved() -> bool:
    if os.environ.get("HKII_PUBLISH_APPROVED") == "1":
        _audit("env:HKII_PUBLISH_APPROVED=1")
        return True
    if APPROVAL_FILE.is_file():
        try:
            ok = APPROVAL_FILE.read_text().strip() == date.today().isoformat()
            if ok:
                _audit(f"file:{APPROVAL_FILE.name}")
            return ok
        except OSError:
            return False
    return False


def _audit(how: str) -> None:
    """批准无法技术上禁止（agent 也能设 env / 写文件），所以至少留痕。

    agent 自批会在这里留下一条记录；人工审时可据此判断该次发布是否需要复查。
    """
    try:
        log = REPO / "data" / "_gate-approvals.log"
        log.parent.mkdir(parents=True, exist_ok=True)
        with log.open("a", encoding="utf-8") as f:
            f.write(
                f"{datetime.now().isoformat(timespec='seconds')}\t{how}\t"
                f"cwd={Path.cwd()}\n"
            )
    except OSError:
        pass


def main() -> int:
    structural, data_touched, stats = classify()
    need_confirm = bool(structural) or bool(stats["deleted"]) or bool(stats["meta_changed"])

    if "--explain" in sys.argv:
        print(f"结构改动 {len(structural)} 项 / 数据改动 {len(data_touched)} 项")
        return 0

    # 无任何改动 → 放行（publish.sh 后面会走「无改动跳过」）
    if not structural and not data_touched:
        print("[gate] 🟢 无改动")
        return 0

    summary = (
        f"+{stats['added']} 条 · 改 {stats['modified']} 条 · 删 {len(stats['deleted'])} 条"
        f" · enrich 派生 {stats.get('enriched', 0)} 条（不计入口径）"
    )
    print(f"[gate] 数据变动：{summary}")

    if not need_confirm:
        print("[gate] 🟢 放行 —— 仅条目增补 / rebuild 派生物，属日常更新")
        return 0

    # —— 需确认：把「为什么拦」写清楚
    print("[gate] 🔴 需确认后才能发布（对外可见的改动）")
    if structural:
        print("  结构 / 文案 / 脚本改动：")
        for p in sorted(structural)[:20]:
            print(f"    · {p}")
        if len(structural) > 20:
            print(f"    · …另 {len(structural) - 20} 个")
    if stats["deleted"]:
        print(f"  删除条目 {len(stats['deleted'])} 条（删数据）：")
        for iid in stats["deleted"][:10]:
            print(f"    · {iid}")
    if stats["meta_changed"]:
        print(f"  口径段改动：{', '.join(stats['meta_changed'][:10])}")

    if approved():
        print("[gate] ✅ 已获批准，放行")
        return 0

    print()
    print("  批准方式（二选一）：")
    print("    1) 运行一次：HKII_PUBLISH_APPROVED=1 bash scripts/publish.sh")
    print(f"    2) echo \"{date.today().isoformat()}\" > data/.publish-approved   # 当日有效")
    print("  未发布的内容仍留在本地，不会被丢弃。")
    return 3


if __name__ == "__main__":
    sys.exit(main())
