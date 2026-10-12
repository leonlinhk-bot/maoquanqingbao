#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 2026-10-12 18:1x increment into live-items.json.

窗口：2026-10-12T00:27（凌晨轮）→ 2026-10-12T18:18。
本期新增 17 条：
  insuranceasianews 6（FWD 入股 bolttech HK、日本自保制度、Lloyd's Asia 加入 GAIP、
    印尼 RBC/惠誉、The Hartford 新加坡能源险、Nat Re AM Best）
  insuranceasia 6（GlobalData AI 应用调查、Mox×QBE 数码家居险、台湾外币保单+39%、
    日本寿险 4-7 月新造、Tune Protect×Airpaz 三地、GIC Re AM Best）
  scmp 2（T. Rowe Price AI 退休调查、前滙豐高管 AI 代理财富平台）
  artemis 2（Sage Advisory ILS 分散效果、Pillar Capital 获 SageSure 策略投资）
  manulife 1（补漏：10-10 世界精神健康日「My旗日」）
无新发布信源：IA（通函最新 2026-10-02；新闻稿页无新）、HKMA（最新 2026-10-09）、
  NFRA（最新为 10-09《财产保险公司保险产品开发管理规定》）、HKFI、FSTB、
  AIA（最新 10-09，已收录）、Prudential HK（新闻室列表无新）、AXA、Sun Life、
  Insurance Business（最新 10-10，已收录）。
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


def TC(x):
    s = x[0] if isinstance(x, (tuple, list)) else x
    return T(s)


def mk(id_, sourceKey, tier, kind, pub, url, t, s, w, a_f, a_m, a_l, a_c, ri, boards, themes,
       tags, src, lang, score, verify='pending'):
    return {
        "clusterCount": 1, "score": score, "verifyStatus": verify,
        "sourceTier": tier, "sourceKey": sourceKey, "contentKind": kind,
        "actions": {
            "front": {"sc": a_f[0] if isinstance(a_f, (tuple, list)) else a_f, "tc": TC(a_f)},
            "midback": {"sc": a_m[0] if isinstance(a_m, (tuple, list)) else a_m, "tc": TC(a_m)},
            "lead": {"sc": a_l[0] if isinstance(a_l, (tuple, list)) else a_l, "tc": TC(a_l)},
            "cross": {"sc": a_c[0] if isinstance(a_c, (tuple, list)) else a_c, "tc": TC(a_c)},
        },
        "rolesImpact": {"front": ri[0], "midback": ri[1], "lead": ri[2], "cross": ri[3]},
        "boards": boards, "themes": themes,
        "tags": {"sc": tags, "tc": [T(x) for x in tags]},
        "contentRole": CR, "featured": False, "evergreen": False, "ingestedAt": NOW,
        "id": id_, "publishedAt": pub, "originalUrl": url,
        "title": {"sc": t, "tc": T(t)},
        "summary": {"sc": s, "tc": T(s)},
        "why": {"sc": w, "tc": T(w)},
        "source": {"sc": src[0], "tc": T(src[0]), "lang": lang, "name": src[2],
                   "date": src[3], "note": src[4] if len(src) > 4 else None},
    }


ITEMS = []

# ══ 1. 富衛收購 bolttech Insurance（香港）25% 股權，重返一般保險市場 ══
ITEMS.append(mk(
    "ian-fwd-bolttech-hk-pc-25pct-21m-20261012",
    "insuranceasianews", "media", "news",
    "2026-10-12T11:27:00+08:00",
    "https://insuranceasianews.com/fwd-to-acquire-25-of-hong-kong-pc-carrier-bolttech-insurance-for-us21m/",
    "富衛以2,072萬美元收購bolttech Insurance（香港）25%股權　時隔六年重返一般保險市場",
    "InsuranceAsia News 10月12日報道：港交所上市的富衛集團（FWD Group）同意以基礎代價2,072萬美元（約1.6億港元）收購bolttech Insurance (Hong Kong) 25%股權，交易標的即富衛於2020年剝離、賣給bolttech的前富衛一般保險（FWD General Insurance），富衛由此重返香港一般保險（P&C）市場。 [EN原文]",
    "香港龍頭壽險集團重新配置一般保險資產，屬本地市場結構訊號：①一般保險（家居、旅遊、意外、醫療附加）長期是壽險顧問交叉銷售與客戶黏著的入口，集團股權動作往往先於渠道政策變化；②與黃岡口岸車險／勞保強制承保擴大、大灣區跨境用車等近期事項一併看，可理解為「壽險打底、一般險補位」的客戶服務策略延續。",
    "與團隊分享：本地一般保險市場股權變動與渠道意義",
    "交叉銷售切入點：家居／旅遊／意外險的客戶覆蓋",
    "客戶提問應對：富衛品牌與bolttech關係的準確表述",
    "集團戰略對照：壽險＋一般險的客戶服務閉環",
    (2, 2, 2, 1), ["insurer", "market"], ["ma", "insurer", "hong-kong", "channel"],
    ["富卫", "bolttech", "一般保险", "股权收购", "香港市场"],
    ("InsuranceAsia News 2026-10-12 报道", "InsuranceAsia News 2026-10-12 報道",
     "InsuranceAsia News", "2026-10-12", "EN原文；基础代价 2,072 万美元，取得 25% 股权"),
    "en", 68, "verified"))

