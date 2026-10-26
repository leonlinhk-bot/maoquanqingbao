#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-27 00:3x 增量：插入 4 条（10-26 21:13 之后新发）"""
import json
import datetime

NOW = datetime.datetime.now().astimezone()
INGEST = NOW.isoformat(timespec='seconds')
PATH = 'data/live-items.json'

new_items = [
    {
        "id": "reinsurancenews-brown-brown-compass-ai-20261027",
        "clusterCount": 1,
        "verifyStatus": "verified",
        "contentKind": "news",
        "ingestedAt": INGEST,
        "publishedAt": "2026-10-27T00:00:00+08:00",
        "originalUrl": "https://www.reinsurancene.ws/brown-brown-launches-connected-intelligence-ecosystem-to-improve-insurance-decisions/",
        "sourceKey": "reinsurancenews",
        "sourceTier": "pro",
        "score": 70,
        "boards": ["tech", "insurer"],
        "themes": ["AI应用", "经纪数字化", "数据分析"],
        "title": {
            "sc": "布朗保险推出 COMPASS 智能生态　把数据与 AI 接到核保决策",
            "tc": "布朗保險推出 COMPASS 智能生態　把數據與 AI 接到核保決策"
        },
        "summary": {
            "sc": "布朗保险（Brown & Brown）推出 COMPASS，把集团数据、分析、专业经验与 AI 能力整合到同一平台，用于保险策略与组合优化；强调并非把通用大模型套进单一流程，而是围绕核保决策构建。案例指有企业客户经分析后保费支出降 65%。[EN原文]",
            "tc": "布朗保險（Brown & Brown）推出 COMPASS，把集團數據、分析、專業經驗與 AI 能力整合到同一平台，用於保險策略與組合優化；強調並非把通用大模型套進單一流程，而是圍繞核保決策構建。案例指有企業客戶經分析後保費支出降 65%。[EN原文]"
        },
        "why": {
            "sc": "经纪巨头自建 AI 生态而非采购单点工具，是 AI 落地的另一条路径。对照我们自己的现状——多数 AI 应用停在文案与检索，别人的 AI 已进入组合优化与报价环节，差距主要在数据能不能打通。",
            "tc": "經紀巨頭自建 AI 生態而非採購單點工具，是 AI 落地的另一條路徑。對照我們自己的現狀——多數 AI 應用停在文案與檢索，別人的 AI 已進入組合優化與報價環節，差距主要在數據能不能打通。"
        },
        "tags": {
            "sc": ["AI应用", "经纪数字化", "数据分析", "核保"],
            "tc": ["AI應用", "經紀數字化", "數據分析", "核保"]
        },
        "actions": {
            "front": {"sc": "客户沟通：AI 与保障方案", "tc": "客戶溝通：AI 與保障方案"},
            "midback": {"sc": "研究：数据打通路径", "tc": "研究：數據打通路徑"},
            "lead": {"sc": "团队简报：AI 落地方式", "tc": "團隊簡報：AI 落地方式"},
            "cross": {"sc": "跨境经纪科技", "tc": "跨境經紀科技"}
        },
        "rolesImpact": {"front": 1, "midback": 2, "lead": 2, "cross": 1},
        "source": {"sc": "Reinsurance News 2026-10-27", "tc": "Reinsurance News 2026-10-27",
                   "name": "reinsurancenews", "date": "2026-10-27", "lang": "en"},
        "lang": "en"
    },
    {
        "id": "reinsurancenews-synthetik-marsh-re-cityscape-20261026",
        "clusterCount": 1,
        "verifyStatus": "verified",
        "contentKind": "news",
        "ingestedAt": INGEST,
        "publishedAt": "2026-10-26T22:00:00+08:00",
        "originalUrl": "https://www.reinsurancene.ws/synthetik-and-marsh-re-extend-cityscape-collaboration/",
        "sourceKey": "reinsurancenews",
        "sourceTier": "pro",
        "score": 70,
        "boards": ["tech", "market"],
        "themes": ["恐怖主义风险", "巨灾建模", "再保"],
        "title": {
            "sc": "Marsh Re 与 Synthetik 续约三年　城市爆炸与恐袭累积建模续用 CityScape",
            "tc": "Marsh Re 與 Synthetik 續約三年　城市爆炸與恐襲累積建模續用 CityScape"
        },
        "summary": {
            "sc": "Synthetik Insurance Technologies 与 Marsh Re 把 CityScape 合作再延长三年。该工具以计算流体力学模拟爆炸冲击，评估高密度城市中恐怖主义与政治暴力的财产损失累积，用于可能最大损失评估与再保安排。[EN原文]",
            "tc": "Synthetik Insurance Technologies 與 Marsh Re 把 CityScape 合作再延長三年。該工具以計算流體力學模擬爆炸衝擊，評估高密度城市中恐怖主義與政治暴力的財產損失累積，用於可能最大損失評估與再保安排。[EN原文]"
        },
        "why": {
            "sc": "高密度城市的恐袭与爆炸累积风险难以用系数估算，物理模型正成为再保定价与累积控制的依据。谈商业财产险或大型项目时，可用它解释「核保为何看累积而不只看单一保额」。",
            "tc": "高密度城市的恐襲與爆炸累積風險難以用係數估算，物理模型正成為再保定價與累積控制的依據。談商業財產險或大型項目時，可用它解釋「核保為何看累積而不只看單一保額」。"
        },
        "tags": {
            "sc": ["恐怖主义风险", "巨灾建模", "再保", "高密度城市"],
            "tc": ["恐怖主義風險", "巨災建模", "再保", "高密度城市"]
        },
        "actions": {
            "front": {"sc": "客户沟通：累积风险概念", "tc": "客戶溝通：累積風險概念"},
            "midback": {"sc": "研究：恐袭建模方法", "tc": "研究：恐襲建模方法"},
            "lead": {"sc": "团队简报：再保定价依据", "tc": "團隊簡報：再保定價依據"},
            "cross": {"sc": "大型项目跨境保障", "tc": "大型項目跨境保障"}
        },
        "rolesImpact": {"front": 1, "midback": 2, "lead": 1, "cross": 2},
        "source": {"sc": "Reinsurance News 2026-10-26", "tc": "Reinsurance News 2026-10-26",
                   "name": "reinsurancenews", "date": "2026-10-26", "lang": "en"},
        "lang": "en"
    },
    {
        "id": "artemis-hcma-sidecars-data-centres-2027-20261026",
        "clusterCount": 1,
        "verifyStatus": "verified",
        "contentKind": "news",
        "ingestedAt": INGEST,
        "publishedAt": "2026-10-26T22:00:00+08:00",
        "originalUrl": "https://www.artemis.bm/news/sidecars-and-data-centres-key-opportunity-areas-for-hcma-in-2027-ceo-madea/",
        "sourceKey": "artemis",
        "sourceTier": "pro",
        "score": 71,
        "boards": ["market"],
        "themes": ["ILS", "侧挂车", "数据中心"],
        "title": {
            "sc": "Howden 资本市场主管：2027 年侧挂车与数据中心是两大机会",
            "tc": "Howden 資本市場主管：2027 年側掛車與數據中心是兩大機會"
        },
        "summary": {
            "sc": "Howden Capital Markets & Advisory 行政总裁 Jarad Madea 表示，抵押再保侧挂车持续扩张、数据中心建设加快，是公司 2027 年的两大机会。他称今年蒙特卡洛真正的终端投资人由三、五年前的两位增至至少二十位，机构资金正寻求更直接参与保险风险。[EN原文]",
            "tc": "Howden Capital Markets & Advisory 行政總裁 Jarad Madea 表示，抵押再保側掛車持續擴張、數據中心建設加快，是公司 2027 年的兩大機會。他稱今年蒙特卡洛真正的終端投資人由三、五年前的兩位增至至少二十位，機構資金正尋求更直接參與保險風險。[EN原文]"
        },
        "why": {
            "sc": "侧挂车与数据中心是目前机构资本进入保险风险的两条主线，说明另类风险资本仍在扩容。做高客或机构沟通时，这是「保险资产化」叙事里较硬的外部证据，可以替代空泛的「市场看好」。",
            "tc": "側掛車與數據中心是目前機構資本進入保險風險的兩條主線，說明另類風險資本仍在擴容。做高客或機構溝通時，這是「保險資產化」敘事裡較硬的外部證據，可以替代空泛的「市場看好」。"
        },
        "tags": {
            "sc": ["ILS", "侧挂车", "数据中心", "再保"],
            "tc": ["ILS", "側掛車", "數據中心", "再保"]
        },
        "actions": {
            "front": {"sc": "客户沟通：保险风险资产化", "tc": "客戶溝通：保險風險資產化"},
            "midback": {"sc": "研究：资本结构变化", "tc": "研究：資本結構變化"},
            "lead": {"sc": "团队简报：ILS 市场", "tc": "團隊簡報：ILS 市場"},
            "cross": {"sc": "机构资金跨境配置", "tc": "機構資金跨境配置"}
        },
        "rolesImpact": {"front": 1, "midback": 1, "lead": 2, "cross": 2},
        "source": {"sc": "Artemis.bm 2026-10-26", "tc": "Artemis.bm 2026-10-26",
                   "name": "artemis", "date": "2026-10-26", "lang": "en"},
        "lang": "en"
    },
    {
        "id": "scmp-china-offshore-trust-tax-disclosure-20261026",
        "clusterCount": 1,
        "verifyStatus": "pending",
        "contentKind": "news",
        "ingestedAt": INGEST,
        "publishedAt": "2026-10-26T21:30:00+08:00",
        "originalUrl": "https://www.scmp.com/economy/china-economy/article/3372178/chinas-tax-offices-issue-disclosure-orders-offshore-asset-grace-period-ends",
        "sourceKey": "scmp",
        "sourceTier": "media",
        "score": 74,
        "boards": ["family", "market"],
        "themes": ["跨境税务", "离岸信托", "高净值"],
        "title": {
            "sc": "内地税务局发通知追查离岸信托　90 天宽限期届满",
            "tc": "內地稅務局發通知追查離岸信託　90 天寬限期屆滿"
        },
        "summary": {
            "sc": "内地离岸信托申报的 90 天宽限期上周四届满，各地税务局随即加强核查。北京市税务局在官网对 21 名个人发出通知，要求提交离岸信托相关税务资料。对以境外保单、信托作传承安排的高客，信息透明化压力再升一档。[EN原文]",
            "tc": "內地離岸信託申報的 90 天寬限期上週四屆滿，各地稅務局隨即加強核查。北京市稅務局在官網對 21 名個人發出通知，要求提交離岸信託相關稅務資料。對以境外保單、信託作傳承安排的高客，信息透明化壓力再升一檔。[EN原文]"
        },
        "why": {
            "sc": "客户问「境外保单会不会被交换回内地」时，这条是可引用的最新事实：宽限期已过、个案追查已启动。谈传承架构要把税务申报义务与保险方案分开讲，别把保单包装成税务解决方案。",
            "tc": "客戶問「境外保單會不會被交換回內地」時，這條是可引用的最新事實：寬限期已過、個案追查已啟動。談傳承架構要把稅務申報義務與保險方案分開講，別把保單包裝成稅務解決方案。"
        },
        "tags": {
            "sc": ["跨境税务", "离岸信托", "高净值", "自愿披露"],
            "tc": ["跨境稅務", "離岸信託", "高淨值", "自願披露"]
        },
        "actions": {
            "front": {"sc": "客户沟通：境外资产申报义务", "tc": "客戶溝通：境外資產申報義務"},
            "midback": {"sc": "合规：传承架构税务提示", "tc": "合規：傳承架構稅務提示"},
            "lead": {"sc": "团队简报：跨境透明度", "tc": "團隊簡報：跨境透明度"},
            "cross": {"sc": "跨境高客税务风险", "tc": "跨境高客稅務風險"}
        },
        "rolesImpact": {"front": 2, "midback": 2, "lead": 2, "cross": 3},
        "source": {"sc": "South China Morning Post 2026-10-26", "tc": "South China Morning Post 2026-10-26",
                   "name": "scmp", "date": "2026-10-26", "lang": "en"},
        "lang": "en"
    },
]


