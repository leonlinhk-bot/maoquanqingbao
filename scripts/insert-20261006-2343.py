#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 2026-10-06 (23:43 run) increment into live-items.json"""
import json
from datetime import datetime, timezone, timedelta

NOW = datetime.now(timezone(timedelta(hours=8))).strftime('%Y-%m-%dT%H:%M:%S+08:00')
CR = {"sc": "本站导读", "tc": "本站導讀"}


def mk(id_, sourceKey, tier, kind, pub, url, title_sc, title_tc, sum_sc, sum_tc,
       why_sc, why_tc, a_f, a_m, a_l, a_c, ri, boards, themes, tags, src_sc, src_tc, lang, score):
    ts = tags
    return {
        "clusterCount": 1, "score": score, "verifyStatus": "pending",
        "sourceTier": tier, "sourceKey": sourceKey, "contentKind": kind,
        "actions": {
            "front": {"sc": a_f[0], "tc": a_f[1]},
            "midback": {"sc": a_m[0], "tc": a_m[1]},
            "lead": {"sc": a_l[0], "tc": a_l[1]},
            "cross": {"sc": a_c[0], "tc": a_c[1]},
        },
        "rolesImpact": {"front": ri[0], "midback": ri[1], "lead": ri[2], "cross": ri[3]},
        "boards": boards, "themes": themes,
        "tags": {"sc": ts, "tc": ts},
        "contentRole": CR, "featured": False, "evergreen": False, "ingestedAt": NOW,
        "id": id_, "publishedAt": pub, "originalUrl": url,
        "title": {"sc": title_sc, "tc": title_tc},
        "summary": {"sc": sum_sc, "tc": sum_tc},
        "why": {"sc": why_sc, "tc": why_tc},
        "source": {"sc": src_sc, "tc": src_tc, "lang": lang},
    }


ITEMS = []

ITEMS.append(mk(
 "hkma-bnm-bilateral-cooperation-20261006", "hkma", "official", "press", "2026-10-06",
 "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/10/20261006-4/",
 "金管局與馬來西亞央行加強雙邊合作：涵蓋跨境支付、金融科技與伊斯蘭金融",
 "金管局與馬來西亞央行加強雙邊合作：涵蓋跨境支付、金融科技與伊斯蘭金融",
 "金管局10月6日宣布與馬來西亞中央銀行（Bank Negara Malaysia）加強雙邊合作，由總裁余偉文代表簽署；合作涵蓋跨境支付、金融科技應用，並提及支持伊斯蘭金融市場發展。屬兩地監管機構層面的合作框架，具體措施有待雙方後續公布。 [EN原文]",
 "金管局10月6日宣布與馬來西亞中央銀行（Bank Negara Malaysia）加強雙邊合作，由總裁余偉文代表簽署；合作涵蓋跨境支付、金融科技應用，並提及支持伊斯蘭金融市場發展。屬兩地監管機構層面的合作框架，具體措施有待雙方後續公布。 [EN原文]",
 "香港在東盟方向持續鋪路，對「香港作為區域風險管理中心與資金樞紐」的敘事是加分項。前線在談跨境資產與區域配置時可作宏觀環境佐證，但不應延伸解讀為個別產品或市場的利好。",
 "香港在東盟方向持續鋪路，對「香港作為區域風險管理中心與資金樞紐」的敘事是加分項。前線在談跨境資產與區域配置時可作宏觀環境佐證，但不應延伸解讀為個別產品或市場的利好。",
 ("客戶問及香港競爭力時，引述官方新聞稿的公開表述即可，不作額外推論",
  "客戶問及香港競爭力時，引述官方新聞稿的公開表述即可，不作額外推論"),
 ("留意跨境支付與金融科技合作的合規口徑（數據、反洗錢）後續指引",
  "留意跨境支付與金融科技合作的合規口徑（數據、反洗錢）後續指引"),
 ("納入區域佈局簡報素材，強調香港與東盟的互聯互通",
  "納入區域佈局簡報素材，強調香港與東盟的互聯互通"),
 ("跨境架構客戶可參考兩地監管合作方向，具體安排以官方公布為準",
  "跨境架構客戶可參考兩地監管合作方向，具體安排以官方公布為準"),
 (1, 2, 3, 3), ["reg", "market"],
 ["hkma", "malaysia", "asean", "cross-border", "cooperation"],
 ["金管局", "馬來西亞央行", "雙邊合作", "跨境支付", "伊斯蘭金融"],
 "香港金融管理局 2026-10-06 新聞稿（中／英）", "香港金融管理局 2026-10-06 新聞稿（中／英）", "en", 88))

ITEMS.append(mk(
 "mpfa-mpf-provisional-returns-20261006", "mpfa", "official", "stats", "2026-10-06",
 "https://www.mpfa.org.hk/en/info-centre/press-releases/20261006",
 "積金局公布強積金臨時投資回報：股票基金過去12個月平均年率化淨回報10.3%",
 "積金局公布強積金臨時投資回報：股票基金過去12個月平均年率化淨回報10.3%",
 "積金局10月6日公布截至9月底的臨時數據：股票基金過去12個月平均年率化淨回報10.3%、混合資產基金8.5%，預設投資策略（DIS）核心累積基金9.5%（自2017年推出以來年率化7.1%）；債券基金期內平均錄得1.5%虧損。積金局同時提醒強積金屬超過40年的長線投資，不應以短線角度看待或嘗試捕捉市場。 [EN原文]",
 "積金局10月6日公布截至9月底的臨時數據：股票基金過去12個月平均年率化淨回報10.3%、混合資產基金8.5%，預設投資策略（DIS）核心累積基金9.5%（自2017年推出以來年率化7.1%）；債券基金期內平均錄得1.5%虧損。積金局同時提醒強積金屬超過40年的長線投資，不應以短線角度看待或嘗試捕捉市場。 [EN原文]",
 "官方季度口徑是最可核查的一手數據，可用於回應團隊與客戶對「強積金回報」的提問，亦適合說明DIS的長期基準。須注意這是全體基金平均、且屬過去12個月區間，不構成任何個別基金或產品的回報預期。",
 "官方季度口徑是最可核查的一手數據，可用於回應團隊與客戶對「強積金回報」的提問，亦適合說明DIS的長期基準。須注意這是全體基金平均、且屬過去12個月區間，不構成任何個別基金或產品的回報預期。",
 ("客戶問回報時，只引述積金局公布的「全體平均」並說明區間與截至月份",
  "客戶問回報時，只引述積金局公布的「全體平均」並說明區間與截至月份"),
 ("檢視銷售與推廣材料有否誤用「全體平均」數字作個別產品賣點",
  "檢視銷售與推廣材料有否誤用「全體平均」數字作個別產品賣點"),
 ("以官方數據向團隊說明長線投資與分散配置的理由",
  "以官方數據向團隊說明長線投資與分散配置的理由"),
 ("只作數據引用，不套用於任何個別跨境或投資架構建議",
  "只作數據引用，不套用於任何個別跨境或投資架構建議"),
 (2, 2, 2, 1), ["market", "product"],
 ["mpf", "retirement", "dis", "returns", "stats"],
 ["積金局", "強積金", "DIS", "核心累積基金", "投資回報"],
 "積金局 2026-10-06 新聞稿（中／英）", "積金局 2026-10-06 新聞稿（中／英）", "en", 90))

