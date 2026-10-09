import json, os
p = 'data/_raw_1009_1808/_fresh.json'
d = json.load(open(p))
print(type(d))
if isinstance(d, dict):
    print('keys:', list(d.keys())[:20])
    for k, v in list(d.items())[:5]:
        print('--', k, type(v), (len(v) if hasattr(v, '__len__') else ''))
        print(json.dumps(v, ensure_ascii=False)[:1500])
elif isinstance(d, list):
    print('len', len(d))
    for x in d[:10]:
        print(json.dumps(x, ensure_ascii=False)[:400])
