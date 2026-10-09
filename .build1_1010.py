#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-10 补采插入：2026-10-09 全天 + 2026-10-10 凌晨新条目"""
import json, shutil, datetime

P = 'data/live-items.json'
ING = '2026-10-10T01:45:00+08:00'


def S(a, b=None):
    return {'sc': a, 'tc': b or a}


def item(**kw):
    it = {
        'clusterCount': 1,
        'score': kw['score'],
        'verifyStatus': kw.get('verify', 'pending'),
        'sourceTier': kw['tier'],
        'sourceKey': kw['key'],
        'contentKind': kw.get('kind', 'news'),
        'actions': {
            'front': S(kw['a_front']),
            'midback': S(kw['a_mid']),
            'lead': S(kw['a_lead']),
            'cross': S(kw['a_cross']),
        },
        'rolesImpact': kw['roles'],
        'boards': kw['boards'],
        'themes': kw['themes'],
        'tags': {'sc': kw['tags'], 'tc': kw['tags']},
        'contentRole': S('本站导读', '本站導讀'),
        'featured': False,
        'evergreen': False,
        'ingestedAt': ING,
        'id': kw['id'],
        'publishedAt': kw['pub'],
        'originalUrl': kw['url'],
        'title': S(kw['title']),
        'summary': S(kw['summary']),
        'why': S(kw['why']),
        'source': kw['source'],
    }
    return it


NEW = []

# ---------------------------------------------------------------- 1. govhk 皇岗
NEW.append(item(
    id='govhk-huanggang-port-motor-ec-cover-45-insurers-20261009',
    score=88, verify='verified', tier='official', key='govhk', kind='press',
    pub='2026-10-09T14:30:00+08:00',
    url='https://www.info.gov.hk/gia/general/202610/09/P2026100900296.htm',
    title='政府與45間保險公司簽署市場協議 強制汽車及僱員補償保險保障伸延至皇崗口岸港方口岸區（10月12日開通）',
    summary='政府新聞網10月9日14時30分發稿：為配合皇崗口岸10月12日正式開通，政府與45間保險公司簽訂市場協議，將現行強制性汽車保險（《汽車保險（第三者風險）條例》第272章第4條）及僱員補償保險（《僱員補償條例》第282章第40條）保單的地域保障範圍擴展至皇崗口岸港方口岸區，生效日期追溯至2026年7月31日（即《皇崗口岸港方口岸區條例》第659章生效當日），保單持有人毋須繳付額外保費。協議由財經事務及庫務局與業界簽訂，經保險業監管局及香港保險業聯會協調促成。財庫局發言人稱，保險保單屬私人合約，不會因條例生效而自動延伸至港方口岸區，故主動在口岸啟用前促成協議，先行消除公眾混淆、減低持份者行政負擔；安排與2007年深圳灣口岸港方口岸區啟用時做法相若。市場協議文本及已簽約保險公司名單已上載財庫局網站。',
    why='口岸開通前先行鎖定強制保險的保障邊界，是本週最貼近前線的跨境配套政策：既避免保單持有人誤以為「過關即無保障」，亦把行政與混淆成本前置處理，可直接作為跨境用車及北上派駐人員保障的說明素材。',
    a_front='客戶問及跨境／北上用車或派駐人員的強制保險時，可引用「保障已延伸至港方口岸區、毋須額外保費」，但不代客判斷個別保單條款或具體個案是否受保',
    a_mid='納入跨境保障清單；核對客戶所用保險公司是否在45間名單以內',
    a_lead='用於說明政府在口岸開通前主動理順強制保險安排的政策取態',
    a_cross='大灣區口岸陸續開通下的保障配套節奏（2007深圳灣 → 2026皇崗）',
    roles={'front': 3, 'midback': 2, 'lead': 3, 'cross': 3},
    boards=['reg', 'product'],
    themes=['motor-insurance', 'employees-compensation', 'cross-border', 'greater-bay-area'],
    tags=['皇崗口岸', '強制汽車保險', '僱員補償保險', '財經事務及庫務局', '保監局'],
    source={'sc': '政府新聞網（財經事務及庫務局發稿）2026-10-09', 'tc': '政府新聞網（財經事務及庫務局發稿）2026-10-09',
            'lang': 'zh', 'name': '香港特區政府新聞公報', 'date': '2026-10-09', 'note': None},
))

