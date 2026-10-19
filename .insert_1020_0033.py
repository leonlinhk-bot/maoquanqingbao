#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-20 00:33 cron 增量入库：6 条（窗口 2026-10-19 21:13 → 2026-10-20 00:50 + 两条凌晨前漏采补录）"""
import json, shutil
from datetime import datetime, timezone, timedelta

HK = timezone(timedelta(hours=8))
NOW = datetime.now(HK)
P = 'data/live-items.json'
shutil.copy(P, 'data/live-items-bak-20261020-0033.json')
d = json.load(open(P, encoding='utf-8'))
items = d['items']
have = {i['id'] for i in items}

def mk(**kw):
    base = {
        'clusterCount': 1, 'score': 70, 'verifyStatus': 'verified',
        'boards': [], 'themes': [], 'contentKind': 'news',
    }
    base.update(kw)
    return base

new = []

new.append(mk(
    id='artemis-hannover-ils-capital-20261019',
    publishedAt='2026-10-19T22:15:00+08:00',
    originalUrl='https://www.artemis.bm/news/hannover-re-sees-ils-capital-as-sustainable-reinsurance-addition-source-of-growth-horstmann/',
    sourceKey='artemis', sourceTier='pro', score=72, contentKind='report',
    boards=['market'], themes=['ils', 'alternative-capital', 'reinsurance', 'market'],
    title={'sc': '漢諾威再：ILS 資本已佔再保容量約 18%　視為可持續增量而非替代',
           'tc': '漢諾威再：ILS 資本已佔再保容量約 18%　視為可持續增量而非替代'},
    summary={'sc': '漢諾威再保險 ILS 主管 Patrick Horstmann 在巴登巴登媒體會表示，ILS 資本增速快於傳統再保資本，現約佔整體再保容量 18%，屬可長期持續的增量而非替代。公司 ILS 業務分五塊：巨災債券轉化、抵押式前置（collateralized fronting）、壽險 ILS、巨災債管理公司 Leine Investment，以及 2025 年 11 月在百慕大設立的 Hannover Re Capital Partners（HCP）；HCP 不自留風險，以抵押式前置承接第三方資本，已募得低三位數（百萬美元級）資金並於 7 月 1 日續保全數投放，正與更多投資人洽談增資。',
              'tc': '漢諾威再保險 ILS 主管 Patrick Horstmann 在巴登巴登媒體會表示，ILS 資本增速快於傳統再保資本，現約佔整體再保容量 18%，屬可長期持續的增量而非替代。公司 ILS 業務分五塊：巨災債券轉化、抵押式前置（collateralized fronting）、壽險 ILS、巨災債管理公司 Leine Investment，以及 2025 年 11 月在百慕大設立的 Hannover Re Capital Partners（HCP）；HCP 不自留風險，以抵押式前置承接第三方資本，已募得低三位數（百萬美元級）資金並於 7 月 1 日續保全數投放，正與更多投資人洽談增資。'},
    why={'sc': '香港近年以 ILS 與專屬自保作為資產管理新賽道（今年首宗 sidecar 已落地）。漢諾威再「ILS 佔 18%、且可持續」的判斷，可用於向高客解釋另類資本的長期定位；HCP「不承擔風險、只做前置」的結構，則是理解香港 ILS 平台角色的現成參照。',
         'tc': '香港近年以 ILS 與專屬自保作為資產管理新賽道（今年首宗 sidecar 已落地）。漢諾威再「ILS 佔 18%、且可持續」的判斷，可用於向高客解釋另類資本的長期定位；HCP「不承擔風險、只做前置」的結構，則是理解香港 ILS 平台角色的現成參照。'},
    actions={'front': {'sc': '客戶溝通：另類資本的長期定位', 'tc': '客戶溝通：另類資本的長期定位'},
             'midback': {'sc': '產品盡調：ILS 平台結構與角色', 'tc': '產品盡調：ILS 平台結構與角色'},
             'lead': {'sc': '團隊簡報：ILS 市場佔比與增長', 'tc': '團隊簡報：ILS 市場佔比與增長'},
             'cross': {'sc': '家辦：另類資產配置素材', 'tc': '家辦：另類資產配置素材'}},
    rolesImpact={'front': 1, 'midback': 1, 'lead': 2, 'cross': 2},
    tags={'sc': ['ILS', '另類資本', '再保險', '漢諾威再', '巨災債券'],
          'tc': ['ILS', '另類資本', '再保險', '漢諾威再', '巨災債券']},
    source={'sc': 'Artemis 2026-10-19（漢諾威再巴登巴登媒體會）', 'tc': 'Artemis 2026-10-19（漢諾威再巴登巴登媒體會）',
            'lang': 'en', 'name': 'artemis', 'date': '2026-10-19'},
))

