import json
d = json.load(open('data/live-items.json'))
kws = ['sandbox', 'sandbox++', 'genai', 'generative', 'esun', 'eSun', 'cuhk', 'gleneagles', '養和', '养和', 'moneyhero', 'critical illness comparison', '危疾比較', '危疾比较', 'AI cohort']
for it in d['items']:
    blob = json.dumps(it, ensure_ascii=False).lower()
    for k in kws:
        if k.lower() in blob:
            print(f"{it['id']} | {it['publishedAt']} | {k}")
            break
print('---- ids containing 202610 ----')
for it in d['items']:
    if '202610' in it['id'] or it['publishedAt'].startswith('2026-10'):
        print(' ', it['id'], it['publishedAt'])
