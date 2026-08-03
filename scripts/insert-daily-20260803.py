#!/usr/bin/env python3
"""Insert daily collected items into live-items.json (2026-08-03 batch)"""
import json
from datetime import datetime, timezone, timedelta

HKT = timezone(timedelta(hours=8))
NOW = datetime(2026, 8, 3, 18, 8, 0, tzinfo=HKT)

new_items = [
    {
        "id": "jefferies-hk-channels-aug03",
        "clusterCount": 1, "score": 75, "verifyStatus": "pending",
        "sourceTier": "pro", "sourceKey": "insuranceasia:jefferies-channels-20260803",
        "title": {"sc": "Jefferies：港险Q1新单保费+47% 保单件数仅+2% 件均保费+45%", "tc": "Jefferies：港險Q1新單保費+47% 保單件數僅+2% 件均保費+45%"},
        "summary": {"sc": "Jefferies拆解港险Q1监管申报数据：个人新单保费同比+47%，代理+39%、银保+59%、经纪+30%，但新保单件数仅+2%、件均保费+45%，增长主要来自高价值保单而非销售产能。经纪已成为宏利与富卫最大渠道，友邦代理新单+44%、宏利代理+102%。[EN原文]", "tc": "Jefferies拆解港險Q1數據：個人新單保費+47%，保單件數僅+2%、件均保費+45%，增長靠高價值保單；經紀已成宏利與富衛最大渠道，友邦代理新單+44%。"},
        "why": {"sc": "渠道格局与件均逻辑=判断高净值客群与经纪渠道趋势的一手依据", "tc": "渠道格局與件均邏輯=判斷高淨值客群與經紀渠道趨勢的一手依據"},
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 2, "midback": 2, "lead": 1, "cross": 1},
        "source": {"sc": "Insurance Asia / Jefferies", "tc": "Insurance Asia / Jefferies", "lang": "en"},
        "boards": ["market"], "themes": ["channel", "mainland-wealth"],
        "tags": {"sc": ["Jefferies", "渠道", "经纪", "银保", "件均保费"], "tc": ["Jefferies", "渠道", "經紀", "銀保", "件均保費"]},
        "contentKind": "news", "publishedAt": "2026-08-03T05:45:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/jefferies-warns-policy-growth-lags-hong-kong-premium-surge"
    },
    {
        "id": "aia-crossborder-care-aug03",
        "clusterCount": 1, "score": 72, "verifyStatus": "pending",
        "sourceTier": "insurer", "sourceKey": "insuranceasia:aia-crossborder-20260803",
        "title": {"sc": "AIA新加坡扩跨境医疗：马来就医免预付 34%担忧医疗开支", "tc": "AIA新加坡擴跨境醫療：馬來就醫免預付 34%擔憂醫療開支"},
        "summary": {"sc": "AIA新加坡8月起升级团体员工医疗保障：逾百万受保成员（约占当地劳动人口1/3）可凭LOG Plus在马国指定医院免预付治疗、牙科卡免垫付，公立医院专科免转介，并上线AIA+全数字预授权。AIA Live Better调研显示34%居民担忧医疗可负担性，反映集团跨境医疗与控费策略。[EN原文]", "tc": "AIA新加坡8月升級團體醫療：百萬成員可憑LOG Plus在馬國醫院免預付治療、牙科免墊付、專科免轉介，並推數字預授權；34%居民擔憂醫療開支，凸顯集團跨境醫療與控費策略。"},
        "why": {"sc": "AIA跨境医疗策略=友邦系产品与服务体系观察窗口（含内地客群关联）", "tc": "AIA跨境醫療策略=友邦系產品與服務體系觀察窗口（含內地客群關聯）"},
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 0, "midback": 1, "lead": 1, "cross": 2},
        "source": {"sc": "Insurance Asia / AIA", "tc": "Insurance Asia / AIA", "lang": "en"},
        "boards": ["insurer"], "themes": ["medical", "cross-border"],
        "tags": {"sc": ["AIA", "跨境医疗", "团体医疗", "医疗通胀"], "tc": ["AIA", "跨境醫療", "團體醫療", "醫療通脹"]},
        "contentKind": "news", "publishedAt": "2026-08-03T05:15:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/aia-expands-cross-border-care-34-fear-medical-costs"
    },
    {
        "id": "cyber-insurer-profit-aug03",
        "clusterCount": 1, "score": 70, "verifyStatus": "pending",
        "sourceTier": "pro", "sourceKey": "insuranceasia:cyber-profit-20260803",
        "title": {"sc": "AM Best/S&P：网安险2025全球保费破160亿美元 费率下行考验盈利", "tc": "AM Best/S&P：網安險2025全球保費破160億美元 費率下行考驗盈利"},
        "summary": {"sc": "AM Best与S&P同月报告网安险前景：2025年全球保费逾160亿美元，需求随数字化与数据保护法规增长，但竞争令费率走低；AM Best维持稳定展望，S&P警告市场接近转折点、费率续跌将侵蚀承保利润。2025年勒索攻击同比+30%至7419起，AI令攻击更易规模化。[EN原文]", "tc": "AM Best與S&P研判網安險：2025全球保費破160億美元，需求增長但費率下行；AM Best展望穩定，S&P警告接近轉折點；去年勒索攻擊+30%至7419起，AI令攻擊更易規模化。"},
        "why": {"sc": "网安险定价与AI风险=企业客户风险管理话题与市场情绪参照", "tc": "網安險定價與AI風險=企業客戶風險管理話題與市場情緒參照"},
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 0, "midback": 1, "lead": 1, "cross": 1},
        "source": {"sc": "Insurance Asia / AM Best·S&P", "tc": "Insurance Asia / AM Best·S&P", "lang": "en"},
        "boards": ["tech"], "themes": ["cyber", "pricing"],
        "tags": {"sc": ["网络安全险", "AM Best", "S&P", "勒索软件", "AI风险"], "tc": ["網絡安全險", "AM Best", "S&P", "勒索軟件", "AI風險"]},
        "contentKind": "news", "publishedAt": "2026-08-03T09:00:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/expert-opinion/can-cyber-insurers-stay-profitable"
    },
    {
        "id": "hkma-sme-credit-aug03",
        "clusterCount": 1, "score": 85, "verifyStatus": "verified",
        "sourceTier": "official", "sourceKey": "hkma:sme-credit-20260803",
        "title": {"sc": "HKMA：Q2中小企业信贷状况总体稳定 78%认为审批取态相近或更易", "tc": "HKMA：Q2中小企業信貸狀況總體穩定 78%認為審批取態相近或更易"},
        "summary": {"sc": "金管局8月3日公布Q2中小企业信贷状况调查：撇除无意见者，78%受访企业认为银行信贷审批取态与半年前相若或更宽松（上季73%），22%认为更困难（上季27%）；新申请成功获批率85%（上季91%），4%反映现有信贷额度收紧。调查覆盖约2500家中小企业，反映企业融资环境边际变化。[EN原文]", "tc": "金管局Q2中小企業信貸調查：78%認為銀行審批取態相近或更寬鬆（上季73%），新申請成功獲批率85%（上季91%）；信貸環境總體穩定但邊際轉緊，覆蓋約2500家中小企業。"},
        "why": {"sc": "企业信贷环境=中小企业主客户经营与融资需求的宏观参照", "tc": "企業信貸環境=中小企業主客戶經營與融資需求的宏觀參照"},
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 0, "midback": 1, "lead": 1, "cross": 0},
        "source": {"sc": "HKMA", "tc": "HKMA", "lang": "en"},
        "boards": ["market"], "themes": ["credit", "sme"],
        "tags": {"sc": ["HKMA", "中小企业", "信贷", "融资"], "tc": ["HKMA", "中小企業", "信貸", "融資"]},
        "contentKind": "stats", "publishedAt": "2026-08-03T16:00:00+08:00",
        "originalUrl": "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/08/20260803-4/"
    },
    {
        "id": "ia-mcv-definition-aug03",
        "clusterCount": 1, "score": 74, "verifyStatus": "pending",
        "sourceTier": "media", "sourceKey": "gmteight:ia-mcv-definition-20260803",
        "title": {"sc": "保监局拟重定义「内地访客」：非内地永久居民或可免赴港投保", "tc": "保監局擬重定義「內地訪客」：非內地永久居民或可免赴港投保"},
        "summary": {"sc": "据明报引述保监局执行董事梁志仁：保监局计划重新定义「内地访客」类别，拟允许非内地永久居民（如海外华侨）毋须亲身来港投保，以吸纳居港外的高净值客群；下季展开正式咨询，年内发布客户定义指引。新定义落地前，内地访客季度数据继续暂缓公布。[EN原文]", "tc": "據明報引述保監局執行董事：擬重定義「內地訪客」，允許非內地永久居民（如海外華僑）毋須親身赴港投保，以吸引海外高淨值客群；下季正式諮詢、年內出指引。新定義落地前內地訪客季度數據續暫緩公佈。"},
        "why": {"sc": "内地访客定义=直接改变MCV渠道规则与跨境投保流程，需重点跟进", "tc": "內地訪客定義=直接改變MCV渠道規則與跨境投保流程，需重點跟進"},
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 3, "midback": 2, "lead": 2, "cross": 3},
        "source": {"sc": "GMT EIGHT / 明报", "tc": "GMT EIGHT / 明報", "lang": "zh+en"},
        "boards": ["reg"], "themes": ["mainland-visitors", "regulation"],
        "tags": {"sc": ["内地访客", "MCV", "保监局", "跨境投保", "定义咨询"], "tc": ["內地訪客", "MCV", "保監局", "跨境投保", "定義諮詢"]},
        "contentKind": "news", "publishedAt": "2026-08-03T09:00:00+08:00",
        "originalUrl": "https://gmteight.com/flash/detail/1245979"
    },
    {
        "id": "goldman-aia-1h26-aug03",
        "clusterCount": 1, "score": 72, "verifyStatus": "pending",
        "sourceTier": "pro", "sourceKey": "aastocks:goldman-aia-20260803",
        "title": {"sc": "高盛维持友邦「买入」：料上半年NBV+15%至32.54亿美元", "tc": "高盛維持友邦「買入」：料上半年NBV+15%至32.54億美元"},
        "summary": {"sc": "高盛8月3日研报：预计友邦上半年新业务价值按实际汇率同比+15%至32.54亿美元，Q2增速放缓至12%（Q1为17%），主因香港高基数而非销售放缓；内地为增长最快市场（Q2按固定汇率+13%），泰国受投连险带动转正（+5%）；维持买入评级、目标价97港元，中报8月20日公布。[EN原文]", "tc": "高盛預計友邦上半年NBV按實際匯率+15%至32.54億美元，Q2放緩至12%（Q1為17%）主因香港高基數而非銷售放緩；內地最快（Q2+13%）、泰國轉正（+5%）；維持買入、目標價97港元，中報8月20日揭曉。"},
        "why": {"sc": "投行对友邦中报预期=港险龙头景气与高基数效应的交叉验证", "tc": "投行對友邦中報預期=港險龍頭景氣與高基數效應的交叉驗證"},
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 1, "midback": 1, "lead": 0, "cross": 0},
        "source": {"sc": "AASTOCKS / Goldman Sachs", "tc": "AASTOCKS / Goldman Sachs", "lang": "en"},
        "boards": ["insurer"], "themes": ["results", "valuation"],
        "tags": {"sc": ["友邦", "高盛", "新业务价值", "中报", "评级"], "tc": ["友邦", "高盛", "新業務價值", "中報", "評級"]},
        "contentKind": "news", "publishedAt": "2026-08-03T12:47:00+08:00",
        "originalUrl": "https://wdatacn.aastocks.com/en/stocks/news/aafn-con/NOW.1536225/latest-news/AAFN"
    }
]

# Load existing JSON
with open("data/live-items.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Check for duplicates
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

# Prepend to items
data["items"] = filtered + data["items"]

# Update meta
data["meta"]["generatedAt"] = NOW.isoformat()
data["meta"]["itemCount"] = len(data["items"])
data["meta"]["windowNote"] = {
    "sc": f"本库{len(data['items'])}条。今日新增{len(filtered)}条。",
    "tc": f"本庫{len(data['items'])}條。今日新增{len(filtered)}條。"
}
data["meta"]["asOf"] = "2026-08-03"

# Write back
with open("data/live-items.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Inserted {len(filtered)} new items. Total: {len(data['items'])}")
for item in filtered:
    print(f"  + {item['id']} [{item['sourceTier']}] {item['title']['sc'][:50]}")