# ══ 2. 日本金融厅研究建立本土再保险自保制度 ══
ITEMS.append(mk(
    "ian-japan-domestic-reinsurance-captive-regime-20261012",
    "insuranceasianews", "media", "news",
    "2026-10-12T14:08:51+08:00",
    "https://insuranceasianews.com/japan-moves-to-create-domestic-reinsurance-captive-regime/",
    "日本金融廳啟動審議　擬建立本土再保險型專屬自保（captive）制度　2027年1月提交法案",
    "InsuranceAsia News 10月12日報道：日本金融廳（FSA）已就建立本土「再保險型專屬自保」（reinsurance captive，承接有限風險）制度展開正式審議，首次會議的說明材料顯示，政府計劃在2027年1月召開的例行國會提交相關法案。 [EN原文]",
    "亞洲專屬自保（captive）制度供給持續增加，與香港近年力推自保及再保險樞紐的政策成直接對照。對前線的實用價值在於：企業客戶（尤其跨境集團）談風險自留、專屬自保與再保安排時，香港的定位、稅務與監管優勢需要以區域競爭格局來表述，而非單點介紹。",
    "與企業客／管理層對談：專屬自保的區域選擇",
    "市場趨勢觀察：亞洲自保與再保樞紐競爭",
    "團隊知識補強：captive 基本架構與適用場景",
    "與香港自保政策（IA/HKFI 推廣）的對照",
    (1, 2, 3, 2), ["reg", "market"], ["captive", "reg", "apac", "reinsurance"],
    ["日本金融厅", "专属自保", "captive", "再保险", "区域枢纽"],
    ("InsuranceAsia News 2026-10-12 报道", "InsuranceAsia News 2026-10-12 報道",
     "InsuranceAsia News", "2026-10-12", "EN原文；法案拟 2027 年 1 月例行国会提交"),
    "en", 66, "verified"))

# ══ 3. Lloyd's Asia 加入 GAIP 成为支持伙伴 ══
ITEMS.append(mk(
    "ian-lloyds-asia-gaip-supporting-partner-20261012",
    "insuranceasianews", "media", "news",
    "2026-10-12T15:18:35+08:00",
    "https://insuranceasianews.com/lloyds-asia-joins-gaip-as-supporting-partner/",
    "Lloyd's Asia加入全球亞洲保險合作夥伴（GAIP）成為支持夥伴　聚焦保障缺口與複雜風險",
    "InsuranceAsia News 10月12日報道：Lloyd's Asia將以支持夥伴（supporting partner）身份加入全球亞洲保險合作夥伴（GAIP），為這個由監管機構、業界與學術界組成的三方平台提供專門（再）保險市場視角，協助應對亞洲的保障缺口並提升對複雜、演變中風險的韌性。 [EN原文]",
    "GAIP 是亞太區少數由政府、監管機構與業界共同參與的保障缺口研究平台（其產出常用於區域保障缺口與產品創新討論）。Lloyd's 以香港為亞洲樞紐參與，屬香港作為區域風險與再保中心地位的訊號；相關研究日後可作為與高客／企業客討論保障缺口與創新風險轉移方案的公開權威引用。",
    "高客溝通素材：區域保障缺口與風險轉移",
    "行業參與觀察：香港作為區域保險樞紐",
    "團隊分享：複雜風險（網絡、氣候）的市場供給",
    "公開引用源整理（GAIP 研究報告）",
    (1, 2, 2, 2), ["market", "insurer"], ["apac", "protection-gap", "firm", "reinsurance"],
    ["Lloyd's Asia", "GAIP", "保障缺口", "区域平台", "香港枢纽"],
    ("InsuranceAsia News 2026-10-12 报道", "InsuranceAsia News 2026-10-12 報道",
     "InsuranceAsia News", "2026-10-12", "EN原文"),
    "en", 62, "verified"))

