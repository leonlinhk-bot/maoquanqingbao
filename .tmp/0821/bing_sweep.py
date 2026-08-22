#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bing RSS sweep for remaining sources - 2026-08-21."""
import re, html, subprocess, json, os
from urllib.parse import quote

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126"
os.makedirs(".tmp/0821", exist_ok=True)

def fetch(url):
    return subprocess.run(["curl", "-sL", "--max-time", "30", "-A", UA, url],
                          capture_output=True, text=True).stdout

def bing(tag, q):
    print("=" * 70)
    print(f"[{tag}] {q}")
    xml = fetch("https://www.bing.com/search?q=" + quote(q) + "&format=rss&count=15")
    items = re.findall(r"<item>(.*?)</item>", xml, re.S)
    print(f"  ({len(items)} results)")
    out = []
    for it in items[:12]:
        t = re.search(r"<title>(.*?)</title>", it, re.S)
        l = re.search(r"<link>(.*?)</link>", it, re.S)
        d = re.search(r"<pubDate>(.*?)</pubDate>", it, re.S)
        title = html.unescape(t.group(1)).strip() if t else ''
        link = html.unescape(l.group(1)).strip() if l else ''
        date = d.group(1)[:25] if d else ''
        print(f"  - {date:26s} | {title[:95]}")
        print(f"    {link[:160]}")
        out.append({"date": date, "title": title, "link": link})
    with open(f".tmp/0821/bing_{tag}.json", "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    return out

# 1. IA (regulator) - blocked by CF, rely on search index
bing("ia_press", 'site:ia.org.hk press release August 2026')
bing("ia_circ", 'site:ia.org.hk circular 2026年8月')
bing("ia_news", '保监局 新闻稿 8月21日')
# 2. NFRA
bing("nfra", '金融监管总局 保险 2026年8月21日')
bing("nfra2", 'site:nfra.gov.cn 保险 8月')
# 3. Family office
bing("famoffice", '香港 家族办公室 2026年8月')
bing("famoffice2", 'family office Hong Kong August 2026')
# 4. Insurtech
bing("insurtech", '香港 保险科技 2026年8月')
bing("insurtech2", 'Insurtech Hong Kong August 2026')
# 5. SCMP
bing("scmp", 'site:scmp.com insurance Hong Kong')
# 6. Insurers HK
bing("sunlife", '永明 香港 新聞 2026年8月')
bing("aia_hk", '友邦香港 新聞稿 2026年8月')
bing("manulife_hk", '宏利香港 新聞 2026年8月')
bing("prudential_hk", '保誠 香港 新聞 2026年8月')
bing("axa_hk", '安盛 香港 新聞 2026年8月')
# 7. HK insurance general
bing("hk_ins", '香港 保險業 2026年8月21日')
bing("hk_ins2", '香港保險 新單 2026年8月')
