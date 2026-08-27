#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""每日增量采集 2026-08-28(补跑 01:22): 插入新条目到 live-items.json 最前, 更新 meta"""
import json, datetime

NOW = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
NOW_STR = NOW.strftime('%Y-%m-%dT%H:%M:%S+08:00')

NEW_ITEMS = [
    {
        "id": "ibm-skorea-h1-20260828",
        "clusterCount": 1,
        "score": 66,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insurancebusinessmag",
        "title": {
            "sc": "韩国上半年险企利润增13%至9.1万亿韩元 投资收益掩盖承保压力 车险由盈转亏 [EN原文]",
            "tc": "韓國上半年險企利潤增13%至9.1萬億韓元 投資收益掩蓋承保壓力 車險由盈轉虧 [EN原文]"
        },
        "summary": {
            "sc": "韩国金融监督院(FSS)8月27日公布上半年初步数据：险企合计净利润9.1万亿韩元增13%，寿险3.93万亿(+17.7%)、非寿险5.09万亿(+9.6%)，增长主要靠投资收益；三星人寿净利增35.8%但保险服务利润跌35.9%，车险承保由盈转亏(自1261亿韩元盈利转105亿韩元亏损)。",
            "tc": "韓國金融監督院(FSS)8月27日公佈上半年初步數據：險企合計淨利潤9.1萬億韓元增13%，壽險3.93萬億(+17.7%)、非壽險5.09萬億(+9.6%)，增長主要靠投資收益；三星人壽淨利增35.8%但保險服務利潤跌35.9%，車險承保由盈轉虧(自1261億韓元盈利轉105億韓元虧損)。"
        },
        "why": {
            "sc": "投资收益撑利润、承保端承压的格局与港险同业高度相似；车险全线转亏是亚太非寿险承保周期的重要信号，值得同业对标。",
            "tc": "投資收益撐利潤、承保端承壓的格局與港險同業高度相似；車險全線轉虧是亞太非壽險承保週期的重要信號，值得同業對標。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "同业业绩与承保周期对标", "tc": "同業業績與承保週期對標"},
            "lead": {},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 1, "lead": 0, "cross": 0},
        "source": {"sc": "Insurance Business", "lang": "en"},
        "boards": ["insurer", "market"],
        "themes": ["results", "underwriting"],
        "tags": {"sc": ["韩国", "FSS", "上半年业绩", "车险承保"], "tc": ["韓國", "FSS", "上半年業績", "車險承保"]},
        "contentKind": "news",
        "publishedAt": "2026-08-28T08:14:33+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/investment-income-masks-underwriting-stress-in-south-koreas-h1-results-587760.aspx",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "ibm-chiba-auto-gap-20260828",
        "clusterCount": 1,
        "score": 64,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insurancebusinessmag",
        "title": {
            "sc": "千叶水灾暴露日本车险保障缺口：近半驾驶者无自愿车损险 费率上调抑制投保 [EN原文]",
            "tc": "千葉水災暴露日本車險保障缺口：近半駕駛者無自願車損險 費率上調抑制投保 [EN原文]"
        },
        "summary": {
            "sc": "千叶水灾约2500辆滞留车辆中近半无车损保障。日本强制车险不覆盖车辆损失，全国自愿车损险投保率仅47.4%，五年仅升1.7个百分点，千叶50.5%仍不足；对比韩国综合车险占比87.2%，日本保障缺口显著。2025年Q4车险费率预计上调6%-8.5%，进一步抑制投保意愿。",
            "tc": "千葉水災約2500輛滯留車輛中近半無車損保障。日本強制車險不覆蓋車輛損失，全國自願車損險投保率僅47.4%，五年僅升1.7個百分點，千葉50.5%仍不足；對比韓國綜合車險佔比87.2%，日本保障缺口顯著。2025年Q4車險費率預計上調6%-8.5%，進一步抑制投保意願。"
        },
        "why": {
            "sc": "车险保障缺口与费率上行相互强化，暴露亚太非寿险渗透难题，对港险车险与非寿险产品设计、区域对标有参考价值。",
            "tc": "車險保障缺口與費率上行相互強化，暴露亞太非壽險滲透難題，對港險車險與非壽險產品設計、區域對標有參考價值。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "非寿险渗透与费率趋势关注", "tc": "非壽險滲透與費率趨勢關注"},
            "lead": {},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 1, "lead": 0, "cross": 0},
        "source": {"sc": "Insurance Business", "lang": "en"},
        "boards": ["market", "product"],
        "themes": ["pricing", "market"],
        "tags": {"sc": ["日本", "车险", "保障缺口", "费率上调"], "tc": ["日本", "車險", "保障缺口", "費率上調"]},
        "contentKind": "news",
        "publishedAt": "2026-08-28T07:32:09+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/auto-motor/chiba-flooding-exposes-japans-stagnant-auto-insurance-enrolment-gap-587754.aspx",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "ibm-kazakhstan-branch-20260828",
        "clusterCount": 1,
        "score": 66,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insurancebusinessmag",
        "title": {
            "sc": "哈萨克斯坦拟解除外资保险分支机构准入禁令 以A-评级取代5亿美元资产门槛 [EN原文]",
            "tc": "哈薩克斯坦擬解除外資保險分支機構准入禁令 以A-評級取代5億美元資產門檻 [EN原文]"
        },
        "summary": {
            "sc": "哈央行起草改革，拟以A-评级加治理质量框架取代现行5亿美元最低资产门槛及10年全险种经营经验要求，允许外资保险分支机构直接进入市场。目前25家险企中9家有外资参与但均为本地注册实体，尚无外资分支；2025年保费1.7万亿坚戈(约34亿美元)增12.5%，保险资产占GDP仅约2%。",
            "tc": "哈央行起草改革，擬以A-評級加治理質量框架取代現行5億美元最低資產門檻及10年全險種經營經驗要求，允許外資保險分支機構直接進入市場。目前25家險企中9家有外資參與但均為本地註冊實體，尚無外資分支；2025年保費1.7萬億堅戈(約34億美元)增12.5%，保險資產佔GDP僅約2%。"
        },
        "why": {
            "sc": "中亚最大市场外资保险准入改革样本，观察新兴市场开放节奏，对布局中亚业务的港险及再保机构有前瞻价值。",
            "tc": "中亞最大市場外資保險准入改革樣本，觀察新興市場開放節奏，對佈局中亞業務的港險及再保機構有前瞻價值。"
        },
        "actions": {
            "front": {},
            "midback": {},
            "lead": {},
            "cross": {"sc": "关注中亚保险市场开放机会", "tc": "關注中亞保險市場開放機會"}
        },
        "rolesImpact": {"front": 0, "midback": 0, "lead": 0, "cross": 1},
        "source": {"sc": "Insurance Business", "lang": "en"},
        "boards": ["market", "reg"],
        "themes": ["reg", "market"],
        "tags": {"sc": ["哈萨克斯坦", "外资准入", "保险市场", "改革"], "tc": ["哈薩克斯坦", "外資准入", "保險市場", "改革"]},
        "contentKind": "news",
        "publishedAt": "2026-08-28T06:46:38+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/kazakhstan-moves-to-end-its-foreign-insurance-branch-lockout-587742.aspx",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "ibm-vietnam-banks-own-20260827",
        "clusterCount": 1,
        "score": 66,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insurancebusinessmag",
        "title": {
            "sc": "越南银行从卖保险转向自营保险：ACB获准设立非寿险子公司 [EN原文]",
            "tc": "越南銀行從賣保險轉向自營保險：ACB獲准設立非壽險子公司 [EN原文]"
        },
        "summary": {
            "sc": "ACB获越南财政部批设ACB Insurance非寿险子公司，注册资本5000亿越南盾(约1900万美元)，总部胡志明市，经营期99年；VPBank亦获批筹建寿险公司。四大国有行早已自营保险(母行持股51%-73%)。ACB拟以insurtech模式优先服务存量客户，从赚代销佣金转向自留承保利润。",
            "tc": "ACB獲越南財政部批設ACB Insurance非壽險子公司，註冊資本5000億越南盾(約1900萬美元)，總部胡志明市，經營期99年；VPBank亦獲批籌建壽險公司。四大國有行早已自營保險(母行持股51%-73%)。ACB擬以insurtech模式優先服務存量客戶，從賺代銷佣金轉向自留承保利潤。"
        },
        "why": {
            "sc": "银保渠道从代销转向自营、封闭式分销挤压独立经纪空间，是亚太银保格局变化的重要样本，与港险银保策略直接相关。",
            "tc": "銀保渠道從代銷轉向自營、封閉式分銷擠壓獨立經紀空間，是亞太銀保格局變化的重要樣本，與港險銀保策略直接相關。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "银保渠道格局变化对标", "tc": "銀保渠道格局變化對標"},
            "lead": {},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 1, "lead": 0, "cross": 0},
        "source": {"sc": "Insurance Business", "lang": "en"},
        "boards": ["market", "firm"],
        "themes": ["channel", "market"],
        "tags": {"sc": ["越南", "银行系险企", "银保渠道", "ACB"], "tc": ["越南", "銀行系險企", "銀保渠道", "ACB"]},
        "contentKind": "news",
        "publishedAt": "2026-08-27T07:20:00+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/vietnams-banks-are-done-selling-insurance--now-they-want-to-own-it-587594.aspx",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "ibm-hormuz-warrisk-20260827",
        "clusterCount": 1,
        "score": 62,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insurancebusinessmag",
        "title": {
            "sc": "特朗普称霍尔木兹海峡已通航 保险市场维持3%-8%战争险费率 [EN原文]",
            "tc": "特朗普稱霍爾木茲海峽已通航 保險市場維持3%-8%戰爭險費率 [EN原文]"
        },
        "summary": {
            "sc": "美方宣布海峡清障，但保险市场维持谨慎：战争险费率仍在船体价值3%-8%。1.5亿美元油轮单次通行保费最高1500万美元，战前约37.5万。劳合社JWC将整个波斯湾列为高风险区，解除须持续无事故通行、地缘稳定及正式排雷证据；战恐政暴险种累计理赔20-30亿美元，超过该险种全球年保费规模。",
            "tc": "美方宣佈海峽清障，但保險市場維持謹慎：戰爭險費率仍在船體價值3%-8%。1.5億美元油輪單次通行保費最高1500萬美元，戰前約37.5萬。勞合社JWC將整個波斯灣列為高風險區，解除須持續無事故通行、地緣穩定及正式排雷證據；戰恐政暴險種累計理賠20-30億美元，超過該險種全球年保費規模。"
        },
        "why": {
            "sc": "战争险定价与承保能力决定全球航运保险成本，费率高企影响供应链保费，港险海事与贸易险团队可关注JWC后续动向。",
            "tc": "戰爭險定價與承保能力決定全球航運保險成本，費率高企影響供應鏈保費，港險海事與貿易險團隊可關注JWC後續動向。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "海事与贸易险费率关注", "tc": "海事與貿易險費率關注"},
            "lead": {},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 1, "lead": 0, "cross": 0},
        "source": {"sc": "Insurance Business", "lang": "en"},
        "boards": ["market"],
        "themes": ["pricing", "market"],
        "tags": {"sc": ["霍尔木兹", "战争险", "费率", "海事保险"], "tc": ["霍爾木茲", "戰爭險", "費率", "海事保險"]},
        "contentKind": "news",
        "publishedAt": "2026-08-27T05:01:06+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/trump-says-hormuz-is-clear--the-insurance-market-disagrees-587553.aspx",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "iaa-singlife-foreigners-20260827",
        "clusterCount": 1,
        "score": 68,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insuranceasia",
        "title": {
            "sc": "Singlife向在坡外国人开放医疗险：私立医院计划年限额最高200万新元 [EN原文]",
            "tc": "Singlife向在坡外國人開放醫療險：私立醫院計劃年限額最高200萬新元 [EN原文]"
        },
        "summary": {
            "sc": "新加坡Singlife将Shield及Health Plus扩展至在坡生活、工作及留学的外国人。Shield Plan 1覆盖私立医院治疗，年限额最高200万新元(约157万美元)，经IHH医疗网络接入逾700名专科医生；Plan 2覆盖公立医院A级病房，年限额120万新元，为外国人可购公立医院计划中最高；家庭投保享折扣并获子女免费Health Plus。",
            "tc": "新加坡Singlife將Shield及Health Plus擴展至在坡生活、工作及留學的外國人。Shield Plan 1覆蓋私立醫院治療，年限額最高200萬新元(約157萬美元)，經IHH醫療網絡接入逾700名專科醫生；Plan 2覆蓋公立醫院A級病房，年限額120萬新元，為外國人可購公立醫院計劃中最高；家庭投保享折扣並獲子女免費Health Plus。"
        },
        "why": {
            "sc": "新加坡向非居民开放医疗险，与香港MCV外籍客群模式同源；产品形态、医疗网络合作与家庭折扣设计对港险跨境健康险有直接参考。",
            "tc": "新加坡向非居民開放醫療險，與香港MCV外籍客群模式同源；產品形態、醫療網絡合作與家庭折扣設計對港險跨境健康險有直接參考。"
        },
        "actions": {
            "front": {},
            "midback": {},
            "lead": {},
            "cross": {"sc": "跨境健康险产品对标", "tc": "跨境健康險產品對標"}
        },
        "rolesImpact": {"front": 0, "midback": 0, "lead": 0, "cross": 1},
        "source": {"sc": "InsuranceAsia", "lang": "en"},
        "boards": ["product", "insurer"],
        "themes": ["health", "cross-border"],
        "tags": {"sc": ["Singlife", "新加坡", "医疗险", "外国人投保"], "tc": ["Singlife", "新加坡", "醫療險", "外國人投保"]},
        "contentKind": "news",
        "publishedAt": "2026-08-27T11:58:54+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/foreigners-gain-access-singlife-health-plans-in-singapore",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "iaa-apac-catgap-20260827",
        "clusterCount": 1,
        "score": 64,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insuranceasia",
        "title": {
            "sc": "Aon：亚太巨灾保障缺口上半年约90% 传统保险难以单靠承保弥合 [EN原文]",
            "tc": "Aon：亞太巨災保障缺口上半年約90% 傳統保險難以單靠承保彌合 [EN原文]"
        },
        "summary": {
            "sc": "Aon亚太气候分析主管Tom Mortlock：上半年亚太巨灾损失100亿美元仅10亿获保险赔付，保障缺口约90%。低收入与可负担性是主因，气旋洪水暴露累积风险；参数保险与小额保险可作补充，根本出路在风险减量与收入增长。模型进步令巨灾更可定价，但新兴市场费率受购买力约束或偏低。",
            "tc": "Aon亞太氣候分析主管Tom Mortlock：上半年亞太巨災損失100億美元僅10億獲保險賠付，保障缺口約90%。低收入與可負擔性是主因，氣旋洪水暴露累積風險；參數保險與小額保險可作補充，根本出路在風險減量與收入增長。模型進步令巨災更可定價，但新興市場費率受購買力約束或偏低。"
        },
        "why": {
            "sc": "巨灾保障缺口与可负担性议题持续发酵，是再保定价、巨灾债券与保险科技应用的风向标，与港险再保及ILS业务相关。",
            "tc": "巨災保障缺口與可負擔性議題持續發酵，是再保定價、巨災債券與保險科技應用的風向標，與港險再保及ILS業務相關。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "巨灾定价与再保策略关注", "tc": "巨災定價與再保策略關注"},
            "lead": {},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 1, "lead": 0, "cross": 0},
        "source": {"sc": "InsuranceAsia", "lang": "en"},
        "boards": ["market"],
        "themes": ["reinsurance", "pricing"],
        "tags": {"sc": ["Aon", "巨灾保障缺口", "参数保险", "再保"], "tc": ["Aon", "巨災保障缺口", "參數保險", "再保"]},
        "contentKind": "news",
        "publishedAt": "2026-08-27T11:47:36+08:00",
        "originalUrl": "https://insuranceasia.com/videos/apac-catastrophe-gap-persists-cover-stays-unaffordable",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "nfra-audit-liability-qa-20260827",
        "clusterCount": 1,
        "score": 85,
        "verifyStatus": "verified",
        "sourceTier": "official",
        "sourceKey": "nfra",
        "title": {
            "sc": "财政部与金融监管总局印发《会计师事务所职业责任保险实施办法》：重点业务保额上限升至1亿元",
            "tc": "財政部與金融監管總局印發《會計師事務所職業責任保險實施辦法》：重點業務保額上限升至1億元"
        },
        "summary": {
            "sc": "财政部、金融监管总局联合印发《会计师事务所职业责任保险实施办法》(财会〔2026〕12号)。从事证券服务及金融企业审计的会计所基本投保额度由5000万元上调至1亿元，合伙人超100名的按每名合伙人100万元计；累计赔偿限额按「100万×合伙人人数与1亿元孰高」执行；费率浮动纳入执业年限、行政处罚与涉诉记录，承保险企近三年综合偿付能力充足率须不低于180%。",
            "tc": "財政部、金融監管總局聯合印發《會計師事務所職業責任保險實施辦法》(財會〔2026〕12號)。從事證券服務及金融企業審計的會計所基本投保額度由5000萬元上調至1億元，合夥人超100名的按每名合夥人100萬元計；累計賠償限額按「100萬×合夥人人數與1億元孰高」執行；費率浮動納入執業年限、行政處罰與涉訴記錄，承保險企近三年綜合償付能力充足率須不低於180%。"
        },
        "why": {
            "sc": "职业责任险是港险财险与再保重要品类，内地保额与费率机制升级利好专业责任险需求，也体现监管对专业服务风险的传导。",
            "tc": "職業責任險是港險財險與再保重要品類，內地保額與費率機制升級利好專業責任險需求，也體現監管對專業服務風險的傳導。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "专业责任险产品与承保跟进", "tc": "專業責任險產品與承保跟進"},
            "lead": {},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 1, "lead": 0, "cross": 0},
        "source": {"sc": "金融监管总局 NFRA", "lang": "zh"},
        "boards": ["reg", "product"],
        "themes": ["reg", "product"],
        "tags": {"sc": ["职业责任保险", "财政部", "金融监管总局", "保额上调"], "tc": ["職業責任保險", "財政部", "金融監管總局", "保額上調"]},
        "contentKind": "news",
        "publishedAt": "2026-08-27T18:02:00+08:00",
        "originalUrl": "https://finance.sina.com.cn/money/insurance/bxdt/2026-08-27/doc-inipucsr9070189.shtml",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "nfra-gyirong-mudslide-20260827",
        "clusterCount": 1,
        "score": 85,
        "verifyStatus": "verified",
        "sourceTier": "official",
        "sourceKey": "nfra",
        "title": {
            "sc": "金融监管总局启动保险业二级救灾应急响应 指导应对吉隆口岸泥石流灾害",
            "tc": "金融監管總局啟動保險業二級救災應急響應 指導應對吉隆口岸泥石流災害"
        },
        "summary": {
            "sc": "8月26日尼泊尔一侧泥石流致西藏日喀则吉隆口岸重大人员伤亡失联，金融监管总局启动保险业二级救灾应急响应。人保财险承保建筑工程一切险及人员意外险并启动一级应急预案；太保产险西藏分公司12小时内赔付18万余元；平安产险跟踪旅游意外险客户；建行1小时划转应急资金30万元，农行落实贷款延期还款。",
            "tc": "8月26日尼泊爾一側泥石流致西藏日喀則吉隆口岸重大人員傷亡失聯，金融監管總局啟動保險業二級救災應急響應。人保財險承保建築工程一切險及人員意外險並啟動一級應急預案；太保產險西藏分公司12小時內賠付18萬餘元；平安產險跟蹤旅遊意外險客戶；建行1小時劃轉應急資金30萬元，農行落實貸款延期還款。"
        },
        "why": {
            "sc": "巨灾应急响应与快速理赔实践反映内地保险业救灾效率，港险可对标跨境灾害应急、承保摸排与理赔服务流程。",
            "tc": "巨災應急響應與快速理賠實踐反映內地保險業救災效率，港險可對標跨境災害應急、承保摸排與理賠服務流程。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "巨灾应急与理赔流程对标", "tc": "巨災應急與理賠流程對標"},
            "lead": {},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 1, "lead": 0, "cross": 0},
        "source": {"sc": "金融监管总局 NFRA", "lang": "zh"},
        "boards": ["market"],
        "themes": ["catastrophe", "claims"],
        "tags": {"sc": ["吉隆口岸", "泥石流", "救灾应急", "快速理赔"], "tc": ["吉隆口岸", "泥石流", "救災應急", "快速理賠"]},
        "contentKind": "news",
        "publishedAt": "2026-08-27T12:14:00+08:00",
        "originalUrl": "https://finance.sina.com.cn/money/bank/gsdt/2026-08-27/doc-iniptnux5508817.shtml",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    }
]

def main():
    path = 'data/live-items.json'
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    items = data['items']
    existing_ids = {it.get('id') for it in items}
    dup = [it['id'] for it in NEW_ITEMS if it['id'] in existing_ids]
    if dup:
        print('SKIP duplicates:', dup)
    fresh = [it for it in NEW_ITEMS if it['id'] not in existing_ids]
    titles = {(it.get('sourceKey'), it.get('title', {}).get('sc')) for it in items}
    fresh = [it for it in fresh if (it.get('sourceKey'), it.get('title', {}).get('sc')) not in titles]
    items[:0] = fresh
    data['items'] = items
    meta = data['meta']
    meta['itemCount'] = len(items)
    meta['generatedAt'] = NOW_STR
    meta['windowNote'] = {
        "sc": f"本库{len(items)}条。",
        "tc": f"本庫{len(items)}條。"
    }
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print(f'新增 {len(fresh)} 条 -> 总条数 {len(items)}')
    for it in fresh:
        print(' +', it['id'])

if __name__ == '__main__':
    main()
