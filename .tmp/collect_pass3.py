#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pass 3: resolve original URLs for candidate stories."""
import re, html, json, subprocess, urllib.parse, datetime

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def fetch(url):
    try:
        return subprocess.run(["curl", "-sL", "--max-time", "30", "-A", UA, url],
                              capture_output=True, text=True, timeout=40).stdout
    except Exception:
        return ""

def bing_rss(q, n=10):
    url = f"https://www.bing.com/search?q={urllib.parse.quote(q)}&format=rss&count=15"
    raw = fetch(url)
    items = re.findall(r"<item>(.*?)</item>", raw, re.S)
    out = []
    for it in items:
        t = re.search(r"<title>(.*?)</title>", it, re.S)
        l = re.search(r"<link>(.*?)</link>", it, re.S)
        d = re.search(r"<pubDate>(.*?)</pubDate>", it, re.S)
        pd = None
        if d:
            for fmt in ("%a, %d %b %Y %H:%M:%S %Z", "%a, %d %b %Y %H:%M:%S %z"):
                try:
                    pd = datetime.datetime.strptime(d.group(1).strip(), fmt)
                    if pd.tzinfo is None:
                        pd = pd.replace(tzinfo=datetime.timezone.utc)
                    break
                except Exception:
                    continue
        out.append({"title": html.unescape(t.group(1)).strip() if t else "",
                    "link": html.unescape(l.group(1)).strip() if l else "",
                    "dt": pd})
    return out

def show(tag, res, n=8):
    print(f"\n=== {tag} ===")
    for r in res[:n]:
        dts = r["dt"].astimezone(datetime.timezone(datetime.timedelta(hours=8))).strftime("%m-%d %H:%M") if r["dt"] else "?"
        print(f"* [{dts}] {r['title'][:90]}")
        print(f"  {r['link'][:160]}")

# 1. HKMA press releases direct (work via curl)
for slug in ["20260821-3", "20260821-4", "20260820-4", "20260820-3"]:
    raw = fetch(f"https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/08/{slug}/")
    t = re.search(r"<title>(.*?)</title>", raw, re.S)
    print(f"=== HKMA {slug}: {(html.unescape(t.group(1)).strip()[:100] if t else 'N/A')} (len={len(raw)})")

# 2. Original URLs for media stories
show("hengda", bing_rss("恒大人寿 吊销 保险业务许可 金融监管总局 8月21日"))
show("silverbond", bing_rss("银色债券2026 认购 8月21日 保证息率"))
show("aia-tax", bing_rss("友邦 税策无碍内地客 需求 新业务价值 信报"))
show("ubs-aia", bing_rss("瑞银 友邦 目标价 102港元 买入"))
show("manulife-airside", bing_rss("宏利 AIRSIDE 乐活节奏健康节"))
show("pru-buyback", bing_rss("Prudential buyback shares August 21 2026"))
show("juliusbaer", bing_rss("金管局 Bank Julius Baer 骗案 通知"))
show("pboc-bills", bing_rss("中国人民银行 香港 300亿元 央行票据"))
