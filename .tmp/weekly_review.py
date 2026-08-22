#!/usr/bin/env python3
import json, collections, datetime, sys

live = json.load(open('data/live-items.json'))
items = live['items']
print("总条数:", len(items))

# 本周范围：周一 2026-08-17 00:00 到 2026-08-22 23:59（本地 +08:00）
start = datetime.datetime(2026,8,17,0,0,0, tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
end   = datetime.datetime(2026,8,22,23,59,59, tzinfo=datetime.timezone(datetime.timedelta(hours=8)))

def parse_ts(s):
    if not s: return None
    s = str(s).strip()
    # 处理带时区 / 无时区 / 只有日期
    try:
        # 尝试 isoformat 带时区
        dt = datetime.datetime.fromisoformat(s)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
        return dt
    except Exception:
        pass
    # date-only
    try:
        d = datetime.datetime.strptime(s[:10], "%Y-%m-%d")
        return d.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
    except Exception:
        return None

week_items = []
for it in items:
    dt = parse_ts(it.get('publishedAt'))
    if dt and start <= dt <= end:
        week_items.append(it)

print("本周(08-17~08-22)新增条数:", len(week_items))

# 按天分布
day_count = collections.Counter()
for it in week_items:
    dt = parse_ts(it.get('publishedAt'))
    day_count[dt.strftime('%Y-%m-%d')] += 1
print("\n按天分布:")
for d in sorted(day_count):
    print(f"  {d}: {day_count[d]}")

# sourceTier 分布
tier_count = collections.Counter(it.get('sourceTier','?') for it in week_items)
print("\nsourceTier分布:", dict(tier_count))

# boards 分布
board_count = collections.Counter()
for it in week_items:
    for b in (it.get('boards') or []):
        board_count[b] += 1
print("boards分布:", dict(board_count))

# contentKind 分布
kind_count = collections.Counter(it.get('contentKind','?') for it in week_items)
print("contentKind分布:", dict(kind_count))

# sourceKey 分布（信源覆盖）
sk_count = collections.Counter(it.get('sourceKey','?') for it in week_items)
print("\nsourceKey分布:")
for k,v in sk_count.most_common():
    print(f"  {k}: {v}")

# 格式检查
print("\n===== 格式检查 =====")
issues = []
for it in week_items:
    iid = it.get('id','?')
    # publishedAt 精确性
    pa = it.get('publishedAt')
    dt = parse_ts(pa)
    if dt is None:
        issues.append(f"[{iid}] publishedAt 无法解析: {pa!r}")
    elif len(str(pa)) <= 10:  # date-only
        issues.append(f"[{iid}] publishedAt 仅日期(未精确到分钟): {pa!r}")
    # source.lang
    src = it.get('source') or {}
    lang = src.get('lang')
    if lang not in ('zh','en','zh+en'):
        issues.append(f"[{iid}] source.lang 缺失/非法: {lang!r}")
    # sc/tc 双语
    for field in ('title','summary','why'):
        fv = it.get(field) or {}
        sc = (fv.get('sc') or '').strip()
        tc = (fv.get('tc') or '').strip()
        if not sc:
            issues.append(f"[{iid}] {field}.sc 为空")
        if not tc:
            issues.append(f"[{iid}] {field}.tc 为空")
    # 必填
    for field in ('sourceTier','sourceKey','originalUrl'):
        if not it.get(field):
            issues.append(f"[{iid}] 缺少 {field}")
    if not (it.get('boards')):
        issues.append(f"[{iid}] 缺少 boards")
    if not (it.get('themes')) or len(it['themes']) < 2:
        issues.append(f"[{iid}] themes < 2")
    # 摘要长度
    for field in ('summary',):
        fv = it.get(field) or {}
        sc = (fv.get('sc') or '')
        if not (50 <= len(sc) <= 100):
            issues.append(f"[{iid}] summary.sc 长度 {len(sc)} (要求50-100)")
    # 佣金/收益敏感词
    sc_full = str(it.get('summary',{}).get('sc','')) + str(it.get('why',{}).get('sc',''))
    for w in ('佣金比例','收益承诺','保证回报','保证收益'):
        if w in sc_full:
            issues.append(f"[{iid}] 含敏感词: {w}")

print(f"发现问题 {len(issues)} 条:")
for i in issues:
    print("  -", i)

# 重复检查（本周内 id 或 originalUrl 重复）
id_cnt = collections.Counter(it.get('id') for it in week_items)
dup_id = {k:v for k,v in id_cnt.items() if v>1}
print("\n本周内重复 id:", dup_id if dup_id else "无")

url_cnt = collections.Counter(it.get('originalUrl') for it in week_items)
dup_url = {k:v for k,v in url_cnt.items() if v>1 and k}
print("本周内重复 originalUrl:", dup_url if dup_url else "无")

# 全库 id 重复检查（本周 id 是否与历史冲突）
all_ids = set(it.get('id') for it in items)
print("全库 id 总数:", len(all_ids), "== 条数" if len(all_ids)==len(items) else "!= 条数(有重复)")