# ---------------------------------------------------------------- 2. FSTB 名单
NEW.append(item(
    id='fstb-huanggang-market-agreement-insurer-list-20261009',
    score=85, verify='verified', tier='official', key='fstb', kind='press',
    pub='2026-10-09',
    url='https://www.fstb.gov.hk/fsb/tc/business/other_matters/index.html',
    title='財庫局專頁上載皇崗口岸強制保險市場協議全文及已簽約保險公司名單',
    summary='財經事務及庫務局在「其他事項」專頁（fstb.gov.hk/fsb/tc/business/other_matters/）新增皇崗口岸強制性汽車及僱員補償保險保障範圍擴展的三份文件：市場協議全文（只提供英文版本）、已簽訂協議的保險公司名單，以及中文新聞公報。該頁最後修訂日期為2026年10月9日。保單持有人與業界可按名單核對自己所用保險公司是否已納入延伸安排，避免因口岸啟用而誤判保障範圍。',
    why='同一政策下的「可核查附件」：市場協議條文與45間保險公司白名單，是前線回覆客戶「我張車保／勞保過關有無效」時唯一可引用的官方依據。',
    a_front='遇到客戶查詢時，以財庫局名單核對保險公司，並提示以保單條款為最終依據',
    a_mid='下載名單存檔，供核保與客服流程對照',
    a_lead='政策落地的執行細節（誰已簽約、條文如何寫）',
    a_cross='跨境口岸政策的可核查披露慣例',
    roles={'front': 2, 'midback': 2, 'lead': 2, 'cross': 2},
    boards=['reg'],
    themes=['motor-insurance', 'employees-compensation', 'cross-border', 'disclosure'],
    tags=['財庫局', '皇崗口岸', '市場協議', '保險公司名單'],
    source={'sc': '財經事務及庫務局「其他事項」專頁 2026-10-09', 'tc': '財經事務及庫務局「其他事項」專頁 2026-10-09',
            'lang': 'zh', 'name': '財經事務及庫務局', 'date': '2026-10-09', 'note': None},
))

# ---------------------------------------------------------------- 3. HKMA 债券
NEW.append(item(
    id='hkma-gb-issuance-schedule-primary-dealers-20261009',
    score=85, verify='verified', tier='official', key='hkma', kind='press',
    pub='2026-10-09T16:30:00+08:00',
    url='https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/10/20261009-3/',
    title='金管局公布2026年10月至2027年3月機構政府債券暫定發行時間表 並委任第一市場交易商',
    summary='金管局10月9日以香港特區政府代表身分，公布基建債券計劃（IBP）及政府可持續債券計劃（GSBP）下，2026年10月至2027年3月六個月機構政府債券的暫定發行時間表。債券以港元及人民幣計價，透過競爭性投標發行；時間表載列各次發行的暫定年期、投標日期、發行規模、發行日期及發行方式，並同時公布第一市場交易商（primary dealers）的委任安排。詳情載於香港政府債券網站（hkgb.gov.hk）的資料備忘錄。 [EN原文]',
    why='政府債券的供給節奏直接影響港元與離岸人民幣資金池的深度，是保險公司、強積金及其他長線資金配置港元／人民幣固定收益產品時的重要背景指標。',
    a_front='僅作市場背景說明，不涉及任何投資建議',
    a_mid='納入港元／人民幣債券供給與流動性監察',
    a_lead='用於說明基建及可持續債券供給與長線資金配置環境',
    a_cross='離岸人民幣產品供給對香港財富與風險管理中心定位的支撐',
    roles={'front': 1, 'midback': 2, 'lead': 3, 'cross': 2},
    boards=['market'],
    themes=['government-bond', 'infrastructure-bond', 'sustainable-finance', 'hkd-rmb'],
    tags=['金管局', '政府債券', '基建債券計劃', '可持續債券', '第一市場交易商'],
    source={'sc': '金管局新聞稿 2026-10-09', 'tc': '金管局新聞稿 2026-10-09',
            'lang': 'en', 'name': '香港金融管理局', 'date': '2026-10-09', 'note': None},
))

