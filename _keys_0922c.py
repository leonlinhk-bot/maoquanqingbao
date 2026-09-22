import json
d=json.load(open('data/live-items.json'))
keys=set()
for it in d['items']:
    keys.add(it.get('id',''))
    keys.add(it.get('sourceKey',''))
    keys.add(it.get('originalUrl',''))
open('.tmp/0922-1808/existing.txt','w').write('\n'.join(sorted(k for k in keys if k)))
import re
# print any containing 0909 or recent markers
print(len(keys))
for k in sorted(keys):
    if '20260921' in k or '20260922' in k:
        print(k)
