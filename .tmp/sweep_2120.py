#!/usr/bin/env python3
"""Bing News RSS sweep for 2026-08-22 21:08 cron. Window: 2026-08-22T15:03:34+08:00."""
import subprocess, re, html, os, json
from urllib.parse import quote
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime

HKT = timezone(timedelta(hours=8))
WINDOW_START = datetime(2026, 8, 22, 15, 3, 34, tzinfo=HKT)
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126"

QUERIES = [
    # (tag, query)
    ("ia_press", "Hong Kong Insurance Authority press release"),
    ("ia_press_zh", "香港保监局 新闻稿"),
    ("ia_circular", "保监局 通函 保险"),
    ("hkma_press", "Hong Kong Monetary Authority"),
    ("hkma_zh", "金管局 银行 新闻"),
    ("aia_news", "AIA Hong Kong"),
    ("aia_zh", "友邦保险"),
    ("manulife_news", "Manulife Hong Kong"),
    ("manulife_zh", "宏利 香港"),
    ("prudential_news", "Prudential Hong Kong insurance"),
    ("prudential_zh", "保诚 香港 保险"),
    ("axa_news", "AXA Hong Kong insurance"),
    ("axa_zh", "安盛 香港 保险"),
    ("sunlife_news", "Sun Life Hong Kong"),
    ("sunlife_zh", "永明 香港 保险"),
    ("insurance_asia", "InsuranceAsia"),
    ("insurance_business", "Insurance Business Asia"),
    ("scmp_insurance", "SCMP Hong Kong insurance"),
    ("nfra", "金融监管总局 保险"),
    ("family_office", "Hong Kong family office"),
    ("family_office_zh", "香港 家族办公室"),
    ("insurtech", "insurtech Hong Kong insurance"),
    ("insurtech_zh", "保险科技 香港"),
    ("hk_insurance", "香港保险 内地访客"),
]

os.makedirs('.tmp/raw', exist_ok=True)

def fetch(url):
    return subprocess.run(["curl", "-sL", "--max-time", "25", "-A", UA, url],
                          capture_output=True, text=True).stdout

results = []
for tag, q in QUERIES:
    url = f"https://www.bing.com/news/search?q={quote(q)}&format=rss&setlang=en&count=15"
    xml = fetch(url)
    fn = f'.tmp/raw/bing_{tag}.xml'
    open(fn, 'w', encoding='utf-8').write(xml)
    items = re.findall(r"<item>(.*?)</item>", xml, re.S)
    tag_hits = []
    for it in items:
        t = re.search(r"<title>(.*?)</title>", it, re.S)
        l = re.search(r"<link>(.*?)</link>", it, re.S)
        d = re.search(r"<pubDate>(.*?)</pubDate>", it, re.S)
        src = re.search(r"<Source>(.*?)</Source>", it, re.S)
        title = html.unescape(t.group(1)).strip() if t else ""
        link = html.unescape(l.group(1)).strip() if l else ""
        try:
            dt = parsedate_to_datetime(d.group(1)).astimezone(HKT) if d else None
        except Exception:
            dt = None
        tag_hits.append((dt, title, link, (src.group(1) if src else "")))
    # sort by date desc
    tag_hits.sort(key=lambda x: (x[0] is not None, x[0] or datetime.min.replace(tzinfo=HKT)), reverse=True)
    new_in_window = [h for h in tag_hits if h[0] and h[0] >= WINDOW_START]
    print(f"\n===== {tag} ({len(items)} items, {len(new_in_window)} in window) =====")
    for dt, title, link, src in tag_hits[:10]:
        flag = "NEW" if dt and dt >= WINDOW_START else ("old" if dt else "nodate")
        print(f"[{flag}] {dt.strftime('%m-%d %H:%M') if dt else '????????'} | {src[:18]:18s} | {title[:72]}")
        if flag == "NEW":
            results.append({"tag": tag, "dt": dt.isoformat() if dt else None, "title": title, "link": link, "src": src})

json.dump(results, open('.tmp/raw/sweep_2120.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f"\nTOTAL in-window candidates: {len(results)}")
