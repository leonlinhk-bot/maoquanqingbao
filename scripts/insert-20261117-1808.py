#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""一次性插入 2026-11-17 18:08 采集的条目
窗口：2026-11-16 21:08 → 2026-11-17 18:08
"""
import json, os, shutil, importlib.util

BASE = '/Users/leonliang/maoquanqingbao'
LIVE = os.path.join(BASE, 'data', 'live-items.json')
NOW = '2026-11-17T18:08:00+08:00'

spec = importlib.util.spec_from_file_location(
    'insbase', os.path.join(BASE, 'scripts', 'insert-20261116-1808.py'))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)   # main() 有 __name__ 守卫，只取 mk
mk = mod.mk

ITEMS = []

# 1. 香港金融学院《由协助到自主》AI 应用与合规报告
ITEMS.append(mk(
    id='hkma-hkimr-ai-governance-report-20261117',
    score=88, sourceTier='official', sourceKey='hkma', verifyStatus='verified',
    t_sc='金融学院报告：九成金融机构已用或计划用生成式 AI　代理式 13% 已落地、合规场景为主战场',
    t_tc='金融學院報告：九成金融機構已用或計劃用生成式 AI　代理式 13% 已落地、合規場景為主戰場',
    s_sc='香港金融学院辖下货币及金融研究中心 11 月 17 日发表《由协助到自主》报告：已用或计划用生成式 AI 的金融机构达 90%（2025 年为 75%），13% 已落地代理式 AI、56% 计划应用；合规场景 86% 已用或计划，逾七成拟三五年内探索代理式。主要障碍是可解释性与安全。',
    s_tc='香港金融學院轄下貨幣及金融研究中心 11 月 17 日發表《由協助到自主》報告：已用或計劃用生成式 AI 的金融機構達 90%（2025 年為 75%），13% 已落地代理式 AI、56% 計劃應用；合規場景 86% 已用或計劃，逾七成擬三五年內探索代理式。主要障礙是可解釋性與安全。',
    w_sc='这份报告的分量在于把「AI 会不会用」翻篇，直接问「敢不敢让它自己跑」。13% 已落地、56% 在计划，意味着明年起代理式 AI 会大量进入核保、合规监测与客服流程；而合规场景采用率（86%）高于整体，说明监管科技是最先松手的地方。报告的保留项是可解释性与安全——这正是前线与合规拉扯的核心，也决定了「AI 出的建议」能不能直接递给客户。',
    w_tc='這份報告的分量在於把「AI 會不會用」翻篇，直接問「敢不敢讓它自己跑」。13% 已落地、56% 在計劃，意味著明年起代理式 AI 會大量進入核保、合規監測與客服流程；而合規場景採用率（86%）高於整體，說明監管科技是最先鬆手的地方。報告的保留項是可解釋性與安全——這正是前線與合規拉扯的核心，也決定「AI 出的建議」能不能直接遞給客戶。',
    a_front=('对客户讲 AI 时，讲清哪一步由系统建议、哪一步由持牌人拍板，别把 AI 当卖点', '對客戶講 AI 時，講清哪一步由系統建議、哪一步由持牌人拍板，別把 AI 當賣點'),
    a_mid=('团队导入 AI 工具时，先写清可解释性与留痕要求，再谈效率', '團隊導入 AI 工具時，先寫清可解釋性與留痕要求，再談效率'),
    a_lead=('「代理式 AI 明年进入核保与合规」可作年度技术路线的对齐依据', '「代理式 AI 明年進入核保與合規」可作年度技術路線的對齊依據'),
    a_cross=('高客对 AI 参与其保单决策敏感，涉及自动化建议须提前披露', '高客對 AI 參與其保單決策敏感，涉及自動化建議須提前披露'),
    r=(2, 3, 3, 2),
    src='香港金管局（金融学院 / HKIMR）', lang='zh',
    boards=['tech', 'reg'],
    themes=['ai-governance', 'agentic-ai', 'compliance'],
    tags_sc=['金融学院', 'HKIMR', '生成式 AI', '代理式 AI', '合规'],
    tags_tc=['金融學院', 'HKIMR', '生成式 AI', '代理式 AI', '合規'],
    kind='press', pub='2026-11-17',
    url='https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/11/20261117-3/',
))

# 2. 香港年金公司「退休世界 变得更美」公众教育
ITEMS.append(mk(
    id='hkma-hkmca-retire-well-campaign-20261117',
    score=85, sourceTier='official', sourceKey='hkma', verifyStatus='verified',
    t_sc='香港年金公司启动退休公众教育　以 Grasshopper 改编曲推「可持续退休生活」',
    t_tc='香港年金公司啟動退休公眾教育　以 Grasshopper 改編曲推「可持續退休生活」',
    s_sc='香港按揭证券公司旗下香港年金公司 11 月 17 日推出「Retire Well. Live Fully.」公众教育计划，邀组合 Grasshopper 把《世界会变得很美》改编为《退休世界 变得更美》。该公司的说法是，按统计处资料，60 岁男性平均余寿约 86 岁、女性约 90 岁，退休可长达数十年，须从财务、健康、社交多面向规划。',
    s_tc='香港按揭證券公司旗下香港年金公司 11 月 17 日推出「Retire Well. Live Fully.」公眾教育計劃，邀組合 Grasshopper 把《世界會變得很美》改編為《退休世界 變得很美》。該公司的說法是，按統計處資料，60 歲男性平均餘壽約 86 歲、女性約 90 歲，退休可長達數十年，須從財務、健康、社交多面向規劃。',
    w_sc='官方口径里最实用的一句是「退休可能长达数十年」——香港 60 岁男性平均余寿 86、女性 90，意味着退休期动辄 25 至 30 年，比很多储蓄险的缴费加保证期还长。这是终身年金这类「活多久领多久」产品最硬的场景依据，也是客户在长寿风险上最容易低估的一段。用流行曲做公众教育，说明这个议题正从产品推销走向全民警觉。',
    w_tc='官方口徑裡最實用的一句是「退休可能長達數十年」——香港 60 歲男性平均餘壽 86、女性 90，意味著退休期動輒 25 至 30 年，比很多儲蓄險的繳費加保證期還長。這是終身年金這類「活多久領多久」產品最硬的場景依據，也是客戶在長壽風險上最容易低估的一段。用流行曲做公眾教育，說明這個議題正從產品推銷走向全民警覺。',
    a_front=('谈退休规划先算「退休期年数」，再谈产品，客户对长寿风险才有体感', '談退休規劃先算「退休期年數」，再談產品，客戶對長壽風險才有體感'),
    a_mid=('把公众教育素材当客户沟通工具，比自制的收益演示更中性', '把公眾教育素材當客戶溝通工具，比自制的收益演示更中性'),
    a_lead=('长寿风险＋年金可作团队专题课，避免落入收益比较', '長壽風險＋年金可作團隊專題課，避免落入收益比較'),
    a_cross=('家办长辈客户的现金流安排，可用终身年金作底仓讨论', '家辦長輩客戶的現金流安排，可用終身年金作底倉討論'),
    r=(3, 2, 2, 2),
    src='香港金管局（香港年金公司）', lang='zh',
    boards=['family'],
    themes=['retirement', 'annuity', 'longevity-risk'],
    tags_sc=['香港年金公司', 'HKMC', '退休规划', '长寿风险', '公众教育'],
    tags_tc=['香港年金公司', 'HKMC', '退休規劃', '長壽風險', '公眾教育'],
    kind='press', pub='2026-11-17',
    url='https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/11/20261117-5/',
))

# 3. SCMP：代理式 AI 入金融，陈茂波指机构负最终责任
ITEMS.append(mk(
    id='scmp-agentic-ai-accountability-20261117',
    score=66, sourceTier='media', sourceKey='scmp', verifyStatus='verified',
    t_sc='代理式 AI 渗入金融　陈茂波：AI 代理「无牌照可失、无声誉可护」　机构仍负最终责任 [EN原文]',
    t_tc='代理式 AI 滲入金融　陳茂波：AI 代理「無牌照可失、無聲譽可護」　機構仍負最終責任 [EN原文]',
    s_sc='《南华早报》11 月 17 日报道，彭博全球监管论坛在港举行，财政司司长陈茂波指出金融机构对 AI 系统的行为负最终责任，AI 代理「无牌照可失、无声誉可护」；金融学院主管 Valente 主张「人在指挥」，为人机边界设限。报道并引美联储理事 Barr 警告代理式 AI 可能在压力期加速存款外流。',
    s_tc='《南華早報》11 月 17 日報道，彭博全球監管論壇在港舉行，財政司司長陳茂波指出金融機構對 AI 系統的行為負最終責任，AI 代理「無牌照可失、無聲譽可護」；金融學院主管 Valente 主張「人在指揮」，為人機邊界設限。報道並引美聯儲理事 Barr 警告代理式 AI 可能在壓力期加速存款外流。',
    w_sc='「无牌照可失、无声誉可护」是这轮 AI 监管讨论里最锋利的一句：责任无法外包给系统，只能落回持牌机构与持牌人。对保险前线，这句话直接对应销售流程——AI 可以生成建议、可以初筛核保，但署名与责任仍在中介人身上。论坛同时把「AI 加速挤兑」这类系统性风险摆上台面，说明监管关注点已从数据隐私转向稳定性。',
    w_tc='「無牌照可失、無聲譽可護」是這輪 AI 監管討論裡最鋒利的一句：責任無法外包給系統，只能落回持牌機構與持牌人。對保險前線，這句話直接對應銷售流程——AI 可以生成建議、可以初篩核保，但署名與責任仍在中介人身上。論壇同時把「AI 加速擠兌」這類系統性風險擺上台面，說明監管關注點已從數據隱私轉向穩定性。',
    a_front=('用 AI 生成的方案与话术，须自己核过再对客，责任不会随工具转移', '用 AI 生成的方案與話術，須自己核過再對客，責任不會隨工具轉移'),
    a_mid=('团队 AI 使用规范要写明「谁签发、谁负责」，避免责任真空', '團隊 AI 使用規範要寫明「誰簽發、誰負責」，避免責任真空'),
    a_lead=('把「责任归属」纳入 AI 工具选型标准，而非只看效率', '把「責任歸屬」納入 AI 工具選型標準，而非只看效率'),
    a_cross=('高客若用 AI 做资产配置建议，须区分顾问责任与工具责任', '高客若用 AI 做資產配置建議，須區分顧問責任與工具責任'),
    r=(3, 2, 3, 2),
    src='南华早报 SCMP', lang='en',
    boards=['tech', 'reg'],
    themes=['agentic-ai', 'accountability', 'regulation'],
    tags_sc=['代理式 AI', '陈茂波', '责任归属', '彭博论坛', '监管'],
    tags_tc=['代理式 AI', '陳茂波', '責任歸屬', '彭博論壇', '監管'],
    kind='news', pub='2026-11-17T17:00:00+08:00',
    url='https://www.scmp.com/business/banking-finance/article/3374724/agentic-ai-seeps-finance-concerns-grow-over-new-risks-and-blind-spots',
))

# 4. 平安集团整合香港总部进驻西九 IGC
ITEMS.append(mk(
    id='scmp-pingan-hk-hub-igc-20261117',
    score=66, sourceTier='media', sourceKey='scmp', verifyStatus='verified',
    t_sc='平安明年进驻西九高铁站上盖 IGC　整合七家香港子公司　并为深圳 APEC 提供约 6,000 万美元保障 [EN原文]',
    t_tc='平安明年進駐西九高鐵站上蓋 IGC　整合七家香港子公司　並為深圳 APEC 提供約 6,000 萬美元保障 [EN原文]',
    s_sc='平安集团联席 CEO 郭晓涛接受《南华早报》访问称，明年起把平安保险海外、平安银行香港、平安数字银行、平安证券香港、壹账通等七家香港子公司迁入新鸿基西九高铁站上盖 IGC，押注大湾区跨境资金与人流。他指 AI 风控至 9 月创造逾 100 亿元价值、AI 辅助销售逾 500 亿元。',
    s_tc='平安集團聯席 CEO 郭曉濤接受《南華早報》訪問稱，明年起把平安保險海外、平安銀行香港、平安數字銀行、平安證券香港、壹賬通等七家香港子公司遷入新鴻基西九高鐵站上蓋 IGC，押注大灣區跨境資金與人流。他指 AI 風控至 9 月創造逾 100 億元價值、AI 輔助銷售逾 500 億元。',
    w_sc='一家内地综合金融集团把七家香港实体收进高铁站上盖，是「跨境流量在哪、办公室就在哪」的直白表态：西九是高铁 14 分钟到深圳的节点，也是内地客南下的第一落点。值得留意的是它自报的 AI 数字（风控 100 亿、辅助销售 500 亿元价值），这是内地大型险企第一次把 AI 贡献量化到可与保费并列的尺度，港险的 AI 投入叙事会被拿来对照。',
    w_tc='一家內地綜合金融集團把七家香港實體收進高鐵站上蓋，是「跨境流量在哪、辦公室就在哪」的直白表態：西九是高鐵 14 分鐘到深圳的節點，也是內地客南下的第一落點。值得留意的是它自報的 AI 數字（風控 100 億、輔助銷售 500 億元價值），這是內地大型險企第一次把 AI 貢獻量化到可與保費並列的尺度，港險的 AI 投入敘事會被拿來對照。',
    a_front=('内地背景客户问「香港还值不值得来」，可讲实体与基建在加码，而非只讲收益', '內地背景客戶問「香港還值不值得來」，可講實體與基建在加碼，而非只講收益'),
    a_mid=('留意平安系跨境车险、跨境医疗的落地节奏，是渠道竞争的先行指标', '留意平安系跨境車險、跨境醫療的落地節奏，是渠道競爭的先行指標'),
    a_lead=('「内地集团加码香港实体」可作团队信心的外部佐证', '「內地集團加碼香港實體」可作團隊信心的外部佐證'),
    a_cross=('跨境医疗与养老服务的在地化，是高客服务的差异化切口', '跨境醫療與養老的在地化，是高客服務的差異化切口'),
    r=(1, 1, 2, 2),
    src='南华早报 SCMP', lang='en',
    boards=['market', 'insurer'],
    themes=['gba', 'cross-border', 'insurer-strategy'],
    tags_sc=['平安集团', '西九 IGC', '大湾区', '跨境医疗', 'AI 风控'],
    tags_tc=['平安集團', '西九 IGC', '大灣區', '跨境醫療', 'AI 風控'],
    kind='news', pub='2026-11-17',
    url='https://www.scmp.com/business/companies/article/3374528/ping-insurance-relocate-new-hong-kong-office-above-west-kowloon-rail-hub',
))

# 5. AXA 安盛 x 圣雅各福群会「心筑未来」青年计划
ITEMS.append(mk(
    id='axa-futureminds-youth-20261117',
    score=75, sourceTier='insurer', sourceKey='axa', verifyStatus='verified',
    t_sc='AXA 安盛伙圣雅各福群会推「心筑未来」　六个月青年计划练心理韧性与数码习惯',
    t_tc='AXA 安盛夥聖雅各福群會推「心築未來」　六個月青年計劃練心理韌性與數碼習慣',
    s_sc='AXA 安盛香港及澳门与圣雅各福群会 11 月 17 日推出为期六个月「心筑未来」青年计划，2026 年 11 月至 2027 年 4 月招募 16 至 35 岁青年，以体验式工作坊、网上研讨会及创新挑战赛培养心理韧性、健康数码习惯与朋辈领导力，预计惠及近 1,000 名青年。',
    s_tc='AXA 安盛香港及澳門與聖雅各福群會 11 月 17 日推出為期六個月「心築未來」青年計劃，2026 年 11 月至 2027 年 4 月招募 16 至 35 歲青年，以體驗式工作坊、網上研討會及創新挑戰賽培養心理韌性、健康數碼習慣與朋輩領導力，預計惠及近 1,000 名青年。',
    w_sc='这是把自家研究报告转成社区项目的一次示范：AXA 的调查说港人业余日均看屏幕 5.5 小时、18 至 24 岁达 6.4 小时，44% 的 AI 使用者宁愿向 AI 求助而非找朋友。对保险业的意义在需求侧——数码生活与 AI 依赖正在制造新的健康风险敞口，而这些风险会先反映在雇员福利与医疗保障的理赔结构上，再反映在产品设计上。',
    w_tc='這是把自家研究報告轉成社區項目的一次示範：AXA 的調查說港人業餘日均看屏幕 5.5 小時、18 至 24 歲達 6.4 小時，44% 的 AI 使用者寧願向 AI 求助而非找朋友。對保險業的意義在需求側——數碼生活與 AI 依賴正在製造新的健康風險敞口，而這些風險會先反映在僱員福利與醫療保障的理賠結構上，再反映在產品設計上。',
    a_front=('对年轻客户谈健康保障，可从屏幕时间与睡眠切入，比谈保障额自然', '對年輕客戶談健康保障，可從屏幕時間與睡眠切入，比談保障額自然'),
    a_mid=('企业客户谈雇员福利时，心理健康支持是比加保额更容易落的筹码', '企業客戶談僱員福利時，心理健康支持是比加保額更容易落的籌碼'),
    a_lead=('社区项目可作团队 ESG 与品牌素材，但不可当作产品卖点', '社區項目可作團隊 ESG 與品牌素材，但不可當作產品賣點'),
    a_cross=('高客家族的二代心理健康与传承压力，是可轻触的话题', '高客家族的二代心理健康與傳承壓力，是可輕觸的話題'),
    r=(2, 2, 1, 1),
    src='AXA 安盛香港及澳门', lang='zh',
    boards=['insurer'],
    themes=['mental-health', 'youth', 'digital-wellbeing'],
    tags_sc=['AXA 安盛', '圣雅各福群会', '青年', '心理健康', '数码生活'],
    tags_tc=['AXA 安盛', '聖雅各福群會', '青年', '心理健康', '數碼生活'],
    kind='press', pub='2026-11-17',
    url='https://www.axa.com.hk/zh/article/axa-partners-with-st-james-settlement-to-launchfutureminds-project-to-strengthen-youth-mental-resilience-and-foster-healthy-digital-habits_',
))


def main():
    d = json.load(open(LIVE, encoding='utf-8'))
    old = d['items']
    existing_ids = {i['id'] for i in old}
    existing_urls = {(i.get('originalUrl') or '').rstrip('/') for i in old}
    new = []
    for it in ITEMS:
        if it['id'] in existing_ids:
            print('SKIP dup id:', it['id']); continue
        if it['originalUrl'].rstrip('/') in existing_urls:
            print('SKIP dup url:', it['id']); continue
        new.append(it)
    d['items'] = new + old
    d.setdefault('meta', {})
    d['meta']['generatedAt'] = NOW
    d['meta']['itemCount'] = len(d['items'])
    d['meta']['windowNote'] = {'sc': f'本库{len(d["items"])}条。', 'tc': f'本庫{len(d["items"])}條。'}
    shutil.copy(LIVE, LIVE + '.bak-1117-1808')
    json.dump(d, open(LIVE, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'inserted {len(new)} items, total {len(d["items"])}')
    for it in new:
        print('  +', it['id'], '|', it['publishedAt'])


if __name__ == '__main__':
    main()
