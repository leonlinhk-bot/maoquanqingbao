# -*- coding: utf-8 -*-
"""2026-10-20 18:08 增量：10 条（再保/MGA/另类资产/亚洲监管）"""
import json

PATH = '/Users/leonliang/maoquanqingbao/data/live-items.json'
NOW = '2026-10-20T18:08:00+08:00'

d = json.load(open(PATH, encoding='utf-8'))
items = d['items']
existing = {i.get('originalUrl', '').split('?')[0].rstrip('/') for i in items}

new_items = [
    {
        "id": "reinsurancenews-nms-ascendra-mga-20261020",
        "publishedAt": "2026-10-20T18:00:00+08:00",
        "originalUrl": "https://www.reinsurancene.ws/nms-capital-launches-specialty-mga-ascendra/",
        "sourceKey": "reinsurancenews",
        "sourceTier": "pro",
        "score": 70,
        "verifyStatus": "verified",
        "contentKind": "news",
        "clusterCount": 1,
        "boards": ["market"],
        "themes": ["mga", "private-capital", "underwriting", "specialty"],
        "title": {
            "sc": "NMS Capital 设专险 MGA「Ascendra」　PE 以平台化方式承接承保能力",
            "tc": "NMS Capital 設專險 MGA「Ascendra」　PE 以平台化方式承接承保能力"
        },
        "summary": {
            "sc": "私募股权公司 NMS Capital 推出 Ascendra Specialty，定位技术驱动的全服务 MGA 与计划管理人，代承保伙伴提供核保专业、授权承保（DUA）与理赔管理。首阶段聚焦专业责任、工伤、运输、网络、建筑、财产、环境及中小企专险约八条业务线，并伙拍 Moonshot Foundry 使用其技术平台与承保人／零售代理网络。NMS 创办人兼行政总裁 Trevor Saliba 称，此举是其保险板块「专属平台部署资本」策略的延伸。",
            "tc": "私募股權公司 NMS Capital 推出 Ascendra Specialty，定位技術驅動的全服務 MGA 與計劃管理人，代承保夥伴提供核保專業、授權承保（DUA）與理賠管理。首階段聚焦專業責任、工傷、運輸、網絡、建築、財產、環境及中小企專險約八條業務線，並夥拍 Moonshot Foundry 使用其技術平台與承保人／零售代理網絡。NMS 創辦人兼行政總裁 Trevor Saliba 稱，此舉是其保險板塊「專屬平台部署資本」策略的延伸。"
        },
        "why": {
            "sc": "MGA 是亚洲专险增长最快的承保组织形式：资本方出钱，MGA 出核保与分销。此类平台入场意味着网络、环境、中小企等细分险种供给增加；前端为客户找非标保障时会更多遇到 MGA 承保的保单，须看清背后承保人（carrier）是谁、授权范围与理赔由谁处理。",
            "tc": "MGA 是亞洲專險增長最快的承保組織形式：資本方出錢，MGA 出核保與分銷。此類平台入場意味網絡、環境、中小企等細分險種供給增加；前端為客户找非標保障時會更多遇到 MGA 承保的保單，須看清背後承保人（carrier）是誰、授權範圍與理賠由誰處理。"
        },
        "source": {
            "sc": "Reinsurance News 2026-10-20（NMS Capital 公告）",
            "tc": "Reinsurance News 2026-10-20（NMS Capital 公告）",
            "lang": "en",
            "name": "reinsurancenews",
            "date": "2026-10-20"
        },
        "tags": {
            "sc": ["MGA", "私募股权", "专险", "授权承保", "承保能力"],
            "tc": ["MGA", "私募股權", "專險", "授權承保", "承保能力"]
        },
        "actions": {
            "front": {"sc": "客户解释：MGA 保单背后的承保人", "tc": "客户解釋：MGA 保單背後的承保人"},
            "midback": {"sc": "产品尽调：授权承保与理赔主体", "tc": "產品盡調：授權承保與理賠主體"},
            "lead": {"sc": "团队简报：MGA 与细分险种供给", "tc": "團隊簡報：MGA 與細分險種供給"},
            "cross": {"sc": "家办：专险平台投资视角", "tc": "家辦：專險平台投資視角"}
        },
        "rolesImpact": {"front": 2, "midback": 2, "lead": 1, "cross": 1},
        "ingestedAt": NOW
    },
    {
        "id": "reinsurancenews-gallagher-re-deschars-cedent-20261020",
        "publishedAt": "2026-10-20T16:00:00+08:00",
        "originalUrl": "https://www.reinsurancene.ws/reinsurers-must-focus-on-cedent-needs-to-attract-more-inflow-gallagher-res-deschars/",
        "sourceKey": "reinsurancenews",
        "sourceTier": "pro",
        "score": 70,
        "verifyStatus": "verified",
        "contentKind": "news",
        "clusterCount": 1,
        "boards": ["market"],
        "themes": ["reinsurance", "pricing", "capacity", "client-engagement"],
        "title": {
            "sc": "Gallagher Re：软市场下再保要「听得懂客户」　保户应重排自留与保障广度而非只追降价",
            "tc": "Gallagher Re：軟市場下再保要「聽得懂客户」　保户應重排自留與保障廣度而非只追降價"
        },
        "summary": {
            "sc": "Gallagher Re 欧洲、中东及非洲区主席 Ditte Deschars 在巴登巴登再保会议前受访称，软市场中资本供给充裕，但真正能吸引保户上门的是「愿意听、能找到解方」的资本方。她提醒保户不要只按 KPI 追逐短期折扣，应借资本充裕之机重设自留额、保障广度以及条款与条件，为下一轮周期留出韧性；只追降价会错过这次策略窗口。",
            "tc": "Gallagher Re 歐洲、中東及非洲區主席 Ditte Deschars 在巴登巴登再保會議前受訪稱，軟市場中資本供給充裕，但真正能吸引保户上門的是「願意聽、能找到解方」的資本方。她提醒保户不要只按 KPI 追逐短期折扣，應借資本充裕之機重設自留額、保障廣度以及條款與條件，為下一輪週期留出韌性；只追降價會錯過這次策略窗口。"
        },
        "why": {
            "sc": "续保谈判最容易被忽略的是结构与自留，而不是价格。这段话可作为向企业客户与高客解释「为什么现在适合重做保障结构」的外部观点引用，也能用于团队培训，纠正只比价的习惯。",
            "tc": "續保談判最容易被忽略的是結構與自留，而不是價格。這段話可作為向企業客户與高客解釋「為什麼現在適合重做保障結構」的外部觀點引用，也能用於團隊培訓，糾正只比價的習慣。"
        },
        "source": {
            "sc": "Reinsurance News 2026-10-20（专访 Gallagher Re EMEA 主席）",
            "tc": "Reinsurance News 2026-10-20（專訪 Gallagher Re EMEA 主席）",
            "lang": "en",
            "name": "reinsurancenews",
            "date": "2026-10-20"
        },
        "tags": {
            "sc": ["再保险", "软市场", "自留额", "保障条款", "巴登巴登"],
            "tc": ["再保險", "軟市場", "自留額", "保障條款", "巴登巴登"]
        },
        "actions": {
            "front": {"sc": "客户沟通：现在为何适合重做结构", "tc": "客户溝通：現在為何適合重做結構"},
            "midback": {"sc": "续保策略：自留额与保障广度检视", "tc": "續保策略：自留額與保障廣度檢視"},
            "lead": {"sc": "团队培训：不要只比价", "tc": "團隊培訓：不要只比價"},
            "cross": {"sc": "企业客户再保采购顾问话术", "tc": "企業客户再保採購顧問話術"}
        },
        "rolesImpact": {"front": 2, "midback": 2, "lead": 2, "cross": 1},
        "ingestedAt": NOW
    },
    {
        "id": "reinsurancenews-moodys-german-insurers-private-credit-20261020",
        "publishedAt": "2026-10-20T14:00:00+08:00",
        "originalUrl": "https://www.reinsurancene.ws/moodys-forecasts-further-growth-in-german-insurers-private-credit-investments/",
        "sourceKey": "reinsurancenews",
        "sourceTier": "pro",
        "score": 71,
        "verifyStatus": "verified",
        "contentKind": "report",
        "clusterCount": 1,
        "boards": ["market"],
        "themes": ["investment", "private-credit", "asset-liability", "regulation"],
        "title": {
            "sc": "穆迪：德国险企私募信贷投资将续增　非流动资产占投资资产 19.4%",
            "tc": "穆迪：德國險企私募信貸投資將續增　非流動資產佔投資資產 19.4%"
        },
        "summary": {
            "sc": "穆迪评级预计德国险企会继续加大私募信贷配置，以争取收益、分散组合并对接长期保单负债；代价是估值、流动性与风险管理难度上升，可能引来更严监管审视，但不预期信用状况实质转弱。按 EIOPA 数据，2025 年德国险企非流动资产占投资资产 19.4%（2019 年 15.8%），寿险由 19% 升至 25.1%；2024 年底私募信贷约占总投资的 9.3%，高于欧洲保险业平均 7.5%，德法荷三国占欧洲私募信贷敞口约 72%。",
            "tc": "穆迪評級預計德國險企會繼續加大私募信貸配置，以爭取收益、分散組合並對接長期保單負債；代價是估值、流動性與風險管理難度上升，可能引來更嚴監管審視，但不預期信用狀況實質轉弱。按 EIOPA 數據，2025 年德國險企非流動資產佔投資資產 19.4%（2019 年 15.8%），壽險由 19% 升至 25.1%；2024 年底私募信貸約佔總投資的 9.3%，高於歐洲保險業平均 7.5%，德法荷三國佔歐洲私募信貸敞口約 72%。"
        },
        "why": {
            "sc": "储蓄型／分红型产品的收益来源越来越依赖另类资产。这条给出可核对的量化参照（19.4%、9.3%、欧洲平均 7.5%），谈分红不确定性与流动性风险时，比空讲「投资环境复杂」更有据。",
            "tc": "儲蓄型／分紅型產品的收益來源越來越依賴另類資產。這條給出可核對的量化參照（19.4%、9.3%、歐洲平均 7.5%），談分紅不確定性與流動性風險時，比空講「投資環境複雜」更有據。"
        },
        "source": {
            "sc": "Reinsurance News 2026-10-20（引穆迪评级报告与 EIOPA 数据）",
            "tc": "Reinsurance News 2026-10-20（引穆迪評級報告與 EIOPA 數據）",
            "lang": "en",
            "name": "reinsurancenews",
            "date": "2026-10-20"
        },
        "tags": {
            "sc": ["私募信贷", "另类资产", "资产负債管理", "穆迪", "德国"],
            "tc": ["私募信貸", "另類資產", "資產負債管理", "穆迪", "德國"]
        },
        "actions": {
            "front": {"sc": "客户沟通：分红不确定性与资产来源", "tc": "客户溝通：分紅不確定性與資產來源"},
            "midback": {"sc": "产品尽调：另类资产占比与流动性", "tc": "產品盡調：另類資產佔比與流動性"},
            "lead": {"sc": "团队简报：险企资产端趋势", "tc": "團隊簡報：險企資產端趨勢"},
            "cross": {"sc": "家办：另类信贷配置参照", "tc": "家辦：另類信貸配置參照"}
        },
        "rolesImpact": {"front": 2, "midback": 2, "lead": 1, "cross": 2},
        "ingestedAt": NOW
    },
    {
        "id": "artemis-ambest-casualty-sidecar-tail-risk-20261020",
        "publishedAt": "2026-10-20T15:00:00+08:00",
        "originalUrl": "https://www.artemis.bm/news/clear-exit-terms-and-liquid-collateral-key-to-lowering-casualty-sidecar-tail-risk-charges-am-best/",
        "sourceKey": "artemis",
        "sourceTier": "pro",
        "score": 72,
        "verifyStatus": "verified",
        "contentKind": "report",
        "clusterCount": 1,
        "boards": ["market"],
        "themes": ["sidecar", "ils", "casualty", "capital"],
        "title": {
            "sc": "AM Best：责任险 sidecar 的退出条款与抵押品质量决定尾部风险资本计提",
            "tc": "AM Best：責任險 sidecar 的退出條款與抵押品質量決定尾部風險資本計提"
        },
        "summary": {
            "sc": "AM Best 指，责任险（casualty）sidecar 要降低发起人的尾部风险资本占用，关键在清晰退出机制、高质量抵押品与透明风险转移；所谓尾部风险是 sidecar 资本不足时回落到发起人的剩余敞口。市场退出期已收敛至约七年，因准备金需先「陈化」估值才可信。可用工具包括 Enstar 的远期退出期权（FEO，首用于 Fractal Re）、约定式转让（Scaur Hill Re 第 7 年可选、第 10 年强制退出）、LPT、ADC 与二级转让；QBE Re 的 George Street Re 则把遗产管理机构 Compre 直接纳入投资人名单。",
            "tc": "AM Best 指，責任險（casualty）sidecar 要降低發起人的尾部風險資本佔用，關鍵在清晰退出機制、高質量抵押品與透明風險轉移；所謂尾部風險是 sidecar 資本不足時回落到發起人的剩餘敞口。市場退出期已收斂至約七年，因準備金需先「陳化」估值才可信。可用工具包括 Enstar 的遠期退出期權（FEO，首用於 Fractal Re）、約定式轉讓（Scaur Hill Re 第 7 年可選、第 10 年強制退出）、LPT、ADC 與二級轉讓；QBE Re 的 George Street Re 則把遺產管理機構 Compre 直接納入投資人名單。"
        },
        "why": {
            "sc": "香港今年落地首宗 sidecar，市场正讨论引入 PCC 制度。这条给出评级机构的视角：sidecar 不是「把风险转出去就完事」，退出条款与抵押品质量决定资本效率与残留风险——与家办、高客谈保险连结工具与另类资本时，这是必须讲清的边界。",
            "tc": "香港今年落地首宗 sidecar，市場正討論引入 PCC 制度。這條給出評級機構的視角：sidecar 不是「把風險轉出去就完事」，退出條款與抵押品質量決定資本效率與殘留風險——與家辦、高客談保險連結工具與另類資本時，這是必須講清的邊界。"
        },
        "source": {
            "sc": "Artemis 2026-10-20（引 AM Best 报告）",
            "tc": "Artemis 2026-10-20（引 AM Best 報告）",
            "lang": "en",
            "name": "artemis",
            "date": "2026-10-20"
        },
        "tags": {
            "sc": ["sidecar", "责任险", "尾部风险", "抵押品", "AM Best"],
            "tc": ["sidecar", "責任險", "尾部風險", "抵押品", "AM Best"]
        },
        "actions": {
            "front": {"sc": "客户沟通：另类资本工具的边界", "tc": "客户溝通：另類資本工具的邊界"},
            "midback": {"sc": "结构尽调：退出条款与抵押品", "tc": "結構盡調：退出條款與抵押品"},
            "lead": {"sc": "团队简报：香港 sidecar 与 PCC", "tc": "團隊簡報：香港 sidecar 與 PCC"},
            "cross": {"sc": "家办：保险连结工具配置", "tc": "家辦：保險連結工具配置"}
        },
        "rolesImpact": {"front": 1, "midback": 2, "lead": 2, "cross": 2},
        "ingestedAt": NOW
    },
    {
        "id": "insuranceasianews-arpc-cyclone-pool-premiums-20261020",
        "publishedAt": "2026-10-20T16:06:00+08:00",
        "originalUrl": "https://insuranceasianews.com/australias-cyclone-pool-cuts-up-to-37-of-home-insurance-premiums-in-high-risk-areas/",
        "sourceKey": "insuranceasianews",
        "sourceTier": "media",
        "score": 66,
        "verifyStatus": "verified",
        "contentKind": "news",
        "clusterCount": 1,
        "boards": ["market"],
        "themes": ["catastrophe", "protection-gap", "pricing", "australia"],
        "title": {
            "sc": "澳洲再保险池公司：加入气旋池后中高风险区家财险报价低 14%–37%",
            "tc": "澳洲再保險池公司：加入氣旋池後中高風險區家財險報價低 14%–37%"
        },
        "summary": {
            "sc": "澳洲再保险池公司（ARPC）表示，中至高风险气旋风险保单的平均家财险报价，仍比保险公司加入气旋池之前低 14% 至 37%，反映公营再保池对极端天气高风险区的保费缓减效果可持续。",
            "tc": "澳洲再保險池公司（ARPC）表示，中至高風險氣旋風險保單的平均家財險報價，仍比保險公司加入氣旋池之前低 14% 至 37%，反映公營再保池對極端天氣高風險區的保費緩減效果可持續。"
        },
        "why": {
            "sc": "这是「公营巨灾池能否压低终端保费」少见的官方量化说法，可与香港／大湾区巨灾保障缺口、保险相连证券的讨论对照：池子解决的是「可保性」，未必同时压低长期价格；判断政策成效时要分开看这两个目标。",
            "tc": "這是「公營巨災池能否壓低終端保費」少見的官方量化說法，可與香港／大灣區巨災保障缺口、保險相連證券的討論對照：池子解決的是「可保性」，未必同時壓低長期價格；判斷政策成效時要分開看這兩個目標。"
        },
        "source": {
            "sc": "InsuranceAsia News 2026-10-20（引 ARPC 数据）",
            "tc": "InsuranceAsia News 2026-10-20（引 ARPC 數據）",
            "lang": "en",
            "name": "insuranceasianews",
            "date": "2026-10-20"
        },
        "tags": {
            "sc": ["巨灾池", "气旋", "保障缺口", "家庭财产险", "澳洲"],
            "tc": ["巨災池", "氣旋", "保障缺口", "家庭財產險", "澳洲"]
        },
        "actions": {
            "front": {"sc": "客户沟通：巨灾保障与可保性", "tc": "客户溝通：巨災保障與可保性"},
            "midback": {"sc": "产品研究：公营池与商保分工", "tc": "產品研究：公營池與商保分工"},
            "lead": {"sc": "团队简报：巨灾池政策成效", "tc": "團隊簡報：巨災池政策成效"},
            "cross": {"sc": "大湾区巨灾保障议题素材", "tc": "大灣區巨災保障議題素材"}
        },
        "rolesImpact": {"front": 1, "midback": 2, "lead": 1, "cross": 1},
        "ingestedAt": NOW
    },
    {
        "id": "insuranceasianews-howden-re-apac-softening-souter-20261020",
        "publishedAt": "2026-10-20T07:30:00+08:00",
        "originalUrl": "https://insuranceasianews.com/a-lot-of-hunger-to-grow-strong-reinsurer-results-drive-further-apac-softening-howden-res-souter-says/",
        "sourceKey": "insuranceasianews",
        "sourceTier": "media",
        "score": 66,
        "verifyStatus": "verified",
        "contentKind": "news",
        "clusterCount": 1,
        "boards": ["market"],
        "themes": ["reinsurance", "pricing", "asia-pacific", "renewals"],
        "title": {
            "sc": "Howden Re：资本充裕叠加业绩强劲　亚太再保 1 月续保料进一步软化",
            "tc": "Howden Re：資本充裕疊加業績強勁　亞太再保 1 月續保料進一步軟化"
        },
        "summary": {
            "sc": "Howden Re 的 Andy Souter 表示，资本供给充裕加上再保人留存收益强劲，将推动亚太再保市场在 1 月 1 日续保进一步软化，再保人面临改善条款与条件的压力；用其说法，市场存在「很大的增长饥渴」。",
            "tc": "Howden Re 的 Andy Souter 表示，資本供給充裕加上再保人留存收益強勁，將推動亞太再保市場在 1 月 1 日續保進一步軟化，再保人面臨改善條款與條件的壓力；用其說法，市場存在「很大的增長飢渴」。"
        },
        "why": {
            "sc": "1 月 1 日是亚洲再保续保主场，这条与今日 Gallagher Re 的「重排结构」说法互为印证，可用来判断 2027 年条款与费率基调：上游软化会减轻产品加费压力，但不代表保证利益或分红会回升，两者要分开讲。",
            "tc": "1 月 1 日是亞洲再保續保主場，這條與今日 Gallagher Re 的「重排結構」說法互為印證，可用來判斷 2027 年條款與費率基調：上游軟化會減輕產品加費壓力，但不代表保證利益或分紅會回升，兩者要分開講。"
        },
        "source": {
            "sc": "InsuranceAsia News 2026-10-20（Howden Re 访谈）",
            "tc": "InsuranceAsia News 2026-10-20（Howden Re 訪談）",
            "lang": "en",
            "name": "insuranceasianews",
            "date": "2026-10-20"
        },
        "tags": {
            "sc": ["再保险", "亚太", "1月续保", "软市场", "Howden"],
            "tc": ["再保險", "亞太", "1月續保", "軟市場", "Howden"]
        },
        "actions": {
            "front": {"sc": "客户沟通：2027 年费率与条款基调", "tc": "客户溝通：2027 年費率與條款基調"},
            "midback": {"sc": "产品与再保成本趋势跟踪", "tc": "產品與再保成本趨勢跟蹤"},
            "lead": {"sc": "团队简报：亚太续保周期", "tc": "團隊簡報：亞太續保週期"},
            "cross": {"sc": "企业风险成本展望素材", "tc": "企業風險成本展望素材"}
        },
        "rolesImpact": {"front": 1, "midback": 2, "lead": 2, "cross": 1},
        "ingestedAt": NOW
    },
    {
        "id": "insuranceasia-indonesia-nonlife-profit-squeeze-20261020",
        "publishedAt": "2026-10-20T05:00:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/in-focus/indonesia-insurers-face-profit-squeeze-despite-stable-outlook",
        "sourceKey": "insuranceasia",
        "sourceTier": "media",
        "score": 65,
        "verifyStatus": "verified",
        "contentKind": "report",
        "clusterCount": 1,
        "boards": ["market"],
        "themes": ["indonesia", "non-life", "medical-inflation", "capital-requirement"],
        "title": {
            "sc": "AM Best：印尼非寿险展望稳定　医疗通胀与竞争压缩利润、资本新规首阶段年底生效",
            "tc": "AM Best：印尼非壽險展望穩定　醫療通脹與競爭壓縮利潤、資本新規首階段年底生效"
        },
        "summary": {
            "sc": "AM Best 10 月 8 日报告维持印尼非寿险「稳定」展望：保费增长预期仍强，但理赔通胀与竞争持续压制盈利。IMF 预测印尼实质 GDP 增速由 2025 年 5.1% 放缓至 2026 年 5.0%，通胀由 1.9% 升至 3.0%；印尼央行 6 月加息 25 个基点至 5.75%。按 OJK 2023 年第 23 号条例，险企与再保须分阶段满足更高最低权益，首阶段 2026 年 12 月 31 日生效，截至 2026 年 7 月多数公司已达 1,400 万美元（2,500 亿印尼盾）初始门槛。",
            "tc": "AM Best 10 月 8 日報告維持印尼非壽險「穩定」展望：保費增長預期仍強，但理賠通脹與競爭持續壓制盈利。IMF 預測印尼實質 GDP 增速由 2025 年 5.1% 放緩至 2026 年 5.0%，通脹由 1.9% 升至 3.0%；印尼央行 6 月加息 25 個基點至 5.75%。按 OJK 2023 年第 23 號條例，險企與再保須分階段滿足更高最低權益，首階段 2026 年 12 月 31 日生效，截至 2026 年 7 月多數公司已達 1,400 萬美元（2,500 億印尼盾）初始門檻。"
        },
        "why": {
            "sc": "医疗通胀压利润加上资本门槛抬升，是东南亚市场未来两年的主线，意味当地中小型险企可能增资或整合。对跨境团队判断合作方、转介对象与区域扩张节奏有参考价值。",
            "tc": "醫療通脹壓利潤加上資本門檻抬升，是東南亞市場未來兩年的主線，意味當地中小型險企可能增資或整合。對跨境團隊判斷合作方、轉介對象與區域擴張節奏有參考價值。"
        },
        "source": {
            "sc": "Insurance Asia 2026-10-20（引 AM Best 10 月 8 日报告）",
            "tc": "Insurance Asia 2026-10-20（引 AM Best 10 月 8 日報告）",
            "lang": "en",
            "name": "insuranceasia",
            "date": "2026-10-20"
        },
        "tags": {
            "sc": ["印尼", "非寿险", "医疗通胀", "资本要求", "AM Best"],
            "tc": ["印尼", "非壽險", "醫療通脹", "資本要求", "AM Best"]
        },
        "actions": {
            "front": {"sc": "客户沟通：区域市场风险认知", "tc": "客户溝通：區域市場風險認知"},
            "midback": {"sc": "合作方评估：资本与盈利能力", "tc": "合作方評估：資本與盈利能力"},
            "lead": {"sc": "团队简报：东南亚市场主线", "tc": "團隊簡報：東南亞市場主線"},
            "cross": {"sc": "跨境业务布局参考", "tc": "跨境業務佈局參考"}
        },
        "rolesImpact": {"front": 1, "midback": 2, "lead": 2, "cross": 1},
        "ingestedAt": NOW
    },
    {
        "id": "insuranceasia-taiwan-nhi-seniors-subsidy-20261020",
        "publishedAt": "2026-10-20T05:30:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/taiwan-approves-full-health-insurance-subsidies-seniors",
        "sourceKey": "insuranceasia",
        "sourceTier": "media",
        "score": 66,
        "verifyStatus": "verified",
        "contentKind": "news",
        "clusterCount": 1,
        "boards": ["reg"],
        "themes": ["taiwan", "health-insurance", "subsidy", "policy"],
        "title": {
            "sc": "台湾修法：65 岁以上符合资格者健保费由中央全额补助　年需约 390 亿新台币",
            "tc": "台灣修法：65 歲以上符合資格者健保費由中央全額補助　年需約 390 億新台幣"
        },
        "summary": {
            "sc": "台湾立法院以 60 比 39 通过《老人福利法》第 22 条修正，规定 65 岁以上、年度净所得低于申报门槛或适用税率低于 20% 者，其全民健保每月保费（25.42 美元／826 新台币）由中央政府全额补助；按现行税级，年净所得约 4.25 万美元（138 万新台币）以下可适用。民众党估计年需约 12 亿美元（390 亿新台币）；卫福部长石崇良担忧财政冲击，指其偏离量能负担原则。法案在地方选举前六周通过。",
            "tc": "台灣立法院以 60 比 39 通過《老人福利法》第 22 條修正，規定 65 歲以上、年度淨所得低於申報門檻或適用稅率低於 20% 者，其全民健保每月保費（25.42 美元／826 新台幣）由中央政府全額補助；按現行稅級，年淨所得約 4.25 萬美元（138 萬新台幣）以下可適用。民眾黨估計年需約 12 億美元（390 億新台幣）；衛福部長石崇良擔憂財政衝擊，指其偏離量能負擔原則。法案在地方選舉前六週通過。"
        },
        "why": {
            "sc": "公费补助扩张会削弱商业医疗险的补位诉求，同时加重财政与健保体系压力。台湾是高龄化与商保互动最典型的样本，可用于对照香港自愿医保、长者医疗券的取舍逻辑：公费覆盖越宽，商保卖点越要向自费药、私家服务与跨境医疗迁移。",
            "tc": "公費補助擴張會削弱商業醫療險的補位訴求，同時加重財政與健保體系壓力。台灣是高齡化與商保互動最典型的樣本，可用於對照香港自願醫保、長者醫療券的取捨邏輯：公費覆蓋越寬，商保賣點越要向自費藥、私家服務與跨境醫療遷移。"
        },
        "source": {
            "sc": "Insurance Asia 2026-10-20（引 Focus Taiwan 报道）",
            "tc": "Insurance Asia 2026-10-20（引 Focus Taiwan 報道）",
            "lang": "en",
            "name": "insuranceasia",
            "date": "2026-10-20"
        },
        "tags": {
            "sc": ["台湾", "全民健保", "长者补助", "公费医疗", "政策"],
            "tc": ["台灣", "全民健保", "長者補助", "公費醫療", "政策"]
        },
        "actions": {
            "front": {"sc": "客户沟通：公费医疗与商保分工", "tc": "客户溝通：公費醫療與商保分工"},
            "midback": {"sc": "产品定位：医疗险补位空间", "tc": "產品定位：醫療險補位空間"},
            "lead": {"sc": "团队简报：高龄化与医保财政", "tc": "團隊簡報：高齡化與醫保財政"},
            "cross": {"sc": "跨境养老与医疗安排素材", "tc": "跨境養老與醫療安排素材"}
        },
        "rolesImpact": {"front": 2, "midback": 1, "lead": 1, "cross": 1},
        "ingestedAt": NOW
    },
    {
        "id": "insuranceasia-hdfc-life-vnb-q2fy27-20261020",
        "publishedAt": "2026-10-20T05:45:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/hdfc-life-lifts-new-business-value-15-122m",
        "sourceKey": "insuranceasia",
        "sourceTier": "media",
        "score": 64,
        "verifyStatus": "verified",
        "contentKind": "report",
        "clusterCount": 1,
        "boards": ["insurer"],
        "themes": ["india", "life-insurance", "vnb", "distribution"],
        "title": {
            "sc": "HDFC Life 二季度新业务价值升 15% 至 1.22 亿美元　利润率 24.5%",
            "tc": "HDFC Life 二季度新業務價值升 15% 至 1.22 億美元　利潤率 24.5%"
        },
        "summary": {
            "sc": "HDFC Life 2027 财年第二季（截至 2026 年 9 月）新业务价值同比升 15% 至 1.221 亿美元（116 亿印度卢比），VNB 利润率由 24.1% 升至 24.5%，落于 24%–25% 指引；年化保费等值（APE）升 13% 至 4.981 亿美元，个人 APE 升 11%、团体升 25%。渠道分化明显：经纪升 26%、银保升 12%、代理仅升 3%、直销升 2%；HDFC 银行占上半年 APE 的 48%。Motilal Oswal 预期 2026–28 财年年增 14%，利润率 2028 财年升至 25.5%。",
            "tc": "HDFC Life 2027 財年第二季（截至 2026 年 9 月）新業務價值同比升 15% 至 1.221 億美元（116 億印度盧比），VNB 利潤率由 24.1% 升至 24.5%，落於 24%–25% 指引；年化保費等值（APE）升 13% 至 4.981 億美元，個人 APE 升 11%、團體升 25%。渠道分化明顯：經紀升 26%、銀保升 12%、代理僅升 3%、直銷升 2%；HDFC 銀行佔上半年 APE 的 48%。Motilal Oswal 預期 2026–28 財年年增 14%，利潤率 2028 財年升至 25.5%。"
        },
        "why": {
            "sc": "保护型与分红型产品结构如何影响新业务价值率，印度市场给出干净样本；渠道分化（经纪 +26%、代理 +3%）也说明分销结构本身就是利润杠杆，比单纯看保费增速更能判断一家公司的质量。",
            "tc": "保護型與分紅型產品結構如何影響新業務價值率，印度市場給出乾淨樣本；渠道分化（經紀 +26%、代理 +3%）也說明分銷結構本身就是利潤槓桿，比單純看保費增速更能判斷一家公司的質量。"
        },
        "source": {
            "sc": "Insurance Asia 2026-10-20（引 Motilal Oswal 研究）",
            "tc": "Insurance Asia 2026-10-20（引 Motilal Oswal 研究）",
            "lang": "en",
            "name": "insuranceasia",
            "date": "2026-10-20"
        },
        "tags": {
            "sc": ["新业务价值", "印度", "渠道结构", "利润率", "银保"],
            "tc": ["新業務價值", "印度", "渠道結構", "利潤率", "銀保"]
        },
        "actions": {
            "front": {"sc": "客户沟通：产品结构决定价值率", "tc": "客户溝通：產品結構決定價值率"},
            "midback": {"sc": "同业对标：VNB 与渠道效率", "tc": "同業對標：VNB 與渠道效率"},
            "lead": {"sc": "团队简报：分销结构的利润杠杆", "tc": "團隊簡報：分銷結構的利潤槓桿"},
            "cross": {"sc": "区域市场比较素材", "tc": "區域市場比較素材"}
        },
        "rolesImpact": {"front": 1, "midback": 2, "lead": 2, "cross": 0},
        "ingestedAt": NOW
    },
    {
        "id": "asiainsurancereview-nfra-pc-product-rules-20261016",
        "publishedAt": "2026-10-16T00:00:00+08:00",
        "originalUrl": "https://www.asiainsurancereview.com/News/View-NewsLetter-Article/id/97257/Type/eCin/NFRA-revises-insurance-product-development-and-management-regulations",
        "sourceKey": "asiainsurancereview",
        "sourceTier": "pro",
        "score": 70,
        "verifyStatus": "pending",
        "contentKind": "circular",
        "clusterCount": 1,
        "boards": ["reg"],
        "themes": ["china", "nfra", "product-regulation", "p-and-c"],
        "title": {
            "sc": "金融监管总局发布财产险公司产品开发管理规定（2026 年 10 月 9 日）",
            "tc": "金融監管總局發布財產險公司產品開發管理規定（2026 年 10 月 9 日）"
        },
        "summary": {
            "sc": "国家金融监督管理总局于 2026 年 10 月 9 日发布《财产保险公司保险产品开发管理办法》，规范财产险公司产品开发管理；同期报道指新规收紧产品治理与审批流程。（本条为补漏入库，内容源自行业媒体摘要，尚待核对总局原文。）",
            "tc": "國家金融監督管理總局於 2026 年 10 月 9 日發布《財產保險公司保險產品開發管理辦法》，規範財產險公司產品開發管理；同期報道指新規收緊產品治理與審批流程。（本條為補漏入庫，內容源自行業媒體摘要，尚待核對總局原文。）"
        },
        "why": {
            "sc": "内地财产险产品治理与审批趋严，是跨境业务（大湾区联动、内地客户在港配置）监管环境的背景变量。此前本库 NFRA 侧仅覆盖 2025 年预定利率机制，此条补上 2026 年产品端规则变化，待取得总局原文后再升级为已核。",
            "tc": "內地財產險產品治理與審批趨嚴，是跨境業務（大灣區聯動、內地客户在港配置）監管環境的背景變量。此前本庫 NFRA 側僅覆蓋 2025 年預定利率機制，此條補上 2026 年產品端規則變化，待取得總局原文後再升級為已核。"
        },
        "source": {
            "sc": "Asia Insurance Review（eWeekly China）2026-10-16",
            "tc": "Asia Insurance Review（eWeekly China）2026-10-16",
            "lang": "en",
            "name": "asiainsurancereview",
            "date": "2026-10-16"
        },
        "tags": {
            "sc": ["NFRA", "财产险", "产品管理", "监管规则", "中国"],
            "tc": ["NFRA", "財產險", "產品管理", "監管規則", "中國"]
        },
        "actions": {
            "front": {"sc": "—", "tc": "—"},
            "midback": {"sc": "合规跟踪：内地产品规则变化", "tc": "合規跟蹤：內地產品規則變化"},
            "lead": {"sc": "团队简报：跨境监管环境", "tc": "團隊簡報：跨境監管環境"},
            "cross": {"sc": "—", "tc": "—"}
        },
        "rolesImpact": {"front": 0, "midback": 2, "lead": 1, "cross": 0},
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
