#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Daily collection v2: HKMA parse + InsuranceAsia RSS (+article titles) + Google News/Bing sweep."""
import re, html, json, subprocess, urllib.parse, datetime

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
TZ8 = datetime.timezone(datetime.timedelta(hours=8))
UTC = datetime.timezone.utc
LAST = datetime.datetime(2026, 8, 20, 21, 14, 53, tzinfo=TZ8)
NOW = datetime.datetime.now(TZ8)
print(f"Window: {LAST.isoformat()} -> {NOW.isoformat()}")

def fetch(url):
    return subprocess.run(["curl", "-sL", "--max-time", "30", "-A", UA, url],
                          capture_output=True, text=True).stdout

def parse_pubdate(s):
    if not s:
        return None
    s = s.strip()
    for fmt in ("%a, %d %b %Y %H:%M:%S %Z", "%a, %d %b %Y %H:%M:%S %z",
                "%a, %d %b %Y %H:%M:%S GMT", "%Y-%m-%dT%H:%M:%S%z",
                "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%d %H:%M:%S"):
        try:
            dt = datetime.datetime.strptime(s, fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=UTC)
            return dt
        except Exception:
            continue
    return None

def gnews(q, hl="zh-HK", gl="HK", n=25):
    url = f"https://news.google.com/rss/search?q={urllib.parse.quote(q)}&hl={hl}&gl={gl}&ceid={gl}:{hl}"
    raw = fetch(url)
    items = re.findall(r"<item>(.*?)</item>", raw, re.S)
    out = []
    for it in items:
        t = re.search(r"<title>(.*?)</title>", it, re.S)
        l = re.search(r"<link>(.*?)</link>", it, re.S)
        d = re.search(r"<pubDate>(.*?)</pubDate>", it, re.S)
        s = re.search(r"<source[^>]*>(.*?)</source>", it, re.S)
        out.append({
            "title": html.unescape(t.group(1)) if t else "",
            "link": html.unescape(l.group(1)) if l else "",
            "dt": parse_pubdate(d.group(1)) if d else None,
            "source": html.unescape(s.group(1)) if s else "",
        })
    return out

def bing_rss(q):
    url = f"https://www.bing.com/news/search?q={urllib.parse.quote(q)}&format=rss&setlang=en"
    raw = fetch(url)
    out = []
    for it in re.findall(r"<item>(.*?)</item>", raw, re.S):
        t = re.search(r"<title>(.*?)</title>", it, re.S)
        l = re.search(r"<link>(.*?)</link>", it, re.S)
        d = re.search(r"<pubDate>(.*?)</pubDate>", it, re.S)
        out.append({"title": html.unescape(t.group(1)) if t else "",
                    "link": html.unescape(l.group(1)) if l else "",
                    "dt": parse_pubdate(d.group(1)) if d else None, "source": "bing"})
    return out

def parse_hkma(raw):
    out = []
    for m in re.finditer(r'<li>(\d{1,2} \w{3} \d{4})</li><li><a href="(/eng/news-and-media/press-releases/[^"]+)" title="([^"]+)">', raw):
        dt = datetime.datetime.strptime(m.group(1), "%d %b %Y").replace(tzinfo=TZ8)
        out.append({"title": html.unescape(m.group(3)).strip(),
                    "url": "https://www.hkma.gov.hk" + m.group(2), "dt": dt})
    return out

def og_title(url):
    raw = fetch(url)
    m = re.search(r'<meta property="og:title" content="([^"]+)"', raw)
    if m:
        return html.unescape(m.group(1)).strip()
    m = re.search(r'<title[^>]*>([^<]+)</title>', raw, re.S)
    return html.unescape(m.group(1)).strip() if m else ""

def parse_iarss(raw):
    out = []
    for it in re.findall(r"<item>(.*?)</item>", raw, re.S):
        t = re.search(r"<title>(.*?)</title>", it, re.S)
        l = re.search(r"<link>(.*?)</link>", it, re.S)
        d = re.search(r"<pubDate>(.*?)</pubDate>", it, re.S)
        out.append({"title": html.unescape(t.group(1)) if t else "",
                    "link": html.unescape(l.group(1)) if l else "",
                    "dt": parse_pubdate(d.group(1)) if d else None, "source": "insuranceasia"})
    return out

all_cands = {}

