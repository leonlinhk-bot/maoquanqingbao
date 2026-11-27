# -*- coding: utf-8 -*-
import json, zhconv
LIVE = '/Users/leonliang/maoquanqingbao/data/live-items.json'
d = json.load(open(LIVE, encoding='utf-8'))
items = d['items']
existing = {i.get('id') for i in items}
urls = {i.get('originalUrl') for i in items}

def E(**kw):
    return kw

new = []

new.append(E(
 id='insuranceasia-ia-conduct-complaints-h1-2026-20261126',
 clusterCount=1, score=68, verifyStatus='pending', sourceTier='media', sourceKey='insuranceasia',
 contentKind='report',
 title={'sc':'保监局上半年接获投诉 652 宗增 10%　点名代理流失率与「非保证利益」失实陈述 [EN原文]'},
 summary={'sc':'Insurance Asia 11 月 26 日报道保监局 2026 年 9 月号《Conduct in Focus》：2026 年上半年接获投诉 652 宗，同比增 10%（去年同期 593 宗），增幅低于首季保费 32% 的同比增速。业务及营运类占比最大、同比升 9%，涉保单行政、公司管理手法与代理服务质素；索偿类以医疗保险居首，其次汽车与旅游，焦点是理赔延迟与「应赔未赔」感。中介投诉大致平稳，但失实陈述、不当建议、欺诈及伪造文件仍持续。局方点名代理流失：约 12 万名持牌中介中，逾半新领牌者做不满首个三年牌照期，并把新人销售压力与非保证利益失实表述挂钩；另对三家经纪公司施加牌照续期条件、禁止接收转介业务，并警告数码广告只突出高实现率、分红增长与短回本期而未同幅披露限制。'},
 why={'sc':'这条把监管当前的两个抓手说得很直白：一是保单行政与理赔延迟，二是「数字上头条、限制也要同幅」的披露要求。对前线，后一句等于给非保证利益话术定了判准——不能只讲实现率或回本期。对团队主管，逾半新领牌者做不满三年意味着新人留存本身就是合规风险源，招募与陪访节奏要按这个现实设计，而不是按理想留存设计。'},
 actions={'front':{'sc':'见客讲分红/实现率时，把「非保证」与主要假设放同一页同一视觉层级，别只在备注小字写。'},
          'midback':{'sc':'把「投诉集中在保单行政与理赔延迟」写进后台服务清单：投保后 30 天内的保全与理赔进度主动通报，减少「感觉没赔」。'},
          'lead':{'sc':'新人培训加一节「非保证利益怎么讲」，并把三家经纪被禁转介业务的案例做成一页风险卡。'},
          'cross':{'sc':'若与转介伙伴合作，先确认对方是否具备可留痕的转介安排，避免落入被施加牌照条件的同类情形。'}},
 rolesImpact={'front':3,'midback':1,'lead':3,'cross':2},
 source={'sc':'Insurance Asia（引保监局《Conduct in Focus》2026 年 9 月号）','lang':'en'},
 boards=['reg'], themes=['reg','compliance','distribution'],
 tags={'sc':['保监局','投诉统计','非保证利益','代理流失','转介业务']},
 publishedAt='2026-11-26T05:45:00+08:00',
 originalUrl='https://insuranceasia.com/insurance/news/hong-kong-insurance-complaints-rise-10-in-h1-2026'
))

