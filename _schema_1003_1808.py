import json
d = json.load(open('data/live-items.json'))
print(json.dumps(d['items'][0], ensure_ascii=False, indent=1))
print('--- meta keys ---')
for k, v in d['meta'].items():
    s = json.dumps(v, ensure_ascii=False)
    print(k, '=>', s[:200])
print('--- boards keys ---')
print(json.dumps(d['boards'], ensure_ascii=False)[:400])
print('--- stats ---')
print(json.dumps(d['stats'], ensure_ascii=False)[:600])
print('--- feedFacets ---')
print(json.dumps(d['feedFacets'], ensure_ascii=False)[:400])
