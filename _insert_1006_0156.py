# -*- coding: utf-8 -*-
"""1006 0156 增量采集插入脚本：30 条（覆盖 10/5-10/6）"""
import json, datetime, shutil, os
from zhconv import convert

TZ = datetime.timezone(datetime.timedelta(hours=8))
NOW = datetime.datetime.now(TZ)
NOW_ISO = NOW.strftime('%Y-%m-%dT%H:%M:%S+08:00')

def to_tc(o):
    if isinstance(o, str):
        return convert(o, 'zh-hant')
    if isinstance(o, dict):
        out = {}
        for k, v in o.items():
            if k == 'lang' or isinstance(v, bool):
                out[k] = v
            else:
                out[k] = to_tc(v)
        return out
    if isinstance(o, list):
        return [to_tc(x) for x in o]
    return o

def bi(sc, tc):
    return {'sc': sc, 'tc': tc}

def mk(iid, skey, tier, score, kind, pub, url, title, summary, why, boards, themes,
       tags, actions, roles, src_label, lang='en', verify='pending'):
    it = {
        'clusterCount': 1,
        'score': score,
        'verifyStatus': verify,
        'sourceTier': tier,
        'contentKind': kind,
        'actions': actions,
        'rolesImpact': roles,
        'boards': boards,
        'themes': themes,
        'tags': bi(tags, tags),
        'contentRole': bi('本站导读', '本站导读'),
        'featured': False,
        'evergreen': False,
        'ingestedAt': NOW_ISO,
        'id': iid,
        'sourceKey': skey,
        'publishedAt': pub,
        'originalUrl': url,
        'title': bi(title, title),
        'summary': bi(summary, summary),
        'why': bi(why, why),
        'source': bi(src_label, src_label),
        'source': {'sc': src_label, 'tc': src_label, 'lang': lang},
    }
    # 生成繁体
    for k in ('title', 'summary', 'why', 'tags', 'actions', 'contentRole'):
        it[k] = to_tc(it[k]) if k != 'tags' else it[k]
    it['title'] = to_tc(it['title']) if isinstance(it['title'], str) else it['title']
    return it

def A(front, midback, lead, cross):
    return {'front': bi(front, front), 'midback': bi(midback, midback),
            'lead': bi(lead, lead), 'cross': bi(cross, cross)}

def R(a=1, b=2, c=2, d=1):
    return {'front': a, 'midback': b, 'lead': c, 'cross': d}

RAW = []

def add(*args, **kw):
    RAW.append((args, kw))

# ---------------- HKMA (official) ----------------
add('hkma-bakai-bank-restricted-licence-20261005', 'hkma', 'official', 86, 'press',
    '2026-10-05',
    'https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/10/20261005-4/',
    '金管局向 BAKAI BANK 批出有限制银行牌照（香港首家中亚银行）',
    '金管局10月5日公布，向 BAKAI BANK Open Joint Stock Company（哈萨克斯坦）批出有限制银行牌照（restricted banking licence），为香港首间来自中亚的持牌银行机构。 [EN原文]',
    '香港作为区域金融枢纽持续引入新市场参与者，中亚资金与跨境结算通道增加，间接有利跨境财富管理与保险资金配置的中介生态；亦可留意金管局批牌取向。',
    ['reg', 'market'], ['hkma', 'licensing', 'banking', 'central-asia', 'market'],
    ['金管局', 'BAKAI BANK', '有限制银行牌照', '中亚', '香港金融'],
    A('客户问及香港金融中心地位时，可引用金管局批出新市场参与者的公开事实，不引申为投资建议',
      '留意新持牌机构的银保/分销合作动向，若涉及保险分销需符合持牌与转介合规要求',
      '把「监管持续扩阔市场参与者」作为香港市场韧性论据之一，用于招募与客户沟通',
      '涉及中亚、跨境资金来源的客户咨询，以公司合规与反洗钱程序为准'),
    R(1, 1, 2, 1), 'HKMA 新闻稿 2026-10-05', 'en', 'pending')

add('hkma-cargox-solution-day-trade-data-20261005', 'hkma', 'official', 85, 'press',
    '2026-10-05',
    'https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/10/20261005-3/',
    '金管局举办 Cargox Solution Day，推动区域贸易数据互联',
    '金管局10月5日举办 Cargox Solution Day，推动区域贸易数据互联互通，属该局贸易融资数据基建工作的一部分。 [EN原文]',
    '贸易数据基建属长期工程，短期对保险销售无直接影响；但对理解「数据互联＋贸易融资＋保险」的跨境风险定价方向有参考价值。',
    ['tech', 'market'], ['hkma', 'trade-finance', 'data', 'infrastructure'],
    ['金管局', 'Cargox', '贸易数据', '贸易融资', '香港'],
    A('客户问及香港金融基建时，以金管局公开通报为据，不作延伸解读',
      '留意贸易数据互联对货运/贸易信用险条款与核保数据来源的潜在影响',
      '作为「香港持续建设金融基建」的公开素材，用于对内培训与对外沟通',
      '跨境贸易客户的风险管理方案仍以公司核保与再保安排为准'),
    R(1, 1, 2, 1), 'HKMA 新闻稿 2026-10-05', 'en', 'pending')

