#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-03 00:3x 增量采集（承接 10-02 02:20 批次；10-02 18:08/21:08 两班未跑，本班为补跑）。

窗口：2026-10-02 02:20 → 2026-10-03 00:35
逐源核验（14 信源）：
- IA：press_releases / circulars 页对直连与 web 抓取均返回 403（Cloudflare 拦截）；
  circulars 页可得版本最新为 2026-05-13 跨行业背景查核安排 → 窗口内无新增。
- HKMA：新闻稿页实抓，最新为 2026-09-30 16:30 四则统计（货币统计／住宅按揭／外汇基金资产负债表等，已入库）→ 窗口内无新增。
- 保司（AIA/宏利/保诚/安盛/永明）：官网新闻室窗口内无新稿（友邦最新 2025-12-02；宏利最新 2026-09-10；
  保诚列表页最新条目早于窗口；安盛最新 2026-09-07；永明最新 2026-09-15）。
- insuranceasia(RSS)：窗口内 5 则（10-01 21:00–10-02 06:51 UTC 转为 10-02 05:00–14:51 HKT）；
  「This week in insurance」汇总所涉 FWD AML 罚款／保诚新加坡单元信托／Income Insurance 新CEO 均已入库 → 取 3 则。
- insuranceasianews(WP API)：窗口内 8 则，取 5 则（人事与市场类，剔除重复主题）。
- insurancebusinessmag(Atom)：窗口内 5 则，取 4 则（「Allianz names new CEOs at Allianz Partners/
  Allianz Direct」与他源安联人事重叠，暂不取）。
