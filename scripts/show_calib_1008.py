#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Print source/score/lang/boards for calibration items."""
import json

d = json.load(open('/Users/leonliang/maoquanqingbao/data/live-items.json', encoding='utf-8'))
for tid in ('scmp-family-offices-pe-infrastructure-20261007', 'hkma-silver-bond-4th-interest-4-00-20261008',
            'bochk-online-life-premium-digital-one-20261006'):
    for it in d['items']:
        if it.get('id') == tid:
            print(tid)
            print('  score', it.get('score'), '| tier', it.get('sourceTier'), '| kind', it.get('contentKind'),
                  '| pub', it.get('publishedAt'))
            print('  source', json.dumps(it.get('source'), ensure_ascii=False))
            print('  boards', it.get('boards'), '| themes', it.get('themes'), '| verify', it.get('verifyStatus'))
            print('  title', json.dumps(it.get('title'), ensure_ascii=False))
            print('  actions', json.dumps(it.get('actions'), ensure_ascii=False)[:300])
            print('  roles', it.get('rolesImpact'))
            break
    else:
        print('MISSING', tid)
