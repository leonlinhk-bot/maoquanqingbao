#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert daily collected items (2026-08-12 18:08 run) into live-items.json + update last-check.json."""
import json
from pathlib import Path
from datetime import datetime, timezone, timedelta

ROOT = Path(__file__).resolve().parent.parent
LIVE = ROOT / 'data/live-items.json'
LASTCHECK = ROOT / 'data/last-check.json'
INGESTED = "2026-08-12T18:08:00+08:00"
HKT = timezone(timedelta(hours=8))

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
    # 1. 21世纪经济报道: ST official 3-point response + tax framework (3 scenarios)
    item(
        "21jingji-hk-tax-framework-20260811", 70, "verified", "media",
        "21jingji:hk-tax-framework-20260811",
        "税务总局回应港险征税：非新政策非针对保险 律师拆解退保/分红/理赔三种税务处理",
        "稅務總局回應港險徵稅：非新政策非針對保險 律師拆解退保/分紅/理賠三種稅務處理",
        "21世纪经济报道联系国家税务总局，相关司局负责人三点回应：境外保险收益属全球所得纳税范畴、并非新政策、更非针对香港保险，规范境外所得税收管理旨在防范跨境逃避税。报道梳理三种资金出口的税务处理：退保增值部分按20%征税、分红提取大概率按20%、身故理赔免税；并披露2026年一季度香港长期业务新单保费1411亿港元、同比大涨51%。",
        "21世紀經濟報道聯繫國家稅務總局，相關司局負責人三點回應：境外保險收益屬全球所得納稅範疇、並非新政策、更非針對香港保險，規範境外所得稅收管理旨在防範跨境逃避稅。報道梳理三種資金出口的稅務處理：退保增值部分按20%徵稅、分紅提取大概率按20%、身故理賠免稅；並披露2026年一季度香港長期業務新單保費1411億港元、同比大漲51%。",
        "征税从「个案」走向「框架」的标志性报道：官方口径（非新政策）+律师拆解的三种情形税务处理，是 IFA 与客户沟通境外保单税务时必须掌握的话术与事实基础。",
        "徵稅從「個案」走向「框架」的標誌性報道：官方口徑（非新政策）+律師拆解的三種情形稅務處理，是 IFA 與客戶溝通境外保單稅務時必須掌握的話術與事實基礎。",
        {"front": L("三种情形税务框架=客户沟通实操", "三種情形稅務框架=客戶溝通實操"), "midback": L("官方口径=合规答复依据", "官方口徑=合規答覆依據"), "lead": {}, "cross": L("征税框架影响跨境架构税务评估", "徵稅框架影響跨境架構稅務評估")},
        {"front": 3, "midback": 3, "lead": 2, "cross": 3},
        "21世纪经济报道（南方财经）", "zh",
        ["reg", "market"], ["taxation", "cross-border", "compliance"],
        ["港险征税", "税务总局", "退保", "分红", "理赔"], ["港險徵稅", "稅務總局", "退保", "分紅", "理賠"],
        "news", "2026-08-11T18:50:42+08:00",
        "http://m.toutiao.com/group/7672724709955600930/",
    ),
    # 2. 观潮财经: mainland participating (分红险) premium exceeds 1 trillion in H1
    item(
        "toutiao-participating-1trillion-20260811", 66, "verified", "media",
        "toutiao:guanchao-participating-1trillion-20260811",
        "内地分红险半年保费破万亿 同比增94.4% 占比首破35%",
        "內地分紅險半年保費破萬億 同比增94.4% 佔比首破35%",
        "中保协数据显示2026上半年内地分红险原保险保费收入10126亿元，同比暴增94.4%，半年规模即超2024全年（7659亿）与2025全年（9042亿），占人身险总保费比重突破35%；同期人身险整体保费增速仅3.6%。50家人身险公司前五大主力产品中分红险保费占45.47%，太平、太平等公司新单分红占比超50%。",
        "中保協數據顯示2026上半年內地分紅險原保險保費收入10126億元，同比暴增94.4%，半年規模即超2024全年與2025全年，佔人身險總保費比重突破35%；同期人身險整體保費增速僅3.6%。50家人身險公司前五大主力產品中分紅險保費佔45.47%，太平、太平等公司新單分紅佔比超50%。",
        "低利率时代内地险企集体转向「保底+浮动」分红险，与港险分红储蓄产品形成直接竞争与配置参照，是判断内地客户需求与渠道话术的重要宏观背景。",
        "低利率時代內地險企集體轉向「保底+浮動」分紅險，與港險分紅儲蓄產品形成直接競爭與配置參照，是判斷內地客戶需求與渠道話術的重要宏觀背景。",
        {"front": L("内地分红险放量=港险竞争参照", "內地分紅險放量=港險競爭參照"), "midback": {}, "lead": {}, "cross": {}},
        {"front": 2, "midback": 1, "lead": 1, "cross": 1},
        "观潮财经（今日头条·新浪财经）", "zh",
        ["market"], ["china-market", "participating", "low-rate"],
        ["分红险", "万亿", "中保协", "低利率", "人身险"], ["分紅險", "萬億", "中保協", "低利率", "人身險"],
        "news", "2026-08-11T18:42:26+08:00",
        "http://m.toutiao.com/group/7672722587726463523/",
    ),
    # 3. 丹论财: IRR demo cap + ICAC enforcement + underground policy red lines
    item(
        "toutiao-irr-cap-enforcement-20260811", 62, "pending", "media",
        "toutiao:danluncai-irr-cap-enforcement-20260811",
        "监管重拳后赴港投保降温：分红演示设6%/6.5%上限 廉署联手整治无牌转介与返佣",
        "監管重拳後赴港投保降溫：分紅演示設6%/6.5%上限 廉署聯手整治無牌轉介與返佣",
        "文章梳理赴港投保降温的监管三因素：香港保监局要求2025年7月起分红保单预期回报演示设上限（港元保单IRR不超6%、美元等非港元不超6.5%）；保监局与廉政公署联合执法，搜查涉嫌通过无牌内地转介人推销保单、并将九成以上高额佣金私下返还的经纪公司；两地监管重申投保须亲赴香港签署，内地签单或网络代办保单属「地下保单」，两地均不受法律保护。",
        "文章梳理赴港投保降溫的監管三因素：香港保監局要求2025年7月起分紅保單預期回報演示設上限（港元保單IRR不超6%、美元等非港元不超6.5%）；保監局與廉政公署聯合執法，搜查涉嫌透過無牌內地轉介人推銷保單、並將九成以上高額佣金私下返還的經紀公司；兩地監管重申投保須親赴香港簽署，內地簽單或網絡代辦保單屬「地下保單」，兩地均不受法律保護。",
        "把IRR演示上限、无牌转介整治、地下保单红线串成「渠道合规全景」，前线展业与客户沟通时可直接对照红线，避免踩入灰色地带。",
        "把IRR演示上限、無牌轉介整治、地下保單紅線串成「渠道合規全景」，前線展業與客戶溝通時可直接對照紅線，避免踩入灰色地帶。",
        {"front": L("演示上限+红线=展业对照清单", "演示上限+紅線=展業對照清單"), "midback": L("返佣整治=中介合规警示", "返佣整治=中介合規警示"), "lead": {}, "cross": {}},
        {"front": 2, "midback": 2, "lead": 1, "cross": 1},
        "丹论财（今日头条）", "zh",
        ["compliance", "market"], ["channel", "compliance", "sales-conduct"],
        ["分红演示上限", "廉政公署", "无牌转介", "返佣", "地下保单"], ["分紅演示上限", "廉政公署", "無牌轉介", "返佣", "地下保單"],
        "news", "2026-08-11T19:23:28+08:00",
        "http://m.toutiao.com/group/7672731992790729279/",
    ),
    # 4. 胡说保险: tax mechanics — gains not policy value; prepaid premium interest taxed
    item(
        "toutiao-husao-tax-mechanics-20260811", 64, "pending", "media",
        "toutiao:husao-tax-mechanics-20260811",
        "港险征税再拆解：征的是「收益」不是保单价值 预缴保费利息纳入范围",
        "港險徵稅再拆解：徵的是「收益」不是保單價值 預繳保費利息納入範圍",
        "自媒体拆解征税细节：统一适用20%比例税率（比照利息、股息、红利所得）；征税范围涉及分红收益与预缴保费利息收益两类，理赔款明确不征税；按「收益」而非保单价值计税——如100万保费保单，仅超出保单价值部分的收益才计征。文章解释香港预缴保费机制（首年一次性缴清多年保费、剩余资金计息）与内地保单的差异。",
        "自媒體拆解徵稅細節：統一適用20%比例稅率（比照利息、股息、紅利所得）；徵稅範圍涉及分紅收益與預繳保費利息收益兩類，理賠款明確不徵稅；按「收益」而非保單價值計稅。文章解釋香港預繳保費機制（首年一次性繳清多年保費、剩餘資金計息）與內地保單的差異。",
        "预缴保费利息被纳入征税范围是此前报道未展开的细节，对持有多缴保费保单的客户有直接提示价值，值得在保单检视时主动沟通。",
        "預繳保費利息被納入徵稅範圍是此前報道未展開的細節，對持有多繳保費保單的客戶有直接提示價值，值得在保單檢視時主動溝通。",
        {"front": L("预缴利息征税=保单检视新要点", "預繳利息徵稅=保單檢視新要點"), "midback": {}, "lead": {}, "cross": L("预缴机制涉跨境税务安排", "預繳機制涉跨境稅務安排")},
        {"front": 2, "midback": 1, "lead": 1, "cross": 2},
        "胡说保险（今日头条）", "zh",
        ["reg", "product"], ["taxation", "product", "cross-border"],
        ["预缴保费", "利息", "征税范围", "税率", "理赔免税"], ["預繳保費", "利息", "徵稅範圍", "稅率", "理賠免稅"],
        "news", "2026-08-11T22:14:33+08:00",
        "http://m.toutiao.com/group/7672770547847283254/",
    ),
    # 5. 千龙网/新京报: NFRA nat-cat claims progress (typhoon Dolphin + floods)
    item(
        "nfra-natcat-claims-20260812", 68, "verified", "media",
        "bjnews:nfra-natcat-claims-20260812",
        "金融监管总局：近期重大自然灾害保险业累计已赔付76亿元",
        "金融監管總局：近期重大自然災害保險業累計已賠付76億元",
        "金融监管总局披露：台风「白海豚」登陆浙江后，截至8月11日12时，浙江、上海、江苏、江西、宁波5地保险机构共接报案近10万件、估损12亿元、已赔付（含预赔付）3409万元；针对近期强降雨、台风、地震、山洪等灾害，22省份保险业累计接报案67万件、估损132亿元、已赔付76亿元，赔付进度57%。",
        "金融監管總局披露：颱風「白海豚」登陸浙江後，截至8月11日12時，浙江、上海、江蘇、江西、寧波5地保險機構共接報案近10萬件、估損12億元、已賠付（含預賠付）3409萬元；針對近期強降雨、颱風、地震、山洪等災害，22省份保險業累計接報案67萬件、估損132億元、已賠付76億元，賠付進度57%。",
        "官方理赔数据量化台风白海豚与汛期灾害的赔付进度，可与巨灾建模、区域累积风险议题联动，服务机构客户沟通与理赔预期管理。",
        "官方理賠數據量化颱風白海豚與汛期災害的賠付進度，可與巨災建模、區域累積風險議題聯動，服務機構客戶溝通與理賠預期管理。",
        {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        {"front": 1, "midback": 2, "lead": 0, "cross": 1},
        "千龙网（新京报·金融监管总局数据）", "zh",
        ["market", "insurer"], ["natcat", "claims", "china"],
        ["台风白海豚", "理赔", "金融监管总局", "巨灾", "估损"], ["颱風白海豚", "理賠", "金融監管總局", "巨災", "估損"],
        "news", "2026-08-12T00:26:00+08:00",
        "https://m.bjnews.com.cn/detail/1786465979189263.html",
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
