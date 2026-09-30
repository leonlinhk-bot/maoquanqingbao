#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-30 18:08（周三）增量采集。

窗口：2026-09-30 00:55 → 18:08（承接 09-30 00:23 深夜批次）
逐源核验（14 信源）：
- IA：通函页实抓 → 30/9 新增《监管通讯》Conduct in Focus 第13期（2026年9月），PDF 正文已读 → 入库。
  press_releases 页为 JS 渲染（表格空），speeches_articles 最新 8/9 → 窗口内无新闻稿新增。
- HKMA：新闻稿页实抓，30/9 共 8 则（20260930-3 至 -10）。经 info.gov.hk RSS 核对发布时间：
  16:30 货币统计/住宅按揭/外汇基金资产负债表+国际储备、12:25 知识产权融资沙盒、17:05 HKICL 伪冒网站、
  11:15 Mastercard 伪冒网站、另有与银行有关骗案通知。取 4 则（货币统计、住宅按揭、IP沙盒、外汇基金），
  并单列 HKICL 伪冒网站警示（涉 FPS「买家保障」新变体 refund-fps.ink）；Mastercard/银行骗案同类合并于该条导读。
- NFRA：官网列表经 doubao 交叉核验，9/29 另有《安责险事故预防服务通知》（应急厅函〔2026〕352号，
  应急管理部 9/29 15:42 发布），上一批次仅取内贸险 → 本条属补录，已核全文。
  9/30 当日无新文件。
- HKFI：media-release 页最新 16/9 → 无新增。
- FSTB(family_office)：官网新闻 30/9 两则（大宗商品交易联合工作组首次会议、政府首五个月财务状况），
  均非保险/家办核心，且中英文版发布时间不一致（12:30 / 17:10）→ 本批不取。
- 保司：AIA 最新 24/9、宏利最新 28/9、保诚香港最新 23/9、AXA 最新 23/9、永明最新 15/9 → 窗口内无新增。
- insuranceasia(RSS)：上批未能取时间戳，本次 RSS 正常，30/9 05:00–06:00 共 5 则；
  Markel 与 Chubb MyLegacy 两则库内已有（同题不同源）→ 跳过；取 2 则（保诚新加坡危疾调查、日本保费份额）。
- insuranceasianews(WP API)：窗口内 4 则 → 取 2 则（Marsh ASEAN CEO、澳洲监管 2026-27 优先事项）；
  Perils 亚太累积风险一则内容付费墙仅见导语 → 不取；乐天损害险出售一则信息量不足 → 不取。
