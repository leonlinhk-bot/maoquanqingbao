#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-02 02:20 增量入库（覆盖 2026-10-01 内容）"""
import json, shutil, datetime, zhconv

ROOT = '/Users/leonliang/maoquanqingbao'
NOW = '2026-10-02T02:20:00+08:00'
today = datetime.date(2026, 10, 2)

def tc(s):
    return zhconv.convert(s, 'zh-hant')

def bi(obj):
    """{'sc':...} -> add tc"""
    return {'sc': obj, 'tc': tc(obj)}

ITEMS = [
 dict(
  id='ian-allianz-sg-ceo-great-eastern-raissi-20261001',
  publishedAt='2026-10-01T12:16:00+08:00',
  score=70, sourceTier='media', sourceKey='insuranceasianews', contentKind='news',
  boards=['people', 'leadership'],
  themes=['people', 'leadership', 'career', 'asia', 'channel'],
  tags=['安联新加坡', '大东方', 'CEO', '人事变动', '团体险', '一般险'],
  title='安联新加坡COO Bi Ying Ong 升任CEO；Hicham Raissi 同日转任大东方一般险及团体险董事总经理 [EN原文]',
  summary='InsuranceAsia News 10月1日12:16报道，安联新加坡营运总监（COO）Bi Ying Ong 将接替 Hicham Raissi 出任安联新加坡行政总裁。同日11:58该网另文报道，大东方（Great Eastern）委任 Hicham Raissi 为一般保险及团体保险董事总经理。保险商业（亚洲）同日人事汇总并指，安联新加坡由COO内部晋升CEO、友邦人寿韩国提名其中国区财务总监出任要职、怡安（Aon）从韦莱韬悦（WTW）延揽人才负责日本跨国企业业务，反映区域保险集团在换防中同时补齐财务与跨国企业客户能力。',
  why='同一日内安联新加坡与大东方完成CEO/董事总经理级交叉换防，加上友邦韩国、怡安日本的人事补位，说明亚太保险公司在承保周期转软、竞争加剧时更倾向用内部晋升＋跨机构挖角同步解决「本地市场理解」与「跨国企业客户能力」两块短板。对渠道合作方而言，区域管理层更替常伴随渠道政策、佣金结构与产品重心调整窗口，值得提前建立直接沟通。',
  actions={
   'front': '关注区域管理层更替后的渠道政策与产品重心变化，避免在交接期内依赖口头承诺',
   'midback': '合作机构负责人员变更须及时更新尽职调查档案与合约联络人',
   'lead': '把区域人事变化纳入季度竞争情报，评估对招募与团队激励政策的传导',
   'cross': '涉跨境架构的集团人事变动可能影响境外保单服务口径，提前确认服务接续安排',
  },
  rolesImpact={'front': 2, 'midback': 2, 'lead': 2, 'cross': 1},
  originalUrl='https://insuranceasianews.com/bi-ying-ong-to-succeed-hicham-raissi-as-allianz-singapore-ceo/',
  source='InsuranceAsia News 2026-10-01 12:16（另见同日11:58及Insurance Business Asia人事汇总）[EN原文]',
  lang='en', verifyStatus='pending',
 ),
 dict(
  id='ian-suncorp-tokio-marine-takeover-denial-20261001',
  publishedAt='2026-10-01T10:16:00+08:00',
  score=68, sourceTier='media', sourceKey='insuranceasianews', contentKind='news',
  boards=['insurer', 'm&a'],
  themes=['m&a', 'australia', 'japan', 'capital', 'market'],
  tags=['Suncorp', 'Tokio Marine', '收购', '澳交所', '回应'],
  title='澳洲Suncorp在澳交所回应中否认与Tokio Marine进行收购磋商 [EN原文]',
  summary='InsuranceAsia News 10月1日10:16报道，澳洲上市保险集团 Suncorp 在回应澳洲证券交易所（ASX）查询时，否认与日本 Tokio Marine 就收购事项进行谈判。报道未披露收购传闻的具体来源与作价区间。',
  why='Suncorp 为澳洲主要一般保险公司，Tokio Marine 近年持续在亚太收购扩张，若成事将属区域重大整合。此番否认属上市规则下的正式回应，可作为观察日资险企在亚太并购路线是否延续的观察点；对香港市场而言，日资集团跨境整合往往连带再保安排与区域管理架构调整。',
  actions={
   'front': '客户若引用并购传闻影响产品信心，应以其官方披露为准，不作投资或收益推断',
   'midback': '把区域并购传闻纳入合作方尽调关注清单，留意股权变动后的承保主体变化',
   'lead': '涉及日资／澳资集团客户与产品的团队，留意整合对区域服务与再保层级的影响',
   'cross': '跨境架构安排不宜建立在未确认的股权变动之上，须等官方公告',
  },
  rolesImpact={'front': 1, 'midback': 2, 'lead': 2, 'cross': 1},
  originalUrl='https://insuranceasianews.com/suncorp-denies-tokio-marine-takeover-talks-in-asx-response/',
  source='InsuranceAsia News 2026-10-01 10:16 [EN原文]',
  lang='en', verifyStatus='pending',
 ),
 dict(
  id='ian-simon-global-sg-reinsurance-broker-20261001',
  publishedAt='2026-10-01T06:00:00+08:00',
  score=64, sourceTier='media', sourceKey='insuranceasianews', contentKind='news',
  boards=['reinsurance', 'market'],
  themes=['reinsurance', 'broker', 'korea', 'singapore', 'expansion'],
  tags=['Simon Global', '韩国', '再保险经纪', '新加坡', '区域扩张'],
  title='韩国经纪集团 Simon Global 在新加坡设立再保险经纪公司 [EN原文]',
  summary='InsuranceAsia News 10月1日06:00报道，韩国经纪集团 Simon Global 在新加坡成立再保险经纪机构，把业务版图从韩国延伸至亚洲再保枢纽。报道未披露新实体的资本规模与团队编制。',
  why='亚洲再保市场在定价转软、资本充裕的环境下仍持续吸引新入场者，韩国经纪集团以新加坡为跳板，反映区域分出需求与再保中介竞争同步升温。对香港经纪人而言，这类新再保中介的出现意味着潜在的分出渠道与替代方案增加，也提示再保安排的中介选择需重新评估。',
  actions={
   'front': '再保层级变动一般不直接触及零售保单条款，无须向客户转述',
   'midback': '留意再保中介结构与分出安排变化，核对现有再保合约的相对竞争力',
   'lead': '把新兴再保中介纳入年度供应商评估，评估议价能力与条款条件',
   'cross': '跨境分出安排须符合本地监管与资产维持要求，新增中介须完成合规尽调',
  },
  rolesImpact={'front': 0, 'midback': 2, 'lead': 2, 'cross': 1},
  originalUrl='https://insuranceasianews.com/korean-broking-group-simon-global-launches-singapore-based-reinsurance-broker/',
  source='InsuranceAsia News 2026-10-01 06:00 [EN原文]',
  lang='en', verifyStatus='pending',
 ),
 dict(
  id='ian-markel-rob-jones-sg-renewables-20261001',
  publishedAt='2026-10-01T11:30:00+08:00',
  score=66, sourceTier='media', sourceKey='insuranceasianews', contentKind='news',
  boards=['insurer', 'market'],
  themes=['energy', 'underwriting', 'asia', 'climate', 'capacity'],
  tags=['Markel', '新能源', '可再生能源', '新加坡', '承保'],
  title='Markel 把可再生能源承保人 Rob Jones 调驻新加坡，抢占亚太能源险需求 [EN原文]',
  summary='InsuranceAsia News 10月1日11:30报道，Markel 将可再生能源承保人 Rob Jones 调驻新加坡，配合亚太区能源险布局。保险商业（亚洲）同日报道补充，亚太可再生能源项目的专业承保容量正在增长，但承保人变得更具选择性——项目的资历、工程与风险管理证明将决定能否取得较优条款。',
  why='能源转型带动亚太新能源项目工程险、营运险与相关责任险需求上升，但承保人同时提高门槛。对香港保险经纪与高客服务而言，这既是企业客户新风险需求，也提示「绿色项目」并非自动获得优惠条款；项目尽调与风险资料准备质量将直接影响承保结果。',
  actions={
   'front': '面向企业客户不谈「必然承保」，先了解项目阶段与风险资料完整度再谈条款',
   'midback': '绿色／新能源项目须留存完整工程与风险管理文件，避免以口号替代技术资料',
   'lead': '把能源转型相关险种纳入团队能力建设，明确可承接的项目类型边界',
   'cross': '跨境项目投保须确认属地与保险利益，避免多层安排出现保障空档',
  },
  rolesImpact={'front': 2, 'midback': 2, 'lead': 3, 'cross': 2},
  originalUrl='https://insuranceasianews.com/markel-shifts-rob-jones-to-singapore-in-apac-renewables-push/',
  source='InsuranceAsia News 2026-10-01 11:30（另见Insurance Business Asia同日报道）[EN原文]',
  lang='en', verifyStatus='pending',
 ),
 dict(
  id='ibm-india-broker-commission-rules-20261001',
  publishedAt='2026-10-01T09:00:00+08:00',
  score=68, sourceTier='media', sourceKey='insurancebusinessmag', contentKind='news',
  boards=['reg', 'channel', 'commission'],
  themes=['commission', 'distribution', 'india', 'broker', 'regulation'],
  tags=['IRDAI', 'IBAI', '佣金改革', '分销成本', '经纪', '代理'],
  title='印度拟议佣金新规引发经纪业反弹：独立顾问成本更高却回报更低，经纪渠道商业逻辑或消失 [EN原文]',
  summary='保险商业（亚洲）10月1日报道，印度保险监管与发展局（IRDAI）9月23日发表《重整保险分销经济性改革》咨询文件后，代表全国798家持牌保险经纪的印度保险经纪协会（IBAI）提出严重关切：在拟议佣金结构下，经纪人的收入可能低于专属代理，而独立顾问的交付成本更高、所得报酬却更低，经纪分销的商业基础可能消失。Insurance Asia同日报道，IBAI警告费用上限可能导致保险公司削减销售、服务与理赔人手并收窄分销覆盖。',
  why='这是9月29日Nomura解读之后的「渠道侧」回应：监管若把佣金从产品端大幅压向一致化，最先失去经济性的是成本结构最重的独立经纪模式。对香港亦有参照价值——本地正以转介费50%上限、佣金改革与披露要求收紧渠道经济性；经纪团队应把「顾问成本与报酬是否匹配」纳入长期商业模式评估，而非只看单笔佣金率。',
  actions={
   'front': '不与客户讨论佣金水平，但须清楚向客户说明自身服务范围与收费／报酬来源结构',
   'midback': '复核转介费与佣金结构是否符合本地比例上限要求，留存服务与收费对应关系',
   'lead': '把「顾问交付成本 vs 报酬结构」列为年度经营评审项，避免在高成本客群上依赖低报酬渠道',
   'cross': '跨境分销若涉及境外持牌主体，须分别符合两地佣金与转介规则，不得以结构安排规避',
  },
  rolesImpact={'front': 1, 'midback': 3, 'lead': 3, 'cross': 2},
  originalUrl='https://www.insurancebusinessmag.com/asia/news/breaking-news/brokers-would-earn-less-than-tied-agents-under-indias-proposed-commission-rules-591968.aspx',
  source='Insurance Business Asia 2026-10-01（另见 Asia Insurance Review、Insurance Asia 同日报道）[EN原文]',
  lang='en', verifyStatus='pending',
 ),
 dict(
  id='ibm-swissre-asia-flood-protection-gap-83pct-20261001',
  publishedAt='2026-10-01T10:30:00+08:00',
  score=66, sourceTier='media', sourceKey='insurancebusinessmag', contentKind='news',
  boards=['product', 'market', 'cat'],
  themes=['flood', 'protection-gap', 'data', 'property', 'parametric'],
  tags=['瑞士再保险', '洪水保障缺口', '楼层高度', '风险暴露数据', '定价'],
  title='瑞士再保险：亚洲洪水保障缺口接近83%，建筑层面定价未普及，「楼层高度」量测谁受益取决于风险暴露数据 [EN原文]',
  summary='保险商业（亚洲）10月1日报道指出，瑞士再保险把亚洲洪水保障缺口估算为接近83%；在尚未能应用建筑层面（building-level）定价的市场，以「楼层高度」作为洪水风险量测方式能否真正带来更公平的定价，取决于风险暴露数据的质量与覆盖度，而非量测方法本身。',
  why='保护缺口83%意味亚洲绝大多数洪水损失未被保险覆盖，这是参数型产品与公共风险池的政策空间；但对前线实务更直接的含义是：没有可靠的暴露与高程数据，再精细的定价方法也无法落地。香港与湾区近年推动参数型天气／洪水保障，经纪团队在与企业客户谈防洪方案时，应先盘点标的层高、地库、存货位置等基础数据。',
  actions={
   'front': '与客户谈洪水保障时先收集楼层、地库与存货布置等基础暴露资料，避免空谈覆盖比例',
   'midback': '把风险暴露数据质量纳入承保资料清单，缺项不予虚假补足',
   'lead': '评估参数型／指数型产品在本地客户群中的适用边界与服务能力',
   'cross': '跨境物业与厂房的洪水保障按标的分层核查，避免与所在地公共补偿重复或漏空',
  },
  rolesImpact={'front': 2, 'midback': 3, 'lead': 2, 'cross': 2},
  originalUrl='https://www.insurancebusinessmag.com/asia/news/property/exposure-data-decides-who-benefits-from-floor-height-measurement-591912.aspx',
  source='Insurance Business Asia 2026-10-01（援引瑞士再保险估算）[EN原文]',
  lang='en', verifyStatus='pending',
 ),
 dict(
  id='insuranceasia-mas-governance-consultation-20261001',
  publishedAt='2026-10-01T15:00:00+08:00',
  score=70, sourceTier='media', sourceKey='insuranceasia', contentKind='news',
  boards=['reg', 'firm'],
  themes=['governance', 'regulation', 'singapore', 'board', 'compliance'],
  tags=['MAS', '新加坡金管局', '管治咨询', '董事独立性', '董事会构成'],
  title='新加坡金管局就银行与保险公司管治要求展开咨询：涵盖董事独立性、董事会构成等 [EN原文]',
  summary='Insurance Asia 10月1日报道，新加坡金融管理局（MAS）就银行与保险公司的企业管治要求提出更新建议并展开咨询，内容包括董事独立性、董事会组成等，另涉其他管治安排。报道未披露咨询截止日期。',
  why='新加坡是香港在财富管理与保险枢纽上的直接竞争对手，MAS 每次修订金融机构管治要求都会形成区域对标压力。香港保监局《监管通讯》第13期同样把负责人员（RO）在任年期与适当人选评估列为重点，两地同步收紧「谁在治理、治理多久、有无实权」这一条主线。对机构与团队而言，董事／负责人员安排的稳定性正由内部治理题变成监管检视项。',
  actions={
   'front': '不涉及客户沟通；若客户问及区域监管差异，只陈述已公布事实',
   'midback': '对照本地要求梳理董事与负责人员安排的稳定性证据，避免频繁更替',
   'lead': '把治理架构稳定性列入年度自查，与区域同业要求对标',
   'cross': '同时受两地监管的集团须分别满足各属地要求，不得以较高标准替代属地义务',
  },
  rolesImpact={'front': 0, 'midback': 3, 'lead': 3, 'cross': 2},
  originalUrl='https://insuranceasia.com/news/mas-proposes-governance-updates-banks-and-insurers',
  source='Insurance Asia 2026-10-01 [EN原文]',
  lang='en', verifyStatus='pending',
 ),
 dict(
  id='insuranceasia-monee-great-eastern-shopee-embed-20261001',
  publishedAt='2026-10-01T14:00:00+08:00',
  score=62, sourceTier='media', sourceKey='insuranceasia', contentKind='news',
  boards=['tech', 'product', 'channel'],
  themes=['embedded', 'ecommerce', 'partnership', 'digital', 'distribution'],
  tags=['Monee', '大东方', 'Shopee', '嵌入式保险', '旅游险', '车险'],
  title='Monee 与大东方在 Shopee 上线旅游险与车险：嵌入式保险继续向电商场景渗透 [EN原文]',
  summary='Insurance Asia 10月1日报道，Monee 与大东方（Great Eastern）在电商平台 Shopee 推出旅游保险与汽车保险，旅游险涵盖行程取消、航班延误与行李遗失。Tech in Asia（10月1日）补充，Sea 集团已于2025年把 SeaMoney 重塑为 Monee，本次是大东方与 Monee 在 Shopee 上的合作，此前同类合作包括与 MSIG 推出的宠物保险。',
  why='嵌入式保险正把「先有需求再找保险」改成「在消费场景里顺手投保」，旅游与车险是最容易标准化、比价透明的两个险种。对传统经纪与代理渠道而言，这类合作压缩的是低复杂度、低咨询需求的客群，倒逼前线把价值往复杂需求（家庭保障规划、传承与跨境架构）迁移；同时也提示平台分佣与透明度将成为合规关注点。',
  actions={
   'front': '把低复杂度产品交由平台化的趋势视为客户认知变化，主动升级咨询深度与需求分析能力',
   'midback': '与平台方合作须明确各自责任边界、客户资料使用与披露安排',
   'lead': '评估嵌入渠道对现有团队的客群结构影响，调整产品组合与培训重点',
   'cross': '平台跨境销售须按属地牌照与远程销售规则处理，不得以线上流程规避持牌要求',
  },
  rolesImpact={'front': 3, 'midback': 2, 'lead': 2, 'cross': 1},
  originalUrl='https://insuranceasia.com/insurance/news/monee-and-great-eastern-launch-travel-and-motor-cover-shopee',
  source='Insurance Asia 2026-10-01（另见 Tech in Asia 同日报道）[EN原文]',
  lang='en', verifyStatus='pending',
 ),
 dict(
  id='insurtech-bolttech-bold-penguin-global-partnership-20261001',
  publishedAt='2026-10-01T19:44:00+08:00',
  score=62, sourceTier='media', sourceKey='insurtech', contentKind='news',
  boards=['insurtech', 'tech'],
  themes=['insurtech', 'distribution', 'partnership', 'embedded', 'ai'],
  tags=['Bolttech', 'Bold Penguin', '保险科技', '全球合作', '分销'],
  title='新加坡保特科技 Bolttech 与 Bold Penguin 建立全球保险合作，整合AI工作流与分销能力 [EN原文]',
  summary='Tech in Asia 10月1日19:44报道，总部位于新加坡的保险科技公司 Bolttech 与美国商业保险数字化平台 Bold Penguin 建立全球保险合作，报道指合作将整合 Bolttech 具备AI能力的工作流程与分销网络。报道未披露合作的具体商业条款与目标收入。',
  why='Bolttech 已多次通过合作与收购扩张嵌入式分销网络，此次与美国商业险数字平台结盟，反映保险科技公司正把「交易所式」的报价与核保工作流当作跨国复制的主要资产。对香港市场而言，值得关注的是这类平台进入后的中介角色分工：谁能提供咨询与合规把关，谁只提供流程效率。',
  actions={
   'front': '关注平台化工具是否替代部分标准化报价环节，提前建立不可被替代的咨询价值',
   'midback': '若接入第三方平台，须审查数据流向、客户授权与责任划分',
   'lead': '评估与技术平台合作的可复制性与议价条件，避免单纯成为流量来源',
   'cross': '跨境平台涉及多地持牌与数据合规，合作前须逐地区确认',
  },
  rolesImpact={'front': 1, 'midback': 2, 'lead': 1, 'cross': 1},
  originalUrl='https://www.techinasia.com/tag/insurtech',
  source='Tech in Asia 2026-10-01 19:44 [EN原文]',
  lang='en', verifyStatus='pending',
 ),
 dict(
  id='insurtech-moneyhero-critical-illness-comparison-hk-20261001',
  publishedAt='2026-10-01T09:00:00+08:00',
  score=60, sourceTier='media', sourceKey='insurtech', contentKind='news',
  boards=['insurtech', 'tech', 'hk'],
  themes=['insurtech', 'critical-illness', 'comparison', 'hk', 'consumer'],
  tags=['MoneyHero', '危疾保险', '比价平台', '香港', '消费者'],
  title='MoneyHero 在香港保险比较平台加上危疾保险比较：可对比单次赔付与多次赔付并直接跳转投保 [EN原文]',
  summary='GlobeNewswire 10月1日09:00新闻稿，香港保险比较平台 MoneyHero 把危疾保险纳入比较功能，用户可对比单次赔付（single-claim）与多次赔付（multiple-claim）方案，并直接跳转至所选保险公司完成申请；平台此前已提供人寿、旅游与医疗保险比较。',
  why='危疾是香港消费者最需要、也最难自行比较的险种之一——单次赔付与多次赔付的责任结构差异极大，过去依赖代理人口述。比价平台把「结构对比」暴露给消费者，会同时抬高两个门槛：产品条款的清晰度，以及前线对「多次赔付触发条件、间隔期、分组限制」的解释能力。用含糊话术带过结构差异，正是投诉高发区。',
  actions={
   'front': '谈危疾先讲清单次与多次赔付的触发条件、间隔期与分组限制，不以「多次赔付」四字带过',
   'midback': '产品说明与营销材料须准确呈现赔付结构差异，避免可比性误导',
   'lead': '把危疾条款结构对比能力列为团队必修与质检项',
   'cross': '客户若持有多地危疾保单，须逐份核对赔付触发与不保事项，避免重复投保的误判',
  },
  rolesImpact={'front': 3, 'midback': 3, 'lead': 2, 'cross': 2},
  originalUrl='https://www.globenewswire.com/news-release/2026/10/01/3372946/0/en/moneyhero-adds-critical-illness-comparison-on-hong-kong-insurance-marketplace.html',
  source='GlobeNewswire（MoneyHero）2026-10-01 09:00 [EN原文]',
  lang='en', verifyStatus='pending',
 ),
 dict(
  id='nfra-serious-dishonesty-list-management-rules-effective-20261001',
  publishedAt='2026-10-01',
  score=88, sourceTier='official', sourceKey='nfra', contentKind='circular',
  boards=['reg', 'enforcement'],
  themes=['regulation', 'china', 'enforcement', 'credit', 'governance'],
  tags=['金融监管总局', '严重失信主体名单', '终身禁止进入保险业', '信用修复', '10月1日施行'],
  title='《金融监管总局关于严重失信主体名单管理的规定（试行）》10月1日起施行：终身禁止进入保险业等情形列入严重失信名单',
  summary='《国家金融监督管理总局关于严重失信主体名单管理的规定（试行）》（2026年7月3日总局令2026年第3号公布）自2026年10月1日起施行。规定明确三类列入情形：一是法人机构被吊销经营或业务许可证、被取消或撤销终身任职资格、终身禁止从事银行业工作或终身禁止进入保险业等行政处罚；二是因六类行为被从重行政处罚或被限制市场准入、责令转让股权、撤销行政许可，严重破坏市场公平竞争秩序与社会正常秩序；三是当事人有履行能力但拒不履行、逃避执行行政决定，被人民法院作出强制执行裁定。规定同时明确信用修复条件与程序：列入满一年且同时符合三项条件者可申请提前移出，经总局及其派出机构核实后决定是否准予。',
  why='这是内地金融监管把「行政处罚」升级为「名单＋市场禁入」的制度化一步，保险业被明确写入终身禁入情形。对香港跨境业务而言，重点是人员关联：若合作方、股东或关键人员在内地被列入名单，将直接影响跨境合作的适当人选评估与集团声誉。此外，信用修复机制的「提前移出」要求满一年且符合条件，说明名单并非终身烙印，但退出成本高，事前合规远比事后修复划算。',
  actions={
   'front': '不得就监管处罚或名单事宜向客户作任何解释性承诺，涉客户资料问题一律转合规',
   'midback': '把内地严重失信名单筛查纳入合作方与关键人员年度尽调流程，留存筛查记录',
   'lead': '向团队明确终身禁入情形与后果，把名单风险纳入用人红线',
   'cross': '跨境合作股东、董事与关键人员须同时通过两地适当人选评估，发现名单情形立即上报',
  },
  rolesImpact={'front': 1, 'midback': 3, 'lead': 3, 'cross': 3},
  originalUrl='https://www.gov.cn/gongbao/2026/issue_12946/202608/content_7079357.html',
  source='国家金融监督管理总局令2026年第3号（2026年7月3日公布，2026年10月1日施行）',
  lang='zh', verifyStatus='verified',
 ),
 dict(
  id='artemis-catbond-record-pace-after-q3-20261001',
  publishedAt='2026-10-01T18:00:00+08:00',
  score=70, sourceTier='pro', sourceKey='artemis', contentKind='report',
  boards=['cat', 'ils', 'market'],
  themes=['cat', 'ils', 'reinsurance', 'capital', 'market'],
  tags=['巨灾债', 'ILS', '第三季', '发行纪录', '再保资本'],
  title='Artemis：第三季发行高于平均水平后，巨灾债市场维持纪录级发行节奏 [EN原文]',
  summary='Artemis 10月1日报道引述最新报告指出，第三季巨灾债（catastrophe bond）发行量高于历年同期平均水平，带动全年发行维持纪录级节奏，显示保险相连证券（ILS）作为再保资本的供给持续充裕。报道未在标题摘要中披露具体发行规模与收益率区间。',
  why='巨灾债供给持续高企是亚太再保定价转软的重要背景之一——替代资本充裕会压缩传统再保人的定价空间，进而影响分出成本与产品结构。对香港而言，ILC／ILS 是政策推动的枢纽方向之一（保险相连证券资助先导计划、专属自保与基建资本待遇），发行节奏纪录化说明市场深度在改善，值得持续跟踪对再保成本的传导。',
  actions={
   'front': '不与客户谈再保资本或投资收益，产品演示须使用保司已批核资料',
   'midback': '再保成本变化须在下次核保／分保评估时纳入，不作前瞻性承诺',
   'lead': '把再保定价趋势纳入年度产品与渠道规划假设，避免沿用旧成本假设',
   'cross': '涉 ILS 与结构性安排须确认持牌与销售限制，不得向零售客户推介',
  },
  rolesImpact={'front': 0, 'midback': 3, 'lead': 2, 'cross': 1},
  originalUrl='https://www.artemis.bm/news/catastrophe-bond-market-keeps-record-pace-after-above-average-q3-report/',
  source='Artemis 2026-10-01 [EN原文]',
  lang='en', verifyStatus='pending',
 ),
 dict(
  id='insuranceasia-universal-sompo-cardiac-claims-india-20261001',
  publishedAt='2026-10-01T14:30:00+08:00',
  score=60, sourceTier='media', sourceKey='insuranceasia', contentKind='stats',
  boards=['health', 'claims'],
  themes=['health', 'claims', 'india', 'risk', 'data'],
  tags=['Universal Sompo', '心脏疾病理赔', '印度', '三级城市', '健康险'],
  title='Universal Sompo 警示印度小城市心脏疾病理赔激增：非都市区理赔中三级城市占比显著 [EN原文]',
  summary='Insurance Asia 10月1日报道，印度保险公司 Universal Sompo 指出来自小城市（非都市区）的心脏疾病理赔明显上升，其中三级城市（Tier 3）持续占都市以外理赔的显著份额，反映生活方式变化与医疗可及性差异正在改变健康险理赔结构。',
  why='健康险理赔结构的地区性变化是产品定价与核保假设的先行指标：当理赔从大城市向中小城市扩散，意味风险分布更广、经验数据更分散，也意味医疗服务使用习惯在变化。香港与湾区健康险同样面对「跨境就医＋慢病年轻化」的组合压力，理赔地域结构的变化值得作为核保与产品设计讨论的参照案例。',
  actions={
   'front': '谈健康保障时以实际医疗需求与就医地点为依据，不夸大或回避既往症处理',
   'midback': '理赔地域与病种结构变化应定期反馈核保，供经验分析与假设检视',
   'lead': '把健康险理赔趋势纳入产品组合评审，避免按旧经验判断新增风险',
   'cross': '跨境就医理赔须逐案核对保障范围、指定医院网络与不保事项',
  },
  rolesImpact={'front': 2, 'midback': 3, 'lead': 2, 'cross': 2},
  originalUrl='https://insuranceasia.com/insurance/news/universal-sompo-flags-cardiac-claims-surge-indias-smaller-cities',
  source='Insurance Asia 2026-10-01 [EN原文]',
  lang='en', verifyStatus='pending',
 ),
]

