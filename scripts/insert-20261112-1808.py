#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""一次性插入 2026-11-12 18:08 采集的 8 条（窗口 2026-11-10 20:50 → 2026-11-12 18:08）"""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIVE = os.path.join(BASE, "data", "live-items.json")
NOW = "2026-11-12T18:08:00+08:00"

def mk(**kw):
    d = {
        "id": kw["id"],
        "clusterCount": 1,
        "score": kw["score"],
        "verifyStatus": kw.get("verifyStatus", "pending"),
        "sourceTier": kw["sourceTier"],
        "sourceKey": kw["sourceKey"],
        "title": {"sc": kw["t_sc"], "tc": kw["t_tc"]},
        "summary": {"sc": kw["s_sc"], "tc": kw["s_tc"]},
        "why": {"sc": kw["w_sc"], "tc": kw["w_tc"]},
        "actions": {
            "front": {"sc": kw["a_front"][0], "tc": kw["a_front"][1]} if kw.get("a_front") else {},
            "midback": {"sc": kw["a_mid"][0], "tc": kw["a_mid"][1]} if kw.get("a_mid") else {},
            "lead": {"sc": kw["a_lead"][0], "tc": kw["a_lead"][1]} if kw.get("a_lead") else {},
            "cross": {"sc": kw["a_cross"][0], "tc": kw["a_cross"][1]} if kw.get("a_cross") else {},
        },
        "rolesImpact": {
            "front": kw["r"][0], "midback": kw["r"][1],
            "lead": kw["r"][2], "cross": kw["r"][3],
        },
        "source": {"sc": kw["src"], "lang": kw["lang"]},
        "boards": kw["boards"],
        "themes": kw["themes"],
        "tags": {"sc": kw["tags_sc"], "tc": kw["tags_tc"]},
        "contentKind": kw["kind"],
        "publishedAt": kw["pub"],
        "originalUrl": kw["url"],
        "ingestedAt": NOW,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False,
        "summaryShort": {"sc": kw["s_sc"][:80], "tc": kw["s_tc"][:80]},
    }
    return d

ITEMS = []

# 1. IAIS 年会在港 + 许正宇致辞
ITEMS.append(mk(
    id="iais-2026-hk-fstb-speech-20261112",
    score=88, sourceTier="official", sourceKey="family_office", verifyStatus="verified",
    t_sc="IAIS 2026 年会首度在港举行　许正宇：持牌保险中介逾 12 万、保险专才获批逾百宗",
    t_tc="IAIS 2026 年會首度在港舉行　許正宇：持牌保險中介逾 12 萬、保險專才獲批逾百宗",
    s_sc="国际保险监督官协会（IAIS）2026 年会 11 月 12 至 13 日首度由香港保监局主办，约 120 个司法管辖区、逾 600 名代表出席。财库局局长许正宇致辞指，香港持牌保险中介已逾 12 万人，「提升保险业人才培训计划」十年累计约 2.2 万人参与，人才清单「专项保险专才」与「精算师」两类已批逾 100 宗申请；他并强调应用 AI 须同步完善管治、维持人类监督并能向客户解释决策，保险相连证券资助计划已延长至 2028 年。",
    s_tc="國際保險監督官協會（IAIS）2026 年會 11 月 12 至 13 日首度由香港保監局主辦，約 120 個司法管轄區、逾 600 名代表出席。財庫局局長許正宇致辭指，香港持牌保險中介已逾 12 萬人，「提升保險業人才培訓計劃」十年累計約 2.2 萬人參與，人才清單「專項保險專才」與「精算師」兩類已批逾 100 宗申請；他並強調應用 AI 須同步完善管治、維持人類監督並能向客戶解釋決策，保險相連證券資助計劃已延長至 2028 年。",
    w_sc="这是本周香港监管外交的主场：IAIS 首度在港开年会，亚洲保险论坛 11/13 紧随，等于把「区域风险管理中心」从口号变成主办权。12 万中介与百宗专才获批，是判断本地人才供给松紧最直接的刻度。",
    w_tc="這是本週香港監管外交的主場：IAIS 首度在港開年會，亞洲保險論壇 11/13 緊隨，等於把「區域風險管理中心」從口號變成主辦權。12 萬中介與百宗專才獲批，是判斷本地人才供給鬆緊最直接的刻度。",
    a_front=("理解 AI 管治四要点：知系统限制、留人类监督、能向客户解释、问责到人", "理解 AI 管治四要點：知系統限制、留人類監督、能向客戶解釋、問責到人"),
    a_mid=("年会与论坛议题可作合规培训素材", "年會與論壇議題可作合規培訓素材"),
    a_lead=("关注 11/13 亚洲保险论坛对资产密集型再保与另类投资的表态", "關注 11/13 亞洲保險論壇對資產密集型再保與另類投資的表態"),
    a_cross=("专属自保与保险相连证券政策取向，是跨境架构客户的机会窗口", "專屬自保與保險相連證券政策取向，是跨境架構客戶的機會窗口"),
    r=(2, 2, 3, 2),
    src="财库局（香港商报报道）", lang="zh",
    boards=["reg", "market"], themes=["iais", "talent", "ai-governance"],
    tags_sc=["IAIS", "持牌中介人", "保险专才", "AI管治", "保险相连证券"],
    tags_tc=["IAIS", "持牌中介人", "保險專才", "AI管治", "保險相連證券"],
    kind="speech", pub="2026-11-12T11:30:00+08:00",
    url="https://hkcd.com/hkcdweb/content/2026/11/12/content_8784912.html",
))

