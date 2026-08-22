#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Multi-engine news search: Google News RSS + DuckDuckGo HTML + Bing. Window: >= 2026-08-20T21:14+08:00."""
import re, html, json, subprocess, urllib.parse, datetime, sys, os

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
LAST = datetime.datetime(2026, 8, 20, 21, 14, 53, tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
TZ8 = datetime.timezone(datetime.timedelta(hours=8))

def fetch(url, t=25):
    try:
        return subprocess.run(["curl", "-sL", "--max-time", str(t), "-A", UA,
                               "-H", "Accept-Language: en,zh-CN;q=0.9", url],
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

def gnews(q, hl="zh-HK", gl="HK", n=25):
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

def ddg(q, n=12):
    url = "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote(q)
    raw = fetch(url)
    out = []
    for b in re.split(r'<div class="result results_links', raw)[1:]:
        m = re.search(r'<a[^>]+class="result__a"[^>]+href="([^"]+)"[^>]*>(.*?)</a>', b, re.S)
        if not m: continue
        u = html.unescape(m.group(1))
        u = re.sub(r"^//duckduckgo\.com/l/\?uddg=", "", u)
        u = urllib.parse.unquote(u)
        title = html.unescape(re.sub(r"<[^>]+>", "", m.group(2))).strip()
        sn = re.search(r'<a[^>]+class="result__snippet"[^>]*>(.*?)</a>', b, re.S)
        snip = html.unescape(re.sub(r"<[^>]+>", "", sn.group(1))).strip() if sn else ""
        dm = re.search(r"result__timestamp[^>]*>\s*([^<]+)<", b)
        out.append({"title": title, "url": u, "snippet": snip[:250], "date": (dm.group(1).strip() if dm else "")})
    return out[:n]

def bing(q, n=10):
    url = "https://www.bing.com/search?q=" + urllib.parse.quote(q) + "&count=15&setlang=en&cc=hk"
    raw = fetch(url)
    out = []
    for b in re.split(r'<li class="b_algo"', raw)[1:]:
        m = re.search(r'<h2[^>]*>\s*<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', b, re.S)
        if not m: continue
        u = html.unescape(m.group(1))
        title = html.unescape(re.sub(r"<[^>]+>", "", m.group(2))).strip()
        pm = re.search(r"<p[^>]*>(.*?)</p>", b, re.S)
        snip = html.unescape(re.sub(r"<[^>]+>", "", pm.group(1))).strip() if pm else ""
        dm = re.search(r'<span class="news_dur">([^<]+)</span>', b)
        out.append({"title": title, "url": u, "snippet": snip[:250], "date": (dm.group(1).strip() if dm else "")})
    return out[:n]

def run(tag, q):
    print(f"\n########## {tag}: {q}")
    try:
        res = gnews(q)
        fresh = [r for r in res if r["dt"] and r["dt"] >= LAST.astimezone(datetime.timezone.utc)]
        print(f"--- GoogleNews: {len(res)} total, {len(fresh)} fresh ---")
        for r in (fresh[:8] if fresh else res[:4]):
            dt = r["dt"].astimezone(TZ8).strftime("%m-%d %H:%M") if r["dt"] else "????"
            print(f"  [{dt}] {r['src'][:14]:14s} {r['title'][:85]}")
            print(f"        {r['link'][:120]}")
    except Exception as e:
        print("  GN ERR", e)
    try:
        res = ddg(q)
        print(f"--- DuckDuckGo: {len(res)} ---")
        for r in res[:7]:
            print(f"  [{r['date'][:12]}] {r['title'][:85]}")
            print(f"        {r['url'][:120]}")
    except Exception as e:
        print("  DDG ERR", e)
    try:
        res = bing(q)
        print(f"--- Bing: {len(res)} ---")
        for r in res[:7]:
            print(f"  [{r['date'][:12]}] {r['title'][:85]}")
            print(f"        {r['url'][:120]}")
    except Exception as e:
        print("  BING ERR", e)

if __name__ == "__main__":
    tag = sys.argv[1]
    q = sys.argv[2]
    run(tag, q)