ITEMS.append(mk(
 "ia-dpp-eap-circular-20261002", "ia_circular", "official", "circular", "2026-10-02",
 "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/files/20261002_Circulars_DPP_and_EAP_Eng.pdf",
 "保監局通函：紀律處分委員會小組及專家顧問小組的委任與續任",
 "保監局通函：紀律處分委員會小組及專家顧問小組的委任與續任",
 "保監局10月2日發出通函，公布保險業監管局紀律處分委員會小組（Disciplinary Panel Pool）及專家顧問小組（Expert Advisor Panel）的委任及續任安排。 [EN原文]",
 "保監局10月2日發出通函，公布保險業監管局紀律處分委員會小組（Disciplinary Panel Pool）及專家顧問小組（Expert Advisor Panel）的委任及續任安排。 [EN原文]",
 "紀律處分與專家顧問名單屬執法架構的常設人事安排，反映保監局處理操守個案的機制。中後台可作認識執法流程的索引，但不涉個別公司評價。",
 "紀律處分與專家顧問名單屬執法架構的常設人事安排，反映保監局處理操守個案的機制。中後台可作認識執法流程的索引，但不涉個別公司評價。",
 ("無需主動向客戶提及；被問及監管執法流程時，引述公開通函",
  "無需主動向客戶提及；被問及監管執法流程時，引述公開通函"),
 ("把通函歸入合規資料庫，標註紀律處分程序的節點",
  "把通函歸入合規資料庫，標註紀律處分程序的節點"),
 ("提醒團隊紀律處分機制的獨立性與程序性",
  "提醒團隊紀律處分機制的獨立性與程序性"),
 ("對跨境架構無直接影響", "對跨境架構無直接影響"),
 (0, 2, 1, 0), ["reg"],
 ["ia", "enforcement", "governance", "circular"],
 ["保監局", "紀律處分委員會", "專家顧問小組", "通函"],
 "保險業監管局 2026-10-02 通函", "保險業監管局 2026-10-02 通函", "en", 86))

ITEMS.append(mk(
 "hk-freest-economy-fraser-20261006", "govhk", "official", "press", "2026-10-06T20:00:00+08:00",
 "https://www.info.gov.hk/gia/general/202610/06/P2026100600631.htm",
 "菲沙研究所報告：香港繼續獲評為全球最自由經濟體",
 "菲沙研究所報告：香港繼續獲評為全球最自由經濟體",
 "菲沙研究所10月6日發表《世界經濟自由度2026年度報告》，香港繼續獲評為全球最自由經濟體；在五個評估大項中，「國際貿易自由」蟬聯首位，「監管」維持全球第二。政府發言人表示，報告肯定香港的自由市場優勢及開放、高效和公平的營商環境。",
 "菲沙研究所10月6日發表《世界經濟自由度2026年度報告》，香港繼續獲評為全球最自由經濟體；在五個評估大項中，「國際貿易自由」蟬聯首位，「監管」維持全球第二。政府發言人表示，報告肯定香港的自由市場優勢及開放、高效和公平的營商環境。",
 "屬可公開引用的國際評級材料，常用於回應客戶對香港營商與資金環境的關注。適合作為宏觀背景，而非個別產品或回報的理據。",
 "屬可公開引用的國際評級材料，常用於回應客戶對香港營商與資金環境的關注。適合作為宏觀背景，而非個別產品或回報的理據。",
 ("客戶關注資金環境時，引述報告結論與政府公開表述",
  "客戶關注資金環境時，引述報告結論與政府公開表述"),
 ("對外材料引用時註明報告名稱、發布機構與日期",
  "對外材料引用時註明報告名稱、發布機構與日期"),
 ("用於團隊對外簡報的宏觀開場", "用於團隊對外簡報的宏觀開場"),
 ("向跨境客戶說明香港制度穩定性時可引用", "向跨境客戶說明香港制度穩定性時可引用"),
 (1, 1, 2, 1), ["market"],
 ["hong-kong", "competitiveness", "freedom", "regulation"],
 ["菲沙研究所", "經濟自由度", "香港", "營商環境"],
 "香港特區政府新聞公報 2026-10-06", "香港特區政府新聞公報 2026-10-06", "zh", 85))

