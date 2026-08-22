#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract result links from saved Bing debug HTML."""
import re, html

h = open(".tmp/0821/bing-debug.html", encoding="utf-8", errors="replace").read()
# split by b_algo blocks
blocks = re.split(r'<li class="b_algo"', h)[1:]
print("blocks:", len(blocks))
for i, b in enumerate(blocks[:12]):
    m = re.search(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', b, re.S)
    if m:
        u = html.unescape(m.group(1))
        t = html.unescape(re.sub(r"<[^>]+>", "", m.group(2))).strip()
        print(f"[{i}] {t[:95]}\n    {u[:170]}")
    # snippet
    s = re.search(r'<p[^>]*>(.*?)</p>', b, re.S)
    if s:
        sn = html.unescape(re.sub(r"<[^>]+>", "", s.group(1))).strip()
        print("    SN:", sn[:180])
