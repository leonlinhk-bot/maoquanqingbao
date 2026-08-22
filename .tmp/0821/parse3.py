#!/usr/bin/env python3
"""Parse SCMP insurance topic page for recent article links + dates."""
import re, html

def clean(s):
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()

raw = open('.tmp/0821/scmp.html', encoding='utf-8', errors='replace').read()
print(f"SCMP size={len(raw)}")

# SCMP article links look like https://www.scmp.com/business/banking-finance/article/...
links = re.findall(r'href="(https://www\.scmp\.com/[^"]+)"', raw)
seen = set()
arts = []
for l in links:
    if '/article/' not in l:
        continue
    if l in seen:
        continue
    seen.add(l)
    arts.append(l)
print("article links:", len(arts))
for a in arts[:40]:
    print("-", a)
