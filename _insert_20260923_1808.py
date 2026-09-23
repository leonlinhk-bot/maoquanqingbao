#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-23 18:08 增量采集插入"""
import json, shutil, datetime, os

ROOT = os.path.dirname(os.path.abspath(__file__))
NOW = "2026-09-23T18:08:00+08:00"

def item(**kw):
    it = {
        "clusterCount": 1,
        "score": 70,
        "verifyStatus": "pending",
        "sourceTier": "pro",
        "contentKind": "news",
        "source": {"sc": "", "lang": "en"},
        "boards": [],
        "themes": [],
        "tags": {"sc": [], "tc": []},
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False,
        "ingestedAt": NOW,
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 0, "midback": 0, "lead": 0, "cross": 0},
    }
    it.update(kw)
    return it

NEW = []

# 1. HKMA 债市峰会（官方）
NEW.append(item(
    id="hkma-treasury-markets-summit-20260923",
    score=85, verifyStatus="verified", sourceTier="official", sourceKey="hkma",
    contentKind="press",
    title={"sc": "金管局与财资市场公会举办「2026 财资市场峰会」：推动债券市场深度、离岸人民币流动性与数字化基建",
           "tc": "金管局與財資市場公會舉辦「2026 財資市場峰會」：推動債券市場深度、離岸人民幣流動性與數字化基建"},
    summary={"sc": "金管局与财资市场公会 9 月 23 日在香港合办财资市场峰会，总裁余伟文致辞提出鼓励市场参与与发债、深化离岸人民币流动性、以现代化基建支持数字化与跨境固定收益活动，呼吁业界共建多元、有深度、动态且「数字原生」的债券市场。三个专题讨论涵盖人民币国际化、债市宏观展望与科技改造财资运营，逾 300 名从业者出席。",
             "tc": "金管局與財資市場公會 9 月 23 日在香港合辦財資市場峰會，總裁余偉文致辭提出鼓勵市場參與與發債、深化離岸人民幣流動性、以現代化基建支持數字化與跨境固定收益活動，呼籲業界共建多元、有深度、動態且「數字原生」的債券市場。三個專題討論涵蓋人民幣國際化、債市宏觀展望與科技改造財資運營，逾 300 名從業者出席。"},
    why={"sc": "保险公司是香港债券市场最大的机构投资者之一，负债久期长、对离岸人民币与跨境固定收益工具高度敏感。金管局对债市深度与基建的表态，直接影响长期保单资产端的可投品种与匹配效率；对做高净值客户的团队而言，也是理解「分红实现率背后资产端」的公开材料。",
         "tc": "保險公司是香港債券市場最大的機構投資者之一，負債久期長、對離岸人民幣與跨境固定收益工具高度敏感。金管局對債市深度與基建的表態，直接影響長期保單資產端的可投品種與匹配效率；對做高淨值客戶的團隊而言，也是理解「分紅實現率背後資產端」的公開材料。"},
    actions={"front": {},
             "midback": {"sc": "了解公司固定收益配置中离岸人民币与跨境内地债券工具的占比与久期", "tc": "了解公司固定收益配置中離岸人民幣與跨境內地債券工具的佔比與久期"},
             "lead": {"sc": "把「资产端债券市场深化」纳入分红与长期收益沟通框架，避免只谈产品不谈底层", "tc": "把「資產端債券市場深化」納入分紅與長期收益溝通框架，避免只談產品不談底層"},
             "cross": {"sc": "关注跨境固定收益与人民币资产安排对高客多币种配置的影响", "tc": "關注跨境固定收益與人民幣資產安排對高客多幣種配置的影響"}},
    rolesImpact={"front": 0, "midback": 1, "lead": 2, "cross": 1},
    source={"sc": "香港金融管理局新闻稿（2026-09-23）[EN原文]", "lang": "en"},
    boards=["market"], themes=["bond-market", "hong-kong"],
    tags={"sc": ["金管局", "财资市场峰会", "债券市场", "离岸人民币", "余伟文"],
          "tc": ["金管局", "財資市場峰會", "債券市場", "離岸人民幣", "余偉文"]},
    publishedAt="2026-09-23T17:00:00+08:00",
    originalUrl="https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/09/20260923-4/",
))

