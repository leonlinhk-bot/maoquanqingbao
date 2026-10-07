import json
d=json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
it=d['items'][0]
print('ITEM KEYS:', list(it.keys()))
for k in ['id','score','verifyStatus','sourceTier','sourceKey','contentKind','publishedAt','effectiveAt','originalUrl','source','clusterCount','featured']:
    print(f'  {k}:', json.dumps(it.get(k), ensure_ascii=False)[:260])
print('\ntitle:', json.dumps(it.get('title'), ensure_ascii=False))
print('summary:', json.dumps(it.get('summary'), ensure_ascii=False))
print('why:', json.dumps(it.get('why'), ensure_ascii=False))
print('\nmeta.generatedAt:', d['meta'].get('generatedAt'))
print('meta.itemCount:', d['meta'].get('itemCount'))
print('meta.windowNote:', json.dumps(d['meta'].get('windowNote'), ensure_ascii=False))
print('boards sample:', json.dumps(d.get('boards'), ensure_ascii=False)[:300])
