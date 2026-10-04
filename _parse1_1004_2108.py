# -*- coding: utf-8 -*-
import json, re, datetime

raw = json.load(open('data/_raw_1004_2108.json', encoding='utf-8'))

LAST = '2026-10-04T18:13:00+08:00'
print('=== insuranceasianews_api (WP JSON) ===')
try:
    posts = json.loads(raw['insuranceasianews_api']['text'])
    for p in posts[:20]:
        print(p.get('date'), '|', p.get('title', {}).get('rendered', '')[:80])
except Exception as e:
    print('ERR', e)

print()
print('=== insuranceasia_rss items ===')
txt = raw['insuranceasia_rss']['text']
for m in re.finditer(r'<item>(.*?)</item>', txt, re.S):
    blk = m.group(1)
    t = re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', blk, re.S)
    pd = re.search(r'<pubDate>(.*?)</pubDate>', blk, re.S)
    ln = re.search(r'<link>(.*?)</link>', blk, re.S)
    print((pd.group(1).strip() if pd else '?'), '|', (t.group(1).strip()[:70] if t else '?'))

print()
print('=== artemis headlines ===')
txt = raw['artemis']['text']
for m in re.finditer(r'<h[23][^>]*>\s*<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', txt, re.S)[:0] if False else []:
    pass
arts = re.findall(r'class="[^"]*entry-title[^"]*"[^>]*>\s*<a[^>]*>(.*?)</a>', txt, re.S)
for a in arts[:15]:
    print(re.sub(r'<[^>]+>', '', a).strip()[:80])
