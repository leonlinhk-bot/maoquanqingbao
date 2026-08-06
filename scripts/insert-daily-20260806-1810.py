#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert daily collected items into live-items.json (2026-08-06 18:08 slot, evening run)"""
import json
from datetime import datetime, timezone, timedelta

HKT = timezone(timedelta(hours=8))
NOW = datetime(2026, 8, 6, 18, 10, 0, tzinfo=HKT)

new_items = [
    {
        "id": "hk-policy-tax-selloff-aug06",
        "clusterCount": 12, "score": 84, "verifyStatus": "verified",
        "sourceTier": "media", "sourceKey": "caixin:london-selloff-20260806",
        "title": {"sc": "征税20%发酵：香港保险股集体重挫 友邦一度跌9% 大行称抛售过度", "tc": "徵稅20%發酵：香港保險股集體重挫 友邦一度跌9% 大行稱拋售過度"},
        "summary": {"sc": "财新报道内地对境外保单收益征20%个税后，8月6日港保险股集体重挫：友邦一度跌超9%，保诚跌逾5%（伦敦曾挫13%）。花旗、瑞银指个案零星、无全国统一标准，抛售由恐慌主导且过度；摩根大通称内地访客仅占友邦新业务价值21%。", "tc": "財新報道內地對境外保單收益徵20%個稅後，8月6日港保險股集體重挫：友邦一度跌超9%，保誠跌逾5%（倫敦曾挫13%）。花旗、瑞銀指個案零星、無全國統一標準，拋售由恐慌主導且過度；摩根大通稱內地訪客僅佔友邦新業務價值21%。"},
        "why": {"sc": "昨日「征税落地」报道后市场用脚投票，但大行共识是个案零星、法理存争议、无全国统一标准；恐慌抛售恰是向内地客群解释「税务合规≠港险失效」、重申离岸配置、多元货币、环球医疗等结构性优势的沟通窗口。", "tc": "昨日「徵稅落地」報道後市場用腳投票，但大行共識是個案零星、法理存爭議、無全國統一標準；恐慌拋售恰是向內地客群解釋「稅務合規≠港險失效」、重申離岸配置、多元貨幣、環球醫療等結構性優勢的溝通窗口。"},
        "actions": {"front": {"sc": "征税传闻重挫股价=税后回报叙事必须重写", "tc": "徵稅傳聞重挫股價=稅後回報敘事必須重寫"}, "midback": {"sc": "地方个案+CRS交换=征管趋势确认", "tc": "地方個案+CRS交換=徵管趨勢確認"}, "lead": {"sc": "恐慌抛售后是客户教育与合规沟通窗口", "tc": "恐慌拋售後是客戶教育與合規溝通窗口"}, "cross": {"sc": "跨境架构需同步重估税务合规", "tc": "跨境架構需同步重估稅務合規"}},
        "rolesImpact": {"front": 3, "midback": 2, "lead": 2, "cross": 2},
        "source": {"sc": "财新网 / 新浪财经 / AAStocks", "lang": "zh"},
        "boards": ["reg", "market"], "themes": ["compliance", "offshore", "macro"],
        "tags": {"sc": ["境外保单征税", "20%个税", "CRS", "友邦", "保诚", "大行观点"], "tc": ["境外保單徵稅", "20%個稅", "CRS", "友邦", "保誠", "大行觀點"]},
        "contentKind": "news", "publishedAt": "2026-08-06T08:36:00+08:00",
        "originalUrl": "https://finance.caixin.com/m/2026-08-06/102471644.html"
    },
    {
        "id": "manulife-q2-2026-hk-ape37",
        "clusterCount": 1, "score": 80, "verifyStatus": "verified",
        "sourceTier": "insurer", "sourceKey": "manulife:q2-2026-0806",
        "title": {"sc": "宏利金融次季核心盈利+12% 港澳APE+37% 新业务价值21亿港元+12%", "tc": "宏利金融次季核心盈利+12% 港澳APE+37% 新業務價值21億港元+12%"},
        "summary": {"sc": "宏利次季核心盈利19.23亿加元按年+12%，净收入21.1亿加元+17%；港澳为引擎：核心盈利27亿港元+31%、APE 55亿港元+37%、新业务价值21亿港元+12%。中期股息0.485加元。", "tc": "宏利次季核心盈利19.23億加元按年+12%，淨收入21.1億加元+17%；港澳為引擎：核心盈利27億港元+31%、APE 55億港元+37%、新業務價值21億港元+12%。中期股息0.485加元。"},
        "why": {"sc": "宏利港澳业绩是港险基本盘的最新官方样本：征税消息扰动前公布的强劲数据，说明本地及MCV需求动能仍在，亦为8月下旬友邦、保诚业绩季提供对照基准。", "tc": "宏利港澳業績是港險基本盤的最新官方樣本：徵稅消息擾動前公佈的強勁數據，說明本地及MCV需求動能仍在，亦為8月下旬友邦、保誠業績季提供對照基準。"},
        "actions": {"front": {"sc": "港澳APE+37%=渠道动能强劲", "tc": "港澳APE+37%=渠道動能強勁"}, "midback": {"sc": "新造CSM+16%=未来利润储备增厚", "tc": "新造CSM+16%=未來利潤儲備增厚"}, "lead": {"sc": "业绩季开启=可借力官方数据做客户沟通", "tc": "業績季開啟=可借力官方數據做客戶溝通"}, "cross": {}},
        "rolesImpact": {"front": 2, "midback": 1, "lead": 1, "cross": 0},
        "source": {"sc": "星岛头条 / 宏利金融", "lang": "zh"},
        "boards": ["insurer"], "themes": ["firm", "results"],
        "tags": {"sc": ["宏利", "Q2业绩", "港澳", "APE", "新业务价值"], "tc": ["宏利", "Q2業績", "港澳", "APE", "新業務價值"]},
        "contentKind": "news", "publishedAt": "2026-08-06T10:00:00+08:00",
        "originalUrl": "https://www.stheadline.com/zh-hans/stock-market/3601490/%E5%AE%8F%E5%88%A9%E9%87%91%E8%9E%8D%E6%AC%A1%E5%AD%A3%E6%A0%B8%E5%BF%83%E7%9B%88%E5%88%A9%E5%8D%8712-%E6%B4%BE%E6%81%AF0485%E5%8A%A0%E5%85%83-%E6%B8%AF%E6%BE%B3%E4%B8%9A%E5%8A%A1%E4%B8%BB%E8%A6%81%E4%B8%9A%E7%BB%A9%E5%9D%87%E5%BD%95%E5%8F%8C%E4%BD%8D%E5%A2%9E%E9%95%BF"
    },
    {
        "id": "hsbc-h1-insurance-sales-26pct",
        "clusterCount": 1, "score": 66, "verifyStatus": "pending",
        "sourceTier": "media", "sourceKey": "insuranceasia:hsbc-h1-sales-20260805",
        "title": {"sc": "汇丰保险香港上半年保费+26% 存量银行客户贡献85%新单", "tc": "匯豐保險香港上半年保費+26% 存量銀行客戶貢獻85%新單"},
        "summary": {"sc": "InsuranceAsia报道，汇丰保险香港上半年保费按年增26%，带动市场前景改善；存量银行客户贡献85%保费。银保渠道在港险上半年爆发中持续扮演主力，与Jefferies「首季新单+51%」数据互相印证。[EN原文]", "tc": "InsuranceAsia報道，匯豐保險香港上半年保費按年增26%，帶動市場前景改善；存量銀行客戶貢獻85%保費。銀保渠道在港險上半年爆發中持續扮演主力，與Jefferies「首季新單+51%」數據互相印證。[EN原文]"},
        "why": {"sc": "银保渠道数据揭示港险上半年爆发的结构：存量客户转化而非新增客户扩张，渠道效率与交叉销售成为竞争主轴，与代理渠道形成对照。", "tc": "銀保渠道數據揭示港險上半年爆發的結構：存量客戶轉化而非新增客戶擴張，渠道效率與交叉銷售成為競爭主軸，與代理渠道形成對照。"},
        "actions": {"front": {"sc": "存量客户85%=银保交叉销售是主战场", "tc": "存量客戶85%=銀保交叉銷售是主戰場"}, "midback": {}, "lead": {"sc": "银保主导=与代理人渠道结构对比值得跟踪", "tc": "銀保主導=與代理人渠道結構對比值得跟蹤"}, "cross": {}},
        "rolesImpact": {"front": 1, "midback": 0, "lead": 1, "cross": 0},
        "source": {"sc": "Insurance Asia", "lang": "en"},
        "boards": ["market"], "themes": ["channel", "market"],
        "tags": {"sc": ["汇丰保险", "银保", "上半年保费", "香港"], "tc": ["匯豐保險", "銀保", "上半年保費", "香港"]},
        "contentKind": "news", "publishedAt": "2026-08-06T05:15:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/hsbcs-26-insurance-sales-jump-lifts-hong-kongs-market-outlook"
    },
    {
        "id": "prudential-cuts-china-risk-aug06",
        "clusterCount": 1, "score": 64, "verifyStatus": "pending",
        "sourceTier": "media", "sourceKey": "insuranceasia:prudential-china-risk-20260805",
        "title": {"sc": "保诚削减中国风险敞口 面临利润率挤压 参与型产品占前五大产品保费80%", "tc": "保誠削減中國風險敞口 面臨利潤率擠壓 參與型產品佔前五大產品保費80%"},
        "summary": {"sc": "InsuranceAsia报道，保诚正削减中国相关风险敞口并面临利润率挤压；截至7月30日，五大主打产品中参与型产品占保费量80%。在MCV征税消息与产品更名双重背景下，保诚地区与产品策略调整值得关注。[EN原文]", "tc": "InsuranceAsia報道，保誠正削減中國相關風險敞口並面臨利潤率擠壓；截至7月30日，五大主打產品中參與型產品佔保費量80%。在MCV徵稅消息與產品更名雙重背景下，保誠地區與產品策略調整值得關注。[EN原文]"},
        "why": {"sc": "保诚产品结构高度集中于参与型（分红）产品，恰逢内地征税个案与产品更名潮，其风险重配动作是观察头部保司应对监管环境变化的样本。", "tc": "保誠產品結構高度集中於參與型（分紅）產品，恰逢內地徵稅個案與產品更名潮，其風險重配動作是觀察頭部保司應對監管環境變化的樣本。"},
        "actions": {"front": {"sc": "参与型占80%=分红产品依赖度高", "tc": "參與型佔80%=分紅產品依賴度高"}, "midback": {"sc": "削减中国敞口=地缘与监管双重考量", "tc": "削減中國敞口=地緣與監管雙重考量"}, "lead": {"sc": "头部保司策略转向=渠道话术需同步", "tc": "頭部保司策略轉向=渠道話術需同步"}, "cross": {}},
        "rolesImpact": {"front": 1, "midback": 2, "lead": 1, "cross": 0},
        "source": {"sc": "Insurance Asia", "lang": "en"},
        "boards": ["insurer"], "themes": ["firm", "market"],
        "tags": {"sc": ["保诚", "中国敞口", "参与型产品", "利润率"], "tc": ["保誠", "中國敞口", "參與型產品", "利潤率"]},
        "contentKind": "news", "publishedAt": "2026-08-06T06:00:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/prudential-cuts-china-risk-faces-margin-squeeze"
    },
    {
        "id": "howden-cancer-cover-aug06",
        "clusterCount": 1, "score": 62, "verifyStatus": "pending",
        "sourceTier": "media", "sourceKey": "insuranceasia:howden-cancer-20260805",
        "title": {"sc": "Howden推癌症保障 为阿斯利康员工及父母即时承保 保司倾向避开单独销售", "tc": "Howden推癌症保障 為阿斯利康員工及父母即時承保 保司傾向避開單獨銷售"},
        "summary": {"sc": "InsuranceAsia报道，经纪商Howden推出癌症保障计划，阿斯利康员工及其父母可即时获保；报道指保险公司倾向避免单独销售癌症产品。雇员健康福利（EB）渠道创新是亚太健康险增长的观察切口。[EN原文]", "tc": "InsuranceAsia報道，經紀商Howden推出癌症保障計劃，阿斯利康員工及其父母可即時獲保；報道指保險公司傾向避免單獨銷售癌症產品。僱員健康福利（EB）渠道創新是亞太健康險增長的觀察切口。[EN原文]"},
        "why": {"sc": "雇员健康福利是健康险增长点：经纪牵头+药企员工渠道的癌症保障模式，可作为香港团体医疗险产品创新的参照。", "tc": "僱員健康福利是健康險增長點：經紀牽頭+藥企員工渠道的癌症保障模式，可作為香港團體醫療險產品創新的參照。"},
        "actions": {"front": {"sc": "团体癌症保障=雇员福利新卖点", "tc": "團體癌症保障=僱員福利新賣點"}, "midback": {}, "lead": {"sc": "保司避开单独销售=捆绑策略仍是主流", "tc": "保司避開單獨銷售=捆綁策略仍是主流"}, "cross": {}},
        "rolesImpact": {"front": 1, "midback": 0, "lead": 1, "cross": 0},
        "source": {"sc": "Insurance Asia", "lang": "en"},
        "boards": ["product"], "themes": ["health", "market"],
        "tags": {"sc": ["Howden", "癌症保障", "雇员福利", "健康险"], "tc": ["Howden", "癌症保障", "僱員福利", "健康險"]},
        "contentKind": "news", "publishedAt": "2026-08-06T05:30:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/howden-launches-cancer-cover-insurers-avoid-standalone-plans"
    },
    {
        "id": "sunlife-mpf-concentration-aug06",
        "clusterCount": 1, "score": 63, "verifyStatus": "verified",
        "sourceTier": "media", "sourceKey": "sunlife:mpf-concentration-20260806",
        "title": {"sc": "永明：17.4%强积金成员投资过度集中 近四成50岁以上面临退休风险", "tc": "永明：17.4%強積金成員投資過度集中 近四成50歲以上面臨退休風險"},
        "summary": {"sc": "永明金融数据显示，17.4%强积金成员将资金集中于单一市场或资产类别，其中近四成（38.9%）为50岁或以上；财富及退休金业务CFO陈琎提醒临近退休人士组合风险过集中，应及时检视配置。", "tc": "永明金融數據顯示，17.4%強積金成員將資金集中於單一市場或資產類別，其中近四成（38.9%）為50歲或以上；財富及退休金業務CFO陳琎提醒臨近退休人士組合風險過集中，應及時檢視配置。"},
        "why": {"sc": "退休规划是港险与家办业务交汇点：MPF配置集中度数据可直接用于客户退休检视沟通，也是中后台产品适配与再平衡建议的参考。", "tc": "退休規劃是港險與家辦業務交匯點：MPF配置集中度數據可直接用於客戶退休檢視溝通，也是中後台產品適配與再平衡建議的參考。"},
        "actions": {"front": {"sc": "MPF集中度数据=退休检视沟通抓手", "tc": "MPF集中度數據=退休檢視溝通抓手"}, "midback": {}, "lead": {"sc": "50+客户风险集中=需配置再平衡话术", "tc": "50+客戶風險集中=需配置再平衡話術"}, "cross": {}},
        "rolesImpact": {"front": 2, "midback": 0, "lead": 1, "cross": 0},
        "source": {"sc": "星岛头条 / 永明金融", "lang": "zh"},
        "boards": ["family"], "themes": ["retirement", "market"],
        "tags": {"sc": ["永明", "强积金", "退休规划", "投资集中"], "tc": ["永明", "強積金", "退休規劃", "投資集中"]},
        "contentKind": "news", "publishedAt": "2026-08-06T16:48:00+08:00",
        "originalUrl": "https://www.stheadline.com/zh-hans/investment/3601656/%E8%BF%91%E5%9B%9B%E6%88%9050%E5%B2%81%E4%BB%A5%E4%B8%8AMPF%E6%88%90%E5%91%98%E6%8A%95%E8%B5%84%E8%BF%87%E4%BA%8E%E9%9B%86%E4%B8%AD-%E6%B0%B8%E6%98%8E%E9%80%80%E4%BC%91%E8%B5%84%E4%BA%A7%E6%89%BF%E5%8F%97%E8%BE%83%E5%A4%A7%E5%B8%82%E5%9C%BA%E9%A3%8E%E9%99%A9"
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
