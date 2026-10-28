#!/usr/bin/env python3
"""检查各保司 newsroom 最新条目日期。"""
import os, re, html

D = os.path.expanduser('~/maoquanqingbao/.cache1029_0030/ins')


def txt(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S | re.I)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S | re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()


PATS = [r'2026[-/年]1?\d[-/月]\d{1,2}', r'\d{1,2} (?:Oct|October) 2026', r'(?:Oct|October) \d{1,2}, 2026']
for name in ('aia', 'prudential', 'axa', 'sunlife', 'nfra'):
    p = f'{D}/{name}.html'
    if not os.path.exists(p):
        print(name, 'MISSING'); continue
    raw = open(p, encoding='utf-8', errors='replace').read()
    print('=' * 60)
    print(name, len(raw))
    hits = []
    for pat in PATS:
        for m in re.finditer(pat, raw):
            s = max(0, m.start() - 100)
            ctx = txt(raw[s:m.end() + 200])
            hits.append((m.group(0), ctx[-190:]))
    seen = set()
    for d, c in hits:
        if d in seen:
            continue
        seen.add(d)
        print(f'  {d:14} | {c[:150]}')