# ---------------- (Re)in Asia (pro) ----------------
add('reinasia-cigna-hk-jay-chan-head-distribution-20261005', 'reinasia', 'pro', 70, 'news',
    '2026-10-05',
    'https://reinasia.com/cigna-healthcare-hong-kong-appoints-jay-chan-as-head-of-distribution/',
    'Cigna Healthcare 香港委任 Jay Chan 为分销主管',
    '(Re)in Asia 10月5日报道：Cigna Healthcare 香港委任 Jay Chan 出任分销主管（head of distribution），负责本地分销渠道管理。 [EN原文]',
    '健康险公司在港换帅分销条线，反映医疗健康险竞争重心在渠道与客户获取；可作为同业组织架构观察点。',
    ['insurer', 'market'], ['hk', 'health-insurance', 'people-move', 'distribution'],
    ['Cigna', '信诺', '香港', '分销', '人事'],
    A('客户问及医疗险市场格局时，只陈述公开人事信息，不与自家产品作优劣比较',
      '留意同业健康险渠道策略变化，作为招募与渠道合作的背景参考',
      '把人事变动作为「健康险在港持续投入」的公开信号，用于团队信心沟通',
      '涉及同业产品比较时以公司合规口径为准，不引用二手评价'),
    R(0, 1, 2, 1), '(Re)in Asia 2026-10-05', 'en', 'pending')

add('reinasia-cpic-hk-liquidity-sp-ratings-20261005', 'reinasia', 'pro', 72, 'news',
    '2026-10-05',
    'https://reinasia.com/cpic-hks-liquidity-improves-on-cut-in-high-risk-assets-as-sp-affirms-ratings/',
    '太保香港：高风险资产占比降至39%，标普确认评级',
    '(Re)in Asia 10月5日报道：标普确认中国太平洋保险（香港）评级，指其流动性因减少高风险资产投资而改善，高风险资产占比降至39%。 [EN原文]',
    '评级机构对在港内地系险企的资本与资产质量观察，是客户问及「公司实力」时的可引用公开资料；也提示资产端风险偏好与分红/偿付能力的关系。',
    ['insurer', 'market'], ['hk', 'ratings', 'capital', 'asset-quality', 'mainland-insurer'],
    ['太保香港', 'CPIC', '标普', '评级', '高风险资产'],
    A('客户问及公司实力时，统一以监管公开数据与官方评级报告为准，不引用未核实市场传言',
      '留意资产端风险偏好变化对分红实现与偿付能力指标的传导，但不作收益预测',
      '把「第三方评级确认」作为合规可引用的证据类型，纳入团队话术白名单',
      '涉及同业评级比较时，只引用原始评级机构报告'),
    R(1, 2, 2, 1), '(Re)in Asia 2026-10-05', 'en', 'pending')

add('reinasia-apac-insurers-prediction-markets-20261005', 'reinasia', 'pro', 70, 'news',
    '2026-10-05',
    'https://reinasia.com/apac-insurers-in-wait-and-watch-mode-for-impact-of-prediction-markets/',
    '亚太险企对预测市场采取「观望」态度',
    '(Re)in Asia 10月5日专题报道：面对预测市场（prediction markets，对事件结果定价的交易平台）近年扩张，亚太区保险公司普遍采取「观望」策略，关注其对风险转移、资本与合规框架的潜在影响。 [EN原文]',
    '新兴风险载体进入保险视野，属前沿观察类信息；对团队的用处是理解「新型风险定价市场」与保险/再保的关系，而非直接业务机会。',
    ['market', 'reg'], ['apac', 'prediction-markets', 'emerging-risk', 'regulation'],
    ['预测市场', '亚太', '保险公司', '新兴风险', '监管'],
    A('客户问及新兴投资/预测平台时，明确说明其非保险产品、不受保险监管保障，不推荐也不贬抑',
      '留意此类平台是否触及公司合规清单中的「不可合作渠道」，需报备',
      '把「新兴风险载体」纳入团队市场认知课，说明与保险的风险转移机制差异',
      '涉及跨境平台与资金出入的咨询，一律转合规处理'),
    R(0, 2, 2, 1), '(Re)in Asia 2026-10-05', 'en', 'pending')

add('reinasia-malaysia-motor-insurance-fraud-doubled-2025-20261005', 'reinasia', 'pro', 68, 'news',
    '2026-10-05',
    'https://reinasia.com/malaysias-reported-motor-insurance-fraud-cases-more-than-doubled-in-2025/',
    '马来西亚举报车险欺诈案件2025年翻倍',
    '(Re)in Asia 10月5日报道：马来西亚2025年举报的汽车保险欺诈案件数量较前一年增加逾一倍，显示车险道德风险与理赔管控压力上升。 [EN原文]',
    '车险欺诈上升是区域理赔管控信号；对香港团队的借鉴意义在于理赔文件核验与客户教育（勿轻信「包赔」中介），与销售端红线自查相呼应。',
    ['insurer', 'market'], ['malaysia', 'motor', 'fraud', 'claims', 'conduct'],
    ['马来西亚', '车险', '保险欺诈', '理赔', '道德风险'],
    A('不向客户承诺任何理赔结果；说明理赔以保单条款与核保结论为准',
      '把欺诈案例纳入理赔沟通培训，强化文件核验与可疑个案上报流程',
      '用区域案例说明行业对欺诈的共同立场，减少「理赔一定宽松」的误解',
      '客户在马来西亚等市场有保单时，以当地保单条款与公司程序为准'),
    R(0, 2, 1, 1), '(Re)in Asia 2026-10-05', 'en', 'pending')

add('reinasia-china-trade-credit-insurance-coverage-20261005', 'reinasia', 'pro', 70, 'news',
    '2026-10-05',
    'https://reinasia.com/china-bats-for-wider-domestic-trade-credit-insurance-coverage/',
    '中国推动扩大国内贸易信用保险覆盖',
    '(Re)in Asia 10月5日报道：中国推动扩大国内贸易信用保险的承保覆盖面，以支持内需与供应链结算风险的转移。 [EN原文]',
    '内地政策方向属「保险服务实体」范畴；对在港团队的意义在于理解客户在内地的贸易应收账款风险，及其与信贷、保理工具的互补关系。',
    ['reg', 'market'], ['china', 'trade-credit', 'policy', 'sme'],
    ['中国', '贸易信用保险', '内地政策', '中小企业', '供应链'],
    A('客户问及内地贸易信用险时，说明其属内地市场产品，香港保单不能替代，须按内地监管与公司渠道办理',
      '把内贸信用险纳入跨境客户的风险敞口盘点清单',
      '作为「保险服务实体经济」的政策案例，用于团队行业理解训练',
      '跨境合规与内地监管要求以公司及持牌人判断为准'),
    R(0, 2, 2, 2), '(Re)in Asia 2026-10-05', 'en', 'pending')