new.append(E(
 id='icac-mpf-intermediary-jailed-40-months-20261126',
 clusterCount=1, score=86, verifyStatus='verified', sourceTier='official', sourceKey='icac',
 contentKind='press',
 title={'sc':'强积金中介人伪造「移居内地」证明助客提早提取 460 万　判囚 40 个月'},
 summary={'sc':'廉政公署 11 月 26 日公布：37 岁强积金中介人、富卫人寿（百慕达）时任保险代理黄锦辉，串同三名客户以虚假法定声明及证明文件，讹称移居中国内地并永久离开香港，向永明信托申请提早提取强积金共约 460 万港元，在区域法院被判囚 40 个月；三名客户判囚 12 至 16 个月、缓刑两年。法官指案件涉庞大公众利益、严重损害强积金制度，被告为金钱利益犯案、违反诚信并主导整个计划，须即时监禁。廉署已申请充公其犯罪得益，积金局、富卫及永明信托在调查中提供协助。'},
 why={'sc':'这是保险代理兼强积金中介双重身份下的典型红线案例：客户有资金需求时，「帮你搞个移居证明」是最容易被当作服务的越界动作，而代价是刑责。判决把「文件真伪」与「制度公信力」直接连起来，比任何内部合规手册都有说服力。'},
 actions={'front':{'sc':'遇到客户问「能不能提早拿 MPF」，只讲法定六种提取理由与对应证明要求，绝不代拟、代办任何声明。'},
          'midback':{'sc':'在 MPF/退休咨询 SOP 里加一条：涉及提早提取的查询必须留档并转合规复核，不接受口头「你去弄个证明」。'},
          'lead':{'sc':'把本案做成 10 分钟早会案例，明确「代客造文件＝串谋诈骗」，并说明缓刑只适用于客户而非中介。'},
          'cross':{'sc':'与转介的 MPF 顾问对齐口径：提取资格以受托人及积金局规则为准，任何「包搞定」承诺一律不接。'}},
 rolesImpact={'front':3,'midback':2,'lead':3,'cross':2},
 source={'sc':'香港廉政公署（ICAC）新闻公报','lang':'zh'},
 boards=['reg'], themes=['compliance','fraud','regulation'],
 tags={'sc':['廉政公署','强积金','虚假声明','中介操守','判刑']},
 publishedAt='2026-11-26',
 originalUrl='https://icac.org.hk/tc/p/press/index_id_5062.html'
))

new.append(E(
 id='hkfi-ridehailing-12-insurers-20261127',
 clusterCount=1, score=66, verifyStatus='verified', sourceTier='media', sourceKey='oncc',
 contentKind='news',
 title={'sc':'保险业联会：12 间险企已推网约车保险　商用部分保费 1 万至 1.3 万、低于的士'},
 summary={'sc':'东网 11 月 27 日报道，保险业联会表示现有 12 间保险公司已推出网约车第三者保险保单，数目占私家车保险市场逾 70%，相信供应充足。网约车「人车绑定」、保险公司掌握车主身份，加上服务时间较的士短、风险较低，商用部分保费低至 1 万至 1.3 万港元，低于的士。联会行政总监刘佩玲强调，由于网约车同时是私家车，私家车与网约车商用部分的保单必须由同一公司承保，以确保保障无缝交接；联会正向当局及平台争取更多出行数据，以便更准确评估风险、日后调节保费。网约车车辆许可证名额上限 1 万个，明年初公开接受申请。'},
 why={'sc':'网约车是港险少数还在扩容的新险种，且规则里有一条容易被忽略的业务门槛：私家车与商用部分必须同一承保人。这条对做车队、的士或商用车的同事是直接的交叉销售切入点，也提醒别在两家公司分开投保造成保障断点。'},
 actions={'front':{'sc':'拜访车主客户时先问「有没有打算申请网约车许可证」，若有，核对现有私家车保单承保公司是否能一并承接商用部分。'},
          'midback':{'sc':'整理一份网约车保险对照表：12 家承保公司、承保条件、私家车与商用须同一公司的要求、保费区间。'},
          'lead':{'sc':'把网约车列为 Q1 车险专项，指定一名同事跟联会与平台数据进展。'},
          'cross':{'sc':'与车行、车队管理方对齐：许可证申请时间表与保单生效日的衔接安排。'}},
 rolesImpact={'front':2,'midback':2,'lead':2,'cross':2},
 source={'sc':'东网 on.cc（引保险业联会）','lang':'zh'},
 boards=['product','market'], themes=['product','hong-kong','distribution'],
 tags={'sc':['网约车保险','保险业联会','第三者保险','车险','许可证']},
 publishedAt='2026-11-27T11:45:00+08:00',
 originalUrl='https://hk.on.cc/hk/bkn/cnt/news/20261127/bkn-20261127114500759-1127_00822_001.html'
))

