import json
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json', encoding='utf-8'))
for kw in ['Mox', 'Home Cushion', 'bolttech', 'Igloo', 'Atradius', 'Donaldson', 'AIF', 'Kerry Hotel', 'IAIS']:
    hits = [it for it in d['items'] if kw.lower() in (it['title']['sc'] + it.get('summary', {}).get('sc', '')).lower()]
    print('%-14s %d %s' % (kw, len(hits), [h['publishedAt'][:10] for h in hits[:5]]))
try:
    import zhconv
    print('zhconv OK', zhconv.convert('保险业监管局', 'zh-hant'))
except Exception as e:
    print('zhconv FAIL', e)
