import json
d=json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
print('TOP KEYS:', list(d.keys()))
print('\nSAMPLE ITEM (newest):')
print(json.dumps(d['items'][0], ensure_ascii=False, indent=1)[:2200])
print('\nMETA KEYS:', list(d['meta'].keys()))
for k in ['generatedAt','itemCount','windowNote','asOf','digests']:
    v=d['meta'].get(k)
    print(f'  {k}:', (json.dumps(v,ensure_ascii=False)[:200] if not isinstance(v,(str,int)) else v))