- scmp(RSS 92)：窗口内 9 则，仅 1 则与本域相关（Savills 下一代财富枢纽指数：香港第七、落后新加坡）→ 取 1 则。
- artemis(RSS)：窗口内 4 则，取 2 则（Hannover Re Capital Partners 百慕达基金与 SPI；Willis 北美商业地产费率十年最大跌幅）。
- NFRA：官网 JS 不可直连；经检索与站内比对，窗口内无新发（《保险法（修订草案征求意见稿）》10月3日截止征求意见，主体已于 09-04 入库）。
- govhk(info.gov.hk RSS)：10-02 共 7 则含关键词，均为运输物流／商务经发局五年规划简报、海关执法等 → 无保险实体内容，不取。
- HKFI：media-release 路径改版 404，检索确认最新新闻稿为 2026-09-16 → 窗口内无新增。
- family_office / insurtech：窗口内无新增（insurtech 取 Bolttech×Bold Penguin 已于 10-01 入库）。
本批 15 条覆盖 insuranceasianews / insuranceasia / insurancebusinessmag / artemis / scmp 五类信源（5 个 sourceKey）。
"""
import json, shutil, os
import zhconv

BASE = '/Users/leonliang/maoquanqingbao'
NOW = '2026-10-03T00:35:00+08:00'

FIX = {'轉帳': '轉賬', '鏈接': '連結', '裏面': '裡面'}


def tc(s):
    out = zhconv.convert(s, 'zh-tw')
    for a, b in FIX.items():
        out = out.replace(a, b)
    return out


def T(sc, tcv=None):
    return {'sc': sc, 'tc': tcv if tcv else tc(sc)}


def item(**kw):
    d = {
        'clusterCount': 1, 'score': 65, 'verifyStatus': 'pending',
        'sourceTier': 'media', 'sourceKey': '', 'contentKind': 'news',
        'actions': {'front': {}, 'midback': {}, 'lead': {}, 'cross': {}},
        'rolesImpact': {'front': 0, 'midback': 0, 'lead': 0, 'cross': 0},
        'boards': [], 'themes': [], 'tags': {'sc': [], 'tc': []},
        'contentRole': {'sc': '本站导读', 'tc': '本站導讀'},
        'featured': False, 'evergreen': False, 'ingestedAt': NOW,
    }
    d.update(kw)
    return d


def tg(*words):
    return {'sc': list(words), 'tc': [tc(w) for w in words]}


NEW = [
    # ============ 1. 苏黎世完成对 Beazley 的收购（全球最大专业险集团） ============
    item(id='ibm-zurich-beazley-completion-cox-exit-20261002', score=66, verifyStatus='verified',
         sourceTier='media', sourceKey='insurancebusinessmag', contentKind='news',
         publishedAt='2026-10-02T18:11:00+08:00',
         title=T('苏黎世保险完成对 Beazley 的81亿英镑（约109亿美元）收购：合并后按承保保费计成为全球最大专业险集团，Beazley 同日自伦交所摘牌、进入 Lloyd\'s 市场；行政总裁 Adrian Cox 离任，由苏黎世欧洲、中东区CEO Kristof Terryn 出任 Beazley 及苏黎世全球专业险CEO（待监管批准） [EN原文]',
                 '蘇黎世保險完成對 Beazley 的81億英鎊（約109億美元）收購：合併後按承保保費計成爲全球最大專業險集團，Beazley 同日自倫交所摘牌、進入 Lloyd\'s 市場；行政總裁 Adrian Cox 離任，由蘇黎世歐洲、中東區CEO Kristof Terryn 出任 Beazley 及蘇黎世全球專業險CEO（待監管批准）[EN原文]'),
         summary=T('Insurance Business Asia 10月2日18:11（香港时间）报道：苏黎世保险集团确认完成对 Beazley 的81亿英镑（约109亿美元）收购，合并后实体按其口径成为全球按承保保费计最大的专业险集团。公告同时确认 Adrian Cox 不再担任 Beazley 行政总裁，集团未交代离任时间；Kristof Terryn 获任命为 Beazley 及苏黎世全球专业险CEO（待监管批准），Helen Pickford 出任CFO、Sally Henderson 出任首席人才与可持续发展官。整合目标包括2029年前年收入增量逾10亿美元、年成本节省至少1.5亿美元，以及两年内一次性释放至少10亿美元资本。安排计划于10月1日生效、Beazley 股份停牌，10月2日自伦敦证券交易所摘牌；其辛迪加为苏黎世带来 Lloyd\'s 平台，集团称是其首次进入 Lloyd\'s 市场。', None),
         why=T('专业险与再保的供给结构在这一并购后更集中：苏黎世获得 Lloyd\'s 辛迪加平台与 Beazley 的专业险组合，意味着可承保能力与定价权向少数综合集团靠拢。对依赖专业险、特种险与再保渠道的方案设计者，供给方减少通常先体现为条款与自留额度的议价空间收窄，随后才反映在费率上；整合期还常出现承保团队流失与授权边界调整。此外「两年释放10亿美元资本」的目标提示新集团会主动优化资本占用，历史上这类动作会传导为对低回报业务的收紧续保。', None),
         actions={'front': T('客户问及专业险板块时，只陈述公开的并购与人事事实，不推断条款或费率走向'),
                  'midback': T('把主要再保／专业险对手方的整合进度纳入对手方风险与合约联络人档案'),
                  'lead': T('留意整合期承保团队流动对既有合作条款与服务连续性的影响'),
                  'cross': T('跨境与特种风险项目须重新确认合并后承保主体的授权与签单能力')},
         rolesImpact={'front': 1, 'midback': 2, 'lead': 2, 'cross': 2},
         source={'sc': 'Insurance Business Asia 2026-10-02 18:11（香港时间）[EN原文]',
                 'tc': 'Insurance Business Asia 2026-10-02 18:11（香港時間）[EN原文]', 'lang': 'en'},
         boards=['insurer', 'market'], themes=['ma', 'specialty', 'reinsurance', 'market', 'people'],
         tags=tg('苏黎世', 'Beazley', '专业险', 'Lloyd\'s', '并购', '人事变动'),
         originalUrl='https://www.insurancebusinessmag.com/asia/news/mergers-acquisitions/zurich-completes-beazley-deal-as-adrian-cox-steps-down-as-ceo-592095.aspx'),

    # ============ 2. 韩国：广播渠道销售误导率三倍于其他渠道 ============
    item(id='ibm-korea-broadcast-misselling-fss-20261002', score=64, verifyStatus='verified',
         sourceTier='media', sourceKey='insurancebusinessmag', contentKind='news',
         publishedAt='2026-10-02T22:46:00+08:00',
         title=T('韩国金融监督院（FSS）数据：电视购物／广播广告渠道销售的保单不当销售率为0.036%，是其他渠道0.012%的三倍；第13个月继续率79.3%亦低于其他渠道86.3%，70岁以上客户占该渠道保单13.4%（其他渠道7.4%）；FSS 10月1日召集寿险协会、产险协会、险企及13家电视购物GA商讨收紧广告审查与加大披露 [EN原文]',
                 '韓國金融監督院（FSS）數據：電視購物／廣播廣告渠道銷售的保單不當銷售率爲0.036%，是其他渠道0.012%的三倍；第13個月繼續率79.3%亦低於其他渠道86.3%，70歲以上客戶佔該渠道保單13.4%（其他渠道7.4%）；FSS 10月1日召集壽險協會、產險協會、險企及13家電視購物GA商討收緊廣告審查與加大披露 [EN原文]'),
         summary=T('Insurance Business Asia 10月2日22:46（香港时间）报道：韩国金融监督院（FSS）数据显示，通过广播广告（含电视购物）销售的保单不当销售率0.036%，对比其他渠道0.012%；第13个月保单继续率79.3%，低于其他渠道的86.3%；70岁以上客户占该渠道保单13.4%，其他渠道为7.4%。报道同时说明这是渠道结果差异，并不等同于广告本身直接造成。背景是保险广告投放量激增：2025年平均每日1,121条、较2024年672条增66.9%，每日总时长增65.2%至57小时。FSS 指出反复播出、煽动性用语、夸大表述，以及强调可多次领取利益而不突出限领条件等问题；并于10月1日与韩国寿险协会、一般保险协会、险企及电视购物所属GA（13家）召开会议，讨论强化协会审查标准、提高处罚实效、扩大广告披露与强化险企及GA内控。报道并指过去五年电视购物保险广告仅收到一次警告，现行不当销售处罚门槛0.4%远高于行业平均0.03%，FSS 认为门槛应重新考虑。', None),
         why=T('这是一条可直接引用、且与香港业务高度可类比的操守证据链：代理因素被控制后，广播／购物型渠道的不当销售率仍是其他渠道三倍、继续率低7个百分点，且高龄客群占比近乎翻倍。对前线与培训岗来说，它说明「渠道合规强度」与「客户年龄结构」是比产品本身更有效的风险预测因子；对管理岗来说，处罚门槛与审查时点的设计（播出后审查对直播无效）是制度性漏洞的样本。香港近年对转介业务、分红保单佣金分摊与演示利率的收紧，逻辑一致：把诱因从交易前端移向长期服务。', None),
         actions={'front': T('涉及高龄客户时逐项确认理解程度与缴费能力，避免以「多次领取」类话术替代条款说明'),
                  'midback': T('将「渠道×年龄结构」作为不当销售预警维度，纳入电话／线上展业抽查'),
                  'lead': T('参照该案例检视团队激励是否与继续率脱钩，避免只考核首年成交'),
                  'cross': T('客户涉韩国或东南亚市场配置时，只引述公开监管数据，不作跨市场产品比较')},
         rolesImpact={'front': 2, 'midback': 3, 'lead': 2, 'cross': 1},
         source={'sc': 'Insurance Business Asia 2026-10-02 22:46（据 FSS 数据、首尔经济日报与 SBS 报道）[EN原文]',
                 'tc': 'Insurance Business Asia 2026-10-02 22:46（據 FSS 數據、首爾經濟日報與 SBS 報道）[EN原文]', 'lang': 'en'},
         boards=['reg', 'compliance'], themes=['compliance', 'distribution', 'channel', 'reg', 'consumer'],
         tags=tg('韩国FSS', '不当销售', '电视购物', '继续率', '高龄客户', '广告审查'),
         originalUrl='https://www.insurancebusinessmag.com/asia/news/breaking-news/south-korea-flags-misselling-gap-in-broadcast-insurance-sales-592125.aspx'),

    # ============ 3. 韩华生命收购 Acuon Capital：资本与监管视角 ============
    item(id='ibm-hanwha-life-acuon-capital-20261002', score=63, verifyStatus='verified',
         sourceTier='media', sourceKey='insurancebusinessmag', contentKind='news',
         publishedAt='2026-10-02T23:34:00+08:00',
         title=T('韩华生命董事会9月30日批准以4,400亿韩元收购 Acuon Capital 50.54%控股权（卖方为EQT Partners，Centroid Investment 作财务投资人）：Acuon Capital 2026上半年资产约4.6万亿韩元、全资持有 Acuon 储蓄银行（约5.1万亿韩元），拟与韩华储蓄银行合并成约6.5万亿韩元储蓄银行；韩国存款保险公司（KDIC）持有韩华生命10%股权且债券偿还基金2027年底到期，收购推高RWA并压缩K-ICS偿付能力比率 [EN原文]',
                 '韓華生命董事會9月30日批准以4,400億韓元收購 Acuon Capital 50.54%控股權（賣方爲EQT Partners，Centroid Investment 作財務投資人）：Acuon Capital 2026上半年資產約4.6萬億韓元、全資持有 Acuon 儲蓄銀行（約5.1萬億韓元），擬與韓華儲蓄銀行合併成約6.5萬億韓元儲蓄銀行；韓國存款保險公司（KDIC）持有韓華生命10%股權且債券償還基金2027年底到期，收購推高RWA並壓縮K-ICS償付能力比率 [EN原文]'),
         summary=T('Insurance Business Asia 10月2日23:34（香港时间）报道：韩华生命董事会9月30日批准以4,400亿韩元收购韩国信贷金融机构 Acuon Capital 50.54%控股权，卖方为私募股权公司 EQT Partners，Centroid Investment Partners 作为财务投资人参与，交易尚待监管批准、未公布完成日期。Acuon Capital 2026上半年资产约4.6万亿韩元，并全资持有 Acuon 储蓄银行（同期约5.1万亿韩元资产）；韩华生命拟把该行与旗下韩华储蓄银行合并，形成合计约6.5万亿韩元资产的储蓄银行，把吸存与放贷风险引入以长期保险负债与投资组合为核心的集团。同期韩华生命另对韩华投资证券增资2,500亿韩元（同系资产管理公司另出资2,500亿韩元，合计5,000亿韩元），并考虑最多4,000亿韩元混合资本证券；另据韩国时报，其亦入标竞购 KDB 生命保险。文中特别指出韩国存款保险公司（KDIC）持有韩华生命10%股权（源自1999至2001年对原大韩生命3.55万亿韩元公共资金注资），债券偿还基金2027年底到期，目标售价每股5,000韩元而当时股价约4,845韩元；收购推高风险加权资产、压缩 K-ICS 偿付能力比率，直接构成 KDIC 的股价压力。AM Best 2026年7月报告指若子公司或母公司资产负债表转弱可能触发负面评级行动。', None),
         why=T('这条的价值不在并购本身，而在它把「保险集团多线资本消耗」的传导链讲清楚了：母公司同时承担收购、证券增资、混合资本发行与竞购同业，任何一头超支都会压缩 K-ICS 偿付能力比率，而评级机构与持有10%股权的公共资金方都在盯同一张资产负债表。对以保险集团作交易对手或渠道伙伴的团队，这是判断「集团资本纪律」的观察样本：集团资本分配优先级变化，会先影响子公司的渠道支持、共同销售安排与产品供给节奏，而非等到评级动作。', None),
         actions={'front': T('不评论个别集团资本状况；客户问及保司实力时只引述公开评级报告与监管披露'),
                  'midback': T('把主要合作集团的多线资本动作纳入对手方观察清单，关注偿付能力披露变化'),
                  'lead': T('评估集团层面的资本优先级调整对子公司渠道政策与产品供给的传导'),
                  'cross': T('跨市场集团架构下，须确认签约主体与承担偿付责任的主体是否一致')},
         rolesImpact={'front': 1, 'midback': 3, 'lead': 2, 'cross': 2},
         source={'sc': 'Insurance Business Asia 2026-10-02 23:34（香港时间，综合首尔经济日报／AM Best）[EN原文]',
                 'tc': 'Insurance Business Asia 2026-10-02 23:34（香港時間，綜合首爾經濟日報／AM Best）[EN原文]', 'lang': 'en'},
         boards=['insurer', 'market'], themes=['ma', 'capital', 'solvency', 'market', 'korea'],
         tags=tg('韩华生命', 'Acuon Capital', 'K-ICS', 'KDIC', '并购', '集团资本'),
         originalUrl='https://www.insurancebusinessmag.com/asia/news/life-insurance/regulators-close-in-on-hanwha-lifes-acuon-deal-as-capital-questions-stack-up-592146.aspx'),

    # ============ 4. 印度延长出口风险保障至2027年3月 ============
    item(id='ibm-india-export-risk-relief-extension-20261002', score=62, verifyStatus='verified',
         sourceTier='media', sourceKey='insurancebusinessmag', contentKind='news',
         publishedAt='2026-10-02T21:59:00+08:00',
         title=T('印度把政府支持的西亚洲出口保险计划 RELIEF 延长至2027年3月31日：第二部分为符合条件的新出运提供最高95%信用风险保障（高于ECGC标准80%–90%），超出部分保费由政府承担；第三部分面向危机期间无ECGC保单的MSME出口商，报销最多50%额外运费与保险费、每户上限50万卢比；霍尔木兹海峡战争险费率达船体价值的7.5%–10% [EN原文]',
                 '印度把政府支持的西亞洲出口保險計劃 RELIEF 延長至2027年3月31日：第二部分爲符合條件的新出運提供最高95%信用風險保障（高於ECGC標準80%–90%），超出部分保費由政府承擔；第三部分面向危機期間無ECGC保單的MSME出口商，報銷最多50%額外運費與保險費、每戶上限50萬盧比；霍爾木茲海峽戰爭險費率達船體價值的7.5%–10% [EN原文]'),
         summary=T('Insurance Business Asia 10月2日21:59（香港时间）报道：印度把政府支持的西亚洲出口保险计划 RELIEF（Resilience and Logistics Intervention for Export Facilitation）延长至2027年3月31日，由 ECGC Ltd 在出口促进任务下管理。该计划2026年3月19日批准，起因是霍尔木兹海峡冲突升级后运费与战争险保费飙升，覆盖运往阿联酋、沙特、科威特、以色列、卡塔尔、阿曼、巴林、伊拉克、伊朗与也门的货物。第二部分（现延至2027年3月）为符合条件的新出运提供最高95%信用风险保障，高于 ECGC 标准的80%–90%，额外保费由政府承担并直接向 ECGC 补偿超额赔款；第三部分面向危机期间未持有 ECGC 保单的 MSME 出口商，可报销最多50%合格额外运费与保险成本、每户上限50万卢比，占4.97亿卢比总拨款中2.82亿卢比。文中并引 S&P Global 数据指霍尔木兹海峡船舶战争险费率已升至船体价值的7.5%–10%，海湾至中国原油运费约为五年均值18.91美元／公吨的四倍。印度大米出口商联合会已建议成员对海湾目的地由 CIF 改为 FOB 交易（由买方投保主航段），但出口商在买方保险不足时仍有敞口，卖方利益／或有保险因此成为经纪可承接的业务。', None),
         why=T('地缘冲突正在被制度化：政府以财政资金补贴战争险与信用险，等于把原本由商业市场定价的政治风险部分移出价格信号之外，短期内压低出口商可见成本，但风险本身未消失，只是转移到财政与出口商在买方保险失效时的残余敞口。对承保与经纪业务而言，这提示两条实务线索：一是「卖方利益／或有保险」这类补充保障的需求在贸易条款从 CIF 转向 FOB 时会上升；二是同一风险的定价基准（战争险费率、运费倍率）是判断区域风险溢价的可追踪指标。', None),
         actions={'front': T('客户涉中东贸易安排时，提示贸易条款切换（CIF→FOB）会改变投保责任方与敞口归属'),
                  'midback': T('把战争险费率与运费倍率作为区域风险溢价指标，定期更新承保与条款审查参考'),
                  'lead': T('关注「买方保险不足时的卖方敞口」这类补充保障需求，纳入特种险能力建设方向'),
                  'cross': T('涉及受制裁或高风险航段的项目，须先确认可承保性与合规限制，再谈保障安排')},
         rolesImpact={'front': 1, 'midback': 2, 'lead': 2, 'cross': 3},
         source={'sc': 'Insurance Business Asia 2026-10-02 21:59（香港时间，综合 ECGC／S&P Global／Al Jazeera）[EN原文]',
                 'tc': 'Insurance Business Asia 2026-10-02 21:59（香港時間，綜合 ECGC／S&P Global／Al Jazeera）[EN原文]', 'lang': 'en'},
         boards=['market', 'product'], themes=['marine', 'geopolitics', 'market', 'trade', 'capital'],
         tags=tg('印度RELIEF', '出口信用险', '霍尔木兹', '战争险费率', 'MSME', 'FOB条款'),
         originalUrl='https://www.insurancebusinessmag.com/asia/news/breaking-news/india-extends-export-risk-relief-to-march-2027-as-gulf-warrisk-costs-stay-high-592114.aspx'),

    # ============ 5. 安联马来西亚设纳闽子公司服务高净值 ============
    item(id='iaasia-allianz-malaysia-labuan-hnw-20261002', score=66, verifyStatus='verified',
         sourceTier='media', sourceKey='insuranceasia', contentKind='news',
         publishedAt='2026-10-02T06:15:00+08:00',
         title=T('安联马来西亚于10月1日在纳闽（Labuan）完成全资子公司 Allianz Labuan 注册：面向马来西亚高净值客户提供外币计价寿险方案；安联亚太2026上半年经营利润升11.4%至5.291亿美元 [EN原文]',
                 '安聯馬來西亞於10月1日在納閩（Labuan）完成全資子公司 Allianz Labuan 註冊：面向馬來西亞高淨值客戶提供外幣計價壽險方案；安聯亞太2026上半年經營利潤升11.4%至5.291億美元 [EN原文]'),
         summary=T('Insurance Asia 10月2日06:15（香港时间）报道：安联马来西亚（Allianz Malaysia Berhad）自2026年10月1日起在马来西亚联邦直辖区纳闽（Labuan）设立全资子公司 Allianz Labuan，为马来西亚高净值客户群提供寿险方案，并在纳闽提供外币计价产品。安联马来西亚表示，此次设立扩大其业务版图并巩固其在区域寿险业的地位。报道并附背景：安联亚太2026年上半年经营利润同比升11.4%至5.291亿美元。', None),
         why=T('纳闽是亚洲少数同时具备低税制、外币计价与离岸保险牌照属性的司法管辖区，此前区内已有米勒（Miller）等机构在纳闽设立平台承接亚太再保与自保需求。安联以本地大型保险公司身份直接在纳闽设高净值专属实体，说明区内「高净值＋外币资产」的分层供给正在从香港、新加坡向纳闽等次级枢纽扩散。对以香港为基地服务的团队，这是竞争格局而非产品信息：同一批寻求外币计价与财富传承架构的东南亚客户，会多一个合规可选项，客户比较的维度将从产品条款扩展到司法管辖区与税务处理。', None),
         actions={'front': T('客户问及东南亚配置选项时，只说明存在不同司法管辖区的合规安排，不比较税负高低'),
                  'midback': T('把纳闽等地纳入区域牌照与外汇／税务规则观察清单，注意外币计价产品的准入差异'),
                  'lead': T('评估东南亚高净值客户分层供给变化对香港渠道定位的长期影响'),
                  'cross': T('客户涉跨境架构时，须按客户自身税务居民身份确认持有与申报义务')},
         rolesImpact={'front': 2, 'midback': 2, 'lead': 3, 'cross': 2},
         source={'sc': 'Insurance Asia 2026-10-02 06:15（香港时间）[EN原文]',
                 'tc': 'Insurance Asia 2026-10-02 06:15（香港時間）[EN原文]', 'lang': 'en'},
         boards=['market', 'family'], themes=['hnw', 'offshore', 'market', 'distribution', 'labuan'],
         tags=tg('安联马来西亚', '纳闽', 'Allianz Labuan', '高净值', '外币保单', '离岸保险'),
         originalUrl='https://insuranceasia.com/insurance/news/allianz-malaysia-launches-labuan-unit-wealthy-clients'),

    # ============ 6. 标普评述 CPIC 香港资本状况 ============
    item(id='iaasia-cpic-hk-capital-sp-review-20261002', score=68, verifyStatus='verified',
         sourceTier='media', sourceKey='insuranceasia', contentKind='news',
         publishedAt='2026-10-02T05:30:00+08:00',
         title=T('标普（S&P）9月30日评级评论：预期中国太平洋保险（香港）未来两年资本与盈利稳健，母公司7月注资15亿港元有助其过渡至风险为本资本制度；其高风险资产敞口已由2023年的100%降至2025年底仅占调整后资本39%，固定收益配置持续转向投资级；但资本基础较小，对单一巨灾事件较敏感 [EN原文]',
                 '標普（S&P）9月30日評級評論：預期中國太平洋保險（香港）未來兩年資本與盈利穩健，母公司7月注資15億港元有助其過渡至風險爲本資本制度；其高風險資產敞口已由2023年的100%降至2025年底僅佔調整後資本39%，固定收益配置持續轉向投資級；但資本基礎較小，對單一巨災事件較敏感 [EN原文]'),
         summary=T('Insurance Asia 10月2日05:30（香港时间）报道：标普全球评级（S&P Global Ratings）于2026年9月30日发表评级评论，预期中国太平洋保险（香港）有限公司（CPIC Hong Kong）未来两年维持较强资本与盈利，并认为其在集团（中国太平洋财产保险股份有限公司 CPPIC）内持续具战略重要性，母公司会在需要时提供资本支持。标普指出，母公司7月向 CPIC 香港注资15亿港元，将便利其过渡至风险为本资本制度并支持业务扩张。资产质量方面，CPIC 香港持续削减高风险资产，敞口由2023年的100%降至2025年底仅为调整后资本的39%，固定收益配置继续转向投资级；标普认为这有助其在未来12个月业务增长加快的情况下满足流动性需要，尤其理赔支付。同时标普提示其资本基础规模不大，或使其相对假设更易受冲击，或暴露于单一大额事件风险；并预期公司会加强承保纪律、与母集团对保险利润的重视保持一致，以管理持续增加的海外敞口所带来的巨灾类承保波动。', None),
         why=T('这是可核对的公开评级视角，把「资本充足」与「资本规模」两个常被混为一谈的维度拆开：CPIC 香港属于资本比率达标但绝对规模有限的一类，标普据此点出单一巨灾事件的风险敏感性。对香港市场的意义在于，风险为本资本制度（RBC）落地后，评级机构与监管同时以调整后资本口径审视高风险资产与巨灾敞口，资产端由非投资级转向投资级的动作会被计为资本效率改善。判断一家公司抗风险能力时，比偿付能力比率数字更值得看的是资产质量趋势与集团注资的持续性。', None),
         actions={'front': T('客户问及保司实力时，只引述公开评级评论与监管披露，不转述为推荐理由'),
                  'midback': T('把评级评论作为对手方财务观察的补充来源，关注注资与资产质量趋势而非单一比率'),
                  'lead': T('区分「资本充足率达标」与「资本绝对规模与业务扩张匹配度」，用于内部对手方评估'),
                  'cross': T('集团支持承诺与法律上的资本义务不同，跨境项目须以签约主体为评估对象')},
         rolesImpact={'front': 1, 'midback': 3, 'lead': 2, 'cross': 2},
         source={'sc': 'Insurance Asia 2026-10-02 05:30（香港时间，引 S&P Global Ratings 2026-09-30 评级评论）[EN原文]',
                 'tc': 'Insurance Asia 2026-10-02 05:30（香港時間，引 S&P Global Ratings 2026-09-30 評級評論）[EN原文]', 'lang': 'en'},
         boards=['insurer', 'reg'], themes=['capital', 'solvency', 'rbc', 'rating', 'market'],
         tags=tg('太保香港', '标普评级', '风险为本资本', '母公司注资', '高风险资产', '巨灾敞口'),
         originalUrl='https://insuranceasia.com/news/cpic-hong-kong-capital-strengthens-high-risk-assets-fall-39'),

    # ============ 7. 威利斯临时分保报告：临分从「难险工具」转为增长工具 ============
    item(id='iaasia-willis-fac-reinsurance-report-2026-20261002', score=68, verifyStatus='verified',
         sourceTier='pro', sourceKey='insuranceasia', contentKind='news',
         publishedAt='2026-10-02T05:00:00+08:00',
         title=T('威利斯（WTW）《2026临时再保险报告》：380名全球保险高管中52%以资本管理为主要购买动因（2024年为44%），60%预计未来两年增加临分使用（仅13%计划减少）；56%视全球扩张为最大机会（此前39%），57%担忧地缘政治、54%担忧网络风险（此前24%）、40%担忧气候风险 [EN原文]',
                 '威利斯（WTW）《2026臨時再保險報告》：380名全球保險高管中52%以資本管理爲主要購買動因（2024年爲44%），60%預計未來兩年增加臨分使用（僅13%計劃減少）；56%視全球擴張爲最大機會（此前39%），57%擔憂地緣政治、54%擔憂網絡風險（此前24%）、40%擔憂氣候風險 [EN原文]'),
         summary=T('Insurance Asia 10月2日05:00（香港时间）报道：威利斯（Willis，WTW 旗下）与 Coleman Parkes Research 的《2026临时再保险报告》调查了北美、欧洲、中东、亚太与拉丁美洲380名保险业高管。52%受访者以资本管理为主要购买临时再保险（facultative reinsurance）的动因，高于2024年的44%；56%视全球扩张为未来两年最大机会（此前39%）；52%把进入新市场与新风险领域列为首要战略目标（此前45%）；55%以提升承保能力为优先（此前48%）。60%预计未来两年增加临分使用，仅13%计划减少；82%认为临分是管理风险、能力、资本与风险偏好的重要一环，仅22%视其为最后手段（2024年为28%）。新兴风险担忧显著上升：地缘政治57%（此前52%）、网络风险54%（此前24%）、气候风险40%（此前30%）。威利斯全球直接与临分业务主管 Garret Gaughan 表示，临分日益用于扩张能力、进入新市场与管理资本，并在不确定环境中提供弹性。', None),
         why=T('临分的使用动机从「兜住难承保风险」转为「支持扩张与管理资本」，说明在市场转软、capacity 充裕的环境里，再保不再只是风控工具，而是承保能力的调节阀。这对产品与承保策略的含义是双向的：一方面险企可用临分快速试水新市场与新险种，产品上市门槛因此下降；另一方面网络风险担忧一年内由24%跃升至54%，意味着这一风险的定价与条款仍在快速重估期，前期承接的敞口可能被再保市场重新定价。', None),
         actions={'front': T('不以临分安排推断产品稳定性；客户问及保司承保能力时只作原则性说明'),
                  'midback': T('把再保市场动机转变纳入承保能力与条款稳定性观察，网络风险须单列关注'),
                  'lead': T('关注网络与地缘政治风险的再保定价重估对相关险种供给节奏的影响'),
                  'cross': T('新市场扩张常伴随属地监管差异，须确认再保安排的属地合规性')},
         rolesImpact={'front': 1, 'midback': 2, 'lead': 3, 'cross': 2},
         source={'sc': 'Insurance Asia 2026-10-02 05:00（香港时间，引 WTW／Coleman Parkes《Facultative Reinsurance Report 2026》）[EN原文]',
                 'tc': 'Insurance Asia 2026-10-02 05:00（香港時間，引 WTW／Coleman Parkes《Facultative Reinsurance Report 2026》）[EN原文]', 'lang': 'en'},
         boards=['market', 'product'], themes=['reinsurance', 'capital', 'cyber', 'market', 'growth'],
         tags=tg('临时再保险', '威利斯', 'WTW', '资本管理', '网络风险', '全球扩张'),
         originalUrl='https://insuranceasia.com/insurance/in-focus/insurers-boost-facultative-reinsurance-use-growth'),

    # ============ 8. Hannover Re Capital Partners 设百慕达基金与 SPI ============
    item(id='artemis-hannover-re-bermuda-fund-spi-20261002', score=70, verifyStatus='verified',
         sourceTier='pro', sourceKey='artemis', contentKind='news',
         publishedAt='2026-10-02T16:00:00+08:00',
         title=T('Artemis：Hannover Re 旗下 ILS 平台 Hannover Re Capital Partners（HCP）在百慕达注册 Hannover Re Capital Partners Fund Ltd.（混合投资基金结构）与 Hannover Re Capital Partners SPI Ltd.（特殊目的保险人，作风险转换器），以扩大可管理并供客户投资的 ILS 机会范围；市场消息指目前部署的投资者资本仍在「数亿美元以内」 [EN原文]',
                 'Artemis：Hannover Re 旗下 ILS 平台 Hannover Re Capital Partners（HCP）在百慕達註冊 Hannover Re Capital Partners Fund Ltd.（混合投資基金結構）與 Hannover Re Capital Partners SPI Ltd.（特殊目的保險人，作風險轉換器），以擴大可管理並供客戶投資的 ILS 機會範圍；市場消息指目前部署的投資者資本仍在「數億美元以內」 [EN原文]'),
         summary=T('Artemis 10月2日16:00（香港时间）报道：再保险集团 Hannover Re 在百慕达设立的保险相连证券（ILS）平台 Hannover Re Capital Partners（HCP，2026年初成立，已于2026年1月1日再保续期开始承保业务）近日注册两家新公司结构，以扩大其管理与提供的 ILS 投资机会范围：一为 Hannover Re Capital Partners Fund Ltd.，属混合投资基金结构；一为 Hannover Re Capital Partners SPI Ltd.，属特殊目的保险人（SPI），将作为风险转换器，为 HCP 策略承接风险以供配置资本与投资，并可能与新基金结构相配合。报道指 HCP 正持续在百慕达构建基础设施并加强团队，目前尚无投资者资本部署规模的明确数字，消息指处于「数亿美元以内」水平；新基金与 SPI 注册完成后，其有望在2027年募集新资本并增加可配置规模。', None),
         why=T('这是 ILS 供给侧的基础设施建设，对香港正在推进的保险相连证券与专属自保生态有直接参照价值：要吸引资本进入保险风险，关键不只是发行端，而是基金载体、SPI 风险转换器与团队三项基础设施是否齐备。HCP 先建结构再谈规模、并明确指向2027年募资，说明 ILS 平台的成熟周期以年计，与监管批准节奏不完全同步。对关注香港风险管理中心定位的团队，可将其作为「ILS 生态需要哪些制度组件」的具象案例。', None),
         actions={'front': T('ILS 属机构级风险转移工具，不对零售客户作任何投资或收益表述'),
                  'midback': T('关注 ILS 载体与 SPI 结构在百慕达、香港的制度差异，作为区域市场观察素材'),
                  'lead': T('把 ILS 基础设施建设节奏纳入香港风险管理中心定位的长期跟踪'),
                  'cross': T('涉跨境风险载体的安排须先确认监管认可范围与投资者适当性要求')},
         rolesImpact={'front': 0, 'midback': 2, 'lead': 2, 'cross': 2},
         source={'sc': 'Artemis 2026-10-02 16:00（香港时间）[EN原文]',
                 'tc': 'Artemis 2026-10-02 16:00（香港時間）[EN原文]', 'lang': 'en'},
         boards=['market', 'reg'], themes=['ils', 'catbond', 'capital', 'bermuda', 'risk-hub'],
         tags=tg('ILS', 'Hannover Re', '百慕达', 'SPI', '保险相连证券', '风险转换器'),
         originalUrl='https://www.artemis.bm/news/hannover-re-capital-partners-establishes-new-bermuda-fund-structure-and-spi/'),

    # ============ 9. 威利斯：北美商业地产费率十年最大跌幅 ============
    item(id='artemis-willis-na-property-rates-decade-drop-20261002', score=70, verifyStatus='verified',
         sourceTier='pro', sourceKey='artemis', contentKind='news',
         publishedAt='2026-10-02T15:00:00+08:00',
         title=T('Artemis 引威利斯《Insurance Marketplace Realities》：北美商业财产险费率录得十年最大跌幅，大型复杂财产项目2026年二季度平均降14.5%（去年同期8.4%），分层共保安排降23.41%（去年同期14.57%）；威利斯预计未来单家承保方案再降5%–15%、分层共保降15%–25%，并指多年硬市场「完全逆转」，除非出现1500亿美元以上巨灾事件 [EN原文]',
                 'Artemis 引威利斯《Insurance Marketplace Realities》：北美商業財產險費率錄得十年最大跌幅，大型複雜財產項目2026年二季度平均降14.5%（去年同期8.4%），分層共保安排降23.41%（去年同期14.57%）；威利斯預計未來單家承保方案再降5%–15%、分層共保降15%–25%，並指多年硬市場「完全逆轉」，除非出現1500億美元以上巨災事件 [EN原文]'),
         summary=T('Artemis 10月2日15:00（香港时间）报道：威利斯（Willis，WTW 旗下）《Insurance Marketplace Realities》报告显示，北美商业财产险市场费率录得十年来最大跌幅，大型复杂财产保险项目2026年二季度费率平均下降14.5%（2025年同期为下降8.4%），分层与共保安排降幅更大、达23.41%（2025年同期为下降14.57%）。报告指市场已从2018年至2024年的硬市场转向接近2019年的价格水平，2026年各续期日的合约再保软化是主因——再保市场的充裕能力与资本水平向下传导，强化了原保险市场供给。威利斯预计未来单家承保财产项目费率再降5%–15%、分层共保安排再降15%–25%，并指险企越来越愿意在条款、条件、免赔额与措辞上让步。报告同时提示重置成本正再度加速上升（受美国关税政策与中东局势推动），准确更新估值因此更为关键；加拿大市场费率下降5%–20%，百慕达非巨灾财产费率预计下降15%–30%、巨灾敞口项目降10%–20%。威利斯认为，除非出现1500亿美元以上的巨灾事件，此趋势预计将持续至年底。', None),
         why=T('这是全球财产险定价周期反转的一手证据，且给出了可量化的传导链：再保能力充裕→合约再保软化→原保险供给过剩→费率与条款同时松动。对香港与亚洲市场的参照意义在于，转软周期通常伴随承保纪律松动（降低起赔点、放宽措辞），而报告同时指重置成本因关税与地缘因素加速上升——即费率下降与风险成本上升同时发生，这是最考验承保纪律的组合。区域再保续期与本地条款谈判将逐步感受到这一压力。', None),
         actions={'front': T('财产险转软不等于保障应缩水；客户问及费率时以核保结论为准，不作费率预期承诺'),
                  'midback': T('关注条款与免赔额松动带来的保障缺口变化，续保时重新核对估值与保额'),
                  'lead': T('把全球财产险周期与重置成本走向并列观察，用于承保纪律与业务组合判断'),
                  'cross': T('跨境财产风险须按属地承保能力与巨灾暴露单独评估，不套用北美费率趋势')},
         rolesImpact={'front': 2, 'midback': 2, 'lead': 3, 'cross': 2},
         source={'sc': 'Artemis 2026-10-02 15:00（香港时间，引 Willis《Insurance Marketplace Realities》）[EN原文]',
                 'tc': 'Artemis 2026-10-02 15:00（香港時間，引 Willis《Insurance Marketplace Realities》）[EN原文]', 'lang': 'en'},
         boards=['market', 'product'], themes=['pricing', 'property', 'reinsurance', 'market', 'cat'],
         tags=tg('财产险费率', '软市场', '威利斯', '合约再保', '重置成本', '巨灾'),
         originalUrl='https://www.artemis.bm/news/na-commercial-property-insurance-rates-fall-the-most-in-a-decade-hard-market-reverses-willis/'),

    # ============ 10. Aon：泰国水灾经济损失或达10亿美元 ============
    item(id='ian-aon-thailand-floods-1bn-loss-20261002', score=65, verifyStatus='pending',
         sourceTier='media', sourceKey='insuranceasianews', contentKind='news',
         publishedAt='2026-10-02T18:11:00+08:00',
         title=T('Aon 自然巨灾报告：泰国水灾经济损失或高达10亿美元，投保损失初步估算仍未公布、但预计显著低于经济总损失 [EN原文]',
                 'Aon 自然巨災報告：泰國水災經濟損失或高達10億美元，投保損失初步估算仍未公佈、但預計顯著低於經濟總損失 [EN原文]'),
         summary=T('InsuranceAsia News 10月2日18:11（香港时间）报道：怡安（Aon）自然巨灾报告指出，泰国水灾造成的经济损失可能高达10亿美元。报道引述该报告称，初步投保损失估算仍未可得，但预计会显著低于经济总损失。该报道属 Flooding 主题连续跟踪的一环，此前该网已于9月27日（曼谷宣布水灾灾难）与10月1日（泰国水灾与台风「杜苏芮」考验亚洲水险与营业中断保障）分别报道同一事件。经济损失与投保损失之间的差额，是衡量保障缺口的直接口径。', None),
         why=T('对亚洲市场最实用的读法不是损失金额，而是「经济损失10亿美元 vs 投保损失显著更低」这一差额——它再次量化了亚太地区的保障缺口。结合该网此前的承保人视角报道（极端降雨成为车险、财产险与营业中断险的主要损失驱动），这类事件对本地财产险定价与条款的影响通常滞后一个续期周期才体现，但对客户的风险认知是即时的：企业客户需要区分「有保险」与「保额是否匹配重置成本」两件事。', None),
         actions={'front': T('客户问及自然灾害影响时，提示检查保额与重置成本匹配度，不作赔付承诺'),
                  'midback': T('把亚太洪水保障缺口数据用于客户保额充足性沟通素材，注意引用来源与日期'),
                  'lead': T('将巨灾损失口径（经济损失／投保损失）纳入区域市场观察的固定指标'),
                  'cross': T('涉泰国产能与供应链的客户，须评估营业中断保障的实际覆盖范围')},
         rolesImpact={'front': 2, 'midback': 1, 'lead': 1, 'cross': 2},
         source={'sc': 'InsuranceAsia News 2026-10-02 18:11（香港时间，引 Aon 自然巨灾报告）[EN原文]',
                 'tc': 'InsuranceAsia News 2026-10-02 18:11（香港時間，引 Aon 自然巨災報告）[EN原文]', 'lang': 'en'},
         boards=['market', 'product'], themes=['cat', 'flood', 'gap', 'market', 'claims'],
         tags=tg('泰国水灾', '怡安Aon', '经济损失', '投保损失', '保障缺口', '巨灾'),
         originalUrl='https://insuranceasianews.com/economic-losses-from-thailand-floods-could-reach-up-to-us1bn-aon/'),

    # ============ 11. Gallagher 收购新西兰经纪 Albany ============
    item(id='ian-gallagher-albany-nz-acquisition-20261002', score=64, verifyStatus='pending',
         sourceTier='media', sourceKey='insuranceasianews', contentKind='news',
         publishedAt='2026-10-02T15:50:00+08:00',
         title=T('Gallagher 达成协议收购新西兰零售保险经纪 Albany Insurance Services：标的服务奥克兰与坎特伯雷地区商业险与个人险客户 [EN原文]',
                 'Gallagher 達成協議收購新西蘭零售保險經紀 Albany Insurance Services：標的服務奧克蘭與坎特伯雷地區商業險與個人險客戶 [EN原文]'),
         summary=T('InsuranceAsia News 10月2日15:50（香港时间）报道：全球保险经纪 Gallagher 达成协议，收购新西兰专业零售保险经纪 Albany Insurance Services。报道指 Albany 为专业零售保险经纪，服务新西兰奥克兰（Auckland）与坎特伯雷（Canterbury）地区的商业险与个人险客户。该收购属 Gallagher 持续的区域经纪网络整合动作，与同期 Marsh 完成日本 Eneos 内部保险中介业务收购、Aon 加强日本全球解决方案团队等动作同期出现。', None),
         why=T('经纪行业整合在同一周内出现多起（Gallagher 收购新西兰零售经纪、Marsh 完成日本能源企业内部中介收购、Aon 强化日本跨国企业团队），方向一致：全球经纪集团以并购获取本地客户与渠道，同时把人力集中在跨国企业与高价值客户。对本港中介生态的含义是长期的：独立经纪在不同市场面对的对手规模持续变大，差异化只能来自本地服务深度与专业细分，而非价格。', None),
         actions={'front': T('不评论同业并购；客户问及经纪行业变化时，只陈述公开披露的交易事实'),
                  'midback': T('把区域经纪整合动态纳入竞争情报，关注其本地团队与客户服务连续性'),
                  'lead': T('关注经纪整合对本地顾问人才流动与招募市场的影响'),
                  'cross': T('跨境业务合作须确认合并后签约主体与责任承担主体')},
         rolesImpact={'front': 0, 'midback': 2, 'lead': 3, 'cross': 1},
         source={'sc': 'InsuranceAsia News 2026-10-02 15:50（香港时间）[EN原文]',
                 'tc': 'InsuranceAsia News 2026-10-02 15:50（香港時間）[EN原文]', 'lang': 'en'},
         boards=['market', 'insurer'], themes=['broker', 'ma', 'distribution', 'market', 'apac'],
         tags=tg('Gallagher', 'Albany Insurance', '新西兰', '保险经纪', '并购', '零售经纪'),
         originalUrl='https://insuranceasianews.com/gallagher-strikes-deal-to-acquire-kiwi-broker-albany-insurance-services/'),

    # ============ 12. Axa XL 升任 Thomas Gotting ============
    item(id='ian-axa-xl-gotting-apac-europe-distribution-20261002', score=63, verifyStatus='pending',
         sourceTier='media', sourceKey='insuranceasianews', contentKind='news',
         publishedAt='2026-10-02T15:55:00+08:00',
         title=T('Axa XL 升任 Thomas Gotting 为亚太及欧洲客户与分销总监（Chief Client, Distribution Officer）：常驻科隆，统管欧洲、亚洲与澳洲的客户及分销策略 [EN原文]',
                 'Axa XL 升任 Thomas Gotting 爲亞太及歐洲客戶與分銷總監（Chief Client, Distribution Officer）：常駐科隆，統管歐洲、亞洲與澳洲的客戶及分銷策略 [EN原文]'),
         summary=T('InsuranceAsia News 10月2日15:55（香港时间）报道：Axa XL 升任 Thomas Gotting 为亚太及欧洲首席客户与分销官（Chief Client, Distribution Officer）。报道指 Gotting 常驻德国科隆，将领导 Axa XL 在欧洲、亚洲与澳洲的客户与分销策略。该任命属 Axa XL 在跨区客户与分销管理上的架构调整。', None),
         why=T('把亚太与欧洲的客户与分销职能合并到同一负责人，通常指向两个目的：一是跨国经纪集团与跨国企业客户的管理口径统一，二是分销资源的跨区调配更灵活。对区域渠道合作方而言，这类架构调整意味着对接层级上移、谈判口径可能统一化，本地灵活度短期反而可能下降。值得与同期 Axa XL 在 AI 治理等议题上的公开表态一并观察其亚太策略走向。', None),
         actions={'front': T('不评论个别公司人事安排；涉及合作对手方变更时以官方公告为准'),
                  'midback': T('更新主要再保／专业险对手方的联络与授权层级档案'),
                  'lead': T('留意跨区分销架构调整对本地合作条款与响应速度的影响'),
                  'cross': T('跨区分销口径统一后，本地特殊安排须重新确认授权范围')},
         rolesImpact={'front': 0, 'midback': 2, 'lead': 2, 'cross': 1},
         source={'sc': 'InsuranceAsia News 2026-10-02 15:55（香港时间）[EN原文]',
                 'tc': 'InsuranceAsia News 2026-10-02 15:55（香港時間）[EN原文]', 'lang': 'en'},
         boards=['insurer', 'market'], themes=['people', 'distribution', 'leadership', 'apac', 'specialty'],
         tags=tg('Axa XL', 'Thomas Gotting', '分销策略', '人事任命', '亚太', '专业险'),
         originalUrl='https://insuranceasianews.com/axa-xl-elevates-thomas-gotting-to-chief-client-distribution-officer-for-apac-and-europe/'),

    # ============ 13. 澳洲再保险池拟上调气旋池保费2.9% ============
    item(id='ian-arpa-cyclone-pool-premium-rise-20261002', score=63, verifyStatus='pending',
         sourceTier='media', sourceKey='insuranceasianews', contentKind='news',
         publishedAt='2026-10-02T08:30:00+08:00',
         title=T('澳洲再保险池公司（ARPC）就2026年定价检讨草案建议上调气旋池保费2.9%：长期保费充足度将由95.1%提升至97.9% [EN原文]',
                 '澳洲再保險池公司（ARPC）就2026年定價檢討草案建議上調氣旋池保費2.9%：長期保費充足度將由95.1%提升至97.9% [EN原文]'),
         summary=T('InsuranceAsia News 10月2日08:30（香港时间）报道：澳大利亚再保险池公司（Australian Reinsurance Pool Corporation, ARPC）提出将气旋池（cyclone pool）保费上调2.9%。报道引述其2026年定价检讨草案称，此次上调可把长期保费充足度由95.1%提升至97.9%。该机构为澳大利亚政府设立的巨灾风险池营运方，负责将气旋与相关洪水风险透过再保机制转移至全球市场。', None),
         why=T('公共巨灾风险池的定价检讨提供了一个可对照的监管技术样本：以「长期保费充足度」这一会计口径驱动费率调整，而非按当年损益。香港正推进保单持有人保障计划与巨灾风险相关制度建设，ARPC 的做法说明风险池要对长期充足度负责，费率上调往往与市场周期无关——即便全球财产险刚录得十年最大跌幅，公共池仍按自身模型调价。这一点有助于理解「商业市场转软」与「公共风险池定价」是两个独立轨道。', None),
         actions={'front': T('不对客户比较各地巨灾风险池安排；只说明公共保障机制与商业保险的分工'),
                  'midback': T('把区域巨灾风险池的定价与充足度机制纳入监管制度比较素材'),
                  'lead': T('关注公共风险池与商业市场周期脱钩这一特征，用于内部风险定价讨论'),
                  'cross': T('客户涉澳洲等属地资产时，须按属地公共保障机制与商业保单分别确认覆盖')},
         rolesImpact={'front': 0, 'midback': 2, 'lead': 2, 'cross': 2},
         source={'sc': 'InsuranceAsia News 2026-10-02 08:30（香港时间）[EN原文]',
                 'tc': 'InsuranceAsia News 2026-10-02 08:30（香港時間）[EN原文]', 'lang': 'en'},
         boards=['market', 'reg'], themes=['cat', 'pricing', 'reinsurance', 'pool', 'australia'],
         tags=tg('ARPC', '气旋池', '巨灾风险池', '保费充足度', '再保险', '澳洲'),
         originalUrl='https://insuranceasianews.com/australian-reinsurance-pool-corporation-proposes-raising-cyclone-pool-premiums-by-2-9/'),

    # ============ 14. Markel：海上战争险需中央解决方案 ============
    item(id='ian-markel-marine-war-risk-central-solution-20261002', score=65, verifyStatus='pending',
         sourceTier='media', sourceKey='insuranceasianews', contentKind='news',
         publishedAt='2026-10-02T07:30:00+08:00',
         title=T('Markel 亚洲理赔主管 Bo Yu：自2月以来霍尔木兹海峡已有98艘船舶遭袭，海上战争险的损失累积暴露理赔缺口，业界需要中央化解决方案以应对航次逐一定价的碎片化安排 [EN原文]',
                 'Markel 亞洲理賠主管 Bo Yu：自2月以來霍爾木茲海峽已有98艘船舶遭襲，海上戰爭險的損失累積暴露理賠缺口，業界需要中央化解決方案以應對航次逐一定價的碎片化安排 [EN原文]'),
         summary=T('InsuranceAsia News 10月2日07:30（香港时间）报道：Markel 亚洲理赔主管 Bo Yu 表示，自2026年2月以来已有98艘船舶在霍尔木兹海峡遭到袭击，累积损失正暴露出海上战争险的理赔缺口，业界需要一个中央化的解决方案。报道指相关挑战源于战争险按航次逐一定价与承保的碎片化结构，损失持续累积后，责任的分配与追踪变得困难。该报道属该网海上战争险系列的延续（此前于9月21日至25日期间已从 IUMI 年会、市场参与者角度报道过海湾战争险理赔与逐航次承保问题）。', None),
         why=T('战争险传统上按航次、按船舶逐笔承保，适合偶发事件；当同一海域在数月内累积近百起船舶袭击时，这种碎片化结构就会出现责任追踪与累积暴露管理的断层。这对区域市场的提示有两层：一是特种险的承保结构需要匹配风险的「相关性」而非「单一事件」假设；二是海事与供应链客户的保障安排，需要同时检视战争险、船体险与营业中断之间的衔接是否留有空隙。', None),
         actions={'front': T('客户涉高风险航段时，提示逐航次战争险与船体险的衔接检查，不作可保性承诺'),
                  'midback': T('对累积型风险的承保结构进行复核，关注碎片化安排下的累积暴露管理'),
                  'lead': T('把海上战争险的结构性缺口纳入特种险能力建设与再保安排讨论'),
                  'cross': T('受制裁与高风险航段的安排须先确认合规可承保性再谈条款')},
         rolesImpact={'front': 1, 'midback': 2, 'lead': 2, 'cross': 3},
         source={'sc': 'InsuranceAsia News 2026-10-02 07:30（香港时间）[EN原文]',
                 'tc': 'InsuranceAsia News 2026-10-02 07:30（香港時間）[EN原文]', 'lang': 'en'},
         boards=['product', 'market'], themes=['marine', 'geopolitics', 'claims', 'accumulation', 'specialty'],
         tags=tg('Markel', '海上战争险', '霍尔木兹海峡', '累积暴露', '船舶袭击', '理赔缺口'),
         originalUrl='https://insuranceasianews.com/marine-war-risk-challenges-require-central-solution-as-mounting-losses-expose-claims-gaps-markel/'),

    # ============ 15. Savills：香港下一代财富枢纽排名全球第七 ============
    item(id='scmp-savills-nextgen-wealth-hubs-hk-7th-20261002', score=60, verifyStatus='pending',
         sourceTier='media', sourceKey='scmp', contentKind='news',
         publishedAt='2026-10-02T15:01:00+08:00',
         title=T('第一太平戴维斯（Savills）「下一代财富枢纽指数」：香港在全球吸引与留住下一代高净值人士的排名为第七，落后第六位的新加坡；报告指香港具备低税、金融成熟、安全与连接性等与新加坡类似的优势，支持其作为亚洲财富保存与家族办公室枢纽的地位 [EN原文]',
                 '第一太平戴維斯（Savills）「下一代財富樞紐指數」：香港在全球吸引與留住下一代高淨值人士的排名爲第七，落後第六位的新加坡；報告指香港具備低稅、金融成熟、安全與連接性等與新加坡類似的優勢，支持其作爲亞洲財富保存與家族辦公室樞紐的地位 [EN原文]'),
         summary=T('《南华早报》10月2日15:01（香港时间）报道：全球房地产顾问第一太平戴维斯（Savills）发表「下一代财富枢纽指数」（Next-Generation Wealth Hubs Index），香港在全球吸引与留住下一代高净值人士（HNWI）的排名为第七，落后于排名第六的传统竞争对手新加坡。报道指亚太两大金融枢纽正加紧巩固其区域财富管理中心地位，背景是前所未有的跨世代全球财富转移。报告认为，香港提供多项与新加坡类似的诱因，包括低税制、金融成熟度、安全与连接性，从而强化其作为亚洲财富保存与家族办公室领先枢纽的地位。报道并指年轻一代财富持有者日益全球化，选址时更重视生活方式、健康与价值观。', None),
         why=T('这类指数常被营销引用，其真正价值在于指出客户决策维度的位移：年轻一代高净值客户把生活方式、健康与价值观与税制、金融成熟度并列比较，意味着家族办公室与传承服务不能再只讲税务与回报。香港与新加坡排名相邻、差距有限，说明两地客源争夺更多取决于「配套体验」而非制度优势本身。这对香港前线与家族办公室服务团队的启示是：服务设计中必须包含非财务维度，否则在客户决策权重里会被边缘化。', None),
         actions={'front': T('客户问及枢纽比较时，只引述公开研究结论与排名口径，不评价优劣、不承诺税务结果'),
                  'midback': T('引用第三方指数须标注机构、指数名称与发布日，避免截取单一排名数字'),
                  'lead': T('把年轻一代决策维度（生活方式／健康／价值观）纳入高客服务与内容设计'),
                  'cross': T('客户涉多地身份与资产时，须按各自税务居民身份分别确认持有与申报安排')},
         rolesImpact={'front': 2, 'midback': 1, 'lead': 2, 'cross': 2},
         source={'sc': 'South China Morning Post 2026-10-02 15:01（香港时间，引 Savills「Next-Generation Wealth Hubs Index」；全文受订阅限制，待复核）[EN原文]',
                 'tc': 'South China Morning Post 2026-10-02 15:01（香港時間，引 Savills「Next-Generation Wealth Hubs Index」；全文受訂閱限制，待覆核）[EN原文]', 'lang': 'en'},
         boards=['family', 'market'], themes=['hnw', 'family-office', 'market', 'competition', 'talent'],
         tags=tg('第一太平戴维斯', '财富枢纽指数', '香港', '新加坡', '家族办公室', '高净值'),
         originalUrl='https://www.scmp.com/business/article/3369536/hong-kong-ranks-7th-globally-drawing-next-wealthy-class-trailing-singapore-study'),
]


def main():
    path = os.path.join(BASE, 'data', 'live-items.json')
    data = json.load(open(path, encoding='utf-8'))
    existing = {it.get('id') for it in data['items']}
    dups = [it['id'] for it in NEW if it['id'] in existing]
    if dups:
        print('跳过已存在 id:', dups)
    urls = {it.get('originalUrl') for it in data['items']}
    new = [it for it in NEW if it['id'] not in existing and it.get('originalUrl') not in urls]
    skipped_url = [it['id'] for it in NEW if it.get('originalUrl') in urls]
    if skipped_url:
        print('跳过重复来源链接:', skipped_url)
    new.sort(key=lambda x: x['publishedAt'], reverse=True)
    data['items'] = new + data['items']
    data['meta']['generatedAt'] = NOW
    data['meta']['itemCount'] = len(data['items'])
    n = len(data['items'])
    data['meta']['windowNote'] = {'sc': f'本库{n}条。', 'tc': f'本庫{n}條。'}
    shutil.copy(path, os.path.join(BASE, 'data/live-items.json.bak-1003-0035'))
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print(f'写入完成: 新增 {len(new)} 条, 合计 {n} 条')
    for it in new:
        print(' +', it['publishedAt'], it['sourceKey'], it['id'])


if __name__ == '__main__':
    main()
