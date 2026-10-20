# -*- coding: utf-8 -*-
"""2026-10-21 18:08 增量：11 条（IA 执法 / 巨灾与 ILS / AI 代理 / 亚洲人事）"""
import json

PATH = '/Users/leonliang/maoquanqingbao/data/live-items.json'
NOW = '2026-10-21T18:08:00+08:00'

d = json.load(open(PATH, encoding='utf-8'))
items = d['items']
existing = {i.get('originalUrl', '').split('?')[0].rstrip('/') for i in items}

new_items = [
    {
        "id": "insuranceasianews-helvetia-asia-ceo-tan-20261021",
        "publishedAt": "2026-10-21T05:00:00+08:00",
        "originalUrl": "https://insuranceasianews.com/siew-choo-tan-to-succeed-ivan-chan-as-helvetia-asia-ceo/",
        "sourceKey": "insuranceasianews",
        "sourceTier": "media",
        "score": 64,
        "verifyStatus": "pending",
        "contentKind": "news",
        "clusterCount": 1,
        "boards": ["insurer"],
        "themes": ["people-move", "asia", "leadership", "distribution"],
        "title": {
            "sc": "Helvetia 任命 Siew Choo Tan 为亚洲区 CEO　2027 年 1 月接替九年任期的 Ivan Chan",
            "tc": "Helvetia 任命 Siew Choo Tan 為亞洲區 CEO　2027 年 1 月接替九年任期的 Ivan Chan"
        },
        "summary": {
            "sc": "Helvetia 公布，任命 Siew Choo Tan 出任亚洲区行政总裁，2027 年 1 月 1 日起生效，仍待监管批准，接替任职九年的 Ivan Chan。Chan 会在交接期内转任高级顾问一职。（原文有付费墙，仅据首段与公司新闻稿摘要。）",
            "tc": "Helvetia 公布，任命 Siew Choo Tan 出任亞洲區行政總裁，2027 年 1 月 1 日起生效，仍待監管批准，接替任職九年的 Ivan Chan。Chan 會在交接期內轉任高級顧問一職。（原文有付費牆，僅據首段與公司新聞稿摘要。）"
        },
        "why": {
            "sc": "外资险企亚洲区一把手换届，通常伴随分销策略与合作安排微调。这类人事变动不会即时影响保单条款，但会影响续保谈判节奏、代理合作条件与新产品引入时间表，值得留意后续人事与策略公布。",
            "tc": "外資險企亞洲區一把手換屆，通常伴隨分銷策略與合作安排微調。這類人事變動不會即時影響保單條款，但會影響續保談判節奏、代理合作條件與新產品引入時間表，值得留意後續人事與策略公布。"
        },
        "source": {
            "sc": "InsuranceAsia News 2026-10-21（引 Helvetia 公司公告）",
            "tc": "InsuranceAsia News 2026-10-21（引 Helvetia 公司公告）",
            "lang": "en",
            "name": "insuranceasianews",
            "date": "2026-10-21"
        },
        "tags": {
            "sc": ["人事变动", "亚洲区CEO", "Helvetia", "外资险企", "交接"],
            "tc": ["人事變動", "亞洲區CEO", "Helvetia", "外資險企", "交接"]
        },
        "actions": {
            "front": {"sc": "客户沟通：合作方人事变动提示", "tc": "客户溝通：合作方人事變動提示"},
            "midback": {"sc": "合作方跟踪：策略与条款节奏", "tc": "合作方跟蹤：策略與條款節奏"},
            "lead": {"sc": "团队简报：外资险企亚洲布局", "tc": "團隊簡報：外資險企亞洲佈局"},
            "cross": {"sc": "—", "tc": "—"}
        },
        "rolesImpact": {"front": 1, "midback": 1, "lead": 1, "cross": 0},
        "ingestedAt": NOW
    },
    {
        "id": "reinsurancenews-meta-muse-ai-claims-risk-20261020",
        "publishedAt": "2026-10-21T00:00:00+08:00",
        "originalUrl": "https://www.reinsurancene.ws/metas-muse-ai-agents-could-pose-longer-term-risk-to-loss-costs-autonomous/",
        "sourceKey": "reinsurancenews",
        "sourceTier": "pro",
        "score": 72,
        "verifyStatus": "verified",
        "contentKind": "report",
        "clusterCount": 1,
        "boards": ["tech"],
        "themes": ["agentic-ai", "claims", "loss-cost", "consumer-behaviour"],
        "title": {
            "sc": "Autonomous：Meta「Muse」AI 代理或长远推高理赔成本　已能提醒索赔步骤并连接律师行",
            "tc": "Autonomous：Meta「Muse」AI 代理或長遠推高理賠成本　已能提醒索賠步驟並連接律師行"
        },
        "summary": {
            "sc": "Autonomous 报告把 Meta 的 Muse AI 代理用于购物、支付、存款、投资与保险场景测试：在车险、租客险与微型商业险比价中，Muse 会提醒推进理赔的必办步骤，并替用户连接多家可协助争取最大赔付的律师行。报告认为代理式 AI 将提升简单消费险的价格透明度，长远或有推高理赔成本之虞，但现时仍不及真人代理。",
            "tc": "Autonomous 報告把 Meta 的 Muse AI 代理用於購物、支付、存款、投資與保險場景測試：在車險、租客險與微型商業險比價中，Muse 會提醒推進理賠的必辦步驟，並替用户連接多家可協助爭取最大賠付的律師行。報告認為代理式 AI 將提升簡單消費險的價格透明度，長遠或有推高理賠成本之虞，但現時仍不及真人代理。"
        },
        "why": {
            "sc": "报告的关键不是「AI 会抢代理生意」，而是客户行为变了：索赔前先问 AI、比价前先被 AI 教育。前沿团队应预演「客户带着 AI 生成的对比表来谈」的场景，把不可替代的部分（核保判断、理赔争取、跨公司协调）讲清楚，而不是跟着 AI 比数字。",
            "tc": "報告的關鍵不是「AI 會搶代理生意」，而是客户行為變了：索賠前先問 AI、比價前先被 AI 教育。前線團隊應預演「客户帶着 AI 生成的對比表來談」的場景，把不可替代的部分（核保判斷、理賠爭取、跨公司協調）講清楚，而不是跟着 AI 比數字。"
        },
        "source": {
            "sc": "Reinsurance News 2026-10-21（引 Autonomous 研究报告）",
            "tc": "Reinsurance News 2026-10-21（引 Autonomous 研究報告）",
            "lang": "en",
            "name": "reinsurancenews",
            "date": "2026-10-21"
        },
        "tags": {
            "sc": ["AI代理", "理赔成本", "价格透明", "消费险", "Meta"],
            "tc": ["AI代理", "理賠成本", "價格透明", "消費險", "Meta"]
        },
        "actions": {
            "front": {"sc": "客户沟通：AI 比价之后还差什么", "tc": "客户溝通：AI 比價之後還差什麼"},
            "midback": {"sc": "理赔服务：可解释的争取路径", "tc": "理賠服務：可解釋的爭取路徑"},
            "lead": {"sc": "团队培训：应对 AI 辅助客户", "tc": "團隊培訓：應對 AI 輔助客户"},
            "cross": {"sc": "AI 应用风险议题素材", "tc": "AI 應用風險議題素材"}
        },
        "rolesImpact": {"front": 2, "midback": 1, "lead": 2, "cross": 1},
        "ingestedAt": NOW
    },
    {
        "id": "artemis-perils-july-scs-loss-2806m-20261020",
        "publishedAt": "2026-10-20T23:10:00+08:00",
        "originalUrl": "https://www.artemis.bm/news/perils-lifts-july-european-convective-storms-insured-market-loss-estimate-to-e2-8bn/",
        "sourceKey": "artemis",
        "sourceTier": "pro",
        "score": 71,
        "verifyStatus": "verified",
        "contentKind": "report",
        "clusterCount": 1,
        "boards": ["market"],
        "themes": ["catastrophe", "secondary-perils", "loss-estimate", "europe"],
        "title": {
            "sc": "PERILS 上调 7 月欧洲强对流风暴损失约 28% 至 28.06 亿欧元",
            "tc": "PERILS 上調 7 月歐洲強對流風暴損失約 28% 至 28.06 億歐元"
        },
        "summary": {
            "sc": "PERILS 将 2026 年 7 月 13–19 日吹袭德、法、瑞士及意大利的强对流风暴「Cerry」行业损失估算由初估 21.86 亿欧元上调约 28% 至 28.06 亿欧元，数据来自受影响险企的财产险与车险。这是 PERILS 有记录以来欧洲强对流单次损失最高，第三次估算将于 2027 年 1 月 19 日公布。",
            "tc": "PERILS 將 2026 年 7 月 13–19 日吹襲德、法、瑞士及意大利的強對流風暴「Cerry」行業損失估算由初估 21.86 億歐元上調約 28% 至 28.06 億歐元，數據來自受影響險企的財產險與車險。這是 PERILS 有記錄以來歐洲強對流單次損失最高，第三次估算將於 2027 年 1 月 19 日公布。"
        },
        "why": {
            "sc": "强对流这类「次生灾害」已连续刷新欧洲损失纪录（同月另一场 8 月风暴初估 32.96 亿欧元），说明再保人定价的重心正从飓风转向高频次生风险。讨论大湾区／亚洲巨灾保障缺口与参数式产品时，这是可直接引用的量化参照。",
            "tc": "強對流這類「次生災害」已連續刷新歐洲損失紀錄（同月另一場 8 月風暴初估 32.96 億歐元），說明再保人定價的重心正從颶風轉向高頻次生風險。討論大灣區／亞洲巨災保障缺口與參數式產品時，這是可直接引用的量化參照。"
        },
        "source": {
            "sc": "Artemis 2026-10-20（引 PERILS 第二次损失估算）",
            "tc": "Artemis 2026-10-20（引 PERILS 第二次損失估算）",
            "lang": "en",
            "name": "artemis",
            "date": "2026-10-20"
        },
        "tags": {
            "sc": ["强对流", "次生灾害", "行业损失", "PERILS", "欧洲"],
            "tc": ["強對流", "次生災害", "行業損失", "PERILS", "歐洲"]
        },
        "actions": {
            "front": {"sc": "客户沟通：次生灾害保障缺口", "tc": "客户溝通：次生災害保障缺口"},
            "midback": {"sc": "产品研究：巨灾模型与定价", "tc": "產品研究：巨災模型與定價"},
            "lead": {"sc": "团队简报：次生风险成主线", "tc": "團隊簡報：次生風險成主線"},
            "cross": {"sc": "巨灾债配置风险视角", "tc": "巨災債配置風險視角"}
        },
        "rolesImpact": {"front": 1, "midback": 2, "lead": 1, "cross": 1},
        "ingestedAt": NOW
    },
    {
        "id": "artemis-arbol-datacenter-moratorium-parametric-20261020",
        "publishedAt": "2026-10-20T22:00:00+08:00",
        "originalUrl": "https://www.artemis.bm/news/arbol-launches-parametric-insurance-for-gov-imposed-data-center-construction-moratoriums/",
        "sourceKey": "artemis",
        "sourceTier": "pro",
        "score": 72,
        "verifyStatus": "verified",
        "contentKind": "news",
        "clusterCount": 1,
        "boards": ["tech"],
        "themes": ["parametric", "data-centre", "regulatory-risk", "ai-infrastructure"],
        "title": {
            "sc": "Arbol 推「数据中心监管暂禁令」参数式保险　承保 AI 基建的监管停工风险",
            "tc": "Arbol 推「數據中心監管暫禁令」參數式保險　承保 AI 基建的監管停工風險"
        },
        "summary": {
            "sc": "Arbol 推出「Data Center Regulatory Moratorium Cover」，承保政府以「类别」方式暂停或叫停数据中心建设的监管风险，而非单一选址的许可被拒。触发条件为受保行动持续超过约定等待期，按公共纪录与参数式机制定額赔付，用于覆盖已投入资本与停工期间的持有成本。Arbol 称过往这类风险被视为不可保，现通过经纪提供给开发商及背后资本方。",
            "tc": "Arbol 推出「Data Center Regulatory Moratorium Cover」，承保政府以「類別」方式暫停或叫停數據中心建設的監管風險，而非單一選址的許可被拒。觸發條件為受保行動持續超過約定等待期，按公共紀錄與參數式機制定額賠付，用於覆蓋已投入資本與停工期間的持有成本。Arbol 稱過往這類風險被視為不可保，現通過經紀提供給開發商及背後資本方。"
        },
        "why": {
            "sc": "AI 基建热潮把「政策风险」变成可保标的：数据中心停工不再只是开发商的商业风险，而是可以转移给资本市场的参数式产品。对持有数据中心、物流园等另类资产的家办与高客，这是尽调清单上新的一个问题——既有的财产险与营业中断险通常不回应政府停工。",
            "tc": "AI 基建熱潮把「政策風險」變成可保標的：數據中心停工不再只是開發商的商業風險，而是可以轉移給資本市場的參數式產品。對持有數據中心、物流園等另類資產的家辦與高客，這是盡調清單上新的問題——既有的財產險與營業中斷險通常不回應政府停工。"
        },
        "source": {
            "sc": "Artemis 2026-10-20（Arbol 产品发布）",
            "tc": "Artemis 2026-10-20（Arbol 產品發布）",
            "lang": "en",
            "name": "artemis",
            "date": "2026-10-20"
        },
        "tags": {
            "sc": ["参数式保险", "数据中心", "监管风险", "AI基建", "营业中断"],
            "tc": ["參數式保險", "數據中心", "監管風險", "AI基建", "營業中斷"]
        },
        "actions": {
            "front": {"sc": "客户沟通：政策风险的保障边界", "tc": "客户溝通：政策風險的保障邊界"},
            "midback": {"sc": "产品研究：参数式触发与基差风险", "tc": "產品研究：參數式觸發與基差風險"},
            "lead": {"sc": "团队简报：AI 基建新险种", "tc": "團隊簡報：AI 基建新險種"},
            "cross": {"sc": "家办：基建资产风险尽调", "tc": "家辦：基建資產風險盡調"}
        },
        "rolesImpact": {"front": 1, "midback": 2, "lead": 1, "cross": 2},
        "ingestedAt": NOW
    },
    {
        "id": "artemis-jamaica-cat-bond-melissa-payout-20261020",
        "publishedAt": "2026-10-20T21:00:00+08:00",
        "originalUrl": "https://www.artemis.bm/news/jamaicas-parametric-cat-bond-payout-funded-electricity-restoration-chief-fiscal-economist-francis/",
        "sourceKey": "artemis",
        "sourceTier": "pro",
        "score": 71,
        "verifyStatus": "verified",
        "contentKind": "news",
        "clusterCount": 1,
        "boards": ["market"],
        "themes": ["cat-bond", "parametric", "sovereign-risk", "disaster-financing"],
        "title": {
            "sc": "牙買加：颶風 Melissa 觸發 1.5 億美元巨災債券　30 天內到賬用於恢復供電",
            "tc": "牙買加：颶風 Melissa 觸發 1.5 億美元巨災債券　30 天內到賬用於恢復供電"
        },
        "summary": {
            "sc": "牙买加财政部首席财政经济师 Terron Francis 在 ILS Bermuda 2026 表示，飓风 Melissa 触发 IBRD CAR Jamaica 2024 参数式巨灾债券全额 1.5 亿美元赔付，款项 30 天内到账，直接用于西部受影响地区恢复供电，避免政府紧急借贷或大幅调动项目预算。该国同时有 CCRIF 参数式保险与世银协助的巨灾债券，构成多层灾害风险融资结构。",
            "tc": "牙買加財政部首席財政經濟師 Terron Francis 在 ILS Bermuda 2026 表示，颶風 Melissa 觸發 IBRD CAR Jamaica 2024 參數式巨災債券全額 1.5 億美元賠付，款項 30 天內到賬，直接用於西部受影響地區恢復供電，避免政府緊急借貸或大幅調動項目預算。該國同時有 CCRIF 參數式保險與世銀協助的巨災債券，構成多層災害風險融資結構。"
        },
        "why": {
            "sc": "「参数式工具真的能救急」最干净的实证：30 天到账、用途明确、不靠紧急举债。香港正推动 ILS 与专属自保生态，这类案例可直接用于向企业客户与公共机构解释多层风险融资的价值，也提醒「快」来自结构与触发设计，不是来自保额更大。",
            "tc": "「參數式工具真的能救急」最乾淨的實證：30 天到賬、用途明確、不靠緊急舉債。香港正推動 ILS 與專屬自保生態，這類案例可直接用於向企業客户與公共機構解釋多層風險融資的價值，也提醒「快」來自結構與觸發設計，不是來自保額更大。"
        },
        "source": {
            "sc": "Artemis 2026-10-20（ILS Bermuda 2026 发言）",
            "tc": "Artemis 2026-10-20（ILS Bermuda 2026 發言）",
            "lang": "en",
            "name": "artemis",
            "date": "2026-10-20"
        },
        "tags": {
            "sc": ["巨灾债券", "参数式", "主权风险融资", "牙买加", "灾后恢复"],
            "tc": ["巨災債券", "參數式", "主權風險融資", "牙買加", "災後恢復"]
        },
        "actions": {
            "front": {"sc": "客户沟通：参数式的「快」从何而来", "tc": "客户溝通：參數式的「快」從何而來"},
            "midback": {"sc": "结构研究：多层风险融资", "tc": "結構研究：多層風險融資"},
            "lead": {"sc": "团队简报：香港 ILS 生态素材", "tc": "團隊簡報：香港 ILS 生態素材"},
            "cross": {"sc": "家办：巨灾债案例引用", "tc": "家辦：巨災債案例引用"}
        },
        "rolesImpact": {"front": 1, "midback": 2, "lead": 1, "cross": 1},
        "ingestedAt": NOW
    },
    {
        "id": "reinsurancenews-triplei-milliman-pc-2026-outlook-20261020",
        "publishedAt": "2026-10-20T21:00:00+08:00",
        "originalUrl": "https://www.reinsurancene.ws/us-insurers-forecast-to-sustain-underwriting-gains-in-2026-despite-economic-pressures-triple-i-milliman/",
        "sourceKey": "reinsurancenews",
        "sourceTier": "pro",
        "score": 70,
        "verifyStatus": "verified",
        "contentKind": "report",
        "clusterCount": 1,
        "boards": ["market"],
        "themes": ["underwriting-cycle", "combined-ratio", "us-market", "pricing"],
        "title": {
            "sc": "Triple-I／Milliman：美國產險 2026 年淨綜合成本率 94.0　2027 年增長或放緩",
            "tc": "Triple-I／Milliman：美國產險 2026 年淨綜合成本率 94.0　2027 年增長或放緩"
        },
        "summary": {
            "sc": "Triple-I 与 Milliman 预测美国产险 2026 年净综合成本率 94.0，即维持承保盈利，但 2027 年或因货币紧缩与重置成本上升而增长放缓。基础产险增长在 2026 及 2028 年料跑赢 GDP，2027 年则低于整体经济增长；2026–2028 年商业险净已赚保费增速预计比个人险高约三个百分点。",
            "tc": "Triple-I 與 Milliman 預測美國產險 2026 年淨綜合成本率 94.0，即維持承保盈利，但 2027 年或因貨幣緊縮與重置成本上升而增長放緩。基礎產險增長在 2026 及 2028 年料跑贏 GDP，2027 年則低於整體經濟增長；2026–2028 年商業險淨已賺保費增速預計比個人險高約三個百分點。"
        },
        "why": {
            "sc": "再保与直保的议价能力取决于上游是否真的赚钱。NCR 94.0 说明美国产险仍有承保利润，即「软化」有底线；同时 2027 年增长放缓的预判，是判断亚洲 1 月续保与产品加费节奏的外部坐标。",
            "tc": "再保與直保的議價能力取決於上游是否真的賺錢。NCR 94.0 說明美國產險仍有承保利潤，即「軟化」有底線；同時 2027 年增長放緩的預判，是判斷亞洲 1 月續保與產品加費節奏的外部坐標。"
        },
        "source": {
            "sc": "Reinsurance News 2026-10-20（引 Triple-I 与 Milliman 网络研讨会）",
            "tc": "Reinsurance News 2026-10-20（引 Triple-I 與 Milliman 網絡研討會）",
            "lang": "en",
            "name": "reinsurancenews",
            "date": "2026-10-20"
        },
        "tags": {
            "sc": ["承保周期", "综合成本率", "美国产险", "定价", "经济展望"],
            "tc": ["承保週期", "綜合成本率", "美國產險", "定價", "經濟展望"]
        },
        "actions": {
            "front": {"sc": "客户沟通：费率周期位置", "tc": "客户溝通：費率週期位置"},
            "midback": {"sc": "产品研究：加费空间判断", "tc": "產品研究：加費空間判斷"},
            "lead": {"sc": "团队简报：全球承保盈利图景", "tc": "團隊簡報：全球承保盈利圖景"},
            "cross": {"sc": "险企股票与债券视角", "tc": "險企股票與債券視角"}
        },
        "rolesImpact": {"front": 1, "midback": 2, "lead": 2, "cross": 1},
        "ingestedAt": NOW
    },
    {
        "id": "artemis-gam-aviv-cat-bond-scalability-20261020",
        "publishedAt": "2026-10-20T18:30:00+08:00",
        "originalUrl": "https://www.artemis.bm/news/deepening-cat-bond-market-offers-investors-liquidity-scale-and-broader-diversification-gams-aviv/",
        "sourceKey": "artemis",
        "sourceTier": "pro",
        "score": 70,
        "verifyStatus": "verified",
        "contentKind": "report",
        "clusterCount": 1,
        "boards": ["family"],
        "themes": ["cat-bond", "allocation", "diversification", "family-office"],
        "title": {
            "sc": "GAM：巨災債券指數 2002 年以來年化 7.7%、波動 3.7%　與傳統資產相關性低於 0.26",
            "tc": "GAM：巨災債券指數 2002 年以來年化 7.7%、波動 3.7%　與傳統資產相關性低於 0.26"
        },
        "summary": {
            "sc": "GAM ILS 主管 Rom Aviv 撰文指出，2002 年 2 月至 2026 年 3 月瑞士再保巨灾债券总回报指数年化回报 7.7%、年化波动 3.7%；同期美国高收益债为 7.1%／8.8%，标普 500 为 9.6%／14.8%。该指数与主要资产类别相关系数维持 0.26 以下，自成立以来仅 2022 年录得负回报。他认为市场深化带来规模、流动性与分散度提升，正反过来强化配置理由。",
            "tc": "GAM ILS 主管 Rom Aviv 撰文指出，2002 年 2 月至 2026 年 3 月瑞士再保巨災債券總回報指數年化回報 7.7%、年化波動 3.7%；同期美國高收益債為 7.1%／8.8%，標普 500 為 9.6%／14.8%。該指數與主要資產類別相關係數維持 0.26 以下，自成立以來僅 2022 年錄得負回報。他認為市場深化帶來規模、流動性與分散度提升，正反過來強化配置理由。"
        },
        "why": {
            "sc": "家办谈另类配置时最缺的是「可比的长期数字」。这组回报／波动／相关性可直接放进配置讨论，但要同时讲清代价：巨灾债的损失来自保险事件而非利率，2022 年也曾录负回报，且流动性在事件后可能收紧。",
            "tc": "家辦談另類配置時最缺的是「可比的長期數字」。這組回報／波動／相關性可直接放進配置討論，但要同時講清代價：巨災債的損失來自保險事件而非利率，2022 年也曾錄負回報，且流動性在事件後可能收緊。"
        },
        "source": {
            "sc": "Artemis 2026-10-20（引 GAM ILS 主管 Rom Aviv 文章）",
            "tc": "Artemis 2026-10-20（引 GAM ILS 主管 Rom Aviv 文章）",
            "lang": "en",
            "name": "artemis",
            "date": "2026-10-20"
        },
        "tags": {
            "sc": ["巨灾债券", "资产配置", "相关性", "家办", "另类投资"],
            "tc": ["巨災債券", "資產配置", "相關性", "家辦", "另類投資"]
        },
        "actions": {
            "front": {"sc": "—", "tc": "—"},
            "midback": {"sc": "产品研究：另类资产属性", "tc": "產品研究：另類資產屬性"},
            "lead": {"sc": "团队简报：ILS 长期回报数据", "tc": "團隊簡報：ILS 長期回報數據"},
            "cross": {"sc": "家办：ILS 配置论据与风险", "tc": "家辦：ILS 配置論據與風險"}
        },
        "rolesImpact": {"front": 0, "midback": 1, "lead": 1, "cross": 3},
        "ingestedAt": NOW
    },
    {
        "id": "insuranceasianews-mg-geraghty-phil-steel-20261020",
        "publishedAt": "2026-10-20T18:30:00+08:00",
        "originalUrl": "https://insuranceasianews.com/mg-geraghty-hires-howdens-phil-steel-as-head-of-business-development/",
        "sourceKey": "insuranceasianews",
        "sourceTier": "media",
        "score": 62,
        "verifyStatus": "pending",
        "contentKind": "news",
        "clusterCount": 1,
        "boards": ["insurer"],
        "themes": ["brokers", "hong-kong", "people-move", "distribution"],
        "title": {
            "sc": "香港經紀 MG Geraghty 挖角 Howden 香港 Phil Steel 任業務發展主管",
            "tc": "香港經紀 MG Geraghty 挖角 Howden 香港 Phil Steel 任業務發展主管"
        },
        "summary": {
            "sc": "香港保险经纪 MG Geraghty Insurance Brokers 聘请原 Howden 香港副董事 Phil Bautista Steel 出任业务发展主管。报道指他在香港累积逾十年经验，负责推动公司经纪业务拓展。（原文有付费墙，仅据首段。）",
            "tc": "香港保險經紀 MG Geraghty Insurance Brokers 聘請原 Howden 香港副董事 Phil Bautista Steel 出任業務發展主管。報道指他在香港累積逾十年經驗，負責推動公司經紀業務拓展。（原文有付費牆，僅據首段。）"
        },
        "why": {
            "sc": "本地经纪之间的挖角，反映商业险与专险中介竞争仍在升温。对前线而言，值得留意的是「同一批客户被不同经纪以不同结构接洽」的情况会增加，方案比较与客户预期管理要更细致。",
            "tc": "本地經紀之間的挖角，反映商業險與專險中介競爭仍在升溫。對前線而言，值得留意的是「同一批客户被不同經紀以不同結構接洽」的情況會增加，方案比較與客户預期管理要更細緻。"
        },
        "source": {
            "sc": "InsuranceAsia News 2026-10-20（公司确认）",
            "tc": "InsuranceAsia News 2026-10-20（公司確認）",
            "lang": "en",
            "name": "insuranceasianews",
            "date": "2026-10-20"
        },
        "tags": {
            "sc": ["保险经纪", "香港", "人事变动", "商业险", "分销"],
            "tc": ["保險經紀", "香港", "人事變動", "商業險", "分銷"]
        },
        "actions": {
            "front": {"sc": "客户沟通：多经纪接洽下的方案比较", "tc": "客户溝通：多經紀接洽下的方案比較"},
            "midback": {"sc": "竞争跟踪：本地经纪动向", "tc": "競爭跟蹤：本地經紀動向"},
            "lead": {"sc": "团队简报：中介竞争格局", "tc": "團隊簡報：中介競爭格局"},
            "cross": {"sc": "—", "tc": "—"}
        },
        "rolesImpact": {"front": 1, "midback": 1, "lead": 1, "cross": 0},
        "ingestedAt": NOW
    },
    {
        "id": "reinsurancenews-morningstar-dbrs-france-srcc-20261020",
        "publishedAt": "2026-10-20T19:36:00+08:00",
        "originalUrl": "https://www.reinsurancene.ws/unrest-in-france-underlines-cat-like-risks-of-riots-and-civil-commotion-morningstar-dbrs/",
        "sourceKey": "reinsurancenews",
        "sourceTier": "pro",
        "score": 70,
        "verifyStatus": "verified",
        "contentKind": "report",
        "clusterCount": 1,
        "boards": ["product"],
        "themes": ["srcc", "accumulation-risk", "commercial-property", "pricing"],
        "title": {
            "sc": "Morningstar DBRS：法國騷亂損失料低於 12 億歐元　但 SRCC 已屬累積風險須獨立定價",
            "tc": "Morningstar DBRS：法國騷亂損失料低於 12 億歐元　但 SRCC 已屬累積風險須獨立定價"
        },
        "summary": {
            "sc": "Morningstar DBRS 指法国最新骚乱的保险损失预计低于 12 亿欧元（假设暴力不再扩大），但真正的问题是商业财产、汽车、政府财产与营业中断保单之间的「相关性累积」。该机构认为骚乱与民众骚扰（SRCC）须视为独立累积风险，需要专门定价、限额与再保安排；美国、智利、南非曾出现单一事件超过 20 亿美元损失。法国待推的国家支援机制有望降低极端损失分配的不确定性。",
            "tc": "Morningstar DBRS 指法國最新騷亂的保險損失預計低於 12 億歐元（假設暴力不再擴大），但真正的問題是商業財產、汽車、政府財產與營業中斷保單之間的「相關性累積」。該機構認為騷亂與民眾騷擾（SRCC）須視為獨立累積風險，需要專門定價、限額與再保安排；美國、智利、南非曾出現單一事件超過 20 億美元損失。法國待推的國家支援機制有望降低極端損失分配的不確定性。"
        },
        "why": {
            "sc": "SRCC 长期被当成财产险的「附带风险」，现在评级机构明确要求独立定价与限额。做商业险与财产险方案时，应主动检视 SRCC 是否被除外、限额多少、有无独立免赔额——这是最容易被忽略、却最容易在事件后产生争议的条款。",
            "tc": "SRCC 長期被當成財產險的「附帶風險」，現在評級機構明確要求獨立定價與限額。做商業險與財產險方案時，應主動檢視 SRCC 是否被除外、限額多少、有無獨立免賠額——這是最容易被忽略、卻最容易在事件後產生爭議的條款。"
        },
        "source": {
            "sc": "Reinsurance News 2026-10-20（引 Morningstar DBRS 声明）",
            "tc": "Reinsurance News 2026-10-20（引 Morningstar DBRS 聲明）",
            "lang": "en",
            "name": "reinsurancenews",
            "date": "2026-10-20"
        },
        "tags": {
            "sc": ["SRCC", "累积风险", "商业财产险", "营业中断", "定价"],
            "tc": ["SRCC", "累積風險", "商業財產險", "營業中斷", "定價"]
        },
        "actions": {
            "front": {"sc": "客户沟通：骚乱风险是否受保", "tc": "客户溝通：騷亂風險是否受保"},
            "midback": {"sc": "条款检视：SRCC 除外与限额", "tc": "條款檢視：SRCC 除外與限額"},
            "lead": {"sc": "团队培训：累积风险识别", "tc": "團隊培訓：累積風險識別"},
            "cross": {"sc": "海外资产风险提示", "tc": "海外資產風險提示"}
        },
        "rolesImpact": {"front": 2, "midback": 2, "lead": 1, "cross": 1},
        "ingestedAt": NOW
    },
    {
        "id": "insuranceasianews-cybercube-sompo-japan-20261020",
        "publishedAt": "2026-10-20T20:01:00+08:00",
        "originalUrl": "https://insuranceasianews.com/cybercube-adds-sompo-japan-to-growing-apac-client-base/",
        "sourceKey": "insuranceasianews",
        "sourceTier": "media",
        "score": 62,
        "verifyStatus": "pending",
        "contentKind": "news",
        "clusterCount": 1,
        "boards": ["tech"],
        "themes": ["cyber", "cat-modelling", "apac", "underwriting"],
        "title": {
            "sc": "CyberCube 新增日本損保為亞太客戶　續擴網絡風險分析版圖",
            "tc": "CyberCube 新增日本損保為亞太客戶　續擴網絡風險分析版圖"
        },
        "summary": {
            "sc": "网络风险分析商 CyberCube 宣布新增 Sompo Japan（日本損保）为亚洲客户，作为其区域扩张的一部分。该公司为保险公司提供网络风险累积建模与核保分析工具，并把亚太视为未来数年的增长重心。（原文有付费墙，仅据首段与新闻稿摘要。）",
            "tc": "網絡風險分析商 CyberCube 宣布新增 Sompo Japan（日本損保）為亞洲客户，作為其區域擴張的一部分。該公司為保險公司提供網絡風險累積建模與核保分析工具，並把亞太視為未來數年的增長重心。（原文有付費牆，僅據首段與新聞稿摘要。）"
        },
        "why": {
            "sc": "网络险的核保越来越依赖累积建模——单一云服务商或软件漏洞可同时牵动成千上万张保单。亚洲大型险企陆续接入分析平台，意味企业客户在续保时会被要求提供更细的IT与供应链资料，提前准备可缩短核保周期。",
            "tc": "網絡險的核保越來越依賴累積建模——單一雲服務商或軟件漏洞可同時牽動成千上萬張保單。亞洲大型險企陸續接入分析平台，意味企業客户在續保時會被要求提供更細的IT與供應鏈資料，提前準備可縮短核保週期。"
        },
        "source": {
            "sc": "InsuranceAsia News 2026-10-20（CyberCube 新闻稿）",
            "tc": "InsuranceAsia News 2026-10-20（CyberCube 新聞稿）",
            "lang": "en",
            "name": "insuranceasianews",
            "date": "2026-10-20"
        },
        "tags": {
            "sc": ["网络风险", "累积建模", "亚太", "核保", "CyberCube"],
            "tc": ["網絡風險", "累積建模", "亞太", "核保", "CyberCube"]
        },
        "actions": {
            "front": {"sc": "客户沟通：网络险核保资料", "tc": "客户溝通：網絡險核保資料"},
            "midback": {"sc": "产品研究：网络累积风险", "tc": "產品研究：網絡累積風險"},
            "lead": {"sc": "团队简报：亚太网络险趋势", "tc": "團隊簡報：亞太網絡險趨勢"},
            "cross": {"sc": "企业客户IT尽调清单", "tc": "企業客户IT盡調清單"}
        },
        "rolesImpact": {"front": 1, "midback": 2, "lead": 1, "cross": 1},
        "ingestedAt": NOW
    },
    {
        "id": "ia-enforcement-jian-yongqin-suspension-20261016",
        "publishedAt": "2026-10-16",
        "originalUrl": "https://www.ia.org.hk/en/enforcement/enforcement_news/news.html",
        "sourceKey": "ia",
        "sourceTier": "official",
        "score": 90,
        "verifyStatus": "verified",
        "contentKind": "news",
        "clusterCount": 1,
        "boards": ["reg"],
        "themes": ["enforcement", "witness-signature", "internal-controls", "conduct"],
        "title": {
            "sc": "保監局停牌三個月：中介人未親身見證客戶在港簽署　自行簽名確認「已見證」",
            "tc": "保監局停牌三個月：中介人未親身見證客户在港簽署　自行簽名確認「已見證」"
        },
        "summary": {
            "sc": "保监局 10 月 16 日公布，持牌保险中介人 Jian Yongqin（IH4992）被停牌三个月。案情指其所属公司内控要求她亲身在香港见证客户签署声明书（确认客户已购买银行本票缴付保费），她将表格电邮予两名不在港的客户，客户签署后寄回，再由她签名确认「已见证」，令保险公司误信客户在港亲签。保监局指其违反「适当人选」准则。",
            "tc": "保監局 10 月 16 日公布，持牌保險中介人 Jian Yongqin（IH4992）被停牌三個月。案情指其所屬公司內控要求她親身在香港見證客户簽署聲明書（確認客户已購買銀行本票繳付保費），她將表格電郵予兩名不在港的客户，客户簽署後寄回，再由她簽名確認「已見證」，令保險公司誤信客户在港親簽。保監局指其違反「適當人選」準則。"
        },
        "why": {
            "sc": "这是「见证签署」红线最直接的反面案例：客户不在港、表格邮寄、代理代确认见证，三个动作全部踩线，结果停牌三个月并留下公开纪律纪录。比抽象条文更适合做前线合规培训的第一张投影片——尤其跨境客户「先签后到」的灰色做法。",
            "tc": "這是「見證簽署」紅線最直接的反面案例：客户不在港、表格郵寄、代理代確認見證，三個動作全部踩線，結果停牌三個月並留下公開紀律紀錄。比抽象條文更適合做前線合規培訓的第一張投影片——尤其跨境客户「先簽後到」的灰色做法。"
        },
        "source": {
            "sc": "香港保监局（IA）执法新闻 2026-10-16（列表页；个案无独立文章链接）",
            "tc": "香港保監局（IA）執法新聞 2026-10-16（列表頁；個案無獨立文章連結）",
            "lang": "en",
            "name": "ia",
            "date": "2026-10-16"
        },
        "tags": {
            "sc": ["保监局", "停牌", "见证签署", "内部控制", "适当人选"],
            "tc": ["保監局", "停牌", "見證簽署", "內部控制", "適當人選"]
        },
        "actions": {
            "front": {"sc": "合规红线：见证签署必须亲身在港", "tc": "合規紅線：見證簽署必須親身在港"},
            "midback": {"sc": "流程检视：声明书签署与回传", "tc": "流程檢視：聲明書簽署與回傳"},
            "lead": {"sc": "团队培训：本案作为案例教材", "tc": "團隊培訓：本案作為案例教材"},
            "cross": {"sc": "跨境客户安排风险提示", "tc": "跨境客户安排風險提示"}
        },
        "rolesImpact": {"front": 3, "midback": 2, "lead": 2, "cross": 1},
        "ingestedAt": NOW
    },
]

added = []
for it in new_items:
    key = it['originalUrl'].split('?')[0].rstrip('/')
    if key in existing:
        print('skip dup:', it['id'])
        continue
    items.insert(0, it)
    existing.add(key)
    added.append(it['id'])

items.sort(key=lambda x: x.get('publishedAt') or '', reverse=True)

meta = d['meta']
meta['generatedAt'] = NOW
meta['itemCount'] = len(items)
meta['windowNote'] = {"sc": f"本库{len(items)}条。", "tc": f"本庫{len(items)}條。"}

json.dump(d, open(PATH, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('added', len(added), 'total', len(items))
for a in added:
    print('  +', a)
