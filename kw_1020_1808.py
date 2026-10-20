import json, re
d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json'))
items = d['items']
print('total', len(items))
kw = ['标普', '標普', '五年规划', '五年規劃', 'Five-Year', '中介人', '纪律', '处分', 'ART 框架', 'ART框架', 'Sun Life', '永明', '印尼', '台湾', '台灣', 'HDFC', '大平', 'Taiping', 'NFRA', '国家金融监督管理总局', '气旋', '颱風', '巨灾基金', 'quick returns', '快返']
for k in kw:
    hits = [it for it in items if k in it['title']['sc'] or k in it['title']['tc']]
    print(f'--- {k}: {len(hits)}')
    for it in hits[:5]:
        print('    ', it['publishedAt'][:16], it['sourceKey'], it['title']['sc'][:70])
