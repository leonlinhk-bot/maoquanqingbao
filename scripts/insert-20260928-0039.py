#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-28 00:39 增量采集（补跑 9/27 18:08 + 21:08 时段）。

窗口：2026-09-27 01:10 → 2026-09-28 00:39
核验结果：IA（新闻稿最新 24/9、通函最新 31/8）、HKMA（最新 25/9）、HKFI（最新 16/9）、
AIA（24/9）、AXA（23/9）、Prudential/Sun Life/Manulife（无新增）、NFRA、InsuranceAsia
（最新周报 26/9）、InsuranceBusiness、Artemis（最新 25/9）、AIR（最新 25/9）——窗口内均无新增，
系港周六日休市所致。故仅入 2 条窗口内新增（InsuranceAsia News 9/27）+ 1 条漏采补录
（金融监管总局险资投资港股通ETF 监管口径函，9/20 起实施，此前各批次漏采）。
"""
import json, shutil, os

BASE = '/Users/leonliang/maoquanqingbao'
NOW = '2026-09-28T00:39:00+08:00'


def item(**kw):
    d = {
        'clusterCount': 1, 'score': 65, 'verifyStatus': 'pending',
        'sourceTier': 'media', 'sourceKey': '', 'contentKind': 'news',
        'actions': {'front': {}, 'midback': {}, 'lead': {}, 'cross': {}},
        'rolesImpact': {'front': 0, 'midback': 0, 'lead': 0, 'cross': 0},
        'boards': [], 'themes': [], 'tags': {'sc': [], 'tc': []},
        'contentRole': {'sc': '本站导读', 'tc': '本站導讀'},
        'featured': False, 'evergreen': False, 'ingestedAt': NOW,
    }
    d.update(kw)
    return d


T = lambda sc, tc=None: {'sc': sc, 'tc': tc or sc}

NEW = [
    item(id='nfra-funds-hk-connect-etf-20260924', score=86, verifyStatus='pending',
         sourceTier='official', sourceKey='nfra', contentKind='circular',
         publishedAt='2026-09-24T15:34:00+08:00',
         title=T('内地险资获准投资港股通ETF：监管口径函明确自9月20日起实施，参照港股通股票规定执行、不占用QDII额度',
                 '內地險資獲准投資港股通ETF：監管口徑函明確自9月20日起實施，參照港股通股票規定執行、不佔用QDII額度'),
         summary=T('财联社独家：多家险企近日收到《关于明确保险资金投资港股通ETF监管口径的函》，文件明确「按照监管规定可投资港股通股票的保险机构可以投资港股通ETF，参照保险资金投资港股通股票的相关监管规定执行」，该监管口径自2026年9月20日起实施。港股通ETF指纳入内地与香港股票市场交易互联互通机制、在香港联交所上市的ETF产品，无需占用QDII额度。政策脉络：金融监管总局8月18日表示支持内地保险机构经沪深港通投资香港ETF，当日行政长官、财政司司长、财库局、证监会与港交所先后表态支持；港交所数据今年1至7月南向／北向ETF日均成交约58亿／51亿元人民币，同比分别升61%／86%，香港ETF市场日均成交406亿元、同比升22%。',
                 '財聯社獨家：多家險企近日收到《關於明確保險資金投資港股通ETF監管口徑的函》，文件明確「按照監管規定可投資港股通股票的保險機構可以投資港股通ETF，參照保險資金投資港股通股票的相關監管規定執行」，該監管口徑自2026年9月20日起實施。港股通ETF指納入內地與香港股票市場交易互聯互通機制、在香港聯交所上市的ETF產品，無需佔用QDII額度。政策脈絡：金融監管總局8月18日表示支持內地保險機構經滬深港通投資香港ETF，當日行政長官、財政司司長、財庫局、證監會與港交所先後表態支持；港交所數據今年1至7月南向／北向ETF日均成交約58億／51億元人民幣，同比分別升61%／86%，香港ETF市場日均成交406億元、同比升22%。'),
         why=T('这是香港资金面的官方增量：内地保险资金属长钱，获准经沪深港通配置在港上市ETF，等于为香港ETF生态多开一条制度性南向通道，且不占用机构QDII额度。对前线与高客而言，可用于解释香港市场流动性、ETF与投资相连类产品环境的变化依据，也是「香港作资产管理枢纽」政策链条的最新一环。',
                 '這是香港資金面的官方增量：內地保險資金屬長錢，獲准經滬深港通配置在港上市ETF，等於為香港ETF生態多開一條制度性南向通道，且不佔用機構QDII額度。對前線與高客而言，可用於解釋香港市場流動性、ETF與投資相連類產品環境的變化依據，也是「香港作資產管理樞紐」政策鏈條的最新一環。'),
         actions={'front': {},
                  'midback': T('把「南向险资通道」纳入月度市场简报，标注9月20日实施日与不占QDII额度两点口径'),
                  'lead': T('对外沟通统一使用监管原口径表述（可投港股通股票的机构即可投港股通ETF、参照股票规定执行），避免夸大为「新增额度」'),
                  'cross': T('内地险资跨境配置需求上升，可作为香港ETF、投资相连与储蓄型产品资金面观察指标')},
         rolesImpact={'front': 1, 'midback': 2, 'lead': 3, 'cross': 2},
         source={'sc': '财联社（21世纪经济报道／新浪财经 2026-09-24 转载）；背景表态见香港特区政府与监管机构2026-08-18回应（星島頭條）',
                 'tc': '財聯社（21世紀經濟報道／新浪財經 2026-09-24 轉載）；背景表態見香港特區政府與監管機構2026-08-18回應（星島頭條）',
                 'lang': 'zh'},
         boards=['reg', 'market'], themes=['reg', 'market', 'capital', 'cross-border'],
         tags={'sc': ['金融监管总局', '港股通ETF', '险资', '沪深港通', '南向资金', 'QDII'],
               'tc': ['金融監管總局', '港股通ETF', '險資', '滬深港通', '南向資金', 'QDII']},
         originalUrl='https://finance.sina.com.cn/roll/2026-09-24/doc-inisxhpc5024660.shtml'),

    item(id='insuranceasianews-bangkok-flood-disaster-20260927', score=72, verifyStatus='pending',
         sourceTier='pro', sourceKey='insuranceasianews', contentKind='news',
         publishedAt='2026-09-27T10:09:00+08:00',
         title=T('曼谷宣布进入洪水灾区状态：48小时暴雨引发全市内涝，未来数日仍有降雨，湄南河流域水位受监测 [EN原文]',
                 '曼谷宣布進入洪水災區狀態：48小時暴雨引發全市內澇，未來數日仍有降雨，湄南河流域水位受監測 [EN原文]'),
         summary=T('InsuranceAsia News 9月27日报道，曼谷市长差察·西迪汶（Chadchart Sittipunt）在连续48小时暴雨引发泰国首都大范围内涝后宣布曼谷进入灾害状态，且未来数日仍有降雨预报。泰国政府已将洪水预警延长至9月27日，正密切监测湄南河（Chao Phraya）流域与湄南河大坝水位；当地媒体报道城区多处积水深及摩托车半个车身、部分高架桥下整段道路被淹，各区办事处已接获指示协助居民记录损失（保留灾前灾后照片）以便申请当局援助。',
                 'InsuranceAsia News 9月27日報道，曼谷市長差察·西迪汶（Chadchart Sittipunt）在連續48小時暴雨引發泰國首都大範圍內澇後宣布曼谷進入災害狀態，且未來數日仍有降雨預報。泰國政府已將洪水預警延長至9月27日，正密切監測湄南河（Chao Phraya）流域與湄南河大壩水位；當地媒體報道城區多處積水深及摩托車半個車身、部分高架橋下整段道路被淹，各區辦事處已接獲指示協助居民記錄損失（保留災前災後照片）以便申請當局援助。'),
         why=T('泰国是东南亚财险与再保的重要暴露区域，曼谷城区内涝若演变为工业园区与商业中断损失，将进入区域再保续保条件与巨灾债券风险利差的定价窗口；对以「风险管理枢纽」为定位的香港（专属自保、ILS）而言，亦是观察亚洲巨灾风险需求与灾难数据披露机制的时点。',
                 '泰國是東南亞財險與再保的重要暴露區域，曼谷城區內澇若演變為工業園區與商業中斷損失，將進入區域再保續保條件與巨災債券風險利差的定價窗口；對以「風險管理樞紐」為定位的香港（專屬自保、ILS）而言，亦是觀察亞洲巨災風險需求與災難數據披露機制的時點。'),
         actions={'front': {},
                  'midback': T('把曼谷内涝纳入区域巨灾跟踪清单，与8月千叶水灾、台风杜娟并列观察损失口径'),
                  'lead': T('对外引用时仅用「宣布灾区／预警延长至9月27日」等已披露事实，不预设损失金额'),
                  'cross': T('东南亚客户若在泰国持有资产或供应链暴露，可提示复核财产／营业中断险的洪水条款与免赔')},
         rolesImpact={'front': 1, 'midback': 3, 'lead': 2, 'cross': 2},
         source={'sc': 'InsuranceAsia News（2026-09-27，Aidan Gregory）；灾情事实另见央视网／联合早报 2026-09-26 报道',
                 'tc': 'InsuranceAsia News（2026-09-27，Aidan Gregory）；災情事實另見央視網／聯合早報 2026-09-26 報道',
                 'lang': 'en'},
         boards=['market'], themes=['catastrophe', 'reinsurance', 'market'],
         tags={'sc': ['泰国', '曼谷', '洪水', '巨灾风险', '再保险', '营业中断'],
               'tc': ['泰國', '曼谷', '洪水', '巨災風險', '再保險', '營業中斷']},
         originalUrl='https://insuranceasianews.com/bangkok-declares-flood-disaster-following-two-days-of-torrential-rains/'),

    item(id='insuranceasianews-frontier-global-underwriting-smart-20260927', score=68, verifyStatus='pending',
         sourceTier='pro', sourceKey='insuranceasianews', contentKind='news',
         publishedAt='2026-09-27T09:04:00+08:00',
         title=T('澳洲专业险MGA Frontier Global Underwriting 委任 Lindsay Smart 为高级网络与金融条线核保人（覆盖澳新）[EN原文]',
                 '澳洲專業險MGA Frontier Global Underwriting 委任 Lindsay Smart 為高級網絡與金融條線核保人（覆蓋澳紐）[EN原文]'),
         summary=T('InsuranceAsia News 9月27日报道，澳洲金融条线专业MGA「Frontier Global Underwriting」委任 Lindsay Smart 为高级网络（cyber）及金融条线核保人，负责澳洲与新西兰市场。该条消息属其 People（人事）栏目，同期该栏目还包括安达（Chubb）擢升 Lulu Tsai 为香港海运及专项业务主管、Scor 增聘澳洲建筑险核保人、新成立的 Miller Malaysia 委任条约再保副董事等，反映亚太专业险与金融条线在需求变化下持续补充承保人才。',
                 'InsuranceAsia News 9月27日報道，澳洲金融條線專業MGA「Frontier Global Underwriting」委任 Lindsay Smart 為高級網絡（cyber）及金融條線核保人，負責澳洲與紐西蘭市場。該條消息屬其 People（人事）欄目，同期該欄目還包括安達（Chubb）擢升 Lulu Tsai 為香港海運及專項業務主管、Scor 增聘澳洲建築險核保人、新成立的 Miller Malaysia 委任條約再保副董事等，反映亞太專業險與金融條線在需求變化下持續補充承保人才。'),
         why=T('网络与金融条线（D&O／专业责任／网络）是近年香港经纪与MGA渠道的增长条线，亚太承保人才流动可作为条线竞争格局与费率走向的前置信号；也便于对内说明专业险承保能力正在向区域MGA与专业平台集中。',
                 '網絡與金融條線（D&O／專業責任／網絡）是近年香港經紀與MGA渠道的增長條線，亞太承保人才流動可作為條線競爭格局與費率走向的前置信號；也便於對內說明專業險承保能力正在向區域MGA與專業平台集中。'),
         actions={'front': {},
                  'midback': T('纳入亚太人事动向月度归集，用于跟踪网络／金融条线承保能力布局'),
                  'lead': {},
                  'cross': T('专业险人才向区域MGA集中，可作为香港经纪渠道产品线与承保伙伴选择的前瞻参考')},
         rolesImpact={'front': 0, 'midback': 2, 'lead': 1, 'cross': 1},
         source={'sc': 'InsuranceAsia News · People（2026-09-27，Aidan Gregory）',
                 'tc': 'InsuranceAsia News · People（2026-09-27，Aidan Gregory）',
                 'lang': 'en'},
         boards=['insurer'], themes=['talent', 'cyber', 'uw'],
         tags={'sc': ['人事动向', '网络险', '金融条线', 'MGA', '澳洲', '专业险'],
               'tc': ['人事動向', '網絡險', '金融條線', 'MGA', '澳洲', '專業險']},
         originalUrl='https://insuranceasianews.com/frontier-global-underwriting-appoints-lindsay-smart-as-senior-financial-lines-underwriter/'),
]

path = os.path.join(BASE, 'data/live-items.json')
shutil.copy(path, os.path.join(BASE, 'data/live-items.json.bak-0928-0039'))
doc = json.load(open(path, encoding='utf-8'))
old_ids = {it['id'] for it in doc['items']}
old_urls = {it.get('originalUrl', '').split('?')[0].rstrip('/') for it in doc['items']}
added, skipped = [], []
for it in NEW:
    u = it['originalUrl'].split('?')[0].rstrip('/')
    if it['id'] in old_ids or u in old_urls:
        skipped.append(it['id'])
        continue
    added.append(it)
doc['items'] = added + doc['items']
n = len(doc['items'])
doc['meta']['itemCount'] = n
doc['meta']['generatedAt'] = NOW
doc['meta']['windowNote'] = {'sc': f'本库{n}条。', 'tc': f'本庫{n}條。'}
json.dump(doc, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'added={len(added)} skipped={len(skipped)} total={n}')
for a in added:
    print('  +', a['publishedAt'], a['sourceKey'], a['id'])
if skipped:
    print('SKIPPED DUPES:', skipped)
