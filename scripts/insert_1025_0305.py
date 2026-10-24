#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-25 02:xx 每日增量：插入 6 条（10-24 为主 + 2 条前次漏采补漏）"""
import json
import datetime

NOW = datetime.datetime.now().astimezone()
INGEST = NOW.isoformat(timespec='seconds')
PATH = 'data/live-items.json'

new_items = [
    {
        "id": "ian-fullcapacity-captive-race-20261024",
        "clusterCount": 1,
        "verifyStatus": "verified",
        "contentKind": "news",
        "ingestedAt": INGEST,
        "publishedAt": "2026-10-24T16:00:00+08:00",
        "originalUrl": "https://insuranceasianews.com/asian-regulators-race-to-unlock-the-captive-boom/",
        "sourceKey": "ian",
        "sourceTier": "pro",
        "score": 74,
        "boards": ["reg", "market"],
        "themes": ["专属自保", "PCC", "风险管理中心"],
        "title": {
            "sc": "亚洲监管竞逐专属自保　香港拟修例引入PCC、目标一年半内翻倍",
            "tc": "亞洲監管競逐專屬自保　香港擬修例引入PCC、目標一年半內翻倍"
        },
        "summary": {
            "sc": "全球自保公司2025年增至6549家、升3.8%，亚太仅207家、占3.2%。日本拟建本土再保险型自保制度（最多162家日企已在夏威夷等地设自保），新加坡、纳闽、香港同场竞争。香港拟修例引入PCC结构，保监局目标12至18个月内自保数目翻倍。[EN原文]",
            "tc": "全球自保公司2025年增至6549家、升3.8%，亞太僅207家、佔3.2%。日本擬建本土再保險型自保制度（最多162家日企已在夏威夷等地設自保），新加坡、納閩、香港同場競爭。香港擬修例引入PCC結構，保監局目標12至18個月內自保數目翻倍。[EN原文]"
        },
        "why": {
            "sc": "香港「国际风险管理中心」从口号走向制度供给的进度条：PCC 一旦落地，企业可把巨灾、网络等难保风险自留，直接改变经纪的企业险组合。适合与准备设自保的企业客户、家办做前瞻沟通，也是判断保监局未来一年半监管重点的依据。",
            "tc": "香港「國際風險管理中心」從口號走向制度供給的進度條：PCC 一旦落地，企業可把巨災、網絡等難保風險自留，直接改變經紀的企業險組合。適合與準備設自保的企業客戶、家辦做前瞻溝通，也是判斷保監局未來一年半監管重點的依據。"
        },
        "tags": {
            "sc": ["专属自保", "PCC", "香港机遇", "亚洲监管"],
            "tc": ["專屬自保", "PCC", "香港機遇", "亞洲監管"]
        },
        "actions": {
            "front": {"sc": "企业客户沟通：自留风险的边界", "tc": "企業客戶溝通：自留風險的邊界"},
            "midback": {"sc": "产品研究：自保与保单组合", "tc": "產品研究：自保與保單組合"},
            "lead": {"sc": "团队简报：香港制度供给", "tc": "團隊簡報：香港制度供給"},
            "cross": {"sc": "跨境企业与家办", "tc": "跨境企業與家辦"}
        },
        "rolesImpact": {"front": 1, "midback": 2, "lead": 2, "cross": 2},
        "source": {"sc": "InsuranceAsia News 2026-10-24", "tc": "InsuranceAsia News 2026-10-24",
                   "name": "ian", "date": "2026-10-24", "lang": "en"},
        "lang": "en"
    },
    {
        "id": "ibm-china-15fyp-insurance-roadmap-20261024",
        "clusterCount": 1,
        "verifyStatus": "verified",
        "contentKind": "news",
        "ingestedAt": INGEST,
        "publishedAt": "2026-10-24T01:14:00+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/foreign-brokers-gain-wider-access-in-chinas-us850bn-insurance-market-594812.aspx",
        "sourceKey": "ibm",
        "sourceTier": "media",
        "score": 66,
        "boards": ["reg", "market"],
        "themes": ["十五五", "对外开放", "再保险"],
        "title": {
            "sc": "内地保险业「十五五」路线图出炉　主线扩大外资参与、再保分出首破千亿",
            "tc": "內地保險業「十五五」路線圖出爐　主線擴大外資參與、再保分出首破千億"
        },
        "summary": {
            "sc": "中国保险行业协会在金融街论坛发布「十五五」保险业高质量发展研究，由150余名专家历时半年完成，主线是扩大外资参与、市场改革与扩面。2025年全国保费约6.12万亿元（约8500亿美元）；财产险再保分出保费首度单半年破千亿元，2026年4月续转需求升约一成。[EN原文]",
            "tc": "中國保險行業協會在金融街論壇發布「十五五」保險業高質量發展研究，由150餘名專家歷時半年完成，主線是擴大外資參與、市場改革與擴面。2025年全國保費約6.12萬億元（約8500億美元）；財產險再保分出保費首度單半年破千億元，2026年4月續轉需求升約一成。[EN原文]"
        },
        "why": {
            "sc": "内地开放节奏决定港险中介与再保的分工：外资持牌路径一旦清晰，跨境安排与再保容量都会变。做跨境客户、与内地机构合作的团队要同步这条监管风向，也别把单一内地客源当成长期结构。",
            "tc": "內地開放節奏決定港險中介與再保的分工：外資持牌路徑一旦清晰，跨境安排與再保容量都會變。做跨境客戶、與內地機構合作的團隊要同步這條監管風向，也別把單一內地客源當成長期結構。"
        },
        "tags": {
            "sc": ["十五五", "对外开放", "再保险", "内地市场"],
            "tc": ["十五五", "對外開放", "再保險", "內地市場"]
        },
        "actions": {
            "front": {"sc": "客户沟通：跨境配置的政策节奏", "tc": "客戶溝通：跨境配置的政策節奏"},
            "midback": {"sc": "产品研究：再保容量变化", "tc": "產品研究：再保容量變化"},
            "lead": {"sc": "团队简报：内地开放路线", "tc": "團隊簡報：內地開放路線"},
            "cross": {"sc": "跨境与内地机构合作", "tc": "跨境與內地機構合作"}
        },
        "rolesImpact": {"front": 1, "midback": 1, "lead": 2, "cross": 2},
        "source": {"sc": "Insurance Business Asia 2026-10-24", "tc": "Insurance Business Asia 2026-10-24",
                   "name": "ibm", "date": "2026-10-24", "lang": "en"},
        "lang": "en"
    },
    {
        "id": "ibm-hk-gi-253-pecuniary-loss-20261024",
        "clusterCount": 1,
        "verifyStatus": "verified",
        "contentKind": "news",
        "ingestedAt": INGEST,
        "publishedAt": "2026-10-24T01:34:00+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/hong-kong-insurance-underwriting-profit-surges-253-as-market-posts-573-6b-in-premiums-594814.aspx",
        "sourceKey": "ibm",
        "sourceTier": "media",
        "score": 68,
        "boards": ["market"],
        "themes": ["一般险", "承保利润", "按揭保证"],
        "title": {
            "sc": "香港一般险承保利润升253%　一条 pecuniary loss 由蚀3亿转赚31亿",
            "tc": "香港一般險承保利潤升253%　一條 pecuniary loss 由蝕3億轉賺31億"
        },
        "summary": {
            "sc": "保监局上半年数据拆解：一般业务承保利润58亿元、升253.1%，在岸 pecuniary loss（含按揭保证）由去年同期亏损3亿元转为盈利31亿元，一项即贡献34亿元转向；一般业务经营利润96亿元升48.1%，毛保费637亿元升9.1%。[EN原文]",
            "tc": "保監局上半年數據拆解：一般業務承保利潤58億元、升253.1%，在岸 pecuniary loss（含按揭保證）由去年同期虧損3億元轉為盈利31億元，一項即貢獻34億元轉向；一般業務經營利潤96億元升48.1%，毛保費637億元升9.1%。[EN原文]"
        },
        "why": {
            "sc": "同一份保监局数据，这条补上「利润从哪来」：单一险种（按揭保证）决定了一般险整体盈亏。做企业险与银保渠道的团队，可据此判断承保胃口与条款松紧，而不是只看总保费增速。",
            "tc": "同一份保監局數據，這條補上「利潤從哪來」：單一險種（按揭保證）決定了一般險整體盈虧。做企業險與銀保渠道的團隊，可據此判斷承保胃口與條款鬆緊，而不是只看總保費增速。"
        },
        "tags": {
            "sc": ["一般险", "承保利润", "按揭保证", "半年数据"],
            "tc": ["一般險", "承保利潤", "按揭保證", "半年數據"]
        },
        "actions": {
            "front": {"sc": "客户沟通：企业险条款走向", "tc": "客戶溝通：企業險條款走向"},
            "midback": {"sc": "产品研究：承保胃口判断", "tc": "產品研究：承保胃口判斷"},
            "lead": {"sc": "团队简报：数据归因", "tc": "團隊簡報：數據歸因"},
            "cross": {"sc": "银行与按揭渠道", "tc": "銀行與按揭渠道"}
        },
        "rolesImpact": {"front": 1, "midback": 2, "lead": 2, "cross": 1},
        "source": {"sc": "Insurance Business Asia 2026-10-24", "tc": "Insurance Business Asia 2026-10-24",
                   "name": "ibm", "date": "2026-10-24", "lang": "en"},
        "lang": "en"
    },
    {
        "id": "scmp-hsbc-abu-dhabi-wealth-centre-20261024",
        "clusterCount": 1,
        "verifyStatus": "verified",
        "contentKind": "news",
        "ingestedAt": INGEST,
        "publishedAt": "2026-10-24T14:00:00+08:00",
        "originalUrl": "https://www.scmp.com/business/article/3371958/hsbc-open-new-wealth-centre-abu-dhabi-despite-regional-conflict",
        "sourceKey": "scmp",
        "sourceTier": "media",
        "score": 62,
        "boards": ["market", "family"],
        "themes": ["家族办公室", "财富管理", "中东"],
        "title": {
            "sc": "滙豐12月在阿布扎比开财富中心　称中东高净值需求未受战事拖累",
            "tc": "滙豐12月在阿布扎比開財富中心　稱中東高淨值需求未受戰事拖累"
        },
        "summary": {
            "sc": "滙豐阿联酋CEO表示，12月将在阿布扎比开设财富管理中心，属该行二十年来中东最大投资的一部分，去年已在迪拜设首个区域财富中心。美以对伊朗战事自2月底持续，但上半年当地高净值新客仍大增；他称客户仍经新加坡、香港、伦敦、日内瓦分散配置，亦有更多转投区内。[EN原文]",
            "tc": "滙豐阿聯酋CEO表示，12月將在阿布扎比開設財富管理中心，屬該行二十年來中東最大投資的一部分，去年已在迪拜設首個區域財富中心。美以對伊朗戰事自2月底持續，但上半年當地高淨值新客仍大增；他稱客戶仍經新加坡、香港、倫敦、日內瓦分散配置，亦有更多轉投區內。[EN原文]"
        },
        "why": {
            "sc": "中东正在从「资金来源地」变成「财富管理中心」，与香港争同一批高净值客户。做跨境高客与家办业务的团队，可用这条提醒客户比较各中心在税务、私隐与服务成本上的差别，而不是默认香港是唯一选项。",
            "tc": "中東正在從「資金來源地」變成「財富管理中心」，與香港爭同一批高淨值客戶。做跨境高客與家辦業務的團隊，可用這條提醒客戶比較各中心在稅務、私隱與服務成本上的差別，而不是默認香港是唯一選項。"
        },
        "tags": {
            "sc": ["家族办公室", "财富管理", "中东", "客户竞争"],
            "tc": ["家族辦公室", "財富管理", "中東", "客戶競爭"]
        },
        "actions": {
            "front": {"sc": "高客沟通：财富中心比较", "tc": "高客溝通：財富中心比較"},
            "midback": {"sc": "研究：跨境配置地选择", "tc": "研究：跨境配置地選擇"},
            "lead": {"sc": "团队简报：区域竞争", "tc": "團隊簡報：區域競爭"},
            "cross": {"sc": "跨境高客与家办", "tc": "跨境高客與家辦"}
        },
        "rolesImpact": {"front": 2, "midback": 1, "lead": 1, "cross": 2},
        "source": {"sc": "South China Morning Post 2026-10-24", "tc": "South China Morning Post 2026-10-24",
                   "name": "scmp", "date": "2026-10-24", "lang": "en"},
        "lang": "en"
    },
    {
        "id": "ibm-bangladesh-idra-cooling-off-20261023",
        "clusterCount": 1,
        "verifyStatus": "verified",
        "contentKind": "news",
        "ingestedAt": INGEST,
        "publishedAt": "2026-10-23T23:45:00+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/life-insurance/bangladesh-claims-delays-now-block-brokers-from-writing-new-policies-594791.aspx",
        "sourceKey": "ibm",
        "sourceTier": "media",
        "score": 64,
        "boards": ["reg"],
        "themes": ["理赔监管", "分销限制", "亚洲市场"],
        "title": {
            "sc": "孟加拉IDRA：保司理赔慢　经纪对新客出单最长被冻结180天",
            "tc": "孟加拉IDRA：保司理賠慢　經紀對新客出單最長被凍結180天"
        },
        "summary": {
            "sc": "IDRA 10月15日通函禁止保司把赔款与新单捆绑，并设冷却期：90天内结案无限制；90至120天结案者，赔款起30天内不得再向该客户出单，逾120天则180天。整体寿险理赔率由2020年85%跌至2025年66%，问题保司Baira Life仅1.6%，MetLife孟加拉98.3%。[EN原文]",
            "tc": "IDRA 10月15日通函禁止保司把賠款與新單捆綁，並設冷卻期：90天內結案無限制；90至120天結案者，賠款起30天內不得再向該客戶出單，逾120天則180天。整體壽險理賠率由2020年85%跌至2025年66%，問題保司Baira Life僅1.6%，MetLife孟加拉98.3%。[EN原文]"
        },
        "why": {
            "sc": "罕见的「理赔表现直接限制分销」监管样本，给出可复用的选品框架：先看理赔时效，再看佣金与产品。香港目前靠 GN16 与理赔统计披露，尚未走到限制出单，正好用来做对照客户教育。",
            "tc": "罕見的「理賠表現直接限制分銷」監管樣本，給出可複用的選品框架：先看理賠時效，再看佣金與產品。香港目前靠 GN16 與理賠統計披露，尚未走到限制出單，正好用來做對照客戶教育。"
        },
        "tags": {
            "sc": ["理赔监管", "分销限制", "选品", "亚洲市场"],
            "tc": ["理賠監管", "分銷限制", "選品", "亞洲市場"]
        },
        "actions": {
            "front": {"sc": "客户教育：理赔时效优先", "tc": "客戶教育：理賠時效優先"},
            "midback": {"sc": "产品研究：保司理赔比较", "tc": "產品研究：保司理賠比較"},
            "lead": {"sc": "团队培训：选品框架", "tc": "團隊培訓：選品框架"},
            "cross": {"sc": "合规与培训", "tc": "合規與培訓"}
        },
        "rolesImpact": {"front": 2, "midback": 1, "lead": 2, "cross": 1},
        "source": {"sc": "Insurance Business Asia 2026-10-23", "tc": "Insurance Business Asia 2026-10-23",
                   "name": "ibm", "date": "2026-10-23", "lang": "en"},
        "lang": "en"
    },
    {
        "id": "ibm-willis-defence-security-unit-20261023",
        "clusterCount": 1,
        "verifyStatus": "verified",
        "contentKind": "news",
        "ingestedAt": INGEST,
        "publishedAt": "2026-10-23T11:37:00+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/willis-launches-defence-unit-as-asian-spending-hits-record-rise-594694.aspx",
        "sourceKey": "ibm",
        "sourceTier": "media",
        "score": 63,
        "boards": ["product", "market"],
        "themes": ["国防保险", "特殊风险", "军费"],
        "title": {
            "sc": "韦莱设全球国防与安全专组　亚洲军费2025年升8.1%至6810亿美元",
            "tc": "韋萊設全球國防與安全專組　亞洲軍費2025年升8.1%至6810億美元"
        },
        "summary": {
            "sc": "WTW旗下韦莱（Willis）成立全球国防与安全业务，整合风险转移、网络、危机管理、理赔与风险工程等能力，覆盖140个国家，由 Jennifer Caldarella 领军。据SIPRI，2025年亚洲及大洋洲军费达6810亿美元、按年升8.1%，为2009年以来最大升幅；无人机与AI带来传统风险管理未覆盖的敞口。[EN原文]",
            "tc": "WTW旗下韋萊（Willis）成立全球國防與安全業務，整合風險轉移、網絡、危機管理、理賠與風險工程等能力，覆蓋140個國家，由 Jennifer Caldarella 領軍。據SIPRI，2025年亞洲及大洋洲軍費達6810億美元、按年升8.1%，為2009年以來最大升幅；無人機與AI帶來傳統風險管理未覆蓋的敞口。[EN原文]"
        },
        "why": {
            "sc": "国防产业链是典型的「保费大、供给小」赛道：需求随军费上行，但多数保司不敢承接。企业险与专业险团队可留意相关供应链企业的保险安排缺口，也可作为与客户谈风险格局变化的素材。",
            "tc": "國防產業鏈是典型的「保費大、供給小」賽道：需求隨軍費上行，但多數保司不敢承接。企業險與專業險團隊可留意相關供應鏈企業的保險安排缺口，也可作為與客戶談風險格局變化的素材。"
        },
        "tags": {
            "sc": ["国防保险", "特殊风险", "军费", "产品缺口"],
            "tc": ["國防保險", "特殊風險", "軍費", "產品缺口"]
        },
        "actions": {
            "front": {"sc": "客户沟通：风险格局变化", "tc": "客戶溝通：風險格局變化"},
            "midback": {"sc": "产品研究：特殊风险承接", "tc": "產品研究：特殊風險承接"},
            "lead": {"sc": "团队简报：新赛道", "tc": "團隊簡報：新賽道"},
            "cross": {"sc": "工业企业客户", "tc": "工業企業客戶"}
        },
        "rolesImpact": {"front": 1, "midback": 1, "lead": 1, "cross": 2},
        "source": {"sc": "Insurance Business Asia 2026-10-23", "tc": "Insurance Business Asia 2026-10-23",
                   "name": "ibm", "date": "2026-10-23", "lang": "en"},
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

# last-check 全信源回写
lc = json.load(open('data/last-check.json', encoding='utf-8'))
lc['lastCheck'] = INGEST
for k in lc.get('sources', {}):
    lc['sources'][k]['last'] = INGEST
json.dump(lc, open('data/last-check.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

print('added', len(added), added)
print('total', n, 'lastCheck', lc['lastCheck'])
print('--- top 10 ---')
for it in items[:10]:
    print(it['publishedAt'][:16], '|', it['id'], '|', it['title']['sc'][:46])
