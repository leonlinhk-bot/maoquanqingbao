#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 2026-10-08 00:07 (catch-up for missed 21:08) increment into live-items.json"""
import json
from datetime import datetime, timezone, timedelta

NOW = datetime.now(timezone(timedelta(hours=8))).strftime('%Y-%m-%dT%H:%M:%S+08:00')
CR = {"sc": "本站导读", "tc": "本站導讀"}


def mk(id_, sourceKey, tier, kind, pub, url, t_sc, t_tc, s_sc, s_tc, w_sc, w_tc,
       a_f, a_m, a_l, a_c, ri, boards, themes, tags, src_sc, src_tc, lang, score):
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
        "tags": {"sc": tags, "tc": tags},
        "contentRole": CR, "featured": False, "evergreen": False, "ingestedAt": NOW,
        "id": id_, "publishedAt": pub, "originalUrl": url,
        "title": {"sc": t_sc, "tc": t_tc},
        "summary": {"sc": s_sc, "tc": s_tc},
        "why": {"sc": w_sc, "tc": w_tc},
        "source": {"sc": src_sc, "tc": src_tc, "lang": lang},
    }


ITEMS = []

# ── 1. InsuranceAsia News：Awbury 辛迪加在日本開展承保業務 ────────────────
ITEMS.append(mk(
 "ian-awbury-syndicate-japan-20261007", "insuranceasianews", "pro", "news", "2026-10-07T21:39:00+08:00",
 "https://insuranceasianews.com/awbury-syndicate-2025-launches-japanese-underwriting-operations-via-lloyds-japan/",
 "Awbury 旗下 Syndicate 2025 經勞合社日本開展日本承保業務",
 "Awbury 旗下 Syndicate 2025 經勞合社日本開展日本承保業務",
 "InsuranceAsia News 10月7日報道：Awbury 旗下勞合社辛迪加 Syndicate 2025 正式在日本開展承保業務，透過 Lloyd's Japan 平台落地，切入信用（credit）及貿易相關風險。報道指該辛迪加此番在東京設立承保團隊，屬勞合社保險市場在日本的又一次擴張。 [EN原文]",
 "InsuranceAsia News 10月7日報道：Awbury 旗下勞合社辛迪加 Syndicate 2025 正式在日本開展承保業務，透過 Lloyd's Japan 平台落地，切入信用（credit）及貿易相關風險。報道指該辛迪加此番在東京設立承保團隊，屬勞合社保險市場在日本的又一次擴張。 [EN原文]",
 "勞合社辛迪加直接落戶日本，反映亞洲信用、貿易與地緣相關風險的專業承保需求上升，也為區內經紀與企業客戶多開一條特種險渠道。",
 "勞合社辛迪加直接落戶日本，反映亞洲信用、貿易與地緣相關風險的專業承保需求上升，也為區內經紀與企業客戶多開一條特種險渠道。",
 ("客戶有跨境貿易或信用風險敞口時，可把勞合社辛迪加列為其中一個市場選項，但必須逐一核實承保範圍",
  "客戶有跨境貿易或信用風險敞口時，可把勞合社辛迪加列為其中一個市場選項，但必須逐一核實承保範圍"),
 ("納入市場與承保能力情報，不作產品推介", "納入市場與承保能力情報，不作產品推介"),
 ("用於說明亞洲特種險承保能力來源", "用於說明亞洲特種險承保能力來源"),
 ("跨境信用與貿易風險安排的市場背景", "跨境信用與貿易風險安排的市場背景"),
 (1, 2, 2, 2), ["market", "insurer"], ["lloyds", "apac", "credit", "distribution"],
 ["勞合社", "Awbury", "辛迪加", "日本", "信用保險"],
 "InsuranceAsia News 2026-10-07 報道", "InsuranceAsia News 2026-10-07 報道", "en", 70))

# ── 2. InsuranceAsia News：三井物產 Pana Harrison 委任一般保險主管 ──────
ITEMS.append(mk(
 "ian-mitsui-bussan-alice-lim-gi-20261007", "insuranceasianews", "pro", "news", "2026-10-07T18:08:00+08:00",
 "https://insuranceasianews.com/mitsui-bussan-pana-harrison-appoints-alice-lim-as-head-of-general-insurance/",
 "三井物產 Pana Harrison 委任 Alice Lim 為一般保險主管",
 "三井物產 Pana Harrison 委任 Alice Lim 為一般保險主管",
 "InsuranceAsia News 10月7日報道：經紀行 Mitsui Bussan Pana Harrison（新加坡）委任 Alice Lim 為一般保險主管，接替 Lisa Marbon；Marbon 將留任高級職務，專注策略客戶關係及業務發展。 [EN原文]",
 "InsuranceAsia News 10月7日報道：經紀行 Mitsui Bussan Pana Harrison（新加坡）委任 Alice Lim 為一般保險主管，接替 Lisa Marbon；Marbon 將留任高級職務，專注策略客戶關係及業務發展。 [EN原文]",
 "亞洲區經紀行的人事更替往往反映業務重心轉移；日本大型商社系經紀的一般保險主管換人，是觀察日系企業客戶風險需求變化的切入點。",
 "亞洲區經紀行的人事更替往往反映業務重心轉移；日本大型商社系經紀的一般保險主管換人，是觀察日系企業客戶風險需求變化的切入點。",
 ("涉及同業人事消息，僅作行業資訊參考，不作為銷售話術",
  "涉及同業人事消息，僅作行業資訊參考，不作為銷售話術"),
 ("歸入同業與渠道情報", "歸入同業與渠道情報"),
 ("用於了解亞洲經紀市場競爭格局", "用於了解亞洲經紀市場競爭格局"),
 ("日系企業客戶於亞洲的保險安排渠道背景", "日系企業客戶於亞洲的保險安排渠道背景"),
 (1, 1, 2, 1), ["market"], ["people", "broker", "apac", "talent"],
 ["人事任命", "三井物產", "新加坡", "一般保險"],
 "InsuranceAsia News 2026-10-07 報道", "InsuranceAsia News 2026-10-07 報道", "en", 70))

# ── 3. InsuranceAsia News：Lockton 委任日本業務高級顧問 ────────────────
ITEMS.append(mk(
 "ian-lockton-kenichiro-miki-japan-20261007", "insuranceasianews", "pro", "news", "2026-10-07T17:53:00+08:00",
 "https://insuranceasianews.com/lockton-taps-kenichiro-miki-as-senior-consultant-for-japan-business/",
 "Lockton 委任 Kenichiro Miki 為日本業務高級顧問",
 "Lockton 委任 Kenichiro Miki 為日本業務高級顧問",
 "InsuranceAsia News 10月7日報道：全球經紀行 Lockton 委任 Kenichiro Miki 為日本業務高級顧問，他此前在 Price Forbes 出任日本業務主管（head of Japan practice）。 [EN原文]",
 "InsuranceAsia News 10月7日報道：全球經紀行 Lockton 委任 Kenichiro Miki 為日本業務高級顧問，他此前在 Price Forbes 出任日本業務主管（head of Japan practice）。 [EN原文]",
 "國際經紀行持續加碼日本市場人才，與同日 Awbury、三井物產消息並讀，可見亞洲（尤其日本）企業風險業務正成為經紀競爭焦點。",
 "國際經紀行持續加碼日本市場人才，與同日 Awbury、三井物產消息並讀，可見亞洲（尤其日本）企業風險業務正成為經紀競爭焦點。",
 ("同業人事消息，僅作行業資訊參考", "同業人事消息，僅作行業資訊參考"),
 ("歸入同業與渠道情報", "歸入同業與渠道情報"),
 ("用於團隊了解國際經紀行亞洲布局", "用於團隊了解國際經紀行亞洲布局"),
 ("日系跨國企業保險安排的市場背景", "日系跨國企業保險安排的市場背景"),
 (1, 1, 2, 1), ["market"], ["people", "broker", "apac", "talent"],
 ["人事任命", "Lockton", "日本", "保險經紀"],
 "InsuranceAsia News 2026-10-07 報道", "InsuranceAsia News 2026-10-07 報道", "en", 70))

