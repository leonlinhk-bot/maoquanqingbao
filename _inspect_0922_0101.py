import json
p='data/live-items.json'
d=json.load(open(p))
items=d['items']
print('total',len(items))
for it in items[:25]:
    print(it.get('publishedAt'),'|',it.get('sourceKey'),'|',it.get('sourceTier'),'|',it.get('title',{}).get('sc','')[:60])
print('---keys---')
ks={}
for it in items[:200]:
    k=it.get('sourceKey')
    ks[k]=ks.get(k,0)+1
print(ks)