# 2. 张云正：保险仅占医疗开支 16%
ITEMS.append(mk(
    id="ia-iais-medical-gap-20261112",
    score=86, sourceTier="official", sourceKey="ia", verifyStatus="pending",
    t_sc="张云正：保险仅占香港医疗开支 16%、政府补贴 51%　65 岁以上仅两成受保",
    t_tc="張雲正：保險僅佔香港醫療開支 16%、政府補貼 51%　65 歲以上僅兩成受保",
    s_sc="保监局行政总监张云正于 IAIS 年会表示，香港正步入超高龄社会，约 700 万人口仅约一半有保险，65 岁以上仅两成受保；保险仅占整体医疗开支约 16%，政府补贴达 51%，而医疗通胀每年约 10%，政府长远难以独力支撑。他提到监管理念正由「规管」转向争取「协同」，支持险企推出配合北上养老的年金计划，并推动气候模型项目以发展基差风险低的参数型保险。",
    s_tc="保監局行政總監張雲正於 IAIS 年會表示，香港正步入超高齡社會，約 700 萬人口僅約一半有保險，65 歲以上僅兩成受保；保險僅佔整體醫療開支約 16%，政府補貼達 51%，而醫療通脹每年約 10%，政府長遠難以獨力支撐。他提到監管理念正由「規管」轉向爭取「協同」，支持險企推出配合北上養老的年金計劃，並推動氣候模型項目以發展基差風險低的參數型保險。",
    w_sc="「16% 对 51%」是谈保障缺口最硬的底稿——它不讲收益，只讲谁在付钱，比任何演示利率都更能说服客户为何要买医疗与年金。",
    w_tc="「16% 對 51%」是談保障缺口最硬的底稿——它不講收益，只講誰在付錢，比任何演示利率都更能說服客戶為何要買醫療與年金。",
    a_front=("用「保险只付 16%、政府付 51%」开场谈医疗缺口", "用「保險只付 16%、政府付 51%」開場談醫療缺口"),
    a_mid=("医疗通胀 10% 与补贴可持续性，可作产品培训背景", "醫療通脹 10% 與補貼可持續性，可作產品培訓背景"),
    a_lead=("关注北上养老年金与跨境福利支付打通进度", "關注北上養老年金與跨境福利支付打通進度"),
    a_cross=("医疗纪录互通与跨境救护车安排，是港人在内地养老的落地条件", "醫療紀錄互通與跨境救護車安排，是港人在內地養老的落地條件"),
    r=(3, 1, 2, 2),
    src="保监局（香港电台报道）", lang="zh",
    boards=["market", "product"], themes=["protection-gap", "medical-inflation", "annuity"],
    tags_sc=["保障缺口", "医疗通胀", "年金", "北上养老", "参数型保险"],
    tags_tc=["保障缺口", "醫療通脹", "年金", "北上養老", "參數型保險"],
    kind="speech", pub="2026-11-12",
    url="https://news.rthk.hk/rthk/ch/component/k2/1877516-20261112.htm",
))

