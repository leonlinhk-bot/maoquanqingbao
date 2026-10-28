import json
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
recent = [i for i in d['items'][7:40]]
ls = [len(i.get('summary', {}).get('sc', '')) for i in recent]
print('prev 33 items summary len: min', min(ls), 'max', max(ls), 'avg', sum(ls) // len(ls))
