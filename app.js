window.HKII_DATA = {
  "meta": {
    "product": "猫圈儿港险情报站",
    "generatedAt": "2026-07-26T23:59:00+08:00",
    "itemCount": 45,
    "windowNote": {
      "sc": "本库 45 条导读，数据窗口截至 2026-07-26。信源：监管+保司官网+机构研究+媒体线索。全部动态默认按发布时间降序。导读≠原文。",
      "tc": "本庫 45 條導讀，數據窗口截至 2026-07-26。信源：監管+保司官網+機構研究+媒體線索。全部動態默認按發布時間降序。導讀≠原文。"
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
      "version": "0.3.1",
      "updatedAt": "2026-07-26",
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
    "asOf": "2026-07-26",
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
    ]
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
      "clusterCount": 1,
      "score": 70,
      "verifyStatus": "pending",
      "featured": false,
      "evergreen": false,
      "ingestedAt": "2026-07-26T23:59:00+08:00",
      "contentRole": {
        "sc": "本站导读（非原文）",
        "tc": "本站導讀（非原文）"
      },
      "id": "aif-2026-save-the-date",
      "title": {
        "sc": "日程：Asian Insurance Forum 2026（11 月 13 日 · 保监局主办语境）",
        "tc": "日程：Asian Insurance Forum 2026（11 月 13 日 · 保監局主辦語境）"
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
      "clusterCount": 1,
      "score": 76,
      "verifyStatus": "pending",
      "featured": true,
      "evergreen": false,
      "ingestedAt": "2026-07-26T23:59:00+08:00",
      "contentRole": {
        "sc": "本站导读（非原文）",
        "tc": "本站導讀（非原文）"
      },
      "id": "ia-public-disclosure-2026",
      "title": {
        "sc": "公开披露规则推进：获授权保险人公众披露要求（2026 落地语境）",
        "tc": "公開披露規則推進：獲授權保險人公眾披露要求（2026 落地語境）"
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
      "sourceTier": "media",
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
      "sourceKey": "media:insurance-asia:public-disclosure-2026",
      "boards": [
        "reg"
      ],
      "contentKind": "industry_news"
    },
    {
      "id": "ia-q1-2026-stats",
      "title": {
        "sc": "2026年Q1临时统计：长期业务新造保费约1411亿港元，同比约+51.1%",
        "tc": "2026年Q1臨時統計：長期業務新造保費約1411億港元，同比約+51.1%"
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
      "sourceTier": "media",
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
      "verifyStatus": "pending",
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
      "sourceKey": "7708009f3dce",
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
        "sc": "金管局《投诉观察》第28期发布（2026-07-24）",
        "tc": "金管局《投訴觀察》第28期發布（2026-07-24）"
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
      "sourceKey": "640ae1431773",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "market",
        "reg"
      ],
      "contentKind": "press"
    },
    {
      "id": "ia-20260716-ashk-ifoa",
      "title": {
        "sc": "保监局刘中健：香港精算学会与英国精算师协会联合会议主题演讲（2026-07-16）",
        "tc": "保監局劉中健：香港精算學會與英國精算師協會聯合會議主題演講（2026-07-16）"
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
      "sourceKey": "374966cc5e38",
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
      "clusterCount": 1,
      "score": 80,
      "verifyStatus": "pending",
      "featured": true,
      "evergreen": false,
      "ingestedAt": "2026-07-26T23:59:00+08:00",
      "contentRole": {
        "sc": "本站导读（非原文）",
        "tc": "本站導讀（非原文）"
      },
      "id": "ia-20260715-sales-practices",
      "title": {
        "sc": "行业观察：保监局强化销售行为监管（误导/适当性/录音录像相关叙事升温）",
        "tc": "行業觀察：保監局強化銷售行為監管（誤導/適當性/錄音錄影相關敘事升溫）"
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
      "sourceTier": "media",
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
      "sourceKey": "media:asia-insurance-review:2026-07-15-sales",
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
      "id": "ia-licence-20260630",
      "title": {
        "sc": "持牌中介统计（截至2026-06-30）：个人持牌约12.25万，经纪公司810家",
        "tc": "持牌中介統計（截至2026-06-30）：個人持牌約12.25萬，經紀公司810家"
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
      "sourceKey": "66820b56a89e",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "market",
        "reg"
      ],
      "contentKind": "stats"
    },
    {
      "id": "ia-20260712-speech",
      "title": {
        "sc": "保监局：分红保单三项监管措施落地回顾与「跨行业背景查核」推进",
        "tc": "保監局：分紅保單三項監管措施落地回顧與「跨行業背景查核」推進"
      },
      "summary": {
        "sc": "保监局2026年7月12日文章回顾自2025年起分阶段推出的分红保单销售三项措施：2025年7月演示利率上限、2025年10月经纪转介费基准、2026年1月中介佣金分摊。文中并说明与金管局推动的跨行业背景查核安排已于2026年7月生效，覆盖约11万名长期业务中介。",
        "tc": "保監局2026年7月12日文章回顧自2025年起分階段推出的分紅保單銷售三項措施：2025年7月演示利率上限、2025年10月經紀轉介費基準、2026年1月中介佣金分攤。文中並說明與金管局推動的跨行業背景查核安排已於2026年7月生效，覆蓋約11萬名長期業務中介。"
      },
      "why": {
        "sc": "这是当前港险前线与合规的总纲领：三项费用/演示规则改变激励与话术，背景查核改变跳槽与聘用尽调。",
        "tc": "這是當前港險前線與合規的總綱領：三項費用/演示規則改變激勵與話術，背景查核改變跳槽與聘用盡調。"
      },
      "actions": {
        "front": {
          "sc": "检查计划书演示口径与转介书面披露；勿口头承诺旧佣金结构。",
          "tc": "檢查計劃書演示口徑與轉介書面披露；勿口頭承諾舊佣金結構。"
        },
        "midback": {
          "sc": "更新培训：三项措施时间轴 + 背景查核对招募话术的影响。｜核对聘用前主事人查核流程是否覆盖银行/保险跨界跳槽。",
          "tc": "更新培訓：三項措施時間軸 + 背景查核對招募話術的影響。｜核對聘用前主事人查核流程是否覆蓋銀行/保險跨界跳槽。"
        },
        "lead": {
          "sc": "把三项措施与查核纳入团队 KPI 与合规仪表盘。",
          "tc": "把三項措施與查核納入團隊 KPI 與合規儀表盤。"
        },
        "cross": {
          "sc": "跨境转介与大额单更易触发无牌风险，默认走公司协议。",
          "tc": "跨境轉介與大額單更易觸發無牌風險，默認走公司協議。"
        }
      },
      "source": {
        "sc": "保险业监管局 · 演辞/文章 2026-07-12",
        "tc": "保險業監管局 · 演辭/文章 2026-07-12"
      },
      "sourceTier": "official",
      "tags": {
        "sc": [
          "分红",
          "佣金分摊",
          "转介",
          "背景查核"
        ],
        "tc": [
          "分紅",
          "佣金分攤",
          "轉介",
          "背景查核"
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
        "cross": 2
      },
      "publishedAt": "2026-07-12T10:00:00+08:00",
      "effectiveAt": "2026-07-01",
      "clusterCount": 3,
      "score": 96,
      "verifyStatus": "verified",
      "originalUrl": "https://www.ia.org.hk/tc/infocenter/speeches_articles/20260712.html",
      "featured": true,
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "386163325a35",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": true,
      "boards": [
        "market",
        "reg"
      ],
      "contentKind": "speech"
    },
    {
      "id": "ia-20260710-illustration-review",
      "title": {
        "sc": "演示利率上限检讨机制：保监局发布释义说明（2026-07-10）",
        "tc": "演示利率上限檢討機制：保監局發布釋義說明（2026-07-10）"
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
      "sourceKey": "ad062ce68233",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "product",
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "ia-20260708-captive",
      "title": {
        "sc": "两间新专属自保公司获授权，巩固风险管理中心策略（2026-07-08）",
        "tc": "兩間新專屬自保公司獲授權，鞏固風險管理中心策略（2026-07-08）"
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
      "sourceKey": "f278318f2603",
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
      "id": "ia-20260703-rfyc",
      "title": {
        "sc": "指定无风险收益率曲线（截至2026-06-30）发布（2026-07-03）",
        "tc": "指定無風險收益率曲線（截至2026-06-30）發布（2026-07-03）"
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
      "sourceKey": "689c86ed9cfd",
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
      "id": "ia-ai-seminar-20260615",
      "title": {
        "sc": "保监局举办「人工智能促进计划」研讨会，新增强点参与保司",
        "tc": "保監局舉辦「人工智能促進計劃」研討會，新增重點參與保司"
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
      "verifyStatus": "pending",
      "originalUrl": "https://www.ia.org.hk/sc/infocenter/press_releases/20260615.html",
      "featured": false,
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "0ce9dc37bd81",
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
      "id": "ia-hkma-remuneration-20260605",
      "title": {
        "sc": "保监局提请业界注意：金管局关于银行保险中介分红报酬结构通函",
        "tc": "保監局提請業界注意：金管局關於銀行保險中介分紅報酬結構通函"
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
      "sourceKey": "32f430b3e9e3",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "market",
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "ia-20260529-onsite-findings",
      "title": {
        "sc": "保司现场操守巡查常见问题与最佳实务（2026-05-29）",
        "tc": "保司現場操守巡查常見問題與最佳實務（2026-05-29）"
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
      "sourceKey": "9cb97d91ba1f",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "insurer",
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "ia-20260513-cross-refcheck",
      "title": {
        "sc": "银行与保险跨行业背景查核安排通函（2026-05-13）",
        "tc": "銀行與保險跨行業背景查核安排通函（2026-05-13）"
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
      "sourceKey": "2a14ea72c7aa",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": true,
      "boards": [
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "ia-20260508-rbc-conclusions",
      "title": {
        "sc": "RBC 制度优化咨询结论发布：鼓励基建投资、巩固风险管理中心（2026-05-08）",
        "tc": "RBC 制度優化諮詢結論發布：鼓勵基建投資、鞏固風險管理中心（2026-05-08）"
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
      "sourceKey": "4fa91bb178e0",
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
      "id": "ia-20260424-stats-2025",
      "title": {
        "sc": "保监局公布2025年临时统计（2026-04-24）",
        "tc": "保監局公布2025年臨時統計（2026-04-24）"
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
      "verifyStatus": "pending",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "21a8432a9a6e",
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
      "id": "ia-20260422-ils",
      "title": {
        "sc": "2026保险相连证券（ILS）研讨会：主席开幕辞（2026-04-22）",
        "tc": "2026保險相連證券（ILS）研討會：主席開幕辭（2026-04-22）"
      },
      "summary": {
        "sc": "保监局主席姚建华于2026年4月22日在保险相连证券研讨会上致开幕辞，聚焦巨灾风险转移、资本市场与香港风险管理中心建设。",
        "tc": "保監局主席姚建華於2026年4月22日在保險相連證券研討會上致開幕辭，聚焦巨災風險轉移、資本市場與香港風險管理中心建設。"
      },
      "why": {
        "sc": "零售以外的风险证券化叙事，补强「港险=风险管理中心」定位。",
        "tc": "零售以外的風險證券化敘事，補強「港險=風險管理中心」定位。"
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
      "sourceKey": "a2752628d9f1",
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
      "id": "ia-20260416-cyber",
      "title": {
        "sc": "APAC 网络风险与保险峰会简报（2026-04-16）",
        "tc": "APAC 網絡風險與保險峰會簡報（2026-04-16）"
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
      "sourceKey": "1aef27bc0afd",
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
      "id": "ia-20260409-captive-beijing",
      "title": {
        "sc": "保监局于北京举办专属自保论坛（2026-04-09）",
        "tc": "保監局於北京舉辦專屬自保論壇（2026-04-09）"
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
      "sourceKey": "de24d648be8a",
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
      "id": "ia-20260331-cpd-reporting",
      "title": {
        "sc": "CPD合规汇报安排：2025/26及后续评核期（2026-03-31）",
        "tc": "CPD合規匯報安排：2025/26及後續評核期（2026-03-31）"
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
      "sourceKey": "b721bb626546",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "ia-20260327-cif12",
      "title": {
        "sc": "《监管通讯》第12期（2026-03）：投诉、社媒推广与合规专题",
        "tc": "《監管通訊》第12期（2026-03）：投訴、社媒推廣與合規專題"
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
      "sourceKey": "a0031316f7fd",
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
        "sc": "亚太医疗与健康保险会议主题演讲（2026-03-26）",
        "tc": "亞太醫療與健康保險會議主題演講（2026-03-26）"
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
      "sourceKey": "178ef09bdb19",
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
        "sc": "2026专属自保保险座谈会开幕致辞（2026-03-25）",
        "tc": "2026專屬自保保險座談會開幕致辭（2026-03-25）"
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
      "sourceKey": "7694ed371349",
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
      "id": "ia-20260305-genai-sandbox",
      "title": {
        "sc": "监管机构推出 GenA.I. 沙盒++ 覆盖保险等多元金融领域（2026-03-05）",
        "tc": "監管機構推出 GenA.I. 沙盒++ 覆蓋保險等多元金融領域（2026-03-05）"
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
      "sourceKey": "d23c1dd4648f",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "reg",
        "tech"
      ],
      "contentKind": "circular"
    },
    {
      "id": "ia-budget-20260225",
      "title": {
        "sc": "保监局欢迎2026-27财政预算案中与国家规划对接的措施",
        "tc": "保監局歡迎2026-27財政預算案中與國家規劃對接的措施"
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
      "verifyStatus": "pending",
      "originalUrl": "https://www.ia.org.hk/tc/infocenter/press_releases/20260225.html",
      "featured": false,
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "40a7a9469d40",
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
        "sc": "保险人中介管理关键人员（KPIM）手册发布（2026-02-24）",
        "tc": "保險人中介管理關鍵人員（KPIM）手冊發布（2026-02-24）"
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
      "sourceKey": "f00d4e531261",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "market",
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "ia-20260213-low-altitude",
      "title": {
        "sc": "保险创新助力低空经济发展（2026-02-13）",
        "tc": "保險創新助力低空經濟發展（2026-02-13）"
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
      "sourceKey": "b80d5dccfb71",
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
        "sc": "完善风险为本资本制度公众咨询启动（2026-02-11）",
        "tc": "完善風險為本資本制度公眾諮詢啟動（2026-02-11）"
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
      "sourceKey": "747f0412f09b",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "insurer",
        "reg"
      ],
      "contentKind": "press"
    },
    {
      "id": "ia-20260206-gl16-gl34",
      "title": {
        "sc": "修订 GL16 与 GL34：长期承保与分红基金管理（2026-02-06）",
        "tc": "修訂 GL16 與 GL34：長期承保與分紅基金管理（2026-02-06）"
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
      "sourceKey": "fab557563f4f",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "product",
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "ia-20260126-aff",
      "title": {
        "sc": "亚洲金融论坛2026：保监局开场发言（2026-01-26）",
        "tc": "亞洲金融論壇2026：保監局開場發言（2026-01-26）"
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
      "sourceKey": "02dce8fc5ff5",
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
      "id": "ia-20260123-stats-3q2025",
      "title": {
        "sc": "2025年前三季临时统计：长期新造约2645亿，同比约+55.9%（2026-01-23）",
        "tc": "2025年前三季臨時統計：長期新造約2645億，同比約+55.9%（2026-01-23）"
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
      "verifyStatus": "pending",
      "contentRole": {
        "sc": "本站条目为导读与索引：摘要/动作卡由本站整理，不替代原文。请点「打开原文」核对。",
        "tc": "本站條目為導讀與索引：摘要/動作卡由本站整理，不替代原文。請點「打開原文」核對。"
      },
      "sourceKey": "d4285f5df623",
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
      "id": "ia-gl34-20260331",
      "title": {
        "sc": "修订 GL34 分红业务基金管理：主体2026-03-31 生效，公司政策段2026-06-30",
        "tc": "修訂 GL34 分紅業務基金管理：主體2026-03-31 生效，公司政策段2026-06-30"
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
      "verifyStatus": "pending",
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
      "id": "ia-20251120-refcheck-scheme",
      "title": {
        "sc": "保险中介人背景查核计划通函（2025-11-20）",
        "tc": "保險中介人背景查核計劃通函（2025-11-20）"
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
      "sourceKey": "9f22d9b9ffe6",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "ia-20251024-1h2025-stats",
      "title": {
        "sc": "2025上半年临时统计：长期新造约1737亿港元，同比约+50%",
        "tc": "2025上半年臨時統計：長期新造約1737億港元，同比約+50%"
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
      "sourceKey": "16b295515e4e",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "insurer",
        "market"
      ],
      "contentKind": "press"
    },
    {
      "id": "ia-ro-cpd-20251014",
      "title": {
        "sc": "负责人（RO）强制 CPD：2025/26 评估期首轮安排（2025-10-14 通函）",
        "tc": "負責人（RO）強制 CPD：2025/26 評估期首輪安排（2025-10-14 通函）"
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
      "sourceKey": "ef881447d786",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "ia-20250919-product-naming",
      "title": {
        "sc": "保险产品命名要求联合通函（2025-09-19）",
        "tc": "保險產品命名要求聯合通函（2025-09-19）"
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
      "sourceKey": "7a9e691315c4",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "product",
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "ia-20250901-referral-fee",
      "title": {
        "sc": "分红保单转介费监管期望：50%基准（2025-09-01，10-01起遵从）",
        "tc": "分紅保單轉介費監管期望：50%基準（2025-09-01，10-01起遵從）"
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
      "sourceKey": "3db7b216865d",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": true,
      "boards": [
        "market",
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "ia-commission-20260101",
      "title": {
        "sc": "分红保单佣金分摊：2026-01-01 起首年不超过总额70%，其余至少分5年",
        "tc": "分紅保單佣金分攤：2026-01-01 起首年不超過總額70%，其餘至少分5年"
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
      "sourceKey": "646e0be57941",
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
        "sc": "风险为本资本制度首个财政年度公众披露要求（2025-08-08）",
        "tc": "風險為本資本制度首個財政年度公眾披露要求（2025-08-08）"
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
      "sourceKey": "7b8b734014dc",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "insurer",
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "ia-20250711-ro-cpd-compulsory",
      "title": {
        "sc": "经纪公司负责人强制RO-CPD自2025-08-01生效（2025-07-11）",
        "tc": "經紀公司負責人強制RO-CPD自2025-08-01生效（2025-07-11）"
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
      "sourceKey": "f4e6f61cb783",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "reg"
      ],
      "contentKind": "circular"
    },
    {
      "id": "ia-20250330-illustration-article",
      "title": {
        "sc": "保监局文章：引入演示利率上限，提升投保人保障（2025-03-30）",
        "tc": "保監局文章：引入演示利率上限，提升投保人保障（2025-03-30）"
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
      "sourceKey": "2aafbac0bb66",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "product",
        "reg"
      ],
      "contentKind": "speech"
    },
    {
      "id": "ia-20250313-iul-pi",
      "title": {
        "sc": "指数型万用寿险（IUL）面向专业投资者的联合通函（2025-03-13）",
        "tc": "指數型萬用壽險（IUL）面向專業投資者的聯合通函（2025-03-13）"
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
      "sourceKey": "468167a07da6",
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
      "id": "ia-20250228-illustration-cap-pn",
      "title": {
        "sc": "分红保单演示利率上限应用说明（2025-02-28）",
        "tc": "分紅保單演示利率上限應用說明（2025-02-28）"
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
      "sourceKey": "b207ba3771bd",
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
        "sc": "理赔管理发现与建议（2025-02-06）",
        "tc": "理賠管理發現與建議（2025-02-06）"
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
      "sourceKey": "69df2e553578",
      "ingestedAt": "2026-07-26T01:08:49+08:00",
      "evergreen": false,
      "boards": [
        "product",
        "reg"
      ],
      "contentKind": "circular"
    }
  ],
  "calendar": [
    {
      "date": "2026-11-13",
      "title": {
        "sc": "Asian Insurance Forum 2026",
        "tc": "Asian Insurance Forum 2026"
      },
      "theme": "firm"
    },
    {
      "date": "2026-07-31",
      "title": {
        "sc": "CPD 2025/26 学时完成截止（评核期）",
        "tc": "CPD 2025/26 學時完成截止（評核期）"
      },
      "theme": "career"
    },
    {
      "date": "2026-07-10",
      "title": {
        "sc": "演示上限检讨机制释义",
        "tc": "演示上限檢討機制釋義"
      },
      "theme": "par"
    },
    {
      "date": "2026-07-01",
      "title": {
        "sc": "跨行业背景查核安排生效（保监局叙述）",
        "tc": "跨行業背景查核安排生效（保監局敘述）"
      },
      "theme": "compliance"
    },
    {
      "date": "2026-06-30",
      "title": {
        "sc": "GL34 公司政策节生效",
        "tc": "GL34 公司政策節生效"
      },
      "theme": "reg"
    },
    {
      "date": "2026-03-31",
      "title": {
        "sc": "GL34 修订主体生效",
        "tc": "GL34 修訂主體生效"
      },
      "theme": "reg"
    },
    {
      "date": "2026-01-01",
      "title": {
        "sc": "分红保单佣金分摊要求生效",
        "tc": "分紅保單佣金分攤要求生效"
      },
      "theme": "compliance"
    },
    {
      "date": "2025-10-01",
      "title": {
        "sc": "转介费50%基准遵从",
        "tc": "轉介費50%基準遵從"
      },
      "theme": "compliance"
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
      "theme": "par"
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
        "key": "2026-07-26",
        "label": {
          "sc": "2026-07-26",
          "tc": "2026-07-26"
        },
        "itemCount": 1,
        "itemIds": [
          "aif-2026-save-the-date"
        ],
        "leadTitle": {
          "sc": "日程：Asian Insurance Forum 2026（11 月 13 日 · 保监局主办语境）",
          "tc": "日程：Asian Insurance Forum 2026（11 月 13 日 · 保監局主辦語境）"
        },
        "note": {
          "sc": "2026-07-26 收录 1 条导读",
          "tc": "2026-07-26 收錄 1 條導讀"
        }
      },
      {
        "key": "2026-07-25",
        "label": {
          "sc": "2026-07-25",
          "tc": "2026-07-25"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-public-disclosure-2026"
        ],
        "leadTitle": {
          "sc": "公开披露规则推进：获授权保险人公众披露要求（2026 落地语境）",
          "tc": "公開披露規則推進：獲授權保險人公眾披露要求（2026 落地語境）"
        },
        "note": {
          "sc": "2026-07-25 收录 1 条导读",
          "tc": "2026-07-25 收錄 1 條導讀"
        }
      },
      {
        "key": "2026-07-24",
        "label": {
          "sc": "2026-07-24",
          "tc": "2026-07-24"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-q1-2026-stats",
          "hkma-complaints-20260724"
        ],
        "leadTitle": {
          "sc": "2026年Q1临时统计：长期业务新造保费约1411亿港元，同比约+51.1%",
          "tc": "2026年Q1臨時統計：長期業務新造保費約1411億港元，同比約+51.1%"
        },
        "note": {
          "sc": "2026-07-24 收录 2 条导读",
          "tc": "2026-07-24 收錄 2 條導讀"
        }
      },
      {
        "key": "2026-07-16",
        "label": {
          "sc": "2026-07-16",
          "tc": "2026-07-16"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260716-ashk-ifoa"
        ],
        "leadTitle": {
          "sc": "保监局刘中健：香港精算学会与英国精算师协会联合会议主题演讲（2026-07-16）",
          "tc": "保監局劉中健：香港精算學會與英國精算師協會聯合會議主題演講（2026-07-16）"
        },
        "note": {
          "sc": "2026-07-16 收录 1 条导读",
          "tc": "2026-07-16 收錄 1 條導讀"
        }
      },
      {
        "key": "2026-07-15",
        "label": {
          "sc": "2026-07-15",
          "tc": "2026-07-15"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260715-sales-practices"
        ],
        "leadTitle": {
          "sc": "行业观察：保监局强化销售行为监管（误导/适当性/录音录像相关叙事升温）",
          "tc": "行業觀察：保監局強化銷售行為監管（誤導/適當性/錄音錄影相關敘事升溫）"
        },
        "note": {
          "sc": "2026-07-15 收录 1 条导读",
          "tc": "2026-07-15 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "持牌中介统计（截至2026-06-30）：个人持牌约12.25万，经纪公司810家",
          "tc": "持牌中介統計（截至2026-06-30）：個人持牌約12.25萬，經紀公司810家"
        },
        "note": {
          "sc": "2026-07-14 收录 1 条导读",
          "tc": "2026-07-14 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "保监局：分红保单三项监管措施落地回顾与「跨行业背景查核」推进",
          "tc": "保監局：分紅保單三項監管措施落地回顧與「跨行業背景查核」推進"
        },
        "note": {
          "sc": "2026-07-12 收录 1 条导读",
          "tc": "2026-07-12 收錄 1 條導讀"
        }
      },
      {
        "key": "2026-07-10",
        "label": {
          "sc": "2026-07-10",
          "tc": "2026-07-10"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260710-illustration-review"
        ],
        "leadTitle": {
          "sc": "演示利率上限检讨机制：保监局发布释义说明（2026-07-10）",
          "tc": "演示利率上限檢討機制：保監局發布釋義說明（2026-07-10）"
        },
        "note": {
          "sc": "2026-07-10 收录 1 条导读",
          "tc": "2026-07-10 收錄 1 條導讀"
        }
      },
      {
        "key": "2026-07-08",
        "label": {
          "sc": "2026-07-08",
          "tc": "2026-07-08"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260708-captive"
        ],
        "leadTitle": {
          "sc": "两间新专属自保公司获授权，巩固风险管理中心策略（2026-07-08）",
          "tc": "兩間新專屬自保公司獲授權，鞏固風險管理中心策略（2026-07-08）"
        },
        "note": {
          "sc": "2026-07-08 收录 1 条导读",
          "tc": "2026-07-08 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "指定无风险收益率曲线（截至2026-06-30）发布（2026-07-03）",
          "tc": "指定無風險收益率曲線（截至2026-06-30）發布（2026-07-03）"
        },
        "note": {
          "sc": "2026-07-03 收录 1 条导读",
          "tc": "2026-07-03 收錄 1 條導讀"
        }
      },
      {
        "key": "2026-06-15",
        "label": {
          "sc": "2026-06-15",
          "tc": "2026-06-15"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-ai-seminar-20260615"
        ],
        "leadTitle": {
          "sc": "保监局举办「人工智能促进计划」研讨会，新增强点参与保司",
          "tc": "保監局舉辦「人工智能促進計劃」研討會，新增重點參與保司"
        },
        "note": {
          "sc": "2026-06-15 收录 1 条导读",
          "tc": "2026-06-15 收錄 1 條導讀"
        }
      },
      {
        "key": "2026-06-05",
        "label": {
          "sc": "2026-06-05",
          "tc": "2026-06-05"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-hkma-remuneration-20260605"
        ],
        "leadTitle": {
          "sc": "保监局提请业界注意：金管局关于银行保险中介分红报酬结构通函",
          "tc": "保監局提請業界注意：金管局關於銀行保險中介分紅報酬結構通函"
        },
        "note": {
          "sc": "2026-06-05 收录 1 条导读",
          "tc": "2026-06-05 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "保司现场操守巡查常见问题与最佳实务（2026-05-29）",
          "tc": "保司現場操守巡查常見問題與最佳實務（2026-05-29）"
        },
        "note": {
          "sc": "2026-05-29 收录 1 条导读",
          "tc": "2026-05-29 收錄 1 條導讀"
        }
      },
      {
        "key": "2026-05-13",
        "label": {
          "sc": "2026-05-13",
          "tc": "2026-05-13"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260513-cross-refcheck"
        ],
        "leadTitle": {
          "sc": "银行与保险跨行业背景查核安排通函（2026-05-13）",
          "tc": "銀行與保險跨行業背景查核安排通函（2026-05-13）"
        },
        "note": {
          "sc": "2026-05-13 收录 1 条导读",
          "tc": "2026-05-13 收錄 1 條導讀"
        }
      },
      {
        "key": "2026-05-08",
        "label": {
          "sc": "2026-05-08",
          "tc": "2026-05-08"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260508-rbc-conclusions"
        ],
        "leadTitle": {
          "sc": "RBC 制度优化咨询结论发布：鼓励基建投资、巩固风险管理中心（2026-05-08）",
          "tc": "RBC 制度優化諮詢結論發布：鼓勵基建投資、鞏固風險管理中心（2026-05-08）"
        },
        "note": {
          "sc": "2026-05-08 收录 1 条导读",
          "tc": "2026-05-08 收錄 1 條導讀"
        }
      },
      {
        "key": "2026-04-24",
        "label": {
          "sc": "2026-04-24",
          "tc": "2026-04-24"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260424-stats-2025"
        ],
        "leadTitle": {
          "sc": "保监局公布2025年临时统计（2026-04-24）",
          "tc": "保監局公布2025年臨時統計（2026-04-24）"
        },
        "note": {
          "sc": "2026-04-24 收录 1 条导读",
          "tc": "2026-04-24 收錄 1 條導讀"
        }
      },
      {
        "key": "2026-04-22",
        "label": {
          "sc": "2026-04-22",
          "tc": "2026-04-22"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260422-ils"
        ],
        "leadTitle": {
          "sc": "2026保险相连证券（ILS）研讨会：主席开幕辞（2026-04-22）",
          "tc": "2026保險相連證券（ILS）研討會：主席開幕辭（2026-04-22）"
        },
        "note": {
          "sc": "2026-04-22 收录 1 条导读",
          "tc": "2026-04-22 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "APAC 网络风险与保险峰会简报（2026-04-16）",
          "tc": "APAC 網絡風險與保險峰會簡報（2026-04-16）"
        },
        "note": {
          "sc": "2026-04-16 收录 1 条导读",
          "tc": "2026-04-16 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "保监局于北京举办专属自保论坛（2026-04-09）",
          "tc": "保監局於北京舉辦專屬自保論壇（2026-04-09）"
        },
        "note": {
          "sc": "2026-04-09 收录 1 条导读",
          "tc": "2026-04-09 收錄 1 條導讀"
        }
      },
      {
        "key": "2026-03-31",
        "label": {
          "sc": "2026-03-31",
          "tc": "2026-03-31"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260331-cpd-reporting"
        ],
        "leadTitle": {
          "sc": "CPD合规汇报安排：2025/26及后续评核期（2026-03-31）",
          "tc": "CPD合規匯報安排：2025/26及後續評核期（2026-03-31）"
        },
        "note": {
          "sc": "2026-03-31 收录 1 条导读",
          "tc": "2026-03-31 收錄 1 條導讀"
        }
      },
      {
        "key": "2026-03-27",
        "label": {
          "sc": "2026-03-27",
          "tc": "2026-03-27"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260327-cif12"
        ],
        "leadTitle": {
          "sc": "《监管通讯》第12期（2026-03）：投诉、社媒推广与合规专题",
          "tc": "《監管通訊》第12期（2026-03）：投訴、社媒推廣與合規專題"
        },
        "note": {
          "sc": "2026-03-27 收录 1 条导读",
          "tc": "2026-03-27 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "亚太医疗与健康保险会议主题演讲（2026-03-26）",
          "tc": "亞太醫療與健康保險會議主題演講（2026-03-26）"
        },
        "note": {
          "sc": "2026-03-26 收录 1 条导读",
          "tc": "2026-03-26 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "2026专属自保保险座谈会开幕致辞（2026-03-25）",
          "tc": "2026專屬自保保險座談會開幕致辭（2026-03-25）"
        },
        "note": {
          "sc": "2026-03-25 收录 1 条导读",
          "tc": "2026-03-25 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "监管机构推出 GenA.I. 沙盒++ 覆盖保险等多元金融领域（2026-03-05）",
          "tc": "監管機構推出 GenA.I. 沙盒++ 覆蓋保險等多元金融領域（2026-03-05）"
        },
        "note": {
          "sc": "2026-03-05 收录 1 条导读",
          "tc": "2026-03-05 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "保监局欢迎2026-27财政预算案中与国家规划对接的措施",
          "tc": "保監局歡迎2026-27財政預算案中與國家規劃對接的措施"
        },
        "note": {
          "sc": "2026-02-25 收录 1 条导读",
          "tc": "2026-02-25 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "保险人中介管理关键人员（KPIM）手册发布（2026-02-24）",
          "tc": "保險人中介管理關鍵人員（KPIM）手冊發布（2026-02-24）"
        },
        "note": {
          "sc": "2026-02-24 收录 1 条导读",
          "tc": "2026-02-24 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "保险创新助力低空经济发展（2026-02-13）",
          "tc": "保險創新助力低空經濟發展（2026-02-13）"
        },
        "note": {
          "sc": "2026-02-13 收录 1 条导读",
          "tc": "2026-02-13 收錄 1 條導讀"
        }
      },
      {
        "key": "2026-02-11",
        "label": {
          "sc": "2026-02-11",
          "tc": "2026-02-11"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260211-rbc-consult"
        ],
        "leadTitle": {
          "sc": "完善风险为本资本制度公众咨询启动（2026-02-11）",
          "tc": "完善風險為本資本制度公眾諮詢啟動（2026-02-11）"
        },
        "note": {
          "sc": "2026-02-11 收录 1 条导读",
          "tc": "2026-02-11 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "修订 GL16 与 GL34：长期承保与分红基金管理（2026-02-06）",
          "tc": "修訂 GL16 與 GL34：長期承保與分紅基金管理（2026-02-06）"
        },
        "note": {
          "sc": "2026-02-06 收录 1 条导读",
          "tc": "2026-02-06 收錄 1 條導讀"
        }
      },
      {
        "key": "2026-01-26",
        "label": {
          "sc": "2026-01-26",
          "tc": "2026-01-26"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260126-aff"
        ],
        "leadTitle": {
          "sc": "亚洲金融论坛2026：保监局开场发言（2026-01-26）",
          "tc": "亞洲金融論壇2026：保監局開場發言（2026-01-26）"
        },
        "note": {
          "sc": "2026-01-26 收录 1 条导读",
          "tc": "2026-01-26 收錄 1 條導讀"
        }
      },
      {
        "key": "2026-01-23",
        "label": {
          "sc": "2026-01-23",
          "tc": "2026-01-23"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260123-stats-3q2025"
        ],
        "leadTitle": {
          "sc": "2025年前三季临时统计：长期新造约2645亿，同比约+55.9%（2026-01-23）",
          "tc": "2025年前三季臨時統計：長期新造約2645億，同比約+55.9%（2026-01-23）"
        },
        "note": {
          "sc": "2026-01-23 收录 1 条导读",
          "tc": "2026-01-23 收錄 1 條導讀"
        }
      },
      {
        "key": "2026-01-15",
        "label": {
          "sc": "2026-01-15",
          "tc": "2026-01-15"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-gl34-20260331"
        ],
        "leadTitle": {
          "sc": "修订 GL34 分红业务基金管理：主体2026-03-31 生效，公司政策段2026-06-30",
          "tc": "修訂 GL34 分紅業務基金管理：主體2026-03-31 生效，公司政策段2026-06-30"
        },
        "note": {
          "sc": "2026-01-15 收录 1 条导读",
          "tc": "2026-01-15 收錄 1 條導讀"
        }
      },
      {
        "key": "2025-11-20",
        "label": {
          "sc": "2025-11-20",
          "tc": "2025-11-20"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20251120-refcheck-scheme"
        ],
        "leadTitle": {
          "sc": "保险中介人背景查核计划通函（2025-11-20）",
          "tc": "保險中介人背景查核計劃通函（2025-11-20）"
        },
        "note": {
          "sc": "2025-11-20 收录 1 条导读",
          "tc": "2025-11-20 收錄 1 條導讀"
        }
      },
      {
        "key": "2025-10-24",
        "label": {
          "sc": "2025-10-24",
          "tc": "2025-10-24"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20251024-1h2025-stats"
        ],
        "leadTitle": {
          "sc": "2025上半年临时统计：长期新造约1737亿港元，同比约+50%",
          "tc": "2025上半年臨時統計：長期新造約1737億港元，同比約+50%"
        },
        "note": {
          "sc": "2025-10-24 收录 1 条导读",
          "tc": "2025-10-24 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "负责人（RO）强制 CPD：2025/26 评估期首轮安排（2025-10-14 通函）",
          "tc": "負責人（RO）強制 CPD：2025/26 評估期首輪安排（2025-10-14 通函）"
        },
        "note": {
          "sc": "2025-10-14 收录 1 条导读",
          "tc": "2025-10-14 收錄 1 條導讀"
        }
      },
      {
        "key": "2025-09-19",
        "label": {
          "sc": "2025-09-19",
          "tc": "2025-09-19"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20250919-product-naming"
        ],
        "leadTitle": {
          "sc": "保险产品命名要求联合通函（2025-09-19）",
          "tc": "保險產品命名要求聯合通函（2025-09-19）"
        },
        "note": {
          "sc": "2025-09-19 收录 1 条导读",
          "tc": "2025-09-19 收錄 1 條導讀"
        }
      },
      {
        "key": "2025-09-01",
        "label": {
          "sc": "2025-09-01",
          "tc": "2025-09-01"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20250901-referral-fee"
        ],
        "leadTitle": {
          "sc": "分红保单转介费监管期望：50%基准（2025-09-01，10-01起遵从）",
          "tc": "分紅保單轉介費監管期望：50%基準（2025-09-01，10-01起遵從）"
        },
        "note": {
          "sc": "2025-09-01 收录 1 条导读",
          "tc": "2025-09-01 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "分红保单佣金分摊：2026-01-01 起首年不超过总额70%，其余至少分5年",
          "tc": "分紅保單佣金分攤：2026-01-01 起首年不超過總額70%，其餘至少分5年"
        },
        "note": {
          "sc": "2025-08-08 收录 2 条导读",
          "tc": "2025-08-08 收錄 2 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "经纪公司负责人强制RO-CPD自2025-08-01生效（2025-07-11）",
          "tc": "經紀公司負責人強制RO-CPD自2025-08-01生效（2025-07-11）"
        },
        "note": {
          "sc": "2025-07-11 收录 1 条导读",
          "tc": "2025-07-11 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "保监局文章：引入演示利率上限，提升投保人保障（2025-03-30）",
          "tc": "保監局文章：引入演示利率上限，提升投保人保障（2025-03-30）"
        },
        "note": {
          "sc": "2025-03-30 收录 1 条导读",
          "tc": "2025-03-30 收錄 1 條導讀"
        }
      },
      {
        "key": "2025-03-13",
        "label": {
          "sc": "2025-03-13",
          "tc": "2025-03-13"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20250313-iul-pi"
        ],
        "leadTitle": {
          "sc": "指数型万用寿险（IUL）面向专业投资者的联合通函（2025-03-13）",
          "tc": "指數型萬用壽險（IUL）面向專業投資者的聯合通函（2025-03-13）"
        },
        "note": {
          "sc": "2025-03-13 收录 1 条导读",
          "tc": "2025-03-13 收錄 1 條導讀"
        }
      },
      {
        "key": "2025-02-28",
        "label": {
          "sc": "2025-02-28",
          "tc": "2025-02-28"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20250228-illustration-cap-pn"
        ],
        "leadTitle": {
          "sc": "分红保单演示利率上限应用说明（2025-02-28）",
          "tc": "分紅保單演示利率上限應用說明（2025-02-28）"
        },
        "note": {
          "sc": "2025-02-28 收录 1 条导读",
          "tc": "2025-02-28 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "理赔管理发现与建议（2025-02-06）",
          "tc": "理賠管理發現與建議（2025-02-06）"
        },
        "note": {
          "sc": "2025-02-06 收录 1 条导读",
          "tc": "2025-02-06 收錄 1 條導讀"
        }
      }
    ],
    "weekly": [
      {
        "key": "2026-W30",
        "label": {
          "sc": "2026-W30",
          "tc": "2026-W30"
        },
        "itemCount": 4,
        "itemIds": [
          "aif-2026-save-the-date",
          "ia-public-disclosure-2026",
          "ia-q1-2026-stats",
          "hkma-complaints-20260724"
        ],
        "leadTitle": {
          "sc": "日程：Asian Insurance Forum 2026（11 月 13 日 · 保监局主办语境）",
          "tc": "日程：Asian Insurance Forum 2026（11 月 13 日 · 保監局主辦語境）"
        },
        "note": {
          "sc": "2026-W30 共 4 条",
          "tc": "2026-W30 共 4 條"
        }
      },
      {
        "key": "2026-W29",
        "label": {
          "sc": "2026-W29",
          "tc": "2026-W29"
        },
        "itemCount": 3,
        "itemIds": [
          "ia-20260716-ashk-ifoa",
          "ia-20260715-sales-practices",
          "ia-licence-20260630"
        ],
        "leadTitle": {
          "sc": "保监局刘中健：香港精算学会与英国精算师协会联合会议主题演讲（2026-07-16）",
          "tc": "保監局劉中健：香港精算學會與英國精算師協會聯合會議主題演講（2026-07-16）"
        },
        "note": {
          "sc": "2026-W29 共 3 条",
          "tc": "2026-W29 共 3 條"
        }
      },
      {
        "key": "2026-W28",
        "label": {
          "sc": "2026-W28",
          "tc": "2026-W28"
        },
        "itemCount": 3,
        "itemIds": [
          "ia-20260712-speech",
          "ia-20260710-illustration-review",
          "ia-20260708-captive"
        ],
        "leadTitle": {
          "sc": "保监局：分红保单三项监管措施落地回顾与「跨行业背景查核」推进",
          "tc": "保監局：分紅保單三項監管措施落地回顧與「跨行業背景查核」推進"
        },
        "note": {
          "sc": "2026-W28 共 3 条",
          "tc": "2026-W28 共 3 條"
        }
      },
      {
        "key": "2026-W27",
        "label": {
          "sc": "2026-W27",
          "tc": "2026-W27"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260703-rfyc"
        ],
        "leadTitle": {
          "sc": "指定无风险收益率曲线（截至2026-06-30）发布（2026-07-03）",
          "tc": "指定無風險收益率曲線（截至2026-06-30）發布（2026-07-03）"
        },
        "note": {
          "sc": "2026-W27 共 1 条",
          "tc": "2026-W27 共 1 條"
        }
      },
      {
        "key": "2026-W25",
        "label": {
          "sc": "2026-W25",
          "tc": "2026-W25"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-ai-seminar-20260615"
        ],
        "leadTitle": {
          "sc": "保监局举办「人工智能促进计划」研讨会，新增强点参与保司",
          "tc": "保監局舉辦「人工智能促進計劃」研討會，新增重點參與保司"
        },
        "note": {
          "sc": "2026-W25 共 1 条",
          "tc": "2026-W25 共 1 條"
        }
      },
      {
        "key": "2026-W23",
        "label": {
          "sc": "2026-W23",
          "tc": "2026-W23"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-hkma-remuneration-20260605"
        ],
        "leadTitle": {
          "sc": "保监局提请业界注意：金管局关于银行保险中介分红报酬结构通函",
          "tc": "保監局提請業界注意：金管局關於銀行保險中介分紅報酬結構通函"
        },
        "note": {
          "sc": "2026-W23 共 1 条",
          "tc": "2026-W23 共 1 條"
        }
      },
      {
        "key": "2026-W22",
        "label": {
          "sc": "2026-W22",
          "tc": "2026-W22"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260529-onsite-findings"
        ],
        "leadTitle": {
          "sc": "保司现场操守巡查常见问题与最佳实务（2026-05-29）",
          "tc": "保司現場操守巡查常見問題與最佳實務（2026-05-29）"
        },
        "note": {
          "sc": "2026-W22 共 1 条",
          "tc": "2026-W22 共 1 條"
        }
      },
      {
        "key": "2026-W20",
        "label": {
          "sc": "2026-W20",
          "tc": "2026-W20"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260513-cross-refcheck"
        ],
        "leadTitle": {
          "sc": "银行与保险跨行业背景查核安排通函（2026-05-13）",
          "tc": "銀行與保險跨行業背景查核安排通函（2026-05-13）"
        },
        "note": {
          "sc": "2026-W20 共 1 条",
          "tc": "2026-W20 共 1 條"
        }
      },
      {
        "key": "2026-W19",
        "label": {
          "sc": "2026-W19",
          "tc": "2026-W19"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260508-rbc-conclusions"
        ],
        "leadTitle": {
          "sc": "RBC 制度优化咨询结论发布：鼓励基建投资、巩固风险管理中心（2026-05-08）",
          "tc": "RBC 制度優化諮詢結論發布：鼓勵基建投資、鞏固風險管理中心（2026-05-08）"
        },
        "note": {
          "sc": "2026-W19 共 1 条",
          "tc": "2026-W19 共 1 條"
        }
      },
      {
        "key": "2026-W17",
        "label": {
          "sc": "2026-W17",
          "tc": "2026-W17"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-20260424-stats-2025",
          "ia-20260422-ils"
        ],
        "leadTitle": {
          "sc": "保监局公布2025年临时统计（2026-04-24）",
          "tc": "保監局公布2025年臨時統計（2026-04-24）"
        },
        "note": {
          "sc": "2026-W17 共 2 条",
          "tc": "2026-W17 共 2 條"
        }
      },
      {
        "key": "2026-W16",
        "label": {
          "sc": "2026-W16",
          "tc": "2026-W16"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260416-cyber"
        ],
        "leadTitle": {
          "sc": "APAC 网络风险与保险峰会简报（2026-04-16）",
          "tc": "APAC 網絡風險與保險峰會簡報（2026-04-16）"
        },
        "note": {
          "sc": "2026-W16 共 1 条",
          "tc": "2026-W16 共 1 條"
        }
      },
      {
        "key": "2026-W15",
        "label": {
          "sc": "2026-W15",
          "tc": "2026-W15"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260409-captive-beijing"
        ],
        "leadTitle": {
          "sc": "保监局于北京举办专属自保论坛（2026-04-09）",
          "tc": "保監局於北京舉辦專屬自保論壇（2026-04-09）"
        },
        "note": {
          "sc": "2026-W15 共 1 条",
          "tc": "2026-W15 共 1 條"
        }
      },
      {
        "key": "2026-W14",
        "label": {
          "sc": "2026-W14",
          "tc": "2026-W14"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260331-cpd-reporting"
        ],
        "leadTitle": {
          "sc": "CPD合规汇报安排：2025/26及后续评核期（2026-03-31）",
          "tc": "CPD合規匯報安排：2025/26及後續評核期（2026-03-31）"
        },
        "note": {
          "sc": "2026-W14 共 1 条",
          "tc": "2026-W14 共 1 條"
        }
      },
      {
        "key": "2026-W13",
        "label": {
          "sc": "2026-W13",
          "tc": "2026-W13"
        },
        "itemCount": 3,
        "itemIds": [
          "ia-20260327-cif12",
          "ia-20260326-health-conf",
          "ia-20260325-captive-forum-speech"
        ],
        "leadTitle": {
          "sc": "《监管通讯》第12期（2026-03）：投诉、社媒推广与合规专题",
          "tc": "《監管通訊》第12期（2026-03）：投訴、社媒推廣與合規專題"
        },
        "note": {
          "sc": "2026-W13 共 3 条",
          "tc": "2026-W13 共 3 條"
        }
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
        ],
        "leadTitle": {
          "sc": "监管机构推出 GenA.I. 沙盒++ 覆盖保险等多元金融领域（2026-03-05）",
          "tc": "監管機構推出 GenA.I. 沙盒++ 覆蓋保險等多元金融領域（2026-03-05）"
        },
        "note": {
          "sc": "2026-W10 共 1 条",
          "tc": "2026-W10 共 1 條"
        }
      },
      {
        "key": "2026-W09",
        "label": {
          "sc": "2026-W09",
          "tc": "2026-W09"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-budget-20260225",
          "ia-20260224-kpim-handbook"
        ],
        "leadTitle": {
          "sc": "保监局欢迎2026-27财政预算案中与国家规划对接的措施",
          "tc": "保監局歡迎2026-27財政預算案中與國家規劃對接的措施"
        },
        "note": {
          "sc": "2026-W09 共 2 条",
          "tc": "2026-W09 共 2 條"
        }
      },
      {
        "key": "2026-W07",
        "label": {
          "sc": "2026-W07",
          "tc": "2026-W07"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-20260213-low-altitude",
          "ia-20260211-rbc-consult"
        ],
        "leadTitle": {
          "sc": "保险创新助力低空经济发展（2026-02-13）",
          "tc": "保險創新助力低空經濟發展（2026-02-13）"
        },
        "note": {
          "sc": "2026-W07 共 2 条",
          "tc": "2026-W07 共 2 條"
        }
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
        ],
        "leadTitle": {
          "sc": "修订 GL16 与 GL34：长期承保与分红基金管理（2026-02-06）",
          "tc": "修訂 GL16 與 GL34：長期承保與分紅基金管理（2026-02-06）"
        },
        "note": {
          "sc": "2026-W06 共 1 条",
          "tc": "2026-W06 共 1 條"
        }
      },
      {
        "key": "2026-W05",
        "label": {
          "sc": "2026-W05",
          "tc": "2026-W05"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260126-aff"
        ],
        "leadTitle": {
          "sc": "亚洲金融论坛2026：保监局开场发言（2026-01-26）",
          "tc": "亞洲金融論壇2026：保監局開場發言（2026-01-26）"
        },
        "note": {
          "sc": "2026-W05 共 1 条",
          "tc": "2026-W05 共 1 條"
        }
      },
      {
        "key": "2026-W04",
        "label": {
          "sc": "2026-W04",
          "tc": "2026-W04"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20260123-stats-3q2025"
        ],
        "leadTitle": {
          "sc": "2025年前三季临时统计：长期新造约2645亿，同比约+55.9%（2026-01-23）",
          "tc": "2025年前三季臨時統計：長期新造約2645億，同比約+55.9%（2026-01-23）"
        },
        "note": {
          "sc": "2026-W04 共 1 条",
          "tc": "2026-W04 共 1 條"
        }
      },
      {
        "key": "2026-W03",
        "label": {
          "sc": "2026-W03",
          "tc": "2026-W03"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-gl34-20260331"
        ],
        "leadTitle": {
          "sc": "修订 GL34 分红业务基金管理：主体2026-03-31 生效，公司政策段2026-06-30",
          "tc": "修訂 GL34 分紅業務基金管理：主體2026-03-31 生效，公司政策段2026-06-30"
        },
        "note": {
          "sc": "2026-W03 共 1 条",
          "tc": "2026-W03 共 1 條"
        }
      },
      {
        "key": "2025-W47",
        "label": {
          "sc": "2025-W47",
          "tc": "2025-W47"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20251120-refcheck-scheme"
        ],
        "leadTitle": {
          "sc": "保险中介人背景查核计划通函（2025-11-20）",
          "tc": "保險中介人背景查核計劃通函（2025-11-20）"
        },
        "note": {
          "sc": "2025-W47 共 1 条",
          "tc": "2025-W47 共 1 條"
        }
      },
      {
        "key": "2025-W43",
        "label": {
          "sc": "2025-W43",
          "tc": "2025-W43"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20251024-1h2025-stats"
        ],
        "leadTitle": {
          "sc": "2025上半年临时统计：长期新造约1737亿港元，同比约+50%",
          "tc": "2025上半年臨時統計：長期新造約1737億港元，同比約+50%"
        },
        "note": {
          "sc": "2025-W43 共 1 条",
          "tc": "2025-W43 共 1 條"
        }
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
        ],
        "leadTitle": {
          "sc": "负责人（RO）强制 CPD：2025/26 评估期首轮安排（2025-10-14 通函）",
          "tc": "負責人（RO）強制 CPD：2025/26 評估期首輪安排（2025-10-14 通函）"
        },
        "note": {
          "sc": "2025-W42 共 1 条",
          "tc": "2025-W42 共 1 條"
        }
      },
      {
        "key": "2025-W38",
        "label": {
          "sc": "2025-W38",
          "tc": "2025-W38"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20250919-product-naming"
        ],
        "leadTitle": {
          "sc": "保险产品命名要求联合通函（2025-09-19）",
          "tc": "保險產品命名要求聯合通函（2025-09-19）"
        },
        "note": {
          "sc": "2025-W38 共 1 条",
          "tc": "2025-W38 共 1 條"
        }
      },
      {
        "key": "2025-W36",
        "label": {
          "sc": "2025-W36",
          "tc": "2025-W36"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20250901-referral-fee"
        ],
        "leadTitle": {
          "sc": "分红保单转介费监管期望：50%基准（2025-09-01，10-01起遵从）",
          "tc": "分紅保單轉介費監管期望：50%基準（2025-09-01，10-01起遵從）"
        },
        "note": {
          "sc": "2025-W36 共 1 条",
          "tc": "2025-W36 共 1 條"
        }
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
        ],
        "leadTitle": {
          "sc": "分红保单佣金分摊：2026-01-01 起首年不超过总额70%，其余至少分5年",
          "tc": "分紅保單佣金分攤：2026-01-01 起首年不超過總額70%，其餘至少分5年"
        },
        "note": {
          "sc": "2025-W32 共 2 条",
          "tc": "2025-W32 共 2 條"
        }
      },
      {
        "key": "2025-W28",
        "label": {
          "sc": "2025-W28",
          "tc": "2025-W28"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20250711-ro-cpd-compulsory"
        ],
        "leadTitle": {
          "sc": "经纪公司负责人强制RO-CPD自2025-08-01生效（2025-07-11）",
          "tc": "經紀公司負責人強制RO-CPD自2025-08-01生效（2025-07-11）"
        },
        "note": {
          "sc": "2025-W28 共 1 条",
          "tc": "2025-W28 共 1 條"
        }
      },
      {
        "key": "2025-W13",
        "label": {
          "sc": "2025-W13",
          "tc": "2025-W13"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20250330-illustration-article"
        ],
        "leadTitle": {
          "sc": "保监局文章：引入演示利率上限，提升投保人保障（2025-03-30）",
          "tc": "保監局文章：引入演示利率上限，提升投保人保障（2025-03-30）"
        },
        "note": {
          "sc": "2025-W13 共 1 条",
          "tc": "2025-W13 共 1 條"
        }
      },
      {
        "key": "2025-W11",
        "label": {
          "sc": "2025-W11",
          "tc": "2025-W11"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20250313-iul-pi"
        ],
        "leadTitle": {
          "sc": "指数型万用寿险（IUL）面向专业投资者的联合通函（2025-03-13）",
          "tc": "指數型萬用壽險（IUL）面向專業投資者的聯合通函（2025-03-13）"
        },
        "note": {
          "sc": "2025-W11 共 1 条",
          "tc": "2025-W11 共 1 條"
        }
      },
      {
        "key": "2025-W09",
        "label": {
          "sc": "2025-W09",
          "tc": "2025-W09"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20250228-illustration-cap-pn"
        ],
        "leadTitle": {
          "sc": "分红保单演示利率上限应用说明（2025-02-28）",
          "tc": "分紅保單演示利率上限應用說明（2025-02-28）"
        },
        "note": {
          "sc": "2025-W09 共 1 条",
          "tc": "2025-W09 共 1 條"
        }
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
        ],
        "leadTitle": {
          "sc": "理赔管理发现与建议（2025-02-06）",
          "tc": "理賠管理發現與建議（2025-02-06）"
        },
        "note": {
          "sc": "2025-W06 共 1 条",
          "tc": "2025-W06 共 1 條"
        }
      }
    ],
    "monthly": [
      {
        "key": "2026-07",
        "label": {
          "sc": "2026-07",
          "tc": "2026-07"
        },
        "itemCount": 11,
        "itemIds": [
          "aif-2026-save-the-date",
          "ia-public-disclosure-2026",
          "ia-q1-2026-stats",
          "hkma-complaints-20260724",
          "ia-20260716-ashk-ifoa",
          "ia-20260715-sales-practices",
          "ia-licence-20260630",
          "ia-20260712-speech",
          "ia-20260710-illustration-review",
          "ia-20260708-captive",
          "ia-20260703-rfyc"
        ],
        "leadTitle": {
          "sc": "日程：Asian Insurance Forum 2026（11 月 13 日 · 保监局主办语境）",
          "tc": "日程：Asian Insurance Forum 2026（11 月 13 日 · 保監局主辦語境）"
        },
        "note": {
          "sc": "2026-07 共 11 条",
          "tc": "2026-07 共 11 條"
        }
      },
      {
        "key": "2026-06",
        "label": {
          "sc": "2026-06",
          "tc": "2026-06"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-ai-seminar-20260615",
          "ia-hkma-remuneration-20260605"
        ],
        "leadTitle": {
          "sc": "保监局举办「人工智能促进计划」研讨会，新增强点参与保司",
          "tc": "保監局舉辦「人工智能促進計劃」研討會，新增重點參與保司"
        },
        "note": {
          "sc": "2026-06 共 2 条",
          "tc": "2026-06 共 2 條"
        }
      },
      {
        "key": "2026-05",
        "label": {
          "sc": "2026-05",
          "tc": "2026-05"
        },
        "itemCount": 3,
        "itemIds": [
          "ia-20260529-onsite-findings",
          "ia-20260513-cross-refcheck",
          "ia-20260508-rbc-conclusions"
        ],
        "leadTitle": {
          "sc": "保司现场操守巡查常见问题与最佳实务（2026-05-29）",
          "tc": "保司現場操守巡查常見問題與最佳實務（2026-05-29）"
        },
        "note": {
          "sc": "2026-05 共 3 条",
          "tc": "2026-05 共 3 條"
        }
      },
      {
        "key": "2026-04",
        "label": {
          "sc": "2026-04",
          "tc": "2026-04"
        },
        "itemCount": 4,
        "itemIds": [
          "ia-20260424-stats-2025",
          "ia-20260422-ils",
          "ia-20260416-cyber",
          "ia-20260409-captive-beijing"
        ],
        "leadTitle": {
          "sc": "保监局公布2025年临时统计（2026-04-24）",
          "tc": "保監局公布2025年臨時統計（2026-04-24）"
        },
        "note": {
          "sc": "2026-04 共 4 条",
          "tc": "2026-04 共 4 條"
        }
      },
      {
        "key": "2026-03",
        "label": {
          "sc": "2026-03",
          "tc": "2026-03"
        },
        "itemCount": 5,
        "itemIds": [
          "ia-20260331-cpd-reporting",
          "ia-20260327-cif12",
          "ia-20260326-health-conf",
          "ia-20260325-captive-forum-speech",
          "ia-20260305-genai-sandbox"
        ],
        "leadTitle": {
          "sc": "CPD合规汇报安排：2025/26及后续评核期（2026-03-31）",
          "tc": "CPD合規匯報安排：2025/26及後續評核期（2026-03-31）"
        },
        "note": {
          "sc": "2026-03 共 5 条",
          "tc": "2026-03 共 5 條"
        }
      },
      {
        "key": "2026-02",
        "label": {
          "sc": "2026-02",
          "tc": "2026-02"
        },
        "itemCount": 5,
        "itemIds": [
          "ia-budget-20260225",
          "ia-20260224-kpim-handbook",
          "ia-20260213-low-altitude",
          "ia-20260211-rbc-consult",
          "ia-20260206-gl16-gl34"
        ],
        "leadTitle": {
          "sc": "保监局欢迎2026-27财政预算案中与国家规划对接的措施",
          "tc": "保監局歡迎2026-27財政預算案中與國家規劃對接的措施"
        },
        "note": {
          "sc": "2026-02 共 5 条",
          "tc": "2026-02 共 5 條"
        }
      },
      {
        "key": "2026-01",
        "label": {
          "sc": "2026-01",
          "tc": "2026-01"
        },
        "itemCount": 3,
        "itemIds": [
          "ia-20260126-aff",
          "ia-20260123-stats-3q2025",
          "ia-gl34-20260331"
        ],
        "leadTitle": {
          "sc": "亚洲金融论坛2026：保监局开场发言（2026-01-26）",
          "tc": "亞洲金融論壇2026：保監局開場發言（2026-01-26）"
        },
        "note": {
          "sc": "2026-01 共 3 条",
          "tc": "2026-01 共 3 條"
        }
      },
      {
        "key": "2025-11",
        "label": {
          "sc": "2025-11",
          "tc": "2025-11"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20251120-refcheck-scheme"
        ],
        "leadTitle": {
          "sc": "保险中介人背景查核计划通函（2025-11-20）",
          "tc": "保險中介人背景查核計劃通函（2025-11-20）"
        },
        "note": {
          "sc": "2025-11 共 1 条",
          "tc": "2025-11 共 1 條"
        }
      },
      {
        "key": "2025-10",
        "label": {
          "sc": "2025-10",
          "tc": "2025-10"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-20251024-1h2025-stats",
          "ia-ro-cpd-20251014"
        ],
        "leadTitle": {
          "sc": "2025上半年临时统计：长期新造约1737亿港元，同比约+50%",
          "tc": "2025上半年臨時統計：長期新造約1737億港元，同比約+50%"
        },
        "note": {
          "sc": "2025-10 共 2 条",
          "tc": "2025-10 共 2 條"
        }
      },
      {
        "key": "2025-09",
        "label": {
          "sc": "2025-09",
          "tc": "2025-09"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-20250919-product-naming",
          "ia-20250901-referral-fee"
        ],
        "leadTitle": {
          "sc": "保险产品命名要求联合通函（2025-09-19）",
          "tc": "保險產品命名要求聯合通函（2025-09-19）"
        },
        "note": {
          "sc": "2025-09 共 2 条",
          "tc": "2025-09 共 2 條"
        }
      },
      {
        "key": "2025-08",
        "label": {
          "sc": "2025-08",
          "tc": "2025-08"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-commission-20260101",
          "ia-20250808-rbc-disclosure"
        ],
        "leadTitle": {
          "sc": "分红保单佣金分摊：2026-01-01 起首年不超过总额70%，其余至少分5年",
          "tc": "分紅保單佣金分攤：2026-01-01 起首年不超過總額70%，其餘至少分5年"
        },
        "note": {
          "sc": "2025-08 共 2 条",
          "tc": "2025-08 共 2 條"
        }
      },
      {
        "key": "2025-07",
        "label": {
          "sc": "2025-07",
          "tc": "2025-07"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20250711-ro-cpd-compulsory"
        ],
        "leadTitle": {
          "sc": "经纪公司负责人强制RO-CPD自2025-08-01生效（2025-07-11）",
          "tc": "經紀公司負責人強制RO-CPD自2025-08-01生效（2025-07-11）"
        },
        "note": {
          "sc": "2025-07 共 1 条",
          "tc": "2025-07 共 1 條"
        }
      },
      {
        "key": "2025-03",
        "label": {
          "sc": "2025-03",
          "tc": "2025-03"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-20250330-illustration-article",
          "ia-20250313-iul-pi"
        ],
        "leadTitle": {
          "sc": "保监局文章：引入演示利率上限，提升投保人保障（2025-03-30）",
          "tc": "保監局文章：引入演示利率上限，提升投保人保障（2025-03-30）"
        },
        "note": {
          "sc": "2025-03 共 2 条",
          "tc": "2025-03 共 2 條"
        }
      },
      {
        "key": "2025-02",
        "label": {
          "sc": "2025-02",
          "tc": "2025-02"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-20250228-illustration-cap-pn",
          "ia-20250206-claims-mgmt"
        ],
        "leadTitle": {
          "sc": "分红保单演示利率上限应用说明（2025-02-28）",
          "tc": "分紅保單演示利率上限應用說明（2025-02-28）"
        },
        "note": {
          "sc": "2025-02 共 2 条",
          "tc": "2025-02 共 2 條"
        }
      }
    ],
    "yearly": [
      {
        "key": "2026",
        "label": {
          "sc": "2026 年",
          "tc": "2026 年"
        },
        "itemCount": 33,
        "itemIds": [
          "aif-2026-save-the-date",
          "ia-public-disclosure-2026",
          "ia-q1-2026-stats",
          "hkma-complaints-20260724",
          "ia-20260716-ashk-ifoa",
          "ia-20260715-sales-practices",
          "ia-licence-20260630",
          "ia-20260712-speech",
          "ia-20260710-illustration-review",
          "ia-20260708-captive",
          "ia-20260703-rfyc",
          "ia-ai-seminar-20260615",
          "ia-hkma-remuneration-20260605",
          "ia-20260529-onsite-findings",
          "ia-20260513-cross-refcheck",
          "ia-20260508-rbc-conclusions",
          "ia-20260424-stats-2025",
          "ia-20260422-ils",
          "ia-20260416-cyber",
          "ia-20260409-captive-beijing",
          "ia-20260331-cpd-reporting",
          "ia-20260327-cif12",
          "ia-20260326-health-conf",
          "ia-20260325-captive-forum-speech",
          "ia-20260305-genai-sandbox",
          "ia-budget-20260225",
          "ia-20260224-kpim-handbook",
          "ia-20260213-low-altitude",
          "ia-20260211-rbc-consult",
          "ia-20260206-gl16-gl34",
          "ia-20260126-aff",
          "ia-20260123-stats-3q2025",
          "ia-gl34-20260331"
        ],
        "leadTitle": {
          "sc": "日程：Asian Insurance Forum 2026（11 月 13 日 · 保监局主办语境）",
          "tc": "日程：Asian Insurance Forum 2026（11 月 13 日 · 保監局主辦語境）"
        },
        "note": {
          "sc": "2026 年共 33 条",
          "tc": "2026 年共 33 條"
        }
      },
      {
        "key": "2025",
        "label": {
          "sc": "2025 年",
          "tc": "2025 年"
        },
        "itemCount": 12,
        "itemIds": [
          "ia-20251120-refcheck-scheme",
          "ia-20251024-1h2025-stats",
          "ia-ro-cpd-20251014",
          "ia-20250919-product-naming",
          "ia-20250901-referral-fee",
          "ia-commission-20260101",
          "ia-20250808-rbc-disclosure",
          "ia-20250711-ro-cpd-compulsory",
          "ia-20250330-illustration-article",
          "ia-20250313-iul-pi",
          "ia-20250228-illustration-cap-pn",
          "ia-20250206-claims-mgmt"
        ],
        "leadTitle": {
          "sc": "保险中介人背景查核计划通函（2025-11-20）",
          "tc": "保險中介人背景查核計劃通函（2025-11-20）"
        },
        "note": {
          "sc": "2025 年共 12 条",
          "tc": "2025 年共 12 條"
        }
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
        "sc": "家族办公室、跨境架构、身份/财富规划协作及相关服务生态。",
        "tc": "家族辦公室、跨境架構、身份/財富規劃協作及相關服務生態。"
      },
      "matchThemes": [
        "offshore",
        "intl"
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
        {id:"pulse",label:"今日脉搏",ico:"◈"},{id:"all",label:"全部动态",ico:"☰"},{id:"daily",label:"角色日报",ico:"▣"},{id:"download",label:"数据下载",ico:"⬇"},
        {id:"themes",label:"主题雷达",ico:"◎"},{id:"calendar",label:"监管日历",ico:"◷"},{id:"fav",label:"收藏",ico:"☆"},{id:"about",label:"关于",ico:"ⓘ"}
      ],
      sec:{c:"内容",a:"接入",m:"更多"},
      views:{
        pulse:{t:"今日脉搏",s:"按你的角色加权的高价值精选"},
        all:{t:"全部动态",s:"全量信息流 · 按信源/文种细筛（≠主题雷达）"},
        daily:{t:"角色日报",s:"固定节奏的专业早报"},download:{t:"数据下载",s:"按日/周/月/年打包导出 Markdown · 原文可溯"},
        themes:{t:"主题雷达",s:"六大业务板块地图 · 战略导航，不是信息流细筛"},
        calendar:{t:"监管日历",s:"生效日与关键窗口"},
        fav:{t:"收藏",s:"保存在本机"},
        about:{t:"关于",s:"定位、原则与免责"}
      },
      themes:{reg:"监管",product:"产品",channel:"渠道人力",macro:"宏观资产",par:"分红实现率",uw:"核保理赔",compliance:"合规实操",offshore:"跨境离岸",firm:"机构竞争",tech:"科技运营",career:"职业CPD",intl:"国际对标"},
      tier:{official:"一手监管",insurer:"保司官方",pro:"专业解读",media:"媒体"},
      hot:"当前热点", allChip:"全部", searchPh:"搜索标题 / 摘要 / 标签…", empty:"没有匹配的条目。",
      verified:"已核原文", pending:"待复核", score:"评分", cluster:"源同题", why:"为什么重要",
      actionNow:"今日动作", actionAll:"全角色动作", summary:"摘要", themesH:"主题", effective:"生效 / 相关日期",
      original:"打开原文", note:"核对提示", dayUnit:"条", roleNow:"当前角色", window:"数据窗口",
      about1:"猫圈儿港险情报站=港险相关官方/一手资讯的高效汇聚台：监管、保司官网披露、机构研究与媒体线索，导读可追溯原文。不做分红实现率数据库（公司另有专业工具）。",
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
      themesIntro:"点击主题进入全部动态并筛选。", calH:"关键节点", dailyLead:"按区块聚合的专业早报。排序随角色变化。",
      evergreen:"生效中 · 常驻",
      archiveTabs:{daily:"日报",weekly:"周报",monthly:"月报",yearly:"年报"},
      downloadHint:"按时间打包下载导读清单（日/周/月/年）。点进某期可预览条目并导出 Markdown；数字与规则以原文链接为准。",
      openDigest:"查看该期条目",
      backDownload:"返回下载列表",
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
        {id:"pulse",label:"今日脈搏",ico:"◈"},{id:"all",label:"全部動態",ico:"☰"},{id:"daily",label:"角色日報",ico:"▣"},{id:"download",label:"數據下載",ico:"⬇"},
        {id:"themes",label:"主題雷達",ico:"◎"},{id:"calendar",label:"監管日曆",ico:"◷"},{id:"fav",label:"收藏",ico:"☆"},{id:"about",label:"關於",ico:"ⓘ"}
      ],
      sec:{c:"內容",a:"接入",m:"更多"},
      views:{
        pulse:{t:"今日脈搏",s:"按你的角色加權的高價值精選"},
        all:{t:"全部動態",s:"全量資訊流 · 按信源/文種細篩（≠主題雷達）"},
        daily:{t:"角色日報",s:"固定節奏的專業早報"},download:{t:"數據下載",s:"按日/週/月/年打包導出 Markdown · 原文可溯"},
        themes:{t:"主題雷達",s:"六大業務板塊地圖 · 戰略導航，不是資訊流細篩"},
        calendar:{t:"監管日曆",s:"生效日與關鍵窗口"},
        fav:{t:"收藏",s:"保存在本機"},
        about:{t:"關於",s:"定位、原則與免責"}
      },
      themes:{reg:"監管",product:"產品",channel:"渠道人力",macro:"宏觀資產",par:"分紅實現率",uw:"核保理賠",compliance:"合規實操",offshore:"跨境離岸",firm:"機構競爭",tech:"科技運營",career:"職業CPD",intl:"國際對標"},
      tier:{official:"一手監管",insurer:"保司官方",pro:"專業解讀",media:"媒體"},
      hot:"當前熱點", allChip:"全部", searchPh:"搜尋標題 / 摘要 / 標籤…", empty:"沒有匹配的條目。",
      verified:"已核原文", pending:"待複核", score:"評分", cluster:"源同題", why:"為什麼重要",
      actionNow:"今日動作", actionAll:"全角色動作", summary:"摘要", themesH:"主題", effective:"生效 / 相關日期",
      original:"打開原文", note:"核對提示", dayUnit:"條", roleNow:"當前角色", window:"數據窗口",
      about1:"貓圈兒港險情報站=港險相關官方/一手資訊的高效匯聚台：監管、保司官網披露、機構研究與媒體線索，導讀可追溯原文。不做分紅實現率數據庫（公司另有專業工具）。",
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
      themesIntro:"點擊主題進入全部動態並篩選。", calH:"關鍵節點", dailyLead:"按區塊聚合的專業早報。排序隨角色變化。",
      evergreen:"生效中 · 常駐",
      archiveTabs:{daily:"日報",weekly:"週報",monthly:"月報",yearly:"年報"},
      downloadHint:"按時間打包下載導讀清單（日/週/月/年）。點進某期可預覽條目並導出 Markdown；數字與規則以原文連結為準。",
      openDigest:"查看該期條目",
      backDownload:"返回下載列表",
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
    theme: localStorage.getItem("hkii_theme") || "dark",
    lang: localStorage.getItem("hkii_lang") || "sc",
    q: "", themeFilter: "all", feedTier: "all", feedKind: "all", selectedId: null, archivePeriod: "daily", archiveKey: null, archiveQ: "", themeBoard: null, points: Number(localStorage.getItem("hkii_points")||"20"), pro: localStorage.getItem("hkii_pro")==="1",
    fav: new Set(JSON.parse(localStorage.getItem("hkii_fav") || "[]"))
  };

  const $ = (s, el=document) => el.querySelector(s);
  const $$ = (s, el=document) => [...el.querySelectorAll(s)];
  const T = () => L[state.lang];
  const tx = (o) => !o ? "" : (typeof o === "string" ? o : (o[state.lang] || o.sc || o.tc || ""));
  const esc = (s) => String(s??"").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");

  function applyChrome() {
    const t = T();
    document.documentElement.lang = state.lang === "tc" ? "zh-Hant" : "zh-Hans";
    document.documentElement.setAttribute("data-theme", state.theme === "light" ? "light" : "dark");
    document.title = t.brandName;
    $("#brandName").textContent = t.brandName;
    $("#brandSub").textContent = t.brandSub;
    $("#wechatPill").textContent = t.wechat;
    $("#footNote").textContent = t.foot;
    const pb=$("#pointsBar");
    if(pb){
      const mon=DATA.meta&&DATA.meta.monetization;
      const on=mon&&mon.enabled;
      pb.textContent = on ? `${t.pointsLabel} ${state.points}${state.pro?" · Pro":""}` : (tx(mon&&mon.note)||"");
    }
    $("#menuBtn").textContent = t.menu;
    $("#q").placeholder = t.searchPh;
    $$("[data-lang]").forEach(b => b.classList.toggle("on", b.dataset.lang === state.lang));
    $$("[data-theme-btn]").forEach(b => {
      b.classList.toggle("on", b.dataset.themeBtn === state.theme);
      b.textContent = b.dataset.themeBtn === "dark" ? t.dark : t.light;
    });
    const n = t.nav;
    $("#nav").innerHTML = `
      <div class="nav-section">${t.sec.c}</div>
      ${n.slice(0,7).map(x=>`<button class="nav-item ${state.view===x.id?'active':''}" data-view="${x.id}"><span class="ico">${x.ico}</span>${x.label}</button>`).join("")}
      <div class="nav-section">${t.sec.a}</div>
      ${n.slice(7,8).map(x=>`<button class="nav-item ${state.view===x.id?'active':''}" data-view="${x.id}"><span class="ico">${x.ico}</span>${x.label}</button>`).join("")}
      <div class="nav-section">${t.sec.m}</div>
      ${n.slice(8).map(x=>`<button class="nav-item ${state.view===x.id?'active':''}" data-view="${x.id}"><span class="ico">${x.ico}</span>${x.label}</button>`).join("")}`;
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
  function list({featuredOnly=false,favOnly=false,forceTime=false}={}) {
    let arr = DATA.items.slice();
    if (featuredOnly) arr = arr.filter(i=>i.featured);
    if (favOnly) arr = arr.filter(i=>state.fav.has(i.id));
    // 全部动态：信源 × 文种（细维度）
    if (state.view === "all") {
      if (state.feedTier && state.feedTier !== "all") arr = arr.filter(i => i.sourceTier === state.feedTier);
      if (state.feedKind && state.feedKind !== "all") arr = arr.filter(i => (i.contentKind || "other") === state.feedKind);
    } else if (state.themeFilter && state.themeFilter !== "all") {
      // 脉搏等：仍可用主题码（非六大板块）
      arr = arr.filter(i => (i.themes || []).includes(state.themeFilter) || (i.boards || []).includes(state.themeFilter));
    }
    arr = arr.filter(matches);
    // 全部动态 / 显式要求：严格发布时间降序（筛选不改变排序键）
    // 其他视图：角色加权优先，时间次之
    if (forceTime || state.view === "all" || state.view === "fav" || state.view === "download") {
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
      <div class="card-time">${fmtTime(it.publishedAt)}</div>
      <div class="card-body">
        <h3 class="card-title">${esc(tx(it.title))}</h3>
        <p class="card-sum">${esc(tx(it.summary))}</p>
        <div class="meta-row">
          <span class="badge ${it.sourceTier}">${t.tier[it.sourceTier]||it.sourceTier}</span>
          <span class="badge">${t.score} ${it.score}</span>
          <span class="badge verify-${it.verifyStatus}">${it.verifyStatus==='verified'?t.verified:t.pending}</span>
          ${it.clusterCount?`<span class="badge">${it.clusterCount} ${t.cluster}</span>`:''}
          ${tags}
        </div>
      </div>
      <div class="card-side">
        <button type="button" class="star ${state.fav.has(it.id)?'on':''}" data-fav="${it.id}">☆</button>
        <div class="impact">${dots(imp)}</div>
      </div>
    </article>`;
  }
  function feed(items){
    const t=T();
    if(!items.length) return `<div class="empty">${t.empty}</div>`;
    // 先按时间降序，再按日分组，日组也降序，组内再保时间降序
    const sorted = items.slice().sort(byPublishedDesc);
    const map=new Map();
    sorted.forEach(it=>{const d=fmtDay(it.publishedAt); if(!map.has(d.key)) map.set(d.key,{meta:d,items:[]}); map.get(d.key).items.push(it);});
    const groups = [...map.values()].sort((a,b)=> (b.meta.key||"").localeCompare(a.meta.key||""));
    groups.forEach(g=> g.items.sort(byPublishedDesc));
    return groups.map(g=>`<div class="day-head"><h3>${g.meta.label}</h3><span>${g.meta.week} · ${g.items.length} ${t.dayUnit}</span></div>${g.items.map(card).join("")}`).join("");
  }
  function chips(active){
    const t=T();
    // 全部动态：信源 × 文种（与主题雷达六大板块刻意分离）
    if(state.view === "all"){
      const facets = DATA.feedFacets || {};
      const tiers = facets.sourceTiers || [];
      const kinds = facets.contentKinds || [];
      const tierRow = tiers.map(f=>`<button type="button" class="chip ${state.feedTier===f.id?'on':''}" data-feed-tier="${f.id}">${f.icon||""} ${esc(tx(f.title))}</button>`).join("");
      const kindRow = kinds.map(f=>`<button type="button" class="chip ${state.feedKind===f.id?'on':''}" data-feed-kind="${f.id}">${f.icon||""} ${esc(tx(f.title))}</button>`).join("");
      return `<div class="facet-stack">
        <div class="facet-hint">${esc(t.facetHint||"")}</div>
        <div class="facet-row"><span class="facet-label">${esc(t.facetSource||"信源")}</span><div class="chips">${tierRow}</div></div>
        <div class="facet-row"><span class="facet-label">${esc(t.facetKind||"文种")}</span><div class="chips">${kindRow}</div></div>
      </div>`;
    }
    // 脉搏等：用 12 主题细码（仍不等于六大板块地图）
    return `<div class="chips"><button type="button" class="chip ${active==='all'||!active?'on':''}" data-theme-filter="all">${t.allChip}</button>${Object.entries(t.themes).map(([k,v])=>`<button type="button" class="chip ${active===k?'on':''}" data-theme-filter="${k}">${v}</button>`).join("")}</div>`;
  }
  function hot(){
    const t=T();
    const items=(DATA.hot||[]).map(byId).filter(Boolean);
    if(!items.length) return "";
    return `<section class="hot"><div class="hot-label">${t.hot}</div><ol>${items.map((it,i)=>`<li><button type="button" data-open="${it.id}">${i+1}. ${esc(tx(it.title))}</button></li>`).join("")}</ol></section>`;
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
    if(state.view==="pulse"){
      // evergreen
      const eg=(DATA.evergreen||[]).map(byId).filter(Boolean).filter(matches);
      if(eg.length){
        html+=`<div class="panel evergreen"><h3>${t.evergreen}</h3><p style="margin:0 0 8px;font-size:12px;color:var(--text-dim)">${t.fidelityText}</p>${eg.map(card).join("")}</div>`;
      }
      html+=hot()+chips(state.themeFilter)+feed(list({featuredOnly:true}));
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
    else if(state.view==="fav") html+=feed(list({favOnly:true}));
    else if(state.view==="daily"){
      const d=DATA.daily||{date:"",sections:[]};
      html+=`<div class="panel"><h3>${meta.t} · ${esc(d.date||"")}</h3><p>${t.dailyLead}</p></div>`;
      (d.sections||[]).forEach(sec=>{
        const items=(sec.itemIds||[]).map(byId).filter(Boolean).filter(matches);
        html+=`<div class="day-head"><h3>${esc(tx(sec.title))}</h3><span>${items.length} ${t.dayUnit}</span></div>${items.map(card).join("")||`<div class="empty">${t.empty}</div>`}`;
      });
    } else if(state.view==="themes"){
      const boards = DATA.boards || [];
      const byBoard = (bid) => DATA.items.filter(it => (it.boards||[]).includes(bid)).filter(matches)
        .sort((a,b)=> (b.publishedAt||"").localeCompare(a.publishedAt||"") || (b.score||0)-(a.score||0));

      if(state.themeBoard){
        const b = boards.find(x=>x.id===state.themeBoard) || {id:state.themeBoard,title:{sc:state.themeBoard},icon:"◎",desc:{sc:""}};
        const its = byBoard(state.themeBoard);
        html += `<div class="panel board-hero">
          <button type="button" class="pill" data-board-back="1">← ${t.boardBack||"返回"}</button>
          <div class="board-hero-row">
            <div class="board-hero-ico">${b.icon||"◎"}</div>
            <div>
              <h3 style="margin:0 0 6px;font-size:22px">${esc(tx(b.title))}</h3>
              <p style="margin:0;color:var(--text-muted)">${esc(tx(b.desc))}</p>
              <p style="margin:8px 0 0;font-size:12px;color:var(--text-dim)">${its.length} ${t.boardCount||"条"}</p>
            </div>
          </div>
        </div>`;
        html += its.length ? feed(its) : `<div class="empty">${t.empty}</div>`;
      } else {
        html += `<div class="topics-head">
          <div class="topics-kicker">TOPICS · ${t.boardMap||"主题地图"}</div>
          <h3 class="topics-title">${meta.t}</h3>
          <p class="topics-sub">${t.boardHint||""}</p>
        </div>`;
        html += `<div class="board-grid">` + boards.map(b=>{
          const its = byBoard(b.id);
          const top = its.slice(0,3);
          const headlines = top.map(it=>`<li>${esc(tx(it.title))}</li>`).join("") || `<li class="muted">—</li>`;
          return `<button type="button" class="board-card" data-board="${b.id}">
            <div class="board-card-top">
              <div class="board-ico">${b.icon||"◎"}</div>
              <div class="board-meta">
                <div class="board-name">${esc(tx(b.title))}</div>
                <div class="board-n">${its.length} ${t.boardCount||""}</div>
              </div>
            </div>
            <p class="board-desc">${esc(tx(b.desc))}</p>
            <div class="board-latest-label">${t.boardLatest||"最新"}</div>
            <ul class="board-headlines">${headlines}</ul>
            <div class="board-cta">${t.boardViewAll||"进入板块"} →</div>
          </button>`;
        }).join("") + `</div>`;
      }
    } else if(state.view==="calendar"){
      html+=`<div class="panel"><h3>${t.calH}</h3>${(DATA.calendar||[]).map(c=>`<div class="cal-item"><div class="cal-date">${esc(c.date)}</div><div>${esc(tx(c.title))} <span class="tag">${esc(t.themes[c.theme]||"")}</span></div></div>`).join("")}</div>`;
    } 
    else if(state.view==="download"){
      const periods=["daily","weekly","monthly","yearly"];
      html+=`<div class="panel"><h3>${meta.t}</h3><p>${t.downloadHint||t.archiveHint||""}</p>
        <div class="chips">${periods.map(p=>`<button type="button" class="chip ${state.archivePeriod===p?'on':''}" data-arch-period="${p}">${t.archiveTabs[p]}</button>`).join("")}</div>
      </div>`;
      const digests=(DATA.digests&&DATA.digests[state.archivePeriod])||[];
      if(state.archiveKey){
        const dig=digests.find(x=>x.key===state.archiveKey);
        if(!dig){ html+=`<div class="empty">${t.noDigest}</div>`; }
        else {
          const gate=canExportDigest(state.archivePeriod);
          const price=(mon().prices&&mon().prices[state.archivePeriod])||0;
          const exportLabel = (!mon().enabled || gate.free) ? t.digestExport : (gate.ok? `${t.digestExport}` : `${t.digestExport} · ${t.proLock}`);
          html+=`<div class="panel"><button type="button" class="pill" data-arch-back="1">← ${t.backDownload||t.backArchive||"返回"}</button>
            <h3 style="margin-top:12px">${esc(tx(dig.label))}</h3>
            <p>${t.itemsInPeriod}：${dig.itemCount} · ${esc(tx(dig.note||{}))}</p>
            <div class="action-bar">
              <button type="button" class="btn primary" data-export-digest="1">${exportLabel}${(!mon().enabled||price===0)?"":` <span class="pro-tag">${price?price+"pts":t.proFree}</span>`}</button>
            </div>
            <p class="lock-note">${mon().enabled? (gate.ok? (gate.free?t.proFree:t.unlocked) : t.proNeed.replace("{n}", String(price))) : (tx(mon().note)||"")}</p>
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
        if(!list.length) html+=`<div class="empty">${t.noDigest}</div>`;
        else {
          html+=`<div class="arch-list">`+list.map(dig=>{
            const lead=tx(dig.leadTitle||{})||"";
            return `<button type="button" class="arch-row" data-arch-key="${esc(dig.key)}">
              <div class="arch-date">${esc(tx(dig.label))}</div>
              <div class="arch-lead">${esc(lead)}</div>
              <div class="arch-count">${dig.itemCount}</div>
            </button>`;
          }).join("")+`</div>`;
        }
      }
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
          <div class="qr-placeholder" id="qrCode">[公众号二维码]</div>
          <p><strong>${t.wechat}</strong></p>
          <p class="qr-tip">${t.qrTip}</p>
        </div>
      </div>
      <div class="panel"><h3>${t.fidelity}</h3><p>${esc(t.fidelityText)}</p></div>
      <div class="panel"><h3>${t.principles}</h3><ul><li>${esc(t.p1)}</li><li>${esc(t.p2)}</li><li>${esc(t.p3)}</li><li>${esc(t.p4)}</li></ul></div>
      <div class="panel"><h3>${t.positioningH}</h3><p>${esc(tx((DATA.meta&&DATA.meta.positioning)||{}))}</p></div>
      <div class="panel"><h3>${t.disclaimer}</h3><p>${esc(t.disc)}</p></div>`;
      html+=`<div class="panel"><h3>${t.brandName}</h3><p>${t.about1}</p><p>${t.about2}</p><p>${esc(tx((DATA.meta&&DATA.meta.positioning)||{}))}</p></div><div class="panel"><h3>${t.fidelity}</h3><p>${t.fidelityText}</p><p>${t.downloadHint||t.archiveHint||""}</p></div><div class="panel"><h3>${t.principles}</h3><ul><li>${t.p1}</li><li>${t.p2}</li><li>${t.p3}</li><li>${t.p4}</li></ul></div><div class="panel"><h3>Pro / 积分（规划）</h3>
      <p>${esc(tx((mon().note)||{}))}</p>
      <p>免费：浏览、收藏、单条 MD、海报、日报导出。周/月/年打包下载可积分或 Pro（当前锁：${mon().enabled?"开":"关-对内全免费"}）。</p>
      </div>
      <div class="panel"><h3>${t.disclaimer}</h3><p>${t.disc}</p></div>`;
    }
    $("#content").innerHTML=html;
  }


  function savePoints(){ localStorage.setItem("hkii_points", String(state.points)); }
  function mon(){ return (DATA.meta && DATA.meta.monetization) || {enabled:false,prices:{}}; }
  function canExportDigest(period){
    const m=mon();
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
  function posterBullets(it){
    // extract short sharable bullets - no commission numbers heavy detail
    const sum=tx(it.summary)||"";
    const why=tx(it.why)||"";
    const act=tx(it.actions&&it.actions[state.role])||"";
    const cut=(s,n)=>{s=(s||"").replace(/\s+/g," ").trim(); return s.length>n?s.slice(0,n-1)+"…":s;};
    // avoid posting raw commission if user might share externally - soften
    const soft=s=>s.replace(/不超过总额\d+%/g,"结构已调整").replace(/不超過總額\d+%/g,"結構已調整").replace(/\d+%/g, (m)=>m); 
    return [cut(soft(sum),72), cut(soft(why),56), cut(soft(act),48)].filter(Boolean);
  }
  function isMomentsFriendly(it){
    // internal-heavy: RO CPD details etc still ok but mark
    const blob=(tx(it.title)+tx(it.summary));
    if(/巡查常见|汇報安排|匯報安排|KPIM|申报表/.test(blob)) return false;
    return true;
  }
  function drawPoster(it){
    const canvas=$("#posterCanvas"); if(!canvas) return;
    const ctx=canvas.getContext("2d");
    const W=1080,H=1350; canvas.width=W; canvas.height=H;
    const t=T();
    // background warm dark + gold
    const g=ctx.createLinearGradient(0,0,0,H);
    g.addColorStop(0,"#1a140c"); g.addColorStop(0.55,"#0f1218"); g.addColorStop(1,"#0a0e14");
    ctx.fillStyle=g; ctx.fillRect(0,0,W,H);
    // gold frame
    ctx.strokeStyle="rgba(232,165,75,0.45)"; ctx.lineWidth=4;
    ctx.strokeRect(48,48,W-96,H-96);
    // brand
    ctx.fillStyle="#e8a54b"; ctx.font="700 36px sans-serif";
    ctx.fillText("猫圈儿 · 港险情报", 90, 130);
    ctx.fillStyle="rgba(232,237,245,0.55)"; ctx.font="400 26px sans-serif";
    ctx.fillText(tx(it.source).slice(0,42), 90, 175);
    // board badge
    const bid=(it.boards&&it.boards[0])||"reg";
    const board=(DATA.boards||[]).find(b=>b.id===bid);
    ctx.fillStyle="rgba(232,165,75,0.16)";
    roundRect(ctx,90,210,320,56,28); ctx.fill();
    ctx.fillStyle="#e8a54b"; ctx.font="600 28px sans-serif";
    ctx.fillText(`${board?board.icon:""} ${board?tx(board.title):""}`.trim().slice(0,14), 115, 248);
    // title
    ctx.fillStyle="#e8edf5";
    wrapText(ctx, tx(it.title), 90, 340, W-180, 52, "700 44px sans-serif", 4);
    // divider
    ctx.strokeStyle="rgba(232,165,75,0.35)"; ctx.beginPath(); ctx.moveTo(90,560); ctx.lineTo(W-90,560); ctx.stroke();
    // bullets
    const bullets=posterBullets(it);
    let y=620;
    bullets.forEach((b,i)=>{
      ctx.fillStyle="#e8a54b"; ctx.font="700 28px sans-serif"; ctx.fillText(["①","②","③"][i]||"•", 90, y);
      ctx.fillStyle="rgba(232,237,245,0.88)";
      y = wrapText(ctx, b, 150, y-8, W-240, 40, "400 30px sans-serif", 3) + 36;
    });
    // footer
    ctx.fillStyle="rgba(232,165,75,0.9)"; ctx.font="600 24px sans-serif";
    ctx.fillText("专业分享 · 非销售邀约 · 详情以监管/保司原文为准", 90, H-160);
    ctx.fillStyle="rgba(232,237,245,0.45)"; ctx.font="400 22px sans-serif";
    const url=(it.originalUrl||"").replace(/^https?:\/\//,"").slice(0,52);
    ctx.fillText(url ? ("原文："+url) : "请在情报站打开原文核对", 90, H-115);
    ctx.fillText("维港猫圈儿", 90, H-70);
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
        if(lines>=maxLines-1){ // rest
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
      const a=document.createElement("a");
      a.href=$("#posterCanvas").toDataURL("image/png");
      a.download=`猫圈儿-海报-${it.id}.png`; a.click();
      state.points+=5; savePoints(); applyChrome();
    };
    $("#posterCopy").onclick=async()=>{
      const bullets=posterBullets(it).map((b,i)=>`${i+1}. ${b}`).join("\n");
      const text=`【${tx(it.title)}】\n\n${bullets}\n\n原文：${it.originalUrl||""}\n——猫圈儿港险情报站 · 专业分享非销售邀约`;
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
  $("#q").addEventListener("input", e=>{ state.q=e.target.value; render(); });
  $("#content").addEventListener("click", e=>{
    const fav=e.target.closest("[data-fav]"); if(fav){ e.stopPropagation(); const id=fav.dataset.fav; state.fav.has(id)?state.fav.delete(id):state.fav.add(id); localStorage.setItem("hkii_fav", JSON.stringify([...state.fav])); render(); return; }
    const o=e.target.closest("[data-open]"); if(o){ openDrawer(o.dataset.open); return; }
    // 主题雷达：进板块页（不跳全部动态）
    const bb=e.target.closest("[data-board-back]"); if(bb){ state.themeBoard=null; render(); return; }
    const bd=e.target.closest("[data-board]"); if(bd){ state.themeBoard=bd.dataset.board; render(); return; }
    const ft=e.target.closest("[data-feed-tier]"); if(ft){ state.feedTier=ft.dataset.feedTier; render(); return; }
    const fk=e.target.closest("[data-feed-kind]"); if(fk){ state.feedKind=fk.dataset.feedKind; render(); return; }
    const bf=e.target.closest("[data-board-filter]"); if(bf){ state.themeFilter=bf.dataset.boardFilter; render(); return; }
    // 档案
    const ap=e.target.closest("[data-arch-period]"); if(ap){ state.archivePeriod=ap.dataset.archPeriod; state.archiveKey=null; render(); return; }
    const ab=e.target.closest("[data-arch-back]"); if(ab){ state.archiveKey=null; render(); return; }
    const ak=e.target.closest("[data-arch-key]"); if(ak){ state.archiveKey=ak.dataset.archKey; render(); return; }
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
