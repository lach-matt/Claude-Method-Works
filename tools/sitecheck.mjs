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
import { createHash } from 'node:crypto';
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
const targetArg = opt('--target', 'worktree');
const [TARGET, REV] = targetArg.startsWith('commit') ? ['commit', targetArg.split('=')[1] || 'origin/main'] : [targetArg, null];
const SUITES = new Set((opt('--suite', 'all') === 'all' ? 'papers,routing,review' : opt('--suite', 'all')).split(','));
const NONAV = flag('--nonav'), LIST = flag('--list');
if (!['worktree', 'commit', 'live'].includes(TARGET)) { console.error(`unknown --target ${targetArg}`); process.exit(2); }

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
});
scenario('papers', 'what the renderer must get right in the papers', async ({ open, ok, W }) => {
  const p = await open(DESK); await p.goto(B + '#paper=everything-is-relative'); await W(p, 3000);
  const r = await p.evaluate(() => {
    const a = document.querySelector('#paper-article');
    const p1 = [...a.querySelectorAll('li')].find((li) => li.textContent.startsWith('P1.'));
    return { pipes: [...a.querySelectorAll('td')].map((td) => td.textContent).filter((t) => /16\|α\|m|8\|Hḟ\||\|ξ\|²/.test(t)).length,
      escapes: (a.textContent.match(/\\[_|[\]*]/g) || []).length,
      jhep: [...a.querySelectorAll('a[href*="JHEP"]')].map((x) => x.getAttribute('href')),
      grqc: [...a.querySelectorAll('a[href="https://arxiv.org/abs/gr-qc/0411023"]')].length,
      p1: p1 && /no other scale\.$/.test(p1.textContent.trim()), p1list: p1 && p1.parentElement.children.length };
  });
  ok('escaped pipes are literal pipes in their table cells', r.pipes === 3, r.pipes);
  ok('no backslash escape survives the render', r.escapes === 0, r.escapes);
  ok('a DOI with a balanced parenthesised group links whole', JSON.stringify(r.jhep.sort()) === JSON.stringify(['https://doi.org/10.1007/JHEP02(2016)020', 'https://doi.org/10.1007/JHEP08(2022)157']), r.jhep);
  ok('an old-style arXiv id with a version suffix is linked', r.grqc >= 1, r.grqc);
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
  ok('the paper closes; camera and scroll unmoved', onSite(p) && !after.open && after.hash === '#/' && after.y === before.y && JSON.stringify(after.cam) === JSON.stringify(before.cam), { before, after }, { nav: true });
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
  const p = await open(); await p.route(B + 'data/elements/92.js', async (r) => { await new Promise((res) => setTimeout(res, 5000)); await r.fallback(); });
  await p.goto(ELSEWHERE); await p.goto(B + '#/U/III'); await W(p, 1200);
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
scenario('review', 'an address changed during the first load opens no paper', async ({ open, ok, W }) => {
  const p = await open(); await p.addInitScript(() => { document.addEventListener('DOMContentLoaded', () => setTimeout(() => { location.hash = '#/Fe'; }, 0)); });
  await p.goto(B + '#paper=lowdin'); await W(p, 4000);
  const r = await p.evaluate(() => ({ hash: location.hash, open: document.querySelector('#dlg-papers').open, crumbs: [...document.querySelectorAll('#crumbs button')].map((x) => x.textContent).join(' › ') }));
  ok('no paper; the explorer at Fe', r.hash === '#/Fe' && !r.open && /Fe$/.test(r.crumbs), r);
});
scenario('review', 'the explorer\'s own keys still act with no dialog open', async ({ open, ok, W }) => {
  const p = await open(); await p.goto(B + '#/Fe/II'); await W(p, 3500);
  const crumbs = () => p.evaluate(() => [...document.querySelectorAll('#crumbs button')].map((x) => x.textContent).join(' › '));
  await p.evaluate(() => document.querySelector('#canvas').focus());
  await p.keyboard.press('Escape'); await W(p, 900); ok('Escape goes up to Fe', /Fe$/.test(await crumbs()), await crumbs());
  await p.keyboard.press('h'); await W(p, 900); ok('h goes home', (await crumbs()) === 'Index', await crumbs());
  await p.keyboard.press('/'); await W(p, 300); ok('/ focuses the search', (await p.evaluate(() => document.activeElement.id)) === 'q', null);
});

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
  execFileSync('sh', ['-c', `git archive ${sha} public | tar -x -C "${tmp}"`], { cwd: REPO });
  ROOT = path.join(tmp, 'public');
  console.log(`serving public/ of ${sha.slice(0, 12)} (${REV}) at ${SITE}`);
  // each key file against the copy GitHub serves for that commit (curl honours the session's proxy)
  let differs = 0, unreached = 0;
  for (const f of KEY_FILES) {
    const local = md5(readFileSync(path.join(ROOT, f)));
    const got = spawnSync('curl', ['-sSf', '-m', '90', RAW + sha + '/public/' + f], { maxBuffer: 64 << 20 });
    const remote = got.status === 0 ? md5(got.stdout) : null;
    if (!remote) unreached++; else if (remote !== local) differs++;
    console.log(`  ${f.padEnd(62)} ${local}  ${remote === null ? 'GitHub unreachable' : remote === local ? 'same as GitHub serves' : 'DIFFERS from GitHub: ' + remote}`);
  }
  if (differs) { console.error('the commit\'s files differ from the copy GitHub serves; stopping'); process.exit(2); }
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
const browser = await chromium.launch({ executablePath: EXE, headless: true });

async function route(r) {
  const url = r.request().url();
  if (url.startsWith(ELSEWHERE)) return r.fulfill({ status: 200, body: '<!doctype html><title>elsewhere</title><p>a page before the site</p>', headers: { 'content-type': 'text/html' } });
  if (TARGET === 'live') return r.fallback();
  if (url.startsWith(SITE)) {
    let rel = decodeURIComponent(new URL(url).pathname.slice('/Claude-Method-Works/'.length)) || 'index.html';
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
    console.error(`${SITE} is not reachable from here (${resp instanceof Error ? resp.message.split('\n')[0] : resp && resp.status()}).`);
    console.error('Allow lach-matt.github.io in the environment\'s network access, or use --target commit to serve the deployed commit\'s own files.');
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
  y: Math.round(scrollY), cam: (() => { const c = window.__mi_state && window.__mi_state.cam; return c ? [+c.k.toFixed(3), Math.round(c.tx), Math.round(c.ty)] : null; })() }));
const onSite = (p) => p.url().startsWith(SITE);
for (const sc of SCENARIOS) {
  if (!SUITES.has(sc.suite)) continue;
  const contexts = [];
  const open = async (vp = DESK, mobile = false) => {
    const ctx = await browser.newContext({ viewport: vp, isMobile: mobile, hasTouch: mobile }); contexts.push(ctx);
    await ctx.route('**/*', route);
    if (NONAV) await ctx.addInitScript(() => { try { Object.defineProperty(window, 'navigation', { value: undefined, configurable: true }); } catch (e) { /* not definable */ } });
    const p = await ctx.newPage(); p.on('pageerror', (e) => pageErrors.push(`${sc.name}: ${e.message}`)); return p;
  };
  const ok = (name, cond, got, o = {}) => results.push({ suite: sc.suite, scenario: sc.name, name, status: o.nav && NONAV ? 'n/a' : cond ? 'PASS' : 'FAIL', got: cond ? '' : JSON.stringify(got) });
  try { await sc.fn({ open, st, ok, W, onSite }); }
  catch (e) { results.push({ suite: sc.suite, scenario: sc.name, name: 'ran to the end', status: 'FAIL', got: e.message.split('\n')[0] }); }
  finally { for (const c of contexts) await c.close().catch(() => {}); }
  const mine = results.filter((r) => r.scenario === sc.name);
  console.log(`\n${sc.suite} · ${sc.name}`);
  for (const r of mine) console.log(`  ${r.status.padEnd(4)}  ${r.name}${r.status === 'FAIL' ? '\n        got ' + r.got.slice(0, 600) : ''}`);
}
await browser.close();
if (tmp) rmSync(tmp, { recursive: true, force: true });
const n = (s) => results.filter((r) => r.status === s).length;
console.log(`\n${n('PASS')} passed, ${n('FAIL')} failed${n('n/a') ? `, ${n('n/a')} n/a without the Navigation API` : ''}; page errors: ${pageErrors.length ? pageErrors.join(' | ') : 'none'}`);
process.exit(n('FAIL') || pageErrors.length ? 1 : 0);
