#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 2026-10-13 18:08 increment into live-items.json.

窗口：2026-10-13T00:46（上轮）→ 2026-10-13T18:08（本轮）。
本期新增 14 条：
  insuranceasianews 5（日本資產密集型再保新規／蘇黎世大中華 CFO／新韓收購樂天保險／
                        Aon-EBRD 烏克蘭戰爭風險／Pacific Life Re 日本第二宗結構性再保）
  insurancebusinessmag 5（Atrium 晶片廠資產申報／前 Chubb 澳新高管申索／
                          APAC 醫療成本 2027 放緩／旅遊保險年齡分層／數據中心累積風險）
  artemis 2（Aon：captive 演變為資本平台／颶風 Isaias 損失 20-40 億美元）
  asiainsurancereview 2（標普：香港五年規劃機遇／香港壽險未來兩年 5-10% 增長）
无新发布信源：IA（通函最新 2026-10-02；新闻稿页无新增）、HKMA（最新 2026-10-08）、
  AIA（最新 10-09）、Manulife HK（最新 10-10，已收录）、Prudential HK（最新 10-04）、
  AXA HK（最新 10-08）、Sun Life HK（最新 10-02）、SCMP 保险专题（最新 10-07）、
  NFRA（最新 10-09）、govhk（10-13 有多条但无保险相关）、insuranceasia.com（今日头条
  均为 10-12 已收录条目）、HKFI、FSTB（无新）。
