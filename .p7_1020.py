import json
live = json.load(open('data/live-items.json'))
seen = set()
for it in live['items']:
    k = it.get('sourceKey')
    if k in ('reinsurancenews', 'artemis', 'insuranceasianews') and k not in seen:
        seen.add(k)
        print(k, '|', it.get('sourceTier'), '|', it.get('score'), '|', it.get('contentKind'), '|', it.get('boards'), '|', it.get('themes'))
# sample rolesImpact / actions structure
s = live['items'][0]
print(json.dumps({k: s[k] for k in ('actions', 'rolesImpact', 'tags', 'why', 'source', 'clusterCount', 'verifyStatus')}, ensure_ascii=False, indent=1))
