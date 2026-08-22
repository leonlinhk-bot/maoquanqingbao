#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Multi-engine search: ddg-lite, bing site:, publisher search. Usage: python3 hunt.py 'query' [site]"""
import subprocess, re, html, sys
from urllib.parse import quote

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126"

def fetch(url):
    try:
        r = subprocess.run(["curl", "-sL", "--max-time", "25", "-A", UA, url],
                           capture_output=True, text=True, timeout=35)
        return r.stdout
    except Exception:
        return ""

def ddg_lite(q):
    h = fetch(f"https://lite.duckduckgo.com/lite/?q={quote(q)}")
    print(f"--- DDG-lite [{q[:70]}] size={len(h)} ---")
    for m in re.finditer(r'<a[^>]+class="result-link"[^>]+href="([^"]+)"[^>]*>(.*?)</a>', h, re.S):
        print("T:", html.unescape(re.sub(r"<[^>]+>", "", m.group(2))).strip()[:90])
        print("U:", html.unescape(m.group(1))[:170])
    # alt: any external link
    for m in re.finditer(r'<a[^>]+href="(https?://[^"]+)"[^>]*>(.*?)</a>', h, re.S):
        u = html.unescape(m.group(1))
        if any(x in u for x in ["duckduckgo", "duck.co"]):
            continue
        t = html.unescape(re.sub(r"<[^>]+>", "", m.group(2))).strip()
        if len(t) > 15:
            print("T:", t[:90])
            print("U:", u[:170])

def bing_site(q, site):
    h = fetch(f"https://www.bing.com/search?q={quote(q + ' site:' + site)}&count=10")
    print(f"--- Bing-site {site} [{q[:50]}] size={len(h)} ---")
    blocks = re.split(r'<li class="b_algo"', h)[1:]
    for i, b in enumerate(blocks[:8]):
        m = re.search(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', b, re.S)
        if m:
            u = html.unescape(m.group(1))
            t = html.unescape(re.sub(r"<[^>]+>", "", m.group(2))).strip()
            if "bing.com" in u:
                continue
            print(f"[{i}] {t[:90]}\n    {u[:170]}")

if __name__ == "__main__":
    q = sys.argv[1]
    ddg_lite(q)
    if len(sys.argv) > 2:
        bing_site(q, sys.argv[2])
