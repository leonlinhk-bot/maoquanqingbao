# -*- coding: utf-8 -*-
import json, re

raw = json.load(open('data/_raw_1004_2108.json', encoding='utf-8'))
live = json.load(open('data/live-items.json', encoding='utf-8'))['items']
existing_ids = {it.get('id', '') for it in live}
alltext = json.dumps(live, ensure_ascii=False)

def has(s):
    return s.lower() in alltext.lower()

cands = [
    ('IBM', 'Insurance moves: Allianz, AIA Life, Aon, Coface'),
    ('IBM', 'South Korea flags mis-selling gap in broadcast insurance sales'),
    ('IBM', 'Zurich completes Beazley deal as Adrian Cox steps down as CEO'),
    ('IBM', 'Allianz names new CEOs at Allianz Partners and Allianz Direct'),
    ('IAN', 'IRDAI reform push needs a finer touch'),
]
for tag, c in cands:
    print('DUP' if has(c[:30]) else 'NEW', '|', tag, '|', c)

print()
print('=== IBM Asia: extract dates around headlines ===')
txt = raw['ibm_asia']['text']
# find each headline with nearby date
for m in re.finditer(r'(Insurance moves: Allianz[^<]*|South Korea flags[^<]*|Zurich completes Beazley[^<]*|Allianz names new CEOs[^<]*)', txt):
    s = max(0, m.start()-600)
    ctx = txt[s:m.end()+200]
    dates = re.findall(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2},\s*2026', ctx)
    print(m.group(1)[:60], '=>', dates)
