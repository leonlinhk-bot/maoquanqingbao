#!/usr/bin/env python3
import re, os, glob, html

OUT = '/Users/leonliang/maoquanqingbao/data/_raw_1025_0044'
UA = None

def text(p):
    b = open(p, 'rb').read().decode('utf-8', 'ignore')
    b = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', b, flags=re.S | re.I)
    t = re.sub(r'<[^>]+>', '\n', b)
    t = html.unescape(t)
    lines = [re.sub(r'\s+', ' ', x).strip() for x in t.split('\n')]
    return b, [x for x in lines if x]

def show(key, pats, ctx=0):
    g = glob.glob(os.path.join(OUT, key + '_*.html'))
    if not g:
        print(f'== {key}: MISSING'); return
    raw, lines = text(g[0])
    print(f'\n===== {key}  ({len(lines)} lines)')
    hits = 0
    for i, ln in enumerate(lines):
        if any(re.search(p, ln) for p in pats):
            print(f'  [{i}] {ln[:190]}')
            hits += 1
            if hits > 45: break
    if not hits:
        print('  (no date hits) first 40 lines:')
        for ln in lines[:40]:
            print('   ', ln[:150])

show('hkma_press', [r'2026-10-2[45]', r'2[45] October 2026', r'2026102[45]'])
show('aia', [r'2026[-/年]?10[-/月]?2[45]', r'2026年10月2[45]'])
show('prudential', [r'2026[-/年]?10[-/月]?2[45]', r'2[45] Oct'])
show('axa', [r'2026[-/年]?10[-/月]?2[45]', r'2[45] Oct'])
show('sunlife', [r'2026[-/年]?10[-/月]?2[45]', r'2[45] Oct'])
show('nfra_list', [r'2026'], 0)
