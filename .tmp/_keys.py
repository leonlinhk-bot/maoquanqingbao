import json
d = json.load(open('data/live-items.json'))
keys = set()
for it in d['items']:
    keys.add(it['id'])
    if 'sourceKey' in it:
        keys.add(it['sourceKey'])
# also gather originalUrl
urls = set()
for it in d['items']:
    if it.get('originalUrl'):
        urls.add(it['originalUrl'])
print('total keys:', len(keys))
print('total urls:', len(urls))
# print last 5 days item ids for reference
import datetime
for it in d['items'][:40]:
    print(it['id'], '|', it.get('sourceKey',''), '|', it.get('originalUrl','')[:80])