# ── 4. IBM：菲律賓鎖定巨災風險轉移安排 ────────────────────────────────
ITEMS.append(mk(
 "ibm-philippines-catastrophe-pool-deal-20261007", "insurancebusinessmag", "pro", "news", "2026-10-07T23:12:00+08:00",
 "https://www.insurancebusinessmag.com/asia/news/catastrophe/philippines-locks-in-disaster-risk-deal-as-domestic-catastrophe-pool-struggles-for-traction-592676.aspx",
 "Insurance Business：菲律賓落實災害風險轉移安排 本土巨災池仍待推動",
 "Insurance Business：菲律賓落實災害風險轉移安排 本土巨災池仍待推動",
 "Insurance Business Asia 10月7日報道：菲律賓已落實一項災害風險轉移（disaster risk）安排，惟當地本土巨災保險池（catastrophe pool）在爭取市場參與上仍遇困難，報道比較兩者在推動災害保障覆蓋上的進展差異。 [EN原文]",
 "Insurance Business Asia 10月7日報道：菲律賓已落實一項災害風險轉移（disaster risk）安排，惟當地本土巨災保險池（catastrophe pool）在爭取市場參與上仍遇困難，報道比較兩者在推動災害保障覆蓋上的進展差異。 [EN原文]",
 "亞洲新興市場的巨災保障缺口，主要靠主權／國際風險轉移與本土保險池兩條腿走路；菲律賓案例說明「有安排」不等於「有覆蓋」，是理解保障缺口的現實教材。",
 "亞洲新興市場的巨災保障缺口，主要靠主權／國際風險轉移與本土保險池兩條腿走路；菲律賓案例說明「有安排」不等於「有覆蓋」，是理解保障缺口的現實教材。",
 ("客戶關注自然災害保障時，說明本地與跨境安排的分別，不引述未經核實的賠付細節",
  "客戶關注自然災害保障時，說明本地與跨境安排的分別，不引述未經核實的賠付細節"),
 ("納入保障缺口與巨災情報", "納入保障缺口與巨災情報"),
 ("用於說明新興市場巨災保障的結構性限制", "用於說明新興市場巨災保障的結構性限制"),
 ("東南亞巨災風險的跨境再保與轉移視角", "東南亞巨災風險的跨境再保與轉移視角"),
 (1, 2, 2, 2), ["market", "insurer"], ["catastrophe", "apac", "protection-gap", "reinsurance"],
 ["菲律賓", "巨災風險", "保障缺口", "風險轉移"],
 "Insurance Business Asia 2026-10-07 報道", "Insurance Business Asia 2026-10-07 報道", "en", 71))

# ── 5. IBM：韓國免費中小企保障的缺口 ──────────────────────────────────
ITEMS.append(mk(
 "ibm-south-korea-sme-free-cover-20261007", "insurancebusinessmag", "pro", "news", "2026-10-07T22:18:00+08:00",
 "https://www.insurancebusinessmag.com/asia/news/sme/south-koreas-free-sme-cover-what-the-limits-leave-exposed-592667.aspx",
 "Insurance Business：韓國免費中小企保障計劃 上限與除外揭示商業險空間",
 "Insurance Business：韓國免費中小企保障計劃 上限與除外揭示商業險空間",
 "Insurance Business Asia 10月7日報道：韓國全羅北道中小企業綜合保險於2026年10月6日推出，由金融服務委員會（FSC）與韓國一般保險協會（GIAK）共同成立的共生基金出資，覆蓋全北特別自治道約24.8萬名經營者、為期一年；年銷售額3億韓圜或以下的商戶自動受保，毋須投保、毋須付費。保障包括：工傷意外補償20萬至40萬韓圜（交通意外除外）、處所火災或爆炸財產損失每次最高5,000萬韓圜、第三方財物（鄰居）火災責任每次最高1,000萬韓圜。報道強調這是全國推行的國家級安排而非地方試點。 [EN原文]",
 "Insurance Business Asia 10月7日報道：韓國全羅北道中小企業綜合保險於2026年10月6日推出，由金融服務委員會（FSC）與韓國一般保險協會（GIAK）共同成立的共生基金出資，覆蓋全北特別自治道約24.8萬名經營者、為期一年；年銷售額3億韓圜或以下的商戶自動受保，毋須投保、毋須付費。保障包括：工傷意外補償20萬至40萬韓圜（交通意外除外）、處所火災或爆炸財產損失每次最高5,000萬韓圜、第三方財物（鄰居）火災責任每次最高1,000萬韓圜。報道強調這是全國推行的國家級安排而非地方試點。 [EN原文]",
 "「政府提供基本盤、商業險補缺口」的模式在亞洲陸續出現。免費保障明確排除營業中斷，等於為經紀劃出清晰的切入問題：客戶的存貨、設備與營運收入實際需要多少保額。",
 "「政府提供基本盤、商業險補缺口」的模式在亞洲陸續出現。免費保障明確排除營業中斷，等於為經紀劃出清晰的切入問題：客戶的存貨、設備與營運收入實際需要多少保額。",
 ("與中小企客戶討論保障時，著眼點放在基本盤之外的口徑（營業中斷、存貨、設備），不作保費比較",
  "與中小企客戶討論保障時，著眼點放在基本盤之外的口徑（營業中斷、存貨、設備），不作保費比較"),
 ("納入政府主導保障計劃與保障缺口研究", "納入政府主導保障計劃與保障缺口研究"),
 ("用於說明商業險在公共基本盤之上的價值定位", "用於說明商業險在公共基本盤之上的價值定位"),
 ("韓國市場的公共保障與商業補充架構參考", "韓國市場的公共保障與商業補充架構參考"),
 (2, 2, 2, 1), ["market", "product"], ["product", "protection-gap", "apac", "channel"],
 ["韓國", "中小企保險", "保障缺口", "營業中斷"],
 "Insurance Business Asia 2026-10-07 報道", "Insurance Business Asia 2026-10-07 報道", "en", 72))

