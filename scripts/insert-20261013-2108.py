#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 2026-10-13 21:08 increment into live-items.json.

窗口：2026-10-13T18:12（上轮）→ 2026-10-13T21:08（本轮），并补回当日 18:12 前遗漏的
同日条目（同属 10-13 发布，均未入库）。

本期新增 11 条：
  artemis 3（Leadenhall 受控 AI 用于 ILS／瑞士再保：再保資本增加是好事、另類資本合理配置／
            Liberty Mutual Re 向墨西哥政府作出感測器觸發參數式地震賠付）
  insuranceasianews 3（巴塞隆拿水災＝城市洪水風險警鐘／IBISA 委任印度 CEO、參數式延伸至中小企／
                      Howden 澳洲自 Marsh 引入五人組建體育娛樂專項）
  insuranceasia 2（Singlife：AI 處理逾五分之一查詢、複雜個案留人手／新加坡由「有無保」轉向
                  「保得夠不夠」、客戶視保險為財富與退休工具）
  insurancebusinessmag 1（日本 FSA 勒令保德信兩家壽險停售新單至 2027-01-31，僱員渠道受限、
                          獨立代理獲豁免）
  asiainsurancereview 2（台灣金管會放寬保險業投資健康／長照事業／精神健康缺勤按年升 35%
                        已成機構層面風險）

无新发布信源：IA（通函最新 2026-10-02，lastUpdate 2026-10-02；新闻稿页无新增）、
  HKMA（新闻稿页最新 2026-10-08）、AIA HK、Manulife HK、Prudential HK、AXA HK、
  Sun Life HK、SCMP 保险专题、NFRA、FSTB/govhk、HKFI、insuranceasia.com 其他
  10-12 及更早条目、IAI 其他条目（多为 10-12 及更早，属窗口外或已收录）。
  已按 substance 去重跳过：AIA 優悅年金（已收）、Jefferies AIA 銀保份額（已收）、
  皇崗口岸強制車保延伸（已收 3 个版本）、IAI Zhibao Labuan Re 進軍香港（发布于 2026-09-24，
  窗口外）。