ITEMS.append(mk(
 "aia-genz-mpf-virtual-competition-20261005", "aia", "insurer", "press", "2026-10-05T18:34:00+08:00",
 "https://www.stheadline.com/investment/3622739/",
 "友邦香港：不足兩成Z世代兩年內轉換MPF組合，推「AIA MPF虛擬投資比賽」",
 "友邦香港：不足兩成Z世代兩年內轉換MPF組合，推「AIA MPF虛擬投資比賽」",
 "友邦香港表示，旗下強積金成員中不足20%的Z世代成員在過去兩年曾轉換投資組合，反映年輕成員較少主動管理MPF，且資產偏向保證基金及混合資產基金等低至中度風險類別。該公司推出為期三個月的「AIA MPF虛擬投資比賽」，以虛擬資金模擬組合，比賽不涉真實資金及實際強積金交易；並表示其智能投資顧問「積金『智』邦手」推出滿一年。",
 "友邦香港表示，旗下強積金成員中不足20%的Z世代成員在過去兩年曾轉換投資組合，反映年輕成員較少主動管理MPF，且資產偏向保證基金及混合資產基金等低至中度風險類別。該公司推出為期三個月的「AIA MPF虛擬投資比賽」，以虛擬資金模擬組合，比賽不涉真實資金及實際強積金交易；並表示其智能投資顧問「積金『智』邦手」推出滿一年。",
 "保司以遊戲化與數碼顧問拉動年輕MPF成員參與度，是產品以外的競爭動作。對前線的啟示是MPF討論正從回報轉向行為引導：主動管理、風險與投資年期匹配。",
 "保司以遊戲化與數碼顧問拉動年輕MPF成員參與度，是產品以外的競爭動作。對前線的啟示是MPF討論正從回報轉向行為引導：主動管理、風險與投資年期匹配。",
 ("與年輕客戶談MPF時，引導討論風險承受能力與投資年期，而非追逐短期回報",
  "與年輕客戶談MPF時，引導討論風險承受能力與投資年期，而非追逐短期回報"),
 ("檢視MPF相關推廣物料有否涉及回報暗示或保證性表述",
  "檢視MPF相關推廣物料有否涉及回報暗示或保證性表述"),
 ("觀察保司數碼工具的客戶黏性，納入競爭情報",
  "觀察保司數碼工具的客戶黏性，納入競爭情報"),
 ("無直接影響", "無直接影響"),
 (2, 1, 2, 0), ["product", "tech"],
 ["mpf", "digital", "gen-z", "insurer", "distribution"],
 ["友邦香港", "強積金", "虛擬投資比賽", "積金智邦手", "數碼工具"],
 "星島頭條 2026-10-05 報道", "星島頭條 2026-10-05 報道", "zh", 78))

ITEMS.append(mk(
 "bochk-online-life-premium-digital-one-20261006", "bochk", "insurer", "press", "2026-10-06T13:51:00+08:00",
 "https://hk.finance.yahoo.com/news/%E8%B2%A1%E7%B6%93-%E4%B8%AD%E9%8A%80%E9%A6%99%E6%B8%AF%E6%95%B8%E7%A2%BC%E7%90%86%E8%B2%A1%E9%9C%80%E6%B1%82%E5%8D%87%E6%BA%AB-%E7%B7%9A%E4%B8%8A%E4%BA%BA%E5%A3%BD%E4%BF%9D%E9%9A%AA%E6%96%B0%E9%80%A0%E4%BF%9D%E8%B2%BB%E5%A2%9E%E8%BF%91%E4%B8%83%E6%88%90-044410131.html",
 "中銀香港：線上人壽保險新造保費按年升近七成 推「Digital One」數碼財富平台",
 "中銀香港：線上人壽保險新造保費按年升近七成 推「Digital One」數碼財富平台",
 "中銀香港10月6日表示，客戶對數碼理財及跨境金融服務需求持續上升：截至今年8月，線上人壽保險新造保費按年上升近七成，超過九成相關交易經數碼渠道完成；基金交易近七成經網上完成，帶動零售銀行基金業務市佔連續五年上升。該行同時推出「Digital One智勝一籌」數碼財富管理平台，新增基金交易導航及外匯限價指示功能。",
 "中銀香港10月6日表示，客戶對數碼理財及跨境金融服務需求持續上升：截至今年8月，線上人壽保險新造保費按年上升近七成，超過九成相關交易經數碼渠道完成；基金交易近七成經網上完成，帶動零售銀行基金業務市佔連續五年上升。該行同時推出「Digital One智勝一籌」數碼財富管理平台，新增基金交易導航及外匯限價指示功能。",
 "銀保渠道數碼化是香港分銷格局的關鍵變量：銀行以平台化服務承接保險與財富管理需求，直接影響中介在「保障以外」的比較優勢。",
 "銀保渠道數碼化是香港分銷格局的關鍵變量：銀行以平台化服務承接保險與財富管理需求，直接影響中介在「保障以外」的比較優勢。",
 ("客戶在銀行渠道被比較時，聚焦保障缺口與理賠服務等可核對的差異",
  "客戶在銀行渠道被比較時，聚焦保障缺口與理賠服務等可核對的差異"),
 ("對外引用銀行自行公布數據時註明時點與來源",
  "對外引用銀行自行公布數據時註明時點與來源"),
 ("把渠道數碼化列入競爭情報，思考協作或差異化定位",
  "把渠道數碼化列入競爭情報，思考協作或差異化定位"),
 ("跨境理財客戶可留意數碼渠道的開戶與服務安排",
  "跨境理財客戶可留意數碼渠道的開戶與服務安排"),
 (2, 2, 3, 1), ["product", "market"],
 ["bancassurance", "digital", "distribution", "hong-kong"],
 ["中銀香港", "線上保險", "新造保費", "數碼財富"],
 "Yahoo 財經（香港）2026-10-06 報道", "Yahoo 財經（香港）2026-10-06 報道", "zh", 78))

ITEMS.append(mk(
 "prudential-prismic-5bn-reinsurance-20261006", "prudential", "insurer", "news", "2026-10-06T12:20:00+08:00",
 "https://insuranceasianews.com/prudential-agrees-us5bn-reinsurance-deal-with-prismic-life/",
 "保誠與 Prismic Life 達成約50億美元再保險協議",
 "保誠與 Prismic Life 達成約50億美元再保險協議",
 "InsuranceAsia News 10月6日報道：保誠（Prudential）與 Prismic Life 達成約50億美元的再保險交易，屬集團層面的風險轉移與資本管理安排。 [EN原文]",
 "InsuranceAsia News 10月6日報道：保誠（Prudential）與 Prismic Life 達成約50億美元的再保險交易，屬集團層面的風險轉移與資本管理安排。 [EN原文]",
 "大型壽險集團持續把長壽與投資風險轉移至第三方資本，反映行業在資本效率與資產負債管理上的取向；對理解集團層面的財務安排背景有參考價值。",
 "大型壽險集團持續把長壽與投資風險轉移至第三方資本，反映行業在資本效率與資產負債管理上的取向；對理解集團層面的財務安排背景有參考價值。",
 ("客戶問及公司財務穩健性時，只引述公司公開披露與監管資本要求",
  "客戶問及公司財務穩健性時，只引述公司公開披露與監管資本要求"),
 ("涉及集團層面交易不作專業判斷，以官方披露為準",
  "涉及集團層面交易不作專業判斷，以官方披露為準"),
 ("納入保司動態觀察清單", "納入保司動態觀察清單"),
 ("高淨值客戶架構討論可留意同業思路，但不作建議",
  "高淨值客戶架構討論可留意同業思路，但不作建議"),
 (1, 2, 2, 1), ["insurer", "market"],
 ["reinsurance", "capital", "prudential", "risk-transfer"],
 ["保誠", "Prismic Life", "再保險", "資本管理"],
 "InsuranceAsia News 2026-10-06 報道", "InsuranceAsia News 2026-10-06 報道", "en", 76))