# 3. HKMA + IA 联合执法
ITEMS.append(mk(
    id="hkma-ia-lim-ka-kit-ban-20261111",
    score=88, sourceTier="official", sourceKey="hkma", verifyStatus="verified",
    t_sc="金管局与保监局联合执法：银行前代理施压八客买医保、两度诱改身高体重　禁牌九个月",
    t_tc="金管局與保監局聯合執法：銀行前代理施壓八客買醫保、兩度誘改身高體重　禁牌九個月",
    s_sc="金管局与保监局 11 月 11 日公布联合执法行动：认可机构前业务代表林嘉杰（牌照编号 IC3091）被禁止申请保险中介人牌照九个月。金管局调查发现，他透过电话销售向八名客户施压，客户要求时间考虑仍被强迫购买医疗保险；其中两次更诱使客户更改身高及体重资料，以符合相关核保要求。行动依据两局跨部门合作谅解备忘录作出。",
    s_tc="金管局與保監局 11 月 11 日公布聯合執法行動：認可機構前業務代表林嘉傑（牌照編號 IC3091）被禁止申請保險中介人牌照九個月。金管局調查發現，他透過電話銷售向八名客戶施壓，客戶要求時間考慮仍被強迫購買醫療保險；其中兩次更誘使客戶更改身高及體重資料，以符合相關核保要求。行動依據兩局跨部門合作諒解備忘錄作出。",
    w_sc="这是「核保资料造假」的教科书案例：改身高体重不是小事，它直接动摇核保基础，后患落在客户日后理赔上。前线话术里最容易被「帮客户美化一下」的那一步，正是不良销售的高危点。",
    w_tc="這是「核保資料造假」的教科書案例：改身高體重不是小事，它直接動搖核保基礎，後患落在客戶日後理賠上。前線話術裡最容易被「幫客戶美化一下」的那一步，正是不良銷售的高危點。",
    a_front=("健康告知与身高体重一律照实，不替客户「优化」", "健康告知與身高體重一律照實，不替客戶「優化」"),
    a_mid=("可作电销话术合规抽查的判例教材", "可作電銷話術合規抽查的判例教材"),
    a_lead=("团队早会 5 分钟案例：施压＋改资料双重红线", "團隊早會 5 分鐘案例：施壓＋改資料雙重紅線"),
    a_cross=None,
    r=(3, 3, 2, 0),
    src="金管局／保监局", lang="zh+en",
    boards=["reg"], themes=["enforcement", "mis-selling", "underwriting-integrity"],
    tags_sc=["联合执法", "不良销售", "核保诚信", "电话销售", "银行保险"],
    tags_tc=["聯合執法", "不良銷售", "核保誠信", "電話銷售", "銀行保險"],
    kind="enforcement", pub="2026-11-11",
    url="https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/11/20261111-3/",
))