# ── 6. IBM：韓國 NHIS 離職申報漏洞與欠費 ──────────────────────────────
ITEMS.append(mk(
 "ibm-south-korea-nhis-fraud-window-20261007", "insurancebusinessmag", "pro", "news", "2026-10-07T23:47:00+08:00",
 "https://www.insurancebusinessmag.com/asia/news/life-insurance/the-fraud-window-in-south-koreas-nhis-opens-the-moment-a-foreign-worker-leaves-592689.aspx",
 "Insurance Business：韓國國民健康保險外籍勞工離職漏洞 五年核銷477億韓圜",
 "Insurance Business：韓國國民健康保險外籍勞工離職漏洞 五年核銷477億韓圜",
 "Insurance Business Asia 10月7日報道（引述韓國國會預算辦公室10月5日報告）：部分離韓外籍勞工把外國人登錄證及健康保險資格文件交給留在韓國的人，後者藉此就醫或取得處方藥物出口。制度上國民健康保險（NHIS）保障在投保人離境期間應中止，但中止須以居留狀態更新為前提；僱主若不向 NHIS 申報外籍勞工已離職，保障便持續有效，形成漏洞。截至2025年底，外籍人士及海外韓人的欠繳 NHIS 保費達375億韓圜（約2,790萬美元）；過去五年有134,505宗、合計477億韓圜被列為無法收回而核銷。外籍人士欠費在2021至2025年間上升42%（由264億韓圜增至375億韓圜），欠費住戶由21,728戶增58.1%至34,349戶，其中33,725戶屬外籍人士、欠款344億韓圜。 [EN原文]",
 "Insurance Business Asia 10月7日報道（引述韓國國會預算辦公室10月5日報告）：部分離韓外籍勞工把外國人登錄證及健康保險資格文件交給留在韓國的人，後者藉此就醫或取得處方藥物出口。制度上國民健康保險（NHIS）保障在投保人離境期間應中止，但中止須以居留狀態更新為前提；僱主若不向 NHIS 申報外籍勞工已離職，保障便持續有效，形成漏洞。截至2025年底，外籍人士及海外韓人的欠繳 NHIS 保費達375億韓圜（約2,790萬美元）；過去五年有134,505宗、合計477億韓圜被列為無法收回而核銷。外籍人士欠費在2021至2025年間上升42%（由264億韓圜增至375億韓圜），欠費住戶由21,728戶增58.1%至34,349戶，其中33,725戶屬外籍人士、欠款344億韓圜。 [EN原文]",
 "公共醫保的「離境不停保」漏洞顯示制度完整性缺口，正好說明私營補充醫療保障在韓國的空間；對從事跨境僱員團體保險的同業，離職申報流程是現成的風險自查問題。",
 "公共醫保的「離境不停保」漏洞顯示制度完整性缺口，正好說明私營補充醫療保障在韓國的空間；對從事跨境僱員團體保險的同業，離職申報流程是現成的風險自查問題。",
 ("涉及外籍勞工保障時，聚焦合規申報與保障期銜接，不評論個別司法管轄區的稅務或執法",
  "涉及外籍勞工保障時，聚焦合規申報與保障期銜接，不評論個別司法管轄區的稅務或執法"),
 ("納入醫保制度誠信與反欺詐情報", "納入醫保制度誠信與反欺詐情報"),
 ("用於說明公共與私營醫保的分工與缺口", "用於說明公共與私營醫保的分工與缺口"),
 ("跨境僱員團體保障的申報與期間管理啟示", "跨境僱員團體保障的申報與期間管理啟示"),
 (1, 3, 2, 2), ["market", "reg"], ["fraud", "health", "apac", "enforcement"],
 ["韓國", "國民健康保險", "外籍勞工", "保險欺詐"],
 "Insurance Business Asia 2026-10-07 報道", "Insurance Business Asia 2026-10-07 報道", "en", 72))

# ── 7. Insurance Asia：安聯高層調整 ───────────────────────────────────
ITEMS.append(mk(
 "iaasia-allianz-ceo-reshuffle-kunzmann-20261006", "insuranceasia", "pro", "news", "2026-10-06T05:45:00+08:00",
 "https://insuranceasia.com/insurance/news/allianz-reshuffles-ceos-after-kunzmann-board-move",
 "安聯集團調整子公司CEO：Kroetz 接掌 Allianz Partners，Floquet 接掌 Allianz Direct",
 "安聯集團調整子公司CEO：Kroetz 接掌 Allianz Partners，Floquet 接掌 Allianz Direct",
 "Insurance Asia 10月6日報道：因 Tomas Kunzmann 獲委任進入安聯集團（Allianz SE）董事會，安聯公布接任安排——現任 Allianz Direct 行政總裁 Philipp Kroetz 於2026年11月1日出任 Allianz Partners 行政總裁；Allianz Partners 現任營運總監 Laurent Floquet 同日接任 Allianz Direct 行政總裁。Kroetz 自2022年1月執掌 Allianz Direct，期內客戶數增至逾320萬、覆蓋五個歐洲市場；Floquet 於2014年加入安聯，此前為 Accenture 合夥人逾十年。兩項任命仍待監管批准；Allianz Partners 營運總監的接任人選稍後公布。 [EN原文]",
 "Insurance Asia 10月6日報道：因 Tomas Kunzmann 獲委任進入安聯集團（Allianz SE）董事會，安聯公布接任安排——現任 Allianz Direct 行政總裁 Philipp Kroetz 於2026年11月1日出任 Allianz Partners 行政總裁；Allianz Partners 現任營運總監 Laurent Floquet 同日接任 Allianz Direct 行政總裁。Kroetz 自2022年1月執掌 Allianz Direct，期內客戶數增至逾320萬、覆蓋五個歐洲市場；Floquet 於2014年加入安聯，此前為 Accenture 合夥人逾十年。兩項任命仍待監管批准；Allianz Partners 營運總監的接任人選稍後公布。 [EN原文]",
 "Allianz Partners 是安聯的全球健康與援助業務平台，其掌舵人變動會影響該集團在區內醫療、旅遊及援助類產品的策略取向，值得持續跟進。",
 "Allianz Partners 是安聯的全球健康與援助業務平台，其掌舵人變動會影響該集團在區內醫療、旅遊及援助類產品的策略取向，值得持續跟進。",
 ("同業高層變動僅作市場資訊，不與產品比較掛鈎", "同業高層變動僅作市場資訊，不與產品比較掛鈎"),
 ("納入保司動態情報", "納入保司動態情報"),
 ("用於掌握主要保險集團的人事與業務布局", "用於掌握主要保險集團的人事與業務布局"),
 ("國際保險集團亞太策略的人事前瞻指標", "國際保險集團亞太策略的人事前瞻指標"),
 (1, 1, 2, 2), ["insurer"], ["people", "governance", "apac", "talent"],
 ["安聯", "人事任命", "Allianz Partners", "監管批准"],
 "Insurance Asia 2026-10-06 報道", "Insurance Asia 2026-10-06 報道", "en", 71))

