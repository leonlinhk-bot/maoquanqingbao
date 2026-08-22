#!/usr/bin/env python3
import re, html

raw = open('.tmp/0821/scmp.html', encoding='utf-8', errors='ignore').read()
print('SCMP len', len(raw))
# Try JSON-LD or headline patterns
heads = re.findall(r'<h\d[^>]*>(.*?)</h\d>', raw, re.S)
n = 0
for h in heads:
    t = html.unescape(re.sub(r'<[^>]+>', '', h)).strip()
    t = re.sub(r'\s+', ' ', t)
    if len(t) > 25 and ('insur' in t.lower() or 'insurance' in t.lower() or '保' in t):
        print('H:', t[:100])
        n += 1
        if n >= 20:
            break
print('---headlines with insurance:', n)
# JSON-LD
for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', raw, re.S):
    j = m.group(1)
    if 'NewsArticle' in j and '2026-08-2' in j:
        print('JSONLD:', j[:400].replace('\n', ' '))
