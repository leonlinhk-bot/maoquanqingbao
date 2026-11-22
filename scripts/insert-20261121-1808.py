#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""一次性插入 2026-11-21 18:08 采集的条目
窗口：2026-11-20 17:15 → 2026-11-21 18:08 HKT
"""
import json
import shutil

BASE = '/Users/leonliang/maoquanqingbao'
LIVE = BASE + '/data/live-items.json'
NOW = '2026-11-21T18:08:00+08:00'

ITEMS = [
    {
        "id": "govhk-aiib-hk-office-20261121",
        "clusterCount": 1,
        "score": 85,
        "verifyStatus": "verified",
        "sourceTier": "official",
        "sourceKey": "govhk",
        "title": {
            "sc": "亞投行簽署在港設辦公室協定　港府向項目準備基金注資 2,000 萬美元",
            "tc": "亞投行簽署在港設辦公室協定　港府向項目準備基金注資 2,000 萬美元",
        },
        "summary": {
            "sc": "國家財政部與亞洲基礎設施投資銀行 11 月 21 日在港簽署協定，為亞投行在香港設立辦公室奠定基礎，並訂明辦公室的特權及豁免原則；財政司司長陳茂波、署理財庫局局長陳浩濂出席。同一場合，陳浩濂代表港府與亞投行簽署向「項目準備特別基金」注資 2,000 萬美元，港府將盡早向立法會提交附屬法例。",
            "tc": "國家財政部與亞洲基礎設施投資銀行 11 月 21 日在港簽署協定，為亞投行在香港設立辦公室奠定基礎，並訂明辦公室的特權及豁免原則；財政司司長陳茂波、署理財庫局局長陳浩濂出席。同一場合，陳浩濂代表港府與亞投行簽署向「項目準備特別基金」注資 2,000 萬美元，港府將盡早向立法會提交附屬法例。",
        },
        "why": {
            "sc": "多邊開發銀行把辦公室放在香港，實際帶動的是項目融資、工程與營運期風險的保險需求，以及跨境專業服務的落單機會。對高客與企業客戶而言，這是「香港仍是區域風險與資本交匯點」最硬的背书之一——講資產配置與傳承時，比空談樞紐定位更有說服力。",
            "tc": "多邊開發銀行把辦公室放在香港，實際帶動的是項目融資、工程與營運期風險的保險需求，以及跨境專業服務的落單機會。對高客與企業客戶而言，這是「香港仍是區域風險與資本交匯點」最硬的背書之一——講資產配置與傳承時，比空談樞紐定位更有說服力。",
        },
        "actions": {
            "front": {
                "sc": "向关注区域配置的客户提一句：多邊機構落戶落地，基建与项目风险的承保需求会跟着来",
                "tc": "向關注區域配置的客戶提一句：多邊機構落戶落地，基建與項目風險的承保需求會跟著來",
            },
            "midback": {
                "sc": "留意后续附属法例与银行业、工程险的机会名单",
                "tc": "留意後續附屬法例與銀行業、工程險的機會名單",
            },
            "lead": {
                "sc": "把「国际组织+基建资本」纳入香港平台叙事，用于对外沟通与家办路演",
                "tc": "把「國際組織+基建資本」納入香港平台敘事，用於對外溝通與家辦路演",
            },
            "cross": {
                "sc": "跨境基建与政治风险保障，可作为与律师、税务方联合服务的切入点",
                "tc": "跨境基建與政治風險保障，可作為與律師、稅務方聯合服務的切入點",
            },
        },
        "rolesImpact": {"front": 1, "midback": 1, "lead": 2, "cross": 2},
        "source": {"sc": "香港特区政府新闻公报", "lang": "zh"},
        "boards": ["market"],
        "themes": ["infrastructure", "multilateral", "hong-kong"],
        "tags": {
            "sc": ["亚投行", "办公室", "项目融资", "基建保险", "香港金融中心"],
            "tc": ["亞投行", "辦公室", "項目融資", "基建保險", "香港金融中心"],
        },
        "contentKind": "press",
        "publishedAt": "2026-11-21T17:11:00+08:00",
        "originalUrl": "https://www.info.gov.hk/gia/general/202611/21/P2026112000492.htm",
    },
    {
        "id": "govhk-brussels-family-office-20261121",
        "clusterCount": 1,
        "score": 86,
        "verifyStatus": "verified",
        "sourceTier": "official",
        "sourceKey": "govhk",
        "title": {
            "sc": "許正宇布魯塞爾收官：家辦優惠税制修訂待通過　首十個月逾 75 間家辦落戶",
            "tc": "許正宇布魯塞爾收官：家辦優惠稅制修訂待通過　首十個月逾 75 間家辦落戶",
        },
        "summary": {
            "sc": "財經事務及庫務局局長許正宇 11 月 20 日（布魯塞爾時間）結束訪歐，並在當地宴請家族辦公室代表推介香港。他指投資推廣署協助下，2026 年首十個月已有逾 75 間家辦在港設立或擴展，另有約 160 間正準備或已決定落戶；政府正修訂基金、單一家族辦公室及附帶權益的優惠税制，條例通過後自 2025/26 課税年度起生效。",
            "tc": "財經事務及庫務局局長許正宇 11 月 20 日（布魯塞爾時間）結束訪歐，並在當地宴請家族辦公室代表推介香港。他指投資推廣署協助下，2026 年首十個月已有逾 75 間家辦在港設立或擴展，另有約 160 間正準備或已決定落戶；政府正修訂基金、單一家族辦公室及附帶權益的優惠稅制，條例通過後自 2025/26 課稅年度起生效。",
        },
        "why": {
            "sc": "「160 間正在籌備」是真实在谈的管道，不是宣传口径——意味着未来一年家办相关的保单结构、信托与税务对接需求仍有增量。许正宇同场提到离岸人民币债券已占香港上市债券发行额 38%、超过美元债的 31%，这对讲分散配置的高客是一条现成的数据。",
            "tc": "「160 間正在籌備」是真實在談的管道，不是宣傳口徑——意味著未來一年家辦相關的保單結構、信託與稅務對接需求仍有增量。許正宇同場提到離岸人民幣債券已佔香港上市債券發行額 38%、超過美元債的 31%，這對講分散配置的高客是一條現成的數據。",
        },
        "actions": {
            "front": {
                "sc": "与高客聊家办时，可用「75 已落户、160 在筹备」说明香港生态正在变厚",
                "tc": "與高客聊家辦時，可用「75 已落戶、160 在籌備」說明香港生態正在變厚",
            },
            "midback": {
                "sc": "更新家办与传承方案的税务优惠说明页，待条例通过即换版",
                "tc": "更新家辦與傳承方案的稅務優惠說明頁，待條例通過即換版",
            },
            "lead": {
                "sc": "把欧洲家办资本列为下一轮路演目标客群，准备英文与法文版材料",
                "tc": "把歐洲家辦資本列為下一輪路演目標客群，準備英文與法文版材料",
            },
            "cross": {
                "sc": "家族信托＋保险的组合方案，可参照新优惠税制重新测算持有成本",
                "tc": "家族信託＋保險的組合方案，可參照新優惠稅制重新測算持有成本",
            },
        },
        "rolesImpact": {"front": 2, "midback": 2, "lead": 3, "cross": 3},
        "source": {"sc": "香港特区政府新闻公报", "lang": "zh"},
        "boards": ["family", "market"],
        "themes": ["family-office", "tax-incentive", "capital-connect"],
        "tags": {
            "sc": ["家族办公室", "优惠税制", "许正宇", "离岸人民币", "香港"],
            "tc": ["家族辦公室", "優惠稅制", "許正宇", "離岸人民幣", "香港"],
        },
        "contentKind": "press",
        "publishedAt": "2026-11-21T12:00:00+08:00",
        "originalUrl": "https://www.info.gov.hk/gia/general/202611/21/P2026112000289.htm",
    },
    {
        "id": "insuranceasianews-private-equity-insurance-20261121",
        "clusterCount": 1,
        "score": 70,
        "verifyStatus": "verified",
        "sourceTier": "pro",
        "sourceKey": "insuranceasianews",
        "title": {
            "sc": "私募股權重倉保險業　Aon 與貝萊德在勞合社組建 Cortina 跟單辛迪加 [EN原文]",
            "tc": "私募股權重倉保險業　Aon 與貝萊德在勞合社組建 Cortina 跟單辛迪加 [EN原文]",
        },
        "summary": {
            "sc": "InsuranceAsia News 周报：KKR 与韩国投资公社联手三星火灾，收购劳合社承保商 Canopius 余下 60%；Aon 与贝莱德合组劳合社跟单再保险辛迪加 Cortina，2027 年起提供多年期承保能力；淡马锡加入 KKR 牵头的 Steadfast 收购财团；亚太方面 KKR 入股香港 Peak Re。",
            "tc": "InsuranceAsia News 週報：KKR 與韓國投資公社聯手三星火災，收購勞合社承保商 Canopius 餘下 60%；Aon 與貝萊德合組勞合社跟單再保險辛迪加 Cortina，2027 年起提供多年期承保能力；淡馬錫加入 KKR 牽頭的 Steadfast 收購財團；亞太方面 KKR 入股香港 Peak Re。",
        },
        "why": {
            "sc": "资本进来改的是分销与议价结构：经纪商被并购后整合、佣金与后台支持会重排，承保端拿到长期资本后对费率的容忍度也会变。对前线团队，这意味着「你所在的中介会不会被整合」不再是遥远话题；对客户，则是「保单背后的承保主体是谁、会不会换」值得问一句。",
            "tc": "資本進來改的是分銷與議價結構：經紀商被併購後整合、佣金與後台支持會重排，承保端拿到長期資本後對費率的容忍度也會變。對前線團隊，這意味著「你所在的中介會不會被整合」不再是遙遠話題；對客戶，則是「保單背後的承保主體是誰、會不會換」值得問一句。",
        },
        "actions": {
            "front": {
                "sc": "客户问「公司稳不稳」时，用「股东是谁、资本多久」回答，比讲规模更实在",
                "tc": "客戶問「公司穩不穩」時，用「股東是誰、資本多久」回答，比講規模更實在",
            },
            "midback": {
                "sc": "梳理代理的承保主体股权结构，标注近年易手的公司",
                "tc": "梳理代理的承保主體股權結構，標註近年易手的公司",
            },
            "lead": {
                "sc": "把资本整合纳入年度渠道策略：哪些伙伴可能被并购、如何保住客户",
                "tc": "把資本整合納入年度渠道策略：哪些夥伴可能被併購、如何保住客戶",
            },
            "cross": {
                "sc": "高客长期保单的承保主体稳定性，纳入年度保单检视清单",
                "tc": "高客長期保單的承保主體穩定性，納入年度保單檢視清單",
            },
        },
        "rolesImpact": {"front": 2, "midback": 2, "lead": 3, "cross": 2},
        "source": {"sc": "InsuranceAsia News", "lang": "en"},
        "boards": ["market"],
        "themes": ["private-equity", "m-and-a", "asia-pacific"],
        "tags": {
            "sc": ["私募股权", "劳合社", "Canopius", "Cortina", "Peak Re"],
            "tc": ["私募股權", "勞合社", "Canopius", "Cortina", "Peak Re"],
        },
        "contentKind": "news",
        "publishedAt": "2026-11-21T08:00:00+08:00",
        "originalUrl": "https://insuranceasianews.com/private-equity-grows-an-appetite-for-insurance/",
    },
    {
        "id": "ibm-japan-cyber-claims-20261120",
        "clusterCount": 1,
        "score": 68,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insurancebusinessmag",
        "title": {
            "sc": "日本兩大產險 10 月網絡險賠案激增　東京海上達平常三倍、SOMPO 2.5 倍 [EN原文]",
            "tc": "日本兩大產險 10 月網絡險賠案激增　東京海上達平常三倍、SOMPO 2.5 倍 [EN原文]",
        },
        "summary": {
            "sc": "東京海上控股與 SOMPO 控股在 11 月 19 日業績披露：10 月網絡保險賠案通知分別增至平常三倍與 2.5 倍，兩者均指向 AI 輔助攻擊手法升級；SOMPO 高層稱客戶查詢提高保額或加保項目亦達平常三倍。日本個人資料保護委員會數據顯示，自 2026 年 4 月以來累計約 2.6 億人資料外泄，超過該國人口兩倍。",
            "tc": "東京海上控股與 SOMPO 控股在 11 月 19 日業績披露：10 月網絡保險賠案通知分別增至平常三倍與 2.5 倍，兩者均指向 AI 輔助攻擊手法升級；SOMPO 高層稱客戶查詢提高保額或加保項目亦達平常三倍。日本個人資料保護委員會數據顯示，自 2026 年 4 月以來累計約 2.6 億人資料外泄，超過該國人口兩倍。",
        },
        "why": {
            "sc": "赔案与「加保查询」同步放大，是风险认知真正转向的信号——香港的企业客户、诊所、律师事务所与家族办公室，同样把大量客户资料放在自家系统里。这类风险不在传统财产险的保障范围，量能也常常不足，是保单检视时最容易被跳过的一页。",
            "tc": "賠案與「加保查詢」同步放大，是風險認知真正轉向的信號——香港的企業客戶、診所、律師事務所與家族辦公室，同樣把大量客戶資料放在自家系統裡。這類風險不在傳統財產險的保障範圍，量能也常常不足，是保單檢視時最容易被跳過的一頁。",
        },
        "actions": {
            "front": {
                "sc": "见企业主客户时加一句：资料外泄的善后成本，财产险通常不赔",
                "tc": "見企業主客戶時加一句：資料外洩的善後成本，財產險通常不賠",
            },
            "midback": {
                "sc": "把网络险保额与实际资料量做一次对照，标出明显不足者",
                "tc": "把網絡險保額與實際資料量做一次對照，標出明顯不足者",
            },
            "lead": {
                "sc": "把网络风险纳入企业客户年度风险报告的固定章节",
                "tc": "把網絡風險納入企業客戶年度風險報告的固定章節",
            },
            "cross": {
                "sc": "家办的客户资料与第三方供应商条款，与律师一并复核",
                "tc": "家辦的客戶資料與第三方供應商條款，與律師一併覆核",
            },
        },
        "rolesImpact": {"front": 2, "midback": 2, "lead": 2, "cross": 2},
        "source": {"sc": "Insurance Business Asia", "lang": "en"},
        "boards": ["tech", "insurer"],
        "themes": ["cyber", "claims", "japan"],
        "tags": {
            "sc": ["网络保险", "赔案", "资料外泄", "东京海上", "SOMPO"],
            "tc": ["網絡保險", "賠案", "資料外洩", "東京海上", "SOMPO"],
        },
        "contentKind": "news",
        "publishedAt": "2026-11-20T21:50:00+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/cyber/japan-cyber-claims-surge-as-ai-sharpens-hacking-attacks-598246.aspx",
    },
    {
        "id": "ibm-ai-spend-vs-returns-20261120",
        "clusterCount": 1,
        "score": 66,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insurancebusinessmag",
        "title": {
            "sc": "KPMG：保險 CEO 擬把一到兩成預算投 AI　僅 1% 稱已見可量化回報 [EN原文]",
            "tc": "KPMG：保險 CEO 擬把一到兩成預算投 AI　僅 1% 稱已見可量化回報 [EN原文]",
        },
        "summary": {
            "sc": "KPMG《2026 全球保險 CEO 展望》訪問 12 個市場、100 位年收入逾 5 億美元的保險 CEO：近三分之二計劃未來 12 個月把總預算的 11% 至 20% 投向人工智能，82% 視 AI 為未來三年首要投資，但僅 1% 表示已取得可量化回報。30% 預期年度盈利增長 5% 至 9.99%，較去年 15% 翻倍。",
            "tc": "KPMG《2026 全球保險 CEO 展望》訪問 12 個市場、100 位年收入逾 5 億美元的保險 CEO：近三分之二計劃未來 12 個月把總預算的 11% 至 20% 投向人工智能，82% 視 AI 為未來三年首要投資，但僅 1% 表示已取得可量化回報。30% 預期年度盈利增長 5% 至 9.99%，較去年 15% 翻倍。",
        },
        "why": {
            "sc": "总部都还在为「AI 回报算不清」发愁，业务团队就更不该把「换了工具」当成「效率提升」。判断标准应该是可量化的场景：计划书对比原来两小时、现在多久；核保问题从等两天变成当天回复；客户回访覆盖率有没有真的上升。",
            "tc": "總部都還在為「AI 回報算不清」發愁，業務團隊就更不該把「換了工具」當成「效率提升」。判斷標準應該是可量化的場景：計劃書對比原來兩小時、現在多久；核保問題從等兩天變成當天回覆；客戶回訪覆蓋率有沒有真的上升。",
        },
        "actions": {
            "front": {
                "sc": "给自己定三个可量化的 AI 使用指标，月底对一次数",
                "tc": "給自己定三個可量化的 AI 使用指標，月底對一次數",
            },
            "midback": {
                "sc": "把团队 AI 投入按场景拆账，砍掉只用过两次的工具",
                "tc": "把團隊 AI 投入按場景拆賬，砍掉只用過兩次的工具",
            },
            "lead": {
                "sc": "向管理层汇报赋能成果时，用「省下的小时数」而非「培训场次」",
                "tc": "向管理層匯報賦能成果時，用「省下的小時數」而非「培訓場次」",
            },
            "cross": {
                "sc": "向高客展示 AI 辅助的检视流程时，先说清数据不外传的边界",
                "tc": "向高客展示 AI 輔助的檢視流程時，先說清資料不外傳的邊界",
            },
        },
        "rolesImpact": {"front": 2, "midback": 2, "lead": 3, "cross": 1},
        "source": {"sc": "Insurance Business Asia（引 KPMG 调查）", "lang": "en"},
        "boards": ["tech"],
        "themes": ["ai", "roi", "insurer-strategy"],
        "tags": {
            "sc": ["KPMG", "AI 投资", "回报", "保险科技", "预算"],
            "tc": ["KPMG", "AI 投資", "回報", "保險科技", "預算"],
        },
        "contentKind": "research",
        "publishedAt": "2026-11-20T19:00:00+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/technology/insurance-ai-spend-soars-as-measurable-returns-stay-out-of-reach-598234.aspx",
    },
    {
        "id": "artemis-blue-ridge-re-2026-1-20261120",
        "clusterCount": 1,
        "score": 70,
        "verifyStatus": "verified",
        "sourceTier": "pro",
        "sourceKey": "artemis",
        "title": {
            "sc": "北卡農民局第三筆巨災債券　Blue Ridge Re 2026-1 五檔合計目標 4.75 億美元 [EN原文]",
            "tc": "北卡農民局第三筆巨災債券　Blue Ridge Re 2026-1 五檔合計目標 4.75 億美元 [EN原文]",
        },
        "summary": {
            "sc": "北卡罗来纳农民局再度进入巨灾债券市场，透过百慕达特殊目的保险人 Blue Ridge Re 发行 2026-1 系列，五个分层合计目标 4.75 亿美元，只提供单次事故保障，但覆盖风险范围较 2025-1 更广；2023-1 的 4 亿美元保障年底到期，今次属续保并可能扩容。",
            "tc": "北卡羅來納農民局再度進入巨災債券市場，透過百慕達特殊目的保險人 Blue Ridge Re 發行 2026-1 系列，五個分層合計目標 4.75 億美元，只提供單次事故保障，但覆蓋風險範圍較 2025-1 更廣；2023-1 的 4 億美元保障年底到期，今次屬續保並可能擴容。",
        },
        "why": {
            "sc": "巨灾债券与保险相连证券（ILS）在香港仍是新品，判断本地产品能不能做大，看的是国际市场的续保与定价节奏。同一发行人连续三年回来、且这次目标规模高于到期规模，说明资本市场对灾害风险仍有承接力——这是香港推 ILS 与专属自保时最需要的参照。",
            "tc": "巨災債券與保險相連證券（ILS）在香港仍是新品，判斷本地產品能不能做大，看的是國際市場的續保與定價節奏。同一發行人連續三年回來、且這次目標規模高於到期規模，說明資本市場對災害風險仍有承接力——這是香港推 ILS 與專屬自保時最需要的參照。",
        },
        "actions": {
            "front": {
                "sc": "客户问「巨灾风险谁买单」时，可用 ILS 举例说明风险已被资本市场分担",
                "tc": "客戶問「巨災風險誰買單」時，可用 ILS 舉例說明風險已被資本市場分擔",
            },
            "midback": {
                "sc": "留意本地 ILS 与侧挂车发行进度，纳入再保安排备选",
                "tc": "留意本地 ILS 與側掛車發行進度，納入再保安排備選",
            },
            "lead": {
                "sc": "把 ILS 市场的续保节奏列为年度另类资产观察项",
                "tc": "把 ILS 市場的續保節奏列為年度另類資產觀察項",
            },
            "cross": {
                "sc": "高客若持有灾害相关资产，可用 ILS 说明分散机制如何运作",
                "tc": "高客若持有災害相關資產，可用 ILS 說明分散機制如何運作",
            },
        },
        "rolesImpact": {"front": 1, "midback": 1, "lead": 2, "cross": 1},
        "source": {"sc": "Artemis", "lang": "en"},
        "boards": ["market"],
        "themes": ["cat-bond", "reinsurance", "ils"],
        "tags": {
            "sc": ["巨灾债券", "Blue Ridge Re", "ILS", "再保险", "美国"],
            "tc": ["巨災債券", "Blue Ridge Re", "ILS", "再保險", "美國"],
        },
        "contentKind": "news",
        "publishedAt": "2026-11-20T22:00:00+08:00",
        "originalUrl": "https://www.artemis.bm/news/nc-farm-bureau-sponsoring-its-third-catastrophe-bond-475m-blue-ridge-re-2026-1/",
    },
]


def main():
    d = json.load(open(LIVE, encoding='utf-8'))
    old = d['items']
    existing_ids = {i['id'] for i in old}
    existing_urls = {(i.get('originalUrl') or '').rstrip('/') for i in old}

    new = []
    for it in ITEMS:
        it['ingestedAt'] = NOW
        it['contentRole'] = {'sc': '本站导读', 'tc': '本站導讀'}
        it['featured'] = False
        it['evergreen'] = False
        it['summaryShort'] = {'sc': it['summary']['sc'][:80], 'tc': it['summary']['tc'][:80]}
        if it['id'] in existing_ids:
            print('SKIP dup id:', it['id'])
            continue
        if it['originalUrl'].rstrip('/') in existing_urls:
            print('SKIP dup url:', it['id'])
            continue
        assert len(it['boards']) >= 1, it['id']
        assert len(it['themes']) >= 2, it['id']
        assert it['originalUrl'].startswith('http'), it['id']
        slen = len(it['summary']['sc'])
        assert 50 <= slen <= 170, (it['id'], slen)
        existing_ids.add(it['id'])
        existing_urls.add(it['originalUrl'].rstrip('/'))
        new.append(it)

    new.sort(key=lambda x: x['publishedAt'], reverse=True)
    print('inserting', len(new), 'items')
    d['items'] = new + old
    d.setdefault('meta', {})
    d['meta']['generatedAt'] = NOW
    d['meta']['itemCount'] = len(d['items'])
    d['meta']['windowNote'] = {'sc': f'本库{len(d["items"])}条。', 'tc': f'本庫{len(d["items"])}條。'}

    shutil.copy(LIVE, LIVE + '.bak-1121-1808')
    json.dump(d, open(LIVE, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('total now:', len(d['items']))


if __name__ == '__main__':
    main()
