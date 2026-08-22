#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DDG html sweep for 21:08 cron window (2026-08-22 15:03 -> now)."""
import re, html, subprocess, urllib.parse, json, os
from datetime import datetime, timezone, timedelta
HKT = timezone(timedelta(hours=8))
WINDOW = datetime(2026, 8, 22, 15, 3, 34, tzinfo=HKT)
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def search(q, n=10):
    raw = subprocess.run(["curl", "-sL", "--max-time", "25", "-A", UA,
                          "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote(q)],
                         capture_output=True, text=True).stdout
    out = []
    for m in re.finditer(r'class="result__a" href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S):
        url = html.unescape(m.group(1))
        m2 = re.search(r"uddg=([^&]+)", url)
        if m2:
            url = urllib.parse.unquote(m2.group(1))
        title = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", m.group(2)))).strip()
        out.append((title, url))
    snips = re.findall(r'class="result__snippet"[^>]*>(.*?)</a>', raw, re.S)
    snips = [re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip() for s in snips]
    return list(zip(out, snips))

QUERIES = [
    ("ia_press", "香港保监局 新闻 8月22日"),
    ("ia_press_en", "Insurance Authority Hong Kong announcement August 22 2026"),
    ("hkma", "金管局 新闻 8月22日"),
    ("hkma_en", "Hong Kong Monetary Authority press release 22 August 2026"),
    ("aia", "友邦保险 新闻 8月22日"),
    ("aia_en", "AIA Hong Kong news August 22 2026"),
    ("manulife", "宏利 香港 8月22日"),
    ("prudential", "保诚 香港 新闻 8月22日"),
    ("axa", "安盛 香港 新闻 8月22日"),
    ("sunlife", "永明 香港 新闻 8月22日"),
    ("ia_circular", "保监局 通函 8月22日"),
    ("insuranceasia", "insuranceasia Hong Kong news August 2026"),
    ("ib", "Insurance Business Asia news August 2026"),
    ("scmp", "南华早报 保险 8月22日"),
    ("nfra", "金融监管总局 保险 8月22日"),
    ("family", "香港 家族办公室 8月22日"),
    ("insurtech", "香港 保险科技 8月22日"),
    ("hk_ins", "香港保险 8月22日 投保"),
]

os.makedirs('.tmp/raw', exist_ok=True)
allres = []
for tag, q in QUERIES:
    try:
        res = search(q)
    except Exception as e:
        print(f"### {tag}: ERR {e}")
        continue
    print(f"\n### {tag} ({len(res)}) — {q}")
    for (t, u), s in res[:6]:
        print(f"  - {t[:95]}")
        print(f"    {u[:140]}")
        if s:
            print(f"    > {s[:130]}")
        allres.append({"tag": tag, "title": t, "url": u, "snippet": s})

json.dump(allres, open('.tmp/raw/ddg_2125.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f"\nTOTAL {len(allres)} results saved")
