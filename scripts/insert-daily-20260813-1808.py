#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert daily collected items (2026-08-13 18:08 run) into live-items.json + update last-check.json."""
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
    # 1. SCMP Opinion: Beijing's offshore insurance tax tests HK wealth management (Aug 13 16:30)
    item(
        "scmp-offshore-tax-opinion-20260813", 68, "verified", "media",
        "scmp:offshore-tax-opinion-20260813",
        "南华早报评论：港险征税风波考验香港财富管理 税务总局称20%税率非新政非针对香港",
        "南華早報評論：港險徵稅風波考驗香港財富管理 稅務總局稱20%稅率非新政非針對香港",
        "南华早报评论指，财新报道北京、杭州对内地居民香港保单收益执行征税后市场连日波动，事件意义比初时反应更复杂。国家税务总局回应：20%税率并非新政策、并非针对香港，呼吁勿过度解读；真正的问题是既有规则会否随CRS数据交换获得更系统性执行。2024年内地访客新造保费628亿港元、占香港个人新单28.6%，香港2024年底管理资产35.1万亿港元，征税执行力度直接牵动港险与财富管理生态。[EN原文]",
        "南華早報評論指，財新報道北京、杭州對內地居民香港保單收益執行徵稅後市場連日波動，事件意義比初時反應更複雜。國家稅務總局回應：20%稅率並非新政策、並非針對香港，呼籲勿過度解讀；真正的問題是既有規則會否隨CRS數據交換獲得更系統性執行。2024年內地訪客新造保費628億港元、佔香港個人新單28.6%，香港2024年底管理資產35.1萬億港元，徵稅執行力度直接牽動港險與財富管理生態。",
        "从监管表态到市场体量数据，系统梳理港险征税事件的来龙去脉与后续观察点，是高净值客户沟通与展业话术的权威参考。",
        "從監管表態到市場體量數據，系統梳理港險徵稅事件的來龍去脈與後續觀察點，是高淨值客戶溝通與展業話術的權威參考。",
        {"front": L("征税执行节奏=客户预期管理", "徵稅執行節奏=客戶預期管理"), "midback": {}, "lead": {}, "cross": L("CRS数据交换放大征管=合规提示", "CRS數據交換放大徵管=合規提示")},
        {"front": 2, "midback": 1, "lead": 1, "cross": 3},
        "SCMP 南华早报", "en",
        ["market"], ["taxation", "cross-border"],
        ["港险征税", "税务总局", "内地访客", "财富管理", "CRS"], ["港險徵稅", "稅務總局", "內地訪客", "財富管理", "CRS"],
        "news", "2026-08-13T16:30:07+08:00",
        "https://www.scmp.com/opinion/hong-kong-opinion/article/3363670/beijings-offshore-insurance-tax-tests-hong-kong-wealth-management",
    ),
    # 2. InsuranceAsia: HK insurers slide as China tightens tax enforcement — CGS quantification (Aug 13 05:00)
    item(
        "insuranceasia-hk-insurers-slide-tax-20260813", 66, "verified", "media",
        "insuranceasia:hk-insurers-slide-tax-20260813",
        "InsuranceAsia：友邦保诚因征税传闻重挫后 分析师称市场反应过度 MCV敞口仅占新业务价值两成",
        "InsuranceAsia：友邦保誠因徵稅傳聞重挫後 分析師稱市場反應過度 MCV敞口僅佔新業務價值兩成",
        "InsuranceAsia引述CGS International研报：8月6日友邦收跌5.9%至73.15港元、保诚跌4.6%至108.5港元后，分析师认为市场对内地港险征税反应过度并维持正面看法。CGS估算内地访客(MCV)业务约占友邦FY25集团新业务价值20%、保诚22%；按股价跌幅简单推算，市场已计入友邦MCV业务约三成、保诚约两成的损失。Fitch旗下CreditSights持相似观点，将征税执行定性为区域差异化的渐进过程。[EN原文]",
        "InsuranceAsia引述CGS International研報：8月6日友邦收跌5.9%至73.15港元、保誠跌4.6%至108.5港元後，分析師認為市場對內地港險徵稅反應過度並維持正面看法。CGS估算內地訪客(MCV)業務約佔友邦FY25集團新業務價值20%、保誠22%；按股價跌幅簡單推算，市場已計入友邦MCV業務約三成、保誠約兩成的損失。Fitch旗下CreditSights持相似觀點，將徵稅執行定性為區域差異化的漸進過程。",
        "提供征税冲击的量化视角（MCV占新业务价值比重与股价隐含损失），帮助客观评估友邦、保诚等港险龙头的实际敞口与估值。",
        "提供徵稅衝擊的量化視角（MCV佔新業務價值比重與股價隱含損失），幫助客觀評估友邦、保誠等港險龍頭的實際敞口與估值。",
        {"front": {}, "midback": L("VONB敞口量化=估值参考", "VONB敞口量化=估值參考"), "lead": L("MCV依赖度=选品与渠道提示", "MCV依賴度=選品與渠道提示"), "cross": {}},
        {"front": 1, "midback": 2, "lead": 2, "cross": 1},
        "InsuranceAsia", "en",
        ["market"], ["taxation", "firm"],
        ["港险征税", "友邦", "保诚", "新业务价值", "CGS"], ["港險徵稅", "友邦", "保誠", "新業務價值", "CGS"],
        "news", "2026-08-13T05:00:00+08:00",
        "https://insuranceasia.com/insurance/in-focus/hong-kong-insurers-slide-china-tightens-tax-enforcement",
    ),
    # 3. 南方都市报: 离岸信托避税通道被封堵 宗馥莉家族陷补税争议 (Aug 13 07:45)
    item(
        "nandu-offshore-trust-case-20260813", 63, "verified", "media",
        "toutiao:nandu-offshore-trust-20260813",
        "离岸信托「避税通道」被封堵：宗馥莉家族陷补税争议 涉18亿美元汇丰账户资产",
        "離岸信託「避稅通道」被封堵：宗馥莉家族陷補稅爭議 涉18億美元滙豐賬戶資產",
        "南方都市报报道：香港高院上诉庭7月21日驳回宗馥莉一方上诉许可申请，娃哈哈创始人宗庆后遗产纠纷涉约18亿美元的汇丰银行账户继续冻结至杭州中院诉讼审结。财政部、税务总局7月24日发布《关于离岸信托个人所得税有关事项的公告》后，若该资产被认定为离岸信托，宗馥莉家族将面临补税。报道将离岸信托征税与港险收益征税并列为内地收紧境外财富征管的同一浪潮。",
        "南方都市報報道：香港高院上訴庭7月21日駁回宗馥莉一方上訴許可申請，娃哈哈創始人宗慶後遺產糾紛涉約18億美元的滙豐銀行賬戶繼續凍結至杭州中院訴訟審結。財政部、稅務總局7月24日發佈《關於離岸信託個人所得稅有關事項的公告》後，若該資產被認定為離岸信託，宗馥莉家族將面臨補稅。報道將離岸信託徵稅與港險收益徵稅並列為內地收緊境外財富徵管的同一浪潮。",
        "离岸信托个税新规落地后的首个标志性争议案例，直接关系高净值客户家族信托与境外架构规划，与港险征税同源同向，具强警示意义。",
        "離岸信託個稅新規落地後的首個標誌性爭議案例，直接關係高淨值客戶家族信託與境外架構規劃，與港險徵稅同源同向，具強警示意義。",
        {"front": {}, "midback": {}, "lead": L("离岸信托征管案例=家办客户警示", "離岸信託徵管案例=家辦客戶警示"), "cross": L("境外财富征管浪潮=税务规划联动", "境外財富徵管浪潮=稅務規劃聯動")},
        {"front": 1, "midback": 1, "lead": 2, "cross": 2},
        "南方都市报（今日头条）", "zh",
        ["family"], ["taxation", "offshore"],
        ["离岸信托", "宗馥莉", "补税", "娃哈哈", "境外财富"], ["離岸信託", "宗馥莉", "補稅", "娃哈哈", "境外財富"],
        "news", "2026-08-13T07:45:06+08:00",
        "http://m.toutiao.com/group/7673295310735360546/",
    ),
]

# ---- insert into live-items.json ----
data = json.loads(LIVE.read_text(encoding='utf-8'))
existing_keys = {it.get('sourceKey') for it in data['items']}
added = []
for it in new_items:
    if it['sourceKey'] in existing_keys:
        print(f"SKIP duplicate: {it['sourceKey']}")
        continue
    added.append(it)
    existing_keys.add(it['sourceKey'])

data['items'] = added + data['items']
data['meta']['generatedAt'] = INGESTED
data['meta']['itemCount'] = len(data['items'])
LIVE.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding='utf-8')
print(f"Inserted {len(added)} items. Total: {len(data['items'])}")

# ---- update last-check.json (checkpoint mechanism) ----
now = datetime.now(HKT).isoformat(timespec='seconds')
lc = json.loads(LASTCHECK.read_text(encoding='utf-8'))
lc['lastCheck'] = now
for key, src in lc['sources'].items():
    src['last'] = now
LASTCHECK.write_text(json.dumps(lc, ensure_ascii=False, indent=2) + "\n", encoding='utf-8')
print("last-check.json updated ->", now)