new.append(E(
 id='convoy-broker-cyber-incident-20261126',
 clusterCount=2, score=64, verifyStatus='verified', sourceTier='media', sourceKey='stheadline',
 contentKind='news',
 title={'sc':'康宏理财遭网络安全事件　暂停后勤系统与客户专页　私隐公署已展开循规审查'},
 summary={'sc':'康宏理财服务 11 月 26 日发出「重要服务通知」，指近日发现一宗网络安全事件，作为审慎预防措施已即时暂停后勤管理系统及「客户专页」服务，以配合调查与系统恢复，并已向相关监管及执法机构通报。公司称现阶段评估无证据显示经康宏安排的保险保单或强积金账户受影响，亦未发现未经授权交易，建议客户警惕可疑电邮、来电、短讯或链接。个人资料私隐专员公署回复星岛头条表示，已于 11 月 16 日接获该机构资料外泄事故通报，机构仍在确定受影响人数及个人资料类别，公署已按既定机制展开循规审查，并提醒尽快通知受影响人士。'},
 why={'sc':'这是本月第三宗香港保险相关机构披露的网络安全事件（前有苏黎世香港、OneDegree），模式一致：先停系统、再通报、受影响人数要等鉴证。对经纪团队的实际意义是两件事——客户会用「你们系统安全吗」来试探专业性，以及一旦自己是涉事机构的分销方，需要立刻准备好「保单是否受影响」的统一口径。'},
 actions={'front':{'sc':'客户问起时，只讲已公开事实（停系统、已通报、暂未见保单受影响），不猜测受影响人数，也不替涉事机构背书。'},
          'midback':{'sc':'把「合作机构安全事件」加入供应商风险管理清单：通报时限、客户通知责任、保单资料是否在对方系统。'},
          'lead':{'sc':'检视团队自身的客户资料存放方式，落实最小必要收集与双因素验证。'},
          'cross':{'sc':'若与康宏或其他经纪有转介合作，先确认客户资料由谁持有、事故时谁负责通知。'}},
 rolesImpact={'front':2,'midback':2,'lead':2,'cross':2},
 source={'sc':'星岛头条（引康宏通告、私隐专员公署回复）','lang':'zh'},
 boards=['market','tech'], themes=['cyber','hong-kong','firm'],
 tags={'sc':['康宏理财','网络安全事件','私隐专员公署','资料外泄','经纪公司']},
 publishedAt='2026-11-26T21:34:00+08:00',
 originalUrl='https://headline4hk.com/article/20261126/stheadline/3641520'
))

new.append(E(
 id='insuranceasianews-wangfuk-claims-74m-20261126',
 clusterCount=1, score=72, verifyStatus='pending', sourceTier='pro', sourceKey='insuranceasianews',
 contentKind='news',
 title={'sc':'宏福苑火灾一周年：相关保险索偿已逾 7,400 万美元　中国太平为承保人 [EN原文]'},
 summary={'sc':'Insurance Asia News 11 月 26 日报道，大埔宏福苑火灾发生一年后，相关保险索偿金额已超过 7,400 万美元。报道指该场火灾共造成 168 人死亡，中国太平为所有相关保单的承保公司。原文为付费内容，本条目仅据可见导语整理，索偿构成（财产险、公众责任、人寿）与再保安排待补。'},
 why={'sc':'一年后的累计索偿额，是观察香港单一物业巨灾如何穿透财产险、公众责任与再保安排的真实样本。对做高客与团体业务的同事，这类事件的后续（保费重定价、楼宇管理方投保要求收紧）往往比事件本身更有商业含义。'},
 actions={'front':{'sc':'与旧楼、法团客户谈火险时，可用本案说明「保额是否足够重建」比「保费便宜多少」更关键。'},
          'midback':{'sc':'补一份宏福苑理赔结构笔记（财产险/公众责任/人寿各自口径），原文解锁后更新。'},
          'lead':{'sc':'把旧楼与法团财产险列为下季度风险检视重点，安排同事复查在保客户的保额充足度。'},
          'cross':{'sc':'与公估、法团管理方对齐重建成本估算口径，避免续保时保额与造价脱节。'}},
 rolesImpact={'front':2,'midback':1,'lead':2,'cross':2},
 source={'sc':'Insurance Asia News','lang':'en'},
 boards=['market','insurer'], themes=['claims','catastrophe','hong-kong'],
 tags={'sc':['宏福苑','火灾','中国太平','财产险','索偿']},
 publishedAt='2026-11-26T06:00:00+08:00',
 originalUrl='https://insuranceasianews.com/hong-kongs-wang-fuk-court-fire-claims-top-us74m-a-year-on/'
))