new.append(mk(
    id='rn-howden-re-capital-tool-20261020',
    publishedAt='2026-10-20T00:00:00+08:00',
    originalUrl='https://www.reinsurancene.ws/howden-re-highlights-reinsurances-role-as-a-capital-tool-as-prices-soften/',
    sourceKey='reinsurancenews', sourceTier='pro', score=72, contentKind='report',
    boards=['market'], themes=['reinsurance', 'capital-management', 'roi', 'market'],
    title={'sc': 'Howden Re：再保應視為資本工具而非單純保障　資本輕的組合 ROE 達 22%',
           'tc': 'Howden Re：再保應視為資本工具而非單純保障　資本輕的組合 ROE 達 22%'},
    summary={'sc': 'Howden Re 以 2023–25 年 42 家歐洲非壽險公司為樣本發布基準報告：表現最佳者把再保當作資本管理工具，而非僅是保障。資本輕、回報高的組別每 100 歐元保費只佔約 28 歐元資本，平均 ROE 約 22%；資本密集、低回報組則佔 86 歐元，ROE 不足 5%。綜合成本率最優組 ROE 約 17%、最弱組約 4%，說明資本效率是放大而非創造承保成果。報告建議按明確的資本與回報目標重設再保結構，而非照舊續轉，並把投資風險與承保風險一併納入資本規劃。',
              'tc': 'Howden Re 以 2023–25 年 42 家歐洲非壽險公司為樣本發布基準報告：表現最佳者把再保當作資本管理工具，而非僅是保障。資本輕、回報高的組別每 100 歐元保費只佔約 28 歐元資本，平均 ROE 約 22%；資本密集、低回報組則佔 86 歐元，ROE 不足 5%。綜合成本率最優組 ROE 約 17%、最弱組約 4%，說明資本效率是放大而非創造承保成果。報告建議按明確的資本與回報目標重設再保結構，而非照舊續轉，並把投資風險與承保風險一併納入資本規劃。'},
    why={'sc': '當前再保價格軟化、條款對買方有利，正是重審自留額與波動轉移的窗口。對顧問的啟示是：談再保不該只講「買保障」，而要回到資本效率與 ROE——這套語言在與保司、家辦談風險融資時同樣適用。',
         'tc': '當前再保價格軟化、條款對買方有利，正是重審自留額與波動轉移的窗口。對顧問的啟示是：談再保不該只講「買保障」，而要回到資本效率與 ROE——這套語言在與保司、家辦談風險融資時同樣適用。'},
    actions={'front': {'sc': '客戶溝通：風險融資與資本效率', 'tc': '客戶溝通：風險融資與資本效率'},
             'midback': {'sc': '方案設計：自留額與波動轉移', 'tc': '方案設計：自留額與波動轉移'},
             'lead': {'sc': '團隊簡報：再保買方市場窗口', 'tc': '團隊簡報：再保買方市場窗口'},
             'cross': {'sc': '家辦：保險資本效率視角', 'tc': '家辦：保險資本效率視角'}},
    rolesImpact={'front': 2, 'midback': 2, 'lead': 1, 'cross': 2},
    tags={'sc': ['再保險', '資本管理', 'ROE', '自留額', '歐洲非壽險'],
          'tc': ['再保險', '資本管理', 'ROE', '自留額', '歐洲非壽險']},
    source={'sc': 'Reinsurance News 2026-10-19（引 Howden Re 報告）', 'tc': 'Reinsurance News 2026-10-19（引 Howden Re 報告）',
            'lang': 'en', 'name': 'reinsurancenews', 'date': '2026-10-19'},
))

