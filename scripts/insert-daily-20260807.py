#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert daily collected items into live-items.json (2026-08-07 slot)"""
import json
from datetime import datetime, timezone, timedelta

HKT = timezone(timedelta(hours=8))
NOW = datetime(2026, 8, 7, 6, 35, 0, tzinfo=HKT)

new_items = [
    {
        "id": "ia-tax-response-aug06",
        "clusterCount": 3, "score": 85, "verifyStatus": "verified",
        "sourceTier": "official", "sourceKey": "interface:ia-tax-response-20260806",
        "title": {"sc": "香港保监局回应「港险收益征税」：正密切注意内地税务安排新进展 吁勿过度解读", "tc": "香港保監局回應「港險收益徵稅」：正密切注意內地稅務安排新進展 籲勿過度解讀"},
        "summary": {"sc": "针对财新「境外保单收益按20%征税」报道，保监局8月6日独家回应界面新闻：正密切注意内地金融产品税务安排的最新发展，并与业界保持紧密沟通。局方强调，中国居民就境外投资收益依法申报及缴税的要求一直存在，市场不用过度解读或作出揣测。", "tc": "針對財新「境外保單收益按20%徵稅」報道，保監局8月6日獨家回應界面新聞：正密切注意內地金融產品稅務安排的最新發展，並與業界保持緊密溝通。局方強調，中國居民就境外投資收益依法申報及繳稅的要求一直存在，市場不用過度解讀或作出揣測。"},
        "why": {"sc": "官方首次就征税传闻正式表态，为恐慌市场提供权威定调：申报义务一直存在、个案不具普遍性。这是向客户解释「税务合规≠港险失效」最有力的官方依据，也是压过市场噪音的定盘星。", "tc": "官方首次就徵稅傳聞正式表態，為恐慌市場提供權威定調：申報義務一直存在、個案不具普遍性。這是向客戶解釋「稅務合規≠港險失效」最有力的官方依據，也是壓過市場噪音的定盤星。"},
        "actions": {"front": {"sc": "官方定调=恐慌后最权威的沟通依据", "tc": "官方定調=恐慌後最權威的溝通依據"}, "midback": {}, "lead": {"sc": "申报义务一直存在=合规叙事转向常态管理", "tc": "申報義務一直存在=合規敘事轉向常態管理"}, "cross": {"sc": "跨境税务合规需同步跟进", "tc": "跨境稅務合規需同步跟進"}},
        "rolesImpact": {"front": 3, "midback": 0, "lead": 2, "cross": 1},
        "source": {"sc": "界面新闻（东方财富转载）", "lang": "zh"},
        "boards": ["reg", "market"], "themes": ["compliance", "offshore"],
        "tags": {"sc": ["保监局", "境外保单征税", "官方回应", "税务合规"], "tc": ["保監局", "境外保單徵稅", "官方回應", "稅務合規"]},
        "contentKind": "news", "publishedAt": "2026-08-06T19:30:00+08:00",
        "originalUrl": "https://wap.eastmoney.com/a/202608063834049890.html"
    },
    {
        "id": "manulife-asia-q2-2026",
        "clusterCount": 1, "score": 75, "verifyStatus": "verified",
        "sourceTier": "insurer", "sourceKey": "insuranceasia:manulife-asia-q2-20260807",
        "title": {"sc": "宏利亚洲次季股东应占净利+28%至7.68亿美元 APE+21%至15亿美元", "tc": "宏利亞洲次季股東應佔淨利+28%至7.68億美元 APE+21%至15億美元"},
        "summary": {"sc": "InsuranceAsia报道，宏利亚洲Q2股东应占净利7.68亿美元按年+28%，核心盈利+21%至6.16亿美元；APE销售15亿美元+21%，新业务CSM+17%至5.61亿美元，新业务价值+13%至5.06亿美元。上半年净利+17%、NBV+14%。[EN原文]", "tc": "InsuranceAsia報道，宏利亞洲Q2股東應佔淨利7.68億美元按年+28%，核心盈利+21%至6.16億美元；APE銷售15億美元+21%，新業務CSM+17%至5.61億美元，新業務價值+13%至5.06億美元。上半年淨利+17%、NBV+14%。[EN原文]"},
        "why": {"sc": "昨日港澳数据之外补齐亚洲全景：MCV及本地需求动能延续至集团层面，为8月下旬友邦、保诚业绩季提供第二份对照样本；NBV+13%与CSM+17%显示未来利润储备持续增厚。", "tc": "昨日港澳數據之外補齊亞洲全景：MCV及本地需求動能延續至集團層面，為8月下旬友邦、保誠業績季提供第二份對照樣本；NBV+13%與CSM+17%顯示未來利潤儲備持續增厚。"},
        "actions": {"front": {"sc": "亚洲APE+21%=区域动能延续", "tc": "亞洲APE+21%=區域動能延續"}, "midback": {"sc": "新业务CSM+17%=未来利润增厚", "tc": "新業務CSM+17%=未來利潤增厚"}, "lead": {"sc": "业绩季对照样本+1", "tc": "業績季對照樣本+1"}, "cross": {}},
        "rolesImpact": {"front": 2, "midback": 1, "lead": 1, "cross": 0},
        "source": {"sc": "Insurance Asia", "lang": "en"},
        "boards": ["insurer"], "themes": ["firm", "results"],
        "tags": {"sc": ["宏利", "Q2业绩", "亚洲", "新业务价值"], "tc": ["宏利", "Q2業績", "亞洲", "新業務價值"]},
        "contentKind": "news", "publishedAt": "2026-08-07T06:20:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/manulifes-asia-business-sees-profit-soar-28-in-q2-2026"
    },
    {
        "id": "scmp-levy-next-steps-aug06",
        "clusterCount": 1, "score": 66, "verifyStatus": "pending",
        "sourceTier": "media", "sourceKey": "scmp:levy-reaction-20260806",
        "title": {"sc": "港险股消化征税报道后市场聚焦北京下一步 高盛指利润冲击或有限", "tc": "港險股消化徵稅報道後市場聚焦北京下一步 高盛指利潤衝擊或有限"},
        "summary": {"sc": "SCMP报道，20%征税报道令友邦、保诚、汇丰等港险股下挫后，投资者转而关注北京下一步政策动向；高盛认为利润影响可能有限。报道将观察焦点从单日抛售转向政策演进节奏，为后续跟踪提供坐标。[EN原文]", "tc": "SCMP報道，20%徵稅報道令友邦、保誠、匯豐等港險股下挫後，投資者轉而關注北京下一步政策動向；高盛認為利潤影響可能有限。報道將觀察焦點從單日拋售轉向政策演進節奏，為後續跟蹤提供座標。[EN原文]"},
        "why": {"sc": "英文主流媒体+外资行视角：把焦点从「已发生的抛售」转向「北京下一步」，提示政策演进节奏才是中期变量，与中文媒体叙事互补，适合作为客户沟通的平衡视角。", "tc": "英文主流媒體+外資行視角：把焦點從「已發生的拋售」轉向「北京下一步」，提示政策演進節奏才是中期變量，與中文媒體敘事互補，適合作為客戶溝通的平衡視角。"},
        "actions": {"front": {}, "midback": {}, "lead": {"sc": "北京下一步=中期变量观察点", "tc": "北京下一步=中期變量觀察點"}, "cross": {"sc": "政策演进节奏需持续跟踪", "tc": "政策演進節奏需持續跟蹤"}},
        "rolesImpact": {"front": 0, "midback": 0, "lead": 1, "cross": 1},
        "source": {"sc": "SCMP", "lang": "en"},
        "boards": ["market"], "themes": ["macro", "compliance"],
        "tags": {"sc": ["港险股", "征税", "高盛", "政策观察"], "tc": ["港險股", "徵稅", "高盛", "政策觀察"]},
        "contentKind": "news", "publishedAt": "2026-08-06T18:49:00+08:00",
        "originalUrl": "https://www.scmp.com/business/banking-finance/article/3363106/shares-major-hong-kong-insurance-finance-firms-tumble-following-report-20-levy"
    },
    {
        "id": "zurich-apac-h1-2026",
        "clusterCount": 1, "score": 64, "verifyStatus": "pending",
        "sourceTier": "media", "sourceKey": "insurancebusinessmag:zurich-apac-h1-20260806",
        "title": {"sc": "苏黎世亚太上半年经营利润+15%至3.48亿美元 香港投连险成增长引擎", "tc": "蘇黎世亞太上半年經營利潤+15%至3.48億美元 香港投連險成增長引擎"},
        "summary": {"sc": "Insurance Business报道，苏黎世亚太区上半年经营利润3.48亿美元按年+15%，跑赢集团13%增速；寿险经营利润+19%，投连险在日本和香港表现强劲，带动区域PVNBP按年+28%。亚太新业务利润率12.1%为集团最高，财险综合成本率94.0%。[EN原文]", "tc": "Insurance Business報道，蘇黎世亞太區上半年經營利潤3.48億美元按年+15%，跑贏集團13%增速；壽險經營利潤+19%，投連險在日本和香港表現強勁，帶動區域PVNBP按年+28%。亞太新業務利潤率12.1%為集團最高，財險綜合成本率94.0%。[EN原文]"},
        "why": {"sc": "香港投连险被点名为区域增长引擎之一，印证港险投连险回暖的结构性信号；苏黎世逆势加码亚洲，与国际巨头收缩形成对照，值得渠道与产品端关注。", "tc": "香港投連險被點名為區域增長引擎之一，印證港險投連險回暖的結構性信號；蘇黎世逆勢加碼亞洲，與國際巨頭收縮形成對照，值得渠道與產品端關注。"},
        "actions": {"front": {}, "midback": {}, "lead": {"sc": "投连险回暖=香港产品叙事新看点", "tc": "投連險回暖=香港產品敘事新看點"}, "cross": {"sc": "外资加码亚洲=竞争格局信号", "tc": "外資加碼亞洲=競爭格局信號"}},
        "rolesImpact": {"front": 0, "midback": 0, "lead": 1, "cross": 1},
        "source": {"sc": "Insurance Business", "lang": "en"},
        "boards": ["insurer", "market"], "themes": ["results", "product"],
        "tags": {"sc": ["苏黎世", "H1业绩", "投连险", "香港"], "tc": ["蘇黎世", "H1業績", "投連險", "香港"]},
        "contentKind": "news", "publishedAt": "2026-08-06T21:00:00+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/zurichs-asiapacific-business-operating-profit-rises-15-to-us348-million-in-h1-2026-585153.aspx"
    },
    {
        "id": "swissre-pnc-h1-2026",
        "clusterCount": 1, "score": 62, "verifyStatus": "pending",
        "sourceTier": "media", "sourceKey": "insurancebusinessmag:swissre-pnc-h1-20260806",
        "title": {"sc": "瑞再财险再保上半年综合成本率76.7% 年中续转定价缺口扩大", "tc": "瑞再財險再保上半年綜合成本率76.7% 年中續轉定價缺口擴大"},
        "summary": {"sc": "Insurance Business报道，温和损失环境下，瑞士再保险财险再保上半年综合成本率降至76.7%；但年中续转中名义定价与风险调整后定价出现分化、缺口扩大，再保市场费率拐点信号渐显。[EN原文]", "tc": "Insurance Business報道，溫和損失環境下，瑞士再保險財險再保上半年綜合成本率降至76.7%；但年中續轉中名義定價與風險調整後定價出現分化、缺口擴大，再保市場費率拐點信號漸顯。[EN原文]"},
        "why": {"sc": "再保定价分化是港险分保成本的前瞻信号：若缺口持续扩大，直保公司分保成本与承保策略将受影响，值得中后台与产品端跟踪。", "tc": "再保定價分化是港險分保成本的前瞻信號：若缺口持續擴大，直保公司分保成本與承保策略將受影響，值得中後台與產品端跟蹤。"},
        "actions": {"front": {}, "midback": {"sc": "再保定价分化=分保成本前瞻信号", "tc": "再保定價分化=分保成本前瞻信號"}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 0, "midback": 1, "lead": 0, "cross": 0},
        "source": {"sc": "Insurance Business", "lang": "en"},
        "boards": ["market"], "themes": ["reinsurance", "macro"],
        "tags": {"sc": ["瑞士再保险", "综合成本率", "再保定价"], "tc": ["瑞士再保險", "綜合成本率", "再保定價"]},
        "contentKind": "news", "publishedAt": "2026-08-06T20:00:00+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/swiss-re-pandc-hits-76-7-combined-ratio-but-pricing-gap-widens-585163.aspx"
    },
    {
        "id": "thailand-life-digital-channel-aug07",
        "clusterCount": 1, "score": 61, "verifyStatus": "pending",
        "sourceTier": "media", "sourceKey": "insurancebusinessmag:thailand-life-digital-20260807",
        "title": {"sc": "泰国寿险数字化直营渠道逼近代理人 监管改革同步推进", "tc": "泰國壽險數字化直營渠道逼近代理人 監管改革同步推進"},
        "summary": {"sc": "Insurance Business报道，泰国寿险直销数字渠道份额快速攀升、正逼近代理人渠道，同时伴随大规模监管改革落地。数字直营对传统代理模式的替代效应在东南亚加速显现，为港险渠道结构演变提供参照。[EN原文]", "tc": "Insurance Business報道，泰國壽險直銷數字渠道份額快速攀升、正逼近代理人渠道，同時伴隨大規模監管改革落地。數字直營對傳統代理模式的替代效應在東南亞加速顯現，為港險渠道結構演變提供參照。[EN原文]"},
        "why": {"sc": "渠道结构演变是港险长期议题：泰国案例显示「监管改革+数字直营」组合正改写分销版图，对香港代理人渠道与银保格局有对照意义。", "tc": "渠道結構演變是港險長期議題：泰國案例顯示「監管改革+數字直營」組合正改寫分銷版圖，對香港代理人渠道與銀保格局有對照意義。"},
        "actions": {"front": {"sc": "数字直营逼近代理=渠道洗牌信号", "tc": "數字直營逼近代理=渠道洗牌信號"}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 1, "midback": 0, "lead": 0, "cross": 0},
        "source": {"sc": "Insurance Business", "lang": "en"},
        "boards": ["tech"], "themes": ["distribution", "insurtech"],
        "tags": {"sc": ["泰国", "数字渠道", "代理人", "监管改革"], "tc": ["泰國", "數字渠道", "代理人", "監管改革"]},
        "contentKind": "news", "publishedAt": "2026-08-07T05:00:00+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/life-insurance/thailands-life-insurance-digital-channel-is-closing-in-on-agents-585257.aspx"
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
data["meta"]["asOf"] = "2026-08-07"

with open("data/live-items.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Inserted {len(filtered)} new items. Total: {len(data['items'])}")
for item in filtered:
    print(f"  + {item['id']} [{item['sourceTier']}] {item['title']['sc'][:50]}")