# 4. HKMA + SFC 代币化研讨会
ITEMS.append(mk(
    id="hkma-sfc-tokenisation-seminar-20261112",
    score=84, sourceTier="official", sourceKey="hkma", verifyStatus="verified",
    t_sc="金管局与证监会办代币化研讨会　逾 200 人出席、EnsembleTX 已支持 24×7 代币化存款结算",
    t_tc="金管局與證監會辦代幣化研討會　逾 200 人出席、EnsembleTX 已支持 24×7 代幣化存款結算",
    s_sc="金管局与证监会 11 月 11 日合办研讨会，约 200 名业界人士出席，聚焦 Project Ensemble 与代币化证监会认可投资产品。此前金融科技周 2026 公布 EnsembleTX 新阶段，支持代币化存款的 24×7 银行间结算；证监会亦已批准代币化货币市场基金的全天候二级交易，使代币化存款可与投资产品对接、实时优化投资与回报。",
    s_tc="金管局與證監會 11 月 11 日合辦研討會，約 200 名業界人士出席，聚焦 Project Ensemble 與代幣化證監會認可投資產品。此前金融科技周 2026 公布 EnsembleTX 新階段，支持代幣化存款的 24×7 銀行間結算；證監會亦已批准代幣化貨幣市場基金的全天候二級交易，使代幣化存款可與投資產品對接、實時優化投資與回報。",
    w_sc="重点不在技术名词，而在「监管基础设施已到位」：代币化存款与代币化货基可 24 小时互相结算，客户现金管理的规则在变，保险侧的资金与抵押品安排迟早被牵动。",
    w_tc="重點不在技術名詞，而在「監管基礎設施已到位」：代幣化存款與代幣化貨基可 24 小時互相結算，客戶現金管理的規則在變，保險側的資金與抵押品安排遲早被牽動。",
    a_front=("向高净值客户解释：代币化≠虚拟货币，是结算轨道升级", "向高淨值客戶解釋：代幣化≠虛擬貨幣，是結算軌道升級"),
    a_mid=("关注代币化产品在适当性、托管与披露上的合规要求", "關注代幣化產品在適當性、託管與披露上的合規要求"),
    a_lead=("观察资产密集型再保与代币化抵押品的结合动向", "觀察資產密集型再保與代幣化抵押品的結合動向"),
    a_cross=("家办层面：代币化货基可作短期现金管理工具", "家辦層面：代幣化貨基可作短期現金管理工具"),
    r=(1, 2, 2, 3),
    src="金管局", lang="zh+en",
    boards=["tech", "market"], themes=["tokenisation", "settlement", "digital-asset"],
    tags_sc=["代币化", "EnsembleTX", "Project Ensemble", "货币市场基金", "结算"],
    tags_tc=["代幣化", "EnsembleTX", "Project Ensemble", "貨幣市場基金", "結算"],
    kind="press", pub="2026-11-12",
    url="https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/11/20261112-3/",
))

# 5. BEA x AIA 银保五年
ITEMS.append(mk(
    id="insuranceasia-bea-aia-bancassurance-20261112",
    score=65, sourceTier="media", sourceKey="insuranceasia", verifyStatus="pending",
    t_sc="东亚银行×友邦银保五年：年化新保费复合增长逾 60%　高净值客成最快增长板块",
    t_tc="東亞銀行×友邦銀保五年：年化新保費複合增長逾 60%　高淨值客成最快增長板塊",
    s_sc="东亚银行公布，与友邦香港的独家银保合作在 2021 至 2025 年间，年化新保费（ANP）复合年增长超过 60%，高净值客户为增长最快的板块之一并持续同比上升。双方于 10 月 26 日举行合作五周年晚宴，逾 250 名嘉宾出席；东亚称随合作进入下一阶段，将继续与友邦提供保障与财富累积方案，包括灵活保障计划。",
    s_tc="東亞銀行公布，與友邦香港的獨家銀保合作在 2021 至 2025 年間，年化新保費（ANP）複合年增長超過 60%，高淨值客戶為增長最快的板塊之一並持續同比上升。雙方於 10 月 26 日舉行合作五週年晚宴，逾 250 名嘉賓出席；東亞稱隨合作進入下一階段，將繼續與友邦提供保障與財富累積方案，包括靈活保障計劃。",
    w_sc="五年 ANP 复合 60% 以上说明高净值仍走「银行＋保险」这条路。对只做经纪渠道的团队，对手不是别家经纪，而是客户身边的客户经理。",
    w_tc="五年 ANP 複合 60% 以上說明高淨值仍走「銀行＋保險」這條路。對只做經紀渠道的團隊，對手不是別家經紀，而是客戶身邊的客戶經理。",
    a_front=("与银保客户比较时，讲清经纪端的产品广度与独立顾问角色", "與銀保客戶比較時，講清經紀端的產品廣度與獨立顧問角色"),
    a_mid=("银保高净值客群的适当性与销售流程要求可作参考", "銀保高淨值客群的適當性與銷售流程要求可作參考"),
    a_lead=("留意银保渠道在高净值段的产品与激励结构变化", "留意銀保渠道在高淨值段的產品與激勵結構變化"),
    a_cross=None,
    r=(2, 1, 3, 0),
    src="Insurance Asia", lang="zh+en",
    boards=["insurer", "market"], themes=["bancassurance", "hnw", "distribution"],
    tags_sc=["银保", "高净值", "年化新保费", "东亚银行", "友邦"],
    tags_tc=["銀保", "高淨值", "年化新保費", "東亞銀行", "友邦"],
    kind="news", pub="2026-11-12",
    url="https://insuranceasia.com/insurance/news/bea-aia-insurance-premiums-grow-over-60-annually-2021",
))