new.append(mk(
    id='rn-doxa-re-launch-femia-20261019',
    publishedAt='2026-10-19T23:30:00+08:00',
    originalUrl='https://www.reinsurancene.ws/femia-to-lead-newly-launched-doxa-re-as-president/',
    sourceKey='reinsurancenews', sourceTier='pro', score=70, contentKind='news',
    boards=['market', 'insurer'], themes=['reinsurance', 'mga', 'property', 'capacity'],
    title={'sc': 'DOXA 設專險財產再保 MGU　James Femia 任總裁',
           'tc': 'DOXA 設專險財產再保 MGU　James Femia 任總裁'},
    summary={'sc': '美國 MGU 平台 DOXA 成立 DOXA Re，專做財產險成數分保（quota share）及相關比例再保方案，對象為傳統保司、混合型承保體與 MGA。DOXA 首席產品與承保官 Joe Guerrero 指，MGA 與混合承保體計劃持續擴張，令財產險分保安排更複雜，而有專業能力與胃納參與的再保人仍然有限。具 22 年財產再保承保經驗的 James Femia 出任總裁，將以委派承保授權（DUA）建立跨險類、跨地區、跨客群的平衡組合，並擴充承保與分析團隊。',
              'tc': '美國 MGU 平台 DOXA 成立 DOXA Re，專做財產險成數分保（quota share）及相關比例再保方案，對象為傳統保司、混合型承保體與 MGA。DOXA 首席產品與承保官 Joe Guerrero 指，MGA 與混合承保體計劃持續擴張，令財產險分保安排更複雜，而有專業能力與胃納參與的再保人仍然有限。具 22 年財產再保承保經驗的 James Femia 出任總裁，將以委派承保授權（DUA）建立跨險類、跨地區、跨客群的平衡組合，並擴充承保與分析團隊。'},
    why={'sc': 'MGA／委派承保模式在亞洲（含香港一般保險與專業險）快速擴張，瓶頸往往在「誰來承接分保容量」。這條說明資本市場正以 MGU 形態補上這一層，對判斷未來中小保司與 MGA 的再保可得性有參考價值。',
         'tc': 'MGA／委派承保模式在亞洲（含香港一般保險與專業險）快速擴張，瓶頸往往在「誰來承接分保容量」。這條說明資本市場正以 MGU 形態補上這一層，對判斷未來中小保司與 MGA 的再保可得性有參考價值。'},
    actions={'front': {'sc': '客戶溝通：MGA 與承保容量關係', 'tc': '客戶溝通：MGA 與承保容量關係'},
             'midback': {'sc': '方案設計：成數分保結構', 'tc': '方案設計：成數分保結構'},
             'lead': {'sc': '團隊簡報：專業再保平台動態', 'tc': '團隊簡報：專業再保平台動態'},
             'cross': {'sc': '同業情報：MGU 生態變化', 'tc': '同業情報：MGU 生態變化'}},
    rolesImpact={'front': 1, 'midback': 2, 'lead': 1, 'cross': 1},
    tags={'sc': ['再保險', 'MGU', '成數分保', '財產險', '承保能力'],
          'tc': ['再保險', 'MGU', '成數分保', '財產險', '承保能力']},
    source={'sc': 'Reinsurance News 2026-10-19', 'tc': 'Reinsurance News 2026-10-19',
            'lang': 'en', 'name': 'reinsurancenews', 'date': '2026-10-19'},
))