# ══ 4. 惠誉：印尼更严偿付能力要求推动增资与整合 ══
ITEMS.append(mk(
    "ian-indonesia-solvency-rbc-consolidation-fitch-20261012",
    "insuranceasianews", "media", "news",
    "2026-10-12T10:15:25+08:00",
    "https://insuranceasianews.com/indonesian-solvency-rules-to-drive-consolidation-capital-raising-fitch/",
    "惠譽：印尼分階段收緊資本要求　未來兩年推動保險業增資與併購（2027年實施RBC制度）",
    "InsuranceAsia News 10月12日報道：惠譽評級（Fitch Ratings）指出，印尼保險業分階段引入更嚴格的資本要求，將在未來兩年引發大規模增資與整合；當地保險公司同時面對2027年落實風險為本資本（RBC）制度的壓力。 [EN原文]",
    "亞洲多個市場同步走向風險為本資本制度（香港 RBC 亦在推進），「監管資本要求→增資／併購→產品與定價取向變化」是可重複使用的分析框架。用於向團隊說明：客戶關心的公司償付能力與產品長期承諾，最終由資本制度與股東注資能力決定，而非單一產品條款。",
    "團隊知識補強：RBC 制度與保險公司償付能力",
    "客戶溝通素材：公司資本實力如何看",
    "市場趨勢觀察：亞洲保險業整合潮",
    "與香港 RBC 推進節奏的對照",
    (1, 2, 2, 2), ["reg", "market"], ["capital", "reg", "apac", "ma"],
    ["惠誉", "印尼", "RBC", "偿付能力", "并购整合"],
    ("InsuranceAsia News 2026-10-12 报道", "InsuranceAsia News 2026-10-12 報道",
     "InsuranceAsia News", "2026-10-12", "EN原文；RBC 拟 2027 年实施"),
    "en", 66, "verified"))

# ══ 5. The Hartford 瞄准亚太增长，新加坡能源险 2027 Q1 上线 ══
ITEMS.append(mk(
    "ian-hartford-singapore-energy-launch-2027-20261012",
    "insuranceasianews", "media", "news",
    "2026-10-12T07:30:32+08:00",
    "https://insuranceasianews.com/the-hartford-targets-apac-growth-with-singapore-energy-launch-in-q1-2027/",
    "The Hartford瞄準亞太增長　2027年首季於新加坡推出能源保險並推自動化報價工具",
    "InsuranceAsia News 10月12日報道：美國保險集團The Hartford國際業務主管Carl Bach表示，集團在所涉亞太各市場均見「充裕機會」，將持續擴展專門險種能力並推出自動化報價工具；能源保險業務預計2027年第一季在新加坡啟動。 [EN原文]",
    "區域專門險種（能源、工程、海運）供給與自動化報價是兩個可觀察方向：①跨國承保能力回流亞太，對香港企業客的風險轉移選擇有間接影響；②自動化報價工具是承保效率的實務議題，可與團隊討論「哪些環節適合自動化、哪些必須人手判斷」。",
    "與企業客談風險轉移時的區域承保供給",
    "團隊分享：自動化報價對承保與服務的影響",
    "市場趨勢觀察：跨國險企亞太佈局",
    "與香港專門險種市場供給的對照",
    (1, 1, 1, 2), ["insurer", "market"], ["apac", "firm", "distribution", "uw"],
    ["The Hartford", "新加坡", "能源保险", "亚太扩张", "自动报价"],
    ("InsuranceAsia News 2026-10-12 报道", "InsuranceAsia News 2026-10-12 報道",
     "InsuranceAsia News", "2026-10-12", "EN原文"),
    "en", 60, "verified"))

# ══ 6. AM Best：Nat Re 承保表现改善，维持 B++ ══
ITEMS.append(mk(
    "ian-nat-re-am-best-underwriting-improves-20261012",
    "insuranceasianews", "media", "news",
    "2026-10-12T09:35:38+08:00",
    "https://insuranceasianews.com/nat-res-underwriting-performance-improves-on-non-life-claims-development-life-margins-am-best/",
    "AM Best：菲律賓再保險公司Nat Re承保表現改善　維持B++（良好）評級、展望穩定",
    "InsuranceAsia News 10月12日報道：評級機構AM Best指菲律賓再保險公司Nat Re（National Reinsurance Corporation of the Philippines）受惠於非壽險理賠發展及壽險業務利潤率改善，承保表現提升，維持其B++（良好）財務實力評級及穩定展望。 [EN原文]",
    "再保險人評級變動是下游保司資本與分出安排的先行指標；東南亞再保市場的承保週期亦影響區域價格。適合放入「客戶問及保司穩健性時，專業上應看什麼」的清單：評級機構最新意見、承保表現、資本充足度，而非只看品牌或規模。",
    "團隊知識補強：再保險人評級與分出安排",
    "客戶提問應對：如何解讀評級與展望",
    "市場趨勢觀察：東南亞再保週期",
    "公開引用源整理（AM Best 區域評級）",
    (1, 1, 1, 2), ["insurer"], ["reinsurance", "results", "apac", "capital"],
    ["Nat Re", "AM Best", "评级", "再保险", "菲律宾"],
    ("InsuranceAsia News 2026-10-12 报道", "InsuranceAsia News 2026-10-12 報道",
     "InsuranceAsia News", "2026-10-12", "EN原文；评级 B++（good）展望稳定"),
    "en", 60, "verified"))