# ---------------------------------------------------------------- 4. AIA 年金
NEW.append(item(
    id='aia-yuet-yuet-annuity-launch-20261009',
    score=78, verify='verified', tier='insurer', key='aia', kind='press',
    pub='2026-10-09',
    url='https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/2026/aia-press-release-20261009',
    title='友邦香港推出「優悅年金保險計劃」 首創「自主樂齡健康服務」結合終身保證入息',
    summary='友邦香港及澳門10月9日宣布推出終身分紅保險計劃「優悅年金保險計劃」，主打終身保證每月入息，另設潛在非保證每月入息及非保證終期紅利，客戶可選擇把每月入息保留在保單內累積。計劃亮點包括：市場首創「自主樂齡健康服務」，聚焦認知能力、視力及活動能力三大樂齡支柱，以醫療機構認可的樂齡科技作非入侵性評估，並可與配偶及父母共享服務，覆蓋香港及中國內地指定城市；「額外入息利益」於第五個保單周年日或之後確診亞爾茲默氏病、不可還原器質性腦退化疾病或柏金遜症，可額外獲相當於保證每月入息50%的入息，最多120個月；另設「入息調配選項」可將每月入息支付予指定收款人，以及「預支入息利益」在子女或孫子女結婚、獲大學取錄、孫子女出生、家居維修等合資格事件下預支最多24個月保證入息。',
    why='「年金＋健康服務」的捆綁是香港退休產品近年主流演化方向，直接回應退休儲備不足（研究指平均需延遲12.8年退休）與認知／視力／關節三大老齡關注，是前線講解長壽風險與「預防為本」概念的可引用案例。',
    a_front='只作產品導讀，須清楚區分保證與非保證部分，不作任何回報承諾或比較性宣稱',
    a_mid='納入年金與樂齡服務產品比較表',
    a_lead='用於說明保險公司由「事後理賠者」轉向「健康管理者」的策略演進',
    a_cross='香港與大灣區樂齡健康服務網絡的落地路徑',
    roles={'front': 2, 'midback': 2, 'lead': 2, 'cross': 2},
    boards=['product', 'insurer'],
    themes=['annuity', 'retirement', 'longevity', 'health-service'],
    tags=['友邦香港', '優悅年金保險計劃', '自主樂齡健康服務', '退休規劃', '認知障礙'],
    source={'sc': '友邦香港新聞稿 2026-10-09', 'tc': '友邦香港新聞稿 2026-10-09',
            'lang': 'zh', 'name': '友邦保險（香港及澳門）', 'date': '2026-10-09', 'note': None},
))

# ---------------------------------------------------------------- 5. IAN 皇岗（同题聚合）
NEW.append(item(
    id='ian-huanggang-port-motor-ec-market-agreement-20261009',
    score=70, verify='pending', tier='pro', key='insuranceasianews',
    pub='2026-10-09T18:08:00+08:00',
    url='https://insuranceasianews.com/insurers-to-extend-mandatory-motorm-employees-compensation-cover-to-huanggang-port-area-at-no-extra-cost/',
    title='InsuranceAsia News：港府與45間保險公司達成市場協議 皇崗口岸強制車險與僱員補償保障零額外保費延伸',
    summary='InsuranceAsia News 10月9日報道（國際版時間18:08）：香港政府與保險業就皇崗口岸達成市場協議，45間保險公司把現行強制性汽車保險及僱員補償（EC）保險保單的保障範圍，以不收取額外保費的方式延伸至皇崗口岸港方口岸區，趕及口岸下周一（10月12日）正式開通。報道把事件歸類為監管機構、行業協會、汽車及僱員補償業務線議題，並涉及保險業監管局。 [EN原文]，正文需訂閱，重點已與政府新聞公報（2026-10-09 14:30）核對。',
    why='國際行業媒體以香港監管動作為當日頭條，反映跨境口岸保險配套是區內關注點；英文表述可作為對外或跨境客戶說明的平行參考。',
    a_front='對外引用時以政府新聞公報為準，媒體版本作補充',
    a_mid='記錄國際媒體對香港監管動作的關注角度',
    a_lead='用於跨境客戶溝通的英文表述參考',
    a_cross='香港口岸保險安排在區域媒體的呈現方式',
    roles={'front': 1, 'midback': 1, 'lead': 2, 'cross': 2},
    boards=['reg', 'product'],
    themes=['motor-insurance', 'employees-compensation', 'cross-border', 'media-coverage'],
    tags=['皇崗口岸', 'InsuranceAsia News', '強制車險', '僱員補償'],
    source={'sc': 'InsuranceAsia News 2026-10-09 報道', 'tc': 'InsuranceAsia News 2026-10-09 報道',
            'lang': 'en', 'name': 'InsuranceAsia News', 'date': '2026-10-09', 'note': '付費牆'},
))

