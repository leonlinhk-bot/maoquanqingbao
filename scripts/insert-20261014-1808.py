#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 2026-10-14 18:08 increment into live-items.json.

窗口：2026-10-14T02:11（上轮 last-check）→ 2026-10-14T18:08（本轮）。

本期新增 17 条：
  insuranceasianews 4（印度推兩項造船信用風險保險／蘇黎世委任中國業務CEO／日本內閣通過油輪
                      海運保險支援法案／供應鏈或有營業中斷「宿命感」）
  insuranceasia 3（滙豐人壽增設四個跨境醫療服務點／Nat Re 資本實力配合賠付改善／
                  壽險面對退休儲蓄模式轉變的競爭壓力）
  insurancebusinessmag 3（宏利企業級AI平台目標2027年10億美元價值／印尼擬收緊資本規則、
                           七成受評保險人未達2028年資本目標／穆迪：單靠信用保險不足以擴大
                           新興市場氣候融資）
  hkma 2（渝港跨境數據驗證平台投入運作／金融學院2027年度金融領袖計劃開始接受申請）
  fstb 2（財庫局歡迎首宗「側掛車」保險相連證券在港發行／香港與六國全面性避免雙重課稅
          協定命令刊憲）
  govhk 1（立法會十二題：2026年銀色債券）
  artemis 1（Calidris：傷亡類ILS須理解策略夥伴動機、時間表要現實）
  scmp 1（IMF 警告借貸成本上升正令公共財政受壓）

无新增信源：IA（監管通函最新仍為 2026-05-13；新聞稿頁為 JS 渲染、本輪主機不可達，
無法確認新增）、AIA HK、Manulife HK、Prudential HK、AXA HK、Sun Life HK（官網最新
分別為 2025-12-02 / 2026-10-10 / 無日期清單未變 / 2026-09-07 / 2026-10-02，均在本窗口前）、
HKFI（站點不可達）、SCMP 保險專題（最新保險相關報道為 2026-10-07）。

已按 substance 去重跳过：人保財險首宗側掛車（InsuranceAsia News 10-14 04:01 UTC 報道，
與財庫局官方稿同一事件，取官方稿）、Lloyd's Asia 加入 GAIP（Insurance Business 版本與
已收 2026-10-12 InsuranceAsia News 條目同一事件）、McLarens 區域理算師任命（人事、無實質）。

网络说明：本轮后半段代理隧道劣化（SSL EOF），部分正文未能取回，相关条目事实来源为
信源官網導語／標題，verifyStatus 標 pending。
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

# ══ 1. 印度推出兩項造船信用風險保險政策 ══
ITEMS.append(mk(
    "ian-india-shipbuilding-credit-risk-policies-20261014",
    "insuranceasianews", "pro", "news",
    "2026-10-14T17:29:38+08:00",
    "https://insuranceasianews.com/india-launches-pair-of-shipbuilding-credit-risk-insurance-policies/",
    "印度推出兩項造船信用風險保險　涵蓋出口及本地造船項目　政府提供保費補貼並直接支援保險人賠付",
    "InsuranceAsia News 於10月14日報道，印度推出兩項造船信用風險保險政策，分別涵蓋出口及本地造船項目；政府提供保費補貼，並就賠付向保險人提供直接支援。 [EN原文]",
    "造船業屬資本密集、履約週期長的行業，信用風險保險由政府補貼與兜底，是「政策性保險支撐戰略產業」的典型做法。對香港的參照在於：本地正推動船舶與海事保險專項市場，政策端如何以保費補貼與再保支援撬動商業承保，值得留意其邊界與定價邏輯。",
    "與客戶談信用風險保障時的區域案例",
    "政策性信用保險的補貼與兜底結構",
    "團隊分享：亞洲造船業保險政策",
    "香港海事及專項保險政策參照",
    (0, 2, 2, 2), ["product", "market"],
    ["credit-insurance", "marine", "policy", "trade", "india"],
    ["印度", "造船", "信用風險保險", "保費補貼", "出口信用"],
    ("InsuranceAsia News 2026-10-14 報道", "InsuranceAsia News", "2026-10-14",
     "EN原文；訂閱內容，事實來自官網導語"),
    "en", 62, "verified"))

