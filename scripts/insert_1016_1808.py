#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-16 18:08 增量：插入新条目 + 回写 meta + last-check。"""
import json, shutil, os
import zhconv

P = '/Users/leonliang/maoquanqingbao'
NOW = '2026-10-16T18:08:00+08:00'
STAMP = '1016-1808'


def t2(s):
    return zhconv.convert(s, 'zh-hant')


def pair(s):
    return {'sc': s, 'tc': t2(s)}


def tlist(items):
    return {'sc': items, 'tc': [t2(x) for x in items]}


ITEMS = [
    # ---------- insuranceasia (media 66) ----------
    {
        "id": "iaasia-generali-world-bank-mou-asia-climate-20261016",
        "publishedAt": "2026-10-16T06:30:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/generali-world-bank-target-asias-climate-insurance-gaps",
        "sourceKey": "insuranceasia", "sourceTier": "media", "score": 66, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["market", "reg"],
        "themes": ["climate-risk", "agriculture-insurance", "ageing", "public-private-partnership", "emerging-markets"],
        "summary": pair("忠利（Generali）與世界銀行集團在世界銀行及國際貨幣基金組織曼谷年會期間簽署諒解備忘錄，聚焦動員私人資本、強化韌性並擴大新興市場的保險與投資方案。保險部分初期以亞洲市場為重點，三個優先領域為：配合世銀「銀髮經濟計劃」為高齡人口設計保障、為農業提供氣候及農作物保險、以及強化災害與氣候風險保障；雙方亦會合作推動區域風險池，建立可分散、可擴展的巨災保障結構，並設計與氣候風險掛鈎的風險轉移機制。[EN原文]"),
        "why": pair("官方機構與大型保險集團的「公共—私人」合作，正成為應對氣候與老齡化保障缺口的主要框架；香港若要坐實區域風險管理中心，這類跨國風險池與參數式工具的參與空間值得跟進。"),
        "source": {"sc": "Insurance Asia 2026-10-16 报道（Generali 与世银集团公布）",
                   "tc": "Insurance Asia 2026-10-16 報道（Generali 與世銀集團公布）",
                   "lang": "en", "name": "Insurance Asia", "date": "2026-10-16",
                   "note": "EN原文；含三大优先领域与风险池安排"},
        "tags": tlist(["Generali", "世界银行", "气候保险", "参数式保险", "银发经济"]),
        "actions": {"front": {},
                    "midback": pair("气候与农业保险产品动态跟踪"),
                    "lead": pair("团队简报：新兴市场保障缺口"),
                    "cross": pair("客户解说素材：气候风险转移")},
        "rolesImpact": {"front": 0, "midback": 2, "lead": 2, "cross": 1},
        "title": pair("Generali 与世银集团签署备忘录　聚焦亚洲气候、农业与高龄保障缺口"),
    },
    {
        "id": "iaasia-kovernow-axa-xl-art-collectables-sg-20261016",
        "publishedAt": "2026-10-16T06:15:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/kovernow-widens-insurance-cover-collectors-turn-digital",
        "sourceKey": "insuranceasia", "sourceTier": "media", "score": 66, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["product", "tech"],
        "themes": ["digital-insurance", "fine-art", "high-net-worth", "underwriting", "hong-kong-expansion"],
        "summary": pair("新加坡保险科企 KoverNow 扩大数字保险范围，新增艺术品、红酒、威士忌及各类收藏品保障，由 AXA XL 承保，全球保障遗失、盗窃及意外损坏；产品经 iOS 及 Android 应用提供即时报价，覆盖画作、雕塑、古董、专业评级交易卡、体育及电影纪念品。KoverNow 行政总裁 Stephan Kaiser 指藏家已转向数字交易平台买卖，但保险仍是另一套更耗时的流程；AXA XL 亚洲艺术品及贵重物品核保经理 Rhiannon Alban-Davies 称客户期望专项保障更易获取。双方合作始于 2026 年 1 月的手表、珠宝与手袋数字保险，KoverNow 计划把扩展产品带到香港。[EN原文]"),
        "why": pair("高价值收藏品长期依赖人手核保、流程冗长，App 化即时报价正把这块高净值市场拆细；AXA XL 愿以专项承保能力支持平台化分销，是「科技分销＋传统承保」模式向香港复制的前置信号。"),
        "source": {"sc": "Insurance Asia 2026-10-16 报道（KoverNow 与 AXA XL 公布）",
                   "tc": "Insurance Asia 2026-10-16 報道（KoverNow 與 AXA XL 公布）",
                   "lang": "en", "name": "Insurance Asia", "date": "2026-10-16",
                   "note": "EN原文；含承保方、覆盖标的与香港延伸计划"},
        "tags": tlist(["KoverNow", "AXA XL", "艺术品保险", "保险科技", "香港"]),
        "actions": {"front": pair("高净值收藏品保障切入点"),
                    "midback": pair("艺术品及贵重物品承保动态"),
                    "lead": pair("产品简报：平台化专项保障"),
                    "cross": pair("家办客户另类资产保障素材")},
        "rolesImpact": {"front": 1, "midback": 2, "lead": 1, "cross": 2},
        "title": pair("AXA XL 承保 KoverNow 新加坡艺术品与收藏品保单　平台拟延伸至香港"),
    },
    {
        "id": "iaasia-ransomware-cyber-insurance-singapore-20261016",
        "publishedAt": "2026-10-16T05:30:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/ransomware-hits-cyber-insurance-47-singapore-firms",
        "sourceKey": "insuranceasia", "sourceTier": "media", "score": 66, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["market", "tech"],
        "themes": ["cyber-insurance", "ransomware", "artificial-intelligence", "singapore", "claims"],
        "summary": pair("网络安全韧性公司 Semperis 调查显示，新加坡 52% 机构因勒索软件攻击出现业务中断或收入损失，47% 面临网络保险被取消或保费上调，26% 曾支付赎金。六成受攻击企业指攻击者使用人工智能，高于全球的 40%，新加坡的 AI 使用率为全球 1.5 倍；98% 受访者称 AI 以某种形式参与事件，其中 49% 靠 AI 成功侦测或回应，28% 称工具失效或仅部分有效。逾九成攻击针对身分系统（Active Directory 52%、Entra ID 48%、Okta 37%），56% 受威胁机构收到寄往住所或办公室的恐吓信件或包裹。[EN原文]"),
        "why": pair("网络保险的承保结果正被 AI 驱动的攻击手法直接改写——保单取消与加费已是客户实感；前線为中小企业客户做风险检视时，AI 治理与身分基础设施防护可成为加保与核保的切入点。"),
        "source": {"sc": "Insurance Asia 2026-10-16 报道（引述 Semperis 调查）",
                   "tc": "Insurance Asia 2026-10-16 報道（引述 Semperis 調查）",
                   "lang": "en", "name": "Insurance Asia", "date": "2026-10-16",
                   "note": "EN原文；含保险端影响与 AI 相关数据"},
        "tags": tlist(["网络保险", "勒索软件", "人工智能", "新加坡", "Semperis"]),
        "actions": {"front": pair("企业客户网络安全风险检视"),
                    "midback": pair("网络险核保与续保条件跟踪"),
                    "lead": pair("团队简报：AI 时代的网络风险"),
                    "cross": {}},
        "rolesImpact": {"front": 2, "midback": 2, "lead": 1, "cross": 0},
        "title": pair("新加坡 47% 企业因勒索软件遭遇网络险取消或加费　六成攻击涉 AI"),
    },
    {
        "id": "iaasia-fwd-hkfi-qmark-critical-illness-20261016",
        "publishedAt": "2026-10-16T05:15:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/fwd-launches-illness-insurance-amidst-push-clearer-claims",
        "sourceKey": "insuranceasia", "sourceTier": "media", "score": 66, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["product"],
        "themes": ["critical-illness", "standardisation", "q-mark", "hkfi", "claims"],
        "summary": pair("富卫香港推出「危疾全支援」保险系列，成为香港首个新推出、取得保联「危疾定义标准化」Q 标志的危疾产品。系列涵盖危疾、早期疾病及多项特殊疾病，并提供多重赔偿与确诊后支援，另设家庭保障概念，子女及父母无须健康核保即可纳入。FWD 同时採用「FavourU」原则：若保单定义与保联标准定义出现冲突，以对客户较有利者为准，并会适用于新客户及现有客户的危疾产品。保联行政总监刘佩玲指标准化有助减少消费者混淆、提升透明度及改善理赔体验。[EN原文]"),
        "why": pair("保联危疾定义标准化自 2026 年 9 月 1 日起适用于新产品，Q 标志让客户一眼可比；若「较有利定义优先」成为行业惯例，将直接改写前线的产品比较叙事与理赔预期管理方式。"),
        "source": {"sc": "Insurance Asia 2026-10-16 报道（产品于 10 月 14 日发布，FWD 与保联公布）",
                   "tc": "Insurance Asia 2026-10-16 報道（產品於 10 月 14 日發布，FWD 與保聯公布）",
                   "lang": "en", "name": "Insurance Asia", "date": "2026-10-16",
                   "note": "EN原文；含 Q 标志与较有利定义原则"},
        "tags": tlist(["富卫", "危疾", "保联", "Q标志", "定义标准化"]),
        "actions": {"front": pair("危疾产品比较与理赔预期沟通"),
                    "midback": pair("同业危疾产品是否跟进较有利定义"),
                    "lead": pair("团队培训素材：标准化定义要点"),
                    "cross": {}},
        "rolesImpact": {"front": 3, "midback": 2, "lead": 2, "cross": 0},
        "title": pair("富卫香港推危疾全支援系列　成首个取得保联危疾标准化定义 Q 标志的新产品"),
    },
    {
        "id": "iaasia-aon-medical-trend-2027-20261016",
        "publishedAt": "2026-10-16T05:00:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/in-focus/health-insurance-costs-strain-employers-in-2027",
        "sourceKey": "insuranceasia", "sourceTier": "media", "score": 66, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["market", "product"],
        "themes": ["medical-inflation", "employee-benefits", "apac", "glp-1", "expatriate"],
        "summary": pair("怡安（Aon）《2027 全球医疗趋势费率报告》预计全球平均医疗趋势率为 9.0%，低于 2026 年的 9.8%，但仍为一般通胀率 2.6% 的三倍以上。亚太区由 11.3% 降至 9.7%（中国降至 6.0%、印度降至 10.1%），中東及非洲由 15.3% 降至 12.2%，拉丁美洲大致持平於 10.4%。跨国流动雇员医疗保费持续跑赢本土计划，美英外派保单预计升 11.5%，亚太及中东外派保单达 15.0%。主要驱动因素包括心血管疾病、癌症、高血压、肥胖率上升，以及 GLP-1 减重及糖尿病药物（占部分市场趋势率最多 10.0%、全球平均逾 3.0%）。[EN原文]"),
        "why": pair("团体医疗是香港雇员福利与企业客户的核心成本项，亚太外派保单 15% 的趋势率意味续保加费压力未减；GLP-1 已成可量化的成本变量，可作为与客户讨论福利设计与成本控制的具体依据。"),
        "source": {"sc": "Insurance Asia 2026-10-16 报道（引述 Aon 2027 报告）",
                   "tc": "Insurance Asia 2026-10-16 報道（引述 Aon 2027 報告）",
                   "lang": "en", "name": "Insurance Asia", "date": "2026-10-16",
                   "note": "EN原文；含区域趋势率与驱动因素"},
        "tags": tlist(["Aon", "医疗通胀", "雇员福利", "亚太", "GLP-1"]),
        "actions": {"front": pair("团体医疗续保加费预警沟通"),
                    "midback": pair("医疗趋势率与区域对比跟踪"),
                    "lead": pair("团队简报：福利成本与保障设计"),
                    "cross": pair("企业客户福利优化素材")},
        "rolesImpact": {"front": 2, "midback": 2, "lead": 2, "cross": 1},
        "title": pair("怡安预测 2027 全球医疗趋势率 9.0%　亚太外派保单高达 15%"),
    },

    # ---------- insurancebusinessmag (media 62) ----------
    {
        "id": "ibm-lloyds-capital-asian-hubs-20261016",
        "publishedAt": "2026-10-16T17:14:00+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/capital-is-pouring-into-lloyds-even-as-asian-hubs-top-the-insurance-rankings-593819.aspx",
        "sourceKey": "insurancebusinessmag", "sourceTier": "media", "score": 62, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["market"],
        "themes": ["lloyds", "capital", "syndicates", "softening-rates", "asia-hubs"],
        "summary": pair("Insurance Business 引述劳合社 2025 年年报及巴克莱分析：2025 年有 7 个新辛迪加开始承保，2026 年 1 月 1 日再增 13 个，另有逾 50 宗认真承保查询，网络再保人 Envelop 已获原则性批准于明年把特别目的安排转为完整辛迪加。劳合社 2025 年毛保费增 4.2% 至 579 亿英镑、利润 106 亿英镑、资本回报 22%，连续三年超过 20%；2026 年获批准资本 362 亿英镑，较 337 亿增 7.4%。巴克莱指资金回流源于劳合社现代化、投资者基础扩大，以及辛迪加资本结构变复杂，但 2023 及 2024 年财产巨灾费率急升提供了顺风，市场正转入软化。[EN原文]"),
        "why": pair("资本持续流入劳合社的同时费率下行，与亚洲枢纽（香港、新加坡）在专属自保与 ILS 上的追赶形成对照；香港要在区域风险中心竞争中留住人才与资本，须正视伦敦在准入效率与资本结构创新上的改变。"),
        "source": {"sc": "Insurance Business 2026-10-16 报道（引述劳合社年报与巴克莱分析）",
                   "tc": "Insurance Business 2026-10-16 報道（引述勞合社年報與巴克萊分析）",
                   "lang": "en", "name": "Insurance Business", "date": "2026-10-16",
                   "note": "EN原文；含辛迪加数目、保费与资本数据"},
        "tags": tlist(["劳合社", "辛迪加", "资本", "软市场", "亚洲枢纽"]),
        "actions": {"front": {},
                    "midback": pair("离岸承保能力与费率周期跟踪"),
                    "lead": pair("团队简报：伦敦与亚洲枢纽竞争"),
                    "cross": pair("客户解说素材：承保周期")},
        "rolesImpact": {"front": 0, "midback": 2, "lead": 2, "cross": 1},
        "title": pair("资本持续流入劳合社　2026 年新增 13 个辛迪加、获批资本 362 亿英镑"),
    },
    {
        "id": "ibm-sumitomo-life-income-insurance-20261016",
        "publishedAt": "2026-10-16T11:09:00+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/giant-japanese-insurer-looking-south-and-to-the-us-for-deals-593771.aspx",
        "sourceKey": "insurancebusinessmag", "sourceTier": "media", "score": 62, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["insurer", "market"],
        "themes": ["mergers-acquisitions", "singapore", "japan", "income-insurance", "governance"],
        "summary": pair("住友生命社长高田幸德接受彭博访问时表示，正评估包括新加坡 Income Insurance 在内的收购对象，并确认至 2029 年 3 月已预留最多 1 万亿日圆作投资。Income 是 2024 年安联拟以约 22 亿新加坡元收购 51% 股权但最终告吹的标的，因文化、社区及青年部关注其对合作社社会使命缺乏约束性保障，NTUC Enterprise 仍持约 72.8% 控股權。住友生命年内曾与安联、第一生命一同入围滙丰新加坡寿险业务竞投，最终安联以估值 27 亿新加坡元胜出。[EN原文]"),
        "why": pair("日本寿险资金持续南下寻找规模，但 Income 的社会使命条款要求任何买家先解决治理承诺；这宗潜在交易将再次测试新加坡对保险并购的社会责任红线，并牵动区内寿险资产的估值参考。"),
        "source": {"sc": "Insurance Business 2026-10-16 报道（引述彭博访问）",
                   "tc": "Insurance Business 2026-10-16 報道（引述彭博訪問）",
                   "lang": "en", "name": "Insurance Business", "date": "2026-10-16",
                   "note": "EN原文；含投资预算与历史交易背景"},
        "tags": tlist(["住友生命", "Income Insurance", "并购", "新加坡", "日本"]),
        "actions": {"front": {},
                    "midback": pair("亚洲寿险并购与估值动态"),
                    "lead": pair("团队简报：日本资金南下"),
                    "cross": pair("家办客户区域资产配置参考")},
        "rolesImpact": {"front": 0, "midback": 2, "lead": 2, "cross": 1},
        "title": pair("住友生命评估收购新加坡 Income Insurance　已预留最多 1 万亿日圆作投资"),
    },
    {
        "id": "ibm-sunlife-global-rebrand-20261016",
        "publishedAt": "2026-10-16T09:12:00+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/life-insurance/sun-life-becomes-sunlife-in-global-rebrand-593788.aspx",
        "sourceKey": "insurancebusinessmag", "sourceTier": "media", "score": 62, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["insurer", "product"],
        "themes": ["rebrand", "branding", "asia-growth", "retirement", "caregiving"],
        "summary": pair("永明金融把全球品牌统一为「Sunlife」，取消名称中的空格，并採用新标志及标语「Making life brighter」；集团指改动反映业务已由寿险延伸至资产管理、健康、财富与保险，新标志为简化版的太阳球设计，将分阶段在各地市场推出，过渡期新旧品牌可能并存。集团同时发布八个市场调查（六個在亚洲：香港、菲律宾、越南、印尼、马来西亚、新加坡，另加加拿大与美国）：61% 受访者认为应对突发疾病或意外开支非常重要，但仅 33% 有完整计划；照顾年长或患病家人的落差最大（57% 认为重要、27% 有完整计划）；退休为 56% 对 31%。[EN原文]"),
        "why": pair("品牌整合往往先于区域业务整合，亚洲占调查市场三分之二可见战略重心；「重视程度高、行动比例低」的落差是保障缺口最直接的销售语言，可直接用于客户风险检视对话。"),
        "source": {"sc": "Insurance Business 2026-10-16 报道（永明金融公布）",
                   "tc": "Insurance Business 2026-10-16 報道（永明金融公布）",
                   "lang": "en", "name": "Insurance Business", "date": "2026-10-16",
                   "note": "EN原文；含品牌安排与八市场调查数据"},
        "tags": tlist(["永明金融", "品牌重塑", "保障缺口", "退休", "亚洲"]),
        "actions": {"front": pair("保障缺口对话素材（照顾与退休）"),
                    "midback": pair("品牌更新与客户沟通口径跟踪"),
                    "lead": pair("团队简报：保障缺口数据"),
                    "cross": {}},
        "rolesImpact": {"front": 2, "midback": 1, "lead": 1, "cross": 0},
        "title": pair("永明金融全球统一品牌为「Sunlife」　同步发布亚洲保障缺口调查"),
    },
    {
        "id": "ibm-sme-cyber-penetration-20261016",
        "publishedAt": "2026-10-16T03:11:00+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/cyber/sme-cyber-insurance-uptake-stalls-everywhere-except-the-us-593616.aspx",
        "sourceKey": "insurancebusinessmag", "sourceTier": "media", "score": 62, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["market", "product"],
        "themes": ["cyber-insurance", "sme", "penetration", "distribution", "cfc"],
        "summary": pair("Insurance Business 引述 CFC 全球网络发展主管 Lindsey Maher：美国中小企业独立网络保险渗透率约 30% 至 40%，英国、加拿大、澳洲、新西兰等可比市场仅约 10% 至 15%，且多年来停滞。美国有逾 200 个可供选择的网络保险承保市场。她认为差距源于市场结构而非客户认知——「不知道有这个风险」的问题基本已解决，但成交未跟上，各地客户的反对理由亦大致相同；她把承保市场密度本身视为增长机制，认为更多承保人报价会带来更多对话。报道同时指出，这些保单所覆盖的暴露正朝相反方向扩大。[EN原文]"),
        "why": pair("网络险的瓶颈由「客户不知道」转为「分销密度不足」，意味着加保要靠多渠道持续对话而非单次教育；对香港中小企业客群，这是把风险检视常规化、以接触密度带动转化的直接依据。"),
        "source": {"sc": "Insurance Business 2026-10-16 报道（引述 CFC 主管）",
                   "tc": "Insurance Business 2026-10-16 報道（引述 CFC 主管）",
                   "lang": "en", "name": "Insurance Business", "date": "2026-10-16",
                   "note": "EN原文；含各地区渗透率与市场结构对比"},
        "tags": tlist(["网络保险", "中小企业", "渗透率", "分销", "CFC"]),
        "actions": {"front": pair("中小企业客户网络险加保切入点"),
                    "midback": pair("渗透率与产品供给跟踪"),
                    "lead": pair("团队简报：网络险分销策略"),
                    "cross": {}},
        "rolesImpact": {"front": 2, "midback": 1, "lead": 1, "cross": 0},
        "title": pair("美国中小企业网络险渗透率 30% 至 40%　可比市场仅约一成、瓶颈在分销密度"),
    },
    {
        "id": "ibm-marsh-thrive-ai-costs-20261016",
        "publishedAt": "2026-10-16T01:16:00+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/marsh-looking-to-cut-even-more-costs-as-ai-reshapes-its-back-office-593717.aspx",
        "sourceKey": "insurancebusinessmag", "sourceTier": "media", "score": 62, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["market", "tech"],
        "themes": ["artificial-intelligence", "cost-efficiency", "broker", "back-office", "automation"],
        "summary": pair("威达信（Marsh）把三年效率与增长计划「Thrive」的年度节省目标由 4 亿美元上调至约 6 亿美元，主要来自共享服务部門与科技进步；达标成本同时由约 5 亿上调至约 7.5 亿美元，自推出以来已入帐 3.1 亿美元（主要為遣散费，其中第三季 7,100 万美元）。行政总裁 John Doyle 指已开始「消化部分自然流失」，节省将用于增聘前線生产人员，中台及后台岗位收缩；共享服务正建立客户开户、数据接入与商业赋能能力，并把工序移至集团能力中心（未公布地点，对亚洲服务枢纽有影响）。集团自建内部 AI 模型、每周向员工推出新工具，Broker Workbench 令伦敦批发业务 93% 交易数字化，报价由 2 至 4 周缩短至数小时。[EN原文]"),
        "why": pair("这是「AI 直接压缩中后台人手、资源前移至前线」最清楚的经纪案例；香港团队在资源配置与生产力叙事上可作对照，亦提醒中后台岗位的技能转型压力。"),
        "source": {"sc": "Insurance Business 2026-10-16 报道（Marsh 第三季业绩会与 SEC 文件）",
                   "tc": "Insurance Business 2026-10-16 報道（Marsh 第三季業績會與 SEC 文件）",
                   "lang": "en", "name": "Insurance Business", "date": "2026-10-16",
                   "note": "EN原文；含节省目标、成本与 AI 工具数据"},
        "tags": tlist(["威达信", "人工智能", "效率计划", "保险经纪", "中后台"]),
        "actions": {"front": {},
                    "midback": pair("中后台流程自动化与人力结构跟踪"),
                    "lead": pair("团队简报：AI 与组织效率"),
                    "cross": pair("内部生产力提升参考")},
        "rolesImpact": {"front": 0, "midback": 3, "lead": 2, "cross": 1},
        "title": pair("威达信上调「Thrive」年度节省目标至 6 亿美元　AI 重塑中后台、资源转投前线"),
    },

    # ---------- artemis (pro 70) ----------
    {
        "id": "artemis-ccrif-panama-parametric-17m-20261016",
        "publishedAt": "2026-10-16T16:00:00+08:00",
        "originalUrl": "https://www.artemis.bm/news/ccrif-to-pay-us-17-4m-to-panama-after-m7-7-quake-triggers-parametric-coverage/",
        "sourceKey": "artemis", "sourceTier": "pro", "score": 70, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["market"],
        "themes": ["parametric-insurance", "catastrophe-risk", "earthquake", "risk-pool", "payout"],
        "summary": pair("加勒比与中美洲地区参数式风险池 CCRIF SPC 将向巴拿马政府支付 1,740 万美元，因 10 月 9 日该国 7.7 级地震触发其参数式地震保障。CCRIF 以 SPHERA 地震模型估算全国峰值地面加速度最高达 0.5g，巴拿马是唯一超过模型 0.03g 报告门槛的成员国；模拟损失超过地震保单的参数触发值，赔款将于地震后 14 天内支付。地震造成多省房屋、学校、医院、公共建筑及道路损毁，初步评估 656 所学校受影响。巴拿马自 2018 年参与 CCRIF，此前已获三次赔款共约 2,900 万美元。连同本次，CCRIF 自 2007 年成立以来已赔付 83 次、总额逾 5 亿美元，全部于事件后 14 天内完成。[EN原文]"),
        "why": pair("参数式保险把「快速流动性」做成可验证的产品承诺，是主权与巨灾风险融资的成熟范式；香港争取区域风险管理中心与巨灾债券枢纽时，这类风险池的触发设计与结算速度是最直观的对标。"),
        "source": {"sc": "Artemis.bm 2026-10-16 报道（CCRIF 公布）",
                   "tc": "Artemis.bm 2026-10-16 報道（CCRIF 公布）",
                   "lang": "en", "name": "Artemis.bm", "date": "2026-10-16",
                   "note": "EN原文；含触发模型、赔款金额与时限"},
        "tags": tlist(["CCRIF", "参数式保险", "地震", "巨灾债券", "巴拿马"]),
        "actions": {"front": {},
                    "midback": pair("参数式产品触发与结算机制跟踪"),
                    "lead": pair("专题：巨灾风险融资范式"),
                    "cross": pair("家办另类资产（ILS）参考")},
        "rolesImpact": {"front": 0, "midback": 2, "lead": 2, "cross": 1},
        "title": pair("巴拿马 7.7 级地震触发参数式保障　CCRIF 赔付 1,740 万美元"),
    },
    {
        "id": "artemis-nascent-re-plymouth-warwick-36m-20261016",
        "publishedAt": "2026-10-16T15:00:00+08:00",
        "originalUrl": "https://www.artemis.bm/news/nascent-re-issues-36m-across-plymouth-warwick-preferred-share-insurance-linked-securities/",
        "sourceKey": "artemis", "sourceTier": "pro", "score": 70, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["market"],
        "themes": ["ils", "collateralized-reinsurance", "preferred-shares", "bermuda", "retrocession"],
        "summary": pair("百慕大 Nascent Group 旗下持牌再保转换平台 Nascent Re Ltd. 再发行 3,600 万美元优先股保险相连证券（ILS），分为 Plymouth（1,600 万美元，2027 年 6 月 30 日到期）与 Warwick（2,000 万美元，2026 年 12 月 15 日到期）两个独立帐户，属 Artemis 追踪到的第六宗同类发行，全部以优先股形式进行，可能代表某种抵押式再保或私人 ILS 安排。该平台今年 3 月首度发行 OFS Re 优先股（1,000 万欧元），8 月 Telford 2,350 万美元为最大单笔，9 月再发 Quinton 与 Stevenage 各 2,000 万美元。[EN原文]"),
        "why": pair("抵押式再保与私人 ILS 的发行频率上升，显示中型平台正把「风险转换」做成可重复的标准化产品；这类结构的成熟度，是香港与新加坡推动 PCC 制度时最需要对接的市场实务。"),
        "source": {"sc": "Artemis.bm 2026-10-16 报道（Nascent Re 发行）",
                   "tc": "Artemis.bm 2026-10-16 報道（Nascent Re 發行）",
                   "lang": "en", "name": "Artemis.bm", "date": "2026-10-16",
                   "note": "EN原文；含金额、到期日与历史发行梳理"},
        "tags": tlist(["Nascent Re", "ILS", "抵押式再保", "优先股", "百慕大"]),
        "actions": {"front": {},
                    "midback": pair("私人 ILS 发行与结构跟踪"),
                    "lead": pair("团队简报：抵押式再保工具"),
                    "cross": pair("家办另类资产（ILS）参考")},
        "rolesImpact": {"front": 0, "midback": 2, "lead": 1, "cross": 2},
        "title": pair("Nascent Re 再发行 3,600 万美元优先股 ILS　Plymouth 与 Warwick 两系列"),
    },

    # ---------- insuranceasianews (pro 70) ----------
    {
        "id": "ian-asian-ils-pcc-hong-kong-singapore-20261016",
        "publishedAt": "2026-10-16T07:30:00+08:00",
        "originalUrl": "https://insuranceasianews.com/real-step-forward-for-asian-ils-as-hong-kong-singapore-eye-pccs/",
        "sourceKey": "insuranceasianews", "sourceTier": "pro", "score": 70, "verifyStatus": "pending",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["reg", "market"],
        "themes": ["ils", "protected-cell-companies", "sidecar", "hong-kong", "singapore"],
        "summary": pair("InsuranceAsia News 分析指，香港与新加坡拟引入保护 cell 公司（PCC）制度，有望为亚洲侧挂（sidecar）市场带来增长与发展，再保业界认为区内第三方资本需求庞大，PCC 可提供更标准化、成本更低的风险隔离架构，报道形容这是亚洲 ILS 的「真正一步」。此前 MS Amlin 已物色投资者筹组 4,000 至 5,000 万美元的新加坡侧挂，人保财险亦于 10 月中完成香港首宗 1,200 万美元侧挂发行（财库局表示欢迎）。[EN原文；IAAN 正文需订阅，导读仅依公开导语与已公开事件]"),
        "why": pair("PCC 是把「一次性侧挂」变成「可重复设立平台」的关键基础设施；若香港落实，前线与家办客群对另类风险资产（ILS）的可及性将出现结构性变化，值得提前纳入客户教育素材。"),
        "source": {"sc": "InsuranceAsia News 2026-10-16 分析报道",
                   "tc": "InsuranceAsia News 2026-10-16 分析報道",
                   "lang": "en", "name": "InsuranceAsia News", "date": "2026-10-16",
                   "note": "EN原文；正文需订阅，待复核细节"},
        "tags": tlist(["保护cell公司", "ILS", "侧挂", "香港", "新加坡"]),
        "actions": {"front": {},
                    "midback": pair("香港 PCC 制度进展跟踪"),
                    "lead": pair("专题：亚洲 ILS 基建"),
                    "cross": pair("家办客户另类风险资产素材")},
        "rolesImpact": {"front": 0, "midback": 2, "lead": 3, "cross": 2},
        "title": pair("亚洲 ILS 迎来「真正一步」　香港与新加坡拟引入保护 cell 公司制度"),
    },
    {
        "id": "ian-kb-insurance-uk-lloyds-stakes-20261016",
        "publishedAt": "2026-10-16T11:23:00+08:00",
        "originalUrl": "https://insuranceasianews.com/kb-insurance-opens-uk-arm-sets-sights-on-stakes-in-lloyds-syndicates-report/",
        "sourceKey": "insuranceasianews", "sourceTier": "pro", "score": 70, "verifyStatus": "pending",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["insurer", "market"],
        "themes": ["korea", "lloyds", "expansion", "syndicates", "overseas"],
        "summary": pair("据 Chosun Biz 报道，韩国 KB 保险已在英国设立子公司，并计划投资劳合社辛迪加；报道指该韩国产险公司正循伦敦市场路径获取特殊风险承保能力并推进国际化。此举与近期多家亚洲保险集团加码劳合社的方向一致——劳合社 2026 年 1 月新增 13 个辛迪加，网络再保人 Envelop 亦获原则性批准转为完整辛迪加。KB 保险的既有海外布局以东南亚为主，英国为其首次进入劳合社生态。[EN原文；IAAN 正文需订阅]"),
        "why": pair("亚洲保险资本正沿「设点伦敦、入股辛迪加」的路线补足特殊风险能力；香港若要留住区域承保与再保功能，须正视本地市场在高端特殊风险与自保工具上的相对短板。"),
        "source": {"sc": "InsuranceAsia News 2026-10-16 报道（引述 Chosun Biz）",
                   "tc": "InsuranceAsia News 2026-10-16 報道（引述 Chosun Biz）",
                   "lang": "en", "name": "InsuranceAsia News", "date": "2026-10-16",
                   "note": "EN原文；正文需订阅，待复核"},
        "tags": tlist(["KB保险", "韩国", "劳合社", "辛迪加", "海外扩张"]),
        "actions": {"front": {},
                    "midback": pair("亚洲险企海外布局跟踪"),
                    "lead": pair("团队简报：承保能力外移趋势"),
                    "cross": {}},
        "rolesImpact": {"front": 0, "midback": 2, "lead": 2, "cross": 0},
        "title": pair("韩国 KB 保险设英国子公司　拟入股劳合社辛迪加"),
    },
    {
        "id": "ian-allianz-jingdong-ceo-chen-20261016",
        "publishedAt": "2026-10-16T12:59:00+08:00",
        "originalUrl": "https://insuranceasianews.com/john-chen-succeeds-william-liang-as-allianz-jingdong-ceo/",
        "sourceKey": "insuranceasianews", "sourceTier": "pro", "score": 70, "verifyStatus": "pending",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["insurer"],
        "themes": ["appointments", "allianz", "china", "joint-venture", "leadership"],
        "summary": pair("安联与京东在中国的合资公司安联京东财产保险（Allianz JD）换帅：John Chen 接任行政总裁，接替于周四离任、另寻发展的 William Liang，新任命自周五生效。该合营由安联与京东集团共同持股，属外资在内地产险的合资平台；安联近期在亚洲多线推进，包括 7 月以约 27 亿新加坡元收购滙丰新加坡寿险业务并取得 15 年独家银保合作。[EN原文；IAAN 正文需订阅]"),
        "why": pair("中国产险合资平台的管理层调整往往先于策略重估；安联同时在新加坡寿险、中国产险与香港区域平台多线布局，集团资源在区内的分配重心值得持续留意。"),
        "source": {"sc": "InsuranceAsia News 2026-10-16 报道",
                   "tc": "InsuranceAsia News 2026-10-16 報道",
                   "lang": "en", "name": "InsuranceAsia News", "date": "2026-10-16",
                   "note": "EN原文；正文需订阅，待复核"},
        "tags": tlist(["安联", "中国", "合资公司", "人事任命", "京东"]),
        "actions": {"front": {},
                    "midback": pair("外资在内地产险布局跟踪"),
                    "lead": pair("团队简报：集团区域人事变动"),
                    "cross": {}},
        "rolesImpact": {"front": 0, "midback": 1, "lead": 1, "cross": 0},
        "title": pair("安联京东产险换帅　John Chen 接替 William Liang 出任行政总裁"),
    },

    # ---------- reinsurancenews (pro 70) ----------
    {
        "id": "rn-aon-rafferty-chief-integration-officer-20261016",
        "publishedAt": "2026-10-16T18:00:00+08:00",
        "originalUrl": "https://www.reinsurancene.ws/aon-promotes-chris-rafferty-to-chief-integration-officer-for-imo/",
        "sourceKey": "reinsurancenews", "sourceTier": "pro", "score": 70, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["insurer", "market"],
        "themes": ["appointments", "aon", "integration", "mergers-acquisitions", "leadership"],
        "summary": pair("怡安（Aon）委任 Chris Rafferty 为整合管理办公室（IMO）首席整合官。他 2007 年加入集团任营运总监近 15 年，其后出任全球特殊产品主管两年，最近为芝加哥市场主管；他早年任职 Lincoln International 併购部副董事，2001 年起于美联银行证券任分析员。集团同时委任 Steven Carleton 接任芝加哥市场主管——他 2010 年以健康与福利实习生加入，在集团工作满 15 年，最近为中西部董事总经理兼区域销售主管，亦曾任芝加哥区域销售主管及三藩市驻点销售董事。[EN原文]"),
        "why": pair("整合管理办公室主管的设立通常对应大型收购的落地整合期，反映怡安正集中处理併购后的业务融合；大型经纪的整合动作往往伴随团队与客户关系变动，可作为人才流动的先行信号。"),
        "source": {"sc": "Reinsurance News 2026-10-16 报道（Aon 公布）",
                   "tc": "Reinsurance News 2026-10-16 報道（Aon 公布）",
                   "lang": "en", "name": "Reinsurance News", "date": "2026-10-16",
                   "note": "EN原文；含两宗委任与履历背景"},
        "tags": tlist(["Aon", "整合管理", "并购", "人事任命", "保险经纪"]),
        "actions": {"front": {},
                    "midback": pair("大型经纪整合与人才流动跟踪"),
                    "lead": pair("团队简报：经纪併购后整合"),
                    "cross": {}},
        "rolesImpact": {"front": 0, "midback": 1, "lead": 1, "cross": 0},
        "title": pair("怡安委任 Chris Rafferty 为整合管理办公室首席整合官　Steven Carleton 接任芝加哥主管"),
    },

    # ---------- govhk (official 84) ----------
    {
        "id": "govhk-mpf-full-portability-phase1-20261016",
        "publishedAt": "2026-10-16T11:00:00+08:00",
        "originalUrl": "https://www.info.gov.hk/gia/general/202610/16/P2026101500569.htm",
        "sourceKey": "govhk", "sourceTier": "official", "score": 84, "verifyStatus": "verified",
        "contentKind": "press", "clusterCount": 1,
        "boards": ["reg"],
        "themes": ["mpf", "full-portability", "pension", "legislation", "hong-kong"],
        "summary": pair("香港政府今日在宪报刊登《〈2025 年强制性公积金计划（一般）（修订）规例〉（生效日期）公告》，指定 12 月 21 日起实施修订规例，为强积金首阶段「全自由行」提供法律基础。2025 年 5 月 1 日或之后入职的新聘雇员，可选择每个公历年内一次（或在计划管限规则容许下每年多于一次），把现职雇主强制性供款产生的累算权益全数由雇主计划的供款帐户转至自选计划的个人帐户。财经事务及库务局局长许正宇表示已履行 2026 年《施政报告》年内落实首阶段「全自由行」的承诺，次阶段将惠及其余雇员，相关立法建议将于 2027 年年中提交立法会。政府 10 月 21 日向立法会提交公告，进行先订立后审议程序。[官方新聞稿]"),
        "why": pair("首阶段覆盖新聘雇员，等于把「转受托人」由离职时的一次性动作变成在职期间的年度选择，受托人与中介的客户黏性与产品竞争将重新洗牌；强积金配合自愿性供款与退休保障产品，成为前线可主动经营的题材。"),
        "source": {"sc": "香港特区政府新闻公报 2026-10-16（财经事务及库务局）",
                   "tc": "香港特區政府新聞公報 2026-10-16（財經事務及庫務局）",
                   "lang": "zh", "name": "香港政府新闻公报", "date": "2026-10-16",
                   "note": "官方新聞稿；含生效日期、适用范围与立法时间表"},
        "tags": tlist(["强积金", "全自由行", "退休保障", "条例", "香港"]),
        "actions": {"front": pair("MPF 客户转移选项沟通准备"),
                    "midback": pair("首阶段实施与次阶段立法跟踪"),
                    "lead": pair("团队简报：强积金全自由行"),
                    "cross": pair("退休规划产品组合素材")},
        "rolesImpact": {"front": 3, "midback": 3, "lead": 3, "cross": 1},
        "title": pair("强积金首阶段「全自由行」12 月 21 日实施　生效日期公告今日刊宪"),
    },

    # ---------- scmp (media 60) ----------
    {
        "id": "scmp-hk-investors-natixis-return-expectations-20261016",
        "publishedAt": "2026-10-16T07:00:00+08:00",
        "originalUrl": "https://www.scmp.com/business/markets/article/3371039/hong-kong-investors-most-eager-asia-beat-markets-temper-return-hopes-report",
        "sourceKey": "scmp", "sourceTier": "media", "score": 60, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["market"],
        "themes": ["investor-sentiment", "natixis", "return-expectations", "hong-kong", "wealth-management"],
        "summary": pair("法盛投资管理（Natixis Investment Managers）8 月调查显示，95% 香港受访者希望跑赢市场，比例为亚洲最高（亚洲平均 85%）；香港投资者预期长期回报较通胀高 12.3%，明显低于亚洲平均的 17.3%。调查访问香港、日本、新加坡、韩国及台湾共 750 名持有至少 10 万美元可投资资产的个人投资者。香港理财顾问提出的合理长期回报为 8.8%，投资者预期较此高 40%，落差较一年前的 16% 收窄，亦优于新加坡的 84% 与韩国的 110%。恒指 2025 年升约 28%，今年至今跌逾 8%；香港投资者最关注市场下行，其他亚洲市场则最关注通胀与利率。[EN原文]"),
        "why": pair("客户「想赢市场、但预期回报回落」的组合，正是保障与稳健收益产品切入的窗口；相比新加坡与韩国逾八成的预期落差，香港客户对回报的想像较贴近顾问基准，有利以风险管理而非高回报话术开展对话。"),
        "source": {"sc": "南华早报 2026-10-16 报道（引述 Natixis 调查）",
                   "tc": "南華早報 2026-10-16 報道（引述 Natixis 調查）",
                   "lang": "en", "name": "South China Morning Post", "date": "2026-10-16",
                   "note": "EN原文；含调查样本、回报预期与市场背景"},
        "tags": tlist(["投资者情绪", "Natixis", "回报预期", "香港", "财富管理"]),
        "actions": {"front": pair("客户预期管理对话素材"),
                    "midback": pair("投资者情绪与产品定位参考"),
                    "lead": pair("团队简报：客户回报预期"),
                    "cross": pair("家办客户资产配置参考")},
        "rolesImpact": {"front": 2, "midback": 1, "lead": 1, "cross": 2},
        "title": pair("调查：95% 香港投资者想跑赢市场　但预期回报低于亚洲平均"),
    },
]


