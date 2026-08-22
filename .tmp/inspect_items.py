#!/usr/bin/env python3
import json
live = json.load(open('data/live-items.json'))
items = live['items']
by_id = {it['id']: it for it in items}

# 看看 date-only 条目和几条超长摘要的实际内容
for iid in ['ia-premium-financing-circular-20260820','hkma-fake-doc-scam-alert-20260820','chinalife-h1-2026-briefing-20260819']:
    it = by_id[iid]
    print("="*80)
    print("ID:", iid)
    print("publishedAt:", repr(it.get('publishedAt')))
    print("sourceTier:", it.get('sourceTier'), "| sourceKey:", it.get('sourceKey'))
    print("contentKind:", it.get('contentKind'))
    print("boards:", it.get('boards'))
    print("title.sc:", it['title']['sc'])
    print("summary.sc:", it['summary']['sc'])
    print("why.sc:", it.get('why',{}).get('sc'))
    print("source:", it.get('source'))
    print("originalUrl:", it.get('originalUrl'))