# ══ 2. Calidris：傷亡類 ILS 動機與時間表 ══
ITEMS.append(mk(
    "artemis-casualty-ils-motivations-timelines-calidris-20261014",
    "artemis", "pro", "news",
    "2026-10-14T16:00:41+08:00",
    "https://www.artemis.bm/news/in-casualty-ils-motivations-are-key-timelines-must-be-realistic-trahan-calidris/",
    "Calidris：傷亡類 ILS 首重理解策略夥伴動機　時間表必須現實",
    "Artemis 於10月14日報道，專注保險投資的資產管理人 Calidris Investment Partners 聯合創辦人兼聯席行政總裁 Philippe Trahan 表示，傷亡類（casualty）保險相連證券交易結構複雜，須有高度一致性（alignment），因此尋找策略夥伴並理解其動機最為關鍵；同時，鑑於傷亡側掛車等安排的複雜度，設定現實可行的時間表同樣重要。 [EN原文]",
    "傷亡類 ILS 是2026年另類資本的主增長軸，但與財產巨災債的季度化節奏不同：結構複雜、估值與退出機制未成熟，故業界反覆強調「對齊動機」與「現實時間表」。對香港發展 ILS 生態的啟示是，制度設計不只要能發行，還要處理投資者與保薦人動機不一致、以及存續期長的資本終局性問題。",
    "客戶問 ILS 風險時的上游說明",
    "傷亡側掛車與財產巨災債的結構差異",
    "團隊簡報：傷亡類 ILS 的執行要點",
    "香港 ILS 生態的制度配套討論",
    (0, 2, 3, 2), ["market"],
    ["ils", "casualty", "sidecar", "reinsurance", "alternative-capital"],
    ["Calidris", "傷亡ILS", "側掛車", "另類資本", "策略夥伴"],
    ("Artemis.bm 2026-10-14 報道", "Artemis.bm", "2026-10-14", "EN原文；含原文導語與正文摘錄"),
    "en", 70, "verified"))

# ══ 3. 六份全面性避免雙重課稅協定命令刊憲 ══
ITEMS.append(mk(
    "fstb-six-cdta-orders-gazetted-20261014",
    "fstb", "official", "press",
    "2026-10-14T16:00:00+08:00",
    "https://www.info.gov.hk/gia/general/202610/14/P2026101400351.htm",
    "香港與六國全面性避免雙重課稅協定命令刊憲　10月21日提交立法會　累計已簽60個稅務管轄區",
    "香港特區政府於10月14日公布，行政長官會同行政會議已於10月6日根據《稅務條例》（第112章）作出六項命令，分別實施香港與巴巴多斯、約旦、吉爾吉斯共和國、馬爾代夫、挪威及盧旺達簽署的全面性避免雙重課稅協定。命令於10月16日刊憲，並於10月21日提交立法會進行先訂立後審議程序；六份協定將在香港與相關稅務管轄區各自完成批准程序後生效。財經事務及庫務局發言人表示，協定確保兩地居民無須為同一收入雙重課稅，並讓投資者更有效評估跨境經濟活動的潛在稅務負擔，促進雙邊貿易和投資。香港至今已與60個稅務管轄區簽訂協定，其中15份由現屆政府簽訂。",
    "稅務協定網絡是跨境財富與家族辦公室佈局的底層條件：雙重課稅風險直接影響保單架構、信託與控股公司選址。挪威屬新覆蓋的成熟市場，吉爾吉斯、巴巴多斯、約旦、馬爾代夫、盧旺達則補上新興市場拼圖。對前線的實務意義是，客戶問及資產跨境配置與稅務居民身份安排時，協定是否生效、何時生效是必須核對的事實項。",
    "客戶問跨境稅務安排時的核對要點",
    "雙重課稅協定與保單／信託架構基礎",
    "團隊簡報：香港稅務協定網絡更新",
    "家辦與高客跨境稅務佈局",
    (1, 2, 2, 2), ["family", "reg"],
    ["taxation", "double-taxation", "cross-border", "family-office", "hong-kong"],
    ["全面性避免雙重課稅協定", "刊憲", "挪威", "巴巴多斯", "跨境稅務"],
    ("香港特區政府新聞公報（財經事務及庫務局發稿）2026-10-14 16:00", "財經事務及庫務局", "2026-10-14", None),
    "zh", 84, "verified"))

