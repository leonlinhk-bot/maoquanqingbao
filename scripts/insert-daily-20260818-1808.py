#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert daily collected items (2026-08-18 18:08 run) into live-items.json + update last-check.json.

Items collected after lastCheck 2026-08-17T18:22:46+08:00:
  1. IBMag: Aon Sidecar X - US$200M dedicated capacity for R&W + tax insurance (2026-08-17 22:37+08)
  2. 金融界(今日头条): 上半年银保盈利回暖 非上市险企净利+81.75% (2026-08-17 20:11+08)
  3. 深圳商报(今日头条): 大地财险文山支公司罚单56万 (2026-08-18 00:07+08)
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
    # 1. Aon Sidecar X: US$200M dedicated capacity for R&W and tax insurance (pro, EN)
    item(
        "ibmag-aon-sidecarx-20260817", 70, "verified", "pro",
        "insurancebusinessmag",
        "Aon推出Sidecar X平台：为R&W及税务保险提供2亿美元专属承保容量",
        "Aon推出Sidecar X平台：為R&W及稅務保險提供2億美元專屬承保容量",
        "Aon推出Sidecar X平台，以预先约定的核保与理赔框架连接保险资本与陈述保证（R&W）及税务保险产品，提供最高2亿美元专属承保容量，较市场标准条款缩短执行时间并享10%保费折扣；平台覆盖美国、加拿大、英国、欧洲经济区及亚洲客户。[EN原文]",
        "Aon推出Sidecar X平台，以預先約定的核保與理賠框架連接保險資本與陳述保證（R&W）及稅務保險產品，提供最高2億美元專屬承保容量，較市場標準條款縮短執行時間並享10%保費折扣；平台覆蓋美國、加拿大、英國、歐洲經濟區及亞洲客戶。[EN原文]",
        "并购交易保障需求升温背景下，经纪商以预承诺容量平台切入R&W与税务险，压缩交易时间并让利保费，是专业险与并购生态竞争升级的信号，对中港并购保险布局有参照意义。",
        "併購交易保障需求升溫背景下，經紀商以預承諾容量平台切入R&W與稅務險，壓縮交易時間並讓利保費，是專業險與併購生態競爭升級的信號，對中港併購保險佈局有參照意義。",
        {"front": {}, "midback": L("并购交易险报价与容量渠道对比", "併購交易險報價與容量渠道對比"), "lead": {}, "cross": L("R&W/税务险市场格局跟踪", "R&W/稅務險市場格局跟蹤")},
        {"front": 0, "midback": 2, "lead": 1, "cross": 1},
        "Insurance Business Asia", "en",
        ["market"], ["ma", "reinsurance"],
        ["Aon", "Sidecar X", "R&W保险", "税务保险", "并购交易险"], ["Aon", "Sidecar X", "R&W保險", "稅務保險", "併購交易險"],
        "news", "2026-08-17T22:37:31+08:00",
        "https://www.insurancebusinessmag.com/asia/news/breaking-news/aon-brings-us200-million-in-dedicated-capacity-to-randw-and-tax-insurance-586358.aspx",
    ),
    # 2. 金融界/今日头条: H1 banking & insurance earnings recovery (media, zh)
    item(
        "toutiao-h1-insurers-profit-20260817", 62, "pending", "media",
        "toutiao",
        "上半年银保盈利回暖：非上市险企净利707亿增81.75% 国寿中期预增215%-235%创千亿中报",
        "上半年銀保盈利回暖：非上市險企淨利707億增81.75% 國壽中期預增215%-235%創千億中報",
        "金融监管总局数据显示，上半年135家非上市险企合计净利润约707亿元，同比大增81.75%；中国人寿中期净利预增215%-235%至约1289-1371亿元，为保险业首个千亿利润中报；新华预增40%-60%、中国太平预增85%-95%，权益投资收益改善为核心驱动；银行业净息差1.41%四年首升。",
        "金融監管總局數據顯示，上半年135家非上市險企合計淨利潤約707億元，同比大增81.75%；中國人壽中期淨利預增215%-235%至約1289-1371億元，為保險業首個千億利潤中報；新華預增40%-60%、中國太平預增85%-95%，權益投資收益改善為核心驅動；銀行業淨息差1.41%四年首升。",
        "内地险企盈利与投资端修复是判断行业景气、分红险热销背景与资金面的宏观坐标，头部寿险千亿级利润中报对市场情绪与竞争格局有直接参照意义。",
        "內地險企盈利與投資端修復是判斷行業景氣、分紅險熱銷背景與資金面的宏觀座標，頭部壽險千億級利潤中報對市場情緒與競爭格局有直接參照意義。",
        {"front": L("分红险竞争宏观背景话术", "分紅險競爭宏觀背景話術"), "midback": {}, "lead": {}, "cross": L("内地险企业绩坐标", "內地險企業績座標")},
        {"front": 2, "midback": 0, "lead": 1, "cross": 1},
        "今日头条（金融界）", "zh",
        ["market"], ["results", "capital"],
        ["中国人寿", "新华保险", "中国太平", "非上市险企", "中期业绩预增"], ["中國人壽", "新華保險", "中國太平", "非上市險企", "中期業績預增"],
        "news", "2026-08-17T20:11:25+08:00",
        "http://m.toutiao.com/group/7674972016360915471/",
    ),
    # 3. 深圳商报/今日头条: 大地财险文山支公司罚单 (media, zh)
    item(
        "toutiao-dadi-fine-20260818", 60, "pending", "media",
        "toutiao",
        "大地财险文山两家支公司被罚56万元：未按规定使用费率+编制虚假财务资料",
        "大地財險文山兩家支公司被罰56萬元：未按規定使用費率+編製虛假財務資料",
        "文山金融监管分局8月17日披露，大地财险文山中心支公司、麻栗坡支公司因未按规定使用经批准或备案的保险费率、编制虚假财务资料等违规，合计被罚56万元，相关责任人3人遭警告并罚款11万元；年内大地财险多地分支机构已接连受罚，财险基层合规问题持续暴露。",
        "文山金融監管分局8月17日披露，大地財險文山中心支公司、麻栗坡支公司因未按規定使用經批准或備案的保險費率、編製虛假財務資料等違規，合計被罰56萬元，相關責任人3人遭警告並罰款11萬元；年內大地財險多地分支機構已接連受罰，財險基層合規問題持續暴露。",
        "内地财险监管对费率执行与财务数据真实性的执法持续加码，是跨境再保、代销合作中对手方合规筛查与内地市场环境判断的小样本信号，供合规与风控参考。",
        "內地財險監管對費率執行與財務數據真實性的執法持續加碼，是跨境再保、代銷合作中對手方合規篩查與內地市場環境判斷的小樣本信號，供合規與風控參考。",
        {"front": {}, "midback": L("内地险企合规风险筛查", "內地險企合規風險篩查"), "lead": {}, "cross": L("财险监管执法动态", "財險監管執法動態")},
        {"front": 0, "midback": 2, "lead": 0, "cross": 1},
        "今日头条（深圳商报）", "zh",
        ["market"], ["compliance", "regulation"],
        ["大地财险", "监管处罚", "文山金融监管分局", "编制虚假财务资料", "财险"], ["大地財險", "監管處罰", "文山金融監管分局", "編製虛假財務資料", "財險"],
        "enforcement", "2026-08-18T00:07:35+08:00",
        "http://m.toutiao.com/group/7675032860624962082/",
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