# ---------------- InsuranceAsia News (pro) ----------------
add('ian-daniel-rombach-great-eastern-digital-distribution-20261005', 'insuranceasianews', 'pro', 68, 'news',
    '2026-10-05T22:29:00+08:00',
    'https://insuranceasianews.com/daniel-rombach-joins-great-eastern-as-vp-for-digital-distribution-platforms/',
    'Daniel Rombach 加入 Great Eastern，出任数字分销平台副总裁',
    'InsuranceAsia News 10月5日报道：Daniel Rombach 加入新加坡 Great Eastern，出任数字分销平台副总裁，负责数字化分销渠道建设。 [EN原文]',
    '区域险企持续加码数字分销组织建设，是「渠道数字化」趋势的人事信号；可对照自身团队的线上获客与转介链路。',
    ['insurer', 'market'], ['singapore', 'digital', 'distribution', 'people-move'],
    ['Great Eastern', '数字分销', '人事', '新加坡', '渠道'],
    A('客户问及线上线下服务差异时，说明以公司官方平台与持牌顾问为准，不夸大同业数字化程度',
      '留意数字分销的合规边界（身份核验、电子投保、转介留痕）',
      '把数字化组织建设纳入团队能力发展讨论，评估自身工具缺口',
      '跨境数字渠道涉及数据与隐私要求，按公司合规指引执行'),
    R(0, 2, 2, 1), 'InsuranceAsia News 2026-10-05 22:29', 'en', 'pending')

add('ian-south-korea-natcat-public-schemes-1bn-20261005', 'insuranceasianews', 'pro', 70, 'news',
    '2026-10-05T17:54:00+08:00',
    'https://insuranceasianews.com/south-koreas-nat-cat-claims-under-public-insurance-schemes-top-us1bn-in-2025-korean-re/',
    '韩国公共保险计划巨灾理赔2025年突破10亿美元：Korean Re',
    'InsuranceAsia News 10月5日报道：据 Korean Re，韩国公共保险计划下的自然灾害（nat cat）理赔金额2025年首次突破10亿美元，反映巨灾风险敞口上升。 [EN原文]',
    '巨灾损失上升是区域再保与保险定价的核心变量；对团队的用处是理解「气候变化→理赔→费率」的传导，帮助客户建立合理保障预期。',
    ['market', 'insurer'], ['korea', 'natcat', 'reinsurance', 'climate', 'claims'],
    ['韩国', '巨灾保险', 'Korean Re', '再保险', '气候变化'],
    A('不承诺任何「保障足够」的结论；以客户实际风险敞口与保单限额为基础讨论',
      '把巨灾/极端天气案例纳入保障缺口检视清单（旅游、居所、财产）',
      '用区域数据说明再保与定价压力，帮助团队理解费率环境',
      '涉及气候风险的方案以公司核保与再保安排为准'),
    R(0, 2, 2, 1), 'InsuranceAsia News 2026-10-05 17:54', 'en', 'pending')

add('ian-everest-di-pasquale-apac-financial-lines-20261005', 'insuranceasianews', 'pro', 66, 'news',
    '2026-10-05T11:58:00+08:00',
    'https://insuranceasianews.com/everest-names-adrian-di-pasquale-as-apac-financial-lines-director-for-wholesale-specialty/',
    'Everest 委任 Adrian Di Pasquale 为亚太区金融险总监（批发与专业险）',
    'InsuranceAsia News 10月5日报道：Everest 任命 Adrian Di Pasquale 为亚太区金融险（financial lines）总监，负责批发与专业险业务。 [EN原文]',
    '专业险/金融险（D&O、专业责任等）在亚太持续扩编，属高净值与企业客户的相邻需求；可作为企业客户风险管理的观察点。',
    ['insurer', 'product'], ['apac', 'financial-lines', 'specialty', 'people-move'],
    ['Everest', '亚太', '金融险', '专业责任', '人事'],
    A('企业客户问及 D&O/专业责任时，说明香港市场产品与承保条件须逐案核保，不作概括比较',
      '把专业险纳入企业客户需求盘点清单，识别转介与联合服务机会',
      '用区域承保能力扩张说明专业险市场成熟度，作为团队知识扩充',
      '跨市场承保以公司授权与再保安排为准'),
    R(0, 2, 1, 2), 'InsuranceAsia News 2026-10-05 11:58', 'en', 'pending')

add('ian-regulatory-fragmentation-asia-insurance-20261005', 'insuranceasianews', 'pro', 74, 'news',
    '2026-10-05T11:26:00+08:00',
    'https://insuranceasianews.com/same-asset-different-market-why-regulatory-fragmentation-changes-how-insurance-responds-in-asia/',
    '同一资产、不同市场：监管碎片化如何改变亚洲保险的风险响应',
    'InsuranceAsia News 10月5日分析文章指出：亚洲各市场对同一类资产的监管要求日益分化，令保险方案在承保、资本与合规层面必须按市场分别设计，不能跨境照搬。 [EN原文]',
    '直接对应跨境客户的常见误解——「同一套方案可通行亚洲」；可作为向客户解释跨境保单须按市场合规办理的说明材料。',
    ['reg', 'market'], ['asia', 'regulation', 'crossborder', 'compliance', 'capital'],
    ['亚洲', '监管碎片化', '跨境', '合规', '资本'],
    A('向客户说明跨境保单须各自符合当地法规，不存在「一套方案通吃」；不承诺跨境可比待遇',
      '把「按市场分别评估合规」写入跨境业务前置检查清单',
      '作为跨境业务培训的核心材料，统一团队对监管差异的认知',
      '具体市场准入与销售资格以公司合规意见与持牌人判断为准'),
    R(2, 2, 3, 3), 'InsuranceAsia News 2026-10-05 11:26', 'en', 'pending')

