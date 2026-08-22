#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Debug: dump Bing search HTML."""
import subprocess, re, sys
from urllib.parse import quote

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126"
q = sys.argv[1]
r = subprocess.run(["curl", "-sL", "--max-time", "25", "-A", UA,
                    f"https://www.bing.com/search?q={quote(q)}&count=12"],
                   capture_output=True, text=True, timeout=35)
h = r.stdout
print("len:", len(h))
print("has captcha:", "captcha" in h.lower())
print("b_algo count:", h.count("b_algo"))
m = re.search(r"<title>(.*?)</title>", h, re.S)
print("title:", m.group(1) if m else None)
open(".tmp/0821/bing-debug.html", "w", encoding="utf-8").write(h)
# print all hrefs to external sites
for mm in re.finditer(r'href="(https?://[^"]+)"', h):
    u = mm.group(1)
    if "bing.com" in u or "microsoft" in u or "go.micro" in u:
        continue
    print("H:", u[:160])
