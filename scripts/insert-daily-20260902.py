#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""每日增量采集 2026-09-02 (catch-up/18:08 例行): 插入新条目到 live-items.json 最前, 更新 meta
窗口: 2026-09-01T21:10:00+08:00 (last-check) 之后
信源覆盖: insuranceasia RSS(3) / jefferies-智通(1, 补录同日漏采); IA/HKMA/AIA/Manulife/Prudential/AXA/SunLife/IBM/SCMP/NFRA/家办/insurtech 无窗口内新公告
"""
import json, datetime

NOW = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
NOW_STR = NOW.strftime('%Y-%m-%dT%H:%M:%S+08:00')

NEW_ITEMS = [
    {
        "id": "iaa-tokio-marine-direct-commercial-20260902",
        "clusterCount": 1,
        "score": 63,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insuranceasia",
        "title": {
            "sc": "东京海上拟以3.61亿美元收购英国商业车险MGA Direct Commercial 料9月完成 [EN原文]",
            "tc": "東京海上擬以3.61億美元收購英國商業車險MGA Direct Commercial 料9月完成 [EN原文]"
        },
        "summary": {
            "sc": "东京海上控股拟经旗下Tokio Marine HCC以3.61亿美元收购英国商业车险管理总代理(MGA)Direct Commercial，已获监管批准、预期9月内完成。标的上一财年毛保费逾2.72亿美元、雇员约200人，专注货车等商业机动车险，与HCC现有组合不重叠，有助多元化与盈利增长。",
            "tc": "東京海上控股擬經旗下Tokio Marine HCC以3.61億美元收購英國商業車險管理總代理(MGA)Direct Commercial，已獲監管批准、預期9月內完成。標的上一年度毛保費逾2.72億美元、僱員約200人，專注貨車等商業機動車險，與HCC現有組合不重疊，有助多元化與盈利增長。"
        },
        "why": {
            "sc": "全球头部险企并购与分销形态变化样本：MGA模式在商业车险承保链条的价值上升，对香港经纪与承保格局具参照意义。",
            "tc": "全球頭部險企併購與分銷形態變化樣本：MGA模式在商業車險承保鏈條的價值上升，對香港經紀與承保格局具參照意義。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "全球险企并购格局跟踪", "tc": "全球險企併購格局跟蹤"},
            "lead": {},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 1, "lead": 0, "cross": 0},
        "source": {"sc": "InsuranceAsia 保险亚洲", "lang": "en"},
        "boards": ["insurer"],
        "themes": ["ma", "distribution"],
        "tags": {
            "sc": ["东京海上", "Tokio Marine", "MGA", "并购", "商业车险"],
            "tc": ["東京海上", "Tokio Marine", "MGA", "併購", "商業車險"]
        },
        "contentKind": "news",
        "publishedAt": "2026-09-02T06:00:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/tokio-marine-buys-direct-commercial-361m",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "iaa-pru-japan-sales-halt-20260902",
        "clusterCount": 1,
        "score": 62,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insuranceasia",
        "title": {
            "sc": "日本保德信人寿停售后新契约年化保费挫84% 涉106名在职及离职员工不当行为 [EN原文]",
            "tc": "日本保德信人壽停售後新契約年化保費挫84% 涉106名在職及離職員工不當行為 [EN原文]"
        },
        "summary": {
            "sc": "美国保德信金融旗下日本保德信人寿因员工不当行为自2月9日起暂停新单销售并延长，首季新契约年化保费跌84.3%至1,760万美元、件数跌91%；事件涉106名在职及离职员工，令数百客户损失约1,940万美元，公司靠价格变动准备金净利反升64.6%。",
            "tc": "美國保德信金融旗下日本保德信人壽因員工不當行為自2月9日起暫停新單銷售並延長，首季新契約年化保費跌84.3%至1,760萬美元、件數跌91%；事件涉106名在職及離職員工，令數百客戶損失約1,940萬美元，公司靠價格變動準備金淨利反升64.6%。"
        },
        "why": {
            "sc": "同业销售不当行为与停售整改的完整案例：涉百人规模、跨季影响新业务与客户赔偿，在销售行为监管趋严背景下具合规借鉴价值。",
            "tc": "同業銷售不當行為與停售整改的完整案例：涉百人規模、跨季影響新業務與客戶賠償，在銷售行為監管趨嚴背景下具合規借鑑價值。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "销售不当行为停售整改案例库", "tc": "銷售不當行為停售整改案例庫"},
            "lead": {},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 1, "lead": 0, "cross": 0},
        "source": {"sc": "InsuranceAsia 保险亚洲", "lang": "en"},
        "boards": ["insurer"],
        "themes": ["compliance", "distribution"],
        "tags": {
            "sc": ["保德信", "Prudential Financial", "销售停售", "不当行为", "合规"],
            "tc": ["保德信", "Prudential Financial", "銷售停售", "不當行為", "合規"]
        },
        "contentKind": "news",
        "publishedAt": "2026-09-02T05:30:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/prudential-life-insurances-new-contracts-plunge-91-after-sales-halt",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "iaa-apac-retirement-gap-20260902",
        "clusterCount": 1,
        "score": 65,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insuranceasia",
        "title": {
            "sc": "麦肯锡：亚太退休产品未满足「健康+财富」整合需求 仅14%持长期护理保障 [EN原文]",
            "tc": "麥肯錫：亞太退休產品未滿足「健康+財富」整合需求 僅14%持長期護理保障 [EN原文]"
        },
        "summary": {
            "sc": "麦肯锡2026亚洲退休客户调查：约30%受访者期望退休产品兼含健康与财富保障，但两类产品仍割裂供给；长期护理保障覆盖率仅14%（各市场6%-23%），26%想加购；另有26%不满产品缺乏通胀保障，31%最想要随通胀调整的给付。",
            "tc": "麥肯錫2026亞洲退休客戶調查：約30%受訪者期望退休產品兼含健康與財富保障，但兩類產品仍割裂供給；長期護理保障覆蓋率僅14%（各市場6%-23%），26%想加購；另有26%不滿產品缺乏通脹保障，31%最想要隨通脹調整的給付。"
        },
        "why": {
            "sc": "退休规划是港险主力场景：健康与财富整合、通胀挂钩给付、长护缺口三组数据，可直接用于客户退休需求诊断与产品对位。",
            "tc": "退休規劃是港險主力場景：健康與財富整合、通脹掛鈎給付、長護缺口三組數據，可直接用於客戶退休需求診斷與產品對位。"
        },
        "actions": {
            "front": {"sc": "客户退休需求诊断数据点", "tc": "客戶退休需求診斷數據點"},
            "midback": {},
            "lead": {"sc": "退休+长护产品对位素材", "tc": "退休+長護產品對位素材"},
            "cross": {}
        },
        "rolesImpact": {"front": 1, "midback": 0, "lead": 1, "cross": 0},
        "source": {"sc": "InsuranceAsia 保险亚洲", "lang": "en"},
        "boards": ["product"],
        "themes": ["retirement", "health"],
        "tags": {
            "sc": ["麦肯锡", "退休调查", "长期护理", "健康财富整合", "通胀"],
            "tc": ["麥肯錫", "退休調查", "長期護理", "健康財富整合", "通脹"]
        },
        "contentKind": "news",
        "publishedAt": "2026-09-02T05:00:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/in-focus/apac-retirement-products-fail-consumers-seeking-combined-cover",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "jefferies-aia-tp-20260901",
        "clusterCount": 1,
        "score": 70,
        "verifyStatus": "pending",
        "sourceTier": "pro",
        "sourceKey": "jefferies",
        "title": {
            "sc": "富瑞上调友邦目标价至114港元 维持「买入」 认为ROEV是最可靠估值指标",
            "tc": "富瑞上調友邦目標價至114港元 維持「買入」 認為ROEV是最可靠估值指標"
        },
        "summary": {
            "sc": "富瑞发研报指友邦第二季业绩符合预期，上半年新业务价值增速高于市场预测0.4%、税后经营溢利高4.1%；认为内含价值回报率(ROEV)是最可靠估值指标，目标价由111港元上调至114港元，维持「买入」，并将2026财年每股盈测上调3.5%、新业务价值预测上调0.7%。",
            "tc": "富瑞發研報指友邦第二季業績符合預期，上半年新業務價值增速高於市場預測0.4%、稅後經營溢利高4.1%；認為內含價值回報率(ROEV)是最可靠估值指標，目標價由111港元上調至114港元，維持「買入」，並將2026財年每股盈測上調3.5%、新業務價值預測上調0.7%。"
        },
        "why": {
            "sc": "继高盛点评保诚后卖方对友邦中报的又一解读：ROEV估值框架与盈测上调，反映对香港业务质量及内地客需求的正面判断。",
            "tc": "繼高盛點評保誠後賣方對友邦中報的又一解讀：ROEV估值框架與盈測上調，反映對香港業務質量及內地客需求的正面判斷。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "卖方估值观点跟踪", "tc": "賣方估值觀點跟蹤"},
            "lead": {"sc": "AIA中报后评级动向跟踪", "tc": "AIA中報後評級動向跟蹤"},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 1, "lead": 1, "cross": 0},
        "source": {"sc": "富瑞 Jefferies（转引智通财经/新浪财经）", "lang": "zh"},
        "boards": ["insurer"],
        "themes": ["aia", "analyst"],
        "tags": {
            "sc": ["富瑞", "Jefferies", "友邦", "目标价", "ROEV"],
            "tc": ["富瑞", "Jefferies", "友邦", "目標價", "ROEV"]
        },
        "contentKind": "news",
        "publishedAt": "2026-09-01T15:10:00+08:00",
        "originalUrl": "https://finance.sina.com.cn/stock/hkstock/hkgg/2026-09-01/doc-iniqiatv8215773.shtml",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    }
]


def main():
    # 摘要字数校验 (50-105字)
    for it in NEW_ITEMS:
        n = len(it['summary']['sc'])
        if not (50 <= n <= 105):
            print(f"WARN 摘要字数 {n}: {it['id']}")
        else:
            print(f"OK 摘要 {n}字: {it['id']}")

    path = 'data/live-items.json'
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    items = data['items']
    existing_ids = {it.get('id') for it in items}
    dup = [it['id'] for it in NEW_ITEMS if it['id'] in existing_ids]
    if dup:
        print('SKIP duplicates:', dup)
    fresh = [it for it in NEW_ITEMS if it['id'] not in existing_ids]
    titles = {(it.get('sourceKey'), it.get('title', {}).get('sc')) for it in items}
    fresh = [it for it in fresh if (it.get('sourceKey'), it.get('title', {}).get('sc')) not in titles]
    items[:0] = fresh
    data['items'] = items
    meta = data['meta']
    meta['itemCount'] = len(items)
    meta['generatedAt'] = NOW_STR
    meta['windowNote'] = {
        "sc": f"本库{len(items)}条。",
        "tc": f"本庫{len(items)}條。"
    }
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print(f'新增 {len(fresh)} 条 -> 总条数 {len(items)}')
    for it in fresh:
        print(' +', it['id'])


if __name__ == '__main__':
    main()
