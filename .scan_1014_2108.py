#!/usr/bin/env python3
"""Scan insurer / HKFI / NFRA pages for announcements dated on/after 2026-10-13."""
import re, os, html, glob

D = '/Users/leonliang/maoquanqingbao/data/_1014_2108'
FILES = {
    'aia': f'{D}/aia.raw',
    'prudential': f'{D}/prudential.raw',
    'axa': f'{D}/axa.raw',
    'sunlife': f'{D}/sunlife.raw',
    'hkfi': '/tmp/hkfi.html',
    'nfra': f'{D}/nfra.raw',
    'nfra_stats': f'{D}/nfra_stats.raw',
}
PAT_DATES = [
    r'2026[-/年]\s*1[0-2][-/月]\s*[0-3]?\d日?',   # 2026-10-14 / 2026年10月14日
    r'\b\d{1,2}\s+(?:Oct|October)\s+2026\b',
    r'\b(?:Oct|October)\s+\d{1,2},?\s+2026\b',
    r'2026-1[0-2]-\d{2}',
]


def strip(s):
    return html.unescape(re.sub(r'\s+', ' ', re.sub('<[^>]+>', ' ', s))).strip()


for name, path in FILES.items():
    if not os.path.exists(path):
        print(f'\n### {name}: MISSING'); continue
    raw = open(path, encoding='utf-8', errors='replace').read()
    print(f'\n### {name}  ({len(raw)} bytes)')
    hits = []
    for m in re.finditer(r'(?is)<(?:a|li|h[1-4]|div|p|span|td)[^>]*>(.{0,400}?)</(?:a|li|h[1-4]|div|p|span|td)>', raw):
        txt = strip(m.group(1))
        if len(txt) < 12:
            continue
        if re.search(r'2026[-/年]\s*1[0-2]|(?:Oct|October)\s+\d{1,2}|\d{1,2}\s+(?:Oct|October)', txt):
            hits.append(txt)
    seen = set()
    for h in hits[:25]:
        k = h[:60]
        if k in seen:
            continue
        seen.add(k)
        print('   ', h[:170])
    if not hits:
        print('    (no Oct-2026 date strings found)')
