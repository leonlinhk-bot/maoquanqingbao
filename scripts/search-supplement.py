#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
search-supplement.py —— DeepSeek Search 旁路补漏（不写库）

用途：每天 RSS 采集之后跑一轮，把「RSS 没覆盖到、但权威度够」的候选攒到
      data/_staging/search-candidates.json，供人工/Agent 复核后再决定入不入库。

铁律：
  1. 绝不写 data/live-items.json —— 只产候选
  2. 输出目录 data/_staging/ 已 gitignore，不会被 publish.sh 推上线
  3. 只保留白名单域名 + authority>=3 + 45 天内

为什么查询措辞很关键（2026-10-18 实测）：
  「香港保监局 通函」   → 中位 390 天（返回归档旧文）
  「香港保险业 最新 消息」→ 中位 3 天（返回当天新闻）
  所以本脚本统一用「最新 / 消息 / news」类口语措辞，**不写年份**。

用法：
  python3 scripts/search-supplement.py            # 正常跑
  python3 scripts/search-supplement.py --dry-run  # 只打印，不落盘
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "data"
STAGING = DATA / "_staging"
OUT_JSON = STAGING / "search-candidates.json"
OUT_MD = STAGING / "search-candidates.md"
LAST_CHECK = DATA / "last-check.json"
LIVE = DATA / "live-items.json"
ENV_FILE = Path.home() / ".hermes" / ".env"

# ── 查询：分板块，口语化时效措辞，不带年份 ────────────────────────────
QUERIES = [
    ("reg",        "香港保监局 最新 公告"),
    ("reg",        "香港保监局 最新 执法 消息"),
    ("market",     "香港保险业 最新 消息"),
    ("product",    "香港保险 分红 最新 消息"),
    ("family",     "香港 家族办公室 最新 消息"),
    ("nfra",       "金融监管总局 保险 最新 消息"),
    ("competitor", "香港 保险经纪 最新 消息"),
]

# ── 白名单 ───────────────────────────────────────────────────────────
OFFICIAL = {
    "ia.org.hk", "hkma.gov.hk", "info.gov.hk", "nfra.gov.cn",
    "fstb.gov.hk", "hkfi.org.hk", "fsc.gov.tw", "gov.hk",
    "investhk.gov.hk", "cef.gov.hk",
}
INSURER = {
    "aia.com.hk", "prudential.com.hk", "manulife.com.hk", "axa.com.hk",
    "sunlife.com.hk", "fwd.com.hk", "boclife.com.hk", "ctflife.com.hk",
    "hsbc.com.hk", "yflife.com",
}
PRO = {
    "swissre.com", "allianz.com", "bcg.com", "henleyglobal.com",
    "blackrock.com", "goldmansachs.com", "morganstanley.com",
    "jpmorgan.com", "pimco.com", "ubs.com", "mckinsey.com",
}
MEDIA = {
    "insuranceasia.com", "insurancebusinessmag.com", "insuranceasianews.com",
    "scmp.com", "artemis.bm", "reinsurancenews.com", "bloomberg.com",
    "reuters.com", "ft.com", "wsj.com", "risk.net", "nikkei.com",
}
# 香港本地财经媒体：允许，但单独标 tier 供人工判断（可在下方开关关掉）
MEDIA_HK = {
    "hket.com", "stheadline.com", "mingpao.com", "hkej.com",
    "businesstimes.com.hk", "hk01.com", "thestandard.com.hk",
}
ALLOW_MEDIA_HK = True

MIN_AUTHORITY = 3
MAX_AGE_DAYS = 45
COUNT = 10


def load_key():
    key, base = None, "https://api.deepseek.com"
    if ENV_FILE.is_file():
        for line in ENV_FILE.read_text().splitlines():
            if line.startswith("DEEPSEEK_API_KEY="):
                key = line.split("=", 1)[1].strip().strip('"').strip("'")
            elif line.startswith("DEEPSEEK_BASE_URL="):
                base = line.split("=", 1)[1].strip().strip('"').strip("'").rstrip("/")
    key = key or os.environ.get("DEEPSEEK_API_KEY")
    return key, base