# 2. S&P：AI 成为信用评级因素
NEW.append(item(
    id="ian-sp-ai-credit-factors-20260923",
    score=70, sourceKey="insuranceasianews",
    title={"sc": "S&P：AI 的效益与风险将成(再)保险信用评级的实质考量（121家机构调研）[EN原文]",
           "tc": "S&P：AI 的效益與風險將成(再)保險信用評級的實質考量（121家機構調研）[EN原文]"},
    summary={"sc": "标普全球评级对 121 家全球(再)保险机构调研后指出，AI 带来的效益与风险预计将日益成为保险业信用评估的考量因素。对能有效落地 AI 的机构，效率与定价能力构成正面因素；而模型风险、数据治理、第三方依赖与资本占用则可能形成评级压力。",
             "tc": "標普全球評級對 121 家全球(再)保險機構調研後指出，AI 帶來的效益與風險預計將日益成為保險業信用評估的考量因素。對能有效落地 AI 的機構，效率與定價能力構成正面因素；而模型風險、數據治理、第三方依賴與資本佔用則可能形成評級壓力。"},
    why={"sc": "香港保监局正推 GenA.I. Sandbox++、保险公司把 AI 推进到承保与销售前端，业界讨论多集中在效率。标普的视角提供了另一条线：AI 不只是生产力工具，也会进入评级与资本视角，这会影响公司的融资成本与资本策略，进而传导到产品定价与分红能力。",
         "tc": "香港保監局正推 GenA.I. Sandbox++、保險公司把 AI 推進到承保與銷售前端，業界討論多集中在效率。標普的視角提供了另一條線：AI 不只是生產力工具，也會進入評級與資本視角，這會影響公司的融資成本與資本策略，進而傳導到產品定價與分紅能力。"},
    actions={"front": {},
             "midback": {"sc": "关注核保/核赔 AI 工具的准确率与人工复核机制，避免以 AI 输出直接替代核保结论", "tc": "關注核保/核賠 AI 工具的準確率與人工覆核機制，避免以 AI 輸出直接替代核保結論"},
             "lead": {"sc": "把 AI 治理（数据、模型、第三方依赖）纳入部门风险管理与合规汇报口径", "tc": "把 AI 治理（數據、模型、第三方依賴）納入部門風險管理與合規匯報口徑"},
             "cross": {"sc": "关注母公司层面 AI 评级叙事对资本与再保谈判的间接影响", "tc": "關注母公司層面 AI 評級敘事對資本與再保談判的間接影響"}},
    rolesImpact={"front": 0, "midback": 1, "lead": 2, "cross": 1},
    source={"sc": "InsuranceAsia News（2026-09-23，S&P Global Ratings 调研）[EN原文]", "lang": "en"},
    boards=["tech"], themes=["ai", "rating"],
    tags={"sc": ["AI治理", "信用评级", "S&P", "资本", "模型风险"],
          "tc": ["AI治理", "信用評級", "S&P", "資本", "模型風險"]},
    publishedAt="2026-09-23T16:07:00+08:00",
    originalUrl="https://insuranceasianews.com/ai-benefits-risks-to-become-relevant-credit-factors-for-reinsurers-sp-ratings/",
))