# ══ 4. 渝港跨境數據驗證平台投入運作 ══
ITEMS.append(mk(
    "hkma-chongqing-hk-cross-boundary-data-validation-platform-20261014",
    "hkma", "official", "press",
    "2026-10-14T15:30:00+08:00",
    "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/10/20261014-4/",
    "金管局歡迎渝港跨境數據驗證平台投入運作　區塊鏈與數據代碼驗證、不涉數據原文件跨境傳輸",
    "重慶與香港於10月14日宣布渝港跨境數據驗證平台正式投入運作，是《行政長官2026年施政報告》中促進兩地金融要素有序流動的措施之一，由金管局與中國人民銀行重慶市分行、重慶市委金融委員會辦公室等共同協調構建。平台採用區塊鏈技術和數據代碼（hash values）驗證客戶自主攜帶的數據，過程中不涉及數據原文件的跨境傳輸和儲存；相關機制已應用於深港跨境數據驗證平台並證實穩定有效。首階段集中於跨境金融場景，兩地銀行正推進「北向」與「南向」雙向數據流與驗證案例，協助客戶辦理開立帳戶、申請貸款等銀行服務。金管局總裁余偉文表示，在「金融科技2030」策略下會持續構建新一代數據基建。目前深港平台使用次數已超過40,000次，協助超過10家銀行完成開戶、匯款及貸款所需的驗證，落地逾10類業務場景。",
    "跨境數據驗證是「客戶自主攜帶、可用不可見」的合規路徑：對保險業而言，核保、理賠、投保人身份與財務證明等場景都可沿用同一技術框架，且無須原文件過境，屬資料跨境傳輸合規與效率的平衡方案。深港平台逾4萬次使用與10家銀行落地，已具備可複製的實證；重慶加入後，西部客戶經港投保與理賠的數據摩擦有望下降。",
    "客戶問資料跨境合規時的技術路徑",
    "跨境數據驗證與核保理賠流程",
    "團隊簡報：跨境數據基建新進展",
    "大灣區及內陸城市客戶服務流程",
    (1, 3, 3, 3), ["tech", "reg"],
    ["cross-border", "data", "fintech", "hong-kong", "greater-bay-area"],
    ["渝港平台", "跨境數據驗證", "區塊鏈", "金管局", "余偉文", "金融科技2030"],
    ("香港金融管理局 2026-10-14 新聞稿（政府新聞公報同日發稿）", "香港金融管理局", "2026-10-14",
     "中英雙語；含余偉文發言"),
    "zh", 86, "verified"))

# ══ 5. 立法會十二題：2026年銀色債券 ══
ITEMS.append(mk(
    "govhk-legco-silver-bond-2026-qa-20261014",
    "govhk", "official", "press",
    "2026-10-14T14:27:00+08:00",
    "https://www.info.gov.hk/gia/general/202610/14/P2026101400250.htm",
    "立法會十二題：2026年銀色債券47.6萬份有效申請、認購近1,200億元　政府指銀債屬「投資選項」非退休入息保障",
    "財經事務及庫務局局長許正宇於10月14日回覆立法會提問時披露，2026年發行的銀色債券錄得逾47.6萬份有效申請，認購金額接近1,200億元，最終發行額由目標500億元提高至550億元。配發方面，最高配發上限為每位投資者100萬港元（100手）；認購12手或以下的88,422份申請全數獲配，餘下認購12手以上的388,281份申請先獲配12手，經抽籤後其中97,396份可多獲一手，即最多13手。政府在答覆中明確：銀色債券主要目的是募集資金用於工務工程，同時為年長市民提供穩健回報的投資選項，但「並不是為長者提供退休入息保障」，故不會就其在退休入息保障方面的作用作評估；並指政府另透過「銀色財務及保障安排」以退休理財產品、房屋按揭、投資者教育等協助年長市民規劃。",
    "政府對「銀債＝投資選項，非退休入息保障」的定性，是與客戶討論退休入息安排時的重要事實邊界：政府債券提供的是穩定票息與流動性，並不承擔長壽風險或保證終身給付，後者仍屬年金與保險產品的功能範圍。認購逾47.6萬份、超額逾一倍，亦反映本地長者對穩定收益工具的需求缺口。",
    "客戶把銀債與年金比較時的定位說明",
    "穩定收益工具與終身給付的功能分野",
    "團隊分享：長者理財需求與供給缺口",
    "退休入息方案的產品組合邏輯",
    (2, 2, 3, 2), ["market", "family"],
    ["retirement", "silver-bond", "retail-bond", "ageing", "hong-kong"],
    ["銀色債券", "退休入息", "立法會", "許正宇", "長者理財"],
    ("香港特區政府新聞公報（立法會答覆全文）2026-10-14 14:27", "香港特區政府新聞公報", "2026-10-14", None),
    "zh", 84, "verified"))

