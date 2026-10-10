#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 2026-10-11 00:2x increment into live-items.json.

窗口：2026-10-10T01:12（上次检查）→ 2026-10-11T00:2x。10月10日为周六，
香港监管/保司信源无新发布；本期新增 7 条（含1条10月9日晚发布的补漏条目）。
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

# ══ 1. Insurance Business：新加坡危疾定義擬由手術程序轉向疾病嚴重程度 ══
_s = ("Insurance Business Asia 10月10日報道：新加坡政府要求壽險協會（LIA）研究把危疾（CI）定義由指定手術程序"
      "轉向疾病本身及其嚴重程度，副總理兼金管局主席顏金勇10月7日以書面答覆國會確認方向；LIA將於2027年起"
      "展開檢討，任何更新只適用於新產品。報道指LIA《危疾框架2024》已自2025年10月1日起強制適用於所有新保單，"
      "但2025年10月前簽發的保單仍沿用2019年或更早的定義，而2019年前簽發者更沿用再上一代框架。以心臟瓣膜病"
      "為例，舊定義以「開胸手術」為賠付觸發，如今心臟科醫生多採經導管置換（TAVI），疾病與嚴重程度相同、"
      "治療更佳，但舊保單可能不賠付。新加坡逾九成危疾索償集中於主要癌症、指定嚴重程度心臟病發及冠狀動脈搭橋，"
      "正是醫療創新最快、新舊定義落差最易在索償時浮現的範疇。報道形容10月7日答覆為顧問提供了一個客戶聽得懂的"
      "保單檢視切入點，並提醒顧問應即時啟動組合檢視，而非等待2027年檢討結果。 [EN原文]")
ITEMS.append(mk(
    "ibm-singapore-ci-definitions-disease-severity-legacy-policies-20261010",
    "insurancebusinessmag", "media", "news",
    "2026-10-10T02:13:00+08:00",
    "https://www.insurancebusinessmag.com/asia/news/life-insurance/singapores-ci-definitions-are-moving-toward-disease--legacy-policies-arent-593043.aspx",
    ("Insurance Business：新加坡危疾定義擬轉向「疾病嚴重程度」 2025年10月前舊保單不受影響 顧問須主動檢視",
     "Insurance Business：新加坡危疾定義擬轉向「疾病嚴重程度」 2025年10月前舊保單不受影響 顧問須主動檢視"),
    (_s, _s),
    ("同一疾病因治療方式進步而出現「舊保單不賠」落差，是港新兩地危疾產品共通的條款風險；新加坡由監管層面"
     "推動定義轉向疾病嚴重程度，值得對照香港現行危疾定義與顧問檢視話術。",
     "同一疾病因治療方式進步而出現「舊保單不賠」落差，是港新兩地危疾產品共通的條款風險；新加坡由監管層面"
     "推動定義轉向疾病嚴重程度，值得對照香港現行危疾定義與顧問檢視話術。"),
    ("向客戶解釋「治療方式演變 vs 保單定義年份」的落差", "向客戶解釋「治療方式演變 vs 保單定義年份」的落差"),
    ("客戶保單檢視清單加入「危疾定義年份」核對項", "客戶保單檢視清單加入「危疾定義年份」核對項"),
    ("團隊培訓：危疾定義由手術觸發轉向疾病嚴重程度的趨勢", "團隊培訓：危疾定義由手術觸發轉向疾病嚴重程度的趨勢"),
    ("港新危疾定義與舊保單處理方式對照", "港新危疾定義與舊保單處理方式對照"),
    (2, 2, 1, 2), ["product"], ["critical-illness", "product-design", "regulation", "policy-review"],
    ["危疾定義", "CI框架", "保單檢視", "新加坡"],
    ("Insurance Business Asia 2026-10-10 報道", "Insurance Business Asia 2026-10-10 報道",
     "Insurance Business", "2026-10-10", "EN原文"), "en", 68, "verified"))