ITEMS.append(mk(
 "ian-canopius-castle-underwriter-qbe-20261006", "insuranceasianews", "pro", "news", "2026-10-06T23:19:00+08:00",
 "https://insuranceasianews.com/canopius-to-takeover-as-castle-insurance-underwriter-from-qbe/",
 "Canopius 接替 QBE 出任 Castle Insurance 承保人",
 "Canopius 接替 QBE 出任 Castle Insurance 承保人",
 "InsuranceAsia News 10月6日報道：Canopius 將接替 QBE 出任 Castle Insurance 的承保人，屬亞洲（再）保險市場承保能力與合作安排的變動。 [EN原文]",
 "InsuranceAsia News 10月6日報道：Canopius 將接替 QBE 出任 Castle Insurance 的承保人，屬亞洲（再）保險市場承保能力與合作安排的變動。 [EN原文]",
 "承保人更替關係到既有保單的續保安排與核保口徑，屬渠道與專業險種層面的實務信息。",
 "承保人更替關係到既有保單的續保安排與核保口徑，屬渠道與專業險種層面的實務信息。",
 ("專屬或特殊險種客戶問及承保人變更時，只引述公開報道並提示以保單文件為準",
  "專屬或特殊險種客戶問及承保人變更時，只引述公開報道並提示以保單文件為準"),
 ("留意承保人變更對條款與續保的實務影響", "留意承保人變更對條款與續保的實務影響"),
 ("納入渠道與專業險種情報", "納入渠道與專業險種情報"),
 ("跨境風險安排可留意承保能力來源變化", "跨境風險安排可留意承保能力來源變化"),
 (1, 2, 2, 1), ["insurer", "market"],
 ["apac", "underwriting", "mga", "capacity"],
 ["Canopius", "Castle Insurance", "QBE", "承保人", "亞洲"],
 "InsuranceAsia News 2026-10-06 報道", "InsuranceAsia News 2026-10-06 報道", "en", 72))

ITEMS.append(mk(
 "ian-meritz-indonesia-jv-stake-20261006", "insuranceasianews", "pro", "news", "2026-10-06T18:04:00+08:00",
 "https://insuranceasianews.com/meritz-moving-to-sell-51-stake-in-indonesian-jv-report/",
 "韓國 Meritz 擬出售印尼合資公司51%股權",
 "韓國 Meritz 擬出售印尼合資公司51%股權",
 "InsuranceAsia News 10月6日報道（據報）：韓國 Meritz 集團計劃出售其印尼合資保險公司的51%股權。此舉反映韓國險企在東南亞佈局的策略調整，交易仍須待監管及相關方批准。 [EN原文]",
 "InsuranceAsia News 10月6日報道（據報）：韓國 Meritz 集團計劃出售其印尼合資保險公司的51%股權。此舉反映韓國險企在東南亞佈局的策略調整，交易仍須待監管及相關方批准。 [EN原文]",
 "東南亞合資保險股權變動，是觀察亞洲險企區域策略與資本配置的窗口；屬行業格局情報，與香港市場直接關聯有限。",
 "東南亞合資保險股權變動，是觀察亞洲險企區域策略與資本配置的窗口；屬行業格局情報，與香港市場直接關聯有限。",
 ("無需主動提及", "無需主動提及"),
 ("屬據報消息，若對外引用須標明未經官方確認", "屬據報消息，若對外引用須標明未經官方確認"),
 ("納入亞洲險企區域策略觀察", "納入亞洲險企區域策略觀察"),
 ("無直接影響", "無直接影響"),
 (0, 1, 2, 1), ["insurer", "market"],
 ["indonesia", "korea", "mergers-acquisitions", "apac"],
 ["Meritz", "印尼", "合資", "股權出售", "韓國"],
 "InsuranceAsia News 2026-10-06 報道", "InsuranceAsia News 2026-10-06 報道", "en", 72))

ITEMS.append(mk(
 "ian-axa-xl-paul-gardner-asia-20261006", "insuranceasianews", "pro", "news", "2026-10-06T14:08:00+08:00",
 "https://insuranceasianews.com/axa-xl-promotes-paul-gardner-to-asia-underwriting-manager-for-political-risk-credit-bond/",
 "AXA XL 擢升 Paul Gardner 為亞洲政治風險、信用及保證核保主管",
 "AXA XL 擢升 Paul Gardner 為亞洲政治風險、信用及保證核保主管",
 "InsuranceAsia News 10月6日報道：AXA XL 擢升 Paul Gardner 出任亞洲區政治風險、信用及保證（credit & bond）核保主管。 [EN原文]",
 "InsuranceAsia News 10月6日報道：AXA XL 擢升 Paul Gardner 出任亞洲區政治風險、信用及保證（credit & bond）核保主管。 [EN原文]",
 "專業險種（政治風險、信用及保證）在亞洲的核保人事佈局，反映該類風險的區域需求與承保能力配置。",
 "專業險種（政治風險、信用及保證）在亞洲的核保人事佈局，反映該類風險的區域需求與承保能力配置。",
 ("企業客戶問及信用與保證保險時，可留意區域核保團隊配置",
  "企業客戶問及信用與保證保險時，可留意區域核保團隊配置"),
 ("納入專業險種供應商情報", "納入專業險種供應商情報"),
 ("團隊拓展企業客戶時納入參考", "團隊拓展企業客戶時納入參考"),
 ("跨境企業風險安排的供應商視角", "跨境企業風險安排的供應商視角"),
 (1, 1, 2, 1), ["insurer"],
 ["apac", "underwriting", "people-moves", "credit-risk"],
 ["AXA XL", "政治風險", "信用保證", "核保", "人事"],
 "InsuranceAsia News 2026-10-06 報道", "InsuranceAsia News 2026-10-06 報道", "en", 70))