# 6. Talanx 九个月
ITEMS.append(mk(
    id="ibm-talanx-9m-2026-20261112",
    score=72, sourceTier="pro", sourceKey="insurancebusinessmag", verifyStatus="verified",
    t_sc="Talanx 九个月净利 21.95 亿欧元升 12%　汉诺威再保寿险健康业务靠亚洲长寿需求增 8%",
    t_tc="Talanx 九個月淨利 21.95 億歐元升 12%　漢諾威再保壽險健康業務靠亞洲長壽需求增 8%",
    s_sc="Talanx 公布第三季业绩：九个月集团净利 21.95 亿欧元、同比升 12%，大额赔款较预算低约 7.5 亿欧元，综合成本率由 89.8% 改善至 89.0%，净保险财务与投资收益升 52% 至 15 亿欧元。旗下汉诺威再保的人寿与健康再保业务受亚洲长寿与财务解决方案需求带动增长 8%。全年净利指引逾 28 亿欧元，并首次设定 2027 年逾 30 亿欧元目标；Solvency II 比率 241%。",
    s_tc="Talanx 公布第三季業績：九個月集團淨利 21.95 億歐元、同比升 12%，大額賠款較預算低約 7.5 億歐元，綜合成本率由 89.8% 改善至 89.0%，淨保險財務與投資收益升 52% 至 15 億歐元。旗下漢諾威再保的人壽與健康再保業務受亞洲長壽與財務解決方案需求帶動增長 8%。全年淨利指引逾 28 億歐元，並首次設定 2027 年逾 30 億歐元目標；Solvency II 比率 241%。",
    w_sc="读再保财报要看两件事：赔款低于预算带来的「一次性好看」，与投资收益里可重复的部分。Talanx 自己承认已实现收益不可重复——这种区分能力，用来看港险分红演示同样管用。",
    w_tc="讀再保財報要看兩件事：賠款低於預算帶來的「一次性好看」，與投資收益裡可重複的部分。Talanx 自己承認已實現收益不可重複——這種區分能力，用來看港險分紅演示同樣管用。",
    a_front=("向客户解释「已实现收益不可重复」如何影响分红非保证部分", "向客戶解釋「已實現收益不可重複」如何影響分紅非保證部分"),
    a_mid=("再保承保周期与费率走软对产品定价的传导，可作培训", "再保承保週期與費率走軟對產品定價的傳導，可作培訓"),
    a_lead=("亚洲长寿与财务解决方案需求，是再保端确认的长期主题", "亞洲長壽與財務解決方案需求，是再保端確認的長期主題"),
    a_cross=None,
    r=(1, 2, 3, 0),
    src="Insurance Business Asia", lang="zh+en",
    boards=["market"], themes=["reinsurance", "results", "longevity"],
    tags_sc=["再保险", "业绩", "长寿风险", "综合成本率", "偿付能力"],
    tags_tc=["再保險", "業績", "長壽風險", "綜合成本率", "償付能力"],
    kind="results", pub="2026-11-12",
    url="https://www.insurancebusinessmag.com/asia/news/breaking-news/talanx-posts-record-nine-months-as-losses-run-750m-below-budget-597126.aspx",
))

