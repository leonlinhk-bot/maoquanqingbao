#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""一次性插入 2026-11-20 18:08 采集的条目
窗口：2026-11-19 18:08 → 2026-11-20 18:08 HKT
"""
import json
import shutil

BASE = '/Users/leonliang/maoquanqingbao'
LIVE = BASE + '/data/live-items.json'
NOW = '2026-11-20T18:08:00+08:00'

ITEMS = [
    {
        "id": "hk01-zurich-hk-breach-20261120",
        "clusterCount": 1,
        "score": 66,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "hk01",
        "title": {
            "sc": "苏黎世香港客户网上平台遭未授权存取　私隐公署：38,453 人资料或受影响",
            "tc": "蘇黎世香港客戶網上平台遭未授權存取　私隱公署：38,453 人資料或受影響",
        },
        "summary": {
            "sc": "苏黎世保险（香港）11 月 19 日发重要告示，指客户网上平台遭未经授权存取，已停用平台维护并向监管机构通报；个人资料私隐专员公署确认 38,453 人资料或受影响，涉姓名、香港身份证、护照号码、出生日期、电邮及电话，已对苏黎世人寿（香港）等三家公司展开调查。",
            "tc": "蘇黎世保險（香港）11 月 19 日發重要告示，指客戶網上平台遭未經授權存取，已停用平台維護並向監管機構通報；個人資料私隱專員公署確認 38,453 人資料或受影響，涉姓名、香港身份證、護照號碼、出生日期、電郵及電話，已對蘇黎世人壽（香港）等三家公司展開調查。",
        },
        "why": {
            "sc": "保险公司自有客户平台被入侵，泄漏的是核保端最敏感的身份与保单资料；这类资料外流后最常见的用途，是「报得出保单号与身份证尾号」的精准诈骗。前线不能等客户从新闻里先看到才解释——本港近期已有国泰、香港航空等第三方外泄案在前，客户对「你们会不会也这样」的敏感度很高。",
            "tc": "保險公司自有客戶平台被入侵，洩漏的是核保端最敏感的身份與保單資料；這類資料外流後最常見的用途，是「報得出保單號與身份證尾號」的精準詐騙。前線不能等客戶從新聞裡先看到才解釋——本港近期已有國泰、香港航空等第三方外洩案在前，客戶對「你們會不會也這樣」的敏感度很高。",
        },
        "actions": {
            "front": {
                "sc": "向客户统一口径：公司不会来电索取密码或验证码；可疑来电请挂断后打保单上的官方热线核实",
                "tc": "向客戶統一口徑：公司不會來電索取密碼或驗證碼；可疑來電請掛斷後打保單上的官方熱線核實",
            },
            "midback": {
                "sc": "复核客户平台与第三方供应商的权限最小化与访问日志留存",
                "tc": "覆核客戶平台與第三方供應商的權限最小化與訪問日誌留存",
            },
            "lead": {
                "sc": "把资料外泄纳入年度风险清单，预备对外说法与客服话术",
                "tc": "把資料外洩納入年度風險清單，預備對外說法與客服話術",
            },
            "cross": {
                "sc": "高客的资料安全与保密条款，随年度保单检视一并复核",
                "tc": "高客的資料安全與保密條款，隨年度保單檢視一併覆核",
            },
        },
        "rolesImpact": {"front": 3, "midback": 2, "lead": 2, "cross": 2},
        "source": {"sc": "香港01", "lang": "zh"},
        "boards": ["tech", "reg"],
        "themes": ["cyber", "hong-kong", "privacy"],
        "tags": {
            "sc": ["苏黎世", "资料外泄", "私隐公署", "网络安全", "保单资料"],
            "tc": ["蘇黎世", "資料外洩", "私隱公署", "網絡安全", "保單資料"],
        },
        "contentKind": "news",
        "publishedAt": "2026-11-20",
        "originalUrl": "https://www.hk01.com/%E7%A4%BE%E6%9C%83%E6%96%B0%E8%81%9E/60413006/%E8%98%87%E9%BB%8E%E4%B8%96%E4%BF%9D%E9%9A%AA%E7%B6%B2%E4%B8%8A%E5%B9%B3%E5%8F%B0%E9%81%AD%E5%85%A5%E4%BE%B5-3-8%E8%90%AC%E5%AE%A2%E6%88%B6%E8%B3%87%E6%96%99%E7%96%91%E5%A4%96%E6%B4%A9-%E7%B6%B2%E4%B8%8A%E5%B9%B3%E5%8F%B0%E5%81%9C%E7%94%A8",
    },
    {
        "id": "govhk-va-services-bill-20261120",
        "clusterCount": 1,
        "score": 85,
        "verifyStatus": "verified",
        "sourceTier": "official",
        "sourceKey": "govhk",
        "title": {
            "sc": "虚拟资产服务修订条例草案刊宪　交易、顾问、管理、托管四类服务须领牌",
            "tc": "虛擬資產服務修訂條例草案刊憲　交易、顧問、管理、託管四類服務須領牌",
        },
        "summary": {
            "sc": "政府 11 月 20 日刊宪《2026 年虚拟资产服务（修订）条例草案》，把虚拟资产交易、顾问、管理及托管四类服务纳入监管：在港经营有关业务者须获证监会发牌或注册并通过适当人选测试；银行及储值支付工具持牌人提供相关服务亦须注册。草案 12 月 2 日提交立法会首读。",
            "tc": "政府 11 月 20 日刊憲《2026 年虛擬資產服務（修訂）條例草案》，把虛擬資產交易、顧問、管理及託管四類服務納入監管：在港經營有關業務者須獲證監會發牌或註冊並通過適當人選測試；銀行及儲值支付工具持牌人提供相關服務亦須註冊。草案 12 月 2 日提交立法會首讀。",
        },
        "why": {
            "sc": "「同一活动、同一风险、同一监管」落到条文，直接改变高客数字资产的合规路径：托管、代币化资产顾问、买卖中介日后都要认清持牌机构。过去「找个平台代持、顺手给点建议」的灰色做法，条例通过后基本没有立足点——对做传承与家办的团队，这是主动重检客户数字资产安排的窗口。",
            "tc": "「同一活動、同一風險、同一監管」落到條文，直接改變高客數字資產的合規路徑：託管、代幣化資產顧問、買賣中介日後都要認清持牌機構。過去「找個平台代持、順手給點建議」的灰色做法，條例通過後基本沒有立足點——對做傳承與家辦的團隊，這是主動重檢客戶數字資產安排的窗口。",
        },
        "actions": {
            "front": {
                "sc": "提醒持有加密资产的高客：托管与买卖安排日后须走持牌机构",
                "tc": "提醒持有加密資產的高客：託管與買賣安排日後須走持牌機構",
            },
            "midback": {
                "sc": "梳理现有客户的数字资产相关服务，标记合规缺口",
                "tc": "梳理現有客戶的數字資產相關服務，標記合規缺口",
            },
            "lead": {
                "sc": "家办与高客服务线的数字资产口径，需在条例通过前统一",
                "tc": "家辦與高客服務線的數字資產口徑，需在條例通過前統一",
            },
            "cross": {
                "sc": "传承架构里涉及数字资产的托管与私钥安排，提前与律师对照新规",
                "tc": "傳承架構裡涉及數字資產的託管與私鑰安排，提前與律師對照新規",
            },
        },
        "rolesImpact": {"front": 1, "midback": 1, "lead": 2, "cross": 3},
        "source": {"sc": "香港特区政府新闻公报", "lang": "zh"},
        "boards": ["reg", "family"],
        "themes": ["regulation", "hong-kong", "digital"],
        "tags": {
            "sc": ["虚拟资产", "证监会", "发牌制度", "家办", "数字资产托管"],
            "tc": ["虛擬資產", "證監會", "發牌制度", "家辦", "數字資產託管"],
        },
        "contentKind": "press",
        "publishedAt": "2026-11-20T17:15:00+08:00",
        "originalUrl": "https://www.info.gov.hk/gia/general/202611/20/P2026112000582.htm",
    },
    {
        "id": "govhk-ai-risk-governance-wg-20261120",
        "clusterCount": 1,
        "score": 86,
        "verifyStatus": "verified",
        "sourceTier": "official",
        "sourceKey": "govhk",
        "title": {
            "sc": "政务司司长主持 AI 风险治理协调工作组首次会议　七项行动含「AI 代理管理指引」",
            "tc": "政務司司長主持 AI 風險治理協調工作組首次會議　七項行動含「AI 代理管理指引」",
        },
        "summary": {
            "sc": "政务司司长陈国基 11 月 20 日主持「AI 风险治理协调工作组」首次会议，统筹落实《施政报告》的 AI 风险治理策略，检视七项行动的工作计划：打击以 AI 犯罪、保护未成年用户、评估 AI 伦理风险、推动各行业安全有序应用、检视 AI 产品事故法律责任、引入 AI 代理管理指引、研究 AI 对就业的影响。",
            "tc": "政務司司長陳國基 11 月 20 日主持「AI 風險治理協調工作組」首次會議，統籌落實《施政報告》的 AI 風險治理策略，檢視七項行動的工作計劃：打擊以 AI 犯罪、保護未成年用戶、評估 AI 倫理風險、推動各行業安全有序應用、檢視 AI 產品事故法律責任、引入 AI 代理管理指引、研究 AI 對就業的影響。",
        },
        "why": {
            "sc": "香港把 AI 治理从「各部门各自出指引」升格为跨局协调。其中「AI 代理管理指引」与「AI 产品事故法律责任」两条，直接关系到前线用 AI 工具做销售、核保、客服时责任落在谁头上。对做团队赋能的人是明确信号：工具可以先上，但权限边界、操作留痕与责任归属要同时备好。",
            "tc": "香港把 AI 治理從「各部門各自出指引」升格為跨局協調。其中「AI 代理管理指引」與「AI 產品事故法律責任」兩條，直接關係到前線用 AI 工具做銷售、核保、客服時責任落在誰頭上。對做團隊賦能的人是明確信號：工具可以先上，但權限邊界、操作留痕與責任歸屬要同時備好。",
        },
        "actions": {
            "front": {
                "sc": "对客讲解 AI 服务时，讲「有框架、有留痕」，不讲「无监管」",
                "tc": "對客講解 AI 服務時，講「有框架、有留痕」，不講「無監管」",
            },
            "midback": {
                "sc": "把 AI 工具的使用边界与审计留痕写进内部操作规范",
                "tc": "把 AI 工具的使用邊界與審計留痕寫進內部操作規範",
            },
            "lead": {
                "sc": "留意 AI 代理管理指引出台时间，提前预留合规预算",
                "tc": "留意 AI 代理管理指引出台時間，提前預留合規預算",
            },
            "cross": {
                "sc": "家族企业客户的 AI 使用政策，可顺势做一次盘点",
                "tc": "家族企業客戶的 AI 使用政策，可順勢做一次盤點",
            },
        },
        "rolesImpact": {"front": 3, "midback": 3, "lead": 2, "cross": 2},
        "source": {"sc": "香港特区政府新闻公报", "lang": "zh"},
        "boards": ["tech", "reg"],
        "themes": ["ai-governance", "hong-kong", "regulation"],
        "tags": {
            "sc": ["AI 治理", "AI 代理", "施政报告", "跨局协调", "合规"],
            "tc": ["AI 治理", "AI 代理", "施政報告", "跨局協調", "合規"],
        },
        "contentKind": "press",
        "publishedAt": "2026-11-20T13:13:00+08:00",
        "originalUrl": "https://www.info.gov.hk/gia/general/202611/20/P2026112000407.htm",
    },
    {
        "id": "ian-kumamoto-quake-payouts-800m-20261120",
        "clusterCount": 1,
        "score": 72,
        "verifyStatus": "verified",
        "sourceTier": "pro",
        "sourceKey": "insuranceasianews",
        "title": {
            "sc": "熊本地震住宅地震险赔款升至 1,265 亿日元　GIAJ：查勘推进、赔付仍在累积",
            "tc": "熊本地震住宅地震險賠款升至 1,265 億日元　GIAJ：查勘推進、賠付仍在累積",
        },
        "summary": {
            "sc": "日本损害保险协会（GIAJ）公布，7 月熊本地震的住宅地震保险赔款已累计 1,265 亿日元（约 7.94 亿美元），远高于 9 月中约 238 亿日元的水平，反映查勘逐批推进后赔付持续上修、尚未封顶。",
            "tc": "日本損害保險協會（GIAJ）公布，7 月熊本地震的住宅地震保險賠款已累計 1,265 億日元（約 7.94 億美元），遠高於 9 月中約 238 億日元的水平，反映查勘逐批推進後賠付持續上修、尚未封頂。",
        },
        "why": {
            "sc": "同一场地震，住宅险赔款从 9 月的 238 亿日元涨到 1,265 亿日元，五倍级的差距不是新损失，而是「查勘没走完时数字必然偏低」。巨灾定价与再保合约的重置，靠的就是这类滞后上修的真实曲线；对客户则是提醒——地震险从报案到定损，本来就是以月计的事。",
            "tc": "同一場地震，住宅險賠款從 9 月的 238 億日元漲到 1,265 億日元，五倍級的差距不是新損失，而是「查勘沒走完時數字必然偏低」。巨災定價與再保合約的重置，靠的就是這類滯後上修的真實曲線；對客戶則是提醒——地震險從報案到定損，本來就是以月計的事。",
        },
        "actions": {
            "front": {
                "sc": "向客户说明天灾理赔周期以月计，报案后先保存现场影像与票据",
                "tc": "向客戶說明天災理賠週期以月計，報案後先保存現場影像與票據",
            },
            "midback": {
                "sc": "按上修后的损失重跑巨灾累计与再保起赔点的压力测试",
                "tc": "按上修後的損失重跑巨災累計與再保起賠點的壓力測試",
            },
            "lead": {
                "sc": "对财产险组合的巨灾敞口做一次年中体检",
                "tc": "對財產險組合的巨災敞口做一次年中體檢",
            },
            "cross": {
                "sc": "高客的不动产组合，检查地震与洪水附加保障是否覆盖",
                "tc": "高客的不動產組合，檢查地震與洪水附加保障是否覆蓋",
            },
        },
        "rolesImpact": {"front": 1, "midback": 3, "lead": 2, "cross": 2},
        "source": {"sc": "InsuranceAsia News（引 GIAJ）", "lang": "en"},
        "boards": ["market"],
        "themes": ["catastrophe", "japan", "claims"],
        "tags": {
            "sc": ["熊本地震", "地震险", "GIAJ", "赔款上修", "巨灾"],
            "tc": ["熊本地震", "地震險", "GIAJ", "賠款上修", "巨災"],
        },
        "contentKind": "stats",
        "publishedAt": "2026-11-20T16:30:00+08:00",
        "originalUrl": "https://insuranceasianews.com/kumamoto-earthquake-insurance-payouts-climb-to-us800m-giaj/",
    },
    {
        "id": "ian-gift-city-ils-20261120",
        "clusterCount": 1,
        "score": 70,
        "verifyStatus": "verified",
        "sourceTier": "pro",
        "sourceKey": "insuranceasianews",
        "title": {
            "sc": "印度 GIFT City 拟让特殊目的保险人入场　巨灾债券与 ILS 可在特区内发行",
            "tc": "印度 GIFT City 擬讓特殊目的保險人入場　巨災債券與 ILS 可在特區內發行",
        },
        "summary": {
            "sc": "印度 GIFT City 金融特区监管机构（IFSCA）正研究允许特殊目的保险人（SPI）进驻经济特区，在区内承做巨灾债券及其他保险相连证券（ILS）业务，为印度市场引入离岸式的风险转移工具。",
            "tc": "印度 GIFT City 金融特區監管機構（IFSCA）正研究允許特殊目的保險人（SPI）進駐經濟特區，在區內承做巨災債券及其他保險相連證券（ILS）業務，為印度市場引入離岸式的風險轉移工具。",
        },
        "why": {
            "sc": "ILS 是香港近两年明确要抢的赛道：至今累计 8 宗，其中 7 宗巨灾债券，上月更出了首宗侧挂车。印度用特区税制加 SPI 入场，抢的是同一批 sponsor 与同一批巨灾资本——亚洲的风险证券化正从「香港独选」变成多点竞争。",
            "tc": "ILS 是香港近兩年明確要搶的賽道：至今累計 8 宗，其中 7 宗巨災債券，上月更出了首宗側掛車。印度用特區稅制加 SPI 入場，搶的是同一批 sponsor 與同一批巨災資本——亞洲的風險證券化正從「香港獨選」變成多點競爭。",
        },
        "actions": {
            "front": {
                "sc": "对高客讲 ILS 时说明：这是机构与合格投资者市场，不是零售保单",
                "tc": "對高客講 ILS 時說明：這是機構與合格投資者市場，不是零售保單",
            },
            "midback": {
                "sc": "跟踪区内 ILS 与侧挂车发行节奏，掌握资本成本参考",
                "tc": "跟蹤區內 ILS 與側掛車發行節奏，掌握資本成本參考",
            },
            "lead": {
                "sc": "香港 ILS 政策优势要靠发行案例维持，留意后续政策与补贴",
                "tc": "香港 ILS 政策優勢要靠發行案例維持，留意後續政策與補貼",
            },
            "cross": {
                "sc": "家办的另类资产配置可关注 ILS 的分散性，但须先过合格投资者门槛",
                "tc": "家辦的另類資產配置可關注 ILS 的分散性，但須先過合格投資者門檻",
            },
        },
        "rolesImpact": {"front": 1, "midback": 1, "lead": 2, "cross": 2},
        "source": {"sc": "InsuranceAsia News", "lang": "en"},
        "boards": ["market"],
        "themes": ["ils", "catastrophe", "india"],
        "tags": {
            "sc": ["GIFT City", "ILS", "巨灾债券", "特殊目的保险人", "印度"],
            "tc": ["GIFT City", "ILS", "巨災債券", "特殊目的保險人", "印度"],
        },
        "contentKind": "news",
        "publishedAt": "2026-11-20T15:54:00+08:00",
        "originalUrl": "https://insuranceasianews.com/gift-city-regulator-moves-to-open-doors-to-cat-bonds-ils/",
    },
    {
        "id": "ia-aia-sg-caregiving-20261120",
        "clusterCount": 1,
        "score": 72,
        "verifyStatus": "verified",
        "sourceTier": "pro",
        "sourceKey": "insuranceasia",
        "title": {
            "sc": "AIA 新加坡调查：77% 不确定保险能否覆盖照护开支　仅两成准照护者自认准备好",
            "tc": "AIA 新加坡調查：77% 不確定保險能否覆蓋照護開支　僅兩成準照護者自認準備好",
        },
        "summary": {
            "sc": "AIA 新加坡「Live Better」研究显示，77% 受访者对长期照护费用及现有保险是否足够感到不确定；26% 不知道照护要花多少钱、22% 未备好资金，仅 20% 的未来照护者自认准备充分；72% 受访者已以某种形式参与照护或受照护。",
            "tc": "AIA 新加坡「Live Better」研究顯示，77% 受訪者對長期照護費用及現有保險是否足夠感到不確定；26% 不知道照護要花多少錢、22% 未備好資金，僅 20% 的未來照護者自認準備充分；72% 受訪者已以某種形式參與照護或受照護。",
        },
        "why": {
            "sc": "照护是长寿风险里最难开口、也最刚需的一块——客户不是不肯买，是不知道要买多少。这类调查可以直接变成客户沟通会的开场问题（「你算过父母十年照护要花多少吗」），比讲产品条款有效得多。亚太人口结构同向，香港客户的心理账户与新加坡高度相似。",
            "tc": "照護是長壽風險裡最難開口、也最剛需的一塊——客戶不是不肯買，是不知道要買多少。這類調查可以直接變成客戶溝通會的開場問題（「你算過父母十年照護要花多少嗎」），比講產品條款有效得多。亞太人口結構同向，香港客戶的心理賬戶與新加坡高度相似。",
        },
        "actions": {
            "front": {
                "sc": "客户沟通会开场用「照护成本算过没有」破题，而不是先讲产品",
                "tc": "客戶溝通會開場用「照護成本算過沒有」破題，而不是先講產品",
            },
            "midback": {
                "sc": "把长期照护缺口纳入保障检视清单的固定项",
                "tc": "把長期照護缺口納入保障檢視清單的固定項",
            },
            "lead": {
                "sc": "长寿与照护是可持续的产品线，但要先配一套讲得清的成本口径",
                "tc": "長壽與照護是可持續的產品線，但要先配一套講得清的成本口徑",
            },
            "cross": {
                "sc": "高客的家族照护安排，与传承和保险结构一并规划",
                "tc": "高客的家族照護安排，與傳承和保險結構一併規劃",
            },
        },
        "rolesImpact": {"front": 3, "midback": 1, "lead": 2, "cross": 2},
        "source": {"sc": "InsuranceAsia（引 AIA 新加坡研究）", "lang": "en"},
        "boards": ["insurer", "product"],
        "themes": ["protection-gap", "health", "retirement"],
        "tags": {
            "sc": ["长期照护", "AIA 新加坡", "长寿风险", "保障缺口", "调查"],
            "tc": ["長期照護", "AIA 新加坡", "長壽風險", "保障缺口", "調查"],
        },
        "contentKind": "news",
        "publishedAt": "2026-11-20T05:00:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/in-focus/two-in-five-singaporeans-unsure-if-insurance-can-cover-caregiving-costs",
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

    shutil.copy(LIVE, LIVE + '.bak-1120-1808')
    json.dump(d, open(LIVE, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('total now:', len(d['items']))


if __name__ == '__main__':
    main()
