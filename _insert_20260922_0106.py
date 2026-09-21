# -*- coding: utf-8 -*-
"""猫圈儿港险情报站 2026-09-22 01:0x 增量采集插入脚本（窗口：09-21 21:15 → 09-22 01:05）"""
import json, datetime, os

BASE = os.path.dirname(os.path.abspath(__file__))
LIVE = os.path.join(BASE, 'data', 'live-items.json')
CHECK = os.path.join(BASE, 'data', 'last-check.json')

NOW = "2026-09-22T01:06:00+08:00"

def it(**kw):
    d = {
        "clusterCount": 1, "score": 60, "verifyStatus": "verified",
        "sourceTier": "media", "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False, "evergreen": False,
        "actions": {"front": {}, "midback": {}, "lead": {}, "cross": {}},
        "rolesImpact": {"front": 0, "midback": 0, "lead": 0, "cross": 0},
        "source": {"sc": "", "lang": "en"}, "contentKind": "news",
    }
    d.update(kw)
    return d

new_items = []

# ── 1. 日本台风「杜鹃」／软市场再保结构检验 ─────────────────────────────
new_items.append(it(
    id="ibm-japan-typhoon-dujuan-soft-market-test-20260922",
    score=65, sourceTier="media", sourceKey="insurancebusinessmag",
    title={"sc": "台风「杜鹃」登陆日本：软市场下搭建的再保结构面临检验，4月续保曾降价最多20% [EN原文]",
           "tc": "颱風「杜鵑」登陸日本：軟市場下搭建的再保結構面臨檢驗，4月續保曾降價最多20% [EN原文]"},
    summary={"sc": "台风「杜鹃」9月21日以持续风速130公里、阵风194公里登陆日本太平洋沿岸，近200万人接获疏散指示、逾5万户停电，数百航班取消。日本4月1日续保时巨灾超赔按风险调整后降价最多20%（点估计16%），业界关注降价期搭建的保障结构是否足够；完整损失评估料9月23日后方有，巨灾模型暂未发布承保损失估算。",
             "tc": "颱風「杜鵑」9月21日以持續風速130公里、陣風194公里登陸日本太平洋沿岸，近200萬人接獲疏散指示、逾5萬戶停電，數百航班取消。日本4月1日續保時巨災超賠按風險調整後降價最多20%（點估計16%），業界關注降價期搭建的保障結構是否足夠；完整損失評估料9月23日後方有，巨災模型暫未發布承保損失估算。"},
    why={"sc": "「4月续保最多降价两成」是软市场的典型读数，而一次大型台风就足以把降价换来的节省重新交回。这类周期信息用于理解再保资本与定价节奏；同时提醒客户：再保价格战不等于自己的保障条款变宽。",
         "tc": "「4月續保最多降價兩成」是軟市場的典型讀數，而一次大型颱風就足以把降價換來的節省重新交回。這類週期信息用於理解再保資本與定價節奏；同時提醒客戶：再保價格戰不等於自己的保障條款變寬。"},
    actions={"front": {"sc": "与客户谈旅游／家居／商业财产时，可说明再保定价与个人保单条款是两件事", "tc": "與客戶談旅遊／家居／商業財產時，可說明再保定價與個人保單條款是兩件事"},
             "midback": {"sc": "留意后续巨灾损失估算对2027年续保报价的传导", "tc": "留意後續巨災損失估算對2027年續保報價的傳導"},
             "lead": {"sc": "关注日本巨灾超赔损失对区域再保容量与定价的影响", "tc": "關注日本巨災超賠損失對區域再保容量與定價的影響"},
             "cross": {}},
    rolesImpact={"front": 1, "midback": 2, "lead": 2, "cross": 0},
    source={"sc": "Insurance Business Asia（2026-09-22）", "lang": "en"},
    boards=["market"], themes=["catastrophe", "reinsurance", "pricing"],
    tags={"sc": ["台风杜鹃", "日本再保", "巨灾超赔", "续保定价", "软市场"],
          "tc": ["颱風杜鵑", "日本再保", "巨災超賠", "續保定價", "軟市場"]},
    publishedAt="2026-09-22",
    originalUrl="https://www.insurancebusinessmag.com/asia/news/catastrophe/japans-soft-reinsurance-market-faces-a-new-catastrophe-test-590527.aspx",
))

