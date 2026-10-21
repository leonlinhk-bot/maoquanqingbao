import json, re
D = '/Users/leonliang/maoquanqingbao/data/_1022_0037'
data = json.load(open(D + '/ian.json'))
want = ['Gallagher Re', 'AUB Group', 'BESS', 'climate action', 'IndusInd']
for it in data:
    t = re.sub(r'<[^>]+>', ' ', it['title']['rendered'])
    if any(w.lower() in t.lower() for w in want):
        print('##', it['date'], '|', t)
        print('   ', re.sub(r'<[^>]+>', '', it['excerpt']['rendered']).replace('\n', ' ').strip()[:500])
        print('   ', it['link'])
        print()
