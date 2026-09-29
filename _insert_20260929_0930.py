#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-29 09:30 增量采集插入（覆盖 09-28 18:10 → 09-29 09:30 窗口）"""
import json, shutil, os

ROOT = os.path.dirname(os.path.abspath(__file__))
NOW = "2026-09-29T09:30:00+08:00"

def item(**kw):
    it = {
        "clusterCount": 1,
        "score": 70,
        "verifyStatus": "pending",
        "sourceTier": "media",
        "contentKind": "news",
        "source": {"sc": "", "tc": "", "lang": "en"},
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

# 1. Igloo 2025 年度账目（保险科技财务可持续性）
NEW.append(item(
    id="iaasia-igloo-net-loss-narrows-2025-20260929",
    score=68, verifyStatus="verified", sourceTier="media", sourceKey="insuranceasia",
    title={"sc": "新加坡Igloo 2025年净亏损收窄60.4%至673万美元、收入增45.9%：称靠嵌入式保险营运杠杆＋AI原生基建，目标2026年底经调整EBITDA打平 [EN原文]",
           "tc": "新加坡Igloo 2025年淨虧損收窄60.4%至673萬美元、收入增45.9%：稱靠嵌入式保險營運槓桿＋AI原生基建，目標2026年底經調整EBITDA打平 [EN原文]"},
    summary={"sc": "新加坡嵌入式保险科技商 Igloo 于 9 月 28 日公布经审计的 2025 年账目：净亏损收窄 60.4% 至 673 万美元（860 万新元），收入同比增 45.9% 至 6,327 万美元（8,090 万新元），营运开支大致持平。公司把改善归因于嵌入式保险业务的营运杠杆，以及 AI 原生基建令产品搭建、合作方营运与理赔处理自动化，合伙人数量与保单量增长未带来固定成本同比例上升。联合创办人兼 CEO Raunak Mehta 称「服务下一个合伙人与下一个百万张保单的成本持续下降」。公司目标 2026 年底实现经调整 EBITDA 收支平衡（汇率 1 美元＝1.28 新元）。",
             "tc": "新加坡嵌入式保險科技商 Igloo 於 9 月 28 日公布經審計的 2025 年帳目：淨虧損收窄 60.4% 至 673 萬美元（860 萬新元），收入同比增 45.9% 至 6,327 萬美元（8,090 萬新元），營運開支大致持平。公司把改善歸因於嵌入式保險業務的營運槓桿，以及 AI 原生基建令產品搭建、合作方營運與理賠處理自動化，合伙人數量與保單量增長未帶來固定成本同比例上升。聯合創辦人兼 CEO Raunak Mehta 稱「服務下一個合伙人與下一個百萬張保單的成本持續下降」。公司目標 2026 年底實現經調整 EBITDA 收支平衡（匯率 1 美元＝1.28 新元）。"},
    why={"sc": "保险科技的叙事正从「补贴换规模」转向「AI原生降本」，Igloo 是少数给出经审计数字与打平时间表的样本。港险渠道与科技合作方越来越多来自这类公司，其单位服务成本与 EBITDA 时间表是判断合作方能否长期存续、以及渠道外包条款风险的公开参照。",
         "tc": "保險科技的敘事正從「補貼換規模」轉向「AI 原生降本」，Igloo 是少數給出經審計數字與打平時間表的樣本。港險渠道與科技合作方越來越多來自這類公司，其單位服務成本與 EBITDA 時間表是判斷合作方能否長期存續、以及渠道外包條款風險的公開參照。"},
    actions={"front": {},
             "midback": {"sc": "评估数字/嵌入式渠道合作前，要求对方披露单位服务成本趋势与EBITDA打平时间表",
                         "tc": "評估數字/嵌入式渠道合作前，要求對方披露單位服務成本趨勢與 EBITDA 打平時間表"},
             "lead": {"sc": "把「渠道方财务可持续性」纳入合作评估清单，避免只以新单量作唯一指标",
                      "tc": "把「渠道方財務可持續性」納入合作評估清單，避免只以新單量作唯一指標"},
             "cross": {"sc": "关注科技方股东背景（含日资、创投方）对本地合作资源与合规安排的影响",
                       "tc": "關注科技方股東背景（含日資、創投方）對本地合作資源與合規安排的影響"}},
    rolesImpact={"front": 0, "midback": 1, "lead": 1, "cross": 1},
    source={"sc": "Insurance Asia 2026-09-29（Igloo 2025 年度经审计账目 2026-09-28 发布）[EN原文]",
            "tc": "Insurance Asia 2026-09-29（Igloo 2025 年度經審計賬目 2026-09-28 發布）[EN原文]", "lang": "en"},
    boards=["tech"], themes=["insurtech", "ai", "cost"],
    tags={"sc": ["保险科技", "Igloo", "嵌入式保险", "AI原生", "EBITDA", "新加坡"],
          "tc": ["保險科技", "Igloo", "嵌入式保險", "AI原生", "EBITDA", "新加坡"]},
    publishedAt="2026-09-29T05:45:00+08:00",
    originalUrl="https://insuranceasia.com/insurance/news/igloos-net-loss-narrows-604-in-2025",
))

# 2. 印度分销改革（Nomura 解读）
NEW.append(item(
    id="iaasia-india-distribution-reform-nomura-20260929",
    score=72, verifyStatus="verified", sourceTier="media", sourceKey="insuranceasia",
    title={"sc": "印度拟议分销改革：寿险代理扩张料加速，但一般险与健康险佣金上限「偏陡」、车险三者险佣金归零——Nomura解读 [EN原文]",
           "tc": "印度擬議分銷改革：壽險代理擴張料加速，但一般險與健康險佣金上限「偏陡」、車險三者險佣金歸零——Nomura解讀 [EN原文]"},
    summary={"sc": "Insurance Asia 9 月 29 日报道 Nomura Global Markets Research（报告日期 2026 年 9 月 24 日）对印度保险监管机构拟议分销改革的解读：改革令费用管理（EOM）上限更严，并按产品、渠道与地区重新引入佣金上限。个人纯定期寿险获相近或更优佣金结构，预计加速寿险公司代理渠道扩张；一般险与健康险佣金上限相对寿险「偏陡」，其中健康险上限比现行支付水平更严，车险第三方责任险佣金由 2.5% 上限降至零。Nomura 担忧健康险分销渠道的销售动力，并指车险零佣金或拖慢私人一般险公司依靠车行扩份额的步伐；在其覆盖的寿险公司中，SBI Life 的费用管理比率最为宽松、处境最佳。",
             "tc": "Insurance Asia 9 月 29 日報道 Nomura Global Markets Research（報告日期 2026 年 9 月 24 日）對印度保險監管機構擬議分銷改革的解讀：改革令費用管理（EOM）上限更嚴，並按產品、渠道與地區重新引入佣金上限。個人純定期壽險獲相近或更優佣金結構，預計加速壽險公司代理渠道擴張；一般險與健康險佣金上限相對壽險「偏陡」，其中健康險上限比現行支付水平更嚴，車險第三者責任險佣金由 2.5% 上限降至零。Nomura 擔憂健康險分銷渠道的銷售動力，並指車險零佣金或拖慢私人一般險公司依靠車行擴份額的步伐；在其覆蓋的壽險公司中，SBI Life 的費用管理比率最為寬鬆、處境最佳。"},
    why={"sc": "印度是全球中介与银保佣金监管的实验场：「收紧费用管理＋重建佣金上限＋车险三者险零佣金」这一组合，正面回答监管如何在压低渠道成本与保住分销动力之间取舍。对香港讨论转介费上限、佣金与费用披露的同事，是一份现成的区域对照样本。",
         "tc": "印度是全球中介與銀保佣金監管的實驗場：「收緊費用管理＋重建佣金上限＋車險三者險零佣金」這一組合，正面回答監管如何在壓低渠道成本與保住分銷動力之間取捨。對香港討論轉介費上限、佣金與費用披露的同事，是一份現成的區域對照樣本。"},
    actions={"front": {},
             "midback": {"sc": "把印度分销佣金改革列为区域监管对照案例，用于佣金结构与费用管控讨论",
                         "tc": "把印度分銷佣金改革列為區域監管對照案例，用於佣金結構與費用管控討論"},
             "lead": {"sc": "渠道激励设计中预留「监管压降费用」情景，避免承诺长期高佣金结构",
                      "tc": "渠道激勵設計中預留「監管壓降費用」情景，避免承諾長期高佣金結構"},
             "cross": {"sc": "关注港资/中资保司在印度的合作与投资门槛变化对区域布局的影响",
                       "tc": "關注港資/中資保司在印度的合作與投資門檻變化對區域佈局的影響"}},
    rolesImpact={"front": 0, "midback": 1, "lead": 2, "cross": 1},
    source={"sc": "Insurance Asia 2026-09-29（引 Nomura Global Markets Research 2026-09-24 报告）[EN原文]",
            "tc": "Insurance Asia 2026-09-29（引 Nomura Global Markets Research 2026-09-24 報告）[EN原文]", "lang": "en"},
    boards=["reg"], themes=["regulation", "distribution", "commission"],
    tags={"sc": ["印度", "IRDAI", "佣金上限", "费用管理", "Nomura", "分销渠道"],
          "tc": ["印度", "IRDAI", "佣金上限", "費用管理", "Nomura", "分銷渠道"]},
    publishedAt="2026-09-29T05:30:00+08:00",
    originalUrl="https://insuranceasia.com/news/india-insurance-reforms-boost-life-agents-expansion-health-caps-tightened",
))

# 3. 安联世博旅游险生态（产品/数字化）
NEW.append(item(
    id="iaasia-allianz-partners-travel-ecosystem-au-20260929",
    score=70, verifyStatus="verified", sourceTier="media", sourceKey="insuranceasia",
    title={"sc": "安联世博在澳洲上线新一代旅游险生态：客户可自助加购邮轮、滑雪与探险保障并延长行程，主打「非一价通吃」 [EN原文]",
           "tc": "安聯世博在澳洲上線新一代旅遊險生態：客戶可自助加購郵輪、滑雪與探險保障並延長行程，主打「非一價通吃」 [EN原文]"},
    summary={"sc": "Allianz Partners 在 9 月 28 日声明中宣布于澳洲透过其 Metaportal 平台推出新一代旅游保险生态：客户可在线激活与管理旅游保障，并按需自选加购项——包括邮轮、滑雪、探险旅游保障，以及更高取消上限与更长行程天数。澳洲旅游险执行主管 Damiel Arthur 表示，客户期望已改变，「一价通吃」不再适用：今天的旅客要的是反映其出行方式、地点与原因的保障，企业则希望藉此强化客户关系与长期黏性。",
             "tc": "Allianz Partners 在 9 月 28 日聲明中宣布於澳洲透過其 Metaportal 平台推出新一代旅遊保險生態：客戶可線上激活與管理旅遊保障，並按需自選加購項——包括郵輪、滑雪、探險旅遊保障，以及更高取消上限與更長行程天數。澳洲旅遊險執行主管 Damiel Arthur 表示，客戶期望已改變，「一價通吃」不再適用：今天的旅客要的是反映其出行方式、地點與原因的保障，企業則希望藉此強化客戶關係與長期黏性。"},
    why={"sc": "旅游险正从「标准套餐」转向「模块化自选＋自助保单管理」，与香港保诚刚推出的大湾区短途旅游险升级是同一趋势。对前线而言，它直接改变销售动作（做「出行场景→加购项」清单而非只报保额），也提示线上自选模式对人工中介的替代压力。",
         "tc": "旅遊險正從「標準套餐」轉向「模組化自選＋自助保單管理」，與香港保誠剛推出的大灣區短途旅遊險升級是同一趨勢。對前線而言，它直接改變銷售動作（做「出行場景→加購項」清單而非只報保額），也提示線上自選模式對人工中介的替代壓力。"},
    actions={"front": {"sc": "按出行场景逐项核对除外与限额：邮轮、滑雪、探险各自是否受保、器材与救援是否限额",
                       "tc": "按出行場景逐項核對除外與限額：郵輪、滑雪、探險各自是否受保、器材與救援是否限額"},
             "midback": {"sc": "整理本地旅游险「可加购 vs 必然除外」清单，作为客户咨询的标准答复材料",
                         "tc": "整理本地旅遊險「可加購 vs 必然除外」清單，作為客戶諮詢的標準答覆材料"},
             "lead": {"sc": "关注模块化定价对旅游险佣金结构、续保率与销售话术的影响",
                      "tc": "關注模組化定價對旅遊險佣金結構、續保率與銷售話術的影響"},
             "cross": {"sc": "多程出行高客可评估年度多次行程产品与家庭整体安排的匹配度",
                       "tc": "多程出行高客可評估年度多次行程產品與家庭整體安排的匹配度"}},
    rolesImpact={"front": 2, "midback": 1, "lead": 1, "cross": 1},
    source={"sc": "Insurance Asia 2026-09-29（Allianz Partners 2026-09-28 声明）[EN原文]",
            "tc": "Insurance Asia 2026-09-29（Allianz Partners 2026-09-28 聲明）[EN原文]", "lang": "en"},
    boards=["product"], themes=["travel", "product", "digital"],
    tags={"sc": ["旅游保险", "安联世博", "模块化保障", "澳洲", "数字化投保", "自驾/邮轮/滑雪"],
          "tc": ["旅遊保險", "安聯世博", "模組化保障", "澳洲", "數字化投保", "自駕/郵輪/滑雪"]},
    publishedAt="2026-09-29T05:15:00+08:00",
    originalUrl="https://insuranceasia.com/insurance/news/allianz-partners-launches-personalised-digital-travel-insurance-cover-in-australia",
))

# 4. AM Best 对 Tokio Marine 资本评估
NEW.append(item(
    id="iaasia-tokio-marine-am-best-capital-20260929",
    score=68, verifyStatus="verified", sourceTier="media", sourceKey="insuranceasia",
    title={"sc": "AM Best：Tokio Marine资产负债表评为「最强」、资本足以吸收波动，惟海外扩张带来权益与承保风险；集团拟FY2029前清空策略性持股 [EN原文]",
           "tc": "AM Best：Tokio Marine資產負債表評為「最強」、資本足以吸收波動，惟海外擴張帶來權益與承保風險；集團擬FY2029前清空策略性持股 [EN原文]"},
    summary={"sc": "Insurance Asia 9 月 29 日引述 AM Best 报告：Tokio Marine Holdings 因海外扩张而仍然承担权益风险与日益上升的承保风险，但资本足以吸收潜在波动，资产负债表强度获评为「最强」，同时具备良好经营绩效、非常有利的业务组合与很强的企业风险管理。集团已加速策略性持股处置计划，目标在 2029 财年前全数清仓，中期将显著降低权益风险敞口；国际业务盈利能力持续改善（北美利润增长强劲），本土承保亦保持韧性。",
             "tc": "Insurance Asia 9 月 29 日引述 AM Best 報告：Tokio Marine Holdings 因海外擴張而仍然承擔權益風險與日益上升的承保風險，但資本足以吸收潛在波動，資產負債表強度獲評為「最強」，同時具備良好經營績效、非常有利的業務組合與很強的企業風險管理。集團已加速策略性持股處置計劃，目標在 2029 財年前全數清倉，中期將顯著降低權益風險敞口；國際業務盈利能力持續改善（北美利潤增長強勁），本土承保亦保持韌性。"},
    why={"sc": "亚洲大型保险集团正系统性「降权益风险、靠海外承保与再保增长」，这决定它们对再保价格的议价能力与资本回报节奏。集团层评级与资本评估，是判断合作保司长期承保能力与再保安排稳健度的公开依据，比宣传口径更可用。",
         "tc": "亞洲大型保險集團正系統性「降權益風險、靠海外承保與再保增長」，這決定它們對再保價格的議價能力與資本回報節奏。集團層評級與資本評估，是判斷合作保司長期承保能力與再保安排穩健度的公開依據，比宣傳口徑更可用。"},
    actions={"front": {},
             "midback": {"sc": "把主要合作保司的集团评级与资本评估结论纳入年度复核材料",
                         "tc": "把主要合作保司的集團評級與資本評估結論納入年度覆核材料"},
             "lead": {"sc": "向高客解释集团资本实力时引用评级机构原文与日期，不用宣传性表述",
                      "tc": "向高客解釋集團資本實力時引用評級機構原文與日期，不用宣傳性表述"},
             "cross": {"sc": "关注日资集团在亚太再保、并购与资本处置上的后续动作",
                       "tc": "關注日資集團在亞太再保、併購與資本處置上的後續動作"}},
    rolesImpact={"front": 0, "midback": 1, "lead": 2, "cross": 1},
    source={"sc": "Insurance Asia 2026-09-29（引 AM Best 报告）[EN原文]",
            "tc": "Insurance Asia 2026-09-29（引 AM Best 報告）[EN原文]", "lang": "en"},
    boards=["insurer"], themes=["rating", "capital", "reinsurance"],
    tags={"sc": ["Tokio Marine", "AM Best", "评级", "资本充足", "权益风险", "日本保险"],
          "tc": ["Tokio Marine", "AM Best", "評級", "資本充足", "權益風險", "日本保險"]},
    publishedAt="2026-09-29T05:00:00+08:00",
    originalUrl="https://insuranceasia.com/insurance/news/tokio-marines-capital-sufficient-despite-equity-and-overseas-risks-am-best",
))

# 5. AI 信任与客户数据（技术/合规）
NEW.append(item(
    id="iaasia-ai-trust-customer-data-20260929",
    score=74, verifyStatus="verified", sourceTier="media", sourceKey="insuranceasia",
    title={"sc": "业界警告：用公开数据做AI分析会侵蚀客户信任——建议改用自有理赔与风控记录，并建立清晰的AI治理与披露规则 [EN原文]",
           "tc": "業界警告：用公開數據做AI分析會侵蝕客戶信任——建議改用自有理賠與風控記錄，並建立清晰的AI治理與披露規則 [EN原文]"},
    summary={"sc": "Insurance Asia 9 月 29 日独家报道：Lockton 高级副总裁 Olive Lam 指，把公开可得数据用于涉及客户的 AI 分析会侵蚀信任——客户会质疑为何收集其资料、如何据此作决定，甚至担心第三方信息被误读；她建议改用与客户直接相关的信息（历史理赔与事故、内部风险评估、损失控制记录、场地设施特征），并结合自身数据库中的损失经验、核保指引与可比较风险。EY-Parthenon 合伙人 Oki Stefanus 强调须建立治理框架、透明度与问责机制。文中引 Smart Communications 6 月报告：仅 38% 消费者认为 AI 在保险互动中有帮助、84% 要求披露 AI 使用；29% 曾因私隐或透明度疑虑而停止与保司往来，63% 全球消费者（新加坡 67%）表示沟通未达期望会换保司。",
             "tc": "Insurance Asia 9 月 29 日獨家報道：Lockton 高級副總裁 Olive Lam 指，把公開可得數據用於涉及客戶的 AI 分析會侵蝕信任——客戶會質疑為何收集其資料、如何據此作決定，甚至擔心第三方信息被誤讀；她建議改用與客戶直接相關的信息（歷史理賠與事故、內部風險評估、損失控制記錄、場地設施特徵），並結合自身數據庫中的損失經驗、核保指引與可比較風險。EY-Parthenon 合伙人 Oki Stefanus 強調須建立治理框架、透明度與問責機制。文中引 Smart Communications 6 月報告：僅 38% 消費者認為 AI 在保險互動中有幫助、84% 要求披露 AI 使用；29% 曾因私隱或透明度疑慮而停止與保司往來，63% 全球消費者（新加坡 67%）表示溝通未達期望會換保司。"},
    why={"sc": "AI 在保险场景的争议正从「能不能用」转向「数据从哪来、怎样讲清楚」。这对香港前线同样适用：凡以 AI 辅助核保、理赔、客群分析的表述，都需要数据来源与披露口径支撑，否则同时踩信任与合规两条线。",
         "tc": "AI 在保險場景的爭議正從「能不能用」轉向「數據從哪來、怎樣講清楚」。這對香港前線同樣適用：凡以 AI 輔助核保、理賠、客群分析的表述，都需要數據來源與披露口徑支撐，否則同時踩信任與合規兩條線。"},
    actions={"front": {"sc": "客户沟通中不得把AI分析结果当作保障范围或理赔结论的依据，遇个案须回到条款与核保口径",
                       "tc": "客戶溝通中不得把 AI 分析結果當作保障範圍或理賠結論的依據，遇個案須回到條款與核保口徑"},
             "midback": {"sc": "梳理团队在用AI工具的数据来源，区分「自有客户数据」与「公开/第三方数据」并标注使用边界",
                         "tc": "梳理團隊在用 AI 工具的數據來源，區分「自有客戶數據」與「公開/第三方數據」並標註使用邊界"},
             "lead": {"sc": "引进AI工具时要求供应商说明数据来源、模型输出用途与披露机制，留存书面记录",
                      "tc": "引進 AI 工具時要求供應商說明數據來源、模型輸岀用途與披露機制，留存書面記錄"},
             "cross": {"sc": "高客数据敏感度高，优先使用内部数据、保留人工复核环节与沟通留痕",
                       "tc": "高客數據敏感度高，優先使用內部數據、保留人工覆核環節與溝通留痕"}},
    rolesImpact={"front": 1, "midback": 2, "lead": 2, "cross": 1},
    source={"sc": "Insurance Asia 2026-09-29 独家（引 Lockton、EY-Parthenon、Smart Communications 2026-06 报告）[EN原文]",
            "tc": "Insurance Asia 2026-09-29 獨家（引 Lockton、EY-Parthenon、Smart Communications 2026-06 報告）[EN原文]", "lang": "en"},
    boards=["tech"], themes=["ai", "data", "compliance"],
    tags={"sc": ["AI治理", "客户数据", "私隐", "信任", "Lockton", "披露"],
          "tc": ["AI治理", "客戶數據", "私隱", "信任", "Lockton", "披露"]},
    publishedAt="2026-09-29T05:00:00+08:00",
    originalUrl="https://insuranceasia.com/insurance/exclusive/insurers-told-use-own-customer-data-build-ai-trust",
))

# 6. 亚太再保 2027 续保前瞻
NEW.append(item(
    id="ian-apac-reinsurance-right-sizing-2027-20260929",
    score=70, verifyStatus="pending", sourceTier="media", sourceKey="insuranceasianews",
    title={"sc": "亚太再保进入新阶段：定价承压、资本高企，分出公司转向「把再保安排调整到合适规模」，2027续保周期成观察窗口 [EN原文]",
           "tc": "亞太再保進入新階段：定價承壓、資本高企，分出公司轉向「把再保安排調整到合適規模」，2027續保週期成觀察窗口 [EN原文]"},
    summary={"sc": "InsuranceAsia News 9 月 29 日分析（付费内容，仅摘要公开）：亚太再保市场正进入新阶段——定价条件开始承压，同时资本水平维持高位，分出公司与再保人日益聚焦把再保安排「调整到合适规模（right-sizing）」。公开导语指行业领袖正在软化定价环境、创纪录承保能力、新兴风险与快速演变的风险格局之间取得平衡。文章定位于 2027 年续保周期前瞻分析，具体条款、自留额与价格细节未公开，本站未取得全文。",
             "tc": "InsuranceAsia News 9 月 29 日分析（付費內容，僅摘要公開）：亞太再保市場正進入新階段——定價條件開始承壓，同時資本水平維持高位，分出公司與再保人日益聚焦把再保安排「調整到合適規模（right-sizing）」。公開導語指行業領袖正在軟化定價環境、創紀錄承保能力、新興風險與快速演變的風險格局之間取得平衡。文章定位於 2027 年續保週期前瞻分析，具體條款、自留額與價格細節未公開，本站未取得全文。"},
    why={"sc": "2027 续保季的价格与结构走向最终会传导到香港的核保成本与产品定价，尤其医疗、寿险与巨灾相关再保安排。right-sizing 意味着分出公司不再只求压价，而是重新评估自留额与保障层级——这是理解明年承保条件的前置信号，值得在年度产品定价复核前跟踪。",
         "tc": "2027 續保季的價格與結構走向最終會傳導到香港的核保成本與產品定價，尤其醫療、壽險與巨災相關再保安排。right-sizing 意味著分出公司不再只求壓價，而是重新評估自留額與保障層級——這是理解明年承保條件的前置信號，值得在年度產品定價覆核前跟蹤。"},
    actions={"front": {},
             "midback": {"sc": "关注2027续保季自留额与保障层级调整，及其对核保口径与理赔处理的影响",
                         "tc": "關注2027續保季自留額與保障層級調整，及其對核保口徑與理賠處理的影響"},
             "lead": {"sc": "年度产品定价复核时把再保成本假设单列，避免以「再保趋软」一句概括",
                      "tc": "年度產品定價覆核時把再保成本假設單列，避免以「再保趨軟」一句概括"},
             "cross": {"sc": "高客大额保单的再保承接能力与自留安排须个案确认，不作普遍承诺",
                       "tc": "高客大額保單的再保承接能力與自留安排須個案確認，不作普遍承諾"}},
    rolesImpact={"front": 0, "midback": 2, "lead": 2, "cross": 1},
    source={"sc": "InsuranceAsia News 2026-09-29（Analysis，付费墙；仅采用公开摘要）[EN原文]",
            "tc": "InsuranceAsia News 2026-09-29（Analysis，付費牆；僅採用公開摘要）[EN原文]", "lang": "en"},
    boards=["market"], themes=["reinsurance", "renewals", "capacity"],
    tags={"sc": ["再保险", "2027续保", "承保能力", "自留额", "亚太市场", "right-sizing"],
          "tc": ["再保險", "2027續保", "承保能力", "自留額", "亞太市場", "right-sizing"]},
    publishedAt="2026-09-29T07:30:00+08:00",
    originalUrl="https://insuranceasianews.com/cedents-to-focus-on-right-sizing-reinsurance-programs-as-apac-market-enters-new-phase/",
))

# ---------- 写入 ----------
path = os.path.join(ROOT, "data", "live-items.json")
shutil.copy(path, os.path.join(ROOT, "data", "live-items.json.bak-0929-0930"))
data = json.load(open(path, encoding="utf-8"))
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
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("inserted:", len(new), "skipped:", skipped, "total:", n)
for it in new:
    print(" -", it["publishedAt"], it["id"], "|", it["score"], it["verifyStatus"])
