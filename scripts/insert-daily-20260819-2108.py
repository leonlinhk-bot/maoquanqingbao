#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert daily collected items (2026-08-19 21:08 run) into live-items.json + update last-check.json.

Items collected after lastCheck 2026-08-19T18:23:59+08:00:
  1. HKEX: 2026 interim results - H1 revenue HK$16.7b (+19%), net profit HK$10.57b (+24%),
     Stock Connect revenue +57% to record HK$2.85b (2026-08-19 12:20+08, 上轮窗口遗漏补采:
     18:08 轮聚焦保司/监管，港交所中期业绩公告与当日「内地险资经沪深港通投港股ETF」
     政策主题直接呼应，作为市场基础设施数据点收录)
"""
import json
from pathlib import Path
from datetime import datetime, timezone, timedelta

ROOT = Path(__file__).resolve().parent.parent
LIVE = ROOT / 'data/live-items.json'
LASTCHECK = ROOT / 'data/last-check.json'
HKT = timezone(timedelta(hours=8))
INGESTED = datetime.now(HKT).isoformat(timespec='seconds')


def item(id_, score, verify, tier, key, title_sc, title_tc, sum_sc, sum_tc,
         why_sc, why_tc, actions, roles, src_sc, lang, boards, themes,
         tags_sc, tags_tc, kind, published, url):
    return {
        "id": id_, "clusterCount": 1, "score": score, "verifyStatus": verify,
        "sourceTier": tier, "sourceKey": key,
        "title": {"sc": title_sc, "tc": title_tc},
        "summary": {"sc": sum_sc, "tc": sum_tc},
        "why": {"sc": why_sc, "tc": why_tc},
        "actions": actions, "rolesImpact": roles,
        "source": {"sc": src_sc, "lang": lang},
        "boards": boards, "themes": themes,
        "tags": {"sc": tags_sc, "tc": tags_tc},
        "contentKind": kind, "publishedAt": published, "originalUrl": url,
        "ingestedAt": INGESTED,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False, "evergreen": False,
    }


def L(sc, tc):
    return {"sc": sc, "tc": tc}


new_items = [
    # 1. HKEX 2026 interim results (pro, zh)
    item(
        "hkex-h1-2026-results-20260819", 70, "verified", "pro",
        "hkex",
        "港交所中期业绩：上半年溢利105.7亿港元(+24%) 沪深港通收入28.5亿港元创新高",
        "港交所中期業績：上半年溢利105.7億港元(+24%) 滬深港通收入28.5億港元創新高",
        "港交所2026中期业绩：上半年收入及其他收益167亿港元(+19%)、股东应占溢利105.7亿港元(+24%)，现货市场日均成交2830亿港元创同期新高，沪深港通收入28.5亿港元、同比升57%，创历来半年度新高。监管刚放行内地险资经沪深港通投资港股ETF，市场基础设施活跃度数据为险资南下配置提供宏观参照。",
        "港交所2026中期業績：上半年收入及其他收益167億港元(+19%)、股東應佔溢利105.7億港元(+24%)，現貨市場日均成交2830億港元創同期新高，滬深港通收入28.5億港元、同比升57%，創歷來半年度新高。監管剛放行內地險資經滬深港通投資港股ETF，市場基礎設施活躍度數據為險資南下配置提供宏觀參照。",
        "内地险资经沪深港通投资港股ETF的通道刚获监管层明确支持，港交所作为通道基础设施，其沪深港通与ETF成交数据是评估险资南下配置落地空间的关键参照，亦反映香港市场对保险资金的承接能力，与当日港险资讯主题直接衔接。",
        "內地險資經滬深港通投資港股ETF的通道剛獲監管層明確支持，港交所作為通道基礎設施，其滬深港通與ETF成交數據是評估險資南下配置落地空間的關鍵參照，亦反映香港市場對保險資金的承接能力，與當日港險資訊主題直接銜接。",
        {"front": {}, "midback": {}, "lead": L("险资南下配置渠道与数据跟踪", "險資南下配置渠道與數據跟蹤"), "cross": L("互联互通/ETF生态观察", "互聯互通/ETF生態觀察")},
        {"front": 0, "midback": 0, "lead": 2, "cross": 1},
        "界面新闻（港交所公告）", "zh",
        ["market"], ["crossborder", "results"],
        ["港交所", "中期业绩", "沪深港通", "内地险资", "港股ETF"], ["港交所", "中期業績", "滬深港通", "內地險資", "港股ETF"],
        "news", "2026-08-19T12:20:00+08:00",
        "https://www.jiemian.com/article/14949228.html",
    ),
]


def main():
    data = json.loads(LIVE.read_text(encoding='utf-8'))
    items = data['items']

    existing_ids = {i['id'] for i in items}
    existing_urls = {i.get('originalUrl', '') for i in items}
    added = []
    for it in new_items:
        if it['id'] in existing_ids or it['originalUrl'] in existing_urls:
            print(f"SKIP duplicate: {it['id']}")
            continue
        added.append(it)

    if not added:
        print("Nothing to add.")
        return

    items[0:0] = added
    data['items'] = items
    data['meta']['itemCount'] = len(items)
    data['meta']['generatedAt'] = INGESTED
    data['meta']['windowNote'] = {
        "sc": f"本库{len(items)}条。",
        "tc": f"本庫{len(items)}條。"
    }
    LIVE.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding='utf-8')

    # update last-check.json: all source timestamps -> now
    lc = json.loads(LASTCHECK.read_text(encoding='utf-8'))
    lc['lastCheck'] = INGESTED
    for k in lc['sources']:
        lc['sources'][k]['last'] = INGESTED
    LASTCHECK.write_text(json.dumps(lc, ensure_ascii=False, indent=2), encoding='utf-8')

    print(f"INSERTED {len(added)} items; total now {len(items)}")
    for it in added:
        print(' +', it['id'], '|', it['sourceTier'], it['score'], '|', it['publishedAt'])


if __name__ == '__main__':
    main()
