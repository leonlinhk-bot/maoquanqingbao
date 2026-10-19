import json
live = json.load(open('data/live-items.json'))
checks = ['Australia', 'Penang', 'Tysers', 'Saha', 'Marsh', 'DOXA', 'Howden', 'SRCC', 'riot', 'France', 'Hannover']
for k in checks:
    hits = [it for it in live['items'] if k.lower() in json.dumps(it, ensure_ascii=False).lower()]
    print('##', k, len(hits))
    for it in hits[:4]:
        print('   ', it['id'], it['publishedAt'][:16], it['title']['sc'][:70])
