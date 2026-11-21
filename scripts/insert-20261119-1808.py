#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""一次性插入 2026-11-18（上轮遗留候选）与 2026-11-19 18:08 采集的条目
窗口：2026-11-17 18:08 → 2026-11-19 18:08（11-18 轮未完成入库，本次补入）
"""
import json
import os
import shutil

BASE = '/Users/leonliang/maoquanqingbao'
LIVE = os.path.join(BASE, 'data', 'live-items.json')
FILES = [
    (os.path.join(BASE, 'data', '_new_1118.json'), '2026-11-18T18:08:00+08:00'),
    (os.path.join(BASE, 'data', '_new_1119.json'), '2026-11-19T18:08:00+08:00'),
]


def main():
    items = []
    for path, now in FILES:
        payload = json.load(open(path, encoding='utf-8'))
        for it in payload['items']:
            it['ingestedAt'] = now
            it['contentRole'] = {'sc': '本站导读', 'tc': '本站導讀'}
            it['featured'] = False
            it['evergreen'] = False
            it['summaryShort'] = {'sc': it['summary']['sc'][:80], 'tc': it['summary']['tc'][:80]}
            items.append(it)

    d = json.load(open(LIVE, encoding='utf-8'))
    old = d['items']
    existing_ids = {i['id'] for i in old}
    existing_urls = {(i.get('originalUrl') or '').rstrip('/') for i in old}

    new = []
    for it in items:
        if it['id'] in existing_ids:
            print('SKIP dup id:', it['id'])
            continue
        if it['originalUrl'].rstrip('/') in existing_urls:
            print('SKIP dup url:', it['id'])
            continue
        assert len(it['boards']) >= 1, it['id']
        assert len(it['themes']) >= 2, it['id']
        assert it['originalUrl'].startswith('http'), it['id']
        slen = len(it['summary']['sc'])
        assert 50 <= slen <= 170, (it['id'], slen)
        existing_ids.add(it['id'])
        existing_urls.add(it['originalUrl'].rstrip('/'))
        new.append(it)

    new.sort(key=lambda x: x['publishedAt'], reverse=True)
    d['items'] = new + old
    d.setdefault('meta', {})
    d['meta']['generatedAt'] = '2026-11-19T18:08:00+08:00'
    d['meta']['itemCount'] = len(d['items'])
    d['meta']['windowNote'] = {'sc': f'本库{len(d["items"])}条。', 'tc': f'本庫{len(d["items"])}條。'}

    shutil.copy(LIVE, LIVE + '.bak-1119-1808')
    json.dump(d, open(LIVE, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'inserted {len(new)} items, total {len(d["items"])}')
    for it in new:
        print('  +', it['id'], '|', it['publishedAt'], '| summary', len(it['summary']['sc']), '字')


if __name__ == '__main__':
    main()
