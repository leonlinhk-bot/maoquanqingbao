#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert daily collected items (2026-08-17 18:08 run) into live-items.json + update last-check.json."""
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
    # 1. BOC Life x Hygge Living cross-border elder care alliance (17 Aug 2026, official)
    item(
        "boclife-hygge-eldercare-alliance-20260817", 75, "verified", "insurer",
        "boclife",
        "中银人寿与Hygge Living策略联盟：共建中产家庭跨境养老服务生态",
        "中銀人壽與Hygge Living策略聯盟：共建中產家庭跨境養老服務生態",
        "中银人寿8月17日宣布与Hygge Living达成策略联盟，共建面向中产家庭的优质跨境养老服务生态，整合保险与养老照护资源。继与Deloitte Private合作财富传承后，中银人寿年内再度深化康养布局，养老金融生态持续扩容。[EN原文]",
        "中銀人壽8月17日宣佈與Hygge Living達成策略聯盟，共建面向中產家庭的優質跨境養老服務生態，整合保險與養老照護資源。繼與Deloitte Private合作財富傳承後，中銀人壽年內再度深化康養佈局，養老金融生態持續擴容。[EN原文]",
        "养老金融是港险结构性主线，银保系保司年内连续落子财富传承与跨境养老，康养生态竞争升级；对前线养老方案推荐与跨境服务合作有直接参考价值。",
        "養老金融是港險結構性主線，銀保系保司年內連續落子財富傳承與跨境養老，康養生態競爭升級；對前線養老方案推薦與跨境服務合作有直接參考價值。",
        {"front": L("养老+保险组合方案话术", "養老+保險組合方案話術"), "midback": L("跨境养老合作合规要点", "跨境養老合作合規要點"), "lead": {}, "cross": L("中港养老资源衔接节点", "中港養老資源銜接節點")},
        {"front": 2, "midback": 1, "lead": 0, "cross": 2},
        "中银人寿官网新闻稿", "zh+en",
        ["family"], ["retirement", "cross-border"],
        ["中银人寿", "Hygge Living", "跨境养老", "养老金融", "策略联盟"], ["中銀人壽", "Hygge Living", "跨境養老", "養老金融", "策略聯盟"],
        "news", "2026-08-17T00:00:00+08:00",
        "https://bocg-life.bocgroup.com/en/news/boc-life-and-hygge-living-form-strategic-alliance-to-build-a-premium-cross-border-elder-care-ecosystem-for-middle-class-families.html",
    ),
    # 2. 金融时报: 5 insurers fail Q2 2026 solvency standards
    item(
        "nfra-solvency-q2-5-insurers-20260817", 62, "pending", "media",
        "sina",
        "二季度5家险企偿付能力不达标：长生人寿综合充足率68.4%评级D类 华汇人寿连续C类",
        "二季度5家險企償付能力不達標：長生人壽綜合充足率68.4%評級D類 華匯人壽連續C類",
        "金融时报梳理134家已披露二季度偿付能力报告的险企，华汇人寿、安华农险、长生人寿、前海财险、亚太财险5家不达标：长生人寿综合充足率68.4%、评级D类，华汇人寿连续C类，另有20余家长期未披露；行业平均180.6%，中小机构资本补充承压。",
        "金融時報梳理134家已披露二季度償付能力報告的險企，華匯人壽、安華農險、長生人壽、前海財險、亞太財險5家不達標：長生人壽綜合充足率68.4%、評級D類，華匯人壽連續C類，另有20餘家長期未披露；行業平均180.6%，中小機構資本補充承壓。",
        "内地险企偿付能力与资本出清进度是跨境再保、代销合作与行业景气判断的重要参照，中小险企风险与长期未披露问题值得持续跟踪。",
        "內地險企償付能力與資本出清進度是跨境再保、代銷合作與行業景氣判斷的重要參照，中小險企風險與長期未披露問題值得持續跟蹤。",
        {"front": {}, "midback": L("再保/代销对手方风险筛查", "再保/代銷對手方風險篩查"), "lead": {}, "cross": L("内地险企风险坐标", "內地險企風險座標")},
        {"front": 0, "midback": 2, "lead": 1, "cross": 1},
        "金融时报（新浪财经转载）", "zh",
        ["market"], ["capital", "statistics"],
        ["偿付能力", "金融监管总局", "长生人寿", "华汇人寿", "亚太财险"], ["償付能力", "金融監管總局", "長生人壽", "華匯人壽", "亞太財險"],
        "news", "2026-08-17T15:18:01+08:00",
        "http://finance.sina.cn/insurance/hydt/2026-08-17/detail-ininreat7846340.d.html",
    ),
    # 3. 证券日报: insurance funds usage balance tops RMB40 trillion
    item(
        "ce-insurance-funds-40trillion-20260817", 62, "pending", "media",
        "cecn",
        "险资运用余额首破40万亿：二季度末40.82万亿元 权益配置占比15.66%创历史新高",
        "險資運用餘額首破40萬億：二季度末40.82萬億元 權益配置佔比15.66%創歷史新高",
        "金融监管总局数据显示，二季度末险资运用余额40.82万亿元，首破40万亿关口，较年初增6.1%。股票与基金权益配置占比15.66%创历史新高，银行存款占比7.43%创新低；分红险热销与权益回暖推动险资加仓，权益配置连续8季提升。",
        "金融監管總局數據顯示，二季度末險資運用餘額40.82萬億元，首破40萬億關口，較年初增6.1%。股票與基金權益配置佔比15.66%創歷史新高，銀行存款佔比7.43%創新低；分紅險熱銷與權益回暖推動險資加倉，權益配置連續8季提升。",
        "内地险资规模与权益配置动向影响长线资金面与市场情绪，分红险热销亦与港险竞争环境联动，是市场板块的宏观背景坐标。",
        "內地險資規模與權益配置動向影響長線資金面與市場情緒，分紅險熱銷亦與港險競爭環境聯動，是市場板塊的宏觀背景座標。",
        {"front": L("分红险竞争背景话术", "分紅險競爭背景話術"), "midback": {}, "lead": {}, "cross": L("内地资金面与港险联动", "內地資金面與港險聯動")},
        {"front": 1, "midback": 0, "lead": 0, "cross": 1},
        "证券日报（央视网财经转载）", "zh",
        ["market"], ["capital", "macro"],
        ["保险资金", "40万亿", "权益配置", "险资入市", "金融监管总局"], ["保險資金", "40萬億", "權益配置", "險資入市", "金融監管總局"],
        "stats", "2026-08-17T09:35:00+08:00",
        "https://finance.cctv.com/2026/08/17/ARTIWJrHKIaQPZz7PWhHw4Hk260817.shtml",
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