# 3. 荷莫兹海峡：海险「可计算风险」
NEW.append(item(
    id="ian-hormuz-marine-calculated-risk-20260923",
    score=70, sourceKey="insuranceasianews",
    title={"sc": "荷莫兹海峡冲突下，海险承保人被吁视为「可计算风险」而非不可保，继续承保 [EN原文]",
           "tc": "荷莫茲海峽衝突下，海險承保人被籲視為「可計算風險」而非不可保，繼續承保 [EN原文]"},
    summary={"sc": "面对荷莫兹海峡冲突持续，海险业界被提醒应把该区域风险视为「可计算的承保变量」而非整体不可保，继续为往来船舶提供保障，避免承保能力集体退场。此前 IUMI 会议披露，海湾冲突引发的海上战争险索赔已达 15 至 20 亿美元、涉约 70 艘船舶。",
             "tc": "面對荷莫茲海峽衝突持續，海險業界被提醒應把該區域風險視為「可計算的承保變量」而非整體不可保，繼續為往來船舶提供保障，避免承保能力集體退場。此前 IUMI 會議披露，海灣衝突引發的海上戰爭險索賠已達 15 至 20 億美元、涉約 70 艘船舶。"},
    why={"sc": "香港正以「航运专项风险池」为抓手巩固国际风险管理中心地位，战争险与海上风险的定价与承接能力直接决定该池的可持续性。对做航运、贸易与跨境企业风险的专业团队，这是判断承保条件与除外责任走向的一手信号。",
         "tc": "香港正以「航運專項風險池」為抓手鞏固國際風險管理中心地位，戰爭險與海上風險的定價與承接能力直接決定該池的可持續性。對做航運、貿易與跨境企業風險的專業團隊，這是判斷承保條件與除外責任走向的一手信號。"},
    actions={"front": {},
             "midback": {"sc": "复核涉中东航线客户的战争险与除外条款，提前沟通可能的费率与条件调整", "tc": "覆核涉中東航線客戶的戰爭險與除外條款，提前溝通可能的費率與條件調整"},
             "lead": {"sc": "跟踪主要再保人对海湾水域的累积敞口态度与分出条件变化", "tc": "跟蹤主要再保人對海灣水域的累積敞口態度與分出條件變化"},
             "cross": {"sc": "关注香港航运专项风险池承接能力与内地航运央企出海需求的对接机会", "tc": "關注香港航運專項風險池承接能力與內地航運央企出海需求的對接機會"}},
    rolesImpact={"front": 0, "midback": 1, "lead": 2, "cross": 1},
    source={"sc": "InsuranceAsia News（2026-09-23）[EN原文]", "lang": "en"},
    boards=["market"], themes=["marine", "war-risk"],
    tags={"sc": ["海上战争险", "荷莫兹海峡", "航运风险", "再保险", "IUMI"],
          "tc": ["海上戰爭險", "荷莫茲海峽", "航運風險", "再保險", "IUMI"]},
    publishedAt="2026-09-23T07:30:00+08:00",
    originalUrl="https://insuranceasianews.com/calculated-risk-not-uninsurable-marine-insurers-urged-to-stay-the-course-amid-strait-of-hormuz-conflict/",
))

# 4. Sompo 委任
NEW.append(item(
    id="ian-sompo-joe-wee-apac-construction-20260923",
    score=70, sourceKey="insuranceasianews",
    title={"sc": "损保（Sompo）委任 Joe Wee 为亚太区建筑工程承保主管 [EN原文]",
           "tc": "損保（Sompo）委任 Joe Wee 為亞太區建築工程承保主管 [EN原文]"},
    summary={"sc": "Sompo 任命驻新加坡的 Joe Wee 出任亚太区建筑工程承保主管，其在工程与建筑（engineering & construction）险种有超过 26 年经验。该任命发生在亚太基建、数据中心与新能源项目密集上马、工程险专业承保能力紧张之际。",
             "tc": "Sompo 任命駐新加坡的 Joe Wee 出任亞太區建築工程承保主管，其在工程與建築（engineering & construction）險種有超過 26 年經驗。該任命發生在亞太基建、數據中心與新能源項目密集上馬、工程險專業承保能力緊張之際。"},
    why={"sc": "数据中心、电力与基建项目是当前亚太工程险增长最快的标的，也是香港「专项保险」政策方向的重点。承保主管层面的调动，往往预示着某些险种能力与议价力的重新分配，对做大型项目与团体业务的专业团队有风向意义。",
         "tc": "數據中心、電力與基建項目是當前亞太工程險增長最快的標的，也是香港「專項保險」政策方向的重點。承保主管層面的調動，往往預示著某些險種能力與議價力的重新分配，對做大型項目與團體業務的專業團隊有風向意義。"},
    actions={"front": {},
             "midback": {"sc": "梳理手上在建项目清单，关注工程险续保时点与承保能力变化", "tc": "梳理手上在建項目清單，關注工程險續保時點與承保能力變化"},
             "lead": {"sc": "与主要工程险承保方确认数据中心类项目的承保口径与免赔条件", "tc": "與主要工程險承保方確認數據中心類項目的承保口徑與免賠條件"},
             "cross": {"sc": "关注工程险专才流动对香港专项保险人才策略的启示", "tc": "關注工程險專才流動對香港專項保險人才策略的啟示"}},
    rolesImpact={"front": 0, "midback": 1, "lead": 2, "cross": 1},
    source={"sc": "InsuranceAsia News（2026-09-23）[EN原文]", "lang": "en"},
    boards=["insurer"], themes=["talent", "construction"],
    tags={"sc": ["Sompo", "工程险", "数据中心", "亚太承保", "人事"],
          "tc": ["Sompo", "工程險", "數據中心", "亞太承保", "人事"]},
    publishedAt="2026-09-23T15:50:00+08:00",
    originalUrl="https://insuranceasianews.com/sompo-names-joe-wee-as-apac-construction-underwriting-head/",
))