# ── 2. 富卫 FWD Care 扩展：宁养认知落差 ─────────────────────────────────
new_items.append(it(
    id="iaasia-fwd-care-palliative-awareness-hk-20260922",
    clusterCount=2, score=68, sourceTier="media", sourceKey="insuranceasia",
    title={"sc": "富卫香港扩展 FWD Care 服务：新增长者认知筛查与宁养转介；调查指69%受访者不了解宁养服务、本港认知障碍症患者2045年料达55万 [EN原文]",
           "tc": "富衛香港擴展 FWD Care 服務：新增長者認知篩查與寧養轉介；調查指69%受訪者不了解寧養服務、本港認知障礙症患者2045年料達55萬 [EN原文]"},
    summary={"sc": "富卫香港与养和医疗集团及灵实司务道宁养院合作升级 FWD Care：合资格健康险客户可获免费阿兹海默症早期筛查（含 p-Tau 217 血液检测及两次门诊），癌症第二医疗意见扩至全部健康险客户，并新增由专属康复护士转介的宁养服务。调查指78%受访者认为确诊重病时非财务支援同等重要，69%不了解宁养服务；本港60岁以上人士认知障碍症患病率约10%、85岁以上约50%。",
             "tc": "富衛香港與養和醫療集團及靈實司務道寧養院合作升級 FWD Care：合資格健康險客戶可獲免費阿茲海默症早期篩查（含 p-Tau 217 血液檢測及兩次門診），癌症第二醫療意見擴至全部健康險客戶，並新增由專屬康復護士轉介的寧養服務。調查指78%受訪者認為確診重病時非財務支援同等重要，69%不了解寧養服務；本港60歲以上人士認知障礙症患病率約10%、85歲以上約50%。"},
    why={"sc": "真正可用于需求探索的是那组数字：69%不了解宁养服务、30%倾向居家照护。护理与临终阶段的安排几乎是客户从未被问过的问题，而它直接决定保额与保障结构是否够用。内容属第三方增值服务，须与条款保障分清。",
         "tc": "真正可用於需求探索的是那組數字：69%不了解寧養服務、30%傾向居家照護。護理與臨終階段的安排幾乎是客戶從未被問過的問題，而它直接決定保額與保障結構是否夠用。內容屬第三方增值服務，須與條款保障分清。"},
    actions={"front": {"sc": "用「确诊后谁照顾、在哪照顾」切入保障缺口，勿把第三方服务说成保单利益", "tc": "用「確診後誰照顧、在哪照顧」切入保障缺口，勿把第三方服務說成保單利益"},
             "midback": {"sc": "关注同业在健康险增值服务上的差异化路径", "tc": "關注同業在健康險增值服務上的差異化路徑"},
             "lead": {}, "cross": {}},
    rolesImpact={"front": 3, "midback": 2, "lead": 1, "cross": 0},
    source={"sc": "Insurance Asia（2026-09-22）", "lang": "en"},
    boards=["insurer", "product"], themes=["health", "consumer", "claims"],
    tags={"sc": ["富卫香港", "FWD Care", "阿兹海默症", "宁养服务", "健康险增值服务"],
          "tc": ["富衛香港", "FWD Care", "阿茲海默症", "寧養服務", "健康險增值服務"]},
    publishedAt="2026-09-22T00:35:00+08:00",
    originalUrl="https://insuranceasia.com/insurance/news/fwd-hong-kong-expands-care-awareness-gaps-persist",
))