# ══ 2. Insurance Asia 週報：新加坡檢討家辦稅務投資清單 ══
_s = ("Insurance Asia 10月10日「本週保險」專欄（涵蓋10月5至9日）：新加坡副總理兼金管局主席顏金勇在財富管理"
      "學院「全球亞洲家族辦公室峰會」表示，當局正檢討家辦稅務政策框架，金管局將檢視「指定投資清單」"
      "（designated investment list）——即基金稅務優惠計劃下可享免稅的投資類別，以回應單一家族辦公室希望在"
      "數位支付代幣、保險保單等資產上取得更大靈活度的訴求；他指地緣政治、科技進步及投資者偏好轉變令財富管理"
      "更趨複雜。同期要聞：蘇黎世保險完成收購Beazley，組成總部設於倫敦的全球最大特殊險業務，預計2029年前"
      "每年新增收入逾10億美元並節省至少1.5億美元成本；宏利與慕尼黑再旗下慕尼黑美國再保險完成32億美元長期護理"
      "準備金再保交易（8月5日公布），全面轉移該組合的生物風險。另有保誠新加坡推出可同時保障子女與年邁父母的"
      "終身計劃、Singlife與NHG Health合作、UNDP與Generali在印度推MSME保險創新挑戰。 [EN原文]")
ITEMS.append(mk(
    "iaasia-week-in-insurance-sg-family-office-tax-list-beazley-manulife-20261010",
    "insuranceasia", "media", "news",
    "2026-10-10T05:00:00+08:00",
    "https://insuranceasia.com/insurance/news/week-in-insurance-zurich-completes-beazley-deal-manulife-reinsures-32b-in-reserves-singapore-reviews-tax-rules",
    ("Insurance Asia 週報：新加坡檢討家辦稅務投資清單（擬納數位支付代幣及保單） 蘇黎世完成收購Beazley 宏利32億美元長護再保交割",
     "Insurance Asia 週報：新加坡檢討家辦稅務投資清單（擬納數位支付代幣及保單） 蘇黎世完成收購Beazley 宏利32億美元長護再保交割"),
    (_s, _s),
    ("新加坡放寬家辦可享稅務優惠的資產類別（含保單、數位資產），直接關係香港與新加坡在家辦與保單架構上的"
     "競爭格局；宏利與蘇黎世的交易則反映人壽與特殊險的資本配置方向。",
     "新加坡放寬家辦可享稅務優惠的資產類別（含保單、數位資產），直接關係香港與新加坡在家辦與保單架構上的"
     "競爭格局；宏利與蘇黎世的交易則反映人壽與特殊險的資本配置方向。"),
    ("與客戶談及家辦落點時，可對照新加坡最新稅務檢討方向", "與客戶談及家辦落點時，可對照新加坡最新稅務檢討方向"),
    ("保單在家族架構中的角色（新加坡免稅清單擬納入保單）", "保單在家族架構中的角色（新加坡免稅清單擬納入保單）"),
    ("團隊分享：亞太再保與併購動態", "團隊分享：亞太再保與併購動態"),
    ("港新家辦稅務優惠比較的討論素材", "港新家辦稅務優惠比較的討論素材"),
    (2, 2, 2, 3), ["family", "insurer"], ["family-office", "tax", "m&a", "reinsurance", "long-term-care"],
    ["新加坡家辦", "稅務優惠", "Beazley", "宏利再保"],
    ("Insurance Asia 2026-10-10 報道", "Insurance Asia 2026-10-10 報道",
     "Insurance Asia", "2026-10-10", "EN原文"), "en", 66, "verified"))

# ══ 3. InsuranceAsia News 週報：澳洲高院 Scope 3 判決 ══
_s = ("InsuranceAsia News 10月10日「Full Capacity」週報：澳洲高等法院裁定否決新南威爾士Mount Pleasant煤礦"
      "擴建計劃，確立規劃機關須考慮Scope 3（下游燃燒）排放，並須考慮如何緩解煤炭出口後所產生的溫室氣體；"
      "該項目下游排放佔其氣候足印98%，判決明言「溫室氣體排放的影響不因其分類方式而改變」。報道指這對作為"
      "全球最大化石燃料出口國之一的澳洲能源業構成壓力，其他礦業樞紐（如西澳）亦恐受波及，並與2026至2028年間"
      "在多數司法管轄區陸續生效的Scope 3披露規則互相呼應，監管機構、法院、貸款人、投資者及保險人將密切注視"
      "問責向價值鏈上游轉移。同期獨家：MS Amlin正與投資者磋商2027年在Phoenix架構下設立新加坡註冊全sidecar，"
      "初步目標4,000萬至5,000萬美元。另有：IAG與RAC就ACCC否決其9.4億美元收購向澳洲競爭審裁處申請覆核；"
      "韓國三大政策保險計劃2025年自然災害索償升至11.7億美元，連續三年上升；韓國OK金融集團簽約收購Yebyeol保險。 [EN原文]")
