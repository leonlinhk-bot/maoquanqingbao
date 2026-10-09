#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-10 补采插入 第二部分"""
import json

ING = '2026-10-10T01:45:00+08:00'


def S(a, b=None):
    return {'sc': a, 'tc': b or a}


def item(**kw):
    return {
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


IA = lambda d: {'sc': 'Insurance Asia 2026-10-09 報道', 'tc': 'Insurance Asia 2026-10-09 報道',
                'lang': 'en', 'name': 'Insurance Asia', 'date': d, 'note': None}
IAN = lambda d, n=None: {'sc': 'InsuranceAsia News 2026-10-09 報道', 'tc': 'InsuranceAsia News 2026-10-09 報道',
                         'lang': 'en', 'name': 'InsuranceAsia News', 'date': d, 'note': n}
ART = lambda d: {'sc': 'Artemis 2026-10-09 報道', 'tc': 'Artemis 2026-10-09 報道',
                 'lang': 'en', 'name': 'Artemis', 'date': d, 'note': None}
SC = lambda d, t: {'sc': '南華早報（SCMP）%s' % t, 'tc': '南華早報（SCMP）%s' % t,
                   'lang': 'en', 'name': 'South China Morning Post', 'date': d, 'note': None}

NEW = []

# ---- 10. 韩国寿险偿付能力
NEW.append(item(
    id='iaasia-south-korea-life-solvency-gaps-20261009',
    score=70, verify='verified', tier='pro', key='insuranceasia',
    pub='2026-10-09T06:30:00+08:00',
    url='https://insuranceasia.com/insurance/news/south-korea-life-insurers-face-widening-solvency-gaps',
    title='Insurance Asia：南韓壽險業K-ICS比率表面平穩 個別公司資本差距擴大至138%–396%',
    summary='Insurance Asia 10月9日報道，引述 CreditSights 數據：南韓壽險業2026年6月底資本水平按季大致平穩，但個別公司差異顯著。行業過渡後 K-ICS 比率跌0.7個百分點至206.8%，剔除緩解措施的基礎比率則升2.5個百分點至193.0%。各公司過渡後比率介乎 Hana Life 的138.3% 至 NongHyup Life 的396.4%；Hanwha Life 升至168.0%（按季升5.9個百分點，受惠利率、外匯及新合約服務邊際，管理層目標年底維持165%以上）；Kyobo Life 基礎比率跌5.0個百分點至155.4%（精算假設收緊及為收購 SBI Savings 配置資本）；NongHyup Life 升21.8個百分點，KB Life 跌28.8個百分點至223.4%；Fubon Hyundai Life 與 KDB Life 仍高度依賴臨時監管緩解。 [EN原文]',
    why='K-ICS 過渡期完結後的資本分化，是亞洲壽險監管與資產負債管理壓力的先行樣本；對香港市場理解「會計與精算標準收緊如何侵蝕資本」有對照價值。',
    a_front='不主動對客戶提及個別公司，僅作行業背景理解',
    a_mid='納入亞洲壽險資本充足度觀察名單',
    a_lead='用於說明利率與精算假設對壽險資本的雙向影響',
    a_cross='亞洲壽險監管標準演進的比較參考',
    roles={'front': 0, 'midback': 3, 'lead': 2, 'cross': 2},
    boards=['market'],
    themes=['solvency', 'k-ics', 'life-insurance', 'capital'],
    tags=['南韓', 'K-ICS', 'CreditSights', '壽險資本', '償付能力'],
    source=IA('2026-10-09'),
))

# ---- 11. AIA x Chi Longevity
NEW.append(item(
    id='iaasia-aia-chi-longevity-hk-longevity-centre-20261009',
    score=70, verify='verified', tier='pro', key='insuranceasia',
    pub='2026-10-09T06:15:00+08:00',
    url='https://insuranceasia.com/insurance/news/aia-and-chi-longevity-tackle-wealthy-clients-ageing-concerns',
    title='Insurance Asia：友邦伙新加坡Chi Longevity 年內在港設長壽中心服務高淨值客戶',
    summary='Insurance Asia 10月9日報道：友邦香港及澳門與新加坡健康長壽醫學機構 Chi Longevity 合作，為香港高淨值（HNW）客戶提供長壽及精準老年醫學服務，今年稍後將開設 AIA Alta 長壽中心，合資格客戶可使用由 Chi Longevity 開發的長壽科學方案。合作源於「友邦峻宇高淨值極臻長壽指數」發現認知與準備度落差：受訪者認知度74分、準備度僅54分。Chi Longevity 由 Andrea B. Maier 教授共同創辦，以實證為本的健康長壽與精準老年醫學，結合診斷與干預，協助客戶了解自身老化狀況、找出可干預項目並持續監測。 [EN原文]',
    why='高淨值客群的「長壽服務」由產品延伸至醫療與數據服務生態，反映香港高端市場競爭已從回報比較轉向健康與服務整合；同一議題已有友邦官方新聞稿，本條為行業媒體視角。',
    a_front='向高淨值客戶介紹時，強調服務屬健康管理支援、非醫療診斷或療效承諾',
    a_mid='納入高端客戶生態圈與增值服務競品記錄',
    a_lead='用於說明長壽經濟在保險業的落地形式',
    a_cross='香港與新加坡長壽醫療資源的跨境整合',
    roles={'front': 2, 'midback': 2, 'lead': 2, 'cross': 2},
    boards=['product', 'family', 'insurer'],
    themes=['hnw', 'longevity', 'health', 'ecosystem'],
    tags=['友邦峻宇', 'Chi Longevity', '高淨值', '長壽', '健康服務'],
    source=IA('2026-10-09'),
))

# ---- 12. 营业中断索赔
NEW.append(item(
    id='iaasia-allianz-business-interruption-claims-70pc-20261009',
    score=70, verify='verified', tier='pro', key='insuranceasia',
    pub='2026-10-09T06:00:00+08:00',
    url='https://insuranceasia.com/insurance/news/business-interruption-claims-outstrip-property-losses-70',
    title='Insurance Asia／安聯商業：營業中斷平均索賠金額比財產損毀高約70%',
    summary='Insurance Asia 10月9日報道安聯商業（Allianz Commercial）最新報告：分析2021年1月1日至2025年12月31日共7,888宗索賠，營業中斷平均索賠額超過98.6萬美元，較平均財產損毀索賠（近55.98萬美元／50萬歐元）高約70%；索賠頻率大致穩定，但平均賠付在期末兩年每年增長逾30%。樣本總損失約78.2億美元，火災及爆炸為最貴觸發因素，佔全部索賠金額逾40%（33億美元），十宗最大人為營業中斷損失中有九宗由火災造成，涵蓋英國、美國、德國、新加坡及香港等主要市場。非自然災害事件佔索賠宗數74%、金額66%；自然災害佔宗數26%、金額34%，復原期延長拉長索賠時間（颶風 Helene 相關個案兩年後仍未關閉，主因復原期長而非條款爭議）。報告點出通脹導致不足額投保、供應鏈集中與數碼依賴上升等新增風險。 [EN原文]',
    why='明確資料支持「營業中斷比財產損毀更貴」這一常被低估的商業保險事實，並直接點名香港市場；對企業客戶講解足額投保與供應鏈風險時極具說服力。',
    a_front='向企業客戶講解商業保險時，可引用「營業中斷平均賠付高於財產損毀約七成」說明保額與保障範圍需同步檢視',
    a_mid='納入商業風險與理賠趨勢資料庫',
    a_lead='用於說明企業風險由有形損毀轉向營運中斷',
    a_cross='跨市場（含香港）火災為主的營業中斷損失結構',
    roles={'front': 3, 'midback': 2, 'lead': 2, 'cross': 1},
    boards=['product', 'market'],
    themes=['business-interruption', 'commercial-insurance', 'claims', 'underinsurance'],
    tags=['安聯商業', '營業中斷', '火災', '不足額投保', '供應鏈'],
    source=IA('2026-10-09'),
))

# ---- 13. Generali + UNDP 印度 MSME
NEW.append(item(
    id='iaasia-generali-undp-india-msme-insurance-challenge-20261009',
    score=66, verify='verified', tier='pro', key='insuranceasia',
    pub='2026-10-09T05:45:00+08:00',
    url='https://insuranceasia.com/insurance/news/generali-and-undp-target-indias-msme-insurance-gap',
    title='Insurance Asia：Generali與聯合國開發計劃署辦印度微中小企保險創新挑戰',
    summary='Insurance Asia 10月9日報道：聯合國開發計劃署（UNDP）與 Generali Central 推出「保險創新挑戰」，尋找並規模化可提升印度微、小及中型企業（MSME）韌性的保險方案。印度有逾7,300萬家 MSME，貢獻約30% GDP及44%出口、僱用60%勞動力（SIDBI 2025年數據），但面對氣候衝擊、供應鏈中斷、工傷及負責人／員工健康事件等風險時保障有限，主因認知低、成本觀感及產品不貼合需要。挑戰聚焦健康事件、營業中斷及資產損失，開放予在印度註冊的保險公司、保險科技、技術服務商、社會企業及分銷公司；優先考慮以科技改善可得性與可負擔性、結合保險與金融服務、開發新分銷渠道或提升理財素養的方案。最多三個優勝方案各獲最高4萬美元資助，2026年11月20日截止申請，2027年2月公布結果。 [EN原文]',
    why='新興市場以開放式創新處理中小企保障缺口的模式，與香港／大灣區中小企保險的推廣痛點（認知、成本、產品貼合度）高度相似，可作方法論參考。',
    a_front='與中小企客戶討論保障缺口時的類比素材',
    a_mid='納入普惠保險與分銷創新案例',
    a_lead='用於說明保險業與公共機構協作處理結構性缺口',
    a_cross='亞洲新興市場與香港中小企保障議題的對照',
    roles={'front': 1, 'midback': 2, 'lead': 2, 'cross': 1},
    boards=['market', 'product'],
    themes=['msme', 'protection-gap', 'insurtech', 'distribution'],
    tags=['Generali', 'UNDP', '印度', 'MSME', '普惠保險'],
    source=IA('2026-10-09'),
))

# ---- 14. Singlife NHG
NEW.append(item(
    id='iaasia-singlife-nhg-health-digestive-care-20261009',
    score=66, verify='verified', tier='pro', key='insuranceasia',
    pub='2026-10-09T05:30:00+08:00',
    url='https://insuranceasia.com/insurance/news/singlife-nhg-health-target-high-volume-digestive-claims',
    title='Insurance Asia：Singlife夥NHG Health 整合新加坡三間公立醫院消化道專科網絡',
    summary='Insurance Asia 10月9日報道：新加坡 Singlife 與 NHG Health 合作，加入其「Singlife Care Collab」醫療服務樞紐，提升客戶專科服務可及性並探索以療效、康復與成本效益為核心的醫療模式。合作首階段聚焦消化道健康，Singlife Integrated Shield 客戶可使用 Khoo Teck Puat、Tan Tock Seng 及 Woodlands 醫院（包括新開設的消化道健康中心）的腸胃及結直腸外科服務，涵蓋預防、篩查、診斷、治療、康復及覆診。消化道內窺鏡檢查約佔 Singlife Shield 索賠宗數兩成；結直腸癌為新加坡男女第二常見癌症（2019至2023年近1.3萬宗新症）。雙方亦會探索以價值為本的模式，包括參考 ERAS（加速康復外科）經驗，以及為全膝置換等指定手術研究打包及定額收費。 [EN原文]',
    why='醫療保險競爭前線已轉向「服務網絡＋成本控制」：以高頻索賠項目切入、配合定額收費與加速康復路徑，是香港自願醫保及高端醫保可對照的產品思路。',
    a_front='客戶比較醫保時，可說明「網絡與服務整合」如何影響實際體驗與索賠效率',
    a_mid='納入醫保服務網絡與成本控制做法比較',
    a_lead='用於說明保險公司與公立醫療體系協作的路徑',
    a_cross='新加坡與香港醫療保險公私協作模式對比',
    roles={'front': 1, 'midback': 2, 'lead': 2, 'cross': 2},
    boards=['product', 'market'],
    themes=['health-insurance', 'provider-network', 'claims', 'value-based-care'],
    tags=['Singlife', 'NHG Health', '消化道', '定額收費', '醫保'],
    source=IA('2026-10-09'),
))

# ---- 15. CTF Life + HKMCA
NEW.append(item(
    id='iaasia-ctf-life-hkmca-retirement-collaboration-20261009',
    score=70, verify='verified', tier='pro', key='insuranceasia',
    pub='2026-10-09T05:15:00+08:00',
    url='https://insuranceasia.com/insurance/news/ctf-life-hkmca-team-tackle-retirement-risks',
    title='Insurance Asia：周大福人壽夥香港年金公司 合推退休規劃與公眾教育',
    summary='Insurance Asia 10月9日報道：周大福人壽（CTF Life）與香港年金有限公司（HKMCA，香港按揭證券公司旗下）合作，結合退休規劃與人壽保險專業，拓寬客戶退休規劃選擇，並合作舉辦專題講座、客戶活動及理財教育項目，提升公眾對長壽風險、退休入息規劃及資產配置的認知。報道指政府在《2026年施政報告》披露，65歲及以上人口預計2046年達274萬、佔全港人口超過三分之一。周大福人壽行政總裁葉文傑表示，合作為合資格客戶提供多一個了解「香港年金計劃」的途徑；HKMCA 行政總裁 Daniel Leong 稱期望與業界一同提升公眾對及早規劃退休的意識。 [EN原文]',
    why='保險公司與公共年金機構的合作，是香港退休入息市場的結構性變化：把公共年金納入私營渠道的客戶教育體系，前線在講解退休入息組合時可直接引用。',
    a_front='向客戶介紹退休入息方案時，可說明公共年金與私營年金的互補角色，但不可宣稱任何收益保證',
    a_mid='納入退休入息產品與合作渠道清單',
    a_lead='用於說明人口老化壓力下的市場協作',
    a_cross='公共年金與私營退休產品的銜接路徑',
    roles={'front': 2, 'midback': 2, 'lead': 2, 'cross': 1},
    boards=['product', 'insurer', 'market'],
    themes=['retirement', 'annuity', 'longevity', 'public-private'],
    tags=['周大福人壽', '香港年金有限公司', '退休規劃', '長壽風險', '施政報告'],
    source=IA('2026-10-09'),
))

# ---- 16. 印度 vs 中国
NEW.append(item(
    id='iaasia-india-china-premium-growth-swiss-re-20261009',
    score=70, verify='verified', tier='pro', key='insuranceasia',
    pub='2026-10-09T05:00:00+08:00',
    url='https://insuranceasia.com/insurance/exclusive/market-face-off-which-market-offers-bigger-long-term-insurance-prize',
    title='Insurance Asia專訪：印度保費增速將超中國 但中國市場規模仍為六倍',
    summary='Insurance Asia 10月9日刊出專訪：瑞士再保險研究院亞太區首席經濟學家 John Zhu 指出，2025年中國總保費約8,510億美元、為全球第二大市場，印度約1,510億美元居第十，中國市場規模約為印度六倍。瑞士再保險（1月報告）預測2026至2030年印度保費扣除通脹後年均增長6.9%，中國3.9%，印度為期間增速最快的主要保險市場。Zhu 提醒增速不能可靠推斷印度何時追上中國，因匯率、通脹、產品結構與監管各異；差異對保險公司決定投資、擴張分銷與開發產品具意義——印度機會在於把更多人納入保險市場，中國則已有更高保險使用率與更大保費池。GlobalData 分析師 Manogna Vangari 預期單計壽險的差距仍將相當顯著。 [EN原文]',
    why='為中國與印度兩個亞洲核心市場提供可引用的量化對照，有助於課程與客戶溝通中避免「增速高即市場大」的直覺誤判。',
    a_front='不直接對客引用，作行業格局背景',
    a_mid='納入亞洲市場規模與增長基準數據',
    a_lead='用於說明區域市場機會的兩種不同邏輯',
    a_cross='內地與亞洲新興市場對香港保險樞紐的間接影響',
    roles={'front': 0, 'midback': 2, 'lead': 3, 'cross': 2},
    boards=['market'],
    themes=['market-size', 'growth', 'india', 'china'],
    tags=['瑞士再保險', '印度', '中國', '保費增長', 'John Zhu'],
    source=IA('2026-10-09'),
))

# ---- 17. IAN 黑天鹅
NEW.append(item(
    id='ian-ferma-black-swans-risk-managers-insurers-20261009',
    score=68, verify='pending', tier='pro', key='insuranceasianews',
    pub='2026-10-09T15:30:00+08:00',
    url='https://insuranceasianews.com/insurers-urged-to-step-up-as-risk-managers-confront-flock-of-black-swans/',
    title='InsuranceAsia News：Ferma論壇風險經理批保險業追不上「黑天鵝群」 促產品與回應提速',
    summary='InsuranceAsia News 10月9日報道：在本週於鹿特丹舉行的 Ferma Forum（歐洲風險管理協會聯盟年會）上，環球風險經理對保險業提出批評，指傳統年度保單與緩慢的市場回應，已追不上日益增加且互相關聯的風險（報道配圖指向自然災害、航運與工廠風險，文章標籤涵蓋網絡風險）。多家企業要求保險夥伴提供超出目前水平的支援。 [EN原文]，正文需訂閱，此條僅按標題、導語及分類標籤整理，待補充原文後覆核。',
    why='風險經理社群的集體不滿是產品創新壓力的先行信號：當企業風險由「單一事件」轉為「相互關聯的黑天鵝群」，年度保單與單一險種框架的局限性就成為前線與核保都要面對的議題。',
    a_front='向企業客戶講解風險時，可引導由單一險種轉向整體風險檢視',
    a_mid='標記為產品創新與市場回應速度的觀察項',
    a_lead='用於說明企業風險管理需求與保險供給的落差',
    a_cross='歐洲風險經理訴求對亞洲市場產品設計的參照',
    roles={'front': 1, 'midback': 2, 'lead': 2, 'cross': 1},
    boards=['market', 'product'],
    themes=['risk-management', 'cedents', 'product-innovation', 'cyber'],
    tags=['Ferma', '風險經理', '黑天鵝', '年度保單', '產品創新'],
    source=IAN('2026-10-09', '付費牆'),
))

# ---- 18. TT Club / UK P&I 合并
NEW.append(item(
    id='ian-tt-club-uk-pi-club-merger-unified-transport-mutual-20261009',
    score=68, verify='pending', tier='pro', key='insuranceasianews',
    pub='2026-10-09T17:07:00+08:00',
    url='https://insuranceasianews.com/tt-club-and-uk-pi-club-members-vote-to-merge-creating-unified-transport-mutual/',
    title='InsuranceAsia News：TT Club與UK P&I Club會員通過合併 組成首個覆蓋全貨運供應鏈的運輸互保',
    summary='InsuranceAsia News 10月9日報道：TT Club 與 UK P&I Club 的會員已表決通過合併，組成首個橫跨整條貨運供應鏈的運輸互保組織（Unified Transport Mutual）。合併將於明年2月20日生效，預計為合併後實體帶來綜合成本率（COR）約5%的改善。報道將此歸入保險公司、海運、船東互保（P&I）及併購類別，並與伊朗衝突等航運風險背景並列。 [EN原文]，正文需訂閱，此條按標題、導語及摘要整理，待補充原文後覆核。',
    why='海運互保領域的整合直接影響亞洲貿易走廊的責任保險供給與定價：COR 改善亦反映規模效應在互保模式中的重要性，對香港海運保險與專項風險池發展具參考價值。',
    a_front='不主動對客提及，作行業整合背景',
    a_mid='納入海運責任保險供給與併購動態',
    a_lead='用於說明互保模式與規模效應',
    a_cross='香港航運保險與專項風險池發展的參照',
    roles={'front': 0, 'midback': 2, 'lead': 2, 'cross': 2},
    boards=['market', 'insurer'],
    themes=['marine', 'p-and-i', 'merger', 'mutual'],
    tags=['TT Club', 'UK P&I Club', '互保', '合併', 'COR'],
    source=IAN('2026-10-09', '付費牆'),
))

# ---- 19. 泰国水浸损失
NEW.append(item(
    id='ian-thailand-insured-flood-losses-297-327m-oic-20261009',
    score=66, verify='pending', tier='pro', key='insuranceasianews',
    pub='2026-10-09T12:27:00+08:00',
    url='https://insuranceasianews.com/thailands-insured-flood-losses-to-date-in-2026-at-us297-327m-oic/',
    title='InsuranceAsia News：泰國2026年承保水浸損失累計2.97億至3.27億美元',
    summary='InsuranceAsia News 10月9日報道，引述泰國保險委員會（OIC）：泰國今年以來承保水浸損失約100億至110億泰銖（2.97億至3.27億美元），索賠主要來自住宅、汽車、農地、果園、工廠及商業。Crawford 的 Sompong Suriwong 指出，最新一次事件未造成重大損失，因財產保單現已加入水浸分項限額（sublimit），限制保險公司責任、避免失控賠付。 [EN原文]，正文需訂閱，此條按標題、導語及摘要整理，待補充原文後覆核。',
    why='「水浸分項限額」是把氣候風險轉為可控承保條件的最直接工具，亦是前線向客戶說明水浸保障上限時最需要理解的產品設計邏輯。',
    a_front='向客戶說明水浸／天災保障時，須明確分項限額的存在與作用，避免客戶誤解為全額保障',
    a_mid='納入亞洲水浸風險與承保條件觀察',
    a_lead='用於說明氣候風險如何被寫入承保條件',
    a_cross='亞洲多市場水浸限額設計對比',
    roles={'front': 2, 'midback': 2, 'lead': 1, 'cross': 1},
    boards=['product', 'market'],
    themes=['flood', 'catastrophe', 'sublimit', 'thailand'],
    tags=['泰國', '水浸', 'OIC', '分項限額', 'Crawford'],
    source=IAN('2026-10-09', '付費牆'),
))

# ---- 20. Tuvalu PCRIC
NEW.append(item(
    id='ian-tuvalu-13th-member-pcric-cyclone-cover-20261009',
    score=64, verify='pending', tier='pro', key='insuranceasianews',
    pub='2026-10-09T07:55:00+08:00',
    url='https://insuranceasianews.com/tuvalu-becomes-13th-member-of-pcric-securing-cyclone-coverage/',
    title='InsuranceAsia News：圖瓦盧成為太平洋巨災風險保險公司第13個成員國 取得氣旋保障',
    summary='InsuranceAsia News 10月9日報道：圖瓦盧加入太平洋巨災風險保險公司（PCRIC），成為第13個成員國，並取得針對氣旋風險的保險保障——氣旋是該國最重大的氣候相關風險之一。 [EN原文]，正文需訂閱，此條按標題、導語及分類標籤（保險公司／太平洋島國／參數式）整理，待補充原文後覆核。',
    why='小島國以參數式區域風險池取得氣候保障，是主權層面風險轉移的低成本範式；對理解香港發展保險相連證券與氣候風險融資的政策方向具參照作用。',
    a_front='不對客引用，作政策背景素材',
    a_mid='納入參數式主權保障案例',
    a_lead='用於說明氣候風險融資的區域協作模式',
    a_cross='太平洋與亞洲主權風險轉移路徑比較',
    roles={'front': 0, 'midback': 1, 'lead': 2, 'cross': 2},
    boards=['market'],
    themes=['parametric', 'climate-risk', 'sovereign-risk-pool', 'pacific'],
    tags=['圖瓦盧', 'PCRIC', '參數式保險', '氣旋', '氣候風險'],
    source=IAN('2026-10-09', '付費牆'),
))

# ---- 21. 亚太人事
NEW.append(item(
    id='ian-apac-insurance-people-moves-13-20261009',
    score=64, verify='pending', tier='pro', key='insuranceasianews',
    pub='2026-10-09T17:00:00+08:00',
    url='https://insuranceasianews.com/bajaj-finserv-everest-aviso-lockton-swiss-re-corso-13-apac-insurance-people-moves-of-the-week/',
    title='InsuranceAsia News：本週亞太保險業13宗人事變動 涉Marsh、Axa XL、Great Eastern、Lockton等',
    summary='InsuranceAsia News 10月9日刊出每週人事匯總：本週亞太區共有13宗保險業人事變動，涉及 Bajaj Finserv、Aviso Specialty、Swiss Re CorSo、Everest、Lockton、Mitsui Bussan Pana Harrison、Marsh、Axa XL、Great Eastern、HDI Global、Knightcorp、Ace Insurance Brokers 及 Howden Re。 [EN原文]，正文需訂閱，此條按標題與摘要整理，待補充原文後覆核。',
    why='區域人事流動是觀察分銷、再保及專業險種策略調整的低成本先行指標，尤其涉及香港市場的再保與經紀團隊。',
    a_front='不對客提及',
    a_mid='納入同業人事流動記錄',
    a_lead='用於觀察區域人才與職能配置趨勢',
    a_cross='香港在區域人才流動中的位置',
    roles={'front': 0, 'midback': 2, 'lead': 1, 'cross': 1},
    boards=['insurer'],
    themes=['people', 'apac', 'distribution', 'reinsurance'],
    tags=['人事變動', '亞太', 'Marsh', 'Howden Re', 'Lockton'],
    source=IAN('2026-10-09', '付費牆'),
))

# ---- 22. 尼泊尔巨灾债券
NEW.append(item(
    id='artemis-nepal-world-bank-quake-catbond-mandate-20261009',
    score=70, verify='verified', tier='pro', key='artemis',
    pub='2026-10-09T22:17:00+08:00',
    url='https://www.artemis.bm/news/nepal-government-approves-world-bank-earthquake-cat-bond-mandate-agreement/',
    title='Artemis：尼泊爾政府批准與世界銀行簽署地震巨災債券授權協議',
    summary='Artemis 10月9日報道：據尼泊爾新聞來源，該國內閣部長會議已批准與世界銀行簽署「尼泊爾地震巨災債券項目」授權協議（Mandate Agreement）。世界銀行今年7月已展開該項目的工作，目標為尼泊爾籌措8,000萬至最高1.9億美元的全額抵押災害風險融資，並擬設計、結構化及發行三年期參數式地震巨災債券；世界銀行將擔任中介，支持設計、交付及影響評估。此次政府批准簽署授權協議，是項目取得政府背書的正式一步。 [EN原文]',
    why='世界銀行主導的主權參數式巨災債券是保險相連證券（ILS）市場的重要供給來源，亦是香港推動 ILS 生態圈時的國際參照：政府授權是發行前最關鍵的程序節點。',
    a_front='引用資本市場工具條款時只作架構說明，不涉及任何投資建議',
    a_mid='納入ILS與巨災債券發行監察',
    a_lead='用於說明主權風險轉移與资本市场工具結合',
    a_cross='香港ILS政策方向與世界銀行發行節奏的對照',
    roles={'front': 1, 'midback': 2, 'lead': 2, 'cross': 2},
    boards=['market'],
    themes=['ils', 'catastrophe-bond', 'parametric', 'sovereign-risk'],
    tags=['尼泊爾', '世界銀行', '巨災債券', '地震', '參數式'],
    source=ART('2026-10-09'),
))

# ---- 23. 飓风 Simon
NEW.append(item(
    id='artemis-hurricane-simon-mexico-catbond-focus-20261009',
    score=68, verify='verified', tier='pro', key='artemis',
    pub='2026-10-09T20:02:00+08:00',
    url='https://www.artemis.bm/news/hurricane-simon-rapidly-intensifying-bringing-mexico-catastrophe-bond-back-into-focus/',
    title='Artemis：颶風Simon快速增強 墨西哥參數式巨災債券再度受關注',
    summary='Artemis 10月9日報道：太平洋颶風 Simon 正快速增強，有機會在周日於墨西哥海岸登陸時維持颶風強度，令規模1.75億美元的 IBRD CAR Mexico 2024（Pacific）參數式巨災債券再度受關注。報道指，就在數週前的9月，同一巨災債券曾面對颶風 Polo 的威脅——Polo 快速增強，中心最低氣壓一度深入足以觸發債券參數式觸發條件的水平，但最終減弱登陸，未造成損失。 [EN原文]',
    why='同一張墨西哥參數式巨災債券在一個月內兩度逼近觸發點，是觀察參數式觸發門檻實際運作的最佳實例；對亞洲新興市場設計參數式產品時選擇觸發指標具參考意義。',
    a_front='僅作市場機制說明，不涉及投資建議',
    a_mid='納入ILS觸發事件監察',
    a_lead='用於說明參數式觸發條件與實際登陸強度的差異',
    a_cross='新興市場參數式產品設計的可借鑑處',
    roles={'front': 0, 'midback': 2, 'lead': 2, 'cross': 1},
    boards=['market'],
    themes=['ils', 'catastrophe-bond', 'parametric', 'natural-catastrophe'],
    tags=['颶風Simon', '墨西哥', 'IBRD CAR', '參數式', '巨災債券'],
    source=ART('2026-10-09'),
))

# ---- 24. Hannover Re Acorn Re
NEW.append(item(
    id='artemis-hannover-re-acorn-re-2026-1-200m-20261009',
    score=70, verify='verified', tier='pro', key='artemis',
    pub='2026-10-09T15:55:00+08:00',
    url='https://www.artemis.bm/news/hannover-re-targets-200m-seventh-acorn-re-parametric-us-earthquake-cat-bond/',
    title='Artemis：漢諾威再保險發行第七宗Acorn Re 目標2億美元美國參數式地震巨災債券',
    summary='Artemis 10月9日報道：漢諾威再保險（Hannover Re）推出每年一度參數式美國地震巨災債券系列的第七宗，Acorn Re Ltd.（Series 2026-1）初步目標2億美元。與前六宗相同，本次由漢諾威再保險作為分出再保險公司，為單一具名分出保險人 Oak Tree Assurance Ltd. 提供保障，同時為其在相關地區的其他再保交易取得額外保障。Acorn Re 系列已連續四年在同期於市場發行，成為每年此時的常規交易。 [EN原文]',
    why='年度例行發行是觀察美國地震風險定價與 ILS 資金胃納的穩定基準；連續四年發行反映贊助人已把資本市場工具納入常規再保結構。',
    a_front='僅作架構說明，不涉及投資建議',
    a_mid='納入ILS發行監察',
    a_lead='用於說明再保公司如何把資本市場工具常規化',
    a_cross='香港發展ILS市場時可參考的年度發行模式',
    roles={'front': 0, 'midback': 2, 'lead': 2, 'cross': 2},
    boards=['market'],
    themes=['ils', 'catastrophe-bond', 'earthquake', 'reinsurance'],
    tags=['漢諾威再保險', 'Acorn Re', '地震', '巨災債券', 'Oak Tree Assurance'],
    source=ART('2026-10-09'),
))

# ---- 25. 飓风 Isaias
NEW.append(item(
    id='artemis-hurricane-isaias-cat3-insured-losses-20261009',
    score=66, verify='pending', tier='pro', key='artemis',
    pub='2026-10-09T14:40:00+08:00',
    url='https://www.artemis.bm/news/hurricane-isaias-forecast-to-hit-cat-3-then-weaken-single-digit-billion-insured-losses-still-likely/',
    title='Artemis：颶風Isaias料增強至三級後減弱 承保損失仍可能達數十億美元量級',
    summary='Artemis 10月9日報道：颶風 Isaias 最新預測將進一步增強為三級（major）颶風，其後在逼近／登陸前減弱，業界仍預期承保損失會達到單位數十億美元（single-digit billion）水平。此條為同一風暴的跟進報道，本站早前已收錄 10月7日及10月8日的預測更新。 [EN原文]，僅按標題與導語整理，詳細段落待覆核。',
    why='同一風暴的逐日損失預估是觀察財產巨災定價預期變化的連續信號；單位數十億美元量級的預估有助理解為何風季淡靜後再保價格仍偏軟。',
    a_front='不作對客引用',
    a_mid='納入風季損失預估追蹤',
    a_lead='用於說明預估損失與再保定價的關係',
    a_cross='美國風季對亞洲再保市場的間接傳導',
    roles={'front': 0, 'midback': 1, 'lead': 2, 'cross': 1},
    boards=['market'],
    themes=['ils', 'natural-catastrophe', 'insured-losses', 'pricing'],
    tags=['颶風Isaias', '三級颶風', '承保損失', '再保定價'],
    source=ART('2026-10-09'),
))

# ---- 26. Conning 人寿保单贴现
NEW.append(item(
    id='artemis-conning-us-life-settlement-market-2035-20261009',
    score=66, verify='verified', tier='pro', key='artemis',
    pub='2026-10-09T13:30:00+08:00',
    url='https://www.artemis.bm/news/conning-forecasts-long-term-expansion-for-us-life-settlement-market-through-2035/',
    title='Artemis：Conning預測美國人壽保單貼現市場將擴張至2035年',
    summary='Artemis 10月9日報道：投資管理顧問 Conning 最新研究預測，美國人壽保單貼現（life settlement）市場將長期擴張至2035年，動力來自投資者對低相關性另類資產的需求、人口老化，以及退休與長期護理融資需求上升和更廣泛的直接面向消費者認知。研究涵蓋2025年市場分析、主要驅動因素，以及年度貼現成交量與市場潛力預測。Conning 指出，較高的保險公司組合收益率或有助提升萬能壽險入帳利率與保費優化策略；在消費者端，美國老年人口擴張與長期護理成本上升，或促使更多保單持有人以貼現代替失效或退保。 [EN原文]',
    why='保單貼現市場與長壽風險互為表裡：同一批高齡保單既是保險公司的負債，亦是被證券化的資產，對理解長壽風險定價與另類資產供給有交叉參考價值。',
    a_front='不對客引用，不構成任何資產建議',
    a_mid='納入長壽風險與另類資產觀察',
    a_lead='用於說明長壽風險的資產化路徑',
    a_cross='亞洲長壽風險轉移市場的成熟度差距',
    roles={'front': 0, 'midback': 2, 'lead': 2, 'cross': 1},
    boards=['market'],
    themes=['longevity', 'life-settlement', 'alternative-assets', 'ils'],
    tags=['Conning', '保單貼現', '長壽風險', '美國', '另類資產'],
    source=ART('2026-10-09'),
))

print('part2 items:', len(NEW))
json.dump(NEW, open('/tmp/_new_part2.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