# ── 8. Insurance Asia：Aon 強化日本網絡 ───────────────────────────────
ITEMS.append(mk(
 "iaasia-aon-japan-leadership-20261006", "insuranceasia", "pro", "news", "2026-10-06T06:30:00+08:00",
 "https://insuranceasia.com/insurance/news/aon-strengthens-japan-network-two-leadership-appointments",
 "Aon 委任 Naoki Kido 及 Yuki Tanemura 強化日本全球解決方案網絡",
 "Aon 委任 Naoki Kido 及 Yuki Tanemura 強化日本全球解決方案網絡",
 "Insurance Asia 10月6日報道：Aon plc 委任 Naoki Kido 及 Yuki Tanemura 出任日本全球解決方案（Japan Global Solutions）領導職務。Kido 自2026年9月30日起任全球主管，駐東京，向亞太區首席客戶官兼企業客戶主管 Craig Torgius 匯報；他此前為 WTW 日本全球業務組北美區主管，擁有逾20年服務日本跨國企業經驗。Tanemura 自2027年1月1日起任全球首席商務官兼北美主管，駐芝加哥，向 Kido 匯報；他加入 Aon 已20年，曾在日本、東南亞及美國擔任多個領導職位。兩項任命仍須符合相關監管要求。 [EN原文]",
 "Insurance Asia 10月6日報道：Aon plc 委任 Naoki Kido 及 Yuki Tanemura 出任日本全球解決方案（Japan Global Solutions）領導職務。Kido 自2026年9月30日起任全球主管，駐東京，向亞太區首席客戶官兼企業客戶主管 Craig Torgius 匯報；他此前為 WTW 日本全球業務組北美區主管，擁有逾20年服務日本跨國企業經驗。Tanemura 自2027年1月1日起任全球首席商務官兼北美主管，駐芝加哥，向 Kido 匯報；他加入 Aon 已20年，曾在日本、東南亞及美國擔任多個領導職位。兩項任命仍須符合相關監管要求。 [EN原文]",
 "日本跨國企業的全球保險計劃（global programme）是經紀行競爭的關鍵賽道；Aon 以「東京主管＋芝加哥北美主管」雙任命強化日企外拓支持，反映日企海外布局帶來的風險安排需求。",
 "日本跨國企業的全球保險計劃（global programme）是經紀行競爭的關鍵賽道；Aon 以「東京主管＋芝加哥北美主管」雙任命強化日企外拓支持，反映日企海外布局帶來的風險安排需求。",
 ("同業人事消息僅作行業資訊參考，不作客戶招攬材料",
  "同業人事消息僅作行業資訊參考，不作客戶招攬材料"),
 ("納入同業與渠道情報", "納入同業與渠道情報"),
 ("用於說明全球保險計劃的市場競爭格局", "用於說明全球保險計劃的市場競爭格局"),
 ("日企全球風險安排的經紀渠道背景", "日企全球風險安排的經紀渠道背景"),
 (1, 1, 2, 2), ["market"], ["people", "broker", "apac", "talent"],
 ["Aon", "人事任命", "日本", "全球保險計劃"],
 "Insurance Asia 2026-10-06 報道", "Insurance Asia 2026-10-06 報道", "en", 71))

# ── 9. Insurance Asia：MSIG 馬來西亞原住民房屋火險 ────────────────────
ITEMS.append(mk(
 "iaasia-msig-orang-asli-fire-cover-20261006", "insuranceasia", "pro", "news", "2026-10-06T06:00:00+08:00",
 "https://insuranceasia.com/insurance/news/msig-extends-fire-cover-over-300-orang-asli-homes",
 "MSIG 馬來西亞為逾300間原住民（Orang Asli）房屋提供火險保障",
 "MSIG 馬來西亞為逾300間原住民（Orang Asli）房屋提供火險保障",
 "Insurance Asia 10月6日報道：MSIG Insurance (Malaysia) Bhd 延續與 EPIC Homes 的合作，為該組織為原住民（Orang Asli）家庭興建的房屋提供火險保障，自2018年起累計覆蓋逾300間。2026年 MSIG 支持在 Simpang Pulai 興建兩間房屋：首間於7月由31名員工（包括行政總裁 Ang Yien Chia）聯同義工三日內完成，第二間於9月由25名員工參與。Ang 指2025年有受保房屋因風暴損毀，理賠協助家庭支付維修費用。截至2026年8月，該合作已為逾300間房屋提供保障。 [EN原文]",
 "Insurance Asia 10月6日報道：MSIG Insurance (Malaysia) Bhd 延續與 EPIC Homes 的合作，為該組織為原住民（Orang Asli）家庭興建的房屋提供火險保障，自2018年起累計覆蓋逾300間。2026年 MSIG 支持在 Simpang Pulai 興建兩間房屋：首間於7月由31名員工（包括行政總裁 Ang Yien Chia）聯同義工三日內完成，第二間於9月由25名員工參與。Ang 指2025年有受保房屋因風暴損毀，理賠協助家庭支付維修費用。截至2026年8月，該合作已為逾300間房屋提供保障。 [EN原文]",
 "保險的社會價值（縮窄保障缺口、社區韌性）正成為監管與公眾敘事的重要一環；此類項目是理解「保險如何被期待回應社會需要」的現成案例。",
 "保險的社會價值（縮窄保障缺口、社區韌性）正成為監管與公眾敘事的重要一環；此類項目是理解「保險如何被期待回應社會需要」的現成案例。",
 ("用於說明保險的保障功能與社會價值，不作為產品宣傳素材",
  "用於說明保險的保障功能與社會價值，不作為產品宣傳素材"),
 ("納入保險社會價值與企業責任情報", "納入保險社會價值與企業責任情報"),
 ("團隊文化溝通素材：保險的實際作用", "團隊文化溝通素材：保險的實際作用"),
 ("東南亞保障缺口與社區風險轉移案例", "東南亞保障缺口與社區風險轉移案例"),
 (1, 1, 2, 1), ["insurer", "product"], ["protection-gap", "product", "apac", "claims"],
 ["MSIG", "馬來西亞", "火險", "保障缺口"],
 "Insurance Asia 2026-10-06 報道", "Insurance Asia 2026-10-06 報道", "en", 70))

# ── 10. Artemis：人保財險第二隻「長城再」巨災債券 ─────────────────────
ITEMS.append(mk(
 "artemis-picc-great-wall-re-catbond-3-12m-20261007", "artemis", "pro", "news", "2026-10-07",
 "https://www.artemis.bm/news/picc-pc-new-great-wall-re-catastrophe-bond-said-a-12m-issuance/",
 "Artemis：人保財險第二隻「長城再」巨災債券 規模確認為1,200萬美元",
 "Artemis：人保財險第二隻「長城再」巨災債券 規模確認為1,200萬美元",
 "Artemis 10月7日報道：人保財險（PICC P&C）透過其香港註冊的特殊目的保險公司 Great Wall Re Limited 發行的新一隻巨災債券，據悉規模為1,200萬美元，屬約一年期的再保安排（預定到期日2027年9月30日，尚待確認），保障範圍料為中國境內某類自然災害風險。人保財險2022年底首隻長城再巨災債券規模為3,250萬美元，為約三年期中國地震全額抵押再保，採賠付觸發（indemnity trigger）、逐次事故（per-occurrence）基礎。 [EN原文]",
 "Artemis 10月7日報道：人保財險（PICC P&C）透過其香港註冊的特殊目的保險公司 Great Wall Re Limited 發行的新一隻巨災債券，據悉規模為1,200萬美元，屬約一年期的再保安排（預定到期日2027年9月30日，尚待確認），保障範圍料為中國境內某類自然災害風險。人保財險2022年底首隻長城再巨災債券規模為3,250萬美元，為約三年期中國地震全額抵押再保，採賠付觸發（indemnity trigger）、逐次事故（per-occurrence）基礎。 [EN原文]",
 "內地保險機構以香港特殊目的保險公司發行巨災債券，正是香港「保險相連證券（ILS）」政策方向的實例；對關注風險管理樞紐定位與跨境架構的人而言，這是可追蹤的市場信號。",
 "內地保險機構以香港特殊目的保險公司發行巨災債券，正是香港「保險相連證券（ILS）」政策方向的實例；對關注風險管理樞紐定位與跨境架構的人而言，這是可追蹤的市場信號。",
 ("涉及巨災債券等另類風險轉移工具時，只作架構說明，不涉及任何投資建議",
  "涉及巨災債券等另類風險轉移工具時，只作架構說明，不涉及任何投資建議"),
 ("納入ILS與巨災債券情報庫", "納入ILS與巨災債券情報庫"),
 ("用於說明香港ILS生態與內地保險機構的互動", "用於說明香港ILS生態與內地保險機構的互動"),
 ("香港作為跨境風險轉移平台的具體案例", "香港作為跨境風險轉移平台的具體案例"),
 (1, 2, 2, 3), ["market", "ils"], ["ils", "catastrophe", "china", "cross-border"],
 ["人保財險", "巨災債券", "香港", "保險相連證券"],
 "Artemis 2026-10-07 報道", "Artemis 2026-10-07 報道", "en", 74))

