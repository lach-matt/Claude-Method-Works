/* The Method Index — a zoomable reading of the index.
 *
 * The explorer computes nothing. Every number it shows is tools/populate.py's,
 * written by tools/webindex.py into data/, and the page draws it with the
 * status the data gives it. A status is never flattened. The solver suite
 * (window.MI.solvers, a module appended to the end of this file) does compute,
 * and every solver carries a selftest against the instrument's own numbers.
 *
 * Data protocol: data/index.js sets window.__mi.index before this script runs;
 * data/elements/<Z>.js sets window.__mi.el[Z] and is injected on demand, so the
 * page opens from a plain file:// URL where fetch() of a local file is blocked.
 */
(() => {
  'use strict';

  const $ = (s) => document.querySelector(s);
  const canvas = $('#canvas');
  const ctx = canvas.getContext('2d');
  const wrap = $('#canvas-wrap');
  const CELL = 100;                 // world units per table cell
  const EL_R = 44;                  // radius of the circle inside a cell
  const DATA = 'data/';
  // a query string tied to the edition, so a browser that cached an older element or papers file fetches the one this index was built with
  const dataVersion = () => (state.index && state.index.meta && state.index.meta.commit && location.protocol !== 'file:' ? `?v=${state.index.meta.commit}` : '');

  const state = {
    index: null,
    layout: 'table',
    frames: new Map(),              // Z -> {x, y, cx, cy}
    ghosts: [],                     // {p, g, x, y, def}
    heliumAt: 18,                   // 18 (the drawn layout, IUPAC) or 2 (the priced alternative)
    bounds: { x0: 0, y0: 0, x1: 1, y1: 1 },
    elements: new Map(),            // Z -> record
    trees: new Map(),               // Z -> {ions: [...]} with relative frames
    pending: new Map(),
    papers: null,                   // data/papers.js, loaded on demand             // Z -> promise
    loadErrors: new Map(),          // Z -> message
    selected: null,                 // node
    hover: null, hoverKey: '',      // the node under a mouse pointer on the plane
    cam: { k: 1, tx: 0, ty: 0 },
    anim: null,
    view: 'plane',                  // 'plane' (the zoomable layout) or 'lattice' (three dimensions)
    elementView: 'lattice',         // how an element opens: its slab of the lattice, or the nested circles
    orbit: null,                    // {rx, ry, zoom} of the lattice camera
    scene: null,                    // the lattice scene drawn: kind 'element' (Z) or 'index'
    colors: {},
    lastHash: '',
  };

  // ---------------------------------------------------------------- helpers
  const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  // fmtVal's rule (the solver renderer): exponent form below 1e-3, so a residual of 6e-7 never prints as 0.0000
  const fmt = (v, nd = 4) => (v === null || v === undefined) ? '—' : (typeof v === 'number' && !Number.isInteger(v) ? (Math.abs(v) < 1e-3 ? v.toExponential(4) : v.toFixed(nd)) : String(v));
  // a READ figure is printed with the digits its source carries (COORDINATES-2.13 holds δ at 5 dp), never rounded
  const fmtRead = (v) => (v === null || v === undefined) ? '—' : String(v);
  // populate.LSYM: ℓ = 6, 7 are labelled by number, as the record's subshell_letter is
  const LSYM = 'spdfgh';
  // an ℓ token of a hash or search path: one letter of LSYM, else a number; never a substring match
  const parseL = (tok) => { const t = String(tok).toLowerCase(); if (t.length === 1 && LSYM.indexOf(t) >= 0) return LSYM.indexOf(t); return /^\d+$/.test(t) ? parseInt(t, 10) : NaN; };
  const reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const isPhone = () => window.innerWidth < 900;

  function roman(n) {
    const t = [[100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'], [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']];
    let s = '';
    for (const [v, r] of t) while (n >= v) { s += r; n -= v; }
    return s;
  }
  function fromRoman(s) {
    const m = { I: 1, V: 5, X: 10, L: 50, C: 100 };
    if (!/^[IVXLC]+$/.test(s)) return null;
    let n = 0;
    for (let i = 0; i < s.length; i++) {
      const a = m[s[i]], b = m[s[i + 1]] || 0;
      n += a < b ? -a : a;
    }
    return n;
  }
  function readColors() {
    const cs = getComputedStyle(document.documentElement);
    const g = (n) => cs.getPropertyValue(n).trim();
    state.fonts = { mono: g('--font-mono') || 'ui-monospace, monospace', sans: g('--font-body') || 'sans-serif', serif: g('--font-display') || 'serif' };
    state.colors = {
      bg: g('--canvas-bg'), grid: g('--canvas-grid'), text: g('--canvas-text'), muted: g('--canvas-text-muted'),
      surface: g('--surface'), line: g('--line'), lineStrong: g('--line-strong'), accent: g('--accent'), glow: g('--accent-glow') || g('--accent'),
      measured: g('--measured'), exact: g('--exact'), computed: g('--computed'), ghost: g('--ghost'), csv: g('--csv'),
      ink: g('--ink'),
      blk: { s: g('--blk-s'), p: g('--blk-p'), d: g('--blk-d'), f: g('--blk-f'), none: g('--blk-none') },
      rel: g('--rel') || g('--accent'),
      faint: g('--faint') || g('--canvas-text-muted'),
      walk: g('--walk') || g('--rel') || g('--accent'),
      lim: Object.fromEntries(LIMIT_KIND_ORDER.map((k) => [k, g('--lim-' + k) || g('--computed')])),
    };
  }

  // canvas type: mono for numerals and identifiers, sans for labels, serif for symbols
  const F = (px, role = 'mono', weight = '') => `${weight ? weight + ' ' : ''}${px}px ${(state.fonts || {})[role] || 'monospace'}`;

  // a cell of the index: inset from its frame so the gutters draw the grid, with soft corners
  function cellRect(p, s) {
    const g = Math.max(1, s * 0.045), r = Math.max(1.5, s * 0.075);
    return { x: p.x + g, y: p.y + g, w: s - 2 * g, h: s - 2 * g, r };
  }
  function roundRectPath(x, y, w, h, r) {
    r = Math.min(r, w / 2, h / 2);
    ctx.beginPath();
    ctx.moveTo(x + r, y);
    ctx.arcTo(x + w, y, x + w, y + h, r);
    ctx.arcTo(x + w, y + h, x, y + h, r);
    ctx.arcTo(x, y + h, x, y, r);
    ctx.arcTo(x, y, x + w, y, r);
    ctx.closePath();
  }

  // ---------------------------------------------------------------- the limits facet
  // A bound note in COORDINATES-2.13 is READ; its kind is DERIVED by the rules data/index.js
  // carries (index.limits.rules), applied here exactly as tools/webindex.py applied them.
  const LIMIT_KIND_ORDER = ['ionisation-limit', 'unresolved', 'nuclear', 'term', 'coupling', 'no-analysis', 'symmetry', 'none'];
  const LIMIT_LABEL = {
    'ionisation-limit': 'series limit printed', unresolved: 'series unresolved', nuclear: 'nuclear: no isotope or nuclide',
    term: 'not keyable (no single 2S+1)', coupling: 'open-shell core', 'no-analysis': 'no analysis located (not a bound)',
    symmetry: 'δ = 0 by symmetry', none: 'no note',
  };
  const limitCache = new Map();
  function limitKind(note) {
    if (limitCache.has(note)) return limitCache.get(note);
    const rules = (state.index && state.index.limits && state.index.limits.rules) || [];
    let kind = null;
    for (const r of rules) { if (new RegExp(r.regex).test(note)) { kind = r.kind; break; } }
    limitCache.set(note, kind);
    return kind;
  }
  function limitRule(kind) {
    const rules = (state.index && state.index.limits && state.index.limits.rules) || [];
    return rules.find((r) => r.kind === kind) || null;
  }
  function setCellColor(mode) {
    state.cellColor = mode === 'limit' ? 'limit' : 'grade';
    const legend = $('#legend');
    if (legend) {
      legend.dataset.color = state.cellColor;
      legend.querySelectorAll('.legend-seg button').forEach((b) => b.classList.toggle('is-on', b.dataset.color === state.cellColor));
    }
    requestDraw();
  }

  // ---------------------------------------------------------------- layout
  function buildFrames() {
    const L = state.index.layout;
    state.frames.clear();
    state.ghosts = [];
    let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
    const put = (Z, col, row) => {
      const x = col * CELL, y = row * CELL;
      state.frames.set(Z, { x, y, cx: x + CELL / 2, cy: y + CELL / 2 });
      x0 = Math.min(x0, x); y0 = Math.min(y0, y); x1 = Math.max(x1, x + CELL); y1 = Math.max(y1, y + CELL);
    };
    if (state.layout !== 'janet') {
      const c = state.index.closure;
      const he2 = state.heliumAt === 2 && c.placement && c.placement.helium_at_2;
      for (const e of L) {
        if (e.set_aside) {
          const lan = e.Z <= 71;
          put(e.Z, (lan ? e.Z - 58 : e.Z - 90) + 3, lan ? 8.5 : 9.5);
        } else if (he2 && e.Z === 2) {
          put(e.Z, 1, 0);                 // helium drawn at group 2 (the priced alternative)
        } else {
          put(e.Z, e.group - 1, e.period - 1);
        }
      }
      // the cells R admits and the layout does not hold, each with its stated definition
      const defs = new Map((c.denied_cells || []).map((d) => [`${d.p},${d.g}`, d]));
      const denied = state.layout === 'table' || state.layout === 'table3d' ? (he2 ? c.placement.helium_at_2.denied : c.denied) : [];
      for (const [p, g] of denied) {
        state.ghosts.push({ p, g, x: (g - 1) * CELL, y: (p - 1) * CELL, def: defs.get(`${p},${g}`) || null });
      }
    } else {
      const off = { 3: 0, 2: 14, 1: 24, 0: 30 };
      const groups = new Map();
      for (const e of L) {
        if (!e.janet) continue;
        const key = e.janet.join(',');
        if (!groups.has(key)) groups.set(key, []);
        groups.get(key).push(e);
      }
      for (const [key, es] of groups) {
        const [nl, l] = key.split(',').map(Number);
        es.sort((a, b) => a.Z - b.Z);
        es.forEach((e, i) => put(e.Z, off[l] + i, nl - 1));
      }
      const rest = L.filter((e) => !e.janet).sort((a, b) => a.Z - b.Z);
      rest.forEach((e, i) => put(e.Z, i, 9.5));
    }
    state.bounds = { x0: x0 - CELL * 0.6, y0: y0 - CELL * 0.6, x1: x1 + CELL * 0.2, y1: y1 + CELL * 0.2 };
  }

  // children packed inside a circle of radius R: positions relative to centre
  function pack(n, R) {
    if (n <= 0) return { pos: [], r: 0 };
    if (n === 1) return { pos: [{ x: 0, y: 0 }], r: R * 0.55 };
    if (n <= 8) {
      const ring = R * 0.6;
      const r = Math.min(R * 0.34, ring * Math.sin(Math.PI / n) * 0.9);
      const pos = [];
      for (let i = 0; i < n; i++) {
        const a = -Math.PI / 2 + (i * 2 * Math.PI) / n;
        pos.push({ x: ring * Math.cos(a), y: ring * Math.sin(a) });
      }
      return { pos, r };
    }
    // n > 8: an Archimedean spiral, consecutive children adjacent along it, so the
    // Lambda_8 ladder (charge c-1 -> c) traces the spiral instead of crossing the circle.
    // Same packing density as a sunflower: r = 0.66 R / sqrt(n).
    let r = (0.66 * R) / Math.sqrt(n);
    const d = 2 * r * 1.12;                 // spacing along the spiral and between turns
    const b = d / (2 * Math.PI);            // rho = b * theta
    const pos = [{ x: 0, y: 0 }];
    // arc length of rho = b*theta from 0: s(t) = (b/2)(t sqrt(1+t^2) + asinh t); ds/dt = b sqrt(1+t^2).
    // Inverted by Newton from a guess at or above the root, so it always terminates (a stepwise
    // march on floating-point residue did not, for n = 51, 60, 67, 70, 79, 90 among others).
    const arc = (t) => (b / 2) * (t * Math.sqrt(1 + t * t) + Math.asinh(t));
    // The centre holds the first child; the spiral starts one full turn out, at rho = d, because
    // near the origin the curve wraps so tightly that an arc of length d ends only 0.5 d away.
    let theta = 2 * Math.PI;
    const s0 = arc(theta);
    for (let i = 1; i < n; i++) {
      const target = s0 + (i - 1) * d;
      let t = Math.max(theta, Math.sqrt((2 * target) / b));
      for (let k = 0; k < 30; k++) {
        const step = (arc(t) - target) / (b * Math.sqrt(1 + t * t));
        t -= step;
        if (Math.abs(step) < 1e-10) break;
      }
      theta = t;
      pos.push({ x: b * theta * Math.cos(theta), y: b * theta * Math.sin(theta) });
    }
    let maxr = 0;
    for (const p of pos) maxr = Math.max(maxr, Math.hypot(p.x, p.y));
    const scale = maxr > 0 ? Math.min(1, (R - r) / maxr) : 1;
    if (scale < 1) { for (const p of pos) { p.x *= scale; p.y *= scale; } r *= scale; }
    return { pos, r };
  }

  // the tree under one element, with frames relative to the element centre
  function buildTree(Z, rec) {
    const byCharge = new Map();
    for (const ch of rec.channels) {
      if (!byCharge.has(ch.charge)) byCharge.set(ch.charge, []);
      byCharge.get(ch.charge).push(ch);
    }
    const charges = [...byCharge.keys()].sort((a, b) => a - b);
    const pk = pack(charges.length, EL_R * 0.86);
    const ladder = rec.lambda8 || [];
    const ions = charges.map((c, i) => {
      const chans = byCharge.get(c).slice().sort((a, b) => a.l - b.l);
      const stepIndex = ladder.findIndex((s) => s.charge === c);
      const ion = {
        kind: 'ion', Z, charge: c, dx: pk.pos[i].x, dy: pk.pos[i].y, r: pk.r,
        rec: chans, step: stepIndex >= 0 ? ladder[stepIndex] : null, stepIndex, channels: [],
        nMeasured: chans.reduce((a, ch) => a + ch.measured.filter((m) => m.grade === 'measured').length, 0),
      };
      const pc = pack(chans.length, pk.r * 0.92);
      ion.channels = chans.map((ch, j) => {
        const node = {
          kind: 'channel', Z, charge: c, l: ch.l, dx: ion.dx + pc.pos[j].x, dy: ion.dy + pc.pos[j].y, r: pc.r,
          rec: ch, parent: ion, cells: [],
          nMeasured: ch.measured.filter((m) => m.grade === 'measured').length,
        };
        const pm = pack(ch.measured.length, pc.r * 0.9);
        node.cells = ch.measured.map((m, q) => ({
          kind: 'cell', Z, charge: c, l: ch.l, mult: m.mult, dx: node.dx + pm.pos[q].x, dy: node.dy + pm.pos[q].y, r: pm.r,
          rec: m, parent: node, lim: limitKind(m.bound_note),
        }));
        return node;
      });
      return ion;
    });
    return { ions };
  }

  // ---------------------------------------------------------------- loading (the data protocol)
  function ensureElement(Z) {
    Z = +Z;
    if (state.elements.has(Z)) return Promise.resolve(state.elements.get(Z));
    if (state.pending.has(Z)) return state.pending.get(Z);
    const p = new Promise((resolve, reject) => {
      const have = window.__mi && window.__mi.el && window.__mi.el[Z];
      if (have) { resolve(have); return; }
      const s = document.createElement('script');
      s.src = `${DATA}elements/${Z}.js${dataVersion()}`;
      s.async = true;
      s.onload = () => {
        s.remove();
        const rec = window.__mi && window.__mi.el && window.__mi.el[Z];
        if (rec) resolve(rec);
        else reject(new Error(`data/elements/${Z}.js loaded but set no window.__mi.el[${Z}] — it is not a protocol file (run python3 tools/webindex.py)`));
      };
      s.onerror = () => {
        s.remove();
        reject(new Error(`data/elements/${Z}.js could not be loaded. It is written by python3 tools/webindex.py into public/data/; without it this element has no record.`));
      };
      document.head.appendChild(s);
    }).then((rec) => {
      state.elements.set(Z, rec);
      state.trees.set(Z, buildTree(Z, rec));
      state.pending.delete(Z);
      state.loadErrors.delete(Z);
      $('#loading').hidden = state.pending.size === 0;
      requestDraw();
      return rec;
    }).catch((err) => {
      state.pending.delete(Z);
      state.loadErrors.set(Z, err.message);
      $('#loading').hidden = state.pending.size === 0;
      console.error(err);
      throw err;
    });
    state.pending.set(Z, p);
    $('#loading').hidden = false;
    return p;
  }
  // every element file, settled rather than all-or-nothing: {records, failed} so a caller can say
  // which elements were unavailable instead of throwing on the first
  function loadAll() {
    const zs = state.index.layout.map((e) => e.Z);
    return Promise.allSettled(zs.map((Z) => ensureElement(Z))).then((rs) => {
      const records = [], failed = [];
      rs.forEach((r, i) => { if (r.status === 'fulfilled') records.push(r.value); else failed.push(zs[i]); });
      return { records, failed };
    });
  }
  // the size of that load, from the manifest, so no figure is typed
  function dataSize() {
    const m = state.index.manifest || [];
    return { files: m.length, bytes: m.reduce((a, x) => a + (x.bytes || 0), 0) };
  }

  // ---------------------------------------------------------------- nodes
  function elementNode(Z) {
    const e = state.index.layout.find((x) => x.Z === Z);
    return e ? { kind: 'element', Z, e } : null;
  }
  const rootNode = { kind: 'root' };

  function nodeFrame(node) {
    if (node.kind === 'root') {
      const b = state.bounds;
      return { cx: (b.x0 + b.x1) / 2, cy: (b.y0 + b.y1) / 2, r: Math.max(b.x1 - b.x0, b.y1 - b.y0) / 2, w: b.x1 - b.x0, h: b.y1 - b.y0 };
    }
    if (node.kind === 'element') {
      const f = state.frames.get(node.Z);
      return { cx: f.cx, cy: f.cy, r: CELL / 2, w: CELL, h: CELL };
    }
    if (node.kind === 'ghost') {
      return { cx: node.x + CELL / 2, cy: node.y + CELL / 2, r: CELL / 2, w: CELL, h: CELL };
    }
    const f = state.frames.get(node.Z);
    return { cx: f.cx + node.dx, cy: f.cy + node.dy, r: node.r, w: node.r * 2, h: node.r * 2 };
  }

  function parentOf(node) {
    if (node.kind === 'root') return null;
    if (node.kind === 'element' || node.kind === 'ghost') return rootNode;
    if (node.kind === 'ion') return elementNode(node.Z);
    return node.parent;
  }

  function pathOf(node) {
    const out = [];
    for (let n = node; n; n = parentOf(n)) out.unshift(n);
    return out;
  }

  function label(node) {
    switch (node.kind) {
      case 'root': return 'Index';
      case 'element': return node.e.symbol;
      case 'ghost': return `period ${node.p} · group ${node.g}`;
      case 'ion': return `${symbolOf(node.Z)} ${roman(node.charge)}`;
      case 'channel': return `${LSYM[node.l] || node.l}`;
      case 'cell': return `2S+1 = ${node.mult}`;
    }
    return '';
  }
  const symbolOf = (Z) => (state.index.layout.find((x) => x.Z === Z) || {}).symbol || `Z${Z}`;

  function hashOf(node) {
    if (node.kind === 'root') return '#/';
    if (node.kind === 'ghost') return `#/E/${node.p}/${node.g}`;
    const parts = [symbolOf(node.Z)];
    if (node.charge) parts.push(roman(node.charge));
    if (node.l !== undefined) parts.push(LSYM[node.l] || String(node.l));
    if (node.mult !== undefined) parts.push(String(node.mult));
    return '#/' + parts.join('/');
  }
  function pathText(node) {
    return pathOf(node).map((n) => n.kind === 'root' ? 'The Method Index' : n.kind === 'channel' ? `ℓ=${n.l}` : n.kind === 'cell' ? `2S+1=${n.mult}` : label(n)).join(' › ');
  }

  // ---------------------------------------------------------------- camera
  function W() { return canvas.clientWidth; }
  function H() { return canvas.clientHeight; }
  const toScreen = (x, y) => ({ x: x * state.cam.k + state.cam.tx, y: y * state.cam.k + state.cam.ty });
  const toWorld = (sx, sy) => ({ x: (sx - state.cam.tx) / state.cam.k, y: (sy - state.cam.ty) / state.cam.k });

  // the legend sits over the canvas at bottom-left; the home view fits the layout above it
  function overlayInsets() {
    const legend = $('#legend');
    return { top: 0, bottom: legend && !legend.hidden ? legend.offsetHeight + 12 : 0 };
  }
  function homeCam() {
    const b = state.bounds, ins = overlayInsets();
    const h = Math.max(60, H() - ins.top - ins.bottom);
    const k = Math.min(W() / (b.x1 - b.x0), h / (b.y1 - b.y0));
    return { k, tx: (W() - (b.x0 + b.x1) * k) / 2, ty: ins.top + (h - (b.y0 + b.y1) * k) / 2 };
  }
  function camFor(frame, fill = 0.72) {
    const k = (fill * Math.min(W(), H())) / Math.max(frame.w, frame.h);
    return { k, tx: W() / 2 - frame.cx * k, ty: H() / 2 - frame.cy * k };
  }
  function flyTo(target, ms = 650) {
    if (reduced || ms === 0) { state.cam = target; state.anim = null; requestDraw(); return; }
    const from = { ...state.cam };
    const t0 = performance.now();
    state.anim = { from, to: target, t0, ms };
    requestDraw();
  }
  function stepAnim(now) {
    const a = state.anim;
    if (!a) return false;
    let t = Math.min(1, (now - a.t0) / a.ms);
    t = t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
    const lk = Math.log(a.from.k) + (Math.log(a.to.k) - Math.log(a.from.k)) * t;
    const k = Math.exp(lk);
    const cxTo = (W() / 2 - a.to.tx) / a.to.k, cyTo = (H() / 2 - a.to.ty) / a.to.k;
    const cxFrom = (W() / 2 - a.from.tx) / a.from.k, cyFrom = (H() / 2 - a.from.ty) / a.from.k;
    const cx = cxFrom + (cxTo - cxFrom) * t, cy = cyFrom + (cyTo - cyFrom) * t;
    state.cam = { k, tx: W() / 2 - cx * k, ty: H() / 2 - cy * k };
    if (t >= 1) { state.cam = a.to; state.anim = null; }
    return true;
  }
  function zoomAt(sx, sy, factor) {
    if (state.view === 'lattice') { orbitZoom(factor); return; }
    const home = homeCam();
    const k = Math.max(home.k * 0.4, Math.min(20000, state.cam.k * factor));
    const f = k / state.cam.k;
    state.cam = { k, tx: sx - (sx - state.cam.tx) * f, ty: sy - (sy - state.cam.ty) * f };
    state.anim = null;
    requestDraw();
  }

  // ---------------------------------------------------------------- drawing
  let drawQueued = false;
  let canvasVisible = true;          // an IntersectionObserver on #canvas-wrap clears it while scrolled away
  function requestDraw() {
    if (drawQueued) return;
    drawQueued = true;
    requestAnimationFrame(draw);
  }

  function resize() {
    if (state.view === 'lattice' && state.scene && state.orbit) fitOrbit(state.scene, state.orbit);
    const dpr = window.devicePixelRatio || 1;
    canvas.width = Math.round(wrap.clientWidth * dpr);
    canvas.height = Math.round(wrap.clientHeight * dpr);
    canvas.style.width = wrap.clientWidth + 'px';
    canvas.style.height = wrap.clientHeight + 'px';
    requestDraw();
  }

  function draw(now) {
    try { drawInner(now); }
    catch (err) {
      // a blank canvas says nothing; the error is written on it, and to the console, so it can be reported
      console.error(err);
      try {
        const dpr = window.devicePixelRatio || 1; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
        ctx.fillStyle = state.colors ? state.colors.bg : '#fff'; ctx.fillRect(0, 0, W(), H());
        ctx.fillStyle = '#b3261e'; ctx.font = '13px system-ui, sans-serif'; ctx.textAlign = 'left'; ctx.textBaseline = 'top';
        const lines = ['the drawing failed in this browser:', String(err && err.message || err), (err && err.stack || '').split('\n')[1] || '', 'Please report this line with your browser and device.'];
        lines.forEach((t, i) => ctx.fillText(t.slice(0, 120), 12, 12 + i * 18));
      } catch (e2) { /* nothing more to do */ }
    }
  }
  function drawInner(now) {
    drawQueued = false;
    if (!canvasVisible) return;      // resumed by the observer when the canvas scrolls back into view
    const animating = stepAnim(now || performance.now());
    const dpr = window.devicePixelRatio || 1;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    const C = state.colors;
    ctx.fillStyle = C.bg;
    ctx.fillRect(0, 0, W(), H());
    if (!state.index) return;
    if (state.view === 'lattice') { drawLattice(); if (animating) requestDraw(); return; }
    const s = CELL * state.cam.k;

    drawAxes(s);

    if (state.layout === 'table') {
      for (const g of state.ghosts) {
        const p = toScreen(g.x, g.y);
        if (p.x + s < 0 || p.y + s < 0 || p.x > W() || p.y > H()) continue;
        const deferred = g.def && g.def.class === 'deferred';
        const R = cellRect(p, s);
        const isHoverG = state.hover && state.hover.kind === 'ghost' && state.hover.p === g.p && state.hover.g === g.g;
        // a tint, not a dash: the lighter one forbidden by l <= n-1, the fuller one a cell that
        // could hold an element and does not; no edge, the gutters draw the grid
        roundRectPath(R.x, R.y, R.w, R.h, R.r);
        ctx.fillStyle = C.ghost; ctx.globalAlpha = deferred ? 0.4 : 0.16;
        ctx.fill(); ctx.globalAlpha = 1;
        if (isHoverG) { ctx.strokeStyle = C.accent; ctx.globalAlpha = 0.6; ctx.lineWidth = 1.25; ctx.stroke(); ctx.globalAlpha = 1; ctx.lineWidth = 1; }
        if (s >= 30) {
          ctx.fillStyle = C.faint;
          ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
          const sub = g.def ? (g.def.p === 1 && g.def.g === 2 ? 'He' : g.def.subshell) : 'E';
          ctx.font = F(Math.max(9, s * 0.16));
          ctx.fillText(sub, p.x + s / 2, p.y + s / 2 - (s >= 60 ? s * 0.06 : 0));
          if (s >= 60 && g.def) {
            ctx.font = F(Math.max(8, s * 0.075));
            ctx.fillText(g.def.p === 1 && g.def.g === 2 ? "helium's slot" : g.def.class, p.x + s / 2, p.y + s / 2 + s * 0.12);
          }
        }
        if (state.selected && state.selected.kind === 'ghost' && state.selected.p === g.p && state.selected.g === g.g) {
          roundRectPath(R.x - 1, R.y - 1, R.w + 2, R.h + 2, R.r + 1);
          ctx.strokeStyle = C.accent; ctx.lineWidth = 2; ctx.stroke(); ctx.lineWidth = 1;
        }
      }
    }

    for (const e of state.index.layout) {
      const f = state.frames.get(e.Z);
      const p = toScreen(f.x, f.y);
      if (p.x + s < 0 || p.y + s < 0 || p.x > W() || p.y > H()) continue;
      drawElement(e, p, s);
    }
    if (animating) requestDraw();
  }

  function drawAxes(s) {
    const C = state.colors;
    if (s < 14) return;
    ctx.fillStyle = C.muted;
    ctx.fillStyle = C.faint;
    ctx.font = F(Math.max(9, Math.min(11.5, s * 0.14)), 'sans');
    ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
    if (state.layout === 'table') {
      for (let g = 1; g <= 18; g++) {
        const p = toScreen((g - 0.5) * CELL, -0.42 * CELL);
        ctx.fillText(String(g), p.x, p.y);
      }
      ctx.textAlign = 'right';
      for (let per = 1; per <= 7; per++) {
        const p = toScreen(-0.32 * CELL, (per - 0.5) * CELL);
        ctx.fillText(String(per), p.x, p.y);
      }
      ctx.textAlign = 'left';
      ctx.textAlign = 'right';
      let p = toScreen(2.8 * CELL, 9 * CELL); ctx.fillText('58–71', p.x, p.y);
      p = toScreen(2.8 * CELL, 10 * CELL); ctx.fillText('90–103', p.x, p.y);
      ctx.textAlign = 'right';
      p = toScreen(-0.32 * CELL, 7.5 * CELL); ctx.fillText('8', p.x, p.y);
    } else {
      ctx.textAlign = 'right';
      for (let nl = 1; nl <= 8; nl++) {
        const p = toScreen(-0.25 * CELL, (nl - 0.5) * CELL);
        ctx.fillText(`n+ℓ=${nl}`, p.x, p.y);
      }
      ctx.textAlign = 'center';
      const blocks = [['f', 0, 14], ['d', 14, 10], ['p', 24, 6], ['s', 30, 2]];
      for (const [b, o, n] of blocks) {
        const p = toScreen((o + n / 2) * CELL, -0.35 * CELL);
        ctx.fillText(`ℓ=${LSYM.indexOf(b)} (${b})`, p.x, p.y);
      }
      const p = toScreen(-0.25 * CELL, 10 * CELL); ctx.fillText('no cell', p.x, p.y);
    }
  }

  function drawElement(e, p, s) {
    const C = state.colors;
    const sel = state.selected;
    const isSel = sel && sel.kind === 'element' && sel.Z === e.Z;
    const isHover = !isSel && state.hover && state.hover.kind === 'element' && state.hover.Z === e.Z;
    const R = cellRect(p, s);
    const tint = e.populated ? (C.blk[e.block] || C.blk.none) : C.blk.none;
    roundRectPath(R.x, R.y, R.w, R.h, R.r);
    ctx.fillStyle = tint;
    ctx.fill();
    // the edge is the tint itself, one tone deeper; a spectra-only element carries its colour there
    ctx.lineWidth = 1;
    ctx.strokeStyle = e.populated ? shade(tint, effectiveTheme() === 'dark' ? 1.35 : 0.9) : shade(C.csv, 1, 0.55);
    ctx.stroke();
    if (isHover || isSel) {
      roundRectPath(R.x - 1, R.y - 1, R.w + 2, R.h + 2, R.r + 1);
      ctx.strokeStyle = C.accent; ctx.lineWidth = isSel ? 2 : 1.25;
      if (isHover) ctx.globalAlpha = 0.6;
      ctx.stroke(); ctx.globalAlpha = 1; ctx.lineWidth = 1;
    }
    // the markers: a filled dot for one of the eleven the record displaces at c → ∞ (READ), a
    // hollow one for a displacement in the reconstructed walk (RECONSTRUCTED), top right
    if (s >= 14 && (e.relativistic || e.walk_displaced)) {
      const d = Math.max(2, s * 0.045);
      let mx = R.x + R.w - d * 1.8, my = R.y + d * 1.8;
      if (e.relativistic) {
        ctx.beginPath(); ctx.arc(mx, my, d, 0, Math.PI * 2); ctx.fillStyle = C.rel; ctx.fill();
        mx -= d * 2.8;
      }
      if (e.walk_displaced) {
        ctx.beginPath(); ctx.arc(mx, my, d * 0.9, 0, Math.PI * 2); ctx.strokeStyle = C.walk; ctx.lineWidth = Math.max(1, d * 0.45); ctx.stroke(); ctx.lineWidth = 1;
      }
      if (s >= 150) {
        ctx.textAlign = 'right'; ctx.textBaseline = 'top'; ctx.font = F(s * 0.032, 'sans');
        const parts = [];
        if (e.relativistic) parts.push('displaced at c → ∞');
        if (e.walk_displaced) parts.push('reconstructed walk');
        ctx.fillStyle = C.muted;
        ctx.fillText(parts.join(' · '), R.x + R.w - d * 6, R.y + d * 0.9);
      }
    }

    if (s >= 20) {
      ctx.fillStyle = C.text;
      ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
      const symSize = s >= 150 ? s * 0.11 : s * 0.3;
      ctx.font = F(symSize, 'serif', '500');
      const sy = s >= 150 ? p.y + s * 0.085 : p.y + s * 0.5;
      ctx.fillText(e.symbol, p.x + s / 2, sy);
    }
    if (s >= 48) {
      ctx.fillStyle = C.muted;
      ctx.textAlign = 'left'; ctx.textBaseline = 'top';
      ctx.font = F(s * 0.1);
      ctx.fillText(String(e.Z), p.x + s * 0.085, p.y + s * 0.075);
      if (e.name) {
        ctx.textAlign = 'center'; ctx.textBaseline = 'bottom';
        ctx.font = F(s * 0.08, 'sans');
        ctx.fillText(e.name, p.x + s / 2, p.y + s * 0.935);
      }
      if (e.counts) {
        ctx.textAlign = 'right'; ctx.textBaseline = 'top';
        ctx.font = F(s * 0.075);
        ctx.fillStyle = e.counts.measured ? C.measured : C.muted;
        ctx.fillText(e.counts.measured ? `${e.counts.measured} m` : `${e.counts.rows}`, p.x + s * 0.915, p.y + s * 0.075 + (s >= 150 && (e.relativistic || e.walk_displaced) ? s * 0.04 : 0));
      }
    }
    if (s >= 150) {
      const cx = p.x + s / 2, cy = p.y + s * 0.53;
      const R = EL_R * state.cam.k;
      ctx.beginPath(); ctx.arc(cx, cy, R, 0, Math.PI * 2);
      ctx.strokeStyle = C.line; ctx.setLineDash([3, 4]); ctx.lineWidth = 1; ctx.stroke(); ctx.setLineDash([]);
      const tree = state.trees.get(e.Z);
      if (tree) {
        drawLadder(e, tree, cx, cy);
        drawIons(e, tree, cx, cy);
      } else {
        if (!state.loadErrors.has(e.Z) && !state.pending.has(e.Z)) ensureElement(e.Z).catch(() => {});
        ctx.fillStyle = C.muted;
        ctx.font = F(Math.max(10, s * 0.06));
        ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText(state.loadErrors.has(e.Z) ? 'record not loaded' : 'loading …', cx, cy);
      }
    }
  }

  // the element's inner circle is drawn at (cx, cy + 0.03 s) so the symbol has room above;
  // the same offset is used by hit-testing and flying via ionCentre()
  function ionOrigin(Z) {
    const f = state.frames.get(Z);
    return { x: f.cx, y: f.cy + CELL * 0.03 };
  }

  // The Λ₈ ionisation ladder: one line per step of the record's own ladder, joining the
  // ion at charge − 1 to the ion at charge. Nothing that is not a step is drawn.
  function drawLadder(e, tree, ox, oy) {
    const rec = state.elements.get(e.Z);
    if (!rec || !rec.lambda8 || !rec.lambda8.length) return;
    const C = state.colors, k = state.cam.k, sel = state.selected;
    const byCharge = new Map(tree.ions.map((i) => [i.charge, i]));
    const selCharge = sel && sel.Z === e.Z && sel.charge !== undefined ? sel.charge : null;
    ctx.save();
    ctx.lineCap = 'round';
    const pass = (hot) => {
      for (const s of rec.lambda8) {
        if ((selCharge === s.charge) !== hot) continue;
        const a = byCharge.get(s.charge - 1), b = byCharge.get(s.charge);
        if (!a || !b) continue;
        const ax = ox + a.dx * k, ay = oy + a.dy * k, bx = ox + b.dx * k, by = oy + b.dy * k;
        const dx = bx - ax, dy = by - ay, d = Math.hypot(dx, dy);
        if (d < 1) continue;
        const ux = dx / d, uy = dy / d;
        const x1 = ax + ux * a.r * k, y1 = ay + uy * a.r * k, x2 = bx - ux * b.r * k, y2 = by - uy * b.r * k;
        if ((x2 - x1) * ux + (y2 - y1) * uy <= 0) continue;
        // one quiet line per rung; the selected ion's rungs drawn full
        ctx.strokeStyle = C.accent;
        ctx.globalAlpha = hot ? 1 : 0.45;
        ctx.lineWidth = hot ? 2 : 1.25;
        ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x2, y2); ctx.stroke();
      }
    };
    pass(false);
    pass(true);
    ctx.restore();
  }

  function drawIons(e, tree, ox, oy) {
    const C = state.colors, k = state.cam.k, sel = state.selected;
    for (const ion of tree.ions) {
      const rs = ion.r * k;
      const x = ox + ion.dx * k, y = oy + ion.dy * k;
      if (x + rs < 0 || y + rs < 0 || x - rs > W() || y - rs > H()) continue;
      if (rs < 1.2) continue;
      const isSel = sel && sel.kind === 'ion' && sel.Z === ion.Z && sel.charge === ion.charge;
      const inPath = sel && sel.Z === ion.Z && sel.charge === ion.charge;
      ctx.beginPath(); ctx.arc(x, y, rs, 0, Math.PI * 2);
      ctx.fillStyle = C.surface; ctx.fill();
      ctx.lineWidth = isSel ? 2 : 1;
      ctx.strokeStyle = isSel ? C.accent : (inPath ? C.accent : C.lineStrong);
      ctx.stroke();
      if (ion.nMeasured && rs >= 4) {
        ctx.beginPath(); ctx.arc(x, y, rs * 0.94, 0, Math.PI * 2);
        ctx.strokeStyle = C.measured; ctx.lineWidth = Math.max(1, rs * 0.05); ctx.stroke();
      }
      if (rs >= 13 && rs < 45) {
        ctx.fillStyle = C.text;
        ctx.font = F(Math.max(9, rs * 0.42), 'mono', '500');
        ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText(roman(ion.charge), x, y);
      } else if (rs >= 45) {
        ctx.fillStyle = C.muted;
        ctx.font = F(Math.max(10, rs * 0.11), 'mono', '500');
        ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText(`${e.symbol} ${roman(ion.charge)}`, x, y - rs * 0.82);
        drawChannels(ion, ox, oy);
      }
    }
  }

  function drawChannels(ion, ox, oy) {
    const C = state.colors, k = state.cam.k, sel = state.selected;
    for (const ch of ion.channels) {
      const rs = ch.r * k;
      const x = ox + ch.dx * k, y = oy + ch.dy * k;
      if (rs < 1.5) continue;
      const isSel = sel && sel.kind === 'channel' && sel.Z === ch.Z && sel.charge === ch.charge && sel.l === ch.l;
      const inPath = sel && sel.Z === ch.Z && sel.charge === ch.charge && sel.l === ch.l;
      const nM = ch.nMeasured;
      ctx.beginPath(); ctx.arc(x, y, rs, 0, Math.PI * 2);
      ctx.fillStyle = C.bg; ctx.fill();
      ctx.lineWidth = isSel ? 2 : 1;
      ctx.strokeStyle = isSel || inPath ? C.accent : (nM ? C.measured : C.lineStrong);
      ctx.stroke();
      if (rs >= 10 && rs < 40) {
        ctx.fillStyle = C.text;
        ctx.font = F(Math.max(9, rs * 0.7), 'mono', '500');
        ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText(LSYM[ch.l] || String(ch.l), x, y);
      } else if (rs >= 40) {
        ctx.fillStyle = C.muted;
        ctx.font = F(Math.max(10, rs * 0.16), 'mono', '500');
        ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText(`${LSYM[ch.l] || ch.l}`, x, y - rs * 0.78);
        drawCells(ch, ox, oy);
      }
    }
  }

  function drawCells(ch, ox, oy) {
    const C = state.colors, k = state.cam.k, sel = state.selected;
    for (const c of ch.cells) {
      const rs = c.r * k;
      const x = ox + c.dx * k, y = oy + c.dy * k;
      if (rs < 1) continue;
      const isSel = sel && sel.kind === 'cell' && sel.Z === c.Z && sel.charge === c.charge && sel.l === c.l && sel.mult === c.mult;
      ctx.beginPath(); ctx.arc(x, y, rs, 0, Math.PI * 2);
      if (state.cellColor === 'limit') {
        const col = C.lim[c.lim] || C.computed;
        if (c.lim === 'symmetry') { ctx.fillStyle = C.surface; ctx.fill(); ctx.strokeStyle = col; ctx.lineWidth = Math.max(1, rs * 0.12); ctx.stroke(); }
        else { ctx.fillStyle = col; ctx.fill(); }
        if (c.rec.grade === 'measured') { ctx.strokeStyle = C.measured; ctx.lineWidth = Math.max(1, rs * 0.14); ctx.stroke(); }
      } else if (c.rec.grade === 'measured') { ctx.fillStyle = C.measured; ctx.fill(); }
      else if (c.rec.grade === 'exact') { ctx.fillStyle = C.surface; ctx.fill(); ctx.strokeStyle = C.exact; ctx.lineWidth = Math.max(1, rs * 0.12); ctx.stroke(); }
      else { ctx.fillStyle = C.computed; ctx.globalAlpha = 0.7; ctx.fill(); ctx.globalAlpha = 1; }
      if (c.rec.witness === 'witnessed' && rs >= 6) {
        ctx.beginPath(); ctx.arc(x, y, rs * 1.25, 0, Math.PI * 2);
        ctx.strokeStyle = C.measured; ctx.lineWidth = 1; ctx.stroke();
      }
      if (isSel) { ctx.beginPath(); ctx.arc(x, y, rs + 3, 0, Math.PI * 2); ctx.strokeStyle = C.accent; ctx.lineWidth = 2; ctx.stroke(); }
      if (rs >= 9) {
        ctx.fillStyle = (state.cellColor === 'limit' ? (c.lim === 'symmetry' || c.lim === 'none' || c.lim === 'no-analysis') : c.rec.grade !== 'measured') ? C.text : C.bg;
        ctx.font = F(Math.max(9, rs * 0.8), 'mono', '500');
        ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText(String(c.mult), x, y);
      }
    }
  }

  // ---------------------------------------------------------------- the lattice, in three dimensions
  // Λ_spectra drawn as the source figure draws it — the Löwdin paper's Figure 1(b) and the
  // source renderer: element across,
  // ionisation stage up, ℓ into the page, one cube per cell, a known cell a full cube and an
  // unmeasured one a faint small cube. An element is its slab at x = Z; where a site holds two
  // multiplicities the cells sit side by side along x. The scene is built from the element
  // record the plane draws, nothing is computed here, and a colour means the grade it means
  // everywhere else on the page. The whole index (the third layout) is every slab at once.
  const LAT = { KNOWN: 0.86, FAINT: 0.26 };     // node diameters, in cells: the archived renderer's 0.86 for a known cell; the unmeasured drawn small
  function orbitHome() { return { rx: 0.36, ry: -0.6, zoom: 1 }; }

  function rgbOf(col) {
    const s = String(col || '').trim();
    let m = s.match(/^#([0-9a-f]{6})$/i);
    if (m) return [parseInt(m[1].slice(0, 2), 16), parseInt(m[1].slice(2, 4), 16), parseInt(m[1].slice(4, 6), 16)];
    m = s.match(/^#([0-9a-f]{3})$/i);
    if (m) return [17 * parseInt(m[1][0], 16), 17 * parseInt(m[1][1], 16), 17 * parseInt(m[1][2], 16)];
    m = s.match(/^rgba?\(([^)]+)\)$/i);
    if (m) { const v = m[1].split(',').map((x) => parseFloat(x)); return [v[0], v[1], v[2]]; }
    return [128, 128, 128];
  }
  function shade(col, k, a) {
    const [r, g, b] = rgbOf(col).map((v) => Math.max(0, Math.min(255, Math.round(v * k))));
    return a === undefined ? `rgb(${r},${g},${b})` : `rgba(${r},${g},${b},${a})`;
  }

  // the camera: yaw about y, pitch about x, the eye at −D on the rotated z axis, a mild
  // perspective; zoom is the focal length, so the scene turns about its own centre
  function latRotation(scene, o) {
    const cy = Math.cos(o.ry), sy = Math.sin(o.ry), cx = Math.cos(o.rx), sx = Math.sin(o.rx);
    const c = scene.centre;
    const rot = (x, y, z) => {
      x -= c[0]; y -= c[1]; z -= c[2];
      const x1 = x * cy + z * sy, z1 = -x * sy + z * cy;
      return [x1, y * cx - z1 * sx, y * sx + z1 * cx];
    };
    const rotN = (x, y, z) => { const x1 = x * cy + z * sy, z1 = -x * sy + z * cy; return [x1, y * cx - z1 * sx, y * sx + z1 * cx]; };
    return { rot, rotN, D: Math.max(3, scene.R * 3.2) };
  }
  // fit: the eight corners of the scene's extent, projected at the orbit's angle, fill 86 % of the
  // viewport; the focal length and the centring shift are kept on the orbit so the scene does not
  // swim as it turns, and are refitted on Reset and on resize
  function fitOrbit(scene, o) {
    const { rot, D } = latRotation(scene, o), ex = scene.ext;
    let x0 = Infinity, x1 = -Infinity, y0 = Infinity, y1 = -Infinity;
    for (const x of [ex.x0, ex.x1]) for (const y of [ex.y0, ex.y1]) for (const z of [ex.z0, ex.z1]) {
      const r = rot(x, y, z), d = Math.max(0.05, r[2] + D);
      x0 = Math.min(x0, r[0] / d); x1 = Math.max(x1, r[0] / d); y0 = Math.min(y0, r[1] / d); y1 = Math.max(y1, r[1] / d);
    }
    const legend = $('#legend');
    const pad = 28, bottom = legend && !legend.hidden && !legend.classList.contains('is-collapsed') ? Math.min(H() * 0.4, legend.offsetHeight + 24) : 44;
    const w = Math.max(60, W() - 2 * pad), h = Math.max(60, H() - pad - bottom);
    o.fitF = Math.min(w / Math.max(1e-6, x1 - x0), h / Math.max(1e-6, y1 - y0));
    o.dx = -o.fitF * (x0 + x1) / 2;
    o.dy = o.fitF * (y0 + y1) / 2 - (bottom - pad) / 2;
    if (scene.kind === 'element' && scene.ions.length > 1) {
      // the ions must stay legible: at least 13 px apart, the slab's base anchored near the bottom
      // of the viewport, so a heavy element shows its lower stages (where the known cells sit)
      // and the reader zooms out or pans for the rest
      const a = rot(scene.lx, 0, 3.5), b2 = rot(scene.lx, 1, 3.5);
      const da = Math.max(0.05, a[2] + D), db = Math.max(0.05, b2[2] + D);
      const gap = o.fitF * Math.hypot(b2[0] / db - a[0] / da, b2[1] / db - a[1] / da);
      if (gap < 13) {
        o.fitF *= 13 / gap;
        const base = rot(scene.centre[0], ex.y0, scene.centre[2]), dbase = Math.max(0.05, base[2] + D);
        o.dx = -o.fitF * (x0 + x1) / 2;
        o.dy = (H() - bottom - 10) - H() / 2 + (o.fitF * base[1]) / dbase;
      }
    }
    return o;
  }
  function latCamera(scene) {
    const o = state.orbit || orbitHome();
    if (!o.fitF) fitOrbit(scene, o);
    const { rot, rotN, D } = latRotation(scene, o);
    const f = o.fitF * o.zoom, dx = o.dx || 0, dy = o.dy || 0;
    const proj = (p) => { const d = Math.max(0.05, p[2] + D); return { x: W() / 2 + dx + (f * p[0]) / d, y: H() / 2 + dy - (f * p[1]) / d, d, k: f / d }; };
    return { rot, rotN, proj, D, f, eye: [0, 0, -D] };
  }

  function cellColour(node) {
    const C = state.colors;
    if (state.cellColor === 'limit') return C.lim[node.lim] || C.computed;
    return node.rec.grade === 'measured' ? C.measured : node.rec.grade === 'exact' ? C.exact : C.computed;
  }

  // one element: its slab, stage up (y = charge − 1), ℓ into the page (z = ℓ), the cells of a
  // site along x, and the Λ₈ ladder climbing the front-left edge one rung per recorded step
  function buildElementScene(Z) {
    const rec = state.elements.get(Z), tree = state.trees.get(Z);
    const e = state.index.layout.find((x) => x.Z === Z);
    if (!rec || !tree || !e) return null;
    const cubes = [], ions = [];
    let xmax = 0;
    for (const ion of tree.ions) {
      ions.push({ charge: ion.charge, y: ion.charge - 1, node: ion });
      for (const ch of ion.channels) {
        const n = ch.cells.length;
        ch.cells.forEach((c, i) => {
          const x = i - (n - 1) / 2;
          xmax = Math.max(xmax, Math.abs(x));
          const known = c.rec.grade !== 'computed';
          cubes.push({ x, y: ion.charge - 1, z: ch.l, s: known ? LAT.KNOWN : LAT.FAINT, known, node: c, Z, charge: ion.charge, l: ch.l, mult: c.mult });
        });
      }
    }
    const lx = -(xmax + 1.15);
    const byCharge = new Map(ions.map((i) => [i.charge, i]));
    const ladder = [];
    for (const s of rec.lambda8 || []) {
      const a = byCharge.get(s.charge - 1), b = byCharge.get(s.charge);
      if (a && b) ladder.push({ a: [lx, a.y, -0.85], b: [lx, b.y, -0.85], charge: s.charge });
    }
    const ext = { x0: lx - 0.3, x1: xmax + 0.6, y0: -0.6, y1: ions.length - 0.4, z0: -1.1, z1: 7.6 };
    const centre = [(ext.x0 + ext.x1) / 2, (ext.y0 + ext.y1) / 2, (ext.z0 + ext.z1) / 2];
    const R = Math.hypot(ext.x1 - ext.x0, ext.y1 - ext.y0, ext.z1 - ext.z0) / 2;
    return { kind: 'element', Z, e, rec, cubes, ions, ladder, ext, centre, R, lx, xmax, slabs: [] };
  }

  // the whole index: every element a slab at x = Z (charge 1..Z by ℓ 0..7, the generator
  // asserts it), the known cells as cubes, one per site, from data/index.js's lattice block
  function buildIndexScene() {
    const lat = state.index.lattice;
    if (!lat || !lat.known) return null;
    const byEl = new Map(state.index.layout.map((e) => [e.Z, e]));
    const slabs = [], cubes = [];
    for (const e of state.index.layout) {
      const Z = e.Z;
      slabs.push({ Z, e, node: { kind: 'element', Z, e }, centre: [Z, (Z - 1) / 2, 3.5],
        corners: [[Z, -0.5, -0.5], [Z, Z - 0.5, -0.5], [Z, Z - 0.5, 7.5], [Z, -0.5, 7.5]] });
    }
    const sites = new Map();
    for (const k of lat.known) {
      const key = `${k[0]},${k[1]},${k[2]}`;
      let s = sites.get(key);
      if (!s) { s = { Z: k[0], charge: k[1], l: k[2], mults: [], measured: 0, exact: 0 }; sites.set(key, s); }
      s.mults.push(k[3]); if (k[4] === 1) s.measured++; else s.exact++;
    }
    for (const s of sites.values()) {
      cubes.push({ x: s.Z, y: s.charge - 1, z: s.l, s: LAT.KNOWN, known: true, grade: s.measured ? 'measured' : 'exact', site: s, Z: s.Z, charge: s.charge, l: s.l, e: byEl.get(s.Z), node: null });
    }
    const zmax = lat.Z_max || 120;
    const ext = { x0: 0.4, x1: zmax + 0.6, y0: -0.6, y1: zmax - 0.4, z0: -0.6, z1: 7.6 };
    const centre = [(ext.x0 + ext.x1) / 2, (ext.y0 + ext.y1) / 2, (ext.z0 + ext.z1) / 2];
    const R = Math.hypot(ext.x1 - ext.x0, ext.y1 - ext.y0, ext.z1 - ext.z0) / 2;
    return { kind: 'index', cubes, slabs, ions: [], ladder: [], ext, centre, R, lat };
  }

  // the drawn periodic layout as a lattice: group across (x), period up (y, period 1 at the
  // top), ℓ into the page (z), so the s, p, d and f blocks become layers. An element is a node
  // at its drawn cell in its block's layer; the set-aside lanthanides and actinides, which the
  // layout gives no group, are drawn in their period row at the long-form table's columns 3 to
  // 16 (x = 3 + Z − 58, and Z − 90), which is a DERIVED placement and the caption says so; the
  // thirty-six ghosts sit at their cells in the layer the ℓ-by-group rule gives them. Every node
  // is the same node the plane view opens.
  function tableHome() { return { rx: 0.7, ry: -0.48, zoom: 1 }; }
  function lOfGroup(g) { return g <= 2 ? 0 : g <= 12 ? 2 : 1; }
  function buildTableScene() {
    const c = state.index.closure, C = state.colors;
    const he2 = state.heliumAt === 2 && c.placement && c.placement.helium_at_2;
    const cubes = [];
    let derivedPlacements = 0;
    for (const e of state.index.layout) {
      let x, derived = false;
      if (e.set_aside) { x = (e.Z <= 71 ? e.Z - 58 : e.Z - 90) + 3; derived = true; derivedPlacements += 1; }
      else if (he2 && e.Z === 2) x = 2;
      else x = e.group;
      if (x === null || x === undefined || e.period === null || e.period === undefined) continue;
      const lz = e.block && LSYM.indexOf(e.block) >= 0 ? LSYM.indexOf(e.block) : lOfGroup(x);
      cubes.push({ x, y: 8 - e.period, z: lz, s: LAT.KNOWN, known: true, Z: e.Z, e, derivedX: derived, label: e.symbol,
        colour: e.populated ? (C.blk[e.block] || C.blk.none) : C.csv, node: { kind: 'element', Z: e.Z, e } });
    }
    for (const g of state.ghosts || []) {
      const d = g.def || {};
      cubes.push({ x: g.g, y: 8 - g.p, z: d.l !== undefined && d.l !== null ? d.l : lOfGroup(g.g), s: LAT.KNOWN * 0.8, known: false, ghost: true, p: g.p, g: g.g,
        cls: d.class || null, label: d.subshell ? d.subshell.split(',')[0] : null, node: { kind: 'ghost', ...g } });
    }
    const ext = { x0: 0.3, x1: 18.7, y0: -0.6, y1: 7.6, z0: -0.7, z1: 3.7 };
    const centre = [(ext.x0 + ext.x1) / 2, (ext.y0 + ext.y1) / 2, (ext.z0 + ext.z1) / 2];
    const R = Math.hypot(ext.x1 - ext.x0, ext.y1 - ext.y0, ext.z1 - ext.z0) / 2;
    return { kind: 'table', cubes, slabs: [], ions: [], ladder: [], ext, centre, R, ghosts: (state.ghosts || []).length, derivedPlacements, heliumAt: he2 ? 2 : 18 };
  }
  function drawTableAxes(scene, cam) {
    const C = state.colors, ex = scene.ext;
    scene._labels = [];
    const P = (x, y, z) => cam.proj(cam.rot(x, y, z));
    // the base plane under the table, and the four ℓ layers as hairlines across it
    const by = ex.y0 + 0.05;
    ctx.beginPath();
    [[ex.x0, by, ex.z0], [ex.x1, by, ex.z0], [ex.x1, by, ex.z1], [ex.x0, by, ex.z1]].forEach((q, i) => { const p = P(q[0], q[1], q[2]); if (i === 0) ctx.moveTo(p.x, p.y); else ctx.lineTo(p.x, p.y); });
    ctx.closePath(); ctx.fillStyle = shade(C.lineStrong, 1, 0.08); ctx.fill(); ctx.strokeStyle = shade(C.lineStrong, 1, 0.5); ctx.lineWidth = 1; ctx.stroke();
    for (let l = 0; l <= 3; l++) latLine(cam, [ex.x0, by, l], [ex.x1, by, l], shade(C.lineStrong, 1, 0.2), 1);
    // each layer's outline, a faint frame standing on the base
    for (let l = 0; l <= 3; l++) {
      const E = [[[ex.x0, by, l], [ex.x0, ex.y1, l]], [[ex.x1, by, l], [ex.x1, ex.y1, l]], [[ex.x0, ex.y1, l], [ex.x1, ex.y1, l]]];
      for (const [a, b] of E) latLine(cam, a, b, shade(C.lineStrong, 1, 0.12), 1);
    }
    // the axes: group along the front edge, period up the left, ℓ into the page
    const ox = ex.x0, oy = ex.y0, oz = -0.5;
    latLine(cam, [ox, oy, oz], [ex.x1, oy, oz], shade(C.lineStrong, 1, 0.9), 1);
    latLine(cam, [ox, oy, oz], [ox, ex.y1, oz], shade(C.lineStrong, 1, 0.9), 1);
    latLine(cam, [ox, oy, oz], [ox, oy, 3.5], shade(C.lineStrong, 1, 0.9), 1);
    ctx.fillStyle = C.muted; ctx.textBaseline = 'middle';
    const p1 = P(1, oy, oz), p2 = P(2, oy, oz), gap = Math.hypot(p2.x - p1.x, p2.y - p1.y);
    ctx.font = F(Math.max(9, Math.min(11, gap * 0.6)), 'sans'); ctx.textAlign = 'center';
    const every = gap >= 12 ? 1 : gap >= 6 ? 2 : 3;
    for (let g = 1; g <= 18; g++) { if ((g - 1) % every !== 0 && g !== 18) continue; const p = P(g, oy, oz); ctx.fillText(String(g), p.x, p.y + 12); }
    ctx.textAlign = 'right';
    for (let per = 1; per <= 8; per++) { const p = P(ox, 8 - per, oz); ctx.fillText(String(per), p.x - 7, p.y); }
    ctx.textAlign = 'center';
    for (let l = 0; l <= 3; l++) { const p = P(ox, oy, l); ctx.fillText(LSYM[l], p.x - 10, p.y + 10); }
    ctx.font = F(10.5, 'sans'); ctx.textAlign = 'left';
    const pX = P(ex.x1 + 0.6, oy, oz); ctx.fillText('group →', pX.x + 4, pX.y);
    const pY = P(ox, ex.y1 + 0.5, oz); ctx.fillText('period (1 at the top)', pY.x + 4, pY.y);
    const pZ = P(ox, oy, 4.1); ctx.fillText('ℓ → (the blocks as layers)', pZ.x + 4, pZ.y);
  }

  function sameNode(a, b) {
    return !!a && !!b && a.kind === b.kind && a.Z === b.Z && a.charge === b.charge && a.l === b.l && a.mult === b.mult;
  }
  function selMatchesCube(sel, cb) {
    if (!sel || sel.Z !== cb.Z) return false;
    if (sel.kind === 'cell') return sel.charge === cb.charge && sel.l === cb.l && sel.mult === cb.mult;
    if (sel.kind === 'channel') return sel.charge === cb.charge && sel.l === cb.l;
    if (sel.kind === 'ion') return sel.charge === cb.charge;
    return false;
  }

  // a cell as a node: the nest view's vocabulary in three dimensions -- a filled sphere for a
  // measured cell, a paper disc ringed in green for an exact one, a small grey dot for a computed
  // one, the witnessed ring outside a measured node, the limit colours when that facet is on;
  // a soft highlight off the top left gives the sphere its shape
  function drawCube(cb, cam, col, outline) {
    const C = state.colors;
    const p0 = cam.proj(cb._r);
    if (p0.x < -40 || p0.y < -40 || p0.x > W() + 40 || p0.y > H() + 40) return;
    const r = Math.max(0.6, (cb.s / 2) * p0.k * (cb.known ? 1 : 0.9));
    const node = cb.node;
    if (cb.ghost) {
      // a cell the operator admits and the layout does not hold: a hollow node in the ghost tint,
      // the deferred ones fuller, its subshell written in when there is room
      ctx.beginPath(); ctx.arc(p0.x, p0.y, r, 0, Math.PI * 2);
      ctx.fillStyle = C.ghost; ctx.globalAlpha = cb.cls === 'deferred' ? 0.38 : 0.16; ctx.fill(); ctx.globalAlpha = 1;
      ctx.setLineDash([3, 3]); ctx.strokeStyle = shade(C.ghost, 0.8); ctx.lineWidth = 1; ctx.stroke(); ctx.setLineDash([]);
      if (cb.label && r >= 9) { ctx.fillStyle = C.muted; ctx.font = F(Math.max(8, r * 0.55), 'sans'); ctx.textAlign = 'center'; ctx.textBaseline = 'middle'; ctx.fillText(cb.label, p0.x, p0.y); }
      if (outline) { ctx.beginPath(); ctx.arc(p0.x, p0.y, r + 2.5, 0, Math.PI * 2); ctx.strokeStyle = outline; ctx.lineWidth = 1.75; ctx.stroke(); }
      ctx.lineWidth = 1;
      return;
    }
    const grade = node && node.rec ? node.rec.grade : cb.grade;
    const byLimit = state.cellColor === 'limit' && node && node.rec;
    const hollow = byLimit ? node.lim === 'symmetry' : grade === 'exact';
    ctx.beginPath(); ctx.arc(p0.x, p0.y, r, 0, Math.PI * 2);
    if (!cb.known) {
      ctx.fillStyle = C.computed; ctx.globalAlpha = 0.55; ctx.fill(); ctx.globalAlpha = 1;
    } else if (hollow) {
      ctx.fillStyle = C.surface; ctx.fill();
      ctx.strokeStyle = col; ctx.lineWidth = Math.max(1, r * 0.22); ctx.stroke();
    } else {
      if (r >= 3) {
        const g = ctx.createRadialGradient(p0.x - r * 0.35, p0.y - r * 0.35, r * 0.1, p0.x, p0.y, r);
        g.addColorStop(0, shade(col, 1.25)); g.addColorStop(0.7, col); g.addColorStop(1, shade(col, 0.72));
        ctx.fillStyle = g;
      } else ctx.fillStyle = col;
      ctx.fill();
      if (r >= 2) { ctx.strokeStyle = shade(col, 0.7); ctx.lineWidth = 0.6; ctx.stroke(); }
      if (grade === 'measured' && node && node.rec && node.rec.witness === 'witnessed' && r >= 4) {
        ctx.beginPath(); ctx.arc(p0.x, p0.y, r * 1.3, 0, Math.PI * 2);
        ctx.strokeStyle = C.measured; ctx.lineWidth = 1; ctx.stroke();
      }
    }
    if (cb.label && r >= 7) {
      // the element's symbol on its node, in the table lattice
      ctx.fillStyle = C.ink || C.text || '#1c2128'; ctx.font = F(Math.max(8, Math.min(16, r * 0.95)), 'serif', '600'); ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
      ctx.fillText(cb.label, p0.x, p0.y + 0.5);
      if (cb.derivedX && r >= 10) { ctx.font = F(Math.max(7, r * 0.4), 'sans'); ctx.fillStyle = C.muted; ctx.fillText('set aside', p0.x, p0.y + r * 0.72); }
    }
    if (outline) {
      ctx.beginPath(); ctx.arc(p0.x, p0.y, r + 2.5, 0, Math.PI * 2);
      ctx.strokeStyle = outline; ctx.lineWidth = 1.75; ctx.stroke();
    }
    ctx.lineWidth = 1;
  }

  function latLine(cam, a, b, style, width, dash) {
    const pa = cam.proj(cam.rot(a[0], a[1], a[2])), pb = cam.proj(cam.rot(b[0], b[1], b[2]));
    ctx.beginPath(); ctx.moveTo(pa.x, pa.y); ctx.lineTo(pb.x, pb.y);
    ctx.strokeStyle = style; ctx.lineWidth = width; if (dash) ctx.setLineDash(dash);
    ctx.stroke(); ctx.setLineDash([]);
    return [pa, pb];
  }

  // the axes and their ticks: stage up (roman numerals, each an ion, tappable), ℓ into the
  // page (s p d f g h i k), and for the whole index Z across
  function drawLatAxes(scene, cam) {
    if (scene.kind === 'table') return drawTableAxes(scene, cam);
    const C = state.colors, ex = scene.ext;
    scene._labels = [];
    const ox = scene.kind === 'element' ? scene.lx - 0.15 : ex.x0, oy = -0.5, oz = -0.5;
    const yTop = scene.kind === 'element' ? scene.ions.length - 0.5 : ex.y1;
    const P = (x, y, z) => cam.proj(cam.rot(x, y, z));
    // the base plane, under everything, and the slab's silhouette
    const bx0 = scene.kind === 'element' ? scene.lx - 0.4 : ex.x0, bx1 = ex.x1, by = ex.y0 + 0.05, bz0 = -0.6, bz1 = 7.6;
    ctx.beginPath();
    [[bx0, by, bz0], [bx1, by, bz0], [bx1, by, bz1], [bx0, by, bz1]].forEach((q, i) => { const p = P(q[0], q[1], q[2]); if (i === 0) ctx.moveTo(p.x, p.y); else ctx.lineTo(p.x, p.y); });
    ctx.closePath(); ctx.fillStyle = shade(C.surface === '' ? C.bg : C.lineStrong, 1, 0.08); ctx.fill();
    ctx.strokeStyle = shade(C.lineStrong, 1, 0.5); ctx.lineWidth = 1; ctx.stroke();
    if (scene.kind === 'index') {
      for (let Z = 10; Z < ex.x1; Z += 10) latLine(cam, [Z, by, bz0], [Z, by, bz1], shade(C.lineStrong, 1, 0.25), 1);
    } else {
      for (let l = 0; l <= 7; l++) latLine(cam, [bx0, by, l], [bx1, by, l], shade(C.lineStrong, 1, 0.18), 1);
      // the silhouette of the slab, twelve hairlines
      const sx0 = -(scene.xmax || 0) - 0.5, sx1 = (scene.xmax || 0) + 0.5, sy0 = -0.5, sy1 = yTop, sz0 = -0.5, sz1 = 7.5;
      const E = [[[sx0, sy0, sz0], [sx1, sy0, sz0]], [[sx0, sy0, sz1], [sx1, sy0, sz1]], [[sx0, sy1, sz0], [sx1, sy1, sz0]], [[sx0, sy1, sz1], [sx1, sy1, sz1]],
                 [[sx0, sy0, sz0], [sx0, sy1, sz0]], [[sx1, sy0, sz0], [sx1, sy1, sz0]], [[sx0, sy0, sz1], [sx0, sy1, sz1]], [[sx1, sy0, sz1], [sx1, sy1, sz1]],
                 [[sx0, sy0, sz0], [sx0, sy0, sz1]], [[sx1, sy0, sz0], [sx1, sy0, sz1]], [[sx0, sy1, sz0], [sx0, sy1, sz1]], [[sx1, sy1, sz0], [sx1, sy1, sz1]]];
      for (const [q1, q2] of E) latLine(cam, q1, q2, shade(C.lineStrong, 1, 0.3), 1);
    }
    // the axes
    latLine(cam, [ox, oy, oz], [ox, yTop, oz], shade(C.lineStrong, 1, 0.9), 1);
    latLine(cam, [ox, oy, oz], [ox, oy, 7.5], shade(C.lineStrong, 1, 0.9), 1);
    if (scene.kind === 'index') latLine(cam, [ox, oy, oz], [ex.x1, oy, oz], shade(C.lineStrong, 1, 0.9), 1);
    ctx.fillStyle = C.muted; ctx.textBaseline = 'middle';
    // ℓ ticks
    const zt = [];
    for (let l = 0; l < 8; l++) zt.push(P(ox, oy, l));
    const zgap = Math.hypot(zt[1].x - zt[0].x, zt[1].y - zt[0].y);
    if (zgap >= 9) {
      ctx.font = F(Math.max(9, Math.min(12, zgap * 0.75)), 'sans'); ctx.textAlign = 'center';
      for (let l = 0; l < 8; l++) ctx.fillText(LSYM[l] || String(l), zt[l].x, zt[l].y + 11);
    }
    // stage ticks: every ion in the element scene (each a tappable numeral), every tenth in the index
    if (scene.kind === 'element') {
      const ys = scene.ions.map((i) => P(ox, i.y, oz));
      const ygap = ys.length > 1 ? Math.hypot(ys[1].x - ys[0].x, ys[1].y - ys[0].y) : 40;
      const step = ygap >= 11 ? 1 : Math.ceil(11 / Math.max(ygap, 0.5));
      ctx.font = F(Math.max(9, Math.min(11.5, ygap * 0.6 + 5)), 'sans'); ctx.textAlign = 'right';
      const sel = state.selected;
      scene.ions.forEach((ion, i) => {
        const p = ys[i];
        const hot = sel && sel.Z === scene.Z && sel.charge === ion.charge;
        if (i % step === 0 || hot) {
          const t = roman(ion.charge);
          ctx.fillStyle = hot ? C.accent : C.muted;
          ctx.fillText(t, p.x - 7, p.y);
          const w = ctx.measureText(t).width;
          scene._labels.push({ x: p.x - 7 - w - 2, y: p.y - 7, w: w + 8, h: 14, node: ion.node });
        }
      });
      ctx.fillStyle = C.muted;
    } else {
      ctx.font = F(10, 'sans'); ctx.textAlign = 'right';
      for (let c = 10; c <= ex.y1; c += 10) { const p = P(ox, c - 1, oz); ctx.fillText(roman(c), p.x - 7, p.y); }
      ctx.textAlign = 'center';
      for (let Z = 10; Z <= ex.x1; Z += 10) { const p = P(Z, oy, oz); ctx.fillText(String(Z), p.x, p.y + 12); }
      // the slabs' symbols, where they have room
      const p1 = P(1, ex.y1, oz), p2 = P(2, ex.y1, oz);
      const gap = Math.hypot(p2.x - p1.x, p2.y - p1.y);
      const every = gap >= 13 ? 1 : gap >= 6.5 ? 2 : gap >= 2.6 ? 5 : 10;
      ctx.font = F(Math.max(9, Math.min(11, gap * 0.8)), 'sans'); ctx.textAlign = 'center'; ctx.textBaseline = 'bottom';
      ctx.fillStyle = C.faint;
      for (const sl of scene.slabs) {
        if (sl.Z % every !== 0 && every !== 1) continue;
        const p = P(sl.Z, sl.Z - 0.5 + 0.6, 3.5);
        ctx.fillText(sl.e.symbol, p.x, p.y);
      }
      ctx.textBaseline = 'middle';
    }
    // axis names
    ctx.fillStyle = C.muted; ctx.font = F(10.5, 'sans'); ctx.textAlign = 'left';
    const pY = P(ox, yTop + (scene.kind === 'element' ? 0.7 : 4), oz);
    ctx.fillText('ionisation stage ↑', pY.x + 4, pY.y);
    const pZ = P(ox, oy, 8.3);
    ctx.fillText('ℓ →', pZ.x + 4, pZ.y);
    if (scene.kind === 'index') { const pX = P(ex.x1 + 1, oy, oz); ctx.fillText('Z →', pX.x + 4, pX.y); }
  }

  function drawLattice() {
    const scene = state.scene, C = state.colors;
    if (!scene) {
      ctx.fillStyle = C.muted; ctx.font = F(12);
      ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
      const sel = state.selected;
      ctx.fillText(sel && state.loadErrors.has(sel.Z) ? 'record not loaded' : 'loading the lattice …', W() / 2, H() / 2);
      return;
    }
    const cam = latCamera(scene);
    const sel = state.selected;
    drawLatAxes(scene, cam);
    // the selected ion's row, as a plane under its cubes
    if (scene.kind === 'element' && sel && sel.Z === scene.Z && sel.kind === 'ion') {
      const y = sel.charge - 1, ex = scene.ext;
      ctx.beginPath();
      [[ex.x0 + 0.5, y, -0.5], [ex.x1, y, -0.5], [ex.x1, y, 7.5], [ex.x0 + 0.5, y, 7.5]].forEach((q, i) => { const p = cam.proj(cam.rot(q[0], q[1], q[2])); if (i === 0) ctx.moveTo(p.x, p.y); else ctx.lineTo(p.x, p.y); });
      ctx.closePath(); ctx.fillStyle = shade(C.accent, 1, 0.1); ctx.fill(); ctx.strokeStyle = shade(C.accent, 1, 0.5); ctx.lineWidth = 1; ctx.stroke();
    }
    const items = [];
    for (const sl of scene.slabs) { const r = cam.rot(sl.centre[0], sl.centre[1], sl.centre[2]); items.push({ t: 'slab', d: r[2], sl }); }
    for (const cb of scene.cubes) { cb._r = cam.rot(cb.x, cb.y, cb.z); items.push({ t: 'cube', d: cb._r[2], cb }); }
    for (const seg of scene.ladder) { const a = cam.rot(seg.a[0], seg.a[1], seg.a[2]), b = cam.rot(seg.b[0], seg.b[1], seg.b[2]); items.push({ t: 'ladder', d: (a[2] + b[2]) / 2, seg }); }
    items.sort((a, b) => b.d - a.d);
    for (const it of items) {
      if (it.t === 'cube') {
        const cb = it.cb;
        const col = cb.colour ? cb.colour : (cb.node && cb.node.rec ? cellColour(cb.node) : (cb.grade === 'measured' ? C.measured : C.exact));
        const hot = scene.kind === 'element' ? selMatchesCube(sel, cb)
          : scene.kind === 'table' ? (cb.ghost ? !!(sel && sel.kind === 'ghost' && sel.p === cb.p && sel.g === cb.g) : !!(sel && sel.kind !== 'root' && sel.kind !== 'ghost' && sel.Z === cb.Z))
          : (sel && sel.kind !== 'root' && sel.Z === cb.Z);
        drawCube(cb, cam, col, hot ? C.accent : null);
      } else if (it.t === 'slab') {
        const sl = it.sl;
        const hot = sel && sel.kind !== 'root' && sel.Z === sl.Z;
        ctx.beginPath();
        sl.corners.forEach((q, i) => { const p = cam.proj(cam.rot(q[0], q[1], q[2])); if (i === 0) ctx.moveTo(p.x, p.y); else ctx.lineTo(p.x, p.y); });
        ctx.closePath();
        ctx.fillStyle = shade(sl.e.populated ? (C.blk[sl.e.block] || C.blk.none) : C.csv, 1, hot ? 0.75 : 0.5); ctx.fill();
        ctx.strokeStyle = hot ? C.accent : shade(C.lineStrong, 1, 0.6); ctx.lineWidth = hot ? 1.5 : 0.5; ctx.stroke();
      } else {
        const seg = it.seg;
        const hot = sel && sel.Z === scene.Z && sel.charge === seg.charge;
        const [pa, pb] = [cam.proj(cam.rot(seg.a[0], seg.a[1], seg.a[2])), cam.proj(cam.rot(seg.b[0], seg.b[1], seg.b[2]))];
        ctx.lineCap = 'round';
        ctx.strokeStyle = C.accent; ctx.globalAlpha = hot ? 1 : 0.5; ctx.lineWidth = hot ? 2 : 1.25;
        ctx.beginPath(); ctx.moveTo(pa.x, pa.y); ctx.lineTo(pb.x, pb.y); ctx.stroke();
        // the rung's ion, a dot at the upper end
        ctx.beginPath(); ctx.arc(pb.x, pb.y, hot ? 3.2 : 2.2, 0, Math.PI * 2); ctx.fillStyle = C.accent; ctx.fill();
        ctx.globalAlpha = 1;
      }
    }
    // a scene taller or wider than the canvas: how much is clipped, kept for the drag handler,
    // and a chip at the clipped edge saying so, since a cut-off slab looks finished otherwise
    state.latOverflow = latOverflow(scene, cam);
    const ov = state.latOverflow;
    if (ov.top > 0 || ov.bottom > 0) {
      ctx.font = F(11, 'sans'); ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
      const chip = (text, y) => {
        const w = ctx.measureText(text).width + 18;
        ctx.fillStyle = shade(C.surface === '' ? C.bg : C.surface, 1, 0.92); roundRectPath(W() / 2 - w / 2, y - 11, w, 22, 11); ctx.fill();
        ctx.strokeStyle = shade(C.lineStrong, 1, 0.6); ctx.lineWidth = 1; ctx.stroke();
        ctx.fillStyle = C.muted; ctx.fillText(text, W() / 2, y);
      };
      const stages = scene.kind === 'element' ? ' stages' : '';
      if (ov.top > 0) chip(`▲ ${scene.kind === 'element' ? ov.topCount + stages + ' above' : 'more above'} · pull down to see them`, 16);
      if (ov.bottom > 0) chip(`▼ ${scene.kind === 'element' ? ov.bottomCount + stages + ' below' : 'more below'} · pull up to see them`, H() - 16);
    }
  }
  // how far the scene's projected extent overruns the canvas, in px, and for an element how
  // many stages are hidden at each edge
  function latOverflow(scene, cam) {
    const ex = scene.ext;
    let y0 = Infinity, y1 = -Infinity;
    for (const x of [ex.x0, ex.x1]) for (const y of [ex.y0, ex.y1]) for (const z of [ex.z0, ex.z1]) { const p = cam.proj(cam.rot(x, y, z)); y0 = Math.min(y0, p.y); y1 = Math.max(y1, p.y); }
    const out = { top: Math.max(0, 8 - y0), bottom: Math.max(0, y1 - (H() - 8)), topCount: 0, bottomCount: 0 };
    if (scene.kind === 'element') {
      for (const ion of scene.ions) { const p = cam.proj(cam.rot(0, ion.y, 3.5)); if (p.y < 6) out.topCount += 1; else if (p.y > H() - 6) out.bottomCount += 1; }
    }
    return out;
  }
  // the scene may be scrolled by dragging, never out of sight: at least 60 px of it stays on the canvas
  function clampPan(scene, o) {
    const cam = latCamera(scene), ex = scene.ext;
    let y0 = Infinity, y1 = -Infinity, x0 = Infinity, x1 = -Infinity;
    for (const x of [ex.x0, ex.x1]) for (const y of [ex.y0, ex.y1]) for (const z of [ex.z0, ex.z1]) { const p = cam.proj(cam.rot(x, y, z)); y0 = Math.min(y0, p.y); y1 = Math.max(y1, p.y); x0 = Math.min(x0, p.x); x1 = Math.max(x1, p.x); }
    if (y1 < 60) o.dy += 60 - y1; else if (y0 > H() - 60) o.dy -= y0 - (H() - 60);
    if (x1 < 60) o.dx += 60 - x1; else if (x0 > W() - 60) o.dx -= x0 - (W() - 60);
    return o;
  }

  // the caption in the bar above the canvas: what is drawn, and what it is drawn from
  function updateCaption() {
    const el = $('#canvas-caption');
    if (!el || !state.index) return;
    let html = '';
    if (state.view === 'lattice') {
      const sc = state.scene;
      if (!sc) html = 'loading the lattice …';
      else if (sc.kind === 'element') {
        const n = sc.cubes.length, k = sc.cubes.filter((c) => c.known).length;
        html = `<b>${esc(sc.e.symbol)}</b> as its slab of the lattice · stage up, ℓ into the page · ${sc.ions.length} ions · ${n.toLocaleString()} cells, ${k} known · one node per cell · derived from the record, nothing computed`;
      } else if (sc.kind === 'table') {
        const c = state.index.closure;
        html = `<b>The drawn layout as a lattice</b> · group across, period up, ℓ into the page · ${sc.cubes.length - sc.ghosts} elements · ${sc.ghosts} ghosts${sc.heliumAt === 2 ? ' · helium at group 2' : ''} · E = ${sc.heliumAt === 2 && c.placement ? c.placement.helium_at_2.E : c.E} · the ${sc.derivedPlacements} set aside drawn at the long-form columns`;
      } else {
        html = `<b>Λ_spectra as a lattice</b> · element across, stage up, ℓ into the page · ${sc.lat.sites.toLocaleString()} sites · ${sc.lat.known.length.toLocaleString()} known cells as nodes (Figure 6)`;
      }
    } else {
      const c = state.index.closure;
      const sel = state.selected;
      if (sel && sel.kind !== 'root' && sel.kind !== 'ghost' && sel.Z) {
        const e = state.index.layout.find((x) => x.Z === sel.Z) || {};
        html = `<b>${esc(e.symbol || '')}</b> as nested circles · ions, channels, cells`;
      } else if (state.layout === 'janet') html = `<b>Janet's layout</b> (n+ℓ, ℓ) · E = 0`;
      else html = `<b>The drawn layout</b> · ${c.held} held · ${c.admitted} admitted by ℛ · E = ${state.heliumAt === 2 && c.placement ? c.placement.helium_at_2.E + ' with helium at group 2' : c.E}`;
    }
    if (el.innerHTML !== html) el.innerHTML = html;
  }

  function hitLattice(sx, sy) {
    const scene = state.scene;
    if (!scene) return null;
    for (const lb of scene._labels || []) if (sx >= lb.x && sx <= lb.x + lb.w && sy >= lb.y && sy <= lb.y + lb.h) return lb.node;
    const cam = latCamera(scene);
    let best = null;
    for (const cb of scene.cubes) {
      const p = cam.proj(cam.rot(cb.x, cb.y, cb.z));
      const hs = Math.max(3, (cb.s / 2) * p.k * 1.1);
      if (Math.hypot(sx - p.x, sy - p.y) <= hs && (!best || p.d < best.d)) best = { d: p.d, cb };
    }
    if (best) return best.cb.node || { go: [best.cb.Z, best.cb.charge, best.cb.l] };
    let bestSlab = null;
    for (const sl of scene.slabs) {
      const pts = sl.corners.map((q) => cam.proj(cam.rot(q[0], q[1], q[2])));
      let inside = false;
      for (let i = 0, j = 3; i < 4; j = i++) {
        if ((pts[i].y > sy) !== (pts[j].y > sy) && sx < ((pts[j].x - pts[i].x) * (sy - pts[i].y)) / (pts[j].y - pts[i].y) + pts[i].x) inside = !inside;
      }
      if (!inside) continue;
      const d = cam.rot(sl.centre[0], sl.centre[1], sl.centre[2])[2];
      if (!bestSlab || d < bestSlab.d) bestSlab = { d, sl };
    }
    return bestSlab ? bestSlab.sl.node : null;
  }

  // which view a node opens in: the plane for the layouts' root and the ghosts, the lattice
  // for the third layout's root and, by the element-view toggle, for every node of an element
  function viewFor(node) {
    if (node.kind === 'root') return state.layout === 'lattice' || state.layout === 'table3d' ? 'lattice' : 'plane';
    if (node.kind === 'ghost') return state.layout === 'table3d' ? 'lattice' : 'plane';
    return state.elementView === 'lattice' ? 'lattice' : 'plane';
  }
  function enterView(node) {
    const v = viewFor(node), prev = state.view;
    state.view = v;
    const lg = $('#legend-lattice'); if (lg) lg.hidden = v !== 'lattice';
    if (v !== 'lattice') return v;
    if (node.kind === 'root' || node.kind === 'ghost') {
      if (state.layout === 'table3d') {
        if (!state.scene || state.scene.kind !== 'table') { state.scene = buildTableScene(); state.orbit = tableHome(); if (state.scene) fitOrbit(state.scene, state.orbit); }
        else if (node.kind === 'root' && state.orbit) { state.orbit.zoom = 1; fitOrbit(state.scene, state.orbit); }
      } else if (!state.scene || state.scene.kind !== 'index') { state.scene = buildIndexScene(); state.orbit = orbitHome(); if (state.scene) fitOrbit(state.scene, state.orbit); }
      else if (node.kind === 'root' && state.orbit) { state.orbit.zoom = 1; fitOrbit(state.scene, state.orbit); }
    } else if (!state.scene || state.scene.kind !== 'element' || state.scene.Z !== node.Z) {
      state.scene = buildElementScene(node.Z);
      if (!state.scene) {
        ensureElement(node.Z).then(() => {
          if (state.view === 'lattice' && state.selected && state.selected.Z === node.Z) { state.scene = buildElementScene(node.Z); if (state.scene && state.orbit) fitOrbit(state.scene, state.orbit); updateCaption(); requestDraw(); }
        }).catch(() => { requestDraw(); });
      }
      state.orbit = prev === 'lattice' && state.orbit ? { rx: state.orbit.rx, ry: state.orbit.ry, zoom: 1 } : orbitHome();
      if (state.scene) fitOrbit(state.scene, state.orbit);
    }
    return v;
  }
  function setElementView(mode) {
    if (mode === state.elementView) return;
    state.elementView = mode;
    document.querySelectorAll('.seg-btn[data-elview]').forEach((b) => b.classList.toggle('is-on', b.dataset.elview === mode));
    const sel = state.selected || rootNode;
    select(sel, { setHash: false, reveal: false });
  }
  // exposed for the browser smoke test, which reads the scene it cannot otherwise see
  window.__mi_state = state;
  window.__mi_lat = { cam: latCamera, hit: hitLattice };
  function orbitZoom(factor) {
    const o = state.orbit || orbitHome();
    o.zoom = Math.max(0.25, Math.min(16, o.zoom * factor));
    state.orbit = o; requestDraw();
  }

  // ---------------------------------------------------------------- hit test
  function hit(sx, sy) {
    const w = toWorld(sx, sy);
    const s = CELL * state.cam.k;
    for (const e of state.index.layout) {
      const f = state.frames.get(e.Z);
      if (w.x < f.x || w.x > f.x + CELL || w.y < f.y || w.y > f.y + CELL) continue;
      const el = { kind: 'element', Z: e.Z, e };
      if (s < 150) return el;
      const tree = state.trees.get(e.Z);
      if (!tree) return el;
      const o = ionOrigin(e.Z);
      const k = state.cam.k;
      for (const ion of tree.ions) {
        const dx = w.x - (o.x + ion.dx), dy = w.y - (o.y + ion.dy);
        if (dx * dx + dy * dy > ion.r * ion.r) continue;
        if (ion.r * k < 45) return ion;
        for (const ch of ion.channels) {
          const ex = w.x - (o.x + ch.dx), ey = w.y - (o.y + ch.dy);
          if (ex * ex + ey * ey > ch.r * ch.r) continue;
          if (ch.r * k < 40) return ch;
          for (const c of ch.cells) {
            const fx = w.x - (o.x + c.dx), fy = w.y - (o.y + c.dy);
            if (fx * fx + fy * fy <= c.r * c.r * 1.6) return c;
          }
          return ch;
        }
        return ion;
      }
      return el;
    }
    if (state.layout === 'table') {
      for (const g of state.ghosts) {
        if (w.x >= g.x && w.x <= g.x + CELL && w.y >= g.y && w.y <= g.y + CELL) return { kind: 'ghost', ...g };
      }
    }
    return null;
  }

  function frameFor(node) {
    if (node.kind === 'ion' || node.kind === 'channel' || node.kind === 'cell') {
      const o = ionOrigin(node.Z);
      return { cx: o.x + node.dx, cy: o.y + node.dy, r: node.r, w: node.r * 2, h: node.r * 2 };
    }
    return nodeFrame(node);
  }

  // ---------------------------------------------------------------- selection
  function revealPlate() {
    const plate = $('#inspector');
    const behavior = reduced ? 'auto' : 'smooth';
    try {
      if (isPhone()) {
        plate.scrollIntoView({ behavior, block: 'start' });
      } else {
        const side = $('#side');
        const top = plate.getBoundingClientRect().top - side.getBoundingClientRect().top + side.scrollTop;
        side.scrollTo({ top, behavior });
      }
    } catch (e) { plate.scrollIntoView(); }
  }
  function revealCanvas() {
    try { wrap.scrollIntoView({ behavior: reduced ? 'auto' : 'smooth', block: 'start' }); } catch (e) { wrap.scrollIntoView(); }
  }

  async function select(node, opts = {}) {
    const { fly = true, ms = 650, setHash = true, reveal = true } = opts;
    state.selected = node;
    renderInspector(node);
    renderCrumbs(node);
    if (setHash) {
      const h = hashOf(node);
      state.lastHash = h;
      if (location.hash !== h) history.replaceState(null, '', h);
    }
    const view = enterView(node);
    if (fly && view === 'plane') {
      const flyMs = reveal && isPhone() ? 0 : ms;   // the plate scrolls the canvas away on a phone
      if (node.kind === 'root') flyTo(homeCam(), flyMs);
      else {
        const fill = node.kind === 'element' ? 0.78 : node.kind === 'ghost' ? 0.5 : 0.6;
        flyTo(camFor(frameFor(node), fill), flyMs);
      }
    }
    if (reveal) revealPlate();
    updateCaption();
    requestDraw();
  }

  async function goToPath(Z, charge, l, mult, opts = {}) {
    const el = elementNode(Z);
    if (!el) return false;
    if (charge === undefined) { await select(el, opts); return true; }
    try { await ensureElement(Z); } catch (e) { await select(el, opts); return false; }
    const tree = state.trees.get(Z);
    const ion = tree.ions.find((i) => i.charge === charge);
    if (!ion) { await select(el, opts); return false; }
    if (l === undefined) { await select(ion, opts); return true; }
    const ch = ion.channels.find((c) => c.l === l);
    if (!ch) { await select(ion, opts); return false; }
    if (mult === undefined) { await select(ch, opts); return true; }
    const cell = ch.cells.find((c) => c.mult === mult);
    if (!cell) { await select(ch, opts); return false; }
    await select(cell, opts);
    return true;
  }

  function parseHash(h) {
    const parts = (h || '').replace(/^#\/?/, '').split('/').filter(Boolean);
    if (!parts.length) return { root: true };
    if (parts[0] === 'E' && parts.length === 3) return { ghost: { p: +parts[1], g: +parts[2] } };
    const e = state.index.layout.find((x) => x.symbol.toLowerCase() === parts[0].toLowerCase() || String(x.Z) === parts[0]);
    if (!e) return null;
    const out = { Z: e.Z };
    if (parts[1]) out.charge = fromRoman(parts[1].toUpperCase()) || parseInt(parts[1], 10) || undefined;
    if (parts[2]) out.l = parseL(parts[2]);
    if (parts[3]) out.mult = parseInt(parts[3], 10);
    return out;
  }

  async function applyHash(fly = true, ms = 650, reveal = true) {
    const h = location.hash;
    if (h === state.lastHash) return;
    const p = parseHash(h);
    if (!p || p.root) return select(rootNode, { fly, ms, reveal });
    if (p.ghost) {
      const g = state.ghosts.find((x) => x.p === p.ghost.p && x.g === p.ghost.g);
      return g ? select({ kind: 'ghost', ...g }, { fly, ms, reveal }) : select(rootNode, { fly, ms, reveal });
    }
    return goToPath(p.Z, p.charge, p.l, p.mult, { fly, ms, reveal });
  }

  // ---------------------------------------------------------------- crumbs
  function renderCrumbs(node) {
    const path = pathOf(node);
    const el = $('#crumbs');
    el.innerHTML = '';
    path.forEach((n, i) => {
      if (i) { const sep = document.createElement('span'); sep.className = 'sep'; sep.textContent = '›'; el.appendChild(sep); }
      const b = document.createElement('button');
      b.type = 'button';
      b.textContent = n.kind === 'ion' ? roman(n.charge) : n.kind === 'channel' ? `ℓ=${n.l} ${LSYM[n.l] || ''}`.trim() : n.kind === 'cell' ? `mult ${n.mult}` : label(n);
      if (i === path.length - 1) b.classList.add('is-current');
      b.addEventListener('click', () => select(n));
      el.appendChild(b);
    });
  }

  // ---------------------------------------------------------------- inspector
  const AX = {};
  function axisStatus(name) { return AX[name] || null; }
  function badge(status, tip) {
    if (!status) return `<span class="badge st-NONE" title="${esc(tip || 'no status carried')}">—</span>`;
    const t = tip || ((state.index.status_legend || {})[status] || '');
    return `<span class="badge st-${esc(status)}" title="${esc(t)}">${esc(status)}</span>`;
  }
  function row(k, v, status, tip, plain) {
    const val = plain ? `<span class="plain">${v}</span>` : v;
    return `<div class="f-k">${esc(k)}</div><div class="f-v">${val} ${status === undefined ? '' : badge(status, tip)}</div>`;
  }
  function axRow(k, v, axis, plain) {
    // a value the record does not carry (null, shown as a dash) takes no axis status: the axis
    // table describes the value, not its absence
    if (v === null || v === undefined || v === '—') return row(k, '—', null, 'not carried in this record', plain);
    const a = axisStatus(axis);
    return row(k, v, a ? a.status : null, a ? `${a.status} — ${a.source}` : undefined, plain);
  }
  function section(title, body, note) {
    return `<section class="blk"><h3>${esc(title)}${note ? `<span class="h-note">${note}</span>` : ''}</h3>${body}</section>`;
  }
  function actions(node, record) {
    const raw = JSON.stringify(record, null, 1);
    const cite = citation(node);
    return `<div class="actions">
      <button type="button" data-act="copy-json">Copy JSON</button>
      <button type="button" data-act="copy-link">Copy link</button>
      <button type="button" data-act="toggle-raw">Raw record</button>
      ${node.Z ? `<a href="${DATA}elements/${node.Z}.js" target="_blank" rel="noopener">data/elements/${node.Z}.js</a>` : ''}
    </div>
    <pre class="raw" hidden>${esc(raw)}</pre>
    <div class="cite">${esc(cite)}</div>`;
  }
  function citation(node) {
    const m = state.index.meta || {};
    const src = (state.index.sources || []).map((s) => `${s.file.split('/').pop()} ${s.md5_measured ? s.md5_measured.slice(0, 8) : '?'}`).join(', ');
    return `${pathText(node)}. The Method Index, read by tools/populate.py and written by tools/webindex.py; commit ${m.commit || '?'}, built ${m.built || '?'}. Sources: ${src}. ${location.origin && location.origin !== 'null' ? location.origin : ''}${location.pathname}${hashOf(node)}`;
  }

  function renderInspector(node) {
    const body = $('#inspector-body');
    let html = '';
    switch (node.kind) {
      case 'root': html = renderRoot(); break;
      case 'element': html = renderElement(node); break;
      case 'ghost': html = renderGhost(node); break;
      case 'ion': html = renderIon(node); break;
      case 'channel': html = renderChannel(node); break;
      case 'cell': html = renderCell(node); break;
    }
    body.innerHTML = html;
    $('#status').textContent = pathText(node);
    $('#btn-up').disabled = node.kind === 'root';
    bindGo(body);
    body.querySelectorAll('[data-act]').forEach((b) => b.addEventListener('click', () => {
      const act = b.dataset.act;
      if (act === 'toggle-raw') { const pre = body.querySelector('pre.raw'); pre.hidden = !pre.hidden; }
      if (act === 'copy-json') copyText(body.querySelector('pre.raw').textContent, b);
      if (act === 'copy-link') copyText(location.href.split('#')[0] + hashOf(node), b);
      if (act === 'open-prov') $('#dlg-provenance').showModal();
      if (act === 'color-limit') setCellColor('limit');
      if (act === 'color-grade') setCellColor('grade');
      if (act === 'helium-toggle') setHelium(state.heliumAt === 2 ? 18 : 2);
      if (act === 'lattice-view') { if (state.elementView !== 'lattice') setElementView('lattice'); else select(node, { setHash: false, reveal: false }); revealCanvas(); }
      if (act === 'nest-view') { setElementView('nest'); revealCanvas(); }
    }));
  }

  // The alternative placement: helium at group 2, E = 20. The frames are rebuilt
  // from the build's own two closures; nothing is recomputed here.
  function setHelium(at) {
    if (at === state.heliumAt) return;
    state.heliumAt = at;
    buildFrames();
    if (state.scene && state.scene.kind === 'table') { state.scene = buildTableScene(); if (state.orbit) fitOrbit(state.scene, state.orbit); }
    updateCaption();
    const sel = state.selected || rootNode;
    if (sel.kind === 'ghost') {
      const g = state.ghosts.find((x) => x.p === sel.p && x.g === sel.g);
      select(g ? { kind: 'ghost', ...g } : rootNode, { setHash: false, reveal: false });
    } else select(sel, { setHash: false, reveal: false });
    requestDraw();
  }
  function bindGo(root) {
    root.querySelectorAll('[data-go]').forEach((el) => {
      const go = () => {
        const [Z, c, l, m] = el.dataset.go.split('/');
        goToPath(+Z, c === '' || c === undefined ? undefined : +c, l === '' || l === undefined ? undefined : +l, m === '' || m === undefined ? undefined : +m);
      };
      el.addEventListener('click', go);
      if (el.tagName === 'TR') {           // a table row is not focusable by itself
        el.tabIndex = 0; el.setAttribute('role', 'link');
        el.addEventListener('keydown', (ev) => { if (ev.key === 'Enter' || ev.key === ' ') { ev.preventDefault(); go(); } });
      }
    });
  }
  function copyText(t, btn) {
    const done = () => { const old = btn.textContent; btn.textContent = 'Copied'; setTimeout(() => { btn.textContent = old; }, 1200); };
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(t).then(done, () => { btn.textContent = 'Copy failed'; });
    else btn.textContent = 'Copy unavailable';
  }
  const caveat = (id) => { const c = (state.index.caveats || []).find((v) => v.id === id); return c ? c.text : ''; };
  // E = admitted − held carries one status wherever the data's own figure is quoted: PINNED, as
  // the generator's fixtures pin the structural half (90 held, 126 admitted, E = 36) and as
  // cypher.py's selftest asserts it; the closure solver's own E over any cell set is the same row.
  const E_TIP = 'admitted − held; the drawn layout against ℛ, the structural half the fixtures pin';

  function renderRoot() {
    const ix = state.index, t = ix.totals, c = ix.closure;
    const lat = ix.lattice;
    const layoutNote = state.layout === 'lattice' && lat
      ? `Λ_spectra as a lattice, the way the source figure draws it: every element a slab at its Z, ionisation stage up, ℓ into the page — <b>${lat.sites.toLocaleString()}</b> sites, <b>${lat.known.length.toLocaleString()}</b> known cells (${lat.counts.measured} measured, ${lat.counts.exact} exact) drawn as cubes, the rest the faint body of each slab. The measured wedge sits at low Z and low ℓ. Drag to rotate, wheel or pinch to zoom, tap a slab for its element.`
      : state.layout === 'table' || state.layout === 'table3d'
      ? `The drawn periodic layout: <b>${c.held}</b> cells held, <b>${c.admitted}</b> admitted by ℛ, <b>E = ${c.E}</b>. The ${c.E} are the gaps in the short periods, drawn as tinted ghosts each labelled with its subshell; ${c.set_aside} f-block elements are set aside below the table.`
      : `Janet's coordinate: the cell is (n+ℓ, ℓ) of the differentiating electron, and on it E = 0. Elements without a cell (Z &gt; 108) sit on the bottom row.`;
    return `<div class="kind">the index</div>
      <h2 class="node-title">${esc(ix.meta.title)}</h2>
      <p class="node-sub">${esc(ix.meta.subtitle)}</p>
      <p class="note">${layoutNote}</p>
      <div class="stats">
        <div class="stat"><b>${t.populated}</b><span>elements populated ${badge('DERIVED', 'count of the elements the observed configurations table carries')}</span></div>
        <div class="stat"><b>${t.csv_only}</b><span>spectra rows only (Z 109–120) ${badge('DERIVED', 'count of the elements COORDINATES-2.13 carries beyond the observed configurations')}</span></div>
        <div class="stat"><b>${t.rows.toLocaleString()}</b><span>channel cells ${badge('READ', 'COORDINATES-2.13 rows')}</span></div>
        <div class="stat"><b>${t.measured}</b><span>measured ${badge('DERIVED', 'count over COORDINATES-2.13\'s grade column')}</span></div>
        <div class="stat"><b>${t.exact}</b><span>exact ${badge('DERIVED', 'count over COORDINATES-2.13\'s grade column')}</span></div>
        <div class="stat"><b>${t.computed.toLocaleString()}</b><span>computed ${badge('DERIVED', 'count over COORDINATES-2.13\'s grade column')}</span></div>
      </div>
      ${section('How to read it', `<p class="note">Tap any element: its ions appear inside it in spectroscopic order (I is neutral), joined by the Λ₈ ionisation ladder; each ion opens into its ℓ channels, each channel into its cells, one per multiplicity, coloured by grade. Every value in this plate carries the status the data gives it: ${Object.keys(ix.status_legend || {}).map((s) => badge(s)).join(' ')}. The explorer computes nothing; the solver suite below does, and every solver carries a selftest.</p>`)}
      ${section('Closure of this layout', `<div class="fields">
        ${row('index', esc(c.index), 'PINNED', 'the drawn layout', true)}
        ${row('operator', esc(c.operator), 'PINNED', 'the order operator', true)}
        ${row('held', c.held, 'PINNED', 'the drawn layout: ninety main-table cells')}
        ${row('admitted', c.admitted, 'PINNED', 'ℛ over the layout')}
        ${row('E', c.E, 'PINNED', E_TIP)}
        ${c.decomposition ? row('the thirty-six', `${c.decomposition.forbidden} forbidden by ℓ ≤ n−1 (1d, 1p, 2d) + ${c.decomposition.deferred} deferred (3d, and helium's slot)`, 'READ', 'the stated decomposition — tap a ghost for its definition') : ''}
        ${c.placement ? row('helium at 2 instead', `E = ${c.placement.helium_at_2.E}, priced at ${c.placement.priced} cells`, 'READ', c.placement.source) : ''}
        ${row('set aside', c.set_aside, 'PINNED', 'the lanthanides and actinides, set aside below the table')}
      </div>${c.placement && (state.layout === 'table' || state.layout === 'table3d') ? `<div class="actions"><button type="button" data-act="helium-toggle">${state.heliumAt === 2 ? 'Draw helium at group 18 (IUPAC)' : 'Draw helium at group 2 (E = ' + c.placement.helium_at_2.E + ')'}</button></div>` : ''}`)}
      ${(() => { const rel = ix.relativistic, lim = ix.limits; if (!rel && !lim) return ''; let b = ''; if (rel) { const paper = (rel.sources || {}).paper || {}; b += `<div class="fields">${row('displaced at c → ∞', esc((rel.eleven || []).map((x) => x.symbol).join(', ')), 'READ', `${(paper.title || 'the Löwdin paper')} L${paper.eleven_line}`, true)}${row('instrument', 'not held — the construction is record-carried; nothing here computes it', null, esc((rel.instrument && rel.instrument.note) || ''), true)}${rel.walk && rel.walk.summary && rel.walk.summary.compare ? row('the walk, reconstructed', esc(`${rel.walk.summary.compare.displaced.length} displaced at c → ∞ in the ${rel.walk.primary === 'hf' ? 'Hartree–Fock' : 'local-exchange'} field (${rel.walk.summary.compare.displaced.map((d) => d.symbol).join(', ') || 'none'}); ${rel.walk.summary.compare.in_eleven.length} of the record's eleven`), 'RECONSTRUCTED', 'tools/lowdin_walk.py over LOWDIN-WALK.tsv: the record\'s construction rebuilt from its statement; placed beside the record, never in its place', true) : ''}</div>`; } if (lim) { b += `<p class="note" style="margin-top:8px">Every cell carries the bound the csv records; by kind: ${(lim.kinds || []).map((k) => `<span class="dot dot-lim-${k.kind}"></span>${esc(LIMIT_LABEL[k.kind] || k.kind)} ${k.count.toLocaleString()}`).join(' · ')} ${badge('DERIVED', 'kind by the stated rule; the note is READ')}</p><div class="actions"><button type="button" data-act="color-limit">Colour cells by limit</button><button type="button" data-act="color-grade">by grade</button></div>`; } return section('The relativistic limit and the bounds', b); })()}
      ${section('Caveats that travel with every value', `<ul class="note">${(ix.caveats || []).map((v) => `<li>${esc(v.text)}</li>`).join('')}</ul>`)}
      <div class="actions"><button type="button" data-act="open-prov">Provenance and sources</button></div>
      <div class="cite">${esc(citation(rootNode))}</div>`;
  }

  function renderGhost(node) {
    const c = state.index.closure;
    const d = node.def || (c.denied_cells || []).find((x) => x.p === node.p && x.g === node.g) || null;
    const dec = c.decomposition || {};
    const pl = c.placement || null;
    const heSlot = d && d.p === 1 && d.g === 2;
    const title = d ? (heSlot ? 'Period 1, group 2 — the slot helium vacates' : `Period ${node.p}, group ${node.g} — ${esc(d.subshell)}, ${d.class}`) : `Period ${node.p}, group ${node.g}`;
    const kindLine = d ? (d.class === 'forbidden' ? 'admitted, not held · forbidden by ℓ ≤ n−1' : 'admitted, not held · deferred') : 'admitted, not held';
    const defn = d ? (d.class === 'forbidden'
      ? `<p class="note">The layout puts this cell in period ${node.p}, and its group ${node.g} carries ℓ = ${d.l} (${LSYM[d.l]}: ℓ is fixed by group — s at 1–2, d at 3–12, p at 13–18). A ${esc(d.subshell)} orbital needs ℓ ≤ n − 1 = ${d.n - 1}, and ℓ = ${d.l} fails it: the hydrogenic radial solution has no such state. The cell could never hold an element. It is one of the twenty-five that two constraints cast as a shadow.</p>`
      : heSlot
        ? `<p class="note">Helium sits at group 18 in the drawn layout, and the cell it vacates — period 1, group 2 — carries ℓ = 0, which satisfies ℓ ≤ n − 1 = 0. So this cell is deferred, not forbidden: it could hold an element, and the only reason it holds none is where helium is drawn. That is also why 1p contributes five cells and not six. The alternative placement prices the choice: with helium at group 2, E falls from 36 to 20.</p>`
        : `<p class="note">Group ${node.g} carries ℓ = 2 (d), and period ${node.p} gives n = ${d.n}, so this is a ${esc(d.subshell)} cell and ℓ = 2 ≤ n − 1 = ${d.n - 1} holds: the orbital exists. It stands empty because the Madelung order fills 3d after 4s, so the ten 3d elements are drawn in period 4. Real, and deferred: one of the eleven cells that could hold an element and do not.</p>`)
      : `<p class="note">ℛ, the order operator, admits this cell: the layout has a period ${node.p} and a group ${node.g}, so the downward closure of the held set reaches it. The drawn table does not hold it.</p>`;
    return `<div class="kind">${kindLine}</div>
      <h2 class="node-title">${title}</h2>
      <p class="node-sub">one of the ${c.E} cells that make E = ${c.E}${state.heliumAt === 2 ? ' · drawn with helium at group 2 (E = ' + (pl ? pl.helium_at_2.E : '?') + ')' : ''}</p>
      ${defn}
      ${d ? section('Definition', `<div class="fields">
        ${row('cell', `(${node.p}, ${node.g})`, 'DERIVED', 'admitted − held')}
        ${row('subshell', esc(d.subshell), 'READ', 'the thirty-six decompose as subshells of their rows; ℓ by group: s at 1–2, d at 3–12, p at 13–18')}
        ${row('n, ℓ', `${d.n}, ${d.l} (${LSYM[d.l]})`, 'DERIVED', 'n is the period; ℓ is fixed by the group')}
        ${row('ℓ ≤ n − 1', d.class === 'forbidden' ? '<span class="bad">fails</span>' : '<span class="ok">holds</span>', 'PINNED', 'the hydrogenic radial solution')}
        ${row('class', d.class, 'DERIVED', 'from the bound; the totals 25 + 11 are READ and the derivation is asserted against them')}
        ${row('why', esc(d.reason), null, undefined, true)}
      </div>`) : ''}
      ${section('The thirty-six', `<div class="fields">
        ${row('forbidden by ℓ ≤ n−1', dec.forbidden !== undefined ? `${dec.forbidden} — 1d (10), 1p (5), 2d (10)` : '—', 'READ', '25 + 11, not 26 + 10, and the discrepancy is helium')}
        ${row('real but deferred', dec.deferred !== undefined ? `${dec.deferred} — 3d (10), and period 1 group 2` : '—', 'READ', 'the stated decomposition')}
        ${row('held', c.held, 'PINNED', 'the drawn layout')}
        ${row('admitted', c.admitted, 'PINNED', 'ℛ over the layout')}
        ${row('E', c.E, 'PINNED', E_TIP)}
        ${row('not the void', 'the void is L.void, chapter 10\'s box-minus-lattice remainder, and is not these cells', null, dec.not_the_void || '', true)}
      </div>`)}
      ${pl ? section('Where helium is drawn', `<p class="note">E is not a property of the elements; it is a property of where helium is drawn. With helium at group 18 the first row's gaps are admitted, ${pl.helium_at_18.E} in all; with helium at group 2, φ̂(group | period ≤ 1) drops from 18 to 2 and the whole first row disappears, ${pl.helium_at_2.E}. E prices the choice at ${pl.priced} cells.</p>
        <div class="fields">
          ${row('helium at 18', `E = ${pl.helium_at_18.E}`, 'READ', pl.source)}
          ${row('helium at 2', `E = ${pl.helium_at_2.E}`, 'READ', pl.source)}
          ${row('recomputed here', `${pl.helium_at_18.E} and ${pl.helium_at_2.E}`, 'DERIVED', 'ℛ (cypher.op_order) over the ninety cells, helium moved and nothing else, at build; the closure solver\'s selftest reproduces both in the browser')}
        </div>
        <div class="actions"><button type="button" data-act="helium-toggle">${state.heliumAt === 2 ? 'Draw helium at group 18 (IUPAC)' : 'Draw helium at group 2 (E = ' + pl.helium_at_2.E + ')'}</button></div>`, badge('READ', 'the priced alternative')) : ''}
      <div class="cite">${esc(citation(node))}</div>`;
  }

  function latticeSection(e, rec) {
    const lat = state.index.lattice || {};
    const n = rec ? rec.channels.reduce((a, ch) => a + ch.measured.length, 0) : (e.counts ? e.counts.rows : 0);
    const k = rec ? rec.channels.reduce((a, ch) => a + ch.measured.filter((m) => m.grade !== 'computed').length, 0) : ((e.counts ? e.counts.measured + e.counts.exact : 0));
    const on = state.view === 'lattice' && state.scene && state.scene.kind === 'element' && state.scene.Z === e.Z;
    return section('The lattice', `<p class="note">${esc(e.symbol)} as its slab of Λ_spectra, on the record's own axes: ionisation stage up, ℓ into the page, one node per cell, the cells of a site side by side where it holds two multiplicities. Nodes carry the same marks as the nested view — a filled sphere for a measured cell, a ringed disc for an exact one, a small grey dot for a computed one — and the ladder climbs the front edge, one rung per recorded step.</p>
      <div class="fields">
        ${row('axes', 'element across · stage up · ℓ into the page', 'READ', lat.source || 'Index of Indices, Figure 6')}
        ${row('cells drawn', `${n.toLocaleString()} (${k} known)`, 'DERIVED', 'one cube per row of COORDINATES-2.13 for this element; nothing computed')}
        ${row('the source renderer', `cubes of edge ${(lat.cube || {}).known || 0.86} known, ${(lat.cube || {}).faint || 0.3} unmeasured`, 'READ', ((lat.cube || {}).note || '') + '; drawn here as nodes of the same footprint, in the nested view\'s marks')}
      </div>
      <div class="actions"><button type="button" data-act="lattice-view">${on ? 'Rotate it on the canvas' : 'Open the lattice'}</button><button type="button" data-act="nest-view">${state.elementView === 'nest' ? 'Nested circles (shown)' : 'Show as nested circles'}</button></div>`);
  }
  function relSection(e, rec) {
    const rel = state.index.relativistic;
    if (!rel) return '';
    return relRecordSection(e, rel) + walkSection(e, rec, rel);
  }

const WALK_FIELD_LABEL = { hf: 'Hartree–Fock, non-local exchange (the paper\'s field, rebuilt)', lx: 'local exchange (Hartree–Fock–Slater)' };
  function walkSection(e, rec, rel) {
    // the reconstruction (tools/lowdin_walk.py over LOWDIN-WALK.tsv), RECONSTRUCTED, beside the
    // record's READ result and never in its place; one block per field, the record's own
    // (Hartree–Fock) first where it is held
    const walk = rel.walk;
    if (!walk) return '';
    const wr = rec && rec.walk;
    if (!wr || !wr.fields) return section('The walk, reconstructed', `<p class="note">no row at Z = ${e.Z}: the walk runs Z = 2 to 120 (${esc(walk.table.file)})</p>`, badge('RECONSTRUCTED', walk.field));
    const fmtD = (v) => (v === null || v === undefined) ? '—' : v.toFixed(6);
    const spec = (r) => r.spectrum.slice(0, 6).map((x) => `${esc(x.channel)} ${x.D.toFixed(5)}`).join(' · ') + (r.spectrum.length > 6 ? ' · …' : '');
    const order = [walk.primary].concat(Object.keys(wr.fields).filter((k) => k !== walk.primary));
    let body = '';
    for (const fld of order) {
      const wf = wr.fields[fld];
      if (!wf) continue;
      const one = (k, label) => {
        const r = wf[k];
        if (!r) return row(label, 'no row', null, 'the walk carries no row here');
        return row(label, `<strong>${esc(r.entrant)}</strong> <span class="plain">D = ${fmtD(r.D_ent)} Ha · runner-up ${esc(r.runner_up)} by ${fmtD(r.margin)} · in the field of (Z = ${e.Z}, ${esc(r.cfg_prev)}) · candidates: ${spec(r)}</span>`, 'RECONSTRUCTED', `tools/lowdin_walk.py, field ${fld}: scf ${r.scf_iterations} iterations${r.converged ? ', converged' : ', NOT CONVERGED'}; the depth is one electron's eigenvalue in the frozen field`);
      };
      const c1 = wf.c137;
      body += `<div class="fields">
        ${row('field', esc(WALK_FIELD_LABEL[fld] || fld), 'RECONSTRUCTED', esc(((walk.fields || {})[fld] || {}).name || ''), true)}
        ${one('c137', 'entrant at c = 137.035999')}
        ${one('cinf', 'entrant at c → ∞')}
        ${row('displaced in this field', wf.displaced ? `yes <span class="rel-tag walk-tag">entrants differ</span>` : 'no', 'RECONSTRUCTED', 'whether the two settings\' entrants differ at this Z in this field')}
        ${c1 && c1.observed_gain !== '-' ? row('observed gain at this Z', `${esc(c1.observed_gain)} — the c = 137 entrant ${c1.agree === 'yes' ? 'agrees' : 'differs'}`, 'READ', 'the observed configurations table: the channel that gained an electron from Z − 1 to Z. The chain never moves an electron, so a rearranged step (Cr, Cu, Pd, La, Gd, Th …) reads as a disagreement under this reading') : ''}
      </div>`;
    }
    body += `<div class="fields">${e.relativistic ? row('in the record', 'one of the eleven the Löwdin paper displaces', 'READ', 'the Löwdin paper') : row('in the record', 'not among the eleven', 'READ', 'the Löwdin paper')}</div>
      <p class="note">${esc(caveat('walk-reconstructed'))}</p>`;
    return section('The walk, reconstructed', body, badge('RECONSTRUCTED', `${walk.instrument} over ${walk.table.file}, md5 ${walk.table.md5.slice(0, 12)}; primary field ${walk.primary}`));
  }

  function relRecordSection(e, rel) {
    const src = rel.sources || {}, paper = src.paper || {};
    const cite = `${(paper.title || 'the Löwdin paper')} L${paper.eleven_line}; the SCF audit`;
    const hit = (rel.eleven || []).find((x) => x.Z === e.Z);
    const fig = (state.index.figures || [])[0];
    let body = `<div class="fields">
      ${row('displaced at c → ∞', hit ? `yes <span class="rel-tag">one of the eleven</span>` : 'no', 'READ', hit ? cite : cite + ': not among the eleven')}
      ${hit ? row('observed configuration', esc(hit.configuration || '—'), 'READ', 'the SCF audit over the observed configurations table') : ''}
      ${hit ? row('entrant channel', esc(hit.entrant || '—'), 'READ', 'the SCF audit: the channel the relativistic walk enters at this Z') : ''}
      ${e.Z === 90 && rel.thorium ? row('thorium', esc(rel.thorium), 'READ', `${(paper.title || 'the Löwdin paper')} L${paper.thorium_line}`, true) : ''}
      ${row('c', rel.c, 'READ', esc(rel.construction || 'the one admitted constant'))}
      ${row('instrument', 'not held — nothing computed here', null, esc((rel.instrument && rel.instrument.note) || ''), true)}
    </div>`;
    if (hit || e.Z === 90) {
      body += `<div class="callout is-plain">${esc(rel.statement || '')}</div>`;
      if (fig && fig.file) body += `<figure class="plate-fig"><a href="data/${esc(fig.file)}" target="_blank" rel="noopener" title="open the figure at full size"><img src="data/${esc(fig.file)}" alt="${esc(fig.caption || 'Figure 5')}" loading="lazy"></a><figcaption>${esc(fig.caption || '')} · md5 ${esc((fig.md5 || '').slice(0, 12))} as the ledger records ${badge('READ', 'the figure as the repository holds it')}</figcaption></figure>`;
    }
    return section('Relativistic limit', body, badge('READ', 'the paper\'s own result; the construction is not held'));
  }

  function limitsSection(e) {
    const lim = state.index.limits;
    if (!lim || !e.limits) return '';
    const total = Object.values(e.limits).reduce((a, b) => a + b, 0);
    const rows = LIMIT_KIND_ORDER.filter((k) => e.limits[k]).map((k) => {
      const r = limitRule(k);
      return `<div class="f-k"><span class="dot dot-lim-${k}"></span>${esc(LIMIT_LABEL[k] || k)}</div><div class="f-v">${e.limits[k].toLocaleString()} ${badge('DERIVED', r ? r.meaning : 'kind by the stated rule')}</div>`;
    }).join('');
    return section('Limits', `<p class="note">The bound the csv records on each of the element's ${total.toLocaleString()} cells, by kind. The note is ${badge('READ', lim.source || 'COORDINATES-2.13, bound column')}; the kind is ${badge('DERIVED', 'by the rule data/index.js carries; see the cell plate for the rule')}.</p>
      <div class="fields">${rows}</div>
      <div class="actions"><button type="button" data-act="color-limit">Colour cells by limit</button><button type="button" data-act="color-grade">by grade</button></div>`);
  }

  function renderElement(node) {
    const e = node.e;
    const rec = state.elements.get(node.Z);
    const head = `<div class="kind">element · Z = ${e.Z}</div>
      <h2 class="node-title">${esc(e.symbol)} <span class="note" style="font-family:var(--font-body);font-size:15px;font-weight:400">${esc(e.name || '')}</span></h2>
      <p class="node-sub">${e.populated ? `${esc(e.shells)} · ${esc(e.level)}` : 'spectra rows only'}</p>`;
    const loadErr = state.loadErrors.get(node.Z);
    const loadNote = () => loadErr ? `<div class="callout is-finding">${esc(loadErr)}</div>` : '<p class="note">loading the element …</p>';
    if (!rec && !loadErr) ensureElement(node.Z).then(() => { if (state.selected === node) renderInspector(node); }).catch(() => { if (state.selected === node) renderInspector(node); });
    if (!e.populated) {
      const ions = rec ? state.trees.get(node.Z).ions : null;
      return head + `<div class="callout is-finding">${esc(caveat('above-108'))}</div>
        ${section('Layout', `<div class="fields">
          ${axRow('period', e.period, 'period')}
          ${axRow('group', fmt(e.group), 'group')}
          ${row('configuration', 'none carried', null, undefined, true)}
        </div>`)}
        ${section('Spectra rows', `<div class="fields">
          ${row('cells', e.counts.rows, 'DERIVED', "counts over the record's COORDINATES-2.13 rows")}
          ${row('measured', e.counts.measured, 'DERIVED', "counts over the record's COORDINATES-2.13 rows")}
          ${row('ions', e.counts.ions, 'DERIVED', "counts over the record's COORDINATES-2.13 rows")}
        </div>`)}
        ${ions ? section('Ions', `<div class="chips">${ions.map((i) => `<button type="button" class="chip is-csv" data-go="${node.Z}/${i.charge}">${esc(e.symbol)} ${roman(i.charge)}</button>`).join('')}</div>`) : loadNote()}
        ${walkSection(e, rec, state.index.relativistic || {})}
        ${limitsSection(e)}
        ${rec ? actions(node, { Z: rec.Z, symbol: rec.symbol, populated: rec.populated, note: rec.note, channels: rec.channels.length }) : ''}`;
    }
    let html = head;
    html += section('Identity', `<div class="fields">
      ${axRow('Z', e.Z, 'Z')}
      ${axRow('symbol', esc(e.symbol), 'symbol')}
      ${axRow('ground shells', esc(e.shells), 'configuration')}
      ${axRow('ground level', esc(e.level), 'level')}
      ${rec ? row('electron count', `${rec.electron_count} ${rec.electron_count_ok ? '<span class="ok">= Z</span>' : '<span class="bad">≠ Z</span>'}`, 'DERIVED', 'occupancies summed against Z') : ''}
      ${row('name', esc(e.name || '—'), null, 'IUPAC label; not a figure of the index', true)}
    </div>`);
    html += section('Layout', `<div class="fields">
      ${axRow('period', e.period, 'period')}
      ${axRow('group', e.set_aside ? 'set aside' : e.group, 'group')}
      ${axRow('block', esc(e.block || '—'), 'block')}
      ${axRow('Janet cell (n+ℓ, ℓ)', e.janet ? `(${e.janet[0]}, ${e.janet[1]})` : '—', 'janet cell')}
      ${rec ? row('cell held', rec.closure.cell_held ? 'yes' : (e.set_aside ? 'set aside' : 'no'), 'PINNED', 'the drawn layout against ℛ') : ''}
      ${rec && rec.closure.denied_in_this_period.length ? row('denied in this period', `groups ${rec.closure.denied_in_this_period.join(', ')}`, 'DERIVED', 'admitted − held, this period') : ''}
    </div>`);
    html += latticeSection(e, rec);
    if (rec) {
      html += section('Configuration', `<div class="tbl-wrap"><table class="t"><thead><tr><th>subshell</th><th class="num">n</th><th class="num">ℓ</th><th class="num">occ</th><th class="num">cap</th><th class="num">n+ℓ</th><th>full</th></tr></thead><tbody>
        ${rec.configuration.map((c) => `<tr><td>${esc(c.subshell)}</td><td class="num">${c.n}</td><td class="num">${c.l}</td><td class="num">${c.occupancy}</td><td class="num">${c.capacity}</td><td class="num">${c['n+l']}</td><td>${c.full ? '●' : '○'}</td></tr>`).join('')}
      </tbody></table></div>`, `${badge('READ', 'shells: the observed configurations table')} ${badge('DERIVED', 'n, ℓ, occupancy, n+ℓ')} ${badge('PINNED', 'capacity 2(2ℓ+1), Pauli')}`);
      const tree = state.trees.get(node.Z);
      html += section('Ions', `<p class="note">${e.counts.ions} spectroscopic stages, ${e.counts.channels} channels, ${e.counts.rows.toLocaleString()} cells; ${e.counts.measured} measured, ${e.counts.exact} exact, ${e.counts.computed.toLocaleString()} computed ${badge('DERIVED', 'counts over the record\'s COORDINATES-2.13 rows')}</p>
        <div class="chips">${tree.ions.map((i) => {
          const nM = i.nMeasured;
          return `<button type="button" class="chip" data-go="${node.Z}/${i.charge}" title="${nM} measured">${esc(e.symbol)} ${roman(i.charge)}${nM ? ` <span class="dot dot-measured" style="margin:0 0 0 4px"></span>` : ''}</button>`;
        }).join('')}</div>`);
      if (rec.lambda8 && rec.lambda8.length) {
        html += section('Λ₈ ionisation ladder', `<div class="callout">${esc(caveat('lambda8-mapping'))}</div>
          <p class="note">Drawn on the canvas as the glowing lines between consecutive ions: ${rec.lambda8.length} steps, each linking the ion at charge − 1 to the ion at charge.</p>
          <div class="tbl-wrap"><table class="t"><thead><tr><th>step</th><th>stage</th><th>transition</th><th>(n, ℓ, k, q, e, f, g, 2S)</th><th>7.1</th><th>within 7.4 caps</th></tr></thead><tbody>
          ${rec.lambda8.map((s, i) => {
            const holds = s.constraints.filter((c) => c.holds).length;
            const within = Object.values(s.within_caps).every(Boolean);
            const need = Object.entries(s.caps_needed).filter(([k, v]) => v > state.index.caps[k]).map(([k, v]) => `${k}≥${v}`).join(' ');
            return `<tr class="is-link" data-go="${node.Z}/${s.charge}"><td class="num">${i + 1}</td><td>${roman(s.charge)}</td><td>${esc(s.from)} → ${esc(s.to)}</td><td>(${s.cell.map((v) => v === null ? '·' : v).join(', ')})</td><td>${holds}/${s.constraints.length}</td><td>${within ? 'within' : `<span class="bad">outside</span> ${esc(need)}`}</td></tr>`;
          }).join('')}
          </tbody></table></div>`, badge('RECONSTRUCTED', (axisStatus('Lambda_8 cell') || {}).source));
      }
      html += relSection(e, rec) + limitsSection(e) + elementReferences(e, rec);
      html += actions(node, { ...rec, channels: `${rec.channels.length} channels — see the ion nodes` });
    } else {
      html += loadNote();
    }
    return html;
  }

  function renderIon(node) {
    const sym = symbolOf(node.Z);
    const e = state.index.layout.find((x) => x.Z === node.Z);
    const populated = e.populated;
    const first = node.rec[0];
    const rec = state.elements.get(node.Z);
    const nSteps = rec && rec.lambda8 ? rec.lambda8.length : 0;
    let html = `<div class="kind">ion · spectroscopic stage ${roman(node.charge)}</div>
      <h2 class="node-title">${esc(sym)} ${roman(node.charge)}</h2>
      <p class="node-sub">Nₑ = ${first.Ne}${populated && first.core_symbol ? ` · core ${esc(first.core_symbol)} (${first.core_Ne} e⁻)` : ''}</p>`;
    html += section('Identity', `<div class="fields">
      ${axRow('charge', `${node.charge} (${roman(node.charge)})`, 'charge')}
      ${axRow('Nₑ', first.Ne, 'Ne')}
      ${populated ? row('core', `${esc(first.core_symbol || '—')} · ${first.core_Ne} e⁻`, 'DERIVED', 'Nₑ − 1 electrons, the observed configuration of that count') : ''}
    </div>`);
    html += section('Channels', `<div class="tbl-wrap"><table class="t"><thead><tr>
      <th>ℓ</th><th class="num">p</th><th class="num">n₀</th><th class="num">B</th><th class="num">C(Z)</th><th class="num">δ eq.</th><th class="num">cells</th><th class="num">meas.</th></tr></thead><tbody>
      ${node.channels.map((ch) => {
        const r = ch.rec, nM = ch.nMeasured;
        return `<tr class="is-link" data-go="${node.Z}/${node.charge}/${ch.l}"><td>${LSYM[ch.l] || ch.l} <span class="note">ℓ=${ch.l}</span></td><td class="num">${fmt(r.p)}</td><td class="num">${fmt(r.n0)}</td><td class="num">${fmt(r.B_computed)}</td><td class="num">${fmt(r.C_of_Z, 3)}</td><td class="num">${fmt(r.delta_equation)}</td><td class="num">${r.measured.length}</td><td class="num">${nM ? `<span class="dot dot-measured"></span>${nM}` : '—'}</td></tr>`;
      }).join('')}
    </tbody></table></div>
    <p class="note" style="margin-top:6px">${[['p', 'p'], ['n₀', 'n0'], ['B', 'B'], ['C(Z)', 'C(Z)'], ['δ equation', 'delta equation']].map(([k, ax]) => { const a = axisStatus(ax) || {}; return `${k} ${badge(a.status, a.source)}`; }).join(' · ')} · cells, meas. ${badge('DERIVED', 'counts over the record')}${populated ? '' : ' · none carried above Z = 108'}</p>`);
    if (node.step) {
      const s = node.step, cm = state.index.lambda_meaning || {};
      html += section('Λ₈ step at this stage', `<div class="callout is-accent">Step <b>${node.stepIndex + 1} of ${nSteps}</b> on the ladder: ${esc(s.from)} → ${esc(s.to)}, the line drawn from stage ${roman(node.charge - 1)} to stage ${roman(node.charge)} — the bright one while this ion is selected.</div>
        <div class="fields">
        ${row('transition', `${esc(s.from)} → ${esc(s.to)}`, 'RECONSTRUCTED', (axisStatus('Lambda_8 cell') || {}).source, true)}
        ${Object.entries(s.coords).map(([k, v]) => row(k, v === null ? '— (not carried)' : v, v === null ? null : 'RECONSTRUCTED', v === null ? 'the ion\'s term is not carried, so 2S may not be inferred' : (cm[k] || 'Λ₈ coordinate'))).join('')}
      </div>
      <div class="tbl-wrap" style="margin-top:8px"><table class="t"><thead><tr><th>constraint</th><th>holds</th><th>origin</th></tr></thead><tbody>
        ${s.constraints.map((c) => `<tr><td>${esc(c.rule)}</td><td class="${c.holds ? 'ok' : 'holds-false'}">${c.holds ? 'holds' : 'fails'}</td><td class="plain" style="font-family:var(--font-body)">${esc(c.origin)}${c.rule === '2S <= k' && s.coords['2S'] === null ? ' — 2S not carried; probed as 0, as populate.py does' : ''}</td></tr>`).join('')}
      </tbody></table></div>
      <div class="fields" style="margin-top:8px">
        ${row('within the standing caps', Object.entries(s.within_caps).map(([k, v]) => `${esc(k)}:${v ? '✓' : '✗'}`).join(' '), 'PINNED', (axisStatus('caps') || {}).source)}
        ${row('caps needed', Object.entries(s.caps_needed).map(([k, v]) => `${esc(k)}≥${esc(v)}`).join(' '), 'DERIVED', 'the cap at which this cell would be admitted')}
      </div>`);
    } else if (nSteps) {
      html += section('Λ₈ step at this stage', `<p class="note">${node.charge === 1 ? `No step arrives at stage I: it is the neutral atom the ladder's ${nSteps} steps leave from.` : 'The record carries no Λ₈ step arriving at this stage.'}</p>`);
    }
    html += actions(node, { Z: node.Z, charge: node.charge, channels: node.rec, lambda8_step: node.step });
    return html;
  }

  function renderChannel(node) {
    const r = node.rec, sym = symbolOf(node.Z);
    const populated = state.index.layout.find((x) => x.Z === node.Z).populated;
    let html = `<div class="kind">channel · ${esc(sym)} ${roman(node.charge)}</div>
      <h2 class="node-title">${esc(sym)} ${roman(node.charge)} <span style="font-family:var(--font-display)">${LSYM[node.l] || node.l}</span></h2>
      <p class="node-sub">ℓ = ${node.l} · ${r.measured.length} cells</p>`;
    html += section('The channel', `<div class="fields">
      ${row('ℓ', `${node.l} (${LSYM[node.l] || node.l})`, 'READ', 'COORDINATES-2.13, l column')}
      ${axRow('p', fmt(r.p), 'p')}
      ${axRow('n₀', fmt(r.n0), 'n0')}
      ${axRow('B = min(p, n₀−ℓ−1)', fmt(r.B_computed), 'B')}
      ${axRow('C(Z, ℓ)', fmt(r.C_of_Z, 3), 'C(Z)')}
      ${axRow('δ by equation', fmt(r.delta_equation), 'delta equation')}
    </div>${populated ? '' : `<div class="callout is-finding">${esc(caveat('above-108'))}</div>`}`);
    html += section('Cells, one per multiplicity', `<div class="tbl-wrap"><table class="t"><thead><tr><th class="num">2S+1</th><th class="num">δ</th><th>grade</th><th class="num">residual</th><th class="num">B (csv)</th><th>agrees</th><th>witness</th></tr></thead><tbody>
      ${node.cells.map((c) => {
        const m = c.rec;
        return `<tr class="is-link" data-go="${node.Z}/${node.charge}/${node.l}/${c.mult}"><td class="num">${c.mult}</td><td class="num">${fmtRead(m.delta)}</td><td><span class="dot dot-${esc(m.grade)}"></span>${esc(m.grade)}</td><td class="num">${fmt(m.residual)}</td><td class="num">${m.B_csv_is_not_a_bound ? '<span class="bad">not a bound</span>' : fmt(m.B_csv)}</td><td>${m.B_agrees === null ? '—' : m.B_agrees ? '<span class="ok">yes</span>' : '<span class="bad">no</span>'}</td><td>${m.witness === 'witnessed' ? '<span class="ok">witnessed</span>' : '<span class="note">unwitnessed</span>'}</td></tr>`;
      }).join('')}
    </tbody></table></div>
    <p class="note" style="margin-top:6px">δ ${badge('READ', 'COORDINATES-2.13, grade as the row states it')} · residual = δ − δ equation ${badge('DERIVED')} · B (csv) ${badge('READ', 'COORDINATES-2.13, B column')}</p>`);
    html += actions(node, r);
    return html;
  }

  function renderCell(node) {
    const m = node.rec, ch = node.parent.rec, sym = symbolOf(node.Z);
    const populated = (state.index.layout.find((x) => x.Z === node.Z) || {}).populated;
    let html = `<div class="kind">cell · ${esc(sym)} ${roman(node.charge)} ${LSYM[node.l] || node.l}</div>
      <h2 class="node-title">${esc(sym)} ${roman(node.charge)} ${LSYM[node.l] || node.l}, 2S+1 = ${node.mult}</h2>
      <p class="node-sub"><span class="dot dot-${esc(m.grade)}"></span>${esc(m.grade)} · ${esc(m.witness)}</p>
      ${populated ? '' : `<div class="callout is-finding">${esc(caveat('above-108'))}</div>`}`;
    html += section('Coordinates', `<div class="fields">
      ${axRow('Z', node.Z, 'Z')}
      ${axRow('charge', `${node.charge} (${roman(node.charge)})`, 'charge')}
      ${row('ℓ', node.l, 'READ', 'COORDINATES-2.13, l column')}
      ${row('2S+1', node.mult, 'READ', 'COORDINATES-2.13, mult column')}
    </div>`);
    html += section('The value', `<div class="fields">
      ${row('δ', fmtRead(m.delta), 'READ', 'COORDINATES-2.13, grade ' + m.grade + (m.grade === 'computed' ? ' (the csv\'s computed column)' : ''))}
      ${row('grade', esc(m.grade), 'READ', 'COORDINATES-2.13, grade column', true)}
      ${axRow('δ by equation', fmt(ch.delta_equation), 'delta equation')}
      ${row('residual', fmt(m.residual), m.residual === null ? null : 'DERIVED', 'δ − δ equation')}
      ${row('⌊δ⌋ ≤ B', m.floor_le_B === null ? '—' : m.floor_le_B ? '<span class="ok">yes</span>' : '<span class="bad">no</span>', m.floor_le_B === null ? null : 'DERIVED', 'the integer part of δ against the Pauli bound')}
    </div>`);
    html += section('Pauli bound', `<div class="fields">
      ${axRow('B computed', fmt(ch.B_computed), 'B')}
      ${row('B in the csv', m.B_csv_is_not_a_bound ? '<span class="bad">not a bound here</span>' : fmt(m.B_csv), 'READ', 'COORDINATES-2.13, B column')}
      ${row('agree', m.B_agrees === null ? '—' : m.B_agrees ? '<span class="ok">yes</span>' : '<span class="bad">no — both shown, neither repaired</span>', m.B_agrees === null ? null : 'DERIVED', 'equality of the two')}
    </div>
    ${m.B_csv_is_not_a_bound ? `<div class="callout is-finding">${esc(caveat('b-overloaded'))}</div>` : ''}
    ${m.B_agrees === false ? `<div class="callout is-finding">${esc(caveat('b-aufbau'))}</div>` : ''}`);
    html += section('Witness', `<div class="fields">
      ${axRow('witness', esc(m.witness), 'witness', true)}
      ${row('source', esc(m.source), 'READ', 'COORDINATES-2.13, source column', true)}
      ${(() => { const L = cellSourceLink(node, m); if (!L) return ''; const v = (L.url ? ext(L.url, L.text) : esc(L.text)) + (L.doi ? ' · ' + ext(L.doi, 'DOI') : ''); return row('resolved to', v, L.status, L.note, true); })()}
      ${axRow('bound note', esc(m.bound_note), 'bound', true)}
      ${(() => { const k = limitKind(m.bound_note); const r = limitRule(k); return row('limit kind', k ? `<span class="dot dot-lim-${k}"></span>${esc(LIMIT_LABEL[k] || k)}` : '—', k ? 'DERIVED' : null, r ? `rule ${esc(r.regex)}: ${esc(r.meaning)}` : 'no rule matched'); })()}
      ${(() => { const mm = /^limit ([0-9.]+);/.exec(m.bound_note); return mm ? row('series limit, as printed', mm[1], 'READ', 'COORDINATES-2.13, bound column; no unit is carried and none is added') : ''; })()}
    </div>`);
    html += actions(node, { Z: node.Z, charge: node.charge, l: node.l, ...m, delta_equation: ch.delta_equation, B_computed: ch.B_computed });
    return html;
  }

  // ---------------------------------------------------------------- particles and references
  // What the sources state of the binders and particles beyond the electron, and every
  // outward identifier it prints. Both blocks are read from data/index.js, where the generator
  // parsed each figure out of the passage that states it; the page prints them with their
  // statuses and links only what an identifier the sources print resolves to.
  const siteText = (s) => s ? `${(s.file || '').split('/').pop()} L${s.line}` : '';
  const quoteBlock = (s) => s && s.quote ? `<blockquote class="q">${esc(s.quote)} <span class="cite-inline">${esc(siteText(s))}</span></blockquote>` : '';
  const ext = (url, text) => `<a href="${esc(url)}" target="_blank" rel="noopener noreferrer">${esc(text)}</a>`;


  // ---------------------------------------------------------------- the particle indexes
  // data/particles.js sets window.__mi.particle_index: the three indexes of the particles
  // that are not periodic atoms, read at build from the other session's instruments. Every
  // member carries its coordinates with their statuses; every refused coordinate carries
  // the measurement that refuses it. Loaded on demand; the summary is index.particle_index.
  function ensureParticleIndex() {
    if (state.particleIndex) return Promise.resolve(state.particleIndex);
    if (window.__mi && window.__mi.particle_index) { state.particleIndex = window.__mi.particle_index; return Promise.resolve(state.particleIndex); }
    return new Promise((resolve, reject) => {
      const sc = document.createElement('script');
      sc.src = `${DATA}particles.js${dataVersion()}`; sc.async = true;
      sc.onload = () => { sc.remove(); if (window.__mi && window.__mi.particle_index) { state.particleIndex = window.__mi.particle_index; resolve(state.particleIndex); } else reject(new Error('data/particles.js loaded but set no window.__mi.particle_index')); };
      sc.onerror = () => { sc.remove(); reject(new Error('data/particles.js could not be loaded; it is written by python3 tools/webindex.py when the particle instruments are in the tree')); };
      document.head.appendChild(sc);
    });
  }
  const fmtV = (v) => v === null || v === undefined ? '—' : (typeof v === 'number' && !Number.isInteger(v) ? String(+v.toPrecision(7)) : String(v));
  function particleFigure(ix) {
    // members on (Q3 across, 2J up), one mark per member, jittered within the cell by index,
    // coloured by the third coordinate; the cell count under the figure is the index's own
    const names = ix.coordinates.map((c) => c.name);
    const qi = names.indexOf('Q3'), ji = names.indexOf('2J');
    const ci = ix.id === 'fundamental' ? names.indexOf('GEN') : names.indexOf('P');
    const rows = ix.rows.filter((r) => r.coords[qi] !== null && r.coords[ji] !== null);
    const qs = [...new Set(rows.map((r) => r.coords[qi]))].sort((a, b) => a - b), js = [...new Set(rows.map((r) => r.coords[ji]))].sort((a, b) => a - b);
    const W = 640, H = 60 + js.length * 44, m = { l: 54, r: 16, t: 16, b: 40 };
    const cw = (W - m.l - m.r) / qs.length, ch = (H - m.t - m.b) / js.length;
    const svg = figFrame(W, H);
    qs.forEach((q, i) => svg.appendChild(svgEl('text', { x: m.l + (i + 0.5) * cw, y: H - m.b + 16, 'text-anchor': 'middle', class: 'tick' }, ix.id === 'fundamental' ? `${q}/3` : String(q / 3))));
    svg.appendChild(svgEl('text', { x: (m.l + W - m.r) / 2, y: H - 8, 'text-anchor': 'middle', class: 'lab' }, 'electric charge Q' + (ix.id === 'fundamental' ? ' (thirds)' : '')));
    js.forEach((j, i) => svg.appendChild(svgEl('text', { x: m.l - 8, y: m.t + (js.length - i - 0.5) * ch + 4, 'text-anchor': 'end', class: 'tick' }, `J = ${j % 2 ? j + '/2' : j / 2}`)));
    qs.forEach((q, i) => js.forEach((j, k) => svg.appendChild(svgEl('rect', { x: m.l + i * cw, y: m.t + (js.length - k - 1) * ch, width: cw, height: ch, fill: 'none', class: 'ax', 'stroke-opacity': 0.35 }))));
    const cvals = [...new Set(rows.map((r) => r.coords[ci]))].sort((a, b) => a - b);
    const bucket = new Map();
    rows.forEach((r) => { const k = r.coords[qi] + '|' + r.coords[ji]; if (!bucket.has(k)) bucket.set(k, []); bucket.get(k).push(r); });
    bucket.forEach((rs, k) => {
      const [q, j] = k.split('|').map(Number), x0 = m.l + qs.indexOf(q) * cw, y0 = m.t + (js.length - js.indexOf(j) - 1) * ch;
      const n = rs.length, cols = Math.ceil(Math.sqrt(n * cw / ch)), rws = Math.ceil(n / cols);
      rs.forEach((r, i) => {
        const cx = x0 + ((i % cols) + 0.5) * cw / cols, cy = y0 + (Math.floor(i / cols) + 0.5) * ch / rws;
        const col = L_COLOR[Math.max(0, cvals.indexOf(r.coords[ci])) % L_COLOR.length];
        const c = svgEl('circle', { cx, cy, r: Math.max(1.6, Math.min(4, cw / cols / 2.6)), fill: col, 'fill-opacity': 0.8 });
        c.append(svgEl('title', {}, `${r.name}: ${names.map((nm, t) => nm + ' = ' + fmtV(r.coords[t])).join(', ')}${r.extra && r.extra.mass_MeV !== null ? '; mass ' + r.extra.mass_MeV + ' MeV' : ''}`));
        svg.appendChild(c);
      });
    });
    cvals.forEach((v, i) => { svg.appendChild(svgEl('circle', { cx: m.l + 10 + i * 96, cy: m.t - 6, r: 4, fill: L_COLOR[i % L_COLOR.length] })); svg.appendChild(svgEl('text', { x: m.l + 18 + i * 96, y: m.t - 2, class: 'tick' }, `${names[ci]} ${v === null ? 'not printed' : '= ' + v}`)); });
    return svg;
  }
  function renderParticleIndex(host, px) {
    const src = px.source, ac = px.accounting;
    let html = `<p class="note">${esc(px.status_note)}</p>
      <h3>The accounting</h3>
      <div class="fields">
        ${row('the table', `${ac.table_total.toLocaleString()} entries in the Particle Data Group's 2026 table`, 'READ', 'the capture\'s own header', true)}
        ${row('composite nuclei', ac.composite_nuclei.toLocaleString(), 'READ', 'the periodic elements: the subject of the rest of this site', true)}
        ${row('status 4', ac.status_4, 'READ', 'the fourth generation and the diquarks, excluded on PDG\'s own flag', true)}
        ${row('kept', ac.kept, 'READ', `${esc(ac.identity)}; every one a member of one of the three indexes`, true)}
        ${row('charted', `${ac.charted} of ${ac.members}`, 'DERIVED', `${ac.unplaced} members carry no printed parity and land on no cell; a gap in the table, not in physics`, true)}
      </div>
      <p class="note">${esc(ac.note)}</p>
      ${ac.named ? `<h3>The three asked for by name</h3><div class="fields">${ac.named.rows.map((r) => row(esc(r.what), `<span class="mono">${esc(r.name)}</span> — a member of the ${esc(r.index)} index, at cell (${r.cell.join(', ')}): ${Object.entries(r.coordinates).map(([k, v]) => `${esc(k)} = ${v}`).join(', ')}`, ac.named.status, null, true)).join('')}</div><p class="note">${esc(ac.named.note)}</p>` : ''}
      ${ac.antimatter ? `<h3>Antimatter, counted rather than implied</h3><div class="fields">${ac.antimatter.by_index.map((r) => row(esc(r.index), `${r.antiparticles} of ${r.members} charted members are antiparticles`, 'DERIVED', null, true)).join('')}${row('in all', `${ac.antimatter.total} of ${ac.antimatter.of_charted} charted members, ${Math.round(ac.antimatter.share * 100)} %`, ac.antimatter.status, null, true)}</div><p class="note">${esc(ac.antimatter.note)}</p>` : ''}
      <h3>Where the data comes from</h3>
      <div class="fields">
        ${row('citation', `${esc(src.citation)} · ${ext('https://doi.org/' + src.doi, 'DOI ' + src.doi)}`, 'READ', 'the review the capture reads', true)}
        ${row('via', esc(src.via), 'READ', null, true)}
        ${src.capture.map((c) => row('capture', `${esc(c.path)} · ${c.bytes.toLocaleString()} bytes · md5 <span class="mono">${esc(c.md5)}</span>`, 'READ', 'declared beside the code that reads it and hashed at build', true)).join('')}
        ${row('note', esc(src.quantum_numbers_note), null, null, true)}
        ${row('instruments', `${esc(src.tree.root)}: ${src.tree.instruments.map((i) => `<span class="mono">${esc(i)}</span>`).join(', ')}${src.tree.commit ? ` · tree at <span class="mono">${esc(String(src.tree.commit).slice(0, 12))}</span>` : ''}`, null, 'imported at build, never copied', true)}
      </div>`;
    px.indexes.forEach((ix) => {
      const names = ix.coordinates.map((c) => c.name);
      html += `<h3>${esc(ix.title)}</h3>
        <p class="note">One member is ${esc(ix.member)}. ${ix.members} members, ${ix.charted} charted on ${ix.cells} cells${ix.unplaced.length ? `, ${ix.unplaced.length} set aside by name (${esc(ix.unplaced.join(', '))}) because ${esc(ix.unplaced_why || '')}` : ''}. Closure channel K${ix.cell.channel} (height ${ix.cell.height}, width ${ix.cell.width}); closed by ${ix.closers.length ? esc(ix.closers.join(', ')) : 'no language'}. ${badge('DERIVED', 'the cells and the channel are the instrument\'s own measurement over the members')}</p>
        <div class="tbl-wrap"><table class="t"><thead><tr><th>coordinate</th><th>meaning</th><th>status</th></tr></thead><tbody>
          ${ix.coordinates.map((c) => `<tr><td class="mono">${esc(c.name)}</td><td class="wrap">${esc(c.meaning)}</td><td>${badge(c.status)}</td></tr>`).join('')}
        </tbody></table></div>
        <figure class="data-fig" id="pfig-${esc(ix.id)}"></figure>
        ${ix.colour_rule ? `<p class="note">The colour assignment, which is not in the capture: ${ix.colour_rule.map((c) => `${esc(c.what)} → ${c.dimension}`).join(' · ')} ${badge('PINNED', 'the Standard Model\'s definition, printed rather than hidden')}</p>` : ''}
        ${ix.collisions ? `<p class="note"><b>${ix.collisions.length} cells hold two members</b> — ${esc(ix.collisions_note)}: ${ix.collisions.map((c) => `(${c.cell.join(', ')}) ${esc(c.members.join(' / '))}`).join('; ')} ${badge('DERIVED')}</p>` : ''}
        ${ix.conjugation ? `<p class="note"><b>Antimatter, measured rather than seated:</b> ${ix.conjugation.pairs} particle–antiparticle pairs, ${ix.conjugation.split} split by the chart and ${ix.conjugation.collided} collided${ix.conjugation.note ? '; ' + esc(ix.conjugation.note) : ''}${ix.conjugation.mechanism ? '; under conjugation ' + ix.conjugation.mechanism.map((m) => `${esc(m.coordinate)} ${esc(m.under_conjugation)}`).join(', ') : ''}. ${badge('DERIVED')}</p>` : ''}
        ${ix.axis_contributions ? `<p class="note">Cells with one axis dropped: ${ix.axis_contributions.map((a) => `${a.dropped === null ? 'all seven' : 'without ' + esc(a.dropped)} ${a.cells}`).join(' · ')} ${badge('DERIVED')}</p>` : ''}
        <details><summary>Refused coordinates, each with its measurement (${ix.refused.length})</summary>
          <div class="fields">${ix.refused.map((r) => row(esc(r.coordinate), `<b>${esc(r.verdict)}</b> — ${esc(r.why)}${r.measurement ? `<div class="note mono" style="margin-top:4px">${esc(JSON.stringify(r.measurement))}</div>` : ''}`, r.status, null, true)).join('')}</div>
        </details>
        <details><summary>Every member (${ix.rows.length})</summary>
          <div class="tbl-wrap"><table class="t particle-table"><thead><tr><th>name</th><th class="hide-narrow">pdgid</th>${names.map((n) => `<th>${esc(n)}</th>`).join('')}<th>mass (MeV)</th><th class="hide-narrow">width (MeV)</th><th class="hide-narrow">quarks</th></tr></thead><tbody>
            ${ix.rows.map((r) => `<tr${r.coords.some((v) => v === null) ? ' class="is-unplaced"' : ''}><td>${esc(r.name)}</td><td class="hide-narrow mono">${r.pdgid}</td>${r.coords.map((v, i) => `<td>${v === null ? '<span class="muted">not printed</span>' : esc(String(v))} ${badge(ix.coordinates[i].status)}</td>`).join('')}<td>${r.extra.mass_MeV === null ? '<span class="muted">limit only</span>' : esc(fmtV(r.extra.mass_MeV)) + ' ' + badge('READ')}</td><td class="hide-narrow">${r.extra.width_MeV === null ? '—' : esc(fmtV(r.extra.width_MeV))}</td><td class="hide-narrow mono">${esc(r.extra.quarks || '')}</td></tr>`).join('')}
          </tbody></table></div>
        </details>`;
    });
    const sw = px.sweep;
    if (sw && !sw.absent) {
      const st = sw.seated;
      html += `<h3>Every chart the member sets admit, swept</h3><p class="note">${esc(sw.status_note)}</p>
        <div class="fields">
          ${row('the census', `${sw.charts} charts: ${Object.entries(sw.census).map(([k, v]) => `${esc(k)} ${v}`).join(', ')}`, 'DERIVED', 'every subset of the declared columns of size two or more, the parent included', true)}
          ${row('channels occupied', `before this docket K${sw.occupancy.before_this_sweep.join(', K')}; now K${sw.occupancy.now.join(', K')}`, 'DERIVED', esc(sw.occupancy.note), true)}
          ${row('reaching an empty channel', `${sw.hits.against_the_honest_occupancy.map((h) => `${esc(h.parent)} (${h.cols.join(', ')}) → K${h.channel}, ${h.cells} cells`).join('; ')}`, 'DERIVED', `against the overlap rule's own census a third does: ${sw.hits.against_the_overlap_rules_census.map((h) => `${esc(h.parent)} (${h.cols.join(', ')}) → K${h.channel}`).join('; ')}`, true)}
        </div>
        <h3>The seating: the only K5</h3>
        <p class="note"><b>${esc(st.parent)} (${st.cols.join(', ')})</b> — ${esc(st.registered_as)}: ${st.cells} cells, cell (${st.cell.channel}, ${st.cell.height}, ${st.cell.width}), channel K${st.channel}. ${badge(st.verdict_status, 'the seating is the sweep\'s verdict; every ground below is measured')}</p>
        <figure class="data-fig" id="pfig-isomultiplet"></figure>
        <div class="fields">
          ${Object.entries(st.grounds).map(([g, v]) => row(esc(g), v ? '<span class="ok">holds</span>' : '<span class="bad">fails</span>', 'DERIVED', g === 'reach stable' ? `K${st.channel} at every mass cut: ${st.reach.sweep.map((r) => `${esc(r.cut)} → ${r.cells} cells, K${r.channel}`).join('; ')}` : null, true)).join('')}
          ${row('the cells', st.rows.map((r) => `2I = ${r.I2}: Q3 in {${r.Q3.join(', ')}}`).join(' · '), 'DERIVED', esc(st.reading), true)}
          ${row('the corners', `${st.corners_not_held.map((c) => `(${c.join(', ')})`).join(', ')} not held, ${st.corners_outside_hull ? 'all outside the convex hull' : 'NOT all outside the hull'}`, 'DERIVED', null, true)}
          ${row('why arity 2 does not reach it', esc(st.why_arity_2_does_not_reach_it), 'DERIVED', `arity-2 freeness over the tree: ${Object.entries(sw.arity2_freeness).map(([L, f]) => `${esc(L)} ${f.closes} of ${f.charts}`).join(', ')}`, true)}
        </div>
        <h3>The two refusals</h3>
        <div class="fields">${sw.refused.map((r) => row(`${esc(r.parent)} (${r.cols.join(', ')}) → K${r.channel}${r.cells ? ', ' + r.cells + ' cells' : ''}`, `<b>${esc(r.verdict)}</b> — ${esc(r.why)}`, r.status, null, true)).join('')}</div>
        <p class="note"><b>Claimed:</b> ${esc(sw.claimed)} <b>Not claimed:</b> ${sw.not_claimed.map(esc).join(' ')} ${esc(sw.channels_note)}.</p>`;
    }
    const q = px.quasiparticles;
    if (q) {
      html += `<h3>Quasiparticles ${q.in_progress ? '<span class="muted">(in progress on the other session)</span>' : ''}</h3><p class="note">${esc(q.status_note || '')}</p>`;
      const bq = q.bosons;
      if (bq) {
        html += `<h3>${esc(bq.title)}</h3>
          <p class="note">One member is ${esc(bq.member)}. ${bq.members.length} members on ${bq.cells} cells; closure channel K${bq.cell.channel} (height ${bq.cell.height}, width ${bq.cell.width}); closed by ${bq.closers.length ? esc(bq.closers.join(', ')) : 'no language'}. ${badge('DERIVED', 'the cells and the channel are the instrument\'s own measurement')}</p>
          <div class="fields">
            ${row('source', esc(bq.source), bq.source_status, esc(bq.source_note), true)}
            ${bq.rules.map((r) => row(esc(r.rule), esc(r.text), 'DERIVED', null, true)).join('')}
            ${row('the relation', `the tree's own bosons hold ${bq.relation.boson_cells} cells and are ${bq.relation.bosons_sublattice ? 'a sublattice' : 'not a sublattice'}; the excitations hold ${bq.relation.qp_cells} and are ${bq.relation.qp_sublattice ? 'a sublattice' : 'not a sublattice'}; ${bq.relation.qp_subset_of_bosons ? 'a subset' : 'not a subset'} — outside: ${bq.relation.outside_members.map((o) => `(${o.cell.join(', ')}) ${esc(o.members.join(', '))}`).join('; ') || 'none'}; the union holds ${bq.relation.union_cells} cells and is ${bq.relation.union_sublattice ? 'still a sublattice' : 'not a sublattice'}`, bq.relation.status, esc(bq.relation.note), true)}
            ${row('the channel', `${bq.channel_note.is_chain ? 'a chain' : 'not a chain'}; over the chart's own box ${bq.channel_note.box.closing_all} of ${bq.channel_note.box.subsets} subsets close under every language, ${bq.channel_note.box.of_this_size_closing} of the ${bq.channel_note.box.of_this_size} of this size`, 'DERIVED', esc(bq.channel_note.text), true)}
            ${bq.excluded.map((x) => row('excluded: ' + esc(x.name), `${esc(x.parts.join(' + '))} → 2J in {${x.spins.join(', ')}}: ${esc(x.why)}`, 'DERIVED', 'the computation refuses it, not a choice', true)).join('')}
          </div>
          <div class="tbl-wrap"><table class="t"><thead><tr><th>member</th><th>kind</th><th>made of / breaks</th>${bq.coordinates.map((c) => `<th>${esc(c.name)}</th>`).join('')}</tr></thead><tbody>
            ${bq.composites.map((r) => `<tr><td>${esc(r.name)}</td><td>composite</td><td class="mono">${esc(r.parts.join(' + '))}</td>${r.coords.map((v) => `<td>${v} ${badge('DERIVED')}</td>`).join('')}</tr>`).join('')}
            ${bq.broken.map((r) => `<tr><td>${esc(r.name)}</td><td>broken symmetry</td><td class="wrap">${esc(r.breaks)} — generator ${esc(r.generator)}</td>${r.coords.map((v) => `<td>${v} ${badge('DERIVED')}</td>`).join('')}</tr>`).join('')}
            ${bq.hybrids.map((r) => `<tr><td>${esc(r.name)}</td><td>hybrid</td><td class="mono">${esc(r.parts.join(' × '))}</td>${r.coords.map((v) => `<td>${v} ${badge('DERIVED')}</td>`).join('')}</tr>`).join('')}
          </tbody></table></div>`;
      }
      const rr = q.nonabelian;
      if (rr) {
        html += `<h3>${esc(rr.title)}</h3>
          <p class="note">One member is ${esc(rr.member)}. Reach k ≤ ${rr.reach}: ${rr.levels} levels, ${rr.members} members on ${rr.cells} cells; closure channel K${rr.cell.channel} (height ${rr.cell.height}, width ${rr.cell.width}); closed by ${rr.closers.length ? esc(rr.closers.join(', ')) : 'no language'}. ${badge('DERIVED')}</p>
          <div class="fields">
            ${row('source', esc(rr.source), rr.source_status, esc(rr.source_note), true)}
            ${row('observed levels', rr.observed.map((o) => `k = ${o.k}: ν = ${esc(o.nu)} (${esc(o.name)}, quasihole charge e/${o.fundamental_charge.split('/')[1] || '?'})`).join(' · '), 'READ', 'named plateaux; the rest of the reach is the series\' own continuation', true)}
            ${row('validated against the literature', rr.validation.map((v) => `${esc(v.what)}: ${v.agrees ? 'agrees' : 'DISAGREES'}`).join(' · '), 'DERIVED', 'the closed form against the values the literature fixes: the Ising category at k = 2, the Fibonacci τ at k = 3, the quasihole charges e/4 and e/5', true)}
            ${row('verdict', `<b>${esc(rr.verdict)}</b> — ${esc(rr.why)}`, rr.verdict_status, 'the sweep: ' + rr.sweep.map((b) => `${esc(b.box)} → ${b.cells} cells, K${b.channel}${b.degenerate ? ' (degenerate)' : ''}`).join('; '), true)}
            ${row('fermions', `${rr.fermions.length}: ${rr.fermions.slice(0, 6).map((f) => `k = ${f.k} (l, m) = (${f.l}, ${f.m}) h = ${esc(f.h)}`).join('; ')}${rr.fermions.length > 6 ? ' …' : ''}`, 'DERIVED', esc(rr.fermions_note), true)}
            ${row('against the abelian index', `${rr.nesting.abelian_cells} abelian cells, ${rr.nesting.nonabelian_cells} non-abelian, ${rr.nesting.shared} shared; abelian in non-abelian: ${rr.nesting.abelian_in_nonabelian ? 'yes' : 'no'}; non-abelian in abelian: ${rr.nesting.nonabelian_in_abelian ? 'yes' : 'no'}; sublattices: ${rr.nesting.abelian_sublattice ? 'yes' : 'no'} / ${rr.nesting.nonabelian_sublattice ? 'yes' : 'no'}`, rr.nesting.status, esc(rr.nesting.note), true)}
          </div>
          <div class="tbl-wrap"><table class="t"><thead><tr><th>coordinate</th><th>meaning</th><th>status</th></tr></thead><tbody>
            ${rr.coordinates.map((c) => `<tr><td class="mono">${esc(c.name)}</td><td class="wrap">${esc(c.meaning)}</td><td>${badge(c.status)}</td></tr>`).join('')}
          </tbody></table></div>
          <details><summary>Every member (${rr.rows.length})</summary>
            <div class="tbl-wrap"><table class="t particle-table"><thead><tr><th>k</th><th>l</th><th>m</th><th>h</th><th>Q (e)</th>${rr.coordinates.map((c) => `<th>${esc(c.name)}</th>`).join('')}<th class="hide-narrow">level</th></tr></thead><tbody>
              ${rr.rows.map((r) => `<tr><td>${r.k}</td><td>${r.l}</td><td>${r.m}</td><td>${esc(r.h)} ${badge('DERIVED')}</td><td>${esc(r.Q)} ${badge('DERIVED')}</td>${r.coords.map((v, i) => `<td>${v} ${badge(rr.coordinates[i].status)}</td>`).join('')}<td class="hide-narrow">${r.observed ? 'observed plateau' : '<span class="muted">continuation</span>'}</td></tr>`).join('')}
            </tbody></table></div>
          </details>`;
      }
      const fq = q.seated;
      if (fq && !fq.absent) {
        html += `<h3>${esc(fq.title)}</h3>
          <p class="note">One member is ${esc(fq.member)}. Reach m ≤ ${fq.reach}: ${fq.states} states, ${fq.members} members on ${fq.cells} cells; closure channel K${fq.cell.channel} (height ${fq.cell.height}, width ${fq.cell.width}); closed by ${fq.closers.length ? esc(fq.closers.join(', ')) : 'no language'}. ${badge('DERIVED', 'the cells and the channel are the instrument\'s own measurement')}</p>
          <div class="fields">
            ${row('source', esc(fq.source), fq.source_status, esc(fq.source_note), true)}
            ${row('observed states', fq.observed.map((o) => `ν = ${esc(o.filling)} (fundamental charge ${esc(o.fundamental_charge)})`).join(' · '), 'READ', esc(fq.observed_note), true)}
            ${row('the e/3 quasiparticle', esc(fq.e_over_3.text), fq.e_over_3.status, null, true)}
            ${row('statistics', `${fq.statistics.anyons} anyons, ${fq.statistics.fermions} fermions, ${fq.statistics.bosons} bosons`, fq.statistics.status, esc(fq.statistics.note), true)}
            ${row('verdict', `<b>${esc(fq.verdict)}</b> — ${esc(fq.why)}`, fq.verdict_status, esc(fq.verdict_note) + '; the sweep: ' + fq.sweep.map((b) => `${esc(b.box)} → ${b.cells} cells, K${b.channel}${b.degenerate ? ' (degenerate)' : ''}`).join('; '), true)}
          </div>
          <div class="tbl-wrap"><table class="t"><thead><tr><th>coordinate</th><th>meaning</th><th>status</th></tr></thead><tbody>
            ${fq.coordinates.map((c) => `<tr><td class="mono">${esc(c.name)}</td><td class="wrap">${esc(c.meaning)}</td><td>${badge(c.status)}</td></tr>`).join('')}
          </tbody></table></div>
          <figure class="data-fig" id="pfig-fqh"></figure>
          <details><summary>Refused coordinates (${fq.refused.length})</summary><div class="fields">${fq.refused.map((r) => row(esc(r.coordinate), `<b>${esc(r.verdict)}</b> — ${esc(r.why)}`, r.status, null, true)).join('')}</div></details>
          <details><summary>Every member (${fq.rows.length})</summary>
            <div class="tbl-wrap"><table class="t particle-table"><thead><tr><th>m</th><th>j</th><th>Q (e)</th><th>θ/π</th>${fq.coordinates.map((c) => `<th>${esc(c.name)}</th>`).join('')}<th class="hide-narrow">state</th></tr></thead><tbody>
              ${fq.rows.map((r) => `<tr><td>${r.m}</td><td>${r.j}</td><td>${esc(r.Q)} ${badge('DERIVED')}</td><td>${esc(r.theta)} ${badge('DERIVED')}</td>${r.coords.map((v, i) => `<td>${v} ${badge(fq.coordinates[i].status)}</td>`).join('')}<td class="hide-narrow">${r.observed ? 'observed plateau' : '<span class="muted">continuation</span>'}</td></tr>`).join('')}
            </tbody></table></div>
          </details>
          <p class="note"><b>Not here:</b> ${esc(fq.not_here)}</p>
          <h3>The earlier chart, still on the record</h3>`;
      }
      if (q.no_table) html += `<div class="fields">
          ${row('no table', esc(q.no_table.claim), q.no_table.status, `${q.no_table.space_groups} space groups, ${q.no_table.point_groups} point groups, ${q.no_table.arithmetic_classes} arithmetic crystal classes: the host's, not the quasiparticle's`, true)}
          ${row('the universal numbers', `${q.no_table.universal.list.map((u) => `${esc(u.kind)} (spin ${u.spin})`).join(', ')}: ${q.no_table.universal.kinds} kinds on ${q.no_table.universal.distinct_cells} cells`, 'DERIVED', 'a chart with that resolution reports on bosons', true)}
        </div>`;
      if (q.anyons) html += `<p class="note">${esc(q.anyons.claim)}</p>
        <div class="fields">${row('verdict', `<b>${esc(q.anyons.verdict)}</b> — ${esc(q.anyons.why)}`, q.anyons.verdict_status, 'the box-invariance test, imported and not reimplemented: ' + q.anyons.sweep.map((b) => `${esc(b.box)} → ${b.cells} cells, K${b.channel}`).join('; '), true)}</div>
        <div class="tbl-wrap"><table class="t"><thead><tr><th>k</th><th>J</th><th>h</th><th>d</th><th>J × J</th>${q.anyons.coordinates.map((c) => `<th title="${esc(c.meaning)}">${esc(c.name)}</th>`).join('')}</tr></thead><tbody>
          ${q.anyons.rows.map((r) => `<tr><td>${r.k}</td><td>${r.J}</td><td>${esc(r.h)} ${badge(q.anyons.rows_status)}</td><td>${esc(fmtV(r.d))}</td><td class="mono">${r.fusion_JxJ.join(' ')}</td>${r.coords.map((v) => `<td>${v} ${badge('DERIVED')}</td>`).join('')}</tr>`).join('')}
        </tbody></table></div>
        <p class="note">Spot checks: ${q.anyons.spot_checks.map((c) => `${esc(c.what)} = ${esc(String(c.computed))} (expected ${esc(String(c.expected))})`).join(' · ')}. ${esc(q.anyons.not_ising)}</p>`;
      if (q.reopens) html += `<p class="note"><b>What would reopen it:</b> ${esc(q.reopens)}</p>`;
    }
    host.innerHTML = html;
    const fqFig = host.querySelector('#pfig-fqh');
    if (fqFig && q && q.seated && q.seated.rows) {
      const fq = q.seated, ms = [...new Set(fq.rows.map((r) => r.m))].sort((a, b) => a - b), jmax = Math.max(...fq.rows.map((r) => r.j));
      const W = 640, H = 300, m = { l: 48, r: 16, t: 26, b: 40 };
      const sx = (mm) => m.l + (ms.indexOf(mm) + 0.5) / ms.length * (W - m.l - m.r), sy = (j) => H - m.b - j / jmax * (H - m.t - m.b);
      const svg = figFrame(W, H);
      ms.forEach((mm) => svg.appendChild(svgEl('text', { x: sx(mm), y: H - m.b + 16, 'text-anchor': 'middle', class: 'tick', 'font-weight': fq.observed.some((o) => o.m === mm) ? '700' : '400' }, `1/${mm}`)));
      svg.appendChild(svgEl('text', { x: (m.l + W - m.r) / 2, y: H - 8, 'text-anchor': 'middle', class: 'lab' }, 'filling fraction ν = 1/m (bold: observed plateau)'));
      axisY(svg, m.l, H - m.b, m.t, niceTicks(0, jmax, 5).map((v) => [sy(v), v]), (v) => String(v), 'j');
      const cols = { 0: '#3a7d44', 1: '#b5651d', 2: '#1f4e8c' }, lab = { 0: 'boson', 1: 'fermion', 2: 'anyon' };
      fq.rows.forEach((r) => { const c = svgEl('circle', { cx: sx(r.m), cy: sy(r.j), r: 3.4, fill: cols[r.coords[0]], 'fill-opacity': 0.85 }); c.append(svgEl('title', {}, `m = ${r.m}, j = ${r.j}: Q = ${r.Q} e, θ/π = ${r.theta}, ${lab[r.coords[0]]}, ORD ${r.coords[1]}, CHORD ${r.coords[2]}`)); svg.appendChild(c); });
      [2, 0, 1].forEach((k, i) => { svg.appendChild(svgEl('circle', { cx: m.l + 10 + i * 90, cy: m.t - 12, r: 4, fill: cols[k] })); svg.appendChild(svgEl('text', { x: m.l + 18 + i * 90, y: m.t - 8, class: 'tick' }, `${lab[k]} (${fq.statistics[lab[k] + 's']})`)); });
      fqFig.appendChild(svg);
      const cap = document.createElement('figcaption'); cap.innerHTML = `The ${fq.members} quasiparticles of the ${fq.states} Laughlin states, j against the filling fraction, coloured by statistics class; hover a mark for its charge and exchange phase. No member is a fermion. ${badge('DERIVED', 'drawn from the member table')}`; fqFig.appendChild(cap);
    }
    const isoFig = host.querySelector('#pfig-isomultiplet');
    if (isoFig && sw && sw.seated) {
      const st = sw.seated, Is = st.rows.map((r) => r.I2), Qs = [...new Set(st.rows.flatMap((r) => r.Q3).concat(st.corners_not_held.map((c) => c[1])))].sort((a, b) => a - b);
      const W = 420, H = 60 + Is.length * 40, m = { l: 60, r: 16, t: 14, b: 40 }, cw = (W - m.l - m.r) / Qs.length, ch = (H - m.t - m.b) / Is.length;
      const svg = figFrame(W, H);
      Qs.forEach((q, i) => svg.appendChild(svgEl('text', { x: m.l + (i + 0.5) * cw, y: H - m.b + 16, 'text-anchor': 'middle', class: 'tick' }, String(q / 3))));
      svg.appendChild(svgEl('text', { x: (m.l + W - m.r) / 2, y: H - 8, 'text-anchor': 'middle', class: 'lab' }, 'electric charge Q'));
      Is.forEach((i, k) => svg.appendChild(svgEl('text', { x: m.l - 8, y: m.t + (Is.length - k - 0.5) * ch + 4, 'text-anchor': 'end', class: 'tick' }, `I = ${i % 2 ? i + '/2' : i / 2}`)));
      const held = new Set(st.rows.flatMap((r) => r.Q3.map((q) => r.I2 + '|' + q))), miss = new Set(st.corners_not_held.map((c) => c.join('|')));
      Is.forEach((i, k) => Qs.forEach((q, j) => {
        const key = i + '|' + q, x = m.l + j * cw, y = m.t + (Is.length - k - 1) * ch;
        const r = svgEl('rect', { x: x + 2, y: y + 2, width: cw - 4, height: ch - 4, rx: 3, fill: held.has(key) ? '#1f4e8c' : (miss.has(key) ? 'none' : 'none'), 'fill-opacity': 0.75, stroke: miss.has(key) ? '#b5651d' : 'var(--line)', 'stroke-dasharray': miss.has(key) ? '4 3' : 'none' });
        r.append(svgEl('title', {}, `2I = ${i}, Q3 = ${q}: ${held.has(key) ? 'held' : (miss.has(key) ? 'a box point not held, outside the hull' : 'no such box point')}`));
        svg.appendChild(r);
      }));
      isoFig.appendChild(svg);
      const cap = document.createElement('figcaption'); cap.innerHTML = `The ${st.cells} cells of baryons (2I, Q3), isospin up and charge across; the dashed corners are the four box points the chart does not hold, which lie outside the convex hull of the sixteen. ${badge('DERIVED', 'drawn from the seated chart\'s rows')}`; isoFig.appendChild(cap);
    }
    px.indexes.forEach((ix) => {
      const fig = host.querySelector('#pfig-' + ix.id);
      if (!fig) return;
      fig.appendChild(particleFigure(ix));
      const cap = document.createElement('figcaption'); cap.innerHTML = `${ix.charted} charted members by electric charge and spin, one mark per member, coloured by ${esc(ix.id === 'fundamental' ? 'generation' : 'parity')}; hover a mark for its coordinates. ${badge('DERIVED', 'drawn from the member table; the cells are the instrument\'s')}`; fig.appendChild(cap);
    });
  }

  function renderParticles() {
    const pt = state.index.particles, rf = state.index.references || {};
    const host = $('#particles-body');
    if (state.index.particle_index) {
      host.innerHTML = '<p class="note">loading the particle indexes…</p>';
      ensureParticleIndex().then((px) => {
        renderParticleIndex(host, px);
        if (pt) { const more = document.createElement('div'); more.id = 'particles-muon'; host.appendChild(more); renderMuonBlock(more, pt, rf); }
      }).catch((err) => { host.innerHTML = `<p class="note">${esc(err.message)}</p>`; });
      return;
    }
    if (!pt) { host.innerHTML = '<p class="note">this build carries no particles block.</p>'; return; }
    renderMuonBlock(host, pt, rf);
  }
  function renderMuonBlock(host, pt, rf) {
    const w = pt.window, mu = pt.muon, am = pt.antimatter, ah = pt.antiprotonic_helium, ph = pt.photon;
    const inst = mu.instrument, cc = mu.collection, arx = (id) => ext('https://arxiv.org/abs/' + id, 'arXiv:' + id);
    let html = `<p class="note">${esc(pt.status_note)}</p>`;
    html += `<h3>What the lattice says of them</h3><div class="fields">${pt.scope.map((s) => row(esc(s.name), esc(s.site.quote), s.status, siteText(s.site), true)).join('')}</div>`;
    html += `<h3>The binder window</h3>
      <div class="fields">
        ${row('structural window', `[${w.m_e[0]}, ${w.m_e[1]}] mₑ`, w.status, siteText(w.site))}
        ${row('its occupants', `muon ${w.occupants.muon} mₑ · pion ${w.occupants.pion} mₑ`, 'READ', siteText(w.occupants.site))}
        ${row('the muon, interior by', `${w.interior.below}× below · ${w.interior.above}× above`, 'READ', siteText(w.interior.site))}
        ${row('molecular bound states', `electron ${w.N_states.electron} · muon ${w.N_states.muon} · tau ${w.N_states.tau}`, w.N_states.status, siteText(w.N_states.site))}
        ${row('a binder', esc(pt.binder.quote), 'READ', siteText(pt.binder), true)}
      </div>${quoteBlock(w.bracket)}`;
    html += `<h3>The muon</h3>
      <div class="fields">
        ${row('mass, as printed', `${mu.mass_m_e.printed} mₑ`, 'READ', siteText(w.occupants.site))}
        ${row('mass, PDG, in fault ' + esc(mu.mass_m_e.fault), `${mu.mass_m_e.PDG} mₑ`, mu.mass_m_e.status, siteText(mu.mass_m_e.site))}
        ${row('the fault', esc(mu.mass_m_e.fault_note.quote), 'READ', siteText(mu.mass_m_e.fault_note), true)}
      </div>
      <p class="note">The energy balance is an instrument, <code>tools/mucf.py</code>, and its inputs carry the paper's own statuses, never flattened; the eighth solver mode runs it here. Its header table, read from the instrument:</p>
      <div class="tbl-wrap"><table class="t"><thead><tr><th>input</th><th>value</th><th>status</th><th>note</th></tr></thead><tbody>
        ${inst.status_table.map((r) => `<tr><td>${esc(r.name)}</td><td>${esc(r.value)}</td><td>${badge(r.status, 'mucf.py\'s own vocabulary')}</td><td class="wrap">${esc(r.note)}</td></tr>`).join('')}
      </tbody></table></div>
      <div class="callout is-finding">${esc(inst.reclassified.quote)} <span class="cite-inline">${esc(siteText(inst.reclassified))}</span></div>
      <p class="note">The collection budget (<code>tools/collector.py</code>, ${badge('SOURCED', 'each stage sourced to a published machine figure; a stage it cannot source is not filled')}): MuSIC ${cc.MuSIC_mu_minus_per_W[0].toExponential(1)} ± ${cc.MuSIC_mu_minus_per_W[1].toExponential(1)} μ⁻ s⁻¹ W⁻¹ (${arx(cc.arxiv.MuSIC)}); Mu2e ${cc.Mu2e_stopped_per_p} stopped μ⁻ per 8 GeV proton (${arx(cc.arxiv.Mu2e)}); COMET ${cc.COMET_captured_per_p[0]}–${cc.COMET_captured_per_p[1]} captured π⁻ + μ⁻ per proton (${arx(cc.arxiv.COMET)}); the kinematic floor ${cc.pion_threshold_GeV} GeV; the paper prices its binder at ${cc.paper_assumed_GeV} GeV, work-breakeven at ${cc.work_breakeven_GeV} GeV and heat-breakeven at ${cc.heat_breakeven_GeV} GeV.</p>
      <div class="actions"><button type="button" data-act="mucf-mode">Run the energy balance (solver suite, mode 8)</button></div>`;
    html += `<h3>What the definition excludes</h3>
      <div class="tbl-wrap"><table class="t"><thead><tr><th>excluded</th><th>grounds</th></tr></thead><tbody>
        ${pt.exclusions.rows.map((r) => `<tr><td>${esc(r.excluded)}</td><td class="wrap">${esc(r.grounds)} <span class="cite-inline">L${r.line}</span></td></tr>`).join('')}
      </tbody></table></div><p class="note">${badge(pt.exclusions.status)} ${esc(pt.exclusions.file.split('/').pop())} §6: the pion, kaon, antiproton and Σ⁻ by nuclear absorption; the tau because the molecular index degenerates.</p>`;
    html += `<h3>Antimatter and the exotic atoms</h3>
      <p class="note">${badge(am.status, am.note)} ${esc(am.note)}.</p>
      ${quoteBlock(am.cpt)}
      <div class="fields">${row('antihydrogen 1S–2S against hydrogen (ALPHA)', esc(am.alpha.value), 'RECOVERED', siteText(am.alpha.site))}</div>
      ${quoteBlock(am.reduced_mass.site)}
      <div class="tbl-wrap"><table class="t"><thead><tr><th>system</th><th class="num">μ / mₑ</th><th class="num">radius / Å</th></tr></thead><tbody>
        ${am.reduced_mass.systems.map((x) => `<tr><td>${esc(x.system)}</td><td class="num">${x.mu_over_me}</td><td class="num">${x.radius_A}</td></tr>`).join('')}
      </tbody></table></div>
      ${quoteBlock(am.antihydrogen)}${quoteBlock(am.antiprotonic_only)}`;
    html += `<h3>Antiprotonic helium, the worked cell</h3>
      <div class="fields">
        ${row('cell', `(${ah.cell[0]}, ${ah.cell[1]})`, ah.status, siteText(ah.site))}
        ${ah.routes.map((r) => row(esc(r.route), `${esc(r.MHz)} ± ${r.pm} MHz`, 'READ', `L${r.line}`)).join('')}
        ${row('agreement', `${ah.agreement_sigma}σ, with no shared measurement`, 'READ', siteText(ah.agreement_site))}
        ${row('scope', esc(ah.scope), 'PROSE-ONLY', 'PROSE-ONLY.tsv PO-0279', true)}
      </div>`;
    html += `<h3>The photon</h3>
      <div class="fields">${row('E over the dipole selection index', ph.E, ph.status, siteText(ph.site))}</div>
      ${quoteBlock(ph.site)}${quoteBlock(ph.claim)}`;
    html += `<h3>Λ_phys, the ${pt.constants.count} constants</h3>
      <p class="note">${badge(pt.constants.status)} ${esc(pt.constants.note)}.</p>
      <div class="tbl-wrap"><table class="t"><thead><tr><th>parameter</th><th>value</th><th>note</th></tr></thead><tbody>
        ${pt.constants.rows.map((c) => `<tr${c.withdrawn ? ' class="is-withdrawn"' : ''}><td>${esc(c.name)}</td><td><code>${esc(c.value)}</code></td><td class="wrap">${esc(c.note)} <span class="cite-inline">L${c.line}</span></td></tr>`).join('')}
      </tbody></table></div>`;
    html += `<h3>Held in prose only</h3>
      <p class="note">Rows of PROSE-ONLY.tsv: statements the chat export holds and no file does. A row is a candidate for a home, not a figure of the index.</p>
      <div class="tbl-wrap"><table class="t"><thead><tr><th>id</th><th>kind</th><th>label</th><th>confidence</th></tr></thead><tbody>
        ${pt.prose_only.map((r) => `<tr><td>${esc(r.id)}</td><td>${esc(r.category)}</td><td class="wrap">${esc(r.label)}<div class="note" style="margin-top:4px">${esc(r.quote)}</div></td><td>${esc(r.confidence)}</td></tr>`).join('')}
      </tbody></table></div>`;
    const ab = pt.absent.terms;
    html += `<h3>Counted absent</h3>
      <p class="note">${badge(pt.absent.status)} ${esc(pt.absent.note)}: ${Object.keys(ab).map((t) => `<b>${esc(t)}</b> ${ab[t].occurrences}${ab[t].first ? ` (first at ${esc(siteText(ab[t].first))})` : ''}`).join(' · ')}.</p>`;
    if (rf.nist_asd) html += `<p class="note">Outward: ${ext(rf.nist_asd.url, 'NIST ASD')} · ${ext(rf.nist_asd.doi_url, 'DOI ' + rf.nist_asd.doi)} · the References dialog lists every arXiv and DOI identifier the sources cite.</p>`;
    const body = host;
    body.innerHTML = html;
    body.querySelectorAll('[data-act="mucf-mode"]').forEach((b) => b.addEventListener('click', () => { $('#dlg-particles').close(); openSolver('mucf'); }));
  }

  function renderReferences() {
    const rf = state.index.references;
    if (!rf) { $('#references-body').innerHTML = '<p class="note">data/index.js carries no references block.</p>'; return; }
    const n = rf.nist_asd, ss = rf.spectra_sources || { rows: [], by_species: {} };
    const cites = (e) => e.cites.map((c) => `<div class="note"><span class="cite-inline">${esc(c.paper)}</span> ${esc(c.text)}</div>`).join('');
    let html = `<p class="note">${esc(rf.note)}</p>`;
    html += `<h3>The data source the index links itself</h3>
      <div class="fields">
        ${row('database', ext(n.url, n.name), 'READ', 'the citation as the sources print it', true)}
        ${row('DOI', ext(n.doi_url, n.doi), 'READ', 'as printed', true)}
        ${row('the query', esc(n.query_not_held), null, 'not held', true)}
      </div>${(n.cited_for || []).map((t) => `<p class="note">cited for ${esc(t)}</p>`).join('')}`;
    html += `<h3>The spectra compilations, by species</h3>
      <p class="note">Which compilation each measured species' levels were drawn from, as the spectra sources table prints it. Only NIST ASD carries an identifier the sources print, so only it is linked.</p>
      <div class="tbl-wrap"><table class="t"><thead><tr><th>compilation</th><th>spectra drawn</th></tr></thead><tbody>
        ${ss.rows.map((r) => `<tr><td>${r.compilation.startsWith('NIST ASD') ? ext(n.url, r.compilation) : esc(r.compilation)}</td><td class="wrap">${esc(r.species)} <span class="cite-inline">L${r.line}</span></td></tr>`).join('')}
      </tbody></table></div>`;
    html += `<h3>arXiv identifiers (${rf.arxiv.length})</h3>
      <div class="tbl-wrap"><table class="t"><thead><tr><th>identifier</th><th>cited at</th></tr></thead><tbody>
        ${rf.arxiv.map((e) => `<tr><td>${ext(e.url, e.id)}<div class="note">${e.n} site${e.n === 1 ? '' : 's'}</div></td><td class="wrap">${cites(e)}</td></tr>`).join('')}
      </tbody></table></div>`;
    html += `<h3>DOIs (${rf.doi.length})</h3>
      <div class="tbl-wrap"><table class="t"><thead><tr><th>DOI</th><th>cited at</th></tr></thead><tbody>
        ${rf.doi.map((e) => `<tr><td>${ext(e.url, e.id)}<div class="note">${e.n} site${e.n === 1 ? '' : 's'}</div></td><td class="wrap">${cites(e)}</td></tr>`).join('')}
      </tbody></table></div>`;
    if (rf.urls.length) html += `<h3>Other addresses printed (${rf.urls.length})</h3><div class="fields">${rf.urls.map((e) => row(ext(e.url, e.id), cites(e), 'READ', 'as printed', true)).join('')}</div>`;
    $('#references-body').innerHTML = html;
  }

  // the source behind a measured cell, linked only where the sources print the target
  function cellSourceLink(node, m) {
    const rf = state.index.references || {};
    const n = rf.nist_asd, bs = (rf.spectra_sources || {}).by_species || {};
    const src = m.source || '';
    if (/^NIST ASD/.test(src) && n) return { text: `NIST ASD (ver. 5.12) — the retrieval the source column names`, url: n.url, doi: n.doi_url, status: 'READ', note: 'the sources print the database and its DOI; the query itself is not held' };
    if (src === 'captured levels') {
      const key = `${symbolOf(node.Z)} ${roman(node.charge)}`;
      const hit = Object.keys(bs).find((k) => k === key || k.startsWith(key + ' ('));
      if (hit) return { text: `${bs[hit].compilation} (${hit})`, url: bs[hit].url, doi: bs[hit].url && n ? n.doi_url : null, status: 'READ', note: 'the spectra sources table, by species' };
      return { text: 'captured levels — the compilation is not named for this species', url: null, status: null, note: 'no target is invented' };
    }
    if (/Theodosiou/.test(src)) return { text: 'Theodosiou, Manson & Inokuti 1986, PRA 34, 943 — a journal reference, no identifier printed', url: null, status: 'READ', note: 'cited as a string' };
    if (/R 1627/.test(src)) return { text: 'read from the species\' own level files', url: null, status: 'READ', note: 'the index\'s own level files' };
    if (/by symmetry/.test(src)) return { text: 'one electron, δ = 0 by symmetry — no external source', url: null, status: 'READ', note: 'exact' };
    if (/channel equation/.test(src)) return { text: 'the channel equation — computed, no external source', url: null, status: null, note: 'a computed cell links nowhere' };
    return null;
  }
  function elementReferences(e, rec) {
    const rf = state.index.references || {};
    const n = rf.nist_asd;
    if (!n) return '';
    const kinds = new Map();
    if (rec) for (const ch of rec.channels) for (const m of ch.measured) if (m.grade === 'measured') {
      const k = /^NIST ASD/.test(m.source) ? 'NIST ASD, the dated retrieval' : m.source;
      kinds.set(k, (kinds.get(k) || 0) + 1);
    }
    return section('References', `<div class="fields">
      ${row('ground configuration', `${ext(n.url, 'NIST ASD ver. 5.12')} · ${ext(n.doi_url, 'DOI ' + n.doi)}`, 'READ', 'the observed configurations table: read, not computed; the query itself is not held', true)}
      ${kinds.size ? row('measured cells\' sources', [...kinds].map(([k, v]) => `${esc(k)} (${v})`).join(' · '), 'READ', 'COORDINATES-2.13, source column; each cell\'s plate resolves its compilation', true) : ''}
    </div>`);
  }
  function openSolver(id) {
    const sel = document.querySelector('#solver-body select');
    if (!sel) return;
    const reg = solverRegistry() || [];
    const i = reg.findIndex((m) => m.id === id);
    if (i >= 0 && i < sel.options.length) { sel.selectedIndex = i; sel.dispatchEvent(new Event('change')); }
    try { $('#solvers').scrollIntoView({ behavior: reduced ? 'auto' : 'smooth', block: 'start' }); } catch (err) { /* no scroll */ }
  }

  // ---------------------------------------------------------------- provenance

  // ---------------------------------------------------------------- the released papers
  // data/papers.js sets window.__mi.papers: each released paper rendered at build from
  // its own text, its headings, its figures with their ledger md5. Loaded on demand.
  function ensurePapers() {
    if (state.papers) return Promise.resolve(state.papers);
    if (window.__mi && window.__mi.papers) { state.papers = window.__mi.papers; return Promise.resolve(state.papers); }
    return new Promise((resolve, reject) => {
      const sc = document.createElement('script');
      sc.src = `${DATA}papers.js${dataVersion()}`; sc.async = true;
      sc.onload = () => { sc.remove(); if (window.__mi && window.__mi.papers) { state.papers = window.__mi.papers; resolve(state.papers); } else reject(new Error('data/papers.js loaded but set no window.__mi.papers')); };
      sc.onerror = () => { sc.remove(); reject(new Error('data/papers.js could not be loaded; it is written by python3 tools/webindex.py')); };
      document.head.appendChild(sc);
    });
  }
  function paperCite(pp) {
    const m = state.index.meta || {}, c = m.cite || {};
    return `${c.author || 'Lach, M.'} (${c.year || ''}). ${pp.title}. In ${c.title || 'The Method Index'}, edition ${c.commit || '?'}. ${c.url || ''}#paper=${pp.slug}`;
  }
  function renderPapers(slug) {
    const host = $('#papers-body');
    host.innerHTML = '<p class="note">loading the papers…</p>';
    ensurePapers().then((papers) => {
      const sum = (state.index.papers || {});
      if (!slug) {
        host.innerHTML = `<p class="note">The papers the author has released to this site, as written. Each is rendered at build from its own text; its figures travel with the md5 the repository's ledger records. ${sum.papers ? badge('READ', 'the paper\'s own text; nothing in it is edited for the site') : ''}</p>
          <div class="paper-list">${papers.map((pp) => `<div class="paper-card${pp.held ? '' : ' is-slot'}">
            <h3>${esc(pp.title)}</h3>${pp.subtitle ? `<p class="paper-sub">${esc(pp.subtitle)}</p>` : ''}
            <p class="note">${esc(pp.author || '')}${pp.held ? ` · ${(pp.words || 0).toLocaleString()} words · ${(pp.figures || []).length} figure${(pp.figures || []).length === 1 ? '' : 's'} · ${(pp.arxiv || []).length + (pp.doi || []).length} linked identifiers · md5 <span class="mono">${esc((pp.md5 || '').slice(0, 12))}</span>${pp.md5_recorded ? (pp.md5 === pp.md5_recorded ? ' <span class="ok">matches the store</span>' : ' <span class="bad">DRIFT from the store</span>') : ''}` : ` · <b>not yet held</b> — ${esc(pp.note || '')}`}</p>
            ${pp.held ? `<div class="actions"><button type="button" data-paper="${esc(pp.slug)}">Read</button><button type="button" class="ghost" data-cite="${esc(pp.slug)}">Cite</button></div>` : ''}
          </div>`).join('')}</div>`;
        host.querySelectorAll('button[data-paper]').forEach((b) => b.addEventListener('click', () => renderPapers(b.dataset.paper)));
        host.querySelectorAll('button[data-cite]').forEach((b) => b.addEventListener('click', () => {
          const pp = papers.find((x) => x.slug === b.dataset.cite);
          const line = paperCite(pp);
          try { navigator.clipboard.writeText(line); } catch (e) { /* no clipboard */ }
          b.textContent = 'copied'; setTimeout(() => { b.textContent = 'Cite'; }, 1200);
          alertLine(host, line);
        }));
        return;
      }
      const pp = papers.find((x) => x.slug === slug);
      if (!pp || !pp.held) { host.innerHTML = '<p class="note">no such paper is held.</p>'; return; }
      host.innerHTML = `<div class="paper-head"><button type="button" class="ghost" data-act="papers-back">← all papers</button>
          <span class="note">${esc(pp.author || '')} · md5 <span class="mono">${esc((pp.md5 || '').slice(0, 12))}</span> ${badge('READ', 'the paper\'s own text, rendered at build')}</span></div>
        <div class="paper-layout">
          <nav class="paper-toc" aria-label="Contents">${pp.headings.filter((h) => h.level >= 2 && h.level <= 3).map((h) => `<a href="#${esc(h.id)}" data-h="${esc(h.id)}" class="toc-${h.level}">${esc(h.text)}</a>`).join('')}
            <div class="note" style="margin-top:10px">figures ${pp.figures.filter((f) => f.held).length} held${pp.figures.some((f) => !f.held) ? `, ${pp.figures.filter((f) => !f.held).length} not held` : ''}; every held figure's md5 ${pp.figures.every((f) => !f.held || f.ok) ? 'matches the ledger' : 'DRIFTS from the ledger'}</div>
            <div class="note" style="margin-top:6px"><a href="#" data-act="paper-cite">cite this paper</a></div>
          </nav>
          <article class="paper" id="paper-article">${pp.html}</article>
        </div>`;
      host.querySelectorAll('#paper-article img').forEach((im) => { const a = document.createElement('a'); a.className = 'fig-link'; a.href = im.getAttribute('src'); a.target = '_blank'; a.rel = 'noopener'; a.title = 'open the figure at full size'; im.replaceWith(a); a.appendChild(im); });
      host.querySelector('[data-act="papers-back"]').addEventListener('click', () => renderPapers());
      host.querySelectorAll('.paper-toc a[data-h]').forEach((a) => a.addEventListener('click', (ev) => { ev.preventDefault(); const t = host.querySelector('#' + CSS.escape(a.dataset.h)); if (t) t.scrollIntoView({ block: 'start', behavior: 'smooth' }); }));
      host.querySelector('[data-act="paper-cite"]').addEventListener('click', (ev) => { ev.preventDefault(); alertLine(host, paperCite(pp)); });
      host.scrollTop = 0;
    }).catch((err) => { host.innerHTML = `<p class="note">${esc(err.message)}</p>`; });
  }
  function alertLine(host, text) {
    let box = host.querySelector('.cite-box');
    if (!box) { box = document.createElement('div'); box.className = 'cite-box'; host.prepend(box); }
    box.innerHTML = `<span class="mono">${esc(text)}</span>`;
  }

  // ---------------------------------------------------------------- figures from the data
  // Every figure here is drawn from data/index.js at open: no number is typed, and the
  // caption names the block it is drawn from and the status that block carries.
  const SVG_NS = 'http://www.w3.org/2000/svg';
  function svgEl(tag, attrs, text) {
    const e = document.createElementNS(SVG_NS, tag);
    Object.entries(attrs || {}).forEach(([k, v]) => e.setAttribute(k, v));
    if (text !== undefined) e.textContent = text;
    return e;
  }
  function figFrame(w, h) {
    const svg = svgEl('svg', { viewBox: `0 0 ${w} ${h}`, width: '100%', role: 'img', class: 'fig-svg', 'font-family': 'IBM Plex Sans, system-ui, sans-serif', 'font-size': '11' });
    return svg;
  }
  function axisX(svg, x0, x1, y, ticks, fmt, label) {
    svg.appendChild(svgEl('line', { x1: x0, x2: x1, y1: y, y2: y, class: 'ax' }));
    ticks.forEach(([px, v]) => { svg.appendChild(svgEl('line', { x1: px, x2: px, y1: y, y2: y + 4, class: 'ax' })); svg.appendChild(svgEl('text', { x: px, y: y + 15, 'text-anchor': 'middle', class: 'tick' }, fmt(v))); });
    if (label) svg.appendChild(svgEl('text', { x: (x0 + x1) / 2, y: y + 30, 'text-anchor': 'middle', class: 'lab' }, label));
  }
  function axisY(svg, x, y0, y1, ticks, fmt, label) {
    svg.appendChild(svgEl('line', { x1: x, x2: x, y1: y0, y2: y1, class: 'ax' }));
    ticks.forEach(([py, v]) => { svg.appendChild(svgEl('line', { x1: x - 4, x2: x, y1: py, y2: py, class: 'ax' })); svg.appendChild(svgEl('text', { x: x - 7, y: py + 3.5, 'text-anchor': 'end', class: 'tick' }, fmt(v))); });
    if (label) { const t = svgEl('text', { x: 14, y: (y0 + y1) / 2, 'text-anchor': 'middle', class: 'lab', transform: `rotate(-90 14 ${(y0 + y1) / 2})` }, label); svg.appendChild(t); }
  }
  function niceTicks(lo, hi, n) {
    const span = hi - lo || 1, raw = span / n, mag = Math.pow(10, Math.floor(Math.log10(raw)));
    const step = [1, 2, 2.5, 5, 10].map((m) => m * mag).find((st) => span / st <= n) || mag * 10;
    const out = []; for (let v = Math.ceil(lo / step) * step; v <= hi + 1e-9; v += step) out.push(+v.toFixed(10));
    return out;
  }
  const L_COLOR = ['#1f4e8c', '#b5651d', '#3a7d44', '#8b3a62', '#6b6b6b', '#c9a227', '#2a9d8f', '#7b2cbf'];
  function figEquation(ix) {
    const fd = (ix.figure_data || {}).equation; if (!fd || !fd.rows.length) return null;
    const W = 560, H = 400, m = { l: 56, r: 16, t: 14, b: 44 };
    const xs = fd.rows.map((r) => r[3]), ys = fd.rows.map((r) => r[4]);
    const lo = Math.min(...xs, ...ys), hi = Math.max(...xs, ...ys);
    const sx = (v) => m.l + (v - lo) / (hi - lo) * (W - m.l - m.r), sy = (v) => H - m.b - (v - lo) / (hi - lo) * (H - m.t - m.b);
    const svg = figFrame(W, H);
    const tk = niceTicks(lo, hi, 6);
    axisX(svg, m.l, W - m.r, H - m.b, tk.map((v) => [sx(v), v]), (v) => String(v), 'δ measured (READ)');
    axisY(svg, m.l, H - m.b, m.t, tk.map((v) => [sy(v), v]), (v) => String(v), 'δ by the channel equation (PINNED)');
    svg.appendChild(svgEl('line', { x1: sx(lo), y1: sy(lo), x2: sx(hi), y2: sy(hi), class: 'ref' }));
    fd.rows.forEach((r) => svg.appendChild(svgEl('circle', { cx: sx(r[3]), cy: sy(r[4]), r: 3.2, fill: L_COLOR[r[2] % L_COLOR.length], 'fill-opacity': 0.75, stroke: 'none' })).append(svgEl('title', {}, `${symbolOf(r[0])} ${roman(r[1])} ${LSYM[r[2]] || r[2]}: δ ${r[3]} measured, ${r[4]} by equation`)));
    const ls = [...new Set(fd.rows.map((r) => r[2]))].sort((a, b) => a - b);
    ls.forEach((l, i) => { svg.appendChild(svgEl('circle', { cx: m.l + 14, cy: m.t + 12 + i * 15, r: 4, fill: L_COLOR[l % L_COLOR.length] })); svg.appendChild(svgEl('text', { x: m.l + 24, y: m.t + 16 + i * 15, class: 'tick' }, `ℓ = ${LSYM[l] || l} (${fd.rows.filter((r) => r[2] === l).length})`)); });
    const rep = (ix.fixtures || {}).equation_report || {};
    return { id: 'equation', title: 'The channel equation against every measured channel', svg,
      caption: `${fd.rows.length} measured channels: δ read from the spectra index (READ) against δ from the channel equation (PINNED), coloured by ℓ; the diagonal is agreement. rms ${rep.rms !== undefined ? rep.rms.toFixed(4) : '?'}, R² ${rep.R2 !== undefined ? rep.R2.toFixed(4) : '?'}, median |error| ${rep.median_abs_error !== undefined ? rep.median_abs_error.toFixed(4) : '?'} over the same rows. ${fd.source}`, status: 'DERIVED' };
  }
  function figResiduals(ix) {
    const fd = (ix.figure_data || {}).equation; if (!fd || !fd.rows.length) return null;
    const res = fd.rows.map((r) => r[3] - r[4]);
    const W = 560, H = 300, m = { l: 56, r: 16, t: 14, b: 44 };
    const lo = Math.min(...res), hi = Math.max(...res), nb = 30, bw = (hi - lo) / nb || 1;
    const bins = new Array(nb).fill(0); res.forEach((v) => { bins[Math.min(nb - 1, Math.floor((v - lo) / bw))] += 1; });
    const top = Math.max(...bins);
    const sx = (v) => m.l + (v - lo) / (hi - lo) * (W - m.l - m.r), sy = (c) => H - m.b - c / top * (H - m.t - m.b);
    const svg = figFrame(W, H);
    axisX(svg, m.l, W - m.r, H - m.b, niceTicks(lo, hi, 7).map((v) => [sx(v), v]), (v) => String(v), 'residual: δ measured − δ by equation');
    axisY(svg, m.l, H - m.b, m.t, niceTicks(0, top, 5).map((v) => [sy(v), v]), (v) => String(v), 'channels');
    bins.forEach((c, i) => svg.appendChild(svgEl('rect', { x: sx(lo + i * bw) + 0.5, y: sy(c), width: Math.max(1, sx(lo + bw) - sx(lo) - 1), height: H - m.b - sy(c), fill: '#1f4e8c', 'fill-opacity': 0.7 })));
    if (lo < 0 && hi > 0) svg.appendChild(svgEl('line', { x1: sx(0), x2: sx(0), y1: m.t, y2: H - m.b, class: 'ref' }));
    const by = ((ix.fixtures || {}).equation_report || {}).by_l || [];
    return { id: 'residuals', title: 'The residual distribution', svg,
      caption: `${res.length} residuals in ${nb} bins; the dashed line is zero. By ℓ, rms: ${by.map((b) => `${LSYM[b.l] || b.l} ${b.rms.toFixed(3)} (${b.n})`).join(', ')}. DERIVED from the same rows as the figure above.`, status: 'DERIVED' };
  }
  function figCoverage(ix) {
    const lay = ix.layout || []; if (!lay.length) return null;
    const W = 720, H = 240, m = { l: 48, r: 12, t: 14, b: 40 };
    const zmax = Math.max(...lay.map((e) => e.Z)), top = Math.max(...lay.map((e) => e.counts.measured)) || 1;
    const sx = (z) => m.l + (z - 0.5) / zmax * (W - m.l - m.r), sy = (c) => H - m.b - c / top * (H - m.t - m.b);
    const svg = figFrame(W, H);
    axisX(svg, m.l, W - m.r, H - m.b, niceTicks(0, zmax, 12).filter((v) => v > 0).map((v) => [sx(v), v]), (v) => String(v), 'Z');
    axisY(svg, m.l, H - m.b, m.t, niceTicks(0, top, 4).map((v) => [sy(v), v]), (v) => String(v), 'measured cells');
    lay.forEach((e) => { const r = svgEl('rect', { x: sx(e.Z) - 2, y: sy(e.counts.measured), width: 4, height: H - m.b - sy(e.counts.measured), fill: e.populated ? '#1f4e8c' : '#999', 'fill-opacity': 0.8 }); r.append(svgEl('title', {}, `${e.symbol} (Z = ${e.Z}): ${e.counts.measured} measured of ${e.counts.rows} cells`)); svg.appendChild(r); });
    const t = ix.totals || {};
    return { id: 'coverage', title: 'Where the measurements are', svg,
      caption: `Measured cells per element, Z = 1 to ${zmax}: ${t.measured} measured of ${(t.rows || 0).toLocaleString()} cells in all; grey bars are elements the observed configurations table does not reach (Z > 108). DERIVED from the layout's counts.`, status: 'DERIVED' };
  }
  function figWalk(ix) {
    const rel = ix.relativistic || {}, walk = rel.walk; if (!walk || !walk.fields) return null;
    const fld = walk.fields[walk.primary] || walk.fields.hf || walk.fields.lx; if (!fld) return null;
    const ents = fld.entrants.filter((e) => e.margin_c137 !== null && e.margin_c137 !== undefined);
    const W = 720, H = 300, m = { l: 56, r: 12, t: 14, b: 40 };
    const zmax = Math.max(...ents.map((e) => e.Z));
    const vals = ents.flatMap((e) => [e.margin_c137, e.margin_cinf]).filter((v) => v !== null && v !== undefined && isFinite(v));
    const lo = 0, hi = Math.max(...vals);
    const sx = (z) => m.l + (z - 1) / (zmax - 1) * (W - m.l - m.r), sy = (v) => H - m.b - (v - lo) / (hi - lo) * (H - m.t - m.b);
    const svg = figFrame(W, H);
    axisX(svg, m.l, W - m.r, H - m.b, niceTicks(0, zmax, 12).filter((v) => v > 0).map((v) => [sx(v), v]), (v) => String(v), 'Z');
    axisY(svg, m.l, H - m.b, m.t, niceTicks(lo, hi, 5).map((v) => [sy(v), v]), (v) => String(v), 'margin, hartree');
    const path = (key, cls) => { const d = ents.map((e, i) => `${i ? 'L' : 'M'}${sx(e.Z).toFixed(1)},${sy(e[key]).toFixed(1)}`).join(''); svg.appendChild(svgEl('path', { d, class: cls, fill: 'none' })); };
    path('margin_c137', 'ln-a'); path('margin_cinf', 'ln-b');
    ents.filter((e) => e.displaced).forEach((e) => { const c = svgEl('circle', { cx: sx(e.Z), cy: sy(Math.min(e.margin_c137, e.margin_cinf)), r: 5, fill: 'none', stroke: '#b5651d', 'stroke-width': 1.6 }); c.append(svgEl('title', {}, `${e.symbol}: entrant ${e.c137} at c = 137.035999, ${e.cinf} at c → ∞`)); svg.appendChild(c); svg.appendChild(svgEl('text', { x: sx(e.Z), y: sy(Math.min(e.margin_c137, e.margin_cinf)) - 8, 'text-anchor': 'middle', class: 'tick' }, e.symbol)); });
    svg.appendChild(svgEl('line', { x1: m.l + 10, x2: m.l + 34, y1: m.t + 8, y2: m.t + 8, class: 'ln-a' })); svg.appendChild(svgEl('text', { x: m.l + 40, y: m.t + 12, class: 'tick' }, 'c = 137.035999'));
    svg.appendChild(svgEl('line', { x1: m.l + 10, x2: m.l + 34, y1: m.t + 24, y2: m.t + 24, class: 'ln-b' })); svg.appendChild(svgEl('text', { x: m.l + 40, y: m.t + 28, class: 'tick' }, 'c → ∞'));
    svg.appendChild(svgEl('circle', { cx: m.l + 22, cy: m.t + 40, r: 5, fill: 'none', stroke: '#b5651d', 'stroke-width': 1.6 })); svg.appendChild(svgEl('text', { x: m.l + 40, y: m.t + 44, class: 'tick' }, 'displaced between the settings'));
    return { id: 'walk', title: 'The reconstructed walk: the entrant\'s margin at both settings', svg,
      caption: `For every Z the gap in energy between the entrant channel and its runner-up, in the ${WALK_FIELD_LABEL[walk.primary] || walk.primary} field, at c = 137.035999 and at c → ∞; a ring marks an element whose entrant differs between the settings. A small margin is a contested row. RECONSTRUCTED: the walk is this repository's rebuild of the paper's chain, placed beside the paper's result and never in its place.`, status: 'RECONSTRUCTED' };
  }
  function figClosure(ix) {
    const c = ix.closure || {}, pl = c.placement || {}, jan = ((ix.fixtures || {}).closure || {}).janet || null;
    if (c.E === undefined) return null;
    const bars = [{ k: 'periodic, helium at 18', E: c.E, parts: c.decomposition ? [['forbidden (1d, 1p, 2d)', c.decomposition.forbidden, '#8b3a62'], ['deferred (3d, helium\'s slot)', c.decomposition.deferred, '#c9a227']] : [['E', c.E, '#1f4e8c']] },
      { k: 'periodic, helium at 2', E: pl.helium_at_2 ? pl.helium_at_2.E : null, parts: pl.helium_at_2 ? [['E', pl.helium_at_2.E, '#1f4e8c']] : [] },
      { k: 'Janet (n+ℓ, ℓ)', E: jan ? jan.E : null, parts: jan ? [['E', jan.E, '#1f4e8c']] : [] }].filter((b) => b.E !== null);
    const W = 560, H = 220, m = { l: 56, r: 16, t: 14, b: 44 };
    const top = Math.max(...bars.map((b) => b.E), 1);
    const sy = (v) => H - m.b - v / top * (H - m.t - m.b), bw = (W - m.l - m.r) / bars.length;
    const svg = figFrame(W, H);
    axisY(svg, m.l, H - m.b, m.t, niceTicks(0, top, 4).map((v) => [sy(v), v]), (v) => String(v), 'E = admitted − held');
    svg.appendChild(svgEl('line', { x1: m.l, x2: W - m.r, y1: H - m.b, y2: H - m.b, class: 'ax' }));
    bars.forEach((b, i) => { let acc = 0; const x = m.l + i * bw + bw * 0.25; b.parts.forEach(([name, v, col]) => { const r = svgEl('rect', { x, y: sy(acc + v), width: bw * 0.5, height: sy(acc) - sy(acc + v), fill: col, 'fill-opacity': 0.85 }); r.append(svgEl('title', {}, `${b.k}: ${name} ${v}`)); svg.appendChild(r); acc += v; }); svg.appendChild(svgEl('text', { x: x + bw * 0.25, y: sy(b.E) - 6, 'text-anchor': 'middle', class: 'lab' }, `E = ${b.E}`)); svg.appendChild(svgEl('text', { x: x + bw * 0.25, y: H - m.b + 16, 'text-anchor': 'middle', class: 'tick' }, b.k)); });
    return { id: 'closure', title: 'Closure across the layouts', svg,
      caption: `E, the cells ℛ admits and the layout does not hold, on the drawn periodic layout (${c.held} held, ${c.admitted} admitted; the split is 25 forbidden by ℓ ≤ n − 1 and 11 deferred), on the same layout with helium at group 2, and on the Janet layout. Computed at build with the order operator (PINNED); the split is READ.`, status: 'PINNED' };
  }
  function renderFigures() {
    const host = $('#figures-body'), ix = state.index;
    const figs = [figEquation(ix), figResiduals(ix), figCoverage(ix), figWalk(ix), figClosure(ix)].filter(Boolean);
    host.innerHTML = `<p class="note">Drawn in the browser from <code>data/index.js</code> when this dialog opens: no figure here is an image, and no number in one is typed. Each caption names the block it is drawn from and the status that block carries. Hover a mark for its value; download any figure as SVG.</p>`;
    figs.forEach((f) => {
      const fig = document.createElement('figure'); fig.className = 'data-fig'; fig.id = 'fig-' + f.id;
      const h = document.createElement('h3'); h.textContent = f.title; fig.appendChild(h);
      fig.appendChild(f.svg);
      const cap = document.createElement('figcaption'); cap.innerHTML = `${esc(f.caption)} ${badge(f.status)} <a href="#" data-dl="${f.id}">download SVG</a>`; fig.appendChild(cap);
      host.appendChild(fig);
    });
    host.querySelectorAll('a[data-dl]').forEach((a) => a.addEventListener('click', (ev) => {
      ev.preventDefault();
      const svg = host.querySelector('#fig-' + a.dataset.dl + ' svg').cloneNode(true);
      svg.setAttribute('xmlns', SVG_NS);
      const style = document.createElementNS(SVG_NS, 'style'); style.textContent = '.ax{stroke:#555;stroke-width:1}.tick{fill:#333;font-size:11px}.lab{fill:#333;font-size:12px}.ref{stroke:#999;stroke-dasharray:4 3}.ln-a{stroke:#1f4e8c;stroke-width:1.6}.ln-b{stroke:#b5651d;stroke-width:1.6;stroke-dasharray:5 3}';
      svg.prepend(style);
      const blob = new Blob([new XMLSerializer().serializeToString(svg)], { type: 'image/svg+xml' });
      const url = URL.createObjectURL(blob), dl = document.createElement('a'); dl.href = url; dl.download = `method-index-${a.dataset.dl}-${(state.index.meta || {}).commit || 'edition'}.svg`; dl.click();
      setTimeout(() => URL.revokeObjectURL(url), 2000);
    }));
  }

  function renderProvenance() {
    const ix = state.index, m = ix.meta || {}, t = ix.totals || {};
    const eq = ix.equation || null, col = ix.collapse || null, ins = ix.instruments || null, fx = ix.fixtures || null;
    let html = `
      <p>${esc(m.generator || '')}. Commit <code>${esc(m.commit || 'unknown')}</code>, built ${esc(m.built || '?')}. ${esc(m.names_note || '')}</p>
      <h3>Sources, with the md5 the store records and the md5 measured at build</h3>
      <div class="tbl-wrap"><table class="t"><thead><tr><th>file</th><th>role</th><th class="hide-narrow">recorded</th><th class="hide-narrow">measured</th><th class="hide-narrow"></th></tr></thead><tbody>
        ${(ix.sources || []).map((s) => { const ok = s.ok ? '<span class="ok">match</span>' : '<span class="bad">DRIFT</span>'; return `<tr><td class="wrap">${esc(s.file)}<div class="note only-narrow">recorded ${esc((s.md5_recorded || '?').slice(0, 12))} · measured ${esc((s.md5_measured || '?').slice(0, 12))} · ${ok}</div></td><td class="wrap" style="font-family:var(--font-body)">${esc(s.role)}</td><td class="hide-narrow">${esc((s.md5_recorded || '?').slice(0, 12))}</td><td class="hide-narrow">${esc((s.md5_measured || '?').slice(0, 12))}</td><td class="hide-narrow">${ok}</td></tr>`; }).join('')}
      </tbody></table></div>
      <h3>Totals</h3>
      <div class="stats">
        <div class="stat"><b>${t.populated}</b><span>elements populated </span></div>
        <div class="stat"><b>${t.csv_only}</b><span>spectra rows only</span></div>
        <div class="stat"><b>${(t.rows || 0).toLocaleString()}</b><span>cells = COORDINATES-2.13 rows</span></div>
        <div class="stat"><b>${t.measured}</b><span>measured</span></div>
        <div class="stat"><b>${t.exact}</b><span>exact</span></div>
        <div class="stat"><b>${t.witnessed}</b><span>witnessed</span></div>
      </div>`;
    if (eq || col) {
      html += `<h3>The equation and the collapse</h3><div class="fields">
        ${eq ? row('channel equation', `A = ${eq.A}, K = ${eq.K}, H = ${eq.H}`, eq.status, eq.source) : ''}
        ${eq && eq.E0 !== undefined ? row('exponent', `E0 = ${eq.E0}, E1 = ${eq.E1}${eq.exponent ? ` · ${esc(eq.exponent)}` : ''}`, eq.status, `${eq.source} (populate.E0, populate.E1)`) : ''}
        ${eq && Array.isArray(eq.form) ? row('form', eq.form.map((f) => `<code>${esc(f)}</code>`).join('<br>'), eq.status, 'read out of populate.channel_delta\'s docstring', true) : ''}
        ${col ? row('collapse C(Z, ℓ)', esc(col.form), col.status, 'the stated thresholds; the form inverted out of the computed column') : ''}
        ${col ? row('Z₀(ℓ)', Object.entries(col.Z0).map(([l, z]) => `ℓ=${esc(l)}: ${esc(z)}`).join(' · '), col.status, 'the Janet block openings') : ''}
        ${ix.caps ? row('the standing caps', Object.entries(ix.caps).map(([k, v]) => `${esc(k)}≤${esc(v)}`).join(' '), 'PINNED', '(n, e, l, k, f) = (3, 3, 1, 3, 1)') : ''}
      </div>`;
    }
    if (ins) {
      html += `<h3>Instruments carried verbatim (by inspect.getsource)</h3>
      <div class="tbl-wrap"><table class="t"><thead><tr><th>function</th><th>file</th><th class="num">line</th><th>status</th><th>source</th></tr></thead><tbody>
        ${Object.entries(ins).map(([k, v]) => `<tr><td>${esc(k)}</td><td>${esc(v.file || '')}</td><td class="num">${v.line || ''}</td><td>${badge(v.status)}</td><td class="wrap" style="font-family:var(--font-body)">${esc(v.source || '')}</td></tr>`).join('')}
      </tbody></table></div>
      <p class="note">The solver suite shows each one beside its browser-side mirror under "Instrument source".</p>`;
    } else {
      html += `<h3>Instruments</h3><p class="note">This build of <code>data/index.js</code> carries no <code>instruments</code> block; the solver suite's "Instrument source" will say so.</p>`;
    }
    if (fx) {
      const er = fx.equation_report, cl = fx.closure, pa = fx.pauli, hz = fx.hydrogenic_zero, cs = fx.coefficient_roundtrip_sample;
      html += `<h3>Fixtures the browser-side selftests must reproduce</h3>
      <p class="note">${esc(fx.note || '')}</p>
      <div class="fields">
        ${er ? row('equation report', `${er.channels} channels · rms ${fmt(er.rms)} · R² ${fmt(er.R2)} · median |error| ${fmt(er.median_abs_error)}`, 'DERIVED', 'populate.equation_report over the measured rows, computed at build') : ''}
        ${er && er.by_l ? row('by ℓ', er.by_l.map((b) => `ℓ=${b.l}: n=${b.n} rms ${fmt(b.rms)}`).join(' · '), 'DERIVED', 'populate.equation_report') : ''}
        ${cl && cl.periodic ? row('closure, periodic', `held ${cl.periodic.held} · admitted ${cl.periodic.admitted} · E = ${cl.periodic.E}`, cl.status || 'PINNED', cl.operator || '') : ''}
        ${cl && cl.janet ? row('closure, Janet', `held ${cl.janet.held} · admitted ${cl.janet.admitted} · E = ${cl.janet.E} · box ${cl.janet.box}`, cl.status || 'PINNED', 'the elements\' own distinct Janet cells; not cypher.py\'s 22-cell fixture') : ''}
        ${hz ? row('hydrogenic zero', `channel_delta(${hz.Z}, ${hz.charge}, ${hz.l}) = ${hz.delta_equation}`, hz.status, hz.source) : ''}
        ${pa ? row('Pauli bound', pa.rows.map((r) => `${esc(r.label)}: B = ${esc(r.B)}`).join(' · '), pa.status, pa.source) : ''}
        ${cs ? row('coefficient round-trip sample', `${cs.rows.length} measured rows${cs.note ? ` — ${esc(cs.note)}` : ''}`, null, undefined, true) : ''}
      </div>`;
    } else {
      html += `<h3>Fixtures</h3><p class="note">This build of <code>data/index.js</code> carries no <code>fixtures</code> block; a solver selftest that needs them will report that rather than pass.</p>`;
    }
    html += `<h3>Every axis and its status</h3>
      <div class="tbl-wrap"><table class="t"><thead><tr><th>axis</th><th>status</th><th>source</th></tr></thead><tbody>
        ${(ix.axes || []).map((a) => `<tr><td>${esc(a.axis)}</td><td>${badge(a.status)}</td><td class="wrap" style="font-family:var(--font-body)">${esc(a.source)}</td></tr>`).join('')}
      </tbody></table></div>
      <h3>Status vocabulary</h3>
      <div class="fields">${Object.entries(ix.status_legend || {}).map(([k, v]) => row(k, esc(v), k, undefined, true)).join('')}</div>
      <h3>Caveats</h3>
      <ul>${(ix.caveats || []).map((v) => `<li>${esc(v.text)}</li>`).join('')}</ul>
      <h3>Element files</h3>
      <p class="note">${(ix.manifest || []).length} files under <code>data/elements/</code>, ${((ix.manifest || []).reduce((a, x) => a + (x.bytes || 0), 0) / 1e6).toFixed(1)} MB, each md5 recorded in <code>data/index.js</code>; <code>python3 tools/webindex.py --verify</code> checks them.${ix.protocol ? ` Protocol: ${esc(ix.protocol.index)}; ${esc(ix.protocol.element)} — ${esc(ix.protocol.why)}.` : ''}</p>`;
    const cite = m.cite || null, dls = ix.downloads || [], hist = m.history || [];
    if (cite) {
      html += `<h3>How to cite</h3><p class="note">The site as a whole, at this edition. A paper carries its own cite line under Papers, and every node's plate offers a citation naming its path.</p>
        <div class="cite-box"><span class="mono">${esc(cite.text)}</span></div>
        <details class="note"><summary>BibTeX</summary><pre class="mono">${esc(cite.bibtex || '')}</pre></details>`;
    }
    if (dls.length) {
      html += `<h3>Downloads</h3><p class="note">The data the site reads, as files, each with the md5 recorded at build where the file is a single blob.</p>
        <div class="tbl-wrap"><table class="t"><thead><tr><th>file</th><th>what</th><th class="hide-narrow">bytes</th><th class="hide-narrow">md5</th></tr></thead><tbody>
        ${dls.map((d) => `<tr><td class="wrap">${d.file.includes('<') ? esc(d.file) : `<a href="${esc(d.file)}" download>${esc(d.file)}</a>`}</td><td class="wrap">${esc(d.what || '')}</td><td class="hide-narrow">${d.bytes ? d.bytes.toLocaleString() : ''}</td><td class="hide-narrow mono">${esc((d.md5 || '').slice(0, 12))}</td></tr>`).join('')}
        </tbody></table></div>
        <p class="note">The repository itself, with every generator and its selftest: <a href="https://github.com/lach-matt/Claude-Method-Works" target="_blank" rel="noopener noreferrer">github.com/lach-matt/Claude-Method-Works</a>.</p>`;
    }
    if (hist.length) {
      html += `<h3>Editions</h3><p class="note">Every commit that changed the site or its generator, oldest first; the current edition is the last row. A note is the site's own description of the change; the commit is the record.</p>
        <div class="tbl-wrap"><table class="t"><thead><tr><th>date</th><th>edition</th><th>change</th><th class="hide-narrow">files</th></tr></thead><tbody>
        ${hist.map((h) => `<tr${m.commit && (m.commit.startsWith(h.commit) || h.commit.startsWith(m.commit)) ? ' class="is-current"' : ''}><td>${esc(h.date)}</td><td><a href="${esc(h.url)}" target="_blank" rel="noopener noreferrer" class="mono">${esc(h.commit)}</a></td><td class="wrap">${esc(h.note || '')}</td><td class="hide-narrow">${h.files}</td></tr>`).join('')}
        </tbody></table></div>`;
    }
    $('#provenance-body').innerHTML = html;
  }

  // ---------------------------------------------------------------- search
  function suggestions(q) {
    const L = state.index.layout;
    const toks = q.trim().split(/\s+/).filter(Boolean);
    if (!toks.length) return [];
    const t0 = toks[0].toLowerCase();
    let els = L.filter((e) => e.symbol.toLowerCase() === t0 || String(e.Z) === t0);
    const exact = els.length === 1;
    if (!els.length) els = L.filter((e) => e.symbol.toLowerCase().startsWith(t0) || (e.name && e.name.toLowerCase().startsWith(t0)));
    if (!els.length) els = L.filter((e) => e.name && e.name.toLowerCase().includes(t0));
    if (toks.length === 1 || !exact) {
      return els.slice(0, 10).map((e) => ({ path: e.symbol, note: `${e.name || ''} · Z=${e.Z}${e.populated ? '' : ' · rows only'}`, go: [e.Z] }));
    }
    const e = els[0];
    const c = fromRoman(toks[1].toUpperCase()) || parseInt(toks[1], 10);
    if (!c || c < 1 || c > e.Z) return [{ path: `${e.symbol} ?`, note: `stage I–${roman(e.Z)}`, go: [e.Z] }];
    if (toks.length === 2) return [{ path: `${e.symbol} ${roman(c)}`, note: `ion, Nₑ = ${e.Z - c + 1}`, go: [e.Z, c] }];
    const l = parseL(toks[2]);
    if (Number.isNaN(l) || l < 0 || l > 7) return [{ path: `${e.symbol} ${roman(c)} ?`, note: 'ℓ = s p d f g h, or 0–7', go: [e.Z, c] }];
    if (toks.length === 3) return [{ path: `${e.symbol} ${roman(c)} ${LSYM[l] || l}`, note: `channel ℓ=${l}`, go: [e.Z, c, l] }];
    const mult = parseInt(toks[3], 10);
    return [{ path: `${e.symbol} ${roman(c)} ${LSYM[l] || l} ${mult || '?'}`, note: 'cell, 2S+1', go: [e.Z, c, l, mult || undefined] }];
  }
  function setupSearch() {
    const q = $('#q'), ul = $('#suggest');
    let items = [], active = -1;
    const render = () => {
      ul.innerHTML = items.map((it, i) => `<li id="sg-${i}" role="option" aria-selected="${i === active}" class="${i === active ? 'is-active' : ''}"><span class="s-path">${esc(it.path)}</span><span class="s-note">${esc(it.note)}</span></li>`).join('');
      ul.hidden = items.length === 0;
      q.setAttribute('aria-expanded', String(items.length > 0));
      if (active >= 0 && items.length) q.setAttribute('aria-activedescendant', `sg-${active}`); else q.removeAttribute('aria-activedescendant');
      ul.querySelectorAll('li').forEach((li, i) => li.addEventListener('mousedown', (ev) => { ev.preventDefault(); go(items[i]); }));
    };
    const go = (it) => { if (!it) return; ul.hidden = true; q.blur(); goToPath(...it.go); };
    q.addEventListener('input', () => { items = suggestions(q.value); active = items.length ? 0 : -1; render(); });
    q.addEventListener('focus', () => { items = suggestions(q.value); render(); });
    q.addEventListener('blur', () => { setTimeout(() => { ul.hidden = true; }, 120); });
    q.addEventListener('keydown', (ev) => {
      if (ev.key === 'ArrowDown') { active = Math.min(items.length - 1, active + 1); render(); ev.preventDefault(); }
      else if (ev.key === 'ArrowUp') { active = Math.max(0, active - 1); render(); ev.preventDefault(); }
      else if (ev.key === 'Escape') { q.blur(); ul.hidden = true; }
    });
    $('#search').addEventListener('submit', (ev) => { ev.preventDefault(); if (!items.length) items = suggestions(q.value); go(items[active] || items[0]); });
  }

  // ---------------------------------------------------------------- input
  function setupPointer() {
    const pts = new Map();
    let dragged = false, last = null, pinch = null;
    canvas.addEventListener('pointerdown', (ev) => {
      canvas.setPointerCapture(ev.pointerId);
      pts.set(ev.pointerId, { x: ev.clientX, y: ev.clientY });
      dragged = false; last = { x: ev.clientX, y: ev.clientY, x0: ev.clientX, y0: ev.clientY, mode: null };
      if (pts.size === 2) {
        const [a, b] = [...pts.values()];
        pinch = { d: Math.hypot(a.x - b.x, a.y - b.y), k: state.cam.k, zoom: (state.orbit || orbitHome()).zoom, mx: (a.x + b.x) / 2, my: (a.y + b.y) / 2 };
      }
      canvas.classList.add('is-dragging');
    });
    const hoverKey = (n) => n ? `${n.kind}:${n.Z || ''}:${n.p || ''}:${n.g || ''}:${n.charge || ''}:${n.l === undefined ? '' : n.l}:${n.mult || ''}` : '';
    canvas.addEventListener('pointermove', (ev) => {
      const rect = canvas.getBoundingClientRect();
      if (!pts.has(ev.pointerId)) {
        // no button down: a hover, for the plane's cells and ghosts
        if (ev.pointerType === 'mouse') {
          const n = state.view === 'lattice' ? null : hit(ev.clientX - rect.left, ev.clientY - rect.top);
          const key = hoverKey(n);
          if (key !== state.hoverKey) { state.hoverKey = key; state.hover = n; requestDraw(); }
          canvas.style.cursor = n ? 'pointer' : (state.view === 'lattice' ? 'grab' : 'grab');
        }
        return;
      }
      pts.set(ev.pointerId, { x: ev.clientX, y: ev.clientY });
      if (pts.size === 2 && pinch) {
        const [a, b] = [...pts.values()];
        const d = Math.hypot(a.x - b.x, a.y - b.y);
        const mx = (a.x + b.x) / 2 - rect.left, my = (a.y + b.y) / 2 - rect.top;
        if (state.view === 'lattice') {
          const o = state.orbit || orbitHome();
          o.zoom = Math.max(0.25, Math.min(16, pinch.zoom * (d / pinch.d)));
          const cmx = (a.x + b.x) / 2, cmy = (a.y + b.y) / 2;
          o.dx = (o.dx || 0) + (cmx - pinch.mx); o.dy = (o.dy || 0) + (cmy - pinch.my); pinch.mx = cmx; pinch.my = cmy;
          state.orbit = o; requestDraw();
        }
        else zoomAt(mx, my, (pinch.k * (d / pinch.d)) / state.cam.k);
        dragged = true;
        return;
      }
      if (pts.size === 1 && last) {
        const dx = ev.clientX - last.x, dy = ev.clientY - last.y;
        if (Math.abs(dx) + Math.abs(dy) > 2) dragged = true;
        if (state.view === 'lattice') {
          const o = state.orbit || orbitHome();
          if (!last.mode) {
            const tx = ev.clientX - last.x0, ty = ev.clientY - last.y0;
            if (Math.abs(tx) + Math.abs(ty) >= 6) {
              // a slab taller than the canvas scrolls under a mostly vertical drag; anything else rotates
              const ov = state.latOverflow || {};
              last.mode = ev.shiftKey ? 'pan' : ((ov.top > 0 || ov.bottom > 0) && Math.abs(ty) > 1.4 * Math.abs(tx)) ? 'pan' : 'rotate';
            }
          }
          if (last.mode === 'pan' || (last.mode === null && ev.shiftKey)) { o.dx = (o.dx || 0) + (last.mode === 'pan' && !ev.shiftKey ? 0 : dx); o.dy = (o.dy || 0) + dy; if (state.scene) clampPan(state.scene, o); }
          else if (last.mode === 'rotate') { o.ry += dx * 0.008; o.rx = Math.max(-1.45, Math.min(1.45, o.rx + dy * 0.008)); }
          state.orbit = o;
        } else { state.cam.tx += dx; state.cam.ty += dy; state.anim = null; }
        last.x = ev.clientX; last.y = ev.clientY;
        requestDraw();
      }
    });
    const up = (ev) => {
      if (!pts.has(ev.pointerId)) return;
      const rect = canvas.getBoundingClientRect();
      const wasClick = !dragged && pts.size === 1;
      pts.delete(ev.pointerId);
      if (pts.size < 2) pinch = null;
      if (pts.size === 0) canvas.classList.remove('is-dragging');
      if (wasClick) {
        const sx = ev.clientX - rect.left, sy = ev.clientY - rect.top;
        const node = state.view === 'lattice' ? hitLattice(sx, sy) : hit(sx, sy);
        if (node && node.go) goToPath(...node.go);
        else if (node) select(node);
      }
    };
    canvas.addEventListener('pointerup', up);
    canvas.addEventListener('pointercancel', up);
    canvas.addEventListener('pointerleave', () => { if (state.hover) { state.hover = null; state.hoverKey = ''; requestDraw(); } });
    canvas.addEventListener('wheel', (ev) => {
      ev.preventDefault();
      const rect = canvas.getBoundingClientRect();
      const dy = ev.deltaMode === 1 ? ev.deltaY * 18 : ev.deltaMode === 2 ? ev.deltaY * 400 : ev.deltaY;
      zoomAt(ev.clientX - rect.left, ev.clientY - rect.top, Math.exp(-dy * 0.0016));
    }, { passive: false });
    canvas.addEventListener('dblclick', (ev) => {
      const rect = canvas.getBoundingClientRect();
      zoomAt(ev.clientX - rect.left, ev.clientY - rect.top, 1.8);
    });
  }

  function setupKeys() {
    // the canvas is focusable (tabindex on #canvas), and the shortcuts act only while it — or
    // nothing — has focus, so a button or a plate row keeps its own keys and the page its scroll
    window.addEventListener('keydown', (ev) => {
      const ae = document.activeElement;
      const inField = !!(ae && /INPUT|TEXTAREA|SELECT/.test(ae.tagName));
      if (ev.key === '/' && !inField) { ev.preventDefault(); $('#q').focus(); $('#q').select(); return; }
      if (inField) return;
      const onCanvas = !ae || ae === document.body || wrap.contains(ae);
      if (!onCanvas) return;
      if (ev.key === 'Escape') { if (document.querySelector('dialog[open]')) return; goUp(); }
      else if (ev.key === 'h' || ev.key === 'H') select(rootNode);
      else if (ev.key === '+' || ev.key === '=') zoomAt(W() / 2, H() / 2, 1.5);
      else if (ev.key === '-' || ev.key === '_') zoomAt(W() / 2, H() / 2, 1 / 1.5);
      else if (ev.key.startsWith('Arrow') && state.view === 'lattice') {
        const o = state.orbit || orbitHome();
        if (ev.key === 'ArrowLeft') o.ry -= 0.12; if (ev.key === 'ArrowRight') o.ry += 0.12;
        const ov = state.latOverflow || {}; const scrolls = ov.top > 0 || ov.bottom > 0;
        if (ev.key === 'ArrowUp') { if (scrolls) { o.dy = (o.dy || 0) + 60; if (state.scene) clampPan(state.scene, o); } else o.rx = Math.max(-1.45, o.rx - 0.12); }
        if (ev.key === 'ArrowDown') { if (scrolls) { o.dy = (o.dy || 0) - 60; if (state.scene) clampPan(state.scene, o); } else o.rx = Math.min(1.45, o.rx + 0.12); }
        state.orbit = o; requestDraw(); ev.preventDefault();
      }
      else if (ev.key.startsWith('Arrow')) {
        const d = 60;
        if (ev.key === 'ArrowLeft') state.cam.tx += d; if (ev.key === 'ArrowRight') state.cam.tx -= d;
        if (ev.key === 'ArrowUp') state.cam.ty += d; if (ev.key === 'ArrowDown') state.cam.ty -= d;
        state.anim = null; requestDraw(); ev.preventDefault();
      }
    });
  }
  function goUp() {
    const p = state.selected ? parentOf(state.selected) : null;
    select(p || rootNode);
  }

  const sysLight = window.matchMedia ? window.matchMedia('(prefers-color-scheme: light)') : { matches: false, addEventListener() {} };
  function effectiveTheme() {
    // Light is the default, as a reference work is read; dark only when stamped explicitly, by
    // the toggle or by the host.
    return document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
  }
  function setupChrome() {
    $('#z-in').addEventListener('click', () => zoomAt(W() / 2, H() / 2, 1.5));
    $('#z-out').addEventListener('click', () => zoomAt(W() / 2, H() / 2, 1 / 1.5));
    $('#z-home').addEventListener('click', () => select(rootNode, { reveal: false }));
    $('#btn-up').addEventListener('click', goUp);
    $('#btn-canvas').addEventListener('click', revealCanvas);
    const legend = $('#legend'), legendBtn = $('#legend-toggle');
    const setLegend = (open, remember) => {
      legend.classList.toggle('is-collapsed', !open); legendBtn.setAttribute('aria-expanded', String(open));
      if (remember) { try { localStorage.setItem('key', open ? 'open' : 'closed'); } catch (e) { /* private window */ } }
    };
    legendBtn.addEventListener('click', () => setLegend(legend.classList.contains('is-collapsed'), true));
    legend.querySelectorAll('.legend-seg button').forEach((b) => b.addEventListener('click', () => setCellColor(b.dataset.color)));
    // the key folds by default so the table and the lattice stand clear; a reader's choice is kept
    let keyOpen = false;
    try { keyOpen = localStorage.getItem('key') === 'open'; } catch (e) { /* none */ }
    setLegend(keyOpen && !isPhone());
    $('#btn-provenance').addEventListener('click', () => $('#dlg-provenance').showModal());
    if (state.index.particles || state.index.particle_index) $('#btn-particles').addEventListener('click', () => { if (!$('#particles-body').innerHTML) renderParticles(); $('#dlg-particles').showModal(); });
    else $('#btn-particles').hidden = true;
    $('#btn-references').addEventListener('click', () => { if (!$('#references-body').innerHTML) renderReferences(); $('#dlg-references').showModal(); });
    $('#btn-papers').addEventListener('click', () => { if (!$('#papers-body').innerHTML) renderPapers(); $('#dlg-papers').showModal(); });
    $('#btn-figures').addEventListener('click', () => { renderFigures(); $('#dlg-figures').showModal(); });
    $('#btn-glossary').addEventListener('click', () => $('#dlg-glossary').showModal());
    $('#btn-help').addEventListener('click', () => $('#dlg-help').showModal());
    document.querySelectorAll('.dlg-close').forEach((b) => b.addEventListener('click', () => $('#' + b.dataset.close).close()));
    document.querySelectorAll('dialog').forEach((d) => d.addEventListener('click', (ev) => { if (ev.target === d) d.close(); }));
    document.querySelectorAll('.seg-btn[data-layout]').forEach((b) => b.addEventListener('click', () => setLayout(b.dataset.layout)));
    document.querySelectorAll('.seg-btn[data-elview]').forEach((b) => b.addEventListener('click', () => setElementView(b.dataset.elview)));
    $('#btn-theme').addEventListener('click', () => {
      const next = effectiveTheme() === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      try { localStorage.setItem('theme', next); } catch (e) { /* private window */ }
      readColors(); requestDraw();
    });
    sysLight.addEventListener('change', () => { readColors(); requestDraw(); });
    window.addEventListener('hashchange', () => applyHash());
    new ResizeObserver(resize).observe(wrap);
    if ('IntersectionObserver' in window) {
      new IntersectionObserver((es) => {
        const en = es[es.length - 1];
        canvasVisible = en.isIntersecting || en.intersectionRatio > 0;
        if (canvasVisible) requestDraw();
      }).observe(wrap);
    }
  }

  // the edition: which build of the data this page reads, from data/index.js's own meta
  function setupEdition() {
    const m = (state.index && state.index.meta) || {};
    const commit = (m.commit || '').slice(0, 7), built = (m.built || '').slice(0, 10);
    const ed = $('#edition');
    if (ed) ed.textContent = commit ? `edition ${commit} · ${built}` : '';
    const foot = `<span><b>The Method Index</b> — every element on every axis of every index.</span>
      <span>Data generated by <span class="mono">tools/webindex.py</span> over <span class="mono">tools/populate.py</span>; every value carries the status the data gives it, and the explorer computes nothing.</span>
      ${commit ? `<span>Edition <span class="mono">${esc(commit)}</span>, built ${esc(built)}.</span>` : ''}
      <button type="button" class="ghost" data-act="open-prov">Provenance and sources</button>`;
    for (const id of ['#foot', '#side-foot']) {
      const el = $(id);
      if (!el) continue;
      el.innerHTML = foot;
      el.querySelectorAll('[data-act="open-prov"]').forEach((b) => b.addEventListener('click', () => $('#dlg-provenance').showModal()));
    }
  }

  function rebuildTableScene() { if (state.scene && state.scene.kind === 'table') { buildFrames(); state.scene = buildTableScene(); if (state.orbit) fitOrbit(state.scene, state.orbit); updateCaption(); requestDraw(); } }
  function setLayout(mode) {
    if (mode === state.layout) return;
    state.layout = mode;
    document.querySelectorAll('.seg-btn[data-layout]').forEach((b) => b.classList.toggle('is-on', b.dataset.layout === mode));
    buildFrames();
    if (mode !== 'lattice' && state.scene && state.scene.kind === 'index') state.scene = null;
    if (mode !== 'table3d' && state.scene && state.scene.kind === 'table') state.scene = null;
    const sel = state.selected || rootNode;
    if (sel.kind === 'ghost' && mode !== 'table' && mode !== 'table3d') select(rootNode, { reveal: false });
    else select(sel, { setHash: false, reveal: false });
  }

  // ---------------------------------------------------------------- assistant: the console
  const HELP = `console — deterministic, answered from the loaded data; nothing is computed here.
  help                this text
  go <path>           navigate: go Fe · go Fe II · go Fe II d · go Fe II d 3
  axes                every axis with its status and source
  closure             ℛ over the layouts: held, admitted, E
  sources             the files behind the data, md5 recorded against md5 measured
  caveats             the caveats that travel with every value
  count               the totals
  measured <El>       the element's measured rows
  residuals <El>      its measured rows: δ, δ by equation, residual
  B <El>              rows where B in the csv disagrees with B computed, and rows where B is not a bound
  ladder <El>         the Λ₈ steps, with any failing constraint
  limits <El>         the bound the csv records on its cells, by kind; series limits as printed
  relativistic        the eleven elements displaced at c → ∞ (READ; the construction is not held), and the reconstruction beside them
  walk <El>           the element in the reconstructed walk at both settings (RECONSTRUCTED; tools/lowdin_walk.py)
  lattice             the whole index as a lattice: sites, known cells, the axes and their source
  particles           what the sources state of the binders and particles beyond the electron
  particle <term>     one of them: muon, pion, tau, antimatter, positronium, antiprotonic, photon, quark, boson, neutrino …
  references [term]   every arXiv and DOI identifier the sources print, or those whose citing line mentions <term>
  papers              the released papers held here, with their md5s
  figures             what the Figures dialog draws
  cite                the site's cite line at this edition
  history             every edition of the site
  glossary            where the terms are defined
  check <text>        the machine check over pasted text with the markers ⟦path⟧ ⟪f(args) = v⟫ ⦃equation⦄
<El> is a symbol, a Z or a name; the element is loaded if it is not yet. An unknown input prints this text.`;

  function findElement(tok) {
    if (!tok) return null;
    const t = tok.toLowerCase();
    const L = state.index.layout;
    return L.find((e) => e.symbol.toLowerCase() === t) || L.find((e) => String(e.Z) === t) || L.find((e) => e.name && e.name.toLowerCase() === t) || null;
  }
  const st = (s) => `[${s}]`;
  async function withElement(tok, fn) {
    const e = findElement(tok);
    if (!e) return tok ? `no element "${tok}" in the index (symbol, Z or name)` : 'name an element: symbol, Z or name';
    let rec;
    try { rec = await ensureElement(e.Z); } catch (err) { return `${e.symbol}: ${err.message}`; }
    return fn(e, rec);
  }
  function measuredRows(rec) {
    const out = [];
    for (const ch of rec.channels) for (const m of ch.measured) if (m.grade === 'measured') out.push({ ch, m });
    return out;
  }
  const cellName = (sym, ch, m) => `${sym} ${roman(ch.charge)} ${LSYM[ch.l] || ch.l} 2S+1=${m.mult}`;

  async function consoleAnswer(input) {
    const q = input.trim();
    if (!q) return HELP;
    const toks = q.split(/\s+/);
    const cmd = toks[0].toLowerCase();
    const ix = state.index;
    const ax = (name) => { const a = axisStatus(name); return a ? a.status : '—'; };
    switch (cmd) {
      case 'help': return HELP;
      case 'particles': {
        const pt = ix.particles; if (!pt) return ix.particle_index ? `the particle indexes: ${ix.particle_index.indexes.map((x) => x.title + ' (' + x.members + ' members, ' + x.cells + ' cells, K' + x.cell.channel + ')').join('; ')}; ${ix.particle_index.accounting.identity}. Open Particles for every member with its statuses.` : 'this build of the index carries no particles block';
        const w = pt.window;
        return [`${pt.status_note}`,
          `  window [${w.m_e[0]}, ${w.m_e[1]}] m_e ${st(w.status)}; occupants muon ${w.occupants.muon}, pion ${w.occupants.pion}; the muon interior by ${w.interior.below}x and ${w.interior.above}x`,
          `  muon: mass ${pt.muon.mass_m_e.printed} m_e printed, ${pt.muon.mass_m_e.PDG} PDG (fault ${pt.muon.mass_m_e.fault}); instrument tools/mucf.py, ${pt.muon.instrument.status_table.length} inputs with statuses; solver mode 8`,
          `  excluded (${pt.exclusions.rows.length} rows): ` + pt.exclusions.rows.map((r) => r.excluded).join(' | '),
          `  antimatter ${st(pt.antimatter.status)}: ${pt.antimatter.cpt.quote}`,
          `  reduced mass: ` + pt.antimatter.reduced_mass.systems.map((x) => `${x.system} ${x.mu_over_me} (${x.radius_A} A)`).join('; '),
          `  antiprotonic helium: cell (${pt.antiprotonic_helium.cell.join(', ')}), ${pt.antiprotonic_helium.routes.map((r) => r.route + ' ' + r.MHz + ' +/- ' + r.pm + ' MHz').join('; ')}, ${pt.antiprotonic_helium.agreement_sigma} sigma ${st('READ')}`,
          `  photon: E = ${pt.photon.E} over the dipole selection index; ${pt.photon.claim.quote}`,
          `  constants: ${pt.constants.count} of Lambda_phys ${st(pt.constants.status)}`,
          `  prose-only: ` + pt.prose_only.map((r) => r.id + ' ' + r.label).join('; '),
          `  absent ${st(pt.absent.status)}: ` + Object.keys(pt.absent.terms).map((t) => `${t} ${pt.absent.terms[t].occurrences}`).join(', '),
          `  scope: ` + pt.scope.map((x) => x.name).join('; ')].join('\n');
      }
      case 'particle': {
        const pt = ix.particles; if (!pt) return ix.particle_index ? `the particle indexes: ${ix.particle_index.indexes.map((x) => x.title + ' (' + x.members + ' members, ' + x.cells + ' cells, K' + x.cell.channel + ')').join('; ')}; ${ix.particle_index.accounting.identity}. Open Particles for every member with its statuses.` : 'this build of the index carries no particles block';
        const term = toks.slice(1).join(' ').toLowerCase();
        if (!term) return 'name a particle: muon, pion, tau, kaon, antiproton, positron, antihydrogen, positronium, antiprotonic helium, photon, boson, quark, neutrino, gluon, Higgs';
        const flat = JSON.stringify(pt, null, 1);
        const out = [];
        const w = pt.window;
        if (/muon/.test(term)) out.push(`muon: ${w.occupants.muon} m_e printed (PDG ${pt.muon.mass_m_e.PDG}, fault ${pt.muon.mass_m_e.fault}); the window's one occupant, interior by ${w.interior.below}x and ${w.interior.above}x ${st('READ')}; molecular bound states ${w.N_states.muon}; a muonic atom occupies the same lattice cell as its electronic twin (the lattice carries no scale); the balance is solver mode 8`);
        if (/pion/.test(term)) out.push(`pion: ${w.occupants.pion} m_e, inside the window and excluded — nuclear absorption preempts catalysis ${st('READ')}`);
        if (/tau/.test(term)) out.push(`tau: above ${w.m_e[1]} m_e; the molecular index degenerates to ${w.N_states.tau} bound states, no edge cell ${st('READ')}`);
        if (/kaon|antiproton|sigma|Σ/.test(term)) out.push(`π⁻, K⁻, p̄, Σ⁻: excluded, nuclear absorption preempts catalysis (paper section 6) ${st('READ')}; the antiproton also appears bound in antiprotonic helium, cell (${pt.antiprotonic_helium.cell.join(', ')})`);
        if (/positron|antimatter|antihydrogen|anti/.test(term)) out.push(`antimatter ${st(pt.antimatter.status)}: ${pt.antimatter.cpt.quote} ALPHA: antihydrogen 1S-2S agrees with hydrogen at ${pt.antimatter.alpha.value}. ${pt.antimatter.antihydrogen.quote}`);
        if (/positronium|muonic hydrogen|exotic|reduced/.test(term)) out.push(`reduced mass ${st(pt.antimatter.status)}: ` + pt.antimatter.reduced_mass.systems.map((x) => `${x.system} mu/m_e ${x.mu_over_me}, radius ${x.radius_A} A`).join('; '));
        if (/antiprotonic|helium/.test(term)) out.push(`antiprotonic helium ${st('READ')}: cell (${pt.antiprotonic_helium.cell.join(', ')}); ${pt.antiprotonic_helium.routes.map((r) => r.route + ' ' + r.MHz + ' +/- ' + r.pm + ' MHz').join('; ')}; agreement ${pt.antiprotonic_helium.agreement_sigma} sigma with no shared measurement; ${pt.antiprotonic_helium.scope}`);
        if (/photon|gamma/.test(term)) out.push(`photon ${st('READ')}: ${pt.photon.site.quote} ${pt.photon.claim.quote}`);
        if (/boson|quark|decuplet/.test(term)) out.push(pt.prose_only.filter((r) => /boson|decuplet|quark/i.test(r.label + r.quote)).map((r) => `${r.id} ${st('PROSE-ONLY')} ${r.label}: ${r.quote}`).join('\n') || 'no row');
        if (/electron/.test(term)) out.push(`electron: the lattice's own binder — every cell of the index; below the window (geometry, ${w.N_states.electron} molecular bound states) ${st('READ')}`);
        if (/proton|nucle/.test(term)) out.push(`proton: m_p/m_e = ${(pt.constants.rows.find((c) => /mass ratio/.test(c.name)) || {}).value} in Lambda_phys ${st('PINNED')}; nuclear supply 37 rows (Angeli & Marinova 2013; AME2020) — see the References dialog`);
        Object.keys(pt.absent.terms).forEach((t) => { if (term.includes(t.toLowerCase())) { const a = pt.absent.terms[t]; out.push(`${t}: ${a.occurrences ? a.occurrences + ' occurrences, first at ' + a.first.file + ' L' + a.first.line : 'absent from the sources — counted at build, not a cell of the lattice'} ${st(pt.absent.status)}`); } });
        return out.length ? out.join('\n') : `nothing in the particles block matches "${term}"` + (flat.toLowerCase().includes(term) ? ' by name, though the term occurs in a passage; open Particles' : '');
      }
      case 'check': {
        const text = q.slice(5).trim(); if (!text) return 'check <text>: runs the machine check over any pasted text that uses the markers ⟦path⟧, ⟪f(args) = v⟫ and ⦃equation⦄';
        const L = window.MI && window.MI.solverLib; if (!L || !L.checkAnswer) return 'the solver module is not loaded';
        const zs = new Set(); let mm; const erx = /⟦el\/(\d+)\//g; while ((mm = erx.exec(text)) !== null) zs.add(+mm[1]);
        await Promise.allSettled([...zs].map((Z) => ensureElement(Z)));
        if (/⟦pi\//.test(text) && ix.particle_index) await ensureParticleIndex().catch(() => null);
        const r = L.checkAnswer(text, askResolve, askCompute);
        return [r.summary, ...(r.retrieval.present ? r.retrieval.targets.map((t) => `  retrieval ${t.target}: ρ = ${t.rho}, ${t.verdict} (${t.routes.join(', ')})`) : []),
          ...r.sources.map((c) => `  ⟨⟨${c.text}⟩⟩ ${c.verdict}`), ...r.citations.map((c) => `  ⟦${c.path}⟧ ${c.verdict}${c.value !== null && c.value !== undefined ? ' — index: ' + JSON.stringify(c.value) + (c.status ? ' [' + c.status + ']' : '') : ''}`),
          ...r.computations.map((c) => `  ⟪${c.name}(${c.args.join(', ')})⟫ ${c.verdict}${typeof c.value === 'number' ? ' — page: ' + c.value : ''}`),
          ...r.equations.map((e) => `  ⦃${e.text}⦄ ${e.verdict}${e.result.atoms ? ' — ' + e.result.atoms.map((a) => a.element + ' ' + a.left + '→' + a.right).join(', ') + '; charge ' + e.result.charge.left + '→' + e.result.charge.right : ''}`)].join('\n');
      }
      case 'papers': {
        const pp = (ix.papers || {}).papers || []; if (!pp.length) return 'this build carries no papers block';
        return pp.map((p) => `  ${p.title}${p.subtitle ? ' — ' + p.subtitle : ''} · ${p.author} · ${p.held ? `${p.words.toLocaleString()} words, ${p.figures} figures, md5 ${p.md5.slice(0, 12)} ${p.md5 === p.md5_recorded ? '(matches the store)' : '(DRIFT)'}` : 'not yet held: ' + p.note}`).join('\n') + '\nOpen Papers to read one.';
      }
      case 'figures': return 'Figures drawn from the data at open: the channel equation against every measured channel; the residual distribution; where the measurements are; the reconstructed walk\'s margins at both settings; closure across the layouts. Open Figures to see them; each downloads as SVG.';
      case 'cite': { const c = (ix.meta || {}).cite; return c ? c.text : 'no cite line in this build'; }
      case 'history': case 'editions': { const h = (ix.meta || {}).history || []; return h.length ? h.map((r) => `  ${r.date}  ${r.commit}  ${r.note || ''}`).join('\n') : 'no edition history in this build'; }
      case 'glossary': return 'Open Glossary for every term and mark the site uses, defined in the site\'s own words: the statuses, cells and channels, the channel equation\'s terms, layouts and closure, the lattice, the relativistic limit and the walk.';
      case 'references': case 'refs': {
        const rf = ix.references; if (!rf) return 'no references block in data/index.js';
        const term = toks.slice(1).join(' ').toLowerCase();
        const pick = (list) => list.filter((e) => !term || e.id.toLowerCase().includes(term) || e.cites.some((c) => c.text.toLowerCase().includes(term) || c.paper.toLowerCase().includes(term)));
        const ax = pick(rf.arxiv), dx = pick(rf.doi);
        const line = (e) => `  ${e.url}  (${e.n} site${e.n === 1 ? '' : 's'}${e.cites.length ? '; quoted in ' + e.cites[0].paper : ''})`;
        return [`NIST ASD ${rf.nist_asd.url}  DOI ${rf.nist_asd.doi_url} ${st('READ')} — the one data source the index links itself; the query is not held`,
          `arXiv (${ax.length}${term ? ' matching' : ''}):`, ...ax.map(line), `DOI (${dx.length}${term ? ' matching' : ''}):`, ...dx.map(line),
          `compilations by species: ${Object.keys(rf.spectra_sources.by_species).length} species; only NIST ASD is linked`].join('\n');
      }
      case 'lattice': { const lat = ix.lattice; if (!lat) return 'no lattice block in data/index.js'; return `${lat.index} ${st(lat.status)}\n  axes: x ${lat.axes.x}; y ${lat.axes.y}; z ${lat.axes.z}\n  ${lat.sites.toLocaleString()} sites (${lat.slab}); ${lat.known.length.toLocaleString()} known cells: ${lat.counts.measured} measured, ${lat.counts.exact} exact, over ${lat.counts.known_sites} sites\n  drawing ${st(lat.drawing)}: ${lat.cube.note}\n  source: ${lat.source}`; }
      case 'go': {
        const it = suggestions(toks.slice(1).join(' '))[0];
        if (!it || !it.go) return `no such path: ${toks.slice(1).join(' ')}`;
        const ok = await goToPath(...it.go);
        return `${ok ? '→' : '→ (nearest)'} ${pathText(state.selected)}`;
      }
      case 'axes':
        return (ix.axes || []).map((a) => `${a.axis.padEnd(16)} ${st(a.status).padEnd(16)} ${a.source}`).join('\n') || 'no axis table carried';
      case 'closure': {
        const c = ix.closure;
        const lines = [`${c.index}`, `operator: ${c.operator}`, `held ${c.held} ${st('PINNED')}   admitted ${c.admitted} ${st('PINNED')}   E = ${c.E} ${st('PINNED')} (admitted − held)   set aside ${c.set_aside} ${st('PINNED')}`,
          `denied cells (period, group): ${c.denied.map(([p, g]) => `(${p},${g})`).join(' ')}`];
        const fx = ix.fixtures && ix.fixtures.closure;
        if (fx && fx.janet) lines.push(`Janet (n+ℓ, ℓ), the elements' own cells: held ${fx.janet.held}  admitted ${fx.janet.admitted}  E = ${fx.janet.E}  box ${fx.janet.box} ${st(fx.status || 'PINNED')}`);
        else lines.push('Janet figures: not carried in this build of data/index.js (no fixtures.closure block)');
        return lines.join('\n');
      }
      case 'sources':
        return (ix.sources || []).map((s) => `${s.ok ? 'match' : 'DRIFT'}  ${s.file}\n       recorded ${(s.md5_recorded || '?').slice(0, 12)}  measured ${(s.md5_measured || '?').slice(0, 12)}  — ${s.role}`).join('\n') || 'no sources carried';
      case 'caveats':
        return (ix.caveats || []).map((v) => `${v.id}: ${v.text}`).join('\n\n') || 'no caveats carried';
      case 'count': {
        const t = ix.totals;
        return `elements populated ${t.populated} · spectra rows only ${t.csv_only}\ncells ${t.rows} = measured ${t.measured} + exact ${t.exact} + computed ${t.computed}; witnessed ${t.witnessed}\ncommit ${ix.meta.commit || '?'} · built ${ix.meta.built}`;
      }
      case 'limits':
        return withElement(toks[1], (e, rec) => {
          const counts = {}, lims = [];
          for (const ch of rec.channels) for (const m of ch.measured) {
            const k = limitKind(m.bound_note) || 'unclassified';
            counts[k] = (counts[k] || 0) + 1;
            const mm = /^limit ([0-9.]+);/.exec(m.bound_note);
            if (mm) lims.push(`${cellName(e.symbol, ch, m).padEnd(22)} limit ${mm[1]} (as printed)`);
          }
          const lines = [`${e.symbol}: bound note ${st('READ')} · kind ${st('DERIVED')} by the rule data/index.js carries`];
          for (const k of LIMIT_KIND_ORDER) if (counts[k]) lines.push(`${(LIMIT_LABEL[k] || k).padEnd(34)} ${counts[k]}`);
          if (lims.length) lines.push('', 'series limits printed in the csv (no unit carried):', ...lims);
          return lines.join('\n');
        });
      case 'relativistic': {
        const rel = ix.relativistic;
        if (!rel) return 'no relativistic block in this build of data/index.js';
        const paper = (rel.sources || {}).paper || {};
        const lines = [`${rel.statement || ''} ${st('READ')}`, `source: ${paper.title || 'the Löwdin paper'} L${paper.eleven_line}; the SCF audit`, ''];
        for (const x of rel.eleven || []) lines.push(`${x.symbol.padEnd(3)} Z=${String(x.Z).padEnd(4)} ${(x.configuration || '').padEnd(24)} entrant ${x.entrant || '?'}`);
        if (rel.thorium) lines.push('', rel.thorium);
        lines.push('', `instrument: not held — ${(rel.instrument && rel.instrument.note) || ''}`, (rel.instrument && rel.instrument.note) || '');
        const walk = rel.walk;
        if (walk && walk.summary && walk.summary.compare) {
          const cp = walk.summary.compare;
          lines.push('', `the walk, reconstructed ${st('RECONSTRUCTED')} — ${walk.instrument} over ${walk.table.file} (md5 ${walk.table.md5.slice(0, 12)})`, walk.field);
          Object.keys(walk.summary.settings).sort().forEach((key) => {
            const sm = walk.summary.settings[key];
            lines.push(`  field ${sm.field || key.split(':')[0]}, c = ${sm.c || key.split(':')[1]}: entrant = observed gain at ${sm.agree} of ${sm.scored}; openings ${sm.openings.map((o) => `${o.channel}@${o.Z}`).join(' ')}; clause 1 violations ${sm.clause1_violations.length}, clause 2 exceptions ${sm.clause2_exceptions.length}${sm.clause2_exceptions.length ? ' (' + sm.clause2_exceptions.join(', ') + ')' : ''}`);
          });
          const fieldsCmp = walk.summary.fields || { [walk.primary || 'lx']: cp };
          Object.keys(fieldsCmp).sort().forEach((fld) => {
            const c = fieldsCmp[fld];
            lines.push(`  field ${fld}: displaced at c → ∞: ${c.displaced.length} — ${c.displaced.map((d) => `${d.symbol}(${d.entrant_c137}|${d.entrant_cinf})`).join(' ') || 'none'}`);
            lines.push(`    of the record's eleven: ${c.in_eleven.length} displaced here too${c.in_eleven.length ? ' (' + c.in_eleven.join(', ') + ')' : ''}; ${c.eleven_not_displaced.length} not${c.eleven_not_displaced.length ? ' (' + c.eleven_not_displaced.join(', ') + ')' : ''}; ${c.not_in_eleven.length} displaced here and not in the record${c.not_in_eleven.length ? ' (' + c.not_in_eleven.join(', ') + ')' : ''}`);
            if (c.thorium) lines.push(`    Th: ${c.thorium.entrant_c137} at c = 137.035999, ${c.thorium.entrant_cinf} at c → ∞ — ${c.thorium.identical ? 'identical' : 'different'}`);
          });
          const fc = walk.summary.fields_compare;
          if (fc) lines.push(`  the two fields at c = 137.035999: entrants differ at ${fc.entrants_differ.length} — ${fc.entrants_differ.map((d) => `${d.symbol}(lx ${d.lx}|hf ${d.hf})`).join(' ') || 'none'}`);
          lines.push(`  ${caveat('walk-reconstructed')}`);
        }
        return lines.join('\n');
      }
      case 'walk':
        return withElement(toks[1], (e, rec) => {
          const walk = (ix.relativistic || {}).walk, wr = rec && rec.walk;
          if (!walk) return 'no reconstructed walk in this build of data/index.js (LOWDIN-WALK.tsv was absent when webindex.py ran)';
          if (!wr) return `${e.symbol}: no walk row (the walk runs Z = 2 to 120)`;
          const lines = [`${e.symbol} (Z = ${e.Z}) in the reconstructed walk ${st('RECONSTRUCTED')} — ${walk.instrument} over ${walk.table.file}`];
          const order = [walk.primary].concat(Object.keys(wr.fields || {}).filter((k) => k !== walk.primary));
          for (const fld of order) {
            const wf = (wr.fields || {})[fld];
            if (!wf) continue;
            lines.push(`  field ${fld} — ${WALK_FIELD_LABEL[fld] || fld}`);
            for (const k of ['c137', 'cinf']) {
              const r = wf[k];
              if (!r) continue;
              lines.push(`    c = ${k === 'cinf' ? '∞' : '137.035999'}: entrant ${r.entrant} (D ${r.D_ent.toFixed(6)} Ha), runner-up ${r.runner_up} by ${r.margin === null ? '—' : r.margin.toFixed(6)}; field of (${e.Z}, ${r.cfg_prev}); scf ${r.scf_iterations}${r.converged ? '' : ' NOT CONVERGED'}`);
              lines.push(`      candidates: ${r.spectrum.map((x) => `${x.channel} ${x.D.toFixed(5)}`).join('  ')}`);
            }
            lines.push(`    displaced in this field: ${wf.displaced ? 'yes' : 'no'}${wf.c137 && wf.c137.observed_gain !== '-' ? `; observed gain ${wf.c137.observed_gain} (${wf.c137.agree === 'yes' ? 'the c = 137 entrant agrees' : 'the c = 137 entrant differs'}) ${st('READ')}` : ''}`);
          }
          lines.push(`  in the record: ${e.relativistic ? 'one of the eleven' : 'not among the eleven'} ${st('READ')}`);
          lines.push(`  ${caveat('walk-reconstructed')}`);
          return lines.join('\n');
        });
      case 'measured':
        return withElement(toks[1], (e, rec) => {
          const rows = measuredRows(rec);
          if (!rows.length) return `${e.symbol}: no measured rows`;
          return [`${e.symbol}: ${rows.length} measured rows (δ ${st(ax('delta measured'))}, grade and witness READ from COORDINATES-2.13)`]
            .concat(rows.map(({ ch, m }) => `${cellName(e.symbol, ch, m).padEnd(22)} δ=${fmtRead(m.delta)}  ${m.witness}  ${m.source}`)).join('\n');
        });
      case 'residuals':
        return withElement(toks[1], (e, rec) => {
          const rows = measuredRows(rec);
          if (!rows.length) return `${e.symbol}: no measured rows`;
          return [`${e.symbol}: δ ${st(ax('delta measured'))}   δ eq ${st(ax('delta equation'))}   residual = δ − δ eq ${st('DERIVED')}`]
            .concat(rows.map(({ ch, m }) => `${cellName(e.symbol, ch, m).padEnd(22)} δ=${fmtRead(m.delta)}  δ eq=${fmt(ch.delta_equation)}  residual=${fmt(m.residual)}`)).join('\n');
        });
      case 'b':
        return withElement(toks[1], (e, rec) => {
          const dis = [], nb = [];
          for (const ch of rec.channels) for (const m of ch.measured) {
            if (m.B_csv_is_not_a_bound) nb.push({ ch, m });
            else if (m.B_agrees === false) dis.push({ ch, m });
          }
          const cap = 60;
          const lines = [`${e.symbol}: B computed ${st(ax('B'))} against B in the csv ${st('READ')} — recorded, never repaired`];
          lines.push(`\n${dis.length} rows where B (csv) disagrees with B computed${dis.length > cap ? ` (first ${cap})` : ''}`);
          for (const { ch, m } of dis.slice(0, cap)) lines.push(`${cellName(e.symbol, ch, m).padEnd(22)} B csv=${m.B_csv}  B computed=${ch.B_computed}  (p=${ch.p}, n₀=${ch.n0})`);
          if (dis.length) lines.push(`caveat b-aufbau: ${caveat('b-aufbau')}`);
          lines.push(`\n${nb.length} rows where B in the csv is not a bound`);
          for (const { ch, m } of nb) lines.push(`${cellName(e.symbol, ch, m).padEnd(22)} B csv=${m.B_csv}  (a float; a dispersion, not a bound)  B computed=${ch.B_computed}`);
          if (nb.length) lines.push(`caveat b-overloaded: ${caveat('b-overloaded')}`);
          return lines.join('\n');
        });
      case 'ladder':
        return withElement(toks[1], (e, rec) => {
          if (!rec.lambda8 || !rec.lambda8.length) return `${e.symbol}: no Λ₈ ladder carried (${e.populated ? 'no steps in the record' : 'not populated above Z = 108'})`;
          const lines = [`${e.symbol}: ${rec.lambda8.length} Λ₈ steps ${st(ax('Lambda_8 cell'))} — the ionisation-ladder mapping; caps ${st(ax('caps'))}`];
          rec.lambda8.forEach((s, i) => {
            const fails = s.constraints.filter((c) => !c.holds);
            const within = Object.values(s.within_caps).every(Boolean);
            const need = Object.entries(s.caps_needed).filter(([k, v]) => v > ix.caps[k]).map(([k, v]) => `${k}≥${v}`).join(' ');
            lines.push(`${String(i + 1).padStart(2)}. ${roman(s.charge).padEnd(6)} ${s.from} → ${s.to}  (${s.cell.map((v) => v === null ? '·' : v).join(', ')})  constraints ${s.constraints.length - fails.length}/${s.constraints.length}  ${within ? 'within caps' : `OUTSIDE the caps: needs ${need}`}`);
            for (const f of fails) lines.push(`      fails: ${f.rule}  (${f.origin})`);
          });
          return lines.join('\n');
        });
      default:
        return `unknown input: ${q}\n\n${HELP}`;
    }
  }

  // ---------------------------------------------------------------- assistant: Claude (claude.ai artifact runtime only)
  const claude = { fn: null, ctl: null };
  const RUN_LABEL = { console: 'Ask', both: 'Ask · console + Claude' };
  function setupClaude() {
    const mode = $('#assist-mode'), run = $('#assist-run');
    run.textContent = RUN_LABEL.console;
    if (!(window.claude && typeof window.claude.use === 'function')) { mode.textContent = 'console'; return; }
    mode.textContent = 'console · Claude: checking …';
    let p;
    try { p = Promise.resolve(window.claude.use('sample')); } catch (e) { mode.textContent = 'console'; return; }
    p.then((fn) => {
      if (typeof fn === 'function') { claude.fn = fn; mode.textContent = 'console + Claude (claude.ai artifact)'; run.textContent = RUN_LABEL.both; }
      else mode.textContent = 'console';
    }).catch(() => { mode.textContent = 'console'; });
  }
  function hideClaude(reason) {
    claude.fn = null;
    $('#assist-mode').textContent = `console${reason ? ` · Claude ${reason}` : ''}`;
    $('#assist-run').textContent = RUN_LABEL.console;
  }
  const LIMIT = 12000;
  function recordForClaude(node) {
    if (!node || node.kind === 'root') {
      return { kind: 'index', meta: state.index.meta, closure: state.index.closure, totals: state.index.totals };
    }
    if (node.kind === 'ghost') return { kind: 'admitted-not-held cell', period: node.p, group: node.g, closure: state.index.closure };
    const rec = state.elements.get(node.Z);
    const e = state.index.layout.find((x) => x.Z === node.Z);
    if (node.kind === 'element') {
      if (!rec) return { kind: 'element', identity: { Z: e.Z, symbol: e.symbol }, note: 'record not loaded' };
      const measured = measuredRows(rec).map(({ ch, m }) => ({ charge: ch.charge, l: ch.l, mult: m.mult, delta: m.delta, delta_equation: ch.delta_equation, residual: m.residual, B_computed: ch.B_computed, B_csv: m.B_csv, B_agrees: m.B_agrees, witness: m.witness }));
      const full = {
        kind: 'element',
        identity: { Z: rec.Z, symbol: rec.symbol, shells: rec.shells_as_printed, level: rec.level, electron_count: rec.electron_count, electron_count_ok: rec.electron_count_ok },
        layout: { period: rec.period, group: rec.group, block: rec.block_letter, set_aside: rec.set_aside, janet_cell: rec.janet_cell },
        closure: rec.closure, configuration: rec.configuration, counts: e.counts,
        lambda8: (rec.lambda8 || []).map((s) => ({ charge: s.charge, from: s.from, to: s.to, cell: s.cell, constraints_holding: s.constraints.filter((c) => c.holds).length, constraints: s.constraints.length, within_caps: s.within_caps, caps_needed: s.caps_needed })),
        measured_rows: measured,
      };
      let out = full, txt = JSON.stringify(out);
      if (txt.length > LIMIT) { out = { ...full, lambda8: full.lambda8.map((s) => ({ charge: s.charge, from: s.from, to: s.to })), _note: 'lambda8 shortened to fit' }; txt = JSON.stringify(out); }
      if (txt.length > LIMIT) { out = { ...out, measured_rows: measured.slice(0, 40), _note: `${out._note}; measured rows truncated to 40 of ${measured.length}` }; }
      return out;
    }
    if (node.kind === 'ion') return { kind: 'ion', Z: node.Z, symbol: e.symbol, charge: node.charge, channels: node.rec, lambda8_step: node.step };
    if (node.kind === 'channel') return { kind: 'channel', Z: node.Z, symbol: e.symbol, charge: node.charge, l: node.l, channel: node.rec };
    if (node.kind === 'cell') return { kind: 'cell', Z: node.Z, symbol: e.symbol, charge: node.charge, l: node.l, mult: node.mult, cell: node.rec, channel: { p: node.parent.rec.p, n0: node.parent.rec.n0, B_computed: node.parent.rec.B_computed, C_of_Z: node.parent.rec.C_of_Z, delta_equation: node.parent.rec.delta_equation } };
    return null;
  }
  function claudePrompt(question) {
    const node = state.selected || rootNode;
    const rec = recordForClaude(node);
    const axes = (state.index.axes || []).map((a) => `${a.axis} | ${a.status} | ${a.source}`).join('\n');
    const cav = (state.index.caveats || []).map((c) => `- ${c.text}`).join('\n');
    return `You are answering a question about ONE record of The Method Index (read by tools/populate.py and serialised by tools/webindex.py). Strict rules:
- Answer ONLY from the RECORD, the AXIS/STATUS TABLE and the CAVEATS below. Nothing else is known to you.
- Every number you quote must be followed by its status in square brackets — READ, PINNED, DERIVED, RECOVERED or RECONSTRUCTED — as the axis table or the record gives it. If no status is given for a value, say so.
- If the record does not carry what is asked, answer "not in the record".
- Do no physics, arithmetic, inference or verification of your own. Never say anything is verified, validated, stable, confirmed or correct: this page computes nothing and you must not claim it did.
- At most 200 words. Plain prose, no headings.

SELECTED NODE: ${pathText(node)}
RECORD (JSON):
${JSON.stringify(rec)}

AXIS | STATUS | SOURCE
${axes}

CAVEATS:
${cav}

QUESTION: ${question}`;
  }


  // ---------------------------------------------------------------- ask a model, with a machine check
  // The page never answers a question itself. With a key saved in this browser it sends the
  // question to Claude with web search on, hands the model the data it has loaded as cited
  // lines, and then CHECKS the answer with the solver module's checker: every ⟦path⟧ resolved
  // against the data, every ⟪computation⟫ repeated with the page's own library, every
  // ⦃equation⦄ tallied for conservation. A mismatch is shown, never corrected.
  const ASK_KEY = 'ask.settings';
  function askSettings() {
    let s = {};
    try { s = JSON.parse(localStorage.getItem(ASK_KEY) || '{}') || {}; } catch (e) { s = {}; }
    return { key: s.key || '', model: s.model || 'claude-opus-5', proxy: s.proxy || '', search: s.search !== false, searches: Number.isFinite(+s.searches) ? +s.searches : 5 };
  }
  function saveAskSettings(s) { try { localStorage.setItem(ASK_KEY, JSON.stringify(s)); } catch (e) { /* storage unavailable */ } }
  const ASK_STATUS = {
    delta: 'READ', delta_equation: 'PINNED', p: 'PINNED', n0: 'RECONSTRUCTED', B_computed: 'PINNED', B: 'PINNED', limit: 'READ', residual: 'DERIVED',
    shells_as_printed: 'READ', configuration: 'READ', level: 'READ', symbol: 'READ', electron_count: 'DERIVED', E: 'PINNED', held: 'PINNED', admitted: 'PINNED',
    A: 'PINNED', K: 'PINNED', H: 'PINNED', E0: 'PINNED', E1: 'PINNED', mass_MeV: 'READ', width_MeV: 'READ',
  };
  function askStatusFor(path, container, key) {
    if (container && typeof container === 'object' && container.status && typeof container.status === 'string') return container.status;
    return ASK_STATUS[key] || null;
  }
  // the data the model may cite, as "path = value [STATUS]" lines; every path resolves in askResolve
  function contextLines(question) {
    const ix = state.index, lines = [], q = question || '';
    const push = (path, value, status) => { if (value === null || value === undefined) return; lines.push(`${path} = ${typeof value === 'object' ? JSON.stringify(value) : value}${status ? ' [' + status + ']' : ''}`); };
    const c = ix.closure || {};
    push('index/closure/held', c.held, 'PINNED'); push('index/closure/admitted', c.admitted, 'PINNED'); push('index/closure/E', c.E, 'PINNED');
    const eq = ix.equation || {};
    ['A', 'K', 'H', 'E0', 'E1'].forEach((k) => push('index/equation/' + k, eq[k], 'PINNED'));
    if (eq.form) push('index/equation/form', eq.form, 'PINNED');
    const rep = (ix.fixtures || {}).equation_report;
    if (rep) { push('index/fixtures/equation_report/rms', rep.rms, 'DERIVED'); push('index/fixtures/equation_report/R2', rep.R2, 'DERIVED'); push('index/fixtures/equation_report/channels', rep.channels, 'DERIVED'); }
    // elements the question names
    const zs = new Set();
    (ix.layout || []).forEach((e) => {
      if (new RegExp('(^|[^A-Za-z])' + e.symbol + '(?![a-z])').test(q)) zs.add(e.Z);
      if (e.name && new RegExp('\\b' + e.name + '\\b', 'i').test(q)) zs.add(e.Z);
    });
    let m; const zrx = /\bZ\s*=\s*(\d{1,3})\b/g; while ((m = zrx.exec(q)) !== null) zs.add(+m[1]);
    if (!zs.size && state.selected && state.selected.Z) zs.add(state.selected.Z);
    const elements = [...zs].slice(0, 6).map((Z) => state.elements.get(Z)).filter(Boolean);
    elements.forEach((rec) => {
      const b = `el/${rec.Z}`; let n = 0;
      push(b + '/symbol', rec.symbol, 'READ'); push(b + '/shells_as_printed', rec.shells_as_printed, 'READ'); push(b + '/level', rec.level, 'READ');
      push(b + '/electron_count', rec.electron_count, 'DERIVED'); push(b + '/period', rec.period, 'DERIVED'); push(b + '/group', rec.group, 'DERIVED');
      if (rec.closure) push(b + '/closure/cell_held', rec.closure.cell_held, 'PINNED');
      if (rec.series_limit) { push(b + '/series_limit/value', rec.series_limit.value, rec.series_limit.status); }
      (rec.channels || []).forEach((ch, i) => {
        if (n > 90) return;
        const cb = `${b}/channels/${i}`;
        push(cb + '/charge', ch.charge, 'READ'); push(cb + '/l', ch.l, 'READ'); push(cb + '/p', ch.p, 'PINNED'); push(cb + '/n0', ch.n0, 'RECONSTRUCTED'); push(cb + '/B_computed', ch.B_computed, 'PINNED'); push(cb + '/delta_equation', ch.delta_equation, 'PINNED'); n += 6;
        (ch.measured || []).forEach((mr, j) => { push(`${cb}/measured/${j}/mult`, mr.mult, 'READ'); push(`${cb}/measured/${j}/delta`, mr.delta, 'READ'); if (mr.limit !== null && mr.limit !== undefined) push(`${cb}/measured/${j}/limit`, mr.limit, 'READ'); n += 3; });
      });
      (rec.lambda8 || []).slice(0, 12).forEach((st, i) => push(`${b}/lambda8/${i}`, { charge: st.charge, from: st.from, to: st.to, cell: st.cell }, 'RECONSTRUCTED'));
    });
    // particles the question names
    const pi = state.particleIndex;
    if (pi) {
      const want = /\b(muon|pion|kaon|proton|neutron|antiproton|positron|electron|neutrino|photon|gluon|higgs|quark|lepton|meson|baryon|hadron|boson|fermion|anyon|quasiparticle|laughlin|hall)\b/i.test(q);
      const named = [];
      pi.indexes.forEach((ixp) => ixp.rows.forEach((r) => { if (q.toLowerCase().includes(r.name.toLowerCase().replace(/[()~*]/g, '')) && r.name.length > 1) named.push([ixp, r]); }));
      if (want || named.length) {
        push('pi/accounting/identity', pi.accounting.identity, 'READ'); push('pi/accounting/charted', pi.accounting.charted, 'DERIVED');
        pi.indexes.forEach((ixp) => { push(`pi/${ixp.id}/members`, ixp.members, 'READ'); push(`pi/${ixp.id}/cells`, ixp.cells, 'DERIVED'); push(`pi/${ixp.id}/coordinates`, ixp.coordinates.map((c) => c.name), 'PINNED'); });
        const rows = named.length ? named : [];
        if (!rows.length && want) { const f = pi.indexes[0]; f.rows.forEach((r) => rows.push([f, r])); }
        rows.slice(0, 40).forEach(([ixp, r]) => { const i = ixp.rows.indexOf(r); ixp.coordinates.forEach((cd, k) => push(`pi/${ixp.id}/rows/${i}/coords/${k}`, r.coords[k], cd.status)); push(`pi/${ixp.id}/rows/${i}/name`, r.name, 'READ'); push(`pi/${ixp.id}/rows/${i}/extra/mass_MeV`, r.extra.mass_MeV, 'READ'); });
        const fq = pi.quasiparticles && pi.quasiparticles.seated;
        if (fq && /anyon|quasiparticle|laughlin|hall/i.test(q)) { push('pi/fqh/members', fq.members, 'DERIVED'); push('pi/fqh/cells', fq.cells, 'DERIVED'); fq.rows.slice(0, 40).forEach((r, i) => push(`pi/fqh/rows/${i}`, { m: r.m, j: r.j, Q: r.Q, theta: r.theta, coords: r.coords }, 'DERIVED')); }
      }
    }
    return { lines: lines.slice(0, 700), elements: elements.map((r) => r.Z) };
  }
  // the resolver the checker uses: a path from the context lines back to the loaded value
  function askResolve(path) {
    const parts = String(path).split('/').filter(Boolean);
    let root = null, i = 0;
    if (parts[0] === 'index') { root = state.index; i = 1; }
    else if (parts[0] === 'el') { root = state.elements.get(+parts[1]) || null; i = 2; }
    else if (parts[0] === 'pi') {
      const pi = state.particleIndex; if (!pi) return null;
      if (parts[1] === 'accounting') { root = pi.accounting; i = 2; }
      else if (parts[1] === 'fqh') { root = pi.quasiparticles && pi.quasiparticles.seated; i = 2; }
      else { root = pi.indexes.find((x) => x.id === parts[1]) || null; i = 2; if (root && parts[2] === 'coordinates') return { value: root.coordinates.map((c) => c.name), status: 'PINNED' }; }
    }
    if (!root) return null;
    let cur = root, parent = null, key = null;
    for (; i < parts.length; i++) { if (cur === null || typeof cur !== 'object') return null; parent = cur; key = parts[i]; cur = Array.isArray(cur) ? cur[+key] : cur[key]; if (cur === undefined) return null; }
    let status = askStatusFor(path, cur, key);
    if (parts[0] === 'pi' && parts[2] === 'rows' && parts[4] === 'coords' && root.coordinates) status = (root.coordinates[+parts[5]] || {}).status || status;
    return { value: cur, status: status };
  }
  function askCompute(name, args) {
    const L = window.MI && window.MI.solverLib; if (!L) return null;
    const num = (v) => (typeof v === 'number' ? v : null);
    if (name === 'channel_delta') { const rec = state.elements.get(num(args[0])); if (!rec) return null; const ch = (rec.channels || []).find((c) => c.charge === num(args[1]) && c.l === num(args[2])); return ch ? ch.delta_equation : null; }
    if (name === 'pauli_bound') return (args.length === 3 && args.every((a) => typeof a === 'number')) ? L.pauliBound(args[0], args[1], args[2]) : null;
    if (name === 'collapse_C') return (args.length === 2) ? L.collapseC(args[0], args[1], L.collapseParams(state.index)) : null;
    if (name === 'core_p' || name === 'n0_of') { const rec = state.elements.get(num(args[0])); if (!rec || !rec.configuration) return null; return name === 'core_p' ? L.coreP(rec.configuration, args[1]) : L.n0Of(rec.configuration, args[1]); }
    if (name === 'closure_E') return (state.index.closure || {}).E;
    return undefined;
  }
  function askSystem() {
    return `You answer questions about chemistry and physics for readers of The Method Index, a public research site whose data you are handed below as cited lines. Method:
1. Use web search first for context and method: definitions, standard procedures, published values, the way a question of this kind is normally solved. Search the way this site retrieves: (a) before searching, enumerate the target facts the question needs; (b) for each target list the routes that could carry it, by type — primary paper, preprint, review, compilation or table, citing paper, deposit or archive, database — and try the open routes first, since a paywall blocks a route and not a fact, and a compilation can carry a better figure than the primary; (c) read each retrieved source for the sources it names and follow them before searching afresh; (d) when a route is blocked move to the next route, never re-attempt the same one; (e) a fact confirmed on two independent routes closes, a fact on one route is fragile and must be marked so, and a fact you could not retrieve is a stated gap with the routes you tried, never an unexplained absence; (f) ask for a source as a catalogue entry (a DOI, an arXiv number, an archive identifier, a database record), not only as a text string, because a source has an index and it is rarely the one with a search box. Every figure you take from the web is followed by its source in the marker ⟨⟨url⟩⟩, one marker per route that carried it.
2. Then apply that method to the DATA lines: every figure you take from them must be followed by its path in the marker ⟦path⟧, copied exactly. Do not invent paths. If the data lacks what you need, say "not in the index" for that part and continue with what web sources give, marked as theirs.
3. Every calculation you perform with the site's own instruments must be written as ⟪function(args) = value⟫ so the page can repeat it. Available: channel_delta(Z, charge, l), pauli_bound(p, n0, l), collapse_C(Z, l), core_p(Z_core, l), n0_of(Z_core, l), closure_E(). Other arithmetic: show it in plain text.
4. Every chemical equation you write goes on its own line inside ⦃ ⦄, with spaces around + signs, charges as Fe3+ or SO4^2- or e-, and the arrow → . The page will tally atoms and charge.
5. Never say the page verified, confirmed or validated anything: the page checks your answer after you write it, and you do not know the result. Do not claim a status for a value; the page attaches statuses.
6. Do not write laboratory procedures or safety instructions.
7. If you balance an equation, write the balanced form inside ⦃ ⦄; the page has its own exact balancer (solver mode 10) and will tally yours.
Plain prose, at most 350 words. Then a line RETRIEVAL and one line per (target, route) you tried, pipe-separated:
target | route type | source: url or identifier | result: open, blocked, untried or empty | value found
List a blocked or empty route as honestly as an open one; the page counts the open routes per target and marks a target carried by one route as fragile.`;
  }
  async function askModel(question, context, settings, signal) {
    const base = (settings.proxy || 'https://api.anthropic.com').replace(/\/+$/, '');
    const body = {
      model: settings.model, max_tokens: 3000, system: askSystem(),
      messages: [{ role: 'user', content: `DATA (path = value [STATUS]):\n${context.lines.join('\n')}\n\nQUESTION: ${question}` }],
    };
    if (settings.search && settings.searches > 0) body.tools = [{ type: 'web_search_20250305', name: 'web_search', max_uses: settings.searches }];
    const res = await fetch(base + '/v1/messages', {
      method: 'POST', signal,
      headers: { 'content-type': 'application/json', 'x-api-key': settings.key, 'anthropic-version': '2023-06-01', 'anthropic-dangerous-direct-browser-access': 'true' },
      body: JSON.stringify(body),
    });
    const j = await res.json().catch(() => null);
    if (!res.ok) throw new Error(`${res.status} ${(j && j.error && j.error.message) || res.statusText}`);
    const text = (j.content || []).filter((b) => b.type === 'text').map((b) => b.text).join('');
    const sources = new Map();
    (j.content || []).forEach((b) => {
      if (b.type === 'web_search_tool_result' && Array.isArray(b.content)) b.content.forEach((r) => { if (r.url) sources.set(r.url, r.title || r.url); });
      if (b.type === 'text' && Array.isArray(b.citations)) b.citations.forEach((c) => { if (c.url) sources.set(c.url, c.title || c.url); });
    });
    return { text, sources: [...sources.entries()].map(([url, title]) => ({ url, title })), usage: j.usage || null, searches: (j.usage && j.usage.server_tool_use && j.usage.server_tool_use.web_search_requests) || 0 };
  }
  function chk(cls, text, tip) { return `<span class="chk chk-${cls}" title="${esc(tip || '')}">${esc(text)}</span>`; }
  const hostOfUrl = (u) => { try { return new URL(u).host.replace(/^www\./, ''); } catch (e) { return null; } };
  function renderChecked(host, text, sources, ctx, searchedUrls) {
    const L = window.MI && window.MI.solverLib;
    if (!L || !L.checkAnswer) { host.innerHTML = `<div class="resp-answer">${esc(text)}</div><div class="resp-checks">the solver module is not loaded, so this answer is unchecked</div>`; return null; }
    const r = L.checkAnswer(text, askResolve, askCompute, searchedUrls === undefined ? null : searchedUrls);
    const marks = [];
    r.sources.forEach((c) => marks.push({ at: c.at, len: c.len, html: c.identifier ? `<a href="${esc(c.identifier.url)}" target="_blank" rel="noopener noreferrer" class="chk ${/NOT/.test(c.verdict) ? 'chk-warn' : /among/.test(c.verdict) ? 'chk-ok' : 'chk-none'}" title="${esc(c.verdict)}">${/NOT/.test(c.verdict) ? '? ' : /among/.test(c.verdict) ? '✓ ' : '· '}${esc(c.identifier.kind === 'url' ? (hostOfUrl(c.identifier.url) || c.identifier.id) : c.identifier.kind + ' ' + c.identifier.id)}</a>` : chk('bad', '✗ no identifier', c.text) }));
    if (r.retrieval.present) marks.push({ at: r.retrieval.at, len: text.length - r.retrieval.at, html: '' });
    r.citations.forEach((c) => marks.push({ at: c.at, len: c.len, html: c.verdict === 'matches' ? chk('ok', '✓ ' + c.path.split('/').slice(-2).join('/') + (c.status ? ' · ' + c.status : ''), `index value ${c.value}`) : c.verdict === 'cited' ? chk('ok', '✓ cited' + (c.status ? ' · ' + c.status : ''), `index value ${JSON.stringify(c.value)}`) : c.verdict === 'DIFFERS' ? chk('bad', '✗ index says ' + c.value + (c.status ? ' · ' + c.status : ''), c.path) : c.verdict === 'not in the index' ? chk('bad', '✗ not in the index', c.path) : chk('warn', '? ' + c.verdict, c.path) }));
    r.computations.forEach((c) => marks.push({ at: c.at, len: c.len, html: c.verdict === 'agrees' ? chk('ok', `✓ ${c.name} = ${typeof c.value === 'number' ? +c.value.toFixed(6) : c.value}`, 'repeated by the page') : c.verdict === 'DIFFERS' ? chk('bad', `✗ ${c.name}: the page gets ${typeof c.value === 'number' ? +c.value.toFixed(6) : c.value}, the model wrote ${c.stated}`) : chk('warn', `? ${c.name}: ${c.verdict}`) }));
    r.equations.forEach((e) => marks.push({ at: e.at, len: e.len, html: `<span class="mono">${esc(e.text)}</span> ` + (e.verdict === 'balanced' ? chk('ok', '✓ balanced', e.result.atoms.map((a) => `${a.element} ${a.left}→${a.right}`).join(', ')) : e.verdict === 'NOT balanced' ? chk('bad', '✗ not balanced', e.result.atoms.filter((a) => !a.ok).map((a) => `${a.element} ${a.left}→${a.right}`).concat(e.result.charge.ok ? [] : [`charge ${e.result.charge.left}→${e.result.charge.right}`]).join(', ')) : chk('warn', '? unreadable', e.result.error || e.result.errors.join('; '))) }));
    marks.sort((a, b) => a.at - b.at);
    let html = '', pos = 0;
    marks.forEach((mk) => { html += esc(text.slice(pos, mk.at)) + mk.html; pos = mk.at + mk.len; });
    html += esc(text.slice(pos));
    const eqRows = r.equations.map((e) => `<tr><td class="mono wrap">${esc(e.text)}</td><td>${e.verdict}</td><td class="wrap">${e.result.atoms ? e.result.atoms.map((a) => `${a.element}${a.Z ? ' (Z ' + a.Z + ')' : ''} ${a.left}→${a.right}`).join(', ') + `; charge ${e.result.charge.left}→${e.result.charge.right}` : esc(e.result.error || '')}</td></tr>`).join('');
    const rt = r.retrieval;
    const rtRows = rt.present ? rt.rows.map((row) => `<tr><td class="wrap">${esc(row.target)}</td><td>${esc(row.route)}</td><td class="wrap">${row.identifier ? `<a href="${esc(row.identifier.url)}" target="_blank" rel="noopener noreferrer">${esc(row.identifier.kind === 'url' ? (hostOfUrl(row.identifier.url) || row.identifier.id) : row.identifier.kind + ' ' + row.identifier.id)}</a>` : esc(row.source || '—')}</td><td>${/NOT|no identifier/.test(row.verdict) ? chk('warn', row.verdict) : row.result === 'open' ? chk('ok', row.verdict) : chk('none', row.verdict)}</td><td class="wrap">${esc(row.value)}</td></tr>`).join('') : '';
    const rtTargets = rt.present ? rt.targets.map((t) => `<li><b>${esc(t.target)}</b>: ρ = ${t.rho} — ${t.rho >= 2 ? chk('ok', t.verdict) : t.rho === 1 ? chk('warn', t.verdict) : chk('bad', t.verdict)} (${t.routes.join(', ')})</li>`).join('') : '';
    host.innerHTML = `<div class="resp-answer">${html}</div>
      <div class="resp-checks"><b>Machine check:</b> ${esc(r.summary)}.${eqRows ? `<div class="tbl-wrap"><table class="t"><thead><tr><th>equation</th><th>verdict</th><th>tally</th></tr></thead><tbody>${eqRows}</tbody></table></div>` : ''}
      ${rt.present ? `<h4 class="resp-h">Retrieval: the routes tried, and the redundancy of each target</h4><ul class="resp-targets">${rtTargets}</ul><div class="tbl-wrap"><table class="t"><thead><tr><th>target</th><th>route</th><th>source</th><th>result</th><th>value</th></tr></thead><tbody>${rtRows}</tbody></table></div><p class="note">ρ counts the open routes per target: two survive the loss of either, one is fragile, none is a stated gap with the routes tried. A source is checked against the searches the API reported this session; one it never returned is flagged, not trusted.</p>` : `<p class="note">the model gave no retrieval table, so no route or redundancy could be checked</p>`}</div>
      ${sources && sources.length ? `<div class="resp-sources"><b>Web sources the model used:</b> ${sources.map((s) => `<a href="${esc(s.url)}" target="_blank" rel="noopener noreferrer">${esc(s.title || s.url)}</a>`).join(' · ')}</div>` : ''}`;
    return r;
  }
  function setupAsk() {
    const s = askSettings();
    $('#ask-key').value = s.key; $('#ask-model').value = s.model; $('#ask-proxy').value = s.proxy; $('#ask-search').checked = s.search; $('#ask-searches').value = s.searches;
    const stateEl = $('#ask-state');
    const show = () => { const cur = askSettings(); stateEl.textContent = cur.key ? `key saved · ${cur.model}${cur.search ? ' · web search on' : ''}` : 'no key: the console answers alone'; $('#assist-run').textContent = cur.key ? 'Ask · console + model, checked' : RUN_LABEL.console; };
    $('#ask-save').addEventListener('click', () => { saveAskSettings({ key: $('#ask-key').value.trim(), model: $('#ask-model').value, proxy: $('#ask-proxy').value.trim(), search: $('#ask-search').checked, searches: +$('#ask-searches').value || 0 }); show(); });
    $('#ask-forget').addEventListener('click', () => { const cur = askSettings(); cur.key = ''; saveAskSettings(cur); $('#ask-key').value = ''; show(); });
    show();
  }

  function respBlock(who, cls) {
    const out = $('#assist-out');
    const b = document.createElement('div');
    b.className = 'resp-block';
    b.innerHTML = `<div class="resp-who ${cls}"><span class="tag">${esc(who)}</span><span class="resp-who-note"></span></div><pre class="resp-body"></pre>`;
    out.appendChild(b);
    return { block: b, body: b.querySelector('.resp-body'), note: b.querySelector('.resp-who-note') };
  }
  function setupAssistant() {
    const ta = $('#assist-q'), run = $('#assist-run'), stop = $('#assist-stop'), clear = $('#assist-clear');
    const ask = async () => {
      const q = ta.value;
      const out = $('#assist-out');
      out.innerHTML = '';
      const c = respBlock('console', 'is-console');
      c.note.textContent = 'deterministic, from the loaded data';
      c.body.textContent = '…';
      const isCommand = /^(help|go|axes|closure|sources|caveats|count|measured|residuals|B|ladder|limits|relativistic|walk|lattice|particles|particle|references|refs|papers|figures|cite|history|editions|glossary|check)\b/i.test(q.trim());
      if (!isCommand && q.trim() && askSettings().key) c.body.textContent = 'not a console command; the question goes to the model below (type help for the commands)';
      else { try { c.body.textContent = await consoleAnswer(q); } catch (err) { c.body.textContent = `console error: ${err.message}`; } }
      if (claude.fn && q.trim()) {
        const k = respBlock('Claude', 'is-claude');
        k.note.textContent = 'claude.ai artifact runtime · instructed to answer only from the selected record; not checked by the page';
        k.body.textContent = 'Thinking …';
        claude.ctl = new AbortController();
        stop.hidden = false; run.disabled = true;
        try {
          const res = await claude.fn(claudePrompt(q), { signal: claude.ctl.signal, onText: ({ text }) => { k.body.textContent = text; } });
          k.body.textContent = res && res.text ? res.text : k.body.textContent;
          if (res && res.truncated) k.note.textContent += ' · cut short';
        } catch (e) {
          const code = e && e.code;
          if (code === 'not_granted') { k.body.textContent = 'Claude: not granted by the viewer; this answerer is now hidden.'; hideClaude('not granted'); }
          else if (code === 'rate_limited') k.body.textContent = 'Claude: rate limited — too many calls; try again later.';
          else if (code === 'cancelled') k.body.textContent = (e.text || '') + '\n[stopped]';
          else k.body.textContent = `${e && e.text ? e.text + '\n' : ''}Claude: ${code || 'error'}${e && e.message ? ` — ${e.message}` : ''}`;
        } finally { stop.hidden = true; run.disabled = false; claude.ctl = null; }
      }
      const settings = askSettings();
      if (settings.key && q.trim() && !/^(help|go|axes|closure|sources|caveats|count|measured|residuals|B|ladder|limits|relativistic|walk|lattice|particles|particle|references|refs|papers|figures|cite|history|editions|glossary|check)\b/i.test(q.trim())) {
        const k = respBlock('model', 'is-model');
        k.note.textContent = `${settings.model}${settings.search ? ' with web search' : ''} · grounded on the loaded data · checked by the page after it answers`;
        const bodyHost = k.body; bodyHost.textContent = 'Loading the records the question names …';
        claude.ctl = new AbortController();
        stop.hidden = false; run.disabled = true;
        try {
          const ix = state.index;
          const zs = new Set();
          (ix.layout || []).forEach((e) => { if (new RegExp('(^|[^A-Za-z])' + e.symbol + '(?![a-z])').test(q) || (e.name && new RegExp('\\b' + e.name + '\\b', 'i').test(q))) zs.add(e.Z); });
          let mm; const zrx = /\bZ\s*=\s*(\d{1,3})\b/g; while ((mm = zrx.exec(q)) !== null) zs.add(+mm[1]);
          if (state.selected && state.selected.Z) zs.add(state.selected.Z);
          await Promise.allSettled([...zs].slice(0, 6).map((Z) => ensureElement(Z)));
          if (ix.particle_index) await ensureParticleIndex().catch(() => null);
          const context = contextLines(q);
          bodyHost.textContent = `Asking ${settings.model}${settings.search ? ' (web search on)' : ''} with ${context.lines.length} data lines …`;
          const res = await askModel(q, context, settings, claude.ctl.signal);
          const host = document.createElement('div'); bodyHost.replaceWith(host);
          renderChecked(host, res.text, res.sources, null, res.sources.map((x) => x.url));
          k.note.textContent += ` · ${res.searches || 0} searches · ${res.usage ? (res.usage.input_tokens + res.usage.output_tokens).toLocaleString() + ' tokens' : ''}`;
        } catch (e) {
          bodyHost.textContent = e.name === 'AbortError' ? '[stopped]' : `model: ${e.message}`;
        } finally { stop.hidden = true; run.disabled = false; claude.ctl = null; }
      }
    };
    run.addEventListener('click', ask);
    ta.addEventListener('keydown', (ev) => { if (ev.key === 'Enter' && (ev.ctrlKey || ev.metaKey)) { ev.preventDefault(); ask(); } });
    stop.addEventListener('click', () => { if (claude.ctl) claude.ctl.abort(); });
    clear.addEventListener('click', () => { ta.value = ''; $('#assist-out').innerHTML = ''; ta.focus(); });
  }

  // ---------------------------------------------------------------- solver suite: a renderer over window.MI.solvers
  function solverCtx() {
    return {
      index: state.index,
      element: (Z) => state.elements.get(+Z) || null,
      load: (Z) => ensureElement(+Z),
      loadAll,
    };
  }
  function seriesSVG(series, yLabel) {
    const pts = series.filter((p) => Number.isFinite(+p.x) && Number.isFinite(+p.y)).map((p) => ({ x: +p.x, y: +p.y, label: p.label }));
    if (!pts.length) return '<p class="note">series carries no finite points</p>';
    const Wd = 440, Hd = 170, ml = 52, mr = 12, mt = 12, mb = 30;
    const xs = pts.map((p) => p.x), ys = pts.map((p) => p.y);
    let x0 = Math.min(...xs), x1 = Math.max(...xs), y0 = Math.min(...ys), y1 = Math.max(...ys);
    if (x1 === x0) { x0 -= 1; x1 += 1; }
    if (y1 === y0) { y0 -= 1; y1 += 1; }
    const sx = (x) => ml + ((x - x0) / (x1 - x0)) * (Wd - ml - mr);
    const sy = (y) => mt + (1 - (y - y0) / (y1 - y0)) * (Hd - mt - mb);
    const sorted = pts.slice().sort((a, b) => a.x - b.x);
    const line = sorted.length > 1 ? `<polyline class="ln" points="${sorted.map((p) => `${sx(p.x).toFixed(1)},${sy(p.y).toFixed(1)}`).join(' ')}"/>` : '';
    const dots = pts.map((p) => `<circle class="pt" cx="${sx(p.x).toFixed(1)}" cy="${sy(p.y).toFixed(1)}" r="4"><title>${esc(p.label || '')} x=${p.x} y=${fmt(p.y, 5)}</title></circle>`).join('');
    const ny = (v) => (Number.isInteger(v) ? String(v) : v.toPrecision(3));
    return `<svg class="spark" viewBox="0 0 ${Wd} ${Hd}" width="${Wd}" height="${Hd}" role="img" aria-label="${esc(yLabel || 'y')} against Z">
      <line class="grid" x1="${ml}" x2="${Wd - mr}" y1="${sy(y1)}" y2="${sy(y1)}"/>
      <line class="axis" x1="${ml}" x2="${ml}" y1="${mt}" y2="${Hd - mb}"/>
      <line class="axis" x1="${ml}" x2="${Wd - mr}" y1="${Hd - mb}" y2="${Hd - mb}"/>
      <text x="${ml - 6}" y="${sy(y1) + 3}" text-anchor="end">${ny(y1)}</text>
      <text x="${ml - 6}" y="${sy(y0) + 3}" text-anchor="end">${ny(y0)}</text>
      <text x="${ml}" y="${Hd - mb + 14}" text-anchor="start">${ny(x0)}</text>
      <text x="${Wd - mr}" y="${Hd - mb + 14}" text-anchor="end">${ny(x1)}</text>
      <text x="${(ml + Wd - mr) / 2}" y="${Hd - 4}" text-anchor="middle">x = Z</text>
      <text transform="translate(10 ${(mt + Hd - mb) / 2}) rotate(-90)" text-anchor="middle">${esc(yLabel || 'y')}</text>
      ${line}${dots}
    </svg>`;
  }
  // the registry as this build can run it: a mode that requires a block of the index
  // (the muon balance requires index.particles) is absent from a build without the block
  function solverRegistry() {
    const reg = window.MI && Array.isArray(window.MI.solvers) ? window.MI.solvers : null;
    if (!reg) return null;
    return reg.filter((m) => !m.requires || (state.index && state.index[m.requires]));
  }

  function setupSolvers() {
    const body = $('#solver-body'), count = $('#solver-count');
    const reg = solverRegistry();
    if (!reg || !reg.length) {
      count.textContent = 'not loaded';
      body.innerHTML = `<div class="callout is-finding">solver module not loaded — <code>window.MI.solvers</code> is absent. The solver module is appended to the end of <code>script.js</code>; without it the suite has nothing to run, and the explorer above computes nothing.</div>`;
      return;
    }
    count.textContent = `${reg.length} modes`;
    const ctxS = solverCtx();
    body.innerHTML = `<div class="solver-top">
        <div class="field"><label for="solver-mode">Mode</label><select id="solver-mode" class="sel">${reg.map((m, i) => `<option value="${i}">${esc(m.title || m.id)}</option>`).join('')}</select></div>
      </div>
      <div id="solver-mode-body"></div>`;
    const sel = $('#solver-mode');
    const renderMode = () => {
      const mode = reg[+sel.value];
      const host = $('#solver-mode-body');
      const inputs = Array.isArray(mode.inputs) ? mode.inputs : [];
      const field = (inp) => {
        const id = `sv-${esc(mode.id)}-${esc(inp.name)}`;
        const wide = inp.type === 'textarea' ? ' is-wide' : '';
        let ctl;
        if (inp.type === 'select') ctl = `<select id="${id}" data-name="${esc(inp.name)}">${(inp.options || []).map((o) => `<option value="${esc(o.value)}" ${String(o.value) === String(inp.default) ? 'selected' : ''}>${esc(o.label)}</option>`).join('')}</select>`;
        else if (inp.type === 'textarea') ctl = `<textarea id="${id}" data-name="${esc(inp.name)}" spellcheck="false">${esc(inp.default === undefined || inp.default === null ? '' : inp.default)}</textarea>`;
        else ctl = `<input id="${id}" data-name="${esc(inp.name)}" type="${inp.type === 'number' ? 'text' : 'text'}" ${inp.type === 'number' ? 'inputmode="decimal"' : ''} value="${esc(inp.default === undefined || inp.default === null ? '' : inp.default)}" autocomplete="off" spellcheck="false">`;
        return `<div class="field${wide}"><label for="${id}">${esc(inp.label || inp.name)}${inp.fromSelection ? ` <span class="note">← ${esc(inp.fromSelection)}</span>` : ''}</label>${ctl}${inp.help ? `<span class="help">${esc(inp.help)}</span>` : ''}</div>`;
      };
      const src = mode.source || {};
      const desc = typeof mode.description === 'function' ? mode.description(ctxS) : (mode.description || '');
      const sz = dataSize();
      host.innerHTML = `
        <div class="solver-desc">
          <p>${badge(mode.status)} <span class="note">${esc(mode.statusNote || '')}</span></p>
          <p>${esc(desc)}</p>
          ${src.instrument ? `<p class="note">mirrors <code>${esc(src.instrument)}</code> in <code>${esc(src.file || '')}</code></p>` : ''}
          ${mode.loadsAll ? `<p class="note">${esc(mode.loadsAll)} load every element file: ${sz.files} files, ${(sz.bytes / 1e6).toFixed(1)} MB, as the manifest in data/index.js records them.</p>` : ''}
        </div>
        <div class="solver-inputs">${inputs.map(field).join('')}</div>
        <div class="solver-actions">
          <button type="button" class="btn is-primary" data-sv="run">Run</button>
          ${inputs.some((i) => i.fromSelection) ? '<button type="button" class="btn" data-sv="fill">From selection</button>' : ''}
          <button type="button" class="btn" data-sv="selftest">Run selftest${mode.loadsAll ? ` (loads ${sz.files} files, ${(sz.bytes / 1e6).toFixed(1)} MB)` : ''}</button>
          <button type="button" class="btn" data-sv="source" aria-expanded="false">Instrument source</button>
        </div>
        <pre class="src" data-sv-src hidden></pre>
        <div class="solver-out" data-sv-out></div>
        <div class="solver-out" data-sv-test></div>`;
      const values = () => {
        const v = {};
        host.querySelectorAll('[data-name]').forEach((el) => { v[el.dataset.name] = el.value; });
        return v;
      };
      const out = host.querySelector('[data-sv-out]'), test = host.querySelector('[data-sv-test]'), srcPre = host.querySelector('[data-sv-src]');
      host.querySelector('[data-sv="run"]').addEventListener('click', async () => {
        out.innerHTML = '<p class="note">running …</p>';
        let res;
        try { res = await Promise.resolve(mode.run(values(), ctxS)); }
        catch (err) { out.innerHTML = `<div class="solver-msg">the mode threw instead of returning ok:false — ${esc(err && err.message ? err.message : String(err))}</div>`; return; }
        if (!res || typeof res !== 'object') { out.innerHTML = '<div class="solver-msg">the mode returned nothing</div>'; return; }
        let html = '';
        if (res.message) html += `<div class="solver-msg${res.ok ? ' is-ok' : ''}">${esc(res.message)}</div>`;
        if (!res.ok && !res.message) html += '<div class="solver-msg">the mode reported ok:false without a message</div>';
        if (Array.isArray(res.rows) && res.rows.length) {
          html += `<div class="tbl-wrap"><table class="t"><thead><tr><th>quantity</th><th class="num">value</th><th>status</th><th>note</th></tr></thead><tbody>
            ${res.rows.map((r) => `<tr><td class="wrap">${esc(r.label)}</td><td class="num">${esc(fmtVal(r.value))}</td><td>${r.status ? badge(r.status) : (isNumeric(r.value) ? badge(null) : '')}</td><td class="wrap" style="font-family:var(--font-body)">${esc(r.note || '')}</td></tr>`).join('')}
          </tbody></table></div>`;
        }
        if (res.text) html += `<pre class="out">${esc(res.text)}</pre>`;
        if (Array.isArray(res.series) && res.series.length) html += `<div class="tbl-wrap">${seriesSVG(res.series, res.seriesLabel)}</div>`;
        out.innerHTML = html || '<p class="note">the mode returned no rows</p>';
      });
      const fill = host.querySelector('[data-sv="fill"]');
      if (fill) fill.addEventListener('click', () => {
        const n = state.selected;
        if (!n || n.kind === 'root' || n.kind === 'ghost') { out.innerHTML = '<div class="solver-msg">select an element, ion, channel or cell first</div>'; return; }
        let filled = 0;
        inputs.forEach((inp) => {
          if (!inp.fromSelection) return;
          const el = host.querySelector(`[data-name="${CSS.escape(inp.name)}"]`);
          const v = n[inp.fromSelection];
          if (el && v !== undefined && v !== null) { el.value = String(v); filled++; }
        });
        out.innerHTML = `<div class="solver-msg is-ok">${filled} field${filled === 1 ? '' : 's'} filled from ${esc(pathText(n))}</div>`;
      });
      host.querySelector('[data-sv="selftest"]').addEventListener('click', async () => {
        test.innerHTML = '<p class="note">selftest running …</p>';
        let r;
        try { r = await Promise.resolve(mode.selftest(ctxS)); }
        catch (err) { test.innerHTML = `<div class="solver-msg">selftest threw — ${esc(err && err.message ? err.message : String(err))}</div>`; return; }
        if (!r) { test.innerHTML = '<div class="solver-msg">selftest returned nothing</div>'; return; }
        const failed = Array.isArray(r.failures) ? r.failures.length : (r.failed || 0);
        test.innerHTML = `<div class="selftest-summary"><span>checked <b>${r.checked}</b></span><span class="${failed ? 'bad' : 'ok'}">failed <b>${r.failed}</b></span></div>
          ${failed ? `<div class="tbl-wrap"><table class="t"><thead><tr><th>fixture</th><th>got</th><th>want</th></tr></thead><tbody>${(r.failures || []).map((f) => `<tr><td class="wrap">${esc(f.name)}</td><td class="wrap">${esc(fmtVal(f.got))}</td><td class="wrap">${esc(fmtVal(f.want))}</td></tr>`).join('')}</tbody></table></div>` : ''}
          ${r.notes ? `<p class="note">${esc(r.notes)}</p>` : ''}`;
      });
      host.querySelector('[data-sv="source"]').addEventListener('click', (ev) => {
        const b = ev.currentTarget;
        if (!srcPre.hidden) { srcPre.hidden = true; b.setAttribute('aria-expanded', 'false'); return; }
        const ins = state.index.instruments;
        const it = ins && src.instrument ? ins[src.instrument] : null;
        if (it && it.python) srcPre.textContent = `# ${it.file || ''}:${it.line || ''} — ${it.status || ''}\n# ${it.source || ''}\n${it.python}`;
        else if (it && it.text) srcPre.textContent = `# ${it.file || ''} — ${it.status || ''}${it.held === false ? ' — instrument NOT HELD' : ''}\n# ${it.source || ''}\n\n${it.text}`;
        if (it && src.also && ins) {
          // the reconstruction's own functions, after the record's passages, each with its status
          const more = src.also.map((n) => ins[n]).filter((x) => x && x.python).map((x) => `# ${x.file || ''}:${x.line || ''} — ${x.status || ''}\n# ${x.source || ''}\n${x.python}`);
          if (more.length) srcPre.textContent += `\n\n# ---- the walk, reconstructed (${more.length} functions; tools/lowdin_walk.py) ----\n\n` + more.join('\n\n');
        }
        else if (!ins) srcPre.textContent = 'instrument source not carried: this build of data/index.js has no instruments block (run python3 tools/webindex.py).';
        else srcPre.textContent = `no instrument named "${src.instrument || '?'}" in data/index.js → instruments (${Object.keys(ins).join(', ')}).`;
        srcPre.hidden = false; b.setAttribute('aria-expanded', 'true');
      });
    };
    sel.addEventListener('change', renderMode);
    renderMode();
  }
  const isNumeric = (v) => typeof v === 'number' || (typeof v === 'string' && v.trim() !== '' && Number.isFinite(+v));
  function fmtVal(v) {
    if (v === null || v === undefined) return '—';
    if (typeof v === 'number') return Number.isInteger(v) ? String(v) : (Math.abs(v) < 1e-3 || Math.abs(v) >= 1e6 ? v.toExponential(4) : v.toFixed(6).replace(/0+$/, '').replace(/\.$/, ''));
    if (typeof v === 'object') return JSON.stringify(v);
    return String(v);
  }

  // ---------------------------------------------------------------- boot
  async function boot() {
    try { const t = localStorage.getItem('theme'); if (t === 'dark' || t === 'light') document.documentElement.setAttribute('data-theme', t); } catch (e) { /* none */ }
    readColors();
    const ix = window.__mi && window.__mi.index;
    if (!ix) {
      $('#inspector-body').innerHTML = `<div class="callout is-finding">data/index.js did not load, or did not set <code>window.__mi.index</code>. Run <code>python3 tools/webindex.py</code> to write <code>public/data/</code>, then open <code>public/index.html</code> — from a file:// URL or any static host.</div>`;
      $('#solver-body').innerHTML = '<p class="note">no index, so no solver context</p>';
      $('#assist-mode').textContent = 'no data';
      return;
    }
    if (!ix.lattice || !ix.meta || !ix.manifest) {
      // an index.js older than this page (a cached copy): fetch a fresh one past the cache and boot again
      if (!window.__mi_reloaded) {
        window.__mi_reloaded = true;
        $('#inspector-body').innerHTML = '<p class="note">the data this browser cached is older than the page; loading the current data …</p>';
        const sc = document.createElement('script'); sc.src = `${DATA}index.js?v=${Date.now()}`; sc.onload = () => { sc.remove(); boot(); }; sc.onerror = () => { $('#inspector-body').innerHTML = '<p class="note">could not load a current data/index.js; reload the page</p>'; };
        document.head.appendChild(sc);
        return;
      }
    }
    state.index = ix;
    for (const a of ix.axes || []) AX[a.axis] = a;
    $('#site-title').textContent = ix.meta.title;
    $('#site-subtitle').innerHTML = `${esc(ix.meta.subtitle)}.<span id="edition"></span>`;
    document.title = ix.meta.title;
    $('#n-measured').textContent = ix.totals.measured;
    $('#n-exact').textContent = ix.totals.exact;
    $('#n-computed').textContent = ix.totals.computed.toLocaleString();
    const limRows = $('#legend-limit-rows');
    if (limRows && ix.limits) limRows.innerHTML = (ix.limits.kinds || []).map((k) => `<div class="legend-row"><span class="sw sw-lim-${esc(k.kind)}"></span> ${esc(LIMIT_LABEL[k.kind] || k.kind)} <span class="legend-n">${k.count.toLocaleString()}</span></div>`).join('');
    // the layout buttons' titles and the help dialog's figures, from index.closure and the fixtures
    const cl = ix.closure || {}, jan = ((ix.fixtures || {}).closure || {}).janet || null;
    $('#layout-table').title = `The drawn layout: period × group. ${cl.held} held, ${cl.admitted} admitted, E = ${cl.E}`;
    $('#layout-janet').title = `Janet: (n+ℓ, ℓ). E = ${jan ? jan.E : '?'}`;
    const fills = { held: cl.held, admitted: cl.admitted, E: cl.E, janetE: jan ? jan.E : '?' };
    document.querySelectorAll('[data-fill]').forEach((el) => { const v = fills[el.dataset.fill]; if (v !== undefined) el.textContent = String(v); });
    buildFrames();
    resize();
    renderProvenance();
    setupSearch(); setupPointer(); setupKeys(); setupChrome(); setupAssistant(); setupClaude(); setupAsk(); setupSolvers(); setupEdition();
    state.cam = homeCam();
    state.lastHash = null;
    if (location.hash && location.hash !== '#/') await applyHash(true, 0, false);
    else await select(rootNode, { fly: false, reveal: false });
    requestDraw();
  }

  const start = () => boot().catch((err) => {
    console.error(err);
    $('#inspector-body').innerHTML = `<div class="callout is-finding">The index failed to start: ${esc(err.message)}</div>`;
  });
  // The solver module is appended to the end of this file, so the suite is rendered only once
  // the whole script — and the document — has finished loading.
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else setTimeout(start, 0);
})();


/* =====================================================================
 * Solver suite — six modes ported from tools/populate.py and tools/cypher.py, and a seventh
 * that computes nothing: the relativistic limit, READ from the seated paper.
 * Registry: window.MI.solvers; library: window.MI.solverLib.
 * ===================================================================== */
(function () {
'use strict';
/* solvers.js -- the six browser-side solvers of The Method Index.
 *
 * Faithful ports of tools/populate.py (channel_delta, collapse_C, pauli_bound,
 * core_p, n0_of, lambda_constraints, caps_needed, within_caps, equation_report)
 * and of tools/cypher.py (class Index + op_order, R the order operator), in the
 * same order of floating-point operations, plus the coefficient calculator
 * engineered on the channel equation.
 *
 * ES2019, no DOM access, no imports. Every row that carries a number carries
 * the status the data gives it -- READ, PINNED, DERIVED, RECOVERED or
 * RECONSTRUCTED -- and a value typed by the reader carries none (status null),
 * exactly as the site badges an IUPAC name. A finding is recorded, never
 * repaired; a refusal is a result, not an error.
 *
 * Registry: window.MI.solvers (the seven modes) and window.MI.solverLib (LIB).
 * Nothing else is global: the whole module is one function scope.
 */

var SOLVERS, LIB;

  // ------------------------------------------------------------------ status
  var READ = 'READ', PINNED = 'PINNED', DERIVED = 'DERIVED',
      RECOVERED = 'RECOVERED', RECONSTRUCTED = 'RECONSTRUCTED';
  var WALK_FIELD_LABEL = { hf: 'Hartree–Fock, non-local exchange (the paper\'s field, rebuilt)', lx: 'local exchange (Hartree–Fock–Slater)' };

  // The channel equation's coefficients, digit for digit, used only when
  // ctx.index.equation does not carry them (the fallback is reported).
  var FALLBACK_COEF = { A: 0.3772, E0: 0.8297, E1: 0.0900, K: 0.4942, H: 0.5415 };
  var FALLBACK_COLLAPSE = { Z0: { 1: 5, 2: 21, 3: 57 }, width: 8.0 };
  var FALLBACK_CAPS = { n: 3, e: 3, l: 1, f: 1, k: 3 };
  var LSYM = 'spdfgh';
  var LAMBDA_COORDS = ['n', 'l', 'k', 'q', 'e', 'f', 'g', '2S'];
  var CAP_AXES = ['n', 'e', 'l', 'f', 'k'];          // populate.CAPS's own order
  var COEF_NAMES = ['A', 'E0', 'E1', 'K', 'H'];

  // ----------------------------------------------------------------- helpers
  function isBlank(v) {
    return v === undefined || v === null || (typeof v === 'string' && v.trim() === '');
  }
  function num(v) {
    if (isBlank(v)) return null;
    if (typeof v === 'number') return isFinite(v) ? v : null;
    var s = String(v).trim();
    if (!/^[-+]?(\d+\.?\d*|\.\d+)([eE][-+]?\d+)?$/.test(s)) return null;
    var x = Number(s);
    return isFinite(x) ? x : null;
  }
  function int(v) {
    var x = num(v);
    if (x === null || x !== Math.floor(x)) return null;
    return x;
  }
  function roman(n) {
    var t = [[100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'], [10, 'X'], [9, 'IX'],
             [5, 'V'], [4, 'IV'], [1, 'I']];
    var s = '', k = n;
    for (var i = 0; i < t.length; i++) { while (k >= t[i][0]) { s += t[i][1]; k -= t[i][0]; } }
    return s;
  }
  function lsym(l) { return l < LSYM.length ? LSYM.charAt(l) : String(l); }
  function label(sym, charge, l, mult) {
    var s = sym + ' ' + roman(charge) + ' ' + lsym(l);
    return mult === undefined || mult === null ? s : s + ' ' + mult;
  }
  function fmt(x, nd) {
    if (x === null || x === undefined) return '-';
    if (typeof x !== 'number') return String(x);
    if (x !== 0 && Math.abs(x) < 5e-5) return x.toExponential(3);
    return x.toFixed(nd === undefined ? 6 : nd);
  }
  function pad(s, w) { s = String(s); while (s.length < w) s += ' '; return s; }
  function lpad(s, w) { s = String(s); while (s.length < w) s = ' ' + s; return s; }
  function fail(message) { return { rows: [], ok: false, message: message }; }
  function row(labelText, value, status, note) {
    var r = { label: labelText, value: value };
    if (status !== undefined) r.status = status;
    if (note) r.note = note;
    return r;
  }
  function caveat(index, id) {
    var cs = (index && index.caveats) || [];
    for (var i = 0; i < cs.length; i++) if (cs[i].id === id) return cs[i].text;
    return null;
  }
  function median(sortedAbs) {              // populate: sorted(...)[n // 2]
    return sortedAbs[Math.floor(sortedAbs.length / 2)];
  }

  // -------------------------------------------------------------- the index
  function coefficients(index) {
    var eq = (index && index.equation) || {};
    var out = {}, fallback = [];
    COEF_NAMES.forEach(function (k) {
      var v = num(eq[k]);
      if (v === null) { v = FALLBACK_COEF[k]; fallback.push(k); }
      out[k] = v;
    });
    out.fallback = fallback;
    out.note = fallback.length
      ? fallback.join(', ') + ' not carried by index.equation; the equation\'s pinned values ' +
        fallback.map(function (k) { return k + ' = ' + FALLBACK_COEF[k]; }).join(', ') +
        ' used, as tools/populate.py pins them'
      : 'A, E0, E1, K, H read from index.equation (' + (eq.source || 'the channel equation, final form') + ')';
    return out;
  }
  function collapseParams(index) {
    var c = (index && index.collapse) || {};
    var Z0 = c.Z0 || FALLBACK_COLLAPSE.Z0;
    var width = num(c.width);
    if (width === null) width = FALLBACK_COLLAPSE.width;
    return { Z0: Z0, width: width, fromIndex: !!(c.Z0 && num(c.width) !== null) };
  }
  function capsOf(index) {
    var c = index && index.caps;
    if (!c) return FALLBACK_CAPS;
    var out = {};
    CAP_AXES.forEach(function (ax) { var v = num(c[ax]); out[ax] = v === null ? FALLBACK_CAPS[ax] : v; });
    return out;
  }
  function withCoef(coef, name, value) {
    var out = {};
    COEF_NAMES.forEach(function (k) { out[k] = coef[k]; });
    out[name] = value;
    return out;
  }

  // ------------------------------------------- populate.collapse_C, RECOVERED
  // C(Z, l) = clamp(0.5 + (Z - Z0(l)) / 8, 0, 1); zero where l has no Z0.
  function collapseC(Z, l, params) {
    var p = params || FALLBACK_COLLAPSE;
    var z0 = p.Z0[l];
    if (z0 === undefined || z0 === null) return 0.0;
    return Math.min(1.0, Math.max(0.0, 0.5 + (Z - z0) / p.width));
  }

  // ----------------------------------------- populate.channel_delta, PINNED
  //   delta = A p^e(Ne) Ne^K ln(c+1)/c                 p > 0,  e = E0 - E1 ln Ne
  //   delta = H C(Z) ((Ne-1)/Ne) Ne^K ln(c+1)/c        p = 0
  // Same left-to-right products as populate.py, so the doubles agree.
  function channelTerms(p, Ne, charge, C, coef) {
    var c = charge;
    if (Ne < 1 || c < 1) return null;
    var cf = Math.log(c + 1) / c;
    if (p > 0) {
      var e = coef.E0 - coef.E1 * Math.log(Ne);
      var pe = Math.pow(p, e), nk = Math.pow(Ne, coef.K);
      return { branch: 'p > 0', cf: cf, e: e, pe: pe, nk: nk, C: C, ratio: null,
               delta: coef.A * pe * nk * cf };
    }
    var ratio = (Ne - 1) / Ne, nk0 = Math.pow(Ne, coef.K);
    return { branch: 'p = 0', cf: cf, e: null, pe: null, nk: nk0, C: C, ratio: ratio,
             delta: coef.H * C * ratio * nk0 * cf };
  }
  function channelDelta(p, Ne, charge, C, coef) {
    var t = channelTerms(p, Ne, charge, C, coef || FALLBACK_COEF);
    return t === null ? null : t.delta;
  }

  // ------------------------------ populate.core_p / n0_of over a configuration
  // cfg is a record's "configuration": [{n, l, occupancy}, ...] of the CORE.
  function coreP(cfg, l) {
    var p = 0;
    for (var i = 0; i < cfg.length; i++) if (cfg[i].l === l && cfg[i].occupancy > 0) p += 1;
    return p;
  }
  function n0Of(cfg, l) {
    var occ = {};
    for (var i = 0; i < cfg.length; i++) occ[cfg[i].n + ',' + cfg[i].l] = cfg[i].occupancy;
    var n = l + 1;
    while ((occ[n + ',' + l] || 0) > 0) n += 1;
    return n;
  }
  // populate.pauli_bound: B = max(0, min(p, n0 - l - 1)).
  function pauliBound(p, n0, l) {
    return Math.max(0, Math.min(p, n0 - l - 1));
  }

  // ----------------------------------- Lambda_8: the seven constraints and the standing caps
  function lambdaConstraints(cell) {
    var n = cell[0], l = cell[1], k = cell[2], q = cell[3], e = cell[4], f = cell[5],
        g = cell[6], S2 = cell[7];
    return [
      { rule: 'l <= n-1', holds: l <= n - 1, origin: 'hydrogenic radial solution' },
      { rule: 'k <= 2(2l+1)', holds: k <= 2 * (2 * l + 1), origin: 'Pauli exclusion' },
      { rule: 'q <= k', holds: q <= k, origin: 'counting' },
      { rule: 'f <= e-1', holds: f <= e - 1, origin: 'hydrogenic radial solution' },
      { rule: 'g <= 2(2f+1)', holds: g <= 2 * (2 * f + 1), origin: 'Pauli exclusion' },
      { rule: 'g <= q', holds: g <= q, origin: 'counting' },
      { rule: '2S <= k', holds: S2 <= k, origin: 'vector coupling (an envelope)' }
    ];
  }
  function capsNeeded(cell) {
    return { n: cell[0], e: cell[4], l: cell[1], f: cell[5], k: cell[2] };
  }
  function withinCaps(cell, caps) {
    var need = capsNeeded(cell), c = caps || FALLBACK_CAPS, out = {};
    CAP_AXES.forEach(function (ax) { if (ax in c) out[ax] = need[ax] <= c[ax]; });
    return out;
  }

  // ------------------------------------------ cypher.Index + op_order, R
  // Coordinates are recoded to ordinals exactly as cypher.Index does (sorted by
  // numeric value), duplicates collapse with a warning, and R is run over the
  // ambient product of the alphabets; the admitted set is decoded back.
  function orderClosure(cells) {
    if (!cells || !cells.length) throw new Error('index has no cells');
    var d = cells[0].length;
    if (d < 2) throw new Error('R needs at least two coordinates');
    for (var r = 0; r < cells.length; r++) {
      if (cells[r].length !== d) {
        throw new Error('cell (' + cells[r].join(', ') + ') has ' + cells[r].length +
                        ' values, expected ' + d);
      }
    }
    var code = [], decode = [], warnings = [];
    for (var i = 0; i < d; i++) {
      var vals = {};
      cells.forEach(function (c) { vals[c[i]] = c[i]; });
      var order = Object.keys(vals).map(function (k) { return vals[k]; })
        .sort(function (a, b) { return a - b || String(a).localeCompare(String(b)); });
      var m = {};
      order.forEach(function (v, rnk) { m[v] = rnk; });
      code.push(m);
      decode.push(order);
    }
    var seen = {}, X = [];
    cells.forEach(function (c) {
      var t = c.map(function (v, i) { return code[i][v]; });
      var key = t.join(',');
      if (!seen[key]) { seen[key] = true; X.push(t); }
    });
    if (X.length !== cells.length) warnings.push((cells.length - X.length) + ' duplicate cells collapsed');
    var alphabets = [], box = 1;
    for (i = 0; i < d; i++) {
      var s = {};
      X.forEach(function (t) { s[t[i]] = true; });
      var a = Object.keys(s).map(Number).sort(function (p, q) { return p - q; });
      alphabets.push(a);
      box *= a.length;
    }
    // phi[(i, j, a)] = max{ y_i : y in X, y_j <= a }, None if empty
    var phi = {};
    for (i = 0; i < d; i++) {
      for (var j = 0; j < d; j++) {
        if (i === j) continue;
        for (var ai = 0; ai < alphabets[j].length; ai++) {
          var av = alphabets[j][ai], best = null;
          for (var y = 0; y < X.length; y++) {
            if (X[y][j] <= av && (best === null || X[y][i] > best)) best = X[y][i];
          }
          phi[i + ',' + j + ',' + av] = best;
        }
      }
    }
    // admitted = { x in ambient : for all i != j, phi(i,j,x_j) is not None and x_i <= phi }
    var admitted = [], idx = new Array(d).fill(0), done = false;
    while (!done) {
      var x = idx.map(function (k, i) { return alphabets[i][k]; });
      var good = true;
      for (i = 0; i < d && good; i++) {
        for (j = 0; j < d; j++) {
          if (i === j) continue;
          var p = phi[i + ',' + j + ',' + x[j]];
          if (p === null || x[i] > p) { good = false; break; }
        }
      }
      if (good) admitted.push(x);
      var pos = d - 1;
      while (pos >= 0) {
        idx[pos] += 1;
        if (idx[pos] < alphabets[pos].length) break;
        idx[pos] = 0;
        pos -= 1;
      }
      if (pos < 0) done = true;
    }
    var heldKeys = {};
    X.forEach(function (t) { heldKeys[t.join(',')] = true; });
    var dec = function (t) { return t.map(function (v, i) { return decode[i][v]; }); };
    var denied = admitted.filter(function (t) { return !heldKeys[t.join(',')]; }).map(dec);
    var heldDec = X.map(dec);
    return {
      d: d, held: heldDec, admitted: admitted.map(dec), denied: denied,
      E: admitted.length - X.length, box: box, warnings: warnings,
      note: 'staircase closure over the ambient product'
    };
  }

  // ------------------------------------------- populate.equation_report
  // rows: [{delta, delta_equation, l}] -- the measured rows, in index order.
  function equationReport(rows) {
    var res = rows.map(function (r) { return { d: r.delta - r.delta_equation, v: r.delta, l: r.l }; });
    var n = res.length;
    if (!n) return null;
    var ss_res = 0, sum_v = 0;
    res.forEach(function (x) { ss_res += x.d * x.d; sum_v += x.v; });
    var rms = Math.sqrt(ss_res / n);
    var mean = sum_v / n, ss_tot = 0;
    res.forEach(function (x) { ss_tot += (x.v - mean) * (x.v - mean); });
    var r2 = ss_tot ? 1 - ss_res / ss_tot : null;
    var abs = res.map(function (x) { return Math.abs(x.d); }).sort(function (a, b) { return a - b; });
    var by_l = [];
    var ls = {};
    res.forEach(function (x) { ls[x.l] = true; });
    Object.keys(ls).map(Number).sort(function (a, b) { return a - b; }).forEach(function (l) {
      var s = 0, k = 0;
      res.forEach(function (x) { if (x.l === l) { s += x.d * x.d; k += 1; } });
      by_l.push({ l: l, n: k, rms: Math.sqrt(s / k) });
    });
    return { channels: n, rms: rms, R2: r2, median_abs_error: median(abs), by_l: by_l };
  }

  // ------------------------------------------------- the measured channels
  // A flat row per (Z, charge, l, mult) of a populated element record.
  function channelRows(rec, params, onlyMeasured) {
    var out = [];
    if (!rec || !rec.populated || !rec.channels) return out;
    rec.channels.forEach(function (ch) {
      var C = collapseC(rec.Z, ch.l, params);
      (ch.measured || []).forEach(function (m) {
        if (onlyMeasured && m.grade !== 'measured') return;
        out.push({
          Z: rec.Z, symbol: rec.symbol, charge: ch.charge, l: ch.l, mult: m.mult,
          p: ch.p, Ne: ch.Ne, C: C, C_exported: ch.C_of_Z, delta: m.delta, grade: m.grade,
          witness: m.witness, source: m.source, delta_equation: ch.delta_equation,
          residual_exported: m.residual, label: label(rec.symbol, ch.charge, ch.l, m.mult)
        });
      });
    });
    return out;
  }
  function findChannel(rec, charge, l) {
    if (!rec || !rec.channels) return null;
    for (var i = 0; i < rec.channels.length; i++) {
      var ch = rec.channels[i];
      if (ch.charge === charge && ch.l === l) return ch;
    }
    return null;
  }
  function measuredRowsAll(records, params) {
    var rows = [];
    records.forEach(function (rec) { channelRows(rec, params, true).forEach(function (r) { rows.push(r); }); });
    rows.sort(function (a, b) { return a.Z - b.Z || a.charge - b.charge || a.l - b.l || a.mult - b.mult; });
    return rows;
  }

  // ------------------------------------------------ the coefficient calculator
  // (a) invert: one channel, one coefficient, closed form, all others pinned.
  function invertCoefficient(r, name, coef) {
    var out = { coefficient: name, pinned: coef[name], solvable: false, reason: null,
                value: null, branch: r.p > 0 ? 'p > 0' : 'p = 0', label: r.label };
    var terms = channelTerms(r.p, r.Ne, r.charge, r.C, coef);
    out.delta_equation = terms === null ? null : terms.delta;
    out.residual = terms === null ? null : r.delta - terms.delta;
    if (COEF_NAMES.indexOf(name) < 0) { out.code = 'unknown'; out.reason = 'unknown coefficient ' + name; return out; }
    if (terms === null) { out.code = 'no channel'; out.reason = 'Ne < 1 or charge < 1: no channel'; return out; }
    var d = r.delta, cf = terms.cf, Ne = r.Ne, p = r.p;
    // the identity comes before the grade: at Ne = 1 no coefficient moves the channel whatever
    // the row's grade, and H carries no measured row at all
    if (Ne === 1) {
      out.code = 'Ne = 1, the hydrogenic channel';
      out.reason = 'Ne = 1: the (Ne-1)/Ne factor vanishes identically, so no coefficient moves ' +
                   'the channel, exactly zero at one electron' +
                   (r.grade !== 'measured' ? '; the row\'s grade is ' + r.grade + ', not measured' : '');
      return out;
    }
    if (r.grade !== 'measured') {
      out.code = 'grade ' + r.grade + ', not measured';
      out.reason = 'grade ' + r.grade + ': the delta is ' + (r.grade === 'exact' ? 'exact' : 'computed') +
                   ', not measured, so there is nothing to solve against';
      return out;
    }
    var logs = (name === 'K' || name === 'E0' || name === 'E1');
    if (p > 0) {
      if (name === 'H') { out.code = 'not in the p > 0 branch'; out.reason = 'H is not in the p > 0 branch (p = ' + p + ')'; return out; }
      if ((name === 'E0' || name === 'E1') && p === 1) {
        out.code = 'p = 1, no effect';
        out.reason = 'p = 1: p^e = 1 for every exponent, so E0 and E1 have no effect on this channel';
        return out;
      }
      if (logs && d <= 0) {
        out.code = 'delta <= 0, log inversion';
        out.reason = 'delta = ' + d + ' <= 0: a log inversion has no real solution';
        return out;
      }
      var e = terms.e;
      if (name === 'A') {
        out.value = d / (terms.pe * terms.nk * cf);
      } else if (name === 'K') {
        out.value = Math.log(d / (coef.A * terms.pe * cf)) / Math.log(Ne);
      } else {
        var eStar = Math.log(d / (coef.A * terms.nk * cf)) / Math.log(p);
        out.e_solved = eStar;
        out.e_pinned = e;
        out.value = name === 'E0' ? eStar + coef.E1 * Math.log(Ne)
                                  : (coef.E0 - eStar) / Math.log(Ne);
      }
    } else {
      if (name === 'A' || name === 'E0' || name === 'E1') {
        out.code = 'not in the p = 0 branch';
        out.reason = name + ' is not in the p = 0 branch (p = 0: the channel runs on H, C(Z) and K)';
        return out;
      }
      if (r.C === 0) {
        out.code = 'C(Z, l) = 0, no effect';
        out.reason = 'C(Z, l) = 0: the p = 0 branch is identically zero here, so no value of ' + name +
                     ' moves the channel';
        return out;
      }
      if (logs && d <= 0) {
        out.code = 'delta <= 0, log inversion';
        out.reason = 'delta = ' + d + ' <= 0: a log inversion has no real solution';
        return out;
      }
      if (name === 'H') {
        out.value = d / (r.C * terms.ratio * terms.nk * cf);
      } else {
        out.value = Math.log(d / (coef.H * r.C * terms.ratio * cf)) / Math.log(Ne);
      }
    }
    if (!isFinite(out.value)) { out.code = 'not finite'; out.reason = 'the inversion is not finite'; out.value = null; return out; }
    out.solvable = true;
    out.gap = out.value - out.pinned;
    out.gap_rel = out.pinned !== 0 ? out.gap / out.pinned : null;
    var rt = channelDelta(r.p, r.Ne, r.charge, r.C, withCoef(coef, name, out.value));
    out.roundtrip_delta = rt;
    out.roundtrip_error = rt - d;
    if (d <= 0 && !logs) out.sign_note = 'delta <= 0 on this channel: the solved ' + name + ' is <= 0, ' +
                                          'outside the pinned sign; recorded, not repaired';
    return out;
  }

  // Linear algebra, stdlib-free: rank by modified Gram-Schmidt (two passes), whose
  // orthonormal basis Q and triangular factor R are kept, so the least-squares
  // solution is x = R^-1 Q^T y -- no normal equations, whose condition number is
  // the square of X's.
  function dot(a, b) { var s = 0; for (var i = 0; i < a.length; i++) s += a[i] * b[i]; return s; }
  function norm(a) { return Math.sqrt(dot(a, a)); }
  function rankColumns(X, names, tol) {
    var m = names.length, n = X.length, basis = [], basisNames = [], Rcols = [];
    var determined = [], undetermined = [];
    for (var j = 0; j < m; j++) {
      var v = X.map(function (r) { return r[j]; });
      var n0 = norm(v);
      if (n0 <= 1e-12 * Math.sqrt(n) || n0 === 0) {
        undetermined.push({ index: j, name: names[j].coef, column: names[j].column,
                            reason: 'its column ' + names[j].column + ' is identically zero over these rows' });
        continue;
      }
      var combos = [];
      for (var pass = 0; pass < 2; pass++) {
        for (var t = 0; t < basis.length; t++) {
          var c = dot(basis[t], v);
          combos[t] = (combos[t] || 0) + c;
          for (var i = 0; i < n; i++) v[i] -= c * basis[t][i];
        }
      }
      var n1 = norm(v);
      if (n1 <= tol * n0) {
        var deps = [];
        for (t = 0; t < basis.length; t++) if (Math.abs(combos[t]) > 1e-9 * n0) deps.push(basisNames[t]);
        undetermined.push({ index: j, name: names[j].coef, column: names[j].column,
                            reason: 'inseparable from ' + (deps.length ? deps.join(' and ') : 'the fitted columns') +
                                    ': its column ' + names[j].column + ' is a combination of theirs over these rows' });
        continue;
      }
      for (i = 0; i < n; i++) v[i] /= n1;
      var col = [];
      for (t = 0; t < basis.length; t++) col.push(combos[t] || 0);
      col.push(n1);                          // R's column for this basis vector, diagonal last
      Rcols.push(col);
      basis.push(v);
      basisNames.push(names[j].coef);
      determined.push(j);
    }
    return { determined: determined, undetermined: undetermined, Q: basis, Rcols: Rcols };
  }
  // x = R^-1 Q^T y over the determined columns, by back substitution
  function solveQR(Q, Rcols, y) {
    var k = Q.length, z = [], x = new Array(k).fill(0);
    for (var t = 0; t < k; t++) z.push(dot(Q[t], y));
    for (var r = k - 1; r >= 0; r--) {
      var s2 = z[r];
      for (var c = r + 1; c < k; c++) s2 -= Rcols[c][r] * x[c];
      x[r] = s2 / Rcols[r][r];
    }
    return x;
  }
  // Least squares over named columns, unknowns not determined held at their
  // pinned value (their columns move to the right-hand side).
  function lsHeld(X, y, names, pinnedVals, tol) {
    var rk = rankColumns(X, names, tol);
    var held = rk.undetermined.map(function (u) { return u.index; });
    var y2 = y.map(function (v, r) {
      var s = v;
      held.forEach(function (j) { s -= X[r][j] * pinnedVals[j]; });
      return s;
    });
    var beta = new Array(names.length);
    held.forEach(function (j) { beta[j] = pinnedVals[j]; });
    if (rk.determined.length) {
      var sol = solveQR(rk.Q, rk.Rcols, y2);
      rk.determined.forEach(function (j, t) { beta[j] = sol[t]; });
    }
    return { beta: beta, determined: rk.determined, undetermined: rk.undetermined, rank: rk.determined.length };
  }
  function rmsOf(arr) { var s = 0; arr.forEach(function (v) { s += v * v; }); return arr.length ? Math.sqrt(s / arr.length) : null; }

  // (b) atom: the element's coefficient set jointly, in log form.
  function atomSolve(rows, coef, subset) {
    subset = subset || 'all';
    var tol = 1e-9;
    var measured = rows.filter(function (r) { return r.grade === 'measured'; });
    var usedP = [], usedH = [], excluded = [];
    // 'all' and 'A and K' solve in the log form, where delta must be positive; 'A only' and
    // 'H only' are closed forms linear in delta, so a delta <= 0 row stays in and the solved
    // value may leave the pinned sign -- recorded, not repaired
    var logForm = (subset === 'all' || subset === 'A and K');
    measured.forEach(function (r) {
      if (r.Ne === 1) { excluded.push({ row: r, why: 'Ne = 1, the hydrogenic channel' }); return; }
      if (r.p > 0) {
        if (logForm && r.delta <= 0) { excluded.push({ row: r, why: 'p > 0 but delta <= 0: no log form' }); return; }
        usedP.push(r);
      } else {
        if (r.C === 0) { excluded.push({ row: r, why: 'p = 0 and C(Z, l) = 0: identically zero' }); return; }
        if (logForm && r.delta <= 0) { excluded.push({ row: r, why: 'p = 0 but delta <= 0: no log form' }); return; }
        usedH.push(r);
      }
    });
    var out = { subset: subset, n_measured: measured.length, usedP: usedP, usedH: usedH, excluded: excluded,
                solved: {}, status: {}, notes: [], undetermined: [], rank: null, dof: null,
                rms_before: null, rms_after: null, log_rms_before: null, log_rms_after: null, perRow: [], H: null };
    COEF_NAMES.forEach(function (k) { out.solved[k] = coef[k]; out.status[k] = PINNED; });
    var distinctP = {}, distinctNe = {};
    usedP.forEach(function (r) { distinctP[r.p] = true; distinctNe[r.Ne] = true; });
    out.distinct_p = Object.keys(distinctP).map(Number).sort(function (a, b) { return a - b; });
    out.distinct_Ne = Object.keys(distinctNe).map(Number).sort(function (a, b) { return a - b; });

    function termsPinned(r) { return channelTerms(r.p, r.Ne, r.charge, r.C, coef); }

    if (subset === 'A only' || subset === 'H only') {
      var use = subset === 'A only' ? usedP : usedH, name = subset === 'A only' ? 'A' : 'H';
      if (!use.length) { out.notes.push('no usable rows for ' + name + ' (see the exclusions)'); return out; }
      var sgd = 0, sgg = 0;
      use.forEach(function (r) {
        var t = termsPinned(r);
        var g = name === 'A' ? t.pe * t.nk * t.cf : r.C * t.ratio * t.nk * t.cf;
        sgd += g * r.delta; sgg += g * g;
      });
      out.solved[name] = sgd / sgg;
      out.status[name] = DERIVED;
      out.rank = 1; out.dof = use.length - 1;
      out.notes.push(name + '* = sum(g d) / sum(g^2) over ' + use.length + ' rows, g the row\'s factor: ' +
                     'least squares in delta itself, closed form');
      if (out.solved[name] <= 0) out.notes.push('solved ' + name + ' <= 0, outside the pinned sign; recorded, not repaired');
      out.rowsUsed = use;
    } else {
      if (!usedP.length) {
        out.notes.push('no usable p > 0 rows (see the exclusions); nothing to solve for A, E0, E1, K');
      } else {
        var names, X, y, pinnedVals;
        if (subset === 'A and K') {
          names = [{ coef: 'ln A', column: '1' }, { coef: 'K', column: 'ln Ne' }];
          X = usedP.map(function (r) { return [1, Math.log(r.Ne)]; });
          y = usedP.map(function (r) {
            var t = termsPinned(r);
            return Math.log(r.delta) - Math.log(t.cf) - t.e * Math.log(r.p);
          });
          pinnedVals = [Math.log(coef.A), coef.K];
        } else {
          // ln d - ln cf = ln A + K ln Ne + E0 ln p - E1 (ln Ne)(ln p); columns in
          // the priority order the pivots are kept: ln A, K, E0, E1.
          names = [{ coef: 'ln A', column: '1' }, { coef: 'K', column: 'ln Ne' },
                   { coef: 'E0', column: 'ln p' }, { coef: 'E1', column: '-(ln Ne)(ln p)' }];
          X = usedP.map(function (r) {
            var lp = Math.log(r.p), ln = Math.log(r.Ne);
            return [1, ln, lp, -ln * lp];
          });
          y = usedP.map(function (r) { return Math.log(r.delta) - Math.log(channelTerms(r.p, r.Ne, r.charge, r.C, coef).cf); });
          pinnedVals = [Math.log(coef.A), coef.K, coef.E0, coef.E1];
        }
        var ls;
        try { ls = lsHeld(X, y, names, pinnedVals, tol); }
        catch (err) { out.notes.push('solve failed: ' + err.message); ls = null; }
        if (ls) {
          var map = { 'ln A': 'A', 'K': 'K', 'E0': 'E0', 'E1': 'E1' };
          names.forEach(function (nm, j) {
            var k = map[nm.coef];
            var determined = ls.determined.indexOf(j) >= 0;
            out.solved[k] = k === 'A' ? Math.exp(ls.beta[j]) : ls.beta[j];
            out.status[k] = determined ? DERIVED : PINNED;
          });
          out.rank = ls.rank;
          out.dof = usedP.length - ls.rank;
          out.undetermined = ls.undetermined.map(function (u) {
            return { coefficient: map[u.name], reason: u.reason };
          });
          // the quantity minimised, in ln delta: the pinned set is a feasible point, so the
          // solved set is never above it here, whatever the rms in delta does
          out.log_rms_before = rmsOf(y.map(function (v, r) { return v - dot(X[r], pinnedVals); }));
          out.log_rms_after = rmsOf(y.map(function (v, r) { return v - dot(X[r], ls.beta); }));
          if (out.distinct_p.length === 1) out.notes.push('all ' + usedP.length + ' rows share p = ' + out.distinct_p[0]);
          if (out.distinct_Ne.length === 1) out.notes.push('all ' + usedP.length + ' rows share Ne = ' + out.distinct_Ne[0]);
          if (out.dof === 0) {
            out.notes.push('as many determined unknowns as rows (' + ls.rank + '): the solve interpolates and ' +
                           'every residual vanishes by construction. No evidence is left to test the ' +
                           'coefficients -- this is the debt the brief names, hidden rather than paid');
          }
          out.notes.push('minimised: the squared residual of ln delta (the log form is linear); ' +
                         'the rms reported is in delta itself, for comparison with the pinned set');
        }
        out.rowsUsed = usedP;
      }
      // the p = 0 rows, separately: ln d - ln cf - ln C - ln((Ne-1)/Ne) = ln H + K ln Ne
      if (subset === 'all') {
        if (usedH.length) {
          var namesH = [{ coef: 'ln H', column: '1' }, { coef: 'K', column: 'ln Ne' }];
          var XH = usedH.map(function (r) { return [1, Math.log(r.Ne)]; });
          var yH = usedH.map(function (r) {
            var t = termsPinned(r);
            return Math.log(r.delta) - Math.log(t.cf) - Math.log(r.C) - Math.log(t.ratio);
          });
          try {
            var lsH = lsHeld(XH, yH, namesH, [Math.log(coef.H), coef.K], tol);
            out.H = { H: Math.exp(lsH.beta[0]), K: lsH.beta[1], rank: lsH.rank, dof: usedH.length - lsH.rank,
                      status_H: lsH.determined.indexOf(0) >= 0 ? DERIVED : PINNED,
                      status_K: lsH.determined.indexOf(1) >= 0 ? DERIVED : PINNED,
                      undetermined: lsH.undetermined.map(function (u) { return { coefficient: u.name === 'ln H' ? 'H' : 'K', reason: u.reason }; }),
                      n: usedH.length };
            var dsH = { H: out.H.H, K: out.H.K };
            var bH = [], aH = [];
            usedH.forEach(function (r) {
              bH.push(r.delta - termsPinned(r).delta);
              aH.push(r.delta - channelDelta(r.p, r.Ne, r.charge, r.C, withCoef(withCoef(coef, 'H', dsH.H), 'K', dsH.K)));
            });
            out.H.rms_before = rmsOf(bH); out.H.rms_after = rmsOf(aH);
          } catch (err2) { out.notes.push('p = 0 solve failed: ' + err2.message); }
        } else {
          out.notes.push('no usable p = 0 rows for (ln H, K)');
        }
      }
    }
    // residuals before / after, in delta, over the rows used for the main solve
    var used = out.rowsUsed || [];
    var before = [], after = [];
    used.forEach(function (r) {
      var eqP = termsPinned(r).delta;
      var eqS = channelDelta(r.p, r.Ne, r.charge, r.C, out.solved);
      before.push(r.delta - eqP); after.push(r.delta - eqS);
      out.perRow.push({ row: r, eq_pinned: eqP, res_pinned: r.delta - eqP, eq_solved: eqS, res_solved: r.delta - eqS });
    });
    out.rms_before = rmsOf(before);
    out.rms_after = rmsOf(after);
    return out;
  }

  // (c) drift: one coefficient inverted at every measured channel of the index.
  function drift(rows, name, coef) {
    var series = [], refused = {}, nRef = 0, solved = [];
    rows.forEach(function (r) {
      var inv = invertCoefficient(r, name, coef);
      if (inv.solvable) {
        series.push({ x: r.Z, y: inv.value, label: r.label, charge: r.charge, l: r.l, mult: r.mult,
                      gap: inv.gap, residual: inv.residual });
        solved.push(inv.value);
      } else {
        nRef += 1;
        refused[inv.code] = (refused[inv.code] || 0) + 1;
      }
    });
    var sorted = solved.slice().sort(function (a, b) { return a - b; });
    var trend = null;
    if (series.length >= 2) {
      var n = series.length, sx = 0, sy = 0;
      series.forEach(function (s) { sx += s.x; sy += s.y; });
      var mx = sx / n, my = sy / n, sxx = 0, sxy = 0, syy = 0;
      series.forEach(function (s) { sxx += (s.x - mx) * (s.x - mx); sxy += (s.x - mx) * (s.y - my); syy += (s.y - my) * (s.y - my); });
      if (sxx > 0) {
        var slope = sxy / sxx;
        trend = { slope: slope, intercept: my - slope * mx,
                  r: (syy > 0 ? sxy / Math.sqrt(sxx * syy) : null), n: n };
      }
    }
    return { coefficient: name, pinned: coef[name], n_rows: rows.length, n_solvable: series.length,
             n_refused: nRef, refused: refused, series: series,
             min: sorted.length ? sorted[0] : null, max: sorted.length ? sorted[sorted.length - 1] : null,
             median: sorted.length ? median(sorted) : null, trend: trend };
  }

  // ---------------------------------------------------------- a selftest kit
  function Checker() { this.checked = 0; this.failed = 0; this.failures = []; this.notes = []; }
  Checker.prototype.eq = function (name, got, want) {
    this.checked += 1;
    var ok = (typeof got === 'object' && got !== null) ? JSON.stringify(got) === JSON.stringify(want) : got === want;
    if (!ok) { this.failed += 1; this.failures.push({ name: name, got: got, want: want }); }
    return ok;
  };
  Checker.prototype.near = function (name, got, want, tol) {
    this.checked += 1;
    var ok = typeof got === 'number' && typeof want === 'number' && Math.abs(got - want) <= tol;
    if (!ok) { this.failed += 1; this.failures.push({ name: name, got: got, want: want }); }
    return ok;
  };
  Checker.prototype.ok = function (name, cond, got, want) {
    this.checked += 1;
    if (!cond) { this.failed += 1; this.failures.push({ name: name, got: got === undefined ? false : got, want: want === undefined ? true : want }); }
    return !!cond;
  };
  Checker.prototype.result = function () {
    return { checked: this.checked, failed: this.failed, failures: this.failures, notes: this.notes.join('\n') };
  };

  function loadedRecords(ctx) {
    var out = [];
    for (var Z = 1; Z <= 120; Z++) { var r = ctx.element(Z); if (r) out.push(r); }
    return out;
  }
  // The equation port against every channel of the given records: to 1e-9 and
  // exactly; C(Z, l) against the exported C_of_Z exactly.
  function checkEquationPort(ck, records, ctx, tag) {
    var coef = coefficients(ctx.index), params = collapseParams(ctx.index);
    var n = 0, exact = 0, worst = 0, badC = 0, bad = 0, first = null;
    records.forEach(function (rec) {
      if (!rec.populated) return;
      rec.channels.forEach(function (ch) {
        var C = collapseC(rec.Z, ch.l, params);
        if (C !== ch.C_of_Z) badC += 1;
        var d = channelDelta(ch.p, ch.Ne, ch.charge, C, coef);
        n += 1;
        if (d === ch.delta_equation) exact += 1;
        var err = Math.abs(d - ch.delta_equation);
        if (err > worst) worst = err;
        if (!(err <= 1e-9)) { bad += 1; if (!first) first = { Z: rec.Z, charge: ch.charge, l: ch.l, got: d, want: ch.delta_equation }; }
      });
    });
    ck.ok(tag + ': every channel\'s delta_equation reproduced to 1e-9 (' + n + ' channels, ' + records.length + ' records)', bad === 0, first || bad, 0);
    ck.ok(tag + ': C(Z, l) equals the exported C_of_Z exactly', badC === 0, badC, 0);
    ck.notes.push(tag + ': ' + n + ' channels compared, ' + exact + ' bit-exact, worst |difference| ' + worst.toExponential(3) +
                  '; ' + coef.note);
    return n;
  }
  function checkHydrogenic(ck, ctx) {
    var coef = coefficients(ctx.index), params = collapseParams(ctx.index);
    [1, 20, 50, 92].forEach(function (Z) {
      [0, 2, 3].forEach(function (l) {
        // charge = Z is the one-electron ion: Ne = 1, core = 0, p = 0
        ck.eq('hydrogenic channel Z=' + Z + ' l=' + l + ' returns exactly 0',
              channelDelta(0, 1, Z, collapseC(Z, l, params), coef), 0);
      });
    });
    var fx = ctx.index && ctx.index.fixtures && ctx.index.fixtures.hydrogenic_zero;
    if (fx) ck.eq('fixtures.hydrogenic_zero', channelDelta(0, 1, fx.charge, collapseC(fx.Z, fx.l, params), coef), fx.delta_equation);
  }
  function measuredRowsFrom(records, ctx) {
    return measuredRowsAll(records.filter(function (r) { return r.populated; }), collapseParams(ctx.index));
  }
  function checkEquationReport(ck, rows, ctx) {
    var coef = coefficients(ctx.index);
    var rep = equationReport(rows.map(function (r) {
      return { delta: r.delta, delta_equation: channelDelta(r.p, r.Ne, r.charge, r.C, coef), l: r.l };
    }));
    var fx = ctx.index && ctx.index.fixtures && ctx.index.fixtures.equation_report;
    if (fx) {
      ck.eq('equation report: channels = fixtures.equation_report.channels', rep.channels, fx.channels);
      ck.near('equation report: rms = fixture', rep.rms, fx.rms, 1e-9);
      ck.near('equation report: R2 = fixture', rep.R2, fx.R2, 1e-9);
      ck.near('equation report: median |error| = fixture', rep.median_abs_error, fx.median_abs_error, 1e-9);
      if (fx.by_l) {
        ck.eq('equation report: by-l counts = fixture', rep.by_l.map(function (b) { return [b.l, b.n]; }),
              fx.by_l.map(function (b) { return [b.l, b.n]; }));
        var worst = 0;
        rep.by_l.forEach(function (b, i) { if (fx.by_l[i]) worst = Math.max(worst, Math.abs(b.rms - fx.by_l[i].rms)); });
        ck.ok('equation report: by-l rms = fixture to 1e-9', worst <= 1e-9, worst, 0);
      }
      ck.notes.push('equation report held against ctx.index.fixtures.equation_report');
    } else {
      ck.eq('equation report: 358 measured channels compared', rep.channels, 358);
      ck.eq('equation report: rms 0.1809 (4 dp, the generator\'s fixture)', Number(rep.rms.toFixed(4)), 0.1809);
      ck.eq('equation report: R2 0.9656 (4 dp)', Number(rep.R2.toFixed(4)), 0.9656);
      ck.eq('equation report: median |error| 0.0587 (4 dp)', Number(rep.median_abs_error.toFixed(4)), 0.0587);
      ck.notes.push('no ctx.index.fixtures.equation_report; held against the generator\'s recorded figures to 4 dp');
    }
    ck.notes.push('equation report: n ' + rep.channels + ' rms ' + rep.rms.toFixed(4) + ' R2 ' + rep.R2.toFixed(4) +
                  ' median |error| ' + rep.median_abs_error.toFixed(4));
    return rep;
  }

  // ------------------------------------------------------------------ modes
  var SELECTION = { Z: { name: 'Z', label: 'Z', type: 'number', default: 19, fromSelection: 'Z', help: 'atomic number, 1 to 120' },
                    charge: { name: 'charge', label: 'stage (charge)', type: 'number', default: 1, fromSelection: 'charge', help: 'spectroscopic stage; 1 is neutral' },
                    l: { name: 'l', label: 'l', type: 'number', default: 0, fromSelection: 'l', help: '0 = s, 1 = p, 2 = d, 3 = f ...' },
                    mult: { name: 'mult', label: 'mult', type: 'number', default: '', fromSelection: 'mult', help: 'the measured row\'s multiplicity; blank picks the channel\'s only measured row' } };
  function sel(name, override) {
    var o = {}; var base = SELECTION[name];
    Object.keys(base).forEach(function (k) { o[k] = base[k]; });
    if (override) Object.keys(override).forEach(function (k) { o[k] = override[k]; });
    return o;
  }
  async function elementOrFail(ctx, Z) {
    if (Z === null || Z < 1 || Z > 120) return { fail: fail('Z must be an integer from 1 to 120') };
    var rec = ctx.element(Z) || await ctx.load(Z);
    if (!rec) return { fail: fail('no record for Z = ' + Z) };
    if (!rec.populated) {
      return { fail: fail('Z = ' + Z + ' (' + rec.symbol + ') is not populated: ' +
                          (caveat(ctx.index, 'above-108') || 'the observed configurations stop at Z = 108') +
                          (rec.note ? ' (' + rec.note + ')' : '')) };
    }
    return { rec: rec };
  }

  // 1. channel-equation ---------------------------------------------------
  var MODE_EQUATION = {
    id: 'channel-equation',
    title: 'The channel equation',
    status: PINNED,
    statusNote: 'The final form of the channel equation, as tools/populate.py channel_delta computes it; its p = 0 branch carries the RECOVERED collapse ramp.',
    description: 'Values one Rydberg channel (Z, stage, l) of a populated element by the channel equation, term by term: the charge factor ln(c+1)/c, the exponent e(Ne) = E0 - E1 ln Ne, p^e, Ne^K and C(Z) where the branch needs it. The result is set beside the delta_equation the exporter wrote, with their difference, and beside every measured row of the channel with its residual. Nothing is fitted; the coefficients are the equation\'s own.',
    inputs: [sel('Z'), sel('charge'), sel('l')],
    source: { instrument: 'channel_delta', file: 'tools/populate.py' },
    run: async function (values, ctx) {
      var Z = int(values.Z), charge = int(values.charge), l = int(values.l);
      if (Z === null || charge === null || l === null) return fail('Z, charge and l must be integers');
      if (l < 0) return fail('l must be 0 or more');
      var got = await elementOrFail(ctx, Z);
      if (got.fail) return got.fail;
      var rec = got.rec;
      if (charge < 1 || charge > Z) return fail('stage must be 1 to ' + Z + ' for Z = ' + Z);
      var coef = coefficients(ctx.index), params = collapseParams(ctx.index);
      var ch = findChannel(rec, charge, l);
      var Ne = Z - charge + 1, core = Ne - 1, p, pSource, exported = null, C = collapseC(Z, l, params);
      if (ch) { p = ch.p; pSource = 'the record\'s channel ' + label(rec.symbol, charge, l); exported = ch.delta_equation; }
      else if (core === 0) { p = 0; pSource = 'core Ne = 0: p = 0 (populate.channel_delta)'; }
      else {
        var coreRec = ctx.element(core) || await ctx.load(core);
        if (!coreRec || !coreRec.populated) return fail('no channel (' + charge + ', ' + l + ') in the record and the core Z = ' + core + ' is not populated');
        p = coreP(coreRec.configuration, l);
        pSource = 'core_p over the observed configuration of the core, ' + coreRec.symbol;
      }
      var t = channelTerms(p, Ne, charge, C, coef);
      var rows = [
        row('channel', label(rec.symbol, charge, l), READ, 'Ne = Z - charge + 1; the core it presents is ' + (core >= 1 ? 'Z = ' + core : 'empty')),
        row('Ne', Ne, DERIVED, 'electron count of the ion'),
        row('p', p, PINNED, pSource),
        row('branch', t.branch, PINNED, t.branch === 'p > 0' ? 'delta = A p^e(Ne) Ne^K ln(c+1)/c' : 'delta = H C(Z) ((Ne-1)/Ne) Ne^K ln(c+1)/c'),
        row('charge factor ln(c+1)/c', t.cf, DERIVED, 'c = ' + charge)
      ];
      if (t.branch === 'p > 0') {
        rows.push(row('e(Ne) = E0 - E1 ln Ne', t.e, PINNED, 'E0 = ' + coef.E0 + ', E1 = ' + coef.E1 + (coef.fallback.length ? ' (' + coef.note + ')' : '')));
        rows.push(row('p^e', t.pe, DERIVED));
        rows.push(row('Ne^K', t.nk, DERIVED, 'K = ' + coef.K));
        rows.push(row('A', coef.A, PINNED, 'the channel equation, final form'));
      } else {
        rows.push(row('C(Z, l)', C, RECOVERED, 'the collapse ramp; its form is stated in no source'));
        rows.push(row('(Ne-1)/Ne', t.ratio, DERIVED, Ne === 1 ? 'vanishes identically at Ne = 1, the hydrogenic channel: the hydrogenic channel is exactly zero' : undefined));
        rows.push(row('Ne^K', t.nk, DERIVED, 'K = ' + coef.K));
        rows.push(row('H', coef.H, PINNED, 'the channel equation, final form'));
      }
      rows.push(row('delta by equation', t.delta, PINNED, 'computed here from the terms above'));
      if (exported !== null) {
        rows.push(row('delta_equation exported', exported, PINNED, 'tools/populate.py, as the exporter wrote it'));
        rows.push(row('difference (here - exported)', t.delta - exported, DERIVED, t.delta === exported ? 'bit-exact' : 'the two ports differ in the last bits of pow/log'));
      } else {
        rows.push(row('delta_equation exported', 'no channel (' + charge + ', ' + l + ') in the record', undefined, 'p came from the core\'s configuration instead'));
      }
      if (ch && ch.measured && ch.measured.length) {
        ch.measured.forEach(function (m) {
          rows.push(row('delta, mult ' + m.mult + ' (' + m.grade + ')', m.delta, READ, m.witness + '; ' + m.source));
          rows.push(row('residual, mult ' + m.mult, m.delta - t.delta, DERIVED, 'measured - equation' + (m.grade !== 'measured' ? '; the row is ' + m.grade + ', not measured' : '')));
        });
      }
      if (coef.fallback.length) rows.push(row('coefficients', coef.note, PINNED));
      var dom = caveat(ctx.index, 'equation-domain');
      if (dom) rows.push(row('caveat', dom));
      return { rows: rows, ok: true };
    },
    selftest: async function (ctx) {
      var ck = new Checker();
      checkHydrogenic(ck, ctx);
      var recs = loadedRecords(ctx);
      if (!recs.length) { recs = [await ctx.load(19)]; ck.notes.push('no element was loaded; K (Z = 19) loaded for the port check'); }
      checkEquationPort(ck, recs, ctx, 'loaded elements');
      var k = ctx.element(19) || await ctx.load(19);
      if (k && k.populated) {
        var coef = coefficients(ctx.index), params = collapseParams(ctx.index);
        var s = findChannel(k, 1, 0), f = findChannel(k, 1, 3);
        ck.ok('K I: the equation falls with l (ns > nf)',
              channelDelta(s.p, s.Ne, 1, collapseC(19, 0, params), coef) > channelDelta(f.p, f.Ne, 1, collapseC(19, 3, params), coef));
      }
      var fx = ctx.index && ctx.index.fixtures;
      var sample = fx && (fx.coefficient_roundtrip_sample && fx.coefficient_roundtrip_sample.rows || fx.sample);
      if (sample && sample.length) {
        var coef2 = coefficients(ctx.index), params2 = collapseParams(ctx.index), bad = 0;
        sample.forEach(function (s) {
          var d = channelDelta(s.p, s.Ne, s.charge, collapseC(s.Z, s.l, params2), coef2);
          if (!(Math.abs(d - s.delta_equation) <= 1e-9)) bad += 1;
        });
        ck.ok('fixtures sample: ' + sample.length + ' rows reproduced to 1e-9', bad === 0, bad, 0);
      }
      return ck.result();
    }
  };

  // 2. pauli-bound --------------------------------------------------------
  var MODE_PAULI = {
    id: 'pauli-bound',
    title: 'The Pauli bound',
    status: PINNED,
    statusNote: 'The Pauli bound, B = min(p, n0 - l - 1), Pauli 1925 and Janet 1929; n0\'s reading is RECONSTRUCTED.',
    description: 'B = max(0, min(p, n0 - l - 1)) for a channel. p is the core\'s orbital count at this l and n0 the first entirely unoccupied n; both are taken from the selected channel\'s record unless typed. n0\'s reading is a reconstruction: the definition names the term but not whether a partly filled subshell counts, and He I ns settles it for "first entirely unoccupied n". Where the record carries the CSV\'s B the two are set side by side and a disagreement is recorded, not repaired.',
    inputs: [sel('Z'), sel('charge'), sel('l'),
             { name: 'p', label: 'p', type: 'number', default: '', help: 'blank: from the selected channel\'s record' },
             { name: 'n0', label: 'n0', type: 'number', default: '', help: 'blank: from the selected channel\'s record' }],
    source: { instrument: 'pauli_bound', file: 'tools/populate.py' },
    run: async function (values, ctx) {
      var l = int(values.l), p = int(values.p), n0 = int(values.n0);
      var Z = int(values.Z), charge = int(values.charge);
      if (l === null || l < 0) return fail('l must be an integer, 0 or more');
      var rows = [], ch = null, rec = null, pSrc = 'typed', nSrc = 'typed';
      if (p === null || n0 === null) {
        if (Z === null || charge === null) return fail('type p and n0, or give Z and charge so they can be read from the record');
        var got = await elementOrFail(ctx, Z);
        if (got.fail) return got.fail;
        rec = got.rec;
        if (charge < 1 || charge > Z) return fail('stage must be 1 to ' + Z);
        ch = findChannel(rec, charge, l);
        var core = Z - charge;
        if (ch) {
          if (p === null) { p = ch.p; pSrc = 'record, channel ' + label(rec.symbol, charge, l); }
          if (n0 === null) { n0 = ch.n0; nSrc = 'record, channel ' + label(rec.symbol, charge, l); }
        }
        if (p === null || n0 === null) {
          if (core < 1) { if (p === null) p = 0; if (n0 === null) n0 = l + 1; pSrc = nSrc = 'empty core (one-electron ion): p = 0'; }
          else {
            var coreRec = ctx.element(core) || await ctx.load(core);
            if (!coreRec || !coreRec.populated) return fail('no channel (' + charge + ', ' + l + ') in the record and the core Z = ' + core + ' is not populated');
            if (p === null) { p = coreP(coreRec.configuration, l); pSrc = 'core_p over ' + coreRec.symbol + '\'s observed configuration'; }
            if (n0 === null) { n0 = n0Of(coreRec.configuration, l); nSrc = 'n0_of over ' + coreRec.symbol + '\'s observed configuration'; }
          }
        }
      }
      if (n0 === null) return fail('n0 is not carried for this channel; type it');
      var B = pauliBound(p, n0, l);
      rows.push(row('p', p, pSrc === 'typed' ? null : PINNED, pSrc === 'typed' ? 'typed, not a figure of the index' : pSrc));
      rows.push(row('n0', n0, nSrc === 'typed' ? null : RECONSTRUCTED, nSrc === 'typed' ? 'typed, not a figure of the index' : nSrc + '; first entirely unoccupied n at this l'));
      rows.push(row('l', l, ch ? READ : null, ch ? 'the channel\'s l' : 'typed'));
      rows.push(row('n0 - l - 1', n0 - l - 1, DERIVED));
      rows.push(row('B = max(0, min(p, n0 - l - 1))', B, PINNED, 'the Pauli bound'));
      if (ch) {
        rows.push(row('B_computed exported', ch.B_computed, PINNED, ch.B_computed === B ? 'agrees' : 'DIFFERS from the value computed here'));
        (ch.measured || []).forEach(function (m) {
          if (m.B_csv_is_not_a_bound) rows.push(row('B in the CSV, mult ' + m.mult, 'not a bound', READ, caveat(ctx.index, 'b-overloaded') || 'a dispersion, not a bound'));
          else if (m.B_csv !== null && m.B_csv !== undefined) rows.push(row('B in the CSV, mult ' + m.mult, m.B_csv, READ, m.B_csv === B ? 'agrees' : 'DISAGREES: ' + (caveat(ctx.index, 'b-aufbau') || 'the column was built on the withdrawn aufbau table')));
        });
      }
      var cv = caveat(ctx.index, 'n0-reading');
      rows.push(row('caveat', cv || 'n0\'s reading is RECONSTRUCTED (caveat n0-reading is not carried by this build of data/index.js)'));
      return { rows: rows, ok: true };
    },
    selftest: async function (ctx) {
      var ck = new Checker();
      var he = ctx.element(2) || await ctx.load(2), be = ctx.element(4) || await ctx.load(4);
      var heCh = findChannel(he, 1, 0), beCh = findChannel(be, 1, 0);
      ck.eq('He I ns: B = 1 (populate.selftest)', pauliBound(heCh.p, heCh.n0, 0), 1);
      ck.eq('Be I ns: B = 2', pauliBound(beCh.p, beCh.n0, 0), 2);
      var fx = ctx.index && ctx.index.fixtures && ctx.index.fixtures.pauli;
      if (fx && fx.rows) {
        for (var i = 0; i < fx.rows.length; i++) {
          var f = fx.rows[i], r = ctx.element(f.Z) || await ctx.load(f.Z), c = findChannel(r, f.charge, f.l);
          ck.eq('fixtures.pauli ' + f.label, pauliBound(c.p, c.n0, f.l), f.B);
        }
      }
      var recs = loadedRecords(ctx), n = 0, bad = 0, nCore = 0, badCore = 0, first = null;
      var byZ = {};
      recs.forEach(function (r) { byZ[r.Z] = r; });
      recs.forEach(function (rec) {
        if (!rec.populated) return;
        rec.channels.forEach(function (ch) {
          if (ch.core_Ne < 1) return;
          n += 1;
          if (pauliBound(ch.p, ch.n0, ch.l) !== ch.B_computed) { bad += 1; if (!first) first = { Z: rec.Z, charge: ch.charge, l: ch.l }; }
          var core = byZ[ch.core_Ne];
          if (core && core.populated) {
            nCore += 1;
            if (coreP(core.configuration, ch.l) !== ch.p || n0Of(core.configuration, ch.l) !== ch.n0) badCore += 1;
          }
        });
      });
      ck.ok('every loaded channel: B = max(0, min(p, n0-l-1)) reproduces B_computed (' + n + ' channels)', bad === 0, first || bad, 0);
      ck.ok('every loaded channel with a loaded core: core_p and n0_of over the core\'s configuration reproduce p and n0 (' + nCore + ' channels)', badCore === 0, badCore, 0);
      // a typed p with a blank n0: n0 comes from the record and keeps its RECONSTRUCTED status
      var fe = ctx.element(26) || await ctx.load(26);
      if (fe) {
        var typed = await MODE_PAULI.run({ Z: 26, charge: 1, l: 0, p: '4', n0: '' }, ctx);
        ck.eq('typed p, blank n0 (Fe I s): n0 read from the record is RECONSTRUCTED', typed.rows[1].status, RECONSTRUCTED);
        ck.eq('typed p, blank n0 (Fe I s): the typed p carries no status', typed.rows[0].status, null);
        ck.eq('typed p, blank n0 (Fe I s): n0 is the record\'s', typed.rows[1].value, findChannel(fe, 1, 0).n0);
      }
      ck.notes.push(recs.length + ' records loaded');
      return ck.result();
    }
  };

  // 3. collapse -----------------------------------------------------------
  var MODE_COLLAPSE = {
    id: 'collapse',
    title: 'The collapse coordinate C(Z, l)',
    status: RECOVERED,
    statusNote: 'The collapse ramp\'s thresholds are stated, and that it is "one lookup, not fitted"; the form was inverted out of COORDINATES-2.13\'s computed column and no source states it.',
    description: function (ctx) {
      var p = collapseParams(ctx.index), ls = Object.keys(p.Z0).sort();
      return 'C(Z, l) = clamp(0.5 + (Z - Z0(l)) / ' + p.width + ', 0, 1), a ramp ' + p.width + ' wide reaching exactly 0.5 at the Janet block opening Z0 = ' +
             ls.map(function (l) { return p.Z0[l]; }).join(', ') + ' for l = ' + ls.join(', ') + (p.fromIndex ? ' (index.collapse)' : ' (populate.py\'s own values; index.collapse absent)') +
             '. It is RECOVERED, not PINNED: the index agrees with it exactly but no source writes it down. Above l = ' + ls[ls.length - 1] + ' every channel inverts to C = 0 and there is no ramp to show.';
    },
    inputs: [sel('Z'), sel('l', { default: 2 })],
    source: { instrument: 'collapse_C', file: 'tools/populate.py' },
    run: async function (values, ctx) {
      var Z = int(values.Z), l = int(values.l);
      if (Z === null || l === null || l < 0) return fail('Z and l must be integers, l 0 or more');
      var params = collapseParams(ctx.index);
      var z0 = params.Z0[l];
      var C = collapseC(Z, l, params);
      var rows = [row('C(Z = ' + Z + ', l = ' + l + ')', C, RECOVERED, 'clamp(0.5 + (Z - Z0) / ' + params.width + ', 0, 1)')];
      var rec = ctx.element(Z);
      if (rec && rec.populated) {
        var any = null;
        for (var i = 0; i < rec.channels.length; i++) if (rec.channels[i].l === l) { any = rec.channels[i]; break; }
        if (any) rows.push(row('C_of_Z exported', any.C_of_Z, RECOVERED, any.C_of_Z === C ? 'agrees exactly' : 'DIFFERS'));
      }
      if (z0 === undefined || z0 === null) {
        rows.push(row('Z0(l)', 'none', RECOVERED, l >= 4
          ? 'no collapse above l = 3: every l >= 4 channel of the index inverts to C = 0 exactly, so C = 0'
          : 'l = 0 has no Janet threshold in the recovered form (Z0 is stated for l = 1, 2, 3); C = 0, and the p = 0 branch is reached at l = 0 only by the one-electron ion, where (Ne-1)/Ne vanishes'));
        return { rows: rows, ok: true };
      }
      rows.push(row('Z0(l = ' + l + ')', z0, RECOVERED, l === 2 ? 'the stated threshold: the n+l = 5 block opens at Z = 21 (Sc)' : l === 3 ? 'the stated threshold: the n+l = 7 block opens at Z = 57 (La)' : 'boron, where the 2p block opens: the same rule, stated nowhere'));
      rows.push(row('ramp width', params.width, RECOVERED, 'eight wide, saturating four beyond Z0'));
      var series = [];
      for (var z = z0 - 4; z <= z0 + 4; z++) {
        var c = collapseC(z, l, params);
        rows.push(row('C(' + z + ', ' + l + ')' + (z === Z ? '  <- this Z' : ''), c, RECOVERED, z === z0 ? 'the Janet boundary: exactly 0.5' : undefined));
        series.push({ x: z, y: c, label: 'C(' + z + ', ' + l + ')' });
      }
      return { rows: rows, ok: true, series: series, seriesLabel: 'C(Z, l = ' + l + ') across the ramp Z0 - 4 .. Z0 + 4' };
    },
    selftest: async function (ctx) {
      var ck = new Checker(), params = collapseParams(ctx.index);
      Object.keys(params.Z0).forEach(function (lk) {
        var l = Number(lk), z0 = params.Z0[lk];
        ck.eq('C at the l=' + l + ' Janet boundary Z=' + z0 + ' is 0.5', collapseC(z0, l, params), 0.5);
        ck.eq('C four below Z0 (l=' + l + ') is 0', collapseC(z0 - 4, l, params), 0.0);
        ck.eq('C four above Z0 (l=' + l + ') is 1', collapseC(z0 + 4, l, params), 1.0);
      });
      [[18, 0.125], [19, 0.25], [20, 0.375], [21, 0.5], [25, 1.0], [17, 0.0]].forEach(function (zw) {
        ck.near('C(' + zw[0] + ', 2) = ' + zw[1] + ' (inverted out of the index)', collapseC(zw[0], 2, params), zw[1], 1e-12);
      });
      ck.eq('C(50, 4) = 0 above l = 3', collapseC(50, 4, params), 0.0);
      ck.eq('C(50, 7) = 0 above l = 3', collapseC(50, 7, params), 0.0);
      var fx = ctx.index && ctx.index.fixtures && ctx.index.fixtures.collapse_table;
      if (fx && fx.by_l) {
        var bad = 0, n = 0;
        fx.by_l.forEach(function (b) { b.rows.forEach(function (r) { n += 1; if (collapseC(r.Z, b.l, params) !== r.C) bad += 1; }); });
        ck.ok('fixtures.collapse_table: ' + n + ' ramp values reproduced exactly', bad === 0, bad, 0);
      }
      var recs = loadedRecords(ctx), nc = 0, badc = 0;
      recs.forEach(function (rec) {
        if (!rec.populated) return;
        rec.channels.forEach(function (ch) { nc += 1; if (collapseC(rec.Z, ch.l, params) !== ch.C_of_Z) badc += 1; });
      });
      ck.ok('every loaded channel\'s C_of_Z reproduced exactly (' + nc + ' channels)', badc === 0, badc, 0);
      ck.notes.push(params.fromIndex ? 'Z0 and width read from index.collapse' : 'index.collapse absent; Z0 = {1: 5, 2: 21, 3: 57}, width 8 as populate.py pins them');
      return ck.result();
    }
  };

  // 4. closure ------------------------------------------------------------
  function parseCells(text) {
    var lines = String(text || '').split(/\r?\n/), cells = [], d = null, bad = [];
    lines.forEach(function (ln, i) {
      var s = ln.trim();
      if (!s || s.charAt(0) === '#') return;
      var parts = s.split(/[\s,;]+/).map(num);
      if (parts.some(function (v) { return v === null; })) { bad.push('line ' + (i + 1) + ': "' + ln + '" is not a row of numbers'); return; }
      if (d === null) d = parts.length;
      if (parts.length !== d) { bad.push('line ' + (i + 1) + ': ' + parts.length + ' values, expected ' + d); return; }
      cells.push(parts);
    });
    return { cells: cells, d: d, errors: bad };
  }
  function presetCells(index, name) {
    var lay = (index && index.layout) || [], out = [], seen = {};
    if (name === 'periodic') {
      // populate.layout_closure: Z in range(1, 119) and not set aside -- chapter
      // 6's table ends at 118. The exporter draws 119 and 120 at period 8 with
      // set_aside false; they are not main-table cells of the drawn layout.
      lay.forEach(function (e) {
        if (e.Z > 118 || e.set_aside || e.period === null || e.group === null || e.period === undefined || e.group === undefined) return;
        var k = e.period + ',' + e.group;
        if (!seen[k]) { seen[k] = true; out.push([e.period, e.group]); }
      });
      return { name: 'periodic', coords: ['period', 'group'], cells: out.sort(function (a, b) { return a[0] - b[0] || a[1] - b[1]; }),
               index: 'periodic table (period x group): the elements Z <= 118 not set aside' };
    }
    if (name === 'janet') {
      lay.forEach(function (e) {
        if (!e.janet) return;
        var k = e.janet[0] + ',' + e.janet[1];
        if (!seen[k]) { seen[k] = true; out.push([e.janet[0], e.janet[1]]); }
      });
      return { name: 'janet', coords: ['n+l', 'l'], cells: out.sort(function (a, b) { return a[0] - b[0] || a[1] - b[1]; }),
               index: 'Janet (n+l x l): the distinct cells of the elements that have one' };
    }
    return null;
  }
  function cellsText(cells) { return cells.map(function (c) { return c.join(' '); }).join('\n'); }
  function janetCypherFixture() {          // cypher._janet: n = 1..7, l < min(n, 4)
    var cells = [], seen = {};
    for (var n = 1; n <= 7; n++) for (var l = 0; l < Math.min(n, 4); l++) {
      var k = (n + l) + ',' + l;
      if (!seen[k]) { seen[k] = true; cells.push([n + l, l]); }
    }
    return cells;
  }
  function lambdaCypherFixture() {         // cypher._lambda: the 976 cells at the standing caps
    var cells = [];
    for (var n = 1; n <= 3; n++) for (var l = 0; l <= 1; l++) for (var k = 1; k <= 3; k++)
      for (var q = 0; q <= 3; q++) for (var e = 1; e <= 3; e++) for (var f = 0; f <= 1; f++)
        for (var g = 0; g <= 3; g++) for (var S = 0; S <= 3; S++) {
          var cell = [n, l, k, q, e, f, g, S];
          if (lambdaConstraints(cell).every(function (c) { return c.holds; })) cells.push(cell);
        }
    return cells;
  }
  var MODE_CLOSURE = {
    id: 'closure',
    title: 'Order closure, R',
    status: PINNED,
    statusNote: 'R, the order operator, as tools/cypher.py op_order runs it: a cell is admitted when every cell below it on every axis is held.',
    description: function (ctx) {
      var c = (ctx.index && ctx.index.closure) || null, j = ((ctx.index && ctx.index.fixtures && ctx.index.fixtures.closure) || {}).janet || null;
      return 'Runs R over a set of cells: the alphabets are the distinct values per coordinate, the ambient set their product, phi(i, j, a) = max{ y_i : y in X, y_j <= a }, and a cell is admitted when x_i <= phi(i, j, x_j) for every pair. Reports the cells held, the cells admitted, E = admitted - held and the denied cells.' +
             (c ? ' On the drawn periodic layout its ' + c.held + ' cells give ' + c.admitted + ' admitted and E = ' + c.E + ' (index.closure)' : '') +
             (j ? '; on Janet\'s coordinate, the elements\' own cells, E = ' + j.E + ' (fixtures.closure.janet)' : '') + '.';
    },
    inputs: [
      { name: 'preset', label: 'cells from', type: 'select', default: 'periodic',
        options: [{ value: 'periodic', label: 'periodic table (period x group), the held cells' },
                  { value: 'janet', label: 'Janet (n+l, l), the elements\' distinct cells' },
                  { value: 'custom', label: 'the cells typed below' }],
        help: 'periodic and janet read ctx.index.layout; custom parses the box' },
      { name: 'cells', label: 'cells, one per line', type: 'textarea', default: '',
        help: 'used when "cells from" is custom: "p g" per line, any dimension d >= 2, every line the same d; the UI may prefill it with LIB.presetCells' }
    ],
    source: { instrument: 'op_order', file: 'tools/cypher.py' },
    run: async function (values, ctx) {
      var preset = values.preset || 'periodic', cells, coords, srcNote;
      if (preset === 'custom') {
        var parsed = parseCells(values.cells);
        if (parsed.errors.length) return fail(parsed.errors.join('; '));
        if (!parsed.cells.length) return fail('no cells in the box');
        if (parsed.d < 2) return fail('R needs at least two coordinates per cell');
        cells = parsed.cells; coords = null; srcNote = 'the cells box, ' + cells.length + ' lines';
      } else {
        var ps = presetCells(ctx.index, preset);
        if (!ps || !ps.cells.length) return fail('preset ' + preset + ' has no cells in ctx.index.layout');
        cells = ps.cells; coords = ps.coords; srcNote = ps.index;
      }
      var res;
      try { res = orderClosure(cells); } catch (err) { return fail(err.message); }
      var rows = [
        row('cells from', srcNote, undefined),
        row('coordinates', coords ? coords.join(' x ') : 'd = ' + res.d, undefined),
        row('held', res.held.length, PINNED, 'distinct cells given'),
        row('ambient box', res.box, DERIVED, 'product of the alphabets'),
        row('admitted by R', res.admitted.length, PINNED, res.note),
        row('E = admitted - held', res.E, PINNED, 'admitted - held; ' + (res.E === 0 ? 'R admits nothing the set does not hold' : res.E + ' cells R admits and the set denies'))
      ];
      res.warnings.forEach(function (w) { rows.push(row('warning', w)); });
      var text = res.denied.length ? 'denied (admitted, not held):\n' + res.denied.map(function (c) { return '  (' + c.join(', ') + ')'; }).join('\n') : 'no denied cells';
      if (preset === 'periodic' && ctx.index && ctx.index.closure) {
        var ix = ctx.index.closure;
        rows.push(row('exported: held / admitted / E', ix.held + ' / ' + ix.admitted + ' / ' + ix.E, PINNED,
                      (ix.held === res.held.length && ix.admitted === res.admitted.length && ix.E === res.E) ? 'agrees with index.closure' : 'DIFFERS from index.closure'));
      }
      return { rows: rows, ok: true, text: text, denied: res.denied };
    },
    selftest: async function (ctx) {
      var ck = new Checker();
      var fx = ctx.index && ctx.index.fixtures && ctx.index.fixtures.closure;
      var per = presetCells(ctx.index, 'periodic');
      if (per && per.cells.length) {
        var r = orderClosure(per.cells);
        var want = fx && fx.periodic ? fx.periodic : { held: 90, admitted: 126, E: 36 };
        ck.eq('periodic: held', r.held.length, want.held);
        ck.eq('periodic: admitted', r.admitted.length, want.admitted);
        ck.eq('periodic: E', r.E, want.E);
        var want36 = [];
        for (var g = 2; g <= 17; g++) want36.push([1, g]);
        for (g = 3; g <= 12; g++) want36.push([2, g]);
        for (g = 3; g <= 12; g++) want36.push([3, g]);
        var denied = r.denied.slice().sort(function (a, b) { return a[0] - b[0] || a[1] - b[1]; });
        ck.eq('periodic: the 36 denied are the drawn layout\'s (p1,g2..g17), (p2,g3..g12), (p3,g3..g12)', denied, want36);
        if (ctx.index.closure && ctx.index.closure.denied) ck.eq('periodic: denied = index.closure.denied', denied, ctx.index.closure.denied);
        // E is placement-sensitive -- helium moved from (1, 18) to (1, 2) and
        // nothing else, E falls from 36 to 20; the build's own figure is the fixture
        var moved = per.cells.filter(function (c) { return !(c[0] === 1 && c[1] === 18); }).concat([[1, 2]]);
        var r2 = orderClosure(moved);
        var want2 = fx && fx.helium_at_2 ? fx.helium_at_2 : { held: 90, admitted: 110, E: 20 };
        ck.eq('helium at group 2: held', r2.held.length, want2.held);
        ck.eq('helium at group 2: E = 20 (the priced alternative)', r2.E, want2.E);
        if (want2.denied) ck.eq('helium at group 2: the twenty denied are the build\'s', r2.denied.slice().sort(function (a, b) { return a[0] - b[0] || a[1] - b[1]; }), want2.denied);
        ck.eq('E prices the placement at sixteen cells', r.E - r2.E, 16);
      } else ck.ok('periodic preset available from index.layout', false, 'no cells', '90 cells');
      var jan = presetCells(ctx.index, 'janet');
      if (jan && jan.cells.length) {
        var rj = orderClosure(jan.cells);
        if (fx && fx.janet) {
          ck.eq('janet (elements): held = fixture', rj.held.length, fx.janet.held);
          ck.eq('janet (elements): admitted = fixture', rj.admitted.length, fx.janet.admitted);
          ck.eq('janet (elements): E = fixture', rj.E, fx.janet.E);
          if (fx.janet.box !== undefined) ck.eq('janet (elements): box = fixture', rj.box, fx.janet.box);
        } else {
          ck.eq('janet (elements): E = 0', rj.E, 0);
        }
        ck.notes.push('janet (elements): ' + rj.held.length + ' cells, box ' + rj.box + ', E ' + rj.E);
      }
      var cj = orderClosure(janetCypherFixture());
      var wantC = fx && fx.janet_cypher_fixture ? fx.janet_cypher_fixture : { held: 22, admitted: 22, E: 0 };
      ck.eq('cypher\'s Janet fixture: held 22', cj.held.length, wantC.held);
      ck.eq('cypher\'s Janet fixture: admitted 22', cj.admitted.length, wantC.admitted);
      ck.eq('cypher\'s Janet fixture: E 0', cj.E, wantC.E);
      var lam = lambdaCypherFixture();
      ck.eq('Lambda_8 at the standing caps: 976 cells (cypher._lambda)', lam.length, 976);
      var rl = orderClosure(lam);
      ck.eq('Lambda_8: box 6912', rl.box, 6912);
      ck.eq('Lambda_8: E(order) = 0', rl.E, 0);
      var cube = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0], [1, 0, 1], [0, 1, 1]];
      var rc = orderClosure(cube);
      ck.eq('d = 3: the cube less a corner, R fills it (E = 1, denied (1,1,1))', [rc.E, rc.denied], [1, [[1, 1, 1]]]);
      return ck.result();
    }
  };

  // 5. lambda8 ------------------------------------------------------------
  var MODE_LAMBDA = {
    id: 'lambda8',
    title: 'A Lambda_8 cell against its constraints',
    status: RECONSTRUCTED,
    statusNote: 'The seven constraints and the standing caps are PINNED; the mapping of an element to cells (the ionisation ladder) is RECONSTRUCTED, and a typed cell carries no status of its own.',
    description: 'Tests one cell (n, l, k, q, e, f, g, 2S) against the seven constraints, each with its origin, and against the standing caps (n, e, l, k, f) = (3, 3, 1, 3, 1). A cell can satisfy all seven and still lie outside the caps; that is reported OUTSIDE with the caps it needs, never truncated. 2S may be left blank, and is then probed as 0 exactly as tools/populate.py does.',
    inputs: [
      { name: 'n', label: 'n (source shell)', type: 'number', default: 3 },
      { name: 'l', label: 'l (source subshell)', type: 'number', default: 1 },
      { name: 'k', label: 'k (source occupancy)', type: 'number', default: 3 },
      { name: 'q', label: 'q (electrons removed)', type: 'number', default: 1 },
      { name: 'e', label: 'e (target shell)', type: 'number', default: 3 },
      { name: 'f', label: 'f (target subshell)', type: 'number', default: 1 },
      { name: 'g', label: 'g (target occupancy)', type: 'number', default: 0 },
      { name: '2S', label: '2S (multiplicity)', type: 'text', default: '', help: 'blank where the term is not carried; probed as 0' }
    ],
    source: { instrument: 'lambda_constraints', file: 'tools/populate.py' },
    run: async function (values, ctx) {
      var cell = [], missing = [];
      LAMBDA_COORDS.forEach(function (c) {
        if (c === '2S') { var s = int(values['2S']); cell.push(s === null ? null : s); return; }
        var v = int(values[c]);
        if (v === null) missing.push(c);
        cell.push(v);
      });
      if (missing.length) return fail('integers needed for ' + missing.join(', '));
      var probe = cell.map(function (v) { return v === null ? 0 : v; });
      var caps = capsOf(ctx.index);
      var cons = lambdaConstraints(probe), within = withinCaps(probe, caps), need = capsNeeded(probe);
      var rows = [row('cell (n, l, k, q, e, f, g, 2S)', '(' + cell.map(function (v) { return v === null ? '-' : v; }).join(', ') + ')', null, 'typed, not a figure of the index' + (cell[7] === null ? '; 2S blank, probed as 0' : ''))];
      var held = 0;
      cons.forEach(function (c) { if (c.holds) held += 1; rows.push(row(c.rule, c.holds ? 'holds' : 'FAILS', PINNED, c.origin)); });
      rows.push(row('constraints held', held + '/7', PINNED));
      var over = [];
      CAP_AXES.forEach(function (ax) {
        if (!(ax in within)) return;
        if (!within[ax]) over.push(ax);
        rows.push(row('cap ' + ax + ' <= ' + caps[ax], within[ax] ? 'within' : 'OUTSIDE', PINNED, 'needs ' + ax + ' >= ' + need[ax]));
      });
      rows.push(row('verdict at the standing caps', over.length ? 'OUTSIDE: needs ' + over.map(function (ax) { return ax + '>=' + need[ax]; }).join(', ') : 'within the caps', PINNED,
                    held === 7 && over.length ? 'satisfies all seven constraints and is still not a cell of Lambda_8 at these caps: the point of the caps' : undefined));
      var cv = caveat(ctx.index, 'lambda8-mapping');
      if (cv) rows.push(row('caveat', cv));
      return { rows: rows, ok: true };
    },
    selftest: async function (ctx) {
      var ck = new Checker(), caps = capsOf(ctx.index);
      var inside = [1, 0, 1, 0, 1, 0, 0, 0];      // TOWER.L8()[0]
      ck.ok('the first cell of L8 satisfies all seven constraints', lambdaConstraints(inside).every(function (c) { return c.holds; }));
      ck.eq('seven constraints are stated', lambdaConstraints(inside).length, 7);
      ck.eq('l <= n-1 fires on (1,1,1,1,1,0,1,1)', lambdaConstraints([1, 1, 1, 1, 1, 0, 1, 1])[0].holds, false);
      ck.eq('Lambda_8 at the caps: 976 cells', lambdaCypherFixture().length, 976);
      var recs = loadedRecords(ctx), nStep = 0, bad = 0, first = null, nEl = 0;
      if (!recs.length) { recs = [await ctx.load(26)]; ck.notes.push('no element was loaded; Fe (Z = 26) loaded for the ladder check'); }
      recs.forEach(function (rec) {
        if (!rec.populated || !rec.lambda8) return;
        nEl += 1;
        rec.lambda8.forEach(function (st) {
          nStep += 1;
          var probe = st.cell.map(function (v) { return v === null ? 0 : v; });
          var cons = lambdaConstraints(probe);
          var okC = JSON.stringify(cons) === JSON.stringify(st.constraints);
          var okW = JSON.stringify(withinCaps(probe, caps)) === JSON.stringify(st.within_caps);
          var okN = JSON.stringify(capsNeeded(probe)) === JSON.stringify(st.caps_needed);
          if (!(okC && okW && okN)) { bad += 1; if (!first) first = { Z: rec.Z, step: st.from + '->' + st.to, constraints: okC, within: okW, needed: okN }; }
        });
      });
      ck.ok('every Lambda_8 step of every loaded element: constraints, within_caps and caps_needed reproduced (' + nStep + ' steps, ' + nEl + ' elements)', nStep > 0 && bad === 0, nStep > 0 ? (first || bad) : 'no steps checked', 0);
      ck.notes.push(nEl + ' populated elements loaded, ' + nStep + ' ladder steps checked');
      return ck.result();
    }
  };

  // 6. coefficient --------------------------------------------------------
  function pickRow(rec, charge, l, mult, params) {
    var ch = findChannel(rec, charge, l);
    if (!ch) return { fail: fail('no channel (' + charge + ', ' + l + ') in the record of ' + rec.symbol) };
    var rows = channelRows({ Z: rec.Z, symbol: rec.symbol, populated: true, channels: [ch] }, params, false);
    if (!rows.length) return { fail: fail('channel ' + label(rec.symbol, charge, l) + ' carries no rows') };
    if (mult !== null) {
      for (var i = 0; i < rows.length; i++) if (rows[i].mult === mult) return { row: rows[i] };
      return { fail: fail('no row at mult ' + mult + ' in ' + label(rec.symbol, charge, l) + '; it holds mult ' + rows.map(function (r) { return r.mult; }).join(', ')) };
    }
    var meas = rows.filter(function (r) { return r.grade === 'measured'; });
    if (meas.length === 1) return { row: meas[0] };
    if (meas.length > 1) return { fail: fail(label(rec.symbol, charge, l) + ' has measured rows at mult ' + meas.map(function (r) { return r.mult; }).join(', ') + '; choose one') };
    if (rows.length === 1) return { row: rows[0] };
    return { fail: fail(label(rec.symbol, charge, l) + ' has no measured row; its rows are mult ' + rows.map(function (r) { return r.mult + ' (' + r.grade + ')'; }).join(', ')) };
  }
  function invertRows(inv, r) {
    var rows = [
      row('channel', r.label, READ, 'grade ' + r.grade + '; ' + r.witness + '; ' + r.source),
      row('branch', inv.branch, PINNED, r.p > 0 ? 'delta = A p^e(Ne) Ne^K ln(c+1)/c' : 'delta = H C(Z) ((Ne-1)/Ne) Ne^K ln(c+1)/c'),
      row('p', r.p, PINNED), row('Ne', r.Ne, DERIVED), row('C(Z, l)', r.C, RECOVERED),
      row(r.grade === 'measured' ? 'delta measured' : 'delta in the csv (grade ' + r.grade + ')', r.delta, READ, r.grade === 'measured' ? 'COORDINATES-2.13' : 'COORDINATES-2.13, grade ' + r.grade + ': not a measurement'),
      row('delta by equation, pinned set', inv.delta_equation, PINNED),
      row('residual under the pinned set (the debt on this channel)', inv.residual, DERIVED, 'measured - equation')
    ];
    if (!inv.solvable) {
      rows.push(row(inv.coefficient + ' solved', 'not solvable', undefined, inv.reason));
      rows.push(row(inv.coefficient + ' pinned', inv.pinned, PINNED, 'the channel equation, final form'));
      return rows;
    }
    if (inv.e_solved !== undefined) {
      rows.push(row('e solved (ln(d / (A Ne^K cf)) / ln p)', inv.e_solved, DERIVED));
      rows.push(row('e pinned (E0 - E1 ln Ne)', inv.e_pinned, PINNED));
    }
    rows.push(row(inv.coefficient + ' solved', inv.value, DERIVED, 'closed form, every other coefficient held pinned' + (inv.sign_note ? '; ' + inv.sign_note : '')));
    rows.push(row(inv.coefficient + ' pinned', inv.pinned, PINNED, 'the channel equation, final form'));
    rows.push(row('gap, absolute (solved - pinned)', inv.gap, DERIVED));
    rows.push(row('gap, relative', inv.gap_rel, DERIVED, 'gap / pinned'));
    rows.push(row('round trip: delta with the solved ' + inv.coefficient, inv.roundtrip_delta, DERIVED));
    rows.push(row('round trip error', inv.roundtrip_error, DERIVED, Math.abs(inv.roundtrip_error) <= 1e-9 ? 'reproduces the measured delta to 1e-9' : 'DOES NOT reproduce the measured delta'));
    return rows;
  }
  function atomRows(res, rec, coef) {
    var rows = [
      row('element', rec.symbol + ' (Z = ' + rec.Z + ')', READ),
      row('measured rows', res.n_measured, DERIVED, 'grade measured, in the record'),
      row('rows used, p > 0 (log-linear form)', res.usedP.length, DERIVED, 'distinct p ' + res.distinct_p.join(', ') + '; distinct Ne ' + res.distinct_Ne.join(', ')),
      row('rows used, p = 0 (ln H, K)', res.usedH.length, DERIVED),
      row('rows excluded', res.excluded.length, DERIVED, res.excluded.length ? res.excluded.map(function (x) { return x.row.label + ': ' + x.why; }).join('; ') : undefined),
      row('subset', res.subset, undefined)
    ];
    if (res.rank !== null) {
      rows.push(row('rank / determined unknowns', res.rank, DERIVED, 'degrees of freedom ' + res.dof));
      res.undetermined.forEach(function (u) { rows.push(row(u.coefficient + ' not determined', 'held pinned', PINNED, u.reason)); });
    }
    ['A', 'E0', 'E1', 'K'].forEach(function (k) {
      if (res.status[k] === DERIVED) {
        rows.push(row(k + ' solved', res.solved[k], DERIVED, 'pinned ' + coef[k] + '; gap ' + (res.solved[k] - coef[k]).toExponential(4) + (coef[k] ? ', relative ' + ((res.solved[k] - coef[k]) / coef[k]).toExponential(4) : '')));
      } else if (!res.undetermined.some(function (u) { return u.coefficient === k; }) &&
                 (res.subset === 'all' || res.subset === 'A and K' || (res.subset === 'A only' && k === 'A'))) {
        rows.push(row(k + ' held', coef[k], PINNED, 'not solved for in this subset'));
      }
    });
    if (res.subset === 'H only') {
      rows.push(row('H solved', res.solved.H, res.status.H, res.status.H === DERIVED ? 'pinned ' + coef.H + '; gap ' + (res.solved.H - coef.H).toExponential(4) : 'no usable p = 0 rows'));
    }
    if (res.rms_before !== null) {
      rows.push(row('rms of delta residuals, pinned set', res.rms_before, DERIVED, 'over the rows used'));
      rows.push(row('rms of delta residuals, solved set', res.rms_after, DERIVED, res.rms_after <= res.rms_before ? 'not above the pinned set' : 'ABOVE the pinned set: the log-form minimum is not the delta-form minimum here'));
    }
    if (res.log_rms_before !== null) {
      rows.push(row('rms of ln delta residuals, pinned / solved', fmt(res.log_rms_before, 6) + ' / ' + fmt(res.log_rms_after, 6), DERIVED, 'the quantity the log-form solve minimises'));
    }
    if (res.H) {
      rows.push(row('p = 0 rows: H solved', res.H.H, res.H.status_H, 'pinned ' + coef.H + '; gap ' + (res.H.H - coef.H).toExponential(4) + '; rank ' + res.H.rank + ', dof ' + res.H.dof));
      rows.push(row('p = 0 rows: K solved', res.H.K, res.H.status_K, 'pinned ' + coef.K + '; the p = 0 branch\'s own K, solved apart from the p > 0 branch\'s' + (res.status.K === DERIVED ? ' (' + res.solved.K.toFixed(6) + ')' : '')));
      res.H.undetermined.forEach(function (u) { rows.push(row('p = 0 rows: ' + u.coefficient + ' not determined', 'held pinned', PINNED, u.reason)); });
      if (res.H.dof === 0) rows.push(row('p = 0 rows: note', 'as many determined unknowns as rows (' + res.H.rank + '): the solve interpolates and every residual vanishes by construction; no evidence is left to test H and K'));
      rows.push(row('p = 0 rows: rms pinned / solved', res.H.rms_before.toFixed(6) + ' / ' + res.H.rms_after.toFixed(6), DERIVED));
    }
    res.notes.forEach(function (n) { rows.push(row('note', n)); });
    return rows;
  }
  function atomText(res) {
    if (!res.perRow.length) return 'no rows used';
    var out = [pad('channel', 14) + lpad('p', 3) + lpad('Ne', 4) + lpad('C', 7) + lpad('delta', 10) + lpad('eq pinned', 11) + lpad('resid', 10) + lpad('eq solved', 11) + lpad('resid', 10)];
    res.perRow.forEach(function (x) {
      var r = x.row;
      out.push(pad(r.label, 14) + lpad(r.p, 3) + lpad(r.Ne, 4) + lpad(r.C.toFixed(3), 7) + lpad(r.delta.toFixed(4), 10) +
               lpad(x.eq_pinned.toFixed(4), 11) + lpad(x.res_pinned.toFixed(4), 10) + lpad(x.eq_solved.toFixed(4), 11) + lpad(x.res_solved.toFixed(4), 10));
    });
    if (res.excluded.length) {
      out.push('');
      out.push('excluded:');
      res.excluded.forEach(function (x) { out.push('  ' + pad(x.row.label, 14) + ' delta ' + x.row.delta + '  ' + x.why); });
    }
    return out.join('\n');
  }
  function driftRows(res) {
    var rows = [
      row('coefficient', res.coefficient, undefined),
      row(res.coefficient + ' pinned', res.pinned, PINNED, 'the channel equation, final form'),
      row('measured channels in the index', res.n_rows, DERIVED, 'grade measured, over every populated element'),
      row('solvable', res.n_solvable, DERIVED, 'one measurement determines one unknown: every solved value is conditional on the other four staying pinned'),
      row('refused', res.n_refused, DERIVED, Object.keys(res.refused).map(function (k) { return res.refused[k] + ' x ' + k; }).join('; ') || undefined)
    ];
    if (res.n_solvable) {
      rows.push(row('min', res.min, DERIVED));
      rows.push(row('median', res.median, DERIVED));
      rows.push(row('max', res.max, DERIVED));
    }
    if (res.trend) {
      rows.push(row('trend: slope per unit Z', res.trend.slope, DERIVED, 'least-squares line of the solved value against Z, ' + res.trend.n + ' points'));
      rows.push(row('trend: intercept at Z = 0', res.trend.intercept, DERIVED));
      rows.push(row('trend: r', res.trend.r, DERIVED, 'Pearson correlation of solved value with Z; the drift, stated as arithmetic and nothing more'));
    } else rows.push(row('trend', 'not defined', undefined, 'fewer than two solvable channels'));
    return rows;
  }
  var MODE_COEFFICIENT = {
    id: 'coefficient',
    title: 'The coefficient calculator',
    status: DERIVED,
    statusNote: 'Engineered on the channel equation: the five pinned constants A, E0, E1, K (p > 0) and H, K (p = 0), solved back out of the READ deltas of COORDINATES-2.13\'s measured channels.',
    description: 'The author\'s brief: a coefficient is a guess that nobody returns to evaluate, and it leaves a debt; the more coefficients an equation carries, the more that debt compounds, and the result drifts; if the coefficient is instead evaluated and solved for each atom, nothing needs renormalising afterwards. This mode pays the debt in arithmetic. "invert" solves one coefficient exactly out of one measured channel with the other four held pinned, and shows the residual the pinned value left there. "atom" solves an element\'s whole set jointly from its measured rows, in the log form where the equation is linear, and says which coefficients the rows cannot separate. "drift" inverts one coefficient at every measured channel of the index and reports the trend against Z. Every refusal is a result: a channel where a coefficient has no effect cannot be solved for it.',
    inputs: [
      sel('Z'), sel('charge'), sel('l'), sel('mult'),
      { name: 'coefficient', label: 'coefficient', type: 'select', default: 'A',
        options: [{ value: 'A', label: 'A (p > 0 scale)' }, { value: 'E0', label: 'E0 (exponent, constant term)' },
                  { value: 'E1', label: 'E1 (exponent, ln Ne term)' }, { value: 'K', label: 'K (Ne^K, both branches)' },
                  { value: 'H', label: 'H (p = 0 scale)' }] },
      { name: 'operation', label: 'operation', type: 'select', default: 'invert',
        options: [{ value: 'invert', label: 'invert: one channel, one coefficient, closed form' },
                  { value: 'atom', label: 'atom: the element\'s set, jointly, least squares' },
                  { value: 'drift', label: 'drift: one coefficient at every measured channel (loads every element file)' }] },
      { name: 'subset', label: 'atom: unknowns', type: 'select', default: 'all',
        options: [{ value: 'all', label: 'all: A, E0, E1, K (and H, K on the p = 0 rows)' }, { value: 'A only', label: 'A only, closed form' },
                  { value: 'H only', label: 'H only, closed form' }, { value: 'A and K', label: 'A and K, log-linear' }],
        help: 'used by the atom operation' }
    ],
    source: { instrument: 'channel_delta', file: 'tools/populate.py' },
    loadsAll: 'The drift operation and the selftest',
    run: async function (values, ctx) {
      var op = values.operation || 'invert', name = values.coefficient || 'A';
      if (COEF_NAMES.indexOf(name) < 0) return fail('coefficient must be one of ' + COEF_NAMES.join(', '));
      var coef = coefficients(ctx.index), params = collapseParams(ctx.index);
      if (op === 'drift') {
        var la = await ctx.loadAll();
        var rowsAll = measuredRowsAll(la.records.filter(function (r) { return r && r.populated; }), params);
        var res = drift(rowsAll, name, coef);
        var rows = driftRows(res);
        if (la.failed.length) rows.push(row('elements not loaded', la.failed.join(', '), undefined, la.failed.length + ' element file(s) could not be loaded; the drift is over the ' + la.records.length + ' that were'));
        rows.push(row('note', 'every solved value is exact for its own channel and conditional on the other four coefficients staying pinned: a single measurement determines a single unknown. ' + coef.note));
        var text = res.series.map(function (s) { return pad(s.label, 14) + lpad(s.y.toFixed(6), 12) + '   residual under pinned ' + s.residual.toFixed(4); }).join('\n');
        return { rows: rows, ok: true, series: res.series.map(function (s) { return { x: s.x, y: s.y, label: s.label }; }),
                 seriesLabel: name + ' solved per measured channel, by Z (pinned ' + coef[name] + ')', text: text };
      }
      var Z = int(values.Z);
      var got = await elementOrFail(ctx, Z);
      if (got.fail) return got.fail;
      var rec = got.rec;
      if (op === 'atom') {
        var subset = values.subset || 'all';
        if (['all', 'A only', 'H only', 'A and K'].indexOf(subset) < 0) return fail('subset must be all, A only, H only or A and K');
        var rowsEl = channelRows(rec, params, true);
        if (!rowsEl.length) return fail(rec.symbol + ' has no measured rows in the index; nothing to solve against');
        var ares = atomSolve(rowsEl, coef, subset);
        var arows = atomRows(ares, rec, coef);
        if (coef.fallback.length) arows.push(row('coefficients', coef.note, PINNED));
        return { rows: arows, ok: true, text: atomText(ares) };
      }
      var charge = int(values.charge), l = int(values.l), mult = int(values.mult);
      if (charge === null || l === null) return fail('charge and l must be integers');
      if (charge < 1 || charge > Z) return fail('stage must be 1 to ' + Z);
      var pk = pickRow(rec, charge, l, mult, params);
      if (pk.fail) return pk.fail;
      var inv = invertCoefficient(pk.row, name, coef);
      var irows = invertRows(inv, pk.row);
      if (coef.fallback.length) irows.push(row('coefficients', coef.note, PINNED));
      return { rows: irows, ok: true };
    },
    selftest: async function (ctx) {
      var ck = new Checker();
      var la = await ctx.loadAll();
      var all = la.records.filter(function (r) { return r && r.populated; });
      ck.ok('every element file loaded (' + la.records.length + ' of ' + (la.records.length + la.failed.length) + ')', la.failed.length === 0, la.failed.join(', ') || 0, 0);
      var coef = coefficients(ctx.index), params = collapseParams(ctx.index);
      checkEquationPort(ck, all, ctx, 'all elements');
      checkHydrogenic(ck, ctx);
      var rows = measuredRowsFrom(all, ctx);
      ck.eq('measured rows across all populated elements: 358', rows.length, (ctx.index && ctx.index.totals && ctx.index.totals.measured) || 358);
      checkEquationReport(ck, rows, ctx);
      // exported residuals agree with measured - port
      var badRes = 0;
      rows.forEach(function (r) { if (!(Math.abs((r.delta - channelDelta(r.p, r.Ne, r.charge, r.C, coef)) - r.residual_exported) <= 1e-9)) badRes += 1; });
      ck.ok('exported residuals reproduced to 1e-9 on every measured row', badRes === 0, badRes, 0);
      // invert: round trip on every measured row, every solvable coefficient
      var solvable = {}, refused = {}, bad = 0, worst = 0, first = null, nInv = 0;
      COEF_NAMES.forEach(function (k) { solvable[k] = 0; });
      rows.forEach(function (r) {
        COEF_NAMES.forEach(function (k) {
          var inv = invertCoefficient(r, k, coef);
          if (!inv.solvable) { var key = k + ': ' + inv.code; refused[key] = (refused[key] || 0) + 1; return; }
          nInv += 1; solvable[k] += 1;
          var err = Math.abs(inv.roundtrip_error);
          if (err > worst) worst = err;
          if (!(err <= 1e-9)) { bad += 1; if (!first) first = { row: r.label, coefficient: k, error: err }; }
        });
      });
      ck.ok('invert: every solvable (row, coefficient) round-trips to the measured delta within 1e-9 (' + nInv + ' inversions over ' + rows.length + ' rows)', bad === 0, first || bad, 0);
      ck.notes.push('invert: solvable per coefficient ' + COEF_NAMES.map(function (k) { return k + ' ' + solvable[k]; }).join(', ') + '; worst round-trip error ' + worst.toExponential(3));
      ck.notes.push('invert: refusals ' + Object.keys(refused).sort().map(function (k) { return refused[k] + ' x ' + k; }).join('; '));
      // a non-measured row is refused
      var nonMeas = null;
      for (var i = 0; i < all.length && !nonMeas; i++) {
        var cr = channelRows(all[i], params, false);
        for (var j = 0; j < cr.length; j++) if (cr[j].grade !== 'measured') { nonMeas = cr[j]; break; }
      }
      if (nonMeas) ck.eq('invert refuses a row whose grade is not measured', invertCoefficient(nonMeas, 'A', coef).solvable, false);
      // the p = 1 refusal and the Ne = 1 refusal
      var p1 = rows.filter(function (r) { return r.p === 1; })[0], ne1 = rows.filter(function (r) { return r.Ne === 1; })[0];
      if (p1) ck.eq('invert refuses E0 at p = 1 (' + p1.label + ')', invertCoefficient(p1, 'E0', coef).solvable, false);
      if (ne1) ck.eq('invert refuses everything at Ne = 1 (' + ne1.label + ')', COEF_NAMES.map(function (k) { return invertCoefficient(ne1, k, coef).solvable; }), [false, false, false, false, false]);
      // atom: Fe
      var fe = all.filter(function (r) { return r.Z === 26; })[0];
      if (fe) {
        // Fe's four p > 0 rows determine four unknowns: an interpolation, dof 0, every residual
        // vanishing by construction -- asserted as such, not as a fit that lowered anything
        var feRes = atomSolve(channelRows(fe, params, true), coef, 'all');
        ck.eq('atom (Fe, all): rank 4 over 4 rows, dof 0 -- an interpolation, not a test', [feRes.rank, feRes.dof], [4, 0]);
        ck.ok('atom (Fe, all): the interpolation reproduces every row (rms after < 1e-9)', feRes.rms_after !== null && feRes.rms_after < 1e-9, feRes.rms_after, 0);
        ck.notes.push('atom Fe: ' + feRes.usedP.length + ' p > 0 rows, rank ' + feRes.rank + ', dof ' + feRes.dof + ', rms ' + fmt(feRes.rms_before, 4) + ' -> ' + fmt(feRes.rms_after, 4) +
                      '; A ' + fmt(feRes.solved.A, 4) + ' E0 ' + fmt(feRes.solved.E0, 4) + ' E1 ' + fmt(feRes.solved.E1, 4) + ' K ' + fmt(feRes.solved.K, 4));
        // an element with dof > 0: the log-form residual, the quantity minimised, is not above the pinned set's
        var over = null;
        for (var q = 0; q < all.length && !over; q++) {
          var rq = channelRows(all[q], params, true);
          if (!rq.length) continue;
          var sq = atomSolve(rq, coef, 'all');
          if (sq.rank === 4 && sq.dof > 0) over = { rec: all[q], res: sq };
        }
        if (over) {
          ck.ok('atom (' + over.rec.symbol + ', all, rank 4, dof ' + over.res.dof + '): ln-delta rms after <= before', over.res.log_rms_after <= over.res.log_rms_before + 1e-12, [over.res.log_rms_before, over.res.log_rms_after]);
          ck.notes.push('atom ' + over.rec.symbol + ': ' + over.res.usedP.length + ' p > 0 rows, dof ' + over.res.dof + ', ln-delta rms ' + fmt(over.res.log_rms_before, 4) + ' -> ' + fmt(over.res.log_rms_after, 4) +
                        ', delta rms ' + fmt(over.res.rms_before, 4) + ' -> ' + fmt(over.res.rms_after, 4));
        } else ck.ok('an element with rank 4 and dof > 0 exists for the overdetermined check', false, 'none', 'one');
        var feAK = atomSolve(channelRows(fe, params, true), coef, 'A and K');
        ck.ok('atom (Fe, A and K): rms after <= rms before', feAK.rms_after <= feAK.rms_before, [feAK.rms_before, feAK.rms_after]);
        var feA = atomSolve(channelRows(fe, params, true), coef, 'A only');
        ck.ok('atom (Fe, A only): closed form lowers or keeps the delta rms', feA.rms_after <= feA.rms_before + 1e-12, [feA.rms_before, feA.rms_after]);
      } else ck.ok('Fe loaded for the atom check', false, 'not loaded', 'loaded');
      // atom: every element with measured rows, count outcomes (recorded, not asserted, since the log-form minimum need not be the delta-form minimum)
      var nAt = 0, nDown = 0, nUp = [];
      all.forEach(function (rec) {
        var rr = channelRows(rec, params, true);
        if (!rr.length) return;
        var res = atomSolve(rr, coef, 'all');
        if (res.rms_before === null) return;
        nAt += 1;
        if (res.rms_after <= res.rms_before + 1e-12) nDown += 1; else nUp.push(rec.symbol + ' ' + res.rms_before.toFixed(4) + '->' + res.rms_after.toFixed(4));
      });
      ck.notes.push('atom over every element with usable rows: ' + nAt + ' solved, delta rms not above the pinned set in ' + nDown + (nUp.length ? '; above in ' + nUp.join(', ') : ''));
      // rank detection: a synthetic set where all rows share p must leave E0 and E1 undetermined
      var syn = rows.filter(function (r) { return r.p === 2 && r.delta > 0; }).slice(0, 6);
      if (syn.length >= 3) {
        var sres = atomSolve(syn, coef, 'all');
        var und = sres.undetermined.map(function (u) { return u.coefficient; }).sort();
        ck.eq('atom: rows sharing one p leave E0 and E1 undetermined (held pinned)', und, ['E0', 'E1']);
      }
      // drift: A over every channel agrees with the per-row inversion count
      var dr = drift(rows, 'A', coef);
      ck.eq('drift A: solvable count = invert\'s count', dr.n_solvable, solvable.A);
      ck.eq('drift A: solvable + refused = rows', dr.n_solvable + dr.n_refused, rows.length);
      if (dr.trend) ck.notes.push('drift A: slope ' + dr.trend.slope.toExponential(3) + ' per Z, r ' + dr.trend.r.toFixed(3) + ', median ' + dr.median.toFixed(4) + ' against pinned ' + coef.A);
      return ck.result();
    }
  };


  // 7. relativistic ---------------------------------------------------------
  // Nothing here is computed. The scalar-relativistic construction (Koelling-Harmon
  // Hartree-Fock at c = 137) and its repetition at c -> inf are not held; what is held
  // is the paper's own result and the SCF audit's table, all READ.
  var MODE_RELATIVISTIC = {
    id: 'relativistic',
    title: 'The relativistic limit (c = 137 against c → ∞)',
    status: READ,
    statusNote: 'The Löwdin paper: the observed table is irreducibly relativistic. The record\'s construction is not held: the Löwdin project\'s reply of 2026-09-18 locates the c → ∞ path in a delivery that never arrived, and the project has since concluded. So the mode reads the record\'s result (READ) and, beside it, carries a RECONSTRUCTION: tools/lowdin_walk.py runs the record\'s own algorithm — the V^{N−1} chain with the Koelling–Harmon equation — in a local-exchange field, at both settings, into LOWDIN-WALK.tsv. The reconstruction is never the record\'s number; where the two disagree, the disagreement is the measurement.',
    description: 'Quantum mechanics supplies the range of configurations; the speed of light, entering once as c = 137 through the scalar-relativistic reduction of the Dirac equation, decides which of them the observed table holds. Repeated with c sent to infinity, the record\'s construction misplaces eleven elements and inverts the channel competition at thorium. That construction is not held, so this mode reports the paper\'s own result, READ, and refuses to recompute its c → ∞ table. What it can show beside the record is the reconstructed walk (RECONSTRUCTED): the same chain, run here in a field that is not the record\'s, with its entrant, runner-up, margin and candidate spectrum at every Z at both settings, and the reconstruction\'s own list of displaced elements measured against the Löwdin paper\'s eleven.',
    inputs: [sel('Z'),
             { name: 'operation', label: 'operation', type: 'select', default: 'element',
               options: [{ value: 'element', label: 'is this element displaced at c → ∞? (the record)' },
                         { value: 'walk', label: 'this element in the reconstructed walk, both settings' },
                         { value: 'eleven', label: 'the eleven, with their entrant channels (the record)' },
                         { value: 'compare', label: 'the reconstruction against the record' },
                         { value: 'recompute', label: 'recompute the c → ∞ table' }] }],
    source: { instrument: 'lowdin_construction', file: 'the Löwdin paper',
              also: ['walk_scan_hf', 'walk_scf_hf', 'walk_hf_operator', 'walk_solve_inh', 'walk_scan', 'walk_frontier', 'walk_solve', 'walk_integrate', 'walk_potentials', 'walk_scf'] },
    run: async function (values, ctx) {
      var rel = ctx.index && ctx.index.relativistic;
      if (!rel) return fail('this build of data/index.js carries no relativistic block (run python3 tools/webindex.py)');
      var op = values.operation || 'element', rows = [];
      var src = rel.sources || {}, paper = src.paper || {};
      var cite = (paper.title || 'the Löwdin paper') + ' L' + paper.eleven_line + '; the SCF audit';
      var inst = rel.instrument || {};
      var walk = rel.walk;
      var wcite = walk ? walk.instrument + ' over ' + walk.table.file + ' (md5 ' + walk.table.md5.slice(0, 12) + ')' : '';
      var fmt6 = function (v) { return (v === null || v === undefined) ? '—' : v.toFixed(6); };
      if (op === 'recompute') {
        rows.push(row('c → ∞ table', 'not computable here', null, inst.note || 'the construction is not held'));
        rows.push(row('why', 'the record\'s scalar-relativistic construction (Koelling–Harmon Hartree–Fock, c = 137) and its repetition at c → ∞ are not held; the delivery that would have carried them never arrived', null, inst.note || ''));
        rows.push(row('what is held', 'the paper\'s statement and the SCF audit\'s table of the eleven', READ, cite));
        if (walk && walk.summary && walk.summary.compare) {
          var cp = walk.summary.compare;
          rows.push(row('the walk, reconstructed', 'a c → ∞ table exists here as a reconstruction, not the record\'s: Z = ' + cp.Z_first + ' to ' + cp.Z_last + ' at both settings, in ' + Object.keys(walk.fields || { lx: 1 }).length + ' field(s); the primary is ' + (walk.primary || 'lx'), RECONSTRUCTED, wcite));
          rows.push(row('field (primary)', walk.field, RECONSTRUCTED, 'what the reconstruction is; not reproduced: ' + walk.not_reproduced));
          rows.push(row('displaced in the reconstruction', cp.displaced.length ? cp.displaced.map(function (d) { return d.symbol + ' (' + d.entrant_c137 + ' | ' + d.entrant_cinf + ')'; }).join(', ') : 'none', RECONSTRUCTED, 'entrants that differ between c = 137.035999 and c → ∞'));
          rows.push(row('against the record\'s eleven', cp.in_eleven.length + ' displaced here too' + (cp.in_eleven.length ? ' (' + cp.in_eleven.join(', ') + ')' : '') + '; ' + cp.eleven_not_displaced.length + ' not' + (cp.eleven_not_displaced.length ? ' (' + cp.eleven_not_displaced.join(', ') + ')' : '') + '; ' + cp.not_in_eleven.length + ' displaced here and not in the record' + (cp.not_in_eleven.length ? ' (' + cp.not_in_eleven.join(', ') + ')' : ''), RECONSTRUCTED, 'the Löwdin paper\'s eleven against ' + walk.table.file));
          if (cp.thorium) rows.push(row('thorium, the null-difference control', cp.thorium.entrant_c137 + ' at c = 137.035999, ' + cp.thorium.entrant_cinf + ' at c → ∞ — ' + (cp.thorium.identical ? 'identical' : 'different'), RECONSTRUCTED, 'the record: the entrant survives by path and the competition inverts'));
        }
        return { rows: rows, ok: true, text: rel.statement || '' };
      }
      if (op === 'compare') {
        if (!walk || !walk.summary) return fail('no reconstructed walk in this build of data/index.js (LOWDIN-WALK.tsv was absent when webindex.py ran)');
        var sm = walk.summary, cmp = sm.compare;
        rows.push(row('instrument', walk.instrument + ' → ' + walk.table.file + ', ' + walk.table.rows + ' rows; fields ' + Object.keys(walk.fields || { lx: 1 }).join(', ') + '; primary ' + (walk.primary || 'lx'), RECONSTRUCTED, wcite));
        Object.keys(walk.fields || {}).forEach(function (fld) { rows.push(row('field ' + fld, walk.fields[fld].name, RECONSTRUCTED, 'not reproduced: ' + walk.fields[fld].not_reproduced)); });
        Object.keys(sm.settings).sort().forEach(function (key) {
          var s = sm.settings[key], lab = 'field ' + (s.field || key.split(':')[0]) + ', c = ' + ((s.c || key.split(':')[1]) === 'inf' ? '∞' : (s.c || key.split(':')[1]));
          rows.push(row(lab + ': openings', s.openings.map(function (o) { return o.channel + '@' + o.Z; }).join(' '), RECONSTRUCTED, 'first Z at which each channel is the entrant; observed: ' + s.openings_observed.map(function (o) { return o.channel + '@' + o.Z; }).join(' ')));
          rows.push(row(lab + ': same order as observed', s.same_order ? 'yes' : 'no', RECONSTRUCTED, 'over the channels both sequences open' + (s.openings_displaced.length ? '; at a different Z: ' + s.openings_displaced.map(function (o) { return o.channel + ' ' + o.Z + '≠' + o.observed_Z; }).join(', ') : '')));
          rows.push(row(lab + ': clause 1 violations / clause 2 exceptions', s.clause1_violations.length + ' / ' + s.clause2_exceptions.length + (s.clause2_exceptions.length ? ' (' + s.clause2_exceptions.join('; ') + ')' : ''), RECONSTRUCTED, 'the record: 0 violations, exceptions exactly La, Ac, Th'));
          rows.push(row(lab + ': entrant = observed gain', s.agree + ' of ' + s.scored, RECONSTRUCTED, 'differentiating-electron reading over the observed configurations; disagreements: ' + (s.disagree.map(function (d) { return d.symbol + '(' + d.entrant + '≠' + d.observed_gain + ')'; }).join(' ') || 'none')));
          rows.push(row(lab + ': chain configuration identical to observed', s.cfg_identical + ' of ' + Math.min(s.rows, 107), RECONSTRUCTED, 'the chain never moves an electron'));
          rows.push(row(lab + ': g channels', s.g_pins.map(function (g) { return g.channel + ' offered at ' + g.offered + ', max |D + 1/(2n²)| ' + g.max_dev.toExponential(2); }).join('; '), RECONSTRUCTED, 'the record: 5g 65, 6g 70, 7g 57, 8g 28 elements, −1/(2n²) to storage precision'));
          rows.push(row(lab + ': smallest margins', s.smallest_margins.map(function (m) { return m.symbol + ' ' + m.entrant + ' over ' + m.runner_up + ' by ' + fmt6(m.margin); }).join('; '), RECONSTRUCTED, 'the record\'s contested rows: Z = 38, 56, 72, 89, 105'));
          if (s.not_converged.length) rows.push(row(lab + ': NOT CONVERGED', s.not_converged.join(' '), RECONSTRUCTED, 'rows whose field did not converge'));
        });
        var fieldsCmp = sm.fields || (cmp ? { lx: cmp } : {});
        Object.keys(fieldsCmp).sort().forEach(function (fld) {
          var c = fieldsCmp[fld], pre = 'field ' + fld + ': ';
          rows.push(row(pre + 'displaced at c → ∞', c.displaced.length ? c.displaced.map(function (d) { return d.symbol + ' (' + d.entrant_c137 + ' | ' + d.entrant_cinf + ')'; }).join(', ') : 'none', RECONSTRUCTED, 'entrants differ between the two settings'));
          rows.push(row(pre + 'the record\'s eleven', c.eleven.join(', '), READ, 'the Löwdin paper'));
          rows.push(row(pre + 'of the eleven, displaced here too', c.in_eleven.length + (c.in_eleven.length ? ': ' + c.in_eleven.join(', ') : ''), RECONSTRUCTED, ''));
          rows.push(row(pre + 'of the eleven, not displaced here', c.eleven_not_displaced.length + (c.eleven_not_displaced.length ? ': ' + c.eleven_not_displaced.join(', ') : ''), RECONSTRUCTED, ''));
          rows.push(row(pre + 'displaced here, not in the record', c.not_in_eleven.length + (c.not_in_eleven.length ? ': ' + c.not_in_eleven.join(', ') : ''), RECONSTRUCTED, ''));
          if (c.thorium) rows.push(row(pre + 'thorium, the null-difference control', c.thorium.entrant_c137 + ' at c = 137.035999, ' + c.thorium.entrant_cinf + ' at c → ∞ — ' + (c.thorium.identical ? 'identical' : 'different') + '; top three: ' + c.thorium.top3_c137.join(' ') + ' | ' + c.thorium.top3_cinf.join(' '), RECONSTRUCTED, 'the record: the entrant survives by path, the competition inverts'));
          (c.named_rows || []).forEach(function (nr) { rows.push(row(pre + nr.symbol + ' (' + nr.Z + ') top three', nr.top3_c137.join(' ') + '  |  ' + nr.top3_cinf.join(' '), RECONSTRUCTED, 'c = 137.035999 | c → ∞')); });
        });
        if (sm.fields_compare) rows.push(row('the two fields at c = 137.035999', sm.fields_compare.entrants_differ.length ? sm.fields_compare.entrants_differ.map(function (d) { return d.symbol + ' (lx ' + d.lx + ' | hf ' + d.hf + ')'; }).join(', ') : 'no entrant differs', RECONSTRUCTED, 'local exchange against Hartree–Fock over ' + sm.fields_compare.rows + ' rows'));
        return { rows: rows, ok: true, text: caveat(ctx.index, 'walk-reconstructed') || '' };
      }
      if (op === 'walk') {
        if (!walk) return fail('no reconstructed walk in this build of data/index.js (LOWDIN-WALK.tsv was absent when webindex.py ran)');
        var Zw = int(values.Z);
        if (Zw === null || Zw < 1 || Zw > 120) return fail('Z must be an integer from 1 to 120');
        var recw = ctx.element(Zw) || await ctx.load(Zw);
        if (!recw) return fail('no record for Z = ' + Zw);
        var wr = recw.walk;
        if (!wr || !wr.fields) return fail('the walk has no row at Z = ' + Zw + ' (it runs Z = 2 to 120)');
        rows.push(row('element', recw.symbol + ' (Z = ' + Zw + ')', READ, 'the observed configurations table'));
        var order = [walk.primary].concat(Object.keys(wr.fields).filter(function (k) { return k !== walk.primary; }));
        order.forEach(function (fld) {
          var wf = wr.fields[fld]; if (!wf) return;
          rows.push(row('field ' + fld, WALK_FIELD_LABEL[fld] || fld, RECONSTRUCTED, ((walk.fields || {})[fld] || {}).name || ''));
          ['c137', 'cinf'].forEach(function (k) {
            var r = wf[k]; if (!r) return;
            var lab = fld + ', c = ' + (k === 'cinf' ? '∞' : '137.035999');
            rows.push(row(lab + ': entrant', r.entrant, RECONSTRUCTED, 'deepest candidate of one electron in the frozen field of (Z = ' + Zw + ', ' + r.cfg_prev + ')'));
            rows.push(row(lab + ': depth D', fmt6(r.D_ent) + ' Ha', RECONSTRUCTED, 'the eigenvalue of the added electron in the frozen ' + (fld === 'hf' ? 'Hartree–Fock' : 'local-exchange') + ' field; asymptote −1/r'));
            rows.push(row(lab + ': runner-up, margin', r.runner_up + ', ' + fmt6(r.margin) + ' Ha', RECONSTRUCTED, '|D(entrant)| − |D(runner-up)|'));
            rows.push(row(lab + ': candidates', r.spectrum.map(function (x) { return x.channel + ' ' + x.D.toFixed(5); }).join('  '), RECONSTRUCTED, 'every unfilled channel to 8s and 8g that binds, deepest first'));
            rows.push(row(lab + ': scf', r.scf_iterations + ' iterations, ' + (r.converged ? 'converged' : 'NOT CONVERGED'), RECONSTRUCTED, fld === 'hf' ? 'sweeps to 1e-7 in the eigenvalues and orbitals' : 'mixed to 1e-7 in r·V'));
          });
          rows.push(row(fld + ': displaced', wf.displaced ? 'yes' : 'no', RECONSTRUCTED, 'the two settings\' entrants differ in this field, or not'));
        });
        var prim = wr.fields[walk.primary] || wr.fields[order[0]];
        if (prim && prim.c137 && prim.c137.observed_gain !== '-') rows.push(row('observed gain at this Z', prim.c137.observed_gain + ' — the primary field\'s c = 137 entrant ' + (prim.c137.agree === 'yes' ? 'agrees' : 'differs'), READ, 'the observed configurations table: the channel that gained an electron from Z − 1 to Z; the chain never moves an electron'));
        var inEleven = rel.eleven.some(function (e) { return e.Z === Zw; });
        rows.push(row('in the record', inEleven ? 'one of the eleven the Löwdin paper displaces' : 'not among the eleven', READ, cite));
        return { rows: rows, ok: true, walk: wr, primary: walk.primary, text: caveat(ctx.index, 'walk-reconstructed') || '' };
      }
      if (op === 'eleven') {
        rows.push(row('elements displaced at c → ∞', rel.eleven.length, READ, cite));
        rel.eleven.forEach(function (e) {
          rows.push(row(e.symbol + ' (Z = ' + e.Z + ')', (e.configuration || '') + ' → entrant ' + (e.entrant || '?'), READ, 'the SCF audit: the eleven in the observed table, over the observed configurations'));
        });
        if (rel.thorium) rows.push(row('thorium', rel.thorium, READ, (paper.title || 'the Löwdin paper') + ' L' + paper.thorium_line));
        rows.push(row('instrument', 'not held — nothing computed here', null, inst.note || ''));
        return { rows: rows, ok: true, text: 'The Löwdin paper: ' + ((src.paper && src.paper.eleven_text) || '') };
      }
      var Z = int(values.Z);
      if (Z === null || Z < 1 || Z > 120) return fail('Z must be an integer from 1 to 120');
      var got = await elementOrFail(ctx, Z);
      if (got.fail) return got.fail;
      var rec = got.rec, hit = null;
      for (var i = 0; i < rel.eleven.length; i++) if (rel.eleven[i].Z === Z) hit = rel.eleven[i];
      rows.push(row('element', rec.symbol + ' (Z = ' + Z + ')', READ, 'the observed configurations table'));
      rows.push(row('displaced at c → ∞', hit ? 'yes' : 'no', READ, cite + (hit ? '' : ': not among the eleven')));
      if (hit) {
        rows.push(row('observed configuration', hit.configuration || '—', READ, 'the SCF audit over the observed configurations table'));
        rows.push(row('entrant channel', hit.entrant || '—', READ, 'the SCF audit: the channel the relativistic walk enters at this Z'));
      }
      if (Z === 90 && rel.thorium) rows.push(row('thorium', rel.thorium, READ, (paper.title || 'the Löwdin paper') + ' L' + paper.thorium_line));
      if (!rec.populated) rows.push(row('note', 'above Z = 108 the construction\'s 107-row table does not reach; the record carries csv rows only', null));
      rows.push(row('c', rel.c, READ, rel.construction || 'the one admitted constant'));
      rows.push(row('instrument', 'not held — nothing computed here', null, inst.note || ''));
      return { rows: rows, ok: true, text: rel.statement || '' };
    },
    selftest: async function (ctx) {
      var ck = new Checker();
      var rel = ctx.index && ctx.index.relativistic;
      ck.ok('data/index.js carries the relativistic block', !!rel, !!rel, true);
      if (!rel) return ck.result();
      ck.eq('eleven elements READ from the paper', rel.eleven.length, 11);
      var lay = (ctx.index.layout || []).filter(function (e) { return e.relativistic; });
      ck.eq('layout flags exactly the eleven', lay.length, 11);
      var byZ = function (a, b) { return a - b; };
      ck.eq('the flagged Z are the eleven', lay.map(function (e) { return e.Z; }).sort(byZ).join(','), rel.eleven.map(function (e) { return e.Z; }).sort(byZ).join(','));
      ck.ok('every one of the eleven carries an entrant channel', rel.eleven.every(function (e) { return !!e.entrant; }), rel.eleven.filter(function (e) { return !e.entrant; }).length, 0);
      ck.eq('Th (90) is not among the eleven', rel.eleven.some(function (e) { return e.Z === 90; }), false);
      ck.ok('the thorium inversion sentence is carried', !!rel.thorium, !!rel.thorium, true);
      ck.eq('instrument recorded as not held', !!(rel.instrument && rel.instrument.held), false);
      var r1 = await MODE_RELATIVISTIC.run({ Z: 47, operation: 'element' }, ctx);
      ck.eq('Ag: displaced at c → ∞ = yes', r1.ok ? r1.rows[1].value : r1.message, 'yes');
      var r2 = await MODE_RELATIVISTIC.run({ Z: 26, operation: 'element' }, ctx);
      ck.eq('Fe: displaced at c → ∞ = no', r2.ok ? r2.rows[1].value : r2.message, 'no');
      // Both directions, as the Löwdin project's reply of 2026-09-18 recommends: Hg is displaced,
      // Th is a collapse-criterion row and the null-difference control. A c switch
      // that displaced everything would pass a displacement-only test; Th is what catches it.
      var r4 = await MODE_RELATIVISTIC.run({ Z: 80, operation: 'element' }, ctx);
      ck.eq('Hg: displaced at c → ∞ = yes (displacement direction)', r4.ok ? r4.rows[1].value : r4.message, 'yes');
      var r5 = await MODE_RELATIVISTIC.run({ Z: 90, operation: 'element' }, ctx);
      ck.eq('Th: displaced at c → ∞ = no (the null-difference control)', r5.ok ? r5.rows[1].value : r5.message, 'no');
      ck.ok('Th carries the thorium inversion sentence, not a displacement', r5.ok && r5.rows.some(function (r) { return r.label === 'thorium'; }), r5.ok, true);
      var r3 = await MODE_RELATIVISTIC.run({ Z: 47, operation: 'recompute' }, ctx);
      ck.eq('recompute refuses and prints no number', r3.ok ? r3.rows[0].value : r3.message, 'not computable here');
      var noNumber = r3.ok && r3.rows.every(function (r) { return typeof r.value !== 'number'; });
      ck.ok('recompute rows carry no numeric value', noNumber, noNumber, true);
      var figs = ctx.index.figures || [];
      ck.ok('Figure 5 is carried with the md5 the ledger records', figs.length > 0 && figs.every(function (f) { return f.ok; }), figs.length, 1);
      // the reconstruction beside the record: carried, consistent between index.js and the
      // element files, and never flattened to the record's status
      var walk = rel.walk;
      ck.ok('the reconstructed walk is carried (LOWDIN-WALK.tsv read by webindex.py)', !!walk, !!walk, true);
      if (walk) {
        ck.eq('walk status is RECONSTRUCTED', walk.status, RECONSTRUCTED);
        var ents = walk.entrants || [];
        ck.eq('walk carries one entrant row per Z, 2 to 120', ents.length, 119);
        ck.ok('every walk row carries both settings', ents.every(function (e) { return e.c137 && e.cinf; }), ents.filter(function (e) { return !(e.c137 && e.cinf); }).length, 0);
        var cp = walk.summary.compare;
        var disp = ents.filter(function (e) { return e.displaced; }).map(function (e) { return e.symbol; });
        ck.eq('displaced set recounted from the entrants equals the summary\'s', disp.join(','), cp.displaced.map(function (d) { return d.symbol; }).join(','));
        ck.eq('the summary\'s eleven are the paper\'s eleven, in order', cp.eleven.join(','), rel.eleven.map(function (e) { return e.symbol; }).join(','));
        var layw = (ctx.index.layout || []).filter(function (e) { return e.walk_displaced; }).map(function (e) { return e.symbol; }).sort();
        ck.eq('layout flags exactly the reconstruction\'s displaced', layw.join(','), disp.slice().sort().join(','));
        var prim = walk.primary || 'lx';
        ck.ok('the primary field is hf when held', !walk.fields || !walk.fields.hf || prim === 'hf', prim, 'hf');
        Object.keys(walk.fields || {}).forEach(function (fld) {
          ck.eq('field ' + fld + ' carries one entrant row per Z', (walk.fields[fld].entrants || []).length, 119);
        });
        var w47 = await MODE_RELATIVISTIC.run({ Z: 47, operation: 'walk' }, ctx);
        var e47 = ents.filter(function (e) { return e.Z === 47; })[0];
        var f47 = w47.ok ? w47.walk.fields[prim] : null;
        ck.eq('Ag walk row: the element file\'s primary-field entrant at c = 137 is the index\'s', f47 ? f47.c137.entrant : w47.message, e47.c137);
        ck.eq('Ag walk row: the element file\'s primary-field entrant at c → ∞ is the index\'s', f47 ? f47.cinf.entrant : w47.message, e47.cinf);
        var w90 = await MODE_RELATIVISTIC.run({ Z: 90, operation: 'walk' }, ctx);
        var f90 = w90.ok ? w90.walk.fields[prim] : null;
        ck.eq('Th: the two entrants ' + (cp.thorium && cp.thorium.identical ? 'identical' : 'different') + ' in the element file, as the summary states', f90 ? (f90.c137.entrant === f90.cinf.entrant) : w90.message, !!(cp.thorium && cp.thorium.identical));
        var w120 = await MODE_RELATIVISTIC.run({ Z: 120, operation: 'walk' }, ctx);
        ck.ok('Z = 120 carries walk rows though it is not populated', w120.ok, w120.ok, true);
        var rc = await MODE_RELATIVISTIC.run({ Z: 47, operation: 'recompute' }, ctx);
        ck.ok('recompute still refuses the record\'s table and names the reconstruction beside it', rc.ok && rc.rows[0].value === 'not computable here' && rc.rows.some(function (r) { return r.status === RECONSTRUCTED; }), rc.ok, true);
        var cmpr = await MODE_RELATIVISTIC.run({ operation: 'compare' }, ctx);
        ck.ok('compare reports every row as RECONSTRUCTED or READ, never bare', cmpr.ok && cmpr.rows.every(function (r) { return r.status === RECONSTRUCTED || r.status === READ; }), cmpr.ok, true);
        ck.notes.push('reconstruction beside the record (' + prim + ' field primary): ' + cp.displaced.length + ' displaced at c → ∞, ' + cp.in_eleven.length + ' of the record\'s eleven; the record\'s own table stays not held');
      }
      ck.notes.push('nothing of the record\'s is computed: its construction is not held; ' + rel.eleven.length + ' elements READ');
      return ck.result();
    }
  };

  // 8. the muon energy balance ----------------------------------------------
  // tools/mucf.py's model over its three free axes, ported term for term; every input carries
  // the paper's own status and the result the weakest of them, REFUSED below the kinematic
  // floor. The fixtures are the paper's Table 5.1 and section 5.1 thresholds, read from the
  // instrument at build (index.particles.muon.instrument.fixtures), never typed here.
  function mucfConsts(ctx) {
    var pt = ctx.index && ctx.index.particles;
    return pt && pt.muon && pt.muon.instrument ? pt.muon.instrument.constants : null;
  }
  function mucfCycles(k, omega_s, phi, lambda_c) { lambda_c = lambda_c === undefined ? k.lambda_c : lambda_c; return phi * lambda_c / (k.lambda_0 + omega_s * phi * lambda_c); }
  function mucfGain(k, omega_s, phi, e_mu, lambda_c) { return mucfCycles(k, omega_s, phi, lambda_c) * k.Q_fus_MeV / (e_mu * 1000.0); }
  function mucfEmuFor(k, omega_s, phi, target, lambda_c) { return mucfCycles(k, omega_s, phi, lambda_c) * k.Q_fus_MeV / (target * 1000.0); }
  function mucfEmuForWork(k, omega_s, phi, target, lambda_c) { return mucfEmuFor(k, omega_s, phi, target, lambda_c) * k.f_work; }
  function mucfStatusOf(k, omega_s, phi, e_mu) {
    var worst = 'MEASURED', why = [];
    if (phi > k.phi_measured_max) { worst = 'EXTRAPOLATED'; why.push('phi=' + phi + ' exceeds the scanned record (<= ' + k.phi_measured_max + ' LHD)'); }
    var projected = false;
    Object.keys(k.sticking).forEach(function (name) { var s = k.sticking[name]; if (Math.abs(s.omega_s - omega_s) < 1e-9 && s.status === 'PROJECTED') projected = true; });
    if (projected || omega_s < k.omega_measured_min) { if (worst !== 'EXTRAPOLATED') worst = 'PROJECTED'; why.push('sticking below the measured floor requires an undemonstrated lever'); }
    if (e_mu < k.E_mu_achieved_GeV) { if (worst === 'MEASURED') worst = 'PROJECTED'; why.push('E_mu=' + e_mu + ' GeV is below the achieved ' + k.E_mu_achieved_GeV + ' GeV'); }
    if (e_mu < k.E_mu_floor_GeV) { worst = 'REFUSED'; why.push('E_mu=' + e_mu + ' GeV is below the ' + k.E_mu_floor_GeV + ' GeV kinematic floor'); }
    return { status: worst, why: why.length ? why.join('; ') : 'all inputs within the measured record' };
  }
  function mucfBand(k, omega_s, phi, e_mu) {
    var c = k.transfer[0], u = k.transfer[1], scale = k.lambda_c / c;
    return [-1, 0, 1].map(function (s) { return mucfGain(k, omega_s, phi, e_mu, (c + s * u) * scale); });
  }
  function mucfMuonsFor(k, power_w, omega_s, phi) { return power_w / (k.Q_fus_MeV * 1.602e-13) / mucfCycles(k, omega_s, phi); }
  function mucfBisectSticking(k, phi, e_mu, target) {
    var lo = 1e-5, hi = 0.02;
    for (var i = 0; i < 200; i++) { var mid = (lo + hi) / 2; if (mucfGain(k, mid, phi, e_mu) > target) lo = mid; else hi = mid; }
    return lo;
  }
  var MODE_MUCF = {
    id: 'mucf',
    requires: 'particles',
    title: 'The muon energy balance',
    status: PINNED,
    statusNote: 'The paper\'s own model (papers/Muon_Catalysed_Fusion_v1.1.md section 5, tools/mucf.py), computed for it; every input carries the paper\'s status — MEASURED, PINNED, PROJECTED, EXTRAPOLATED, PROSE-ONLY — and the result the weakest of them. Below the 0.30 GeV kinematic floor the mode refuses. Not a lattice figure: the lattice supplies the frame, not the rates.',
    description: 'N = φλ_c / (λ₀ + ω_s φλ_c) catalytic cycles per muon, Q = N · Q_fus / E_μ, and the production cost at which Q reaches a target under the heat convention and, with only f_work of the fusion heat convertible, the work convention; Q across the transfer-rate band; the muon rate a fusion power needs. Sticking ω_s, density φ (liquid-hydrogen density units) and E_μ (GeV) are the three free axes.',
    inputs: [
      { name: 'sticking', label: 'sticking case', type: 'select', default: 'sin',
        options: [{ value: 'sin', label: 'SIN, 0.45 % measured' }, { value: 'psi', label: 'PSI, 0.56 % measured' },
                  { value: 'pol', label: 'dual polarisation, 0.34 % projected' }, { value: 'j1', label: 'J=1,v=0, 0.31 % projected (reserved)' },
                  { value: 'both', label: 'both levers composed, 0.234 % projected' }, { value: 'custom', label: 'typed below' }] },
      { name: 'omega_s', label: 'ω_s (fraction)', type: 'number', default: '', help: 'used when the case is "typed": net sticking loss per fusion, e.g. 0.0045' },
      { name: 'phi', label: 'φ (LHD)', type: 'number', default: 1.2, help: 'density in liquid-hydrogen units; the scanned record is 0.01 to 1.5' },
      { name: 'e_mu', label: 'E_μ (GeV per muon)', type: 'number', default: 5, help: 'the paper prices its binder at 5; the kinematic floor is 0.30; below it the mode refuses' },
      { name: 'target', label: 'target Q', type: 'number', default: 1, help: '1 is scientific breakeven, the paper\'s convention, not a plant that feeds itself' },
      { name: 'power', label: 'fusion power (W, optional)', type: 'number', default: '', help: 'if given, the muon rate it needs' },
    ],
    source: { instrument: 'mucf_gain', file: 'tools/mucf.py',
              also: ['mucf_cycles', 'mucf_e_mu_for', 'mucf_e_mu_for_work', 'mucf_status_of', 'mucf_band', 'mucf_muons_for'] },
    run: async function (values, ctx) {
      var k = mucfConsts(ctx);
      if (!k) return fail('data/index.js carries no muon instrument block (index.particles.muon.instrument)');
      var rows = [];
      var caseName = values.sticking || 'sin', omega_s, oStatus, oNote;
      if (caseName === 'custom') { omega_s = num(values.omega_s); if (omega_s === null || omega_s <= 0) return fail('type ω_s as a positive fraction, or pick a case'); oStatus = null; oNote = 'typed, not a figure of the index'; }
      else { var sc = k.sticking[caseName]; if (!sc) return fail('unknown sticking case ' + caseName); omega_s = sc.omega_s; oStatus = sc.status; oNote = 'mucf.py STICKING["' + caseName + '"]' + (caseName === 'j1' ? '; ' + k.reservation_j1 : ''); }
      var phi = num(values.phi), e_mu = num(values.e_mu), target = num(values.target), power = num(values.power);
      if (phi === null || phi <= 0) return fail('φ must be a positive density in LHD units');
      if (e_mu === null || e_mu <= 0) return fail('E_μ must be a positive cost in GeV');
      if (target === null || target <= 0) target = 1;
      var st = mucfStatusOf(k, omega_s, phi, e_mu);
      rows.push(row('ω_s', omega_s, oStatus, oNote));
      rows.push(row('φ', phi + ' LHD', phi <= k.phi_measured_max ? 'MEASURED' : 'EXTRAPOLATED', phi <= k.phi_measured_max ? 'within the scanned record (PSI 0.01–1.5 LHD)' : 'beyond the scanned record'));
      rows.push(row('E_μ', e_mu + ' GeV', e_mu >= k.E_mu_achieved_GeV ? 'MEASURED' : (e_mu >= k.E_mu_floor_GeV ? 'PROJECTED' : 'REFUSED'), 'the paper\'s 5 GeV is reclassified aspirational in v1.1; the best published figure is 5 TeV per stopped muon (collection budget)'));
      rows.push(row('λ₀', k.lambda_0.toExponential(3) + ' s⁻¹', 'MEASURED', 'bound-muon disappearance'));
      rows.push(row('λ_c', k.lambda_c.toExponential(2) + ' s⁻¹', 'PINNED', 'cycle saturation, the harmonic sum (section 3.3); its parent the transfer rate (' + k.transfer[0].toExponential(1) + ' ± ' + k.transfer[1].toExponential(1) + ') MEASURED'));
      rows.push(row('Q_fus', k.Q_fus_MeV + ' MeV', 'MEASURED', 'd + t'));
      if (st.status === 'REFUSED') {
        rows.push(row('status', 'REFUSED', 'REFUSED', st.why));
        return { rows: rows, ok: false, message: 'refused: ' + st.why + '. Nothing is computed below the kinematic floor; a perfect collector costs 0.30 GeV per muon.' };
      }
      var N = mucfCycles(k, omega_s, phi), Q = mucfGain(k, omega_s, phi, e_mu), b = mucfBand(k, omega_s, phi, e_mu);
      rows.push(row('N, cycles per muon', fmt(N, 1), st.status, 'φλ_c / (λ₀ + ω_s φλ_c)'));
      rows.push(row('Q, heat convention', fmt(Q, 3), st.status, 'N · Q_fus / E_μ; ' + st.why));
      rows.push(row('Q across the transfer band', fmt(b[0], 3) + ' … ' + fmt(b[2], 3), st.status, 'λ_c inherits its parent\'s ±' + k.transfer[1].toExponential(1) + ' band, scaled by 2.6/2.7'));
      rows.push(row('E_μ for Q = ' + target + ', heat', fmt(mucfEmuFor(k, omega_s, phi, target), 3) + ' GeV', st.status, 'the cost at which heat out reaches the target'));
      rows.push(row('E_μ for Q = ' + target + ', work', fmt(mucfEmuForWork(k, omega_s, phi, target), 3) + ' GeV', 'PROSE-ONLY', 'only f_work = ' + k.f_work + ' of the fusion heat is convertible (alpha share ' + k.f_alpha + ', blanket at 800 K ' + k.carnot_800 + '); PROSE-ONLY'));
      rows.push(row('sticking ceiling', fmt(1 / omega_s, 0) + ' turns', 'DERIVED', 'the asymptote 1/ω_s, omitting decay'));
      rows.push(row('breakeven sticking at this φ and E_μ', (mucfBisectSticking(k, phi, e_mu, target) * 100).toFixed(3) + ' %', st.status, 'the ω_s at which Q reaches the target, by bisection'));
      if (power !== null && power > 0) rows.push(row('muons per second for ' + power + ' W', mucfMuonsFor(k, power, omega_s, phi).toExponential(2) + ' s⁻¹', st.status, 'power / (Q_fus · N); against ~10⁸ /s at PSI today and ~10¹⁰ /s planned (PO-0898)'));
      rows.push(row('the collection chain', k.E_mu_delivered_TeV + ' TeV per muon delivered; gap ' + k.collection_factor.toExponential(2) + '×', 'PROSE-ONLY', 'a real beamline delivers one muon per 874 TeV of driver energy; the two gaps of section 5 are one chain read at two thresholds'));
      return { rows: rows, ok: true };
    },
    selftest: async function (ctx) {
      var ck = new Checker();
      var k = mucfConsts(ctx), fx = ctx.index && ctx.index.particles && ctx.index.particles.muon.instrument.fixtures;
      if (!k || !fx) { ck.ok('muon instrument block present in data/index.js', false, 'absent', 'present'); return ck.result(); }
      var diverge = [];
      fx.table_5_1.forEach(function (r) {
        r.Q.forEach(function (want, i) {
          var got = mucfGain(k, r.omega_s, fx.phis[i], fx.E_mu);
          if (Math.abs(got - want) <= 0.006) ck.ok('Table 5.1: ω_s=' + r.omega_s + ' φ=' + fx.phis[i] + ' Q=' + want, true, got.toFixed(3), want);
          else diverge.push({ r: r, i: i, got: got, want: want });
        });
      });
      // the recorded divergence: the 0.234 % row reproduces at the unrounded transfer rate 2.7e8, not the pinned 2.6e8 (mucf.py --selftest, [1b]); NOTED, not repaired
      diverge.forEach(function (d) {
        var at27 = mucfGain(k, d.r.omega_s, fx.phis[d.i], fx.E_mu, k.transfer[0]);
        ck.ok('Table 5.1: ω_s=' + d.r.omega_s + ' φ=' + fx.phis[d.i] + ' diverges at λ_c=2.6e8 (' + d.got.toFixed(3) + ' vs ' + d.want + ') and reproduces at the transfer rate 2.7e8 — the instrument\'s recorded finding', Math.abs(at27 - d.want) <= 0.006, at27.toFixed(3), d.want);
      });
      ck.ok('the divergent cells are all in one row, ω_s = 0.234 %', diverge.every(function (d) { return Math.abs(d.r.omega_s - 0.00234) < 1e-9; }), diverge.length, 'one row');
      fx.breakeven_5_1.forEach(function (b) {
        var got = mucfBisectSticking(k, b.phi, fx.E_mu, 1.0);
        ck.near('breakeven sticking at φ=' + b.phi + ' (section 5.1)', got, b.omega_s, 2e-5);
      });
      ck.near('the composed lever 0.34 % · 0.31/0.45 = 0.234 %', 0.0034 * 0.31 / 0.45, 0.00234, 5e-6);
      ck.near('sticking ceiling ~222 turns at 0.45 %', 1 / 0.0045, 222, 1.0);
      ck.eq('status: measured inputs at 5 GeV, φ = 1.2', mucfStatusOf(k, k.sticking.sin.omega_s, 1.2, 5.0).status, 'MEASURED');
      ck.eq('status: a projected lever is PROJECTED', mucfStatusOf(k, k.sticking.pol.omega_s, 1.2, 5.0).status, 'PROJECTED');
      ck.eq('status: φ beyond the scanned record is EXTRAPOLATED', mucfStatusOf(k, k.sticking.sin.omega_s, 2.0, 5.0).status, 'EXTRAPOLATED');
      ck.eq('status: below the kinematic floor is REFUSED', mucfStatusOf(k, k.sticking.sin.omega_s, 1.2, 0.2).status, 'REFUSED');
      ck.ok('the band brackets the central value', (function () { var b = mucfBand(k, 0.0045, 1.2, 5.0); return b[0] < b[1] && b[1] < b[2]; })(), 'ordered', 'ordered');
      return ck.result();
    },
  };


  // ----------------------------------- chemistry: formulas and equations, checked not written
  // The page writes no chemistry. It checks a chemical equation another author wrote -- a
  // model's answer, or one typed here -- for conservation of every element and of charge,
  // and links every element in it to its record. Everything here is deterministic and the
  // selftest holds it to fixtures.
  var ELEMENT_SYMBOLS = ('H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr ' +
    'Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn ' +
    'Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og').split(' ');
  var SYMBOL_Z = {};
  ELEMENT_SYMBOLS.forEach(function (sy, i) { SYMBOL_Z[sy] = i + 1; });
  var SUB = { '₀': '0', '₁': '1', '₂': '2', '₃': '3', '₄': '4', '₅': '5', '₆': '6', '₇': '7', '₈': '8', '₉': '9' };
  var SUP = { '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9', '⁺': '+', '⁻': '-' };
  function normaliseFormula(s) {
    // subscripts to digits; a superscript charge (²⁺, ⁻) to the explicit ^2+ form, so it stays
    // distinguishable from a subscript followed by a sign
    return String(s).replace(/[₀₁₂₃₄₅₆₇₈₉]/g, function (c) { return SUB[c]; })
      .replace(/([⁰¹²³⁴⁵⁶⁷⁸⁹]*)([⁺⁻])/g, function (_m, d, sg) { return '^' + d.split('').map(function (c) { return SUP[c]; }).join('') + SUP[sg]; })
      .replace(/[−–]/g, '-').replace(/\s+/g, '');
  }
  var ROMAN = { I: 1, II: 2, III: 3, IV: 4, V: 5, VI: 6, VII: 7, VIII: 8 };
  var SUBS = '₀₁₂₃₄₅₆₇₈₉', SUPS = '⁰¹²³⁴⁵⁶⁷⁸⁹';
  function typesetFormula(f, charge) {
    // digits after a letter or a closing bracket are subscripts; the charge is a superscript
    var t = f.replace(/([A-Za-z\)\]])(\d+)/g, function (_m, a, d) { return a + d.split('').map(function (c) { return SUBS[+c]; }).join(''); });
    if (charge) t += (Math.abs(charge) > 1 ? String(Math.abs(charge)).split('').map(function (c) { return SUPS[+c]; }).join('') : '') + (charge > 0 ? '⁺' : '⁻');
    return t;
  }
  function parseFormula(text, reading) {
    // {counts: {El: n}, charge, phase, errors: [], notes: [], typeset, ambiguous}
    // reading: 'charge' or 'subscript', for a plain "X<digits><sign>" after a single element
    // symbol, which the text alone cannot decide: Fe3+ is iron(III) but N3- is azide and I3-
    // triiodide. The default is the charge reading, the alternative is recorded, and the
    // balancer and the check try the other where the default cannot balance.
    var out = { counts: {}, charge: 0, phase: null, errors: [], notes: [], ambiguous: null, typeset: '' };
    var f = normaliseFormula(text);
    var ph = f.match(/\((s|l|g|aq|cr|am)\)$/i);
    if (ph) { out.phase = ph[1].toLowerCase(); f = f.slice(0, -ph[0].length); }
    var ch = f.match(/\^\{?(\d*)([+-])\}?$/) || f.match(/[\{\(](\d*)([+-])[\}\)]$/) || f.match(/([+-])(\d+)$/);
    if (ch) {
      var mag, sg;
      if (/^[+-]\d+$/.test(ch[0])) { sg = ch[1]; mag = ch[2]; } else { mag = ch[1]; sg = ch[2]; }
      out.charge = (mag ? parseInt(mag, 10) : 1) * (sg === '+' ? 1 : -1); f = f.slice(0, -ch[0].length);
    } else {
      var rm = f.match(/^([A-Z][a-z]?)\((I{1,3}|IV|VI{0,3}|VIII)\)$/);
      if (rm) { out.charge = ROMAN[rm[2]]; f = rm[1]; out.notes.push(rm[1] + '(' + rm[2] + ') read as the ion ' + rm[1] + '^' + ROMAN[rm[2]] + '+'); }
      else {
        ch = f.match(/(\d*)([+-])$/);
        if (ch) {
          var before = f.slice(0, -ch[0].length);
          if (ch[1] && /^[A-Z][a-z]?$/.test(before)) {
            var asCharge = { counts: {}, charge: parseInt(ch[1], 10) * (ch[2] === '+' ? 1 : -1), f: before },
                asSub = { counts: {}, charge: ch[2] === '+' ? 1 : -1, f: before + ch[1] };
            asCharge.counts[before] = 1; asSub.counts[before] = parseInt(ch[1], 10);
            var use = reading === 'subscript' ? asSub : asCharge, alt = reading === 'subscript' ? asCharge : asSub;
            out.charge = use.charge; f = use.f;
            out.ambiguous = { readAs: reading === 'subscript' ? 'subscript' : 'charge', alt: { counts: alt.counts, charge: alt.charge, typeset: typesetFormula(alt.f, alt.charge) },
              spellings: { charge: before + '^' + ch[1] + ch[2], subscript: before + ch[1] + '^' + ch[2] } };
          } else { out.charge = ch[2] === '+' ? 1 : -1; f = f.slice(0, -1); }
        }
      }
    }
    if (f === 'e' || f === '') { if (f === 'e') { if (!ch) out.errors.push('an electron needs its charge, e-'); out.typeset = 'e⁻'; } else out.errors.push('empty formula'); return out; }
    var parts = f.split(/[·*]/);
    parts.forEach(function (part, pi) {
      var mult = 1;
      if (pi > 0) { var m = part.match(/^(\d+)/); if (m) { mult = parseInt(m[1], 10); part = part.slice(m[1].length); } }
      var stack = [{}], i = 0;
      while (i < part.length) {
        var c = part[i];
        if (c === '(' || c === '[') { stack.push({}); i += 1; continue; }
        if (c === ')' || c === ']') {
          i += 1; var n = part.slice(i).match(/^\d+/); var k = n ? parseInt(n[0], 10) : 1; if (n) i += n[0].length;
          var top = stack.pop(); if (!stack.length) { out.errors.push('unbalanced bracket'); return; }
          Object.keys(top).forEach(function (el) { stack[stack.length - 1][el] = (stack[stack.length - 1][el] || 0) + top[el] * k; });
          continue;
        }
        var em = part.slice(i).match(/^([A-Z][a-z]?)(\d*)/);
        if (!em) { out.errors.push('cannot read "' + part.slice(i, i + 4) + '"'); return; }
        var el = em[1], cnt = em[2] ? parseInt(em[2], 10) : 1;
        if (el === 'D' || el === 'T') { out.notes.push(el + ' counted as H'); el = 'H'; }
        if (!SYMBOL_Z[el]) { out.errors.push('unknown element symbol ' + el); }
        stack[stack.length - 1][el] = (stack[stack.length - 1][el] || 0) + cnt;
        i += em[0].length;
      }
      if (stack.length !== 1) { out.errors.push('unbalanced bracket'); return; }
      Object.keys(stack[0]).forEach(function (el) { out.counts[el] = (out.counts[el] || 0) + stack[0][el] * mult; });
    });
    out.typeset = typesetFormula(f, out.charge) + (out.phase ? '(' + out.phase + ')' : '');
    return out;
  }
  function describeReading(sp) {
    // "Fe³⁺: Fe 1, charge +3" -- how a species was read, for the rows that show it
    var els = Object.keys(sp.counts).map(function (e) { return e + ' ' + sp.counts[e]; }).join(', ');
    return sp.typeset + ': ' + (els || 'no atoms') + ', charge ' + (sp.charge > 0 ? '+' : '') + sp.charge;
  }
  function parseSide(text, readings) {
    readings = readings || {};
    return text.split(/\s\+\s|\s\+$|^\+\s/).map(function (t) { return t.trim(); }).filter(Boolean).map(function (t) {
      var m = t.match(/^(\d+(?:\.\d+)?|\d+\/\d+)\s*(.*)$/), coef = 1, formula = t;
      if (m && m[2]) { coef = m[1].indexOf('/') >= 0 ? parseInt(m[1].split('/')[0], 10) / parseInt(m[1].split('/')[1], 10) : parseFloat(m[1]); formula = m[2]; }
      var f = parseFormula(formula, readings[normaliseFormula(formula)]);
      return { coef: coef, formula: formula, counts: f.counts, charge: f.charge, phase: f.phase, errors: f.errors, notes: f.notes, typeset: f.typeset, ambiguous: f.ambiguous };
    });
  }
  function parseEquation(text, readings) {
    var t = String(text).trim().replace(/\s+/g, ' ');
    var arrow = t.match(/\s(→|⟶|->|—>|⇌|⇄|<=>|↔|⟷|=)\s/);
    if (!arrow) return { error: 'no arrow found: write reactants → products (→, ->, = or ⇌), with spaces around + signs' };
    var idx = t.indexOf(arrow[0]);
    return { arrow: arrow[1], reactants: parseSide(t.slice(0, idx), readings), products: parseSide(t.slice(idx + arrow[0].length), readings) };
  }
  function ambiguousSpecies(eq) {
    var out = {};
    eq.reactants.concat(eq.products).forEach(function (sp) { if (sp.ambiguous) out[normaliseFormula(sp.formula)] = sp; });
    return Object.keys(out);
  }
  function readingCombos(keys) {
    // every assignment of charge/subscript to the ambiguous species, default first; capped
    keys = keys.slice(0, 6);
    var combos = [];
    for (var mask = 0; mask < (1 << keys.length); mask++) {
      var r = {}; keys.forEach(function (k, i) { r[k] = (mask >> i) & 1 ? 'subscript' : 'charge'; });
      combos.push(r);
    }
    return combos;
  }
  function readingNotes(eq) {
    return eq.reactants.concat(eq.products).filter(function (sp) { return sp.ambiguous; }).map(function (sp) {
      return sp.formula + ' read as ' + sp.typeset + ' (' + sp.ambiguous.readAs + '); the other reading, ' + sp.ambiguous.alt.typeset + ', is written ' + sp.ambiguous.spellings[sp.ambiguous.readAs === 'charge' ? 'subscript' : 'charge'];
    });
  }
  function checkEquation(text, readings) {
    var eq = parseEquation(text, readings);
    if (eq.error) return { ok: false, error: eq.error, text: text };
    if (!readings) {
      var amb = ambiguousSpecies(eq);
      if (amb.length) {
        var combos = readingCombos(amb), first = null;
        for (var ci = 0; ci < combos.length; ci++) {
          var r = checkEquation(text, combos[ci]);
          if (ci === 0) first = r;
          if (r.balanced) { if (ci > 0) r.notes = r.notes.concat(['balanced under the other reading of an ambiguous ion: ' + readingNotes(parseEquation(text, combos[ci])).join('; ')]); r.readings = combos[ci]; return r; }
        }
        first.notes = first.notes.concat(readingNotes(eq)); first.readings = combos[0];
        return first;
      }
    }
    var tally = {}, chargeL = 0, chargeR = 0, errors = [], notes = [];
    function add(side, sign) {
      side.forEach(function (sp) {
        errors = errors.concat(sp.errors.map(function (e) { return sp.formula + ': ' + e; })); notes = notes.concat(sp.notes);
        Object.keys(sp.counts).forEach(function (el) { tally[el] = tally[el] || [0, 0]; tally[el][sign] += sp.coef * sp.counts[el]; });
        if (sign === 0) chargeL += sp.coef * sp.charge; else chargeR += sp.coef * sp.charge;
      });
    }
    add(eq.reactants, 0); add(eq.products, 1);
    var atoms = Object.keys(tally).sort().map(function (el) { return { element: el, Z: SYMBOL_Z[el] || null, left: tally[el][0], right: tally[el][1], ok: Math.abs(tally[el][0] - tally[el][1]) < 1e-9 }; });
    var balancedAtoms = atoms.every(function (a) { return a.ok; }), balancedCharge = Math.abs(chargeL - chargeR) < 1e-9;
    return { ok: errors.length === 0, text: text, arrow: eq.arrow, reactants: eq.reactants, products: eq.products, atoms: atoms,
      charge: { left: chargeL, right: chargeR, ok: balancedCharge }, balanced: errors.length === 0 && balancedAtoms && balancedCharge,
      readings: readings || {}, readAs: eq.reactants.concat(eq.products).map(describeReading),
      typeset: eq.reactants.map(function (sp) { return (sp.coef === 1 ? '' : sp.coef + ' ') + sp.typeset; }).join(' + ') + ' → ' + eq.products.map(function (sp) { return (sp.coef === 1 ? '' : sp.coef + ' ') + sp.typeset; }).join(' + '),
      errors: errors, notes: notes.filter(function (n, i, a) { return a.indexOf(n) === i; }) };
  }

  // ------------------------------------- the machine check over a model's answer
  // Three markers the model is instructed to use: ⟦path⟧ cites a figure of the loaded data by
  // its path; ⟪fn(args) = value⟫ states a computation the page's own library can repeat;
  // ⦃equation⦄ wraps a chemical equation. The checker resolves, recomputes and balances, and
  // it never repairs: a mismatch is reported beside the model's own words.
  var NUM_RX = /[-−]?\d+(?:[.,]\d+)?(?:\s?[×x]\s?10\^?[-−]?\d+|e[-−]?\d+)?/g;
  function parseNum(s) {
    if (s === null || s === undefined) return null;
    var t = String(s).trim().replace(/−/g, '-').replace(/,/g, '').replace(/\s?[×x]\s?10\^?/, 'e');
    var v = parseFloat(t);
    return isNaN(v) ? null : v;
  }
  function numbersAgree(a, b) {
    if (a === null || b === null) return false;
    var tol = Math.max(5e-4, 1e-3 * Math.abs(b));
    return Math.abs(a - b) <= tol;
  }
  function lastNumberBefore(text, at) {
    var win = text.slice(Math.max(0, at - 60), at), m, last = null;
    NUM_RX.lastIndex = 0;
    while ((m = NUM_RX.exec(win)) !== null) last = m[0];
    return last;
  }
  var ROUTE_TYPES = ['primary', 'preprint', 'review', 'compilation', 'citing', 'deposit', 'database'];
  function routeType(t) {
    var s = String(t || '').toLowerCase();
    for (var i = 0; i < ROUTE_TYPES.length; i++) if (s.indexOf(ROUTE_TYPES[i]) >= 0) return ROUTE_TYPES[i];
    if (/table|handbook|codata|compend/.test(s)) return 'compilation';
    if (/arxiv|eprint/.test(s)) return 'preprint';
    if (/archive|repositor|scan|hathi|gallica/.test(s)) return 'deposit';
    if (/nist|pdg|database|db\b/.test(s)) return 'database';
    return null;
  }
  function identifierOf(src) {
    var t = String(src || '');
    var m = t.match(/10\.\d{4,9}\/[^\s"'<>,;)\]]+/); if (m) return { kind: 'doi', id: m[0].replace(/[.)]+$/, ''), url: 'https://doi.org/' + m[0].replace(/[.)]+$/, '') };
    m = t.match(/arXiv[: ]?(\d{4}\.\d{4,5}(?:v\d+)?)/i) || t.match(/arxiv\.org\/abs\/([^\s)]+)/i); if (m) return { kind: 'arxiv', id: m[1], url: 'https://arxiv.org/abs/' + m[1] };
    m = t.match(/ark:\/\d{5}\/[A-Za-z0-9]+/); if (m) return { kind: 'ark', id: m[0], url: 'https://gallica.bnf.fr/' + m[0] };
    m = t.match(/https?:\/\/[^\s)\]>"']+/); if (m) return { kind: 'url', id: m[0].replace(/[.,;)]+$/, ''), url: m[0].replace(/[.,;)]+$/, '') };
    return null;
  }
  function hostOf(u) { try { return new URL(u).host.replace(/^www\./, ''); } catch (e) { return null; } }
  function checkRetrieval(text, searched) {
    // the RETRIEVAL table at the end of an answer, one row per (target, route), against the
    // sources the search tool actually returned: a source the searches never returned is
    // flagged, an open route with no identifier is flagged, and the open routes per target
    // are counted -- one route is fragile, two survive the loss of either
    var out = { rows: [], targets: [], present: false };
    var at = text.search(/^\s*RETRIEVAL\s*$/mi);
    if (at < 0) return out;
    out.present = true; out.at = at;
    var hosts = {}; (searched || []).forEach(function (u) { var h = hostOf(u); if (h) hosts[h] = true; hosts[u] = true; });
    var lines = text.slice(at).split('\n').slice(1);
    var byTarget = {};
    lines.forEach(function (ln) {
      if (!/\|/.test(ln)) return;
      var c = ln.split('|').map(function (x) { return x.trim(); });
      if (c.length < 4) return;
      if (/^target$/i.test(c[0]) && /^route/i.test(c[1])) return;   // a header the model echoed
      var id = identifierOf(c[2]), res = String(c[3] || '').toLowerCase();
      var result = /open|found|retriev/.test(res) ? 'open' : /block|paywall|closed/.test(res) ? 'blocked' : /untried|not tried/.test(res) ? 'untried' : /empty|none|no /.test(res) ? 'empty' : res || '?';
      var searchedHere = id && id.url ? (hosts[id.url] || hosts[hostOf(id.url)] || false) : false;
      var row = { target: c[0], route: routeType(c[1]) || c[1] || '?', source: c[2], identifier: id, result: result, value: c[4] || '',
        verdict: result !== 'open' ? result : (!id ? 'open, no identifier' : (searched === null ? 'open, unverifiable here' : (searchedHere ? 'open, among this session\'s searches' : 'open, NOT among this session\'s searches'))) };
      out.rows.push(row);
      var t = byTarget[row.target] || (byTarget[row.target] = { target: row.target, routes: [], open: 0, blocked: 0, untried: 0, empty: 0 });
      t.routes.push(row.route); t[result === 'open' || result === 'blocked' || result === 'untried' || result === 'empty' ? result : 'empty'] += 1;
    });
    out.targets = Object.keys(byTarget).map(function (k) { var t = byTarget[k]; t.rho = t.open; t.verdict = t.open >= 2 ? 'closes on two routes' : t.open === 1 ? 'FRAGILE: one route' : 'not retrieved: a stated gap'; return t; });
    return out;
  }
  function checkAnswer(text, resolve, compute, searched) {
    // resolve(path) -> {value, status} | null;  compute(name, args) -> number | null (not computable) | undefined (unknown)
    // searched: the URLs the search tool returned this session, or null when not known
    var out = { citations: [], computations: [], equations: [], numbers: 0, unverified: 0, sources: [] };
    var body = text, retrieval = checkRetrieval(text, searched === undefined ? null : searched);
    if (retrieval.present) body = text.slice(0, retrieval.at);
    out.retrieval = retrieval;
    var hostsS = {}; (searched || []).forEach(function (u) { var h = hostOf(u); if (h) hostsS[h] = true; hostsS[u] = true; });
    var mm, srx = /⟨⟨([^⟩]+)⟩⟩/g;
    while ((mm = srx.exec(body)) !== null) {
      var idm = identifierOf(mm[1]);
      out.sources.push({ text: mm[1].trim(), identifier: idm, at: mm.index, len: mm[0].length,
        verdict: !idm ? 'no identifier' : (searched === undefined || searched === null ? 'unverifiable here' : (hostsS[idm.url] || hostsS[hostOf(idm.url)] ? 'among this session\'s searches' : 'NOT among this session\'s searches')) });
    }
    text = body;
    var claimed = [];
    var m, rx = /⟦([^⟧]+)⟧/g;
    while ((m = rx.exec(text)) !== null) {
      var path = m[1].trim(), got = resolve(path), stated = lastNumberBefore(text, m.index), verdict;
      if (!got) verdict = 'not in the index';
      else if (typeof got.value === 'number') {
        var sv = parseNum(stated);
        verdict = sv === null ? 'cited, no figure beside it' : (numbersAgree(sv, got.value) ? 'matches' : 'DIFFERS');
      } else verdict = 'cited';
      out.citations.push({ path: path, stated: stated, value: got ? got.value : null, status: got ? got.status : null, verdict: verdict, at: m.index, len: m[0].length });
      if (stated !== null) claimed.push(m.index);
    }
    rx = /⟪([A-Za-z_][A-Za-z0-9_]*)\(([^)]*)\)\s*=\s*([^⟫]+)⟫/g;
    while ((m = rx.exec(text)) !== null) {
      var name = m[1], args = m[2].split(',').map(function (a) { return a.trim(); }).filter(Boolean).map(function (a) { var v = parseNum(a); return v === null ? a : v; });
      var stated2 = parseNum(m[3]), val = compute(name, args), verdict2;
      if (val === undefined) verdict2 = 'unknown function';
      else if (val === null) verdict2 = 'not computable from the loaded data';
      else verdict2 = numbersAgree(stated2, val) ? 'agrees' : 'DIFFERS';
      out.computations.push({ name: name, args: args, stated: m[3].trim(), value: val, verdict: verdict2, at: m.index, len: m[0].length });
    }
    rx = /⦃([^⦄]+)⦄/g;
    while ((m = rx.exec(text)) !== null) {
      var eq = checkEquation(m[1]);
      out.equations.push({ text: m[1].trim(), result: eq, verdict: eq.error ? 'unreadable' : (eq.errors.length ? 'unreadable' : (eq.balanced ? 'balanced' : 'NOT balanced')), at: m.index, len: m[0].length });
    }
    // numbers the model states that no marker covers
    var stripped = text.replace(/⟦[^⟧]*⟧|⟪[^⟫]*⟫|⦃[^⦄]*⦄|⟨⟨[^⟩]*⟩⟩/g, function (x) { return ' '.repeat(x.length); });
    NUM_RX.lastIndex = 0;
    var total = 0, covered = 0;
    while ((m = NUM_RX.exec(stripped)) !== null) {
      if (m.index > 0 && /[A-Za-z]/.test(stripped[m.index - 1])) continue;   // a subscript in a formula, not a figure
      total += 1;
      var end = m.index + m[0].length, after = text.slice(end, end + 40);
      if (/^[^⟦⟪⦃⟨]{0,30}(?:[⟦⟪]|⟨⟨)/.test(after)) covered += 1;   // cited from the index, computed, or attributed to a web route
    }
    out.numbers = total; out.unverified = total - covered;
    out.summary = out.citations.length + ' citation' + (out.citations.length === 1 ? '' : 's') + ' (' +
      out.citations.filter(function (c) { return c.verdict === 'matches' || c.verdict === 'cited'; }).length + ' verified, ' +
      out.citations.filter(function (c) { return c.verdict === 'DIFFERS'; }).length + ' differing, ' +
      out.citations.filter(function (c) { return c.verdict === 'not in the index'; }).length + ' not found); ' +
      out.computations.length + ' computation' + (out.computations.length === 1 ? '' : 's') + ' (' + out.computations.filter(function (c) { return c.verdict === 'agrees'; }).length + ' agree); ' +
      out.equations.length + ' equation' + (out.equations.length === 1 ? '' : 's') + ' (' + out.equations.filter(function (e) { return e.verdict === 'balanced'; }).length + ' balanced); ' +
      out.unverified + ' of ' + out.numbers + ' numbers left unverified (the model\'s own)' +
      (out.sources.length ? '; ' + out.sources.length + ' web source' + (out.sources.length === 1 ? '' : 's') + ' cited (' + out.sources.filter(function (x) { return /among this session/.test(x.verdict) && !/NOT/.test(x.verdict); }).length + ' among the searches)' : '') +
      (retrieval.present ? '; retrieval: ' + retrieval.targets.length + ' target' + (retrieval.targets.length === 1 ? '' : 's') + ', ' + retrieval.targets.filter(function (t) { return t.rho >= 2; }).length + ' closing on two routes, ' + retrieval.targets.filter(function (t) { return t.rho === 1; }).length + ' fragile, ' + retrieval.targets.filter(function (t) { return t.rho === 0; }).length + ' not retrieved' : '');
    return out;
  }

  // ------------------------------------- balancing: the algebraic method, exact
  // Conservation of every element and of charge is a homogeneous linear system over the
  // species; its nullspace, computed exactly over the rationals (BigInt fractions), holds
  // every balance the species admit. One dimension is a balance, scaled to the smallest
  // whole numbers; none means the species cannot balance as written; more than one means
  // the species admit more than one reaction and the mode shows the basis rather than
  // choosing. Redox in water adds H+ and H2O (acidic) or OH- and H2O (basic), and a
  // half-reaction adds e-; an added species lands on whichever side its sign puts it.
  function bgcd(a, b) { a = a < 0n ? -a : a; b = b < 0n ? -b : b; while (b) { var t = a % b; a = b; b = t; } return a; }
  function fr(n, d) { d = d === undefined ? 1n : d; if (d < 0n) { n = -n; d = -d; } var g = bgcd(n, d) || 1n; return { n: n / g, d: d / g }; }
  function fadd(a, b) { return fr(a.n * b.d + b.n * a.d, a.d * b.d); }
  function fsub(a, b) { return fr(a.n * b.d - b.n * a.d, a.d * b.d); }
  function fmul(a, b) { return fr(a.n * b.n, a.d * b.d); }
  function fdiv(a, b) { return fr(a.n * b.d, a.d * b.n); }
  function fzero(a) { return a.n === 0n; }
  function nullspace(M, ncols) {
    // M: rows of BigInt fractions; returns a list of basis vectors (fractions) of {x : M x = 0}
    var A = M.map(function (r) { return r.slice(); }), pivots = [], r = 0;
    for (var c = 0; c < ncols && r < A.length; c++) {
      var pr = -1;
      for (var i = r; i < A.length; i++) if (!fzero(A[i][c])) { pr = i; break; }
      if (pr < 0) continue;
      var tmp = A[r]; A[r] = A[pr]; A[pr] = tmp;
      var pv = A[r][c];
      A[r] = A[r].map(function (v) { return fdiv(v, pv); });
      for (var k = 0; k < A.length; k++) {
        if (k === r || fzero(A[k][c])) continue;
        var f = A[k][c];
        A[k] = A[k].map(function (v, j) { return fsub(v, fmul(f, A[r][j])); });
      }
      pivots.push(c); r += 1;
    }
    var free = []; for (var j = 0; j < ncols; j++) if (pivots.indexOf(j) < 0) free.push(j);
    return free.map(function (fc) {
      var v = []; for (var j = 0; j < ncols; j++) v.push(fr(0n));
      v[fc] = fr(1n);
      pivots.forEach(function (pc, i) { v[pc] = fr(-A[i][fc].n, A[i][fc].d); });
      return v;
    });
  }
  function toIntegers(v) {
    var L = 1n; v.forEach(function (x) { L = L / bgcd(L, x.d) * x.d; });
    var ints = v.map(function (x) { return x.n * (L / x.d); });
    var g = 0n; ints.forEach(function (x) { g = bgcd(g, x); });
    if (g > 1n) ints = ints.map(function (x) { return x / g; });
    var neg = 0, pos = 0; ints.forEach(function (x) { if (x < 0n) neg += 1; else if (x > 0n) pos += 1; });
    if (neg > pos) ints = ints.map(function (x) { return -x; });
    return ints;
  }
  var MEDIUM_SPECIES = { acidic: ['H+', 'H2O'], basic: ['OH-', 'H2O'], none: [] };
  function balanceEquation(text, options) {
    options = options || {};
    var eq0 = parseEquation(text);
    if (eq0.error) return { ok: false, error: eq0.error };
    var amb = ambiguousSpecies(eq0);
    if (amb.length && !options.readings) {
      // try every reading of the ambiguous ions; use the one that balances, and say so
      var combos = readingCombos(amb), results = [];
      for (var ci = 0; ci < combos.length; ci++) {
        var rr = balanceEquation(text, Object.assign({}, options, { readings: combos[ci] }));
        results.push(rr);
        if (rr.ok) {
          if (ci > 0) rr.readingNote = 'balanced under the other reading of an ambiguous ion: ' + readingNotes(parseEquation(text, combos[ci])).join('; ');
          else rr.readingNote = readingNotes(eq0).join('; ');
          var others = results.slice(0, ci).filter(function (x) { return x.ok; });
          if (others.length) rr.readingNote += '; another reading also balances: ' + others[0].balanced;
          return rr;
        }
      }
      results[0].readingNote = readingNotes(eq0).join('; ') + '; no reading of the ambiguous ions balances';
      return results[0];
    }
    var eq = parseEquation(text, options.readings);
    var species = [];
    eq.reactants.forEach(function (sp) { species.push({ formula: sp.formula, counts: sp.counts, charge: sp.charge, side: 0, given: true, errors: sp.errors, typeset: sp.typeset }); });
    eq.products.forEach(function (sp) { species.push({ formula: sp.formula, counts: sp.counts, charge: sp.charge, side: 1, given: true, errors: sp.errors, typeset: sp.typeset }); });
    var bad = species.filter(function (sp) { return sp.errors.length; });
    if (bad.length) return { ok: false, error: bad.map(function (sp) { return sp.formula + ': ' + sp.errors.join('; '); }).join(' · ') };
    var have = {}; species.forEach(function (sp) { have[normaliseFormula(sp.formula)] = true; });
    var extra = (MEDIUM_SPECIES[options.medium] || []).concat(options.halfReaction ? ['e-'] : []);
    var added = [];
    extra.forEach(function (f) { if (!have[normaliseFormula(f)]) { var pf = parseFormula(f); species.push({ formula: f, counts: pf.counts, charge: pf.charge, side: 0, given: false, errors: [], typeset: pf.typeset }); added.push(f); } });
    function solve(list) {
      var els = {}; list.forEach(function (sp) { Object.keys(sp.counts).forEach(function (e) { els[e] = 1; }); });
      var rows = Object.keys(els).sort().map(function (e) { return list.map(function (sp) { return fr(BigInt((sp.side === 0 ? 1 : -1) * (sp.counts[e] || 0))); }); });
      rows.push(list.map(function (sp) { return fr(BigInt((sp.side === 0 ? 1 : -1) * sp.charge)); }));
      return nullspace(rows, list.length);
    }
    var basis = solve(species);
    // with the medium's species added, try dropping each added species that is not needed
    if (basis.length > 1 && added.length) {
      for (var drop = 0; drop < added.length; drop++) {
        var trial = species.filter(function (sp) { return sp.given || sp.formula !== added[drop]; });
        var b2 = solve(trial);
        if (b2.length === 1) { species = trial; basis = b2; added = added.filter(function (f) { return f !== added[drop]; }); break; }
      }
    }
    var out = { ok: true, species: species.map(function (sp) { return { formula: sp.formula, given: sp.given, side: sp.side }; }), added: added, dimension: basis.length, medium: options.medium || 'none', halfReaction: !!options.halfReaction };
    if (basis.length === 0) { out.ok = false; out.error = 'the species given admit no balance: atoms or charge cannot be conserved with these alone' + (options.medium && options.medium !== 'none' ? ', even with ' + extra.join(' and ') : ' (for a reaction in water, choose acidic or basic; for a half-reaction, allow e-)'); return out; }
    if (basis.length > 1) { out.ok = false; out.error = 'the species admit ' + basis.length + ' independent reactions, so no single balance is determined; the basis is shown'; out.basis = basis.map(function (v) { return toIntegers(v).map(function (x) { return Number(x); }); }); return out; }
    var ints = toIntegers(basis[0]);
    var coef = ints.map(function (x) { return Number(x); });
    var moved = [], wrong = [];
    species.forEach(function (sp, i) {
      if (coef[i] < 0) { if (sp.given) wrong.push(sp.formula); else { sp.side = 1 - sp.side; coef[i] = -coef[i]; moved.push(sp.formula); } }
    });
    out.coefficients = species.map(function (sp, i) { return { formula: sp.formula, coefficient: coef[i], side: sp.side, given: sp.given }; });
    if (wrong.length) { out.ok = false; out.error = 'a balance exists only with ' + wrong.join(', ') + ' on the other side of the arrow; not rewritten'; return out; }
    var zero = species.filter(function (sp, i) { return coef[i] === 0 && sp.given; }).map(function (sp) { return sp.formula; });
    if (zero.length) out.note = 'takes no part: ' + zero.join(', ');
    var L = [], R = [];
    species.forEach(function (sp, i) { if (coef[i] === 0) return; var t = (coef[i] === 1 ? '' : coef[i] + ' ') + sp.formula; (sp.side === 0 ? L : R).push(t); });
    out.balanced = L.join(' + ') + ' → ' + R.join(' + ');
    var TL = [], TR = [];
    species.forEach(function (sp, i) { if (coef[i] === 0) return; var t = (coef[i] === 1 ? '' : coef[i] + ' ') + sp.typeset; (sp.side === 0 ? TL : TR).push(t); });
    out.typeset = TL.join(' + ') + ' → ' + TR.join(' + ');
    out.readAs = species.map(describeReading);
    var e = species.findIndex(function (sp) { return normaliseFormula(sp.formula) === 'e-'; });
    if (e >= 0 && coef[e]) out.electrons = { n: coef[e], side: species[e].side === 0 ? 'gained (reduction)' : 'lost (oxidation)' };
    out.check = checkEquation(out.balanced, options.readings);
    return out;
  }

  var MODE_BALANCE = {
    id: 'balance',
    title: 'Balance a chemical equation',
    status: DERIVED,
    statusNote: 'The algebraic method, exact: conservation of every element and of charge as a linear system over the species given, its nullspace computed in rational arithmetic, the smallest whole-number solution. Redox in water by adding H+/H2O or OH-/H2O; half-reactions by adding e-. Nothing is guessed: species that cannot balance are said to, and species that admit more than one reaction get the basis, not a choice.',
    description: 'Give the species: reactants → products, with charges as Fe3+, Cr2O7^2-, e-. Charges in any usual notation: Fe3+, Fe^3+, Fe{3+}, Fe(3+), Fe+3, Fe³⁺ or Fe(III); MnO4-, SO4^2-, SO4-2, SO4(2-), SO₄²⁻. A plain digit and sign after a single element symbol is the one ambiguous form (Fe3+ is iron(III), but N3- is azide and I3- triiodide): the mode reads it as a charge, shows every reading it made, and where that reading cannot balance and the other can it uses the other and says so. The mode balances by conservation of every element and of charge, exactly. For a redox reaction in water choose the medium: acidic adds H⁺ and H₂O, basic adds OH⁻ and H₂O, each only where needed and on whichever side the arithmetic puts it. A half-reaction allows e⁻, and the electrons transferred are reported. If the species admit no balance, or more than one, the mode says so and does not invent a species or pick a reaction. The result is then tallied by the equation check, so the balancer is checked by an instrument that is not itself.',
    inputs: [{ name: 'equation', label: 'species', type: 'textarea', default: 'MnO4- + Fe2+ → Mn2+ + Fe3+', help: 'reactants → products; spaces around +' },
             { name: 'medium', label: 'medium', type: 'select', default: 'acidic', options: [{ value: 'none', label: 'as written' }, { value: 'acidic', label: 'acidic (H⁺, H₂O)' }, { value: 'basic', label: 'basic (OH⁻, H₂O)' }] },
             { name: 'half', label: 'half-reaction', type: 'select', default: 'no', options: [{ value: 'no', label: 'no' }, { value: 'yes', label: 'yes: allow e⁻' }] }],
    source: { instrument: 'balanceEquation', file: 'public/script.js' },
    run: async function (values, ctx) {
      var r = balanceEquation(values.equation || '', { medium: values.medium, halfReaction: values.half === 'yes' });
      var rows = [];
      if (!r.ok) {
        if (r.basis) r.basis.forEach(function (v, i) { rows.push(row('basis ' + (i + 1), r.species.map(function (sp, j) { return v[j] ? v[j] + '·' + sp.formula : null; }).filter(Boolean).join(', '), DERIVED, 'a coefficient vector; a negative entry means the other side')); });
        if (r.readAs) r.readAs.forEach(function (d, i) { rows.push(row('read ' + r.species[i].formula, d, null, 'how the species was read')); });
        if (r.readingNote) rows.push(row('ambiguous ion', r.readingNote, DERIVED));
        return { rows: rows, ok: false, message: r.error };
      }
      rows.push(row('balanced', r.balanced, DERIVED, 'smallest whole-number coefficients; the species are typed, not a figure of the index'));
      rows.push(row('typeset', r.typeset, DERIVED));
      r.readAs.forEach(function (d, i) { rows.push(row('read ' + r.species[i].formula, d, null, r.species[i].given ? 'how the species was read' : 'added')); });
      if (r.readingNote) rows.push(row('ambiguous ion', r.readingNote, DERIVED, 'a plain digit and sign after one element symbol: Fe3+ is a charge, I3- a subscript; write the caret form to be explicit'));
      r.coefficients.forEach(function (c) { rows.push(row((c.side === 0 ? 'reactant ' : 'product ') + c.formula, c.coefficient, DERIVED, c.given ? undefined : 'added for the ' + r.medium + ' medium' + (normaliseFormula(c.formula) === 'e-' ? ' (electrons)' : ''))); });
      if (r.added.length) rows.push(row('added', r.added.join(', '), DERIVED, 'each on the side the arithmetic put it; none where not needed'));
      if (r.electrons) rows.push(row('electrons', r.electrons.n + ' ' + r.electrons.side, DERIVED, 'the half-reaction\'s transfer'));
      if (r.note) rows.push(row('note', r.note, DERIVED));
      var ck = r.check;
      rows.push(row('checked', ck.balanced ? 'the equation check tallies it as balanced' : 'THE EQUATION CHECK DOES NOT TALLY IT AS BALANCED', DERIVED, ck.atoms.map(function (a) { return a.element + ' ' + a.left + '→' + a.right; }).join(', ') + '; charge ' + ck.charge.left + '→' + ck.charge.right));
      return { rows: rows, ok: true, text: r.balanced };
    },
    selftest: async function () {
      var ck = new Checker();
      var co = function (text, opt) { var r = balanceEquation(text, opt || {}); return r.ok ? r.balanced : 'FAIL: ' + r.error; };
      ck.eq('H2 + O2 → H2O', co('H2 + O2 → H2O'), '2 H2 + O2 → 2 H2O');
      ck.eq('Fe + O2 → Fe2O3', co('Fe + O2 → Fe2O3'), '4 Fe + 3 O2 → 2 Fe2O3');
      ck.eq('C3H8 + O2 → CO2 + H2O', co('C3H8 + O2 → CO2 + H2O'), 'C3H8 + 5 O2 → 3 CO2 + 4 H2O');
      ck.eq('KMnO4 + HCl → KCl + MnCl2 + H2O + Cl2', co('KMnO4 + HCl → KCl + MnCl2 + H2O + Cl2'), '2 KMnO4 + 16 HCl → 2 KCl + 2 MnCl2 + 8 H2O + 5 Cl2');
      ck.eq('redox, acidic: permanganate and iron(II)', co('MnO4- + Fe2+ → Mn2+ + Fe3+', { medium: 'acidic' }), 'MnO4- + 5 Fe2+ + 8 H+ → Mn2+ + 5 Fe3+ + 4 H2O');
      ck.eq('redox, acidic: dichromate and iron(II)', co('Cr2O7^2- + Fe2+ → Cr3+ + Fe3+', { medium: 'acidic' }), 'Cr2O7^2- + 6 Fe2+ + 14 H+ → 2 Cr3+ + 6 Fe3+ + 7 H2O');
      ck.eq('redox, basic: permanganate and iodide', co('MnO4- + I- → MnO2 + I2', { medium: 'basic' }), '2 MnO4- + 6 I- + 4 H2O → 2 MnO2 + 3 I2 + 8 OH-');
      ck.eq('half-reaction: Fe2+ → Fe3+', co('Fe2+ → Fe3+', { halfReaction: true }), 'Fe2+ → Fe3+ + e-');
      ck.eq('half-reaction, acidic: permanganate reduction', co('MnO4- → Mn2+', { medium: 'acidic', halfReaction: true }), 'MnO4- + 8 H+ + 5 e- → Mn2+ + 4 H2O');
      var h = balanceEquation('MnO4- → Mn2+', { medium: 'acidic', halfReaction: true });
      ck.eq('and it reports five electrons gained', h.electrons.n + ' ' + h.electrons.side, '5 gained (reduction)');
      ck.eq('disproportionation, species given in full', co('Cl2 + OH- → Cl- + ClO3- + H2O'), '3 Cl2 + 6 OH- → 5 Cl- + ClO3- + 3 H2O');
      ck.eq('a non-redox equation in an acidic medium adds nothing', co('H2 + O2 → H2O', { medium: 'acidic' }), '2 H2 + O2 → 2 H2O');
      ck.eq('an added species lands on the side the arithmetic puts it', balanceEquation('MnO4- + I- → MnO2 + I2', { medium: 'basic' }).coefficients.filter(function (c) { return !c.given; }).map(function (c) { return c.formula + (c.side ? '→right' : '→left'); }).join(','), 'OH-→right,H2O→left');
      ck.eq('species that cannot balance are refused, not padded', balanceEquation('H2 → O2').ok, false);
      var amb = balanceEquation('C + O2 → CO + CO2');
      ck.eq('two independent reactions are reported as a basis, not chosen', (amb.ok === false) && amb.dimension === 2 && amb.basis.length === 2, true);
      ck.eq('a species that must cross the arrow is reported, not moved', /other side/.test(balanceEquation('H2O → H2 + O2 + H2O2').error || '') || balanceEquation('H2O → H2 + O2 + H2O2').dimension === 2, true);
      ck.eq('the balanced result passes the equation check', balanceEquation('Cr2O7^2- + Fe2+ → Cr3+ + Fe3+', { medium: 'acidic' }).check.balanced, true);
      ck.eq('an ambiguous ion is read the way that balances, and the reading is said: triiodide', (function () { var r = balanceEquation('I2 + I- → I3-'); return r.balanced + ' | ' + (/other reading/.test(r.readingNote || '')); })(), 'I2 + I- → I3- | true');
      ck.eq('sign-first and roman notations balance the same redox', co('Fe+2 + Ce(IV) → Fe(III) + Ce+3'), 'Fe+2 + Ce(IV) → Fe(III) + Ce+3');
      ck.eq('the typeset balance', balanceEquation('MnO4- + Fe2+ → Mn2+ + Fe3+', { medium: 'acidic' }).typeset, 'MnO₄⁻ + 5 Fe²⁺ + 8 H⁺ → Mn²⁺ + 5 Fe³⁺ + 4 H₂O');
      ck.eq('every species reports how it was read', balanceEquation('Fe3+ + e- → Fe2+').readAs.join(' | '), 'Fe³⁺: Fe 1, charge +3 | e⁻: no atoms, charge -1 | Fe²⁺: Fe 1, charge +2');
      return ck.result();
    }
  };

  var MODE_CHEM = {
    id: 'equation-check',
    title: 'Chemical equation check',
    status: DERIVED,
    statusNote: 'Deterministic: conservation of every element and of charge, checked over an equation another author wrote; each element linked to its record. The page writes no chemistry.',
    description: 'Paste a chemical equation (→, ->, = or ⇌; spaces around + signs; charges as Fe3+, SO4^2-, Fe(III), SO₄²⁻, e-; hydrates with ·). The mode shows how it read every species, tallies every element on each side and the charge, says whether the equation balances, and links each element to its record in the index. It does not balance the equation for you: a finding is recorded, never repaired.',
    inputs: [{ name: 'equation', label: 'equation', type: 'textarea', default: '2 H2 + O2 → 2 H2O', help: 'one equation' }],
    source: { instrument: 'checkEquation', file: 'public/script.js' },
    run: async function (values, ctx) {
      var r = checkEquation(values.equation || '');
      if (r.error) return fail(r.error);
      var rows = [];
      rows.push(row('typeset', r.typeset, null, 'as read'));
      r.readAs.forEach(function (d) { rows.push(row('read', d, null)); });
      r.atoms.forEach(function (a) {
        var e = ctx.index && ctx.index.layout ? ctx.index.layout.find(function (x) { return x.Z === a.Z; }) : null;
        rows.push(row(a.element + ' (Z = ' + (a.Z || '?') + ')', a.left + ' → ' + a.right + (a.ok ? '' : '  UNBALANCED'), DERIVED, e ? 'in the index: ' + (e.name || e.symbol) + (e.populated ? ', populated' : ', spectra rows only') : 'not an element of the index'));
      });
      rows.push(row('charge', r.charge.left + ' → ' + r.charge.right + (r.charge.ok ? '' : '  UNBALANCED'), DERIVED));
      rows.push(row('verdict', r.errors.length ? 'UNREADABLE: ' + r.errors.join('; ') : (r.balanced ? 'balanced' : 'NOT balanced'), DERIVED, r.notes.length ? r.notes.join('; ') : undefined));
      return { rows: rows, ok: true, text: r.balanced ? 'balanced' : 'not balanced' };
    },
    selftest: async function () {
      var ck = new Checker();
      ck.eq('2 H2 + O2 → 2 H2O balances', checkEquation('2 H2 + O2 → 2 H2O').balanced, true);
      ck.eq('Fe + Cl2 -> FeCl3 does not', checkEquation('Fe + Cl2 -> FeCl3').balanced, false);
      ck.eq('2 Fe + 3 Cl2 -> 2 FeCl3 does', checkEquation('2 Fe + 3 Cl2 -> 2 FeCl3').balanced, true);
      ck.eq('Ca(OH)2 + 2 HCl = CaCl2 + 2 H2O: brackets', checkEquation('Ca(OH)2 + 2 HCl = CaCl2 + 2 H2O').balanced, true);
      ck.eq('CuSO4·5H2O → CuSO4 + 5 H2O: hydrate', checkEquation('CuSO4·5H2O → CuSO4 + 5 H2O').balanced, true);
      ck.eq('Fe3+ + e- → Fe2+: charge balances', checkEquation('Fe3+ + e- → Fe2+').balanced, true);
      ck.eq('Fe3+ → Fe2+: charge does not', checkEquation('Fe3+ → Fe2+').charge.ok, false);
      ck.eq('Zn + 2 H+ → Zn2+ + H2 with unicode charges', checkEquation('Zn + 2 H⁺ → Zn²⁺ + H₂').balanced, true);
      ck.eq('MnO4^- + 8 H+ + 5 Fe2+ → Mn2+ + 5 Fe3+ + 4 H2O', checkEquation('MnO4^- + 8 H+ + 5 Fe2+ → Mn2+ + 5 Fe3+ + 4 H2O').balanced, true);
      ck.eq('an unknown symbol is an error, not a guess', checkEquation('Xx + O2 → XxO2').errors.length > 0, true);
      ck.eq('Fe3+ is a monatomic ion of charge 3; MnO4- a polyatomic ion of charge 1; O2^- needs the caret', [parseFormula('Fe3+').charge, parseFormula('MnO4-').charge, parseFormula('MnO4-').counts.O, parseFormula('O2^-').charge, parseFormula('O2^-').counts.O, parseFormula('Hg2^2+').charge].join(','), '3,-1,4,-1,2,2');
      ck.eq('every usual charge notation reads the same ion', ['Fe^3+', 'Fe{3+}', 'Fe(3+)', 'Fe+3', 'Fe³⁺', 'Fe(III)'].map(function (f) { return parseFormula(f).charge; }).join(','), '3,3,3,3,3,3');
      ck.eq('and for a polyatomic ion', ['SO4^2-', 'SO4-2', 'SO4(2-)', 'SO₄²⁻', 'SO4{2-}'].map(function (f) { var r = parseFormula(f); return r.charge + '/' + r.counts.O; }).join(','), '-2/4,-2/4,-2/4,-2/4,-2/4');
      ck.eq('a plain digit and sign after one symbol is ambiguous and both readings are kept', (function () { var r = parseFormula('I3-'); return r.charge + ',' + r.counts.I + ',' + r.ambiguous.alt.charge + ',' + r.ambiguous.alt.counts.I + ',' + r.ambiguous.alt.typeset; })(), '-3,1,-1,3,I₃⁻');
      ck.eq('the check tries the other reading: I2 + I- → I3- balances as triiodide', (function () { var r = checkEquation('I2 + I- → I3-'); return r.balanced + '|' + (r.notes.some(function (n) { return /other reading/.test(n); })); })(), 'true|true');
      ck.eq('the typeset form', checkEquation('2 Fe3+ + Sn2+ → 2 Fe2+ + Sn4+').typeset, '2 Fe³⁺ + Sn²⁺ → 2 Fe²⁺ + Sn⁴⁺');
      ck.eq('phase labels are read and dropped', checkEquation('NaCl(aq) → Na+(aq) + Cl-(aq)').balanced, true);
      ck.eq('no arrow is refused', !!checkEquation('H2 + O2 H2O').error, true);
      ck.eq('the elements of an equation are listed with Z', checkEquation('2 H2 + O2 → 2 H2O').atoms.map(function (a) { return a.element + a.Z; }).join(','), 'H1,O8');
      // the answer checker, over fixtures
      var data = { 'el/26/symbol': { value: 'Fe', status: 'READ' }, 'el/26/channels/0/delta_equation': { value: 1.3456, status: 'PINNED' }, 'index/closure/E': { value: 36, status: 'PINNED' } };
      var resolve = function (p) { return data[p] || null; };
      var compute = function (name, args) { if (name === 'pauli_bound') return pauliBound(args[0], args[1], args[2]); if (name === 'nothing') return null; return undefined; };
      var r = checkAnswer('Iron ⟦el/26/symbol⟧ has E = 36 ⟦index/closure/E⟧ and δ = 1.346 ⟦el/26/channels/0/delta_equation⟧, not 2.0 ⟦el/26/channels/9/delta_equation⟧; B: ⟪pauli_bound(3, 4, 0) = 3⟫, wrong ⟪pauli_bound(3, 4, 0) = 2⟫, ⟪nothing(1) = 1⟫, ⟪unknown(1) = 1⟫; ⦃2 H2 + O2 → 2 H2O⦄ and the model\'s own 42.', resolve, compute);
      ck.eq('citations: string cited, two numeric matches, one not found', r.citations.map(function (c) { return c.verdict; }).join('|'), 'cited|matches|matches|not in the index');
      ck.eq('a differing figure is reported, not repaired', checkAnswer('E = 35 ⟦index/closure/E⟧', resolve, compute).citations[0].verdict, 'DIFFERS');
      ck.eq('computations: agrees, differs, not computable, unknown', r.computations.map(function (c) { return c.verdict; }).join('|'), 'agrees|DIFFERS|not computable from the loaded data|unknown function');
      ck.eq('equations: balanced', r.equations[0].verdict, 'balanced');
      ck.eq('the model\'s own number is counted unverified, and a formula\'s subscript is not a number', r.unverified, 1);
      ck.eq('a number within 30 characters before a citation counts as covered', checkAnswer('E is 36 (thirty-six) ⟦index/closure/E⟧', resolve, compute).unverified, 0);
      var ans = 'The frequency is 2.7 GHz ⟨⟨https://arxiv.org/abs/1203.5425⟩⟩ ⟨⟨https://doi.org/10.1038/nature10260⟩⟩ and 5 ⟨⟨no source given⟩⟩.\nRETRIEVAL\ntarget | route type | source | result | value\nfrequency | primary | Nature 475, 484 (2011) doi 10.1038/nature10260 | blocked | \nfrequency | compilation | arXiv:1203.5425 Table XII | open | 2.7 GHz\nfrequency | citing paper | https://arxiv.org/abs/1308.1711 | open | 2.7 GHz\nmass | database | https://physics.nist.gov/asd | open | 5\nEdlen 1964 | review | | untried | ';
      var rr = checkAnswer(ans, resolve, compute, ['https://arxiv.org/abs/1203.5425', 'https://arxiv.org/abs/1308.1711']);
      ck.eq('web sources: a DOI and an arXiv id are identifiers, a bare phrase is not', rr.sources.map(function (x) { return x.identifier ? x.identifier.kind : 'none'; }).join(','), 'arxiv,doi,none');
      ck.eq('web sources: one among the searches, one not, one without identifier', rr.sources.map(function (x) { return x.verdict; }).join(' | '), 'among this session\'s searches | NOT among this session\'s searches | no identifier');
      ck.eq('retrieval: five rows parsed, the header skipped', rr.retrieval.rows.length, 5);
      ck.eq('retrieval: route types read from the words', rr.retrieval.rows.map(function (r) { return r.route; }).join(','), 'primary,compilation,citing,database,review');
      ck.eq('retrieval: the frequency closes on two open routes, the mass is fragile, the review is not retrieved', rr.retrieval.targets.map(function (t) { return t.target + ':' + t.rho + ':' + t.verdict; }).join(' | '), 'frequency:2:closes on two routes | mass:1:FRAGILE: one route | Edlen 1964:0:not retrieved: a stated gap');
      ck.eq('retrieval: an open route not among the searches is flagged', rr.retrieval.rows[3].verdict, 'open, NOT among this session\'s searches');
      ck.eq('retrieval: the table is not counted as unverified numbers', rr.unverified <= 1, true);
      ck.eq('without a search list the sources are unverifiable here, not wrong', checkAnswer('x ⟨⟨https://example.org⟩⟩', resolve, compute).sources[0].verdict, 'unverifiable here');
      return ck.result();
    }
  };

  SOLVERS = [MODE_EQUATION, MODE_PAULI, MODE_COLLAPSE, MODE_CLOSURE, MODE_LAMBDA, MODE_COEFFICIENT, MODE_RELATIVISTIC, MODE_MUCF, MODE_CHEM, MODE_BALANCE];
  LIB = {
    channelDelta: channelDelta, channelTerms: channelTerms, collapseC: collapseC, pauliBound: pauliBound,
    coreP: coreP, n0Of: n0Of, orderClosure: orderClosure, lambdaConstraints: lambdaConstraints,
    capsNeeded: capsNeeded, withinCaps: withinCaps, invertCoefficient: invertCoefficient,
    atomSolve: atomSolve, drift: drift, equationReport: equationReport,
    coefficients: coefficients, collapseParams: collapseParams, channelRows: channelRows,
    measuredRowsAll: measuredRowsAll, presetCells: presetCells, cellsText: cellsText, parseCells: parseCells,
    janetCypherFixture: janetCypherFixture, lambdaCypherFixture: lambdaCypherFixture,
    label: label, roman: roman, FALLBACK_COEF: FALLBACK_COEF, COEF_NAMES: COEF_NAMES,
    parseFormula: parseFormula, checkEquation: checkEquation, checkAnswer: checkAnswer, balanceEquation: balanceEquation, SYMBOL_Z: SYMBOL_Z
  };

if (typeof window !== 'undefined') { window.MI = window.MI || {}; window.MI.solvers = SOLVERS; window.MI.solverLib = LIB; }
if (typeof module !== 'undefined') module.exports = { SOLVERS: SOLVERS, LIB: LIB };
})();
