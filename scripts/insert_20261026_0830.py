#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-26 08:xx 每日增量：插入 6 条（10-25 晚至 10-26 早）"""
import json
import datetime

NOW = datetime.datetime.now().astimezone()
INGEST = NOW.isoformat(timespec='seconds')
PATH = 'data/live-items.json'

new_items = [
    {
        "id": "iasia-sme-cyber-3in10-uninsured-20261026",
        "clusterCount": 1,
        "verifyStatus": "verified",
        "contentKind": "news",
        "ingestedAt": INGEST,
        "publishedAt": "2026-10-26T06:00:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/3-in-10-uninsured-firms-dismiss-cyberattack-risks-globaldata",
        "sourceKey": "insuranceasia",
        "sourceTier": "media",
        "score": 66,
        "boards": ["product", "market"],
        "themes": ["网络安全险", "中小企业", "AI钓鱼"],
        "title": {
            "sc": "三成未投保中小企自认不会被针对　GlobalData：AI把「低调」变成劣势",
            "tc": "三成未投保中小企自認不會被針對　GlobalData：AI把「低調」變成劣勢"
        },
        "summary": {
            "sc": "GlobalData 2025年中小企业调查显示，没有网络安全险的受访者中27%认为「自己不太可能被攻击」，其余不投保原因包括难找合适保单、自认已有足够保障。Coalition数据指2025年下半年商业电邮诈骗（BEC）理赔较2024年同期升约30%，升势延续至2026年，微型企业受冲击不成比例。分析师建议保司简化条款，把BEC与转账欺诈纳入标准商业险。[EN原文]",
            "tc": "GlobalData 2025年中小企業調查顯示，沒有網絡安全險的受訪者中27%認為「自己不太可能被攻擊」，其餘不投保原因包括難找合適保單、自認已有足夠保障。Coalition數據指2025年下半年商業電郵詐騙（BEC）理賠較2024年同期升約30%，升勢延續至2026年，微型企業受衝擊不成比例。分析師建議保司簡化條款，把BEC與轉帳欺詐納入標準商業險。[EN原文]"
        },
        "why": {
            "sc": "企业险的真正缺口不在产品供给，而在客户的风险认知：客户觉得「我太小没人盯上」。生成式AI已经把攻击边际成本压到近乎零，这个认知正在变成实际敞口。团队可用这条做SME客户的破冰素材——先讲BEC与转账欺诈的具体场景，再谈保单，比讲保额有效。",
            "tc": "企業險的真正缺口不在產品供給，而在客戶的風險認知：客戶覺得「我太小沒人盯上」。生成式AI已把攻擊邊際成本壓到近乎零，這個認知正在變成實際敞口。團隊可用這條做SME客戶的破冰素材——先講BEC與轉帳欺詐的具體場景，再談保單，比講保額有效。"
        },
        "tags": {
            "sc": ["网络安全险", "中小企业", "商业电邮诈骗", "责任险"],
            "tc": ["網絡安全險", "中小企業", "商業電郵詐騙", "責任險"]
        },
        "actions": {
            "front": {"sc": "客户沟通：BEC与转账欺诈场景", "tc": "客戶溝通：BEC與轉帳欺詐場景"},
            "midback": {"sc": "产品研究：商业险套餐边界", "tc": "產品研究：商業險套餐邊界"},
            "lead": {"sc": "团队培训：SME风险认知", "tc": "團隊培訓：SME風險認知"},
            "cross": {"sc": "企业客户与银行渠道", "tc": "企業客戶與銀行渠道"}
        },
        "rolesImpact": {"front": 2, "midback": 1, "lead": 1, "cross": 1},
        "source": {"sc": "Insurance Asia 2026-10-26", "tc": "Insurance Asia 2026-10-26",
                   "name": "insuranceasia", "date": "2026-10-26", "lang": "en"},
        "lang": "en"
    },
    {
        "id": "iasia-jefferies-asia-life-regulatory-risk-20261026",
        "clusterCount": 1,
        "verifyStatus": "verified",
        "contentKind": "news",
        "ingestedAt": INGEST,
        "publishedAt": "2026-10-26T05:45:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/regulatory-risks-threaten-asian-insurers-growth-jefferies",
        "sourceKey": "insuranceasia",
        "sourceTier": "pro",
        "score": 70,
        "boards": ["market", "insurer"],
        "themes": ["亚洲寿险", "监管风险", "估值"],
        "title": {
            "sc": "Jefferies：监管摩擦叠加高基数　AIA、保诚2026年增长承压",
            "tc": "Jefferies：監管摩擦疊加高基數　AIA、保誠2026年增長承壓"
        },
        "summary": {
            "sc": "Jefferies研究报告指，亚洲寿险（含AIA、保诚）的主要风险来自近期监管关注与2026年艰难同比基数；一般投资者仍普遍怀疑亚洲增长动能能否延续。泰国因本地信贷特性跑输区域；香港与内地面对内需偏弱；东南亚、韩国、台湾扩张与美国AI相关资本开支高度挂钩，韩国3%至4%增长亦系于全球供应链。[EN原文]",
            "tc": "Jefferies研究報告指，亞洲壽險（含AIA、保誠）的主要風險來自近期監管關注與2026年艱難同比基數；一般投資者仍普遍懷疑亞洲增長動能能否延續。泰國因本地信貸特性跑輸區域；香港與內地面對內需偏弱；東南亞、韓國、台灣擴張與美國AI相關資本開支高度掛鈎，韓國3%至4%增長亦繫於全球供應鏈。[EN原文]"
        },
        "why": {
            "sc": "卖方开始把「监管摩擦」列为亚洲寿险的首要变量，而不是增长故事：一旦监管关注落到分红实现率、销售行为或跨境保单，直接影响就是产品节奏与佣金结构。团队做年度规划时，宜把监管情景写进假设，而不是只按保费增速推演。",
            "tc": "賣方開始把「監管摩擦」列為亞洲壽險的首要變量，而不是增長故事：一旦監管關注落到分紅實現率、銷售行為或跨境保單，直接影響就是產品節奏與佣金結構。團隊做年度規劃時，宜把監管情景寫進假設，而不是只按保費增速推演。"
        },
        "tags": {
            "sc": ["亚洲寿险", "监管风险", "估值", "卖方研究"],
            "tc": ["亞洲壽險", "監管風險", "估值", "賣方研究"]
        },
        "actions": {
            "front": {"sc": "高客沟通：监管情景说明", "tc": "高客溝通：監管情景說明"},
            "midback": {"sc": "产品研究：监管假设入模", "tc": "產品研究：監管假設入模"},
            "lead": {"sc": "团队简报：年度规划变量", "tc": "團隊簡報：年度規劃變量"},
            "cross": {"sc": "跨境客户与投资端", "tc": "跨境客戶與投資端"}
        },
        "rolesImpact": {"front": 1, "midback": 2, "lead": 2, "cross": 1},
        "source": {"sc": "Insurance Asia 2026-10-26", "tc": "Insurance Asia 2026-10-26",
                   "name": "insuranceasia", "date": "2026-10-26", "lang": "en"},
        "lang": "en"
    },
    {
        "id": "iasia-pingan-good-doctor-ai-profit-20261026",
        "clusterCount": 1,
        "verifyStatus": "verified",
        "contentKind": "news",
        "ingestedAt": INGEST,
        "publishedAt": "2026-10-26T05:30:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/ping-good-doctor-profit-rises-35-amidst-ai-healthcare-push",
        "sourceKey": "insuranceasia",
        "sourceTier": "insurer",
        "score": 66,
        "boards": ["tech", "market"],
        "themes": ["AI医疗", "健康管理", "平安"],
        "title": {
            "sc": "平安好医生首三季净利升35%　AI医生用户近1300万",
            "tc": "平安好醫生首三季淨利升35%　AI醫生用戶近1300萬"
        },
        "summary": {
            "sc": "平安健康医疗科技（1833.HK）公布2026年首三季净利2.5亿元人民币（约3730万美元），按年升35%；收入35.1亿元（约5.24亿美元）。期内AI医生服务用户近1300万人；AI辅助多学科会诊平台截至9月底覆盖四大类疾病，复杂疾病诊疗方案准确率约90%。[EN原文]",
            "tc": "平安健康醫療科技（1833.HK）公布2026年首三季淨利2.5億元人民幣（約3,730萬美元），按年升35%；收入35.1億元（約5.24億美元）。期內AI醫生服務用戶近1,300萬人；AI輔助多學科會診平台截至9月底覆蓋四大類疾病，複雜疾病診療方案準確率約90%。[EN原文]"
        },
        "why": {
            "sc": "「保险+健康管理」的AI版本正在跑出真实收入：AI医生用户规模与三甲多学科会诊的准确率，是判断健康险服务包能否降本的两个硬指标。做医疗险、重疾险附加服务的团队，可直接对照看自家服务供应商处于什么水平。",
            "tc": "「保險+健康管理」的AI版本正在跑出真實收入：AI醫生用戶規模與三甲多學科會診的準確率，是判斷健康險服務包能否降本的兩個硬指標。做醫療險、重疾險附加服務的團隊，可直接對照看自家服務供應商處於什麼水平。"
        },
        "tags": {
            "sc": ["AI医疗", "健康管理", "健康险", "平安"],
            "tc": ["AI醫療", "健康管理", "健康險", "平安"]
        },
        "actions": {
            "front": {"sc": "客户沟通：健康管理附加值", "tc": "客戶溝通：健康管理附加值"},
            "midback": {"sc": "产品研究：附加服务成本", "tc": "產品研究：附加服務成本"},
            "lead": {"sc": "团队简报：AI医疗服务", "tc": "團隊簡報：AI醫療服務"},
            "cross": {"sc": "医疗健康生态合作", "tc": "醫療健康生態合作"}
        },
        "rolesImpact": {"front": 1, "midback": 2, "lead": 1, "cross": 1},
        "source": {"sc": "Insurance Asia 2026-10-26", "tc": "Insurance Asia 2026-10-26",
                   "name": "insuranceasia", "date": "2026-10-26", "lang": "en"},
        "lang": "en"
    },
    {
        "id": "iasia-gallagher-re-cat-losses-92b-20261026",
        "clusterCount": 1,
        "verifyStatus": "verified",
        "contentKind": "news",
        "ingestedAt": INGEST,
        "publishedAt": "2026-10-26T05:15:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/global-insured-catastrophe-losses-fall-92b-in-2026",
        "sourceKey": "insuranceasia",
        "sourceTier": "pro",
        "score": 72,
        "boards": ["market", "product"],
        "themes": ["巨灾损失", "再保容量", "2027续保"],
        "title": {
            "sc": "Gallagher Re：首三季保险损失约920亿美元　2019年以来最低",
            "tc": "Gallagher Re：首三季保險損失約920億美元　2019年以來最低"
        },
        "summary": {
            "sc": "Gallagher Re《2026年第三季自然灾害与气候报告》（10月21日发布）：首三季全球自然灾害经济损失至少2420亿美元，保险损失约920亿美元，分别为2015年及2019年以来同期最低。第三季为连续第六个季度无单一巨灾造成逾100亿美元保险损失；强对流风暴占全球保险损失近六成，仅美国即逾430亿美元。[EN原文]",
            "tc": "Gallagher Re《2026年第三季自然災害與氣候報告》（10月21日發布）：首三季全球自然災害經濟損失至少2,420億美元，保險損失約920億美元，分別為2015年及2019年以來同期最低。第三季為連續第六個季度無單一巨災造成逾100億美元保險損失；強對流風暴佔全球保險損失近六成，僅美國即逾430億美元。[EN原文]"
        },
        "why": {
            "sc": "低损失周期直接决定明年1月1日续保的议价空间：再保容量充裕、盈利强，买方杠杆更大。但报告同时提示强厄尔尼诺可能在2027年成形——现在是锁定多年期条件较好的窗口，别把连续六个季度的平静当成常态。",
            "tc": "低損失周期直接決定明年1月1日續保的議價空間：再保容量充裕、盈利強，買方槓桿更大。但報告同時提示強厄爾尼諾可能在2027年成形——現在是鎖定多年期條件較好的窗口，別把連續六個季度的平靜當成常態。"
        },
        "tags": {
            "sc": ["巨灾损失", "再保容量", "厄尔尼诺", "续保谈判"],
            "tc": ["巨災損失", "再保容量", "厄爾尼諾", "續保談判"]
        },
        "actions": {
            "front": {"sc": "企业客户：续保时机说明", "tc": "企業客戶：續保時機說明"},
            "midback": {"sc": "产品研究：再保条件与定价", "tc": "產品研究：再保條件與定價"},
            "lead": {"sc": "团队简报：巨灾周期", "tc": "團隊簡報：巨災周期"},
            "cross": {"sc": "再保与ILS投资", "tc": "再保與ILS投資"}
        },
        "rolesImpact": {"front": 1, "midback": 2, "lead": 1, "cross": 2},
        "source": {"sc": "Insurance Asia 2026-10-26", "tc": "Insurance Asia 2026-10-26",
                   "name": "insuranceasia", "date": "2026-10-26", "lang": "en"},
        "lang": "en"
    },
    {
        "id": "ian-energy-transition-parametric-basis-risk-20261026",
        "clusterCount": 1,
        "verifyStatus": "pending",
        "contentKind": "news",
        "ingestedAt": INGEST,
        "publishedAt": "2026-10-26T07:30:52+08:00",
        "originalUrl": "https://insuranceasianews.com/231651-2/",
        "sourceKey": "insuranceasianews",
        "sourceTier": "pro",
        "score": 72,
        "boards": ["product", "market"],
        "themes": ["能源转型", "参数保险", "基差风险"],
        "title": {
            "sc": "能源转型重塑承保风险　参数保险走向主流、基差风险仍是硬伤",
            "tc": "能源轉型重塑承保風險　參數保險走向主流、基差風險仍是硬傷"
        },
        "summary": {
            "sc": "InsuranceAsia News分析（作者Roshan Nambiar）指，能源转型正在重塑保险风险：供应链仍有大量未投保敞口，模型主导定价，参数保险逐步走向主流，但基差风险仍被视为最主要局限。文章梳理 Gallagher Re、Howden、Marsh Re、WTW、Twelve Securis 等机构观点，归类为巨灾与气候专题。（全文在付费墙后）[EN原文]",
            "tc": "InsuranceAsia News分析（作者Roshan Nambiar）指，能源轉型正在重塑保險風險：供應鏈仍有大量未投保敞口，模型主導定價，參數保險逐步走向主流，但基差風險仍被視為最主要局限。文章梳理 Gallagher Re、Howden、Marsh Re、WTW、Twelve Securis 等機構觀點，歸類為巨災與氣候專題。（全文在付費牆後）[EN原文]"
        },
        "why": {
            "sc": "转型风险（而非天灾）才是企业客户未来十年的主战场：新能源供应链跨度长、单点事故损失大，传统财产险难以覆盖。参数保险能补缺口，但「赔了不等于损失全补」的基差风险必须提前讲清，否则容易变成理赔争议。",
            "tc": "轉型風險（而非天災）才是企業客戶未來十年的主戰場：新能源供應鏈跨度長、單點事故損失大，傳統財產險難以覆蓋。參數保險能補缺口，但「賠了不等於損失全補」的基差風險必須提前講清，否則容易變成理賠爭議。"
        },
        "tags": {
            "sc": ["能源转型", "参数保险", "基差风险", "企业险"],
            "tc": ["能源轉型", "參數保險", "基差風險", "企業險"]
        },
        "actions": {
            "front": {"sc": "客户沟通：参数保险赔付逻辑", "tc": "客戶溝通：參數保險賠付邏輯"},
            "midback": {"sc": "产品研究：基差风险测算", "tc": "產品研究：基差風險測算"},
            "lead": {"sc": "团队培训：转型风险", "tc": "團隊培訓：轉型風險"},
            "cross": {"sc": "新能源与基建客户", "tc": "新能源與基建客戶"}
        },
        "rolesImpact": {"front": 1, "midback": 2, "lead": 2, "cross": 2},
        "source": {"sc": "InsuranceAsia News 2026-10-26", "tc": "InsuranceAsia News 2026-10-26",
                   "name": "insuranceasianews", "date": "2026-10-26", "lang": "en"},
        "lang": "en"
    },
    {
        "id": "scmp-goldman-asia-wealth-hiring-20261026",
        "clusterCount": 1,
        "verifyStatus": "verified",
        "contentKind": "news",
        "ingestedAt": INGEST,
        "publishedAt": "2026-10-26T08:00:00+08:00",
        "originalUrl": "https://www.scmp.com/business/china-business/article/3372055/goldman-sachs-steps-asia-hiring-wealthy-clients-eye-us-assets-diversification",
        "sourceKey": "scmp",
        "sourceTier": "media",
        "score": 62,
        "boards": ["market", "family"],
        "themes": ["财富管理", "家族办公室", "高净值"],
        "title": {
            "sc": "高盛亚洲加码招聘财富顾问　称富豪家族转向美元资产、AI造新富",
            "tc": "高盛亞洲加碼招聘財富顧問　稱富豪家族轉向美元資產、AI造新富"
        },
        "summary": {
            "sc": "高盛全球财富管理联席主管 Nishi Somaiya 上任后首度访港表示，将在香港、新加坡及澳洲扩充顾问团队，并在交易、贷款等专业领域增聘人手；该行亚洲财富管理业务过去数年录双位数增长，目标维持。客户在多年市场升幅后增加配置美国资产分散风险，AI热潮则催生新一批百万富翁，理财规划需求上升。[EN原文]",
            "tc": "高盛全球財富管理聯席主管 Nishi Somaiya 上任後首度訪港表示，將在香港、新加坡及澳洲擴充顧問團隊，並在交易、貸款等專業領域增聘人手；該行亞洲財富管理業務過去數年錄雙位數增長，目標維持。客戶在多年市場升幅後增加配置美國資產分散風險，AI熱潮則催生新一批百萬富翁，理財規劃需求上升。[EN原文]"
        },
        "why": {
            "sc": "「AI造富＋美元分散」是今年高净值客户需求的两条主线，也是私行与保险经纪抢同一批客户的战场。做高客与家办的团队可据此调整话题顺序：先谈资产分散与传承结构，再谈保障，而不是反过来。",
            "tc": "「AI造富＋美元分散」是今年高淨值客戶需求的兩條主線，也是私行與保險經紀搶同一批客戶的戰場。做高客與家辦的團隊可據此調整話題順序：先談資產分散與傳承結構，再談保障，而不是反過來。"
        },
        "tags": {
            "sc": ["财富管理", "家族办公室", "高净值", "资产分散"],
            "tc": ["財富管理", "家族辦公室", "高淨值", "資產分散"]
        },
        "actions": {
            "front": {"sc": "高客沟通：分散与传承话题", "tc": "高客溝通：分散與傳承話題"},
            "midback": {"sc": "研究：私行与经纪分工", "tc": "研究：私行與經紀分工"},
            "lead": {"sc": "团队简报：高客需求变化", "tc": "團隊簡報：高客需求變化"},
            "cross": {"sc": "家办与跨境高客", "tc": "家辦與跨境高客"}
        },
        "rolesImpact": {"front": 2, "midback": 1, "lead": 1, "cross": 2},
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
