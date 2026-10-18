#!/usr/bin/env node
// tools/sitecheck.mjs -- the site's click-through, in headless Chromium at the site's own address.
//
// The page is opened at https://lach-matt.github.io/Claude-Method-Works/ whatever the target, so its
// origin, its history and every address it writes are the deployed site's. Only where the bytes come
// from changes:
//
//   --target worktree        this checkout's public/ (the default: check a change before committing it)
//   --target commit[=REV]    the public/ of a commit (default origin/main, the one Pages deploys), each
//                            key file first held against the copy GitHub serves for that commit
//   --target live            the network, as a reader gets it; needs the session's proxy to allow
//                            lach-matt.github.io, and stops with a note where it does not
//
//   --root DIR               with the worktree target, serve DIR in place of public/ (a built copy,
//                            or a deliberately broken one to prove a check catches what it names)
//   --suite papers,routing,review   which scenarios to run (default all)
//   --nonav     remove the Navigation API, as a browser without it has; the checks that need it are
//               reported n/a, since the page's fallback for them is documented in docs/WEB-INDEX.md
//   --list      name every scenario and check without running them
//
// The page Back must reach before the site is a stand-in served here (https://elsewhere.example/),
// so no target needs any other host. Exit status: 0 all pass, 1 a check failed or the page threw,
// 2 the run could not start. See docs/SITECHECK.md.
import { execFileSync, spawnSync } from 'node:child_process';
import { X509Certificate, createHash } from 'node:crypto';
import { existsSync, mkdtempSync, readFileSync, rmSync } from 'node:fs';
import { readFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const REPO = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const SITE = 'https://lach-matt.github.io/Claude-Method-Works/';
const ELSEWHERE = 'https://elsewhere.example/';
const RAW = 'https://raw.githubusercontent.com/lach-matt/Claude-Method-Works/';
// the files held against GitHub's copy before a commit's bytes are served
const KEY_FILES = ['index.html', 'script.js', 'style.css', 'data/index.js', 'data/papers.js',
  'data/papers/everything-is-relative/EVERYTHING-IS-RELATIVE.pdf'];
const TYPES = { '.html': 'text/html; charset=utf-8', '.js': 'application/javascript; charset=utf-8', '.css': 'text/css; charset=utf-8',
  '.pdf': 'application/pdf', '.png': 'image/png', '.jpg': 'image/jpeg', '.svg': 'image/svg+xml', '.tsv': 'text/tab-separated-values; charset=utf-8',
  '.json': 'application/json', '.txt': 'text/plain; charset=utf-8' };

// ---------------------------------------------------------------- arguments
const argv = process.argv.slice(2);
const flag = (name) => argv.includes(name);
const opt = (name, dflt) => { const a = argv.find((x) => x === name || x.startsWith(name + '=')); if (!a) return dflt; const i = argv.indexOf(a); return a.includes('=') ? a.slice(name.length + 1) : (argv[i + 1] && !argv[i + 1].startsWith('--') ? argv[i + 1] : dflt); };
const die = (m) => { console.error(m); process.exit(2); };
// every argument is a known flag, a known option with its value, or that value: anything else is a
// mistake to stop on, not to ignore (a misspelt --nonav would otherwise run with the API present)
for (let i = 0; i < argv.length; i++) {
  const a = argv[i], name = a.split('=')[0];
  if (a === '--nonav' || a === '--list') continue;
  if (!['--target', '--suite', '--root'].includes(name)) die(`unknown argument ${a}${a.startsWith('--') ? '' : ' (use --target commit=REV)'}`);
  if (a.includes('=') ? a.length === name.length + 1 : !argv[i + 1] || argv[i + 1].startsWith('--')) die(`${name} needs a value`);
  if (!a.includes('=')) i++;
}
const targetArg = opt('--target', 'worktree');
const tm = /^(worktree|live|commit)(?:=(.+))?$/s.exec(targetArg);
if (!tm || (tm[2] !== undefined && tm[1] !== 'commit')) die(`unknown --target ${targetArg}`);
const [TARGET, REV] = [tm[1], tm[1] === 'commit' ? (tm[2] || 'origin/main') : null];
if (opt('--root') !== undefined && TARGET !== 'worktree') die('--root serves a directory with the worktree target only');
let SUITES = new Set(opt('--suite', 'all').split(','));
const NONAV = flag('--nonav'), LIST = flag('--list');

// ---------------------------------------------------------------- the scenarios
// scenario(suite, name, fn): fn receives { open, st, ok, W } and opens its own pages; every page is
// its own browser context, closed when the scenario ends, so one scenario cannot leak into the next
const SCENARIOS = [];
const scenario = (suite, name, fn) => SCENARIOS.push({ suite, name, fn });
const B = SITE;
const LO = /LÖWDIN/;
const DESK = { width: 1400, height: 900 }, PHONE = { width: 390, height: 844 };

// ---- papers: the Papers dialog, the reader and the renderer
for (const vp of [DESK, PHONE]) scenario('papers', `the Papers dialog and Everything Is Relative at ${vp.width} px`, async ({ open, ok, W }) => {
  const p = await open(vp); await p.goto(B); await W(p, 2500);
  await p.click('#btn-papers'); await W(p, 2500);
  const cards = await p.$$eval('.paper-card h3', (hs) => hs.map((h) => h.textContent));
  const held = await p.evaluate(() => (window.__mi.papers || []).filter((x) => x.held).length);
  ok('every held paper has a card, Everything Is Relative last', cards.length === held && held >= 15 && cards[cards.length - 1] === 'Everything Is Relative', { cards: cards.length, held, last: cards[cards.length - 1] });
  await p.click('button[data-paper="everything-is-relative"]'); await W(p, 1500);
  const r = await p.evaluate(async () => {
    const a = document.querySelector('#paper-article'), pp = window.__mi.papers.find((x) => x.slug === 'everything-is-relative');
    const pdf = [...document.querySelectorAll('.paper-toc a')].find((x) => x.textContent === 'PDF');
    const got = pdf ? await fetch(pdf.getAttribute('href')).then(async (x) => [x.status, (await x.arrayBuffer()).byteLength]) : null;
    return { h1: a.querySelector('h1') && a.querySelector('h1').textContent, std: a.querySelectorAll('p')[0].textContent, by: a.querySelectorAll('p')[1].textContent,
      yaml: /title:\s*"/.test(a.textContent), toc: document.querySelectorAll('.paper-toc a[data-h]').length, heads: pp.headings.filter((h) => h.level >= 2 && h.level <= 3).length,
      pdf: got, pdfBytes: pp.pdf && pp.pdf.bytes, witness: /matches the released copy/.test(document.querySelector('.paper-toc').textContent),
      hscroll: document.documentElement.scrollWidth > document.documentElement.clientWidth };
  });
  ok('the title block is the front matter\'s: title, standfirst, byline, no YAML', r.h1 === 'Everything Is Relative' && /^How quantum physics stands to relativity/.test(r.std) && r.by === 'Matthew Lach · Independent Researcher · 16 October 2026' && !r.yaml, r);
  ok('the contents carry every section heading', r.toc === r.heads && r.toc > 0, { toc: r.toc, heads: r.heads });
  ok('the PDF is served whole and matches the released copy', r.pdf && r.pdf[0] === 200 && r.pdf[1] === r.pdfBytes && r.witness, r);
  ok('no horizontal scroll', !r.hscroll, r.hscroll);
  const id = await p.evaluate(() => document.querySelectorAll('.paper-toc a[data-h]')[4].dataset.h);
  await p.click(`.paper-toc a[data-h="${id}"]`); await W(p, 1200);
  const j = await p.evaluate((h) => { const b = document.querySelector('#papers-body'), t = document.getElementById(h);
    return { open: document.querySelector('#dlg-papers').open, hash: location.hash, scroll: b.scrollTop, off: t ? Math.round(t.getBoundingClientRect().top - b.getBoundingClientRect().top) : null }; }, id);
  ok('a contents link scrolls to its heading, the paper and its address kept', j.open && j.hash === '#paper=everything-is-relative' && j.scroll > 0 && j.off !== null && Math.abs(j.off) < 40, j);
});
scenario('papers', 'what the renderer must get right in the papers', async ({ open, ok, W }) => {
  const p = await open(DESK); await p.goto(B + '#paper=everything-is-relative'); await W(p, 3000);
  const r = await p.evaluate(() => {
    const a = document.querySelector('#paper-article');
    const p1 = [...a.querySelectorAll('li')].find((li) => li.textContent.startsWith('P1.'));
    return { pipes: [...a.querySelectorAll('td')].map((td) => td.textContent).filter((t) => /16\|α\|m|8\|Hḟ\||\|ξ\|²/.test(t)).length,
      escapes: (a.textContent.match(/\\[_|[\]*]/g) || []).length,
      jhep: [...a.querySelectorAll('a[href*="JHEP"]')].map((x) => x.getAttribute('href')),
      grqc: [...a.querySelectorAll('a[href="https://arxiv.org/abs/gr-qc/0411023"]')].map((x) => x.textContent),
      rtr: (a.textContent.match(/R\^\{tr\}_\{tr\}/g) || []).length,
      unlinked: (() => { const pp = window.__mi.papers.find((x) => x.slug === 'everything-is-relative');
        const hrefs = new Set([...a.querySelectorAll('a[href]')].map((x) => x.getAttribute('href')));
        return [...pp.arxiv.map((i) => 'https://arxiv.org/abs/' + i), ...pp.doi.map((i) => 'https://doi.org/' + i)].filter((u) => !hrefs.has(u)); })(),
      p1: p1 && /no other scale\.$/.test(p1.textContent.trim()), p1list: p1 && p1.parentElement.children.length };
  });
  ok('escaped pipes are literal pipes in their table cells', r.pipes === 3, r.pipes);
  ok('no backslash escape survives the render', r.escapes === 0, r.escapes);
  ok('a DOI with a balanced parenthesised group links whole', JSON.stringify(r.jhep.sort()) === JSON.stringify(['https://doi.org/10.1007/JHEP02(2016)020', 'https://doi.org/10.1007/JHEP08(2022)157']), r.jhep);
  ok('an old-style arXiv id with a version suffix is linked, as printed, at both its sites', r.grqc.length === 2 && r.grqc.every((t) => t === 'gr-qc/0411023v3'), r.grqc);
  ok('every arXiv and DOI identifier the paper cites is linked', r.unlinked.length === 0, r.unlinked);
  ok('an escaped underscore is its character: R^{tr}_{tr} as printed', r.rtr >= 1, r.rtr);
  ok('a list item\'s lazy continuation stays in it: P1 whole, P1–P4 one list', r.p1 && r.p1list === 4, r);
  for (const slug of ['closure-beyond', 'languages', 'bracket', 'closure-law', 'indexes']) {
    await p.evaluate((s) => { location.hash = '#paper=' + s; }, slug); await W(p, 1300);
    const q = await p.evaluate(() => { const a = document.querySelector('#paper-article'); return { escapes: (a.textContent.match(/\\[_|[\]*]/g) || []).length,
      dead: [...a.querySelectorAll('a')].filter((x) => !/^(https?:|mailto:|#|data\/)/.test(x.getAttribute('href') || '')).length, cl: (a.textContent.match(/cl\[[Lab]\]\(X\)/g) || []).length }; });
    ok(`${slug}: no escape printed, no dead link${slug === 'indexes' ? ', cl[L](X) printed as written' : ''}`, q.escapes === 0 && q.dead === 0 && (slug !== 'indexes' || q.cl >= 6), q);
  }
});

// ---- routing: a paper's cite address, the address and the dialog in step, history
scenario('routing', 'Back off a paper\'s address closes it; Forward reopens', async ({ open, st, ok, W }) => {
  const p = await open(); await p.goto(B + '#/Fe'); await W(p, 3000);
  await p.evaluate(() => { location.hash = '#paper=lowdin'; }); await W(p, 1800);
  let s = await st(p); ok('a hash to a paper opens it', s.open && LO.test(s.h1) && s.hash === '#paper=lowdin', s);
  await p.goBack(); await W(p, 1800); s = await st(p); ok('Back closes the paper, explorer at Fe', !s.open && s.hash === '#/Fe' && /Fe$/.test(s.crumbs), s);
  await p.goForward(); await W(p, 1800); s = await st(p); ok('Forward reopens it', s.open && LO.test(s.h1), s);
  await p.evaluate(() => { location.hash = '#/p/mesons'; }); await W(p, 3500); s = await st(p); ok('a particle route closes it', !s.open && s.hash.startsWith('#/p/mesons'), s);
});
scenario('routing', 'closing gives the explorer its address back; the same citation reopens', async ({ open, st, ok, W }) => {
  const p = await open(); await p.goto(B + '#paper=lowdin'); await W(p, 3000);
  await p.keyboard.press('Escape'); await W(p, 600); let s = await st(p); ok('Escape restores #/', !s.open && s.hash === '#/', s);
  await p.evaluate(() => { location.hash = '#paper=lowdin'; }); await W(p, 1500); s = await st(p); ok('the same citation reopens', s.open && LO.test(s.h1), s);
  await p.click('#dlg-papers [data-close="dlg-papers"]'); await W(p, 600); s = await st(p); ok('✕ restores #/', !s.open && s.hash === '#/', s);
  await p.goto(B + '#paper=lowdin'); await W(p, 2500); s = await st(p); ok('navigating to the same URL reopens', s.open && LO.test(s.h1), s);
});
scenario('routing', 'reading another paper keeps the address in step', async ({ open, st, ok, W }) => {
  const p = await open(); await p.goto(B + '#paper=tower'); await W(p, 3000);
  await p.click('[data-act="papers-back"]'); await W(p, 800); let s = await st(p); ok('the list gives the explorer address', s.open && s.cards >= 15 && s.hash === '#/', s);
  await p.click('button[data-paper="bracket"]'); await W(p, 1000); s = await st(p); ok('reading Bracket names it', /Bracket/.test(s.h1) && s.hash === '#paper=bracket', s);
  await p.reload(); await W(p, 3000); s = await st(p); ok('a reload shows Bracket', s.open && /Bracket/.test(s.h1), s);
});
scenario('routing', 'a citation read loosely, as it is pasted', async ({ open, st, ok, W }) => {
  for (const [h, want, canon] of [['#paper=lowdin.', LO, '#paper=lowdin'], ['#paper=lowdin)', LO, '#paper=lowdin'], ['#paper=lowdin/', LO, '#paper=lowdin'],
    ['#paper=lowdin&utm_source=x', LO, '#paper=lowdin'], ['#paper=three%2Dbody', /Three-Body/, '#paper=three-body'], ['#paper=Tower', /Tower/, '#paper=tower'],
    ['#paper=everything-is-relative', /Everything/, '#paper=everything-is-relative']]) {
    const p = await open(); await p.goto(B + h); await W(p, 3000); const s = await st(p); ok(h, s.open && want.test(s.h1 || '') && s.hash === canon, s); await p.context().close();
  }
  let p = await open(); await p.goto(B + '#paper='); await W(p, 3000); let s = await st(p); ok('#paper= (empty) gives the list', s.open && s.cards >= 15 && s.hash === '#/', s); await p.context().close();
  p = await open(); await p.goto(B + '#paper=nope'); await W(p, 3000); s = await st(p); ok('an unknown name keeps its address and says so', s.open && /no paper named “nope”/.test(s.note) && s.hash === '#paper=nope', s);
  await p.click('[data-act="papers-back"]'); await W(p, 800); s = await st(p); ok('an unknown name → the list restores #/', s.cards >= 15 && s.hash === '#/', s);
});
for (const vp of [DESK, PHONE]) scenario('routing', `focus on a cited paper at ${vp.width} px`, async ({ open, st, ok, W }) => {
  const p = await open(vp); await p.goto(B + '#paper=tower'); await W(p, 3000);
  let s = await st(p); ok('focus on the paper body', s.active === 'papers-body', s);
  await p.keyboard.press('PageDown'); await W(p, 400); await p.keyboard.press('Space'); await W(p, 400); s = await st(p);
  ok('PageDown and Space scroll it and keep it open', s.open && s.scroll > 0, s);
  ok('no horizontal scroll', await p.evaluate(() => document.documentElement.scrollWidth <= document.documentElement.clientWidth), null);
});
scenario('routing', 'the Papers button flow, and a close raced by a new citation', async ({ open, st, ok, W }) => {
  const p = await open(); await p.goto(B + '#/Fe'); await W(p, 3000);
  await p.click('#btn-papers'); await W(p, 1500); let s = await st(p); ok('the button opens the list, address unchanged', s.cards >= 15 && s.hash === '#/Fe', s);
  await p.click('button[data-paper="lattice"]'); await W(p, 1000); s = await st(p); ok('Read names the paper', s.hash === '#paper=lattice', s);
  await p.keyboard.press('Escape'); await W(p, 600); s = await st(p); ok('closing restores #/Fe', !s.open && s.hash === '#/Fe', s);
  await p.click('#btn-papers'); await W(p, 1000); s = await st(p); ok('reopening names the paper shown', s.open && /Lattice/.test(s.h1) && s.hash === '#paper=lattice', s);
  await p.evaluate(() => { document.querySelector('#dlg-papers').close(); location.hash = '#paper=tower'; }); await W(p, 1500); s = await st(p);
  ok('a close then a new citation at once: the new one wins', s.open && /Tower/.test(s.h1) && s.hash === '#paper=tower', s);
});
scenario('routing', 'the explorer\'s own routes, and every Cite address', async ({ open, st, ok, W }) => {
  const p = await open();
  for (const [h, re] of [['#/Fe/iso/56', /A = 56/], ['#/Fe/II', /Fe › II/], ['#/', /^Index$/]]) { await p.goto(B + h); await W(p, 3000); const s = await st(p); ok('route ' + h, !s.open && re.test(s.crumbs), s); }
  await p.goto(B); await W(p, 3000); await p.click('#btn-papers'); await W(p, 1500);
  const slugs = await p.$$eval('button[data-cite]', (bs) => bs.map((x) => x.dataset.cite)); const bad = [];
  for (const sl of slugs) {
    await p.click(`button[data-cite="${sl}"]`); await W(p, 120); const line = await p.evaluate(() => document.querySelector('#papers-body .cite-box').textContent);
    const q = await open({ width: 1200, height: 800 }); await q.goto(B + line.slice(line.indexOf('#'))); await W(q, 2500); const s = await st(q);
    if (!(line.includes(SITE) && s.open && s.h1 && s.hash === '#paper=' + sl)) bad.push([sl, line, s]); await q.context().close();
  }
  ok(`all ${slugs.length} Cite addresses name the site and open their paper`, slugs.length >= 15 && !bad.length, bad);
});
for (const vp of [DESK, PHONE]) scenario('routing', `Read from the list at ${vp.width} px: focus, scrolling, no keys behind the dialog`, async ({ open, st, ok, W }) => {
  const p = await open(vp); await p.goto(B + '#/Fe'); await W(p, 3000);
  await p.click('#btn-papers'); await W(p, 1500); await p.click('button[data-paper="lowdin"]'); await W(p, 1200);
  let s = await st(p); ok('focus on the paper', s.active === 'papers-body' && s.hash === '#paper=lowdin', s);
  for (let i = 0; i < 6; i++) await p.keyboard.press('ArrowDown'); await W(p, 300);
  s = await st(p); ok('ArrowDown scrolls the paper', s.scroll > 0, s);
  await p.keyboard.press('h'); await W(p, 600); s = await st(p); ok('h does not act behind the dialog', s.open && s.hash === '#paper=lowdin' && /Fe$/.test(s.crumbs), s);
  const cam = s.cam; await p.evaluate(() => document.activeElement.blur()); await W(p, 200);
  for (const k of ['h', '+', 'ArrowRight']) { await p.keyboard.press(k); await W(p, 400); }
  s = await st(p); ok('with focus fallen to the page, still no key acts behind the dialog', s.open && s.hash === '#paper=lowdin' && /Fe$/.test(s.crumbs) && Array.isArray(cam) && JSON.stringify(s.cam) === JSON.stringify(cam), s);
  await p.click('[data-act="papers-back"]'); await W(p, 800); s = await st(p); ok('back to the list keeps focus in the dialog', s.active === 'papers-body' && s.hash === '#/Fe', s);
});
scenario('routing', 'reopening with the Papers button: focus on the paper', async ({ open, st, ok, W }) => {
  const p = await open(); await p.goto(B + '#paper=lowdin'); await W(p, 3000);
  await p.keyboard.press('Escape'); await W(p, 600); await p.click('#btn-papers'); await W(p, 1200);
  let s = await st(p); ok('reopened on the paper, named, focused', s.open && LO.test(s.h1) && s.hash === '#paper=lowdin' && s.active === 'papers-body', s);
  await p.keyboard.press('Space'); await W(p, 400); s = await st(p); ok('Space scrolls it and keeps it open', s.open && s.scroll > 0, s);
});
scenario('routing', 'citations read and closed leave no dead Back presses', async ({ open, st, ok, W, onSite }) => {
  let p = await open(); await p.goto(ELSEWHERE); await p.goto(B + '#/Fe'); await W(p, 3000);
  for (const sl of ['lowdin', 'tower', 'bracket']) { await p.evaluate((x) => { location.hash = '#paper=' + x; }, sl); await W(p, 1500); await p.keyboard.press('Escape'); await W(p, 900); }
  let s = await st(p); ok('after three citations closed, at #/Fe', !s.open && s.hash === '#/Fe', s);
  await p.goBack(); await W(p, 1500); ok('one Back leaves the site', !onSite(p), p.url(), { nav: true }); await p.context().close();
  p = await open(); await p.goto(ELSEWHERE); await p.goto(B + '#/Fe'); await W(p, 3000);
  await p.evaluate(() => { location.hash = '#paper=lowdin'; }); await W(p, 1500);
  await p.click('[data-act="papers-back"]'); await W(p, 900); s = await st(p); ok('the list path: at #/Fe, the list open', s.open && s.cards >= 15 && s.hash === '#/Fe', s);
  await p.keyboard.press('Escape'); await W(p, 600); await p.goBack(); await W(p, 1500); ok('the list path: one Back leaves the site', !onSite(p), p.url(), { nav: true });
});
scenario('routing', 'Back and Forward through a citation', async ({ open, st, ok, W }) => {
  const p = await open(); await p.goto(B + '#/Fe'); await W(p, 3000);
  await p.evaluate(() => { location.hash = '#paper=lowdin'; }); await W(p, 1500);
  await p.evaluate(() => { location.hash = '#/Cu'; }); await W(p, 2500);
  let s = await st(p); ok('a route after a citation closes it', !s.open && /Cu$/.test(s.crumbs), s);
  await p.goBack(); await W(p, 1500); s = await st(p); ok('Back to the citation reopens it', s.open && LO.test(s.h1) && s.hash === '#paper=lowdin', s);
  await p.keyboard.press('Escape'); await W(p, 1200); s = await st(p); ok('closing it steps forward to #/Cu, no copy', !s.open && s.hash === '#/Cu', s);
  await p.goBack(); await W(p, 1500); s = await st(p); ok('Back from there reopens the citation', s.open && LO.test(s.h1), s, { nav: true });
});
scenario('routing', 'a pasted citation, then the list, the button or Back (with a page before the site)', async ({ open, st, ok, W, onSite }) => {
  const off = (p) => onSite(p) ? null : { url: p.url() };
  let p = await open(); await p.goto(ELSEWHERE); await p.goto(B + '#/Fe'); await W(p, 3000);
  await p.goto(B + '#paper=lowdin'); await W(p, 1800);
  await p.keyboard.press('Escape'); await W(p, 900); await p.click('#btn-papers'); await W(p, 1200);
  let s = await st(p); ok('Escape then Papers reopens Löwdin', s.open && LO.test(s.h1) && s.hash === '#paper=lowdin', s);
  await p.goBack(); await W(p, 1800); s = off(p) || await st(p); ok('Back closes it at #/Fe, on the site', onSite(p) && !s.open && s.hash === '#/Fe' && /Fe$/.test(s.crumbs), s); await p.context().close();
  p = await open(); await p.goto(ELSEWHERE); await p.goto(B + '#/Fe'); await W(p, 3000);
  await p.goto(B + '#paper=lowdin'); await W(p, 1800);
  await p.click('[data-act="papers-back"]'); await W(p, 900); await p.click('button[data-paper="tower"]'); await W(p, 1200);
  s = await st(p); ok('← all papers then Read Tower names it', /Tower/.test(s.h1) && s.hash === '#paper=tower', s);
  await p.goBack(); await W(p, 1800); s = off(p) || await st(p); ok('Back closes Tower at #/Fe, on the site', onSite(p) && !s.open && s.hash === '#/Fe', s); await p.context().close();
  p = await open(); await p.goto(ELSEWHERE); await p.goto(B + '#/Fe'); await W(p, 3000);
  await p.goto(B + '#paper=lowdin'); await W(p, 1800); await p.goto(B + '#/Cu'); await W(p, 2500);
  await p.goBack(); await W(p, 1800); s = await st(p); ok('Back reopens the citation', s.open && LO.test(s.h1), s);
  await p.keyboard.press('Escape'); await W(p, 1200); s = await st(p); ok('Escape leaves the paper for #/Cu', !s.open && s.hash === '#/Cu', s);
  await p.click('#btn-papers'); await W(p, 1500); s = await st(p); ok('Papers reopens Löwdin, named', s.open && LO.test(s.h1) && s.hash === '#paper=lowdin', s);
  await p.goBack(); await W(p, 1800); s = off(p) || await st(p); ok('the first Back closes it at #/Cu (no dead press)', onSite(p) && !s.open && s.hash === '#/Cu' && /Cu$/.test(s.crumbs), s, { nav: true }); await p.context().close();
  p = await open(); await p.goto(ELSEWHERE); await p.goto(B + '#/Fe'); await W(p, 3000);
  await p.click('#btn-papers'); await W(p, 1500); await p.click('button[data-paper="lattice"]'); await W(p, 1200);
  await p.goBack(); await W(p, 1800); s = off(p) || await st(p); ok('a plain Read: Back closes the paper, on the site', onSite(p) && !s.open && s.hash === '#/Fe', s, { nav: true });
});

// ---- review: what the reviews of the routing found, kept found
for (const [vp, mobile] of [[PHONE, true], [DESK, false]]) scenario('review', `Back closes a paper without moving the explorer or the page at ${vp.width} px`, async ({ open, st, ok, W, onSite }) => {
  const p = await open(vp, mobile); await p.goto(ELSEWHERE); await p.goto(B + '#/'); await W(p, 3000);
  await p.evaluate(() => document.querySelector('#canvas').focus()); for (let i = 0; i < 3; i++) { await p.keyboard.press('+'); await W(p, 250); }
  const before = await st(p);
  await p.click('#btn-papers'); await W(p, 1500); await p.click('button[data-paper="lowdin"]'); await W(p, 1200);
  await p.goBack(); await W(p, 1800); const after = onSite(p) ? await st(p) : { url: p.url() };
  ok('the paper closes; camera and scroll unmoved', onSite(p) && !after.open && after.hash === '#/' && after.y === before.y && Array.isArray(before.cam) && JSON.stringify(after.cam) === JSON.stringify(before.cam), { before, after }, { nav: true });
  if (!onSite(p)) { ok('Forward reopens it', false, 'Back had left the site', { nav: true }); return; }
  await p.goForward(); await W(p, 1500); const fw = await st(p); ok('Forward reopens it', fw.open && LO.test(fw.h1), fw, { nav: true });
});
scenario('review', 'a paper over the explorer never steps back onto an older entry for itself', async ({ open, st, ok, W, onSite }) => {
  let p = await open(); await p.goto(ELSEWHERE); await p.goto(B + '#paper=lowdin'); await W(p, 3000); await p.goto(B + '#/Cu'); await W(p, 2500);
  await p.click('#btn-papers'); await W(p, 1500); let s = await st(p); ok('Papers reopens Löwdin over #/Cu', s.open && LO.test(s.h1) && s.hash === '#paper=lowdin', s);
  await p.goBack(); await W(p, 1800); s = onSite(p) ? await st(p) : { url: p.url() }; ok('Back closes it at #/Cu, on the site', onSite(p) && !s.open && s.hash === '#/Cu' && /Cu$/.test(s.crumbs), s, { nav: true }); await p.context().close();
  p = await open(); await p.goto(ELSEWHERE); await p.goto(B + '#/Fe'); await W(p, 3000);
  await p.goto(B + '#paper=bracket'); await W(p, 1800); await p.goto(B + '#paper=lowdin'); await W(p, 1800); await p.goto(B + '#/Cu'); await W(p, 2500);
  await p.click('#btn-papers'); await W(p, 1500); s = await st(p); ok('Papers reopens Löwdin', s.open && LO.test(s.h1), s);
  await p.goBack(); await W(p, 1800); s = onSite(p) ? await st(p) : { url: p.url() }; ok('Back closes Löwdin at #/Cu, Bracket not opened', onSite(p) && !s.open && s.hash === '#/Cu', s, { nav: true });
});
scenario('review', 'a selection landing late behind an open paper leaves its entry alone', async ({ open, st, ok, W, onSite }) => {
  let held = 0; const p = await open(); await p.route(/\/data\/elements\/92\.js(\?|$)/, async (r) => { held++; await new Promise((res) => setTimeout(res, 5000)); await r.fallback(); });
  await p.goto(ELSEWHERE); await p.goto(B + '#/U/III', { waitUntil: 'commit' }); await W(p, 1200);
  const early = await st(p); ok('the element load is held back past the Papers press', held > 0 && !early.crumbs.endsWith('III'), { held, crumbs: early.crumbs });
  await p.click('#btn-papers'); await W(p, 1500); await p.click('button[data-paper="lowdin"]'); await W(p, 6000);
  let s = await st(p); ok('after the late load: the paper open, its address kept', s.open && LO.test(s.h1) && s.hash === '#paper=lowdin', s);
  await p.goBack(); await W(p, 1800); s = onSite(p) ? await st(p) : { url: p.url() }; ok('Back closes it at the element asked for', onSite(p) && !s.open && /^#\/U/.test(s.hash) && /U/.test(s.crumbs), s, { nav: true });
});
scenario('review', 'a rotation keeps the reading position', async ({ open, ok, W }) => {
  const p = await open(PHONE, true); await p.goto(B + '#/Fe'); await W(p, 3000);
  await p.click('#btn-papers'); await W(p, 1500); await p.click('button[data-paper="lowdin"]'); await W(p, 1500);
  await p.evaluate(() => { document.querySelector('#papers-body').scrollTop = 6000; }); await W(p, 400);
  const top = () => p.evaluate(() => { const h = document.querySelector('#papers-body'), t = h.getBoundingClientRect().top; const el = [...document.querySelector('#paper-article').children].find((c) => c.getBoundingClientRect().bottom > t + 2); return el ? el.textContent.slice(0, 60) : null; });
  const t0 = await top(); await p.setViewportSize({ width: 844, height: 390 }); await W(p, 900); const t1 = await top();
  await p.setViewportSize(PHONE); await W(p, 900); const t2 = await top();
  ok('the block at the top survives a turn and a turn back', t0 && t0 === t1 && t1 === t2, { t0, t1, t2 });
});
scenario('review', 'a reload on a paper closes onto the element behind it', async ({ open, st, ok, W }) => {
  const p = await open(); await p.goto(ELSEWHERE); await p.goto(B + '#/Fe'); await W(p, 3000);
  await p.click('#btn-papers'); await W(p, 1500); await p.click('button[data-paper="lowdin"]'); await W(p, 1200);
  await p.reload(); await W(p, 3500); let s = await st(p); ok('after the reload: the paper open, the explorer at Fe behind it', s.open && LO.test(s.h1) && /Fe$/.test(s.crumbs), s, { nav: true });
  await p.keyboard.press('Escape'); await W(p, 1200); s = await st(p); ok('Escape returns to #/Fe', !s.open && s.hash === '#/Fe' && /Fe$/.test(s.crumbs), s, { nav: true });
  await p.goForward(); await W(p, 1500); s = await st(p); ok('Forward reopens the paper', s.open && LO.test(s.h1), s, { nav: true });
});
scenario('review', 'a citation followed from another page opens over the root', async ({ open, st, ok, W }) => {
  const p = await open(); await p.goto(ELSEWHERE); await p.goto(B + '#paper=tower'); await W(p, 3500); const s = await st(p);
  ok('Tower over the root', s.open && /Tower/.test(s.h1) && s.crumbs === 'Index', s);
});
scenario('review', 'an address changed during the first load opens no paper', async ({ open, st, ok, W }) => {
  const p = await open(); await p.goto(ELSEWHERE); await p.goto(B + '#/U/III'); await W(p, 3000);
  await p.click('#btn-papers'); await W(p, 1500); await p.click('button[data-paper="lowdin"]'); await W(p, 1200);
  // the reload restores the ion behind the paper and waits on its element file, held back here
  await p.route(/\/data\/elements\/92\.js(\?|$)/, async (r) => { await new Promise((res) => setTimeout(res, 4000)); await r.fallback(); });
  await p.reload({ waitUntil: 'domcontentloaded' }); await W(p, 1000);
  const pending = await p.evaluate(() => !document.querySelector('#dlg-papers').open);
  await p.evaluate(() => { location.hash = '#/Fe'; }); await W(p, 6000);
  const s = await st(p);
  ok('no paper; the address and the explorer are the reader\'s', pending && !s.open && s.hash === '#/Fe' && /Fe$/.test(s.crumbs), { pending, ...s }, { nav: true });
});
scenario('review', 'the explorer\'s own keys still act with no dialog open', async ({ open, ok, W }) => {
  const p = await open(); await p.goto(B + '#/Fe/II'); await W(p, 3500);
  const at = () => p.evaluate(() => ({ crumbs: [...document.querySelectorAll('#crumbs button')].map((x) => x.textContent).join(' › '), hash: location.hash }));
  await p.evaluate(() => document.querySelector('#canvas').focus());
  await p.keyboard.press('Escape'); await W(p, 900); let s = await at(); ok('Escape goes up to Fe', /Fe$/.test(s.crumbs) && s.hash === '#/Fe', s);
  await p.keyboard.press('h'); await W(p, 900); s = await at(); ok('h goes home', s.crumbs === 'Index' && s.hash === '#/', s);
  await p.keyboard.press('/'); await W(p, 300); ok('/ focuses the search', (await p.evaluate(() => document.activeElement.id)) === 'q', null);
});

// ---- solvers: the suite runs, and answers what a reader asks of it
const pickMode = (p, title) => p.evaluate((t) => { const s = document.querySelector('#solver-mode'), o = [...s.options].find((x) => x.textContent === t);
  if (!o) return false; s.value = o.value; s.dispatchEvent(new Event('change')); return true; }, title);
const solve = async (p, title, fills = {}) => {
  if (!(await pickMode(p, title))) return { rows: {}, msg: `no mode "${title}"` };
  for (const [k, v] of Object.entries(fills)) await p.fill(`#solver-mode-body [data-name="${k}"]`, v);
  await p.click('#solver-mode-body [data-sv="run"]');
  await p.waitForFunction(() => !/running …/.test(document.querySelector('[data-sv-out]').innerText), null, { timeout: 60000 });
  return p.evaluate(() => { const out = document.querySelector('[data-sv-out]'), rows = {};
    out.querySelectorAll('tbody tr').forEach((tr) => { const td = tr.querySelectorAll('td'); rows[td[0].textContent] = { value: td[1].textContent, status: td[2].textContent.trim(), note: td[3].textContent }; });
    return { rows, msg: (out.querySelector('.solver-msg') || {}).textContent || '', toGravity: !!out.querySelector('[data-solver="gravity"]') }; });
};
const selftestOf = async (p, title) => {
  if (!(await pickMode(p, title))) return null;
  await p.click('#solver-mode-body [data-sv="selftest"]');
  await p.waitForFunction(() => !/selftest running/.test(document.querySelector('[data-sv-test]').innerText), null, { timeout: 120000 });
  return p.evaluate(() => { const b = [...document.querySelectorAll('[data-sv-test] .selftest-summary b')].map((x) => +x.textContent);
    return { checked: b[0], failed: b[1], failures: [...document.querySelectorAll('[data-sv-test] tbody tr')].map((tr) => tr.textContent.slice(0, 160)) }; });
};
const MODES = ['The channel equation', 'The Pauli bound', 'The collapse coordinate C(Z, l)', 'Order closure, R', 'A Lambda_8 cell against its constraints',
  'The coefficient calculator', 'The relativistic limit (c = 137 against c → ∞)', 'Chemical equation check', 'Balance a chemical equation',
  'Relative gravity of a body', 'Build an atom, ion or molecule'];
for (const [what, from, to] of [['the record\'s own modes', 0, 7], ['the chemistry and gravity modes', 7, 11]]) scenario('solvers', `${what}: each selftest passes`, async ({ open, ok, W }) => {
  const p = await open(); await p.goto(B); await W(p, 3000);
  if (from === 0) { const n = await p.evaluate(() => [...document.querySelectorAll('#solver-mode option')].map((o) => o.textContent));
    ok('the suite loads every mode', JSON.stringify(n) === JSON.stringify(MODES), n); }
  for (const t of MODES.slice(from, to)) { const r = await selftestOf(p, t); ok(`${t}: selftest passes`, r && r.checked > 0 && r.failed === 0, r); }
});
scenario('solvers', 'what a reader asks the builder and the gravity mode, on a phone', async ({ open, ok, W }) => {
  const p = await open(PHONE, true); await p.goto(B); await W(p, 3000);
  const B1 = 'Build an atom, ion or molecule', G1 = 'Relative gravity of a body';
  let r = await solve(p, B1, { formula: 'water' });
  ok('water: the molar mass 18.015 g/mol and the most abundant isotopologue, A = 18', /^18\.015 g\/mol/.test((r.rows['molar mass (standard atomic weights)'] || {}).value || '') && (r.rows['nucleons A, neutrons N'] || {}).value === '18, 8' && /^18\.010565 u/.test((r.rows['mass M (the most abundant isotopologue)'] || {}).value || ''), r.rows);
  r = await solve(p, B1, { formula: 'glucose' });
  ok('glucose: 180.156 g/mol', /^180\.156 g\/mol/.test((r.rows['molar mass (standard atomic weights)'] || {}).value || ''), r.rows['molar mass (standard atomic weights)']);
  r = await solve(p, B1, { formula: 'electron' });
  ok('electron: a particle, sent to the gravity mode', /particle e-/.test(r.msg) && r.toGravity, r);
  r = await solve(p, G1, { species: 'Fe', two_j: '', level: '', reference: '^1H' });
  ok('Fe: χ from the ground term, the bound decided at D = 4, the χ ratio against ¹H', /^\d\.\d+e[+-]\d+/.test((r.rows['χ, the Kerr spin'] || {}).value || '') && (r.rows['horizon bound at D = 4'] || {}).value === '1 · a bound' && /^\d/.test((r.rows['χ / χ_ref'] || {}).value || ''), r.rows);
  r = await solve(p, G1, { species: '^12C' });
  ok('¹²C: exactly 12 u at the ground, J from the ground term, not the banked excited level', /^12\.000000 u/.test((r.rows['mass M'] || {}).value || '') && /ground term 3P0/.test((r.rows['2J'] || {}).note || ''), r.rows);
  r = await solve(p, G1, { species: 'proton' });
  ok('proton: read as the baryon p', /^p \(a member of the baryons index\)/.test((r.rows.body || {}).value || ''), r.rows.body || r.msg);
  r = await solve(p, G1, { species: 'photon' });
  ok('photon: massless, χ not defined', (r.rows['mass M'] || {}).value === '0 (massless)' && (r.rows['χ, the Kerr spin'] || {}).value === 'not defined', r.rows);
  r = await solve(p, G1, { species: 'pion' });
  ok('pion: three particles listed, none chosen', /names 3 particles: pi\+, pi0, pi-/.test(r.msg), r.msg);
});
scenario('solvers', 'the search box reads a particle by its name', async ({ open, ok, W }) => {
  const p = await open(); await p.goto(B); await W(p, 3000);
  await p.fill('#q', 'proto'); await p.type('#q', 'n', { delay: 30 }); await W(p, 2500);
  await p.type('#q', ' '); await p.keyboard.press('Backspace'); await W(p, 600);   // again, the indexes now loaded
  const sug = await p.$$eval('#suggest li', (ls) => ls.map((l) => l.textContent));
  ok('proton: its plate and its gravity are offered', sug.some((s) => /proton → p.*baryons · its plate/i.test(s)) && sug.some((s) => /proton → p.*relative gravity/.test(s)), sug);
  const i = sug.findIndex((s) => /relative gravity/.test(s));
  if (i >= 0) await p.dispatchEvent(`#suggest li:nth-child(${i + 1})`, 'mousedown');
  await W(p, 1200);
  const m = await p.evaluate(() => ({ mode: document.querySelector('#solver-mode').selectedOptions[0].textContent, body: (document.querySelector('#solver-mode-body [data-name="species"]') || {}).value }));
  ok('...and the gravity suggestion opens the mode on it', m.mode === 'Relative gravity of a body' && m.body === 'proton', m);
});

// ---- caveats: the list as reviewed on 2026-10-17, and each repair where a reader meets it
const plate = (p) => p.evaluate(() => document.querySelector('#inspector-body').textContent.replace(/\s+/g, ' '));
scenario('caveats', 'the caveats carry their state, and each repair shows on its plate', async ({ open, ok, W }) => {
  const p = await open(); await p.goto(B + '#/'); await W(p, 3000);
  const cv = await p.evaluate(() => [...document.querySelectorAll('#inspector-body .cv-list li')].map((li) => ({ state: (li.querySelector('.cv-state') || {}).textContent || null, was: !!li.querySelector('.cv-was'), text: li.textContent })));
  ok('eleven caveats, each with a state; every repaired one says what it read before', cv.length === 11 && cv.every((c) => c.state) && cv.filter((c) => /^Repaired/.test(c.state)).every((c) => c.was), cv.map((c) => [c.state, c.was]));
  ok('the table stops where NIST\'s neutral ground levels stop, not "because measurement does"', cv.some((c) => /NIST's compilation of neutral ground levels/.test(c.text)) && !cv.some((c) => /because measurement does/.test(c.text.replace(/Before the review it read:.*$/, ''))), cv[0] && cv[0].text);
  await p.goto(B + '#/Na/I/s/2'); await W(p, 3000); let t = await plate(p);
  ok('Na I s: the csv\'s B is the range of the series\' defects, not a bound', /range of the series’ quantum defects, not a bound/.test(t) && /0\.02475/.test(t), t.slice(0, 600));
  ok('Na I s: the series limit carries its unit, cm⁻¹', /41449\.451 cm⁻¹/.test(t) && /cm⁻¹, the neutral ionisation energy/.test(t), t.match(/series limit.{0,120}/));
  ok('Na I s: inside the equation\'s domain', /equation domain\s*validated/.test(t), t.match(/equation domain.{0,60}/));
  await p.goto(B + '#/Fe/IV/s'); await W(p, 3000); t = await plate(p);
  ok('Fe IV s: outside the domain, with the reason', /equation domain\s*extrapolated — open-shell core at 16 parents/.test(t), t.match(/equation domain.{0,80}/));
  await p.goto(B + '#/Rf'); await W(p, 3500); t = await plate(p);
  ok('Rf: the ground level is NIST\'s lone level, its ionisation energy ab initio', /NIST holds the ground level of Rf I and no excited level/.test(t) && /ab initio/.test(t), t.match(/what it rests on.{0,160}/));
  await p.goto(B + '#/Uue/XI/s'); await W(p, 3500); t = await plate(p);
  ok('Z = 119: the csv\'s B is named a bare 0, not a bound', /0, not a bound/.test(t), t.slice(0, 500));
  await p.goto(B + '#/Fe/I/s'); await W(p, 3000); t = await plate(p);
  ok('Fe I s: n₀ is RECOVERED', /n₀\s*\d+\s*RECOVERED/.test(t), t.match(/n₀.{0,40}/));
  await p.goto(B + '#/Fe'); await W(p, 3500); t = await plate(p);
  ok('Fe: its Λ cells as the record builds them, 14, five composable within iron; the ladder labelled a reconstruction', /Λ cells, as the record builds them/.test(t) && /cells\s*14\s*RECOVERED/.test(t) && /composable within the element\s*5 of 14/.test(t) && /The ionisation ladder, a reconstruction/.test(t), t.match(/Λ cells, as the record.{0,300}/));
  await p.goto(B + '#/H'); await W(p, 3500); t = await plate(p);
  ok('H: one subshell listed, so no Λ cell', /One subshell is listed[^.]*: the element has no cell/.test(t), t.match(/Λ cells, as the record.{0,300}/));
});

// ---------------------------------------------------------------- suites
const KNOWN = [...new Set(SCENARIOS.map((x) => x.suite))];
if (SUITES.has('all')) SUITES = new Set(KNOWN);
{ const bad = [...SUITES].filter((x) => !KNOWN.includes(x)); if (bad.length) die(`unknown --suite ${bad.join(',')}; the suites are ${KNOWN.join(', ')}`); }

// ---------------------------------------------------------------- listing
if (LIST) {
  for (const sc of SCENARIOS) if (SUITES.has(sc.suite)) console.log(`${sc.suite.padEnd(8)} ${sc.name}`);
  process.exit(0);
}

// ---------------------------------------------------------------- the files the site is served from
let ROOT = null, tmp = null;
const md5 = (b) => createHash('md5').update(b).digest('hex');
if (TARGET === 'worktree') ROOT = path.resolve(opt('--root', path.join(REPO, 'public')));
if (TARGET === 'worktree' && !existsSync(path.join(ROOT, 'index.html'))) { console.error(`no index.html in ${ROOT}`); process.exit(2); }
if (TARGET === 'commit') {
  let sha;
  try { sha = execFileSync('git', ['rev-parse', REV], { cwd: REPO }).toString().trim(); } catch (e) { console.error(`cannot resolve ${REV}`); process.exit(2); }
  tmp = mkdtempSync(path.join(tmpdir(), 'sitecheck-'));
  process.on('exit', () => { if (tmp) rmSync(tmp, { recursive: true, force: true }); });   // every exit path, a throw included
  try { execFileSync('sh', ['-c', `git archive ${sha} public | tar -x -C "${tmp}"`], { cwd: REPO, stdio: ['ignore', 'ignore', 'pipe'] }); }
  catch (e) { die(`cannot extract public/ from ${REV} (${sha.slice(0, 12)}): ${String(e.stderr || e.message).split('\n')[0]}`); }
  ROOT = path.join(tmp, 'public');
  if (!existsSync(path.join(ROOT, 'index.html'))) die(`no public/index.html in ${REV}`);
  console.log(`serving public/ of ${sha.slice(0, 12)} (${REV}) at ${SITE}`);
  // each key file against the copy GitHub serves for that commit (curl honours the session's proxy)
  let differs = 0, unreached = 0;
  for (const f of KEY_FILES) {
    const lp = path.join(ROOT, f);
    if (!existsSync(lp)) { console.log(`  ${f.padEnd(62)} not in this commit`); continue; }
    const local = md5(readFileSync(lp));
    const got = spawnSync('curl', ['-sSf', '-m', '90', RAW + sha + '/public/' + f], { maxBuffer: 64 << 20 });
    const remote = got.status === 0 ? md5(got.stdout) : null;
    if (!remote) unreached++; else if (remote !== local) differs++;
    console.log(`  ${f.padEnd(62)} ${local}  ${remote === null ? 'GitHub unreachable' : remote === local ? 'same as GitHub serves' : 'DIFFERS from GitHub: ' + remote}`);
  }
  if (differs) die('the commit\'s files differ from the copy GitHub serves; stopping');
  if (unreached) console.log('  (GitHub could not be reached for some files; served from the commit as held here)');
}
if (TARGET === 'worktree') console.log(`serving ${path.relative(REPO, ROOT) || ROOT} at ${SITE}`);
if (TARGET === 'live') console.log(`loading ${SITE} from the network`);
if (NONAV) console.log('the Navigation API removed: checks that need it are n/a');

// ---------------------------------------------------------------- the browser
const PW = process.env.PLAYWRIGHT_MODULE || '/opt/node22/lib/node_modules/playwright/index.mjs';
let chromium;
try { ({ chromium } = await import(existsSync(PW) ? PW : 'playwright')); } catch (e) { console.error('Playwright not found: set PLAYWRIGHT_MODULE to its index.mjs'); process.exit(2); }
const EXE = process.env.CHROMIUM || (existsSync('/opt/pw-browsers/chromium') ? '/opt/pw-browsers/chromium' : undefined);
// the session's proxy re-signs TLS with its own CA, which curl and Node are given: Chromium is told to
// trust the same keys (and nothing else is relaxed), so the live target can load where the proxy allows
const CA = process.env.SSL_CERT_FILE || process.env.NODE_EXTRA_CA_CERTS || '/root/.ccr/ca-bundle.crt';
let spki = [];
try { spki = existsSync(CA) ? [...new Set((readFileSync(CA, 'utf8').match(/-----BEGIN CERTIFICATE-----[\s\S]+?-----END CERTIFICATE-----/g) || [])
  .map((pem) => createHash('sha256').update(new X509Certificate(pem).publicKey.export({ type: 'spki', format: 'der' })).digest('base64')))] : []; } catch (e) { spki = []; }
let browser;
try { browser = await chromium.launch({ executablePath: EXE, headless: true, args: spki.length ? ['--ignore-certificate-errors-spki-list=' + spki.join(',')] : [] }); }
catch (e) { die(`Chromium could not be launched: ${e.message.split('\n')[0]} (set CHROMIUM to its executable)`); }

async function route(r) {
  try { return await serve(r); } catch (e) { return r.fulfill({ status: 500, body: String(e) }).catch(() => {}); }
}
async function serve(r) {
  const url = r.request().url();
  if (url.startsWith(ELSEWHERE)) return r.fulfill({ status: 200, body: '<!doctype html><title>elsewhere</title><p>a page before the site</p>', headers: { 'content-type': 'text/html' } });
  if (TARGET === 'live') return r.fallback();
  if (url.startsWith(SITE)) {
    let rel;
    try { rel = decodeURIComponent(new URL(url).pathname.slice('/Claude-Method-Works/'.length)) || 'index.html'; }
    catch (e) { return r.fulfill({ status: 400, body: 'bad path', headers: { 'content-type': 'text/plain' } }); }
    if (rel.endsWith('/')) rel += 'index.html';
    const file = path.join(ROOT, rel);
    if (!file.startsWith(ROOT + path.sep)) return r.fulfill({ status: 403, body: 'outside the site' });
    try { return r.fulfill({ status: 200, body: await readFile(file), headers: { 'content-type': TYPES[path.extname(rel)] || 'application/octet-stream' } }); }
    catch (e) { return r.fulfill({ status: 404, body: 'not found', headers: { 'content-type': 'text/plain' } }); }
  }
  return r.abort();   // fonts and other hosts: the site does not depend on them
}

// a live target that the network does not reach stops here, with what to do about it
if (TARGET === 'live') {
  const ctx = await browser.newContext(); const p = await ctx.newPage();
  const resp = await p.goto(SITE, { timeout: 30000 }).catch((e) => e);
  await ctx.close();
  if (!resp || resp instanceof Error || !resp.ok()) {
    const why = resp instanceof Error ? resp.message.split('\n')[0] : `HTTP ${resp && resp.status()}`;
    console.error(`${SITE} did not load from here: ${why}.`);
    if (/ERR_TUNNEL_CONNECTION_FAILED|HTTP 40[37]/.test(why)) console.error('The session\'s proxy refused the host: allow lach-matt.github.io in the environment\'s network access, or use --target commit to serve the deployed commit\'s own files.');
    else if (/ERR_CERT_/.test(why)) console.error(`The browser does not trust the certificate it was given: a trust-store problem, not the allowlist (the CA bundle read was ${CA}).`);
    await browser.close(); process.exit(2);
  }
}

// ---------------------------------------------------------------- the run
const results = [], pageErrors = [];
const W = (p, ms) => p.waitForTimeout(ms);
const st = (p) => p.evaluate(() => ({ open: document.querySelector('#dlg-papers').open, h1: (document.querySelector('#paper-article h1') || {}).textContent || null,
  note: [...document.querySelectorAll('#papers-body .note')].map((n) => n.textContent).join(' | '), cards: document.querySelectorAll('#papers-body .paper-card').length,
  crumbs: [...document.querySelectorAll('#crumbs button')].map((x) => x.textContent).join(' › '), hash: location.hash,
  active: document.activeElement && (document.activeElement.id || document.activeElement.tagName), scroll: document.querySelector('#papers-body').scrollTop,
  y: Math.round(scrollY), cam: (() => { if (!window.__mi_state) return 'no window.__mi_state'; const c = window.__mi_state.cam; return c ? [+c.k.toFixed(3), Math.round(c.tx), Math.round(c.ty)] : null; })() }));
const onSite = (p) => p.url().startsWith(SITE);
const SCENARIO_MS = 180000;   // the longest scenario takes well under a minute
for (const sc of SCENARIOS) {
  if (!SUITES.has(sc.suite)) continue;
  const contexts = [];
  const open = async (vp = DESK, mobile = false) => {
    const ctx = await browser.newContext({ viewport: vp, isMobile: mobile, hasTouch: mobile }); contexts.push(ctx);
    await ctx.route('**/*', route);
    if (NONAV) await ctx.addInitScript(() => { try { Object.defineProperty(window, 'navigation', { value: undefined, configurable: true }); } catch (e) { /* not definable */ } });
    ctx.setDefaultTimeout(30000);
    const p = await ctx.newPage(); p.on('pageerror', (e) => pageErrors.push(`${sc.name}: ${e.message}`));
    // the page reports a caught failure (a draw, the boot, an element load) on the console only; a
    // refused request to another host (the fonts route() turns away) is not the site's and is left out
    p.on('console', (m) => { if (m.type() !== 'error') return; const at = (m.location() || {}).url || '';
      if (/^Failed to load resource/.test(m.text()) && at && !at.startsWith(SITE)) return;
      pageErrors.push(`${sc.name}: console: ${m.text().split('\n')[0]}`); });
    return p;
  };
  let done = false, timer;
  const ok = (name, cond, got, o = {}) => { if (!done) results.push({ suite: sc.suite, scenario: sc.name, name, status: o.nav && NONAV ? 'n/a' : cond ? 'PASS' : 'FAIL', got: cond ? '' : String(JSON.stringify(got === undefined ? null : got)) }); };
  const deadline = new Promise((_, rej) => { timer = setTimeout(() => rej(new Error(`did not finish in ${SCENARIO_MS / 1000} s (the page stopped responding?)`)), SCENARIO_MS); });
  try { await Promise.race([sc.fn({ open, st, ok, W, onSite }), deadline]); }
  catch (e) { results.push({ suite: sc.suite, scenario: sc.name, name: 'ran to the end', status: 'FAIL', got: e.message.split('\n')[0] }); }
  finally { done = true; clearTimeout(timer); for (const c of contexts) await c.close().catch(() => {}); }
  const mine = results.filter((r) => r.scenario === sc.name);
  console.log(`\n${sc.suite} · ${sc.name}`);
  for (const r of mine) console.log(`  ${r.status.padEnd(4)}  ${r.name}${r.status === 'FAIL' ? '\n        got ' + r.got.slice(0, 600) : ''}`);
}
await browser.close();
const n = (s) => results.filter((r) => r.status === s).length;
if (!results.length) die('no checks ran');
console.log(`\n${n('PASS')} passed, ${n('FAIL')} failed${n('n/a') ? `, ${n('n/a')} n/a without the Navigation API` : ''}; page errors: ${pageErrors.length ? pageErrors.join(' | ') : 'none'}`);
process.exit(n('FAIL') || pageErrors.length ? 1 : 0);