ITEMS.append(mk(
    "ian-australia-high-court-scope3-mount-pleasant-apac-weekly-20261010",
    "insuranceasianews", "media", "news",
    "2026-10-10T08:00:00+08:00",
    "https://insuranceasianews.com/australias-coal-industry-faces-climate-reckoning/",
    ("InsuranceAsia News：澳洲高院裁定環評須計入Scope 3排放（Mount Pleasant煤礦擴建被否）",
     "InsuranceAsia News：澳洲高院裁定環評須計入Scope 3排放（Mount Pleasant煤礦擴建被否）"),
    (_s, _s),
    ("Scope 3問責向上游轉移，將影響能源與基建項目的可保性、承保限制與轉型計劃審查；新加坡sidecar動向亦"
     "反映亞洲ILS與再保資本平台化趨勢。",
     "Scope 3問責向上游轉移，將影響能源與基建項目的可保性、承保限制與轉型計劃審查；新加坡sidecar動向亦"
     "反映亞洲ILS與再保資本平台化趨勢。"),
    ("向企業客戶說明氣候訴訟與Scope 3如何影響承保", "向企業客戶說明氣候訴訟與Scope 3如何影響承保"),
    ("一般業務：能源／工程項目的環境責任風險提示", "一般業務：能源／工程項目的環境責任風險提示"),
    ("團隊培訓：氣候風險監管與披露趨勢", "團隊培訓：氣候風險監管與披露趨勢"),
    ("香港ILS政策與亞洲sidecar發展對照", "香港ILS政策與亞洲sidecar發展對照"),
    (2, 2, 2, 3), ["reg", "market"], ["climate", "litigation", "scope-3", "natcat", "ils"],
    ["Scope 3", "氣候訴訟", "煤礦", "sidecar"],
    ("InsuranceAsia News 2026-10-10 報道", "InsuranceAsia News 2026-10-10 報道",
     "InsuranceAsia News", "2026-10-10", "EN原文"), "en", 64, "verified"))

# ══ 4. Artemis：颶風Simon增強至四級 墨西哥巨災債券逼近觸發 ══
_s = ("Artemis 10月10日報道：太平洋颶風Simon持續快速增強，美國國家颶風中心指其已達四級（持續風速150英里、"
      "中心最低氣壓約938mb），預計周日於墨西哥西南至中西部登陸，令規模1.75億美元的IBRD CAR Mexico 2024"
      "（Pacific）參數式颶風巨災債券再度受關注。該債券以中心最低氣壓為觸發指標，參數區下限為937mb；消息指"
      "按預測登陸區域，氣壓須降至932mb或以下才觸發25%本金賠付，更低氣壓方對應50%至100%賠付。報道指多個數值"
      "模式預期登陸前會明顯減弱，但NHC預測登陸時仍達三至四級，不確定性高；9月同一債券曾受颶風Polo威脅，"
      "Polo最終減弱登陸未造成損失。 [EN原文]")
ITEMS.append(mk(
    "artemis-hurricane-simon-cat4-mexico-catbond-trigger-20261010",
    "artemis", "pro", "news",
    "2026-10-10T16:00:00+08:00",
    "https://www.artemis.bm/news/hurricane-simon-intensify-mexico-catastrophe-bond-watch/",
    ("Artemis：颶風Simon增強至四級 墨西哥1.75億美元參數式巨災債券逼近觸發（932mb或觸發25%賠付）",
     "Artemis：颶風Simon增強至四級 墨西哥1.75億美元參數式巨災債券逼近觸發（932mb或觸發25%賠付）"),
    (_s, _s),
    ("同一張墨西哥參數式巨災債券一個月內兩度逼近觸發點，是觀察氣壓型參數門檻在實戰中如何運作的活教材；"
     "對亞洲新興市場設計颱風／地震參數式產品時選擇觸發指標具參考意義。",
     "同一張墨西哥參數式巨災債券一個月內兩度逼近觸發點，是觀察氣壓型參數門檻在實戰中如何運作的活教材；"
     "對亞洲新興市場設計颱風／地震參數式產品時選擇觸發指標具參考意義。"),
    ("引用資本市場工具條款時只作架構說明，不涉投資建議", "引用資本市場工具條款時只作架構說明，不涉投資建議"),
    ("納入ILS與巨災債券觸發事件監察", "納入ILS與巨災債券觸發事件監察"),
    ("用於說明參數式產品觸發門檻與基差風險", "用於說明參數式產品觸發門檻與基差風險"),
    ("香港ILS政策方向與國際發行節奏對照", "香港ILS政策方向與國際發行節奏對照"),
    (1, 2, 2, 2), ["market"], ["ils", "catastrophe-bond", "parametric", "natural-catastrophe"],
    ["颶風Simon", "墨西哥巨災債券", "參數式", "IBRD"],
    ("Artemis 2026-10-10 報道", "Artemis 2026-10-10 報道", "Artemis", "2026-10-10", "EN原文"),
    "en", 70, "verified"))

