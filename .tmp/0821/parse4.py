#!/usr/bin/env python3
"""Extract first paragraphs from fetched IBMag article pages; scan SCMP html for links."""
import re, html, json

def clean(s):
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()

for aid in ['586912', '586909', '586906', '586726', '586773']:
    raw = open(f'.tmp/0821/ib-{aid}.html', encoding='utf-8', errors='replace').read()
    # article body paragraphs
    paras = re.findall(r'<p[^>]*>(.*?)</p>', raw, re.S)
    txts = [clean(p) for p in paras]
    txts = [t for t in txts if len(t) > 40]
    print(f"\n===== IBMag {aid} ===== ({len(txts)} paras)")
    for t in txts[:6]:
        print("-", t[:220])

# SCMP link scan
raw = open('.tmp/0821/scmp.html', encoding='utf-8', errors='replace').read()
links = re.findall(r'href="(https?://[^"]*scmp\.com[^"]*)"', raw)
print(f"\nSCMP links total: {len(links)}")
seen = set()
for l in links:
    if l in seen: continue
    seen.add(l)
    if any(k in l for k in ['insurance', 'insurance-sector', 'banking-finance', 'markets']):
        print("-", l[:150])