def tracked_hosts():
    """从 last-check.json 动态取已跟踪域名，保持与采集配置同步。"""
    hosts = set()
    try:
        cfg = json.loads(LAST_CHECK.read_text(encoding="utf-8"))
        for _k, v in (cfg.get("sources") or {}).items():
            url = (v or {}).get("url", "")
            if "//" in url:
                hosts.add(url.split("//", 1)[1].split("/", 1)[0].lower().replace("www.", "", 1))
    except (OSError, json.JSONDecodeError):
        pass
    return hosts


def classify(host, tracked):
    def hit(bucket):
        return any(host == d or host.endswith("." + d) for d in bucket)

    if hit(OFFICIAL):
        return "official"
    if hit(INSURER):
        return "insurer"
    if hit(PRO):
        return "pro"
    if hit(MEDIA):
        return "media"
    if ALLOW_MEDIA_HK and hit(MEDIA_HK):
        return "media-hk"
    if host in tracked:
        return "tracked"
    return None


def host_of(url):
    if "//" not in url:
        return ""
    return url.split("//", 1)[1].split("/", 1)[0].lower().replace("www.", "", 1)


def norm(url):
    return url.split("?", 1)[0].rstrip("/").lower()


_SUFFIX_RE = re.compile(r"\s*[-–—|]\s*[^-–—|]{0,20}\d{6,8}.*$|\s*[-–—|]\s*(?:即時|即时|財經|财经|新聞|新闻).*$")


def title_key(title):
    """把「同一事件 / 同一文章的不同站内版本」归一：去站点后缀、去标点、去空白。"""
    t = (title or "").strip()
    t = _SUFFIX_RE.sub("", t)
    t = re.sub(r"[\s\-–—|·:：,，。.、()（）\[\]【】]", "", t)
    return t.lower()


def looks_like_listing(url):
    """列表页/索引页特征：无文章 ID 数字段，且路径含 news/press/circular 之类的栏目名。"""
    path = url.split("//", 1)[-1]
    if re.search(r"\d{4,}", path):
        return False
    return bool(re.search(r"/(?:news|press|press-releases|circulars?|enforcement_news|media-centre)(?:/|\.html?$)", path, re.I))


