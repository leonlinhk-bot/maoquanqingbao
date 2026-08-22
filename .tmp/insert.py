#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert new daily items into live-items.json with dedupe check, update meta."""
import json, datetime, sys

TZ8 = datetime.timezone(datetime.timedelta(hours=8))
NOW = datetime.datetime.now(TZ8)
now_iso = NOW.strftime("%Y-%m-%dT%H:%M:%S+08:00")
today = NOW.strftime("%Y-%m-%d")

NEW = [
    {
        "id": "ia-aia-h1-profit-20260821",
        "clusterCount": 1,
        "score": 66,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insuranceasia",
        "title": {
            "sc": "InsuranceAsia：友邦2026上半年净利大增69.2%至43亿美元 股东获返还36亿美元 [EN原文]",
            "tc": "InsuranceAsia：友邦2026上半年淨利大增69.2%至43億美元 股東獲返還36億美元 [EN原文]"
        },
        "summary": {
            "sc": "友邦集团2026年中期业绩：综合净利按年增69.2%至43亿美元；新业务价值升10%至32亿美元，香港为最大新业务市场，内地访客业务约占港澳新业务价值一半；期内透过股息及回购向股东返还36亿美元，多项关键财务指标录双位数增长。",
            "tc": "友邦集團2026年中期業績：綜合淨利按年增69.2%至43億美元；新業務價值升10%至32億美元，香港為最大新業務市場，內地訪客業務約佔港澳新業務價值一半；期內透過股息及回購向股東返還36億美元，多項關鍵財務指標錄雙位數增長。"
        },
        "why": {
            "sc": "中报补上纯利维度：净利增速69.2%远超新业务价值10%的增速，反映营运杠杆与投资表现；股东返还36亿美元显示龙头现金流与分红能力，是渠道谈长期保单与公司基本面的第一手数据。",
            "tc": "中報補上純利維度：淨利增速69.2%遠超新業務價值10%的增速，反映營運槓桿與投資表現；股東返還36億美元顯示龍頭現金流與分紅能力，是渠道談長期保單與公司基本面的第一手數據。"
        },
        "actions": {"front": {}, "midback": {}, "lead": {"sc": "友邦中报纯利数据话术", "tc": "友邦中報純利數據話術"}, "cross": {}},
        "rolesImpact": {"front": 0, "midback": 0, "lead": 1, "cross": 0},
        "source": {"sc": "InsuranceAsia", "lang": "en"},
        "boards": ["insurer", "market"],
        "themes": ["results", "market"],
        "tags": {"sc": ["友邦", "中报", "净利", "新业务价值"], "tc": ["友邦", "中報", "淨利", "新業務價值"]},
        "contentKind": "news",
        "publishedAt": "2026-08-21T05:15:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/aia-profit-surges-692-43b-in-h1-2026",
        "ingestedAt": now_iso,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "ia-week-in-insurance-20260822",
        "clusterCount": 1,
        "score": 64,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insuranceasia",
        "title": {
            "sc": "InsuranceAsia一周速览：Chubb危疾系列登场 保诚扩充太古坊 友邦平安纯利大增 [EN原文]",
            "tc": "InsuranceAsia一週速覽：Chubb危疾系列登場 保誠擴充太古坊 友邦平安純利大增 [EN原文]"
        },
        "summary": {
            "sc": "本周（8月17-21日）行业要点：Chubb Life香港推出Chubb Care危疾系列（覆盖146种疾病、中港统一保费）；保诚香港太古坊办公室扩至8.3万平方呎；友邦、平安H1纯利大增；新加坡寿险顾问渠道新单占比达79.4%；另有多项新产品与扩张动态。",
            "tc": "本週（8月17-21日）行業要點：Chubb Life香港推出Chubb Care危疾系列（覆蓋146種疾病、中港統一保費）；保誠香港太古坊辦公室擴至8.3萬平方呎；友邦、平安H1純利大增；新加坡壽險顧問渠道新單佔比達79.4%；另有多項新產品與擴張動態。"
        },
        "why": {
            "sc": "一周速览助渠道快速对齐行业动态：Chubb新危疾产品与保诚扩张都是可直接转述的谈资；叠加中报季业绩，适合作为团队晨会素材与客户沟通背景。",
            "tc": "一週速覽助渠道快速對齊行業動態：Chubb新危疾產品與保誠擴張都是可直接轉述的談資；疊加中報季業績，適合作為團隊晨會素材與客戶溝通背景。"
        },
        "actions": {"front": {"sc": "新产品谈资速览", "tc": "新產品談資速覽"}, "midback": {}, "lead": {"sc": "团队晨会素材", "tc": "團隊晨會素材"}, "cross": {}},
        "rolesImpact": {"front": 1, "midback": 0, "lead": 1, "cross": 0},
        "source": {"sc": "InsuranceAsia", "lang": "en"},
        "boards": ["market"],
        "themes": ["market", "results"],
        "tags": {"sc": ["一周速览", "Chubb", "保诚", "友邦", "平安"], "tc": ["一週速覽", "Chubb", "保誠", "友邦", "平安"]},
        "contentKind": "news",
        "publishedAt": "2026-08-22T05:00:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/week-in-insurance-new-products-launch-insurers-expand-aia-and-ping-profits-surge",
        "ingestedAt": now_iso,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "scmp-pingan-hk-etf-20260821",
        "clusterCount": 1,
        "score": 70,
        "verifyStatus": "pending",
        "sourceTier": "media",
        "sourceKey": "scmp",
        "title": {
            "sc": "南华早报：平安获准跨境投资后拟投香港ETF 淡化征税影响 上半年纯利增36% [EN原文]",
            "tc": "南華早報：平安獲准跨境投資後擬投香港ETF 淡化徵稅影響 上半年純利增36% [EN原文]"
        },
        "summary": {
            "sc": "内地最大险企平安在获跨境投资许可后拟配置香港ETF：H1纯利按年增长36%，管理层淡化内地征税消息影响并给出正面展望；监管同步扩大险资跨境投资渠道，内地机构资金南下配置港股与ETF成为新趋势，与港险资金面形成联动。",
            "tc": "內地最大險企平安在獲跨境投資許可後擬配置香港ETF：H1純利按年增長36%，管理層淡化內地徵稅消息影響並給出正面展望；監管同步擴大險資跨境投資渠道，內地機構資金南下配置港股與ETF成為新趨勢，與港險資金面形成聯動。"
        },
        "why": {
            "sc": "内地险资获准投资香港ETF，机构资金南下通道拓宽，直接关联中港保险资金联动叙事；客户问及内地保险资金动向、税改影响时，这是可引用的最新监管与公司动向。",
            "tc": "內地險資獲准投資香港ETF，機構資金南下通道拓寬，直接關聯中港保險資金聯動敘事；客戶問及內地保險資金動向、稅改影響時，這是可引用的最新監管與公司動向。"
        },
        "actions": {"front": {}, "midback": {}, "lead": {"sc": "中港资金联动话术", "tc": "中港資金聯動話術"}, "cross": {"sc": "内地险资南下动态跟踪", "tc": "內地險資南下動態跟蹤"}},
        "rolesImpact": {"front": 0, "midback": 0, "lead": 1, "cross": 1},
        "source": {"sc": "南华早报 SCMP（经MSN转载）", "lang": "en"},
        "boards": ["cross", "market"],
        "themes": ["cross-border", "market"],
        "tags": {"sc": ["平安", "ETF", "跨境投资", "港股通"], "tc": ["平安", "ETF", "跨境投資", "港股通"]},
        "contentKind": "news",
        "publishedAt": "2026-08-21T18:31:00+08:00",
        "originalUrl": "https://www.msn.com/en-xl/money/investment/chinese-insurer-ping-an-eyes-hong-kong-etfs-as-beijing-greenlights-cross-border-investment/ar-AA2aEauA",
        "ingestedAt": now_iso,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "ib-mainland-etf-access-20260821",
        "clusterCount": 1,
        "score": 71,
        "verifyStatus": "verified",
        "sourceTier": "pro",
        "sourceKey": "insurancebusinessmag",
        "title": {
            "sc": "Insurance Business：内地险企获ETF通道 散户同类渠道却被收紧 [EN原文]",
            "tc": "Insurance Business：內地險企獲ETF通道 散戶同類渠道卻被收緊 [EN原文]"
        },
        "summary": {
            "sc": "港股通ETF扩容公告中易被忽略的细节：内地险企获机构通道投资香港市场，同期北京却收紧内地散户同类渠道；分析指对向内地客户销售投资相连及分红产品的经纪而言，机构与散户通道此消彼长才是真正故事，内地险企总资产41.31万亿元（约6.1万亿美元）正获得更直接的南下路径。",
            "tc": "港股通ETF擴容公告中易被忽略的細節：內地險企獲機構通道投資香港市場，同期北京卻收緊內地散戶同類渠道；分析指對向內地客戶銷售投資相連及分紅產品的經紀而言，機構與散戶通道此消彼長才是真正故事，內地險企總資產41.31萬億元（約6.1萬億美元）正獲得更直接的南下路徑。"
        },
        "why": {
            "sc": "从渠道视角解读同一监管动作：机构南下 vs 散户收紧的对比，直接影响内地客户投资相连/分红产品的销售叙事与客群结构；对中港两地牌照的团队是重要的资金面背景。",
            "tc": "從渠道視角解讀同一監管動作：機構南下 vs 散戶收緊的對比，直接影響內地客戶投資相連/分紅產品的銷售敘事與客群結構；對中港兩地牌照的團隊是重要的資金面背景。"
        },
        "actions": {"front": {}, "midback": {}, "lead": {"sc": "渠道资金面解读", "tc": "渠道資金面解讀"}, "cross": {"sc": "内地客户资金通道动态", "tc": "內地客戶資金通道動態"}},
        "rolesImpact": {"front": 0, "midback": 0, "lead": 1, "cross": 1},
        "source": {"sc": "Insurance Business Asia", "lang": "en"},
        "boards": ["market", "cross"],
        "themes": ["cross-border", "market"],
        "tags": {"sc": ["ETF", "港股通", "内地险资", "投资相连"], "tc": ["ETF", "港股通", "內地險資", "投資相連"]},
        "contentKind": "news",
        "publishedAt": "2026-08-21T23:35:00+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/life-insurance/mainland-insurers-gain-etf-access-retail-traders-just-lost-587035.aspx",
        "ingestedAt": now_iso,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "crntt-aia-mcv-demand-20260822",
        "clusterCount": 1,
        "score": 72,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "crntt",
        "title": {
            "sc": "友邦管理层：内地客来港投保需求持续 征税属既有政策非针对港险「新香港人」占本地新业务约30%",
            "tc": "友邦管理層：內地客來港投保需求持續 徵稅屬既有政策非針對港險「新香港人」佔本地新業務約30%"
        },
        "summary": {
            "sc": "友邦CEO李源祥及区域CEO陈荣声回应「保单税」传闻：内地对境外投资收益征税属既有政策、非专门针对港险；内地访客投保需求持续，6月为上半年最佳月份，7-8月需求仍良好；内地访客业务约占港澳新业务价值一半，「新香港人」已占友邦香港本地客户新业务价值约30%且占比连年提升。",
            "tc": "友邦CEO李源祥及區域CEO陳榮聲回應「保單稅」傳聞：內地對境外投資收益徵稅屬既有政策、非專門針對港險；內地訪客投保需求持續，6月為上半年最佳月份，7-8月需求仍良好；內地訪客業務約佔港澳新業務價值一半，「新香港人」已佔友邦香港本地客戶新業務價值約30%且佔比連年提升。"
        },
        "why": {
            "sc": "管理层首次系统回应征税传闻并给出最新MCV数据：6月最佳、7-8月需求良好，叠加「新香港人」占本地新业务三成的结构性变化，是渠道校准内地客话术、开拓人才输入计划新客群的第一手依据。",
            "tc": "管理層首次系統回應徵稅傳聞並給出最新MCV數據：6月最佳、7-8月需求良好，疊加「新香港人」佔本地新業務三成的結構性變化，是渠道校準內地客話術、開拓人才輸入計劃新客群的第一手依據。"
        },
        "actions": {"front": {"sc": "内地客需求话术校准", "tc": "內地客需求話術校準"}, "midback": {}, "lead": {"sc": "新香港人客群策略", "tc": "新香港人客群策略"}, "cross": {}},
        "rolesImpact": {"front": 1, "midback": 0, "lead": 1, "cross": 0},
        "source": {"sc": "中评社（中国评论新闻，转载大公报）", "lang": "zh"},
        "boards": ["market"],
        "themes": ["mcv", "taxation"],
        "tags": {"sc": ["友邦", "内地访客", "征税", "新香港人", "MCV"], "tc": ["友邦", "內地訪客", "徵稅", "新香港人", "MCV"]},
        "contentKind": "news",
        "publishedAt": "2026-08-22T00:40:00+08:00",
        "originalUrl": "https://hk.crntt.com/doc/1072/2/6/3/107226380.html?coluid=7&kindid=0&docid=107226380&mdate=0822004037",
        "ingestedAt": now_iso,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    }
]

d = json.load(open('data/live-items.json'))
items = d['items']
existing_ids = {it['id'] for it in items}
existing_titles = [it['title']['sc'] for it in items]

added = []
for it in NEW:
    if it['id'] in existing_ids:
        print(f"[skip] dup id: {it['id']}")
        continue
    # title-similarity dedupe
    t = it['title']['sc']
    dup = False
    for et in existing_titles:
        common = sum(1 for a, b in zip(t, et) if a == b)
        if common > 30 and min(len(t), len(et)) > 20:
            print(f"[skip] similar title: {it['id']} ~ {et[:40]}")
            dup = True
            break
    if dup:
        continue
    added.append(it)

items[0:0] = added
d['items'] = items
d['meta']['generatedAt'] = now_iso
d['meta']['itemCount'] = len(items)
json.dump(d, open('data/live-items.json', 'w'), ensure_ascii=False, indent=2)
print(f"added {len(added)} items; total now {len(items)}")
for it in added:
    print("+", it['id'], "|", it['publishedAt'], "|", it['title']['sc'][:50])
