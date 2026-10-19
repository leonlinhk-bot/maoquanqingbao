import json
d = json.load(open('data/live-items.json'))
print('meta.itemCount', d['meta']['itemCount'], 'generatedAt', d['meta']['generatedAt'], 'len', len(d['items']))
for it in d['items'][:6]:
    print('==', it['id'])
    print('  title.sc:', it['title']['sc'])
    print('  title.tc:', it['title']['tc'])
    print('  summary.sc:', it['summary']['sc'][:80])
    print('  tags.sc:', it['tags']['sc'], '| tags.tc:', it['tags']['tc'])
    print('  boards', it['boards'], 'themes', it['themes'], 'kind', it['contentKind'], 'url', it['originalUrl'][:70])
# schema check across all
req = ['id','publishedAt','originalUrl','sourceKey','sourceTier','score','verifyStatus','contentKind','clusterCount','boards','themes','title','summary','why','actions','rolesImpact','tags','source']
bad = 0
for it in d['items']:
    miss = [k for k in req if k not in it]
    if miss:
        bad += 1
        if bad < 5: print('MISSING', it.get('id'), miss)
print('items missing required fields:', bad)