def search(key, base, query):
    payload = {"query": query, "count": COUNT, "need_content": False}
    req = urllib.request.Request(
        base + "/v1/tools/search",
        data=json.dumps(payload).encode(),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        method="POST",
    )
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.loads(r.read().decode())
    return data.get("results", []), time.time() - t0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    key, base = load_key()
    if not key:
        print("❌ 缺 DEEPSEEK_API_KEY", file=sys.stderr)
        return 1

    tracked = tracked_hosts()

    existing = set()
    if LIVE.is_file():
        raw = json.loads(LIVE.read_text(encoding="utf-8"))
        items = raw if isinstance(raw, list) else raw.get("items", [])
        existing = {norm(str(i.get("originalUrl", ""))) for i in items if i.get("originalUrl")}

    now = datetime.now(timezone.utc)
    stats = {"queries": 0, "failed": 0, "raw": 0, "off_whitelist": 0,
             "low_authority": 0, "stale": 0, "no_date": 0, "dup": 0,
             "dup_title": 0, "kept": 0}
    seen = set()
    seen_titles = set()
    candidates = []
    per_query = []

    for board, q in QUERIES:
        stats["queries"] += 1
        try:
            results, dt = search(key, base, q)
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as exc:
            stats["failed"] += 1
            per_query.append({"board": board, "query": q, "error": f"{type(exc).__name__}: {exc}"})
            print(f"❌ {q}  {type(exc).__name__}")
            continue

        kept_here = 0
        for r in results:
            stats["raw"] += 1
            url = str(r.get("url") or "")
            host = host_of(url)
            tier = classify(host, tracked)

            if not tier:
                stats["off_whitelist"] += 1
                continue
            if int(r.get("authority") or 0) < MIN_AUTHORITY:
                stats["low_authority"] += 1
                continue

            raw_date = r.get("date")
            if not raw_date:
                stats["no_date"] += 1
                continue
            try:
                ts = datetime.fromisoformat(str(raw_date).replace("Z", "+00:00"))
            except ValueError:
                stats["no_date"] += 1
                continue
            if now - ts > timedelta(days=MAX_AGE_DAYS):
                stats["stale"] += 1
                continue

            n = norm(url)
            if n in existing or n in seen:
                stats["dup"] += 1
                continue

            tk = title_key(r.get("title", ""))
            if tk and tk in seen_titles:
                stats["dup_title"] += 1
                continue

            seen.add(n)
            if tk:
                seen_titles.add(tk)
            stats["kept"] += 1
            kept_here += 1
            candidates.append({
                "board": board,
                "query": q,
                "title": r.get("title", ""),
                "url": url,
                "host": host,
                "tier": tier,
                "authority": r.get("authority"),
                "date": str(raw_date)[:10],
                "site_name": r.get("site_name", ""),
                "snippet": (r.get("snippet") or "")[:300],
                "likely_listing": looks_like_listing(url),
            })

        per_query.append({"board": board, "query": q, "n": len(results),
                          "kept": kept_here, "latency_s": round(dt, 1)})
        print(f"✅ {board:11} {q[:24]:26} 取{len(results):2} 留{kept_here:2}  {dt:.1f}s")

    tier_rank = {"official": 0, "insurer": 1, "pro": 2, "media": 3, "media-hk": 4, "tracked": 5}
    # 稳定排序：先按日期新→旧，再按 层级 + authority 分组，组内保持日期序
    candidates.sort(key=lambda c: c["date"], reverse=True)
    candidates.sort(key=lambda c: (tier_rank.get(c["tier"], 9), -int(c["authority"] or 0)))

    payload = {
        "generatedAt": datetime.now().astimezone().isoformat(timespec="seconds"),
        "note": "旁路候选：未写入 live-items.json，需人工/Agent 复核后才入库",
        "config": {"min_authority": MIN_AUTHORITY, "max_age_days": MAX_AGE_DAYS,
                   "allow_media_hk": ALLOW_MEDIA_HK, "count_per_query": COUNT},
        "stats": stats,
        "per_query": per_query,
        "candidates": candidates,
    }

    print("\n=== 统计 ===")
    for k, v in stats.items():
        print(f"  {k}: {v}")

    if args.dry_run:
        print("\n(dry-run，未落盘)")
        return 0

    STAGING.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        f"# Search 补漏候选 · {payload['generatedAt'][:16]}",
        "",
        f"筛选：白名单域名 + authority≥{MIN_AUTHORITY} + {MAX_AGE_DAYS} 天内 + 未收录",
        f"结果：原始 {stats['raw']} 条 → **保留 {stats['kept']}** 条"
        f"（白名单外 {stats['off_whitelist']}、权威低 {stats['low_authority']}、"
        f"过期 {stats['stale']}、无日期 {stats['no_date']}、"
        f"重复 {stats['dup']}、同题 {stats['dup_title']}）",
        "",
        "> ⚠️ 标 `[列表页]` 的是栏目索引，不是单篇文章——入库前需换成具体文章链接。",
        "",
    ]
    by_tier = {}
    for c in candidates:
        by_tier.setdefault(c["tier"], []).append(c)
    for tier in ("official", "insurer", "pro", "media", "media-hk", "tracked"):
        group = by_tier.get(tier)
        if not group:
            continue
        lines.append(f"## {tier}（{len(group)}）")
        for c in group:
            flag = " `[列表页]`" if c.get("likely_listing") else ""
            lines.append(f"- **{c['date']}** [{c['title']}]({c['url']}) · a{c['authority']} · {c['board']}{flag}")
        lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")

    print(f"\n候选：{OUT_JSON}")
    print(f"速览：{OUT_MD}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