ITEMS.append(mk(
 "ian-swiss-re-corso-adnan-bhat-20261006", "insuranceasianews", "pro", "news", "2026-10-06T14:20:00+08:00",
 "https://insuranceasianews.com/adnan-bhat-joins-swiss-re-corso-as-apac-global-network-manager/",
 "瑞士再保險企業解決方案委任 Adnan Bhat 為亞太區全球網絡經理",
 "瑞士再保險企業解決方案委任 Adnan Bhat 為亞太區全球網絡經理",
 "InsuranceAsia News 10月6日報道：Swiss Re Corporate Solutions（瑞士再保險企業解決方案）委任 Adnan Bhat 為亞太區全球網絡經理，負責跨市場客戶與網絡協調。 [EN原文]",
 "InsuranceAsia News 10月6日報道：Swiss Re Corporate Solutions（瑞士再保險企業解決方案）委任 Adnan Bhat 為亞太區全球網絡經理，負責跨市場客戶與網絡協調。 [EN原文]",
 "再保／企業解決方案團隊的區域人事佈局，是跨國企業風險安排的供應側觀察點。",
 "再保／企業解決方案團隊的區域人事佈局，是跨國企業風險安排的供應側觀察點。",
 ("無需主動提及", "無需主動提及"),
 ("納入再保險供應商情報", "納入再保險供應商情報"),
 ("跨國企業客戶項目可留意供應商網絡", "跨國企業客戶項目可留意供應商網絡"),
 ("跨境架構的供應商視角參考", "跨境架構的供應商視角參考"),
 (0, 1, 2, 1), ["insurer"],
 ["apac", "people-moves", "swiss-re", "corporate-solutions"],
 ["Swiss Re", "企業解決方案", "亞太", "人事"],
 "InsuranceAsia News 2026-10-06 報道", "InsuranceAsia News 2026-10-06 報道", "en", 70))

ITEMS.append(mk(
 "ian-el-nino-australia-bushfire-flood-20261006", "insuranceasianews", "pro", "news", "2026-10-06T07:30:00+08:00",
 "https://insuranceasianews.com/el-nino-changes-risk-conversation-as-australian-insurers-scrutinise-bushfire-flood-exposure/",
 "厄爾尼諾改變風險討論：澳洲險企重新審視山火與洪水敞口",
 "厄爾尼諾改變風險討論：澳洲險企重新審視山火與洪水敞口",
 "InsuranceAsia News 10月6日報道：厄爾尼諾現象改變了澳洲的風險討論，當地保險公司正重新審視山火與洪水的風險敞口及再保險安排。 [EN原文]",
 "InsuranceAsia News 10月6日報道：厄爾尼諾現象改變了澳洲的風險討論，當地保險公司正重新審視山火與洪水的風險敞口及再保險安排。 [EN原文]",
 "氣候週期對巨災敞口與再保險定價的影響是區域性議題；對理解保障缺口與再保成本傳導有幫助。",
 "氣候週期對巨災敞口與再保險定價的影響是區域性議題；對理解保障缺口與再保成本傳導有幫助。",
 ("澳洲或跨境物業客戶問及極端天氣風險時，可引述公開報道",
  "澳洲或跨境物業客戶問及極端天氣風險時，可引述公開報道"),
 ("留意氣候風險對核保與再保條款的長期影響", "留意氣候風險對核保與再保條款的長期影響"),
 ("團隊培訓納入氣候風險與保障缺口議題", "團隊培訓納入氣候風險與保障缺口議題"),
 ("跨境資產持有人的物理風險視角", "跨境資產持有人的物理風險視角"),
 (1, 2, 2, 2), ["market"],
 ["climate", "cat-risk", "australia", "reinsurance"],
 ["厄爾尼諾", "澳洲", "山火", "洪水", "氣候風險"],
 "InsuranceAsia News 2026-10-06 報道", "InsuranceAsia News 2026-10-06 報道", "en", 71))

ITEMS.append(mk(
 "insuranceasia-aon-gas-power-programme-20261006", "insuranceasia", "pro", "news", "2026-10-06T05:30:00+08:00",
 "https://insuranceasia.com/insurance/news/aon-launches-insurance-programme-gas-power-projects",
 "Aon 推出燃氣發電項目保險計劃：建設與測試期最高25億美元保障",
 "Aon 推出燃氣發電項目保險計劃：建設與測試期最高25億美元保障",
 "Insurance Asia 10月6日報道：Aon 推出針對燃氣發電項目的保險計劃，開發商在建設與測試階段最高可獲25億美元保障，旨在回應亞洲能源基建項目的風險轉移需求。 [EN原文]",
 "Insurance Asia 10月6日報道：Aon 推出針對燃氣發電項目的保險計劃，開發商在建設與測試階段最高可獲25億美元保障，旨在回應亞洲能源基建項目的風險轉移需求。 [EN原文]",
 "能源與基建項目的保險方案是企業風險管理的高門檻領域；對理解大型項目保險與再保安排有參考價值。",
 "能源與基建項目的保險方案是企業風險管理的高門檻領域；對理解大型項目保險與再保安排有參考價值。",
 ("企業客戶問及項目保險時，引述公開方案並轉介專業團隊",
  "企業客戶問及項目保險時，引述公開方案並轉介專業團隊"),
 ("留意大型項目保險的限額與條款結構", "留意大型項目保險的限額與條款結構"),
 ("納入企業客戶拓展的產業情報", "納入企業客戶拓展的產業情報"),
 ("跨境基建與能源投資的風險安排參考", "跨境基建與能源投資的風險安排參考"),
 (1, 2, 2, 2), ["market", "product"],
 ["energy", "infrastructure", "broking", "apac"],
 ["Aon", "燃氣發電", "項目保險", "基建"],
 "Insurance Asia 2026-10-06 報道", "Insurance Asia 2026-10-06 報道", "en", 72))