# ── 11. Artemis：UCITS 巨災債券基金資產逼近218億美元 ──────────────────
ITEMS.append(mk(
 "artemis-ucits-catbond-funds-21-8bn-sep-20261007", "artemis", "pro", "news", "2026-10-07",
 "https://www.artemis.bm/news/ucits-catastrophe-bond-funds-keep-growing-near-21-8bn-combined-aum-after-september/",
 "Artemis：UCITS 巨災債券基金資產9月底逼近218億美元 年內增13.25%",
 "Artemis：UCITS 巨災債券基金資產9月底逼近218億美元 年內增13.25%",
 "Artemis 10月7日報道：UCITS 格式巨災債券基金2026年內資產增加逾25億美元，9月底合併管理資產（AUM）達約217.6億美元，年內累計增幅13.25%。第三季仍增近10億美元，但8至9月因新發行管道放緩而增速減慢。該板塊2025年全年增約53億美元（39%）至2024年底191.2億美元；2026年2月首次突破200億美元，6月底達207.6億美元。規模最大的三隻基金合計119.8億美元；前六大（唯一各自逾10億美元的基金）合計逾177億美元，佔板塊約82%。 [EN原文]",
 "Artemis 10月7日報道：UCITS 格式巨災債券基金2026年內資產增加逾25億美元，9月底合併管理資產（AUM）達約217.6億美元，年內累計增幅13.25%。第三季仍增近10億美元，但8至9月因新發行管道放緩而增速減慢。該板塊2025年全年增約53億美元（39%）至2024年底191.2億美元；2026年2月首次突破200億美元，6月底達207.6億美元。規模最大的三隻基金合計119.8億美元；前六大（唯一各自逾10億美元的基金）合計逾177億美元，佔板塊約82%。 [EN原文]",
 "UCITS 巨災債券基金是巨災風險資本市場化的主要載體，其 AUM 走勢直接反映機構資金對再保風險的胃納，是判斷承保能力與費率走向的滯後但可靠的指標。",
 "UCITS 巨災債券基金是巨災風險資本市場化的主要載體，其 AUM 走勢直接反映機構資金對再保風險的胃納，是判斷承保能力與費率走向的滯後但可靠的指標。",
 ("向客戶說明另類風險轉移時，只引述公開市場規模數據，不涉及投資建議",
  "向客戶說明另類風險轉移時，只引述公開市場規模數據，不涉及投資建議"),
 ("納入ILS與另類資本情報庫", "納入ILS與另類資本情報庫"),
 ("用於說明承保能力與資本市場的關係", "用於說明承保能力與資本市場的關係"),
 ("ILS 資本來源的規模視角", "ILS 資本來源的規模視角"),
 (1, 3, 2, 2), ["market"], ["ils", "capital", "catastrophe", "returns"],
 ["巨災債券", "UCITS", "另類資本", "管理資產"],
 "Artemis 2026-10-07 報道", "Artemis 2026-10-07 報道", "en", 71))

# ── 12. Artemis：Pacific Life Re 首進美國長壽再保市場 ─────────────────
ITEMS.append(mk(
 "artemis-pacific-life-re-us-longevity-3bn-20261007", "artemis", "pro", "news", "2026-10-07",
 "https://www.artemis.bm/news/pacific-life-re-enters-us-longevity-reinsurance-market-with-3bn-american-national-deal/",
 "Artemis：Pacific Life Re 以30億美元交易首進美國長壽再保市場",
 "Artemis：Pacific Life Re 以30億美元交易首進美國長壽再保市場",
 "Artemis 10月7日報道：壽險及健康險再保公司 Pacific Life Re 與 American National Insurance Company 達成30億美元長壽再保協議，承接與30億美元退休金風險轉移（PRT, Pension Risk Transfer）負債相關的長壽風險。此舉標誌其 Savings & Retirement 業務首次進入美國市場，並延伸其在英國、荷蘭及加拿大的既有版圖。該公司 Savings & Retirement 執行副總裁 Phill Beach 表示，交易體現其大規模交付長壽方案的能力；交易由國際律師事務所 Eversheds Sutherland 提供支持。 [EN原文]",
 "Artemis 10月7日報道：壽險及健康險再保公司 Pacific Life Re 與 American National Insurance Company 達成30億美元長壽再保協議，承接與30億美元退休金風險轉移（PRT, Pension Risk Transfer）負債相關的長壽風險。此舉標誌其 Savings & Retirement 業務首次進入美國市場，並延伸其在英國、荷蘭及加拿大的既有版圖。該公司 Savings & Retirement 執行副總裁 Phill Beach 表示，交易體現其大規模交付長壽方案的能力；交易由國際律師事務所 Eversheds Sutherland 提供支持。 [EN原文]",
 "退休金風險轉移與長壽風險再保，是成熟市場應對人口老化的主要金融工具；亞洲市場（含香港）的退休與年金需求趨升，這個領域的國際玩家動向值得長期跟蹤。",
 "退休金風險轉移與長壽風險再保，是成熟市場應對人口老化的主要金融工具；亞洲市場（含香港）的退休與年金需求趨升，這個領域的國際玩家動向值得長期跟蹤。",
 ("涉及退休與長壽風險議題時，只作趨勢說明，不作任何回報或產品承諾",
  "涉及退休與長壽風險議題時，只作趨勢說明，不作任何回報或產品承諾"),
 ("納入長壽風險轉移與再保情報", "納入長壽風險轉移與再保情報"),
 ("用於說明退休金風險轉移的國際格局", "用於說明退休金風險轉移的國際格局"),
 ("跨境退休與長壽風險管理的機構視角", "跨境退休與長壽風險管理的機構視角"),
 (1, 2, 2, 2), ["market", "insurer"], ["reinsurance", "longevity", "capital", "returns"],
 ["Pacific Life Re", "長壽風險", "退休金風險轉移", "再保險"],
 "Artemis 2026-10-07 報道", "Artemis 2026-10-07 報道", "en", 71))