add('ian-marsh-re-parametric-wind-bushfire-apac-20261005', 'insuranceasianews', 'pro', 72, 'news',
    '2026-10-05T07:29:00+08:00',
    'https://insuranceasianews.com/as-apac-risk-transfer-market-opens-up-marsh-re-eyes-parametric-wind-bushfire-cover/',
    '亚太风险转移市场开放：Marsh Re 着眼参数化风灾与山火保障',
    'InsuranceAsia News 10月5日报道：随着亚太风险转移（risk transfer）市场逐步开放，Marsh Re 表示正关注参数化（parametric）风灾与山火保障产品的发展机会。 [EN原文]',
    '参数化保险是「气候风险→快速赔付」的产品方向，对巨灾与业务中断类保障有借鉴意义；可帮助团队向客户解释赔付触发机制与传统保单的差异。',
    ['product', 'market'], ['apac', 'parametric', 'climate', 'reinsurance', 'risk-transfer'],
    ['参数化保险', '亚太', 'Marsh Re', '山火', '风险转移'],
    A('向客户解释参数化产品的赔付以客观指数触发，与传统实损赔偿机制不同，不混同销售',
      '把参数化方案纳入企业客户业务中断保障的备选讨论清单',
      '把「赔付触发机制」纳入产品理解训练，避免术语误用',
      '是否可选参数化方案以公司核保与再保支持为准'),
    R(0, 2, 2, 2), 'InsuranceAsia News 2026-10-05 07:29', 'en', 'pending')

# ---------------- Insurance Business Asia (pro) ----------------
add('ibm-ia-conduct-focus-broker-ro-tenure-20260930', 'insurancebusinessmag', 'pro', 78, 'news',
    '2026-09-30T21:14:00+08:00',
    'https://www.insurancebusinessmag.com/asia/news/breaking-news/broker-leadership-churn-emerges-as-conduct-risk-signal-in-hong-kong-ia-report-591783.aspx',
    '保监局《Conduct in Focus》第13期：经纪公司负责人任期过短被视为操守风险信号',
    'Insurance Business 9月30日报道保监局《Conduct in Focus》第13期：2019年9月至2026年6月共核准3,201名负责人（RO），整体平均在任3.8年；长期业务机构中51.4%的RO任命不足两年，经纪公司RO平均仅2.3年（代理机构3.3年）。保监局视在任超过三年为稳定管理基准，任期过短或反复任命可能指向治理与资源不足，并已对三家经纪公司施加牌照续期条件。 [EN原文]',
    '这是本站最直接的香港监管执法脉络之一：RO任期数据被用作监管工具，说明「人事留任」本身就是合规指标。对经纪/代理团队负责人而言，任期短、频繁更换不仅影响授权与治理，也可能触发实地审查与续期条件；转介费超过佣金50%须额外披露的规定同样在本期中被提及。',
    ['reg', 'market'], ['hk', 'ia', 'conduct', 'broker', 'governance', 'ro'],
    ['保监局', 'Conduct in Focus', '负责人RO', '经纪公司', '转介费', '牌照条件'],
    A('不把「负责人任期」信息用于比较同业或贬损竞争对手，只作内部治理自查参考',
      '自查：RO任命与留任安排是否符合稳定管理预期；转介费是否触及50%披露门槛并留痕',
      '把「任期＝治理指标」纳入负责人与管理层的合规课程，说明续期条件的现实成本',
      '如涉及转介安排或RO变更，先与合规确认再执行'),
    R(2, 3, 3, 2), 'Insurance Business Asia 2026-09-30 21:14', 'en', 'verified')

add('ibm-howden-collins-steps-down-executive-chairman-20261005', 'insurancebusinessmag', 'pro', 70, 'news',
    '2026-10-05T20:49:00+08:00',
    'https://www.insurancebusinessmag.com/asia/news/breaking-news/dominic-collins-to-step-down-as-howdens-executive-chairman-592300.aspx',
    'Howden 执行主席 Dominic Collins 将卸任',
    'Insurance Business 10月5日报道：经纪集团 Howden 执行主席 Dominic Collins 将卸任，属该集团高层人事变动。 [EN原文]',
    '大型经纪集团高层变动常伴随策略与整合节奏调整，对市场渠道格局有间接影响，属行业观察类信息。',
    ['insurer', 'market'], ['broker', 'people-move', 'howden', 'distribution'],
    ['Howden', '经纪', '人事', '管理层'],
    A('客户问及经纪合作方变化时，只陈述公开人事信息，不揣测策略走向',
      '留意大型经纪集团整合对渠道合作条款的间接影响',
      '作为行业格局观察材料，用于团队市场认知更新',
      '渠道合作与佣金安排一律以公司合约与合规要求为准'),
    R(0, 1, 2, 1), 'Insurance Business Asia 2026-10-05 20:49', 'en', 'verified')

add('ibm-mas-nominating-committee-chair-approval-20261006', 'insurancebusinessmag', 'pro', 72, 'news',
    '2026-10-06',
    'https://www.insurancebusinessmag.com/asia/news/breaking-news/mas-moves-to-approve-who-chairs-insurer-nominating-committees-592336.aspx',
    '新加坡金管局拟审批保险公司提名委员会主席人选',
    'Insurance Business 10月6日报道：新加坡金融管理局（MAS）拟要求就保险公司提名委员会主席人选取得其审批，收紧对承保人董事会治理的直接介入。 [EN原文]',
    '区域监管持续把治理（董事会、提名、独立性）纳入审慎监管范围，与香港对RO任期与治理的关注方向一致；对理解「治理即合规」的地区趋势有帮助。',
    ['reg', 'market'], ['singapore', 'mas', 'governance', 'board', 'regulation'],
    ['MAS', '新加坡', '提名委员会', '公司治理', '保险公司'],
    A('客户问及公司治理时，说明治理要求属监管制度安排，不代表对个体公司的评价',
      '把治理要求纳入管理层合规学习清单（董事会/委员会/独立性）',
      '用区域监管对照说明「治理趋严」是共同方向，强化团队合规意识',
      '涉及具体公司治理判断以监管公开文件为准'),
    R(1, 2, 3, 2), 'Insurance Business Asia 2026-10-06', 'en', 'pending')