# 5. Lockton 分析主管
NEW.append(item(
    id="ian-lockton-arthur-wong-analytics-20260923",
    score=70, sourceKey="insuranceasianews",
    title={"sc": "Lockton 委任 Arthur Wong 为太平洋区分析（Analytics）主管 [EN原文]",
           "tc": "Lockton 委任 Arthur Wong 為太平洋區分析（Analytics）主管 [EN原文]"},
    summary={"sc": "保险经纪 Lockton 任命 Arthur Wong 为太平洋区分析主管，反映经纪商正把精算与数据分析能力前置到客户风险咨询、自留与自保方案设计中。Lockton 近月已连续在亚洲增聘信用险区域总监与香港人身保险方案负责人。",
             "tc": "保險經紀 Lockton 任命 Arthur Wong 為太平洋區分析主管，反映經紀商正把精算與數據分析能力前置到客戶風險諮詢、自留與自保方案設計中。Lockton 近月已連續在亞洲增聘信用險區域總監與香港人身保險方案負責人。"},
    why={"sc": "香港政策方向是「专属自保 + ILS + 专项保险」，而自保与替代风险转移方案的核心能力恰恰是数据建模与损失分析。经纪商把 analytics 升格为区域职能，说明客户侧对量化风险咨询的需求已从大企业扩展到中型客户，专业中介的差异化正在往数据能力上走。",
         "tc": "香港政策方向是「專屬自保 + ILS + 專項保險」，而自保與替代風險轉移方案的核心能力恰恰是數據建模與損失分析。經紀商把 analytics 升格為區域職能，說明客戶側對量化風險諮詢的需求已從大企業擴展到中型客戶，專業中介的差異化正在往數據能力上走。"},
    actions={"front": {},
             "midback": {"sc": "识别有自留/自保意向的客户，为量化风险分析预留资料口径", "tc": "識別有自留/自保意向的客戶，為量化風險分析預留資料口徑"},
             "lead": {"sc": "评估把数据分析能力纳入客户风险检视流程的可行性", "tc": "評估把數據分析能力納入客戶風險檢視流程的可行性"},
             "cross": {"sc": "关注数字财险、自保与 ILS 经纪服务能力在香港的供给变化", "tc": "關注數字財險、自保與 ILS 經紀服務能力在香港的供給變化"}},
    rolesImpact={"front": 0, "midback": 1, "lead": 2, "cross": 1},
    source={"sc": "InsuranceAsia News（2026-09-23）[EN原文]", "lang": "en"},
    boards=["insurer", "tech"], themes=["broker", "data-analytics"],
    tags={"sc": ["Lockton", "经纪", "数据分析", "自保", "人事"],
          "tc": ["Lockton", "經紀", "數據分析", "自保", "人事"]},
    publishedAt="2026-09-23T12:05:00+08:00",
    originalUrl="https://insuranceasianews.com/lockton-appoints-arthur-wong-as-pacific-head-of-analytics/",
))

