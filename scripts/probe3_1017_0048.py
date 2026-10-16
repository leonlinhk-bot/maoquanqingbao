#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, re, html
D = '/Users/leonliang/maoquanqingbao/data/_1017_0048/'
def strip(t):
    t = re.sub(r'<[^>]+>', ' ', t or '')
    return html.unescape(re.sub(r'\s+', ' ', t)).strip()

# --- govhk: insurance/finance/MPF related in window ---
KW = ['保險', '保監', '強積金', '積金局', '退休', '年金', '財經', '金融', '投資', '債券', '證券', '虛擬資產',
      '風險', '保險業', '再保險', '專屬自保', '家族辦公室', '資產管理', '跨境', '大灣區', '稅務', '信託']
raw = open(D + 'govhk.out', encoding='utf-8', errors='replace').read()
items = re.findall(r'<item[\s>].*?</item>', raw, re.S)
print('GOVHK items', len(items))
for e in items:
    ti = re.search(r'<title[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', e, re.S)
    li = re.search(r'<link[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</link>', e, re.S)
    pu = re.search(r'<pubDate[^>]*>(.*?)</', e, re.S)
    de = re.search(r'<description[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</description>', e, re.S)
    t = strip(ti.group(1)) if ti else ''
    d = strip(de.group(1)) if de else ''
    hit = [k for k in KW if k in t + d[:300]]
    if hit:
        print(' HIT', strip(pu.group(1)) if pu else '', '|', t[:80], '|', hit[:4])
        print('     ', strip(li.group(1)) if li else '')

for f in ['aia.out', 'prudential.out', 'axa.out', 'sunlife.out', 'nfra.out']:
    print('=====', f)
    r = open(D + f, encoding='utf-8', errors='replace').read()
    print(' len', len(r))
    txt = strip(r)
    for pat in [r'\d{1,2}\s+\w+\s+20\d{2}', r'20\d{2}-\d{2}-\d{2}', r'\d{2}/\d{2}/20\d{2}']:
        hits = re.findall(pat, txt)
        if hits:
            print('  datefmt', pat, hits[:12])
    links = re.findall(r'href="([^"]+)"[^>]*>([^<]{12,110})<', r)
    ins = [l for l in links if re.search(r'news|press|media|announce|updates', l[0], re.I)]
    for l in ins[:12]:
        print('  L', l[0][:110], '|', strip(l[1])[:90])
