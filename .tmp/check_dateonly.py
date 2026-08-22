#!/usr/bin/env python3
import json, collections
live = json.load(open('data/live-items.json'))
items = live['items']

# 全库 publishedAt 格式统计
dateonly = []
full = []
for it in items:
    pa = str(it.get('publishedAt') or '')
    if len(pa) == 10 and pa[4]=='-' and pa[7]=='-':
        dateonly.append(it['id'])
    else:
        full.append(pa)

print("全库 date-only (仅YYYY-MM-DD) 条数:", len(dateonly))
for i in dateonly:
    print("  ", i)

print("\n本周3条date-only的 contentKind:")
by = {it['id']:it for it in items}
for i in dateonly:
    it = by.get(i)
    # 只看本周
    print("  ", i, "|", it.get('contentKind'), "|", it.get('sourceTier'), "|", it.get('sourceKey'))

# 检查是否有 dateOnly 或 date-only 标记字段存在于任何条目
marker_fields = set()
for it in items:
    for k in it.keys():
        if 'date' in k.lower() and 'only' in k.lower():
            marker_fields.add(k)
print("\n条目中含 date-only 相关字段:", marker_fields or "无")

# 佣金/收益敏感词全面扫描
import re
sensitive = ['佣金','返佣','回佣','收益率','年化收益','保证收益','保证回报','回报率','杠杆','翻倍','稳赚','保本','承诺收益']
hits = collections.defaultdict(list)
for it in items:
    sc = str(it.get('summary',{}).get('sc',''))
    for w in sensitive:
        if w in sc:
            hits[w].append(it['id'])
print("\n敏感词扫描(摘要sc):")
for w, ids in hits.items():
    print(f"  {w}: {len(ids)}条 -> {ids[:10]}")
