import json, collections
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json', encoding='utf-8'))
items = d['items']
s = d['meta']
print('total:', len(items), '| meta.itemCount:', s['itemCount'], '| generatedAt:', s['generatedAt'])

ids = [it['id'] for it in items]
dups = [k for k, v in collections.Counter(ids).items() if v > 1]
print('dup ids:', dups[:5] or 'none')

urls = [it.get('originalUrl', '').split('?')[0].rstrip('/') for it in items]
dupu = [k for k, v in collections.Counter(urls).items() if v > 1]
print('dup urls:', len(dupu), dupu[:3])

errs = []
for it in items[:11]:
    if not it.get('boards'): errs.append((it['id'], 'no boards'))
    if len(it.get('themes') or []) < 2: errs.append((it['id'], 'themes<2'))
    if not it.get('sourceTier'): errs.append((it['id'], 'no tier'))
    if not it.get('originalUrl'): errs.append((it['id'], 'no url'))
    if it['sourceTier'] == 'official' and it['score'] < 85: errs.append((it['id'], 'score<85 official'))
    if it['sourceTier'] == 'insurer' and it['score'] < 75: errs.append((it['id'], 'score<75 insurer'))
    if it['sourceTier'] == 'pro' and it['score'] < 70: errs.append((it['id'], 'score<70 pro'))
    if it['sourceTier'] == 'media' and it['score'] < 60: errs.append((it['id'], 'score<60 media'))
    for k in ('sc', 'tc'):
        if not isinstance(it['tags'].get(k), list): errs.append((it['id'], f'tags.{k} not list'))
        if not isinstance(it['summary'].get(k), str): errs.append((it['id'], f'summary.{k} missing'))
        if not isinstance(it['title'].get(k), str): errs.append((it['id'], f'title.{k} missing'))
    if not (50 <= len(it['summary']['sc']) <= 100): errs.append((it['id'], 'summary len ' + str(len(it['summary']['sc']))))
print('schema errors:', errs or 'none')

print('\n--- 新增11条 ---')
for it in items[:11]:
    print(f"{it['publishedAt']} | {it['sourceKey']:20s} | {it['score']} | {it['verifyStatus']:8s} | {it['title']['sc'][:44]}")
print('\n--- 今次覆盖的信源 ---', sorted({it['sourceKey'] for it in items[:11]}))
