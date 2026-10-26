import json, re
d = json.load(open('data/live-items.json'))
items = d['items'] if isinstance(d, dict) else d
kw = ['保費融資', '保费融资', 'premium financing', 'Premium financing', '臨時統計', '临时统计', 'provisional statistics',
      '代幣化', '代币化', 'tokenis', 'ART', '按揭證券', 'Mortgage Corporation', '穩定幣', '稳定币', '南韓', '韩国', 'Lloyd', '勞合社', '劳合社',
      '專屬自保', 'captive', '參數', '参数保险', 'param']
for k in kw:
    hits = [(it.get('publishedAt'), it.get('sourceKey'), it.get('title', {}).get('sc', '')) for it in items
            if k.lower() in json.dumps(it, ensure_ascii=False).lower()]
    print('###', k, len(hits))
    for h in hits[:6]:
        print('   ', h[0], '|', h[1], '|', h[2][:70])
print('\n--- IA source latest 8 ---')
ia = [it for it in items if it.get('sourceKey') == 'ia']
ia.sort(key=lambda x: x.get('publishedAt') or '', reverse=True)
for it in ia[:8]:
    print(it.get('publishedAt'), '|', it.get('title', {}).get('sc', '')[:70])
print('\n--- hkma latest 6 ---')
hk = [it for it in items if it.get('sourceKey') == 'hkma']
hk.sort(key=lambda x: x.get('publishedAt') or '', reverse=True)
for it in hk[:6]:
    print(it.get('publishedAt'), '|', it.get('title', {}).get('sc', '')[:70])