ITEMS.append(mk(
 "insuranceasia-india-penetration-life-coverage-20261006", "insuranceasia", "pro", "news", "2026-10-06T05:00:00+08:00",
 "https://insuranceasia.com/insurance/in-focus/india-insurance-growth-fails-widen-life-coverage",
 "印度保險滲透率仍僅佔GDP 3.7%：增長未同步擴闊壽險覆蓋",
 "印度保險滲透率仍僅佔GDP 3.7%：增長未同步擴闊壽險覆蓋",
 "Insurance Asia 10月6日報道：印度保險滲透率維持在GDP約3.7%，約為全球平均的一半，保費增長未能同步擴闊壽險覆蓋；報道聚焦分銷渠道與可負擔性等結構性因素。 [EN原文]",
 "Insurance Asia 10月6日報道：印度保險滲透率維持在GDP約3.7%，約為全球平均的一半，保費增長未能同步擴闊壽險覆蓋；報道聚焦分銷渠道與可負擔性等結構性因素。 [EN原文]",
 "亞洲新興市場的「增長不等於覆蓋」現象，是理解保障缺口與分銷模式的區域對照；對香港市場的直接影響有限。",
 "亞洲新興市場的「增長不等於覆蓋」現象，是理解保障缺口與分銷模式的區域對照；對香港市場的直接影響有限。",
 ("無需主動提及", "無需主動提及"),
 ("區域對標資料存檔", "區域對標資料存檔"),
 ("用於說明保障缺口的區域背景", "用於說明保障缺口的區域背景"),
 ("跨境市場研究的背景資料", "跨境市場研究的背景資料"),
 (0, 1, 2, 1), ["market"],
 ["india", "penetration", "protection-gap", "distribution"],
 ["印度", "保險滲透率", "保障缺口", "壽險覆蓋"],
 "Insurance Asia 2026-10-06 報道", "Insurance Asia 2026-10-06 報道", "en", 71))

ITEMS.append(mk(
 "insuranceasia-mas-family-office-digital-tokens-20261006", "insuranceasia", "pro", "news", "2026-10-06T12:49:00+08:00",
 "https://insuranceasia.com/news/digital-tokens-eye-tax-exempt-status-singapore-reviews-family-office-list",
 "新加坡檢視家族辦公室名單 數字代幣擬享稅務豁免地位",
 "新加坡檢視家族辦公室名單 數字代幣擬享稅務豁免地位",
 "Insurance Asia 10月6日報道：新加坡正檢視其家族辦公室名單與相關激勵安排，同時研究把數字代幣納入稅務豁免範圍；MAS 表示更新後的名單及實施日期將另行公布。 [EN原文]",
 "Insurance Asia 10月6日報道：新加坡正檢視其家族辦公室名單與相關激勵安排，同時研究把數字代幣納入稅務豁免範圍；MAS 表示更新後的名單及實施日期將另行公布。 [EN原文]",
 "新加坡家辦與稅務優惠的每一次調整，都直接影響香港家辦與高客資金流向的比較；適合作為區域競合格局的持續觀察點。",
 "新加坡家辦與稅務優惠的每一次調整，都直接影響香港家辦與高客資金流向的比較；適合作為區域競合格局的持續觀察點。",
 ("高客問及區域落戶比較時，只陳述兩地公開政策，不作推薦",
  "高客問及區域落戶比較時，只陳述兩地公開政策，不作推薦"),
 ("對外引用時註明 MAS 尚未公布實施細節", "對外引用時註明 MAS 尚未公布實施細節"),
 ("把星港家辦政策變化納入長期競爭情報", "把星港家辦政策變化納入長期競爭情報"),
 ("跨境架構討論中作為區域制度比較的背景", "跨境架構討論中作為區域制度比較的背景"),
 (2, 2, 3, 3), ["family", "reg", "market"],
 ["family-office", "singapore", "tax", "digital-assets"],
 ["家族辦公室", "新加坡", "MAS", "數字代幣", "稅務豁免"],
 "Insurance Asia 2026-10-06 報道", "Insurance Asia 2026-10-06 報道", "en", 73))

ITEMS.append(mk(
 "ibm-hdi-global-healthcare-unit-20261006", "insurancebusinessmag", "pro", "news", "2026-10-06T17:06:00+08:00",
 "https://www.insurancebusinessmag.com/asia/news/professional-liability/hdi-global-expands-medical-malpractice-into-global-healthcare-unit-592443.aspx",
 "HDI Global 把醫療責任險擴展為全球醫療保健業務部門",
 "HDI Global 把醫療責任險擴展為全球醫療保健業務部門",
 "Insurance Business 10月6日報道：HDI Global 把醫療責任險（medical malpractice）業務擴展為全球醫療保健業務部門，以統一承接跨市場醫療機構與專業責任風險。 [EN原文]",
 "Insurance Business 10月6日報道：HDI Global 把醫療責任險（medical malpractice）業務擴展為全球醫療保健業務部門，以統一承接跨市場醫療機構與專業責任風險。 [EN原文]",
 "專業責任險的全球化整合，反映醫療與生命科學領域的風險需求上升，屬專業險種供應側的結構變化。",
 "專業責任險的全球化整合，反映醫療與生命科學領域的風險需求上升，屬專業險種供應側的結構變化。",
 ("無需主動提及", "無需主動提及"),
 ("納入專業責任險供應商情報", "納入專業責任險供應商情報"),
 ("團隊拓展醫療與專業客戶時參考", "團隊拓展醫療與專業客戶時參考"),
 ("跨境醫療機構風險安排的供應視角", "跨境醫療機構風險安排的供應視角"),
 (0, 2, 2, 1), ["insurer", "market"],
 ["healthcare", "professional-liability", "global", "medical"],
 ["HDI Global", "醫療責任險", "專業責任", "全球化"],
 "Insurance Business Asia 2026-10-06 報道", "Insurance Business Asia 2026-10-06 報道", "en", 72))

ITEMS.append(mk(
 "ibm-life-sciences-risk-shifting-20261005", "insurancebusinessmag", "pro", "news", "2026-10-05T15:13:00+08:00",
 "https://www.insurancebusinessmag.com/asia/news/breaking-news/life-sciences-risk-is-shifting-and-coverage-may-not-follow-592256.aspx",
 "生命科學風險結構轉變：保障設計未能同步跟上",
 "生命科學風險結構轉變：保障設計未能同步跟上",
 "Insurance Business 10月5日報道：生命科學行業的風險結構正在轉變（涵蓋研發週期、臨床試驗與供應鏈等），但現行保障設計未必同步跟進，出現保障缺口與條款錯配的討論。 [EN原文]",
 "Insurance Business 10月5日報道：生命科學行業的風險結構正在轉變（涵蓋研發週期、臨床試驗與供應鏈等），但現行保障設計未必同步跟進，出現保障缺口與條款錯配的討論。 [EN原文]",
 "新興行業的保障缺口是「風險轉移」思維的典型案例；對企業客戶與專業責任產品的討論有參考價值。",
 "新興行業的保障缺口是「風險轉移」思維的典型案例；對企業客戶與專業責任產品的討論有參考價值。",
 ("企業客戶問及新興行業保障時，說明缺口與核保邏輯",
  "企業客戶問及新興行業保障時，說明缺口與核保邏輯"),
 ("留意專業責任產品的條款與除外責任", "留意專業責任產品的條款與除外責任"),
 ("納入產品設計與缺口分析素材", "納入產品設計與缺口分析素材"),
 ("跨境研發與供應鏈風險的保障視角", "跨境研發與供應鏈風險的保障視角"),
 (1, 2, 2, 2), ["product", "market"],
 ["life-sciences", "protection-gap", "product-design"],
 ["生命科學", "保障缺口", "專業責任", "核保"],
 "Insurance Business Asia 2026-10-05 報道", "Insurance Business Asia 2026-10-05 報道", "en", 71))