# 7. Allianz Q3
ITEMS.append(mk(
    id="ibm-allianz-q3-cat-20261112",
    score=72, sourceTier="pro", sourceKey="insurancebusinessmag", verifyStatus="verified",
    t_sc="安联第三季产险综合成本率升至 93.8%　巨灾损失占损失率由 0.3 个百分点跳到 5.1",
    t_tc="安聯第三季產險綜合成本率升至 93.8%　巨災損失佔損失率由 0.3 個百分點跳到 5.1",
    s_sc="安联第三季业绩：九个月营业利润 141 亿欧元创纪录、升 7.8%，但产险第三季明显转差——自然巨灾成本占损失率由去年同期 0.3 个百分点升至 5.1 个百分点，综合成本率由 91.9% 恶化至 93.8%，产险营业利润跌 7.9% 至 22 亿欧元；资产管理（PIMCO 等）季度营业利润升 35.1% 至 11 亿欧元支撑集团数字。全年营业利润目标上限上调至约 186 亿欧元，Solvency II 比率 219%。",
    s_tc="安聯第三季業績：九個月營業利潤 141 億歐元創紀錄、升 7.8%，但產險第三季明顯轉差——自然巨災成本佔損失率由去年同期 0.3 個百分點升至 5.1 個百分點，綜合成本率由 91.9% 惡化至 93.8%，產險營業利潤跌 7.9% 至 22 億歐元；資產管理（PIMCO 等）季度營業利潤升 35.1% 至 11 億歐元支撐集團數字。全年營業利潤目標上限上調至約 186 億歐元，Solvency II 比率 219%。",
    w_sc="巨灾在亚洲不是抽象风险：安联 Risk Barometer 2026 里自然灾害在亚太排第五、网络风险排第一。产险承保转紧最终会落到商业险条款与费率上，做企业客户与高客保障的团队要提前知情。",
    w_tc="巨災在亞洲不是抽象風險：安聯 Risk Barometer 2026 裡自然災害在亞太排第五、網絡風險排第一。產險承保轉緊最終會落到商業險條款與費率上，做企業客戶與高客保障的團隊要提前知情。",
    a_front=("企业客户续保前预判条款收紧，提早做风险查勘", "企業客戶續保前預判條款收緊，提早做風險查勘"),
    a_mid=("综合成本率与巨灾口径，可作产品培训基础概念", "綜合成本率與巨災口徑，可作產品培訓基礎概念"),
    a_lead=("关注亚太网络险与自然灾害的承保取向变化", "關注亞太網絡險與自然災害的承保取向變化"),
    a_cross=("跨境资产的自然巨灾累积，是家办投资尽调项", "跨境資產的自然巨災累積，是家辦投資盡調項"),
    r=(1, 2, 2, 1),
    src="Insurance Business Asia", lang="zh+en",
    boards=["market"], themes=["cat-loss", "p&c", "combined-ratio"],
    tags_sc=["安联", "巨灾损失", "综合成本率", "产险", "资产管理"],
    tags_tc=["安聯", "巨災損失", "綜合成本率", "產險", "資產管理"],
    kind="results", pub="2026-11-12",
    url="https://www.insurancebusinessmag.com/asia/news/breaking-news/cat-losses-push-allianz-pandc-to-worst-quarterly-result-in-two-years-597114.aspx",
))

