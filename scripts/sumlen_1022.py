import json, statistics
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json', encoding='utf-8'))
lens = [len(it['summary']['sc']) for it in d['items'] if it.get('summary', {}).get('sc')]
print('n=', len(lens), 'median=', statistics.median(lens), 'mean=', round(statistics.mean(lens), 1))
print('p90=', sorted(lens)[int(len(lens)*0.9)], 'max=', max(lens))
print('share <=110:', round(sum(1 for l in lens if l <= 110) / len(lens) * 100, 1), '%')