# ── 13. Artemis：熱帶風暴 Isaias 逼近墨西哥灣 ─────────────────────────
ITEMS.append(mk(
 "artemis-hurricane-isaias-gulf-coast-20261007", "artemis", "pro", "news", "2026-10-07",
 "https://www.artemis.bm/news/tropical-storm-isaias-forms-nhc-forecasts-hurricane-prior-to-gulf-coast-landfall/",
 "Artemis：熱帶風暴 Isaias 形成 料登陸墨西哥灣沿岸前增強為颶風",
 "Artemis：熱帶風暴 Isaias 形成 料登陸墨西哥灣沿岸前增強為颶風",
 "Artemis 10月7日報道：一個大西洋熱帶低氣壓增強為熱帶風暴 Isaias，美國國家颶風中心（NHC）預料其在未來一至兩日快速增強，周四前成為颶風，並朝墨西哥灣沿岸推進。最新預報顯示登陸前持續風速約90至95節（約110英里/小時，二級颶風），登陸前或有所減弱；風暴潮最高達7英尺（Ocean Springs 至 Indian Pass 及 Mobile Bay 一帶），雨量3至6英寸、局部達10英寸。報道指出，即使季節預測數字偏少，條件轉趨有利時短期內仍可形成威脅，對保險及 ILS 市場屬需監察的變化。 [EN原文]",
 "Artemis 10月7日報道：一個大西洋熱帶低氣壓增強為熱帶風暴 Isaias，美國國家颶風中心（NHC）預料其在未來一至兩日快速增強，周四前成為颶風，並朝墨西哥灣沿岸推進。最新預報顯示登陸前持續風速約90至95節（約110英里/小時，二級颶風），登陸前或有所減弱；風暴潮最高達7英尺（Ocean Springs 至 Indian Pass 及 Mobile Bay 一帶），雨量3至6英寸、局部達10英寸。報道指出，即使季節預測數字偏少，條件轉趨有利時短期內仍可形成威脅，對保險及 ILS 市場屬需監察的變化。 [EN原文]",
 "巨災事件是再保與 ILS 市場的即時變數；本案說明「淡季不等於無風險」，也提醒風險溝通應以事件而非季節平均為基礎。",
 "巨災事件是再保與 ILS 市場的即時變數；本案說明「淡季不等於無風險」，也提醒風險溝通應以事件而非季節平均為基礎。",
 ("客戶關注巨災新聞時，只引述官方氣象機構預報，不作損失或賠付推測",
  "客戶關注巨災新聞時，只引述官方氣象機構預報，不作損失或賠付推測"),
 ("納入巨災事件監察", "納入巨災事件監察"),
 ("用於說明巨災事件對再保市場的即時影響", "用於說明巨災事件對再保市場的即時影響"),
 ("美國颶風風險對全球再保資本的傳導路徑", "美國颶風風險對全球再保資本的傳導路徑"),
 (1, 2, 1, 2), ["market"], ["catastrophe", "cat-risk", "ils", "climate"],
 ["颶風", "Isaias", "墨西哥灣", "巨災風險"],
 "Artemis 2026-10-07 報道", "Artemis 2026-10-07 報道", "en", 70))

# ── 14. Artemis：德州 TWIA 2027年再保需求 ─────────────────────────────
ITEMS.append(mk(
 "artemis-twia-2027-catbond-need-2-05bn-20261007", "artemis", "pro", "news", "2026-10-07",
 "https://www.artemis.bm/news/twia-forecasts-2-05bn-reinsurance-cat-bond-need-for-2027-proposes-18-budget-reduction/",
 "Artemis：德州 TWIA 預計2027年再保及巨災債券需求20.5億美元 風險轉移預算擬降約18%",
 "Artemis：德州 TWIA 預計2027年再保及巨災債券需求20.5億美元 風險轉移預算擬降約18%",
 "Artemis 10月7日報道：德州風災保險協會（TWIA）預計2027年需約20.5億美元再保及巨災債券，較2026年減少逾10%，主因巨災儲備信託基金（CRTF）預計由2026年的2,500萬美元增至最多3.5億美元。2027年1-in-50年最低所需資金水平料為44億美元（2026年為43.051億美元），董事會近日否決回復至100年回歸期的建議。2026年中期續保取得約22.8億美元風險轉移，其中巨災債券市場提供10.5億美元。2027年風險轉移預算料約1.73億美元，較2026年約2.1億美元下降近18%。 [EN原文]",
 "Artemis 10月7日報道：德州風災保險協會（TWIA）預計2027年需約20.5億美元再保及巨災債券，較2026年減少逾10%，主因巨災儲備信託基金（CRTF）預計由2026年的2,500萬美元增至最多3.5億美元。2027年1-in-50年最低所需資金水平料為44億美元（2026年為43.051億美元），董事會近日否決回復至100年回歸期的建議。2026年中期續保取得約22.8億美元風險轉移，其中巨災債券市場提供10.5億美元。2027年風險轉移預算料約1.73億美元，較2026年約2.1億美元下降近18%。 [EN原文]",
 "TWIA 是巨災債券市場最大的機構發行人之一；其需求預測與預算下降，是「費率走軟＋儲備充足」共同作用的實例，對理解巨災債券供求與定價週期有參考價值。",
 "TWIA 是巨災債券市場最大的機構發行人之一；其需求預測與預算下降，是「費率走軟＋儲備充足」共同作用的實例，對理解巨災債券供求與定價週期有參考價值。",
 ("涉及巨災保險機制時，只作制度與市場說明，不引伸至本地產品",
  "涉及巨災保險機制時，只作制度與市場說明，不引伸至本地產品"),
 ("納入巨災債券供求情報", "納入巨災債券供求情報"),
 ("用於說明巨災保障與再保定價週期", "用於說明巨災保障與再保定價週期"),
 ("公共巨災保險機制的國際對標案例", "公共巨災保險機制的國際對標案例"),
 (1, 3, 2, 2), ["market", "reg"], ["reinsurance", "catastrophe", "ils", "pricing"],
 ["TWIA", "巨災債券", "再保險", "德州"],
 "Artemis 2026-10-07 報道", "Artemis 2026-10-07 報道", "en", 71))

