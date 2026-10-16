#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-17 00:48 增量（补 10-16 21:08 时段的空档）：
窗口 = lastCheck 2026-10-16T18:08 → 2026-10-17T00:48。
新增：artemis 6 + reinsurancenews 6 + insurancebusinessmag 2 + scmp 1 + insuranceasianews 1（补漏）。
"""
import json, shutil, os
try:
    import zhconv
except Exception:
    zhconv = None
    print('WARN: zhconv missing, fallback no-conversion')

P = '/Users/leonliang/maoquanqingbao'
NOW = '2026-10-17T00:48:00+08:00'
STAMP = '1017-0048'


def t2(s):
    return zhconv.convert(s, 'zh-hant') if zhconv else s


def pair(s):
    return {'sc': s, 'tc': t2(s)}


def tlist(items):
    return {'sc': items, 'tc': [t2(x) for x in items]}


ITEMS = [
    # ---------- reinsurancenews (pro 72) ----------
    {
        "id": "rn-gallagher-re-apac-market-watch-2026-20261016",
        "publishedAt": "2026-10-17T00:00:00+08:00",
        "originalUrl": "https://www.reinsurancene.ws/apac-re-insurance-markets-face-shifting-risks-and-growth-pressures-gallagher-re/",
        "sourceKey": "reinsurancenews", "sourceTier": "pro", "score": 72, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["market", "insurer"],
        "themes": ["apac", "premium-growth", "emerging-risk", "cyber", "ai", "market-outlook"],
        "summary": pair("怡和再保（Gallagher Re）亚太区行政总裁 Roshan Perera 在即将发表的《APAC Market Watch 2026》报告中指出，区内 14 个主要市场 2025 年非寿险保费增长 5%，多数市场承保表现改善，但保费增长放缓；尽管面对经济与地缘压力，区内保险公司盈利与资本状况仍相对稳健。他点出事故及健康险、网络、人工智能与数据中心基建是新的保障需求来源，并认为组合分散、国际扩张与新兴风险是可持续增长的关键。[EN原文]"),
        "why": pair("亚太非寿险增长放缓但承保改善，需求增量转向健康、网络与 AI 相关风险；对香港团队而言，这些正是可与非寿险／专案型保障结合开展对话的方向，也是再保人视角的风向标。"),
        "source": {"sc": "Reinsurance News 2026-10-16 报道（引述 Gallagher Re 亚太区行政总裁）",
                   "tc": "Reinsurance News 2026-10-16 報道（引述 Gallagher Re 亞太區行政總裁）",
                   "lang": "en", "name": "Reinsurance News", "date": "2026-10-16",
                   "note": "EN原文；含 14 个市场保费增长与需求领域"},
        "tags": tlist(["Gallagher Re", "亚太市场", "保费增长", "网络保险", "新兴风险"]),
        "actions": {"front": {},
                    "midback": pair("亚太市场展望要点整理"),
                    "lead": pair("团队简报：亚太新需求领域"),
                    "cross": pair("客户对谈素材：新兴风险保障")},
        "rolesImpact": {"front": 0, "midback": 2, "lead": 2, "cross": 1},
        "title": pair("Gallagher Re：亚太保险市场面临风险迁移与增长压力"),
    },
    {
        "id": "rn-generali-syndicate-2031-red-bridge-20261016",
        "publishedAt": "2026-10-16T23:33:00+08:00",
        "originalUrl": "https://www.reinsurancene.ws/generali-advances-reinsurance-strategy-with-launch-of-syndicate-2031-red-bridge-at-lloyds/",
        "sourceKey": "reinsurancenews", "sourceTier": "pro", "score": 72, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 2,
        "boards": ["insurer", "market"],
        "themes": ["lloyds", "syndicates", "sidecar", "generali", "reinsurance-strategy", "alternative-capital"],
        "summary": pair("忠利（Generali）获劳合社原则性批准，设立辛迪加 2031「Red Bridge」，拟于 2027 年在劳合社平台开始承保。该辛迪加将承接集团部分外向分出再保业务，覆盖多个业务线，属侧车式（sidecar-like）结构，旨在拓宽风险资本来源、提升再保安排效率并强化与全球再保市场的长期合作。集团称其地域布局与分出业务类型提供差异化的分散效益，市场视之为另类资本与资本市场资金参与劳合社的又一入口。[EN原文]"),
        "why": pair("大型再保集团把再保安排搬到劳合社平台，反映资本效率竞争正在重塑再保通道；香港推动专属自保与 ILS 生态时，如何吸引这类资本与结构创新，是区域风险中心竞争的必答题。"),
        "source": {"sc": "Reinsurance News / Artemis 2026-10-16 报道（Generali 公布）",
                   "tc": "Reinsurance News / Artemis 2026-10-16 報道（Generali 公布）",
                   "lang": "en", "name": "Reinsurance News", "date": "2026-10-16",
                   "note": "EN原文；双源同题（Artemis 23:45 亦报道）；含原则性批准与 2027 年生效时点"},
        "tags": tlist(["Generali", "劳合社", "辛迪加", "侧车结构", "再保策略"]),
        "actions": {"front": {},
                    "midback": pair("再保资本结构动态跟踪"),
                    "lead": pair("团队简报：全球再保渠道"),
                    "cross": pair("家办另类风险资本参考")},
        "rolesImpact": {"front": 0, "midback": 1, "lead": 1, "cross": 2},
        "title": pair("忠利设劳合社辛迪加 2031「Red Bridge」　2027 年起承接集团分出业务"),
    },
    {
        "id": "rn-visionfund-amazon-basin-parametric-20261016",
        "publishedAt": "2026-10-16T23:00:00+08:00",
        "originalUrl": "https://www.reinsurancene.ws/visionfund-global-parametrics-to-develop-amazon-basin-parametric-cover/",
        "sourceKey": "reinsurancenews", "sourceTier": "pro", "score": 70, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["product", "market"],
        "themes": ["parametric-insurance", "climate-risk", "microinsurance", "latam", "development"],
        "summary": pair("世界宣明会金融普惠机构 VisionFund 与 Global Parametrics 合作、并由 InsuResilience Solutions Fund 共同出资，为世界宣明会在玻利维亚、巴西、哥伦比亚及秘鲁的办公室设计双灾因参数式中介保险（meso-insurance），以应对愈趋频密的水灾、旱灾等气候冲击，减少危机对家庭财务的挤压。方案将于 2026 年第四季启动，亚马逊流域模式同时作为复制样板，初期拟延伸至东南亚与南部非洲。[EN原文]"),
        "why": pair("参数式保险从巨灾债券走进基层气候保障，公共资金＋NGO＋私营技术方的组合正在成型；这类气候风险转移机制的设计经验，对亚洲新兴市场的农业与社区保障有直接借鉴价值。"),
        "source": {"sc": "Reinsurance News 2026-10-16 报道（VisionFund 与 Global Parametrics 公布）",
                   "tc": "Reinsurance News 2026-10-16 報道（VisionFund 與 Global Parametrics 公布）",
                   "lang": "en", "name": "Reinsurance News", "date": "2026-10-16",
                   "note": "EN原文；含双灾因设计与复制计划"},
        "tags": tlist(["参数式保险", "气候风险", "普惠保险", "Global Parametrics", "VisionFund"]),
        "actions": {"front": {},
                    "midback": pair("参数式产品设计参考"),
                    "lead": pair("团队简报：气候保障创新"),
                    "cross": pair("ESG／影响力投资参考")},
        "rolesImpact": {"front": 0, "midback": 2, "lead": 1, "cross": 1},
        "title": pair("VisionFund 与 Global Parametrics 开发亚马逊流域参数式保障"),
    },
    {
        "id": "rn-travelers-q3-2026-results-20261016",
        "publishedAt": "2026-10-16T21:00:00+08:00",
        "originalUrl": "https://www.reinsurancene.ws/travelers-q326-net-income-rises-despite-higher-cat-losses-but-9m-cat-toll-down-considerably/",
        "sourceKey": "reinsurancenews", "sourceTier": "pro", "score": 70, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["market"],
        "themes": ["earnings", "cat-losses", "reserve-development", "us", "pricing"],
        "summary": pair("Travelers 公布 2026 年第三季业绩：净利 19.17 亿美元（去年同期 18.88 亿），核心收入 19.47 亿美元，主要受惠于 2.34 亿美元税前有利的往年准备金发展（三个分部均为有利）及净投资收益增加，部分被巨灾损失上升抵销。季内净已实现投资亏损 3,400 万美元（税后 3,000 万），去年同期为收益 2,700 万美元。今年首九个月巨灾损失总额则显著低于同期。[EN原文]"),
        "why": pair("美国大型财产险商「准备金释放撑住利润、巨灾损失抬头但年内总额回落」的组合，是再保定价与费率周期转向的最新公司层面证据。"),
        "source": {"sc": "Reinsurance News 2026-10-16 报道（Travelers 第三季业绩）",
                   "tc": "Reinsurance News 2026-10-16 報道（Travelers 第三季業績）",
                   "lang": "en", "name": "Reinsurance News", "date": "2026-10-16",
                   "note": "EN原文；含净利、核心收入与准备金发展数据"},
        "tags": tlist(["Travelers", "第三季业绩", "准备金", "巨灾损失", "财产险"]),
        "actions": {"front": {},
                    "midback": pair("再保同业财务数据跟踪"),
                    "lead": pair("团队简报：公司层面费率信号"),
                    "cross": {}},
        "rolesImpact": {"front": 0, "midback": 2, "lead": 1, "cross": 0},
        "title": pair("Travelers 第三季净利 19.17 亿美元　巨灾损失上升但首九个月总额回落"),
    },
    {
        "id": "rn-marsh-re-baden-baden-janeke-20261016",
        "publishedAt": "2026-10-16T20:30:00+08:00",
        "originalUrl": "https://www.reinsurancene.ws/marsh-res-janeke-expects-baden-baden-to-entrench-buyer-favourable-reinsurance-market/",
        "sourceKey": "reinsurancenews", "sourceTier": "pro", "score": 70, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["market"],
        "themes": ["reinsurance-renewals", "baden-baden", "pricing", "capacity", "broker-view"],
        "summary": pair("达信再保（Marsh Re）英国财产及意外险与伦敦欧洲主管 Leon Janeke 在巴登巴登会议前接受访问，预期会议将「确认并进一步巩固」1 月续保前对买方有利的再保市场。他指出再保人承担的已发生损失份额由 2023 年约 20% 降至约 12%，但预期 2027 年回升；市场因资本充裕而竞争，再保人愿与分出人更广泛合作，但强调并非「不计代价的增长」。[EN原文]"),
        "why": pair("续保季节前的买方市场延续，代表分出成本压力可控；对依赖再保安排的产品定价与承保能力是利好背景，也是观察 2027 年费率拐点的关键窗口。"),
        "source": {"sc": "Reinsurance News 2026-10-16 报道（专访 Marsh Re）",
                   "tc": "Reinsurance News 2026-10-16 報道（專訪 Marsh Re）",
                   "lang": "en", "name": "Reinsurance News", "date": "2026-10-16",
                   "note": "EN原文；含再保人损失份额 20%→12% 数据"},
        "tags": tlist(["再保续保", "巴登巴登", "买方市场", "Marsh Re", "费率"]),
        "actions": {"front": {},
                    "midback": pair("续保季节行情跟踪"),
                    "lead": pair("团队简报：续保市场展望"),
                    "cross": {}},
        "rolesImpact": {"front": 0, "midback": 2, "lead": 2, "cross": 0},
        "title": pair("Marsh Re：巴登巴登会议将进一步巩固买方有利的再保市场"),
    },
    {
        "id": "rn-coalition-ai-cyber-escalation-20261016",
        "publishedAt": "2026-10-16T20:00:00+08:00",
        "originalUrl": "https://www.reinsurancene.ws/ai-driven-incidents-will-escalate-in-frequency-once-attackers-find-the-right-business-model-coalition/",
        "sourceKey": "reinsurancenews", "sourceTier": "pro", "score": 72, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["tech", "market"],
        "themes": ["cyber-insurance", "ai-risk", "accumulation", "underwriting", "systemic-risk"],
        "summary": pair("网络险专业机构 Coalition 认为，网络风险可多年持平，一旦攻击者找到利用新技术的可行商业模式便会急升，人工智能或循同一路径。业界网络险承保额度合计接近 1 万亿美元，承保人面对两类威胁：攻击频率与严重程度持续攀升，或单一事件同时冲击大量被保险人。报道亦回顾 2026 年 9 月 Anthropic 行政总裁警告 AI 集群可在一年内接管「整个互联网」，并获 OpenAI 与 xAI 高层附和。[EN原文]"),
        "why": pair("AI 相关网络风险从技术议题变为承保与累积风险议题；客户端的网络保障缺口、除外责任与保单措辞理解，将成为前线需要说清楚的内容。"),
        "source": {"sc": "Reinsurance News 2026-10-16 报道（引述 Coalition 观点）",
                   "tc": "Reinsurance News 2026-10-16 報道（引述 Coalition 觀點）",
                   "lang": "en", "name": "Reinsurance News", "date": "2026-10-16",
                   "note": "EN原文；含网络险承保额度与两类威胁框架"},
        "tags": tlist(["网络保险", "人工智能风险", "累积风险", "承保", "Coalition"]),
        "actions": {"front": pair("客户网络保障对话素材"),
                    "midback": pair("网络险承保条件跟踪"),
                    "lead": pair("团队简报：AI 与网络风险"),
                    "cross": pair("家办风险管理参考")},
        "rolesImpact": {"front": 1, "midback": 2, "lead": 2, "cross": 1},
        "title": pair("Coalition：攻击者找到商业模式后　AI 驱动事故频率将急升"),
    },
    {
        "id": "rn-credeq-syndicate-1998-lloyds-approval-20261016",
        "publishedAt": "2026-10-16T19:30:00+08:00",
        "originalUrl": "https://www.reinsurancene.ws/credeq-syndicate-1998-receives-lloyds-in-principle-approval/",
        "sourceKey": "reinsurancenews", "sourceTier": "pro", "score": 70, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["reg", "market"],
        "themes": ["lloyds", "credit-risk", "syndicate", "approval", "trade-credit"],
        "summary": pair("劳合社向总部设于伦敦的专业信用风险保险人 Credeq 发出原则性批准，准许其设立辛迪加 1998，预计在完成余下实施要求并取得最终承保许可后于 2027 年 1 月 1 日开始承保。该辛迪加将聚焦信用风险保险、保证再保及欧洲专项贸易信用，为 Credeq 现有信用风险业务提供额外且策略对齐的承保能力。Credeq 业务覆盖英国、欧洲、非洲、澳洲及新西兰，并涉足 AI 风险。[EN原文]"),
        "why": pair("信用险与保证险在劳合社扩产，反映贸易信用与 AI 责任等新风险正被制度化承保；对做贸易融资相关客户的风险顾问，是保障工具供给增加的信号。"),
        "source": {"sc": "Reinsurance News 2026-10-16 报道（劳合社批准 Credeq）",
                   "tc": "Reinsurance News 2026-10-16 報道（勞合社批准 Credeq）",
                   "lang": "en", "name": "Reinsurance News", "date": "2026-10-16",
                   "note": "EN原文；含 2027-01-01 承保时点与业务范围"},
        "tags": tlist(["劳合社", "信用风险保险", "保证再保", "Credeq", "承保能力"]),
        "actions": {"front": {},
                    "midback": pair("信用与保证险承保能力跟踪"),
                    "lead": pair("团队简报：劳合社新增产能"),
                    "cross": pair("贸易融资客户风险参考")},
        "rolesImpact": {"front": 0, "midback": 2, "lead": 1, "cross": 1},
        "title": pair("Credeq 获劳合社原则性批准设辛迪加 1998　2027 年起承保信用风险"),
    },
    # ---------- artemis (pro 70) ----------
    {
        "id": "artemis-lloyds-broker-originated-guidance-20261016",
        "publishedAt": "2026-10-16T22:52:00+08:00",
        "originalUrl": "https://www.artemis.bm/news/lloyds-issues-guidance-and-expectations-for-broker-originated-reinsurance-structures/",
        "sourceKey": "artemis", "sourceTier": "pro", "score": 70, "verifyStatus": "verified",
        "contentKind": "circular", "clusterCount": 1,
        "boards": ["reg", "market"],
        "themes": ["lloyds", "broker-structures", "alternative-capital", "guidance", "approval"],
        "summary": pair("劳合社发出指引，说明其对经纪主导再保结构的期望、做法与审批要求，并认为这类结构的需求将日益增加。此举紧接怡安（Aon）与黑石（Blackstone）合作（市场称代号 Cortina）的消息——该策略拟由资产管理人支持怡安在劳合社所经纪业务的一部分份额，显示资产管理人与资本市场对分散化保险与再保回报的兴趣正上升。[EN原文]"),
        "why": pair("中介主导的资本结构规范化，意味着资本、经纪与承保人角色重新划分；香港发展 ILS 与专属自保时，中介在资本结构中的定位与披露要求需要同步落地。"),
        "source": {"sc": "Artemis 2026-10-16 报道（劳合社指引）",
                   "tc": "Artemis 2026-10-16 報道（勞合社指引）",
                   "lang": "en", "name": "Artemis", "date": "2026-10-16",
                   "note": "EN原文；含审批框架与 Aon／Blackstone 背景"},
        "tags": tlist(["劳合社", "经纪结构", "资产管理人", "监管指引", "怡安"]),
        "actions": {"front": {},
                    "midback": pair("资本结构监管框架跟踪"),
                    "lead": pair("团队简报：中介与资本角色"),
                    "cross": pair("家办资本参与渠道参考")},
        "rolesImpact": {"front": 0, "midback": 1, "lead": 1, "cross": 2},
        "title": pair("劳合社就经纪主导再保结构发指引　资产管理者入场通道明确化"),
    },
    {
        "id": "artemis-moodys-rms-isaias-loss-estimate-20261016",
        "publishedAt": "2026-10-16T21:56:00+08:00",
        "originalUrl": "https://www.artemis.bm/news/moodys-estimates-insured-losses-from-hurricane-isaias-in-2-5bn-to-4-5bn-range/",
        "sourceKey": "artemis", "sourceTier": "pro", "score": 70, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 2,
        "boards": ["market"],
        "themes": ["catastrophe-risk", "hurricane", "insured-losses", "us", "risk-modelling"],
        "summary": pair("穆迪 RMS Event Response 首次估算飓风 Isaias 对美国私营市场造成的保险损失介于 25 亿至 45 亿美元，最可能（最佳估算）为 35 亿，涵盖风灾、风暴潮与降水引发的内陆水灾，其中风灾占多数；风暴潮、内陆水灾及美国国家洪水保险计划（NFIP）相关损失合计仅约 2.5 亿美元。估算包括住宅、商业、工业、汽车及船只的财产损失与营业中断，并计入灾后损失放大效应。[EN原文]"),
        "why": pair("巨灾损失的行业估算直接进入再保与 ILS 定价模型；与日前另一家机构的同类估算并列观察，可掌握市场对同一事件的分歧幅度。"),
        "source": {"sc": "Artemis 2026-10-16 报道（穆迪 RMS 估算）",
                   "tc": "Artemis 2026-10-16 報道（穆迪 RMS 估算）",
                   "lang": "en", "name": "Artemis", "date": "2026-10-16",
                   "note": "EN原文；双源同题（Reinsurance News 22:00 亦报道）"},
        "tags": tlist(["飓风 Isaias", "巨灾损失", "穆迪 RMS", "风险模型", "美国"]),
        "actions": {"front": {},
                    "midback": pair("巨灾损失估算与定价跟踪"),
                    "lead": pair("团队简报：巨灾事件影响"),
                    "cross": {}},
        "rolesImpact": {"front": 0, "midback": 2, "lead": 1, "cross": 0},
        "title": pair("穆迪 RMS 估飓风 Isaias 保险损失 25–45 亿美元　最佳估算 35 亿"),
    },
    {
        "id": "artemis-safepoint-nature-coast-re-2026-2-20261016",
        "publishedAt": "2026-10-16T20:55:00+08:00",
        "originalUrl": "https://www.artemis.bm/news/safepoint-targets-250m-nature-coast-re-2026-2-cat-bond-for-broadest-coverage-yet/",
        "sourceKey": "artemis", "sourceTier": "pro", "score": 70, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["market"],
        "themes": ["ils", "cat-bond", "named-storm", "us-property", "capital-markets"],
        "summary": pair("美国 SafePoint Insurance Company 再度进入巨灾债券市场，初步目标为通过 Nature Coast Re Ltd.（2026-2 系列）取得 2.5 亿美元多年期命名风暴再保保障，覆盖美国州份范围为其历来最广。该公司 2025 年发行两笔共 3.5 亿美元，2026 年 2 月已发行 2026-1 系列的 2.5 亿美元，本次持续以资本市场资金支持业务扩张。[EN原文]"),
        "why": pair("同一发起人连年增发、覆盖面扩大，显示中小型财产险商正把资本市场作为常规承保能力来源；对香港建设 ILS 市场而言，这类地方性发起人是潜在的可争取需求。"),
        "source": {"sc": "Artemis 2026-10-16 报道（Nature Coast Re 2026-2）",
                   "tc": "Artemis 2026-10-16 報道（Nature Coast Re 2026-2）",
                   "lang": "en", "name": "Artemis", "date": "2026-10-16",
                   "note": "EN原文；含发行目标、历年发行记录"},
        "tags": tlist(["巨灾债券", "ILS", "命名风暴", "SafePoint", "资本市场"]),
        "actions": {"front": {},
                    "midback": pair("ILS 发行案例跟踪"),
                    "lead": pair("团队简报：资本市场承接风险"),
                    "cross": pair("家办 ILS 资产参考")},
        "rolesImpact": {"front": 0, "midback": 1, "lead": 1, "cross": 2},
        "title": pair("SafePoint 拟发 2.5 亿美元 Nature Coast Re 2026-2 巨灾债券　覆盖面历来最广"),
    },
    {
        "id": "artemis-777-wander-guilty-plea-20261016",
        "publishedAt": "2026-10-16T19:47:00+08:00",
        "originalUrl": "https://www.artemis.bm/news/777-co-founder-wander-pleads-guilty-to-500m-scheme-to-defraud-lenders-and-investors/",
        "sourceKey": "artemis", "sourceTier": "pro", "score": 70, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["market"],
        "themes": ["fraud", "litigation", "ils-collateral", "due-diligence", "enforcement"],
        "summary": pair("投资公司 777 Partners 联合创办人 Josh Wander 就电汇欺诈及证券欺诈认罪，涉及逾 5 亿美元诈骗贷款人与投资者的计划，并同意没收至少 5 亿美元所得，由纽约南区联邦检察官公布。美国证券交易委员会早前已对公司及创办人提诉，指其不当使用资金与抵押品，包括把本应为贷款工具提供担保的资产重复质押。[EN原文]"),
        "why": pair("抵押品重复质押正是 ILS 与私人再保结构最敏感的尽调风险点；此案有助理解为什么机构在配置另类风险资产时，会把资产隔离与抵押品查验放在首位。"),
        "source": {"sc": "Artemis 2026-10-16 报道（美国司法部公布）",
                   "tc": "Artemis 2026-10-16 報道（美國司法部公布）",
                   "lang": "en", "name": "Artemis", "date": "2026-10-16",
                   "note": "EN原文；含认罪罪名与没收金额"},
        "tags": tlist(["欺诈", "抵押品", "尽调", "ILS", "执法"]),
        "actions": {"front": {},
                    "midback": pair("另类资产抵押品风险案例"),
                    "lead": pair("团队简报：结构与尽调风险"),
                    "cross": pair("家办投资尽调警示素材")},
        "rolesImpact": {"front": 0, "midback": 1, "lead": 1, "cross": 1},
        "title": pair("777 Partners 联合创办人 Wander 认罪　涉逾 5 亿美元欺诈贷款人与投资者"),
    },
    {
        "id": "artemis-allstate-september-cat-losses-20261016",
        "publishedAt": "2026-10-16T18:30:00+08:00",
        "originalUrl": "https://www.artemis.bm/news/allstate-reports-220m-september-pre-tax-cat-losses-taking-aggregate-year-to-3-37bn/",
        "sourceKey": "artemis", "sourceTier": "pro", "score": 70, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["market"],
        "themes": ["cat-losses", "cat-bonds", "us-property", "aggregate-retention", "earnings"],
        "summary": pair("美国 Allstate 公布 2026 年 9 月税前巨灾损失为 2.2 亿美元，较前数月明显回落，令其巨灾债券年度累计风险期（4 月起算）的累计损失升至 33.72 亿美元。Artemis 提醒并非所有巨灾损失都会符合条件侵蚀债券的累计自留额，实际触发情况仍取决于事件计入规则。[EN原文]"),
        "why": pair("单一大型财产险商的累计损失轨迹，是判断巨灾债券自留额何时被击穿的关键输入；对关注 ILS 触发风险的资金方与中介属高频跟踪数据。"),
        "source": {"sc": "Artemis 2026-10-16 报道（Allstate 月度披露）",
                   "tc": "Artemis 2026-10-16 報道（Allstate 月度披露）",
                   "lang": "en", "name": "Artemis", "date": "2026-10-16",
                   "note": "EN原文；含单月损失与累计 33.72 亿美元"},
        "tags": tlist(["Allstate", "巨灾损失", "巨灾债券", "累计自留额", "美国财产险"]),
        "actions": {"front": {},
                    "midback": pair("巨灾债券触发风险跟踪"),
                    "lead": pair("团队简报：ILS 触发观察"),
                    "cross": {}},
        "rolesImpact": {"front": 0, "midback": 2, "lead": 1, "cross": 1},
        "title": pair("Allstate 9 月巨灾损失 2.2 亿美元　巨灾债券年度累计升至 33.72 亿"),
    },
    # ---------- insurancebusinessmag (media 62) ----------
    {
        "id": "ibm-axa-mental-health-survey-20261016",
        "publishedAt": "2026-10-16T22:27:00+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/life-insurance/eight-in-10-workers-would-use-workplace-mental-health-support-but-twothirds-lack-access-axa-finds-593858.aspx",
        "sourceKey": "insurancebusinessmag", "sourceTier": "media", "score": 62, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["product", "market"],
        "themes": ["health-insurance", "mental-health", "employee-benefits", "survey", "ai-in-health"],
        "summary": pair("保险商业杂志引述安盛（AXA）在 18 个国家、1.9 万人所做的调查：八成在职人士愿意使用雇主提供的心理健康支援，但三分之二表示难以取得相关渠道；三分之一因费用问题未能寻求专业协助。调查又指在服务障碍最高的群体中，人工智能工具正在填补空缺。[EN原文]"),
        "why": pair("雇员福利与心理健康保障需求明确但供给不足，是企业团险与个人健康险的切入场景；AI 作为「替代性入口」的出现，也牵动未来保障设计与核保数据收集方式。"),
        "source": {"sc": "Insurance Business 2026-10-16 报道（引述 AXA 调查）",
                   "tc": "Insurance Business 2026-10-16 報道（引述 AXA 調查）",
                   "lang": "en", "name": "Insurance Business", "date": "2026-10-16",
                   "note": "EN原文；样本 18 国 1.9 万人"},
        "tags": tlist(["AXA", "心理健康", "雇员福利", "健康保险", "调查"]),
        "actions": {"front": pair("企业客户健康福利对话素材"),
                    "midback": pair("健康险需求与产品设计参考"),
                    "lead": pair("团队简报：心理健康保障缺口"),
                    "cross": {}},
        "rolesImpact": {"front": 2, "midback": 1, "lead": 1, "cross": 0},
        "title": pair("AXA 调查：八成在职者愿用职场心理健康支援　三分之二难获渠道"),
    },
    {
        "id": "ibm-marsh-talent-poaching-30m-20261016",
        "publishedAt": "2026-10-16T18:59:00+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/poaching-wars-marsh-spends-us30m-in-a-quarter-fighting-rivals-over-staff-593832.aspx",
        "sourceKey": "insurancebusinessmag", "sourceTier": "media", "score": 62, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["insurer", "market"],
        "themes": ["talent", "brokers", "asia-expansion", "howden", "competition"],
        "summary": pair("Insurance Business 报道，经纪巨头达信（Marsh）单季花费 3,000 万美元应对同业高薪挖角，反映经纪行业人才争夺战升级；报道指 Howden 正从 Marsh 等竞争对手延揽资深人员，以扩充其亚洲团队。Marsh 选择以高成本投入守住团队，而非让人员自然流失。[EN原文]"),
        "why": pair("国际经纪在亚洲抢人才，直接改变前线团队的薪酬预期与流动节奏；对正在建立复制型团队的机构，是人才成本与留任策略的现实参照。"),
        "source": {"sc": "Insurance Business 2026-10-16 报道",
                   "tc": "Insurance Business 2026-10-16 報道",
                   "lang": "en", "name": "Insurance Business", "date": "2026-10-16",
                   "note": "EN原文；含单季投入金额与 Howden 亚洲扩张"},
        "tags": tlist(["Marsh", "Howden", "人才流动", "亚洲扩张", "经纪"]),
        "actions": {"front": {},
                    "midback": pair("同业人才与团队动态跟踪"),
                    "lead": pair("团队简报：人才竞争与留任"),
                    "cross": {}},
        "rolesImpact": {"front": 0, "midback": 2, "lead": 2, "cross": 0},
        "title": pair("抢人大战：Marsh 单季斥资 3,000 万美元应对同业挖角"),
    },
    # ---------- scmp (media 60) ----------
    {
        "id": "scmp-hkex-t1-settlement-delay-2028-20261016",
        "publishedAt": "2026-10-16T18:19:00+08:00",
        "originalUrl": "https://www.scmp.com/business/markets/article/3371176/hkex-pushes-back-t1-trade-settlement-2028-after-brokers-request-more-prep-time",
        "sourceKey": "scmp", "sourceTier": "media", "score": 60, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["market"],
        "themes": ["hkex", "settlement", "market-infrastructure", "brokers", "operations"],
        "summary": pair("南华早报报道，香港交易所把缩短股票交易结算周期的 T+1 计划推迟至 2028 年下半年实施，以回应业界普遍要求更多准备时间。港交所原本希望在更早时间落地，市场关注对券商与基金营运流程、资金周转与后台系统的连带影响。[EN原文]"),
        "why": pair("结算周期是市场基础设施的底层改动，牵动券商现金流与营运安排；对以交收效率为卖点的投资平台与产品结构，是需要重新评估的时间表。"),
        "source": {"sc": "南华早报 2026-10-16 报道（港交所公布）",
                   "tc": "南華早報 2026-10-16 報道（港交所公布）",
                   "lang": "en", "name": "South China Morning Post", "date": "2026-10-16",
                   "note": "EN原文；含推迟至 2028 年下半年"},
        "tags": tlist(["港交所", "T+1", "结算周期", "市场基建", "营运"]),
        "actions": {"front": {},
                    "midback": pair("市场基建时间表跟踪"),
                    "lead": pair("团队简报：交收效率变动"),
                    "cross": pair("家办营运安排参考")},
        "rolesImpact": {"front": 0, "midback": 1, "lead": 1, "cross": 1},
        "title": pair("港交所把 T+1 结算推迟至 2028 年　回应业界要求更多准备时间"),
    },
    # ---------- insuranceasianews（补 10-16 18:08 时段漏采，pro 70） ----------
    {
        "id": "ian-apac-people-moves-week-20261016",
        "publishedAt": "2026-10-16T17:06:00+08:00",
        "originalUrl": "https://insuranceasianews.com/zurich-allianz-jd-howden-mclarens-8-apac-insurance-people-moves-of-the-week/",
        "sourceKey": "insuranceasianews", "sourceTier": "pro", "score": 70, "verifyStatus": "pending",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["insurer"],
        "themes": ["appointments", "apac", "leadership", "people-moves"],
        "summary": pair("InsuranceAsia News 汇总本周亚太区保险业八宗人事变动，涉及苏黎世（Zurich）、安联京东（Allianz JD）、Howden 及 McLarens 等机构，涵盖核保、财务与高管层调整。该栏目每周整理区内承保人、经纪与理赔服务商的人事更替，是追踪竞争对手团队与业务方向的高效来源。[EN原文]"),
        "why": pair("人事变动往往先于业务策略调整出现；对需要掌握同业团队动向与人才市场的机构，这类每周汇总比单条任命更具结构价值。"),
        "source": {"sc": "InsuranceAsia News 2026-10-16 报道（本周人事汇总）",
                   "tc": "InsuranceAsia News 2026-10-16 報道（本週人事匯總）",
                   "lang": "en", "name": "InsuranceAsia News", "date": "2026-10-16",
                   "note": "EN原文；该文 17:06 发布，属上一时段漏采补录"},
        "tags": tlist(["人事变动", "亚太", "高管任命", "同业动态"]),
        "actions": {"front": {},
                    "midback": pair("同业人事与组织动态跟踪"),
                    "lead": pair("团队简报：区內人事变动"),
                    "cross": {}},
        "rolesImpact": {"front": 0, "midback": 1, "lead": 1, "cross": 0},
        "title": pair("本周亚太保险人事变动　涉 Zurich、Allianz JD、Howden、McLarens 等八宗"),
    },
]


def main():
    path = os.path.join(P, 'data/live-items.json')
    shutil.copy(path, os.path.join(P, 'data', 'live-items.json.bak-%s' % STAMP))
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
    shutil.copy(lc_path, os.path.join(P, 'data', 'last-check.json.bak-%s' % STAMP))
    lc = json.load(open(lc_path, encoding='utf-8'))
    lc['lastCheck'] = NOW
    for k, v in lc.get('sources', {}).items():
        v['last'] = NOW
    json.dump(lc, open(lc_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('last-check updated:', len(lc.get('sources', {})), 'sources')


if __name__ == '__main__':
    main()
