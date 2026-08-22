#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Google News sweep for all sources. Window: >= 2026-08-20T21:14+08:00."""
import re, html, json, subprocess, urllib.parse, datetime

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
LAST = datetime.datetime(2026, 8, 20, 21, 14, 53, tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
TZ8 = datetime.timezone(datetime.timedelta(hours=8))

def fetch(url, t=25):
    try:
        return subprocess.run(["curl", "-sL", "--max-time", str(t), "-A", UA, url],
                              capture_output=True, text=True, timeout=35).stdout
    except Exception:
        return ""

def parse_dt(s):
    if not s: return None
    for fmt in ("%a, %d %b %Y %H:%M:%S %Z", "%a, %d %b %Y %H:%M:%S %z"):
        try:
            pd = datetime.datetime.strptime(s.strip(), fmt)
            if pd.tzinfo is None: pd = pd.replace(tzinfo=datetime.timezone.utc)
            return pd
        except Exception:
            continue
    return None

def gnews(q, hl="zh-HK", gl="HK", n=30):
    url = f"https://news.google.com/rss/search?q={urllib.parse.quote(q)}&hl={hl}&gl={gl}&ceid={gl}:{hl}"
    raw = fetch(url)
    out = []
    for it in re.findall(r"<item>(.*?)</item>", raw, re.S):
        t = re.search(r"<title>(.*?)</title>", it, re.S)
        l = re.search(r"<link>(.*?)</link>", it, re.S)
        d = re.search(r"<pubDate>(.*?)</pubDate>", it, re.S)
        s = re.search(r"<source[^>]*>(.*?)</source>", it, re.S)
        out.append({"title": html.unescape(t.group(1)) if t else "",
                    "link": html.unescape(l.group(1)) if l else "",
                    "dt": parse_dt(d.group(1)) if d else None,
                    "src": html.unescape(s.group(1)) if s else ""})
    return out

QUERIES = [
    ("ia-press", "Insurance Authority Hong Kong 保监局 2026"),
    ("ia-press2", "保监局 保险业 监管 8月22日"),
    ("hkma-news", "金管局 香港 2026年8月21日"),
    ("hkma-news2", "Hong Kong Monetary Authority August 22 2026"),
    ("aia-news", "友邦保险 AIA 2026年8月21日"),
    ("aia-news2", "AIA Hong Kong news August 22 2026"),
    ("manulife-news", "宏利 香港 2026年8月"),
    ("pru-news", "保诚 香港 2026年8月21日"),
    ("iaa-news", "Insurance Asia insurance news August 22 2026"),
    ("iaa-news2", "香港保险 新造保费 2026"),
    ("ib-news", "Insurance Business Asia August 21 2026"),
    ("scmp-ins", "SCMP insurance Hong Kong August 2026"),
    ("nfra", "金融监管总局 保险 2026年8月21日"),
    ("nfra2", "国家金融监督管理总局 通知 2026年8月"),
    ("family-office", "香港 家办 家族办公室 2026年8月"),
    ("fstb", "香港 财经事务及库务局 2026年8月"),
    ("insurtech", "香港 保险科技 insurtech 2026年8月"),
    ("mcv", "香港保险 内地访客 2026年8月 保费"),
    ("premfin", "保费融资 保监局 2026"),
    ("china-tax", "香港保单 征税 2026年8月"),
]

allres = {}
for tag, q in QUERIES:
    try:
        res = gnews(q)
    except Exception as e:
        print(f"ERR {tag}: {e}")
        continue
    fresh = [r for r in res if r["dt"] and r["dt"] >= LAST.astimezone(datetime.timezone.utc)]
    allres[tag] = {"q": q, "total": len(res), "fresh": fresh}
    print(f"\n=== GN[{tag}] '{q}': {len(res)} total, {len(fresh)} fresh ===")
    for r in (fresh[:10] if fresh else res[:4]):
        dt = r["dt"].astimezone(TZ8).strftime("%m-%d %H:%M") if r["dt"] else "????"
        print(f"- {dt} | {r['src'][:16]:16s} | {r['title'][:88]}")
        print(f"    {r['link'][:110]}")
    if not fresh:
        print("  (no fresh; older shown above)")

json.dump({k: {"q": v["q"], "total": v["total"],
               "fresh": [{"title": r["title"], "link": r["link"], "src": r["src"],
                          "dt": r["dt"].isoformat() if r["dt"] else None} for r in v["fresh"]]}
           for k, v in allres.items()},
          open("data/_raw/t0822b/gnews-sweep.json", "w"), ensure_ascii=False, indent=1)
print("\nSAVED data/_raw/t0822b/gnews-sweep.json")