# ══ 7. GlobalData：保险业 AI 投资重心从核保转向产品开发 ══
ITEMS.append(mk(
    "iaasia-ai-spending-beyond-underwriting-globaldata-20261012",
    "insuranceasia", "pro", "report",
    "2026-10-12T09:30:00+08:00",
    "https://insuranceasia.com/insurance/expert-opinion/can-insurers-turn-ai-spending-gains-beyond-underwriting",
    "GlobalData調查：保險業AI應用重心由核保擴散至產品開發　產品開發佔比升8.9個百分點",
    "Insurance Asia 10月12日報道：GlobalData調查（2026年4月15日至7月22日）顯示，34.4%受訪者預期核保及風險評估最能受惠於AI，其次客戶服務20.4%、理賠管理18.3%、產品開發16.1%、市場推廣及分銷10.8%。核保仍居首，但佔比較2025年7月下跌11.4個百分點；產品開發升幅最大（+8.9個百分點）。報道引述Fortune Business Insights估算，全球保險AI市場2025年104億美元，今年將達135億美元，2034年1,544億美元（年複合增長35.7%）；亞太2025年28億美元（中國7.1億、印度5.8億），區內增速42.2%。 [EN原文]",
    "直接對應「IFA AI賦能」主線：AI在保險業的價值正由核保（公司內部效率）擴散至產品開發與客戶互動（前線可感知），說明「AI工具＝銷售輔助」的定位正在被推前。可用於設計團隊AI工作流的取捨：先做甚麼（會議紀錄、文件、客戶互動）、後做甚麼（產品比較、方案生成），避免一上手就追求全流程自動化。",
    "團隊AI工作流優先次序設計（先客戶互動、後自動化）",
    "新人培育：AI輔助客戶溝通與方案說明的邊界",
    "客戶溝通素材：數碼化服務體驗的行業趨勢",
    "對標工具選型：顧問端AI產品形態與市場增速",
    (3, 3, 3, 2), ["tech"], ["ai", "tech", "insurtech", "product"],
    ["GlobalData", "AI应用", "产品开发", "核保", "保险科技"],
    ("Insurance Asia 2026-10-12 报道（引 GlobalData、Fortune Business Insights）",
     "Insurance Asia 2026-10-12 報道（引 GlobalData、Fortune Business Insights）",
     "Insurance Asia", "2026-10-12", "EN原文；调查 2026-04-15 至 2026-07-22"),
    "en", 76, "verified"))

# ══ 8. Mox Bank × QBE：全数码家居保险经手机 App 投保 ══
ITEMS.append(mk(
    "iaasia-mox-bank-qbe-home-insurance-app-20261012",
    "insuranceasia", "pro", "news",
    "2026-10-12T05:30:00+08:00",
    "https://insuranceasia.com/insurance/news/mox-bank-offers-qbe-backed-home-insurance-through-banking-app",
    "Mox Bank推全數碼家居保險「Home Cushion」　QBE承保、App內預填資料即時投保",
    "Insurance Asia 10月12日報道：香港Mox Bank Limited推出Home Cushion保險，由昆士蘭保險（QBE Hongkong & Shanghai Insurance Limited）承保，透過Mox手機應用程式全數碼投保，涵蓋家居財物、樓宇結構及第三者責任，租客、自住業主與業主均可投保。第三者責任上限1,000萬港元；設搬遷保障最多28天（現居及新居）、轉運保障上限總保額15%、家居財物以重置成本賠付（不扣折舊）、重大搬遷期間寵物臨時住宿。保障分三個計劃，樓宇結構最高150萬港元、家居財物最高10萬港元；App內以預填資料完成投保，2026年10月31日前投保可獲最多200港元超市禮券，現有Mox Insure客戶另有獎賞。 [EN原文]",
    "香港本地嵌入式保險（銀行App＋保險）再添一例，是「渠道去中介化」壓力的具體形態：簡單標準化產品（家居、旅遊、意外）正被銀行／平台以預填與即時出單吸收。對前線的實際含義是產品組合必須向「複雜、需要建議與持續服務」的部分靠攏（醫療、危疾、退休與傳承），並把數碼渠道產品當作客戶教育與交叉銷售的補充而非對手。",
    "團隊分享：嵌入式保險與渠道變化對顧問的影響",
    "客戶場景切入：租客／業主的家居保障缺口",
    "組合策略討論：簡單產品數碼化後的顧問價值",
    "產品對標：數碼投保體驗與傳統流程差異",
    (3, 2, 3, 2), ["product", "tech"], ["channel", "product", "hong-kong", "insurtech"],
    ["Mox Bank", "QBE", "家居保险", "嵌入式保险", "数码投保"],
    ("Insurance Asia 2026-10-12 报道", "Insurance Asia 2026-10-12 報道",
     "Insurance Asia", "2026-10-12", "EN原文；QBE 承保，10-31 前投保有礼券"),
    "en", 72, "verified"))