new.append(E(
 id='insuranceasianews-insurtech-insights-asia-hk-2026-20261127',
 clusterCount=1, score=70, verifyStatus='verified', sourceTier='pro', sourceKey='insuranceasianews',
 contentKind='news',
 title={'sc':'Insurtech Insights Asia 2026 重临香港　主题由「实验」转向「执行」 [EN原文]'},
 summary={'sc':'Insurance Asia News 11 月 27 日报道，Insurtech Insights Asia 2026 在香港 Kerry Hotel 举行，逾 5,000 名与会者、300 多位讲者，主题是从「实验」走向「执行」：AI、数据与新的合作模式正在重塑风险如何被理解、定价与承保。'},
 why={'sc':'会议主题本身就是行业节奏的信号：保险科技的叙事已从「试点 PoC」转到「上线与 ROI」。对国内团队，值得留意的是香港正把自己定位成区域 insurtech 的落地场，这会带来更多本地合作与人才流动机会。'},
 actions={'front':{'sc':'与客户谈数字化时，用「从 PoC 到上线」这个框架，问对方现有系统到底哪一步还没跑通。'},
          'midback':{'sc':'梳理大会公开的讲者与议题清单，筛出与核保、理赔自动化相关的 3 家可对接供应商。'},
          'lead':{'sc':'把「AI 已进入执行期」作为团队年度能力升级的说服材料，而非单纯的行业新闻。'},
          'cross':{'sc':'留意会后与本地 insurtech 的合作机会，优先评估与现有 BOS 流程可对接的方案。'}},
 rolesImpact={'front':1,'midback':2,'lead':2,'cross':2},
 source={'sc':'Insurance Asia News','lang':'en'},
 boards=['tech','market'], themes=['insurtech','ai','hong-kong'],
 tags={'sc':['Insurtech Insights','香港','保险科技','AI','行业会议']},
 publishedAt='2026-11-27T09:00:00+08:00',
 originalUrl='https://insuranceasianews.com/from-experimentation-to-execution-insurtech-insights-asia-2026-returns-to-hong-kong/'
))

new.append(E(
 id='insuranceasianews-msig-hk-kathy-mak-financial-lines-20261126',
 clusterCount=1, score=70, verifyStatus='pending', sourceTier='pro', sourceKey='insuranceasianews',
 contentKind='news',
 title={'sc':'MSIG 香港委任 Kathy Mak 为财务险高级经理　来自 Chubb [EN原文]'},
 summary={'sc':'Insurance Asia News 11 月 26 日报道，MSIG 香港委任 Kathy Mak 为财务险（financial lines）高级经理，她此前在 Chubb 出任财务险高级核保人，自 2022 年 5 月起任职。原文为付费内容，本条目据可见导语整理。'},
 why={'sc':'单一人事变动本身价值有限，但它指向一个持续的趋势：香港财务险（D&O、专业责任、网络）承保人才在少数国际险企之间流转，说明该条线仍在扩容而非收缩。做企业险与董责险的同事可留意各家的核保口径变化。'},
 actions={'front':{'sc':'拜访企业客户时顺带确认董责险与专业责任的核保口径是否有调整。'},
          'midback':{'sc':'维护一份主要承保人财务险团队名单（含近期变动），续保前先核对对口核保人。'},
          'lead':{'sc':'把财务险列为团队能力建设的次级方向，与团体医疗形成组合。'},
          'cross':{'sc':'与再保/核保伙伴保持信息同步，掌握费率和条款松紧。'}},
 rolesImpact={'front':1,'midback':1,'lead':1,'cross':1},
 source={'sc':'Insurance Asia News','lang':'en'},
 boards=['insurer'], themes=['talent','people','underwriting'],
 tags={'sc':['MSIG','财务险','人事任命','核保']},
 publishedAt='2026-11-26T12:12:00+08:00',
 originalUrl='https://insuranceasianews.com/msig-hong-kong-hires-kathy-mak-as-senior-manager-for-financial-lines/'
))

