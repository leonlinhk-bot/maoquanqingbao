import json, re
j = json.load(open('.cache1020_0033/ian.json'))
for p in j[:8]:
    print(p['date'], '|', re.sub(r'<[^>]+>', '', p['title']['rendered'])[:90])
    print('   ', p['link'])
