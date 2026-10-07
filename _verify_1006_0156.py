import json, subprocess, datetime
def get(url):
    r = subprocess.run(['curl', '-sL', '-m', '25', url], capture_output=True, text=True)
    return r.stdout

live = json.load(open('data/live-items.json'))
items = json.load(open('data/items.json'))
core = json.load(open('data/core.json'))
print('local live=%d items=%d core=%d meta.itemCount=%s' % (
    len(live['items']), len(items['items']), len(core['items']), live['meta']['itemCount']))

print('--- deployed ---')
for u in ['https://hkmaoquanqingbao.com/feed/all.json',
          'https://hkmaoquanqingbao.com/data/core.json']:
    out = get(u + '?v=' + str(int(datetime.datetime.now().timestamp())))
    try:
        d = json.loads(out)
        n = d.get('itemCount', len(d.get('items', [])))
        print(u, '-> itemCount/len =', n, '| generatedAt', d.get('generatedAt'))
    except Exception as e:
        print(u, '-> parse fail', type(e).__name__, out[:120])

print('--- new items present in deployed app.js? ---')
app = get('https://hkmaoquanqingbao.com/app.js?v=' + str(int(datetime.datetime.now().timestamp())))
print('app.js bytes:', len(app))
for probe in ['hkma-bakai-bank-restricted-licence-20261005',
              'ibm-ia-conduct-focus-broker-ro-tenure-20260930',
              'insurtech-corgi-datacentre-ai-infrastructure-cover-20261005',
              'reinasia-cpic-hk-liquidity-sp-ratings-20261005']:
    print('  ', probe, '->', probe in app)