# ══ 9. 台湾寿险外币保单新造保费升 39% ══
ITEMS.append(mk(
    "iaasia-taiwan-fc-policy-sales-39-july-2026-20261012",
    "insuranceasia", "pro", "stats",
    "2026-10-12T06:15:00+08:00",
    "https://insuranceasia.com/insurance/news/taiwan-life-insurers-foreign-currency-policy-sales-rise-39-in-july-2026",
    "台灣壽險外幣保單新造保費升39%　傳統型佔八成、投資型升85%（截至2026年7月底）",
    "Insurance Asia 10月12日報道：台灣壽險業外幣計價新造保單保費截至2026年7月底達104億美元（3,309億新台幣），按年升39%（去年同期75億美元／2,381.9億新台幣）。傳統型產品83億美元（2,650.1億新台幣），佔總額約八成，按年升31%；投資型產品21億美元（658.9億新台幣），按年升85%，佔約兩成。（1美元＝31.94新台幣） [EN原文]",
    "同屬華人高儲蓄市場的外幣保單需求指標：台灣外幣保單（多為美元）高增長，反映利率環境下客戶對外幣計價長期儲蓄／保障的偏好仍在，且投資型（類投連）增速更快。可作與高客討論「幣種配置與長期保單」時的區域參照，同時提醒：外幣保單的匯率風險與產品結構差異必須逐項披露，不可與本地產品類比收益。",
    "高客溝通素材：外幣保單需求與幣種配置",
    "產品對照：傳統型與投資型外幣保單增速差異",
    "合規提醒：外幣保單匯率與結構風險披露",
    "市場參照：華人市場外幣長期儲蓄偏好",
    (2, 3, 3, 1), ["market", "product"], ["market", "apac", "par", "macro"],
    ["台湾寿险", "外币保单", "新造保费", "投资型", "汇率风险"],
    ("Insurance Asia 2026-10-12 报道", "Insurance Asia 2026-10-12 報道",
     "Insurance Asia", "2026-10-12", "EN原文；截至 2026 年 7 月底"),
    "en", 70, "verified"))

# ══ 10. 日本寿险 4–7 月新造件数下滑、保费升 2.3% ══
ITEMS.append(mk(
    "iaasia-japan-life-sales-fall-premium-growth-july-2026-20261012",
    "insuranceasia", "pro", "stats",
    "2026-10-12T06:00:00+08:00",
    "https://insuranceasia.com/insurance/news/japan-life-insurance-sales-fall-despite-23-premium-growth-in-july-2026",
    "日本壽險4–7月新造件數僅及去年91.8%　保費收入升2.3%；個人年金新造金額跌16.3%",
    "Insurance Asia 10月12日報道：日本41家壽險公司2026年4月至7月底累計新造個人保險543.6萬件、保額1,149億美元（18.161萬億日圓），分別為去年同期的91.8%（件數）及100.2%（金額）；7月單月134.2萬件、303億美元，為去年92.8%及98.3%。累計個人年金新造39.4萬件、149億美元，件數及金額為去年83.2%及83.7%。期內保費收入812億美元、按年升2.3%；理賠、年金及給付合計397億美元、按年跌1.2%；解約返還金306億美元、按年升40.2%；營運費用升5%至112億美元。7月底總資產2.55萬億美元、按年升0.5%。（1美元＝158.05日圓） [EN原文]",
    "成熟高齡市場的結構性訊號：保費微升而新造件數下滑＝平均保額上升、件數增長見頂；個人年金新造金額大幅回落，而解約返還金按年飆升40.2%，反映利率環境變化下客戶取態在變。可用作討論「退休產品需求不等於年金需求、解約風險與流動性」的數據參照，也提醒向客戶解說長期保單不宜以短期市況作單一決策。",
    "團隊分享：高齡市場新造與解約數據的啟示",
    "客戶溝通素材：年金與退休規劃的取捨",
    "風險提示討論：保單解約與流動性安排",
    "市場參照：日本壽險結構變化對香港的啟示",
    (2, 3, 2, 1), ["market", "product"], ["market", "apac", "retirement", "results"],
    ["日本寿险", "新造保单", "个人年金", "解约返还", "退休市场"],
    ("Insurance Asia 2026-10-12 报道", "Insurance Asia 2026-10-12 報道",
     "Insurance Asia", "2026-10-12", "EN原文；2026 年 4–7 月累计"),
    "en", 70, "verified"))

