# -*- coding: utf-8 -*-
import json, re
live = json.load(open('data/live-items.json', encoding='utf-8'))['items']
for t in ['Half-Yearly', 'Half Yearly', '金融稳定', '金融穩定', 'Monetary and Financial']:
    hits = [(it.get('id'), it.get('publishedAt')) for it in live if t.lower() in json.dumps(it, ensure_ascii=False).lower()]
    print(f'{t}: {len(hits)}')
    for h in hits[:4]:
        print('   ', h)
print()
raw = json.load(open('data/_raw_1004_2108.json', encoding='utf-8'))
txt = raw['hkma_press']['text']
i = txt.find('Half-Yearly Monetary')
print('HKMA context:', re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', txt[i-400:i+200])))
print()
print('=== scmp insurance topic headlines ===')
st = raw['scmp_insurance']['text']
for m in list(re.finditer(r'"headline":"([^"]{15,120})"', st))[:15]:
    print(m.group(1))
for m in list(re.finditer(r'<a[^>]{0,200}>(?:<[^>]+>)*([^<>]{20,110})</', st))[:15]:
    s = m.group(1).strip()
    if s and not s.startswith('{'):
        print('A:', s)
