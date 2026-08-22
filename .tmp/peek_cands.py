import json
d = json.load(open('.tmp/cands.json'))
print(type(d).__name__, len(d) if hasattr(d, '__len__') else '')
if isinstance(d, dict):
    for k, v in list(d.items())[:12]:
        print(k, '->', str(v)[:220])
elif isinstance(d, list):
    for v in d[:12]:
        print(str(v)[:220])