# ══ 6. 金融領袖計劃 2027 年度接受申請 ══
ITEMS.append(mk(
    "hkma-hk-academy-finance-financial-leaders-programme-2027-20261014",
    "hkma", "official", "press",
    "2026-10-14T12:00:00+08:00",
    "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/10/20261014-3/",
    "金融學院2027年度「金融領袖計劃」10月15日起接受申請　12月4日截止　保監局為支持監管機構之一",
    "香港金融學院宣布，2027年度「金融領袖計劃」將於10月15日開始接受報名，12月4日或之前截止。該計劃自2022年推出以來，在各香港金融監管機構（包括香港金融管理局、保險業監管局、強制性公積金計劃管理局及證券及期貨事務監察委員會）和參與機構支持下，已培育出逾100名未來金融領袖組成的活躍網絡。計劃以兼讀形式進行，專為來自不同專業背景、現職於行政總裁以下約一至兩個級別的優秀高級金融行政人員而設，提供與全球及本地傑出領袖直接對話、擴展跨行業專業網絡及提升戰略思維的機會。金管局總裁兼金融學院主席余偉文表示，未來金融領袖必須具備遠見、創新思維及堅實專業知識，並鼓勵高級金融行政人員參與或提名具潛質的候選人。",
    "對以培訓與人才複製為核心的團隊而言，這是與監管機構同一網絡的現成通道：計劃由四大監管機構共同支持，學員網絡跨銀行、保險、證券與強積金，適合有志走向管理層的高級行政人員。提名候選人本身亦是一種人才盤點動作，可配合年度梯隊規劃一同進行。",
    "客戶端接班人與人才規劃的外部資源",
    "高級行政人員培養路徑",
    "團隊人才梯隊與提名建議",
    "跨行業監管與業界網絡",
    (0, 1, 3, 2), ["reg", "market"],
    ["talent", "leadership", "hong-kong", "regulator", "training"],
    ["金融學院", "金融領袖計劃", "保監局", "余偉文", "人才培育"],
    ("香港金融管理局 2026-10-14 新聞稿（代金融學院發稿）", "香港金融管理局／金融學院", "2026-10-14",
     "中英雙語"),
    "zh", 82, "verified"))

# ══ 7. 穆迪：信用保險不足以擴大氣候融資 ══
ITEMS.append(mk(
    "ibm-moodys-credit-cover-emerging-market-climate-finance-593437-20261014",
    "insurancebusinessmag", "media", "news",
    "2026-10-14T11:12:28+08:00",
    "https://www.insurancebusinessmag.com/asia/news/breaking-news/credit-cover-alone-will-not-scale-emergingmarket-climate-finance-moodys-says-593437.aspx",
    "穆迪：單靠信用保險不足以擴大新興市場氣候融資　保險與保證僅佔優惠支持14%",
    "Insurance Business Asia 於10月14日報道，穆迪（Moody's）指出，單靠信用保險（credit cover）無法把新興市場氣候融資擴展至所需規模：保險與保證在優惠支持（concessional support）中僅佔約14%，而項目本身仍須具備可自行付費的能力（able to pay their own way）。 [EN原文]",
    "氣候與轉型融資的保障缺口，往往被簡化為「多買保險即可」，但穆迪點出關鍵前提——保險是風險轉移工具，不是資金來源，項目現金流與還本能力才是槓桿支點。對香港市場的參照是：討論綠色金融與氣候風險轉移時，須把信用增級、優惠資金與保險三者的分工講清楚，避免把保險當作萬能的信用替代。",
    "客戶問綠色／氣候項目保障時的邊界說明",
    "信用保險與信用增級的分工",
    "團隊分享：氣候融資的保障缺口",
    "轉型金融與風險轉移工具組合",
    (0, 2, 2, 2), ["market"],
    ["climate", "credit-insurance", "emerging-markets", "protection-gap", "sustainability"],
    ["穆迪", "信用保險", "氣候融資", "新興市場", "優惠支持"],
    ("Insurance Business Asia 2026-10-14 報道", "Insurance Business Asia", "2026-10-14",
     "EN原文；正文未及取回，事實來自官網導語"),
    "en", 68, "pending"))

