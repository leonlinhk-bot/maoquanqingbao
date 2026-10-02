import json
d = json.load(open('data/live-items.json'))
items = d['items']
kws = ['Conduct in Focus', 'FWD', 'AML', '洗錢', '洗钱', 'Beazley', 'Zurich', '蘇黎世', '蘇黎世', '五年規劃', '五年规划', 'Labuan', '納閩', '納閩', 'CPIC', '太保', 'facultative', '臨分', '临分', 'Hannover', 'Willis', '威達信', '威达信', 'Hanwha', '韓華', '韩华', 'broadcast', 'Thailand', '泰國', '泰国', 'Gallagher', 'Aon', 'Budget', 'Income Insurance', '單元信託', '单位信托']
for k in kws:
    hits = [it['id'] for it in items if k.lower() in json.dumps(it, ensure_ascii=False).lower()]
    print(f'{k}: {len(hits)} -> {hits[:6]}')
