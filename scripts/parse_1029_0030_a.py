#!/usr/bin/env python3
"""解析 1029_0030 缓存，列出各源最新条目（标题/日期/链接），供人工挑选。"""
import os, re, html, json

D = os.path.expanduser('~/maoquanqingbao/.cache1029_0030')


def clean(s):
    s = re.sub(r'<[^>]+>', ' ', s or '')
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()


def rss_items(path, limit=25):
    t = open(path, encoding='utf-8', errors='replace').read()
    items = re.findall(r'<item[ >].*?</item>', t, re.S)
    if not items:
        items = re.findall(r'<entry[ >].*?</entry>', t, re.S)
    out = []
    for it in items[:limit]:
        m = re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', it, re.S)
        title = clean(m.group(1)) if m else ''
        lm = re.search(r'<link[^>]*href="([^"]+)"', it) or re.search(r'<link>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</link>', it, re.S)
        link = clean(lm.group(1)) if lm else ''
        dm = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S) or re.search(r'<published>(.*?)</published>', it, re.S) or re.search(r'<updated>(.*?)</updated>', it, re.S)
        date = clean(dm.group(1)) if dm else ''
        out.append((date, title, link))
    return out


def report_rss(name, path, limit=20, kw=None):
    print('=' * 70)
    print(name, path)
    if not os.path.exists(path):
        print('  MISSING'); return
    rows = rss_items(path, limit)
    print('  items parsed:', len(rows))
    for date, title, link in rows:
        if kw and not any(k in title for k in kw):
            continue
        print(f'  {date[:31]:32} | {title[:78]}')
        print(f'      {link[:130]}')


def report_html(name, path, patterns, limit=25):
    print('=' * 70)
    print(name, path)
    if not os.path.exists(path):
        print('  MISSING'); return
    t = open(path, encoding='utf-8', errors='replace').read()
    hits = []
    for pat in patterns:
        hits += re.findall(pat, t, re.S)
    seen = set()
    for h in hits:
        if isinstance(h, tuple):
            h = ' | '.join(clean(x) for x in h)
        h = clean(h)
        if not h or h in seen:
            continue
        seen.add(h)
        print('  ', h[:200])
        if len(seen) >= limit:
            break


# 1) govhk zh RSS
KWHK = ['保险', '保險', '保監', '金融', '財經', '強積金', '年金', '退休', '證監', '金管局', '家族辦公室', '資產管理', '跨境', '人民幣', '銀髮', '保險業']
report_rss('GOVHK zh', f'{D}/govhk_zh.raw', 400, KWHK)

# 2) InsuranceAsia News HK feed
report_rss('IAN HK', f'{D}/ian_hk.raw', 20)

# 3) Artemis
report_html('ARTEMIS', f'{D}/artemis.raw', [
    r'<h[23][^>]*>\s*<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>',
], 30)
