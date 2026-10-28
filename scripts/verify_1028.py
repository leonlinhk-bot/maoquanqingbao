import json, collections
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
its = d['items']
print('total', len(its), '| meta', d['meta']['itemCount'], '| generatedAt', d['meta']['generatedAt'])
urls = collections.Counter(i['originalUrl'].rstrip('/') for i in its)
ids = collections.Counter(i['id'] for i in its)
print('dup urls:', [u for u, c in urls.items() if c > 1][:5])
print('dup ids:', [u for u, c in ids.items() if c > 1][:5])
print('\n--- today/this-batch entries ---')
for i in its[:7]:
    req = ['id','title','summary','why','tags','actions','rolesImpact','source','boards','themes','originalUrl','publishedAt','sourceTier','score','contentKind','verifyStatus','lang','summaryShort']
    missing = [k for k in req if k not in i]
    tc_missing = [k for k in ('sc','tc') if k not in i.get('title', {}) or k not in i.get('summary', {})]
    print(f"{i['publishedAt']} | {i['sourceKey']:16s} | {i['sourceTier']:6s} | {i['score']} | {i['boards']} | {len(i['summary']['sc'])}字摘要 | missing={missing}{tc_missing}")
    print('    ', i['title']['sc'])
print('\nfeed/all items:', len(json.load(open('/Users/leonliang/maoquanqingbao/feed/all.json'))['items']))
print('date counts:', collections.Counter(i['publishedAt'][:10] for i in its).most_common(3))