# ---------------------------------------------------------------- 6. IBM 跨境 ADAS
NEW.append(item(
    id='ibm-hk-crossborder-adas-pay-first-recover-later-20261009',
    score=72, verify='verified', tier='pro', key='insurancebusinessmag', kind='news',
    pub='2026-10-09T00:39:00+08:00',
    url='https://www.insurancebusinessmag.com/asia/news/auto-motor/hong-kong-insurers-must-pay-first-when-crossborder-drivers-use-unapproved-driverassist-systems-592867.aspx',
    title='Insurance Business：跨境司機使用未經批准駕駛輔助系統 香港保險公司仍須先賠付第三方再追償',
    summary='Insurance Business 10月8日（香港時間10月9日00:39）報道：根據《汽車保險（第三者風險）條例》（第272章），人身傷亡的第三者責任屬法定保障，即使啟用未經批准的駕駛輔助系統（ADAS）落入保單除外條款，政府回覆明確「保險公司仍須先向受影響第三者作出賠償，其後可向投保人追討相關金額」；第三者財物損失則按個別保單條款及事故情況處理，形成保險公司的追償風險。報道引述：2025年12月23日「港車北上」首日，有內地司機在港珠澳大橋口岸附近啟用未經批准的智能駕駛系統並雙手離開方向盤，運輸署發出警告信；截至2026年5月底約8,400宗市區進入申請獲批、約6,700宗完成行程，2026年7月起市區每日配額由100增至200輛，並擴展至大灣區九市、計劃2027年第一季覆蓋廣東21市。香港車險市場2023年承保逾95.2萬輛車、毛保費51.6億港元；2025年全港保險業毛保費8,270億港元、按年升29.7%，一般業務毛保費1,085億港元。 [EN原文]',
    why='把「先賠後追」的法定責任與新興 ADAS 除外條款的張力講清楚，是汽車保險前線最容易誤答的題目之一；同時串連港車北上規模擴張與自動駕駛試行，屬跨境車險風險的新增維度。',
    a_front='向客戶說明第三者人身傷亡責任屬法定保障、不受除外條款影響，但個人違規使用未經批准系統仍可能被追償及被罰',
    a_mid='納入車險索償與追償風險個案庫',
    a_lead='用於說明自動駕駛與傳統車險責任分配尚未完全接軌',
    a_cross='港車北上規模擴張下的跨境車險理賠實務',
    roles={'front': 3, 'midback': 2, 'lead': 2, 'cross': 3},
    boards=['reg', 'product', 'market'],
    themes=['motor-insurance', 'adas', 'cross-border', 'claims-recovery'],
    tags=['港車北上', 'ADAS', '第272章', '先賠後追', '運輸署'],
    source={'sc': 'Insurance Business Asia 2026-10-09 報道', 'tc': 'Insurance Business Asia 2026-10-09 報道',
            'lang': 'en', 'name': 'Insurance Business Asia', 'date': '2026-10-09', 'note': None},
))