# ── 15. Artemis／Plenum：9月巨災債券風險息差跌9.5% ────────────────────
ITEMS.append(mk(
 "artemis-catbond-spreads-fall-sep-plenum-20261007", "artemis", "pro", "news", "2026-10-07",
 "https://www.artemis.bm/news/cat-bond-risk-spreads-fall-9-5-in-september-but-rising-risk-free-rate-helps-to-offset-plenum/",
 "Artemis／Plenum：9月巨災債券風險息差跌9.5% 抵押品收益率升至逾一年新高",
 "Artemis／Plenum：9月巨災債券風險息差跌9.5% 抵押品收益率升至逾一年新高",
 "Artemis 10月7日報道（引述 Plenum Investments 數據）：2026年9月巨災債券保險風險息差下跌9.5%，由8月28日的5.05%降至9月25日的4.57%，主要受風季季節性效應及近期新發行息差偏低影響。同期美國國債收益率上升，帶動抵押品收益率由3.81%升至4.17%（逾一年最高），抵銷部分影響；整體票息收益率由8月28日的8.87%微降至9月25日的8.74%。Plenum 表示，9月是夏季各月息差收窄幅度最大的一個月，預期10月起收窄速度因季節效應進一步放緩。 [EN原文]",
 "Artemis 10月7日報道（引述 Plenum Investments 數據）：2026年9月巨災債券保險風險息差下跌9.5%，由8月28日的5.05%降至9月25日的4.57%，主要受風季季節性效應及近期新發行息差偏低影響。同期美國國債收益率上升，帶動抵押品收益率由3.81%升至4.17%（逾一年最高），抵銷部分影響；整體票息收益率由8月28日的8.87%微降至9月25日的8.74%。Plenum 表示，9月是夏季各月息差收窄幅度最大的一個月，預期10月起收窄速度因季節效應進一步放緩。 [EN原文]",
 "巨災債券息差是再保定價的市場化讀數。風險息差收窄而無風險利率上升的組合，說明投資者回報的構成正在位移，對理解再保條款與價格走勢有前瞻意義。",
 "巨災債券息差是再保定價的市場化讀數。風險息差收窄而無風險利率上升的組合，說明投資者回報的構成正在位移，對理解再保條款與價格走勢有前瞻意義。",
 ("引用市場息差數據時，須註明屬第三方指數與觀察日期，不代表任何投資回報",
  "引用市場息差數據時，須註明屬第三方指數與觀察日期，不代表任何投資回報"),
 ("納入ILS定價與資本市場情報", "納入ILS定價與資本市場情報"),
 ("用於說明再保定價與資本市場利率的互動", "用於說明再保定價與資本市場利率的互動"),
 ("全球利率環境對風險轉移定價的傳導", "全球利率環境對風險轉移定價的傳導"),
 (1, 3, 2, 2), ["market"], ["ils", "catastrophe", "pricing", "returns"],
 ["巨災債券", "息差", "Plenum", "抵押品收益率"],
 "Artemis 2026-10-07 報道", "Artemis 2026-10-07 報道", "en", 71))

# ── 16. Artemis：KCC 推出美國強對流風暴模型5.0 ────────────────────────
ITEMS.append(mk(
 "artemis-kcc-us-scs-model-v5-20261007", "artemis", "pro", "news", "2026-10-07",
 "https://www.artemis.bm/news/kcc-updates-and-enhances-us-severe-convective-storm-model/",
 "Artemis：Karen Clark & Company 推出美國強對流風暴模型5.0 引入AI四維大氣建模",
 "Artemis：Karen Clark & Company 推出美國強對流風暴模型5.0 引入AI四維大氣建模",
 "Artemis 10月7日報道：巨災風險模型公司 Karen Clark & Company（KCC）發布美國強對流風暴（SCS）模型5.0，細化龍捲風爆發（tornado outbreaks）技術及東南沿岸龍捲風與風力強度計算，並以 AI 驅動的四維（4D）大氣建模取代單純依賴歷史風暴報告，以呈現冰雹、龍捲風及直線風損失的物理過程；同時調整組合屋（manufactured homes）脆弱度函數、按樓齡更新獨立屋冰雹脆弱度，並引入屋頂年齡加減項及可自訂屋頂重置價值，方便快速調整屋頂實際現金價值（ACV）批註。KCC 指頻率類風險模型若數年未更新便已過時，故每年更新。 [EN原文]",
 "Artemis 10月7日報道：巨災風險模型公司 Karen Clark & Company（KCC）發布美國強對流風暴（SCS）模型5.0，細化龍捲風爆發（tornado outbreaks）技術及東南沿岸龍捲風與風力強度計算，並以 AI 驅動的四維（4D）大氣建模取代單純依賴歷史風暴報告，以呈現冰雹、龍捲風及直線風損失的物理過程；同時調整組合屋（manufactured homes）脆弱度函數、按樓齡更新獨立屋冰雹脆弱度，並引入屋頂年齡加減項及可自訂屋頂重置價值，方便快速調整屋頂實際現金價值（ACV）批註。KCC 指頻率類風險模型若數年未更新便已過時，故每年更新。 [EN原文]",
 "AI 正被直接寫入巨災模型的物理建模層，而非只作輔助工具；模型的「更新頻率」本身成為承保與定價的關鍵變數，是風險科技值得留意的方向。",
 "AI 正被直接寫入巨災模型的物理建模層，而非只作輔助工具；模型的「更新頻率」本身成為承保與定價的關鍵變數，是風險科技值得留意的方向。",
 ("涉及風險模型時，說明其屬行業定價工具，不作個別保單核保結果推論",
  "涉及風險模型時，說明其屬行業定價工具，不作個別保單核保結果推論"),
 ("納入風險模型與科技情報", "納入風險模型與科技情報"),
 ("用於說明科技如何重塑風險量化", "用於說明科技如何重塑風險量化"),
 ("跨境風險定價工具的一致性議題", "跨境風險定價工具的一致性議題"),
 (1, 2, 2, 2), ["tech"], ["cat-risk", "data", "ai", "underwriting"],
 ["KCC", "風險模型", "強對流風暴", "人工智能"],
 "Artemis 2026-10-07 報道", "Artemis 2026-10-07 報道", "en", 70))

# ── 17. Artemis：Hannover Re 談第三方資本 ─────────────────────────────
ITEMS.append(mk(
 "artemis-hannover-re-third-party-capital-althoff-20261006", "artemis", "pro", "news", "2026-10-06",
 "https://www.artemis.bm/news/third-party-capital-more-than-just-complementary-capacity-for-hannover-re-althoff/",
 "Artemis：Hannover Re 董事 Althoff 稱第三方資本「更多是夥伴與機遇」",
 "Artemis：Hannover Re 董事 Althoff 稱第三方資本「更多是夥伴與機遇」",
 "Artemis 10月6日報道：Hannover Re 財險執行董事會成員 Sven Althoff 在 Aon 主辦、以再保與 ILS 資本及增長為題的網絡研討會上表示，第三方資本對集團而言「固然是競爭來源之一，但我們更看重其夥伴與機遇的一面」，並以轉分保（retrocession）作為調控波動的重要工具。他指集團幾乎在所有財險層級（事件型、總括型、成數型）都與 ILS 資本長期合作，並提供抵押前臺（collateralized fronting）、巨災債券轉化等服務，最新一項是設立 Hannover Re Capital Partners，以代理承保形式按投資者風險偏好代為承做組合。 [EN原文]",
 "Artemis 10月6日報道：Hannover Re 財險執行董事會成員 Sven Althoff 在 Aon 主辦、以再保與 ILS 資本及增長為題的網絡研討會上表示，第三方資本對集團而言「固然是競爭來源之一，但我們更看重其夥伴與機遇的一面」，並以轉分保（retrocession）作為調控波動的重要工具。他指集團幾乎在所有財險層級（事件型、總括型、成數型）都與 ILS 資本長期合作，並提供抵押前臺（collateralized fronting）、巨災債券轉化等服務，最新一項是設立 Hannover Re Capital Partners，以代理承保形式按投資者風險偏好代為承做組合。 [EN原文]",
 "大型再保人如何「與 ILS 資本共處」，決定了未來承保能力的結構與費用；其態度由「競爭」轉向「夥伴」，是近年市場軟化的重要組織性原因。",
 "大型再保人如何「與 ILS 資本共處」，決定了未來承保能力的結構與費用；其態度由「競爭」轉向「夥伴」，是近年市場軟化的重要組織性原因。",
 ("引用業界觀點時標明屬受訪者意見，不代表市場共識",
  "引用業界觀點時標明屬受訪者意見，不代表市場共識"),
 ("納入ILS與再保策略情報", "納入ILS與再保策略情報"),
 ("用於說明再保人與另類資本的關係演變", "用於說明再保人與另類資本的關係演變"),
 ("跨境風險安排的資本來源結構", "跨境風險安排的資本來源結構"),
 (1, 2, 2, 2), ["market"], ["reinsurance", "ils", "capital", "talent"],
 ["Hannover Re", "第三方資本", "轉分保", "ILS"],
 "Artemis 2026-10-06 報道", "Artemis 2026-10-06 報道", "en", 70))

