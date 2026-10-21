import json, urllib.request, time

base = 'https://hkmaoquanqingbao.com'
for attempt in range(3):
    try:
        core = json.load(urllib.request.urlopen(base + '/data/core.json?t=' + str(int(time.time())), timeout=30))
        items = json.load(urllib.request.urlopen(base + '/data/items.json?t=' + str(int(time.time())), timeout=30))
        break
    except Exception as e:
        print('retry', e)
        time.sleep(10)

print('live core items:', len(core['items']), '| items.json:', len(items['items']), '| itemCount:', items.get('itemCount'))
print('core top3:')
for it in core['items'][:3]:
    print('  ', it.get('publishedAt'), '|', it.get('title', {}).get('sc', '')[:60])
idx = {i['id']: i for i in items['items']}
for k in ['ia-enforcement-jian-yongqin-suspension-20261016',
          'reinsurancenews-meta-muse-ai-claims-risk-20261020',
          'artemis-arbol-datacenter-moratorium-parametric-20261020']:
    it = idx.get(k)
    print('FOUND' if it else 'MISSING', k, '|', (it or {}).get('title', {}).get('sc', '')[:50])