def key_of(it):
    p = it.get('publishedAt') or ''
    return (p + 'T23:59:59+08:00') if len(p) == 10 else p


d = json.load(open(PATH, encoding='utf-8'))
items = d['items']
existing_ids = {i['id'] for i in items}
existing_urls = {(i.get('originalUrl') or '').split('?')[0] for i in items}

added = []
for it in new_items:
    if it['id'] in existing_ids:
        print('skip dup id', it['id'])
        continue
    if (it['originalUrl'].split('?')[0]) in existing_urls:
        print('skip dup url', it['id'])
        continue
    k = key_of(it)
    pos = len(items)
    for idx, cur in enumerate(items):
        if key_of(cur) < k:
            pos = idx
            break
    items.insert(pos, it)
    added.append(it['id'])

n = len(items)
d['items'] = items
meta = d.setdefault('meta', {})
meta['generatedAt'] = INGEST
meta['itemCount'] = n
meta['windowNote'] = {"sc": f"本库{n}条。", "tc": f"本庫{n}條。"}
json.dump(d, open(PATH, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

lc = json.load(open('data/last-check.json', encoding='utf-8'))
lc['lastCheck'] = INGEST
for k in lc.get('sources', {}):
    lc['sources'][k]['last'] = INGEST
json.dump(lc, open('data/last-check.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

print('added', len(added), added)
print('total', n, 'lastCheck', lc['lastCheck'])
for it in items[:8]:
    print(it['publishedAt'][:16], '|', it['id'], '|', it['title']['sc'][:44])
