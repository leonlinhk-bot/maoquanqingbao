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

wk_start = datetime(2026,10,19,0,0,0, tzinfo=timezone(timedelta(hours=8)))
wk_end   = datetime(2026,10,25,0,0,0, tzinfo=timezone(timedelta(hours=8)))
week = []
for it in items:
    ts = parse_ts(it.get('publishedAt')) or parse_ts(it.get('ingestedAt'))
    if ts and wk_start <= ts < wk_end:
        week.append(it)

print(f'本周 {len(week)} 条\n')

# --- Format checks ---
issues = Counter()
date_only = 0
full_ts = 0
no_pub = 0
missing_lang = 0
missing_sc_tc = []
missing_boards = 0
missing_themes = 0
missing_sourceTier = 0
missing_originalUrl = 0
missing_sourceObj = 0
missing_summary = 0
missing_why = 0

for it in week:
    pid = it.get('id','?')
    pa = it.get('publishedAt')
    if not pa:
        no_pub += 1
    elif re.fullmatch(r'\d{4}-\d{2}-\d{2}', str(pa).strip()):
        date_only += 1
    else:
        full_ts += 1
    # source object lang
    src = it.get('source')
    if isinstance(src, dict):
        if not src.get('lang'):
            missing_lang += 1
    else:
        missing_sourceObj += 1
    # sc/tc completeness for title/summary/why
    for f in ('title','summary','why'):
        v = it.get(f)
        if not isinstance(v, dict) or 'sc' not in v or 'tc' not in v:
            missing_sc_tc.append((pid, f))
    if not it.get('boards'): missing_boards += 1
    if not it.get('themes') or len(it.get('themes',[]))<2: missing_themes += 1
    if not it.get('sourceTier'): missing_sourceTier += 1
    if not it.get('originalUrl'): missing_originalUrl += 1
    if not it.get('summary'): missing_summary += 1
    if not it.get('why'): missing_why += 1

print('=== 格式检查 ===')
print(f'publishedAt 缺失: {no_pub}')
print(f'publishedAt 仅日期(应精确到分钟, date-only): {date_only}')
print(f'publishedAt 完整时间戳: {full_ts}')
print(f'source.lang 缺失: {missing_lang}')
print(f'source 非对象: {missing_sourceObj}')
print(f'sc/tc 双语缺失: {len(missing_sc_tc)}')
for pid,f in missing_sc_tc[:20]:
    print(f'   {pid} -> {f}')
print(f'boards 缺失: {missing_boards}')
print(f'themes <2: {missing_themes}')
print(f'sourceTier 缺失: {missing_sourceTier}')
print(f'originalUrl 缺失: {missing_originalUrl}')
print(f'summary 缺失: {missing_summary}')
print(f'why 缺失: {missing_why}')

# --- Official / insurer / HKMA detail ---
print('\n=== 官方源明细 (sourceTier=official) ===')
for it in week:
    if it.get('sourceTier')=='official':
        print(f"  {it.get('id')} | {it.get('sourceKey')} | {it.get('publishedAt')} | {it.get('contentKind')} | {it.get('title',{}).get('sc','')[:50]}")
print('\n=== 保司源明细 (sourceTier=insurer) ===')
for it in week:
    if it.get('sourceTier')=='insurer':
        print(f"  {it.get('id')} | {it.get('sourceKey')} | {it.get('publishedAt')} | {it.get('title',{}).get('sc','')[:60]}")
print('\n=== reg board 明细 ===')
for it in week:
    if 'reg' in it.get('boards',[]):
        print(f"  {it.get('id')} | {it.get('sourceKey')} | {it.get('publishedAt')} | {it.get('title',{}).get('sc','')[:55]}")
print('\n=== family board 明细 ===')
for it in week:
    if 'family' in it.get('boards',[]):
        print(f"  {it.get('id')} | {it.get('sourceKey')} | {it.get('publishedAt')} | {it.get('title',{}).get('sc','')[:55]}")
