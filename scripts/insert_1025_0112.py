#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 2026-10-24 (Sat) + 10-23 late items into live-items.json."""
import json, io
from datetime import datetime

PATH = '/Users/leonliang/maoquanqingbao/data/live-items.json'
NOW = '2026-10-25T01:12:00+08:00'

def item(**kw):
    it = {
        'clusterCount': 1,
        'verifyStatus': kw.get('verifyStatus', 'verified'),
        'contentKind': kw.get('contentKind', 'news'),
        'ingestedAt': NOW,
    }
    it.update(kw)
    it.pop('verifyStatus', None) if False else None
    return it

def mk(id, publishedAt, url, sourceKey, sourceTier, score, boards, themes,
       t_sc, t_tc, s_sc, s_tc, w_sc, w_tc, tags_sc, tags_tc,
       act_sc, act_tc, roles, src_name, src_date, lang, kind='news',
       verify='verified'):
    return {
        'clusterCount': 1,
        'verifyStatus': verify,
        'contentKind': kind,
        'ingestedAt': NOW,
        'id': id,
        'publishedAt': publishedAt,
        'originalUrl': url,
        'sourceKey': sourceKey,
        'sourceTier': sourceTier,
        'score': score,
        'boards': boards,
        'themes': themes,
        'title': {'sc': t_sc, 'tc': t_tc},
        'summary': {'sc': s_sc, 'tc': s_tc},
        'why': {'sc': w_sc, 'tc': w_tc},
        'tags': {'sc': tags_sc, 'tc': tags_tc},
        'actions': {
            'front': {'sc': act_sc[0], 'tc': act_tc[0]},
            'midback': {'sc': act_sc[1], 'tc': act_tc[1]},
            'lead': {'sc': act_sc[2], 'tc': act_tc[2]},
            'cross': {'sc': act_sc[3], 'tc': act_tc[3]},
        },
        'rolesImpact': {'front': roles[0], 'midback': roles[1], 'lead': roles[2], 'cross': roles[3]},
        'source': {'sc': src_name, 'tc': src_name, 'name': sourceKey, 'date': src_date, 'lang': lang},
        'lang': lang,
        'summaryShort': {'sc': s_sc, 'tc': s_tc},
    }

NEW = []

# 1. SCMP — HSBC Abu Dhabi wealth centre
NEW.append(mk(
    'scmp-hsbc-abu-dhabi-wealth-centre-20261024', '2026-10-24T14:00:00+08:00',
    'https://www.scmp.com/business/article/3371958/hsbc-open-new-wealth-centre-abu-dhabi-despite-regional-conflict',
    'scmp', 'media', 66, ['market', 'family'], ['财富管理', '中东', '高净值'],
    '汇丰12月在阿布扎比开财富中心　称中东高客需求未受战事影响',
    '滙豐12月在阿布扎比開財富中心　稱中東高客需求未受戰事影響',
    '汇丰将于12月在阿布扎比开设财富管理中心，属其二十年来中东最大投资的一部分，去年已在迪拜设立首个区域财富枢纽。汇丰阿联酋行政总裁 Mohamed Al Marzooqi 表示，即使2月底美以对伊朗开战，今年上半年该行在阿联酋的高净值新客仍持续增长。汇丰调查指97%全球投资者认为阿联酋具基建投资吸引力。[EN原文]',
    '滙豐將於12月在阿布扎比開設財富管理中心，屬其二十年來中東最大投資的一部分，去年已在杜拜設立首個區域財富樞紐。滙豐阿聯酋行政總裁 Mohamed Al Marzooqi 表示，即使2月底美以對伊朗開戰，今年上半年該行在阿聯酋的高淨值新客仍持續增長。滙豐調查指97%全球投資者認為阿聯酋具基建投資吸引力。[EN原文]',
    '高客与家办的钱正在重排赛道：香港守跨境财富管理中心的位置，中东抢增量。对做高客的团队，这是解释「客户为何同时看香港与中东架构」的实证线索。',
    '高客與家辦的錢正在重排賽道：香港守跨境財富管理中心的位置，中東搶增量。對做高客的團隊，這是解釋「客戶為何同時看香港與中東架構」的實證線索。',
    ['财富管理', '中东', '高净值', '跨境架构'], ['財富管理', '中東', '高淨值', '跨境架構'],
    ['客户沟通：高客为何看中东', '产品研究：跨境财富架构对比', '团队简报：家办地理分散', '家办客户的区域配置'],
    ['客戶溝通：高客為何看中東', '產品研究：跨境財富架構對比', '團隊簡報：家辦地理分散', '家辦客戶的區域配置'],
    (1, 1, 2, 2), 'SCMP 2026-10-24', '2026-10-24', 'en'))