# ── 3. AI 数据中心：安联火灾损失占比 ───────────────────────────────────
new_items.append(it(
    id="iaasia-ai-datacentre-fire-concentration-allianz-20260922",
    clusterCount=2, score=64, sourceTier="media", sourceKey="insuranceasia",
    title={"sc": "AI数据中心承保风险画像：安联分析约8亿美元损失中逾半由火灾造成，亚太（除中国）容量2030年将由约9吉瓦升至逾28吉瓦 [EN原文]",
           "tc": "AI數據中心承保風險畫像：安聯分析約8億美元損失中逾半由火災造成，亞太（除中國）容量2030年將由約9吉瓦升至逾28吉瓦 [EN原文]"},
    summary={"sc": "安联商业8月的报告分析约8亿美元数据中心损失，发现火灾占严重损失逾半，其后依次为自然灾害、犯罪与网络事件及电力故障。报告指美国与中国将占2030年前全球新增数据中心容量约62%，亚太（除中国）容量由约9吉瓦升至逾28吉瓦，马来西亚或录得十倍以上增长；数据中心相关保费料由约110亿美元增至2030年逾240亿美元。",
             "tc": "安聯商業8月的報告分析約8億美元數據中心損失，發現火災佔嚴重損失逾半，其後依次為自然災害、犯罪與網絡事件及電力故障。報告指美國與中國將佔2030年前全球新增數據中心容量約62%，亞太（除中國）容量由約9吉瓦升至逾28吉瓦，馬來西亞或錄得十倍以上增長；數據中心相關保費料由約110億美元增至2030年逾240億美元。"},
    why={"sc": "「火灾占严重损失逾半」把数据中心的巨灾想象从台风地震拉回日常工程与营运风险，也解释了为何承保人开始关注高压变压器更换周期与共用电力、冷却、网络带来的跨企业累积。对做企业客户与高净值客户资产安排的团队，这是可引用的风险结构说明。",
         "tc": "「火災佔嚴重損失逾半」把數據中心的巨災想像從颱風地震拉回日常工程與營運風險，也解釋了為何承保人開始關注高壓變壓器更換週期與共用電力、冷卻、網絡帶來的跨企業累積。對做企業客戶與高淨值客戶資產安排的團隊，這是可引用的風險結構說明。"},
    actions={"front": {"sc": "谈企业财产与工程险时，可用「单一事故可跨多家企业累积」解释投保范围", "tc": "談企業財產與工程險時，可用「單一事故可跨多家企業累積」解釋投保範圍"},
             "midback": {"sc": "关注数据中承保条款对网络与营运中断的定义", "tc": "關注數據中心承保條款對網絡與營運中斷的定義"},
             "lead": {"sc": "评估区域数据中心与能源基建承接能力的机会", "tc": "評估區域數據中心與能源基建承接能力的機會"},
             "cross": {}},
    rolesImpact={"front": 1, "midback": 2, "lead": 2, "cross": 0},
    source={"sc": "Insurance Asia（安联商业／瑞再研究院报告引述，2026-09-22）", "lang": "en"},
    boards=["tech", "market"], themes=["ai", "market", "tech"],
    tags={"sc": ["AI数据中心", "安联商业", "火灾风险", "承保能力", "亚太基建"],
          "tc": ["AI數據中心", "安聯商業", "火災風險", "承保能力", "亞太基建"]},
    publishedAt="2026-09-22T00:35:00+08:00",
    originalUrl="https://insuranceasia.com/insurance/expert-opinion/can-insurers-keep-pace-ai-data-centre-boom",
))