add('ibm-cambodia-bancassurance-squeezes-brokers-20261006', 'insurancebusinessmag', 'pro', 68, 'news',
    '2026-10-06',
    'https://www.insurancebusinessmag.com/asia/news/life-insurance/cambodia-bancassurance-deals-squeeze-out-independent-brokers-592348.aspx',
    '柬埔寨银保独家协议挤压独立经纪生存空间',
    'Insurance Business 10月6日报道：柬埔寨银行保险（bancassurance）独家协议令独立保险经纪渠道被挤出市场，渠道结构进一步向银行集中。 [EN原文]',
    '渠道集中化是新兴市场常见风险；对香港团队的启示是「渠道依赖度」本身就是经营风险，需评估自身获客渠道的集中与替代性。',
    ['market', 'insurer'], ['cambodia', 'bancassurance', 'broker', 'distribution'],
    ['柬埔寨', '银行保险', '经纪', '渠道集中', '新兴市场'],
    A('不评价个别市场渠道优劣；说明渠道结构差异不影响保单条款与客户权益',
      '把「渠道集中度」纳入自身业务风险评估，检视获客来源单一化风险',
      '用区域案例说明渠道结构演变，作为团队经营意识训练',
      '跨境渠道合作须符合当地牌照与公司合规要求'),
    R(0, 2, 2, 1), 'Insurance Business Asia 2026-10-06', 'en', 'pending')

add('ibm-japan-fsa-prudential-life-parent-20261006', 'insurancebusinessmag', 'pro', 72, 'news',
    '2026-10-06',
    'https://www.insurancebusinessmag.com/asia/news/life-insurance/japans-fsa-moves-against-prudential-life--and-the-parent-company-above-it-592352.aspx',
    '日本金融厅对保德信生命的行动延伸至其母公司层面',
    'Insurance Business 10月6日报道：日本金融厅（FSA）就日本保德信生命保险的不当销售事件采取行动，并进一步触及母公司层面，凸显监管对集团治理与总部责任的追问。 [EN原文]',
    '与本站早前条目（10月4日业务停止令）互为延伸：监管关注点从「个别员工行为」上升到「母公司治理与问责」。提醒团队，销售端红线事件的最终成本会回溯至集团层面。',
    ['reg', 'insurer'], ['japan', 'fsa', 'prudential-life', 'conduct', 'group-governance'],
    ['日本金融厅', '保德信生命', '母公司问责', '不当销售', '集团治理'],
    A('厘清主体：美国保德信金融集团/日本保德信生命与香港保诚（Prudential plc）无股权关系，不可混同',
      '把「上级问责」逻辑纳入销售行为红线培训：个人违规的成本由机构承担',
      '用案例说明监管对集团治理的追问方式，提升管理层风险意识',
      '涉及境外主体与保单的咨询，以官方公告与公司合规意见为准'),
    R(1, 2, 3, 1), 'Insurance Business Asia 2026-10-06', 'en', 'pending')

add('ibm-life-sciences-risk-coverage-shift-20261005', 'insurancebusinessmag', 'pro', 66, 'news',
    '2026-10-05',
    'https://www.insurancebusinessmag.com/asia/news/breaking-news/life-sciences-risk-is-shifting-and-coverage-may-not-follow-592256.aspx',
    '生命科学风险正在位移，保障未必跟得上',
    'Insurance Business 10月5日报道/分析：生命科学行业（药械、临床与生物科技）的风险结构正在变化，但现有保险保障未必同步覆盖，形成新的保障缺口。 [EN原文]',
    '保障缺口类议题对高净值与科创背景客户有直接价值：可借「新兴行业风险 vs 现有条款」切入需求检视，而非直接推销。',
    ['product', 'market'], ['life-sciences', 'protection-gap', 'product', 'emerging-risk'],
    ['生命科学', '保障缺口', '产品设计', '新兴风险'],
    A('向科创/医药背景客户做需求访谈时，先问风险与责任结构，不预设产品',
      '把「新兴行业保障缺口」纳入高客需求检视清单，必要时联合核保评估',
      '作为保障缺口教学案例，训练团队从行业风险出发做需求分析',
      '承保可行性以公司核保意见为准，不承诺可保性'),
    R(1, 2, 2, 2), 'Insurance Business Asia 2026-10-05', 'en', 'pending')

# ---------------- Artemis (pro) ----------------
add('artemis-picc-great-wall-re-cat-bond-2-20261005', 'artemis', 'pro', 72, 'news',
    '2026-10-05',
    'https://www.artemis.bm/news/picc-pc-appears-to-have-returned-for-its-second-great-wall-re-catastrophe-bond/',
    '人保财险据报再度发行第二只「长城再」巨灾债券',
    'Artemis 10月5日报道：中国人民财产保险（PICC P&C）据报已再度进入市场，发行其第二只「Great Wall Re」巨灾债券，延续内地险企运用保险相连证券（ILS）转移巨灾风险的做法。 [EN原文]',
    '内地巨灾债券常态化是「保险相连证券」的重要进展，与香港推动 ILS 与专属自保的方向呼应；对理解香港作为风险管理中心的角色有帮助。',
    ['market', 'reg'], ['ils', 'cat-bond', 'china', 'hk', 'risk-transfer'],
    ['巨灾债券', '人保财险', 'Great Wall Re', 'ILS', '香港风险管理中心'],
    A('客户问及另类风险转移工具时，说明巨灾债券属机构级工具，非个人可投产品，不作推介',
      '把 ILS/巨灾债券纳入「香港风险管理中心」知识模块，供对外沟通使用',
      '作为团队理解资本市场与保险风险联动的基础案例',
      '涉及投资产品的咨询必须转介持牌机构，不越界'),
    R(0, 1, 2, 2), 'Artemis 2026-10-05', 'en', 'pending')

