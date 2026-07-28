#!/usr/bin/env node
/**
 * Capture top-view screenshots of original source pages for all items.
 * Saves to assets/thumbs/{id}.png (1200x760 crop of page top).
 * Usage: node scripts/capture-thumbs.js [--only-missing] [--limit N]
 */
const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');

const ROOT = path.resolve(__dirname, '..');
const DATA = path.join(ROOT, 'data/live-items.json');
const OUT = path.join(ROOT, 'assets/thumbs');

const args = process.argv.slice(2);
const ONLY_MISSING = args.includes('--only-missing');
const limitIdx = args.indexOf('--limit');
const LIMIT = limitIdx >= 0 ? parseInt(args[limitIdx + 1]) : Infinity;

if (!fs.existsSync(OUT)) fs.mkdirSync(OUT, { recursive: true });

function sanitize(url) {
  try { return new URL(url).href; } catch { return null; }
}

(async () => {
  const data = JSON.parse(fs.readFileSync(DATA, 'utf-8'));
  let items = data.items.filter(i => i.originalUrl && sanitize(i.originalUrl));
  if (ONLY_MISSING) {
    items = items.filter(i => !fs.existsSync(path.join(OUT, `${i.id}.png`)));
  }
  items = items.slice(0, LIMIT === Infinity ? items.length : LIMIT);

  console.log(`Capturing ${items.length} thumbnails...`);

  const browser = await chromium.launch({ headless: true });
  const ctx = await browser.newContext({
    viewport: { width: 1280, height: 800 },
    userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36',
    locale: 'zh-HK',
  });
  const page = await ctx.newPage();

  let ok = 0, fail = 0;
  const results = [];
  for (let n = 0; n < items.length; n++) {
    const it = items[n];
    const outPath = path.join(OUT, `${it.id}.png`);
    try {
      await page.goto(it.originalUrl, { waitUntil: 'domcontentloaded', timeout: 25000 });
      // Wait a bit for content to settle
      await page.waitForTimeout(1800);
      // Scroll to top
      await page.evaluate(() => window.scrollTo(0, 0));
      await page.screenshot({ path: outPath, clip: { x: 0, y: 0, width: 1280, height: 800 } });
      ok++;
      results.push({ id: it.id, ok: true });
      if (n % 10 === 0) console.log(`  ${n + 1}/${items.length} ok=${ok} fail=${fail} ${it.id}`);
    } catch (e) {
      fail++;
      results.push({ id: it.id, ok: false, err: String(e).slice(0, 100) });
      console.log(`  FAIL ${it.id}: ${String(e).slice(0, 80)}`);
    }
  }

  await browser.close();
  fs.writeFileSync(
    path.join(OUT, '_manifest.json'),
    JSON.stringify({ generatedAt: new Date().toISOString(), ok, fail, results }, null, 2)
  );
  console.log(`DONE ok=${ok} fail=${fail}`);
})();