def main():
    path = os.path.join(P, 'data/live-items.json')
    shutil.copy(path, os.path.join(P, 'data', f'live-items.json.bak-{STAMP}'))
    d = json.load(open(path, encoding='utf-8'))
    have = {it.get('id') for it in d['items']}
    urls = {it.get('originalUrl') for it in d['items']}
    new = []
    for it in ITEMS:
        if it['id'] in have:
            print('SKIP dup id:', it['id']); continue
        if it['originalUrl'] in urls:
            print('SKIP dup url:', it['id']); continue
        it.setdefault('featured', False)
        it.setdefault('evergreen', False)
        it.setdefault('contentRole', {"sc": "本站导读", "tc": "本站導讀"})
        it['ingestedAt'] = NOW
        new.append(it)
    new.sort(key=lambda x: x['publishedAt'], reverse=True)
    d['items'] = new + d['items']
    meta = d['meta']
    meta['generatedAt'] = NOW
    meta['itemCount'] = len(d['items'])
    meta['windowNote'] = {"sc": "本库%d条。" % len(d['items']), "tc": "本庫%d條。" % len(d['items'])}
    json.dump(d, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('inserted:', len(new), 'total:', len(d['items']))
    for it in new:
        print('  +', it['publishedAt'], '|', it['sourceKey'], '|', it['title']['sc'][:56])

    lc_path = os.path.join(P, 'data/last-check.json')
    shutil.copy(lc_path, os.path.join(P, 'data', f'last-check.json.bak-{STAMP}'))
    lc = json.load(open(lc_path, encoding='utf-8'))
    lc['lastCheck'] = NOW
    for k, v in lc.get('sources', {}).items():
        v['last'] = NOW
    json.dump(lc, open(lc_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('last-check updated:', len(lc.get('sources', {})), 'sources')


if __name__ == '__main__':
    main()