# ══ 11. Tune Protect × Airpaz：嵌入式旅游保险扩展至三个东盟市场 ══
ITEMS.append(mk(
    "iaasia-tune-protect-airpaz-travel-3-asean-20261012",
    "insuranceasia", "pro", "news",
    "2026-10-12T06:30:00+08:00",
    "https://insuranceasia.com/insurance/news/tune-protect-expands-travel-insurance-three-asean-markets",
    "Tune Protect與Airpaz把嵌入式旅遊保險由馬來西亞擴展至印尼、泰國及菲律賓",
    "Insurance Asia 10月12日報道：馬來西亞Tune Protect Group Berhad旗下Tune Protect Re把與訂票平台Airpaz的旅遊保險合作，由馬來西亞擴展至印尼、泰國及菲律賓；旅客在Airpaz網站或手機應用程式訂購機票時可直接投保並即時獲得電子保單，各地由Tune Protect Malaysia、Oona Insurance Indonesia、Krungthai Panich Insurance及Pioneer Insurance & Surety Corporation承保。Tune Protect Re行政總裁Janet Chin表示，擴展有助鞏固集團在旅客增長及數碼採用率高的東南亞市場的區域佈局。 [EN原文]",
    "嵌入式旅遊保險是「平台＋多家承保商」模式的典型：同一產品在不同市場由不同本地承保商承接，旅遊平台負責流量與投保體驗。對前線的啟示是：旅客客群的保障缺口正被平台以最低摩擦方式覆蓋，顧問的差異化應落在需要建議的場景（家庭旅遊綜合保障、醫療與危疾銜接、多年期規劃）。",
    "團隊分享：嵌入式旅遊保險的模式與分工",
    "客戶場景切入：常旅遊客戶的保障缺口盤點",
    "渠道觀察：平台流量與多家承保商的分工",
    "產品對標：單次旅遊險與綜合醫療保障的銜接",
    (2, 2, 2, 2), ["product", "tech"], ["distribution", "product", "apac", "travel"],
    ["Tune Protect", "Airpaz", "旅游保险", "嵌入式保险", "东盟市场"],
    ("Insurance Asia 2026-10-12 报道", "Insurance Asia 2026-10-12 報道",
     "Insurance Asia", "2026-10-12", "EN原文"),
    "en", 68, "verified"))

# ══ 12. AM Best：GIC Re 资本最强但承保续亏 ══
ITEMS.append(mk(
    "iaasia-gic-re-underwriting-losses-am-best-20261012",
    "insuranceasia", "pro", "report",
    "2026-10-12T05:15:00+08:00",
    "https://insuranceasia.com/insurance/news/gic-re-faces-underwriting-losses-despite-strong-capital",
    "AM Best：印度GIC Re維持最強風險調整資本　惟承保續虧、2026財年ROE 11.5%",
    "Insurance Asia 10月12日報道：AM Best指印度再保險公司General Insurance Corporation of India（GIC Re）中長期可維持其最強水平的風險調整資本，資本管理支持監管償付能力，但對本地股票投資配置較高令其承受市場風險；2026財年（截至2026年3月31日）股東回報率（ROE）11.5%，2022–2026五個財年平均9.5%。承保表現持續虧損、綜合成本率偏高，長期由投資收益（含股票已實現收益）補足；AM Best評其業務組合為「有利」，GIC Re為全球第10大非IFRS 17再保險人，並受惠印度4%法定分保與優先承保權。 [EN原文]",
    "再保險商業模式的教科書級個案：「資本強、承保弱、靠投資收益補」，正好用來說明客戶常問的「保費去哪了、公司怎樣賺錢」。亦可用於向團隊解釋為何分析保司要看承保與投資兩條線，以及為何評級與展望需分開理解（資本充足≠盈利穩健）。",
    "團隊知識補強：再保險人盈利結構（承保 vs 投資）",
    "客戶提問應對：保費與公司盈利的關係",
    "市場參照：亞洲再保市場結構與法定分保",
    "公開引用源整理（AM Best 全球再保排名）",
    (1, 2, 2, 2), ["insurer", "market"], ["reinsurance", "capital", "results", "apac"],
    ["GIC Re", "AM Best", "再保险", "承保盈利", "偿付能力"],
    ("Insurance Asia 2026-10-12 报道（引 AM Best）", "Insurance Asia 2026-10-12 報道（引 AM Best）",
     "Insurance Asia", "2026-10-12", "EN原文；2026 财年 ROE 11.5%"),
    "en", 70, "verified"))

