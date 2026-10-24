#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, re
from datetime import datetime, timedelta, timezone
from collections import Counter

d = json.load(open('data/live-items.json'))
items = d['items']

def parse_ts(s):
    if not s: return None
    s = str(s).strip()
    if re.fullmatch(r'\d{4}-\d{2}-\d{2}', s):
        return datetime.fromisoformat(s).replace(tzinfo=timezone(timedelta(hours=8)))
    try:
        return datetime.fromisoformat(s)
    except:
        return None

# This week window: Monday 2026-10-19 00:00 -> Sunday 2026-10-25 00:00 (HK time)
wk_start = datetime(2026,10,19,0,0,0, tzinfo=timezone(timedelta(hours=8)))
wk_end   = datetime(2026,10,25,0,0,0, tzinfo=timezone(timedelta(hours=8)))

week = []
for it in items:
    # use publishedAt first, fall back to ingestedAt for dating
    ts = parse_ts(it.get('publishedAt')) or parse_ts(it.get('ingestedAt'))
    if ts and wk_start <= ts < wk_end:
        week.append((ts, it))

week.sort(key=lambda x: x[0])
print(f'本周({wk_start.date()} ~ {wk_end.date()}) 新增: {len(week)} 条\n')

# daily breakdown
days = Counter(t.date() for t,_ in week)
for dd in sorted(days):
    print(f'  {dd} ({dd.strftime("%a")}): {days[dd]} 条')

# boards distribution
print('\n=== 类别分布 (boards) ===')
bcount = Counter()
for _,it in week:
    for b in it.get('boards',[]):
        bcount[b]+=1
for b,c in bcount.most_common():
    print(f'  {b}: {c}')

# contentKind distribution
print('\n=== contentKind ===')
ck = Counter(it.get('contentKind') for _,it in week)
for k,c in ck.most_common():
    print(f'  {k}: {c}')

# sourceTier distribution
print('\n=== sourceTier ===')
st = Counter(it.get('sourceTier') for _,it in week)
for k,c in st.most_common():
    print(f'  {k}: {c}')

# sourceKey distribution
print('\n=== sourceKey ===')
sk = Counter(it.get('sourceKey') for _,it in week)
for k,c in sk.most_common():
    print(f'  {k}: {c}')

# themes distribution
print('\n=== themes (top) ===')
th = Counter()
for _,it in week:
    for t in it.get('themes',[]):
        th[t]+=1
for t,c in th.most_common(25):
    print(f'  {t}: {c}')
