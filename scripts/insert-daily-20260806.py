#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert daily collected items into live-items.json (2026-08-06 batch)"""
import json
from datetime import datetime, timezone, timedelta

HKT = timezone(timedelta(hours=8))
NOW = datetime(2026, 8, 6, 18, 8, 0, tzinfo=HKT)

new_items = [
    {
        "id": "cupi-am-best-profits-aug05",
        "clusterCount": 1, "score": 72, "verifyStatus": "verified",
        "sourceTier": "pro", "sourceKey": "insuranceasia:cupi-am-best-20260805",
        "title": {"sc": "AM Best：中华联合财险盈利依赖投资收益 承保接近盈亏平衡", "tc": "AM Best：中華聯合財險盈利依賴投資收益 承保接近盈虧平衡"},
        "summary": {"sc": "AM Best研究指出，中华联合财险（CUPI）盈利主要由投资收益驱动，承保结果接近盈亏平衡；2025年资本及盈余增5.4%至27.8亿美元，风险调整后资本维持极强水平。公司为中投旗下国内主要农险保司，占全国非寿险市场约4%、农险市场12%；相对较高承保杠杆及政策性农险大额应收保费为主要抵消因素。[EN原文]", "tc": "AM Best研究指出，中華聯合財險（CUPI）盈利主要由投資收益驅動，承保結果接近盈虧平衡；2025年資本及盈餘增5.4%至27.8億美元，風險調整後資本維持極強水平。公司為中投旗下國內主要農險保司，佔全國非壽險市場約4%、農險市場12%；相對較高承保槓桿及政策性農險大額應收保費為主要抵消因素。[EN原文]"},
        "why": {"sc": "中资财险「承保弱、投资补」困局+主权基金股东支持的样本，可与港险财险板块承保表现对照；政策性农险应收保费风险亦是理解内地财险报表的素材。", "tc": "中資財險「承保弱、投資補」困局+主權基金股東支持的樣本，可與港險財險板塊承保表現對照；政策性農險應收保費風險亦是理解內地財險報表的素材。"},
        "actions": {"front": {"sc": "投资收益撑盈利=内地财险承保仍弱", "tc": "投資收益撐盈利=內地財險承保仍弱"}, "midback": {"sc": "农险应收保费=政策性业务的报表风险点", "tc": "農險應收保費=政策性業務的報表風險點"}, "lead": {"sc": "中投股东支持=资本实力背书", "tc": "中投股東支持=資本實力背書"}, "cross": {}},
        "rolesImpact": {"front": 0, "midback": 2, "lead": 1, "cross": 0},
        "source": {"sc": "Insurance Asia / AM Best", "tc": "Insurance Asia / AM Best", "lang": "en"},
        "boards": ["insurer"], "themes": ["firm", "market"],
        "tags": {"sc": ["AM Best", "中华联合财险", "投资收益", "农险", "评级"], "tc": ["AM Best", "中華聯合財險", "投資收益", "農險", "評級"]},
        "contentKind": "research", "publishedAt": "2026-08-05T05:30:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/investment-income-props-china-united-property-profits"
    },
    {
        "id": "beazley-h1-profits-halve-aug05",
        "clusterCount": 1, "score": 64, "verifyStatus": "verified",
        "sourceTier": "media", "sourceKey": "insurancebusinessmag:beazley-h1-20260805",
        "title": {"sc": "Beazley上半年税前利润腰斩53% 网络险费率连跌12季 苏黎世收购推进中", "tc": "Beazley上半年稅前利潤腰斬53% 網絡險費率連跌12季 蘇黎世收購推進中"},
        "summary": {"sc": "伦敦上市专业险企Beazley上半年税前利润2.377亿美元，同比降53%；综合成本率升至93.3%。全球网络险费率二季度再跌4%、连续12季下行，商业险整体费率跌6%；公司主动收缩美国网络险敞口、转向百慕大平台，MAP风险业务因中东局势增长6.1%。苏黎世81亿英镑收购待多监管审批，预计下半年完成。[EN原文]", "tc": "倫敦上市專業險企Beazley上半年稅前利潤2.377億美元，同比降53%；綜合成本率升至93.3%。全球網絡險費率二季度再跌4%、連續12季下行，商業險整體費率跌6%；公司主動收縮美國網絡險敞口、轉向百慕大平台，MAP風險業務因中東局勢增長6.1%。蘇黎世81億英鎊收購待多監管審批，預計下半年完成。[EN原文]"},
        "why": {"sc": "网络险价格周期见顶回落+中东地缘风险推高索赔，是亚太及香港网络险与marine war风险定价的背景板；苏黎世收购Beazley亦将重塑全球专业险格局。", "tc": "網絡險價格週期見頂回落+中東地緣風險推高索賠，是亞太及香港網絡險與marine war風險定價的背景板；蘇黎世收購Beazley亦將重塑全球專業險格局。"},
        "actions": {"front": {"sc": "网络险费率12季连跌=价格周期见顶", "tc": "網絡險費率12季連跌=價格週期見頂"}, "midback": {"sc": "中东冲突推高MAP索赔=地缘风险传导", "tc": "中東衝突推高MAP索賠=地緣風險傳導"}, "lead": {"sc": "苏黎世收购年内完成=专业险格局生变", "tc": "蘇黎世收購年內完成=專業險格局生變"}, "cross": {}},
        "rolesImpact": {"front": 1, "midback": 2, "lead": 1, "cross": 1},
        "source": {"sc": "Insurance Business Asia / Beazley", "tc": "Insurance Business Asia / Beazley", "lang": "en"},
        "boards": ["market"], "themes": ["market", "tech"],
        "tags": {"sc": ["Beazley", "网络险", "费率周期", "苏黎世", "专业险"], "tc": ["Beazley", "網絡險", "費率週期", "蘇黎世", "專業險"]},
        "contentKind": "news", "publishedAt": "2026-08-05T14:30:00+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/beazleys-profits-halve-as-cyber-prices-and-middle-east-squeeze-the-market-584983.aspx"
    },
    {
        "id": "korea-health-gap-brokers-aug05",
        "clusterCount": 1, "score": 66, "verifyStatus": "verified",
        "sourceTier": "media", "sourceKey": "insurancebusinessmag:korea-health-gap-20260805",
        "title": {"sc": "韩国健康险三重压力：公共医保财政悬崖+补偿险亏损1.87万亿韩元+佣金分期改革", "tc": "韓國健康險三重壓力：公共醫保財政懸崖+補償險虧損1.87萬億韓元+佣金分期改革"},
        "summary": {"sc": "韩国健康保险市场面临三重结构性压力：国民健康保险储备预计2030年耗尽、2042年年度赤字达123万亿韩元；私人补偿型健康险2025年亏损1.87万亿韩元、赔付率101%；分销端自2027年1月起佣金改为四年分期、2029年延至七年，首年佣金1200%上限扩大至个人代理。72%韩民持有商业健康险，公共体系仅覆盖医疗支出62.3%。[EN原文]", "tc": "韓國健康保險市場面臨三重結構性壓力：國民健康保險儲備預計2030年耗盡、2042年年度赤字達123萬億韓元；私人補償型健康險2025年虧損1.87萬億韓元、賠付率101%；分銷端自2027年1月起佣金改為四年分期、2029年延至七年，首年佣金1200%上限擴大至個人代理。72%韓民持有商業健康險，公共體系僅覆蓋醫療支出62.3%。[EN原文]"},
        "why": {"sc": "韩国佣金分期+上限改革与香港佣金设限监管同频，是观察「佣金改革对渠道与产品影响」的对照样本；公共医保财政压力下商业健康险重定价逻辑亦值得港险参考。", "tc": "韓國佣金分期+上限改革與香港佣金設限監管同頻，是觀察「佣金改革對渠道與產品影響」的對照樣本；公共醫保財政壓力下商業健康險重定價邏輯亦值得港險參考。"},
        "actions": {"front": {"sc": "佣金分期改革=与香港佣金设限同频", "tc": "佣金分期改革=與香港佣金設限同頻"}, "midback": {"sc": "公共医保财政悬崖=商业健康险需求上行", "tc": "公共醫保財政懸崖=商業健康險需求上行"}, "lead": {"sc": "赔付率101%=重定价周期开启", "tc": "賠付率101%=重定價週期開啟"}, "cross": {}},
        "rolesImpact": {"front": 2, "midback": 1, "lead": 1, "cross": 1},
        "source": {"sc": "Insurance Business Asia", "tc": "Insurance Business Asia", "lang": "en"},
        "boards": ["market"], "themes": ["channel", "market"],
        "tags": {"sc": ["韩国", "健康险", "佣金改革", "医保赤字", "重定价"], "tc": ["韓國", "健康險", "佣金改革", "醫保赤字", "重定價"]},
        "contentKind": "news", "publishedAt": "2026-08-05T10:00:00+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/life-insurance/south-koreas-health-coverage-gap-is-widening--and-brokers-are-in-the-middle-585038.aspx"
    }
]

