import json, collections
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
c = collections.Counter(i['originalUrl'].rstrip('/') for i in d['items'])
dups = {u: n for u, n in c.items() if n > 1}
print('dup url groups:', len(dups), '| extra entries:', sum(n - 1 for n in dups.values()))
