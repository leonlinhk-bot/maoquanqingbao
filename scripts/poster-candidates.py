#!/usr/bin/env python3
"""
猫圈儿周报海报 · 候选条目提取器
自动取「上一完整周」（上周一~上周日）的条目，按 score 排序输出候选，
供人工/Agent 挑选 5 条并精写解读。

用法:
  python3 scripts/poster-candidates.py [--week 2026-W39] [--top 12] [--json]

输出 JSON:
{
  "week": "2026-W39", "range": "9 月 21 日 — 9 月 27 日",
  "start": "2026-09-21", "end": "2026-09-27",
  "total": 161, "digestCount": 13,
  "candidates": [{"id","score","date","tier","title","summary","why","source","url"}, ...]
}
"""
import json, sys, argparse
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIVE = ROOT / 'data' / 'live-items.json'


def tx(o):
    if not o:
        return ''
    if isinstance(o, dict):
        return o.get('sc') or o.get('tc') or ''
    return str(o)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--week', default=None, help='ISO 周号，如 2026-W39；默认上一完整周')
    ap.add_argument('--top', type=int, default=12)
    ap.add_argument('--json', action='store_true', help='仅输出 JSON（默认也是 JSON，此开关保留兼容）')
    a = ap.parse_args()

    today = date.today()
    if a.week:
        y, w = a.week.split('-W')
        mon = date.fromisocalendar(int(y), int(w), 1)
    else:
        # 上一完整周：本周一 - 7 天
        mon = today - timedelta(days=today.weekday() + 7)
    sun = mon + timedelta(days=6)
    wk = f"{mon.isocalendar()[0]}-W{mon.isocalendar()[1]:02d}"

    data = json.loads(LIVE.read_text(encoding='utf-8'))
    items = data.get('items', [])
    s, e = mon.isoformat(), sun.isoformat()
    week_items = [i for i in items if s <= (i.get('publishedAt') or '')[:10] <= e]

    # digests.weekly 的精选条数（海报「本周共 N 条导读」口径）
    digest_count = 0
    for d in (data.get('digests', {}) or {}).get('weekly', []):
        if d.get('key') == wk:
            digest_count = d.get('itemCount', 0)
            break

    cands = sorted(week_items, key=lambda x: (-(x.get('score') or 0), (x.get('publishedAt') or '')))[:a.top]
    out = {
        'week': wk,
        'range': f"{mon.month} 月 {mon.day} 日 — {sun.month} 月 {sun.day} 日",
        'start': s, 'end': e,
        'total': len(week_items),
        'digestCount': digest_count,
        'candidates': [{
            'id': i.get('id'),
            'score': i.get('score'),
            'date': (i.get('publishedAt') or '')[:10],
            'tier': i.get('sourceTier', ''),
            'title': tx(i.get('title')),
            'summary': tx(i.get('summary')),
            'why': tx(i.get('why')),
            'source': tx(i.get('source')),
            'url': i.get('originalUrl', ''),
        } for i in cands],
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
