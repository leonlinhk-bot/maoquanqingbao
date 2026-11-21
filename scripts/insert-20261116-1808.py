#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""一次性插入 2026-11-16 18:08 采集的条目
窗口：2026-11-15 18:08 → 2026-11-16 18:08
"""
import json, os, sys

BASE = '/Users/leonliang/maoquanqingbao'
LIVE = os.path.join(BASE, 'data', 'live-items.json')
NOW = '2026-11-16T18:08:00+08:00'


def mk(**kw):
    return {
        'id': kw['id'],
        'clusterCount': 1,
        'score': kw['score'],
        'verifyStatus': kw.get('verifyStatus', 'pending'),
        'sourceTier': kw['sourceTier'],
        'sourceKey': kw['sourceKey'],
        'title': {'sc': kw['t_sc'], 'tc': kw['t_tc']},
        'summary': {'sc': kw['s_sc'], 'tc': kw['s_tc']},
        'why': {'sc': kw['w_sc'], 'tc': kw['w_tc']},
        'actions': {
            'front': {'sc': kw['a_front'][0], 'tc': kw['a_front'][1]} if kw.get('a_front') else {},
            'midback': {'sc': kw['a_mid'][0], 'tc': kw['a_mid'][1]} if kw.get('a_mid') else {},
            'lead': {'sc': kw['a_lead'][0], 'tc': kw['a_lead'][1]} if kw.get('a_lead') else {},
            'cross': {'sc': kw['a_cross'][0], 'tc': kw['a_cross'][1]} if kw.get('a_cross') else {},
        },
        'rolesImpact': {'front': kw['r'][0], 'midback': kw['r'][1], 'lead': kw['r'][2], 'cross': kw['r'][3]},
        'source': {'sc': kw['src'], 'lang': kw['lang']},
        'boards': kw['boards'],
        'themes': kw['themes'],
        'tags': {'sc': kw['tags_sc'], 'tc': kw['tags_tc']},
        'contentKind': kw['kind'],
        'publishedAt': kw['pub'],
        'originalUrl': kw['url'],
        'ingestedAt': NOW,
        'contentRole': {'sc': '本站导读', 'tc': '本站導讀'},
        'featured': False,
        'evergreen': False,
        'summaryShort': {'sc': kw['s_sc'][:80], 'tc': kw['s_tc'][:80]},
    }


ITEMS = []

# 1. 香港首家本地船东互保协会获保监局批准开业
ITEMS.append(mk(
    id='ian-hk-pi-club-authorised-20261116',
    score=72, sourceTier='pro', sourceKey='insuranceasianews', verifyStatus='verified',
    t_sc='香港首家本地船东互保协会获保监局发牌　HK P&I Club 可开展业务 [EN原文]',
    t_tc='香港首家本地船東互保協會獲保監局發牌　HK P&I Club 可開展業務 [EN原文]',
    s_sc='保监局已批准香港船东互保协会（HK P&I Club）开展业务，成为香港首家本地船东互保（P&I）协会。香港近年为 P&I 协会设立专门监管制度，在资本与监管要求上作相应安排。',
    s_tc='保監局已批准香港船東互保協會（HK P&I Club）開展業務，成為香港首家本地船東互保（P&I）協會。香港近年為 P&I 協會設立專門監管制度，在資本與監管要求上作相應安排。',
    w_sc='香港过去主要做海事保险的「承保地」而非「承保主体」——船东的保赔保障多经伦敦、北欧、新加坡安排。首家本地 P&I 协会落地，意味着香港开始把互保这一最专业的海事风险载体搬进来；对「国际风险管理中心」的叙事而言，这是少见的可验证实体，而不是又一纸政策。对前线的影响不在个人寿险，而在企业客户里的航运、物流与跨境贸易敞口。',
    w_tc='香港過去主要做海事保險的「承保地」而非「承保主體」——船東的保賠保障多經倫敦、北歐、新加坡安排。首家本地 P&I 協會落地，意味著香港開始把互保這一最專業的海事風險載體搬進來；對「國際風險管理中心」的敘事而言，這是少見的可驗證實體，而不是又一紙政策。對前線的影響不在個人壽險，而在企業客戶裡的航運、物流與跨境貿易敞口。',
    a_front=('企业客户若有船运、货运或跨境物流敞口，可问一句 P&I 与货运险是否同一张单覆盖', '企業客戶若有船運、貨運或跨境物流敞口，可問一句 P&I 與貨運險是否同一張單覆蓋'),
    a_mid=('新协会初期承保能力与再保安排要逐单确认，别默认等同国际保赔集团成员', '新協會初期承保能力與再保安排要逐單確認，別默認等同國際保賠集團成員'),
    a_lead=('「首家本地 P&I 协会」可作为对高客讲香港风险管理中心的实据', '「首家本地 P&I 協會」可作為對高客講香港風險管理中心的實據'),
    a_cross=('家办若持有航运／物流资产，这是重新审视风险池与承保地的时点', '家辦若持有航運／物流資產，這是重新審視風險池與承保地的時點'),
    r=(1, 3, 2, 2),
    src='InsuranceAsia News', lang='en',
    boards=['reg', 'market'],
    themes=['marine', 'pi-club', 'market-development'],
    tags_sc=['香港船东互保协会', 'P&I', '海事保险', '保监局发牌', '风险管理中心'],
    tags_tc=['香港船東互保協會', 'P&I', '海事保險', '保監局發牌', '風險管理中心'],
    kind='news', pub='2026-11-16T15:41:00+08:00',
    url='https://insuranceasianews.com/hong-kongs-first-local-pi-club-secures-regulatory-nod/',
))

# 2. 安达人寿委任陈鸿展为香港总裁
ITEMS.append(mk(
    id='chubb-life-hk-president-20261116',
    score=78, sourceTier='insurer', sourceKey='chubb', verifyStatus='verified',
    t_sc='安达人寿委任陈鸿展为香港总裁　明言拓展财富策划与高净值市场',
    t_tc='安達人壽委任陳鴻展為香港總裁　明言拓展財富策劃與高淨值市場',
    s_sc='安达人寿 11 月 16 日委任陈鸿展为香港总裁，即时生效但须待监管批准。他负责香港寿险业务管理与营运，向总裁 Bryce Johns 汇报；此前任宏利香港及澳门首席经销总监。',
    s_tc='安達人壽 11 月 16 日委任陳鴻展為香港總裁，即時生效但須待監管批准。他負責香港壽險業務管理與營運，向總裁 Bryce Johns 匯報；此前任宏利香港及澳門首席經銷總監。',
    w_sc='安达在公告里把战略讲得很直白：拓展财富策划，靠「安达财富平台＋百慕大产品系列」，即离岸高客架构。挖角对象是宏利的经销体系主管，说明香港高客竞争的焦点已从产品条款转到平台与经销能力；对同业而言，接下来要看的是它的银行与经纪转介政策会不会重排。',
    w_tc='安達在公告裡把戰略講得很直白：拓展財富策劃，靠「安達財富平台＋百慕大產品系列」，即離岸高客架構。挖角對象是宏利的經銷體系主管，說明香港高客競爭的焦點已從產品條款轉到平台與經銷能力；對同業而言，接下來要看的是它的銀行與經紀轉介政策會不會重排。',
    a_front=('与高客谈离岸架构时，安达财富平台＋百慕大产品线会成为同业对标项', '與高客談離岸架構時，安達財富平台＋百慕大產品線會成為同業對標項'),
    a_mid=('留意新总裁上任后的渠道政策与合作条件变化', '留意新總裁上任後的渠道政策與合作條件變化'),
    a_lead=('若团队与宏利、安达两边均有合作，须预判人员流动带来的对接人变更', '若團隊與宏利、安達兩邊均有合作，須預判人員流動帶來的對接人變更'),
    a_cross=('高客离岸架构的供应商名单可能重排，家办可提前建立新对接', '高客離岸架構的供應商名單可能重排，家辦可提前建立新對接'),
    r=(2, 2, 1, 3),
    src='安达人寿（美通社）', lang='zh',
    boards=['insurer', 'family'],
    themes=['people', 'hnw', 'distribution'],
    tags_sc=['安达人寿', '陈鸿展', '高净值', '财富策划', '人事变动'],
    tags_tc=['安達人壽', '陳鴻展', '高淨值', '財富策劃', '人事變動'],
    kind='press', pub='2026-11-16T09:52:00+08:00',
    url='https://www.prnewswire.com/apac/zh/news-releases/-302939841.html',
))

# 3. 周大福人寿新任 CEO
ITEMS.append(mk(
    id='ctf-life-ceo-charles-hung-20261116',
    score=76, sourceTier='insurer', sourceKey='ctflife', verifyStatus='verified',
    t_sc='周大福人寿委任 Charles Hung 为行政总裁　11 月 24 日生效',
    t_tc='周大福人壽委任 Charles Hung 為行政總裁　11 月 24 日生效',
    s_sc='周大福人寿委任 Charles Hung 为行政总裁，11 月 24 日生效，接替在位五年的 Man Kit Ip。他有逾 30 年保险、资产与财富管理经验，曾任 Blue Insurance 香港行政总裁。',
    s_tc='周大福人壽委任 Charles Hung 為行政總裁，11 月 24 日生效，接替在位五年的 Man Kit Ip。他有逾 30 年保險、資產與財富管理經驗，曾任 Blue Insurance 香港行政總裁。',
    w_sc='周大福人寿是周大福企业应占经营溢利的最大贡献者，换帅往往伴随渠道与产品结构重排。新 CEO 的组合是「数字保险公司＋私行／财富管理＋资本市场」，指向高客与数字化分销，而不是继续拼代理人规模——这对以代理人为主战场的团队是可预期的竞争变量。',
    w_tc='周大福人壽是周大福企業應佔經營溢利的最大貢獻者，換帥往往伴隨渠道與產品結構重排。新 CEO 的組合是「數字保險公司＋私行／財富管理＋資本市場」，指向高客與數字化分銷，而不是繼續拼代理人規模——這對以代理人為主戰場的團隊是可預期的競爭變量。',
    a_front=('若客户在周大福人寿有存量单，留意其服务与增值权益是否随新管理层调整', '若客戶在周大福人壽有存量單，留意其服務與增值權益是否隨新管理層調整'),
    a_mid=('新产品节奏与核保口径可能变化，跟单前先确认最新指引', '新產品節奏與核保口徑可能變化，跟單前先確認最新指引'),
    a_lead=('对手方换帅期是观察其招募与渠道政策的窗口', '對手方換帥期是觀察其招募與渠道政策的窗口'),
    a_cross=('高客方案若用周大福人寿产品做底层，宜同步复核服务对接人', '高客方案若用周大福人壽產品做底層，宜同步複核服務對接人'),
    r=(2, 2, 2, 1),
    src='Insurance Asia', lang='en',
    boards=['insurer'],
    themes=['people', 'strategy', 'hnw'],
    tags_sc=['周大福人寿', 'CTF Life', '行政总裁', '人事变动', '高客'],
    tags_tc=['周大福人壽', 'CTF Life', '行政總裁', '人事變動', '高客'],
    kind='news', pub='2026-11-16T05:15:00+08:00',
    url='https://insuranceasia.com/insurance/news/ctf-life-names-charles-hung-ceo',
))

# 4. AXA 24 款产品更名（11/16 生效）
ITEMS.append(mk(
    id='axa-hk-product-renaming-20261116',
    score=80, sourceTier='insurer', sourceKey='axa', verifyStatus='verified',
    t_sc='AXA 安盛 24 款产品 11 月 16 日起更名　储蓄与危疾名称统一加入「保险」',
    t_tc='AXA 安盛 24 款產品 11 月 16 日起更名　儲蓄與危疾名稱統一加入「保險」',
    s_sc='AXA 安盛按保监局与金管局命名要求，11 月 16 日起为 24 款产品更名，中英文名称加入「保险」及 Insurance，如「真智珍宝 III 储蓄计划」改为「储蓄保险」。条款与保费不变。',
    s_tc='AXA 安盛按保監局與金管局命名要求，11 月 16 日起為 24 款產品更名，中英文名稱加入「保險」及 Insurance，如「真智珍寶 III 儲蓄計劃」改為「儲蓄保險」。條款與保費不變。',
    w_sc='这是 2025 年 9 月保监局／金管局联合通函的落地期：友邦、保诚、中银人寿 8 月已先行，宏利 11 月跟上，安盛现在 24 款一次过。名称加「保险」看似文书，实际是把储蓄型产品的保险本质写进第一行；对前线最直接的影响是所有建议书、比较表与朋友圈素材都要换新名——用旧名，客户会以为是另一款产品。',
    w_tc='這是 2025 年 9 月保監局／金管局聯合通函的落地期：友邦、保誠、中銀人壽 8 月已先行，宏利 11 月跟上，安盛現在 24 款一次過。名稱加「保險」看似文書，實際是把儲蓄型產品的保險本質寫進第一行；對前線最直接的影響是所有建議書、比較表與朋友圈素材都要換新名——用舊名，客戶會以為是另一款產品。',
    a_front=('逐份核对手上建议书与比较表的产品名，尤其「储蓄计划→储蓄保险」', '逐份核對手頭建議書與比較表的產品名，尤其「儲蓄計劃→儲蓄保險」'),
    a_mid=('更名不改条款，但要向客户说明「同一张单、同一个保单号码」', '更名不改條款，但要向客戶說明「同一張單、同一個保單號碼」'),
    a_lead=('团队话术库与素材需统一更新，避免新旧名混用引起误解', '團隊話術庫與素材需統一更新，避免新舊名混用引起誤解'),
    a_cross=('家办年度检视旧名保单时，加一行新旧名称对照', '家辦年度檢視舊名保單時，加一行新舊名稱對照'),
    r=(3, 1, 2, 1),
    src='AXA 安盛', lang='zh',
    boards=['product', 'reg', 'insurer'],
    themes=['naming-rule', 'compliance', 'product'],
    tags_sc=['AXA 安盛', '产品更名', '保险产品命名', '储蓄保险', '危疾保险'],
    tags_tc=['AXA 安盛', '產品更名', '保險產品命名', '儲蓄保險', '危疾保險'],
    kind='press', pub='2026-11-16T00:00:00+08:00',
    url='https://axa.com.hk/zh/article/change-of-product-name',
))

# 5. 达信风险 港澳商业总监
ITEMS.append(mk(
    id='marsh-risk-rory-young-20261116',
    score=70, sourceTier='pro', sourceKey='insuranceasianews', verifyStatus='verified',
    t_sc='达信风险擢升 Rory Young 为香港、澳门商业总监　此前主管大型网络风险客户 [EN原文]',
    t_tc='達信風險擢升 Rory Young 為香港、澳門商業總監　此前主管大型網絡風險客戶 [EN原文]',
    s_sc='据 InsuranceAsia News，Marsh Risk 擢升 Rory Young 为香港及澳门商业总监。他自 2025 年 11 月起任高级副总裁兼大型网络风险客户主管。',
    s_tc='據 InsuranceAsia News，Marsh Risk 擢升 Rory Young 為香港及澳門商業總監。他自 2025 年 11 月起任高級副總裁兼大型網絡風險客戶主管。',
    w_sc='商业险与网络险是港资与外资企业客户这两年最愿意加保的两块，把网络险客户主管放到港澳商业总监的位置，等于承认经纪行的增长点已从传统财产险转到「网络＋责任」。本地经纪在企业客户续保时会发现，对方主动提的题是网络险保额、勒索软件与营业中断条款。',
    w_tc='商業險與網絡險是港資與外資企業客戶這兩年最願意加保的兩塊，把網絡險客戶主管放到港澳商業總監的位置，等於承認經紀行的增長點已從傳統財產險轉到「網絡＋責任」。本地經紀在企業客戶續保時會發現，對方主動提的題是網絡險保額、勒索軟件與營業中斷條款。',
    a_front=('企业客户续保时，主动问网络险保额与实际营业中断缺口', '企業客戶續保時，主動問網絡險保額與實際營業中斷缺口'),
    a_mid=('留意大经纪把网络险与责任险打包承保的市场做法', '留意大經紀把網絡險與責任險打包承保的市場做法'),
    a_lead=('若团队涉企业险，网络险是可加挂的专业化标签', '若團隊涉企業險，網絡險是可加掛的專業化標籤'),
    a_cross=('家办持股的运营公司，网络险是尽调清单里常被忽略的一项', '家辦持股的運營公司，網絡險是盡調清單裡常被忽略的一項'),
    r=(2, 2, 1, 2),
    src='InsuranceAsia News', lang='en',
    boards=['market'],
    themes=['people', 'commercial', 'cyber'],
    tags_sc=['达信', 'Marsh', '网络险', '商业险', '人事'],
    tags_tc=['達信', 'Marsh', '網絡險', '商業險', '人事'],
    kind='news', pub='2026-11-16T17:01:00+08:00',
    url='https://insuranceasianews.com/marsh-risk-promotes-rory-young-to-commercial-director-for-hong-kong-macau/',
))

# 6. 忠意 GC&C 香港财产险
ITEMS.append(mk(
    id='generali-gcc-eric-lim-20261116',
    score=70, sourceTier='pro', sourceKey='insuranceasianews', verifyStatus='verified',
    t_sc='忠意 GC&C 延揽 Eric Lim 主管香港财产险业务　此前在 AIG 逾三年 [EN原文]',
    t_tc='忠意 GC&C 延攬 Eric Lim 主管香港財產險業務　此前在 AIG 逾三年 [EN原文]',
    s_sc='忠意环球企业与商业险（GC&C）委任 Eric Lim 主管香港财产险业务。他此前在 AIG 任职逾三年，现转投忠意香港。',
    s_tc='忠意環球企業與商業險（GC&C）委任 Eric Lim 主管香港財產險業務。他此前在 AIG 任職逾三年，現轉投忠意香港。',
    w_sc='忠意近月在香港与亚洲持续加码：设劳合社辛迪加 2031、与世银集团签备忘、11 月起重整集团架构并指定亚洲区领军。挖 AIG 的财产险人，是把企业险承保能力本地化的一步；对客户而言，复杂财产与工程风险多了一个报价方。',
    w_tc='忠意近月在香港與亞洲持續加碼：設勞合社辛迪加 2031、與世銀集團簽備忘、11 月起重整集團架構並指定亞洲區領軍。挖 AIG 的財產險人，是把企業險承保能力本地化的一步；對客戶而言，複雜財產與工程風險多了一個報價方。',
    a_front=('有复杂财产或工程风险的客户，可把忠意列入比价名单', '有複雜財產或工程風險的客戶，可把忠意列入比價名單'),
    a_mid=('新承接人上任初期，承保口径与核保弹性需个案确认', '新承接人上任初期，承保口徑與核保彈性需個案確認'),
    a_lead=('企业险比价窗口期，宜同步整理客户的风险改善清单', '企業險比價窗口期，宜同步整理客戶的風險改善清單'),
    a_cross=('家族企业资产包的财产险安排，可借此重谈条件', '家族企業資產包的財產險安排，可借此重談條件'),
    r=(2, 2, 1, 1),
    src='InsuranceAsia News', lang='en',
    boards=['market', 'insurer'],
    themes=['people', 'property', 'commercial'],
    tags_sc=['忠意', 'Generali', '财产险', '企业险', '人事'],
    tags_tc=['忠意', 'Generali', '財產險', '企業險', '人事'],
    kind='news', pub='2026-11-16T12:52:00+08:00',
    url='https://insuranceasianews.com/generali-gcc-taps-eric-lim-for-hong-kong-property-role/',
))

# 7. Deutsche Rück 首笔巨灾债券
ITEMS.append(mk(
    id='artemis-pontgaia-re-deutscheruck-20261116',
    score=71, sourceTier='pro', sourceKey='artemis', verifyStatus='verified',
    t_sc='德国再保险 Deutsche Rück 首笔巨灾债券：1 亿欧元 Pontgaia Re　首年只保德国地震、次年可加洪水 [EN原文]',
    t_tc='德國再保險 Deutsche Rück 首筆巨災債券：1 億歐元 Pontgaia Re　首年只保德國地震、次年可加洪水 [EN原文]',
    s_sc='德国再保 Deutsche Rück 首次发行巨灾债券：1 亿欧元 Pontgaia Re，为其承保的德国公共保险机构业务提供回溯保障。首年只保德国地震，起赔 9,000 万欧元，年期至 2030 年。',
    s_tc='德國再保 Deutsche Rück 首次發行巨災債券：1 億歐元 Pontgaia Re，為其承保的德國公共保險機構業務提供回溯保障。首年只保德國地震，起賠 9,000 萬歐元，年期至 2030 年。',
    w_sc='2026 年首次发行主体数量将创纪录，说明资本市场上「把巨灾风险证券化」的门槛在下降。对香港的直接意义是 ILS 生态仍在起步（10 月才有首笔 sidecar），而欧洲中型再保都在自建 cat bond 通道——香港要抢这块，靠的是制度（PCC 结构、合格投资者定义）而不是利率。',
    w_tc='2026 年首次發行主體數量將創紀錄，說明資本市場上「把巨災風險證券化」的門檻在下降。對香港的直接意義是 ILS 生態仍在起步（10 月才有首筆 sidecar），而歐洲中型再保都在自建 cat bond 通道——香港要搶這塊，靠的是制度（PCC 結構、合格投資者定義）而不是利率。',
    a_front=('若客户问 ILS，可用「灾备资金来自资本市场」取代「再保公司扛」的旧说法', '若客戶問 ILS，可用「災備資金來自資本市場」取代「再保公司扛」的舊說法'),
    a_mid=('巨灾债券与参数型产品是两件事，别在客户面前混为一谈', '巨災債券與參數型產品是兩件事，別在客戶面前混為一談'),
    a_lead=('香港 ILS 生态仍小，短期不构成产品供给，但可作专业形象素材', '香港 ILS 生態仍小，短期不構成產品供給，但可作專業形象素材'),
    a_cross=('家办若看绝对收益，cat bond 属可纳入讨论的另类固收', '家辦若看絕對收益，cat bond 屬可納入討論的另類固收'),
    r=(0, 2, 1, 2),
    src='Artemis', lang='en',
    boards=['market', 'tech'],
    themes=['ils', 'cat-bond', 'reinsurance'],
    tags_sc=['巨灾债券', 'ILS', 'Deutsche Rück', 'Pontgaia Re', '德国地震'],
    tags_tc=['巨災債券', 'ILS', 'Deutsche Rück', 'Pontgaia Re', '德國地震'],
    kind='news', pub='2026-11-16T16:59:00+08:00',
    url='https://www.artemis.bm/news/deutsche-ruck-sponsoring-its-first-catastrophe-bond-e100m-pontgaia-re-dac/',
))

# 8. CEA Ursa Re 9 亿美元
ITEMS.append(mk(
    id='artemis-cea-ursa-re-2026-1-20261116',
    score=71, sourceTier='pro', sourceKey='artemis', verifyStatus='verified',
    t_sc='加州地震局 9 亿美元 Ursa Re 2026-1 定价完成　规模上调 50%、为其史上第二大巨灾债券 [EN原文]',
    t_tc='加州地震局 9 億美元 Ursa Re 2026-1 定價完成　規模上調 50%、為其史上第二大巨災債券 [EN原文]',
    s_sc='加州地震局完成 Ursa Re 2026-1 定价，规模由 6 亿美元上调至 9 亿美元，两档均以下限定价（D 档 3.5%、H 档 8%），为 CEA 史上第二大单笔巨灾债券。',
    s_tc='加州地震局完成 Ursa Re 2026-1 定價，規模由 6 億美元上調至 9 億美元，兩檔均以下限定價（D 檔 3.5%、H 檔 8%），為 CEA 史上第二大單筆巨災債券。',
    w_sc='同一笔交易三次下调定价仍然超额认购，说明巨灾债券市场当前资金充裕、投资者愿意往风险塔下层走（H 档预期损失 6.35%，为 CEA 史上最高）。对香港的含义是：本地要吸引这类发行，除了制度，还得有能承受中高预期损失档的机构投资者——这一层目前仍主要在新加坡与百慕大。',
    w_tc='同一筆交易三次下調定價仍然超額認購，說明巨災債券市場當前資金充裕、投資者願意往風險塔下層走（H 檔預期損失 6.35%，為 CEA 史上最高）。對香港的含義是：本地要吸引這類發行，除了制度，還得有能承受中高預期損失檔的機構投資者——這一層目前仍主要在新加坡與百慕大。',
    a_front=('客户若问「保险风险能不能不靠保险公司」，这是可讲的资本市场案例', '客戶若問「保險風險能不能不靠保險公司」，這是可講的資本市場案例'),
    a_mid=('巨灾债券条款复杂，不宜作为销售素材向零售客户推介', '巨災債券條款複雜，不宜作為銷售素材向零售客戶推介'),
    a_lead=('可作为「再保成本上涨的融资替代」知识点用于团队培训', '可作為「再保成本上漲的融資替代」知識點用於團隊培訓'),
    a_cross=('机构型家办若配置另类固收，cat bond 值得列入观察池', '機構型家辦若配置另類固收，cat bond 值得列入觀察池'),
    r=(0, 2, 1, 2),
    src='Artemis', lang='en',
    boards=['market'],
    themes=['ils', 'cat-bond', 'earthquake'],
    tags_sc=['巨灾债券', 'Ursa Re', '加州地震局', 'CEA', 'ILS'],
    tags_tc=['巨災債券', 'Ursa Re', '加州地震局', 'CEA', 'ILS'],
    kind='news', pub='2026-11-16T16:00:00+08:00',
    url='https://www.artemis.bm/news/california-earthquake-authority-secures-its-second-largest-cat-bond-900m-ursa-re-2026-1/',
))

# 9. 金管局与 Swift 拓展 Project Ensemble
ITEMS.append(mk(
    id='hkma-swift-ensemble-ledger-20261116',
    score=85, sourceTier='official', sourceKey='hkma', verifyStatus='verified',
    t_sc='金管局与 Swift 深化合作　研究以代币化存款打通跨境支付：Ensemble 结算层对接 Swift 账本',
    t_tc='金管局與 Swift 深化合作　研究以代幣化存款打通跨境支付：Ensemble 結算層對接 Swift 賬本',
    s_sc='金管局 11 月 16 日宣布加强与 Swift 合作，以 Project Ensemble 沙盒为基础，探索 Swift 账本与 Ensemble 结算层的互通，发展多币种代币化存款的跨境支付机制。中银香港、渣打香港与汇丰香港参与其中。金管局副总裁李达志称，EnsembleTX 已进入新阶段；Swift 商务总监 Thierry Chilosi 指 Swift 现连接 150 种货币的支付结算。',
    s_tc='金管局 11 月 16 日宣布加強與 Swift 合作，以 Project Ensemble 沙盒為基礎，探索 Swift 賬本與 Ensemble 結算層的互通，發展多幣種代幣化存款的跨境支付機制。中銀香港、渣打香港與匯豐香港參與其中。金管局副總裁李達志稱，EnsembleTX 已進入新階段；Swift 商務總監 Thierry Chilosi 指 Swift 現連接 150 種貨幣的支付結算。',
    w_sc='跨境支付一直是港险高客与跨国家办的摩擦点：缴费用电汇、理赔用支票、资金到位要几天。Ensemble 接 Swift 的意义是让「代币化存款」不只停留在本地结算，而是能对接全球银行网络。对保险业而言，这是未来保费收付与理赔跨境清分的底层轨道，短期不改变产品，但会改变资金效率的比较基准。',
    w_tc='跨境支付一直是港險高客與跨國家辦的摩擦點：繳費用電匯、理賠用支票、資金到位要幾天。Ensemble 接 Swift 的意義是讓「代幣化存款」不只停留在本地結算，而是能對接全球銀行網絡。對保險業而言，這是未來保費收付與理賠跨境清分的底層軌道，短期不改變產品，但會改變資金效率的比較基準。',
    a_front=('客户抱怨跨境缴费慢时，可说明基建正在升级，别承诺时间表', '客戶抱怨跨境繳費慢時，可說明基建正在升級，別承諾時間表'),
    a_mid=('留意参与银行（中银香港、渣打、汇丰）后续的跨境方案落地', '留意參與銀行（中銀香港、渣打、匯豐）後續的跨境方案落地'),
    a_lead=('跨境支付效率是高客服务体验的隐性指标，可纳入服务承诺讨论', '跨境支付效率是高客服務體驗的隱性指標，可納入服務承諾討論'),
    a_cross=('跨国家办资金调拨若走代币化存款，合规与税务口径要同步确认', '跨國家辦資金調撥若走代幣化存款，合規與稅務口徑要同步確認'),
    r=(2, 3, 2, 3),
    src='香港金管局', lang='zh',
    boards=['tech', 'market', 'reg'],
    themes=['tokenisation', 'cross-border-payment', 'infrastructure'],
    tags_sc=['金管局', 'Project Ensemble', 'Swift', '代币化存款', '跨境支付'],
    tags_tc=['金管局', 'Project Ensemble', 'Swift', '代幣化存款', '跨境支付'],
    kind='press', pub='2026-11-16T00:00:00+08:00',
    url='https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/11/20261116-4/',
))

# 10. AI 保险市场 2034 年 1544 亿美元
ITEMS.append(mk(
    id='insuranceasia-ai-insurance-market-2034-20261116',
    score=66, sourceTier='media', sourceKey='insuranceasia', verifyStatus='verified',
    t_sc='AI 保险市场 2034 年上看 1,544 亿美元　亚太年增 42.2% 最快、承保应用增速第一 [EN原文]',
    t_tc='AI 保險市場 2034 年上看 1,544 億美元　亞太年增 42.2% 最快、承保應用增速第一 [EN原文]',
    s_sc='Insurance Asia 引述 Fortune Business Insights：全球 AI 保险市场将从今年 135 亿美元增至 2034 年 1,544 亿美元，年复合增长 35.7%；亚太增速最快，年增 42.2%，2025 年区内规模 28 亿美元（中国 7.1 亿、印度 5.8 亿）。GlobalData 调查显示 2026 年 34.4% 受访者认为核保与风险画像最受益于 AI，但占比同比降 11.4 个百分点，产品开发升幅最大（+8.9 个百分点）。',
    s_tc='Insurance Asia 引述 Fortune Business Insights：全球 AI 保險市場將從今年 135 億美元增至 2034 年 1,544 億美元，年複合增長 35.7%；亞太增速最快，年增 42.2%，2025 年區內規模 28 億美元（中國 7.1 億、印度 5.8 億）。GlobalData 調查顯示 2026 年 34.4% 受訪者認為核保與風險畫像最受益於 AI，但佔比同比降 11.4 個百分點，產品開發升幅最大（+8.9 個百分點）。',
    w_sc='值得注意的不是总额，而是结构变化：核保作为 AI 首要应用的地位在下降，产品开发与客户服务在上升——意味着 AI 正从「核保工具」变成「产品与分销工具」。这对前线是双面的：一方面产品迭代会更快，另一方面客户会用 AI 做比较，靠信息差成交的空间更薄。',
    w_tc='值得注意的不是總額，而是結構變化：核保作為 AI 首要應用的地位在下降，產品開發與客戶服務在上升——意味著 AI 正從「核保工具」變成「產品與分銷工具」。這對前線是雙面的：一方面產品迭代會更快，另一方面客戶會用 AI 做比較，靠信息差成交的空間更薄。',
    a_front=('客户已经会用 AI 比产品，别在条款细节上取巧，讲清楚不保什么更重要', '客戶已經會用 AI 比產品，別在條款細節上取巧，講清楚不保什麼更重要'),
    a_mid=('产品迭代加快，跟单时务必用最新版建议书与条款', '產品迭代加快，跟單時務必用最新版建議書與條款'),
    a_lead=('团队培训重心可从「背产品」转向「解释取舍」', '團隊培訓重心可從「背產品」轉向「解釋取捨」'),
    a_cross=('高客对 AI 使用的合规与数据边界有疑问，可预备一页说明', '高客對 AI 使用的合規與數據邊界有疑問，可預備一頁說明'),
    r=(2, 2, 3, 1),
    src='Insurance Asia', lang='en',
    boards=['tech', 'market'],
    themes=['ai', 'insurtech', 'underwriting'],
    tags_sc=['AI 保险', '保险科技', '核保', '亚太市场', '产品开发'],
    tags_tc=['AI 保險', '保險科技', '核保', '亞太市場', '產品開發'],
    kind='news', pub='2026-11-16T11:58:00+08:00',
    url='https://insuranceasia.com/insurance/expert-opinion/can-ai-do-more-underwrite-insurance',
))


def main():
    d = json.load(open(LIVE, encoding='utf-8'))
    old = d['items']
    existing_ids = {i['id'] for i in old}
    existing_urls = {(i.get('originalUrl') or '').rstrip('/') for i in old}
    new = []
    for it in ITEMS:
        if it['id'] in existing_ids:
            print('SKIP dup id:', it['id']); continue
        if it['originalUrl'].rstrip('/') in existing_urls:
            print('SKIP dup url:', it['id']); continue
        new.append(it)
    d['items'] = new + old
    d.setdefault('meta', {})
    d['meta']['generatedAt'] = NOW
    d['meta']['itemCount'] = len(d['items'])
    d['meta']['windowNote'] = {'sc': f'本库{len(d["items"])}条。', 'tc': f'本庫{len(d["items"])}條。'}
    json.dump(d, open(LIVE, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'inserted {len(new)} items, total {len(d["items"])}')


if __name__ == '__main__':
    import shutil
    shutil.copy(LIVE, LIVE + '.bak-1116-1808')
    main()
