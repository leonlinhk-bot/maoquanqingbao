# -*- coding: utf-8 -*-
import json
live = json.load(open('data/live-items.json', encoding='utf-8'))['items']
terms = ['CRS', '税务', '稅務', '境外保单', '境外保單', '沛良', 'Chan Pui', '共同汇报', '共同匯報', '境外保险收益']
for t in terms:
    hits = [(it.get('id'), it.get('sourceKey'), it.get('publishedAt')) for it in live
            if t.lower() in json.dumps(it, ensure_ascii=False).lower()]
    print(f'{t}: {len(hits)} hits')
    for h in hits[:5]:
        print('   ', h)
print()
print('--- any item with "税" or "Tax" in title ---')
for it in live[:250]:
    ti = it.get('title', {}).get('sc', '') + it.get('title', {}).get('tc', '')
    if '税' in ti or '稅' in ti or 'Tax' in ti or 'CRS' in ti:
        print(it.get('publishedAt', '')[:10], '|', it.get('id'), '|', ti[:60])