# 6. 印度放宽外资经纪分红规则
NEW.append(item(
    id="ian-india-broker-dividend-rules-20260923",
    score=70, sourceKey="insuranceasianews",
    title={"sc": "印度监管放宽外资持股保险经纪公司的分红派发规则 [EN原文]",
           "tc": "印度監管放寬外資持股保險經紀公司的分紅派發規則 [EN原文]"},
    summary={"sc": "印度监管机构放宽对外资持股保险经纪公司的分红派发限制，为外资股东回收资本提供更清晰的路径。此举被视为印度改善外资营商环境的一部分，对以亚洲为主战场、通过合资或收购布局分销渠道的国际经纪与保险集团，资本回报可预期性提升。",
             "tc": "印度監管機構放寬對外資持股保險經紀公司的分紅派發限制，為外資股東回收資本提供更清晰的路徑。此舉被視為印度改善外資營商環境的一部分，對以亞洲為主戰場、通過合資或收購布局分銷渠道的國際經紀與保險集團，資本回報可預期性提升。"},
    why={"sc": "香港与新加坡、印度正在争夺亚洲保险分销与专业服务的区域枢纽位置。印度放宽外资经纪资本回收，会改变跨国集团在亚洲的资源配置顺序——这是判断区域竞争格局的合作/竞争态势时，值得放在同一张图上看的一条。",
         "tc": "香港與新加坡、印度正在爭奪亞洲保險分銷與專業服務的區域樞紐位置。印度放寬外資經紀資本回收，會改變跨國集團在亞洲的資源配置順序——這是判斷區域競爭格局的合作/競爭態勢時，值得放在同一張圖上看的一條。"},
    actions={"front": {},
             "midback": {"sc": "了解合作经纪/分销伙伴的集团资本策略是否有区域重心转移", "tc": "了解合作經紀/分銷伙伴的集團資本策略是否有區域重心轉移"},
             "lead": {"sc": "关注区域监管开放节奏对代理与经纪渠道结构的长期影响", "tc": "關注區域監管開放節奏對代理與經紀渠道結構的長期影響"},
             "cross": {"sc": "把印度、新加坡、香港的外资政策节奏纳入区域竞争评估", "tc": "把印度、新加坡、香港的外資政策節奏納入區域競爭評估"}},
    rolesImpact={"front": 0, "midback": 1, "lead": 2, "cross": 2},
    source={"sc": "InsuranceAsia News（2026-09-23）[EN原文]", "lang": "en"},
    boards=["reg"], themes=["regulation", "broker"],
    tags={"sc": ["印度", "保险经纪", "外资", "分红派发", "区域竞争"],
          "tc": ["印度", "保險經紀", "外資", "分紅派發", "區域競爭"]},
    publishedAt="2026-09-23T12:13:00+08:00",
    originalUrl="https://insuranceasianews.com/indian-regulator-eases-dividend-distribution-rules-for-foreign-owned-brokers/",
))

