import json,collections
d=json.load(open('data/live-items.json'))
items=d['items']
th=collections.Counter();bd=collections.Counter();ck=collections.Counter();st=collections.Counter()
for it in items:
    for t in it.get('themes',[]) or []: th[t]+=1
    for b in it.get('boards',[]) or []: bd[b]+=1
    ck[it.get('contentKind')]+=1
    st[it.get('sourceTier')]+=1
print('THEMES:',th.most_common(60))
print('BOARDS:',bd.most_common())
print('KIND:',ck.most_common())
print('TIER:',st.most_common())
