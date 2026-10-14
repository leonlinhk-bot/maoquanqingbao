#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parse HTML newsroom / regulator pages fetched for 1015 run."""
import os, re, json, html
from datetime import datetime, timezone, timedelta

HKT = timezone(timedelta(hours=8))
DIR = '/Users/leonliang/maoquanqingbao/data/_1015'


def strip_html(s):
    s = re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>', '', s or '')
    s = re.sub(r'(?s)<[^>]+>', ' ', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()


def show(path, label, datepat, limit=25):
    print(f'\n########## {label} ##########')
    p = os.path.join(DIR, path)
    if not os.path.exists(p):
        print('  MISSING'); return
    raw = open(p, encoding='utf-8').read()
    print('  bytes:', len(raw))
    hits = []
    for m in re.finditer(r'href="([^"]+)"', raw):
        u = m.group(1)
        if u.startswith('#') or u.startswith('mailto'):
            continue
        ctx = strip_html(raw[max(0, m.start() - 300): m.start() + 700])
        for dm in re.finditer(datepat, ctx):
            hits.append((dm.group(0), u, ctx[:260]))
            break
    seen = set()
    n = 0
    for d, u, ctx in hits:
        key = u.rstrip('/')
        if key in seen:
            continue
        seen.add(key)
        n += 1
        if n > limit:
            break
        print(f'  [{d}] {u[:120]}')
        print(f'      {ctx[:200]}')
    print('  total unique hrefs w/ date:', len(seen))


D_MDY = r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+2026'
D_DMY = r'\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+2026'
D_ISO = r'2026-\d{2}-\d{2}'
D_CN = r'2026年\d{1,2}月\d{1,2}日'
D_SLASH = r'2026/\d{2}/\d{2}'

show('hkma_press.raw', 'HKMA press releases', D_DMY + '|' + D_MDY + '|' + D_ISO)
show('aia_pr.raw', 'AIA press releases', D_DMY + '|' + D_CN + '|' + D_ISO)
show('prudential_nr.raw', 'Prudential newsroom', D_DMY + '|' + D_MDY + '|' + D_ISO)
show('axa_nr.raw', 'AXA news room', D_DMY + '|' + D_ISO + '|' + D_CN)
show('sunlife_nr.raw', 'Sun Life newsroom', D_DMY + '|' + D_MDY + '|' + D_ISO)
show('fstb_idx.raw', 'FSTB index', D_DMY + '|' + D_ISO)

print('\n########## NFRA dynamics JSON ##########')
try:
    j = json.load(open(os.path.join(DIR, 'nfra_dyn.raw'), encoding='utf-8'))
    rows = j if isinstance(j, list) else j.get('data', {}).get('results') or j.get('results') or []
    print('  rows:', len(rows))
    for r in rows[:12]:
        print('  ', json.dumps({k: r.get(k) for k in ('title', 'publishDate', 'pubDate', 'url', 'docUrl', 'itemId') if k in r}, ensure_ascii=False)[:260])
    if not rows:
        print(json.dumps(j, ensure_ascii=False)[:600])
except Exception as e:
    print('  ERR', e)