new.append(mk(
    id='rn-france-riots-srcc-20261019',
    publishedAt='2026-10-19T23:00:00+08:00',
    originalUrl='https://www.reinsurancene.ws/france-riots-put-srcc-accumulation-risk-in-focus-for-re-insurers-morningstar-dbrs/',
    sourceKey='reinsurancenews', sourceTier='pro', score=70, contentKind='report',
    boards=['market', 'tech'], themes=['srcc', 'cat-risk', 'reinsurance', 'accumulation'],
    title={'sc': '法國騷亂：保險損失料 10–12 億歐元　SRCC 須按累積風險定價',
           'tc': '法國騷亂：保險損失料 10–12 億歐元　SRCC 須按累積風險定價'},
    summary={'sc': 'Morningstar DBRS 評估，法國最新一輪騷亂在不再惡化的前提下，保險業損失不超過 10 億至 12 億歐元，計入再保回收及向法國政府索賠後，屬可控的盈利事件而非資本事件。截至 10 月 19 日約 2,400 人被捕、至少 3,000 家商戶受損或被搶；2023 年同類騷亂保險損失約 7.3 億歐元。DBRS 指騷亂愈來愈像自然災害，關鍵風險是多個城市同時出現相關索賠，主張把罷工、騷亂與民眾騷動（SRCC）視作累積風險，單獨定價、設限額並安排再保；法國擬設的國家支援機制已獲批但尚未運作，本輪不適用。',
              'tc': 'Morningstar DBRS 評估，法國最新一輪騷亂在不再惡化的前提下，保險業損失不超過 10 億至 12 億歐元，計入再保回收及向法國政府索賠後，屬可控的盈利事件而非資本事件。截至 10 月 19 日約 2,400 人被捕、至少 3,000 家商戶受損或被搶；2023 年同類騷亂保險損失約 7.3 億歐元。DBRS 指騷亂愈來愈像自然災害，關鍵風險是多個城市同時出現相關索賠，主張把罷工、騷亂與民眾騷動（SRCC）視作累積風險，單獨定價、設限額並安排再保；法國擬設的國家支援機制已獲批但尚未運作，本輪不適用。'},
    why={'sc': '香港一般保險與財產險常把 SRCC 以低價附加方式處理。這個案例說明「多城市同時爆發」會形成累積損失：可用於向商業客戶解釋 SRCC 限額與自留安排的必要性，也是與再保人談條款的現實論據。',
         'tc': '香港一般保險與財產險常把 SRCC 以低價附加方式處理。這個案例說明「多城市同時爆發」會形成累積損失：可用於向商業客戶解釋 SRCC 限額與自留安排的必要性，也是與再保人談條款的現實論據。'},
    actions={'front': {'sc': '商業客戶：SRCC 限額與自留說明', 'tc': '商業客戶：SRCC 限額與自留說明'},
             'midback': {'sc': '條款複核：騷亂與民眾騷動', 'tc': '條款複核：騷亂與民眾騷動'},
             'lead': {'sc': '團隊簡報：累積風險案例', 'tc': '團隊簡報：累積風險案例'},
             'cross': {'sc': '高客：政治風險視角', 'tc': '高客：政治風險視角'}},
    rolesImpact={'front': 2, 'midback': 1, 'lead': 1, 'cross': 1},
    tags={'sc': ['SRCC', '累積風險', '法國騷亂', '再保險', '財產險'],
          'tc': ['SRCC', '累積風險', '法國騷亂', '再保險', '財產險']},
    source={'sc': 'Reinsurance News 2026-10-19（引 Morningstar DBRS）', 'tc': 'Reinsurance News 2026-10-19（引 Morningstar DBRS）',
            'lang': 'en', 'name': 'reinsurancenews', 'date': '2026-10-19'},
))