# ---------- build ----------
for it in ITEMS:
    out = {}
    out['clusterCount'] = 1
    out['score'] = it['score']
    out['verifyStatus'] = it['verifyStatus']
    out['sourceTier'] = it['sourceTier']
    out['sourceKey'] = it['sourceKey']
    out['contentKind'] = it['contentKind']
    out['actions'] = {k: bi(v) for k, v in it['actions'].items()}
    out['actions'] = {k: out['actions'][k] for k in ['front', 'midback', 'lead', 'cross']}
    out['rolesImpact'] = it['rolesImpact']
    out['boards'] = it['boards']
    out['themes'] = it['themes']
    out['tags'] = {'sc': it['tags'], 'tc': [tc(t) for t in it['tags']]}
    out['contentRole'] = {'sc': '本站导读', 'tc': '本站導讀'}
    out['featured'] = False
    out['evergreen'] = False
    out['ingestedAt'] = NOW
    out['id'] = it['id']
    out['publishedAt'] = it['publishedAt']
    out['title'] = bi(it['title'])
    out['summary'] = bi(it['summary'])
    out['why'] = bi(it['why'])
    out['source'] = {'sc': it['source'], 'tc': tc(it['source']), 'lang': it['lang']}
    out['originalUrl'] = it['originalUrl']
    it['_final'] = out

path = f'{ROOT}/data/live-items.json'
shutil.copy(path, f'{ROOT}/data/live-items.json.bak-1002-0220')
data = json.load(open(path))

existing = {i['id'] for i in data['items']}
dupes = [it['id'] for it in ITEMS if it['id'] in existing]
if dupes:
    raise SystemExit(f'ABORT duplicate ids: {dupes}')

new = [it['_final'] for it in ITEMS]
data['items'] = new + data['items']
data['meta']['generatedAt'] = NOW
n = len(data['items'])
data['meta']['itemCount'] = n
data['meta']['windowNote'] = {'sc': f'本库{n}条。', 'tc': f'本庫{n}條。'}
json.dump(data, open(path, 'w'), ensure_ascii=False, indent=1)
print(f'inserted {len(new)} items; total={n}')

# ---------- last-check ----------
lp = f'{ROOT}/data/last-check.json'
lc = json.load(open(lp))
lc['lastCheck'] = NOW
for k, v in lc['sources'].items():
    v['last'] = NOW
json.dump(lc, open(lp, 'w'), ensure_ascii=False, indent=2)
print('last-check updated ->', NOW)
for it in ITEMS:
    print(' *', it['publishedAt'], it['sourceKey'], it['id'])