# ---------------------------------------------------------------- 7. IBM 泰国灾害险
NEW.append(item(
    id='ibm-thailand-disaster-insurance-scheme-100000-baht-20261010',
    score=70, verify='verified', tier='pro', key='insurancebusinessmag', kind='news',
    pub='2026-10-10T00:06:00+08:00',
    url='https://www.insurancebusinessmag.com/asia/news/catastrophe/thailands-new-disaster-insurance-scheme-caps-household-payouts-at-100000-baht-593034.aspx',
    title='Insurance Business：泰國推災害保險計劃 每戶賠償上限10萬泰銖 風災地震定額5,000泰銖',
    summary='Insurance Business 報道（香港時間10月10日00:06）：泰國推出由政府支持的災害保險計劃，按經驗證的房屋結構損壞賠付，每戶每宗災害賠償上限10萬泰銖（約3,020美元），水浸賠償最高10,000泰銖、風暴或地震5,000泰銖，目標15天內發放到戶；可移動物品（冷氣、家具、電器）不在保障範圍。災害相關死亡另有200萬泰銖賠付。計劃由保險委員會（OIC）與泰國一般保險協會（TGIA）參與設計，私營保險公司承保政府資金以外部分。背景：泰國2025年南部水浸造成至少1,400億泰銖（約43億美元）經濟損失、影響約100萬戶；2026年已錄得承保水浸損失100億至11億泰銖（約2.97億至3.27億美元）；泰國非壽險滲透率2020年僅1.9%，不足全球平均4.1%的一半。 [EN原文]',
    why='以「政府兜底＋私營承保」處理保護缺口，是東南亞災害風險融資的第三條路徑（有別於主權參數式保險）；對香港市場觀察氣候風險如何轉化為可承保產品、以及家居財物除外項目的設計取捨有參考價值。',
    a_front='談及水浸／天災家居保障時，可引用「政府計劃只覆蓋結構損壞、不保傢俬電器」提醒客戶檢視自身保單缺口',
    a_mid='納入區域災害保險計劃比較',
    a_lead='用於說明保護缺口與政府介入模式差異',
    a_cross='亞洲市場氣候風險融資路徑對比（主權參數式 vs 家庭定額）',
    roles={'front': 2, 'midback': 2, 'lead': 2, 'cross': 2},
    boards=['product', 'reg'],
    themes=['disaster-insurance', 'protection-gap', 'climate-risk', 'thailand'],
    tags=['泰國', '災害保險', 'OIC', '保護缺口', '水浸'],
    source={'sc': 'Insurance Business Asia 2026-10-10 報道', 'tc': 'Insurance Business Asia 2026-10-10 報道',
            'lang': 'en', 'name': 'Insurance Business Asia', 'date': '2026-10-10', 'note': None},
))

# ---------------------------------------------------------------- 8. IBM 人事
NEW.append(item(
    id='ibm-insurance-moves-manulife-prudential-20261009',
    score=70, verify='verified', tier='pro', key='insurancebusinessmag', kind='news',
    pub='2026-10-09T22:13:00+08:00',
    url='https://www.insurancebusinessmag.com/asia/news/life-insurance/insurance-moves-manulife-prudential-593011.aspx',
    title='Insurance Business：宏利升任香港科技主管為亞洲資訊總監 保誠新加坡連環高層任命',
    summary='Insurance Business 10月9日報道：宏利（Manulife）擢升 Andy Bruce 為宏利亞洲首席資訊總監（CIO），2026年10月1日生效；Bruce 此前出任宏利香港及澳門 CIO，負責區內最大型科技交付組合之一。宏利亞洲總裁兼首席執行官 Steve Finch 表示，任命反映集團在區內強化數碼能力與負責任地規模化 AI 的取向。保誠（Prudential）同時公布新加坡及區域任命：Don Charnsupharindr 任保誠新加坡首席合作分銷官（10月1日生效，來自保誠泰國首席商務官）；Sandeep Nair 任保誠新加坡首席策略及轉型官（10月5日生效，擁有近20年壽險策略、轉型、分析、分銷及併購經驗）；Jason Chiong 出任保誠集團區域 CEO 幕僚長，此前為瀚亞投資（Eastspring）企業策略及併購總監。 [EN原文]',
    why='兩家在香港有重要業務的國際保險集團同日公布科技與分銷領導層調動，反映香港作為區域科技與分銷人才基地的角色，亦可作為同業人才流動與組織方向的觀察點。',
    a_front='不主動向客戶提及，僅作內部行業動態參考',
    a_mid='納入同業高層人事與組織變動記錄',
    a_lead='用於說明區域科技與分銷職能的集中化趨勢',
    a_cross='香港作為區域保險人才與科技樞紐的定位',
    roles={'front': 0, 'midback': 2, 'lead': 2, 'cross': 1},
    boards=['insurer'],
    themes=['people', 'leadership', 'technology', 'apac'],
    tags=['宏利', '保誠', '資訊總監', 'Andy Bruce', 'Steve Finch'],
    source={'sc': 'Insurance Business Asia 2026-10-09 報道', 'tc': 'Insurance Business Asia 2026-10-09 報道',
            'lang': 'en', 'name': 'Insurance Business Asia', 'date': '2026-10-09', 'note': None},
))