# 7. IAG / ACCC
NEW.append(item(
    id="ian-iag-rac-accc-20260923",
    score=70, sourceKey="insuranceasianews",
    title={"sc": "澳洲 ACCC 叫停 IAG 收购 RAC Insurance，IAG 转向「公共利益」审批路径 [EN原文]",
           "tc": "澳洲 ACCC 叫停 IAG 收購 RAC Insurance，IAG 轉向「公共利益」審批路徑 [EN原文]"},
    summary={"sc": "澳洲竞争与消费者委员会（ACCC）否决 IAG 收购 RAC Insurance 的交易，认为会实质削弱西澳车险与家财险市场的竞争。IAG 表示将改走「公共利益」（public benefits）审批路径，主张交易对会员、客户与社区具长期利益。",
             "tc": "澳洲競爭與消費者委員會（ACCC）否決 IAG 收購 RAC Insurance 的交易，認為會實質削弱西澳車險與家財險市場的競爭。IAG 表示將改走「公共利益」（public benefits）審批路徑，主張交易對會員、客戶與社區具長期利益。"},
    why={"sc": "财险整合是本轮亚太保险资本周期的主线之一，监管对「市场集中度 vs 公共利益」的取舍尺度，直接决定后续同类交易能否落地。对香港而言，本地车险与家财险市场同样高度集中，澳洲的审查逻辑有参照价值。",
         "tc": "財險整合是本輪亞太保險資本週期的主線之一，監管對「市場集中度 vs 公共利益」的取捨尺度，直接決定後續同類交易能否落地。對香港而言，本地車險與家財險市場同樣高度集中，澳洲的審查邏輯有參照價值。"},
    actions={"front": {},
             "midback": {"sc": "关注整合交易后承保口径与代理条件的实际变化", "tc": "關注整合交易後承保口徑與代理條件的實際變化"},
             "lead": {"sc": "把区域并购案的市场集中度审查结果纳入渠道与竞争态势跟踪", "tc": "把區域併購案的市場集中度審查結果納入渠道與競爭態勢跟蹤"},
             "cross": {"sc": "关注跨境保险并购在主要市场的审批门槛变化", "tc": "關注跨境保險併購在主要市場的審批門檻變化"}},
    rolesImpact={"front": 0, "midback": 1, "lead": 2, "cross": 1},
    source={"sc": "InsuranceAsia News（2026-09-23）[EN原文]", "lang": "en"},
    boards=["market"], themes=["ma", "regulation"],
    tags={"sc": ["IAG", "ACCC", "并购", "财险", "竞争审查"],
          "tc": ["IAG", "ACCC", "併購", "財險", "競爭審查"]},
    publishedAt="2026-09-23T09:54:00+08:00",
    originalUrl="https://insuranceasianews.com/iag-to-seek-public-benefits-approval-after-accc-halts-rac-insurance-acquisition/",
))

# 8. 汉诺威再保增聘
NEW.append(item(
    id="ian-hannover-re-louise-austin-20260923",
    score=70, sourceKey="insuranceasianews",
    title={"sc": "Hannover Re 增聘 Louise Austin 任澳洲临分意外险高级承保人 [EN原文]",
           "tc": "Hannover Re 增聘 Louise Austin 任澳洲臨分意外險高級承保人 [EN原文]"},
    summary={"sc": "汉诺威再保险任命驻悉尼的 Louise Austin 出任澳洲临分意外险（facultative casualty）高级承保人，其此前任职于 Berkshire Hathaway Specialty Insurance。在意外险长尾风险定价争议加剧、社会通胀（social inflation）压力上升的背景下，再保方正加强临分承保人力。",
             "tc": "漢諾威再保險任命駐悉尼的 Louise Austin 出任澳洲臨分意外險（facultative casualty）高級承保人，其此前任職於 Berkshire Hathaway Specialty Insurance。在意外險長尾風險定價爭議加劇、社會通脹（social inflation）壓力上升的背景下，再保方正加強臨分承保人力。"},
    why={"sc": "意外险长尾风险的再保条件，最终会传导到直接保险的承保条件与费率。再保人加强临分团队，通常意味着对个案风险的审查将更细致，专业中介在为客户争取条款时需要更完整的风险资料准备。",
         "tc": "意外險長尾風險的再保條件，最終會傳導到直接保險的承保條件與費率。再保人加強臨分團隊，通常意味著對個案風險的審查將更細緻，專業中介在為客戶爭取條款時需要更完整的風險資料準備。"},
    actions={"front": {},
             "midback": {"sc": "留意意外险与责任险个案资料要求是否趋严（职业、活动、既往记录）", "tc": "留意意外險與責任險個案資料要求是否趨嚴（職業、活動、既往記錄）"},
             "lead": {"sc": "关注社会通胀叙事对长期责任险准备金与费率的影响", "tc": "關注社會通脹敘事對長期責任險準備金與費率的影響"},
             "cross": {"sc": "关注亚太临分承保人才流动反映的险种热度变化", "tc": "關注亞太臨分承保人才流動反映的險種熱度變化"}},
    rolesImpact={"front": 0, "midback": 1, "lead": 1, "cross": 1},
    source={"sc": "InsuranceAsia News（2026-09-23）[EN原文]", "lang": "en"},
    boards=["insurer"], themes=["talent", "reinsurance"],
    tags={"sc": ["Hannover Re", "临分", "意外险", "长尾风险", "人事"],
          "tc": ["Hannover Re", "臨分", "意外險", "長尾風險", "人事"]},
    publishedAt="2026-09-23T17:18:00+08:00",
    originalUrl="https://insuranceasianews.com/louise-austin-makes-bittersweet-move-to-hannover-re-as-senior-underwriter-for-australian-fac-cas/",
))