add('artemis-ucits-cat-bond-funds-667-ytd-plenum-20261005', 'artemis', 'pro', 68, 'news',
    '2026-10-05',
    'https://www.artemis.bm/news/ucits-cat-bond-funds-average-6-67-return-ytd-fourth-highest-annual-figure-on-record-plenum-index/',
    'UCITS 巨灾债券基金年内平均回报6.67%：Plenum 指数',
    'Artemis 10月5日引述 Plenum 指数：UCITS 巨灾债券基金年初至今平均回报6.67%，为有记录以来第四高年度水平。 [EN原文]',
    'ILS 资产表现是机构资金配置的风向标；对团队而言属背景知识（说明气候风险资产仍被机构配置），不可作为向客户推介任何产品的依据。',
    ['market'], ['ils', 'cat-bond', 'investment', 'plenum'],
    ['巨灾债券基金', 'UCITS', 'Plenum', 'ILS', '机构投资'],
    A('严禁以「回报数字」类比或暗示自家保单收益；保单收益与投资回报性质不同',
      '把资本市场话题与产品销售严格分离，涉及投资咨询转介持牌机构',
      '作为机构资金流向的背景知识，避免用于客户收益预期引导',
      '引用外部回报数据须标明来源与日期，且不得延伸至产品宣传'),
    R(0, 1, 1, 2), 'Artemis 2026-10-05', 'en', 'pending')

add('artemis-apac-ils-parametric-growth-marsh-re-20261005', 'artemis', 'pro', 72, 'news',
    '2026-10-05',
    'https://www.artemis.bm/news/apac-ils-and-parametric-markets-poised-for-growth-as-capital-needs-shift-marsh-res-gallagher/',
    '亚太 ILS 与参数化市场有望增长：Marsh Re 的 Gallagher',
    'Artemis 10月5日报道：Marsh Re 的 Gallagher 表示，随资本需求结构转变，亚太区保险相连证券（ILS）与参数化市场正处于增长前夜，香港等枢纽市场有望受益。 [EN原文]',
    '与本站同日另一条（参数化风灾/山火保障）互相印证，说明参数化与 ILS 是亚太区明确的发展方向；对理解香港政策方向与机构生态有价值。',
    ['market', 'reg'], ['apac', 'ils', 'parametric', 'hk', 'capital'],
    ['亚太', 'ILS', '参数化保险', '资本', '香港'],
    A('说明 ILS 与参数化属机构/企业级风险转移，与个人保单不同，不作混同宣传',
      '把参数化与 ILS 纳入企业客户风险转移的备选讨论（视核保可行性）',
      '作为「香港风险枢纽」叙事的公开素材，用于对内培训与对外沟通',
      '对外发布涉及市场判断时须标明来源与日期'),
    R(0, 2, 2, 2), 'Artemis 2026-10-05', 'en', 'pending')

add('artemis-eaton-vance-ils-holdings-777m-20261005', 'artemis', 'pro', 66, 'news',
    '2026-10-05',
    'https://www.artemis.bm/news/eaton-vance-mutual-fund-ils-holdings-hit-777m-new-swiss-re-and-jaffa-capital-investments/',
    'Eaton Vance 基金 ILS 持仓达7.77亿美元，新增 Swiss Re 与 Jaffa Capital 投资',
    'Artemis 10月5日报道：Eaton Vance 旗下共同基金的保险相连证券（ILS）持仓升至7.77亿美元，并新增对 Swiss Re 与 Jaffa Capital 相关工具的投资。 [EN原文]',
    '机构持续增加 ILS 配置，反映巨灾风险的资本市场化程度上升；属行业背景信息，非客户可投产品。',
    ['market'], ['ils', 'institutional', 'fund', 'cat-bond'],
    ['ILS', 'Eaton Vance', 'Swiss Re', '机构配置'],
    A('不得将机构配置信息转化为对客户的收益暗示；保单与投资产品严格区分',
      '涉及投资类咨询一律转介持牌机构，不越界提供意见',
      '作为行业背景知识更新，避免用于营销话术',
      '引用机构持仓数据须注明来源与日期'),
    R(0, 1, 1, 2), 'Artemis 2026-10-05', 'en', 'pending')

# ---------------- InsuranceAsia (pro/media) ----------------
add('iaasia-datacentre-boom-insurance-rates-20261005', 'insuranceasia', 'pro', 72, 'news',
    '2026-10-05T10:00:00+08:00',
    'https://insuranceasia.com/insurance/expert-opinion/can-asias-data-centre-boom-reverse-falling-insurance-rates',
    '亚洲数据中心热潮能否扭转保险费率下行？',
    'Insurance Asia 10月5日专家观点文章指出：2026年上半年亚洲数据中心建设管道创纪录达26.5GW，但相关保险费率同期仍下跌约5%，新增资产与费率走势背驰。 [EN原文]',
    '「资产快速扩张 + 费率下行」是承保周期的典型张力，对理解财产险/工程险市场环境有帮助；对高净值客户名下的商业/物业资产保障亦具参考价值。',
    ['market', 'insurer'], ['apac', 'datacentre', 'property', 'rates', 'capacity'],
    ['数据中心', '亚洲', '保险费率', '财产险', '承保周期'],
    A('不向客户预测费率走向；保障安排以当前核保报价为准',
      '把「资产扩张 vs 费率」纳入市场环境简报，帮助团队理解续保谈判背景',
      '作为行业周期教学案例，避免团队以「必然涨/跌」表述误导客户',
      '费率与条款以公司报价与核保结论为唯一依据'),
    R(0, 2, 2, 1), 'Insurance Asia 2026-10-05 10:00', 'en', 'pending')

