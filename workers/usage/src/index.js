/**
 * 猫圈儿港险情报站 · 使用度聚合 Worker
 *
 * POST /e  {t, v?, r?, p?}   — 事件上报（fire-and-forget）
 *   t = event type: search | open | view | role | poster | fav | export
 *   v = value (search term / itemId / view id / role id / poster theme)
 *   r = role (optional, current role at event time)
 *   p = path/page (optional)
 *
 * GET  /hot?n=20             — 热搜 top N（公开，供前端「大家都在搜」）
 * GET  /stats?days=7         — 汇总（需 ?key=ADMIN_KEY，可选）
 *
 * KV keys:
 *   s:YYYY-MM-DD:{term}      → count (search)
 *   o:YYYY-MM-DD:{itemId}    → count (open)
 *   v:YYYY-MM-DD:{view}      → count (view switch)
 *   r:YYYY-MM-DD:{role}      → count (role select)
 *   p:YYYY-MM-DD:{theme}     → count (poster download)
 *   f:YYYY-MM-DD             → count (fav toggle)
 *   x:YYYY-MM-DD             → count (export md)
 *   day:YYYY-MM-DD           → total events that day
 */

const MAX_TERM_LEN = 40;
const MAX_ID_LEN = 80;
const RATE_WINDOW_MS = 60_000;
const RATE_MAX = 60; // per IP per minute
const ipBuckets = new Map(); // best-effort in-isolate rate limit

function corsHeaders(origin, allowed) {
  const ok = !origin || origin === allowed || origin.endsWith(".hkmaoquanqingbao.com");
  return {
    "Access-Control-Allow-Origin": ok ? (origin || allowed) : allowed,
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Max-Age": "86400",
    "Vary": "Origin",
  };
}

function todayUTC() {
  return new Date().toISOString().slice(0, 10);
}

function cleanStr(s, max) {
  if (typeof s !== "string") return "";
  return s.trim().slice(0, max);
}

