#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""周末复核脚本：统计本周新增、类别分布、格式检查。"""
import json
from datetime import datetime, timedelta, timezone
from collections import Counter

D = json.load(open('data/live-items.json'))
items = D['items']

CST = timezone(timedelta(hours=8))
week_start = datetime(2026, 9, 7, 0, 0, 0, tzinfo=CST)
week_end = datetime(2026, 9, 12, 23, 59, 59, tzinfo=CST)


def pt(s):
    if not s:
        return None
    s = s.replace('Z', '+00:00')
    try:
        x = datetime.fromisoformat(s)
    except Exception:
        return None
    if x.tzinfo is None:
        x = x.replace(tzinfo=CST)
    return x


week_items = [i for i in items
              if (lambda p: p and week_start <= p <= week_end)(pt(i.get('publishedAt', '')))]

print('本周(9/7周一~9/12周六)新增:', len(week_items))
print()

tier = Counter(i.get('sourceTier') for i in week_items)
print('=== sourceTier 分布 ===')
for k, v in tier.most_common():
    print(f'  {k}: {v}')

print()
kind = Counter(i.get('contentKind') for i in week_items)
print('=== contentKind 分布 ===')
for k, v in kind.most_common():
    print(f'  {k}: {v}')

print()
board = Counter()
for i in week_items:
    for b in (i.get('boards') or []):
        board[b] += 1
print('=== boards 分布 ===')
for k, v in board.most_common():
    print(f'  {k}: {v}')

print()
sk = Counter(i.get('sourceKey') for i in week_items)
print('=== sourceKey 分布 ===')
for k, v in sk.most_common():
    print(f'  {k}: {v}')

print()
bydate = Counter()
for i in week_items:
    p = pt(i.get('publishedAt', ''))
    bydate[p.strftime('%m-%d')] += 1
print('=== 按日分布 ===')
for k in sorted(bydate):
    print(f'  {k}: {bydate[k]}')

# ---- 格式检查 ----
print()
print('=== 格式检查 ===')
issues = []
for i in week_items:
    iid = i.get('id', '?')
    # publishedAt 精确到分钟
    p = i.get('publishedAt', '')
    if not p:
        issues.append(f'{iid}: 缺 publishedAt')
    elif 'date-only' in str(i.get('contentKind', '')):
        pass
    else:
        p2 = pt(p)
        if p2 and p2.minute == 0 and p2.second == 0 and p2.hour == 0:
            issues.append(f'{iid}: publishedAt 疑似仅日期({p})')
    # source.lang
    src = i.get('source', {})
    lang = src.get('lang', '')
    if lang not in ('zh', 'en', 'zh+en'):
        issues.append(f'{iid}: source.lang 异常 ({lang})')
    # sc/tc 双语
    title = i.get('title', {})
    summary = i.get('summary', {})
    if not title.get('sc') or not title.get('tc'):
        issues.append(f'{iid}: title 缺 sc/tc')
    if not summary.get('sc') or not summary.get('tc'):
        issues.append(f'{iid}: summary 缺 sc/tc')
    # sourceTier / originalUrl / boards / themes
    if not i.get('sourceTier'):
        issues.append(f'{iid}: 缺 sourceTier')
    if not i.get('originalUrl'):
        issues.append(f'{iid}: 缺 originalUrl')
    if not (i.get('boards') or []):
        issues.append(f'{iid}: 缺 boards')
    if not (i.get('themes') or []):
        issues.append(f'{iid}: 缺 themes')

if issues:
    for x in issues:
        print('  [问题]', x)
else:
    print('  无格式问题')
print()
print('格式问题总数:', len(issues))