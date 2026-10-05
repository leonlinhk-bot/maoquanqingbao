import json
d = json.load(open('data/live-items.json'))
ids = set()
pairs = set()
for x in d['items']:
    ids.add(x.get('id'))
    t = (x.get('title') or {}).get('sc', '')
    pairs.add((x.get('sourceKey', ''), t[:60]))
json.dump({'ids': sorted(ids), 'pairs': sorted('|'.join(p) for p in pairs)}, open('.tmp/dbids_1006.json', 'w'), ensure_ascii=False)
print('ids', len(ids))
# print ids containing key tokens for manual dedupe
for tok in ['20261005', '20261006', '20261004', 'artemis', 'insuranceasia', 'ibm-', 'ian-', 'hkma-', 'scmp-', 'nfra']:
    hits = [i for i in ids if tok in i]
    print('---', tok, len(hits))
    for h in sorted(hits)[-14:]:
        print('   ', h)
