#!/usr/bin/env python3
import json
d = json.load(open('data/live-items.json'))
for key in ('govhk', 'fstb', 'hkma', 'nfra'):
    its = [i for i in d['items'] if i.get('sourceKey') == key]
    print(f'\n##### {key}: {len(its)}')
    for it in its[:4]:
        print(' -', it.get('publishedAt'), '|', it.get('contentKind'), '|', it.get('score'), it.get('sourceTier'),
              '|', (it.get('title') or {}).get('tc', '')[:70])
        print('   url:', it.get('originalUrl'))
        print('   source:', json.dumps(it.get('source'), ensure_ascii=False))
        print('   boards:', it.get('boards'), 'themes:', it.get('themes'))
