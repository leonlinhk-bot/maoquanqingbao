import json
d = json.load(open('data/live-items.json'))
ids = [it['id'] for it in d['items']]
print('total', len(ids))
kw = ['irdai', 'prudential', 'japan', 'munich', 'manulife', 'chubb', 'moneyhero', 'generali',
      'fsa', 'suspend', 'fullcapacity', 'full-capacity', '2026100', '2026-10-04', '20261004']
for k in kw:
    hits = [i for i in ids if k in i.lower()]
    print(f'[{k}] {len(hits)}')
    for h in hits[:12]:
        print('    ', h)