# ── 18. Artemis 蒙特卡洛圓桌：ILS 投資者情緒穩健強烈 ──────────────────
ITEMS.append(mk(
 "artemis-rvs-roundtable-ils-appetite-20261006", "artemis", "pro", "report", "2026-10-06",
 "https://www.artemis.bm/news/rvs-roundtable-ils-investor-appetite-and-sentiment-is-sound-and-strong/",
 "Artemis 圓桌：ILS 投資者興趣與情緒「穩健而強烈」",
 "Artemis 圓桌：ILS 投資者興趣與情緒「穩健而強烈」",
 "Artemis 10月6日報道：Artemis 第七屆蒙特卡洛高管圓桌（於再保業年度 Rendez-Vous de Septembre 期間舉行，由 SCOR Investment Partners 及 Vantage Risk 贊助，九位 ILS 及再保專家參與）指出，ILS 投資者興趣全面而強勁，巨災債券市場總回報仍具吸引力。SCOR Investment Partners 保險相連證券主管 Sidney Rostan 指，年內巨災債券發行連創紀錄、息差雖下降但近三年回報優異，總回報約9%，相對價值仍突出；私募 ILS 的 rate-on-line 仍屬充足，結構與條款健康，近三年表現強勁。圓桌完整報告將於數週內發布。 [EN原文]",
 "Artemis 10月6日報道：Artemis 第七屆蒙特卡洛高管圓桌（於再保業年度 Rendez-Vous de Septembre 期間舉行，由 SCOR Investment Partners 及 Vantage Risk 贊助，九位 ILS 及再保專家參與）指出，ILS 投資者興趣全面而強勁，巨災債券市場總回報仍具吸引力。SCOR Investment Partners 保險相連證券主管 Sidney Rostan 指，年內巨災債券發行連創紀錄、息差雖下降但近三年回報優異，總回報約9%，相對價值仍突出；私募 ILS 的 rate-on-line 仍屬充足，結構與條款健康，近三年表現強勁。圓桌完整報告將於數週內發布。 [EN原文]",
 "ILS 資金胃納仍是承保能力的核心支撐；與同日 Plenum 息差數據、Hannover Re 表態並讀，可拼出「資本充裕、定價偏軟」的完整市場圖景。",
 "ILS 資金胃納仍是承保能力的核心支撐；與同日 Plenum 息差數據、Hannover Re 表態並讀，可拼出「資本充裕、定價偏軟」的完整市場圖景。",
 ("業界觀點與回報數字只作市場資訊，不構成任何投資建議或回報承諾",
  "業界觀點與回報數字只作市場資訊，不構成任何投資建議或回報承諾"),
 ("納入ILS市場情緒情報", "納入ILS市場情緒情報"),
 ("用於判斷承保能力與再保週期", "用於判斷承保能力與再保週期"),
 ("國際再保資本情緒對區域定價的傳導", "國際再保資本情緒對區域定價的傳導"),
 (1, 3, 2, 2), ["market"], ["ils", "capital", "reinsurance", "market"],
 ["ILS", "巨災債券", "投資者情緒", "再保險"],
 "Artemis 2026-10-06 報道", "Artemis 2026-10-06 報道", "en", 70))

# ── 19. Artemis：CalPERS 擬增 ILS 配置 ────────────────────────────────
ITEMS.append(mk(
 "artemis-calpers-ils-climate-100bn-20261006", "artemis", "pro", "news", "2026-10-06",
 "https://www.artemis.bm/news/calpers-wants-to-increase-ils-investments-to-contribute-to-climate-solutions-goal-bloomberg/",
 "Artemis：CalPERS 擬增 ILS 配置 配合2030年千億美元氣候方案目標",
 "Artemis：CalPERS 擬增 ILS 配置 配合2030年千億美元氣候方案目標",
 "Artemis 10月6日報道（引述彭博）：資產規模約6,370億美元的美國加州公務員退休基金（CalPERS）正探討增加保險相連證券（ILS）配置，該資產類別被視為有助達成其2030年前投入1,000億美元於「氣候方案」的目標。CalPERS 自2025年起配置巨災債券及 ILS，透過三個專業管理人設立三個渠道：Integral ILS（抵押再保）、Swiss Re Insurance-Linked Strategies（巨災債券）及 Tangency Capital（成數再保）。2026年中，其三項 ILS 配置合計估值接近25億美元，上半年增約70%。報道指大型退休基金若要快速達到規模，或需與大型再保人建立更直接的合作關係。 [EN原文]",
 "Artemis 10月6日報道（引述彭博）：資產規模約6,370億美元的美國加州公務員退休基金（CalPERS）正探討增加保險相連證券（ILS）配置，該資產類別被視為有助達成其2030年前投入1,000億美元於「氣候方案」的目標。CalPERS 自2025年起配置巨災債券及 ILS，透過三個專業管理人設立三個渠道：Integral ILS（抵押再保）、Swiss Re Insurance-Linked Strategies（巨災債券）及 Tangency Capital（成數再保）。2026年中，其三項 ILS 配置合計估值接近25億美元，上半年增約70%。報道指大型退休基金若要快速達到規模，或需與大型再保人建立更直接的合作關係。 [EN原文]",
 "巨型退休基金把 ILS 納入「氣候方案」配置，屬結構性資金來源的變化；這類長線資金進場，會持續壓低再保價格並改變承保能力格局。",
 "巨型退休基金把 ILS 納入「氣候方案」配置，屬結構性資金來源的變化；這類長線資金進場，會持續壓低再保價格並改變承保能力格局。",
 ("涉及退休基金與資產配置時，只作市場資訊說明，不構成投資建議",
  "涉及退休基金與資產配置時，只作市場資訊說明，不構成投資建議"),
 ("納入機構資金與ILS情報", "納入機構資金與ILS情報"),
 ("用於說明長線資金與再保市場的關係", "用於說明長線資金與再保市場的關係"),
 ("跨境退休資產與氣候風險投資的趨勢", "跨境退休資產與氣候風險投資的趨勢"),
 (1, 3, 2, 2), ["market", "family"], ["ils", "capital", "climate", "returns"],
 ["CalPERS", "ILS", "氣候方案", "退休基金"],
 "Artemis 2026-10-06 報道", "Artemis 2026-10-06 報道", "en", 70))


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
    print('  +', it['id'], '|', it['publishedAt'], '|', it['sourceKey'], '|', it['sourceTier'])
