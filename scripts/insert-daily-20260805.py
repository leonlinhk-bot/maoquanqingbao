#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert daily collected items into live-items.json (2026-08-05 evening batch)"""
import json
from datetime import datetime, timezone, timedelta

HKT = timezone(timedelta(hours=8))
NOW = datetime(2026, 8, 5, 18, 15, 0, tzinfo=HKT)

new_items = [
    {
        "id": "china-hk-policy-tax-aug05",
        "clusterCount": 3, "score": 86, "verifyStatus": "verified",
        "sourceTier": "media", "sourceKey": "caixin:hk-policy-tax-20260805",
        "title": {"sc": "内地开始对香港保单收益征20%个税：北京杭州已执行 保诚领跌", "tc": "內地開始對香港保單收益徵20%個稅：北京杭州已執行 保誠領跌"},
        "summary": {"sc": "财新独家：内地税务机关已开始对境外保单收益征个税，北京、杭州已有执行案例，对香港保单分红及预缴保费利息适用20%税率；CRS数据共享令征管落地，预计执行趋严。消息令保诚股价一度跌13%，汇丰、渣打跟随下挫。", "tc": "財新獨家：內地稅務機關已開始對境外保單收益徵個稅，北京、杭州已有執行案例，對香港保單分紅及預繳保費利息適用20%稅率；CRS數據共享令徵管落地，預計執行趨嚴。消息令保誠股價一度跌13%，匯豐、渣打跟隨下挫。"},
        "why": {"sc": "继7月离岸信托个税新规后，内地对跨境金融资产的又一次定向收紧，直接冲击MCV储蓄险的税后回报叙事。对IFA：与内地客群沟通必须前置税务合规议题，「保单收益免税」话术已不可用；对持有多张储蓄保单的内地客户，这是需要主动提示的风险事件。", "tc": "繼7月離岸信託個稅新規後，內地對跨境金融資產的又一次定向收緊，直接衝擊MCV儲蓄險的稅後回報敘事。對IFA：與內地客群溝通必須前置稅務合規議題，「保單收益免稅」話術已不可用；對持有多張儲蓄保單的內地客戶，這是需要主動提示的風險事件。"},
        "actions": {"front": {"sc": "内地对港险收益征税落地=储蓄险税后回报逻辑生变", "tc": "內地對港險收益徵稅落地=儲蓄險稅後回報邏輯生變"}, "midback": {"sc": "CRS交换+20%税率=征管闭环正在形成", "tc": "CRS交換+20%稅率=徵管閉環正在形成"}, "lead": {"sc": "MCV客户需重新评估税后IRR与持有结构", "tc": "MCV客戶需重新評估稅後IRR與持有結構"}, "cross": {}},
        "rolesImpact": {"front": 3, "midback": 2, "lead": 3, "cross": 1},
        "source": {"sc": "财新网 / Reuters", "lang": "zh"},
        "boards": ["reg", "market"], "themes": ["compliance", "offshore", "macro"],
        "tags": {"sc": ["境外保单征税", "个税", "CRS", "MCV", "保诚"], "tc": ["境外保單徵稅", "個稅", "CRS", "MCV", "保誠"]},
        "contentKind": "news", "publishedAt": "2026-08-05T17:31:00+08:00",
        "originalUrl": "https://finance.caixin.com/m/2026-08-05/102471513.html"
    },
    {
        "id": "jefferies-hk-sales-soar-aug05",
        "clusterCount": 1, "score": 72, "verifyStatus": "verified",
        "sourceTier": "pro", "sourceKey": "insuranceasia:jefferies-hk-sales-20260805",
        "title": {"sc": "Jefferies：港险Q1新单保费+51%创新高 银保+48%经纪+60% MCV到访年累计破2000万", "tc": "Jefferies：港險Q1新單保費+51%創新高 銀保+48%經紀+60% MCV到訪年累計破2000萬"},
        "summary": {"sc": "Jefferies研报：香港寿险Q1直接个人新单保费同比+51%至逾1400亿港元创历史新高，增速与2025全年持平；银保+48%、经纪+60%领跑，友邦市占率保持稳定。MCV访客年累计破2000万人次（+16%），本地情绪乐观与西方投资者谨慎并存。[EN原文]", "tc": "Jefferies研報：香港壽險Q1直接個人新單保費同比+51%至逾1400億港元創歷史新高，增速與2025全年持平；銀保+48%、經紀+60%領跑，友邦市佔率保持穩定。MCV訪客年累計破2000萬人次（+16%），本地情緒樂觀與西方投資者謹慎並存。[EN原文]"},
        "why": {"sc": "与8月3日「件数仅+2%」条目互补：量价齐升下银保与经纪渠道爆发，港险增长引擎正从代理人转向渠道多元。MCV月均340万人次是后续新单的先行指标，对判断下半年销售动能及友邦8月20日中期业绩有直接参考价值。", "tc": "與8月3日「件數僅+2%」條目互補：量價齊升下銀保與經紀渠道爆發，港險增長引擎正從代理人轉向渠道多元。MCV月均340萬人次是後續新單的先行指標，對判斷下半年銷售動能及友邦8月20日中期業績有直接參考價值。"},
        "actions": {"front": {"sc": "Q1保费+51%创新高=下半年动能延续信号", "tc": "Q1保費+51%創新高=下半年動能延續信號"}, "midback": {"sc": "银保+48%/经纪+60%=渠道结构生变", "tc": "銀保+48%/經紀+60%=渠道結構生變"}, "lead": {"sc": "关注8月20日友邦中期业绩与MCV动能", "tc": "關注8月20日友邦中期業績與MCV動能"}, "cross": {}},
        "rolesImpact": {"front": 2, "midback": 2, "lead": 2, "cross": 1},
        "source": {"sc": "Insurance Asia / Jefferies", "lang": "en"},
        "boards": ["market"], "themes": ["market", "channel", "offshore"],
        "tags": {"sc": ["Jefferies", "新单保费", "银保渠道", "MCV", "友邦"], "tc": ["Jefferies", "新單保費", "銀保渠道", "MCV", "友邦"]},
        "contentKind": "research", "publishedAt": "2026-08-05T06:00:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/hong-kong-life-sales-soar-despite-investor-caution-jefferies"
    },
    {
        "id": "etiqa-index-endowment-aug05",
        "clusterCount": 1, "score": 65, "verifyStatus": "verified",
        "sourceTier": "media", "sourceKey": "insuranceasia:etiqa-index-endowment-20260805",
        "title": {"sc": "Etiqa新加坡推指数挂钩储蓄计划：挂钩Barclays动态指数 到期保本加0%下限", "tc": "Etiqa新加坡推指數掛鉤儲蓄計劃：掛鉤Barclays動態指數 到期保本加0%下限"},
        "summary": {"sc": "Etiqa新加坡推Enrich Index Income非分红储蓄计划：年度利益挂钩Barclays RADAR 6%指数（美股、债、商品动态配置），到期保本并设0%下限；趸缴或3年缴，含身故及末期疾病保障，免体检。[EN原文]", "tc": "Etiqa新加坡推Enrich Index Income非分紅儲蓄計劃：年度利益掛鉤Barclays RADAR 6%指數（美股、債、商品動態配置），到期保本並設0%下限；躉繳或3年繳，含身故及末期疾病保障，免體檢。[EN原文]"},
        "why": {"sc": "市场波动期「指数挂钩+保本」是亚太储蓄险的应对模板，可与香港分红储蓄产品对照：当演示利率上限压缩收益想象空间，指数策略或成产品创新下一站；对客户沟通也是比较保证/非保证结构的好案例。", "tc": "市場波動期「指數掛鉤+保本」是亞太儲蓄險的應對模板，可與香港分紅儲蓄產品對照：當演示利率上限壓縮收益想象空間，指數策略或成產品創新下一站；對客戶溝通也是比較保證/非保證結構的好案例。"},
        "actions": {"front": {"sc": "指数挂钩+保本=储蓄险新形态样本", "tc": "指數掛鉤+保本=儲蓄險新形態樣本"}, "midback": {"sc": "0%下限设计=下行保护的沟通话术", "tc": "0%下限設計=下行保護的溝通話術"}, "lead": {"sc": "留意港险是否跟进指数挂钩类产品", "tc": "留意港險是否跟進指數掛鉤類產品"}, "cross": {}},
        "rolesImpact": {"front": 2, "midback": 1, "lead": 1, "cross": 0},
        "source": {"sc": "Insurance Asia / Etiqa", "lang": "en"},
        "boards": ["product"], "themes": ["product", "market"],
        "tags": {"sc": ["Etiqa", "指数挂钩", "储蓄计划", "保本", "新加坡"], "tc": ["Etiqa", "指數掛鉤", "儲蓄計劃", "保本", "新加坡"]},
        "contentKind": "news", "publishedAt": "2026-08-05T05:45:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/etiqa-launches-endowment-plan-amidst-volatility-fears"
    },
    {
        "id": "apac-natcat-h1-2026-aug05",
        "clusterCount": 1, "score": 70, "verifyStatus": "verified",
        "sourceTier": "media", "sourceKey": "insuranceasia:apac-natcat-h1-20260805",
        "title": {"sc": "Munich Re：亚太上半年巨灾损失远低于均值 中国5月洪灾损失28亿美元大部分无保险", "tc": "Munich Re：亞太上半年巨災損失遠低於均值 中國5月洪災損失28億美元大部分無保險"},
        "summary": {"sc": "慕再：亚太上半年巨灾经济损失约87亿美元、保险赔付仅逾10亿，远低于10年均值（320亿/50亿）；中国5月洪灾损失28亿美元大部分无保险，澳洲山火约三分之二获赔。全球上半年巨灾损失1120亿、保险覆盖440亿，60%无保障；厄尔尼诺或推高下半年风险。[EN原文]", "tc": "慕再：亞太上半年巨災經濟損失約87億美元、保險賠付僅逾10億，遠低於10年均值（320億/50億）；中國5月洪災損失28億美元大部分無保險，澳洲山火約三分之二獲賠。全球上半年巨災損失1120億、保險覆蓋440億，60%無保障；厄爾尼諾或推高下半年風險。[EN原文]"},
        "why": {"sc": "巨灾低损失基数叠加厄尔尼诺风险上行，是财险/再保定价与高净值客户风险管理的背景板；中国洪灾「投保不足」将保障缺口可视化，也是内地客群财产保障需求的佐证素材。", "tc": "巨災低損失基數疊加厄爾尼諾風險上行，是財險/再保定價與高淨值客戶風險管理的背景板；中國洪災「投保不足」將保障缺口可視化，也是內地客群財產保障需求的佐證素材。"},
        "actions": {"front": {"sc": "亚太巨灾赔付低位=财险定价环境仍宽松", "tc": "亞太巨災賠付低位=財險定價環境仍寬鬆"}, "midback": {"sc": "中国洪灾投保不足=保障缺口可视化", "tc": "中國洪災投保不足=保障缺口可視化"}, "lead": {"sc": "厄尔尼诺H2风险=再保与巨灾债券关注点", "tc": "厄爾尼諾H2風險=再保與巨災債券關注點"}, "cross": {}},
        "rolesImpact": {"front": 1, "midback": 2, "lead": 1, "cross": 1},
        "source": {"sc": "Insurance Asia / Munich Re", "lang": "en"},
        "boards": ["market"], "themes": ["macro", "market"],
        "tags": {"sc": ["Munich Re", "巨灾", "厄尔尼诺", "洪灾", "保险缺口"], "tc": ["Munich Re", "巨災", "厄爾尼諾", "洪災", "保險缺口"]},
        "contentKind": "research", "publishedAt": "2026-08-05T05:00:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/in-focus/asia-pacific-losses-fall-insured-damage-hits-1b-in-h1-2026"
    },
    {
        "id": "nfra-audit-liability-aug05",
        "clusterCount": 1, "score": 85, "verifyStatus": "pending",
        "sourceTier": "official", "sourceKey": "nfra:audit-liability-insurance-20260805",
        "title": {"sc": "金融监管总局：新修订《会计师事务所职业责任保险实施办法》拟近期印发 费率与合规记录挂钩", "tc": "金融監管總局：新修訂《會計師事務所職業責任保險實施辦法》擬近期印發 費率與合規記錄掛鉤"},
        "summary": {"sc": "金融监管总局答复政协提案：与财政部联合起草的新修订《会计师事务所职业责任保险实施办法》拟近期印发。办法将事务所处罚、涉诉及历史赔付记录与费率挂钩，鼓励共保提升承保能力，增设账册丢失、追溯期扩展等附加险，并设职业责任保险专家委员会。[EN原文]", "tc": "金融監管總局答覆政協提案：與財政部聯合起草的新修訂《會計師事務所職業責任保險實施辦法》擬近期印發。辦法將事務所處罰、涉訴及歷史賠付記錄與費率掛鉤，鼓勵共保提升承保能力，增設賬冊丟失、追溯期擴展等附加險，並設職業責任保險專家委員會。[EN原文]"},
        "why": {"sc": "责任险「费率与合规记录挂钩」是内地财险定价精细化的最新样本，方向与港险佣金及定价监管趋同；对关注内地保险政策的中介机构，这是理解职业责任险市场扩容（含大湾区跨境执业需求）的参照。", "tc": "責任險「費率與合規記錄掛鉤」是內地財險定價精細化的最新樣本，方向與港險佣金及定價監管趨同；對關注內地保險政策的中介機構，這是理解職業責任險市場擴容（含大灣區跨境執業需求）的參照。"},
        "actions": {"front": {"sc": "责任险费率挂钩合规记录=定价精细化", "tc": "責任險費率掛鉤合規記錄=定價精細化"}, "midback": {"sc": "共保+附加险=职业责任险扩容信号", "tc": "共保+附加險=職業責任險擴容信號"}, "lead": {"sc": "关注印发后的行业示范条款", "tc": "關注印發後的行業示範條款"}, "cross": {}},
        "rolesImpact": {"front": 1, "midback": 1, "lead": 1, "cross": 0},
        "source": {"sc": "金融监管总局（via 新浪财经/金融一线）", "lang": "zh"},
        "boards": ["reg"], "themes": ["reg", "product"],
        "tags": {"sc": ["职业责任保险", "会计师事务所", "费率挂钩", "金融监管总局", "共保"], "tc": ["職業責任保險", "會計師事務所", "費率掛鉤", "金融監管總局", "共保"]},
        "contentKind": "circular", "publishedAt": "2026-08-05T10:33:00+08:00",
        "originalUrl": "http://m.toutiao.com/group/7670370104106680882/"
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
data["meta"]["asOf"] = "2026-08-05"

with open("data/live-items.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Inserted {len(filtered)} new items. Total: {len(data['items'])}")
for item in filtered:
    print(f"  + {item['id']} [{item['sourceTier']}] {item['title']['sc'][:50]}")
