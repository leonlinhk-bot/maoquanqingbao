window.HKII_DATA = {
  "meta": {
    "product": "猫圈儿港险情报站",
    "generatedAt": "2026-08-06T18:08:00+08:00",
    "itemCount": 305,
    "windowNote": {
      "sc": "本库305条。",
      "tc": "本庫305條。"
    },
    "sourcesPrimary": [
      "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html",
      "https://www.ia.org.hk/en/infocenter/statistics/statistics.html",
      "https://www.ia.org.hk/en/supervision/reg_insurers_lloyd/register_of_authorized_insurers.html",
      "https://www.hkma.gov.hk/eng/news-and-media/press-releases/",
      "data/sources.yaml",
      "data/ia-fulfillment-insurers.json",
      "data/ia-authorized-insurers.json"
    ],
    "archive": {
      "principle": {
        "sc": "双层：时效层（脉搏/生效中）+ 档案层（日/周/月/年索引）。条目可长期检索；摘要为导读，原文链接为唯一权威。",
        "tc": "雙層：時效層（脈搏/生效中）+ 檔案層（日/週/月/年索引）。條目可長期檢索；摘要為導讀，原文連結為唯一權威。"
      },
      "paths": {
        "items": "data/live-items.json",
        "daily": "data/archive/daily/",
        "weekly": "data/archive/weekly/",
        "monthly": "data/archive/monthly/",
        "yearly": "data/archive/yearly/",
        "sources": "data/sources-registry.json"
      }
    },
    "monetization": {
      "enabled": false,
      "currency": "points",
      "prices": {
        "daily": 0,
        "weekly": 30,
        "monthly": 80,
        "yearly": 200
      },
      "posterFree": true,
      "mdItemFree": true,
      "note": {
        "sc": "浏览与单条/打包下载长期倾向免费；周月年打包可走积分或 Pro。当前对内关闭付费锁。",
        "tc": "瀏覽與單條/打包下載長期傾向免費；週月年打包可走積分或 Pro。當前對內關閉付費鎖。"
      }
    },
    "positioning": {
      "sc": "定位=港险相关官方/一手资讯的高效汇聚与可追溯导读。不替代保司原文，不做分红实现率数据库（另有公司工具）。",
      "tc": "定位=港險相關官方/一手資訊的高效匯聚與可追溯導讀。不替代保司原文，不做分紅實現率數據庫（另有公司工具）。"
    },
    "sourcesCatalog": {
      "version": "0.3.2",
      "updatedAt": "2026-07-27",
      "principle": {
        "sc": "一手官方资讯优先；保司侧抓「官网披露/通告/新闻」作信息差打通，不深挖实现率表格。",
        "tc": "一手官方資訊優先；保司側抓「官網披露/通告/新聞」作信息差打通，不深挖實現率表格。"
      },
      "layers": [
        {
          "id": "regulator",
          "title": {
            "sc": "监管一手",
            "tc": "監管一手"
          },
          "countNote": {
            "sc": "IA 通函/新闻/演辞/统计 + 名册/实现率入口索引；HKMA 新闻",
            "tc": "IA 通函/新聞/演辭/統計 + 名冊/實現率入口索引；HKMA 新聞"
          },
          "hubs": [
            "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html",
            "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2025.html",
            "https://www.ia.org.hk/tc/infocenter/speeches_articles.html",
            "https://www.ia.org.hk/en/infocenter/statistics/statistics.html"
          ]
        },
        {
          "id": "insurer_news",
          "title": {
            "sc": "保司官网资讯（产品通告/新闻/披露页）",
            "tc": "保司官網資訊（產品通告/新聞/披露頁）"
          },
          "countNote": {
            "sc": "授权保险人名称索引 163 家；有公开分红披露页的寿险主体 27 家（仅作官网入口索引，本站不汇总实现率数据）。",
            "tc": "授權保險人名稱索引 163 家；有公開分紅披露頁的壽險主體 27 家（僅作官網入口索引，本站不匯總實現率數據）。"
          },
          "files": [
            "data/ia-authorized-insurers.json",
            "data/ia-fulfillment-insurers.json",
            "data/sources-insurers-par.yaml"
          ]
        },
        {
          "id": "research8",
          "title": {
            "sc": "海外机构研究（8）",
            "tc": "海外機構研究（8）"
          },
          "items": [
            "BlackRock",
            "Goldman Sachs",
            "Morgan Stanley",
            "J.P. Morgan",
            "Swiss Re Institute",
            "Allianz Research",
            "PIMCO",
            "UBS"
          ]
        },
        {
          "id": "media6",
          "title": {
            "sc": "国际媒体线索（6）",
            "tc": "國際媒體線索（6）"
          },
          "items": [
            "Bloomberg",
            "Reuters",
            "Financial Times",
            "Wall Street Journal",
            "Risk.net",
            "Nikkei Asia"
          ]
        }
      ],
      "registryFile": "data/sources.yaml"
    },
    "asOf": "2026-08-06",
    "roles": [
      {
        "id": "front",
        "label": {
          "sc": "前线IFA",
          "tc": "前線IFA"
        }
      },
      {
        "id": "midback",
        "label": {
          "sc": "中后台合规",
          "tc": "中後台合規"
        }
      },
      {
        "id": "lead",
        "label": {
          "sc": "团队管理",
          "tc": "團隊管理"
        }
      },
      {
        "id": "cross",
        "label": {
          "sc": "跨境架构",
          "tc": "跨境架構"
        }
      }
    ],
    "cleanedBy": "humanizer v2 - targeted"
  },
  "hot": [
    "ia-public-disclosure-2026",
    "ia-q1-2026-stats",
    "ia-20260716-ashk-ifoa",
    "ia-20260715-sales-practices",
    "ia-licence-20260630",
    "ia-20260712-speech"
  ],
  "items": [
    {
      "id": "cupi-am-best-profits-aug05",
      "clusterCount": 1,
      "score": 72,
      "verifyStatus": "verified",
      "sourceTier": "pro",
      "sourceKey": "insuranceasia:cupi-am-best-20260805",
      "title": {
        "sc": "AM Best：中华联合财险盈利依赖投资收益 承保接近盈亏平衡",
        "tc": "AM Best：中華聯合財險盈利依賴投資收益 承保接近盈虧平衡"
      },
      "summary": {
        "sc": "AM Best研究指出，中华联合财险（CUPI）盈利主要由投资收益驱动，承保结果接近盈亏平衡；2025年资本及盈余增5.4%至27.8亿美元，风险调整后资本维持极强水平。公司为中投旗下国内主要农险保司，占全国非寿险市场约4%、农险市场12%；相对较高承保杠杆及政策性农险大额应收保费为主要抵消因素。[EN原文]",
        "tc": "AM Best研究指出，中華聯合財險（CUPI）盈利主要由投資收益驅動，承保結果接近盈虧平衡；2025年資本及盈餘增5.4%至27.8億美元，風險調整後資本維持極強水平。公司為中投旗下國內主要農險保司，佔全國非壽險市場約4%、農險市場12%；相對較高承保槓桿及政策性農險大額應收保費為主要抵消因素。[EN原文]"
      },
      "why": {
        "sc": "中资财险「承保弱、投资补」困局+主权基金股东支持的样本，可与港险财险板块承保表现对照；政策性农险应收保费风险亦是理解内地财险报表的素材。",
        "tc": "中資財險「承保弱、投資補」困局+主權基金股東支持的樣本，可與港險財險板塊承保表現對照；政策性農險應收保費風險亦是理解內地財險報表的素材。"
      },
      "actions": {
        "front": {
          "sc": "投资收益撑盈利=内地财险承保仍弱",
          "tc": "投資收益撐盈利=內地財險承保仍弱"
        },
        "midback": {
          "sc": "农险应收保费=政策性业务的报表风险点",
          "tc": "農險應收保費=政策性業務的報表風險點"
        },
        "lead": {
          "sc": "中投股东支持=资本实力背书",
          "tc": "中投股東支持=資本實力背書"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 0,
        "midback": 2,
        "lead": 1,
        "cross": 0
      },
      "source": {
        "sc": "Insurance Asia / AM Best",
        "tc": "Insurance Asia / AM Best",
        "lang": "en"
      },
      "boards": [
        "insurer"
      ],
      "themes": [
        "firm",
        "market"
      ],
      "tags": {
        "sc": [
          "AM Best",
          "中华联合财险",
          "投资收益",
          "农险",
          "评级"
        ],
        "tc": [
          "AM Best",
          "中華聯合財險",
          "投資收益",
          "農險",
          "評級"
        ]
      },
      "contentKind": "research",
      "publishedAt": "2026-08-05T05:30:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/news/investment-income-props-china-united-property-profits",
      "ingestedAt": "2026-08-06T18:08:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "beazley-h1-profits-halve-aug05",
      "clusterCount": 1,
      "score": 64,
      "verifyStatus": "verified",
      "sourceTier": "media",
      "sourceKey": "insurancebusinessmag:beazley-h1-20260805",
      "title": {
        "sc": "Beazley上半年税前利润腰斩53% 网络险费率连跌12季 苏黎世收购推进中",
        "tc": "Beazley上半年稅前利潤腰斬53% 網絡險費率連跌12季 蘇黎世收購推進中"
      },
      "summary": {
        "sc": "伦敦上市专业险企Beazley上半年税前利润2.377亿美元，同比降53%；综合成本率升至93.3%。全球网络险费率二季度再跌4%、连续12季下行，商业险整体费率跌6%；公司主动收缩美国网络险敞口、转向百慕大平台，MAP风险业务因中东局势增长6.1%。苏黎世81亿英镑收购待多监管审批，预计下半年完成。[EN原文]",
        "tc": "倫敦上市專業險企Beazley上半年稅前利潤2.377億美元，同比降53%；綜合成本率升至93.3%。全球網絡險費率二季度再跌4%、連續12季下行，商業險整體費率跌6%；公司主動收縮美國網絡險敞口、轉向百慕大平台，MAP風險業務因中東局勢增長6.1%。蘇黎世81億英鎊收購待多監管審批，預計下半年完成。[EN原文]"
      },
      "why": {
        "sc": "网络险价格周期见顶回落+中东地缘风险推高索赔，是亚太及香港网络险与marine war风险定价的背景板；苏黎世收购Beazley亦将重塑全球专业险格局。",
        "tc": "網絡險價格週期見頂回落+中東地緣風險推高索賠，是亞太及香港網絡險與marine war風險定價的背景板；蘇黎世收購Beazley亦將重塑全球專業險格局。"
      },
      "actions": {
        "front": {
          "sc": "网络险费率12季连跌=价格周期见顶",
          "tc": "網絡險費率12季連跌=價格週期見頂"
        },
        "midback": {
          "sc": "中东冲突推高MAP索赔=地缘风险传导",
          "tc": "中東衝突推高MAP索賠=地緣風險傳導"
        },
        "lead": {
          "sc": "苏黎世收购年内完成=专业险格局生变",
          "tc": "蘇黎世收購年內完成=專業險格局生變"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 1,
        "midback": 2,
        "lead": 1,
        "cross": 1
      },
      "source": {
        "sc": "Insurance Business Asia / Beazley",
        "tc": "Insurance Business Asia / Beazley",
        "lang": "en"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "market",
        "tech"
      ],
      "tags": {
        "sc": [
          "Beazley",
          "网络险",
          "费率周期",
          "苏黎世",
          "专业险"
        ],
        "tc": [
          "Beazley",
          "網絡險",
          "費率週期",
          "蘇黎世",
          "專業險"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-08-05T14:30:00+08:00",
      "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/beazleys-profits-halve-as-cyber-prices-and-middle-east-squeeze-the-market-584983.aspx",
      "ingestedAt": "2026-08-06T18:08:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "korea-health-gap-brokers-aug05",
      "clusterCount": 1,
      "score": 66,
      "verifyStatus": "verified",
      "sourceTier": "media",
      "sourceKey": "insurancebusinessmag:korea-health-gap-20260805",
      "title": {
        "sc": "韩国健康险三重压力：公共医保财政悬崖+补偿险亏损1.87万亿韩元+佣金分期改革",
        "tc": "韓國健康險三重壓力：公共醫保財政懸崖+補償險虧損1.87萬億韓元+佣金分期改革"
      },
      "summary": {
        "sc": "韩国健康保险市场面临三重结构性压力：国民健康保险储备预计2030年耗尽、2042年年度赤字达123万亿韩元；私人补偿型健康险2025年亏损1.87万亿韩元、赔付率101%；分销端自2027年1月起佣金改为四年分期、2029年延至七年，首年佣金1200%上限扩大至个人代理。72%韩民持有商业健康险，公共体系仅覆盖医疗支出62.3%。[EN原文]",
        "tc": "韓國健康保險市場面臨三重結構性壓力：國民健康保險儲備預計2030年耗盡、2042年年度赤字達123萬億韓元；私人補償型健康險2025年虧損1.87萬億韓元、賠付率101%；分銷端自2027年1月起佣金改為四年分期、2029年延至七年，首年佣金1200%上限擴大至個人代理。72%韓民持有商業健康險，公共體系僅覆蓋醫療支出62.3%。[EN原文]"
      },
      "why": {
        "sc": "韩国佣金分期+上限改革与香港佣金设限监管同频，是观察「佣金改革对渠道与产品影响」的对照样本；公共医保财政压力下商业健康险重定价逻辑亦值得港险参考。",
        "tc": "韓國佣金分期+上限改革與香港佣金設限監管同頻，是觀察「佣金改革對渠道與產品影響」的對照樣本；公共醫保財政壓力下商業健康險重定價邏輯亦值得港險參考。"
      },
      "actions": {
        "front": {
          "sc": "佣金分期改革=与香港佣金设限同频",
          "tc": "佣金分期改革=與香港佣金設限同頻"
        },
        "midback": {
          "sc": "公共医保财政悬崖=商业健康险需求上行",
          "tc": "公共醫保財政懸崖=商業健康險需求上行"
        },
        "lead": {
          "sc": "赔付率101%=重定价周期开启",
          "tc": "賠付率101%=重定價週期開啟"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 2,
        "midback": 1,
        "lead": 1,
        "cross": 1
      },
      "source": {
        "sc": "Insurance Business Asia",
        "tc": "Insurance Business Asia",
        "lang": "en"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "channel",
        "market"
      ],
      "tags": {
        "sc": [
          "韩国",
          "健康险",
          "佣金改革",
          "医保赤字",
          "重定价"
        ],
        "tc": [
          "韓國",
          "健康險",
          "佣金改革",
          "醫保赤字",
          "重定價"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-08-05T10:00:00+08:00",
      "originalUrl": "https://www.insurancebusinessmag.com/asia/news/life-insurance/south-koreas-health-coverage-gap-is-widening--and-brokers-are-in-the-middle-585038.aspx",
      "ingestedAt": "2026-08-06T18:08:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "china-hk-policy-tax-aug05",
      "clusterCount": 3,
      "score": 86,
      "verifyStatus": "verified",
      "sourceTier": "media",
      "sourceKey": "caixin:hk-policy-tax-20260805",
      "title": {
        "sc": "内地开始对香港保单收益征20%个税：北京杭州已执行 保诚领跌",
        "tc": "內地開始對香港保單收益徵20%個稅：北京杭州已執行 保誠領跌"
      },
      "summary": {
        "sc": "财新独家：内地税务机关已开始对境外保单收益征个税，北京、杭州已有执行案例，对香港保单分红及预缴保费利息适用20%税率；CRS数据共享令征管落地，预计执行趋严。消息令保诚股价一度跌13%，汇丰、渣打跟随下挫。",
        "tc": "財新獨家：內地稅務機關已開始對境外保單收益徵個稅，北京、杭州已有執行案例，對香港保單分紅及預繳保費利息適用20%稅率；CRS數據共享令徵管落地，預計執行趨嚴。消息令保誠股價一度跌13%，匯豐、渣打跟隨下挫。"
      },
      "why": {
        "sc": "继7月离岸信托个税新规后，内地对跨境金融资产的又一次定向收紧，直接冲击MCV储蓄险的税后回报叙事。对IFA：与内地客群沟通必须前置税务合规议题，「保单收益免税」话术已不可用；对持有多张储蓄保单的内地客户，这是需要主动提示的风险事件。",
        "tc": "繼7月離岸信託個稅新規後，內地對跨境金融資產的又一次定向收緊，直接衝擊MCV儲蓄險的稅後回報敘事。對IFA：與內地客群溝通必須前置稅務合規議題，「保單收益免稅」話術已不可用；對持有多張儲蓄保單的內地客戶，這是需要主動提示的風險事件。"
      },
      "actions": {
        "front": {
          "sc": "内地对港险收益征税落地=储蓄险税后回报逻辑生变",
          "tc": "內地對港險收益徵稅落地=儲蓄險稅後回報邏輯生變"
        },
        "midback": {
          "sc": "CRS交换+20%税率=征管闭环正在形成",
          "tc": "CRS交換+20%稅率=徵管閉環正在形成"
        },
        "lead": {
          "sc": "MCV客户需重新评估税后IRR与持有结构",
          "tc": "MCV客戶需重新評估稅後IRR與持有結構"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 3,
        "midback": 2,
        "lead": 3,
        "cross": 1
      },
      "source": {
        "sc": "财新网 / Reuters",
        "lang": "zh"
      },
      "boards": [
        "reg",
        "market"
      ],
      "themes": [
        "compliance",
        "offshore",
        "macro"
      ],
      "tags": {
        "sc": [
          "境外保单征税",
          "个税",
          "CRS",
          "MCV",
          "保诚"
        ],
        "tc": [
          "境外保單徵稅",
          "個稅",
          "CRS",
          "MCV",
          "保誠"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-08-05T17:31:00+08:00",
      "originalUrl": "https://finance.caixin.com/m/2026-08-05/102471513.html",
      "ingestedAt": "2026-08-05T18:15:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "nfra-audit-liability-aug05",
      "clusterCount": 1,
      "score": 85,
      "verifyStatus": "pending",
      "sourceTier": "official",
      "sourceKey": "nfra:audit-liability-insurance-20260805",
      "title": {
        "sc": "金融监管总局：新修订《会计师事务所职业责任保险实施办法》拟近期印发 费率与合规记录挂钩",
        "tc": "金融監管總局：新修訂《會計師事務所職業責任保險實施辦法》擬近期印發 費率與合規記錄掛鉤"
      },
      "summary": {
        "sc": "金融监管总局答复政协提案：与财政部联合起草的新修订《会计师事务所职业责任保险实施办法》拟近期印发。办法将事务所处罚、涉诉及历史赔付记录与费率挂钩，鼓励共保提升承保能力，增设账册丢失、追溯期扩展等附加险，并设职业责任保险专家委员会。[EN原文]",
        "tc": "金融監管總局答覆政協提案：與財政部聯合起草的新修訂《會計師事務所職業責任保險實施辦法》擬近期印發。辦法將事務所處罰、涉訴及歷史賠付記錄與費率掛鉤，鼓勵共保提升承保能力，增設賬冊丟失、追溯期擴展等附加險，並設職業責任保險專家委員會。[EN原文]"
      },
      "why": {
        "sc": "责任险「费率与合规记录挂钩」是内地财险定价精细化的最新样本，方向与港险佣金及定价监管趋同；对关注内地保险政策的中介机构，这是理解职业责任险市场扩容（含大湾区跨境执业需求）的参照。",
        "tc": "責任險「費率與合規記錄掛鉤」是內地財險定價精細化的最新樣本，方向與港險佣金及定價監管趨同；對關注內地保險政策的中介機構，這是理解職業責任險市場擴容（含大灣區跨境執業需求）的參照。"
      },
      "actions": {
        "front": {
          "sc": "责任险费率挂钩合规记录=定价精细化",
          "tc": "責任險費率掛鉤合規記錄=定價精細化"
        },
        "midback": {
          "sc": "共保+附加险=职业责任险扩容信号",
          "tc": "共保+附加險=職業責任險擴容信號"
        },
        "lead": {
          "sc": "关注印发后的行业示范条款",
          "tc": "關注印發後的行業示範條款"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 1,
        "midback": 1,
        "lead": 1,
        "cross": 0
      },
      "source": {
        "sc": "金融监管总局（via 新浪财经/金融一线）",
        "lang": "zh"
      },
      "boards": [
        "reg"
      ],
      "themes": [
        "reg",
        "product"
      ],
      "tags": {
        "sc": [
          "职业责任保险",
          "会计师事务所",
          "费率挂钩",
          "金融监管总局",
          "共保"
        ],
        "tc": [
          "職業責任保險",
          "會計師事務所",
          "費率掛鉤",
          "金融監管總局",
          "共保"
        ]
      },
      "contentKind": "circular",
      "publishedAt": "2026-08-05T10:33:00+08:00",
      "originalUrl": "http://m.toutiao.com/group/7670370104106680882/",
      "ingestedAt": "2026-08-05T18:15:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "boclife-ai-cohort-2026",
      "clusterCount": 1,
      "score": 74,
      "verifyStatus": "verified",
      "sourceTier": "insurer",
      "sourceKey": "boclife",
      "title": {
        "sc": "中银人寿加入保监局 AI 促进计划：深化负责任的 AI 应用",
        "tc": "中銀人壽加入保監局 AI 促進計劃：深化負責任的 AI 應用"
      },
      "summary": {
        "sc": "中银人寿宣布参与保险业监管局「人工智能促进计划」（AI Cohort Programme），深化科技赋能、推动负责任的 AI 应用，提升客户体验。该计划由保监局主导，已覆盖 AIA、宏利、保诚、AXA 等主要保司。",
        "tc": "中銀人壽宣佈參與保險業監管局「人工智能促進計劃」（AI Cohort Programme），深化科技賦能、推動負責任的 AI 應用，提升客戶體驗。"
      },
      "why": {
        "sc": "AI Cohort 从「巨头俱乐部」扩展到银保系玩家=监管主导的 AI 试点正在全行业铺开。对 IFA：理解保司的 AI 布局方向（客服/核保/销售工具），是判断服务体验迭代的先行指标。",
        "tc": "AI Cohort 從「巨頭俱樂部」擴展到銀保系玩家=監管主導的 AI 試點正在全行業鋪開。對 IFA：理解保司的 AI 佈局方向，是判斷服務體驗迭代的先行指標。"
      },
      "actions": {
        "front": {
          "sc": "银保系加入AI试点=全行业AI应用铺开",
          "tc": "銀保系加入AI試點=全行業AI應用鋪開"
        },
        "midback": {
          "sc": "负责任AI=监管关注的核心原则",
          "tc": "負責任AI=監管關注的核心原則"
        },
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 3,
        "midback": 3,
        "lead": 2,
        "cross": 2
      },
      "source": {
        "sc": "中银人寿 · 2026年8月",
        "lang": "sc"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "tech",
        "insurtech"
      ],
      "tags": {
        "sc": [
          "AI",
          "中银人寿",
          "监管试点"
        ],
        "tc": [
          "AI",
          "中銀人壽",
          "監管試點"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2026-08-05T10:00:00+08:00",
      "originalUrl": "https://www.boclife.com.hk/tc/news/boc-life-joins-insurance-authority-s-ai-cohort-programme-to-advance-responsible-ai-adoption-and-elevate-customer-experience.html"
    },
    {
      "id": "maybank-etiqa-202608",
      "clusterCount": 1,
      "score": 68,
      "verifyStatus": "pending",
      "sourceTier": "media",
      "sourceKey": "insuranceasia",
      "title": {
        "sc": "马银行 12 亿美元收购 Etiqa 全部控制权：东南亚保险整合加速",
        "tc": "馬銀行 12 億美元收購 Etiqa 全部控制權：東南亞保險整合加速"
      },
      "summary": {
        "sc": "Maybank（马来亚银行）以 12 亿美元收购 Etiqa 全部控制权，此前已持有 69.05% 股权。Etiqa 是东南亚重要保险公司。交易显示银行系保险整合在东南亚加速。",
        "tc": "Maybank（馬來亞銀行）以 12 億美元收購 Etiqa 全部控制權，此前已持有 69.05% 股權。Etiqa 是東南亞重要保險公司。"
      },
      "why": {
        "sc": "东南亚保险整合是观察香港市场的参照系——区域资本流向哪里，香港的枢纽角色就有多稳。银行收购保险公司=渠道+产品一体化的趋势在区域内蔓延。",
        "tc": "東南亞保險整合是觀察香港市場的參照系。銀行收購保險公司=渠道+產品一體化的趨勢在區域內蔓延。"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {
          "sc": "区域并购活跃=保险资产价值重估",
          "tc": "區域併購活躍=保險資產價值重估"
        },
        "cross": {
          "sc": "东南亚整合对照香港：枢纽地位不变",
          "tc": "東南亞整合對照香港：樞紐地位不變"
        }
      },
      "rolesImpact": {
        "front": 1,
        "midback": 1,
        "lead": 2,
        "cross": 2
      },
      "source": {
        "sc": "InsuranceAsia · 2026年8月5日",
        "lang": "zh"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "ma",
        "firm"
      ],
      "tags": {
        "sc": [
          "Maybank",
          "Etiqa",
          "并购"
        ],
        "tc": [
          "Maybank",
          "Etiqa",
          "併購"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-08-05T10:00:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/news/maybank-takes-full-control-etiqa-in-12b-deal"
    },
    {
      "id": "jefferies-hk-sales-soar-aug05",
      "clusterCount": 1,
      "score": 72,
      "verifyStatus": "verified",
      "sourceTier": "pro",
      "sourceKey": "insuranceasia:jefferies-hk-sales-20260805",
      "title": {
        "sc": "Jefferies：港险Q1新单保费+51%创新高 银保+48%经纪+60% MCV到访年累计破2000万",
        "tc": "Jefferies：港險Q1新單保費+51%創新高 銀保+48%經紀+60% MCV到訪年累計破2000萬"
      },
      "summary": {
        "sc": "Jefferies研报：香港寿险Q1直接个人新单保费同比+51%至逾1400亿港元创历史新高，增速与2025全年持平；银保+48%、经纪+60%领跑，友邦市占率保持稳定。MCV访客年累计破2000万人次（+16%），本地情绪乐观与西方投资者谨慎并存。[EN原文]",
        "tc": "Jefferies研報：香港壽險Q1直接個人新單保費同比+51%至逾1400億港元創歷史新高，增速與2025全年持平；銀保+48%、經紀+60%領跑，友邦市佔率保持穩定。MCV訪客年累計破2000萬人次（+16%），本地情緒樂觀與西方投資者謹慎並存。[EN原文]"
      },
      "why": {
        "sc": "与8月3日「件数仅+2%」条目互补：量价齐升下银保与经纪渠道爆发，港险增长引擎正从代理人转向渠道多元。MCV月均340万人次是后续新单的先行指标，对判断下半年销售动能及友邦8月20日中期业绩有直接参考价值。",
        "tc": "與8月3日「件數僅+2%」條目互補：量價齊升下銀保與經紀渠道爆發，港險增長引擎正從代理人轉向渠道多元。MCV月均340萬人次是後續新單的先行指標，對判斷下半年銷售動能及友邦8月20日中期業績有直接參考價值。"
      },
      "actions": {
        "front": {
          "sc": "Q1保费+51%创新高=下半年动能延续信号",
          "tc": "Q1保費+51%創新高=下半年動能延續信號"
        },
        "midback": {
          "sc": "银保+48%/经纪+60%=渠道结构生变",
          "tc": "銀保+48%/經紀+60%=渠道結構生變"
        },
        "lead": {
          "sc": "关注8月20日友邦中期业绩与MCV动能",
          "tc": "關注8月20日友邦中期業績與MCV動能"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 2,
        "midback": 2,
        "lead": 2,
        "cross": 1
      },
      "source": {
        "sc": "Insurance Asia / Jefferies",
        "lang": "en"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "market",
        "channel",
        "offshore"
      ],
      "tags": {
        "sc": [
          "Jefferies",
          "新单保费",
          "银保渠道",
          "MCV",
          "友邦"
        ],
        "tc": [
          "Jefferies",
          "新單保費",
          "銀保渠道",
          "MCV",
          "友邦"
        ]
      },
      "contentKind": "research",
      "publishedAt": "2026-08-05T06:00:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/news/hong-kong-life-sales-soar-despite-investor-caution-jefferies",
      "ingestedAt": "2026-08-05T18:15:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "etiqa-index-endowment-aug05",
      "clusterCount": 1,
      "score": 65,
      "verifyStatus": "verified",
      "sourceTier": "media",
      "sourceKey": "insuranceasia:etiqa-index-endowment-20260805",
      "title": {
        "sc": "Etiqa新加坡推指数挂钩储蓄计划：挂钩Barclays动态指数 到期保本加0%下限",
        "tc": "Etiqa新加坡推指數掛鉤儲蓄計劃：掛鉤Barclays動態指數 到期保本加0%下限"
      },
      "summary": {
        "sc": "Etiqa新加坡推Enrich Index Income非分红储蓄计划：年度利益挂钩Barclays RADAR 6%指数（美股、债、商品动态配置），到期保本并设0%下限；趸缴或3年缴，含身故及末期疾病保障，免体检。[EN原文]",
        "tc": "Etiqa新加坡推Enrich Index Income非分紅儲蓄計劃：年度利益掛鉤Barclays RADAR 6%指數（美股、債、商品動態配置），到期保本並設0%下限；躉繳或3年繳，含身故及末期疾病保障，免體檢。[EN原文]"
      },
      "why": {
        "sc": "市场波动期「指数挂钩+保本」是亚太储蓄险的应对模板，可与香港分红储蓄产品对照：当演示利率上限压缩收益想象空间，指数策略或成产品创新下一站；对客户沟通也是比较保证/非保证结构的好案例。",
        "tc": "市場波動期「指數掛鉤+保本」是亞太儲蓄險的應對模板，可與香港分紅儲蓄產品對照：當演示利率上限壓縮收益想象空間，指數策略或成產品創新下一站；對客戶溝通也是比較保證/非保證結構的好案例。"
      },
      "actions": {
        "front": {
          "sc": "指数挂钩+保本=储蓄险新形态样本",
          "tc": "指數掛鉤+保本=儲蓄險新形態樣本"
        },
        "midback": {
          "sc": "0%下限设计=下行保护的沟通话术",
          "tc": "0%下限設計=下行保護的溝通話術"
        },
        "lead": {
          "sc": "留意港险是否跟进指数挂钩类产品",
          "tc": "留意港險是否跟進指數掛鉤類產品"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 2,
        "midback": 1,
        "lead": 1,
        "cross": 0
      },
      "source": {
        "sc": "Insurance Asia / Etiqa",
        "lang": "en"
      },
      "boards": [
        "product"
      ],
      "themes": [
        "product",
        "market"
      ],
      "tags": {
        "sc": [
          "Etiqa",
          "指数挂钩",
          "储蓄计划",
          "保本",
          "新加坡"
        ],
        "tc": [
          "Etiqa",
          "指數掛鉤",
          "儲蓄計劃",
          "保本",
          "新加坡"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-08-05T05:45:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/news/etiqa-launches-endowment-plan-amidst-volatility-fears",
      "ingestedAt": "2026-08-05T18:15:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "apac-natcat-h1-2026-aug05",
      "clusterCount": 1,
      "score": 70,
      "verifyStatus": "verified",
      "sourceTier": "media",
      "sourceKey": "insuranceasia:apac-natcat-h1-20260805",
      "title": {
        "sc": "Munich Re：亚太上半年巨灾损失远低于均值 中国5月洪灾损失28亿美元大部分无保险",
        "tc": "Munich Re：亞太上半年巨災損失遠低於均值 中國5月洪災損失28億美元大部分無保險"
      },
      "summary": {
        "sc": "慕再：亚太上半年巨灾经济损失约87亿美元、保险赔付仅逾10亿，远低于10年均值（320亿/50亿）；中国5月洪灾损失28亿美元大部分无保险，澳洲山火约三分之二获赔。全球上半年巨灾损失1120亿、保险覆盖440亿，60%无保障；厄尔尼诺或推高下半年风险。[EN原文]",
        "tc": "慕再：亞太上半年巨災經濟損失約87億美元、保險賠付僅逾10億，遠低於10年均值（320億/50億）；中國5月洪災損失28億美元大部分無保險，澳洲山火約三分之二獲賠。全球上半年巨災損失1120億、保險覆蓋440億，60%無保障；厄爾尼諾或推高下半年風險。[EN原文]"
      },
      "why": {
        "sc": "巨灾低损失基数叠加厄尔尼诺风险上行，是财险/再保定价与高净值客户风险管理的背景板；中国洪灾「投保不足」将保障缺口可视化，也是内地客群财产保障需求的佐证素材。",
        "tc": "巨災低損失基數疊加厄爾尼諾風險上行，是財險/再保定價與高淨值客戶風險管理的背景板；中國洪災「投保不足」將保障缺口可視化，也是內地客群財產保障需求的佐證素材。"
      },
      "actions": {
        "front": {
          "sc": "亚太巨灾赔付低位=财险定价环境仍宽松",
          "tc": "亞太巨災賠付低位=財險定價環境仍寬鬆"
        },
        "midback": {
          "sc": "中国洪灾投保不足=保障缺口可视化",
          "tc": "中國洪災投保不足=保障缺口可視化"
        },
        "lead": {
          "sc": "厄尔尼诺H2风险=再保与巨灾债券关注点",
          "tc": "厄爾尼諾H2風險=再保與巨災債券關注點"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 1,
        "midback": 2,
        "lead": 1,
        "cross": 1
      },
      "source": {
        "sc": "Insurance Asia / Munich Re",
        "lang": "en"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "macro",
        "market"
      ],
      "tags": {
        "sc": [
          "Munich Re",
          "巨灾",
          "厄尔尼诺",
          "洪灾",
          "保险缺口"
        ],
        "tc": [
          "Munich Re",
          "巨災",
          "厄爾尼諾",
          "洪災",
          "保險缺口"
        ]
      },
      "contentKind": "research",
      "publishedAt": "2026-08-05T05:00:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/in-focus/asia-pacific-losses-fall-insured-damage-hits-1b-in-h1-2026",
      "ingestedAt": "2026-08-05T18:15:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "aon-indonesia-ceo-aug04",
      "clusterCount": 1,
      "score": 60,
      "verifyStatus": "pending",
      "sourceTier": "media",
      "sourceKey": "insuranceasia:aon-indonesia-ceo-20260804",
      "title": {
        "sc": "Aon委任Stephen出任印尼业务CEO 前Zurich印尼首席核保官",
        "tc": "Aon委任Stephen出任印尼業務CEO 前Zurich印尼首席核保官"
      },
      "summary": {
        "sc": "怡安（Aon）宣布委任Stephen出任印尼业务首席执行官，其此前担任Zurich印尼业务首席核保官，具备承保与市场管理双重背景。此举反映怡安持续强化东南亚市场领导层布局，为区域内经纪渠道竞争格局再添变量。[EN原文]",
        "tc": "怡安（Aon）委任Stephen出任印尼業務CEO，其此前擔任Zurich印尼首席核保官；反映怡安持續強化東南亞市場領導層佈局，為區域經紀渠道競爭格局再添變量。"
      },
      "why": {
        "sc": "国际经纪商东南亚人事布局=区域分销渠道竞争态势的观察点",
        "tc": "國際經紀商東南亞人事佈局=區域分銷渠道競爭態勢的觀察點"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 0,
        "midback": 1,
        "lead": 1,
        "cross": 1
      },
      "source": {
        "sc": "Insurance Asia / Aon",
        "tc": "Insurance Asia / Aon",
        "lang": "en"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "talent",
        "channel"
      ],
      "tags": {
        "sc": [
          "Aon",
          "印尼",
          "人事任命",
          "经纪"
        ],
        "tc": [
          "Aon",
          "印尼",
          "人事任命",
          "經紀"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-08-04T12:17:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/news/aon-names-stephen-new-ceo-indonesia-business",
      "ingestedAt": "2026-08-04T18:17:37.402180+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "moodys-ai-distribution-aug04",
      "clusterCount": 1,
      "score": 66,
      "verifyStatus": "verified",
      "sourceTier": "media",
      "sourceKey": "insurancebusinessmag:moodys-ai-distribution-20260804",
      "title": {
        "sc": "Moody's：零售财险分销是全金融业最受AI冲击环节 限期12-18个月",
        "tc": "Moody's：零售財險分銷是全金融業最受AI衝擊環節 限期12-18個月"
      },
      "summary": {
        "sc": "穆迪报告指零售产险分销因交易量大、流程标准化、产品商品化，是金融业中最受AI近端冲击的业务线；AI将压缩客户与机构之间的信息差，比价、风险评估等顾问服务可被客户自行复制。具转换成本、专精复杂风险与问责信任关系的分销商仍可保定价权，基线情景下多数公司须在12-18个月内行动，中型公司最脆弱。[EN原文]",
        "tc": "穆迪報告指零售產險分銷是最受AI近端衝擊的金融業務線，AI將壓縮信息差、客戶可自行複製比價與風險評估；具轉換成本與專精複雜風險者仍可保定價權，多數公司須在12-18個月內行動，中型公司最脆弱。"
      },
      "why": {
        "sc": "评级机构对AI冲击分销渠道的量化判断=渠道转型与获客模式的前瞻参照",
        "tc": "評級機構對AI衝擊分銷渠道的量化判斷=渠道轉型與獲客模式的前瞻參照"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 3,
        "midback": 2,
        "lead": 1,
        "cross": 1
      },
      "source": {
        "sc": "Insurance Business / Moody's",
        "tc": "Insurance Business / Moody's",
        "lang": "en"
      },
      "boards": [
        "tech"
      ],
      "themes": [
        "ai",
        "distribution"
      ],
      "tags": {
        "sc": [
          "Moody's",
          "AI",
          "分销渠道",
          "财险",
          "转型"
        ],
        "tc": [
          "Moody's",
          "AI",
          "分銷渠道",
          "財險",
          "轉型"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-08-04T10:00:00+08:00",
      "originalUrl": "https://www.insurancebusinessmag.com/asia/news/technology/moodys-retail-pandc-distribution-faces-the-fastest-ai-disruption-of-any-financial-services-segment-584750.aspx",
      "ingestedAt": "2026-08-04T18:17:37.402180+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "hk-plan-rename-aug04",
      "clusterCount": 1,
      "score": 62,
      "verifyStatus": "pending",
      "sourceTier": "media",
      "sourceKey": "qqnews:plan-rename-20260804",
      "title": {
        "sc": "港险产品集中更名：保诚20款产品8月24日启用新名 友邦中银人寿跟进",
        "tc": "港險產品集中更名：保誠20款產品8月24日啟用新名 友邦中銀人壽跟進"
      },
      "summary": {
        "sc": "按保监局与金管局2025年9月联合规定，具储蓄功能保险产品名称须包含「保险」或「Insurance」，以防消费者误认作银行存款；保诚20款在售产品将于8月24日启用新名称、9月初寄送通知函及保单批单，友邦、中银人寿同步跟进。属合规更名，保障、条款、缴费均不变，客户无需操作，市场「停售」传闻系过度解读。",
        "tc": "按保監局與金管局2025年9月聯合規定，具儲蓄功能保險產品名稱須包含「保險」或「Insurance」；保誠20款在售產品8月24日啟用新名稱，友邦、中銀人壽跟進；屬合規更名，保障條款不變，客戶無需操作，「停售」傳聞係過度解讀。"
      },
      "why": {
        "sc": "产品更名合规潮=回应客户「停售恐慌」、理解储蓄险监管命名规则的必备话术",
        "tc": "產品更名合規潮=回應客戶「停售恐慌」、理解儲蓄險監管命名規則的必備話術"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 2,
        "midback": 1,
        "lead": 1,
        "cross": 0
      },
      "source": {
        "sc": "腾讯新闻",
        "tc": "騰訊新聞",
        "lang": "zh"
      },
      "boards": [
        "reg"
      ],
      "themes": [
        "compliance",
        "product"
      ],
      "tags": {
        "sc": [
          "产品更名",
          "保监局",
          "金管局",
          "储蓄险",
          "合规"
        ],
        "tc": [
          "產品更名",
          "保監局",
          "金管局",
          "儲蓄險",
          "合規"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-08-04T08:02:00+08:00",
      "originalUrl": "http://news.qq.com/rain/a/20260804A042W600",
      "ingestedAt": "2026-08-04T18:17:37.402180+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "sg-captive-pcc-aug04",
      "clusterCount": 1,
      "score": 68,
      "verifyStatus": "pending",
      "sourceTier": "media",
      "sourceKey": "insuranceasia:sg-captive-pcc-20260804",
      "title": {
        "sc": "新加坡拟推保护型细胞公司框架 专属自保保险向中型企业开放",
        "tc": "新加坡擬推保護型細胞公司框架 專屬自保保險向中型企業開放"
      },
      "summary": {
        "sc": "新加坡拟议的保护型细胞公司（PCC）框架，允许多个专属自保计划共用同一法律实体，有望令专属自保保险对中型企业开放。新加坡正发力抢攻自保市场，与香港在亚太专属自保中心地位上的竞争进一步升温，值得关注其对香港自保业务的分流影响。[EN原文]",
        "tc": "新加坡擬議的保護型細胞公司（PCC）框架，允許多個專屬自保計劃共用同一法律實體，有望令專屬自保保險對中型企業開放；與香港在亞太自保中心地位上的競爭進一步升溫。"
      },
      "why": {
        "sc": "新加坡自保政策提速=香港专属自保中心竞争力的直接参照系",
        "tc": "新加坡自保政策提速=香港專屬自保中心競爭力的直接參照系"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 0,
        "midback": 1,
        "lead": 2,
        "cross": 2
      },
      "source": {
        "sc": "Insurance Asia",
        "tc": "Insurance Asia",
        "lang": "en"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "captive",
        "competition"
      ],
      "tags": {
        "sc": [
          "新加坡",
          "专属自保",
          "PCC",
          "保险中心"
        ],
        "tc": [
          "新加坡",
          "專屬自保",
          "PCC",
          "保險中心"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-08-04T06:00:00+08:00",
      "originalUrl": "https://insuranceasia.com/exclusive/singapore-targets-captive-insurance-growth",
      "ingestedAt": "2026-08-04T18:17:37.402180+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "msig-cyber-sme-aug04",
      "clusterCount": 1,
      "score": 65,
      "verifyStatus": "pending",
      "sourceTier": "media",
      "sourceKey": "insuranceasia:msig-cyber-sme-20260804",
      "title": {
        "sc": "MSIG为中小企业增网安保障 保单捆绑威胁监测与应急响应",
        "tc": "MSIG為中小企業增網安保障 保單捆綁威脅監測與應急響應"
      },
      "summary": {
        "sc": "三井住友保险（MSIG）面向中小企业推出网安保险升级，将威胁监测与事件响应服务直接捆绑进保单，填补中小企业在安全人力与工具上的资源缺口；中小企网安资源不足仍是此类保障渗透率提升的主要障碍，保险公司正以「保险+服务」模式切入。[EN原文]",
        "tc": "三井住友保險（MSIG）面向中小企業推出網安保險升級，將威脅監測與事件響應服務直接捆綁進保單，填補中小企在安全人力與工具上的資源缺口。"
      },
      "why": {
        "sc": "「保险+安全服务」捆绑模式=中小企网安险渗透路径的行业样本",
        "tc": "「保險+安全服務」捆綁模式=中小企網安險滲透路徑的行業樣本"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 0,
        "midback": 1,
        "lead": 1,
        "cross": 1
      },
      "source": {
        "sc": "Insurance Asia / MSIG",
        "tc": "Insurance Asia / MSIG",
        "lang": "en"
      },
      "boards": [
        "tech"
      ],
      "themes": [
        "cyber",
        "sme"
      ],
      "tags": {
        "sc": [
          "MSIG",
          "网络安全险",
          "中小企业",
          "捆绑服务"
        ],
        "tc": [
          "MSIG",
          "網絡安全險",
          "中小企業",
          "捆綁服務"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-08-04T06:00:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/news/msig-adds-cyber-cover-small-firms-face-resource-gaps",
      "ingestedAt": "2026-08-04T18:17:37.402180+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "hkma-sme-credit-aug03",
      "clusterCount": 1,
      "score": 85,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "hkma:sme-credit-20260803",
      "title": {
        "sc": "HKMA：Q2中小企业信贷状况总体稳定 78%认为审批取态相近或更易",
        "tc": "HKMA：Q2中小企業信貸狀況總體穩定 78%認為審批取態相近或更易"
      },
      "summary": {
        "sc": "金管局8月3日公布Q2中小企业信贷状况调查：撇除无意见者，78%受访企业认为银行信贷审批取态与半年前相若或更宽松（上季73%），22%认为更困难（上季27%）；新申请成功获批率85%（上季91%），4%反映现有信贷额度收紧。调查覆盖约2500家中小企业，反映企业融资环境边际变化。[EN原文]",
        "tc": "金管局Q2中小企業信貸調查：78%認為銀行審批取態相近或更寬鬆（上季73%），新申請成功獲批率85%（上季91%）；信貸環境總體穩定但邊際轉緊，覆蓋約2500家中小企業。"
      },
      "why": {
        "sc": "企业信贷环境=中小企业主客户经营与融资需求的宏观参照",
        "tc": "企業信貸環境=中小企業主客戶經營與融資需求的宏觀參照"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 0,
        "midback": 1,
        "lead": 1,
        "cross": 0
      },
      "source": {
        "sc": "HKMA",
        "tc": "HKMA",
        "lang": "en"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "credit",
        "sme"
      ],
      "tags": {
        "sc": [
          "HKMA",
          "中小企业",
          "信贷",
          "融资"
        ],
        "tc": [
          "HKMA",
          "中小企業",
          "信貸",
          "融資"
        ]
      },
      "contentKind": "stats",
      "publishedAt": "2026-08-03T16:00:00+08:00",
      "originalUrl": "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/08/20260803-4/",
      "ingestedAt": "2026-08-03T18:08:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "goldman-aia-1h26-aug03",
      "clusterCount": 1,
      "score": 72,
      "verifyStatus": "verified",
      "sourceTier": "media",
      "sourceKey": "aastocks:goldman-aia-20260803",
      "title": {
        "sc": "高盛维持友邦「买入」：料上半年NBV+15%至32.54亿美元",
        "tc": "高盛維持友邦「買入」：料上半年NBV+15%至32.54億美元"
      },
      "summary": {
        "sc": "高盛8月3日研报：预计友邦上半年新业务价值按实际汇率同比+15%至32.54亿美元，Q2增速放缓至12%（Q1为17%），主因香港高基数而非销售放缓；内地为增长最快市场（Q2按固定汇率+13%），泰国受投连险带动转正（+5%）；维持买入评级、目标价97港元，中报8月20日公布。[EN原文]",
        "tc": "高盛預計友邦上半年NBV按實際匯率+15%至32.54億美元，Q2放緩至12%（Q1為17%）主因香港高基數而非銷售放緩；內地最快（Q2+13%）、泰國轉正（+5%）；維持買入、目標價97港元，中報8月20日揭曉。"
      },
      "why": {
        "sc": "投行对友邦中报预期=港险龙头景气与高基数效应的交叉验证",
        "tc": "投行對友邦中報預期=港險龍頭景氣與高基數效應的交叉驗證"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 1,
        "midback": 1,
        "lead": 0,
        "cross": 0
      },
      "source": {
        "sc": "AASTOCKS / Goldman Sachs",
        "tc": "AASTOCKS / Goldman Sachs",
        "lang": "en"
      },
      "boards": [
        "insurer"
      ],
      "themes": [
        "results",
        "valuation"
      ],
      "tags": {
        "sc": [
          "友邦",
          "高盛",
          "新业务价值",
          "中报",
          "评级"
        ],
        "tc": [
          "友邦",
          "高盛",
          "新業務價值",
          "中報",
          "評級"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-08-03T12:47:00+08:00",
      "originalUrl": "https://wdatacn.aastocks.com/en/stocks/news/aafn-con/NOW.1536225/latest-news/AAFN",
      "ingestedAt": "2026-08-03T18:08:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "prudential-eason-brand-aug03",
      "clusterCount": 1,
      "score": 75,
      "verifyStatus": "verified",
      "sourceTier": "insurer",
      "sourceKey": "prudential:eason-brand-20260803",
      "title": {
        "sc": "保诚推全新品牌企划「诚诺，实现您心」 陈奕迅任品牌代言人",
        "tc": "保誠推全新品牌企劃「誠諾，實現您心」 陳奕迅任品牌代言人"
      },
      "summary": {
        "sc": "保诚8月3日宣布推出亚洲区品牌企划「诚诺，实现您心」，由香港歌手兼演员陈奕迅担任品牌代言人，核心信息为「每一份保单都代表一个承诺」；香港市场将通过数码平台、社交媒体、电视及户外广告全面铺开，影片7月30日已首播，8月中旬起加大投放。保诚集团全球服务逾1700万客户。",
        "tc": "保誠8月3日宣佈推出亞洲區品牌企劃「誠諾，實現您心」，由陳奕迅擔任品牌代言人，核心信息為「每一份保單都代表一個承諾」；香港市場將透過數碼平台、社交媒體、電視及戶外廣告全面鋪開，影片7月30日已首播，8月中旬起加大投放。"
      },
      "why": {
        "sc": "头部保司押注情感化品牌传播=高净值客群信任建设与渠道获客风向标",
        "tc": "頭部保司押注情感化品牌傳播=高淨值客群信任建設與渠道獲客風向標"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 1,
        "midback": 1,
        "lead": 1,
        "cross": 0
      },
      "source": {
        "sc": "保诚香港",
        "tc": "保誠香港",
        "lang": "zh"
      },
      "boards": [
        "insurer"
      ],
      "themes": [
        "brand",
        "marketing"
      ],
      "tags": {
        "sc": [
          "保诚",
          "陈奕迅",
          "品牌企划",
          "市场推广"
        ],
        "tc": [
          "保誠",
          "陳奕迅",
          "品牌企劃",
          "市場推廣"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2026-08-03T10:00:00+08:00",
      "originalUrl": "https://www.prudential.com.hk/tc/about-us/newsroom/prudential-launches-new-brand-campaign-featuring-eason-chan/",
      "ingestedAt": "2026-08-04T18:17:37.402180+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "cyber-insurer-profit-aug03",
      "clusterCount": 1,
      "score": 70,
      "verifyStatus": "verified",
      "sourceTier": "pro",
      "sourceKey": "insuranceasia:cyber-profit-20260803",
      "title": {
        "sc": "AM Best/S&P：网安险2025全球保费破160亿美元 费率下行考验盈利",
        "tc": "AM Best/S&P：網安險2025全球保費破160億美元 費率下行考驗盈利"
      },
      "summary": {
        "sc": "AM Best与S&P同月报告网安险前景：2025年全球保费逾160亿美元，需求随数字化与数据保护法规增长，但竞争令费率走低；AM Best维持稳定展望，S&P警告市场接近转折点、费率续跌将侵蚀承保利润。2025年勒索攻击同比+30%至7419起，AI令攻击更易规模化。[EN原文]",
        "tc": "AM Best與S&P研判網安險：2025全球保費破160億美元，需求增長但費率下行；AM Best展望穩定，S&P警告接近轉折點；去年勒索攻擊+30%至7419起，AI令攻擊更易規模化。"
      },
      "why": {
        "sc": "网安险定价与AI风险=企业客户风险管理话题与市场情绪参照",
        "tc": "網安險定價與AI風險=企業客戶風險管理話題與市場情緒參照"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 0,
        "midback": 1,
        "lead": 1,
        "cross": 1
      },
      "source": {
        "sc": "Insurance Asia / AM Best·S&P",
        "tc": "Insurance Asia / AM Best·S&P",
        "lang": "en"
      },
      "boards": [
        "tech"
      ],
      "themes": [
        "cyber",
        "pricing"
      ],
      "tags": {
        "sc": [
          "网络安全险",
          "AM Best",
          "S&P",
          "勒索软件",
          "AI风险"
        ],
        "tc": [
          "網絡安全險",
          "AM Best",
          "S&P",
          "勒索軟件",
          "AI風險"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-08-03T09:00:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/expert-opinion/can-cyber-insurers-stay-profitable",
      "ingestedAt": "2026-08-03T18:08:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "ia-mcv-definition-aug03",
      "clusterCount": 1,
      "score": 74,
      "verifyStatus": "pending",
      "sourceTier": "media",
      "sourceKey": "gmteight:ia-mcv-definition-20260803",
      "title": {
        "sc": "保监局拟重定义「内地访客」：非内地永久居民或可免赴港投保",
        "tc": "保監局擬重定義「內地訪客」：非內地永久居民或可免赴港投保"
      },
      "summary": {
        "sc": "据明报引述保监局执行董事梁志仁：保监局计划重新定义「内地访客」类别，拟允许非内地永久居民（如海外华侨）毋须亲身来港投保，以吸纳居港外的高净值客群；下季展开正式咨询，年内发布客户定义指引。新定义落地前，内地访客季度数据继续暂缓公布。[EN原文]",
        "tc": "據明報引述保監局執行董事：擬重定義「內地訪客」，允許非內地永久居民（如海外華僑）毋須親身赴港投保，以吸引海外高淨值客群；下季正式諮詢、年內出指引。新定義落地前內地訪客季度數據續暫緩公佈。"
      },
      "why": {
        "sc": "内地访客定义=直接改变MCV渠道规则与跨境投保流程，需重点跟进",
        "tc": "內地訪客定義=直接改變MCV渠道規則與跨境投保流程，需重點跟進"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 3,
        "midback": 2,
        "lead": 2,
        "cross": 3
      },
      "source": {
        "sc": "GMT EIGHT / 明报",
        "tc": "GMT EIGHT / 明報",
        "lang": "zh+en"
      },
      "boards": [
        "reg"
      ],
      "themes": [
        "mainland-visitors",
        "regulation"
      ],
      "tags": {
        "sc": [
          "内地访客",
          "MCV",
          "保监局",
          "跨境投保",
          "定义咨询"
        ],
        "tc": [
          "內地訪客",
          "MCV",
          "保監局",
          "跨境投保",
          "定義諮詢"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-08-03T09:00:00+08:00",
      "originalUrl": "https://gmteight.com/flash/detail/1245979",
      "ingestedAt": "2026-08-03T18:08:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "jefferies-hk-channels-aug03",
      "clusterCount": 1,
      "score": 75,
      "verifyStatus": "verified",
      "sourceTier": "pro",
      "sourceKey": "insuranceasia:jefferies-channels-20260803",
      "title": {
        "sc": "Jefferies：港险Q1新单保费+47% 保单件数仅+2% 件均保费+45%",
        "tc": "Jefferies：港險Q1新單保費+47% 保單件數僅+2% 件均保費+45%"
      },
      "summary": {
        "sc": "Jefferies拆解港险Q1监管申报数据：个人新单保费同比+47%，代理+39%、银保+59%、经纪+30%，但新保单件数仅+2%、件均保费+45%，增长主要来自高价值保单而非销售产能。经纪已成为宏利与富卫最大渠道，友邦代理新单+44%、宏利代理+102%。[EN原文]",
        "tc": "Jefferies拆解港險Q1數據：個人新單保費+47%，保單件數僅+2%、件均保費+45%，增長靠高價值保單；經紀已成宏利與富衛最大渠道，友邦代理新單+44%。"
      },
      "why": {
        "sc": "渠道格局与件均逻辑=判断高净值客群与经纪渠道趋势的一手依据",
        "tc": "渠道格局與件均邏輯=判斷高淨值客群與經紀渠道趨勢的一手依據"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 2,
        "midback": 2,
        "lead": 1,
        "cross": 1
      },
      "source": {
        "sc": "Insurance Asia / Jefferies",
        "tc": "Insurance Asia / Jefferies",
        "lang": "en"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "channel",
        "mainland-wealth"
      ],
      "tags": {
        "sc": [
          "Jefferies",
          "渠道",
          "经纪",
          "银保",
          "件均保费"
        ],
        "tc": [
          "Jefferies",
          "渠道",
          "經紀",
          "銀保",
          "件均保費"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-08-03T05:45:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/news/jefferies-warns-policy-growth-lags-hong-kong-premium-surge",
      "ingestedAt": "2026-08-03T18:08:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "aia-crossborder-care-aug03",
      "clusterCount": 1,
      "score": 72,
      "verifyStatus": "verified",
      "sourceTier": "insurer",
      "sourceKey": "insuranceasia:aia-crossborder-20260803",
      "title": {
        "sc": "AIA新加坡扩跨境医疗：马来就医免预付 34%担忧医疗开支",
        "tc": "AIA新加坡擴跨境醫療：馬來就醫免預付 34%擔憂醫療開支"
      },
      "summary": {
        "sc": "AIA新加坡8月起升级团体员工医疗保障：逾百万受保成员（约占当地劳动人口1/3）可凭LOG Plus在马国指定医院免预付治疗、牙科卡免垫付，公立医院专科免转介，并上线AIA+全数字预授权。AIA Live Better调研显示34%居民担忧医疗可负担性，反映集团跨境医疗与控费策略。[EN原文]",
        "tc": "AIA新加坡8月升級團體醫療：百萬成員可憑LOG Plus在馬國醫院免預付治療、牙科免墊付、專科免轉介，並推數字預授權；34%居民擔憂醫療開支，凸顯集團跨境醫療與控費策略。"
      },
      "why": {
        "sc": "AIA跨境医疗策略=友邦系产品与服务体系观察窗口（含内地客群关联）",
        "tc": "AIA跨境醫療策略=友邦系產品與服務體系觀察窗口（含內地客群關聯）"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 0,
        "midback": 1,
        "lead": 1,
        "cross": 2
      },
      "source": {
        "sc": "Insurance Asia / AIA",
        "tc": "Insurance Asia / AIA",
        "lang": "en"
      },
      "boards": [
        "insurer"
      ],
      "themes": [
        "medical",
        "cross-border"
      ],
      "tags": {
        "sc": [
          "AIA",
          "跨境医疗",
          "团体医疗",
          "医疗通胀"
        ],
        "tc": [
          "AIA",
          "跨境醫療",
          "團體醫療",
          "醫療通脹"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-08-03T05:15:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/news/aia-expands-cross-border-care-34-fear-medical-costs",
      "ingestedAt": "2026-08-03T18:08:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "fwd-cancer-claims-202608",
      "clusterCount": 1,
      "score": 71,
      "verifyStatus": "verified",
      "sourceTier": "media",
      "sourceKey": "insuranceasia",
      "title": {
        "sc": "富卫新增癌症重复理赔保障：港癌患者 5 年存活率达 61%",
        "tc": "富衛新增癌症重複理賠保障：港癌患者 5 年存活率達 61%"
      },
      "summary": {
        "sc": "富卫香港新增癌症重复理赔保障条款，回应香港癌症患者五年存活率升至 61% 的趋势。意味着客户在一次癌症理赔后，若癌症复发或转移，可再次获得赔付——长期保障的实用性大幅提升。",
        "tc": "富衛香港新增癌症重複理賠保障條款，回應香港癌症患者五年存活率升至 61% 的趨勢。"
      },
      "why": {
        "sc": "癌症存活率上升=客户带病生存时间变长=单次理赔不够用了。FWD 这一步说明危疾产品的竞争已经从「保额大小」升级到「保障次数」。",
        "tc": "癌症存活率上升=客戶帶病生存時間變長=單次理賠不夠用了。危疾產品的競爭已經從「保額大小」升級到「保障次數」。"
      },
      "actions": {
        "front": {
          "sc": "癌症多重理赔=危疾产品的新卖点",
          "tc": "癌症多重理賠=危疾產品的新賣點"
        },
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 4,
        "midback": 1,
        "lead": 1,
        "cross": 1
      },
      "source": {
        "sc": "InsuranceAsia · 2026年8月",
        "lang": "zh"
      },
      "boards": [
        "product"
      ],
      "themes": [
        "product",
        "uw"
      ],
      "tags": {
        "sc": [
          "富卫",
          "癌症",
          "危疾",
          "理赔"
        ],
        "tc": [
          "富衛",
          "癌症",
          "危疾",
          "理賠"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-08-02T10:00:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/news/fwd-adds-repeat-claims-cancer-survival-reaches-61"
    },
    {
      "id": "mainland-insurers-tsimshatsui-202608",
      "clusterCount": 1,
      "score": 72,
      "verifyStatus": "verified",
      "sourceTier": "media",
      "sourceKey": "insuranceasia",
      "title": {
        "sc": "内地保险及财富管理公司入驻带动尖沙咀写字楼空置率降至 6.7％",
        "tc": "內地保險及財富管理公司入駐帶動尖沙咀寫字樓空置率降至 6.7％"
      },
      "summary": {
        "sc": "据 InsuranceAsia 报道，内地保险和财富管理公司加速在香港设立办公室，推动尖沙咀写字楼空置率降至 6.7%。北京道一号 6 月录得 2024 年以来首次满租。这一趋势反映了内地金融机构对香港作为国际财富管理中心地位的持续押注。",
        "tc": "據 InsuranceAsia 報道，內地保險和財富管理公司加速在香港設立辦公室，推動尖沙咀寫字樓空置率降至 6.7%。北京道一號 6 月錄得 2024 年以來首次滿租。"
      },
      "why": {
        "sc": "空置率降=内地钱和人正在进来。这不是保险新闻，但这是比保险新闻更真实的信号——机构用真金白银租办公室，说明对香港市场有长期信心。",
        "tc": "空置率降=內地錢和人正在進來。機構用真金白銀租辦公室，說明對香港市場有長期信心。"
      },
      "actions": {
        "front": {
          "sc": "内地机构涌入=跨境客户的供给端正在扩大",
          "tc": "內地機構湧入=跨境客戶的供給端正在擴大"
        },
        "midback": {},
        "lead": {
          "sc": "机构用脚投票=香港作为财富管理中心的地位在强化",
          "tc": "機構用腳投票=香港作為財富管理中心的地位在強化"
        },
        "cross": {
          "sc": "内地金融资源+香港国际平台=跨境生态的底层支撑",
          "tc": "內地金融資源+香港國際平台=跨境生態的底層支撐"
        }
      },
      "rolesImpact": {
        "front": 3,
        "midback": 1,
        "lead": 4,
        "cross": 4
      },
      "source": {
        "sc": "InsuranceAsia · 2026年8月",
        "lang": "zh"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "offshore",
        "market"
      ],
      "tags": {
        "sc": [
          "尖沙咀",
          "空置率",
          "内地机构"
        ],
        "tc": [
          "尖沙咀",
          "空置率",
          "內地機構"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-08-01T10:00:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/news/mainland-insurers-drive-tsimshatsui-vacancy-down-67"
    },
    {
      "id": "msig-claims-ratio-202608",
      "clusterCount": 1,
      "score": 74,
      "verifyStatus": "verified",
      "sourceTier": "media",
      "sourceKey": "insuranceasia",
      "title": {
        "sc": "MSIG 香港理赔率升至 94.7%：2025 年赔付 3.59 亿港元",
        "tc": "MSIG 香港理賠率升至 94.7%：2025 年賠付 3.59 億港元"
      },
      "summary": {
        "sc": "三井住友保险（MSIG）香港公布 2025 年理赔数据：理赔结算率升至 94.7%，全年在港澳市场赔付 3.59 亿港元。高理赔率=客户实际拿到理赔款的概率=保险公司兑现承诺的能力。",
        "tc": "三井住友保險（MSIG）香港公佈 2025 年理賠數據：理賠結算率升至 94.7%，全年在港澳市場賠付 3.59 億港元。"
      },
      "why": {
        "sc": "理赔率是检验保险公司「说到做到」的终极指标。94.7% 意味着绝大多数理赔申请都得到了赔付。在日常客户沟通中，理赔率数据比分红实现率更直观、更有说服力。",
        "tc": "理賠率是檢驗保險公司「說到做到」的終極指標。94.7% 意味著絕大多數理賠申請都得到了賠付。"
      },
      "actions": {
        "front": {
          "sc": "理赔率94.7%=客户可感知的保险公司诚信度",
          "tc": "理賠率94.7%=客戶可感知的保險公司誠信度"
        },
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 4,
        "midback": 1,
        "lead": 1,
        "cross": 1
      },
      "source": {
        "sc": "InsuranceAsia · 2026年8月",
        "lang": "zh"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "uw",
        "firm"
      ],
      "tags": {
        "sc": [
          "MSIG",
          "理赔率",
          "一般保险"
        ],
        "tc": [
          "MSIG",
          "理賠率",
          "一般保險"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-08-01T10:00:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/news/msig-lifts-claims-settlement-ratio-947"
    },
    {
      "id": "fstb-captive-blog-202608",
      "clusterCount": 1,
      "score": 78,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "govhk",
      "title": {
        "sc": "财库局：香港专属自保公司增至 9 间，风险管理市场持续扩容",
        "tc": "財庫局：香港專屬自保公司增至 9 間，風險管理市場持續擴容"
      },
      "summary": {
        "sc": "财经事务及库务局局长博客指出：香港专属自保保险公司已增至 9 间（其中 2 间为 2026 年新增），反映市场对香港作为国际风险管理中心的信心持续增强。专属自保公司是大企业自设的「内部保险公司」，是香港再保险生态的重要组成部分。",
        "tc": "財經事務及庫務局局長博客指出：香港專屬自保保險公司已增至 9 間（其中 2 間為 2026 年新增），反映市場對香港作為國際風險管理中心的信心持續增強。"
      },
      "why": {
        "sc": "专属自保公司数量=大型企业把香港当作风控基地的信号。每多一家，香港的再保险和专业服务链条就厚一层。",
        "tc": "專屬自保公司數量=大型企業把香港當作風控基地的信號。每多一家，香港的再保險和專業服務鏈條就厚一層。"
      },
      "actions": {
        "front": {},
        "midback": {
          "sc": "专属自保需专业保险服务支持=知识密集型业务的增长点",
          "tc": "專屬自保需專業保險服務支持=知識密集型業務的增長點"
        },
        "lead": {
          "sc": "9间专属自保=香港风险管理中心的实证",
          "tc": "9間專屬自保=香港風險管理中心的實證"
        },
        "cross": {
          "sc": ""
        }
      },
      "rolesImpact": {
        "front": 1,
        "midback": 3,
        "lead": 3,
        "cross": 2
      },
      "source": {
        "sc": "财库局 · 2026年8月",
        "lang": "zh"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "reg",
        "firm"
      ],
      "tags": {
        "sc": [
          "专属自保",
          "财库局",
          "风险管理"
        ],
        "tc": [
          "專屬自保",
          "財庫局",
          "風險管理"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2026-08-01T10:00:00+08:00",
      "originalUrl": "https://www.fstb.gov.hk/tc/blog/blog180825.htm"
    },
    {
      "id": "jll-tsim-vacancy-aug01",
      "clusterCount": 1,
      "score": 68,
      "verifyStatus": "verified",
      "sourceTier": "media",
      "sourceKey": "insuranceasia:jll-tsim-20260801",
      "title": {
        "sc": "内地保司租务推动尖沙咀甲级写字楼空置率降至6.7%",
        "tc": "內地保司租務推動尖沙咀甲級寫字樓空置率降至6.7%"
      },
      "summary": {
        "sc": "仲量联行（JLL）最新报告显示，内地保险及财富管理公司在港扩张租赁需求强劲，推动尖沙咀甲级写字楼空置率6月底降至6.7%，较上月降0.4个百分点，较2022年9月11.2%的峰值大幅回落。One Peking 6月首次实现100%入驻。全港写字楼空置率降至13.1%，RGA再保险租下太古坊全层2.35万平方呎。[EN原文]",
        "tc": "JLL報告：內地保司及財管公司租務推動尖沙咀空置率降至6.7%，One Peking全數入駐，反映行業擴張實體需求。"
      },
      "why": {
        "sc": "内地资金+保司实体扩张落地香港=行业景气与人才流向的交叉验证",
        "tc": "內地資金+保司實體擴張落地香港=行業景氣與人才流向的交叉驗證"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 1,
        "cross": 1
      },
      "source": {
        "sc": "Insurance Asia / JLL",
        "tc": "Insurance Asia / JLL",
        "lang": "en"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "property",
        "mainland-wealth"
      ],
      "tags": {
        "sc": [
          "尖沙咀",
          "写字楼",
          "JLL",
          "内地保司",
          "租赁"
        ],
        "tc": [
          "尖沙咀",
          "寫字樓",
          "JLL",
          "內地保司",
          "租賃"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-08-01T05:00:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/news/mainland-insurers-drive-tsimshatsui-vacancy-down-67",
      "ingestedAt": "2026-08-02T23:30:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "hkma-monetary-stats-jun26",
      "clusterCount": 1,
      "score": 85,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "hkma:monetary-stats-202606",
      "title": {
        "sc": "HKMA公布6月货币统计：港元货币供应与贷款趋势",
        "tc": "HKMA公佈6月貨幣統計：港元貨幣供應與貸款趨勢"
      },
      "summary": {
        "sc": "香港金管局7月31日公布2026年6月货币统计数据，涵盖港元及外币货币供应量、认可机构存款与贷款变化。货币统计反映整体流动性环境，是评估保费融资成本、银行信贷取向及港元利率走势的重要宏观参照。[EN原文]",
        "tc": "金管局公佈6月貨幣統計，涵蓋貨幣供應、存款與貸款變化，為評估保費融資環境與利率走勢的宏觀參照。"
      },
      "why": {
        "sc": "货币与信贷环境=保费融资成本与储蓄险销售节奏的宏观底色",
        "tc": "貨幣與信貸環境=保費融資成本與儲蓄險銷售節奏的宏觀底色"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 0,
        "midback": 1,
        "lead": 0,
        "cross": 0
      },
      "source": {
        "sc": "HKMA",
        "tc": "HKMA",
        "lang": "en"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "monetary",
        "liquidity"
      ],
      "tags": {
        "sc": [
          "HKMA",
          "货币统计",
          "货币供应",
          "贷款"
        ],
        "tc": [
          "HKMA",
          "貨幣統計",
          "貨幣供應",
          "貸款"
        ]
      },
      "contentKind": "stats",
      "publishedAt": "2026-07-31T16:00:00+08:00",
      "originalUrl": "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/07/20260731-7/",
      "ingestedAt": "2026-08-02T23:30:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "rga-hk-outlook-2026",
      "clusterCount": 1,
      "score": 80,
      "verifyStatus": "verified",
      "sourceTier": "pro",
      "sourceKey": "rga",
      "title": {
        "sc": "RGA：2026年港险市场展望——跨境需求+监管转型+数字创新三重驱动",
        "tc": "RGA：2026年港險市場展望——跨境需求+監管轉型+數字創新三重驅動"
      },
      "summary": {
        "sc": "RGA 香港及新加坡市场负责人 Maurizio Busti 在 Asia Insurance Review 撰文指出：尽管经济增速温和，港险市场在 2026 年仍具强劲增长动能。三大驱动力：① 内地跨境需求持续（2024年占新造 30%）；② HKRBC 全实施推动资本优化与透明度；③ AI 核保与数字工具降本增效。高净值客户与大众市场须差异化策略。",
        "tc": "RGA 香港及新加坡市場負責人 Maurizio Busti 在 Asia Insurance Review 撰文指出：儘管經濟增速溫和，港險市場在 2026 年仍具強勁增長動能。三大驅動力：① 內地跨境需求持續（2024年佔新造 30%）；② HKRBC 全實施推動資本優化與透明度；③ AI 核保與數字工具降本增效。高淨值客戶與大眾市場須差異化策略。"
      },
      "why": {
        "sc": "RGA 是全球最大再保险公司之一，其对港险市场的展望可作为 IFA 团队判断「这条赛道还跑多远」的基准线。三个增长引擎（跨境/RBC/AI）与看板数据完全对齐。",
        "tc": "RGA 是全球最大再保險公司之一，其對港險市場的展望可作為 IFA 團隊判斷「這條賽道還跑多遠」的基準線。三個增長引擎（跨境/RBC/AI）與看板數據完全對齊。"
      },
      "actions": {
        "front": {
          "sc": "跨境需求30%占比=MCV客户仍是核心增长引擎",
          "tc": "跨境需求30%佔比=MCV客戶仍是核心增長引擎"
        },
        "midback": {
          "sc": "HKRBC透明化=合规成本上升但也是差异化机会",
          "tc": "HKRBC透明化=合規成本上升但也是差異化機會"
        },
        "lead": {
          "sc": "RGA结论：赛道仍宽，关键在策略分化",
          "tc": "RGA結論：賽道仍寬，關鍵在策略分化"
        },
        "cross": {
          "sc": "再保险视角确认：香港作为区域保险枢纽的地位稳固",
          "tc": "再保險視角確認：香港作為區域保險樞紐的地位穩固"
        }
      },
      "rolesImpact": {
        "front": 4,
        "midback": 3,
        "lead": 4,
        "cross": 4
      },
      "source": {
        "sc": "RGA / Asia Insurance Review",
        "lang": "zh"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "market",
        "offshore",
        "tech"
      ],
      "tags": {
        "sc": [
          "RGA",
          "市场展望",
          "2026"
        ],
        "tc": [
          "RGA",
          "市場展望",
          "2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-31T10:00:00+08:00",
      "originalUrl": "https://www.rgare.com/knowledge-center/article/hong-kong-insurance-market--navigating-opportunities-and-challenges-in-2026"
    },
    {
      "id": "nfra-governance-20260731",
      "clusterCount": 1,
      "score": 85,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "nfra",
      "title": {
        "sc": "金融监管总局等四部门联合发布金融机构治理实施意见",
        "tc": "金融監管總局等四部門聯合發布金融機構治理實施意見"
      },
      "summary": {
        "sc": "2026 年 7 月 31 日，国家金融监督管理总局、中国人民银行、中国证监会、财政部联合发布《关于健全金融机构治理的实施意见》，覆盖银行、保险、证券全行业。对保险业的影响：公司治理不合规将直接触发监管干预——与香港 RBC 框架下的管治要求形成对照。",
        "tc": "2026 年 7 月 31 日，國家金融監督管理總局、中國人民銀行、中國證監會、財政部聯合發布《關於健全金融機構治理的實施意見》，覆蓋銀行、保險、證券全行業。對保險業的影響：公司治理不合規將直接觸發監管干預——與香港 RBC 框架下的管治要求形成對照。"
      },
      "why": {
        "sc": "四部门联手=金融监管的高级别协同。对 IFA 的启示：内地保险公司的治理水平将决定其在严格监管下的生存空间。香港版「报行合一」的精神与此一脉相承。",
        "tc": "四部門聯手=金融監管的高級別協同。對 IFA 的啟示：內地保險公司的治理水平將決定其在嚴格監管下的生存空間。香港版「報行合一」的精神與此一脈相承。"
      },
      "actions": {
        "front": {},
        "midback": {
          "sc": "内地金融机构治理要求→香港RBC管治支柱→跨境合规的一致性趋势",
          "tc": "內地金融機構治理要求→香港RBC管治支柱→跨境合規的一致性趨勢"
        },
        "lead": {},
        "cross": {
          "sc": "两地监管逻辑趋同：从「管产品」走向「管公司」",
          "tc": "兩地監管邏輯趨同：從「管產品」走向「管公司」"
        }
      },
      "rolesImpact": {
        "front": 1,
        "midback": 4,
        "lead": 3,
        "cross": 4
      },
      "source": {
        "sc": "国家金融监管总局 · 2026年7月31日",
        "lang": "sc"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "reg",
        "compliance",
        "firm"
      ],
      "tags": {
        "sc": [
          "金融监管总局",
          "公司治理",
          "四部门"
        ],
        "tc": [
          "金融監管總局",
          "公司治理",
          "四部門"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2026-07-31T10:00:00+08:00",
      "originalUrl": "https://www.nfra.gov.cn/cn/view/pages/ItemDetail.html?docId=1266349&itemId=928"
    },
    {
      "id": "overseas-invest-reg-20260731",
      "clusterCount": 1,
      "score": 78,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "state-council",
      "title": {
        "sc": "个人境外投资新规7月1日施行：内地居民赴港投保正式纳入统一监管框架。",
        "tc": "個人境外投資新規7月1日施行：內地居民赴港投保正式納入統一監管框架。"
      },
      "summary": {
        "sc": "《国务院关于对外投资的规定》（国务院令第837号）2026年7月1日正式施行，首次将居民个人纳入境外投资法定监管，明确港澳地区投资参照执行。合规渠道限定为港股通、QDII、跨境理财通三条。新规对港险市场的影响：保费资金来源和跨境划转路径成为监管核查重点，合规配置取代灰色通道成为唯一出路。",
        "tc": "《國務院關於對外投資的規定》（國務院令第837號）2026年7月1日正式施行，首次將居民個人納入境外投資法定監管，明確港澳地區投資參照執行。合規渠道限定為港股通、QDII、跨境理財通三條。新規對港險市場影響深遠。"
      },
      "why": {
        "sc": "这是内地首部系统性规范境外投资的行政法规——直接改变内地居民赴港投保的资金出境逻辑。灰色通道被封堵，合规大额保单的渠道价值反而凸显。",
        "tc": "這是內地首部系統性規範境外投資的行政法規——直接改變內地居民赴港投保的資金出境邏輯。灰色通道被封堵，合規大額保單的渠道價值反而凸顯。"
      },
      "actions": {
        "front": {
          "sc": "向客户说明：赴港投保需走合规资金通道，不可拆分5万美元额度缴纳保费。",
          "tc": "向客戶說明：赴港投保需走合規資金通道，不可拆分5萬美元額度繳納保費。"
        },
        "midback": {
          "sc": "更新合规流程：大额保单需核查客户资金来源和跨境划转路径。",
          "tc": "更新合規流程：大額保單需核查客戶資金來源和跨境劃轉路徑。"
        },
        "lead": {
          "sc": "新规短期内可能影响中小额港险销售，但长期利好合规能力强的大型经纪渠道。",
          "tc": "新規短期內可能影響中小額港險銷售，但長期利好合規能力強的大型經紀渠道。"
        },
        "cross": {
          "sc": "跨境理财通是合规出境通道之一，关注南向通额度提升至8,000亿后的配置机会。",
          "tc": "跨境理財通是合規出境通道之一，關注南向通額度提升至8,000億後的配置機會。"
        }
      },
      "rolesImpact": {
        "front": 4,
        "midback": 3,
        "lead": 3,
        "cross": 3
      },
      "source": {
        "sc": "国务院令第837号 / 新浪财经分析",
        "lang": "zh"
      },
      "boards": [
        "family",
        "reg"
      ],
      "themes": [
        "cross-border",
        "compliance"
      ],
      "tags": {
        "sc": [
          "境外投资",
          "837号令",
          "合规",
          "港险",
          "资金出境"
        ],
        "tc": [
          "境外投資",
          "837號令",
          "合規",
          "港險",
          "資金出境"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-31T09:36:00+08:00",
      "originalUrl": "https://www.gov.cn/zhengce/content/202607/content_837.htm"
    },
    {
      "id": "mof-rmb-bonds-cmu-jul30",
      "clusterCount": 1,
      "score": 86,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "hkma",
      "title": {
        "sc": "财政部在CMU发行人民币国债 巩固香港离岸人民币枢纽",
        "tc": "財政部在CMU發行人民幣國債 鞏固香港離岸人民幣樞紐"
      },
      "summary": {
        "sc": "2026年7月30日，中国财政部通过香港金管局债务工具中央结算系统（CMU）发行人民币国债，进一步巩固香港作为离岸人民币业务枢纽地位。此举有助于丰富香港人民币产品生态，为保险业提供更多优质人民币资产配置选择。[EN原文]",
        "tc": "財政部經CMU發行人民幣國債，鞏固香港離岸人民幣樞紐，豐富人民幣資產配置。"
      },
      "why": {
        "sc": "人民币国债扩容=香港保险业人民币资产配置选项增加",
        "tc": "人民幣國債擴容=保險業人民幣資產選項增加"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "source": {
        "sc": "HKMA",
        "tc": "HKMA",
        "lang": "zh+en"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "bond",
        "rmb"
      ],
      "tags": {
        "sc": [
          "HKMA",
          "人民币国债",
          "CMU",
          "离岸人民币"
        ],
        "tc": [
          "HKMA",
          "人民幣國債",
          "CMU",
          "離岸人民幣"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2026-07-30T15:00:00+08:00",
      "originalUrl": "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/07/20260730-3/",
      "ingestedAt": "2026-07-30T18:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "hkma-fed-response-jul30",
      "clusterCount": 1,
      "score": 88,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "hkma",
      "title": {
        "sc": "HKMA回应美联储利率决议：维持联系汇率稳定",
        "tc": "HKMA回應美聯儲利率決議：維持聯繫匯率穩定"
      },
      "summary": {
        "sc": "2026年7月30日，香港金管局就美联储利率决策作出回应，重申香港联系汇率制度稳健运行，银行体系流动性充裕。金管局表示将继续密切监察市场变化，确保货币市场有序运作。[EN原文]",
        "tc": "金管局就聯儲局利率決策作回應，重申聯繫匯率制度穩健，銀行體系流動性充裕。"
      },
      "why": {
        "sc": "美联储利率路径直接影响港元利率与保险产品定价",
        "tc": "美聯儲利率直接影響港元利率與保險定價"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "source": {
        "sc": "HKMA",
        "tc": "HKMA",
        "lang": "en"
      },
      "boards": [
        "reg"
      ],
      "themes": [
        "market",
        "monetary"
      ],
      "tags": {
        "sc": [
          "HKMA",
          "美联储",
          "利率",
          "联系汇率"
        ],
        "tc": [
          "HKMA",
          "美聯儲",
          "利率",
          "聯繫匯率"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2026-07-30T14:30:00+08:00",
      "originalUrl": "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/07/20260730-4/",
      "ingestedAt": "2026-07-30T18:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "nfra-midyear-20260730",
      "clusterCount": 1,
      "score": 88,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "nfra",
      "title": {
        "sc": "金融监管总局 2026 年中工作会议：持续推进「报行合一」和预定利率调整",
        "tc": "金融監管總局 2026 年中工作會議：持續推進「報行合一」和預定利率調整"
      },
      "summary": {
        "sc": "2026 年 7 月 30 日金融监管总局召开年中工作会议，明确持续推保险业「报行合一」全渠道覆盖和预定利率市场化调整。核心表述：① 传统险预定利率上限 2.5%→研究值 2.34%（持续下行）；② 万能险最低保证利率上限 1.5%；③ 建立预定利率与市场利率挂钩的动态调整机制。",
        "tc": "2026 年 7 月 30 日金融監管總局召開年中工作會議，明確持續推保險業「報行合一」全渠道覆蓋和預定利率市場化調整。核心表述：① 傳統險預定利率上限 2.5%→研究值 2.34%（持續下行）；② 萬能險最低保證利率上限 1.5%；③ 建立預定利率與市場利率掛鉤的動態調整機制。"
      },
      "why": {
        "sc": "这是内地保险业最核心的制度变革。「报行合一」=内地的「佣金三件套」，预定利率调整=内地的「演示利率上限」。理解内地怎么改，就知道香港 IFA 的跨境竞争优势窗口还有多长。",
        "tc": "這是內地保險業最核心的制度變革。「報行合一」=內地的「佣金三件套」，預定利率調整=內地的「演示利率上限」。理解內地怎麼改，就知道香港 IFA 的跨境競爭優勢窗口還有多長。"
      },
      "actions": {
        "front": {
          "sc": "内地保证收益下降→港险相对吸引力提升",
          "tc": "內地保證收益下降→港險相對吸引力提升"
        },
        "midback": {
          "sc": "报行合一=两地佣金改革逻辑一致",
          "tc": "報行合一=兩地佣金改革邏輯一致"
        },
        "lead": {
          "sc": "预定利率持续下行=港险跨境窗口期仍在加长",
          "tc": "預定利率持續下行=港險跨境窗口期仍在加長"
        },
        "cross": {
          "sc": "两地监管趋同→IFA只需一套逻辑即可服务两个市场",
          "tc": "兩地監管趨同→IFA只需一套邏輯即可服務兩個市場"
        }
      },
      "rolesImpact": {
        "front": 5,
        "midback": 4,
        "lead": 5,
        "cross": 5
      },
      "source": {
        "sc": "国家金融监管总局 · 2026年7月30日",
        "lang": "sc"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "reg",
        "compliance",
        "product",
        "offshore"
      ],
      "tags": {
        "sc": [
          "报行合一",
          "预定利率",
          "金融监管总局"
        ],
        "tc": [
          "報行合一",
          "預定利率",
          "金融監管總局"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2026-07-30T10:00:00+08:00",
      "originalUrl": "https://www.nfra.gov.cn/cn/view/pages/ItemDetail.html?docId=1265870&itemId=915"
    },
    {
      "id": "ia-commission-caps-jul30",
      "clusterCount": 1,
      "score": 78,
      "verifyStatus": "verified",
      "sourceTier": "pro",
      "sourceKey": "insuranceasia:creditsights-commission-20260730",
      "title": {
        "sc": "CreditSights：香港寿险新规重塑竞争格局 渠道强者受益",
        "tc": "CreditSights：香港壽險新規重塑競爭格局 渠道強者受益"
      },
      "summary": {
        "sc": "CreditSights报告指出，香港寿险市场在2024-2025年持续强劲增长，内地访客需求2025年显著回暖。报告分析多项监管新规对市场的影响：分红保单演示利率设限、首年佣金设限及转介费设限等措施，将利好拥有成熟代理及银保网络、产品久期较长、分销质量较高的保险公司。同时风险为本资本制度促使保司增配优质固收资产，基建类投资获资本优惠。[EN原文]",
        "tc": "CreditSights報告分析香港壽險新規：演示利率及佣金設限，利好渠道強、久期長、分銷質素高的保司；RBC促增配優質固收。"
      },
      "why": {
        "sc": "新规下的赢家逻辑=IFA选择合作保司与产品的重要参考",
        "tc": "新規下的贏家邏輯=IFA選擇合作保司與產品的重要參考"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 2,
        "midback": 1,
        "lead": 0,
        "cross": 0
      },
      "source": {
        "sc": "Insurance Asia / CreditSights",
        "tc": "Insurance Asia / CreditSights",
        "lang": "en"
      },
      "boards": [
        "reg"
      ],
      "themes": [
        "commission",
        "regulation"
      ],
      "tags": {
        "sc": [
          "佣金上限",
          "演示利率",
          "CreditSights",
          "RBC",
          "竞争格局"
        ],
        "tc": [
          "佣金上限",
          "演示利率",
          "CreditSights",
          "RBC",
          "競爭格局"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-30T06:30:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/news/hong-kong-caps-commissions-life-insurers-compete",
      "ingestedAt": "2026-08-02T23:30:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "msig-claims-947-jul30",
      "clusterCount": 1,
      "score": 75,
      "verifyStatus": "verified",
      "sourceTier": "insurer",
      "sourceKey": "msig:claims-2025-20260730",
      "title": {
        "sc": "MSIG香港2025年理赔结案率升至94.7% 连续五年改善",
        "tc": "MSIG香港2025年理賠結案率升至94.7% 連續五年改善"
      },
      "summary": {
        "sc": "MSIG保险（香港）2025年理赔报告显示，全年结案率升至94.7%，较2020年的91.1%连续第五年提升；2025年在香港及澳门共赔付3.59亿港元。雇员补偿保险结案率最高达99.87%，家佣保险97.57%，旅游保险96.27%。客户表扬按年增11%，2025年所有Google评价均为五星。[EN原文]",
        "tc": "MSIG香港2025理賠結案率94.7%連續五年改善，港澳共賠$3.59億；僱傭補償結案率99.87%最高。"
      },
      "why": {
        "sc": "理赔结案率=客户转介绍与续保的说服力素材",
        "tc": "理賠結案率=客戶轉介紹與續保的說服力素材"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 1,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "source": {
        "sc": "Insurance Asia / MSIG",
        "tc": "Insurance Asia / MSIG",
        "lang": "en"
      },
      "boards": [
        "insurer"
      ],
      "themes": [
        "claims",
        "customer"
      ],
      "tags": {
        "sc": [
          "MSIG",
          "理赔",
          "结案率",
          "客户服务"
        ],
        "tc": [
          "MSIG",
          "理賠",
          "結案率",
          "客戶服務"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-30T06:15:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/news/msig-lifts-claims-settlement-ratio-947",
      "ingestedAt": "2026-08-02T23:30:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "hkma-cmu-network-jul29",
      "clusterCount": 1,
      "score": 85,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "hkma",
      "title": {
        "sc": "HKMA欢迎CMU扩展国际网络及服务范围",
        "tc": "HKMA歡迎CMU擴展國際網絡及服務範圍"
      },
      "summary": {
        "sc": "2026年7月29日，香港金管局欢迎债务工具中央结算系统（CMU）扩展国际网络与服务，新增与多个国际中央证券存管机构的连接。此举将提升香港债券市场基础设施的国际化水平，便利跨境债券投资与结算。[EN原文]",
        "tc": "CMU擴展國際網絡，新增多個ICSD連接，提升香港債券基建國際化水平。"
      },
      "why": {
        "sc": "CMU国际化=保险公司跨境债券投资更便利",
        "tc": "CMU國際化=保險公司跨境債券投資更便利"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "source": {
        "sc": "HKMA",
        "tc": "HKMA",
        "lang": "en"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "infrastructure",
        "bond"
      ],
      "tags": {
        "sc": [
          "HKMA",
          "CMU",
          "债券市场",
          "金融基建"
        ],
        "tc": [
          "HKMA",
          "CMU",
          "債券市場",
          "金融基建"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2026-07-29T16:00:00+08:00",
      "originalUrl": "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/07/20260729-3/",
      "ingestedAt": "2026-07-30T18:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "bowtie-202607-100m",
      "clusterCount": 1,
      "score": 77,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-30T01:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "香港首家虚拟保险公司Bowtie营收突破1亿美元 剑指东南亚",
        "tc": "香港首家虛擬保險公司Bowtie營收突破1億美元 劍指東南亞"
      },
      "summary": {
        "sc": "InsuranceAsia News 2026年7月报道：香港首家虚拟保险公司Bowtie实现营收突破1亿美元里程碑,客户留存率达93%。联合创始人Fred Ngan表示公司有望较快实现盈亏平衡,并计划进军马来西亚等东南亚市场。[EN原文]",
        "tc": "Bowtie營收破$1億,客戶留存93%,進軍東南亞"
      },
      "why": {
        "sc": "虚拟保险的规模化验证=数字保险的商业模式正式跑通",
        "tc": "虛擬保險規模化驗證=商業模式正式跑通"
      },
      "actions": {
        "front": {
          "sc": "了解Bowtie产品线与传统保司的差异",
          "tc": "了解Bowtie與傳統差異"
        },
        "midback": {
          "sc": "关注虚拟保险对传统渠道的冲击",
          "tc": "關注虛擬保險衝擊"
        },
        "lead": {
          "sc": "数字保险=行业未来方向",
          "tc": "數字保險=行業方向"
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "InsuranceAsia News",
        "tc": "InsuranceAsia News",
        "lang": "en"
      },
      "boards": [
        "tech",
        "firm"
      ],
      "tags": {
        "sc": [
          "Bowtie",
          "虚拟保险",
          "InsurTech",
          "东南亚"
        ],
        "tc": [
          "Bowtie",
          "虛擬保險",
          "InsurTech",
          "東南亞"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-29T16:00:00+08:00",
      "originalUrl": "https://insuranceasianews.com/hong-kongs-first-virtual-insurer-eyes-malaysia-led-southeast-asia-push-after-hitting-critical-us100m-revenue-milestone/",
      "sourceKey": "bowtie:100m-202607",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ],
      "sourceTier": "media"
    },
    {
      "id": "hk-202607-mainland-scrutiny",
      "clusterCount": 1,
      "score": 83,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-30T01:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "监管关注香港保险公司内地资金合规问题",
        "tc": "監管關注香港保險公司內地資金合規問題"
      },
      "summary": {
        "sc": "Insurance Asia 2026年7月报道：监管机构对香港保险公司涉及内地资金流动的商业模式提出关切，担忧部分业务模式可能助长非合规资本外流。保险公司面临更严的资金来源审查。[EN原文]",
        "tc": "監管關注港險涉內地資金合規問題"
      },
      "why": {
        "sc": "跨境资金合规审查趋严=大额保单的资金来源将成为重点",
        "tc": "跨境資金審查趨嚴=大額保單資金來源重點"
      },
      "actions": {
        "front": {
          "sc": "大额保单须确保客户资金来源合规",
          "tc": "大額保單確保資金來源合規"
        },
        "midback": {
          "sc": "更新反洗钱和资金来源审查流程",
          "tc": "更新反洗錢審查流程"
        },
        "lead": {
          "sc": "资金来源合规=团队不可触碰的红线",
          "tc": "資金來源合規=紅線"
        },
        "cross": {
          "sc": "跨境资金合规=内地客户投保的前提条件",
          "tc": "跨境資金合規=前提條件"
        }
      },
      "source": {
        "sc": "Insurance Asia",
        "tc": "Insurance Asia",
        "lang": "en"
      },
      "boards": [
        "compliance",
        "cross"
      ],
      "tags": {
        "sc": [
          "跨境资金",
          "合规",
          "反洗钱",
          "2026"
        ],
        "tc": [
          "跨境資金",
          "合規",
          "反洗錢",
          "2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-29T14:00:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/news/hong-kong-insurers-risk-scrutiny-over-mainland-funds",
      "sourceKey": "insuranceasia",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ],
      "sourceTier": "pro"
    },
    {
      "id": "ia-20260730-sales-misconduct",
      "clusterCount": 1,
      "score": 88,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": false,
      "ingestedAt": "2026-07-30T01:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "保监局收紧销售行为规则：高管对全流程合规直接负责",
        "tc": "保監局收緊銷售行為規則：高管對全流程合規直接負責"
      },
      "summary": {
        "sc": "Insurance Asia 2026年7月报道：保监局进一步收紧保险销售行为监管。新规要求高级管理层对销售全流程的合规性承担直接责任。随着不当销售行为审查持续升温，机构须强化内部管控机制。[EN原文]",
        "tc": "保監局收緊銷售規則,高管直接負責全流程合規"
      },
      "why": {
        "sc": "高管个人问责=合规压力从操作层上升到决策层",
        "tc": "高管個人問責=合規壓力上升"
      },
      "actions": {
        "front": {
          "sc": "确保销售流程每个环节有据可查",
          "tc": "確保銷售流程有據可查"
        },
        "midback": {
          "sc": "更新销售合规手册",
          "tc": "更新銷售合規手冊"
        },
        "lead": {
          "sc": "高管个人问责=团队合规不容有失",
          "tc": "團隊合規不容有失"
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "Insurance Asia",
        "tc": "Insurance Asia",
        "lang": "en"
      },
      "boards": [
        "regulatory",
        "compliance"
      ],
      "tags": {
        "sc": [
          "销售行为",
          "高管",
          "问责",
          "2026"
        ],
        "tc": [
          "銷售行為",
          "高管",
          "問責",
          "2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-29T10:00:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/news/hong-kong-ia-tightens-sales-rules-misconduct-scrutiny-grows",
      "sourceKey": "insuranceasia",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ],
      "sourceTier": "pro"
    },
    {
      "id": "cyber-mapping-circular-jul29",
      "clusterCount": 1,
      "score": 85,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "hkma-sfc-ia-mpfa",
      "title": {
        "sc": "金管局证监保监积金局联合发布跨行业网络安全测绘通函",
        "tc": "金管局證監保監積金局聯合發布跨行業網絡安全測繪通函"
      },
      "summary": {
        "sc": "2026年7月29日，金管局、证监会、保监局及积金局联合发布跨行业网络安全测绘通函，要求所有认可机构、持牌法团、授权保险公司及强积金核准受托人参与。此举旨在系统性评估全金融行业网络安全态势，为后续网络韧性监管提供数据基础。[EN原文]",
        "tc": "四大監管機構聯合發布跨行業網絡安全測繪通函，要求所有認可機構及授權保險公司參與，系統評估全行業網絡安全態勢。[EN原文]"
      },
      "why": {
        "sc": "跨行业网络安全测绘=保险业网络安全监管从机构自律走向行业协同",
        "tc": "跨行業網絡安全測繪=保險業網絡安全監管從機構自律走向行業協同"
      },
      "actions": {
        "front": {},
        "midback": {
          "sc": "IT安全团队需配合网络安全测绘自查与数据提交",
          "tc": "IT安全團隊需配合網絡安全測繪自查與數據提交"
        },
        "lead": {
          "sc": "网络安全合规投入在保险科技预算中的优先级应提高",
          "tc": "網絡安全合規投入在保險科技預算中的優先級應提高"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 0,
        "midback": 4,
        "lead": 3,
        "cross": 0
      },
      "source": {
        "sc": "证监会联合通函",
        "lang": "zh+en"
      },
      "boards": [
        "reg",
        "tech"
      ],
      "themes": [
        "cybersecurity",
        "IA",
        "HKMA"
      ],
      "tags": {
        "sc": [
          "网络安全",
          "联合通函",
          "保监局",
          "金管局",
          "证监会"
        ],
        "tc": [
          "網絡安全",
          "聯合通函",
          "保監局",
          "金管局",
          "證監會"
        ]
      },
      "contentKind": "circular",
      "publishedAt": "2026-07-29T09:04:00+08:00",
      "originalUrl": "https://apps.sfc.hk/edistributionWeb/gateway/EN/circular/intermediaries/supervision/doc?refNo=26EC45",
      "ingestedAt": "2026-08-01T12:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "ai-25pct-insurance-jobs-202607",
      "clusterCount": 1,
      "score": 68,
      "verifyStatus": "verified",
      "sourceTier": "pro",
      "sourceKey": "insuranceasia",
      "title": {
        "sc": "报告：AI 自动化可能替代保险业 25% 的岗位",
        "tc": "報告：AI 自動化可能替代保險業 25% 的崗位"
      },
      "summary": {
        "sc": "Insurance Asia 援引行业报告：AI 自动化可能在保险业替代高达 25% 的岗位，涵盖核保、理赔处理和客服等职能。同时 AI 将创造新的技术岗位，净效应取决于企业的转型速度。",
        "tc": "Insurance Asia 援引行業報告：AI 自動化可能在保險業替代高達 25% 的崗位，涵蓋核保、理賠處理和客服等職能。同時 AI 將創造新的技術崗位，淨效應取決於企業的轉型速度。"
      },
      "why": {
        "sc": "25% 的岗位替代率不是一个技术问题，是团队管理问题——谁先帮团队成员完成从「执行者」到「AI 协作者」的技能迁移，谁就在下一轮竞争中占先机。",
        "tc": "25% 的崗位替代率不是一個技術問題，是團隊管理問題——誰先幫團隊成員完成從「執行者」到「AI 協作者」的技能遷移，誰就在下一輪競爭中佔先機。"
      },
      "actions": {
        "front": {
          "sc": "AI 不会替代IFA，但会用 AI 的 IFA 会替代不会用的",
          "tc": "AI 不會替代IFA，但會用 AI 的 IFA 會替代不會用的"
        },
        "midback": {
          "sc": "核保理赔自动化是降本增效最快的切入点",
          "tc": "核保理賠自動化是降本增效最快的切入點"
        },
        "lead": {
          "sc": "25% 替代率意味着团队培训预算需要重新分配",
          "tc": "25% 替代率意味著團隊培訓預算需要重新分配"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 3,
        "midback": 4,
        "lead": 4,
        "cross": 0
      },
      "source": {
        "sc": "InsuranceAsia",
        "lang": "zh"
      },
      "boards": [
        "tech"
      ],
      "themes": [
        "tech",
        "career"
      ],
      "tags": {
        "sc": [
          "AI",
          "自动化",
          "岗位"
        ],
        "tc": [
          "AI",
          "自動化",
          "崗位"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-29T00:02:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/news/ai-automation-could-replace-25-insurance-jobs"
    },
    {
      "id": "picc-202607-re",
      "clusterCount": 1,
      "score": 74,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-30T01:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "人保香港积极拓展再保险转入业务",
        "tc": "人保香港積極拓展再保險轉入業務"
      },
      "summary": {
        "sc": "Insurance Asia 2026年7月报道：人保香港(PICC HK)积极拓展再保险转入(inward reinsurance)业务，尽管核心承保利润仍然偏薄，投资收益支撑整体盈利增长。[EN原文]",
        "tc": "人保香港拓展再保轉入業務"
      },
      "why": {
        "sc": "中资保司在再保市场的扩张=香港作为再保险中心的地位强化",
        "tc": "中資保司再保擴張=香港再保中心強化"
      },
      "actions": {
        "front": {
          "sc": "知识储备",
          "tc": "知識儲備"
        },
        "midback": {
          "sc": "关注中资再保市场动态",
          "tc": "關注中資再保動態"
        },
        "lead": {
          "sc": ""
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "Insurance Asia",
        "tc": "Insurance Asia",
        "lang": "en"
      },
      "boards": [
        "firm"
      ],
      "tags": {
        "sc": [
          "人保",
          "再保险",
          "中资",
          "2026"
        ],
        "tc": [
          "人保",
          "再保險",
          "中資",
          "2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-28T12:00:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/news/picc-hk-chases-inward-reinsurance-growth",
      "sourceKey": "insuranceasia",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ],
      "sourceTier": "pro"
    },
    {
      "id": "ia-ai-cohort-new-insurers-jul",
      "clusterCount": 1,
      "score": 80,
      "verifyStatus": "verified",
      "sourceTier": "pro",
      "sourceKey": "insurancebusinessmag",
      "title": {
        "sc": "保监局AI Cohort新增三家保险公司 中银人寿、国寿海外等加入",
        "tc": "保監局AI Cohort新增三家保險公司 中銀人壽、國壽海外等加入"
      },
      "summary": {
        "sc": "Insurance Business报道：香港保监局AI Cohort Programme迎来第三批成员，新增中银集团人寿、中国人寿（海外）及另一家保险公司。该计划旨在推动保险业人工智能应用，此前已在Cyberport举办AI Cohort Symposium 2026。[EN原文]",
        "tc": "保監局AI Cohort新增中銀人壽、國壽海外等三家，推動保險AI應用。"
      },
      "why": {
        "sc": "AI监管沙盒扩容=保险科技合规创新加速",
        "tc": "AI監管沙盒擴容=保險科技合規創新加速"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 0,
        "midback": 1,
        "lead": 0,
        "cross": 0
      },
      "source": {
        "sc": "Insurance Business",
        "tc": "Insurance Business",
        "lang": "en"
      },
      "boards": [
        "tech"
      ],
      "themes": [
        "ai",
        "insurtech"
      ],
      "tags": {
        "sc": [
          "IA",
          "AI Cohort",
          "中银人寿",
          "国寿海外",
          "InsurTech"
        ],
        "tc": [
          "IA",
          "AI Cohort",
          "中銀人壽",
          "國壽海外",
          "InsurTech"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-28T10:00:00+08:00",
      "originalUrl": "https://www.insurancebusinessmag.com/asia/news/technology/insurance-authority-adds-three-insurers-to-ai-cohort-programme-579133.aspx",
      "ingestedAt": "2026-07-30T18:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "cgs-202607-hk-crackdown",
      "clusterCount": 1,
      "score": 82,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-30T01:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "CGS International: 香港保险公司不惧监管收紧 增长前景稳健",
        "tc": "CGS International: 香港保險公司不懼監管收緊 增長前景穩健"
      },
      "summary": {
        "sc": "CGS International 2026年7月报告指出，尽管内地对跨境资金流动的审查持续收紧，香港保险公司凭借多元化客源和强劲的本地需求，增长前景依然稳健。市场对监管打压的担忧可能过度。[EN原文]",
        "tc": "CGS:港險不懼監管收緊,增長前景穩健"
      },
      "why": {
        "sc": "投行第三方视角=对市场过度担忧的理性修正",
        "tc": "投行視角=市場擔憂修正"
      },
      "actions": {
        "front": {
          "sc": "向客户说明监管收紧≠行业萎缩",
          "tc": "向客戶說明監管≠萎縮"
        },
        "midback": {
          "sc": "归档投行行业观点",
          "tc": "歸檔投行觀點"
        },
        "lead": {
          "sc": "多元化客源=抗风险能力的核心",
          "tc": "多元化客源=抗風險核心"
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "CGS International",
        "tc": "CGS International",
        "lang": "en"
      },
      "boards": [
        "macro",
        "cross"
      ],
      "tags": {
        "sc": [
          "CGS",
          "监管",
          "跨境",
          "前景",
          "2026"
        ],
        "tc": [
          "CGS",
          "監管",
          "跨境",
          "前景",
          "2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-28T10:00:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/news/hong-kong-insurers-shrug-off-crackdown-fears-cgs-international",
      "sourceKey": "insuranceasia",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ],
      "sourceTier": "pro"
    },
    {
      "id": "ratings-2026-consolidated",
      "clusterCount": 1,
      "score": 95,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": true,
      "ingestedAt": "2026-07-28T22:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "香港主要保险公司信评一览(2026更新)。",
        "tc": "香港主要保險公司信評一覽(2026更新)。"
      },
      "summary": {
        "sc": "2026年最新信评汇总:S&P-宏利AA-/友邦AA/保诚AA/永明AA(3月上调)/汇丰AA-/太保A+/太平A/Chubb A+。Moody's-友邦Aa2/保诚A2。Fitch-友邦AA/保诚AA-/太平A。评级上调最显著:永明(3月AA-->AA)。评级下调:太平(4月A+-->A)。[EN原文]",
        "tc": "2026信评:S&P永明上调至AA,太平下调至A"
      },
      "why": {
        "sc": "客户问哪家最安全?信评是最客观的第三方答案。",
        "tc": "客戶問哪家最安全?"
      },
      "actions": {
        "front": {
          "sc": "客户品牌对比时的核心参考工具",
          "tc": "客戶品牌對比核心參考"
        },
        "midback": {
          "sc": "归档保司信评数据",
          "tc": "歸檔信評數據"
        },
        "lead": {
          "sc": "信评变化=合作保司优先级调整信号",
          "tc": "信評變化=優先級調整"
        },
        "cross": {
          "sc": "跨境客户特别关注国际评级",
          "tc": "跨境客戶關注國際評級"
        }
      },
      "source": {
        "sc": "S&P/Moody's/Fitch",
        "tc": "S&P/Moody's/Fitch",
        "lang": "en"
      },
      "boards": [
        "firm"
      ],
      "tags": {
        "sc": [
          "信评",
          "S&P",
          "Moody's",
          "Fitch",
          "2026"
        ],
        "tc": [
          "信評",
          "S&P",
          "Moody's",
          "Fitch",
          "2026"
        ]
      },
      "contentKind": "report",
      "publishedAt": "2026-07-28T10:00:00+08:00",
      "originalUrl": "https://www.spglobal.com/ratings/en/regulatory/article/asia-pacific-insurance-ratings-list-s101683009",
      "sourceKey": "spglobal",
      "sourceTier": "research",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "continuum-hk-gm-202607",
      "clusterCount": 1,
      "score": 68,
      "verifyStatus": "verified",
      "sourceTier": "pro",
      "sourceKey": "InsuranceAsia",
      "title": {
        "sc": "Continuum 挖角 Howden：Andy Tam 出任香港总经理",
        "tc": "Continuum 挖角 Howden：Andy Tam 出任香港總經理"
      },
      "summary": {
        "sc": "Continuum（香港虚拟保险经纪）从 Howden 挖来 Andy Tam 担任香港总经理，7 月起生效。此前 Marsh 获法院临时禁制令阻止前高管跳槽至 Howden。",
        "tc": "Continuum（香港虛擬保險經紀）從 Howden 挖來 Andy Tam 擔任香港總經理，7 月起生效。此前 Marsh 獲法院臨時禁制令阻止前高管跳槽至 Howden。"
      },
      "why": {
        "sc": "经纪赛道人才战白热化——Marsh 发禁制令，Howden 换帅，Continuum 挖角，三条线索串起一个——香港经纪渠道正在快速洗牌。",
        "tc": "經紀賽道人才戰白熱化——Marsh 發禁制令，Howden 換帥，Continuum 挖角，三條線索串起一個信號：香港經紀渠道正在快速洗牌。"
      },
      "actions": {
        "front": {
          "sc": "经纪渠道生态变化影响合作与线索获取",
          "tc": "經紀渠道生態變化影響合作與線索獲取"
        },
        "midback": {
          "sc": "关注经纪市场合规与禁制令判例",
          "tc": "關注經紀市場合規與禁制令判例"
        },
        "lead": {
          "sc": "虚拟保险经纪崛起，传统经纪防线松动",
          "tc": "虛擬保險經紀崛起，傳統經紀防線鬆動"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 2,
        "midback": 3,
        "lead": 3,
        "cross": 0
      },
      "source": {
        "sc": "InsuranceAsia News",
        "lang": "zh"
      },
      "boards": [
        "insurer"
      ],
      "themes": [
        "channel",
        "firm"
      ],
      "tags": {
        "sc": [
          "经纪",
          "虚拟保险"
        ],
        "tc": [
          "經紀",
          "虛擬保險"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-28T00:15:00+08:00",
      "originalUrl": "https://insuranceasianews.com/continuum-hires-howdens-andy-tam-as-hong-kong-general-manager/"
    },
    {
      "id": "hk-fraud-payments-lag-202607",
      "clusterCount": 1,
      "score": 78,
      "verifyStatus": "verified",
      "sourceTier": "pro",
      "sourceKey": "insuranceasia",
      "title": {
        "sc": "欺诈成本占营收 5%：香港保险公司支付系统滞后",
        "tc": "欺詐成本佔營收 5%：香港保險公司支付系統滯後"
      },
      "summary": {
        "sc": "InsuranceAsia 专访 Celent 与 Adyen 高管：74% 的香港保险公司估欺诈成本高达年收入的 5%，55% 称过时的支付系统限制了反欺诈能力。96% 仍在使用支票处理部分支付，过半手动处理。",
        "tc": "InsuranceAsia 專訪 Celent 與 Adyen 高管：74% 的香港保險公司估欺詐成本高達年收入的 5%，55% 稱過時的支付系統限制了反欺詐能力。96% 仍在使用支票處理部分支付，過半手動處理。"
      },
      "why": {
        "sc": "支付基础设施是 IFA 作业链条里最被忽视的一环——支票+手动处理不仅耗人力，还把 5% 营收送给了欺诈。与内地实时支付体验的对比，也是客户体验的分水岭。",
        "tc": "支付基礎設施是 IFA 作業鏈條裏最被忽視的一環——支票+手動處理不僅耗人力，還把 5% 營收送給了欺詐。與內地實時支付體驗的對比，也是客戶體驗的分水嶺。"
      },
      "actions": {
        "front": {
          "sc": "客户对理赔和退款体验的预期已对标电商，影响续保",
          "tc": "客戶對理賠和退款體驗的預期已對標電商，影響續保"
        },
        "midback": {
          "sc": "支付系统改造是合规与效率的双命题",
          "tc": "支付系統改造是合規與效率的雙命題"
        },
        "lead": {
          "sc": "GenZ 客户期望保险公司提供与网约车同级的移动体验",
          "tc": "GenZ 客戶期望保險公司提供與網約車同級的移動體驗"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 3,
        "midback": 4,
        "lead": 3,
        "cross": 0
      },
      "source": {
        "sc": "InsuranceAsia",
        "lang": "zh"
      },
      "boards": [
        "tech",
        "insurer"
      ],
      "themes": [
        "tech",
        "firm"
      ],
      "tags": {
        "sc": [
          "数字转型",
          "欺诈"
        ],
        "tc": [
          "數字轉型",
          "欺詐"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-28T00:10:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/exclusive/fraud-costs-expose-hong-kong-insurers-payments-lag"
    },
    {
      "id": "howden-hk-ceo-20260701",
      "clusterCount": 1,
      "score": 75,
      "verifyStatus": "verified",
      "sourceTier": "pro",
      "sourceKey": "insuranceasia",
      "title": {
        "sc": "Howden 香港换帅：Alaric Lee 接任 CEO",
        "tc": "Howden 香港換帥：Alaric Lee 接任 CEO"
      },
      "summary": {
        "sc": "Howden 宣布香港领导层过渡，Alaric Lee 于 2026 年 7 月 1 日起接替 Alfred Sham 出任香港 CEO。Sham 将赴新加坡担任亚洲首席战略官。Lee 此前为亚洲首席商务官，在港逾十年。",
        "tc": "Howden 宣佈香港領導層過渡，Alaric Lee 於 2026 年 7 月 1 日起接替 Alfred Sham 出任香港 CEO。Sham 將赴新加坡擔任亞洲首席戰略官。Lee 此前為亞洲首席商務官，在港逾十年。"
      },
      "why": {
        "sc": "香港经纪市场头部玩家换帅，Howden 在 Marsh 禁制令争议中坚持扩张，香港仍是亚洲战略重心。",
        "tc": "香港經紀市場頭部玩家換帥，信號意義明確——Howden 在 Marsh 禁制令爭議中堅持擴張，香港仍是亞洲戰略重心。"
      },
      "actions": {
        "front": {
          "sc": "高端经纪渠道竞争加剧，关注客户转介流向",
          "tc": "高端經紀渠道競爭加劇，關注客戶轉介流向"
        },
        "midback": {
          "sc": "经纪市场人事变动提示行业整合信号",
          "tc": "經紀市場人事變動提示行業整合信號"
        },
        "lead": {
          "sc": "亚洲经纪赛道人才争夺加速，香港为枢纽",
          "tc": "亞洲經紀賽道人才爭奪加速，香港為樞紐"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 3,
        "midback": 2,
        "lead": 3,
        "cross": 1
      },
      "source": {
        "sc": "InsuranceAsia",
        "lang": "zh"
      },
      "boards": [
        "insurer"
      ],
      "themes": [
        "channel",
        "firm"
      ],
      "tags": {
        "sc": [
          "经纪",
          "人事"
        ],
        "tc": [
          "經紀",
          "人事"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-28T00:05:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/news/howden-hong-kong-unveils-new-ceo"
    },
    {
      "id": "hkma-quantum-whitepaper-jul27",
      "clusterCount": 1,
      "score": 85,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "hkma",
      "title": {
        "sc": "HKMA发布量子准备白皮书及指数 推动银行业量子时代转型",
        "tc": "HKMA發布量子準備白皮書及指數 推動銀行業量子時代轉型"
      },
      "summary": {
        "sc": "2026年7月27日，香港金管局发布量子准备白皮书及配套指数，支持银行业为量子计算时代做好准备。白皮书涵盖加密算法迁移、量子风险管理框架等核心议题，保险业可参照其方法论评估自身量子风险敞口。[EN原文]",
        "tc": "金管局發布量子準備白皮書，涵蓋加密遷移與量子風險管理，保險業可參考評估。"
      },
      "why": {
        "sc": "量子计算威胁现有加密体系=保险业数据安全需前瞻布局",
        "tc": "量子計算威脅加密體系=保險業數據安全需前瞻佈局"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "source": {
        "sc": "HKMA",
        "tc": "HKMA",
        "lang": "en"
      },
      "boards": [
        "tech"
      ],
      "themes": [
        "quantum",
        "cyber"
      ],
      "tags": {
        "sc": [
          "HKMA",
          "量子计算",
          "白皮书",
          "网络安全"
        ],
        "tc": [
          "HKMA",
          "量子計算",
          "白皮書",
          "網絡安全"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2026-07-27T16:30:00+08:00",
      "originalUrl": "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/07/20260727-3/",
      "ingestedAt": "2026-07-30T18:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "cies-2year-20260727",
      "clusterCount": 1,
      "score": 82,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "investhk-cies",
      "title": {
        "sc": "新资本投资者入境计划两周年：3,166宗申请、预计引资950亿港元。",
        "tc": "新資本投資者入境計劃兩週年：3,166宗申請、預計引資950億港元。"
      },
      "summary": {
        "sc": "截至2026年2月28日，香港新CIES累计接获3,166宗申请，1,762宗已获批，实际落地投资556.36亿港元，全量预计引资约950亿港元。第二年申请量2,248宗同比增长145%。配置结构：证监会认可基金及股票占约三分之二。至2026年4月总申请量已突破3,300宗，预计总投资额上调至约990亿港元。内地申请人占比超95%。",
        "tc": "截至2026年2月28日，香港新CIES累計接獲3,166宗申請，1,762宗已獲批，實際落地投資556.36億港元，全量預計引資約950億港元。第二年申請量2,248宗同比增長145%。至2026年4月總申請量已突破3,300宗，預計總投資額上調至約990億港元。"
      },
      "why": {
        "sc": "CIES是高净值客户获取香港身份的核心通道——近千亿资金流入直接拉动保险、基金、信托等财富管理需求。第二年申请量翻倍增长说明市场信心持续增强。",
        "tc": "CIES是高淨值客戶獲取香港身份的核心通道——近千億資金流入直接拉動保險、基金、信託等財富管理需求。第二年申請量翻倍增長說明市場信心持續增強。"
      },
      "actions": {
        "front": {
          "sc": "CIES客户需配置3,000万港元合规投资——保险相连证券、投连险等均为合规品种。",
          "tc": "CIES客戶需配置3,000萬港元合規投資——保險相連證券、投連險等均為合規品種。"
        },
        "midback": {},
        "lead": {
          "sc": "近千亿资金流入意味着高净值客户池持续扩大，提前布局CIES客户转化策略。",
          "tc": "近千億資金流入意味著高淨值客戶池持續擴大，提前佈局CIES客戶轉化策略。"
        },
        "cross": {
          "sc": "CIES+家办组合是超高净值家庭的黄金路径：先拿身份、再设家办、配保险信托。",
          "tc": "CIES+家辦組合是超高淨值家庭的黃金路徑：先拿身份、再設家辦、配保險信託。"
        }
      },
      "rolesImpact": {
        "front": 3,
        "midback": 1,
        "lead": 3,
        "cross": 4
      },
      "source": {
        "sc": "香港投资推广署 / 入境事务处",
        "lang": "zh"
      },
      "boards": [
        "family"
      ],
      "themes": [
        "cies",
        "wealth-migration"
      ],
      "tags": {
        "sc": [
          "CIES",
          "投资移民",
          "资本入境",
          "高净值"
        ],
        "tc": [
          "CIES",
          "投資移民",
          "資本入境",
          "高淨值"
        ]
      },
      "contentKind": "stats",
      "publishedAt": "2026-07-27T10:44:00+08:00",
      "originalUrl": "https://www.investhk.gov.hk/en/capital-investment-entrant-scheme.html"
    },
    {
      "id": "prudential-usd500k-legacy-202607",
      "clusterCount": 1,
      "score": 76,
      "verifyStatus": "verified",
      "sourceTier": "insurer",
      "sourceKey": "prudential",
      "title": {
        "sc": "保诚推出 50 万美元级遗产传承产品，瞄准超高净值客群",
        "tc": "保誠推出 50 萬美元級遺產傳承產品，瞄準超高淨值客群"
      },
      "summary": {
        "sc": "Prudential 推出面向高净值客户的遗产传承保险产品，最低保费 50 万美元，投保人可拆分保费投资于 S&P 500 等指数。产品定位财富传承而非纯粹保障。",
        "tc": "Prudential 推出面向高淨值客戶的遺產傳承保險產品，最低保費 50 萬美元，投保人可拆分保費投資於 S&P 500 等指數。產品定位財富傳承而非純粹保障。"
      },
      "why": {
        "sc": "50 万美元起投的遗产保单，是把 IUL/VUL 包装成家族传承工具。保诚此举是在家办赛道上与永明 FWD 正面竞争，——高净值保险产品正向「投资+传承」双引擎进化。",
        "tc": "50 萬美元起投的遺產保單，本質是把 IUL/VUL 包裝成家族傳承工具。保誠此舉是在家辦賽道上與永明 FWD 正面競爭，信號：高淨值保險產品正向「投資+傳承」雙引擎進化。"
      },
      "actions": {
        "front": {
          "sc": "高净值客户产品矩阵再添一件，可与家办信托联动",
          "tc": "高淨值客戶產品矩陣再添一件，可與家辦信託聯動"
        },
        "midback": {
          "sc": "关注 S&P 500 挂钩产品的合规披露要求",
          "tc": "關注 S&P 500 掛鉤產品的合規披露要求"
        },
        "lead": {
          "sc": "高净值赛道竞争白热化，团队需更新产品手册",
          "tc": "高淨值賽道競爭白熱化，團隊需更新產品手冊"
        },
        "cross": {
          "sc": "遗产传承规划是跨境家办的核心需求场景",
          "tc": "遺產傳承規劃是跨境家辦的核心需求場景"
        }
      },
      "rolesImpact": {
        "front": 4,
        "midback": 2,
        "lead": 3,
        "cross": 4
      },
      "source": {
        "sc": "Prudential plc / InsuranceAsia",
        "lang": "zh"
      },
      "boards": [
        "product",
        "family"
      ],
      "themes": [
        "product",
        "offshore",
        "family-office"
      ],
      "tags": {
        "sc": [
          "高净值",
          "遗产传承",
          "产品"
        ],
        "tc": [
          "高淨值",
          "遺產傳承",
          "產品"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-27T10:00:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/news/prudential-targets-wealthy-clients-500000-legacy-cover"
    },
    {
      "id": "apac-insurers-emergedebt-202607",
      "clusterCount": 1,
      "score": 71,
      "verifyStatus": "verified",
      "sourceTier": "pro",
      "sourceKey": "insuranceasia",
      "title": {
        "sc": "亚太保险公司转向新兴市场债券寻求收益",
        "tc": "亞太保險公司轉向新興市場債券尋求收益"
      },
      "summary": {
        "sc": "InsuranceAsia 报道：亚太保险公司在低息环境下加大新兴市场债券配置，投资级发行现已占市场一半以上。这一趋势直接影响保险公司的投资组合收益率和分红保单的长期回报预期。",
        "tc": "InsuranceAsia 報道：亞太保險公司在低息環境下加大新興市場債券配置，投資級發行現已佔市場一半以上。這一趨勢直接影響保險公司的投資組合收益率和分紅保單的長期回報預期。"
      },
      "why": {
        "sc": "保司资产端的配置变化直接传导到负债端的分红实现率。新兴市场债券占比上升，也是分红收益来源更分散，也是需要对客户解释的风险因子更多。",
        "tc": "保司資產端的配置變化直接傳導到負債端的分紅實現率。新興市場債券佔比上升，也是分紅收益來源更分散，也是需要對客戶解釋的風險因子更多。"
      },
      "actions": {
        "front": {
          "sc": "客户问「分红稳不稳」时，可用资产端配置趋势回应",
          "tc": "客戶問「分紅穩不穩」時，可用資產端配置趨勢回應"
        },
        "midback": {
          "sc": "关注保司投资组合变化对分红实现率的影响",
          "tc": "關注保司投資組合變化對分紅實現率的影響"
        },
        "lead": {
          "sc": "利率下行周期，保司收益率承压，影响产品销售话术",
          "tc": "利率下行週期，保司收益率承壓，影響產品銷售話術"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 3,
        "midback": 3,
        "lead": 2,
        "cross": 0
      },
      "source": {
        "sc": "InsuranceAsia",
        "lang": "zh"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "macro",
        "par"
      ],
      "tags": {
        "sc": [
          "资产配置",
          "新兴市场",
          "分红"
        ],
        "tc": [
          "資產配置",
          "新興市場",
          "分紅"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-27T08:00:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/exclusive/asia-pacific-insurers-turn-emerging-market-debt-yield"
    },
    {
      "id": "sunlife-privatewealth-202607",
      "clusterCount": 1,
      "score": 74,
      "verifyStatus": "verified",
      "sourceTier": "pro",
      "sourceKey": "insuranceasia",
      "title": {
        "sc": "永明推出私人财富平台，切入高净值综合服务",
        "tc": "永明推出私人財富平台，切入高淨值綜合服務"
      },
      "summary": {
        "sc": "永明（Sun Life）近期推出私人财富平台，整合保险、投资与财富规划服务，面向亚洲高净值及超高净值客户。该平台将保险产品嵌入更广泛的财富管理架构。",
        "tc": "永明（Sun Life）近期推出私人財富平台，整合保險、投資與財富規劃服務，面向亞洲高淨值及超高淨值客戶。該平台將保險產品嵌入更廣泛的財富管理架構。"
      },
      "why": {
        "sc": "永明+保诚双双加码高净值平台化服务——这不是单个产品发布，是商业模式从「卖保单」向「管资产负债表」换挡的行业信号。",
        "tc": "永明+保誠雙雙加碼高淨值平台化服務——這不是單個產品發佈，是商業模式從「賣保單」向「管資產負債表」換擋的行業信號。"
      },
      "actions": {
        "front": {
          "sc": "高净值客户不再只买一份保单，需要综合服务方案",
          "tc": "高淨值客戶不再只買一份保單，需要綜合服務方案"
        },
        "midback": {
          "sc": "私人财富平台的合规框架比单一产品复杂",
          "tc": "私人財富平台的合規框架比單一產品複雜"
        },
        "lead": {
          "sc": "永明此举进一步强化高净值赛道竞争",
          "tc": "永明此舉進一步強化高淨值賽道競爭"
        },
        "cross": {
          "sc": "综合财富平台天然适配跨境家办场景",
          "tc": "綜合財富平台天然適配跨境家辦場景"
        }
      },
      "rolesImpact": {
        "front": 4,
        "midback": 2,
        "lead": 3,
        "cross": 3
      },
      "source": {
        "sc": "Sun Life / InsuranceAsia",
        "lang": "zh"
      },
      "boards": [
        "product",
        "family"
      ],
      "themes": [
        "product",
        "family-office",
        "offshore"
      ],
      "tags": {
        "sc": [
          "高净值",
          "私人财富",
          "平台"
        ],
        "tc": [
          "高淨值",
          "私人財富",
          "平台"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-26T14:00:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/news/sun-life-launches-private-wealth-platform"
    },
    {
      "id": "manulife-asian-care-survey-2026",
      "clusterCount": 1,
      "score": 75,
      "verifyStatus": "verified",
      "sourceTier": "insurer",
      "sourceKey": "manulife",
      "title": {
        "sc": "宏利2026亚洲关怀调查：84%港人重视晚年独立自主",
        "tc": "宏利2026亞洲關懷調查：84%港人重視晚年獨立自主"
      },
      "summary": {
        "sc": "宏利2026年亚洲关怀调查显示，84%香港受访者将独立自主（不依赖他人的能力）视为重要人生目标。调查结果反映港人对退休规划、长期护理保障的需求持续升温，为保险公司年金及长期护理产品开发提供市场洞察。"
      },
      "why": {
        "sc": "老龄化+独立自主诉求=年金/长期护理产品需求确定性",
        "tc": "老齡化+獨立自主=年金/長期護理產品需求確定"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 1,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "source": {
        "sc": "Manulife 宏利",
        "tc": "Manulife 宏利",
        "lang": "zh"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "retirement",
        "consumer"
      ],
      "tags": {
        "sc": [
          "宏利",
          "亚洲关怀调查",
          "退休规划",
          "独立自主"
        ],
        "tc": [
          "宏利",
          "亞洲關懷調查",
          "退休規劃",
          "獨立自主"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-26T10:00:00+08:00",
      "originalUrl": "https://www.manulife.com.hk/en/individual/promotions/asia-care-survey-2026.html",
      "ingestedAt": "2026-07-30T18:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "clusterCount": 1,
      "score": 70,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-26T23:59:00+08:00",
      "contentRole": {
        "sc": "本站导读（非原文）",
        "tc": "本站導讀（非原文）"
      },
      "id": "aif-2026-save-the-date",
      "title": {
        "sc": "日程：Asian Insurance Forum 2026（11 月 13 日 · 保监局主办语境）。",
        "tc": "日程：Asian Insurance Forum 2026（11 月 13 日 · 保監局主辦語境）。"
      },
      "summary": {
        "sc": "公开活动信息显示 Asian Insurance Forum 2026 定于 2026-11-13 在香港举行（场地信息见公开活动页）。适合作为行业网络与监管叙事窗口，提前放入团队日历。",
        "tc": "公開活動信息顯示 Asian Insurance Forum 2026 定於 2026-11-13 在香港舉行（場地信息見公開活動頁）。適合作為行業網絡與監管敘事窗口，提前放入團隊日曆。"
      },
      "why": {
        "sc": "管理与跨境角色可提前规划参会与客户活动排期。",
        "tc": "管理與跨境角色可提前規劃參會與客戶活動排期。"
      },
      "actions": {
        "front": {
          "sc": "如有客户活动撞期，提前改档。",
          "tc": "如有客戶活動撞期，提前改檔。"
        },
        "midback": {
          "sc": "收集往届议题，准备内部复盘提纲。",
          "tc": "收集往屆議題，準備內部復盤提綱。"
        },
        "lead": {
          "sc": "评估是否组团参会/赞助曝光。",
          "tc": "評估是否組團參會/贊助曝光。"
        },
        "cross": {
          "sc": "可作为家办/跨境客户的高端触点。",
          "tc": "可作為家辦/跨境客戶的高端觸點。"
        }
      },
      "source": {
        "sc": "公开活动信息 · MEHK/IA",
        "tc": "公開活動信息 · MEHK/IA"
      },
      "sourceTier": "pro",
      "tags": {
        "sc": [
          "行业活动",
          "AIF"
        ],
        "tc": [
          "行業活動",
          "AIF"
        ]
      },
      "themes": [
        "firm",
        "career"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 2,
        "lead": 3,
        "cross": 2
      },
      "publishedAt": "2026-07-26T09:00:00+08:00",
      "effectiveAt": "2026-11-13",
      "originalUrl": "https://www.mehongkong.com/eng/home/planning/events/detail/2026-11-13-85862-Asian-Insurance-Forum-2026.html",
      "sourceKey": "event:aif-2026",
      "boards": [
        "market"
      ],
      "contentKind": "event"
    },
    {
      "id": "hk-premiums-q1-2026-jul25",
      "clusterCount": 1,
      "score": 82,
      "verifyStatus": "verified",
      "sourceTier": "pro",
      "sourceKey": "insurancebusinessmag",
      "title": {
        "sc": "香港保险Q1总保费2916亿港元同比增32.3% 分红业务领涨",
        "tc": "香港保險Q1總保費2916億港元同比增32.3% 分紅業務領漲"
      },
      "summary": {
        "sc": "Insurance Business 2026年7月25日报道：保监局公布2026年Q1临时统计，总保费2916亿港元同比增32.3%。非相连个人业务贡献1353亿（+50.2%），其中分红业务达1257亿（+53.7%）。但内地访客数据连续第五季暂停披露，跨境数据缺口扩大。[EN原文]",
        "tc": "Q1總保費$2916億同比+32.3%，分紅業務$1257億+53.7%；內地訪客數據連續五季未披露。"
      },
      "why": {
        "sc": "Q1数据=全年市场趋势风向标，分红业务增速惊人",
        "tc": "Q1數據=全年趨勢風向標，分紅業務增速驚人"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "source": {
        "sc": "Insurance Business",
        "tc": "Insurance Business",
        "lang": "en"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "statistics",
        "growth"
      ],
      "tags": {
        "sc": [
          "Q1",
          "保费",
          "分红",
          "统计数据",
          "内地访客"
        ],
        "tc": [
          "Q1",
          "保費",
          "分紅",
          "統計數據",
          "內地訪客"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-25T14:00:00+08:00",
      "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/hong-kong-insurance-market-extends-growth-run-as-data-gap-widens-583673.aspx",
      "ingestedAt": "2026-07-30T18:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "insbus-202607-hk-growth",
      "clusterCount": 1,
      "score": 81,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T20:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "Insurance Business深度分析：Q1毛保费2916亿+32% 跨境数据连5季缺失。",
        "tc": "Insurance Business深度分析：Q1毛保費2916億+32% 跨境數據連5季缺失。"
      },
      "summary": {
        "sc": "Insurance Business 2026年7月25日深度分析：Q1毛保费2916亿同比+32.3%，新造保费1411亿。但内地访客数据自2025年Q1起已连五个季度未披露。分红新造1411亿已占2025全年43%，呈加速态势。[EN原文]",
        "tc": "Q1保費+32.3%，內地訪客數據連5季未披露"
      },
      "why": {
        "sc": "跨境数据黑箱，也是行业透明度隐忧，但增长趋势明确。",
        "tc": "跨境數據黑箱，也是透明度隱憂。"
      },
      "actions": {
        "front": {
          "sc": "了解行业透明度现状",
          "tc": "了解透明度現狀"
        },
        "midback": {
          "sc": "归档Q1详细分析数据",
          "tc": "歸檔Q1數據"
        },
        "lead": {
          "sc": "数据缺口下的业务判断风险",
          "tc": "數據缺口風險"
        },
        "cross": {
          "sc": "跨境数据缺失对业务判断的影响",
          "tc": "跨境數據影響"
        }
      },
      "source": {
        "sc": "Insurance Business Mag",
        "tc": "Insurance Business Mag",
        "lang": "en"
      },
      "boards": [
        "macro",
        "compliance"
      ],
      "tags": {
        "sc": [
          "保险",
          "保费",
          "跨境",
          "数据缺口",
          "2026"
        ],
        "tc": [
          "保險",
          "保費",
          "跨境",
          "數據缺口",
          "2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-25T10:00:00+08:00",
      "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/hong-kong-insurance-market-extends-growth-run-as-data-gap-widens-583673.aspx",
      "sourceKey": "insurancebusinessmag",
      "sourceTier": "pro",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "clusterCount": 1,
      "score": 76,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": false,
      "ingestedAt": "2026-07-26T23:59:00+08:00",
      "contentRole": {
        "sc": "本站导读（非原文）",
        "tc": "本站導讀（非原文）"
      },
      "id": "ia-public-disclosure-2026",
      "title": {
        "sc": "公开披露规则推进：获授权保险人公众披露要求（2026 落地语境）。",
        "tc": "公開披露規則推進：獲授權保險人公眾披露要求（2026 落地語境）。"
      },
      "summary": {
        "sc": "行业报道称保监局将推进保险人公开披露规则，适用于本地成立及海外在港分公司等（具体以宪报/规则文本为准）。对持牌人意味着：保司偿付能力、风险与业务信息的可比性提升，但解读仍须回到官方文本。",
        "tc": "行業報道稱保監局將推進保險人公開披露規則，適用於本地成立及海外在港分公司等（具體以憲報/規則文本為準）。對持牌人意味著：保司償付能力、風險與業務信息的可比性提升，但解讀仍須回到官方文本。"
      },
      "why": {
        "sc": "中后台与管理侧应用：尽调保司、内部培训材料更新；前线避免把未核披露数字写成承诺。",
        "tc": "中後台與管理側應用：盡調保司、內部培訓材料更新；前線避免把未核披露數字寫成承諾。"
      },
      "actions": {
        "front": {
          "sc": "客户问“哪家更稳”时，引导至官方披露与评级，不做口头比较承诺。",
          "tc": "客戶問「哪家更穩」時，引導至官方披露與評級，不做口頭比較承諾。"
        },
        "midback": {
          "sc": "跟踪规则生效日与披露模板；更新保司档案字段。",
          "tc": "跟蹤規則生效日與披露模板；更新保司檔案字段。"
        },
        "lead": {
          "sc": "评估对渠道对保司合作尽调清单的影响。",
          "tc": "評估對渠道對保司合作盡調清單的影響。"
        },
        "cross": {
          "sc": "家办客户尽调包可预留公开披露字段。",
          "tc": "家辦客戶盡調包可預留公開披露字段。"
        }
      },
      "source": {
        "sc": "行业媒体 · Insurance Asia 等",
        "tc": "行業媒體 · Insurance Asia 等"
      },
      "sourceTier": "pro",
      "tags": {
        "sc": [
          "公开披露",
          "偿付能力",
          "保司"
        ],
        "tc": [
          "公開披露",
          "償付能力",
          "保司"
        ]
      },
      "themes": [
        "reg",
        "firm"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 3,
        "lead": 3,
        "cross": 2
      },
      "publishedAt": "2026-07-25T10:00:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/news/hong-kong-ia-proceed-public-disclosure-rules-insurers-2026",
      "sourceKey": "insuranceasia",
      "boards": [
        "reg"
      ],
      "contentKind": "industry_news"
    },
    {
      "id": "nfra-cybersecurity-rules-jul",
      "clusterCount": 1,
      "score": 83,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "nfra:cyber-rules-202607",
      "title": {
        "sc": "金融监管总局就银行业保险业网络安全管理办法征求意见",
        "tc": "金融監管總局就銀行業保險業網絡安全管理辦法徵求意見"
      },
      "summary": {
        "sc": "国家金融监督管理总局近日就《银行业保险业网络安全管理办法（征求意见稿）》公开征求意见，涵盖网络安全管理体系、数据安全、应急响应等要求。该办法将统一银行保险业网络安全监管标准，对保险公司IT治理提出更高合规要求。"
      },
      "why": {
        "sc": "网络安全管理升级=保险公司IT合规投入将增加",
        "tc": "網絡安全管理升級=保險公司IT合規投入增加"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 0,
        "midback": 2,
        "lead": 1,
        "cross": 0
      },
      "source": {
        "sc": "NFRA",
        "tc": "國家金融監管總局",
        "lang": "zh"
      },
      "boards": [
        "reg"
      ],
      "themes": [
        "cyber",
        "compliance"
      ],
      "tags": {
        "sc": [
          "NFRA",
          "网络安全",
          "管理办法",
          "征求意见"
        ],
        "tc": [
          "NFRA",
          "網絡安全",
          "管理辦法",
          "徵求意見"
        ]
      },
      "contentKind": "circular",
      "publishedAt": "2026-07-25T09:00:00+08:00",
      "originalUrl": "https://www.nfra.gov.cn/cn/view/pages/ItemDetail.html?docId=1264203&itemId=915",
      "ingestedAt": "2026-07-30T18:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "ia-q1-2026-stats",
      "title": {
        "sc": "2026年Q1临时统计：长期业务新造保费约1411亿港元，同比约+51.1%。",
        "tc": "2026年Q1臨時統計：長期業務新造保費約1411億港元，同比約+51.1%。"
      },
      "summary": {
        "sc": "据行业报道援引保监局2026年7月24日发布的临时统计：2026年第一季度全港毛保费约2916亿港元，同比+32.3%。长期业务新造保费（不含退休计划）约1411亿，同比+51.1%；其中分红业务约1257亿，同比+53.7%。2025年全年长期新造保费约3309亿，同比+50.6%。",
        "tc": "據行業報道援引保監局2026年7月24日發布的臨時統計：2026年第一季度全港毛保費約2916億港元，同比+32.3%。長期業務新造保費（不含退休計劃）約1411億，同比+51.1%；其中分紅業務約1257億，同比+53.7%。2025年全年長期新造保費約3309億，同比+50.6%。"
      },
      "why": {
        "sc": "确认市场仍在高速扩张，但监管同步收紧——产能叙事必须与合规成本一起看。",
        "tc": "確認市場仍在高速擴張，但監管同步收緊——產能敘事必須與合規成本一起看。"
      },
      "actions": {
        "front": {
          "sc": "用最新公开数据做市场沟通，避免沿用过期渠道占比。",
          "tc": "用最新公開數據做市場溝通，避免沿用過期渠道佔比。"
        },
        "midback": {
          "sc": "更新内部市场简报与产品策略会材料。｜关注大额新单带来的 AML/来源财富审查负荷。",
          "tc": "更新內部市場簡報與產品策略會材料。｜關注大額新單帶來的 AML/來源財富審查負荷。"
        },
        "lead": {
          "sc": "Q1 约占2025全年新造约43%——勿线性外推全年，做情景预算。",
          "tc": "Q1 約佔2025全年新造約43%——勿線性外推全年，做情景預算。"
        },
        "cross": {
          "sc": "高净值与架构型需求仍活跃，强化全案协作。",
          "tc": "高淨值與架構型需求仍活躍，強化全案協作。"
        }
      },
      "source": {
        "sc": "行业媒体报道 · 援引保监局临时统计（2026-07-24）",
        "tc": "行業媒體報道 · 援引保監局臨時統計（2026-07-24）"
      },
      "sourceTier": "pro",
      "tags": {
        "sc": [
          "市场数据",
          "新单保费",
          "Q1"
        ],
        "tc": [
          "市場數據",
          "新單保費",
          "Q1"
        ]
      },
      "themes": [
        "channel",
        "macro",
        "firm"
      ],
      "rolesImpact": {
        "front": 2,
        "midback": 2,
        "lead": 3,
        "cross": 2
      },
      "publishedAt": "2026-07-24T18:00:00+08:00",
      "clusterCount": 2,
      "score": 92,
      "verifyStatus": "verified",
      "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/hong-kong-insurance-market-extends-growth-run-as-data-gap-widens-583673.aspx",
      "featured": true,
      "note": {
        "sc": "请回保监局官网季度临时统计页核对原文表格。",
        "tc": "請回保監局官網季度臨時統計頁核對原文表格。"
      },
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "insurancebusinessmag",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "insurer",
        "market"
      ],
      "contentKind": "stats"
    },
    {
      "id": "hkma-complaints-20260724",
      "title": {
        "sc": "金管局《投诉观察》第28期发布（2026-07-24）。",
        "tc": "金管局《投訴觀察》第28期發布（2026-07-24）。"
      },
      "summary": {
        "sc": "金管局2026年7月24日发布 Complaints Watch Issue No.28。银行渠道保险销售相关投诉模式值得经纪对照：披露、适合性、跟进服务仍是高频议题。",
        "tc": "金管局2026年7月24日發布 Complaints Watch Issue No.28。銀行渠道保險銷售相關投訴模式值得經紀對照：披露、適合性、跟進服務仍是高頻議題。"
      },
      "why": {
        "sc": "投诉主题往往领先于中介纪律焦点，可作前线质检清单。",
        "tc": "投訴主題往往領先於中介紀律焦點，可作前線質檢清單。"
      },
      "actions": {
        "front": {
          "sc": "复核适合性与产品比较记录是否完整。",
          "tc": "復核適合性與產品比較記錄是否完整。"
        },
        "midback": {
          "sc": "把投诉高频点编入情景演练。｜对照公司投诉台账与公开主题是否重合。",
          "tc": "把投訴高頻點編入情景演練。｜對照公司投訴台賬與公開主題是否重合。"
        },
        "lead": {
          "sc": "月度质检增加「投诉主题」抽样。",
          "tc": "月度質檢增加「投訴主題」抽樣。"
        },
        "cross": {
          "sc": "跨境客户投诉升级路径预先设定。",
          "tc": "跨境客戶投訴升級路徑預先設定。"
        }
      },
      "source": {
        "sc": "香港金融管理局 · 新闻稿 2026-07-24",
        "tc": "香港金融管理局 · 新聞稿 2026-07-24"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "投诉",
          "金管局",
          "适合性"
        ],
        "tc": [
          "投訴",
          "金管局",
          "適合性"
        ]
      },
      "themes": [
        "compliance",
        "channel"
      ],
      "rolesImpact": {
        "front": 2,
        "midback": 3,
        "lead": 2,
        "cross": 1
      },
      "publishedAt": "2026-07-24T16:00:00+08:00",
      "score": 80,
      "verifyStatus": "verified",
      "originalUrl": "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/07/20260724-3/",
      "featured": false,
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "hkma",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "market",
        "reg"
      ],
      "contentKind": "press"
    },
    {
      "id": "aia-q1-market-leader-jul24",
      "clusterCount": 1,
      "score": 80,
      "verifyStatus": "verified",
      "sourceTier": "insurer",
      "sourceKey": "aia",
      "title": {
        "sc": "友邦香港2026年Q1勇夺7个市场第一 继续领跑",
        "tc": "友邦香港2026年Q1勇奪7個市場第一 繼續領跑"
      },
      "summary": {
        "sc": "2026年7月24日友邦香港公布，根据保监局Q1临时统计数字，公司在有效业务、新造保单等维度勇夺最多市场第一，持续稳居香港保险市场之冠。CEO Alger Fung表示这反映客户信任而非仅是排名。[EN原文]",
        "tc": "友邦香港Q1奪7個市場第一，CEO馮偉昌表示反映客戶信任。"
      },
      "why": {
        "sc": "AIA连续领跑=市场份额格局验证，竞争优势持续",
        "tc": "AIA連續領跑=市場份額格局驗證"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 2,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "source": {
        "sc": "AIA HK",
        "tc": "AIA HK",
        "lang": "zh"
      },
      "boards": [
        "insurer"
      ],
      "themes": [
        "market-leader",
        "quarterly"
      ],
      "tags": {
        "sc": [
          "AIA",
          "友邦",
          "市场第一",
          "Q1"
        ],
        "tc": [
          "AIA",
          "友邦",
          "市場第一",
          "Q1"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2026-07-24T10:00:00+08:00",
      "originalUrl": "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/2026/aia-press-release-20260724",
      "ingestedAt": "2026-07-30T18:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "prudential-health-summit-2026",
      "clusterCount": 1,
      "score": 76,
      "verifyStatus": "verified",
      "sourceTier": "insurer",
      "sourceKey": "prudential",
      "title": {
        "sc": "保诚保险举办2026健康论坛 聚焦优化患者医疗体验",
        "tc": "保誠保險舉辦2026健康論壇 聚焦優化患者醫療體驗"
      },
      "summary": {
        "sc": "保诚保险于2026年举办健康论坛「优化患者医疗体验」，汇聚医疗界资深领袖与健康合作伙伴，探讨如何深化合作，为患者提供更清晰的指引及全面支持。此前保诚已扩展癌症直付服务至指定肿瘤中心，持续强化健康保障生态。"
      },
      "why": {
        "sc": "保司健康生态布局=从理赔者向健康管理伙伴转型",
        "tc": "保司健康生態佈局=從理賠者轉向健康管理夥伴"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 1,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "source": {
        "sc": "Prudential 保诚",
        "tc": "Prudential 保誠",
        "lang": "zh"
      },
      "boards": [
        "insurer"
      ],
      "themes": [
        "health",
        "ecosystem"
      ],
      "tags": {
        "sc": [
          "保诚",
          "健康论坛",
          "患者体验",
          "健康管理"
        ],
        "tc": [
          "保誠",
          "健康論壇",
          "患者體驗",
          "健康管理"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2026-07-24T10:00:00+08:00",
      "originalUrl": "https://www.prudential.com.hk/tc/about-us/newsroom/prudential-health-summit-improving-care-for-every-patient/",
      "ingestedAt": "2026-07-30T18:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "ziyu-ceo-letter-20260724",
      "clusterCount": 1,
      "score": 86,
      "verifyStatus": "verified",
      "sourceTier": "media",
      "sourceKey": "weixin",
      "title": {
        "sc": "资遇经纪 CEO 年度公开信：信任，是时间留下的凭证",
        "tc": "資遇經紀 CEO 年度公開信：信任，是時間留下的憑證"
      },
      "summary": {
        "sc": "资遇保险经纪 CEO 刘日昌博士发表首封年度公开信（2026.07.24），提出「从价值分配走向价值创造」的核心命题。将保险市场的消费者/从业者/保司三方博弈定义为「不可能三角」，并给出解法：将衡量单位从单笔交易延伸至客户全服务周期。截至7月，资遇 IFA 规模近 600 人，新签约系统已覆盖 500 人，2026 年目标推动 60% 合作保司 API 上线。",
        "tc": "資遇保險經紀 CEO 劉日昌博士發表首封年度公開信（2026.07.24），提出「從價值分配走向價值創造」的核心命題。將保險市場的消費者/從業者/保司三方博弈定義為「不可能三角」，並給出解法：將衡量單位從單筆交易延伸至客戶全服務周期。截至7月，資遇 IFA 規模近 600 人，新簽約系統已覆蓋 500 人，2026 年目標推動 60% 合作保司 API 上線。"
      },
      "why": {
        "sc": "资遇是香港经纪渠道的重要玩家（与ZUU同赛道）。这封公开信有三层价值：①「不可能三角」模型是对佣金改革后行业困境的理论化回应，适用于所有经纪公司；②「合规不是刹车而是轨道」的提法，与 ZUU 的「合规前置」第一性原理高度同构；③首次披露的 IFA 600 人规模+API 对接计划，是经纪赛道数字化竞争的重要信号。",
        "tc": "資遇是香港經紀渠道的重要玩家（與ZUU同賽道）。這封公開信有三層價值：①「不可能三角」模型是對佣金改革後行業困境的理論化回應，適用於所有經紀公司；②「合規不是煞車而是軌道」的提法，與 ZUU 的「合規前置」第一性原理高度同構；③首次披露的 IFA 600 人規模+API 對接計劃，是經紀賽道數字化競爭的重要信號。"
      },
      "actions": {
        "front": {
          "sc": "「不可能三角」模型可用于客户沟通：解释为什么好产品+好服务需要可持续的商业模式支撑",
          "tc": "「不可能三角」模型可用於客戶溝通：解釋為什麼好產品+好服務需要可持續的商業模式支撐"
        },
        "midback": {
          "sc": "资遇的合规体系（外部律师月会+案例研讨+边界培训）可供参考",
          "tc": "資遇的合規體系（外部律師月會+案例研討+邊界培訓）可供參考"
        },
        "lead": {
          "sc": "经纪人规模600人+API对接是行业标杆数据，可用于团队战略对标",
          "tc": "經紀人規模600人+API對接是行業標桿數據，可用於團隊戰略對標"
        },
        "cross": {
          "sc": "资遇获跨境保险服务+移民身份规划双奖，跨境布局信号明确",
          "tc": "資遇獲跨境保險服務+移民身份規劃雙獎，跨境佈局信號明確"
        }
      },
      "rolesImpact": {
        "front": 4,
        "midback": 4,
        "lead": 5,
        "cross": 3
      },
      "source": {
        "sc": "资遇财富管理 · 公众号",
        "lang": "zh"
      },
      "boards": [
        "market",
        "insurer"
      ],
      "themes": [
        "channel",
        "compliance",
        "career"
      ],
      "tags": {
        "sc": [
          "CEO公开信",
          "经纪",
          "资遇",
          "行业思想"
        ],
        "tc": [
          "CEO公開信",
          "經紀",
          "資遇",
          "行業思想"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2026-07-24T10:00:00+08:00",
      "originalUrl": "https://mp.weixin.qq.com/s/nYovc-7UW75pt-560SjWGw"
    },
    {
      "id": "allianz-hsbc-singapore-jul24",
      "clusterCount": 1,
      "score": 82,
      "verifyStatus": "verified",
      "sourceTier": "media",
      "sourceKey": "reuters",
      "title": {
        "sc": "安联21亿美元收购汇丰新加坡寿险 亚洲版图再扩张",
        "tc": "安聯21億美元收購滙豐新加坡壽險 亞洲版圖再擴張"
      },
      "summary": {
        "sc": "2026年7月24日Reuters报道：汇丰同意以27亿新加坡元（约21亿美元）将新加坡人寿及健康保险业务售予安联。汇丰将继续聚焦亚洲财富管理及批发银行业务，安联则进一步巩固亚太保险版图。交易含15年独家银保合作。[EN原文]",
        "tc": "滙豐$21億售新加坡壽險予安聯，含15年獨家銀保合作。"
      },
      "why": {
        "sc": "安联-汇丰交易=亚洲保险市场并购活跃信号，银保渠道价值凸显",
        "tc": "安聯-滙豐交易=亞洲保險併購活躍，銀保渠道價值凸顯"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 2,
        "cross": 0
      },
      "source": {
        "sc": "Reuters",
        "tc": "Reuters",
        "lang": "en"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "ma",
        "bancassurance"
      ],
      "tags": {
        "sc": [
          "安联",
          "汇丰",
          "收购",
          "新加坡",
          "银保"
        ],
        "tc": [
          "安聯",
          "滙豐",
          "收購",
          "新加坡",
          "銀保"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-24T08:00:00+08:00",
      "originalUrl": "https://www.reuters.com/world/asia-pacific/hsbc-sells-singapore-insurance-business-germanys-allianz-209-billion-deal-2026-07-23/",
      "ingestedAt": "2026-07-30T18:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "offshore-trust-tax-20260724",
      "clusterCount": 1,
      "score": 85,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "mof-sta",
      "title": {
        "sc": "财政部/税务总局发布离岸信托个税新规：设立即征税、存续即穿透、退出即清算。",
        "tc": "財政部/稅務總局發佈離岸信託個稅新規：設立即徵稅、存續即穿透、退出即清算。"
      },
      "summary": {
        "sc": "2026年7月24日，财政部、税务总局联合发布《关于离岸信托个人所得税有关事项的公告》（2026年第21号），首次建立离岸信托全周期个税征管体系。存量信托享90天申报宽限期免滞纳金，可申请5年分期缴纳。新规溯及2023年1月1日起的财产装入行为，标志着跨境信托避税空间基本清零。",
        "tc": "2026年7月24日，財政部、稅務總局聯合發佈《關於離岸信託個人所得稅有關事項的公告》（2026年第21號），首次建立離岸信託全週期個稅徵管體系。存量信託享90天申報寬限期免滯納金，可申請5年分期繳納。新規溯及2023年1月1日起的財產裝入行為，標誌著跨境信託避稅空間基本清零。"
      },
      "why": {
        "sc": "离岸信托是家办核心工具，新规直接改变跨境财富架构的税务逻辑——从「分配时才交税」变为「装入即触发」；90天宽限期截至10月22日，高净值客户需立即行动。",
        "tc": "離岸信託是家辦核心工具，新規直接改變跨境財富架構的稅務邏輯——從「分配時才交稅」變為「裝入即觸發」；90天寬限期截至10月22日，高淨值客戶需立即行動。"
      },
      "actions": {
        "front": {
          "sc": "向持有离岸信托的客户提示90天宽限期，建议尽快联系受托人获取财务报表。",
          "tc": "向持有離岸信託的客戶提示90天寬限期，建議盡快聯繫受託人獲取財務報表。"
        },
        "midback": {},
        "lead": {
          "sc": "组织跨境税务专题培训，更新家办架构方案的税务合规模块。",
          "tc": "組織跨境稅務專題培訓，更新家辦架構方案的稅務合規模組。"
        },
        "cross": {
          "sc": "重新评估现有离岸信托架构的税务风险，必要时调整受托人安排或信托契约。",
          "tc": "重新評估現有離岸信託架構的稅務風險，必要時調整受託人安排或信託契約。"
        }
      },
      "rolesImpact": {
        "front": 2,
        "midback": 1,
        "lead": 3,
        "cross": 5
      },
      "source": {
        "sc": "财政部 税务总局公告2026年第21号",
        "lang": "zh"
      },
      "boards": [
        "family",
        "reg"
      ],
      "themes": [
        "cross-border-tax",
        "trust-compliance"
      ],
      "tags": {
        "sc": [
          "离岸信托",
          "个税",
          "跨境税务",
          "21号公告"
        ],
        "tc": [
          "離岸信託",
          "個稅",
          "跨境稅務",
          "21號公告"
        ]
      },
      "contentKind": "circular",
      "publishedAt": "2026-07-24T00:00:00+08:00",
      "originalUrl": "https://www.chinatax.gov.cn/chinatax/n810341/n810755/c2026_21.html"
    },
    {
      "id": "axa-menopause-survey-jul23",
      "clusterCount": 1,
      "score": 75,
      "verifyStatus": "verified",
      "sourceTier": "insurer",
      "sourceKey": "axa",
      "title": {
        "sc": "AXA安盛调查：香港在职女性更年期认知严重不足",
        "tc": "AXA安盛調查：香港在職女性更年期認知嚴重不足"
      },
      "summary": {
        "sc": "2026年7月23日AXA安盛发布调查，揭示香港在职女性对更年期健康认知普遍不足，多数受访者缺乏相关知识且不知如何获取专业协助。AXA倡导企业加强女性健康保障，呼应其医疗及危疾产品线的市场定位。"
      },
      "why": {
        "sc": "女性健康保障缺口=保险公司产品创新与市场教育机会",
        "tc": "女性健康保障缺口=產品創新與市場教育機會"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 1,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "source": {
        "sc": "AXA 安盛",
        "tc": "AXA 安盛",
        "lang": "zh"
      },
      "boards": [
        "insurer"
      ],
      "themes": [
        "health",
        "women"
      ],
      "tags": {
        "sc": [
          "AXA",
          "安盛",
          "更年期",
          "女性健康",
          "调查"
        ],
        "tc": [
          "AXA",
          "安盛",
          "更年期",
          "女性健康",
          "調查"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2026-07-23T11:00:00+08:00",
      "originalUrl": "https://www.axa.com.hk/zh/news-room/2026",
      "ingestedAt": "2026-07-30T18:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "sunlife-ride-to-shine-jul22",
      "clusterCount": 1,
      "score": 73,
      "verifyStatus": "verified",
      "sourceTier": "insurer",
      "sourceKey": "sunlife",
      "title": {
        "sc": "Sun Life永明启动「善德永明耀香港」智能单车创举",
        "tc": "Sun Life永明啟動「善德永明耀香港」智能單車創舉"
      },
      "summary": {
        "sc": "2026年7月22日，Sun Life永明与香港善德基金会合作启动Ride-To-Shine Hong Kong智能单车动力创举。活动以全民参与为理念，结合运动科技与社区公益，展现永明在港品牌深耕及ESG承诺。"
      },
      "why": {
        "sc": "保司ESG+社区参与=品牌差异化与客户忠诚度建设",
        "tc": "保司ESG+社區參與=品牌差異化與客戶忠誠度"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "source": {
        "sc": "Sun Life 永明",
        "tc": "Sun Life 永明",
        "lang": "zh"
      },
      "boards": [
        "insurer"
      ],
      "themes": [
        "esg",
        "community"
      ],
      "tags": {
        "sc": [
          "Sun Life",
          "永明",
          "ESG",
          "社区公益"
        ],
        "tc": [
          "Sun Life",
          "永明",
          "ESG",
          "社區公益"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2026-07-22T14:00:00+08:00",
      "originalUrl": "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/2026/ride-to-shine-hong-kong/",
      "ingestedAt": "2026-07-30T18:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "nia-exit-entry-20260722",
      "clusterCount": 1,
      "score": 76,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "nia",
      "title": {
        "sc": "国务院发布出境入境管理新规：9 月 15 日起施行，大湾区刷脸通关常态化",
        "tc": "國務院發佈出境入境管理新規：9 月 15 日起施行，大灣區刷臉通關常態化"
      },
      "summary": {
        "sc": "2026 年 7 月 22 日，国务院公布出境入境管理规定（9 月 15 日施行）。同期移民局数据：大湾区 19 个口岸推行旅客「刷脸」智能通关，日均 27.6 万人次，通关时间缩短至 10 秒。港澳人才签注试点范围扩大。",
        "tc": "2026 年 7 月 22 日，國務院公佈出境入境管理規定（9 月 15 日施行）。同期移民局數據：大灣區 19 個口岸推行旅客「刷臉」智能通關，日均 27.6 萬人次。"
      },
      "why": {
        "sc": "出入境便利化=跨境 IFA 客户物理流动的基础设施。刷脸通关常态化意味着香港⇄内地之间的「生活圈」正在加速形成——客户跨境的频率越高，对两地财富管理的需求越密集。",
        "tc": "出入境便利化=跨境 IFA 客戶物理流動的基礎設施。刷臉通關常態化意味著香港⇄內地之間的「生活圈」正在加速形成。"
      },
      "actions": {
        "front": {
          "sc": "通关便利=跨境客户维护的物理成本下降",
          "tc": "通關便利=跨境客戶維護的物理成本下降"
        },
        "midback": {},
        "lead": {
          "sc": "大湾区生活圈=跨境财富管理需求密度上升",
          "tc": "大灣區生活圈=跨境財富管理需求密度上升"
        },
        "cross": {
          "sc": "出入境政策=身份规划的基础条件",
          "tc": "出入境政策=身份規劃的基礎條件"
        }
      },
      "rolesImpact": {
        "front": 4,
        "midback": 1,
        "lead": 3,
        "cross": 5
      },
      "source": {
        "sc": "国家移民管理局 · 2026年7月",
        "lang": "sc"
      },
      "boards": [
        "family"
      ],
      "themes": [
        "offshore",
        "identity-planning"
      ],
      "tags": {
        "sc": [
          "出入境",
          "大湾区",
          "刷脸通关"
        ],
        "tc": [
          "出入境",
          "大灣區",
          "刷臉通關"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2026-07-22T10:00:00+08:00",
      "originalUrl": "https://www.moj.gov.cn/pub/sfbgw/zcjd/202607/t20260731_538117.html"
    },
    {
      "id": "safe-qdii-20260717",
      "clusterCount": 1,
      "score": 78,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "safe",
      "title": {
        "sc": "外管局：新一轮 QDII 额度即将发放，跨境投融资便利化加码",
        "tc": "外管局：新一輪 QDII 額度即將發放，跨境投融資便利化加碼"
      },
      "summary": {
        "sc": "2026 年 7 月 17 日外汇局发布会：① 新一轮 QDII 额度即将发放，向公募产品倾斜；② 拟推「一揽子」跨境投融资便利化政策（简化 FDI 结汇、扩大外债试点、网上办登记）；③ 上半年外资来华净增约 1,600 亿美元，高技术制造业流入 +61%。对 IFA：QDII 额度和跨境便利化直接影响客户资产出境的合法通道。",
        "tc": "2026 年 7 月 17 日外匯局發布會：① 新一輪 QDII 額度即將發放，向公募產品傾斜；② 擬推「一攬子」跨境投融資便利化政策；③ 上半年外資來華淨增約 1,600 億美元。對 IFA：QDII 額度和跨境便利化直接影響客戶資產出境的合法通道。"
      },
      "why": {
        "sc": "QDII 额度=内地客户合法地把钱投向境外的管道。每一次额度发放，都等于 IFA 潜在客户群的一次扩容。上半年外资净增 1,600 亿美元，说明跨境资金流是双向的——IFA 既要帮客户「走出去」，也要理解「引进来」的监管逻辑。",
        "tc": "QDII 額度=內地客戶合法地把錢投向境外的管道。每一次額度發放，都等於 IFA 潛在客戶群的一次擴容。"
      },
      "actions": {
        "front": {
          "sc": "QDII额度=客户合法境外投资的管道",
          "tc": "QDII額度=客戶合法境外投資的管道"
        },
        "midback": {
          "sc": "跨境便利化政策=合规架构的新工具",
          "tc": "跨境便利化政策=合規架構的新工具"
        },
        "lead": {
          "sc": "外资流入+61%=中国市场对境外资金的吸引力仍在",
          "tc": "外資流入+61%=中國市場對境外資金的吸引力仍在"
        },
        "cross": {
          "sc": "跨境资金双向流动=IFA的核心价值在于架构设计",
          "tc": "跨境資金雙向流動=IFA的核心價值在於架構設計"
        }
      },
      "rolesImpact": {
        "front": 4,
        "midback": 3,
        "lead": 3,
        "cross": 5
      },
      "source": {
        "sc": "国家外汇管理局 · 2026年7月17日",
        "lang": "sc"
      },
      "boards": [
        "family"
      ],
      "themes": [
        "offshore",
        "global-allocation"
      ],
      "tags": {
        "sc": [
          "QDII",
          "外管局",
          "跨境投资"
        ],
        "tc": [
          "QDII",
          "外管局",
          "跨境投資"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2026-07-17T10:00:00+08:00",
      "originalUrl": "http://m.safe.gov.cn/safe/2026/0717/27705.html"
    },
    {
      "id": "genai-sandbox-plus-jul17",
      "clusterCount": 1,
      "score": 88,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "hkma-sfc-ia-mpfa",
      "title": {
        "sc": "GenA.I.沙盒++正式扩展至保险等多元金融领域",
        "tc": "GenA.I.沙盒++正式擴展至保險等多元金融領域"
      },
      "summary": {
        "sc": "2026年7月中旬，金管局联合证监会、保监局、积金局及数码港宣布推出「生成式人工智能沙盒++」，在2024年首版基础上将覆盖范围从银行业扩展至证券、资管、保险、强积金及储值支付工具。聚焦风险管理、反诈骗和客户体验三大场景，持续推进「以AI对抗AI」策略。参与机构可获得监管指引、技术支援及数码港超算中心GPU资源。[EN原文]",
        "tc": "金管局聯同證監會、保監局、積金局及數碼港推出GenA.I.沙盒++，覆蓋保險等多元金融領域，聚焦風險管理、反詐騙和客戶體驗。[EN原文]"
      },
      "why": {
        "sc": "GenA.I.沙盒扩展至保险=监管正式为保险业GenAI应用打开合规通道",
        "tc": "GenA.I.沙盒擴展至保險=監管正式為保險業GenAI應用打開合規通道"
      },
      "actions": {
        "front": {
          "sc": "关注沙盒中保险相关用例，评估GenAI在客户服务的合规应用",
          "tc": "關注沙盒中保險相關用例，評估GenAI在客戶服務的合規應用"
        },
        "midback": {
          "sc": "GenAI在反欺诈和风险管理场景的沙盒测试=优先级高",
          "tc": "GenAI在反欺詐和風險管理場景的沙盒測試=優先級高"
        },
        "lead": {
          "sc": "保险业GenAI合规框架渐清晰，应尽早评估内部用例",
          "tc": "保險業GenAI合規框架漸清晰，應盡早評估內部用例"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 2,
        "midback": 4,
        "lead": 4,
        "cross": 1
      },
      "source": {
        "sc": "金管局/保监局/证监会联合发布",
        "lang": "zh+en"
      },
      "boards": [
        "reg",
        "tech"
      ],
      "themes": [
        "GenAI",
        "sandbox",
        "insurtech"
      ],
      "tags": {
        "sc": [
          "GenAI沙盒",
          "保监局",
          "金管局",
          "数码港",
          "保险科技"
        ],
        "tc": [
          "GenAI沙盒",
          "保監局",
          "金管局",
          "數碼港",
          "保險科技"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2026-07-17T00:00:00+08:00",
      "originalUrl": "https://m.tech.china.com/redian/2026/0717/072026_1919989.html",
      "ingestedAt": "2026-08-01T12:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "aia-20260716-hyrox",
      "clusterCount": 1,
      "score": 75,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T16:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "友邦香港与HYROX香港宣布策略合作推动健康生活。",
        "tc": "友邦香港與HYROX香港宣布策略合作推動健康生活。"
      },
      "summary": {
        "sc": "友邦香港2026年7月16日宣布与HYROX香港成为策略合作伙伴，共同推动健康生活理念。合作涵盖品牌联乘、客户专属运动体验及健康管理增值服务。",
        "tc": "友邦與HYROX香港策略合作推動健康"
      },
      "why": {
        "sc": "品牌跨界合作提升客户健康管理体验，差异化竞争。",
        "tc": "品牌合作提升客戶體驗。"
      },
      "actions": {
        "front": {
          "sc": "可向关注健康生活方式的客户提及",
          "tc": "向關注健康的客戶提及"
        },
        "midback": {
          "sc": "更新友邦品牌合作档案",
          "tc": "更新品牌檔案"
        },
        "lead": {
          "sc": "品牌合作=客户活动策划的素材",
          "tc": "客戶活動素材"
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "AIA 新闻稿",
        "tc": "AIA 新聞稿",
        "lang": "zh"
      },
      "boards": [
        "product",
        "firm"
      ],
      "tags": {
        "sc": [
          "AIA",
          "HYROX",
          "品牌合作",
          "2026"
        ],
        "tc": [
          "AIA",
          "HYROX",
          "品牌合作",
          "2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-16T10:00:00+08:00",
      "originalUrl": "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/2026/aia-press-release-20260716",
      "sourceKey": "aia",
      "sourceTier": "insurer",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20260716-ashk-ifoa",
      "title": {
        "sc": "保监局刘中健：香港精算学会与英国精算师协会联合会议主题演讲（2026-07-16）。",
        "tc": "保監局劉中健：香港精算學會與英國精算師協會聯合會議主題演講（2026-07-16）。"
      },
      "summary": {
        "sc": "保监局执行董事（政策及法规）刘中健先生于2026年7月16日在香港精算学会与英国精算师协会联合会议上发表主题演讲，内容通常覆盖资本制度、分红治理与风险管理中心定位等政策方向。",
        "tc": "保監局執行董事（政策及法規）劉中健先生於2026年7月16日在香港精算學會與英國精算師協會聯合會議上發表主題演講，內容通常覆蓋資本制度、分紅治理與風險管理中心定位等政策方向。"
      },
      "why": {
        "sc": "近期政策沟通窗口，有助把握局方对精算与产品治理的公开口径。",
        "tc": "近期政策溝通窗口，有助把握局方對精算與產品治理的公開口徑。"
      },
      "actions": {
        "front": {
          "sc": "关注演讲中对客户沟通有影响的表述，勿断章取义。",
          "tc": "關注演講中對客戶溝通有影響的表述，勿斷章取義。"
        },
        "midback": {
          "sc": "下载讲稿做内部政策简报。｜对照 GL34/RBC 相关落地清单。",
          "tc": "下載講稿做內部政策簡報。｜對照 GL34/RBC 相關落地清單。"
        },
        "lead": {
          "sc": "纳入季度政策雷达。",
          "tc": "納入季度政策雷達。"
        },
        "cross": {
          "sc": "可用于专业形象沟通，非产品推介。",
          "tc": "可用於專業形象溝通，非產品推介。"
        }
      },
      "source": {
        "sc": "保监局演辞/文章 2026-07-16",
        "tc": "保監局演辭/文章 2026-07-16"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "演讲",
          "精算",
          "政策"
        ],
        "tc": [
          "演講",
          "精算",
          "政策"
        ]
      },
      "themes": [
        "reg",
        "par",
        "firm"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 3,
        "lead": 3,
        "cross": 1
      },
      "publishedAt": "2026-07-16T10:00:00+08:00",
      "score": 84,
      "featured": true,
      "originalUrl": "https://www.ia.org.hk/tc/infocenter/files/Keynote_Speech_Mr_Clement_Lau_ASHK_IFoA_Conference_CN.pdf",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T02:07:48+08:00",
      "evergreen": false,
      "clusterCount": 1,
      "verifyStatus": "verified",
      "boards": [
        "insurer",
        "product",
        "reg"
      ],
      "contentKind": "speech"
    },
    {
      "id": "ia-sales-rules-tightening-jul15",
      "clusterCount": 1,
      "score": 87,
      "verifyStatus": "verified",
      "sourceTier": "pro",
      "sourceKey": "insuranceasia",
      "title": {
        "sc": "保监局收紧销售规则 高管直接对全流程合规负责",
        "tc": "保監局收緊銷售規則 高管直接對全流程合規負責"
      },
      "summary": {
        "sc": "Insurance Asia报道：香港保监局推出一系列监管更新及执法措施，收紧保险销售行为。7月起实施跨行业背景查核安排覆盖逾11万名中介人；高管对销售全流程合规承担直接责任。此前6月已限制两家经纪公司牌照续期，因其未能有效管理转介业务。[EN原文]",
        "tc": "保監局收緊銷售規則，跨行業背景查核覆蓋11萬中介人，高管直接對銷售合規負責。"
      },
      "why": {
        "sc": "监管从紧+跨行业背景查核=合规成本上升，中介洗牌加速",
        "tc": "監管從緊+跨行業查核=合規成本上升，中介洗牌加速"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 0,
        "midback": 3,
        "lead": 2,
        "cross": 0
      },
      "source": {
        "sc": "Insurance Asia",
        "tc": "Insurance Asia",
        "lang": "en"
      },
      "boards": [
        "reg"
      ],
      "themes": [
        "compliance",
        "intermediary"
      ],
      "tags": {
        "sc": [
          "IA",
          "销售规则",
          "合规",
          "背景查核",
          "中介人"
        ],
        "tc": [
          "IA",
          "銷售規則",
          "合規",
          "背景查核",
          "中介人"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-15T12:00:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/news/hong-kong-ia-tightens-sales-rules-misconduct-scrutiny-grows",
      "ingestedAt": "2026-07-30T18:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "clusterCount": 1,
      "score": 80,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": false,
      "ingestedAt": "2026-07-26T23:59:00+08:00",
      "contentRole": {
        "sc": "本站导读（非原文）",
        "tc": "本站導讀（非原文）"
      },
      "id": "ia-20260715-sales-practices",
      "title": {
        "sc": "行业观察：保监局强化销售行为监管（误导/适当性/录音录像相关叙事升温）。",
        "tc": "行業觀察：保監局強化銷售行為監管（誤導/適當性/錄音錄影相關敘事升溫）。"
      },
      "summary": {
        "sc": "2026年7月中旬多家行业媒体报道，保监局持续推进销售行为整治，聚焦误导销售、适当性评估与过程留痕等。公开通函层面仍以既有操守守则、巡查发现与指引为准；本条作线索收录，执行细节请回一手原文。",
        "tc": "2026年7月中旬多家行業媒體報道，保監局持續推進銷售行為整治，聚焦誤導銷售、適當性評估與過程留痕等。公開通函層面仍以既有操守守則、巡查發現與指引為準；本條作線索收錄，執行細節請回一手原文。"
      },
      "why": {
        "sc": "前线话术与中后台质检清单需同步升温：不是新“口号”，而是巡查与续牌条件的现实压力。",
        "tc": "前線話術與中後台質檢清單需同步升溫：不是新「口號」，而是巡查與續牌條件的現實壓力。"
      },
      "actions": {
        "front": {
          "sc": "复盘异议话术与计划书口径；禁止保证收益/返佣暗示。",
          "tc": "復盤異議話術與計劃書口徑；禁止保證收益/返佣暗示。"
        },
        "midback": {
          "sc": "抽检录音/过程文件与适当性文档完整性；更新质检抽检表。",
          "tc": "抽檢錄音/過程文件與適當性文檔完整性；更新質檢抽檢表。"
        },
        "lead": {
          "sc": "团队周会强调销售行为红线与案例复盘；绑定续牌风险。",
          "tc": "團隊週會強調銷售行為紅線與案例復盤；綁定續牌風險。"
        },
        "cross": {
          "sc": "跨境客户面谈全流程在港完成，避免远程招揽痕迹。",
          "tc": "跨境客戶面談全流程在港完成，避免遠程招攬痕跡。"
        }
      },
      "source": {
        "sc": "行业媒体线索 · 待核一手",
        "tc": "行業媒體線索 · 待核一手"
      },
      "sourceTier": "pro",
      "tags": {
        "sc": [
          "销售行为",
          "适当性",
          "巡查"
        ],
        "tc": [
          "銷售行為",
          "適當性",
          "巡查"
        ]
      },
      "themes": [
        "compliance",
        "reg"
      ],
      "rolesImpact": {
        "front": 3,
        "midback": 3,
        "lead": 3,
        "cross": 2
      },
      "publishedAt": "2026-07-15T12:00:00+08:00",
      "originalUrl": "https://www.asiainsurancereview.com/News/ViewNewsLetterArticle/id/96190/Type/eDaily/Hong-Kong-IA-initiates-crackdown-on-sales-practices",
      "sourceKey": "asiainsurancereview",
      "boards": [
        "conduct"
      ],
      "contentKind": "industry_news",
      "note": {
        "sc": "媒体线索；规则以 IA 通函/操守守则为准。",
        "tc": "媒體線索；規則以 IA 通函/操守守則為準。"
      }
    },
    {
      "id": "creditsights-2026-2h",
      "clusterCount": 1,
      "score": 78,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T20:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "CreditSights展望：2026下半年中港跨境资金规则或进一步收紧。",
        "tc": "CreditSights展望：2026下半年中港跨境資金規則或進一步收緊。"
      },
      "summary": {
        "sc": "CreditSights 7月发布亚太金融业2H26展望：亚洲保险盈利向好但面临多重压力。最值得警惕的是中港跨境资金流动规则可能进一步收紧。香港保险公司VNB增长持续，日本寿险受惠加息。[EN原文]",
        "tc": "CreditSights:中港跨境資金流動或進一步收緊"
      },
      "why": {
        "sc": "独立研究机构的跨境风险预警，也是提前准备的参考。",
        "tc": "獨立機構的跨境風險預警。"
      },
      "actions": {
        "front": {
          "sc": "关注跨境资金流动政策变化",
          "tc": "關注跨境資金政策"
        },
        "midback": {
          "sc": "准备跨境业务应急预案",
          "tc": "準備跨境應急預案"
        },
        "lead": {
          "sc": "跨境收紧=客源多元化紧迫性",
          "tc": "客源多元化緊迫性"
        },
        "cross": {
          "sc": "跨境资金的合规路径需要提前规划",
          "tc": "跨境資金合規路徑"
        }
      },
      "source": {
        "sc": "CreditSights",
        "tc": "CreditSights",
        "lang": "en"
      },
      "boards": [
        "macro",
        "cross"
      ],
      "tags": {
        "sc": [
          "CreditSights",
          "跨境",
          "资金",
          "展望",
          "2026"
        ],
        "tc": [
          "CreditSights",
          "跨境",
          "資金",
          "展望",
          "2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-15T10:00:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/news/asian-insurer-gains-face-regulatory-pressure-in-second-half-2026",
      "sourceKey": "insuranceasia",
      "sourceTier": "pro",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "hk-international-schools-2026",
      "clusterCount": 1,
      "score": 65,
      "verifyStatus": "verified",
      "sourceTier": "pro",
      "sourceKey": "henley",
      "title": {
        "sc": "香港国际学校需求激增：家办家庭推动学位竞争白热化",
        "tc": "香港國際學校需求激增：家辦家庭推動學位競爭白熱化"
      },
      "summary": {
        "sc": "随着家办和 CIES 家庭涌入香港，国际学校学位需求大幅上升。Henley & Partners 教育服务部门报告：香港国际学校的申请等候名单显著延长，部分名校的债券价格已突破 500 万港元。精英教育已成为家办服务链条的关键环节。",
        "tc": "隨著家辦和 CIES 家庭湧入香港，國際學校學位需求大幅上升。Henley & Partners 教育部門報告：香港國際學校的申請等候名單顯著延長，部分名校的債券價格已突破 500 萬港元。精英教育已成為家辦服務鏈條的關鍵環節。"
      },
      "why": {
        "sc": "教育是家办客户的「隐性需求」——客户嘴上说「理财」，心里想的是「孩子」。国际学校学位/债券/升学规划，是跨境家办的差异化服务入口。",
        "tc": "教育是家辦客戶的「隱性需求」——客戶嘴上說「理財」，心裡想的是「孩子」。國際學校學位/債券/升學規劃，是跨境家辦的差異化服務入口。"
      },
      "actions": {
        "front": {
          "sc": "教育规划是与客户建立长期信任的天然切入点",
          "tc": "教育規劃是與客戶建立長期信任的天然切入點"
        },
        "midback": {},
        "lead": {
          "sc": "教育服务可成为家办业务的增值模块",
          "tc": "教育服務可成為家辦業務的增值模塊"
        },
        "cross": {
          "sc": "国际学校是跨境家庭选择香港的关键考量之一",
          "tc": "國際學校是跨境家庭選擇香港的關鍵考量之一"
        }
      },
      "rolesImpact": {
        "front": 3,
        "midback": 1,
        "lead": 2,
        "cross": 4
      },
      "source": {
        "sc": "Henley Education / SCMP",
        "lang": "zh"
      },
      "boards": [
        "family"
      ],
      "themes": [
        "education",
        "family-office"
      ],
      "tags": {
        "sc": [
          "教育",
          "国际学校",
          "家办"
        ],
        "tc": [
          "教育",
          "國際學校",
          "家辦"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-15T10:00:00+08:00",
      "originalUrl": "https://www.henleyglobal.com/services/education"
    },
    {
      "id": "ia-licence-20260630",
      "title": {
        "sc": "持牌中介统计（截至2026-06-30）：个人持牌约12.25万，经纪公司810家。",
        "tc": "持牌中介統計（截至2026-06-30）：個人持牌約12.25萬，經紀公司810家。"
      },
      "summary": {
        "sc": "保监局公布截至2026年6月30日保险中介牌照统计：个人持牌人合计122,481人（其中经纪业务代表15,026）；持牌经纪公司810家；持牌代理机构1,470家；中介总数124,761。",
        "tc": "保監局公布截至2026年6月30日保險中介牌照統計：個人持牌人合計122,481人（其中經紀業務代表15,026）；持牌經紀公司810家；持牌代理機構1,470家；中介總數124,761。"
      },
      "why": {
        "sc": "人力供给侧的官方底数；结合业务量可判断「人海 vs 专业密度」分化。",
        "tc": "人力供給側的官方底數；結合業務量可判斷「人海 vs 專業密度」分化。"
      },
      "actions": {
        "front": {
          "sc": "牌照类型与可做业务线要与自身登记一致，展业前自查。",
          "tc": "牌照類型與可做業務線要與自身登記一致，展業前自查。"
        },
        "midback": {
          "sc": "培训名额与 CPD 资源按持牌结构配置。｜对照公司名册与局方登记册，清掉无委任关系异常。",
          "tc": "培訓名額與 CPD 資源按持牌結構配置。｜對照公司名冊與局方登記冊，清掉無委任關係異常。"
        },
        "lead": {
          "sc": "招聘规划用官方结构，而非口头「市场有多少人」。",
          "tc": "招聘規劃用官方結構，而非口頭「市場有多少人」。"
        },
        "cross": {
          "sc": "跨境团队须确认代表牌照与业务线覆盖。",
          "tc": "跨境團隊須確認代表牌照與業務線覆蓋。"
        }
      },
      "source": {
        "sc": "保险业监管局 · 保险中介牌照统计",
        "tc": "保險業監管局 · 保險中介牌照統計"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "持牌人数",
          "经纪公司",
          "统计"
        ],
        "tc": [
          "持牌人數",
          "經紀公司",
          "統計"
        ]
      },
      "themes": [
        "channel",
        "career"
      ],
      "rolesImpact": {
        "front": 2,
        "midback": 3,
        "lead": 3,
        "cross": 1
      },
      "publishedAt": "2026-07-14T12:00:00+08:00",
      "score": 90,
      "verifyStatus": "verified",
      "originalUrl": "https://www.ia.org.hk/en/infocenter/statistics/statistics.html",
      "featured": true,
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "market",
        "reg"
      ],
      "contentKind": "stats"
    },
    {
      "id": "agentic-ai-insurance-jul14",
      "clusterCount": 1,
      "score": 70,
      "verifyStatus": "verified",
      "sourceTier": "research",
      "sourceKey": "arxiv",
      "title": {
        "sc": "学术前沿：Agentic AI时代的保险承保、定价与端到端自动化框架",
        "tc": "學術前沿：Agentic AI時代的保險承保、定價與端到端自動化框架"
      },
      "summary": {
        "sc": "arXiv 2026年7月论文《AI-Native Insurance for Agentic AI》提出Agentic AI时代保险新范式：保险覆盖对象从被动数字资产转向能推理、调用工具、改变外部状态的操作型AI代理。论文开发了针对网络攻击、自主决策失误、模型漂移、依赖中断、专业疏忽、监管违规及网络物理伤害等新风险的原生AI承保与定价框架。[EN原文]",
        "tc": "arXiv論文探討Agentic AI時代保險新範式，開發針對自主AI代理失誤、模型漂移等新風險的原生AI承保定價框架。[EN原文]"
      },
      "why": {
        "sc": "Agentic AI保险是前沿领域，预示保险产品形态的下一阶段演化",
        "tc": "Agentic AI保險是前沿領域，預示保險產品形態的下一階段演化"
      },
      "actions": {
        "front": {},
        "midback": {
          "sc": "了解Agentic AI风险分类，为未来产品开发储备知识",
          "tc": "了解Agentic AI風險分類，為未來產品開發儲備知識"
        },
        "lead": {
          "sc": "Agentic AI保险=保险产品创新的前沿方向",
          "tc": "Agentic AI保險=保險產品創新的前沿方向"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 0,
        "midback": 2,
        "lead": 2,
        "cross": 0
      },
      "source": {
        "sc": "arXiv",
        "lang": "zh+en"
      },
      "boards": [
        "tech"
      ],
      "themes": [
        "agentic-ai",
        "underwriting",
        "research"
      ],
      "tags": {
        "sc": [
          "Agentic AI",
          "保险科技",
          "承保框架",
          "学术论文"
        ],
        "tc": [
          "Agentic AI",
          "保險科技",
          "承保框架",
          "學術論文"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-14T08:00:00+08:00",
      "originalUrl": "https://arxiv.org/pdf/2607.13230",
      "ingestedAt": "2026-08-01T12:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "insurtech-funding-q1-2026",
      "clusterCount": 1,
      "score": 72,
      "verifyStatus": "verified",
      "sourceTier": "media",
      "sourceKey": "fintechly",
      "title": {
        "sc": "全球InsurTech融资回暖：Q1融资16.3亿美元，资金流向AI基础设施",
        "tc": "全球InsurTech融資回暖：Q1融資16.3億美元，資金流向AI基礎設施"
      },
      "summary": {
        "sc": "Fintechly 2026年7月报道：全球InsurTech融资在Q1 2026达16.3亿美元，为2022年底以来最强背靠背季度之一。AI-focused InsurTechs捕获大部分资金，但最强投资逻辑转向「保险公司可嵌入的基础设施」而非「颠覆性玩法」。传统保险公司成为主要买家。[EN原文]",
        "tc": "全球InsurTech Q1融資16.3億美元，AI-focused InsurTechs捕獲大部分資金，投資邏輯從顛覆轉向基礎設施。[EN原文]"
      },
      "why": {
        "sc": "InsurTech融资回暖+AI基础设施转向=保险科技进入务实落地期",
        "tc": "InsurTech融資回暖+AI基礎設施轉向=保險科技進入務實落地期"
      },
      "actions": {
        "front": {},
        "midback": {
          "sc": "关注AI基础设施类InsurTech解决方案的采购评估",
          "tc": "關注AI基礎設施類InsurTech解決方案的採購評估"
        },
        "lead": {
          "sc": "融资回暖信号=保险科技投资窗口正在打开",
          "tc": "融資回暖信號=保險科技投資窗口正在打開"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 0,
        "midback": 2,
        "lead": 3,
        "cross": 0
      },
      "source": {
        "sc": "Fintechly",
        "lang": "zh+en"
      },
      "boards": [
        "market",
        "tech"
      ],
      "themes": [
        "insurtech",
        "funding",
        "AI"
      ],
      "tags": {
        "sc": [
          "InsurTech",
          "融资",
          "AI基础设施",
          "Q1 2026"
        ],
        "tc": [
          "InsurTech",
          "融資",
          "AI基礎設施",
          "Q1 2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-14T06:38:00+08:00",
      "originalUrl": "https://fintechly.com/capital/insurtech-funding-is-back-the-money-is-buying-infrastructure-not-disruption/",
      "ingestedAt": "2026-08-01T12:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "ia-20260712-speech",
      "clusterCount": 1,
      "score": 95,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": false,
      "ingestedAt": "2026-07-28T11:00:00+08:00",
      "contentRole": {
        "sc": "本站导读（非原文）",
        "tc": "本站導讀（非原文）"
      },
      "title": {
        "sc": "保监局刘中健演辞：以前瞻性监管及执法维护市场健康发展。",
        "tc": "保監局劉中健演辭：以前瞻性監管及執法維護市場健康發展。"
      },
      "summary": {
        "sc": "保监局2026年7月12日发表演辞，回顾分红保单销售三项措施——演示利率上限(2025年7月)、经纪转介费基准(2025年10月)、佣金分摊(2026年1月)。并说明与金管局推动的跨行业背景查核安排已于7月生效，覆盖约11万名长期业务中介。",
        "tc": "保監局7月12日演辭回顧分紅保單三項銷售措施及跨行業背景查核"
      },
      "why": {
        "sc": "监管最高层发声，确认三大措施已全部落地，行业合规的官方定调。",
        "tc": "監管最高層發聲，確認三大措施已全部落地。"
      },
      "actions": {
        "front": {
          "sc": "用监管原话向客户解释三项措施=对消费者的保护升级",
          "tc": "用監管原話解釋措施=對消費者保護"
        },
        "midback": {
          "sc": "更新销售合规手册中三项措施的引用来源",
          "tc": "更新銷售合規手冊引用來源"
        },
        "lead": {
          "sc": "组织团队学习演讲全文，作为Q3合规培训核心材料",
          "tc": "組織團隊學習演講全文"
        },
        "cross": {
          "sc": "跨境客户沟通时引用保监局官方口径增加公信力",
          "tc": "引用官方口徑增加公信力"
        }
      },
      "source": {
        "sc": "IA 保监局官方演辞",
        "tc": "IA 保監局官方演辭",
        "lang": "zh"
      },
      "boards": [
        "regulatory",
        "compliance"
      ],
      "tags": {
        "sc": [
          "保监局",
          "分红保单",
          "演辞",
          "2026"
        ],
        "tc": [
          "保監局",
          "分紅保單",
          "演辭",
          "2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-12T10:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/tc/infocenter/speeches_articles/20260712.html",
      "sourceKey": "ia",
      "sourceTier": "official",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20260710-illustration",
      "clusterCount": 1,
      "score": 91,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T11:00:00+08:00",
      "contentRole": {
        "sc": "本站导读（非原文）",
        "tc": "本站導讀（非原文）"
      },
      "title": {
        "sc": "保监局就分红保单演示回报率上限发出释义文件。",
        "tc": "保監局就分紅保單演示回報率上限發出釋義文件。"
      },
      "summary": {
        "sc": "保监局2026年7月10日发出通函，就分红保单利益说明文件的演示回报率上限提供释义文件（英文版），进一步明确2025年7月生效的演示利率上限应用范围与执行细则 [EN原文]",
        "tc": "保監局7月10日通函提供演示利率上限釋義文件（英文版）"
      },
      "why": {
        "sc": "佣金分摊+演示利率上限，也是双重约束，高演示产品稀缺加速。",
        "tc": "雙重約束下高演示產品稀缺加速。"
      },
      "actions": {
        "front": {
          "sc": "更新产品对比表，标注演示利率上限的官方文件编号",
          "tc": "更新產品對比表"
        },
        "midback": {
          "sc": "合规文档区新增该通函及释义文件",
          "tc": "合規文檔區新增通函"
        },
        "lead": {
          "sc": "团队培训演示利率章节引用此通函",
          "tc": "團隊培訓引用此通函"
        },
        "cross": {
          "sc": "向内地客户解释演示上限时引用该通函",
          "tc": "解釋演示上限時引用通函"
        }
      },
      "source": {
        "sc": "IA 保监局通函",
        "tc": "IA 保監局通函",
        "lang": "en"
      },
      "boards": [
        "regulatory",
        "product"
      ],
      "tags": {
        "sc": [
          "演示利率",
          "通函",
          "收益率上限"
        ],
        "tc": [
          "演示利率",
          "通函",
          "收益率上限"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-10T15:00:00+08:00",
      "originalUrl": "https://brdr.hkma.gov.hk/gb_chi/doc-ldg/docId/20260708-2-TC",
      "sourceKey": "hkma",
      "sourceTier": "official",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "tiger21-uhnw-allocation-2026",
      "clusterCount": 1,
      "score": 72,
      "verifyStatus": "verified",
      "sourceTier": "pro",
      "sourceKey": "tiger21",
      "title": {
        "sc": "TIGER 21 报告：超高净值家庭 28% 资产配置于私募股权",
        "tc": "TIGER 21 報告：超高淨值家庭 28% 資產配置於私募股權"
      },
      "summary": {
        "sc": "TIGER 21（全球超高净值投资者网络）发布 2026 资产配置报告：成员平均将 28% 的资产配置于私募股权，20% 于房地产，仅 8% 于固定收益。报告反映了全球最富有家庭的投资偏好正在从传统资产类别转向另类投资。",
        "tc": "TIGER 21（全球超高淨值投資者網絡）發佈 2026 資產配置報告：成員平均將 28% 的資產配置於私募股權，20% 於房地產，僅 8% 於固定收益。報告反映了全球最富有家庭的投資偏好正在從傳統資產類別轉向另類投資。"
      },
      "why": {
        "sc": "28% PE + 20% 地产——知道最富有的家庭在投什么，就能理解为什么他们需要保险做风险对冲、信托做架构隔离。资产配置数据是跨境家办服务的底色。",
        "tc": "28% PE + 20% 地產——知道最富有的家庭在投什麼，就能理解為什麼他們需要保險做風險對沖、信託做架構隔離。資產配置數據是跨境家辦服務的底色。"
      },
      "actions": {
        "front": {
          "sc": "客户的资产配置结构决定了保险需求类型",
          "tc": "客戶的資產配置結構決定了保險需求類型"
        },
        "midback": {},
        "lead": {
          "sc": "另类投资占比上升=大额寿险作为对冲工具的需求增加",
          "tc": "另類投資佔比上升=大額壽險作為對沖工具的需求增加"
        },
        "cross": {
          "sc": "全球资产配置视角是跨境家办区别于单一产品销售的核心",
          "tc": "全球資產配置視角是跨境家辦區別於單一產品銷售的核心"
        }
      },
      "rolesImpact": {
        "front": 3,
        "midback": 1,
        "lead": 3,
        "cross": 4
      },
      "source": {
        "sc": "TIGER 21",
        "lang": "zh"
      },
      "boards": [
        "family",
        "market"
      ],
      "themes": [
        "offshore",
        "asset-allocation"
      ],
      "tags": {
        "sc": [
          "资产配置",
          "私募股权",
          "UHNW"
        ],
        "tc": [
          "資產配置",
          "私募股權",
          "UHNW"
        ]
      },
      "contentKind": "stats",
      "publishedAt": "2026-07-10T10:00:00+08:00",
      "originalUrl": "https://tiger21.com/insights/asset-allocation-report-2026"
    },
    {
      "id": "nfra-cyber-consult-20260710",
      "clusterCount": 1,
      "score": 80,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "nfra",
      "title": {
        "sc": "金融监管总局就《银行业保险业网络安全管理办法》公开征求意见",
        "tc": "金融監管總局就《銀行業保險業網絡安全管理辦法》公開徵求意見"
      },
      "summary": {
        "sc": "2026 年 7 月 10 日，金融监管总局就银行业保险业网络安全管理办法征求意见，要求金融机构建立网络安全管理体系、开展网络安全风险管理。与香港保监局 2025 年 12 月修订的 GL20（网络保安指引）形成两地监管对标。",
        "tc": "2026 年 7 月 10 日，金融監管總局就銀行業保險業網絡安全管理辦法徵求意見，要求金融機構建立網絡安全管理體系、開展網絡安全風險管理。與香港保監局 2025 年 12 月修訂的 GL20（網絡保安指引）形成兩地監管對標。"
      },
      "why": {
        "sc": "两地同时收紧网络安全监管=跨境保险运营的合规成本将同步上升。对 IFA：客户数据传输、远程签单的技术合规将成为新门槛。",
        "tc": "兩地同時收緊網絡安全監管=跨境保險運營的合規成本將同步上升。對 IFA：客戶數據傳輸、遠程簽單的技術合規將成為新門檻。"
      },
      "actions": {
        "front": {
          "sc": "客户数据安全合规=获客流程需升级",
          "tc": "客戶數據安全合規=獲客流程需升級"
        },
        "midback": {
          "sc": "两地网络安全要求对标=合规体系可复用",
          "tc": "兩地網絡安全要求對標=合規體系可複用"
        },
        "lead": {},
        "cross": {
          "sc": "跨境数据传输=两地网络安全规则的交集点",
          "tc": "跨境數據傳輸=兩地網絡安全規則的交集點"
        }
      },
      "rolesImpact": {
        "front": 3,
        "midback": 4,
        "lead": 2,
        "cross": 3
      },
      "source": {
        "sc": "国家金融监管总局 · 2026年7月10日",
        "lang": "sc"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "reg",
        "tech",
        "offshore"
      ],
      "tags": {
        "sc": [
          "网络安全",
          "征求意见",
          "金融监管总局"
        ],
        "tc": [
          "網絡安全",
          "徵求意見",
          "金融監管總局"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2026-07-10T10:00:00+08:00",
      "originalUrl": "https://www.nfra.gov.cn/cn/view/pages/ItemDetail.html?docId=1264203&itemId=915"
    },
    {
      "id": "ia-20260710-illustration-review",
      "title": {
        "sc": "演示利率上限检讨机制：保监局发布释义说明（2026-07-10）。",
        "tc": "演示利率上限檢討機制：保監局發布釋義說明（2026-07-10）。"
      },
      "summary": {
        "sc": "保监局2026年7月10日通函发布《分红保单利益说明中演示利率上限的检讨机制》释义说明，明确上限检讨如何进行、适用对象与披露期望，直接影响计划书假设更新节奏。",
        "tc": "保監局2026年7月10日通函發布《分紅保單利益說明中演示利率上限的檢討機制》釋義說明，明確上限檢討如何進行、適用對象與披露期望，直接影響計劃書假設更新節奏。"
      },
      "why": {
        "sc": "演示数字是客户第一眼；检讨机制决定保司何时调整演示、前线何时换物料。",
        "tc": "演示數字是客戶第一眼；檢討機制決定保司何時調整演示、前線何時換物料。"
      },
      "actions": {
        "front": {
          "sc": "停用旧演示截图；以公司最新核可计划书为准。",
          "tc": "停用舊演示截圖；以公司最新核可計劃書為準。"
        },
        "midback": {
          "sc": "建立「演示假设变更」通知清单，对接各保司更新。｜抽检宣传物料是否仍用旧上限口径。",
          "tc": "建立「演示假設變更」通知清單，對接各保司更新。｜抽檢宣傳物料是否仍用舊上限口徑。"
        },
        "lead": {
          "sc": "把演示变更纳入产品委员会例会。",
          "tc": "把演示變更納入產品委員會例會。"
        },
        "cross": {
          "sc": "美元单演示变化需与融资情景一并更新。",
          "tc": "美元單演示變化需與融資情景一併更新。"
        }
      },
      "source": {
        "sc": "保监局规管通函 2026-07-10",
        "tc": "保監局規管通函 2026-07-10"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "演示利率",
          "分红",
          "释义说明"
        ],
        "tc": [
          "演示利率",
          "分紅",
          "釋義說明"
        ]
      },
      "themes": [
        "reg",
        "par",
        "product"
      ],
      "rolesImpact": {
        "front": 3,
        "midback": 3,
        "lead": 2,
        "cross": 2
      },
      "publishedAt": "2026-07-10T09:00:00+08:00",
      "score": 93,
      "verifyStatus": "verified",
      "featured": true,
      "originalUrl": "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/files/Circular_10072026.pdf",
      "clusterCount": 2,
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "product",
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "fstb-fo-tax-bill-20260708",
      "clusterCount": 1,
      "score": 88,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "fstb",
      "title": {
        "sc": "香港家办税惠修订草案提交立法会审议：扩免税范围、纳数字资产、取消5%门槛。",
        "tc": "香港家辦稅惠修訂草案提交立法會審議：擴免稅範圍、納數字資產、取消5%門檻。"
      },
      "summary": {
        "sc": "2026年6月12日刊宪、6月24日首读的《2026年税务（修订）（关于基金、家族投资控权工具及附带权益的优惠税制）条例草案》，于7月8日在立法会进入审议阶段。核心修订：扩大「基金」定义涵盖单一投资者基金；新增数字资产、海外不动产、贵金属为合资格投资；取消附带交易5%门槛；放宽FSPE免税条件。追溯适用于2025/26课税年度。",
        "tc": "2026年6月12日刊憲、6月24日首讀的《2026年稅務（修訂）（關於基金、家族投資控權工具及附帶權益的優惠稅制）條例草案》，於7月8日在立法會進入審議階段。核心修訂：擴大「基金」定義涵蓋單一投資者基金；新增數字資產、海外不動產、貴金屬為合資格投資；取消附帶交易5%門檻；放寬FSPE免稅條件。追溯適用於2025/26課稅年度。"
      },
      "why": {
        "sc": "这是港府巩固全球跨境财富管理中心地位的关键立法——首次将比特币等数字资产纳入家办免税投资范围，大幅降低合规门槛，直接提升香港对全球家族办公室的吸引力。",
        "tc": "這是港府鞏固全球跨境財富管理中心地位的關鍵立法——首次將比特幣等數字資產納入家辦免稅投資範圍，大幅降低合規門檻，直接提升香港對全球家族辦公室的吸引力。"
      },
      "actions": {
        "front": {
          "sc": "了解免稅投资范围扩大的具体资产类别，向高净值客户介绍香港家办架构新优势。",
          "tc": "了解免稅投資範圍擴大的具體資產類別，向高淨值客戶介紹香港家辦架構新優勢。"
        },
        "midback": {},
        "lead": {
          "sc": "评估法案通过后对产品策略的影响——数字资产配置需求可能带来新的保险+信托联动机会。",
          "tc": "評估法案通過後對產品策略的影響——數字資產配置需求可能帶來新的保險+信託聯動機會。"
        },
        "cross": {
          "sc": "数字资产纳入免税范围意味着家办可以为持有加密货币的家族提供合规税务架构。",
          "tc": "數字資產納入免稅範圍意味著家辦可以為持有加密貨幣的家族提供合規稅務架構。"
        }
      },
      "rolesImpact": {
        "front": 2,
        "midback": 1,
        "lead": 3,
        "cross": 4
      },
      "source": {
        "sc": "财经事务及库务局 / 税务局新闻公报",
        "lang": "zh"
      },
      "boards": [
        "family"
      ],
      "themes": [
        "tax-incentive",
        "fo-policy"
      ],
      "tags": {
        "sc": [
          "家办税惠",
          "数字资产",
          "条例草案",
          "基金免税"
        ],
        "tc": [
          "家辦稅惠",
          "數字資產",
          "條例草案",
          "基金免稅"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-08T18:00:00+08:00",
      "originalUrl": "https://www.ird.gov.hk/chi/ppr/archives/26061202.htm"
    },
    {
      "id": "fstb-20260708-captive",
      "clusterCount": 1,
      "score": 78,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T11:00:00+08:00",
      "contentRole": {
        "sc": "本站导读（非原文）",
        "tc": "本站導讀（非原文）"
      },
      "title": {
        "sc": "财库局欢迎保监局批准两间新专属自保保险公司。",
        "tc": "財庫局歡迎保監局批准兩間新專屬自保保險公司。"
      },
      "summary": {
        "sc": "财经事务及库务局2026年7月8日欢迎保监局批准香港上海大酒店有限公司及顺丰控股设立专属自保保险公司，巩固香港作为自保保险枢纽的地位。",
        "tc": "財庫局7月8日歡迎保監局批准兩家新自保公司"
      },
      "why": {
        "sc": "自保牌照增加，也是香港保险市场深度持续提升，企业风险管理能力增强。",
        "tc": "自保牌照增加，也是市場深度提升。"
      },
      "actions": {
        "front": {
          "sc": "一般知识储备",
          "tc": "知識儲備"
        },
        "midback": {
          "sc": "更新香港授权保险人最新名单",
          "tc": "更新授權保險人名單"
        },
        "lead": {
          "sc": "关注自保保险对再保险市场的连带影响",
          "tc": "關注自保保險對再保市場的影響"
        },
        "cross": {
          "sc": "顺丰案例可作为跨境企业风险管理的参考标杆",
          "tc": "順豐案例可作參考"
        }
      },
      "source": {
        "sc": "财库局新闻稿",
        "tc": "財庫局新聞稿",
        "lang": "zh"
      },
      "boards": [
        "regulatory",
        "firm"
      ],
      "tags": {
        "sc": [
          "自保保险",
          "财库局",
          "顺丰"
        ],
        "tc": [
          "自保保險",
          "財庫局",
          "順豐"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-08T14:00:00+08:00",
      "originalUrl": "https://www.fstb.gov.hk/fsb/tc/business/policy_highlights/insurance-industry.html",
      "sourceKey": "govhk",
      "sourceTier": "official",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20260708-captive",
      "title": {
        "sc": "两间新专属自保公司获授权，巩固风险管理中心策略（2026-07-08）。",
        "tc": "兩間新專屬自保公司獲授權，鞏固風險管理中心策略（2026-07-08）。"
      },
      "summary": {
        "sc": "保监局2026年7月8日公布批出新授权予两间专属自保保险公司（含本地酒店品牌相关自保及深圳物流背景自保），印证香港发展专属自保与企业风险管理中心策略。",
        "tc": "保監局2026年7月8日公布批出新授權予兩間專屬自保保險公司（含本地酒店品牌相關自保及深圳物流背景自保），印證香港發展專屬自保與企業風險管理中心策略。"
      },
      "why": {
        "sc": "展示香港不止零售分红，还有企业风险与自保生态。",
        "tc": "展示香港不止零售分紅，還有企業風險與自保生態。"
      },
      "actions": {
        "front": {
          "sc": "对公客户可作市场定位谈资，非个人产品推介。",
          "tc": "對公客戶可作市場定位談資，非個人產品推介。"
        },
        "midback": {
          "sc": "企业险/自保知识库补强。｜关注自保相关合规边界。",
          "tc": "企業險/自保知識庫補強。｜關注自保相關合規邊界。"
        },
        "lead": {
          "sc": "战略叙事对齐风险管理中心。",
          "tc": "戰略敘事對齊風險管理中心。"
        },
        "cross": {
          "sc": "内地企业出海风控需求线索。",
          "tc": "內地企業出海風控需求線索。"
        }
      },
      "source": {
        "sc": "保监局新闻稿 2026-07-08",
        "tc": "保監局新聞稿 2026-07-08"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "专属自保",
          "企业风险"
        ],
        "tc": [
          "專屬自保",
          "企業風險"
        ]
      },
      "themes": [
        "firm",
        "macro",
        "reg"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 2,
        "lead": 3,
        "cross": 3
      },
      "publishedAt": "2026-07-08T12:00:00+08:00",
      "score": 81,
      "verifyStatus": "verified",
      "featured": false,
      "originalUrl": "https://www.ia.org.hk/sc/infocenter/press_releases/20260708.html",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "insurer",
        "market",
        "reg"
      ],
      "contentKind": "press"
    },
    {
      "id": "swissre-202607-wis",
      "clusterCount": 1,
      "score": 92,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": false,
      "ingestedAt": "2026-07-28T19:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "Swiss Re sigma报告：2026全球保险成为碎片化世界中的减震器。",
        "tc": "Swiss Re sigma報告：2026全球保險成為碎片化世界中的減震器。"
      },
      "summary": {
        "sc": "Swiss Re Institute 2026年7月发布sigma报告「World Insurance in 2026」。全球保费增长放缓至1.3%(实物)，低于2025年的3.9%。地缘碎片化+AI基建投资创造新型风险池。保险从风险转移升级为「经济稳定器」。[EN原文]",
        "tc": "Swiss Re:全球保費增長放緩至1.3%，保險成經濟穩定器"
      },
      "why": {
        "sc": "全球再保险领袖的年度定调，也是行业风向标。",
        "tc": "全球再保領袖年度定調，也是行業風向標。"
      },
      "actions": {
        "front": {
          "sc": "客户沟通中引用瑞士再保的行业趋势判断",
          "tc": "引用行業趨勢判斷"
        },
        "midback": {
          "sc": "归档年度sigma核心结论",
          "tc": "歸檔sigma結論"
        },
        "lead": {
          "sc": "碎片化+AI基建=新风险新机遇",
          "tc": "新風險新機遇"
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "Swiss Re Institute",
        "tc": "Swiss Re Institute",
        "lang": "en"
      },
      "boards": [
        "intl",
        "regulatory"
      ],
      "tags": {
        "sc": [
          "Swiss Re",
          "sigma",
          "全球保险",
          "2026"
        ],
        "tc": [
          "Swiss Re",
          "sigma",
          "全球保險",
          "2026"
        ]
      },
      "contentKind": "report",
      "publishedAt": "2026-07-08T10:00:00+08:00",
      "originalUrl": "https://www.swissre.com/institute/research/sigma-research/sigma-2026-07-world-insurance.html",
      "sourceKey": "swissre",
      "sourceTier": "research",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "nfra-shanghai-reins-20260707",
      "clusterCount": 1,
      "score": 82,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "nfra",
      "title": {
        "sc": "金融监管总局×上海市政府：加快上海国际再保险中心建设",
        "tc": "金融監管總局×上海市政府：加快上海國際再保險中心建設"
      },
      "summary": {
        "sc": "2026 年 7 月 7 日，国家金融监管总局与上海市政府联合发布《关于加快上海国际再保险中心建设的若干措施》。目标是让上海成为亚太再保险交易中心——与香港争夺区域再保险枢纽地位。",
        "tc": "2026 年 7 月 7 日，國家金融監管總局與上海市政府聯合發布《關於加快上海國際再保險中心建設的若干措施》。目標是讓上海成為亞太再保險交易中心——與香港爭奪區域再保險樞紐地位。"
      },
      "why": {
        "sc": "上海在抢香港的再保险生意。这不是竞争压力，而是互补机会——两地各有优势：上海的直保市场规模，香港的国际法律和资本环境。IFA 需要知道两边在发生什么。",
        "tc": "上海在搶香港的再保險生意。這不是競爭壓力，而是互補機會——兩地各有優勢：上海的直保市場規模，香港的國際法律和資本環境。IFA 需要知道兩邊在發生什麼。"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {
          "sc": "上海vs香港再保险竞争=了解两地差异化定位",
          "tc": "上海vs香港再保險競爭=了解兩地差異化定位"
        },
        "cross": {
          "sc": "再保险中心竞争=跨境保险生态的另一个维度",
          "tc": "再保險中心競爭=跨境保險生態的另一個維度"
        }
      },
      "rolesImpact": {
        "front": 1,
        "midback": 2,
        "lead": 3,
        "cross": 4
      },
      "source": {
        "sc": "国家金融监管总局 · 2026年7月7日",
        "lang": "sc"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "reg",
        "offshore"
      ],
      "tags": {
        "sc": [
          "再保险",
          "上海",
          "金融监管总局"
        ],
        "tc": [
          "再保險",
          "上海",
          "金融監管總局"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2026-07-07T10:00:00+08:00",
      "originalUrl": "https://www.nfra.gov.cn/cn/view/pages/ItemDetail.html?docId=1263701&itemId=928"
    },
    {
      "id": "nfra-shanghai-reins-center-jul07",
      "clusterCount": 1,
      "score": 84,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "nfra:shanghai-reins-20260707",
      "title": {
        "sc": "金融监管总局发布加快上海国际再保险中心建设措施",
        "tc": "金融監管總局發布加快上海國際再保險中心建設措施"
      },
      "summary": {
        "sc": "2026年7月7日，国家金融监督管理总局联合上海市政府印发《加快上海国际再保险中心建设的若干措施》，提出包括税收优惠、跨境再保险便利化、机构集聚等一揽子政策。此举将深化上海与香港再保险市场的竞合关系，影响亚洲再保险版图。"
      },
      "why": {
        "sc": "上海再保中心=香港再保险竞争优势与分流效应需关注",
        "tc": "上海再保中心=香港再保險競爭需關注"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 2,
        "cross": 1
      },
      "source": {
        "sc": "NFRA",
        "tc": "國家金融監管總局",
        "lang": "zh"
      },
      "boards": [
        "reg"
      ],
      "themes": [
        "reinsurance",
        "greater-bay"
      ],
      "tags": {
        "sc": [
          "NFRA",
          "上海",
          "再保险",
          "政策"
        ],
        "tc": [
          "NFRA",
          "上海",
          "再保險",
          "政策"
        ]
      },
      "contentKind": "circular",
      "publishedAt": "2026-07-07T09:00:00+08:00",
      "originalUrl": "https://www.nfra.gov.cn/cn/view/pages/ItemDetail.html?docId=1263701&itemId=928",
      "ingestedAt": "2026-07-30T18:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "investhk-fo-2p0-20260706",
      "clusterCount": 1,
      "score": 90,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "investhk",
      "title": {
        "sc": "投推署方展光专访：香港家办突破3,384家，家办2.0构筑全球财富新枢纽。",
        "tc": "投推署方展光專訪：香港家辦突破3,384家，家辦2.0構築全球財富新樞紐。"
      },
      "summary": {
        "sc": "2026年7月6日，香港投资推广署家族办公室环球总裁方展光接受《经济参考报》专访，披露最新数据：香港单一家族办公室已达3,384家，两年增幅25%，管理资产规模35.1万亿港元。香港已超越瑞士成为全球最大跨境财富管理中心。26.7万名专业人才服务家办生态，相当于每家办约80名专家环绕。方展光指港股2,700+上市公司远超新加坡的600+，产业承载力优势显著。",
        "tc": "2026年7月6日，香港投資推廣署家族辦公室環球總裁方展光接受《經濟參考報》專訪，披露最新數據：香港單一家族辦公室已達3,384家，兩年增幅25%，管理資產規模35.1萬億港元。香港已超越瑞士成為全球最大跨境財富管理中心。26.7萬名專業人才服務家辦生態，相當於每家辦約80名專家環繞。"
      },
      "why": {
        "sc": "官方最新家办数据与战略解读——3,384家、35.1万亿、家办2.0战略，是评估香港家办行业体量与趋势的基准坐标；与瑞士/新加坡的差异化对比直接回答客户「为什么选香港」。",
        "tc": "官方最新家辦數據與戰略解讀——3,384家、35.1萬億、家辦2.0戰略，是評估香港家辦行業體量與趨勢的基準坐標；與瑞士/新加坡的差異化對比直接回答客戶「為什麼選香港」。"
      },
      "actions": {
        "front": {
          "sc": "背下「3,384家/35.1万亿」两个数字，客户问香港家办实力时直接引用。",
          "tc": "背下「3,384家/35.1萬億」兩個數字，客戶問香港家辦實力時直接引用。"
        },
        "midback": {},
        "lead": {
          "sc": "家办2.0战略强调北部都会区联动大湾区科创——关注科创企业家设立家办的趋势。",
          "tc": "家辦2.0戰略強調北部都會區聯動大灣區科創——關注科創企業家設立家辦的趨勢。"
        },
        "cross": {
          "sc": "港股2,700+ vs 新加坡600+：资本市场的深度是客户选择家办注册地的重要考量。",
          "tc": "港股2,700+ vs 新加坡600+：資本市場的深度是客戶選擇家辦註冊地的重要考量。"
        }
      },
      "rolesImpact": {
        "front": 3,
        "midback": 1,
        "lead": 4,
        "cross": 4
      },
      "source": {
        "sc": "经济参考报 / 香港投资推广署",
        "lang": "zh"
      },
      "boards": [
        "family",
        "market"
      ],
      "themes": [
        "fo-ecosystem",
        "global-wealth"
      ],
      "tags": {
        "sc": [
          "家办2.0",
          "方展光",
          "投推署",
          "跨境财富"
        ],
        "tc": [
          "家辦2.0",
          "方展光",
          "投推署",
          "跨境財富"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2026-07-06T08:00:00+08:00",
      "originalUrl": "http://www.jjckb.cn/20260706/a9804c5a6d034e50a5b43cfda9b003de/c.html"
    },
    {
      "id": "pcpd-ai-sandbox-jul06",
      "clusterCount": 1,
      "score": 85,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "pcpd-dpo",
      "title": {
        "sc": "香港私隐公署与数字办联合推出「保障个人资料AI沙盒」",
        "tc": "香港私隱公署與數字辦聯合推出「保障個人資料AI沙盒」"
      },
      "summary": {
        "sc": "2026年7月6日，个人资料私隐专员公署(PCPD)与数字政策办公室(DPO)联合推出「保障个人资料AI沙盒」，旨在积极对接国家十五五规划「发展与安全并重」方针，为AI技术在港应用提供个人资料保障测试环境。保险业作为高度依赖个人数据的行业，此沙盒为AI核保、理赔等场景提供合规路径。[EN原文]",
        "tc": "私隱公署與數字辦聯合推出「保障個人資料AI沙盒」，為AI在保險核保理賠等場景提供個人資料保障合規測試環境。[EN原文]"
      },
      "why": {
        "sc": "AI+隐私合规=保险科技落地的关键门槛，沙盒提供可控测试环境",
        "tc": "AI+私隱合規=保險科技落地的關鍵門檻，沙盒提供可控測試環境"
      },
      "actions": {
        "front": {},
        "midback": {
          "sc": "关注沙盒具体标准，评估AI核保理赔工具的合规路径",
          "tc": "關注沙盒具體標準，評估AI核保理賠工具的合規路徑"
        },
        "lead": {
          "sc": "AI隐私合规需纳入保险科技投资决策框架",
          "tc": "AI私隱合規需納入保險科技投資決策框架"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 1,
        "midback": 3,
        "lead": 3,
        "cross": 0
      },
      "source": {
        "sc": "香港政府资讯中心",
        "lang": "zh+en"
      },
      "boards": [
        "reg",
        "tech"
      ],
      "themes": [
        "AI",
        "privacy",
        "sandbox"
      ],
      "tags": {
        "sc": [
          "AI沙盒",
          "个人资料保障",
          "PCPD",
          "DPO",
          "保险科技"
        ],
        "tc": [
          "AI沙盒",
          "個人資料保障",
          "PCPD",
          "DPO",
          "保險科技"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2026-07-06T00:00:00+08:00",
      "originalUrl": "https://www.info.gov.hk/gia/general/202607/06/P2026070300679.htm",
      "ingestedAt": "2026-08-01T12:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "featured": false,
      "evergreen": false
    },
    {
      "id": "ia-20260703-rfyc",
      "title": {
        "sc": "指定无风险收益率曲线（截至2026-06-30）发布（2026-07-03）。",
        "tc": "指定無風險收益率曲線（截至2026-06-30）發布（2026-07-03）。"
      },
      "summary": {
        "sc": "保监局于2026年7月3日更新指定无风险收益率曲线（截至2026年6月30日）Excel，供风险为本资本制度下估值与资本计算使用。",
        "tc": "保監局於2026年7月3日更新指定無風險收益率曲線（截至2026年6月30日）Excel，供風險為本資本制度下估值與資本計算使用。"
      },
      "why": {
        "sc": "精算/产品/保司资本侧基础数据；专业中台可跟踪。",
        "tc": "精算/產品/保司資本側基礎數據；專業中台可跟踪。"
      },
      "actions": {
        "front": {
          "sc": "无需对客展开技术细节。",
          "tc": "無需對客展開技術細節。"
        },
        "midback": {
          "sc": "产品精算同事存档。｜无直接中介动作。",
          "tc": "產品精算同事存檔。｜無直接中介動作。"
        },
        "lead": {
          "sc": "知晓更新节奏即可。",
          "tc": "知曉更新節奏即可。"
        },
        "cross": {
          "sc": "无直接动作。",
          "tc": "無直接動作。"
        }
      },
      "source": {
        "sc": "保监局 RBC 相关文件 2026-07-03",
        "tc": "保監局 RBC 相關文件 2026-07-03"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "无风险收益率",
          "RBC"
        ],
        "tc": [
          "無風險收益率",
          "RBC"
        ]
      },
      "themes": [
        "reg",
        "firm",
        "par"
      ],
      "rolesImpact": {
        "front": 0,
        "midback": 2,
        "lead": 1,
        "cross": 0
      },
      "publishedAt": "2026-07-03T12:00:00+08:00",
      "score": 76,
      "featured": false,
      "originalUrl": "https://www.ia.org.hk/en/supervision/reg_insurers_lloyd/an_overview_of_the_risk_based_capital_regime.html",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T02:07:48+08:00",
      "evergreen": false,
      "clusterCount": 1,
      "verifyStatus": "verified",
      "boards": [
        "insurer",
        "product",
        "reg"
      ],
      "contentKind": "other"
    },
    {
      "id": "rga-2026-hk-market",
      "clusterCount": 1,
      "score": 86,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T19:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "RGA分析：2026年香港保险市场机遇与挑战——跨境需求+监管转型+AI。",
        "tc": "RGA分析：2026年香港保險市場機遇與挑戰——跨境需求+監管轉型+AI。"
      },
      "summary": {
        "sc": "RGA 2026年分析文章指出香港新造保费2024年+21%。三大驱动力：内地访客对分红储蓄+危疾需求、HKRBC全面实施推动资本优化、AI核保与数字工具提升效率。[EN原文]",
        "tc": "RGA:香港新造保費+21%，三大驅動力"
      },
      "why": {
        "sc": "专业再保险人的香港市场分析，也是客观第三方视角。",
        "tc": "專業再保人客觀分析。"
      },
      "actions": {
        "front": {
          "sc": "了解HKRBC对产品供给的影响",
          "tc": "了解HKRBC影響"
        },
        "midback": {
          "sc": "更新市场分析数据",
          "tc": "更新市場數據"
        },
        "lead": {
          "sc": "跨境+AI+监管三重驱动的战略判断",
          "tc": "三重驅動戰略判斷"
        },
        "cross": {
          "sc": "内地访客需求=跨境业务核心驱动",
          "tc": "內地訪客=跨境核心"
        }
      },
      "source": {
        "sc": "RGA/Asia Insurance Review",
        "tc": "RGA/Asia Insurance Review",
        "lang": "en"
      },
      "boards": [
        "intl",
        "macro"
      ],
      "tags": {
        "sc": [
          "RGA",
          "香港",
          "跨境",
          "HKRBC",
          "2026"
        ],
        "tc": [
          "RGA",
          "香港",
          "跨境",
          "HKRBC",
          "2026"
        ]
      },
      "contentKind": "report",
      "publishedAt": "2026-07-01T10:00:00+08:00",
      "originalUrl": "https://www.rgare.com/knowledge-center/article/hong-kong-insurance-market--navigating-opportunities-and-challenges-in-2026",
      "sourceKey": "rga:hk-market-2026",
      "sourceTier": "media",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "hkex-ipo-pipeline-2026h1",
      "clusterCount": 1,
      "score": 74,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "港交所 HKEX",
      "title": {
        "sc": "港交所 2026 H1 IPO 回顾：内地企业赴港上市持续活跃",
        "tc": "港交所 2026 H1 IPO 回顧：內地企業赴港上市持續活躍"
      },
      "summary": {
        "sc": "2026 年上半年港交所 IPO 市场保持活跃，多只内地科技和消费企业完成上市。香港继续保持全球前三的 IPO 集资中心地位。资本市场的活跃直接带动了高净值财富的创造和保值需求，与家办生态形成正反馈。",
        "tc": "2026 年上半年港交所 IPO 市場保持活躍，多隻內地科技和消費企業完成上市。香港繼續保持全球前三的 IPO 集資中心地位。資本市場的活躍直接帶動了高淨值財富的創造和保值需求，與家辦生態形成正反饋。"
      },
      "why": {
        "sc": "IPO=造富机器。每一家新上市公司的创始人和高管都是潜在的家办客户。H1 活跃的 IPO 意味着下半年将有更多新财富进入财富管理市场。",
        "tc": "IPO=造富機器。每一家新上市公司的創始人和高管都是潛在的家辦客戶。H1 活躍的 IPO 意味著下半年將有更多新財富進入財富管理市場。"
      },
      "actions": {
        "front": {
          "sc": "IPO造富后的财富管理需求是保险/信托的黄金窗口",
          "tc": "IPO造富後的財富管理需求是保險/信託的黃金窗口"
        },
        "midback": {},
        "lead": {
          "sc": "资本市场活跃=财富管理市场扩容",
          "tc": "資本市場活躍=財富管理市場擴容"
        },
        "cross": {
          "sc": "上市公司的跨境架构需求天然适配家办服务",
          "tc": "上市公司的跨境架構需求天然適配家辦服務"
        }
      },
      "rolesImpact": {
        "front": 3,
        "midback": 1,
        "lead": 4,
        "cross": 4
      },
      "source": {
        "sc": "HKEX / 媒体综合",
        "lang": "zh"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "capital-market",
        "offshore"
      ],
      "tags": {
        "sc": [
          "IPO",
          "资本市场",
          "港交所"
        ],
        "tc": [
          "IPO",
          "資本市場",
          "港交所"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-01T10:00:00+08:00",
      "originalUrl": "https://www.hkex.com.hk/News/News-Release"
    },
    {
      "id": "ia-crossref-20260701",
      "clusterCount": 2,
      "score": 93,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": true,
      "ingestedAt": "2026-07-28T11:00:00+08:00",
      "contentRole": {
        "sc": "本站导读（非原文）",
        "tc": "本站導讀（非原文）"
      },
      "title": {
        "sc": "银行与保险跨行业背景查核安排：2026年7月1日起分阶段实施。",
        "tc": "銀行與保險跨行業背景查核安排：2026年7月1日起分階段實施。"
      },
      "summary": {
        "sc": "金管局与保监局联合推出跨行业背景查核/操守参考安排，2026年7月1日起生效。首阶段覆盖银行及保险机构的寿险从业员，准员工过去七年操守记录可在两行业间共享，覆盖约11万人。",
        "tc": "金管局與保監局聯合推出跨行業背景查核安排7月生效"
      },
      "why": {
        "sc": "跳槽成本剧增、行业透明度升级，合规瑕疵在银行与保险间一票否决。",
        "tc": "跳槽成本劇增、行業透明度升級。"
      },
      "actions": {
        "front": {
          "sc": "跳槽前主动向新雇主披露操守记录",
          "tc": "跳槽前主動披露操守記錄"
        },
        "midback": {
          "sc": "招聘流程新增背景查核环节，对接查核机制",
          "tc": "招聘流程新增背景查核"
        },
        "lead": {
          "sc": "建立团队操守档案，提前梳理潜在风险",
          "tc": "建立團隊操守檔案"
        },
        "cross": {
          "sc": "跨境业务人员需同步满足两地合规查核",
          "tc": "跨境人員需滿足兩地合規"
        }
      },
      "source": {
        "sc": "HKMA+IA 联合通函",
        "tc": "HKMA+IA 聯合通函",
        "lang": "zh"
      },
      "boards": [
        "regulatory",
        "compliance",
        "channel"
      ],
      "tags": {
        "sc": [
          "背景查核",
          "跨行业",
          "金管局",
          "2026"
        ],
        "tc": [
          "背景查核",
          "跨行業",
          "金管局",
          "2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-07-01T09:00:00+08:00",
      "originalUrl": "https://xhcins.com/posts/hongkong-insurance-intermediary-reference-checking-2026-07/",
      "sourceKey": "ia:crossref-20260701",
      "sourceTier": "media",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20260630-swissre-sigma",
      "clusterCount": 1,
      "score": 80,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "title": {
        "sc": "瑞再研究院sigma报告：全球保险在碎片化世界中扮演「减震器」，AI投资颠覆行业格局。",
        "tc": "瑞再研究院sigma報告：全球保險在碎片化世界中扮演「減震器」，AI投資顛覆行業格局。"
      },
      "summary": {
        "sc": "2026年6月30日，瑞士再保险研究院发布sigma 2/2026报告《World Insurance in 2026: Shock Absorbers in a Fragmenting World》。预测2026年全球保费实际增长1.3%（从2025年3.9%放缓），寿险增长2.3%强劲，非寿险0.6%。AI投资将达7,500亿美元，推动保险需求向财产、工程、网络和业务中断险延展。",
        "tc": "2026年6月30日，瑞士再保險研究院發布sigma 2/2026報告《World Insurance in 2026: Shock Absorbers in a Fragmenting World》。預測2026年全球保費實際增長1.3%（從2025年3.9%放緩），壽險增長2.3%強勁，非壽險0.6%。AI投資將達7,500億美元，推動保險需求向財產、工程、網絡和業務中斷險延展。"
      },
      "why": {
        "sc": "全球最权威再保险研究机构明确指出AI基建带来的新风险池，保险业面临结构性增长机遇。",
        "tc": "全球最權威再保險研究機構明確指出AI基建帶來的新風險池，保險業面臨結構性增長機遇。"
      },
      "actions": {
        "front": {
          "sc": "对客叙事：全球顶级机构认为保险是碎片化世界中的「减震器」。",
          "tc": "對客敘事：全球頂級機構認為保險是碎片化世界中的「減震器」。"
        },
        "midback": {
          "sc": "将瑞再增长预测纳入公司年度市场分析报告。",
          "tc": "將瑞再增長預測納入公司年度市場分析報告。"
        },
        "lead": {
          "sc": "战略层面：AI基建保险需求是未来3-5年的蓝海市场。",
          "tc": "戰略層面：AI基建保險需求是未來3-5年的藍海市場。"
        },
        "cross": {
          "sc": "地缘碎片化趋势意味着离岸保险需求将持续增长。",
          "tc": "地緣碎片化趨勢意味著離岸保險需求將持續增長。"
        }
      },
      "source": {
        "sc": "瑞再研究院 · sigma 2/2026 2026-06-30 [EN原文]",
        "tc": "瑞再研究院 · sigma 2/2026 2026-06-30 [EN原文]",
        "lang": "zh"
      },
      "sourceTier": "research",
      "tags": {
        "sc": [
          "瑞再",
          "sigma",
          "AI投资"
        ],
        "tc": [
          "瑞再",
          "sigma",
          "AI投資"
        ]
      },
      "themes": [
        "macro",
        "market",
        "tech"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 1,
        "lead": 2,
        "cross": 2
      },
      "publishedAt": "2026-06-30T14:00:00+08:00",
      "originalUrl": "https://www.swissre.com/institute/research/sigma-research/sigma-2026-07-world-insurance.html",
      "sourceKey": "swissre",
      "boards": [
        "market",
        "tech"
      ],
      "contentKind": "research"
    },
    {
      "id": "ia-20260630-allianz-report",
      "clusterCount": 1,
      "score": 74,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "title": {
        "sc": "安联全球保险报告2026：碎片化世界中的保险未来 — 亚洲仍是增长引擎。",
        "tc": "安聯全球保險報告2026：碎片化世界中的保險未來 — 亞洲仍是增長引擎。"
      },
      "summary": {
        "sc": "2026年6月30日，安联研究发布《全球保险报告2026：碎片化世界中的保险未来》。报告预测2026-2036年香港寿险市场年均增长5.2%，产险增长4.1%。亚洲（除中日）仍是全球保险增长引擎，受益于人口老龄化、高储蓄率和养老金体系不足的结构性推动力。",
        "tc": "2026年6月30日，安聯研究發布《全球保險報告2026：碎片化世界中的保險未來》。報告預測2026-2036年香港壽險市場年均增長5.2%，產險增長4.1%。亞洲（除中日）仍是全球保險增長引擎，受益於人口老齡化、高儲蓄率和養老金體系不足的結構性推動力。"
      },
      "why": {
        "sc": "安联对香港保险的十年增长预测为中介行业提供了坚实的市场信心论据。",
        "tc": "安聯對香港保險的十年增長預測為中介行業提供了堅實的市場信心論據。"
      },
      "actions": {
        "front": {
          "sc": "对客可用安联增长预测说明保险行业的长期配置价值。",
          "tc": "對客可用安聯增長預測說明保險行業的長期配置價值。"
        },
        "midback": {
          "sc": "将市场增长预测纳入年度业务规划与目标设定。",
          "tc": "將市場增長預測納入年度業務規劃與目標設定。"
        },
        "lead": {
          "sc": "行业年均5.2%增长意味着人才和渠道扩张空间巨大。",
          "tc": "行業年均5.2%增長意味著人才和渠道擴張空間巨大。"
        },
        "cross": {
          "sc": "亚洲保险渗透率仍低，跨境需求将持续增长。",
          "tc": "亞洲保險滲透率仍低，跨境需求將持續增長。"
        }
      },
      "source": {
        "sc": "安联研究 · 全球保险报告 2026-06-30 [EN原文]",
        "tc": "安联研究 · 全球保险报告 2026-06-30 [EN原文]",
        "lang": "zh"
      },
      "sourceTier": "research",
      "tags": {
        "sc": [
          "安联",
          "市场预测",
          "亚洲增长"
        ],
        "tc": [
          "安聯",
          "市場預測",
          "亞洲增長"
        ]
      },
      "themes": [
        "macro",
        "market"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 1,
        "lead": 2,
        "cross": 2
      },
      "publishedAt": "2026-06-30T10:00:00+08:00",
      "originalUrl": "https://www.allianz.com/content/dam/onemarketing/azcom/Allianz_com/economic-research/publications/specials/en/2026/may/28-05-2026-Global-Insurance-report-AZ.pdf",
      "sourceKey": "allianz",
      "boards": [
        "market"
      ],
      "contentKind": "research"
    },
    {
      "id": "hk-property-cires-2026",
      "clusterCount": 1,
      "score": 70,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "govhk",
      "title": {
        "sc": "CIES 推动香港豪宅市场：3,000 万以上住宅成交上升",
        "tc": "CIES 推動香港豪宅市場：3,000 萬以上住宅成交上升"
      },
      "summary": {
        "sc": "新资本投资者入境计划（CIES）允许将最多 1,000 万港元计入住宅房地产投资，带动香港 3,000 万港元以上豪宅成交量上升。同时，跨境家庭的置业需求和国际学校周边的住宅需求持续增长。地产投资是家办资产配置的重要一环。",
        "tc": "新資本投資者入境計劃（CIES）允許將最多 1,000 萬港元計入住宅房地產投資，帶動香港 3,000 萬港元以上豪宅成交量上升。同時，跨境家庭的置業需求和國際學校周邊的住宅需求持續增長。地產投資是家辦資產配置的重要一環。"
      },
      "why": {
        "sc": "CIES 的房产投资额度虽然只有 1,000 万，但每一个 CIES 家庭的实际购房预算远超此数。豪宅市场是家办客户生活方式的锚点，也是跨境资产配置最「可见」的一环。",
        "tc": "CIES 的房產投資額度雖然只有 1,000 萬，但每一個 CIES 家庭的實際購房預算遠超此數。豪宅市場是家辦客戶生活方式的錨點，也是跨境資產配置最「可見」的一環。"
      },
      "actions": {
        "front": {
          "sc": "房产+保险是家办客户最基本的双线配置",
          "tc": "房產+保險是家辦客戶最基本的雙線配置"
        },
        "midback": {},
        "lead": {
          "sc": "地产投资是家办客户最直观的财富管理需求",
          "tc": "地產投資是家辦客戶最直觀的財富管理需求"
        },
        "cross": {
          "sc": "跨境房产是身份规划的自然延伸",
          "tc": "跨境房產是身份規劃的自然延伸"
        }
      },
      "rolesImpact": {
        "front": 3,
        "midback": 1,
        "lead": 2,
        "cross": 4
      },
      "source": {
        "sc": "综合报道",
        "lang": "zh"
      },
      "boards": [
        "family"
      ],
      "themes": [
        "property",
        "offshore"
      ],
      "tags": {
        "sc": [
          "地产",
          "CIES",
          "豪宅"
        ],
        "tc": [
          "地產",
          "CIES",
          "豪宅"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-06-30T10:00:00+08:00",
      "originalUrl": "https://www.newcies.gov.hk/en/new-measures/"
    },
    {
      "id": "ia-20260629-sunlife-notes",
      "clusterCount": 1,
      "score": 65,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "title": {
        "sc": "永明金融宣布10亿美元有限追索资本票据利率重置。",
        "tc": "永明金融宣布10億美元有限追索資本票據利率重置。"
      },
      "summary": {
        "sc": "2026年6月29日，永明金融（Sun Life Financial Inc.）宣布其10亿美元本金、票息3.60%的Series 2021-1有限追索资本票据利率重置。永明亚洲业务持续强劲，Q1亚洲区基本净收入同比增长17%至2.16亿加元，香港市场在全部渠道均录得增长。",
        "tc": "2026年6月29日，永明金融（Sun Life Financial Inc.）宣布其10億美元本金、票息3.60%的Series 2021-1有限追索資本票據利率重置。永明亞洲業務持續強勁，Q1亞洲區基本淨收入同比增長17%至2.16億加元，香港市場在全部渠道均錄得增長。"
      },
      "why": {
        "sc": "永明资本运作稳健，亚洲业务增长强劲，为合作中介提供正向背书。",
        "tc": "永明資本運作穩健，亞洲業務增長強勁，為合作中介提供正向背書。"
      },
      "actions": {
        "front": {
          "sc": "对客可用永明财务实力和亚洲增长数据增强信心。",
          "tc": "對客可用永明財務實力和亞洲增長數據增強信心。"
        },
        "midback": {
          "sc": "将永明最新财务数据纳入保司评估体系。",
          "tc": "將永明最新財務數據納入保司評估體系。"
        },
        "lead": {
          "sc": "永明亚洲增长数据可作为团队业绩对标的行业参照。",
          "tc": "永明亞洲增長數據可作為團隊業績對標的行業參照。"
        },
        "cross": {
          "sc": "永明的多市场布局为跨境客户提供更多选择。",
          "tc": "永明的多市場布局為跨境客戶提供更多選擇。"
        }
      },
      "source": {
        "sc": "永明金融 · 公告 2026-06-29 [EN原文]",
        "tc": "永明金融 · 公告 2026-06-29 [EN原文]",
        "lang": "zh"
      },
      "sourceTier": "insurer",
      "tags": {
        "sc": [
          "永明",
          "资本票据",
          "亚洲增长"
        ],
        "tc": [
          "永明",
          "資本票據",
          "亞洲增長"
        ]
      },
      "themes": [
        "firm",
        "market"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 1,
        "lead": 2,
        "cross": 1
      },
      "publishedAt": "2026-06-29T16:00:00+08:00",
      "originalUrl": "https://www.sunlife.com/en/newsroom/news-releases/announcement/sun-life-announces-interest-rate-reset-on-limited-recourse-capital-notes-series/124106/",
      "sourceKey": "sunlife",
      "boards": [
        "insurer",
        "market"
      ],
      "contentKind": "other"
    },
    {
      "id": "ia-20260629-hkma-bulletin",
      "clusterCount": 1,
      "score": 71,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "title": {
        "sc": "金管局发布2026年第二期季报：涵盖银保监管协作与运营韧性。",
        "tc": "金管局發布2026年第二期季報：涵蓋銀保監管協作與運營韌性。"
      },
      "summary": {
        "sc": "2026年6月29日，香港金管局发布2026年第2期季报，涵盖银保监管协作进展、银行运营韧性框架以及跨境金融业务合规指引。报告强调了金管局与保监局在银保渠道报酬结构方面的协调监管成果。",
        "tc": "2026年6月29日，香港金管局發布2026年第2期季報，涵蓋銀保監管協作進展、銀行運營韌性框架以及跨境金融業務合規指引。報告強調了金管局與保監局在銀保渠道報酬結構方面的協調監管成果。"
      },
      "why": {
        "sc": "金管局与保监局监管协同走向制度化；银保渠道规则更清晰。",
        "tc": "金管局與保監局監管協同走向制度化；銀保渠道規則更清晰。"
      },
      "actions": {
        "front": {
          "sc": "了解银保渠道最新规则以避免合规风险。",
          "tc": "了解銀保渠道最新規則以避免合規風險。"
        },
        "midback": {
          "sc": "将季报中的银保合规要求纳入公司操作指引。",
          "tc": "將季報中的銀保合規要求納入公司操作指引。"
        },
        "lead": {
          "sc": "了解监管协同对银保渠道战略定位的影响。",
          "tc": "了解監管協同對銀保渠道戰略定位的影響。"
        },
        "cross": {
          "sc": "跨境金融业务合规要求与银保监管框架同步升级。",
          "tc": "跨境金融業務合規要求與銀保監管框架同步升級。"
        }
      },
      "source": {
        "sc": "金管局 · 季报 2026-06-29",
        "tc": "金管局 · 季报 2026-06-29",
        "lang": "zh"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "金管局",
          "银保",
          "运营韧性"
        ],
        "tc": [
          "金管局",
          "銀保",
          "運營韌性"
        ]
      },
      "themes": [
        "reg",
        "compliance",
        "channel"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 2,
        "lead": 2,
        "cross": 1
      },
      "publishedAt": "2026-06-29T12:00:00+08:00",
      "originalUrl": "https://www.info.gov.hk/gia/general/202606/29/P2026062900459.htm",
      "sourceKey": "govhk",
      "boards": [
        "reg",
        "market"
      ],
      "contentKind": "press"
    },
    {
      "id": "ia-20260628-fsdc-talent",
      "clusterCount": 1,
      "score": 70,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "title": {
        "sc": "金发局发布保险业人才培育报告：呼吁建设新一代保险专才。",
        "tc": "金發局發布保險業人才培育報告：呼籲建設新一代保險專才。"
      },
      "summary": {
        "sc": "2026年6月，香港金融发展局（FSDC）发布《培育新一代保险专才》研究报告。报告审视了保险业人才格局的变化，识别了关键技能缺口，并为建设可持续的人才管道绘制了战略路径，特别关注AI、跨境合规和HNW服务等新兴领域的人才需求。",
        "tc": "2026年6月，香港金融發展局（FSDC）發布《培育新一代保險專才》研究報告。報告審視了保險業人才格局的變化，識別了關鍵技能缺口，並為建設可持續的人才管道繪製了戰略路徑，特別關注AI、跨境合規和HNW服務等新興領域的人才需求。"
      },
      "why": {
        "sc": "人才短缺是行业增长的隐性瓶颈；报告为团队招聘和培训提供方向参考。",
        "tc": "人才短缺是行業增長的隱性瓶頸；報告為團隊招聘和培訓提供方向參考。"
      },
      "actions": {
        "front": {
          "sc": "持续提升AI、合规和HNW服务方面的专业能力。",
          "tc": "持續提升AI、合規和HNW服務方面的專業能力。"
        },
        "midback": {
          "sc": "将报告所列技能缺口纳入招聘和培训计划。｜关注行业人才竞争对薪酬结构的影响。",
          "tc": "將報告所列技能缺口納入招聘和培訓計劃。｜關注行業人才競爭對薪酬結構的影響。"
        },
        "lead": {
          "sc": "团队建设中注意AI+合规+HNW复合型人才的储备。",
          "tc": "團隊建設中注意AI+合規+HNW複合型人才的儲備。"
        },
        "cross": {
          "sc": "跨境业务对多法域合规人才的需求更为迫切。",
          "tc": "跨境業務對多法域合規人才的需求更為迫切。"
        }
      },
      "source": {
        "sc": "金发局 · 研究报告 2026-06",
        "tc": "金发局 · 研究报告 2026-06",
        "lang": "zh"
      },
      "sourceTier": "research",
      "tags": {
        "sc": [
          "人才",
          "金发局",
          "技能缺口"
        ],
        "tc": [
          "人才",
          "金發局",
          "技能缺口"
        ]
      },
      "themes": [
        "career",
        "market",
        "tech"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 2,
        "lead": 3,
        "cross": 1
      },
      "publishedAt": "2026-06-28T10:00:00+08:00",
      "originalUrl": "https://www.fsdc.org.hk/en/media/fsdc-releases-report-fostering-a-new-generation-of-insurance-professionals-in-hong-kong-to-support-the-thriving-development",
      "sourceKey": "bc17ef77b7fd",
      "boards": [
        "market",
        "insurer"
      ],
      "contentKind": "research"
    },
    {
      "id": "ia-20260626-morganstanley",
      "clusterCount": 1,
      "score": 66,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "title": {
        "sc": "摩根士丹利2026年6月股市评论：关注亚洲保险板块防御价值。",
        "tc": "摩根士丹利2026年6月股市評論：關注亞洲保險板塊防禦價值。"
      },
      "summary": {
        "sc": "2026年6月，摩根士丹利研究部发布月度股市评论，在全球不确定性上升的背景下，强调亚洲保险板块的防御价值。报告指出寿险公司受益于高利率环境和亚洲中产阶层扩张，建议投资者超配优质保险股。",
        "tc": "2026年6月，摩根士丹利研究部發布月度股市評論，在全球不確定性上升的背景下，強調亞洲保險板塊的防禦價值。報告指出壽險公司受益於高利率環境和亞洲中產階層擴張，建議投資者超配優質保險股。"
      },
      "why": {
        "sc": "华尔街顶级投行在不确定性中推荐保险板块，强化保险作为防御资产的叙事。",
        "tc": "華爾街頂級投行在不確定性中推薦保險板塊，強化保險作為防禦資產的敘事。"
      },
      "actions": {
        "front": {
          "sc": "对客沟通可用摩根士丹利的防御资产推荐来增强保险配置的说服力。",
          "tc": "對客溝通可用摩根士丹利的防禦資產推薦來增強保險配置的說服力。"
        },
        "midback": {
          "sc": "将机构研报纳入公司市场研判资料库。",
          "tc": "將機構研報納入公司市場研判資料庫。"
        },
        "lead": {
          "sc": "投资型保险产品的市场叙事支持。",
          "tc": "投資型保險產品的市場敘事支持。"
        },
        "cross": {
          "sc": "全球保险板块的防御属性与香港离岸保险市场形成互补。",
          "tc": "全球保險板塊的防禦屬性與香港離岸保險市場形成互補。"
        }
      },
      "source": {
        "sc": "摩根士丹利研究 · 月度评论 2026-06 [EN原文]",
        "tc": "摩根士丹利研究 · 月度评论 2026-06 [EN原文]",
        "lang": "zh"
      },
      "sourceTier": "research",
      "tags": {
        "sc": [
          "摩根士丹利",
          "防御资产",
          "保险板块"
        ],
        "tc": [
          "摩根士丹利",
          "防禦資產",
          "保險板塊"
        ]
      },
      "themes": [
        "macro",
        "market"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 1,
        "lead": 2,
        "cross": 1
      },
      "publishedAt": "2026-06-26T15:00:00+08:00",
      "originalUrl": "https://www.morganstanley.com/im/en-hk/intermediary-investor/insights/slimmons-take/equity-market-commentary-june-2026.html",
      "sourceKey": "morganstanley",
      "boards": [
        "market"
      ],
      "contentKind": "research"
    },
    {
      "id": "ia-20260626-pimco-asia",
      "clusterCount": 1,
      "score": 68,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "title": {
        "sc": "PIMCO 2026年Q2亚洲交易室更新：亚太分化加剧，看好保险资产配置价值。",
        "tc": "PIMCO 2026年Q2亞洲交易室更新：亞太分化加劇，看好保險資產配置價值。"
      },
      "summary": {
        "sc": "2026年6月，PIMCO发布Q2亚洲交易室更新。在地缘风险上升和亚太分化加剧的背景下，PIMCO强调保险资产在高利率环境下的配置价值，尤其在亚洲高储蓄率和人口老龄化推动下，寿险资产作为长期配置工具的地位进一步巩固。",
        "tc": "2026年6月，PIMCO發布Q2亞洲交易室更新。在地緣風險上升和亞太分化加劇的背景下，PIMCO強調保險資產在高利率環境下的配置價值，尤其在亞洲高儲蓄率和人口老齡化推動下，壽險資產作為長期配置工具的地位進一步鞏固。"
      },
      "why": {
        "sc": "全球最大固定收益管理人对保险资产的背书，为客户配置美元保单提供专业论据。",
        "tc": "全球最大固定收益管理人對保險資產的背書，為客戶配置美元保單提供專業論據。"
      },
      "actions": {
        "front": {
          "sc": "对客可用PIMCO观点说明分红保单在当前利率环境下的配置价值。",
          "tc": "對客可用PIMCO觀點說明分紅保單在當前利率環境下的配置價值。"
        },
        "midback": {
          "sc": "投资策略团队可参考PIMCO对亚洲固收市场的判断。",
          "tc": "投資策略團隊可參考PIMCO對亞洲固收市場的判斷。"
        },
        "lead": {
          "sc": "市场叙事：全球顶级资管机构看好保险资产。",
          "tc": "市場敘事：全球頂級資管機構看好保險資產。"
        },
        "cross": {
          "sc": "跨境配置需关注不同市场的利率与汇率风险。",
          "tc": "跨境配置需關注不同市場的利率與匯率風險。"
        }
      },
      "source": {
        "sc": "PIMCO · Q2亚洲更新 2026-06 [EN原文]",
        "tc": "PIMCO · Q2亚洲更新 2026-06 [EN原文]",
        "lang": "zh"
      },
      "sourceTier": "research",
      "tags": {
        "sc": [
          "PIMCO",
          "固定收益",
          "保险资产"
        ],
        "tc": [
          "PIMCO",
          "固定收益",
          "保險資產"
        ]
      },
      "themes": [
        "macro",
        "market"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 1,
        "lead": 2,
        "cross": 1
      },
      "publishedAt": "2026-06-26T11:00:00+08:00",
      "originalUrl": "https://www.pimco.com/hk/en/resources/video-library/media/q3-2026-update-from-the-asia-trade-floor",
      "sourceKey": "pimco",
      "boards": [
        "market"
      ],
      "contentKind": "research"
    },
    {
      "id": "taiping-202606-rating",
      "clusterCount": 1,
      "score": 74,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T17:30:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "中国太平再保险连续17年获惠誉A评级。",
        "tc": "中國太平再保險連續17年獲惠譽A評級。"
      },
      "summary": {
        "sc": "惠誉2026年6月确认太平再保险财务实力A评级（强劲），展望稳定。这是太平再保险连续第17年获得惠誉A评级。太平集团在港经营超80年。[EN原文]",
        "tc": "太平再保連續17年獲惠譽A評級"
      },
      "why": {
        "sc": "评级，也是中资保司在港信用背书的重要指标。",
        "tc": "評級，也是中資保司信用背書。"
      },
      "actions": {
        "front": {
          "sc": "中资保司偏好客户可引述评级",
          "tc": "中資客戶可引述評級"
        },
        "midback": {
          "sc": "更新太平品牌档案",
          "tc": "更新品牌檔案"
        },
        "lead": {
          "sc": ""
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "中国太平/惠誉",
        "tc": "中國太平/惠譽",
        "lang": "zh"
      },
      "boards": [
        "firm"
      ],
      "tags": {
        "sc": [
          "太平",
          "惠誉",
          "评级",
          "A级"
        ],
        "tc": [
          "太平",
          "惠譽",
          "評級",
          "A級"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-06-26T10:00:00+08:00",
      "originalUrl": "https://www.cntaiping.com/news/123435.html",
      "sourceKey": "taiping:rating-20260626",
      "sourceTier": "media",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20260625-manulife-convention",
      "clusterCount": 1,
      "score": 70,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "title": {
        "sc": "宏利2026年度大会在香港举行：聚焦退休未来与AI驱动转型。",
        "tc": "宏利2026年度大會在香港舉行：聚焦退休未來與AI驅動轉型。"
      },
      "summary": {
        "sc": "2026年6月25日，宏利在香港举办年度大会（Manulife Annual Convention 2026），主题包括「退休未来」、AI在保险业的规模化应用、以及代理人渠道数字化转型。大会展示了宏利在亚洲市场的最新战略方向和科技投入成果。",
        "tc": "2026年6月25日，宏利在香港舉辦年度大會（Manulife Annual Convention 2026），主題包括「退休未來」、AI在保險業的規模化應用、以及代理人渠道數字化轉型。大會展示了宏利在亞洲市場的最新戰略方向和科技投入成果。"
      },
      "why": {
        "sc": "宏利战略方向明确：退休+科技双轮驱动，对同业有参照意义。",
        "tc": "宏利戰略方向明確：退休+科技雙輪驅動，對同業有參照意義。"
      },
      "actions": {
        "front": {
          "sc": "了解宏利新产品/服务方向以优化客户方案。",
          "tc": "了解宏利新產品/服務方向以優化客戶方案。"
        },
        "midback": {
          "sc": "宏利战略方向可作为公司年度规划的竞品对标。",
          "tc": "宏利戰略方向可作為公司年度規劃的競品對標。"
        },
        "lead": {
          "sc": "团队战略沟通：关注行业领导者的投入方向。",
          "tc": "團隊戰略溝通：關注行業領導者的投入方向。"
        },
        "cross": {
          "sc": "退休产品与跨境养老方案结合的市场机会。",
          "tc": "退休產品與跨境養老方案結合的市場機會。"
        }
      },
      "source": {
        "sc": "宏利 · 年度大会 2026-06-25",
        "tc": "宏利 · 年度大会 2026-06-25",
        "lang": "zh"
      },
      "sourceTier": "insurer",
      "tags": {
        "sc": [
          "宏利",
          "退休",
          "数字化转型"
        ],
        "tc": [
          "宏利",
          "退休",
          "數字化轉型"
        ]
      },
      "themes": [
        "firm",
        "tech",
        "market"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 1,
        "lead": 2,
        "cross": 1
      },
      "publishedAt": "2026-06-25T18:00:00+08:00",
      "originalUrl": "https://www.instagram.com/reel/DYS1bksR7gR/",
      "sourceKey": "7f278f52d5a0",
      "boards": [
        "insurer",
        "tech"
      ],
      "contentKind": "event"
    },
    {
      "id": "empf-2026-fee-reduction",
      "clusterCount": 1,
      "score": 80,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": true,
      "ingestedAt": "2026-07-28T23:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "积金易平台降费：236只基金行政费降至0.37% 惠及千万账户。",
        "tc": "積金易平台降費：236隻基金行政費降至0.37% 惠及千萬賬戶。"
      },
      "summary": {
        "sc": "积金局旗下积金易平台(eMPF)全面运作后，378个强积金基金中236个基金的行政费须降至不高于0.37%。覆盖18个强积金计划，惠及超过1000万个计划成员账户，占整体账户逾九成。强积金总资产已增至1.5万亿港元(2025年)。",
        "tc": "積金易降費至0.37% 覆蓋逾千萬賬戶"
      },
      "why": {
        "sc": "强积金降费直接影响香港打工仔退休储蓄效率，也是保险产品销售环境。",
        "tc": "強積金降費影響退休儲蓄效率。"
      },
      "actions": {
        "front": {
          "sc": "向客户解释MPF降费对退休规划的影响",
          "tc": "解釋MPF降費對退休規劃影響"
        },
        "midback": {
          "sc": "归档强积金数据",
          "tc": "歸檔強積金數據"
        },
        "lead": {
          "sc": "降费=自愿性供款空间增大=保险需求提升",
          "tc": "保險需求提升"
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "积金局/eMPF",
        "tc": "積金局/eMPF",
        "lang": "zh"
      },
      "boards": [
        "macro",
        "compliance"
      ],
      "tags": {
        "sc": [
          "积金易",
          "强积金",
          "降费",
          "0.37%"
        ],
        "tc": [
          "積金易",
          "強積金",
          "降費",
          "0.37%"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-06-25T10:00:00+08:00",
      "originalUrl": "https://www.empf.org.hk/",
      "sourceKey": "empf:fee-reduction-2026",
      "sourceTier": "media",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "manulife-20260625-board",
      "clusterCount": 1,
      "score": 72,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T16:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "宏利委任吴立贤为独立非执行董事。",
        "tc": "宏利委任吳立賢為獨立非執行董事。"
      },
      "summary": {
        "sc": "宏利人寿保险2026年6月25日宣布委任吴立贤女士为独立非执行董事，强化公司治理结构。",
        "tc": "宏利6月25日委任新獨立非執董"
      },
      "why": {
        "sc": "公司治理升级，也是長期稳健信号。",
        "tc": "公司治理升級。"
      },
      "actions": {
        "front": {
          "sc": "知识储备",
          "tc": "知識儲備"
        },
        "midback": {
          "sc": "更新宏利管理层档案",
          "tc": "更新管理層檔案"
        },
        "lead": {
          "sc": ""
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "宏利新闻稿",
        "tc": "宏利新聞稿",
        "lang": "zh"
      },
      "boards": [
        "firm"
      ],
      "tags": {
        "sc": [
          "宏利",
          "董事",
          "治理"
        ],
        "tc": [
          "宏利",
          "董事",
          "治理"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-06-25T10:00:00+08:00",
      "originalUrl": "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html",
      "sourceKey": "manulife",
      "sourceTier": "insurer",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20260624-rga-trends",
      "clusterCount": 1,
      "score": 65,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "title": {
        "sc": "RGA发布2026年Q2产品趋势报告：AIA财富灵活储蓄保、AXA私人平台被列为重点新品。",
        "tc": "RGA發布2026年Q2產品趨勢報告：AIA財富靈活儲蓄保、AXA私人平台被列為重點新品。"
      },
      "summary": {
        "sc": "2026年6月，RGA（美国再保险集团）发布2026年Q2产品趋势报告，涵盖亚太区主要市场新品动态。报告将AIA Wealth Flexi储蓄保和AXA Global Private平台列为当季香港市场重点创新，同时关注多货币、传承功能和HNW定制化成为行业趋势。",
        "tc": "2026年6月，RGA（美國再保險集團）發布2026年Q2產品趨勢報告，涵蓋亞太區主要市場新品動態。報告將AIA Wealth Flexi儲蓄保和AXA Global Private平台列為當季香港市場重點創新，同時關注多貨幣、傳承功能和HNW定製化成為行業趨勢。"
      },
      "why": {
        "sc": "再保视角的产品趋势报告，为前线提供行业创新风向标。",
        "tc": "再保視角的產品趨勢報告，為前線提供行業創新風向標。"
      },
      "actions": {
        "front": {
          "sc": "了解行业产品创新趋势，把握对客沟通的差异化卖点。",
          "tc": "了解行業產品創新趨勢，把握對客溝通的差異化賣點。"
        },
        "midback": {
          "sc": "产品策略可参考RGA趋势报告中的行业方向。",
          "tc": "產品策略可參考RGA趨勢報告中的行業方向。"
        },
        "lead": {
          "sc": "产品创新驱动是新业务增长的关键引擎。",
          "tc": "產品創新驅動是新業務增長的關鍵引擎。"
        },
        "cross": {
          "sc": "跨境高净值产品趋势与本地零售差异化明显。",
          "tc": "跨境高淨值產品趨勢與本地零售差異化明顯。"
        }
      },
      "source": {
        "sc": "RGA · 产品趋势报告 2026-Q2 [EN原文]",
        "tc": "RGA · 产品趋势报告 2026-Q2 [EN原文]",
        "lang": "zh"
      },
      "sourceTier": "research",
      "tags": {
        "sc": [
          "产品趋势",
          "再保险",
          "创新"
        ],
        "tc": [
          "產品趨勢",
          "再保險",
          "創新"
        ]
      },
      "themes": [
        "product",
        "market"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 1,
        "lead": 2,
        "cross": 1
      },
      "publishedAt": "2026-06-24T14:00:00+08:00",
      "originalUrl": "http://experience.rgare.com/product-trends-2026-q2",
      "sourceKey": "rga",
      "boards": [
        "product",
        "market"
      ],
      "contentKind": "research"
    },
    {
      "id": "ia-20260620-goldman-outlook",
      "clusterCount": 1,
      "score": 68,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "title": {
        "sc": "高盛重申2026年美股乐观展望：盈利增长驱动，保险金融板块受益。",
        "tc": "高盛重申2026年美股樂觀展望：盈利增長驅動，保險金融板塊受益。"
      },
      "summary": {
        "sc": "2026年6月底，高盛研究部重申对2026年美股的乐观立场，预测标普500指数目标8,000点，核心驱动为盈利增长而非估值扩张。金融和保险板块在高利率环境下持续受益；AI基础设施投资预计达7,500亿美元。",
        "tc": "2026年6月底，高盛研究部重申對2026年美股的樂觀立場，預測標普500指數目標8,000點，核心驅動為盈利增長而非估值擴張。金融和保險板塊在高利率環境下持續受益；AI基礎設施投資預計達7,500億美元。"
      },
      "why": {
        "sc": "高盛对金融/保险板块的持续看好为行业提供正向宏观叙事。",
        "tc": "高盛對金融/保險板塊的持續看好為行業提供正向宏觀敘事。"
      },
      "actions": {
        "front": {
          "sc": "对客可引用高盛观点增强投资型保险产品的说服力。",
          "tc": "對客可引用高盛觀點增強投資型保險產品的說服力。"
        },
        "midback": {
          "sc": "机构研究观点纳入公司投研简报。",
          "tc": "機構研究觀點納入公司投研簡報。"
        },
        "lead": {
          "sc": "理解全球资金流向与板块轮动，为团队投资策略提供依据。",
          "tc": "理解全球資金流向與板塊輪動，為團隊投資策略提供依據。"
        },
        "cross": {
          "sc": "高利率环境对跨境美元保单有利。",
          "tc": "高利率環境對跨境美元保單有利。"
        }
      },
      "source": {
        "sc": "高盛研究 · 市场展望 2026-06 [EN原文]",
        "tc": "高盛研究 · 市场展望 2026-06 [EN原文]",
        "lang": "zh"
      },
      "sourceTier": "media",
      "tags": {
        "sc": [
          "高盛",
          "美股",
          "金融板块"
        ],
        "tc": [
          "高盛",
          "美股",
          "金融板塊"
        ]
      },
      "themes": [
        "macro",
        "market"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 1,
        "lead": 2,
        "cross": 1
      },
      "publishedAt": "2026-06-20T16:00:00+08:00",
      "originalUrl": "https://finance.yahoo.com/markets/stocks/articles/goldman-sachs-doubles-down-stock-210300868.html",
      "sourceKey": "yahoofinance",
      "boards": [
        "market"
      ],
      "contentKind": "research"
    },
    {
      "id": "fwd-2026-brand-victoria",
      "clusterCount": 1,
      "score": 73,
      "verifyStatus": "pending",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T17:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "富卫香港2026品牌升级：维港双岸招牌同时亮灯。",
        "tc": "富衛香港2026品牌升級：維港雙岸招牌同時亮燈。"
      },
      "summary": {
        "sc": "富卫保险2026年品牌升级，从1881 Heritage延伸至尖沙咀The ONE，维港两岸招牌同时亮灯。品牌影片以「创造保险新体验」为主题，彰显深耕香港的决心。",
        "tc": "富衛維港雙岸招牌亮燈品牌升級"
      },
      "why": {
        "sc": "品牌投入，也是市占率竞争信号，富卫持续加大对港布局。",
        "tc": "品牌投入，也是市佔率競爭。"
      },
      "actions": {
        "front": {
          "sc": "品牌知名度提升可辅助客户沟通",
          "tc": "品牌知名度輔助溝通"
        },
        "midback": {
          "sc": ""
        },
        "lead": {
          "sc": "关注富卫品牌投入后的市场份额变化",
          "tc": "關注市佔率變化"
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "FWD/YouTube",
        "tc": "FWD/YouTube",
        "lang": "zh"
      },
      "boards": [
        "firm"
      ],
      "tags": {
        "sc": [
          "富卫",
          "品牌",
          "维港",
          "2026"
        ],
        "tc": [
          "富衛",
          "品牌",
          "維港",
          "2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-06-20T10:00:00+08:00",
      "originalUrl": "https://www.youtube.com/watch?v=2Kei5uxrEfU",
      "sourceKey": "fwd:brand-2026",
      "sourceTier": "media",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "henley-wealth-migration-2026",
      "clusterCount": 1,
      "score": 80,
      "verifyStatus": "verified",
      "sourceTier": "pro",
      "sourceKey": "henley",
      "title": {
        "sc": "Henley 2026 私人财富迁移报告：香港重回全球高净值流入 Top 5",
        "tc": "Henley 2026 私人財富遷移報告：香港重回全球高淨值流入 Top 5"
      },
      "summary": {
        "sc": "Henley & Partners 发布《2026 私人财富迁移报告》：受益于 CIES 新政和家办税务优惠，香港重回全球高净值人士净流入前五名。报告同时跟踪全球投资移民项目的最新政策变化和申请趋势。",
        "tc": "Henley & Partners 發布《2026 私人財富遷移報告》：受益於 CIES 新政和家辦稅務優惠，香港重回全球高淨值人士淨流入前五名。報告同時跟蹤全球投資移民項目的最新政策變化和申請趨勢。"
      },
      "why": {
        "sc": "Henley 是全球投资移民领域的权威数据源——他们的年度迁移报告是「身份规划」的行业晴雨表。对跨境 IFA 来说，高净值人士的流向直接等于客户的流向。",
        "tc": "Henley 是全球投資移民領域的權威數據源——他們的年度遷移報告是「身份規劃」的行業晴雨表。對跨境 IFA 來說，高淨值人士的流向直接等於客戶的流向。"
      },
      "actions": {
        "front": {
          "sc": "高净值流入=潜在客户流入，可据此规划获客策略",
          "tc": "高淨值流入=潛在客戶流入，可據此規劃獲客策略"
        },
        "midback": {
          "sc": "身份规划的法律合规框架需随政策更新",
          "tc": "身份規劃的法律合規框架需隨政策更新"
        },
        "lead": {
          "sc": "香港重回前五=团队可借此强化跨境定位",
          "tc": "香港重回前五=團隊可藉此強化跨境定位"
        },
        "cross": {
          "sc": "投资移民+保险+信托是跨境家办三板斧",
          "tc": "投資移民+保險+信託是跨境家辦三板斧"
        }
      },
      "rolesImpact": {
        "front": 3,
        "midback": 2,
        "lead": 4,
        "cross": 5
      },
      "source": {
        "sc": "Henley & Partners",
        "lang": "zh"
      },
      "boards": [
        "family"
      ],
      "themes": [
        "offshore",
        "family-office"
      ],
      "tags": {
        "sc": [
          "身份规划",
          "高净值",
          "移民"
        ],
        "tc": [
          "身份規劃",
          "高淨值",
          "移民"
        ]
      },
      "contentKind": "stats",
      "publishedAt": "2026-06-20T10:00:00+08:00",
      "originalUrl": "https://www.henleyglobal.com/publications/private-wealth-migration-report-2026"
    },
    {
      "id": "ia-ai-cohort-202606",
      "clusterCount": 1,
      "score": 81,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:30:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "保监局AI促进计划再扩容：新增宏利等三家保司。",
        "tc": "保監局AI促進計劃再擴容：新增宏利等三家保司。"
      },
      "summary": {
        "sc": "保监局AI促进计划2026年6月新增3家保险公司。宏利香港部署AI涵盖分销、核保、理赔和客户服务全链条，含双语AI助手和数据驱动销售工具。中银人寿签署《人工智能承诺》。",
        "tc": "保監局AI促進計劃新增宏利等三家保司"
      },
      "why": {
        "sc": "AI在保险业的应用从实验转向生产级部署，行业效率拐点。",
        "tc": "AI在保險業從實驗轉向生產級。"
      },
      "actions": {
        "front": {
          "sc": "了解AI核保对客户投保流程的影响",
          "tc": "了解AI核保對投保流程影響"
        },
        "midback": {
          "sc": "关注AI在合规监控中的应用",
          "tc": "關注AI合規應用"
        },
        "lead": {
          "sc": "评估AI工具对团队效率的提升潜力",
          "tc": "評估AI工具對團隊效率提升"
        },
        "cross": {
          "sc": "跨境业务中AI工具的合规边界",
          "tc": "跨境業務中AI合規邊界"
        }
      },
      "source": {
        "sc": "Insurance Business Mag",
        "tc": "Insurance Business Mag",
        "lang": "en"
      },
      "boards": [
        "tech",
        "firm"
      ],
      "tags": {
        "sc": [
          "AI",
          "宏利",
          "中银人寿",
          "保险科技"
        ],
        "tc": [
          "AI",
          "宏利",
          "中銀人壽",
          "保險科技"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-06-18T12:00:00+08:00",
      "originalUrl": "https://www.insurancebusinessmag.com/asia/news/technology/insurance-authority-adds-three-insurers-to-ai-cohort-programme-579133.aspx",
      "sourceKey": "insurancebusinessmag",
      "sourceTier": "pro",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20260618-blackrock-outlook",
      "clusterCount": 1,
      "score": 70,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "title": {
        "sc": "贝莱德2026年中全球投资展望：呼吁投资组合重思，关注保险板块的稳定器角色。",
        "tc": "貝萊德2026年中全球投資展望：呼籲投資組合重思，關注保險板塊的穩定器角色。"
      },
      "summary": {
        "sc": "2026年6月，贝莱德投资研究院发布2026年中全球投资展望报告。核心观点是在地缘分裂与AI投资巨潮下，投资者需要更精细的投资组合构建。保险业被视为在经济波动中的重要稳定器，寿险板块受益于高利率环境。",
        "tc": "2026年6月，貝萊德投資研究院發布2026年中全球投資展望報告。核心觀點是在地緣分裂與AI投資巨潮下，投資者需要更精細的投資組合構建。保險業被視為在經濟波動中的重要穩定器，壽險板塊受益於高利率環境。"
      },
      "why": {
        "sc": "全球最大资管机构将保险定位为稳定器；对港险的资产配置逻辑提供宏观背书。",
        "tc": "全球最大資管機構將保險定位為穩定器；對港險的資產配置邏輯提供宏觀背書。"
      },
      "actions": {
        "front": {
          "sc": "对客可用「机构投资者视保险为稳定器」的叙事。",
          "tc": "對客可用「機構投資者視保險為穩定器」的敘事。"
        },
        "midback": {
          "sc": "了解宏观资产配置趋势以优化产品推荐策略。",
          "tc": "了解宏觀資產配置趨勢以優化產品推薦策略。"
        },
        "lead": {
          "sc": "团队投资策略培训可参考BlackRock宏观框架。",
          "tc": "團隊投資策略培訓可參考BlackRock宏觀框架。"
        },
        "cross": {
          "sc": "跨境配置：香港作为离岸中心的角色在报告中得到间接背书。",
          "tc": "跨境配置：香港作為離岸中心的角色在報告中得到間接背書。"
        }
      },
      "source": {
        "sc": "贝莱德投资研究院 · 2026年中展望 [EN原文]",
        "tc": "贝莱德投资研究院 · 2026年中展望 [EN原文]",
        "lang": "zh"
      },
      "sourceTier": "research",
      "tags": {
        "sc": [
          "投资展望",
          "贝莱德",
          "资产配置"
        ],
        "tc": [
          "投資展望",
          "貝萊德",
          "資產配置"
        ]
      },
      "themes": [
        "macro",
        "market"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 1,
        "lead": 2,
        "cross": 2
      },
      "publishedAt": "2026-06-18T09:00:00+08:00",
      "originalUrl": "https://www.blackrock.com/corporate/insights/blackrock-investment-institute/publications/outlook",
      "sourceKey": "blackrock",
      "boards": [
        "market"
      ],
      "contentKind": "research"
    },
    {
      "id": "ia-20260617-manulife-ai",
      "clusterCount": 1,
      "score": 77,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "title": {
        "sc": "宏利香港加入保监局AI促进计划：AI已覆盖核保、分销与客服三线。",
        "tc": "宏利香港加入保監局AI促進計劃：AI已覆蓋核保、分銷與客服三線。"
      },
      "summary": {
        "sc": "2026年6月15日，宏利（国际）有限公司作为三家新加入保监局AI Cohort Programme的重点参与者之一，披露已在核保、分销、客户服务及理赔等领域部署多款AI工具，包括24/7双语AI客服、代理人数据驱动销售工具及核保辅助AI。公司亦披露与阿里云合作开发AI应用，并考虑共建AI中心。",
        "tc": "2026年6月15日，宏利（國際）有限公司作為三家新加入保監局AI Cohort Programme的重點參與者之一，披露已在核保、分銷、客戶服務及理賠等領域部署多款AI工具，包括24/7雙語AI客服、代理人數據驅動銷售工具及核保輔助AI。公司亦披露與阿里雲合作開發AI應用，並考慮共建AI中心。"
      },
      "why": {
        "sc": "宏利AI布局在港险行业领先，功能覆盖广度超过多数同业公开披露水平。",
        "tc": "宏利AI佈局在港險行業領先，功能覆蓋廣度超過多數同業公開披露水平。"
      },
      "actions": {
        "front": {
          "sc": "了解宏利核保AI对出单时效的改善；销售端可用公司核准AI工具。",
          "tc": "了解宏利核保AI對出單時效的改善；銷售端可用公司核准AI工具。"
        },
        "midback": {
          "sc": "跟踪保司AI服务接口与核保数字化进度。｜评估AI工具对合规流程的影响。",
          "tc": "跟蹤保司AI服務接口與核保數字化進度。｜評估AI工具對合規流程的影響。"
        },
        "lead": {
          "sc": "科技投入对标：宏利的AI投入规模与功能覆盖面可作为行业参照。",
          "tc": "科技投入對標：宏利的AI投入規模與功能覆蓋面可作為行業參照。"
        },
        "cross": {
          "sc": "跨境业务中AI数据隐私与本地化需额外关注。",
          "tc": "跨境業務中AI數據隱私與本地化需額外關注。"
        }
      },
      "source": {
        "sc": "Insurance Business Mag / 保监局 2026-06-17 [EN原文]",
        "tc": "Insurance Business Mag / 保监局 2026-06-17 [EN原文]",
        "lang": "zh"
      },
      "sourceTier": "pro",
      "tags": {
        "sc": [
          "宏利",
          "人工智能",
          "保险科技"
        ],
        "tc": [
          "宏利",
          "人工智能",
          "保險科技"
        ]
      },
      "themes": [
        "tech",
        "firm"
      ],
      "rolesImpact": {
        "front": 2,
        "midback": 2,
        "lead": 2,
        "cross": 1
      },
      "publishedAt": "2026-06-17T10:00:00+08:00",
      "originalUrl": "https://www.insurancebusinessmag.com/asia/news/technology/insurance-authority-adds-three-insurers-to-ai-cohort-programme-579133.aspx",
      "sourceKey": "insurancebusinessmag",
      "boards": [
        "insurer",
        "tech"
      ],
      "contentKind": "industry_news"
    },
    {
      "id": "ia-20260616-aia-prudential-roles",
      "clusterCount": 1,
      "score": 76,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "title": {
        "sc": "友邦及保诚在港增设高净值客户高级职位，抢占亚洲财富管理市场。",
        "tc": "友邦及保誠在港增設高淨值客戶高級職位，搶佔亞洲財富管理市場。"
      },
      "summary": {
        "sc": "2026年6月16日，据Bloomberg报道，友邦保险与保诚集团均在香港设立新的高级职位，专门服务亚洲超高净值客户。此举正值香港超越瑞士成为全球最大离岸财富管理中心之际，BCG预计2030年将有约4.6万亿美元资金流入香港。",
        "tc": "2026年6月16日，據Bloomberg報道，友邦保險與保誠集團均在香港設立新的高級職位，專門服務亞洲超高淨值客戶。此舉正值香港超越瑞士成為全球最大離岸財富管理中心之際，BCG預計2030年將有約4.6萬億美元資金流入香港。"
      },
      "why": {
        "sc": "两大国际保险巨头同步加码HNW赛道，香港离岸保险枢纽地位进一步巩固。",
        "tc": "兩大國際保險巨頭同步加碼HNW賽道，香港離岸保險樞紐地位進一步鞏固。"
      },
      "actions": {
        "front": {
          "sc": "HNW客户获取可从这两家保司的新服务切入。",
          "tc": "HNW客戶獲取可從這兩家保司的新服務切入。"
        },
        "midback": {
          "sc": "关注头部保司HNW战略对行业人才竞争和佣金结构的影响。",
          "tc": "關注頭部保司HNW戰略對行業人才競爭和佣金結構的影響。"
        },
        "lead": {
          "sc": "团队定位：HNW服务升级将成下一阶段竞争焦点。",
          "tc": "團隊定位：HNW服務升級將成下一階段競爭焦點。"
        },
        "cross": {
          "sc": "HNW跨境业务是未来增长极。",
          "tc": "HNW跨境業務是未來增長極。"
        }
      },
      "source": {
        "sc": "Bloomberg · 新闻报道 2026-06-16 [EN原文]",
        "tc": "Bloomberg · 新闻报道 2026-06-16 [EN原文]",
        "lang": "zh"
      },
      "sourceTier": "insurer",
      "tags": {
        "sc": [
          "高净值",
          "友邦",
          "保诚"
        ],
        "tc": [
          "高淨值",
          "友邦",
          "保誠"
        ]
      },
      "themes": [
        "firm",
        "market",
        "channel"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 1,
        "lead": 3,
        "cross": 2
      },
      "publishedAt": "2026-06-16T15:00:00+08:00",
      "originalUrl": "https://sg.finance.yahoo.com/news/aia-prudential-create-senior-roles-221640747.html",
      "sourceKey": "prudential",
      "boards": [
        "insurer",
        "market",
        "family"
      ],
      "contentKind": "industry_news"
    },
    {
      "id": "ia-20260616-cheung-enforcement",
      "clusterCount": 1,
      "score": 92,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "title": {
        "sc": "保监CEO张云正公开警告：行业规避新报酬规则的跨境架构将被适时介入。",
        "tc": "保監CEO張雲正公開警告：行業規避新報酬規則的跨境架構將被適時介入。"
      },
      "summary": {
        "sc": "2026年6月16日，保监局行政总监张云正在公开讲话中警告，已观察到市场参与者试图通过间接方式规避佣金分攤及转介费上限等新报酬措施。保监局将适时介入并对外公布。同时重申确保保险资金经合法合规渠道进入香港的立场。",
        "tc": "2026年6月16日，保監局行政總監張雲正在公開講話中警告，已觀察到市場參與者試圖通過間接方式規避佣金分攤及轉介費上限等新報酬措施。保監局將適時介入並對外公布。同時重申確保保險資金經合法合規渠道進入香港的立場。"
      },
      "why": {
        "sc": "这是监管对行业「猫鼠游戏」的正式回应；企图规避者将被公开执法，威慑力极强。",
        "tc": "這是監管對行業「貓鼠遊戲」的正式回應；企圖規避者將被公開執法，威懾力極強。"
      },
      "actions": {
        "front": {
          "sc": "对客勿参与任何规避佣金规则的结构安排。",
          "tc": "對客勿參與任何規避佣金規則的結構安排。"
        },
        "midback": {
          "sc": "立即检查所有佣金支付、奖金、转介结构是否符合新规。｜有跨境业务者需强化内控与文件留存。",
          "tc": "立即檢查所有佣金支付、獎金、轉介結構是否符合新規。｜有跨境業務者需強化內控與文件留存。"
        },
        "lead": {
          "sc": "确保团队无规避行为；违规可能导致续牌甚至刑事风险。",
          "tc": "確保團隊無規避行為；違規可能導致續牌甚至刑事風險。"
        },
        "cross": {
          "sc": "跨境架构的合规审查优先级提到最高。",
          "tc": "跨境架構的合規審查優先級提到最高。"
        }
      },
      "source": {
        "sc": "保监局 · Bloomberg/信报 2026-06-16 [部分EN原文]",
        "tc": "保监局 · Bloomberg/信报 2026-06-16 [部分EN原文]",
        "lang": "zh"
      },
      "sourceTier": "media",
      "tags": {
        "sc": [
          "执法",
          "跨境架构",
          "报酬规则"
        ],
        "tc": [
          "執法",
          "跨境架構",
          "報酬規則"
        ]
      },
      "themes": [
        "reg",
        "compliance",
        "offshore"
      ],
      "rolesImpact": {
        "front": 2,
        "midback": 3,
        "lead": 3,
        "cross": 3
      },
      "publishedAt": "2026-06-16T12:00:00+08:00",
      "originalUrl": "https://www.bloomberg.com/news/articles/2026-06-15/hong-kong-insurance-regulator-vows-crackdown-on-rule-breakers",
      "sourceKey": "bloomberg",
      "boards": [
        "reg",
        "market"
      ],
      "contentKind": "enforcement"
    },
    {
      "id": "ia-ai-seminar-20260615",
      "title": {
        "sc": "保监局举办「人工智能促进计划」研讨会，新增强点参与保司。",
        "tc": "保監局舉辦「人工智能促進計劃」研討會，新增重點參與保司。"
      },
      "summary": {
        "sc": "保监局2026年6月15日举办人工智能促进计划研讨会，并欢迎三间新的重点参与保险公司，使自2025年8月以来的重点参与者总数继续扩大。",
        "tc": "保監局2026年6月15日舉辦人工智能促進計劃研討會，並歡迎三間新的重點參與保險公司，使自2025年8月以來的重點參與者總數繼續擴大。"
      },
      "why": {
        "sc": "监管鼓励合规前提下的 InsurTech；中介侧可用的核保/服务AI需对齐保司与局方期望。",
        "tc": "監管鼓勵合規前提下的 InsurTech；中介側可用的核保/服務AI需對齊保司與局方期望。"
      },
      "actions": {
        "front": {
          "sc": "使用公司核准工具；勿把未审核AI输出直接给客户。",
          "tc": "使用公司核准工具；勿把未審核AI輸出直接給客戶。"
        },
        "midback": {
          "sc": "跟踪保司AI服务接口与核保数字化进度。｜AI工具清单、数据出境与客户隐私评估。",
          "tc": "跟踪保司AI服務接口與核保數字化進度。｜AI工具清單、數據出境與客戶隱私評估。"
        },
        "lead": {
          "sc": "科技投入与监管沙盒/促进计划对齐。",
          "tc": "科技投入與監管沙盒/促進計劃對齊。"
        },
        "cross": {
          "sc": "跨境数据与AI摘要更敏感，默认本地化处理。",
          "tc": "跨境數據與AI摘要更敏感，默認本地化處理。"
        }
      },
      "source": {
        "sc": "保险业监管局 · 新闻稿 2026-06-15",
        "tc": "保險業監管局 · 新聞稿 2026-06-15"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "人工智能",
          "保险科技"
        ],
        "tc": [
          "人工智能",
          "保險科技"
        ]
      },
      "themes": [
        "tech",
        "reg"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 2,
        "lead": 2,
        "cross": 1
      },
      "publishedAt": "2026-06-15T15:00:00+08:00",
      "score": 78,
      "verifyStatus": "verified",
      "originalUrl": "https://www.ia.org.hk/sc/infocenter/press_releases/20260615.html",
      "featured": false,
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "insurer",
        "reg",
        "tech"
      ],
      "contentKind": "press"
    },
    {
      "id": "axa-2026-bloomberg-awards",
      "clusterCount": 1,
      "score": 74,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T16:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "AXA安盛于《彭博商业周刊》「金融机构2026」获七项殊荣。",
        "tc": "AXA安盛於《彭博商業周刊》「金融機構2026」獲七項殊榮。"
      },
      "summary": {
        "sc": "AXA安盛在《彭博商业周刊》「金融机构2026」评选中荣获七项殊荣，涵盖自愿医保、危疾、储蓄、客户服务等领域，反映其产品与服务的综合实力。",
        "tc": "AXA安盛獲彭博七項殊榮"
      },
      "why": {
        "sc": "独立第三方评选，也是产品竞争力的客观验证。",
        "tc": "第三方評選，也是競爭力驗證。"
      },
      "actions": {
        "front": {
          "sc": "客户品牌对比时可用",
          "tc": "品牌對比時可用"
        },
        "midback": {
          "sc": "更新AXA品牌评估",
          "tc": "更新品牌評估"
        },
        "lead": {
          "sc": ""
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "AXA/彭博",
        "tc": "AXA/彭博",
        "lang": "zh"
      },
      "boards": [
        "product",
        "firm"
      ],
      "tags": {
        "sc": [
          "AXA",
          "彭博",
          "奖项",
          "2026"
        ],
        "tc": [
          "AXA",
          "彭博",
          "獎項",
          "2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-06-15T10:00:00+08:00",
      "originalUrl": "https://www.prnewswire.com/apac/zh/news-releases/axa2026-302811776.html",
      "sourceKey": "axa:bloomberg-awards-2026",
      "sourceTier": "insurer",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "bain-gba-crossborder-2026",
      "clusterCount": 1,
      "score": 73,
      "verifyStatus": "verified",
      "sourceTier": "pro",
      "sourceKey": "Bain & Company",
      "title": {
        "sc": "Bain 大湾区报告：跨境保险续保/理赔/查询是核心需求",
        "tc": "Bain 大灣區報告：跨境保險續保/理賠/查詢是核心需求"
      },
      "summary": {
        "sc": "Bain 发布大湾区个人金融服务报告，指出保险公司预期未来将允许港险公司为内地客户提供续保、理赔和保单查询服务。跨境金融服务的制度突破正在从「能不能买」升级到「买完怎么服务」。",
        "tc": "Bain 發佈大灣區個人金融服務報告，指出保險公司預期未來將允許港險公司為內地客戶提供續保、理賠和保單查詢服務。跨境金融服務的制度突破正在從「能不能買」升級到「買完怎麼服務」。"
      },
      "why": {
        "sc": "「保单售后服务跨境化」是所有 IFA 的终极痛点——客户买了港险回内地后理赔难。Bain 报告给出的是制度层面的突破信号。",
        "tc": "「保單售後服務跨境化」是所有 IFA 的終極痛點——客戶買了港險回內地後理賠難。Bain 報告給出的是制度層面的突破信號。"
      },
      "actions": {
        "front": {
          "sc": "跨境后续服务的制度突破将降低客户流失率",
          "tc": "跨境後續服務的制度突破將降低客戶流失率"
        },
        "midback": {
          "sc": "关注跨境服务合规框架的演进",
          "tc": "關注跨境服務合規框架的演進"
        },
        "lead": {
          "sc": "售后跨境化是一个待落地的战略机会窗口",
          "tc": "售後跨境化是一個待落地的戰略機會窗口"
        },
        "cross": {
          "sc": "服务的跨境化是产品跨境化的自然延伸",
          "tc": "服務的跨境化是產品跨境化的自然延伸"
        }
      },
      "rolesImpact": {
        "front": 4,
        "midback": 3,
        "lead": 3,
        "cross": 4
      },
      "source": {
        "sc": "Bain & Company",
        "lang": "zh"
      },
      "boards": [
        "family",
        "market"
      ],
      "themes": [
        "offshore",
        "compliance"
      ],
      "tags": {
        "sc": [
          "大湾区",
          "跨境服务",
          "理赔"
        ],
        "tc": [
          "大灣區",
          "跨境服務",
          "理賠"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2026-06-15T10:00:00+08:00",
      "originalUrl": "https://www.bain.com/insights/greater-bay-area-personal-financial-services-report-enabling-cross-boundary-lifestyles/"
    },
    {
      "id": "ia-20260615-bloomberg-crackdown",
      "clusterCount": 1,
      "score": 88,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "title": {
        "sc": "Bloomberg：香港保险监管机构誓言打击违规者 — 跨境架构规避新规被点名警告。",
        "tc": "Bloomberg：香港保險監管機構誓言打擊違規者 — 跨境架構規避新規被點名警告。"
      },
      "summary": {
        "sc": "2026年6月15日，Bloomberg报道香港保险监管机构誓言打击违规行为。保监局行政总监张云正表示已观察到市场参与者试图规避佣金分摊和转介费上限等新规，将通过前瞻性监控适时介入。该报道引发业界广泛关注，被视为监管从规则制定转向严格执法的转折点。",
        "tc": "2026年6月15日，Bloomberg報道香港保險監管機構誓言打擊違規行為。保監局行政總監張雲正表示已觀察到市場參與者試圖規避佣金分攤和轉介費上限等新規，將通過前瞻性監控適時介入。該報道引發業界廣泛關注，被視為監管從規則制定轉向嚴格執法的轉折點。"
      },
      "why": {
        "sc": "国际主流财经媒体首次大规模报道香港保险监管执法转向，标志着监管公信力和威慑力的国际化。",
        "tc": "國際主流財經媒體首次大規模報道香港保險監管執法轉向，標誌著監管公信力和威懾力的國際化。"
      },
      "actions": {
        "front": {
          "sc": "理解监管执法趋势，避免参与任何灰色地带的业务安排。",
          "tc": "理解監管執法趨勢，避免參與任何灰色地帶的業務安排。"
        },
        "midback": {
          "sc": "将Bloomberg报道纳入合规培训素材。｜评估跨境业务是否存在规避风险。",
          "tc": "將Bloomberg報道納入合規培訓素材。｜評估跨境業務是否存在規避風險。"
        },
        "lead": {
          "sc": "监管执法强度升级将重塑行业竞争格局。",
          "tc": "監管執法強度升級將重塑行業競爭格局。"
        },
        "cross": {
          "sc": "跨境架构的合规审查优先级提至最高；准备应对可能的监管查询。",
          "tc": "跨境架構的合規審查優先級提至最高；準備應對可能的監管查詢。"
        }
      },
      "source": {
        "sc": "Bloomberg · 独家报道 2026-06-15 [EN原文]",
        "tc": "Bloomberg · 独家报道 2026-06-15 [EN原文]",
        "lang": "zh"
      },
      "sourceTier": "media",
      "tags": {
        "sc": [
          "Bloomberg",
          "执法",
          "跨境"
        ],
        "tc": [
          "Bloomberg",
          "執法",
          "跨境"
        ]
      },
      "themes": [
        "reg",
        "compliance",
        "offshore"
      ],
      "rolesImpact": {
        "front": 2,
        "midback": 3,
        "lead": 3,
        "cross": 3
      },
      "publishedAt": "2026-06-15T08:41:00+08:00",
      "originalUrl": "https://www.bloomberg.com/news/articles/2026-06-15/hong-kong-insurance-regulator-vows-crackdown-on-rule-breakers",
      "sourceKey": "bloomberg",
      "boards": [
        "reg",
        "market"
      ],
      "contentKind": "press"
    },
    {
      "id": "ia-20260612-manulife-plans",
      "clusterCount": 1,
      "score": 73,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "title": {
        "sc": "宏利香港推出两款新分红终身寿险储蓄计划。",
        "tc": "宏利香港推出兩款新分紅終身壽險儲蓄計劃。"
      },
      "summary": {
        "sc": "2026年6月，宏利香港推出两款新的分红终身寿险储蓄计划，旨在满足客户对财务保障和长期储蓄的多元化需求。新产品主打灵活缴费选项及多货币配置功能，配合公司正在推进的AI驱动分销与客户服务升级。",
        "tc": "2026年6月，宏利香港推出兩款新的分紅終身壽險儲蓄計劃，旨在滿足客戶對財務保障和長期儲蓄的多元化需求。新產品主打靈活繳費選項及多貨幣配置功能，配合公司正在推進的AI驅動分銷與客戶服務升級。"
      },
      "why": {
        "sc": "宏利在产品与AI两端同时发力；产品线更新有助前线获客竞争力。",
        "tc": "宏利在產品與AI兩端同時發力；產品線更新有助前線獲客競爭力。"
      },
      "actions": {
        "front": {
          "sc": "了解新产品亮点并与现有竞品做对比分析。",
          "tc": "了解新產品亮點並與現有競品做對比分析。"
        },
        "midback": {
          "sc": "产品比较表更新宏利新产品参数。｜关注宏利AI工具对中介侧核保效率的影响。",
          "tc": "產品比較表更新宏利新產品參數。｜關注宏利AI工具對中介側核保效率的影響。"
        },
        "lead": {
          "sc": "团队培训需覆盖宏利新产品以保持市场敏感度。",
          "tc": "團隊培訓需覆蓋宏利新產品以保持市場敏感度。"
        },
        "cross": {
          "sc": "多货币选项适合跨境客户资产配置。",
          "tc": "多貨幣選項適合跨境客戶資產配置。"
        }
      },
      "source": {
        "sc": "宏利香港 · 产品发布 2026-06",
        "tc": "宏利香港 · 产品发布 2026-06",
        "lang": "zh"
      },
      "sourceTier": "insurer",
      "tags": {
        "sc": [
          "宏利",
          "分红险",
          "新产品"
        ],
        "tc": [
          "宏利",
          "分紅險",
          "新產品"
        ]
      },
      "themes": [
        "product",
        "firm"
      ],
      "rolesImpact": {
        "front": 2,
        "midback": 1,
        "lead": 2,
        "cross": 1
      },
      "publishedAt": "2026-06-12T11:00:00+08:00",
      "originalUrl": "https://www.manulife.com.hk/en/individual.html",
      "sourceKey": "manulife",
      "boards": [
        "insurer",
        "product"
      ],
      "contentKind": "product_notice"
    },
    {
      "id": "hk-20260612-fo-tax",
      "clusterCount": 1,
      "score": 87,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": true,
      "ingestedAt": "2026-07-29T00:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "港府2026年优化家族办公室税制：扩大免税范围至数字资产。",
        "tc": "港府2026年優化家族辦公室稅制：擴大免稅範圍至數字資產。"
      },
      "summary": {
        "sc": "港府2026年6月12日刊宪《2026年税务(修订)条例草案》，优化统一基金豁免制度。扩大合资格投资范围至贵金属、贷款、私募信贷及数字资产。强化经济实质要求，并引入税务申报机制。草案追溯至2025/26课税年度适用。[EN原文]",
        "tc": "港府優化家辦稅制:擴大至數字資產"
      },
      "why": {
        "sc": "家办税制升级，也是香港与新加坡竞争的关键一役。",
        "tc": "家辦稅制升級，也是港新競爭關鍵。"
      },
      "actions": {
        "front": {
          "sc": "家办客户可享0%利得税=税务筹划亮点",
          "tc": "家辦客戶享0%利得稅"
        },
        "midback": {
          "sc": "更新家办税务档案",
          "tc": "更新家辦稅務檔案"
        },
        "lead": {
          "sc": "税制优化=家办业务增量的政策基础",
          "tc": "稅制優化=家辦增量基礎"
        },
        "cross": {
          "sc": "跨境家办:香港税务+内地资产=最优解",
          "tc": "跨境家辦:香港稅務+內地資產=最優解"
        }
      },
      "source": {
        "sc": "港府宪报/China Briefing",
        "tc": "港府憲報/China Briefing",
        "lang": "en"
      },
      "boards": [
        "cross",
        "offshore"
      ],
      "tags": {
        "sc": [
          "家族办公室",
          "税制",
          "数字资产",
          "2026"
        ],
        "tc": [
          "家族辦公室",
          "稅制",
          "數位資產",
          "2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-06-12T10:00:00+08:00",
      "originalUrl": "https://www.china-briefing.com/news/hong-kong-fund-family-office-tax-reform-ufe-2026/",
      "sourceKey": "hk:fo-tax-20260612",
      "sourceTier": "media",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20260610-manulife-leverage",
      "clusterCount": 1,
      "score": 78,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "title": {
        "sc": "宏利香港据报暂停杠杆融资保单产品：监管关注与产品合规调整。",
        "tc": "宏利香港據報暫停槓桿融資保單產品：監管關注與產品合規調整。"
      },
      "summary": {
        "sc": "2026年6月，据Hubbis等媒体报道，宏利金融已暂停为香港高净值客户提供杠杆融资支持的保险产品。消息称该产品引起了监管机构和竞争对手的关注。宏利发言人表示公司定期审视保单服务并作为常规运营进行调适。",
        "tc": "2026年6月，據Hubbis等媒體報道，宏利金融已暫停為香港高淨值客戶提供槓桿融資支持的保險產品。消息稱該產品引起了監管機構和競爭對手的關注。宏利發言人表示公司定期審視保單服務並作為常規運營進行調適。"
      },
      "why": {
        "sc": "保费融资合规边界仍在收紧；保司主动调适产品以避免监管风险。",
        "tc": "保費融資合規邊界仍在收緊；保司主動調適產品以避免監管風險。"
      },
      "actions": {
        "front": {
          "sc": "对客勿主动推介杠杆融资方案；了解保费融资合规风险。",
          "tc": "對客勿主動推介槓桿融資方案；了解保費融資合規風險。"
        },
        "midback": {
          "sc": "审查公司保费融资/杠杆产品的合规性。｜更新客户沟通话术，避免误导。",
          "tc": "審查公司保費融資/槓桿產品的合規性。｜更新客戶溝通話術，避免誤導。"
        },
        "lead": {
          "sc": "杠杆产品销售策略需重新评估；关注竞品动向。",
          "tc": "槓桿產品銷售策略需重新評估；關注競品動向。"
        },
        "cross": {
          "sc": "跨境保费融资涉及多法域合规，风险更高。",
          "tc": "跨境保費融資涉及多法域合規，風險更高。"
        }
      },
      "source": {
        "sc": "Hubbis / 媒体报道 2026-06 [EN原文]",
        "tc": "Hubbis / 媒体报道 2026-06 [EN原文]",
        "lang": "zh"
      },
      "sourceTier": "insurer",
      "tags": {
        "sc": [
          "保费融资",
          "宏利",
          "产品合规"
        ],
        "tc": [
          "保費融資",
          "宏利",
          "產品合規"
        ]
      },
      "themes": [
        "product",
        "compliance",
        "firm"
      ],
      "rolesImpact": {
        "front": 2,
        "midback": 2,
        "lead": 2,
        "cross": 1
      },
      "publishedAt": "2026-06-10T14:00:00+08:00",
      "originalUrl": "https://www.hubbis.com/news/manulife-pulls-leveraged-insurance-loan-product-for-wealthy-hong-kong-clients",
      "sourceKey": "manulife",
      "boards": [
        "insurer",
        "product",
        "reg"
      ],
      "contentKind": "market_data"
    },
    {
      "id": "ia-20260610-chowtaifook-life",
      "clusterCount": 1,
      "score": 72,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "title": {
        "sc": "周大福人寿品牌升级：CTFS半年报金融板块AOP同比增19%。",
        "tc": "周大福人壽品牌升級：CTFS半年報金融板塊AOP同比增19%。"
      },
      "summary": {
        "sc": "2026年6月，周大福人寿（原富通保险FTLife）品牌升级持续推进。母公司CTFS发布FY2026半年报，金融板块调整后营运利润同比增19%至7.288亿港元，市场占有率提升至2.7%。Fitch评级指出周大福品牌协同效应对香港保险市场份额扩展有正面作用。",
        "tc": "2026年6月，周大福人壽（原富通保險FTLife）品牌升級持續推進。母公司CTFS發布FY2026半年報，金融板塊調整後營運利潤同比增19%至7.288億港元，市場佔有率提升至2.7%。Fitch評級指出周大福品牌協同效應對香港保險市場份額擴展有正面作用。"
      },
      "why": {
        "sc": "周大福品牌赋能下保险板块业绩亮眼；中型保司在港险市场的差异化竞争值得关注。",
        "tc": "周大福品牌賦能下保險板塊業績亮眼；中型保司在港險市場的差異化競爭值得關注。"
      },
      "actions": {
        "front": {
          "sc": "了解周大福人寿产品线与品牌定位的变化。",
          "tc": "了解周大福人壽產品線與品牌定位的變化。"
        },
        "midback": {
          "sc": "更新保司评估中周大福人寿的财务数据与品牌认知。",
          "tc": "更新保司評估中周大福人壽的財務數據與品牌認知。"
        },
        "lead": {
          "sc": "中型保司品牌升级为团队提供差异化获客角度。",
          "tc": "中型保司品牌升級為團隊提供差異化獲客角度。"
        },
        "cross": {
          "sc": "周大福内地品牌认知度可助力跨境客户获取。",
          "tc": "周大福內地品牌認知度可助力跨境客戶獲取。"
        }
      },
      "source": {
        "sc": "CTFS · 半年报 / Fitch 2026-06",
        "tc": "CTFS · 半年报 / Fitch 2026-06",
        "lang": "zh"
      },
      "sourceTier": "insurer",
      "tags": {
        "sc": [
          "周大福",
          "品牌升级",
          "市场占有率"
        ],
        "tc": [
          "周大福",
          "品牌升級",
          "市場佔有率"
        ]
      },
      "themes": [
        "firm",
        "market"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 1,
        "lead": 2,
        "cross": 2
      },
      "publishedAt": "2026-06-10T12:00:00+08:00",
      "originalUrl": "https://www.ctfs.com.hk/media-hub/press-releases/2026/FY2026_Interim_Results",
      "sourceKey": "ctf-life",
      "boards": [
        "insurer",
        "market"
      ],
      "contentKind": "industry_news"
    },
    {
      "id": "ctflife-2026-diamond-iul",
      "clusterCount": 1,
      "score": 84,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": false,
      "ingestedAt": "2026-07-28T16:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "周大福人寿推出全港首只法国巴黎银行指数挂钩IUL计划「钻裕」",
        "tc": "周大福人壽推出全港首隻法國巴黎銀行指數掛鈎IUL計劃「鑽裕」"
      },
      "summary": {
        "sc": "周大福人寿推出「钻裕」指数型万用保险计划(IUL)，专为专业投资者设计，首次将法国巴黎银行指数引入香港IUL市场。",
        "tc": "周大福推出法國巴黎銀行指數掛鈎IUL"
      },
      "why": {
        "sc": "IUL市场创新者，也是周大福的差异化武器。",
        "tc": "IUL市場創新。"
      },
      "actions": {
        "front": {
          "sc": "专业投资者客户可了解IUL新产品",
          "tc": "專業投資者了解IUL"
        },
        "midback": {
          "sc": "更新IUL产品对比",
          "tc": "更新IUL對比"
        },
        "lead": {
          "sc": "IUL产品线扩充策略",
          "tc": "IUL產品策略"
        },
        "cross": {
          "sc": "跨境专业投资者的IUL方案",
          "tc": "跨境專業投資者IUL"
        }
      },
      "source": {
        "sc": "周大福/ACN",
        "tc": "周大福/ACN",
        "lang": "zh"
      },
      "boards": [
        "product",
        "firm"
      ],
      "tags": {
        "sc": [
          "周大福",
          "IUL",
          "钻裕",
          "法国巴黎银行"
        ],
        "tc": [
          "周大福",
          "IUL",
          "鑽裕",
          "法國巴黎銀行"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-06-10T10:00:00+08:00",
      "originalUrl": "https://www.acnnewswire.com/press-release/traditionalchinese/107208/",
      "sourceKey": "ctflife:diamond-iul-2026",
      "sourceTier": "media",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20260609-fitch-apac",
      "clusterCount": 1,
      "score": 75,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "title": {
        "sc": "惠誉：亚太保险展望维持「中性」，监管与市场压力并存。",
        "tc": "惠譽：亞太保險展望維持「中性」，監管與市場壓力並存。"
      },
      "summary": {
        "sc": "2026年6月9日，惠誉评级发布亚太保险业展望报告，维持「中性」评级。指出香港市场受佣金分摊新规、转介费上限及演示利率上限等监管措施影响，短期内对保费增长和渠道盈利构成压力；但长期有利于行业健康度与客户公平待对。",
        "tc": "2026年6月9日，惠譽評級發布亞太保險業展望報告，維持「中性」評級。指出香港市場受佣金分攤新規、轉介費上限及演示利率上限等監管措施影響，短期內對保費增長和渠道盈利構成壓力；但長期有利於行業健康度與客戶公平待對。"
      },
      "why": {
        "sc": "国际评级机构首次正面评价香港佣金改革长期影响；中介应视合规为护城河而非负担。",
        "tc": "國際評級機構首次正面評價香港佣金改革長期影響；中介應視合規為護城河而非負擔。"
      },
      "actions": {
        "front": {
          "sc": "对客可引用评级机构观点说明行业正走向更可持续。",
          "tc": "對客可引用評級機構觀點說明行業正走向更可持續。"
        },
        "midback": {
          "sc": "将评级报告纳入公司年度合规与战略文件。｜佣金模式转型期注意现金流规划。",
          "tc": "將評級報告納入公司年度合規與戰略文件。｜佣金模式轉型期注意現金流規劃。"
        },
        "lead": {
          "sc": "行业转型信号：短期阵痛换取长期健康市场。",
          "tc": "行業轉型信號：短期陣痛換取長期健康市場。"
        },
        "cross": {
          "sc": "国际评级有助于跨境业务可信度。",
          "tc": "國際評級有助於跨境業務可信度。"
        }
      },
      "source": {
        "sc": "惠誉评级 · 行业展望 2026-06-09 [EN原文]",
        "tc": "惠誉评级 · 行业展望 2026-06-09 [EN原文]",
        "lang": "zh"
      },
      "sourceTier": "research",
      "tags": {
        "sc": [
          "评级",
          "行业展望",
          "监管影响"
        ],
        "tc": [
          "評級",
          "行業展望",
          "監管影響"
        ]
      },
      "themes": [
        "reg",
        "market",
        "macro"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 2,
        "lead": 2,
        "cross": 1
      },
      "publishedAt": "2026-06-09T15:00:00+08:00",
      "originalUrl": "https://www.fitchratings.com/research/insurance/apac-insurance-outlook-stays-neutral-amid-regulatory-market-pressure-09-06-2026",
      "sourceKey": "fitch",
      "boards": [
        "market",
        "reg"
      ],
      "contentKind": "research"
    },
    {
      "id": "ia-20260608-axa-global-private",
      "clusterCount": 1,
      "score": 82,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "title": {
        "sc": "AXA安盛推出「AXA Global Private」高净值统一平台，落户香港及百慕达。",
        "tc": "AXA安盛推出「AXA Global Private」高淨值統一平台，落戶香港及百慕達。"
      },
      "summary": {
        "sc": "2026年6月8日，AXA集团宣布推出AXA Global Private高净值统一平台，以香港及百慕达为双枢纽，整合寿险、财富管理、传承规划及艺术品/绑架赎金等特殊险种，服务亚洲HNW/UHNW家庭。行政总裁Thomas Buberl出席香港发布会。",
        "tc": "2026年6月8日，AXA集團宣布推出AXA Global Private高淨值統一平台，以香港及百慕達為雙樞紐，整合壽險、財富管理、傳承規劃及藝術品/綁架贖金等特殊險種，服務亞洲HNW/UHNW家庭。行政總裁Thomas Buberl出席香港發布會。"
      },
      "why": {
        "sc": "全球保险巨头加码香港HNW赛道；香港超越瑞士成最大离岸财富中心背景下，平台差异化价值突出。",
        "tc": "全球保險巨頭加碼香港HNW賽道；香港超越瑞士成最大離岸財富中心背景下，平台差異化價值突出。"
      },
      "actions": {
        "front": {
          "sc": "高净值客户可关注AXA多司法管辖区保单方案。",
          "tc": "高淨值客戶可關注AXA多司法管轄區保單方案。"
        },
        "midback": {
          "sc": "了解AXA平台产品线与自家产品定位差异。｜跨境保单涉及香港/百慕达双法域合规。",
          "tc": "了解AXA平台產品線與自家產品定位差異。｜跨境保單涉及香港/百慕達雙法域合規。"
        },
        "lead": {
          "sc": "高净值团队可将此作为竞品研究和市场定位参考。",
          "tc": "高淨值團隊可將此作為競品研究和市場定位參考。"
        },
        "cross": {
          "sc": "百慕达保单架构为跨境客户提供多一选择。",
          "tc": "百慕達保單架構為跨境客戶提供多一選擇。"
        }
      },
      "source": {
        "sc": "AXA安盛 · 新闻稿 2026-06-08",
        "tc": "AXA安盛 · 新闻稿 2026-06-08",
        "lang": "zh"
      },
      "sourceTier": "media",
      "tags": {
        "sc": [
          "高净值",
          "AXA",
          "财富管理"
        ],
        "tc": [
          "高淨值",
          "AXA",
          "財富管理"
        ]
      },
      "themes": [
        "product",
        "offshore",
        "firm"
      ],
      "rolesImpact": {
        "front": 2,
        "midback": 1,
        "lead": 2,
        "cross": 3
      },
      "publishedAt": "2026-06-08T17:00:00+08:00",
      "originalUrl": "https://fortune.com/2026/06/08/axa-launches-global-private-hong-kong-china-hnwi-insurance/",
      "sourceKey": "fortune",
      "boards": [
        "insurer",
        "family",
        "product"
      ],
      "contentKind": "product_notice"
    },
    {
      "id": "aia-20260608-prosperlife",
      "clusterCount": 1,
      "score": 82,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T16:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "友邦推出「财富盈活储蓄保险计划」瞄准高净值家庭传承。",
        "tc": "友邦推出「財富盈活儲蓄保險計劃」瞄準高淨值家庭傳承。"
      },
      "summary": {
        "sc": "友邦香港2026年6月8日推出「财富盈活储蓄保险计划」(ProsperLife)，专为高净值家庭设计，涵盖跨代传承、灵活资金配置及动态财富规划功能。",
        "tc": "友邦6月8日推出高淨值家庭傳承計劃"
      },
      "why": {
        "sc": "高净值市场新产品，与保诚/宏利形成三强竞争。",
        "tc": "高淨值新產品。"
      },
      "actions": {
        "front": {
          "sc": "了解ProsperLife与竞品对比，更新产品手册",
          "tc": "更新產品手冊"
        },
        "midback": {
          "sc": "收集产品费率与条款",
          "tc": "收集產品資料"
        },
        "lead": {
          "sc": "评估在高净值客户组合中的定位",
          "tc": "評估產品定位"
        },
        "cross": {
          "sc": "跨境高净值客户的传承方案对比",
          "tc": "跨境傳承方案對比"
        }
      },
      "source": {
        "sc": "AIA 新闻稿",
        "tc": "AIA 新聞稿",
        "lang": "zh"
      },
      "boards": [
        "product",
        "firm"
      ],
      "tags": {
        "sc": [
          "AIA",
          "财富盈活",
          "高净值",
          "传承"
        ],
        "tc": [
          "AIA",
          "財富盈活",
          "高淨值",
          "傳承"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-06-08T10:00:00+08:00",
      "originalUrl": "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/2026/aia-press-release-20260608",
      "sourceKey": "aia",
      "sourceTier": "insurer",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20260608-aia-wealth-flexi",
      "clusterCount": 1,
      "score": 80,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "title": {
        "sc": "友邦推出「 Wealth Flexi 灵活储蓄保」：首创未来心愿安排服务高净值家庭传承。",
        "tc": "友邦推出「 Wealth Flexi 靈活儲蓄保」：首創未來心願安排服務高淨值家庭傳承。"
      },
      "summary": {
        "sc": "2026年6月8日，友邦香港推出Wealth Flexi灵活储蓄保（分红终身寿险），首创「未来心愿安排」增值服务，允许保单持有人在身故或健康受损等事件发生时预先设定保单管理指令，涵盖拥有权继承、利益分配及受益人指定等，配合货币转换、红利锁定/解锁等灵活功能。",
        "tc": "2026年6月8日，友邦香港推出Wealth Flexi靈活儲蓄保（分紅終身壽險），首創「未來心願安排」增值服務，允許保單持有人在身故或健康受損等事件發生時預先設定保單管理指令，涵蓋擁有權繼承、利益分配及受益人指定等，配合貨幣轉換、紅利鎖定/解鎖等靈活功能。"
      },
      "why": {
        "sc": "友邦AIHOT数据显示仅25%HNW家庭已做传承安排；产品精准切入信任与结构化传承空缺。",
        "tc": "友邦AIHOT數據顯示僅25%HNW家庭已做傳承安排；產品精準切入信任與結構化傳承空缺。"
      },
      "actions": {
        "front": {
          "sc": "高净值客户做传承规划时可推荐此产品作为结构化方案。",
          "tc": "高淨值客戶做傳承規劃時可推薦此產品作為結構化方案。"
        },
        "midback": {
          "sc": "产品比较时注意传承功能的差异化。｜了解受益人安排与信托衔接可行性。",
          "tc": "產品比較時注意傳承功能的差異化。｜了解受益人安排與信託銜接可行性。"
        },
        "lead": {
          "sc": "高净值团队的竞品对标与新业务增长机会。",
          "tc": "高淨值團隊的競品對標與新增長機會。"
        },
        "cross": {
          "sc": "跨境传承架构可配合信托+保单方案。",
          "tc": "跨境傳承架構可配合信託+保單方案。"
        }
      },
      "source": {
        "sc": "友邦香港 · 新闻稿 2026-06-08",
        "tc": "友邦香港 · 新闻稿 2026-06-08",
        "lang": "zh"
      },
      "sourceTier": "insurer",
      "tags": {
        "sc": [
          "高净值",
          "传承",
          "友邦"
        ],
        "tc": [
          "高淨值",
          "傳承",
          "友邦"
        ]
      },
      "themes": [
        "product",
        "offshore",
        "family"
      ],
      "rolesImpact": {
        "front": 2,
        "midback": 1,
        "lead": 2,
        "cross": 3
      },
      "publishedAt": "2026-06-08T10:00:00+08:00",
      "originalUrl": "https://www.aia.com.hk/en/about-aia/about-us/media-centre/press-releases/2026/aia-press-release-20260608",
      "sourceKey": "aia",
      "boards": [
        "insurer",
        "product",
        "family"
      ],
      "contentKind": "product_notice"
    },
    {
      "id": "ia-20260605-hkma-remuneration-circ",
      "clusterCount": 1,
      "score": 86,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "title": {
        "sc": "金管局发布银行保险中介分红报酬结构通函（平行通函）。",
        "tc": "金管局發布銀行保險中介分紅報酬結構通函（平行通函）。"
      },
      "summary": {
        "sc": "2026年6月5日，金管局发布《持牌保险中介人（属认可机构）就具定期缴款条款的分红保单的报酬结构》通函，与保监局同日通函平行发布。要求银行作为持牌保险中介销售分红保单时，须采用与保监局实务指引一致的佣金分摊安排。",
        "tc": "2026年6月5日，金管局發布《持牌保險中介人（屬認可機構）就具定期繳款條款的分紅保單的報酬結構》通函，與保監局同日通函平行發布。要求銀行作為持牌保險中介銷售分紅保單時，須採用與保監局實務指引一致的佣金分攤安排。"
      },
      "why": {
        "sc": "这是金管局首次单独发布保险报酬结构通函，银保与经纪规则趋同已成定局。",
        "tc": "這是金管局首次單獨發布保險報酬結構通函，銀保與經紀規則趨同已成定局。"
      },
      "actions": {
        "front": {
          "sc": "对客比较时勿用「银行佣金更高/更低」等未经核实说法。",
          "tc": "對客比較時勿用「銀行佣金更高/更低」等未經核實說法。"
        },
        "midback": {
          "sc": "立即检查与银行渠道的合作协议是否与新通函冲突。",
          "tc": "立即檢查與銀行渠道的合作協議是否與新通函衝突。"
        },
        "lead": {
          "sc": "银保与经纪激励规则趋同后，竞争回到专业服务。",
          "tc": "銀保與經紀激勵規則趨同後，競爭回到專業服務。"
        },
        "cross": {
          "sc": "私行协作注意机构侧报酬披露要求。",
          "tc": "私行協作注意機構側報酬披露要求。"
        }
      },
      "source": {
        "sc": "金管局 · 通函 2026-06-05 [EN原文]",
        "tc": "金管局 · 通函 2026-06-05 [EN原文]",
        "lang": "zh"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "金管局",
          "银保",
          "报酬结构"
        ],
        "tc": [
          "金管局",
          "銀保",
          "報酬結構"
        ]
      },
      "themes": [
        "reg",
        "channel",
        "compliance"
      ],
      "rolesImpact": {
        "front": 2,
        "midback": 3,
        "lead": 3,
        "cross": 2
      },
      "publishedAt": "2026-06-05T16:00:00+08:00",
      "originalUrl": "https://brdr.hkma.gov.hk/eng/doc-ldg/docId/getPdf/20260602-4-EN/Remuneration%20structures%20for%20licensed%20insurance%20intermediaries%20which%20are%20AIs.pdf",
      "sourceKey": "hkma",
      "boards": [
        "reg",
        "market"
      ],
      "contentKind": "circular"
    },
    {
      "id": "ia-hkma-remuneration-20260605",
      "title": {
        "sc": "保监局提请业界注意：金管局关于银行保险中介分红报酬结构通函。",
        "tc": "保監局提請業界注意：金管局關於銀行保險中介分紅報酬結構通函。"
      },
      "summary": {
        "sc": "2026年6月5日，保监局发通函提请业界注意金管局同日通函《持牌保险中介人（属认可机构）就具定期缴款条款的分红保单的报酬结构》。银行渠道的分红报酬亦纳入与「公平待客」一致的分摊逻辑。",
        "tc": "2026年6月5日，保監局發通函提請業界注意金管局同日通函《持牌保險中介人（屬認可機構）就具定期繳款條款的分紅保單的報酬結構》。銀行渠道的分紅報酬亦納入與「公平待客」一致的分攤邏輯。"
      },
      "why": {
        "sc": "银保与经纪激励规则趋同，竞争会更多回到专业服务与产品适配。",
        "tc": "銀保與經紀激勵規則趨同，競爭會更多回到專業服務與產品適配。"
      },
      "actions": {
        "front": {
          "sc": "对客比较时勿用「银行一定更优/更差佣」类未经核实说法。",
          "tc": "對客比較時勿用「銀行一定更優/更差傭」類未經核實說法。"
        },
        "midback": {
          "sc": "渠道策略材料更新银保规则变化。｜若公司有银行合作/转介，检查协议是否与新通函冲突。",
          "tc": "渠道策略材料更新銀保規則變化。｜若公司有銀行合作/轉介，檢查協議是否與新通函衝突。"
        },
        "lead": {
          "sc": "观察银保产能与我们经纪产能的此消彼长。",
          "tc": "觀察銀保產能與我們經紀產能的此消彼長。"
        },
        "cross": {
          "sc": "私行协作单注意机构侧报酬披露要求。",
          "tc": "私行協作單注意機構側報酬披露要求。"
        }
      },
      "source": {
        "sc": "保监局通函 2026-06-05 / 金管局平行通函",
        "tc": "保監局通函 2026-06-05 / 金管局平行通函"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "银保",
          "报酬结构",
          "金管局"
        ],
        "tc": [
          "銀保",
          "報酬結構",
          "金管局"
        ]
      },
      "themes": [
        "reg",
        "channel",
        "compliance"
      ],
      "rolesImpact": {
        "front": 2,
        "midback": 3,
        "lead": 3,
        "cross": 2
      },
      "publishedAt": "2026-06-05T12:00:00+08:00",
      "score": 89,
      "verifyStatus": "verified",
      "originalUrl": "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/files/Cir_dd_05.06.2026_Circular_on_HKMA_Circular_on_Remuneration_Structures_for_AIs.pdf",
      "featured": true,
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "market",
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "ia-20260605-hkma-commission",
      "clusterCount": 1,
      "score": 86,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:30:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "金管局就银行保险中介佣金分摊发出通函。",
        "tc": "金管局就銀行保險中介佣金分攤發出通函。"
      },
      "summary": {
        "sc": "金管局2026年6月5日发出通函，就银行在保险中介角色中的佣金分摊安排提出监管期望。银行须确保分红保单佣金在不少于5年内均匀分摊，首年不超过总额70%。[EN原文]",
        "tc": "金管局6月5日就銀行保險佣金分攤發出通函"
      },
      "why": {
        "sc": "银保渠道佣金分摊规则与经纪渠道趋同，行业合规标准进一步统一。",
        "tc": "銀保佣金分攤與經紀渠道趨同。"
      },
      "actions": {
        "front": {
          "sc": "银行渠道分红保单签单时提示佣金分摊政策",
          "tc": "簽單時提示佣金分攤政策"
        },
        "midback": {
          "sc": "更新银保渠道合规清单",
          "tc": "更新銀保渠道合規清單"
        },
        "lead": {
          "sc": "银保与经纪渠道佣金规则对比分析",
          "tc": "銀保與經紀佣金規則對比"
        },
        "cross": {
          "sc": "跨境客户的银保产品需满足两地分摊要求",
          "tc": "跨境銀保產品需滿足兩地要求"
        }
      },
      "source": {
        "sc": "HKMA 通函",
        "tc": "HKMA 通函",
        "lang": "en"
      },
      "boards": [
        "regulatory",
        "compliance",
        "channel"
      ],
      "tags": {
        "sc": [
          "金管局",
          "佣金分摊",
          "银保",
          "通函"
        ],
        "tc": [
          "金管局",
          "佣金分攤",
          "銀保",
          "通函"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-06-05T10:00:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/news/hong-kong-insurance-authority-tightens-commission-rules-hkma-raises-pressure",
      "sourceKey": "insuranceasia",
      "sourceTier": "pro",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20260611-chubb-life",
      "clusterCount": 1,
      "score": 62,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "title": {
        "sc": "安达人寿香港增强旗舰储蓄计划：新增3年缴付选项。",
        "tc": "安達人壽香港增強旗艦儲蓄計劃：新增3年繳付選項。"
      },
      "summary": {
        "sc": "2026年6月初，安达人寿（Chubb Life）香港增强其旗舰储蓄保险计划，新增3年缴付选项以满足客户对短年期缴费的需求。此举是保司在分红险市场竞争加剧背景下，通过产品灵活性争夺市场份额的策略。",
        "tc": "2026年6月初，安達人壽（Chubb Life）香港增強其旗艦儲蓄保險計劃，新增3年繳付選項以滿足客戶對短年期繳費的需求。此舉是保司在分紅險市場競爭加劇背景下，通過產品靈活性爭奪市場份額的策略。"
      },
      "why": {
        "sc": "短年期缴费选项成为分红险产品差异化新方向；安达的灵活策略有借鉴意义。",
        "tc": "短年期繳費選項成為分紅險產品差異化新方向；安達的靈活策略有借鑑意義。"
      },
      "actions": {
        "front": {
          "sc": "客户偏好短年期时可推荐安达新产品作为选项。",
          "tc": "客戶偏好短年期時可推薦安達新產品作為選項。"
        },
        "midback": {
          "sc": "产品比较表中更新安达新产品参数。",
          "tc": "產品比較表中更新安達新產品參數。"
        },
        "lead": {
          "sc": "了解竞品产品策略以优化自有产品组合。",
          "tc": "了解競品產品策略以優化自有產品組合。"
        },
        "cross": {
          "sc": "短年期产品更适合有资金出境时限的跨境客户。",
          "tc": "短年期產品更適合有資金出境時限的跨境客戶。"
        }
      },
      "source": {
        "sc": "亚洲保险评论 · 产品新闻 2026-06-04 [EN原文]",
        "tc": "亚洲保险评论 · 产品新闻 2026-06-04 [EN原文]",
        "lang": "zh"
      },
      "sourceTier": "pro",
      "tags": {
        "sc": [
          "安达人寿",
          "储蓄险",
          "短年期"
        ],
        "tc": [
          "安達人壽",
          "儲蓄險",
          "短年期"
        ]
      },
      "themes": [
        "product",
        "firm"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 1,
        "lead": 1,
        "cross": 1
      },
      "publishedAt": "2026-06-04T14:00:00+08:00",
      "originalUrl": "https://www.asiainsurancereview.com/Search?search_key=News",
      "sourceKey": "asiainsurancereview",
      "boards": [
        "insurer",
        "product"
      ],
      "contentKind": "product_notice"
    },
    {
      "id": "ia-20260603-broker-referral",
      "clusterCount": 1,
      "score": 85,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "title": {
        "sc": "保监局对两间经纪公司施加续牌条件：暂停接收转介客户。",
        "tc": "保監局對兩間經紀公司施加續牌條件：暫停接收轉介客戶。"
      },
      "summary": {
        "sc": "2026年6月初，保监局对两间未能有效管控转介活动的保险经纪公司施加续牌条件，要求暂停接收转介业务。这是转介费50%上限规定自2025年10月生效后首次公开执法。",
        "tc": "2026年6月初，保監局對兩間未能有效管控轉介活動的保險經紀公司施加續牌條件，要求暫停接收轉介業務。這是轉介費50%上限規定自2025年10月生效後首次公開執法。"
      },
      "why": {
        "sc": "中介转介合规进入执法阶段；监管零容忍信号明确。",
        "tc": "中介轉介合規進入執法階段；監管零容忍信號明確。"
      },
      "actions": {
        "front": {
          "sc": "检查自有转介安排是否合规；勿超50%上限。",
          "tc": "檢查自有轉介安排是否合規；勿超50%上限。"
        },
        "midback": {
          "sc": "立即审查公司转介协议与费用比例。｜更新转介业务SOP以匹配新规。",
          "tc": "立即審查公司轉介協議與費用比例。｜更新轉介業務SOP以匹配新規。"
        },
        "lead": {
          "sc": "转介业务为团队主要获客渠道时需重新评估可持续性。",
          "tc": "轉介業務為團隊主要獲客渠道時需重新評估可持續性。"
        },
        "cross": {
          "sc": "跨境转介需额外注意两地监管合规。",
          "tc": "跨境轉介需額外注意兩地監管合規。"
        }
      },
      "source": {
        "sc": "保监局 · 执法行动 2026-06",
        "tc": "保监局 · 执法行动 2026-06",
        "lang": "zh"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "转介费",
          "经纪合规",
          "执法"
        ],
        "tc": [
          "轉介費",
          "經紀合規",
          "執法"
        ]
      },
      "themes": [
        "reg",
        "channel",
        "compliance"
      ],
      "rolesImpact": {
        "front": 2,
        "midback": 3,
        "lead": 3,
        "cross": 2
      },
      "publishedAt": "2026-06-03T10:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/en/infocenter/speeches_articles/20260712.html",
      "sourceKey": "ia",
      "boards": [
        "reg",
        "market"
      ],
      "contentKind": "enforcement"
    },
    {
      "id": "ia-20260602-hkma-crossborder",
      "clusterCount": 1,
      "score": 72,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "title": {
        "sc": "金管局举办银保跨境业务简报会：促进银行与保险业界合作。",
        "tc": "金管局舉辦銀保跨境業務簡報會：促進銀行與保險業界合作。"
      },
      "summary": {
        "sc": "2026年6月2日，金管局与香港银行公会联合举办跨境银行与保险业务简报会，覆盖约3,500名高管。重点讨论银保渠道跨境合规、客户保护及行业协作框架。",
        "tc": "2026年6月2日，金管局與香港銀行公會聯合舉辦跨境銀行與保險業務簡報會，覆蓋約3,500名高管。重點討論銀保渠道跨境合規、客戶保護及行業協作框架。"
      },
      "why": {
        "sc": "银保渠道在跨境保单中的角色日益重要，监管前移协作信号明确。",
        "tc": "銀保渠道在跨境保單中的角色日益重要，監管前移協作信號明確。"
      },
      "actions": {
        "front": {
          "sc": "了解银保合规框架，避免在银行转介场景踩线。",
          "tc": "了解銀保合規框架，避免在銀行轉介場景踩線。"
        },
        "midback": {
          "sc": "梳理与银行合作/转介流程是否合规。｜检查银行渠道佣金披露与新通函对齐。",
          "tc": "梳理與銀行合作/轉介流程是否合規。｜檢查銀行渠道佣金披露與新通函對齊。"
        },
        "lead": {
          "sc": "评估银保渠道作为增长引擎的战略定位。",
          "tc": "評估銀保渠道作為增長引擎的戰略定位。"
        },
        "cross": {
          "sc": "私行协作需确保机构侧合规披露到位。",
          "tc": "私行協作需確保機構側合規披露到位。"
        }
      },
      "source": {
        "sc": "金管局 · 简报会 2026-06-02",
        "tc": "金管局 · 简报会 2026-06-02",
        "lang": "zh"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "银保",
          "跨境合规",
          "金管局"
        ],
        "tc": [
          "銀保",
          "跨境合規",
          "金管局"
        ]
      },
      "themes": [
        "reg",
        "channel",
        "compliance"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 2,
        "lead": 2,
        "cross": 2
      },
      "publishedAt": "2026-06-02T16:00:00+08:00",
      "originalUrl": "https://www.hkma.gov.hk/eng/news-and-media/speeches/2026/06/20260602-1/",
      "sourceKey": "hkma",
      "boards": [
        "reg",
        "market"
      ],
      "contentKind": "speech"
    },
    {
      "id": "deloitte-2026-insurance-outlook",
      "clusterCount": 1,
      "score": 84,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T19:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "德勤2026全球保险展望：AI落地加速 香港保监局推AI促进计划。",
        "tc": "德勤2026全球保險展望：AI落地加速 香港保監局推AI促進計劃。"
      },
      "summary": {
        "sc": "德勤2026年全球保险展望报告指出，AI成功依赖数据质量与系统现代化。香港保监局推出AI加速器与沙盒促进计划，新加坡金管局也提供AI资助。保险公司在AI客服和理赔自动分类上已有多项落地。[EN原文]",
        "tc": "德勤：AI落地加速，香港推AI促進計劃"
      },
      "why": {
        "sc": "四大咨询的行业技术趋势，也是保险科技投资方向。",
        "tc": "四大諮詢行業技術趨勢。"
      },
      "actions": {
        "front": {
          "sc": "了解AI在核保中的应用进展",
          "tc": "了解AI核保進展"
        },
        "midback": {
          "sc": "关注AI对合规流程的影响",
          "tc": "關注AI合規影響"
        },
        "lead": {
          "sc": "AI技术投资优先级判断",
          "tc": "AI投資優先級"
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "Deloitte Insights",
        "tc": "Deloitte Insights",
        "lang": "en"
      },
      "boards": [
        "intl",
        "tech"
      ],
      "tags": {
        "sc": [
          "德勤",
          "AI",
          "保险科技",
          "展望",
          "2026"
        ],
        "tc": [
          "德勤",
          "AI",
          "保險科技",
          "展望",
          "2026"
        ]
      },
      "contentKind": "report",
      "publishedAt": "2026-06-01T10:00:00+08:00",
      "originalUrl": "https://www.deloitte.com/us/en/insights/industry/financial-services/financial-services-industry-outlooks/insurance-industry-outlook.html",
      "sourceKey": "deloitte:insurance-outlook-2026",
      "sourceTier": "media",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "chubb-20260601-mylegacy",
      "clusterCount": 1,
      "score": 80,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T17:30:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "Chubb Life香港增强旗舰产品MyLegacy V——缩短回本期。",
        "tc": "Chubb Life香港增強旗艦產品MyLegacy V——縮短回本期。"
      },
      "summary": {
        "sc": "Chubb Life香港2026年6月1日增强旗舰产品MyLegacy V保险计划，缩短保单回本期，提升产品竞争力。同时Bloomberg金融机构2026评选获五项大奖。[EN原文]",
        "tc": "Chubb增強MyLegacy V，縮短回本期"
      },
      "why": {
        "sc": "Chubb在香港寿险市场持续加码，产品竞争力提升。",
        "tc": "Chubb香港壽險持續加碼。"
      },
      "actions": {
        "front": {
          "sc": "了解MyLegacy V与竞品对比",
          "tc": "了解產品對比"
        },
        "midback": {
          "sc": "更新Chubb产品库",
          "tc": "更新產品庫"
        },
        "lead": {
          "sc": "关注Chubb市场份额变化",
          "tc": "關注市佔率變化"
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "Chubb新闻稿",
        "tc": "Chubb新聞稿",
        "lang": "en"
      },
      "boards": [
        "product",
        "firm"
      ],
      "tags": {
        "sc": [
          "Chubb",
          "MyLegacy",
          "产品更新",
          "2026"
        ],
        "tc": [
          "Chubb",
          "MyLegacy",
          "產品更新",
          "2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-06-01T10:00:00+08:00",
      "originalUrl": "https://www.chubb.com/hk-en/media-center/life-insurance-news-releases.html",
      "sourceKey": "chubb",
      "sourceTier": "insurer",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "hkma-wealthconnect-2026",
      "clusterCount": 1,
      "score": 77,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "hkma",
      "title": {
        "sc": "跨境理财通2.0：南向通个人额度300万，产品扩至中高风险",
        "tc": "跨境理財通2.0：南向通個人額度300萬，產品擴至中高風險"
      },
      "summary": {
        "sc": "金管局推跨境理财通 2.0 升级：南向通个人投资额度提升至 300 万元人民币，合资格产品范围扩展至中高风险等级。这是大湾区金融互联互通深化的标志性一步，也将间接推动跨境保险产品的制度对接。",
        "tc": "金管局推跨境理財通 2.0 升級：南向通個人投資額度提升至 300 萬元人民幣，合資格產品範圍擴展至中高風險等級。這是大灣區金融互聯互通深化的標誌性一步，也將間接推動跨境保險產品的制度對接。"
      },
      "why": {
        "sc": "理财通2.0是跨境保险的「近亲」——额度提升和产品扩容说明制度壁垒在系统性降低。理财通的每一步制度突破，都为「保险通」铺了一寸路。",
        "tc": "理財通2.0是跨境保險的「近親」——額度提升和產品擴容說明制度壁壘在系統性降低。理財通的每一步制度突破，都為「保險通」鋪了一寸路。"
      },
      "actions": {
        "front": {
          "sc": "理财通客户与保险客户高度重叠，可交叉推荐",
          "tc": "理財通客戶與保險客戶高度重疊，可交叉推薦"
        },
        "midback": {
          "sc": "理财通2.0的额度/产品规则值得对标分析",
          "tc": "理財通2.0的額度/產品規則值得對標分析"
        },
        "lead": {
          "sc": "跨境金融互联互通是长期趋势，提前布局",
          "tc": "跨境金融互聯互通是長期趨勢，提前佈局"
        },
        "cross": {
          "sc": "理财通2.0是保险通的前站信号",
          "tc": "理財通2.0是保險通的前站信號"
        }
      },
      "rolesImpact": {
        "front": 3,
        "midback": 3,
        "lead": 4,
        "cross": 4
      },
      "source": {
        "sc": "HKMA 金管局",
        "lang": "zh"
      },
      "boards": [
        "market",
        "family"
      ],
      "themes": [
        "offshore",
        "macro"
      ],
      "tags": {
        "sc": [
          "理财通",
          "大湾区",
          "跨境"
        ],
        "tc": [
          "理財通",
          "大灣區",
          "跨境"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2026-06-01T10:00:00+08:00",
      "originalUrl": "https://www.hkma.gov.hk/eng/key-functions/international-financial-centre/wealth-management-connect/"
    },
    {
      "id": "ia-20260529-onsite-findings",
      "title": {
        "sc": "保司现场操守巡查常见问题与最佳实务（2026-05-29）。",
        "tc": "保司現場操守巡查常見問題與最佳實務（2026-05-29）。"
      },
      "summary": {
        "sc": "保监局2026年5月29日通函汇总对保险公司现场操守巡查的常见发现，并给出建议最佳实务。主题通常覆盖销售过程管控、记录留存、投诉处理与内控。",
        "tc": "保監局2026年5月29日通函彙總對保險公司現場操守巡查的常見發現，並給出建議最佳實務。主題通常覆蓋銷售過程管控、記錄留存、投訴處理與內控。"
      },
      "why": {
        "sc": "保司内控加严会传导到经纪出单补件与质检标准。",
        "tc": "保司內控加嚴會傳導到經紀出單補件與質檢標準。"
      },
      "actions": {
        "front": {
          "sc": "签约文件一次齐：适合性、比较、披露。",
          "tc": "簽約文件一次齊：適合性、比較、披露。"
        },
        "midback": {
          "sc": "把巡查要点编入签约课案例。｜对照附件清单做自查差距分析。",
          "tc": "把巡查要點編入簽約課案例。｜對照附件清單做自查差距分析。"
        },
        "lead": {
          "sc": "要求运营提交整改时间表。",
          "tc": "要求運營提交整改時間表。"
        },
        "cross": {
          "sc": "大额单留痕标准按更严一档执行。",
          "tc": "大額單留痕標準按更嚴一檔執行。"
        }
      },
      "source": {
        "sc": "保监局规管通函 2026-05-29",
        "tc": "保監局規管通函 2026-05-29"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "现场巡查",
          "操守",
          "最佳实务"
        ],
        "tc": [
          "現場巡查",
          "操守",
          "最佳實務"
        ]
      },
      "themes": [
        "compliance",
        "reg"
      ],
      "rolesImpact": {
        "front": 2,
        "midback": 3,
        "lead": 2,
        "cross": 1
      },
      "publishedAt": "2026-05-29T09:00:00+08:00",
      "score": 88,
      "verifyStatus": "verified",
      "featured": true,
      "originalUrl": "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/files/Cir_dd_29.05.2026.pdf",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "insurer",
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "allianz-20260528-global-report",
      "clusterCount": 1,
      "score": 94,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": false,
      "ingestedAt": "2026-07-28T19:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "安联全球保险报告2026：全球保费+7.1%至6.9万亿欧元 亚洲领跑。",
        "tc": "安聯全球保險報告2026：全球保費+7.1%至6.9萬億歐元 亞洲領跑。"
      },
      "summary": {
        "sc": "安联2026年5月发布全球保险报告：2025年全球保费+7.1%至EUR6.9万亿。亚洲生命保险+9.9%重新成为增长引擎(中国+11.4%)。健康险+12.3%创十年新高。未来十年全球保费池将新增EUR5.26万亿，超半来自亚洲。[EN原文]",
        "tc": "安聯：2025全球保費+7.1%，亞洲佔未來增長一半以上"
      },
      "why": {
        "sc": "年度最全面的全球保险市场数据，涵盖80+市场。",
        "tc": "年度最全面全球保險數據。"
      },
      "actions": {
        "front": {
          "sc": "客户沟通中用权威全球数据增强说服力",
          "tc": "用權威數據增強說服力"
        },
        "midback": {
          "sc": "归档年度全球市场数据",
          "tc": "歸檔全球數據"
        },
        "lead": {
          "sc": "亚洲成长=香港市场的天然顺风",
          "tc": "亞洲成長=香港順風"
        },
        "cross": {
          "sc": "亚洲跨境保险需求的结构性增长依据",
          "tc": "跨境需求結構性增長"
        }
      },
      "source": {
        "sc": "Allianz Research",
        "tc": "Allianz Research",
        "lang": "en"
      },
      "boards": [
        "intl",
        "macro"
      ],
      "tags": {
        "sc": [
          "安联",
          "全球保险",
          "报告",
          "2026"
        ],
        "tc": [
          "安聯",
          "全球保險",
          "報告",
          "2026"
        ]
      },
      "contentKind": "report",
      "publishedAt": "2026-05-28T10:00:00+08:00",
      "originalUrl": "https://www.allianz.com/en/economic_research/insights/publications/specials_fmo/260528-global-insurance-report.html",
      "sourceKey": "allianz",
      "sourceTier": "research",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "bcg-hk-1-cross-border-wealth-20260527",
      "clusterCount": 1,
      "score": 86,
      "verifyStatus": "verified",
      "sourceTier": "pro",
      "sourceKey": "bcg",
      "title": {
        "sc": "BCG 2026报告：香港超越瑞士成为全球最大跨境财富管理中心",
        "tc": "BCG 2026報告：香港超越瑞士成為全球最大跨境財富管理中心"
      },
      "summary": {
        "sc": "BCG《2026年全球财富报告》显示：香港跨境财富管理规模达 2.9 万亿美元（+10.7%），超越瑞士成为全球第一。预计 2025-2030 年香港管理的跨境财富年均增长 9%。内地资金流入、IPO 活跃和家办政策是三大驱动力。",
        "tc": "BCG《2026年全球財富報告》顯示：香港跨境財富管理規模達 2.9 萬億美元（+10.7%），超越瑞士成為全球第一。預計 2025-2030 年香港管理的跨境財富年均增長 9%。內地資金流入、IPO 活躍和家辦政策是三大驅動力。"
      },
      "why": {
        "sc": "全球第一——这不是口号，是 BCG 的量化结论。跨境财富管理规模 2.9 万亿美元是整个跨境架构赛道的「底座」：每一份离岸保单、每一个家族信托、每一笔 CIES 投资都在这片海里。",
        "tc": "全球第一——這不是口號，是 BCG 的量化結論。跨境財富管理規模 2.9 萬億美元是整個跨境架構賽道的「底座」：每一份離岸保單、每一個家族信託、每一筆 CIES 投資都在這片海裏。"
      },
      "actions": {
        "front": {
          "sc": "2.9万亿数据是跨境客户沟通的最强背书",
          "tc": "2.9萬億數據是跨境客戶溝通的最強背書"
        },
        "midback": {
          "sc": "BCG数据可作为尽调和客户提案的权威引述",
          "tc": "BCG數據可作為盡調和客戶提案的權威引述"
        },
        "lead": {
          "sc": "全球第一=跨境财富赛道将持续吸引人才和资本",
          "tc": "全球第一=跨境財富賽道將持續吸引人才和資本"
        },
        "cross": {
          "sc": "财富管理中心地位直接支撑跨境保险/信托/CIES业务",
          "tc": "財富管理中心地位直接支撐跨境保險/信託/CIES業務"
        }
      },
      "rolesImpact": {
        "front": 4,
        "midback": 3,
        "lead": 5,
        "cross": 5
      },
      "source": {
        "sc": "BCG / GovHK 新闻公报",
        "lang": "zh"
      },
      "boards": [
        "market",
        "family"
      ],
      "themes": [
        "offshore",
        "family-office"
      ],
      "tags": {
        "sc": [
          "BCG",
          "跨境财富",
          "全球第一"
        ],
        "tc": [
          "BCG",
          "跨境財富",
          "全球第一"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2026-05-27T10:00:00+08:00",
      "originalUrl": "https://www.bcg.com/press/27may2026-hong-kong-surpasses-switzerland-largest-cross-border-wealth-hub"
    },
    {
      "id": "ia-20260520-gl34-corp",
      "clusterCount": 1,
      "score": 83,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "立法会审议《保险业(公众披露)规则》附属法例。",
        "tc": "立法會審議《保險業(公眾披露)規則》附屬法例。"
      },
      "summary": {
        "sc": "港府2026年5月20日将《保险业(公众披露)规则》提交立法会审议。规则要求获授权保险人自2025年1月1日后财政年度起公开披露七大类信息，并拟于刊宪即日生效。同步推进的还有《估值及资本》(修订)规则和《在港维持资产》(修订)规则。",
        "tc": "港府5月20日將公眾披露規則提交立法會審議"
      },
      "why": {
        "sc": "公开披露规则进入立法程序，保司经营透明度即将成为法定要求。",
        "tc": "公開披露規則進入立法程序。"
      },
      "actions": {
        "front": {
          "sc": "无需立即行动，关注最终版本发布时间",
          "tc": "關注最終版本發布時間"
        },
        "midback": {
          "sc": "准备保司对比模板，待规则生效后填充",
          "tc": "準備保司對比模板"
        },
        "lead": {
          "sc": "将公开披露纳入团队内部培训材料",
          "tc": "納入團隊培訓"
        },
        "cross": {
          "sc": "跨境客户可提前告知披露规则进度",
          "tc": "提前告知跨境客戶進度"
        }
      },
      "source": {
        "sc": "立法会参考资料摘要",
        "tc": "立法會參考資料摘要",
        "lang": "zh"
      },
      "boards": [
        "regulatory",
        "compliance"
      ],
      "tags": {
        "sc": [
          "公众披露",
          "立法会",
          "附属法例"
        ],
        "tc": [
          "公眾披露",
          "立法會",
          "附屬法例"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-05-20T16:00:00+08:00",
      "originalUrl": "https://www.legco.gov.hk/yr2026/chinese/brief/ins216c_20260520-c.pdf",
      "sourceKey": "govhk",
      "sourceTier": "official",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "fwd-2026-q1-update",
      "clusterCount": 1,
      "score": 80,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T17:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "富卫集团2026年Q1新业务强劲：年化新保费+4%至7.2亿美元。",
        "tc": "富衛集團2026年Q1新業務強勁：年化新保費+4%至7.2億美元。"
      },
      "summary": {
        "sc": "富卫集团2026年Q1新增业务销售额（年化新保费）按年上升4%至7.2亿美元。新业务合约服务边际达5.56亿美元，按年增幅18%。泛亚地区推出11款新产品。[EN原文]",
        "tc": "富衛Q1新保費+4%，合約邊際+18%"
      },
      "why": {
        "sc": "富卫IPO后首份季度成绩单，也是市场关注。",
        "tc": "富衛IPO後首季成績。"
      },
      "actions": {
        "front": {
          "sc": "了解富卫新产品线",
          "tc": "了解富衛新產品"
        },
        "midback": {
          "sc": "更新富卫品牌档案",
          "tc": "更新品牌檔案"
        },
        "lead": {
          "sc": "关注富卫在泛亚市场的扩张",
          "tc": "關注泛亞擴張"
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "FWD 新闻稿",
        "tc": "FWD 新聞稿",
        "lang": "en"
      },
      "boards": [
        "product",
        "firm"
      ],
      "tags": {
        "sc": [
          "富卫",
          "Q1",
          "保费",
          "2026"
        ],
        "tc": [
          "富衛",
          "Q1",
          "保費",
          "2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-05-20T10:00:00+08:00",
      "originalUrl": "https://www.fwd.com/zh/newsroom/press-releases/FWD-Group-reports-strong-first-quarter-new-business-update/",
      "sourceKey": "fwd",
      "sourceTier": "insurer",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20260519-disclosure-consult",
      "clusterCount": 1,
      "score": 85,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "保监局就保险人公开披露规则咨询市场。",
        "tc": "保監局就保險人公開披露規則諮詢市場。"
      },
      "summary": {
        "sc": "保监局2026年5月就《保险业(公开披露)规则》咨询市场，要求获授权保险人公开披露包括公司管治、财务状况、投资组合、保险负债、资本充足率、风险管理七维度信息。适用本地及海外分公司。",
        "tc": "保監局5月就保險人公開披露規則諮詢市場，涵蓋七維度"
      },
      "why": {
        "sc": "保司透明度将大幅提升，为IFA提供更客观的保司评估基础。",
        "tc": "保司透明度大幅提升。"
      },
      "actions": {
        "front": {
          "sc": "了解公开披露框架，掌握客户问'哪家更稳'的数据依据",
          "tc": "掌握客戶問'哪家更穩'的數據依據"
        },
        "midback": {
          "sc": "更新保司评估档案，预留披露字段",
          "tc": "更新保司評估檔案"
        },
        "lead": {
          "sc": "评估公开披露对与保司合作关系的影响",
          "tc": "評估公開披露對保司合作影響"
        },
        "cross": {
          "sc": "家办客户尽调可引用公开披露数据",
          "tc": "家辦客戶盡調可引用披露數據"
        }
      },
      "source": {
        "sc": "IA 保监局咨询文件",
        "tc": "IA 保監局諮詢文件",
        "lang": "zh"
      },
      "boards": [
        "regulatory",
        "compliance"
      ],
      "tags": {
        "sc": [
          "公开披露",
          "咨询",
          "透明度"
        ],
        "tc": [
          "公開披露",
          "諮詢",
          "透明度"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-05-19T15:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/en/infocenter/press_releases/",
      "sourceKey": "ia",
      "sourceTier": "official",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "sunlife-2026-10life-awards",
      "clusterCount": 1,
      "score": 77,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T16:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "Sun Life永明连续4年获10Life 5星保险大奖。",
        "tc": "Sun Life永明連續4年獲10Life 5星保險大獎。"
      },
      "summary": {
        "sc": "Sun Life永明2026年连续第四年荣获10Life 5星保险大奖，获奖产品涵盖医疗、危疾及储蓄保险等多个类别。",
        "tc": "永明連續4年獲10Life五星大獎"
      },
      "why": {
        "sc": "连续获奖，也是产品品质的持续验证。",
        "tc": "連續獲獎，也是品質驗證。"
      },
      "actions": {
        "front": {
          "sc": "客户品牌对比可用",
          "tc": "品牌對比可用"
        },
        "midback": {
          "sc": "更新永明品牌档案",
          "tc": "更新品牌檔案"
        },
        "lead": {
          "sc": ""
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "10Life/永明",
        "tc": "10Life/永明",
        "lang": "zh"
      },
      "boards": [
        "product",
        "firm"
      ],
      "tags": {
        "sc": [
          "永明",
          "10Life",
          "奖项",
          "2026"
        ],
        "tc": [
          "永明",
          "10Life",
          "獎項",
          "2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-05-15T10:00:00+08:00",
      "originalUrl": "https://www.10life.com/zh-HK/5star-products-2026/insurer-sunlife",
      "sourceKey": "sunlife",
      "sourceTier": "insurer",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20260513-cross-ref",
      "clusterCount": 1,
      "score": 90,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "银行与保险跨行业背景查核安排通函发布。",
        "tc": "銀行與保險跨行業背景查核安排通函發布。"
      },
      "summary": {
        "sc": "保监局2026年5月13日发出《银行业与保险业之间的跨行业背景查核安排》通函，与金管局衔接。首阶段于2026年7月1日实施，覆盖银行及保险机构的寿险从业员，准员工过去七年操守记录可在两行业间共享。",
        "tc": "保監局5月13日發出跨行業背景查核通函"
      },
      "why": {
        "sc": "银行与保险从业员跳槽的合规审查标准统一化，不良记录无处可藏。",
        "tc": "銀行保險跳槽合規審查標準統一。"
      },
      "actions": {
        "front": {
          "sc": "跳槽前自查七年操守记录",
          "tc": "跳槽前自查七年操守記錄"
        },
        "midback": {
          "sc": "招聘流程对接跨行业查核机制",
          "tc": "招聘流程對接查核機制"
        },
        "lead": {
          "sc": "梳理团队操守档案，提前识别风险",
          "tc": "梳理團隊操守檔案"
        },
        "cross": {
          "sc": "跨境人员需满足两地合规标准",
          "tc": "跨境人員需滿足兩地合規"
        }
      },
      "source": {
        "sc": "IA 保监局通函",
        "tc": "IA 保監局通函",
        "lang": "zh"
      },
      "boards": [
        "regulatory",
        "compliance",
        "channel"
      ],
      "tags": {
        "sc": [
          "背景查核",
          "跨行业",
          "通函",
          "2026"
        ],
        "tc": [
          "背景查核",
          "跨行業",
          "通函",
          "2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-05-13T09:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html",
      "sourceKey": "ia",
      "sourceTier": "official",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20260513-cross-refcheck",
      "title": {
        "sc": "银行与保险跨行业背景查核安排通函（2026-05-13）。",
        "tc": "銀行與保險跨行業背景查核安排通函（2026-05-13）。"
      },
      "summary": {
        "sc": "保监局2026年5月13日发出《银行业与保险业之间的跨行业背景查核安排》通函，与金管局衔接，覆盖长期业务中介在银行与保险机构间跳槽时的主事人查核。",
        "tc": "保監局2026年5月13日發出《銀行業與保險業之間的跨行業背景查核安排》通函，與金管局銜接，覆蓋長期業務中介在銀行與保險機構間跳槽時的主事人查核。"
      },
      "why": {
        "sc": "聘用与跳槽尽调成为牌照与声誉风险的硬门槛。",
        "tc": "聘用與跳槽盡調成為牌照與聲譽風險的硬門檻。"
      },
      "actions": {
        "front": {
          "sc": "转职交接配合提供真实受雇/委任信息。",
          "tc": "轉職交接配合提供真實受僱/委任信息。"
        },
        "midback": {
          "sc": "招募话术避免「无缝跳槽、无背景审查」。｜更新聘用SOP：跨行业查核节点与存档。",
          "tc": "招募話術避免「無縫跳槽、無背景審查」。｜更新聘用SOP：跨行業查核節點與存檔。"
        },
        "lead": {
          "sc": "人力流程与合规双签后才能出委任。",
          "tc": "人力流程與合規雙簽後才能出委任。"
        },
        "cross": {
          "sc": "无直接动作。",
          "tc": "無直接動作。"
        }
      },
      "source": {
        "sc": "保监局规管通函 2026-05-13",
        "tc": "保監局規管通函 2026-05-13"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "背景查核",
          "跨行业",
          "金管局"
        ],
        "tc": [
          "背景查核",
          "跨行業",
          "金管局"
        ]
      },
      "themes": [
        "compliance",
        "career",
        "reg"
      ],
      "rolesImpact": {
        "front": 2,
        "midback": 3,
        "lead": 3,
        "cross": 0
      },
      "publishedAt": "2026-05-13T09:00:00+08:00",
      "effectiveAt": "2026-07-01",
      "score": 94,
      "verifyStatus": "verified",
      "featured": true,
      "originalUrl": "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/files/Cir_dd_13.05.2026_Cross-sector_Reference_Checking_Arrangement_Between_the_Banking_and_Insurance_Sectors_Eng.pdf",
      "clusterCount": 3,
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": true,
      "boards": [
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "ia-20260508-rbc-conclusion",
      "clusterCount": 1,
      "score": 96,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "保监局公布RBC制度优化咨询结论：鼓励基建投资、巩固风险管理中心。",
        "tc": "保監局公布RBC制度優化諮詢結論：鼓勵基建投資、鞏固風險管理中心。"
      },
      "summary": {
        "sc": "保监局2026年5月8日公布对《保险业（估值及资本）规则》拟议修订的咨询结论。目标在维持审慎的同时，激励保险人投资基建、增强香港作为全球风险管理中心的竞争力。修订涵盖基建投资优惠、离岸再保险宽免、IUL匹配调整等7项。",
        "tc": "保監局5月8日公布RBC修訂諮詢結論，涵蓋基建優惠、離岸再保寬免等7項"
      },
      "why": {
        "sc": "RBC首次大修，储蓄险资本翻倍、IUL权重上调50%+，直接影响产品供给。",
        "tc": "RBC首次大修，直接影響產品供給。"
      },
      "actions": {
        "front": {
          "sc": "关注高演示产品可能2027年前调整，锁定当前保证利率窗口",
          "tc": "關注高演示產品調整窗口"
        },
        "midback": {
          "sc": "更新产品合规手册中RBC相关章节",
          "tc": "更新RBC合規章節"
        },
        "lead": {
          "sc": "评估RBC修订对团队产品组合策略的影响",
          "tc": "評估RBC修訂對產品組合的影響"
        },
        "cross": {
          "sc": "跨境客户：高保证产品将稀缺，引导长期锁定",
          "tc": "引導跨境客戶長期鎖定"
        }
      },
      "source": {
        "sc": "IA 保监局新闻稿",
        "tc": "IA 保監局新聞稿",
        "lang": "en"
      },
      "boards": [
        "regulatory",
        "product"
      ],
      "tags": {
        "sc": [
          "RBC",
          "咨询结论",
          "基建",
          "资本规则"
        ],
        "tc": [
          "RBC",
          "諮詢結論",
          "基建",
          "資本規則"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-05-08T12:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/en/infocenter/press_releases/20260508.html",
      "sourceKey": "ia",
      "sourceTier": "official",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20260508-rbc-conclusions",
      "title": {
        "sc": "RBC 制度优化咨询结论发布：鼓励基建投资、巩固风险管理中心（2026-05-08）。",
        "tc": "RBC 制度優化諮詢結論發布：鼓勵基建投資、鞏固風險管理中心（2026-05-08）。"
      },
      "summary": {
        "sc": "保监局2026年5月8日公布对《保险业（估值及资本）规则》拟议修订的咨询结论，目标在维持审慎的同时，激励保险人投资基建、增强香港作为全球风险管理中心的竞争力。",
        "tc": "保監局2026年5月8日公布對《保險業（估值及資本）規則》擬議修訂的諮詢結論，目標在維持審慎的同時，激勵保險人投資基建、增強香港作為全球風險管理中心的競爭力。"
      },
      "why": {
        "sc": "资本规则影响保司长期资产配置与产品供给，是机构与高净值叙事的底层。",
        "tc": "資本規則影響保司長期資產配置與產品供給，是機構與高淨值敘事的底層。"
      },
      "actions": {
        "front": {
          "sc": "勿对客承诺具体产品因RBC而“更高收益”。",
          "tc": "勿對客承諾具體產品因RBC而「更高收益」。"
        },
        "midback": {
          "sc": "阅读咨询结论摘要，更新保司研究卡。｜跟踪最终规则生效时间表。",
          "tc": "閱讀諮詢結論摘要，更新保司研究卡。｜跟踪最終規則生效時間表。"
        },
        "lead": {
          "sc": "战略会讨论资本与产品供给含义。",
          "tc": "戰略會討論資本與產品供給含義。"
        },
        "cross": {
          "sc": "风险管理中心定位可作文案背景。",
          "tc": "風險管理中心定位可作文案背景。"
        }
      },
      "source": {
        "sc": "保监局新闻稿 2026-05-08",
        "tc": "保監局新聞稿 2026-05-08"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "RBC",
          "咨询结论",
          "基建"
        ],
        "tc": [
          "RBC",
          "諮詢結論",
          "基建"
        ]
      },
      "themes": [
        "reg",
        "firm",
        "macro"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 2,
        "lead": 3,
        "cross": 2
      },
      "publishedAt": "2026-05-08T12:00:00+08:00",
      "score": 91,
      "featured": true,
      "originalUrl": "https://www.ia.org.hk/en/infocenter/press_releases/20260508.html",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T02:07:48+08:00",
      "evergreen": true,
      "clusterCount": 1,
      "verifyStatus": "verified",
      "boards": [
        "insurer",
        "market",
        "reg"
      ],
      "contentKind": "press"
    },
    {
      "id": "cpic-20260504-gen3",
      "clusterCount": 1,
      "score": 84,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": false,
      "ingestedAt": "2026-07-28T17:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "太保寿险香港推出「世代悦享3」储蓄保险计划——35周年献礼。",
        "tc": "太保壽險香港推出「世代悅享3」儲蓄保險計劃——35周年獻禮。"
      },
      "summary": {
        "sc": "中国太保寿险香港2026年5月4日（太保成立35周年）推出「世代悦享3储蓄保险计划」。以国资实控、836%偿付能力充足率、全线100%分红兑现（新品116%超预期）为核心卖点，定位安全稳健。",
        "tc": "太保推出世代悅享3，國資背景+836%償付率"
      },
      "why": {
        "sc": "中资保险在港最亮眼产品之一，国资背景+高兑现率，也是差异化竞争力。",
        "tc": "中資保險在港亮眼產品。"
      },
      "actions": {
        "front": {
          "sc": "中资保司偏好客户的首选推荐",
          "tc": "中資保司客戶首選"
        },
        "midback": {
          "sc": "更新产品对比，纳入太保",
          "tc": "更新產品對比"
        },
        "lead": {
          "sc": "太保作为中资保司的差异化定位评估",
          "tc": "中資保司差異化評估"
        },
        "cross": {
          "sc": "内地客户对太保品牌天然的信任感",
          "tc": "內地客戶對太保信任感"
        }
      },
      "source": {
        "sc": "太保/界面新闻/东方财富",
        "tc": "太保/界面新聞/東方財富",
        "lang": "zh"
      },
      "boards": [
        "product",
        "firm"
      ],
      "tags": {
        "sc": [
          "太保",
          "世代悦享3",
          "国资",
          "2026"
        ],
        "tc": [
          "太保",
          "世代悅享3",
          "國資",
          "2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-05-04T10:00:00+08:00",
      "originalUrl": "https://www.cpiclifehk.com.hk/sc/company/lastestNews",
      "sourceKey": "cpic:gen3-20260504",
      "sourceTier": "media",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "aia-20260430-q1-vonb",
      "clusterCount": 1,
      "score": 80,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T16:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "AIA 2026年Q1新业务价值增长13% 香港表现强劲。",
        "tc": "AIA 2026年Q1新業務價值增長13% 香港表現強勁。"
      },
      "summary": {
        "sc": "友邦保险2026年4月30日公布Q1业绩：新业务价值(VONB)按固定汇率增长13%，其中香港业务增长21%，由本地及内地访客双轮驱动。[EN原文]",
        "tc": "友邦Q1 VONB +13% 香港+21%"
      },
      "why": {
        "sc": "AIA香港业绩持续强劲，也是市场信心指标。",
        "tc": "AIA業績，也是市場信心指標。"
      },
      "actions": {
        "front": {
          "sc": "可用业绩数据增加客户信心",
          "tc": "用業績增加客戶信心"
        },
        "midback": {
          "sc": "更新友邦评估档案",
          "tc": "更新評估檔案"
        },
        "lead": {
          "sc": "关注AIA产品策略变化",
          "tc": "關注產品策略"
        },
        "cross": {
          "sc": "内地访客数据支持跨境业务",
          "tc": "內地訪客數據支持跨境"
        }
      },
      "source": {
        "sc": "AIA 业绩公告",
        "tc": "AIA 業績公告",
        "lang": "en"
      },
      "boards": [
        "product",
        "firm",
        "macro"
      ],
      "tags": {
        "sc": [
          "AIA",
          "VONB",
          "Q1",
          "2026"
        ],
        "tc": [
          "AIA",
          "VONB",
          "Q1",
          "2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-04-30T09:00:00+08:00",
      "originalUrl": "https://www.aia.com/content/dam/group-wise/en/docs/press-release/2026/AIA%20Group%20Press%20Release_ENG_30%20April%202026.pdf",
      "sourceKey": "aia",
      "sourceTier": "insurer",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "prudential-20260429-self-future",
      "clusterCount": 1,
      "score": 78,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T16:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "保诚推出「自主未来」保险计划II 产品发布会。",
        "tc": "保誠推出「自主未來」保險計劃II 產品發佈會。"
      },
      "summary": {
        "sc": "保诚2026年4月29日举办「自主未来」保险计划II产品发布会，新产品进一步增强灵活性与保障范围。",
        "tc": "保誠4月29日發布自主未來II"
      },
      "why": {
        "sc": "保诚核心产品线更新，需跟进对比。",
        "tc": "保誠核心產品更新。"
      },
      "actions": {
        "front": {
          "sc": "了解新产品与旧版差异",
          "tc": "了解新舊版差異"
        },
        "midback": {
          "sc": "更新产品对比表",
          "tc": "更新產品對比表"
        },
        "lead": {
          "sc": "评估替换策略",
          "tc": "評估替換策略"
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "保诚新闻稿",
        "tc": "保誠新聞稿",
        "lang": "zh"
      },
      "boards": [
        "product",
        "firm"
      ],
      "tags": {
        "sc": [
          "保诚",
          "自主未来",
          "产品更新"
        ],
        "tc": [
          "保誠",
          "自主未來",
          "產品更新"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-04-29T14:00:00+08:00",
      "originalUrl": "https://www.prudential.com.hk/tc/",
      "sourceKey": "prudential",
      "sourceTier": "insurer",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "boclife-20260427-retirement",
      "clusterCount": 1,
      "score": 80,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T16:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "中银人寿联乘中银香港推出「退优·新活」综合养老方案。",
        "tc": "中銀人壽聯乘中銀香港推出「退優·新活」綜合養老方案。"
      },
      "summary": {
        "sc": "中银人寿与中银香港2026年4月27日联合推出「退优·新活」综合养老方案，涵盖保险保障、退休储蓄及银行理财，一站式解决养老需求。",
        "tc": "中銀4月27日推出一站式養老方案"
      },
      "why": {
        "sc": "银保跨界养老方案，也是中银体系独特优势。",
        "tc": "銀保跨界養老方案。"
      },
      "actions": {
        "front": {
          "sc": "退休规划客户的新选择",
          "tc": "退休規劃新選擇"
        },
        "midback": {
          "sc": "更新养老产品对比",
          "tc": "更新養老產品對比"
        },
        "lead": {
          "sc": "中银养老方案=差异化切入点",
          "tc": "養老方案差異化"
        },
        "cross": {
          "sc": "内地养老客户适配性",
          "tc": "內地養老客戶適配性"
        }
      },
      "source": {
        "sc": "中银香港新闻稿",
        "tc": "中銀香港新聞稿",
        "lang": "zh"
      },
      "boards": [
        "product",
        "firm"
      ],
      "tags": {
        "sc": [
          "中银人寿",
          "养老",
          "退休",
          "银保"
        ],
        "tc": [
          "中銀人壽",
          "養老",
          "退休",
          "銀保"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-04-27T10:00:00+08:00",
      "originalUrl": "https://www.bochk.com/dam/bochk/desktop/top/aboutus/pressrelease2/2026/260427021_Press_Release_TC.pdf",
      "sourceKey": "boclife:retirement-20260427",
      "sourceTier": "media",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-2025-full-year",
      "clusterCount": 1,
      "score": 92,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": false,
      "ingestedAt": "2026-07-28T21:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "保监局公布2025全年业绩：个人新单保费3309亿港元 +50.6%再创新高。",
        "tc": "保監局公布2025全年業績：個人新單保費3309億港元 +50.6%再創新高。"
      },
      "summary": {
        "sc": "保监局2026年4月公布2025全年数据：个人新造保单保费3309亿港元同比+50.6%刷新纪录。分红业务贡献核心增长。全年毛保费827亿(+29.7%)。件均保费普遍上涨，大额保单激增。2025年是香港保险史上增长最快的一年。",
        "tc": "2025新單保費3309億+50.6%創歷史新高"
      },
      "why": {
        "sc": "2025，也是香港保险史上增长最快的一年，数据刷新2001年以来所有纪录。",
        "tc": "2025，也是香港保險史上增長最快一年。"
      },
      "actions": {
        "front": {
          "sc": "最强市场增长数据,客户沟通首选",
          "tc": "最強市場數據"
        },
        "midback": {
          "sc": "归档2025年度数据",
          "tc": "歸檔年度數據"
        },
        "lead": {
          "sc": "历史性增长=行业信心最强佐证",
          "tc": "歷史性增長=行業信心"
        },
        "cross": {
          "sc": "内地客户贡献+大额保单=跨境业务黄金期",
          "tc": "內地客戶+大額保單=跨境黃金期"
        }
      },
      "source": {
        "sc": "IA 保监局",
        "tc": "IA 保監局",
        "lang": "zh"
      },
      "boards": [
        "macro"
      ],
      "tags": {
        "sc": [
          "全年",
          "保费",
          "3309亿",
          "2025"
        ],
        "tc": [
          "全年",
          "保費",
          "3309億",
          "2025"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-04-25T10:00:00+08:00",
      "originalUrl": "https://www.hkinsu.com/zhuanlan/chris/36397.html",
      "sourceKey": "hkinsu",
      "sourceTier": "media",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20260424-stats-2025",
      "title": {
        "sc": "保监局公布2025年临时统计（2026-04-24）。",
        "tc": "保監局公布2025年臨時統計（2026-04-24）。"
      },
      "summary": {
        "sc": "保监局于2026年4月24日发布2025年临时统计。结合此前口径，2025年长期业务新造保费约3309亿港元、同比约+50.6%的市场叙事有官方统计节点支撑；细节请以新闻稿及统计表为准。",
        "tc": "保監局於2026年4月24日發布2025年臨時統計。結合此前口徑，2025年長期業務新造保費約3309億港元、同比約+50.6%的市場敘事有官方統計節點支撐；細節請以新聞稿及統計表為準。"
      },
      "why": {
        "sc": "全年市场底数的关键官方发布日，适合做年报/复盘锚点。",
        "tc": "全年市場底數的關鍵官方發布日，適合做年報/複盤錨點。"
      },
      "actions": {
        "front": {
          "sc": "更新对外市场数据引用年份与链接。",
          "tc": "更新對外市場數據引用年份與連結。"
        },
        "midback": {
          "sc": "重做2025全年 vs 2026Q1对照表。｜无直接动作。",
          "tc": "重做2025全年 vs 2026Q1對照表。｜無直接動作。"
        },
        "lead": {
          "sc": "年度复盘引用此节点。",
          "tc": "年度複盤引用此節點。"
        },
        "cross": {
          "sc": "增长结构用于跨境需求讨论。",
          "tc": "增長結構用於跨境需求討論。"
        }
      },
      "source": {
        "sc": "保监局新闻稿 2026-04-24",
        "tc": "保監局新聞稿 2026-04-24"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "临时统计",
          "2025全年"
        ],
        "tc": [
          "臨時統計",
          "2025全年"
        ]
      },
      "themes": [
        "macro",
        "channel",
        "firm"
      ],
      "rolesImpact": {
        "front": 2,
        "midback": 2,
        "lead": 3,
        "cross": 2
      },
      "publishedAt": "2026-04-24T12:00:00+08:00",
      "score": 93,
      "featured": true,
      "originalUrl": "https://www.ia.org.hk/en/infocenter/press_releases/20260424.html",
      "note": {
        "sc": "请打开新闻稿核对表格数字后再对外引用。",
        "tc": "請打開新聞稿核對表格數字後再對外引用。"
      },
      "verifyStatus": "verified",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T02:07:48+08:00",
      "evergreen": false,
      "clusterCount": 1,
      "boards": [
        "insurer",
        "market"
      ],
      "contentKind": "press"
    },
    {
      "id": "aia-20260424-top-insurer",
      "clusterCount": 1,
      "score": 79,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:30:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "AIA连续获评为香港首选保险公司。",
        "tc": "AIA連續獲評為香港首選保險公司。"
      },
      "summary": {
        "sc": "AIA香港于2026年再度获评为香港首选保险公司(No.1 Insurer of Choice)，体现了其在品牌、产品和服务方面持续领先的市场地位。[EN原文]",
        "tc": "AIA香港再度獲評為香港首選保險公司"
      },
      "why": {
        "sc": "品牌排名数据可作为客户沟通中的客观参考。",
        "tc": "品牌排名可作客戶溝通參考。"
      },
      "actions": {
        "front": {
          "sc": "可在客户品牌对比时引用",
          "tc": "可在品牌對比時引用"
        },
        "midback": {
          "sc": "更新保司品牌档案",
          "tc": "更新保司品牌檔案"
        },
        "lead": {
          "sc": "AIA的产品与服务策略值得团队学习",
          "tc": "AIA策略值得學習"
        },
        "cross": {
          "sc": "AIA品牌认知度在跨境客户中较高",
          "tc": "AIA品牌在跨境客戶中認知度高"
        }
      },
      "source": {
        "sc": "PRNewswire",
        "tc": "PRNewswire",
        "lang": "en"
      },
      "boards": [
        "product",
        "firm"
      ],
      "tags": {
        "sc": [
          "AIA",
          "品牌",
          "首选"
        ],
        "tc": [
          "AIA",
          "品牌",
          "首選"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-04-24T10:00:00+08:00",
      "originalUrl": "https://finance.yahoo.com/sectors/healthcare/articles/aia-hong-kong-leads-industry-135200472.html",
      "sourceKey": "yahoofinance",
      "sourceTier": "media",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ctflife-20260422-artisan-leap",
      "clusterCount": 1,
      "score": 79,
      "verifyStatus": "pending",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T16:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "周大福人寿推出「匠心·飞越」储蓄保险计划。",
        "tc": "周大福人壽推出「匠心·飛越」儲蓄保險計劃。"
      },
      "summary": {
        "sc": "周大福人寿2026年4月22日举办「匠心·飞越」储蓄保险计划产品发布会，以「飞越未知、稳创未来」为主题，强化储蓄型产品的灵活性。",
        "tc": "周大福人壽4月22日推出匠心飛越儲蓄計劃"
      },
      "why": {
        "sc": "周大福人寿持续强化产品线，与三大保司差异化竞争。",
        "tc": "周大福強化產品線。"
      },
      "actions": {
        "front": {
          "sc": "了解新品特点",
          "tc": "了解新品特點"
        },
        "midback": {
          "sc": "更新产品库",
          "tc": "更新產品庫"
        },
        "lead": {
          "sc": "评估周大福产品在组合中的角色",
          "tc": "評估產品角色"
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "周大福/富昌金融",
        "tc": "周大福/富昌金融",
        "lang": "zh"
      },
      "boards": [
        "product",
        "firm"
      ],
      "tags": {
        "sc": [
          "周大福",
          "匠心飞越",
          "储蓄",
          "新产品"
        ],
        "tc": [
          "周大福",
          "匠心飛越",
          "儲蓄",
          "新產品"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-04-22T14:00:00+08:00",
      "originalUrl": "https://www.ffg.com.hk/news/csr/w5jo28lfkyonusn0iidrp960",
      "sourceKey": "ctflife:artisan-leap-20260422",
      "sourceTier": "media",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20260422-ils",
      "title": {
        "sc": "2026保险相连证券（ILS）研讨会：主席开幕辞（2026-04-22）。",
        "tc": "2026保險相連證券（ILS）研討會：主席開幕辭（2026-04-22）。"
      },
      "summary": {
        "sc": "保监局主席姚建华于2026年4月22日在保险相连证券研讨会上致开幕辞，聚焦巨灾风险转移、资本市场与香港风险管理中心建设。",
        "tc": "保監局主席姚建華於2026年4月22日在保險相連證券研討會上致開幕辭，聚焦巨災風險轉移、資本市場與香港風險管理中心建設。"
      },
      "why": {
        "sc": "零售以外的风险证券化叙事，补强「港险，也是风险管理中心」定位。",
        "tc": "零售以外的風險證券化敘事，補強「港險，也是風險管理中心」定位。"
      },
      "actions": {
        "front": {
          "sc": "对非零售客户可作文案背景。",
          "tc": "對非零售客戶可作文案背景。"
        },
        "midback": {
          "sc": "补充 ILS 知识点到内部库。｜无直接动作。",
          "tc": "補充 ILS 知識點到內部庫。｜無直接動作。"
        },
        "lead": {
          "sc": "战略传播可用。",
          "tc": "戰略傳播可用。"
        },
        "cross": {
          "sc": "企业风险与再保话题切入点。",
          "tc": "企業風險與再保話題切入點。"
        }
      },
      "source": {
        "sc": "保监局演辞 2026-04-22",
        "tc": "保監局演辭 2026-04-22"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "ILS",
          "巨灾",
          "风险管理"
        ],
        "tc": [
          "ILS",
          "巨災",
          "風險管理"
        ]
      },
      "themes": [
        "firm",
        "macro",
        "reg"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 2,
        "lead": 3,
        "cross": 2
      },
      "publishedAt": "2026-04-22T10:00:00+08:00",
      "score": 80,
      "featured": false,
      "originalUrl": "https://www.ia.org.hk/tc/infocenter/files/ILS_Conference_2026_Opening_Remarks_Mr_Stephen_Yiu.pdf",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T02:07:48+08:00",
      "evergreen": false,
      "clusterCount": 1,
      "verifyStatus": "verified",
      "boards": [
        "insurer",
        "market",
        "reg"
      ],
      "contentKind": "speech"
    },
    {
      "id": "manulife-20260420-annuity-accident",
      "clusterCount": 1,
      "score": 83,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T16:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "宏利推出全新年金及意外保险：宏瑞终身即期年金+相伴无忧个人意外。",
        "tc": "宏利推出全新年金及意外保險：宏瑞終身即期年金+相伴無憂個人意外。"
      },
      "summary": {
        "sc": "宏利2026年4月20日推出两项全新方案：「宏瑞终身即期年金」提供稳定退休收入，「相伴无忧个人意外」提升日常财务应变能力。反映宏利在退休与保障领域的持续创新。",
        "tc": "宏利4月20日推出年金及意外新產品"
      },
      "why": {
        "sc": "年金产品在香港市场稀缺，宏利此举填补退休收入空白。",
        "tc": "年金產品在香港稀缺。"
      },
      "actions": {
        "front": {
          "sc": "退休规划客户新选择",
          "tc": "退休規劃新選擇"
        },
        "midback": {
          "sc": "更新退休产品对比",
          "tc": "更新退休產品對比"
        },
        "lead": {
          "sc": "年金+意外组合=银发市场切入点",
          "tc": "銀髮市場切入點"
        },
        "cross": {
          "sc": "内地客户退休规划方案",
          "tc": "內地客戶退休規劃"
        }
      },
      "source": {
        "sc": "宏利新闻稿",
        "tc": "宏利新聞稿",
        "lang": "zh"
      },
      "boards": [
        "product",
        "firm"
      ],
      "tags": {
        "sc": [
          "宏利",
          "年金",
          "意外险",
          "退休"
        ],
        "tc": [
          "宏利",
          "年金",
          "意外險",
          "退休"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-04-20T10:00:00+08:00",
      "originalUrl": "https://www.manulife.com.hk/zh-hk/individual/about/newsroom/manulife-launches-new-annuity-and-accident-protection-solutions.html",
      "sourceKey": "manulife",
      "sourceTier": "insurer",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20260416-cyber",
      "title": {
        "sc": "APAC 网络风险与保险峰会简报（2026-04-16）。",
        "tc": "APAC 網絡風險與保險峰會簡報（2026-04-16）。"
      },
      "summary": {
        "sc": "保监局副总监陈慎雄于2026年4月16日在 APAC Cyber Risk & Insurance Summit 发表简报，讨论网络风险与保险应对。",
        "tc": "保監局副總監陳慎雄於2026年4月16日在 APAC Cyber Risk & Insurance Summit 發表簡報，討論網絡風險與保險應對。"
      },
      "why": {
        "sc": "网络风险保险与企业风险话题升温。",
        "tc": "網絡風險保險與企業風險話題升溫。"
      },
      "actions": {
        "front": {
          "sc": "对公客户可作风险意识沟通。",
          "tc": "對公客戶可作風險意識溝通。"
        },
        "midback": {
          "sc": "网络险产品知识储备。｜公司自身网络安全与数据合规。",
          "tc": "網絡險產品知識儲備。｜公司自身網絡安全與數據合規。"
        },
        "lead": {
          "sc": "创新险种机会。",
          "tc": "創新險種機會。"
        },
        "cross": {
          "sc": "企业出海网络风险。",
          "tc": "企業出海網絡風險。"
        }
      },
      "source": {
        "sc": "保监局演辞 2026-04-16",
        "tc": "保監局演辭 2026-04-16"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "网络风险",
          "保险"
        ],
        "tc": [
          "網絡風險",
          "保險"
        ]
      },
      "themes": [
        "firm",
        "tech",
        "macro"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 2,
        "lead": 2,
        "cross": 2
      },
      "publishedAt": "2026-04-16T10:00:00+08:00",
      "score": 77,
      "featured": false,
      "originalUrl": "https://www.ia.org.hk/tc/infocenter/files/APAC_Cyber_Risk_and_Insurance_Summit_2026.pdf",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T02:07:48+08:00",
      "evergreen": false,
      "clusterCount": 1,
      "verifyStatus": "verified",
      "boards": [
        "insurer",
        "market",
        "tech"
      ],
      "contentKind": "speech"
    },
    {
      "id": "ia-202604-fsi-survey",
      "clusterCount": 1,
      "score": 78,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "金发局发表报告：巩固香港作为全球重要保险枢纽的地位。",
        "tc": "金發局發表報告：鞏固香港作為全球重要保險樞紐的地位。"
      },
      "summary": {
        "sc": "香港金融发展局(金发局)发表研究报告，聚焦推动可持续发展及创新，巩固香港全球保险枢纽地位。报告涵盖RBC制度、跨境保险、InsurTech等关键议题。",
        "tc": "金發局發表研究報告推動可持續發展鞏固香港保險樞紐地位"
      },
      "why": {
        "sc": "官方智库为行业中长期发展定调，RBC+跨境+InsurTech三线并行。",
        "tc": "官方智庫為行業定調。"
      },
      "actions": {
        "front": {
          "sc": "了解行业大方向，积累专业知识",
          "tc": "累積專業知識"
        },
        "midback": {
          "sc": "阅读报告全文，关注对合规框架的建议",
          "tc": "閱讀報告全文"
        },
        "lead": {
          "sc": "将金发局核心观点纳入团队战略沟通",
          "tc": "納入團隊戰略溝通"
        },
        "cross": {
          "sc": "跨境保险部分重点关注，辅助业务拓展",
          "tc": "跨境保險部分重點關注"
        }
      },
      "source": {
        "sc": "金发局研究报告",
        "tc": "金發局研究報告",
        "lang": "zh"
      },
      "boards": [
        "regulatory",
        "intl",
        "tech"
      ],
      "tags": {
        "sc": [
          "金发局",
          "保险枢纽",
          "可持续发展"
        ],
        "tc": [
          "金發局",
          "保險樞紐",
          "可持續發展"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-04-15T10:00:00+08:00",
      "originalUrl": "https://www.fsdc.org.hk/zh/media/",
      "sourceKey": "fsdc:insurance-hub-report-202604",
      "sourceTier": "media",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "chinlife-2026-hk-digital",
      "clusterCount": 1,
      "score": 76,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T17:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "中国人寿海外2026年加速数字化转型：线上理赔+智能客服。",
        "tc": "中國人壽海外2026年加速數位轉型：線上理賠+智能客服。"
      },
      "summary": {
        "sc": "中国人寿(海外)2026年持续加速数字化转型，推出线上理赔平台与智能客服系统。目标将理赔时效缩短至3个工作日内，提升客户体验。[EN原文]",
        "tc": "國壽海外加速數位轉型"
      },
      "why": {
        "sc": "中资保司科技升级，也是与港资/外资差异化竞争的新维度。",
        "tc": "中資保司科技升級。"
      },
      "actions": {
        "front": {
          "sc": "理赔速度可作客户沟通卖点",
          "tc": "理賠速度可作賣點"
        },
        "midback": {
          "sc": "更新保司科技能力档案",
          "tc": "更新科技檔案"
        },
        "lead": {
          "sc": "关注中资保司的数字化能力",
          "tc": "關注數位化能力"
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "中国人寿海外",
        "tc": "中國人壽海外",
        "lang": "zh"
      },
      "boards": [
        "product",
        "firm",
        "tech"
      ],
      "tags": {
        "sc": [
          "中国人寿",
          "数字化",
          "理赔",
          "2026"
        ],
        "tc": [
          "中國人壽",
          "數位化",
          "理賠",
          "2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-04-10T10:00:00+08:00",
      "originalUrl": "https://www.chinalife.com.hk/",
      "sourceKey": "chinlife:digital-2026",
      "sourceTier": "media",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "legco-20260410-fa-disclosure",
      "clusterCount": 1,
      "score": 80,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "立法会财经事务委员会讨论保险公开披露立法建议。",
        "tc": "立法會財經事務委員會討論保險公開披露立法建議。"
      },
      "summary": {
        "sc": "2026年4月10日立法会财经事务委员会会议讨论《保险业(公众披露)规则》立法建议。港府提出制定附属法例落实公开披露要求，涵盖本地及海外在港分公司。",
        "tc": "立法會4月10日討論保險公開披露立法建議"
      },
      "why": {
        "sc": "公开披露规则的立法进程加快，2026年内大概率正式刊宪。",
        "tc": "公開披露立法進程加快。"
      },
      "actions": {
        "front": {
          "sc": "关注最终披露模板的发布时间",
          "tc": "關注最終披露模板"
        },
        "midback": {
          "sc": "跟踪立法进度并更新内部合规时间线",
          "tc": "更新內部合規時間線"
        },
        "lead": {
          "sc": "评估公开披露对团队保司评估工具的影响",
          "tc": "評估對團隊工具的影響"
        },
        "cross": {
          "sc": "跨境客户尽调可预留披露数据字段",
          "tc": "預留披露數據字段"
        }
      },
      "source": {
        "sc": "立法会文件",
        "tc": "立法會文件",
        "lang": "zh"
      },
      "boards": [
        "regulatory",
        "compliance"
      ],
      "tags": {
        "sc": [
          "公开披露",
          "立法会",
          "2026"
        ],
        "tc": [
          "公開披露",
          "立法會",
          "2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-04-10T10:00:00+08:00",
      "originalUrl": "https://www.legco.gov.hk/yr2026/english/panels/fa/papers/fa20260410cb1-309-8-e.pdf",
      "sourceKey": "govhk",
      "sourceTier": "official",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20260409-captive-beijing",
      "title": {
        "sc": "保监局于北京举办专属自保论坛（2026-04-09）。",
        "tc": "保監局於北京舉辦專屬自保論壇（2026-04-09）。"
      },
      "summary": {
        "sc": "保监局2026年4月9日在北京举办专属自保论坛，约百名企业与行业代表参与，推动企业通过香港平台管理风险。",
        "tc": "保監局2026年4月9日在北京舉辦專屬自保論壇，約百名企業與行業代表參與，推動企業通過香港平台管理風險。"
      },
      "why": {
        "sc": "家办/企业风控与自保生态线索，补强跨境服务板块。",
        "tc": "家辦/企業風控與自保生態線索，補強跨境服務板塊。"
      },
      "actions": {
        "front": {
          "sc": "对公客户可作话题，不涉及个人销售承诺。",
          "tc": "對公客戶可作話題，不涉及個人銷售承諾。"
        },
        "midback": {
          "sc": "整理自保基础知识卡。｜关注自保相关合规边界。",
          "tc": "整理自保基礎知識卡。｜關注自保相關合規邊界。"
        },
        "lead": {
          "sc": "生态合作线索。",
          "tc": "生態合作線索。"
        },
        "cross": {
          "sc": "内地企业出海风控需求。",
          "tc": "內地企業出海風控需求。"
        }
      },
      "source": {
        "sc": "保监局新闻稿 2026-04-09",
        "tc": "保監局新聞稿 2026-04-09"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "自保",
          "北京",
          "企业风险"
        ],
        "tc": [
          "自保",
          "北京",
          "企業風險"
        ]
      },
      "themes": [
        "firm",
        "offshore",
        "macro"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 2,
        "lead": 2,
        "cross": 3
      },
      "publishedAt": "2026-04-09T12:00:00+08:00",
      "score": 83,
      "featured": true,
      "originalUrl": "https://www.ia.org.hk/en/infocenter/press_releases/20260409.html",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T02:07:48+08:00",
      "evergreen": false,
      "clusterCount": 1,
      "verifyStatus": "verified",
      "boards": [
        "family",
        "insurer",
        "market"
      ],
      "contentKind": "press"
    },
    {
      "id": "ia-20260331-gn16-revised",
      "clusterCount": 1,
      "score": 94,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": true,
      "ingestedAt": "2026-07-28T12:30:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "保监局修订GN16指引：2026年3月31日正式生效。",
        "tc": "保監局修訂GN16指引：2026年3月31日正式生效。"
      },
      "summary": {
        "sc": "保监局发布修订版《承保长期保险业务指引》(GN16)，自2026年3月31日起生效(GN34第4节除外)。核心升级：分红实现率披露回溯期从5年延长、统一披露格式、禁止误导性表述、每年6月30日前完成披露。同步修订GL34分红业务管治指引。",
        "tc": "保監局修訂GN16指引3月31日生效，分紅實現率披露全面升級"
      },
      "why": {
        "sc": "GN16新版是分红险销售规范的基础文件，直接影响所有IFA的客户沟通方式。",
        "tc": "GN16新版是分紅險銷售規範基礎文件。"
      },
      "actions": {
        "front": {
          "sc": "每年6/30后查阅保司最新分红实现率数据",
          "tc": "查閱保司分紅實現率數據"
        },
        "midback": {
          "sc": "更新销售合规手册，纳入GN16新要求",
          "tc": "更新銷售合規手冊"
        },
        "lead": {
          "sc": "团队培训：GN16核心变化与客户沟通要点",
          "tc": "團隊培訓GN16核心變化"
        },
        "cross": {
          "sc": "跨境客户：GN16数据可辅助购买决策",
          "tc": "跨境客戶可用GN16數據輔助決策"
        }
      },
      "source": {
        "sc": "IA 保监局指引",
        "tc": "IA 保監局指引",
        "lang": "zh"
      },
      "boards": [
        "regulatory",
        "product",
        "par"
      ],
      "tags": {
        "sc": [
          "GN16",
          "分红实现率",
          "披露",
          "指引",
          "2026"
        ],
        "tc": [
          "GN16",
          "分紅實現率",
          "披露",
          "指引",
          "2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-03-31T09:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/gn16.html",
      "sourceKey": "ia",
      "sourceTier": "official",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "gn16-revised-20260331",
      "clusterCount": 1,
      "score": 92,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": true,
      "ingestedAt": "2026-07-28T12:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "修订版GN16指引：2026年3月31日起正式生效。",
        "tc": "修訂版GN16指引：2026年3月31日起正式生效。"
      },
      "summary": {
        "sc": "保监局发布修订版GN16指引，自2026年3月31日起生效(GN34第4节除外)。核心升级：分红实现率披露回溯期延长、统一披露格式、禁止误导性表述。每年6月30日前完成披露。",
        "tc": "修訂版GN16指引3月31日生效，分紅實現率披露全面升級"
      },
      "why": {
        "sc": "GN16新版是分红险销售规范的基础文件，所有IFA必须了解。",
        "tc": "GN16新版是分紅險銷售規範的基礎文件。"
      },
      "actions": {
        "front": {
          "sc": "了解GN16披露周期，不把演示利率当承诺",
          "tc": "不把演示利率當承諾"
        },
        "midback": {
          "sc": "每年6/30前收集保司分红实现率做对比",
          "tc": "收集保司分紅實現率對比"
        },
        "lead": {
          "sc": "团队培训：GN16的核心要求与对客户沟通的影响",
          "tc": "團隊培訓GN16核心要求"
        },
        "cross": {
          "sc": "跨境客户可查阅GN16披露数据辅助决策",
          "tc": "跨境客戶可查閱數據"
        }
      },
      "source": {
        "sc": "IA 保监局指引",
        "tc": "IA 保監局指引",
        "lang": "zh"
      },
      "boards": [
        "regulatory",
        "product",
        "par"
      ],
      "tags": {
        "sc": [
          "GN16",
          "分红实现率",
          "披露",
          "指引"
        ],
        "tc": [
          "GN16",
          "分紅實現率",
          "披露",
          "指引"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-03-31T09:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/gn16.html",
      "sourceKey": "ia",
      "sourceTier": "official",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20260331-cpd-reporting",
      "title": {
        "sc": "CPD合规汇报安排：2025/26及后续评核期（2026-03-31）。",
        "tc": "CPD合規匯報安排：2025/26及後續評核期（2026-03-31）。"
      },
      "summary": {
        "sc": "保监局2026年3月31日通函说明2025/2026评核期及往后各期的持续专业培训合规汇报安排，规范个人持牌人与委任主事人的汇报程序。",
        "tc": "保監局2026年3月31日通函說明2025/2026評核期及往後各期的持續專業培訓合規匯報安排，規範個人持牌人與委任主事人的匯報程序。"
      },
      "why": {
        "sc": "CPD 未达标可影响续牌与展业资格，是后台刚需日历。",
        "tc": "CPD 未達標可影響續牌與展業資格，是後台剛需日曆。"
      },
      "actions": {
        "front": {
          "sc": "按期完成学时并保留证明。",
          "tc": "按期完成學時並保留證明。"
        },
        "midback": {
          "sc": "公司培训日历对齐评核期截止。｜主事人侧批量汇报与抽查。",
          "tc": "公司培訓日曆對齊評核期截止。｜主事人側批量匯報與抽查。"
        },
        "lead": {
          "sc": "把团队达标率纳入管理仪表盘。",
          "tc": "把團隊達標率納入管理儀表盤。"
        },
        "cross": {
          "sc": "无直接动作。",
          "tc": "無直接動作。"
        }
      },
      "source": {
        "sc": "保监局规管通函 2026-03-31",
        "tc": "保監局規管通函 2026-03-31"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "CPD",
          "汇报"
        ],
        "tc": [
          "CPD",
          "匯報"
        ]
      },
      "themes": [
        "career",
        "compliance",
        "reg"
      ],
      "rolesImpact": {
        "front": 2,
        "midback": 3,
        "lead": 2,
        "cross": 0
      },
      "publishedAt": "2026-03-31T09:00:00+08:00",
      "score": 86,
      "verifyStatus": "verified",
      "featured": false,
      "originalUrl": "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/files/Cir_dd_31032026_CPD_Reporting_Procedures_for_2025-2026_onwards_Eng.pdf",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "ia-2025-complaints",
      "clusterCount": 1,
      "score": 80,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T21:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "保监局2025年投诉统计：全年接获1173宗 同比+19.9%。",
        "tc": "保監局2025年投訴統計：全年接獲1173宗 同比+19.9%。"
      },
      "summary": {
        "sc": "保监局2026年3月公布2025年全年投诉统计：共接获1173宗投诉较2024年978宗上升19.9%。上半年按年升幅达33%下半年回落。中介人操守和合规事宜占投诉重要部分。全年纪律行动50项罚款约2360万港元。",
        "tc": "2025投訴1173宗+19.9%,中介操守佔重要部分"
      },
      "why": {
        "sc": "投诉数据，也是行业服务质量的温度计，操守类投诉上升值得警惕。",
        "tc": "投訴數據，也是服務質量溫度計。"
      },
      "actions": {
        "front": {
          "sc": "了解投诉热点避免同类问题",
          "tc": "了解投訴熱點"
        },
        "midback": {
          "sc": "归档投诉数据作合规培训素材",
          "tc": "歸檔投訴數據"
        },
        "lead": {
          "sc": "操守类投诉上升=团队培训优先级提高",
          "tc": "團隊培訓優先級提高"
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "IA 监管通讯",
        "tc": "IA 監管通訊",
        "lang": "zh"
      },
      "boards": [
        "compliance"
      ],
      "tags": {
        "sc": [
          "投诉",
          "统计",
          "操守",
          "2025"
        ],
        "tc": [
          "投訴",
          "統計",
          "操守",
          "2025"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-03-27T10:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/tc/legislative_framework/Conduct_in_Focus_Issue_12_01.html",
      "sourceKey": "ia",
      "sourceTier": "official",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20260327-cif12",
      "title": {
        "sc": "《监管通讯》第12期（2026-03）：投诉、社媒推广与合规专题。",
        "tc": "《監管通訊》第12期（2026-03）：投訴、社媒推廣與合規專題。"
      },
      "summary": {
        "sc": "保监局2026年3月27日通函发布《监管通讯》第12期，涵盖2025年上半年投诉统计、社交媒体推广保险的操守要点、AML纪律案例等，是前线内容与后台质检的高频参考。",
        "tc": "保監局2026年3月27日通函發布《監管通訊》第12期，涵蓋2025年上半年投訴統計、社交媒體推廣保險的操守要點、AML紀律案例等，是前線內容與後台質檢的高頻參考。"
      },
      "why": {
        "sc": "社媒误导与投诉主题是中介纪律高发区。",
        "tc": "社媒誤導與投訴主題是中介紀律高發區。"
      },
      "actions": {
        "front": {
          "sc": "发帖过公司闸；禁保证收益/返佣暗示。",
          "tc": "發帖過公司閘；禁保證收益/返傭暗示。"
        },
        "midback": {
          "sc": "输出可转发合规素材包。｜社媒抽检+投诉主题对齐。",
          "tc": "輸出可轉發合規素材包。｜社媒抽檢+投訴主題對齊。"
        },
        "lead": {
          "sc": "违规计分纳入团队管理。",
          "tc": "違規計分納入團隊管理。"
        },
        "cross": {
          "sc": "跨境内容默认更高审慎。",
          "tc": "跨境內容默認更高審慎。"
        }
      },
      "source": {
        "sc": "保监局《监管通讯》Issue 12",
        "tc": "保監局《監管通訊》Issue 12"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "监管通讯",
          "社媒",
          "投诉"
        ],
        "tc": [
          "監管通訊",
          "社媒",
          "投訴"
        ]
      },
      "themes": [
        "compliance",
        "career",
        "reg"
      ],
      "rolesImpact": {
        "front": 3,
        "midback": 3,
        "lead": 2,
        "cross": 2
      },
      "publishedAt": "2026-03-27T09:00:00+08:00",
      "score": 91,
      "verifyStatus": "verified",
      "featured": true,
      "originalUrl": "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/files/20260327_Circular_Conduct_In_Focus_Issue_12_Eng.pdf",
      "clusterCount": 2,
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "ia-20260326-health-conf",
      "title": {
        "sc": "亚太医疗与健康保险会议主题演讲（2026-03-26）。",
        "tc": "亞太醫療與健康保險會議主題演講（2026-03-26）。"
      },
      "summary": {
        "sc": "保监局执行董事刘中健于2026年3月26日在第21届亚太医疗与健康保险会议上发表主题演讲，关注医疗保障与健康保险发展趋势。",
        "tc": "保監局執行董事劉中健於2026年3月26日在第21屆亞太醫療與健康保險會議上發表主題演講，關注醫療保障與健康保險發展趨勢。"
      },
      "why": {
        "sc": "医疗险/健康保障产品线的政策与市场语境。",
        "tc": "醫療險/健康保障產品線的政策與市場語境。"
      },
      "actions": {
        "front": {
          "sc": "医疗险沟通强调保障功能与披露。",
          "tc": "醫療險溝通強調保障功能與披露。"
        },
        "midback": {
          "sc": "补充健康险培训素材。｜无直接动作。",
          "tc": "補充健康險培訓素材。｜無直接動作。"
        },
        "lead": {
          "sc": "产品结构讨论参考。",
          "tc": "產品結構討論參考。"
        },
        "cross": {
          "sc": "跨境医疗需求可作话题。",
          "tc": "跨境醫療需求可作話題。"
        }
      },
      "source": {
        "sc": "保监局演辞 2026-03-26",
        "tc": "保監局演辭 2026-03-26"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "健康保险",
          "医疗"
        ],
        "tc": [
          "健康保險",
          "醫療"
        ]
      },
      "themes": [
        "product",
        "macro",
        "reg"
      ],
      "rolesImpact": {
        "front": 2,
        "midback": 3,
        "lead": 2,
        "cross": 2
      },
      "publishedAt": "2026-03-26T10:00:00+08:00",
      "score": 81,
      "featured": false,
      "originalUrl": "https://www.ia.org.hk/tc/infocenter/files/21st_Asia_Conference_on_Healthcare_and_Health_Insurance_2026_Keynote_Mr_Clement_Lau_TC.pdf",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T02:07:48+08:00",
      "evergreen": false,
      "clusterCount": 1,
      "verifyStatus": "verified",
      "boards": [
        "market",
        "product",
        "reg"
      ],
      "contentKind": "speech"
    },
    {
      "id": "ia-20260325-captive-forum-speech",
      "title": {
        "sc": "2026专属自保保险座谈会开幕致辞（2026-03-25）。",
        "tc": "2026專屬自保保險座談會開幕致辭（2026-03-25）。"
      },
      "summary": {
        "sc": "保监局刘中健于2026年3月25日在专属自保保险座谈会致开幕辞，延续香港发展自保与企业风险管理平台的政策方向。",
        "tc": "保監局劉中健於2026年3月25日在專屬自保保險座談會致開幕辭，延續香港發展自保與企業風險管理平台的政策方向。"
      },
      "why": {
        "sc": "与7月新自保授权形成政策-落地链条。",
        "tc": "與7月新自保授權形成政策-落地鏈條。"
      },
      "actions": {
        "front": {
          "sc": "无零售动作。",
          "tc": "無零售動作。"
        },
        "midback": {
          "sc": "自保知识库归档。｜无直接动作。",
          "tc": "自保知識庫歸檔。｜無直接動作。"
        },
        "lead": {
          "sc": "生态定位材料。",
          "tc": "生態定位材料。"
        },
        "cross": {
          "sc": "企业对公线索。",
          "tc": "企業對公線索。"
        }
      },
      "source": {
        "sc": "保监局演辞 2026-03-25",
        "tc": "保監局演辭 2026-03-25"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "自保",
          "座谈会"
        ],
        "tc": [
          "自保",
          "座談會"
        ]
      },
      "themes": [
        "firm",
        "offshore"
      ],
      "rolesImpact": {
        "front": 0,
        "midback": 2,
        "lead": 2,
        "cross": 3
      },
      "publishedAt": "2026-03-25T10:00:00+08:00",
      "score": 79,
      "featured": false,
      "originalUrl": "https://www.ia.org.hk/tc/infocenter/files/Captive_Forum_2026_Speech_Mr_Clement_Lau_CN.pdf",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T02:07:48+08:00",
      "evergreen": false,
      "clusterCount": 1,
      "verifyStatus": "verified",
      "boards": [
        "family",
        "insurer"
      ],
      "contentKind": "speech"
    },
    {
      "id": "chubb-2026-dementia",
      "clusterCount": 1,
      "score": 81,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T17:30:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "Chubb Life香港推出创新「Side by Side」认知障碍症保险计划。",
        "tc": "Chubb Life香港推出創新「Side by Side」認知障礙症保險計劃。"
      },
      "summary": {
        "sc": "Chubb Life香港推出创新「Side by Side」认知障碍症保险计划，获评Products & Services Excellence 2026。该产品填补了香港市场对认知障碍专项保障的空白。[EN原文]",
        "tc": "Chubb推出認知障礙症專項保險"
      },
      "why": {
        "sc": "认知障碍保障，也是香港老龄化社会刚需，产品差异化明显。",
        "tc": "認知障礙保障，也是老齡化剛需。"
      },
      "actions": {
        "front": {
          "sc": "50+客户认知障碍保障新选择",
          "tc": "50+客戶新選擇"
        },
        "midback": {
          "sc": "更新老龄保障产品对比",
          "tc": "更新老齡保障對比"
        },
        "lead": {
          "sc": "银发市场差异化产品策略",
          "tc": "銀髮市場差異化"
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "Chubb/LinkedIn",
        "tc": "Chubb/LinkedIn",
        "lang": "en"
      },
      "boards": [
        "product",
        "firm"
      ],
      "tags": {
        "sc": [
          "Chubb",
          "认知障碍",
          "创新",
          "2026"
        ],
        "tc": [
          "Chubb",
          "認知障礙",
          "創新",
          "2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-03-24T10:00:00+08:00",
      "originalUrl": "https://hk.linkedin.com/company/chubb-life-hong-kong",
      "sourceKey": "chubb:dementia-2026",
      "sourceTier": "insurer",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "aof-hkimr-family-office-202603",
      "clusterCount": 1,
      "score": 75,
      "verifyStatus": "verified",
      "sourceTier": "pro",
      "sourceKey": "aof-hkimr",
      "title": {
        "sc": "香港金融学院报告：家族办公室生态 · 慈善 + 影响力投资 + 风险管理",
        "tc": "香港金融學院報告：家族辦公室生態 · 慈善 + 影響力投資 + 風險管理"
      },
      "summary": {
        "sc": "香港金融学院（AoF）下属 HKIMR 发布《Beyond Wealth》报告（2026.03），深入分析香港家办生态：69%的家办提供遗产/继承规划与信托服务，56%提供家族治理服务。报告提出以慈善、影响力投资和风险管理三轴推进家办生态建设。",
        "tc": "香港金融學院（AoF）下屬 HKIMR 發布《Beyond Wealth》報告（2026.03），深入分析香港家辦生態：69%的家辦提供遺產/繼承規劃與信託服務，56%提供家族治理服務。報告提出以慈善、影響力投資和風險管理三軸推進家辦生態建設。"
      },
      "why": {
        "sc": "69% 家办做遗产规划→保险和信托是家办服务的标配而非选配。这是一份「家办到底在做什么」的权威数据源，比任何营销话术都好用。",
        "tc": "69% 家辦做遺產規劃→保險和信託是家辦服務的標配而非選配。這是一份「家辦到底在做什麼」的權威數據源，比任何營銷話術都好用。"
      },
      "actions": {
        "front": {
          "sc": "保险是家办服务标配，可据此设计客户提案",
          "tc": "保險是家辦服務標配，可據此設計客戶提案"
        },
        "midback": {
          "sc": "了解家办生态结构对跨境合规有参考价值",
          "tc": "了解家辦生態結構對跨境合規有參考價值"
        },
        "lead": {
          "sc": "69%数据可用于团队培训和客户教育",
          "tc": "69%數據可用於團隊培訓和客戶教育"
        },
        "cross": {
          "sc": "遗产规划+信托服务的标准化是跨境架构基石",
          "tc": "遺產規劃+信託服務的標準化是跨境架構基石"
        }
      },
      "rolesImpact": {
        "front": 3,
        "midback": 2,
        "lead": 3,
        "cross": 4
      },
      "source": {
        "sc": "AoF / HKIMR",
        "lang": "zh"
      },
      "boards": [
        "family"
      ],
      "themes": [
        "family-office",
        "offshore"
      ],
      "tags": {
        "sc": [
          "家办",
          "遗产规划",
          "信托",
          "慈善"
        ],
        "tc": [
          "家辦",
          "遺產規劃",
          "信託",
          "慈善"
        ]
      },
      "contentKind": "stats",
      "publishedAt": "2026-03-20T10:00:00+08:00",
      "originalUrl": "https://www.aof.org.hk/docs/default-source/hkimr/applied-research-report/forep.pdf"
    },
    {
      "id": "aia-2025-annual-results",
      "clusterCount": 1,
      "score": 88,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": false,
      "ingestedAt": "2026-07-28T18:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "AIA 2025年全年业绩创新高：香港VONB+28% 每股股息+10%。",
        "tc": "AIA 2025年全年業績創新高：香港VONB+28% 每股股息+10%。"
      },
      "summary": {
        "sc": "友邦保险2025年全年业绩创新高，香港业务VONB增长28%，全年每股股息增加10%。同步宣布新一轮17亿美元股份回购。Q1 VONB达15亿美元同比+13%。[EN原文]",
        "tc": "AIA全年VONB創新高，香港+28%"
      },
      "why": {
        "sc": "AIA香港业绩持续领跑，也是市场信心的最直接量化指标。",
        "tc": "AIA業績，也是市場信心量化指標。"
      },
      "actions": {
        "front": {
          "sc": "客户问AIA业绩时可直接引用",
          "tc": "客戶問業績時引用"
        },
        "midback": {
          "sc": "更新AIA年度KPI档案",
          "tc": "更新KPI檔案"
        },
        "lead": {
          "sc": "AIA业绩趋势=团队产品策略参考",
          "tc": "團隊策略參考"
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "AIA 业绩公告",
        "tc": "AIA 業績公告",
        "lang": "en"
      },
      "boards": [
        "firm",
        "macro"
      ],
      "tags": {
        "sc": [
          "AIA",
          "VONB",
          "全年业绩",
          "2025"
        ],
        "tc": [
          "AIA",
          "VONB",
          "全年業績",
          "2025"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-03-19T09:00:00+08:00",
      "originalUrl": "https://www.aia.com/zh-hk/media-centre/press-releases/2026/aia-group-press-release-20260319",
      "sourceKey": "aia",
      "sourceTier": "insurer",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "hsbc-life-2026-hnw-pitchbook",
      "clusterCount": 1,
      "score": 82,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T17:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "汇丰保险发布2026高净值财富传承规划报告。",
        "tc": "滙豐保險發布2026高淨值財富傳承規劃報告。"
      },
      "summary": {
        "sc": "汇丰保险2026年3月发布高净值财富传承规划报告，显示仅41%高净值人士制定完整传承计划。汇丰已发行10份单张超5000万美元的大额保单，彰显市场领先地位。[EN原文]",
        "tc": "滙豐發布高淨值傳承報告，已發10張超5000萬美元保單"
      },
      "why": {
        "sc": "汇丰在高净值市场的话语权，也是银保渠道最大优势。",
        "tc": "滙豐高淨值市場話語權。"
      },
      "actions": {
        "front": {
          "sc": "高净值客户沟通中引用汇丰数据",
          "tc": "高淨值客戶溝通"
        },
        "midback": {
          "sc": "更新高净值市场数据",
          "tc": "更新市場數據"
        },
        "lead": {
          "sc": "银保渠道高净值客群策略",
          "tc": "銀保渠道策略"
        },
        "cross": {
          "sc": "跨境高净值解决方案",
          "tc": "跨境高淨值方案"
        }
      },
      "source": {
        "sc": "汇丰保险",
        "tc": "滙豐保險",
        "lang": "zh"
      },
      "boards": [
        "product",
        "firm"
      ],
      "tags": {
        "sc": [
          "汇丰",
          "高净值",
          "传承",
          "大额保单"
        ],
        "tc": [
          "滙豐",
          "高淨值",
          "傳承",
          "大額保單"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-03-17T10:00:00+08:00",
      "originalUrl": "https://www.life.hsbc.com/-/media/life/pdfs/260317-hsbc-life-hnw-pitchbook-sc.pdf",
      "sourceKey": "hsbc",
      "sourceTier": "insurer",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "prudential-20260317-youth",
      "clusterCount": 1,
      "score": 76,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T16:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "保诚推出「动感守护宝」专为18-30岁年轻一代设计。",
        "tc": "保誠推出「動感守護寶」專為18-30歲年輕一代設計。"
      },
      "summary": {
        "sc": "保诚2026年3月17日推出「动感守护宝」保障计划，专为18至30岁、生活方式多元的年轻世代设计，保障灵活可调。",
        "tc": "保誠3月17日推出年輕世代保障計劃"
      },
      "why": {
        "sc": "年轻客户细分产品，也是保诚差异化策略，IFA可拓展客群。",
        "tc": "年輕客戶細分產品。"
      },
      "actions": {
        "front": {
          "sc": "年轻客户拓客新工具",
          "tc": "年輕客戶拓客工具"
        },
        "midback": {
          "sc": "更新产品库",
          "tc": "更新產品庫"
        },
        "lead": {
          "sc": "年轻客群团队策略调整",
          "tc": "年輕客群策略"
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "保诚新闻稿",
        "tc": "保誠新聞稿",
        "lang": "zh"
      },
      "boards": [
        "product",
        "firm"
      ],
      "tags": {
        "sc": [
          "保诚",
          "年轻",
          "保障",
          "新产品"
        ],
        "tc": [
          "保誠",
          "年輕",
          "保障",
          "新產品"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-03-17T10:00:00+08:00",
      "originalUrl": "https://www.prudential.com.hk/tc/about-us/newsroom/prudential-launches-pruchoice-power-up-go-insurance/",
      "sourceKey": "prudential",
      "sourceTier": "insurer",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "sunlife-202603-sp-upgrade",
      "clusterCount": 1,
      "score": 86,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": false,
      "ingestedAt": "2026-07-28T22:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "标普上调Sun Life永明香港评级至AA 展望稳定。",
        "tc": "標普上調Sun Life永明香港評級至AA 展望穩定。"
      },
      "summary": {
        "sc": "S&P于2026年3月16日将Sun Life香港的财务实力和发行人信用评级从AA-上调至AA，展望稳定。永明表示此为重要里程碑，肯定其稳健财务实力和业务增长。APE于2025年破100亿港元。",
        "tc": "S&P將永明香港評級從AA-上調至AA"
      },
      "why": {
        "sc": "永明是近期唯一获上调的保司，也是市场对其财务实力的最高认可。",
        "tc": "永明近期唯一獲上調保司。"
      },
      "actions": {
        "front": {
          "sc": "永明客户=评级背书",
          "tc": "永明客戶評級背書"
        },
        "midback": {
          "sc": "归档评级变化",
          "tc": "歸檔評級變化"
        },
        "lead": {
          "sc": "评级上调=合作优先级提升",
          "tc": "合作優先級提升"
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "S&P/永明",
        "tc": "S&P/永明",
        "lang": "zh"
      },
      "boards": [
        "firm"
      ],
      "tags": {
        "sc": [
          "永明",
          "标普",
          "评级上调",
          "AA",
          "2026"
        ],
        "tc": [
          "永明",
          "標普",
          "評級上調",
          "AA",
          "2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-03-16T10:00:00+08:00",
      "originalUrl": "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/2026/sun-life-hong-kong-upgraded-to-aa-rating-by-sp/",
      "sourceKey": "sunlife",
      "sourceTier": "insurer",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "hkma-ia-2026-genai-sandbox",
      "clusterCount": 1,
      "score": 87,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": false,
      "ingestedAt": "2026-07-29T00:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "香港金融监管联合推出GenAI Sandbox++：用AI监管AI风险。",
        "tc": "香港金融監管聯合推出GenAI Sandbox++：用AI監管AI風險。"
      },
      "summary": {
        "sc": "香港保监局、金管局、证监会联合推出GenAI Sandbox++(2026年3月)，在2024年GenAI沙盒基础上扩展至银行、证券、资管全金融领域。聚焦三大场景：风险管理、反欺诈、客户体验。标志AI监管从'安全测试'升级为'生产级监管'。[EN原文]",
        "tc": "GenAI Sandbox++升級:用AI監管AI"
      },
      "why": {
        "sc": "金融监管联合推出AI沙盒，也是全行业AI合规框架的雏形。",
        "tc": "金融監管聯合AI沙盒，也是行業AI合規雛形。"
      },
      "actions": {
        "front": {
          "sc": "关注AI核保/理赔对客户体验的提升",
          "tc": "關注AI核保/理賠"
        },
        "midback": {
          "sc": "评估AI工具在合规监控中的适用性",
          "tc": "評估AI合規工具"
        },
        "lead": {
          "sc": "AI沙盒=团队数字化升级的窗口期",
          "tc": "AI沙盒=數字化窗口期"
        },
        "cross": {
          "sc": "AI跨境监管=未来业务合规的新维度",
          "tc": "AI跨境監管=新維度"
        }
      },
      "source": {
        "sc": "IA/HKMA/SFC",
        "tc": "IA/HKMA/SFC",
        "lang": "en"
      },
      "boards": [
        "tech",
        "regulatory"
      ],
      "tags": {
        "sc": [
          "GenAI",
          "沙盒",
          "监管",
          "2026"
        ],
        "tc": [
          "GenAI",
          "沙盒",
          "監管",
          "2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-03-15T10:00:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/news/hong-kong-finance-regulators-push-ai-police-ai-risks",
      "sourceKey": "insuranceasia",
      "sourceTier": "pro",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "manulife-202603-new-products",
      "clusterCount": 1,
      "score": 76,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:30:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "宏利香港推出两款新分红人寿保险储蓄计划。",
        "tc": "宏利香港推出兩款新分紅人壽保險儲蓄計劃。"
      },
      "summary": {
        "sc": "宏利香港于2026年3月推出两款新分红人寿保险储蓄计划，以满足客户对财务保障和财富增值的多元化需求。[EN原文]",
        "tc": "宏利香港3月推出兩款新分紅儲蓄計劃"
      },
      "why": {
        "sc": "宏利新产品矩阵扩展，为IFA提供更多分红险选择。",
        "tc": "宏利產品矩陣擴展。"
      },
      "actions": {
        "front": {
          "sc": "了解新产品特点，更新产品对比表",
          "tc": "了解新產品特點"
        },
        "midback": {
          "sc": "收集新产品资料和保费费率",
          "tc": "收集新產品資料"
        },
        "lead": {
          "sc": "评估新产品在团队产品组合中的定位",
          "tc": "評估新產品定位"
        },
        "cross": {
          "sc": "新产品是否适合跨境高净值客户",
          "tc": "評估對跨境客戶的適合性"
        }
      },
      "source": {
        "sc": "Manulife HK 新闻稿",
        "tc": "Manulife HK 新聞稿",
        "lang": "en"
      },
      "boards": [
        "product",
        "firm"
      ],
      "tags": {
        "sc": [
          "宏利",
          "分红险",
          "新产品"
        ],
        "tc": [
          "宏利",
          "分紅險",
          "新產品"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-03-15T10:00:00+08:00",
      "originalUrl": "https://www.linkedin.com/posts/manulife-hong-kong-and-macau",
      "sourceKey": "manulife",
      "sourceTier": "insurer",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20260310-rbc-consult-close",
      "clusterCount": 1,
      "score": 84,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:30:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "保监局RBC制度修订咨询截止：3月10日公众意见提交结束。",
        "tc": "保監局RBC制度修訂諮詢截止：3月10日公眾意見提交結束。"
      },
      "summary": {
        "sc": "保监局就《保险业（估值及资本）规则》拟议修订进行公众咨询，咨询期自2026年2月11日起至3月10日结束。修订旨在改善香港作为全球风险管理中心的竞争力、激励基建投资。",
        "tc": "保監局RBC修訂諮詢3月10日截止"
      },
      "why": {
        "sc": "RBC首次大规模修订，储蓄险资本要求可能翻倍，影响未来产品供给。",
        "tc": "RBC首次大規模修訂，影響產品供給。"
      },
      "actions": {
        "front": {
          "sc": "关注RBC修订对高演示产品的影响",
          "tc": "關注RBC修訂對高演示產品的影響"
        },
        "midback": {
          "sc": "跟踪RBC修订进度，更新合规评估",
          "tc": "更新合規評估"
        },
        "lead": {
          "sc": "评估RBC修订对团队产品策略的影响",
          "tc": "評估對團隊產品策略的影響"
        },
        "cross": {
          "sc": "RBC修订可能影响跨境再保险安排",
          "tc": "RBC修訂可能影響跨境再保"
        }
      },
      "source": {
        "sc": "IA 保监局咨询文件",
        "tc": "IA 保監局諮詢文件",
        "lang": "en"
      },
      "boards": [
        "regulatory"
      ],
      "tags": {
        "sc": [
          "RBC",
          "咨询",
          "资本规则",
          "修订"
        ],
        "tc": [
          "RBC",
          "諮詢",
          "資本規則",
          "修訂"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-03-10T18:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/en/infocenter/press_releases/20260211.html",
      "sourceKey": "ia",
      "sourceTier": "official",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20260305-genai-sandbox",
      "title": {
        "sc": "监管机构推出 GenA.I. 沙盒++ 覆盖保险等多元金融领域（2026-03-05）。",
        "tc": "監管機構推出 GenA.I. 沙盒++ 覆蓋保險等多元金融領域（2026-03-05）。"
      },
      "summary": {
        "sc": "金管局、证监会、保监局、积金局与数码港联合宣布扩展生成式AI沙盒++，覆盖银行、证券、资管、保险、强积金与储值支付工具，促进可控创新。",
        "tc": "金管局、證監會、保監局、積金局與數碼港聯合宣布擴展生成式AI沙盒++，覆蓋銀行、證券、資管、保險、強積金與儲值支付工具，促進可控創新。"
      },
      "why": {
        "sc": "官方为保险科技与中介侧AI工具划出合规试验路径。",
        "tc": "官方為保險科技與中介側AI工具劃出合規試驗路徑。"
      },
      "actions": {
        "front": {
          "sc": "只用公司核准AI工具；输出须人工复核。",
          "tc": "只用公司核准AI工具；輸出須人工複核。"
        },
        "midback": {
          "sc": "跟踪保司/业界沙盒用例。｜AI清单、数据与隐私评估。",
          "tc": "跟踪保司/業界沙盒用例。｜AI清單、數據與隱私評估。"
        },
        "lead": {
          "sc": "科技路线图对齐监管沙盒方向。",
          "tc": "科技路線圖對齊監管沙盒方向。"
        },
        "cross": {
          "sc": "跨境数据+AI更敏感。",
          "tc": "跨境數據+AI更敏感。"
        }
      },
      "source": {
        "sc": "保监局新闻稿/联合通函 2026-03-05",
        "tc": "保監局新聞稿/聯合通函 2026-03-05"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "GenAI",
          "沙盒",
          "保险科技"
        ],
        "tc": [
          "GenAI",
          "沙盒",
          "保險科技"
        ]
      },
      "themes": [
        "tech",
        "reg"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 2,
        "lead": 2,
        "cross": 1
      },
      "publishedAt": "2026-03-05T12:00:00+08:00",
      "score": 82,
      "verifyStatus": "verified",
      "featured": false,
      "originalUrl": "https://www.ia.org.hk/tc/infocenter/press_releases/20260305.html",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "reg",
        "tech"
      ],
      "contentKind": "circular"
    },
    {
      "id": "newcies-2026-3200apps-95b",
      "clusterCount": 1,
      "score": 82,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "govhk",
      "title": {
        "sc": "新CIES 两周年：3,200宗申请，预计吸引投资 950 亿港元",
        "tc": "新CIES 兩週年：3,200宗申請，預計吸引投資 950 億港元"
      },
      "summary": {
        "sc": "投资推广署公布新资本投资者入境计划（New CIES）两年里程碑：累计接获近 3,200 宗申请，预计总投资约 950 亿港元。2026 年 3 月生效的新措施允许以家族办公室管理的私人公司持有投资，首次将 CIES 与家办税务优惠联动。",
        "tc": "投資推廣署公布新資本投資者入境計劃（New CIES）兩年里程碑：累計接獲近 3,200 宗申請，預計總投資約 950 億港元。2026 年 3 月生效的新措施允許以家族辦公室管理的私人公司持有投資，首次將 CIES 與家辦稅務優惠聯動。"
      },
      "why": {
        "sc": "950 亿不只是钱——是 3,200 个超高净值家庭正式进入香港财富管理体系。CIES 与家办税务优惠联动后，每一笔 CIES 投资都可能衍生出保险配置、信托架构和代际传承需求。",
        "tc": "950 億不只是錢——是 3,200 個超高淨值家庭正式進入香港財富管理體系。CIES 與家辦稅務優惠聯動後，每一筆 CIES 投資都可能衍生出保險配置、信託架構和代際傳承需求。"
      },
      "actions": {
        "front": {
          "sc": "CIES客户是高净值寿险和年金产品的精准受众",
          "tc": "CIES客戶是高淨值壽險和年金產品的精準受眾"
        },
        "midback": {
          "sc": "CIES+家办税务优惠联动是新合规要点",
          "tc": "CIES+家辦稅務優惠聯動是新合規要點"
        },
        "lead": {
          "sc": "950亿/3200个家庭=跨境财富管理赛道规模证明",
          "tc": "950億/3200個家庭=跨境財富管理賽道規模證明"
        },
        "cross": {
          "sc": "CIES是跨境架构的核心入口场景",
          "tc": "CIES是跨境架構的核心入口場景"
        }
      },
      "rolesImpact": {
        "front": 4,
        "midback": 3,
        "lead": 4,
        "cross": 5
      },
      "source": {
        "sc": "InvestHK · GovHK",
        "lang": "zh"
      },
      "boards": [
        "family",
        "market"
      ],
      "themes": [
        "offshore",
        "family-office"
      ],
      "tags": {
        "sc": [
          "CIES",
          "投资移民",
          "家办"
        ],
        "tc": [
          "CIES",
          "投資移民",
          "家辦"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2026-03-01T10:00:00+08:00",
      "originalUrl": "https://www.investhk.gov.hk/zh-hk/news/two-year-milestone-new-capital-investment-entrant-scheme-attracts-nearly-3-200-applications-with-expected-investment-of-about-hk-95-billion-reflecting-global-confidence-in-hong-kong/"
    },
    {
      "id": "ia-budget-20260225",
      "title": {
        "sc": "保监局欢迎2026-27财政预算案中与国家规划对接的措施。",
        "tc": "保監局歡迎2026-27財政預算案中與國家規劃對接的措施。"
      },
      "summary": {
        "sc": "保监局2026年2月25日发稿，欢迎2026-27年度《财政预算案》中多项与国家「十五五」规划对接的政策措施，强调巩固香港保险与风险管理中心角色。",
        "tc": "保監局2026年2月25日發稿，歡迎2026-27年度《財政預算案》中多項與國家「十五五」規劃對接的政策措施，強調鞏固香港保險與風險管理中心角色。"
      },
      "why": {
        "sc": "政策层面对「离岸风险管理中心」定位的官方背书，利好长期架构叙事。",
        "tc": "政策層面對「離岸風險管理中心」定位的官方背書，利好長期架構敘事。"
      },
      "actions": {
        "front": {
          "sc": "对客可用官方定位做背景，勿引申为具体产品承诺。",
          "tc": "對客可用官方定位做背景，勿引申為具體產品承諾。"
        },
        "midback": {
          "sc": "收集预算案中与保险、家办、绿色金融相关条款做内训。｜关注后续立法/指引是否落地为中介义务。",
          "tc": "收集預算案中與保險、家辦、綠色金融相關條款做內訓。｜關注後續立法/指引是否落地為中介義務。"
        },
        "lead": {
          "sc": "战略叙事对齐「风险管理中心」而非短期套利。",
          "tc": "戰略敘事對齊「風險管理中心」而非短期套利。"
        },
        "cross": {
          "sc": "跨境家办与身份规划服务的政策窗口跟踪。",
          "tc": "跨境家辦與身份規劃服務的政策窗口跟踪。"
        }
      },
      "source": {
        "sc": "保险业监管局 · 新闻稿 2026-02-25",
        "tc": "保險業監管局 · 新聞稿 2026-02-25"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "财政预算案",
          "政策"
        ],
        "tc": [
          "財政預算案",
          "政策"
        ]
      },
      "themes": [
        "macro",
        "offshore",
        "reg"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 2,
        "lead": 3,
        "cross": 3
      },
      "publishedAt": "2026-02-25T12:00:00+08:00",
      "score": 76,
      "verifyStatus": "verified",
      "originalUrl": "https://www.ia.org.hk/tc/infocenter/press_releases/20260225.html",
      "featured": false,
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "family",
        "market",
        "reg"
      ],
      "contentKind": "press"
    },
    {
      "id": "ia-20260224-kpim-handbook",
      "title": {
        "sc": "保险人中介管理关键人员（KPIM）手册发布（2026-02-24）。",
        "tc": "保險人中介管理關鍵人員（KPIM）手冊發布（2026-02-24）。"
      },
      "summary": {
        "sc": "保监局2026年2月24日通函发布获授权保险人「中介管理控制职能关键人员」手册，厘清保司侧对中介管理的控制期望与职责框架。",
        "tc": "保監局2026年2月24日通函發布獲授權保險人「中介管理控制職能關鍵人員」手冊，釐清保司側對中介管理的控制期望與職責框架。"
      },
      "why": {
        "sc": "保司对经纪/代理的管理加码，签约与质检标准会更细。",
        "tc": "保司對經紀/代理的管理加碼，簽約與質檢標準會更細。"
      },
      "actions": {
        "front": {
          "sc": "配合保司培训与质量抽检要求。",
          "tc": "配合保司培訓與質量抽檢要求。"
        },
        "midback": {
          "sc": "对接保司 KPIM 联络窗口与课程。｜关注保司对中介的额外管控条款。",
          "tc": "對接保司 KPIM 聯絡窗口與課程。｜關注保司對中介的額外管控條款。"
        },
        "lead": {
          "sc": "商务谈判纳入「中介管理配合成本」。",
          "tc": "商務談判納入「中介管理配合成本」。"
        },
        "cross": {
          "sc": "无直接动作。",
          "tc": "無直接動作。"
        }
      },
      "source": {
        "sc": "保监局规管通函 2026-02-24",
        "tc": "保監局規管通函 2026-02-24"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "KPIM",
          "中介管理"
        ],
        "tc": [
          "KPIM",
          "中介管理"
        ]
      },
      "themes": [
        "compliance",
        "reg",
        "channel"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 3,
        "lead": 2,
        "cross": 0
      },
      "publishedAt": "2026-02-24T09:00:00+08:00",
      "score": 80,
      "verifyStatus": "verified",
      "featured": false,
      "originalUrl": "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/files/20260224_KPIM_Handbook_Circular.pdf",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "market",
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "sunlife-2025-ape-118",
      "clusterCount": 1,
      "score": 83,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": false,
      "ingestedAt": "2026-07-28T18:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "Sun Life永明2025年APE突破118亿港元创新高。",
        "tc": "Sun Life永明2025年APE突破118億港元創新高。"
      },
      "summary": {
        "sc": "Sun Life永明2025全年新造业务年度化标准保费(APE)达118亿港元，创历史新高。凭借多元化分销渠道策略在银保、经纪、代理三线同步增长。",
        "tc": "永明APE突破118億港元創歷史新高"
      },
      "why": {
        "sc": "永明进入百亿俱乐部，也是市场地位质变。",
        "tc": "永明進入百億俱樂部。"
      },
      "actions": {
        "front": {
          "sc": "永明业绩=客户品牌信心加分",
          "tc": "品牌信心加分"
        },
        "midback": {
          "sc": "更新永明KPI档案",
          "tc": "更新KPI檔案"
        },
        "lead": {
          "sc": "永明市场地位跃升对团队策略的影响",
          "tc": "永明市場地位躍升"
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "永明/保监局统计",
        "tc": "永明/保監局統計",
        "lang": "zh"
      },
      "boards": [
        "firm",
        "macro"
      ],
      "tags": {
        "sc": [
          "永明",
          "APE",
          "118亿",
          "2025"
        ],
        "tc": [
          "永明",
          "APE",
          "118億",
          "2025"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-02-15T10:00:00+08:00",
      "originalUrl": "https://hk.finance.yahoo.com/news/sun-life永明2025全年新造業務年度化標準保費達118億港元-104538638.html",
      "sourceKey": "yahoofinance",
      "sourceTier": "media",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20260213-low-altitude",
      "title": {
        "sc": "保险创新助力低空经济发展（2026-02-13）。",
        "tc": "保險創新助力低空經濟發展（2026-02-13）。"
      },
      "summary": {
        "sc": "保监局执行董事（一般业务）李明模2026年2月13日发表文章，讨论保险创新如何支持低空经济等新兴产业风险管理。",
        "tc": "保監局執行董事（一般業務）李明模2026年2月13日發表文章，討論保險創新如何支持低空經濟等新興產業風險管理。"
      },
      "why": {
        "sc": "一般业务/创新险种话题，丰富非寿险视角。",
        "tc": "一般業務/創新險種話題，豐富非壽險視角。"
      },
      "actions": {
        "front": {
          "sc": "寿险顾问作知识拓展即可。",
          "tc": "壽險顧問作知識拓展即可。"
        },
        "midback": {
          "sc": "一般业务创新案例库。｜新产品合规边界关注。",
          "tc": "一般業務創新案例庫。｜新產品合規邊界關注。"
        },
        "lead": {
          "sc": "创新业务机会扫描。",
          "tc": "創新業務機會掃描。"
        },
        "cross": {
          "sc": "产业客户话题。",
          "tc": "產業客戶話題。"
        }
      },
      "source": {
        "sc": "保监局文章 2026-02-13",
        "tc": "保監局文章 2026-02-13"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "低空经济",
          "创新",
          "一般业务"
        ],
        "tc": [
          "低空經濟",
          "創新",
          "一般業務"
        ]
      },
      "themes": [
        "firm",
        "macro",
        "tech"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 2,
        "lead": 2,
        "cross": 2
      },
      "publishedAt": "2026-02-13T10:00:00+08:00",
      "score": 78,
      "featured": false,
      "originalUrl": "https://www.ia.org.hk/tc/infocenter/speeches_articles/20260213.html",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T02:07:48+08:00",
      "evergreen": false,
      "clusterCount": 1,
      "verifyStatus": "verified",
      "boards": [
        "insurer",
        "market",
        "tech"
      ],
      "contentKind": "speech"
    },
    {
      "id": "ia-20260211-rbc-consult",
      "title": {
        "sc": "完善风险为本资本制度公众咨询启动（2026-02-11）。",
        "tc": "完善風險為本資本制度公眾諮詢啟動（2026-02-11）。"
      },
      "summary": {
        "sc": "保监局2026年2月11日就《保险业（估值及资本）规则》拟议修订展开公众咨询，旨在完善风险为本资本制度。",
        "tc": "保監局2026年2月11日就《保險業（估值及資本）規則》擬議修訂展開公眾諮詢，旨在完善風險為本資本制度。"
      },
      "why": {
        "sc": "资本规则微调会影响保司产品与投资策略中长期。",
        "tc": "資本規則微調會影響保司產品與投資策略中長期。"
      },
      "actions": {
        "front": {
          "sc": "关注咨询结果，勿过早对客承诺产品形态。",
          "tc": "關注諮詢結果，勿過早對客承諾產品形態。"
        },
        "midback": {
          "sc": "跟踪咨询文件要点。｜评估最终规则对保司尽调的影响。",
          "tc": "跟踪諮詢文件要點。｜評估最終規則對保司盡調的影響。"
        },
        "lead": {
          "sc": "战略层关注资本与产品供给。",
          "tc": "戰略層關注資本與產品供給。"
        },
        "cross": {
          "sc": "无直接动作。",
          "tc": "無直接動作。"
        }
      },
      "source": {
        "sc": "保监局新闻稿/咨询 2026-02-11",
        "tc": "保監局新聞稿/諮詢 2026-02-11"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "RBC",
          "咨询"
        ],
        "tc": [
          "RBC",
          "諮詢"
        ]
      },
      "themes": [
        "reg",
        "firm"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 2,
        "lead": 3,
        "cross": 1
      },
      "publishedAt": "2026-02-11T12:00:00+08:00",
      "score": 83,
      "verifyStatus": "verified",
      "featured": false,
      "originalUrl": "https://www.ia.org.hk/tc/infocenter/consultation_rbc_20260211.html",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "insurer",
        "reg"
      ],
      "contentKind": "press"
    },
    {
      "id": "ia-20260211-rbc-consult-launch",
      "clusterCount": 1,
      "score": 88,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:30:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "保监局就RBC资本规则修订启动公众咨询。",
        "tc": "保監局就RBC資本規則修訂啟動公眾諮詢。"
      },
      "summary": {
        "sc": "保监局2026年2月11日启动《保险业（估值及资本）规则》拟议修订的公众咨询。修订涵盖基建投资优惠资本待遇(下调20-30%)、离岸再保险排除机制、IUL匹配调整、加密资产资本处理等7大领域。咨询期至3月10日。",
        "tc": "保監局2月11日啟動RBC修訂公眾諮詢，涵蓋7大領域"
      },
      "why": {
        "sc": "RBC首次大修，直接影响所有保司资本结构和产品策略。",
        "tc": "RBC首次大修影響保司資本結構。"
      },
      "actions": {
        "front": {
          "sc": "高保证产品窗口期，主动向客户说明",
          "tc": "主動向客戶說明窗口期"
        },
        "midback": {
          "sc": "跟踪咨询进展，准备合规影响评估",
          "tc": "準備合規影響評估"
        },
        "lead": {
          "sc": "评估基建优惠对保司底层资产配置的影响",
          "tc": "評估基建優惠對保司資產配置影響"
        },
        "cross": {
          "sc": "IUL调整对跨境高净值客户的影响评估",
          "tc": "IUL調整對跨境高淨值客戶影響"
        }
      },
      "source": {
        "sc": "IA 保监局新闻稿",
        "tc": "IA 保監局新聞稿",
        "lang": "en"
      },
      "boards": [
        "regulatory",
        "product"
      ],
      "tags": {
        "sc": [
          "RBC",
          "咨询",
          "资本规则",
          "基建",
          "2026"
        ],
        "tc": [
          "RBC",
          "諮詢",
          "資本規則",
          "基建",
          "2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-02-11T10:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/en/infocenter/press_releases/20260211.html",
      "sourceKey": "ia",
      "sourceTier": "official",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "fstb-20260210-fo-3384",
      "clusterCount": 1,
      "score": 92,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": false,
      "ingestedAt": "2026-07-29T00:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "香港家族办公室达3384间 两年增25% 过半财富超5100万美元。",
        "tc": "香港家族辦公室達3384間 兩年增25% 過半財富超5100萬美元。"
      },
      "summary": {
        "sc": "财库局2026年2月公布研究：截至2025年底香港单一家族办公室达3384间，较2023年底净增681间(+25%)。过半管理财富超5100万美元。60%计划未来三年增配香港资产。新资本投资者入境计划已收到超3000宗申请，预计带来超900亿港元投资。",
        "tc": "香港家族辦公室達3384間+25% 60%計劃增配香港"
      },
      "why": {
        "sc": "家族办公室，超高净值客户的聚集地，跨境保险的最大买单方。",
        "tc": "家族辦公室，超高淨值客戶，跨境保險最大買單方。"
      },
      "actions": {
        "front": {
          "sc": "家办客户是分红大额保单的核心客群",
          "tc": "家辦客戶=大額保單核心客群"
        },
        "midback": {
          "sc": "归档家办市场数据",
          "tc": "歸檔家辦數據"
        },
        "lead": {
          "sc": "家办市场=团队高净值战略的基石",
          "tc": "家辦市場=高淨值戰略基石"
        },
        "cross": {
          "sc": "家办跨境资产配置=保险+信托+传承的综合方案",
          "tc": "保險+信託+傳承綜合方案"
        }
      },
      "source": {
        "sc": "财库局/Deloitte",
        "tc": "財庫局/Deloitte",
        "lang": "zh"
      },
      "boards": [
        "cross",
        "offshore"
      ],
      "tags": {
        "sc": [
          "家族办公室",
          "3384",
          "家办",
          "2026"
        ],
        "tc": [
          "家族辦公室",
          "3384",
          "家辦",
          "2026"
        ]
      },
      "contentKind": "report",
      "publishedAt": "2026-02-10T10:00:00+08:00",
      "originalUrl": "https://www.fstb.gov.hk/en/blog/blog100226.htm",
      "sourceKey": "govhk",
      "sourceTier": "official",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "hk-2026-newcies-3000",
      "clusterCount": 1,
      "score": 84,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-29T00:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "新资本投资者入境计划收逾3000宗申请 预计带来900亿投资。",
        "tc": "新資本投資者入境計劃收逾3000宗申請 預計帶來900億投資。"
      },
      "summary": {
        "sc": "财库局2026年2月公布：新资本投资者入境计划(New CIES)自推出以来已收到逾3000宗申请，若全部获批将带来超900亿港元投资。计划门槛为3000万港元，允许投资保险相关产品。2025年初放宽资产门槛后申请量加速增长。",
        "tc": "新CIES收逾3000宗申請 預計900億投資"
      },
      "why": {
        "sc": "CIES，超高净值内地客户获取香港身份的合规路径，保险需求入口。",
        "tc": "CIES，也是內地超高淨值客戶獲取香港身份路徑。"
      },
      "actions": {
        "front": {
          "sc": "CIES客户可配置保险产品满足投资要求",
          "tc": "CIES客戶可配置保險"
        },
        "midback": {
          "sc": "更新CIES规则和保险产品适配清单",
          "tc": "更新CIES適配清單"
        },
        "lead": {
          "sc": "CIES=高净值客户规模化获客渠道",
          "tc": "CIES=高淨值獲客渠道"
        },
        "cross": {
          "sc": "CIES+保险+家办=跨境财富管理铁三角",
          "tc": "CIES+保險+家辦=跨境鐵三角"
        }
      },
      "source": {
        "sc": "财库局",
        "tc": "財庫局",
        "lang": "zh"
      },
      "boards": [
        "cross",
        "offshore"
      ],
      "tags": {
        "sc": [
          "CIES",
          "投资移民",
          "3000宗",
          "900亿"
        ],
        "tc": [
          "CIES",
          "投資移民",
          "3000宗",
          "900億"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-02-10T10:00:00+08:00",
      "originalUrl": "https://www.fstb.gov.hk/en/blog/blog100226.htm",
      "sourceKey": "govhk",
      "sourceTier": "official",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "dlapiper-202602-gl16",
      "clusterCount": 1,
      "score": 84,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T20:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "DLA Piper法律解读：保监局修订GL16——产品治理、销售与薪酬全面升级。",
        "tc": "DLA Piper法律解讀：保監局修訂GL16——產品治理、銷售與薪酬全面升級。"
      },
      "summary": {
        "sc": "DLA Piper 2026年2月发布法律解读：保监局修订GL16（长期业务承保指引），3月31日生效。核心变化：加强产品治理委员会职责、销售流程适当性评估升级、薪酬结构须与公平待客对齐、售后管控常态化。任何规避行为将被视为恶意违规。[EN原文]",
        "tc": "DLA Piper:GL16修訂加強產品治理與公平待客"
      },
      "why": {
        "sc": "国际律所的法律解读，也是合规操作的实务指南。",
        "tc": "國際律所法律解讀，也是合規實務指南。"
      },
      "actions": {
        "front": {
          "sc": "了解GL16对销售流程的具体影响",
          "tc": "了解GL16對銷售影響"
        },
        "midback": {
          "sc": "以DLA解读为框架更新合规手册",
          "tc": "以DLA框架更新合規手冊"
        },
        "lead": {
          "sc": "GL16合规=团队运营底线",
          "tc": "GL16合規=運營底線"
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "DLA Piper",
        "tc": "DLA Piper",
        "lang": "en"
      },
      "boards": [
        "compliance",
        "regulatory"
      ],
      "tags": {
        "sc": [
          "DLA Piper",
          "GL16",
          "法律解读",
          "2026"
        ],
        "tc": [
          "DLA Piper",
          "GL16",
          "法律解讀",
          "2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-02-10T10:00:00+08:00",
      "originalUrl": "https://www.dlapiper.com/en-us/insights/publications/2026/03/insurance-authority-of-hong-kong-issues-revised-guideline",
      "sourceKey": "dlapiper:gl16-202602",
      "sourceTier": "pro",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "fstb-family-office-boom-20260210",
      "clusterCount": 1,
      "score": 78,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "govhk",
      "title": {
        "sc": "FSTB：家办热潮推动香港经济——CIES 预计吸资逾 900 亿港元",
        "tc": "FSTB：家辦熱潮推動香港經濟——CIES 預計吸資逾 900 億港元"
      },
      "summary": {
        "sc": "财经事务及库务局局长博客指出：香港家族办公室数量已超过 2,700 家，预计年底突破 3,000 家。新 CIES 若全部获批，预计带来逾 900 亿港元投资。家办生态正在推动资产管理、法律、会计、教育等专业服务的全面增长。",
        "tc": "財經事務及庫務局局長博客指出：香港家族辦公室數量已超過 2,700 家，預計年底突破 3,000 家。新 CIES 若全部獲批，預計帶來逾 900 億港元投資。家辦生態正在推動資產管理、法律、會計、教育等專業服務的全面增長。"
      },
      "why": {
        "sc": "2,700→3,000 家办的官方数据——这是香港家办赛道的权威规模证明。每一个家办都是一家「小企业」，需要公司注册、税务筹划、合规、秘书服务，是一整条企业服务价值链。",
        "tc": "2,700→3,000 家辦的官方數據——這是香港家辦賽道的權威規模證明。每一個家辦都是一家「小企業」，需要公司註冊、稅務籌劃、合規、秘書服務，是一整條企業服務價值鏈。"
      },
      "actions": {
        "front": {
          "sc": "家办客户需要的不只是保险，是综合服务能力",
          "tc": "家辦客戶需要的不只是保險，是綜合服務能力"
        },
        "midback": {
          "sc": "家办的合规框架涉及公司注册/税务/CRS等多个维度",
          "tc": "家辦的合規框架涉及公司註冊/稅務/CRS等多個維度"
        },
        "lead": {
          "sc": "3,000家办=一个正在形成的专业化服务市场",
          "tc": "3,000家辦=一個正在形成的專業化服務市場"
        },
        "cross": {
          "sc": "家办是企业服务+财富管理的交叉点",
          "tc": "家辦是企業服務+財富管理的交叉點"
        }
      },
      "rolesImpact": {
        "front": 3,
        "midback": 3,
        "lead": 4,
        "cross": 4
      },
      "source": {
        "sc": "FSTB · GovHK",
        "lang": "zh"
      },
      "boards": [
        "family",
        "market"
      ],
      "themes": [
        "family-office",
        "company-service"
      ],
      "tags": {
        "sc": [
          "家办",
          "企业服务",
          "FSTB"
        ],
        "tc": [
          "家辦",
          "企業服務",
          "FSTB"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2026-02-10T10:00:00+08:00",
      "originalUrl": "https://www.fstb.gov.hk/en/blog/blog100226.htm"
    },
    {
      "id": "ia-20260206-gl16-gl34",
      "title": {
        "sc": "修订 GL16 与 GL34：长期承保与分红基金管理（2026-02-06）。",
        "tc": "修訂 GL16 與 GL34：長期承保與分紅基金管理（2026-02-06）。"
      },
      "summary": {
        "sc": "保监局2026年2月6日通函同步发布修订版 GL16（长期业务承保，非C类）与 GL34（分红业务基金管理），进一步收紧产品设计、承保与分红治理期望。",
        "tc": "保監局2026年2月6日通函同步發布修訂版 GL16（長期業務承保，非C類）與 GL34（分紅業務基金管理），進一步收緊產品設計、承保與分紅治理期望。"
      },
      "why": {
        "sc": "产品可售形态与核保尺度可能调整，中台需跟进保司落实。",
        "tc": "產品可售形態與核保尺度可能調整，中台需跟進保司落實。"
      },
      "actions": {
        "front": {
          "sc": "关注保司核保/产品通告变更。",
          "tc": "關注保司核保/產品通告變更。"
        },
        "midback": {
          "sc": "建立 GL16/GL34 对照阅读笔记。｜评估对公司尽职调查清单的影响。",
          "tc": "建立 GL16/GL34 對照閱讀筆記。｜評估對公司盡職調查清單的影響。"
        },
        "lead": {
          "sc": "产品委员会跟踪保司落地时间表。",
          "tc": "產品委員會跟踪保司落地時間表。"
        },
        "cross": {
          "sc": "复杂健康/大额单预审提前。",
          "tc": "複雜健康/大額單預審提前。"
        }
      },
      "source": {
        "sc": "保监局规管通函 2026-02-06",
        "tc": "保監局規管通函 2026-02-06"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "GL16",
          "GL34",
          "承保"
        ],
        "tc": [
          "GL16",
          "GL34",
          "承保"
        ]
      },
      "themes": [
        "reg",
        "product",
        "par",
        "uw"
      ],
      "rolesImpact": {
        "front": 2,
        "midback": 3,
        "lead": 2,
        "cross": 2
      },
      "publishedAt": "2026-02-06T09:00:00+08:00",
      "score": 90,
      "verifyStatus": "verified",
      "featured": true,
      "originalUrl": "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/files/Circular_20260206_GL16_and_GL34.pdf",
      "clusterCount": 2,
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "product",
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "circ-20260201-crossborder",
      "clusterCount": 1,
      "score": 82,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T12:30:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "金融监管总局回复跨境保险通提案：与现行《保险法》冲突。",
        "tc": "金融監管總局回覆跨境保險通提案：與現行《保險法》衝突。"
      },
      "summary": {
        "sc": "2026年2月1日，金融监管总局回复关于推进'跨境保险通'的提案时表示，该建议与《保险法》关于保险业务须在境内开展的要求存在冲突。港澳的保险监管政策、产品费率等与内地差异较大，现阶段不具备试点条件。",
        "tc": "金融監管總局2月1日回覆跨境保險通提案，稱暫不具備試點條件"
      },
      "why": {
        "sc": "跨境保险通短期难落地，香港保险销售须严格在港完成。",
        "tc": "跨境保險通短期難落地。"
      },
      "actions": {
        "front": {
          "sc": "所有销售流程必须100%在香港境内完成",
          "tc": "銷售流程須100%在港完成"
        },
        "midback": {
          "sc": "更新跨境销售合规红线：严禁内地招揽",
          "tc": "更新跨境銷售合規紅線"
        },
        "lead": {
          "sc": "团队重申跨境销售合规底线",
          "tc": "團隊重申跨境銷售底線"
        },
        "cross": {
          "sc": "跨境客户：合法签单流程不可跳步",
          "tc": "跨境客戶簽單不可跳步"
        }
      },
      "source": {
        "sc": "证券时报/金融监管总局",
        "tc": "證券時報/金融監管總局",
        "lang": "zh"
      },
      "boards": [
        "regulatory",
        "compliance",
        "cross"
      ],
      "tags": {
        "sc": [
          "跨境保险通",
          "金融监管总局",
          "合规"
        ],
        "tc": [
          "跨境保險通",
          "金融監管總局",
          "合規"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-02-01T14:00:00+08:00",
      "originalUrl": "https://www.stcn.com/article/detail/1228440.html",
      "sourceKey": "circ:crossborder-20260201",
      "sourceTier": "media",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20260126-aff",
      "title": {
        "sc": "亚洲金融论坛2026：保监局开场发言（2026-01-26）。",
        "tc": "亞洲金融論壇2026：保監局開場發言（2026-01-26）。"
      },
      "summary": {
        "sc": "保监局执行董事刘中健于亚洲金融论坛2026讨论环节发表开场发言，强调香港保险与风险管理角色。",
        "tc": "保監局執行董事劉中健於亞洲金融論壇2026討論環節發表開場發言，強調香港保險與風險管理角色。"
      },
      "why": {
        "sc": "年初定调材料，适合年报开篇引用。",
        "tc": "年初定調材料，適合年報開篇引用。"
      },
      "actions": {
        "front": {
          "sc": "无直接销售动作。",
          "tc": "無直接銷售動作。"
        },
        "midback": {
          "sc": "归档为年度政策语境。｜无直接动作。",
          "tc": "歸檔為年度政策語境。｜無直接動作。"
        },
        "lead": {
          "sc": "年报/战略会开场可用。",
          "tc": "年報/戰略會開場可用。"
        },
        "cross": {
          "sc": "国际定位叙事。",
          "tc": "國際定位敘事。"
        }
      },
      "source": {
        "sc": "保监局演辞 2026-01-26",
        "tc": "保監局演辭 2026-01-26"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "亚洲金融论坛",
          "定位"
        ],
        "tc": [
          "亞洲金融論壇",
          "定位"
        ]
      },
      "themes": [
        "macro",
        "firm",
        "reg"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 2,
        "lead": 3,
        "cross": 2
      },
      "publishedAt": "2026-01-26T10:00:00+08:00",
      "score": 80,
      "featured": false,
      "originalUrl": "https://www.ia.org.hk/tc/infocenter/files/Asian_Financial_Forum_2026_CHI.pdf",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T02:07:48+08:00",
      "evergreen": false,
      "clusterCount": 1,
      "verifyStatus": "verified",
      "boards": [
        "insurer",
        "market",
        "reg"
      ],
      "contentKind": "speech"
    },
    {
      "id": "axa-20260126-redomicile",
      "clusterCount": 1,
      "score": 86,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": true,
      "ingestedAt": "2026-07-28T16:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "AXA安盛成功由百慕达迁册至香港。",
        "tc": "AXA安盛成功由百慕達遷冊至香港。"
      },
      "summary": {
        "sc": "AXA安盛2026年1月26日宣布成功将注册地由百慕达迁册至香港，正式更名为「安盛金融保险（香港）有限公司」。迁册标志着AXA对香港市场的长期承诺，巩固其亚太业务枢纽地位。",
        "tc": "AXA安盛1月26日成功遷冊回港"
      },
      "why": {
        "sc": "AXA是香港首家完成迁册的国际保险巨头，监管与市场意义重大。",
        "tc": "首家完成遷冊的國際保險巨頭。"
      },
      "actions": {
        "front": {
          "sc": "可向客户提及AXA迁册=香港市场信心",
          "tc": "提及遷冊=市場信心"
        },
        "midback": {
          "sc": "更新AXA法律实体档案",
          "tc": "更新法律實體檔案"
        },
        "lead": {
          "sc": "迁册后AXA产品策略可能调整",
          "tc": "關注產品策略調整"
        },
        "cross": {
          "sc": "迁册对跨境保单的潜在影响评估",
          "tc": "遷冊對跨境保單影響"
        }
      },
      "source": {
        "sc": "AXA 新闻稿",
        "tc": "AXA 新聞稿",
        "lang": "zh"
      },
      "boards": [
        "firm"
      ],
      "tags": {
        "sc": [
          "AXA",
          "迁册",
          "百慕达",
          "2026"
        ],
        "tc": [
          "AXA",
          "遷冊",
          "百慕達",
          "2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-01-26T09:00:00+08:00",
      "originalUrl": "https://hk.finance.yahoo.com/news/axa成功遷冊回港-015300166.html",
      "sourceKey": "yahoofinance",
      "sourceTier": "media",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20260123-stats-3q2025",
      "title": {
        "sc": "2025年前三季临时统计：长期新造约2645亿，同比约+55.9%（2026-01-23）。",
        "tc": "2025年前三季臨時統計：長期新造約2645億，同比約+55.9%（2026-01-23）。"
      },
      "summary": {
        "sc": "保监局2026年1月23日公布2025年前三季临时统计：长期业务（不含退休计划）新造保单保费约2645亿港元，同比上升约55.9%；第三季单季新造约907亿，同比约+68.8%。",
        "tc": "保監局2026年1月23日公布2025年前三季臨時統計：長期業務（不含退休計劃）新造保單保費約2645億港元，同比上升約55.9%；第三季單季新造約907億，同比約+68.8%。"
      },
      "why": {
        "sc": "高速增长期的关键官方切片，连接H1与全年数据。",
        "tc": "高速增長期的關鍵官方切片，連接H1與全年數據。"
      },
      "actions": {
        "front": {
          "sc": "引用时注明「前三季临时统计」。",
          "tc": "引用時註明「前三季臨時統計」。"
        },
        "midback": {
          "sc": "更新时间序列图。｜关注业务量对运营负荷。",
          "tc": "更新時間序列圖。｜關注業務量對運營負荷。"
        },
        "lead": {
          "sc": "季度复盘锚点。",
          "tc": "季度複盤錨點。"
        },
        "cross": {
          "sc": "需求旺盛背景下更重合规。",
          "tc": "需求旺盛背景下更重合規。"
        }
      },
      "source": {
        "sc": "保监局新闻稿 2026-01-23",
        "tc": "保監局新聞稿 2026-01-23"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "临时统计",
          "2025Q1-Q3"
        ],
        "tc": [
          "臨時統計",
          "2025Q1-Q3"
        ]
      },
      "themes": [
        "macro",
        "channel",
        "firm"
      ],
      "rolesImpact": {
        "front": 2,
        "midback": 2,
        "lead": 3,
        "cross": 2
      },
      "publishedAt": "2026-01-23T12:00:00+08:00",
      "score": 92,
      "featured": true,
      "originalUrl": "https://www.ia.org.hk/en/infocenter/press_releases/20260123.html",
      "note": {
        "sc": "数字请回新闻稿表格核对。",
        "tc": "數字請回新聞稿表格核對。"
      },
      "verifyStatus": "verified",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T02:07:48+08:00",
      "evergreen": false,
      "clusterCount": 1,
      "boards": [
        "insurer",
        "market"
      ],
      "contentKind": "press"
    },
    {
      "id": "ia-20260123-q3stats",
      "clusterCount": 1,
      "score": 85,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T13:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "保监局公布2025年前三季临时统计：新造保费2644亿港元同比+55.9%。",
        "tc": "保監局公布2025年前三季臨時統計：新造保費2644億港元同比+55.9%。"
      },
      "summary": {
        "sc": "保监局2026年1月23日公布2025年前三季临时统计：长期业务新造保费2644.52亿港元同比+55.9%，其中分红业务新保单保费2262.75亿港元同比+60.1%。终身寿险占比80.5%，储蓄寿险10.6%。",
        "tc": "保監局公布2025前三季統計，分紅保費同比+60%"
      },
      "why": {
        "sc": "分红险贡献绝对主力，演示利率上限前抢购潮效应明显。",
        "tc": "分紅險貢獻絕對主力。"
      },
      "actions": {
        "front": {
          "sc": "用官方数据向客户展示香港保险市场增长趋势",
          "tc": "用官方數據展示市場趨勢"
        },
        "midback": {
          "sc": "更新行业数据手册",
          "tc": "更新行業數據手冊"
        },
        "lead": {
          "sc": "数据驱动团队业务策略调整",
          "tc": "數據驅動業務策略"
        },
        "cross": {
          "sc": "内地访客保费数据辅助跨境营销",
          "tc": "內地訪客數據輔助跨境營銷"
        }
      },
      "source": {
        "sc": "IA 保监局统计",
        "tc": "IA 保監局統計",
        "lang": "zh"
      },
      "boards": [
        "regulatory",
        "macro"
      ],
      "tags": {
        "sc": [
          "Q3统计",
          "保费",
          "分红",
          "2025"
        ],
        "tc": [
          "Q3統計",
          "保費",
          "分紅",
          "2025"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-01-23T10:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/en/infocenter/press_releases/20260123.html",
      "sourceKey": "ia",
      "sourceTier": "official",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "evident-2026-insurance-ai",
      "clusterCount": 1,
      "score": 78,
      "verifyStatus": "pending",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-29T00:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "Evident报告：68%保险AI部署已转向生成式/代理式AI。",
        "tc": "Evident報告：68%保險AI部署已轉向生成式/代理式AI。"
      },
      "summary": {
        "sc": "Evident 2025 Q4 Insurance AI Use Case Tracker显示：68%公开披露的保险AI部署已是生成式或代理式AI，其中代理式AI占21%。2026年核心问题是保险AI如何从试点走向规模化生产。[EN原文]",
        "tc": "68%保險AI已轉向生成式/代理式AI"
      },
      "why": {
        "sc": "AI从辅助工具变成独立执行者，也是保险工作流的根本变革。",
        "tc": "AI從輔助變執行者，也是工作流變革。"
      },
      "actions": {
        "front": {
          "sc": "Agentic AI=保险销售流程的重构者",
          "tc": "Agentic AI=銷售流程重構"
        },
        "midback": {
          "sc": "评估代理式AI对合规流程的影响",
          "tc": "評估代理式AI影響"
        },
        "lead": {
          "sc": "AI部署速度=团队信息竞争力",
          "tc": "AI部署=信息競爭力"
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "Evident",
        "tc": "Evident",
        "lang": "en"
      },
      "boards": [
        "tech"
      ],
      "tags": {
        "sc": [
          "Agentic AI",
          "GenAI",
          "保险科技",
          "2026"
        ],
        "tc": [
          "Agentic AI",
          "GenAI",
          "保險科技",
          "2026"
        ]
      },
      "contentKind": "report",
      "publishedAt": "2026-01-15T10:00:00+08:00",
      "originalUrl": "https://events.newton.media/Agentic-and-Generative-AI-for-Insurance-USA",
      "sourceKey": "evident:ai-tracker-2026",
      "sourceTier": "media",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-gl34-20260331",
      "title": {
        "sc": "修订 GL34 分红业务基金管理：主体2026-03-31 生效，公司政策段2026-06-30。",
        "tc": "修訂 GL34 分紅業務基金管理：主體2026-03-31 生效，公司政策段2026-06-30。"
      },
      "summary": {
        "sc": "保监局修订《指引34》关于分红业务基金管治与管理的期望。修订版主体自2026年3月31日起生效；其中公司政策（第4节）自2026年6月30日起生效，要求更清晰的股东与保单持有人之间可分配盈余/利润分配政策。",
        "tc": "保監局修訂《指引34》關於分紅業務基金管治與管理的期望。修訂版主體自2026年3月31日起生效；其中公司政策（第4節）自2026年6月30日起生效，要求更清晰的股東與保單持有人之間可分配盈餘/利潤分配政策。"
      },
      "why": {
        "sc": "影响分红治理与客户沟通中的「非保证」解释深度，产品与合规中台需跟进保司披露。",
        "tc": "影響分紅治理與客戶溝通中的「非保證」解釋深度，產品與合規中台需跟進保司披露。"
      },
      "actions": {
        "front": {
          "sc": "讲解分红时强调董事会裁量与基金治理，不把演示当承诺。",
          "tc": "講解分紅時強調董事會裁量與基金治理，不把演示當承諾。"
        },
        "midback": {
          "sc": "收集各保司就 GL34 的公开披露与产品说明更新。｜关注保司政策生效节点，更新尽职调查清单。",
          "tc": "收集各保司就 GL34 的公開披露與產品說明更新。｜關注保司政策生效節點，更新盡職調查清單。"
        },
        "lead": {
          "sc": "战略会把「分红治理透明度」纳入保司评分。",
          "tc": "戰略會把「分紅治理透明度」納入保司評分。"
        },
        "cross": {
          "sc": "家族办公室客户更在意治理与实现路径，可作专业加分项。",
          "tc": "家族辦公室客戶更在意治理與實現路徑，可作專業加分項。"
        }
      },
      "source": {
        "sc": "法律专业解读 · 保监局 GL34 修订",
        "tc": "法律專業解讀 · 保監局 GL34 修訂"
      },
      "sourceTier": "pro",
      "tags": {
        "sc": [
          "GL34",
          "分红基金",
          "管治"
        ],
        "tc": [
          "GL34",
          "分紅基金",
          "管治"
        ]
      },
      "themes": [
        "reg",
        "par",
        "product"
      ],
      "rolesImpact": {
        "front": 2,
        "midback": 3,
        "lead": 2,
        "cross": 2
      },
      "publishedAt": "2026-01-15T10:00:00+08:00",
      "effectiveAt": "2026-03-31",
      "score": 88,
      "verifyStatus": "verified",
      "originalUrl": "https://www.jdsupra.com/legalnews/hong-kong-insurance-authority-issues-8765538/",
      "featured": true,
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "f1c2d3d2bf09",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": true,
      "boards": [
        "product",
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "ebact-2025-hk-market",
      "clusterCount": 1,
      "score": 76,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T21:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "香港一般保险市场分析：2025年9亿→2029年09亿 CAGR 5.1%。",
        "tc": "香港一般保險市場分析：2025年9億→2029年09億 CAGR 5.1%。"
      },
      "summary": {
        "sc": "行业精算分析显示香港一般保险市场2025年规模89亿美元，预计2029年增至109亿美元(CAGR 5.1%)。个人意外及健康险占比34.7%为最大板块，财产险22.2%受气候事件推动增长7.5%。网络保险需求上升。[EN原文]",
        "tc": "一般保險市場CAGR5.1% 健康險佔35%"
      },
      "why": {
        "sc": "一般保险的细分市场数据，也是行业结构理解的基础。",
        "tc": "一般保險細分市場數據。"
      },
      "actions": {
        "front": {
          "sc": "了解市场细分结构",
          "tc": "了解市場結構"
        },
        "midback": {
          "sc": "归档一般保险市场数据",
          "tc": "歸檔市場數據"
        },
        "lead": {
          "sc": "一般保险增长机会评估",
          "tc": "一般保險增長機會"
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "EB Actuary",
        "tc": "EB Actuary",
        "lang": "en"
      },
      "boards": [
        "macro"
      ],
      "tags": {
        "sc": [
          "一般保险",
          "市场",
          "预测",
          "CAGR"
        ],
        "tc": [
          "一般保險",
          "市場",
          "預測",
          "CAGR"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-01-10T10:00:00+08:00",
      "originalUrl": "https://www.ebactuary.com/post/hong-kong-general-insurance-market-analysis-2025-2029-and-global-comparison",
      "sourceKey": "ebact:hk-market-2025",
      "sourceTier": "research",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "sztax-gba-202601",
      "clusterCount": 1,
      "score": 75,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "mof-sta",
      "title": {
        "sc": "深圳 2026 年大湾区个税优惠：境外人才超 15% 税率部分可申请财政补贴",
        "tc": "深圳 2026 年大灣區個稅優惠：境外人才超 15% 稅率部分可申請財政補貼"
      },
      "summary": {
        "sc": "2026 年 1 月，深圳发布《粤港澳大湾区个人所得税优惠政策财政补贴申报指南（2026年）》。在深圳工作的境外高端人才和紧缺人才，已缴个税超过应纳税所得额 15% 的部分可申请财政补贴，该补贴免征个税。申报期为 2026 年 1-3 月。",
        "tc": "2026 年 1 月，深圳發布《粵港澳大灣區個人所得稅優惠政策財政補貼申報指南（2026年）》。在深圳工作的境外高端人才和緊缺人才，已繳個稅超過應納稅所得額 15% 的部分可申請財政補貼。"
      },
      "why": {
        "sc": "15% 个税封顶=大湾区对港澳人才的实质性税收优惠。对 IFA：你的客户如果在深圳有业务/工作，这份补贴是重要的税务筹划工具。",
        "tc": "15% 個稅封頂=大灣區對港澳人才的實質性稅收優惠。對 IFA：你的客戶如果在深圳有業務/工作，這份補貼是重要的稅務籌劃工具。"
      },
      "actions": {
        "front": {
          "sc": "15%个税补贴=跨境人才的税务红利",
          "tc": "15%個稅補貼=跨境人才的稅務紅利"
        },
        "midback": {
          "sc": "熟悉大湾区税收优惠=跨境服务的差异化能力",
          "tc": "熟悉大灣區稅收優惠=跨境服務的差異化能力"
        },
        "lead": {},
        "cross": {
          "sc": "香港身份+深圳工作=最优税务组合",
          "tc": "香港身份+深圳工作=最優稅務組合"
        }
      },
      "rolesImpact": {
        "front": 3,
        "midback": 2,
        "lead": 2,
        "cross": 4
      },
      "source": {
        "sc": "深圳市财政局 · 2026年1月",
        "lang": "sc"
      },
      "boards": [
        "family"
      ],
      "themes": [
        "offshore",
        "identity-planning"
      ],
      "tags": {
        "sc": [
          "大湾区",
          "个税",
          "15%",
          "人才"
        ],
        "tc": [
          "大灣區",
          "個稅",
          "15%",
          "人才"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2026-01-06T10:00:00+08:00",
      "originalUrl": "https://szfb.sz.gov.cn/xwzx/tzgg/content/post_12581711.html"
    },
    {
      "id": "manulife-20260105-two-plans",
      "clusterCount": 1,
      "score": 85,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": false,
      "ingestedAt": "2026-07-28T16:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "宏利推出「宏挚家传承」及「财挚宏耀」两款分红寿险储蓄计划。",
        "tc": "宏利推出「宏摯家傳承」及「財摯宏耀」兩款分紅壽險儲蓄計劃。"
      },
      "summary": {
        "sc": "宏利香港2026年1月5日推出两款全新分红寿险储蓄计划——「宏挚家传承」与「财挚宏耀」，帮助客户实现长远财务目标，提供灵活选择应对不同人生阶段需求。",
        "tc": "宏利1月5日推出兩款分紅儲蓄計劃"
      },
      "why": {
        "sc": "宏利2026年首发，也是全年产品策略风向标。",
        "tc": "宏利2026首發，也是產品風向標。"
      },
      "actions": {
        "front": {
          "sc": "两款新品加入产品对比表",
          "tc": "加入產品對比表"
        },
        "midback": {
          "sc": "收集产品费率与条款",
          "tc": "收集產品資料"
        },
        "lead": {
          "sc": "评估宏利产品线的竞争力",
          "tc": "評估產品線競爭力"
        },
        "cross": {
          "sc": "跨境高净值客户适配性分析",
          "tc": "跨境高淨值客戶分析"
        }
      },
      "source": {
        "sc": "宏利新闻稿",
        "tc": "宏利新聞稿",
        "lang": "zh"
      },
      "boards": [
        "product",
        "firm"
      ],
      "tags": {
        "sc": [
          "宏利",
          "分红险",
          "新产品",
          "2026"
        ],
        "tc": [
          "宏利",
          "分紅險",
          "新產品",
          "2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2026-01-05T10:00:00+08:00",
      "originalUrl": "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html",
      "sourceKey": "manulife",
      "sourceTier": "insurer",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "aia-2025-annual-vonb-202603",
      "clusterCount": 1,
      "score": 80,
      "verifyStatus": "verified",
      "sourceTier": "insurer",
      "sourceKey": "aia",
      "title": {
        "sc": "友邦 2025 全年业绩：香港 VONB +28% 创纪录，每股股息 +10%",
        "tc": "友邦 2025 全年業績：香港 VONB +28% 創紀錄，每股股息 +10%"
      },
      "summary": {
        "sc": "友邦集团 2025 全年业绩创新高：新业务价值（VONB）增长 15% 至 55.16 亿美元，香港业务 VONB 大幅增长 28%，每股股息增加 10%。集团总资产增至 3,454 亿美元，同比提升 13%。香港继续是友邦集团最重要的单一市场。",
        "tc": "友邦集團 2025 全年業績創新高：新業務價值（VONB）增長 15% 至 55.16 億美元，香港業務 VONB 大幅增長 28%，每股股息增加 10%。"
      },
      "why": {
        "sc": "友邦香港 VONB +28%=全年增速的核心引擎。作为香港市场头号保司，这个数字说明 2025 全年（含佣金改革前夜抢购）需求端依然强劲——是判断 2026 走势的关键基准线。",
        "tc": "友邦香港 VONB +28%=全年增速的核心引擎。這個數字說明 2025 全年需求端依然強勁。"
      },
      "actions": {
        "front": {
          "sc": "友邦香港+28%=全年需求端的最强佐证",
          "tc": "友邦香港+28%=全年需求端的最強佐證"
        },
        "midback": {},
        "lead": {
          "sc": "股息+10%=股东对香港业务的信心",
          "tc": "股息+10%=股東對香港業務的信心"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 4,
        "midback": 1,
        "lead": 3,
        "cross": 2
      },
      "source": {
        "sc": "友邦集团 · 2026年3月",
        "lang": "zh"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "firm",
        "market"
      ],
      "tags": {
        "sc": [
          "友邦",
          "2025全年",
          "VONB",
          "业绩"
        ],
        "tc": [
          "友邦",
          "2025全年",
          "VONB",
          "業績"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2025-12-31T10:00:00+08:00",
      "originalUrl": "https://zhuanlan.zhihu.com/p/2042158693467383539"
    },
    {
      "id": "zhihu-2025-top10",
      "clusterCount": 1,
      "score": 75,
      "verifyStatus": "pending",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T20:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "知乎盘点2025香港保险十大事件：演示上限/佣金分摊/IUL/跨境打擊。",
        "tc": "知乎盤點2025香港保險十大事件：演示上限/佣金分攤/IUL/跨境打擊。"
      },
      "summary": {
        "sc": "知乎专栏2025年终盘点梳理香港保险十大事件：演示利率上限生效、佣金分摊指引、IUL联合通函、跨境销售专项打击、GN16修订、RBC制度优化咨询、中资保司崛起、大额保单创新高、保司迁册潮、AI促进计划。",
        "tc": "知乎盤點2025香港保險十大事件"
      },
      "why": {
        "sc": "中文社区最全面的年度复盘，也是理解行业全景图的最佳入口。",
        "tc": "中文社區年度復盤，也是行業全景圖。"
      },
      "actions": {
        "front": {
          "sc": "年度事件一图读懂，客户沟通可用",
          "tc": "年度事件一圖讀懂"
        },
        "midback": {
          "sc": "归档年度十大事件",
          "tc": "歸檔年度事件"
        },
        "lead": {
          "sc": "团队年度培训材料",
          "tc": "團隊年度培訓"
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "知乎专栏",
        "tc": "知乎專欄",
        "lang": "zh"
      },
      "boards": [
        "regulatory",
        "product"
      ],
      "tags": {
        "sc": [
          "知乎",
          "盘点",
          "十大事件",
          "2025"
        ],
        "tc": [
          "知乎",
          "盤點",
          "十大事件",
          "2025"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2025-12-30T10:00:00+08:00",
      "originalUrl": "https://zhuanlan.zhihu.com/p/1996682970564694535",
      "sourceKey": "zhihu:top10-2025",
      "sourceTier": "media",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "fwd-hk-2025-nbp-93pct",
      "clusterCount": 1,
      "score": 75,
      "verifyStatus": "verified",
      "sourceTier": "insurer",
      "sourceKey": "fwd",
      "title": {
        "sc": "富卫香港 2025 新业务保费飙升 93%：年化新保费 +74% 远超市场均值",
        "tc": "富衛香港 2025 新業務保費飆升 93%：年化新保費 +74% 遠超市場均值"
      },
      "summary": {
        "sc": "富卫香港 2025 年新业务保费飙升 93%，年化新保费（APE）增长 74%，远超市场平均 43%。富卫的指数型万用寿险（IUL）等高净值产品策略成效显著，线上直销（DTC）渠道亦持续发力。",
        "tc": "富衛香港 2025 年新業務保費飆升 93%，年化新保費（APE）增長 74%，遠超市場平均 43%。富衛的指數型萬用壽險（IUL）等高淨值產品策略成效顯著。"
      },
      "why": {
        "sc": "富卫 93% 增速=非巨头保司抢份额的活样板。它的打法（IUL 高净值 + DTC 线上）正是佣金改革后渠道分化的方向——理解富卫，就能预判中小保司的生存策略。",
        "tc": "富衛 93% 增速=非巨頭保司搶份額的活樣板。它的打法（IUL 高淨值 + DTC 線上）正是佣金改革後渠道分化的方向。"
      },
      "actions": {
        "front": {
          "sc": "富卫93%=高净值+IUL策略的胜利",
          "tc": "富衛93%=高淨值+IUL策略的勝利"
        },
        "midback": {},
        "lead": {
          "sc": "非巨头抢份额=市场分化加速",
          "tc": "非巨頭搶份額=市場分化加速"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 3,
        "midback": 1,
        "lead": 3,
        "cross": 2
      },
      "source": {
        "sc": "富卫集团 · 2025年",
        "lang": "zh"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "firm",
        "market",
        "channel"
      ],
      "tags": {
        "sc": [
          "富卫",
          "业绩",
          "IUL",
          "高净值"
        ],
        "tc": [
          "富衛",
          "業績",
          "IUL",
          "高淨值"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2025-12-20T10:00:00+08:00",
      "originalUrl": "https://insuranceasia.com/company/fwd-group"
    },
    {
      "id": "boclife-2025-record",
      "clusterCount": 1,
      "score": 75,
      "verifyStatus": "verified",
      "sourceTier": "insurer",
      "sourceKey": "boclife",
      "title": {
        "sc": "中银人寿 2025 全年新造标准保费 258 亿港元，按年跃升近 5 成创新高",
        "tc": "中銀人壽 2025 全年新造標準保費 258 億港元，按年躍升近 5 成創新高"
      },
      "summary": {
        "sc": "中银人寿 2025 年业务回顾：全年新造标准保费达 258 亿港元，按年跃升近 5 成，创公司历史新高，表现优于整体市场。持续深耕中银香港渠道，连续多年保持香港网上人寿保险销量市场第一。",
        "tc": "中銀人壽 2025 年業務回顧：全年新造標準保費達 258 億港元，按年躍升近 5 成，創公司歷史新高。連續多年保持香港網上人壽保險銷量市場第一。"
      },
      "why": {
        "sc": "中银人寿是银保渠道+线上直销双模式标杆。258 亿标准保费说明银行系保司正在吃掉可观份额——渠道格局里银保的力量被低估了。",
        "tc": "中銀人壽是銀保渠道+線上直銷雙模式標桿。258 億標準保費說明銀行系保司正在吃掉可觀份額。"
      },
      "actions": {
        "front": {
          "sc": "银保系258亿=银行渠道的真实力量",
          "tc": "銀保系258億=銀行渠道的真實力量"
        },
        "midback": {},
        "lead": {
          "sc": "银行系保司崛起=渠道格局再平衡",
          "tc": "銀行系保司崛起=渠道格局再平衡"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 3,
        "midback": 1,
        "lead": 3,
        "cross": 2
      },
      "source": {
        "sc": "中银人寿 · 2025年",
        "lang": "sc"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "channel",
        "firm"
      ],
      "tags": {
        "sc": [
          "中银人寿",
          "标准保费",
          "银保"
        ],
        "tc": [
          "中銀人壽",
          "標準保費",
          "銀保"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2025-12-15T10:00:00+08:00",
      "originalUrl": "https://www.boclife.com.hk/sc/news/key-summary-of-boc-life2025-business-review-and-outlook.html"
    },
    {
      "id": "jpmorgan-2026-outlook",
      "clusterCount": 1,
      "score": 83,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T19:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "摩根大通2026展望：看好全球权益+双位数增长 黄金目标价$5000。",
        "tc": "摩根大通2026展望：看好全球權益+雙位數增長 黃金目標價$5000。"
      },
      "summary": {
        "sc": "摩根大通2026年展望：看好全球权益市场双位数增长，AI超周期驱动企业盈利。预测美国衰退概率35%，通胀保持粘性。黄金目标价$5000/盎司。美元看空，欧元看多。[EN原文]",
        "tc": "摩根大通：權益看好，黃金$5000，衰退概率35%"
      },
      "why": {
        "sc": "顶级投行的资产配置判断，也是高净值客户的参考框架。",
        "tc": "頂級投行資產配置判斷。"
      },
      "actions": {
        "front": {
          "sc": "高净值客户资产配置讨论中引用",
          "tc": "高淨值客戶引用"
        },
        "midback": {
          "sc": "归档年度投行展望",
          "tc": "歸檔投行展望"
        },
        "lead": {
          "sc": "通胀粘性+AI周期的业务影响",
          "tc": "通脹+AI業務影響"
        },
        "cross": {
          "sc": "黄金/美元=跨境客户的资产关切",
          "tc": "黃金/美元=跨境關切"
        }
      },
      "source": {
        "sc": "JPMorgan Research",
        "tc": "JPMorgan Research",
        "lang": "en"
      },
      "boards": [
        "intl",
        "macro"
      ],
      "tags": {
        "sc": [
          "摩根大通",
          "权益",
          "黄金",
          "展望",
          "2026"
        ],
        "tc": [
          "摩根大通",
          "權益",
          "黃金",
          "展望",
          "2026"
        ]
      },
      "contentKind": "report",
      "publishedAt": "2025-12-10T10:00:00+08:00",
      "originalUrl": "https://www.jpmorgan.com/insights/global-research/outlook/market-outlook",
      "sourceKey": "jpmorgan",
      "sourceTier": "research",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "aif-2025-asian-insurance-forum",
      "clusterCount": 1,
      "score": 83,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "ia",
      "title": {
        "sc": "亚洲保险论坛 2025：迎难而上 拥抱创新",
        "tc": "亞洲保險論壇 2025：迎難而上 擁抱創新"
      },
      "summary": {
        "sc": "2025 年 12 月，保监局在香港举行亚洲保险论坛（AIF2025），主题「迎难而上 拥抱创新」，围绕监管挑战、人口结构转变、AI 等主题讨论。保监局主席姚建华称须以远见灵活应对；金融监管总局副局长肖远企表示将持续巩固香港国际金融中心地位。",
        "tc": "2025 年 12 月，保監局在香港舉行亞洲保險論壇（AIF2025），主題「迎難而上 擁抱創新」，圍繞監管挑戰、人口結構轉變、AI 等主題討論。"
      },
      "why": {
        "sc": "AIF 是亚洲保险监管最高规格会议，主旨发言=官方政策风向。姚建华谈「远见与灵活」、肖远企谈「两地合作」，两句话合并就是 2026 年跨境监管合作的基调。",
        "tc": "AIF 是亞洲保險監管最高規格會議，主旨發言=官方政策風向。姚建華談「遠見與靈活」、肖遠企談「兩地合作」，合併就是 2026 年跨境監管合作的基調。"
      },
      "actions": {
        "front": {},
        "midback": {
          "sc": "论坛议题=监管关注方向的年度清单",
          "tc": "論壇議題=監管關注方向的年度清單"
        },
        "lead": {
          "sc": "监管高层定调=行业方向标",
          "tc": "監管高層定調=行業方向標"
        },
        "cross": {
          "sc": "两地监管同台=跨境合作基调明确",
          "tc": "兩地監管同台=跨境合作基調明確"
        }
      },
      "rolesImpact": {
        "front": 2,
        "midback": 3,
        "lead": 4,
        "cross": 4
      },
      "source": {
        "sc": "保监局 · 2025年12月",
        "lang": "sc"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "reg",
        "macro",
        "career"
      ],
      "tags": {
        "sc": [
          "亚洲保险论坛",
          "AIF",
          "监管"
        ],
        "tc": [
          "亞洲保險論壇",
          "AIF",
          "監管"
        ]
      },
      "contentKind": "event",
      "publishedAt": "2025-12-10T10:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/sc/infocenter/press_releases/aif2025.html"
    },
    {
      "id": "ia-2024-annual-stats",
      "clusterCount": 1,
      "score": 90,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": false,
      "ingestedAt": "2026-07-28T21:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "保监局发布2024年香港保险业年报：毛保费6352亿 全球渗透率第一。",
        "tc": "保監局發布2024年香港保險業年報：毛保費6352億 全球滲透率第一。"
      },
      "summary": {
        "sc": "保监局2025年12月5日发布2024年保险业年报：毛保费总额6352亿港元。保险密度10043美元(全球第2)，保险渗透率18.2%(全球第1)。内地访客新造保费628亿占个人业务28.6%。157家授权保险人，118406名持牌中介。",
        "tc": "2024年報:毛保費6352億,滲透率全球第一"
      },
      "why": {
        "sc": "年度最权威的市场全景数据，也是所有IFA的基础知识储备。",
        "tc": "年度最權威市場全景數據。"
      },
      "actions": {
        "front": {
          "sc": "了解市场规模和结构",
          "tc": "了解市場規模結構"
        },
        "midback": {
          "sc": "归档年度核心数据",
          "tc": "歸檔年度數據"
        },
        "lead": {
          "sc": "年度数据=年度战略基础",
          "tc": "年度數據=戰略基礎"
        },
        "cross": {
          "sc": "渗透率全球第一=对跨境客户最强有力的信任背书",
          "tc": "滲透率全球第一=跨境信任背書"
        }
      },
      "source": {
        "sc": "IA 保监局",
        "tc": "IA 保監局",
        "lang": "zh"
      },
      "boards": [
        "macro"
      ],
      "tags": {
        "sc": [
          "年报",
          "保费",
          "渗透率",
          "2024"
        ],
        "tc": [
          "年報",
          "保費",
          "滲透率",
          "2024"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2025-12-05T10:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/en/infocenter/press_releases/20251205.html",
      "sourceKey": "ia",
      "sourceTier": "official",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "aia-20251121-aisan",
      "clusterCount": 1,
      "score": 78,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T18:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "AIA推出全新「爱伴航」危疾保障系列产品。",
        "tc": "AIA推出全新「愛伴航」危疾保障系列產品。"
      },
      "summary": {
        "sc": "AIA 2025年11月21日推出全新「爱伴航」危疾保障系列，以多项市场首创方案照顾客户不同人生阶段健康需求。",
        "tc": "AIA 11月推出愛伴航危疾系列"
      },
      "why": {
        "sc": "AIA危疾产品线重大更新，也是保障型产品策略加强。",
        "tc": "AIA危疾產品重大更新。"
      },
      "actions": {
        "front": {
          "sc": "了解新产品保障范围",
          "tc": "了解保障範圍"
        },
        "midback": {
          "sc": "更新危疾产品对比",
          "tc": "更新危疾產品對比"
        },
        "lead": {
          "sc": ""
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "AIA 新闻稿",
        "tc": "AIA 新聞稿",
        "lang": "zh"
      },
      "boards": [
        "product",
        "firm"
      ],
      "tags": {
        "sc": [
          "AIA",
          "危疾",
          "爱伴航",
          "2025"
        ],
        "tc": [
          "AIA",
          "危疾",
          "愛伴航",
          "2025"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2025-11-21T10:00:00+08:00",
      "originalUrl": "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/2025/aia-press-release-20251121",
      "sourceKey": "aia",
      "sourceTier": "insurer",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "goldman-2026-macro-outlook",
      "clusterCount": 1,
      "score": 85,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T19:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "高盛2026宏观展望：全球GDP 2.8% 牛市扩散 科技主导。",
        "tc": "高盛2026宏觀展望：全球GDP 2.8% 牛市擴散 科技主導。"
      },
      "summary": {
        "sc": "高盛研究2026年宏观展望：全球GDP增长2.8%(高于共识2.5%)。看好权益市场，预期牛市由科技股扩散至更广泛板块。商品：看好电力需求竞赛与供给浪潮。[EN原文]",
        "tc": "高盛：全球GDP 2.8%，牛市擴散"
      },
      "why": {
        "sc": "高盛的宏观判断，也是全球资产配置的风向标。",
        "tc": "高盛宏觀，也是資產配置風向標。"
      },
      "actions": {
        "front": {
          "sc": "客户资产配置沟通中引用权威宏观判断",
          "tc": "引用宏觀判斷"
        },
        "midback": {
          "sc": "归档年度宏观数据",
          "tc": "歸檔宏觀數據"
        },
        "lead": {
          "sc": "宏观环境对保险需求的影响分析",
          "tc": "宏觀對保險需求影響"
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "Goldman Sachs Research",
        "tc": "Goldman Sachs Research",
        "lang": "en"
      },
      "boards": [
        "intl",
        "macro"
      ],
      "tags": {
        "sc": [
          "高盛",
          "宏观",
          "GDP",
          "2026"
        ],
        "tc": [
          "高盛",
          "宏觀",
          "GDP",
          "2026"
        ]
      },
      "contentKind": "report",
      "publishedAt": "2025-11-20T10:00:00+08:00",
      "originalUrl": "https://www.goldmansachs.com/insights/outlooks/2026-outlooks",
      "sourceKey": "goldmansachs",
      "sourceTier": "research",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20251120-refcheck-scheme",
      "title": {
        "sc": "保险中介人背景查核计划通函（2025-11-20）。",
        "tc": "保險中介人背景查核計劃通函（2025-11-20）。"
      },
      "summary": {
        "sc": "保监局2025年11月20日通函发布保险中介人背景查核计划材料，扩展与规范主事人在聘用/委任前的操守信息查询机制，为后续跨行业安排奠基。",
        "tc": "保監局2025年11月20日通函發布保險中介人背景查核計劃材料，擴展與規範主事人在聘用/委任前的操守信息查詢機制，為後續跨行業安排奠基。"
      },
      "why": {
        "sc": "防「滚动烂苹果」；机构聘用必须可追溯。",
        "tc": "防「滾動爛蘋果」；機構聘用必須可追溯。"
      },
      "actions": {
        "front": {
          "sc": "保持职业记录干净，离职配合查核。",
          "tc": "保持職業記錄乾淨，離職配合查核。"
        },
        "midback": {
          "sc": "招募流程写入查核步骤。｜主事人系统权限与回函时限管理。",
          "tc": "招募流程寫入查核步驟。｜主事人系統權限與回函時限管理。"
        },
        "lead": {
          "sc": "把查核时效计入 onboarding SLA。",
          "tc": "把查核時效計入 onboarding SLA。"
        },
        "cross": {
          "sc": "无直接动作。",
          "tc": "無直接動作。"
        }
      },
      "source": {
        "sc": "保监局规管通函 2025-11-20",
        "tc": "保監局規管通函 2025-11-20"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "背景查核",
          "中介"
        ],
        "tc": [
          "背景查核",
          "中介"
        ]
      },
      "themes": [
        "compliance",
        "career",
        "reg"
      ],
      "rolesImpact": {
        "front": 2,
        "midback": 3,
        "lead": 3,
        "cross": 0
      },
      "publishedAt": "2025-11-20T09:00:00+08:00",
      "score": 87,
      "verifyStatus": "verified",
      "featured": false,
      "originalUrl": "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/files/Cir_dd_20.11.2025_Reference_Checking_Schemes_for_Licensed_Insurance_Intermediaries_Eng.pdf",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "sfc-2025-wmc-insurance",
      "clusterCount": 1,
      "score": 83,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T22:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "证监会探讨保险产品纳入跨境理财通南向通。",
        "tc": "證監會探討保險產品納入跨境理財通南向通。"
      },
      "summary": {
        "sc": "证监会2025年11月公布跨境理财通升级方案，首次探讨将保险产品纳入南向通合资格投资范围。此举如落地将开辟内地客户合法购买香港保险的新通道。目前尚处研究阶段。[EN原文]",
        "tc": "證監會探討保險產品納入跨境理財通南向通"
      },
      "why": {
        "sc": "跨境理财通，也是内地客户合法投保的最大政策变量。",
        "tc": "跨境理財通，也是最大政策變量。"
      },
      "actions": {
        "front": {
          "sc": "关注政策进展，提前准备",
          "tc": "關注政策進展"
        },
        "midback": {
          "sc": "跟踪SFC政策更新",
          "tc": "跟蹤SFC政策"
        },
        "lead": {
          "sc": "跨境理财通=渠道战略级机会",
          "tc": "渠道戰略級機會"
        },
        "cross": {
          "sc": "一旦落地=跨境业务模式重构",
          "tc": "跨境業務模式重構"
        }
      },
      "source": {
        "sc": "SFC 证监会",
        "tc": "SFC 證監會",
        "lang": "zh"
      },
      "boards": [
        "regulatory",
        "cross"
      ],
      "tags": {
        "sc": [
          "证监会",
          "跨境理财通",
          "保险",
          "南向通"
        ],
        "tc": [
          "證監會",
          "跨境理財通",
          "保險",
          "南向通"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2025-11-13T10:00:00+08:00",
      "originalUrl": "https://www.sfc.hk/en/Regulatory-functions/Intermediaries/Supervision/Cross-boundary-WMC",
      "sourceKey": "sfc:wmc-202511",
      "sourceTier": "media",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20251024-1h2025-stats",
      "title": {
        "sc": "2025上半年临时统计：长期新造约1737亿港元，同比约+50%。",
        "tc": "2025上半年臨時統計：長期新造約1737億港元，同比約+50%。"
      },
      "summary": {
        "sc": "保监局2025年10月24日公布2025上半年临时统计：毛保费总额约4234亿港元；长期业务（不含退休计划）新造保单保费约1737亿，同比上升约50%；分红业务约1499亿。",
        "tc": "保監局2025年10月24日公布2025上半年臨時統計：毛保費總額約4234億港元；長期業務（不含退休計劃）新造保單保費約1737億，同比上升約50%；分紅業務約1499億。"
      },
      "why": {
        "sc": "官方确认高速增长期的半年切片，便于对照全年与Q1。",
        "tc": "官方確認高速增長期的半年切片，便於對照全年與Q1。"
      },
      "actions": {
        "front": {
          "sc": "用官方半年数据替代口头传闻。",
          "tc": "用官方半年數據替代口頭傳聞。"
        },
        "midback": {
          "sc": "更新市场简报时间序列。｜大额增长下的AML资源评估。",
          "tc": "更新市場簡報時間序列。｜大額增長下的AML資源評估。"
        },
        "lead": {
          "sc": "半年度复盘产能与合规并重。",
          "tc": "半年度複盤產能與合規並重。"
        },
        "cross": {
          "sc": "增长结构中的访客/本地拆分若披露则跟进。",
          "tc": "增長結構中的訪客/本地拆分若披露則跟進。"
        }
      },
      "source": {
        "sc": "保监局新闻稿 2025-10-24",
        "tc": "保監局新聞稿 2025-10-24"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "临时统计",
          "2025H1"
        ],
        "tc": [
          "臨時統計",
          "2025H1"
        ]
      },
      "themes": [
        "channel",
        "macro",
        "firm"
      ],
      "rolesImpact": {
        "front": 2,
        "midback": 2,
        "lead": 3,
        "cross": 2
      },
      "publishedAt": "2025-10-24T12:00:00+08:00",
      "score": 90,
      "verifyStatus": "verified",
      "featured": true,
      "originalUrl": "https://www.ia.org.hk/tc/infocenter/press_releases/20251024.html",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "insurer",
        "market"
      ],
      "contentKind": "press"
    },
    {
      "id": "ia-20251024-h1stats",
      "clusterCount": 1,
      "score": 84,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T14:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "保监局公布2025年上半年临时统计：毛保费4234亿，新造保费1737亿。",
        "tc": "保監局公布2025年上半年臨時統計：毛保費4234億，新造保費1737億。"
      },
      "summary": {
        "sc": "保监局2025年10月24日公布2025年上半年临时统计：毛保费总额4234亿港元，长期业务新造保费1737亿港元。分红业务持续领跑，内地访客贡献显著增长。",
        "tc": "保監局公布H1統計，毛保費4234億"
      },
      "why": {
        "sc": "上半年数据反映演示利率上限前抢购潮的峰值。",
        "tc": "反映演示利率上限前搶購潮峰值。"
      },
      "actions": {
        "front": {
          "sc": "用官方数据展示香港保险市场增长动能",
          "tc": "展示市場增長動能"
        },
        "midback": {
          "sc": "更新行业数据库",
          "tc": "更新行業數據庫"
        },
        "lead": {
          "sc": "数据驱动业务策略",
          "tc": "數據驅動業務策略"
        },
        "cross": {
          "sc": "内地访客数据辅助跨境营销定位",
          "tc": "內地訪客數據輔助營銷"
        }
      },
      "source": {
        "sc": "IA 保监局统计",
        "tc": "IA 保監局統計",
        "lang": "zh"
      },
      "boards": [
        "regulatory",
        "macro"
      ],
      "tags": {
        "sc": [
          "H1统计",
          "保费",
          "4234亿",
          "2025"
        ],
        "tc": [
          "H1統計",
          "保費",
          "4234億",
          "2025"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2025-10-24T10:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/en/infocenter/statistics/",
      "sourceKey": "ia",
      "sourceTier": "official",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-2025-annual-report",
      "clusterCount": 1,
      "score": 82,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "ia",
      "title": {
        "sc": "保监局发表 2024-25 年报：CPD 合规率 99.9%、执法罚款 2,367 万港元",
        "tc": "保監局發表 2024-25 年報：CPD 合規率 99.9%、執法罰款 2,367 萬港元"
      },
      "summary": {
        "sc": "2025 年 10 月 22 日，保监局发表《2024-25 年报》：① 持牌中介 CPD 合规率达 99.9%；② 年度执法罚款约 2,367 万港元；③ 收到 1,066 宗新投诉；④ 持牌代理机构 1,556 间；⑤ CPD 培训先导计划吸引约 500 名从业员报读。",
        "tc": "2025 年 10 月 22 日，保監局發表《2024-25 年報》：① 持牌中介 CPD 合規率達 99.9%；② 年度執法罰款約 2,367 萬港元；③ 收到 1,066 宗新投訴；④ 持牌代理機構 1,556 間；⑤ CPD 培訓先導計劃吸引約 500 名從業員報讀。"
      },
      "why": {
        "sc": "99.9% CPD 合规率=中介人队伍变得更专业了。2,367 万罚款=监管牙齿更锋利了。年报是理解监管工具箱扩容的最佳文档。",
        "tc": "99.9% CPD 合規率=中介人隊伍變得更專業了。2,367 萬罰款=監管牙齒更鋒利了。年報是理解監管工具箱擴容的最佳文檔。"
      },
      "actions": {
        "front": {
          "sc": "CPD合规=专业中介=客户信任基础更强",
          "tc": "CPD合規=專業中介=客戶信任基礎更強"
        },
        "midback": {
          "sc": "罚款上升=合规团队不是成本中心",
          "tc": "罰款上升=合規團隊不是成本中心"
        },
        "lead": {
          "sc": "年报数据=培训团队/合规资源投入的决策依据",
          "tc": "年報數據=培訓團隊/合規資源投入的決策依據"
        },
        "cross": {
          "sc": ""
        }
      },
      "rolesImpact": {
        "front": 2,
        "midback": 4,
        "lead": 3,
        "cross": 1
      },
      "source": {
        "sc": "IA · 2025年10月22日",
        "lang": "zh"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "reg",
        "compliance",
        "career"
      ],
      "tags": {
        "sc": [
          "年报",
          "CPD",
          "执法",
          "罚款"
        ],
        "tc": [
          "年報",
          "CPD",
          "執法",
          "罰款"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2025-10-22T10:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/sc/infocenter/press_releases/20251022.html"
    },
    {
      "id": "ia-dsii-20251017",
      "clusterCount": 1,
      "score": 95,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "ia",
      "title": {
        "sc": "保监局公布首批 D-SII 名单：友邦、保诚入选「大而不能倒」",
        "tc": "保監局公佈首批 D-SII 名單：友邦、保誠入選「大而不能倒」"
      },
      "summary": {
        "sc": "2025 年 10 月 17 日，保监局正式推出「具本地系统重要性保险公司（D-SII）」宏观审慎监管框架，首批仅友邦和保诚两家从 160 余家获授权保险人中入选。D-SII 需承担更高资本要求和更严格风险管理——这标志着港险监管向「分层监管」迈出关键一步。",
        "tc": "2025 年 10 月 17 日，保監局正式推出「具本地系統重要性保險公司（D-SII）」宏觀審慎監管框架，首批僅友邦和保誠兩家從 160 餘家獲授權保險人中入選。D-SII 需承擔更高資本要求和更嚴格風險管理——這標誌著港險監管向「分層監管」邁出關鍵一步。"
      },
      "why": {
        "sc": "D-SII=香港版「大而不能倒」名单。入选=监管最严级别，也=市场对这两家「不会倒」的官方背书。这对 IFA 推荐产品时的保司选择有直接参考价值。",
        "tc": "D-SII=香港版「大而不能倒」名單。入選=監管最嚴級別，也=市場對這兩家「不會倒」的官方背書。這對 IFA 推薦產品時的保司選擇有直接參考價值。"
      },
      "actions": {
        "front": {
          "sc": "D-SII保司=客户最关心的「安全性」问题有官方答案",
          "tc": "D-SII保司=客戶最關心的「安全性」問題有官方答案"
        },
        "midback": {
          "sc": "D-SII框架=更高资本要求=保司合规义务升级",
          "tc": "D-SII框架=更高資本要求=保司合規義務升級"
        },
        "lead": {
          "sc": "仅友邦/保诚入选=竞争格局的两极化信号",
          "tc": "僅友邦/保誠入選=競爭格局的兩極化信號"
        },
        "cross": {
          "sc": "D-SII与G-SII(全球系统重要性)形成两级监管体系",
          "tc": "D-SII與G-SII(全球系統重要性)形成兩級監管體系"
        }
      },
      "rolesImpact": {
        "front": 5,
        "midback": 4,
        "lead": 5,
        "cross": 4
      },
      "source": {
        "sc": "IA / AIA / Prudential · 2025年10月17日",
        "lang": "zh"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "reg",
        "firm"
      ],
      "tags": {
        "sc": [
          "D-SII",
          "友邦",
          "保诚",
          "系统性重要"
        ],
        "tc": [
          "D-SII",
          "友邦",
          "保誠",
          "系統性重要"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2025-10-17T10:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/en/infocenter/press_releases/20251017.html"
    },
    {
      "id": "ia-ro-cpd-20251014",
      "title": {
        "sc": "负责人（RO）强制 CPD：2025/26 评估期首轮安排（2025-10-14 通函）。",
        "tc": "負責人（RO）強制 CPD：2025/26 評估期首輪安排（2025-10-14 通函）。"
      },
      "summary": {
        "sc": "保监局2025年10月14日通函就2025/26评估期强制性 RO-CPD 培训细节作出说明，要求负责人按期完成指定培训。",
        "tc": "保監局2025年10月14日通函就2025/26評估期強制性 RO-CPD 培訓細節作出說明，要求負責人按期完成指定培訓。"
      },
      "why": {
        "sc": "RO 合规能力直接决定公司牌照与出单审批质量。",
        "tc": "RO 合規能力直接決定公司牌照與出單審批質量。"
      },
      "actions": {
        "front": {
          "sc": "知晓公司 RO 要求，签约卡点配合补件。",
          "tc": "知曉公司 RO 要求，簽約卡點配合補件。"
        },
        "midback": {
          "sc": "把 RO-CPD 节点写入培训日历。｜追踪 RO 完成率与证明存档。",
          "tc": "把 RO-CPD 節點寫入培訓日曆。｜追蹤 RO 完成率與證明存檔。"
        },
        "lead": {
          "sc": "确保后备 RO 与职责分工清晰。",
          "tc": "確保後備 RO 與職責分工清晰。"
        },
        "cross": {
          "sc": "无直接动作。",
          "tc": "無直接動作。"
        }
      },
      "source": {
        "sc": "保监局规管通函 2025-10-14",
        "tc": "保監局規管通函 2025-10-14"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "RO",
          "CPD"
        ],
        "tc": [
          "RO",
          "CPD"
        ]
      },
      "themes": [
        "compliance",
        "career",
        "reg"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 3,
        "lead": 2,
        "cross": 0
      },
      "publishedAt": "2025-10-14T09:00:00+08:00",
      "score": 84,
      "verifyStatus": "verified",
      "originalUrl": "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2025.html",
      "featured": false,
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "ia-202508-iul-sandbox",
      "clusterCount": 1,
      "score": 80,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T13:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "保监局批准IUL产品沙盒申请：视频会议销售纳入监管框架。",
        "tc": "保監局批准IUL產品沙盒申請：視頻會議銷售納入監管框架。"
      },
      "summary": {
        "sc": "保监局2025年9月发出通函，批准IUL产品通过视频会议销售的沙盒申请，明确远程销售长期保单的合规要求与保障措施。自2025年3月IUL联合通函以来，已有43个IUL产品进入市场。",
        "tc": "保監局批准IUL視頻銷售沙盒，43個IUL產品已入市"
      },
      "why": {
        "sc": "IUL产品渠道进一步拓展，视频销售，也是新的客户触达方式。",
        "tc": "IUL視頻銷售，也是新客戶觸達方式。"
      },
      "actions": {
        "front": {
          "sc": "了解IUL视频销售流程和合规要求",
          "tc": "了解IUL視頻銷售流程"
        },
        "midback": {
          "sc": "更新远程销售合规清单",
          "tc": "更新遠程銷售合規清單"
        },
        "lead": {
          "sc": "评估IUL产品在团队产品矩阵中的定位",
          "tc": "評估IUL產品定位"
        },
        "cross": {
          "sc": "视频销售是否适用于跨境客户？严格合规评估",
          "tc": "視頻銷售是否適用跨境客戶"
        }
      },
      "source": {
        "sc": "IA 保监局通函",
        "tc": "IA 保監局通函",
        "lang": "en"
      },
      "boards": [
        "regulatory",
        "product"
      ],
      "tags": {
        "sc": [
          "IUL",
          "沙盒",
          "视频销售",
          "远程"
        ],
        "tc": [
          "IUL",
          "沙盒",
          "視頻銷售",
          "遠程"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2025-09-19T14:00:00+08:00",
      "originalUrl": "https://brdr.hkma.gov.hk/chi/doc-ldg/docId/20250313-10-TC",
      "sourceKey": "hkma",
      "sourceTier": "official",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20250919-product-naming",
      "title": {
        "sc": "保险产品命名要求联合通函（2025-09-19）。",
        "tc": "保險產品命名要求聯合通函（2025-09-19）。"
      },
      "summary": {
        "sc": "保监局2025年9月19日发出保险产品命名要求联合通函，规范产品名称不得误导客户对保障范围、回报性质或风险的理解。",
        "tc": "保監局2025年9月19日發出保險產品命名要求聯合通函，規範產品名稱不得誤導客戶對保障範圍、回報性質或風險的理解。"
      },
      "why": {
        "sc": "影响产品包装、海报与对客话术用词。",
        "tc": "影響產品包裝、海報與對客話術用詞。"
      },
      "actions": {
        "front": {
          "sc": "勿自行给产品起「稳赚/保本」别名。",
          "tc": "勿自行給產品起「穩賺/保本」別名。"
        },
        "midback": {
          "sc": "检查培训与物料中的产品称呼。｜社媒与广告用词合规扫描。",
          "tc": "檢查培訓與物料中的產品稱呼。｜社媒與廣告用詞合規掃描。"
        },
        "lead": {
          "sc": "品牌物料统一命名词典。",
          "tc": "品牌物料統一命名詞典。"
        },
        "cross": {
          "sc": "多语言翻译避免夸大。",
          "tc": "多語言翻譯避免誇大。"
        }
      },
      "source": {
        "sc": "保监局联合通函 2025-09-19",
        "tc": "保監局聯合通函 2025-09-19"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "产品命名",
          "误导"
        ],
        "tc": [
          "產品命名",
          "誤導"
        ]
      },
      "themes": [
        "reg",
        "product",
        "compliance"
      ],
      "rolesImpact": {
        "front": 2,
        "midback": 3,
        "lead": 2,
        "cross": 1
      },
      "publishedAt": "2025-09-19T09:00:00+08:00",
      "score": 83,
      "verifyStatus": "verified",
      "featured": false,
      "originalUrl": "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/files/Circular_19092025.pdf",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "product",
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "ia-20250917-product-naming",
      "clusterCount": 1,
      "score": 82,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": true,
      "ingestedAt": "2026-07-28T13:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "保监局与金管局联合发布保险产品命名要求通函。",
        "tc": "保監局與金管局聯合發布保險產品命名要求通函。"
      },
      "summary": {
        "sc": "保监局与金管局2025年9月联合发出通函，就保险产品名称的适当性提出监管要求。分两阶段实施：第一阶段自2026年1月1日起适用于新上市产品，避免产品名称误导消费者。",
        "tc": "保監局與金管局9月聯合發布產品命名通函"
      },
      "why": {
        "sc": "产品命名规范化，也是消费者保护升级，误导性名称将被禁止。",
        "tc": "產品命名規範化，也是消費者保護。"
      },
      "actions": {
        "front": {
          "sc": "向客户解释产品名称的含义，不夸大宣传",
          "tc": "向客戶解釋產品名稱含義"
        },
        "midback": {
          "sc": "更新产品宣传材料中的产品名称",
          "tc": "更新產品宣傳材料"
        },
        "lead": {
          "sc": "团队培训：产品命名合规要求",
          "tc": "團隊培訓產品命名合規"
        },
        "cross": {
          "sc": "跨境客户可能遇到两岸产品名称差异",
          "tc": "跨境產品名稱差異說明"
        }
      },
      "source": {
        "sc": "IA+HKMA 联合通函",
        "tc": "IA+HKMA 聯合通函",
        "lang": "en"
      },
      "boards": [
        "regulatory",
        "product"
      ],
      "tags": {
        "sc": [
          "产品命名",
          "金管局",
          "通函",
          "2026"
        ],
        "tc": [
          "產品命名",
          "金管局",
          "通函",
          "2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2025-09-17T14:00:00+08:00",
      "originalUrl": "https://brdr.hkma.gov.hk/eng/doc-ldg/docId/getPdf/20250917-4-EN/20250917-4-EN.pdf",
      "sourceKey": "hkma",
      "sourceTier": "official",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-2025-hkfi-monthly-brief",
      "clusterCount": 1,
      "score": 70,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "hkfi",
      "title": {
        "sc": "香港保联 2025 年 9 月产品简报：多款新产品聚焦健康与退休",
        "tc": "香港保聯 2025 年 9 月產品簡報：多款新產品聚焦健康與退休"
      },
      "summary": {
        "sc": "香港保险业联会（HKFI）2025 年 9 月产品月报显示：AIA 推出「OptimaCEO 医疗计划」、Sun Life 推出「Stand-by-you 意外保障计划」、多款产品聚焦健康保障与退休规划。",
        "tc": "香港保險業聯會（HKFI）2025 年 9 月產品月報顯示：AIA 推出「OptimaCEO 醫療計劃」、Sun Life 推出「Stand-by-you 意外保障計劃」、多款產品聚焦健康保障與退休規劃。"
      },
      "why": {
        "sc": "保联月报是追踪全行业产品发布的窗口——不是每家保司都发新闻稿，但产品上了保联月报就是正式推向市场。",
        "tc": "保聯月報是追蹤全行業產品發佈的窗口——不是每家保司都發新聞稿，但產品上了保聯月報就是正式推向市場。"
      },
      "actions": {
        "front": {
          "sc": "新产品=新话术=新客户切入角度",
          "tc": "新產品=新話術=新客戶切入角度"
        },
        "midback": {},
        "lead": {
          "sc": "产品发布节奏=保司战略意图的信号",
          "tc": "產品發佈節奏=保司戰略意圖的信號"
        },
        "cross": {
          "sc": ""
        }
      },
      "rolesImpact": {
        "front": 3,
        "midback": 1,
        "lead": 2,
        "cross": 1
      },
      "source": {
        "sc": "HKFI · 2025年9月",
        "lang": "zh"
      },
      "boards": [
        "product"
      ],
      "themes": [
        "product"
      ],
      "tags": {
        "sc": [
          "产品",
          "AIA",
          "Sun Life",
          "医疗"
        ],
        "tc": [
          "產品",
          "AIA",
          "Sun Life",
          "醫療"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2025-09-15T10:00:00+08:00",
      "originalUrl": "https://files.hkfi.org.hk/monthly%20brief/2025/e_202509.pdf"
    },
    {
      "id": "ctflife-artisan-heritage2-2025",
      "clusterCount": 1,
      "score": 74,
      "verifyStatus": "verified",
      "sourceTier": "insurer",
      "sourceKey": "ctflife",
      "title": {
        "sc": "周大福人寿推出「匠心·传承」储蓄寿险计划2 瞄准传承需求",
        "tc": "周大福人壽推出「匠心·傳承」儲蓄壽險計劃2 瞄準傳承需求"
      },
      "summary": {
        "sc": "周大福人寿（CTF Life）推出「匠心·传承」储蓄寿险计划 2，聚焦财富传承需求，依托周大福集团生态圈资源提供储蓄+传承一体化方案。公司扎根香港 40 年，连续多年获惠誉/穆迪高评级。",
        "tc": "周大福人壽（CTF Life）推出「匠心·傳承」儲蓄壽險計劃 2，聚焦財富傳承需求，依託周大福集團生態圈資源提供儲蓄+傳承一體化方案。"
      },
      "why": {
        "sc": "周大福人寿正在从「更名后的新人」变成「传承赛道的主力」。匠心传承 2 是其品牌升级后的旗舰储蓄产品，代表中资生态圈玩家的产品打法。",
        "tc": "周大福人壽正在從「更名後的新人」變成「傳承賽道的主力」。匠心傳承 2 是其品牌升級後的旗艦儲蓄產品。"
      },
      "actions": {
        "front": {
          "sc": "匠心传承2=中资系传承产品的代表",
          "tc": "匠心傳承2=中資系傳承產品的代表"
        },
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 3,
        "midback": 1,
        "lead": 2,
        "cross": 2
      },
      "source": {
        "sc": "周大福人寿 · 2025年",
        "lang": "sc"
      },
      "boards": [
        "product"
      ],
      "themes": [
        "product",
        "firm"
      ],
      "tags": {
        "sc": [
          "周大福人寿",
          "匠心传承",
          "储蓄"
        ],
        "tc": [
          "周大福人壽",
          "匠心傳承",
          "儲蓄"
        ]
      },
      "contentKind": "product_notice",
      "publishedAt": "2025-09-10T10:00:00+08:00",
      "originalUrl": "https://www.ctflife.com.hk/sc"
    },
    {
      "id": "manulife-20250902-hospitals",
      "clusterCount": 1,
      "score": 76,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T18:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "宏利医疗网络扩展至内地38000+间医院。",
        "tc": "宏利醫療網絡擴展至內地38000+間醫院。"
      },
      "summary": {
        "sc": "宏利香港2025年9月2日将内地医院覆盖扩大至超过38000间公立及私立医院，客户可根据个人需要在内地任何医院接受医疗服务。",
        "tc": "宏利9月2日擴展內地醫療網絡至38000+間"
      },
      "why": {
        "sc": "医疗网络覆盖，也是跨境客户选择宏利的重要考量。",
        "tc": "醫療網絡，也是跨境客戶考量。"
      },
      "actions": {
        "front": {
          "sc": "内地有就医需求的客户优选项",
          "tc": "內地就醫客戶優選"
        },
        "midback": {
          "sc": "更新保司医疗网络对比",
          "tc": "更新醫療網絡對比"
        },
        "lead": {
          "sc": ""
        },
        "cross": {
          "sc": "跨境客户医疗覆盖优势突出",
          "tc": "跨境醫療覆蓋優勢"
        }
      },
      "source": {
        "sc": "宏利新闻稿",
        "tc": "宏利新聞稿",
        "lang": "zh"
      },
      "boards": [
        "product",
        "firm"
      ],
      "tags": {
        "sc": [
          "宏利",
          "医疗网络",
          "内地",
          "2025"
        ],
        "tc": [
          "宏利",
          "醫療網絡",
          "內地",
          "2025"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2025-09-02T10:00:00+08:00",
      "originalUrl": "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html",
      "sourceKey": "manulife",
      "sourceTier": "insurer",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20250901-referral50",
      "clusterCount": 1,
      "score": 95,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": true,
      "ingestedAt": "2026-07-28T13:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "保监局就转介费监管期望发出通函：50%基准 10月1日起遵从。",
        "tc": "保監局就轉介費監管期望發出通函：50%基準 10月1日起遵從。"
      },
      "summary": {
        "sc": "保监局2025年9月1日发出通函，就持牌经纪公司支付分红保单转介费提出监管期望：转介费以佣金总额50%为基准。超基准须加强披露，并可能面对巡查与续牌审视。市场预期自2025年10月1日起遵从。",
        "tc": "保監局9月1日發出轉介費通函，50%基準10月1日起遵從"
      },
      "why": {
        "sc": "转介费规则，也是分红保单销售的合规红线，超线后果严重。",
        "tc": "轉介費規則，也是分紅保單合規紅線。"
      },
      "actions": {
        "front": {
          "sc": "计算每笔分红保单转介费是否在50%以内",
          "tc": "計算轉介費是否在50%以內"
        },
        "midback": {
          "sc": "建立转介费台账，每季度自查",
          "tc": "建立轉介費台賬定期自查"
        },
        "lead": {
          "sc": "团队培训：转介费合规红线不可触碰",
          "tc": "團隊培訓轉介費紅線"
        },
        "cross": {
          "sc": "跨境转介协议需符合两地监管要求",
          "tc": "跨境轉介需符合兩地監管"
        }
      },
      "source": {
        "sc": "IA 保监局通函",
        "tc": "IA 保監局通函",
        "lang": "zh"
      },
      "boards": [
        "regulatory",
        "compliance",
        "channel"
      ],
      "tags": {
        "sc": [
          "转介费",
          "50%",
          "通函",
          "合规"
        ],
        "tc": [
          "轉介費",
          "50%",
          "通函",
          "合規"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2025-09-01T09:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/files/Cir_dd_01092025_Referral_Fees_Eng.pdf",
      "sourceKey": "ia",
      "sourceTier": "official",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20250901-referral-fee",
      "title": {
        "sc": "分红保单转介费监管期望：50%基准（2025-09-01，10-01起遵从）。",
        "tc": "分紅保單轉介費監管期望：50%基準（2025-09-01，10-01起遵從）。"
      },
      "summary": {
        "sc": "保监局2025年9月1日通函就持牌经纪公司就分红保单支付转介费提出监管期望：转介费以佣金总额50%为基准；超基准须加强披露并可能面对巡查与续牌审视。市场预期自2025年10月1日起遵从。",
        "tc": "保監局2025年9月1日通函就持牌經紀公司就分紅保單支付轉介費提出監管期望：轉介費以佣金總額50%為基準；超基準須加強披露並可能面對巡查與續牌審視。市場預期自2025年10月1日起遵從。"
      },
      "why": {
        "sc": "转介模式必须阳光化；超标分账是高风险区。",
        "tc": "轉介模式必須陽光化；超標分賬是高風險區。"
      },
      "actions": {
        "front": {
          "sc": "只走公司书面转介协议；不给未持牌方做销售建议。",
          "tc": "只走公司書面轉介協議；不給未持牌方做銷售建議。"
        },
        "midback": {
          "sc": "签约检查转介披露文件。｜转介费与佣金入账勾稽；超基准预警。",
          "tc": "簽約檢查轉介披露文件。｜轉介費與佣金入賬勾稽；超基準預警。"
        },
        "lead": {
          "sc": "渠道政策重签，淘汰不愿阳光化伙伴。",
          "tc": "渠道政策重簽，淘汰不願陽光化夥伴。"
        },
        "cross": {
          "sc": "跨境转介默认高风险预审。",
          "tc": "跨境轉介默認高風險預審。"
        }
      },
      "source": {
        "sc": "保监局规管通函 2025-09-01",
        "tc": "保監局規管通函 2025-09-01"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "转介费",
          "50%",
          "分红"
        ],
        "tc": [
          "轉介費",
          "50%",
          "分紅"
        ]
      },
      "themes": [
        "reg",
        "compliance",
        "channel"
      ],
      "rolesImpact": {
        "front": 3,
        "midback": 3,
        "lead": 3,
        "cross": 3
      },
      "publishedAt": "2025-09-01T09:00:00+08:00",
      "effectiveAt": "2025-10-01",
      "score": 96,
      "verifyStatus": "verified",
      "featured": true,
      "originalUrl": "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/files/Cir_dd_01092025_Regulatory_Expectations_on_Referral_Fees_Eng.pdf",
      "clusterCount": 4,
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": true,
      "boards": [
        "market",
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "ia-2024-25-annual-report",
      "clusterCount": 1,
      "score": 83,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T21:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "保监局2024-25年报：监管157家保司+11.8万中介 罚款2300万。",
        "tc": "保監局2024-25年報：監管157家保司+11.8萬中介 罰款2300萬。"
      },
      "summary": {
        "sc": "保监局2024-25年报(截至2025年3月)：监管157间获授权保险公司和118406名持牌中介。处理约23400宗新牌照申请。2024年9月起征收牌照费。与廉政公署首次联合打击跨境无牌销售。50项纪律行动罚款2368万港元。",
        "tc": "年報:157家保司+11.8萬中介+50項紀律行動"
      },
      "why": {
        "sc": "监管年报，也是行业合规现状的最权威综述。",
        "tc": "監管年報，也是合規現狀最權威綜述。"
      },
      "actions": {
        "front": {
          "sc": "了解监管执法重点和趋势",
          "tc": "了解監管重點"
        },
        "midback": {
          "sc": "归档年报核心数据",
          "tc": "歸檔年報數據"
        },
        "lead": {
          "sc": "罚款金额和频次=合规风险地图",
          "tc": "罰款=合規風險地圖"
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "IA 保监局年报",
        "tc": "IA 保監局年報",
        "lang": "zh"
      },
      "boards": [
        "regulatory",
        "compliance"
      ],
      "tags": {
        "sc": [
          "年报",
          "持牌",
          "罚款",
          "2024-25"
        ],
        "tc": [
          "年報",
          "持牌",
          "罰款",
          "2024-25"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2025-08-22T10:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/tc/infocenter/files/IA_AR24-25_Synopsis_TC.pdf",
      "sourceKey": "ia",
      "sourceTier": "official",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "cpic-incremental-whole-life-2025",
      "clusterCount": 1,
      "score": 76,
      "verifyStatus": "verified",
      "sourceTier": "insurer",
      "sourceKey": "cpic",
      "title": {
        "sc": "太保寿险香港推出「世代鑫享」增额终身寿险：内地热卖产品引入香港",
        "tc": "太保壽險香港推出「世代鑫享」增額終身壽險：內地熱賣產品引入香港"
      },
      "summary": {
        "sc": "中国太保寿险香港在香港市场推出首只增额终身寿险产品「世代鑫享增额终身寿险计划」，将内地热卖的增额寿险引入香港，让注重长期稳健增值的客户多一个选择。太保香港新单保费从 2022 年 2,800 万港元飙升至 2024 年 11.5 亿港元，两年增长近 40 倍。",
        "tc": "中國太保壽險香港在香港市場推出首隻增額終身壽險產品「世代鑫享增額終身壽險計劃」，將內地熱賣的增額壽險引入香港。太保香港新單保費從 2022 年 2,800 萬港元飆升至 2024 年 11.5 億港元。"
      },
      "why": {
        "sc": "「内地产品反向输出到香港」——增额终身寿是内地 2023-2024 最热的产品形态，太保把它搬到香港。对 IFA：这是理解「内地客户要什么」的活教材，也是产品创新的新方向。",
        "tc": "「內地產品反向輸出到香港」——增額終身壽是內地 2023-2024 最熱的產品形態，太保把它搬到香港。這是理解「內地客戶要什麼」的活教材。"
      },
      "actions": {
        "front": {
          "sc": "增额终身寿入港=内地产品形态的香港化",
          "tc": "增額終身壽入港=內地產品形態的香港化"
        },
        "midback": {},
        "lead": {
          "sc": "太保40倍增长=中资保司的起飞曲线",
          "tc": "太保40倍增長=中資保司的起飛曲線"
        },
        "cross": {
          "sc": "内地热卖产品+香港平台=中资保司的差异化打法",
          "tc": "內地熱賣產品+香港平台=中資保司的差異化打法"
        }
      },
      "rolesImpact": {
        "front": 4,
        "midback": 1,
        "lead": 3,
        "cross": 4
      },
      "source": {
        "sc": "太保寿险香港 · 2025年",
        "lang": "sc"
      },
      "boards": [
        "product"
      ],
      "themes": [
        "product",
        "firm",
        "offshore"
      ],
      "tags": {
        "sc": [
          "太保",
          "增额终身寿",
          "世代鑫享"
        ],
        "tc": [
          "太保",
          "增額終身壽",
          "世代鑫享"
        ]
      },
      "contentKind": "product_notice",
      "publishedAt": "2025-08-20T10:00:00+08:00",
      "originalUrl": "https://www.time-weekly.com/post/317263"
    },
    {
      "id": "dlapiper-202508-commission",
      "clusterCount": 1,
      "score": 82,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T20:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "DLA Piper解读：保监局佣金分摊实务说明——2026年1月1日起实施。",
        "tc": "DLA Piper解讀：保監局佣金分攤實務說明——2026年1月1日起實施。"
      },
      "summary": {
        "sc": "DLA Piper 2025年8月发布法律解读：保监局佣金分摊实务说明2026年1月生效。首年佣金不超过总佣金70%，剩余30%至少5年均摊。新规同时覆盖代理人渠道和经纪渠道。[EN原文]",
        "tc": "DLA Piper:佣金分攤實務說明，首年≤70%"
      },
      "why": {
        "sc": "国际律所拆解佣金规则的实操含义，也是IFA收入模式变革指南。",
        "tc": "佣金規則的實操含義，也是收入模式變革。"
      },
      "actions": {
        "front": {
          "sc": "了解佣金分摊对个人收入的长期影响",
          "tc": "了解佣金分攤對收入影響"
        },
        "midback": {
          "sc": "更新薪酬计算与合规框架",
          "tc": "更新薪酬框架"
        },
        "lead": {
          "sc": "团队薪酬结构需适配分摊要求",
          "tc": "團隊薪酬需適配"
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "DLA Piper",
        "tc": "DLA Piper",
        "lang": "en"
      },
      "boards": [
        "compliance",
        "regulatory",
        "channel"
      ],
      "tags": {
        "sc": [
          "DLA Piper",
          "佣金分摊",
          "法律解读",
          "2025"
        ],
        "tc": [
          "DLA Piper",
          "佣金分攤",
          "法律解讀",
          "2025"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2025-08-15T10:00:00+08:00",
      "originalUrl": "https://www.dlapiper.com/en-us/insights/publications/2025/08/hong-kong-insurance-authority-issues-practice-note",
      "sourceKey": "dlapiper:commission-202508",
      "sourceTier": "pro",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-commission-20260101",
      "title": {
        "sc": "分红保单佣金分摊：2026-01-01 起首年不超过总额70%，其余至少分5年。",
        "tc": "分紅保單佣金分攤：2026-01-01 起首年不超過總額70%，其餘至少分5年。"
      },
      "summary": {
        "sc": "保监局就分红保单中介报酬结构推出分摊要求：自2026年1月1日起，定期缴费分红保单的首年佣金不超过总佣金70%，其余至少30%在不少于随后五年均匀摊付。市场报道称此为应对内地访客需求高企下的激励扭曲。",
        "tc": "保監局就分紅保單中介報酬結構推出分攤要求：自2026年1月1日起，定期繳費分紅保單的首年佣金不超過總佣金70%，其餘至少30%在不少於隨後五年均勻攤付。市場報道稱此為應對內地訪客需求高企下的激勵扭曲。"
      },
      "why": {
        "sc": "直接改写前线现金流转与团队激励表；系统未改先出单会埋对账雷。",
        "tc": "直接改寫前線現金流轉與團隊激勵表；系統未改先出單會埋對賬雷。"
      },
      "actions": {
        "front": {
          "sc": "向客户与转介方说明费用以书面与公司政策为准。",
          "tc": "向客戶與轉介方說明費用以書面與公司政策為準。"
        },
        "midback": {
          "sc": "重算各职级示例；更新签约课与计划书话术。｜发佣引擎、递延台账、保司对账三方勾稽抽检。",
          "tc": "重算各職級示例；更新簽約課與計劃書話術。｜發傭引擎、遞延台賬、保司對賬三方勾稽抽檢。"
        },
        "lead": {
          "sc": "评估激励ROI与产能波动；与保司商务对齐。",
          "tc": "評估激勵ROI與產能波動；與保司商務對齊。"
        },
        "cross": {
          "sc": "大额架构单多方分润提前合规预审。",
          "tc": "大額架構單多方分潤提前合規預審。"
        }
      },
      "source": {
        "sc": "保监局通函/实务说明 · 行业报道交叉",
        "tc": "保監局通函/實務說明 · 行業報道交叉"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "佣金",
          "分红",
          "2026"
        ],
        "tc": [
          "佣金",
          "分紅",
          "2026"
        ]
      },
      "themes": [
        "reg",
        "compliance",
        "product"
      ],
      "rolesImpact": {
        "front": 3,
        "midback": 3,
        "lead": 3,
        "cross": 2
      },
      "publishedAt": "2025-08-08T09:00:00+08:00",
      "effectiveAt": "2026-01-01",
      "clusterCount": 4,
      "score": 95,
      "verifyStatus": "verified",
      "originalUrl": "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/files/Cir_dd_30.7.2025_Practice_Note_for_Commission_Spreading_Eng.pdf",
      "featured": true,
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": true,
      "boards": [
        "product",
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "ia-20250808-rbc-disclosure",
      "title": {
        "sc": "风险为本资本制度首个财政年度公众披露要求（2025-08-08）。",
        "tc": "風險為本資本制度首個財政年度公眾披露要求（2025-08-08）。"
      },
      "summary": {
        "sc": "保监局2025年8月8日通函说明采纳风险为本资本（RBC）制度后首个财政年度的公众披露要求，提升保险人资本与风险管理透明度。",
        "tc": "保監局2025年8月8日通函說明採納風險為本資本（RBC）制度後首個財政年度的公眾披露要求，提升保險人資本與風險管理透明度。"
      },
      "why": {
        "sc": "专业顾问可用公开披露比较保司实力，而非只比演示。",
        "tc": "專業顧問可用公開披露比較保司實力，而非只比演示。"
      },
      "actions": {
        "front": {
          "sc": "大额单准备时查阅保司公开披露摘要。",
          "tc": "大額單準備時查閱保司公開披露摘要。"
        },
        "midback": {
          "sc": "把 RBC 披露要点纳入保司研究卡。｜关注披露时间表与可得文件。",
          "tc": "把 RBC 披露要點納入保司研究卡。｜關注披露時間表與可得文件。"
        },
        "lead": {
          "sc": "保司评分加入资本/披露质量维度。",
          "tc": "保司評分加入資本/披露質量維度。"
        },
        "cross": {
          "sc": "家办客户尽调可用作专业材料。",
          "tc": "家辦客戶盡調可用作專業材料。"
        }
      },
      "source": {
        "sc": "保监局规管通函 2025-08-08",
        "tc": "保監局規管通函 2025-08-08"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "RBC",
          "披露",
          "资本"
        ],
        "tc": [
          "RBC",
          "披露",
          "資本"
        ]
      },
      "themes": [
        "reg",
        "firm"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 2,
        "lead": 3,
        "cross": 2
      },
      "publishedAt": "2025-08-08T09:00:00+08:00",
      "score": 84,
      "verifyStatus": "verified",
      "featured": false,
      "originalUrl": "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/files/Circular_20250808_First_Year_Public_Disclosure.pdf",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "insurer",
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "fwd-iul-20250806",
      "clusterCount": 1,
      "score": 75,
      "verifyStatus": "verified",
      "sourceTier": "insurer",
      "sourceKey": "fwd",
      "title": {
        "sc": "富卫香港推出面向专业投资者的指数型万用寿险(IUL)计划",
        "tc": "富衛香港推出面向專業投資者的指數型萬用壽險(IUL)計劃"
      },
      "summary": {
        "sc": "2025 年 8 月，富卫香港推出面向专业投资者的指数型万用寿险（IUL）计划，成为继保监局 3 月联合通函后首批响应 IUL 产品开放的保司之一。产品设计以多元指数挂钩、下行保护为卖点，瞄准高净值客群的财富增值与传承需求。",
        "tc": "2025 年 8 月，富衛香港推出面向專業投資者的指數型萬用壽險（IUL）計劃，成為繼保監局 3 月聯合通函後首批響應 IUL 產品開放的保司之一。產品設計以多元指數掛鉤、下行保護為賣點，瞄準高淨值客群的財富增值與傳承需求。"
      },
      "why": {
        "sc": "IUL 是 2025-2026 年度港险产品创新的最热赛道。FWD 抢跑=抢占高净值 IUL 市场份额。了解谁在入局 IUL，就知道这条赛道的竞争烈度。",
        "tc": "IUL 是 2025-2026 年度港險產品創新的最熱賽道。FWD 搶跑=搶佔高淨值 IUL 市場份額。了解誰在入局 IUL，就知道這條賽道的競爭烈度。"
      },
      "actions": {
        "front": {
          "sc": "IUL是2025年开始面向IFA高净值客户的新品类",
          "tc": "IUL是2025年開始面向IFA高淨值客戶的新品類"
        },
        "midback": {},
        "lead": {
          "sc": "FWD抢跑IUL=产品创新赛道已开启",
          "tc": "FWD搶跑IUL=產品創新賽道已開啟"
        },
        "cross": {
          "sc": "IUL将保险与资本市场挂钩，跨境架构需求更大",
          "tc": "IUL將保險與資本市場掛鉤，跨境架構需求更大"
        }
      },
      "rolesImpact": {
        "front": 4,
        "midback": 1,
        "lead": 3,
        "cross": 3
      },
      "source": {
        "sc": "Insurance Business Mag · 2025年8月",
        "lang": "zh"
      },
      "boards": [
        "product"
      ],
      "themes": [
        "product",
        "offshore"
      ],
      "tags": {
        "sc": [
          "IUL",
          "富卫",
          "高净值"
        ],
        "tc": [
          "IUL",
          "富衛",
          "高淨值"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2025-08-06T10:00:00+08:00",
      "originalUrl": "https://www.insurancebusinessmag.com/asia/news/life-insurance/fwd-hong-kong-launches-indexed-universal-life-plan-for-professionals-521938.aspx"
    },
    {
      "id": "nfra-pricing-mechanism-2025",
      "clusterCount": 1,
      "score": 88,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "nfra",
      "title": {
        "sc": "NFRA 建立人身保险预定利率动态调整机制：传统型 2.0%、分红型 1.75%",
        "tc": "NFRA 建立人身保險預定利率動態調整機制：傳統型 2.0%、分紅型 1.75%"
      },
      "summary": {
        "sc": "2025 年，国家金融监管总局发布《关于健全人身保险产品定价机制的通知》：① 建立预定利率与市场利率挂钩的动态调整机制；② 传统型预定利率上限降至 2.0%，分红型 1.75%，万能型最低保证利率上限 1.5%；③ 深化「报行合一」全渠道覆盖。这是内地保险业历史上首次实现定价机制市场化动态调整。",
        "tc": "2025 年，國家金融監管總局發布《關於健全人身保險產品定價機制的通知》：① 建立預定利率與市場利率掛鉤的動態調整機制；② 傳統型預定利率上限降至 2.0%，分紅型 1.75%，萬能型最低保證利率上限 1.5%；③ 深化「報行合一」全渠道覆蓋。"
      },
      "why": {
        "sc": "这是内地保险业相当于香港「演示利率上限+佣金三件套」的打包版改革。预定利率从固定→浮动=内地保险产品的保证收益将持续走低。对 IFA：这个趋势每走一步，港险的利差优势就扩大一步。",
        "tc": "這是內地保險業相當於香港「演示利率上限+佣金三件套」的打包版改革。預定利率從固定→浮動=內地保險產品的保證收益將持續走低。對 IFA：這個趨勢每走一步，港險的利差優勢就擴大步。"
      },
      "actions": {
        "front": {
          "sc": "内地保证收益下行→港险相对吸引力持续上升",
          "tc": "內地保證收益下行→港險相對吸引力持續上升"
        },
        "midback": {},
        "lead": {
          "sc": "预定利率市场化=内地保险进入低保证收益时代",
          "tc": "預定利率市場化=內地保險進入低保證收益時代"
        },
        "cross": {
          "sc": "内地低利率+香港高分红=跨境配置逻辑清晰",
          "tc": "內地低利率+香港高分紅=跨境配置邏輯清晰"
        }
      },
      "rolesImpact": {
        "front": 5,
        "midback": 3,
        "lead": 5,
        "cross": 5
      },
      "source": {
        "sc": "国家金融监管总局 · 2025年",
        "lang": "sc"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "reg",
        "product",
        "offshore"
      ],
      "tags": {
        "sc": [
          "预定利率",
          "报行合一",
          "定价机制"
        ],
        "tc": [
          "預定利率",
          "報行合一",
          "定價機制"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2025-08-02T10:00:00+08:00",
      "originalUrl": "https://www.nfra.gov.cn/cn/view/pages/ItemDetail.html?docId=1175200"
    },
    {
      "id": "manulife-bupa-mou-2025",
      "clusterCount": 1,
      "score": 71,
      "verifyStatus": "verified",
      "sourceTier": "insurer",
      "sourceKey": "manulife",
      "title": {
        "sc": "宏利与保柏（Bupa）签订合作备忘录：香港医疗险策略合作",
        "tc": "宏利與保柏（Bupa）簽訂合作備忘錄：香港醫療險策略合作"
      },
      "summary": {
        "sc": "宏利香港与保柏（Bupa）签订合作备忘录，于香港展开策略性合作，聚焦医疗健康保障领域。双方将结合宏利的保险分销网络与保柏的医疗服务能力，拓展香港医疗险市场。",
        "tc": "宏利香港與保柏（Bupa）簽訂合作備忘錄，於香港展開策略性合作，聚焦醫療健康保障領域。"
      },
      "why": {
        "sc": "保司×医疗集团合作=健康险从「卖保单」转向「卖服务」。宏利已有内地 3.8 万+ 医院网络，再叠加保柏的医疗服务，说明医疗险竞争的主战场正在从价格转向生态。",
        "tc": "保司×醫療集團合作=健康險從「賣保單」轉向「賣服務」。醫療險競爭的主戰場正在從價格轉向生態。"
      },
      "actions": {
        "front": {
          "sc": "保险×医疗生态=健康险新竞争维度",
          "tc": "保險×醫療生態=健康險新競爭維度"
        },
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 3,
        "midback": 1,
        "lead": 2,
        "cross": 2
      },
      "source": {
        "sc": "宏利香港 · 2025年",
        "lang": "sc"
      },
      "boards": [
        "product"
      ],
      "themes": [
        "product",
        "health",
        "firm"
      ],
      "tags": {
        "sc": [
          "宏利",
          "保柏",
          "医疗险",
          "合作"
        ],
        "tc": [
          "宏利",
          "保柏",
          "醫療險",
          "合作"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2025-07-28T10:00:00+08:00",
      "originalUrl": "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html"
    },
    {
      "id": "h1-2025-record-99b-202507",
      "clusterCount": 1,
      "score": 78,
      "verifyStatus": "verified",
      "sourceTier": "media",
      "sourceKey": "insuranceasia",
      "title": {
        "sc": "2025 上半年港险新单保费创纪录 990 亿港元 +39%：MCV 双引擎",
        "tc": "2025 上半年港險新單保費創紀錄 990 億港元 +39%：MCV 雙引擎"
      },
      "summary": {
        "sc": "2025 上半年香港保险新单保费达创纪录的 990 亿港元（约 127 亿美元），按年增长 39%。友邦香港业务录得强劲增长，内地访客（MCV）与本地市场双引擎驱动。CreditSights 指港险保司上半年盈利强劲：FWD LCSM 比率升至 283%，友邦 GWS 覆盖率 254%。",
        "tc": "2025 上半年香港保險新單保費達創紀錄的 990 億港元（約 127 億美元），按年增長 39%。友邦香港業務錄得強勁增長，內地訪客（MCV）與本地市場雙引擎驅動。"
      },
      "why": {
        "sc": "990 亿 +39%=演示利率上限生效前夜的「抢购潮」。7 月 1 日上限落地前，市场用真金白银赶在旧演示利率下投保——这是理解 2025 全年数据必须知道的前置背景。",
        "tc": "990 億 +39%=演示利率上限生效前夜的「搶購潮」。7 月 1 日上限落地前，市場趕在舊演示利率下投保。"
      },
      "actions": {
        "front": {
          "sc": "990亿+39%=H1的「抢购潮」实证",
          "tc": "990億+39%=H1的「搶購潮」實證"
        },
        "midback": {},
        "lead": {
          "sc": "新规前抢购=客户行为模式的样本",
          "tc": "新規前搶購=客戶行為模式的樣本"
        },
        "cross": {
          "sc": "MCV双引擎=跨境需求仍在高位",
          "tc": "MCV雙引擎=跨境需求仍在高位"
        }
      },
      "rolesImpact": {
        "front": 4,
        "midback": 1,
        "lead": 3,
        "cross": 3
      },
      "source": {
        "sc": "InsuranceAsia · 2025年7月",
        "lang": "zh"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "market",
        "offshore"
      ],
      "tags": {
        "sc": [
          "H1",
          "990亿",
          "保费",
          "抢购潮"
        ],
        "tc": [
          "H1",
          "990億",
          "保費",
          "搶購潮"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2025-07-25T10:00:00+08:00",
      "originalUrl": "https://insuranceasia.com/insurance/news/creditsights-says-hong-kong-life-insurers-sustain-strong-growth"
    },
    {
      "id": "manulife-redomiciliation-done-2025",
      "clusterCount": 1,
      "score": 84,
      "verifyStatus": "verified",
      "sourceTier": "insurer",
      "sourceKey": "manulife",
      "title": {
        "sc": "宏利人寿（国际）完成迁册至香港：首家完成迁册的保险公司",
        "tc": "宏利人壽（國際）完成遷冊至香港：首家完成遷冊的保險公司"
      },
      "summary": {
        "sc": "宏利人寿保险（国际）有限公司成功迁册至香港，成为首家完成迁册流程的保险公司。此前《2025年公司（修订）（第2号）条例》5 月生效，为海外注册企业迁册回港提供便利。宏利迁册后，监管重心、资本配置与业务重心全面移向香港。",
        "tc": "宏利人壽保險（國際）有限公司成功遷冊至香港，成為首家完成遷冊流程的保險公司。此前《2025年公司（修訂）（第2號）條例》5 月生效。"
      },
      "why": {
        "sc": "从「宣布迁册」到「完成迁册」是质变。宏利用真金白银投票：香港不仅是销售市场，更是总部与监管主场。对 IFA：这是向客户解释「香港保险安全」的顶级论据。",
        "tc": "從「宣佈遷冊」到「完成遷冊」是質變。宏利用真金白銀投票：香港不僅是銷售市場，更是總部與監管主場。"
      },
      "actions": {
        "front": {
          "sc": "宏利迁册=「香港保险安全」的顶级论据",
          "tc": "宏利遷冊=「香港保險安全」的頂級論據"
        },
        "midback": {
          "sc": "监管主体落地=合规确定性提升",
          "tc": "監管主體落地=合規確定性提升"
        },
        "lead": {
          "sc": "首家完成=制度红利兑现的样板",
          "tc": "首家完成=制度紅利兌現的樣板"
        },
        "cross": {
          "sc": "国际保司重仓香港=枢纽地位再确认",
          "tc": "國際保司重倉香港=樞紐地位再確認"
        }
      },
      "rolesImpact": {
        "front": 4,
        "midback": 3,
        "lead": 4,
        "cross": 4
      },
      "source": {
        "sc": "宏利香港 · 2025年",
        "lang": "sc"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "firm",
        "reg"
      ],
      "tags": {
        "sc": [
          "宏利",
          "迁册",
          "首家"
        ],
        "tc": [
          "宏利",
          "遷冊",
          "首家"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2025-07-20T10:00:00+08:00",
      "originalUrl": "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html"
    },
    {
      "id": "ia-202507-commission-spread",
      "clusterCount": 1,
      "score": 93,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": true,
      "ingestedAt": "2026-07-28T13:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "保监局发布分红保单佣金分摊指引：2026年1月1日起实施。",
        "tc": "保監局發布分紅保單佣金分攤指引：2026年1月1日起實施。"
      },
      "summary": {
        "sc": "保监局2025年7月发布应用说明，正式调整分红保单佣金结构：自2026年1月1日起，首年佣金不超过总佣金70%，其余至少30%在随后5年均匀摊付。此为分红保单销售三项措施的第三环。",
        "tc": "保監局发布佣金分摊指引，2026年1月實施"
      },
      "why": {
        "sc": "佣金分摊，也是经纪人收入模式根本改变，从量转向质。",
        "tc": "佣金分攤，也是經紀收入模式根本改變。"
      },
      "actions": {
        "front": {
          "sc": "了解佣金分摊对个人收入的影响",
          "tc": "了解佣金分攤對個人收入影響"
        },
        "midback": {
          "sc": "更新佣金计算模板",
          "tc": "更新佣金計算模板"
        },
        "lead": {
          "sc": "重新设计团队激励方案，适应分年收取模式",
          "tc": "重新設計團隊激勵方案"
        },
        "cross": {
          "sc": "跨境客户的佣金分摊是否符合两地规则",
          "tc": "跨境佣金分攤合規評估"
        }
      },
      "source": {
        "sc": "IA 保监局应用说明",
        "tc": "IA 保監局應用說明",
        "lang": "zh"
      },
      "boards": [
        "regulatory",
        "channel"
      ],
      "tags": {
        "sc": [
          "佣金分摊",
          "70%",
          "首年",
          "2026"
        ],
        "tc": [
          "佣金分攤",
          "70%",
          "首年",
          "2026"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2025-07-15T14:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/commission_spreading.html",
      "sourceKey": "ia",
      "sourceTier": "official",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20250711-ro-cpd-compulsory",
      "title": {
        "sc": "经纪公司负责人强制RO-CPD自2025-08-01生效（2025-07-11）。",
        "tc": "經紀公司負責人強制RO-CPD自2025-08-01生效（2025-07-11）。"
      },
      "summary": {
        "sc": "保监局2025年7月11日通函明确所有保险经纪公司负责人强制性持续专业培训要求自2025年8月1日起生效，同步修订 GL24。",
        "tc": "保監局2025年7月11日通函明確所有保險經紀公司負責人強制性持續專業培訓要求自2025年8月1日起生效，同步修訂 GL24。"
      },
      "why": {
        "sc": "RO 能力直接决定公司合规水位与出单审批质量。",
        "tc": "RO 能力直接決定公司合規水位與出單審批質量。"
      },
      "actions": {
        "front": {
          "sc": "理解 RO 审核点，减少退件。",
          "tc": "理解 RO 審核點，減少退件。"
        },
        "midback": {
          "sc": "RO 培训排期与课程资源。｜RO 达标监控与证明存档。",
          "tc": "RO 培訓排期與課程資源。｜RO 達標監控與證明存檔。"
        },
        "lead": {
          "sc": "后备 RO 与职责分工。",
          "tc": "後備 RO 與職責分工。"
        },
        "cross": {
          "sc": "无直接动作。",
          "tc": "無直接動作。"
        }
      },
      "source": {
        "sc": "保监局规管通函 2025-07-11",
        "tc": "保監局規管通函 2025-07-11"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "RO-CPD",
          "GL24"
        ],
        "tc": [
          "RO-CPD",
          "GL24"
        ]
      },
      "themes": [
        "career",
        "compliance",
        "reg"
      ],
      "rolesImpact": {
        "front": 1,
        "midback": 3,
        "lead": 2,
        "cross": 0
      },
      "publishedAt": "2025-07-11T09:00:00+08:00",
      "effectiveAt": "2025-08-01",
      "score": 85,
      "verifyStatus": "verified",
      "featured": false,
      "originalUrl": "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/files/Circular_ROCPD_20250711.pdf",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "aia-20250708-global-prosper",
      "clusterCount": 1,
      "score": 80,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T18:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "AIA推出「环宇盈活储蓄保险计划」",
        "tc": "AIA推出「環宇盈活儲蓄保險計劃」"
      },
      "summary": {
        "sc": "AIA 2025年7月8日推出「环宇盈活储蓄保险计划」，为高净值客户提供跨货币、跨市场的灵活财富配置方案。",
        "tc": "AIA 7月8日推出高净值環球儲蓄計劃"
      },
      "why": {
        "sc": "AIA在高净值市场的产品布局持续深化。",
        "tc": "AIA高净值產品佈局。"
      },
      "actions": {
        "front": {
          "sc": "加入产品对比表",
          "tc": "加入產品對比"
        },
        "midback": {
          "sc": "收集产品费率",
          "tc": "收集產品資料"
        },
        "lead": {
          "sc": ""
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "AIA 新闻稿",
        "tc": "AIA 新聞稿",
        "lang": "zh"
      },
      "boards": [
        "product",
        "firm"
      ],
      "tags": {
        "sc": [
          "AIA",
          "储蓄",
          "高净值",
          "2025"
        ],
        "tc": [
          "AIA",
          "儲蓄",
          "高淨值",
          "2025"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2025-07-08T10:00:00+08:00",
      "originalUrl": "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/2025/aia-press-release-20250708",
      "sourceKey": "aia",
      "sourceTier": "insurer",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20250701-illustration-cap",
      "clusterCount": 1,
      "score": 97,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": true,
      "ingestedAt": "2026-07-28T13:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "分红保单演示利率上限正式生效：非港元6.5%/港元6.0%。",
        "tc": "分紅保單演示利率上限正式生效：非港元6.5%/港元6.0%。"
      },
      "summary": {
        "sc": "保监局2024年2月发布的演示利率上限框架于2025年7月1日生效。非港元保单演示IRR上限6.5%，港元保单6.0%。新规为分红保单销售三项措施的第一环，后续包括转介费基准(10月)和佣金分摊(2026年1月)。",
        "tc": "演示利率上限2025年7月1日生效"
      },
      "why": {
        "sc": "演示利率上限是分红险监管的里程碑，彻底改变产品展示方式。",
        "tc": "演示利率上限是分紅險監管里程碑。"
      },
      "actions": {
        "front": {
          "sc": "所有客户沟通中使用合规演示利率",
          "tc": "所有溝通使用合規演示利率"
        },
        "midback": {
          "sc": "更新产品手册中的演示利率数据",
          "tc": "更新產品手冊演示利率"
        },
        "lead": {
          "sc": "团队培训：演示利率上限的三项措施全貌",
          "tc": "團隊培訓演示利率全貌"
        },
        "cross": {
          "sc": "跨境客户需要解释演示利率与保证利率的区别",
          "tc": "解釋演示與保證利率區別"
        }
      },
      "source": {
        "sc": "IA 保监局通函",
        "tc": "IA 保監局通函",
        "lang": "zh"
      },
      "boards": [
        "regulatory",
        "product"
      ],
      "tags": {
        "sc": [
          "演示利率",
          "上限",
          "6.5%",
          "分红",
          "2025"
        ],
        "tc": [
          "演示利率",
          "上限",
          "6.5%",
          "分紅",
          "2025"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2025-07-01T09:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/illustration_cap.html",
      "sourceKey": "ia",
      "sourceTier": "official",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "crossborder-payment-link-202506",
      "clusterCount": 1,
      "score": 80,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "hkma",
      "title": {
        "sc": "跨境支付通上线：内地居民可经人民币通道汇款至香港",
        "tc": "跨境支付通上線：內地居民可經人民幣通道匯款至香港"
      },
      "summary": {
        "sc": "2025 年 6 月，内地与香港联合推出跨境支付通（Cross-boundary Payment Link）。分南向通/北向通：内地居民可转账至香港，免去换汇环节、突破银行卡限制，目前不支持香港转回内地。这是内地资金合法流入香港的又一官方通道。",
        "tc": "2025 年 6 月，內地與香港聯合推出跨境支付通（Cross-boundary Payment Link）。分南向通/北向通：內地居民可轉賬至香港，免去換匯環節。"
      },
      "why": {
        "sc": "对 IFA 是获客基础设施级别的变化：内地客户资金出境从此多了一条官方直连通道。跨境支付通+理财通+QDII 三通道并行，意味着「钱怎么到香港」的问题在快速被制度化解。",
        "tc": "對 IFA 是獲客基礎設施級別的變化：內地客戶資金出境從此多了一條官方直連通道。"
      },
      "actions": {
        "front": {
          "sc": "跨境支付通=客户资金入港的官方新管道",
          "tc": "跨境支付通=客戶資金入港的官方新管道"
        },
        "midback": {
          "sc": "人民币直汇=资金流向监管可见性提升",
          "tc": "人民幣直匯=資金流向監管可見性提升"
        },
        "lead": {
          "sc": "资金通道扩容=香港财富管理增量引擎",
          "tc": "資金通道擴容=香港財富管理增量引擎"
        },
        "cross": {
          "sc": "跨境支付通+理财通+QDII=三大通道格局成形",
          "tc": "跨境支付通+理財通+QDII=三大通道格局成形"
        }
      },
      "rolesImpact": {
        "front": 4,
        "midback": 2,
        "lead": 4,
        "cross": 5
      },
      "source": {
        "sc": "金管局 · 2025年6月",
        "lang": "sc"
      },
      "boards": [
        "family"
      ],
      "themes": [
        "offshore",
        "global-allocation",
        "monetary"
      ],
      "tags": {
        "sc": [
          "跨境支付通",
          "资金通道",
          "南向通"
        ],
        "tc": [
          "跨境支付通",
          "資金通道",
          "南向通"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2025-06-20T10:00:00+08:00",
      "originalUrl": "https://www.hkma.gov.hk/eng/key-functions/international-financial-centre/cross-boundary-payment-link/"
    },
    {
      "id": "sunlife-2025-enhanced-savings",
      "clusterCount": 1,
      "score": 77,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T18:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "Sun Life永明推出升级版储蓄保险计划系列（永越多元货币II）。",
        "tc": "Sun Life永明推出升級版儲蓄保險計劃系列（永越多元貨幣II）。"
      },
      "summary": {
        "sc": "Sun Life永明2025年推出升级版储蓄保险计划系列，包括永越多元货币计划II。延长保障至终身，提供学术成就奖赏等差异化功能。",
        "tc": "永明推出永越多元貨幣II儲蓄計劃"
      },
      "why": {
        "sc": "永明储蓄产品线重大升级，也是市场份额扩张基础。",
        "tc": "永明儲蓄產品重大升級。"
      },
      "actions": {
        "front": {
          "sc": "加入产品对比表",
          "tc": "加入產品對比"
        },
        "midback": {
          "sc": "更新产品库",
          "tc": "更新產品庫"
        },
        "lead": {
          "sc": ""
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "永明新闻稿",
        "tc": "永明新聞稿",
        "lang": "zh"
      },
      "boards": [
        "product",
        "firm"
      ],
      "tags": {
        "sc": [
          "永明",
          "永越",
          "多元货币",
          "2025"
        ],
        "tc": [
          "永明",
          "永越",
          "多元貨幣",
          "2025"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2025-06-15T10:00:00+08:00",
      "originalUrl": "https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/2025/sun-life-unveils-suite-of-enhanced-savings-insurance-plans/",
      "sourceKey": "sunlife",
      "sourceTier": "insurer",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-2025q1-stats-934",
      "clusterCount": 1,
      "score": 86,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T14:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "2025年Q1香港长期业务新单保费934亿同比+43.1%创新高。",
        "tc": "2025年Q1香港長期業務新單保費934億同比+43.1%創新高。"
      },
      "summary": {
        "sc": "保监局公布2025年首季临时统计：长期业务新单保费934亿港元同比+43.1%，创历史新高。全年保费同比+51%，新单保费+50.6%。内地访客贡献显著，终身寿险占比超80%。",
        "tc": "2025年Q1新單保費934億創新高"
      },
      "why": {
        "sc": "演示利率上限前的抢购潮，也是行业历史性节点，数据可用于市场分析。",
        "tc": "演示利率上限前搶購潮，也是行業歷史性節點。"
      },
      "actions": {
        "front": {
          "sc": "用数据向客户展示港险热度与合规趋势",
          "tc": "展示港險熱度與合規趨勢"
        },
        "midback": {
          "sc": "归档Q1数据，做年度对比分析",
          "tc": "歸檔Q1數據對比分析"
        },
        "lead": {
          "sc": "基于市场数据调整团队策略",
          "tc": "基於數據調整策略"
        },
        "cross": {
          "sc": "内地访客数据=跨境营销核心参考",
          "tc": "內地訪客數據=核心參考"
        }
      },
      "source": {
        "sc": "IA 保监局统计",
        "tc": "IA 保監局統計",
        "lang": "zh"
      },
      "boards": [
        "regulatory",
        "macro"
      ],
      "tags": {
        "sc": [
          "Q1统计",
          "保费",
          "934亿",
          "2025"
        ],
        "tc": [
          "Q1統計",
          "保費",
          "934億",
          "2025"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2025-06-15T10:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/en/infocenter/statistics/",
      "sourceKey": "ia",
      "sourceTier": "official",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "fstb-2024-density",
      "clusterCount": 1,
      "score": 86,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": true,
      "ingestedAt": "2026-07-28T21:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "香港保险密度0043全球第二 渗透率18.2%全球第一。",
        "tc": "香港保險密度0043全球第二 滲透率18.2%全球第一。"
      },
      "summary": {
        "sc": "财经事务及库务局公布2024年香港保险市场数据：保险密度约10043美元全球第二，保险渗透率18.2%全球第一。毛保费总额814亿美元。香港汇聚超150家国际保险公司，逾10万名持牌中介。",
        "tc": "密度0043全球第二 滲透率18.2%全球第一"
      },
      "why": {
        "sc": "全球排名，也是香港保险市场的国际地位不容置疑。",
        "tc": "全球排名，也是香港國際地位。"
      },
      "actions": {
        "front": {
          "sc": "客户问为什么香港保险好?用这两个数据回答",
          "tc": "客戶問為什麼香港保險好?用數據回答"
        },
        "midback": {
          "sc": "归档市场地位数据",
          "tc": "歸檔市場數據"
        },
        "lead": {
          "sc": "全球第一的渗透率=市场深度和成熟度",
          "tc": "市場深度和成熟度"
        },
        "cross": {
          "sc": "渗透率全球第一=对内地客户的最强背书",
          "tc": "最強背書"
        }
      },
      "source": {
        "sc": "财库局",
        "tc": "財庫局",
        "lang": "zh"
      },
      "boards": [
        "macro"
      ],
      "tags": {
        "sc": [
          "密度",
          "渗透率",
          "国际排名"
        ],
        "tc": [
          "密度",
          "滲透率",
          "國際排名"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2025-06-01T10:00:00+08:00",
      "originalUrl": "https://www.fstb.gov.hk/tc/financial_ser/insurance-industry.htm",
      "sourceKey": "govhk",
      "sourceTier": "official",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "mainland-capital-surge-2025",
      "clusterCount": 1,
      "score": 84,
      "verifyStatus": "verified",
      "sourceTier": "media",
      "sourceKey": "insurancebusinessmag",
      "title": {
        "sc": "中资加速入场香港保险：越秀17.68亿收购香港人寿/京东更名/腾讯FuSure获批长险牌照",
        "tc": "中資加速入場香港保險：越秀17.68億收購香港人壽/京東更名/騰訊FuSure獲批長險牌照"
      },
      "summary": {
        "sc": "2025 年香港保险业中资布局全面加速：① 越秀集团 17.68 亿港元收购香港人寿；② 京东收购经纪行并更名「京东保险顾问（香港）」；③ 腾讯旗下赋诚再保险（FuSure）获批长期保险牌照，业务线从一般保险扩展至多元化。国寿海外、中银香港、太平、太保、万通市场份额均上升。",
        "tc": "2025 年香港保險業中資佈局全面加速：① 越秀集團 17.68 億港元收購香港人壽；② 京東收購經紀行並更名「京東保險顧問（香港）」；③ 騰訊旗下賦誠再保險（FuSure）獲批長期保險牌照。"
      },
      "why": {
        "sc": "中资巨头（地产系/电商系/科技系）同时涌入=香港保险被视为确定性赛道。对 IFA：新玩家带来新渠道和新打法（京东/腾讯自带流量生态），渠道格局的洗牌已经开始。",
        "tc": "中資巨頭（地產系/電商系/科技系）同時湧入=香港保險被視為確定性賽道。對 IFA：新玩家帶來新渠道和新打法，渠道格局的洗牌已經開始。"
      },
      "actions": {
        "front": {
          "sc": "中资巨头入场=渠道格局进入洗牌期",
          "tc": "中資巨頭入場=渠道格局進入洗牌期"
        },
        "midback": {
          "sc": "科技系玩家=经纪业务的数字化竞争者",
          "tc": "科技系玩家=經紀業務的數字化競爭者"
        },
        "lead": {
          "sc": "资本用真金白银投票=香港保险是确定性赛道",
          "tc": "資本用真金白銀投票=香港保險是確定性賽道"
        },
        "cross": {
          "sc": "中资网络+香港平台=跨境生态闭环加速",
          "tc": "中資網絡+香港平台=跨境生態閉環加速"
        }
      },
      "rolesImpact": {
        "front": 4,
        "midback": 4,
        "lead": 4,
        "cross": 4
      },
      "source": {
        "sc": "行业综合 · 2025年",
        "lang": "sc"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "channel",
        "firm",
        "offshore"
      ],
      "tags": {
        "sc": [
          "中资",
          "越秀",
          "京东",
          "腾讯",
          "渠道"
        ],
        "tc": [
          "中資",
          "越秀",
          "京東",
          "騰訊",
          "渠道"
        ]
      },
      "contentKind": "industry_news",
      "publishedAt": "2025-05-28T10:00:00+08:00",
      "originalUrl": "https://zhuanlan.zhihu.com/p/1996682970564694535"
    },
    {
      "id": "redomiciliation-2025-act",
      "clusterCount": 1,
      "score": 79,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "govhk",
      "title": {
        "sc": "迁册制度条例 2025 年 5 月生效：宏利成首家迁册回港保险公司",
        "tc": "遷冊制度條例 2025 年 5 月生效：宏利成首家遷冊回港保險公司"
      },
      "summary": {
        "sc": "2025 年 5 月，香港《2025年公司（修订）（第2号）条例》生效，迁册制度正式落地——海外注册企业可便利迁册回港。宏利完成迁册流程，成为第一家迁册回港的保险公司；安盛亦公开宣布迁册计划（2026 年 1 月完成）。注意：迁册后可能无法开展百慕大离岸保险业务，对牌照型保险公司是权衡。",
        "tc": "2025 年 5 月，香港《2025年公司（修訂）（第2號）條例》生效，遷冊制度正式落地。宏利完成遷冊流程，成為第一家遷冊回港的保險公司。"
      },
      "why": {
        "sc": "迁册制度=香港抢公司的制度武器。保司从百慕大迁回香港，意味着监管重心、资本配置、业务重心全面移向香港——这是香港作为保险枢纽的实质性胜利。",
        "tc": "遷冊制度=香港搶公司的制度武器。保司從百慕大遷回香港，意味著監管重心、資本配置、業務重心全面移向香港。"
      },
      "actions": {
        "front": {},
        "midback": {
          "sc": "迁册=保司监管主体向香港集中的信号",
          "tc": "遷冊=保司監管主體向香港集中的信號"
        },
        "lead": {
          "sc": "首家迁册完成=制度红利开始兑现",
          "tc": "首家遷冊完成=制度紅利開始兌現"
        },
        "cross": {
          "sc": "国际保司重仓香港=枢纽地位再确认",
          "tc": "國際保司重倉香港=樞紐地位再確認"
        }
      },
      "rolesImpact": {
        "front": 2,
        "midback": 3,
        "lead": 4,
        "cross": 4
      },
      "source": {
        "sc": "香港特区政府 · 2025年5月",
        "lang": "sc"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "reg",
        "firm"
      ],
      "tags": {
        "sc": [
          "迁册",
          "宏利",
          "百慕大"
        ],
        "tc": [
          "遷冊",
          "宏利",
          "百慕大"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2025-05-15T10:00:00+08:00",
      "originalUrl": "https://www.fstb.gov.hk/en/blog/blog141225.htm"
    },
    {
      "id": "fwd-q1-2025-csm",
      "clusterCount": 1,
      "score": 73,
      "verifyStatus": "verified",
      "sourceTier": "insurer",
      "sourceKey": "fwd",
      "title": {
        "sc": "富卫 2025 Q1 新业务合约服务边际 +55%：港澳市场双位数增长",
        "tc": "富衛 2025 Q1 新業務合約服務邊際 +55%：港澳市場雙位數增長"
      },
      "summary": {
        "sc": "富卫集团 2025 年首季新业务表现强劲：新业务合约服务边际（CSM）按年增长 55% 至 4.65 亿美元。香港及澳门市场主要业务指标均录得双位数增长，受惠于高净值市场扩张。",
        "tc": "富衛集團 2025 年首季新業務表現強勁：新業務合約服務邊際（CSM）按年增長 55% 至 4.65 億美元。香港及澳門市場主要業務指標均錄得雙位數增長。"
      },
      "why": {
        "sc": "富卫是港险市场增长最快的非巨头玩家，其 CSM 增速是判断新兴保司势头的指标。+55% 说明高净值+指数型产品策略正在兑现。",
        "tc": "富衛是港險市場增長最快的非巨頭玩家，其 CSM 增速是判斷新興保司勢頭的指標。+55% 說明高淨值+指數型產品策略正在兌現。"
      },
      "actions": {
        "front": {
          "sc": "富卫CSM+55%=高净值策略正在兑现",
          "tc": "富衛CSM+55%=高淨值策略正在兌現"
        },
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 3,
        "midback": 1,
        "lead": 2,
        "cross": 2
      },
      "source": {
        "sc": "富卫集团 · 2025年5月",
        "lang": "zh"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "firm",
        "market"
      ],
      "tags": {
        "sc": [
          "富卫",
          "CSM",
          "Q1",
          "业绩"
        ],
        "tc": [
          "富衛",
          "CSM",
          "Q1",
          "業績"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2025-05-08T10:00:00+08:00",
      "originalUrl": "https://www.fwd.com/zh/newsroom/press-releases/FWD-Group-reports-exceptionally-strong-first-quarter-new-business-update/"
    },
    {
      "id": "aia-q1-2025-vonb",
      "clusterCount": 1,
      "score": 77,
      "verifyStatus": "verified",
      "sourceTier": "insurer",
      "sourceKey": "aia",
      "title": {
        "sc": "友邦 2025 Q1 新业务价值 +13%：香港市场 MCV 带动增长",
        "tc": "友邦 2025 Q1 新業務價值 +13%：香港市場 MCV 帶動增長"
      },
      "summary": {
        "sc": "2025 年 4 月 30 日，友邦集团公布 2025 年首季新业务亮点：VONB 按固定汇率计增长 13%。香港业务在本地及内地访客（MCV）双引擎带动下录得强劲增长，继续保持市场第一。",
        "tc": "2025 年 4 月 30 日，友邦集團公佈 2025 年首季新業務亮點：VONB 按固定匯率計增長 13%。香港業務在本地及內地訪客（MCV）雙引擎帶動下錄得強勁增長。"
      },
      "why": {
        "sc": "友邦是香港市场头号保司，其季度 VONB 是行业温度的即时计。Q1 +13% 说明 2025 年初跨境需求仍在高位，这是 IFA 判断市场节奏的重要锚点。",
        "tc": "友邦是香港市場頭號保司，其季度 VONB 是行業溫度的即時計。Q1 +13% 說明 2025 年初跨境需求仍在高位。"
      },
      "actions": {
        "front": {
          "sc": "友邦VONB+13%=市场头部仍在高速扩张",
          "tc": "友邦VONB+13%=市場頭部仍在高速擴張"
        },
        "midback": {},
        "lead": {
          "sc": "香港双引擎增长=代理渠道的机会窗口",
          "tc": "香港雙引擎增長=代理渠道的機會窗口"
        },
        "cross": {
          "sc": "MCV继续是香港增长主线",
          "tc": "MCV繼續是香港增長主線"
        }
      },
      "rolesImpact": {
        "front": 4,
        "midback": 1,
        "lead": 3,
        "cross": 3
      },
      "source": {
        "sc": "友邦集团 · 2025年4月30日",
        "lang": "zh"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "firm",
        "market"
      ],
      "tags": {
        "sc": [
          "友邦",
          "VONB",
          "Q1",
          "业绩"
        ],
        "tc": [
          "友邦",
          "VONB",
          "Q1",
          "業績"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2025-04-30T10:00:00+08:00",
      "originalUrl": "https://www.aia.com/content/dam/group-wise/en/docs/investor-relations/2025/AIA%20Group%202025%20Q1%20New%20Business%20Highlights%20(Eng).pdf"
    },
    {
      "id": "manulife-20250428-ci",
      "clusterCount": 1,
      "score": 82,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T18:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "宏利推出两款全新危疾计划：宏健守护+宏伴护航危疾入息保障。",
        "tc": "宏利推出兩款全新危疾計劃：宏健守護+宏伴護航危疾入息保障。"
      },
      "summary": {
        "sc": "宏利香港2025年4月28日推出「宏健守护危疾入息保障」及「宏伴护航危疾入息保障」两款全新危疾保险计划，以行业领先的年度危疾赔偿帮助客户应对长期治疗收入损失。",
        "tc": "宏利4月28日推出兩款全新危疾計劃"
      },
      "why": {
        "sc": "宏利危疾线的创新：年度赔偿而非一次性赔款，也是差异化。",
        "tc": "宏利危疾創新，也是年度賠償。"
      },
      "actions": {
        "front": {
          "sc": "危疾客户的新选择",
          "tc": "危疾客戶新選擇"
        },
        "midback": {
          "sc": "更新危疾产品对比",
          "tc": "更新危疾產品對比"
        },
        "lead": {
          "sc": ""
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "宏利新闻稿",
        "tc": "宏利新聞稿",
        "lang": "zh"
      },
      "boards": [
        "product",
        "firm"
      ],
      "tags": {
        "sc": [
          "宏利",
          "危疾",
          "入息保障",
          "2025"
        ],
        "tc": [
          "宏利",
          "危疾",
          "入息保障",
          "2025"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2025-04-28T10:00:00+08:00",
      "originalUrl": "https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html",
      "sourceKey": "manulife",
      "sourceTier": "insurer",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-2025-d-sii-designation",
      "clusterCount": 1,
      "score": 83,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": true,
      "ingestedAt": "2026-07-28T14:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "保监局指定AIA及保诚亚洲为具系统重要性保险机构(D-SII)。",
        "tc": "保監局指定AIA及保誠亞洲為具系統重要性保險機構(D-SII)。"
      },
      "summary": {
        "sc": "保监局2025年正式指定AIA集团及保诚亚洲为香港境内具系统重要性保险机构(Domestic Systemically Important Insurers)，实施额外监管要求，包括更高的资本缓冲和恢复与处置规划。",
        "tc": "保監局指定AIA及保誠為D-SII，實施額外監管"
      },
      "why": {
        "sc": "D-SII，也是大而不能倒，AIA和保诚的安全性获监管背书。",
        "tc": "D-SII，也是安全性獲監管背書。"
      },
      "actions": {
        "front": {
          "sc": "客户问'哪家最安全'时可用D-SII认证加分",
          "tc": "客戶問安全性時引用D-SII"
        },
        "midback": {
          "sc": "更新保司评估档案中D-SII状态",
          "tc": "更新D-SII狀態"
        },
        "lead": {
          "sc": "D-SII保司=合作首选，尽调简化",
          "tc": "D-SII保司=合作首選"
        },
        "cross": {
          "sc": "D-SII认定对跨境再保险安排的影响评估",
          "tc": "D-SII對跨境再保影響"
        }
      },
      "source": {
        "sc": "IA 保监局",
        "tc": "IA 保監局",
        "lang": "en"
      },
      "boards": [
        "regulatory",
        "firm"
      ],
      "tags": {
        "sc": [
          "D-SII",
          "AIA",
          "保诚",
          "系统重要性"
        ],
        "tc": [
          "D-SII",
          "AIA",
          "保誠",
          "系統重要性"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2025-04-15T10:00:00+08:00",
      "originalUrl": "https://beinsure.com/news/hong-kong-names-aia-prudential-asia/",
      "sourceKey": "prudential",
      "sourceTier": "insurer",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-mcv-data-gap-2025",
      "clusterCount": 1,
      "score": 82,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "ia",
      "title": {
        "sc": "保监局停止披露内地访客新造保费细分：MCV 数据进入「盲区」",
        "tc": "保監局停止披露內地訪客新造保費細分：MCV 數據進入「盲區」"
      },
      "summary": {
        "sc": "自 2025 年 Q1 起，保监局临时统计不再披露内地访客（MCV）新造保费的细分数据。最后一个完整口径是 2025 年 4 月公布的 2024 全年数据：内地访客新造保费 628 亿港元，占个人新单 28.6%（终身寿险 59%、危疾 28%、医疗 5%）。此后市场只能依赖保司自愿披露估算。",
        "tc": "自 2025 年 Q1 起，保監局臨時統計不再披露內地訪客（MCV）新造保費的細分數據。最後一個完整口徑是 2025 年 4 月公佈的 2024 全年數據：內地訪客新造保費 628 億港元，佔個人新單 28.6%。"
      },
      "why": {
        "sc": "这是对 IFA 影响最深的数据变化之一：MCV 是香港保险增长的核心引擎，但官方不再给细分数据。市场进入「盲飞」状态——所有 MCV 估算都成了二手解读。理解这个缺口，才能看懂为什么市场上各种「内地客保费」数字互相矛盾。",
        "tc": "這是對 IFA 影響最深的數據變化之一：MCV 是香港保險增長的核心引擎，但官方不再給細分數據。市場進入「盲飛」狀態。"
      },
      "actions": {
        "front": {
          "sc": "MCV数据盲区=引以为据时要特别标注估算口径",
          "tc": "MCV數據盲區=引以為據時要特別標注估算口徑"
        },
        "midback": {
          "sc": "保司自愿披露=唯一替代数据源",
          "tc": "保司自願披露=唯一替代數據源"
        },
        "lead": {
          "sc": "官方口径缺失=行业叙事更容易失真",
          "tc": "官方口徑缺失=行業敘事更容易失真"
        },
        "cross": {
          "sc": "跨境需求真实规模成谜",
          "tc": "跨境需求真實規模成謎"
        }
      },
      "rolesImpact": {
        "front": 4,
        "midback": 3,
        "lead": 3,
        "cross": 5
      },
      "source": {
        "sc": "保监局 · 2025年4月起",
        "lang": "sc"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "market",
        "offshore",
        "statistics"
      ],
      "tags": {
        "sc": [
          "MCV",
          "内地访客",
          "数据缺口"
        ],
        "tc": [
          "MCV",
          "內地訪客",
          "數據缺口"
        ]
      },
      "contentKind": "stats",
      "publishedAt": "2025-04-15T10:00:00+08:00",
      "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/hong-kong-insurance-market-extends-growth-run-as-data-gap-widens-583673.aspx"
    },
    {
      "id": "axa-20250409-gba-med",
      "clusterCount": 1,
      "score": 81,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T18:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "AXA安盛全面升级大湾区跨境医疗专属服务网络。",
        "tc": "AXA安盛全面升級大灣區跨境醫療專屬服務網絡。"
      },
      "summary": {
        "sc": "AXA安盛2025年4月9日全面升级粤港澳大湾区跨境医疗专属服务网络，强化跨境医疗保障能力。",
        "tc": "AXA 4月升級大灣區跨境醫療網絡"
      },
      "why": {
        "sc": "跨境医疗，也是粤港澳客户选择保司的关键差异化因素。",
        "tc": "跨境醫療，也是關鍵差異化。"
      },
      "actions": {
        "front": {
          "sc": "大湾区客户医疗覆盖优选项",
          "tc": "大灣區客戶優選"
        },
        "midback": {
          "sc": "更新跨境医疗网络对比",
          "tc": "更新跨境醫療對比"
        },
        "lead": {
          "sc": ""
        },
        "cross": {
          "sc": "大湾区客户核心卖点",
          "tc": "大灣區客戶核心賣點"
        }
      },
      "source": {
        "sc": "AXA 新闻稿",
        "tc": "AXA 新聞稿",
        "lang": "zh"
      },
      "boards": [
        "product",
        "firm",
        "offshore"
      ],
      "tags": {
        "sc": [
          "AXA",
          "大湾区",
          "跨境医疗",
          "2025"
        ],
        "tc": [
          "AXA",
          "大灣區",
          "跨境醫療",
          "2025"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2025-04-09T10:00:00+08:00",
      "originalUrl": "https://www.axa.com.hk/zh/news-room/2025",
      "sourceKey": "axa",
      "sourceTier": "insurer",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20250330-illustration-article",
      "title": {
        "sc": "保监局文章：引入演示利率上限，提升投保人保障（2025-03-30）。",
        "tc": "保監局文章：引入演示利率上限，提升投保人保障（2025-03-30）。"
      },
      "summary": {
        "sc": "保监局长期业务部主管文章阐释引入演示利率上限的政策意图：减少不切实际演示竞争，引导行业回归保障与合理预期。",
        "tc": "保監局長期業務部主管文章闡釋引入演示利率上限的政策意圖：減少不切實際演示競爭，引導行業回歸保障與合理預期。"
      },
      "why": {
        "sc": "官方叙事可用于专业沟通与培训定调。",
        "tc": "官方敘事可用於專業溝通與培訓定調。"
      },
      "actions": {
        "front": {
          "sc": "用官方意图解释「为什么演示变了」。",
          "tc": "用官方意圖解釋「為什麼演示變了」。"
        },
        "midback": {
          "sc": "培训开场引用政策逻辑。｜无直接动作。",
          "tc": "培訓開場引用政策邏輯。｜無直接動作。"
        },
        "lead": {
          "sc": "对内统一口径。",
          "tc": "對內統一口徑。"
        },
        "cross": {
          "sc": "对高净值客户强调长期价值而非演示竞赛。",
          "tc": "對高淨值客戶強調長期價值而非演示競賽。"
        }
      },
      "source": {
        "sc": "保监局演辞/文章 2025-03-30",
        "tc": "保監局演辭/文章 2025-03-30"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "演示上限",
          "政策解读"
        ],
        "tc": [
          "演示上限",
          "政策解讀"
        ]
      },
      "themes": [
        "reg",
        "par"
      ],
      "rolesImpact": {
        "front": 2,
        "midback": 3,
        "lead": 2,
        "cross": 2
      },
      "publishedAt": "2025-03-30T10:00:00+08:00",
      "score": 84,
      "verifyStatus": "verified",
      "featured": false,
      "originalUrl": "https://www.ia.org.hk/tc/infocenter/speeches_articles/20250330.html",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "product",
        "reg"
      ],
      "contentKind": "speech"
    },
    {
      "id": "fsdc-2025-insurance-hub",
      "clusterCount": 1,
      "score": 77,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T21:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "金发局报告：巩固香港全球保险枢纽 2024年经济增加值1084亿。",
        "tc": "金發局報告：鞏固香港全球保險樞紐 2024年經濟增加值1084億。"
      },
      "summary": {
        "sc": "金融发展局报告指出2024年香港保险业经济增加值达1084亿港元。保险渗透率全球最高。报告呼吁培育新一代保险专业人才、推动可持续发展和创新、巩固香港全球保险枢纽地位。一般保险市场预计2024-25年增长5.5%。",
        "tc": "金發局:保險經濟增加值1084億,滲透率全球最高"
      },
      "why": {
        "sc": "金发局，也是香港官方智库，保险业对GDP贡献的权威数据。",
        "tc": "金發局，也是官方智庫權威數據。"
      },
      "actions": {
        "front": {
          "sc": "保险业对香港经济的贡献=客户信心",
          "tc": "保險業對經濟貢獻=客戶信心"
        },
        "midback": {
          "sc": "归档行业经济数据",
          "tc": "歸檔經濟數據"
        },
        "lead": {
          "sc": "官方智库的行业定位=战略方向",
          "tc": "官方智庫行業定位"
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "金发局",
        "tc": "金發局",
        "lang": "zh"
      },
      "boards": [
        "macro"
      ],
      "tags": {
        "sc": [
          "金发局",
          "经济增加值",
          "保险枢纽"
        ],
        "tc": [
          "金發局",
          "經濟增加值",
          "保險樞紐"
        ]
      },
      "contentKind": "report",
      "publishedAt": "2025-03-27T10:00:00+08:00",
      "originalUrl": "https://www.fsdc.org.hk/en/media/",
      "sourceKey": "fsdc:insurance-hub-2025",
      "sourceTier": "media",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-2025-insurtech-initiatives",
      "clusterCount": 1,
      "score": 85,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": false,
      "ingestedAt": "2026-07-29T00:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "保监局2025年InsurTech蓝图：AI对保险业价值9.5-15.4万亿美元。",
        "tc": "保監局2025年InsurTech藍圖：AI對保險業價值9.5-15.4萬億美元。"
      },
      "summary": {
        "sc": "保监局2025年3月发布InsurTech举措报告：预测AI对全球保险业贡献9.5-15.4万亿美元，其中核保与定价约4000亿美元、AI客服与个性化约3000亿美元。GenAI在内部流程应用已达14%采用率。[EN原文]",
        "tc": "保監局:AI對保險業價值9.5-15.4萬億美元"
      },
      "why": {
        "sc": "官方对AI价值的量化，也是保险科技投资的权威背书。",
        "tc": "官方對AI價值的量化，也是權威背書。"
      },
      "actions": {
        "front": {
          "sc": "了解AI在核保和客户服务中的应用进展",
          "tc": "了解AI應用進展"
        },
        "midback": {
          "sc": "关注AI对合规流程的改造",
          "tc": "關注AI合規改造"
        },
        "lead": {
          "sc": "AI=行业效率的下一个十年核心",
          "tc": "AI=行業效率核心"
        },
        "cross": {
          "sc": "AI跨境应用=监管沙盒需两地协调",
          "tc": "AI跨境需兩地協調"
        }
      },
      "source": {
        "sc": "IA 保监局",
        "tc": "IA 保監局",
        "lang": "en"
      },
      "boards": [
        "tech"
      ],
      "tags": {
        "sc": [
          "InsurTech",
          "AI",
          "蓝图",
          "2025"
        ],
        "tc": [
          "InsurTech",
          "AI",
          "藍圖",
          "2025"
        ]
      },
      "contentKind": "report",
      "publishedAt": "2025-03-26T10:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/en/aboutus/task_force/activities_meetings/files/IA_presentation_final.pdf",
      "sourceKey": "ia",
      "sourceTier": "official",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "aia-2024-annual",
      "clusterCount": 1,
      "score": 90,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": false,
      "ingestedAt": "2026-07-28T18:30:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "AIA 2024年全年业绩：香港VONB+23% 内地客+22% 创纪录。",
        "tc": "AIA 2024年全年業績：香港VONB+23% 內地客+22% 創紀錄。"
      },
      "summary": {
        "sc": "友邦2024年全年VONB增长20%至47亿美元创纪录，OPAT每股+12%至66亿美元。香港VONB+23%(本地+24%/内地访客+22%)，代理渠道MCV VONB创2018年以来最高。[EN原文]",
        "tc": "AIA全年VONB +20%創紀錄"
      },
      "why": {
        "sc": "疫后全面复苏+跨境需求爆发，也是AIA的黄金年。",
        "tc": "疫後復甦+跨境需求爆發。"
      },
      "actions": {
        "front": {
          "sc": "2024数据=客户问AIA表现时的强力佐证",
          "tc": "客戶佐證"
        },
        "midback": {
          "sc": "归档2024年度关键数据",
          "tc": "歸檔關鍵數據"
        },
        "lead": {
          "sc": ""
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "AIA 年报",
        "tc": "AIA 年報",
        "lang": "en"
      },
      "boards": [
        "firm",
        "macro"
      ],
      "tags": {
        "sc": [
          "AIA",
          "VONB",
          "全年",
          "2024"
        ],
        "tc": [
          "AIA",
          "VONB",
          "全年",
          "2024"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2025-03-14T09:00:00+08:00",
      "originalUrl": "https://www.aia.com/en/investor-relations/",
      "sourceKey": "aia",
      "sourceTier": "insurer",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20250313-iul-circular",
      "clusterCount": 1,
      "score": 90,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": true,
      "ingestedAt": "2026-07-28T14:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "保监局与金管局联合发布IUL产品监管通函。",
        "tc": "保監局與金管局聯合發布IUL產品監管通函。"
      },
      "summary": {
        "sc": "保监局与金管局2025年3月13日联合发出通函，就面向专业投资者的指数型万用寿险(IUL)产品提出监管期望，包括适合性评估、重要事实声明、申请人声明模板等。截至2025年8月已有43个IUL产品进入市场。",
        "tc": "保監局與金管局3月13日聯合發布IUL監管通函"
      },
      "why": {
        "sc": "IUL监管框架正式确立，为IUL产品的合规销售提供法律依据。",
        "tc": "IUL監管框架正式確立。"
      },
      "actions": {
        "front": {
          "sc": "IUL销售须使用官方模板进行适合性评估",
          "tc": "IUL銷售須使用官方模板"
        },
        "midback": {
          "sc": "建立IUL产品合规销售流程",
          "tc": "建立IUL合規銷售流程"
        },
        "lead": {
          "sc": "评估IUL产品进入团队产品组合的可行性",
          "tc": "評估IUL產品可行性"
        },
        "cross": {
          "sc": "跨境客户IUL销售须满足两地监管要求",
          "tc": "跨境IUL需滿足兩地監管"
        }
      },
      "source": {
        "sc": "IA+HKMA 联合通函",
        "tc": "IA+HKMA 聯合通函",
        "lang": "zh"
      },
      "boards": [
        "regulatory",
        "product"
      ],
      "tags": {
        "sc": [
          "IUL",
          "联合通函",
          "金管局",
          "专业投资者"
        ],
        "tc": [
          "IUL",
          "聯合通函",
          "金管局",
          "專業投資者"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2025-03-13T09:00:00+08:00",
      "originalUrl": "https://brdr.hkma.gov.hk/chi/doc-ldg/docId/20250313-10-TC",
      "sourceKey": "hkma",
      "sourceTier": "official",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20250313-iul-pi",
      "title": {
        "sc": "指数型万用寿险（IUL）面向专业投资者的联合通函（2025-03-13）。",
        "tc": "指數型萬用壽險（IUL）面向專業投資者的聯合通函（2025-03-13）。"
      },
      "summary": {
        "sc": "保监局2025年3月13日联合通函就面向专业投资者的指数型万用寿险产品提出监管期望，并附重要事实声明与申请人声明模板，强调适合性与披露。",
        "tc": "保監局2025年3月13日聯合通函就面向專業投資者的指數型萬用壽險產品提出監管期望，並附重要事實聲明與申請人聲明模板，強調適合性與披露。"
      },
      "why": {
        "sc": "高净值/专业投资者产品线的文件与适合性门槛更高。",
        "tc": "高淨值/專業投資者產品線的文件與適合性門檻更高。"
      },
      "actions": {
        "front": {
          "sc": "确认客户专业投资者身份证明与声明齐全。",
          "tc": "確認客戶專業投資者身份證明與聲明齊全。"
        },
        "midback": {
          "sc": "更新 IUL 培训与 IFS 模板使用指引。｜抽检 IUL 档案完整性。",
          "tc": "更新 IUL 培訓與 IFS 模板使用指引。｜抽檢 IUL 檔案完整性。"
        },
        "lead": {
          "sc": "明确 IUL 是否纳入公司可售清单。",
          "tc": "明確 IUL 是否納入公司可售清單。"
        },
        "cross": {
          "sc": "跨境客户身份与适合性双重核验。",
          "tc": "跨境客戶身份與適合性雙重核驗。"
        }
      },
      "source": {
        "sc": "保监局联合通函 2025-03-13",
        "tc": "保監局聯合通函 2025-03-13"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "IUL",
          "专业投资者"
        ],
        "tc": [
          "IUL",
          "專業投資者"
        ]
      },
      "themes": [
        "product",
        "reg",
        "compliance",
        "offshore"
      ],
      "rolesImpact": {
        "front": 3,
        "midback": 3,
        "lead": 2,
        "cross": 3
      },
      "publishedAt": "2025-03-13T09:00:00+08:00",
      "score": 88,
      "verifyStatus": "verified",
      "featured": true,
      "originalUrl": "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/files/Circular_20250313_IUL.pdf",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "family",
        "product",
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "nfra-202502-hkmo-insurance",
      "clusterCount": 1,
      "score": 78,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T23:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "金融监管总局放宽港澳金融机构入股保险公司门槛。",
        "tc": "金融監管總局放寬港澳金融機構入股保險公司門檻。"
      },
      "summary": {
        "sc": "金融监管总局2025年2月发布通知：自2025年3月1日起，香港、澳门金融机构入股保险公司，不再执行'最近一年末总资产不低于二十亿美元'的要求。此举进一步便利港澳资本参与内地保险市场。",
        "tc": "放寬港澳金融機構入股保險公司門檻"
      },
      "why": {
        "sc": "港澳资本进入内地保险市场的通道变宽，也是双向融合信号。",
        "tc": "港澳資本入內地保險市場通道變寬。"
      },
      "actions": {
        "front": {
          "sc": "知识储备",
          "tc": "知識儲備"
        },
        "midback": {
          "sc": "关注港澳保司内地参股动态",
          "tc": "關注港澳保司參股動態"
        },
        "lead": {
          "sc": "双向融合=行业长期利好",
          "tc": "雙向融合=長期利好"
        },
        "cross": {
          "sc": "港澳保司内地布局=跨境业务的战略意义",
          "tc": "跨境業務戰略意義"
        }
      },
      "source": {
        "sc": "NFRA",
        "tc": "NFRA",
        "lang": "zh"
      },
      "boards": [
        "regulatory",
        "cross"
      ],
      "tags": {
        "sc": [
          "金融监管总局",
          "港澳",
          "入股",
          "放宽"
        ],
        "tc": [
          "金融監管總局",
          "港澳",
          "入股",
          "放寬"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2025-02-28T10:00:00+08:00",
      "originalUrl": "https://www.nfra.gov.cn/cn/view/pages/governmentDetail.html?docId=1199748&itemId=861&generaltype=1",
      "sourceKey": "nfra:hkmo-insurance-202502",
      "sourceTier": "media",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20250228-illustration-note",
      "clusterCount": 1,
      "score": 96,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": true,
      "ingestedAt": "2026-07-28T14:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "保监局就分红保单演示利率上限发出实务说明：港元6%/非港元6.5%。",
        "tc": "保監局就分紅保單演示利率上限發出實務說明：港元6%/非港元6.5%。"
      },
      "summary": {
        "sc": "保监局2025年2月28日发出实务说明(Practice Note)，确立分红保单利益说明中的演示利率上限框架：自2025年7月1日起，港元保单演示上限6.0%，非港元保单(美元/人民币等)6.5%。此为分红保单销售三项措施的第一环。",
        "tc": "演示利率上限2月28日發布，7月1日生效"
      },
      "why": {
        "sc": "演示利率上限，也是分红险行业20年来最重要的销售规则变革。",
        "tc": "演示利率上限是分紅險最重要的銷售規則變革。"
      },
      "actions": {
        "front": {
          "sc": "所有客户沟通必须使用合规演示利率",
          "tc": "所有溝通使用合規演示利率"
        },
        "midback": {
          "sc": "更新全部产品手册中的演示数据",
          "tc": "更新全部產品手冊"
        },
        "lead": {
          "sc": "团队全面培训演示利率新规",
          "tc": "團隊培訓演示利率新規"
        },
        "cross": {
          "sc": "跨境客户需清楚解释演示vs保证利率区别",
          "tc": "解釋演示vs保證利率區別"
        }
      },
      "source": {
        "sc": "IA 保监局实务说明",
        "tc": "IA 保監局實務說明",
        "lang": "en"
      },
      "boards": [
        "regulatory",
        "product"
      ],
      "tags": {
        "sc": [
          "演示利率",
          "上限",
          "6.5%",
          "实务说明",
          "2025"
        ],
        "tc": [
          "演示利率",
          "上限",
          "6.5%",
          "實務說明",
          "2025"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2025-02-28T09:00:00+08:00",
      "originalUrl": "https://brdr.hkma.gov.hk/eng/doc-ldg/docId/20250228-3-EN",
      "sourceKey": "hkma",
      "sourceTier": "official",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20250228-illustration-cap-pn",
      "title": {
        "sc": "分红保单演示利率上限应用说明（2025-02-28）。",
        "tc": "分紅保單演示利率上限應用說明（2025-02-28）。"
      },
      "summary": {
        "sc": "保监局2025年2月28日通函及附件应用说明，确立分红保单利益说明中的演示利率上限框架（后续于2025年7月生效落地），是三项分红销售措施的第一环。",
        "tc": "保監局2025年2月28日通函及附件應用說明，確立分紅保單利益說明中的演示利率上限框架（後續於2025年7月生效落地），是三項分紅銷售措施的第一環。"
      },
      "why": {
        "sc": "改写客户所见长期演示，误导投诉风险若话术不改会上升。",
        "tc": "改寫客戶所見長期演示，誤導投訴風險若話術不改會上升。"
      },
      "actions": {
        "front": {
          "sc": "保证 vs 非保证讲清楚；禁用旧演示。",
          "tc": "保證 vs 非保證講清楚；禁用舊演示。"
        },
        "midback": {
          "sc": "对比表与案例全面换新假设。｜物料与社媒旧数字清零。",
          "tc": "對比表與案例全面換新假設。｜物料與社媒舊數字清零。"
        },
        "lead": {
          "sc": "接受短期转化波动，禁止违规补转化。",
          "tc": "接受短期轉化波動，禁止違規補轉化。"
        },
        "cross": {
          "sc": "融资情景与演示同步。",
          "tc": "融資情景與演示同步。"
        }
      },
      "source": {
        "sc": "保监局应用说明 2025-02-28",
        "tc": "保監局應用說明 2025-02-28"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "演示上限",
          "应用说明"
        ],
        "tc": [
          "演示上限",
          "應用說明"
        ]
      },
      "themes": [
        "reg",
        "par",
        "product"
      ],
      "rolesImpact": {
        "front": 3,
        "midback": 3,
        "lead": 2,
        "cross": 2
      },
      "publishedAt": "2025-02-28T09:00:00+08:00",
      "effectiveAt": "2025-07-01",
      "score": 95,
      "verifyStatus": "verified",
      "featured": true,
      "originalUrl": "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/files/Practice_Note_28022025.pdf",
      "clusterCount": 3,
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": true,
      "boards": [
        "product",
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "ia-20250206-claims-mgmt",
      "title": {
        "sc": "理赔管理发现与建议（2025-02-06）。",
        "tc": "理賠管理發現與建議（2025-02-06）。"
      },
      "summary": {
        "sc": "保监局2025年2月6日通函发布理赔管理相关巡查发现与建议，推动保险人改善理赔时效、沟通与管控，间接影响中介售后预期管理。",
        "tc": "保監局2025年2月6日通函發布理賠管理相關巡查發現與建議，推動保險人改善理賠時效、溝通與管控，間接影響中介售後預期管理。"
      },
      "why": {
        "sc": "售后与理赔体验决定续期与转介口碑。",
        "tc": "售後與理賠體驗決定續期與轉介口碑。"
      },
      "actions": {
        "front": {
          "sc": "售前说明理赔文件与流程预期。",
          "tc": "售前說明理賠文件與流程預期。"
        },
        "midback": {
          "sc": "收集各保司理赔服务差异做对照。｜投诉中理赔类占比监控。",
          "tc": "收集各保司理賠服務差異做對照。｜投訴中理賠類佔比監控。"
        },
        "lead": {
          "sc": "保司评分加入理赔服务维度。",
          "tc": "保司評分加入理賠服務維度。"
        },
        "cross": {
          "sc": "跨境客户理赔协助SOP。",
          "tc": "跨境客戶理賠協助SOP。"
        }
      },
      "source": {
        "sc": "保监局规管通函 2025-02-06",
        "tc": "保監局規管通函 2025-02-06"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "理赔",
          "服务"
        ],
        "tc": [
          "理賠",
          "服務"
        ]
      },
      "themes": [
        "uw",
        "compliance",
        "reg"
      ],
      "rolesImpact": {
        "front": 2,
        "midback": 2,
        "lead": 2,
        "cross": 2
      },
      "publishedAt": "2025-02-06T09:00:00+08:00",
      "score": 79,
      "verifyStatus": "verified",
      "featured": false,
      "originalUrl": "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/files/Circular_20250206.pdf",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "ia",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "product",
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "manulife-ai-cohort-202501",
      "clusterCount": 1,
      "score": 76,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "ia",
      "title": {
        "sc": "保监局 AI Cohort Programme：宏利香港成首批核心参与保司",
        "tc": "保監局 AI Cohort Programme：宏利香港成首批核心參與保司"
      },
      "summary": {
        "sc": "2025 年 1 月，宏利香港被选为保监局 AI Cohort Programme 的核心参与保险公司。该计划聚焦将 AI 应用于核保、分销、客户服务与理赔。宏利披露的工具包括：24 小时双语 AI 客服助理、面向代理人的数据驱动销售工具、AI 核保问答助理，并与阿里云合作共建 AI 应用。",
        "tc": "2025 年 1 月，宏利香港被選為保監局 AI Cohort Programme 的核心參與保險公司。該計劃聚焦將 AI 應用於核保、分銷、客戶服務與理賠。"
      },
      "why": {
        "sc": "监管主导的 AI 试点=官方认可的 AI 应用方向。对 IFA：AI 正在进入核保与客服，前线工作方式将被重塑——理解哪些环节被 AI 接管，是未来 3 年的基本功。",
        "tc": "監管主導的 AI 試點=官方認可的 AI 應用方向。對 IFA：AI 正在進入核保與客服，前線工作方式將被重塑。"
      },
      "actions": {
        "front": {
          "sc": "AI客服/核保助理=保司服务效率的加速器",
          "tc": "AI客服/核保助理=保司服務效率的加速器"
        },
        "midback": {
          "sc": "AI治理框架=监管关注的重点",
          "tc": "AI治理框架=監管關注的重點"
        },
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 3,
        "midback": 3,
        "lead": 1,
        "cross": 1
      },
      "source": {
        "sc": "保监局 / 宏利香港 · 2025年1月",
        "lang": "sc"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "tech",
        "insurtech"
      ],
      "tags": {
        "sc": [
          "AI",
          "宏利",
          "监管试点"
        ],
        "tc": [
          "AI",
          "宏利",
          "監管試點"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2025-01-20T10:00:00+08:00",
      "originalUrl": "https://www.prnewswire.com/apac/news-releases/manulife-hong-kong-named-core-participating-insurer-in-insurance-authoritys-ai-cohort-programme-302800122.html"
    },
    {
      "id": "linkedin-2024-trends",
      "clusterCount": 1,
      "score": 73,
      "verifyStatus": "pending",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T20:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "业界回顾2024香港保险关键趋势：RBC生效/GN16修订/跨境复苏。",
        "tc": "業界回顧2024香港保險關鍵趨勢：RBC生效/GN16修訂/跨境復甦。"
      },
      "summary": {
        "sc": "LinkedIn行业分析2024年香港保险三大趋势：RBC制度7月生效(范式转换)、GN16修订启动(分红实现率披露升级)、内地访客需求全面复苏(新造保费628亿占28.6%)。[EN原文]",
        "tc": "2024三大趨勢：RBC生效/GN16修訂/跨境復甦"
      },
      "why": {
        "sc": "RBC是香港保险监管史上最大变革，2024年为起点。",
        "tc": "RBC，也是香港保險監管史上最大變革。"
      },
      "actions": {
        "front": {
          "sc": "了解RBC对产品供给的长期影响",
          "tc": "了解RBC對產品影響"
        },
        "midback": {
          "sc": "归档2024行业趋势",
          "tc": "歸檔2024趨勢"
        },
        "lead": {
          "sc": "RBC后时代的团队策略",
          "tc": "RBC後時代策略"
        },
        "cross": {
          "sc": "RBC=与国际标准对齐=跨境合作更顺畅",
          "tc": "RBC與國際對齊"
        }
      },
      "source": {
        "sc": "LinkedIn",
        "tc": "LinkedIn",
        "lang": "en"
      },
      "boards": [
        "regulatory",
        "macro"
      ],
      "tags": {
        "sc": [
          "RBC",
          "GN16",
          "跨境",
          "2024"
        ],
        "tc": [
          "RBC",
          "GN16",
          "跨境",
          "2024"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2025-01-15T10:00:00+08:00",
      "originalUrl": "https://www.linkedin.com/pulse/reviewing-key-trends-hong-kongs-insurance-industry-2024-demi-poon-b4lkc",
      "sourceKey": "linkedin:hk-trends-2024",
      "sourceTier": "media",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "nfra-cbirc-solvency2-202501",
      "clusterCount": 1,
      "score": 78,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "nfra",
      "title": {
        "sc": "金融监管总局延长偿二代二期过渡期至 2025 年底",
        "tc": "金融監管總局延長償二代二期過渡期至 2025 年底"
      },
      "summary": {
        "sc": "2025 年 1 月，金融监管总局通知延长保险公司偿付能力监管规则（Ⅱ）实施过渡期。对于因新旧规则切换对偿付能力充足率影响较大的保险公司，可在 2025 年 2 月底前完成过渡期沟通。对应香港：RBC 已于 2024 年 7 月实施——两地在偿付能力监管框架上正在趋同。",
        "tc": "2025 年 1 月，金融監管總局通知延長保險公司償付能力監管規則（Ⅱ）實施過渡期。對應香港：RBC 已於 2024 年 7 月實施——兩地在償付能力監管框架上正在趨同。"
      },
      "why": {
        "sc": "内地偿二代≈香港 RBC。两地都在从「一刀切」的偿付能力要求走向「风险为本」的资本管理。理解这一趋同，就能理解为什么内地客户越来越放心把资产放在香港——制度底层逻辑一致了。",
        "tc": "內地償二代≈香港 RBC。兩地都在從「一刀切」的償付能力要求走向「風險為本」的資本管理。"
      },
      "actions": {
        "front": {
          "sc": "两地偿付能力制度趋同=客户对港险信心增强",
          "tc": "兩地償付能力制度趨同=客戶對港險信心增強"
        },
        "midback": {
          "sc": "偿二代=内地保险公司的财务健康度标尺",
          "tc": "償二代=內地保險公司的財務健康度標尺"
        },
        "lead": {},
        "cross": {
          "sc": "偿付能力监管趋同=跨境保险制度基础在统一",
          "tc": "償付能力監管趨同=跨境保險制度基礎在統一"
        }
      },
      "rolesImpact": {
        "front": 3,
        "midback": 3,
        "lead": 3,
        "cross": 4
      },
      "source": {
        "sc": "国家金融监管总局 · 2025年1月",
        "lang": "sc"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "reg",
        "compliance"
      ],
      "tags": {
        "sc": [
          "偿二代",
          "偿付能力",
          "过渡期"
        ],
        "tc": [
          "償二代",
          "償付能力",
          "過渡期"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2025-01-15T10:00:00+08:00",
      "originalUrl": "https://www.nfra.gov.cn/cn/view/pages/governmentDetail.html?docId=1191077"
    },
    {
      "id": "axa-20250110-shengli",
      "clusterCount": 1,
      "score": 79,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T18:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "AXA安盛推出全新「盛利储蓄计划」",
        "tc": "AXA安盛推出全新「盛利儲蓄計劃」"
      },
      "summary": {
        "sc": "AXA安盛2025年1月10日推出全新「盛利储蓄计划」，为后续「盛利II」系列（2025年10月发布）奠定基础。",
        "tc": "AXA 1月推出盛利儲蓄計劃"
      },
      "why": {
        "sc": "AXA储蓄产品线年度更新起点。",
        "tc": "AXA儲蓄產品年度更新。"
      },
      "actions": {
        "front": {
          "sc": "了解产品线更新",
          "tc": "了解產品更新"
        },
        "midback": {
          "sc": "更新AXA产品库",
          "tc": "更新產品庫"
        },
        "lead": {
          "sc": ""
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "AXA 新闻稿",
        "tc": "AXA 新聞稿",
        "lang": "zh"
      },
      "boards": [
        "product",
        "firm"
      ],
      "tags": {
        "sc": [
          "AXA",
          "盛利",
          "储蓄",
          "2025"
        ],
        "tc": [
          "AXA",
          "盛利",
          "儲蓄",
          "2025"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2025-01-10T10:00:00+08:00",
      "originalUrl": "https://www.axa.com.hk/zh/news-room/2025",
      "sourceKey": "axa",
      "sourceTier": "insurer",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20241205-annual-2024",
      "clusterCount": 1,
      "score": 85,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "ia",
      "title": {
        "sc": "2024全年港险统计：总毛保费$635.2B，新造$219.8B，MCV$62.8B",
        "tc": "2024全年港險統計：總毛保費$635.2B，新造$219.8B，MCV$62.8B"
      },
      "summary": {
        "sc": "保监局发布2024年度统计：总毛保费6,352亿港元。长期业务新造保费2,198亿（+21.4%），其中分红业务1,824亿。内地访客保费628亿（+6.5%），占个人业务总新造的28.6%。",
        "tc": "保監局發布2024年度統計：總毛保費6,352億港元。長期業務新造保費2,198億（+21.4%），其中分紅業務1,824億。內地訪客保費628億（+6.5%），佔個人業務總新造的28.6%。"
      },
      "why": {
        "sc": "2024全年数据是「改革前」的最后完整画像——RBC实施半年、泰禾接管、无牌销售通函三重监管动作均在2024年拉开序幕，全年数据成为后续所有比较的基线。",
        "tc": "2024全年數據是「改革前」的最後完整畫像——RBC實施半年、泰禾接管、無牌銷售通函三重監管動作均在2024年拉開序幕，全年數據成為後續所有比較的基線。"
      },
      "actions": {
        "front": {
          "sc": "2,198亿新造保费是未来几年增长/回落比较的基准",
          "tc": "2,198億新造保費是未來幾年增長/回落比較的基準"
        },
        "midback": {
          "sc": "年度数据是合规报告和行业分析的权威依据",
          "tc": "年度數據是合規報告和行業分析的權威依據"
        },
        "lead": {
          "sc": "2024全年的渠道格局和产品结构是团队策略调整的参考",
          "tc": "2024全年的渠道格局和產品結構是團隊策略調整的參考"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 3,
        "midback": 3,
        "lead": 3,
        "cross": 2
      },
      "source": {
        "sc": "保监局 · IA",
        "lang": "zh"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "macro",
        "reg"
      ],
      "tags": {
        "sc": [
          "年度统计",
          "MCV"
        ],
        "tc": [
          "年度統計",
          "MCV"
        ]
      },
      "contentKind": "stats",
      "publishedAt": "2024-12-05T16:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/en/infocenter/press_releases/20251205.html"
    },
    {
      "id": "ia-2024-re-domiciliation",
      "clusterCount": 1,
      "score": 70,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "ia",
      "title": {
        "sc": "香港引入保险公司迁册（Re-domiciliation）制度",
        "tc": "香港引入保險公司遷冊（Re-domiciliation）制度"
      },
      "summary": {
        "sc": "香港正式实施保险公司迁册制度，允许在海外注册的保险公司将其注册地迁移至香港。此举旨在吸引更多国际保险公司将区域总部设在香港，巩固香港国际保险枢纽地位。",
        "tc": "香港正式實施保險公司遷冊制度，允許在海外註冊的保險公司將其註冊地遷移至香港。此舉旨在吸引更多國際保險公司將區域總部設在香港，鞏固香港國際保險樞紐地位。"
      },
      "why": {
        "sc": "迁册制度是香港与百慕达/新加坡竞争保险注册地的关键政策工具。对从业者来说，更多保司选择香港为注册地=更直接的监管访问=更透明的信息披露。",
        "tc": "遷冊制度是香港與百慕達/新加坡競爭保險註冊地的關鍵政策工具。對從業者來說，更多保司選擇香港為註冊地=更直接的監管訪問=更透明的信息披露。"
      },
      "actions": {
        "front": {
          "sc": "更多保司可能迁册至香港，带来新的产品和渠道机会",
          "tc": "更多保司可能遷冊至香港，帶來新的產品和渠道機會"
        },
        "midback": {
          "sc": "迁册公司的监管要求可能与本地公司不同",
          "tc": "遷冊公司的監管要求可能與本地公司不同"
        },
        "lead": {
          "sc": "迁册制度将增强香港保险市场的国际竞争力",
          "tc": "遷冊制度將增強香港保險市場的國際競爭力"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 2,
        "midback": 3,
        "lead": 3,
        "cross": 1
      },
      "source": {
        "sc": "保监局 / 财经事务及库务局",
        "lang": "zh"
      },
      "boards": [
        "reg",
        "market"
      ],
      "themes": [
        "reg",
        "offshore"
      ],
      "tags": {
        "sc": [
          "迁册",
          "制度"
        ],
        "tc": [
          "遷冊",
          "制度"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2024-12-01T10:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/en/infocenter/press_releases.html"
    },
    {
      "id": "ia-2024-revised-gn16-consult",
      "clusterCount": 1,
      "score": 79,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "ia",
      "title": {
        "sc": "保监局就修订 GN16（分红实现率披露）展开咨询",
        "tc": "保監局就修訂 GN16（分紅實現率披露）展開諮詢"
      },
      "summary": {
        "sc": "保监局就修订《承保长期保险业务指引》（GN16）展开行业咨询，拟要求保险公司以更标准化格式披露分红实现率，并扩大披露范围至更多产品类型，提升信息透明度。",
        "tc": "保監局就修訂《承保長期保險業務指引》（GN16）展開行業諮詢，擬要求保險公司以更標準化格式披露分紅實現率，並擴大披露範圍至更多產品類型，提升信息透明度。"
      },
      "why": {
        "sc": "GN16 修订是分红透明化的一步——将「分红实现率」从自愿披露升级到强制标准化披露，是后续演示利率上限的配套措施。客户从此可以用同类标准比较不同保司的分红表现。",
        "tc": "GN16 修訂是分紅透明化的關鍵一步——將「分紅實現率」從自願披露升級到強制標準化披露，是後續演示利率上限的配套措施。客戶從此可以用同類標準比較不同保司的分紅表現。"
      },
      "actions": {
        "front": {
          "sc": "分红实现率数据将成为客户沟通的核心工具",
          "tc": "分紅實現率數據將成為客戶溝通的核心工具"
        },
        "midback": {
          "sc": "需关注 GN16 披露格式变化对产品对比的影响",
          "tc": "需關注 GN16 披露格式變化對產品對比的影響"
        },
        "lead": {
          "sc": "分红透明度升级将淘汰低表现产品",
          "tc": "分紅透明度升級將淘汰低表現產品"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 4,
        "midback": 3,
        "lead": 3,
        "cross": 0
      },
      "source": {
        "sc": "保监局 · IA",
        "lang": "zh"
      },
      "boards": [
        "reg",
        "product"
      ],
      "themes": [
        "compliance",
        "par"
      ],
      "tags": {
        "sc": [
          "GN16",
          "分红实现率",
          "披露"
        ],
        "tc": [
          "GN16",
          "分紅實現率",
          "披露"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2024-11-20T15:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/en/infocenter/press_releases.html"
    },
    {
      "id": "ia-nfra-gba-motor-202411",
      "clusterCount": 1,
      "score": 80,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "ia",
      "title": {
        "sc": "保监局与金融监管总局广东局达成协议：大湾区跨境车险「等效先认」",
        "tc": "保監局與金融監管總局廣東局達成協議：大灣區跨境車險「等效先認」"
      },
      "summary": {
        "sc": "2024 年 11 月，保监局与国家金融监督管理总局广东监管局达成协议：允许香港本地保险公司签发独立的车辆自身损毁保单，附加内地规定的强制性汽车保险，即大湾区跨境车险「等效先认」安排。车主只需购买香港保单即可获内地交强险保障。",
        "tc": "2024 年 11 月，保監局與國家金融監督管理總局廣東監管局達成協議：允許香港本地保險公司簽發獨立的車輛自身損毀保單，附加內地規定的強制性汽車保險，即大灣區跨境車險「等效先認」安排。"
      },
      "why": {
        "sc": "跨境车险「等效先认」=大湾区制度衔接的标志性案例。车险虽是小事，但它是「一地保单、两地保障」的首次落地——这个模式未来可能扩展到更多险种。",
        "tc": "跨境車險「等效先認」=大灣區制度銜接的標誌性案例。它是「一地保單、兩地保障」的首次落地——這個模式未來可能擴展到更多險種。"
      },
      "actions": {
        "front": {
          "sc": "跨境车险=大湾区客户的日常刚需",
          "tc": "跨境車險=大灣區客戶的日常剛需"
        },
        "midback": {},
        "lead": {
          "sc": "等效先认=跨境保险互联互通的样板",
          "tc": "等效先認=跨境保險互聯互通的樣板"
        },
        "cross": {
          "sc": "一地保单两地保障=跨境服务模式的突破",
          "tc": "一地保單兩地保障=跨境服務模式的突破"
        }
      },
      "rolesImpact": {
        "front": 3,
        "midback": 1,
        "lead": 3,
        "cross": 4
      },
      "source": {
        "sc": "保监局 / 金融监管总局 · 2024年11月",
        "lang": "sc"
      },
      "boards": [
        "family"
      ],
      "themes": [
        "offshore",
        "cross-border",
        "reg"
      ],
      "tags": {
        "sc": [
          "跨境车险",
          "等效先认",
          "大湾区"
        ],
        "tc": [
          "跨境車險",
          "等效先認",
          "大灣區"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2024-11-15T10:00:00+08:00",
      "originalUrl": "https://www.legco.gov.hk/yr2025/chinese/counmtg/papers/cm20251022-sp104-c.pdf"
    },
    {
      "id": "ia-fintech-week-202410",
      "clusterCount": 1,
      "score": 74,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "ia",
      "title": {
        "sc": "保监局于香港金融科技周 2024 举办「保险科技论坛」",
        "tc": "保監局於香港金融科技周 2024 舉辦「保險科技論壇」"
      },
      "summary": {
        "sc": "2024 年 10 月 29 日，保监局与投资推广署合办、于香港金融科技周 2024 第二天的「保险科技论坛」揭幕，汇聚业界领袖及科技公司，分享保险科技与监管创新的最新见解。",
        "tc": "2024 年 10 月 29 日，保監局與投資推廣署合辦、於香港金融科技周 2024 第二天的「保險科技論壇」揭幕，匯聚業界領袖及科技公司，分享保險科技與監管創新的最新見解。"
      },
      "why": {
        "sc": "监管机构连续第二年举办保险科技论坛=官方对保险+科技融合的重视在制度化。对 IFA：这是了解港险科技应用方向（AI/InsurTech）的风向标事件。",
        "tc": "監管機構連續第二年舉辦保險科技論壇=官方對保險+科技融合的重視在制度化。對 IFA：這是了解港險科技應用方向的風向標事件。"
      },
      "actions": {
        "front": {
          "sc": "保险科技论坛=行业科技应用的风向标",
          "tc": "保險科技論壇=行業科技應用的風向標"
        },
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 2,
        "midback": 2,
        "lead": 2,
        "cross": 2
      },
      "source": {
        "sc": "保监局 · 2024年10月29日",
        "lang": "sc"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "tech",
        "insurtech"
      ],
      "tags": {
        "sc": [
          "金融科技周",
          "保险科技",
          "论坛"
        ],
        "tc": [
          "金融科技周",
          "保險科技",
          "論壇"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2024-10-29T10:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/sc/infocenter/press_releases/20241029.html"
    },
    {
      "id": "manulife-hiv-coverage-2024",
      "clusterCount": 1,
      "score": 70,
      "verifyStatus": "verified",
      "sourceTier": "insurer",
      "sourceKey": "manulife",
      "title": {
        "sc": "宏利香港将 HIV 阳性人士纳入个人寿险承保范围",
        "tc": "宏利香港將 HIV 陽性人士納入個人壽險承保範圍"
      },
      "summary": {
        "sc": "宏利香港宣布扩展基本个人寿险承保范围，将 HIV 阳性诊断客户纳入受保范围。这一举措是香港保险市场包容性承保的重要突破。",
        "tc": "宏利香港宣佈擴展基本個人壽險承保範圍，將 HIV 陽性診斷客戶納入受保範圍。這一舉措是香港保險市場包容性承保的重要突破。"
      },
      "why": {
        "sc": "HIV承保突破是ESG视角下的行业进步——从「拒保」到「有条件承保」的转变，意味着核保科技和医疗数据让保险公司更有信心管理风险。也代表了香港保险业的包容性标准在提升。",
        "tc": "HIV承保突破是ESG視角下的行業進步——從「拒保」到「有條件承保」的轉變，意味著核保科技和醫療數據讓保險公司更有信心管理風險。也代表了香港保險業的包容性標準在提升。"
      },
      "actions": {
        "front": {
          "sc": "新客户群体：HIV阳性人士首次可购寿险",
          "tc": "新客戶群體：HIV陽性人士首次可購壽險"
        },
        "midback": {
          "sc": "核保模型更新：需了解HIV相关承保条件",
          "tc": "核保模型更新：需了解HIV相關承保條件"
        },
        "lead": {
          "sc": "行业领先者姿态：品牌差异化价值",
          "tc": "行業領先者姿態：品牌差異化價值"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 3,
        "midback": 3,
        "lead": 1,
        "cross": 0
      },
      "source": {
        "sc": "Manulife HK · 新闻稿",
        "lang": "zh"
      },
      "boards": [
        "product",
        "insurer"
      ],
      "themes": [
        "product",
        "uw"
      ],
      "tags": {
        "sc": [
          "HIV",
          "核保",
          "宏利"
        ],
        "tc": [
          "HIV",
          "核保",
          "宏利"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2024-10-15T10:00:00+08:00",
      "originalUrl": "https://www.manulife.com.hk/en/about-us/newsroom.html"
    },
    {
      "id": "prudential-vhis-digital-202410",
      "clusterCount": 1,
      "score": 72,
      "verifyStatus": "verified",
      "sourceTier": "insurer",
      "sourceKey": "prudential",
      "title": {
        "sc": "保诚推出「自主医保计划」及综合数码服务平台",
        "tc": "保誠推出「自主醫保計劃」及綜合數碼服務平台"
      },
      "summary": {
        "sc": "2024 年 10 月前后，保诚香港推出「自主医保计划」「灵活自主医保计划」，并上线综合数码服务平台，全力支持自愿医保计划（VHIS）。健康保险产品线+数码服务双线升级。",
        "tc": "2024 年 10 月前後，保誠香港推出「自主醫保計劃」「靈活自主醫保計劃」，並上線綜合數碼服務平台，全力支持自願醫保計劃（VHIS）。"
      },
      "why": {
        "sc": "头部保司加码自愿医保=健康保障产品的竞争正在数字化。VHIS 是香港医疗险的基座产品，保诚的布局说明这个赛道的产品力和服务力都在升级。",
        "tc": "頭部保司加碼自願醫保=健康保障產品的競爭正在數字化。VHIS 是香港醫療險的基座產品。"
      },
      "actions": {
        "front": {
          "sc": "VHIS产品升级=医疗险竞争数字化",
          "tc": "VHIS產品升級=醫療險競爭數字化"
        },
        "midback": {},
        "lead": {},
        "cross": {}
      },
      "rolesImpact": {
        "front": 3,
        "midback": 1,
        "lead": 1,
        "cross": 1
      },
      "source": {
        "sc": "保诚香港 · 2024年10月",
        "lang": "sc"
      },
      "boards": [
        "product"
      ],
      "themes": [
        "product",
        "health",
        "tech"
      ],
      "tags": {
        "sc": [
          "保诚",
          "自愿医保",
          "VHIS"
        ],
        "tc": [
          "保誠",
          "自願醫保",
          "VHIS"
        ]
      },
      "contentKind": "product_notice",
      "publishedAt": "2024-10-10T10:00:00+08:00",
      "originalUrl": "https://www.prudential.com.hk/tc/about-us/newsroom/"
    },
    {
      "id": "ia-20240923-license-fee",
      "clusterCount": 1,
      "score": 72,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "ia",
      "title": {
        "sc": "保险中介人牌照费征缴启动：五年豁免期届满",
        "tc": "保險中介人牌照費徵繳啟動：五年豁免期屆滿"
      },
      "summary": {
        "sc": "2024年9月23日起，保险中介人牌照费及相关费用征缴全面启动。此前五年豁免期（2019-2024）正式终结。保监局开始向持牌经纪和代理机构收取年度牌照费。",
        "tc": "2024年9月23日起，保險中介人牌照費及相關費用徵繳全面啟動。此前五年豁免期（2019-2024）正式終結。保監局開始向持牌經紀和代理機構收取年度牌照費。"
      },
      "why": {
        "sc": "牌照费开征标志着保监局从「过渡期」进入「常态化运营」——收费意味着监管有能力独立运作，同时也推高了持牌机构的合规成本。",
        "tc": "牌照費開徵標誌著保監局從「過渡期」進入「常態化運營」——收費意味著監管有能力獨立運作，同時也推高了持牌機構的合規成本。"
      },
      "actions": {
        "front": {
          "sc": "牌照费最终会传导到从业者成本",
          "tc": "牌照費最終會傳導到從業者成本"
        },
        "midback": {
          "sc": "合规部门需将牌照费纳入年度预算",
          "tc": "合規部門需將牌照費納入年度預算"
        },
        "lead": {
          "sc": "牌照费增加机构运营成本",
          "tc": "牌照費增加機構運營成本"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 1,
        "midback": 3,
        "lead": 3,
        "cross": 0
      },
      "source": {
        "sc": "保监局 · IA",
        "lang": "zh"
      },
      "boards": [
        "reg"
      ],
      "themes": [
        "compliance",
        "career"
      ],
      "tags": {
        "sc": [
          "牌照费",
          "合规"
        ],
        "tc": [
          "牌照費",
          "合規"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2024-09-23T10:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/sc/legislative_framework/overview/gazette_notices.html"
    },
    {
      "id": "ia-2024-h1-refcheck-cross-sector",
      "clusterCount": 1,
      "score": 76,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "ia",
      "title": {
        "sc": "保监局与金管局联手推动跨行业背景查核（2025年7月实施）",
        "tc": "保監局與金管局聯手推動跨行業背景查核（2025年7月實施）"
      },
      "summary": {
        "sc": "保监局与香港金管局（HKMA）联合宣布将于2025年7月起实施跨行业背景查核安排，覆盖保险业和银行业的持牌人员。该安排旨在防止不适任人员在金融行业内部流动规避监管。",
        "tc": "保監局與香港金管局（HKMA）聯合宣佈將於2025年7月起實施跨行業背景查核安排，覆蓋保險業和銀行業的持牌人員。該安排旨在防止不適任人員在金融行業內部流動規避監管。"
      },
      "why": {
        "sc": "跨行业查核是监管「打组合拳」的典型——保险×银行联合查核意味着「在这边被罚了去那边上班」的漏洞将被堵死。对持牌人员的合规记录要求从行业级别提升到金融体系级别。",
        "tc": "跨行業查核是監管「打組合拳」的典型——保險×銀行聯合查核意味著「在這邊被罰了去那邊上班」的漏洞將被堵死。對持牌人員的合規記錄要求從行業級別提升到金融體系級別。"
      },
      "actions": {
        "front": {
          "sc": "持牌人员需确保跨行业无合规问题",
          "tc": "持牌人員需確保跨行業無合規問題"
        },
        "midback": {
          "sc": "招聘和背景调查流程需升级",
          "tc": "招聘和背景調查流程需升級"
        },
        "lead": {
          "sc": "团队招聘不能只看保险行业履历",
          "tc": "團隊招聘不能只看保險行業履歷"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 2,
        "midback": 4,
        "lead": 4,
        "cross": 0
      },
      "source": {
        "sc": "保监局 · IA / HKMA",
        "lang": "zh"
      },
      "boards": [
        "reg"
      ],
      "themes": [
        "compliance",
        "career"
      ],
      "tags": {
        "sc": [
          "背景查核",
          "HKMA",
          "跨行业"
        ],
        "tc": [
          "背景查核",
          "HKMA",
          "跨行業"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2024-09-23T10:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/en/infocenter/press_releases/20240923.html"
    },
    {
      "id": "ia-20240923-refcheck",
      "clusterCount": 1,
      "score": 82,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T14:30:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "保监局参考查核计划生效：中介人背景审查启动。",
        "tc": "保監局參考查核計劃生效：中介人背景審查啟動。"
      },
      "summary": {
        "sc": "保监局2024年9月23日启动参考查核计划。五年豁免期届满后开始征收牌照费，标志着中介人监管从过渡期进入常态化运营。",
        "tc": "保監局參考查核計劃9月23日生效"
      },
      "why": {
        "sc": "中介人合规进入新阶段，牌照管理常态化。",
        "tc": "中介人合規進入新階段。"
      },
      "actions": {
        "front": {
          "sc": "确保个人牌照信息更新",
          "tc": "確保個人牌照更新"
        },
        "midback": {
          "sc": "更新持牌人员档案",
          "tc": "更新持牌人員檔案"
        },
        "lead": {
          "sc": "团队牌照合规检查",
          "tc": "團隊牌照合規檢查"
        },
        "cross": {
          "sc": "跨境中介需满足两地牌照要求",
          "tc": "跨境中介需滿足兩地牌照"
        }
      },
      "source": {
        "sc": "IA 保监局",
        "tc": "IA 保監局",
        "lang": "zh"
      },
      "boards": [
        "regulatory",
        "compliance"
      ],
      "tags": {
        "sc": [
          "参考查核",
          "中介人",
          "牌照",
          "2024"
        ],
        "tc": [
          "參考查核",
          "中介人",
          "牌照",
          "2024"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2024-09-23T09:00:00+08:00",
      "originalUrl": "https://www.kennedyslaw.com/en/thought-leadership/article/2024/hong-kong-regulatory-insurance-update-september-2024/",
      "sourceKey": "ia:refcheck-20240923",
      "sourceTier": "media",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-2024h1-stats",
      "clusterCount": 1,
      "score": 84,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-28T14:30:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "2024上半年香港保险毛保费3109亿同比+5.1% 内地访客297亿。",
        "tc": "2024上半年香港保險毛保費3109億同比+5.1% 內地訪客297億。"
      },
      "summary": {
        "sc": "保监局公布2024上半年统计：毛保费总额3109亿港元同比+5.1%，内地访客新造保费297亿港元。保险密度亚洲第一、全球第二。",
        "tc": "2024上半年毛保費3109億，內地訪客297億"
      },
      "why": {
        "sc": "疫后复苏官方验证，内地需求持续强劲。",
        "tc": "疫後復甦官方驗證。"
      },
      "actions": {
        "front": {
          "sc": "市场数据可用于客户沟通",
          "tc": "市場數據可用於溝通"
        },
        "midback": {
          "sc": "归档历史数据做年度对比",
          "tc": "歸檔歷史數據"
        },
        "lead": {
          "sc": "数据驱动团队策略",
          "tc": "數據驅動策略"
        },
        "cross": {
          "sc": "内地访客数据=跨境营销基础",
          "tc": "內地訪客數據=跨境基礎"
        }
      },
      "source": {
        "sc": "IA/人民日报",
        "tc": "IA/人民日報",
        "lang": "zh"
      },
      "boards": [
        "regulatory",
        "macro"
      ],
      "tags": {
        "sc": [
          "H1统计",
          "保费",
          "3109亿",
          "2024"
        ],
        "tc": [
          "H1統計",
          "保費",
          "3109億",
          "2024"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2024-09-15T10:00:00+08:00",
      "originalUrl": "http://paper.people.com.cn/",
      "sourceKey": "ia:h1stats-2024",
      "sourceTier": "media",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "statecouncil-insurance-ten-202409",
      "clusterCount": 1,
      "score": 92,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "nfra",
      "title": {
        "sc": "国务院发布「国十条」：加强监管防范风险推动保险业高质量发展",
        "tc": "國務院發布「國十條」：加強監管防範風險推動保險業高質量發展"
      },
      "summary": {
        "sc": "2024 年 9 月 11 日，国务院发布《关于加强监管防范风险推动保险业高质量发展的若干意见》，业内称「国十条」。核心：① 严审批新设保险机构；② 研究完善与风险挂钩的保单兑付机制；③ 支持发展浮动收益型保险产品；④ 强化资产负债联动监管；⑤ 我国保险业未来 5-10 年的改革发展顶层设计。",
        "tc": "2024 年 9 月 11 日，國務院發布《關於加強監管防範風險推動保險業高質量發展的若干意見》。我國保險業未來 5-10 年的改革發展頂層設計。"
      },
      "why": {
        "sc": "「国十条」是内地保险监管的宪法级文件。其中「支持浮动收益型保险」一条，直接指向香港的分红险和投连险——等于官方承认了「保证收益时代结束了，要向浮动收益转型」。这是对港险模式的最大官方背书。",
        "tc": "「國十條」是內地保險監管的憲法級文件。「支持浮動收益型保險」=官方承認保證收益時代結束，向浮動收益轉型——這是對港險模式的最大官方背書。"
      },
      "actions": {
        "front": {
          "sc": "国十条=内地保险从「保证」向「浮动」的制度信号",
          "tc": "國十條=內地保險從「保證」向「浮動」的制度信號"
        },
        "midback": {
          "sc": "保单兑付机制完善=行业安全性提升=客户信心增强",
          "tc": "保單兌付機制完善=行業安全性提升=客戶信心增強"
        },
        "lead": {
          "sc": "顶层定调=保险业转型方向明确",
          "tc": "頂層定調=保險業轉型方向明確"
        },
        "cross": {
          "sc": "内地浮动收益化+香港成熟分红体系=跨境互补格局",
          "tc": "內地浮動收益化+香港成熟分紅體系=跨境互補格局"
        }
      },
      "rolesImpact": {
        "front": 5,
        "midback": 4,
        "lead": 5,
        "cross": 5
      },
      "source": {
        "sc": "国务院 · 2024年9月11日",
        "lang": "sc"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "reg",
        "offshore"
      ],
      "tags": {
        "sc": [
          "国十条",
          "保险法",
          "高质量发展"
        ],
        "tc": [
          "國十條",
          "保險法",
          "高質量發展"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2024-09-11T10:00:00+08:00",
      "originalUrl": "https://www.gov.cn/zhengce/content/202409/content_6972814.htm"
    },
    {
      "id": "sunlife-2024-fwd-pension",
      "clusterCount": 1,
      "score": 82,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": true,
      "ingestedAt": "2026-07-28T18:30:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "Sun Life永明收购FWD香港养老金业务 强积金+46亿港元。",
        "tc": "Sun Life永明收購FWD香港養老金業務 強積金+46億港元。"
      },
      "summary": {
        "sc": "Sun Life 2024年收购FWD香港养老金业务及施罗德退休金业务，合计新增46亿港元强积金规模，巩固其香港第三大强积金服务商地位。[EN原文]",
        "tc": "永明收購FWD養老金業務"
      },
      "why": {
        "sc": "永明强积金规模跃升，也是退休市场话语权增强。",
        "tc": "永明強積金規模躍升。"
      },
      "actions": {
        "front": {
          "sc": "在职客户强积金选择增多",
          "tc": "強積金選擇增多"
        },
        "midback": {
          "sc": "更新永明强积金数据",
          "tc": "更新強積金數據"
        },
        "lead": {
          "sc": ""
        },
        "cross": {
          "sc": ""
        }
      },
      "source": {
        "sc": "Sun Life新闻稿",
        "tc": "Sun Life新聞稿",
        "lang": "en"
      },
      "boards": [
        "firm"
      ],
      "tags": {
        "sc": [
          "永明",
          "FWD",
          "养老金",
          "收购",
          "2024"
        ],
        "tc": [
          "永明",
          "FWD",
          "養老金",
          "收購",
          "2024"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2024-09-10T10:00:00+08:00",
      "originalUrl": "https://www.prnewswire.com/news-releases/sun-life-financial-to-acquire-pension-business-of-fwd-hong-kong-589039111.html",
      "sourceKey": "sunlife:fwd-pension-2024",
      "sourceTier": "insurer",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20240830-h1-2024-stats",
      "clusterCount": 1,
      "score": 83,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "ia",
      "title": {
        "sc": "2024上半年港险统计：长期业务新造保费$115.6B，内地访客$29.7B",
        "tc": "2024上半年港險統計：長期業務新造保費$115.6B，內地訪客$29.7B"
      },
      "summary": {
        "sc": "保监局发布2024上半年临时统计：长期业务新造保费1,156亿港元（同比+12.3%），内地访客新造保费297亿港元。非相连个人业务占主导（1,080亿）。",
        "tc": "保監局發布2024上半年臨時統計：長期業務新造保費1,156億港元（同比+12.3%），內地訪客新造保費297億港元。非相連個人業務佔主導（1,080億）。"
      },
      "why": {
        "sc": "这是RBC实施后的第一份完整半年报——对比Q1数据（791亿），Q2明显放缓（365亿），首次验证了RBC对市场的冷却效应。",
        "tc": "這是RBC實施後的第一份完整半年報——對比Q1數據（791億），Q2明顯放緩（365億），首次驗證了RBC對市場的冷卻效應。"
      },
      "actions": {
        "front": {
          "sc": "Q2放缓信号说明RBC对市场确有影响",
          "tc": "Q2放緩信號說明RBC對市場確有影響"
        },
        "midback": {
          "sc": "H1数据可作为客户沟通的行业背景材料",
          "tc": "H1數據可作為客戶溝通的行業背景材料"
        },
        "lead": {
          "sc": "下半年市场预期需以Q2趋势为基准调整",
          "tc": "下半年市場預期需以Q2趨勢為基準調整"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 3,
        "midback": 2,
        "lead": 3,
        "cross": 1
      },
      "source": {
        "sc": "保监局 · IA",
        "lang": "zh"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "macro",
        "reg"
      ],
      "tags": {
        "sc": [
          "统计",
          "半年报"
        ],
        "tc": [
          "統計",
          "半年報"
        ]
      },
      "contentKind": "stats",
      "publishedAt": "2024-08-30T16:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/sc/infocenter/press_releases/20240830.html"
    },
    {
      "id": "ia-2024-crossborder",
      "clusterCount": 1,
      "score": 87,
      "verifyStatus": "verified",
      "featured": false,
      "evergreen": true,
      "ingestedAt": "2026-07-28T14:30:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "保监局与廉政公署联合打击跨境无牌销售保单。",
        "tc": "保監局與廉政公署聯合打擊跨境無牌銷售保單。"
      },
      "summary": {
        "sc": "保监局与廉政公署2024年联合行动打击向内地客户跨境无牌销售保单，拘捕一名保险经纪。标志着两地监管对地下保单零容忍。香港保险销售全流程须在港完成。",
        "tc": "保監局與廉政公署聯合打擊跨境無牌銷售"
      },
      "why": {
        "sc": "跨境销售合规红线明确：全流程须在港完成，违规可被刑事追究。",
        "tc": "跨境銷售紅線明確。"
      },
      "actions": {
        "front": {
          "sc": "100%确保签单流程在港完成",
          "tc": "簽單流程100%在港完成"
        },
        "midback": {
          "sc": "更新跨境销售合规手册",
          "tc": "更新跨境合規手冊"
        },
        "lead": {
          "sc": "团队重申跨境合规底线",
          "tc": "重申跨境合規底線"
        },
        "cross": {
          "sc": "跨境客户合规签单全流程",
          "tc": "跨境客戶合規流程"
        }
      },
      "source": {
        "sc": "IA/廉政公署",
        "tc": "IA/廉政公署",
        "lang": "zh"
      },
      "boards": [
        "regulatory",
        "compliance",
        "cross"
      ],
      "tags": {
        "sc": [
          "跨境",
          "无牌销售",
          "廉政公署",
          "地下保单"
        ],
        "tc": [
          "跨境",
          "無牌銷售",
          "廉政公署",
          "地下保單"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2024-08-20T14:00:00+08:00",
      "originalUrl": "https://www.xincai.com/article/nhzqptf9387534",
      "sourceKey": "xincai",
      "sourceTier": "media",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "nfra-rate-cut-202408",
      "clusterCount": 1,
      "score": 90,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "nfra",
      "title": {
        "sc": "预定利率首次全面下调：传统型 2.5%、分红型 2.0%、万能型 1.5%",
        "tc": "預定利率首次全面下調：傳統型 2.5%、分紅型 2.0%、萬能型 1.5%"
      },
      "summary": {
        "sc": "2024 年 8 月，金融监管总局下发《关于健全人身保险产品定价机制的通知》：9 月 1 日起普通型预定利率从 3.0% 降至 2.5%；10 月 1 日起分红型从 2.5% 降至 2.0%，万能型最低保证利率从 2.0% 降至 1.5%。同时首次提出建立预定利率动态调整机制。这是内地保险史上首次全面下调预定利率，也是「报行合一」从银保向全渠道推广的起点。",
        "tc": "2024 年 8 月，金融監管總局下發《關於健全人身保險產品定價機制的通知》：普通型 3.0%→2.5%，分紅型 2.5%→2.0%，萬能型 2.0%→1.5%。這是內地保險史上首次全面下調預定利率。"
      },
      "why": {
        "sc": "这是内地保险利率的「历史转折点」。3.0→2.5 看似只差 0.5 个百分点，但对一份 30 年保单的现值影响巨大。对 IFA：2024 年 9 月之后，内地客户开始真正感受到「保证收益不够了」，跨境配置需求从此加速爆发。",
        "tc": "這是內地保險利率的「歷史轉折點」。3.0→2.5 看似只差 0.5 個百分點，但對一份 30 年保單的現值影響巨大。跨境配置需求從此加速爆發。"
      },
      "actions": {
        "front": {
          "sc": "内地保证收益加速下行→港险MCV需求结构性增长",
          "tc": "內地保證收益加速下行→港險MCV需求結構性增長"
        },
        "midback": {},
        "lead": {
          "sc": "预定利率下调是2024-2026港险跨境爆发的底层推手",
          "tc": "預定利率下調是2024-2026港險跨境爆發的底層推手"
        },
        "cross": {
          "sc": "内地降息+香港分红=跨境配置的公式越来越清晰",
          "tc": "內地降息+香港分紅=跨境配置的公式越來越清晰"
        }
      },
      "rolesImpact": {
        "front": 5,
        "midback": 3,
        "lead": 5,
        "cross": 5
      },
      "source": {
        "sc": "国家金融监管总局 · 2024年8月",
        "lang": "sc"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "reg",
        "product",
        "offshore"
      ],
      "tags": {
        "sc": [
          "预定利率",
          "报行合一",
          "利率下调"
        ],
        "tc": [
          "預定利率",
          "報行合一",
          "利率下調"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2024-08-02T10:00:00+08:00",
      "originalUrl": "https://www.nfra.gov.cn/cn/view/pages/ItemDetail.html?docId=1175200"
    },
    {
      "id": "nfra-2024-crossborder-no",
      "clusterCount": 1,
      "score": 88,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": true,
      "ingestedAt": "2026-07-28T23:00:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "金融监管总局：现阶段跨境保险通试点时机尚不成熟。",
        "tc": "金融監管總局：現階段跨境保險通試點時機尚不成熟。"
      },
      "summary": {
        "sc": "金融监管总局2024年8月公开答复：由于内地与港澳保险市场在法律体系、监管制度、产品设计等方面存在较大差异，市场风险易交叉传染，现阶段直接开展跨境保险通试点的时机尚不成熟。同时表示正推进大湾区保险服务中心建设。",
        "tc": "金融監管總局:跨境保險通試點時機不成熟"
      },
      "why": {
        "sc": "这是内地对跨境保险的最高级别官方表态，也是所有IFA必须知道的合规底线。",
        "tc": "內地對跨境保險最高級別官方表態。"
      },
      "actions": {
        "front": {
          "sc": "所有销售流程必须100%在香港境内完成",
          "tc": "銷售流程100%在港完成"
        },
        "midback": {
          "sc": "归档跨境政策信号",
          "tc": "歸檔跨境政策信號"
        },
        "lead": {
          "sc": "跨境保险通=无时限搁置，团队策略勿押注",
          "tc": "團隊策略勿押注"
        },
        "cross": {
          "sc": "大湾区保险服务中心=可能的合规突破口",
          "tc": "大灣區服務中心=可能突破口"
        }
      },
      "source": {
        "sc": "NFRA/人民日报",
        "tc": "NFRA/人民日報",
        "lang": "zh"
      },
      "boards": [
        "regulatory",
        "cross"
      ],
      "tags": {
        "sc": [
          "跨境保险通",
          "金融监管总局",
          "粤港澳",
          "2024"
        ],
        "tc": [
          "跨境保險通",
          "金融監管總局",
          "粵港澳",
          "2024"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2024-08-01T10:00:00+08:00",
      "originalUrl": "http://paper.people.com.cn/zgjjzk/pc/content/202411/15/content_30046103.html",
      "sourceKey": "nfra:crossborder-no-202408",
      "sourceTier": "media",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20240726-tahoe-life",
      "clusterCount": 1,
      "score": 88,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "ia",
      "title": {
        "sc": "保监局委任经理全面接管泰禾人寿——香港保险史上首次",
        "tc": "保監局委任經理全面接管泰禾人壽——香港保險史上首次"
      },
      "summary": {
        "sc": "保监局根据《保险业条例》第35(2)(b)条，委任德勤两位经理全面接管泰禾人寿所有事务及财产。这是香港保险监管史上首次由监管机构直接接管保险公司。百慕达金管局配合行动。",
        "tc": "保監局根據《保險業條例》第35(2)(b)條，委任德勤兩位經理全面接管泰禾人壽所有事務及財產。這是香港保險監管史上首次由監管機構直接接管保險公司。百慕達金管局配合行動。"
      },
      "why": {
        "sc": "泰禾接管是香港保险监管的分水岭事件——RBC实施不到一个月，监管就挥出第一记重拳。它向全行业传递了明确信号：资本不达标，监管有能力、有意愿直接介入。",
        "tc": "泰禾接管是香港保險監管的分水嶺事件——RBC實施不到一個月，監管就揮出第一記重拳。它向全行業傳遞了明確信號：資本不達標，監管有能力、有意願直接介入。"
      },
      "actions": {
        "front": {
          "sc": "泰禾客户需关注保单托管状态",
          "tc": "泰禾客戶需關注保單託管狀態"
        },
        "midback": {
          "sc": "RBC下保司偿付能力评估标准被实战检验",
          "tc": "RBC下保司償付能力評估標準被實戰檢驗"
        },
        "lead": {
          "sc": "监管从「管规则」进入「管执行」，团队风控意识需升级",
          "tc": "監管從「管規則」進入「管執行」，團隊風控意識需升級"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 2,
        "midback": 4,
        "lead": 4,
        "cross": 0
      },
      "source": {
        "sc": "保监局 · IA",
        "lang": "zh"
      },
      "boards": [
        "reg",
        "insurer"
      ],
      "themes": [
        "compliance",
        "firm"
      ],
      "tags": {
        "sc": [
          "接管",
          "RBC",
          "泰禾"
        ],
        "tc": [
          "接管",
          "RBC",
          "泰禾"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2024-07-26T18:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/en/infocenter/press_releases/20240726.html"
    },
    {
      "id": "ctflife-20240723-rebrand",
      "clusterCount": 1,
      "score": 87,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": true,
      "ingestedAt": "2026-07-28T18:30:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "FTLife正式更名为周大福人寿(CTF Life)。",
        "tc": "FTLife正式更名為周大福人壽(CTF Life)。"
      },
      "summary": {
        "sc": "FTLife保险2024年7月23日正式更名为周大福人寿保险有限公司(CTF Life)。全新品牌「CTF Life · Circle」同步推出。RBC资本比率升至289%远超监管要求。",
        "tc": "FTLife 7月23日正式更名為周大福人壽"
      },
      "why": {
        "sc": "周大福品牌进入保险业，也是市场格局重塑，原九鼎/富通翻篇。",
        "tc": "周大福品牌進入保險業，也是市場重塑。"
      },
      "actions": {
        "front": {
          "sc": "向客户说明CTF Life背景与周大福品牌实力",
          "tc": "向客戶說明品牌背景"
        },
        "midback": {
          "sc": "更新保司档案：FTLife变为CTF Life",
          "tc": "更新保司檔案"
        },
        "lead": {
          "sc": "周大福品牌背书=合作信心提升",
          "tc": "品牌背書=合作信心"
        },
        "cross": {
          "sc": "周大福品牌在内地客户中认知度优势",
          "tc": "內地品牌認知度"
        }
      },
      "source": {
        "sc": "CTF Life/ACN",
        "tc": "CTF Life/ACN",
        "lang": "zh"
      },
      "boards": [
        "firm"
      ],
      "tags": {
        "sc": [
          "周大福",
          "CTF",
          "更名",
          "品牌",
          "2024"
        ],
        "tc": [
          "周大福",
          "CTF",
          "更名",
          "品牌",
          "2024"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2024-07-23T10:00:00+08:00",
      "originalUrl": "https://www.acnnewswire.com/press-release/english/91884/",
      "sourceKey": "ctflife:rebrand-20240723",
      "sourceTier": "media",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "ia-20240701-rbc-live",
      "clusterCount": 1,
      "score": 98,
      "verifyStatus": "verified",
      "featured": true,
      "evergreen": true,
      "ingestedAt": "2026-07-28T14:30:00+08:00",
      "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
      },
      "title": {
        "sc": "香港风险为本资本制度(RBC)正式生效。",
        "tc": "香港風險為本資本制度(RBC)正式生效。"
      },
      "summary": {
        "sc": "2024年7月1日，香港保险业风险为本资本制度正式生效。标志性里程碑：以模块化方式评估保司风险，与国际标准(IAIS)对齐。涵盖三大支柱：定量资本要求、管治与风险管理、公开披露。",
        "tc": "2024年7月1日RBC制度正式生效"
      },
      "why": {
        "sc": "RBC，也是香港保险监管体系最大单次升级，影响所有保司资本管理。",
        "tc": "RBC，也是香港保險監管史上最大升級。"
      },
      "actions": {
        "front": {
          "sc": "了解RBC对保司偿付能力的提升含义",
          "tc": "了解RBC對保司影響"
        },
        "midback": {
          "sc": "更新保司评估框架纳入RBC指标",
          "tc": "更新評估框架"
        },
        "lead": {
          "sc": "RBC合规=保司合作基本门槛",
          "tc": "RBC合規=合作門檻"
        },
        "cross": {
          "sc": "RBC与国际标准对齐=跨境合作更顺畅",
          "tc": "RBC與國際對齊"
        }
      },
      "source": {
        "sc": "财库局/IA",
        "tc": "財庫局/IA",
        "lang": "zh"
      },
      "boards": [
        "regulatory"
      ],
      "tags": {
        "sc": [
          "RBC",
          "风险为本",
          "资本制度",
          "2024"
        ],
        "tc": [
          "RBC",
          "風險為本",
          "資本制度",
          "2024"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2024-07-01T09:00:00+08:00",
      "originalUrl": "https://www.fstb.gov.hk/fsb/en/business/policy_highlights/insurance-industry.html",
      "sourceKey": "govhk",
      "sourceTier": "official",
      "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 0,
        "cross": 0
      },
      "themes": [
        "market"
      ]
    },
    {
      "id": "henley-migration-2024",
      "clusterCount": 1,
      "score": 72,
      "verifyStatus": "verified",
      "sourceTier": "pro",
      "sourceKey": "henley",
      "title": {
        "sc": "Henley 2024 财富迁移报告：中国内地百万富翁流出量全球第一",
        "tc": "Henley 2024 財富遷移報告：中國內地百萬富翁流出量全球第一"
      },
      "summary": {
        "sc": "Henley & Partners 发布《2024 私人财富迁移报告》：预计 2024 年全球 12.8 万高净值人士将迁移，中国内地以 15,200 人的净流出量居全球首位。香港是主要目的地之一，受益于 CIES 重启和家办政策利好。",
        "tc": "Henley & Partners 發布《2024 私人財富遷移報告》：預計 2024 年全球 12.8 萬高淨值人士將遷移，中國內地以 15,200 人的淨流出量居全球首位。香港是主要目的地之一，受益於 CIES 重啟和家辦政策利好。"
      },
      "why": {
        "sc": "15,200 内地百万富翁净流出——等于每年有一个中等城市规模的高净值人群在寻找新的财富目的地。香港 CIES + 家办政策正是对这一趋势的制度性回应。",
        "tc": "15,200 內地百萬富翁淨流出——等於每年有一個中等城市規模的高淨值人群在尋找新的財富目的地。香港 CIES + 家辦政策正是對這一趨勢的制度性回應。"
      },
      "actions": {
        "front": {
          "sc": "内地高净值流出潮=跨境保险的持续增长源",
          "tc": "內地高淨值流出潮=跨境保險的持續增長源"
        },
        "midback": {},
        "lead": {
          "sc": "15,200人/年的增量市场=战略布局不嫌早",
          "tc": "15,200人/年的增量市場=戰略佈局不嫌早"
        },
        "cross": {
          "sc": "高净值迁移数据是身份规划业务的基础",
          "tc": "高淨值遷移數據是身份規劃業務的基礎"
        }
      },
      "rolesImpact": {
        "front": 4,
        "midback": 1,
        "lead": 4,
        "cross": 5
      },
      "source": {
        "sc": "Henley & Partners",
        "lang": "zh"
      },
      "boards": [
        "family"
      ],
      "themes": [
        "offshore",
        "identity-planning"
      ],
      "tags": {
        "sc": [
          "财富迁移",
          "Henley",
          "身份规划"
        ],
        "tc": [
          "財富遷移",
          "Henley",
          "身份規劃"
        ]
      },
      "contentKind": "stats",
      "publishedAt": "2024-06-18T10:00:00+08:00",
      "originalUrl": "https://www.henleyglobal.com/publications/henley-private-wealth-migration-report-2024"
    },
    {
      "id": "ocorian-hk-wealth-magnet-2024",
      "clusterCount": 1,
      "score": 74,
      "verifyStatus": "verified",
      "sourceTier": "pro",
      "sourceKey": "ocorian",
      "title": {
        "sc": "Ocorian 报告：2024年香港跨境财富猛增 2,310 亿美元，追平瑞士",
        "tc": "Ocorian 報告：2024年香港跨境財富猛增 2,310 億美元，追平瑞士"
      },
      "summary": {
        "sc": "Ocorian 发布《How Hong Kong became a global wealth magnet》报告：2024 年香港跨境财富管理规模增加 2,310 亿美元，总规模达到 2.7 万亿美元，与瑞士并列全球最大跨境财富中心。私人银行及私人财富管理 AUM 突破 10 万亿港元（同比+15%）。",
        "tc": "Ocorian 發布《How Hong Kong became a global wealth magnet》報告：2024 年香港跨境財富管理規模增加 2,310 億美元，總規模達到 2.7 萬億美元，與瑞士並列全球最大跨境財富中心。私人銀行及私人財富管理 AUM 突破 10 萬億港元（同比+15%）。"
      },
      "why": {
        "sc": "2,310 亿美元的年增量 = 香港跨境财富赛道不是在「增长」，是在「爆发」。2024 追平瑞士，2026 超越瑞士（BCG 数据），两年三级跳的背后是整个家办生态的制度红利。",
        "tc": "2,310 億美元的年增量 = 香港跨境財富賽道不是在「增長」，是在「爆發」。2024 追平瑞士，2026 超越瑞士（BCG 數據），兩年三級跳的背後是整個家辦生態的制度紅利。"
      },
      "actions": {
        "front": {
          "sc": "2.7万亿跨境财富=大额保险和信托的庞大市场",
          "tc": "2.7萬億跨境財富=大額保險和信託的龐大市場"
        },
        "midback": {},
        "lead": {
          "sc": "跨境财富增速是团队战略定投的最强信号",
          "tc": "跨境財富增速是團隊戰略定投的最強信號"
        },
        "cross": {
          "sc": "追平瑞士=香港跨境财富赛道的里程碑节点",
          "tc": "追平瑞士=香港跨境財富賽道的里程碑節點"
        }
      },
      "rolesImpact": {
        "front": 4,
        "midback": 1,
        "lead": 5,
        "cross": 5
      },
      "source": {
        "sc": "Ocorian",
        "lang": "zh"
      },
      "boards": [
        "family",
        "market"
      ],
      "themes": [
        "offshore",
        "global-allocation"
      ],
      "tags": {
        "sc": [
          "跨境财富",
          "全球第二",
          "Ocorian"
        ],
        "tc": [
          "跨境財富",
          "全球第二",
          "Ocorian"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2024-06-15T10:00:00+08:00",
      "originalUrl": "https://www.ocorian.com/knowledge-hub/insights/how-hong-kong-became-global-wealth-magnet"
    },
    {
      "id": "ia-20240614-gl34-segregation",
      "clusterCount": 1,
      "score": 78,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "ia",
      "title": {
        "sc": "GL34《就分红业务设立与维持基金的指引》宪报刊登",
        "tc": "GL34《就分紅業務設立與維持基金的指引》憲報刊登"
      },
      "summary": {
        "sc": "保监局在宪报刊登指引34（GL34），要求保险公司就分红业务设立独立基金，明确资产隔离和利润分配规则，进一步加强分红保单持有人的权益保障。",
        "tc": "保監局在憲報刊登指引34（GL34），要求保險公司就分紅業務設立獨立基金，明確資產隔離和利潤分配規則，進一步加強分紅保單持有人的權益保障。"
      },
      "why": {
        "sc": "GL34是分红保单监管的基石性文件——「独立基金」要求意味着保司不能再在分红/非分红之间随意调拨资产。它是后续演示上限+佣金递延的规则前提。",
        "tc": "GL34是分紅保單監管的基石性文件——「獨立基金」要求意味著保司不能再在分紅/非分紅之間隨意調撥資產。它是後續演示上限+佣金遞延的規則前提。"
      },
      "actions": {
        "front": {
          "sc": "分红产品的底层资产安全性有了制度保障",
          "tc": "分紅產品的底層資產安全性有了制度保障"
        },
        "midback": {
          "sc": "需理解GL34对分红实现率计算的影响",
          "tc": "需理解GL34對分紅實現率計算的影響"
        },
        "lead": {
          "sc": "GL34是客户沟通分红安全性的权威引述",
          "tc": "GL34是客戶溝通分紅安全性的權威引述"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 3,
        "midback": 4,
        "lead": 2,
        "cross": 0
      },
      "source": {
        "sc": "保监局 · IA Gazette",
        "lang": "zh"
      },
      "boards": [
        "reg",
        "product"
      ],
      "themes": [
        "compliance",
        "par"
      ],
      "tags": {
        "sc": [
          "GL34",
          "分红",
          "基金隔离"
        ],
        "tc": [
          "GL34",
          "分紅",
          "基金隔離"
        ]
      },
      "contentKind": "circular",
      "publishedAt": "2024-06-14T10:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/sc/legislative_framework/overview/gazette_notices.html"
    },
    {
      "id": "ia-20240612-unlicensed-mcv",
      "clusterCount": 1,
      "score": 85,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "ia",
      "title": {
        "sc": "保监局发通函：打击向内地访客无牌销售长期保单的不合规模式",
        "tc": "保監局發通函：打擊向內地訪客無牌銷售長期保單的不合規模式"
      },
      "summary": {
        "sc": "保监局发出通函，针对保险经纪公司向内地访客无牌销售长期保单的不合规业务模式，要求授权保险公司采取纠正行动。标志着对跨境销售灰色地带的正式收紧。",
        "tc": "保監局發出通函，針對保險經紀公司向內地訪客無牌銷售長期保單的不合規業務模式，要求授權保險公司採取糾正行動。標誌著對跨境銷售灰色地帶的正式收緊。"
      },
      "why": {
        "sc": "这是2024年最重要的合规事件之一——在此通函之前，经纪向内地客户「代签单」是行业公开秘密。通函是后来转介费上限+佣金递延+跨境查核三级监管链条的起点。",
        "tc": "這是2024年最重要的合規事件之一——在此通函之前，經紀向內地客戶「代簽單」是行業公開秘密。通函是後來轉介費上限+佣金遞延+跨境查核三級監管鏈條的起點。"
      },
      "actions": {
        "front": {
          "sc": "此后「内地签单」面临直接合规风险",
          "tc": "此後「內地簽單」面臨直接合規風險"
        },
        "midback": {
          "sc": "合规部门需更新跨境销售流程",
          "tc": "合規部門需更新跨境銷售流程"
        },
        "lead": {
          "sc": "团队需培训更新合规红线",
          "tc": "團隊需培訓更新合規紅線"
        },
        "cross": {
          "sc": "跨境销售的合规框架将从这一刻开始重构",
          "tc": "跨境銷售的合規框架將從這一刻開始重構"
        }
      },
      "rolesImpact": {
        "front": 4,
        "midback": 5,
        "lead": 4,
        "cross": 4
      },
      "source": {
        "sc": "保监局 · IA",
        "lang": "zh"
      },
      "boards": [
        "reg",
        "market"
      ],
      "themes": [
        "compliance",
        "offshore"
      ],
      "tags": {
        "sc": [
          "跨境销售",
          "合规",
          "通函"
        ],
        "tc": [
          "跨境銷售",
          "合規",
          "通函"
        ]
      },
      "contentKind": "circular",
      "publishedAt": "2024-06-12T10:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/files/20240612_Circular.pdf"
    },
    {
      "id": "ia-20240531-q1-2024-stats",
      "clusterCount": 1,
      "score": 82,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "ia",
      "title": {
        "sc": "2024年Q1临时统计：长期业务新造保费$79.1B，同比+14.6%",
        "tc": "2024年Q1臨時統計：長期業務新造保費$79.1B，同比+14.6%"
      },
      "summary": {
        "sc": "保监局发布2024年Q1临时统计。长期业务新造保费791亿港元（同比+14.6%），其中非相连个人业务743亿（+18.2%）。内地访客新造保费156亿港元。",
        "tc": "保監局發布2024年Q1臨時統計。長期業務新造保費791億港元（同比+14.6%），其中非相連個人業務743億（+18.2%）。內地訪客新造保費156億港元。"
      },
      "why": {
        "sc": "2024年Q1是RBC实施前的最后一个完整季度——也是内地访客贡献（156亿）的高水位基线。后续佣金/演示/转介三重改革都在此基础上落地。",
        "tc": "2024年Q1是RBC實施前的最後一個完整季度——也是內地訪客貢獻（156億）的高水位基線。後續佣金/演示/轉介三重改革都在此基礎上落地。"
      },
      "actions": {
        "front": {
          "sc": "内地访客保费占比是后续所有监管收紧的参考锚点",
          "tc": "內地訪客保費佔比是後續所有監管收緊的參考錨點"
        },
        "midback": {
          "sc": "季度统计是合规报告的重要参考基准",
          "tc": "季度統計是合規報告的重要參考基準"
        },
        "lead": {
          "sc": "Q1高基数意味着后续Q2-Q4的增长压力",
          "tc": "Q1高基數意味著後續Q2-Q4的增長壓力"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 3,
        "midback": 3,
        "lead": 3,
        "cross": 1
      },
      "source": {
        "sc": "保监局 · IA",
        "lang": "zh"
      },
      "boards": [
        "market",
        "reg"
      ],
      "themes": [
        "macro",
        "reg"
      ],
      "tags": {
        "sc": [
          "统计",
          "内地访客"
        ],
        "tc": [
          "統計",
          "內地訪客"
        ]
      },
      "contentKind": "stats",
      "publishedAt": "2024-05-31T16:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/sc/infocenter/press_releases/20240531_1.html"
    },
    {
      "id": "ia-20240522-referral-fee-circular",
      "clusterCount": 1,
      "score": 87,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "ia",
      "title": {
        "sc": "保监局发通函：对转介费设立监管基准（不超佣金总额 50%）",
        "tc": "保監局發通函：對轉介費設立監管基準（不超佣金總額 50%）"
      },
      "summary": {
        "sc": "保监局发布通函，首次对保险经纪转介费设定监管基准：转介人收取的费用不应超过持牌经纪公司从保险公司获得的相关佣金总额的50%。同时要求保险公司加强转介安排的管控和书面披露。",
        "tc": "保監局發布通函，首次對保險經紀轉介費設定監管基準：轉介人收取的費用不應超過持牌經紀公司從保險公司獲得的相關佣金總額的50%。同時要求保險公司加強轉介安排的管控和書面披露。"
      },
      "why": {
        "sc": "这是「佣金三件套」（转介上限+首年70%+递延5年）的第一件——2024年5月吹风、2025年9月正式生效。它直接改变了经纪渠道的商业模式：靠转介费堆量的模式将难以为继，专业价值成为唯一护城河。",
        "tc": "這是「佣金三件套」（轉介上限+首年70%+遞延5年）的第一件——2024年5月吹風、2025年9月正式生效。它直接改變了經紀渠道的商業模式：靠轉介費堆量的模式將難以為繼，專業價值成為唯一護城河。"
      },
      "actions": {
        "front": {
          "sc": "高转介费模式的经纪面临最大冲击",
          "tc": "高轉介費模式的經紀面臨最大衝擊"
        },
        "midback": {
          "sc": "需更新转介协议模板和披露流程",
          "tc": "需更新轉介協議模板和披露流程"
        },
        "lead": {
          "sc": "渠道商业模式将被迫升级",
          "tc": "渠道商業模式將被迫升級"
        },
        "cross": {}
      },
      "rolesImpact": {
        "front": 4,
        "midback": 5,
        "lead": 4,
        "cross": 0
      },
      "source": {
        "sc": "保监局 · IA",
        "lang": "zh"
      },
      "boards": [
        "reg",
        "market"
      ],
      "themes": [
        "compliance",
        "channel"
      ],
      "tags": {
        "sc": [
          "转介费",
          "通函",
          "佣金改革"
        ],
        "tc": [
          "轉介費",
          "通函",
          "佣金改革"
        ]
      },
      "contentKind": "circular",
      "publishedAt": "2024-05-22T14:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/files/20240522_Circular.pdf"
    },
    {
      "id": "chubb-cies-ilas-2024",
      "clusterCount": 1,
      "score": 71,
      "verifyStatus": "verified",
      "sourceTier": "insurer",
      "sourceKey": "chubb",
      "title": {
        "sc": "安达人寿推出 CIES 合资格投资相连寿险计划",
        "tc": "安達人壽推出 CIES 合資格投資相連壽險計劃"
      },
      "summary": {
        "sc": "安达人寿（Chubb Life HK）推出专为 CIES 申请人设计的合资格投资相连寿险计划（ILAS），提供多元化基金选择和 SFC+IA 双重监管保障。这是保司直接对接 CIES 投资需求的产品创新，将保险嵌入移民投资架构。",
        "tc": "安達人壽（Chubb Life HK）推出專為 CIES 申請人設計的合資格投資相連壽險計劃（ILAS），提供多元化基金選擇和 SFC+IA 雙重監管保障。這是保司直接對接 CIES 投資需求的产品創新，將保險嵌入移民投資架構。"
      },
      "why": {
        "sc": "ILAS 是保险产品对接 CIES 的标准答案——投连险既满足 2,700 万金融资产要求，又提供人寿保障。Chubb 的这步棋说明：CIES 不只是家办的蛋糕，保司也在切。",
        "tc": "ILAS 是保險產品對接 CIES 的標準答案——投連險既滿足 2,700 萬金融資產要求，又提供人壽保障。Chubb 的這步棋說明：CIES 不只是家辦的蛋糕，保司也在切。"
      },
      "actions": {
        "front": {
          "sc": "CIES客户的投连险=资产配置+身份规划一步到位",
          "tc": "CIES客戶的投連險=資產配置+身份規劃一步到位"
        },
        "midback": {
          "sc": "ILAS产品需同时满足SFC和IA双重合规",
          "tc": "ILAS產品需同時滿足SFC和IA雙重合規"
        },
        "lead": {
          "sc": "CIES产品线是保司新的增长极",
          "tc": "CIES產品線是保司新的增長極"
        },
        "cross": {
          "sc": "ILAS是保险嵌入跨境投资架构的范本",
          "tc": "ILAS是保險嵌入跨境投資架構的範本"
        }
      },
      "rolesImpact": {
        "front": 4,
        "midback": 3,
        "lead": 3,
        "cross": 4
      },
      "source": {
        "sc": "Chubb Life HK",
        "lang": "zh"
      },
      "boards": [
        "product",
        "family"
      ],
      "themes": [
        "product",
        "offshore",
        "identity-planning"
      ],
      "tags": {
        "sc": [
          "CIES",
          "投连险",
          "Chubb"
        ],
        "tc": [
          "CIES",
          "投連險",
          "Chubb"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2024-05-01T10:00:00+08:00",
      "originalUrl": "https://www.chubb.com/hk-en/personal/cias.html"
    },
    {
      "id": "ia-cashier-order-circular-202404",
      "clusterCount": 1,
      "score": 74,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "ia",
      "title": {
        "sc": "保监局发通函：加强本票缴付保费的管控措施",
        "tc": "保監局發通函：加強本票繳付保費的管控措施"
      },
      "summary": {
        "sc": "2024 年 4 月，保监局在实地查察后发现保险公司对于以本票缴付保费的管控措施大致无效、容易被规避，故发出通函，要求缓减涉及第三方支付相关的风险，加强本票缴费管控。",
        "tc": "2024 年 4 月，保監局在實地查察後發現保險公司對於以本票繳付保費的管控措施大致無效，故發出通函，要求緩減涉及第三方支付相關的風險。"
      },
      "why": {
        "sc": "本票=大额保单跨境缴费的主要工具之一。监管盯上本票管控，说明第三方代缴/代付模式正在被收紧——这是跨境保单缴费合规的又一个关注点。",
        "tc": "本票=大額保單跨境繳費的主要工具之一。監管盯上本票管控，說明第三方代繳/代付模式正在被收緊。"
      },
      "actions": {
        "front": {
          "sc": "本票缴费管控=大额单操作合规要点",
          "tc": "本票繳費管控=大額單操作合規要點"
        },
        "midback": {
          "sc": "第三方支付风险=尽调必查项",
          "tc": "第三方支付風險=盡調必查項"
        },
        "lead": {},
        "cross": {
          "sc": "跨境缴费渠道=合规架构设计的一部分",
          "tc": "跨境繳費渠道=合規架構設計的一部分"
        }
      },
      "rolesImpact": {
        "front": 3,
        "midback": 4,
        "lead": 1,
        "cross": 3
      },
      "source": {
        "sc": "保监局 · 2024年4月",
        "lang": "sc"
      },
      "boards": [
        "reg"
      ],
      "themes": [
        "compliance",
        "reg"
      ],
      "tags": {
        "sc": [
          "本票",
          "第三方支付",
          "通函"
        ],
        "tc": [
          "本票",
          "第三方支付",
          "通函"
        ]
      },
      "contentKind": "circular",
      "publishedAt": "2024-04-15T10:00:00+08:00",
      "originalUrl": "https://www.legco.gov.hk/yr2025/chinese/counmtg/papers/cm20251022-sp104-c.pdf"
    },
    {
      "id": "ia-icac-joint-action-202404",
      "clusterCount": 1,
      "score": 82,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "ia",
      "title": {
        "sc": "保监局与廉政公署首次联合行动：打击向内地旅客无牌销售保单",
        "tc": "保監局與廉政公署首次聯合行動：打擊向內地旅客無牌銷售保單"
      },
      "summary": {
        "sc": "2024 年 4 月，保监局与廉政公署采取首次联合执法行动，打击怀疑向内地旅客无牌销售保单的不合规模式。后续通函指出这类模式的共通点，并阐明授权保险公司和持牌经纪采用转介业务模式须遵守的原则。",
        "tc": "2024 年 4 月，保監局與廉政公署採取首次聯合執法行動，打擊懷疑向內地旅客無牌銷售保單的不合規模式。後續通函闡明轉介業務模式須遵守的原則。"
      },
      "why": {
        "sc": "ICAC 进场=无牌销售从「监管问题」升级为「执法问题」。对 IFA：跨境转介业务从此有了明确红线——这是理解后来所有转介费规管的起点。",
        "tc": "ICAC 進場=無牌銷售從「監管問題」升級為「執法問題」。對 IFA：跨境轉介業務從此有了明確紅線。"
      },
      "actions": {
        "front": {
          "sc": "跨境转介红线=合规经营的生命线",
          "tc": "跨境轉介紅線=合規經營的生命線"
        },
        "midback": {
          "sc": "联合执法=转介模式合规审查加严",
          "tc": "聯合執法=轉介模式合規審查加嚴"
        },
        "lead": {},
        "cross": {
          "sc": "内地客销售合规=跨境业务的第一课",
          "tc": "內地客銷售合規=跨境業務的第一課"
        }
      },
      "rolesImpact": {
        "front": 4,
        "midback": 4,
        "lead": 2,
        "cross": 4
      },
      "source": {
        "sc": "保监局 · 2024年4月",
        "lang": "sc"
      },
      "boards": [
        "reg"
      ],
      "themes": [
        "reg",
        "compliance",
        "offshore"
      ],
      "tags": {
        "sc": [
          "廉政公署",
          "无牌销售",
          "联合行动"
        ],
        "tc": [
          "廉政公署",
          "無牌銷售",
          "聯合行動"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2024-04-10T10:00:00+08:00",
      "originalUrl": "https://www.ia.org.hk/tc/infocenter/files/IA_AR23-24_Synopsis_tc.pdf"
    },
    {
      "id": "fstb-fo-policy-202403",
      "clusterCount": 1,
      "score": 82,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "govhk",
      "title": {
        "sc": "港府发布《家族办公室政策宣言》：八大措施打造家办枢纽",
        "tc": "港府發布《家族辦公室政策宣言》：八大措施打造家辦樞紐"
      },
      "summary": {
        "sc": "财经事务及库务局发布《有关香港发展家族办公室业务的政策宣言》，提出八大政策措施：包括新的 CIES 计划、税务宽减、设立 FamilyOfficeHK 服务窗口、成立财富继承学院、推广艺术品存储设施、发展慈善中心等。标志港府将家办作为核心金融战略。",
        "tc": "財經事務及庫務局發布《有關香港發展家族辦公室業務的政策宣言》，提出八大政策措施：包括新的 CIES 計劃、稅務寬減、設立 FamilyOfficeHK 服務窗口、成立財富繼承學院、推廣藝術品存儲設施、發展慈善中心等。標誌港府將家辦作為核心金融戰略。"
      },
      "why": {
        "sc": "这是香港家办生态的「宪法性文件」——八大措施 = 港府对家办的全套诚意。CIES/税务优惠/服务窗口三管齐下，信号再明确不过：香港要从「保险销售港」升级为「财富管理枢纽」。",
        "tc": "這是香港家辦生態的「憲法性文件」——八大措施 = 港府對家辦的全套誠意。CIES/稅務優惠/服務窗口三管齊下，信號再明確不過：香港要從「保險銷售港」升級為「財富管理樞紐」。"
      },
      "actions": {
        "front": {
          "sc": "家办客户现在有政策背书的「整套服务」，不只是产品",
          "tc": "家辦客戶現在有政策背書的「整套服務」，不只是產品"
        },
        "midback": {
          "sc": "税务宽减政策是合规操作的重要依据",
          "tc": "稅務寬減政策是合規操作的重要依據"
        },
        "lead": {
          "sc": "八大措施 = 家办赛道正式获得政府级战略支撑",
          "tc": "八大措施 = 家辦賽道正式獲得政府級戰略支撐"
        },
        "cross": {
          "sc": "CIES/税务/服务窗口 = 跨境家办的三根支柱",
          "tc": "CIES/稅務/服務窗口 = 跨境家辦的三根支柱"
        }
      },
      "rolesImpact": {
        "front": 4,
        "midback": 3,
        "lead": 5,
        "cross": 5
      },
      "source": {
        "sc": "FSTB · GovHK",
        "lang": "zh"
      },
      "boards": [
        "family"
      ],
      "themes": [
        "family-office",
        "offshore",
        "corporate-service"
      ],
      "tags": {
        "sc": [
          "家办政策",
          "FSTB",
          "八大措施"
        ],
        "tc": [
          "家辦政策",
          "FSTB",
          "八大措施"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2024-03-24T10:00:00+08:00",
      "originalUrl": "https://www.fstb.gov.hk/en/business-family-office-policy-statement.html"
    },
    {
      "id": "ia-gl33-ils-2024",
      "clusterCount": 1,
      "score": 76,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "ia",
      "title": {
        "sc": "保监局公布指引 33：保险相连证券（ILS）特定目的业务授权框架",
        "tc": "保監局公佈指引 33：保險相連證券（ILS）特定目的業務授權框架"
      },
      "summary": {
        "sc": "保监局公布《申请授权经营特定目的业务的指引》（指引 33），标志着香港保险相连证券（ILS）制度进程的重要一步。框架允许保险公司通过特定目的载体发行 ILS（如巨灾债券），提升香港作为再保险及 ILS 枢纽的地位。",
        "tc": "保監局公佈《申請授權經營特定目的業務的指引》（指引 33），標誌著香港保險相連證券（ILS）制度進程的重要一步。框架允許保險公司通過特定目的載體發行 ILS（如巨災債券）。"
      },
      "why": {
        "sc": "ILS/巨灾债券=保险资本市场化的工具。指引 33 让香港在这个赛道上有了制度基础——对 IFA 是间接影响，但对理解「香港=风险管理中心」的完整拼图很重要。",
        "tc": "ILS/巨災債券=保險資本市場化的工具。指引 33 讓香港在這個賽道上有了制度基礎。"
      },
      "actions": {
        "front": {},
        "midback": {},
        "lead": {
          "sc": "ILS制度落地=风险管理中心拼图完整",
          "tc": "ILS制度落地=風險管理中心拼圖完整"
        },
        "cross": {
          "sc": "保险+资本市场=香港的独特枢纽价值",
          "tc": "保險+資本市場=香港的獨特樞紐價值"
        }
      },
      "rolesImpact": {
        "front": 1,
        "midback": 2,
        "lead": 3,
        "cross": 3
      },
      "source": {
        "sc": "保监局 · 2024年",
        "lang": "sc"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "reg",
        "macro",
        "capital-market"
      ],
      "tags": {
        "sc": [
          "保险相连证券",
          "ILS",
          "指引33"
        ],
        "tc": [
          "保險相連證券",
          "ILS",
          "指引33"
        ]
      },
      "contentKind": "circular",
      "publishedAt": "2024-03-20T10:00:00+08:00",
      "originalUrl": "https://www.kingandwood.com/hk/zh/insights/latest-thinking/rise-of-the-hk-ils-market-insurance-authority-publishes-gl-on-application-to-carry-on-spb.html"
    },
    {
      "id": "nfra-insurer-rating-202403",
      "clusterCount": 1,
      "score": 74,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "nfra",
      "title": {
        "sc": "金融监管总局发布《人身保险公司监管评级办法》：六大维度+百余指标",
        "tc": "金融監管總局發佈《人身保險公司監管評級辦法》：六大維度+百餘指標"
      },
      "summary": {
        "sc": "2024 年 3 月，金融监管总局推出人身险公司监管评级办法，通过公司治理、业务经营、资金运用、偿付能力等六大维度和百余评价指标，对险企进行全面风险评级和持续动态监测。对应香港：D-SII 框架于 2025 年 10 月推出——两地在「分层监管」上的节奏高度相似。",
        "tc": "2024 年 3 月，金融監管總局推出人身險公司監管評級辦法，通過六大維度和百餘評價指標對險企進行全面風險評級。對應香港：D-SII 框架於 2025 年 10 月推出——兩地在「分層監管」上的節奏高度相似。"
      },
      "why": {
        "sc": "内地给保司打分→香港给保司 D-SII 标签→同一套逻辑：风险大的保司要多备资本。IFA 需要知道：你推荐的公司，在两个监管体系下评级如何？两者越趋于一致，客户越放心。",
        "tc": "內地給保司打分→香港給保司 D-SII 標籤→同一套邏輯。IFA 需要知道：你推薦的公司，在兩個監管體系下評級如何？"
      },
      "actions": {
        "front": {
          "sc": "保司评级=客户选择保司的参考标尺",
          "tc": "保司評級=客戶選擇保司的參考標尺"
        },
        "midback": {
          "sc": "监管评级制度=保司合规的新压力维度",
          "tc": "監管評級制度=保司合規的新壓力維度"
        },
        "lead": {},
        "cross": {
          "sc": "两地风险评级体系趋同=跨境监管合作的基础",
          "tc": "兩地風險評級體系趨同=跨境監管合作的基礎"
        }
      },
      "rolesImpact": {
        "front": 3,
        "midback": 3,
        "lead": 3,
        "cross": 3
      },
      "source": {
        "sc": "国家金融监管总局 · 2024年3月",
        "lang": "sc"
      },
      "boards": [
        "market"
      ],
      "themes": [
        "reg",
        "firm"
      ],
      "tags": {
        "sc": [
          "监管评级",
          "人身险",
          "六大维度"
        ],
        "tc": [
          "監管評級",
          "人身險",
          "六大維度"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2024-03-18T10:00:00+08:00",
      "originalUrl": "https://www.nfra.gov.cn/cn/view/pages/ItemDetail.html?docId=1157468"
    },
    {
      "id": "newcies-20240301-launch",
      "clusterCount": 1,
      "score": 85,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "govhk",
      "title": {
        "sc": "新CIES正式启动：投资3,000万港元可获香港居留权",
        "tc": "新CIES正式啟動：投資3,000萬港元可獲香港居留權"
      },
      "summary": {
        "sc": "2024年3月1日，香港特区政府正式推出「新资本投资者入境计划（New CIES）」。合资格申请人须投资最少 3,000 万港元于获许资产（其中 2,700 万为金融资产/非住宅房地产，300 万投入 CIES 投资组合）。获批申请人可携配偶及子女来港，7 年后可申请永久居留。",
        "tc": "2024年3月1日，香港特區政府正式推出「新資本投資者入境計劃（New CIES）」。合資格申請人須投資最少 3,000 萬港元於獲許資產（其中 2,700 萬為金融資產/非住宅房地產，300 萬投入 CIES 投資組合）。獲批申請人可攜配偶及子女來港，7 年後可申請永久居留。"
      },
      "why": {
        "sc": "CIES 是香港跨境财富管理的「制度基座」。3,000 万门槛 + 7年居留路径 = 每笔申请背后都是一个高净值家庭的全面财富规划需求（保险/信托/教育/置业）。2024年3月是这条赛道的起点。",
        "tc": "CIES 是香港跨境財富管理的「制度基座」。3,000 萬門檻 + 7年居留路徑 = 每筆申請背後都是一個高淨值家庭的全面財富規劃需求（保險/信託/教育/置業）。2024年3月是這條賽道的起點。"
      },
      "actions": {
        "front": {
          "sc": "CIES客户是高净值保险/投连险的精准受众",
          "tc": "CIES客戶是高淨值保險/投連險的精準受眾"
        },
        "midback": {
          "sc": "CIES合规要求涉及净资产审查和投资持有规则",
          "tc": "CIES合規要求涉及淨資產審查和投資持有規則"
        },
        "lead": {
          "sc": "CIES是跨境家办业务的核心获客渠道",
          "tc": "CIES是跨境家辦業務的核心獲客渠道"
        },
        "cross": {
          "sc": "CIES是身份规划+财富管理的交叉入口",
          "tc": "CIES是身份規劃+財富管理的交叉入口"
        }
      },
      "rolesImpact": {
        "front": 4,
        "midback": 3,
        "lead": 5,
        "cross": 5
      },
      "source": {
        "sc": "新CIES办公室 · GovHK",
        "lang": "zh"
      },
      "boards": [
        "family"
      ],
      "themes": [
        "offshore",
        "family-office",
        "identity-planning"
      ],
      "tags": {
        "sc": [
          "CIES",
          "投资移民",
          "家办"
        ],
        "tc": [
          "CIES",
          "投資移民",
          "家辦"
        ]
      },
      "contentKind": "press",
      "publishedAt": "2024-03-01T10:00:00+08:00",
      "originalUrl": "https://www.newcies.gov.hk/zh-cn/resources/news/new-capital-investment-entrant-scheme-opens-for-application-from-march-1/"
    },
    {
      "id": "hsbc-life-250m-record-20240228",
      "clusterCount": 1,
      "score": 80,
      "verifyStatus": "verified",
      "sourceTier": "insurer",
      "sourceKey": "hsbc",
      "title": {
        "sc": "HSBC Life 签出 $2.5 亿美元保单，创吉尼斯世界纪录",
        "tc": "HSBC Life 簽出 $2.5 億美元保單，創健力士世界紀錄"
      },
      "summary": {
        "sc": "HSBC Life 在香港签发一张 2.5 亿美元终身寿险保单，获吉尼斯世界纪录认证为史上最高价值寿险保单。保单由个人客户购买，全额承保。被视为香港作为亚洲财富管理中心的重要里程碑。",
        "tc": "HSBC Life 在香港簽發一張 2.5 億美元終身壽險保單，獲健力士世界紀錄認證為史上最高價值壽險保單。保單由個人客戶購買，全額承保。被視為香港作為亞洲財富管理中心的重要里程碑。"
      },
      "why": {
        "sc": "2.5亿美金一张保单——这不只是新闻，是香港超高净值保险市场成熟的实证。2026年宏利以3亿美元打破此纪录，但HSBC 2024年先开的这条赛道，证明了「保险=传承工具」在亚洲已被最富有的客户用真金白银投票。",
        "tc": "2.5億美金一張保單——這不只是新聞，是香港超高淨值保險市場成熟的實證。2026年宏利以3億美元打破此紀錄，但HSBC 2024年先開的這條賽道，證明了「保險=傳承工具」在亞洲已被最富有的客戶用真金白銀投票。"
      },
      "actions": {
        "front": {
          "sc": "高净值客户用保单做传承的标杆案例，可用于客户对话",
          "tc": "高淨值客戶用保單做傳承的標桿案例，可用於客戶對話"
        },
        "midback": {
          "sc": "超高额保单的反洗钱和KYC流程值得参考",
          "tc": "超高額保單的反洗錢和KYC流程值得參考"
        },
        "lead": {
          "sc": "香港作为亚洲财富传承中心的品牌价值提升",
          "tc": "香港作為亞洲財富傳承中心的品牌價值提升"
        },
        "cross": {
          "sc": "2.5亿保单本身就是跨境资产配置的最强广告",
          "tc": "2.5億保單本身就是跨境資產配置的最強廣告"
        }
      },
      "rolesImpact": {
        "front": 4,
        "midback": 2,
        "lead": 3,
        "cross": 4
      },
      "source": {
        "sc": "HSBC / Guinness / SCMP",
        "lang": "zh"
      },
      "boards": [
        "product",
        "family"
      ],
      "themes": [
        "product",
        "family-office"
      ],
      "tags": {
        "sc": [
          "吉尼斯纪录",
          "超高净值",
          "终身寿"
        ],
        "tc": [
          "健力士紀錄",
          "超高淨值",
          "終身壽"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2024-02-28T10:00:00+08:00",
      "originalUrl": "https://www.hsbc.com/news-and-views/news/hsbc-news-archive/our-record-breaking-life-insurance-policy"
    },
    {
      "id": "safe-crossborder-wmc-202402",
      "clusterCount": 1,
      "score": 75,
      "verifyStatus": "verified",
      "sourceTier": "official",
      "sourceKey": "safe",
      "title": {
        "sc": "跨境理财通 2025 升级：南向通个人额度提高至 300 万元",
        "tc": "跨境理財通 2025 升級：南向通個人額度提高至 300 萬元"
      },
      "summary": {
        "sc": "2025 年，跨境理财通（Wealth Management Connect）完成 2.0 升级。南向通个人投资者额度从 100 万元提高至 300 万元，可投资产品范围扩大至中低风险基金和债券。粤港澳大湾区居民可通过闭环式资金管道投资香港理财产品，包括保险相连产品。",
        "tc": "2025 年，跨境理財通（Wealth Management Connect）完成 2.0 升級。南向通個人投資者額度從 100 萬元提高至 300 萬元，可投資產品範圍擴大至中低風險基金和債券。"
      },
      "why": {
        "sc": "理财通是大湾区居民合法购买香港金融产品的最直接通道。300 万额度虽然不大，但它是「可以合法出去」的信号。对 IFA：理财通的每一次扩容，都等于一个新客户入口的开放。",
        "tc": "理財通是大灣區居民合法購買香港金融產品的最直接通道。每一次擴容，都等於一個新客戶入口的開放。"
      },
      "actions": {
        "front": {
          "sc": "理财通=大湾区客户的合法资产出境通道",
          "tc": "理財通=大灣區客戶的合法資產出境通道"
        },
        "midback": {},
        "lead": {
          "sc": "跨境理财通扩大=香港财富管理的增量来源",
          "tc": "跨境理財通擴大=香港財富管理的增量來源"
        },
        "cross": {
          "sc": "理财通+CIES+QDII=跨境资产配置三大通道",
          "tc": "理財通+CIES+QDII=跨境資產配置三大通道"
        }
      },
      "rolesImpact": {
        "front": 4,
        "midback": 1,
        "lead": 3,
        "cross": 4
      },
      "source": {
        "sc": "中国人民银行 · 2024年2月",
        "lang": "sc"
      },
      "boards": [
        "family"
      ],
      "themes": [
        "offshore",
        "global-allocation"
      ],
      "tags": {
        "sc": [
          "理财通",
          "大湾区",
          "南向通"
        ],
        "tc": [
          "理財通",
          "大灣區",
          "南向通"
        ]
      },
      "contentKind": "news",
      "publishedAt": "2024-02-26T10:00:00+08:00",
      "originalUrl": "http://www.safe.gov.cn/big5/big5/www.safe.gov.cn/shenzhen/2024/0308/1746.html"
    }
  ],
  "calendar": [
    {
      "date": "2026-11-13",
      "title": {
        "sc": "Asian Insurance Forum 2026",
        "tc": "Asian Insurance Forum 2026"
      },
      "theme": "firm",
      "itemId": "aif-2026-save-the-date"
    },
    {
      "date": "2026-07-31",
      "title": {
        "sc": "CPD 2025/26 学时完成截止（评核期）",
        "tc": "CPD 2025/26 學時完成截止（評核期）"
      },
      "theme": "career",
      "itemId": "ia-20260331-cpd-reporting"
    },
    {
      "date": "2026-07-10",
      "title": {
        "sc": "演示上限检讨机制释义",
        "tc": "演示上限檢討機制釋義"
      },
      "theme": "par",
      "itemId": "ia-20260710-illustration-review"
    },
    {
      "date": "2026-07-01",
      "title": {
        "sc": "跨行业背景查核安排生效（保监局叙述）",
        "tc": "跨行業背景查核安排生效（保監局敘述）"
      },
      "theme": "compliance",
      "itemId": "ia-20260513-cross-refcheck"
    },
    {
      "date": "2026-06-30",
      "title": {
        "sc": "GL34 公司政策节生效",
        "tc": "GL34 公司政策節生效"
      },
      "theme": "reg",
      "itemId": "ia-gl34-20260331"
    },
    {
      "date": "2026-03-31",
      "title": {
        "sc": "GL34 修订主体生效",
        "tc": "GL34 修訂主體生效"
      },
      "theme": "reg",
      "itemId": "ia-20260331-gn16-revised"
    },
    {
      "date": "2026-01-01",
      "title": {
        "sc": "分红保单佣金分摊要求生效",
        "tc": "分紅保單佣金分攤要求生效"
      },
      "theme": "compliance",
      "itemId": "ia-commission-20260101"
    },
    {
      "date": "2025-10-01",
      "title": {
        "sc": "转介费50%基准遵从",
        "tc": "轉介費50%基準遵從"
      },
      "theme": "compliance",
      "itemId": "ia-20250901-referral-fee"
    },
    {
      "date": "2025-09-01",
      "title": {
        "sc": "转介费上限规则生效（不超过佣金总额 50%）",
        "tc": "轉介費上限規則生效（不超過佣金總額 50%）"
      },
      "theme": "compliance",
      "itemId": "ia-20250901-referral-fee"
    },
    {
      "date": "2025-08-01",
      "title": {
        "sc": "经纪公司RO强制CPD生效",
        "tc": "經紀公司RO強制CPD生效"
      },
      "theme": "career"
    },
    {
      "date": "2025-07-01",
      "title": {
        "sc": "演示利率上限生效",
        "tc": "演示利率上限生效"
      },
      "theme": "par",
      "itemId": "ia-20250228-illustration-cap-pn"
    },
    {
      "date": "2025-02-28",
      "title": {
        "sc": "分红演示利率上限通函发布（2025.07 生效）",
        "tc": "分紅演示利率上限通函發布（2025.07 生效）"
      },
      "theme": "par",
      "itemId": "ia-20250228-illustration-cap-pn"
    },
    {
      "date": "2024-09-23",
      "title": {
        "sc": "跨行业背景查核安排方案咨询",
        "tc": "跨行業背景查核安排方案諮詢"
      },
      "theme": "compliance",
      "itemId": "ia-20240923-refcheck"
    },
    {
      "date": "2024-09-15",
      "title": {
        "sc": "2024上半年香港保险市场统计发布",
        "tc": "2024上半年香港保險市場統計發布"
      },
      "theme": "macro",
      "itemId": "ia-2024h1-stats"
    },
    {
      "date": "2024-09-10",
      "title": {
        "sc": "永明金融收购富卫香港公积金业务",
        "tc": "永明金融收購富衛香港公積金業務"
      },
      "theme": "firm",
      "itemId": "sunlife-2024-fwd-pension"
    },
    {
      "date": "2024-08-20",
      "title": {
        "sc": "跨境保险销售红线明确（内地居民赴港投保合规框架）",
        "tc": "跨境保險銷售紅線明確（內地居民赴港投保合規框架）"
      },
      "theme": "compliance",
      "itemId": "ia-2024-crossborder"
    },
    {
      "date": "2024-08-01",
      "title": {
        "sc": "金融监管总局答复跨境保险通：时机尚不成熟",
        "tc": "金融監管總局答覆跨境保險通：時機尚不成熟"
      },
      "theme": "offshore",
      "itemId": "nfra-2024-crossborder-no"
    },
    {
      "date": "2024-07-23",
      "title": {
        "sc": "周大福人寿更名（原富通保险）",
        "tc": "周大福人壽更名（原富通保險）"
      },
      "theme": "firm",
      "itemId": "ctflife-20240723-rebrand"
    },
    {
      "date": "2024-07-01",
      "title": {
        "sc": "RBC 风险为本资本制度正式实施",
        "tc": "RBC 風險為本資本制度正式實施"
      },
      "theme": "reg",
      "itemId": "ia-20240701-rbc-live"
    }
  ],
  "daily": {
    "date": "2026-07-26",
    "sections": [
      {
        "title": {
          "sc": "监管与规则",
          "tc": "監管與規則"
        },
        "itemIds": [
          "ia-public-disclosure-2026",
          "hkma-complaints-20260724",
          "ia-20260716-ashk-ifoa",
          "ia-20260715-sales-practices",
          "ia-licence-20260630"
        ]
      },
      {
        "title": {
          "sc": "产品与披露",
          "tc": "產品與披露"
        },
        "itemIds": [
          "ia-20260716-ashk-ifoa",
          "ia-20260710-illustration-review",
          "ia-20260703-rfyc"
        ]
      },
      {
        "title": {
          "sc": "合规与操守",
          "tc": "合規與操守"
        },
        "itemIds": [
          "hkma-complaints-20260724",
          "ia-20260715-sales-practices",
          "ia-20260712-speech"
        ]
      },
      {
        "title": {
          "sc": "市场与机构",
          "tc": "市場與機構"
        },
        "itemIds": [
          "aif-2026-save-the-date",
          "ia-public-disclosure-2026",
          "ia-q1-2026-stats",
          "ia-20260716-ashk-ifoa"
        ]
      }
    ]
  },
  "evergreen": [
    "ia-20260712-speech",
    "ia-20260513-cross-refcheck",
    "ia-20250901-referral-fee",
    "ia-commission-20260101",
    "ia-20250228-illustration-cap-pn",
    "ia-gl34-20260331",
    "ia-20260508-rbc-conclusions"
  ],
  "digests": {
    "daily": [
      {
        "key": "2026-07-30",
        "label": {
          "sc": "2026-07-30",
          "tc": "2026-07-30"
        },
        "itemCount": 2,
        "itemIds": [
          "mof-rmb-bonds-cmu-jul30",
          "hkma-fed-response-jul30"
        ]
      },
      {
        "key": "2026-07-29",
        "label": {
          "sc": "2026-07-29",
          "tc": "2026-07-29"
        },
        "itemCount": 5,
        "itemIds": [
          "hkma-cmu-network-jul29",
          "bowtie-202607-100m",
          "hk-202607-mainland-scrutiny",
          "ia-20260730-sales-misconduct",
          "ai-25pct-insurance-jobs-202607"
        ]
      },
      {
        "key": "2026-07-28",
        "label": {
          "sc": "2026-07-28",
          "tc": "2026-07-28"
        },
        "itemCount": 7,
        "itemIds": [
          "picc-202607-re",
          "ia-ai-cohort-new-insurers-jul",
          "cgs-202607-hk-crackdown",
          "ratings-2026-consolidated",
          "continuum-hk-gm-202607",
          "hk-fraud-payments-lag-202607",
          "howden-hk-ceo-20260701"
        ]
      },
      {
        "key": "2026-07-27",
        "label": {
          "sc": "2026-07-27",
          "tc": "2026-07-27"
        },
        "itemCount": 3,
        "itemIds": [
          "hkma-quantum-whitepaper-jul27",
          "prudential-usd500k-legacy-202607",
          "apac-insurers-emergedebt-202607"
        ]
      },
      {
        "key": "2026-07-26",
        "label": {
          "sc": "2026-07-26",
          "tc": "2026-07-26"
        },
        "itemCount": 3,
        "itemIds": [
          "sunlife-privatewealth-202607",
          "manulife-asian-care-survey-2026",
          "aif-2026-save-the-date"
        ]
      },
      {
        "key": "2026-07-25",
        "label": {
          "sc": "2026-07-25",
          "tc": "2026-07-25"
        },
        "itemCount": 4,
        "itemIds": [
          "hk-premiums-q1-2026-jul25",
          "insbus-202607-hk-growth",
          "ia-public-disclosure-2026",
          "nfra-cybersecurity-rules-jul"
        ]
      },
      {
        "key": "2026-07-24",
        "label": {
          "sc": "2026-07-24",
          "tc": "2026-07-24"
        },
        "itemCount": 6,
        "itemIds": [
          "ia-q1-2026-stats",
          "hkma-complaints-20260724",
          "aia-q1-market-leader-jul24",
          "prudential-health-summit-2026",
          "ziyu-ceo-letter-20260724",
          "allianz-hsbc-singapore-jul24"
        ]
      },
      {
        "key": "2026-07-23",
        "label": {
          "sc": "2026-07-23",
          "tc": "2026-07-23"
        },
        "itemCount": 1,
        "itemIds": [
          "axa-menopause-survey-jul23"
        ]
      },
      {
        "key": "2026-07-22",
        "label": {
          "sc": "2026-07-22",
          "tc": "2026-07-22"
        },
        "itemCount": 1,
        "itemIds": [
          "sunlife-ride-to-shine-jul22"
        ]
      },
      {
        "key": "2026-07-16",
        "label": {
          "sc": "2026-07-16",
          "tc": "2026-07-16"
        },
        "itemCount": 2,
        "itemIds": [
          "aia-20260716-hyrox",
          "ia-20260716-ashk-ifoa"
        ]
      },
      {
        "key": "2026-07-15",
        "label": {
          "sc": "2026-07-15",
          "tc": "2026-07-15"
        },
        "itemCount": 4,
        "itemIds": [
          "ia-sales-rules-tightening-jul15",
          "ia-20260715-sales-practices",
          "creditsights-2026-2h",
          "hk-international-schools-2026"
        ]
      },
      {
        "key": "2026-07-14",
        "label": {
          "sc": "2026-07-14",
          "tc": "2026-07-14"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-licence-20260630"
        ]
      },
      {
        "key": "2026-07-12",
        "label": {
          "sc": "2026-07-12",
          "tc": "2026-07-12"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260712-speech"
        ]
      },
      {
        "key": "2026-07-10",
        "label": {
          "sc": "2026-07-10",
          "tc": "2026-07-10"
        },
        "itemCount": 3,
        "itemIds": [
          "ia-20260710-illustration",
          "tiger21-uhnw-allocation-2026",
          "ia-20260710-illustration-review"
        ]
      },
      {
        "key": "2026-07-08",
        "label": {
          "sc": "2026-07-08",
          "tc": "2026-07-08"
        },
        "itemCount": 3,
        "itemIds": [
          "fstb-20260708-captive",
          "ia-20260708-captive",
          "swissre-202607-wis"
        ]
      },
      {
        "key": "2026-07-07",
        "label": {
          "sc": "2026-07-07",
          "tc": "2026-07-07"
        },
        "itemCount": 1,
        "itemIds": [
          "nfra-shanghai-reins-center-jul07"
        ]
      },
      {
        "key": "2026-07-03",
        "label": {
          "sc": "2026-07-03",
          "tc": "2026-07-03"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260703-rfyc"
        ]
      },
      {
        "key": "2026-07-01",
        "label": {
          "sc": "2026-07-01",
          "tc": "2026-07-01"
        },
        "itemCount": 3,
        "itemIds": [
          "rga-2026-hk-market",
          "hkex-ipo-pipeline-2026h1",
          "ia-crossref-20260701"
        ]
      },
      {
        "key": "2026-06-30",
        "label": {
          "sc": "2026-06-30",
          "tc": "2026-06-30"
        },
        "itemCount": 3,
        "itemIds": [
          "ia-20260630-swissre-sigma",
          "ia-20260630-allianz-report",
          "hk-property-cires-2026"
        ]
      },
      {
        "key": "2026-06-29",
        "label": {
          "sc": "2026-06-29",
          "tc": "2026-06-29"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-20260629-sunlife-notes",
          "ia-20260629-hkma-bulletin"
        ]
      },
      {
        "key": "2026-06-28",
        "label": {
          "sc": "2026-06-28",
          "tc": "2026-06-28"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260628-fsdc-talent"
        ]
      },
      {
        "key": "2026-06-26",
        "label": {
          "sc": "2026-06-26",
          "tc": "2026-06-26"
        },
        "itemCount": 3,
        "itemIds": [
          "ia-20260626-morganstanley",
          "ia-20260626-pimco-asia",
          "taiping-202606-rating"
        ]
      },
      {
        "key": "2026-06-25",
        "label": {
          "sc": "2026-06-25",
          "tc": "2026-06-25"
        },
        "itemCount": 3,
        "itemIds": [
          "ia-20260625-manulife-convention",
          "empf-2026-fee-reduction",
          "manulife-20260625-board"
        ]
      },
      {
        "key": "2026-06-24",
        "label": {
          "sc": "2026-06-24",
          "tc": "2026-06-24"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260624-rga-trends"
        ]
      },
      {
        "key": "2026-06-20",
        "label": {
          "sc": "2026-06-20",
          "tc": "2026-06-20"
        },
        "itemCount": 3,
        "itemIds": [
          "ia-20260620-goldman-outlook",
          "fwd-2026-brand-victoria",
          "henley-wealth-migration-2026"
        ]
      },
      {
        "key": "2026-06-18",
        "label": {
          "sc": "2026-06-18",
          "tc": "2026-06-18"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-ai-cohort-202606",
          "ia-20260618-blackrock-outlook"
        ]
      },
      {
        "key": "2026-06-17",
        "label": {
          "sc": "2026-06-17",
          "tc": "2026-06-17"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260617-manulife-ai"
        ]
      },
      {
        "key": "2026-06-16",
        "label": {
          "sc": "2026-06-16",
          "tc": "2026-06-16"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-20260616-aia-prudential-roles",
          "ia-20260616-cheung-enforcement"
        ]
      },
      {
        "key": "2026-06-15",
        "label": {
          "sc": "2026-06-15",
          "tc": "2026-06-15"
        },
        "itemCount": 4,
        "itemIds": [
          "ia-ai-seminar-20260615",
          "axa-2026-bloomberg-awards",
          "bain-gba-crossborder-2026",
          "ia-20260615-bloomberg-crackdown"
        ]
      },
      {
        "key": "2026-06-12",
        "label": {
          "sc": "2026-06-12",
          "tc": "2026-06-12"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-20260612-manulife-plans",
          "hk-20260612-fo-tax"
        ]
      },
      {
        "key": "2026-06-10",
        "label": {
          "sc": "2026-06-10",
          "tc": "2026-06-10"
        },
        "itemCount": 3,
        "itemIds": [
          "ia-20260610-manulife-leverage",
          "ia-20260610-chowtaifook-life",
          "ctflife-2026-diamond-iul"
        ]
      },
      {
        "key": "2026-06-09",
        "label": {
          "sc": "2026-06-09",
          "tc": "2026-06-09"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260609-fitch-apac"
        ]
      },
      {
        "key": "2026-06-08",
        "label": {
          "sc": "2026-06-08",
          "tc": "2026-06-08"
        },
        "itemCount": 3,
        "itemIds": [
          "ia-20260608-axa-global-private",
          "aia-20260608-prosperlife",
          "ia-20260608-aia-wealth-flexi"
        ]
      },
      {
        "key": "2026-06-05",
        "label": {
          "sc": "2026-06-05",
          "tc": "2026-06-05"
        },
        "itemCount": 3,
        "itemIds": [
          "ia-20260605-hkma-remuneration-circ",
          "ia-hkma-remuneration-20260605",
          "ia-20260605-hkma-commission"
        ]
      },
      {
        "key": "2026-06-04",
        "label": {
          "sc": "2026-06-04",
          "tc": "2026-06-04"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260611-chubb-life"
        ]
      },
      {
        "key": "2026-06-03",
        "label": {
          "sc": "2026-06-03",
          "tc": "2026-06-03"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260603-broker-referral"
        ]
      },
      {
        "key": "2026-06-02",
        "label": {
          "sc": "2026-06-02",
          "tc": "2026-06-02"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260602-hkma-crossborder"
        ]
      },
      {
        "key": "2026-06-01",
        "label": {
          "sc": "2026-06-01",
          "tc": "2026-06-01"
        },
        "itemCount": 3,
        "itemIds": [
          "deloitte-2026-insurance-outlook",
          "chubb-20260601-mylegacy",
          "hkma-wealthconnect-2026"
        ]
      },
      {
        "key": "2026-05-29",
        "label": {
          "sc": "2026-05-29",
          "tc": "2026-05-29"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260529-onsite-findings"
        ]
      },
      {
        "key": "2026-05-28",
        "label": {
          "sc": "2026-05-28",
          "tc": "2026-05-28"
        },
        "itemCount": 1,
        "itemIds": [
          "allianz-20260528-global-report"
        ]
      },
      {
        "key": "2026-05-27",
        "label": {
          "sc": "2026-05-27",
          "tc": "2026-05-27"
        },
        "itemCount": 1,
        "itemIds": [
          "bcg-hk-1-cross-border-wealth-20260527"
        ]
      },
      {
        "key": "2026-05-20",
        "label": {
          "sc": "2026-05-20",
          "tc": "2026-05-20"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-20260520-gl34-corp",
          "fwd-2026-q1-update"
        ]
      },
      {
        "key": "2026-05-19",
        "label": {
          "sc": "2026-05-19",
          "tc": "2026-05-19"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260519-disclosure-consult"
        ]
      },
      {
        "key": "2026-05-15",
        "label": {
          "sc": "2026-05-15",
          "tc": "2026-05-15"
        },
        "itemCount": 1,
        "itemIds": [
          "sunlife-2026-10life-awards"
        ]
      },
      {
        "key": "2026-05-13",
        "label": {
          "sc": "2026-05-13",
          "tc": "2026-05-13"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-20260513-cross-ref",
          "ia-20260513-cross-refcheck"
        ]
      },
      {
        "key": "2026-05-08",
        "label": {
          "sc": "2026-05-08",
          "tc": "2026-05-08"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-20260508-rbc-conclusion",
          "ia-20260508-rbc-conclusions"
        ]
      },
      {
        "key": "2026-05-04",
        "label": {
          "sc": "2026-05-04",
          "tc": "2026-05-04"
        },
        "itemCount": 1,
        "itemIds": [
          "cpic-20260504-gen3"
        ]
      },
      {
        "key": "2026-04-30",
        "label": {
          "sc": "2026-04-30",
          "tc": "2026-04-30"
        },
        "itemCount": 1,
        "itemIds": [
          "aia-20260430-q1-vonb"
        ]
      },
      {
        "key": "2026-04-29",
        "label": {
          "sc": "2026-04-29",
          "tc": "2026-04-29"
        },
        "itemCount": 1,
        "itemIds": [
          "prudential-20260429-self-future"
        ]
      },
      {
        "key": "2026-04-27",
        "label": {
          "sc": "2026-04-27",
          "tc": "2026-04-27"
        },
        "itemCount": 1,
        "itemIds": [
          "boclife-20260427-retirement"
        ]
      },
      {
        "key": "2026-04-25",
        "label": {
          "sc": "2026-04-25",
          "tc": "2026-04-25"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-2025-full-year"
        ]
      },
      {
        "key": "2026-04-24",
        "label": {
          "sc": "2026-04-24",
          "tc": "2026-04-24"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-20260424-stats-2025",
          "aia-20260424-top-insurer"
        ]
      },
      {
        "key": "2026-04-22",
        "label": {
          "sc": "2026-04-22",
          "tc": "2026-04-22"
        },
        "itemCount": 2,
        "itemIds": [
          "ctflife-20260422-artisan-leap",
          "ia-20260422-ils"
        ]
      },
      {
        "key": "2026-04-20",
        "label": {
          "sc": "2026-04-20",
          "tc": "2026-04-20"
        },
        "itemCount": 1,
        "itemIds": [
          "manulife-20260420-annuity-accident"
        ]
      },
      {
        "key": "2026-04-16",
        "label": {
          "sc": "2026-04-16",
          "tc": "2026-04-16"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260416-cyber"
        ]
      },
      {
        "key": "2026-04-15",
        "label": {
          "sc": "2026-04-15",
          "tc": "2026-04-15"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-202604-fsi-survey"
        ]
      },
      {
        "key": "2026-04-10",
        "label": {
          "sc": "2026-04-10",
          "tc": "2026-04-10"
        },
        "itemCount": 2,
        "itemIds": [
          "chinlife-2026-hk-digital",
          "legco-20260410-fa-disclosure"
        ]
      },
      {
        "key": "2026-04-09",
        "label": {
          "sc": "2026-04-09",
          "tc": "2026-04-09"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260409-captive-beijing"
        ]
      },
      {
        "key": "2026-03-31",
        "label": {
          "sc": "2026-03-31",
          "tc": "2026-03-31"
        },
        "itemCount": 3,
        "itemIds": [
          "ia-20260331-gn16-revised",
          "gn16-revised-20260331",
          "ia-20260331-cpd-reporting"
        ]
      },
      {
        "key": "2026-03-27",
        "label": {
          "sc": "2026-03-27",
          "tc": "2026-03-27"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-2025-complaints",
          "ia-20260327-cif12"
        ]
      },
      {
        "key": "2026-03-26",
        "label": {
          "sc": "2026-03-26",
          "tc": "2026-03-26"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260326-health-conf"
        ]
      },
      {
        "key": "2026-03-25",
        "label": {
          "sc": "2026-03-25",
          "tc": "2026-03-25"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260325-captive-forum-speech"
        ]
      },
      {
        "key": "2026-03-24",
        "label": {
          "sc": "2026-03-24",
          "tc": "2026-03-24"
        },
        "itemCount": 1,
        "itemIds": [
          "chubb-2026-dementia"
        ]
      },
      {
        "key": "2026-03-20",
        "label": {
          "sc": "2026-03-20",
          "tc": "2026-03-20"
        },
        "itemCount": 1,
        "itemIds": [
          "aof-hkimr-family-office-202603"
        ]
      },
      {
        "key": "2026-03-19",
        "label": {
          "sc": "2026-03-19",
          "tc": "2026-03-19"
        },
        "itemCount": 1,
        "itemIds": [
          "aia-2025-annual-results"
        ]
      },
      {
        "key": "2026-03-17",
        "label": {
          "sc": "2026-03-17",
          "tc": "2026-03-17"
        },
        "itemCount": 2,
        "itemIds": [
          "hsbc-life-2026-hnw-pitchbook",
          "prudential-20260317-youth"
        ]
      },
      {
        "key": "2026-03-16",
        "label": {
          "sc": "2026-03-16",
          "tc": "2026-03-16"
        },
        "itemCount": 1,
        "itemIds": [
          "sunlife-202603-sp-upgrade"
        ]
      },
      {
        "key": "2026-03-15",
        "label": {
          "sc": "2026-03-15",
          "tc": "2026-03-15"
        },
        "itemCount": 2,
        "itemIds": [
          "hkma-ia-2026-genai-sandbox",
          "manulife-202603-new-products"
        ]
      },
      {
        "key": "2026-03-10",
        "label": {
          "sc": "2026-03-10",
          "tc": "2026-03-10"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260310-rbc-consult-close"
        ]
      },
      {
        "key": "2026-03-05",
        "label": {
          "sc": "2026-03-05",
          "tc": "2026-03-05"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260305-genai-sandbox"
        ]
      },
      {
        "key": "2026-03-01",
        "label": {
          "sc": "2026-03-01",
          "tc": "2026-03-01"
        },
        "itemCount": 1,
        "itemIds": [
          "newcies-2026-3200apps-95b"
        ]
      },
      {
        "key": "2026-02-25",
        "label": {
          "sc": "2026-02-25",
          "tc": "2026-02-25"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-budget-20260225"
        ]
      },
      {
        "key": "2026-02-24",
        "label": {
          "sc": "2026-02-24",
          "tc": "2026-02-24"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260224-kpim-handbook"
        ]
      },
      {
        "key": "2026-02-15",
        "label": {
          "sc": "2026-02-15",
          "tc": "2026-02-15"
        },
        "itemCount": 1,
        "itemIds": [
          "sunlife-2025-ape-118"
        ]
      },
      {
        "key": "2026-02-13",
        "label": {
          "sc": "2026-02-13",
          "tc": "2026-02-13"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260213-low-altitude"
        ]
      },
      {
        "key": "2026-02-11",
        "label": {
          "sc": "2026-02-11",
          "tc": "2026-02-11"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-20260211-rbc-consult",
          "ia-20260211-rbc-consult-launch"
        ]
      },
      {
        "key": "2026-02-10",
        "label": {
          "sc": "2026-02-10",
          "tc": "2026-02-10"
        },
        "itemCount": 4,
        "itemIds": [
          "fstb-20260210-fo-3384",
          "hk-2026-newcies-3000",
          "dlapiper-202602-gl16",
          "fstb-family-office-boom-20260210"
        ]
      },
      {
        "key": "2026-02-06",
        "label": {
          "sc": "2026-02-06",
          "tc": "2026-02-06"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260206-gl16-gl34"
        ]
      },
      {
        "key": "2026-02-01",
        "label": {
          "sc": "2026-02-01",
          "tc": "2026-02-01"
        },
        "itemCount": 1,
        "itemIds": [
          "circ-20260201-crossborder"
        ]
      },
      {
        "key": "2026-01-26",
        "label": {
          "sc": "2026-01-26",
          "tc": "2026-01-26"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-20260126-aff",
          "axa-20260126-redomicile"
        ]
      },
      {
        "key": "2026-01-23",
        "label": {
          "sc": "2026-01-23",
          "tc": "2026-01-23"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-20260123-stats-3q2025",
          "ia-20260123-q3stats"
        ]
      },
      {
        "key": "2026-01-15",
        "label": {
          "sc": "2026-01-15",
          "tc": "2026-01-15"
        },
        "itemCount": 2,
        "itemIds": [
          "evident-2026-insurance-ai",
          "ia-gl34-20260331"
        ]
      },
      {
        "key": "2026-01-10",
        "label": {
          "sc": "2026-01-10",
          "tc": "2026-01-10"
        },
        "itemCount": 1,
        "itemIds": [
          "ebact-2025-hk-market"
        ]
      },
      {
        "key": "2026-01-05",
        "label": {
          "sc": "2026-01-05",
          "tc": "2026-01-05"
        },
        "itemCount": 1,
        "itemIds": [
          "manulife-20260105-two-plans"
        ]
      },
      {
        "key": "2025-12-30",
        "label": {
          "sc": "2025-12-30",
          "tc": "2025-12-30"
        },
        "itemCount": 1,
        "itemIds": [
          "zhihu-2025-top10"
        ]
      },
      {
        "key": "2025-12-10",
        "label": {
          "sc": "2025-12-10",
          "tc": "2025-12-10"
        },
        "itemCount": 1,
        "itemIds": [
          "jpmorgan-2026-outlook"
        ]
      },
      {
        "key": "2025-12-05",
        "label": {
          "sc": "2025-12-05",
          "tc": "2025-12-05"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-2024-annual-stats"
        ]
      },
      {
        "key": "2025-11-21",
        "label": {
          "sc": "2025-11-21",
          "tc": "2025-11-21"
        },
        "itemCount": 1,
        "itemIds": [
          "aia-20251121-aisan"
        ]
      },
      {
        "key": "2025-11-20",
        "label": {
          "sc": "2025-11-20",
          "tc": "2025-11-20"
        },
        "itemCount": 2,
        "itemIds": [
          "goldman-2026-macro-outlook",
          "ia-20251120-refcheck-scheme"
        ]
      },
      {
        "key": "2025-11-13",
        "label": {
          "sc": "2025-11-13",
          "tc": "2025-11-13"
        },
        "itemCount": 1,
        "itemIds": [
          "sfc-2025-wmc-insurance"
        ]
      },
      {
        "key": "2025-10-24",
        "label": {
          "sc": "2025-10-24",
          "tc": "2025-10-24"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-20251024-1h2025-stats",
          "ia-20251024-h1stats"
        ]
      },
      {
        "key": "2025-10-14",
        "label": {
          "sc": "2025-10-14",
          "tc": "2025-10-14"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-ro-cpd-20251014"
        ]
      },
      {
        "key": "2025-09-19",
        "label": {
          "sc": "2025-09-19",
          "tc": "2025-09-19"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-202508-iul-sandbox",
          "ia-20250919-product-naming"
        ]
      },
      {
        "key": "2025-09-17",
        "label": {
          "sc": "2025-09-17",
          "tc": "2025-09-17"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20250917-product-naming"
        ]
      },
      {
        "key": "2025-09-02",
        "label": {
          "sc": "2025-09-02",
          "tc": "2025-09-02"
        },
        "itemCount": 1,
        "itemIds": [
          "manulife-20250902-hospitals"
        ]
      },
      {
        "key": "2025-09-01",
        "label": {
          "sc": "2025-09-01",
          "tc": "2025-09-01"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-20250901-referral50",
          "ia-20250901-referral-fee"
        ]
      },
      {
        "key": "2025-08-22",
        "label": {
          "sc": "2025-08-22",
          "tc": "2025-08-22"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-2024-25-annual-report"
        ]
      },
      {
        "key": "2025-08-15",
        "label": {
          "sc": "2025-08-15",
          "tc": "2025-08-15"
        },
        "itemCount": 1,
        "itemIds": [
          "dlapiper-202508-commission"
        ]
      },
      {
        "key": "2025-08-08",
        "label": {
          "sc": "2025-08-08",
          "tc": "2025-08-08"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-commission-20260101",
          "ia-20250808-rbc-disclosure"
        ]
      },
      {
        "key": "2025-07-15",
        "label": {
          "sc": "2025-07-15",
          "tc": "2025-07-15"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-202507-commission-spread"
        ]
      },
      {
        "key": "2025-07-11",
        "label": {
          "sc": "2025-07-11",
          "tc": "2025-07-11"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20250711-ro-cpd-compulsory"
        ]
      },
      {
        "key": "2025-07-08",
        "label": {
          "sc": "2025-07-08",
          "tc": "2025-07-08"
        },
        "itemCount": 1,
        "itemIds": [
          "aia-20250708-global-prosper"
        ]
      },
      {
        "key": "2025-07-01",
        "label": {
          "sc": "2025-07-01",
          "tc": "2025-07-01"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20250701-illustration-cap"
        ]
      },
      {
        "key": "2025-06-15",
        "label": {
          "sc": "2025-06-15",
          "tc": "2025-06-15"
        },
        "itemCount": 2,
        "itemIds": [
          "sunlife-2025-enhanced-savings",
          "ia-2025q1-stats-934"
        ]
      },
      {
        "key": "2025-06-01",
        "label": {
          "sc": "2025-06-01",
          "tc": "2025-06-01"
        },
        "itemCount": 1,
        "itemIds": [
          "fstb-2024-density"
        ]
      },
      {
        "key": "2025-04-28",
        "label": {
          "sc": "2025-04-28",
          "tc": "2025-04-28"
        },
        "itemCount": 1,
        "itemIds": [
          "manulife-20250428-ci"
        ]
      },
      {
        "key": "2025-04-15",
        "label": {
          "sc": "2025-04-15",
          "tc": "2025-04-15"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-2025-d-sii-designation"
        ]
      },
      {
        "key": "2025-04-09",
        "label": {
          "sc": "2025-04-09",
          "tc": "2025-04-09"
        },
        "itemCount": 1,
        "itemIds": [
          "axa-20250409-gba-med"
        ]
      },
      {
        "key": "2025-03-30",
        "label": {
          "sc": "2025-03-30",
          "tc": "2025-03-30"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20250330-illustration-article"
        ]
      },
      {
        "key": "2025-03-27",
        "label": {
          "sc": "2025-03-27",
          "tc": "2025-03-27"
        },
        "itemCount": 1,
        "itemIds": [
          "fsdc-2025-insurance-hub"
        ]
      },
      {
        "key": "2025-03-26",
        "label": {
          "sc": "2025-03-26",
          "tc": "2025-03-26"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-2025-insurtech-initiatives"
        ]
      },
      {
        "key": "2025-03-14",
        "label": {
          "sc": "2025-03-14",
          "tc": "2025-03-14"
        },
        "itemCount": 1,
        "itemIds": [
          "aia-2024-annual"
        ]
      },
      {
        "key": "2025-03-13",
        "label": {
          "sc": "2025-03-13",
          "tc": "2025-03-13"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-20250313-iul-circular",
          "ia-20250313-iul-pi"
        ]
      },
      {
        "key": "2025-02-28",
        "label": {
          "sc": "2025-02-28",
          "tc": "2025-02-28"
        },
        "itemCount": 3,
        "itemIds": [
          "nfra-202502-hkmo-insurance",
          "ia-20250228-illustration-note",
          "ia-20250228-illustration-cap-pn"
        ]
      },
      {
        "key": "2025-02-06",
        "label": {
          "sc": "2025-02-06",
          "tc": "2025-02-06"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20250206-claims-mgmt"
        ]
      },
      {
        "key": "2025-01-15",
        "label": {
          "sc": "2025-01-15",
          "tc": "2025-01-15"
        },
        "itemCount": 1,
        "itemIds": [
          "linkedin-2024-trends"
        ]
      },
      {
        "key": "2025-01-10",
        "label": {
          "sc": "2025-01-10",
          "tc": "2025-01-10"
        },
        "itemCount": 1,
        "itemIds": [
          "axa-20250110-shengli"
        ]
      },
      {
        "key": "2024-12-05",
        "label": {
          "sc": "2024-12-05",
          "tc": "2024-12-05"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20241205-annual-2024"
        ]
      },
      {
        "key": "2024-12-01",
        "label": {
          "sc": "2024-12-01",
          "tc": "2024-12-01"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-2024-re-domiciliation"
        ]
      },
      {
        "key": "2024-11-20",
        "label": {
          "sc": "2024-11-20",
          "tc": "2024-11-20"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-2024-revised-gn16-consult"
        ]
      },
      {
        "key": "2024-10-15",
        "label": {
          "sc": "2024-10-15",
          "tc": "2024-10-15"
        },
        "itemCount": 1,
        "itemIds": [
          "manulife-hiv-coverage-2024"
        ]
      },
      {
        "key": "2024-09-23",
        "label": {
          "sc": "2024-09-23",
          "tc": "2024-09-23"
        },
        "itemCount": 3,
        "itemIds": [
          "ia-20240923-license-fee",
          "ia-2024-h1-refcheck-cross-sector",
          "ia-20240923-refcheck"
        ]
      },
      {
        "key": "2024-09-15",
        "label": {
          "sc": "2024-09-15",
          "tc": "2024-09-15"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-2024h1-stats"
        ]
      },
      {
        "key": "2024-09-10",
        "label": {
          "sc": "2024-09-10",
          "tc": "2024-09-10"
        },
        "itemCount": 1,
        "itemIds": [
          "sunlife-2024-fwd-pension"
        ]
      },
      {
        "key": "2024-08-30",
        "label": {
          "sc": "2024-08-30",
          "tc": "2024-08-30"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20240830-h1-2024-stats"
        ]
      },
      {
        "key": "2024-08-20",
        "label": {
          "sc": "2024-08-20",
          "tc": "2024-08-20"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-2024-crossborder"
        ]
      },
      {
        "key": "2024-08-01",
        "label": {
          "sc": "2024-08-01",
          "tc": "2024-08-01"
        },
        "itemCount": 1,
        "itemIds": [
          "nfra-2024-crossborder-no"
        ]
      },
      {
        "key": "2024-07-26",
        "label": {
          "sc": "2024-07-26",
          "tc": "2024-07-26"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20240726-tahoe-life"
        ]
      },
      {
        "key": "2024-07-23",
        "label": {
          "sc": "2024-07-23",
          "tc": "2024-07-23"
        },
        "itemCount": 1,
        "itemIds": [
          "ctflife-20240723-rebrand"
        ]
      },
      {
        "key": "2024-07-01",
        "label": {
          "sc": "2024-07-01",
          "tc": "2024-07-01"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20240701-rbc-live"
        ]
      },
      {
        "key": "2024-06-18",
        "label": {
          "sc": "2024-06-18",
          "tc": "2024-06-18"
        },
        "itemCount": 1,
        "itemIds": [
          "henley-migration-2024"
        ]
      },
      {
        "key": "2024-06-15",
        "label": {
          "sc": "2024-06-15",
          "tc": "2024-06-15"
        },
        "itemCount": 1,
        "itemIds": [
          "ocorian-hk-wealth-magnet-2024"
        ]
      },
      {
        "key": "2024-06-14",
        "label": {
          "sc": "2024-06-14",
          "tc": "2024-06-14"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20240614-gl34-segregation"
        ]
      },
      {
        "key": "2024-06-12",
        "label": {
          "sc": "2024-06-12",
          "tc": "2024-06-12"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20240612-unlicensed-mcv"
        ]
      },
      {
        "key": "2024-05-31",
        "label": {
          "sc": "2024-05-31",
          "tc": "2024-05-31"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20240531-q1-2024-stats"
        ]
      },
      {
        "key": "2024-05-22",
        "label": {
          "sc": "2024-05-22",
          "tc": "2024-05-22"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20240522-referral-fee-circular"
        ]
      },
      {
        "key": "2024-05-01",
        "label": {
          "sc": "2024-05-01",
          "tc": "2024-05-01"
        },
        "itemCount": 1,
        "itemIds": [
          "chubb-cies-ilas-2024"
        ]
      },
      {
        "key": "2024-03-24",
        "label": {
          "sc": "2024-03-24",
          "tc": "2024-03-24"
        },
        "itemCount": 1,
        "itemIds": [
          "fstb-fo-policy-202403"
        ]
      },
      {
        "key": "2024-03-01",
        "label": {
          "sc": "2024-03-01",
          "tc": "2024-03-01"
        },
        "itemCount": 1,
        "itemIds": [
          "newcies-20240301-launch"
        ]
      },
      {
        "key": "2024-02-28",
        "label": {
          "sc": "2024-02-28",
          "tc": "2024-02-28"
        },
        "itemCount": 1,
        "itemIds": [
          "hsbc-life-250m-record-20240228"
        ]
      }
    ],
    "weekly": [
      {
        "key": "2026-W31",
        "label": {
          "sc": "2026-W31",
          "tc": "2026-W31"
        },
        "itemCount": 17,
        "itemIds": [
          "mof-rmb-bonds-cmu-jul30",
          "hkma-fed-response-jul30",
          "hkma-cmu-network-jul29",
          "bowtie-202607-100m",
          "hk-202607-mainland-scrutiny",
          "ia-20260730-sales-misconduct",
          "ai-25pct-insurance-jobs-202607",
          "picc-202607-re",
          "ia-ai-cohort-new-insurers-jul",
          "cgs-202607-hk-crackdown",
          "ratings-2026-consolidated",
          "continuum-hk-gm-202607",
          "hk-fraud-payments-lag-202607",
          "howden-hk-ceo-20260701",
          "hkma-quantum-whitepaper-jul27",
          "prudential-usd500k-legacy-202607",
          "apac-insurers-emergedebt-202607"
        ]
      },
      {
        "key": "2026-W30",
        "label": {
          "sc": "2026-W30",
          "tc": "2026-W30"
        },
        "itemCount": 15,
        "itemIds": [
          "sunlife-privatewealth-202607",
          "manulife-asian-care-survey-2026",
          "aif-2026-save-the-date",
          "hk-premiums-q1-2026-jul25",
          "insbus-202607-hk-growth",
          "ia-public-disclosure-2026",
          "nfra-cybersecurity-rules-jul",
          "ia-q1-2026-stats",
          "hkma-complaints-20260724",
          "aia-q1-market-leader-jul24",
          "prudential-health-summit-2026",
          "ziyu-ceo-letter-20260724",
          "allianz-hsbc-singapore-jul24",
          "axa-menopause-survey-jul23",
          "sunlife-ride-to-shine-jul22"
        ]
      },
      {
        "key": "2026-W29",
        "label": {
          "sc": "2026-W29",
          "tc": "2026-W29"
        },
        "itemCount": 7,
        "itemIds": [
          "aia-20260716-hyrox",
          "ia-20260716-ashk-ifoa",
          "ia-sales-rules-tightening-jul15",
          "ia-20260715-sales-practices",
          "creditsights-2026-2h",
          "hk-international-schools-2026",
          "ia-licence-20260630"
        ]
      },
      {
        "key": "2026-W28",
        "label": {
          "sc": "2026-W28",
          "tc": "2026-W28"
        },
        "itemCount": 8,
        "itemIds": [
          "ia-20260712-speech",
          "ia-20260710-illustration",
          "tiger21-uhnw-allocation-2026",
          "ia-20260710-illustration-review",
          "fstb-20260708-captive",
          "ia-20260708-captive",
          "swissre-202607-wis",
          "nfra-shanghai-reins-center-jul07"
        ]
      },
      {
        "key": "2026-W27",
        "label": {
          "sc": "2026-W27",
          "tc": "2026-W27"
        },
        "itemCount": 9,
        "itemIds": [
          "ia-20260703-rfyc",
          "rga-2026-hk-market",
          "hkex-ipo-pipeline-2026h1",
          "ia-crossref-20260701",
          "ia-20260630-swissre-sigma",
          "ia-20260630-allianz-report",
          "hk-property-cires-2026",
          "ia-20260629-sunlife-notes",
          "ia-20260629-hkma-bulletin"
        ]
      },
      {
        "key": "2026-W26",
        "label": {
          "sc": "2026-W26",
          "tc": "2026-W26"
        },
        "itemCount": 8,
        "itemIds": [
          "ia-20260628-fsdc-talent",
          "ia-20260626-morganstanley",
          "ia-20260626-pimco-asia",
          "taiping-202606-rating",
          "ia-20260625-manulife-convention",
          "empf-2026-fee-reduction",
          "manulife-20260625-board",
          "ia-20260624-rga-trends"
        ]
      },
      {
        "key": "2026-W25",
        "label": {
          "sc": "2026-W25",
          "tc": "2026-W25"
        },
        "itemCount": 12,
        "itemIds": [
          "ia-20260620-goldman-outlook",
          "fwd-2026-brand-victoria",
          "henley-wealth-migration-2026",
          "ia-ai-cohort-202606",
          "ia-20260618-blackrock-outlook",
          "ia-20260617-manulife-ai",
          "ia-20260616-aia-prudential-roles",
          "ia-20260616-cheung-enforcement",
          "ia-ai-seminar-20260615",
          "axa-2026-bloomberg-awards",
          "bain-gba-crossborder-2026",
          "ia-20260615-bloomberg-crackdown"
        ]
      },
      {
        "key": "2026-W24",
        "label": {
          "sc": "2026-W24",
          "tc": "2026-W24"
        },
        "itemCount": 9,
        "itemIds": [
          "ia-20260612-manulife-plans",
          "hk-20260612-fo-tax",
          "ia-20260610-manulife-leverage",
          "ia-20260610-chowtaifook-life",
          "ctflife-2026-diamond-iul",
          "ia-20260609-fitch-apac",
          "ia-20260608-axa-global-private",
          "aia-20260608-prosperlife",
          "ia-20260608-aia-wealth-flexi"
        ]
      },
      {
        "key": "2026-W23",
        "label": {
          "sc": "2026-W23",
          "tc": "2026-W23"
        },
        "itemCount": 9,
        "itemIds": [
          "ia-20260605-hkma-remuneration-circ",
          "ia-hkma-remuneration-20260605",
          "ia-20260605-hkma-commission",
          "ia-20260611-chubb-life",
          "ia-20260603-broker-referral",
          "ia-20260602-hkma-crossborder",
          "deloitte-2026-insurance-outlook",
          "chubb-20260601-mylegacy",
          "hkma-wealthconnect-2026"
        ]
      },
      {
        "key": "2026-W22",
        "label": {
          "sc": "2026-W22",
          "tc": "2026-W22"
        },
        "itemCount": 3,
        "itemIds": [
          "ia-20260529-onsite-findings",
          "allianz-20260528-global-report",
          "bcg-hk-1-cross-border-wealth-20260527"
        ]
      },
      {
        "key": "2026-W21",
        "label": {
          "sc": "2026-W21",
          "tc": "2026-W21"
        },
        "itemCount": 3,
        "itemIds": [
          "ia-20260520-gl34-corp",
          "fwd-2026-q1-update",
          "ia-20260519-disclosure-consult"
        ]
      },
      {
        "key": "2026-W20",
        "label": {
          "sc": "2026-W20",
          "tc": "2026-W20"
        },
        "itemCount": 3,
        "itemIds": [
          "sunlife-2026-10life-awards",
          "ia-20260513-cross-ref",
          "ia-20260513-cross-refcheck"
        ]
      },
      {
        "key": "2026-W19",
        "label": {
          "sc": "2026-W19",
          "tc": "2026-W19"
        },
        "itemCount": 3,
        "itemIds": [
          "ia-20260508-rbc-conclusion",
          "ia-20260508-rbc-conclusions",
          "cpic-20260504-gen3"
        ]
      },
      {
        "key": "2026-W18",
        "label": {
          "sc": "2026-W18",
          "tc": "2026-W18"
        },
        "itemCount": 3,
        "itemIds": [
          "aia-20260430-q1-vonb",
          "prudential-20260429-self-future",
          "boclife-20260427-retirement"
        ]
      },
      {
        "key": "2026-W17",
        "label": {
          "sc": "2026-W17",
          "tc": "2026-W17"
        },
        "itemCount": 6,
        "itemIds": [
          "ia-2025-full-year",
          "ia-20260424-stats-2025",
          "aia-20260424-top-insurer",
          "ctflife-20260422-artisan-leap",
          "ia-20260422-ils",
          "manulife-20260420-annuity-accident"
        ]
      },
      {
        "key": "2026-W16",
        "label": {
          "sc": "2026-W16",
          "tc": "2026-W16"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-20260416-cyber",
          "ia-202604-fsi-survey"
        ]
      },
      {
        "key": "2026-W15",
        "label": {
          "sc": "2026-W15",
          "tc": "2026-W15"
        },
        "itemCount": 3,
        "itemIds": [
          "chinlife-2026-hk-digital",
          "legco-20260410-fa-disclosure",
          "ia-20260409-captive-beijing"
        ]
      },
      {
        "key": "2026-W14",
        "label": {
          "sc": "2026-W14",
          "tc": "2026-W14"
        },
        "itemCount": 3,
        "itemIds": [
          "ia-20260331-gn16-revised",
          "gn16-revised-20260331",
          "ia-20260331-cpd-reporting"
        ]
      },
      {
        "key": "2026-W13",
        "label": {
          "sc": "2026-W13",
          "tc": "2026-W13"
        },
        "itemCount": 5,
        "itemIds": [
          "ia-2025-complaints",
          "ia-20260327-cif12",
          "ia-20260326-health-conf",
          "ia-20260325-captive-forum-speech",
          "chubb-2026-dementia"
        ]
      },
      {
        "key": "2026-W12",
        "label": {
          "sc": "2026-W12",
          "tc": "2026-W12"
        },
        "itemCount": 5,
        "itemIds": [
          "aof-hkimr-family-office-202603",
          "aia-2025-annual-results",
          "hsbc-life-2026-hnw-pitchbook",
          "prudential-20260317-youth",
          "sunlife-202603-sp-upgrade"
        ]
      },
      {
        "key": "2026-W11",
        "label": {
          "sc": "2026-W11",
          "tc": "2026-W11"
        },
        "itemCount": 3,
        "itemIds": [
          "hkma-ia-2026-genai-sandbox",
          "manulife-202603-new-products",
          "ia-20260310-rbc-consult-close"
        ]
      },
      {
        "key": "2026-W10",
        "label": {
          "sc": "2026-W10",
          "tc": "2026-W10"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260305-genai-sandbox"
        ]
      },
      {
        "key": "2026-W09",
        "label": {
          "sc": "2026-W09",
          "tc": "2026-W09"
        },
        "itemCount": 3,
        "itemIds": [
          "newcies-2026-3200apps-95b",
          "ia-budget-20260225",
          "ia-20260224-kpim-handbook"
        ]
      },
      {
        "key": "2026-W07",
        "label": {
          "sc": "2026-W07",
          "tc": "2026-W07"
        },
        "itemCount": 8,
        "itemIds": [
          "sunlife-2025-ape-118",
          "ia-20260213-low-altitude",
          "ia-20260211-rbc-consult",
          "ia-20260211-rbc-consult-launch",
          "fstb-20260210-fo-3384",
          "hk-2026-newcies-3000",
          "dlapiper-202602-gl16",
          "fstb-family-office-boom-20260210"
        ]
      },
      {
        "key": "2026-W06",
        "label": {
          "sc": "2026-W06",
          "tc": "2026-W06"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260206-gl16-gl34"
        ]
      },
      {
        "key": "2026-W05",
        "label": {
          "sc": "2026-W05",
          "tc": "2026-W05"
        },
        "itemCount": 3,
        "itemIds": [
          "circ-20260201-crossborder",
          "ia-20260126-aff",
          "axa-20260126-redomicile"
        ]
      },
      {
        "key": "2026-W04",
        "label": {
          "sc": "2026-W04",
          "tc": "2026-W04"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-20260123-stats-3q2025",
          "ia-20260123-q3stats"
        ]
      },
      {
        "key": "2026-W03",
        "label": {
          "sc": "2026-W03",
          "tc": "2026-W03"
        },
        "itemCount": 2,
        "itemIds": [
          "evident-2026-insurance-ai",
          "ia-gl34-20260331"
        ]
      },
      {
        "key": "2026-W02",
        "label": {
          "sc": "2026-W02",
          "tc": "2026-W02"
        },
        "itemCount": 2,
        "itemIds": [
          "ebact-2025-hk-market",
          "manulife-20260105-two-plans"
        ]
      },
      {
        "key": "2026-W01",
        "label": {
          "sc": "2026-W01",
          "tc": "2026-W01"
        },
        "itemCount": 1,
        "itemIds": [
          "zhihu-2025-top10"
        ]
      },
      {
        "key": "2025-W50",
        "label": {
          "sc": "2025-W50",
          "tc": "2025-W50"
        },
        "itemCount": 1,
        "itemIds": [
          "jpmorgan-2026-outlook"
        ]
      },
      {
        "key": "2025-W49",
        "label": {
          "sc": "2025-W49",
          "tc": "2025-W49"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-2024-annual-stats"
        ]
      },
      {
        "key": "2025-W47",
        "label": {
          "sc": "2025-W47",
          "tc": "2025-W47"
        },
        "itemCount": 3,
        "itemIds": [
          "aia-20251121-aisan",
          "goldman-2026-macro-outlook",
          "ia-20251120-refcheck-scheme"
        ]
      },
      {
        "key": "2025-W46",
        "label": {
          "sc": "2025-W46",
          "tc": "2025-W46"
        },
        "itemCount": 1,
        "itemIds": [
          "sfc-2025-wmc-insurance"
        ]
      },
      {
        "key": "2025-W43",
        "label": {
          "sc": "2025-W43",
          "tc": "2025-W43"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-20251024-1h2025-stats",
          "ia-20251024-h1stats"
        ]
      },
      {
        "key": "2025-W42",
        "label": {
          "sc": "2025-W42",
          "tc": "2025-W42"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-ro-cpd-20251014"
        ]
      },
      {
        "key": "2025-W38",
        "label": {
          "sc": "2025-W38",
          "tc": "2025-W38"
        },
        "itemCount": 3,
        "itemIds": [
          "ia-202508-iul-sandbox",
          "ia-20250919-product-naming",
          "ia-20250917-product-naming"
        ]
      },
      {
        "key": "2025-W36",
        "label": {
          "sc": "2025-W36",
          "tc": "2025-W36"
        },
        "itemCount": 3,
        "itemIds": [
          "manulife-20250902-hospitals",
          "ia-20250901-referral50",
          "ia-20250901-referral-fee"
        ]
      },
      {
        "key": "2025-W34",
        "label": {
          "sc": "2025-W34",
          "tc": "2025-W34"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-2024-25-annual-report"
        ]
      },
      {
        "key": "2025-W33",
        "label": {
          "sc": "2025-W33",
          "tc": "2025-W33"
        },
        "itemCount": 1,
        "itemIds": [
          "dlapiper-202508-commission"
        ]
      },
      {
        "key": "2025-W32",
        "label": {
          "sc": "2025-W32",
          "tc": "2025-W32"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-commission-20260101",
          "ia-20250808-rbc-disclosure"
        ]
      },
      {
        "key": "2025-W29",
        "label": {
          "sc": "2025-W29",
          "tc": "2025-W29"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-202507-commission-spread"
        ]
      },
      {
        "key": "2025-W28",
        "label": {
          "sc": "2025-W28",
          "tc": "2025-W28"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-20250711-ro-cpd-compulsory",
          "aia-20250708-global-prosper"
        ]
      },
      {
        "key": "2025-W27",
        "label": {
          "sc": "2025-W27",
          "tc": "2025-W27"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20250701-illustration-cap"
        ]
      },
      {
        "key": "2025-W24",
        "label": {
          "sc": "2025-W24",
          "tc": "2025-W24"
        },
        "itemCount": 2,
        "itemIds": [
          "sunlife-2025-enhanced-savings",
          "ia-2025q1-stats-934"
        ]
      },
      {
        "key": "2025-W22",
        "label": {
          "sc": "2025-W22",
          "tc": "2025-W22"
        },
        "itemCount": 1,
        "itemIds": [
          "fstb-2024-density"
        ]
      },
      {
        "key": "2025-W18",
        "label": {
          "sc": "2025-W18",
          "tc": "2025-W18"
        },
        "itemCount": 1,
        "itemIds": [
          "manulife-20250428-ci"
        ]
      },
      {
        "key": "2025-W16",
        "label": {
          "sc": "2025-W16",
          "tc": "2025-W16"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-2025-d-sii-designation"
        ]
      },
      {
        "key": "2025-W15",
        "label": {
          "sc": "2025-W15",
          "tc": "2025-W15"
        },
        "itemCount": 1,
        "itemIds": [
          "axa-20250409-gba-med"
        ]
      },
      {
        "key": "2025-W13",
        "label": {
          "sc": "2025-W13",
          "tc": "2025-W13"
        },
        "itemCount": 3,
        "itemIds": [
          "ia-20250330-illustration-article",
          "fsdc-2025-insurance-hub",
          "ia-2025-insurtech-initiatives"
        ]
      },
      {
        "key": "2025-W11",
        "label": {
          "sc": "2025-W11",
          "tc": "2025-W11"
        },
        "itemCount": 3,
        "itemIds": [
          "aia-2024-annual",
          "ia-20250313-iul-circular",
          "ia-20250313-iul-pi"
        ]
      },
      {
        "key": "2025-W09",
        "label": {
          "sc": "2025-W09",
          "tc": "2025-W09"
        },
        "itemCount": 3,
        "itemIds": [
          "nfra-202502-hkmo-insurance",
          "ia-20250228-illustration-note",
          "ia-20250228-illustration-cap-pn"
        ]
      },
      {
        "key": "2025-W06",
        "label": {
          "sc": "2025-W06",
          "tc": "2025-W06"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20250206-claims-mgmt"
        ]
      },
      {
        "key": "2025-W03",
        "label": {
          "sc": "2025-W03",
          "tc": "2025-W03"
        },
        "itemCount": 1,
        "itemIds": [
          "linkedin-2024-trends"
        ]
      },
      {
        "key": "2025-W02",
        "label": {
          "sc": "2025-W02",
          "tc": "2025-W02"
        },
        "itemCount": 1,
        "itemIds": [
          "axa-20250110-shengli"
        ]
      },
      {
        "key": "2024-W49",
        "label": {
          "sc": "2024-W49",
          "tc": "2024-W49"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20241205-annual-2024"
        ]
      },
      {
        "key": "2024-W48",
        "label": {
          "sc": "2024-W48",
          "tc": "2024-W48"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-2024-re-domiciliation"
        ]
      },
      {
        "key": "2024-W47",
        "label": {
          "sc": "2024-W47",
          "tc": "2024-W47"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-2024-revised-gn16-consult"
        ]
      },
      {
        "key": "2024-W42",
        "label": {
          "sc": "2024-W42",
          "tc": "2024-W42"
        },
        "itemCount": 1,
        "itemIds": [
          "manulife-hiv-coverage-2024"
        ]
      },
      {
        "key": "2024-W39",
        "label": {
          "sc": "2024-W39",
          "tc": "2024-W39"
        },
        "itemCount": 3,
        "itemIds": [
          "ia-20240923-license-fee",
          "ia-2024-h1-refcheck-cross-sector",
          "ia-20240923-refcheck"
        ]
      },
      {
        "key": "2024-W37",
        "label": {
          "sc": "2024-W37",
          "tc": "2024-W37"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-2024h1-stats",
          "sunlife-2024-fwd-pension"
        ]
      },
      {
        "key": "2024-W35",
        "label": {
          "sc": "2024-W35",
          "tc": "2024-W35"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20240830-h1-2024-stats"
        ]
      },
      {
        "key": "2024-W34",
        "label": {
          "sc": "2024-W34",
          "tc": "2024-W34"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-2024-crossborder"
        ]
      },
      {
        "key": "2024-W31",
        "label": {
          "sc": "2024-W31",
          "tc": "2024-W31"
        },
        "itemCount": 1,
        "itemIds": [
          "nfra-2024-crossborder-no"
        ]
      },
      {
        "key": "2024-W30",
        "label": {
          "sc": "2024-W30",
          "tc": "2024-W30"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-20240726-tahoe-life",
          "ctflife-20240723-rebrand"
        ]
      },
      {
        "key": "2024-W27",
        "label": {
          "sc": "2024-W27",
          "tc": "2024-W27"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20240701-rbc-live"
        ]
      },
      {
        "key": "2024-W25",
        "label": {
          "sc": "2024-W25",
          "tc": "2024-W25"
        },
        "itemCount": 1,
        "itemIds": [
          "henley-migration-2024"
        ]
      },
      {
        "key": "2024-W24",
        "label": {
          "sc": "2024-W24",
          "tc": "2024-W24"
        },
        "itemCount": 3,
        "itemIds": [
          "ocorian-hk-wealth-magnet-2024",
          "ia-20240614-gl34-segregation",
          "ia-20240612-unlicensed-mcv"
        ]
      },
      {
        "key": "2024-W22",
        "label": {
          "sc": "2024-W22",
          "tc": "2024-W22"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20240531-q1-2024-stats"
        ]
      },
      {
        "key": "2024-W21",
        "label": {
          "sc": "2024-W21",
          "tc": "2024-W21"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20240522-referral-fee-circular"
        ]
      },
      {
        "key": "2024-W18",
        "label": {
          "sc": "2024-W18",
          "tc": "2024-W18"
        },
        "itemCount": 1,
        "itemIds": [
          "chubb-cies-ilas-2024"
        ]
      },
      {
        "key": "2024-W12",
        "label": {
          "sc": "2024-W12",
          "tc": "2024-W12"
        },
        "itemCount": 1,
        "itemIds": [
          "fstb-fo-policy-202403"
        ]
      },
      {
        "key": "2024-W09",
        "label": {
          "sc": "2024-W09",
          "tc": "2024-W09"
        },
        "itemCount": 2,
        "itemIds": [
          "newcies-20240301-launch",
          "hsbc-life-250m-record-20240228"
        ]
      }
    ],
    "monthly": [
      {
        "key": "2026-07",
        "label": {
          "sc": "2026-07",
          "tc": "2026-07"
        },
        "itemCount": 51,
        "itemIds": [
          "mof-rmb-bonds-cmu-jul30",
          "hkma-fed-response-jul30",
          "hkma-cmu-network-jul29",
          "bowtie-202607-100m",
          "hk-202607-mainland-scrutiny",
          "ia-20260730-sales-misconduct",
          "ai-25pct-insurance-jobs-202607",
          "picc-202607-re",
          "ia-ai-cohort-new-insurers-jul",
          "cgs-202607-hk-crackdown",
          "ratings-2026-consolidated",
          "continuum-hk-gm-202607",
          "hk-fraud-payments-lag-202607",
          "howden-hk-ceo-20260701",
          "hkma-quantum-whitepaper-jul27",
          "prudential-usd500k-legacy-202607",
          "apac-insurers-emergedebt-202607",
          "sunlife-privatewealth-202607",
          "manulife-asian-care-survey-2026",
          "aif-2026-save-the-date",
          "hk-premiums-q1-2026-jul25",
          "insbus-202607-hk-growth",
          "ia-public-disclosure-2026",
          "nfra-cybersecurity-rules-jul",
          "ia-q1-2026-stats",
          "hkma-complaints-20260724",
          "aia-q1-market-leader-jul24",
          "prudential-health-summit-2026",
          "ziyu-ceo-letter-20260724",
          "allianz-hsbc-singapore-jul24",
          "axa-menopause-survey-jul23",
          "sunlife-ride-to-shine-jul22",
          "aia-20260716-hyrox",
          "ia-20260716-ashk-ifoa",
          "ia-sales-rules-tightening-jul15",
          "ia-20260715-sales-practices",
          "creditsights-2026-2h",
          "hk-international-schools-2026",
          "ia-licence-20260630",
          "ia-20260712-speech",
          "ia-20260710-illustration",
          "tiger21-uhnw-allocation-2026",
          "ia-20260710-illustration-review",
          "fstb-20260708-captive",
          "ia-20260708-captive",
          "swissre-202607-wis",
          "nfra-shanghai-reins-center-jul07",
          "ia-20260703-rfyc",
          "rga-2026-hk-market",
          "hkex-ipo-pipeline-2026h1",
          "ia-crossref-20260701"
        ]
      },
      {
        "key": "2026-06",
        "label": {
          "sc": "2026-06",
          "tc": "2026-06"
        },
        "itemCount": 43,
        "itemIds": [
          "ia-20260630-swissre-sigma",
          "ia-20260630-allianz-report",
          "hk-property-cires-2026",
          "ia-20260629-sunlife-notes",
          "ia-20260629-hkma-bulletin",
          "ia-20260628-fsdc-talent",
          "ia-20260626-morganstanley",
          "ia-20260626-pimco-asia",
          "taiping-202606-rating",
          "ia-20260625-manulife-convention",
          "empf-2026-fee-reduction",
          "manulife-20260625-board",
          "ia-20260624-rga-trends",
          "ia-20260620-goldman-outlook",
          "fwd-2026-brand-victoria",
          "henley-wealth-migration-2026",
          "ia-ai-cohort-202606",
          "ia-20260618-blackrock-outlook",
          "ia-20260617-manulife-ai",
          "ia-20260616-aia-prudential-roles",
          "ia-20260616-cheung-enforcement",
          "ia-ai-seminar-20260615",
          "axa-2026-bloomberg-awards",
          "bain-gba-crossborder-2026",
          "ia-20260615-bloomberg-crackdown",
          "ia-20260612-manulife-plans",
          "hk-20260612-fo-tax",
          "ia-20260610-manulife-leverage",
          "ia-20260610-chowtaifook-life",
          "ctflife-2026-diamond-iul",
          "ia-20260609-fitch-apac",
          "ia-20260608-axa-global-private",
          "aia-20260608-prosperlife",
          "ia-20260608-aia-wealth-flexi",
          "ia-20260605-hkma-remuneration-circ",
          "ia-hkma-remuneration-20260605",
          "ia-20260605-hkma-commission",
          "ia-20260611-chubb-life",
          "ia-20260603-broker-referral",
          "ia-20260602-hkma-crossborder",
          "deloitte-2026-insurance-outlook",
          "chubb-20260601-mylegacy",
          "hkma-wealthconnect-2026"
        ]
      },
      {
        "key": "2026-05",
        "label": {
          "sc": "2026-05",
          "tc": "2026-05"
        },
        "itemCount": 12,
        "itemIds": [
          "ia-20260529-onsite-findings",
          "allianz-20260528-global-report",
          "bcg-hk-1-cross-border-wealth-20260527",
          "ia-20260520-gl34-corp",
          "fwd-2026-q1-update",
          "ia-20260519-disclosure-consult",
          "sunlife-2026-10life-awards",
          "ia-20260513-cross-ref",
          "ia-20260513-cross-refcheck",
          "ia-20260508-rbc-conclusion",
          "ia-20260508-rbc-conclusions",
          "cpic-20260504-gen3"
        ]
      },
      {
        "key": "2026-04",
        "label": {
          "sc": "2026-04",
          "tc": "2026-04"
        },
        "itemCount": 14,
        "itemIds": [
          "aia-20260430-q1-vonb",
          "prudential-20260429-self-future",
          "boclife-20260427-retirement",
          "ia-2025-full-year",
          "ia-20260424-stats-2025",
          "aia-20260424-top-insurer",
          "ctflife-20260422-artisan-leap",
          "ia-20260422-ils",
          "manulife-20260420-annuity-accident",
          "ia-20260416-cyber",
          "ia-202604-fsi-survey",
          "chinlife-2026-hk-digital",
          "legco-20260410-fa-disclosure",
          "ia-20260409-captive-beijing"
        ]
      },
      {
        "key": "2026-03",
        "label": {
          "sc": "2026-03",
          "tc": "2026-03"
        },
        "itemCount": 18,
        "itemIds": [
          "ia-20260331-gn16-revised",
          "gn16-revised-20260331",
          "ia-20260331-cpd-reporting",
          "ia-2025-complaints",
          "ia-20260327-cif12",
          "ia-20260326-health-conf",
          "ia-20260325-captive-forum-speech",
          "chubb-2026-dementia",
          "aof-hkimr-family-office-202603",
          "aia-2025-annual-results",
          "hsbc-life-2026-hnw-pitchbook",
          "prudential-20260317-youth",
          "sunlife-202603-sp-upgrade",
          "hkma-ia-2026-genai-sandbox",
          "manulife-202603-new-products",
          "ia-20260310-rbc-consult-close",
          "ia-20260305-genai-sandbox",
          "newcies-2026-3200apps-95b"
        ]
      },
      {
        "key": "2026-02",
        "label": {
          "sc": "2026-02",
          "tc": "2026-02"
        },
        "itemCount": 12,
        "itemIds": [
          "ia-budget-20260225",
          "ia-20260224-kpim-handbook",
          "sunlife-2025-ape-118",
          "ia-20260213-low-altitude",
          "ia-20260211-rbc-consult",
          "ia-20260211-rbc-consult-launch",
          "fstb-20260210-fo-3384",
          "hk-2026-newcies-3000",
          "dlapiper-202602-gl16",
          "fstb-family-office-boom-20260210",
          "ia-20260206-gl16-gl34",
          "circ-20260201-crossborder"
        ]
      },
      {
        "key": "2026-01",
        "label": {
          "sc": "2026-01",
          "tc": "2026-01"
        },
        "itemCount": 8,
        "itemIds": [
          "ia-20260126-aff",
          "axa-20260126-redomicile",
          "ia-20260123-stats-3q2025",
          "ia-20260123-q3stats",
          "evident-2026-insurance-ai",
          "ia-gl34-20260331",
          "ebact-2025-hk-market",
          "manulife-20260105-two-plans"
        ]
      },
      {
        "key": "2025-12",
        "label": {
          "sc": "2025-12",
          "tc": "2025-12"
        },
        "itemCount": 3,
        "itemIds": [
          "zhihu-2025-top10",
          "jpmorgan-2026-outlook",
          "ia-2024-annual-stats"
        ]
      },
      {
        "key": "2025-11",
        "label": {
          "sc": "2025-11",
          "tc": "2025-11"
        },
        "itemCount": 4,
        "itemIds": [
          "aia-20251121-aisan",
          "goldman-2026-macro-outlook",
          "ia-20251120-refcheck-scheme",
          "sfc-2025-wmc-insurance"
        ]
      },
      {
        "key": "2025-10",
        "label": {
          "sc": "2025-10",
          "tc": "2025-10"
        },
        "itemCount": 3,
        "itemIds": [
          "ia-20251024-1h2025-stats",
          "ia-20251024-h1stats",
          "ia-ro-cpd-20251014"
        ]
      },
      {
        "key": "2025-09",
        "label": {
          "sc": "2025-09",
          "tc": "2025-09"
        },
        "itemCount": 6,
        "itemIds": [
          "ia-202508-iul-sandbox",
          "ia-20250919-product-naming",
          "ia-20250917-product-naming",
          "manulife-20250902-hospitals",
          "ia-20250901-referral50",
          "ia-20250901-referral-fee"
        ]
      },
      {
        "key": "2025-08",
        "label": {
          "sc": "2025-08",
          "tc": "2025-08"
        },
        "itemCount": 4,
        "itemIds": [
          "ia-2024-25-annual-report",
          "dlapiper-202508-commission",
          "ia-commission-20260101",
          "ia-20250808-rbc-disclosure"
        ]
      },
      {
        "key": "2025-07",
        "label": {
          "sc": "2025-07",
          "tc": "2025-07"
        },
        "itemCount": 4,
        "itemIds": [
          "ia-202507-commission-spread",
          "ia-20250711-ro-cpd-compulsory",
          "aia-20250708-global-prosper",
          "ia-20250701-illustration-cap"
        ]
      },
      {
        "key": "2025-06",
        "label": {
          "sc": "2025-06",
          "tc": "2025-06"
        },
        "itemCount": 3,
        "itemIds": [
          "sunlife-2025-enhanced-savings",
          "ia-2025q1-stats-934",
          "fstb-2024-density"
        ]
      },
      {
        "key": "2025-04",
        "label": {
          "sc": "2025-04",
          "tc": "2025-04"
        },
        "itemCount": 3,
        "itemIds": [
          "manulife-20250428-ci",
          "ia-2025-d-sii-designation",
          "axa-20250409-gba-med"
        ]
      },
      {
        "key": "2025-03",
        "label": {
          "sc": "2025-03",
          "tc": "2025-03"
        },
        "itemCount": 6,
        "itemIds": [
          "ia-20250330-illustration-article",
          "fsdc-2025-insurance-hub",
          "ia-2025-insurtech-initiatives",
          "aia-2024-annual",
          "ia-20250313-iul-circular",
          "ia-20250313-iul-pi"
        ]
      },
      {
        "key": "2025-02",
        "label": {
          "sc": "2025-02",
          "tc": "2025-02"
        },
        "itemCount": 4,
        "itemIds": [
          "nfra-202502-hkmo-insurance",
          "ia-20250228-illustration-note",
          "ia-20250228-illustration-cap-pn",
          "ia-20250206-claims-mgmt"
        ]
      },
      {
        "key": "2025-01",
        "label": {
          "sc": "2025-01",
          "tc": "2025-01"
        },
        "itemCount": 2,
        "itemIds": [
          "linkedin-2024-trends",
          "axa-20250110-shengli"
        ]
      },
      {
        "key": "2024-12",
        "label": {
          "sc": "2024-12",
          "tc": "2024-12"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-20241205-annual-2024",
          "ia-2024-re-domiciliation"
        ]
      },
      {
        "key": "2024-11",
        "label": {
          "sc": "2024-11",
          "tc": "2024-11"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-2024-revised-gn16-consult"
        ]
      },
      {
        "key": "2024-10",
        "label": {
          "sc": "2024-10",
          "tc": "2024-10"
        },
        "itemCount": 1,
        "itemIds": [
          "manulife-hiv-coverage-2024"
        ]
      },
      {
        "key": "2024-09",
        "label": {
          "sc": "2024-09",
          "tc": "2024-09"
        },
        "itemCount": 5,
        "itemIds": [
          "ia-20240923-license-fee",
          "ia-2024-h1-refcheck-cross-sector",
          "ia-20240923-refcheck",
          "ia-2024h1-stats",
          "sunlife-2024-fwd-pension"
        ]
      },
      {
        "key": "2024-08",
        "label": {
          "sc": "2024-08",
          "tc": "2024-08"
        },
        "itemCount": 3,
        "itemIds": [
          "ia-20240830-h1-2024-stats",
          "ia-2024-crossborder",
          "nfra-2024-crossborder-no"
        ]
      },
      {
        "key": "2024-07",
        "label": {
          "sc": "2024-07",
          "tc": "2024-07"
        },
        "itemCount": 3,
        "itemIds": [
          "ia-20240726-tahoe-life",
          "ctflife-20240723-rebrand",
          "ia-20240701-rbc-live"
        ]
      },
      {
        "key": "2024-06",
        "label": {
          "sc": "2024-06",
          "tc": "2024-06"
        },
        "itemCount": 4,
        "itemIds": [
          "henley-migration-2024",
          "ocorian-hk-wealth-magnet-2024",
          "ia-20240614-gl34-segregation",
          "ia-20240612-unlicensed-mcv"
        ]
      },
      {
        "key": "2024-05",
        "label": {
          "sc": "2024-05",
          "tc": "2024-05"
        },
        "itemCount": 3,
        "itemIds": [
          "ia-20240531-q1-2024-stats",
          "ia-20240522-referral-fee-circular",
          "chubb-cies-ilas-2024"
        ]
      },
      {
        "key": "2024-03",
        "label": {
          "sc": "2024-03",
          "tc": "2024-03"
        },
        "itemCount": 2,
        "itemIds": [
          "fstb-fo-policy-202403",
          "newcies-20240301-launch"
        ]
      },
      {
        "key": "2024-02",
        "label": {
          "sc": "2024-02",
          "tc": "2024-02"
        },
        "itemCount": 1,
        "itemIds": [
          "hsbc-life-250m-record-20240228"
        ]
      }
    ],
    "yearly": [
      {
        "key": "2026",
        "label": {
          "sc": "2026 年",
          "tc": "2026 年"
        },
        "itemCount": 158,
        "itemIds": [
          "mof-rmb-bonds-cmu-jul30",
          "hkma-fed-response-jul30",
          "hkma-cmu-network-jul29",
          "bowtie-202607-100m",
          "hk-202607-mainland-scrutiny",
          "ia-20260730-sales-misconduct",
          "ai-25pct-insurance-jobs-202607",
          "picc-202607-re",
          "ia-ai-cohort-new-insurers-jul",
          "cgs-202607-hk-crackdown",
          "ratings-2026-consolidated",
          "continuum-hk-gm-202607",
          "hk-fraud-payments-lag-202607",
          "howden-hk-ceo-20260701",
          "hkma-quantum-whitepaper-jul27",
          "prudential-usd500k-legacy-202607",
          "apac-insurers-emergedebt-202607",
          "sunlife-privatewealth-202607",
          "manulife-asian-care-survey-2026",
          "aif-2026-save-the-date",
          "hk-premiums-q1-2026-jul25",
          "insbus-202607-hk-growth",
          "ia-public-disclosure-2026",
          "nfra-cybersecurity-rules-jul",
          "ia-q1-2026-stats",
          "hkma-complaints-20260724",
          "aia-q1-market-leader-jul24",
          "prudential-health-summit-2026",
          "ziyu-ceo-letter-20260724",
          "allianz-hsbc-singapore-jul24",
          "axa-menopause-survey-jul23",
          "sunlife-ride-to-shine-jul22",
          "aia-20260716-hyrox",
          "ia-20260716-ashk-ifoa",
          "ia-sales-rules-tightening-jul15",
          "ia-20260715-sales-practices",
          "creditsights-2026-2h",
          "hk-international-schools-2026",
          "ia-licence-20260630",
          "ia-20260712-speech",
          "ia-20260710-illustration",
          "tiger21-uhnw-allocation-2026",
          "ia-20260710-illustration-review",
          "fstb-20260708-captive",
          "ia-20260708-captive",
          "swissre-202607-wis",
          "nfra-shanghai-reins-center-jul07",
          "ia-20260703-rfyc",
          "rga-2026-hk-market",
          "hkex-ipo-pipeline-2026h1",
          "ia-crossref-20260701",
          "ia-20260630-swissre-sigma",
          "ia-20260630-allianz-report",
          "hk-property-cires-2026",
          "ia-20260629-sunlife-notes",
          "ia-20260629-hkma-bulletin",
          "ia-20260628-fsdc-talent",
          "ia-20260626-morganstanley",
          "ia-20260626-pimco-asia",
          "taiping-202606-rating",
          "ia-20260625-manulife-convention",
          "empf-2026-fee-reduction",
          "manulife-20260625-board",
          "ia-20260624-rga-trends",
          "ia-20260620-goldman-outlook",
          "fwd-2026-brand-victoria",
          "henley-wealth-migration-2026",
          "ia-ai-cohort-202606",
          "ia-20260618-blackrock-outlook",
          "ia-20260617-manulife-ai",
          "ia-20260616-aia-prudential-roles",
          "ia-20260616-cheung-enforcement",
          "ia-ai-seminar-20260615",
          "axa-2026-bloomberg-awards",
          "bain-gba-crossborder-2026",
          "ia-20260615-bloomberg-crackdown",
          "ia-20260612-manulife-plans",
          "hk-20260612-fo-tax",
          "ia-20260610-manulife-leverage",
          "ia-20260610-chowtaifook-life",
          "ctflife-2026-diamond-iul",
          "ia-20260609-fitch-apac",
          "ia-20260608-axa-global-private",
          "aia-20260608-prosperlife",
          "ia-20260608-aia-wealth-flexi",
          "ia-20260605-hkma-remuneration-circ",
          "ia-hkma-remuneration-20260605",
          "ia-20260605-hkma-commission",
          "ia-20260611-chubb-life",
          "ia-20260603-broker-referral",
          "ia-20260602-hkma-crossborder",
          "deloitte-2026-insurance-outlook",
          "chubb-20260601-mylegacy",
          "hkma-wealthconnect-2026",
          "ia-20260529-onsite-findings",
          "allianz-20260528-global-report",
          "bcg-hk-1-cross-border-wealth-20260527",
          "ia-20260520-gl34-corp",
          "fwd-2026-q1-update",
          "ia-20260519-disclosure-consult",
          "sunlife-2026-10life-awards",
          "ia-20260513-cross-ref",
          "ia-20260513-cross-refcheck",
          "ia-20260508-rbc-conclusion",
          "ia-20260508-rbc-conclusions",
          "cpic-20260504-gen3",
          "aia-20260430-q1-vonb",
          "prudential-20260429-self-future",
          "boclife-20260427-retirement",
          "ia-2025-full-year",
          "ia-20260424-stats-2025",
          "aia-20260424-top-insurer",
          "ctflife-20260422-artisan-leap",
          "ia-20260422-ils",
          "manulife-20260420-annuity-accident",
          "ia-20260416-cyber",
          "ia-202604-fsi-survey",
          "chinlife-2026-hk-digital",
          "legco-20260410-fa-disclosure",
          "ia-20260409-captive-beijing",
          "ia-20260331-gn16-revised",
          "gn16-revised-20260331",
          "ia-20260331-cpd-reporting",
          "ia-2025-complaints",
          "ia-20260327-cif12",
          "ia-20260326-health-conf",
          "ia-20260325-captive-forum-speech",
          "chubb-2026-dementia",
          "aof-hkimr-family-office-202603",
          "aia-2025-annual-results",
          "hsbc-life-2026-hnw-pitchbook",
          "prudential-20260317-youth",
          "sunlife-202603-sp-upgrade",
          "hkma-ia-2026-genai-sandbox",
          "manulife-202603-new-products",
          "ia-20260310-rbc-consult-close",
          "ia-20260305-genai-sandbox",
          "newcies-2026-3200apps-95b",
          "ia-budget-20260225",
          "ia-20260224-kpim-handbook",
          "sunlife-2025-ape-118",
          "ia-20260213-low-altitude",
          "ia-20260211-rbc-consult",
          "ia-20260211-rbc-consult-launch",
          "fstb-20260210-fo-3384",
          "hk-2026-newcies-3000",
          "dlapiper-202602-gl16",
          "fstb-family-office-boom-20260210",
          "ia-20260206-gl16-gl34",
          "circ-20260201-crossborder",
          "ia-20260126-aff",
          "axa-20260126-redomicile",
          "ia-20260123-stats-3q2025",
          "ia-20260123-q3stats",
          "evident-2026-insurance-ai",
          "ia-gl34-20260331",
          "ebact-2025-hk-market",
          "manulife-20260105-two-plans"
        ]
      },
      {
        "key": "2025",
        "label": {
          "sc": "2025 年",
          "tc": "2025 年"
        },
        "itemCount": 42,
        "itemIds": [
          "zhihu-2025-top10",
          "jpmorgan-2026-outlook",
          "ia-2024-annual-stats",
          "aia-20251121-aisan",
          "goldman-2026-macro-outlook",
          "ia-20251120-refcheck-scheme",
          "sfc-2025-wmc-insurance",
          "ia-20251024-1h2025-stats",
          "ia-20251024-h1stats",
          "ia-ro-cpd-20251014",
          "ia-202508-iul-sandbox",
          "ia-20250919-product-naming",
          "ia-20250917-product-naming",
          "manulife-20250902-hospitals",
          "ia-20250901-referral50",
          "ia-20250901-referral-fee",
          "ia-2024-25-annual-report",
          "dlapiper-202508-commission",
          "ia-commission-20260101",
          "ia-20250808-rbc-disclosure",
          "ia-202507-commission-spread",
          "ia-20250711-ro-cpd-compulsory",
          "aia-20250708-global-prosper",
          "ia-20250701-illustration-cap",
          "sunlife-2025-enhanced-savings",
          "ia-2025q1-stats-934",
          "fstb-2024-density",
          "manulife-20250428-ci",
          "ia-2025-d-sii-designation",
          "axa-20250409-gba-med",
          "ia-20250330-illustration-article",
          "fsdc-2025-insurance-hub",
          "ia-2025-insurtech-initiatives",
          "aia-2024-annual",
          "ia-20250313-iul-circular",
          "ia-20250313-iul-pi",
          "nfra-202502-hkmo-insurance",
          "ia-20250228-illustration-note",
          "ia-20250228-illustration-cap-pn",
          "ia-20250206-claims-mgmt",
          "linkedin-2024-trends",
          "axa-20250110-shengli"
        ]
      },
      {
        "key": "2024",
        "label": {
          "sc": "2024 年",
          "tc": "2024 年"
        },
        "itemCount": 25,
        "itemIds": [
          "ia-20241205-annual-2024",
          "ia-2024-re-domiciliation",
          "ia-2024-revised-gn16-consult",
          "manulife-hiv-coverage-2024",
          "ia-20240923-license-fee",
          "ia-2024-h1-refcheck-cross-sector",
          "ia-20240923-refcheck",
          "ia-2024h1-stats",
          "sunlife-2024-fwd-pension",
          "ia-20240830-h1-2024-stats",
          "ia-2024-crossborder",
          "nfra-2024-crossborder-no",
          "ia-20240726-tahoe-life",
          "ctflife-20240723-rebrand",
          "ia-20240701-rbc-live",
          "henley-migration-2024",
          "ocorian-hk-wealth-magnet-2024",
          "ia-20240614-gl34-segregation",
          "ia-20240612-unlicensed-mcv",
          "ia-20240531-q1-2024-stats",
          "ia-20240522-referral-fee-circular",
          "chubb-cies-ilas-2024",
          "fstb-fo-policy-202403",
          "newcies-20240301-launch",
          "hsbc-life-250m-record-20240228"
        ]
      }
    ]
  },
  "boards": [
    {
      "id": "reg",
      "icon": "⚖️",
      "order": 1,
      "title": {
        "sc": "监管合规",
        "tc": "監管合規"
      },
      "desc": {
        "sc": "保监局/金管局通函、操守、佣金与转介、CPD、执法与巡查要点。",
        "tc": "保監局/金管局通函、操守、佣金與轉介、CPD、執法與巡查要點。"
      },
      "matchThemes": [
        "reg",
        "compliance",
        "career"
      ]
    },
    {
      "id": "product",
      "icon": "📦",
      "order": 2,
      "title": {
        "sc": "产品与保障",
        "tc": "產品與保障"
      },
      "desc": {
        "sc": "产品相关监管与保司官网资讯（演示规则、命名、披露口径等）。不做分红实现率数据汇总——公司另有专业工具。",
        "tc": "產品相關監管與保司官網資訊（演示規則、命名、披露口徑等）。不做分紅實現率數據匯總——公司另有專業工具。"
      },
      "matchThemes": [
        "product",
        "par",
        "uw"
      ]
    },
    {
      "id": "insurer",
      "icon": "🏢",
      "order": 3,
      "title": {
        "sc": "保司与机构",
        "tc": "保司與機構"
      },
      "desc": {
        "sc": "保险公司、经纪公司、授权与自保、机构竞争与披露。",
        "tc": "保險公司、經紀公司、授權與自保、機構競爭與披露。"
      },
      "matchThemes": [
        "firm"
      ]
    },
    {
      "id": "tech",
      "icon": "🤖",
      "order": 4,
      "title": {
        "sc": "AI 与保险科技",
        "tc": "AI 與保險科技"
      },
      "desc": {
        "sc": "GenAI 沙盒、保监局 AI 促进计划、数字化展业与工具边界。",
        "tc": "GenAI 沙盒、保監局 AI 促進計劃、數字化展業與工具邊界。"
      },
      "matchThemes": [
        "tech"
      ]
    },
    {
      "id": "market",
      "icon": "📈",
      "order": 5,
      "title": {
        "sc": "市场与行业趋势",
        "tc": "市場與行業趨勢"
      },
      "desc": {
        "sc": "新单保费、渠道人力、持牌统计、宏观与行业格局。",
        "tc": "新單保費、渠道人力、持牌統計、宏觀與行業格局。"
      },
      "matchThemes": [
        "channel",
        "macro"
      ]
    },
    {
      "id": "family",
      "icon": "🏠",
      "order": 6,
      "title": {
        "sc": "家办与跨境服务",
        "tc": "家辦與跨境服務"
      },
      "desc": {
        "sc": "身份规划、精英教育、全球资产配置、企业服务、资本市场、风险管理与地产投资",
        "tc": "身份規劃、精英教育、全球資產配置、企業服務、資本市場、風險管理與地產投資"
      },
      "matchThemes": [
        "offshore",
        "intl"
      ],
      "subs": [
        "identity-planning",
        "elite-education",
        "global-allocation",
        "corporate-service",
        "capital-market",
        "risk-management",
        "property-investment"
      ]
    }
  ],
  "feedFacets": {
    "sourceTiers": [
      {
        "id": "all",
        "icon": "◎",
        "title": {
          "sc": "全部信源",
          "tc": "全部信源"
        }
      },
      {
        "id": "official",
        "icon": "⚖️",
        "title": {
          "sc": "监管原文",
          "tc": "監管原文"
        }
      },
      {
        "id": "insurer",
        "icon": "🏢",
        "title": {
          "sc": "保司官网",
          "tc": "保司官網"
        }
      },
      {
        "id": "research",
        "icon": "🌐",
        "title": {
          "sc": "机构研究",
          "tc": "機構研究"
        }
      },
      {
        "id": "pro",
        "icon": "📎",
        "title": {
          "sc": "专业解读",
          "tc": "專業解讀"
        }
      },
      {
        "id": "media",
        "icon": "📰",
        "title": {
          "sc": "媒体线索",
          "tc": "媒體線索"
        }
      }
    ],
    "contentKinds": [
      {
        "id": "all",
        "icon": "☰",
        "title": {
          "sc": "全部文种",
          "tc": "全部文種"
        }
      },
      {
        "id": "circular",
        "icon": "📄",
        "title": {
          "sc": "通函/指引",
          "tc": "通函/指引"
        }
      },
      {
        "id": "press",
        "icon": "📣",
        "title": {
          "sc": "新闻稿",
          "tc": "新聞稿"
        }
      },
      {
        "id": "speech",
        "icon": "🎤",
        "title": {
          "sc": "演辞/讲话",
          "tc": "演辭/講話"
        }
      },
      {
        "id": "stats",
        "icon": "📊",
        "title": {
          "sc": "统计数据",
          "tc": "統計數據"
        }
      },
      {
        "id": "enforcement",
        "icon": "🔍",
        "title": {
          "sc": "执法/巡查/投诉",
          "tc": "執法/巡查/投訴"
        }
      },
      {
        "id": "product_notice",
        "icon": "📦",
        "title": {
          "sc": "产品/披露资讯",
          "tc": "產品/披露資訊"
        }
      },
      {
        "id": "market_data",
        "icon": "📈",
        "title": {
          "sc": "市场动态",
          "tc": "市場動態"
        }
      },
      {
        "id": "research",
        "icon": "📚",
        "title": {
          "sc": "研究观点",
          "tc": "研究觀點"
        }
      },
      {
        "id": "other",
        "icon": "·",
        "title": {
          "sc": "其他",
          "tc": "其他"
        }
      }
    ]
  },
  "deepCards": [
    {
      "id": "deep-commission-reform",
      "title": {
        "sc": "佣金改革三件套",
        "tc": "佣金改革三件套"
      },
      "subtitle": {
        "sc": "转介费上限 → 首年佣金 70% → 递延 5 年",
        "tc": "轉介費上限 → 首年佣金 70% → 遞延 5 年"
      },
      "summary": {
        "sc": "2024-2026 年，香港保监局以「三件套」组合拳重塑分红保单佣金结构：第一步限制转介费不超过佣金的 50%，第二步将首年佣金封顶在总额的 70%，第三步强制剩余佣金至少按 5 年递延支付。这是 IFA 收入结构 20 年来最大的结构性变革。",
        "tc": "2024-2026 年，香港保監局以「三件套」組合拳重塑分紅保單佣金結構：第一步限制轉介費不超過佣金的 50%，第二步將首年佣金封頂在總額的 70%，第三步強制剩餘佣金至少按 5 年遞延支付。這是 IFA 收入結構 20 年來最大的結構性變革。"
      },
      "timeline": [
        {
          "date": "2024-05-22",
          "text": {
            "sc": "保监局发转介费通函，首设 50% 监管基准",
            "tc": "保監局發轉介費通函，首設 50% 監管基準"
          },
          "itemId": "ia-20240522-referral-fee-circular"
        },
        {
          "date": "2025-08",
          "text": {
            "sc": "德普律师事务所分析佣金改革法律框架",
            "tc": "德普律師事務所分析佣金改革法律框架"
          },
          "itemId": "dlapiper-202508-commission"
        },
        {
          "date": "2025-09-01",
          "text": {
            "sc": "转介费 ≤50% 上限规则正式生效",
            "tc": "轉介費 ≤50% 上限規則正式生效"
          },
          "itemId": "ia-20250901-referral-fee"
        },
        {
          "date": "2026-01-01",
          "text": {
            "sc": "首年佣金 ≤70% 生效，剩余佣金至少 5 年递延支付",
            "tc": "首年佣金 ≤70% 生效，剩餘佣金至少 5 年遞延支付"
          },
          "itemId": "ia-commission-20260101"
        },
        {
          "date": "2026-06-05",
          "text": {
            "sc": "金管局联合发函规范薪酬制度",
            "tc": "金管局聯合發函規範薪酬制度"
          },
          "itemId": "ia-20260605-hkma-remuneration-circ"
        },
        {
          "date": "2026-06-03",
          "text": {
            "sc": "保监局明确经纪转介安排底线",
            "tc": "保監局明確經紀轉介安排底線"
          },
          "itemId": "ia-20260603-broker-referral"
        }
      ],
      "impact": {
        "front": {
          "sc": "首年收入天花板已降。正向看：续期复利效应增强；旧单佣金不受影响。关键转型：从「首年爆量」到「长期服务」。",
          "tc": "首年收入天花板已降。正向看：續期複利效應增強；舊單佣金不受影響。關鍵轉型：從「首年爆量」到「長期服務」。"
        },
        "midback": {
          "sc": "佣金架构调整需要更新合同模板、合规审查流程和支付系统。转介协议全文需重新起草。",
          "tc": "佣金架構調整需要更新合同模板、合規審查流程和支付系統。轉介協議全文需重新起草。"
        },
        "lead": {
          "sc": "编制和分成模型需要重构。递延 5 年意味着「代理人留存率」从 nice-to-have 变成 survival factor。",
          "tc": "編制和分成模型需要重構。遞延 5 年意味著「代理人留存率」從 nice-to-have 變成 survival factor。"
        },
        "cross": {
          "sc": "离岸架构的支付合规同步收紧，跨境佣金安排需重新评估",
          "tc": "離岸架構的支付合規同步收緊，跨境佣金安排需重新評估"
        }
      },
      "faq": [
        {
          "q": {
            "sc": "旧单受影响吗？",
            "tc": "舊單受影響嗎？"
          },
          "a": {
            "sc": "不受影响。新规仅适用于 2026 年 1 月 1 日之后签署的新保单。但有保险公司已自主提前执行。",
            "tc": "不受影響。新規僅適用於 2026 年 1 月 1 日之後簽署的新保單。但有保險公司已自主提前執行。"
          }
        },
        {
          "q": {
            "sc": "递延的佣金能提前拿吗？",
            "tc": "遞延的佣金能提前拿嗎？"
          },
          "a": {
            "sc": "不能。剩余 30% 佣金必须分至少 5 年均摊支付。离职不影响已递延部分的归属（视合同条款）。",
            "tc": "不能。剩餘 30% 佣金必須分至少 5 年均攤支付。離職不影響已遞延部分的歸屬（視合同條款）。"
          }
        },
        {
          "q": {
            "sc": "转介费 50% 上限怎么算？",
            "tc": "轉介費 50% 上限怎麼算？"
          },
          "a": {
            "sc": "以持牌经纪公司从保险公司获得的相关佣金总额为基数。转介人（非持牌）收取的费用不得超过此基数的 50%。",
            "tc": "以持牌經紀公司從保險公司獲得的相關佣金總額為基數。轉介人（非持牌）收取的費用不得超過此基數的 50%。"
          }
        }
      ]
    },
    {
      "id": "deep-rbc-implementation",
      "title": {
        "sc": "RBC 制度全程",
        "tc": "RBC 制度全程"
      },
      "subtitle": {
        "sc": "风险为本资本制度从咨询到实战",
        "tc": "風險為本資本制度從諮詢到實戰"
      },
      "summary": {
        "sc": "2024 年 7 月 1 日，香港保险业正式实施风险为本资本制度（RBC）。不到一个月，泰禾人寿因资本问题被接管——RBC 的牙齿第一次亮出来。其后 GL34（分红基金隔离）、RBC 咨询和评估持续深化，标的从「保司会不会倒」升级到「每家公司承受了多少风险」。",
        "tc": "2024 年 7 月 1 日，香港保險業正式實施風險為本資本制度（RBC）。不到一個月，泰禾人壽因資本問題被接管——RBC 的牙齒第一次亮出來。其後 GL34（分紅基金隔離）、RBC 諮詢和評估持續深化，標的從「保司會不會倒」升級到「每家公司承受了多少風險」。"
      },
      "timeline": [
        {
          "date": "2024-06-14",
          "text": {
            "sc": "GL34 宪报刊登：分红业务须设独立基金",
            "tc": "GL34 憲報刊登：分紅業務須設獨立基金"
          },
          "itemId": "ia-20240614-gl34-segregation"
        },
        {
          "date": "2024-07-01",
          "text": {
            "sc": "RBC 风险为本资本制度正式实施",
            "tc": "RBC 風險為本資本制度正式實施"
          },
          "itemId": "ia-20240701-rbc-live"
        },
        {
          "date": "2024-07-26",
          "text": {
            "sc": "泰禾人寿被监管接管——香港保险史上首次",
            "tc": "泰禾人壽被監管接管——香港保險史上首次"
          },
          "itemId": "ia-20240726-tahoe-life"
        },
        {
          "date": "2025-08-08",
          "text": {
            "sc": "RBC 公开披露框架发布",
            "tc": "RBC 公開披露框架發布"
          },
          "itemId": "ia-20250808-rbc-disclosure"
        },
        {
          "date": "2026-02-11",
          "text": {
            "sc": "保监局启动 RBC 规则修订咨询",
            "tc": "保監局啟動 RBC 規則修訂諮詢"
          },
          "itemId": "ia-20260211-rbc-consult"
        },
        {
          "date": "2026-05-08",
          "text": {
            "sc": "RBC 咨询结论发布",
            "tc": "RBC 諮詢結論發布"
          },
          "itemId": "ia-20260508-rbc-conclusions"
        }
      ],
      "impact": {
        "front": {
          "sc": "保司财务稳健性不再靠「大而不倒」的信誉背书，而是有可量化的资本充足率。选保司时多了一个硬指标。",
          "tc": "保司財務穩健性不再靠「大而不倒」的信譽背書，而是有可量化的資本充足率。選保司時多了一個硬指標。"
        },
        "midback": {
          "sc": "RBC 下的偿付能力报告是新的合规参考文件，需纳入尽调流程。泰禾事件表明监管会动真格。",
          "tc": "RBC 下的償付能力報告是新的合規參考文件，需納入盡調流程。泰禾事件表明監管會動真格。"
        },
        "lead": {
          "sc": "客户会开始问「这家公司 RBC 评分多少」。提前准备好答案，而不是临时 Google。",
          "tc": "客戶會開始問「這家公司 RBC 評分多少」。提前準備好答案，而不是臨時 Google。"
        },
        "cross": {}
      },
      "faq": [
        {
          "q": {
            "sc": "RBC 是什么？",
            "tc": "RBC 是什麼？"
          },
          "a": {
            "sc": "风险为本资本制度（Risk-Based Capital），要求保险公司持有的资本金与其承担的风险相匹配。风险越高，要求资本越多。替代原来的「一刀切」偿付准备金模式。",
            "tc": "風險為本資本制度（Risk-Based Capital），要求保險公司持有的資本金與其承擔的風險相匹配。風險越高，要求資本越多。替代原來的「一刀切」償付準備金模式。"
          }
        },
        {
          "q": {
            "sc": "泰禾事件对保单持有人有影响吗？",
            "tc": "泰禾事件對保單持有人有影響嗎？"
          },
          "a": {
            "sc": "接管经理已接管运营。根据 IA 公告，现有保单继续有效，理赔不受影响。但长期看，泰禾可能被出售或整合。",
            "tc": "接管經理已接管運營。根據 IA 公告，現有保單繼續有效，理賠不受影響。但長期看，泰禾可能被出售或整合。"
          }
        },
        {
          "q": {
            "sc": "哪家公司 RBC 评分最高？",
            "tc": "哪家公司 RBC 評分最高？"
          },
          "a": {
            "sc": "RBC 评分不公开排名，但公开披露框架（2025.08）要求保司披露关键资本指标。可查看各保司年度报告中的偿付能力章节。",
            "tc": "RBC 評分不公開排名，但公開披露框架（2025.08）要求保司披露關鍵資本指標。可查看各保司年度報告中的償付能力章節。"
          }
        }
      ]
    },
    {
      "id": "deep-par-transparency",
      "title": {
        "sc": "分红透明度升级",
        "tc": "分紅透明度升級"
      },
      "subtitle": {
        "sc": "GL34 独立基金 → GN16 标准化披露 → 演示利率上限",
        "tc": "GL34 獨立基金 → GN16 標準化披露 → 演示利率上限"
      },
      "summary": {
        "sc": "分红保单是港险的核心品类。2024-2026 年，监管以三层架构重塑分红透明度：底层用 GL34 要求资金隔离，中层用 GN16 标准化披露实现率，顶层用演示利率上限防止销售误导。三层落地后，不同保司的分红产品第一次站在可比较的平台上。",
        "tc": "分紅保單是港險的核心品類。2024-2026 年，監管以三層架構重塑分紅透明度：底層用 GL34 要求資金隔離，中層用 GN16 標準化披露實現率，頂層用演示利率上限防止銷售誤導。三層落地後，不同保司的分紅產品第一次站在可比較的平台上。"
      },
      "timeline": [
        {
          "date": "2024-06-14",
          "text": {
            "sc": "GL34：分红业务须设独立基金，资产隔离",
            "tc": "GL34：分紅業務須設獨立基金，資產隔離"
          },
          "itemId": "ia-20240614-gl34-segregation"
        },
        {
          "date": "2024-11-20",
          "text": {
            "sc": "GN16 修订咨询：推动分红实现率标准化披露",
            "tc": "GN16 修訂諮詢：推動分紅實現率標準化披露"
          },
          "itemId": "ia-2024-revised-gn16-consult"
        },
        {
          "date": "2025-02-28",
          "text": {
            "sc": "分红演示利率上限通函发布（港元 6.0%/非港元 6.5%）",
            "tc": "分紅演示利率上限通函發布（港元 6.0%/非港元 6.5%）"
          },
          "itemId": "ia-20250228-illustration-cap-pn"
        },
        {
          "date": "2025-07-01",
          "text": {
            "sc": "分红保单演示利率上限正式生效",
            "tc": "分紅保單演示利率上限正式生效"
          },
          "itemId": "ia-20250701-illustration-cap"
        },
        {
          "date": "2026-03-31",
          "text": {
            "sc": "GN16 修订版正式生效",
            "tc": "GN16 修訂版正式生效"
          },
          "itemId": "ia-20260331-gn16-revised"
        },
        {
          "date": "2026-07-10",
          "text": {
            "sc": "演示利率上限释义通函发布",
            "tc": "演示利率上限釋義通函發布"
          },
          "itemId": "ia-20260710-illustration-review"
        }
      ],
      "impact": {
        "front": {
          "sc": "客户沟通的核心武器升级：从「这家公司分红不错」升级到「这里有一张标准化的行业对比表」。演示上限也帮你挡住了过度承诺的风险。",
          "tc": "客戶溝通的核心武器升級：從「這家公司分紅不錯」升級到「這裡有一張標準化的行業對比表」。演示上限也幫你擋住了過度承諾的風險。"
        },
        "midback": {
          "sc": "需更新产品对比流程和客户教育物料。GL34 要求影响产品结构和资产管理策略。",
          "tc": "需更新產品對比流程和客戶教育物料。GL34 要求影響產品結構和資產管理策略。"
        },
        "lead": {
          "sc": "团队培训需要将分红知识体系化——不是背数字，是理解三层架构的逻辑。",
          "tc": "團隊培訓需要將分紅知識體系化——不是背數字，是理解三層架構的邏輯。"
        },
        "cross": {
          "sc": "分红产品的跨境适配性受演示上限影响，离岸客户场景需重点说明",
          "tc": "分紅產品的跨境適配性受演示上限影響，離岸客戶場景需重點說明"
        }
      },
      "faq": [
        {
          "q": {
            "sc": "演示利率下调意味着分红会变少吗？",
            "tc": "演示利率下調意味著分紅會變少嗎？"
          },
          "a": {
            "sc": "不。演示利率是销售时用的「假设投资回报率」，下调只是让演示数字更保守、更真实。实际分红由基金表现决定。下调反而减少了客户因为演示过高而失望的风险。",
            "tc": "不。演示利率是銷售時用的「假設投資回報率」，下調只是讓演示數字更保守、更真實。實際分紅由基金表現決定。下調反而減少了客戶因為演示過高而失望的風險。"
          }
        },
        {
          "q": {
            "sc": "GL34 对我的客户有什么实际影响？",
            "tc": "GL34 對我的客戶有什麼實際影響？"
          },
          "a": {
            "sc": "GL34 要求保司将分红业务的资产与其他业务隔离。简单说：你的钱不会被动用于补贴其他业务线。安全性提升。",
            "tc": "GL34 要求保司將分紅業務的資產與其他業務隔離。簡單說：你的錢不會被動用於補貼其他業務線。安全性提升。"
          }
        },
        {
          "q": {
            "sc": "怎么比较不同公司的分红表现？",
            "tc": "怎麼比較不同公司的分紅表現？"
          },
          "a": {
            "sc": "GN16 修订后，所有保司必须用统一格式在官网披露分红实现率。建议查看 5 年以上的实现率趋势而非单一年份。",
            "tc": "GN16 修訂後，所有保司必須用統一的格式在官網披露分紅實現率。建議查看 5 年以上的實現率趨勢而非單一年份。"
          }
        }
      ]
    },
    {
      "id": "deep-mcv-data-gap",
      "title": {
        "sc": "MCV 数据盲区",
        "tc": "MCV 數據盲區"
      },
      "subtitle": {
        "sc": "内地访客保费为何「突然看不见」了",
        "tc": "內地訪客保費為何「突然看不見」了"
      },
      "summary": {
        "sc": "2025 年 Q1 起，保监局临时统计不再披露内地访客（MCV）新造保费的细分数据。最后一个完整口径：2024 全年内地访客新造保费 628 亿港元，占个人新单 28.6%（终身寿 59%、危疾 28%、医疗 5%）。此后市场进入「盲飞」状态——所有关于内地客规模的数字都成了二手估算。",
        "tc": "2025 年 Q1 起，保監局臨時統計不再披露內地訪客（MCV）新造保費的細分數據。最後一個完整口徑：2024 全年內地訪客新造保費 628 億港元，佔個人新單 28.6%。此後市場進入「盲飛」狀態。"
      },
      "timeline": [
        {
          "date": "2024-04-30",
          "text": {
            "sc": "IA 公布 2024 全年：内地访客 628 亿港元占 28.6%（最后一个完整口径）",
            "tc": "IA 公佈 2024 全年：內地訪客 628 億港元佔 28.6%（最後一個完整口徑）"
          },
          "itemId": "ia-20241205-annual-2024"
        },
        {
          "date": "2025-04",
          "text": {
            "sc": "Q1 2025 起临时统计不再披露 MCV 细分，数据盲区开始",
            "tc": "Q1 2025 起臨時統計不再披露 MCV 細分，數據盲區開始"
          },
          "itemId": "ia-mcv-data-gap-2025"
        },
        {
          "date": "2025-04-30",
          "text": {
            "sc": "友邦 Q1 VONB +13%，香港业务 MCV 双引擎仍在增长（保司自愿披露的替代信号）",
            "tc": "友邦 Q1 VONB +13%，香港業務 MCV 雙引擎仍在增長（保司自願披露的替代信號）"
          },
          "itemId": "aia-q1-2025-vonb"
        },
        {
          "date": "2025-10-24",
          "text": {
            "sc": "2025 上半年统计：整体新造 1,737 亿 +50%，但无 MCV 拆分",
            "tc": "2025 上半年統計：整體新造 1,737 億 +50%，但無 MCV 拆分"
          },
          "itemId": "ia-2025h1-stats"
        },
        {
          "date": "2026-07-24",
          "text": {
            "sc": "2026 Q1 整体新造 1,411 亿 +51.1%，MCV 占比只能靠保司披露拼图",
            "tc": "2026 Q1 整體新造 1,411 億 +51.1%，MCV 佔比只能靠保司披露拼圖"
          },
          "itemId": "ia-q1-2026-stats"
        }
      ],
      "impact": {
        "front": {
          "sc": "客户会问「内地客保费到底多少」。正确回答：官方口径停在 2024 年 628 亿/28.6%，之后的数字都是估算——引用时必须标注口径。",
          "tc": "客戶會問「內地客保費到底多少」。正確回答：官方口徑停在 2024 年 628 億/28.6%，之後的數字都是估算——引用時必須標注口徑。"
        },
        "midback": {
          "sc": "宣传材料里凡涉及 MCV 数字的，一律加「估算」标签并注明来源是保司披露拼图还是媒体推算。",
          "tc": "宣傳材料裡凡涉及 MCV 數字的，一律加「估算」標籤並註明來源是保司披露拼圖還是媒體推算。"
        },
        "lead": {
          "sc": "把「数据盲区」本身当作差异化话题——向客户解释官方为什么停披露、怎么读替代信号，反而显得专业。",
          "tc": "把「數據盲區」本身當作差異化話題——向客戶解釋官方為什麼停披露、怎麼讀替代信號，反而顯得專業。"
        },
        "cross": {
          "sc": "跨境需求的真实规模成谜，架构设计只能基于整体趋势推断。监管停止披露本身就是信号：跨境资金流动的敏感度在上升。",
          "tc": "跨境需求的真實規模成謎，架構設計只能基於整體趨勢推斷。監管停止披露本身就是信號：跨境資金流動的敏感度在上升。"
        }
      },
      "faq": [
        {
          "q": {
            "sc": "为什么保监局停止披露 MCV 数据？",
            "tc": "為什麼保監局停止披露 MCV 數據？"
          },
          "a": {
            "sc": "官方未给出明确理由，普遍解读与跨境资金流动敏感度上升有关。注意：整体保费统计仍正常披露，只是去掉了内地访客拆分维度。",
            "tc": "官方未給出明確理由，普遍解讀與跨境資金流動敏感度上升有關。注意：整體保費統計仍正常披露，只是去掉了內地訪客拆分維度。"
          }
        },
        {
          "q": {
            "sc": "那怎么判断内地客需求趋势？",
            "tc": "那怎麼判斷內地客需求趨勢？"
          },
          "a": {
            "sc": "看三个替代信号：① 头部保司季报中的香港 VONB 和 MCV 描述（友邦/保诚会提）；② 整体新造保费增速（2026 Q1 +51.1%）；③ 通关/跨境基建数据。三者拼图近似还原趋势。",
            "tc": "看三個替代信號：① 頭部保司季報中的香港 VONB 和 MCV 描述；② 整體新造保費增速（2026 Q1 +51.1%）；③ 通關/跨境基建數據。三者拼圖近似還原趨勢。"
          }
        },
        {
          "q": {
            "sc": "媒体上的「内地客保费 XX 亿」能信吗？",
            "tc": "媒體上的「內地客保費 XX 億」能信嗎？"
          },
          "a": {
            "sc": "凡是没标注口径和推算方法的，都当参考不当事实。很多媒体数字是把 28.6% 占比套在新总量上算的，误差很大。",
            "tc": "凡是沒標註口徑和推算方法的，都當參考不當事實。很多媒體數字是把 28.6% 佔比套在新總量上算的，誤差很大。"
          }
        }
      ]
    }
  ],
  "stats": {
    "generatedAt": "2026-07-30T00:00:00+08:00",
    "marketPulse": {
      "title": {
        "sc": "市场脉搏",
        "tc": "市場脈搏"
      },
      "items": [
        {
          "key": "annual-nbp",
          "label": {
            "sc": "2025 年度新造保费",
            "tc": "2025 年度新造保費"
          },
          "value": "3,309",
          "unit": {
            "sc": "亿港元",
            "tc": "億港元"
          },
          "trend": "up",
          "change": "+50.6%",
          "changeLabel": {
            "sc": "同比增幅",
            "tc": "同比增幅"
          },
          "note": {
            "sc": "长期业务新造保费（不含退休计划），创历史新高",
            "tc": "長期業務新造保費（不含退休計劃），創歷史新高"
          },
          "source": "IA Annual Statistics 2025 · 2025年12月5日发布",
          "sourceUrl": "https://www.ia.org.hk/en/infocenter/press_releases/20251205.html",
          "asOf": {
            "sc": "截至 2025 年 12 月",
            "tc": "截至 2025 年 12 月"
          }
        },
        {
          "key": "q1-nbp",
          "label": {
            "sc": "2026 Q1 新造保费",
            "tc": "2026 Q1 新造保費"
          },
          "value": "1,411",
          "unit": {
            "sc": "亿港元",
            "tc": "億港元"
          },
          "trend": "up",
          "change": "+51.1%",
          "changeLabel": {
            "sc": "同比增幅",
            "tc": "同比增幅"
          },
          "note": {
            "sc": "Q1 增速未因佣金改革放缓，分红业务领涨 53.7%",
            "tc": "Q1 增速未因佣金改革放緩，分紅業務領漲 53.7%"
          },
          "source": "IA Q1 2026 Provisional · InsuranceAsia",
          "sourceUrl": "https://insuranceasia.com/insurance/in-focus/hong-kong-insurance-premiums-jump-323-38b-in-q1-2026",
          "asOf": {
            "sc": "截至 2026 年 Q1",
            "tc": "截至 2026 年 Q1"
          }
        },
        {
          "key": "mcv-share",
          "label": {
            "sc": "内地访客保费占比",
            "tc": "內地訪客保費佔比"
          },
          "value": "28.6",
          "unit": {
            "sc": "%",
            "tc": "%"
          },
          "trend": "up",
          "change": "+6.5%",
          "changeLabel": {
            "sc": "同比增幅",
            "tc": "同比增幅"
          },
          "note": {
            "sc": "占个人业务总新造的 28.6%，628 亿港元",
            "tc": "佔個人業務總新造的 28.6%，628 億港元"
          },
          "source": "IA Annual Statistics 2024 · 2025年4月25日发布",
          "sourceUrl": "https://www.ia.org.hk/en/infocenter/press_releases/20250425.html",
          "asOf": {
            "sc": "截至 2024 年 12 月",
            "tc": "截至 2024 年 12 月"
          }
        }
      ]
    },
    "familyOffice": {
      "title": {
        "sc": "家办与跨境财富",
        "tc": "家辦與跨境財富"
      },
      "items": [
        {
          "key": "fo-count",
          "label": {
            "sc": "香港家办数量",
            "tc": "香港家辦數量"
          },
          "value": "3,384",
          "unit": {
            "sc": "间",
            "tc": "間"
          },
          "trend": "up",
          "change": "+25%",
          "changeLabel": {
            "sc": "两年增幅",
            "tc": "兩年增幅"
          },
          "note": {
            "sc": "过半财富超 5,100 万美元，年底有望突破 3,000 间",
            "tc": "過半財富超 5,100 萬美元，年底有望突破 3,000 間"
          },
          "source": "投资推广署 · FamilyOfficeHK",
          "sourceUrl": "https://www.investhk.gov.hk/zh-hk/news/two-year-milestone-new-capital-investment-entrant-scheme-attracts-nearly-3-200-applications-with-expected-investment-of-about-hk-95-billion-reflecting-global-confidence-in-hong-kong/",
          "asOf": {
            "sc": "截至 2026 年 7 月",
            "tc": "截至 2026 年 7 月"
          }
        },
        {
          "key": "cross-border-wealth",
          "label": {
            "sc": "跨境财富管理规模",
            "tc": "跨境財富管理規模"
          },
          "value": "2.9",
          "unit": {
            "sc": "万亿美元",
            "tc": "萬億美元"
          },
          "trend": "up",
          "change": "全球第一",
          "changeLabel": {
            "sc": "全球排名",
            "tc": "全球排名"
          },
          "note": {
            "sc": "2026 年 BCG 报告：港超越瑞士成全球最大跨境财富中心",
            "tc": "2026 年 BCG 報告：港超越瑞士成全球最大跨境財富中心"
          },
          "source": "BCG Global Wealth Report 2026 · 2026年5月27日",
          "sourceUrl": "https://www.bcg.com/press/27may2026-hong-kong-surpasses-switzerland-largest-cross-border-wealth-hub",
          "asOf": {
            "sc": "截至 2025 年 12 月",
            "tc": "截至 2025 年 12 月"
          }
        },
        {
          "key": "cies-investment",
          "label": {
            "sc": "新 CIES 吸资规模",
            "tc": "新 CIES 吸資規模"
          },
          "value": "950",
          "unit": {
            "sc": "亿港元",
            "tc": "億港元"
          },
          "trend": "up",
          "change": "3,166 宗申请",
          "changeLabel": {
            "sc": "累计申请",
            "tc": "累計申請"
          },
          "note": {
            "sc": "2024 年 3 月启动，9.9% 资金投向投连险",
            "tc": "2024 年 3 月啟動，9.9% 資金投向投連險"
          },
          "source": "投资推广署 · 2026年3月公告",
          "sourceUrl": "https://www.investhk.gov.hk/zh-hk/news/two-year-milestone-new-capital-investment-entrant-scheme-attracts-nearly-3-200-applications-with-expected-investment-of-about-hk-95-billion-reflecting-global-confidence-in-hong-kong/",
          "asOf": {
            "sc": "截至 2026 年 3 月",
            "tc": "截至 2026 年 3 月"
          }
        }
      ]
    },
    "channelLandscape": {
      "title": {
        "sc": "渠道格局",
        "tc": "渠道格局"
      },
      "items": [
        {
          "key": "broker",
          "label": {
            "sc": "经纪渠道",
            "tc": "經紀渠道"
          },
          "value": "35.5",
          "unit": {
            "sc": "%",
            "tc": "%"
          },
          "trend": "up",
          "change": "人力 +37.1%",
          "changeLabel": {
            "sc": "3年净增",
            "tc": "3年淨增"
          },
          "note": {
            "sc": "2022 年首次超越代理渠道，2025 年与银保基本持平",
            "tc": "2022 年首次超越代理渠道，2025 年與銀保基本持平"
          },
          "source": "IA 年报 + Intermediary Licence Statistics",
          "sourceUrl": "https://www.ia.org.hk/en/infocenter/statistics/statistics.html",
          "asOf": {
            "sc": "截至 2025 年",
            "tc": "截至 2025 年"
          }
        },
        {
          "key": "agent",
          "label": {
            "sc": "代理渠道",
            "tc": "代理渠道"
          },
          "value": "23.5",
          "unit": {
            "sc": "%",
            "tc": "%"
          },
          "trend": "down",
          "change": "63% 人仅贡献 23% 量",
          "changeLabel": {
            "sc": "产能分化",
            "tc": "產能分化"
          },
          "note": {
            "sc": "人海退场：2019-2021 新入行者 65% 不足 3 年，12% 精锐约占 35% 份额，大分化加速",
            "tc": "人海退場：2019-2021 新入行者 65% 不足 3 年，12% 精銳約佔 35% 份額，大分化加速"
          },
          "source": "IA Conduct in Focus Issue 10 (Spring 2025) + IA Intermediary Licence Statistics",
          "sourceUrl": "https://www.ia.org.hk/en/legislative_framework/files/English_Conduct_in_Focus_Issue_10_Spring_2025.pdf",
          "asOf": {
            "sc": "截至 2025 年",
            "tc": "截至 2025 年"
          }
        },
        {
          "key": "bancassurance",
          "label": {
            "sc": "银保渠道",
            "tc": "銀保渠道"
          },
          "value": "35.5",
          "unit": {
            "sc": "%",
            "tc": "%"
          },
          "trend": "flat",
          "change": "HSBC Life 26.6% NBP",
          "changeLabel": {
            "sc": "市占率第一",
            "tc": "市佔率第一"
          },
          "note": {
            "sc": "银行保险与经纪渠道并驾齐驱，HSBC Life 稳居榜首",
            "tc": "銀行保險與經紀渠道並駕齊驅，HSBC Life 穩居榜首"
          },
          "source": "IA 年报 / InsuranceAsia Q1 2026",
          "sourceUrl": "https://insuranceasia.com/insurance/in-focus/hong-kong-insurance-premiums-jump-323-38b-in-q1-2026",
          "asOf": {
            "sc": "截至 2025 年",
            "tc": "截至 2025 年"
          }
        }
      ]
    },
    "regulatoryClock": {
      "title": {
        "sc": "监管时钟",
        "tc": "監管時鐘"
      },
      "subtitle": {
        "sc": "佣金三件套 + RBC + 分红透明度 · 2024-2026 关键节点",
        "tc": "佣金三件套 + RBC + 分紅透明度 · 2024-2026 關鍵節點"
      },
      "events": [
        {
          "date": "2026-03-31",
          "title": {
            "sc": "GN16 修订版正式生效",
            "tc": "GN16 修訂版正式生效"
          },
          "impact": 3,
          "desc": {
            "sc": "分红实现率披露标准化：从此客户可以用同一把尺子比较不同保司",
            "tc": "分紅實現率披露標準化：從此客戶可以用同一把尺子比較不同保司"
          },
          "itemId": "ia-20260331-gn16-revised",
          "category": {
            "sc": "分红透明度",
            "tc": "分紅透明度"
          }
        },
        {
          "date": "2026-01-01",
          "title": {
            "sc": "首年佣金 ≤70% + 递延 ≥5 年",
            "tc": "首年佣金 ≤70% + 遞延 ≥5 年"
          },
          "impact": 5,
          "desc": {
            "sc": "「佣金三件套」第二件：中国保司报行合一精神在香港的落实。IFA 收入结构天花板已降",
            "tc": "「佣金三件套」第二件：中國保司報行合一精神在香港的落實。IFA 收入結構天花板已降"
          },
          "itemId": "ia-commission-20260101",
          "category": {
            "sc": "佣金改革",
            "tc": "佣金改革"
          }
        },
        {
          "date": "2025-09-01",
          "title": {
            "sc": "转介费 ≤ 佣金总额 50%",
            "tc": "轉介費 ≤ 佣金總額 50%"
          },
          "impact": 5,
          "desc": {
            "sc": "「佣金三件套」第一件：封堵无牌转介代签模式",
            "tc": "「佣金三件套」第一件：封堵無牌轉介代簽模式"
          },
          "itemId": "ia-20250901-referral-fee",
          "category": {
            "sc": "佣金改革",
            "tc": "佣金改革"
          }
        },
        {
          "date": "2025-07-01",
          "title": {
            "sc": "分红演示利率上限生效",
            "tc": "分紅演示利率上限生效"
          },
          "impact": 3,
          "desc": {
            "sc": "港元 6.0% / 非港元 6.5%，销售演示必须保守化",
            "tc": "港元 6.0% / 非港元 6.5%，銷售演示必須保守化"
          },
          "itemId": "ia-20250701-illustration-cap",
          "category": {
            "sc": "分红透明度",
            "tc": "分紅透明度"
          }
        },
        {
          "date": "2024-06-14",
          "title": {
            "sc": "GL34：分红业务须设独立基金",
            "tc": "GL34：分紅業務須設獨立基金"
          },
          "impact": 3,
          "desc": {
            "sc": "分红透明度的底座：要求资产隔离，是后续 GN16+演示上限的前提",
            "tc": "分紅透明度的底座：要求資產隔離，是後續 GN16+演示上限的前提"
          },
          "itemId": "ia-20240614-gl34-segregation",
          "category": {
            "sc": "分红透明度",
            "tc": "分紅透明度"
          }
        },
        {
          "date": "2024-07-26",
          "title": {
            "sc": "泰禾人寿被监管接管",
            "tc": "泰禾人壽被監管接管"
          },
          "impact": 4,
          "desc": {
            "sc": "RBC 首战：香港保险史上首次监管直接接管，信号意义压倒一切",
            "tc": "RBC 首戰：香港保險史上首次監管直接接管，信號意義壓倒一切"
          },
          "itemId": "ia-20240726-tahoe-life",
          "category": {
            "sc": "监管执法",
            "tc": "監管執法"
          }
        },
        {
          "date": "2024-07-01",
          "title": {
            "sc": "RBC 风险为本资本制度实施",
            "tc": "RBC 風險為本資本制度實施"
          },
          "impact": 4,
          "desc": {
            "sc": "香港保险监管从「一刀切」向「与风险匹配」转型的基座制度",
            "tc": "香港保險監管從「一刀切」向「與風險匹配」轉型的基座制度"
          },
          "itemId": "ia-20240701-rbc-live",
          "category": {
            "sc": "制度基础",
            "tc": "制度基礎"
          }
        }
      ]
    },
    "dataSummary": {
      "title": {
        "sc": "数据来源与更新",
        "tc": "數據來源與更新"
      },
      "notes": [
        {
          "sc": "所有数值均来自公开权威来源，每条卡片底部标注源头 URL",
          "tc": "所有數值均來自公開權威來源，每條卡片底部標註源頭 URL"
        },
        {
          "sc": "IA 季度统计按 Q1(5月)/H1(8月)/Q3(10月)/全年(12月)发布，看板数据在 IA 新闻稿发布后 48 小时内更新",
          "tc": "IA 季度統計按 Q1(5月)/H1(8月)/Q3(10月)/全年(12月)發佈，看板數據在 IA 新聞稿發佈後 48 小時內更新"
        },
        {
          "sc": "BCG/Henley 年度报告按各自发布周期更新",
          "tc": "BCG/Henley 年度報告按各自發佈周期更新"
        },
        {
          "sc": "家办/CIES数据来自 InvestHK 官方公告",
          "tc": "家辦/CIES數據來自 InvestHK 官方公告"
        },
        {
          "sc": "情报站不做数据生产，只做权威数据的聚合与搬运",
          "tc": "情報站不做數據生產，只做權威數據的聚合與搬運"
        }
      ]
    },
    "insurerRankings": {
      "title": {
        "sc": "保司实力一览",
        "tc": "保司實力一覽"
      },
      "subtitle": {
        "sc": "标准保费排名(整付×10%+年化) · IA 4Q25 统计 · 数据截至 2025 全年",
        "tc": "標準保費排名(整付×10%+年化) · IA 4Q25 統計 · 數據截至 2025 全年"
      },
      "rankings": [
        {
          "rank": 1,
          "name": "HSBC Life",
          "nameZH": {
            "sc": "汇丰人寿",
            "tc": "匯豐人壽"
          },
          "share": "17.6%",
          "shareType": "std",
          "rating": "AA",
          "trend": "up",
          "note": {
            "sc": "标准保费全渠道第一",
            "tc": "標準保費全渠道第一"
          },
          "source": "IA 4Q25 Excel"
        },
        {
          "rank": 2,
          "name": "BOC Life",
          "nameZH": {
            "sc": "中银人寿",
            "tc": "中銀人壽"
          },
          "share": "14.0%",
          "shareType": "std",
          "rating": "A",
          "trend": "flat",
          "note": {
            "sc": "银保主力",
            "tc": "銀保主力"
          },
          "source": "IA 4Q25 Excel"
        },
        {
          "rank": 3,
          "name": "AIA",
          "nameZH": {
            "sc": "友邦",
            "tc": "友邦"
          },
          "share": "12.4%",
          "shareType": "std",
          "rating": "AA",
          "trend": "up",
          "note": {
            "sc": "代理渠道龙头",
            "tc": "代理渠道龍頭"
          },
          "source": "IA 4Q25 Excel"
        },
        {
          "rank": 4,
          "name": "Prudential",
          "nameZH": {
            "sc": "保诚",
            "tc": "保誠"
          },
          "share": "8.8%",
          "shareType": "std",
          "rating": "AA",
          "trend": "up",
          "note": {
            "sc": "代理纯度最高(69%)",
            "tc": "代理純度最高(69%)"
          },
          "source": "IA 4Q25 Excel"
        },
        {
          "rank": 5,
          "name": "Manulife",
          "nameZH": {
            "sc": "宏利",
            "tc": "宏利"
          },
          "share": "8.0%",
          "shareType": "std",
          "rating": "AA-",
          "trend": "up",
          "note": {
            "sc": "混合派代表, +39%YoY",
            "tc": "混合派代表, +39%YoY"
          },
          "source": "IA 4Q25 Excel"
        },
        {
          "rank": 6,
          "name": "China Life",
          "nameZH": {
            "sc": "国寿海外",
            "tc": "國壽海外"
          },
          "share": "6.8%",
          "shareType": "std",
          "rating": "A",
          "trend": "flat",
          "note": {
            "sc": "银保派",
            "tc": "銀保派"
          },
          "source": "IA 4Q25 Excel"
        },
        {
          "rank": 7,
          "name": "Sun Life",
          "nameZH": {
            "sc": "永明金融",
            "tc": "永明金融"
          },
          "share": "6.4%",
          "shareType": "std",
          "rating": "AA",
          "trend": "up",
          "note": {
            "sc": "经纪TOP3, 评级上调至AA",
            "tc": "經紀TOP3, 評級上調至AA"
          },
          "source": "IA 4Q25 Excel"
        },
        {
          "rank": 8,
          "name": "AXA",
          "nameZH": {
            "sc": "安盛",
            "tc": "安盛"
          },
          "share": "6.0%",
          "shareType": "std",
          "rating": "AA-",
          "trend": "flat",
          "note": {
            "sc": "代理派, 全球私行推手",
            "tc": "代理派, 全球私行推手"
          },
          "source": "IA 4Q25 Excel"
        },
        {
          "rank": 9,
          "name": "FWD",
          "nameZH": {
            "sc": "富卫",
            "tc": "富衛"
          },
          "share": "4.2%",
          "shareType": "std",
          "rating": "NR",
          "trend": "up",
          "note": {
            "sc": "混合派, +59%YoY",
            "tc": "混合派, +59%YoY"
          },
          "source": "IA 4Q25 Excel"
        },
        {
          "rank": 10,
          "name": "Hang Seng",
          "nameZH": {
            "sc": "恒生保险",
            "tc": "恒生保險"
          },
          "share": "4.1%",
          "shareType": "std",
          "rating": "AA",
          "trend": "down",
          "note": {
            "sc": "Top10唯一负增长(-23.5%)",
            "tc": "Top10唯一負增長(-23.5%)"
          },
          "source": "IA 4Q25 Excel"
        }
      ],
      "sourceUrl": "https://www.ia.org.hk/en/infocenter/statistics/market.html",
      "ratingSource": "S&P Global Asia-Pacific Insurance Ratings List",
      "ratingUrl": "https://www.spglobal.com/ratings/en/regulatory/article/asia-pacific-insurance-ratings-list-s101683009",
      "calcNote": {
        "sc": "标准保费=整付保费×10%+年度化保费。此口径更能反映持续缴费业务价值。",
        "tc": "標準保費=整付保費×10%+年度化保費。此口徑更能反映持續繳費業務價值。"
      }
    },
    "intelligence": {
      "title": {
        "sc": "情报密度",
        "tc": "情報密度"
      },
      "subtitle": {
        "sc": "自动从 305 条资讯聚合 · sourceKey 标准化完成",
        "tc": "自動從 305 條資訊聚合 · sourceKey 標準化完成"
      },
      "totalItems": 305,
      "sourceTiers": [
        {
          "tier": "official",
          "count": 135,
          "label": "监管一手"
        },
        {
          "tier": "insurer",
          "count": 58,
          "label": "保司公告"
        },
        {
          "tier": "media",
          "count": 56,
          "label": "媒体报道"
        },
        {
          "tier": "pro",
          "count": 41,
          "label": "专业解读"
        },
        {
          "tier": "research",
          "count": 15,
          "label": "机构研究"
        }
      ],
      "sourceKeys": [
        {
          "key": "ia",
          "count": 68
        },
        {
          "key": "insuranceasia",
          "count": 14
        },
        {
          "key": "hkma",
          "count": 13
        },
        {
          "key": "govhk",
          "count": 13
        },
        {
          "key": "manulife",
          "count": 10
        },
        {
          "key": "aia",
          "count": 9
        },
        {
          "key": "insurancebusinessmag",
          "count": 6
        },
        {
          "key": "prudential",
          "count": 6
        },
        {
          "key": "sunlife",
          "count": 5
        },
        {
          "key": "yahoofinance",
          "count": 4
        },
        {
          "key": "axa",
          "count": 3
        },
        {
          "key": "henley",
          "count": 3
        },
        {
          "key": "asiainsurancereview",
          "count": 2
        },
        {
          "key": "swissre",
          "count": 2
        },
        {
          "key": "allianz",
          "count": 2
        }
      ],
      "topThemes": [
        {
          "theme": "market",
          "count": 132,
          "label": "市场"
        },
        {
          "theme": "reg",
          "count": 64,
          "label": "监管"
        },
        {
          "theme": "firm",
          "count": 49,
          "label": "保司"
        },
        {
          "theme": "offshore",
          "count": 48,
          "label": "跨境"
        },
        {
          "theme": "compliance",
          "count": 43,
          "label": "合规"
        },
        {
          "theme": "product",
          "count": 32,
          "label": "产品"
        },
        {
          "theme": "macro",
          "count": 29,
          "label": "宏观"
        },
        {
          "theme": "channel",
          "count": 25,
          "label": "渠道"
        },
        {
          "theme": "tech",
          "count": 17,
          "label": "科技"
        },
        {
          "theme": "career",
          "count": 15,
          "label": "职业"
        }
      ],
      "dateRange": {
        "sc": "2024-02-26 ~ 2026-08-05",
        "tc": "2024-02-26 ~ 2026-08-05"
      }
    },
    "marketData": {
      "title": {
        "sc": "市场数据",
        "tc": "市場數據"
      },
      "description": {
        "sc": "IA 一手统计 · 独立分析 · 不引用第三方平台",
        "tc": "IA 一手統計 · 獨立分析 · 不引用第三方平台"
      },
      "annualHighlights": [
        {
          "sc": "2025 全年新单 3,306 亿(个人)，同比 +50.6%，历史最高",
          "tc": "2025 全年新單 3,306 億(個人)，同比 +50.6%，歷史最高"
        },
        {
          "sc": "2026 Q1 1,410 亿，单季已超 2020-2022 任意全年",
          "tc": "2026 Q1 1,410 億，單季已超 2020-2022 任意全年"
        },
        {
          "sc": "经纪渠道 35.5% 与银保 35.8% 差距仅 0.3pp，事实上已平起平坐",
          "tc": "經紀渠道 35.5% 與銀保 35.8% 差距僅 0.3pp，事實上已平起平坐"
        },
        {
          "sc": "三年(2023→2026)持牌经纪人净增 3,673，+37.1%，银行代理唯一收缩",
          "tc": "三年(2023→2026)持牌經紀人淨增 3,673，+37.1%，銀行代理唯一收縮"
        }
      ],
      "dataFile": "data/market-data.json",
      "liveCheck": "2026-06-30 中介人数据已从 IA 官网实时抓取"
    },
    "companyDNA": {
      "title": {
        "sc": "保司渠道 DNA",
        "tc": "保司渠道 DNA"
      },
      "subtitle": {
        "sc": "13家头部保司×渠道分类 · 代理派/银保派/经纪派/混合派",
        "tc": "13家頭部保司×渠道分類 · 代理派/銀保派/經紀派/混合派"
      },
      "calcNote": {
        "sc": "分类规则：代理>60%→代理派；银保>50%→银保派；经纪>60%→经纪派；无渠道过半→混合派。数据来源：IA 4Q25 Excel 逐公司渠道拆分。渠道占比为近似值，精确数据以 IA Excel 为准。",
        "tc": "分類規則：代理>60%→代理派；銀保>50%→銀保派；經紀>60%→經紀派；無渠道過半→混合派。數據來源：IA 4Q25 Excel 逐公司渠道拆分。渠道佔比為近似值，精確數據以 IA Excel 為準。"
      },
      "sourceUrl": "https://www.ia.org.hk/en/infocenter/statistics/quarterly_release_of_provisional_statistics_for_long_term_business.html",
      "sourceLabel": "IA 4Q25 个人寿险新单业务统计 Excel",
      "rows": [
        {
          "company": "保诚 Prudential",
          "archetype": "agent-dominant",
          "archetypeLabel": {
            "sc": "代理派",
            "tc": "代理派"
          },
          "agentPct": 69,
          "bankPct": 10,
          "brokerPct": 16,
          "directPct": 5,
          "gross2025": 219.8,
          "yoy": 5.2,
          "note": {
            "sc": "代理纯度最高, 绝对规模受产能制约",
            "tc": "代理純度最高, 絕對規模受產能制約"
          }
        },
        {
          "company": "友邦 AIA",
          "archetype": "agent-dominant",
          "archetypeLabel": {
            "sc": "代理派",
            "tc": "代理派"
          },
          "agentPct": 62.5,
          "bankPct": 12,
          "brokerPct": 20,
          "directPct": 5.5,
          "gross2025": 446.9,
          "yoy": 15,
          "note": {
            "sc": "渠道纯度+规模量级双优, 唯二保持代理>经纪",
            "tc": "渠道純度+規模量級雙優, 唯二保持代理>經紀"
          }
        },
        {
          "company": "安盛 AXA",
          "archetype": "agent-dominant",
          "archetypeLabel": {
            "sc": "代理派",
            "tc": "代理派"
          },
          "agentPct": 55,
          "bankPct": 15,
          "brokerPct": 25,
          "directPct": 5,
          "gross2025": 198.0,
          "yoy": 8,
          "note": {
            "sc": "代理为主+全球私行协同",
            "tc": "代理為主+全球私行協同"
          }
        },
        {
          "company": "中银人寿 BOC Life",
          "archetype": "bank-dominant",
          "archetypeLabel": {
            "sc": "银保派",
            "tc": "銀保派"
          },
          "agentPct": 16,
          "bankPct": 53,
          "brokerPct": 25,
          "directPct": 6,
          "gross2025": 463.0,
          "yoy": 10,
          "note": {
            "sc": "背靠中银渠道, 银保占比超50%",
            "tc": "背靠中銀渠道, 銀保佔比超50%"
          }
        },
        {
          "company": "中国人寿海外 China Life",
          "archetype": "bank-dominant",
          "archetypeLabel": {
            "sc": "银保派",
            "tc": "銀保派"
          },
          "agentPct": 14,
          "bankPct": 55,
          "brokerPct": 26,
          "directPct": 5,
          "gross2025": 225.0,
          "yoy": 5,
          "note": {
            "sc": "银保为主, 代理仅14%",
            "tc": "銀保為主, 代理僅14%"
          }
        },
        {
          "company": "立桥人寿",
          "archetype": "broker-dominant",
          "archetypeLabel": {
            "sc": "经纪派",
            "tc": "經紀派"
          },
          "agentPct": 5,
          "bankPct": 5,
          "brokerPct": 85,
          "directPct": 5,
          "gross2025": 16.5,
          "yoy": 50,
          "note": {
            "sc": "几乎全外包给独立中介",
            "tc": "幾乎全外包給獨立中介"
          }
        },
        {
          "company": "忠意 Generali",
          "archetype": "broker-dominant",
          "archetypeLabel": {
            "sc": "经纪派",
            "tc": "經紀派"
          },
          "agentPct": 5,
          "bankPct": 5,
          "brokerPct": 85,
          "directPct": 5,
          "gross2025": 36.3,
          "yoy": 20,
          "note": {
            "sc": "经纪占比超80%",
            "tc": "經紀佔比超80%"
          }
        },
        {
          "company": "安达人寿 Chubb",
          "archetype": "broker-dominant",
          "archetypeLabel": {
            "sc": "经纪派",
            "tc": "經紀派"
          },
          "agentPct": 5,
          "bankPct": 5,
          "brokerPct": 85,
          "directPct": 5,
          "gross2025": 43.0,
          "yoy": 283.4,
          "note": {
            "sc": "2025增速冠军, CIES投连险推手",
            "tc": "2025增速冠軍, CIES投連險推手"
          }
        },
        {
          "company": "宏利 Manulife",
          "archetype": "hybrid",
          "archetypeLabel": {
            "sc": "混合派",
            "tc": "混合派"
          },
          "agentPct": 30,
          "bankPct": 25,
          "brokerPct": 40,
          "directPct": 5,
          "gross2025": 312.8,
          "yoy": 39,
          "note": {
            "sc": "三引擎驱动, +39%高速增长",
            "tc": "三引擎驅動, +39%高速增長"
          }
        },
        {
          "company": "永明 Sun Life",
          "archetype": "hybrid",
          "archetypeLabel": {
            "sc": "混合派",
            "tc": "混合派"
          },
          "agentPct": 20,
          "bankPct": 30,
          "brokerPct": 45,
          "directPct": 5,
          "gross2025": 211.2,
          "yoy": 30,
          "note": {
            "sc": "经纪TOP3, 评级上调至AA",
            "tc": "經紀TOP3, 評級上調至AA"
          }
        },
        {
          "company": "周大福人寿 CTF Life",
          "archetype": "hybrid",
          "archetypeLabel": {
            "sc": "混合派",
            "tc": "混合派"
          },
          "agentPct": 25,
          "bankPct": 30,
          "brokerPct": 40,
          "directPct": 5,
          "gross2025": 69.4,
          "yoy": 15,
          "note": {
            "sc": "2024更名, 三渠道均衡",
            "tc": "2024更名, 三渠道均衡"
          }
        },
        {
          "company": "富卫 FWD",
          "archetype": "hybrid",
          "archetypeLabel": {
            "sc": "混合派",
            "tc": "混合派"
          },
          "agentPct": 25,
          "bankPct": 30,
          "brokerPct": 40,
          "directPct": 5,
          "gross2025": 267.5,
          "yoy": 59,
          "note": {
            "sc": "+59%仅次于Chubb, 三引擎",
            "tc": "+59%僅次於Chubb, 三引擎"
          }
        },
        {
          "company": "恒生保险 Hang Seng",
          "archetype": "bank-dominant",
          "archetypeLabel": {
            "sc": "银保派",
            "tc": "銀保派"
          },
          "agentPct": 10,
          "bankPct": 75,
          "brokerPct": 10,
          "directPct": 5,
          "gross2025": 135.0,
          "yoy": -23.5,
          "note": {
            "sc": "Top10唯一负增长, 银保高度依赖",
            "tc": "Top10唯一負增長, 銀保高度依賴"
          }
        }
      ]
    },
    "talentFlow": {
      "title": {
        "sc": "中介人人才流向",
        "tc": "中介人人才流向"
      },
      "subtitle": {
        "sc": "保险中介人持牌人数变化 · 来源 IA 官网实时数据 + 年度 Excel",
        "tc": "保險中介人持牌人數變化 · 來源 IA 官網實時數據 + 年度 Excel"
      },
      "sourceUrl": "https://www.ia.org.hk/en/infocenter/statistics/statistics.html",
      "sourceLabel": "IA 保险中介人牌照统计",
      "calcNote": {
        "sc": "数据口径：持牌个人（保险代理+技术代表代理+技术代表经纪），不含业务实体。2023-2025 数据待从 IA Excel 逐行提取验证。",
        "tc": "數據口徑：持牌個人（保險代理+技術代表代理+技術代表經紀），不含業務實體。2023-2025 數據待從 IA Excel 逐行提取驗證。"
      },
      "liveData": {
        "date": "2026-06-30",
        "totalIndividuals": 122481,
        "agents": 84019,
        "techRepAgent": 23436,
        "techRepBroker": 15026,
        "agencies": 1470,
        "brokerCompanies": 810,
        "grandTotal": 124761,
        "sourceNote": "IA 官网实时页面, last updated 2026-07-14"
      },
      "historicalEstimate": {
        "2026-03": {
          "total": 121569,
          "brokers": 13500,
          "note": "交叉验证数据"
        },
        "change": {
          "3yNetIncrease": 7562,
          "brokerIncrease": 3673,
          "brokerPct37": 37.1
        }
      },
      "excelDownloads": {
        "2026": "https://www.ia.org.hk/en/infocenter/statistics/files/Insurance_Intermediary_Licence_Statistics_2026_JanToMay.xlsx",
        "2025": "https://www.ia.org.hk/en/infocenter/statistics/files/Insurance_Intermediary_Licence_Statistics_2025.xlsx",
        "2024": "https://www.ia.org.hk/en/infocenter/statistics/files/Insurance_Intermediary_Licence_Statistics_2024.xlsx",
        "2023": "https://www.ia.org.hk/en/infocenter/statistics/files/Insurance_Intermediary_Licence_Statistics_2023.xlsx"
      }
    }
  }
};
(function () {
  const DATA = window.HKII_DATA;
  const L = {
    sc: {
      brandName: "猫圈儿港险情报站", brandSub: "维港猫圈儿 · 持牌人情报台", wechat: "公众号：维港猫圈儿",
      foot: "专业参考 · 非销售/投资建议 · 数字请回原文", menu: "菜单",
      roles: [{id:"front",label:"前线IFA"},{id:"midback",label:"中后台合规"},{id:"lead",label:"团队管理"},{id:"cross",label:"跨境架构"}],
      nav: [
        {id:"dashboard",label:"情报看板",ico:"◉"},{id:"pulse",label:"今日脉搏",ico:"◈"},{id:"all",label:"全部动态",ico:"☰"},{id:"daily",label:"角色日报",ico:"▣"},{id:"themes",label:"主题雷达",ico:"◎"},{id:"deeps",label:"监管深度",ico:"◆"},{id:"calendar",label:"事件日历",ico:"◷"},{id:"download",label:"数据下载",ico:"⬇"},{id:"fav",label:"收藏",ico:"☆"},{id:"agent",label:"Agent 接入",ico:"⌘"},{id:"changelog",label:"更新日志",ico:"◌"},{id:"about",label:"关于",ico:"ⓘ"}
      ],
      sec:{c:"内容",a:"接入",m:"更多"},
      views:{
        dashboard:{t:"情报看板",s:"市场数据实时仪表板 · 源头可溯 · 数字搬运"},pulse:{t:"今日脉搏",s:"热点: 近14天官方高分自动上榜 · 精选: 评分×角色匹配动态排序"},
        all:{t:"全部动态",s:"全量信息流 · 按信源/文种细筛（≠主题雷达）"},
        daily:{t:"角色日报",s:"固定节奏的专业早报"},download:{t:"数据下载",s:"按日/周/月/年打包导出 Markdown · 原文可溯"},
        themes:{t:"主题雷达",s:"六大业务板块地图 · 战略导航，不是信息流细筛"},
        deeps:{t:"监管深度",s:"重大事件完整画像 · 时间线 · 影响矩阵 · FAQ · 关联条目"},calendar:{t:"事件日历",s:"关键事件 · 生效日 · 行业节点"},
        fav:{t:"收藏",s:"保存在本机"},
        agent:{t:"Agent 接入",s:"JSON Feed · RSS · llms.txt"},changelog:{t:"更新日志",s:"功能与数据变更记录"},about:{t:"关于",s:"定位、原则与免责"}
      },
      themes:{reg:"监管",product:"产品",channel:"渠道人力",macro:"宏观资产",par:"分红实现率",uw:"核保理赔",compliance:"合规实操",offshore:"跨境离岸",firm:"机构竞争",tech:"科技运营",career:"职业CPD",intl:"国际对标"},
      tier:{official:"一手监管",insurer:"保司官方",pro:"专业解读",media:"媒体"},
      hot:"热点", allChip:"全部", searchPh:"搜索标题/摘要/标签…", empty:"无匹配结果",
      verified:"已核原文", pending:"待复核", score:"评分", cluster:"源同题", why:"为什么重要",
      actionNow:"今日动作", actionAll:"全角色动作", summary:"摘要", themesH:"主题", effective:"生效 / 相关日期",
      original:"打开原文", note:"核对提示", dayUnit:"条", roleNow:"当前角色", window:"数据截至",
      about1:"猫圈儿港险情报站——专注香港保险监管与行业资讯的聚合导读平台。数据来源：保监局(IA)、金管局(HKMA)、保司官网披露、国际机构研究与权威媒体线索。每条导读均可回追原文，播报时间精确到分钟。",
      about2:"与微信公众号「维港猫圈儿」同一品牌人格：专业、好懂、有温度。站点偏工具与检索；公众号偏解读与陪伴。",
      qrTip:"微信扫码关注，获取每日港险解读与陪伴。",
      principles:"原则", p1:"监管与保司官网资讯优先；媒体/研究作线索，必须可回原文", p2:"同一矿山，按角色切片", p3:"每条精选带「今日动作」", p4:"摘要必须可回原文",
      disclaimer:"免责声明", disc:"内容供香港持牌保险中介及专业人士参考，不构成销售建议、投资建议或法律意见。请以监管与保司原文为准。",
      agentH:"如何接入", agentSub:"三条路径规划与 AI HOT 对齐：网页人读 + RSS/API + Agent Skill。当前原型以网页为准，接口形态如下。",
      a1:"网页：每日打开「今日脉搏 / 全部动态 / 角色日报」，用顶部角色切片视图。",
      a2:"RSS / REST API（下一阶段）：匿名只读、稳定契约；API 轮询建议 ≥60s，RSS ≥30 分钟；收到 429 按 Retry-After 退避。",
      a3:"Agent Skill（下一阶段）：安装一次后用中文问「过去24小时五件大事」；返回时间窗、中文摘要与站内/原文链接。",
      agentUseH:"接入后怎么用",
      agentUse1:"按角色提问：前线 IFA / 中后台合规 / 团队管理 / 跨境架构。",
      agentUse2:"要时间线：例如「佣金分摊 / 转介费 / 演示利率上限」相关规则按生效日排序。",
      agentUse3:"增量同步：首次 snapshot 全量精选，之后只拉 changes（规划中）。",
      agentUse4:"导出：数据下载页按日/周/月/年导出 Markdown，或单条详情导出。",
      agentEx:"示例问法",
      agentCode:"过去 24 小时港险监管与产品最重要的 5 件事？\n只给我中后台合规视角，忽略促销。\n佣金分摊与转介费相关规则时间线。\n把本周精选同步成 Markdown 清单。",
      agentDiscH:"使用与免责（重要）",
      agentDisc1:"摘要与动作卡由人工/AI 二次整理，数字、政策与原话引用前必须打开原文 URL 复核。",
      agentDisc2:"对外发布请保留来源与 canonical；本站导读不构成销售建议、投资建议或法律意见。",
      agentDisc3:"公开可读 ≠ 可忽略版权与频率合同；禁止批量绕过限流的爬取。",
      agentDisc4:"v1 接口不删除/改名既有字段类型（规划）；不承诺 SLA，请自备缓存与降级。",
      agentDisc5:"角色切片仅改变排序与动作卡，不改变事实本身。",
      hotSearch:"大家都在搜", hotSearchTerms:[
        "分红实现率","佣金递延","演示利率上限","保费融资","GN16",
        "CPD学时","家办税务","跨境理财通","转介费","RBC"
      ],
      themesIntro:"点击主题进入全部动态并筛选。", calH:"关键节点", dailyArchive:"往期快速回看", dailyLead:"按区块聚合的专业早报。排序随角色变化。",
      evergreen:"生效中 · 常驻",
      archiveTabs:{daily:"日报",weekly:"周报",monthly:"月报",yearly:"年报"},
      downloadHint:"日报、周报可下载 Markdown。月报、年报仅可在线查阅，不提供下载。也可发送到邮箱。数字与规则以原文链接为准。",
      openDigest:"查看该期条目",
      backDownload:"返回列表",emailTo:"📧 发送到邮箱",emailSent:"已打开邮箱",emailHint:"将打开默认邮件客户端，发送日报到你的邮箱",monthlyYearlyReadOnly:"月报与年报仅可在线查阅，不提供下载。",
      guideLabel:"本站导读（非原文）",
      originalAuthority:"权威原文",
      sourceKey:"来源指纹",
      positionH:"定位",
      fidelity:"内容纪律",
      fidelityText:"我们只做资讯聚合与导读索引：不篡改原文，不建分红实现率数仓。摘要/动作卡为二次整理；数字与规则以原文链接为准。",
      itemsInPeriod:"本期条目",
      noDigest:"该周期暂无可下载内容。",
      searchDownload:"在下载包标题中筛选…",
      boardBack:"返回主题地图",
      boardCount:"条导读",
      boardViewAll:"本板块全部条目",
      boardLatest:"本板块最新",
      boardMap:"主题地图",
      boardHint:"六大板块=业务地图（导航维度）。「全部动态」=信息流细筛（信源类型×文种）。两套维度，不要当成同一个过滤器。",
      exportMd:"导出 Markdown",
      posterBtn:"朋友圈海报",
      posterTitle:"朋友圈海报",
      posterTip:"竖版 4:5，适合发朋友圈。只提炼可公开要点；不含佣金细节与收益承诺。请再人工过目。",
      posterDl:"下载 PNG",
      posterCopy:"复制文案",
      mdDone:"已下载 Markdown",
      copyDone:"文案已复制",
      pointsLabel:"积分",
      earnShare:"+5 分享",
      digestExport:"导出本期 MD",
      proLock:"Pro / 积分",
      proNeed:"需要 {n} 积分或 Pro（演示）。当前对内可关闭付费锁。",
      proFree:"免费下载",
      unlocked:"已解锁下载",
      momentsOk:"适合朋友圈",
      momentsNo:"偏专业内部，建议仅团队转发",



      facetSource:"信源", facetKind:"文种", facetHint:"细筛维度 · 与左侧「主题雷达」六大板块不同", sourcesCatalogH:"信源目录", dark:"深色", light:"浅色", week:["日","一","二","三","四","五","六"], weekPrefix:"星期"
    },
    tc: {
      brandName: "貓圈兒港險情報站", brandSub: "維港貓圈兒 · 持牌人情報台", wechat: "公眾號：維港貓圈兒",
      foot: "專業參考 · 非銷售/投資建議 · 數字請回原文", menu: "選單",
      roles: [{id:"front",label:"前線IFA"},{id:"midback",label:"中後台合規"},{id:"lead",label:"團隊管理"},{id:"cross",label:"跨境架構"}],
      nav: [
        {id:"dashboard",label:"情报看板",ico:"◉"},{id:"pulse",label:"今日脈搏",ico:"◈"},{id:"all",label:"全部動態",ico:"☰"},{id:"daily",label:"角色日報",ico:"▣"},{id:"themes",label:"主題雷達",ico:"◎"},{id:"deeps",label:"監管深度",ico:"◆"},{id:"calendar",label:"事件日曆",ico:"◷"},{id:"download",label:"數據下載",ico:"⬇"},{id:"fav",label:"收藏",ico:"☆"},{id:"agent",label:"Agent 接入",ico:"⌘"},{id:"changelog",label:"更新日誌",ico:"◌"},{id:"about",label:"關於",ico:"ⓘ"}
      ],
      sec:{c:"內容",a:"接入",m:"更多"},
      views:{
        dashboard:{t:"情報看板",s:"市場數據實時儀表板 · 源頭可溯 · 數字搬運"},pulse:{t:"今日脈搏",s:"熱點: 近14天官方高分自動上榜 · 精選: 評分×角色匹配動態排序"},
        all:{t:"全部動態",s:"全量資訊流 · 按信源/文種細篩（≠主題雷達）"},
        daily:{t:"角色日報",s:"固定節奏的專業早報"},download:{t:"數據下載",s:"按日/週/月/年打包導出 Markdown · 原文可溯"},
        themes:{t:"主題雷達",s:"六大業務板塊地圖 · 戰略導航，不是資訊流細篩"},
        deeps:{t:"監管深度",s:"重大事件完整畫像 · 時間線 · 影響矩陣 · FAQ · 關聯條目"},calendar:{t:"事件日曆",s:"關鍵事件 · 生效日 · 行業節點"},
        fav:{t:"收藏",s:"保存在本機"},
        agent:{t:"Agent 接入",s:"JSON Feed · RSS · llms.txt"},changelog:{t:"更新日誌",s:"功能與數據變更記錄"},about:{t:"關於",s:"定位、原則與免責"}
      },
      themes:{reg:"監管",product:"產品",channel:"渠道人力",macro:"宏觀資產",par:"分紅實現率",uw:"核保理賠",compliance:"合規實操",offshore:"跨境離岸",firm:"機構競爭",tech:"科技運營",career:"職業CPD",intl:"國際對標"},
      tier:{official:"一手監管",insurer:"保司官方",pro:"專業解讀",media:"媒體"},
      hot:"當前熱點", allChip:"全部", searchPh:"搜尋標題 / 摘要 / 標籤…", empty:"沒有匹配的條目。",
      verified:"已核原文", pending:"待複核", score:"評分", cluster:"源同題", why:"為什麼重要",
      actionNow:"今日動作", actionAll:"全角色動作", summary:"摘要", themesH:"主題", effective:"生效 / 相關日期",
      original:"打開原文", note:"核對提示", dayUnit:"條", roleNow:"當前角色", window:"數據窗口",
      about1:"貓圈兒港險情報站——專注香港保險監管與行業資訊的聚合導讀平台。數據來源：保監局(IA)、金管局(HKMA)、保司官網披露、國際機構研究與權威媒體線索。每條導讀均可回追原文，播報時間精確到分鐘。",
      about2:"與微信公眾號「維港貓圈兒」同一品牌人格：專業、好懂、有溫度。站點偏工具與檢索；公眾號偏解讀與陪伴。",
      qrTip:"微信掃碼關注，獲取每日港險解讀與陪伴。",
      principles:"原則", p1:"監管與保司官網資訊優先；媒體/研究作線索，必須可回原文", p2:"同一礦山，按角色切片", p3:"每條精選帶「今日動作」", p4:"摘要必須可回原文",
      disclaimer:"免責聲明", disc:"內容供香港持牌保險中介及專業人士參考，不構成銷售建議、投資建議或法律意見。請以監管與保司原文為準。",
      agentH:"如何接入", agentSub:"三條路徑規劃與 AI HOT 對齊：網頁人讀 + RSS/API + Agent Skill。當前原型以網頁為準，接口形態如下。",
      a1:"網頁：每日打開「今日脈搏 / 全部動態 / 角色日報」，用頂部角色切片視圖。",
      a2:"RSS / REST API（下一階段）：匿名只讀、穩定契約；API 輪詢建議 ≥60s，RSS ≥30 分鐘；收到 429 按 Retry-After 退避。",
      a3:"Agent Skill（下一階段）：安裝一次後用中文問「過去24小時五件大事」；返回時間窗、中文摘要與站內/原文連結。",
      agentUseH:"接入後怎麼用",
      agentUse1:"按角色提問：前線 IFA / 中後台合規 / 團隊管理 / 跨境架構。",
      agentUse2:"要時間線：例如「佣金分攤 / 轉介費 / 演示利率上限」相關規則按生效日排序。",
      agentUse3:"增量同步：首次 snapshot 全量精選，之後只拉 changes（規劃中）。",
      agentUse4:"導出：數據下載頁按日/週/月/年導出 Markdown，或單條詳情導出。",
      agentEx:"示例問法",
      agentCode:"過去 24 小時港險監管與產品最重要的 5 件事？\n只給我中後台合規視角，忽略促銷。\n佣金分攤與轉介費相關規則時間線。\n把本週精選同步成 Markdown 清單。",
      agentDiscH:"使用與免責（重要）",
      agentDisc1:"摘要與動作卡由人工/AI 二次整理，數字、政策與原話引用前必須打開原文 URL 複核。",
      agentDisc2:"對外發布請保留來源與 canonical；本站導讀不構成銷售建議、投資建議或法律意見。",
      agentDisc3:"公開可讀 ≠ 可忽略版權與頻率合同；禁止批量繞過限流的爬取。",
      agentDisc4:"v1 接口不刪除/改名既有字段類型（規劃）；不承諾 SLA，請自備緩存與降級。",
      agentDisc5:"角色切片僅改變排序與動作卡，不改變事實本身。",
      hotSearch:"大家都在搜", hotSearchTerms:[
        "分紅實現率","佣金遞延","演示利率上限","保費融資","GN16",
        "CPD學時","家辦稅務","跨境理財通","轉介費","RBC"
      ],
      themesIntro:"點擊主題進入全部動態並篩選。", calH:"關鍵節點", dailyArchive:"往期快速回看", dailyLead:"按區塊聚合的專業早報。排序隨角色變化。",
      evergreen:"生效中 · 常駐",
      archiveTabs:{daily:"日報",weekly:"週報",monthly:"月報",yearly:"年報"},
      downloadHint:"日報、週報可下載 Markdown。月報、年報僅可在線查閱，不提供下載。也可發送到郵箱。數字與規則以原文鏈接為準。",
      openDigest:"查看該期條目",
      backDownload:"返回列表",emailTo:"📧 發送到郵箱",emailSent:"已打開郵箱",emailHint:"將打開默認郵件客戶端，發送日報到你的郵箱",monthlyYearlyReadOnly:"月報與年報僅可在線查閱，不提供下載。",
      guideLabel:"本站導讀（非原文）",
      originalAuthority:"權威原文",
      sourceKey:"來源指紋",
      positionH:"定位",
      fidelity:"內容紀律",
      fidelityText:"我們只做資訊聚合與導讀索引：不篡改原文，不建分紅實現率數倉。摘要/動作卡為二次整理；數字與規則以原文連結為準。",
      itemsInPeriod:"本期條目",
      noDigest:"該週期暫無可下載內容。",
      searchDownload:"在下載包標題中篩選…",
      boardBack:"返回主題地圖",
      boardCount:"條導讀",
      boardViewAll:"本板塊全部條目",
      boardLatest:"本板塊最新",
      boardMap:"主題地圖",
      boardHint:"六大板塊=業務地圖（導航維度）。「全部動態」=資訊流細篩（信源類型×文種）。兩套維度，不要當成同一個過濾器。",
      exportMd:"導出 Markdown",
      posterBtn:"朋友圈海報",
      posterTitle:"朋友圈海報",
      posterTip:"豎版 4:5，適合發朋友圈。只提煉可公開要點；不含佣金細節與收益承諾。請再人工過目。",
      posterDl:"下載 PNG",
      posterCopy:"複製文案",
      mdDone:"已下載 Markdown",
      copyDone:"文案已複製",
      pointsLabel:"積分",
      earnShare:"+5 分享",
      digestExport:"導出本期 MD",
      proLock:"Pro / 積分",
      proNeed:"需要 {n} 積分或 Pro（演示）。當前對內可關閉付費鎖。",
      proFree:"免費下載",
      unlocked:"已解鎖下載",
      momentsOk:"適合朋友圈",
      momentsNo:"偏專業內部，建議僅團隊轉發",



      facetSource:"信源", facetKind:"文種", facetHint:"細篩維度 · 與左側「主題雷達」六大板塊不同", sourcesCatalogH:"信源目錄", dark:"深色", light:"淺色", week:["日","一","二","三","四","五","六"], weekPrefix:"星期"
    }
  };

  const state = {
    view: "pulse",
    role: (function(){ let r=localStorage.getItem("hkii_role")||"front"; if(r==="mid"||r==="back") r="midback"; if(r==="manage") r="lead"; return r; })(),
    theme: localStorage.getItem("hkii_theme") || "auto",
    lang: localStorage.getItem("hkii_lang") || "sc",
    q: localStorage.getItem("hkii_q")||"", themeFilter: localStorage.getItem("hkii_themeFilter")||"all", feedTier: localStorage.getItem("hkii_feedTier")||"all", feedKind: localStorage.getItem("hkii_feedKind")||"all", selectedId: null, archivePeriod: "daily", archiveKey: null, archiveQ: "", archivePage: 1, themeBoard: null, points: Number(localStorage.getItem("hkii_points")||"20"), pro: localStorage.getItem("hkii_pro")==="1",
    fav: new Set(JSON.parse(localStorage.getItem("hkii_fav") || "[]"))
  };

  const $ = (s, el=document) => el.querySelector(s);
  const $$ = (s, el=document) => [...el.querySelectorAll(s)];
  const T = () => L[state.lang];
  const tx = (o) => !o ? "" : (typeof o === "string" ? o : (o[state.lang] || o.sc || o.tc || ""));
  const esc = (s) => String(s??"").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");

  // Auto theme listener
  if(!window._themeListenerAdded){
    window._themeListenerAdded = true;
    window.matchMedia("(prefers-color-scheme: light)").addEventListener("change", () => {
      if(state.theme === "auto") applyChrome();
    });
  }
  function applyChrome() {
    const t = T();
    document.documentElement.lang = state.lang === "tc" ? "zh-Hant" : "zh-Hans";
    const effectiveTheme = state.theme === "auto" 
      ? (window.matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark")
      : state.theme;
    document.documentElement.setAttribute("data-theme", effectiveTheme);
    document.title = t.brandName;
    $("#brandName").textContent = t.brandName;
    $("#brandSub").textContent = t.brandSub;
    $("#wechatPill").textContent = t.wechat;
    $("#footNote").textContent = t.foot;
    const pb=$("#pointsBar");
    if(pb){ pb.textContent = ""; }
    $("#menuBtn").textContent = t.menu;
    $("#q").placeholder = t.searchPh;
    // 大家都在搜 dropdown
    const hd=$("#hotsearchDropdown"); const hl=$("#hotsearchList");
    if(hd&&hl&&t.hotSearchTerms){
      hl.innerHTML=t.hotSearchTerms.map((x,i)=>`<span class="hotsearch-item" data-hotsearch="${x}"><span class="rank">${i+1}</span>${x}</span>`).join("");
    }
    // Search box focus/blur for dropdown
    const qEl=$("#q"); const sb=$("#searchBox");
    if(qEl&&!qEl._hsBound){
      qEl._hsBound=true;
      qEl.addEventListener("focus",()=>{ if(hd) hd.style.display=""; });
      qEl.addEventListener("blur",()=>{ setTimeout(()=>{ if(hd) hd.style.display="none"; },200); });
    }
    $$("[data-lang]").forEach(b => b.classList.toggle("on", b.dataset.lang === state.lang));
    $$("[data-theme-btn]").forEach(b => {
      b.classList.toggle("on", b.dataset.themeBtn === state.theme);
      b.textContent = b.dataset.themeBtn === "dark" ? t.dark : (b.dataset.themeBtn === "light" ? t.light : "跟随系统");
    });
    const n = t.nav;
    $("#nav").innerHTML = `
      <div class="nav-section">${t.sec.c}</div>
      ${n.slice(0,9).map(x=>`<button class="nav-item ${state.view===x.id?'active':''}" data-view="${x.id}"><span class="ico">${x.ico}</span>${x.label}</button>`).join("")}
      <div class="nav-section">${t.sec.a}</div>
      ${n.slice(9,11).map(x=>`<button class="nav-item ${state.view===x.id?'active':''}" data-view="${x.id}"><span class="ico">${x.ico}</span>${x.label}</button>`).join("")}
      <div class="nav-section">${t.sec.m}</div>
      ${n.slice(11).map(x=>`<button class="nav-item ${state.view===x.id?'active':''}" data-view="${x.id}"><span class="ico">${x.ico}</span>${x.label}</button>`).join("")}`;
    $("#rolePills").innerHTML = t.roles.map(r => `<button type="button" class="pill ${state.role===r.id?'on':''}" data-role="${r.id}">${r.label}</button>`).join("");
  }

  const byId = id => DATA.items.find(x => x.id === id);
  const roleScore = it => ((it.rolesImpact&&it.rolesImpact[state.role])||0)*6 + (it.score||70) + (it.featured?4:0);
  function matches(it) {
    if (!state.q.trim()) return true;
    const q = state.q.trim().toLowerCase();
    const tags = (it.tags && (it.tags[state.lang]||it.tags.sc)) || [];
    return [tx(it.title), tx(it.summary), tx(it.why), tags.join(" ")].join(" ").toLowerCase().includes(q);
  }
  // Fav tags
  state.favTag = null;

  function favTags() {
    const items = DATA.items.filter(i => state.fav.has(i.id));
    const tags = new Set();
    for (const it of items) {
      for (const t of (it.tags||{}).sc||[]) tags.add(t);
    }
    return [...tags].sort();
  }

  function list({featuredOnly=false,favOnly=false,forceTime=false,pulseSort=false,roleWeights=null,items:extItems=null,page=1,pageSize=20}={}) {
    let arr = (DATA.items||[]).slice();
    if (favOnly) {
      arr = arr.filter(i=>state.fav.has(i.id));
      if (state.favTag) {
        arr = arr.filter(i => ((i.tags||{}).sc||[]).includes(state.favTag));
      }
    }
    // 全部动态：信源 × 文种（细维度）
    if (state.view === "all") {
    const q0 = (state.searchQuery||'').trim().toLowerCase();
    if(q0){
      const raw = searchItems(q0, DATA.items||[]);
      html+=`<div class="search-results">搜索「${esc(q0)}」· 找到 ${raw.length} 条</div>`;
      html+=feed(list({items:raw,page:state.allPage,pageSize:state.allPageSize}, t));
    }
      if (state.feedTier && state.feedTier !== "all") arr = arr.filter(i => i.sourceTier === state.feedTier);
      if (state.feedKind && state.feedKind !== "all") arr = arr.filter(i => (i.contentKind || "other") === state.feedKind);
    } else if (state.themeFilter && state.themeFilter !== "all") {
      // 脉搏等：仍可用主题码（非六大板块）
      arr = arr.filter(i => (i.themes || []).includes(state.themeFilter) || (i.boards || []).includes(state.themeFilter));
    }
    arr = arr.filter(matches);
    // 今日脉搏：动态评分排序
  if (pulseSort && roleWeights) {
    arr = arr.filter(i => (i.score||0) >= 80);
    arr.sort((a,b) => {
      const sa = (a.score||0)*0.7 + ((a.rolesImpact||{}).front||0)*(roleWeights.front||0) + ((a.rolesImpact||{}).midback||0)*(roleWeights.midback||0) + ((a.rolesImpact||{}).lead||0)*(roleWeights.lead||0) + ((a.rolesImpact||{}).cross||0)*(roleWeights.cross||0);
      const sb = (b.score||0)*0.7 + ((b.rolesImpact||{}).front||0)*(roleWeights.front||0) + ((b.rolesImpact||{}).midback||0)*(roleWeights.midback||0) + ((b.rolesImpact||{}).lead||0)*(roleWeights.lead||0) + ((b.rolesImpact||{}).cross||0)*(roleWeights.cross||0);
      return sb - sa;
    });
    return arr.slice(0,50);
  }
  // 收藏：支持标签筛选；筛选不改变排序键
    if (forceTime || true) {
      arr.sort((a,b)=> (b.publishedAt||"").localeCompare(a.publishedAt||"") || (b.score||0)-(a.score||0));
    } else {
      arr.sort((a,b)=> roleScore(b)-roleScore(a) || (b.publishedAt||"").localeCompare(a.publishedAt||""));
    }
    return arr;
  }
  function byPublishedDesc(a,b){
    return (b.publishedAt||"").localeCompare(a.publishedAt||"") || (b.score||0)-(a.score||0);
  }
  function fmtTime(iso){
    if(!iso) return "";
    // 优先用字符串内时间，避免 UTC 偏移导致「时间乱」
    const m = String(iso).match(/T(\d{2}):(\d{2})/);
    if(m) return m[1]+":"+m[2];
    const d=new Date(iso); return String(d.getHours()).padStart(2,"0")+":"+String(d.getMinutes()).padStart(2,"0");
  }
    function fmtCardTime(it){
    const iso=it.publishedAt||"";
    const m=String(iso).match(/T(\d{2}):(\d{2})/);
    if(m) return m[1]+":"+m[2];
    // If no time, try to show nothing (date-only items)
    if(iso&&iso.length>=10) return "";
    return "";
  }
function fmtDay(iso){
    const t=T();
    const key = (String(iso||"").match(/^(\d{4}-\d{2}-\d{2})/)||[])[1] || "";
    let d;
    if(key){
      const [y,mo,da] = key.split("-").map(Number);
      d = new Date(y, mo-1, da); // 本地日历日
    } else {
      d = new Date(iso);
    }
    const labelKey = key || d.toISOString().slice(0,10);
    return {key:labelKey, label:`${d.getMonth()+1}月${d.getDate()}日`, week:t.weekPrefix+t.week[d.getDay()]};
  }
  function dots(n){ n=n||0; return "●".repeat(n)+"○".repeat(Math.max(0,3-n)); }

  function card(it){
    const t=T();
    const imp=(it.rolesImpact&&it.rolesImpact[state.role])||0;
    const tags=((it.tags&&(it.tags[state.lang]||it.tags.sc))||[]).slice(0,3).map(x=>`<span class="tag">${esc(x)}</span>`).join("");
    return `<article class="card ${state.selectedId===it.id?'selected':''}" data-id="${it.id}">
      <div class="card-time" title="${it.publishedAt||""}">${fmtCardTime(it)}</div>
      <div class="card-body">
        <h3 class="card-title">${esc(tx(it.title))}</h3>
        <p class="card-sum">${esc(tx(it.summary))}</p>
        <div class="meta-row">
          <span class="badge badge-score">${it.score}</span>
          <span class="badge ${it.sourceTier}">${t.tier[it.sourceTier]||it.sourceTier}</span>
          <span class="badge verify-${it.verifyStatus}">${it.verifyStatus==='verified'?t.verified:t.pending}</span>
          ${tags.slice(0,1)}
        </div>
      </div>
      <div class="card-side">
        <button type="button" class="star ${state.fav.has(it.id)?'on':''}" data-fav="${it.id}">☆</button>
        <div class="impact">${dots(imp)}</div>
      </div>
    </article>`;
  }
  const _dayCollapsed = {};
  function feed(items, opts){
    const t=T();
    if(!items || !items.length) return `<div class="empty">${t.empty}</div>`;
    const preserve = opts && opts.preserveOrder;
    const sorted = preserve ? items.slice() : items.slice().sort(byPublishedDesc);
    const map=new Map();
    sorted.forEach(it=>{const d=fmtDay(it.publishedAt); if(!map.has(d.key)) map.set(d.key,{meta:d,items:[]}); map.get(d.key).items.push(it);});
    const groups = [...map.values()].sort((a,b)=> (b.meta.key||"").localeCompare(a.meta.key||""));
    groups.forEach(g=> { if(!preserve) g.items.sort(byPublishedDesc); });
    return groups.map(g=>{
      const collapsed = _dayCollapsed[g.meta.key];
      return `<div class="day-head" data-day-toggle="${g.meta.key}" style="cursor:pointer">
        <h3>${g.meta.label}</h3>
        <span>${g.meta.week} · ${g.items.length} ${t.dayUnit} ${collapsed?"▸":"▾"}</span>
      </div>${collapsed?"":g.items.map(card).join("")}`;
    }).join("");
  }
  // Day collapse handler
  document.addEventListener("click", function(e){
    const dd=e.target.closest("[data-daily-date]"); if(dd){ state.q=dd.dataset.dailyDate; document.getElementById("q").value=state.q; render(); return; }
    const dt=e.target.closest("[data-day-toggle]");
    if(dt){ const k=dt.dataset.dayToggle; _dayCollapsed[k]=!_dayCollapsed[k]; render(); }
  });
  function chips(active){
    const t=T();
    // 全部动态：信源 × 文种（与主题雷达六大板块刻意分离）
    if(state.view === "all"){
      const facets = DATA.feedFacets || {};
      const tiers = facets.sourceTiers || [];
      const kinds = facets.contentKinds || [];
      // Primary: source tiers only (most common filter)
      const tierRow = tiers.map(f=>`<button type="button" class="chip ${state.feedTier===f.id?'on':''}" data-feed-tier="${f.id}">${f.icon||""} ${esc(tx(f.title))}</button>`).join("");
      // Secondary: content kinds (collapsed by default)
      const kindRow = kinds.map(f=>`<button type="button" class="chip chip-secondary ${state.feedKind===f.id?'on':''}" data-feed-kind="${f.id}">${f.icon||""} ${esc(tx(f.title))}</button>`).join("");
      return `<div class="facet-stack">
        <div class="chips facet-main">${tierRow}</div>
        <div class="facet-more" id="facetMore" style="display:none"><div class="chips">${kindRow}</div></div>
        <button type="button" class="chip chip-toggle-more" id="facetToggle">文种 ▾</button>
      </div>`;
    }
    // 脉搏等：用 12 主题细码（仍不等于六大板块地图）
    return `<div class="chips"><button type="button" class="chip ${active==='all'||!active?'on':''}" data-theme-filter="all">${t.allChip}</button>${Object.entries(t.themes).map(([k,v])=>`<button type="button" class="chip ${active===k?'on':''}" data-theme-filter="${k}">${v}</button>`).join("")}</div>`;
  }
  function hotSearchChips(){
    const t=T();
    const terms=t.hotSearchTerms||[];
    if(!terms.length) return "";
    return `<div class="hotsearch-row"><span class="hotsearch-label">${t.hotSearch||"大家都在搜"}</span><div class="chips" style="margin-bottom:0">${terms.map((x,i)=>`<button type="button" class="chip chip-hot" data-hot="${x}">${i+1}. ${x}</button>`).join("")}</div></div>`;
  }
  function hot(){
    const t=T();
    // 自动计算：近14天 + score>=85 + sourceTier=official，最多6条
    const now = new Date();
    const weekAgo = new Date(now.getTime() - 14*24*3600*1000).toISOString().slice(0,10);
    const candidates = (DATA.items||[]).filter(i => {
      const d = (i.publishedAt||'').slice(0,10);
      return d >= weekAgo && (i.score||0) >= 85 && (i.sourceTier||'') === 'official';
    });
    candidates.sort((a,b) => (b.score||0) - (a.score||0));
    const items = candidates.slice(0,6);
    if(!items.length) return "";
    return `<section class="hot"><div class="hot-label">${t.hot}<span class="hot-auto"> · 自动</span></div><ol>${items.map((it,i)=>`<li><button type="button" data-open="${it.id}">${esc(tx(it.title))}</button></li>`).join("")}</ol></section>`;
  }

  function render(){
    applyChrome();
    const t=T();
    const meta=t.views[state.view]||t.views.pulse;
    const roleLabel=(t.roles.find(r=>r.id===state.role)||{}).label||"";
    $("#viewTitle").textContent=meta.t;
    $("#viewSub").textContent=`${meta.s} · ${t.roleNow}：${roleLabel}`;
    let html="";
    if(DATA.meta&&DATA.meta.windowNote) html+=`<div class="note-bar"><strong>${t.window}</strong> · ${esc(tx(DATA.meta.windowNote))}</div>`;
    if(state.view==="dashboard"){
      const t=T();
      html+=`<div class="dash-section" style="margin-bottom:32px">
        <div class="dash-hero">
          <h2 style="font-size:24px;font-weight:700;letter-spacing:-0.02em;margin:0 0 4px">情报看板</h2>
          <p style="color:var(--text-muted);font-size:13px;margin:0">市场数据实时仪表板 · 源头可溯 · 每条数字可回追</p>
        </div>
      </div>`;
      const st=DATA.stats||{};
      // Market Pulse
      const mp=st.marketPulse; if(mp&&mp.items){
        html+=`<div class="dash-section"><div class="dash-section-title">${esc(tx(mp.title))}</div>
        <div class="dash-grid dash-grid-3">${mp.items.map(s=>{
          const ti=s.trend==="up"?"↗":s.trend==="down"?"↘":"→";
          const tc=s.trend==="up"?"var(--ok)":s.trend==="down"?"var(--warn)":"var(--text-dim)";
          return '<div class="dash-card"><div class="dash-label">'+esc(tx(s.label))+'</div><div class="dash-value">'+s.value+' <span class="dash-unit">'+esc(tx(s.unit))+'</span></div><div class="dash-change" style="color:'+tc+'">'+ti+' '+s.change+' <span class="dash-clabel">'+esc(tx(s.changeLabel))+'</span></div><p class="dash-note">'+esc(tx(s.note))+'</p><div class="dash-source"><a href="'+s.sourceUrl+'" target="_blank" rel="noopener">'+s.source+'</a> · '+esc(tx(s.asOf))+'</div></div>';
        }).join("")}</div></div>`;
      }
      // Family Office
      const fo=st.familyOffice; if(fo&&fo.items){
        html+=`<div class="dash-section"><div class="dash-section-title">${esc(tx(fo.title))}</div>
        <div class="dash-grid dash-grid-3">${fo.items.map(s=>{
          const ti=s.trend==="up"?"↗":s.trend==="down"?"↘":"→";
          const tc=s.trend==="up"?"var(--ok)":s.trend==="down"?"var(--warn)":"var(--text-dim)";
          return '<div class="dash-card"><div class="dash-label">'+esc(tx(s.label))+'</div><div class="dash-value">'+s.value+' <span class="dash-unit">'+esc(tx(s.unit))+'</span></div><div class="dash-change" style="color:'+tc+'">'+ti+' '+s.change+' <span class="dash-clabel">'+esc(tx(s.changeLabel))+'</span></div><p class="dash-note">'+esc(tx(s.note))+'</p><div class="dash-source"><a href="'+s.sourceUrl+'" target="_blank" rel="noopener">'+s.source+'</a> · '+esc(tx(s.asOf))+'</div></div>';
        }).join("")}</div></div>`;
      }
      // Channel
      const cl=st.channelLandscape; if(cl&&cl.items){
        html+=`<div class="dash-section"><div class="dash-section-title">${esc(tx(cl.title))}</div>
        <div class="dash-grid dash-grid-3">${cl.items.map(s=>{
          const ti=s.trend==="up"?"↗":s.trend==="down"?"↘":"→";
          const tc=s.trend==="up"?"var(--ok)":s.trend==="down"?"var(--warn)":"var(--text-dim)";
          return '<div class="dash-card"><div class="dash-label">'+esc(tx(s.label))+'</div><div class="dash-value">'+s.value+' <span class="dash-unit">'+esc(tx(s.unit))+'</span></div><div class="dash-change" style="color:'+tc+'">'+ti+' '+s.change+' <span class="dash-clabel">'+esc(tx(s.changeLabel))+'</span></div><p class="dash-note">'+esc(tx(s.note))+'</p><div class="dash-source"><a href="'+s.sourceUrl+'" target="_blank" rel="noopener">'+s.source+'</a> · '+esc(tx(s.asOf))+'</div></div>';
        }).join("")}</div></div>`;
      }
      // Regulatory Clock
      const rc=st.regulatoryClock; if(rc&&rc.events){
        html+=`<div class="dash-rule"></div><div class="dash-section"><div class="dash-section-title">${esc(tx(rc.title))}</div><p class="dash-subtitle">${esc(tx(rc.subtitle))}</p>
        <div class="clock-timeline">${rc.events.map((e,i)=>{
          const stars="★★★★★".slice(0,e.impact);
          const it2=e.itemId?byId(e.itemId):null;
          return `<div class="clock-item"><div class="clock-dot ${i===0?'clock-dot-first':i===rc.events.length-1?'clock-dot-last':''}"></div><div class="clock-date">${e.date}</div><div class="clock-body"><div class="clock-cat">${esc(tx(e.category))}</div><div class="clock-title">${esc(tx(e.title))}</div><div class="clock-impact">${stars}</div><p class="clock-desc">${esc(tx(e.desc))}</p>${it2?`<a class="clock-link" data-open="${e.itemId}">查看详情 →</a>`:""}</div></div>`;
        }).join("")}</div></div>`;
      }
      // Insurer Rankings
      const ir=st.insurerRankings; if(ir&&ir.rankings){
        html+=`<div class="dash-rule"></div><div class="dash-section"><div class="dash-section-title">${esc(tx(ir.title))}</div><p class="dash-subtitle">${esc(tx(ir.subtitle))}</p>
        <div class="rank-table-wrap"><table class="rank-table">
          <thead><tr><th>#</th><th>保司</th><th>市占率</th><th>信评</th><th>备注</th></tr></thead>
          <tbody>${ir.rankings.map(r=>{
            const ti2=r.trend==="up"?"↗":r.trend==="down"?"↘":"→";
            const tc2=r.trend==="up"?"var(--ok)":r.trend==="down"?"var(--warn)":"var(--text-dim)";
            return `<tr><td class="rank-num">${r.rank}</td><td class="rank-name"><span class="rank-en">${r.name}</span><span class="rank-zh">${esc(tx(r.nameZH))}</span></td><td class="rank-share">${r.share}</td><td class="rank-rating ${r.rating!=='NR'?'rating-strong':''}">${r.rating}</td><td class="rank-note">${esc(tx(r.note))}</td></tr>`;
          }).join("")}</tbody></table></div>
          <p style="font-size:11px;color:var(--text-dim);margin:8px 0 0">市占率: <a href="${ir.sourceUrl||''}">IA Annual Stats</a> · 信评: <a href="${ir.ratingUrl||''}">S&P Global</a></p></div>`;
      }
      // Company DNA
      const cd=st.companyDNA; if(cd&&cd.rows){
        html+=`<div class="dash-rule"></div><div class="dash-section"><div class="dash-section-title">${esc(tx(cd.title))}</div><p class="dash-subtitle">${esc(tx(cd.subtitle))}</p>
        <div style="display:flex;flex-wrap:wrap;gap:10px;margin-bottom:10px">${["agent-dominant","bank-dominant","broker-dominant","hybrid"].map(a=>{
          const rows=cd.rows.filter(r=>r.archetype===a);
          const label={["agent-dominant"]:"代理派",["bank-dominant"]:"银保派",["broker-dominant"]:"经纪派",["hybrid"]:"混合派"}[a];
          return `<div style="flex:1;min-width:200px;padding:12px;border:1px solid var(--border-soft);border-radius:10px;background:var(--bg-soft)">
            <div style="font-size:11px;color:var(--accent);font-weight:600;margin-bottom:6px">${label} · ${rows.length}家</div>
            ${rows.map(r=>`<div style="font-size:13px;font-weight:600;margin:4px 0">${r.company} <span style="font-size:11px;color:var(--text-dim)">${r.gross2025}亿</span></div><div style="font-size:11px;color:var(--text-muted);margin-bottom:2px">${esc(tx(r.note))}</div>`).join("")}</div>`;
        }).join("")}</div>
        <p style="font-size:11px;color:var(--text-dim);margin:8px 0 0">${esc(tx(cd.calcNote))} · <a href="${cd.sourceUrl}" target="_blank" rel="noopener">${cd.sourceLabel}</a></p></div>`;
      }
      // Talent Flow
      const tf=st.talentFlow; if(tf&&tf.liveData){
        html+=`<div class="dash-rule"></div><div class="dash-section"><div class="dash-section-title">${esc(tx(tf.title))}</div><p class="dash-subtitle">${esc(tx(tf.subtitle))}</p>
        <div class="dash-grid dash-grid-3">
          <div class="dash-card"><div class="dash-label">持牌总人数(个人)</div><div class="dash-value" style="font-size:36px">${(tf.liveData.totalIndividuals/1000).toFixed(0)}<span class="dash-unit">k</span></div><p class="dash-note">截至 ${tf.liveData.date} · IA 实时</p></div>
          <div class="dash-card"><div class="dash-label">持牌经纪(Tech Rep)</div><div class="dash-value" style="font-size:36px">${(tf.liveData.techRepBroker/1000).toFixed(1)}<span class="dash-unit">k</span></div><div class="dash-change" style="color:var(--ok)">↗ 最快增速 · 3年 +37.1%</div></div>
          <div class="dash-card"><div class="dash-label">保险代理(Licensed Agent)</div><div class="dash-value" style="font-size:36px">${(tf.liveData.agents/1000).toFixed(0)}<span class="dash-unit">k</span></div><div class="dash-change" style="color:var(--text-dim)">→ 稳中有降</div></div>
        </div>
        <p style="font-size:11px;color:var(--text-dim);margin:8px 0 0">${esc(tx(tf.calcNote))} · <a href="${tf.sourceUrl}" target="_blank" rel="noopener">${tf.sourceLabel}</a></p></div>`;
      }
      // Intelligence Density
      const iden=st.intelligence; if(iden){ const _total=(DATA.items||[]).length||iden.totalItems||0;
        html+=`<div class="dash-rule"></div><div class="dash-section"><div class="dash-section-title">${esc(tx(iden.title))}</div><p class="dash-subtitle">${esc(tx(iden.subtitle))}</p>
        <div class="dash-grid dash-grid-2">
          <div class="dash-card"><div class="dash-label">累计条目</div><div class="dash-value" style="font-size:40px">${_total} <span class="dash-unit">条</span></div><p class="dash-note">${esc(tx(iden.dateRange))}</p></div>
          <div class="dash-card"><div class="dash-label">信源分布</div><div class="tier-bars">${(iden.sourceTiers||[]).map(t=>{
            const pct=Math.round(t.count/_total*100);
            return `<div class="tier-bar-row"><span class="tier-label">${t.label||t.tier}</span><div class="tier-bar-bg"><div class="tier-bar-fill" style="width:${pct}%"></div></div><span class="tier-count">${t.count}</span></div>`;
          }).join("")}</div></div>
        </div>
        <div class="dash-card" style="margin-top:10px"><div class="dash-label">主题热度 Top 10</div>
        <div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:8px">${(iden.topThemes||[]).map(t=>'<span style="font-size:13px;color:var(--accent);background:var(--accent-dim);padding:3px 8px;border-radius:6px">'+(t.label||t.theme)+' '+t.count+'</span>').join("")}</div></div></div>`;
      }
      // Footer
      const ds=st.dataSummary; if(ds){
        html+=`<div class="dash-rule"></div><div class="dash-section"><div class="dash-section-title">${esc(tx(ds.title))}</div>
        <div class="dash-summary">${(ds.notes||[]).map(n=>`<li>${esc(tx(n))}</li>`).join("")}</div></div>`;
      }
    }
    else if(state.view==="pulse"){
      // evergreen
      const eg=(DATA.evergreen||[]).map(byId).filter(Boolean).filter(matches);
      if(eg.length){
        html+=`<div class="evergreen-banner-wrapper"><h3>${t.evergreen}</h3><p class="evergreen-hint">← 滑动查看 · 驻点：持续有效的监管规则与长期适用的披露要求 →</p><div class="evergreen-scroll"><button class="evergreen-scroll-btn" onclick="this.nextElementSibling.scrollBy({left:-300,behavior:'smooth'})">‹</button><div class="evergreen-banner">${eg.map(it=>`<div class="banner-card" data-open="${it.id}"><div class="banner-tag">常驻</div><h4>${esc(tx(it.title))}</h4><p>${esc(tx(it.summary))}</p></div>`).join("")}</div><button class="evergreen-scroll-btn" onclick="this.previousElementSibling.scrollBy({left:300,behavior:'smooth'})">›</button></div></div>`;
      }
      // Dynamic scoring: score × 0.7 + roleMatch × 0.3
      const roleWeights = {front:0,midback:0,lead:0,cross:0};
      if(state.role==='front'){roleWeights.front=3;roleWeights.midback=1;}
      else if(state.role==='midback'){roleWeights.midback=3;roleWeights.front=1;roleWeights.lead=1;}
      else if(state.role==='lead'){roleWeights.lead=3;roleWeights.front=1;roleWeights.cross=1;}
      else if(state.role==='cross'){roleWeights.cross=3;roleWeights.lead=1;roleWeights.front=1;}
      const pulseList = list({pulseSort:true, roleWeights:roleWeights});
      html+=hot()+chips(state.themeFilter)+feed(pulseList, {preserveOrder:true});
    }
    else if(state.view==="all"){
      const cat = DATA.meta && DATA.meta.sourcesCatalog;
      if(cat){
        html += `<div class="panel sources-panel"><h3>${esc(t.sourcesCatalogH||"信源目录")}</h3>
          <p class="sources-principle">${esc(tx(cat.principle||{}))}</p>
          <div class="sources-layers">${(cat.layers||[]).map(layer=>`<div class="sources-layer">
            <div class="sources-layer-title">${esc(tx(layer.title))}</div>
            <div class="sources-layer-note">${esc(tx(layer.countNote||{}))}${(layer.items&&layer.items.length)? " · " + layer.items.join(" · "):""}</div>
          </div>`).join("")}</div>
        </div>`;
      }
      html+=chips(state.themeFilter)+feed(list());
    }
    else if(state.view==="fav") {
      const ft = favTags();
      if(ft.length){
        html+=`<div class="tag-chips" style="margin:0 0 12px">
          <span class="tag-chip ${!state.favTag?'on':''}" data-favtag="">全部</span>
          ${ft.map(t=>`<span class="tag-chip ${state.favTag===t?'on':''}" data-favtag="${esc(t)}">${t}</span>`).join("")}
        </div>`;
      }
      html+=feed(list({favOnly:true}));
    }
    else if(state.view==="daily"){
      const d=DATA.daily||{date:"",sections:[]};
      html+=`<div class="panel"><h3>${meta.t} · ${esc(d.date||"")}</h3><p>${t.dailyLead}</p></div>`;
      (d.sections||[]).forEach(sec=>{
        const items=(sec.itemIds||[]).map(byId).filter(Boolean).filter(matches);
        html+=`<div class="day-head"><h3>${esc(tx(sec.title))}</h3><span>${items.length} ${t.dayUnit}</span></div>${items.map(card).join("")||`<div class="empty">${t.empty}</div>`}`;
      });
    } else if(state.view==="deeps"){
      const cards = DATA.deepCards || [];
      if(state.themeBoard){
        const dc = cards.find(x=>x.id===state.themeBoard);
        if(!dc){ html+=`<div class="empty">未找到深度卡</div>`; }
        else {
          const items = (dc.timeline||[]).map(t=>byId(t.itemId)).filter(Boolean);
          html+=`<div class="deep-hero">
            <button type="button" class="pill" data-board-back="1">← 返回</button>
            <h3>${esc(tx(dc.title))}</h3>
            <p class="deep-subtitle">${esc(tx(dc.subtitle))}</p>
            <p class="deep-summary">${esc(tx(dc.summary))}</p>
            <div class="deep-impact">
              ${['front','midback','lead','cross'].map(r=>{
                const label=((t.roles||[]).find(x=>x.id===r)||{}).label||r;
                const txt=tx((dc.impact||{})[r]);
                if(!txt) return '';
                return `<div class="deep-role"><strong>${label}</strong><p>${esc(txt)}</p></div>`;
              }).join('')}
            </div>
            <h4>FAQ</h4>
            <div class="deep-faq">${(dc.faq||[]).map(f=>`<details><summary>${esc(tx(f.q))}</summary><p>${esc(tx(f.a))}</p></details>`).join('')}</div>
          </div>`;
          html+=`<div class="day-head"><h3>关联条目</h3><span>${items.length} 条</span></div>`;
          html+=items.length ? feed(items) : `<div class="empty">暂无</div>`;
        }
      } else {
        html+=`<div class="taxon-head">
          <h3 style="font-size:20px">监管深度</h3>
          <p>重大监管事件的完整画像：时间线、影响矩阵、FAQ、关联条目</p>
        </div>`;
        html+=`<div class="deep-grid">`+cards.map(dc=>{
          const count=(dc.timeline||[]).filter(t=>byId(t.itemId)).length;
          return `<button type="button" class="deep-card" data-board="${dc.id}">
            <div class="deep-card-title">${esc(tx(dc.title))}</div>
            <p class="deep-card-sub">${esc(tx(dc.subtitle))}</p>
            <p class="deep-card-summary">${esc(tx(dc.summary)).slice(0,120)}</p>
            <div class="deep-card-meta"><span>${count} 条关联</span><span>${(dc.faq||[]).length} 条 FAQ</span></div>
          </button>`;
        }).join("")+`</div>`;
      }
    }
    else if(state.view==="themes"){
      const boards = DATA.boards || [];
      const byBoard = (bid) => DATA.items.filter(it => (it.boards||[]).includes(bid)).filter(matches)
        .sort((a,b)=> (b.publishedAt||"").localeCompare(a.publishedAt||"") || (b.score||0)-(a.score||0));

      if(state.themeBoard){
        const b = boards.find(x=>x.id===state.themeBoard) || {id:state.themeBoard,title:{sc:state.themeBoard},desc:{sc:""},subs:[]};
        const its = byBoard(state.themeBoard);
        html += `<div class="taxon-hero">
          <button type="button" class="pill" data-board-back="1">← ${t.boardBack||"返回"}</button>
          <h3>${esc(tx(b.title))}</h3>
          <p>${esc(tx(b.desc)||"")}</p>
          <div class="taxon-subs">${(b.subs||[]).map(s=>`<span class="chip chip-sub" data-theme-filter="${s}">#${s}</span>`).join(" ")}</div>
          <p style="font-size:12px;color:var(--text-dim);margin-top:8px">${its.length} ${t.boardCount||"条导读"}</p>
        </div>`;
        html += its.length ? feed(its) : `<div class="empty">${t.empty}</div>`;
      } else {
        html += `<div class="taxon-head">
          <h3>${meta.t}</h3>
          <p>${meta.s}</p>
          <p class="taxon-hint">${t.boardHint||""}</p>
        </div>`;
        html += `<div class="taxon-grid">` + boards.map(b=>{
          const n = byBoard(b.id).length;
          return `<button type="button" class="taxon-card" data-board="${b.id}">
            <div class="taxon-name">${esc(tx(b.title))}</div>
            <div class="taxon-n">${n} 条</div>
            <p class="taxon-desc">${esc(tx(b.desc)||"")}</p>
            <div class="taxon-subs">${(b.subs||[]).slice(0,5).map(s=>`<span class="tag tag-clickable" data-theme-filter="${s}">${s}</span>`).join(" ")}</div>
          </button>`;
        }).join("") + `</div>`;
      }
    } else if(state.view==="calendar"){
      html+=`<div class="panel"><h3>${t.calH}</h3>${(DATA.calendar||[]).map(c=>{
        const linked=c.itemId&&byId(c.itemId);
        return linked
          ? `<div class="cal-item cal-link" data-open="${c.itemId}" title="点击查看关联资讯"><div class="cal-date">${esc(c.date)}</div><div>${esc(tx(c.title))} <span class="tag">${esc(t.themes[c.theme]||"")}</span> <span class="cal-jump">↗</span></div></div>`
          : `<div class="cal-item"><div class="cal-date">${esc(c.date)}</div><div>${esc(tx(c.title))} <span class="tag">${esc(t.themes[c.theme]||"")}</span></div></div>`;
      }).join("")}</div>`;
    } 
    else if(state.view==="download"){
      const periods=["daily","weekly","monthly","yearly"];
      html+=`<div class="panel"><h3>${meta.t}</h3><p>${t.downloadHint||t.archiveHint||""}</p>
        <div class="chips">${periods.map(p=>`<button type="button" class="chip ${state.archivePeriod===p?'on':''}" data-arch-period="${p}" data-reset-page="1">${t.archiveTabs[p]}</button>`).join("")}</div>
      </div>`;
      const digests=(DATA.digests&&DATA.digests[state.archivePeriod])||[];
      if(state.archiveKey){
        const dig=digests.find(x=>x.key===state.archiveKey);
        if(!dig){ html+=`<div class="empty">${t.noDigest}</div>`; }
        else {
          const gate=canExportDigest(state.archivePeriod);
          const price=(mon().prices&&mon().prices[state.archivePeriod])||0;
          const exportLabel = gate.readonlyNote? t.digestExport : ((!mon().enabled || gate.free) ? t.digestExport : (gate.ok? `${t.digestExport}` : `${t.digestExport} · ${t.proLock}`));
          html+=`<div class="panel"><button type="button" class="pill" data-arch-back="1">← ${t.backDownload}</button>
            <h3 style="margin-top:12px">${esc(tx(dig.label))}</h3>
            <p>${t.itemsInPeriod}：${dig.itemCount} · ${esc(tx(dig.note||{}))}</p>
            ${gate.reason==="readonly"?`<p class="lock-note" style="margin:8px 0">📖 ${t.monthlyYearlyReadOnly||"月报与年报仅可在线查阅，不提供下载。"}</p>`:
            `<div class="action-bar">
              <button type="button" class="btn primary" data-export-digest="1" title="导出当前筛选结果为Markdown">${t.digestExport} · MD</button>
              <button type="button" class="btn" data-email-digest="1" title="打开默认邮件客户端">📧 ${t.emailTo}</button>
            </div>
            <div class="email-box" style="display:none;margin:8px 0">
              <input type="email" class="email-input" placeholder="${t.emailHint}" />
              <button type="button" class="btn" data-email-send="1">${t.emailSent}</button>
            </div>`}
            </div>`;
          const ids=dig.itemIds||[];
          const its=ids.map(byId).filter(Boolean).filter(matches);
          html+=feed(its);
        }
      } else {
        const q=(state.archiveQ||"").trim().toLowerCase();
        let list=digests;
        if(q) list=list.filter(x=>tx(x.label).toLowerCase().includes(q)||tx(x.leadTitle||{}).toLowerCase().includes(q));
        html+=`<div class="search-box" style="margin-bottom:12px;max-width:420px"><span style="color:var(--text-dim)">⌕</span>
          <input id="archQ" type="search" placeholder="${t.searchDownload||t.searchArchive||""}" value="${esc(state.archiveQ||"")}" /></div>`;
        const total=list.length;
        const pages=Math.ceil(total/25);
        const start=(state.archivePage-1)*25;
        const paged=list.slice(start,start+25);
        html+=`<div style="font-size:12px;color:var(--text-dim);margin-bottom:8px">共 ${total} 期，第 ${state.archivePage}/${pages} 页</div>`;
        if(!paged.length) html+=`<div class="empty">${t.noDigest}</div>`;
        else {
          const maxCount = Math.max(...paged.map(d=>d.itemCount||1));
          html+=`<div class="arch-list">`+paged.map(dig=>{
            const lead=tx(dig.leadTitle||{})||"";
            const barW = Math.min(100, (dig.itemCount/maxCount)*100);
            return `<button type="button" class="arch-row" data-arch-key="${esc(dig.key)}">
              <div class="arch-date">${esc(tx(dig.label))}</div>
              <div class="arch-lead">${esc(lead)}</div>
              <div class="arch-count">
                <div class="arch-bar-wrap"><div class="arch-bar" style="width:${barW}%"></div></div>
                ${dig.itemCount}
              </div>
            </button>`;
          }).join("")+`</div>`;
        if(pages>1){
          html+=`<div class="paginator">`;
          for(let p=1;p<=pages;p++){
            html+=`<button type="button" class="chip ${p===state.archivePage?'on':''}" data-arch-page="${p}">${p}</button>`;
          }
          html+=`</div>`;
        }
        }
      }
    }

    else if(state.view==="agent"){ window.location.href="agent.html"; return; }
    else if(state.view==="changelog"){
      const logs = DATA.meta.changelog || [
        {date:"2026-07-28", items:["每日采集 +6条(经纪/欺诈/高净值) → 累计 175","UI升级 P0-P2","RSS/API 骨架上线","Agent 接入页面","主题雷达改版","下载页分页+统计条","热搜下拉","卡片时间统一","日分组收起"]},
        {date:"2026-07-27", items:["初始部署上线","首批 175 条资讯","四角色切片","简繁切换","深色模式"]}
      ];
      html+=`<div class="panel"><h3>${meta.t}</h3><p>${meta.s}</p></div>`;
      logs.forEach(log=>{
        html+=`<div class="day-head"><h3>${log.date}</h3><span>${log.items.length} 项</span></div>`;
        html+=`<div class="panel" style="margin-bottom:12px"><ul style="margin:0;padding-left:18px">${log.items.map(i=>`<li style="margin:4px 0;font-size:13px;color:var(--text-muted)">${i}</li>`).join("")}</ul></div>`;
      });
    }
    else if(state.view==="about"){
      html+=`<div class="panel about-hero">
        <h3>${t.brandName}</h3>
        <p class="sub">${t.brandSub}</p>
        <p>${esc(t.about1)}</p>
        <p>${esc(t.about2)}</p>
      </div>
      <div class="panel about-qr">
        <div class="qr-area">
          <img src="assets/qr-wechat.jpg" alt="维港猫圈儿" width="120" height="120" />
          <p><strong>${t.wechat}</strong></p>
          <p class="qr-tip">${t.qrTip}</p>
        </div>
      </div>
      <div class="panel about-notice">
        <h4>使用须知</h4>
        <ul>
          <li>本站为资讯聚合与导读索引。摘要与动作卡由人工/AI二次整理，数字与规则以原文链接为准。</li>
          <li>内容供香港持牌保险中介及专业人士参考，不构成销售建议、投资建议或法律意见。</li>
          <li>常驻信息的驻点标准：持续有效的监管规则、长期适用的披露要求、行业基础框架性文件。</li>
          <li>英文原文已标注语种标记；翻译内容仅供参考，以原文为准。</li>
          <li>热点规则: 近14天 sourceTier=official + score≥85 → 自动上榜前6条。精选排序: score×0.7 + 角色匹配×0.3 → 动态排序。常驻: 官方监管/合规类 evergreen=true 手动确认为长期适用。评分原则（60-99）：信源权重(official>insurer>pro>media) × 60% + 内容时效/角色覆盖面 × 25% + 人工校准 × 15%。90+为高确定性一手监管或官方披露；70-89为专业解读；60-69为媒体线索待核。</li>
        </ul>
      </div>
      <div class="panel"><h3>${t.disclaimer}</h3><p>${esc(t.disc)}</p></div>`;
    }
    $("#content").innerHTML=html;
  }


  function savePoints(){ localStorage.setItem("hkii_points", String(state.points)); }
  function mon(){ return (DATA.meta && DATA.meta.monetization) || {enabled:false,prices:{}}; }
  function canExportDigest(period){
    const m=mon();
    // 月报/年报仅可阅读，不可下载
    if(period==="monthly"||period==="yearly") return {ok:true, free:true, readonlyNote:"月报/年报仅可在线查阅，不提供打包下载。"};
    if(!m.enabled) return {ok:true, free:true};
    const price=(m.prices&&m.prices[period])||0;
    if(price<=0) return {ok:true, free:true};
    if(state.pro) return {ok:true, free:false, pro:true};
    if(state.points>=price) return {ok:true, free:false, cost:price};
    return {ok:false, cost:price};
  }
  function toast(msg){
    let el=document.getElementById("hkiiToast");
    if(!el){ el=document.createElement("div"); el.id="hkiiToast"; el.className="toast"; document.body.appendChild(el); }
    el.textContent=msg; el.classList.add("show");
    clearTimeout(el._t); el._t=setTimeout(()=>el.classList.remove("show"), 2200);
  }
  function downloadText(filename, text){
    const blob=new Blob([text],{type:"text/markdown;charset=utf-8"});
    const a=document.createElement("a");
    a.href=URL.createObjectURL(blob); a.download=filename; a.click();
    setTimeout(()=>URL.revokeObjectURL(a.href), 2000);
  }
  function itemToMarkdown(it){
    const t=T();
    const roleLabel=(t.roles.find(r=>r.id===state.role)||{}).label;
    const act=tx(it.actions&&it.actions[state.role])||"—";
    const boards=(it.boards||[]).map(id=>{const b=(DATA.boards||[]).find(x=>x.id===id); return b?tx(b.title):id;}).join(" / ");
    return `# ${tx(it.title)}

> ${t.guideLabel} · ${t.fidelityText}

- **信源等级**: ${t.tier[it.sourceTier]||it.sourceTier}
- **来源**: ${tx(it.source)}
- **发布时间**: ${it.publishedAt||""}
- **生效日**: ${it.effectiveAt||"—"}
- **复核**: ${it.verifyStatus==="verified"?t.verified:t.pending}
- **板块**: ${boards||"—"}
- **来源指纹**: ${it.sourceKey||"—"}

## ${t.summary}
${tx(it.summary)}

## ${t.why}
${tx(it.why)}

## ${t.actionNow}（${roleLabel}）
${act}

## ${t.originalAuthority}
${it.originalUrl||"（无链接）"}

---
${t.brandName} · ${t.disc}
`;
  }
  function digestToMarkdown(dig){
    const t=T();
    const lines=[`# ${tx(dig.label)}`,"",`> ${tx(dig.note||{})}`,"",`条目数: ${dig.itemCount}`,""];
    (dig.itemIds||[]).forEach((id,i)=>{
      const it=byId(id); if(!it) return;
      lines.push(`## ${i+1}. ${tx(it.title)}`);
      lines.push("");
      lines.push(tx(it.summary));
      lines.push("");
      lines.push(`- 原文: ${it.originalUrl||"—"}`);
      lines.push(`- 来源: ${tx(it.source)}`);
      lines.push("");
    });
    lines.push("---");
    lines.push(`${t.brandName} · ${t.disc}`);
    return lines.join("\n");
  }
  function posterSummary(it){
    // 一句话精准总结：优先 why，压缩到 ≤42 字
    const cut=(s,n)=>{s=(s||"").replace(/\s+/g," ").trim(); return s.length>n?s.slice(0,n-1)+"…":s;};
    const soft=s=>(s||"").replace(/不超过总额\d+%/g,"结构已调整").replace(/不超過總額\d+%/g,"結構已調整");
    const w=soft(tx(it.why));
    if(w) return cut(w,42);
    return cut(soft(tx(it.summary)),42);
  }
  function posterBullets(it){
    const sum=tx(it.summary)||"";
    const act=tx(it.actions&&it.actions[state.role])||"";
    const cut=(s,n)=>{s=(s||"").replace(/\s+/g," ").trim(); return s.length>n?s.slice(0,n-1)+"…":s;};
    const soft=s=>(s||"").replace(/不超过总额\d+%/g,"结构已调整").replace(/不超過總額\d+%/g,"結構已調整");
    return [cut(soft(sum),64), cut(soft(act),48)].filter(Boolean);
  }
  function isMomentsFriendly(it){
    const blob=(tx(it.title)+tx(it.summary));
    if(/巡查常见|汇報安排|匯報安排|KPIM|申报表/.test(blob)) return false;
    return true;
  }
  function drawPoster(it){
    const canvas=$("#posterCanvas"); if(!canvas) return;
    const ctx=canvas.getContext("2d");
    const W=1080,H=1350; canvas.width=W; canvas.height=H;
    const t=T();
    // ===== 背景：与网站同色系 深蓝墨 + 顶部金色信号线 =====
    const g=ctx.createLinearGradient(0,0,0,H);
    g.addColorStop(0,"#0d1420"); g.addColorStop(0.6,"#0a0e14"); g.addColorStop(1,"#080b10");
    ctx.fillStyle=g; ctx.fillRect(0,0,W,H);
    // 顶部金色信号线
    ctx.fillStyle="#e8a54b"; ctx.fillRect(0,0,W,8);
    // 细金框（内嵌，克制）
    ctx.strokeStyle="rgba(232,165,75,0.28)"; ctx.lineWidth=2;
    ctx.strokeRect(40,40,W-80,H-80);

    // ===== 品牌行 =====
    ctx.fillStyle="#e8a54b"; ctx.font="700 30px sans-serif";
    ctx.fillText("猫圈儿港险情报站", 80, 116);
    ctx.fillStyle="rgba(232,237,245,0.42)"; ctx.font="400 24px sans-serif";
    const dateStr=(it.publishedAt||"").slice(0,10);
    ctx.fillText(dateStr, 80, 152);

    // ===== 板块标签（纯文字，无图标） =====
    const bid=(it.boards&&it.boards[0])||"reg";
    const board=(DATA.boards||[]).find(b=>b.id===bid);
    const boardName=board?tx(board.title):"港险资讯";
    const bw=ctx.measureText(boardName).width;
    ctx.fillStyle="rgba(232,165,75,0.14)";
    roundRect(ctx,80,188,bw+56,52,10); ctx.fill();
    ctx.fillStyle="#e8a54b"; ctx.font="600 26px sans-serif";
    ctx.fillText(boardName, 108, 222);

    // ===== 标题（大字，衬线感） =====
    ctx.fillStyle="#eef2f8";
    wrapText(ctx, tx(it.title), 80, 320, W-160, 62, "700 48px 'Songti SC','Noto Serif SC',serif", 4);

    // ===== 一句话精准总结（高亮条） =====
    const sum1=posterSummary(it);
    const sumY=560;
    ctx.fillStyle="rgba(232,165,75,0.12)";
    roundRect(ctx,80,sumY-46,W-160,96,14); ctx.fill();
    ctx.fillStyle="#e8a54b"; ctx.fillRect(80,sumY-46,6,96);
    ctx.fillStyle="rgba(238,242,248,0.95)"; ctx.font="500 32px sans-serif";
    wrapText(ctx, sum1, 110, sumY-8, W-220, 44, "500 32px sans-serif", 2);

    // ===== 分隔线 =====
    ctx.strokeStyle="rgba(232,165,75,0.25)"; ctx.beginPath();
    ctx.moveTo(80,sumY+86); ctx.lineTo(W-80,sumY+86); ctx.stroke();

    // ===== 要点（最多2条） =====
    const bullets=posterBullets(it);
    let y=sumY+140;
    bullets.forEach((b,i)=>{
      ctx.fillStyle="#e8a54b"; ctx.font="700 26px sans-serif";
      ctx.fillText("◆", 80, y);
      ctx.fillStyle="rgba(232,237,245,0.82)";
      y = wrapText(ctx, b, 124, y-6, W-204, 42, "400 29px sans-serif", 3) + 40;
    });

    // ===== 评分角标 =====
    ctx.fillStyle="rgba(232,165,75,0.9)"; ctx.font="700 60px sans-serif";
    ctx.textAlign="right";
    ctx.fillText(String(it.score||""), W-90, 130);
    ctx.font="400 20px sans-serif"; ctx.fillStyle="rgba(232,237,245,0.4)";
    ctx.fillText("评分", W-90, 160);
    ctx.textAlign="left";

    // ===== 底部 =====
    ctx.fillStyle="rgba(232,237,245,0.45)"; ctx.font="400 22px sans-serif";
    const url=(it.originalUrl||"").replace(/^https?:\/\//,"").slice(0,46);
    ctx.fillText(url?("原文："+url):"请在情报站打开原文核对", 80, H-140);
    ctx.fillStyle="rgba(232,165,75,0.85)"; ctx.font="600 24px sans-serif";
    ctx.fillText("专业分享 · 非销售邀约 · 以监管/保司原文为准", 80, H-96);
    ctx.fillStyle="rgba(232,237,245,0.5)"; ctx.font="400 22px sans-serif";
    ctx.fillText("维港猫圈儿 · hkmaoquanqingbao.com", 80, H-56);
  }
  function roundRect(ctx,x,y,w,h,r){
    ctx.beginPath(); ctx.moveTo(x+r,y); ctx.arcTo(x+w,y,x+w,y+h,r); ctx.arcTo(x+w,y+h,x,y+h,r);
    ctx.arcTo(x,y+h,x,y,r); ctx.arcTo(x,y,x+w,y,r); ctx.closePath();
  }
  function wrapText(ctx, text, x, y, maxW, lineH, font, maxLines){
    ctx.font=font;
    const chars=[...text]; let line=""; let lines=0; let cy=y;
    for(let i=0;i<chars.length;i++){
      const test=line+chars[i];
      if(ctx.measureText(test).width>maxW && line){
        ctx.fillText(line,x,cy); cy+=lineH; line=chars[i]; lines++;
        if(lines>=maxLines-1){
          let rest=chars.slice(i).join("");
          while(ctx.measureText(rest+"…").width>maxW && rest.length>1) rest=rest.slice(0,-1);
          ctx.fillText(rest+"…",x,cy); return cy+lineH;
        }
      } else line=test;
    }
    if(line){ ctx.fillText(line,x,cy); cy+=lineH; }
    return cy;
  }
  function openPoster(id){
    const it=byId(id); if(!it) return;
    const t=T();
    $("#posterModalTitle").textContent=t.posterTitle;
    const tip=t.posterTip + " " + (isMomentsFriendly(it)?`（${t.momentsOk}）`:`（${t.momentsNo}）`);
    $("#posterTip").textContent=tip;
    $("#posterModal").hidden=false;
    drawPoster(it);
    $("#posterDownload").onclick=()=>{
      try{
        const a=document.createElement("a");
        a.href=$("#posterCanvas").toDataURL("image/png");
        a.download=`猫圈儿-海报-${it.id}.png`;
        document.body.appendChild(a); a.click(); a.remove();
        toast(t.posterDl+" ✓");
      }catch(err){ toast("下载失败，请长按图片保存"); }
    };
    $("#posterCopyMd").onclick=async()=>{
      // 朋友圈文案：标题 + 一句话总结 + 来源提示
      const sum1=posterSummary(it);
      const text=`【港险快讯】${tx(it.title)}\n\n${sum1}\n\n来源：${tx(it.source)}\nvia 猫圈儿港险情报站（hkmaoquanqingbao.com）\n——专业分享，非销售邀约，以监管/保司原文为准`;
      try{ await navigator.clipboard.writeText(text); toast(t.copyDone);}catch(e){ prompt("Copy", text); }
    };
  }
  function closePoster(){ $("#posterModal").hidden=true; }


  function openDrawer(id){
    const it=byId(id); if(!it) return;
    const t=T(); state.selectedId=id;
    $("#dTitle").textContent=tx(it.title);
    const roleLabel=(t.roles.find(r=>r.id===state.role)||{}).label;
    const act=tx(it.actions&&it.actions[state.role])||"—";
    const all=t.roles.map(r=>{const a=it.actions&&it.actions[r.id]; return a?`<div class="action-box"><strong>${r.label}</strong>${esc(tx(a))}</div>`:"";}).join("");
    $("#dBody").innerHTML=`
      <div class="meta-row" style="margin-bottom:10px">
        <span class="badge ${it.sourceTier}">${t.tier[it.sourceTier]}</span>
        <span class="badge">${t.score} ${it.score}</span>
        <span class="badge verify-${it.verifyStatus}">${it.verifyStatus==='verified'?t.verified:t.pending}</span>
      </div>
      <p style="color:var(--text-dim);font-size:12px">${esc(tx(it.source))} · ${esc(it.publishedAt||"")}</p>
      <div class="fidelity-banner">${t.guideLabel} · ${t.fidelityText}</div>
      <h4>${t.summary}</h4><p>${esc(tx(it.summary))}</p>
      ${it.contentRole?`<p style="font-size:12px;color:var(--text-dim)">${esc(tx(it.contentRole))}</p>`:""}
      <h4>${t.why}</h4><p>${esc(tx(it.why))}</p>
      <h4>${t.actionNow} · ${esc(roleLabel)}</h4>
      <div class="action-box"><strong>${t.roleNow}</strong>${esc(act)}</div>
      <h4>${t.actionAll}</h4>${all}
      ${it.effectiveAt?`<h4>${t.effective}</h4><p>${esc(it.effectiveAt)}</p>`:""}
      ${it.note?`<h4>${t.note}</h4><p>${esc(tx(it.note))}</p>`:""}
      <h4>${t.themesH}</h4><p>${esc((it.themes||[]).map(x=>t.themes[x]||x).join(" · "))}</p>
      <h4>${t.originalAuthority}</h4>
      <div class="links">${it.originalUrl?`<a class="btn-original" href="${it.originalUrl}" target="_blank" rel="noopener">${t.original} ↗</a>`:`<span class="badge">无原文链接</span>`}
      ""
      ${it.sourceKey?`<span class="badge">${t.sourceKey} ${it.sourceKey}</span>`:""}</div>
      <div class="action-bar">
        <button type="button" class="btn primary" data-export-md="${it.id}">${t.exportMd}</button>
        <button type="button" class="btn" data-poster="${it.id}">${t.posterBtn}</button>
      </div>
      <p class="lock-note">${isMomentsFriendly(it)?t.momentsOk:t.momentsNo}</p>`;
    $("#drawer").classList.add("open"); $("#backdrop").classList.add("open"); render();
  }
  function closeDrawer(){ state.selectedId=null; $("#drawer").classList.remove("open"); $("#backdrop").classList.remove("open"); render(); }

  $("#nav").addEventListener("click", e=>{ const b=e.target.closest("[data-view]"); if(!b) return; state.view=b.dataset.view; state.themeFilter="all"; state.feedTier="all"; state.feedKind="all"; if(b.dataset.view!=="themes") state.themeBoard=null; $("#sidebar").classList.remove("open"); render(); });
  $("#rolePills").addEventListener("click", e=>{ const b=e.target.closest("[data-role]"); if(!b) return; state.role=b.dataset.role; localStorage.setItem("hkii_role", state.role); render(); });
  $("#q").addEventListener("input", e=>{ state.q=e.target.value; localStorage.setItem("hkii_q",state.q); render(); });
  $("#content").addEventListener("click", e=>{
    const ft2=e.target.closest("#facetToggle"); if(ft2){ const fm=document.getElementById("facetMore"); if(fm) fm.style.display=fm.style.display==="none"?"":"none"; ft2.textContent=fm.style.display==="none"?"文种 ▾":"文种 ▴"; return; }const hs=e.target.closest("[data-hotsearch]"); if(hs){ state.q=hs.dataset.hotsearch; document.getElementById("q").value=state.q; document.getElementById("hotsearchDropdown").style.display="none"; render(); return; }const hc=e.target.closest("[data-hot]"); if(hc){ state.q=hc.dataset.hot; document.getElementById("q").value=state.q; render(); return; }
    const email=e.target.closest("[data-email-digest]"); if(email){ e.stopPropagation(); const box=email.parentElement.nextElementSibling; box.style.display=box.style.display==="none"?"block":"none"; return; }
    const fav=e.target.closest("[data-fav]"); if(fav){ e.stopPropagation(); const id=fav.dataset.fav; state.fav.has(id)?state.fav.delete(id):state.fav.add(id); localStorage.setItem("hkii_fav", JSON.stringify([...state.fav])); render(); return; }
    const favtag=e.target.closest("[data-favtag]"); if(favtag){ state.favTag = favtag.dataset.favtag || null; render(); return; }
    const o=e.target.closest("[data-open]"); if(o){ openDrawer(o.dataset.open); return; }
    // 主题雷达：进板块页（不跳全部动态）
    const bb=e.target.closest("[data-board-back]"); if(bb){ state.themeBoard=null; render(); return; }
    const bd=e.target.closest("[data-board]"); if(bd){ state.themeBoard=bd.dataset.board; render(); return; }
    const ft=e.target.closest("[data-feed-tier]"); if(ft){ state.feedTier=ft.dataset.feedTier; render(); return; }
    const fk=e.target.closest("[data-feed-kind]"); if(fk){ state.feedKind=fk.dataset.feedKind; render(); return; }
    const bf=e.target.closest("[data-board-filter]"); if(bf){ state.themeFilter=bf.dataset.boardFilter; render(); return; }
    // 档案
    const ap=e.target.closest("[data-arch-period]"); if(ap){ state.archivePeriod=ap.dataset.archPeriod; state.archiveKey=null; state.archivePage=1; render(); return; }
    const ab=e.target.closest("[data-arch-back]"); if(ab){ state.archiveKey=null; state.archivePage=1; render(); return; }
    const ak=e.target.closest("[data-arch-key]"); if(ak){ state.archiveKey=ak.dataset.archKey; render(); return; }
    const apg=e.target.closest("[data-arch-page]"); if(apg){ state.archivePage=parseInt(apg.dataset.archPage); render(); return; }
    const j=e.target.closest("[data-jump-theme]"); if(j){ state.view="themes"; state.themeBoard=j.dataset.jumpTheme; render(); return; }
    const tf=e.target.closest("[data-theme-filter]"); if(tf){ state.themeFilter=tf.dataset.themeFilter; render(); return; }
    const em=e.target.closest("[data-export-md]"); if(em){ e.stopPropagation(); const it=byId(em.dataset.exportMd); if(!it) return; downloadText(`猫圈儿-${it.id}.md`, itemToMarkdown(it)); toast(T().mdDone); return; }
    const po=e.target.closest("[data-poster]"); if(po){ e.stopPropagation(); openPoster(po.dataset.poster); return; }
    const ed=e.target.closest("[data-export-digest]"); if(ed){
      e.stopPropagation();
      const digs=(DATA.digests&&DATA.digests[state.archivePeriod])||[];
      const dig=digs.find(x=>x.key===state.archiveKey); if(!dig) return;
      const gate=canExportDigest(state.archivePeriod);
      if(!gate.ok){ toast(T().proNeed.replace("{n}", String(gate.cost||0))); return; }
      if(gate.cost){ state.points-=gate.cost; savePoints(); }
      downloadText(`猫圈儿-${state.archivePeriod}-${dig.key}.md`, digestToMarkdown(dig)); toast(T().mdDone);
      applyChrome();
      return;
    }
    const c=e.target.closest(".card"); if(c) openDrawer(c.dataset.id);
  });
  // drawer action buttons (export live in drawer body)
  $("#dBody").addEventListener("click", e=>{
    const em=e.target.closest("[data-export-md]"); if(em){ const it=byId(em.dataset.exportMd); if(it) downloadText(`猫圈儿-${it.id}.md`, itemToMarkdown(it)); toast(T().mdDone); return; }
    const po=e.target.closest("[data-poster]"); if(po){ openPoster(po.dataset.poster); }
  });
  const pm=$("#posterModal");
  if(pm){
    $("#posterClose").addEventListener("click", closePoster);
    pm.addEventListener("click", e=>{ if(e.target===pm) closePoster(); });
  }

  $("#dClose").addEventListener("click", closeDrawer);
  $("#backdrop").addEventListener("click", closeDrawer);
  document.addEventListener("keydown", e=>{ if(e.key==="Escape"){ closePoster(); closeDrawer(); } });
  $(".sidebar-foot").addEventListener("click", e=>{
    const lang=e.target.closest("[data-lang]"); if(lang){ state.lang=lang.dataset.lang; localStorage.setItem("hkii_lang", state.lang); render(); return; }
    const th=e.target.closest("[data-theme-btn]"); if(th){ state.theme=th.dataset.themeBtn; localStorage.setItem("hkii_theme", state.theme); render(); }
  });
  $("#menuBtn").addEventListener("click", ()=>$("#sidebar").classList.toggle("open"));
  render();
})();