# ── 4. 航空险第四季续保 ────────────────────────────────────────────────
new_items.append(it(
    id="ibm-airline-insurers-selective-q4-renewals-20260921",
    score=62, sourceTier="media", sourceKey="insurancebusinessmag",
    title={"sc": "航空险转向选择性承保：容量充足但投放收紧，第四季完成全年机身及责任保费约65% [EN原文]",
           "tc": "航空險轉向選擇性承保：容量充足但投放收緊，第四季完成全年機身及責任保費約65% [EN原文]"},
    summary={"sc": "WTW《2026年第三季航空险展望》指大部分市场承保竞争仍健康，战争险持续软化，而机身与责任险承保人普遍寻求加价；Gallagher Specialty指理论承保能力远超需求，实际投放取决于航空公司风险轮廓、损失记录与区域枢纽集中度，部分承保人已削减份额或退出美国责任风险较高的业务。约65%的年度机身及责任首年保费在第四季完成。",
             "tc": "WTW《2026年第三季航空險展望》指大部分市場承保競爭仍健康，戰爭險持續軟化，而機身與責任險承保人普遍尋求加價；Gallagher Specialty指理論承保能力遠超需求，實際投放取決於航空公司風險輪廓、損失記錄與區域樞紐集中度，部分承保人已削減份額或退出美國責任風險較高的業務。約65%的年度機身及責任首年保費在第四季完成。"},
    why={"sc": "典型的「容量存在≠订约可得」：真正决定价格与条件的是累积风险与单一事件可波及的标的数量（俄罗斯租赁机队、无人机同时损毁多架飞机）。可作解释大型商业客户「市场软但你的方案不软」的实例。",
         "tc": "典型的「容量存在≠訂約可得」：真正決定價格與條件的是累積風險與單一事件可波及的標的數量（俄羅斯租賃機隊、無人機同時損毀多架飛機）。可作解釋大型商業客戶「市場軟但你的方案不軟」的實例。"},
    actions={"front": {}, "midback": {"sc": "同业对标：航空险与专业险的承保口径变化", "tc": "同業對標：航空險與專業險的承保口徑變化"},
             "lead": {"sc": "留意累积风险定价对区域大型商业账户的溢出效应", "tc": "留意累積風險定價對區域大型商業賬戶的溢出效應"},
             "cross": {}},
    rolesImpact={"front": 0, "midback": 2, "lead": 2, "cross": 0},
    source={"sc": "Insurance Business Asia（2026-09-21）", "lang": "en"},
    boards=["market"], themes=["pricing", "uw", "reinsurance"],
    tags={"sc": ["航空险", "第四季续保", "累积风险", "美国责任险", "WTW"],
          "tc": ["航空險", "第四季續保", "累積風險", "美國責任險", "WTW"]},
    publishedAt="2026-09-21T23:30:00+08:00",
    originalUrl="https://www.insurancebusinessmag.com/asia/news/breaking-news/airline-insurers-turn-more-selective-ahead-of-q4-renewals-590504.aspx",
))