# 2. InsuranceAsia News — captive boom
NEW.append(mk(
    'ian-asia-captive-race-hk-pcc-20261024', '2026-10-24T08:00:00+08:00',
    'https://insuranceasianews.com/asian-regulators-race-to-unlock-the-captive-boom/',
    'insuranceasianews', 'pro', 78, ['reg', 'market'], ['专属自保', 'PCC', '区域竞争'],
    '亚洲自保争夺升温：日本入场　港星纳闽抢注册地',
    '亞洲自保爭奪升溫：日本入場　港星納閩搶註冊地',
    'InsuranceAsia News 分析指，日本拟建立本土再保型自保制度，目前最多162家日企在夏威夷、百慕达等地设自保公司。新加坡拟2028年推出专属自保与ILS用的PCC（受保护单元公司）框架；香港政府正研究修例引入PCC，保监局目标12至18个月内把自保公司数目翻倍。全球自保公司2025年增3.8%至6,549家（苏黎世）。[EN原文]',
    'InsuranceAsia News 分析指，日本擬建立本土再保型自保制度，目前最多162家日企在夏威夷、百慕達等地設自保公司。新加坡擬2028年推出專屬自保與ILS用的PCC（受保護單元公司）框架；香港政府正研究修例引入PCC，保監局目標12至18個月內把自保公司數目翻倍。全球自保公司2025年增3.8%至6,549家（蘇黎世）。[EN原文]',
    '自保与ILS是香港「国际风险管理中心」最实的抓手。对前线与企业客户，自保是把可预期的大额风险从保单里拿出来的工具；能把「自保＋PCC＋再保」讲清楚，就有资格谈中大型企业的风险融资。',
    '自保與ILS是香港「國際風險管理中心」最實的抓手。對前線與企業客戶，自保是把可預期的大額風險從保單裡拿出來的工具；能把「自保＋PCC＋再保」講清楚，就有資格談中大型企業的風險融資。',
    ['专属自保', 'PCC', '香港政策', '风险融资'], ['專屬自保', 'PCC', '香港政策', '風險融資'],
    ['客户沟通：企业自留风险的边界', '产品研究：PCC与自保资本效率', '团队简报：香港自保政策窗口', '家办客户的跨境风险架构'],
    ['客戶溝通：企業自留風險的邊界', '產品研究：PCC與自保資本效率', '團隊簡報：香港自保政策窗口', '家辦客戶的跨境風險架構'],
    (1, 2, 2, 2), 'InsuranceAsia News 2026-10-24', '2026-10-24', 'en'))