new.append(E(
 id='insuranceasia-asia-cat-loss-76b-gap-20261127',
 clusterCount=1, score=72, verifyStatus='verified', sourceTier='pro', sourceKey='insuranceasia',
 contentKind='news',
 title={'sc':'亚太 2025 年自然灾害损失 760 亿美元　仅 9.2% 有保险 [EN原文]'},
 summary={'sc':'Insurance Asia 11 月 27 日「Behind the Number」报道：Aon 1 月报告指 2025 年亚太自然灾害造成的经济损失至少 760 亿美元，其中仅 9.2%（约 70 亿）有保险，近半受保金额（34 亿）来自澳洲（29 亿）与新西兰（5 亿）。Swiss Re 同年 1 月估算为 650 亿美元、受保比例 8%；亚洲占全球巨灾经济损失约 30%，但新兴亚洲经济体仅 5% 受保，表现最好的市场也只有 22%。SEADRIF 行政总裁 Benedikt Signer 主张扩大风险数据、公私合营融资与把多年期灾害保险纳入公共财政规划；GAIP 行政总裁郑敏红指亚洲资产敞口因城市化与基建在巨灾暴露区快速累积，而保险渗透与风险融资市场未同步。'},
 why={'sc':'保障缺口不再是抽象口号，而是有具体分母的数字：760 亿对 70 亿。对做企业险与参数型产品的团队，真正的机会点在「数据不足导致无法定价」这一环，而不是单纯教育客户买保险。'},
 actions={'front':{'sc':'与企业客户谈财产险时，用「区域受保比例不足一成」说明自留风险之重，再落到自身厂址的巨灾暴露。'},
          'midback':{'sc':'研究参数型（parametric）产品在本地可用的触发指标，评估能否作为传统财产险的补充。'},
          'lead':{'sc':'把气候风险作为企业客户年度检视的固定议题，而非一次性销售话题。'},
          'cross':{'sc':'与再保与经纪伙伴讨论多年期保障结构，为客户争取续保确定性。'}},
 rolesImpact={'front':2,'midback':1,'lead':2,'cross':2},
 source={'sc':'Insurance Asia（引 Aon、Swiss Re 报告及 SEADRIF、GAIP 访谈）','lang':'en'},
 boards=['market'], themes=['catastrophe','protection-gap','apac'],
 tags={'sc':['自然灾害','保障缺口','Aon','Swiss Re','参数型保险']},
 publishedAt='2026-11-27T05:00:00+08:00',
 originalUrl='https://insuranceasia.com/insurance/exclusive/behind-number-natural-disasters-cost-asia-76b-in-2025-yet-less-10-was-insured'
))

new.append(E(
 id='insuranceasia-generali-china-ai-energy-storage-20261127',
 clusterCount=1, score=70, verifyStatus='verified', sourceTier='pro', sourceKey='insuranceasia',
 contentKind='news',
 title={'sc':'Generali 中国把电池安全技术嵌入储能险定价　并推容量衰减保证险 [EN原文]'},
 summary={'sc':'Insurance Asia 11 月 27 日报道，Generali China Insurance 与北京思仪清能（Beijing Syi Tsing Energy Technology）签署战略合作，把电池安全技术嵌入储能电站的核保与定价：以真实运行数据、历史故障记录与电池安全检查建立 AI 核保平台，把电站运行数据转换为标准化风险分数来计算保费，替代传统定价方式；双方并开发储能资产性能保证保险，用结合电化学模型与 AI 的电池寿命预测算法，在电池容量低于预期时补偿资产方。合作框架覆盖出单前风险评估、保单期内实时安全监测与出险后损失评估。'},
 why={'sc':'这是「保险从赔付方变成风险工程参与者」的清晰样本：定价依据从经验费率转成实时运行数据，产品从赔损扩展到赔「性能不达标」。做新能源、工程险或科技企业客户的同事，这类结构未来会向更多资产类别复制。'},
 actions={'front':{'sc':'见新能源或制造客户时，问一句「设备运行数据有没有留、愿不愿意开放给核保」，这直接决定能否拿到更优费率。'},
          'midback':{'sc':'整理「数据换费率」的可行清单：哪些客户已有 IoT/运维数据、可支撑差异化核保。'},
          'lead':{'sc':'把数据化核保列为团队来年学习主题，先做储能/光伏案例研究。'},
          'cross':{'sc':'与科技公司或检测机构探索联合方案，把第三方数据纳入承保流程。'}},
 rolesImpact={'front':2,'midback':2,'lead':2,'cross':3},
 source={'sc':'Insurance Asia','lang':'en'},
 boards=['tech','product'], themes=['ai','underwriting','pricing'],
 tags={'sc':['Generali','储能保险','AI核保','性能保证保险','电池']},
 publishedAt='2026-11-27T06:15:00+08:00',
 originalUrl='https://insuranceasia.com/insurance/news/generali-china-use-ai-in-energy-storage-insurance-pricing'
))

