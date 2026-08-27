#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""0826 daily ingest: prepend 11 new items, update meta."""
import json, datetime

NOW = datetime.datetime(2026, 8, 26, 14, 25, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
INGEST = NOW.strftime('%Y-%m-%dT%H:%M:%S+08:00')

def mk(iid, score, verify, tier, key, t_sc, t_tc, s_sc, s_tc, w_sc, w_tc,
       actions, roles, src_sc, lang, boards, themes, tags_sc, tags_tc,
       kind, pub, url):
    return {
        "id": iid, "clusterCount": 1, "score": score, "verifyStatus": verify,
        "sourceTier": tier, "sourceKey": key,
        "title": {"sc": t_sc, "tc": t_tc},
        "summary": {"sc": s_sc, "tc": s_tc},
        "why": {"sc": w_sc, "tc": w_tc},
        "actions": actions,
        "rolesImpact": roles,
        "source": {"sc": src_sc, "lang": lang},
        "boards": boards, "themes": themes,
        "tags": {"sc": tags_sc, "tc": tags_tc},
        "contentKind": kind, "publishedAt": pub, "originalUrl": url,
        "ingestedAt": INGEST,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False, "evergreen": False,
    }

new_items = [
    mk("iaa-manulife-ai-20260826", 74, "verified", "media", "insuranceasia",
       "宏利亚洲全面铺开AI 目标2027年AI驱动价值超10亿美元 [EN原文]",
       "宏利亞洲全面鋪開AI 目標2027年AI驅動價值超10億美元 [EN原文]",
       "宏利亚洲总裁Steve Finch接受InsuranceAsia专访：集团把AI工具扩展至亚洲健康、财富及保障三大业务，目标2027年AI驱动价值逾10亿美元，并推动亚洲贡献集团核心盈利一半；强调成为AI驱动组织是战略优先。",
       "宏利亞洲總裁Steve Finch接受InsuranceAsia專訪：集團把AI工具擴展至亞洲健康、財富及保障三大業務，目標2027年AI驅動價值逾10億美元，並推動亞洲貢獻集團核心盈利一半；強調成為AI驅動組織是戰略優先。",
       "宏利是香港主要保司，其AI战略与人才布局反映港险数字化竞争方向，对中后台流程自动化与分销效率提升有参照价值。",
       "宏利是香港主要保司，其AI戰略與人才佈局反映港險數碼化競爭方向，對中後台流程自動化與分銷效率提升有參照價值。",
       {"front": {"sc": "AI赋能销售工具趋势观察", "tc": "AI賦能銷售工具趨勢觀察"},
        "midback": {"sc": "AI中后台与理赔流程对标参考", "tc": "AI中後台與理賠流程對標參考"},
        "lead": {}, "cross": {}},
       {"front": 1, "midback": 1, "lead": 0, "cross": 0},
       "InsuranceAsia", "en", ["insurer", "tech"], ["ai", "tech"],
       ["宏利", "AI", "数字化转型"], ["宏利", "AI", "數碼轉型"],
       "news", "2026-08-26T05:00:00+08:00",
       "https://insuranceasia.com/insurance/exclusive/manulife-asia-pushes-ai-drive-health-wealth-growth"),

    mk("iaa-tw-spillover-152-20260826", 66, "verified", "media", "insuranceasia",
       "台湾「溢出效应」保单上半年新单保费飙152% 发单74.6万件 [EN原文]",
       "台灣「溢出效應」保單上半年新單保費飆152% 發單74.6萬件 [EN原文]",
       "台湾金管会数据：2026上半年台湾寿险「溢出效应」保单首年保费收入按年升152%，发单74.59万件增29%，实物给付型保单销售回落；截至二季度末15家寿险公司共338款溢出效应产品获批或受理。",
       "台灣金管會數據：2026上半年台灣壽險「溢出效應」保單首年保費收入按年升152%，發單74.59萬件增29%，實物給付型保單銷售回落；截至第二季末15家壽險公司共338款溢出效應產品獲批或受理。",
       "溢出效应保单反映高净值客户跨境配置与保单融资需求，与港险跨境储蓄险的竞争格局直接相关。",
       "溢出效應保單反映高淨值客戶跨境配置與保單融資需求，與港險跨境儲蓄險的競爭格局直接相關。",
       {"front": {"sc": "跨境客户需求动向观察", "tc": "跨境客戶需求動向觀察"},
        "midback": {"sc": "竞品结构与定价参考", "tc": "競品結構與定價參考"},
        "lead": {}, "cross": {}},
       {"front": 1, "midback": 1, "lead": 0, "cross": 0},
       "InsuranceAsia", "en", ["market"], ["offshore", "market"],
       ["台湾", "溢出效应", "新单保费"], ["台灣", "溢出效應", "新單保費"],
       "stats", "2026-08-26T07:00:00+08:00",
       "https://insuranceasia.com/insurance/news/taiwan-spillover-effect-premiums-surge-152"),

    mk("iaa-tw-fc-life-20260826", 64, "verified", "media", "insuranceasia",
       "台湾外币保单前5月新单保费增54% 投资型与传统型齐升 [EN原文]",
       "台灣外幣保單前5月新單保費增54% 投資型與傳統型齊升 [EN原文]",
       "台湾寿险外币新保单首年保费今年前5个月约73.2亿美元，按年增54%；其中投资型外币保单贡献14.3亿美元，传统型需求同步回升，反映低利率环境下客户加大外币资产配置。",
       "台灣壽險外幣新保單首年保費今年前5個月約73.2億美元，按年增54%；其中投資型外幣保單貢獻14.3億美元，傳統型需求同步回升，反映低利率環境下客戶加大外幣資產配置。",
       "外币及多币种储蓄险是港险核心卖点之一，台湾外币保单放量印证亚洲客户外币配置趋势，可作产品与话术参考。",
       "外幣及多幣種儲蓄險是港險核心賣點之一，台灣外幣保單放量印證亞洲客戶外幣配置趨勢，可作產品與話術參考。",
       {"front": {"sc": "外币配置趋势素材", "tc": "外幣配置趨勢素材"},
        "midback": {"sc": "多币种产品对标", "tc": "多幣種產品對標"},
        "lead": {}, "cross": {}},
       {"front": 1, "midback": 1, "lead": 0, "cross": 0},
       "InsuranceAsia", "en", ["market"], ["fx", "macro"],
       ["外币保单", "台湾", "多币种"], ["外幣保單", "台灣", "多幣種"],
       "stats", "2026-08-26T06:15:00+08:00",
       "https://insuranceasia.com/insurance/news/taiwan-foreign-currency-life-premiums-surge-54-in-may-2026"),

    mk("iaa-id-health-copay-20260826", 66, "verified", "media", "insuranceasia",
       "印尼新规为健康险设5%共付上限 险企支持OJK第36号条例 [EN原文]",
       "印尼新規為健康險設5%共付上限 險企支持OJK第36號條例 [EN原文]",
       "印尼寿险协会(AAJI)表态支持金融服务管理局(OJK)第36/2025号条例：设门诊共付上限每案约16.9美元，并规范免赔额、保费复审及险企医疗与数字化能力，以应对医疗通胀与保费上升。",
       "印尼壽險協會(AAJI)表態支持金融服務管理局(OJK)第36/2025號條例：設門診共付上限每案約16.9美元，並規範免賠額、保費複審及險企醫療與數碼化能力，以應對醫療通脹與保費上升。",
       "东南亚健康险监管趋势（共付、医疗通胀管控）对港险医疗险产品设计与大湾区市场拓展有参照价值。",
       "東南亞健康險監管趨勢（共付、醫療通脹管控）對港險醫療險產品設計與大灣區市場拓展有參照價值。",
       {"front": {}, "midback": {"sc": "医疗险条款与定价参考", "tc": "醫療險條款與定價參考"},
        "lead": {}, "cross": {}},
       {"front": 0, "midback": 1, "lead": 0, "cross": 0},
       "InsuranceAsia", "en", ["reg"], ["health", "reg"],
       ["印尼", "健康险", "共付"], ["印尼", "健康險", "共付"],
       "news", "2026-08-26T06:45:00+08:00",
       "https://insuranceasia.com/insurance/news/indonesia-health-rules-impose-5-co-pay-claims"),

    mk("iaa-in-life-jul-20260826", 62, "verified", "media", "insuranceasia",
       "印度寿险7月新单保费4.7亿美元 前7月累计增17.45% [EN原文]",
       "印度壽險7月新單保費4.7億美元 前7月累計增17.45% [EN原文]",
       "印度寿险委员会临时数据：截至2026年7月新业务保费156亿美元按年增17.45%，保单件数741万件增4.34%；7月单月新单保费47亿美元，私营寿险公司前7月贡献62亿美元。",
       "印度壽險委員會臨時數據：截至2026年7月新業務保費156億美元按年增17.45%，保單件數741萬件增4.34%；7月單月新單保費47億美元，私營壽險公司前7月貢獻62億美元。",
       "印度寿险高增长印证亚洲保障缺口与保费迁移趋势，是港险机构区域配置与再保策略的重要背景数据。",
       "印度壽險高增長印證亞洲保障缺口與保費遷移趨勢，是港險機構區域配置與再保策略的重要背景數據。",
       {"front": {}, "midback": {"sc": "区域市场研究背景", "tc": "區域市場研究背景"},
        "lead": {}, "cross": {}},
       {"front": 0, "midback": 1, "lead": 0, "cross": 0},
       "InsuranceAsia", "en", ["market"], ["statistics", "market"],
       ["印度", "寿险", "新单保费"], ["印度", "壽險", "新單保費"],
       "stats", "2026-08-26T06:30:00+08:00",
       "https://insuranceasia.com/insurance/news/india-life-premiums-rise-1745-16b-in-july-2026"),

    mk("iaa-vn-acb-20260826", 62, "verified", "media", "insuranceasia",
       "越南亚洲商业银行获准设非寿险子公司 注册资本1910万美元 [EN原文]",
       "越南亞洲商業銀行獲准設非壽險子公司 註冊資本1910萬美元 [EN原文]",
       "越南财政部向亚洲商业银行(ACB)子公司ACB Insurance颁发成立与经营牌照，注册资本1910万美元，由ACB两家子公司出资，标志该行正式进入非寿险市场。",
       "越南財政部向亞洲商業銀行(ACB)子公司ACB Insurance頒發成立與經營牌照，註冊資本1910萬美元，由ACB兩家子公司出資，標誌該行正式進入非壽險市場。",
       "银行系险企扩张是东南亚分销格局的重要变量，反映银保渠道竞争加剧，对港险跨境渠道策略有参考意义。",
       "銀行系險企擴張是東南亞分銷格局的重要變量，反映銀保渠道競爭加劇，對港險跨境渠道策略有參考意義。",
       {"front": {}, "midback": {"sc": "渠道格局观察", "tc": "渠道格局觀察"},
        "lead": {}, "cross": {}},
       {"front": 0, "midback": 1, "lead": 0, "cross": 0},
       "InsuranceAsia", "en", ["market"], ["channel", "distribution"],
       ["越南", "银保", "非寿险"], ["越南", "銀保", "非壽險"],
       "news", "2026-08-26T05:45:00+08:00",
       "https://insuranceasia.com/insurance/news/vietnamese-bank-ventures-non-life-insurance"),

    mk("ibm-steadfast-profit-private-20260826", 66, "pending", "media", "insurancebusinessmag",
       "澳洲Steadfast盈利上升 KKR财团推进55亿美元私有化 [EN原文]",
       "澳洲Steadfast盈利上升 KKR財團推進55億美元私有化 [EN原文]",
       "Steadfast Group（旗下覆盖新加坡及亚太56家经纪公司）基础盈利升8.2%；KKR牵头、含Amwins与Dragoneer的财团正推进对集团的55亿美元收购并私有化。",
       "Steadfast Group（旗下覆蓋新加坡及亞太56家經紀公司）基礎盈利升8.2%；KKR牽頭、含Amwins與Dragoneer的財團正推進對集團的55億美元收購並私有化。",
       "亚太最大经纪集团之一易主，反映私募资本加码保险分销与整合趋势，影响经纪渠道生态与港险再保谈判格局。",
       "亞太最大經紀集團之一易主，反映私募資本加碼保險分銷與整合趨勢，影響經紀渠道生態與港險再保談判格局。",
       {"front": {}, "midback": {"sc": "经纪渠道格局变化关注", "tc": "經紀渠道格局變化關注"},
        "lead": {}, "cross": {}},
       {"front": 0, "midback": 1, "lead": 0, "cross": 0},
       "Insurance Business", "en", ["market"], ["distribution", "firm"],
       ["Steadfast", "并购", "经纪"], ["Steadfast", "併購", "經紀"],
       "news", "2026-08-26T09:10:00+08:00",
       "https://www.insurancebusinessmag.com/asia/news/breaking-news/steadfast-lifts-profit-as-us-consortium-moves-to-take-it-private-587463.aspx"),

    mk("ibm-sg-west-island-20260826", 64, "pending", "media", "insurancebusinessmag",
       "新加坡新西部人工岛将催生尚无先例的保险工具需求 [EN原文]",
       "新加坡新西部人工島將催生尚無先例的保險工具需求 [EN原文]",
       "新加坡规划中的新西部人工岛项目（大型填海与基建）将带来现有市场尚未覆盖的工程、财产与运营风险，保险工具与承保能力存在空白。",
       "新加坡規劃中的新西部人工島項目（大型填海與基建）將帶來現有市場尚未覆蓋的工程、財產與營運風險，保險工具與承保能力存在空白。",
       "大型填海基建催生的保险创新需求，对港险工程险、海上保险及巨灾承保的产品与能力建设有前瞻参考。",
       "大型填海基建催生的保險創新需求，對港險工程險、海上保險及巨災承保的產品與能力建設有前瞻參考。",
       {"front": {}, "midback": {"sc": "工程险创新方向参考", "tc": "工程險創新方向參考"},
        "lead": {}, "cross": {}},
       {"front": 0, "midback": 1, "lead": 0, "cross": 0},
       "Insurance Business", "en", ["market"], ["marine", "uw"],
       ["新加坡", "工程险", "基建"], ["新加坡", "工程險", "基建"],
       "news", "2026-08-26T02:16:00+08:00",
       "https://www.insurancebusinessmag.com/asia/news/construction/singapores-new-western-island-will-need-insurance-tools-that-do-not-yet-exist-587445.aspx"),

    mk("ibm-vn-credit-20260826", 62, "pending", "media", "insurancebusinessmag",
       "越南贸易繁荣但信用保险渗透不足 出口风险敞口扩大 [EN原文]",
       "越南貿易繁榮但信用保險滲透不足 出口風險敞口擴大 [EN原文]",
       "越南出口与贸易量快速增长，但信用保险市场发展滞后于贸易规模，出口企业应收账风险敞口扩大，信用保险渗透率与承保能力存在明显缺口。",
       "越南出口與貿易量快速增長，但信用保險市場發展滯後於貿易規模，出口企業應收賬風險敞口擴大，信用保險滲透率與承保能力存在明顯缺口。",
       "东南亚信用保险缺口是区域贸易增长伴生风险，对港险贸易信用险、出口信用险业务拓展有参考价值。",
       "東南亞信用保險缺口是區域貿易增長伴生風險，對港險貿易信用險、出口信用險業務拓展有參考價值。",
       {"front": {}, "midback": {"sc": "信用险市场机会评估", "tc": "信用險市場機會評估"},
        "lead": {}, "cross": {}},
       {"front": 0, "midback": 1, "lead": 0, "cross": 0},
       "Insurance Business", "en", ["market"], ["uw", "cross-border"],
       ["越南", "信用保险", "出口"], ["越南", "信用保險", "出口"],
       "news", "2026-08-26T02:09:00+08:00",
       "https://www.insurancebusinessmag.com/asia/news/breaking-news/vietnams-trade-boom-outpaces-its-credit-insurance-market-587443.aspx"),

    mk("interface-hsbc-hk-selfdeclaration-20260826", 70, "verified", "media", "interface",
       "汇丰香港要求内地投资客户限期提交自我声明 逾期或停用服务",
       "匯豐香港要求內地投資客戶限期提交自我聲明 逾期或停用服務",
       "汇丰香港近日向部分内地存量投资客户发通知，须于9月12日前经App提交《开立/维持账户之声明书》，确认投资资金来自内地以外合法来源，逾期或停用投资服务；汇丰称仅适用于投资服务客户，属遵循监管要求。",
       "匯豐香港近日向部分內地存量投資客戶發通知，須於9月12日前經App提交《開立/維持賬戶之聲明書》，確認投資資金來自內地以外合法來源，逾期或停用投資服務；匯豐稱僅適用於投資服務客戶，屬遵循監管要求。",
       "内地离岸资产监管从税务延伸至账户KYC环节，直接影响内地客户在港投保及投资账户运作，是港险跨境业务必须跟踪的信号。",
       "內地離岸資產監管從稅務延伸至賬戶KYC環節，直接影響內地客戶在港投保及投資賬戶運作，是港險跨境業務必須跟蹤的信號。",
       {"front": {"sc": "客户KYC与合规提醒", "tc": "客戶KYC與合規提醒"},
        "midback": {"sc": "跨境账户政策监控", "tc": "跨境賬戶政策監控"},
        "lead": {"sc": "高净值客户沟通预案", "tc": "高淨值客戶溝通預案"},
        "cross": {}},
       {"front": 1, "midback": 1, "lead": 1, "cross": 0},
       "界面新闻（经东方财富转载）", "zh", ["reg"], ["cross-border", "compliance"],
       ["汇丰", "KYC", "离岸资产", "内地客户"], ["匯豐", "KYC", "離岸資產", "內地客戶"],
       "news", "2026-08-26T13:23:00+08:00",
       "https://finance.eastmoney.com/a/202608263854423949.html"),

    mk("21jingji-shouhui-h1-20260826", 64, "verified", "media", "21jingji",
       "手回集团上市后首份中报：分红险首年保费增逾4倍 对冲佣金率压力",
       "手回集團上市後首份中報：分紅險首年保費增逾4倍 對沖佣金率壓力",
       "21世纪经济报道：手回集团（02621.HK）首份中期业绩，上半年营收6.27亿元增13.1%，经调整净利7331.7万元增11.5%；首年保费22.1亿元增41.6%，其中分红型产品首年保费12.3亿元增逾400%。行业上半年分红险原保费1.01万亿元增94.4%。",
       "21世紀經濟報道：手回集團（02621.HK）首份中期業績，上半年營收6.27億元增13.1%，經調整淨利7331.7萬元增11.5%；首年保費22.1億元增41.6%，其中分紅型產品首年保費12.3億元增逾400%。行業上半年分紅險原保費1.01萬億元增94.4%。",
       "分红险结构性爆发是内地人身险市场主线，直接影响赴港配置需求与港险分红产品竞争定位，亦是「报行合一」下渠道生态变化的观测样本。",
       "分紅險結構性爆發是內地人身險市場主線，直接影響赴港配置需求與港險分紅產品競爭定位，亦是「報行合一」下渠道生態變化的觀測樣本。",
       {"front": {"sc": "分红险趋势客户素材", "tc": "分紅險趨勢客戶素材"},
        "midback": {"sc": "渠道与产品趋势参考", "tc": "渠道與產品趨勢參考"},
        "lead": {}, "cross": {}},
       {"front": 1, "midback": 1, "lead": 0, "cross": 0},
       "21世纪经济报道（经东方财富转载）", "zh", ["market"], ["par", "distribution"],
       ["分红险", "手回集团", "报行合一", "中期业绩"], ["分紅險", "手回集團", "報行合一", "中期業績"],
       "news", "2026-08-26T13:34:00+08:00",
       "https://finance.eastmoney.com/a/202608263854433255.html"),
]

path = 'data/live-items.json'
with open(path) as f:
    d = json.load(f)

old_ids = {it['id'] for it in d['items']}
old_urls = {it.get('originalUrl') for it in d['items']}
for it in new_items:
    assert it['id'] not in old_ids, f"dupe id {it['id']}"
    assert it['originalUrl'] not in old_urls, f"dupe url {it['originalUrl']}"
    assert 50 <= len(it['summary']['sc']) <= 120, f"summary len {it['id']}: {len(it['summary']['sc'])}"

d['items'] = new_items + d['items']
d['meta']['itemCount'] = len(d['items'])
d['meta']['generatedAt'] = INGEST
d['meta']['windowNote'] = {
    "sc": f"本库{len(d['items'])}条。",
    "tc": f"本庫{len(d['items'])}條。"
}

with open(path, 'w') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('OK: items now', len(d['items']), '| added', len(new_items))