# ---------------------------------------------------------------- 9. IBM 新加坡 AI 管治
NEW.append(item(
    id='ibm-singapore-mas-ai-governance-guidelines-2027-20261009',
    score=70, verify='verified', tier='pro', key='insurancebusinessmag', kind='news',
    pub='2026-10-09T01:14:00+08:00',
    url='https://www.insurancebusinessmag.com/asia/news/technology/singapores-ai-governance-rules-what-brokers-and-insurers-must-know-before-2027-592870.aspx',
    title='Insurance Business：新加坡金管局AI管治指引2027年10月生效 中介須盤點AI用例並承擔第三方模型責任',
    summary='Insurance Business 10月9日報道：新加坡金融管理局（MAS）的AI管治指引將於2027年10月進入首個合規日期，適用於受MAS監管的中介機構，包括保險經紀。指引要求四項：一、由董事會及高層設定AI風險問責、職責與風險胃納；二、在AI全生命周期識別、評估及管理風險，包括維持AI用例清單、評估風險重大性並施加相稱控制（數據管治、測試、人手監督、網絡安全、監測與變更管理）；三、按風險比例實施（影響不重大者可用基本政策）；四、第三方AI（包括經紀行使用的券商平台、客戶關係系統、文件工具）責任不得轉移，須取得供應商充分保證、評估工具是否適合用途，風險超出胃納時須考慮限制、暫停或更換服務。MAS 另稱將於2027年就自主代理型AI（agentic AI）進一步諮詢業界。 [EN原文]',
    why='香港與新加坡同為區內保險中介樞紐，MAS 的AI管治要求是香港從業者理解「AI 工具責任誰屬」最具體的參照：工具是買回來的，責任仍在自己，這對正在導入AI工作流的團隊是直接的合規提醒。',
    a_front='使用任何AI工具處理客戶資料或文件時，須以人手覆核為前提，不可假設供應商已代為合規',
    a_mid='參照四項要求檢視內部AI用例清單與第三方工具保證文件',
    a_lead='用於說明監管機構對AI責任歸屬的一貫立場',
    a_cross='新加坡先行監管對香港同業AI治理預期的參考意義',
    roles={'front': 2, 'midback': 3, 'lead': 2, 'cross': 2},
    boards=['tech', 'reg'],
    themes=['ai-governance', 'third-party-risk', 'mas', 'brokers'],
    tags=['MAS', 'AI管治', '第三方風險', 'agentic AI', '保險經紀'],
    source={'sc': 'Insurance Business Asia 2026-10-09 報道', 'tc': 'Insurance Business Asia 2026-10-09 報道',
            'lang': 'en', 'name': 'Insurance Business Asia', 'date': '2026-10-09', 'note': None},
))

print('part1 items:', len(NEW))
json.dump(NEW, open('/tmp/_new_part1.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
