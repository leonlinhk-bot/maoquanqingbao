# -*- coding: utf-8 -*-
import json, re

raw = json.load(open('data/_raw_1004_2108.json', encoding='utf-8'))

def strip(s):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', s)).strip()

print('=== HKMA press (dates near top) ===')
txt = raw['hkma_press']['text']
for m in re.finditer(r'(\d{2}\s+\w+\s+2026|2026-\d{2}-\d{2})', txt):
    pass
# HKMA typically lists "dd Mon 2026"
seen = []
for m in re.finditer(r'>([^<>]{10,120})</a>', txt):
    t = m.group(1).strip()
    if re.search(r'(insurance|Insur|HKMA|Authority|announce|launch|alert|Beware|warn)', t):
        seen.append(t)
print('\n'.join(seen[:20]))

print()
print('=== IBM Asia headlines ===')
txt = raw['ibm_asia']['text']
for m in re.finditer(r'<a[^>]*href="(/asia/news/[^"]+)"[^>]*>([^<]{15,120})</a>', txt):
    print(m.group(2).strip()[:90])
    if len(set()) > 0: pass

print()
print('=== govhk_zh item dates ===')
txt = raw['govhk_zh']['text']
for m in re.finditer(r'<item>(.*?)</item>', txt, re.S):
    blk = m.group(1)
    t = re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', blk, re.S)
    pd = re.search(r'<pubDate>(.*?)</pubDate>', blk, re.S)
    title = t.group(1).strip() if t else '?'
    if re.search(r'(保险|保險|強積金|积金|保監|保监局|金融|理财|退休)', title):
        print((pd.group(1).strip() if pd else '?'), '|', title[:70])

print()
print('=== NFRA headlines ===')
txt = raw['nfra']['text']
for m in re.finditer(r'<a[^>]*title="([^"]{8,90})"', txt):
    print(m.group(1)[:80])
