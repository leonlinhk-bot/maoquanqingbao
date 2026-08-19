#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert daily collected items (2026-08-20 early run) into live-items.json + update last-check.json.

Window: after lastCheck 2026-08-19T21:17:08+08:00 (overnight, ~6.5h).
web_extract/web_search (Firecrawl) were unconfigured this run -> doubao_search fallback used per skill.
Items:
  1. AIA 2026 interim results announced TODAY 20 Aug 2026 09:00 HKT analyst webcast (AIA IR page, verified)
  2. China Life 2026 interim results: publish 27 Aug, webcast briefing 28 Aug (HKEX filing 2026081900310, verified)
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
    # 1. AIA 2026 interim results day (insurer, zh)
    item(
        "aia-h1-2026-results-day-20260820", 75, "verified", "insurer",
        "aia",
        "友邦保险今日公布2026年中期业绩 上午9时网络直播分析师简报会",
        "友邦保險今日公佈2026年中期業績 上午9時網絡直播分析師簡報會",
        "友邦保险（1299.HK）将于今日上午9时公布2026年中期业绩，并由集团首席执行官兼总裁李源祥主持网络直播分析师简报会。今年首季新业务价值（VONB）按固定汇率增长13%至17.57亿美元、VONB利润率56%，市场聚焦上半年香港及内地业务动能、利润率走向与股东回报安排。",
        "友邦保險（1299.HK）將於今日上午9時公佈2026年中期業績，並由集團首席執行官兼總裁李源祥主持網絡直播分析師簡報會。今年首季新業務價值（VONB）按固定匯率增長13%至17.57億美元、VONB利潤率56%，市場聚焦上半年香港及內地業務動能、利潤率走向與股東回報安排。",
        "今日港险市场最重磅事件：友邦中报是衡量香港及内地新业务动能的核心标尺，结果与管理层指引将直接影响渠道谈单的市场叙事与同业全年预期校准，值得第一时间跟进并解读。",
        "今日港險市場最重磅事件：友邦中報是衡量香港及內地新業務動能的核心標尺，結果與管理層指引將直接影響渠道談單的市場敘事與同業全年預期校準，值得第一時間跟進並解讀。",
        {"front": {}, "midback": {}, "lead": L("友邦中报要点与渠道话术跟进", "友邦中報要點與渠道話術跟進"), "cross": L("港险中报季同业对照", "港險中報季同業對照")},
        {"front": 0, "midback": 0, "lead": 2, "cross": 1},
        "友邦保险投资者关系官网", "zh",
        ["insurer"], ["results", "market"],
        ["友邦保险", "中期业绩", "新业务价值", "VONB", "李源祥"], ["友邦保險", "中期業績", "新業務價值", "VONB", "李源祥"],
        "news", "2026-08-20T09:00:00+08:00",
        "https://www.aia.com/zh-hk/investor-relations/overview",
    ),
    # 2. China Life 2026 interim results schedule (insurer, zh+en)
    item(
        "chinalife-h1-2026-briefing-20260819", 75, "verified", "insurer",
        "chinalife",
        "中国人寿：8月27日公布2026年中期业绩 28日举行网络业绩简报会",
        "中國人壽：8月27日公佈2026年中期業績 28日舉行網絡業績簡報會",
        "中国人寿（2628.HK）公告将于8月27日在港交所披露2026年中期业绩，并于8月28日上午11时至12时举行网络业绩简报会，执行董事兼总裁李明光及高级管理层出席；投资者可于8月26日前电邮提问，会后视频将上载公司官网。",
        "中國人壽（2628.HK）公告將於8月27日在港交所披露2026年中期業績，並於8月28日上午11時至12時舉行網絡業績簡報會，執行董事兼總裁李明光及高級管理層出席；投資者可於8月26日前電郵提問，會後視頻將上載公司官網。",
        "内地寿险龙头中报时点确认，与友邦业绩日前后相接，形成中港中报季对照窗口；中资险企基本面与分红节奏是评估内地客户配置需求的背景信息，对渠道有跟踪价值。",
        "內地壽險龍頭中報時點確認，與友邦業績日前後相接，形成中港中報季對照窗口；中資險企基本面與分紅節奏是評估內地客戶配置需求的背景信息，對渠道有跟蹤價值。",
        {"front": {}, "midback": {}, "lead": L("中资险企中报季跟踪", "中資險企中報季跟蹤"), "cross": L("中港保险中报对照", "中港保險中報對照")},
        {"front": 0, "midback": 0, "lead": 1, "cross": 1},
        "港交所披露易（中国人寿公告）", "zh+en",
        ["insurer"], ["results", "market"],
        ["中国人寿", "中期业绩", "业绩简报会", "2628.HK", "中报季"], ["中國人壽", "中期業績", "業績簡報會", "2628.HK", "中報季"],
        "news", "2026-08-19",
        "https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0819/2026081900310.pdf",
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
