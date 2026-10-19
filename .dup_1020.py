import json
live = json.load(open('data/live-items.json'))
kw = ['sidecar', 'Sidecar', '長城', '长城', 'Great Wall', 'FWD', '富衛', '富卫', '危疾', 'annuity', '年金']
seen = {}
for it in live['items']:
    blob = json.dumps(it, ensure_ascii=False)
    for k in kw:
        if k in blob:
            print(it['id'], '|', it['publishedAt'][:16], '|', it['title']['sc'][:80])
            break