# ══ 8. 宏利推企業級 AI 平台 ══
ITEMS.append(mk(
    "ibm-manulife-enterprise-ai-platform-1bn-2027-593434-20261014",
    "insurancebusinessmag", "media", "news",
    "2026-10-14T11:08:20+08:00",
    "https://www.insurancebusinessmag.com/asia/news/life-insurance/manulife-launches-enterprise-ai-platform-as-it-targets-1-billion-in-value-by-2027-593434.aspx",
    "宏利推企業級 AI 平台　目標2027年創造10億美元價值　已批核工具可跨市場重用（首個為美國人壽報價工具）",
    "Insurance Business Asia 於10月14日報道，宏利（Manulife）推出企業級人工智能平台，目標在2027年前創造10億美元價值；經批核的AI工具可在不同市場重複使用，首個落地案例為美國的人壽保險報價工具，用以加快初步核保（preliminary life underwriting）流程。 [EN原文]",
    "這是「AI 由單點試用走向平台化」的區域標杆做法：真正可複製的價值不在個別模型，而在批核機制＋可重用資產庫＋首個高頻環節（報價／初步核保）。與香港相關的是宏利香港已加入 IA「人工智能促進計劃」及 GenA.I. 沙盒++，其集團層面的平台化路線會直接影響本地前線可用的工具與合規邊界。",
    "客戶問 AI 核保可靠性時的機構案例",
    "AI 工具批核與跨市場重用機制",
    "團隊簡報：企業級 AI 的落地順序",
    "香港 GenA.I. 沙盒與集團平台的關係",
    (1, 3, 3, 2), ["tech", "insurer"],
    ["ai", "underwriting", "productivity", "insurer", "apac"],
    ["宏利", "企業AI平台", "人壽報價", "初步核保", "10億美元"],
    ("Insurance Business Asia 2026-10-14 報道", "Insurance Business Asia", "2026-10-14",
     "EN原文；正文未及取回，事實來自官網導語"),
    "en", 76, "pending"))

# ══ 9. 財庫局歡迎首宗「側掛車」ILS 在港發行 ══
ITEMS.append(mk(
    "fstb-hk-first-sidecar-ils-picc-20261014",
    "fstb", "official", "press",
    "2026-10-14T11:00:00+08:00",
    "https://www.info.gov.hk/gia/general/202610/14/P2026101300435.htm",
    "財庫局歡迎首宗「側掛車」保險相連證券在港發行　人保財險以1,200萬美元為海上風電保險提供比例再保　累計 ILS 發行約63億港元",
    "財經事務及庫務局於10月14日歡迎中國人民財產保險股份有限公司（人保財險）在香港發行首宗「側掛車」（sidecar）形式的保險相連證券，發行總額1,200萬美元（約9,400萬港元），以比例再保險方式為中國內地的海上風電保險業務提供保障。財庫局局長許正宇表示，《香港第一個五年規劃》提出充分運用國際保險、再保險及資本市場比較優勢，推動傳統保險與非傳統風險管理工具協同發展；他指當局與保險業監管局將繼續推廣保險相連證券、縮窄巨災及其他專項風險保障缺口，並會檢視投資者限制以激活保險相連證券基金交易市場，同時研究修改法例引入「受保護單元公司」（PCC）以降低發行成本。許正宇補充，保險相連證券加上專屬自保保險，可為「出海」企業提供多元化風險管理途徑。香港自2021年建立 ILS 專屬規管制度並推出資助先導計劃，至今促成七宗巨災債券及一宗「側掛車」，總發行額約63億港元；國家金融監督管理總局2025年9月發布通知，支持內地保險公司來港發行「側掛車」保險連接證券。",
    "這是香港 ILS 市場的結構性里程碑：首宗「側掛車」落地，且首度以海上風電（能源轉型資產）為標的，說明制度已由巨災債券單一形態擴展至專項風險與比例再保結構。政策端的兩條後續線索值得追蹤——檢視投資者限制以激活 ILS 基金交易市場、以及修例引入 PCC 降低成本，兩者一旦落實，將直接改變香港作為區域風險管理樞紐的成本結構。",
    "客戶問另類風險轉移工具時的官方定位",
    "側掛車結構與比例再保基礎",
    "團隊簡報：香港 ILS 政策與發行進展",
    "出海企業風險管理工具箱",
    (2, 3, 4, 3), ["reg", "market", "product"],
    ["ils", "sidecar", "alternative-capital", "hong-kong", "risk-transfer", "renewable"],
    ["側掛車", "人保財險", "保險相連證券", "巨災債券", "許正宇", "海上風電", "受保護單元公司"],
    ("香港特區政府新聞公報（財經事務及庫務局發稿）2026-10-14 11:00", "財經事務及庫務局", "2026-10-14", None),
    "zh", 92, "verified"))

