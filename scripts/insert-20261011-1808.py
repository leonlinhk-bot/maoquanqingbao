#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 2026-10-11 18:0x increment into live-items.json.

窗口：2026-10-11T00:27（上次检查）→ 2026-10-11T18:08。10月11日为周日，
香港监管/保司信源无新发布（IA 通函最新为10月2日、HKMA 最新为10月9日、
AIA/宏利/保誠/永明/安盛 新闻室最新分别为10月9日/9月28日/10月4日/10月2日/10月8日，
均已入库）；本期新增 7 条（含数条 10月2日至10月9日期间发布但未被上轮采集的补漏条目）。
"""
import json
from datetime import datetime, timezone, timedelta

NOW = datetime.now(timezone(timedelta(hours=8))).strftime('%Y-%m-%dT%H:%M:%S+08:00')
CR = {"sc": "本站导读", "tc": "本站導讀"}


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
                   "date": src[3], "note": src[4] if len(src) > 4 else None},
    }


ITEMS = []

# ══ 1. 金融监管总局《财产保险公司保险产品开发管理规定》（8章41条、8类禁止开发情形）══
ITEMS.append(mk(
    "nfra-pnc-product-development-rules-8-prohibited-20261009",
    "nfra", "official", "circular",
    "2026-10-09",
    "https://www.nfra.gov.cn/cn/view/pages/ItemDetail.html?docId=1274219&itemId=915",
    ("金融監管總局發布《財產保險公司保險產品開發管理規定》：8章41條、明確8類禁止開發情形",
     "金融監管總局發布《財產保險公司保險產品開發管理規定》：8章41條、明確8類禁止開發情形"),
    ("國家金融監督管理總局10月9日發布修訂後的《財產保險公司保險產品開發管理規定》，共8章41條，由原《財產保險公司保險產品開發指引》系統性修訂並更名，涵蓋總則、產品開發基本要求、主險條款費率要求、附加險條款費率要求、產品開發管理要求、評估修訂與清理註銷、監督管理及附則。規定明確8類不得開發的產品情形：一、不具法律上承認的保險利益；二、約定保險事故不會造成被保險人實際損失；三、約定保險事故必然發生或必然不發生；四、承保投機風險；五、無實際保障內容、單純以降價（費）漲價（費）或惡意炒作爲目的；六、承諾未出險返還保險費或其他不當利益；七、實質承擔風險保障但不收取保險費（另有規定除外）；八、其他違反法律法規、保險原理或公序良俗。規定另要求險企成立由主要負責人牽頭的產品管理委員會、對當期簽單保費佔比5%以上在售產品至少每年評估一次保費充足性，並單設附加險專章。總局定調此爲財險監管及非車險綜合治理的重要舉措。",
     "國家金融監督管理總局10月9日發布修訂後的《財產保險公司保險產品開發管理規定》，共8章41條，由原《財產保險公司保險產品開發指引》系統性修訂並更名，涵蓋總則、產品開發基本要求、主險條款費率要求、附加險條款費率要求、產品開發管理要求、評估修訂與清理註銷、監督管理及附則。規定明確8類不得開發的產品情形：一、不具法律上承認的保險利益；二、約定保險事故不會造成被保險人實際損失；三、約定保險事故必然發生或必然不發生；四、承保投機風險；五、無實際保障內容、單純以降價（費）漲價（費）或惡意炒作爲目的；六、承諾未出險返還保險費或其他不當利益；七、實質承擔風險保障但不收取保險費（另有規定除外）；八、其他違反法律法規、保險原理或公序良俗。規定另要求險企成立由主要負責人牽頭的產品管理委員會、對當期簽單保費佔比5%以上在售產品至少每年評估一次保費充足性，並單設附加險專章。總局定調此爲財險監管及非車險綜合治理的重要舉措。"),
    ("內地財險產品開發閘門明顯收緊，附加險與「無實質保障」產品被點名，並首次以部門規範性文件層級列示8類禁止情形；對跨境產品設計思路與經代主推產品的話術合規具前置參考價值。",
     "內地財險產品開發閘門明顯收緊，附加險與「無實質保障」產品被點名，並首次以部門規範性文件層級列示8類禁止情形；對跨境產品設計思路與經代主推產品的話術合規具前置參考價值。"),
    ("向客戶解釋「條款為何這樣寫」時可引用監管口徑", "向客戶解釋「條款為何這樣寫」時可引用監管口徑"),
    ("銷售話術自查：有無過度包裝無實質保障的附加險", "銷售話術自查：有無過度包裝無實質保障的附加險"),
    ("團隊合規課：以8類禁止情形做產品紅線測驗", "團隊合規課：以8類禁止情形做產品紅線測驗"),
    ("大灣區／跨境產品創新時的非車險合規視角", "大灣區／跨境產品創新時的非車險合規視角"),
    (3, 2, 2, 2), ["reg"], ["reg", "product", "compliance"],
    ["金融监管总局", "财险产品开发", "8类禁止情形", "附加险", "产品管理委员会"],
    ("國家金融監督管理總局 2026-10-09 發布", "國家金融監督管理總局 2026-10-09 發布", "国家金融监督管理总局",
     "2026-10-09"),
    "zh", 88, "verified"))

# ══ 2. 信報《保險解碼》：財管業升級 保險專才迎黃金時代 ══
ITEMS.append(mk(
    "hkej-wealth-management-upgrade-insurance-talent-golden-age-20261010",
    "hkej", "pro", "news",
    "2026-10-10T08:00:00+08:00",
    "https://www.hkej.com/dailynews/investment/article/4536766/",
    ("信報《保險解碼》：財管業升級　保險專才迎黃金時代",
     "信報《保險解碼》：財管業升級　保險專才迎黃金時代"),
    ("信報10月10日刊出的《保險解碼》專欄文章，以9月16日出爐的《香港經濟和社會發展第一個五年規劃（2026—2030年）》及2026年《施政報告》為切入點，指出市場雖憂慮環球經濟波動、甚至擔心隨時出現「股債雙殺」，但只要看清政策藍圖，便知香港正全力鞏固國際財富管理中心地位；文章認為這既為市場打下「定海神針」，亦預示財富管理的戰場已由單純的一端轉向更專業的一端（原文為節錄，僅見於開篇論述），並由此推論保險專業人才迎來黃金時代。",
     "信報10月10日刊出的《保險解碼》專欄文章，以9月16日出爐的《香港經濟和社會發展第一個五年規劃（2026—2030年）》及2026年《施政報告》為切入點，指出市場雖憂慮環球經濟波動、甚至擔心隨時出現「股債雙殺」，但只要看清政策藍圖，便知香港正全力鞏固國際財富管理中心地位；文章認為這既為市場打下「定海神針」，亦預示財富管理的戰場已由單純的一端轉向更專業的一端（原文為節錄，僅見於開篇論述），並由此推論保險專業人才迎來黃金時代。"),
    ("施政報告／五年規劃後，少見由業界視角把「財管業升級」與「保險專才需求」直接掛鈎的論述；可作為團隊增員敘事與專業化培訓定位的參考框架。",
     "施政報告／五年規劃後，少見由業界視角把「財管業升級」與「保險專才需求」直接掛鈎的論述；可作為團隊增員敘事與專業化培訓定位的參考框架。"),
    ("與高客談資產配置時引述政策定位", "與高客談資產配置時引述政策定位"),
    ("把「財管升級」轉譯為本團隊的專業服務清單", "把「財管升級」轉譯為本團隊的專業服務清單"),
    ("增員話術：政策藍圖下的保險專業化紅利", "增員話術：政策藍圖下的保險專業化紅利"),
    ("與家族辦公室／私行渠道對接時的定位說明", "與家族辦公室／私行渠道對接時的定位說明"),
    (2, 2, 3, 2), ["market"], ["career", "market", "high-net-worth"],
    ["信报", "保险解码", "财富管理", "保险专才", "施政报告"],
    ("信報 2026-10-10《保險解碼》", "信報 2026-10-10《保險解碼》", "信報", "2026-10-10", "原文為節錄版"),
    "zh", 70, "pending"))

# ══ 3. 財聞（引路透）：保險業界對AI風險責任歸屬分歧顯著 ══
ITEMS.append(mk(
    "caiwen-netdiligence-ai-risk-ownership-divergence-20261007",
    "caiwennews", "media", "news",
    "2026-10-07",
    "https://www.caiwennews.com/article/1638620.shtml",
    ("財聞（引路透）：保險業界對人工智能風險責任歸屬分歧顯著",
     "財聞（引路透）：保險業界對人工智能風險責任歸屬分歧顯著"),
    ("財聞引述路透社報道，10月6日在美國費城舉行的 NetDiligence 數字風險峰會上，與會專家指出黑客已利用AI發動攻擊，但保險業界對AI風險應由哪類保單承保管仍存明顯分歧：一派認為屬數字／網絡風險，一派主張歸入董責險（D&O），亦有觀點認為這是全新風險類型、行業尚未找到合適承保方案。Berkley Cyber Risk Solutions 高級副總裁兼法務總監 Gail Arkin 指AI引發的問題遠超電子數據領域、本質上應屬董責險，數字保險無法覆蓋侵犯第三方權利、違規使用數據或算法偏見；Hartford Steam Boiler 全球數字產品經理 Tim Nazzaro 把AI風險分為安全與隱私（歸網絡保單）、其他險種（如AI招聘歧視歸僱主責任險）及尚無明確歸屬三類，並警告勿簡單擴大承保範圍；AXA XL 北美網絡理賠負責人 Danielle Roth 主張回歸保險基本面（被保險人是誰、損失性質、是否觸發協議、有無除外條款），稱「違規事件中AI是否被使用或許永遠無法查明」。MOXFIVE 事件響應副總裁 Michael Brunetti 透露7月4日前後公司業務量創紀錄，SaaS應用（如 ShinyHunters 針對的目標）成新趨勢，AI被用於篩選敏感數據、撰寫勒索函及快速構建高管畫像。 [EN原文]",
     "財聞引述路透社報道，10月6日在美國費城舉行的 NetDiligence 數字風險峰會上，與會專家指出黑客已利用AI發動攻擊，但保險業界對AI風險應由哪類保單承保管仍存明顯分歧：一派認為屬數字／網絡風險，一派主張歸入董責險（D&O），亦有觀點認為這是全新風險類型、行業尚未找到合適承保方案。Berkley Cyber Risk Solutions 高級副總裁兼法務總監 Gail Arkin 指AI引發的問題遠超電子數據領域、本質上應屬董責險，數字保險無法覆蓋侵犯第三方權利、違規使用數據或算法偏見；Hartford Steam Boiler 全球數字產品經理 Tim Nazzaro 把AI風險分為安全與隱私（歸網絡保單）、其他險種（如AI招聘歧視歸僱主責任險）及尚無明確歸屬三類，並警告勿簡單擴大承保範圍；AXA XL 北美網絡理賠負責人 Danielle Roth 主張回歸保險基本面（被保險人是誰、損失性質、是否觸發協議、有無除外條款），稱「違規事件中AI是否被使用或許永遠無法查明」。MOXFIVE 事件響應副總裁 Michael Brunetti 透露7月4日前後公司業務量創紀錄，SaaS應用（如 ShinyHunters 針對的目標）成新趨勢，AI被用於篩選敏感數據、撰寫勒索函及快速構建高管畫像。 [EN原文]"),
    ("AI責任歸屬未定＝保單責任邊界未定；這正是企業客戶（尤其有跨境或SaaS業務者）在網絡／董責／專業責任保單檢視時最容易被忽略的空白。",
     "AI責任歸屬未定＝保單責任邊界未定；這正是企業客戶（尤其有跨境或SaaS業務者）在網絡／董責／專業責任保單檢視時最容易被忽略的空白。"),
    ("向企業主客戶提示AI責任的保單空白", "向企業主客戶提示AI責任的保單空白"),
    ("網絡／董責／專業責任組合檢視清單新增「AI使用」一欄", "網絡／董責／專業責任組合檢視清單新增「AI使用」一欄"),
    ("團隊分享：新興風險如何轉化為加保需求", "團隊分享：新興風險如何轉化為加保需求"),
    ("跨境客戶風險地圖中的AI治理節點", "跨境客戶風險地圖中的AI治理節點"),
    (2, 2, 2, 2), ["tech", "product"], ["ai", "cyber", "reg", "compliance"],
    ["AI风险", "董责险", "网络保险", "NetDiligence", "SaaS勒索"],
    ("財聞（引路透社）2026-10-07", "財聞（引路透社）2026-10-07", "財聞網", "2026-10-07"),
    "zh", 62, "verified"))

# ══ 4. Sapiens 推出保險原生AI底座 Sapiens Brain ══
ITEMS.append(mk(
    "sapiens-brain-insurance-native-ai-foundation-20261006",
    "sapiens", "pro", "news",
    "2026-10-06",
    "https://www.prnewswire.com/news-releases/sapiens-launches-sapiens-brain-the-insurance-native-ai-foundation-powering-sapiensaip-302899543.html",
    ("Sapiens推出保險原生AI底座「Sapiens Brain」：以40年產品知識圖譜錨定模型、降低幻覺",
     "Sapiens推出保險原生AI底座「Sapiens Brain」：以40年產品知識圖譜錨定模型、降低幻覺"),
    ("保險軟件商 Sapiens（Sapiens International Corporation N.V.）10月6日於倫敦發布 Sapiens Brain，作為其AI平台 SapiensAIP 的專有AI底座。Sapiens Brain 以「互聯記憶系統」（互聯知識圖譜）形式建立保險原生知識基礎，把公司40年建置與運行保險系統所累積的產品、業務邏輯、邊緣個案與監管現實（含數百萬行程式碼、產品文件及設計文件）納入模型推理依據，令輸出「有據可引、結構上抗幻覺」，並可按險種（如 Sapiens Brain for Sapiens Life）沉澱產品歷史。架構上 Sapiens 刻意把 SapiensAIP 及其代理建於核心系統之外，並以模型上下文協議（MCP）暴露核心系統，使外部建立的代理可原生接入而非以傳統API「硬接」；系統另設完整審計軌跡與代理推理鏈記錄，以符合受監管行業要求。CEO Paul Wheeler 稱組合讓代理「如原生於核心系統」，CTO Glen Ceniza 則強調缺乏本體論的通用模型必然漂移與幻覺。 [EN原文]",
     "保險軟件商 Sapiens（Sapiens International Corporation N.V.）10月6日於倫敦發布 Sapiens Brain，作為其AI平台 SapiensAIP 的專有AI底座。Sapiens Brain 以「互聯記憶系統」（互聯知識圖譜）形式建立保險原生知識基礎，把公司40年建置與運行保險系統所累積的產品、業務邏輯、邊緣個案與監管現實（含數百萬行程式碼、產品文件及設計文件）納入模型推理依據，令輸出「有據可引、結構上抗幻覺」，並可按險種（如 Sapiens Brain for Sapiens Life）沉澱產品歷史。架構上 Sapiens 刻意把 SapiensAIP 及其代理建於核心系統之外，並以模型上下文協議（MCP）暴露核心系統，使外部建立的代理可原生接入而非以傳統API「硬接」；系統另設完整審計軌跡與代理推理鏈記錄，以符合受監管行業要求。CEO Paul Wheeler 稱組合讓代理「如原生於核心系統」，CTO Glen Ceniza 則強調缺乏本體論的通用模型必然漂移與幻覺。 [EN原文]"),
    ("「行業原生知識圖譜＋可審計推理鏈」正是保險AI落地的合規門檻示範；對評估本地核保／理賠／客服AI工具的可靠性、可解釋性與可審計性，提供了可借用的判斷標準。",
     "「行業原生知識圖譜＋可審計推理鏈」正是保險AI落地的合規門檻示範；對評估本地核保／理賠／客服AI工具的可靠性、可解釋性與可審計性，提供了可借用的判斷標準。"),
    ("向客戶解釋AI輔助核保／理賠時的可解釋性語言", "向客戶解釋AI輔助核保／理賠時的可解釋性語言"),
    ("內部AI工具選型：把「有無知識錨定與審計軌跡」列為門檻", "內部AI工具選型：把「有無知識錨定與審計軌跡」列為門檻"),
    ("團隊分享：AI在保險價值鏈的落地路徑與風險", "團隊分享：AI在保險價值鏈的落地路徑與風險"),
    ("與合作方談AI合規與責任邊界的話題入口", "與合作方談AI合規與責任邊界的話題入口"),
    (2, 2, 3, 2), ["tech"], ["ai", "insurtech", "tech"],
    ["Sapiens", "Sapiens Brain", "SapiensAIP", "知识图谱", "可解释AI"],
    ("PR Newswire/Sapiens 2026-10-06 發布", "PR Newswire/Sapiens 2026-10-06 發布", "Sapiens International Corporation",
     "2026-10-06"),
    "en", 68, "verified"))

# ══ 5. Insurance Asia／Aon：亞太網絡與私隱監管分歧擴大 ══
ITEMS.append(mk(
    "iaasia-aon-apac-cyber-regulatory-divergence-20261009",
    "insuranceasia", "pro", "news",
    "2026-10-09",
    "https://insuranceasia.com/insurance/news/insurers-face-apac-cyber-regulatory-divergence-enforcement-tightens",
    ("Insurance Asia／Aon：亞太網絡與私隱監管分歧擴大　保險限額需重估",
     "Insurance Asia／Aon：亞太網絡與私隱監管分歧擴大　保險限額需重估"),
    ("Insurance Asia 引述 Aon 報告《The Changing Cyber Risk Landscape in APAC: Regulation, Fines and Insurability》指出，亞太各司法管轄區的網絡安全與數據私隱法規正快速演化並走向分歧：澳洲、印度正強化執法框架並提高罰則上限，內地則擴張域外管轄並釐清安全與通報義務；印尼、日本、馬來西亞、新西蘭、新加坡、韓國、泰國及越南近期立法改革亦收緊資料外洩通報要求並擴大執法權。Aon 提醒董事會與風險經理須確保網絡、董責（D&O）及專業彌償保單的限額、結構與保障對應「可信的最壞情境」，並稱監管變化可實質改變損失結果、令原本看似保守的安排迅速變薄；在監管趨成熟市場，執法一旦確立，審查可迅速升級並延伸至相鄰監管框架。報告指14個受研究市場中13個可就罰款投保，僅內地明文禁止彌償；罰則由新西蘭約6,000美元至澳洲3,500萬美元或年營業額30%不等。 [EN原文]",
     "Insurance Asia 引述 Aon 報告《The Changing Cyber Risk Landscape in APAC: Regulation, Fines and Insurability》指出，亞太各司法管轄區的網絡安全與數據私隱法規正快速演化並走向分歧：澳洲、印度正強化執法框架並提高罰則上限，內地則擴張域外管轄並釐清安全與通報義務；印尼、日本、馬來西亞、新西蘭、新加坡、韓國、泰國及越南近期立法改革亦收緊資料外洩通報要求並擴大執法權。Aon 提醒董事會與風險經理須確保網絡、董責（D&O）及專業彌償保單的限額、結構與保障對應「可信的最壞情境」，並稱監管變化可實質改變損失結果、令原本看似保守的安排迅速變薄；在監管趨成熟市場，執法一旦確立，審查可迅速升級並延伸至相鄰監管框架。報告指14個受研究市場中13個可就罰款投保，僅內地明文禁止彌償；罰則由新西蘭約6,000美元至澳洲3,500萬美元或年營業額30%不等。 [EN原文]"),
    ("跨市場客戶的網絡險／董責險限額基準正面臨重估；對同時在香港、內地與東南亞有業務的企業客戶，是一個具體、可操作的保單檢視切入點。",
     "跨市場客戶的網絡險／董責險限額基準正面臨重估；對同時在香港、內地與東南亞有業務的企業客戶，是一個具體、可操作的保單檢視切入點。"),
    ("向企業客戶提示跨境執法差異對保障的影響", "向企業客戶提示跨境執法差異對保障的影響"),
    ("網絡＋董責＋專業彌償三險限額聯合檢視", "網絡＋董責＋專業彌償三險限額聯合檢視"),
    ("團隊培訓：法規變化如何改寫限額充足性", "團隊培訓：法規變化如何改寫限額充足性"),
    ("大灣區／東南亞業務客戶的風險地圖更新", "大灣區／東南亞業務客戶的風險地圖更新"),
    (2, 2, 2, 2), ["reg", "product"], ["cyber", "reg", "compliance", "cross-border"],
    ["Aon", "亚太网络风险", "监管分歧", "董责险", "限额重估"],
    ("Insurance Asia／Aon 報告 2026-10-09 報道", "Insurance Asia／Aon 報告 2026-10-09 報道", "Insurance Asia",
     "2026-10-09"),
    "en", 70, "verified"))

# ══ 6. Insurance Asia：Markel 把能源核保人由倫敦調駐新加坡 ══
ITEMS.append(mk(
    "iaasia-markel-energy-underwriter-relocates-singapore-20261010",
    "insuranceasia", "media", "news",
    "2026-10-10",
    "https://insuranceasia.com/insurance/news/markel-moves-energy-underwriter-singapore",
    ("Insurance Asia：Markel把可持續能源及電力核保人由倫敦調駐新加坡",
     "Insurance Asia：Markel把可持續能源及電力核保人由倫敦調駐新加坡"),
    ("Insurance Asia 報道，Markel Insurance 委任 Rob Jones 為可持續能源及電力核保人（Sustainable Energy and Power Underwriter），並把他由倫敦調駐新加坡，以強化 Markel（Markel Group Inc. 旗下）在亞太區的能源核保業務。Jones 向高級能源核保人 Aminah Sulaiman 匯報，將負責推動亞太區可再生能源及電力組合的增長，並管理經紀與客戶關係；他擁有逾十年能源保險專業經驗，其中近六年任職於 Markel International 倫敦理賠部門。 [EN原文]",
     "Insurance Asia 報道，Markel Insurance 委任 Rob Jones 為可持續能源及電力核保人（Sustainable Energy and Power Underwriter），並把他由倫敦調駐新加坡，以強化 Markel（Markel Group Inc. 旗下）在亞太區的能源核保業務。Jones 向高級能源核保人 Aminah Sulaiman 匯報，將負責推動亞太區可再生能源及電力組合的增長，並管理經紀與客戶關係；他擁有逾十年能源保險專業經驗，其中近六年任職於 Markel International 倫敦理賠部門。 [EN原文]"),
    ("再保與專業險相繼把核保資源前移亞太，反映新能源與基建風險需求升溫；對有跨境基建、綠能或電力項目客戶的團隊，可用渠道與話語權同步增加。",
     "再保與專業險相繼把核保資源前移亞太，反映新能源與基建風險需求升溫；對有跨境基建、綠能或電力項目客戶的團隊，可用渠道與話語權同步增加。"),
    ("與高客談新能源／基建項目風險時的能力背書", "與高客談新能源／基建項目風險時的能力背書"),
    ("留意亞太能源承保能力與條件的變化", "留意亞太能源承保能力與條件的變化"),
    ("團隊分享：專業險核保重心東移的訊號", "團隊分享：專業險核保重心東移的訊號"),
    ("跨境基建項目保險安排的渠道更新", "跨境基建項目保險安排的渠道更新"),
    (2, 2, 2, 2), ["insurer", "market"], ["career", "firm", "esg"],
    ["Markel", "能源核保", "新加坡", "可再生能源", "亚太"],
    ("Insurance Asia 2026-10-10 報道", "Insurance Asia 2026-10-10 報道", "Insurance Asia", "2026-10-10"),
    "en", 60, "verified"))

# ══ 7. Insurance Asia／標普：太保香港資本獲母公司注資強化 ══
ITEMS.append(mk(
    "iaasia-sp-cpic-hk-capital-high-risk-assets-fall-20261002",
    "insuranceasia", "pro", "news",
    "2026-10-02",
    "https://insuranceasia.com/news/cpic-hong-kong-capital-strengthens-high-risk-assets-fall-39",
    ("Insurance Asia／標普：太保香港資本獲母公司注資強化　高風險資產佔比降至39%",
     "Insurance Asia／標普：太保香港資本獲母公司注資強化　高風險資產佔比降至39%"),
    ("Insurance Asia 引述標普全球評級（S&P Global Ratings）9月30日的評級評論指出，中國太平洋保險（香港）有限公司（CPIC HK）未來兩年可望維持較強資本與盈利，並在母集團中國太平洋財產保險（CPPIC）中維持策略重要性，即使其在港業務規模較小。標普稱母公司於2026年7月向 CPIC HK 注資15億港元，將有助其過渡至風險為本資本制度（RBC）並支持業務擴張；其資本緩衝相對標普 RBC 模型估算大致充足，但資本基礎規模偏小，面對單一大型事件風險的脆弱度可能高於假設。公司持續降低高風險資產曝險，佔總調整後資本比例由2023年的100%降至2025年底的39%，預期將繼續轉向投資級固定收益，以應付加速增長下的理賠流動性需求；標普同時提醒其海外業務擴張或帶來大型損失（如極端天氣）引起的承保波動，並預期公司將強化核保紀律、與母集團的保險利潤導向對齊。 [EN原文]",
     "Insurance Asia 引述標普全球評級（S&P Global Ratings）9月30日的評級評論指出，中國太平洋保險（香港）有限公司（CPIC HK）未來兩年可望維持較強資本與盈利，並在母集團中國太平洋財產保險（CPPIC）中維持策略重要性，即使其在港業務規模較小。標普稱母公司於2026年7月向 CPIC HK 注資15億港元，將有助其過渡至風險為本資本制度（RBC）並支持業務擴張；其資本緩衝相對標普 RBC 模型估算大致充足，但資本基礎規模偏小，面對單一大型事件風險的脆弱度可能高於假設。公司持續降低高風險資產曝險，佔其總調整後資本的比例由2023年的100%降至2025年底的39%，預期將繼續轉向投資級固定收益，以應付加速增長下的理賠流動性需求；標普同時提醒其海外業務擴張或帶來大型損失（如極端天氣）引起的承保波動，並預期公司將強化核保紀律、與母集團的保險利潤導向對齊。 [EN原文]"),
    ("在港中小型險企的 RBC 過渡與母公司注資路徑，是觀察香港風險為本資本制度落地節奏的具體個案；亦提醒資本規模較小機構的尾部風險與再保安排的重要性。",
     "在港中小型險企的 RBC 過渡與母公司注資路徑，是觀察香港風險為本資本制度落地節奏的具體個案；亦提醒資本規模較小機構的尾部風險與再保安排的重要性。"),
    ("向客戶說明險企資本與償付能力時的分層框架", "向客戶說明險企資本與償付能力時的分層框架"),
    ("代理產品盡職調查中納入評級與資本趨勢", "代理產品盡職調查中納入評級與資本趨勢"),
    ("團隊分享：RBC 下中小險企的資本策略", "團隊分享：RBC 下中小險企的資本策略"),
    ("內地母集團在港保險佈局的觀察個案", "內地母集團在港保險佈局的觀察個案"),
    (2, 2, 2, 3), ["insurer"], ["firm", "results", "reg"],
    ["太保香港", "CPIC HK", "标普", "RBC", "资本充足"],
    ("Insurance Asia／標普全球評級 2026-10-02 報道", "Insurance Asia／標普全球評級 2026-10-02 報道", "Insurance Asia",
     "2026-10-02", "評級評論日期為 2026-09-30"),
    "en", 68, "verified"))


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