# 3. IBM — China foreign brokers roadmap
NEW.append(mk(
    'ibm-china-foreign-brokers-15fyp-20261024', '2026-10-24T01:14:00+08:00',
    'https://www.insurancebusinessmag.com/asia/news/breaking-news/foreign-brokers-gain-wider-access-in-chinas-us850bn-insurance-market-594812.aspx',
    'insurancebusinessmag', 'pro', 74, ['reg', 'market'], ['十五五', '外资准入', '再保分出'],
    '内地「十五五」保险路线图：外资准入与再保改革提速',
    '內地「十五五」保險路線圖：外資准入與再保改革提速',
    '中国保险行业协会在金融街论坛发布《十五五时期保险业高质量发展研究》，逾150位专家、30余家机构参与，主线是扩大外资参与与市场改革。2025年全国保费约6.12万亿元人民币（约8,500亿美元）；财产险分出保费2025年上半年首破1,000亿元。NFRA须在收到完整申请后6个月内决定牌照，外资持股上限2021年已取消，总资产50亿美元以上可申请全牌照。[EN原文]',
    '中國保險行業協會在金融街論壇發布《十五五時期保險業高質量發展研究》，逾150位專家、30餘家機構參與，主線是擴大外資參與與市場改革。2025年全國保費約6.12萬億元人民幣（約8,500億美元）；財產險分出保費2025年上半年首破1,000億元。NFRA須在收到完整申請後6個月內決定牌照，外資持股上限2021年已取消，總資產50億美元以上可申請全牌照。[EN原文]',
    '港资经纪与保司「北上」的节奏取决于内地准入。路线图把健康、养老、巨灾列为可加值领域，正好对上香港的产品与再保能力，可作为跨境团队讲「能力互补」的官方口径。',
    '港資經紀與保司「北上」的節奏取決於內地准入。路線圖把健康、養老、巨災列為可加值領域，正好對上香港的產品與再保能力，可作為跨境團隊講「能力互補」的官方口徑。',
    ['十五五', '外资准入', '再保分出', '跨境展业'], ['十五五', '外資准入', '再保分出', '跨境展業'],
    ['客户沟通：跨境保障的互补性', '产品研究：健康养老巨灾缺口', '团队简报：北上准入时间表', '家办客户的内地资产安排'],
    ['客戶溝通：跨境保障的互補性', '產品研究：健康養老巨災缺口', '團隊簡報：北上准入時間表', '家辦客戶的內地資產安排'],
    (1, 2, 2, 1), 'Insurance Business Asia 2026-10-24', '2026-10-24', 'en'))

# 4. HKEJ — MPF October loss
NEW.append(mk(
    'hkej-mpf-oct-loss-5217-20261024', '2026-10-24',
    'https://www.hkej.com/dailynews/headline/article/4546124/10%E6%9C%88MPF%E4%BA%BA%E5%9D%87%E6%9A%AB%E8%9D%955217%E5%85%83',
    'hkej', 'media', 62, ['market', 'product'], ['强积金', '投资回报', '退休'],
    '10月强积金人均暂蚀5,217元　中港股票料成全年最差类别',
    '10月強積金人均暫蝕5,217元　中港股票料成全年最差類別',
    '积金评级估计，10月强积金月度投资亏损1.54%，账面蚀约259亿港元，人均暂蚀5,217元；若最终成真，将是今年首次连续两个月下跌。年初至今回报降至4.57%，仍累赚约710亿元、人均约14,945元。该机构指中港股票料成2026年强积金表现最差的资产类别。',
    '積金評級估計，10月強積金月度投資虧損1.54%，賬面蝕約259億港元，人均暫蝕5,217元；若最終成真，將是今年首次連續兩個月下跌。年初至今回報降至4.57%，仍累賺約710億元、人均約14,945元。該機構指中港股票料成2026年強積金表現最差的資產類別。',
    '退休金账户的短期波动是前线最常被问到的题。这条可当「长期纪律 vs 短期账面」的沟通素材，也为12月21日强积金「全自由行」首阶段实施做铺垫。',
    '退休金賬戶的短期波動是前線最常被問到的題。這條可當「長期紀律 vs 短期賬面」的溝通素材，也為12月21日強積金「全自由行」首階段實施做鋪墊。',
    ['强积金', '投资回报', '退休规划'], ['強積金', '投資回報', '退休規劃'],
    ['客户沟通：短期账面与长期纪律', '产品研究：退休组合分散', '团队简报：全自由行前的沟通', '家办客户的退休金安排'],
    ['客戶溝通：短期賬面與長期紀律', '產品研究：退休組合分散', '團隊簡報：全自由行前的溝通', '家辦客戶的退休金安排'],
    (2, 1, 1, 1), '信报 2026-10-24', '2026-10-24', 'zh'))