# ══ 10. 蘇黎世委任中國業務 CEO ══
ITEMS.append(mk(
    "ian-zurich-scott-yin-china-ceo-20261014",
    "insuranceasianews", "pro", "news",
    "2026-10-14T10:17:45+08:00",
    "https://insuranceasianews.com/zurich-taps-scott-yin-as-china-unit-ceo/",
    "蘇黎世委任 Scott Yin 為中國業務行政總裁　此前於安盛天平任職逾十年",
    "InsuranceAsia News 於10月14日報道，蘇黎世（Zurich）委任 Scott Yin 出任其中國業務行政總裁；他此前在安盛天平（Axa Tianping）任職逾十年。 [EN原文]",
    "內地產壽險管理層的人才流動，是觀察外資保險集團中國戰略調整的先行指標。蘇黎世同期亦委任香港首席財務官 Martin Noble 兼任大中華區 CFO（10月13日），兩項任命同週公布，指向大中華區管理架構的整合。對前線的意義在於，區域管理層更替常伴隨渠道與產品策略微調，跨境業務對接窗口可能隨之變化。",
    "客戶問外資保險集團佈局時的背景",
    "大中華區管理架構整合的觀察點",
    "團隊分享：外資集團人事變動信號",
    "中港兩地業務對接窗口",
    (0, 1, 2, 2), ["insurer", "market"],
    ["talent", "insurer", "china", "leadership", "apac"],
    ["蘇黎世", "Scott Yin", "中國業務", "安盛天平", "人事任命"],
    ("InsuranceAsia News 2026-10-14 報道", "InsuranceAsia News", "2026-10-14",
     "EN原文；訂閱內容，事實來自官網導語"),
    "en", 62, "verified"))

# ══ 11. SCMP：IMF 警告借貸成本上升令公共財政受壓 ══
ITEMS.append(mk(
    "scmp-imf-higher-borrowing-costs-public-finances-20261014",
    "scmp", "media", "news",
    "2026-10-14T10:00:00+08:00",
    "https://www.scmp.com/business/banking-finance/article/3370722/imf-warns-higher-borrowing-costs-are-straining-public-finances-worldwide",
    "IMF 警告借貸成本上升正令全球公共財政承壓　與年會前政策討論同步",
    "《南華早報》10月14日報道，國際貨幣基金組織（IMF）警告借貸成本上升正令全球公共財政承受壓力。本報同日的政府公告顯示，財政司司長陳茂波將於10月15日至17日以中國代表團成員身分出席 IMF 及世界銀行集團年會，議程包括環球經濟前景、金融穩定，以及如何動員私人資本支持基建投資與可持續增長。 [EN原文；正文未及取回，事實為標題級，另配合政府公告作背景]",
    "主權與公共財政壓力是保險人資產端的系統性變數：政府債券收益率曲線、主權評級與財政可持續性，直接影響長年期保單的資產配置與折現假設。IMF 年會期間關於私人資本動員的討論，亦與保險資金作為長期資本的定位相關，值得在週度宏觀簡報中跟進。",
    "客戶問長期回報與利率環境時的宏觀背景",
    "主權風險與保險資金配置基礎",
    "團隊簡報：IMF 年會的保險相關議程",
    "私人資本動員與長期資金供給",
    (0, 2, 2, 2), ["market"],
    ["macro", "interest-rate", "sovereign-risk", "public-finance", "imf"],
    ["IMF", "借貸成本", "公共財政", "陳茂波", "世銀年會"],
    ("南華早報 2026-10-14 報道", "South China Morning Post", "2026-10-14",
     "EN原文；正文未及取回，事實為標題級"),
    "en", 60, "pending"))

# ══ 12. 日本內閣通過油輪海運保險支援法案 ══
ITEMS.append(mk(
    "ian-japan-cabinet-marine-insurance-oil-vessels-20261014",
    "insuranceasianews", "pro", "news",
    "2026-10-14T08:03:16+08:00",
    "https://insuranceasianews.com/japans-cabinet-approves-bill-to-support-marine-insurance-covers-for-oil-vessels/",
    "日本內閣通過法案　以政府支援強化油輪海運保險保障　屬能源供應安全三法案之一",
    "InsuranceAsia News 於10月14日報道，日本內閣通過法案，以政府支援方式強化油輪的海運保險保障。報道指這是內閣為應對中東衝突、加強能源供應安全而通過的三項法案之一。 [EN原文]",
    "戰爭與地緣風險令海運保險的商業承保能力收縮，政府介入成為維持能源運輸的必要條件。這是「國家安全風險商業不可承保時，主權如何補位」的現實案例，與香港發展專項保險與再保中心的定位直接相關——專項風險的政策性支持結構，往往是市場能否成形的關鍵。",
    "客戶問戰爭／地緣風險保障時的區域案例",
    "政策性風險支持結構基礎",
    "團隊分享：能源運輸與地緣風險",
    "香港專項保險與再保中心定位",
    (0, 2, 2, 2), ["product", "reg"],
    ["marine", "war-risk", "energy", "policy", "japan"],
    ["日本", "油輪", "海運保險", "能源安全", "內閣法案"],
    ("InsuranceAsia News 2026-10-14 報道", "InsuranceAsia News", "2026-10-14",
     "EN原文；訂閱內容，事實來自官網導語"),
    "en", 66, "verified"))