# ── 5. 海上战争险逐航次核保 ────────────────────────────────────────────
new_items.append(it(
    id="ibm-marine-war-voyage-by-voyage-iumi-20260921",
    score=60, sourceTier="media", sourceKey="insurancebusinessmag",
    title={"sc": "IUMI：海上战争险转向逐航次核保，全球性开口保单「已不再是选项」 [EN原文]",
           "tc": "IUMI：海上戰爭險轉向逐航次核保，全球性開口保單「已不再是選項」 [EN原文]"},
    summary={"sc": "国际海上保险联盟（IUMI）主席 Frédéric Denèfle 在鹿特丹年会上表示，战争险核保所需信息远超船龄、船旗、船级与航行纪录，还须掌握航线、在高危水域停留时长及装卸货时间，全球性开口保单已不再是选项；截至9月16日，国际海事组织自2月28日中东冲突以来已核实霍尔木兹海峡周边80起商船遇袭事件，至少22名船员死亡。Lloyd's 6月已为海峡战争险成立新联合体。",
             "tc": "國際海上保險聯盟（IUMI）主席 Frédéric Denèfle 在鹿特丹年會上表示，戰爭險核保所需信息遠超船齡、船旗、船級與航行紀錄，還須掌握航線、在高危水域停留時長及裝卸貨時間，全球性開口保單已不再是選項；截至9月16日，國際海事組織自2月28日中东衝突以來已核實霍爾木茲海峽周邊80起商船遇襲事件，至少22名船員死亡。Lloyd's 6月已為海峽戰爭險成立新聯合體。"},
    why={"sc": "战争险从年度开口保单退回逐航次订约，等于把不确定性直接推给货主；同时澄清了「取消通知≠保单终止」这一常见误解——通知只是让承保人重新评估后以调整条件复效。香港作为区域海运与贸易枢纽，相关客户的安排值得提前厘清。",
         "tc": "戰爭險從年度開口保單退回逐航次訂約，等於把不確定性直接推給貨主；同時澄清了「取消通知≠保單終止」這一常見誤解——通知只是讓承保人重新評估後以調整條件復效。香港作為區域海運與貿易樞紐，相關客戶的安排值得提前釐清。"},
    actions={"front": {"sc": "提醒货运与贸易客户：高危水域的保障多为逐次订约，需提前申报航线", "tc": "提醒貨運與貿易客戶：高危水域的保障多為逐次訂約，需提前申報航線"},
             "midback": {"sc": "核查现有货运险／战争险条款是否覆盖中途改航与取消通知情形", "tc": "核查現有貨運險／戰爭險條款是否覆蓋中途改航與取消通知情形"},
             "lead": {"sc": "关注战争险容量与条款变化对区域贸易承保的影响", "tc": "關注戰爭險容量與條款變化對區域貿易承保的影響"},
             "cross": {}},
    rolesImpact={"front": 1, "midback": 2, "lead": 2, "cross": 0},
    source={"sc": "Insurance Business Asia（2026-09-21）", "lang": "en"},
    boards=["market"], themes=["marine", "uw", "market"],
    tags={"sc": ["海上战争险", "IUMI", "逐航次核保", "霍尔木兹海峡", "货运保险"],
          "tc": ["海上戰爭險", "IUMI", "逐航次核保", "霍爾木茲海峽", "貨運保險"]},
    publishedAt="2026-09-21T23:10:00+08:00",
    originalUrl="https://www.insurancebusinessmag.com/asia/news/marine/marine-war-cover-shifts-to-voyagebyvoyage-underwriting-590498.aspx",
))

# ── 6. 日本生命数据中心项目融资 ────────────────────────────────────────
new_items.append(it(
    id="ibm-nippon-life-data-centre-project-finance-20260921",
    score=63, sourceTier="media", sourceKey="insurancebusinessmag",
    title={"sc": "日本生命拟投放2万亿日元（127.5亿美元）于基建项目融资：数据中心保险成为融资前置条件 [EN原文]",
           "tc": "日本生命擬投放2萬億日元（127.5億美元）於基建項目融資：數據中心保險成為融資前置條件 [EN原文]"},
    summary={"sc": "日经亚洲9月20日报道，日本生命保险计划向基建项目融资投放2万亿日元（约127.5亿美元），主攻美国数据中心建设，并考虑于2026财年内在日本开展数据中心项目融资，目标2035财年把相关余额倍增至2万亿日元；路透表示未能独立核实。安联商业行政总裁 Thomas Lillelund 称，全面保险保障已成为许多大型AI基建项目融资的先决条件。",
             "tc": "日經亞洲9月20日報道，日本生命保險計劃向基建項目融資投放2萬億日元（約127.5億美元），主攻美國數據中心建設，並考慮於2026財年內在日本開展數據中心項目融資，目標2035財年把相關餘額倍增至2萬億日元；路透表示未能獨立核實。安聯商業行政總裁 Thomas Lillelund 稱，全面保險保障已成為許多大型AI基建項目融資的先決條件。"},
    why={"sc": "把「AI基建投资」与「保险可得性」直接挂钩：资金端把保障列为放款条件，保障端因此成为项目能否落地的变量。这类结构性信息对理解香港争取数据中心与能源基建落地的竞争力有参考价值。原文为媒体报道，未经保司确认。",
         "tc": "把「AI基建投資」與「保險可得性」直接掛鈎：資金端把保障列為放款條件，保障端因此成為項目能否落地的變量。這類結構性信息對理解香港爭取數據中心與能源基建落地的競爭力有參考價值。原文為媒體報道，未經保司確認。"},
    actions={"front": {}, "midback": {"sc": "关注保险保障作为基建融资条件的表述口径", "tc": "關注保險保障作為基建融資條件的表述口徑"},
             "lead": {"sc": "留意寿险资金转向基建与私人信贷对资产端配置的影响", "tc": "留意壽險資金轉向基建與私人信貸對資產端配置的影響"},
             "cross": {}},
    rolesImpact={"front": 0, "midback": 1, "lead": 3, "cross": 0},
    source={"sc": "Insurance Business Asia（引述日经亚洲／路透，2026-09-21）", "lang": "en"},
    boards=["insurer", "market"], themes=["ai", "capital", "market"],
    tags={"sc": ["日本生命", "数据中心", "项目融资", "基建投资", "AI基建保险"],
          "tc": ["日本生命", "數據中心", "項目融資", "基建投資", "AI基建保險"]},
    publishedAt="2026-09-21T22:50:00+08:00",
    originalUrl="https://www.insurancebusinessmag.com/asia/news/life-insurance/nippon-lifes-us12-75bn-data-centre-move-is-an-insurance-placement-story-not-just-a-finance-one-590508.aspx",
))

