import json
d = json.load(open('data/live-items.json'))
items = d['items']
ls = [len(it['summary']['sc']) for it in items[:60] if it.get('summary')]
print('recent60 summary lens: min', min(ls), 'max', max(ls), 'avg', sum(ls)//len(ls))
ls2 = [len(it.get('summaryShort', {}).get('sc', '')) for it in items[:60] if it.get('summaryShort')]
print('recent60 short len: min', min(ls2), 'max', max(ls2), 'avg', sum(ls2)//len(ls2))