ITEMS.append(mk(
 "artemis-catiq-ontario-quebec-storm-491m-20261006", "artemis", "pro", "news", "2026-10-06",
 "https://www.artemis.bm/news/catiq-lifts-ontario-quebec-thunderstorm-insured-market-loss-estimate-12-to-c491m/",
 "CatIQ 上調安大略及魁北克雷暴保險損失估算12%至4.91億加元",
 "CatIQ 上調安大略及魁北克雷暴保險損失估算12%至4.91億加元",
 "Artemis 10月6日報道：CatIQ 把安大略省及魁北克省嚴重雷暴（2026年6月30日至7月3日）的保險市場損失估算上調12%至4.91億加元，反映加拿大次生災害損失持續累積。 [EN原文]",
 "Artemis 10月6日報道：CatIQ 把安大略省及魁北克省嚴重雷暴（2026年6月30日至7月3日）的保險市場損失估算上調12%至4.91億加元，反映加拿大次生災害損失持續累積。 [EN原文]",
 "次生災害（雷暴、暴雨）損失持續上修，是巨災債券與再保定價的重要背景；對理解氣候風險累積有幫助。",
 "次生災害（雷暴、暴雨）損失持續上修，是巨災債券與再保定價的重要背景；對理解氣候風險累積有幫助。",
 ("無需主動提及", "無需主動提及"),
 ("巨災與次生災害資料存檔", "巨災與次生災害資料存檔"),
 ("團隊培訓中作為氣候風險案例", "團隊培訓中作為氣候風險案例"),
 ("跨境物業與資產風險的背景參考", "跨境物業與資產風險的背景參考"),
 (0, 2, 2, 1), ["market"],
 ["cat-risk", "canada", "weather", "ils"],
 ["CatIQ", "加拿大", "雷暴", "巨災損失"],
 "Artemis 2026-10-06 報道", "Artemis 2026-10-06 報道", "en", 71))

ITEMS.append(mk(
 "artemis-visionfund-global-parametrics-amazon-20261006", "artemis", "pro", "news", "2026-10-06",
 "https://www.artemis.bm/news/visionfund-teams-with-global-parametrics-on-two-peril-amazon-basin-parametric-insurance/",
 "VisionFund 與 Global Parametrics 合作推出亞馬遜盆地雙險種參數化保險",
 "VisionFund 與 Global Parametrics 合作推出亞馬遜盆地雙險種參數化保險",
 "Artemis 10月6日報道：VisionFund 與 Global Parametrics 合作，在 InsuResilience Solutions Fund 共同資助下，為玻利維亞、巴西、哥倫比亞等地世界展望會辦事處設計雙險種參數化（meso）保險產品。 [EN原文]",
 "Artemis 10月6日報道：VisionFund 與 Global Parametrics 合作，在 InsuResilience Solutions Fund 共同資助下，為玻利維亞、巴西、哥倫比亞等地世界展望會辦事處設計雙險種參數化（meso）保險產品。 [EN原文]",
 "參數化保險在氣候風險與普惠金融場景的落地案例，展示「無需逐案理賠」的風險轉移思路，是產品創新的參考樣本。",
 "參數化保險在氣候風險與普惠金融場景的落地案例，展示「無需逐案理賠」的風險轉移思路，是產品創新的參考樣本。",
 ("客戶問及參數化保險時，說明其觸發機制與傳統保單差異",
  "客戶問及參數化保險時，說明其觸發機制與傳統保單差異"),
 ("納入產品創新研究素材", "納入產品創新研究素材"),
 ("團隊分享新興風險轉移工具", "團隊分享新興風險轉移工具"),
 ("跨境資產的氣候風險轉移參考", "跨境資產的氣候風險轉移參考"),
 (1, 2, 2, 2), ["product", "market"],
 ["parametric", "climate", "emerging-markets", "inclusion"],
 ["參數化保險", "氣候風險", "VisionFund", "普惠金融"],
 "Artemis 2026-10-06 報道", "Artemis 2026-10-06 報道", "en", 71))

ITEMS.append(mk(
 "artemis-arbol-atzberger-chief-scientist-20261006", "artemis", "pro", "news", "2026-10-06",
 "https://www.artemis.bm/news/arbol-appoints-atzberger-as-chief-scientist-to-lead-new-innovation-unit/",
 "Arbol 委任 Atzberger 為首席科學家 領導新設創新部門",
 "Arbol 委任 Atzberger 為首席科學家 領導新設創新部門",
 "Artemis 10月6日報道：氣候風險轉移與天氣（再）保險企業 Arbol 成立創新部門，由 Dr. Clement Atzberger 出任首席科學家領導。 [EN原文]",
 "Artemis 10月6日報道：氣候風險轉移與天氣（再）保險企業 Arbol 成立創新部門，由 Dr. Clement Atzberger 出任首席科學家領導。 [EN原文]",
 "保險科技在氣候與參數化風險領域持續投入科研人才，反映「保險＋數據科學」的產品化方向。",
 "保險科技在氣候與參數化風險領域持續投入科研人才，反映「保險＋數據科學」的產品化方向。",
 ("無需主動提及", "無需主動提及"),
 ("納入保險科技情報", "納入保險科技情報"),
 ("團隊培訓中作為科技趨勢案例", "團隊培訓中作為科技趨勢案例"),
 ("無直接影響", "無直接影響"),
 (0, 1, 2, 0), ["tech", "market"],
 ["insurtech", "climate", "parametric", "people-moves"],
 ["Arbol", "保險科技", "氣候風險", "首席科學家"],
 "Artemis 2026-10-06 報道", "Artemis 2026-10-06 報道", "en", 70))