# 5. IBM — big3 broker model
NEW.append(mk(
    'ibm-big3-broker-model-20261023', '2026-10-23T18:07:00+08:00',
    'https://www.insurancebusinessmag.com/asia/news/breaking-news/aon-marsh-wtw-are-they-really-brokerages-any-more-594741.aspx',
    'insurancebusinessmag', 'pro', 70, ['insurer', 'market'], ['经纪模式', '咨询业务', '收入结构'],
    '三大经纪还叫经纪吗？财报拆出「两家带咨询、一家带经纪」',
    '三大經紀還叫經紀嗎？財報拆出「兩家帶諮詢、一家帶經紀」',
    'Insurance Business 拆解三大经纪最新财报：2025年 Marsh 收入64%来自风险与保险服务、36%来自咨询；Aon 为风险资本66%、人力资本34%；WTW 则是健康财富与职业55%、风险与经纪45%，且前者贡献56%分部经营利润。结论是 Marsh 与 Aon 仍是「带咨询的经纪」，WTW 更像「带经纪的咨询」，Marsh 另有3.6亿美元规模的管理咨询业务。[EN原文]',
    'Insurance Business 拆解三大經紀最新財報：2025年 Marsh 收入64%來自風險與保險服務、36%來自諮詢；Aon 為風險資本66%、人力資本34%；WTW 則是健康財富與職業55%、風險與經紀45%，且前者貢獻56%分部經營利潤。結論是 Marsh 與 Aon 仍是「帶諮詢的經紀」，WTW 更像「帶經紀的諮詢」，Marsh 另有3.6億美元規模的管理諮詢業務。[EN原文]',
    '「经纪」的定义正在变宽，直接影响客户对服务费与佣金结构的理解；也是港资经纪对标国际同业的坐标——如果收入结构不同，服务边界该怎么讲清楚。',
    '「經紀」的定義正在變寬，直接影響客戶對服務費與佣金結構的理解；也是港資經紀對標國際同業的坐標——如果收入結構不同，服務邊界該怎麼講清楚。',
    ['经纪模式', '咨询业务', '佣金结构'], ['經紀模式', '諮詢業務', '佣金結構'],
    ['客户沟通：服务费与佣金怎么解释', '产品研究：经纪价值链位置', '团队简报：对标国际经纪', '家办客户的多方顾问协同'],
    ['客戶溝通：服務費與佣金怎麼解釋', '產品研究：經紀價值鏈位置', '團隊簡報：對標國際經紀', '家辦客戶的多方顧問協同'],
    (2, 2, 2, 1), 'Insurance Business Asia 2026-10-23', '2026-10-23', 'en'))

# 6. SCMP — HK life sales record + tax crackdown
NEW.append(mk(
    'scmp-hk-life-sales-record-tax-risk-20261023', '2026-10-23T16:16:00+08:00',
    'https://www.scmp.com/business/money/investment-products/article/3371909/hong-kong-life-insurance-sales-58-first-half-tax-crackdown-threatens-momentum',
    'scmp', 'media', 68, ['market', 'product'], ['新造保费', '内地客', '税务合规'],
    '南早：上半年新造寿险2,751.6亿创新高　惟内地税务收紧或碍动能',
    '南早：上半年新造壽險2,751.6億創新高　惟內地稅務收緊或礙動能',
    '南华早报引保监局数据：上半年新造寿险保费2,751.6亿港元，按年升58%，连续第四年上半年创纪录，去年同期为1,737亿。报道指北京自5月起收紧跨境投资，并对内地居民的离岸信托与境外投资收益严格执行20%个人所得税；有经纪认为部分内地客投保前会「多想一想」。[EN原文]',
    '南華早報引保監局數據：上半年新造壽險保費2,751.6億港元，按年升58%，連續第四年上半年創紀錄，去年同期為1,737億。報道指北京自5月起收緊跨境投資，並對內地居民的離岸信託與境外投資收益嚴格執行20%個人所得稅；有經紀認為部分內地客投保前會「多想一想」。[EN原文]',
    '需求端出现「纪录高位＋政策降温」的双重信号。前线谈内地客要能拆开讲：保障与医疗需求仍强，纯储蓄型跨境配置的税务成本正在被重新定价，沟通顺序应据此调整。',
    '需求端出現「紀錄高位＋政策降溫」的雙重信號。前線談內地客要能拆開講：保障與醫療需求仍強，純儲蓄型跨境配置的稅務成本正在被重新定價，溝通順序應據此調整。',
    ['新造保费', '内地客', '税务合规', '需求结构'], ['新造保費', '內地客', '稅務合規', '需求結構'],
    ['客户沟通：保障需求与税务成本分开谈', '产品研究：储蓄型与保障型配比', '团队简报：内地客动能变化', '家办客户的跨境税务披露'],
    ['客戶溝通：保障需求與稅務成本分開談', '產品研究：儲蓄型與保障型配比', '團隊簡報：內地客動能變化', '家辦客戶的跨境稅務披露'],
    (2, 1, 2, 2), 'SCMP 2026-10-23', '2026-10-23', 'en'))