new.append(E(
 id='nfra-misselling-circular-eight-types-20261126',
 clusterCount=1, score=68, verifyStatus='pending', sourceTier='media', sourceKey='nfra',
 contentKind='circular',
 title={'sc':'金融监管总局通报八类保险不当销售行为　五类涉线上：低价诱导、自动扣费、「黑盒」弹窗'},
 summary={'sc':'每日经济新闻 11 月 26 日报道，国家金融监督管理总局办公厅近日向各金融监管局、各银行及保险机构下发《关于保险不当销售有关问题的通报》，归纳 2026 年以来经日常监管、舆情监测与消费投诉发现的八类典型不当销售行为——线下仍有虚假宣传、误导销售等顽疾，线上则出现低价诱导投保、线上自动扣费套路、「黑盒」式广告骚扰等新问题，其中五类涉线上。通报要求各保险公司与保险中介机构对照问题开展自查自纠、严肃整改问责，并健全长效治理机制。通报原文未公开发布，本条目据媒体转述整理。'},
 why={'sc':'八类行为里有五类发生在线上，说明内地监管的抓手已经从「代理人话术」扩到「产品页与扣费链路」。对做跨境或与内地平台合作的团队，这是自查清单的直接来源——尤其是自动续费与广告弹窗这类由产品经理而非代理人决定的设计。'},
 actions={'front':{'sc':'若客户从线上渠道买过内地保单，提醒核对自动续费授权与扣费记录。'},
          'midback':{'sc':'把八类行为逐条对照自有营销物料与落地页，标出可能被认定为「黑盒」或诱导的设计。'},
          'lead':{'sc':'组织一次合规自查，重点是线上投放素材与自动扣费授权文本。'},
          'cross':{'sc':'与内地合作平台确认其宣传与扣费流程，避免连带责任。'}},
 rolesImpact={'front':2,'midback':2,'lead':2,'cross':2},
 source={'sc':'每日经济新闻（引金融监管总局办公厅通报）','lang':'zh'},
 boards=['reg'], themes=['compliance','reg','channel'],
 tags={'sc':['金融监管总局','不当销售','自动扣费','互联网保险','自查']},
 publishedAt='2026-11-26T22:49:00+08:00',
 originalUrl='https://nbd.com.cn/articles/2026-11-26/4660264.html'
))

new.append(E(
 id='mpfa-full-portability-phase1-20261221-20261125',
 clusterCount=1, score=66, verifyStatus='verified', sourceTier='media', sourceKey='hkcd',
 contentKind='news',
 title={'sc':'首阶段强积金「全自由行」12 月 21 日实施　受托人本周起发通知书'},
 summary={'sc':'积金局 11 月 25 日表示，为配合首阶段强积金「全自由行」于 12 月 21 日实施，各受托人本周起陆续向持有雇员供款账户的成员发出通知书，简介相关资讯及管限规则修订。首阶段涵盖 2025 年 5 月 1 日或之后加入职场或开始新工作的雇员，合资格者可在雇员强制供款之外，把现职期间雇主强制供款产生的强积金全数转至自选计划的个人账户，每个公历年 1 次；可经「积金易」应用程式或网页办理，或使用第 MPF(S)–P(P) 号表格。局方提醒先比较基金选择、特点与收费水平，避免「为转而转」。'},
 why={'sc':'这是 MPF 制度自 2000 年以来最实质的一次权限下放，直接影响 2025 年 5 月后入职的每一位客户。对顾问，这是一个天然的服务触点：帮客户判断「要不要转、转到哪」比推销产品更贴合角色，也更容易建立长期信任。'},
 actions={'front':{'sc':'筛出 2025 年 5 月后入职的客户，主动告知新权利并约一次 15 分钟的账户检视。'},
          'midback':{'sc':'准备一份「全自由行决策清单」：现职供款账户余额、目标计划基金选项、收费、转移时点风险。'},
          'lead':{'sc':'把 MPF 检视纳入 Q1 服务节奏，明确「不建议为转而转」的统一口径。'},
          'cross':{'sc':'与受托人对接转移流程与时间表，避免客户在转移空窗期错失市场。'}},
 rolesImpact={'front':3,'midback':2,'lead':2,'cross':1},
 source={'sc':'香港商报（引积金局）','lang':'zh'},
 boards=['market','family'], themes=['retirement','hong-kong','product'],
 tags={'sc':['强积金','全自由行','积金局','积金易','退休规划']},
 publishedAt='2026-11-25T18:29:00+08:00',
 originalUrl='https://hkcd.com/hkcdweb/content/2026/11/25/content_8787347.html'
))

