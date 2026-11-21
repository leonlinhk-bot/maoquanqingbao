#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""一次性插入 2026-11-18 18:08 采集的条目
窗口：2026-11-17 18:08 → 2026-11-18 18:08
"""
import json, os, shutil

BASE = '/Users/leonliang/maoquanqingbao'
LIVE = os.path.join(BASE, 'data', 'live-items.json')
NEWF = os.path.join(BASE, 'data', '_new_1118.json')
NOW = '2026-11-18T18:08:00+08:00'


def main():
    payload = json.load(open(NEWF, encoding='utf-8'))
    ITEMS = payload['items']
    for it in ITEMS:
        it['ingestedAt'] = NOW
        it['contentRole'] = {'sc': '本站导读', 'tc': '本站導讀'}
        it['featured'] = False
        it['evergreen'] = False
        it['summaryShort'] = {'sc': it['summary']['sc'][:80], 'tc': it['summary']['tc'][:80]}

    d = json.load(open(LIVE, encoding='utf-8'))
    old = d['items']
    existing_ids = {i['id'] for i in old}
    existing_urls = {(i.get('originalUrl') or '').rstrip('/') for i in old}

    new = []
    for it in ITEMS:
        if it['id'] in existing_ids:
            print('SKIP dup id:', it['id']); continue
        if it['originalUrl'].rstrip('/') in existing_urls:
            print('SKIP dup url:', it['id']); continue
        # 质量校验
        assert len(it['boards']) >= 1, it['id']
        assert len(it['themes']) >= 2, it['id']
        assert it['originalUrl'].startswith('http'), it['id']
        slen = len(it['summary']['sc'])
        assert 50 <= slen <= 170, (it['id'], slen)
        new.append(it)

    d['items'] = new + old
    d.setdefault('meta', {})
    d['meta']['generatedAt'] = NOW
    d['meta']['itemCount'] = len(d['items'])
    d['meta']['windowNote'] = {'sc': f'本库{len(d["items"])}条。', 'tc': f'本庫{len(d["items"])}條。'}

    shutil.copy(LIVE, LIVE + '.bak-1118-1808')
    json.dump(d, open(LIVE, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'inserted {len(new)} items, total {len(d["items"])}')
    for it in new:
        print('  +', it['id'], '|', it['publishedAt'], '| summary', len(it['summary']['sc']), '字')


if __name__ == '__main__':
    main()