# ══ 13. T. Rowe Price 调查：香港打工仔怕 AI 打乱退休，仅两成准备充足 ══
ITEMS.append(mk(
    "scmp-trp-hk-workers-ai-retirement-survey-20261012",
    "scmp", "media", "report",
    "2026-10-12T12:00:00+08:00",
    "https://www.scmp.com/business/banking-finance/article/3370504/hong-kong-workers-fear-ai-driven-disruption-retirement-only-20-feel-prepared-survey",
    "調查：逾半香港打工仔料AI令退休路更難預測　僅五分一人自覺財務準備充足（30–39歲最焦慮）",
    "南華早報10月12日報道：資產管理公司T. Rowe Price調查1,004名30歲或以上、月入至少15,000港元的香港在職人士，約55%預期AI驅動的衝擊會動搖長期事業與收入軌跡，使退休路較上一代更難預測，但僅約五分一人自覺在財務上已作好準備；不確定感在30至39歲組別最明顯，61%預期退休之路更崎嶇。 [EN原文]",
    "香港退休保障缺口的最新民意數據，直接對應前線最常遇到的客戶狀態「知道要準備、但不知從何開始」。可用於設計客戶溝通切入（先講風險可辨識與可規劃，再談具體工具）：①AI對收入軌跡的憂慮＝收入保障與儲蓄紀律的話題；②僅兩成有準備＝需求存在但未被滿足；③30–39歲焦慮最高＝這一代同時面對供樓、子女與父母三重責任，適合以「分階段、可持續」而非一次性大額方案切入。",
    "客戶溝通切入：AI焦慮轉化為退休規劃對話",
    "新人培育：用民調數據建立需求意識（非推銷）",
    "客戶溝通素材：退休準備不足的本地數據",
    "團隊目標客群設定：30–39歲三重責任客群",
    (3, 2, 3, 1), ["market", "family"], ["ai", "retirement", "protection-gap", "hong-kong"],
    ["T. Rowe Price", "退休规划", "AI冲击", "香港调查", "保障缺口"],
    ("South China Morning Post 2026-10-12 报道（引 T. Rowe Price 调查）",
     "South China Morning Post 2026-10-12 報道（引 T. Rowe Price 調查）",
     "SCMP", "2026-10-12", "EN原文；样本 1,004 人，30 岁以上、月入 ≥HK$15,000"),
    "en", 66, "verified"))

# ══ 14. 前滙豐高管以 AI 代理团队驱动财富平台 ══
ITEMS.append(mk(
    "scmp-ex-hsbc-ai-agents-wealth-platform-20261012",
    "scmp", "media", "news",
    "2026-10-12T17:00:00+08:00",
    "https://www.scmp.com/business/money/wealth/article/3370565/former-hsbc-executive-launches-wealth-platform-powered-team-ai-agents",
    "前滙豐高管創立AI代理團隊驅動的財富管理平台　面向「大眾富裕」客群",
    "南華早報10月12日報道：一位資深銀行家（前滙豐高管）創立以AI代理（AI agents）團隊驅動的財富管理平台，目標協助「大眾富裕」（mass affluent）投資者管理投資組合、監察風險並主動發掘機會；報道指該產品面世正值通用型AI代理技術日益成熟、大型AI公司加速進軍行業專屬應用之際。 [EN原文]",
    "「AI代理＋財富管理」正式進入本地市場供給，是「IFA AI賦能」主線的競爭側參照：平台以AI代理覆蓋組合管理與風險監察（大眾富裕客層的標準化需求），意味顧問的差異化要落在需要人判斷與承擔責任的部分——目標與風險承受能力的確認、跨產品整合、家族與傳承安排、以及持牌人建議文件的責任歸屬。可作團隊討論「哪些交給AI、哪些必須由持牌人簽署」的現成案例。",
    "團隊AI工作流邊界討論：AI可代勞與必須持牌人負責的分界",
    "客戶溝通素材：AI理財工具的定位與局限",
    "市場趨勢觀察：本地智能投顧供給變化",
    "產品對標：大眾富裕客層的服務模式比較",
    (3, 2, 3, 2), ["tech", "market"], ["ai", "insurtech", "hnw", "tech"],
    ["AI代理", "财富管理平台", "大众富裕", "前滙豐", "智能投顾"],
    ("South China Morning Post 2026-10-12 报道", "South China Morning Post 2026-10-12 報道",
     "SCMP", "2026-10-12", "EN原文"),
    "en", 64, "verified"))

# ══ 15. Sage Advisory：ILS 提供真正分散效果 ══
ITEMS.append(mk(
    "artemis-ils-diversification-sage-advisory-20261012",
    "artemis", "pro", "report",
    "2026-10-12",
    "https://www.artemis.bm/news/ils-delivers-genuine-diversification-for-alternatives-allocations-sage-advisory/",
    "機構觀點：ILS回報與經濟週期脫鈎　可為另類配置帶來真正分散效果（市場規模1,445億美元）",
    "Artemis.bm 10月12日報道：Sage Advisory Services報告（作者Andrew Poreda，副總裁、高級研究分析師）指出，私人信貸、私募股權、房地產及基建最終都與經濟及企業風險掛鈎，而保險相連證券（ILS）的回報取決於自然災害或保險事件而非經濟週期，能為投資者提供另一種風險溢價，達致真正的分散效果；報告指ILS市場規模1,445億美元，巨災債券只是可見的一半，私下協商的再保險是更大的部分，並按不談判的合約日曆接受測試。 [EN原文]",
    "高客資產配置與家辦討論的可用素材：ILS 的分散邏輯建立在「風險來源不同」而非「資產類別不同」，是解釋「為甚麽要配置與股債不相關的資產」的清晰框架。同時提醒兩點專業邊界：①ILS 的尾部風險與流動性特徵須如實披露；②此類資產一般透過專業基金／機構渠道接觸，並非零售保單替代品。",
    "高客資產配置討論：非相關性資產的分散邏輯",
    "家辦溝通素材：另類資產與保險相連證券",
    "合規提醒：尾部風險與流動性披露要點",
    "團隊知識補強：ILS／巨災債券基礎概念",
    (1, 1, 3, 3), ["family", "market"], ["ils", "capital", "reinsurance", "hnw"],
    ["ILS", "巨灾债券", "资产配置", "分散效果", "Sage Advisory"],
    ("Artemis.bm 2026-10-12 报道（引 Sage Advisory Services 报告）",
     "Artemis.bm 2026-10-12 報道（引 Sage Advisory Services 報告）",
     "Artemis.bm", "2026-10-12", "EN原文；ILS 市场规模 1,445 亿美元"),
    "en", 70, "verified"))