new.append(E(
 id='insuranceasia-marsh-cyber-aviation-20261127',
 clusterCount=1, score=70, verifyStatus='verified', sourceTier='pro', sourceKey='insuranceasia',
 contentKind='news',
 title={'sc':'Marsh 推出航空业专属网络险　覆盖营运中断、数据外泄与监管成本 [EN原文]'},
 summary={'sc':'Insurance Asia 11 月 27 日报道，Marsh 推出专为航空公司设计的网络保险 Cyber Aviation，承保营运中断、数据外泄、监管应对成本与网络勒索，同时覆盖第一方与第三方责任，并可选附加乘客与货运相关费用。Marsh 指单一网络事件即可打乱航班运作、暴露敏感资料并波及关键基础设施与供应商，航空公司的 IT 与 OT 互联（订票平台、航班运作、第三方供应商）令监管与合约责任跨越多重司法管辖区。保单可按航空公司的系统架构及对关键科技供应商的依赖度定制。'},
 why={'sc':'「按行业切分的网络险」正在成为常态：通用网络险难以覆盖 OT 与第三方依赖，行业专属产品因此有溢价空间。对做企业客户的同事，这是一个可复制的思路——先找客户最依赖的那套系统，再谈保障边界。'},
 actions={'front':{'sc':'与企业客户谈网络险时，先画出其关键系统与第三方依赖，再对照现有保单的缺口。'},
          'midback':{'sc':'整理行业专属网络险的产品谱（航空、医疗、制造），作为企业客户方案的补充选项。'},
          'lead':{'sc':'把「OT 与第三方依赖」纳入企业险培训课程。'},
          'cross':{'sc':'与技术供应商或律所合作，为客户做一次网络事件桌面演练。'}},
 rolesImpact={'front':2,'midback':1,'lead':1,'cross':2},
 source={'sc':'Insurance Asia','lang':'en'},
 boards=['product','tech'], themes=['cyber','product','distribution'],
 tags={'sc':['Marsh','网络保险','航空','营运中断','产品发布']},
 publishedAt='2026-11-27T06:30:00+08:00',
 originalUrl='https://insuranceasia.com/insurance/news/marsh-launches-cyber-insurance-airline-operational-disruptions'
))

# --- finalize: convert tc, shorten summary, dedupe, insert ---
def conv_tc(v):
    if isinstance(v, dict):
        if 'sc' in v and 'tc' not in v:
            v['tc'] = zhconv.convert(v['sc'], 'zh-tw')
        for k in list(v.keys()):
            if k not in ('sc', 'tc'):
                conv_tc(v[k])
    elif isinstance(v, list):
        for x in v:
            conv_tc(x)

added, skipped = [], []
for it in new:
    if it['id'] in existing or it['originalUrl'] in urls:
        skipped.append(it['id'])
        continue
    conv_tc(it)
    it['summaryShort'] = {}
    for lang in ('sc', 'tc'):
        s = it['summary'][lang]
        it['summaryShort'][lang] = s if len(s) <= 110 else s[:110].rstrip('，、；') + '…'
    it['tags']['tc'] = [zhconv.convert(t, 'zh-tw') for t in it['tags']['sc']]
    added.append(it)

added.sort(key=lambda x: x['publishedAt'], reverse=True)
items[0:0] = added

d['meta']['generatedAt'] = '2026-11-27T18:08:00+08:00'
d['meta']['itemCount'] = len(items)
n = len(items)
d['meta']['windowNote'] = {'sc': f'本库{n}条。', 'tc': f'本庫{n}條。'}

json.dump(d, open(LIVE, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('added', len(added), 'skipped', len(skipped), skipped)
print('total', len(items))
for it in added:
    print(it['publishedAt'], '|', it['sourceKey'], '|', it['title']['sc'][:46], '| summary', len(it['summary']['sc']))