# ══ 5. 南華早報評論：加密貨幣「扳手攻擊」與保護缺口 ══
_s = ("南華早報10月10日評論（作者為亞洲數碼經濟學院院長Tan Poh Hwee）：虛擬資產「扳手攻擊」"
      "（以暴力或威脅迫使人交出加密貨幣）持續上升，今年上半年已從持有人手中奪走逾3,000萬美元。文章指出，"
      "錢包可抵禦精密黑客攻擊，但持有人一旦被脅迫即可即時授權轉帳，持有人及其家人遂成為目標；把數碼資產的"
      "保安與持有人人身安全分開處理，是不足夠的金融保安觀。文章認為行業有責任設計能應對「被脅迫交出資產」"
      "現實的產品與服務，成熟的金融生態須為加密貨幣投資者及其家人提供可信的安全途徑。 [EN原文]")
ITEMS.append(mk(
    "scmp-crypto-wrench-attacks-protection-gap-20261010",
    "scmp", "media", "opinion",
    "2026-10-10T16:30:00+08:00",
    "https://www.scmp.com/opinion/world-opinion/article/3370088/better-protection-needed-violent-cryptocurrency-robberies-surge",
    ("南華早報評論：加密貨幣「扳手攻擊」激增 業界須為持有人人身安全提供保護",
     "南華早報評論：加密貨幣「扳手攻擊」激增 業界須為持有人人身安全提供保護"),
    (_s, _s),
    ("數碼資產持有人的脅迫風險成為新型保障缺口，與高客的資產保全、綁架／勒索及人身安全方案設計直接相關；"
     "亦是與家辦客戶討論「資產形態改變、保障是否跟上」的現成切入點。",
     "數碼資產持有人的脅迫風險成為新型保障缺口，與高客的資產保全、綁架／勒索及人身安全方案設計直接相關；"
     "亦是與家辦客戶討論「資產形態改變、保障是否跟上」的現成切入點。"),
    ("與高客談數碼資產時提示人身安全與脅迫風險", "與高客談數碼資產時提示人身安全與脅迫風險"),
    ("檢視現有保單在綁架、勒索及人身意外方面的保障", "檢視現有保單在綁架、勒索及人身意外方面的保障"),
    ("團隊分享：新興風險與保障缺口題材", "團隊分享：新興風險與保障缺口題材"),
    ("家族資產保護整體方案的討論素材", "家族資產保護整體方案的討論素材"),
    (2, 2, 1, 2), ["tech"], ["crypto", "protection-gap", "high-net-worth", "cyber"],
    ["加密貨幣", "扳手攻擊", "保障缺口", "高淨值"],
    ("南華早報 2026-10-10 評論", "南華早報 2026-10-10 評論", "SCMP", "2026-10-10", "EN原文"),
    "en", 58, "verified"))

# ══ 6. 南華早報：Z世代超越年長藏家成藝術市場最大買家 ══
_s = ("南華早報10月10日報道：Art Basel與UBS《2026全球收藏調查》顯示，Z世代高淨值藏家已超越年長世代成為"
      "藝術市場最大支出者，人均購藏金額為年長藏家的兩倍以上；全球藝術銷售2025年回升4%至約596億美元，結束"
      "連續兩年下跌，內地與香港續扮演關鍵樞紐角色。 [EN原文]")