# 9. 家办增配中国
NEW.append(item(
    id="scmp-family-offices-china-investments-20260923",
    score=62, sourceTier="media", sourceKey="scmp",
    title={"sc": "报告：欧洲、中东及非洲家办在地缘缓和下增配中国资产，组合分散成主因",
           "tc": "報告：歐洲、中東及非洲家辦在地緣緩和下增配中國資產，組合分散成主因"},
    summary={"sc": "有报告指出，欧洲、中东及非洲（EMEA）的家族办公室正提高对中国投资的配置，作为全球组合分散的一部分；在中美紧张情绪阶段性缓和的背景下，家办对中国的兴趣有所回升。相关配置仍属主动选股与另类资产层面的试探性增配，而非全面重仓。",
             "tc": "有報告指出，歐洲、中東及非洲（EMEA）的家族辦公室正提高對中國投資的配置，作為全球組合分散的一部分；在中美緊張情緒階段性緩和的背景下，家辦對中國的興趣有所回升。相關配置仍屬主動選股與另類資產層面的試探性增配，而非全面重倉。"},
    why={"sc": "香港正以家族办公室税制优惠争夺区域家办枢纽地位，EMEA 家办资金回流中国叙事，会直接体现在对香港平台、跨境架构与高客财富传承方案的需求上。这是判断高客客群结构变化（从纯内地客到多元区域客）的先行信号。",
         "tc": "香港正以家族辦公室稅制優惠爭奪區域家辦樞紐地位，EMEA 家辦資金回流中國敘事，會直接體現在對香港平台、跨境架構與高客財富傳承方案的需求上。這是判斷高客客群結構變化（從純內地客到多元區域客）的先行信號。"},
    actions={"front": {},
             "midback": {"sc": "了解所服务高客是否存在多司法辖区资产与架构需求", "tc": "了解所服務高客是否存在多司法轄區資產與架構需求"},
             "lead": {"sc": "把跨境架构与多币种传承方案纳入高客沟通框架", "tc": "把跨境架構與多幣種傳承方案納入高客溝通框架"},
             "cross": {"sc": "关注家办与家族治理服务在香港的供给与竞争变化", "tc": "關注家辦與家族治理服務在香港的供給與競爭變化"}},
    rolesImpact={"front": 0, "midback": 1, "lead": 2, "cross": 2},
    source={"sc": "South China Morning Post（2026-09-22 20:31）[EN原文]", "lang": "en"},
    boards=["family"], themes=["family-office", "cross-border"],
    tags={"sc": ["家族办公室", "中国资产", "资产配置", "高净值", "跨境"],
          "tc": ["家族辦公室", "中國資產", "資產配置", "高淨值", "跨境"]},
    publishedAt="2026-09-22T20:31:00+08:00",
    originalUrl="https://www.scmp.com/business/money/article/3368416/some-family-offices-eyeing-chinese-investments-us-china-tensions-ease-report",
))

