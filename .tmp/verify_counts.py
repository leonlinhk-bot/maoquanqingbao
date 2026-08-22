import json

live = json.load(open('data/live-items.json'))
txt = open('app.js').read()
app = json.loads(txt.split('window.HKII_DATA = ')[1].split(';')[0])
print("live items:", len(live['items']))
print("app items:", len(app['items']))
print("meta.generatedAt:", live['meta']['generatedAt'])
print("meta.itemCount:", live['meta']['itemCount'])
print("windowNote:", live['meta']['windowNote'])
print("top5 ids:", [it['id'] for it in live['items'][:5]])
