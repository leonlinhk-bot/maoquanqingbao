#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pass 2: targeted Google News + Bing RSS for sources with no fresh results."""
import re, html, json, subprocess, urllib.parse, datetime

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
LAST = datetime.datetime(2026, 8, 20, 21, 14, 53, tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
tz8 = datetime.timezone(datetime.timedelta(hours=8))

def fetch(url):
    try:
        return subprocess.run(["curl", "-sL", "--max-time", "30", "-A", UA, url],
                              capture_output=True, text=True, timeout=40).stdout
    except Exception:
        return ""

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
        title = html.unescape(t.group(1)) if t else ""
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
        out.append({"title": title, "link": html.unescape(l.group(1)) if l else "",
                    "dt": pd, "source": html.unescape(s.group(1)) if s else ""})
    return out

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
                    "dt": pd, "source": "bing"})
    return out

def show(tag, res, label):
    fresh = [r for r in res if r["dt"] and r["dt"] >= LAST.astimezone(datetime.timezone.utc)]
    print(f"\n=== {label}: {len(res)} total, {len(fresh)} fresh ===")
    for r in fresh[:12]:
        dts = r["dt"].astimezone(tz8).strftime("%m-%d %H:%M") if r["dt"] else "?"
        print(f"* [{dts}] {r.get('source','')[:20]} | {r['title'][:95]}")
        print(f"  {r['link'][:150]}")

Q2 = [
    ("ia_circular", "保监局 通函 site:ia.org.hk"),
    ("ia_en", "Insurance Authority circular August 2026"),
    ("insuranceasia", "insuranceasia insurance August 2026"),
    ("ibmag", "insurancebusinessmag.com Asia insurance"),
    ("axa", "AXA 香港 保險"),
    ("sunlife", "Sun Life 香港 保險"),
    ("scmp", "site:scmp.com insurance Hong Kong"),
    ("nfra", "金融监管总局 保险 8月21日"),
    ("nfra2", "国家金融监督管理总局 保险业"),
    ("familyoffice", "家族办公室 香港 新政策"),
    ("insurtech", "香港 保险科技 InsurTech 2026"),
    ("aia2", "友邦保险 内地客 需求"),
    ("hkma2", "金管局 8月21日"),
]
for tag, q in Q2:
    try:
        show(tag, gnews(q), f"GN[{tag}] {q}")
    except Exception as e:
        print(f"ERR {tag}: {e}")

# Bing RSS for IA circular specifically
show("bing_ia", bing_rss("保监局 通函 8月"), "BING[ia-circular]")
show("bing_ia2", bing_rss('site:ia.org.hk circular 2026'), "BING[ia-site]")
