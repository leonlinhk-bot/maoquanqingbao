# -*- coding: utf-8 -*-
import json, re
raw = json.load(open('data/_raw_1004_2108.json', encoding='utf-8'))
st = raw['scmp_insurance']['text']
# find headline occurrences with nearby date + url
headlines = [
 'banks set golden week lures',
 'China bans online promos',
 'mainland China\u2019s insurers sitting on',
 'MPF accounts as offshore trusts',
 'Prudential, Manulife seal tech alliances',
]
for h in headlines:
    for m in re.finditer(re.escape(h), st):
        s = max(0, m.start()-1500); e = m.end()+400
        ctx = st[s:e]
        dates = re.findall(r'20\d\d-\d\d-\d\dT[\d:+.]+', ctx) + re.findall(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*\s+\d{1,2},\s*20\d\d', ctx)
        urls = re.findall(r'https?://www\.scmp\.com/[^\s"\\]+', ctx)
        print('###', h)
        print('   dates:', sorted(set(dates))[-4:])
        print('   urls:', sorted(set(urls))[:3])
        break
print()
live = json.load(open('data/live-items.json', encoding='utf-8'))['items']
for t in ['prudential', 'manulife']:
    hits = [it.get('id') for it in live if t in json.dumps(it, ensure_ascii=False).lower()]
    print(t, 'items in DB:', len(hits), hits[:8])
