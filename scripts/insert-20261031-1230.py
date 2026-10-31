# -*- coding: utf-8 -*-
import json, os

ROOT = '/Users/leonliang/maoquanqingbao'
PATH = os.path.join(ROOT, 'data', 'live-items.json')
NOW = '2026-10-31T12:30:00+08:00'

NEW = [
{
 "id": "hkma-monetary-stats-sep2026-20261030",
 "publishedAt": "2026-10-30T16:30:00+08:00",
 "originalUrl": "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/10/20261030-7/",
 "sourceKey": "hkma", "sourceTier": "official", "score": 86, "contentKind": "stats",
 "boards": ["market"], "themes": ["存款结构", "人民币存款", "资金流向"],
 "title": {"sc": "金管局：9月总存款升0.4%　人民币存款增2.6%至11,299亿元、贷款年增7.7%",
           "tc": "金管局：9月總存款升0.4%　人民幣存款增2.6%至11,299億元、貸款年增7.7%"},
 "summary": {"sc": "金管局10月30日公布9月货币统计：总存款升0.4%，其中港元存款跌1.1%、外币存款升1.6%，主要反映企业资金调拨；年內总存款与港元存款分别升7.7%和7.3%。人民币存款升2.6%至11,299亿元，9月跨境贸易人民币汇款12,896亿元（8月为11,038亿元）。总贷款升0.7%、年增7.7%；港元贷存比由69.3%升至70.3%。第三季在港使用贷款（含贸易融资）升0.8%，上季为3.0%，其中贸易融资升，建筑、建造、物业发展及投资贷款跌。港元M2及M3按月跌0.8%、按年升7.5%；整体M2按年升10.1%。[EN原文]",
            "tc": "金管局10月30日公布9月貨幣統計：總存款升0.4%，其中港元存款跌1.1%、外幣存款升1.6%，主要反映企業資金調撥；年內總存款與港元存款分別升7.7%和7.3%。人民幣存款升2.6%至11,299億元，9月跨境貿易人民幣匯款12,896億元（8月為11,038億元）。總貸款升0.7%、年增7.7%；港元貸存比由69.3%升至70.3%。第三季在港使用貸款（含貿易融資）升0.8%，上季為3.0%，其中貿易融資升，建築、建造、物業發展及投資貸款跌。港元M2及M3按月跌0.8%、按年升7.5%；整體M2按年升10.1%。[EN原文]"},
 "why": {"sc": "总量看，存款与贷款年比同为+7.7%——钱没离开香港，只是由港元转外币。客户问「资金在不在香港」时，用年比总量比单月波动更有说服力。",
         "tc": "總量看，存款與貸款年比同為+7.7%——錢沒離開香港，只是由港元轉外幣。客戶問「資金在不在香港」時，用年比總量比單月波動更有說服力。"},
 "tags": {"sc": ["金管局", "货币统计", "人民币存款", "贷存比", "资金流向"], "tc": ["金管局", "貨幣統計", "人民幣存款", "貸存比", "資金流向"]},
 "actions": {"front": {"sc": "客户沟通：资金留存香港的官方数据", "tc": "客戶溝通：資金留存香港的官方數據"},
             "midback": {"sc": "宏观跟踪：港元与外币存款切换", "tc": "宏觀跟蹤：港元與外幣存款切換"},
             "lead": {"sc": "团队简报：资金面口径统一", "tc": "團隊簡報：資金面口徑統一"},
             "cross": {"sc": "跨境客户：人民币资金池变化", "tc": "跨境客戶：人民幣資金池變化"}},
 "rolesImpact": {"front": 2, "midback": 3, "lead": 2, "cross": 3},
 "source": {"sc": "香港金融管理局 2026-10-30", "tc": "香港金融管理局 2026-10-30", "name": "hkma", "date": "2026-10-30", "lang": "zh+en"},
 "lang": "zh+en", "verifyStatus": "verified"
},
{
 "id": "hkma-mortgage-survey-sep2026-20261030",
 "publishedAt": "2026-10-30T16:30:00+08:00",
 "originalUrl": "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/10/20261030-5/",
 "sourceKey": "hkma", "sourceTier": "official", "score": 85, "contentKind": "stats",
 "boards": ["market"], "themes": ["按揭市场", "转按", "楼市需求"],
 "title": {"sc": "金管局：9月按揭申请跌10.5%至7,560宗　新批贷款318亿元、转按逆势升14.6%",
           "tc": "金管局：9月按揭申請跌10.5%至7,560宗　新批貸款318億元、轉按逆勢升14.6%"},
 "summary": {"sc": "金管局9月住宅按揭统计：按揭申请按月跌10.5%至7,560宗；新批贷款跌1.1%至318亿港元，其中一手跌6.8%至85亿、二手跌5.7%至144亿、转按升14.6%至89亿；提取贷款跌22.8%至253亿元。H按占比由57%降至52.7%，P按由1.9%降至1.3%。未偿按揭贷款升0.2%至19,803亿元；拖欠比率维持0.11%低位，经重组贷款比率近0%。[EN原文]",
            "tc": "金管局9月住宅按揭統計：按揭申請按月跌10.5%至7,560宗；新批貸款跌1.1%至318億港元，其中一手跌6.8%至85億、二手跌5.7%至144億、轉按升14.6%至89億；提取貸款跌22.8%至253億元。H按佔比由57%降至52.7%，P按由1.9%降至1.3%。未償按揭貸款升0.2%至19,803億元；拖欠比率維持0.11%低位，經重組貸款比率近0%。[EN原文]"},
 "why": {"sc": "转按逆势升、H按占比反而降——客户在锁息而非加杠杆买楼。替做保费融资或按揭挂钩保单的客户盘点时，这张表能分清「真实需求」与「再融资」。",
         "tc": "轉按逆勢升、H按佔比反而降——客戶在鎖息而非加槓桿買樓。替做保費融資或按揭掛鈎保單的客戶盤點時，這張表能分清「真實需求」與「再融資」。"},
 "tags": {"sc": ["金管局", "按揭统计", "转按", "H按", "拖欠比率"], "tc": ["金管局", "按揭統計", "轉按", "H按", "拖欠比率"]},
 "actions": {"front": {"sc": "客户沟通：楼市数据客观解读", "tc": "客戶溝通：樓市數據客觀解讀"},
             "midback": {"sc": "风险披露：按揭挂钩保单压力测试", "tc": "風險披露：按揭掛鈎保單壓力測試"},
             "lead": {"sc": "团队简报：按揭与保费融资联动", "tc": "團隊簡報：按揭與保費融資聯動"},
             "cross": {"sc": "跨境客户：港物业融资安排", "tc": "跨境客戶：港物業融資安排"}},
 "rolesImpact": {"front": 3, "midback": 3, "lead": 2, "cross": 2},
 "source": {"sc": "香港金融管理局 2026-10-30", "tc": "香港金融管理局 2026-10-30", "name": "hkma", "date": "2026-10-30", "lang": "zh+en"},
 "lang": "zh+en", "verifyStatus": "verified"
},
{
 "id": "ibm-taiwan-cyber-h1-2026-20261031",
 "publishedAt": "2026-10-31",
 "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/taiwans-semiconductor-sector-drives-cyber-insurance-to-record-pace-595684.aspx",
 "sourceKey": "insurancebusinessmag", "sourceTier": "media", "score": 65, "contentKind": "stats",
 "boards": ["tech"], "themes": ["网络安全保险", "核保要点", "半导体供应链"],
 "title": {"sc": "台湾网络险上半年保费3.19亿新台币创新高　半导体业占48.7%、理赔仅25万元",
           "tc": "台灣網絡險上半年保費3.19億新台幣創新高　半導體業佔48.7%、理賠僅25萬元"},
 "summary": {"sc": "台湾金管会数据：2026年上半年产险网络险保费3.19亿新台币（约980万美元），全年有望再创新高。半导体业投保约1.56亿元、占48.71%，金融保险业3,978万元、电脑及周边设备2,583万元居后。上半年三类商品合计理赔仅约25万元（约7,700美元）。资料保护责任险由16家承保、占逾85%保费；综合资讯安全险8家；电脑系统诈骗险7家。保险局副局长蔡火炎（Tsai Huo-yen）称投保应为风险管理补充而非替代，核保看行业风险、防护措施与损失纪录，建议备妥第三方审计报告、业务持续计划与危机通报机制。微软2026数字防御报告将台湾列为全球网络威胁暴露第四、亚太第一。[EN原文]",
            "tc": "台灣金管會數據：2026年上半年產險網絡險保費3.19億新台幣（約980萬美元），全年有望再創新高。半導體業投保約1.56億元、佔48.71%，金融保險業3,978萬元、電腦及周邊設備2,583萬元居後。上半年三類商品合計理賠僅約25萬元（約7,700美元）。資料保護責任險由16家承保、佔逾85%保費；綜合資訊安全險8家；電腦系統詐騙險7家。保險局副局長蔡火炎（Tsai Huo-yen）稱投保應為風險管理補充而非替代，核保看行業風險、防護措施與損失紀錄，建議備妥第三方審計報告、業務持續計劃與危機通報機制。微軟2026數字防禦報告將台灣列為全球網絡威脅暴露第四、亞太第一。[EN原文]"},
 "why": {"sc": "网络险核保清单可直接照抄：第三方审计报告、BCP、通报机制——三项齐了才谈得到优惠费率，缺一项就停在标准条款。给科技制造客户做方案时按这三条先自查。",
         "tc": "網絡險核保清單可直接照抄：第三方審計報告、BCP、通報機制——三項齊了才談得到優惠費率，缺一項就停在標準條款。給科技製造客戶做方案時按這三條先自查。"},
 "tags": {"sc": ["网络险", "台湾", "半导体", "核保", "FSC"], "tc": ["網絡險", "台灣", "半導體", "核保", "FSC"]},
 "actions": {"front": {"sc": "客户沟通：网络险核保三件套", "tc": "客戶溝通：網絡險核保三件套"},
             "midback": {"sc": "产品选型：三类网络险分工", "tc": "產品選型：三類網絡險分工"},
             "lead": {"sc": "团队简报：科技客户风险画像", "tc": "團隊簡報：科技客戶風險畫像"},
             "cross": {"sc": "跨境客户：大中华供应链风险", "tc": "跨境客戶：大中華供應鏈風險"}},
 "rolesImpact": {"front": 3, "midback": 3, "lead": 2, "cross": 3},
 "source": {"sc": "Insurance Business Asia 2026-10-31", "tc": "Insurance Business Asia 2026-10-31", "name": "insurancebusinessmag", "date": "2026-10-31", "lang": "en"},
 "lang": "en", "verifyStatus": "verified"
},
{
 "id": "ibm-korea-gyeonggi-climate-heat-20261031",
 "publishedAt": "2026-10-31",
 "originalUrl": "https://www.insurancebusinessmag.com/asia/news/life-insurance/gyeonggi-heat-illness-payouts-quadruple-in-six-months-595682.aspx",
 "sourceKey": "insurancebusinessmag", "sourceTier": "media", "score": 64, "contentKind": "news",
 "boards": ["product"], "themes": ["气候保险", "参数式保险", "普惠保障"],
 "title": {"sc": "韩国京畿道气候保险：中暑诊断给付一年增至1,472宗　新增300万韩圜身故保障",
           "tc": "韓國京畿道氣候保險：中暑診斷給付一年增至1,472宗　新增300萬韓圜身故保障"},
 "summary": {"sc": "韩国京畿道气候保险数据：中暑诊断给付由2025年累计655宗、6,550万韩圜增至1,472宗、2.208亿韩圜（约15.3万美元），单笔给付由10万提高至15万韩圜。截至10月21日，2026年计划共赔付7.522亿韩圜、25,941宗，其中气候脆弱群门诊24,200宗、4.84亿韩圜（占九成以上），急诊165宗、1,650万韩圜，另有4宗气候灾害身故给付1,200万韩圜。计划覆盖约1,440万居民，保费由省政府全额支付、居民自动参保，今年新增300万韩圜身故给付。私营端东洋人寿、KB产险、农协产险及济州岛亦推出高温相关产品，济州采用参数式触发。[EN原文]",
            "tc": "韓國京畿道氣候保險數據：中暑診斷給付由2025年累計655宗、6,550萬韓圜增至1,472宗、2.208億韓圜（約15.3萬美元），單筆給付由10萬提高至15萬韓圜。截至10月21日，2026年計劃共賠付7.522億韓圜、25,941宗，其中氣候脆弱群門診24,200宗、4.84億韓圜（佔九成以上），急診165宗、1,650萬韓圜，另有4宗氣候災害身故給付1,200萬韓圜。計劃覆蓋約1,440萬居民，保費由省政府全額支付、居民自動參保，今年新增300萬韓圜身故給付。私營端東洋人壽、KB產險、農協產險及濟州島亦推出高溫相關產品，濟州採用參數式觸發。[EN原文]"},
 "why": {"sc": "「政府全付保费＋自动参保＋参数式触发」是气候风险最现实的落地形态。跟企业或团体客户谈极端天气保障时，比讲ESG具体：赔付门槛怎么定、谁付保费、覆盖多大人群。",
         "tc": "「政府全付保費＋自動參保＋參數式觸發」是氣候風險最現實的落地形態。跟企業或團體客戶談極端天氣保障時，比講ESG具體：賠付門檻怎麼定、誰付保費、覆蓋多大人群。"},
 "tags": {"sc": ["气候保险", "参数式保险", "京畿道", "团体保单", "极端天气"], "tc": ["氣候保險", "參數式保險", "京畿道", "團體保單", "極端天氣"]},
 "actions": {"front": {"sc": "客户沟通：极端天气的可保边界", "tc": "客戶溝通：極端天氣的可保邊界"},
             "midback": {"sc": "产品参考：参数式触发设计", "tc": "產品參考：參數式觸發設計"},
             "lead": {"sc": "团队简报：气候风险产品谱系", "tc": "團隊簡報：氣候風險產品譜系"},
             "cross": {"sc": "跨境客户：大湾区高温与停工风险", "tc": "跨境客戶：大灣區高溫與停工風險"}},
 "rolesImpact": {"front": 3, "midback": 2, "lead": 2, "cross": 2},
 "source": {"sc": "Insurance Business Asia 2026-10-31", "tc": "Insurance Business Asia 2026-10-31", "name": "insurancebusinessmag", "date": "2026-10-31", "lang": "en"},
 "lang": "en", "verifyStatus": "verified"
},
{
 "id": "ian-am-best-apac-11-renewals-20261030",
 "publishedAt": "2026-10-30T17:38:00+08:00",
 "originalUrl": "https://insuranceasianews.com/strong-underwriting-results-and-capital-strength-shape-asias-1-1-renewals-am-best/",
 "sourceKey": "insuranceasianews", "sourceTier": "pro", "score": 70, "contentKind": "news",
 "boards": ["market"], "themes": ["1.1续保", "承保盈利", "市场分化"],
 "title": {"sc": "AM Best：亚太承保盈利与资本实力改善　1.1续保前整体稳定但市场分化加剧",
           "tc": "AM Best：亞太承保盈利與資本實力改善　1.1續保前整體穩定但市場分化加劇"},
 "summary": {"sc": "AM Best 就亚太市场1月1日续保发表看法：区内保险业整体保持高度稳定，得益于承保结果转好与资产负债表实力持续改善；但成熟市场与新兴市场之间的分化正在扩大。（原文设付费墙，仅摘要段可见，全文待复核）",
            "tc": "AM Best 就亞太市場1月1日續保發表看法：區內保險業整體保持高度穩定，得益於承保結果轉好與資產負債表實力持續改善；但成熟市場與新興市場之間的分化正在擴大。（原文設付費牆，僅摘要段可見，全文待覆核）"},
 "why": {"sc": "续保季的气氛判断：整体稳、分化大——成熟市场（港、日、新加坡）议价空间小，价格战主要打在新兴市场。谈商业险续保前先定位自己在哪个战场。",
         "tc": "續保季的氣氛判斷：整體穩、分化大——成熟市場（港、日、新加坡）議價空間小，價格戰主要打在新興市場。談商業險續保前先定位自己在哪個戰場。"},
 "tags": {"sc": ["AM Best", "亚太", "1.1续保", "承保盈利", "资本实力"], "tc": ["AM Best", "亞太", "1.1續保", "承保盈利", "資本實力"]},
 "actions": {"front": {"sc": "客户沟通：续保议价预期管理", "tc": "客戶溝通：續保議價預期管理"},
             "midback": {"sc": "核保参考：亚太承保周期位置", "tc": "核保參考：亞太承保週期位置"},
             "lead": {"sc": "团队简报：续保季准备", "tc": "團隊簡報：續保季準備"},
             "cross": {"sc": "跨境资产：区域配置视角", "tc": "跨境資產：區域配置視角"}},
 "rolesImpact": {"front": 2, "midback": 3, "lead": 3, "cross": 1},
 "source": {"sc": "InsuranceAsia News 2026-10-30", "tc": "InsuranceAsia News 2026-10-30", "name": "insuranceasianews", "date": "2026-10-30", "lang": "en"},
 "lang": "en", "verifyStatus": "pending"
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
    print('  ', it['id'], '|', it['publishedAt'], '|', it['boards'], 'sumlen', len(it['summary']['sc']))
print('skipped:', skipped)
print('total now:', len(d['items']))
