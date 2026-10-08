#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 2026-10-08 23:1x increment (21 items) into live-items.json.

Covers: Artemis (3 new incl. late CatIQ & panel video), IBM Asia (2), InsuranceAsia (5 missed
from 10-08 morning), InsuranceAsia News (6 missed), AIA HK (2 press), AXA HK (1 press),
HKICL/HKMA fake-website alert (1 official), SCMP crash-for-cash (1).
"""
import json
from datetime import datetime, timezone, timedelta

NOW = datetime.now(timezone(timedelta(hours=8))).strftime('%Y-%m-%dT%H:%M:%S+08:00')
CR = {"sc": "本站导读", "tc": "本站導讀"}

ITEMS = []


def mk(id_, sourceKey, tier, kind, pub, url, t, s, w, a_f, a_m, a_l, a_c, ri, boards, themes,
       tags, src, lang, score, verify='pending'):
    return {
        "clusterCount": 1, "score": score, "verifyStatus": verify,
        "sourceTier": tier, "sourceKey": sourceKey, "contentKind": kind,
        "actions": {
            "front": {"sc": a_f[0], "tc": a_f[1]},
            "midback": {"sc": a_m[0], "tc": a_m[1]},
            "lead": {"sc": a_l[0], "tc": a_l[1]},
            "cross": {"sc": a_c[0], "tc": a_c[1]},
        },
        "rolesImpact": {"front": ri[0], "midback": ri[1], "lead": ri[2], "cross": ri[3]},
        "boards": boards, "themes": themes,
        "tags": {"sc": tags, "tc": tags},
        "contentRole": CR, "featured": False, "evergreen": False, "ingestedAt": NOW,
        "id": id_, "publishedAt": pub, "originalUrl": url,
        "title": {"sc": t[0], "tc": t[1]},
        "summary": {"sc": s[0], "tc": s[1]},
        "why": {"sc": w[0], "tc": w[1]},
        "source": {"sc": src[0], "tc": src[1], "lang": lang, "name": src[2],
                   "date": src[3], "note": None},
    }


# ══ 1. Artemis：南安大略強對流風暴 業界損失初估5.63億加元 ════════════════════
ITEMS.append(mk(
 "artemis-southern-ontario-storm-catiq-563m-20261008", "artemis", "pro", "news",
 "2026-10-08T22:30:00+08:00",
 "https://www.artemis.bm/news/southern-ontario-severe-storm-outbreak-industry-loss-initially-estimated-c563m-by-catiq/",
 ("Artemis：南安大略9月強對流風暴 業界損失初估5.63億加元",
  "Artemis：南安大略9月強對流風暴 業界損失初估5.63億加元"),
 ("Artemis 10月8日報道：加拿大保險損失指數機構 CatIQ 初步估計，2026年9月2至3日吹襲南安大略（含多倫多）的強對流風暴，造成約5.63億加元（CAD 563 million）業界保險損失，涵蓋商業及住宅財產與汽車索賠，並已計入額外理賠費用。多倫多屬重災區，出現乒乓球大小冰雹及吹至大型體育場館外牆變形的陣風，暴雨造成的閃電水浸令主要道路封閉。CatIQ 指此為初步數字，未來數週至數月或向上修訂。 [EN原文]",
  "Artemis 10月8日報道：加拿大保險損失指數機構 CatIQ 初步估計，2026年9月2至3日吹襲南安大略（含多倫多）的強對流風暴，造成約5.63億加元（CAD 563 million）業界保險損失，涵蓋商業及住宅財產與汽車索賠，並已計入額外理賠費用。多倫多屬重災區，出現乒乓球大小冰雹及吹至大型體育場館外牆變形的陣風，暴雨造成的閃電水浸令主要道路封閉。CatIQ 指此為初步數字，未來數週至數月或向上修訂。 [EN原文]"),
 ("次生災害（強對流風暴、冰雹、水浸）的業界損失數字是參數式產品與 ILW 觸發的重要參考；城市級別的高價損失事件，亦說明「非巨災」風險同樣可以累積成大額損失。",
  "次生災害（強對流風暴、冰雹、水浸）的業界損失數字是參數式產品與 ILW 觸發的重要參考；城市級別的高價損失事件，亦說明「非巨災」風險同樣可以累積成大額損失。"),
 ("客戶問及自然災害保障時，提醒保額須按重置成本重估，並說明次生災害是否在承保範圍內",
  "客戶問及自然災害保障時，提醒保額須按重置成本重估，並說明次生災害是否在承保範圍內"),
 ("納入巨災與次生災害事件監察", "納入巨災與次生災害事件監察"),
 ("用於說明巨災／次生災害損失的市場量化方法", "用於說明巨災／次生災害損失的市場量化方法"),
 ("北美洲次生災害對全球再保資本的傳導", "北美洲次生災害對全球再保資本的傳導"),
 (1, 2, 2, 2), ["market"], ["catastrophe", "cat-risk", "canada", "industry-loss"],
 ["加拿大", "南安大略", "強對流風暴", "巨災損失"],
 ("Artemis 2026-10-08 報道", "Artemis 2026-10-08 報道", "Artemis", "2026-10-08"), "en", 71, "verified"))

# ══ 2. Artemis：Artemis London 2026 論壇影片 巨災債券紀律 ═══════════════════
ITEMS.append(mk(
 "artemis-london-2026-panel-catbond-discipline-20261008", "artemis", "pro", "speech",
 "2026-10-08T21:00:00+08:00",
 "https://www.artemis.bm/news/from-hard-market-to-normalisation-cat-bond-discipline-in-practice-artemis-london-2026-video/",
 ("Artemis London 2026：從硬市場到正常化 巨災債券「紀律」何價（論壇影片）",
  "Artemis London 2026：從硬市場到正常化 巨災債券「紀律」何價（論壇影片）"),
 ("Artemis 10月8日發布 Artemis London 2026 會議第二場座談影片，主題為「從硬市場到正常化：巨災債券紀律的實踐」。該會議於9月1日舉行，約220名來自120多個機構的代表出席。座談由 Twelve Securis 產品及分銷主管 Nils Ossenbrink 主持，講者包括 Icosa Investments 行政總裁 Florian Steiger、Moody's 風險諮詢高級總監 Charlotte Acton、Elementum Advisors 創辦合夥人 John DeCaro 及 Pool Re 首席核保官 Jonathan Gray。與會者認為，儘管市場倍數（multiple）下降、再保業資金大量流入令價格走軟，結構性紀律仍屬穩固；真正的紀律需要嚴謹風險評估與穩健建模，尤其針對山火、恐怖主義等次生災害；並就發行過程的價格發現透明度（認購超額、息差多次收窄）展開討論。 [EN原文]",
  "Artemis 10月8日發布 Artemis London 2026 會議第二場座談影片，主題為「從硬市場到正常化：巨災債券紀律的實踐」。該會議於9月1日舉行，約220名來自120多個機構的代表出席。座談由 Twelve Securis 產品及分銷主管 Nils Ossenbrink 主持，講者包括 Icosa Investments 行政總裁 Florian Steiger、Moody's 風險諮詢高級總監 Charlotte Acton、Elementum Advisors 創辦合夥人 John DeCaro 及 Pool Re 首席核保官 Jonathan Gray。與會者認為，儘管市場倍數（multiple）下降、再保業資金大量流入令價格走軟，結構性紀律仍屬穩固；真正的紀律需要嚴謹風險評估與穩健建模，尤其針對山火、恐怖主義等次生災害；並就發行過程的價格發現透明度（認購超額、息差多次收窄）展開討論。 [EN原文]"),
 ("業界對「價格走軟但紀律仍在」的共識，是理解當前再保與 ILS 週期的關鍵定性判斷；本條可與同日 Plenum 息差、TWIA 需求預測等量化材料並讀。",
  "業界對「價格走軟但紀律仍在」的共識，是理解當前再保與 ILS 週期的關鍵定性判斷；本條可與同日 Plenum 息差、TWIA 需求預測等量化材料並讀。"),
 ("引用業界觀點時標明屬論壇發言，不代表市場共識", "引用業界觀點時標明屬論壇發言，不代表市場共識"),
 ("納入再保週期與承保紀律情報", "納入再保週期與承保紀律情報"),
 ("團隊理解再保定價邏輯的定性素材", "團隊理解再保定價邏輯的定性素材"),
 ("國際再保資本週期對區域定價的傳導", "國際再保資本週期對區域定價的傳導"),
 (1, 2, 2, 2), ["market", "ils"], ["ils", "catastrophe-bond", "pricing", "discipline"],
 ["巨災債券", "Artemis London", "再保週期", "風險紀律"],
 ("Artemis 2026-10-08 報道", "Artemis 2026-10-08 報道", "Artemis", "2026-10-08"), "en", 70, "verified"))

# ══ 3. Artemis：Reask 為 ForecastEx 活躍颶風合約提供結算數據 ═══════════════
ITEMS.append(mk(
 "artemis-reask-forecastex-live-hurricane-contracts-20261008", "artemis", "pro", "news",
 "2026-10-08T18:30:00+08:00",
 "https://www.artemis.bm/news/reask-to-provide-settlement-data-for-interactive-brokers-forecastex-live-hurricane-contracts/",
 ("Artemis：Reask 為盈透證券 ForecastEx「活躍颶風合約」提供結算數據",
  "Artemis：Reask 為盈透證券 ForecastEx「活躍颶風合約」提供結算數據"),
 ("Artemis 10月8日報道：盈透證券（Interactive Brokers）旗下預測市場平台 ForecastEx 與巨災模型及氣候分析公司 Reask 合作，由 Reask 為其新上市的「活躍颶風合約」（live hurricane contracts）提供結算數據，並以 Reask 的 LiveCyc 預報作為公允市值參考（每6小時更新）。合約覆蓋美國墨西哥灣及大西洋沿岸、加勒比、墨西哥、中美洲及南美北部共163個沿海地點，每個結算範圍半徑10公里、以1公里解析度評估；當某地點預測陣風達70英里／小時以上的概率超過約5%時掛牌，並以70至200英里、每10英里一級的階梯交易，風暴消散後數日內結算。Reask 稱此舉把以往雙邊議價、缺乏公開價格的 ILW 與短年期轉分保風險，變成交易所持續定價的工具；熱帶風暴 Isaias 或成首個交易案例。 [EN原文]",
  "Artemis 10月8日報道：盈透證券（Interactive Brokers）旗下預測市場平台 ForecastEx 與巨災模型及氣候分析公司 Reask 合作，由 Reask 為其新上市的「活躍颶風合約」（live hurricane contracts）提供結算數據，並以 Reask 的 LiveCyc 預報作為公允市值參考（每6小時更新）。合約覆蓋美國墨西哥灣及大西洋沿岸、加勒比、墨西哥、中美洲及南美北部共163個沿海地點，每個結算範圍半徑10公里、以1公里解析度評估；當某地點預測陣風達70英里／小時以上的概率超過約5%時掛牌，並以70至200英里、每10英里一級的階梯交易，風暴消散後數日內結算。Reask 稱此舉把以往雙邊議價、缺乏公開價格的 ILW 與短年期轉分保風險，變成交易所持續定價的工具；熱帶風暴 Isaias 或成首個交易案例。 [EN原文]"),
 ("交易所化的活躍颶風合約為巨災風險提供公開價格訊號，日後或成為雙邊報價的基準，並改善 ILS 基金在無巨災期間的估值參考，屬風險轉移基建的結構性發展。",
  "交易所化的活躍颶風合約為巨災風險提供公開價格訊號，日後或成為雙邊報價的基準，並改善 ILS 基金在無巨災期間的估值參考，屬風險轉移基建的結構性發展。"),
 ("涉及另類風險轉移工具時只作架構說明，不涉及任何投資建議", "涉及另類風險轉移工具時只作架構說明，不涉及任何投資建議"),
 ("納入ILS與風險轉移基建情報", "納入ILS與風險轉移基建情報"),
 ("用於說明巨災風險的價格發現機制演變", "用於說明巨災風險的價格發現機制演變"),
 ("跨境巨災風險轉移工具的創新參照", "跨境巨災風險轉移工具的創新參照"),
 (1, 2, 2, 2), ["market", "ils"], ["ils", "catastrophe", "parametric", "innovation"],
 ["Reask", "ForecastEx", "颶風合約", "參數保險"],
 ("Artemis 2026-10-08 報道", "Artemis 2026-10-08 報道", "Artemis", "2026-10-08"), "en", 73, "verified"))

# ══ 4. IBM：韓國 AI 驅動銀行入侵 突顯網安保險缺口 ═════════════════════════
ITEMS.append(mk(
 "ibm-south-korea-ai-bank-hacks-cyber-gaps-20261008", "insurancebusinessmag", "pro", "news",
 "2026-10-08T22:45:00+08:00",
 "https://www.insurancebusinessmag.com/asia/news/cyber/aipowered-bank-hacks-in-south-korea-put-cyber-insurance-gaps-under-scrutiny-592835.aspx",
 ("Insurance Business：韓國銀行遭AI驅動黑客攻擊 網安保險缺口受質疑",
  "Insurance Business：韓國銀行遭AI驅動黑客攻擊 網安保險缺口受質疑"),
 ("Insurance Business Asia 10月8日報道：韓國七間金融機構遭連環網絡攻擊，當局正調查是否涉及AI黑客工具；受影響包括新韓銀行、KB國民銀行、Hana銀行、BNK釜山銀行、Welcome儲蓄銀行、Yegaram儲蓄銀行及現代資本，友利銀行與NH農協銀行偵測到入侵企圖但未失守。Yegaram約4萬筆客戶紀錄外洩、新韓約2.5萬筆；被盜資料包括姓名、電話、居民登記號碼、貸款申請資料及信用額度。七間機構發現同一攻擊者IP，並在系統中找到中國開發的AI滲透測試平台「Artex」痕跡（未經韓方確認）。偵測速度偏慢：新韓約15小時、Hana約42小時、KB國民約68小時。金融服務委員會（FSC）召開緊急會議，要求非業務必需即封鎖外部存取；金融監督院（FSS）向約500間金融機構通報惡意IP，涉12個國家及地區約30個IP。報道引述 Howden 上半年網絡報告指「網安保費創新低、網安風險卻創新高」；Delinea 2025年11月調查顯示42%受訪保安主管稱其網安保單明確排除AI誤用或責任。金管局2026年6月致函銀行，指前沿AI模型或令全球網絡風險出現躍變，並公布新的網絡韌性測試框架。 [EN原文]",
  "Insurance Business Asia 10月8日報道：韓國七間金融機構遭連環網絡攻擊，當局正調查是否涉及AI黑客工具；受影響包括新韓銀行、KB國民銀行、Hana銀行、BNK釜山銀行、Welcome儲蓄銀行、Yegaram儲蓄銀行及現代資本，友利銀行與NH農協銀行偵測到入侵企圖但未失守。Yegaram約4萬筆客戶紀錄外洩、新韓約2.5萬筆；被盜資料包括姓名、電話、居民登記號碼、貸款申請資料及信用額度。七間機構發現同一攻擊者IP，並在系統中找到中國開發的AI滲透測試平台「Artex」痕跡（未經韓方確認）。偵測速度偏慢：新韓約15小時、Hana約42小時、KB國民約68小時。金融服務委員會（FSC）召開緊急會議，要求非業務必需即封鎖外部存取；金融監督院（FSS）向約500間金融機構通報惡意IP，涉12個國家及地區約30個IP。報道引述 Howden 上半年網絡報告指「網安保費創新低、網安風險卻創新高」；Delinea 2025年11月調查顯示42%受訪保安主管稱其網安保單明確排除AI誤用或責任。金管局2026年6月致函銀行，指前沿AI模型或令全球網絡風險出現躍變，並公布新的網絡韌性測試框架。 [EN原文]"),
 ("若以AI自主探測、選擇攻擊手法的攻擊成為常態，現行網安保單的「人為威脅者」假設便可能出現承保空隙；香港監管已就前沿AI網絡風險發函銀行，屬本地客戶網安保障檢視的直接背景。",
  "若以AI自主探測、選擇攻擊手法的攻擊成為常態，現行網安保單的「人為威脅者」假設便可能出現承保空隙；香港監管已就前沿AI網絡風險發函銀行，屬本地客戶網安保障檢視的直接背景。"),
 ("與企業客戶討論網安保障時，重點核對保單是否涵蓋AI驅動攻擊、第三方系統事故及業務中斷",
  "與企業客戶討論網安保障時，重點核對保單是否涵蓋AI驅動攻擊、第三方系統事故及業務中斷"),
 ("納入網安風險與保單條款缺口研究", "納入網安風險與保單條款缺口研究"),
 ("用於說明新興科技風險如何改寫承保假設", "用於說明新興科技風險如何改寫承保假設"),
 ("金管局前沿AI網絡風險函件與跨境客戶的合規提示", "金管局前沿AI網絡風險函件與跨境客戶的合規提示"),
 (2, 3, 3, 2), ["reg", "tech", "market"], ["cyber", "ai", "enforcement", "apac", "hong-kong"],
 ["韓國", "網絡保險", "AI攻擊", "保單缺口"],
 ("Insurance Business Asia 2026-10-08 報道", "Insurance Business Asia 2026-10-08 報道",
  "Insurance Business Asia", "2026-10-08"), "en", 74, "verified"))

# ══ 5. IBM：WTW 第三季併購表現監察 交易更快更大但落後大市 ═══════════════
ITEMS.append(mk(
 "ibm-wtw-q3-deal-performance-monitor-20261008", "insurancebusinessmag", "pro", "report",
 "2026-10-08T18:24:00+08:00",
 "https://www.insurancebusinessmag.com/asia/news/mergers-acquisitions/dealmakers-are-moving-faster-and-bigger-yet-underperforming-wtw-says-592814.aspx",
 ("Insurance Business：WTW 第三季併購表現監察 交易更快更大 收購方卻普遍落後大市",
  "Insurance Business：WTW 第三季併購表現監察 交易更快更大 收購方卻普遍落後大市"),
 ("Insurance Business Asia 10月8日報道（引述 WTW 與 Bayes Business School 併購研究中心合編的《季度交易表現監察》）：2026年第三季有九宗價值逾100億美元的超大型交易完成，帶動年初至今完成24宗，為 WTW 紀錄中九個月最高；期內交易總值按年升23.9%。但收購方第三季表現落後 MSCI 世界指數10.3個百分點，連續兩季落後，200宗交易中121宗（60.5%）跑輸指數；區域上亞太收購方落後18.7個百分點（表現最差），北美落後13.8個百分點，歐洲落後5.0個百分點（成交量連續四季下滑），英國為唯一例外；中國買家交易由第二季7宗躍升至第三季21宗。交易節奏加快：70日內完成的「快速交易」佔比由35%升至43%，跨行業交易由25%升至35%。WTW 歐洲併購諮詢主管 Jana Mercereau 提醒速度不應犧牲嚴謹盡職調查。報道並引 RPC Legal 年度保險回顧指，2025年延續至2026年的保證與賠償（W&I）保險索賠活動持續增加，美國及歐洲、中東與非洲市場均出現逾1,000萬美元的大額索賠。 [EN原文]",
  "Insurance Business Asia 10月8日報道（引述 WTW 與 Bayes Business School 併購研究中心合編的《季度交易表現監察》）：2026年第三季有九宗價值逾100億美元的超大型交易完成，帶動年初至今完成24宗，為 WTW 紀錄中九個月最高；期內交易總值按年升23.9%。但收購方第三季表現落後 MSCI 世界指數10.3個百分點，連續兩季落後，200宗交易中121宗（60.5%）跑輸指數；區域上亞太收購方落後18.7個百分點（表現最差），北美落後13.8個百分點，歐洲落後5.0個百分點（成交量連續四季下滑），英國為唯一例外；中國買家交易由第二季7宗躍升至第三季21宗。交易節奏加快：70日內完成的「快速交易」佔比由35%升至43%，跨行業交易由25%升至35%。WTW 歐洲併購諮詢主管 Jana Mercereau 提醒速度不應犧牲嚴謹盡職調查。報道並引 RPC Legal 年度保險回顧指，2025年延續至2026年的保證與賠償（W&I）保險索賠活動持續增加，美國及歐洲、中東與非洲市場均出現逾1,000萬美元的大額索賠。 [EN原文]"),
 ("W&I 保險索賠上升與交易節奏加快同時出現，正是交易風險轉移需求的前瞻指標；亞太收購方表現最差，亦為本地企業併購保險安排提供討論切入點。",
  "W&I 保險索賠上升與交易節奏加快同時出現，正是交易風險轉移需求的前瞻指標；亞太收購方表現最差，亦為本地企業併購保險安排提供討論切入點。"),
 ("企業客戶進行併購時，可把保證與賠償保險納入交易風險討論，不引述未經核實的索賠個案",
  "企業客戶進行併購時，可把保證與賠償保險納入交易風險討論，不引述未經核實的索賠個案"),
 ("納入併購與交易責任險情報", "納入併購與交易責任險情報"),
 ("用於說明交易活躍度與專業保險需求的關係", "用於說明交易活躍度與專業保險需求的關係"),
 ("亞太企業跨境併購的風險轉移需求背景", "亞太企業跨境併購的風險轉移需求背景"),
 (1, 2, 2, 2), ["market", "product"], ["m&a", "warranty-insurance", "apac", "due-diligence"],
 ["WTW", "併購", "W&I保險", "亞太"],
 ("Insurance Business Asia 2026-10-08 報道", "Insurance Business Asia 2026-10-08 報道",
  "Insurance Business Asia", "2026-10-08"), "en", 72, "verified"))

# ══ 6. Insurance Asia：宏利32億美元長期護理再保交易完成 ══════════════════
ITEMS.append(mk(
 "iaasia-manulife-3-2b-ltc-reinsurance-closed-20261008", "insuranceasia", "pro", "news",
 "2026-10-08T05:30:00+08:00",
 "https://insuranceasia.com/insurance/news/manulife-cuts-risk-32b-reinsurance-deal-closes",
 ("Insurance Asia：宏利完成32億美元長期護理再保交易 累計降低長護發病率敏感度24%",
  "Insurance Asia：宏利完成32億美元長期護理再保交易 累計降低長護發病率敏感度24%"),
 ("Insurance Asia 10月8日報道：宏利金融（Manulife）已完成向慕尼黑再保險旗下 Munich American Reassurance Company 再保32億美元長期護理（LTC）保單準備金的交易，該交易於2026年8月5日首次公布，全面轉移長期護理組合的生物特徵（biometric）風險。連同過往再保交易，宏利累計已降低長期護理發病率敏感度24%。交易採5%負分出（negative 5% cede），與該公司過往交易定價一致，對整體資本大致中性；對核心盈利及股東應佔淨收入的年度影響不重大，估計首年約3,000萬美元，並隨時間遞減。 [EN原文]",
  "Insurance Asia 10月8日報道：宏利金融（Manulife）已完成向慕尼黑再保險旗下 Munich American Reassurance Company 再保32億美元長期護理（LTC）保單準備金的交易，該交易於2026年8月5日首次公布，全面轉移長期護理組合的生物特徵（biometric）風險。連同過往再保交易，宏利累計已降低長期護理發病率敏感度24%。交易採5%負分出（negative 5% cede），與該公司過往交易定價一致，對整體資本大致中性；對核心盈利及股東應佔淨收入的年度影響不重大，估計首年約3,000萬美元，並隨時間遞減。 [EN原文]"),
 ("大型壽險公司持續以再保剝離長壽與長護風險，會影響其在亞洲（含香港）新產品與承保胃納的配置；此類交易的定價與資本影響，是觀察集團資本策略的現成案例。",
  "大型壽險公司持續以再保剝離長壽與長護風險，會影響其在亞洲（含香港）新產品與承保胃納的配置；此類交易的定價與資本影響，是觀察集團資本策略的現成案例。"),
 ("客戶問及保司財務穩健時，引述其公開披露的風險轉移安排，不作投資建議",
  "客戶問及保司財務穩健時，引述其公開披露的風險轉移安排，不作投資建議"),
 ("納入保司資本與再保動態情報", "納入保司資本與再保動態情報"),
 ("用於說明壽險長壽風險的再保處置手法", "用於說明壽險長壽風險的再保處置手法"),
 ("跨境壽險集團資本策略的觀察點", "跨境壽險集團資本策略的觀察點"),
 (1, 2, 2, 2), ["insurer", "market"], ["reinsurance", "long-term-care", "capital", "m&a"],
 ["宏利", "慕尼黑再保險", "長期護理", "風險轉移"],
 ("Insurance Asia 2026-10-08 報道", "Insurance Asia 2026-10-08 報道", "Insurance Asia", "2026-10-08"),
 "en", 75, "verified"))

# ══ 7. Insurance Asia：保誠新加坡推家庭照顧者人壽計劃 ════════════════════
ITEMS.append(mk(
 "iaasia-prudential-sg-pruactive-family-care-20261008", "insuranceasia", "pro", "news",
 "2026-10-08T05:45:00+08:00",
 "https://insuranceasia.com/insurance/news/prudential-plan-eases-protection-gap-caregivers",
 ("Insurance Asia：保誠新加坡推「PRUActive Family Care」 一張保單同時保障子女與年邁父母",
  "Insurance Asia：保誠新加坡推「PRUActive Family Care」 一張保單同時保障子女與年邁父母"),
 ("Insurance Asia 10月8日報道：保誠新加坡推出終身保障計劃「PRUActive Family Care」（PAFC），讓照顧者以一張保單同時為子女及年邁父母提供保障。子女作為受保人獲終身保障，涵蓋死亡、末期疾病及完全永久傷殘；計劃提供嚴重疾病附加保障，覆蓋182項疾病，包括兒童疾病及精神疾病；父母一方則可保障至100歲且毋須醫療核保，涵蓋阿茲海默症、認知障礙症、柏金遜症及進行性核上性麻痺等指定年齡相關疾病。保誠指新加坡2026年65歲及以上公民已超過人口五分之一，預期2035年每四人多於一人為65歲以上，照顧者人數將持續增加。 [EN原文]",
  "Insurance Asia 10月8日報道：保誠新加坡推出終身保障計劃「PRUActive Family Care」（PAFC），讓照顧者以一張保單同時為子女及年邁父母提供保障。子女作為受保人獲終身保障，涵蓋死亡、末期疾病及完全永久傷殘；計劃提供嚴重疾病附加保障，覆蓋182項疾病，包括兒童疾病及精神疾病；父母一方則可保障至100歲且毋須醫療核保，涵蓋阿茲海默症、認知障礙症、柏金遜症及進行性核上性麻痺等指定年齡相關疾病。保誠指新加坡2026年65歲及以上公民已超過人口五分之一，預期2035年每四人多於一人為65歲以上，照顧者人數將持續增加。 [EN原文]"),
 ("「照顧者缺口」正成為亞洲壽險產品設計的新敘事：以單一保單串連兩代保障，回應高齡社會的實際資金與照顧壓力，是觀察同業產品走向的具體案例。",
  "「照顧者缺口」正成為亞洲壽險產品設計的新敘事：以單一保單串連兩代保障，回應高齡社會的實際資金與照顧壓力，是觀察同業產品走向的具體案例。"),
 ("介紹長者保障時，只作功能與條款說明，不比較保費或暗示回報",
  "介紹長者保障時，只作功能與條款說明，不比較保費或暗示回報"),
 ("納入產品設計與保障缺口情報", "納入產品設計與保障缺口情報"),
 ("用於說明高齡化下保障需求的結構轉變", "用於說明高齡化下保障需求的結構轉變"),
 ("亞洲高齡社會的兩代保障需求參照", "亞洲高齡社會的兩代保障需求參照"),
 (2, 2, 2, 2), ["product", "market"], ["product", "protection-gap", "ageing", "critical-illness"],
 ["保誠新加坡", "家庭保障", "長者保障", "認知障礙"],
 ("Insurance Asia 2026-10-08 報道", "Insurance Asia 2026-10-08 報道", "Insurance Asia", "2026-10-08"),
 "en", 73, "verified"))

# ══ 8. Insurance Asia：全球保險科技融資24.4億美元 AI 佔99% ═══════════════
ITEMS.append(mk(
 "iaasia-insurtech-funding-2-44b-q2-ai-gallagher-re-20261008", "insuranceasia", "pro", "report",
 "2026-10-08T06:00:00+08:00",
 "https://insuranceasia.com/insurance/news/insurtech-funding-hits-24b-ai-dominates-deals",
 ("Insurance Asia：全球保險科技融資回升至24.4億美元 AI 公司佔99.1%",
  "Insurance Asia：全球保險科技融資回升至24.4億美元 AI 公司佔99.1%"),
 ("Insurance Asia 10月8日報道（引述 Gallagher Re 保險科技報告）：2026年第二季全球保險科技融資達24.4億美元，為2022年第二季以來最高，其中AI相關公司吸納99.1%（24.2億美元），所有逾500萬美元的交易均由AI公司取得。該報告為三部分AI系列的最後一份，2026年版本聚焦支撐AI的基礎設施所帶來的長期風險與機遇，重點包括數據中心：AI工作量增長推高伺服器、儲存及網絡設備需求，興建速度與AI硬體成本及複雜度正對核保構成壓力，同時為有意進場的保險及再保公司創造機會。期內早期階段融資按季大跌51.8%（由5.48億美元降至2.6419億美元），但早期交易宗數維持54宗；保險及再保公司期內作出27項科技投資（首季為32項），其中51.9%投向早期公司。Gallagher Re 指融資回升同時反映創新管道可能收窄，尤其是傳統保險公司。 [EN原文]",
  "Insurance Asia 10月8日報道（引述 Gallagher Re 保險科技報告）：2026年第二季全球保險科技融資達24.4億美元，為2022年第二季以來最高，其中AI相關公司吸納99.1%（24.2億美元），所有逾500萬美元的交易均由AI公司取得。該報告為三部分AI系列的最後一份，2026年版本聚焦支撐AI的基礎設施所帶來的長期風險與機遇，重點包括數據中心：AI工作量增長推高伺服器、儲存及網絡設備需求，興建速度與AI硬體成本及複雜度正對核保構成壓力，同時為有意進場的保險及再保公司創造機會。期內早期階段融資按季大跌51.8%（由5.48億美元降至2.6419億美元），但早期交易宗數維持54宗；保險及再保公司期內作出27項科技投資（首季為32項），其中51.9%投向早期公司。Gallagher Re 指融資回升同時反映創新管道可能收窄，尤其是傳統保險公司。 [EN原文]"),
 ("資金幾乎全數流向AI賽道，而AI基建（尤其數據中心）正被視為新興承保風險與機遇的交匯點；對關注科技風險與保險產品創新的人而言，這是資金與風險同步位移的清晰信號。",
  "資金幾乎全數流向AI賽道，而AI基建（尤其數據中心）正被視為新興承保風險與機遇的交匯點；對關注科技風險與保險產品創新的人而言，這是資金與風險同步位移的清晰信號。"),
 ("引用融資數據時標明來源與統計季度，不引伸為任何投資建議",
  "引用融資數據時標明來源與統計季度，不引伸為任何投資建議"),
 ("納入保險科技與AI資本情報", "納入保險科技與AI資本情報"),
 ("用於說明AI如何重塑保險價值鏈投資方向", "用於說明AI如何重塑保險價值鏈投資方向"),
 ("跨境科技風險與新型保障需求的背景", "跨境科技風險與新型保障需求的背景"),
 (1, 2, 2, 2), ["tech", "market"], ["insurtech", "ai", "datacentre", "funding"],
 ["保險科技", "融資", "AI", "數據中心"],
 ("Insurance Asia 2026-10-08 報道", "Insurance Asia 2026-10-08 報道", "Insurance Asia", "2026-10-08"),
 "en", 72, "verified"))

# ══ 9. Insurance Asia：AIA 中國銀保市佔下滑 上半年銷售跌6% ═══════════════
ITEMS.append(mk(
 "iaasia-aia-china-bancassurance-share-jefferies-20261008", "insuranceasia", "pro", "news",
 "2026-10-08T05:15:00+08:00",
 "https://insuranceasia.com/insurance/news/aia-loses-china-bancassurance-share-sales-fall-6",
 ("Insurance Asia：AIA 中國銀保銷售上半年跌6% 市佔明顯流失（Jefferies 分析）",
  "Insurance Asia：AIA 中國銀保銷售上半年跌6% 市佔明顯流失（Jefferies 分析）"),
 ("Insurance Asia 10月8日報道（引述 Jefferies）：友邦（AIA）2026年上半年中國銀保渠道銷售按年下跌6%，同期整體市場卻增長，導致其市佔明顯流失；Jefferies 指 AIA 第二季表現疲弱、第三季亦可能疲弱。中國於2026年7月生效的新費用及佣金改革，擴大保險公司向銀行披露佣金的要求，並須於產品報備中申報銀保銷售人員的報酬資料，以確保佣金支付在監管上限內、避免披露安排以外的額外支付；改革前部分市場出現提前銷售，第二季銷售急升後大幅回落。Jefferies 估計中國銀保約佔 AIA 中國新業務價值（VONB）15%；若改革後行業銷售下跌50%，AIA 中國銷售將減少約7%；由於 AIA 中國上半年佔集團 VONB 29%，影響或折算為集團增長約2.1個百分點。該行預期 AIA 市佔自2027年起回升，2027年第二季比較基數亦較有利。 [EN原文]",
  "Insurance Asia 10月8日報道（引述 Jefferies）：友邦（AIA）2026年上半年中國銀保渠道銷售按年下跌6%，同期整體市場卻增長，導致其市佔明顯流失；Jefferies 指 AIA 第二季表現疲弱、第三季亦可能疲弱。中國於2026年7月生效的新費用及佣金改革，擴大保險公司向銀行披露佣金的要求，並須於產品報備中申報銀保銷售人員的報酬資料，以確保佣金支付在監管上限內、避免披露安排以外的額外支付；改革前部分市場出現提前銷售，第二季銷售急升後大幅回落。Jefferies 估計中國銀保約佔 AIA 中國新業務價值（VONB）15%；若改革後行業銷售下跌50%，AIA 中國銷售將減少約7%；由於 AIA 中國上半年佔集團 VONB 29%，影響或折算為集團增長約2.1個百分點。該行預期 AIA 市佔自2027年起回升，2027年第二季比較基數亦較有利。 [EN原文]"),
 ("內地銀保佣金改革直接改變分銷經濟；對香港市場而言，這是理解跨境客戶來源、內地渠道行為變化及集團策略重心的重要背景，而非可直接比較的銷售數據。",
  "內地銀保佣金改革直接改變分銷經濟；對香港市場而言，這是理解跨境客戶來源、內地渠道行為變化及集團策略重心的重要背景，而非可直接比較的銷售數據。"),
 ("引用券商分析時標明屬第三方估算，不作為同業比較的結論",
  "引用券商分析時標明屬第三方估算，不作為同業比較的結論"),
 ("納入分銷渠道與監管改革情報", "納入分銷渠道與監管改革情報"),
 ("用於說明佣金監管如何影響渠道行為", "用於說明佣金監管如何影響渠道行為"),
 ("內地客戶來源與跨境銷售合規的觀察點", "內地客戶來源與跨境銷售合規的觀察點"),
 (1, 2, 3, 2), ["market", "reg"], ["bancassurance", "commission", "china", "distribution"],
 ["友邦", "中國銀保", "佣金改革", "市場份額"],
 ("Insurance Asia 2026-10-08 報道", "Insurance Asia 2026-10-08 報道", "Insurance Asia", "2026-10-08"),
 "en", 73, "pending"))

# ══ 10. Insurance Asia：亞洲責任險索賠成本上升（Marsh Re） ══════════════
ITEMS.append(mk(
 "iaasia-asia-casualty-claims-cost-marsh-re-20261008", "insuranceasia", "pro", "report",
 "2026-10-08T05:00:00+08:00",
 "https://insuranceasia.com/insurance/in-focus/asia-casualty-insurers-face-rising-claims-costs",
 ("Insurance Asia 專題：亞洲責任險保費佔GDP僅0.1% 索賠成本上升與長尾結案成挑戰",
  "Insurance Asia 專題：亞洲責任險保費佔GDP僅0.1% 索賠成本上升與長尾結案成挑戰"),
 ("Insurance Asia 10月8日刊出專題（引述 Marsh Re 9月報告，不含汽車險）：亞洲一般責任險（casualty）毛保費平均僅約GDP的0.1%，遠低於美國約0.5%，顯示市場仍有滲透空間；中國約198億美元、佔亞洲約七成。業務分為一般責任、勞工補償／僱主責任及金融專業責任。亞洲賠付率普遍低於55%，但韓國及印度超過60%。報告指責任險索賠結案需時4至8年，部分長達20年以上，令最終成本與準備金確定困難，尤其在通脹及損失趨勢變化時；索賠頻率大致平穩或微升，但單宗成本因人工、材料及醫療費用上升而增加。亞洲暫未見美國式訴訟成本急升，但在美設有營運、出口、董事及高管責任或產品銷售的亞洲企業仍可能面對更高和解與陪審團裁決。儘管成本上升，亞洲大部分市場一般責任及金融專業責任費率仍因承保能力充裕與競爭而下跌。報告亦列舉歷史大額個案（高田安全氣囊、三星手機電池、武田 Actos 糖尿病藥各逾10億美元），並點出AI、電動車電池、PFAS、氣候責任、網絡實體風險及微塑膠等新興風險；Marsh Re 的 Vista 平台已涵蓋逾300個情境。 [EN原文]",
  "Insurance Asia 10月8日刊出專題（引述 Marsh Re 9月報告，不含汽車險）：亞洲一般責任險（casualty）毛保費平均僅約GDP的0.1%，遠低於美國約0.5%，顯示市場仍有滲透空間；中國約198億美元、佔亞洲約七成。業務分為一般責任、勞工補償／僱主責任及金融專業責任。亞洲賠付率普遍低於55%，但韓國及印度超過60%。報告指責任險索賠結案需時4至8年，部分長達20年以上，令最終成本與準備金確定困難，尤其在通脹及損失趨勢變化時；索賠頻率大致平穩或微升，但單宗成本因人工、材料及醫療費用上升而增加。亞洲暫未見美國式訴訟成本急升，但在美設有營運、出口、董事及高管責任或產品銷售的亞洲企業仍可能面對更高和解與陪審團裁決。儘管成本上升，亞洲大部分市場一般責任及金融專業責任費率仍因承保能力充裕與競爭而下跌。報告亦列舉歷史大額個案（高田安全氣囊、三星手機電池、武田 Actos 糖尿病藥各逾10億美元），並點出AI、電動車電池、PFAS、氣候責任、網絡實體風險及微塑膠等新興風險；Marsh Re 的 Vista 平台已涵蓋逾300個情境。 [EN原文]"),
 ("長尾責任險的準備金不確定性與新興責任風險，是企業風險管理中經常被低估的部分；對有美國業務敞口的客戶，費率走軟期間的保障範圍檢視尤其重要。",
  "長尾責任險的準備金不確定性與新興責任風險，是企業風險管理中經常被低估的部分；對有美國業務敞口的客戶，費率走軟期間的保障範圍檢視尤其重要。"),
 ("企業客戶續保時，重點檢視產品責任、董責險及美國敞口的承保範圍與限額",
  "企業客戶續保時，重點檢視產品責任、董責險及美國敞口的承保範圍與限額"),
 ("納入責任險與新興風險情報庫", "納入責任險與新興風險情報庫"),
 ("用於說明長尾責任風險的結構性挑戰", "用於說明長尾責任風險的結構性挑戰"),
 ("跨境企業在美訴訟敞口的保障提醒", "跨境企業在美訴訟敞口的保障提醒"),
 (2, 3, 2, 2), ["market", "product"], ["casualty", "claims", "liability", "apac", "protection-gap"],
 ["亞洲", "責任險", "索賠成本", "Marsh Re"],
 ("Insurance Asia 2026-10-08 報道", "Insurance Asia 2026-10-08 報道", "Insurance Asia", "2026-10-08"),
 "en", 74, "verified"))

# ══ 11. InsuranceAsia News：MS Amlin 洽推新加坡側車 目標4,000-5,000萬美元 ══
ITEMS.append(mk(
 "ian-ms-amlin-singapore-sidecar-40-50m-20261008", "insuranceasianews", "pro", "news",
 "2026-10-08T07:30:00+08:00",
 "https://insuranceasianews.com/ms-amlin-seeks-investors-for-new-singapore-domiciled-sidecar-eyes-untapped-potential/",
 ("InsuranceAsia News：MS Amlin 洽推新加坡註冊側車 初步目標4,000至5,000萬美元",
  "InsuranceAsia News：MS Amlin 洽推新加坡註冊側車 初步目標4,000至5,000萬美元"),
 ("InsuranceAsia News 10月8日報道：勞合社再保人 MS Amlin 正與投資者洽談，擬推出新加坡註冊的第三方資本工具（側車），初步目標規模約4,000至5,000萬美元；亞太區行政總裁 William Ho 表示，新工具將延續 Phoenix Re 特殊目的再保工具（SPRV）的成功經驗，並看好區內尚未開發的潛力。報道屬訂閱內容，摘要依據公開導語與標題整理。 [EN原文]",
  "InsuranceAsia News 10月8日報道：勞合社再保人 MS Amlin 正與投資者洽談，擬推出新加坡註冊的第三方資本工具（側車），初步目標規模約4,000至5,000萬美元；亞太區行政總裁 William Ho 表示，新工具將延續 Phoenix Re 特殊目的再保工具（SPRV）的成功經驗，並看好區內尚未開發的潛力。報道屬訂閱內容，摘要依據公開導語與標題整理。 [EN原文]"),
 ("亞洲本地註冊的第三方資本工具陸續出現，反映區內再保風險資本市場化與新加坡作為風險轉移平台的吸引力，值得與香港 ILS 政策方向對照觀察。",
  "亞洲本地註冊的第三方資本工具陸續出現，反映區內再保風險資本市場化與新加坡作為風險轉移平台的吸引力，值得與香港 ILS 政策方向對照觀察。"),
 ("涉及另類資本工具時只作架構說明，不涉及任何投資建議", "涉及另類資本工具時只作架構說明，不涉及任何投資建議"),
 ("納入ILS與區域風險資本情報", "納入ILS與區域風險資本情報"),
 ("用於說明亞太風險資本市場的競爭格局", "用於說明亞太風險資本市場的競爭格局"),
 ("香港與新加坡在風險轉移平台的對照", "香港與新加坡在風險轉移平台的對照"),
 (1, 2, 2, 2), ["market", "ils"], ["ils", "sidecar", "singapore", "third-party-capital"],
 ["MS Amlin", "新加坡", "側車", "第三方資本"],
 ("InsuranceAsia News 2026-10-08 報道", "InsuranceAsia News 2026-10-08 報道", "InsuranceAsia News", "2026-10-08"),
 "en", 71))

# ══ 12. InsuranceAsia News：Howden 指亞太數據中心風險集中 ═══════════════
ITEMS.append(mk(
 "ian-howden-apac-datacentre-risk-20261008", "insuranceasianews", "pro", "news",
 "2026-10-08T15:57:00+08:00",
 "https://insuranceasianews.com/apac-data-centre-expansion-concentrates-risk-across-construction-power-operations-and-cyber-howden/",
 ("InsuranceAsia News：Howden 指亞太數據中心擴張 風險集中於建造、電力、營運及網絡",
  "InsuranceAsia News：Howden 指亞太數據中心擴張 風險集中於建造、電力、營運及網絡"),
 ("InsuranceAsia News 10月8日報道：經紀行 Howden 指出，亞太數據中心快速擴張令風險集中於建造、電力、營運及網絡四大環節，令該板塊承保「再次變得越來越高難度」；保險公司與經紀日益提供涵蓋建造期與營運期的綜合方案，其中延誤啟動（DSU）保障只回應由受保實體損失事件所引致的延誤。報道屬訂閱內容，摘要依據公開導語與標題整理。 [EN原文]",
  "InsuranceAsia News 10月8日報道：經紀行 Howden 指出，亞太數據中心快速擴張令風險集中於建造、電力、營運及網絡四大環節，令該板塊承保「再次變得越來越高難度」；保險公司與經紀日益提供涵蓋建造期與營運期的綜合方案，其中延誤啟動（DSU）保障只回應由受保實體損失事件所引致的延誤。報道屬訂閱內容，摘要依據公開導語與標題整理。 [EN原文]"),
 ("數據中心是AI基建的核心資產，其風險集中度高、單一事故可同時觸發建造與營運損失；區內項目融資與大型企業客戶的風險安排將直接受影響。",
  "數據中心是AI基建的核心資產，其風險集中度高、單一事故可同時觸發建造與營運損失；區內項目融資與大型企業客戶的風險安排將直接受影響。"),
 ("客戶涉數據中心或關鍵基建時，須分清建造險、營運險與DSU的觸發條件與除外責任",
  "客戶涉數據中心或關鍵基建時，須分清建造險、營運險與DSU的觸發條件與除外責任"),
 ("納入新興基建風險與核保情報", "納入新興基建風險與核保情報"),
 ("用於說明AI基建投資帶來的保險需求", "用於說明AI基建投資帶來的保險需求"),
 ("跨境數據中心項目的風險安排參照", "跨境數據中心項目的風險安排參照"),
 (2, 3, 2, 2), ["tech", "product"], ["datacentre", "construction", "power", "cyber", "apac"],
 ["Howden", "數據中心", "亞太", "延誤啟動損失"],
 ("InsuranceAsia News 2026-10-08 報道", "InsuranceAsia News 2026-10-08 報道", "InsuranceAsia News", "2026-10-08"),
 "en", 72))

# ══ 13. InsuranceAsia News：AM Best 確認 GIC Re 評級 ════════════════════
ITEMS.append(mk(
 "ian-gic-re-am-best-a-minus-affirmed-20261008", "insuranceasianews", "pro", "news",
 "2026-10-08T14:16:00+08:00",
 "https://insuranceasianews.com/gic-res-investment-income-makes-up-for-lack-of-technical-profits-am-best/",
 ("InsuranceAsia News：AM Best 確認 GIC Re「A-」評級 投資收益彌補承保利潤不足",
  "InsuranceAsia News：AM Best 確認 GIC Re「A-」評級 投資收益彌補承保利潤不足"),
 ("InsuranceAsia News 10月8日報道：評級機構 AM Best 確認印度國有再保公司 GIC Re（General Insurance Corporation of India）的財務實力評級為 A-（excellent）、長期發行人信用評級「a-」（excellent）及印度全國級評級 aaa.IN（exceptional），展望均為穩定；報道指其投資收益彌補了承保（技術）利潤不足。 [EN原文]",
  "InsuranceAsia News 10月8日報道：評級機構 AM Best 確認印度國有再保公司 GIC Re（General Insurance Corporation of India）的財務實力評級為 A-（excellent）、長期發行人信用評級「a-」（excellent）及印度全國級評級 aaa.IN（exceptional），展望均為穩定；報道指其投資收益彌補了承保（技術）利潤不足。 [EN原文]"),
 ("新興市場再保人的盈利結構（依賴投資收益而非承保利潤）是理解其定價行為與長期承保紀律的重要背景，亦影響跨境分保的對手風險評估。",
  "新興市場再保人的盈利結構（依賴投資收益而非承保利潤）是理解其定價行為與長期承保紀律的重要背景，亦影響跨境分保的對手風險評估。"),
 ("引用評級時須註明評級機構、評級日期與展望，不作為投資建議",
  "引用評級時須註明評級機構、評級日期與展望，不作為投資建議"),
 ("納入再保人評級情報", "納入再保人評級情報"),
 ("用於理解新興市場再保人的財務結構", "用於理解新興市場再保人的財務結構"),
 ("跨境分保對手風險的參考", "跨境分保對手風險的參考"),
 (1, 2, 2, 2), ["insurer", "market"], ["ratings", "reinsurance", "india", "investment-income"],
 ["GIC Re", "AM Best", "印度", "再保險"],
 ("InsuranceAsia News 2026-10-08 報道", "InsuranceAsia News 2026-10-08 報道", "InsuranceAsia News", "2026-10-08"),
 "en", 70))

# ══ 14. InsuranceAsia News：Marsh 委任澳洲授權代表主管 ═══════════════════
ITEMS.append(mk(
 "ian-marsh-sonya-febbo-australia-authorised-reps-20261008", "insuranceasianews", "pro", "news",
 "2026-10-08T12:32:00+08:00",
 "https://insuranceasianews.com/marsh-elevates-sonya-febbo-to-australia-head-of-authorised-representatives/",
 ("InsuranceAsia News：Marsh 升任 Sonya Febbo 為澳洲企業及商業授權代表主管",
  "InsuranceAsia News：Marsh 升任 Sonya Febbo 為澳洲企業及商業授權代表主管"),
 ("InsuranceAsia News 10月8日報道：Marsh 委任 Sonya Febbo 為澳洲企業及商業業務的授權代表（authorised representatives）主管；她駐墨爾本，此前在 Marsh 的企業授權代表 XS Insurance 出任董事總經理逾15年。 [EN原文]",
  "InsuranceAsia News 10月8日報道：Marsh 委任 Sonya Febbo 為澳洲企業及商業業務的授權代表（authorised representatives）主管；她駐墨爾本，此前在 Marsh 的企業授權代表 XS Insurance 出任董事總經理逾15年。 [EN原文]"),
 ("授權代表（AR）模式是成熟市場擴張分銷網絡的主要途徑之一；此類人事安排反映經紀行在澳洲的企業與商業險分銷布局，屬同業渠道情報。",
  "授權代表（AR）模式是成熟市場擴張分銷網絡的主要途徑之一；此類人事安排反映經紀行在澳洲的企業與商業險分銷布局，屬同業渠道情報。"),
 ("同業人事消息僅作行業資訊參考，不作客戶招攬材料", "同業人事消息僅作行業資訊參考，不作客戶招攬材料"),
 ("納入同業與渠道情報", "納入同業與渠道情報"),
 ("用於了解經紀行的授權代表分銷模式", "用於了解經紀行的授權代表分銷模式"),
 ("澳洲分銷模式對區域渠道發展的啟示", "澳洲分銷模式對區域渠道發展的啟示"),
 (1, 1, 2, 1), ["market"], ["people", "broker", "australia", "distribution"],
 ["Marsh", "人事任命", "澳洲", "授權代表"],
 ("InsuranceAsia News 2026-10-08 報道", "InsuranceAsia News 2026-10-08 報道", "InsuranceAsia News", "2026-10-08"),
 "en", 70))

# ══ 15. InsuranceAsia News：Aviso 聘 Marsh 前高層領軍資本方案 ═══════════
ITEMS.append(mk(
 "ian-aviso-specialty-wojcik-capital-solutions-20261008", "insuranceasianews", "pro", "news",
 "2026-10-08T10:27:00+08:00",
 "https://insuranceasianews.com/aviso-specialty-hires-marsh-veteran-eric-wojcik-to-stand-up-capital-solutions-group/",
 ("InsuranceAsia News：澳洲 Aviso Specialty 聘 Marsh 前高層 Eric Wojcik 領軍資本方案部門",
  "InsuranceAsia News：澳洲 Aviso Specialty 聘 Marsh 前高層 Eric Wojcik 領軍資本方案部門"),
 ("InsuranceAsia News 10月8日報道：澳洲專業保險經紀 Aviso Specialty 委任 Eric Wojcik 為資本及保證方案（capital and guarantee solutions）主管，2027年3月生效，藉此成立新的資本方案團隊。Wojcik 來自 Marsh，屬資深專才。 [EN原文]",
  "InsuranceAsia News 10月8日報道：澳洲專業保險經紀 Aviso Specialty 委任 Eric Wojcik 為資本及保證方案（capital and guarantee solutions）主管，2027年3月生效，藉此成立新的資本方案團隊。Wojcik 來自 Marsh，屬資深專才。 [EN原文]"),
 ("專門經紀行向「資本與保證方案」延伸，反映客戶對保證（surety／guarantee）與結構性風險轉移需求上升，屬企業客戶保障組合的擴張信號。",
  "專門經紀行向「資本與保證方案」延伸，反映客戶對保證（surety／guarantee）與結構性風險轉移需求上升，屬企業客戶保障組合的擴張信號。"),
 ("同業人事與業務布局消息僅作行業參考", "同業人事與業務布局消息僅作行業參考"),
 ("納入同業與渠道情報", "納入同業與渠道情報"),
 ("用於了解保證與資本方案業務的發展", "用於了解保證與資本方案業務的發展"),
 ("企業客戶跨境保證需求的市場背景", "企業客戶跨境保證需求的市場背景"),
 (1, 2, 2, 1), ["market"], ["people", "broker", "surety", "apac"],
 ["Aviso Specialty", "人事任命", "保證保險", "澳洲"],
 ("InsuranceAsia News 2026-10-08 報道", "InsuranceAsia News 2026-10-08 報道", "InsuranceAsia News", "2026-10-08"),
 "en", 70))

# ══ 16. InsuranceAsia News：特種 MGA 拓展全球血統馬保險 ═════════════════
ITEMS.append(mk(
 "ian-specialty-mga-bloodstock-higgins-20261008", "insuranceasianews", "pro", "news",
 "2026-10-08T17:59:00+08:00",
 "https://insuranceasianews.com/specialty-mga-hires-david-higgins-to-lead-global-bloodstock-expansion/",
 ("InsuranceAsia News：MNK 旗下 Specialty MGA 委任 David Higgins 拓展全球血統馬保險業務",
  "InsuranceAsia News：MNK 旗下 Specialty MGA 委任 David Higgins 拓展全球血統馬保險業務"),
 ("InsuranceAsia News 10月8日報道：MNK Group 旗下 Specialty MGA 委任 David Higgins 帶領拓展其全球血統馬（bloodstock）保險組合，並延伸至澳紐地區；新組合採全球授權，重點市場包括澳紐、美國、英國及歐洲。 [EN原文]",
  "InsuranceAsia News 10月8日報道：MNK Group 旗下 Specialty MGA 委任 David Higgins 帶領拓展其全球血統馬（bloodstock）保險組合，並延伸至澳紐地區；新組合採全球授權，重點市場包括澳紐、美國、英國及歐洲。 [EN原文]"),
 ("血統馬與賽馬相關保險屬高度專業的利基市場，MGA 持續向全球擴張反映特種險的分銷與專業能力競爭；對服務高淨值客戶的團隊屬可留意的利基保障類別。",
  "血統馬與賽馬相關保險屬高度專業的利基市場，MGA 持續向全球擴張反映特種險的分銷與專業能力競爭；對服務高淨值客戶的團隊屬可留意的利基保障類別。"),
 ("涉及利基保險時只作市場資訊說明，不作產品推介", "涉及利基保險時只作市場資訊說明，不作產品推介"),
 ("納入特種險與MGA情報", "納入特種險與MGA情報"),
 ("用於了解利基保障市場的專業分工", "用於了解利基保障市場的專業分工"),
 ("高淨值客戶利基資產保障的國際渠道", "高淨值客戶利基資產保障的國際渠道"),
 (1, 1, 2, 1), ["market", "product"], ["people", "specialty", "bloodstock", "apac"],
 ["Specialty MGA", "血統馬保險", "人事任命", "澳紐"],
 ("InsuranceAsia News 2026-10-08 報道", "InsuranceAsia News 2026-10-08 報道", "InsuranceAsia News", "2026-10-08"),
 "en", 70))

# ══ 17. AIA：友邦峻宇與 Chi Longevity 香港獨家合作 ══════════════════════
ITEMS.append(mk(
 "aia-alta-chi-longevity-hk-exclusive-20261008", "aia", "insurer", "press", "2026-10-08",
 "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/2026/aia-press-release-20261008",
 ("友邦：友邦峻宇與 Chi Longevity 在香港展開獨家合作 今年稍後開設健康長壽中心",
  "友邦：友邦峻宇與 Chi Longevity 在香港展開獨家合作 今年稍後開設健康長壽中心"),
 ("友邦香港及澳門10月8日新聞稿：專為高淨值客戶而設的「友邦峻宇」（AIA Alta）宣布與 Chi Longevity Singapore 在香港展開獨家合作；後者由健康長壽學術權威 Andrea B. Maier 教授共同創辦，在新加坡設有健康長壽醫學診所。友邦峻宇將於今年稍後開設健康長壽中心，讓合資格客戶優先體驗由 Chi Longevity 研發、以實證為本的健康長壽及精準老年醫學方案。新聞稿引述「友邦峻宇高淨值極臻長壽指數」調查，指受訪者對長壽議題的認知評分為74分，但實際準備僅54分，落差明顯。友邦香港及澳門首席執行官馮偉昌表示，香港是全球最長壽地區之一，保險公司角色已超越保障層面，須協助客戶維持健康與身心福祉。",
  "友邦香港及澳門10月8日新聞稿：專為高淨值客戶而設的「友邦峻宇」（AIA Alta）宣布與 Chi Longevity Singapore 在香港展開獨家合作；後者由健康長壽學術權威 Andrea B. Maier 教授共同創辦，在新加坡設有健康長壽醫學診所。友邦峻宇將於今年稍後開設健康長壽中心，讓合資格客戶優先體驗由 Chi Longevity 研發、以實證為本的健康長壽及精準老年醫學方案。新聞稿引述「友邦峻宇高淨值極臻長壽指數」調查，指受訪者對長壽議題的認知評分為74分，但實際準備僅54分，落差明顯。友邦香港及澳門首席執行官馮偉昌表示，香港是全球最長壽地區之一，保險公司角色已超越保障層面，須協助客戶維持健康與身心福祉。"),
 ("高淨值客戶競爭已由保單延伸至健康長壽服務生態；「認知高、準備低」的調查落差，是與高客討論長壽財務與健康規劃的現成切入點。",
  "高淨值客戶競爭已由保單延伸至健康長壽服務生態；「認知高、準備低」的調查落差，是與高客討論長壽財務與健康規劃的現成切入點。"),
 ("與高客討論長壽議題時，聚焦健康管理與保障配套，不使用醫療功效承諾",
  "與高客討論長壽議題時，聚焦健康管理與保障配套，不使用醫療功效承諾"),
 ("納入高客服務生態與同業動態情報", "納入高客服務生態與同業動態情報"),
 ("用於說明保險公司如何延伸至健康服務", "用於說明保險公司如何延伸至健康服務"),
 ("跨境高淨值客戶的長壽與健康服務趨勢", "跨境高淨值客戶的長壽與健康服務趨勢"),
 (2, 2, 3, 2), ["product", "family", "insurer"], ["hnw", "longevity", "health", "ecosystem"],
 ["友邦峻宇", "長壽", "高淨值", "健康管理"],
 ("友邦保險（香港）2026-10-08 新聞稿", "友邦保險（香港）2026-10-08 新聞稿", "AIA Hong Kong", "2026-10-08"),
 "zh", 77, "verified"))

# ══ 18. AIA：第六屆友邦獎學金 100名大學生獲獎 ═════════════════════════
ITEMS.append(mk(
 "aia-scholarships-6th-cohort-100-students-20261008", "aia", "insurer", "press", "2026-10-08",
 "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/2026/aia-press-release-20261008-aia-scholarships-ceremony",
 ("友邦：友邦慈善基金表揚100名大學生 第六屆「友邦獎學金」得獎者誕生",
  "友邦：友邦慈善基金表揚100名大學生 第六屆「友邦獎學金」得獎者誕生"),
 ("友邦香港10月8日新聞稿：友邦慈善基金舉行「友邦獎學金」頒授典禮，向100名傑出大學本科生頒發獎學金，成為第六屆「友邦學人」，並祝賀第三屆學人畢業及回顧「友邦使命實踐計劃」首年進展。AIA 於2020年承諾投入一億美元成立獎學金，每年資助100名就讀香港10間大學的本科生，每人每年可獲5萬港元；基金成立以來已惠及近600名本地大學生，逾230人已完成本科課程。友邦學人自2020年起累計貢獻超過5萬小時義工服務。典禮上香港花劍運動員蔡俊彥與 AIA 管理層及學人對談，分享抗逆力與克服挑戰。",
  "友邦香港10月8日新聞稿：友邦慈善基金舉行「友邦獎學金」頒授典禮，向100名傑出大學本科生頒發獎學金，成為第六屆「友邦學人」，並祝賀第三屆學人畢業及回顧「友邦使命實踐計劃」首年進展。AIA 於2020年承諾投入一億美元成立獎學金，每年資助100名就讀香港10間大學的本科生，每人每年可獲5萬港元；基金成立以來已惠及近600名本地大學生，逾230人已完成本科課程。友邦學人自2020年起累計貢獻超過5萬小時義工服務。典禮上香港花劍運動員蔡俊彥與 AIA 管理層及學人對談，分享抗逆力與克服挑戰。"),
 ("大型保司以慈善基金長期投入本地人才培育，既是品牌與僱主形象工程，也是行業人才管道的一部分；此類企業社會責任資訊適合團隊文化與招募溝通參考。",
  "大型保司以慈善基金長期投入本地人才培育，既是品牌與僱主形象工程，也是行業人才管道的一部分；此類企業社會責任資訊適合團隊文化與招募溝通參考。"),
 ("用於團隊文化與行業人才議題，不作為產品宣傳素材",
  "用於團隊文化與行業人才議題，不作為產品宣傳素材"),
 ("納入保司企業責任情報", "納入保司企業責任情報"),
 ("用於說明行業人才培育的生態投入", "用於說明行業人才培育的生態投入"),
 ("本地人才管道與行業形象的長期觀察", "本地人才管道與行業形象的長期觀察"),
 (0, 1, 2, 1), ["insurer", "market"], ["csr", "talent", "education", "hong-kong"],
 ["友邦", "獎學金", "企業責任", "香港"],
 ("友邦保險（香港）2026-10-08 新聞稿", "友邦保險（香港）2026-10-08 新聞稿", "AIA Hong Kong", "2026-10-08"),
 "zh", 75, "verified"))

# ══ 19. AXA：第三十四屆綠色力量環島行公開報名 ═════════════════════════
ITEMS.append(mk(
 "axa-green-power-island-walk-34-20261008", "axa", "insurer", "press", "2026-10-08",
 "https://www.axa.com.hk/zh/news-room/",
 ("AXA 安盛：第三十四屆綠色力量環島行10月8日起公開接受報名（首席贊助）",
  "AXA 安盛：第三十四屆綠色力量環島行10月8日起公開接受報名（首席贊助）"),
 ("AXA 安盛新聞中心10月8日發布：由 AXA 安盛首席贊助的「第三十四屆綠色力量環島行」於10月8日公開接受報名，屬該公司長期支持的本地環保步行活動。",
  "AXA 安盛新聞中心10月8日發布：由 AXA 安盛首席贊助的「第三十四屆綠色力量環島行」於10月8日公開接受報名，屬該公司長期支持的本地環保步行活動。"),
 ("保司持續以環保與健康社區活動建立品牌連結；在「健康長久好生活」類敘事競爭中，此類活動屬品牌與客戶互動層面的常規動作。",
  "保司持續以環保與健康社區活動建立品牌連結；在「健康長久好生活」類敘事競爭中，此類活動屬品牌與客戶互動層面的常規動作。"),
 ("社區活動資訊可用於客戶互動素材，不涉及產品銷售內容",
  "社區活動資訊可用於客戶互動素材，不涉及產品銷售內容"),
 ("納入保司品牌與社區活動情報", "納入保司品牌與社區活動情報"),
 ("團隊可用作客戶活動的參考", "團隊可用作客戶活動的參考"),
 ("本地客戶活動與品牌連結的常規觀察", "本地客戶活動與品牌連結的常規觀察"),
 (0, 1, 1, 0), ["insurer", "market"], ["csr", "community", "hong-kong", "wellness"],
 ["AXA安盛", "綠色力量環島行", "企業責任", "香港"],
 ("AXA 安盛 2026-10-08 新聞稿", "AXA 安盛 2026-10-08 新聞稿", "AXA Hong Kong", "2026-10-08"),
 "zh", 75, "verified"))

# ══ 20. 政府新聞網／金管局：慎防偽冒香港銀行同業結算網站 ═════════════════
ITEMS.append(mk(
 "hkicl-fake-website-scam-alert-20261008", "govhk", "official", "press",
 "2026-10-08T18:33:00+08:00",
 "https://www.info.gov.hk/gia/general/202610/08/P2026100800441.htm",
 ("政府新聞網（代金管局發稿）：慎防偽冒香港銀行同業結算有限公司的詐騙網站",
  "政府新聞網（代金管局發稿）：慎防偽冒香港銀行同業結算有限公司的詐騙網站"),
 ("香港政府新聞網10月8日18:33代香港金融管理局發出公告：香港銀行同業結算有限公司（結算公司）發現兩個偽冒其官方網站的詐騙網站 tk.hkfps.sbs 及 tuikuan.fpshk.shop，偽裝成「買家網上安全保障」並提供所謂轉數快（FPS）網上交易安全服務（退款、舉報未經授權交易、交易支援），意圖誘導用戶提供銀行名稱、帳號及帳戶持有人姓名，以便從虛擬錢包充值／提款，並引導用戶與偽冒客服對話。結算公司澄清與該等網站絕無關係，重申不會直接向個別公眾提供轉數快服務或主動接觸公眾，真正官方網址為 www.hkicl.com.hk 及 fps.hkicl.com.hk，並呼籲公眾致電 2533 1111 核實可疑通訊，懷疑受騙應盡快報警。",
  "香港政府新聞網10月8日18:33代香港金融管理局發出公告：香港銀行同業結算有限公司（結算公司）發現兩個偽冒其官方網站的詐騙網站 tk.hkfps.sbs 及 tuikuan.fpshk.shop，偽裝成「買家網上安全保障」並提供所謂轉數快（FPS）網上交易安全服務（退款、舉報未經授權交易、交易支援），意圖誘導用戶提供銀行名稱、帳號及帳戶持有人姓名，以便從虛擬錢包充值／提款，並引導用戶與偽冒客服對話。結算公司澄清與該等網站絕無關係，重申不會直接向個別公眾提供轉數快服務或主動接觸公眾，真正官方網址為 www.hkicl.com.hk 及 fps.hkicl.com.hk，並呼籲公眾致電 2533 1111 核實可疑通訊，懷疑受騙應盡快報警。"),
 ("偽冒官方結算平台與客服的詐騙手法持續演變，直接關乎客戶資金安全與支付習慣；屬前線必須轉達的防騙提醒，亦是理財與保障服務的信任基礎議題。",
  "偽冒官方結算平台與客服的詐騙手法持續演變，直接關乎客戶資金安全與支付習慣；屬前線必須轉達的防騙提醒，亦是理財與保障服務的信任基礎議題。"),
 ("提醒客戶只經官方網址及渠道處理轉數快及保費繳付，遇可疑連結先致電機構核實",
  "提醒客戶只經官方網址及渠道處理轉數快及保費繳付，遇可疑連結先致電機構核實"),
 ("納入客戶防騙與支付安全提醒", "納入客戶防騙與支付安全提醒"),
 ("用於向客戶說明官方核實渠道", "用於向客戶說明官方核實渠道"),
 ("跨境客戶在港支付與資金安全的風險提示", "跨境客戶在港支付與資金安全的風險提示"),
 (2, 1, 2, 2), ["reg", "market"], ["fraud", "payment", "consumer-protection", "hong-kong"],
 ["偽冒網站", "轉數快", "防騙", "金管局"],
 ("香港政府新聞網（代金管局發稿）2026-10-08 公告", "香港政府新聞網（代金管局發稿）2026-10-08 公告",
  "HKMA / HKICL", "2026-10-08"), "zh", 85, "verified"))

# ══ 21. SCMP：香港警方再拘17人 涉1.37億「撞車騙保」 ═══════════════════
ITEMS.append(mk(
 "scmp-crash-for-cash-137m-55-arrests-20261007", "scmp", "media", "news",
 "2026-10-07T21:37:00+08:00",
 "https://www.scmp.com/news/hong-kong/law-and-crime/article/3370077/hong-kong-police-arrest-17-more-over-hk137-million-crash-cash-scam",
 ("南華早報：香港警方再拘17人 涉1.37億港元「撞車騙保」 累計55人被捕",
  "南華早報：香港警方再拘17人 涉1.37億港元「撞車騙保」 累計55人被捕"),
 ("南華早報10月7日晚報道：香港警方再拘捕17名與懷疑「撞車騙保」（crash-for-cash）詐騙集團有關的人士，涉及669宗可疑索賠、總額超過1.37億港元（約1,740萬美元）。商業罪案調查科於9月9日至本周二拘捕17名年齡27至49歲的索賠人，令被捕總數增至55人；新一批被捕者與63宗交通意外民事索償有關，涉及2,500萬港元。其中一名被捕人涉嫌提交12宗索賠、申索約364萬港元。警方今年1月起接獲保險公司、相關機構及公眾舉報後展開調查，2月至本月共進行四次執法行動；三人已被控欺詐、企圖欺詐及妨礙司法公正等罪。早前被捕的一對夫婦（37歲司機及38歲註冊護士）共被控20項罪名，因未於6月25日應訊，法院已發出拘捕令。 [EN原文]",
  "南華早報10月7日晚報道：香港警方再拘捕17名與懷疑「撞車騙保」（crash-for-cash）詐騙集團有關的人士，涉及669宗可疑索賠、總額超過1.37億港元（約1,740萬美元）。商業罪案調查科於9月9日至本周二拘捕17名年齡27至49歲的索賠人，令被捕總數增至55人；新一批被捕者與63宗交通意外民事索償有關，涉及2,500萬港元。其中一名被捕人涉嫌提交12宗索賠、申索約364萬港元。警方今年1月起接獲保險公司、相關機構及公眾舉報後展開調查，2月至本月共進行四次執法行動；三人已被控欺詐、企圖欺詐及妨礙司法公正等罪。早前被捕的一對夫婦（37歲司機及38歲註冊護士）共被控20項罪名，因未於6月25日應訊，法院已發出拘捕令。 [EN原文]"),
 ("大額、集團式車禍索賠詐騙直接推高汽車保險與責任險賠付成本，最終由保費承擔；案件規模說明理賠審核與索賠人背景核查在本地市場的重要性。",
  "大額、集團式車禍索賠詐騙直接推高汽車保險與責任險賠付成本，最終由保費承擔；案件規模說明理賠審核與索賠人背景核查在本地市場的重要性。"),
 ("客戶問及車險或索賠時，強調如實申報與配合調查，並提醒虛假索賠的法律後果",
  "客戶問及車險或索賠時，強調如實申報與配合調查，並提醒虛假索賠的法律後果"),
 ("納入保險欺詐與理賠風險情報", "納入保險欺詐與理賠風險情報"),
 ("用於說明保險欺詐對整體保費的影響", "用於說明保險欺詐對整體保費的影響"),
 ("跨境用車與責任保障的合規提醒", "跨境用車與責任保障的合規提醒"),
 (1, 2, 2, 1), ["market", "reg"], ["fraud", "motor", "claims", "enforcement", "hong-kong"],
 ["香港", "車禍騙保", "保險欺詐", "警方"],
 ("南華早報 2026-10-07 報道", "南華早報 2026-10-07 報道", "South China Morning Post", "2026-10-07"),
 "en", 62, "verified"))


path = '/Users/leonliang/maoquanqingbao/data/live-items.json'
d = json.load(open(path, encoding='utf-8'))
ids = {it['id'] for it in d['items']}
urls = {(it.get('originalUrl') or '').rstrip('/') for it in d['items']}
added = []
for it in ITEMS:
    if it['id'] in ids:
        print('SKIP dup id:', it['id'])
        continue
    if it['originalUrl'].rstrip('/') in urls:
        print('SKIP dup url:', it['id'])
        continue
    d['items'] = [it] + d['items']
    ids.add(it['id'])
    urls.add(it['originalUrl'].rstrip('/'))
    added.append(it)

n = len(d['items'])
d['meta']['generatedAt'] = NOW
d['meta']['itemCount'] = n
d['meta']['windowNote'] = {"sc": f"本库{n}条。", "tc": f"本庫{n}條。"}
json.dump(d, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'added {len(added)} items, total {n}, generatedAt {NOW}')

lp = '/Users/leonliang/maoquanqingbao/data/last-check.json'
lc = json.load(open(lp, encoding='utf-8'))
lc['lastCheck'] = NOW
for k, v in lc.get('sources', {}).items():
    v['last'] = NOW
json.dump(lc, open(lp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('last-check.json updated:', NOW, '| sources:', len(lc.get('sources', {})))

for it in added:
    print('  +', it['id'], '|', it['publishedAt'], '|', it['sourceKey'], '|', it['sourceTier'], '|', it['verifyStatus'])
