#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mojeek + DDG-lite retry. Usage: python3 hunt2.py 'query'"""
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

q = sys.argv[1]
print(f"### Mojeek [{q}]")
h = fetch(f"https://www.mojeek.com/search?q={quote(q)}")
print("size:", len(h))
for m in re.finditer(r'<a class="ob"[^>]+href="([^"]+)"[^>]*>(.*?)</a>', h, re.S):
    print("T:", html.unescape(re.sub(r"<[^>]+>", "", m.group(2))).strip()[:90])
    print("U:", html.unescape(m.group(1))[:170])
print(f"\n### DDG-lite [{q}]")
h = fetch(f"https://lite.duckduckgo.com/lite/?q={quote(q)}")
print("size:", len(h))
if "challenge" in h.lower() or "anomaly" in h.lower():
    print("challenge page")
for m in re.finditer(r'<a[^>]+href="(https?://[^"]+)"[^>]*>(.*?)</a>', h, re.S):
    u = html.unescape(m.group(1))
    if "duckduckgo" in u:
        continue
    t = html.unescape(re.sub(r"<[^>]+>", "", m.group(2))).strip()
    if len(t) > 20:
        print("T:", t[:90])
        print("U:", u[:170])
