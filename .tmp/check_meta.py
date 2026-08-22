#!/usr/bin/env python3
import json, collections
live = json.load(open('data/live-items.json'))
items = live['items']

# 摘要长度分布（本周）
import datetime
start = datetime.datetime(2026,8,17,0,0,0, tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
end   = datetime.datetime(2026,8,22,23,59,59, tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
def parse_ts(s):
    if not s: return None
    s=str(s).strip()
    try:
        dt=datetime.datetime.fromisoformat(s)
        if dt.tzinfo is None: dt=dt.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
        return dt
    except: 
        try: return datetime.datetime.strptime(s[:10],"%Y-%m-%d").replace(tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
        except: return None

buckets = collections.Counter()
over = []
for it in items:
    dt = parse_ts(it.get('publishedAt'))
    if dt and start <= dt <= end:
        for f in ('summary','why'):
            for lang in ('sc','tc'):
                L = len((it.get(f,{}) or {}).get(lang,''))
                buckets[(f,lang, '≤100' if L<=100 else ('101-130' if L<=130 else '>130'))] += 1
        sc_len = len(it.get('summary',{}).get('sc',''))
        if sc_len > 100:
            over.append((it['id'], sc_len, len(it.get('summary',{}).get('tc',''))))

print("摘要长度分布(条数):")
for k in sorted(buckets):
    print("  ", k, buckets[k])

print("\n超100字的 summary.sc 条目(id, sc_len, tc_len):")
over.sort(key=lambda x:-x[1])
for iid, sc, tc in over:
    print(f"  {iid}: sc={sc} tc={tc}")

# meta 结构
print("\n===== meta 顶层字段 =====")
print(list(live['meta'].keys()))
print("\nwindowNote:", json.dumps(live['meta'].get('windowNote'), ensure_ascii=False))
print("generatedAt:", live['meta'].get('generatedAt'))
print("itemCount:", live['meta'].get('itemCount'))