# 8. APRA 数据中心
ITEMS.append(mk(
    id="ian-apra-datacentre-capacity-20261112",
    score=70, sourceTier="pro", sourceKey="insuranceasianews", verifyStatus="pending",
    t_sc="APRA 警示：数据中心规模正压测保险容量　前沿 AI 模型缩短漏洞修复窗口",
    t_tc="APRA 警示：數據中心規模正壓測保險容量　前沿 AI 模型縮短漏洞修復窗口",
    s_sc="澳洲审慎监管局（APRA）指出，超大规模、高价值集中的数据中心项目正考验产险与再保的承保假设；同时前沿 AI 模型令机构发现并修补漏洞的时间窗不断缩短。监管机构认为，网络风险的定价、累积风险计量与再保安排都需重估，机构应对集中度与情景压力测试提出更高要求。",
    s_tc="澳洲審慎監管局（APRA）指出，超大規模、高價值集中的數據中心項目正考驗產險與再保的承保假設；同時前沿 AI 模型令機構發現並修補漏洞的時間窗不斷縮短。監管機構認為，網絡風險的定價、累積風險計量與再保安排都需重估，機構應對集中度與情景壓力測試提出更高要求。",
    w_sc="AI 与数据中心正在制造「单一标的、巨额累积」的新型巨灾式风险——这跟香港推 AI 基建、北部都会区数据园区是同一件事的两面：保障能力跟不上，项目融资成本就会上去。",
    w_tc="AI 與數據中心正在製造「單一標的、巨額累積」的新型巨災式風險——這跟香港推 AI 基建、北部都會區數據園區是同一件事的兩面：保障能力跟不上，項目融資成本就會上去。",
    a_front=("企业客户谈数据中心或科技风险时，先问累积与集中度", "企業客戶談數據中心或科技風險時，先問累積與集中度"),
    a_mid=("AI 网络威胁的承保口径变化，纳入风险清单", "AI 網絡威脅的承保口徑變化，納入風險清單"),
    a_lead=("关注本地数据园区与 AI 基建的保险容量议题", "關注本地數據園區與 AI 基建的保險容量議題"),
    a_cross=("跨境数据中心资产的再保安排，是另类投资尽调项", "跨境數據中心資產的再保安排，是另類投資盡調項"),
    r=(1, 2, 2, 2),
    src="InsuranceAsia News", lang="zh+en",
    boards=["tech", "market"], themes=["cyber", "data-centre", "ai-risk"],
    tags_sc=["网络风险", "数据中心", "AI风险", "承保容量", "APRA"],
    tags_tc=["網絡風險", "數據中心", "AI風險", "承保容量", "APRA"],
    kind="news", pub="2026-11-12",
    url="https://insuranceasianews.com/data-centre-scale-strains-insurance-capacity-as-ai-cyber-threats-accelerate-apra-warns/",
))


def main():
    data = json.load(open(LIVE, encoding="utf-8"))
    items = data["items"]
    existing_ids = {i["id"] for i in items}
    existing_urls = {i.get("originalUrl") for i in items}

    added, skipped = [], []
    for it in ITEMS:
        if it["id"] in existing_ids:
            skipped.append((it["id"], "id dup"))
            continue
        if it["originalUrl"] in existing_urls:
            skipped.append((it["id"], "url dup"))
            continue
        added.append(it)

    if not added:
        print("no new items")
        return

    data["items"] = added + items
    n = len(data["items"])
    data["meta"]["itemCount"] = n
    data["meta"]["generatedAt"] = NOW
    data["meta"]["windowNote"] = {"sc": f"本库{n}条。", "tc": f"本庫{n}條。"}

    json.dump(data, open(LIVE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"inserted {len(added)} items -> total {n}")
    for it in added:
        print("  +", it["publishedAt"], it["sourceKey"], it["title"]["sc"][:60])
    for s in skipped:
        print("  skip", s)


if __name__ == "__main__":
    main()