new.append(mk(
    id='ian-niba-2027-brokers-code-20261019',
    publishedAt='2026-10-19T16:47:00+08:00',
    originalUrl='https://insuranceasianews.com/australian-insurance-brokers-new-2027-code-of-practice-doubles-renewal-notice-opens-up-fee-disclosure/',
    sourceKey='insuranceasianews', sourceTier='media', score=66, contentKind='news',
    boards=['reg'], themes=['broker-conduct', 'fee-disclosure', 'regulation', 'professional-standards'],
    title={'sc': '澳洲經紀新守則 2027 年 1 月生效　續保前 28 天聯繫、報酬須答具體金額',
           'tc': '澳洲經紀新守則 2027 年 1 月生效　續保前 28 天聯繫、報酬須答具體金額'},
    summary={'sc': '澳洲全國保險經紀協會（NIBA）在黃金海岸年會發布 2027 版《保險經紀執業守則》，2027 年 1 月 1 日生效。按 7 月諮詢稿：客戶可詢問經紀報酬並取得具體金額（不分產品類別）；新增續保前 28 天主動聯繫承諾；記錄保存升格為守則義務；強制報酬披露擴至全部分層／樓宇保險。守則合規委員會（IBCCC）數據顯示披露壓力仍在：報酬披露違規由 2023 年 42 宗升至 2024 年 334 宗，2025 年報合計 5,417 宗違規。NIBA 另於 10 月 20 日發布經紀業 AI 影響研究。',
              'tc': '澳洲全國保險經紀協會（NIBA）在黃金海岸年會發布 2027 版《保險經紀執業守則》，2027 年 1 月 1 日生效。按 7 月諮詢稿：客戶可詢問經紀報酬並取得具體金額（不分產品類別）；新增續保前 28 天主動聯繫承諾；記錄保存升格為守則義務；強制報酬披露擴至全部分層／樓宇保險。守則合規委員會（IBCCC）數據顯示披露壓力仍在：報酬披露違規由 2023 年 42 宗升至 2024 年 334 宗，2025 年報合計 5,417 宗違規。NIBA 另於 10 月 20 日發布經紀業 AI 影響研究。'},
    why={'sc': '香港經紀同樣面對「報酬披露＋續保主動聯繫」的監管方向（保監局轉介費上限與佣金分期已落地）。澳洲把「客戶可問、須答具體金額」寫進行業守則，是可預期的下一步參照；違規宗數一年增近七倍，也說明披露是最易踩線的一項。',
         'tc': '香港經紀同樣面對「報酬披露＋續保主動聯繫」的監管方向（保監局轉介費上限與佣金分期已落地）。澳洲把「客戶可問、須答具體金額」寫進行業守則，是可預期的下一步參照；違規宗數一年增近七倍，也說明披露是最易踩線的一項。'},
    actions={'front': {'sc': '客戶溝通：報酬披露的答法', 'tc': '客戶溝通：報酬披露的答法'},
             'midback': {'sc': '流程：續保前主動聯繫機制', 'tc': '流程：續保前主動聯繫機制'},
             'lead': {'sc': '團隊簡報：經紀監管趨勢', 'tc': '團隊簡報：經紀監管趨勢'},
             'cross': {'sc': '合規參考：同業守則條文', 'tc': '合規參考：同業守則條文'}},
    rolesImpact={'front': 1, 'midback': 2, 'lead': 2, 'cross': 0},
    tags={'sc': ['經紀守則', '報酬披露', '續保通知', '合規', '澳洲'],
          'tc': ['經紀守則', '報酬披露', '續保通知', '合規', '澳洲']},
    source={'sc': 'InsuranceAsia News 2026-10-19（並參考 Insurance Business AU 2026-10-13）',
            'tc': 'InsuranceAsia News 2026-10-19（並參考 Insurance Business AU 2026-10-13）',
            'lang': 'en', 'name': 'insuranceasianews', 'date': '2026-10-19'},
))

