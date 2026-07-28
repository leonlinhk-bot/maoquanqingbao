window.HKII_DATA = {
  "meta": {
    "product": "猫圈儿港险情报站",
    "generatedAt": "2026-07-28T14:00:00+08:00",
    "itemCount": 169,
    "windowNote": {
      "sc": "本库171条。",
      "tc": "本庫171條。"
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
      "sourceKey": "fstb:fo-3384-202602"
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
      "sourceKey": "hk:fo-tax-20260612"
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
      "sourceKey": "hk:newcies-3000-2026"
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
      "sourceKey": "ia:insurtech-2025"
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
      "sourceKey": "hkma:genai-sandbox-2026"
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
      "sourceKey": "evident:ai-tracker-2026"
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
      "sourceKey": "empf:fee-reduction-2026"
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
      "sourceKey": "nfra:crossborder-no-202408"
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
      "sourceKey": "nfra:hkmo-insurance-202502"
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
      "sourceKey": "ratings:consolidated-2026"
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
      "sourceKey": "sunlife:sp-upgrade-202603"
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
      "sourceKey": "sfc:wmc-202511"
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
      "sourceKey": "ia:annual-stats-2024"
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
      "sourceKey": "ia:complaints-2025"
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
      "sourceKey": "ia:full-year-2025"
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
      "sourceKey": "ia:annual-report-2024-25"
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
      "sourceKey": "fstb:density-2024"
    },
    {
      "id": "ebact-2025-hk-market",
      "clusterCount": 1,
      "score": 76,
      "verifyStatus": "pending",
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
      "sourceKey": "ebact:hk-market-2025"
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
      "sourceKey": "fsdc:insurance-hub-2025"
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
      "sourceKey": "dlapiper:gl16-202602"
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
      "sourceKey": "dlapiper:commission-202508"
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
      "sourceKey": "insbus:hk-growth-20260725"
    },
    {
      "id": "creditsights-2026-2h",
      "clusterCount": 1,
      "score": 78,
      "verifyStatus": "pending",
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
      "sourceKey": "creditsights:2h26-outlook"
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
      "sourceKey": "zhihu:top10-2025"
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
      "sourceKey": "linkedin:hk-trends-2024"
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
      "sourceKey": "swissre:sigma-202607"
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
      "sourceKey": "allianz:global-report-20260528"
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
      "sourceKey": "goldman:macro-2026"
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
      "sourceKey": "rga:hk-market-2026"
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
      "sourceKey": "deloitte:insurance-outlook-2026"
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
      "sourceKey": "jpmorgan:outlook-2026"
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
      "sourceKey": "aia:annual-2024"
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
      "sourceKey": "ctflife:rebrand-20240723"
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
      "sourceKey": "sunlife:fwd-pension-2024"
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
      "sourceKey": "aia:annual-2025"
    },
    {
      "id": "aia-20250708-global-prosper",
      "clusterCount": 1,
      "score": 80,
      "verifyStatus": "pending",
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
      "sourceKey": "aia:global-prosper-20250708"
    },
    {
      "id": "aia-20251121-aisan",
      "clusterCount": 1,
      "score": 78,
      "verifyStatus": "pending",
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
      "sourceKey": "aia:aisan-20251121"
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
      "sourceKey": "manulife:ci-20250428"
    },
    {
      "id": "manulife-20250902-hospitals",
      "clusterCount": 1,
      "score": 76,
      "verifyStatus": "pending",
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
      "sourceKey": "manulife:hospitals-20250902"
    },
    {
      "id": "axa-20250110-shengli",
      "clusterCount": 1,
      "score": 79,
      "verifyStatus": "pending",
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
      "sourceKey": "axa:shengli-20250110"
    },
    {
      "id": "axa-20250409-gba-med",
      "clusterCount": 1,
      "score": 81,
      "verifyStatus": "pending",
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
      "sourceKey": "axa:gba-med-20250409"
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
      "sourceKey": "sunlife:ape-2025"
    },
    {
      "id": "sunlife-2025-enhanced-savings",
      "clusterCount": 1,
      "score": 77,
      "verifyStatus": "pending",
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
      "sourceKey": "sunlife:enhanced-savings-2025"
    },
    {
      "id": "chubb-20260601-mylegacy",
      "clusterCount": 1,
      "score": 80,
      "verifyStatus": "pending",
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
      "sourceKey": "chubb:mylegacy-20260601"
    },
    {
      "id": "chubb-2026-dementia",
      "clusterCount": 1,
      "score": 81,
      "verifyStatus": "pending",
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
      "sourceKey": "chubb:dementia-2026"
    },
    {
      "id": "taiping-202606-rating",
      "clusterCount": 1,
      "score": 74,
      "verifyStatus": "pending",
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
      "sourceKey": "taiping:rating-20260626"
    },
    {
      "id": "cpic-20260504-gen3",
      "clusterCount": 1,
      "score": 84,
      "verifyStatus": "pending",
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
      "sourceKey": "cpic:gen3-20260504"
    },
    {
      "id": "fwd-2026-q1-update",
      "clusterCount": 1,
      "score": 80,
      "verifyStatus": "pending",
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
      "sourceKey": "fwd:q1-2026"
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
      "sourceKey": "fwd:brand-2026"
    },
    {
      "id": "hsbc-life-2026-hnw-pitchbook",
      "clusterCount": 1,
      "score": 82,
      "verifyStatus": "pending",
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
      "sourceKey": "hsbc:hnw-pitchbook-20260317"
    },
    {
      "id": "chinlife-2026-hk-digital",
      "clusterCount": 1,
      "score": 76,
      "verifyStatus": "pending",
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
      "sourceKey": "chinlife:digital-2026"
    },
    {
      "id": "aia-20260716-hyrox",
      "clusterCount": 1,
      "score": 75,
      "verifyStatus": "pending",
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
      "sourceKey": "aia:hyrox-20260716"
    },
    {
      "id": "aia-20260608-prosperlife",
      "clusterCount": 1,
      "score": 82,
      "verifyStatus": "pending",
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
      "sourceKey": "aia:prosperlife-20260608"
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
      "sourceKey": "aia:q1-vonb-20260430"
    },
    {
      "id": "prudential-20260317-youth",
      "clusterCount": 1,
      "score": 76,
      "verifyStatus": "pending",
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
      "sourceKey": "prudential:youth-20260317"
    },
    {
      "id": "prudential-20260429-self-future",
      "clusterCount": 1,
      "score": 78,
      "verifyStatus": "pending",
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
      "sourceKey": "prudential:self-future-ii-20260429"
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
      "sourceKey": "manulife:two-plans-20260105"
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
      "sourceKey": "manulife:annuity-accident-20260420"
    },
    {
      "id": "manulife-20260625-board",
      "clusterCount": 1,
      "score": 72,
      "verifyStatus": "pending",
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
      "sourceKey": "manulife:board-20260625"
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
      "sourceKey": "axa:redomicile-20260126"
    },
    {
      "id": "axa-2026-bloomberg-awards",
      "clusterCount": 1,
      "score": 74,
      "verifyStatus": "pending",
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
      "sourceKey": "axa:bloomberg-awards-2026"
    },
    {
      "id": "sunlife-2026-10life-awards",
      "clusterCount": 1,
      "score": 77,
      "verifyStatus": "pending",
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
      "sourceKey": "sunlife:10life-2026"
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
      "sourceKey": "ctflife:artisan-leap-20260422"
    },
    {
      "id": "ctflife-2026-diamond-iul",
      "clusterCount": 1,
      "score": 84,
      "verifyStatus": "pending",
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
      "sourceKey": "ctflife:diamond-iul-2026"
    },
    {
      "id": "boclife-20260427-retirement",
      "clusterCount": 1,
      "score": 80,
      "verifyStatus": "pending",
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
      "sourceKey": "boclife:retirement-20260427"
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
      "sourceKey": "ia:rbc-live-20240701"
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
      "sourceKey": "ia:refcheck-20240923"
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
      "sourceKey": "ia:h1stats-2024"
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
      "sourceKey": "ia:crossborder-2024"
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
      "sourceKey": "ia:illustration-note-20250228"
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
      "sourceKey": "ia:hkma-iul-circular-20250313"
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
      "sourceKey": "ia:h1stats-20251024"
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
      "sourceKey": "ia:q1stats-2025"
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
      "sourceKey": "ia:d-sii-2025"
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
      "sourceKey": "ia:q3stats-20260123"
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
      "sourceKey": "ia:referral-50-20250901"
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
      "sourceKey": "ia:hkma-product-naming-20250917"
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
      "sourceKey": "ia:illustration-cap-20250701"
    },
    {
      "id": "ia-202508-iul-sandbox",
      "clusterCount": 1,
      "score": 80,
      "verifyStatus": "pending",
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
      "sourceKey": "ia:iul-sandbox-20250919"
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
      "sourceKey": "ia:commission-spread-20250715"
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
      "sourceKey": "ia:gn16-20260331"
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
      "sourceKey": "ia:rbc-consult-close-20260310"
    },
    {
      "id": "manulife-202603-new-products",
      "clusterCount": 1,
      "score": 76,
      "verifyStatus": "pending",
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
      "sourceKey": "manulife:new-products-202603"
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
      "sourceKey": "ia:rbc-consult-launch-20260211"
    },
    {
      "id": "circ-20260201-crossborder",
      "clusterCount": 1,
      "score": 82,
      "verifyStatus": "pending",
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
      "sourceKey": "circ:crossborder-20260201"
    },
    {
      "id": "aia-20260424-top-insurer",
      "clusterCount": 1,
      "score": 79,
      "verifyStatus": "pending",
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
      "sourceKey": "aia:top-insurer-20260424"
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
      "sourceKey": "hkma:commission-circular-20260605"
    },
    {
      "id": "ia-ai-cohort-202606",
      "clusterCount": 1,
      "score": 81,
      "verifyStatus": "pending",
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
      "sourceKey": "ia:ai-cohort-20260618"
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
      "sourceKey": "ia:rbc-consultation-conclusion-20260508"
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
      "sourceKey": "ia:cross-ref-circular-20260513"
    },
    {
      "id": "ia-20260519-disclosure-consult",
      "clusterCount": 1,
      "score": 85,
      "verifyStatus": "pending",
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
      "sourceKey": "ia:disclosure-consult-20260519"
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
      "sourceKey": "legco:disclosure-20260520"
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
      "sourceKey": "ia:gn16-revised-20260331"
    },
    {
      "id": "legco-20260410-fa-disclosure",
      "clusterCount": 1,
      "score": 80,
      "verifyStatus": "pending",
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
      "sourceKey": "legco:fa-disclosure-20260410"
    },
    {
      "id": "ia-202604-fsi-survey",
      "clusterCount": 1,
      "score": 78,
      "verifyStatus": "pending",
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
      "sourceKey": "fsdc:insurance-hub-report-202604"
    },
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
      "sourceKey": "ia:speech-20260712"
    },
    {
      "id": "ia-20260712-speech",
      "title": {
        "sc": "保监局：分红保单三项监管措施落地回顾与「跨行业背景查核」推进。",
        "tc": "保監局：分紅保單三項監管措施落地回顧與「跨行業背景查核」推進。"
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
      "sourceKey": "ia:circular-20260710"
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
      "id": "fstb-20260708-captive",
      "clusterCount": 1,
      "score": 78,
      "verifyStatus": "pending",
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
      "sourceKey": "fstb:captives-20260708"
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
      "sourceKey": "ia:crossref-20260701"
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
      "sourceKey": "80c32beb155c",
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
      "sourceKey": "62897ec5353f",
      "boards": [
        "market"
      ],
      "contentKind": "research"
    },
    {
      "id": "ia-20260629-sunlife-notes",
      "clusterCount": 1,
      "score": 65,
      "verifyStatus": "pending",
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
      "sourceKey": "d9b5ade1f959",
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
      "sourceKey": "39a0671bd7bb",
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
      "verifyStatus": "pending",
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
      "sourceKey": "5c5ae70a7fcf",
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
      "sourceKey": "29b2cf32243c",
      "boards": [
        "market"
      ],
      "contentKind": "research"
    },
    {
      "id": "ia-20260625-manulife-convention",
      "clusterCount": 1,
      "score": 70,
      "verifyStatus": "pending",
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
      "id": "ia-20260624-rga-trends",
      "clusterCount": 1,
      "score": 65,
      "verifyStatus": "pending",
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
      "sourceKey": "463dfaad9ace",
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
      "sourceTier": "research",
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
      "sourceKey": "3b71f432cf00",
      "boards": [
        "market"
      ],
      "contentKind": "research"
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
      "sourceKey": "a81c39c44878",
      "boards": [
        "market"
      ],
      "contentKind": "research"
    },
    {
      "id": "ia-20260617-manulife-ai",
      "clusterCount": 1,
      "score": 77,
      "verifyStatus": "pending",
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
      "sourceTier": "insurer",
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
      "sourceKey": "5d6b2c5f7488",
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
      "verifyStatus": "pending",
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
      "sourceTier": "media",
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
      "sourceKey": "950097c1fdf3",
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
      "sourceTier": "official",
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
      "sourceKey": "71c330b3ad7f",
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
      "id": "ia-20260615-bloomberg-crackdown",
      "clusterCount": 1,
      "score": 88,
      "verifyStatus": "pending",
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
      "sourceKey": "57e7e795548d",
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
      "verifyStatus": "pending",
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
      "sourceKey": "4a69a7fb69e3",
      "boards": [
        "insurer",
        "product"
      ],
      "contentKind": "product_notice"
    },
    {
      "id": "ia-20260610-manulife-leverage",
      "clusterCount": 1,
      "score": 78,
      "verifyStatus": "pending",
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
      "sourceTier": "media",
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
      "sourceKey": "0fff799ebdd0",
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
      "verifyStatus": "pending",
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
      "sourceKey": "449a66631b2e",
      "boards": [
        "insurer",
        "market"
      ],
      "contentKind": "industry_news"
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
      "sourceKey": "3c6555c2829d",
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
      "verifyStatus": "pending",
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
      "sourceTier": "insurer",
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
      "sourceKey": "8f2e7b7f87f2",
      "boards": [
        "insurer",
        "family",
        "product"
      ],
      "contentKind": "product_notice"
    },
    {
      "id": "ia-20260608-aia-wealth-flexi",
      "clusterCount": 1,
      "score": 80,
      "verifyStatus": "pending",
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
      "sourceKey": "cf6228d86dbc",
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
      "sourceKey": "ee9769642cba",
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
      "id": "ia-20260611-chubb-life",
      "clusterCount": 1,
      "score": 62,
      "verifyStatus": "pending",
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
      "sourceTier": "insurer",
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
      "sourceKey": "cefa86411782",
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
      "sourceKey": "ae929e69d230",
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
      "verifyStatus": "pending",
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
      "sourceKey": "a52ee65d5d91",
      "boards": [
        "reg",
        "market"
      ],
      "contentKind": "speech"
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
        "key": "2026-07-28",
        "label": {
          "sc": "2026-07-28",
          "tc": "2026-07-28"
        },
        "itemCount": 1,
        "itemIds": [
          "ratings-2026-consolidated"
        ],
        "leadTitle": {
          "sc": "香港主要保险公司信评一览(2026更新)。",
          "tc": "香港主要保險公司信評一覽(2026更新)。"
        },
        "note": {
          "sc": "2026-07-28 收录 1 条导读",
          "tc": "2026-07-28 收錄 1 條導讀"
        }
      },
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
          "sc": "日程：Asian Insurance Forum 2026（11 月 13 日 · 保监局主办语境）。",
          "tc": "日程：Asian Insurance Forum 2026（11 月 13 日 · 保監局主辦語境）。"
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
        "itemCount": 2,
        "itemIds": [
          "insbus-202607-hk-growth",
          "ia-public-disclosure-2026"
        ],
        "leadTitle": {
          "sc": "Insurance Business深度分析：Q1毛保费2916亿+32% 跨境数据连5季缺失。",
          "tc": "Insurance Business深度分析：Q1毛保費2916億+32% 跨境數據連5季缺失。"
        },
        "note": {
          "sc": "2026-07-25 收录 2 条导读",
          "tc": "2026-07-25 收錄 2 條導讀"
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
          "sc": "2026年Q1临时统计：长期业务新造保费约1411亿港元，同比约+51.1%。",
          "tc": "2026年Q1臨時統計：長期業務新造保費約1411億港元，同比約+51.1%。"
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
        "itemCount": 2,
        "itemIds": [
          "aia-20260716-hyrox",
          "ia-20260716-ashk-ifoa"
        ],
        "leadTitle": {
          "sc": "友邦香港与HYROX香港宣布策略合作推动健康生活。",
          "tc": "友邦香港與HYROX香港宣布策略合作推動健康生活。"
        },
        "note": {
          "sc": "2026-07-16 收录 2 条导读",
          "tc": "2026-07-16 收錄 2 條導讀"
        }
      },
      {
        "key": "2026-07-15",
        "label": {
          "sc": "2026-07-15",
          "tc": "2026-07-15"
        },
        "itemCount": 2,
        "itemIds": [
          "creditsights-2026-2h",
          "ia-20260715-sales-practices"
        ],
        "leadTitle": {
          "sc": "CreditSights展望：2026下半年中港跨境资金规则或进一步收紧。",
          "tc": "CreditSights展望：2026下半年中港跨境資金規則或進一步收緊。"
        },
        "note": {
          "sc": "2026-07-15 收录 2 条导读",
          "tc": "2026-07-15 收錄 2 條導讀"
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
          "sc": "持牌中介统计（截至2026-06-30）：个人持牌约12.25万，经纪公司810家。",
          "tc": "持牌中介統計（截至2026-06-30）：個人持牌約12.25萬，經紀公司810家。"
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
        "itemCount": 2,
        "itemIds": [
          "ia-20260712-speech",
          "ia-20260712-speech"
        ],
        "leadTitle": {
          "sc": "保监局刘中健演辞：以前瞻性监管及执法维护市场健康发展。",
          "tc": "保監局劉中健演辭：以前瞻性監管及執法維護市場健康發展。"
        },
        "note": {
          "sc": "2026-07-12 收录 2 条导读",
          "tc": "2026-07-12 收錄 2 條導讀"
        }
      },
      {
        "key": "2026-07-10",
        "label": {
          "sc": "2026-07-10",
          "tc": "2026-07-10"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-20260710-illustration",
          "ia-20260710-illustration-review"
        ],
        "leadTitle": {
          "sc": "保监局就分红保单演示回报率上限发出释义文件。",
          "tc": "保監局就分紅保單演示回報率上限發出釋義文件。"
        },
        "note": {
          "sc": "2026-07-10 收录 2 条导读",
          "tc": "2026-07-10 收錄 2 條導讀"
        }
      },
      {
        "key": "2026-07-08",
        "label": {
          "sc": "2026-07-08",
          "tc": "2026-07-08"
        },
        "itemCount": 3,
        "itemIds": [
          "swissre-202607-wis",
          "fstb-20260708-captive",
          "ia-20260708-captive"
        ],
        "leadTitle": {
          "sc": "Swiss Re sigma报告：2026全球保险成为碎片化世界中的减震器。",
          "tc": "Swiss Re sigma報告：2026全球保險成為碎片化世界中的減震器。"
        },
        "note": {
          "sc": "2026-07-08 收录 3 条导读",
          "tc": "2026-07-08 收錄 3 條導讀"
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
          "sc": "指定无风险收益率曲线（截至2026-06-30）发布（2026-07-03）。",
          "tc": "指定無風險收益率曲線（截至2026-06-30）發布（2026-07-03）。"
        },
        "note": {
          "sc": "2026-07-03 收录 1 条导读",
          "tc": "2026-07-03 收錄 1 條導讀"
        }
      },
      {
        "key": "2026-07-01",
        "label": {
          "sc": "2026-07-01",
          "tc": "2026-07-01"
        },
        "itemCount": 2,
        "itemIds": [
          "rga-2026-hk-market",
          "ia-crossref-20260701"
        ],
        "leadTitle": {
          "sc": "RGA分析：2026年香港保险市场机遇与挑战——跨境需求+监管转型+AI。",
          "tc": "RGA分析：2026年香港保險市場機遇與挑戰——跨境需求+監管轉型+AI。"
        },
        "note": {
          "sc": "2026-07-01 收录 2 条导读",
          "tc": "2026-07-01 收錄 2 條導讀"
        }
      },
      {
        "key": "2026-06-30",
        "label": {
          "sc": "2026-06-30",
          "tc": "2026-06-30"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-20260630-swissre-sigma",
          "ia-20260630-allianz-report"
        ],
        "leadTitle": {
          "sc": "瑞再研究院sigma报告：全球保险在碎片化世界中扮演「减震器」，AI投资颠覆行业格局。",
          "tc": "瑞再研究院sigma報告：全球保險在碎片化世界中扮演「減震器」，AI投資顛覆行業格局。"
        },
        "note": {
          "sc": "2026-06-30 收录 2 条导读",
          "tc": "2026-06-30 收錄 2 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "永明金融宣布10亿美元有限追索资本票据利率重置。",
          "tc": "永明金融宣布10億美元有限追索資本票據利率重置。"
        },
        "note": {
          "sc": "2026-06-29 收录 2 条导读",
          "tc": "2026-06-29 收錄 2 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "金发局发布保险业人才培育报告：呼吁建设新一代保险专才。",
          "tc": "金發局發布保險業人才培育報告：呼籲建設新一代保險專才。"
        },
        "note": {
          "sc": "2026-06-28 收录 1 条导读",
          "tc": "2026-06-28 收錄 1 條導讀"
        }
      },
      {
        "key": "2026-06-26",
        "label": {
          "sc": "2026-06-26",
          "tc": "2026-06-26"
        },
        "itemCount": 3,
        "itemIds": [
          "taiping-202606-rating",
          "ia-20260626-morganstanley",
          "ia-20260626-pimco-asia"
        ],
        "leadTitle": {
          "sc": "中国太平再保险连续17年获惠誉A评级。",
          "tc": "中國太平再保險連續17年獲惠譽A評級。"
        },
        "note": {
          "sc": "2026-06-26 收录 3 条导读",
          "tc": "2026-06-26 收錄 3 條導讀"
        }
      },
      {
        "key": "2026-06-25",
        "label": {
          "sc": "2026-06-25",
          "tc": "2026-06-25"
        },
        "itemCount": 3,
        "itemIds": [
          "empf-2026-fee-reduction",
          "manulife-20260625-board",
          "ia-20260625-manulife-convention"
        ],
        "leadTitle": {
          "sc": "积金易平台降费：236只基金行政费降至0.37% 惠及千万账户。",
          "tc": "積金易平台降費：236隻基金行政費降至0.37% 惠及千萬賬戶。"
        },
        "note": {
          "sc": "2026-06-25 收录 3 条导读",
          "tc": "2026-06-25 收錄 3 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "RGA发布2026年Q2产品趋势报告：AIA财富灵活储蓄保、AXA私人平台被列为重点新品。",
          "tc": "RGA發布2026年Q2產品趨勢報告：AIA財富靈活儲蓄保、AXA私人平台被列為重點新品。"
        },
        "note": {
          "sc": "2026-06-24 收录 1 条导读",
          "tc": "2026-06-24 收錄 1 條導讀"
        }
      },
      {
        "key": "2026-06-20",
        "label": {
          "sc": "2026-06-20",
          "tc": "2026-06-20"
        },
        "itemCount": 2,
        "itemIds": [
          "fwd-2026-brand-victoria",
          "ia-20260620-goldman-outlook"
        ],
        "leadTitle": {
          "sc": "富卫香港2026品牌升级：维港双岸招牌同时亮灯。",
          "tc": "富衛香港2026品牌升級：維港雙岸招牌同時亮燈。"
        },
        "note": {
          "sc": "2026-06-20 收录 2 条导读",
          "tc": "2026-06-20 收錄 2 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "保监局AI促进计划再扩容：新增宏利等三家保司。",
          "tc": "保監局AI促進計劃再擴容：新增宏利等三家保司。"
        },
        "note": {
          "sc": "2026-06-18 收录 2 条导读",
          "tc": "2026-06-18 收錄 2 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "宏利香港加入保监局AI促进计划：AI已覆盖核保、分销与客服三线。",
          "tc": "宏利香港加入保監局AI促進計劃：AI已覆蓋核保、分銷與客服三線。"
        },
        "note": {
          "sc": "2026-06-17 收录 1 条导读",
          "tc": "2026-06-17 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "友邦及保诚在港增设高净值客户高级职位，抢占亚洲财富管理市场。",
          "tc": "友邦及保誠在港增設高淨值客戶高級職位，搶佔亞洲財富管理市場。"
        },
        "note": {
          "sc": "2026-06-16 收录 2 条导读",
          "tc": "2026-06-16 收錄 2 條導讀"
        }
      },
      {
        "key": "2026-06-15",
        "label": {
          "sc": "2026-06-15",
          "tc": "2026-06-15"
        },
        "itemCount": 3,
        "itemIds": [
          "axa-2026-bloomberg-awards",
          "ia-ai-seminar-20260615",
          "ia-20260615-bloomberg-crackdown"
        ],
        "leadTitle": {
          "sc": "AXA安盛于《彭博商业周刊》「金融机构2026」获七项殊荣。",
          "tc": "AXA安盛於《彭博商業周刊》「金融機構2026」獲七項殊榮。"
        },
        "note": {
          "sc": "2026-06-15 收录 3 条导读",
          "tc": "2026-06-15 收錄 3 條導讀"
        }
      },
      {
        "key": "2026-06-12",
        "label": {
          "sc": "2026-06-12",
          "tc": "2026-06-12"
        },
        "itemCount": 2,
        "itemIds": [
          "hk-20260612-fo-tax",
          "ia-20260612-manulife-plans"
        ],
        "leadTitle": {
          "sc": "港府2026年优化家族办公室税制：扩大免税范围至数字资产。",
          "tc": "港府2026年優化家族辦公室稅制：擴大免稅範圍至數字資產。"
        },
        "note": {
          "sc": "2026-06-12 收录 2 条导读",
          "tc": "2026-06-12 收錄 2 條導讀"
        }
      },
      {
        "key": "2026-06-10",
        "label": {
          "sc": "2026-06-10",
          "tc": "2026-06-10"
        },
        "itemCount": 3,
        "itemIds": [
          "ctflife-2026-diamond-iul",
          "ia-20260610-manulife-leverage",
          "ia-20260610-chowtaifook-life"
        ],
        "leadTitle": {
          "sc": "周大福人寿推出全港首只法国巴黎银行指数挂钩IUL计划「钻裕」",
          "tc": "周大福人壽推出全港首隻法國巴黎銀行指數掛鈎IUL計劃「鑽裕」"
        },
        "note": {
          "sc": "2026-06-10 收录 3 条导读",
          "tc": "2026-06-10 收錄 3 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "惠誉：亚太保险展望维持「中性」，监管与市场压力并存。",
          "tc": "惠譽：亞太保險展望維持「中性」，監管與市場壓力並存。"
        },
        "note": {
          "sc": "2026-06-09 收录 1 条导读",
          "tc": "2026-06-09 收錄 1 條導讀"
        }
      },
      {
        "key": "2026-06-08",
        "label": {
          "sc": "2026-06-08",
          "tc": "2026-06-08"
        },
        "itemCount": 3,
        "itemIds": [
          "aia-20260608-prosperlife",
          "ia-20260608-axa-global-private",
          "ia-20260608-aia-wealth-flexi"
        ],
        "leadTitle": {
          "sc": "友邦推出「财富盈活储蓄保险计划」瞄准高净值家庭传承。",
          "tc": "友邦推出「財富盈活儲蓄保險計劃」瞄準高淨值家庭傳承。"
        },
        "note": {
          "sc": "2026-06-08 收录 3 条导读",
          "tc": "2026-06-08 收錄 3 條導讀"
        }
      },
      {
        "key": "2026-06-05",
        "label": {
          "sc": "2026-06-05",
          "tc": "2026-06-05"
        },
        "itemCount": 3,
        "itemIds": [
          "ia-20260605-hkma-commission",
          "ia-20260605-hkma-remuneration-circ",
          "ia-hkma-remuneration-20260605"
        ],
        "leadTitle": {
          "sc": "金管局就银行保险中介佣金分摊发出通函。",
          "tc": "金管局就銀行保險中介佣金分攤發出通函。"
        },
        "note": {
          "sc": "2026-06-05 收录 3 条导读",
          "tc": "2026-06-05 收錄 3 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "安达人寿香港增强旗舰储蓄计划：新增3年缴付选项。",
          "tc": "安達人壽香港增強旗艦儲蓄計劃：新增3年繳付選項。"
        },
        "note": {
          "sc": "2026-06-04 收录 1 条导读",
          "tc": "2026-06-04 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "保监局对两间经纪公司施加续牌条件：暂停接收转介客户。",
          "tc": "保監局對兩間經紀公司施加續牌條件：暫停接收轉介客戶。"
        },
        "note": {
          "sc": "2026-06-03 收录 1 条导读",
          "tc": "2026-06-03 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "金管局举办银保跨境业务简报会：促进银行与保险业界合作。",
          "tc": "金管局舉辦銀保跨境業務簡報會：促進銀行與保險業界合作。"
        },
        "note": {
          "sc": "2026-06-02 收录 1 条导读",
          "tc": "2026-06-02 收錄 1 條導讀"
        }
      },
      {
        "key": "2026-06-01",
        "label": {
          "sc": "2026-06-01",
          "tc": "2026-06-01"
        },
        "itemCount": 2,
        "itemIds": [
          "deloitte-2026-insurance-outlook",
          "chubb-20260601-mylegacy"
        ],
        "leadTitle": {
          "sc": "德勤2026全球保险展望：AI落地加速 香港保监局推AI促进计划。",
          "tc": "德勤2026全球保險展望：AI落地加速 香港保監局推AI促進計劃。"
        },
        "note": {
          "sc": "2026-06-01 收录 2 条导读",
          "tc": "2026-06-01 收錄 2 條導讀"
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
          "sc": "保司现场操守巡查常见问题与最佳实务（2026-05-29）。",
          "tc": "保司現場操守巡查常見問題與最佳實務（2026-05-29）。"
        },
        "note": {
          "sc": "2026-05-29 收录 1 条导读",
          "tc": "2026-05-29 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "安联全球保险报告2026：全球保费+7.1%至6.9万亿欧元 亚洲领跑。",
          "tc": "安聯全球保險報告2026：全球保費+7.1%至6.9萬億歐元 亞洲領跑。"
        },
        "note": {
          "sc": "2026-05-28 收录 1 条导读",
          "tc": "2026-05-28 收錄 1 條導讀"
        }
      },
      {
        "key": "2026-05-20",
        "label": {
          "sc": "2026-05-20",
          "tc": "2026-05-20"
        },
        "itemCount": 2,
        "itemIds": [
          "fwd-2026-q1-update",
          "ia-20260520-gl34-corp"
        ],
        "leadTitle": {
          "sc": "富卫集团2026年Q1新业务强劲：年化新保费+4%至7.2亿美元。",
          "tc": "富衛集團2026年Q1新業務強勁：年化新保費+4%至7.2億美元。"
        },
        "note": {
          "sc": "2026-05-20 收录 2 条导读",
          "tc": "2026-05-20 收錄 2 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "保监局就保险人公开披露规则咨询市场。",
          "tc": "保監局就保險人公開披露規則諮詢市場。"
        },
        "note": {
          "sc": "2026-05-19 收录 1 条导读",
          "tc": "2026-05-19 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "Sun Life永明连续4年获10Life 5星保险大奖。",
          "tc": "Sun Life永明連續4年獲10Life 5星保險大獎。"
        },
        "note": {
          "sc": "2026-05-15 收录 1 条导读",
          "tc": "2026-05-15 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "银行与保险跨行业背景查核安排通函发布。",
          "tc": "銀行與保險跨行業背景查核安排通函發布。"
        },
        "note": {
          "sc": "2026-05-13 收录 2 条导读",
          "tc": "2026-05-13 收錄 2 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "保监局公布RBC制度优化咨询结论：鼓励基建投资、巩固风险管理中心。",
          "tc": "保監局公布RBC制度優化諮詢結論：鼓勵基建投資、鞏固風險管理中心。"
        },
        "note": {
          "sc": "2026-05-08 收录 2 条导读",
          "tc": "2026-05-08 收錄 2 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "太保寿险香港推出「世代悦享3」储蓄保险计划——35周年献礼。",
          "tc": "太保壽險香港推出「世代悅享3」儲蓄保險計劃——35周年獻禮。"
        },
        "note": {
          "sc": "2026-05-04 收录 1 条导读",
          "tc": "2026-05-04 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "AIA 2026年Q1新业务价值增长13% 香港表现强劲。",
          "tc": "AIA 2026年Q1新業務價值增長13% 香港表現強勁。"
        },
        "note": {
          "sc": "2026-04-30 收录 1 条导读",
          "tc": "2026-04-30 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "保诚推出「自主未来」保险计划II 产品发布会。",
          "tc": "保誠推出「自主未來」保險計劃II 產品發佈會。"
        },
        "note": {
          "sc": "2026-04-29 收录 1 条导读",
          "tc": "2026-04-29 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "中银人寿联乘中银香港推出「退优·新活」综合养老方案。",
          "tc": "中銀人壽聯乘中銀香港推出「退優·新活」綜合養老方案。"
        },
        "note": {
          "sc": "2026-04-27 收录 1 条导读",
          "tc": "2026-04-27 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "保监局公布2025全年业绩：个人新单保费3309亿港元 +50.6%再创新高。",
          "tc": "保監局公布2025全年業績：個人新單保費3309億港元 +50.6%再創新高。"
        },
        "note": {
          "sc": "2026-04-25 收录 1 条导读",
          "tc": "2026-04-25 收錄 1 條導讀"
        }
      },
      {
        "key": "2026-04-24",
        "label": {
          "sc": "2026-04-24",
          "tc": "2026-04-24"
        },
        "itemCount": 2,
        "itemIds": [
          "aia-20260424-top-insurer",
          "ia-20260424-stats-2025"
        ],
        "leadTitle": {
          "sc": "AIA连续获评为香港首选保险公司。",
          "tc": "AIA連續獲評為香港首選保險公司。"
        },
        "note": {
          "sc": "2026-04-24 收录 2 条导读",
          "tc": "2026-04-24 收錄 2 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "周大福人寿推出「匠心·飞越」储蓄保险计划。",
          "tc": "周大福人壽推出「匠心·飛越」儲蓄保險計劃。"
        },
        "note": {
          "sc": "2026-04-22 收录 2 条导读",
          "tc": "2026-04-22 收錄 2 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "宏利推出全新年金及意外保险：宏瑞终身即期年金+相伴无忧个人意外。",
          "tc": "宏利推出全新年金及意外保險：宏瑞終身即期年金+相伴無憂個人意外。"
        },
        "note": {
          "sc": "2026-04-20 收录 1 条导读",
          "tc": "2026-04-20 收錄 1 條導讀"
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
          "sc": "APAC 网络风险与保险峰会简报（2026-04-16）。",
          "tc": "APAC 網絡風險與保險峰會簡報（2026-04-16）。"
        },
        "note": {
          "sc": "2026-04-16 收录 1 条导读",
          "tc": "2026-04-16 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "金发局发表报告：巩固香港作为全球重要保险枢纽的地位。",
          "tc": "金發局發表報告：鞏固香港作為全球重要保險樞紐的地位。"
        },
        "note": {
          "sc": "2026-04-15 收录 1 条导读",
          "tc": "2026-04-15 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "中国人寿海外2026年加速数字化转型：线上理赔+智能客服。",
          "tc": "中國人壽海外2026年加速數位轉型：線上理賠+智能客服。"
        },
        "note": {
          "sc": "2026-04-10 收录 2 条导读",
          "tc": "2026-04-10 收錄 2 條導讀"
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
          "sc": "保监局于北京举办专属自保论坛（2026-04-09）。",
          "tc": "保監局於北京舉辦專屬自保論壇（2026-04-09）。"
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
        "itemCount": 3,
        "itemIds": [
          "ia-20260331-gn16-revised",
          "gn16-revised-20260331",
          "ia-20260331-cpd-reporting"
        ],
        "leadTitle": {
          "sc": "保监局修订GN16指引：2026年3月31日正式生效。",
          "tc": "保監局修訂GN16指引：2026年3月31日正式生效。"
        },
        "note": {
          "sc": "2026-03-31 收录 3 条导读",
          "tc": "2026-03-31 收錄 3 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "保监局2025年投诉统计：全年接获1173宗 同比+19.9%。",
          "tc": "保監局2025年投訴統計：全年接獲1173宗 同比+19.9%。"
        },
        "note": {
          "sc": "2026-03-27 收录 2 条导读",
          "tc": "2026-03-27 收錄 2 條導讀"
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
          "sc": "亚太医疗与健康保险会议主题演讲（2026-03-26）。",
          "tc": "亞太醫療與健康保險會議主題演講（2026-03-26）。"
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
          "sc": "2026专属自保保险座谈会开幕致辞（2026-03-25）。",
          "tc": "2026專屬自保保險座談會開幕致辭（2026-03-25）。"
        },
        "note": {
          "sc": "2026-03-25 收录 1 条导读",
          "tc": "2026-03-25 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "Chubb Life香港推出创新「Side by Side」认知障碍症保险计划。",
          "tc": "Chubb Life香港推出創新「Side by Side」認知障礙症保險計劃。"
        },
        "note": {
          "sc": "2026-03-24 收录 1 条导读",
          "tc": "2026-03-24 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "AIA 2025年全年业绩创新高：香港VONB+28% 每股股息+10%。",
          "tc": "AIA 2025年全年業績創新高：香港VONB+28% 每股股息+10%。"
        },
        "note": {
          "sc": "2026-03-19 收录 1 条导读",
          "tc": "2026-03-19 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "汇丰保险发布2026高净值财富传承规划报告。",
          "tc": "滙豐保險發布2026高淨值財富傳承規劃報告。"
        },
        "note": {
          "sc": "2026-03-17 收录 2 条导读",
          "tc": "2026-03-17 收錄 2 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "标普上调Sun Life永明香港评级至AA 展望稳定。",
          "tc": "標普上調Sun Life永明香港評級至AA 展望穩定。"
        },
        "note": {
          "sc": "2026-03-16 收录 1 条导读",
          "tc": "2026-03-16 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "香港金融监管联合推出GenAI Sandbox++：用AI监管AI风险。",
          "tc": "香港金融監管聯合推出GenAI Sandbox++：用AI監管AI風險。"
        },
        "note": {
          "sc": "2026-03-15 收录 2 条导读",
          "tc": "2026-03-15 收錄 2 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "保监局RBC制度修订咨询截止：3月10日公众意见提交结束。",
          "tc": "保監局RBC制度修訂諮詢截止：3月10日公眾意見提交結束。"
        },
        "note": {
          "sc": "2026-03-10 收录 1 条导读",
          "tc": "2026-03-10 收錄 1 條導讀"
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
          "sc": "监管机构推出 GenA.I. 沙盒++ 覆盖保险等多元金融领域（2026-03-05）。",
          "tc": "監管機構推出 GenA.I. 沙盒++ 覆蓋保險等多元金融領域（2026-03-05）。"
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
          "sc": "保监局欢迎2026-27财政预算案中与国家规划对接的措施。",
          "tc": "保監局歡迎2026-27財政預算案中與國家規劃對接的措施。"
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
          "sc": "保险人中介管理关键人员（KPIM）手册发布（2026-02-24）。",
          "tc": "保險人中介管理關鍵人員（KPIM）手冊發布（2026-02-24）。"
        },
        "note": {
          "sc": "2026-02-24 收录 1 条导读",
          "tc": "2026-02-24 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "Sun Life永明2025年APE突破118亿港元创新高。",
          "tc": "Sun Life永明2025年APE突破118億港元創新高。"
        },
        "note": {
          "sc": "2026-02-15 收录 1 条导读",
          "tc": "2026-02-15 收錄 1 條導讀"
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
          "sc": "保险创新助力低空经济发展（2026-02-13）。",
          "tc": "保險創新助力低空經濟發展（2026-02-13）。"
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
        "itemCount": 2,
        "itemIds": [
          "ia-20260211-rbc-consult-launch",
          "ia-20260211-rbc-consult"
        ],
        "leadTitle": {
          "sc": "保监局就RBC资本规则修订启动公众咨询。",
          "tc": "保監局就RBC資本規則修訂啟動公眾諮詢。"
        },
        "note": {
          "sc": "2026-02-11 收录 2 条导读",
          "tc": "2026-02-11 收錄 2 條導讀"
        }
      },
      {
        "key": "2026-02-10",
        "label": {
          "sc": "2026-02-10",
          "tc": "2026-02-10"
        },
        "itemCount": 3,
        "itemIds": [
          "fstb-20260210-fo-3384",
          "hk-2026-newcies-3000",
          "dlapiper-202602-gl16"
        ],
        "leadTitle": {
          "sc": "香港家族办公室达3384间 两年增25% 过半财富超5100万美元。",
          "tc": "香港家族辦公室達3384間 兩年增25% 過半財富超5100萬美元。"
        },
        "note": {
          "sc": "2026-02-10 收录 3 条导读",
          "tc": "2026-02-10 收錄 3 條導讀"
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
          "sc": "修订 GL16 与 GL34：长期承保与分红基金管理（2026-02-06）。",
          "tc": "修訂 GL16 與 GL34：長期承保與分紅基金管理（2026-02-06）。"
        },
        "note": {
          "sc": "2026-02-06 收录 1 条导读",
          "tc": "2026-02-06 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "金融监管总局回复跨境保险通提案：与现行《保险法》冲突。",
          "tc": "金融監管總局回覆跨境保險通提案：與現行《保險法》衝突。"
        },
        "note": {
          "sc": "2026-02-01 收录 1 条导读",
          "tc": "2026-02-01 收錄 1 條導讀"
        }
      },
      {
        "key": "2026-01-26",
        "label": {
          "sc": "2026-01-26",
          "tc": "2026-01-26"
        },
        "itemCount": 2,
        "itemIds": [
          "axa-20260126-redomicile",
          "ia-20260126-aff"
        ],
        "leadTitle": {
          "sc": "AXA安盛成功由百慕达迁册至香港。",
          "tc": "AXA安盛成功由百慕達遷冊至香港。"
        },
        "note": {
          "sc": "2026-01-26 收录 2 条导读",
          "tc": "2026-01-26 收錄 2 條導讀"
        }
      },
      {
        "key": "2026-01-23",
        "label": {
          "sc": "2026-01-23",
          "tc": "2026-01-23"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-20260123-q3stats",
          "ia-20260123-stats-3q2025"
        ],
        "leadTitle": {
          "sc": "保监局公布2025年前三季临时统计：新造保费2644亿港元同比+55.9%。",
          "tc": "保監局公布2025年前三季臨時統計：新造保費2644億港元同比+55.9%。"
        },
        "note": {
          "sc": "2026-01-23 收录 2 条导读",
          "tc": "2026-01-23 收錄 2 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "Evident报告：68%保险AI部署已转向生成式/代理式AI。",
          "tc": "Evident報告：68%保險AI部署已轉向生成式/代理式AI。"
        },
        "note": {
          "sc": "2026-01-15 收录 2 条导读",
          "tc": "2026-01-15 收錄 2 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "香港一般保险市场分析：2025年9亿→2029年09亿 CAGR 5.1%。",
          "tc": "香港一般保險市場分析：2025年9億→2029年09億 CAGR 5.1%。"
        },
        "note": {
          "sc": "2026-01-10 收录 1 条导读",
          "tc": "2026-01-10 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "宏利推出「宏挚家传承」及「财挚宏耀」两款分红寿险储蓄计划。",
          "tc": "宏利推出「宏摯家傳承」及「財摯宏耀」兩款分紅壽險儲蓄計劃。"
        },
        "note": {
          "sc": "2026-01-05 收录 1 条导读",
          "tc": "2026-01-05 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "知乎盘点2025香港保险十大事件：演示上限/佣金分摊/IUL/跨境打擊。",
          "tc": "知乎盤點2025香港保險十大事件：演示上限/佣金分攤/IUL/跨境打擊。"
        },
        "note": {
          "sc": "2025-12-30 收录 1 条导读",
          "tc": "2025-12-30 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "摩根大通2026展望：看好全球权益+双位数增长 黄金目标价$5000。",
          "tc": "摩根大通2026展望：看好全球權益+雙位數增長 黃金目標價$5000。"
        },
        "note": {
          "sc": "2025-12-10 收录 1 条导读",
          "tc": "2025-12-10 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "保监局发布2024年香港保险业年报：毛保费6352亿 全球渗透率第一。",
          "tc": "保監局發布2024年香港保險業年報：毛保費6352億 全球滲透率第一。"
        },
        "note": {
          "sc": "2025-12-05 收录 1 条导读",
          "tc": "2025-12-05 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "AIA推出全新「爱伴航」危疾保障系列产品。",
          "tc": "AIA推出全新「愛伴航」危疾保障系列產品。"
        },
        "note": {
          "sc": "2025-11-21 收录 1 条导读",
          "tc": "2025-11-21 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "高盛2026宏观展望：全球GDP 2.8% 牛市扩散 科技主导。",
          "tc": "高盛2026宏觀展望：全球GDP 2.8% 牛市擴散 科技主導。"
        },
        "note": {
          "sc": "2025-11-20 收录 2 条导读",
          "tc": "2025-11-20 收錄 2 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "证监会探讨保险产品纳入跨境理财通南向通。",
          "tc": "證監會探討保險產品納入跨境理財通南向通。"
        },
        "note": {
          "sc": "2025-11-13 收录 1 条导读",
          "tc": "2025-11-13 收錄 1 條導讀"
        }
      },
      {
        "key": "2025-10-24",
        "label": {
          "sc": "2025-10-24",
          "tc": "2025-10-24"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-20251024-h1stats",
          "ia-20251024-1h2025-stats"
        ],
        "leadTitle": {
          "sc": "保监局公布2025年上半年临时统计：毛保费4234亿，新造保费1737亿。",
          "tc": "保監局公布2025年上半年臨時統計：毛保費4234億，新造保費1737億。"
        },
        "note": {
          "sc": "2025-10-24 收录 2 条导读",
          "tc": "2025-10-24 收錄 2 條導讀"
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
          "sc": "负责人（RO）强制 CPD：2025/26 评估期首轮安排（2025-10-14 通函）。",
          "tc": "負責人（RO）強制 CPD：2025/26 評估期首輪安排（2025-10-14 通函）。"
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
        "itemCount": 2,
        "itemIds": [
          "ia-202508-iul-sandbox",
          "ia-20250919-product-naming"
        ],
        "leadTitle": {
          "sc": "保监局批准IUL产品沙盒申请：视频会议销售纳入监管框架。",
          "tc": "保監局批准IUL產品沙盒申請：視頻會議銷售納入監管框架。"
        },
        "note": {
          "sc": "2025-09-19 收录 2 条导读",
          "tc": "2025-09-19 收錄 2 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "保监局与金管局联合发布保险产品命名要求通函。",
          "tc": "保監局與金管局聯合發布保險產品命名要求通函。"
        },
        "note": {
          "sc": "2025-09-17 收录 1 条导读",
          "tc": "2025-09-17 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "宏利医疗网络扩展至内地38000+间医院。",
          "tc": "宏利醫療網絡擴展至內地38000+間醫院。"
        },
        "note": {
          "sc": "2025-09-02 收录 1 条导读",
          "tc": "2025-09-02 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "保监局就转介费监管期望发出通函：50%基准 10月1日起遵从。",
          "tc": "保監局就轉介費監管期望發出通函：50%基準 10月1日起遵從。"
        },
        "note": {
          "sc": "2025-09-01 收录 2 条导读",
          "tc": "2025-09-01 收錄 2 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "保监局2024-25年报：监管157家保司+11.8万中介 罚款2300万。",
          "tc": "保監局2024-25年報：監管157家保司+11.8萬中介 罰款2300萬。"
        },
        "note": {
          "sc": "2025-08-22 收录 1 条导读",
          "tc": "2025-08-22 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "DLA Piper解读：保监局佣金分摊实务说明——2026年1月1日起实施。",
          "tc": "DLA Piper解讀：保監局佣金分攤實務說明——2026年1月1日起實施。"
        },
        "note": {
          "sc": "2025-08-15 收录 1 条导读",
          "tc": "2025-08-15 收錄 1 條導讀"
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
          "sc": "分红保单佣金分摊：2026-01-01 起首年不超过总额70%，其余至少分5年。",
          "tc": "分紅保單佣金分攤：2026-01-01 起首年不超過總額70%，其餘至少分5年。"
        },
        "note": {
          "sc": "2025-08-08 收录 2 条导读",
          "tc": "2025-08-08 收錄 2 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "保监局发布分红保单佣金分摊指引：2026年1月1日起实施。",
          "tc": "保監局發布分紅保單佣金分攤指引：2026年1月1日起實施。"
        },
        "note": {
          "sc": "2025-07-15 收录 1 条导读",
          "tc": "2025-07-15 收錄 1 條導讀"
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
          "sc": "经纪公司负责人强制RO-CPD自2025-08-01生效（2025-07-11）。",
          "tc": "經紀公司負責人強制RO-CPD自2025-08-01生效（2025-07-11）。"
        },
        "note": {
          "sc": "2025-07-11 收录 1 条导读",
          "tc": "2025-07-11 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "AIA推出「环宇盈活储蓄保险计划」",
          "tc": "AIA推出「環宇盈活儲蓄保險計劃」"
        },
        "note": {
          "sc": "2025-07-08 收录 1 条导读",
          "tc": "2025-07-08 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "分红保单演示利率上限正式生效：非港元6.5%/港元6.0%。",
          "tc": "分紅保單演示利率上限正式生效：非港元6.5%/港元6.0%。"
        },
        "note": {
          "sc": "2025-07-01 收录 1 条导读",
          "tc": "2025-07-01 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "Sun Life永明推出升级版储蓄保险计划系列（永越多元货币II）。",
          "tc": "Sun Life永明推出升級版儲蓄保險計劃系列（永越多元貨幣II）。"
        },
        "note": {
          "sc": "2025-06-15 收录 2 条导读",
          "tc": "2025-06-15 收錄 2 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "香港保险密度0043全球第二 渗透率18.2%全球第一。",
          "tc": "香港保險密度0043全球第二 滲透率18.2%全球第一。"
        },
        "note": {
          "sc": "2025-06-01 收录 1 条导读",
          "tc": "2025-06-01 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "宏利推出两款全新危疾计划：宏健守护+宏伴护航危疾入息保障。",
          "tc": "宏利推出兩款全新危疾計劃：宏健守護+宏伴護航危疾入息保障。"
        },
        "note": {
          "sc": "2025-04-28 收录 1 条导读",
          "tc": "2025-04-28 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "保监局指定AIA及保诚亚洲为具系统重要性保险机构(D-SII)。",
          "tc": "保監局指定AIA及保誠亞洲為具系統重要性保險機構(D-SII)。"
        },
        "note": {
          "sc": "2025-04-15 收录 1 条导读",
          "tc": "2025-04-15 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "AXA安盛全面升级大湾区跨境医疗专属服务网络。",
          "tc": "AXA安盛全面升級大灣區跨境醫療專屬服務網絡。"
        },
        "note": {
          "sc": "2025-04-09 收录 1 条导读",
          "tc": "2025-04-09 收錄 1 條導讀"
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
          "sc": "保监局文章：引入演示利率上限，提升投保人保障（2025-03-30）。",
          "tc": "保監局文章：引入演示利率上限，提升投保人保障（2025-03-30）。"
        },
        "note": {
          "sc": "2025-03-30 收录 1 条导读",
          "tc": "2025-03-30 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "金发局报告：巩固香港全球保险枢纽 2024年经济增加值1084亿。",
          "tc": "金發局報告：鞏固香港全球保險樞紐 2024年經濟增加值1084億。"
        },
        "note": {
          "sc": "2025-03-27 收录 1 条导读",
          "tc": "2025-03-27 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "保监局2025年InsurTech蓝图：AI对保险业价值9.5-15.4万亿美元。",
          "tc": "保監局2025年InsurTech藍圖：AI對保險業價值9.5-15.4萬億美元。"
        },
        "note": {
          "sc": "2025-03-26 收录 1 条导读",
          "tc": "2025-03-26 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "AIA 2024年全年业绩：香港VONB+23% 内地客+22% 创纪录。",
          "tc": "AIA 2024年全年業績：香港VONB+23% 內地客+22% 創紀錄。"
        },
        "note": {
          "sc": "2025-03-14 收录 1 条导读",
          "tc": "2025-03-14 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "保监局与金管局联合发布IUL产品监管通函。",
          "tc": "保監局與金管局聯合發布IUL產品監管通函。"
        },
        "note": {
          "sc": "2025-03-13 收录 2 条导读",
          "tc": "2025-03-13 收錄 2 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "金融监管总局放宽港澳金融机构入股保险公司门槛。",
          "tc": "金融監管總局放寬港澳金融機構入股保險公司門檻。"
        },
        "note": {
          "sc": "2025-02-28 收录 3 条导读",
          "tc": "2025-02-28 收錄 3 條導讀"
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
          "sc": "理赔管理发现与建议（2025-02-06）。",
          "tc": "理賠管理發現與建議（2025-02-06）。"
        },
        "note": {
          "sc": "2025-02-06 收录 1 条导读",
          "tc": "2025-02-06 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "业界回顾2024香港保险关键趋势：RBC生效/GN16修订/跨境复苏。",
          "tc": "業界回顧2024香港保險關鍵趨勢：RBC生效/GN16修訂/跨境復甦。"
        },
        "note": {
          "sc": "2025-01-15 收录 1 条导读",
          "tc": "2025-01-15 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "AXA安盛推出全新「盛利储蓄计划」",
          "tc": "AXA安盛推出全新「盛利儲蓄計劃」"
        },
        "note": {
          "sc": "2025-01-10 收录 1 条导读",
          "tc": "2025-01-10 收錄 1 條導讀"
        }
      },
      {
        "key": "2024-09-23",
        "label": {
          "sc": "2024-09-23",
          "tc": "2024-09-23"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20240923-refcheck"
        ],
        "leadTitle": {
          "sc": "保监局参考查核计划生效：中介人背景审查启动。",
          "tc": "保監局參考查核計劃生效：中介人背景審查啟動。"
        },
        "note": {
          "sc": "2024-09-23 收录 1 条导读",
          "tc": "2024-09-23 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "2024上半年香港保险毛保费3109亿同比+5.1% 内地访客297亿。",
          "tc": "2024上半年香港保險毛保費3109億同比+5.1% 內地訪客297億。"
        },
        "note": {
          "sc": "2024-09-15 收录 1 条导读",
          "tc": "2024-09-15 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "Sun Life永明收购FWD香港养老金业务 强积金+46亿港元。",
          "tc": "Sun Life永明收購FWD香港養老金業務 強積金+46億港元。"
        },
        "note": {
          "sc": "2024-09-10 收录 1 条导读",
          "tc": "2024-09-10 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "保监局与廉政公署联合打击跨境无牌销售保单。",
          "tc": "保監局與廉政公署聯合打擊跨境無牌銷售保單。"
        },
        "note": {
          "sc": "2024-08-20 收录 1 条导读",
          "tc": "2024-08-20 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "金融监管总局：现阶段跨境保险通试点时机尚不成熟。",
          "tc": "金融監管總局：現階段跨境保險通試點時機尚不成熟。"
        },
        "note": {
          "sc": "2024-08-01 收录 1 条导读",
          "tc": "2024-08-01 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "FTLife正式更名为周大福人寿(CTF Life)。",
          "tc": "FTLife正式更名為周大福人壽(CTF Life)。"
        },
        "note": {
          "sc": "2024-07-23 收录 1 条导读",
          "tc": "2024-07-23 收錄 1 條導讀"
        }
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
        ],
        "leadTitle": {
          "sc": "香港风险为本资本制度(RBC)正式生效。",
          "tc": "香港風險為本資本制度(RBC)正式生效。"
        },
        "note": {
          "sc": "2024-07-01 收录 1 条导读",
          "tc": "2024-07-01 收錄 1 條導讀"
        }
      }
    ],
    "weekly": [
      {
        "key": "2026-W31",
        "label": {
          "sc": "2026-W31",
          "tc": "2026-W31"
        },
        "itemCount": 1,
        "itemIds": [
          "ratings-2026-consolidated"
        ],
        "leadTitle": {
          "sc": "香港主要保险公司信评一览(2026更新)。",
          "tc": "香港主要保險公司信評一覽(2026更新)。"
        },
        "note": {
          "sc": "2026-W31 共 1 条",
          "tc": "2026-W31 共 1 條"
        }
      },
      {
        "key": "2026-W30",
        "label": {
          "sc": "2026-W30",
          "tc": "2026-W30"
        },
        "itemCount": 5,
        "itemIds": [
          "insbus-202607-hk-growth",
          "aif-2026-save-the-date",
          "ia-public-disclosure-2026",
          "ia-q1-2026-stats",
          "hkma-complaints-20260724"
        ],
        "leadTitle": {
          "sc": "Insurance Business深度分析：Q1毛保费2916亿+32% 跨境数据连5季缺失。",
          "tc": "Insurance Business深度分析：Q1毛保費2916億+32% 跨境數據連5季缺失。"
        },
        "note": {
          "sc": "2026-W30 共 5 条",
          "tc": "2026-W30 共 5 條"
        }
      },
      {
        "key": "2026-W29",
        "label": {
          "sc": "2026-W29",
          "tc": "2026-W29"
        },
        "itemCount": 5,
        "itemIds": [
          "creditsights-2026-2h",
          "aia-20260716-hyrox",
          "ia-20260716-ashk-ifoa",
          "ia-20260715-sales-practices",
          "ia-licence-20260630"
        ],
        "leadTitle": {
          "sc": "CreditSights展望：2026下半年中港跨境资金规则或进一步收紧。",
          "tc": "CreditSights展望：2026下半年中港跨境資金規則或進一步收緊。"
        },
        "note": {
          "sc": "2026-W29 共 5 条",
          "tc": "2026-W29 共 5 條"
        }
      },
      {
        "key": "2026-W28",
        "label": {
          "sc": "2026-W28",
          "tc": "2026-W28"
        },
        "itemCount": 7,
        "itemIds": [
          "swissre-202607-wis",
          "ia-20260712-speech",
          "ia-20260712-speech",
          "ia-20260710-illustration",
          "ia-20260710-illustration-review",
          "fstb-20260708-captive",
          "ia-20260708-captive"
        ],
        "leadTitle": {
          "sc": "Swiss Re sigma报告：2026全球保险成为碎片化世界中的减震器。",
          "tc": "Swiss Re sigma報告：2026全球保險成為碎片化世界中的減震器。"
        },
        "note": {
          "sc": "2026-W28 共 7 条",
          "tc": "2026-W28 共 7 條"
        }
      },
      {
        "key": "2026-W27",
        "label": {
          "sc": "2026-W27",
          "tc": "2026-W27"
        },
        "itemCount": 7,
        "itemIds": [
          "rga-2026-hk-market",
          "ia-20260703-rfyc",
          "ia-crossref-20260701",
          "ia-20260630-swissre-sigma",
          "ia-20260630-allianz-report",
          "ia-20260629-sunlife-notes",
          "ia-20260629-hkma-bulletin"
        ],
        "leadTitle": {
          "sc": "RGA分析：2026年香港保险市场机遇与挑战——跨境需求+监管转型+AI。",
          "tc": "RGA分析：2026年香港保險市場機遇與挑戰——跨境需求+監管轉型+AI。"
        },
        "note": {
          "sc": "2026-W27 共 7 条",
          "tc": "2026-W27 共 7 條"
        }
      },
      {
        "key": "2026-W26",
        "label": {
          "sc": "2026-W26",
          "tc": "2026-W26"
        },
        "itemCount": 8,
        "itemIds": [
          "empf-2026-fee-reduction",
          "taiping-202606-rating",
          "manulife-20260625-board",
          "ia-20260628-fsdc-talent",
          "ia-20260626-morganstanley",
          "ia-20260626-pimco-asia",
          "ia-20260625-manulife-convention",
          "ia-20260624-rga-trends"
        ],
        "leadTitle": {
          "sc": "积金易平台降费：236只基金行政费降至0.37% 惠及千万账户。",
          "tc": "積金易平台降費：236隻基金行政費降至0.37% 惠及千萬賬戶。"
        },
        "note": {
          "sc": "2026-W26 共 8 条",
          "tc": "2026-W26 共 8 條"
        }
      },
      {
        "key": "2026-W25",
        "label": {
          "sc": "2026-W25",
          "tc": "2026-W25"
        },
        "itemCount": 10,
        "itemIds": [
          "fwd-2026-brand-victoria",
          "axa-2026-bloomberg-awards",
          "ia-ai-cohort-202606",
          "ia-20260620-goldman-outlook",
          "ia-20260618-blackrock-outlook",
          "ia-20260617-manulife-ai",
          "ia-20260616-aia-prudential-roles",
          "ia-20260616-cheung-enforcement",
          "ia-ai-seminar-20260615",
          "ia-20260615-bloomberg-crackdown"
        ],
        "leadTitle": {
          "sc": "富卫香港2026品牌升级：维港双岸招牌同时亮灯。",
          "tc": "富衛香港2026品牌升級：維港雙岸招牌同時亮燈。"
        },
        "note": {
          "sc": "2026-W25 共 10 条",
          "tc": "2026-W25 共 10 條"
        }
      },
      {
        "key": "2026-W24",
        "label": {
          "sc": "2026-W24",
          "tc": "2026-W24"
        },
        "itemCount": 9,
        "itemIds": [
          "hk-20260612-fo-tax",
          "aia-20260608-prosperlife",
          "ctflife-2026-diamond-iul",
          "ia-20260612-manulife-plans",
          "ia-20260610-manulife-leverage",
          "ia-20260610-chowtaifook-life",
          "ia-20260609-fitch-apac",
          "ia-20260608-axa-global-private",
          "ia-20260608-aia-wealth-flexi"
        ],
        "leadTitle": {
          "sc": "港府2026年优化家族办公室税制：扩大免税范围至数字资产。",
          "tc": "港府2026年優化家族辦公室稅制：擴大免稅範圍至數字資產。"
        },
        "note": {
          "sc": "2026-W24 共 9 条",
          "tc": "2026-W24 共 9 條"
        }
      },
      {
        "key": "2026-W23",
        "label": {
          "sc": "2026-W23",
          "tc": "2026-W23"
        },
        "itemCount": 8,
        "itemIds": [
          "deloitte-2026-insurance-outlook",
          "chubb-20260601-mylegacy",
          "ia-20260605-hkma-commission",
          "ia-20260605-hkma-remuneration-circ",
          "ia-hkma-remuneration-20260605",
          "ia-20260611-chubb-life",
          "ia-20260603-broker-referral",
          "ia-20260602-hkma-crossborder"
        ],
        "leadTitle": {
          "sc": "德勤2026全球保险展望：AI落地加速 香港保监局推AI促进计划。",
          "tc": "德勤2026全球保險展望：AI落地加速 香港保監局推AI促進計劃。"
        },
        "note": {
          "sc": "2026-W23 共 8 条",
          "tc": "2026-W23 共 8 條"
        }
      },
      {
        "key": "2026-W22",
        "label": {
          "sc": "2026-W22",
          "tc": "2026-W22"
        },
        "itemCount": 2,
        "itemIds": [
          "allianz-20260528-global-report",
          "ia-20260529-onsite-findings"
        ],
        "leadTitle": {
          "sc": "安联全球保险报告2026：全球保费+7.1%至6.9万亿欧元 亚洲领跑。",
          "tc": "安聯全球保險報告2026：全球保費+7.1%至6.9萬億歐元 亞洲領跑。"
        },
        "note": {
          "sc": "2026-W22 共 2 条",
          "tc": "2026-W22 共 2 條"
        }
      },
      {
        "key": "2026-W21",
        "label": {
          "sc": "2026-W21",
          "tc": "2026-W21"
        },
        "itemCount": 3,
        "itemIds": [
          "fwd-2026-q1-update",
          "ia-20260519-disclosure-consult",
          "ia-20260520-gl34-corp"
        ],
        "leadTitle": {
          "sc": "富卫集团2026年Q1新业务强劲：年化新保费+4%至7.2亿美元。",
          "tc": "富衛集團2026年Q1新業務強勁：年化新保費+4%至7.2億美元。"
        },
        "note": {
          "sc": "2026-W21 共 3 条",
          "tc": "2026-W21 共 3 條"
        }
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
        ],
        "leadTitle": {
          "sc": "Sun Life永明连续4年获10Life 5星保险大奖。",
          "tc": "Sun Life永明連續4年獲10Life 5星保險大獎。"
        },
        "note": {
          "sc": "2026-W20 共 3 条",
          "tc": "2026-W20 共 3 條"
        }
      },
      {
        "key": "2026-W19",
        "label": {
          "sc": "2026-W19",
          "tc": "2026-W19"
        },
        "itemCount": 3,
        "itemIds": [
          "cpic-20260504-gen3",
          "ia-20260508-rbc-conclusion",
          "ia-20260508-rbc-conclusions"
        ],
        "leadTitle": {
          "sc": "太保寿险香港推出「世代悦享3」储蓄保险计划——35周年献礼。",
          "tc": "太保壽險香港推出「世代悅享3」儲蓄保險計劃——35周年獻禮。"
        },
        "note": {
          "sc": "2026-W19 共 3 条",
          "tc": "2026-W19 共 3 條"
        }
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
        ],
        "leadTitle": {
          "sc": "AIA 2026年Q1新业务价值增长13% 香港表现强劲。",
          "tc": "AIA 2026年Q1新業務價值增長13% 香港表現強勁。"
        },
        "note": {
          "sc": "2026-W18 共 3 条",
          "tc": "2026-W18 共 3 條"
        }
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
          "manulife-20260420-annuity-accident",
          "ctflife-20260422-artisan-leap",
          "aia-20260424-top-insurer",
          "ia-20260424-stats-2025",
          "ia-20260422-ils"
        ],
        "leadTitle": {
          "sc": "保监局公布2025全年业绩：个人新单保费3309亿港元 +50.6%再创新高。",
          "tc": "保監局公布2025全年業績：個人新單保費3309億港元 +50.6%再創新高。"
        },
        "note": {
          "sc": "2026-W17 共 6 条",
          "tc": "2026-W17 共 6 條"
        }
      },
      {
        "key": "2026-W16",
        "label": {
          "sc": "2026-W16",
          "tc": "2026-W16"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-202604-fsi-survey",
          "ia-20260416-cyber"
        ],
        "leadTitle": {
          "sc": "金发局发表报告：巩固香港作为全球重要保险枢纽的地位。",
          "tc": "金發局發表報告：鞏固香港作為全球重要保險樞紐的地位。"
        },
        "note": {
          "sc": "2026-W16 共 2 条",
          "tc": "2026-W16 共 2 條"
        }
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
        ],
        "leadTitle": {
          "sc": "中国人寿海外2026年加速数字化转型：线上理赔+智能客服。",
          "tc": "中國人壽海外2026年加速數位轉型：線上理賠+智能客服。"
        },
        "note": {
          "sc": "2026-W15 共 3 条",
          "tc": "2026-W15 共 3 條"
        }
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
        ],
        "leadTitle": {
          "sc": "保监局修订GN16指引：2026年3月31日正式生效。",
          "tc": "保監局修訂GN16指引：2026年3月31日正式生效。"
        },
        "note": {
          "sc": "2026-W14 共 3 条",
          "tc": "2026-W14 共 3 條"
        }
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
          "chubb-2026-dementia",
          "ia-20260327-cif12",
          "ia-20260326-health-conf",
          "ia-20260325-captive-forum-speech"
        ],
        "leadTitle": {
          "sc": "保监局2025年投诉统计：全年接获1173宗 同比+19.9%。",
          "tc": "保監局2025年投訴統計：全年接獲1173宗 同比+19.9%。"
        },
        "note": {
          "sc": "2026-W13 共 5 条",
          "tc": "2026-W13 共 5 條"
        }
      },
      {
        "key": "2026-W12",
        "label": {
          "sc": "2026-W12",
          "tc": "2026-W12"
        },
        "itemCount": 4,
        "itemIds": [
          "sunlife-202603-sp-upgrade",
          "aia-2025-annual-results",
          "hsbc-life-2026-hnw-pitchbook",
          "prudential-20260317-youth"
        ],
        "leadTitle": {
          "sc": "标普上调Sun Life永明香港评级至AA 展望稳定。",
          "tc": "標普上調Sun Life永明香港評級至AA 展望穩定。"
        },
        "note": {
          "sc": "2026-W12 共 4 条",
          "tc": "2026-W12 共 4 條"
        }
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
          "ia-20260310-rbc-consult-close",
          "manulife-202603-new-products"
        ],
        "leadTitle": {
          "sc": "香港金融监管联合推出GenAI Sandbox++：用AI监管AI风险。",
          "tc": "香港金融監管聯合推出GenAI Sandbox++：用AI監管AI風險。"
        },
        "note": {
          "sc": "2026-W11 共 3 条",
          "tc": "2026-W11 共 3 條"
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
          "sc": "监管机构推出 GenA.I. 沙盒++ 覆盖保险等多元金融领域（2026-03-05）。",
          "tc": "監管機構推出 GenA.I. 沙盒++ 覆蓋保險等多元金融領域（2026-03-05）。"
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
          "sc": "保监局欢迎2026-27财政预算案中与国家规划对接的措施。",
          "tc": "保監局歡迎2026-27財政預算案中與國家規劃對接的措施。"
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
        "itemCount": 7,
        "itemIds": [
          "fstb-20260210-fo-3384",
          "hk-2026-newcies-3000",
          "dlapiper-202602-gl16",
          "sunlife-2025-ape-118",
          "ia-20260211-rbc-consult-launch",
          "ia-20260213-low-altitude",
          "ia-20260211-rbc-consult"
        ],
        "leadTitle": {
          "sc": "香港家族办公室达3384间 两年增25% 过半财富超5100万美元。",
          "tc": "香港家族辦公室達3384間 兩年增25% 過半財富超5100萬美元。"
        },
        "note": {
          "sc": "2026-W07 共 7 条",
          "tc": "2026-W07 共 7 條"
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
          "sc": "修订 GL16 与 GL34：长期承保与分红基金管理（2026-02-06）。",
          "tc": "修訂 GL16 與 GL34：長期承保與分紅基金管理（2026-02-06）。"
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
        "itemCount": 3,
        "itemIds": [
          "axa-20260126-redomicile",
          "circ-20260201-crossborder",
          "ia-20260126-aff"
        ],
        "leadTitle": {
          "sc": "AXA安盛成功由百慕达迁册至香港。",
          "tc": "AXA安盛成功由百慕達遷冊至香港。"
        },
        "note": {
          "sc": "2026-W05 共 3 条",
          "tc": "2026-W05 共 3 條"
        }
      },
      {
        "key": "2026-W04",
        "label": {
          "sc": "2026-W04",
          "tc": "2026-W04"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-20260123-q3stats",
          "ia-20260123-stats-3q2025"
        ],
        "leadTitle": {
          "sc": "保监局公布2025年前三季临时统计：新造保费2644亿港元同比+55.9%。",
          "tc": "保監局公布2025年前三季臨時統計：新造保費2644億港元同比+55.9%。"
        },
        "note": {
          "sc": "2026-W04 共 2 条",
          "tc": "2026-W04 共 2 條"
        }
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
        ],
        "leadTitle": {
          "sc": "Evident报告：68%保险AI部署已转向生成式/代理式AI。",
          "tc": "Evident報告：68%保險AI部署已轉向生成式/代理式AI。"
        },
        "note": {
          "sc": "2026-W03 共 2 条",
          "tc": "2026-W03 共 2 條"
        }
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
        ],
        "leadTitle": {
          "sc": "香港一般保险市场分析：2025年9亿→2029年09亿 CAGR 5.1%。",
          "tc": "香港一般保險市場分析：2025年9億→2029年09億 CAGR 5.1%。"
        },
        "note": {
          "sc": "2026-W02 共 2 条",
          "tc": "2026-W02 共 2 條"
        }
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
        ],
        "leadTitle": {
          "sc": "知乎盘点2025香港保险十大事件：演示上限/佣金分摊/IUL/跨境打擊。",
          "tc": "知乎盤點2025香港保險十大事件：演示上限/佣金分攤/IUL/跨境打擊。"
        },
        "note": {
          "sc": "2026-W01 共 1 条",
          "tc": "2026-W01 共 1 條"
        }
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
        ],
        "leadTitle": {
          "sc": "摩根大通2026展望：看好全球权益+双位数增长 黄金目标价$5000。",
          "tc": "摩根大通2026展望：看好全球權益+雙位數增長 黃金目標價$5000。"
        },
        "note": {
          "sc": "2025-W50 共 1 条",
          "tc": "2025-W50 共 1 條"
        }
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
        ],
        "leadTitle": {
          "sc": "保监局发布2024年香港保险业年报：毛保费6352亿 全球渗透率第一。",
          "tc": "保監局發布2024年香港保險業年報：毛保費6352億 全球滲透率第一。"
        },
        "note": {
          "sc": "2025-W49 共 1 条",
          "tc": "2025-W49 共 1 條"
        }
      },
      {
        "key": "2025-W47",
        "label": {
          "sc": "2025-W47",
          "tc": "2025-W47"
        },
        "itemCount": 3,
        "itemIds": [
          "goldman-2026-macro-outlook",
          "aia-20251121-aisan",
          "ia-20251120-refcheck-scheme"
        ],
        "leadTitle": {
          "sc": "高盛2026宏观展望：全球GDP 2.8% 牛市扩散 科技主导。",
          "tc": "高盛2026宏觀展望：全球GDP 2.8% 牛市擴散 科技主導。"
        },
        "note": {
          "sc": "2025-W47 共 3 条",
          "tc": "2025-W47 共 3 條"
        }
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
        ],
        "leadTitle": {
          "sc": "证监会探讨保险产品纳入跨境理财通南向通。",
          "tc": "證監會探討保險產品納入跨境理財通南向通。"
        },
        "note": {
          "sc": "2025-W46 共 1 条",
          "tc": "2025-W46 共 1 條"
        }
      },
      {
        "key": "2025-W43",
        "label": {
          "sc": "2025-W43",
          "tc": "2025-W43"
        },
        "itemCount": 2,
        "itemIds": [
          "ia-20251024-h1stats",
          "ia-20251024-1h2025-stats"
        ],
        "leadTitle": {
          "sc": "保监局公布2025年上半年临时统计：毛保费4234亿，新造保费1737亿。",
          "tc": "保監局公布2025年上半年臨時統計：毛保費4234億，新造保費1737億。"
        },
        "note": {
          "sc": "2025-W43 共 2 条",
          "tc": "2025-W43 共 2 條"
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
          "sc": "负责人（RO）强制 CPD：2025/26 评估期首轮安排（2025-10-14 通函）。",
          "tc": "負責人（RO）強制 CPD：2025/26 評估期首輪安排（2025-10-14 通函）。"
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
        "itemCount": 3,
        "itemIds": [
          "ia-20250917-product-naming",
          "ia-202508-iul-sandbox",
          "ia-20250919-product-naming"
        ],
        "leadTitle": {
          "sc": "保监局与金管局联合发布保险产品命名要求通函。",
          "tc": "保監局與金管局聯合發布保險產品命名要求通函。"
        },
        "note": {
          "sc": "2025-W38 共 3 条",
          "tc": "2025-W38 共 3 條"
        }
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
        ],
        "leadTitle": {
          "sc": "宏利医疗网络扩展至内地38000+间医院。",
          "tc": "宏利醫療網絡擴展至內地38000+間醫院。"
        },
        "note": {
          "sc": "2025-W36 共 3 条",
          "tc": "2025-W36 共 3 條"
        }
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
        ],
        "leadTitle": {
          "sc": "保监局2024-25年报：监管157家保司+11.8万中介 罚款2300万。",
          "tc": "保監局2024-25年報：監管157家保司+11.8萬中介 罰款2300萬。"
        },
        "note": {
          "sc": "2025-W34 共 1 条",
          "tc": "2025-W34 共 1 條"
        }
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
        ],
        "leadTitle": {
          "sc": "DLA Piper解读：保监局佣金分摊实务说明——2026年1月1日起实施。",
          "tc": "DLA Piper解讀：保監局佣金分攤實務說明——2026年1月1日起實施。"
        },
        "note": {
          "sc": "2025-W33 共 1 条",
          "tc": "2025-W33 共 1 條"
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
          "sc": "分红保单佣金分摊：2026-01-01 起首年不超过总额70%，其余至少分5年。",
          "tc": "分紅保單佣金分攤：2026-01-01 起首年不超過總額70%，其餘至少分5年。"
        },
        "note": {
          "sc": "2025-W32 共 2 条",
          "tc": "2025-W32 共 2 條"
        }
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
        ],
        "leadTitle": {
          "sc": "保监局发布分红保单佣金分摊指引：2026年1月1日起实施。",
          "tc": "保監局發布分紅保單佣金分攤指引：2026年1月1日起實施。"
        },
        "note": {
          "sc": "2025-W29 共 1 条",
          "tc": "2025-W29 共 1 條"
        }
      },
      {
        "key": "2025-W28",
        "label": {
          "sc": "2025-W28",
          "tc": "2025-W28"
        },
        "itemCount": 2,
        "itemIds": [
          "aia-20250708-global-prosper",
          "ia-20250711-ro-cpd-compulsory"
        ],
        "leadTitle": {
          "sc": "AIA推出「环宇盈活储蓄保险计划」",
          "tc": "AIA推出「環宇盈活儲蓄保險計劃」"
        },
        "note": {
          "sc": "2025-W28 共 2 条",
          "tc": "2025-W28 共 2 條"
        }
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
        ],
        "leadTitle": {
          "sc": "分红保单演示利率上限正式生效：非港元6.5%/港元6.0%。",
          "tc": "分紅保單演示利率上限正式生效：非港元6.5%/港元6.0%。"
        },
        "note": {
          "sc": "2025-W27 共 1 条",
          "tc": "2025-W27 共 1 條"
        }
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
        ],
        "leadTitle": {
          "sc": "Sun Life永明推出升级版储蓄保险计划系列（永越多元货币II）。",
          "tc": "Sun Life永明推出升級版儲蓄保險計劃系列（永越多元貨幣II）。"
        },
        "note": {
          "sc": "2025-W24 共 2 条",
          "tc": "2025-W24 共 2 條"
        }
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
        ],
        "leadTitle": {
          "sc": "香港保险密度0043全球第二 渗透率18.2%全球第一。",
          "tc": "香港保險密度0043全球第二 滲透率18.2%全球第一。"
        },
        "note": {
          "sc": "2025-W22 共 1 条",
          "tc": "2025-W22 共 1 條"
        }
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
        ],
        "leadTitle": {
          "sc": "宏利推出两款全新危疾计划：宏健守护+宏伴护航危疾入息保障。",
          "tc": "宏利推出兩款全新危疾計劃：宏健守護+宏伴護航危疾入息保障。"
        },
        "note": {
          "sc": "2025-W18 共 1 条",
          "tc": "2025-W18 共 1 條"
        }
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
        ],
        "leadTitle": {
          "sc": "保监局指定AIA及保诚亚洲为具系统重要性保险机构(D-SII)。",
          "tc": "保監局指定AIA及保誠亞洲為具系統重要性保險機構(D-SII)。"
        },
        "note": {
          "sc": "2025-W16 共 1 条",
          "tc": "2025-W16 共 1 條"
        }
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
        ],
        "leadTitle": {
          "sc": "AXA安盛全面升级大湾区跨境医疗专属服务网络。",
          "tc": "AXA安盛全面升級大灣區跨境醫療專屬服務網絡。"
        },
        "note": {
          "sc": "2025-W15 共 1 条",
          "tc": "2025-W15 共 1 條"
        }
      },
      {
        "key": "2025-W13",
        "label": {
          "sc": "2025-W13",
          "tc": "2025-W13"
        },
        "itemCount": 3,
        "itemIds": [
          "ia-2025-insurtech-initiatives",
          "fsdc-2025-insurance-hub",
          "ia-20250330-illustration-article"
        ],
        "leadTitle": {
          "sc": "保监局2025年InsurTech蓝图：AI对保险业价值9.5-15.4万亿美元。",
          "tc": "保監局2025年InsurTech藍圖：AI對保險業價值9.5-15.4萬億美元。"
        },
        "note": {
          "sc": "2025-W13 共 3 条",
          "tc": "2025-W13 共 3 條"
        }
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
        ],
        "leadTitle": {
          "sc": "AIA 2024年全年业绩：香港VONB+23% 内地客+22% 创纪录。",
          "tc": "AIA 2024年全年業績：香港VONB+23% 內地客+22% 創紀錄。"
        },
        "note": {
          "sc": "2025-W11 共 3 条",
          "tc": "2025-W11 共 3 條"
        }
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
        ],
        "leadTitle": {
          "sc": "金融监管总局放宽港澳金融机构入股保险公司门槛。",
          "tc": "金融監管總局放寬港澳金融機構入股保險公司門檻。"
        },
        "note": {
          "sc": "2025-W09 共 3 条",
          "tc": "2025-W09 共 3 條"
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
          "sc": "理赔管理发现与建议（2025-02-06）。",
          "tc": "理賠管理發現與建議（2025-02-06）。"
        },
        "note": {
          "sc": "2025-W06 共 1 条",
          "tc": "2025-W06 共 1 條"
        }
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
        ],
        "leadTitle": {
          "sc": "业界回顾2024香港保险关键趋势：RBC生效/GN16修订/跨境复苏。",
          "tc": "業界回顧2024香港保險關鍵趨勢：RBC生效/GN16修訂/跨境復甦。"
        },
        "note": {
          "sc": "2025-W03 共 1 条",
          "tc": "2025-W03 共 1 條"
        }
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
        ],
        "leadTitle": {
          "sc": "AXA安盛推出全新「盛利储蓄计划」",
          "tc": "AXA安盛推出全新「盛利儲蓄計劃」"
        },
        "note": {
          "sc": "2025-W02 共 1 条",
          "tc": "2025-W02 共 1 條"
        }
      },
      {
        "key": "2024-W39",
        "label": {
          "sc": "2024-W39",
          "tc": "2024-W39"
        },
        "itemCount": 1,
        "itemIds": [
          "ia-20240923-refcheck"
        ],
        "leadTitle": {
          "sc": "保监局参考查核计划生效：中介人背景审查启动。",
          "tc": "保監局參考查核計劃生效：中介人背景審查啟動。"
        },
        "note": {
          "sc": "2024-W39 共 1 条",
          "tc": "2024-W39 共 1 條"
        }
      },
      {
        "key": "2024-W37",
        "label": {
          "sc": "2024-W37",
          "tc": "2024-W37"
        },
        "itemCount": 2,
        "itemIds": [
          "sunlife-2024-fwd-pension",
          "ia-2024h1-stats"
        ],
        "leadTitle": {
          "sc": "Sun Life永明收购FWD香港养老金业务 强积金+46亿港元。",
          "tc": "Sun Life永明收購FWD香港養老金業務 強積金+46億港元。"
        },
        "note": {
          "sc": "2024-W37 共 2 条",
          "tc": "2024-W37 共 2 條"
        }
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
        ],
        "leadTitle": {
          "sc": "保监局与廉政公署联合打击跨境无牌销售保单。",
          "tc": "保監局與廉政公署聯合打擊跨境無牌銷售保單。"
        },
        "note": {
          "sc": "2024-W34 共 1 条",
          "tc": "2024-W34 共 1 條"
        }
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
        ],
        "leadTitle": {
          "sc": "金融监管总局：现阶段跨境保险通试点时机尚不成熟。",
          "tc": "金融監管總局：現階段跨境保險通試點時機尚不成熟。"
        },
        "note": {
          "sc": "2024-W31 共 1 条",
          "tc": "2024-W31 共 1 條"
        }
      },
      {
        "key": "2024-W30",
        "label": {
          "sc": "2024-W30",
          "tc": "2024-W30"
        },
        "itemCount": 1,
        "itemIds": [
          "ctflife-20240723-rebrand"
        ],
        "leadTitle": {
          "sc": "FTLife正式更名为周大福人寿(CTF Life)。",
          "tc": "FTLife正式更名為周大福人壽(CTF Life)。"
        },
        "note": {
          "sc": "2024-W30 共 1 条",
          "tc": "2024-W30 共 1 條"
        }
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
        ],
        "leadTitle": {
          "sc": "香港风险为本资本制度(RBC)正式生效。",
          "tc": "香港風險為本資本制度(RBC)正式生效。"
        },
        "note": {
          "sc": "2024-W27 共 1 条",
          "tc": "2024-W27 共 1 條"
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
        "itemCount": 21,
        "itemIds": [
          "ratings-2026-consolidated",
          "insbus-202607-hk-growth",
          "creditsights-2026-2h",
          "swissre-202607-wis",
          "rga-2026-hk-market",
          "aia-20260716-hyrox",
          "aif-2026-save-the-date",
          "ia-public-disclosure-2026",
          "ia-q1-2026-stats",
          "hkma-complaints-20260724",
          "ia-20260716-ashk-ifoa",
          "ia-20260715-sales-practices",
          "ia-licence-20260630",
          "ia-20260712-speech",
          "ia-20260712-speech",
          "ia-20260710-illustration",
          "ia-20260710-illustration-review",
          "fstb-20260708-captive",
          "ia-20260708-captive",
          "ia-20260703-rfyc",
          "ia-crossref-20260701"
        ],
        "leadTitle": {
          "sc": "香港主要保险公司信评一览(2026更新)。",
          "tc": "香港主要保險公司信評一覽(2026更新)。"
        },
        "note": {
          "sc": "2026-07 共 21 条",
          "tc": "2026-07 共 21 條"
        }
      },
      {
        "key": "2026-06",
        "label": {
          "sc": "2026-06",
          "tc": "2026-06"
        },
        "itemCount": 39,
        "itemIds": [
          "hk-20260612-fo-tax",
          "empf-2026-fee-reduction",
          "deloitte-2026-insurance-outlook",
          "chubb-20260601-mylegacy",
          "taiping-202606-rating",
          "fwd-2026-brand-victoria",
          "aia-20260608-prosperlife",
          "manulife-20260625-board",
          "axa-2026-bloomberg-awards",
          "ctflife-2026-diamond-iul",
          "ia-20260605-hkma-commission",
          "ia-ai-cohort-202606",
          "ia-20260630-swissre-sigma",
          "ia-20260630-allianz-report",
          "ia-20260629-sunlife-notes",
          "ia-20260629-hkma-bulletin",
          "ia-20260628-fsdc-talent",
          "ia-20260626-morganstanley",
          "ia-20260626-pimco-asia",
          "ia-20260625-manulife-convention",
          "ia-20260624-rga-trends",
          "ia-20260620-goldman-outlook",
          "ia-20260618-blackrock-outlook",
          "ia-20260617-manulife-ai",
          "ia-20260616-aia-prudential-roles",
          "ia-20260616-cheung-enforcement",
          "ia-ai-seminar-20260615",
          "ia-20260615-bloomberg-crackdown",
          "ia-20260612-manulife-plans",
          "ia-20260610-manulife-leverage",
          "ia-20260610-chowtaifook-life",
          "ia-20260609-fitch-apac",
          "ia-20260608-axa-global-private",
          "ia-20260608-aia-wealth-flexi",
          "ia-20260605-hkma-remuneration-circ",
          "ia-hkma-remuneration-20260605",
          "ia-20260611-chubb-life",
          "ia-20260603-broker-referral",
          "ia-20260602-hkma-crossborder"
        ],
        "leadTitle": {
          "sc": "港府2026年优化家族办公室税制：扩大免税范围至数字资产。",
          "tc": "港府2026年優化家族辦公室稅制：擴大免稅範圍至數字資產。"
        },
        "note": {
          "sc": "2026-06 共 39 条",
          "tc": "2026-06 共 39 條"
        }
      },
      {
        "key": "2026-05",
        "label": {
          "sc": "2026-05",
          "tc": "2026-05"
        },
        "itemCount": 11,
        "itemIds": [
          "allianz-20260528-global-report",
          "cpic-20260504-gen3",
          "fwd-2026-q1-update",
          "sunlife-2026-10life-awards",
          "ia-20260508-rbc-conclusion",
          "ia-20260513-cross-ref",
          "ia-20260519-disclosure-consult",
          "ia-20260520-gl34-corp",
          "ia-20260529-onsite-findings",
          "ia-20260513-cross-refcheck",
          "ia-20260508-rbc-conclusions"
        ],
        "leadTitle": {
          "sc": "安联全球保险报告2026：全球保费+7.1%至6.9万亿欧元 亚洲领跑。",
          "tc": "安聯全球保險報告2026：全球保費+7.1%至6.9萬億歐元 亞洲領跑。"
        },
        "note": {
          "sc": "2026-05 共 11 条",
          "tc": "2026-05 共 11 條"
        }
      },
      {
        "key": "2026-04",
        "label": {
          "sc": "2026-04",
          "tc": "2026-04"
        },
        "itemCount": 14,
        "itemIds": [
          "ia-2025-full-year",
          "chinlife-2026-hk-digital",
          "aia-20260430-q1-vonb",
          "prudential-20260429-self-future",
          "manulife-20260420-annuity-accident",
          "ctflife-20260422-artisan-leap",
          "boclife-20260427-retirement",
          "aia-20260424-top-insurer",
          "legco-20260410-fa-disclosure",
          "ia-202604-fsi-survey",
          "ia-20260424-stats-2025",
          "ia-20260422-ils",
          "ia-20260416-cyber",
          "ia-20260409-captive-beijing"
        ],
        "leadTitle": {
          "sc": "保监局公布2025全年业绩：个人新单保费3309亿港元 +50.6%再创新高。",
          "tc": "保監局公布2025全年業績：個人新單保費3309億港元 +50.6%再創新高。"
        },
        "note": {
          "sc": "2026-04 共 14 条",
          "tc": "2026-04 共 14 條"
        }
      },
      {
        "key": "2026-03",
        "label": {
          "sc": "2026-03",
          "tc": "2026-03"
        },
        "itemCount": 16,
        "itemIds": [
          "hkma-ia-2026-genai-sandbox",
          "sunlife-202603-sp-upgrade",
          "ia-2025-complaints",
          "aia-2025-annual-results",
          "chubb-2026-dementia",
          "hsbc-life-2026-hnw-pitchbook",
          "prudential-20260317-youth",
          "ia-20260331-gn16-revised",
          "ia-20260310-rbc-consult-close",
          "manulife-202603-new-products",
          "gn16-revised-20260331",
          "ia-20260331-cpd-reporting",
          "ia-20260327-cif12",
          "ia-20260326-health-conf",
          "ia-20260325-captive-forum-speech",
          "ia-20260305-genai-sandbox"
        ],
        "leadTitle": {
          "sc": "香港金融监管联合推出GenAI Sandbox++：用AI监管AI风险。",
          "tc": "香港金融監管聯合推出GenAI Sandbox++：用AI監管AI風險。"
        },
        "note": {
          "sc": "2026-03 共 16 条",
          "tc": "2026-03 共 16 條"
        }
      },
      {
        "key": "2026-02",
        "label": {
          "sc": "2026-02",
          "tc": "2026-02"
        },
        "itemCount": 11,
        "itemIds": [
          "fstb-20260210-fo-3384",
          "hk-2026-newcies-3000",
          "dlapiper-202602-gl16",
          "sunlife-2025-ape-118",
          "ia-20260211-rbc-consult-launch",
          "circ-20260201-crossborder",
          "ia-budget-20260225",
          "ia-20260224-kpim-handbook",
          "ia-20260213-low-altitude",
          "ia-20260211-rbc-consult",
          "ia-20260206-gl16-gl34"
        ],
        "leadTitle": {
          "sc": "香港家族办公室达3384间 两年增25% 过半财富超5100万美元。",
          "tc": "香港家族辦公室達3384間 兩年增25% 過半財富超5100萬美元。"
        },
        "note": {
          "sc": "2026-02 共 11 条",
          "tc": "2026-02 共 11 條"
        }
      },
      {
        "key": "2026-01",
        "label": {
          "sc": "2026-01",
          "tc": "2026-01"
        },
        "itemCount": 8,
        "itemIds": [
          "evident-2026-insurance-ai",
          "ebact-2025-hk-market",
          "manulife-20260105-two-plans",
          "axa-20260126-redomicile",
          "ia-20260123-q3stats",
          "ia-20260126-aff",
          "ia-20260123-stats-3q2025",
          "ia-gl34-20260331"
        ],
        "leadTitle": {
          "sc": "Evident报告：68%保险AI部署已转向生成式/代理式AI。",
          "tc": "Evident報告：68%保險AI部署已轉向生成式/代理式AI。"
        },
        "note": {
          "sc": "2026-01 共 8 条",
          "tc": "2026-01 共 8 條"
        }
      },
      {
        "key": "2025-12",
        "label": {
          "sc": "2025-12",
          "tc": "2025-12"
        },
        "itemCount": 3,
        "itemIds": [
          "ia-2024-annual-stats",
          "zhihu-2025-top10",
          "jpmorgan-2026-outlook"
        ],
        "leadTitle": {
          "sc": "保监局发布2024年香港保险业年报：毛保费6352亿 全球渗透率第一。",
          "tc": "保監局發布2024年香港保險業年報：毛保費6352億 全球滲透率第一。"
        },
        "note": {
          "sc": "2025-12 共 3 条",
          "tc": "2025-12 共 3 條"
        }
      },
      {
        "key": "2025-11",
        "label": {
          "sc": "2025-11",
          "tc": "2025-11"
        },
        "itemCount": 4,
        "itemIds": [
          "sfc-2025-wmc-insurance",
          "goldman-2026-macro-outlook",
          "aia-20251121-aisan",
          "ia-20251120-refcheck-scheme"
        ],
        "leadTitle": {
          "sc": "证监会探讨保险产品纳入跨境理财通南向通。",
          "tc": "證監會探討保險產品納入跨境理財通南向通。"
        },
        "note": {
          "sc": "2025-11 共 4 条",
          "tc": "2025-11 共 4 條"
        }
      },
      {
        "key": "2025-10",
        "label": {
          "sc": "2025-10",
          "tc": "2025-10"
        },
        "itemCount": 3,
        "itemIds": [
          "ia-20251024-h1stats",
          "ia-20251024-1h2025-stats",
          "ia-ro-cpd-20251014"
        ],
        "leadTitle": {
          "sc": "保监局公布2025年上半年临时统计：毛保费4234亿，新造保费1737亿。",
          "tc": "保監局公布2025年上半年臨時統計：毛保費4234億，新造保費1737億。"
        },
        "note": {
          "sc": "2025-10 共 3 条",
          "tc": "2025-10 共 3 條"
        }
      },
      {
        "key": "2025-09",
        "label": {
          "sc": "2025-09",
          "tc": "2025-09"
        },
        "itemCount": 6,
        "itemIds": [
          "manulife-20250902-hospitals",
          "ia-20250901-referral50",
          "ia-20250917-product-naming",
          "ia-202508-iul-sandbox",
          "ia-20250919-product-naming",
          "ia-20250901-referral-fee"
        ],
        "leadTitle": {
          "sc": "宏利医疗网络扩展至内地38000+间医院。",
          "tc": "宏利醫療網絡擴展至內地38000+間醫院。"
        },
        "note": {
          "sc": "2025-09 共 6 条",
          "tc": "2025-09 共 6 條"
        }
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
        ],
        "leadTitle": {
          "sc": "保监局2024-25年报：监管157家保司+11.8万中介 罚款2300万。",
          "tc": "保監局2024-25年報：監管157家保司+11.8萬中介 罰款2300萬。"
        },
        "note": {
          "sc": "2025-08 共 4 条",
          "tc": "2025-08 共 4 條"
        }
      },
      {
        "key": "2025-07",
        "label": {
          "sc": "2025-07",
          "tc": "2025-07"
        },
        "itemCount": 4,
        "itemIds": [
          "aia-20250708-global-prosper",
          "ia-20250701-illustration-cap",
          "ia-202507-commission-spread",
          "ia-20250711-ro-cpd-compulsory"
        ],
        "leadTitle": {
          "sc": "AIA推出「环宇盈活储蓄保险计划」",
          "tc": "AIA推出「環宇盈活儲蓄保險計劃」"
        },
        "note": {
          "sc": "2025-07 共 4 条",
          "tc": "2025-07 共 4 條"
        }
      },
      {
        "key": "2025-06",
        "label": {
          "sc": "2025-06",
          "tc": "2025-06"
        },
        "itemCount": 3,
        "itemIds": [
          "fstb-2024-density",
          "sunlife-2025-enhanced-savings",
          "ia-2025q1-stats-934"
        ],
        "leadTitle": {
          "sc": "香港保险密度0043全球第二 渗透率18.2%全球第一。",
          "tc": "香港保險密度0043全球第二 滲透率18.2%全球第一。"
        },
        "note": {
          "sc": "2025-06 共 3 条",
          "tc": "2025-06 共 3 條"
        }
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
          "axa-20250409-gba-med",
          "ia-2025-d-sii-designation"
        ],
        "leadTitle": {
          "sc": "宏利推出两款全新危疾计划：宏健守护+宏伴护航危疾入息保障。",
          "tc": "宏利推出兩款全新危疾計劃：宏健守護+宏伴護航危疾入息保障。"
        },
        "note": {
          "sc": "2025-04 共 3 条",
          "tc": "2025-04 共 3 條"
        }
      },
      {
        "key": "2025-03",
        "label": {
          "sc": "2025-03",
          "tc": "2025-03"
        },
        "itemCount": 6,
        "itemIds": [
          "ia-2025-insurtech-initiatives",
          "fsdc-2025-insurance-hub",
          "aia-2024-annual",
          "ia-20250313-iul-circular",
          "ia-20250330-illustration-article",
          "ia-20250313-iul-pi"
        ],
        "leadTitle": {
          "sc": "保监局2025年InsurTech蓝图：AI对保险业价值9.5-15.4万亿美元。",
          "tc": "保監局2025年InsurTech藍圖：AI對保險業價值9.5-15.4萬億美元。"
        },
        "note": {
          "sc": "2025-03 共 6 条",
          "tc": "2025-03 共 6 條"
        }
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
        ],
        "leadTitle": {
          "sc": "金融监管总局放宽港澳金融机构入股保险公司门槛。",
          "tc": "金融監管總局放寬港澳金融機構入股保險公司門檻。"
        },
        "note": {
          "sc": "2025-02 共 4 条",
          "tc": "2025-02 共 4 條"
        }
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
        ],
        "leadTitle": {
          "sc": "业界回顾2024香港保险关键趋势：RBC生效/GN16修订/跨境复苏。",
          "tc": "業界回顧2024香港保險關鍵趨勢：RBC生效/GN16修訂/跨境復甦。"
        },
        "note": {
          "sc": "2025-01 共 2 条",
          "tc": "2025-01 共 2 條"
        }
      },
      {
        "key": "2024-09",
        "label": {
          "sc": "2024-09",
          "tc": "2024-09"
        },
        "itemCount": 3,
        "itemIds": [
          "sunlife-2024-fwd-pension",
          "ia-20240923-refcheck",
          "ia-2024h1-stats"
        ],
        "leadTitle": {
          "sc": "Sun Life永明收购FWD香港养老金业务 强积金+46亿港元。",
          "tc": "Sun Life永明收購FWD香港養老金業務 強積金+46億港元。"
        },
        "note": {
          "sc": "2024-09 共 3 条",
          "tc": "2024-09 共 3 條"
        }
      },
      {
        "key": "2024-08",
        "label": {
          "sc": "2024-08",
          "tc": "2024-08"
        },
        "itemCount": 2,
        "itemIds": [
          "nfra-2024-crossborder-no",
          "ia-2024-crossborder"
        ],
        "leadTitle": {
          "sc": "金融监管总局：现阶段跨境保险通试点时机尚不成熟。",
          "tc": "金融監管總局：現階段跨境保險通試點時機尚不成熟。"
        },
        "note": {
          "sc": "2024-08 共 2 条",
          "tc": "2024-08 共 2 條"
        }
      },
      {
        "key": "2024-07",
        "label": {
          "sc": "2024-07",
          "tc": "2024-07"
        },
        "itemCount": 2,
        "itemIds": [
          "ctflife-20240723-rebrand",
          "ia-20240701-rbc-live"
        ],
        "leadTitle": {
          "sc": "FTLife正式更名为周大福人寿(CTF Life)。",
          "tc": "FTLife正式更名為周大福人壽(CTF Life)。"
        },
        "note": {
          "sc": "2024-07 共 2 条",
          "tc": "2024-07 共 2 條"
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
        "itemCount": 120,
        "itemIds": [
          "fstb-20260210-fo-3384",
          "hk-20260612-fo-tax",
          "hk-2026-newcies-3000",
          "hkma-ia-2026-genai-sandbox",
          "evident-2026-insurance-ai",
          "empf-2026-fee-reduction",
          "ratings-2026-consolidated",
          "sunlife-202603-sp-upgrade",
          "ia-2025-complaints",
          "ia-2025-full-year",
          "ebact-2025-hk-market",
          "dlapiper-202602-gl16",
          "insbus-202607-hk-growth",
          "creditsights-2026-2h",
          "swissre-202607-wis",
          "allianz-20260528-global-report",
          "rga-2026-hk-market",
          "deloitte-2026-insurance-outlook",
          "aia-2025-annual-results",
          "sunlife-2025-ape-118",
          "chubb-20260601-mylegacy",
          "chubb-2026-dementia",
          "taiping-202606-rating",
          "cpic-20260504-gen3",
          "fwd-2026-q1-update",
          "fwd-2026-brand-victoria",
          "hsbc-life-2026-hnw-pitchbook",
          "chinlife-2026-hk-digital",
          "aia-20260716-hyrox",
          "aia-20260608-prosperlife",
          "aia-20260430-q1-vonb",
          "prudential-20260317-youth",
          "prudential-20260429-self-future",
          "manulife-20260105-two-plans",
          "manulife-20260420-annuity-accident",
          "manulife-20260625-board",
          "axa-20260126-redomicile",
          "axa-2026-bloomberg-awards",
          "sunlife-2026-10life-awards",
          "ctflife-20260422-artisan-leap",
          "ctflife-2026-diamond-iul",
          "boclife-20260427-retirement",
          "ia-20260123-q3stats",
          "ia-20260331-gn16-revised",
          "ia-20260310-rbc-consult-close",
          "manulife-202603-new-products",
          "ia-20260211-rbc-consult-launch",
          "circ-20260201-crossborder",
          "aia-20260424-top-insurer",
          "ia-20260605-hkma-commission",
          "ia-ai-cohort-202606",
          "ia-20260508-rbc-conclusion",
          "ia-20260513-cross-ref",
          "ia-20260519-disclosure-consult",
          "ia-20260520-gl34-corp",
          "gn16-revised-20260331",
          "legco-20260410-fa-disclosure",
          "ia-202604-fsi-survey",
          "aif-2026-save-the-date",
          "ia-public-disclosure-2026",
          "ia-q1-2026-stats",
          "hkma-complaints-20260724",
          "ia-20260716-ashk-ifoa",
          "ia-20260715-sales-practices",
          "ia-licence-20260630",
          "ia-20260712-speech",
          "ia-20260712-speech",
          "ia-20260710-illustration",
          "ia-20260710-illustration-review",
          "fstb-20260708-captive",
          "ia-20260708-captive",
          "ia-20260703-rfyc",
          "ia-crossref-20260701",
          "ia-20260630-swissre-sigma",
          "ia-20260630-allianz-report",
          "ia-20260629-sunlife-notes",
          "ia-20260629-hkma-bulletin",
          "ia-20260628-fsdc-talent",
          "ia-20260626-morganstanley",
          "ia-20260626-pimco-asia",
          "ia-20260625-manulife-convention",
          "ia-20260624-rga-trends",
          "ia-20260620-goldman-outlook",
          "ia-20260618-blackrock-outlook",
          "ia-20260617-manulife-ai",
          "ia-20260616-aia-prudential-roles",
          "ia-20260616-cheung-enforcement",
          "ia-ai-seminar-20260615",
          "ia-20260615-bloomberg-crackdown",
          "ia-20260612-manulife-plans",
          "ia-20260610-manulife-leverage",
          "ia-20260610-chowtaifook-life",
          "ia-20260609-fitch-apac",
          "ia-20260608-axa-global-private",
          "ia-20260608-aia-wealth-flexi",
          "ia-20260605-hkma-remuneration-circ",
          "ia-hkma-remuneration-20260605",
          "ia-20260611-chubb-life",
          "ia-20260603-broker-referral",
          "ia-20260602-hkma-crossborder",
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
          "sc": "香港家族办公室达3384间 两年增25% 过半财富超5100万美元。",
          "tc": "香港家族辦公室達3384間 兩年增25% 過半財富超5100萬美元。"
        },
        "note": {
          "sc": "2026 年共 120 条",
          "tc": "2026 年共 120 條"
        }
      },
      {
        "key": "2025",
        "label": {
          "sc": "2025 年",
          "tc": "2025 年"
        },
        "itemCount": 42,
        "itemIds": [
          "ia-2025-insurtech-initiatives",
          "nfra-202502-hkmo-insurance",
          "sfc-2025-wmc-insurance",
          "ia-2024-annual-stats",
          "ia-2024-25-annual-report",
          "fstb-2024-density",
          "fsdc-2025-insurance-hub",
          "dlapiper-202508-commission",
          "zhihu-2025-top10",
          "linkedin-2024-trends",
          "goldman-2026-macro-outlook",
          "jpmorgan-2026-outlook",
          "aia-2024-annual",
          "aia-20250708-global-prosper",
          "aia-20251121-aisan",
          "manulife-20250428-ci",
          "manulife-20250902-hospitals",
          "axa-20250110-shengli",
          "axa-20250409-gba-med",
          "sunlife-2025-enhanced-savings",
          "ia-20250228-illustration-note",
          "ia-20250313-iul-circular",
          "ia-20251024-h1stats",
          "ia-2025q1-stats-934",
          "ia-2025-d-sii-designation",
          "ia-20250901-referral50",
          "ia-20250917-product-naming",
          "ia-20250701-illustration-cap",
          "ia-202508-iul-sandbox",
          "ia-202507-commission-spread",
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
          "sc": "保监局2025年InsurTech蓝图：AI对保险业价值9.5-15.4万亿美元。",
          "tc": "保監局2025年InsurTech藍圖：AI對保險業價值9.5-15.4萬億美元。"
        },
        "note": {
          "sc": "2025 年共 42 条",
          "tc": "2025 年共 42 條"
        }
      },
      {
        "key": "2024",
        "label": {
          "sc": "2024 年",
          "tc": "2024 年"
        },
        "itemCount": 7,
        "itemIds": [
          "nfra-2024-crossborder-no",
          "ctflife-20240723-rebrand",
          "sunlife-2024-fwd-pension",
          "ia-20240701-rbc-live",
          "ia-20240923-refcheck",
          "ia-2024h1-stats",
          "ia-2024-crossborder"
        ],
        "leadTitle": {
          "sc": "金融监管总局：现阶段跨境保险通试点时机尚不成熟。",
          "tc": "金融監管總局：現階段跨境保險通試點時機尚不成熟。"
        },
        "note": {
          "sc": "2024 年共 7 条",
          "tc": "2024 年共 7 條"
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
        {id:"pulse",label:"今日脉搏",ico:"◈"},{id:"all",label:"全部动态",ico:"☰"},{id:"daily",label:"角色日报",ico:"▣"},{id:"themes",label:"主题雷达",ico:"◎"},{id:"calendar",label:"事件日历",ico:"◷"},{id:"download",label:"数据下载",ico:"⬇"},{id:"fav",label:"收藏",ico:"☆"},{id:"agent",label:"Agent 接入",ico:"⌘"},{id:"changelog",label:"更新日志",ico:"◌"},{id:"about",label:"关于",ico:"ⓘ"}
      ],
      sec:{c:"内容",a:"接入",m:"更多"},
      views:{
        pulse:{t:"今日脉搏",s:"按你的角色加权的高价值精选"},
        all:{t:"全部动态",s:"全量信息流 · 按信源/文种细筛（≠主题雷达）"},
        daily:{t:"角色日报",s:"固定节奏的专业早报"},download:{t:"数据下载",s:"按日/周/月/年打包导出 Markdown · 原文可溯"},
        themes:{t:"主题雷达",s:"六大业务板块地图 · 战略导航，不是信息流细筛"},
        calendar:{t:"事件日历",s:"关键事件 · 生效日 · 行业节点"},
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
      themesIntro:"点击主题进入全部动态并筛选。", calH:"关键节点", dailyLead:"按区块聚合的专业早报。排序随角色变化。",
      evergreen:"生效中 · 常驻",
      archiveTabs:{daily:"日报",weekly:"周报",monthly:"月报",yearly:"年报"},
      downloadHint:"日报、周报可下载 Markdown。月报、年报仅可在线查阅，不提供下载。也可发送到邮箱。数字与规则以原文链接为准。",
      openDigest:"查看该期条目",
      backDownload:"返回列表",emailTo:"发送到邮箱（规划中）",emailSent:"已发送",emailHint:"功能规划中，暂不支持",monthlyYearlyReadOnly:"月报与年报仅可在线查阅，不提供下载。",
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
        {id:"pulse",label:"今日脈搏",ico:"◈"},{id:"all",label:"全部動態",ico:"☰"},{id:"daily",label:"角色日報",ico:"▣"},{id:"themes",label:"主題雷達",ico:"◎"},{id:"calendar",label:"事件日曆",ico:"◷"},{id:"download",label:"數據下載",ico:"⬇"},{id:"fav",label:"收藏",ico:"☆"},{id:"agent",label:"Agent 接入",ico:"⌘"},{id:"changelog",label:"更新日誌",ico:"◌"},{id:"about",label:"關於",ico:"ⓘ"}
      ],
      sec:{c:"內容",a:"接入",m:"更多"},
      views:{
        pulse:{t:"今日脈搏",s:"按你的角色加權的高價值精選"},
        all:{t:"全部動態",s:"全量資訊流 · 按信源/文種細篩（≠主題雷達）"},
        daily:{t:"角色日報",s:"固定節奏的專業早報"},download:{t:"數據下載",s:"按日/週/月/年打包導出 Markdown · 原文可溯"},
        themes:{t:"主題雷達",s:"六大業務板塊地圖 · 戰略導航，不是資訊流細篩"},
        calendar:{t:"事件日曆",s:"關鍵事件 · 生效日 · 行業節點"},
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
      themesIntro:"點擊主題進入全部動態並篩選。", calH:"關鍵節點", dailyLead:"按區塊聚合的專業早報。排序隨角色變化。",
      evergreen:"生效中 · 常駐",
      archiveTabs:{daily:"日報",weekly:"週報",monthly:"月報",yearly:"年報"},
      downloadHint:"日報、週報可下載 Markdown。月報、年報僅可在線查閱，不提供下載。也可發送到郵箱。數字與規則以原文鏈接為準。",
      openDigest:"查看該期條目",
      backDownload:"返回列表",emailTo:"發送到郵箱（規劃中）",emailSent:"已發送",emailHint:"功能規劃中，暫不支持",monthlyYearlyReadOnly:"月報與年報僅可在線查閱，不提供下載。",
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
      ${n.slice(0,7).map(x=>`<button class="nav-item ${state.view===x.id?'active':''}" data-view="${x.id}"><span class="ico">${x.ico}</span>${x.label}</button>`).join("")}
      <div class="nav-section">${t.sec.a}</div>
      ${n.slice(7,9).map(x=>`<button class="nav-item ${state.view===x.id?'active':''}" data-view="${x.id}"><span class="ico">${x.ico}</span>${x.label}</button>`).join("")}
      <div class="nav-section">${t.sec.m}</div>
      ${n.slice(9).map(x=>`<button class="nav-item ${state.view===x.id?'active':''}" data-view="${x.id}"><span class="ico">${x.ico}</span>${x.label}</button>`).join("")}`;
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
    // 所有视图：严格发布时间降序；筛选不改变排序键
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
  function feed(items){
    const t=T();
    if(!items.length) return `<div class="empty">${t.empty}</div>`;
    const sorted = items.slice().sort(byPublishedDesc);
    const map=new Map();
    sorted.forEach(it=>{const d=fmtDay(it.publishedAt); if(!map.has(d.key)) map.set(d.key,{meta:d,items:[]}); map.get(d.key).items.push(it);});
    const groups = [...map.values()].sort((a,b)=> (b.meta.key||"").localeCompare(a.meta.key||""));
    groups.forEach(g=> g.items.sort(byPublishedDesc));
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
    const items=(DATA.hot||[]).map(byId).filter(Boolean);
    if(!items.length) return "";
    return `<section class="hot"><div class="hot-label">${t.hot}</div><ol>${items.map((it,i)=>`<li><button type="button" data-open="${it.id}">${esc(tx(it.title))}</button></li>`).join("")}</ol></section>`;
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
        html+=`<div class="evergreen-banner-wrapper"><h3>${t.evergreen}</h3><p class="evergreen-hint">← 滑动查看 · 驻点：持续有效的监管规则与长期适用的披露要求 →</p><div class="evergreen-scroll"><button class="evergreen-scroll-btn" onclick="this.nextElementSibling.scrollBy({left:-300,behavior:'smooth'})">‹</button><div class="evergreen-banner">${eg.map(it=>`<div class="banner-card" data-open="${it.id}"><div class="banner-tag">常驻</div><h4>${esc(tx(it.title))}</h4><p>${esc(tx(it.summary))}</p></div>`).join("")}</div><button class="evergreen-scroll-btn" onclick="this.previousElementSibling.scrollBy({left:300,behavior:'smooth'})">›</button></div></div>`;
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
        const b = boards.find(x=>x.id===state.themeBoard) || {id:state.themeBoard,title:{sc:state.themeBoard},desc:{sc:""},subs:[]};
        const its = byBoard(state.themeBoard);
        html += `<div class="taxon-hero">
          <button type="button" class="pill" data-board-back="1">← ${t.boardBack||"返回"}</button>
          <h3>${esc(tx(b.title))}</h3>
          <p>${esc(tx(b.desc)||"")}</p>
          <div class="taxon-subs">${(b.subs||[]).map(s=>`<span class="chip chip-sub">#${s}</span>`).join(" ")}</div>
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
            <div class="taxon-subs">${(b.subs||[]).slice(0,5).map(s=>`<span class="tag">${s}</span>`).join(" ")}</div>
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
              <button type="button" class="btn primary" data-export-digest="1" disabled style="opacity:.4" title="规划中">${t.digestExport} · MD</button>
              <button type="button" class="btn" data-email-digest="1">📧 ${t.emailTo}</button>
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
        {date:"2026-07-28", items:["RSS/API 骨架上线","Agent 接入页面","主题雷达改版","下载页分页+统计条","热搜下拉","卡片时间统一","日分组收起"]},
        {date:"2026-07-27", items:["初始部署上线","首批 171 条资讯","四角色切片","简繁切换","深色模式"]}
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
          <li>评分原则（60-99）：信源权重(official>insurer>pro>media) × 60% + 内容时效/角色覆盖面 × 25% + 人工校准 × 15%。90+为高确定性一手监管或官方披露；70-89为专业解读；60-69为媒体线索待核。</li>
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
    $("#posterCopy").onclick=async()=>{
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