"""
import json
from datetime import datetime, timezone, timedelta

try:
    import zhconv
    def T(s):
        return zhconv.convert(s, 'zh-hant')
except Exception:  # pragma: no cover
    def T(s):
        return s

NOW = datetime.now(timezone(timedelta(hours=8))).strftime('%Y-%m-%dT%H:%M:%S+08:00')
CR = {"sc": "本站导读", "tc": "本站導讀"}


def mk(id_, sourceKey, tier, kind, pub, url, t, s, w, a_f, a_m, a_l, a_c, ri, boards, themes,
       tags, src, lang, score, verify='pending'):
    return {
        "clusterCount": 1, "score": score, "verifyStatus": verify,
        "sourceTier": tier, "sourceKey": sourceKey, "contentKind": kind,
        "actions": {
            "front": {"sc": a_f, "tc": T(a_f)},
            "midback": {"sc": a_m, "tc": T(a_m)},
            "lead": {"sc": a_l, "tc": T(a_l)},
            "cross": {"sc": a_c, "tc": T(a_c)},
        },
        "rolesImpact": {"front": ri[0], "midback": ri[1], "lead": ri[2], "cross": ri[3]},
        "boards": boards, "themes": themes,
        "tags": {"sc": tags, "tc": [T(x) for x in tags]},
        "contentRole": CR, "featured": False, "evergreen": False, "ingestedAt": NOW,
        "id": id_, "publishedAt": pub, "originalUrl": url,
        "title": {"sc": t, "tc": T(t)},
        "summary": {"sc": s, "tc": T(s)},
        "why": {"sc": w, "tc": T(w)},
        "source": {"sc": src[0], "tc": T(src[0]), "lang": lang, "name": src[1],
                   "date": src[2], "note": src[3] if len(src) > 3 else None},
    }


ITEMS = []

# ══ 1. 日本 FSA 勒令保德信兩家壽險停售新單 ══
ITEMS.append(mk(
    "ibm-japan-fsa-prudential-life-suspension-593252-20261013",
    "insurancebusinessmag", "media", "news",
    "2026-10-13",
    "https://www.insurancebusinessmag.com/asia/news/life-insurance/japan-orders-prudentials-life-units-to-stop-soliciting-new-business-until-january-31-593252.aspx",
    "日本金融廳勒令保德信兩家壽險停售新單至 2027 年 1 月 31 日　僱員銷售渠道受限、獨立代理渠道獲豁免",
    "日本金融廳（FSA）於10月9日向保德信金融（Prudential Financial）旗下兩家壽險發出業務停止及業務改善命令：Prudential of Japan 自10月13日起不得招攬新業務至2027年1月31日；Gibraltar Life 的「生活顧問」僱員銷售渠道被局部停業，但獨立代理渠道可繼續銷售；控股公司 Prudential Holdings of Japan 亦接獲業務改善命令。三家公司須於11月底前提交改善計劃並定期匯報進度。此前該集團披露107名現職及前員工在1991至2025年間詐騙約500名客戶、涉款約31億日圓（約2,000萬美元），另有69人向約240名客戶推介未經批准的投資產品與公司；其自行調查指銷售主管監督不足，讓銷售人員與客戶發展過於密切的關係而未被察覺。 [EN原文]",
    "這是「銷售隊伍自營模式」下內控失效的完整樣本：員工向客戶借款、代墊保費、私下推介非認可產品，全部屬合規紅線。更值得留意的是 FSA 的定性——問題根源是主管監督不足、防弊系統無效，而非個別員工行為。這與香港 IA 對中介人管理責任的取態同源，可作為內部合規培訓中「管理層監督責任」的對照案例；亦提醒前線，代墊保費與私下推介在任何市場都屬高風險動作。",
    "合規警示：代墊保費與私下推介非認可產品屬紅線",
    "銷售隊伍監督責任與防弊系統檢查清單",
    "團隊管理：主管監督失效的代價",
    "日港銷售隊伍監管取向對照",
    (2, 3, 3, 2), ["insurer", "reg"],
    ["enforcement", "conduct", "talent", "japan"],
    ["保德信", "日本金融廳", "銷售違規", "業務停止命令", "客戶賠付"],
    ("Insurance Business Asia 2026-10-13 報道", "Insurance Business Asia", "2026-10-13",
     "EN原文；日期為報道日"),
    "en", 68, "verified"))

# ══ 2. Leadenhall：受控 AI 用於 ILS ══
ITEMS.append(mk(
    "artemis-leadenhall-ils-controlled-ai-20261013",
    "artemis", "pro", "news",
    "2026-10-13",
    "https://www.artemis.bm/news/leadenhall-positions-for-growth-via-ils-product-discipline-and-controlled-ai-use-albertini/",
    "Leadenhall：ILS 產品紀律優先　以「受控 AI」提升生產力與風險分析",
    "Artemis 於10月13日報道，ILS 投資管理人 Leadenhall Capital Partners（2008年成立，股東為 MSI 集團，維持合夥制與投資決策獨立）行政總裁 Luca Albertini 表示，公司2026年資產管理規模顯著增長，團隊仍有餘力擴張現有策略，但會持續觀察投資者對不同 ILS 產品的需求，再對照中期機會與自身所需承保能力才決定投入。科技路線上，他強調對人工智能採取「有節制的採用」：企業層面推動使用，同時施以嚴格監督，用以提升生產力並改善風險分析。 [EN原文]",
    "資產管理端如何引入AI，是「以AI提升效率但不外包責任」的實務版本。可作為內部討論AI治理的參照：把生產力工具、風險分析輔助、人類承保判斷分三層，並理解為何受監管的風險承擔者傾向漸進而非激進採用。",
    "客戶問及AI可靠性時可引述的業界取態",
    "AI 治理三層分工（工具／分析／判斷）",
    "團隊分享：資產端的AI採用節奏",
    "香港ILS生態的國際管理人視角",
    (1, 2, 2, 2), ["tech", "market"],
    ["ai", "ils", "governance", "asset-management"],
    ["Leadenhall", "ILS", "人工智能治理", "風險分析", "資產管理"],
    ("Artemis.bm 2026-10-13 報道", "Artemis.bm", "2026-10-13", "EN原文；含原文正文摘錄"),
    "en", 68, "verified"))

# ══ 3. 瑞士再保：再保資本增加是好事 ══
ITEMS.append(mk(
    "artemis-swiss-re-reinsurance-supply-alt-capital-20261013",
    "artemis", "pro", "news",
    "2026-10-13T19:30:13+08:00",
    "https://www.artemis.bm/news/swiss-re-says-increased-reinsurance-supply-a-positive-will-align-alt-capital-where-it-makes-sense/",
    "瑞士再保：再保資本增加是好消息　另類資本只在合理之處配置",
    "Artemis 於10月13日報道，瑞士再保（Swiss Re）北中東歐產險再保主管 Leopoldo Camara 在2026年巴登-巴登（Baden-Baden）會前表示，更多資本流入再保市場是正面訊號，因為應對日益互聯的風險需要更多資本。他強調瑞士再保的資本定位是長期承擔多線再保（壽險與健康、產險；短尾與長尾），核心承諾是「有能力賠付」，並會配合逾百年累積的風險專業知識，把另類資本配置在合理的地方；他指其資本在市場上需求強勁。 [EN原文]",
    "再保端對「資本充裕」的公開定調，是理解未來續保條件與條款走向的上游信號。瑞士再保把自身資本與另類資本（ILS／巨災債券）明確分工的說法，亦解釋了傳統再保與ILS為何在不同風險層各自定價，可作為向客戶解釋再保環境變化的背景資料。",
    "客戶問再保環境時的上游參照",
    "傳統再保與另類資本分工基礎",
    "團隊簡報：巴登-巴登會前定調",
    "巨災債券與傳統再保的角色分工",
    (0, 2, 3, 2), ["market", "reg"],
    ["reinsurance", "capital", "ils", "pricing"],
    ["瑞士再保", "再保資本", "另類資本", "巴登巴登", "賠付能力"],
    ("Artemis.bm 2026-10-13 報道", "Artemis.bm", "2026-10-13", "EN原文；含原文正文摘錄"),
    "en", 70, "verified"))

# ══ 4. Liberty Mutual Re 墨西哥參數式地震賠付 ══
ITEMS.append(mk(
    "artemis-liberty-mutual-re-mexico-parametric-quake-payout-20261013",
    "artemis", "pro", "news",
    "2026-10-13T17:45:23+08:00",
    "https://www.artemis.bm/news/liberty-mutual-re-makes-sensor-triggered-parametric-earthquake-payout-in-mexico/",
    "Liberty Mutual Re 向墨西哥政府作出感測器觸發的參數式地震賠付　震後數週內啟動",
    "Artemis 於10月13日報道，Liberty Mutual Re（LM Re）就7月17日襲擊墨西哥南部海岸的7.3級地震，向墨西哥聯邦政府作出參數式賠付，並觸發 Safehub「Shake Network」感測器機制。該保單由墨西哥財政部（SHCP）主管、國營保險機構 Agroasemex 管理，採用 LM Re 的 ShakeNet Parametric 方案（結合 Safehub 感測網絡與全球地震模型 GEM 的 OpenQuake 引擎）。地震期間，震央80公里範圍內的感測器錄得實際震動數據，縮窄模型估算與實況差距、降低基差風險，使觸發更精準迅速；該計劃為 ShakeNet Parametric 歷來最大規模部署，保單於6月生效、數週內即被觸發，由 Augment Risk 與當地經紀 TBS 安排。 [EN原文]",
    "這是最完整的「參數式＋感測器」實例：政府層面以參數式保單換取財政韌性與災後公共服務連續性。感測器提供地面實況以降低基差風險，正是參數式最常被質疑的一環。對香港的意義在於發展巨災債券與參數式產品生態時，如何設計觸發門檻與處理基差風險。",
    "與企業客談參數式保障時的實例",
    "參數式觸發與基差風險基礎",
    "團隊分享：感測器觸發的巨災方案",
    "香港巨災債券／參數式方案參照",
    (1, 2, 3, 3), ["product", "market"],
    ["parametric", "catastrophe", "risk-transfer", "technology"],
    ["參數式保險", "地震", "感測器", "墨西哥", "基差風險"],
    ("Artemis.bm 2026-10-13 報道", "Artemis.bm", "2026-10-13", "EN原文；含原文正文摘錄"),
    "en", 72, "verified"))

# ══ 5. 巴塞隆拿水災＝城市洪水風險警鐘 ══
ITEMS.append(mk(
    "ian-barcelona-floods-urban-flood-risk-20261013",
    "insuranceasianews", "pro", "news",
    "2026-10-13T07:30:03+08:00",
    "https://insuranceasianews.com/barcelona-floods-are-a-wake-up-call-on-urban-flood-risk/",
    "InsuranceAsia News 評論：巴塞隆拿水災為城市洪水風險敲響警鐘",
    "InsuranceAsia News 於10月13日發表評論文章，以巴塞隆拿近期水災為切入點，檢視城市洪水風險。作者長期採訪保險人、再保人、經紀與巨災模型機構，指洪水、颱風與氣候變化下的風險累積正被重新評估，並引伸至亞洲城市面對的同一課題；同平台另一篇評論指出，亞洲洪水暴露人口自1975年以來增加約十億，而AI驅動的防禦手段正在香港與曼谷等地出現。文章屬訂閱內容，公開部分為導語。 [EN原文]",
    "城市洪水是香港、曼谷、雅加達等高密度城市共同的保障缺口課題：城市化速度與排水能力不匹配屬結構性問題。可用於與客戶討論財產險中「洪水是否受保、如何定義」以及企業持續計劃的實際風險敞口。",
    "客戶問洪水保障範圍時的背景",
    "城市洪水與保障缺口基礎",
    "團隊分享：亞洲城市洪水風險",
    "粵港澳大灣區城市洪水風險討論",
    (1, 2, 2, 2), ["market", "product"],
    ["catastrophe", "climate", "protection-gap", "property"],
    ["洪水", "城市風險", "巴塞隆拿", "氣候變化", "保障缺口"],
    ("InsuranceAsia News 2026-10-13 評論", "InsuranceAsia News", "2026-10-13",
     "EN原文；訂閱內容，事實來自官網導語"),
    "en", 62, "verified"))

# ══ 6. IBISA 委任印度 CEO、參數式延伸 ══
ITEMS.append(mk(
    "ian-ibisa-parametric-india-ceo-20261013",
    "insuranceasianews", "pro", "news",
    "2026-10-13T07:58:43+08:00",
    "https://insuranceasianews.com/parametric-insurer-ibisa-appoints-samdarshi-vikram-singh-as-ceo-for-india/",
    "參數式保險公司 IBISA 委任印度 CEO　業務由農業延伸至中小企與可再生能源",
    "InsuranceAsia News 於10月13日報道，總部設於盧森堡的參數式保險公司 IBISA 委任 Samdarshi Vikram Singh 為印度行政總裁；公司計劃把業務由農業延伸至借貸、中小企、可再生能源等受氣候波動影響的領域。文章屬訂閱內容，公開部分為導語。 [EN原文]",
    "參數式產品的應用邊界正由傳統農險擴展至中小企營運中斷與可再生能源資產，反映氣候波動如何被轉化為可承保的結構。可作為參數式產品適用場景的觀察案例，亦呼應新興市場保障缺口的商業化路徑。",
    "參數式產品適用場景舉例",
    "參數式保險與氣候風險基礎",
    "團隊分享：新興市場參數式應用",
    "新興市場氣候風險保障路徑",
    (0, 1, 2, 2), ["product", "market"],
    ["parametric", "climate", "emerging-markets", "insurtech"],
    ["參數式保險", "IBISA", "印度", "氣候風險", "中小企"],
    ("InsuranceAsia News 2026-10-13 報道", "InsuranceAsia News", "2026-10-13",
     "EN原文；訂閱內容，事實來自官網導語"),
    "en", 60, "verified"))

# ══ 7. Howden 澳洲組建體育娛樂專項 ══
ITEMS.append(mk(
    "ian-howden-australia-sport-entertainment-practice-20261013",
    "insuranceasianews", "pro", "news",
    "2026-10-13T15:19:09+08:00",
    "https://insuranceasianews.com/howden-australia-drafts-marsh-team-for-sport-and-entertainment-practice-build-out/",
    "Howden 澳洲自 Marsh 引入五名資深經紀　組建體育及娛樂專項業務",
    "InsuranceAsia News 於10月13日報道，Howden Australia 自 Marsh 引入五名資深經紀（包括 Simon Calabrese），擴建其體育及娛樂專項業務，並形容這是對該板塊的「重大投資」。文章屬訂閱內容，公開部分為導語。 [EN原文]",
    "經紀行以「整隊挖角」方式切入專項市場，是中介競爭格局變化的直接信號：專項與高附加值業務正取代單純的規模競爭。可作為觀察香港經紀市場專業化方向的參照。",
    "與客戶談市場專業化時的行業動態",
    "專項保險業務與經紀競爭基礎",
    "團隊分享：區域經紀行業務佈局",
    "專項風險的跨境安排",
    (0, 1, 2, 1), ["insurer", "market"],
    ["brokers", "talent", "specialty", "apac"],
    ["Howden", "體育娛樂保險", "經紀", "人才流動", "澳洲"],
    ("InsuranceAsia News 2026-10-13 報道", "InsuranceAsia News", "2026-10-13",
     "EN原文；訂閱內容，事實來自官網導語"),
    "en", 60, "verified"))

# ══ 8. Singlife：AI 與人工監督 ══
ITEMS.append(mk(
    "iaasia-singlife-ai-human-oversight-20261013",
    "insuranceasia", "media", "news",
    "2026-10-13T16:36:28+08:00",
    "https://insuranceasia.com/videos/singlife-weighs-ai-speed-against-human-oversight",
    "Singlife：AI 已處理逾五分之一查詢、處理時間減 30%　複雜及敏感個案仍保留人手",
    "Insurance Asia 於10月13日報道，新加坡 Singlife 正把人工智能擴展至客戶服務，並為哪些查詢可無需人手介入設定界線。其電郵代理現處理逾五分之一的查詢，處理時間減少30%。集團科技與營運主管 Romil Sharma 表示，系統會先評估客戶意圖、緊急性與情境，再決定自動回覆、人手覆核或升級；保單批註（如增加保障）因涉及保費計算與客戶個別評估，須由人手判斷。Singlife 以是否正確理解與分流、回覆是否有用、客戶是否需再跟進等指標衡量成效，而非只看回應速度。Sharma 強調AI出錯時責任仍在保險人：「你可以外判服務與能力，但不能外判責任與問責。」 [EN原文]",
    "這是「AI 上線前要想清楚的三件事」的現成案例：分流規則、成效衡量、責任歸屬。特別是「不能外判責任」與香港 IA 對中介人責任的取態一致，適合在內部AI培訓中作為治理原則的引述。",
    "客戶問AI客服可靠性時的回應要點",
    "AI 治理：分流規則與責任歸屬",
    "團隊簡報：AI 客服的成效衡量",
    "區域保險人AI落地案例對照",
    (2, 3, 2, 2), ["tech", "insurer"],
    ["ai", "claims", "governance", "customer-service"],
    ["Singlife", "人工智能", "客戶服務", "責任歸屬", "新加坡"],
    ("Insurance Asia 2026-10-13 報道", "Insurance Asia", "2026-10-13",
     "EN原文；含原文正文摘錄"),
    "en", 66, "verified"))

# ══ 9. 新加坡：由「有無保」轉向「保得夠不夠」 ══
ITEMS.append(mk(
    "iaasia-singapore-insurance-adequacy-retirement-20261013",
    "insuranceasia", "media", "news",
    "2026-10-13T13:06:03+08:00",
    "https://insuranceasia.com/insurance/exclusive/singapore-insurers-face-shift-coverage-adequacy",
    "新加坡保險業由「有沒有保」轉向「保得夠不夠」　客戶視保險為財富與退休工具",
    "Insurance Asia 於10月13日報道，Etiqa Insurance Singapore 行政總裁 Claudia Soh 指出，東南亞多數市場仍在擴大保險滲透與收窄保障缺口，新加坡的挑戰則轉為保障是否足夠、是否相關、能否跟上客戶需要的變化。報道引述《安聯全球保險報告2026》，新加坡保險滲透率為GDP的7.6%，在選定亞洲市場中排第四，位列韓國、台灣及香港之後；CIMB 新加坡5月報告指52.6%受訪者認為保險有助達成財務獨立，較2025年的45%上升。客戶正把保險納入長期財務規劃，關注退休、財富累積、傳承，以至寵物與貴重物品保障。Soh 認為AI可助保險人更了解客戶，但「信任、人的判斷與有意義的客戶關係同樣重要」，並指「最大的風險是自滿」。 [EN原文]",
    "「滲透率之後是充足度」的市場階段判斷，對香港同樣適用——香港滲透率高企，前線的價值正從「有無保」轉向「保額與結構是否足夠」。52.6% 這個「保險＝財務獨立工具」的認知轉變，可直接支撐以退休與傳承為切入的顧問式對話。",
    "由「有無保」轉向「夠不夠」的對話框架",
    "保障充足度評估的市場背景",
    "團隊分享：新加坡市場階段與香港對照",
    "高滲透市場的財富傳承需求",
    (2, 3, 3, 2), ["market", "family"],
    ["retirement", "wealth-transfer", "protection-gap", "adequacy"],
    ["新加坡", "保障充足度", "退休規劃", "財富傳承", "滲透率"],
    ("Insurance Asia 2026-10-13 報道", "Insurance Asia", "2026-10-13",
     "EN原文；含原文正文摘錄"),
    "en", 66, "verified"))

# ══ 10. 台灣：放寬保險業投資健康與長照事業 ══
ITEMS.append(mk(
    "iaa-taiwan-insurers-invest-health-ltc-97223-20261013",
    "asiainsurancereview", "pro", "news",
    "2026-10-13",
    "https://www.asiainsurancereview.com/News/View-NewsLetter-Article/id/97223/Type/AirPlus/Taiwan-Regulator-opens-up-insurers-investments-in-health-wellness-and-long-term-care",
    "台灣：金管會放寬保險業投資健康、養生與長期照顧事業",
    "Asia Insurance Review 於10月13日報道，台灣金融監督管理委員會保險局（IB）宣布將發布令釋，明確允許保險公司投資健康促進、長期照顧（LTC）設施及高齡共融服務等相關事業，並歸類為「健康與福祉事業」。此舉為保險資金開拓與本業相連的長期資產類別。 [EN原文]",
    "監管把「保險資金可投什麼」與高齡化服務接軌，是亞洲多個市場的共同方向：保險公司由單純的給付者走向服務供給者。香港正面對退休保障與樂齡服務的討論，台灣做法可作制度對照，亦關係到保險資金長期配置的資產類別選擇。",
    "客戶談退休與樂齡服務時的區域背景",
    "保險資金運用範圍與高齡化政策",
    "團隊簡報：亞洲保險資金投向新趨勢",
    "台港退休與長照制度對照",
    (1, 2, 3, 3), ["reg", "market"],
    ["long-term-care", "ageing", "investment", "policy"],
    ["台灣", "金管會", "長期照顧", "保險資金", "高齡化"],
    ("Asia Insurance Review 2026-10-13 報道", "Asia Insurance Review", "2026-10-13",
     "EN原文；訂戶內容，事實來自官網導語"),
    "en", 68, "pending"))

# ══ 11. 精神健康缺勤＝機構層面風險 ══
ITEMS.append(mk(
    "iaa-mental-health-absences-organisational-risk-97222-20261013",
    "asiainsurancereview", "pro", "news",
    "2026-10-13",
    "https://www.asiainsurancereview.com/News/View-NewsLetter-Article/id/97222/Type/AirPlus/Mental-health-absences-are-now-considered-an-organisational-risk",
    "精神健康缺勤按年升 35%　已成為機構層面的風險",
    "Asia Insurance Review 於10月13日報道，引述 Sedgwick Health Solutions 數據指出，精神健康相關缺勤按年增加35%，已成為澳洲僱員長期休假的主要成因，並被視為機構層面的風險；當地安全網正同時承受精神健康問題與生活成本上升的壓力。 [EN原文]",
    "精神健康已由「個人問題」轉為「機構風險」，直接影響團體醫療與僱員福利的設計與成本。對香港的參照在於：企業客的福利方案如何納入心理健康支援，以及醫療通脹中行為健康項目的佔比變化。",
    "企業客談僱員福利時的新維度",
    "精神健康與團體保險定價基礎",
    "團隊分享：缺勤數據作為風險信號",
    "區域僱員福利趨勢對照",
    (1, 2, 2, 1), ["product", "market"],
    ["health", "employee-benefits", "mental-health", "claims"],
    ["精神健康", "缺勤", "僱員福利", "團體保險", "澳洲"],
    ("Asia Insurance Review 2026-10-13 報道", "Asia Insurance Review", "2026-10-13",
     "EN原文；訂戶內容，事實來自官網導語"),
    "en", 64, "pending"))

# ═══ 写入 ═══
path = '/Users/leonliang/maoquanqingbao/data/live-items.json'
d = json.load(open(path, encoding='utf-8'))
ids = {it.get('id') for it in d['items']}
urls = {(it.get('originalUrl') or '').rstrip('/') for it in d['items']}
added = []
for it in reversed(ITEMS):
    if it['id'] in ids or it['originalUrl'].rstrip('/') in urls:
        print('SKIP dup:', it['id'])
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
    print('  +', it['id'], '|', it['publishedAt'], '|', it['sourceKey'], '|', it['sourceTier'],
          '|', it['verifyStatus'])