ITEMS.append(mk(
    "scmp-gen-z-art-collectors-ubs-artbasel-survey-20261010",
    "scmp", "media", "news",
    "2026-10-10T14:00:00+08:00",
    "https://www.scmp.com/business/article/3370329/gen-z-overtakes-older-collectors-art-market-spending-rebounds-globally-report",
    ("南華早報：Z世代超越年長藏家成藝術市場最大買家 中港仍為關鍵樞紐（Art Basel／UBS調查）",
     "南華早報：Z世代超越年長藏家成藝術市場最大買家 中港仍為關鍵樞紐（Art Basel／UBS調查）"),
    (_s, _s),
    ("年輕高淨值藏家成為藝術市場主力，意味另類資產與傳承需求同步上升，並以香港為重要交易樞紐；"
     "可作為與下一代客戶談資產配置與傳承安排的切入素材。",
     "年輕高淨值藏家成為藝術市場主力，意味另類資產與傳承需求同步上升，並以香港為重要交易樞紐；"
     "可作為與下一代客戶談資產配置與傳承安排的切入素材。"),
    ("與客戶談另類資產時引用年輕藏家趨勢", "與客戶談另類資產時引用年輕藏家趨勢"),
    ("下一代客戶的傳承與收藏品安排討論", "下一代客戶的傳承與收藏品安排討論"),
    ("家辦／高客活動的選題素材", "家辦／高客活動的選題素材"),
    ("香港作為藝術與財富樞紐的定位佐證", "香港作為藝術與財富樞紐的定位佐證"),
    (2, 2, 1, 3), ["family"], ["wealth-transfer", "uhnw", "alternative-assets", "art"],
    ["Z世代藏家", "藝術市場", "另類資產", "傳承"],
    ("南華早報 2026-10-10 報道", "南華早報 2026-10-10 報道", "SCMP", "2026-10-10", "EN原文"),
    "en", 56, "verified"))

# ══ 7. 補漏：比特幣人壽保險 Meanwhile 融資3,750萬美元（10月9日晚發布，上次檢查漏收）══
_s = ("The Block 10月9日報道：以比特幣計價的百慕大人壽保險公司Meanwhile完成3,750萬美元融資，由Bain Capital "
      "Crypto領投，Haun Ventures、Pantera Capital、Apollo等參與，累計融資逾1.8億美元。公司自2026年初推出"
      "面向美國境外高淨值客戶的單一保費終身壽險BTC Life 1-Pay（以比特幣繳付保費、以比特幣支付身故賠償，"
      "首年後可借取最高90%保單價值，無還款時間表、不設追繳保證金），至今已簽約15家服務富裕家庭的經紀夥伴，"
      "覆蓋新加坡、香港、阿聯酋及瑞士，夥伴包括在香港、新加坡及蘇黎世設有辦事處的Lioner，以及經營高淨值"
      "壽險市場平台的Apeiron Group。公司2025年底總資產1,183枚比特幣、法定資本及盈餘759枚，並表示今年長期"
      "承保收入將較去年翻倍以上。 [EN原文]")
ITEMS.append(mk(
    "theblock-meanwhile-bitcoin-life-insurer-37-5m-lioner-hk-20261009",
    "theblock", "media", "news",
    "2026-10-09T18:33:00+08:00",
    "https://www.theblock.co/news/deals/2026-10-09-sam-altman-backed-bitcoin-life-insurer-meanwhile-raises-37-5-million-round-led-by-bain-capital-crypto-418131",
    ("The Block：比特幣人壽保險公司Meanwhile融資3,750萬美元 已簽15家經紀夥伴（含香港Lioner）",
     "The Block：比特幣人壽保險公司Meanwhile融資3,750萬美元 已簽15家經紀夥伴（含香港Lioner）"),
    (_s, _s),
    ("保險與數碼資產的結合開始出現獲監管牌照的商業模式（百慕大IILT牌照），並已吸納香港經紀夥伴；"
     "對高客「以加密資產傳承」的實務需求與本地中介角色有前瞻參考價值。",
     "保險與數碼資產的結合開始出現獲監管牌照的商業模式（百慕大IILT牌照），並已吸納香港經紀夥伴；"
     "對高客「以加密資產傳承」的實務需求與本地中介角色有前瞻參考價值。"),
    ("與高客談及加密資產傳承時的趨勢背景", "與高客談及加密資產傳承時的趨勢背景"),
    ("留意以非傳統資產繳費／賠付產品在港的可行性", "留意以非傳統資產繳費／賠付產品在港的可行性"),
    ("團隊分享：InsurTech 融資與新型產品模式", "團隊分享：InsurTech 融資與新型產品模式"),
    ("跨境高客產品創新的觀察個案", "跨境高客產品創新的觀察個案"),
    (2, 2, 2, 3), ["tech", "product"], ["insurtech", "digital-asset", "high-net-worth", "funding"],
    ["Meanwhile", "比特幣壽險", "Lioner", "InsurTech融資"],
    ("The Block 2026-10-09 報道", "The Block 2026-10-09 報道", "The Block", "2026-10-09", "EN原文"),
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
