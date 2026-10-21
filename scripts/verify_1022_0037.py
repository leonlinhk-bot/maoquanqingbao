import json, datetime
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json', encoding='utf-8'))
items = d['items']
new = [it for it in items if (it.get('ingestedAt') or '') >= '2026-10-22T00:3']
print('new count:', len(new))
req = ['id','publishedAt','originalUrl','sourceKey','sourceTier','score','verifyStatus','contentKind',
       'clusterCount','boards','themes','title','summary','why','source','tags','actions','rolesImpact','ingestedAt']
ok = True
for it in new:
    miss = [k for k in req if k not in it]
    if miss:
        ok = False
        print('MISSING', it['id'], miss)
    if len(it['boards']) != 1:
        print('BOARDS!=1', it['id'], it['boards'])
    if len(it['themes']) < 2:
        print('THEMES<2', it['id'], it['themes'])
    sl = len(it['summary']['sc'])
    print(f"{it['id'][:46]:48s} score={it['score']} tier={it['sourceTier']:7s} sum={sl:3d} "
          f"pub={it['publishedAt'][:16]} {it['verifyStatus']}")
    if not (45 <= sl <= 120):
        print('   !! summary length out of range', sl)
# dup check
urls = [it['originalUrl'] for it in items]
dups = {u for u in urls if urls.count(u) > 1}
print('dup urls:', dups)
ids = [it['id'] for it in items]
dupids = {u for u in ids if ids.count(u) > 1}
print('dup ids:', dupids)
print('meta itemCount:', d['meta']['itemCount'], '| len:', len(items), '| generatedAt:', d['meta']['generatedAt'])
print('schema ok:', ok)
# ordering
bad = [items[i]['id'] for i in range(len(items)-1) if (items[i].get('publishedAt') or '') < (items[i+1].get('publishedAt') or '')]
print('ordering violations:', len(bad), bad[:5])