# ══ 13. 供應鏈或有營業中斷：市場瀰漫「宿命感」 ══
ITEMS.append(mk(
    "ian-supply-chain-cbi-fatalism-basi-20261014",
    "insuranceasianews", "pro", "news",
    "2026-10-14T07:30:08+08:00",
    "https://insuranceasianews.com/sense-of-fatalism-abounds-over-assessment-of-impact-of-conflict-on-supply-chains/",
    "供應鏈或有營業中斷：市場瀰漫「宿命感」　Russell Group 指難以為製造網絡與金融傳導風險定價",
    "InsuranceAsia News 於10月14日報道，Russell Group 的 Suki Basi 指出，面對衝突對供應鏈的影響，市場瀰漫一種「宿命感」：業界在供應鏈或有營業中斷（contingent business interruption, CBI）的產品創新上舉步維艱，亦難以量化製造網絡風險與金融傳染風險。 [EN原文]",
    "CBI 是全球產險最難定價的環節之一：保額與觸發條件難以界定，損失具有跨保單、跨組合的累積性。這與同日 Insurance Business 關於數據中心累積風險的報道同源——供應鏈與共享基礎設施令傳統單一標的承保邏輯失效。對香港的實務意義在於，企業客的營運中斷保障缺口往往不在「有沒有買」，而在「買了能否觸發」。",
    "客戶問營運中斷保障範圍時的實務提醒",
    "CBI 觸發條件與定價難點",
    "團隊分享：供應鏈風險的不可保邊界",
    "跨保單累積風險的識別",
    (1, 3, 2, 3), ["product", "market"],
    ["supply-chain", "business-interruption", "catastrophe", "pricing", "protection-gap"],
    ["供應鏈", "或有營業中斷", "CBI", "Russell Group", "傳染風險"],
    ("InsuranceAsia News 2026-10-14 報道", "InsuranceAsia News", "2026-10-14",
     "EN原文；訂閱內容，事實來自官網導語"),
    "en", 65, "verified"))

# ══ 14. Nat Re：資本實力配合賠付改善 ══
ITEMS.append(mk(
    "iaasia-nat-re-capital-underwriting-volumes-20261014",
    "insuranceasia", "media", "news",
    "2026-10-14T06:00:00+08:00",
    "https://insuranceasia.com/insurance/news/nat-res-capital-strength-opens-door-higher-underwriting-volumes",
    "Nat Re：資本實力配合賠付改善　為非壽險提高承保量打開空間",
    "Insurance Asia 於10月14日報道，菲律賓國家再保險公司（Nat Re）的資本實力，配合優於預期的賠付發展（better-than-expected claims developments），帶動2025年非壽險板塊業績改善，並為提高承保量打開空間。 [EN原文]",
    "東南亞本土再保人的資本與承保能力，是區域分出業務的重要承接方：賠付經驗改善→資本充足→承保量提升，這條鏈條決定了本地保險人分保成本與可得性。對香港的觀察價值在於，區域再保梯隊的健康度，會影響跨境專項風險的分出與定價。",
    "客戶問再保承接與分保成本時的區域背景",
    "再保資本與承保週期的關聯",
    "團隊分享：東南亞再保市場動態",
    "區域風險分出與定價",
    (0, 2, 2, 2), ["market", "insurer"],
    ["reinsurance", "capital", "claims", "asean", "underwriting"],
    ["Nat Re", "菲律賓", "再保險", "資本實力", "承保量"],
    ("Insurance Asia 2026-10-14 報道", "Insurance Asia", "2026-10-14",
     "EN原文；正文未及取回，事實來自官網導語"),
    "en", 64, "pending"))