add('iaasia-unimed-recovers-two-years-losses-20261005', 'insuranceasia', 'pro', 68, 'news',
    '2026-10-05T06:00:00+08:00',
    'https://insuranceasia.com/insurance/news/unimed-recovers-two-years-losses-premium-increases-kick-in',
    'UniMed 扭转两年亏损：保费上调开始见效',
    'Insurance Asia 10月5日报道：新加坡 Union Medical Benefits Society（UniMed）在保费上调后承保表现改善，扭转连续两年亏损。 [EN原文]',
    '医疗险「亏损→加费」的路径是行业常态，对客户沟通有直接价值：解释医疗通胀与保费调整的因果关系，管理续保预期。',
    ['insurer', 'market'], ['health-insurance', 'medical-inflation', 'premium', 'singapore'],
    ['UniMed', '医疗险', '保费调整', '医疗通胀', '承保亏损'],
    A('向客户解释医疗险保费调整与医疗通胀/理赔经验的关系，避免单以「公司加价」表述',
      '把医疗通胀案例纳入续保沟通培训，提前准备客户问答',
      '用区域案例说明医疗险定价压力，统一团队叙事口径',
      '具体续保条件与保费以公司通知书为准'),
    R(2, 2, 2, 1), 'Insurance Asia 2026-10-05 06:00', 'en', 'pending')

add('iaasia-aerospace-insurers-tighten-scrutiny-20261005', 'insuranceasia', 'pro', 66, 'news',
    '2026-10-05T05:45:00+08:00',
    'https://insuranceasia.com/insurance/news/aerospace-insurers-tighten-scrutiny-despite-stable-price-and-capacity',
    '航空险：价格与承保能力稳定，但核保审查趋严',
    'Insurance Asia 10月5日报道：2026年第三季航空保险市场价格与承保能力大致稳定，但承保人明显加强核保审查与条件控制。 [EN原文]',
    '「价格稳、审查紧」是典型的市场纪律化信号；对涉及航空相关风险敞口（企业差旅、货运、特殊资产）的客户沟通有参考意义。',
    ['market', 'insurer'], ['aviation', 'underwriting', 'specialty', 'apac'],
    ['航空保险', '核保', '承保能力', '亚太'],
    A('不承诺可保性与条款；特殊风险须先经核保确认再向客户描述',
      '把特殊险（航空、货运等）纳入企业客户转介与联合服务清单',
      '以「核保趋严」提醒团队前置资料准备，减少反复补件',
      '承保结论以公司核保意见为准'),
    R(0, 1, 2, 2), 'Insurance Asia 2026-10-05 05:45', 'en', 'pending')

add('iaasia-australia-29b-drought-risk-20261005', 'insuranceasia', 'pro', 68, 'news',
    '2026-10-05T05:30:00+08:00',
    'https://insuranceasia.com/insurance/news/australian-insurers-face-29b-drought-risk',
    '澳洲险企面临最高290亿澳元干旱风险',
    'Insurance Asia 10月5日报道：据 Digital Agriculture Services 数据，澳洲保险公司面临的干旱相关风险最高可达290亿澳元，凸显气候类保障缺口。 [EN原文]',
    '气候风险的量化数据可直接用于向客户说明「保障缺口」概念，尤其是农业、财产与业务中断类风险，属于需求教育的可用素材。',
    ['market', 'insurer'], ['australia', 'drought', 'climate', 'protection-gap'],
    ['澳洲', '干旱风险', '气候', '保障缺口'],
    A('用公开量化数据说明保障缺口的存在，但不对个别客户下「保障不足」结论',
      '把气候风险纳入客户风险敞口访谈清单（资产、收入中断、行业暴露）',
      '作为保障缺口教学素材，训练团队以数据开场而非以产品开场',
      '相关条款与可保性以公司核保为准'),
    R(1, 2, 2, 2), 'Insurance Asia 2026-10-05 05:30', 'en', 'pending')

add('iaasia-apac-cyber-regulatory-divergence-20261005', 'insuranceasia', 'pro', 72, 'news',
    '2026-10-05T05:15:00+08:00',
    'https://insuranceasia.com/insurance/news/insurers-face-apac-cyber-regulatory-divergence-enforcement-tightens',
    '亚太网络安全监管分化，执法趋严：保险公司须应对多套规则',
    'Insurance Asia 10月5日报道：亚太各市场的网络安全监管框架日益分化，执法力度同时收紧，保险公司需同时应对多套合规与披露要求。 [EN原文]',
    '网络风险与合规义务叠加，是企业与高净值客户的新增风险面；可借「监管分化＋执法趋严」切入网络安全保险与合规责任的讨论。',
    ['reg', 'product'], ['apac', 'cyber', 'regulation', 'compliance', 'enforcement'],
    ['网络安全', '亚太', '监管分化', '执法', '合规'],
    A('向客户说明网络风险的责任面与合规义务，不夸大保障范围；网络险条款须逐条确认',
      '把网络/数据风险纳入企业客户与高净值客户的风险盘点清单',
      '把跨市场监管差异纳入合规培训，强化「按市场分别合规」意识',
      '跨境数据与网络合规以公司合规意见与当地法规为准'),
    R(2, 2, 3, 3), 'Insurance Asia 2026-10-05 05:15', 'en', 'pending')

