#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert daily collected items (2026-08-19 00:5x catch-up run) into live-items.json + update last-check.json.

Window: after lastCheck 2026-08-18T18:18:06+08:00
Items collected (all verified against original pages):
  1. chinanews 中新社: 香港特区政府欢迎内地保险资金参与互联互通 (2026-08-18 20:38+08)
  2. stcn 证券时报: 证监会/港交所发声欢迎内地险资投资港股ETF (2026-08-18 19:51+08)
  3. scmp: Beijing urges mainland insurers to invest in HK-listed ETFs [EN] (2026-08-18 19:51+08)
  4. IBMag: Aon Working Capital Benchmarking APAC 2026 (2026-08-19 00:43+08)
  5. IBMag: QBE global data centre role / data centre premium (2026-08-19 00:41+08)
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
    # 1. 中新社: 特区政府欢迎内地保险资金参与互联互通 (media, zh)
    item(
        "chinanews-hkgov-insurance-funds-20260818", 64, "verified", "media",
        "chinanews",
        "香港特区政府欢迎内地保险资金参与互联互通 李家超：巩固香港国际金融中心地位",
        "香港特區政府歡迎內地保險資金參與互聯互通 李家超：鞏固香港國際金融中心地位",
        "肖远企8月18日会见许正宇，宣布支持内地保险资金参与互联互通、经沪深港通投资港股ETF；特区政府当晚热烈欢迎，李家超称便利内地险企多元配置、壮大香港ETF生态，陈茂波指将深化两地资本市场联动。",
        "肖遠企8月18日會見許正宇，宣佈支持內地保險資金參與互聯互通、經滬深港通投資港股ETF；特區政府當晚熱烈歡迎，李家超稱便利內地險企多元配置、壯大香港ETF生態，陳茂波指將深化兩地資本市場聯動。",
        "征税风波后罕见的官方暖风第二弹：特区政府最高层表态确认政策含金量，标志「保险资金+互联互通」进入落地通道，是内地险资南向配置与跨境财富叙事的政策温度计。",
        "徵稅風波後罕見的官方暖風第二彈：特區政府最高層表態確認政策含金量，標誌「保險資金+互聯互通」進入落地通道，是內地險資南向配置與跨境財富敘事的政策溫度計。",
        {"front": L("向高净值客户传达内地险资南向配置信号", "向高淨值客戶傳達內地險資南向配置信號"), "midback": L("互联互通政策温度监测", "互聯互通政策溫度監測"), "lead": {}, "cross": L("内地险资港股配置动向跟踪", "內地險資港股配置動向跟蹤")},
        {"front": 1, "midback": 2, "lead": 1, "cross": 2},
        "中新社（引特区政府新闻处）", "zh",
        ["market"], ["connectivity", "cross-border"],
        ["中新社", "特区政府", "李家超", "陈茂波", "互联互通", "保险资金"], ["中新社", "特區政府", "李家超", "陳茂波", "互聯互通", "保險資金"],
        "news", "2026-08-18T20:38:00+08:00",
        "http://m.chinanews.com/wap/detail/chs/zw/10679880.shtml",
    ),
    # 2. 证券时报: 证监会/港交所发声 (media, zh)
    item(
        "stcn-sfc-hkex-etf-20260818", 63, "verified", "media",
        "stcn",
        "证监会、港交所齐发声欢迎内地险资投资港股ETF 称将提升市场流动性",
        "證監會、港交所齊發聲歡迎內地險資投資港股ETF 稱將提升市場流動性",
        "金融监管总局宣布支持内地险资参与互联互通后，香港证监会主席黄天祐、行政总裁梁凤仪与港交所行政总裁陈翊庭相继表态欢迎；梁凤仪指将便利更多内地中长期资金以香港为平台作国际资产配置，陈翊庭称将显著提升香港ETF市场流动性。",
        "金融監管總局宣佈支持內地險資參與互聯互通後，香港證監會主席黃天祐、行政總裁梁鳳儀與港交所行政總裁陳翊庭相繼表態歡迎；梁鳳儀指將便利更多內地中長期資金以香港為平台作國際資產配置，陳翊庭稱將顯著提升香港ETF市場流動性。",
        "市场端监管与交易所集体背书，标志「保险资金+互联互通」从部委表态进入两地机构协同落地阶段；南向ETF资金流与流动性变化是后续最直接的观察指标。",
        "市場端監管與交易所集體背書，標誌「保險資金+互聯互通」從部委表態進入兩地機構協同落地階段；南向ETF資金流與流動性變化是後續最直接的觀察指標。",
        {"front": {}, "midback": {}, "lead": {}, "cross": L("沪深港通ETF资金流跟踪", "滬深港通ETF資金流跟蹤")},
        {"front": 1, "midback": 1, "lead": 1, "cross": 2},
        "证券时报", "zh",
        ["market"], ["connectivity", "cross-border"],
        ["证券时报", "香港证监会", "港交所", "ETF", "保险资金"], ["證券時報", "香港證監會", "港交所", "ETF", "保險資金"],
        "news", "2026-08-18T19:51:00+08:00",
        "https://www.stcn.com/article/detail/4084550.html",
    ),
    # 3. SCMP: Beijing urges mainland insurers to invest in HK-listed ETFs (media, en)
    item(
        "scmp-beijing-insurers-hk-etfs-20260818", 62, "verified", "media",
        "scmp",
        "SCMP：北京鼓励内地保险公司投资香港上市ETF 深化两地市场联通[EN原文]",
        "SCMP：北京鼓勵內地保險公司投資香港上市ETF 深化兩地市場聯通[EN原文]",
        "SCMP报道，肖远企在北京会见许正宇时宣布支持内地保险资金经沪深港通投资香港上市ETF；与会者还包括证监会投资产品部执行董事黄颖嘉及港交所行政总裁陈翊庭，许正宇称此举是深化两地市场联通的关键一步。[EN原文]",
        "SCMP報道，肖遠企在北京會見許正宇時宣佈支持內地保險資金經滬深港通投資香港上市ETF；與會者還包括證監會投資產品部執行董事黃穎嘉及港交所行政總裁陳翊庭，許正宇稱此舉是深化兩地市場聯通的關鍵一步。[EN原文]",
        "英文主流媒体对同一政策的独立报道，补充会议细节与官方英文口径，适合对外沟通与英文素材引用，与中文信源互为印证。",
        "英文主流媒體對同一政策的獨立報道，補充會議細節與官方英文口徑，適合對外溝通與英文素材引用，與中文信源互為印證。",
        {"front": {}, "midback": {}, "lead": {}, "cross": L("两地互联互通英文资料库", "兩地互聯互通英文資料庫")},
        {"front": 1, "midback": 1, "lead": 1, "cross": 2},
        "South China Morning Post", "en",
        ["market"], ["connectivity", "cross-border"],
        ["南华早报", "SCMP", "ETF", "互联互通", "保险资金"], ["南華早報", "SCMP", "ETF", "互聯互通", "保險資金"],
        "news", "2026-08-18T19:51:37+08:00",
        "https://www.scmp.com/business/banking-finance/article/3364453/beijing-urges-mainland-insurers-buy-hong-kong-listed-etfs",
    ),
    # 4. IBMag: Aon Working Capital Benchmarking APAC 2026 (media, en)
    item(
        "ibmag-aon-working-capital-apac-20260819", 61, "verified", "media",
        "insurancebusinessmag",
        "Aon：亚太企业平均79天回款 香港76天按年恶化3天 建筑行业143天最长",
        "Aon：亞太企業平均79天回款 香港76天按年惡化3天 建築行業143天最長",
        "Aon《亚太营运资金基准报告2026》显示，3805家上市公司平均应收账期79天；中国内地最长99天，香港76天、按年恶化3天，工程建筑行业143天居首。高融资成本下，贸易信用保险与应收账款融资是缓解回款压力的主要工具。[EN原文]",
        "Aon《亞太營運資金基準報告2026》顯示，3805家上市公司平均應收賬期79天；中國內地最長99天，香港76天、按年惡化3天，工程建築行業143天居首。高融資成本下，貿易信用保險與應收賬款融資是緩解回款壓力的主要工具。[EN原文]",
        "香港企业回款周期按年拉长叠加高融资成本，企业流动性压力上升——贸易信用险与应收账款融资是港险一般保险与金融险的潜在增长点，也是企业客户触达话题。",
        "香港企業回款周期按年拉長疊加高融資成本，企業流動性壓力上升——貿易信用險與應收賬款融資是港險一般保險與金融險的潛在增長點，也是企業客戶觸達話題。",
        {"front": {}, "midback": L("贸易信用险需求评估", "貿易信用險需求評估"), "lead": {}, "cross": L("亚太企业信用风险坐标", "亞太企業信用風險座標")},
        {"front": 1, "midback": 2, "lead": 1, "cross": 1},
        "Insurance Business Asia（Aon报告）", "en",
        ["market"], ["credit", "trade-credit"],
        ["Aon", "营运资金", "应收账款", "贸易信用保险", "亚太"], ["Aon", "營運資金", "應收賬款", "貿易信用保險", "亞太"],
        "news", "2026-08-19T00:43:00+08:00",
        "https://www.insurancebusinessmag.com/asia/news/breaking-news/cash-flow-squeeze-persists-across-asiapacific-new-aon-benchmarking-shows-586512.aspx",
    ),
    # 5. IBMag: QBE global data centre role / data centre premium (media, en)
    item(
        "ibmag-qbe-data-centre-20260819", 61, "verified", "media",
        "insurancebusinessmag",
        "QBE设立全球数据中心保险主管 标普预计数据中心险2026年新增保费约100亿美元",
        "QBE設立全球數據中心保險主管 標普預計數據中心險2026年新增保費約100億美元",
        "QBE委任资深员工出任新设全球数据中心保险总监，统筹核保、风险工程、理赔与分销。标普估计数据中心险2026年可带来约100亿美元新增保费，约为全球航空险年保费两倍；亚太近九成数据中心位于热旱压力区域，建设标准缺口明显。[EN原文]",
        "QBE委任資深員工出任新設全球數據中心保險總監，統籌核保、風險工程、理賠與分銷。標普估計數據中心險2026年可帶來約100億美元新增保費，約為全球航空險年保費兩倍；亞太近九成數據中心位於熱旱壓力區域，建設標準缺口明顯。[EN原文]",
        "数据中心作为高集中新兴风险类别正催生新保费池；亚太气候暴露与建设标准缺口意味着承保能力与条款创新机会，对港险一般保险与再保布局有前瞻参照。",
        "數據中心作為高集中新興風險類別正催生新保費池；亞太氣候暴露與建設標準缺口意味著承保能力與條款創新機會，對港險一般保險與再保佈局有前瞻參照。",
        {"front": {}, "midback": L("数据中心险承保能力与条款调研", "數據中心險承保能力與條款調研"), "lead": {}, "cross": L("新兴风险保费池跟踪", "新興風險保費池跟蹤")},
        {"front": 1, "midback": 2, "lead": 1, "cross": 1},
        "Insurance Business Asia", "en",
        ["market"], ["data-centre", "emerging-risk"],
        ["QBE", "数据中心", "标普", "新兴风险", "保险容量"], ["QBE", "數據中心", "標普", "新興風險", "保險容量"],
        "news", "2026-08-19T00:41:00+08:00",
        "https://www.insurancebusinessmag.com/asia/news/breaking-news/qbe-has-created-a-global-data-centre-role--and-asia-brokers-should-watch-what-it-does-next-586549.aspx",
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
