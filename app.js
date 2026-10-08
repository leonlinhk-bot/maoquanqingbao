// ══ 数据外链加载（首屏 core.json 小文件 + 后台 items.json 全量）══
// 首屏只等 core.json（约 250KB/gzip 60KB），渲染后静默拉全量并刷新，
// 取代过去把 ~4MB 数据内嵌进 app.js 的做法（首次加载 7s → ~1s）。
window.HKII_DATA = null;
window.HKII_dataReady = (async function () {
  try {
    if (window.HKII_corePromise) {
      // index.html 已在 <head> 后提前并行发起请求（与 app.js 下载并行，首屏更快）
      window.HKII_DATA = await window.HKII_corePromise;
    } else {
      const VER = window.HKII_VER || String(Date.now());
      const r = await fetch('data/core.json?v=' + VER);
      if (!r.ok) throw new Error('HTTP ' + r.status);
      window.HKII_DATA = await r.json();
    }
  } catch (e) {
    window.HKII_DATA = { items: [], meta: {}, stats: {}, boards: [], deepCards: [], digests: {},
      calendar: [], feedFacets: {}, __loadError: String((e && e.message) || e) };
  }
  return window.HKII_DATA;
})();

(async function () {
  const DATA = await window.HKII_dataReady;
  // 数据加载失败：显示可重试的提示（不要白屏）
  if (DATA.__loadError && !(DATA.items || []).length) {
    const _c = document.getElementById('content');
    if (_c) _c.innerHTML = '<div class="panel" style="border-color:#b45309">' +
      '<h3>⚠ 数据加载失败</h3><p>原因：' + String(DATA.__loadError).replace(/</g,'&lt;') + '</p>' +
      '<p style="color:var(--text-dim);font-size:13px">可刷新页面重试；若持续失败请反馈。</p>' +
      '<p><button class="btn primary" onclick="location.reload()">重新加载</button></p></div>';
    return;
  }
  const L = {
    sc: {
      brandName: "猫圈儿港险情报站", brandSub: "维港猫圈儿 · 持牌人情报台", wechat: "公众号：维港猫圈儿",
      foot: "专业参考 · 非销售/投资建议 · 数字请回原文", menu: "菜单",
      roles: [{id:"front",label:"前线IFA"},{id:"midback",label:"中后台合规"},{id:"lead",label:"团队管理"},{id:"cross",label:"跨境架构"}],
      nav: [
        {id:"dashboard",label:"情报看板",ico:"◉"},{id:"pulse",label:"今日脉搏",ico:"◈"},{id:"all",label:"全部动态",ico:"☰"},{id:"daily",label:"角色日报",ico:"▣"},{id:"themes",label:"主题雷达",ico:"◎"},{id:"deeps",label:"监管深度",ico:"◆"},{id:"calendar",label:"事件日历",ico:"◷"},{id:"download",label:"数据下载",ico:"⬇"},{id:"fav",label:"收藏",ico:"☆"},{id:"agent",label:"Agent 接入",ico:"⌘"},{id:"changelog",label:"更新日志",ico:"◌"},{id:"about",label:"关于",ico:"ⓘ"}
      ],
      sec:{c:"内容",a:"接入",m:"更多"},
      views:{
        dashboard:{t:"情报看板",s:"市场数据实时仪表板 · 源头可溯 · 数字搬运"},pulse:{t:"今日脉搏",s:"热点: 近14天官方高分自动上榜 · 精选: 评分×角色匹配动态排序"},
        all:{t:"全部动态",s:"全量信息流 · 按信源/文种细筛（≠主题雷达）"},
        daily:{t:"角色日报",s:"近14天要闻按角色自动聚合"},download:{t:"数据下载",s:"按日/周/月/年打包导出 Markdown · 原文可溯"},
        themes:{t:"主题雷达",s:"六大业务板块地图 · 战略导航，不是信息流细筛"},
        deeps:{t:"监管深度",s:"重大事件完整画像 · 时间线 · 影响矩阵 · FAQ · 关联条目"},calendar:{t:"事件日历",s:"关键事件 · 生效日 · 行业节点"},
        fav:{t:"收藏",s:"保存在本机"},
        agent:{t:"Agent 接入",s:"JSON Feed · RSS · llms.txt"},changelog:{t:"更新日志",s:"功能与数据变更记录"},about:{t:"关于",s:"定位、原则与免责"}
      },
      themes:{reg:"监管",product:"产品",channel:"渠道人力",macro:"宏观资产",par:"分红实现率",uw:"核保理赔",compliance:"合规实操",offshore:"跨境离岸",firm:"机构竞争",tech:"科技运营",career:"职业CPD",intl:"国际对标",taxation:"税务",pricing:"定价",health:"健康医疗",retirement:"退休养老",annuity:"年金",claims:"理赔",underwriting:"核保",distribution:"分销",results:"业绩",reinsurance:"再保险",captive:"专属自保",esg:"ESG",ils:"保险相连证券",natcat:"巨灾",marine:"海事",insurtech:"保险科技",ai:"人工智能",cyber:"网络风险",market:"市场","cross-border":"跨境",statistics:"统计",capital:"资本市场",monetary:"货币",china:"内地",hnw:"高净值",sme:"中小企业","family-office":"家办","global-wealth":"全球财富",benchmark:"对标","identity-planning":"身份规划","global-allocation":"全球配置","fo-ecosystem":"家办生态"},
      tier:{official:"一手监管",insurer:"保司官方",broker:"经纪行",pro:"专业解读",media:"媒体"},
      hot:"热点", allChip:"全部", searchPh:"搜索标题/摘要/标签…", empty:"无匹配结果",
      verified:"已核原文", pending:"待复核", score:"评分", cluster:"源同题", why:"为什么重要",
      actionNow:"今日动作", actionAll:"全角色动作", summary:"摘要", themesH:"主题", effective:"生效 / 相关日期",
      original:"打开原文", note:"核对提示", dayUnit:"条", roleNow:"当前角色", window:"数据截至",
      about1:"猫圈儿港险情报站——专注香港保险监管与行业资讯的聚合导读平台。数据来源：保监局(IA)、金管局(HKMA)、保司官网披露、国际机构研究与权威媒体线索。每条导读均可回追原文，播报时间精确到分钟。",
      about2:"与微信公众号「维港猫圈儿」同一品牌人格：专业、好懂、有温度。站点偏工具与检索；公众号偏解读与陪伴。",
      qrTip:"微信扫码关注，获取每日港险解读与陪伴。",
      principles:"原则", p1:"监管与保司官网资讯优先；媒体/研究作线索，必须可回原文", p2:"同一矿山，按角色切片", p3:"每条精选带「今日动作」", p4:"摘要必须可回原文",
      disclaimer:"免责声明", disc:"内容供香港持牌保险中介及专业人士参考，不构成销售建议、投资建议或法律意见。请以监管与保司原文为准。",
      agentH:"如何接入", agentSub:"三条路径规划与 AI HOT 对齐：网页人读 + RSS/API + Agent Skill。当前原型以网页为准，接口形态如下。",
      a1:"网页：每日打开「今日脉搏 / 全部动态 / 角色日报」，用顶部角色切片视图。",
      a2:"RSS / REST API（下一阶段）：匿名只读、稳定契约；API 轮询建议 ≥60s，RSS ≥30 分钟；收到 429 按 Retry-After 退避。",
      a3:"Agent Skill（下一阶段）：安装一次后用中文问「过去24小时五件大事」；返回时间窗、中文摘要与站内/原文链接。",
      agentUseH:"接入后怎么用",
      agentUse1:"按角色提问：前线 IFA / 中后台合规 / 团队管理 / 跨境架构。",
      agentUse2:"要时间线：例如「佣金分摊 / 转介费 / 演示利率上限」相关规则按生效日排序。",
      agentUse3:"增量同步：首次 snapshot 全量精选，之后只拉 changes（规划中）。",
      agentUse4:"导出：数据下载页按日/周/月/年导出 Markdown，或单条详情导出。",
      agentEx:"示例问法",
      agentCode:"过去 24 小时港险监管与产品最重要的 5 件事？\n只给我中后台合规视角，忽略促销。\n佣金分摊与转介费相关规则时间线。\n把本周精选同步成 Markdown 清单。",
      agentDiscH:"使用与免责（重要）",
      agentDisc1:"摘要与动作卡由人工/AI 二次整理，数字、政策与原话引用前必须打开原文 URL 复核。",
      agentDisc2:"对外发布请保留来源与 canonical；本站导读不构成销售建议、投资建议或法律意见。",
      agentDisc3:"公开可读 ≠ 可忽略版权与频率合同；禁止批量绕过限流的爬取。",
      agentDisc4:"v1 接口不删除/改名既有字段类型（规划）；不承诺 SLA，请自备缓存与降级。",
      agentDisc5:"角色切片仅改变排序与动作卡，不改变事实本身。",
      hotSearch:"大家都在搜", hotSearchTerms:[
        "分红实现率","佣金递延","演示利率上限","保费融资","GN16",
        "CPD学时","家办税务","跨境理财通","转介费","RBC"
      ],
      themesIntro:"点击主题进入全部动态并筛选。", calH:"关键节点", dailyArchive:"往期快速回看", dailyLead:"近14天高分条目按4个角色自动聚合 · 与主题雷达分工：雷达看主题结构，日报看时间快照",
      evergreen:"生效中 · 常驻",
      archiveTabs:{daily:"日报",weekly:"周报",monthly:"月报",yearly:"年报"},
      downloadHint:"日报、周报可下载 Markdown。月报、年报仅可在线查阅，不提供下载。也可发送到邮箱。数字与规则以原文链接为准。",
      openDigest:"查看该期条目",
      backDownload:"返回列表",emailTo:"📧 发送到邮箱",emailSent:"已打开邮箱",emailHint:"将打开默认邮件客户端，发送日报到你的邮箱",monthlyYearlyReadOnly:"月报与年报仅可在线查阅，不提供下载。",
      guideLabel:"本站导读（非原文）",
      originalAuthority:"权威原文",
      sourceKey:"来源指纹",
      positionH:"定位",
      fidelity:"内容纪律",
      fidelityText:"我们只做资讯聚合与导读索引：不篡改原文，不建分红实现率数仓。摘要/动作卡为二次整理；数字与规则以原文链接为准。",
      itemsInPeriod:"本期条目",
      noDigest:"该周期暂无可下载内容。",
      searchDownload:"在下载包标题中筛选…",
      boardBack:"返回主题地图",
      boardCount:"条导读",
      boardViewAll:"本板块全部条目",
      boardLatest:"本板块最新",
      boardMap:"主题地图",
      boardHint:"六大板块=业务地图（导航维度）。「全部动态」=信息流细筛（信源类型×文种）。两套维度，不要当成同一个过滤器。",
      exportMd:"导出 Markdown",
      posterBtn:"朋友圈海报",
      posterTitle:"朋友圈海报",
      posterTip:"竖版 4:5，适合发朋友圈。只提炼可公开要点；不含佣金细节与收益承诺。请再人工过目。",
      posterDl:"下载 PNG",
      posterCopy:"复制文案",
      mdDone:"已下载 Markdown",
      copyDone:"文案已复制",
      pointsLabel:"积分",
      earnShare:"+5 分享",
      digestExport:"导出本期 MD",
      proLock:"Pro / 积分",
      proNeed:"需要 {n} 积分或 Pro（演示）。当前对内可关闭付费锁。",
      proFree:"免费下载",
      unlocked:"已解锁下载",
      momentsOk:"适合朋友圈",
      momentsNo:"偏专业内部，建议仅团队转发",



      facetSource:"信源", facetKind:"文种", facetHint:"细筛维度 · 与左侧「主题雷达」六大板块不同", sourcesCatalogH:"信源目录", dark:"深色", light:"浅色", week:["日","一","二","三","四","五","六"], weekPrefix:"星期"
    },
    tc: {
      brandName: "貓圈兒港險情報站", brandSub: "維港貓圈兒 · 持牌人情報台", wechat: "公眾號：維港貓圈兒",
      foot: "專業參考 · 非銷售/投資建議 · 數字請回原文", menu: "選單",
      roles: [{id:"front",label:"前線IFA"},{id:"midback",label:"中後台合規"},{id:"lead",label:"團隊管理"},{id:"cross",label:"跨境架構"}],
      nav: [
        {id:"dashboard",label:"情报看板",ico:"◉"},{id:"pulse",label:"今日脈搏",ico:"◈"},{id:"all",label:"全部動態",ico:"☰"},{id:"daily",label:"角色日報",ico:"▣"},{id:"themes",label:"主題雷達",ico:"◎"},{id:"deeps",label:"監管深度",ico:"◆"},{id:"calendar",label:"事件日曆",ico:"◷"},{id:"download",label:"數據下載",ico:"⬇"},{id:"fav",label:"收藏",ico:"☆"},{id:"agent",label:"Agent 接入",ico:"⌘"},{id:"changelog",label:"更新日誌",ico:"◌"},{id:"about",label:"關於",ico:"ⓘ"}
      ],
      sec:{c:"內容",a:"接入",m:"更多"},
      views:{
        dashboard:{t:"情報看板",s:"市場數據實時儀表板 · 源頭可溯 · 數字搬運"},pulse:{t:"今日脈搏",s:"熱點: 近14天官方高分自動上榜 · 精選: 評分×角色匹配動態排序"},
        all:{t:"全部動態",s:"全量資訊流 · 按信源/文種細篩（≠主題雷達）"},
        daily:{t:"角色日報",s:"近14天要聞按角色自動聚合"},download:{t:"數據下載",s:"按日/週/月/年打包導出 Markdown · 原文可溯"},
        themes:{t:"主題雷達",s:"六大業務板塊地圖 · 戰略導航，不是資訊流細篩"},
        deeps:{t:"監管深度",s:"重大事件完整畫像 · 時間線 · 影響矩陣 · FAQ · 關聯條目"},calendar:{t:"事件日曆",s:"關鍵事件 · 生效日 · 行業節點"},
        fav:{t:"收藏",s:"保存在本機"},
        agent:{t:"Agent 接入",s:"JSON Feed · RSS · llms.txt"},changelog:{t:"更新日誌",s:"功能與數據變更記錄"},about:{t:"關於",s:"定位、原則與免責"}
      },
      themes:{reg:"監管",product:"產品",channel:"渠道人力",macro:"宏觀資產",par:"分紅實現率",uw:"核保理賠",compliance:"合規實操",offshore:"跨境離岸",firm:"機構競爭",tech:"科技運營",career:"職業CPD",intl:"國際對標",taxation:"稅務",pricing:"定價",health:"健康醫療",retirement:"退休養老",annuity:"年金",claims:"理賠",underwriting:"核保",distribution:"分銷",results:"業績",reinsurance:"再保險",captive:"專屬自保",esg:"ESG",ils:"保險相連證券",natcat:"巨災",marine:"海事",insurtech:"保險科技",ai:"人工智能",cyber:"網絡風險",market:"市場","cross-border":"跨境",statistics:"統計",capital:"資本市場",monetary:"貨幣",china:"內地",hnw:"高淨值",sme:"中小企業","family-office":"家辦","global-wealth":"全球財富",benchmark:"對標","identity-planning":"身份規劃","global-allocation":"全球配置","fo-ecosystem":"家辦生態"},
      tier:{official:"一手監管",insurer:"保司官方",broker:"經紀行",pro:"專業解讀",media:"媒體"},
      hot:"當前熱點", allChip:"全部", searchPh:"搜尋標題 / 摘要 / 標籤…", empty:"沒有匹配的條目。",
      verified:"已核原文", pending:"待複核", score:"評分", cluster:"源同題", why:"為什麼重要",
      actionNow:"今日動作", actionAll:"全角色動作", summary:"摘要", themesH:"主題", effective:"生效 / 相關日期",
      original:"打開原文", note:"核對提示", dayUnit:"條", roleNow:"當前角色", window:"數據窗口",
      about1:"貓圈兒港險情報站——專注香港保險監管與行業資訊的聚合導讀平台。數據來源：保監局(IA)、金管局(HKMA)、保司官網披露、國際機構研究與權威媒體線索。每條導讀均可回追原文，播報時間精確到分鐘。",
      about2:"與微信公眾號「維港貓圈兒」同一品牌人格：專業、好懂、有溫度。站點偏工具與檢索；公眾號偏解讀與陪伴。",
      qrTip:"微信掃碼關注，獲取每日港險解讀與陪伴。",
      principles:"原則", p1:"監管與保司官網資訊優先；媒體/研究作線索，必須可回原文", p2:"同一礦山，按角色切片", p3:"每條精選帶「今日動作」", p4:"摘要必須可回原文",
      disclaimer:"免責聲明", disc:"內容供香港持牌保險中介及專業人士參考，不構成銷售建議、投資建議或法律意見。請以監管與保司原文為準。",
      agentH:"如何接入", agentSub:"三條路徑規劃與 AI HOT 對齊：網頁人讀 + RSS/API + Agent Skill。當前原型以網頁為準，接口形態如下。",
      a1:"網頁：每日打開「今日脈搏 / 全部動態 / 角色日報」，用頂部角色切片視圖。",
      a2:"RSS / REST API（下一階段）：匿名只讀、穩定契約；API 輪詢建議 ≥60s，RSS ≥30 分鐘；收到 429 按 Retry-After 退避。",
      a3:"Agent Skill（下一階段）：安裝一次後用中文問「過去24小時五件大事」；返回時間窗、中文摘要與站內/原文連結。",
      agentUseH:"接入後怎麼用",
      agentUse1:"按角色提問：前線 IFA / 中後台合規 / 團隊管理 / 跨境架構。",
      agentUse2:"要時間線：例如「佣金分攤 / 轉介費 / 演示利率上限」相關規則按生效日排序。",
      agentUse3:"增量同步：首次 snapshot 全量精選，之後只拉 changes（規劃中）。",
      agentUse4:"導出：數據下載頁按日/週/月/年導出 Markdown，或單條詳情導出。",
      agentEx:"示例問法",
      agentCode:"過去 24 小時港險監管與產品最重要的 5 件事？\n只給我中後台合規視角，忽略促銷。\n佣金分攤與轉介費相關規則時間線。\n把本週精選同步成 Markdown 清單。",
      agentDiscH:"使用與免責（重要）",
      agentDisc1:"摘要與動作卡由人工/AI 二次整理，數字、政策與原話引用前必須打開原文 URL 複核。",
      agentDisc2:"對外發布請保留來源與 canonical；本站導讀不構成銷售建議、投資建議或法律意見。",
      agentDisc3:"公開可讀 ≠ 可忽略版權與頻率合同；禁止批量繞過限流的爬取。",
      agentDisc4:"v1 接口不刪除/改名既有字段類型（規劃）；不承諾 SLA，請自備緩存與降級。",
      agentDisc5:"角色切片僅改變排序與動作卡，不改變事實本身。",
      hotSearch:"大家都在搜", hotSearchTerms:[
        "分紅實現率","佣金遞延","演示利率上限","保費融資","GN16",
        "CPD學時","家辦稅務","跨境理財通","轉介費","RBC"
      ],
      themesIntro:"點擊主題進入全部動態並篩選。", calH:"關鍵節點", dailyArchive:"往期快速回看", dailyLead:"近14天高分條目按4個角色自動聚合 · 與主題雷達分工：雷達看主題結構，日報看時間快照",
      evergreen:"生效中 · 常駐",
      archiveTabs:{daily:"日報",weekly:"週報",monthly:"月報",yearly:"年報"},
      downloadHint:"日報、週報可下載 Markdown。月報、年報僅可在線查閱，不提供下載。也可發送到郵箱。數字與規則以原文鏈接為準。",
      openDigest:"查看該期條目",
      backDownload:"返回列表",emailTo:"📧 發送到郵箱",emailSent:"已打開郵箱",emailHint:"將打開默認郵件客戶端，發送日報到你的郵箱",monthlyYearlyReadOnly:"月報與年報僅可在線查閱，不提供下載。",
      guideLabel:"本站導讀（非原文）",
      originalAuthority:"權威原文",
      sourceKey:"來源指紋",
      positionH:"定位",
      fidelity:"內容紀律",
      fidelityText:"我們只做資訊聚合與導讀索引：不篡改原文，不建分紅實現率數倉。摘要/動作卡為二次整理；數字與規則以原文連結為準。",
      itemsInPeriod:"本期條目",
      noDigest:"該週期暫無可下載內容。",
      searchDownload:"在下載包標題中篩選…",
      boardBack:"返回主題地圖",
      boardCount:"條導讀",
      boardViewAll:"本板塊全部條目",
      boardLatest:"本板塊最新",
      boardMap:"主題地圖",
      boardHint:"六大板塊=業務地圖（導航維度）。「全部動態」=資訊流細篩（信源類型×文種）。兩套維度，不要當成同一個過濾器。",
      exportMd:"導出 Markdown",
      posterBtn:"朋友圈海報",
      posterTitle:"朋友圈海報",
      posterTip:"豎版 4:5，適合發朋友圈。只提煉可公開要點；不含佣金細節與收益承諾。請再人工過目。",
      posterDl:"下載 PNG",
      posterCopy:"複製文案",
      mdDone:"已下載 Markdown",
      copyDone:"文案已複製",
      pointsLabel:"積分",
      earnShare:"+5 分享",
      digestExport:"導出本期 MD",
      proLock:"Pro / 積分",
      proNeed:"需要 {n} 積分或 Pro（演示）。當前對內可關閉付費鎖。",
      proFree:"免費下載",
      unlocked:"已解鎖下載",
      momentsOk:"適合朋友圈",
      momentsNo:"偏專業內部，建議僅團隊轉發",



      facetSource:"信源", facetKind:"文種", facetHint:"細篩維度 · 與左側「主題雷達」六大板塊不同", sourcesCatalogH:"信源目錄", dark:"深色", light:"淺色", week:["日","一","二","三","四","五","六"], weekPrefix:"星期"
    }
  };

  const state = {
    view: "pulse",
    role: (function(){ let r=localStorage.getItem("hkii_role")||"front"; if(r==="mid"||r==="back") r="midback"; if(r==="manage") r="lead"; return r; })(),
    theme: localStorage.getItem("hkii_theme") || "auto",
    lang: localStorage.getItem("hkii_lang") || "sc",
    q: localStorage.getItem("hkii_q")||"", themeFilter: localStorage.getItem("hkii_themeFilter")||"all", feedTier: localStorage.getItem("hkii_feedTier")||"all", feedKind: localStorage.getItem("hkii_feedKind")||"all", selectedId: null, archivePeriod: "daily", archiveKey: null, archiveQ: "", archivePage: 1, themeBoard: null, points: Number(localStorage.getItem("hkii_points")||"20"), pro: localStorage.getItem("hkii_pro")==="1",
    fav: new Set(JSON.parse(localStorage.getItem("hkii_fav") || "[]")),
    posterTheme: localStorage.getItem("hkii_posterTheme") || "dark",
  };

  const $ = (s, el=document) => el.querySelector(s);
  const $$ = (s, el=document) => [...el.querySelectorAll(s)];
  const T = () => L[state.lang];
  const tx = (o) => !o ? "" : (typeof o === "string" ? o : (o[state.lang] || o.sc || o.tc || ""));
  const esc = (s) => String(s??"").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");

  // ===== 搜索累计（本地）+ 使用度上报（方案 B：Cloudflare Worker） =====
  const SEARCH_LOG_KEY = "hkii_search_log";
  const USAGE_ENDPOINT = (typeof window !== "undefined" && window.HKII_USAGE_ENDPOINT) || "";
  const GLOBAL_HOT_KEY = "hkii_global_hot";
  const GLOBAL_HOT_TS = "hkii_global_hot_ts";
  function loadSearchLog(){
    try { return JSON.parse(localStorage.getItem(SEARCH_LOG_KEY) || "{}"); }
    catch(e){ return {}; }
  }
  // 拼音中间态特征：纯字母 + 含撇号（如 zhuan'jie、zhuan'ji'er），应过滤
  const isPinyinJunk = (k) => /^[a-z']+$/i.test(k) && k.includes("'");
  // fire-and-forget 上报；无 endpoint 时静默跳过（本地开发/未部署）
  function trackEvent(type, value){
    if(!USAGE_ENDPOINT) return;
    const payload = { t: String(type||"").slice(0,16), v: value == null ? undefined : String(value).slice(0,80), r: state.role || undefined };
    try {
      const body = JSON.stringify(payload);
      if(navigator.sendBeacon){
        const blob = new Blob([body], { type: "application/json" });
        navigator.sendBeacon(USAGE_ENDPOINT.replace(/\/$/,"") + "/e", blob);
      } else {
        fetch(USAGE_ENDPOINT.replace(/\/$/,"") + "/e", { method:"POST", headers:{"Content-Type":"application/json"}, body, keepalive:true, mode:"cors" }).catch(()=>{});
      }
    } catch(e){}
  }
  function recordSearch(term){
    const t = String(term||"").trim();
    if(!t || t.length < 2) return;
    if(isPinyinJunk(t)) return; // 不记录拼音中间态
    const log = loadSearchLog();
    log[t] = (log[t]||0) + 1;
    try { localStorage.setItem(SEARCH_LOG_KEY, JSON.stringify(log)); } catch(e){}
    trackEvent("search", t);
  }
  function loadHotTerms(){
    // 优先「大家」热搜（Worker 聚合，缓存 1h），再拼本地 + 默认词
    let global = [];
    try {
      const ts = parseInt(localStorage.getItem(GLOBAL_HOT_TS)||"0",10)||0;
      if(Date.now() - ts < 3600*1000){
        global = JSON.parse(localStorage.getItem(GLOBAL_HOT_KEY)||"[]") || [];
      }
    } catch(e){ global = []; }
    const log = loadSearchLog();
    const local = Object.entries(log)
      .filter(([k]) => !isPinyinJunk(k))
      .sort((a,b)=>b[1]-a[1]).map(x=>x[0]);
    const defaults = T().hotSearchTerms || [];
    const seen = new Set();
    const merged = [];
    for(const x of [...global, ...local, ...defaults]){
      if(!x || seen.has(x) || isPinyinJunk(x)) continue;
      seen.add(x); merged.push(x);
      if(merged.length >= 10) break;
    }
    return merged;
  }
  // 后台拉「大家」热搜（有 endpoint 才跑；失败静默）
  function refreshGlobalHot(){
    if(!USAGE_ENDPOINT) return;
    try {
      const ts = parseInt(localStorage.getItem(GLOBAL_HOT_TS)||"0",10)||0;
      if(Date.now() - ts < 3600*1000) return; // 1h 内不重拉
    } catch(e){}
    fetch(USAGE_ENDPOINT.replace(/\/$/,"") + "/hot?n=20&days=14", { mode:"cors" })
      .then(r => r.ok ? r.json() : null)
      .then(d => {
        if(!d || !d.ok || !Array.isArray(d.items)) return;
        const terms = d.items.map(x => x.term).filter(Boolean);
        try {
          localStorage.setItem(GLOBAL_HOT_KEY, JSON.stringify(terms));
          localStorage.setItem(GLOBAL_HOT_TS, String(Date.now()));
        } catch(e){}
      }).catch(()=>{});
  }


  // Auto theme listener
  if(!window._themeListenerAdded){
    window._themeListenerAdded = true;
    window.matchMedia("(prefers-color-scheme: light)").addEventListener("change", () => {
      if(state.theme === "auto") applyChrome();
    });
  }
  function applyChrome() {
    const t = T();
    document.documentElement.lang = state.lang === "tc" ? "zh-Hant" : "zh-Hans";
    const effectiveTheme = state.theme === "auto" 
      ? (window.matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark")
      : state.theme;
    document.documentElement.setAttribute("data-theme", effectiveTheme);
    document.title = t.brandName;
    $("#brandName").textContent = t.brandName;
    $("#brandSub").textContent = t.brandSub;
    $("#wechatPill").textContent = t.wechat;
    $("#footNote").textContent = t.foot;
    const pb=$("#pointsBar");
    if(pb){ pb.textContent = ""; }
    $("#menuBtn").textContent = t.menu;
    $("#q").placeholder = t.searchPh;
    // 大家都在搜 dropdown
    const hd=$("#hotsearchDropdown"); const hl=$("#hotsearchList");
    if(hd&&hl){
      const _terms = loadHotTerms();
      if(_terms.length) hl.innerHTML=_terms.map((x,i)=>`<span class="hotsearch-item" data-hotsearch="${esc(x)}"><span class="rank">${i+1}</span>${esc(x)}</span>`).join("");
    }
    // Search box focus/blur for dropdown
    const qEl=$("#q"); const sb=$("#searchBox");
    if(qEl&&!qEl._hsBound){
      qEl._hsBound=true;
      qEl.addEventListener("focus",()=>{ if(hd) hd.style.display=""; });
      qEl.addEventListener("blur",()=>{ setTimeout(()=>{ if(hd) hd.style.display="none"; },200); });
    }
    $$("[data-lang]").forEach(b => b.classList.toggle("on", b.dataset.lang === state.lang));
    $$("[data-theme-btn]").forEach(b => {
      b.classList.toggle("on", b.dataset.themeBtn === state.theme);
      b.textContent = b.dataset.themeBtn === "dark" ? t.dark : (b.dataset.themeBtn === "light" ? t.light : "跟随系统");
    });
    const n = t.nav;
    $("#nav").innerHTML = `
      <div class="nav-section">${t.sec.c}</div>
      ${n.slice(0,9).map(x=>`<button class="nav-item ${state.view===x.id?'active':''}" data-view="${x.id}"><span class="ico">${x.ico}</span>${x.label}</button>`).join("")}
      <div class="nav-section">${t.sec.a}</div>
      ${n.slice(9,11).map(x=>`<button class="nav-item ${state.view===x.id?'active':''}" data-view="${x.id}"><span class="ico">${x.ico}</span>${x.label}</button>`).join("")}
      <div class="nav-section">${t.sec.m}</div>
      ${n.slice(11).map(x=>`<button class="nav-item ${state.view===x.id?'active':''}" data-view="${x.id}"><span class="ico">${x.ico}</span>${x.label}</button>`).join("")}`;
    $("#rolePills").innerHTML = t.roles.map(r => `<button type="button" class="pill ${state.role===r.id?'on':''}" data-role="${r.id}">${r.label}</button>`).join("");
  }

  const byId = id => DATA.items.find(x => x.id === id);
  const roleScore = it => ((it.rolesImpact&&it.rolesImpact[state.role])||0)*6 + (it.score||70) + (it.featured?4:0);
  // 容错取主题标签：tags.sc/tc 必须是数组；历史上曾有条目写成字符串（"A|B|C"）
  // 导致 .slice().map is not a function → 整个列表渲染崩溃、页面空白
  function tagList(it, lang){
    const t = it && it.tags;
    if (!t) return [];
    let v = (lang && t[lang]) || t.sc || t.tc || [];
    if (typeof v === "string") v = v.split("|").map(s => s.trim()).filter(Boolean);
    return Array.isArray(v) ? v : [];
  }
  function matches(it) {
    if (!state.q.trim()) return true;
    const q = state.q.trim().toLowerCase();
    const tags = tagList(it, state.lang);
    return [tx(it.title), tx(it.summary), tx(it.why), tags.join(" ")].join(" ").toLowerCase().includes(q);
  }
  // 语义搜索（本地轻量实现：字符 bigram + Jaccard 相似度，无需外部 API）
  function bigrams(s){
    const t = String(s||"").toLowerCase().replace(/[\s\p{P}\p{S}]+/gu,"");
    const set = new Set();
    for(let i=0; i<t.length-1; i++) set.add(t.slice(i, i+2));
    return set;
  }
  function jaccard(a, b){
    if(!a.size || !b.size) return 0;
    let inter = 0;
    for(const x of a) if(b.has(x)) inter++;
    return inter / (a.size + b.size - inter);
  }
  function itemText(it){
    return [tx(it.title), tx(it.summary), tx(it.why), tagList(it).join(" ")].join(" ");
  }
  // Fav tags
  state.favTag = null;

  function favTags() {
    const items = DATA.items.filter(i => state.fav.has(i.id));
    const tags = new Set();
    for (const it of items) {
      for (const t of tagList(it)) tags.add(t);
    }
    return [...tags].sort();
  }

  function list({featuredOnly=false,favOnly=false,forceTime=false,pulseSort=false,roleWeights=null,items:extItems=null,page=1,pageSize=20}={}) {
    let arr = (DATA.items||[]).slice();
    if (favOnly) {
      arr = arr.filter(i=>state.fav.has(i.id));
      if (state.favTag) {
        arr = arr.filter(i => ((i.tags||{}).sc||[]).includes(state.favTag));
      }
    }
    // 全部动态：信源 × 文种（细维度）
    if (state.view === "all") {
      if (state.feedTier && state.feedTier !== "all") arr = arr.filter(i => i.sourceTier === state.feedTier);
      if (state.feedKind && state.feedKind !== "all") arr = arr.filter(i => (i.contentKind || "other") === state.feedKind);
    } else if (state.themeFilter && state.themeFilter !== "all") {
      // 脉搏等：仍可用主题码（非六大板块）
      arr = arr.filter(i => (i.themes || []).includes(state.themeFilter) || (i.boards || []).includes(state.themeFilter));
    }
    const _pool = arr.slice(); // matches 过滤前的池（已含 tier/theme 过滤）
    arr = arr.filter(matches);
    // 语义搜索兜底：关键词 0 命中时，用 bigram 相似度推荐相关条目
    if(state.q.trim() && arr.length === 0 && !pulseSort){
      const qs = bigrams(state.q);
      arr = _pool.map(i => ({i, s: jaccard(qs, bigrams(itemText(i)))}))
        .filter(x => x.s >= 0.03)
        .sort((a,b) => b.s - a.s)
        .slice(0, 12)
        .map(x => x.i);
    }
    // 今日脉搏：动态评分排序
  if (pulseSort && roleWeights) {
    // 统一门槛：score ≥ 80，控制精选数量
    arr = arr.filter(i => (i.score||0) >= 80);
    // 时间优先：近14天排前（时间倒序），历史精选排后（角色加权）——避免「角色匹配高」的老条目永久霸榜
    const _w = (i) => (i.score||0)*0.7 + ((i.rolesImpact||{}).front||0)*(roleWeights.front||0) + ((i.rolesImpact||{}).midback||0)*(roleWeights.midback||0) + ((i.rolesImpact||{}).lead||0)*(roleWeights.lead||0) + ((i.rolesImpact||{}).cross||0)*(roleWeights.cross||0);
    const _cut = new Date(Date.now() - 14*24*3600*1000).toISOString().slice(0,10);
    const recent = arr.filter(i => (i.publishedAt||"").slice(0,10) >= _cut)
      .sort((a,b) => (b.publishedAt||"").localeCompare(a.publishedAt||"") || (b.score||0)-(a.score||0));
    const history = arr.filter(i => (i.publishedAt||"").slice(0,10) < _cut)
      .sort((a,b) => _w(b) - _w(a));
    return recent.concat(history).slice(0, 50);
  }
  // 收藏：支持标签筛选；筛选不改变排序键
    if (forceTime || true) {
      arr.sort((a,b)=> (b.publishedAt||"").localeCompare(a.publishedAt||"") || (b.score||0)-(a.score||0));
    } else {
      arr.sort((a,b)=> roleScore(b)-roleScore(a) || (b.publishedAt||"").localeCompare(a.publishedAt||""));
    }
    return arr;
  }
  function byPublishedDesc(a,b){
    return (b.publishedAt||"").localeCompare(a.publishedAt||"") || (b.score||0)-(a.score||0);
  }
  function fmtTime(iso){
    if(!iso) return "";
    // 优先用字符串内时间，避免 UTC 偏移导致「时间乱」
    const m = String(iso).match(/T(\d{2}):(\d{2})/);
    if(m) return m[1]+":"+m[2];
    const d=new Date(iso); return String(d.getHours()).padStart(2,"0")+":"+String(d.getMinutes()).padStart(2,"0");
  }
    function fmtCardTime(it){
    const iso=it.publishedAt||"";
    const m=String(iso).match(/T(\d{2}):(\d{2})/);
    if(m) return m[1]+":"+m[2];
    // If no time, try to show nothing (date-only items)
    if(iso&&iso.length>=10) return "";
    return "";
  }
function fmtDay(iso){
    const t=T();
    const key = (String(iso||"").match(/^(\d{4}-\d{2}-\d{2})/)||[])[1] || "";
    let d;
    if(key){
      const [y,mo,da] = key.split("-").map(Number);
      d = new Date(y, mo-1, da); // 本地日历日
    } else {
      d = new Date(iso);
    }
    const labelKey = key || d.toISOString().slice(0,10);
    return {key:labelKey, label:`${d.getMonth()+1}月${d.getDate()}日`, week:t.weekPrefix+t.week[d.getDay()]};
  }
  function dots(n){ n=n||0; return "●".repeat(n)+"○".repeat(Math.max(0,3-n)); }

  function card(it){
    const t=T();
    const imp=(it.rolesImpact&&it.rolesImpact[state.role])||0;
    const tags=tagList(it, state.lang).slice(0,3).map(x=>`<span class="tag">${esc(x)}</span>`).join("");
    return `<article class="card ${state.selectedId===it.id?'selected':''}" data-id="${it.id}">
      <div class="card-time" title="${it.publishedAt||""}">${fmtCardTime(it)}</div>
      <div class="card-body">
        <h3 class="card-title">${esc(tx(it.title))}</h3>
        <p class="card-sum">${esc(tx(it.summaryShort || it.summary))}</p>
        <div class="meta-row">
          <span class="badge badge-score">${it.score}</span>
          <span class="badge ${it.sourceTier}">${t.tier[it.sourceTier]||it.sourceTier}</span>
          <span class="badge verify-${it.verifyStatus}">${it.verifyStatus==='verified'?t.verified:t.pending}</span>
          ${it.clusterCount > 1 ? `<span class="badge cluster-badge" title="${t.cluster||'源同题'}">${t.cluster||'源同题'} ${it.clusterCount}</span>` : ''}
          ${tags.slice(0,1)}
        </div>
      </div>
      <div class="card-side">
        <button type="button" class="star ${state.fav.has(it.id)?'on':''}" data-fav="${it.id}">☆</button>
        <div class="impact">${dots(imp)}</div>
      </div>
    </article>`;
  }
  const _dayCollapsed = {};
  function feed(items, opts){
    const t=T();
    if(!items || !items.length) return `<div class="empty">${t.empty}</div>`;
    const preserve = opts && opts.preserveOrder;
    const sorted = preserve ? items.slice() : items.slice().sort(byPublishedDesc);
    const map=new Map();
    sorted.forEach(it=>{const d=fmtDay(it.publishedAt); if(!map.has(d.key)) map.set(d.key,{meta:d,items:[]}); map.get(d.key).items.push(it);});
    const groups = [...map.values()].sort((a,b)=> (b.meta.key||"").localeCompare(a.meta.key||""));
    groups.forEach(g=> { if(!preserve) g.items.sort(byPublishedDesc); });
    return groups.map(g=>{
      const collapsed = _dayCollapsed[g.meta.key];
      return `<div class="day-head" data-day-toggle="${g.meta.key}" style="cursor:pointer">
        <h3>${g.meta.label}</h3>
        <span>${g.meta.week} · ${g.items.length} ${t.dayUnit} ${collapsed?"▸":"▾"}</span>
      </div>${collapsed?"":g.items.map(card).join("")}`;
    }).join("");
  }
  // Day collapse handler
  document.addEventListener("click", function(e){
    const dd=e.target.closest("[data-daily-date]"); if(dd){ state.q=dd.dataset.dailyDate; document.getElementById("q").value=state.q; render(); return; }
    const dt=e.target.closest("[data-day-toggle]");
    if(dt){ const k=dt.dataset.dayToggle; _dayCollapsed[k]=!_dayCollapsed[k]; render(); }
  });
  function chips(active){
    const t=T();
    // 全部动态：信源 × 文种（与主题雷达六大板块刻意分离）
    if(state.view === "all"){
      const facets = DATA.feedFacets || {};
      const tiers = facets.sourceTiers || [];
      const kinds = facets.contentKinds || [];
      // Primary: source tiers only (most common filter)
      const tierRow = tiers.map(f=>`<button type="button" class="chip ${state.feedTier===f.id?'on':''}" data-feed-tier="${f.id}">${f.icon||""} ${esc(tx(f.title))}</button>`).join("");
      // Secondary: content kinds (collapsed by default)
      const kindRow = kinds.map(f=>`<button type="button" class="chip chip-secondary ${state.feedKind===f.id?'on':''}" data-feed-kind="${f.id}">${f.icon||""} ${esc(tx(f.title))}</button>`).join("");
      return `<div class="facet-stack">
        <div class="chips facet-main">${tierRow}</div>
        <div class="facet-more" id="facetMore" style="display:none"><div class="chips">${kindRow}</div></div>
        <button type="button" class="chip chip-toggle-more" id="facetToggle">文种 ▾</button>
      </div>`;
    }
    // 脉搏等：用 12 主题细码（仍不等于六大板块地图）
    return `<div class="chips-fold" id="themeChipsFold"><div class="chips"><button type="button" class="chip ${active==='all'||!active?'on':''}" data-theme-filter="all">${t.allChip}</button>${Object.entries(t.themes).map(([k,v])=>`<button type="button" class="chip ${active===k?'on':''}" data-theme-filter="${k}">${v}</button>`).join("")}</div><button type="button" class="chip chip-toggle-more" id="themeChipsToggle">主题 ▾</button></div>`;
  }
  function hotSearchChips(){
    const t=T();
    const terms=t.hotSearchTerms||[];
    if(!terms.length) return "";
    return `<div class="hotsearch-row"><span class="hotsearch-label">${t.hotSearch||"大家都在搜"}</span><div class="chips" style="margin-bottom:0">${terms.map((x,i)=>`<button type="button" class="chip chip-hot" data-hot="${x}">${i+1}. ${x}</button>`).join("")}</div></div>`;
  }
  function hot(){
    const t=T();
    // 自动计算：近14天 + score>=85 + sourceTier=official，最多6条
    const now = new Date();
    const weekAgo = new Date(now.getTime() - 14*24*3600*1000).toISOString().slice(0,10);
    const candidates = (DATA.items||[]).filter(i => {
      const d = (i.publishedAt||'').slice(0,10);
      return d >= weekAgo && (i.score||0) >= 85 && (i.sourceTier||'') === 'official';
    });
    candidates.sort((a,b) => (b.score||0) - (a.score||0));
    const items = candidates.slice(0,6);
    if(!items.length) return "";
    return `<section class="hot"><div class="hot-label">${t.hot}<span class="hot-auto"> · 自动</span></div><ol>${items.map((it,i)=>`<li><button type="button" data-open="${it.id}">${esc(tx(it.title))}</button></li>`).join("")}</ol></section>`;
  }

  function render(){
    applyChrome();
    const t=T();
    const meta=t.views[state.view]||t.views.pulse;
    const roleLabel=(t.roles.find(r=>r.id===state.role)||{}).label||"";
    $("#viewTitle").textContent=meta.t;
    $("#viewSub").textContent=`${meta.s} · ${t.roleNow}：${roleLabel}`;
    let html="";
    if(DATA.meta&&DATA.meta.windowNote) html+=`<div class="note-bar"><strong>${t.window}</strong> · ${esc(tx(DATA.meta.windowNote))}</div>`;
    if(state.view==="dashboard"){
      const t=T();
      html+=`<div class="dash-section" style="margin-bottom:32px">
        <div class="dash-hero">
          <h2 style="font-size:24px;font-weight:700;letter-spacing:-0.02em;margin:0 0 4px">情报看板</h2>
          <p style="color:var(--text-muted);font-size:13px;margin:0">市场数据实时仪表板 · 源头可溯 · 每条数字可回追</p>
        </div>
      </div>`;
      const st=DATA.stats||{};
      // Market Pulse
      const mp=st.marketPulse; if(mp&&mp.items){
        html+=`<div class="dash-section"><div class="dash-section-title">${esc(tx(mp.title))}</div>
        <div class="dash-grid dash-grid-3">${mp.items.map(s=>{
          const ti=s.trend==="up"?"↗":s.trend==="down"?"↘":"→";
          const tc=s.trend==="up"?"var(--ok)":s.trend==="down"?"var(--warn)":"var(--text-dim)";
          return '<div class="dash-card"><div class="dash-label">'+esc(tx(s.label))+'</div><div class="dash-value">'+s.value+' <span class="dash-unit">'+esc(tx(s.unit))+'</span></div><div class="dash-change" style="color:'+tc+'">'+ti+' '+s.change+' <span class="dash-clabel">'+esc(tx(s.changeLabel))+'</span></div><p class="dash-note">'+esc(tx(s.note))+'</p><div class="dash-source"><a href="'+s.sourceUrl+'" target="_blank" rel="noopener">'+s.source+'</a> · '+esc(tx(s.asOf))+'</div></div>';
        }).join("")}</div></div>`;
      }
      // Family Office
      const fo=st.familyOffice; if(fo&&fo.items){
        html+=`<div class="dash-section"><div class="dash-section-title">${esc(tx(fo.title))}</div>
        <div class="dash-grid dash-grid-3">${fo.items.map(s=>{
          const ti=s.trend==="up"?"↗":s.trend==="down"?"↘":"→";
          const tc=s.trend==="up"?"var(--ok)":s.trend==="down"?"var(--warn)":"var(--text-dim)";
          return '<div class="dash-card"><div class="dash-label">'+esc(tx(s.label))+'</div><div class="dash-value">'+s.value+' <span class="dash-unit">'+esc(tx(s.unit))+'</span></div><div class="dash-change" style="color:'+tc+'">'+ti+' '+s.change+' <span class="dash-clabel">'+esc(tx(s.changeLabel))+'</span></div><p class="dash-note">'+esc(tx(s.note))+'</p><div class="dash-source"><a href="'+s.sourceUrl+'" target="_blank" rel="noopener">'+s.source+'</a> · '+esc(tx(s.asOf))+'</div></div>';
        }).join("")}</div></div>`;
      }
      // Channel
      const cl=st.channelLandscape; if(cl&&cl.items){
        html+=`<div class="dash-section"><div class="dash-section-title">${esc(tx(cl.title))}</div>
        <div class="dash-grid dash-grid-3">${cl.items.map(s=>{
          const ti=s.trend==="up"?"↗":s.trend==="down"?"↘":"→";
          const tc=s.trend==="up"?"var(--ok)":s.trend==="down"?"var(--warn)":"var(--text-dim)";
          return '<div class="dash-card"><div class="dash-label">'+esc(tx(s.label))+'</div><div class="dash-value">'+s.value+' <span class="dash-unit">'+esc(tx(s.unit))+'</span></div><div class="dash-change" style="color:'+tc+'">'+ti+' '+s.change+' <span class="dash-clabel">'+esc(tx(s.changeLabel))+'</span></div><p class="dash-note">'+esc(tx(s.note))+'</p><div class="dash-source"><a href="'+s.sourceUrl+'" target="_blank" rel="noopener">'+s.source+'</a> · '+esc(tx(s.asOf))+'</div></div>';
        }).join("")}</div></div>`;
      }
      // Regulatory Clock
      const rc=st.regulatoryClock; if(rc&&rc.events){
        html+=`<div class="dash-rule"></div><div class="dash-section"><div class="dash-section-title">${esc(tx(rc.title))}</div><p class="dash-subtitle">${esc(tx(rc.subtitle))}</p>
        <div class="clock-timeline">${rc.events.map((e,i)=>{
          const stars="★★★★★".slice(0,e.impact);
          const it2=e.itemId?byId(e.itemId):null;
          return `<div class="clock-item"><div class="clock-dot ${i===0?'clock-dot-first':i===rc.events.length-1?'clock-dot-last':''}"></div><div class="clock-date">${e.date}</div><div class="clock-body"><div class="clock-cat">${esc(tx(e.category))}</div><div class="clock-title">${esc(tx(e.title))}</div><div class="clock-impact">${stars}</div><p class="clock-desc">${esc(tx(e.desc))}</p>${it2?`<a class="clock-link" data-open="${e.itemId}">查看详情 →</a>`:""}</div></div>`;
        }).join("")}</div></div>`;
      }
      // Insurer Rankings
      const ir=st.insurerRankings; if(ir&&ir.rankings){
        html+=`<div class="dash-rule"></div><div class="dash-section"><div class="dash-section-title">${esc(tx(ir.title))}</div><p class="dash-subtitle">${esc(tx(ir.subtitle))}</p>
        <div class="rank-table-wrap"><table class="rank-table">
          <thead><tr><th>#</th><th>保司</th><th>市占率</th><th>信评</th><th>备注</th></tr></thead>
          <tbody>${ir.rankings.map(r=>{
            const ti2=r.trend==="up"?"↗":r.trend==="down"?"↘":"→";
            const tc2=r.trend==="up"?"var(--ok)":r.trend==="down"?"var(--warn)":"var(--text-dim)";
            return `<tr><td class="rank-num">${r.rank}</td><td class="rank-name"><span class="rank-en">${r.name}</span><span class="rank-zh">${esc(tx(r.nameZH))}</span></td><td class="rank-share">${r.share}</td><td class="rank-rating ${r.rating!=='NR'?'rating-strong':''}">${r.rating}</td><td class="rank-note">${esc(tx(r.note))}</td></tr>`;
          }).join("")}</tbody></table></div>
          <p style="font-size:11px;color:var(--text-dim);margin:8px 0 0">市占率: <a href="${ir.sourceUrl||''}">IA Annual Stats</a> · 信评: <a href="${ir.ratingUrl||''}">S&P Global</a></p></div>`;
      }
      // Company DNA
      const cd=st.companyDNA; if(cd&&cd.rows){
        html+=`<div class="dash-rule"></div><div class="dash-section"><div class="dash-section-title">${esc(tx(cd.title))}</div><p class="dash-subtitle">${esc(tx(cd.subtitle))}</p>
        <div style="display:flex;flex-wrap:wrap;gap:10px;margin-bottom:10px">${["agent-dominant","bank-dominant","broker-dominant","hybrid"].map(a=>{
          const rows=cd.rows.filter(r=>r.archetype===a);
          const label={["agent-dominant"]:"代理派",["bank-dominant"]:"银保派",["broker-dominant"]:"经纪派",["hybrid"]:"混合派"}[a];
          return `<div style="flex:1;min-width:200px;padding:12px;border:1px solid var(--border-soft);border-radius:10px;background:var(--bg-soft)">
            <div style="font-size:11px;color:var(--accent);font-weight:600;margin-bottom:6px">${label} · ${rows.length}家</div>
            ${rows.map(r=>`<div style="font-size:13px;font-weight:600;margin:4px 0">${r.company} <span style="font-size:11px;color:var(--text-dim)">${r.gross2025}亿</span></div><div style="font-size:11px;color:var(--text-muted);margin-bottom:2px">${esc(tx(r.note))}</div>`).join("")}</div>`;
        }).join("")}</div>
        <p style="font-size:11px;color:var(--text-dim);margin:8px 0 0">${esc(tx(cd.calcNote))} · <a href="${cd.sourceUrl}" target="_blank" rel="noopener">${cd.sourceLabel}</a></p></div>`;
      }
      // Talent Flow
      const tf=st.talentFlow; if(tf&&tf.liveData){
        html+=`<div class="dash-rule"></div><div class="dash-section"><div class="dash-section-title">${esc(tx(tf.title))}</div><p class="dash-subtitle">${esc(tx(tf.subtitle))}</p>
        <div class="dash-grid dash-grid-3">
          <div class="dash-card"><div class="dash-label">持牌总人数(个人)</div><div class="dash-value" style="font-size:36px">${(tf.liveData.totalIndividuals/1000).toFixed(0)}<span class="dash-unit">k</span></div><p class="dash-note">截至 ${tf.liveData.date} · IA 实时</p></div>
          <div class="dash-card"><div class="dash-label">持牌经纪(Tech Rep)</div><div class="dash-value" style="font-size:36px">${(tf.liveData.techRepBroker/1000).toFixed(1)}<span class="dash-unit">k</span></div><div class="dash-change" style="color:var(--ok)">↗ 最快增速 · 3年 +37.1%</div></div>
          <div class="dash-card"><div class="dash-label">保险代理(Licensed Agent)</div><div class="dash-value" style="font-size:36px">${(tf.liveData.agents/1000).toFixed(0)}<span class="dash-unit">k</span></div><div class="dash-change" style="color:var(--text-dim)">→ 稳中有降</div></div>
        </div>
        <p style="font-size:11px;color:var(--text-dim);margin:8px 0 0">${esc(tx(tf.calcNote))} · <a href="${tf.sourceUrl}" target="_blank" rel="noopener">${tf.sourceLabel}</a></p></div>`;
      }
      // Intelligence Density
      const iden=st.intelligence; if(iden){ const _total=(DATA.items||[]).length||iden.totalItems||0;
        html+=`<div class="dash-rule"></div><div class="dash-section"><div class="dash-section-title">${esc(tx(iden.title))}</div><p class="dash-subtitle">${esc(tx(iden.subtitle))}</p>
        <div class="dash-grid dash-grid-2">
          <div class="dash-card"><div class="dash-label">累计条目</div><div class="dash-value" style="font-size:40px">${_total} <span class="dash-unit">条</span></div><p class="dash-note">${esc(tx(iden.dateRange))}</p></div>
          <div class="dash-card"><div class="dash-label">信源分布</div><div class="tier-bars">${(iden.sourceTiers||[]).map(t=>{
            const pct=Math.round(t.count/_total*100);
            return `<div class="tier-bar-row"><span class="tier-label">${t.label||t.tier}</span><div class="tier-bar-bg"><div class="tier-bar-fill" style="width:${pct}%"></div></div><span class="tier-count">${t.count}</span></div>`;
          }).join("")}</div></div>
        </div>
        <div class="dash-card" style="margin-top:10px"><div class="dash-label">主题热度 Top 10</div>
        <div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:8px">${(iden.topThemes||[]).map(t=>'<span style="font-size:13px;color:var(--accent);background:var(--accent-dim);padding:3px 8px;border-radius:6px">'+(t.label||t.theme)+' '+t.count+'</span>').join("")}</div></div></div>`;
      }
      // Footer
      const ds=st.dataSummary; if(ds){
        html+=`<div class="dash-rule"></div><div class="dash-section"><div class="dash-section-title">${esc(tx(ds.title))}</div>
        <div class="dash-summary">${(ds.notes||[]).map(n=>`<li>${esc(tx(n))}</li>`).join("")}</div></div>`;
      }
    }
    else if(state.view==="pulse"){
      // evergreen
      const eg=(DATA.evergreen||[]).map(byId).filter(Boolean).filter(matches);
      if(eg.length){
        html+=`<div class="evergreen-banner-wrapper"><h3>${t.evergreen}</h3><p class="evergreen-hint">← 滑动查看 · 驻点：持续有效的监管规则与长期适用的披露要求 →</p><div class="evergreen-scroll"><button class="evergreen-scroll-btn" onclick="this.nextElementSibling.scrollBy({left:-300,behavior:'smooth'})">‹</button><div class="evergreen-banner">${eg.map(it=>`<div class="banner-card" data-open="${it.id}"><div class="banner-tag">常驻</div><h4>${esc(tx(it.title))}</h4><p>${esc(tx(it.summary))}</p></div>`).join("")}</div><button class="evergreen-scroll-btn" onclick="this.previousElementSibling.scrollBy({left:300,behavior:'smooth'})">›</button></div></div>`;
      }
      // Dynamic scoring: score × 0.7 + roleMatch × 0.3
      const roleWeights = {front:0,midback:0,lead:0,cross:0};
      if(state.role==='front'){roleWeights.front=3;roleWeights.midback=1;}
      else if(state.role==='midback'){roleWeights.midback=3;roleWeights.front=1;roleWeights.lead=1;}
      else if(state.role==='lead'){roleWeights.lead=3;roleWeights.front=1;roleWeights.cross=1;}
      else if(state.role==='cross'){roleWeights.cross=3;roleWeights.lead=1;roleWeights.front=1;}
      const pulseList = list({pulseSort:true, roleWeights:roleWeights});
      html+=hot()+chips(state.themeFilter)+feed(pulseList, {preserveOrder:true});
    }
    else if(state.view==="all"){
      const cat = DATA.meta && DATA.meta.sourcesCatalog;
      if(cat){
        html += `<div class="panel sources-panel"><h3>${esc(t.sourcesCatalogH||"信源目录")}</h3>
          <p class="sources-principle">${esc(tx(cat.principle||{}))}</p>
          <div class="sources-layers">${(cat.layers||[]).map(layer=>`<div class="sources-layer">
            <div class="sources-layer-title">${esc(tx(layer.title))}</div>
            <div class="sources-layer-note">${esc(tx(layer.countNote||{}))}${(layer.items&&layer.items.length)? " · " + layer.items.join(" · "):""}</div>
          </div>`).join("")}</div>
        </div>`;
      }
      html+=chips(state.themeFilter)+feed(list());
    }
    else if(state.view==="fav") {
      const ft = favTags();
      if(ft.length){
        html+=`<div class="tag-chips" style="margin:0 0 12px">
          <span class="tag-chip ${!state.favTag?'on':''}" data-favtag="">全部</span>
          ${ft.map(t=>`<span class="tag-chip ${state.favTag===t?'on':''}" data-favtag="${esc(t)}">${t}</span>`).join("")}
        </div>`;
      }
      html+=feed(list({favOnly:true}));
    }
    else if(state.view==="daily"){
      // 自动聚合：近14天按4个角色切片（与主题雷达分工：雷达看空间结构，日报看时间快照）
      const cutoff = new Date(Date.now() - 14*24*3600*1000).toISOString().slice(0,10);
      const recent = DATA.items.filter(i => (i.publishedAt||"").slice(0,10) >= cutoff);
      const roles = (DATA.meta && DATA.meta.roles) || [];
      const todayStr = new Date().toISOString().slice(0,10);
      html+=`<div class="panel"><h3>${meta.t} · ${todayStr}</h3><p>${t.dailyLead}</p></div>`;
      roles.forEach(role=>{
        // 方案C：≥3（深度影响）优先，不足8条用 ≥1（相关）补齐——避免空日报
        const pool = recent.filter(matches);
        const strong = pool.filter(i => ((i.rolesImpact||{})[role.id]||0) >= 3)
          .sort((a,b)=> (b.score||0)-(a.score||0));
        const related = pool.filter(i => ((i.rolesImpact||{})[role.id]||0) === 2 || ((i.rolesImpact||{})[role.id]||0) === 1)
          .sort((a,b)=> (b.score||0)-(a.score||0));
        const items = [...strong, ...related].slice(0, 8);
        const badge = strong.length ? `<span class="badge">${strong.length} 深度</span>` : "";
        html+=`<div class="day-head"><h3>${esc(tx(role.label))}</h3><span>${items.length} ${t.dayUnit}</span>${badge}</div>${items.map(card).join("")||`<div class="empty">${t.empty}</div>`}`;
      });
    } else if(state.view==="deeps"){
      const cards = DATA.deepCards || [];
      if(state.themeBoard){
        const dc = cards.find(x=>x.id===state.themeBoard);
        if(!dc){ html+=`<div class="empty">未找到深度卡</div>`; }
        else {
          const items = (dc.timeline||[]).map(t=>byId(t.itemId)).filter(Boolean);
          html+=`<div class="deep-hero">
            <button type="button" class="pill" data-board-back="1">← 返回</button>
            <h3>${esc(tx(dc.title))}</h3>
            <p class="deep-subtitle">${esc(tx(dc.subtitle))}</p>
            <p class="deep-summary">${esc(tx(dc.summary))}</p>
            <div class="deep-impact">
              ${['front','midback','lead','cross'].map(r=>{
                const label=((t.roles||[]).find(x=>x.id===r)||{}).label||r;
                const txt=tx((dc.impact||{})[r]);
                if(!txt) return '';
                return `<div class="deep-role"><strong>${label}</strong><p>${esc(txt)}</p></div>`;
              }).join('')}
            </div>
            <h4>FAQ</h4>
            <div class="deep-faq">${(dc.faq||[]).map(f=>`<details><summary>${esc(tx(f.q))}</summary><p>${esc(tx(f.a))}</p></details>`).join('')}</div>
          </div>`;
          html+=`<div class="day-head"><h3>关联条目</h3><span>${items.length} 条</span></div>`;
          html+=items.length ? feed(items) : `<div class="empty">暂无</div>`;
        }
      } else {
        html+=`<div class="taxon-head">
          <h3 style="font-size:20px">监管深度</h3>
          <p>重大监管事件的完整画像：时间线、影响矩阵、FAQ、关联条目</p>
        </div>`;
        html+=`<div class="deep-grid">`+cards.map(dc=>{
          const count=(dc.timeline||[]).filter(t=>byId(t.itemId)).length;
          return `<button type="button" class="deep-card" data-board="${dc.id}">
            <div class="deep-card-title">${esc(tx(dc.title))}</div>
            <p class="deep-card-sub">${esc(tx(dc.subtitle))}</p>
            <p class="deep-card-summary">${esc(tx(dc.summary)).slice(0,120)}</p>
            <div class="deep-card-meta"><span>${count} 条关联</span><span>${(dc.faq||[]).length} 条 FAQ</span></div>
          </button>`;
        }).join("")+`</div>`;
      }
    }
    else if(state.view==="themes"){
      const boards = DATA.boards || [];
      const byBoard = (bid) => DATA.items.filter(it => (it.boards||[]).includes(bid)).filter(matches)
        .sort((a,b)=> (b.publishedAt||"").localeCompare(a.publishedAt||"") || (b.score||0)-(a.score||0));

      if(state.themeBoard){
        const b = boards.find(x=>x.id===state.themeBoard) || {id:state.themeBoard,title:{sc:state.themeBoard},desc:{sc:""},subs:[]};
        const its = byBoard(state.themeBoard);
        html += `<div class="taxon-hero">
          <button type="button" class="pill" data-board-back="1">← ${t.boardBack||"返回"}</button>
          <h3>${esc(tx(b.title))}</h3>
          <p>${esc(tx(b.desc)||"")}</p>
          <div class="taxon-subs">${(b.subs||[]).map(s=>`<span class="chip chip-sub" data-theme-filter="${s}">${esc(t.themes[s]||s)}</span>`).join(" ")}</div>
          <p style="font-size:12px;color:var(--text-dim);margin-top:8px">${its.length} ${t.boardCount||"条导读"}</p>
        </div>`;
        html += its.length ? feed(its) : `<div class="empty">${t.empty}</div>`;
      } else {
        html += `<div class="taxon-head">
          <h3>${meta.t}</h3>
          <p>${meta.s}</p>
          <p class="taxon-hint">${t.boardHint||""}</p>
        </div>`;
        html += `<div class="taxon-grid">` + boards.map(b=>{
          const n = byBoard(b.id).length;
          const th = (k) => DATA.items.filter(it => (it.themes||[]).includes(k)).length;
          const subs = (b.subs||[]).map(k => ({key:k, n:th(k)})).filter(x=>x.n>0).sort((a,b)=>b.n-a.n);
          const maxN = subs.length ? subs[0].n : 1;
          const themeLabel = (k) => t.themes[k] || k;
          return `<button type="button" class="taxon-card" data-board="${b.id}">
            <div class="taxon-name">${esc(tx(b.title))}</div>
            <div class="taxon-n">${n} 条</div>
            <p class="taxon-desc">${esc(tx(b.desc)||"")}</p>
            <div class="taxon-heat">${subs.slice(0,8).map(s=>`<span class="heat-row" data-theme-filter="${s.key}"><span class="heat-label">${esc(themeLabel(s.key))}</span><span class="heat-track"><span class="heat-fill" style="width:${Math.round(s.n/maxN*100)}%"></span></span><span class="heat-n">${s.n}</span></span>`).join("")}</div>
          </button>`;
        }).join("") + `</div>`;
      }
    } else if(state.view==="calendar"){
      html+=`<div class="panel"><h3>${t.calH}</h3>${(DATA.calendar||[]).map(c=>{
        const linked=c.itemId&&byId(c.itemId);
        return linked
          ? `<div class="cal-item cal-link" data-open="${c.itemId}" title="点击查看关联资讯"><div class="cal-date">${esc(c.date)}</div><div>${esc(tx(c.title))} <span class="tag">${esc(t.themes[c.theme]||"")}</span> <span class="cal-jump">↗</span></div></div>`
          : `<div class="cal-item"><div class="cal-date">${esc(c.date)}</div><div>${esc(tx(c.title))} <span class="tag">${esc(t.themes[c.theme]||"")}</span></div></div>`;
      }).join("")}</div>`;
    } 
    else if(state.view==="download"){
      const periods=["daily","weekly","monthly","yearly"];
      html+=`<div class="panel"><h3>${meta.t}</h3><p>${t.downloadHint||t.archiveHint||""}</p>
        <div class="chips">${periods.map(p=>`<button type="button" class="chip ${state.archivePeriod===p?'on':''}" data-arch-period="${p}" data-reset-page="1">${t.archiveTabs[p]}</button>`).join("")}</div>
      </div>`;
      const digests=(DATA.digests&&DATA.digests[state.archivePeriod])||[];
      if(state.archiveKey){
        const dig=digests.find(x=>x.key===state.archiveKey);
        if(!dig){ html+=`<div class="empty">${t.noDigest}</div>`; }
        else {
          const gate=canExportDigest(state.archivePeriod);
          const price=(mon().prices&&mon().prices[state.archivePeriod])||0;
          const exportLabel = gate.readonlyNote? t.digestExport : ((!mon().enabled || gate.free) ? t.digestExport : (gate.ok? `${t.digestExport}` : `${t.digestExport} · ${t.proLock}`));
          html+=`<div class="panel"><button type="button" class="pill" data-arch-back="1">← ${t.backDownload}</button>
            <h3 style="margin-top:12px">${esc(tx(dig.label))}</h3>
            <p>${t.itemsInPeriod}：${dig.itemCount} · ${esc(tx(dig.note||{}))}</p>
            ${gate.reason==="readonly"?`<p class="lock-note" style="margin:8px 0">📖 ${t.monthlyYearlyReadOnly||"月报与年报仅可在线查阅，不提供下载。"}</p>`:
            `<div class="action-bar">
              <button type="button" class="btn primary" data-export-digest="1" title="导出当前筛选结果为Markdown">${t.digestExport} · MD</button>
              <button type="button" class="btn" data-email-digest="1" title="打开默认邮件客户端">📧 ${t.emailTo}</button>
            </div>
            <div class="email-box" style="display:none;margin:8px 0">
              <input type="email" class="email-input" placeholder="${t.emailHint}" />
              <button type="button" class="btn" data-email-send="1">${t.emailSent}</button>
            </div>`}
            </div>`;
          const ids=dig.itemIds||[];
          const its=ids.map(byId).filter(Boolean).filter(matches);
          html+=feed(its);
        }
      } else {
        const q=(state.archiveQ||"").trim().toLowerCase();
        let list=digests;
        if(q) list=list.filter(x=>tx(x.label).toLowerCase().includes(q)||tx(x.leadTitle||{}).toLowerCase().includes(q));
        html+=`<div class="search-box" style="margin-bottom:12px;max-width:420px"><span style="color:var(--text-dim)">⌕</span>
          <input id="archQ" type="search" placeholder="${t.searchDownload||t.searchArchive||""}" value="${esc(state.archiveQ||"")}" /></div>`;
        const total=list.length;
        const pages=Math.ceil(total/25);
        const start=(state.archivePage-1)*25;
        const paged=list.slice(start,start+25);
        html+=`<div style="font-size:12px;color:var(--text-dim);margin-bottom:8px">共 ${total} 期，第 ${state.archivePage}/${pages} 页</div>`;
        if(!paged.length) html+=`<div class="empty">${t.noDigest}</div>`;
        else {
          const maxCount = Math.max(...paged.map(d=>d.itemCount||1));
          html+=`<div class="arch-list">`+paged.map(dig=>{
            const lead=tx(dig.leadTitle||{})||"";
            const barW = Math.min(100, (dig.itemCount/maxCount)*100);
            return `<button type="button" class="arch-row" data-arch-key="${esc(dig.key)}">
              <div class="arch-date">${esc(tx(dig.label))}</div>
              <div class="arch-lead">${esc(lead)}</div>
              <div class="arch-count">
                <div class="arch-bar-wrap"><div class="arch-bar" style="width:${barW}%"></div></div>
                ${dig.itemCount}
              </div>
            </button>`;
          }).join("")+`</div>`;
        if(pages>1){
          html+=`<div class="paginator">`;
          for(let p=1;p<=pages;p++){
            html+=`<button type="button" class="chip ${p===state.archivePage?'on':''}" data-arch-page="${p}">${p}</button>`;
          }
          html+=`</div>`;
        }
        }
      }
    }

    else if(state.view==="agent"){ window.location.href="agent.html"; return; }
    else if(state.view==="changelog"){
      const logs = DATA.meta.changelog || [];
      html+=`<div class="panel changelog-hero"><h3>${meta.t}</h3><p>${meta.s}</p></div>`;
      logs.forEach(log=>{
        const title = log.title ? tx(log.title) : "";
        html+=`<div class="day-head" style="border-bottom:1px solid var(--border-soft);padding-bottom:4px"><h3>${log.date}</h3><span>${log.items.length} 项</span></div>`;
        if(title) html+=`<p style="font-size:13px;color:var(--accent);margin:0 0 6px;font-weight:600">${title}</p>`;
        html+=`<div class="panel" style="margin-bottom:16px"><ul style="margin:0;padding-left:18px">${log.items.map(i=>`<li style="margin:4px 0;font-size:13px;color:var(--text-muted)">${i}</li>`).join("")}</ul></div>`;
      });
    }
    else if(state.view==="about"){
      html+=`<div class="panel about-hero">
        <h3>${t.brandName}</h3>
        <p class="sub">${t.brandSub}</p>
        <p>${esc(t.about1)}</p>
        <p>${esc(t.about2)}</p>
      </div>
      <div class="panel about-qr">
        <div class="qr-area">
          <img src="assets/qr-wechat.jpg" alt="维港猫圈儿" width="120" height="120" />
          <p><strong>${t.wechat}</strong></p>
          <p class="qr-tip">${t.qrTip}</p>
        </div>
      </div>
      <div class="panel about-notice">
        <h4>使用须知</h4>
        <ul>
          <li>本站为资讯聚合与导读索引。摘要与动作卡由人工/AI二次整理，数字与规则以原文链接为准。</li>
          <li>内容供香港持牌保险中介及专业人士参考，不构成销售建议、投资建议或法律意见。</li>
          <li>常驻信息的驻点标准：持续有效的监管规则、长期适用的披露要求、行业基础框架性文件。</li>
          <li>英文原文已标注语种标记；翻译内容仅供参考，以原文为准。</li>
          <li>热点规则: 近14天 sourceTier=official + score≥85 → 自动上榜前6条。精选排序: score×0.7 + 角色匹配×0.3 → 动态排序。常驻: 官方监管/合规类 evergreen=true 手动确认为长期适用。评分原则（60-99）：信源权重(official>insurer>pro>media) × 60% + 内容时效/角色覆盖面 × 25% + 人工校准 × 15%。90+为高确定性一手监管或官方披露；70-89为专业解读；60-69为媒体线索待核。</li>
        </ul>
      </div>
      <div class="panel"><h3>${t.disclaimer}</h3><p>${esc(t.disc)}</p></div>`;
    }
    $("#content").innerHTML=html;
  }


  function savePoints(){ localStorage.setItem("hkii_points", String(state.points)); }
  function mon(){ return (DATA.meta && DATA.meta.monetization) || {enabled:false,prices:{}}; }
  function canExportDigest(period){
    const m=mon();
    // 月报/年报仅可阅读，不可下载
    if(period==="monthly"||period==="yearly") return {ok:true, free:true, readonlyNote:"月报/年报仅可在线查阅，不提供打包下载。"};
    if(!m.enabled) return {ok:true, free:true};
    const price=(m.prices&&m.prices[period])||0;
    if(price<=0) return {ok:true, free:true};
    if(state.pro) return {ok:true, free:false, pro:true};
    if(state.points>=price) return {ok:true, free:false, cost:price};
    return {ok:false, cost:price};
  }
  function toast(msg){
    let el=document.getElementById("hkiiToast");
    if(!el){ el=document.createElement("div"); el.id="hkiiToast"; el.className="toast"; document.body.appendChild(el); }
    el.textContent=msg; el.classList.add("show");
    clearTimeout(el._t); el._t=setTimeout(()=>el.classList.remove("show"), 2200);
  }
  function downloadText(filename, text){
    const blob=new Blob([text],{type:"text/markdown;charset=utf-8"});
    const a=document.createElement("a");
    a.href=URL.createObjectURL(blob); a.download=filename; a.click();
    setTimeout(()=>URL.revokeObjectURL(a.href), 2000);
  }
  function itemToMarkdown(it){
    const t=T();
    const roleLabel=(t.roles.find(r=>r.id===state.role)||{}).label;
    const act=tx(it.actions&&it.actions[state.role])||"—";
    const boards=(it.boards||[]).map(id=>{const b=(DATA.boards||[]).find(x=>x.id===id); return b?tx(b.title):id;}).join(" / ");
    return `# ${tx(it.title)}

> ${t.guideLabel} · ${t.fidelityText}

- **信源等级**: ${t.tier[it.sourceTier]||it.sourceTier}
- **来源**: ${tx(it.source)}
- **发布时间**: ${it.publishedAt||""}
- **生效日**: ${it.effectiveAt||"—"}
- **复核**: ${it.verifyStatus==="verified"?t.verified:t.pending}
- **板块**: ${boards||"—"}
- **来源指纹**: ${it.sourceKey||"—"}

## ${t.summary}
${tx(it.summary)}

## ${t.why}
${tx(it.why)}

## ${t.actionNow}（${roleLabel}）
${act}

## ${t.originalAuthority}
${it.originalUrl||"（无链接）"}

---
${t.brandName} · ${t.disc}
`;
  }
  function digestToMarkdown(dig){
    const t=T();
    const lines=[`# ${tx(dig.label)}`,"",`> ${tx(dig.note||{})}`,"",`条目数: ${dig.itemCount}`,""];
    (dig.itemIds||[]).forEach((id,i)=>{
      const it=byId(id); if(!it) return;
      lines.push(`## ${i+1}. ${tx(it.title)}`);
      lines.push("");
      lines.push(tx(it.summary));
      lines.push("");
      lines.push(`- 原文: ${it.originalUrl||"—"}`);
      lines.push(`- 来源: ${tx(it.source)}`);
      lines.push("");
    });
    lines.push("---");
    lines.push(`${t.brandName} · ${t.disc}`);
    return lines.join("\n");
  }
  function posterSummary(it){
    // 为什么重要：全量输出，canvas 自然换行（最多6行）
    const w=tx(it.why);
    return w ? w.replace(/\s+/g," ").trim() : (tx(it.summary)||"").replace(/\s+/g," ").trim();
  }
  function posterBullets(it){
    // 摘要全量（canvas 自然换行，最多3行）+ 当前角色行动建议
    const sum=(tx(it.summary)||"").replace(/\s+/g," ").trim();
    const act=(tx(it.actions&&it.actions[state.role])||"").replace(/\s+/g," ").trim();
    return [sum, act].filter(Boolean);
  }
  function isMomentsFriendly(it){
    const blob=(tx(it.title)+tx(it.summary));
    if(/巡查常见|汇報安排|匯報安排|KPIM|申报表/.test(blob)) return false;
    return true;
  }
  function drawPoster(it, theme){
    theme = theme || "dark";
    const canvas=$("#posterCanvas"); if(!canvas) return;
    const ctx=canvas.getContext("2d");
    const W=1080,H=1350; canvas.width=W; canvas.height=H;
    const t=T();
    // ===== 版式主题：dark=深蓝墨(默认) / light=浅色VI =====
    const C = theme==="light" ? {
      bg0:"#faf7f0", bg1:"#f4efe3", bg2:"#efe8d8",
      gold:"#B6985A", goldSoft:"rgba(182,152,90,0.16)",
      ink:"#103365", inkDim:"rgba(16,51,101,0.66)", inkFaint:"rgba(16,51,101,0.4)",
      line:"rgba(182,152,90,0.35)",
      hlFill:"rgba(182,152,90,0.12)",
    } : {
      bg0:"#0d1420", bg1:"#0a0e14", bg2:"#080b10",
      gold:"#e8a54b", goldSoft:"rgba(232,165,75,0.14)",
      ink:"#eef2f8", inkDim:"rgba(232,237,245,0.82)", inkFaint:"rgba(232,237,245,0.42)",
      line:"rgba(232,165,75,0.25)",
      hlFill:"rgba(232,165,75,0.12)",
    };
    // ===== 背景 =====
    const g=ctx.createLinearGradient(0,0,0,H);
    g.addColorStop(0,C.bg0); g.addColorStop(0.6,C.bg1); g.addColorStop(1,C.bg2);
    ctx.fillStyle=g; ctx.fillRect(0,0,W,H);
    // 顶部金色信号线
    ctx.fillStyle=C.gold; ctx.fillRect(0,0,W,8);
    // 细金框（内嵌，克制）
    ctx.strokeStyle=C.line; ctx.lineWidth=2;
    ctx.strokeRect(40,40,W-80,H-80);

    // ===== 品牌行 =====
    ctx.fillStyle=C.gold; ctx.font="700 30px sans-serif";
    ctx.fillText("猫圈儿港险情报站", 80, 116);
    ctx.fillStyle=C.inkFaint; ctx.font="400 24px sans-serif";
    const dateStr=(it.publishedAt||"").slice(0,10);
    ctx.fillText(dateStr, 80, 152);

    // ===== 板块标签（纯文字，无图标） =====
    const bid=(it.boards&&it.boards[0])||"reg";
    const board=(DATA.boards||[]).find(b=>b.id===bid);
    const boardName=board?tx(board.title):"港险资讯";
    const bw=ctx.measureText(boardName).width;
    ctx.fillStyle=C.goldSoft;
    roundRect(ctx,80,188,bw+56,52,10); ctx.fill();
    ctx.fillStyle=C.gold; ctx.font="600 26px sans-serif";
    ctx.fillText(boardName, 108, 222);

    // ===== 标题（大字，衬线感，最多3行） =====
    const titleText=tx(it.title);
    const tFont="700 46px 'Songti SC','Noto Serif SC',serif";
    const tLines=Math.min(countLines(ctx,titleText,W-160,tFont),3);
    const titleY0=296, titleLH=60, titleH=tLines*titleLH;
    ctx.fillStyle=C.ink;
    wrapText(ctx, titleText, 80, titleY0, W-160, titleLH, tFont, 3);

    // ===== 摘要（全量显示，高亮条高度自适应） =====
    const sum1=posterSummary(it);
    const sFont="500 30px sans-serif";
    const sLines=Math.min(countLines(ctx,sum1,W-220,sFont),6);
    const sumY=titleY0+titleH+34;
    const sumH=sLines*40+40;
    ctx.fillStyle=C.hlFill;
    roundRect(ctx,80,sumY,W-160,sumH,14); ctx.fill();
    ctx.fillStyle=C.gold; ctx.fillRect(80,sumY,6,sumH);
    ctx.fillStyle=C.ink;
    wrapText(ctx, sum1, 110, sumY+34, W-220, 40, sFont, 6);

    // ===== 分隔线 =====
    const lineY=sumY+sumH+36;
    ctx.strokeStyle=C.line; ctx.beginPath();
    ctx.moveTo(80,lineY); ctx.lineTo(W-80,lineY); ctx.stroke();

    // ===== 要点（最多2条，空间自适应） =====
    const bullets=posterBullets(it);
    let y=lineY+52;
    bullets.forEach((b,i)=>{
      if(y>H-190) return;
      ctx.fillStyle=C.gold; ctx.font="700 26px sans-serif";
      ctx.fillText("◆", 80, y);
      ctx.fillStyle=C.inkDim;
      y = wrapText(ctx, b, 124, y-6, W-204, 42, "400 28px sans-serif", 3) + 40;
    });

    // ===== 评分角标 =====
    ctx.fillStyle=C.gold; ctx.font="700 60px sans-serif";
    ctx.textAlign="right";
    ctx.fillText(String(it.score||""), W-90, 130);
    ctx.font="400 20px sans-serif"; ctx.fillStyle=C.inkFaint;
    ctx.fillText("评分", W-90, 160);
    ctx.textAlign="left";

    // ===== 底部 =====
    ctx.fillStyle=C.inkFaint; ctx.font="400 22px sans-serif";
    const url=(it.originalUrl||"").replace(/^https?:\/\//,"").slice(0,46);
    ctx.fillText(url?("原文："+url):"请在情报站打开原文核对", 80, H-140);
    ctx.fillStyle=C.gold; ctx.font="600 24px sans-serif";
    ctx.fillText("专业分享 · 非销售邀约 · 以监管/保司原文为准", 80, H-96);
    ctx.fillStyle=C.inkFaint; ctx.font="400 22px sans-serif";
    ctx.fillText("维港猫圈儿 · hkmaoquanqingbao.com", 80, H-56);
  }
  // 计算文字在给定宽度下会占几行（供动态布局用）
  function countLines(ctx, text, maxW, font){
    ctx.font=font;
    const chars=[...text]; let line=""; let lines=1;
    for(let i=0;i<chars.length;i++){
      const test=line+chars[i];
      if(ctx.measureText(test).width>maxW && line){ lines++; line=chars[i]; }
      else line=test;
    }
    return lines;
  }
  function roundRect(ctx,x,y,w,h,r){
    ctx.beginPath(); ctx.moveTo(x+r,y); ctx.arcTo(x+w,y,x+w,y+h,r); ctx.arcTo(x+w,y+h,x,y+h,r);
    ctx.arcTo(x,y+h,x,y,r); ctx.arcTo(x,y,x+w,y,r); ctx.closePath();
  }
  function wrapText(ctx, text, x, y, maxW, lineH, font, maxLines){
    ctx.font=font;
    const chars=[...text]; let line=""; let lines=0; let cy=y;
    for(let i=0;i<chars.length;i++){
      const test=line+chars[i];
      if(ctx.measureText(test).width>maxW && line){
        ctx.fillText(line,x,cy); cy+=lineH; line=chars[i]; lines++;
        if(lines>=maxLines-1){
          let rest=chars.slice(i).join("");
          while(ctx.measureText(rest+"…").width>maxW && rest.length>1) rest=rest.slice(0,-1);
          ctx.fillText(rest+"…",x,cy); return cy+lineH;
        }
      } else line=test;
    }
    if(line){ ctx.fillText(line,x,cy); cy+=lineH; }
    return cy;
  }
  function openPoster(id){
    const it=byId(id); if(!it) return;
    const t=T();
    $("#posterModalTitle").textContent=t.posterTitle;
    const tip=t.posterTip + " " + (isMomentsFriendly(it)?`（${t.momentsOk}）`:`（${t.momentsNo}）`);
    $("#posterTip").textContent=tip;
    $("#posterModal").hidden=false;
    drawPoster(it, state.posterTheme);
    // 下载指定版式
    function dlPoster(theme, suffix){
      drawPoster(it, theme);
      try{
        const a=document.createElement("a");
        a.href=$("#posterCanvas").toDataURL("image/png");
        a.download=`猫圈儿-海报-${suffix}-${it.id}.png`;
        document.body.appendChild(a); a.click(); a.remove();
        toast(t.posterDl+" ✓");
        trackEvent("poster", theme);
      }catch(err){ toast("下载失败，请长按图片保存"); }
      drawPoster(it, state.posterTheme); // 恢复当前版式
    }
    const dlDark=$("#posterDlDark"), dlLight=$("#posterDlLight");
    if(dlDark) dlDark.onclick=()=>dlPoster("dark","深色");
    if(dlLight) dlLight.onclick=()=>dlPoster("light","浅色");
    $("#posterCopyMd").onclick=async()=>{
      // 朋友圈文案：标题 + 一句话总结 + 来源提示
      const sum1=posterSummary(it);
      const text=`【港险快讯】${tx(it.title)}\n\n${sum1}\n\n来源：${tx(it.source)}\nvia 猫圈儿港险情报站（hkmaoquanqingbao.com）\n——专业分享，非销售邀约，以监管/保司原文为准`;
      try{ await navigator.clipboard.writeText(text); toast(t.copyDone);}catch(e){ prompt("Copy", text); }
    };
  }
  function closePoster(){ $("#posterModal").hidden=true; }


  function openDrawer(id){
    const it=byId(id); if(!it) return;
    trackEvent("open", id);
    const t=T(); state.selectedId=id;
    $("#dTitle").textContent=tx(it.title);
    const roleLabel=(t.roles.find(r=>r.id===state.role)||{}).label;
    const act=tx(it.actions&&it.actions[state.role])||"—";
    const all=t.roles.map(r=>{const a=it.actions&&it.actions[r.id]; return a?`<div class="action-box"><strong>${r.label}</strong>${esc(tx(a))}</div>`:"";}).join("");
    $("#dBody").innerHTML=`
      <div class="meta-row" style="margin-bottom:10px">
        <span class="badge ${it.sourceTier}">${t.tier[it.sourceTier]}</span>
        <span class="badge">${t.score} ${it.score}</span>
        <span class="badge verify-${it.verifyStatus}">${it.verifyStatus==='verified'?t.verified:t.pending}</span>
      </div>
      <p style="color:var(--text-dim);font-size:12px">${esc(tx(it.source))} · ${esc(it.publishedAt||"")}</p>
      <div class="fidelity-banner">${t.guideLabel} · ${t.fidelityText}</div>
      <h4>${t.summary}</h4><p>${esc(tx(it.summary))}</p>
      ${it.contentRole?`<p style="font-size:12px;color:var(--text-dim)">${esc(tx(it.contentRole))}</p>`:""}
      <h4>${t.why}</h4><p>${esc(tx(it.why))}</p>
      <h4>${t.actionNow} · ${esc(roleLabel)}</h4>
      <div class="action-box"><strong>${t.roleNow}</strong>${esc(act)}</div>
      <h4>${t.actionAll}</h4>${all}
      ${it.effectiveAt?`<h4>${t.effective}</h4><p>${esc(it.effectiveAt)}</p>`:""}
      ${it.note?`<h4>${t.note}</h4><p>${esc(tx(it.note))}</p>`:""}
      <h4>${t.themesH}</h4><p>${esc((it.themes||[]).map(x=>t.themes[x]||x).join(" · "))}</p>
      <h4>${t.originalAuthority}</h4>
      <div class="links">${it.originalUrl?`<a class="btn-original" href="${it.originalUrl}" target="_blank" rel="noopener">${t.original} ↗</a>`:`<span class="badge">无原文链接</span>`}
      ""
      ${it.sourceKey?`<span class="badge">${t.sourceKey} ${it.sourceKey}</span>`:""}</div>
      <div class="action-bar">
        <button type="button" class="btn primary" data-export-md="${it.id}">${t.exportMd}</button>
        <button type="button" class="btn" data-poster="${it.id}">${t.posterBtn}</button>
      </div>
      <p class="lock-note">${isMomentsFriendly(it)?t.momentsOk:t.momentsNo}</p>`;
    $("#drawer").classList.add("open"); $("#backdrop").classList.add("open"); render();
  }
  function closeDrawer(){ state.selectedId=null; $("#drawer").classList.remove("open"); $("#backdrop").classList.remove("open"); render(); }

  $("#nav").addEventListener("click", e=>{ const b=e.target.closest("[data-view]"); if(!b) return; state.view=b.dataset.view; state.themeFilter="all"; state.feedTier="all"; state.feedKind="all"; if(b.dataset.view!=="themes") state.themeBoard=null; trackEvent("view", state.view); $("#sidebar").classList.remove("open"); render(); });
  $("#rolePills").addEventListener("click", e=>{ const b=e.target.closest("[data-role]"); if(!b) return; state.role=b.dataset.role; localStorage.setItem("hkii_role", state.role); trackEvent("role", state.role); render(); });
  let _isComposing = false;
  $("#q").addEventListener("compositionstart", ()=>{ _isComposing = true; });
  $("#q").addEventListener("compositionend", (e)=>{ _isComposing = false; recordSearch(e.target.value); });
  $("#q").addEventListener("input", e=>{ state.q=e.target.value; localStorage.setItem("hkii_q",state.q); render(); });
  $("#q").addEventListener("keydown", e=>{ if(e.key==="Enter"){ recordSearch(state.q); } });
  $("#searchBox").addEventListener("click", e=>{ const hs=e.target.closest("[data-hotsearch]"); if(!hs) return; state.q=hs.dataset.hotsearch; document.getElementById("q").value=state.q; const hd=document.getElementById("hotsearchDropdown"); if(hd) hd.style.display="none"; recordSearch(state.q); render(); });
  $("#content").addEventListener("click", e=>{
    const ft2=e.target.closest("#facetToggle"); if(ft2){ const fm=document.getElementById("facetMore"); if(fm) fm.style.display=fm.style.display==="none"?"":"none"; ft2.textContent=fm.style.display==="none"?"文种 ▾":"文种 ▴"; return; }const tc=e.target.closest("#themeChipsToggle"); if(tc){ const tf=document.getElementById("themeChipsFold"); if(tf){ tf.classList.toggle("open"); tc.textContent=tf.classList.contains("open")?"主题 ▴":"主题 ▾"; } return; }const hc=e.target.closest("[data-hot]"); if(hc){ state.q=hc.dataset.hot; document.getElementById("q").value=state.q; recordSearch(state.q); render(); return; }
    const email=e.target.closest("[data-email-digest]"); if(email){ e.stopPropagation(); const box=email.parentElement.nextElementSibling; box.style.display=box.style.display==="none"?"block":"none"; return; }
    const fav=e.target.closest("[data-fav]"); if(fav){ e.stopPropagation(); const id=fav.dataset.fav; state.fav.has(id)?state.fav.delete(id):state.fav.add(id); localStorage.setItem("hkii_fav", JSON.stringify([...state.fav])); trackEvent("fav", id); render(); return; }
    const favtag=e.target.closest("[data-favtag]"); if(favtag){ state.favTag = favtag.dataset.favtag || null; render(); return; }
    const o=e.target.closest("[data-open]"); if(o){ openDrawer(o.dataset.open); return; }
    // 主题雷达：进板块页（不跳全部动态）
    const bb=e.target.closest("[data-board-back]"); if(bb){ state.themeBoard=null; render(); return; }
    // 子主题过滤：需在 data-board 之前（热度条在板块卡片内部），主题雷达内点击跳转到全部动态
    const tf=e.target.closest("[data-theme-filter]"); if(tf){ state.themeFilter=tf.dataset.themeFilter; if(state.view==="themes"){ state.view="all"; state.themeBoard=null; } render(); return; }
    const bd=e.target.closest("[data-board]"); if(bd){ state.themeBoard=bd.dataset.board; render(); return; }
    const ft=e.target.closest("[data-feed-tier]"); if(ft){ state.feedTier=ft.dataset.feedTier; render(); return; }
    const fk=e.target.closest("[data-feed-kind]"); if(fk){ state.feedKind=fk.dataset.feedKind; render(); return; }
    const bf=e.target.closest("[data-board-filter]"); if(bf){ state.themeFilter=bf.dataset.boardFilter; render(); return; }
    // 档案
    const ap=e.target.closest("[data-arch-period]"); if(ap){ state.archivePeriod=ap.dataset.archPeriod; state.archiveKey=null; state.archivePage=1; render(); return; }
    const ab=e.target.closest("[data-arch-back]"); if(ab){ state.archiveKey=null; state.archivePage=1; render(); return; }
    const ak=e.target.closest("[data-arch-key]"); if(ak){ state.archiveKey=ak.dataset.archKey; render(); return; }
    const apg=e.target.closest("[data-arch-page]"); if(apg){ state.archivePage=parseInt(apg.dataset.archPage); render(); return; }
    const j=e.target.closest("[data-jump-theme]"); if(j){ state.view="themes"; state.themeBoard=j.dataset.jumpTheme; render(); return; }
    const em=e.target.closest("[data-export-md]"); if(em){ e.stopPropagation(); const it=byId(em.dataset.exportMd); if(!it) return; downloadText(`猫圈儿-${it.id}.md`, itemToMarkdown(it)); trackEvent("export", it.id); toast(T().mdDone); return; }
    const po=e.target.closest("[data-poster]"); if(po){ e.stopPropagation(); openPoster(po.dataset.poster); return; }
    const ed=e.target.closest("[data-export-digest]"); if(ed){
      e.stopPropagation();
      const digs=(DATA.digests&&DATA.digests[state.archivePeriod])||[];
      const dig=digs.find(x=>x.key===state.archiveKey); if(!dig) return;
      const gate=canExportDigest(state.archivePeriod);
      if(!gate.ok){ toast(T().proNeed.replace("{n}", String(gate.cost||0))); return; }
      if(gate.cost){ state.points-=gate.cost; savePoints(); }
      downloadText(`猫圈儿-${state.archivePeriod}-${dig.key}.md`, digestToMarkdown(dig)); toast(T().mdDone);
      applyChrome();
      return;
    }
    const c=e.target.closest(".card"); if(c) openDrawer(c.dataset.id);
  });
  // drawer action buttons (export live in drawer body)
  $("#dBody").addEventListener("click", e=>{
    const em=e.target.closest("[data-export-md]"); if(em){ const it=byId(em.dataset.exportMd); if(it){ downloadText(`猫圈儿-${it.id}.md`, itemToMarkdown(it)); trackEvent("export", it.id); } toast(T().mdDone); return; }
    const po=e.target.closest("[data-poster]"); if(po){ openPoster(po.dataset.poster); }
  });
  const pm=$("#posterModal");
  if(pm){
    $("#posterClose").addEventListener("click", closePoster);
    pm.addEventListener("click", e=>{ if(e.target===pm) closePoster(); });
  }

  $("#dClose").addEventListener("click", closeDrawer);
  $("#backdrop").addEventListener("click", closeDrawer);
  document.addEventListener("keydown", e=>{ if(e.key==="Escape"){ closePoster(); closeDrawer(); } });
  $(".sidebar-foot").addEventListener("click", e=>{
    const lang=e.target.closest("[data-lang]"); if(lang){ state.lang=lang.dataset.lang; localStorage.setItem("hkii_lang", state.lang); render(); return; }
    const th=e.target.closest("[data-theme-btn]"); if(th){ state.theme=th.dataset.themeBtn; localStorage.setItem("hkii_theme", state.theme); render(); }
  });
  $("#menuBtn").addEventListener("click", ()=>$("#sidebar").classList.toggle("open"));
  refreshGlobalHot();
  trackEvent("view", state.view || "pulse");
  render();

  // ── 后台静默加载全量条目（首屏已用 core 渲染，加载完自动刷新）──
  (async function () {
    try {
      const r = await fetch('data/items.json?v=' + (window.HKII_VER || ''), { cache: 'default' });
      if (!r.ok) return;
      const full = await r.json();
      if (full && Array.isArray(full.items) && full.items.length > (DATA.items || []).length) {
        DATA.items = full.items;
        window.HKII_DATA = DATA;
        render();
      }
    } catch (e) { /* 静默失败：core 数据仍可用 */ }
  })();
})();