ITEMS.append(mk(
 "scmp-planning-legacy-wealth-generations-20261006", "scmp", "media", "report", "2026-10-06T00:00:00+08:00",
 "https://www.scmp.com/presented/business/topics/planning-wealth-generations/article/3369201/planning-legacy-lives-keep-moving",
 "南華早報（特約內容）：為「持續移動的人生」規劃傳承",
 "南華早報（特約內容）：為「持續移動的人生」規劃傳承",
 "南華早報「財富世代規劃」特約專題10月6日刊出，討論跨代傳承規劃在人口流動與家庭結構變化下的安排，聚焦遺產與保障工具的長期視角。屬品牌特約內容，並非新聞報道，引用時宜註明性質。",
 "南華早報「財富世代規劃」特約專題10月6日刊出，討論跨代傳承規劃在人口流動與家庭結構變化下的安排，聚焦遺產與保障工具的長期視角。屬品牌特約內容，並非新聞報道，引用時宜註明性質。",
 "高客傳承話題持續在主流財經媒體獲版面，反映市場對「跨代保障＋架構」的關注；可作為與客戶開啟傳承對話的切入點，但須注意屬特約內容而非編輯部報道。",
 "高客傳承話題持續在主流財經媒體獲版面，反映市場對「跨代保障＋架構」的關注；可作為與客戶開啟傳承對話的切入點，但須注意屬特約內容而非編輯部報道。",
 ("與高客談傳承時，可借此切入「流動性與家族結構變化」的討論",
  "與高客談傳承時，可借此切入「流動性與家族結構變化」的討論"),
 ("對外引用須標明屬特約內容，不作客觀報道的口徑使用",
  "對外引用須標明屬特約內容，不作客觀報道的口徑使用"),
 ("納入高客傳承話題素材庫", "納入高客傳承話題素材庫"),
 ("跨境家族結構變化的討論背景", "跨境家族結構變化的討論背景"),
 (2, 1, 2, 2), ["family"],
 ["wealth-transfer", "legacy", "family-office", "media"],
 ["南華早報", "傳承規劃", "跨代", "財富管理"],
 "南華早報 2026-10-06 特約專題", "南華早報 2026-10-06 特約專題", "en", 62))

ITEMS.append(mk(
 "hk01-hsbc-singapore-ai-centre-hkma-20261006", "hk01", "media", "news", "2026-10-06T11:27:00+08:00",
 "https://global.hk01.com/%E8%B4%A2%E7%BB%8F%E5%BF%AB%E8%AE%AF/60396823/%E6%B1%87%E4%B8%B0ai%E4%B8%AD%E5%BF%83%E9%80%89%E5%9D%80%E6%96%B0%E5%8A%A0%E5%9D%A1-%E4%BC%A0%E9%81%AD%E9%A6%99%E6%B8%AF%E9%87%91%E7%AE%A1%E5%B1%80%E8%B4%A8%E9%97%AE%E6%96%BD%E5%8E%8B-%E9%99%84%E5%9B%9E%E5%BA%94",
 "《金融時報》：滙豐在新加坡設全球AI中心 據報遭金管局質問",
 "《金融時報》：滙豐在新加坡設全球AI中心 據報遭金管局質問",
 "《金融時報》報道（香港01等港媒引述）：滙豐擬於今年下半年在新加坡設立全球人工智能卓越中心、計劃招聘逾100名AI專家，據報金管局曾質問為何不設於香港；金管局回應稱定期與認可機構就各種事宜溝通，不對日常對話或推測性言論發表評論。報道並指金管局曾與滙豐及渣打討論把更多管理層及高級職員設於中國境內。",
 "《金融時報》報道（香港01等港媒引述）：滙豐擬於今年下半年在新加坡設立全球人工智能卓越中心、計劃招聘逾100名AI專家，據報金管局曾質問為何不設於香港；金管局回應稱定期與認可機構就各種事宜溝通，不對日常對話或推測性言論發表評論。報道並指金管局曾與滙豐及渣打討論把更多管理層及高級職員設於中國境內。",
 "反映香港對資源與區域樞紐地位的高度敏感，是「AI＋金融中心競爭」的具體案例；對團隊理解香港政策取向與區域競爭態勢有參考價值。屬媒體報道與消息人士說法，須註明未經官方確認。",
 "反映香港對資源與區域樞紐地位的高度敏感，是「AI＋金融中心競爭」的具體案例；對團隊理解香港政策取向與區域競爭態勢有參考價值。屬媒體報道與消息人士說法，須註明未經官方確認。",
 ("客戶問及香港競爭力時，只引述金管局的官方回應，不引用推測性描述",
  "客戶問及香港競爭力時，只引述金管局的官方回應，不引用推測性描述"),
 ("對外引用須標明為媒體報道、未經官方確認", "對外引用須標明為媒體報道、未經官方確認"),
 ("納入區域競爭與政策取向觀察", "納入區域競爭與政策取向觀察"),
 ("跨境機構落戶比較的背景討論", "跨境機構落戶比較的背景討論"),
 (1, 1, 3, 2), ["tech", "market"],
 ["ai", "hong-kong", "hsbc", "competitiveness"],
 ["滙豐", "人工智能中心", "金管局", "新加坡", "金融時報"],
 "香港01 引述《金融時報》2026-10-06 報道", "香港01 引述《金融時報》2026-10-06 報道", "zh", 66))

path = '/Users/leonliang/maoquanqingbao/data/live-items.json'
d = json.load(open(path, encoding='utf-8'))
ids = {it['id'] for it in d['items']}
added = []
for it in ITEMS:
    if it['id'] in ids:
        print('SKIP dup id:', it['id'])
        continue
    d['items'] = [it] + d['items']
    ids.add(it['id'])
    added.append(it)

n = len(d['items'])
d['meta']['generatedAt'] = NOW
d['meta']['itemCount'] = n
d['meta']['windowNote'] = {"sc": f"本库{n}条。", "tc": f"本庫{n}條。"}
json.dump(d, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'added {len(added)} items, total {n}, generatedAt {NOW}')
for it in added:
    print('  +', it['id'], '|', it['publishedAt'], '|', it['sourceKey'], '|', it['sourceTier'])
