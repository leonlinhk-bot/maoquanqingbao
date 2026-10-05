import json, collections
d = json.load(open('data/live-items.json'))
c = collections.defaultdict(collections.Counter)
for x in d['items']:
    c[x.get('sourceKey')][x.get('sourceTier')] += 1
for k in ['insuranceasia', 'insuranceasianews', 'insurancebusinessmag', 'artemis', 'hkma', 'scmp', 'govhk', 'nfra', 'ia', 'prudential', 'manulife', 'reinasia', 'family_office', 'insurtech', 'asiainsurancereview']:
    print(k, dict(c.get(k, {})))
print('--- sample item keys ---')
print(sorted(d['items'][0].keys()))
print('--- a pro-tier sample (insuranceasia) ---')
for x in d['items']:
    if x.get('sourceKey') == 'insuranceasia':
        print(json.dumps({k: x[k] for k in ('id', 'score', 'sourceTier', 'score', 'contentKind', 'boards', 'themes')}, ensure_ascii=False))
        break
print('--- hot/featured check ---')
print('hot count', len(d.get('hot', [])))
print('featured items', sum(1 for x in d['items'] if x.get('featured')))
print('evergreen flag sample', [x.get('evergreen') for x in d['items'][:5]])
