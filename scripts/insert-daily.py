#!/usr/bin/env python3
"""Insert daily collected items into live-items.json (2026-08-02 batch)"""
import json
from datetime import datetime, timezone, timedelta

HKT = timezone(timedelta(hours=8))
NOW = datetime(2026, 8, 2, 23, 30, 0, tzinfo=HKT)

new_items = [
    {
        "id": "ia-commission-caps-jul30",
        "clusterCount": 1, "score": 78, "verifyStatus": "pending",
        "sourceTier": "pro", "sourceKey": "insuranceasia:creditsights-commission-20260730",
        "title": {"sc": "CreditSights：香港寿险新规重塑竞争格局 渠道强者受益", "tc": "CreditSights：香港壽險新規重塑競爭格局 渠道強者受益"},
        "summary": {"sc": "CreditSights报告指出，香港寿险市场在2024-2025年持续强劲增长，内地访客需求2025年显著回暖。报告分析多项监管新规对市场的影响：分红保单演示利率设限、首年佣金设限及转介费设限等措施，将利好拥有成熟代理及银保网络、产品久期较长、分销质量较高的保险公司。同时风险为本资本制度促使保司增配优质固收资产，基建类投资获资本优惠。[EN原文]", "tc": "CreditSights報告分析香港壽險新規：演示利率及佣金設限，利好渠道強、久期長、分銷質素高的保司；RBC促增配優質固收。"},
        "why": {"sc": "新规下的赢家逻辑=IFA选择合作保司与产品的重要参考", "tc": "新規下的贏家邏輯=IFA選擇合作保司與產品的重要參考"},
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 2, "midback": 1, "lead": 0, "cross": 0},
        "source": {"sc": "Insurance Asia / CreditSights", "tc": "Insurance Asia / CreditSights", "lang": "en"},
        "boards": ["reg"], "themes": ["commission", "regulation"],
        "tags": {"sc": ["佣金上限", "演示利率", "CreditSights", "RBC", "竞争格局"], "tc": ["佣金上限", "演示利率", "CreditSights", "RBC", "競爭格局"]},
        "contentKind": "news", "publishedAt": "2026-07-30T06:30:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/hong-kong-caps-commissions-life-insurers-compete"
    },
    {
        "id": "jll-tsim-vacancy-aug01",
        "clusterCount": 1, "score": 68, "verifyStatus": "pending",
        "sourceTier": "media", "sourceKey": "insuranceasia:jll-tsim-20260801",
        "title": {"sc": "内地保司租务推动尖沙咀甲级写字楼空置率降至6.7%", "tc": "內地保司租務推動尖沙咀甲級寫字樓空置率降至6.7%"},
        "summary": {"sc": "仲量联行（JLL）最新报告显示，内地保险及财富管理公司在港扩张租赁需求强劲，推动尖沙咀甲级写字楼空置率6月底降至6.7%，较上月降0.4个百分点，较2022年9月11.2%的峰值大幅回落。One Peking 6月首次实现100%入驻。全港写字楼空置率降至13.1%，RGA再保险租下太古坊全层2.35万平方呎。[EN原文]", "tc": "JLL報告：內地保司及財管公司租務推動尖沙咀空置率降至6.7%，One Peking全數入駐，反映行業擴張實體需求。"},
        "why": {"sc": "内地资金+保司实体扩张落地香港=行业景气与人才流向的交叉验证", "tc": "內地資金+保司實體擴張落地香港=行業景氣與人才流向的交叉驗證"},
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 0, "midback": 0, "lead": 1, "cross": 1},
        "source": {"sc": "Insurance Asia / JLL", "tc": "Insurance Asia / JLL", "lang": "en"},
        "boards": ["market"], "themes": ["property", "mainland-wealth"],
        "tags": {"sc": ["尖沙咀", "写字楼", "JLL", "内地保司", "租赁"], "tc": ["尖沙咀", "寫字樓", "JLL", "內地保司", "租賃"]},
        "contentKind": "news", "publishedAt": "2026-08-01T05:00:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/mainland-insurers-drive-tsimshatsui-vacancy-down-67"
    },
    {
        "id": "msig-claims-947-jul30",
        "clusterCount": 1, "score": 75, "verifyStatus": "pending",
        "sourceTier": "insurer", "sourceKey": "msig:claims-2025-20260730",
        "title": {"sc": "MSIG香港2025年理赔结案率升至94.7% 连续五年改善", "tc": "MSIG香港2025年理賠結案率升至94.7% 連續五年改善"},
        "summary": {"sc": "MSIG保险（香港）2025年理赔报告显示，全年结案率升至94.7%，较2020年的91.1%连续第五年提升；2025年在香港及澳门共赔付3.59亿港元。雇员补偿保险结案率最高达99.87%，家佣保险97.57%，旅游保险96.27%。客户表扬按年增11%，2025年所有Google评价均为五星。[EN原文]", "tc": "MSIG香港2025理賠結案率94.7%連續五年改善，港澳共賠$3.59億；僱傭補償結案率99.87%最高。"},
        "why": {"sc": "理赔结案率=客户转介绍与续保的说服力素材", "tc": "理賠結案率=客戶轉介紹與續保的說服力素材"},
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 1, "midback": 0, "lead": 0, "cross": 0},
        "source": {"sc": "Insurance Asia / MSIG", "tc": "Insurance Asia / MSIG", "lang": "en"},
        "boards": ["insurer"], "themes": ["claims", "customer"],
        "tags": {"sc": ["MSIG", "理赔", "结案率", "客户服务"], "tc": ["MSIG", "理賠", "結案率", "客戶服務"]},
        "contentKind": "news", "publishedAt": "2026-07-30T06:15:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/msig-lifts-claims-settlement-ratio-947"
    },
    {
        "id": "hkma-monetary-stats-jun26",
        "clusterCount": 1, "score": 85, "verifyStatus": "verified",
        "sourceTier": "official", "sourceKey": "hkma:monetary-stats-202606",
        "title": {"sc": "HKMA公布6月货币统计：港元货币供应与贷款趋势", "tc": "HKMA公佈6月貨幣統計：港元貨幣供應與貸款趨勢"},
        "summary": {"sc": "香港金管局7月31日公布2026年6月货币统计数据，涵盖港元及外币货币供应量、认可机构存款与贷款变化。货币统计反映整体流动性环境，是评估保费融资成本、银行信贷取向及港元利率走势的重要宏观参照。[EN原文]", "tc": "金管局公佈6月貨幣統計，涵蓋貨幣供應、存款與貸款變化，為評估保費融資環境與利率走勢的宏觀參照。"},
        "why": {"sc": "货币与信贷环境=保费融资成本与储蓄险销售节奏的宏观底色", "tc": "貨幣與信貸環境=保費融資成本與儲蓄險銷售節奏的宏觀底色"},
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 0, "midback": 1, "lead": 0, "cross": 0},
        "source": {"sc": "HKMA", "tc": "HKMA", "lang": "en"},
        "boards": ["market"], "themes": ["monetary", "liquidity"],
        "tags": {"sc": ["HKMA", "货币统计", "货币供应", "贷款"], "tc": ["HKMA", "貨幣統計", "貨幣供應", "貸款"]},
        "contentKind": "stats", "publishedAt": "2026-07-31T16:00:00+08:00",
        "originalUrl": "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/07/20260731-7/"
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
data["meta"]["asOf"] = "2026-08-02"

# Write back
with open("data/live-items.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Inserted {len(filtered)} new items. Total: {len(data['items'])}")
for item in filtered:
    print(f"  + {item['id']} [{item['sourceTier']}] {item['title']['sc'][:50]}")