// 拼音中间态：纯字母 + 含撇号
function isPinyinJunk(k) {
  return /^[a-z']+$/i.test(k) && k.includes("'");
}

function rateLimit(ip) {
  const now = Date.now();
  let b = ipBuckets.get(ip);
  if (!b || now - b.ts > RATE_WINDOW_MS) {
    b = { ts: now, n: 0 };
    ipBuckets.set(ip, b);
  }
  b.n += 1;
  // 防止 map 无限涨
  if (ipBuckets.size > 5000) {
    for (const [k, v] of ipBuckets) {
      if (now - v.ts > RATE_WINDOW_MS) ipBuckets.delete(k);
    }
  }
  return b.n <= RATE_MAX;
}

async function incr(kv, key, ttlSec = 60 * 60 * 24 * 90) {
  const cur = parseInt((await kv.get(key)) || "0", 10) || 0;
  await kv.put(key, String(cur + 1), { expirationTtl: ttlSec });
  return cur + 1;
}

async function handleEvent(req, env, cors) {
  let body;
  try {
    body = await req.json();
  } catch {
    return new Response(JSON.stringify({ ok: false, err: "bad json" }), {
      status: 400,
      headers: { ...cors, "Content-Type": "application/json" },
    });
  }

  const t = cleanStr(body.t || body.type || "", 16);
  const v = cleanStr(body.v || body.value || "", MAX_TERM_LEN);
  const r = cleanStr(body.r || body.role || "", 16);
  if (!t) {
    return new Response(JSON.stringify({ ok: false, err: "missing t" }), {
      status: 400,
      headers: { ...cors, "Content-Type": "application/json" },
    });
  }

  const day = todayUTC();
  const kv = env.USAGE_KV;

  try {
    await incr(kv, `day:${day}`);

    if (t === "search" && v && v.length >= 2 && !isPinyinJunk(v)) {
      await incr(kv, `s:${day}:${v}`);
    } else if (t === "open" && v) {
      await incr(kv, `o:${day}:${cleanStr(v, MAX_ID_LEN)}`);
    } else if (t === "view" && v) {
      await incr(kv, `v:${day}:${v}`);
    } else if (t === "role" && v) {
      await incr(kv, `r:${day}:${v}`);
    } else if (t === "poster" && v) {
      await incr(kv, `p:${day}:${v}`);
    } else if (t === "fav") {
      await incr(kv, `f:${day}`);
    } else if (t === "export") {
      await incr(kv, `x:${day}`);
    }
    // 可选：顺带记当前角色分布
    if (r && t !== "role") {
      await incr(kv, `r:${day}:${r}`);
    }
  } catch (e) {
    return new Response(JSON.stringify({ ok: false, err: "kv" }), {
      status: 500,
      headers: { ...cors, "Content-Type": "application/json" },
    });
  }

  return new Response(JSON.stringify({ ok: true }), {
    status: 200,
    headers: { ...cors, "Content-Type": "application/json" },
  });
}

async function handleHot(url, env, cors) {
  const n = Math.min(50, Math.max(1, parseInt(url.searchParams.get("n") || "20", 10) || 20));
  const days = Math.min(30, Math.max(1, parseInt(url.searchParams.get("days") || "14", 10) || 14));
  const kv = env.USAGE_KV;
  const scores = new Map();

  // 扫近 N 天 search keys
  for (let i = 0; i < days; i++) {
    const d = new Date(Date.now() - i * 86400000).toISOString().slice(0, 10);
    const prefix = `s:${d}:`;
    let cursor;
    do {
      const page = await kv.list({ prefix, cursor, limit: 1000 });
      for (const k of page.keys || []) {
        const term = k.name.slice(prefix.length);
        if (!term || isPinyinJunk(term)) continue;
        const c = parseInt((await kv.get(k.name)) || "0", 10) || 0;
        // 近 3 天权重 ×2
        const w = i < 3 ? 2 : 1;
        scores.set(term, (scores.get(term) || 0) + c * w);
      }
      cursor = page.list_complete ? null : page.cursor;
    } while (cursor);
  }

  const top = [...scores.entries()]
    .sort((a, b) => b[1] - a[1])
    .slice(0, n)
    .map(([term, count]) => ({ term, count }));

  return new Response(JSON.stringify({ ok: true, days, items: top, asOf: new Date().toISOString() }), {
    status: 200,
    headers: {
      ...cors,
      "Content-Type": "application/json",
      "Cache-Control": "public, max-age=300",
    },
  });
}

async function handleStats(url, env, cors) {
  // 轻量汇总：近 N 天 day:* + 角色/view/poster 分布
  const days = Math.min(30, Math.max(1, parseInt(url.searchParams.get("days") || "7", 10) || 7));
  const kv = env.USAGE_KV;
  const out = { days, daily: [], roles: {}, views: {}, posters: {}, opens: 0, searches: 0, favs: 0, exports: 0 };

  for (let i = 0; i < days; i++) {
    const d = new Date(Date.now() - i * 86400000).toISOString().slice(0, 10);
    const total = parseInt((await kv.get(`day:${d}`)) || "0", 10) || 0;
    const fav = parseInt((await kv.get(`f:${d}`)) || "0", 10) || 0;
    const exp = parseInt((await kv.get(`x:${d}`)) || "0", 10) || 0;
    out.daily.push({ date: d, events: total, fav, export: exp });
    out.favs += fav;
    out.exports += exp;

    for (const [prefix, bucket, counter] of [
      ["r:", "roles", null],
      ["v:", "views", null],
      ["p:", "posters", null],
      ["o:", null, "opens"],
      ["s:", null, "searches"],
    ]) {
      let cursor;
      do {
        const page = await kv.list({ prefix: `${prefix}${d}:`, cursor, limit: 1000 });
        for (const k of page.keys || []) {
          const c = parseInt((await kv.get(k.name)) || "0", 10) || 0;
          if (bucket) {
            const key = k.name.slice(`${prefix}${d}:`.length);
            out[bucket][key] = (out[bucket][key] || 0) + c;
          }
          if (counter) out[counter] += c;
        }
        cursor = page.list_complete ? null : page.cursor;
      } while (cursor);
    }
  }

  return new Response(JSON.stringify({ ok: true, ...out, asOf: new Date().toISOString() }), {
    status: 200,
    headers: { ...cors, "Content-Type": "application/json", "Cache-Control": "private, max-age=60" },
  });
}

export default {
  async fetch(req, env) {
    const allowed = env.ALLOWED_ORIGIN || "https://hkmaoquanqingbao.com";
    const origin = req.headers.get("Origin") || "";
    const cors = corsHeaders(origin, allowed);
    const url = new URL(req.url);

    if (req.method === "OPTIONS") {
      return new Response(null, { status: 204, headers: cors });
    }

    // health
    if (url.pathname === "/" || url.pathname === "/health") {
      return new Response(JSON.stringify({ ok: true, service: "hkii-usage" }), {
        headers: { ...cors, "Content-Type": "application/json" },
      });
    }

    const ip = req.headers.get("CF-Connecting-IP") || req.headers.get("X-Forwarded-For") || "unknown";
    if (req.method === "POST" && (url.pathname === "/e" || url.pathname === "/event" || url.pathname === "/search-log")) {
      if (!rateLimit(ip)) {
        return new Response(JSON.stringify({ ok: false, err: "rate" }), {
          status: 429,
          headers: { ...cors, "Content-Type": "application/json" },
        });
      }
      return handleEvent(req, env, cors);
    }

    if (req.method === "GET" && url.pathname === "/hot") {
      return handleHot(url, env, cors);
    }

    if (req.method === "GET" && url.pathname === "/stats") {
      return handleStats(url, env, cors);
    }

    return new Response(JSON.stringify({ ok: false, err: "not found" }), {
      status: 404,
      headers: { ...cors, "Content-Type": "application/json" },
    });
  },
};