# ══ 15. 滙豐人壽擴展跨境醫療服務 ══
ITEMS.append(mk(
    "iaasia-hsbc-life-cross-border-healthcare-lounges-20261014",
    "insuranceasia", "media", "news",
    "2026-10-14T05:45:00+08:00",
    "https://insuranceasia.com/insurance/news/hsbc-life-expands-cross-border-healthcare-four-new-lounges",
    "滙豐人壽擴展跨境醫療服務　增設四個服務點　港陸保單持有人可用預約及陪診服務",
    "Insurance Asia 於10月14日報道，滙豐人壽（HSBC Life）擴展跨境醫療服務，增設四個服務點（lounges）；香港及中國內地的保單持有人可使用預約及醫療陪診（medical escort）服務。 [EN原文]",
    "跨境醫療服務正由「醫院網絡覆蓋」競爭，延伸至「服務節點＋就醫陪同」的體驗競爭：這直接對應港人與內地客戶雙向就醫的高頻痛點——掛號、陪診、流程協助。對前線的意義是，醫療保障的差異化已不在保額，而在服務能否落地；此類節點數量與位置，可作為客戶比較方案時的具體依據。",
    "客戶比較醫療保障服務時的具體依據",
    "跨境醫療服務網絡與節點設計",
    "團隊分享：跨境醫療體驗競爭",
    "大灣區醫療服務落地安排",
    (2, 2, 2, 3), ["product", "insurer"],
    ["health", "cross-border", "medical-network", "greater-bay-area", "customer-service"],
    ["滙豐人壽", "跨境醫療", "陪診服務", "服務點", "大灣區"],
    ("Insurance Asia 2026-10-14 報道", "Insurance Asia", "2026-10-14",
     "EN原文；正文未及取回，事實來自官網導語"),
    "en", 72, "pending"))

# ══ 16. 壽險面對退休儲蓄模式轉變 ══
ITEMS.append(mk(
    "iaasia-life-insurers-retirement-savings-shift-20261014",
    "insuranceasia", "media", "news",
    "2026-10-14T05:00:00+08:00",
    "https://insuranceasia.com/insurance/in-focus/life-insurers-face-pressure-retirement-savings-shift",
    "壽險面對退休儲蓄模式轉變的競爭壓力　個人自負退休責任推升產品與理財建議需求",
    "Insurance Asia 於10月14日報道，隨著更多人自行承擔退休儲蓄的管理責任，壽險公司面對日益激烈的競爭；同時，市場對保險產品及理財建議的需求上升。 [EN原文]",
    "「個人自負退休責任」是滲透率見頂後市場的核心敘事：客戶不是不需要保險，而是需要能與資產累積、收入提取、傳承銜接的整合方案。這解釋了為何壽險與資產管理、退休平台的邊界正在模糊，也說明前線的專業價值正由產品銷售轉向規劃與建議能力。",
    "客戶談退休規劃時的市場背景",
    "退休儲蓄模式轉變與產品供給",
    "團隊分享：壽險角色由給付者轉向規劃者",
    "退休與財富管理整合趨勢",
    (2, 3, 3, 2), ["market", "family"],
    ["retirement", "savings", "wealth-management", "life-insurance", "advisory"],
    ["退休儲蓄", "壽險競爭", "理財建議", "個人責任", "亞洲市場"],
    ("Insurance Asia 2026-10-14 報道", "Insurance Asia", "2026-10-14",
     "EN原文；正文未及取回，事實來自官網導語"),
    "en", 66, "pending"))

# ══ 17. 印尼擬收緊資本規則 ══
ITEMS.append(mk(
    "ibm-indonesia-draft-capital-rules-specialty-lines-593358-20261014",
    "insurancebusinessmag", "media", "news",
    "2026-10-14T03:07:49+08:00",
    "https://www.insurancebusinessmag.com/asia/news/breaking-news/indonesias-draft-capital-rules-would-restrict-smaller-insurers-credit-and-specialty-lines-593358.aspx",
    "印尼擬收緊資本規則　惠譽評級保險人七成未達2028年資本目標　小型保險人或失信用險業務及船體、航空、能源自留上限",
    "Insurance Business Asia 於10月14日報道，印尼擬議的資本規則將限制小型保險人的信用險（credit）及專項（specialty）業務：在惠譽（Fitch）評級的保險人中，約七成未達2028年的資本目標；資本較低的保險人可能失去信用險額度，並面對船體（hull）、航空及能源業務的自留上限。 [EN原文]",
    "新興市場以資本規則約束高波動專項業務，是「承保能力與資本匹配」的監管落點。七成未達標的比例說明當地市場將出現明顯的整合與增資壓力，並為區域再保與專項承保人騰出分出空間。與香港的關聯在於：區內專項風險的承接路徑會隨收緊而轉移，值得在亞洲市場週報中追蹤。",
    "客戶問區域專項承保能力時的背景",
    "資本規則與專項業務承保能力",
    "團隊分享：東南亞資本監管收緊",
    "區域專項風險承接路徑變化",
    (0, 2, 2, 2), ["reg", "market"],
    ["capital", "solvency", "credit-insurance", "specialty", "asean"],
    ["印尼", "資本規則", "惠譽", "信用險", "航空保險", "自留上限"],
    ("Insurance Business Asia 2026-10-14 報道", "Insurance Business Asia", "2026-10-14",
     "EN原文；正文未及取回，事實來自官網導語"),
    "en", 70, "pending"))

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