new.append(mk(
    id='ian-penang-bridge-fire-ruling-20261019',
    publishedAt='2026-10-19T14:14:00+08:00',
    originalUrl='https://insuranceasianews.com/penang-bridge-ruling-shows-why-the-first-days-on-site-matter-most/',
    sourceKey='insuranceasianews', sourceTier='media', score=64, contentKind='news',
    boards=['insurer'], themes=['claims', 'forensic', 'liability', 'fire'],
    title={'sc': '檳城大橋火災裁決：現場取證在首幾天定輸贏　國能須賠 1,050 萬馬幣',
           'tc': '檳城大橋火災裁決：現場取證在首幾天定輸贏　國能須賠 1,050 萬馬幣'},
    summary={'sc': '2021 年 2 月檳城大橋火災，馬來亞高等法院五年後裁定起火源於高壓電纜既有機械損傷引致的電弧，駁回「外來垃圾起火」一說，判 Tenaga Nasional 向 Projek Lebuhraya Usahasama 賠償 1,050 萬馬幣（約 260 萬美元）。撰文的 Halliwell 亞洲法證服務總監 Anand Ghnavello 指，法院高度倚重事發初期現場勘查取得的物證，並與自動故障紀錄、殘留電纜護套損傷互相印證；現場一旦清理、修復或受天氣影響，關鍵爭點便無法回答。他主張複雜火災應把法證到場列為標準動作，並明確「先取證、後清理」及證據鏈。',
              'tc': '2021 年 2 月檳城大橋火災，馬來亞高等法院五年後裁定起火源於高壓電纜既有機械損傷引致的電弧，駁回「外來垃圾起火」一說，判 Tenaga Nasional 向 Projek Lebuhraya Usahasama 賠償 1,050 萬馬幣（約 260 萬美元）。撰文的 Halliwell 亞洲法證服務總監 Anand Ghnavello 指，法院高度倚重事發初期現場勘查取得的物證，並與自動故障紀錄、殘留電纜護套損傷互相印證；現場一旦清理、修復或受天氣影響，關鍵爭點便無法回答。他主張複雜火災應把法證到場列為標準動作，並明確「先取證、後清理」及證據鏈。'},
    why={'sc': '香港企業財產險與工程險理賠常有「先搶修、後查因」的實務衝突。這宗裁決是現成教材：保單條款下的檢驗與施救義務、以及理賠初期的現場保全，直接決定因果關係能否舉證——適合用於商業客戶理賠工作坊。',
         'tc': '香港企業財產險與工程險理賠常有「先搶修、後查因」的實務衝突。這宗裁決是現成教材：保單條款下的檢驗與施救義務、以及理賠初期的現場保全，直接決定因果關係能否舉證——適合用於商業客戶理賠工作坊。'},
    actions={'front': {'sc': '客戶溝通：出險後先保全現場', 'tc': '客戶溝通：出險後先保全現場'},
             'midback': {'sc': '理賠協同：法證介入時點', 'tc': '理賠協同：法證介入時點'},
             'lead': {'sc': '團隊簡報：理賠舉證案例', 'tc': '團隊簡報：理賠舉證案例'},
             'cross': {'sc': '高客：財物損失舉證提醒', 'tc': '高客：財物損失舉證提醒'}},
    rolesImpact={'front': 1, 'midback': 2, 'lead': 1, 'cross': 0},
    tags={'sc': ['理賠', '法證', '火災', '因果關係', '工程險'],
          'tc': ['理賠', '法證', '火災', '因果關係', '工程險']},
    source={'sc': 'InsuranceAsia News 2026-10-19（Halliwell 法證評論）', 'tc': 'InsuranceAsia News 2026-10-19（Halliwell 法證評論）',
            'lang': 'en', 'name': 'insuranceasianews', 'date': '2026-10-19'},
))

import zhconv

def _simp(v):
    if isinstance(v, str):
        return zhconv.convert(v, 'zh-cn')
    if isinstance(v, list):
        return [zhconv.convert(x, 'zh-cn') if isinstance(x, str) else x for x in v]
    return v

for it in new:
    for key in ('title', 'summary', 'why', 'source'):
        obj = it.get(key)
        if isinstance(obj, dict) and obj.get('sc') == obj.get('tc'):
            obj['sc'] = _simp(obj['tc'])
    for key in ('actions',):
        for slot, obj in (it.get(key) or {}).items():
            if isinstance(obj, dict) and obj.get('sc') == obj.get('tc'):
                obj['sc'] = _simp(obj['tc'])
    if it.get('tags', {}).get('sc') == it.get('tags', {}).get('tc'):
        it['tags']['sc'] = _simp(it['tags']['tc'])

added = []
for it in new:
    if it['id'] in have:
        print('SKIP dup id:', it['id'])
        continue
    added.append(it)

d['items'] = added + items
d['meta']['generatedAt'] = NOW.replace(microsecond=0).isoformat()
d['meta']['itemCount'] = len(d['items'])
json.dump(d, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('inserted', len(added), 'total', len(d['items']))
for it in added:
    print(' +', it['id'], it['publishedAt'], it['sourceKey'], it['sourceTier'], it['score'])