with open("data/live-items.json", "r", encoding="utf-8") as f:
    data = json.load(f)

existing_ids = {item["id"] for item in data["items"]}
existing_source_keys = {item.get("sourceKey", "") for item in data["items"]}

filtered = []
for item in new_items:
    if item["id"] in existing_ids:
        print(f"SKIP (dup id): {item['id']}")
        continue
    if item.get("sourceKey", "") in existing_source_keys:
        print(f"SKIP (dup sourceKey): {item['sourceKey']}")
        continue
    item["ingestedAt"] = NOW.isoformat()
    item["contentRole"] = {"sc": "本站导读", "tc": "本站導讀"}
    item["featured"] = False
    item["evergreen"] = False
    filtered.append(item)

data["items"] = filtered + data["items"]

data["meta"]["generatedAt"] = NOW.isoformat()
data["meta"]["itemCount"] = len(data["items"])
data["meta"]["windowNote"] = {
    "sc": f"本库{len(data['items'])}条。今日新增{len(filtered)}条。",
    "tc": f"本庫{len(data['items'])}條。今日新增{len(filtered)}條。"
}
data["meta"]["asOf"] = "2026-08-06"

with open("data/live-items.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Inserted {len(filtered)} new items. Total: {len(data['items'])}")
for item in filtered:
    print(f"  + {item['id']} [{item['sourceTier']}] {item['title']['sc'][:50]}")