# ══ 16. SageSure 策略投资 Pillar Capital ══
ITEMS.append(mk(
    "artemis-pillar-capital-sagesure-investment-20261012",
    "artemis", "pro", "news",
    "2026-10-12",
    "https://www.artemis.bm/news/pillar-capital-management-strategic-investment-sagesure/",
    "SageSure策略投資ILS基金管理人Pillar Capital　管理資產約43億美元、管理層續持重大股權",
    "Artemis.bm 10月12日報道：百慕達保險相連證券（ILS）及抵押再保險投資基金管理人Pillar Capital Management獲管理總承保人（MGU）SageSure策略投資。Pillar成立於2008年，截至2026年6月30日管理資產約43億美元，為市場上最大獨立ILS管理人之一；交易前由管理團隊與全球再保險公司TransRe（巴郡旗下）共同持有，交易後管理團隊仍持重大股權，行政總裁兼投資總監Stephen Velotti及營運總監Tara Railton繼續領導。 [EN原文]",
    "ILS 產業鏈（風險承擔方、專業管理人、機構資本）持續整合，對理解「巨災風險如何被資本市場吸收」有結構性價值；亦印證另類風險資產的管理人集中度在提高。對高客與家辦溝通的用途在於說明：接觸此類資產多數要經專業管理人與機構渠道，選擇重點在管理人規模、經驗與治理，而非單一產品過往回報。",
    "家辦溝通素材：另類資產管理人選擇要點",
    "高客資產配置討論：ILS 產業鏈與機構渠道",
    "團隊知識補強：再保險與資本市場的連接",
    "市場趨勢觀察：ILS 管理人整合",
    (1, 1, 2, 3), ["family", "market"], ["ils", "ma", "capital", "reinsurance"],
    ["Pillar Capital", "SageSure", "ILS基金", "策略投资", "再保险"],
    ("Artemis.bm 2026-10-12 报道", "Artemis.bm 2026-10-12 報道",
     "Artemis.bm", "2026-10-12", "EN原文；AUM 约 43 亿美元（截至 2026-06-30）"),
    "en", 70, "verified"))

# ══ 17. 宏利香港「My旗日」响应世界精神健康日（补漏） ══
ITEMS.append(mk(
    "manulife-hk-just-feel-my-flag-day-2026-20261010",
    "manulife", "insurer", "press",
    "2026-10-10",
    "https://www.manulife.com.hk/zh-hk/individual/about/newsroom/manulife-hk-and-just-feel-host-my-flag-day-2026.html",
    "宏利香港與JUST FEEL感講辦「My旗日」響應世界精神健康日　500名家長與子女任義工派逾萬張旗紙",
    "宏利香港與本地情緒教育慈善機構JUST FEEL感講於2026年10月10日世界精神健康日舉辦「My旗日2026」，集合來自宏利香港及九所JUST FEEL感講夥伴學校共500名親子義工，在全港多區派發逾10,000張「感受」旗紙，邀請市民留意自身感受、勇於表達內心所想，藉此推廣情緒健康與善意溝通。",
    "保司在精神健康與家庭溝通議題上的社區活動，可作前線與客戶（尤其年輕家庭客群）建立非銷售話題的素材：情緒健康與家庭關係是長期保障需求（醫療、危疾、家庭收入保障）的軟性切入點，也是團隊活動／客戶活動策劃的現成參考模式。",
    "客戶活動參考：以家庭與情緒健康作軟性切入",
    "團隊分享：保司社區項目與品牌訊息",
    "客戶溝通素材：精神健康與家庭關係話題",
    "活動策劃參考：親子義工與學校夥伴模式",
    (2, 1, 1, 1), ["insurer"], ["esg", "health", "talent", "hong-kong"],
    ["宏利香港", "精神健康", "JUST FEEL感講", "企业社会责任", "家庭"],
    ("宏利香港新聞中心 2026-10-10 新聞稿", "宏利香港新聞中心 2026-10-10 新聞稿",
     "Manulife Hong Kong", "2026-10-10", "中文原文（繁體）"),
    "zh", 75, "verified"))

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
    print('  +', it['id'], '|', it['publishedAt'], '|', it['sourceKey'], '|', it['sourceTier'], '|', it['verifyStatus'])
