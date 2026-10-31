# -*- coding: utf-8 -*-
import json, os, collections

ROOT = '/Users/leonliang/maoquanqingbao'
PATH = os.path.join(ROOT, 'data', 'live-items.json')
NOW = '2026-10-30T18:15:00+08:00'

NEW = [
{
 "id": "ia-hk-life-q3-slowdown-jefferies-20261030",
 "publishedAt": "2026-10-30T07:00:00+08:00",
 "originalUrl": "https://insuranceasia.com/insurance/news/hong-kong-life-insurers-face-slowdown-2025-gains-distort-growth-jefferies",
 "sourceKey": "insuranceasia", "sourceTier": "pro", "score": 72, "contentKind": "news",
 "boards": ["market"], "themes": ["新造保费", "业绩展望", "客户需求"],
 "title": {"sc": "Jefferies：港险三季度增速将「看起来放缓」　但需求未转弱（AIA 新业务价值同比料跌3%）",
           "tc": "Jefferies：港險三季度增速將「看起來放緩」　但需求未轉弱（AIA 新業務價值同比料跌3%）"},
 "summary": {"sc": "Jefferies 股票研究前瞻：AIA、保诚、富卫等在即将公布的季报中面对高基数，市场共识预测 AIA 第三季新业务价值按季持平、同比跌3%。但底层需求仍稳——汇丰第三季数据显示客户获取量趋稳、恒生银行月度客户增长创新高；汇丰年化新造保费维持14亿美元，集团利润存量同比升9.6%至172亿美元（剔除新加坡业务出售后升17.8%），季度确认利润由4亿升至5亿美元；汇丰加恒生占香港直接新造保费29%、有效业务22%。[EN原文]",
            "tc": "Jefferies 股票研究前瞻：AIA、保誠、富衛等在即將公布的季報中面對高基數，市場共識預測 AIA 第三季新業務價值按季持平、同比跌3%。但底層需求仍穩——滙豐第三季數據顯示客戶獲取量趨穩、恒生銀行月度客戶增長創新高；滙豐年化新造保費維持14億美元，集團利潤存量同比升9.6%至172億美元（剔除新加坡業務出售後升17.8%），季度確認利潤由4億升至5億美元；滙豐加恒生佔香港直接新造保費29%、有效業務22%。[EN原文]"},
 "why": {"sc": "「业绩放缓」多半是基数不是需求。客户拿季报增长数字质疑市场时，用汇丰的新造保费持平＋客户数创新高做反证，比空口讲「需求还在」有力。",
         "tc": "「業績放緩」多半是基數不是需求。客戶拿季報增長數字質疑市場時，用滙豐的新造保費持平＋客戶數創新高做反證，比空口講「需求還在」有力。"},
 "tags": {"sc": ["Jefferies", "新业务价值", "AIA", "汇丰", "高基数"], "tc": ["Jefferies", "新業務價值", "AIA", "滙豐", "高基數"]},
 "actions": {"front": {"sc": "客户答疑：增速放缓≠需求转弱，备好汇丰数据", "tc": "客戶答疑：增速放緩≠需求轉弱，備好滙豐數據"},
             "midback": {"sc": "同业对标：新造保费与客户数分开看", "tc": "同業對標：新造保費與客戶數分開看"},
             "lead": {"sc": "团队简报：季报季话术校准", "tc": "團隊簡報：季報季話術校準"},
             "cross": {"sc": "跨境客户：内地访客需求观察", "tc": "跨境客戶：內地訪客需求觀察"}},
 "rolesImpact": {"front": 3, "midback": 2, "lead": 3, "cross": 2},
 "source": {"sc": "Insurance Asia 2026-10-30", "tc": "Insurance Asia 2026-10-30", "name": "insuranceasia", "date": "2026-10-30", "lang": "en"},
 "lang": "en", "verifyStatus": "verified"
},
{
 "id": "ia-peak-re-sp-outlook-20261030",
 "publishedAt": "2026-10-30T06:00:00+08:00",
 "originalUrl": "https://insuranceasia.com/insurance/news/peak-re-faces-margin-squeeze-global-expansion-grows-sp",
 "sourceKey": "insuranceasia", "sourceTier": "pro", "score": 72, "contentKind": "news",
 "boards": ["insurer"], "themes": ["再保险", "承保纪律", "香港枢纽"],
 "title": {"sc": "标普：Peak Re 增长可期但利润率受压　2026-28年综合成本率升至90-95%",
           "tc": "標普：Peak Re 增長可期但利潤率受壓　2026-28年綜合成本率升至90-95%"},
 "summary": {"sc": "标普全球评级展望：香港再保公司 Peak Re（2025年全球毛保费排名第27）将通过新承保平台、地域扩张及结构化方案与寿险再保实现稳步增长；寿险2025年占其保费不足20%。2026-2028年财险综合成本率预计90%-95%，高于2025年的87.9%，因全球再保费率走软及进入新市场的短期波动。资本维持「极强」，高于标普最严99.95%置信水平；2026年初监管偿付能力比率209%，未来两年派息低于净利30%。[EN原文]",
            "tc": "標普全球評級展望：香港再保公司 Peak Re（2025年全球毛保費排名第27）將通過新承保平台、地域擴張及結構化方案與壽險再保實現穩步增長；壽險2025年佔其保費不足20%。2026-2028年財險綜合成本率預計90%-95%，高於2025年的87.9%，因全球再保費率走軟及進入新市場的短期波動。資本維持「極強」，高於標普最嚴99.95%置信水平；2026年初監管償付能力比率209%，未來兩年派息低於淨利30%。[EN原文]"},
 "why": {"sc": "香港本土再保龙头的评级尺：综合成本率从87.9%抬到90-95%＝费率红利在退，但资本与偿付能力仍厚。谈分出安排时可用来判断对手方稳不稳。",
         "tc": "香港本土再保龍頭的評級尺：綜合成本率從87.9%抬到90-95%＝費率紅利在退，但資本與償付能力仍厚。談分出安排時可用來判斷對手方穩不穩。"},
 "tags": {"sc": ["Peak Re", "标普", "综合成本率", "偿付能力", "再保险"], "tc": ["Peak Re", "標普", "綜合成本率", "償付能力", "再保險"]},
 "actions": {"front": {"sc": "客户沟通：再保对手方稳健度", "tc": "客戶溝通：再保對手方穩健度"},
             "midback": {"sc": "核保参考：再保费率走软趋势", "tc": "核保參考：再保費率走軟趨勢"},
             "lead": {"sc": "团队简报：香港再保生态位", "tc": "團隊簡報：香港再保生態位"},
             "cross": {"sc": "跨境风险：分出与自留结构", "tc": "跨境風險：分出與自留結構"}},
 "rolesImpact": {"front": 2, "midback": 3, "lead": 3, "cross": 2},
 "source": {"sc": "Insurance Asia 2026-10-30", "tc": "Insurance Asia 2026-10-30", "name": "insuranceasia", "date": "2026-10-30", "lang": "en"},
 "lang": "en", "verifyStatus": "verified"
},
{
 "id": "ia-apac-reinsurers-margin-sp-20261030",
 "publishedAt": "2026-10-30T05:00:00+08:00",
 "originalUrl": "https://insuranceasia.com/insurance/in-focus/asia-pacific-reinsurers-face-margin-squeeze-rates-fall",
 "sourceKey": "insuranceasia", "sourceTier": "pro", "score": 70, "contentKind": "news",
 "boards": ["market"], "themes": ["亚太再保", "再保定价", "资产配置"],
 "title": {"sc": "标普：亚太再保未来两年利润率受压　股本回报长期落后全球同业",
           "tc": "標普：亞太再保未來兩年利潤率受壓　股本回報長期落後全球同業"},
 "summary": {"sc": "标普10月28日报告《Asia-Pacific Reinsurance In Charts: Discipline Will Differentiate》：亚太再保2027年前年保费增长2%-4%，但竞争与产能充裕令费率持续受压，尤其理赔纪录良好的保单；已发生大额损失的保单可获加价。亚太再保股本回报长期低于全球同业，2025年承保表现连续第三年改善，但盈利差距料延续至2027年。资产端约25%投向股票、物业及另类资产（全球同业18%），下行时波动更大；新增量在电动车、可再生能源、AI 与数据中心等 specialty 险种。[EN原文]",
            "tc": "標普10月28日報告《Asia-Pacific Reinsurance In Charts: Discipline Will Differentiate》：亞太再保2027年前年保費增長2%-4%，但競爭與產能充裕令費率持續受壓，尤其理賠紀錄良好的保單；已發生大額損失的保單可獲加價。亞太再保股本回報長期低於全球同業，2025年承保表現連續第三年改善，但盈利差距料延續至2027年。資產端約25%投向股票、物業及另類資產（全球同業18%），下行時波動更大；新增量在電動車、可再生能源、AI 與數據中心等 specialty 險種。[EN原文]"},
 "why": {"sc": "「承保纪律决定谁能守住利润率」——这句话可直接搬去跟客户讲续保议价：有理赔纪录的保单今年谈不动价，没纪录的才有空间。",
         "tc": "「承保紀律決定誰能守住利潤率」——這句話可直接搬去跟客戶講續保議價：有理賠紀錄的保單今年談不動價，沒紀錄的才有空間。"},
 "tags": {"sc": ["亚太再保", "标普", "股本回报", "费率", "另类资产"], "tc": ["亞太再保", "標普", "股本回報", "費率", "另類資產"]},
 "actions": {"front": {"sc": "客户沟通：续保议价空间判断", "tc": "客戶溝通：續保議價空間判斷"},
             "midback": {"sc": "组合监控：再保对手方资产风险", "tc": "組合監控：再保對手方資產風險"},
             "lead": {"sc": "团队简报：2027年亚太再保定价", "tc": "團隊簡報：2027年亞太再保定價"},
             "cross": {"sc": "新兴险种：AI/数据中心/新能源", "tc": "新興險種：AI/數據中心/新能源"}},
 "rolesImpact": {"front": 3, "midback": 3, "lead": 3, "cross": 2},
 "source": {"sc": "Insurance Asia 2026-10-30", "tc": "Insurance Asia 2026-10-30", "name": "insuranceasia", "date": "2026-10-30", "lang": "en"},
 "lang": "en", "verifyStatus": "verified"
},
{
 "id": "ia-marine-premiums-iumi-20261030",
 "publishedAt": "2026-10-30T05:15:00+08:00",
 "originalUrl": "https://insuranceasia.com/insurance/news/marine-insurance-premiums-hit-426b-despite-pricing-pressure",
 "sourceKey": "insuranceasia", "sourceTier": "pro", "score": 68, "contentKind": "stats",
 "boards": ["market"], "themes": ["水险", "货运险", "费率"],
 "title": {"sc": "IUMI：2025年全球水险保费升5.5%至426亿美元　货运与船壳带动、费率仍受压",
           "tc": "IUMI：2025年全球水險保費升5.5%至426億美元　貨運與船殼帶動、費率仍受壓"},
 "summary": {"sc": "国际海上保险联盟（IUMI）2026年度统计报告（10月23日发布）：2025年全球水险保费升5.5%至426亿美元。货运险保费同比升6.9%至242亿美元，中国因高价值出口（含 AI 相关技术产品）增长强劲；远洋船壳险升9.4%至105亿美元，受船队扩张、船价与战争险附加费带动，但船队增速仍快过保费；离岸能源微升0.1%至48.2亿美元，市场偏软。理赔环境相对稳定、无单一巨灾主导，但小额高频索赔累积持续挤压盈利。[EN原文]",
            "tc": "國際海上保險聯盟（IUMI）2026年度統計報告（10月23日發布）：2025年全球水險保費升5.5%至426億美元。貨運險保費同比升6.9%至242億美元，中國因高價值出口（含 AI 相關技術產品）增長強勁；遠洋船殼險升9.4%至105億美元，受船隊擴張、船價與戰爭險附加費帶動，但船隊增速仍快過保費；離岸能源微升0.1%至48.2億美元，市場偏軟。理賠環境相對穩定、無單一巨災主導，但小額高頻索賠累積持續擠壓盈利。[EN原文]"},
 "why": {"sc": "做贸易/物流客户的同事可直接引用：保费在涨但费率在跌，涨的是船价与货值不是风险加价；报价高不等于贵，要看保额基数。",
         "tc": "做貿易/物流客戶的同事可直接引用：保費在漲但費率在跌，漲的是船價與貨值不是風險加價；報價高不等於貴，要看保額基數。"},
 "tags": {"sc": ["IUMI", "水险", "货运险", "船壳险", "费率"], "tc": ["IUMI", "水險", "貨運險", "船殼險", "費率"]},
 "actions": {"front": {"sc": "客户沟通：保额上升≠费率上升", "tc": "客戶溝通：保額上升≠費率上升"},
             "midback": {"sc": "核保参考：货运险仍处软市", "tc": "核保參考：貨運險仍處軟市"},
             "lead": {"sc": "团队简报：水险板块年度基准", "tc": "團隊簡報：水險板塊年度基準"},
             "cross": {"sc": "跨境贸易：供应链风险敞口", "tc": "跨境貿易：供應鏈風險敞口"}},
 "rolesImpact": {"front": 2, "midback": 3, "lead": 2, "cross": 2},
 "source": {"sc": "Insurance Asia 2026-10-30", "tc": "Insurance Asia 2026-10-30", "name": "insuranceasia", "date": "2026-10-30", "lang": "en"},
 "lang": "en", "verifyStatus": "verified"
},
{
 "id": "ibm-axa-9m-hk-protection-20261030",
 "publishedAt": "2026-10-30T10:47:00+08:00",
 "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/hong-kong-and-japan-protection-sales-power-axas-life-growth-as-axa-xl-pulls-back-595576.aspx",
 "sourceKey": "insurancebusinessmag", "sourceTier": "media", "score": 64, "contentKind": "news",
 "boards": ["insurer"], "themes": ["保司业绩", "保障需求", "储蓄险"],
 "title": {"sc": "安盛前九月寿险健康保费升7%：香港「保障＋一般账户储蓄」、日本「保障＋投连」带动",
           "tc": "安盛前九月壽險健康保費升7%：香港「保障＋一般賬戶儲蓄」、日本「保障＋投連」帶動"},
 "summary": {"sc": "安盛10月29日公布前九月经营指标：寿险与健康毛保费及其他收入升7%至448亿欧元，集团整体升5%至930亿欧元。保障型保费升5%，主要靠香港「保障＋一般账户储蓄」产品与日本「保障＋投连」产品；一般账户储蓄保费升9%，由日本趸缴产品带动、部分被香港储蓄销售下降抵销。亚洲区（含日本、香港、泰国财险、印尼寿险）保费升7%至161亿欧元，寿险健康升12%至111亿欧元。财险集团升3%，但 AXA XL 保费跌1%、价格跌1%，主动削减意外险量；法国、瑞士、意大利冰雹等次生灾害令巨灾损失超预算；偿付能力比率由218%降至213%。[EN原文]",
            "tc": "安盛10月29日公布前九個月經營指標：壽險與健康毛保費及其他收入升7%至448億歐元，集團整體升5%至930億歐元。保障型保費升5%，主要靠香港「保障＋一般賬戶儲蓄」產品與日本「保障＋投連」產品；一般賬戶儲蓄保費升9%，由日本躉繳產品帶動、部分被香港儲蓄銷售下降抵銷。亞洲區（含日本、香港、泰國財險、印尼壽險）保費升7%至161億歐元，壽險健康升12%至111億歐元。財險集團升3%，但 AXA XL 保費跌1%、價格跌1%，主動削減意外險量；法國、瑞士、意大利冰雹等次生災害令巨災損失超預算；償付能力比率由218%降至213%。[EN原文]"},
 "why": {"sc": "两条可用的同业事实：①香港「保障＋储蓄」组合仍在放量，别只卖纯储蓄；②AXA XL 在亚洲意外险不跟价，谈大额商业险时别预设「一定有人更便宜」。",
         "tc": "兩條可用的同業事實：①香港「保障＋儲蓄」組合仍在放量，別只賣純儲蓄；②AXA XL 在亞洲意外險不跟價，談大額商業險時別預設「一定有人更便宜」。"},
 "tags": {"sc": ["安盛", "AXA XL", "香港", "保障型产品", "偿付能力"], "tc": ["安盛", "AXA XL", "香港", "保障型產品", "償付能力"]},
 "actions": {"front": {"sc": "产品组合：保障＋储蓄打包话术", "tc": "產品組合：保障＋儲蓄打包話術"},
             "midback": {"sc": "同业监控：AXA XL 收缩意外险", "tc": "同業監控：AXA XL 收縮意外險"},
             "lead": {"sc": "团队简报：外资保司亚洲策略分化", "tc": "團隊簡報：外資保司亞洲策略分化"},
             "cross": {"sc": "跨境客户：港日产品差异", "tc": "跨境客戶：港日產品差異"}},
 "rolesImpact": {"front": 3, "midback": 2, "lead": 2, "cross": 2},
 "source": {"sc": "Insurance Business Asia 2026-10-30", "tc": "Insurance Business Asia 2026-10-30", "name": "insurancebusinessmag", "date": "2026-10-30", "lang": "en"},
 "lang": "en", "verifyStatus": "verified"
},
{
 "id": "ibm-credit-insurance-icisa-20261030",
 "publishedAt": "2026-10-30T16:48:00+08:00",
 "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/credit-insurance-covers-9-58trn-in-trade-as-insolvencies-rise-595617.aspx",
 "sourceKey": "insurancebusinessmag", "sourceTier": "media", "score": 62, "contentKind": "stats",
 "boards": ["market"], "themes": ["贸易信用险", "企业破产", "贸易融资"],
 "title": {"sc": "ICISA：2025年贸易信用险承保9.58万亿欧元贸易　但覆盖率降至14%",
           "tc": "ICISA：2025年貿易信用險承保9.58萬億歐元貿易　但覆蓋率降至14%"},
 "summary": {"sc": "国际信用保险及保证保险协会（ICISA）数据：2025年受信用险保障的全球贸易额由9.25万亿欧元升至9.58万亿欧元，但占全球贸易比重由约15%降至14%——世界贸易增速（2025年约4.7%）快于 GDP（2.9%），加上欧元兑美元2025年1月至2026年1月升值17%，压低了美元计价的覆盖率；按不变美元计实际升4个基点。安联贸易指2025年全球企业破产升6%，2026年料再升5%（连续第五年）；ICISA 成员占全球保费约八成，2025年贸易应收款相关承保敞口超3.5万亿欧元，约七成由私营市场提供。[EN原文]",
            "tc": "國際信用保險及保證保險協會（ICISA）數據：2025年受信用險保障的全球貿易額由9.25萬億歐元升至9.58萬億歐元，但佔全球貿易比重由約15%降至14%——世界貿易增速（2025年約4.7%）快於 GDP（2.9%），加上歐元兌美元2025年1月至2026年1月升值17%，壓低了美元計價的覆蓋率；按不變美元計實際升4個基點。安聯貿易指2025年全球企業破產升6%，2026年料再升5%（連續第五年）；ICISA 成員佔全球保費約八成，2025年貿易應收款相關承保敞口超3.5萬億歐元，約七成由私營市場提供。[EN原文]"},
 "why": {"sc": "破产连续五年上升是硬背景：做 B2B 客户的，把「应收款被拖死」当独立风险讲，信用险＋贸易融资的组合比单纯加保额更贴需求。",
         "tc": "破產連續五年上升是硬背景：做 B2B 客戶的，把「應收款被拖死」當獨立風險講，信用險＋貿易融資的組合比單純加保額更貼需求。"},
 "tags": {"sc": ["ICISA", "信用险", "企业破产", "贸易融资", "安联贸易"], "tc": ["ICISA", "信用險", "企業破產", "貿易融資", "安聯貿易"]},
 "actions": {"front": {"sc": "客户沟通：应收款风险单独讲", "tc": "客戶溝通：應收款風險單獨講"},
             "midback": {"sc": "核保参考：破产周期与敞口", "tc": "核保參考：破產週期與敞口"},
             "lead": {"sc": "团队简报：信用险渗透率缺口", "tc": "團隊簡報：信用險滲透率缺口"},
             "cross": {"sc": "跨境贸易：买家违约筛查", "tc": "跨境貿易：買家違約篩查"}},
 "rolesImpact": {"front": 3, "midback": 3, "lead": 2, "cross": 3},
 "source": {"sc": "Insurance Business Asia 2026-10-30", "tc": "Insurance Business Asia 2026-10-30", "name": "insurancebusinessmag", "date": "2026-10-30", "lang": "en"},
 "lang": "en", "verifyStatus": "verified"
},
{
 "id": "hkma-negative-equity-2026q3-20261030",
 "publishedAt": "2026-10-30T16:30:00+08:00",
 "originalUrl": "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/10/20261030-6/",
 "sourceKey": "hkma", "sourceTier": "official", "score": 86, "contentKind": "stats",
 "boards": ["market"], "themes": ["负资产", "按揭风险", "楼市"],
 "title": {"sc": "金管局：9月底负资产住宅按揭降至3,819宗　涉款173亿元、连续第二季回落",
           "tc": "金管局：9月底負資產住宅按揭降至3,819宗　涉款173億元、連續第二季回落"},
 "summary": {"sc": "金管局10月30日公布9月底住宅按揭负资产调查：负资产宗数估计3,819宗，较6月底的4,356宗减少537宗（-12.3%）；涉及金额由196亿元降至173亿元；无抵押部分由9亿元降至8亿元。个案主要与银行职员住屋贷款或按揭保险计划下的按揭（一般按揭成数较高）有关。",
            "tc": "金管局10月30日公布9月底住宅按揭負資產調查：負資產宗數估計3,819宗，較6月底的4,356宗減少537宗（-12.3%）；涉及金額由196億元降至173億元；無抵押部分由9億元降至8億元。個案主要與銀行職員住屋貸款或按揭保險計劃下的按揭（一般按揭成數較高）有關。"},
 "why": {"sc": "官方季度数、连续两季改善——保費融資／按揭掛鈎保單的客户最怕「负资产＋call loan」叙事，这张官方数字是最好用的降温材料。",
         "tc": "官方季度數、連續兩季改善——保費融資／按揭掛鈎保單的客戶最怕「負資產＋call loan」敘事，這張官方數字是最好用的降溫材料。"},
 "tags": {"sc": ["金管局", "负资产", "按揭保险", "楼市", "保费融资"], "tc": ["金管局", "負資產", "按揭保險", "樓市", "保費融資"]},
 "actions": {"front": {"sc": "客户沟通：用官方数字回应负资产担忧", "tc": "客戶溝通：用官方數字回應負資產擔憂"},
             "midback": {"sc": "风险披露：按揭挂钩保单压力测试", "tc": "風險披露：按揭掛鈎保單壓力測試"},
             "lead": {"sc": "团队简报：楼市风险口径统一", "tc": "團隊簡報：樓市風險口徑統一"},
             "cross": {"sc": "跨境客户：港物业敞口盘点", "tc": "跨境客戶：港物業敞口盤點"}},
 "rolesImpact": {"front": 3, "midback": 3, "lead": 2, "cross": 2},
 "source": {"sc": "香港金融管理局 2026-10-30", "tc": "香港金融管理局 2026-10-30", "name": "hkma", "date": "2026-10-30", "lang": "zh+en"},
 "lang": "zh+en", "verifyStatus": "verified"
},
{
 "id": "art-safepoint-nature-coast-2026-2-20261030",
 "publishedAt": "2026-10-30T16:45:00+08:00",
 "originalUrl": "https://www.artemis.bm/news/safepoint-more-than-doubles-nature-coast-re-2026-2-cat-bond-target-to-600m/",
 "sourceKey": "artemis", "sourceTier": "pro", "score": 68, "contentKind": "news",
 "boards": ["market"], "themes": ["巨灾债券", "ILS", "再保资本"],
 "title": {"sc": "SafePoint 巨灾债目标翻倍至6亿美元　为历来最大一笔、AA 层指引降至3.75-4%",
           "tc": "SafePoint 巨災債目標翻倍至6億美元　為歷來最大一筆、AA 層指引降至3.75-4%"},
 "summary": {"sc": "Artemis：SafePoint Insurance 将 Nature Coast Re（2026-2系列）巨灾债券目标由2.5亿美元上调逾一倍至6亿美元，为其历来最大一笔、旗下第10笔巨灾债。两只份额中，Class AA 由1亿美元增至3亿美元，基础预期损失0.73%，价格指引由4%-4.75%下调至3.75%-4%；保障为 SafePoint 及两家互惠交易所的命名风暴损失，采赔偿型、每次事故触发，自12月1日起为期四年，覆盖美国州份范围为该公司历来最广。[EN原文]",
            "tc": "Artemis：SafePoint Insurance 將 Nature Coast Re（2026-2系列）巨災債券目標由2.5億美元上調逾一倍至6億美元，為其歷來最大一筆、旗下第10筆巨災債。兩隻份額中，Class AA 由1億美元增至3億美元，基礎預期損失0.73%，價格指引由4%-4.75%下調至3.75%-4%；保障為 SafePoint 及兩家互惠交易所的命名風暴損失，採賠償型、每次事故觸發，自12月1日起為期四年，覆蓋美國州份範圍為該公司歷來最廣。[EN原文]"},
 "why": {"sc": "巨灾债「加量＋降价」同时出现，说明 ILS 投资者仍在抢风险。这是2027年续保定价会继续松的前置信号，比单看再保公司财报更早。",
         "tc": "巨災債「加量＋降價」同時出現，說明 ILS 投資者仍在搶風險。這是2027年續保定價會繼續鬆的前置信號，比單看再保公司財報更早。"},
 "tags": {"sc": ["巨灾债券", "SafePoint", "ILS", "再保定价", "美国风暴"], "tc": ["巨災債券", "SafePoint", "ILS", "再保定價", "美國風暴"]},
 "actions": {"front": {"sc": "客户沟通：再保成本趋势", "tc": "客戶溝通：再保成本趨勢"},
             "midback": {"sc": "续保准备：2027年条款预期", "tc": "續保準備：2027年條款預期"},
             "lead": {"sc": "团队简报：ILS 资本流向", "tc": "團隊簡報：ILS 資本流向"},
             "cross": {"sc": "跨境资产：巨灾债配置视角", "tc": "跨境資產：巨災債配置視角"}},
 "rolesImpact": {"front": 1, "midback": 3, "lead": 3, "cross": 2},
 "source": {"sc": "Artemis 2026-10-30", "tc": "Artemis 2026-10-30", "name": "artemis", "date": "2026-10-30", "lang": "en"},
 "lang": "en", "verifyStatus": "verified"
},
]

d = json.load(open(PATH))
existing_urls = {(i.get('originalUrl') or '').rstrip('/') for i in d['items']}
existing_ids = {i['id'] for i in d['items']}

added, skipped = [], []
for it in NEW:
    u = it['originalUrl'].rstrip('/')
    if u in existing_urls or it['id'] in existing_ids:
        skipped.append(it['id'])
        continue
    it['clusterCount'] = 1
    it['ingestedAt'] = NOW
    added.append(it)
    existing_urls.add(u)
    existing_ids.add(it['id'])

d['items'] = added + d['items']
d['meta']['generatedAt'] = NOW
d['meta']['itemCount'] = len(d['items'])
d['meta']['windowNote'] = {'sc': f"本库{len(d['items'])}条。", 'tc': f"本庫{len(d['items'])}條。"}
json.dump(d, open(PATH, 'w'), ensure_ascii=False, indent=1)

print('added:', len(added))
for it in added:
    print('  ', it['id'], '|', it['publishedAt'], '|', it['boards'], len(it['summary']['sc']))
print('skipped:', skipped)
print('total now:', len(d['items']))
