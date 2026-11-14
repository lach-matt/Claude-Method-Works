// render.mjs IN.html OUT.pdf -- print the HTML to A4 PDF in Playwright's Chromium,
// page numbers in the footer, after checking that nothing overflows the measure.
import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright');
import { pathToFileURL } from 'node:url';
import path from 'node:path';

const [inHtml, outPdf] = process.argv.slice(2);
const browser = await chromium.launch();
// A4 is 210 mm; less 2 x 16 mm margins = 178 mm = 672.76 CSS px at 96 dpi.
const page = await browser.newPage({ viewport: { width: 673, height: 1000 }, deviceScaleFactor: 1 });
await page.goto(pathToFileURL(path.resolve(inHtml)).href, { waitUntil: 'load' });
await page.emulateMedia({ media: 'print' });
await page.evaluate(() => document.fonts.ready);

const over = await page.evaluate(() => {
  const W = document.body.clientWidth, bad = [];
  for (const el of document.querySelectorAll('pre, table, p, li, td, th, blockquote, code, h1, h2, h3')) {
    const r = el.getBoundingClientRect();
    const spill = Math.max(el.scrollWidth - el.clientWidth, r.right - W);
    if (spill > 1 && getComputedStyle(el).display !== 'inline')
      bad.push(`${el.tagName} +${spill.toFixed(1)}px: ${el.textContent.slice(0, 70)}`);
    if (getComputedStyle(el).display === 'inline' && r.right > W + 1)
      bad.push(`${el.tagName} (inline) right=${r.right.toFixed(1)} > ${W}: ${el.textContent.slice(0, 70)}`);
  }
  // display blocks that had to wrap (a wrapped equation line breaks its alignment)
  const lh = s => parseFloat(getComputedStyle(s).lineHeight);
  const wrapped = [...document.querySelectorAll('pre')].filter(p => {
    const n = p.textContent.replace(/\n$/, '').split('\n').length;
    const cs = getComputedStyle(p);
    const h = p.clientHeight - parseFloat(cs.paddingTop) - parseFloat(cs.paddingBottom);
    return Math.round(h / lh(p)) > n;
  }).map(p => p.textContent.slice(0, 60));
  return { W, bad, wrapped };
});
console.log(`measure ${over.W}px; overflowing elements: ${over.bad.length}; wrapped display blocks: ${over.wrapped.length}`);
for (const b of over.bad) console.log('  OVERFLOW ' + b);
for (const b of over.wrapped) console.log('  WRAPPED ' + b);

await page.pdf({
  path: outPdf, format: 'A4', preferCSSPageSize: true, printBackground: true,
  displayHeaderFooter: true,
  headerTemplate: '<div></div>',
  footerTemplate: `<div style="width:100%;text-align:center;font:8.5pt Georgia,'Times New Roman',serif;color:#555;">
    <span class="pageNumber"></span> / <span class="totalPages"></span></div>`,
});
await browser.close();
if (over.bad.length) process.exitCode = 2;
