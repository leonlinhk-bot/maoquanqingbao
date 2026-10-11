import json
d=json.load(open('data/live-items.json'))
for it in d['items']:
    if it.get('sourceKey') in ('insuranceasianews','insurtech','manulife'):
        print(json.dumps({k:it[k] for k in ('id','sourceKey','sourceTier','contentKind','publishedAt','score','verifyStatus','boards','themes','source')}, ensure_ascii=False))
        if it['sourceKey']=='insuranceasianews': break
print('---- one insurtech ----')
for it in d['items']:
    if it.get('sourceKey') in ('insurtech','fintechglobal'):
        print(json.dumps({k:it[k] for k in ('id','sourceKey','sourceTier','contentKind','publishedAt','score','boards','themes','source')}, ensure_ascii=False))
print('---- one manulife ----')
for it in d['items']:
    if it.get('sourceKey')=='manulife':
        print(json.dumps({k:it[k] for k in ('id','sourceKey','sourceTier','contentKind','publishedAt','score','boards','themes','source')}, ensure_ascii=False))