# ── 7. 亚太拆解保险市场 ────────────────────────────────────────────────
new_items.append(it(
    id="ian-apac-decommissioning-insurance-transition-20260921",
    score=72, sourceTier="pro", sourceKey="insuranceasianews",
    title={"sc": "亚太拆解（decommissioning）保险进入过渡期：印尼约630座海上平台、澳洲相关负债达450亿美元 [EN原文]",
           "tc": "亞太拆解（decommissioning）保險進入過渡期：印尼約630座海上平台、澳洲相關負債達450億美元 [EN原文]"},
    summary={"sc": "InsuranceAsia News报道，亚太退役拆解保险市场正进入过渡阶段，数千座海上油气设施接近营运寿命终点：印尼约630座海上平台，澳洲相关负债规模达450亿美元；Gallagher、Marsh 与 Tokio Marine 等正评估运营商在老龄能源基建上的拆解活动与风险承接方式。全文为付费订阅内容，本条摘要依据公开导语与信源署名。",
             "tc": "InsuranceAsia News報道，亞太退役拆解保險市場正進入過渡階段，數千座海上油氣設施接近營運壽命終點：印尼約630座海上平台，澳洲相關負債規模達450億美元；Gallagher、Marsh 與 Tokio Marine 等正評估運營商在老齡能源基建上的拆解活動與風險承接方式。全文為付費訂閱內容，本條摘要依據公開導語與信源署名。"},
    why={"sc": "退役负债正在从报表上的长期假设变成实际账单，且往往跨越十年以上——这与寿险长期负债的久期特征相似，是专项险与再保可以参与的领域。可作为「基建与能源转型」议题的观察点。",
         "tc": "退役負債正在從報表上的長期假設變成實際賬單，且往往跨越十年以上——這與壽險長期負債的久期特徵相似，是專項險與再保可以參與的領域。可作為「基建與能源轉型」議題的觀察點。"},
    actions={"front": {}, "midback": {"sc": "关注拆解与能源转型专项险的条款发展", "tc": "關注拆解與能源轉型專項險的條款發展"},
             "lead": {"sc": "留意区域专项险与再保承接的机会窗口", "tc": "留意區域專項險與再保承接的機會窗口"},
             "cross": {}},
    rolesImpact={"front": 0, "midback": 1, "lead": 2, "cross": 0},
    source={"sc": "InsuranceAsia News（2026-09-21）", "lang": "en"},
    boards=["market"], themes=["esg", "reinsurance", "market"],
    tags={"sc": ["退役拆解", "能源基建", "海上平台", "专项险", "再保"],
          "tc": ["退役拆解", "能源基建", "海上平台", "專項險", "再保"]},
    publishedAt="2026-09-21T21:40:00+08:00",
    originalUrl="https://insuranceasianews.com/apac-decommissioning-market-enters-transitional-phase-as-ageing-energy-assets-reach-end-of-life/",
))

