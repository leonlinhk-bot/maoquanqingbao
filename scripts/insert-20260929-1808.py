#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-29 18:08 增量采集（周二工作日晚间时段）。

窗口：2026-09-29 09:30 → 2026-09-29 18:10（周二，香港监管机构与港股工作日）
核验说明：
- IA 官网（Cloudflare challenge）以 web_extract 核验：新闻稿最新 24/9（富卫AML罚款，已入库）；
  通函最新 13/5；演辞窗口内无新增 —— 窗口内无新增。
- HKMA 新闻稿经 web_extract + info.gov.hk RSS 交叉核验：本次取 29/9 半年度报告（16:30）与
  HKICL 伪冒网站警示（17:10），均为当日新增。
- NFRA 官网 JSON 端已下线，26/9 起改经搜索核验；本批取 29/9 金融监管总局与商务部联合《内贸险通知》。
- 富卫 AML 罚款（24/9）已在库（ia-fwd-aml-fine-1950w-20260924），Insurance Asia 29/9 复述报道不重复入库。
- AIA 最新 24/9、宏利香港最新 10/9、永明最新 15/9、AXA 最新 7/9、保诚香港、Insurance Business Asia
  （Atom feed 最新 28/9）—— 窗口内均无新增。
本批 14 条覆盖 hkma / nfra / family_office / scmp / artemis / insuranceasianews。
"""
import json, shutil, os
import zhconv

BASE = '/Users/leonliang/maoquanqingbao'
NOW = '2026-09-29T18:10:00+08:00'

# zh-tw 转换再修正为港式用字（与库内既有 489 处「保險」、41 处「說明」等保持一致）
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
    # ======================= 官方 / 监管 =======================
    item(id='fstb-stamp-duty-group-relief-gazette-20260929', score=80, verifyStatus='verified',
         sourceTier='official', sourceKey='family_office', contentKind='press',
         publishedAt='2026-09-29T17:30:00+08:00',
         title=T('财库局：《2026年印花税（修订）（第3号）条例草案》10月2日刊宪——放宽集团内部资产转让印花税宽免，相联门槛由90%降至75%并计入实益权益与表决权',
                 '財庫局：《2026年印花稅（修訂）（第3號）條例草案》10月2日刊憲——放寬集團內部資產轉讓印花稅寬免，相聯門檻由90%降至75%並計入實益權益與表決權'),
         summary=T('财库局9月29日宣布，《2026年印花税（修订）（第3号）条例草案》将于10月2日刊宪，落实2026至27年度《财政预算案》措施，放宽企业集团内部资产转让的印花税宽免准则。现行《印花税条例》下，相联法人团体之间转让不动产或香港证券可豁免印花税，但须一方持有另一方90%或以上已发行股本。草案将门槛下调至75%，并在已发行股本之外，一并考虑直接或间接实益权益或表决权，令没有发行股本的新型企业（如有限法律责任合伙、担保有限公司）同样可受惠。草案10月14日提交立法会首读，如获通过将适用于今年2月25日或之后签立的文书。',
                 None),
         why=T('这是「家族与企业架构重组」成本直接相关的税制松绑：门槛90%→75%、并承认实益权益与表决权，意味着以合伙或担保公司持股的家族平台在内部划转资产时更易取得宽免。对高客服务而言，这是保单与信托、公司架构之间「持有结构选择」的新变量，也是与客户会计师/律师对话时可引用的官方时点。',
                 None),
         actions={'front': T('客户问「内部转资产几时免印花税」时，答「草案10月2日刊宪、10月14日首读，通过后追溯至2026年2月25日」，不代客判断个案是否适用'),
                  'midback': T('把该草案列入架构重组类客户的跟进清单，与信托/公司服务供货商对齐口径'),
                  'lead': T('讨论传承架构时把「税负」与「控制权」并列，避免只谈税不谈实质控制与受益人安排'),
                  'cross': T('跨境家族平台若涉香港不动产或港股持有，重组时点值得与客户税务顾问一并确认')},
         rolesImpact={'front': 1, 'midback': 1, 'lead': 3, 'cross': 3},
         source={'sc': '香港特区政府新闻公报（财经事务及库务局） 2026-09-29 17:30', 'tc': '香港特區政府新聞公報（財經事務及庫務局） 2026-09-29 17:30', 'lang': 'zh'},
         boards=['reg', 'market'], themes=['reg', 'family-office', 'taxation'],
         tags=tg('印花税', '集团内部资产转让', '家族架构', '实益权益', '条例草案', '财库局'),
         originalUrl='https://www.info.gov.hk/gia/general/202609/29/P2026092900470.htm'),

    item(id='hkma-hkicl-fraudulent-website-20260929', score=85, verifyStatus='verified',
         sourceTier='official', sourceKey='hkma', contentKind='press',
         publishedAt='2026-09-29T17:10:00+08:00',
         title=T('金管局代发警示：香港银行同业结算公司（HKICL）提醒公众慎防伪冒网站 fpshkicl.store，冒充「买家网上安全保障」提供退款、举报未授权交易及交易支援',
                 '金管局代發警示：香港銀行同業結算公司（HKICL）提醒公眾慎防偽冒網站 fpshkicl.store，冒充「買家網上安全保障」提供退款、舉報未授權交易及交易支援'),
         summary=T('金管局9月29日代香港银行同业结算有限公司（结算公司／HKICL）发出警示：结算公司近日发现一个伪冒成其官方网站的诈骗网站 fpshkicl.store，该站伪装为「买家网上安全保障」，声称提供转数快（FPS）网上交易安全服务，包括1）退款、2）举报未经授权的网上交易、3）网上交易支援；链接结尾可能有多重组合（例：fpshkicl.store/?link=...）。结算公司澄清与该伪冒网站绝无关系，并强调一般情况下不会直接向个别公众人士提供转数快服务，也不会主动接触公众。真正官方网址为 www.hkicl.com.hk 及 fps.hkicl.com.hk；如有可疑通讯可致电2533 1111核实，怀疑受骗应报警。',
                 None),
         why=T('这是本港「买家网上保障」骗局的最新一宗，且与9月28日那宗（hkfps.lol）相隔仅一天，显示伪冒网站正快速换域名、同一套路持续复用。对前线与客服而言，这是可以统一向客户发出的具体防骗口径（含伪冒域名与官方域名对照）；对机构而言，频次本身说明客户在网购与转账场景的暴露度仍在上升。',
                 None),
         actions={'front': T('把 fpshkicl.store 列入客户防骗清单，统一话术：HKICL不会主动接触公众，可疑即致电2533 1111核实'),
                  'midback': T('输入客服知识库并与9月28日伪冒网站 hkfps.lol 合并为同一骗局系列跟踪'),
                  'lead': T('只引用官方稿表述，勿把伪冒网站与任何真实支付平台或保险产品挂钩'),
                  'cross': T('跨境网购与汇款客户的诈骗风险教育可与反洗钱/客户尽职调查流程一并提示')},
         rolesImpact={'front': 2, 'midback': 2, 'lead': 1, 'cross': 1},
         source={'sc': '香港金融管理局代香港银行同业结算有限公司发出 2026-09-29 新闻稿（政府新闻公报中文版）', 'tc': '香港金融管理局代香港銀行同業結算有限公司發出 2026-09-29 新聞稿（政府新聞公報中文版）', 'lang': 'zh'},
         boards=['market'], themes=['market', 'fraud'],
         tags=tg('金管局', 'HKICL', '伪冒网站', '转数快', '反诈骗', '客户保障'),
         originalUrl='https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/09/20260929-4/'),

    item(id='hkma-half-yearly-monetary-financial-stability-20260929', score=88, verifyStatus='verified',
         sourceTier='official', sourceKey='hkma', contentKind='press',
         publishedAt='2026-09-29T16:30:00+08:00',
         title=T('金管局刊发2026年9月号《货币与金融稳定情况半年度报告》：详析环球与本港经济、货币金融体系状况，以及银行体系近期表现与风险',
                 '金管局刊發2026年9月號《貨幣與金融穩定情況半年度報告》：詳析環球與本港經濟、貨幣金融體系狀況，以及銀行體系近期表現與風險'),
         summary=T('金管局9月29日刊发2026年9月号《货币与金融稳定情况半年度报告》，详细分析环球与本港经济，以及本港货币与金融体系状况，并阐述本港银行体系近期的表现及所面对的风险。报告全文已于金管局网站供查阅及下载。本稿指半年一度、覆盖宏观环境与金融体系风险的主要官方报告，为下半年本港利率、信贷与资产价格环境提供监管视角的基线判断。',
                 None),
         why=T('这是本港金融体系风险判断的官方基线文件，直接关系保险公司资产端（债券估值、信贷利差、商业地产敞口）与银行渠道的信贷环境。对前线而言，报告口径是回应客户对利率、楼市与银行稳健性疑问的权威参照；对机构而言，是下半年资本与资产配置讨论的起点。',
                 None),
         actions={'front': T('面对客户对利率与楼市提问，引用报告定性判断，不代客预测利率路径'),
                  'midback': T('把报告要点并入下半年资产端与渠道信贷环境跟踪清单'),
                  'lead': T('引用只限报告与金管局稿原文表述，勿自行外推为投资或产品建议'),
                  'cross': T('高客境外配置与银行渠道产品讨论前，先对齐本港金融体系风险评估口径')},
         rolesImpact={'front': 1, 'midback': 2, 'lead': 3, 'cross': 2},
         source={'sc': '香港金融管理局 2026-09-29 新闻稿（政府新闻公报中文版 16:30）', 'tc': '香港金融管理局 2026-09-29 新聞稿（政府新聞公報中文版 16:30）', 'lang': 'zh'},
         boards=['market'], themes=['market', 'macro'],
         tags=tg('金管局', '半年度报告', '货币与金融稳定', '银行体系风险', '利率环境', '资产配置'),
         originalUrl='https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/09/20260929-5/'),

    item(id='nfra-mofcom-domestic-trade-credit-insurance-20260929', score=88, verifyStatus='verified',
         sourceTier='official', sourceKey='nfra', contentKind='press',
         publishedAt='2026-09-29T16:20:00+08:00',
         title=T('金融监管总局与商务部联合印发《关于加强商务和保险协同 做好内贸险有关工作的通知》：九项重点任务推动内贸险扩面增额，支持北京、江苏、福建、湖南、广东、四川及宁波、深圳先行探索',
                 '金融監管總局與商務部聯合印發《關於加強商務和保險協同 做好內貿險有關工作的通知》：九項重點任務推動內貿險擴面增額，支持北京、江蘇、福建、湖南、廣東、四川及寧波、深圳先行探索'),
         summary=T('金融监管总局、商务部9月29日联合印发《关于加强商务和保险协同 做好内贸险有关工作的通知》，共三部分：一是总体要求，凝聚商务系统与保险行业合力，稳妥有序推动国内贸易信用保险（内贸险）发展，支持北京、江苏、福建、湖南、广东、四川及宁波、深圳加大实践探索；二是九项重点任务，包括精准拓展潜在客户、支持新兴和中小主体需求、完善保障能力供给、发挥共保体作用、推动信用数据共享、强化业务风险防控、建立行业协同机制、加强内贸险监管、加大宣传推广；三是加强组织保障。通知要求保险机构充实内贸险专业队伍、健全核保核赔规则、严防利用虚假贸易骗保，并要求强化政策性保险机构与商业保险机构的协同及再保险支持。',
                 None),
         why=T('这是内地贸易信用险在「政策推动＋严监管」双轨上的最新落点：一方面明确八个先行省市与九项任务，等于给出承保资源倾斜的方向图；另一方面把「信息不对称、逆选择与道德风险、虚假贸易骗保」写进文件，意味着核保与理赔追偿能力将成为产能门槛。对关注内地商业险与企业风险的从业者，这是理解信用险扩面节奏的核心文件。',
                 None),
         actions={'front': T('被问内地贸易信用险时，答「政策方向已明确、监管同步收紧，重点看企业征信与贸易背景真实性」'),
                  'midback': T('把九项重点任务转为内地企业客户风险检视清单（信用集中度、交易对手资信、骗保红线）'),
                  'lead': T('引用只限通知与两部门新闻稿原文，勿延伸为公司具体产品承诺'),
                  'cross': T('涉港企内销与跨境供应链客户，可结合内外贸一体化保障需求一并梳理')},
         rolesImpact={'front': 1, 'midback': 2, 'lead': 2, 'cross': 2},
         source={'sc': '国家金融监督管理总局、商务部联合发布《关于加强商务和保险协同 做好内贸险有关工作的通知》（商务部官网 2026-09-29 16:20）', 'tc': '國家金融監督管理總局、商務部聯合發布《關於加強商務和保險協同 做好內貿險有關工作的通知》（商務部官網 2026-09-29 16:20）', 'lang': 'zh'},
         boards=['reg', 'product'], themes=['reg', 'product', 'china'],
         tags=tg('金融监管总局', '商务部', '内贸险', '信用保险', '共保体', '反骗保'),
         originalUrl='http://www.mofcom.gov.cn/xwfb/rcxwfb/art/2026/art_7922bc64c4b7410c9d4a54af10921130.html'),

    item(id='fstb-north-metropolis-insurance-capital-20260929', score=85, verifyStatus='verified',
         sourceTier='official', sourceKey='family_office', contentKind='press',
         publishedAt='2026-09-29T14:30:00+08:00',
         title=T('财库局局长许正宇率金融业界考察北部都会区：保险业风险为本资本制度优化后，12月31日起为北都在内的基建投资提供资本优惠待遇',
                 '財庫局局長許正宇率金融業界考察北部都會區：保險業風險為本資本制度優化後，12月31日起為北都在內的基建投資提供資本優惠待遇'),
         summary=T('财库局局长许正宇9月29日率金融业界代表团考察北部都会区，成员涵盖资产管理、私募投资、保险、会计及金融科技等领域高层，以及金融监管机构高层代表（包括保险业监管局行政总监张云正）。考察港深创新及科技园（河套香港园区）、古洞北新发展区及洪水桥／厦村新发展区。政府披露：截至今年7月，与北都相关的工务工程获立法会财委会拨款已超过1,800亿港元；并将向三间园区公司各注资100亿元、预留100亿元以贷款方式支持洪水桥大学城校园区。许正宇指，保险业风险为本资本制度经优化后，将由今年12月31日起为北都在内的基础设施投资提供资本优惠待遇，预期释放更多保险资金投入北都基建项目。',
                 None),
         why=T('这条把「北都融资缺口」与「保险资金资本待遇」直接连上：12月31日起基建投资享资本优惠，等于为保险公司配置北都项目降低资本成本，属可预期的资金流向前置信号。对机构而言是资产端与政企对接的时点；对高客服务而言，北都相关基建与产业项目也可能成为长期资本与家族资本关注的方向。',
                 None),
         actions={'front': T('谈资产配置时只讲政策方向（基建资本优惠12月31日生效），不推荐任何具体项目'),
                  'midback': T('把北都资本优惠生效日（2026-12-31）列入资产端政策日历，与RBC优化一并跟踪'),
                  'lead': T('「释放保险资金」是政府预期表述，切勿改写为具体配置规模或收益承诺'),
                  'cross': T('家族资本与保险资金在长周期基建上的关注点不同，讨论时分开处理期限与流动性')},
         rolesImpact={'front': 1, 'midback': 2, 'lead': 3, 'cross': 2},
         source={'sc': '香港特区政府新闻公报（财经事务及库务局） 2026-09-29 14:30', 'tc': '香港特區政府新聞公報（財經事務及庫務局） 2026-09-29 14:30', 'lang': 'zh'},
         boards=['reg', 'market'], themes=['reg', 'market', 'capital'],
         tags=tg('北部都会区', '财库局', '保险资金', '风险为本资本制度', '基建投资', '资本优惠'),
         originalUrl='https://www.info.gov.hk/gia/general/202609/29/P2026092900320.htm'),

    # ======================= 媒体 / 市场 =======================
    item(id='scmp-hk-luxury-property-sales-rate-20260929', score=62,
         sourceTier='media', sourceKey='scmp', contentKind='news',
         publishedAt='2026-09-29T18:00:00+08:00',
         title=T('南华早报：市场忧虑利率上升，名人业主趁高位沽货——模特兼演员Eunis Chan Ka-yung 3,225万售半山两房、账面赚约130%；梁安琪7,000万售西贡独立屋、赚幅不足2% [EN原文]',
                 '南華早報：市場憂慮利率上升，名人業主趁高位沽貨——模特兼演員Eunis Chan Ka-yung 3,225萬售半山兩房、賬面賺約130%；梁安琪7,000萬售西貢獨立屋、賺幅不足2% [EN原文]'),
         summary=T('南华早报9月29日报道：在市场对可能加息的忧虑下，多名知名业主选择现阶段出售豪宅。市场消息指模特兼演员Eunis Chan Ka-yung以3,225万港元（约410万美元）售出半山一个两房单位，账面获利约130%；商人、澳门立法会议员梁安琪（Angela Leong On-kei，已故赌王何鸿燊四太）以7,000万港元售出西贡一幢豪宅，净赚不足2%。代理指部分豪宅业主因忧虑加息而更愿议价，但买家基于同一原因出价审慎；有销售总监形容买家「强烈观望」。报道指高端成交的突增或因库存消化而属短暂。',
                 None),
         why=T('豪宅业主趁预期加息前出货，是观察香港高净值人群资产腾挪偏好的即时样本：同一时段卖方提高议价意愿、买方转观望，意味高端物业的流动性正在变薄。对高客服务而言，物业变现后的资金去向（现金、定存还是长期保障）往往是保障与传承方案的自然切入时点。',
                 None),
         actions={'front': T('客户谈物业套现时，先听资金用途与期限，再谈保障缺口，不作「卖楼买保险」式引导'),
                  'midback': T('把高端物业成交与议价意愿变化列入高客资产偏好观察项'),
                  'lead': T('只引用报道所述成交与代理观点，不预测楼价走势'),
                  'cross': T('港澳两地的物业与居所安排常与跨境保障、医疗及子女教育规划联动，宜一并梳理')},
         rolesImpact={'front': 2, 'midback': 1, 'lead': 1, 'cross': 2},
         source={'sc': '南华早报（SCMP）2026-09-29 [EN原文]', 'tc': '南華早報（SCMP）2026-09-29 [EN原文]', 'lang': 'en'},
         boards=['market'], themes=['market', 'hnw'],
         tags=tg('香港楼市', '豪宅', '加息预期', '高净值', '资产腾挪', '南华早报'),
         originalUrl='https://www.scmp.com/business/article/3369169/eunis-chan-angela-leong-sell-luxury-hong-kong-properties-rate-increases-loom'),

    item(id='scmp-citi-china-30y-bonds-20260929', score=64,
         sourceTier='media', sourceKey='scmp', contentKind='news',
         publishedAt='2026-09-29T17:22:00+08:00',
         title=T('南华早报：花旗研究转而看多中国30年期国债，料收益率向1.8%下行、10年期或趋近1.6%；指3,600亿元人民币金融机构注资计划或推升超长期久期需求 [EN原文]',
                 '南華早報：花旗研究轉而看多中國30年期國債，料收益率向1.8%下行、10年期或趨近1.6%；指3,600億元人民幣金融機構注資計劃或推升超長期久期需求 [EN原文]'),
         summary=T('南华早报9月29日报道：花旗研究在周一报告中转为看多中国30年期国债，预期即使美国国债收益率上行，内地超长期国债收益率仍将下行——30年期收益率料回落至1.8%、10年期或趋近1.6%。花旗EM亚洲利率与外汇策略主管Rohit Garg指，供给侧压力缓解与四季度超长期国债市场动态改善是主因，并点名内地近期公布的3,600亿元人民币（约537亿美元）主要金融机构注资计划，可能推升久期需求、尤其集中在超长端。',
                 None),
         why=T('长端利率走向直接决定保险公司资产负债匹配的成本与空间：若内地超长期收益率继续下行，负债端定价与资产端再投资压力同步放大，反之则为久期配置提供窗口。对香港而言，内地利率与外债收益率的分化也影响客户对人民币与美元资产的取舍。',
                 None),
         actions={'front': T('客户问人民币资产时，引用机构观点须标明来源与日期，且不作收益率承诺'),
                  'midback': T('把内地长端利率预期列入资产端与产品定价讨论的输入项'),
                  'lead': T('花旗预测属观点而非事实，引用一律加「机构研究观点」限定'),
                  'cross': T('内地长端利率与香港美元利率的分化，是讨论币种配置时不可省略的背景')},
         rolesImpact={'front': 1, 'midback': 2, 'lead': 2, 'cross': 2},
         source={'sc': '南华早报（SCMP）2026-09-29 [EN原文]', 'tc': '南華早報（SCMP）2026-09-29 [EN原文]', 'lang': 'en'},
         boards=['market'], themes=['market', 'capital'],
         tags=tg('中国国债', '超长期债券', '收益率', '久期', '花旗', '资产配置'),
         originalUrl='https://www.scmp.com/business/markets/article/3369198/why-citi-betting-chinas-30-year-bonds-us-treasury-yields-climb'),

    item(id='scmp-pimco-china-diversification-20260929', score=63,
         sourceTier='media', sourceKey='scmp', contentKind='news',
         publishedAt='2026-09-29T16:00:00+08:00',
         title=T('南华早报专访：PIMCO总裁称全球投资者对中国的看法「180度转向」，正引导非美客户以中国离岸债券分散美元与美股集中度 [EN原文]',
                 '南華早報專訪：PIMCO總裁稱全球投資者對中國的看法「180度轉向」，正引導非美客戶以中國離岸債券分散美元與美股集中度 [EN原文]'),
         summary=T('南华早报9月29日刊出PIMCO总裁Christian Stracke在香港的专访：全球投资者正重新转向中国以寻找美国资产之外的替代，PIMCO视中国债券为分散组合最安全的方式之一，因市场对中国的情绪已「180度转向」。PIMCO截至6月底管理资产逾2万亿美元，Stracke称该行一直引导客户（尤其是非美国客户）配置中国离岸债券，以降低美元与股票资产的集中度——他强调客户并非都在担忧美国，而是历经美股强势后组合对美国资产与美元的暴露过高。',
                 None),
         why=T('这是全球最大债管机构之一对「资产配置重心偏移」的公开表态，且强调是客户主动提问驱动的分散需求，而非看空美元。对高客服务而言，这为「为何要谈非美元资产」提供了外部机构视角，同时提醒：分散诉求的动因是集中度风险，而不是收益承诺。',
                 None),
         actions={'front': T('客户问分散配置时，可引用机构观点说明「美元集中度」问题，但不代客推荐具体标的'),
                  'midback': T('把「非美客户分散诉求」列为高客资产配置对话的常见情境备用素材'),
                  'lead': T('严格区分机构对市场的观点与我们可提供的产品范围，避免越界'),
                  'cross': T('美元/非美元资产比例是跨境家庭的核心议题，需与税务与流动性安排一并考虑')},
         rolesImpact={'front': 2, 'midback': 1, 'lead': 2, 'cross': 2},
         source={'sc': '南华早报（SCMP）2026-09-29 [EN原文]', 'tc': '南華早報（SCMP）2026-09-29 [EN原文]', 'lang': 'en'},
         boards=['market'], themes=['market', 'global-allocation'],
         tags=tg('PIMCO', '中国离岸债券', '资产分散', '美元集中度', '全球配置', '机构观点'),
         originalUrl='https://www.scmp.com/business/china-business/article/3369148/180-degree-flip-sees-global-investors-turn-china-diversification-pimco-president'),

    item(id='artemis-lane-financial-catbond-soft-market-20260929', score=62,
         sourceTier='media', sourceKey='artemis', contentKind='news',
         publishedAt='2026-09-29T16:00:00+08:00',
         title=T('Lane Financial：巨灾债软市场未至2017年低位但有再走软空间——现时倍数1.9倍（2017年一季度低谷1.7倍），若2026年余下无大灾，软市或再延续一年 [EN原文]',
                 'Lane Financial：巨災債軟市場未至2017年低位但有再走軟空間——現時倍數1.9倍（2017年一季度低谷1.7倍），若2026年餘下無大災，軟市或再延續一年 [EN原文]'),
         summary=T('Artemis 9月29日报道：顾问机构Lane Financial最新分析指，巨灾债券与ILS当前软市场尚未跌至2017年的低迷水平，但存在进一步走软空间——未受损自然巨灾债组合的加权平均倍数现为1.9倍预期损失，2017年一季度上轮软市高峰时为1.7倍（2005年有数据以来最低）。Lane Financial指价格持续下行、收益率降低，并称若2026年余下时间无重大巨灾损失，软市料至少再延续一年（至明年飓风季）；上一次长达四年的软市（2013–2017）最终由Harvey、Irma、Maria接连致损告终。该机构提醒，Q3至Q4通常因1月1日续保季而季节性收紧，但2016年并未出现季节性反弹、软势直接延续至2017年一季度，历史可能重演。',
                 None),
         why=T('巨灾债定价是再保成本链条的最前端：倍数1.9倍接近历史软市区间低位，意味着再保与转分保价格仍处买方有利区，但要留意「软市靠无大灾维持」这一脆弱前提。对产品定价与核保假设而言，这是不宜把「再保持续趋软」当成长期常数的理由。',
                 None),
         actions={'front': T('被问明年产品价格时，答「再保条件仍偏软但取决于无大灾前提」，不承诺价格走向'),
                  'midback': T('在再保成本假设中同时列出软市延续与大灾中断两种情景'),
                  'lead': T('引用须标明来源（Lane Financial）与倍数口径（1.9倍预期损失）及截至时点'),
                  'cross': T('巨灾条款变化最终影响高保额财产与责任类方案的可承接性，需个案确认')},
         rolesImpact={'front': 1, 'midback': 2, 'lead': 2, 'cross': 1},
         source={'sc': 'Artemis.bm 2026-09-29（引述 Lane Financial 报告）[EN原文]', 'tc': 'Artemis.bm 2026-09-29（引述 Lane Financial 報告）[EN原文]', 'lang': 'en'},
         boards=['market'], themes=['market', 'ils', 'catastrophe'],
         tags=tg('巨灾债券', 'ILS', '软市场', '再保险定价', 'Lane Financial', '倍数'),
         originalUrl='https://www.artemis.bm/news/catastrophe-bond-soft-market-not-yet-at-2017-levels-but-could-last-another-year-lane-financial/'),

    item(id='artemis-marsh-archer-life-annuity-platform-20260929', score=62,
         sourceTier='media', sourceKey='artemis', contentKind='news',
         publishedAt='2026-09-29T15:30:00+08:00',
         title=T('Marsh推出「Archer」平台：为寿险与年金再保人、sidecar、SPI及分离账户提供快速设立与营运基础设施，并在百慕大注册 Mangrove ISAC Life Re [EN原文]',
                 'Marsh推出「Archer」平台：為壽險與年金再保人、sidecar、SPI及分離賬戶提供快速設立與營運基礎設施，並在百慕大註冊 Mangrove ISAC Life Re [EN原文]'),
         summary=T('Artemis 9月29日报道：Marsh推出名为Archer的新平台服务，协助资产管理人与寿险／年金保险公司设立并营运再保业务，覆盖独立再保载体、寿险与年金再保sidecar（含特殊目的再保人SPI、专属再保单元及独立分离账户）等结构；赞助方保留所有权与策略控制，Marsh提供共享营运基础设施及精算、资本、风险、再保、寿险与年金保险管理及监管专业能力。为配合该服务，Marsh已在百慕大注册成立一家名为 Mangrove ISAC Life Re 的注册分离账户公司。曾任Oliver Wyman精算业务、驻百慕大的Faisal Haddad获任命为Archer by Marsh行政总裁（待监管批准）。',
                 None),
         why=T('寿险与年金再保正成为第三方资本（资产管理人、机构投资者）进入保险业的主要路径，Marsh此举等于把「设立一个再保载体」从个案工程变成可复用产品，将降低新主体入场门槛。对保险公司而言，意味着分出与资本安排的选项继续增多；对风险评估而言，需留意资本涌入对长期承保条件与资产风险的连带影响。',
                 None),
         actions={'front': T('客户问到「保单背后的再保安排」时，答再保结构属公司层面安排、不影响合同条款，不代答个案'),
                  'midback': T('把寿险/年金再保载体与sidecar兴起的趋势列入资本与再保结构观察'),
                  'lead': T('不要把第三方资本入场解读为具体产品的分红或收益保证'),
                  'cross': T('高保额与长期寿险方案的再保承接与资本安排须个案确认，不作普遍承诺')},
         rolesImpact={'front': 1, 'midback': 2, 'lead': 2, 'cross': 1},
         source={'sc': 'Artemis.bm 2026-09-29 [EN原文]', 'tc': 'Artemis.bm 2026-09-29 [EN原文]', 'lang': 'en'},
         boards=['market', 'product'], themes=['market', 'capital', 'reinsurance'],
         tags=tg('Marsh', '寿险再保', 'sidecar', 'SPI', '第三方资本', '百慕大'),
         originalUrl='https://www.artemis.bm/news/marsh-launches-archer-platform-for-life-and-annuity-reinsurers-sidecars-spis-and-cells/'),

    item(id='ian-aig-keiichi-ishida-japan-20260929', score=60,
         sourceTier='media', sourceKey='insuranceasianews', contentKind='news',
         publishedAt='2026-09-29T14:35:00+08:00',
         title=T('AIG委任Keiichi Ishida为日本商业财产险主管：已从新加坡调回东京，此前在Everest任日本区主管两年 [EN原文]',
                 'AIG委任Keiichi Ishida為日本商業財產險主管：已從新加坡調回東京，此前在Everest任日本區主管兩年 [EN原文]'),
         summary=T('InsuranceAsia News 9月29日报道：AIG任命Keiichi Ishida为日本商业财产险（commercial property）主管。Ishida已调回东京履新，此前两年在Everest担任日本区主管、驻新加坡。这是一宗涉及跨境调任的高管任命，反映AIG在日本商业财产险条线的布局调整。',
                 None),
         why=T('日本商业财产险是亚太区最重要的财产险市场之一，承保人才的跨境调动往往先于业务策略调整。对关注区域险企动向与再保／经纪人脉网络的从业者，这是可以留意的管理层变动信号。',
                 None),
         actions={'front': 0, 'midback': T('把区域保司财产险条线人事变动列入同业动态清单'),
                  'lead': T('引用任命信息只按原文，不作业务策略解读'),
                  'cross': 0},
         rolesImpact={'front': 0, 'midback': 1, 'lead': 1, 'cross': 0},
         source={'sc': 'InsuranceAsia News 2026-09-29 [EN原文]', 'tc': 'InsuranceAsia News 2026-09-29 [EN原文]', 'lang': 'en'},
         boards=['insurer'], themes=['insurer', 'people'],
         tags=tg('AIG', '商业财产险', '日本', '人事任命', '同业动态'),
         originalUrl='https://insuranceasianews.com/aig-names-keiichi-ishida-as-head-of-commercial-property-in-japan/'),

    item(id='ian-hk-broker-nova-revenue-20260929', score=68,
         sourceTier='media', sourceKey='insuranceasianews', contentKind='news',
         publishedAt='2026-09-29T10:52:00+08:00',
         title=T('香港经纪行Nova收入增12%至2,000万美元，内地扩张带来贡献 [EN原文]',
                 '香港經紀行Nova收入增12%至2,000萬美元，內地擴張帶來貢獻 [EN原文]'),
         summary=T('InsuranceAsia News 9月29日报道：香港保险经纪行Nova（新域保险顾问）收入按年增长12%至2,000万美元（约1.56亿港元），内地业务扩张为主要贡献来源。报道归入保险经纪、香港及业绩类别。该行是香港有规模的本地经纪之一，其收入结构变化反映香港经纪板块对内地相关业务的依赖度正在提升。',
                 None),
         why=T('香港经纪板块的收入构成，是观察「内地相关业务（含跨境客群与企业风险）对本地中介渠道贡献」的实用切口。收入增长由内地扩张带动，说明本地经纪的竞争力越来越取决于跨地域服务与合规能力，而非单纯本地销售规模。',
                 None),
         actions={'front': T('客户问经纪规模时，答以公开报道数据为准，不代答偿付或服务承诺'),
                  'midback': T('把本地经纪板块的收入与区域结构变化列入渠道竞争观察'),
                  'lead': T('引用业绩数字须标注来源与期间，避免与保费规模混淆'),
                  'cross': T('内地相关业务增长意味着跨境合规要求同步上升，客户安排须按属地规则处理')},
         rolesImpact={'front': 1, 'midback': 2, 'lead': 2, 'cross': 2},
         source={'sc': 'InsuranceAsia News 2026-09-29 [EN原文]', 'tc': 'InsuranceAsia News 2026-09-29 [EN原文]', 'lang': 'en'},
         boards=['market'], themes=['market', 'channel', 'cross-border'],
         tags=tg('香港经纪', 'Nova', '内地扩张', '收入增长', '渠道竞争'),
         originalUrl='https://insuranceasianews.com/hong-kong-broker-novas-revenue-rises-12-to-us20m-as-mainland-expansion-contributes/'),

    item(id='ian-igloo-dana-parametric-rain-20260929', score=63,
         sourceTier='media', sourceKey='insuranceasianews', contentKind='news',
         publishedAt='2026-09-29T10:18:00+08:00',
         title=T('Igloo联手印尼电子钱包Dana推出参数型降雨保障：以天气指标触发赔付，切入小微与零工经济场景 [EN原文]',
                 'Igloo聯手印尼電子錢包Dana推出參數型降雨保障：以天氣指標觸發賠付，切入小微與零工經濟場景 [EN原文]'),
         summary=T('InsuranceAsia News 9月29日报道：保险科技公司Igloo与印尼电子钱包Dana合作，推出针对印尼市场的参数型降雨保障（parametric rain protection）。该产品以天气指标触发赔付、无需逐案核损，并通过嵌入式渠道触达用户，属新兴市场小微与零工经济场景的保障创新。',
                 None),
         why=T('参数型保障的价值在于「无需核损、按指标自动赔付」，天然适配高频、小额、难以逐案查勘的场景。东南亚嵌入式渠道的这一实践，为「以数据指标代替传统理赔流程」提供了可对照的落地样本，对理解保障型产品的产品形态演进有参考意义。',
                 None),
         actions={'front': T('客户问参数型保险时，先讲清「按指标触发、与实损可能不一致」的特性，不作收益或赔付承诺'),
                  'midback': T('把嵌入式渠道与参数型结构列入新产品形态观察清单'),
                  'lead': T('介绍产品创新时须同时提示参数型产品的基差风险（指标与实际损失不符）'),
                  'cross': T('跨境经营的客户若涉及东南亚市场，可留意当地嵌入式保障的合规与分销要求')},
         rolesImpact={'front': 1, 'midback': 2, 'lead': 2, 'cross': 1},
         source={'sc': 'InsuranceAsia News 2026-09-29 [EN原文]', 'tc': 'InsuranceAsia News 2026-09-29 [EN原文]', 'lang': 'en'},
         boards=['product', 'tech'], themes=['product', 'insurtech', 'regional'],
         tags=tg('Igloo', 'Dana', '参数型保险', '降雨保障', '嵌入式保险', '印尼'),
         originalUrl='https://insuranceasianews.com/igloo-partners-with-dana-to-launch-indonesian-parametric-rain-protection/'),

    item(id='ian-markel-kevin-leung-sea-20260929', score=60,
         sourceTier='media', sourceKey='insuranceasianews', contentKind='news',
         publishedAt='2026-09-29T09:38:00+08:00',
         title=T('Markel调任Kevin Leung为东南亚董事总经理：统一执掌新加坡与马来西亚业务 [EN原文]',
                 'Markel調任Kevin Leung為東南亞董事總經理：統一執掌新加坡與馬來西亞業務 [EN原文]'),
         summary=T('InsuranceAsia News 9月29日报道：专业保险公司Markel将Kevin Leung调任为东南亚董事总经理，统一负责新加坡与马来西亚业务。报道归入人事、保司及东盟类别。该任命反映Markel在东南亚把新马两地营运整合管理的安排。',
                 None),
         why=T('专业险企把新马两地合并由单一主管掌舵，通常意味着区域资源整合与决策效率优先。这类组织调整值得纳入同业区域布局的跟踪，尤其对关注专业险种与跨境承保能力的从业者。',
                 None),
         actions={'front': 0, 'midback': T('把专业险企东南亚组织整合列入同业区域布局观察'),
                  'lead': T('引用任命信息只按原文，勿外推为业务或产品承诺'),
                  'cross': 0},
         rolesImpact={'front': 0, 'midback': 1, 'lead': 1, 'cross': 0},
         source={'sc': 'InsuranceAsia News 2026-09-29 [EN原文]', 'tc': 'InsuranceAsia News 2026-09-29 [EN原文]', 'lang': 'en'},
         boards=['insurer'], themes=['insurer', 'people'],
         tags=tg('Markel', '东南亚', '新加坡', '马来西亚', '人事任命'),
         originalUrl='https://insuranceasianews.com/markel-shifts-kevin-leung-to-managing-director-for-southeast-asia/'),
]


def main():
    path = os.path.join(BASE, 'data', 'live-items.json')
    data = json.load(open(path, encoding='utf-8'))
    existing = {it.get('id') for it in data['items']}
    new = [it for it in NEW if it['id'] not in existing]
    dup = [it['id'] for it in NEW if it['id'] in existing]
    if dup:
        print('跳过已存在:', dup)
    # 按 publishedAt 降序插入（窗口内最新在前）
    new.sort(key=lambda x: x['publishedAt'], reverse=True)
    data['items'] = new + data['items']
    data['meta']['generatedAt'] = NOW
    data['meta']['itemCount'] = len(data['items'])
    n = len(data['items'])
    data['meta']['windowNote'] = {'sc': f'本库{n}条。', 'tc': f'本庫{n}條。'}
    shutil.copy(path, os.path.join(BASE, f'data/live-items.json.bak-0929-1808'))
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print(f'写入完成: 新增 {len(new)} 条, 合计 {n} 条')
    for it in new:
        print(' +', it['publishedAt'], it['id'])


if __name__ == '__main__':
    main()