# ---------------- SCMP (media) ----------------
add('scmp-schroders-nuveen-hk-expansion-20261005', 'scmp', 'media', 66, 'news',
    '2026-10-05T11:00:00+08:00',
    'https://www.scmp.com/business/banking-finance/article/3369699/asset-manager-schroders-expand-hong-kong-after-merger-nuveen-ceo-says',
    '南华早报：Schroders 与 Nuveen 合并后拟扩展香港业务',
    '南华早报10月5日报道：资产管理公司 Schroders 在与 Nuveen 合并后，其行政总裁表示将扩展香港业务，强化香港作为区域资产管理枢纽的角色。 [EN原文]',
    '资产管理机构加码香港，间接反映跨境财富管理与机构资金流动的方向，对高净值客户的资产配置生态有背景意义。',
    ['market'], ['hk', 'asset-management', 'wealth', 'market'],
    ['香港', '施罗德', 'Nuveen', '资产管理', '财富管理'],
    A('不将资产管理机构动向引申为投资建议；涉及投资咨询转介持牌机构',
      '留意财富管理生态变化对客户服务链路（信托、税务、保险）的协同机会',
      '作为「香港金融生态」素材，用于对内市场认知训练',
      '对外引用新闻须标注媒体名称与日期'),
    R(0, 2, 2, 2), 'SCMP 2026-10-05 11:00', 'en', 'pending')

add('scmp-five-year-tax-incentive-too-short-20261005', 'scmp', 'media', 64, 'news',
    '2026-10-05T16:00:00+08:00',
    'https://www.scmp.com/business/companies/article/3369781/hong-kong-lawmakers-say-5-year-tax-incentive-short-entice-major-innovative-firms',
    '南华早报：议员指五年税务优惠期太短，难吸引大型创新企业',
    '南华早报10月5日报道：立法会议员认为政府拟提供的五年税务优惠期过短，难以吸引大型创新企业落户香港，建议延长优惠年期。 [EN原文]',
    '税务优惠年期是招商引资与企业架构决策的关键变量；对家族办公室与跨境企业客户的架构规划讨论有间接关联（但须由税务专业意见支撑）。',
    ['reg', 'market'], ['hk', 'tax', 'policy', 'investment', 'family-office'],
    ['香港', '税务优惠', '立法会', '招商引资', '家办'],
    A('不提供税务意见；涉及税务安排一律转介税务/法务专业顾问',
      '留意税务政策讨论对家办与跨境企业客户架构规划的间接影响',
      '作为政策动态素材，纳入高客服务培训的政策脉络部分',
      '税务与架构建议以持牌专业人士意见为准'),
    R(0, 1, 2, 2), 'SCMP 2026-10-05 16:00', 'en', 'pending')

# ---------------- InsurTech (pro) ----------------
add('insurtech-corgi-datacentre-ai-infrastructure-cover-20261005', 'insurtech', 'pro', 70, 'news',
    '2026-10-05T17:54:00+08:00',
    'https://fintech.global/2026/10/05/corgi-targets-growing-insurance-gap-around-ai-infrastructure/',
    'Corgi 推出数据中心全周期保险计划，瞄准 AI 基础设施保障缺口',
    'FinTech Global 10月5日报道：以 AI 为核心的保险科技承保人 Corgi Insurance 推出数据中心保险计划，把建造期风险（含延迟开业）、运营期的电力、冷却与 UPS 设备、营业中断保障，以及 GPU 硬件残值保障整合为单一方案，让 GPU 作为可融资资产管理。 [EN原文]',
    '该计划的产品思路值得借鉴：不再按阶段分拆投保，而是把「全生命周期 + 关键设备残值」纳入同一框架。对香港团队的用处是理解重资产/科技资产客户的保障缺口与核保数据需求，而非直接销售。',
    ['tech', 'product'], ['insurtech', 'ai', 'datacentre', 'product', 'protection-gap'],
    ['Corgi', '保险科技', '数据中心', 'AI', 'GPU', '保障缺口'],
    A('不向个人客户推介此类企业级方案；涉及企业资产保障转由公司核保评估',
      '把「关键设备残值/营业中断」纳入企业客户保障盘点清单',
      '把「整合式方案 vs 分项投保」作为产品设计思维训练案例',
      '承保范围与可保性以公司核保及再保支持为准'),
    R(0, 1, 2, 2), 'FinTech Global 2026-10-05 17:54', 'en', 'verified')

# ---------------- 组装并写入 ----------------
items = []
for args, kw in RAW:
    it = mk(*args, **kw)
    # tc 转换：对 title/summary/why/tags/actions 生成繁体
    for key in ('title', 'summary', 'why', 'tags', 'actions', 'contentRole'):
        it[key] = to_tc(it[key])
    items.append(it)

print('prepared items:', len(items))
ids = [i['id'] for i in items]
assert len(ids) == len(set(ids)), 'dup within batch'

p = 'data/live-items.json'
shutil.copy(p, 'data/live-items.json.bak-1006-0156')
d = json.load(open(p, encoding='utf-8'))
existing = {x['id'] for x in d['items']}
dups = [i for i in ids if i in existing]
if dups:
    print('SKIP existing:', dups)
    items = [i for i in items if i['id'] not in existing]

items.sort(key=lambda x: x['publishedAt'], reverse=True)
d['items'][0:0] = items
n = len(d['items'])
d['meta']['itemCount'] = n
d['meta']['generatedAt'] = NOW_ISO
d['meta']['windowNote'] = {'sc': f'本库{n}条。', 'tc': f'本庫{n}條。'}
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('live-items.json updated: +%d -> %d' % (len(items), n))

lp = 'data/last-check.json'
lc = json.load(open(lp, encoding='utf-8'))
lc['lastCheck'] = NOW_ISO
for k, v in lc.get('sources', {}).items():
    v['last'] = NOW_ISO
json.dump(lc, open(lp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('last-check.json updated:', NOW_ISO, '| sources:', len(lc.get('sources', {})))

print('--- 本次新增 ---')
for i in items:
    print(' ', i['publishedAt'], '|', i['sourceKey'], '|', i['title']['sc'][:56])
print('counts:', {k: sum(1 for i in items if i['sourceKey'] == k) for k in sorted({i['sourceKey'] for i in items})})
