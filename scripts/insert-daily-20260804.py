#!/usr/bin/env python3
"""Insert daily collected items into live-items.json (2026-08-04 batch)"""
import json
from datetime import datetime, timezone, timedelta

HKT = timezone(timedelta(hours=8))
NOW = datetime.now(HKT)

new_items = [
    {
        "id": "prudential-eason-brand-aug03",
        "clusterCount": 1, "score": 75, "verifyStatus": "verified",
        "sourceTier": "insurer", "sourceKey": "prudential:eason-brand-20260803",
        "title": {"sc": "保诚推全新品牌企划「诚诺，实现您心」 陈奕迅任品牌代言人", "tc": "保誠推全新品牌企劃「誠諾，實現您心」 陳奕迅任品牌代言人"},
        "summary": {"sc": "保诚8月3日宣布推出亚洲区品牌企划「诚诺，实现您心」，由香港歌手兼演员陈奕迅担任品牌代言人，核心信息为「每一份保单都代表一个承诺」；香港市场将通过数码平台、社交媒体、电视及户外广告全面铺开，影片7月30日已首播，8月中旬起加大投放。保诚集团全球服务逾1700万客户。", "tc": "保誠8月3日宣佈推出亞洲區品牌企劃「誠諾，實現您心」，由陳奕迅擔任品牌代言人，核心信息為「每一份保單都代表一個承諾」；香港市場將透過數碼平台、社交媒體、電視及戶外廣告全面鋪開，影片7月30日已首播，8月中旬起加大投放。"},
        "why": {"sc": "头部保司押注情感化品牌传播=高净值客群信任建设与渠道获客风向标", "tc": "頭部保司押注情感化品牌傳播=高淨值客群信任建設與渠道獲客風向標"},
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 1, "midback": 1, "lead": 1, "cross": 0},
        "source": {"sc": "保诚香港", "tc": "保誠香港", "lang": "zh"},
        "boards": ["insurer"], "themes": ["brand", "marketing"],
        "tags": {"sc": ["保诚", "陈奕迅", "品牌企划", "市场推广"], "tc": ["保誠", "陳奕迅", "品牌企劃", "市場推廣"]},
        "contentKind": "press", "publishedAt": "2026-08-03T10:00:00+08:00",
        "originalUrl": "https://www.prudential.com.hk/tc/about-us/newsroom/prudential-launches-new-brand-campaign-featuring-eason-chan/"
    },
    {
        "id": "sg-captive-pcc-aug04",
        "clusterCount": 1, "score": 68, "verifyStatus": "pending",
        "sourceTier": "media", "sourceKey": "insuranceasia:sg-captive-pcc-20260804",
        "title": {"sc": "新加坡拟推保护型细胞公司框架 专属自保保险向中型企业开放", "tc": "新加坡擬推保護型細胞公司框架 專屬自保保險向中型企業開放"},
        "summary": {"sc": "新加坡拟议的保护型细胞公司（PCC）框架，允许多个专属自保计划共用同一法律实体，有望令专属自保保险对中型企业开放。新加坡正发力抢攻自保市场，与香港在亚太专属自保中心地位上的竞争进一步升温，值得关注其对香港自保业务的分流影响。[EN原文]", "tc": "新加坡擬議的保護型細胞公司（PCC）框架，允許多個專屬自保計劃共用同一法律實體，有望令專屬自保保險對中型企業開放；與香港在亞太自保中心地位上的競爭進一步升溫。"},
        "why": {"sc": "新加坡自保政策提速=香港专属自保中心竞争力的直接参照系", "tc": "新加坡自保政策提速=香港專屬自保中心競爭力的直接參照系"},
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 0, "midback": 1, "lead": 2, "cross": 2},
        "source": {"sc": "Insurance Asia", "tc": "Insurance Asia", "lang": "en"},
        "boards": ["market"], "themes": ["captive", "competition"],
        "tags": {"sc": ["新加坡", "专属自保", "PCC", "保险中心"], "tc": ["新加坡", "專屬自保", "PCC", "保險中心"]},
        "contentKind": "news", "publishedAt": "2026-08-04T06:00:00+08:00",
        "originalUrl": "https://insuranceasia.com/exclusive/singapore-targets-captive-insurance-growth"
    },
    {
        "id": "msig-cyber-sme-aug04",
        "clusterCount": 1, "score": 65, "verifyStatus": "pending",
        "sourceTier": "media", "sourceKey": "insuranceasia:msig-cyber-sme-20260804",
        "title": {"sc": "MSIG为中小企业增网安保障 保单捆绑威胁监测与应急响应", "tc": "MSIG為中小企業增網安保障 保單捆綁威脅監測與應急響應"},
        "summary": {"sc": "三井住友保险（MSIG）面向中小企业推出网安保险升级，将威胁监测与事件响应服务直接捆绑进保单，填补中小企业在安全人力与工具上的资源缺口；中小企网安资源不足仍是此类保障渗透率提升的主要障碍，保险公司正以「保险+服务」模式切入。[EN原文]", "tc": "三井住友保險（MSIG）面向中小企業推出網安保險升級，將威脅監測與事件響應服務直接捆綁進保單，填補中小企在安全人力與工具上的資源缺口。"},
        "why": {"sc": "「保险+安全服务」捆绑模式=中小企网安险渗透路径的行业样本", "tc": "「保險+安全服務」捆綁模式=中小企網安險滲透路徑的行業樣本"},
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 0, "midback": 1, "lead": 1, "cross": 1},
        "source": {"sc": "Insurance Asia / MSIG", "tc": "Insurance Asia / MSIG", "lang": "en"},
        "boards": ["tech"], "themes": ["cyber", "sme"],
        "tags": {"sc": ["MSIG", "网络安全险", "中小企业", "捆绑服务"], "tc": ["MSIG", "網絡安全險", "中小企業", "捆綁服務"]},
        "contentKind": "news", "publishedAt": "2026-08-04T06:00:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/msig-adds-cyber-cover-small-firms-face-resource-gaps"
    },
    {
        "id": "moodys-ai-distribution-aug04",
        "clusterCount": 1, "score": 66, "verifyStatus": "verified",
        "sourceTier": "media", "sourceKey": "insurancebusinessmag:moodys-ai-distribution-20260804",
        "title": {"sc": "Moody's：零售财险分销是全金融业最受AI冲击环节 限期12-18个月", "tc": "Moody's：零售財險分銷是全金融業最受AI衝擊環節 限期12-18個月"},
        "summary": {"sc": "穆迪报告指零售产险分销因交易量大、流程标准化、产品商品化，是金融业中最受AI近端冲击的业务线；AI将压缩客户与机构之间的信息差，比价、风险评估等顾问服务可被客户自行复制。具转换成本、专精复杂风险与问责信任关系的分销商仍可保定价权，基线情景下多数公司须在12-18个月内行动，中型公司最脆弱。[EN原文]", "tc": "穆迪報告指零售產險分銷是最受AI近端衝擊的金融業務線，AI將壓縮信息差、客戶可自行複製比價與風險評估；具轉換成本與專精複雜風險者仍可保定價權，多數公司須在12-18個月內行動，中型公司最脆弱。"},
        "why": {"sc": "评级机构对AI冲击分销渠道的量化判断=渠道转型与获客模式的前瞻参照", "tc": "評級機構對AI衝擊分銷渠道的量化判斷=渠道轉型與獲客模式的前瞻參照"},
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 3, "midback": 2, "lead": 1, "cross": 1},
        "source": {"sc": "Insurance Business / Moody's", "tc": "Insurance Business / Moody's", "lang": "en"},
        "boards": ["tech"], "themes": ["ai", "distribution"],
        "tags": {"sc": ["Moody's", "AI", "分销渠道", "财险", "转型"], "tc": ["Moody's", "AI", "分銷渠道", "財險", "轉型"]},
        "contentKind": "news", "publishedAt": "2026-08-04T10:00:00+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/technology/moodys-retail-pandc-distribution-faces-the-fastest-ai-disruption-of-any-financial-services-segment-584750.aspx"
    },
    {
        "id": "hk-plan-rename-aug04",
        "clusterCount": 1, "score": 62, "verifyStatus": "pending",
        "sourceTier": "media", "sourceKey": "qqnews:plan-rename-20260804",
        "title": {"sc": "港险产品集中更名：保诚20款产品8月24日启用新名 友邦中银人寿跟进", "tc": "港險產品集中更名：保誠20款產品8月24日啟用新名 友邦中銀人壽跟進"},
        "summary": {"sc": "按保监局与金管局2025年9月联合规定，具储蓄功能保险产品名称须包含「保险」或「Insurance」，以防消费者误认作银行存款；保诚20款在售产品将于8月24日启用新名称、9月初寄送通知函及保单批单，友邦、中银人寿同步跟进。属合规更名，保障、条款、缴费均不变，客户无需操作，市场「停售」传闻系过度解读。", "tc": "按保監局與金管局2025年9月聯合規定，具儲蓄功能保險產品名稱須包含「保險」或「Insurance」；保誠20款在售產品8月24日啟用新名稱，友邦、中銀人壽跟進；屬合規更名，保障條款不變，客戶無需操作，「停售」傳聞係過度解讀。"},
        "why": {"sc": "产品更名合规潮=回应客户「停售恐慌」、理解储蓄险监管命名规则的必备话术", "tc": "產品更名合規潮=回應客戶「停售恐慌」、理解儲蓄險監管命名規則的必備話術"},
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 2, "midback": 1, "lead": 1, "cross": 0},
        "source": {"sc": "腾讯新闻", "tc": "騰訊新聞", "lang": "zh"},
        "boards": ["reg"], "themes": ["compliance", "product"],
        "tags": {"sc": ["产品更名", "保监局", "金管局", "储蓄险", "合规"], "tc": ["產品更名", "保監局", "金管局", "儲蓄險", "合規"]},
        "contentKind": "news", "publishedAt": "2026-08-04T08:02:00+08:00",
        "originalUrl": "http://news.qq.com/rain/a/20260804A042W600"
    },
    {
        "id": "aon-indonesia-ceo-aug04",
        "clusterCount": 1, "score": 60, "verifyStatus": "pending",
        "sourceTier": "media", "sourceKey": "insuranceasia:aon-indonesia-ceo-20260804",
        "title": {"sc": "Aon委任Stephen出任印尼业务CEO 前Zurich印尼首席核保官", "tc": "Aon委任Stephen出任印尼業務CEO 前Zurich印尼首席核保官"},
        "summary": {"sc": "怡安（Aon）宣布委任Stephen出任印尼业务首席执行官，其此前担任Zurich印尼业务首席核保官，具备承保与市场管理双重背景。此举反映怡安持续强化东南亚市场领导层布局，为区域内经纪渠道竞争格局再添变量。[EN原文]", "tc": "怡安（Aon）委任Stephen出任印尼業務CEO，其此前擔任Zurich印尼首席核保官；反映怡安持續強化東南亞市場領導層佈局，為區域經紀渠道競爭格局再添變量。"},
        "why": {"sc": "国际经纪商东南亚人事布局=区域分销渠道竞争态势的观察点", "tc": "國際經紀商東南亞人事佈局=區域分銷渠道競爭態勢的觀察點"},
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 0, "midback": 1, "lead": 1, "cross": 1},
        "source": {"sc": "Insurance Asia / Aon", "tc": "Insurance Asia / Aon", "lang": "en"},
        "boards": ["market"], "themes": ["talent", "channel"],
        "tags": {"sc": ["Aon", "印尼", "人事任命", "经纪"], "tc": ["Aon", "印尼", "人事任命", "經紀"]},
        "contentKind": "news", "publishedAt": "2026-08-04T12:17:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/aon-names-stephen-new-ceo-indonesia-business"
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
data["meta"]["asOf"] = "2026-08-04"

# Write back
with open("data/live-items.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Inserted {len(filtered)} new items. Total: {len(data['items'])}")
for item in filtered:
    print(f"  + {item['id']} [{item['sourceTier']}] {item['title']['sc'][:50]}")
