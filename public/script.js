/* The Method Index — a zoomable reading of the index.
 *
 * The explorer computes nothing. Every number it shows is tools/populate.py's,
 * written by tools/webindex.py into data/, and the page draws it with the
 * status the corpus gives it. A status is never flattened. The solver suite
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

  const state = {
    index: null,
    layout: 'table',
    frames: new Map(),              // Z -> {x, y, cx, cy}
    ghosts: [],                     // {p, g, x, y, def}
    heliumAt: 18,                   // 18 (section 6, IUPAC) or 2 (Register 448's priced alternative)
    bounds: { x0: 0, y0: 0, x1: 1, y1: 1 },
    elements: new Map(),            // Z -> record
    trees: new Map(),               // Z -> {ions: [...]} with relative frames
    pending: new Map(),             // Z -> promise
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
          put(e.Z, 1, 0);                 // helium drawn at group 2 (Register 448's alternative)
        } else {
          put(e.Z, e.group - 1, e.period - 1);
        }
      }
      // the cells R admits and the layout does not hold, each with section 6.1.1's definition
      const defs = new Map((c.denied_cells || []).map((d) => [`${d.p},${d.g}`, d]));
      const denied = state.layout === 'table' ? (he2 ? c.placement.helium_at_2.denied : c.denied) : [];
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
      s.src = `${DATA}elements/${Z}.js`;
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
  // Λ_spectra drawn as the record draws it — the Index of Indices' Figure 6, the Löwdin paper's
  // Figure 1(b), and the record's own renderer (spectra-lattice.html): element across,
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
    const grade = node ? node.rec.grade : cb.grade;
    const byLimit = state.cellColor === 'limit' && node;
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
      if (grade === 'measured' && node && node.rec.witness === 'witnessed' && r >= 4) {
        ctx.beginPath(); ctx.arc(p0.x, p0.y, r * 1.3, 0, Math.PI * 2);
        ctx.strokeStyle = C.measured; ctx.lineWidth = 1; ctx.stroke();
      }
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
        const col = cb.node ? cellColour(cb.node) : (cb.grade === 'measured' ? C.measured : C.exact);
        const hot = scene.kind === 'element' ? selMatchesCube(sel, cb) : (sel && sel.kind !== 'root' && sel.Z === cb.Z);
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
      else html = `<b>Section 6</b> · ${c.held} held · ${c.admitted} admitted by ℛ · E = ${state.heliumAt === 2 && c.placement ? c.placement.helium_at_2.E + ' with helium at group 2' : c.E}`;
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
    if (node.kind === 'root') return state.layout === 'lattice' ? 'lattice' : 'plane';
    if (node.kind === 'ghost') return 'plane';
    return state.elementView === 'lattice' ? 'lattice' : 'plane';
  }
  function enterView(node) {
    const v = viewFor(node), prev = state.view;
    state.view = v;
    const lg = $('#legend-lattice'); if (lg) lg.hidden = v !== 'lattice';
    if (v !== 'lattice') return v;
    if (node.kind === 'root') {
      if (!state.scene || state.scene.kind !== 'index') { state.scene = buildIndexScene(); state.orbit = orbitHome(); if (state.scene) fitOrbit(state.scene, state.orbit); }
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
    return `${pathText(node)}. The Method 1.6, read by tools/populate.py and written by tools/webindex.py; commit ${m.commit || '?'}, built ${m.built || '?'}. Sources: ${src}. ${location.origin && location.origin !== 'null' ? location.origin : ''}${location.pathname}${hashOf(node)}`;
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

  // Register 448's alternative placement: helium at group 2, E = 20. The frames are rebuilt
  // from the build's own two closures; nothing is recomputed here.
  function setHelium(at) {
    if (at === state.heliumAt) return;
    state.heliumAt = at;
    buildFrames();
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
  // E = admitted − held carries one status wherever the corpus's own figure is quoted: PINNED, as
  // docs/POPULATE.md's table pins the structural half (90 held, 126 admitted, E = 36) and as
  // cypher.py's selftest asserts it; the closure solver's own E over any cell set is the same row.
  const E_TIP = 'admitted − held; section 6 against ℛ (section 32.4.1), the structural half docs/POPULATE.md pins';

  function renderRoot() {
    const ix = state.index, t = ix.totals, c = ix.closure;
    const lat = ix.lattice;
    const layoutNote = state.layout === 'lattice' && lat
      ? `Λ_spectra as a lattice, the way the record draws it (Index of Indices, Figure 6): every element a slab at its Z, ionisation stage up, ℓ into the page — <b>${lat.sites.toLocaleString()}</b> sites, <b>${lat.known.length.toLocaleString()}</b> known cells (${lat.counts.measured} measured, ${lat.counts.exact} exact) drawn as cubes, the rest the faint body of each slab. The measured wedge sits at low Z and low ℓ. Drag to rotate, wheel or pinch to zoom, tap a slab for its element.`
      : state.layout === 'table'
      ? `Section 6's drawn layout: <b>${c.held}</b> cells held, <b>${c.admitted}</b> admitted by ℛ, <b>E = ${c.E}</b>. The ${c.E} are the gaps in the short periods, drawn as tinted ghosts each labelled with the subshell section 6.1.1 names it; ${c.set_aside} f-block elements are set aside below the table.`
      : `Register 1188's coordinate: Janet's cell is (n+ℓ, ℓ) of the differentiating electron, and on it E = 0. Elements without a cell (Z &gt; 108) sit on the bottom row.`;
    return `<div class="kind">the index</div>
      <h2 class="node-title">${esc(ix.meta.title)}</h2>
      <p class="node-sub">${esc(ix.meta.subtitle)}</p>
      <p class="note">${layoutNote}</p>
      <div class="stats">
        <div class="stat"><b>${t.populated}</b><span>elements populated ${badge('DERIVED', 'count of the elements LW1-ground.py carries')}</span></div>
        <div class="stat"><b>${t.csv_only}</b><span>spectra rows only (Z 109–120) ${badge('DERIVED', 'count of the elements COORDINATES-2.13 carries beyond LW1-ground.py')}</span></div>
        <div class="stat"><b>${t.rows.toLocaleString()}</b><span>channel cells ${badge('READ', 'COORDINATES-2.13 rows')}</span></div>
        <div class="stat"><b>${t.measured}</b><span>measured ${badge('DERIVED', 'count over COORDINATES-2.13\'s grade column')}</span></div>
        <div class="stat"><b>${t.exact}</b><span>exact ${badge('DERIVED', 'count over COORDINATES-2.13\'s grade column')}</span></div>
        <div class="stat"><b>${t.computed.toLocaleString()}</b><span>computed ${badge('DERIVED', 'count over COORDINATES-2.13\'s grade column')}</span></div>
      </div>
      ${section('How to read it', `<p class="note">Tap any element: its ions appear inside it in spectroscopic order (I is neutral), joined by the Λ₈ ionisation ladder; each ion opens into its ℓ channels, each channel into its cells, one per multiplicity, coloured by grade. Every value in this plate carries the status the corpus gives it: ${Object.keys(ix.status_legend || {}).map((s) => badge(s)).join(' ')}. The explorer computes nothing; the solver suite below does, and every solver carries a selftest.</p>`)}
      ${section('Closure of this layout', `<div class="fields">
        ${row('index', esc(c.index), 'PINNED', 'section 6', true)}
        ${row('operator', esc(c.operator), 'PINNED', 'section 32.4.1', true)}
        ${row('held', c.held, 'PINNED', 'section 6: ninety main-table cells')}
        ${row('admitted', c.admitted, 'PINNED', 'ℛ over the layout')}
        ${row('E', c.E, 'PINNED', E_TIP)}
        ${c.decomposition ? row('the thirty-six', `${c.decomposition.forbidden} forbidden by ℓ ≤ n−1 (1d, 1p, 2d) + ${c.decomposition.deferred} deferred (3d, and helium's slot)`, 'READ', 'section 6.1.1; Register 448 — tap a ghost for its definition') : ''}
        ${c.placement ? row('helium at 2 instead', `E = ${c.placement.helium_at_2.E}, priced at ${c.placement.priced} cells`, 'READ', c.placement.source) : ''}
        ${row('set aside', c.set_aside, 'PINNED', 'the lanthanides and actinides, section 6')}
      </div>${c.placement && state.layout === 'table' ? `<div class="actions"><button type="button" data-act="helium-toggle">${state.heliumAt === 2 ? 'Draw helium at group 18 (section 6)' : 'Draw helium at group 2 (E = ' + c.placement.helium_at_2.E + ')'}</button></div>` : ''}`)}
      ${(() => { const rel = ix.relativistic, lim = ix.limits; if (!rel && !lim) return ''; let b = ''; if (rel) { const paper = (rel.sources || {}).paper || {}; b += `<div class="fields">${row('displaced at c → ∞', esc((rel.eleven || []).map((x) => x.symbol).join(', ')), 'READ', `${(paper.file || '').split('/').pop()} L${paper.eleven_line}; register 1706`, true)}${row('instrument', 'not held — the construction is record-carried; nothing here computes it', null, esc((rel.instrument && rel.instrument.budget) || ''), true)}${rel.walk && rel.walk.summary && rel.walk.summary.compare ? row('the walk, reconstructed', esc(`${rel.walk.summary.compare.displaced.length} displaced at c → ∞ in the ${rel.walk.primary === 'hf' ? 'Hartree–Fock' : 'local-exchange'} field (${rel.walk.summary.compare.displaced.map((d) => d.symbol).join(', ') || 'none'}); ${rel.walk.summary.compare.in_eleven.length} of the record's eleven`), 'RECONSTRUCTED', 'tools/lowdin_walk.py over LOWDIN-WALK.tsv: the record\'s construction rebuilt from its statement; placed beside the record, never in its place', true) : ''}</div>`; } if (lim) { b += `<p class="note" style="margin-top:8px">Every cell carries the bound the csv records; by kind: ${(lim.kinds || []).map((k) => `<span class="dot dot-lim-${k.kind}"></span>${esc(LIMIT_LABEL[k.kind] || k.kind)} ${k.count.toLocaleString()}`).join(' · ')} ${badge('DERIVED', 'kind by the stated rule; the note is READ')}</p><div class="actions"><button type="button" data-act="color-limit">Colour cells by limit</button><button type="button" data-act="color-grade">by grade</button></div>`; } return section('The relativistic limit and the bounds', b); })()}
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
        ? `<p class="note">Helium sits at group 18 in the drawn layout, and the cell it vacates — period 1, group 2 — carries ℓ = 0, which satisfies ℓ ≤ n − 1 = 0. So this cell is deferred, not forbidden: it could hold an element, and the only reason it holds none is where helium is drawn. That is also why 1p contributes five cells and not six. Register 448 prices the choice: with helium at group 2, E falls from 36 to 20.</p>`
        : `<p class="note">Group ${node.g} carries ℓ = 2 (d), and period ${node.p} gives n = ${d.n}, so this is a ${esc(d.subshell)} cell and ℓ = 2 ≤ n − 1 = ${d.n - 1} holds: the orbital exists. It stands empty because the Madelung order fills 3d after 4s, so the ten 3d elements are drawn in period 4. Real, and deferred: one of the eleven cells that could hold an element and do not.</p>`)
      : `<p class="note">ℛ, the order operator, admits this cell: the layout has a period ${node.p} and a group ${node.g}, so the downward closure of the held set reaches it. Section 6's table does not hold it.</p>`;
    return `<div class="kind">${kindLine}</div>
      <h2 class="node-title">${title}</h2>
      <p class="node-sub">one of the ${c.E} cells that make E = ${c.E}${state.heliumAt === 2 ? ' · drawn with helium at group 2 (E = ' + (pl ? pl.helium_at_2.E : '?') + ')' : ''}</p>
      ${defn}
      ${d ? section('Definition', `<div class="fields">
        ${row('cell', `(${node.p}, ${node.g})`, 'DERIVED', 'admitted − held')}
        ${row('subshell', esc(d.subshell), 'READ', 'section 6.1.1: the thirty-six decompose as subshells of their rows; ℓ by group from Transitions.md L368')}
        ${row('n, ℓ', `${d.n}, ${d.l} (${LSYM[d.l]})`, 'DERIVED', 'n is the period; ℓ is fixed by the group')}
        ${row('ℓ ≤ n − 1', d.class === 'forbidden' ? '<span class="bad">fails</span>' : '<span class="ok">holds</span>', 'PINNED', 'section 7.1, the hydrogenic radial solution')}
        ${row('class', d.class, 'DERIVED', 'from the bound; the totals 25 + 11 are READ (section 6.1.1, Register 448) and the derivation is asserted against them')}
        ${row('why', esc(d.reason), null, undefined, true)}
      </div>`) : ''}
      ${section('The thirty-six', `<div class="fields">
        ${row('forbidden by ℓ ≤ n−1', dec.forbidden !== undefined ? `${dec.forbidden} — 1d (10), 1p (5), 2d (10)` : '—', 'READ', 'section 6.1.1; Register 448: 25 + 11, not 26 + 10, and the discrepancy is helium')}
        ${row('real but deferred', dec.deferred !== undefined ? `${dec.deferred} — 3d (10), and period 1 group 2` : '—', 'READ', 'section 6.1.1')}
        ${row('held', c.held, 'PINNED', 'section 6')}
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
        <div class="actions"><button type="button" data-act="helium-toggle">${state.heliumAt === 2 ? 'Draw helium at group 18 (section 6)' : 'Draw helium at group 2 (E = ' + pl.helium_at_2.E + ')'}</button></div>`, badge('READ', 'Register 448')) : ''}
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
        ${row('the record\'s renderer', `cubes of edge ${(lat.cube || {}).known || 0.86} known, ${(lat.cube || {}).faint || 0.3} unmeasured`, 'READ', ((lat.cube || {}).note || '') + '; drawn here as nodes of the same footprint, in the nested view\'s marks')}
      </div>
      <div class="actions"><button type="button" data-act="lattice-view">${on ? 'Rotate it on the canvas' : 'Open the lattice'}</button><button type="button" data-act="nest-view">${state.elementView === 'nest' ? 'Nested circles (shown)' : 'Show as nested circles'}</button></div>`);
  }
  function relSection(e, rec) {
    const rel = state.index.relativistic;
    if (!rel) return '';
    return relRecordSection(e, rel) + walkSection(e, rec, rel);
  }

const WALK_FIELD_LABEL = { hf: 'Hartree–Fock, non-local exchange (the record\'s field, rebuilt)', lx: 'local exchange (Hartree–Fock–Slater)' };
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
        ${c1 && c1.observed_gain !== '-' ? row('observed gain at this Z', `${esc(c1.observed_gain)} — the c = 137 entrant ${c1.agree === 'yes' ? 'agrees' : 'differs'}`, 'READ', 'LW1-ground.py (register 1306): the channel that gained an electron from Z − 1 to Z. The chain never moves an electron, so a rearranged step (Cr, Cu, Pd, La, Gd, Th …) reads as a disagreement under this reading') : ''}
      </div>`;
    }
    body += `<div class="fields">${e.relativistic ? row('in the record', 'one of the eleven register 1706 displaces', 'READ', 'THE-LOWDIN-SOLUTION-2.md; register 1706') : row('in the record', 'not among the eleven', 'READ', 'register 1706')}</div>
      <p class="note">${esc(caveat('walk-reconstructed'))}</p>`;
    return section('The walk, reconstructed', body, badge('RECONSTRUCTED', `${walk.instrument} over ${walk.table.file}, md5 ${walk.table.md5.slice(0, 12)}; primary field ${walk.primary}`));
  }

  function relRecordSection(e, rel) {
    const src = rel.sources || {}, paper = src.paper || {};
    const cite = `${(paper.file || 'THE-LOWDIN-SOLUTION-2.md').split('/').pop()} L${paper.eleven_line}; register 1706; r2-scf.out`;
    const hit = (rel.eleven || []).find((x) => x.Z === e.Z);
    const fig = (state.index.figures || [])[0];
    let body = `<div class="fields">
      ${row('displaced at c → ∞', hit ? `yes <span class="rel-tag">one of the eleven</span>` : 'no', 'READ', hit ? cite : cite + ': not among the eleven')}
      ${hit ? row('observed configuration', esc(hit.configuration || '—'), 'READ', 'r2-scf.out over LW1-ground.py (register 1306)') : ''}
      ${hit ? row('entrant channel', esc(hit.entrant || '—'), 'READ', 'r2-scf.out: the channel the relativistic walk enters at this Z') : ''}
      ${e.Z === 90 && rel.thorium ? row('thorium', esc(rel.thorium), 'READ', `${(paper.file || '').split('/').pop()} L${paper.thorium_line}`, true) : ''}
      ${row('c', rel.c, 'READ', esc(rel.construction || 'the one admitted constant'))}
      ${row('instrument', 'not held — nothing computed here', null, esc((rel.instrument && rel.instrument.note) || ''), true)}
    </div>`;
    if (hit || e.Z === 90) {
      body += `<div class="callout is-plain">${esc(rel.statement || '')}</div>`;
      if (fig && fig.file) body += `<figure class="plate-fig"><img src="data/${esc(fig.file)}" alt="${esc(fig.caption || 'Figure 5')}" loading="lazy"><figcaption>${esc(fig.caption || '')} · md5 ${esc((fig.md5 || '').slice(0, 12))} as extracted/LEDGER.tsv records ${badge('READ', 'the figure as the extracted tree holds it')}</figcaption></figure>`;
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
      ${row('name', esc(e.name || '—'), null, 'IUPAC label; not a corpus figure', true)}
    </div>`);
    html += section('Layout', `<div class="fields">
      ${axRow('period', e.period, 'period')}
      ${axRow('group', e.set_aside ? 'set aside' : e.group, 'group')}
      ${axRow('block', esc(e.block || '—'), 'block')}
      ${axRow('Janet cell (n+ℓ, ℓ)', e.janet ? `(${e.janet[0]}, ${e.janet[1]})` : '—', 'janet cell')}
      ${rec ? row('cell held', rec.closure.cell_held ? 'yes' : (e.set_aside ? 'set aside' : 'no'), 'PINNED', 'section 6 against ℛ') : ''}
      ${rec && rec.closure.denied_in_this_period.length ? row('denied in this period', `groups ${rec.closure.denied_in_this_period.join(', ')}`, 'DERIVED', 'admitted − held, this period') : ''}
    </div>`);
    html += latticeSection(e, rec);
    if (rec) {
      html += section('Configuration', `<div class="tbl-wrap"><table class="t"><thead><tr><th>subshell</th><th class="num">n</th><th class="num">ℓ</th><th class="num">occ</th><th class="num">cap</th><th class="num">n+ℓ</th><th>full</th></tr></thead><tbody>
        ${rec.configuration.map((c) => `<tr><td>${esc(c.subshell)}</td><td class="num">${c.n}</td><td class="num">${c.l}</td><td class="num">${c.occupancy}</td><td class="num">${c.capacity}</td><td class="num">${c['n+l']}</td><td>${c.full ? '●' : '○'}</td></tr>`).join('')}
      </tbody></table></div>`, `${badge('READ', 'shells: LW1-ground.py, register 1306')} ${badge('DERIVED', 'n, ℓ, occupancy, n+ℓ')} ${badge('PINNED', 'capacity 2(2ℓ+1), section 7.1')}`);
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
        ${Object.entries(s.coords).map(([k, v]) => row(k, v === null ? '— (not carried)' : v, v === null ? null : 'RECONSTRUCTED', v === null ? 'the ion\'s term is not carried, so 2S may not be inferred (§7.1)' : (cm[k] || 'Λ₈ coordinate'))).join('')}
      </div>
      <div class="tbl-wrap" style="margin-top:8px"><table class="t"><thead><tr><th>constraint (§7.1)</th><th>holds</th><th>origin</th></tr></thead><tbody>
        ${s.constraints.map((c) => `<tr><td>${esc(c.rule)}</td><td class="${c.holds ? 'ok' : 'holds-false'}">${c.holds ? 'holds' : 'fails'}</td><td class="plain" style="font-family:var(--font-body)">${esc(c.origin)}${c.rule === '2S <= k' && s.coords['2S'] === null ? ' — 2S not carried; probed as 0, as populate.py does' : ''}</td></tr>`).join('')}
      </tbody></table></div>
      <div class="fields" style="margin-top:8px">
        ${row('within §7.4 caps', Object.entries(s.within_caps).map(([k, v]) => `${esc(k)}:${v ? '✓' : '✗'}`).join(' '), 'PINNED', (axisStatus('caps') || {}).source)}
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
  // What the corpus itself states of the binders and particles beyond the electron, and every
  // outward identifier it prints. Both blocks are read from data/index.js, where the generator
  // parsed each figure out of the passage that states it; the page prints them with their
  // statuses and links only what an identifier the corpus prints resolves to.
  const siteText = (s) => s ? `${(s.file || '').split('/').pop()} L${s.line}` : '';
  const quoteBlock = (s) => s && s.quote ? `<blockquote class="q">${esc(s.quote)} <span class="cite-inline">${esc(siteText(s))}</span></blockquote>` : '';
  const ext = (url, text) => `<a href="${esc(url)}" target="_blank" rel="noopener noreferrer">${esc(text)}</a>`;

  function renderParticles() {
    const pt = state.index.particles, rf = state.index.references || {};
    if (!pt) { $('#particles-body').innerHTML = '<p class="note">data/index.js carries no particles block.</p>'; return; }
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
      <p class="note">Rows of PROSE-ONLY.tsv: statements the chat export holds and no file does. A row is a candidate for a home, not a figure of the corpus.</p>
      <div class="tbl-wrap"><table class="t"><thead><tr><th>id</th><th>kind</th><th>label</th><th>confidence</th></tr></thead><tbody>
        ${pt.prose_only.map((r) => `<tr><td>${esc(r.id)}</td><td>${esc(r.category)}</td><td class="wrap">${esc(r.label)}<div class="note" style="margin-top:4px">${esc(r.quote)}</div></td><td>${esc(r.confidence)}</td></tr>`).join('')}
      </tbody></table></div>`;
    const ab = pt.absent.terms;
    html += `<h3>Counted absent</h3>
      <p class="note">${badge(pt.absent.status)} ${esc(pt.absent.note)}: ${Object.keys(ab).map((t) => `<b>${esc(t)}</b> ${ab[t].occurrences}${ab[t].first ? ` (first at ${esc(siteText(ab[t].first))})` : ''}`).join(' · ')}.</p>`;
    if (rf.nist_asd) html += `<p class="note">Outward: ${ext(rf.nist_asd.url, 'NIST ASD')} · ${ext(rf.nist_asd.doi_url, 'DOI ' + rf.nist_asd.doi)} · the References dialog lists every arXiv and DOI identifier the corpus prints.</p>`;
    const body = $('#particles-body');
    body.innerHTML = html;
    body.querySelectorAll('[data-act="mucf-mode"]').forEach((b) => b.addEventListener('click', () => { $('#dlg-particles').close(); openSolver('mucf'); }));
  }

  function renderReferences() {
    const rf = state.index.references;
    if (!rf) { $('#references-body').innerHTML = '<p class="note">data/index.js carries no references block.</p>'; return; }
    const n = rf.nist_asd, ss = rf.spectra_sources || { rows: [], by_species: {} };
    const cites = (e) => e.cites.map((c) => `<div class="note"><span class="cite-inline">${esc(c.file.split('/').pop())} L${c.line}</span> ${esc(c.text)}</div>`).join('');
    let html = `<p class="note">${esc(rf.note)}</p>`;
    html += `<h3>The data source the corpus links itself</h3>
      <div class="fields">
        ${row('database', ext(n.url, n.name), 'READ', 'the citation as the main volume prints it', true)}
        ${row('DOI', ext(n.doi_url, n.doi), 'READ', 'as printed', true)}
        ${row('the query', esc(n.query_not_held), null, 'LW1-README.md', true)}
      </div>${n.cited_for.map(quoteBlock).join('')}`;
    html += `<h3>The spectra compilations, by species (B.1)</h3>
      <p class="note">Which compilation each measured species' levels were drawn from, as section B.1 of the Spectra Compendium prints it. Only NIST ASD carries an identifier the corpus prints, so only it is linked.</p>
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

  // the source behind a measured cell, linked only where the corpus prints the target
  function cellSourceLink(node, m) {
    const rf = state.index.references || {};
    const n = rf.nist_asd, bs = (rf.spectra_sources || {}).by_species || {};
    const src = m.source || '';
    if (/^NIST ASD/.test(src) && n) return { text: `NIST ASD (ver. 5.12) — the retrieval the source column names`, url: n.url, doi: n.doi_url, status: 'READ', note: 'the corpus prints the database and its DOI; the query itself is not held' };
    if (src === 'captured levels') {
      const key = `${symbolOf(node.Z)} ${roman(node.charge)}`;
      const hit = Object.keys(bs).find((k) => k === key || k.startsWith(key + ' ('));
      if (hit) return { text: `${bs[hit].compilation} (B.1: ${hit})`, url: bs[hit].url, doi: bs[hit].url && n ? n.doi_url : null, status: 'READ', note: `Spectra Compendium B.1 L${bs[hit].line}` };
      return { text: 'captured levels — the compilation is not named for this species in B.1', url: null, status: null, note: 'no target is invented' };
    }
    if (/Theodosiou/.test(src)) return { text: 'Theodosiou, Manson & Inokuti 1986, PRA 34, 943 — a journal reference, no identifier printed', url: null, status: 'READ', note: 'cited as a string' };
    if (/R 1627/.test(src)) return { text: 'read from the species\' own level files at register 1627', url: null, status: 'READ', note: 'the record\'s own files' };
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
      ${row('ground configuration', `${ext(n.url, 'NIST ASD ver. 5.12')} · ${ext(n.doi_url, 'DOI ' + n.doi)}`, 'READ', 'LW1-ground.py (register 1306): read, not computed; the query itself is not held', true)}
      ${kinds.size ? row('measured cells\' sources', [...kinds].map(([k, v]) => `${esc(k)} (${v})`).join(' · '), 'READ', 'COORDINATES-2.13, source column; each cell\'s plate resolves its compilation', true) : ''}
    </div>`);
  }
  function openSolver(id) {
    const sel = document.querySelector('#solver-body select');
    if (!sel) return;
    const reg = window.MI && Array.isArray(window.MI.solvers) ? window.MI.solvers : [];
    const i = reg.findIndex((m) => m.id === id);
    if (i >= 0 && i < sel.options.length) { sel.selectedIndex = i; sel.dispatchEvent(new Event('change')); }
    try { $('#solvers').scrollIntoView({ behavior: reduced ? 'auto' : 'smooth', block: 'start' }); } catch (err) { /* no scroll */ }
  }

  // ---------------------------------------------------------------- provenance
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
        <div class="stat"><b>${t.populated}</b><span>elements populated (LW1-ground.py)</span></div>
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
        ${col ? row('collapse C(Z, ℓ)', esc(col.form), col.status, 'registers 1188–1190; inverted out of the computed column') : ''}
        ${col ? row('Z₀(ℓ)', Object.entries(col.Z0).map(([l, z]) => `ℓ=${esc(l)}: ${esc(z)}`).join(' · '), col.status, 'the Janet block openings') : ''}
        ${ix.caps ? row('§7.4 caps', Object.entries(ix.caps).map(([k, v]) => `${esc(k)}≤${esc(v)}`).join(' '), 'PINNED', 'section 7.4') : ''}
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
      dragged = false; last = { x: ev.clientX, y: ev.clientY };
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
          if (ev.shiftKey) { o.dx = (o.dx || 0) + dx; o.dy = (o.dy || 0) + dy; }
          else { o.ry += dx * 0.008; o.rx = Math.max(-1.45, Math.min(1.45, o.rx + dy * 0.008)); }
          state.orbit = o;
        } else { state.cam.tx += dx; state.cam.ty += dy; state.anim = null; }
        last = { x: ev.clientX, y: ev.clientY };
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
        if (ev.key === 'ArrowUp') o.rx = Math.max(-1.45, o.rx - 0.12); if (ev.key === 'ArrowDown') o.rx = Math.min(1.45, o.rx + 0.12);
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
    $('#btn-particles').addEventListener('click', () => { if (!$('#particles-body').innerHTML) renderParticles(); $('#dlg-particles').showModal(); });
    $('#btn-references').addEventListener('click', () => { if (!$('#references-body').innerHTML) renderReferences(); $('#dlg-references').showModal(); });
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
    const foot = `<span><b>The Method Index</b> — an index of The Method 1.6.</span>
      <span>Data generated by <span class="mono">tools/webindex.py</span> over <span class="mono">tools/populate.py</span>; every value carries the status the corpus gives it, and the explorer computes nothing.</span>
      ${commit ? `<span>Edition <span class="mono">${esc(commit)}</span>, built ${esc(built)}.</span>` : ''}
      <button type="button" class="ghost" data-act="open-prov">Provenance and sources</button>`;
    for (const id of ['#foot', '#side-foot']) {
      const el = $(id);
      if (!el) continue;
      el.innerHTML = foot;
      el.querySelectorAll('[data-act="open-prov"]').forEach((b) => b.addEventListener('click', () => $('#dlg-provenance').showModal()));
    }
  }

  function setLayout(mode) {
    if (mode === state.layout) return;
    state.layout = mode;
    document.querySelectorAll('.seg-btn[data-layout]').forEach((b) => b.classList.toggle('is-on', b.dataset.layout === mode));
    buildFrames();
    if (mode !== 'lattice' && state.scene && state.scene.kind === 'index') state.scene = null;
    const sel = state.selected || rootNode;
    if (sel.kind === 'ghost' && mode !== 'table') select(rootNode, { reveal: false });
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
  particles           what the corpus states of the binders and particles beyond the electron
  particle <term>     one of them: muon, pion, tau, antimatter, positronium, antiprotonic, photon, quark, boson, neutrino …
  references [term]   every arXiv and DOI identifier the corpus prints, or those whose citing line mentions <term>
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
        const pt = ix.particles; if (!pt) return 'no particles block in data/index.js';
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
        const pt = ix.particles; if (!pt) return 'no particles block in data/index.js';
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
        Object.keys(pt.absent.terms).forEach((t) => { if (term.includes(t.toLowerCase())) { const a = pt.absent.terms[t]; out.push(`${t}: ${a.occurrences ? a.occurrences + ' occurrences, first at ' + a.first.file + ' L' + a.first.line : 'absent from the corpus — counted at build, not a cell of the lattice'} ${st(pt.absent.status)}`); } });
        return out.length ? out.join('\n') : `nothing in the particles block matches "${term}"` + (flat.toLowerCase().includes(term) ? ' by name, though the term occurs in a passage; open Particles' : '');
      }
      case 'references': case 'refs': {
        const rf = ix.references; if (!rf) return 'no references block in data/index.js';
        const term = toks.slice(1).join(' ').toLowerCase();
        const pick = (list) => list.filter((e) => !term || e.id.toLowerCase().includes(term) || e.cites.some((c) => c.text.toLowerCase().includes(term) || c.file.toLowerCase().includes(term)));
        const ax = pick(rf.arxiv), dx = pick(rf.doi);
        const line = (e) => `  ${e.url}  (${e.n} site${e.n === 1 ? '' : 's'}; ${e.cites[0].file.split('/').pop()} L${e.cites[0].line})`;
        return [`NIST ASD ${rf.nist_asd.url}  DOI ${rf.nist_asd.doi_url} ${st('READ')} — the one data source the corpus links itself; the query is not held`,
          `arXiv (${ax.length}${term ? ' matching' : ''}):`, ...ax.map(line), `DOI (${dx.length}${term ? ' matching' : ''}):`, ...dx.map(line),
          `B.1 compilations by species: ${Object.keys(rf.spectra_sources.by_species).length} species; only NIST ASD is linked`].join('\n');
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
        const lines = [`${rel.statement || ''} ${st('READ')}`, `source: ${paper.file || ''} L${paper.eleven_line}; register 1706; r2-scf.out`, ''];
        for (const x of rel.eleven || []) lines.push(`${x.symbol.padEnd(3)} Z=${String(x.Z).padEnd(4)} ${(x.configuration || '').padEnd(24)} entrant ${x.entrant || '?'}`);
        if (rel.thorium) lines.push('', rel.thorium);
        lines.push('', `instrument: not held — ${(rel.instrument && rel.instrument.note) || ''}`, (rel.instrument && rel.instrument.budget) || '');
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
            lines.push(`${String(i + 1).padStart(2)}. ${roman(s.charge).padEnd(6)} ${s.from} → ${s.to}  (${s.cell.map((v) => v === null ? '·' : v).join(', ')})  §7.1 ${s.constraints.length - fails.length}/${s.constraints.length}  ${within ? 'within §7.4' : `OUTSIDE §7.4: needs ${need}`}`);
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
    return `You are answering a question about ONE record of The Method Index (The Method 1.6, read by tools/populate.py and serialised by tools/webindex.py). Strict rules:
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
      try { c.body.textContent = await consoleAnswer(q); } catch (err) { c.body.textContent = `console error: ${err.message}`; }
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
  function setupSolvers() {
    const body = $('#solver-body'), count = $('#solver-count');
    const reg = window.MI && Array.isArray(window.MI.solvers) ? window.MI.solvers : null;
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
    $('#layout-table').title = `Section 6: period × group. ${cl.held} held, ${cl.admitted} admitted, E = ${cl.E}`;
    $('#layout-janet').title = `Register 1188: (n+ℓ, ℓ). E = ${jan ? jan.E : '?'}`;
    const fills = { held: cl.held, admitted: cl.admitted, E: cl.E, janetE: jan ? jan.E : '?' };
    document.querySelectorAll('[data-fill]').forEach((el) => { const v = fills[el.dataset.fill]; if (v !== undefined) el.textContent = String(v); });
    buildFrames();
    resize();
    renderProvenance();
    setupSearch(); setupPointer(); setupKeys(); setupChrome(); setupAssistant(); setupClaude(); setupSolvers(); setupEdition();
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
 * and of tools/cypher.py (class Index + op_order, R of section 32.4.1), in the
 * same order of floating-point operations, plus the coefficient calculator
 * engineered on the channel equation.
 *
 * ES2019, no DOM access, no imports. Every row that carries a number carries
 * the status the corpus gives it -- READ, PINNED, DERIVED, RECOVERED or
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
  var WALK_FIELD_LABEL = { hf: 'Hartree–Fock, non-local exchange (the record\'s field, rebuilt)', lx: 'local exchange (Hartree–Fock–Slater)' };

  // Register 1205's coefficients, digit for digit, used only when
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
      ? fallback.join(', ') + ' not carried by index.equation; register 1205\'s values ' +
        fallback.map(function (k) { return k + ' = ' + FALLBACK_COEF[k]; }).join(', ') +
        ' used, as tools/populate.py pins them'
      : 'A, E0, E1, K, H read from index.equation (' + (eq.source || 'register 1205') + ')';
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
  // populate.pauli_bound: B = max(0, min(p, n0 - l - 1)); register 1141.
  function pauliBound(p, n0, l) {
    return Math.max(0, Math.min(p, n0 - l - 1));
  }

  // ----------------------------------- Lambda_8: section 7.1 and section 7.4
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
      out.code = 'Ne = 1 (register 5193)';
      out.reason = 'Ne = 1: the (Ne-1)/Ne factor vanishes identically, so no coefficient moves ' +
                   'the channel (register 5193)' +
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
      if (r.Ne === 1) { excluded.push({ row: r, why: 'Ne = 1 (register 5193)' }); return; }
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
        ck.eq('hydrogenic channel Z=' + Z + ' l=' + l + ' returns exactly 0 (register 5193)',
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
      ck.eq('equation report: rms 0.1809 (4 dp, docs/POPULATE.md)', Number(rep.rms.toFixed(4)), 0.1809);
      ck.eq('equation report: R2 0.9656 (4 dp)', Number(rep.R2.toFixed(4)), 0.9656);
      ck.eq('equation report: median |error| 0.0587 (4 dp)', Number(rep.median_abs_error.toFixed(4)), 0.0587);
      ck.notes.push('no ctx.index.fixtures.equation_report; held against the figures docs/POPULATE.md records to 4 dp');
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
                          (caveat(ctx.index, 'above-108') || 'LW1-ground.py stops at Z = 108') +
                          (rec.note ? ' (' + rec.note + ')' : '')) };
    }
    return { rec: rec };
  }

  // 1. channel-equation ---------------------------------------------------
  var MODE_EQUATION = {
    id: 'channel-equation',
    title: 'The channel equation',
    status: PINNED,
    statusNote: 'Register 1205\'s final form of the channel equation, as tools/populate.py channel_delta computes it; its p = 0 branch carries the RECOVERED collapse ramp.',
    description: 'Values one Rydberg channel (Z, stage, l) of a populated element by the channel equation, term by term: the charge factor ln(c+1)/c, the exponent e(Ne) = E0 - E1 ln Ne, p^e, Ne^K and C(Z) where the branch needs it. The result is set beside the delta_equation the exporter wrote, with their difference, and beside every measured row of the channel with its residual. Nothing is fitted; the coefficients are register 1205\'s.',
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
        pSource = 'core_p over the observed configuration of the core, ' + coreRec.symbol + ' (register 1306)';
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
        rows.push(row('A', coef.A, PINNED, 'register 1205'));
      } else {
        rows.push(row('C(Z, l)', C, RECOVERED, 'the collapse ramp, registers 1188 to 1190; not stated in any member'));
        rows.push(row('(Ne-1)/Ne', t.ratio, DERIVED, Ne === 1 ? 'vanishes identically at Ne = 1 (register 5193): the hydrogenic channel is exactly zero' : undefined));
        rows.push(row('Ne^K', t.nk, DERIVED, 'K = ' + coef.K));
        rows.push(row('H', coef.H, PINNED, 'register 1205'));
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
    statusNote: 'Register 1141: B = min(p, n0 - l - 1), Pauli 1925 and Janet 1929; n0\'s reading is RECONSTRUCTED.',
    description: 'B = max(0, min(p, n0 - l - 1)) for a channel. p is the core\'s orbital count at this l and n0 the first entirely unoccupied n; both are taken from the selected channel\'s record unless typed. n0\'s reading is a reconstruction: register 1141 names the term but not whether a partly filled subshell counts, and He I ns settles it for "first entirely unoccupied n". Where the record carries the CSV\'s B the two are set side by side and a disagreement is recorded, not repaired.',
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
      rows.push(row('p', p, pSrc === 'typed' ? null : PINNED, pSrc === 'typed' ? 'typed, not a corpus figure' : pSrc + ' (register 1141)'));
      rows.push(row('n0', n0, nSrc === 'typed' ? null : RECONSTRUCTED, nSrc === 'typed' ? 'typed, not a corpus figure' : nSrc + '; first entirely unoccupied n at this l'));
      rows.push(row('l', l, ch ? READ : null, ch ? 'the channel\'s l' : 'typed'));
      rows.push(row('n0 - l - 1', n0 - l - 1, DERIVED));
      rows.push(row('B = max(0, min(p, n0 - l - 1))', B, PINNED, 'register 1141'));
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
      ck.eq('He I ns: B = 1 (register 1141, populate.selftest)', pauliBound(heCh.p, heCh.n0, 0), 1);
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
    statusNote: 'Registers 1188 to 1190 state the thresholds and that it is "one lookup, not fitted"; the form was inverted out of COORDINATES-2.13\'s computed column and no member states it.',
    description: function (ctx) {
      var p = collapseParams(ctx.index), ls = Object.keys(p.Z0).sort();
      return 'C(Z, l) = clamp(0.5 + (Z - Z0(l)) / ' + p.width + ', 0, 1), a ramp ' + p.width + ' wide reaching exactly 0.5 at the Janet block opening Z0 = ' +
             ls.map(function (l) { return p.Z0[l]; }).join(', ') + ' for l = ' + ls.join(', ') + (p.fromIndex ? ' (index.collapse)' : ' (populate.py\'s own values; index.collapse absent)') +
             '. It is RECOVERED, not PINNED: the index agrees with it exactly but no member writes it down. Above l = ' + ls[ls.length - 1] + ' every channel inverts to C = 0 and there is no ramp to show.';
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
      rows.push(row('Z0(l = ' + l + ')', z0, RECOVERED, l === 2 ? 'register 1188: the n+l = 5 block opens at Z = 21 (Sc)' : l === 3 ? 'register 1188: the n+l = 7 block opens at Z = 57 (La)' : 'boron, where the 2p block opens: the same rule, stated nowhere'));
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
      // set_aside false; they are not main-table cells of section 6.
      lay.forEach(function (e) {
        if (e.Z > 118 || e.set_aside || e.period === null || e.group === null || e.period === undefined || e.group === undefined) return;
        var k = e.period + ',' + e.group;
        if (!seen[k]) { seen[k] = true; out.push([e.period, e.group]); }
      });
      return { name: 'periodic', coords: ['period', 'group'], cells: out.sort(function (a, b) { return a[0] - b[0] || a[1] - b[1]; }),
               index: 'periodic table (period x group), section 6: the elements Z <= 118 not set aside' };
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
  function lambdaCypherFixture() {         // cypher._lambda: the 976 cells at section 7.4's caps
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
    statusNote: 'R, the order operator of section 32.4.1, as tools/cypher.py op_order runs it (matching the seated instrument rclose.py).',
    description: function (ctx) {
      var c = (ctx.index && ctx.index.closure) || null, j = ((ctx.index && ctx.index.fixtures && ctx.index.fixtures.closure) || {}).janet || null;
      return 'Runs R over a set of cells: the alphabets are the distinct values per coordinate, the ambient set their product, phi(i, j, a) = max{ y_i : y in X, y_j <= a }, and a cell is admitted when x_i <= phi(i, j, x_j) for every pair. Reports the cells held, the cells admitted, E = admitted - held and the denied cells.' +
             (c ? ' On the drawn periodic layout section 6\'s ' + c.held + ' cells give ' + c.admitted + ' admitted and E = ' + c.E + ' (index.closure)' : '') +
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
        row('E = admitted - held', res.E, PINNED, 'admitted - held, section 32.4.1; ' + (res.E === 0 ? 'R admits nothing the set does not hold' : res.E + ' cells R admits and the set denies'))
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
        ck.eq('periodic: the 36 denied are section 6\'s (p1,g2..g17), (p2,g3..g12), (p3,g3..g12)', denied, want36);
        if (ctx.index.closure && ctx.index.closure.denied) ck.eq('periodic: denied = index.closure.denied', denied, ctx.index.closure.denied);
        // Register 448: E is placement-sensitive -- helium moved from (1, 18) to (1, 2) and
        // nothing else, E falls from 36 to 20; the build's own figure is the fixture
        var moved = per.cells.filter(function (c) { return !(c[0] === 1 && c[1] === 18); }).concat([[1, 2]]);
        var r2 = orderClosure(moved);
        var want2 = fx && fx.helium_at_2 ? fx.helium_at_2 : { held: 90, admitted: 110, E: 20 };
        ck.eq('helium at group 2: held', r2.held.length, want2.held);
        ck.eq('helium at group 2: E = 20 (Register 448)', r2.E, want2.E);
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
      ck.eq('Lambda_8 at section 7.4\'s caps: 976 cells (cypher._lambda)', lam.length, 976);
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
    title: 'A Lambda_8 cell against section 7',
    status: RECONSTRUCTED,
    statusNote: 'Section 7.1\'s seven constraints and section 7.4\'s caps are PINNED; the mapping of an element to cells (the ionisation ladder) is RECONSTRUCTED, and a typed cell carries no status of its own.',
    description: 'Tests one cell (n, l, k, q, e, f, g, 2S) against the seven constraints of section 7.1, each with its origin, and against section 7.4\'s caps (n, e, l, k, f) = (3, 3, 1, 3, 1). A cell can satisfy all seven and still lie outside the caps; that is reported OUTSIDE with the caps it needs, never truncated. 2S may be left blank, and is then probed as 0 exactly as tools/populate.py does.',
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
      var rows = [row('cell (n, l, k, q, e, f, g, 2S)', '(' + cell.map(function (v) { return v === null ? '-' : v; }).join(', ') + ')', null, 'typed, not a corpus figure' + (cell[7] === null ? '; 2S blank, probed as 0' : ''))];
      var held = 0;
      cons.forEach(function (c) { if (c.holds) held += 1; rows.push(row(c.rule, c.holds ? 'holds' : 'FAILS', PINNED, c.origin + ' (section 7.1)')); });
      rows.push(row('constraints held', held + '/7', PINNED));
      var over = [];
      CAP_AXES.forEach(function (ax) {
        if (!(ax in within)) return;
        if (!within[ax]) over.push(ax);
        rows.push(row('cap ' + ax + ' <= ' + caps[ax], within[ax] ? 'within' : 'OUTSIDE', PINNED, 'needs ' + ax + ' >= ' + need[ax] + ' (section 7.4)'));
      });
      rows.push(row('verdict at section 7.4\'s caps', over.length ? 'OUTSIDE: needs ' + over.map(function (ax) { return ax + '>=' + need[ax]; }).join(', ') : 'within 7.4', PINNED,
                    held === 7 && over.length ? 'satisfies all seven constraints and is still not a cell of Lambda_8 at these caps: section 7.4\'s point' : undefined));
      var cv = caveat(ctx.index, 'lambda8-mapping');
      if (cv) rows.push(row('caveat', cv));
      return { rows: rows, ok: true };
    },
    selftest: async function (ctx) {
      var ck = new Checker(), caps = capsOf(ctx.index);
      var inside = [1, 0, 1, 0, 1, 0, 0, 0];      // TOWER.L8()[0]
      ck.ok('the first cell of L8 satisfies all seven constraints', lambdaConstraints(inside).every(function (c) { return c.holds; }));
      ck.eq('section 7.1 states seven constraints', lambdaConstraints(inside).length, 7);
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
      rows.push(row(inv.coefficient + ' pinned', inv.pinned, PINNED, 'register 1205'));
      return rows;
    }
    if (inv.e_solved !== undefined) {
      rows.push(row('e solved (ln(d / (A Ne^K cf)) / ln p)', inv.e_solved, DERIVED));
      rows.push(row('e pinned (E0 - E1 ln Ne)', inv.e_pinned, PINNED));
    }
    rows.push(row(inv.coefficient + ' solved', inv.value, DERIVED, 'closed form, every other coefficient held pinned' + (inv.sign_note ? '; ' + inv.sign_note : '')));
    rows.push(row(inv.coefficient + ' pinned', inv.pinned, PINNED, 'register 1205'));
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
      row(res.coefficient + ' pinned', res.pinned, PINNED, 'register 1205'),
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
    statusNote: 'Engineered on register 1205\'s channel equation: the five pinned constants A, E0, E1, K (p > 0) and H, K (p = 0), solved back out of the READ deltas of COORDINATES-2.13\'s measured channels.',
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
  // is the paper's own result, register 1706 and the SCF audit's table, all READ.
  var MODE_RELATIVISTIC = {
    id: 'relativistic',
    title: 'The relativistic limit (c = 137 against c → ∞)',
    status: READ,
    statusNote: 'THE-LOWDIN-SOLUTION-2.md and register 1706: the observed table is irreducibly relativistic. The record\'s construction is not held: the Löwdin project\'s reply of 2026-09-18 (drive/The Method Materials/LOWDIN-DELIVERY-1/LW1-ADDENDUM-REPLY.md, md5 8df39014bb91387d79f358c63982a930) locates the c → ∞ path in LOWDIN-HANDOFF-103.tgz, which was never delivered, and the project has since concluded. So the mode reads the record\'s result (READ) and, beside it, carries a RECONSTRUCTION: tools/lowdin_walk.py runs the record\'s own algorithm — the V^{N−1} chain with the Koelling–Harmon equation — in a local-exchange field, at both settings, into LOWDIN-WALK.tsv. The reconstruction is never the record\'s number; where the two disagree, the disagreement is the measurement.',
    description: 'Quantum mechanics supplies the range of configurations; the speed of light, entering once as c = 137 through the scalar-relativistic reduction of the Dirac equation, decides which of them the observed table holds. Repeated with c sent to infinity, the record\'s construction misplaces eleven elements and inverts the channel competition at thorium. That construction is not held, so this mode reports the paper\'s own result, READ, and refuses to recompute its c → ∞ table. What it can show beside the record is the reconstructed walk (RECONSTRUCTED): the same chain, run here in a field that is not the record\'s, with its entrant, runner-up, margin and candidate spectrum at every Z at both settings, and the reconstruction\'s own list of displaced elements measured against register 1706\'s eleven.',
    inputs: [sel('Z'),
             { name: 'operation', label: 'operation', type: 'select', default: 'element',
               options: [{ value: 'element', label: 'is this element displaced at c → ∞? (the record)' },
                         { value: 'walk', label: 'this element in the reconstructed walk, both settings' },
                         { value: 'eleven', label: 'the eleven, with their entrant channels (the record)' },
                         { value: 'compare', label: 'the reconstruction against the record' },
                         { value: 'recompute', label: 'recompute the c → ∞ table' }] }],
    source: { instrument: 'lowdin_construction', file: 'method/members/THE-LOWDIN-SOLUTION-2.md',
              also: ['walk_scan_hf', 'walk_scf_hf', 'walk_hf_operator', 'walk_solve_inh', 'walk_scan', 'walk_frontier', 'walk_solve', 'walk_integrate', 'walk_potentials', 'walk_scf'] },
    run: async function (values, ctx) {
      var rel = ctx.index && ctx.index.relativistic;
      if (!rel) return fail('this build of data/index.js carries no relativistic block (run python3 tools/webindex.py)');
      var op = values.operation || 'element', rows = [];
      var src = rel.sources || {}, paper = src.paper || {};
      var cite = (paper.file || 'THE-LOWDIN-SOLUTION-2.md') + ' L' + paper.eleven_line + '; register 1706; r2-scf.out';
      var inst = rel.instrument || {};
      var walk = rel.walk;
      var wcite = walk ? walk.instrument + ' over ' + walk.table.file + ' (md5 ' + walk.table.md5.slice(0, 12) + ')' : '';
      var fmt6 = function (v) { return (v === null || v === undefined) ? '—' : v.toFixed(6); };
      if (op === 'recompute') {
        rows.push(row('c → ∞ table', 'not computable here', null, inst.note || 'the construction is not held'));
        rows.push(row('why', 'the record\'s scalar-relativistic construction (Koelling–Harmon Hartree–Fock, c = 137) and its repetition at c → ∞ are not held; session 104 was never sealed and LOWDIN-HANDOFF-103.tgz never arrived', null, inst.budget || ''));
        (inst.readme_rows || []).forEach(function (l, i) { rows.push(row('LW1-README row ' + (i + 1), l, null, 'the delivery README, a seated member')); });
        rows.push(row('what is held', 'the paper\'s statement, register 1706 and the SCF audit\'s table of the eleven', READ, cite));
        if (walk && walk.summary && walk.summary.compare) {
          var cp = walk.summary.compare;
          rows.push(row('the walk, reconstructed', 'a c → ∞ table exists here as a reconstruction, not the record\'s: Z = ' + cp.Z_first + ' to ' + cp.Z_last + ' at both settings, in ' + Object.keys(walk.fields || { lx: 1 }).length + ' field(s); the primary is ' + (walk.primary || 'lx'), RECONSTRUCTED, wcite));
          rows.push(row('field (primary)', walk.field, RECONSTRUCTED, 'what the reconstruction is; not reproduced: ' + walk.not_reproduced));
          rows.push(row('displaced in the reconstruction', cp.displaced.length ? cp.displaced.map(function (d) { return d.symbol + ' (' + d.entrant_c137 + ' | ' + d.entrant_cinf + ')'; }).join(', ') : 'none', RECONSTRUCTED, 'entrants that differ between c = 137.035999 and c → ∞'));
          rows.push(row('against the record\'s eleven', cp.in_eleven.length + ' displaced here too' + (cp.in_eleven.length ? ' (' + cp.in_eleven.join(', ') + ')' : '') + '; ' + cp.eleven_not_displaced.length + ' not' + (cp.eleven_not_displaced.length ? ' (' + cp.eleven_not_displaced.join(', ') + ')' : '') + '; ' + cp.not_in_eleven.length + ' displaced here and not in the record' + (cp.not_in_eleven.length ? ' (' + cp.not_in_eleven.join(', ') + ')' : ''), RECONSTRUCTED, 'register 1706 against ' + walk.table.file));
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
          rows.push(row(lab + ': entrant = observed gain', s.agree + ' of ' + s.scored, RECONSTRUCTED, 'differentiating-electron reading over LW1-ground.py; disagreements: ' + (s.disagree.map(function (d) { return d.symbol + '(' + d.entrant + '≠' + d.observed_gain + ')'; }).join(' ') || 'none')));
          rows.push(row(lab + ': chain configuration identical to observed', s.cfg_identical + ' of ' + Math.min(s.rows, 107), RECONSTRUCTED, 'the chain never moves an electron'));
          rows.push(row(lab + ': g channels', s.g_pins.map(function (g) { return g.channel + ' offered at ' + g.offered + ', max |D + 1/(2n²)| ' + g.max_dev.toExponential(2); }).join('; '), RECONSTRUCTED, 'the record: 5g 65, 6g 70, 7g 57, 8g 28 elements, −1/(2n²) to storage precision'));
          rows.push(row(lab + ': smallest margins', s.smallest_margins.map(function (m) { return m.symbol + ' ' + m.entrant + ' over ' + m.runner_up + ' by ' + fmt6(m.margin); }).join('; '), RECONSTRUCTED, 'the record\'s contested rows: Z = 38, 56, 72, 89, 105'));
          if (s.not_converged.length) rows.push(row(lab + ': NOT CONVERGED', s.not_converged.join(' '), RECONSTRUCTED, 'rows whose field did not converge'));
        });
        var fieldsCmp = sm.fields || (cmp ? { lx: cmp } : {});
        Object.keys(fieldsCmp).sort().forEach(function (fld) {
          var c = fieldsCmp[fld], pre = 'field ' + fld + ': ';
          rows.push(row(pre + 'displaced at c → ∞', c.displaced.length ? c.displaced.map(function (d) { return d.symbol + ' (' + d.entrant_c137 + ' | ' + d.entrant_cinf + ')'; }).join(', ') : 'none', RECONSTRUCTED, 'entrants differ between the two settings'));
          rows.push(row(pre + 'the record\'s eleven', c.eleven_1706.join(', '), READ, 'register 1706'));
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
        rows.push(row('element', recw.symbol + ' (Z = ' + Zw + ')', READ, 'LW1-ground.py (register 1306)'));
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
        if (prim && prim.c137 && prim.c137.observed_gain !== '-') rows.push(row('observed gain at this Z', prim.c137.observed_gain + ' — the primary field\'s c = 137 entrant ' + (prim.c137.agree === 'yes' ? 'agrees' : 'differs'), READ, 'LW1-ground.py: the channel that gained an electron from Z − 1 to Z; the chain never moves an electron'));
        var inEleven = rel.eleven.some(function (e) { return e.Z === Zw; });
        rows.push(row('in the record', inEleven ? 'one of the eleven register 1706 displaces' : 'not among the eleven', READ, cite));
        return { rows: rows, ok: true, walk: wr, primary: walk.primary, text: caveat(ctx.index, 'walk-reconstructed') || '' };
      }
      if (op === 'eleven') {
        rows.push(row('elements displaced at c → ∞', rel.eleven.length, READ, cite));
        rel.eleven.forEach(function (e) {
          rows.push(row(e.symbol + ' (Z = ' + e.Z + ')', (e.configuration || '') + ' → entrant ' + (e.entrant || '?'), READ, 'r2-scf.out: the eleven in the observed table, over LW1-ground.py'));
        });
        if (rel.thorium) rows.push(row('thorium', rel.thorium, READ, (paper.file || '') + ' L' + paper.thorium_line));
        rows.push(row('instrument', 'not held — nothing computed here', null, inst.note || ''));
        return { rows: rows, ok: true, text: 'Register 1706: ' + ((src.register && src.register.text) || '') };
      }
      var Z = int(values.Z);
      if (Z === null || Z < 1 || Z > 120) return fail('Z must be an integer from 1 to 120');
      var got = await elementOrFail(ctx, Z);
      if (got.fail) return got.fail;
      var rec = got.rec, hit = null;
      for (var i = 0; i < rel.eleven.length; i++) if (rel.eleven[i].Z === Z) hit = rel.eleven[i];
      rows.push(row('element', rec.symbol + ' (Z = ' + Z + ')', READ, 'LW1-ground.py (register 1306)'));
      rows.push(row('displaced at c → ∞', hit ? 'yes' : 'no', READ, cite + (hit ? '' : ': not among the eleven')));
      if (hit) {
        rows.push(row('observed configuration', hit.configuration || '—', READ, 'r2-scf.out over LW1-ground.py'));
        rows.push(row('entrant channel', hit.entrant || '—', READ, 'r2-scf.out: the channel the relativistic walk enters at this Z'));
      }
      if (Z === 90 && rel.thorium) rows.push(row('thorium', rel.thorium, READ, (paper.file || '') + ' L' + paper.thorium_line));
      if (!rec.populated) rows.push(row('note', 'above Z = 108 the construction\'s 107-row table does not reach; the record carries csv rows only', null));
      rows.push(row('c', rel.c, READ, rel.construction || 'the one admitted constant'));
      rows.push(row('instrument', 'not held — nothing computed here', null, inst.budget || ''));
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
      // Th is a collapse-criterion row (register 1703) and the null-difference control. A c switch
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
      ck.ok('Figure 5 is carried with the md5 extracted/LEDGER.tsv records', figs.length > 0 && figs.every(function (f) { return f.ok; }), figs.length, 1);
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
        ck.eq('the summary\'s eleven are the paper\'s eleven, in order', cp.eleven_1706.join(','), rel.eleven.map(function (e) { return e.symbol; }).join(','));
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
      if (caseName === 'custom') { omega_s = num(values.omega_s); if (omega_s === null || omega_s <= 0) return fail('type ω_s as a positive fraction, or pick a case'); oStatus = null; oNote = 'typed, not a corpus figure'; }
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

  SOLVERS = [MODE_EQUATION, MODE_PAULI, MODE_COLLAPSE, MODE_CLOSURE, MODE_LAMBDA, MODE_COEFFICIENT, MODE_RELATIVISTIC, MODE_MUCF];
  LIB = {
    channelDelta: channelDelta, channelTerms: channelTerms, collapseC: collapseC, pauliBound: pauliBound,
    coreP: coreP, n0Of: n0Of, orderClosure: orderClosure, lambdaConstraints: lambdaConstraints,
    capsNeeded: capsNeeded, withinCaps: withinCaps, invertCoefficient: invertCoefficient,
    atomSolve: atomSolve, drift: drift, equationReport: equationReport,
    coefficients: coefficients, collapseParams: collapseParams, channelRows: channelRows,
    measuredRowsAll: measuredRowsAll, presetCells: presetCells, cellsText: cellsText, parseCells: parseCells,
    janetCypherFixture: janetCypherFixture, lambdaCypherFixture: lambdaCypherFixture,
    label: label, roman: roman, FALLBACK_COEF: FALLBACK_COEF, COEF_NAMES: COEF_NAMES
  };

if (typeof window !== 'undefined') { window.MI = window.MI || {}; window.MI.solvers = SOLVERS; window.MI.solverLib = LIB; }
if (typeof module !== 'undefined') module.exports = { SOLVERS: SOLVERS, LIB: LIB };
})();