- insurancebusinessmag(Atom)：窗口内 2 则 → 取 KPMG 保险业 AI 报告；中国 AI 模型一则与保险无关 → 不取。
- scmp(RSS)：窗口内 7 则 → 取 2 则（Capco 财富管理 AI 与人手、Grant Thornton 港企董事会 AI/网安人才）。
- artemis(RSS)：窗口内 1 则（Pioneer 巨灾债基金 AUM）→ 入库。
- insurtech / family_office：见上，无新增。
本批 15 条覆盖 ia / hkma / nfra / scmp / insurancebusinessmag / insuranceasia / insuranceasianews / artemis。
"""
import json, shutil, os
import zhconv

BASE = '/Users/leonliang/maoquanqingbao'
NOW = '2026-09-30T18:08:00+08:00'

FIX = {'轉帳': '轉賬', '鏈接': '連結', '裏面': '裡面', '數據': '數據'}


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
    item(id='ia-conduct-in-focus-issue-13-20260930', score=88, verifyStatus='verified',
         sourceTier='official', sourceKey='ia', contentKind='circular',
         publishedAt='2026-09-30T09:00:00+08:00',
         title=T('保监局《监管通讯》第13期（2026年9月）：点名营销选择性数据、伪造文件错分专业投资者的虚假传闻、以「自荐转介」包装的变相回佣，并强调代理主管问责与KPIM角色',
                 '保監局《監管通訊》第13期（2026年9月）：點名營銷選擇性數據、偽造文件錯分專業投資者的虛假傳聞、以「自薦轉介」包裝的變相回佣，並強調代理主管問責與KPIM角色'),
         summary=T('保险业监管局9月30日向所有获授权保险公司的行政总裁、持牌保险代理机构及持牌保险经纪公司的负责人员发出《监管通讯》第13期（2026年9月），列出多项市场监管观察：一是营销操守——吸睛统计数字虽在某一时点数字正确，但抽离背景单独呈现会造成误导性期望，并可能违反监管要求，保司须在营销流程嵌入治理管控与以客为本的复核；二是「假新闻」教训——针对近日市场流传以伪造文件把客户错误分类为专业投资者的虚假传闻，局方重申专业投资者豁免属监管特权，仅应在客户真正符合资格时使用；三是KPIM（中介管理控权职能主要人员）角色日趋复杂，须建立以客为本文化、设计能达成操守目标的管控并强化代理管理层级问责；四是「自荐转介」安排——以自荐转介之名行禁止性回佣之实不会获接受，实质重于形式；五是说明哪些负责人员申请人会被安排面试及面试如何进行；六是两宗执法个案凸显代理主管对下线的问责。另涵盖2026年上半年投诉统计与反诈骗工作。', None),
         why=T('这一期把前线与渠道管理最高频的三个合规雷区一次点清：营销数字的选择性呈现、专业投资者分类的真实性、以及用「自荐转介」包装的回佣。三者都落在日常作业里，不是抽象原则：营销物料怎么写、PI 身分怎么认定、转介与佣金怎么走账，监管已明示会以实质重于形式审视。代理主管须对其下线的行为负责这一点也被再次强调，意味着合规责任不再止于个人。对新客户招揽与团队复制而言，这份文件是当前最直接的自查依据。', None),
         actions={'front': T('营销物料引用统计数字须附背景与口径，不单独引用吸睛数字；不向不符合资格的客户套用专业投资者身分'),
                  'midback': T('复查近半年客户分类为专业投资者的个案是否留有真实资格证明与公平对待纪录'),
                  'lead': T('把营销、PI分类、自荐转介三项列入团队合规例会与自查清单，并明确代理主管的督导责任'),
                  'cross': T('内地访客客户不得以「自荐转介」名义变相回佣，转介与费用安排须逐笔留痕')},
         rolesImpact={'front': 3, 'midback': 3, 'lead': 3, 'cross': 2},
         source={'sc': '保险业监管局通函《监管通讯》（Conduct in Focus）第13期 2026-09-30 [EN原文]',
                 'tc': '保險業監管局通函《監管通訊》（Conduct in Focus）第13期 2026-09-30 [EN原文]', 'lang': 'en'},
         boards=['reg', 'compliance'], themes=['reg', 'compliance', 'channel'],
         tags=tg('监管通讯', '营销操守', '专业投资者', '自荐转介', 'KPIM', '代理主管问责'),
         originalUrl='https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/files/20260930_Circular_Conduct_In_Focus_Issue_13_Eng.pdf'),

    item(id='hkma-monetary-statistics-aug-2026-20260930', score=85, verifyStatus='verified',
         sourceTier='official', sourceKey='hkma', contentKind='stats',
         publishedAt='2026-09-30T16:30:00+08:00',
         title=T('金管局8月货币统计：总存款升1.4%（港元+2.2%）、贷款升0.3%；人民币存款减2.1%至1.1015万亿元，年内总存款累计升7.3%、港元存款升8.6%',
                 '金管局8月貨幣統計：總存款升1.4%（港元+2.2%）、貸款升0.3%；人民幣存款減2.1%至1.1015萬億元，年內總存款累計升7.3%、港元存款升8.6%'),
         summary=T('金管局9月30日公布2026年8月货币统计数字：认可机构总存款8月增加1.4%，其中港元存款及外币存款分别增加2.2%及0.8%；年内至8月底，总存款及港元存款分别累计增加7.3%及8.6%。香港人民币存款8月减少2.1%，至8月底为11,015亿元人民币；8月跨境贸易结算的人民币汇款总额为15,376亿元人民币，7月为13,837亿元。总贷款与垫款8月增加0.3%，年内累计增加7.0%，其中在港使用贷款（含贸易融资）增0.4%，境外使用贷款大致不变。港元贷存比率由7月底的70.7%降至8月底的69.3%，因港元存款增速快于港元贷款。港元M2及M3均升2.1%（同比升9.9%），经季节调整的港元M1升3.5%（同比升4.7%），反映部分投资相关活动；总M2及M3均升1.4%（同比升11.0%）。局方提示单月数字受季节性资金需求等因素影响，宜观察长期趋势。', None),
         why=T('这组数字是理解香港资金面的底稿：港元存款与M2/M3同步走高、贷款温和增长、贷存比率回落，说明流动性充裕而信贷需求未同步跟上；人民币存款单月回落2.1%则提示人民币资金池的波动性，但跨境贸易结算汇款反而由7月的1.38万亿元升至1.54万亿元，使用量并未减弱。对保险与财富管理而言，港元资金充裕、贷存比率下降的环境会影响存款与固定收益类替代品的相对吸引力，也是与客户讨论资金停放与币种配置时的官方口径来源。', None),
         actions={'front': T('引用资金面数据时须标明为金管局月度统计、并说明单月波动不宜过度解读'),
                  'midback': T('把港元贷存比率与人民币存款走势列入季度资产端与产品定价的背景观察'),
                  'lead': T('对内引用须注明来源与月份，勿引申为利率或产品回报预测'),
                  'cross': T('人民币存款与跨境结算数据是讨论跨境客户资金流的基础事实，须按属地规则处理')},
         rolesImpact={'front': 0, 'midback': 2, 'lead': 2, 'cross': 1},
         source={'sc': '香港金融管理局新闻稿（2026-09-30 16:30）[EN原文]', 'tc': '香港金融管理局新聞稿（2026-09-30 16:30）[EN原文]', 'lang': 'en'},
         boards=['market'], themes=['market', 'macro'],
         tags=tg('货币统计', '总存款', '人民币存款', '贷存比率', 'M2', 'M3'),
         originalUrl='https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/09/20260930-9/'),

    item(id='hkma-residential-mortgage-survey-aug-2026-20260930', score=86, verifyStatus='verified',
         sourceTier='official', sourceKey='hkma', contentKind='stats',
         publishedAt='2026-09-30T16:30:00+08:00',
         title=T('金管局8月住宅按揭统计：申请按月减8.3%至8,446宗，新批贷款减28.2%至322亿港元（一手-31.8%、二手-36.7%、再融资+6.8%）；未偿还总额升0.6%至1.9754万亿，拖欠比率0.11%',
                 '金管局8月住宅按揭統計：申請按月減8.3%至8,446宗，新批貸款減28.2%至322億港元（一手-31.8%、二手-36.7%、再融資+6.8%）；未償還總額升0.6%至1.9754萬億，拖欠比率0.11%'),
         summary=T('金管局9月30日公布2026年8月住宅按揭统计调查结果：8月按揭申请按月减少8.3%至8,446宗。8月新批出按揭贷款额较7月减少28.2%至322亿港元，其中一手市场交易批出贷款减31.8%至91亿港元，二手市场减36.7%至153亿港元，涉及再融资的贷款则增6.8%至78亿港元。8月新取用按揭贷款额较7月增加11.6%至328亿港元。新批按揭中，以香港银行同业拆息（HIBOR）为定价参考的比例由7月的61%降至57%，以最优惠利率为定价参考的比例由1.3%升至1.9%。8月底未偿还按揭贷款总额按月增0.6%至19,754亿港元。按揭拖欠比率维持于0.11%的低水平，经重组贷款比率维持接近0%。', None),
         why=T('一手与二手新批贷款同时大幅回落、而再融资逆势上升，是供楼成本与楼价预期变化下最直接的客户行为信号：买家转趋观望，但存量业主趁利率环境转定息或转按。新批按揭中HIBOR定价占比由61%降至57%，说明部分借款人主动选择较稳定的定价结构，这与市场对利率走向的分歧相呼应。拖欠比率维持0.11%，显示资产质素暂未见压力，是高客讨论杠杆与流动性安排时可用的官方参照。', None),
         actions={'front': T('客户问及按揭或杠杆安排时，引用官方统计须标明月份与口径，不作楼价或利率预测'),
                  'midback': T('把HIBOR/最优惠利率定价占比变化列入客户供款能力与产品适配的讨论素材'),
                  'lead': T('引用一律标注金管局住宅按揭统计调查，并注明再融资与市场交易口径不同'),
                  'cross': T('按揭与杠杆数据属香港本地口径，跨境客户涉境外物业融资须按当地规则个案处理')},
         rolesImpact={'front': 2, 'midback': 3, 'lead': 2, 'cross': 1},
         source={'sc': '香港金融管理局新闻稿（2026-09-30 16:30）[EN原文]', 'tc': '香港金融管理局新聞稿（2026-09-30 16:30）[EN原文]', 'lang': 'en'},
         boards=['market'], themes=['market', 'macro'],
         tags=tg('住宅按揭', '按揭申请', '新批贷款', 'HIBOR定价', '按揭拖欠比率', '再融资'),
         originalUrl='https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/09/20260930-8/'),

    item(id='hkma-ip-financing-sandbox-first-batch-20260930', score=85, verifyStatus='verified',
         sourceTier='official', sourceKey='hkma', contentKind='press',
         publishedAt='2026-09-30T12:25:00+08:00',
         title=T('知识产权融资沙盒完成首批试点融资审批：7宗个案、贷款额100万至3,900万港元，涵盖电子、建筑、玩具制造及医疗器械；同日政府推出专利估值先导支援计划',
                 '知識產權融資沙盒完成首批試點融資審批：7宗個案、貸款額100萬至3,900萬港元，涵蓋電子、建築、玩具製造及醫療器械；同日政府推出專利估值先導支援計劃'),
         summary=T('金管局9月30日公布，知识产权（IP）融资沙盒的参与银行已完成首批7宗试点个案的贷款审批，涵盖电子、建筑、玩具制造及医疗器械等行业；贷款额由100万至3,900万港元，将用于营运资金、业务扩展及市场推广。沙盒由金管局联同商务及经济发展局和知识产权署于2025年12月推出，香港银行公会支持，三家牵头银行——中银香港、汇丰及渣打银行（香港）——在风险可控环境下与不同行业企业客户及专业服务提供者试行IP融资安排：银行把估值服务提供者的IP估值报告纳入信贷评估与审批流程，据独立专业估值向借款人提供较高贷款额或较优惠利率，从而提升知识产权资产丰富的中小企业的融资能力。参与机构认为仍可在加强IP相关专业服务费用的资金支援、优化IP估值流程、提升市场认知与专业能力等方面完善生态。同日政府亦公布首批成功试点个案并推出专利估值先导支援计划。', None),
         why=T('这是香港把「无形资产」变成可融资抵押品的第一步实物证据：贷款额上限已做到3,900万港元，说明估值报告已能被银行纳入审批，而不是停留在概念。对家办与高客而言，这打开了以专利、商标等IP作为融资与流动性来源的讨论空间；对保险业则提示，IP相关专业服务的费用补贴与估值流程，会连带出现新的责任与保障需求。', None),
         actions={'front': T('客户问及无形资产融资时，可说明沙盒为银行试点安排、非任何贷款或利率承诺'),
                  'midback': T('把IP估值服务、专业服务费用支援列入中小企与家办客户融资方案的观察清单'),
                  'lead': T('引用须标注为金管局沙盒试点结果，并注明贷款额与行业分布为个案口径'),
                  'cross': T('跨境客户以境外IP在港融资涉及税务与知识产权归属，须按属地规则个案确认')},
         rolesImpact={'front': 1, 'midback': 2, 'lead': 2, 'cross': 1},
         source={'sc': '香港金融管理局新闻稿（2026-09-30 12:25）；同日政府新闻公报公布首批试点及专利估值先导支援计划 [EN原文]',
                 'tc': '香港金融管理局新聞稿（2026-09-30 12:25）；同日政府新聞公報公布首批試點及專利估值先導支援計劃 [EN原文]', 'lang': 'en'},
         boards=['market', 'family'], themes=['market', 'capital'],
         tags=tg('知识产权融资', '沙盒', '专利估值', '中小企业融资', '银行公会', '无形资产'),
         originalUrl='https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/09/20260930-4/'),

    item(id='hkma-exchange-fund-balance-sheet-aug-2026-20260930', score=84, verifyStatus='verified',
         sourceTier='official', sourceKey='hkma', contentKind='stats',
         publishedAt='2026-09-30T16:30:00+08:00',
         title=T('金管局8月外汇基金资产负债表：总资产减683亿港元至43,354亿，货币基础20,802亿，支持比率升至112.00%；同日发布国际储备及外汇流动性数据',
                 '金管局8月外匯基金資產負債表：總資產減683億港元至43,354億，貨幣基礎20,802億，支持比率升至112.00%；同日發布國際儲備及外匯流動性數據'),
         summary=T('金管局9月30日公布，截至2026年8月31日外汇基金总资产为43,354亿港元，较7月底减少683亿港元，其中外币资产减少680亿港元、港元资产减少3亿港元；外币资产下降主要由于财政储备存款提取，港元资产下降主要由于香港股票按市价重估。货币发行局帐目显示，8月底货币基础为20,802亿港元，较7月底增长1亿港元或0.01%，主要由于已发行外汇基金票据及债券的折价摊销，但部分被负债证明书未偿还数额减少所抵销。8月底后备资产增加32亿港元或0.14%至23,299亿港元，主要来自投资利息收入，部分被负债证明书赎回及投资按市价重估所抵销；支持比率由7月底的111.86%升至8月底的112.00%。金管局同日亦发布截至8月底的国际储备及外汇流动性分析数据（国际货币基金组织特殊数据公布标准下的数据模板）。', None),
         why=T('外汇基金账目是联系汇率制度的月度体检报告：总资产下降主要来自财政储备存款提取而非投资亏损，港元资产减少源于港股按市价重估，支持比率反而升到112.00%。理解「货币基础与后备资产」的对应关系，是回应高客对港元信心、储备充足度与资产安全提问时的官方口径；同时它也提醒市场，财政资金的进出会直接改变外汇基金的资产结构。', None),
         actions={'front': T('客户问及港元信心或储备时，引用外汇基金与支持比率的官方数字，并说明资产变动原因'),
                  'midback': T('把货币基础、后备资产与支持比率列入宏观与流动性观察表的月度指标'),
                  'lead': T('引用一律标注金管局外汇基金资产负债表摘要，勿把资产变动解读为投资表现'),
                  'cross': T('国际储备及外汇流动性数据属IMF SDDS口径，跨境引用须注明标准与截止日')},
         rolesImpact={'front': 1, 'midback': 2, 'lead': 2, 'cross': 1},
         source={'sc': '香港金融管理局新闻稿（2026-09-30 16:30）[EN原文]', 'tc': '香港金融管理局新聞稿（2026-09-30 16:30）[EN原文]', 'lang': 'en'},
         boards=['market'], themes=['market', 'macro'],
         tags=tg('外汇基金', '货币发行局帐目', '货币基础', '后备资产', '支持比率', '国际储备'),
         originalUrl='https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/09/20260930-6/'),

    item(id='hkma-hkicl-fraud-website-refund-fps-20260930', score=86, verifyStatus='verified',
         sourceTier='official', sourceKey='hkma', contentKind='press',
         publishedAt='2026-09-30T17:05:00+08:00',
         title=T('香港银行同业结算公司（HKICL）警示伪冒网站 refund-fps.ink：冒充「买家网上保障」提供退款服务并引导至WhatsApp假客服；同日另有Mastercard伪冒网站及与银行有关的骗案通知',
                 '香港銀行同業結算公司（HKICL）警示偽冒網站 refund-fps.ink：冒充「買家網上保障」提供退款服務並引導至WhatsApp假客服；同日另有Mastercard偽冒網站及與銀行有關的騙案通知'),
         summary=T('金管局9月30日代香港银行同业结算有限公司（HKICL）发出警示：HKICL近日发现一个伪冒网站 refund-fps.ink，冒充HKICL并以「买家网上保障」名义向买家提供退款服务，并引导用户与冒充客户服务人员的骗徒进行WhatsApp对话；该伪冒网站连结末端可能有多种组合（例如 refund-fps.ink/registered/?uuid=refund）。HKICL强调该网站与其本身及旗下业务并无任何关系，HKICL在一般情况下不会直接向公众个别人士提供转数快（FPS）服务或主动联络公众；官方网址为 www.hkicl.com.hk 及 fps.hkicl.com.hk。公众如有怀疑可致电HKICL热线2533 1111核实，怀疑受骗应尽快报警。同日金管局亦发出有关Mastercard的伪冒网站警示及与银行有关的骗案通知。', None),
         why=T('这是同一套「买家保障／退款」骗术的第N个变体，而且已从伪冒银行与结算机构扩展到卡组织品牌，说明骗徒正沿支付链条逐个环节借用可信名字。对前线而言，客户一旦在搜索或社媒链接里输入保单与身份资料，风险就不再是信息泄露，而是账户被直接操作；把「只在官方渠道核实」变成标准动作，比事后补救便宜得多。', None),
         actions={'front': T('提醒客户只在官方网址与已登记短讯发送人名称下核实交易，勿信搜索或社媒链接中的「买家保障／退款」页面'),
                  'midback': T('把伪冒网站警示纳入客户通知与团队反诈话术库，明确转介核实渠道'),
                  'lead': T('不代客户处理退款或核实身分，一律引导至官方热线与警方渠道，并留痕'),
                  'cross': T('内地与跨境客户经WhatsApp或社媒接触「客服」的风险相同，须提示官方核实路径')},
         rolesImpact={'front': 3, 'midback': 2, 'lead': 2, 'cross': 2},
         source={'sc': '香港金融管理局代香港银行同业结算有限公司发出警示（2026-09-30 17:05）[EN原文]',
                 'tc': '香港金融管理局代香港銀行同業結算有限公司發出警示（2026-09-30 17:05）[EN原文]', 'lang': 'en'},
         boards=['reg', 'tech'], themes=['fraud', 'compliance'],
         tags=tg('伪冒网站', 'HKICL', '转数快', '骗案警示', '客户教育', 'WhatsApp冒充'),
         originalUrl='https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/09/20260930-10/'),

    item(id='nfra-work-safety-liability-accident-prevention-2026-20260929', score=86, verifyStatus='verified',
         sourceTier='official', sourceKey='nfra', contentKind='circular',
         publishedAt='2026-09-29',
         title=T('应急管理部、金融监管总局、国家矿山安监局联合发文（应急厅函〔2026〕352号）：2026年精准开展安责险事故预防服务，要求年底前高危行业投保覆盖率达100%、防止低价与虚假投保',
                 '應急管理部、金融監管總局、國家礦山安監局聯合發文（應急廳函〔2026〕352號）：2026年精準開展安責險事故預防服務，要求年底前高危行業投保覆蓋率達100%、防止低價與虛假投保'),
         summary=T('应急管理部办公厅、金融监管总局办公厅及国家矿山安监局综合司于2026年9月29日联合印发《关于2026年精准开展安责险事故预防服务 助力重点高危行业领域企业提升安全生产管理水平的通知》（应急厅函〔2026〕352号）。通知要求对矿山、危险化学品、烟花爆竹、金属冶炼等重点高危行业领域实行「应保尽保」：应急管理与矿山安全监管部门须全面摸排应投保安责险企业底数并建立动态更新台账、向保险行业共享，依法查处应投保未投保、未全员投保、未足额投保，确保今年年底前上述行业投保覆盖率达100%；同时指导企业合理确定保障额度，防止高风险企业为节省成本低价投保、虚假投保。承保保险机构须加大事故预防费用投入、制定年度预算目标并确保投入到位，按《安全生产责任保险事故预防服务规范》系列标准开展针对性服务，包括协助研发推广安全新装备新技术、反「三违」培训、安全诊断与重大事故隐患自查自改、标准化建设等，并强调跨部门协同与资金渠道统筹。', None),
         why=T('这是安责险从「买保单」走向「管风险」的年度抓手：一端是投保覆盖率硬指标到100%，另一端是要求承保机构把事故预防费用真正投出去、按标准做服务。对理解内地责任险的走势有直接价值——覆盖面被行政目标推高，服务能力与留痕质量就成为能否续保与定价分层的分水岭，也意味着「低价投保」这条路被监管点名封堵。', None),
         actions={'front': T('客户问及内地安责险或雇主类责任险时，说明其为依法强制投保范畴，不代答免赔与核保个案'),
                  'midback': T('把事故预防服务标准与费用投入要求列入内地责任险客户的年度服务与续保流程'),
                  'lead': T('引用须标注为应急管理部与金融监管总局联合通知（应急厅函〔2026〕352号），并注明适用行业'),
                  'cross': T('涉内地高危行业客户的保险安排须按属地法规与监管口径个案确认')},
         rolesImpact={'front': 1, 'midback': 3, 'lead': 2, 'cross': 1},
         source={'sc': '应急管理部办公厅、金融监管总局办公厅、国家矿山安监局综合司 应急厅函〔2026〕352号（2026-09-29）',
                 'tc': '應急管理部辦公廳、金融監管總局辦公廳、國家礦山安監局綜合司 應急廳函〔2026〕352號（2026-09-29）', 'lang': 'zh'},
         boards=['insurer', 'reg'], themes=['reg', 'uw'],
         tags=tg('安责险', '事故预防服务', '应急管理部', '高危行业', '应保尽保', '责任险'),
         originalUrl='https://www.nfra.gov.cn/cn/view/pages/ItemDetail.html?docId=1273761&itemId=4216'),

    # ======================= 媒体 / 市场 =======================
    item(id='insurancebusinessmag-kpmg-ai-insurance-transformation-20260930', score=68, verifyStatus='verified',
         sourceTier='media', sourceKey='insurancebusinessmag', contentKind='report',
         publishedAt='2026-09-30T09:10:00+08:00',
         title=T('毕马威《释放保险业AI价值》：44%受访保险机构自评AI转型前四分之一、无人自认大幅落后，但没有任何一家围绕AI重建销售分销或核保，保单服务与理赔仅3% [EN原文]',
                 '畢馬威《釋放保險業AI價值》：44%受訪保險機構自評AI轉型前四分之一、無人自認大幅落後，但沒有任何一家圍繞AI重建銷售分銷或核保，保單服務與理賠僅3% [EN原文]'),
         summary=T('Insurance Business Asia 9月30日报道毕马威国际报告《Unlocking AI value in insurance》：44%受访者把自身机构列入AI转型前四分之一，且无人认为显著落后；然而受访机构中没有任何一家已围绕AI完全重新设计销售与分销或核保流程，在保单服务或理赔环节做到这一点的仅3%。77%认为若不重构企业架构以配合AI，五年内竞争力将受损；68%认为行动太慢的风险大于过快。71%主要用AI做内容生成与例行任务自动化，29%以AI代理或自动化运行端到端流程；92%称AI有助提升生产力与降低营运成本，仅25%用它开发新产品与服务增收。接近一半AI预算投放于营运与后台效率，新产品与收入模式仅占5%至10%；仅11%对AI投资回报有非常清晰的看法。数据基础与治理「已准备好」的仅11%；54%提供有效AI培训，但仅8%认为员工高度熟练；45%由科技主管拥有AI主导权，15%已把AI治理完全纳入策略规划。至2029年，72%预期核保将转为混合模式、人手减少且角色重新设计，36%预期理赔、33%预期保单服务出现显著职位削减。', None),
         why=T('这份报告的价值在于把「AI采用」与「AI转型」分开：机构自评很高，但真正被重建的是后台流程，而不是面向渠道与客户的分销与核保。对前线与团队复制而言，这解释了一个现实——短期内承保端的分销、报价与出单仍以人工为主，代理与经纪的差异化空间还在人对人的环节；但2029年的混合核保预期意味着，拥有干净数据与可对接系统的团队会先受益。这是做AI培训与流程改造时最值得引用的现状基线。', None),
         actions={'front': T('客户问AI会否取代顾问时，可引用核保流程短期仍以人工为主、信任与传承环节仍靠人对人'),
                  'midback': T('把「数据质量与系统可对接性」列为团队AI落地的前置条件，而非先买工具'),
                  'lead': T('引用须标注为毕马威国际报告及其调查口径（20国、500人以上机构、2026年5月），勿引申为监管要求'),
                  'cross': T('跨境团队若两地并行，须注意两地在数据、模型与AI治理要求上的差异')},
         rolesImpact={'front': 2, 'midback': 3, 'lead': 3, 'cross': 1},
         source={'sc': 'Insurance Business Asia（引述毕马威国际《Unlocking AI value in insurance》）2026-09-30 [EN原文]',
                 'tc': 'Insurance Business Asia（引述畢馬威國際《Unlocking AI value in insurance》）2026-09-30 [EN原文]', 'lang': 'en'},
         boards=['tech'], themes=['ai', 'distribution', 'ai-governance'],
         tags=tg('毕马威', 'AI转型', '分销', '核保', '数据治理', '投资回报'),
         originalUrl='https://www.insurancebusinessmag.com/asia/news/technology/insurers-rate-themselves-ai-leaders-but-none-has-rebuilt-distribution-around-it--kpmg-591693.aspx'),

    item(id='scmp-capco-wealth-management-ai-headcount-20260930', score=66, verifyStatus='verified',
         sourceTier='media', sourceKey='scmp', contentKind='news',
         publishedAt='2026-09-30T07:00:00+08:00',
         title=T('南华早报：Capco研究指香港财富管理资产去年增24%至12.9万亿港元，但私人银行人手仅增2.2%（9,920人增至10,140人）——AI提升人均产能，顾问角色转向传承与复杂决策 [EN原文]',
                 '南華早報：Capco研究指香港財富管理資產去年增24%至12.9萬億港元，但私人銀行人手僅增2.2%（9,920人增至10,140人）——AI提升人均產能，顧問角色轉向傳承與複雜決策 [EN原文]'),
         summary=T('南华早报9月30日报道：咨询机构Capco研究显示，香港金融机构管理的资产去年达42.2万亿港元（约5.38万亿美元），按年增20%，其中私人银行与家族办公室资产增24%至12.9万亿港元，是主要增长动力；但同期私人银行业人手仅增2.2%，由2024年的9,920人增至去年的10,140人。Capco亚太区保险及财富主管Simon Smallcombe表示，私人银行与财富管理公司近年采用包括AI在内的科技工具，令银行家减少行政工作，因此可在人手不大幅增加下支持资产增长，趋势料将持续。他强调AI不会取代从业员：客户可能用AI搜寻简单资讯，但在传承规划或复杂投资决策时，仍会找可信任的人；关系经理的角色会因科技释放时间而扩展至传承规划等领域，客户期望亦因网购与外卖的即时体验而提高。他并提到汇丰宣布在新加坡增聘关系经理同时加大AI投资。', None),
         why=T('这条把「AI替代」的讨论拉回可验证的数字：资产增24%、人手增2.2%，说明生产力提升已经发生，但被替代的是行政与检索，而不是信任与复杂决策。对IFA与高客服务而言，这是最有力的自我定位依据——传承规划与跨代安排正是AI难以接管的部分，也是顾问角色扩张的方向；同时也提示团队要主动用AI把行政时间释放出来，否则人均产出会被同业拉开差距。', None),
         actions={'front': T('与客户谈AI时，把重点放在「行政由AI处理、传承与复杂决策仍由人负责」的定位，不作收益承诺'),
                  'midback': T('把行政流程AI化列为产能提升项目，量化释放出的客户面谈时间'),
                  'lead': T('引用Capco研究与证监会资产数据须标明来源、年份与口径，勿混用自家业绩'),
                  'cross': T('区域比较（新加坡与香港的人手与资产增长）涉及跨境人才与监管环境差异，须注明属地')},
         rolesImpact={'front': 2, 'midback': 3, 'lead': 2, 'cross': 1},
         source={'sc': '南华早报（SCMP）2026-09-30 07:00 [EN原文]', 'tc': '南華早報（SCMP）2026-09-30 07:00 [EN原文]', 'lang': 'en'},
         boards=['market', 'tech'], themes=['ai', 'talent', 'market'],
         tags=tg('Capco', '私人银行', '家族办公室', '人均产能', '传承规划', '关系经理'),
         originalUrl='https://www.scmp.com/business/banking-finance/article/3369160/ai-uptake-sees-wealth-management-headcounts-hong-kong-trail-growth-assets'),

    item(id='scmp-grant-thornton-hk-boards-ai-cyber-skills-20260930', score=64, verifyStatus='verified',
         sourceTier='media', sourceKey='scmp', contentKind='report',
         publishedAt='2026-09-30T08:00:00+08:00',
         title=T('南华早报：均富第15份企业管治报告指香港大型上市公司董事会严重缺乏科技专才——具备网络安全的董事仅0.56%、AI专才0.26%，59%视网安或AI为主要业务风险但仅11%设专责董事委员会 [EN原文]',
                 '南華早報：均富第15份企業管治報告指香港大型上市公司董事會嚴重缺乏科技專才——具備網絡安全的董事僅0.56%、AI專才0.26%，59%視網安或AI為主要業務風險但僅11%設專責董事委員會 [EN原文]'),
         summary=T('南华早报9月30日报道：均富香港（Grant Thornton Hong Kong）第15份年度企业管治报告调查恒生综合指数100家主要上市公司，发现董事会科技专才严重不足——具备网络安全专长的董事仅占0.56%，具备AI专才者仅0.26%，两者合计不足1%；59%企业视网络安全或AI为主要业务风险，但仅11%设立专责董事委员会监督数字威胁与技术整合。报告指香港董事会大多仍为「资本配置与传统风险」时代而设，未能应对自主AI系统与日益复杂的网络威胁；37%董事席位仍由金融、会计、商业及经济背景人士担任，近三分之二大型企业董事会无任何具备资讯科技或网络安全背景的董事。同时董事会正加速换血以配合港交所引入的独立非执行董事九年硬性任期上限：独立非执行董事平均任期由2025年的6.8年降至2026年的5.8年；女性董事比例微升至22%，仍低于欧洲34%至40%的基准。均富建议企业把握即将到来的董事更替引进数码人才。', None),
         why=T('这份调查揭示了一个结构性缺口：企业已把AI与网安列为头号风险，却没有把相应的专业能力放进决策层。对保险与财富管理而言，客户（尤其上市公司高管与家办）在治理与传承安排上会出现新的顾问需求——不只是保单配置，而是风险治理与董事层能力建设的对话；对团队自身，这也提示「AI治理」正在成为可出售的专业能力，而不只是内部效率工具。', None),
         actions={'front': T('与企业客户谈风险时，可引用治理缺口作为对话切入点，但须说明为第三方调查结论、非监管要求'),
                  'midback': T('把AI与网安治理能力列入企业客户与家办的增值服务议题清单'),
                  'lead': T('引用须标注为均富香港企业管治报告及其样本（恒生综合指数100家），并注明年份'),
                  'cross': T('董事任期上限与女性董事比例属港交所口径，跨境上市客户须按相关市场规则另议')},
         rolesImpact={'front': 1, 'midback': 2, 'lead': 3, 'cross': 1},
         source={'sc': '南华早报（SCMP）2026-09-30 08:00 [EN原文]', 'tc': '南華早報（SCMP）2026-09-30 08:00 [EN原文]', 'lang': 'en'},
         boards=['market', 'tech'], themes=['ai', 'ai-governance', 'talent'],
         tags=tg('企业管治', '均富', 'AI治理', '网络安全', '董事会', '独立非执行董事'),
         originalUrl='https://www.scmp.com/business/companies/article/3369229/hong-kongs-executives-are-ill-prepared-ai-era-report-finds'),

    item(id='insuranceasia-prudential-singapore-critical-illness-poll-20260930', score=62, verifyStatus='verified',
         sourceTier='media', sourceKey='insuranceasia', contentKind='news',
         publishedAt='2026-09-30T06:00:00+08:00',
         title=T('保诚新加坡调查：仅29%新加坡人有足够储蓄应付逾一年的危疾康复期，59%已购危疾计划但仅20%有信心保障足够，64%估计需要逾20万新元 [EN原文]',
                 '保誠新加坡調查：僅29%新加坡人有足夠儲蓄應付逾一年的危疾康復期，59%已購危疾計劃但僅20%有信心保障足夠，64%估計需要逾20萬新元 [EN原文]'),
         summary=T('Insurance Asia 9月30日报道保诚新加坡于2026年6月至7月访问1,000名新加坡成年人的调查：67%预期严重阶段危疾的康复期超过一年，但仅29%表示若失去收入，储蓄可应付家庭开支一年以上；59%持有危疾计划，但仅20%有信心保障足以支撑整段康复期。64%估计应付严重阶段危疾的财务影响需要逾20万新元（约15.6万美元）；46%最担心医疗开支，34%担心失去收入，31%担心成为家人负担。若康复期间资金耗尽，53%会动用应急储备、40%动用退休储蓄、33%出售投资、24%会比原计划提早复工；88%认为一笔过赔偿对管理康复期的照顾开支与收入损失很重要。保诚新加坡首席健康及保障总监Manu Tandon指，缩窄保障缺口需要消费者评估自身保障是否足以支撑整个「健康缺口期」。', None),
         why=T('这组数字把「有保单」与「保障足够」之间的落差量化了：近六成人有危疾计划，却只有两成有信心够用，而多数人要到耗尽资金时才动用退休储备或变卖投资——这是最典型的保障缺口叙事，也是危疾保额讨论的现成素材。对前线而言，把对话从「买不买」推进到「够不够、缺口期多长、钱从哪来」，比强调产品功能更贴近客户真实的恐惧点。', None),
         actions={'front': T('与客户检视危疾保额时，以「康复期长短＋失去收入后的现金流」切入，只讲保障功能、不作赔付承诺'),
                  'midback': T('把「健康缺口期」概念纳入危疾保额需求测算的沟通框架'),
                  'lead': T('引用须标注为保诚新加坡调查及其样本与时间，属市场教育信息、非产品推介'),
                  'cross': T('调查为新加坡市场口径，引用至香港或其他市场时须注明差异，不可直接套用比例')},
         rolesImpact={'front': 3, 'midback': 2, 'lead': 1, 'cross': 1},
         source={'sc': 'Insurance Asia（引述保诚新加坡调查）2026-09-30 [EN原文]', 'tc': 'Insurance Asia（引述保誠新加坡調查）2026-09-30 [EN原文]', 'lang': 'en'},
         boards=['product'], themes=['health', 'product'],
         tags=tg('危疾保障', '健康缺口期', '保障缺口', '一笔过赔偿', '退休储蓄', '市场调查'),
         originalUrl='https://insuranceasia.com/insurance/news/only-20-singaporeans-confident-their-critical-illness-coverage-poll'),

    item(id='insuranceasia-japan-premium-share-allianz-20260930', score=60, verifyStatus='pending',
         sourceTier='media', sourceKey='insuranceasia', contentKind='report',
         publishedAt='2026-09-30T05:00:00+08:00',
         title=T('安联预测：日本保险市场增速将落后亚洲多数市场，全球保费份额由2025年的3.9%降至2036年的3.0%；估计日本年均增长财险2.5%、寿险2.9% [EN原文]',
                 '安聯預測：日本保險市場增速將落後亞洲多數市場，全球保費份額由2025年的3.9%降至2036年的3.0%；估計日本年均增長財險2.5%、壽險2.9% [EN原文]'),
         summary=T('Insurance Asia 9月30日报道：安联预期日本保险市场增长将慢于亚洲大部分市场，其全球保费份额将由2025年的3.9%下降至2036年的3.0%；安联并估计日本财险年均增长约2.5%、寿险年均增长约2.9%。报道指日本作为成熟市场，保费增长受人口结构老化、本地市场趋于饱和等因素影响，份额下降主要来自其他亚洲市场增长更快而非日本市场收缩。（本条据 RSS 摘要导读，尚未逐句核对原文，细节待复核。）', None),
         why=T('这条提供的是亚洲保险版图的中期基准：成熟市场（日本）份额下滑，反映的是新兴市场增速更快，而不是日本绝对规模萎缩。对关注区域配置与承保能力布局的读者，这类份额预测是判断「增量在哪里、竞争会从哪个市场溢出」的参照；也提示以日本经验类比香港时，须注意人口与市场成熟度的差异。', None),
         actions={'front': T('客户问及区域市场比较时，可引用份额趋势作背景，但须说明为第三方预测、非投资建议'),
                  'midback': T('把亚洲各市场份额预测列入区域业务与产品引入的年度背景资料'),
                  'lead': T('引用一律标注为安联预测及年份区间，并注明份额与绝对规模口径不同'),
                  'cross': T('各市场份额比较涉及不同监管与税制环境，跨境引用须注明属地差异')},
         rolesImpact={'front': 0, 'midback': 2, 'lead': 2, 'cross': 1},
         source={'sc': 'Insurance Asia（引述安联预测）2026-09-30 [EN原文，待核原文]',
                 'tc': 'Insurance Asia（引述安聯預測）2026-09-30 [EN原文，待核原文]', 'lang': 'en'},
         boards=['market'], themes=['market', 'macro'],
         tags=tg('日本保险市场', '安联', '保费份额', '亚洲市场', '增长预测'),
         originalUrl='https://insuranceasia.com/insurance/in-focus/japan-insurance-share-set-fall-3-2036'),

    item(id='insuranceasianews-marsh-asean-ceo-singapore-20260930', score=58, verifyStatus='pending',
         sourceTier='media', sourceKey='insuranceasianews', contentKind='news',
         publishedAt='2026-09-30T14:51:00+08:00',
         title=T('Marsh擢升泰国Derek Heng为东盟区行政总裁，新加坡由Peta Latimer掌舵 [EN原文]',
                 'Marsh擢升泰國Derek Heng為東盟區行政總裁，新加坡由Peta Latimer掌舵 [EN原文]'),
         summary=T('InsuranceAsia News 9月30日报道：保险经纪Marsh把泰国业务的Derek Heng擢升为东盟区行政总裁，新加坡业务则由Peta Latimer掌舵，属其东南亚区域管理架构的调整。报道未披露更多细节。（本条据标题与摘要导读，原文为订户内容，细节待复核。）', None),
         why=T('区域人事调整往往先于业务重心变化：东盟层面的统一管理与新加坡的独立掌舵，说明东南亚被拆成「区域统筹＋枢纽城市」两层来经营。对关注区域承保与经纪能力流向的读者，这类变动是判断服务网络覆盖与资源投放的先行指标。', None),
         actions={'front': T('客户问及区域服务网络时，只说明公开的人事安排，不代述服务承诺或对接承诺'),
                  'midback': T('把主要经纪与保司的东盟管理层变动列入区域服务能力观察'),
                  'lead': T('引用须标注为媒体公开报道，勿据此推断任何合作或业务安排'),
                  'cross': T('东盟各市场分销与牌照要求不同，客户涉当地业务须按属地规则个案确认')},
         rolesImpact={'front': 0, 'midback': 1, 'lead': 1, 'cross': 1},
         source={'sc': 'InsuranceAsia News 2026-09-30 [EN原文，待核原文]', 'tc': 'InsuranceAsia News 2026-09-30 [EN原文，待核原文]', 'lang': 'en'},
         boards=['insurer'], themes=['talent', 'career'],
         tags=tg('Marsh', '东盟', '人事任命', '东南亚', '经纪网络'),
         originalUrl='https://insuranceasianews.com/marsh-promotes-thailands-derek-heng-to-asean-ceo-peta-latimer-takes-singapore-helm/'),

    item(id='insuranceasianews-australian-regulator-2026-27-priorities-20260930', score=64, verifyStatus='pending',
         sourceTier='media', sourceKey='insuranceasianews', contentKind='news',
         publishedAt='2026-09-30T12:49:00+08:00',
         title=T('澳洲监管机构公布2026-27年度保险监管优先事项：点名「灾难追逐者」并预告行业实务守则全面检讨 [EN原文]',
                 '澳洲監管機構公布2026-27年度保險監管優先事項：點名「災難追逐者」並預告行業實務守則全面檢討 [EN原文]'),
         summary=T('InsuranceAsia News 9月30日报道：澳洲监管机构公布2026-27年度保险监管优先事项，其中包括点名所谓「灾难追逐者」（disaster chasers）问题，以及预告对行业实务守则（code of practice）进行全面检讨。报道未在公开摘要中披露更多细节。（本条据标题与公开摘要导读，原文为订户内容，细节待复核。）', None),
         why=T('监管年度优先事项是观察执法风向最省力的窗口：把「灾难追逐者」与实务守则检讨并列为优先事项，意味着灾后理赔与中介行为将是下一轮检查重点。香港在极端天气与理赔争议上的关注点与之同源，这类跨境监管动向可作为预案演练的参照。', None),
         actions={'front': T('客户问及灾后理赔或中介行为规范时，只说明监管关注方向，不代答个案赔与不赔'),
                  'midback': T('把灾后理赔流程与记录完整性列入极端天气旺季前的自查项目'),
                  'lead': T('引用须标注为澳洲监管机构优先事项，勿改写为香港监管要求'),
                  'cross': T('各地中介行为与实务守则要求不同，跨境客户须按属地规则个案确认')},
         rolesImpact={'front': 1, 'midback': 2, 'lead': 2, 'cross': 1},
         source={'sc': 'InsuranceAsia News 2026-09-30 [EN原文，待核原文]', 'tc': 'InsuranceAsia News 2026-09-30 [EN原文，待核原文]', 'lang': 'en'},
         boards=['reg'], themes=['reg', 'compliance'],
         tags=tg('澳洲监管', '监管优先事项', '灾难追逐者', '实务守则', '灾后理赔'),
         originalUrl='https://insuranceasianews.com/australian-regulator-flags-disaster-chasers-code-of-practice-overhaul-as-2026-27-insurance-priorities/'),

    item(id='artemis-pioneer-cat-bond-fund-grows-2026-20260930', score=60, verifyStatus='verified',
         sourceTier='media', sourceKey='artemis', contentKind='news',
         publishedAt='2026-09-30T16:00:00+08:00',
         title=T('Artemis：Victory Pioneer巨灾债基金年内增逾10亿美元至27.6亿美元AUM，私募ILS间隔基金升至8.98亿美元（2022年一季度以来最大）；两基金年内合计增约46% [EN原文]',
                 'Artemis：Victory Pioneer巨災債基金年內增逾10億美元至27.6億美元AUM，私募ILS間隔基金升至8.98億美元（2022年一季度以來最大）；兩基金年內合計增約46% [EN原文]'),
         summary=T('Artemis 9月30日报道：Victory Pioneer巨灾债基金2026年至今已增长逾10亿美元资产，本月策略规模达27.6亿美元（2025年底为17.4亿美元，其中逾半增长来自6月之后）；同期Victory Pioneer ILS间隔基金规模增至8.98亿美元（2025年底约7.6亿美元），为至少2022年一季度以来最大规模。截至7月31日，该间隔基金约62%资产投资于再保险sidecar，19.5%为抵押再保，14%为巨灾债。Pioneer Investments团队管理的两只共同ILS基金策略年内资产增长约46%，合计约36.6亿美元；连同机构ILS策略及多资产基金的ILS资产，整体巨灾债与ILS管理规模维持在约50亿美元水平。报道指这反映投资者对巨灾债及更偏私募的再保与sidecar策略兴趣上升。', None),
         why=T('资金端的规模变化先于费率变化：巨灾债基金年内增逾10亿美元、私募ILS基金回到2022年以来最大规模，说明在回报仍然可观、又无重大灾损的窗口里，资本正加速流入再保风险转移。对理解财产险与再保定价条件有直接意义——资本越充裕，费率与条款压力越大；而一旦大灾发生，这条链会迅速反向。', None),
         actions={'front': T('客户问及ILS或再保相关资产时，须说明这属公开基金规模数据、非任何产品的回报承诺'),
                  'midback': T('把ILS基金规模与资本流入列入再保定价与财产险条件的季度观察'),
                  'lead': T('引用一律标注来源（Artemis.bm）与时间点，避免与自家产品的资产规模混用'),
                  'cross': T('ILS与sidecar属专业投资者范畴，跨境客户的参与资格与分销限制按属地规则处理')},
         rolesImpact={'front': 0, 'midback': 2, 'lead': 2, 'cross': 1},
         source={'sc': 'Artemis.bm 2026-09-30 [EN原文]', 'tc': 'Artemis.bm 2026-09-30 [EN原文]', 'lang': 'en'},
         boards=['market'], themes=['ils', 'market', 'catastrophe'],
         tags=tg('巨灾债', 'ILS基金', 'Pioneer', 'sidecar', '再保资本', '私募ILS'),
         originalUrl='https://www.artemis.bm/news/pioneer-cat-bond-fund-grows-by-more-than-1bn-in-2026-to-reach-2-76bn-aum/'),
]


def main():
    path = os.path.join(BASE, 'data', 'live-items.json')
    data = json.load(open(path, encoding='utf-8'))
    existing = {it.get('id') for it in data['items']}
    new = [it for it in NEW if it['id'] not in existing]
    dup = [it['id'] for it in NEW if it['id'] in existing]
    if dup:
        print('跳过已存在:', dup)
    new.sort(key=lambda x: x['publishedAt'], reverse=True)
    data['items'] = new + data['items']
    data['meta']['generatedAt'] = NOW
    data['meta']['itemCount'] = len(data['items'])
    n = len(data['items'])
    data['meta']['windowNote'] = {'sc': f'本库{n}条。', 'tc': f'本庫{n}條。'}
    shutil.copy(path, os.path.join(BASE, 'data/live-items.json.bak-0930-1808'))
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print(f'写入完成: 新增 {len(new)} 条, 合计 {n} 条')
    for it in new:
        print(' +', it['publishedAt'], it['id'])


if __name__ == '__main__':
    main()
