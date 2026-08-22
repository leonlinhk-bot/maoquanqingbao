#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bing search via curl; save parsed results (title/url/snippet/date) to JSON + text."""
import json, subprocess, os, sys, re, html, time, urllib.parse

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def _env():
    e = os.environ.copy()
    for k in list(e):
        if "proxy" in k.lower():
            del e[k]
    return e

def fetch(url):
    r = subprocess.run(["curl", "-s", "-m", "25", "-L", "-A", UA,
                        "-H", "Accept-Language: zh-CN,zh;q=0.9,en;q=0.8",
                        url], capture_output=True, text=True, env=_env())
    return r.stdout

def bing_search(q, count=10):
    url = "https://www.bing.com/search?q=" + urllib.parse.quote(q) + f"&count={count}&setlang=en"
    raw = fetch(url)
    out = []
    # b_algo blocks
    blocks = re.split(r'<li class="b_algo"', raw)[1:]
    for b in blocks:
        m = re.search(r'<h2[^>]*>\s*<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', b, re.S)
        if not m:
            continue
        url2 = html.unescape(m.group(1))
        title = html.unescape(re.sub(r'<[^>]+>', '', m.group(2))).strip()
        pm = re.search(r'<p[^>]*>(.*?)</p>', b, re.S)
        snip = html.unescape(re.sub(r'<[^>]+>', '', pm.group(1))).strip() if pm else ""
        dm = re.search(r'<span class="news_dur">([^<]+)</span>', b) or re.search(r'class="algoSlug_icon"[^>]*>\s*([^<]{4,40})', b)
        date = dm.group(1).strip() if dm else ""
        out.append({"title": title, "url": url2, "snippet": snip[:300], "date": date})
    return out

def main():
    q = sys.argv[1]
    tag = sys.argv[2] if len(sys.argv) > 2 else "q"
    res = bing_search(q)
    path = f"/tmp/bing_{tag}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1)
    print(f"== {tag} ({len(res)} results) ==")
    for r in res:
        print(f"- [{r['date']}] {r['title'][:80]}")
        print(f"  {r['url'][:150]}")
        print(f"  {r['snippet'][:180]}")

if __name__ == "__main__":
    main()