# 1. HKMA
raw = fetch("https://www.hkma.gov.hk/eng/news-and-media/press-releases/")
hkma_all = parse_hkma(raw)
hkma_items = [x for x in hkma_all if x["dt"] >= LAST]
all_cands["hkma"] = hkma_items
print(f"\n=== HKMA page: {len(hkma_all)} entries, {len(hkma_items)} fresh ===")
for it in hkma_items:
    print("-", it["dt"].strftime("%m-%d"), "|", it["title"][:80], "|", it["url"])

# 2. InsuranceAsia RSS + real titles
raw = fetch("https://insuranceasia.com/rss.xml")
ia_all = parse_iarss(raw)
ia_items = [x for x in ia_all if x["dt"] and x["dt"].astimezone(TZ8) >= LAST]
print(f"\n=== InsuranceAsia RSS: {len(ia_all)} entries, {len(ia_items)} fresh ===")
for x in ia_items:
    x["full_title"] = og_title(x["link"])
    print("-", x["dt"].astimezone(TZ8).strftime("%m-%d %H:%M"), "|", x["full_title"][:90])
all_cands["insurance_asia"] = ia_items

# 3. Google News sweep
QUERIES = [
    ("ia", "Hong Kong Insurance Authority"),
    ("ia_cn", "香港保监局"),
    ("hkma", "HKMA Hong Kong Monetary Authority"),
    ("aia", "AIA Hong Kong insurance"),
    ("manulife", "Manulife Hong Kong"),
    ("prudential", "Prudential Hong Kong"),
    ("axa", "AXA Hong Kong insurance"),
    ("sunlife", "Sun Life Hong Kong"),
    ("insuranceasia", "insuranceasia.com"),
    ("ibmag", "Insurance Business Asia"),
    ("scmp", "SCMP Hong Kong insurance"),
    ("nfra", "国家金融监督管理总局 保险"),
    ("familyoffice", "香港 家族办公室 保险"),
    ("insurtech", "香港 保险科技 InsurTech"),
    ("hkins", "香港保險"),
    ("hkins_en", "Hong Kong insurance market news"),
    ("premiumfin", "保费融资 保监局 通函"),
    ("mcv", "内地访客 香港保险 新造保单"),
]
for tag, q in QUERIES:
    try:
        res = gnews(q)
    except Exception as e:
        print(f"ERR {tag}: {e}")
        continue
    fresh = [r for r in res if r["dt"] and r["dt"].astimezone(TZ8) >= LAST]
    all_cands[tag] = fresh
    print(f"\n=== GN[{tag}] '{q}': {len(res)} total, {len(fresh)} fresh ===")
    for r in fresh[:12]:
        print("-", r["dt"].astimezone(TZ8).strftime("%m-%d %H:%M"), "|", r["source"][:16], "|", r["title"][:80])

# 4. Bing cross-check
for tag, q in [("ia_en", "Hong Kong Insurance Authority news August 2026"),
               ("hkins_en", "Hong Kong insurance news August 2026"),
               ("premiumfin", "保费融资 香港 保险 2026")]:
    try:
        res = bing_rss(q)
    except Exception as e:
        print(f"ERR bing {tag}: {e}")
        continue
    fresh = [r for r in res if r["dt"] and r["dt"].astimezone(TZ8) >= LAST]
    all_cands["bing_" + tag] = fresh
    print(f"\n=== BING[{tag}]: {len(res)} total, {len(fresh)} fresh ===")
    for r in fresh[:10]:
        print("-", r["dt"].astimezone(TZ8).strftime("%m-%d %H:%M"), "|", r["title"][:85])

seen = set()
uniq = []
for k, v in all_cands.items():
    for r in v:
        key = (r.get("full_title") or r["title"])[:60].lower()
        if key in seen:
            continue
        seen.add(key)
        uniq.append({**r, "tag": k})
print(f"\n=== UNIQUE fresh candidates: {len(uniq)} ===")
for r in sorted(uniq, key=lambda x: x["dt"] or datetime.datetime.min, reverse=True):
    t = r.get("full_title") or r["title"]
    print("-", r["dt"].astimezone(TZ8).strftime("%m-%d %H:%M") if r["dt"] else "????", "|",
          r["tag"], "|", r["source"][:14], "|", t[:75])

json.dump({k: [{"title": x["title"], "link": x["link"],
                "dt": x["dt"].astimezone(TZ8).isoformat() if x["dt"] else None,
                "source": x["source"], "full_title": x.get("full_title", "")} for x in v]
           for k, v in all_cands.items()},
          open(".tmp/cands.json", "w"), ensure_ascii=False, indent=1)
print("\nSaved .tmp/cands.json")