# ── 8. Alpha TR W&I MGA 成立 ──────────────────────────────────────────
new_items.append(it(
    id="ian-alpha-tr-wi-mga-axa-xl-aviva-20260921",
    score=70, sourceTier="pro", sourceKey="insuranceasianews",
    title={"sc": "并购保证险（W&I）专业MGA「Alpha TR」启动：Axa XL 领头承保、Aviva Syndicates 提供承保纸，单一风险可承保5,400万美元 [EN原文]",
           "tc": "併購保證險（W&I）專業MGA「Alpha TR」啟動：Axa XL 領頭承保、Aviva Syndicates 提供承保紙，單一風險可承保5,400萬美元 [EN原文]"},
    summary={"sc": "伦敦并购保证险（W&I）专业MGA及劳合社承保代理人 Alpha TR 正式启动，由 Axa XL 提供领头承保能力、Aviva Syndicates（前 Probitas）提供承保纸，并获 SRG 支持；目标客群为美国以外国际市场的私募资本与另类资产基金，单一风险可部署5,400万美元。全文为付费订阅内容，摘要依据公开导语。",
             "tc": "倫敦併購保證險（W&I）專業MGA及勞合社承保代理人 Alpha TR 正式啟動，由 Axa XL 提供領頭承保能力、Aviva Syndicates（前 Probitas）提供承保紙，並獲 SRG 支持；目標客群為美國以外國際市場的私募資本與另類資產基金，單一風險可部署5,400萬美元。全文為付費訂閱內容，摘要依據公開導語。"},
    why={"sc": "交易保证险是高净值与家族客户在股权交易中常用的风险转移工具，新专业MGA进场意味着容量与条款竞争加剧。服务家办与私募客群的团队可留意报价与承保口径变化，但它属交易环节工具，不宜与个人寿险方案混谈。",
         "tc": "交易保證險是高淨值與家族客戶在股權交易中常用的風險轉移工具，新專業MGA進場意味着容量與條款競爭加劇。服務家辦與私募客群的團隊可留意報價與承保口徑變化，但它屬交易環節工具，不宜與個人壽險方案混談。"},
    actions={"front": {}, "midback": {"sc": "高客与家族客户交易环节的风险转移工具更新", "tc": "高客與家族客戶交易環節的風險轉移工具更新"},
             "lead": {"sc": "留意另类资产基金交易活跃度对W&I容量的带动", "tc": "留意另類資產基金交易活躍度對W&I容量的帶動"},
             "cross": {}},
    rolesImpact={"front": 0, "midback": 2, "lead": 2, "cross": 1},
    source={"sc": "InsuranceAsia News（2026-09-21）", "lang": "en"},
    boards=["market"], themes=["ma", "hnw"],
    tags={"sc": ["并购保证险", "W&I", "MGA", "家族办公室", "私募资本"],
          "tc": ["併購保證險", "W&I", "MGA", "家族辦公室", "私募資本"]},
    publishedAt="2026-09-21T21:25:00+08:00",
    originalUrl="https://insuranceasianews.com/transactional-risk-lloyds-coverholder-alpha-launches-backed-by-axa-xl-aviva/",
))

# ── 写入 ──────────────────────────────────────────────────────────────
data = json.load(open(LIVE, encoding='utf-8'))
items = data['items']
existing = {x.get('id') for x in items}
added, skipped = [], []
for n in new_items:
    if n['id'] in existing:
        skipped.append(n['id'])
        continue
    items.insert(0, n)
    existing.add(n['id'])
    added.append(n['id'])

data['meta']['generatedAt'] = NOW
json.dump(data, open(LIVE, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('added', len(added))
for a in added:
    print('  +', a)
if skipped:
    print('skipped dup', skipped)
print('total now', len(items))

# ── 检查点回写 ────────────────────────────────────────────────────────
chk = json.load(open(CHECK, encoding='utf-8'))
chk['lastCheck'] = NOW
for k, v in chk.get('sources', {}).items():
    v['last'] = NOW
json.dump(chk, open(CHECK, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('last-check updated ->', NOW)
