import json
j = json.load(open('.cache1020_0033/ian.json'))
for p in j[:4]:
    print(p['date'], '|', p.get('date_gmt'), '|', p['modified'], '|', p.get('modified_gmt'))
