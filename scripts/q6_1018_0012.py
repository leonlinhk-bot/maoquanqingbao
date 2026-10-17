import json
from collections import Counter
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json', encoding='utf-8'))
for key in ['insuranceasia', 'insurancebusinessmag', 'insuranceasianews', 'ia', 'reinsurancenews', 'artemis']:
    tiers = Counter(it.get('sourceTier') for it in d['items'] if it['sourceKey'] == key)
    sample = next((it for it in d['items'] if it['sourceKey'] == key), None)
    print(key, dict(tiers), 'score', sample.get('score') if sample else None)
    if sample:
        print('   boards', sample.get('boards'), 'themes', sample.get('themes'))
        print('   source', json.dumps(sample.get('source'), ensure_ascii=False))
