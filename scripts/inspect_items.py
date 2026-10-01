import json, sys, os
os.chdir('/Users/leonliang/maoquanqingbao')
d = json.load(open('data/live-items.json'))
print('meta:', json.dumps(d.get('meta', {}), ensure_ascii=False)[:600])
print('total items:', len(d['items']))
for it in d['items'][:10]:
    print('---')
    print(it.get('id'), '|', it.get('publishedAt'), '|', it.get('sourceKey'), '|', it.get('score'), it.get('verifyStatus'))
    print('   ', it['title']['sc'][:80])