"""
import json
from datetime import datetime, timezone, timedelta

try:
    import zhconv
    def T(s):
        return zhconv.convert(s, 'zh-hant')
except Exception:  # pragma: no cover
    def T(s):
        return s

NOW = datetime.now(timezone(timedelta(hours=8))).strftime('%Y-%m-%dT%H:%M:%S+08:00')
CR = {"sc": "本站导读", "tc": "本站導讀"}


def mk(id_, sourceKey, tier, kind, pub, url, t, s, w, a_f, a_m, a_l, a_c, ri, boards, themes,
       tags, src, lang, score, verify='pending'):
    return {
        "clusterCount": 1, "score": score, "verifyStatus": verify,
        "sourceTier": tier, "sourceKey": sourceKey, "contentKind": kind,
        "actions": {
            "front": {"sc": a_f, "tc": T(a_f)},
            "midback": {"sc": a_m, "tc": T(a_m)},
            "lead": {"sc": a_l, "tc": T(a_l)},
            "cross": {"sc": a_c, "tc": T(a_c)},
        },
        "rolesImpact": {"front": ri[0], "midback": ri[1], "lead": ri[2], "cross": ri[3]},
        "boards": boards, "themes": themes,
        "tags": {"sc": tags, "tc": [T(x) for x in tags]},
        "contentRole": CR, "featured": False, "evergreen": False, "ingestedAt": NOW,
        "id": id_, "publishedAt": pub, "originalUrl": url,
        "title": {"sc": t, "tc": T(t)},
        "summary": {"sc": s, "tc": T(s)},
        "why": {"sc": w, "tc": T(w)},
        "source": {"sc": src[0], "tc": T(src[0]), "lang": lang, "name": src[1],
                   "date": src[2], "note": src[3] if len(src) > 3 else None},
    }


ITEMS = []

# ══ 1. 日本收緊資產密集型再保規則（惠譽） ══
ITEMS.append(mk(
    "ian-japan-asset-intensive-reinsurance-rules-fitch-20261013",
    "insuranceasianews", "pro", "news",
    "2026-10-13T18:05:27+08:00",
    "https://insuranceasianews.com/japan-asset-intensive-reinsurance-rules-to-drive-capital-strain-recapture-risk-fitch/",
    "日本收紧资产密集型再保险规则　惠誉：或带来资本压力与风险再捕捉　同时解禁代理与经纪合作",
    "InsuranceAsia News 于10月13日报道，惠誉（Fitch）指出日本金融厅（FSA）正收紧资产密集型再保险（asset-intensive reinsurance）相关规则，以遏制保险人对再保交易对手的风险敞口，并可能带来资本压力与风险再捕捉（risk recapture）问题；报道同时提到，FSA 已解除长期禁止保险经纪与代理合作推广的限制，以鼓励更广泛使用经纪渠道。 [EN原文]",
    "资产密集型再保是近年亚太寿险（含日本、香港分红／万能产品）提升资本效率的主要工具之一。监管口径一旦在亚洲扩散，会直接影响高保证产品的资本成本、再保可行性与定价假设，是理解「同业产品为何这样设计」的前置背景，也是与分行／管理层面谈产品可持续性时的硬资料。",
    "与客户谈产品可持续性时的监管环境参照",
    "资产密集型再保与资本效率基础补强",
    "团队简报：亚洲再保监管趋势",
    "香港与日本再保监管取向对照",
    (1, 2, 3, 2), ["reg", "market"], ["reinsurance", "capital", "regulation", "japan"],
    ["惠誉", "日本金融厅", "资产密集型再保险", "资本效率", "经纪渠道"],
    ("InsuranceAsia News 2026-10-13 报道", "InsuranceAsia News", "2026-10-13",
     "EN原文；付费墙，事实来自官网导语"),
    "en", 72, "verified"))

# ══ 2. 苏黎世委任大中华区 CFO ══
ITEMS.append(mk(
    "ian-zurich-martin-noble-greater-china-cfo-20261013",
    "insuranceasianews", "pro", "news",
    "2026-10-13T17:48:16+08:00",
    "https://insuranceasianews.com/zurich-appoints-martin-noble-to-expanded-role-as-greater-china-cfo/",
    "蘇黎世委任香港首席財務官 Martin Noble 兼任大中華區 CFO",
    "10月13日报道，苏黎世保险（Zurich）将现任香港首席财务官 Martin Noble 的职责扩展至大中华区CFO，他在该集团已任职近13年，并曾担任多个高层财务职位。此举反映苏黎世整合大中华区财务管理、加强区域协同的取向。 [EN原文]",
    "港险市场的外资人事布局往往先于业务动作：区域 CFO 权责扩大，通常对应跨市场资本配置、费用与合规口径统一。可作为观察外资在香港与大中华区定位变化的低成本信号。",
    "团队分享：外资保险公司区域布局动向",
    "公司治理与区域财务职能常识",
    "人事变动作为业务信号的情报读法",
    "外资在港区域总部角色讨论",
    (1, 1, 2, 1), ["insurer", "market"], ["people", "insurer-strategy", "greater-china"],
    ["苏黎世", "人事任命", "大中华区", "首席财务官"],
    ("InsuranceAsia News 2026-10-13 报道", "InsuranceAsia News", "2026-10-13",
     "EN原文；付费墙，事实来自官网导语"),
    "en", 62, "verified"))

# ══ 3. 新韩金融收购乐天保险 77% ══
ITEMS.append(mk(
    "ian-shinhan-lotte-insurance-516m-20261013",
    "insuranceasianews", "pro", "news",
    "2026-10-13T15:15:36+08:00",
    "https://insuranceasianews.com/shinhan-agrees-us516m-deal-for-controlling-stake-in-lotte-insurance/",
    "韓國新韓金融以 5.16 億美元收購樂天保險 77% 控股權　私募股東退出",
    "10月13日报道，韩国新韩金融集团与私募基金股东 JKL Partners 签署协议，以约5.16亿美元收购非寿险公司乐天保险（Lotte Insurance）77%股权，取得控股权。该交易为韩国保险业年内规模较大的并购之一，反映当地产险板块在新资本要求下加速整合。 [EN原文]",
    "亚洲保险业并购与私募退出路径，是判断区域市场成熟度与资本流向的观察面。对香港的意义在于对照：本地近年以迁册、再保与银保合作为主，而韩国走「金控并入＋私募退出」路线，两者可作区域资本配置讨论的对照案例。",
    "区域并购动态作为市场成熟度参照",
    "并购与股权结构基础概念",
    "行业整合趋势简报素材",
    "亚太保险资本流动对照",
    (0, 1, 2, 2), ["market", "insurer"], ["m&a", "non-life", "korea", "private-equity"],
    ["新韩金融", "乐天保险", "并购", "韩国", "私募退出"],
    ("InsuranceAsia News 2026-10-13 报道", "InsuranceAsia News", "2026-10-13",
     "EN原文；付费墙，事实来自官网导语"),
    "en", 64, "verified"))

# ══ 4. Aon 与 EBRD 扩大乌克兰战争风险安排 ══
ITEMS.append(mk(
    "ian-aon-ebrd-ukraine-war-risk-facility-168m-20261013",
    "insuranceasianews", "pro", "news",
    "2026-10-13T15:12:06+08:00",
    "https://insuranceasianews.com/aon-ebrd-expand-ukraine-war-risk-facility-to-us168m-as-ms-amlin-adds-capacity/",
    "Aon 與 EBRD 擴大烏克蘭戰爭風險保險安排至 1.68 億美元　MS Amlin 加碼承保",
    "10月13日报道，Aon 与欧洲复兴开发银行（EBRD）将乌克兰战争风险保险机制规模扩大至1.68亿美元；劳合社承保人 MS Amlin 作为该机制2025年3月启动时的首家再保人，把支持额度提高至1.45亿美元，另有两家乌克兰本地保险公司加入。 [EN原文]",
    "战争与政治风险的市场化承接能力，是理解「不可保风险如何被结构化承保」的典型案例：多边机构＋劳合社＋本地保险人的分层设计，可作为向企业客解释政治风险、供应链中断与再保容量如何组合的参照。",
    "与客户谈不可保风险时的机制参照",
    "政治风险与再保分层基础知识",
    "团队分享：地缘风险承保机制",
    "跨境经营风险保障与国际组织角色",
    (0, 1, 2, 2), ["market", "product"], ["political-risk", "reinsurance", "war-risk", "capacity"],
    ["Aon", "EBRD", "战争风险", "乌克兰", "MS Amlin"],
    ("InsuranceAsia News 2026-10-13 报道", "InsuranceAsia News", "2026-10-13",
     "EN原文；付费墙，事实来自官网导语"),
    "en", 60, "verified"))

# ══ 5. Pacific Life Re 日本第二宗结构性再保 ══
ITEMS.append(mk(
    "ian-pacific-life-re-japan-structured-reinsurance-20261013",
    "insuranceasianews", "pro", "news",
    "2026-10-13T13:35:30+08:00",
    "https://insuranceasianews.com/pacific-life-re-seals-second-japan-structured-reinsurance-deal-of-2026/",
    "Pacific Life Re 完成 2026 年第二宗日本結構性再保險交易　配合 ESR 新資本框架",
    "10月13日报道，Pacific Life Re 与一家未具名的大型日本寿险公司完成今年第二宗日本结构性再保险交易，交易设计用于在日本新经济价值偿付能力（ESR）框架下优化资本效率。该行交易反映日本寿险业在新资本制度下持续透过结构性再保释放资本、调整资产负债匹配。 [EN原文]",
    "结构性再保是新偿付能力制度下的标准资本工具。理解「监管资本框架改变 → 再保结构改变 → 产品定价与保证水平改变」这条传导链，有助回答客户对产品可持续性与公司资本实力的关注。",
    "客户关心产品可持续时的资本工具参照",
    "偿付能力制度与再保工具基础",
    "团队简报：日本 ESR 与资本释放",
    "香港 RBC 与日本 ESR 制度对照",
    (0, 2, 3, 3), ["market", "reg"], ["reinsurance", "capital", "esr", "japan"],
    ["Pacific Life Re", "日本", "结构性再保", "ESR", "资本效率"],
    ("InsuranceAsia News 2026-10-13 报道", "InsuranceAsia News", "2026-10-13",
     "EN原文；付费墙，事实来自官网导语"),
    "en", 66, "verified"))

# ══ 6. Atrium：晶片厂资产申报价值 ══
ITEMS.append(mk(
    "ibm-atrium-chipmaker-asset-values-593255-20261013",
    "insurancebusinessmag", "media", "news",
    "2026-10-13T11:02:34+08:00",
    "https://www.insurancebusinessmag.com/asia/news/breaking-news/chipmaker-assets-have-tripled-in-a-decade-and-declared-values-may-not-have-kept-up-593255.aspx",
    "Atrium：全球二十大晶片廠房與庫存申報價值 5,290 億美元　申報條款與或有營業中斷承壓",
    "Insurance Business Asia 10月13日报道，Atrium 指出全球二十大晶片制造商合计申报的厂房与库存价值约5,290亿美元，十年间资产规模增长约两倍，但申报价值未必同步更新，令保单中的申报条款（reporting clause）与「或有营业中断」（contingent BI）保障承受压力。 [EN原文]",
    "供应链高度集中＋申报价值滞后，是营业中断保险最典型的失效场景。可用于向企业客说明保额不等于重置成本、申报条款如何运作，以及为何「上游单一供应商出事」也会触发自身保障讨论。",
    "与企业客谈营业中断与申报条款",
    "或有营业中断（contingent BI）基础补强",
    "团队分享：半导体供应链风险",
    "供应链集中度的区域风险地图",
    (1, 2, 2, 2), ["product", "tech", "market"], ["business-interruption", "property", "supply-chain", "valuation"],
    ["Atrium", "芯片制造业", "营业中断", "申报条款", "供应链"],
    ("Insurance Business Asia 2026-10-13 报道", "Insurance Business Asia", "2026-10-13",
     "EN原文；日期为报道日"),
    "en", 62, "verified"))

# ══ 7. 前 Chubb 澳新高管申索 ══
ITEMS.append(mk(
    "ibm-chubb-anz-chief-lawsuit-593240-20261013",
    "insurancebusinessmag", "media", "news",
    "2026-10-13T11:01:17+08:00",
    "https://www.insurancebusinessmag.com/asia/news/breaking-news/former-chubb-anz-chief-sues-insurer-asiapacific-boss-and-directors-593240.aspx",
    "前 Chubb 澳新業務主管入稟申索　亞太區總裁等 11 人被列答辯人",
    "10月13日报道，曾任 Chubb 澳大利亚及新西兰业务主管、驻新加坡的区域高管 Ben Howell，向澳洲公平工作委员会（Fair Work）提出申索，将亚太区总裁 Marcos Gunn 在内共11名个人列为答辩人。事件涉及跨国保险集团在亚太的高层人事争议与治理安排。 [EN原文]",
    "大型保险集团的高层争议属治理与雇主品牌风险信号。作为行业动态阅读即可，不宜用于与客户讨论个别公司；对内部而言，可用作说明跨国机构合规与人事治理机制差异的案例。",
    "行业治理动态了解（不与客户讨论个案）",
    "跨国机构治理与劳工申索常识",
    "地区人事与治理风险简报素材",
    "亚太保险机构治理对照",
    (0, 1, 2, 1), ["insurer", "market"], ["governance", "talent", "litigation", "apac"],
    ["Chubb", "澳大利亚", "公平工作", "人事争议", "公司治理"],
    ("Insurance Business Asia 2026-10-13 报道", "Insurance Business Asia", "2026-10-13",
     "EN原文；日期为报道日"),
    "en", 60, "verified"))

# ══ 8. APAC 医疗成本 2027 放缓 ══
ITEMS.append(mk(
    "ibm-apac-medical-cost-growth-2027-593200-20261013",
    "insurancebusinessmag", "media", "news",
    "2026-10-13T02:42:41+08:00",
    "https://www.insurancebusinessmag.com/asia/news/life-insurance/apac-medical-cost-growth-to-slow-significantly-in-2027-593200.aspx",
    "報告：2027 年亞太醫療成本增速料顯著放緩　惟未必等同保費升幅收窄",
    "10月13日报道，2027年亚太区医疗成本增速预计显著放缓，有助纾缓医疗开支预算压力；但报道同时指出，成本增速放缓不一定转化为保险保费升幅收窄，赔付频率、医疗通胀结构与承保利润修复等因素仍会左右定价。 [EN原文]",
    "「医疗成本增速放缓 ≠ 医疗险保费回落」是前线最容易讲错、也最容易引发期望落差的一点。这是可用于续保沟通与预期管理的标准口径，避免客户以为成本放缓就应即时减费。",
    "续保沟通：医疗成本与保费关系口径",
    "医疗通胀与医疗险定价基础补强",
    "团队简报：亚太医疗成本趋势",
    "区域医疗成本与保障缺口讨论",
    (2, 3, 2, 2), ["product", "market"], ["medical", "health", "pricing", "apac"],
    ["医疗成本", "亚太", "保费", "健康保险", "医疗通胀"],
    ("Insurance Business Asia 2026-10-13 报道", "Insurance Business Asia", "2026-10-13",
     "EN原文；日期为报道日"),
    "en", 66, "verified"))

# ══ 9. 旅游保险年龄分层（香港研究） ══
ITEMS.append(mk(
    "ibm-travel-insurance-age-cuts-593199-20261013",
    "insurancebusinessmag", "media", "news",
    "2026-10-13T02:38:46+08:00",
    "https://www.insurancebusinessmag.com/asia/news/travel/same-premium-smaller-cover-the-age-cuts-hidden-in-travel-plans-593199.aspx",
    "旅遊保險「同價、保障更細」：年齡分層令長者保障縮水　香港研究指維持原保障成本增 27%–36%",
    "10月13日报道，香港一项研究显示，若要让年长旅客维持原本的旅游保险权益，保费需增加27%至36%；报道并引述 Policybazaar 指出，部分计划已收紧分项限额，形成「同一保费、保障更细」的年龄隐藏条款。 [EN原文]",
    "长者旅游保障是高频查询，也是投诉热点。年龄分层、分项限额与「表面同一保费」是典型的信息披露落差，适合作为「投保前先读条款、向客户明确讲清限额」的示范案例。",
    "客户查询：长者旅游保障与限额说明",
    "旅游保险年龄分层与分项限额条款",
    "团队分享：产品条款中的年龄设计",
    "消费者保障与信息披露讨论",
    (2, 2, 2, 3), ["product", "market"], ["travel", "ageing", "sub-limits", "consumer-protection"],
    ["旅游保险", "长者", "年龄分层", "分项限额", "香港研究"],
    ("Insurance Business Asia 2026-10-13 报道", "Insurance Business Asia", "2026-10-13",
     "EN原文；日期为报道日"),
    "en", 62, "verified"))

# ══ 10. 数据中心损失跨保单 ══
ITEMS.append(mk(
    "ibm-data-centre-losses-accumulation-593176-20261013",
    "insurancebusinessmag", "media", "news",
    "2026-10-13T00:57:19+08:00",
    "https://www.insurancebusinessmag.com/asia/news/technology/data-centre-losses-could-cross-policies-and-portfolios-asiapacific-insurers-warn-593176.aspx",
    "亞太保險人警告：數據中心損失可跨保單、跨投資組合　共用供電與承包鏈令歸因及累積建模更難",
    "10月13日报道，亚太区保险公司警告，数据中心的损失可能横跨多张保单甚至整个投资组合：共用电力、承包商与网络环节互相交织，令单一损失事件的归因变得困难，营业中断保障与累积（accumulation）建模的复杂度上升。 [EN原文]",
    "数据中心是AI与云端投资最集中的实体风险点，属典型新兴累积风险。可用于向机构客与服务商解释多重保险人、多重保单下的责任界线，以及累积风险为何会推高再保成本。",
    "与企业客谈数据中心与累积风险",
    "累积风险与再保建模基础补强",
    "团队分享：AI 基建带来的新风险面",
    "香港数据中心业态的保障缺口讨论",
    (1, 2, 3, 2), ["tech", "product", "market"], ["data-centre", "accumulation", "business-interruption", "cyber"],
    ["数据中心", "累积风险", "营业中断", "亚太", "再保建模"],
    ("Insurance Business Asia 2026-10-13 报道", "Insurance Business Asia", "2026-10-13",
     "EN原文；日期为报道日"),
    "en", 64, "verified"))

# ══ 11. Aon：captive 成为资本平台 ══
ITEMS.append(mk(
    "artemis-aon-captives-third-party-capital-20261013",
    "artemis", "pro", "news",
    "2026-10-13T16:00:19+08:00",
    "https://www.artemis.bm/news/evolving-captives-becoming-strategic-platforms-for-attracting-third-party-capital-aon/",
    "Aon：專屬自保公司正由風險自留工具演變為吸引第三方資本的策略平台",
    "Artemis 于10月13日报道，Aon 指出专属自保公司（captive）正由单纯的自留风险工具，演变为企业的策略性资本获取平台：除填补传统市场保障缺口外，captive 可汇集企业整体风险敞口、接入保险相连证券（ILS）等另类风险转移工具，并开始引入第三方资本，以支撑更大自留额与增长计划。Aon 指风险变化速度已快于可用承保能力，是这轮结构演变的结构性原因。 [EN原文]",
    "香港正推动专属自保与风险管理中心定位，Aon 的「captive＝资本平台」框架比传统「省保费」说法更贴近企业财务决策。可用于向企业客与管理层解释 captive 的真正价值，也是理解香港专责自保政策吸引力所在的基本面。",
    "与企业客谈 captive 价值（非省保费）",
    "专属自保与 ILS 基础补强",
    "团队分享：香港专属自保与风险枢纽",
    "香港 captive 政策与国际实践对照",
    (1, 2, 3, 2), ["market", "reg"], ["captive", "ils", "risk-transfer", "capital"],
    ["专属自保", "Aon", "第三方资本", "ILS", "风险管理中心"],
    ("Artemis.bm 2026-10-13 报道", "Artemis.bm", "2026-10-13",
     "EN原文；含原文正文摘录"),
    "en", 70, "verified"))

# ══ 12. 飓风 Isaias 保险损失估计 ══
ITEMS.append(mk(
    "artemis-hurricane-isaias-loss-estimate-euler-20261013",
    "artemis", "pro", "news",
    "2026-10-13T15:00:15+08:00",
    "https://www.artemis.bm/news/hurricane-isaias-insurance-industry-loss-estimated-in-2bn-4bn-range-euler-ils-partners/",
    "颶風 Isaias 保險業損失料 20 億至 40 億美元　Euler ILS：或計入總額型結構",
    "Artemis 于10月13日报道，瑞士ILS投资管理人 Euler ILS Partners 初步估算飓风 Isaias 造成的保险业损失介乎20亿至40亿美元，并指损失有可能计入总额（aggregate）型结构；飓风于佛罗里达 Destin 附近登陆，损害多来自高度局部的强对流天气与大量树木倒塌，损失评估难度偏高。Cotality（前 CoreLogic）估计风灾与风暴潮保险损失为20亿至30亿美元，AccuWeather 估计整体经济损失160亿至200亿美元。 [EN原文]",
    "巨灾损失估计是ILS／巨灾债券市场定价的第一手信号，也直接影响再保续保条件。香港正发展巨灾债券与ILS生态，理解「初步估计→总额型结构→触发条款」这条链条，是内部讨论风险枢纽定位时需要的实操背景。",
    "与客户谈再保环境时的市场信号",
    "巨灾损失估计与总额型结构基础",
    "团队分享：ILS 与巨灾债券定价逻辑",
    "香港巨灾债券机制的国际参照",
    (0, 1, 2, 2), ["market"], ["catastrophe", "ils", "loss-estimate", "reinsurance"],
    ["巨灾债券", "ILS", "飓风Isaias", "损失估计", "总额型结构"],
    ("Artemis.bm 2026-10-13 报道", "Artemis.bm", "2026-10-13",
     "EN原文；含原文正文摘录"),
    "en", 68, "verified"))

# ══ 13. 标普：香港五年规划与保险机遇 ══
ITEMS.append(mk(
    "air-hk-five-year-plan-insurance-opportunities-20261013",
    "asiainsurancereview", "pro", "news",
    "2026-10-13",
    "https://www.asiainsurancereview.com/News/View-NewsLetter-Article/id/97220/Type/AirPlus/Hong-Kong-Five-Year-Plan-unlocks-insurance-opportunities-but-insurers-need-to-manage-underlying-risks",
    "標普：香港首個五年規劃為保險業打開機遇　惟保險人須管理底層風險",
    "Asia Insurance Review 于10月13日报道，标普全球评级（S&P Global Ratings）保险评级副总监 Judy Chen 指出，香港政府于2026年9月公布的首个五年规划为保险业带来多项机遇，但保险公司同时须妥善管理相关底层风险。报道为订户内容，公开部分仅为摘要。 [EN原文]",
    "五年规划是香港保险业未来数年业务方向的上游政策依据；评级机构视角把「机遇」与「底层风险」并列，适合作为对内说明业务机会时同时提示风险纪律的平衡素材。",
    "对内说明业务机会时的政策依据",
    "五年规划与保险业关联点梳理",
    "政策与评级视角简报素材",
    "香港五年规划中的保险定位",
    (1, 2, 3, 3), ["reg", "market"], ["five-year-plan", "policy", "growth", "hong-kong"],
    ["五年规划", "标普", "香港保险", "政策机遇", "风险管理"],
    ("Asia Insurance Review 2026-10-13 报道", "Asia Insurance Review", "2026-10-13",
     "EN原文；订户内容，仅公开摘要"),
    "en", 70, "pending"))

# ══ 14. 标普：香港寿险未来两年 5-10% 增长 ══
ITEMS.append(mk(
    "air-hk-life-insurance-market-expand-5-10-20261013",
    "asiainsurancereview", "pro", "news",
    "2026-10-13",
    "https://www.asiainsurancereview.com/News/View-NewsLetter-Article/id/97221/type/AIRPlus/Hong-Kong-Life-insurance-market-expected-to-expand-by-5-10-",
    "標普：香港壽險市場未來兩年料每年增長 5% 至 10%",
    "Asia Insurance Review 于10月13日报道，标普全球评级保险评级副总监 Judy Chen 在研讨会上预测，香港寿险保费在未来两年每年增长约5%至10%。报道属订户内容，公开部分仅为摘要。 [EN原文]",
    "评级机构的增速预测可作为年度业务假设的外部交叉验证，也方便把「增长从何而来」（跨境需求、渠道结构、产品组合）作为团队讨论题，而非只谈目标数字。",
    "年度业务假设的外部参照",
    "香港寿险市场结构与增长驱动",
    "团队简报：香港寿险增速预测",
    "跨境需求对本地市场的贡献",
    (1, 2, 3, 3), ["market"], ["life", "growth", "forecast", "hong-kong"],
    ["香港寿险", "保费增长", "标普", "预测", "跨境需求"],
    ("Asia Insurance Review 2026-10-13 报道", "Asia Insurance Review", "2026-10-13",
     "EN原文；订户内容，仅公开摘要"),
    "en", 70, "pending"))

# ═══ 写入 ═══
path = '/Users/leonliang/maoquanqingbao/data/live-items.json'
d = json.load(open(path, encoding='utf-8'))
ids = {it.get('id') for it in d['items']}
urls = {(it.get('originalUrl') or '').rstrip('/') for it in d['items']}
added = []
for it in reversed(ITEMS):
    if it['id'] in ids or it['originalUrl'].rstrip('/') in urls:
        print('SKIP dup:', it['id'])
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
    print('  +', it['id'], '|', it['publishedAt'], '|', it['sourceKey'], '|', it['sourceTier'],
          '|', it['verifyStatus'])