# 10. 险资联手投不动产基金
NEW.append(item(
    id="sina-aia-zhonghong-hsbc-re-fund-20260923",
    score=62, sourceTier="media", sourceKey="sina",
    title={"sc": "友邦人寿、中宏人寿、汇丰人寿联手认缴 23.22 亿元，投资华平 25.8 亿元不动产基金",
           "tc": "友邦人壽、中宏人壽、匯豐人壽聯手認繳 23.22 億元，投資華平 25.8 億元不動產基金"},
    summary={"sc": "据中国证券投资基金业协会备案信息，友邦人寿、中宏人寿、汇丰人寿与华平投资相关方设立「嘉兴曜盈股权投资合伙企业」，基金总规模 25.8 亿元，三家寿险合计认缴 23.22 亿元（友邦 12.64 亿、中宏 8 亿、汇丰 2.58 亿），投向上海、东莞、苏州的仓储物流与保障性租赁住房。2026 年以来险资组团投不动产明显加速。",
             "tc": "據中國證券投資基金業協會備案信息，友邦人壽、中宏人壽、匯豐人壽與華平投資相關方設立「嘉興曜盈股權投資合伙企業」，基金總規模 25.8 億元，三家壽險合計認繳 23.22 億元（友邦 12.64 億、中宏 8 億、匯豐 2.58 億），投向上海、東莞、蘇州的倉儲物流與保障性租賃住房。2026 年以來險資組團投不動產明顯加速。"},
    why={"sc": "友邦、宏利、保诚等集团的中国业务与香港业务同属一个资本池，内地资产端配置动向会影响集团整体投资回报与资本效率。外资系寿险偏爱不动产基金（长租、物流地产）以匹配长久期负债，是一条理解「分红来源与久期匹配」的公开线索。",
         "tc": "友邦、宏利、保誠等集團的中國業務與香港業務同屬一個資本池，內地資產端配置動向會影響集團整體投資回報與資本效率。外資系壽險偏愛不動產基金（長租、物流地產）以匹配長久期負債，是一條理解「分紅來源與久期匹配」的公開線索。"},
    actions={"front": {},
             "midback": {"sc": "在客户沟通中避免把资产端收益叙事简化为「公司投资能力强」", "tc": "在客戶溝通中避免把資產端收益敘事簡化為「公司投資能力強」"},
             "lead": {"sc": "跟踪主要合作保司在内地的资产配置偏好与偿付能力表现", "tc": "跟蹤主要合作保司在內地的資產配置偏好與償付能力表現"},
             "cross": {"sc": "关注险资出海与香港投资平台在另类资产上的协同可能", "tc": "關注險資出海與香港投資平台在另類資產上的協同可能"}},
    rolesImpact={"front": 0, "midback": 1, "lead": 2, "cross": 1},
    source={"sc": "新浪财经（2026-09-23 12:42，引中基协备案信息）", "lang": "zh"},
    boards=["market"], themes=["insurance-fund", "real-estate"],
    tags={"sc": ["险资", "不动产基金", "友邦", "中宏", "汇丰人寿", "资产配置"],
          "tc": ["險資", "不動產基金", "友邦", "中宏", "匯豐人壽", "資產配置"]},
    publishedAt="2026-09-23T12:42:00+08:00",
    originalUrl="https://finance.sina.com.cn/roll/2026-09-23/doc-inisusyf8609866.shtml",
))

# ---------- 写入 ----------
path = os.path.join(ROOT, "data", "live-items.json")
shutil.copy(path, os.path.join(ROOT, "data", "live-items.json.bak-0923-1808"))
data = json.load(open(path))
existing = {it.get("id") for it in data["items"]}
new = [it for it in NEW if it["id"] not in existing]
skipped = [it["id"] for it in NEW if it["id"] in existing]
new.sort(key=lambda x: x["publishedAt"], reverse=True)
data["items"] = new + data["items"]

n = len(data["items"])
data["meta"]["generatedAt"] = NOW
data["meta"]["itemCount"] = n
data["meta"]["windowNote"] = {"sc": f"本库{n}条。", "tc": f"本庫{n}條。"}
if "asOf" in data["meta"]:
    data["meta"]["asOf"] = NOW
json.dump(data, open(path, "w"), ensure_ascii=False, indent=2)
print("inserted:", len(new), "skipped:", skipped, "total:", n)
for it in new:
    print(" -", it["publishedAt"], it["id"])
