import json
d = json.load(open('data/live-items.json'))
items = d['items']
kws = ['保险法', '保險法', '负面清单', '負面清單', '修订草案', '征求意见截止', '人身保险产品', 'Hannover Re Capital', 'Plenum', 'casualty ILS', 'Insurance-linked', 'ILS', 'cyclone pool', 'Hormuz', '霍爾木茲', '霍尔木兹', 'Albany', 'Gotting', 'Acuon', 'Suncorp', 'HKIC', 'wealthy class']
for k in kws:
    hits = [it['id'] for it in items if k.lower() in json.dumps(it, ensure_ascii=False).lower()]
    print(f'{k}: {len(hits)} -> {hits[:8]}')
