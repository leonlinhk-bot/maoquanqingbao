import json
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = d['items']
print(json.dumps(items[0], ensure_ascii=False, indent=1))
print('\n=== meta keys ===')
print(list(d.keys()), list(d['meta'].keys()))
print(json.dumps({k: v for k, v in d['meta'].items() if k not in ('sourcesPrimary','sourceTiers')}, ensure_ascii=False, indent=1)[:1200])
print('\n=== another sample (insuranceasianews skuld-like) ===')
for it in items[:60]:
    if it.get('sourceKey') == 'insuranceasianews':
        print(json.dumps(it, ensure_ascii=False, indent=1))
        break