# 7. IBM — Willis defence unit
NEW.append(mk(
    'ibm-willis-defence-security-unit-20261023', '2026-10-23T11:37:00+08:00',
    'https://www.insurancebusinessmag.com/asia/news/breaking-news/willis-launches-defence-unit-as-asian-spending-hits-record-rise-594694.aspx',
    'insurancebusinessmag', 'pro', 72, ['product', 'tech'], ['防务保险', '特种风险', '承保能力'],
    '威利斯设全球防务与安全专项　亚洲防务开支创2009年以来最快升幅',
    '威利斯設全球防務與安全專項　亞洲防務開支創2009年以來最快升幅',
    'WTW 旗下 Willis 成立全球防务与安全专项，整合风险转移、风险顾问与分析、网络、危机管理、理赔、风险工程、营运韧性等能力，覆盖140个国家，由 Jennifer Caldarella 领军。亚洲与大洋洲2025年防务开支升8.1%至6,810亿美元，为2009年以来最快；无人机、自主航运与AI技术令传统风险管理难以覆盖。[EN原文]',
    'WTW 旗下 Willis 成立全球防務與安全專項，整合風險轉移、風險顧問與分析、網絡、危機管理、理賠、風險工程、營運韌性等能力，覆蓋140個國家，由 Jennifer Caldarella 領軍。亞洲與大洋洲2025年防務開支升8.1%至6,810億美元，為2009年以來最快；無人機、自主航運與AI技術令傳統風險管理難以覆蓋。[EN原文]',
    '地缘风险正把「防务与安全」推成新的特种险需求池，而承保能力有限、条款复杂。做企业险、航运与科技出口客户的团队，可以据此提前建话题与再保渠道。',
    '地緣風險正把「防務與安全」推成新的特種險需求池，而承保能力有限、條款複雜。做企業險、航運與科技出口客戶的團隊，可以據此提前建話題與再保渠道。',
    ['防务保险', '特种风险', '地缘政治'], ['防務保險', '特種風險', '地緣政治'],
    ['客户沟通：地缘风险的可保边界', '产品研究：特种险条款与容量', '团队简报：防务供应链敞口', '家办客户的实业风险体检'],
    ['客戶溝通：地緣風險的可保邊界', '產品研究：特種險條款與容量', '團隊簡報：防務供應鏈敞口', '家辦客戶的實業風險體檢'],
    (1, 2, 2, 1), 'Insurance Business Asia 2026-10-23', '2026-10-23', 'en'))

data = json.load(open(PATH, encoding='utf-8'))
existing = {i['id'] for i in data['items']}
NEW = [n for n in NEW if n['id'] not in existing]
NEW.sort(key=lambda x: x['publishedAt'], reverse=True)
data['items'] = NEW + data['items']
n = len(data['items'])
data['meta']['generatedAt'] = NOW
data['meta']['itemCount'] = n
data['meta']['windowNote'] = {'sc': f'本库{n}条。', 'tc': f'本庫{n}條。'}
json.dump(data, open(PATH, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'inserted {len(NEW)}, total {n}')
for x in NEW:
    print(' ', x['publishedAt'], x['id'])
