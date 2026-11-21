#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""一次性插入 2026-11-16 21:08 采集的条目（复用 18:08 已核条目 + 21:08 新增 2 条）
窗口：2026-11-15 18:08 → 2026-11-16 21:08
"""
import json, os, shutil, importlib.util

BASE = '/Users/leonliang/maoquanqingbao'
LIVE = os.path.join(BASE, 'data', 'live-items.json')
NOW = '2026-11-16T21:08:00+08:00'
SRC = os.path.join(BASE, 'scripts', 'insert-20261116-1808.py')

spec = importlib.util.spec_from_file_location('ins1808', SRC)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)          # 只执行模块顶层，main() 有 __name__ 守卫
ITEMS = list(mod.ITEMS)
mk = mod.mk

# 修正：AXA 原文链接须带 www（无 www 主机不可达）
for it in ITEMS:
    if it['id'] == 'axa-hk-product-renaming-20261116':
        it['originalUrl'] = 'https://www.axa.com.hk/zh/article/change-of-product-name'
    it['ingestedAt'] = NOW

# 11. 投资推广署率团访卢森堡与德国（家办）
ITEMS.append(mk(
    id='govhk-investhk-family-office-europe-20261116',
    score=85, sourceTier='official', sourceKey='govhk', verifyStatus='verified',
    t_sc='投资推广署率团访卢森堡与德国三城　向欧洲家族资本推香港家办枢纽',
    t_tc='投資推廣署率團訪盧森堡與德國三城　向歐洲家族資本推香港家辦樞紐',
    s_sc='投资推广署家族办公室环球总裁方展光率团访问卢森堡、法兰克福及慕尼黑，11 月 15 日结束为期一周行程，与当地家族办公室、家族企业及投资者会面，讨论跨境机遇、家族企业发展与传承。代表团成员包括 Ocean Capital 创始合伙人周运成。',
    s_tc='投資推廣署家族辦公室環球總裁方展光率團訪問盧森堡、法蘭克福及慕尼黑，11 月 15 日結束為期一周行程，與當地家族辦公室、家族企業及投資者會面，討論跨境機遇、家族企業發展與傳承。代表團成員包括 Ocean Capital 創始合伙人周運成。',
    w_sc='欧洲家族资本是香港家办政策这两年最明确要抢的客源。官方带队出访，说明税务宽免、新资本投资者入境计划与单一家办安排这套对外招商口径已定型。对前线的意义不在「家办」名头：这些家族进入亚洲的第一站往往不是设家办，而是先落一张保单或一个传承架构，保险是最容易先碰的产品。',
    w_tc='歐洲家族資本是香港家辦政策這兩年最明確要搶的客源。官方帶隊出訪，說明稅務寬免、新資本投資者入境計劃與單一家辦安排這套對外招商口徑已定型。對前線的意義不在「家辦」名頭：這些家族進入亞洲的第一站往往不是設家辦，而是先落一張保單或一個傳承架構，保險是最容易先碰的產品。',
    a_front=('遇到欧洲背景客户，先问家族在亚洲是否已有实体与传承安排，再谈产品', '遇到歐洲背景客戶，先問家族在亞洲是否已有實體與傳承安排，再談產品'),
    a_mid=('家办招商政策口径会带出跨境架构咨询，涉税与合规问题须转介专业人士', '家辦招商政策口徑會帶出跨境架構諮詢，涉稅與合規問題須轉介專業人士'),
    a_lead=('「欧洲家族南向配置」可作高客沙龙的主题切口', '「歐洲家族南向配置」可作高客沙龍的主題切口'),
    a_cross=('家族企业跨境传承，是家办服务与保险架构最自然的联动点', '家族企業跨境傳承，是家辦服務與保險架構最自然的聯動點'),
    r=(1, 1, 2, 3),
    src='香港政府新闻公报', lang='zh',
    boards=['family', 'market'],
    themes=['family-office', 'wealth-management', 'cross-border'],
    tags_sc=['投资推广署', '家族办公室', '卢森堡', '德国', '跨境传承'],
    tags_tc=['投資推廣署', '家族辦公室', '盧森堡', '德國', '跨境傳承'],
    kind='press', pub='2026-11-16T19:40:00+08:00',
    url='https://www.info.gov.hk/gia/general/202611/16/P2026111600616.htm',
))

# 12. 加州保险局参数型保险法律意见
ITEMS.append(mk(
    id='artemis-california-parametric-opinion-20261116',
    score=70, sourceTier='pro', sourceKey='artemis', verifyStatus='verified',
    t_sc='加州保险局意见函定参数型保险三要件　须有可保利益、真实转移风险、可证损失 [EN原文]',
    t_tc='加州保險局意見函定參數型保險三要件　須有可保利益、真實轉移風險、可證損失 [EN原文]',
    s_sc='加州保险局总法律顾问就 Ceres 7 月的请求发出意见函，明确参数型产品构成「保险」的三项条件：投保人具可保利益、产品真实转移风险、可提供损失证明。Ceres 认为这为加州扩大参数型保险、收窄气候保障缺口铺路；下一任保险专员 2027 年 1 月上任后负责相关费率审批。',
    s_tc='加州保險局總法律顧問就 Ceres 7 月的請求發出意見函，明確參數型產品構成「保險」的三項條件：投保人具可保利益、產品真實轉移風險、可提供損失證明。Ceres 認為這為加州擴大參數型保險、收窄氣候保障缺口鋪路；下一任保險專員 2027 年 1 月上任後負責相關費率審批。',
    w_sc='参数型保险在香港是保监局明确在推的方向（气候模型项目、基差风险较低的产品），但「何时算保险」这个前置法律问题一直没有答案。加州这份意见给出可对照的三要件框架，它决定参数型产品能否进入受监管市场、以及理赔争议时的举证逻辑——不是本地法规，但值得当作监管思路的参照。',
    w_tc='參數型保險在香港是保監局明確在推的方向（氣候模型項目、基差風險較低的產品），但「何時算保險」這個前置法律問題一直沒有答案。加州這份意見給出可對照的三要件框架，它決定參數型產品能否進入受監管市場、以及理賠爭議時的舉證邏輯——不是本地法規，但值得當作監管思路的參照。',
    a_front=('客户问参数型保险时，讲清「触发即赔」与「按实际损失赔」的区别', '客戶問參數型保險時，講清「觸發即賠」與「按實際損失賠」的區別'),
    a_mid=('参数型产品的基差风险与举证要求，须在文件中写明', '參數型產品的基差風險與舉證要求，須在文件中寫明'),
    a_lead=('可作团队培训的监管对照案例，但不可当作香港本地要求引用', '可作團隊培訓的監管對照案例，但不可當作香港本地要求引用'),
    a_cross=('家办若持有气候敏感资产，参数型是可讨论的补位工具', '家辦若持有氣候敏感資產，參數型是可討論的補位工具'),
    r=(2, 2, 1, 2),
    src='Artemis', lang='en',
    boards=['tech', 'market'],
    themes=['parametric', 'regulation', 'climate'],
    tags_sc=['参数型保险', '加州', 'Ceres', '气候风险', '监管框架'],
    tags_tc=['參數型保險', '加州', 'Ceres', '氣候風險', '監管框架'],
    kind='news', pub='2026-11-16T20:40:00+08:00',
    url='https://www.artemis.bm/news/new-california-legal-opinion-sets-guardrails-for-parametric-insurance-deployment-ceres/',
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
    shutil.copy(LIVE, LIVE + '.bak-1116-2108')
    json.dump(d, open(LIVE, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'inserted {len(new)} items, total {len(d["items"])}')
    for it in new:
        print('  +', it['id'], '|', it['publishedAt'])


if __name__ == '__main__':
    main()
