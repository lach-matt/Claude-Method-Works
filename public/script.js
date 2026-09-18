/* The Method Index — a zoomable reading of the index.
 *
 * Nothing here computes a value. Every number is tools/populate.py's, written
 * by tools/webindex.py into data/, and the page draws it with the status the
 * corpus gives it. A status is never flattened.
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
    ghosts: [],                     // {p, g, x, y}
    bounds: { x0: 0, y0: 0, x1: 1, y1: 1 },
    elements: new Map(),            // Z -> record
    trees: new Map(),               // Z -> {ions: [...]} with relative frames
    pending: new Map(),             // Z -> promise
    selected: null,                 // node
    cam: { k: 1, tx: 0, ty: 0 },
    anim: null,
    colors: {},
    lastHash: '',
  };

  // ---------------------------------------------------------------- helpers
  const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const fmt = (v, nd = 4) => (v === null || v === undefined) ? '—' : (typeof v === 'number' && !Number.isInteger(v) ? v.toFixed(nd) : String(v));
  const LSYM = 'spdfghik';
  const reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

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
    state.colors = {
      bg: g('--canvas-bg'), grid: g('--canvas-grid'), text: g('--canvas-text'), muted: g('--canvas-text-muted'),
      surface: g('--surface'), line: g('--line'), lineStrong: g('--line-strong'), accent: g('--accent'),
      measured: g('--measured'), exact: g('--exact'), computed: g('--computed'), ghost: g('--ghost'), csv: g('--csv'),
      blk: { s: g('--blk-s'), p: g('--blk-p'), d: g('--blk-d'), f: g('--blk-f'), none: g('--blk-none') },
    };
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
    if (state.layout === 'table') {
      for (const e of L) {
        if (e.set_aside) {
          const lan = e.Z <= 71;
          put(e.Z, (lan ? e.Z - 58 : e.Z - 90) + 3, lan ? 8.5 : 9.5);
        } else {
          put(e.Z, e.group - 1, e.period - 1);
        }
      }
      for (const [p, g] of state.index.closure.denied) {
        state.ghosts.push({ p, g, x: (g - 1) * CELL, y: (p - 1) * CELL });
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
    const r = (0.66 * R) / Math.sqrt(n);
    const Re = R - r;
    const golden = Math.PI * (3 - Math.sqrt(5));
    const pos = [];
    for (let i = 0; i < n; i++) {
      const rr = Re * Math.sqrt((i + 0.5) / n);
      const a = i * golden;
      pos.push({ x: rr * Math.cos(a), y: rr * Math.sin(a) });
    }
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
    const ions = charges.map((c, i) => {
      const chans = byCharge.get(c).slice().sort((a, b) => a.l - b.l);
      const ion = {
        kind: 'ion', Z, charge: c, dx: pk.pos[i].x, dy: pk.pos[i].y, r: pk.r,
        rec: chans, step: rec.lambda8.find((s) => s.charge === c) || null, channels: [],
      };
      const pc = pack(chans.length, pk.r * 0.92);
      ion.channels = chans.map((ch, j) => {
        const node = {
          kind: 'channel', Z, charge: c, l: ch.l, dx: ion.dx + pc.pos[j].x, dy: ion.dy + pc.pos[j].y, r: pc.r,
          rec: ch, parent: ion, cells: [],
        };
        const pm = pack(ch.measured.length, pc.r * 0.9);
        node.cells = ch.measured.map((m, q) => ({
          kind: 'cell', Z, charge: c, l: ch.l, mult: m.mult, dx: node.dx + pm.pos[q].x, dy: node.dy + pm.pos[q].y, r: pm.r,
          rec: m, parent: node,
        }));
        return node;
      });
      return ion;
    });
    return { ions };
  }

  function ensureElement(Z) {
    if (state.elements.has(Z)) return Promise.resolve(state.elements.get(Z));
    if (state.pending.has(Z)) return state.pending.get(Z);
    const p = fetch(`${DATA}elements/${Z}.json`).then((r) => {
      if (!r.ok) throw new Error(`data/elements/${Z}.json: ${r.status}`);
      return r.json();
    }).then((rec) => {
      state.elements.set(Z, rec);
      state.trees.set(Z, buildTree(Z, rec));
      state.pending.delete(Z);
      $('#loading').hidden = state.pending.size === 0;
      requestDraw();
      return rec;
    }).catch((err) => {
      state.pending.delete(Z);
      $('#loading').hidden = state.pending.size === 0;
      console.error(err);
      throw err;
    });
    state.pending.set(Z, p);
    $('#loading').hidden = false;
    return p;
  }

  // ---------------------------------------------------------------- nodes
  function elementNode(Z) {
    const e = state.index.layout.find((x) => x.Z === Z);
    return e ? { kind: 'element', Z, e } : null;
  }
  const rootNode = { kind: 'root' };

  function nodeFrame(node) {
    // absolute world circle {cx, cy, r} for flying and hit-testing
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

  // ---------------------------------------------------------------- camera
  function W() { return canvas.clientWidth; }
  function H() { return canvas.clientHeight; }
  const toScreen = (x, y) => ({ x: x * state.cam.k + state.cam.tx, y: y * state.cam.k + state.cam.ty });
  const toWorld = (sx, sy) => ({ x: (sx - state.cam.tx) / state.cam.k, y: (sy - state.cam.ty) / state.cam.k });

  function homeCam() {
    const b = state.bounds;
    const k = Math.min(W() / (b.x1 - b.x0), H() / (b.y1 - b.y0));
    return { k, tx: (W() - (b.x0 + b.x1) * k) / 2, ty: (H() - (b.y0 + b.y1) * k) / 2 };
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
    // interpolate log-scale for zoom so the motion reads as steady
    const lk = Math.log(a.from.k) + (Math.log(a.to.k) - Math.log(a.from.k)) * t;
    const k = Math.exp(lk);
    // keep the target's world centre stable along the path
    const cxTo = (W() / 2 - a.to.tx) / a.to.k, cyTo = (H() / 2 - a.to.ty) / a.to.k;
    const cxFrom = (W() / 2 - a.from.tx) / a.from.k, cyFrom = (H() / 2 - a.from.ty) / a.from.k;
    const cx = cxFrom + (cxTo - cxFrom) * t, cy = cyFrom + (cyTo - cyFrom) * t;
    state.cam = { k, tx: W() / 2 - cx * k, ty: H() / 2 - cy * k };
    if (t >= 1) { state.cam = a.to; state.anim = null; }
    return true;
  }
  function zoomAt(sx, sy, factor) {
    const home = homeCam();
    const k = Math.max(home.k * 0.4, Math.min(20000, state.cam.k * factor));
    const f = k / state.cam.k;
    state.cam = { k, tx: sx - (sx - state.cam.tx) * f, ty: sy - (sy - state.cam.ty) * f };
    state.anim = null;
    requestDraw();
  }

  // ---------------------------------------------------------------- drawing
  let drawQueued = false;
  function requestDraw() {
    if (drawQueued) return;
    drawQueued = true;
    requestAnimationFrame(draw);
  }

  function resize() {
    const dpr = window.devicePixelRatio || 1;
    canvas.width = Math.round(wrap.clientWidth * dpr);
    canvas.height = Math.round(wrap.clientHeight * dpr);
    canvas.style.width = wrap.clientWidth + 'px';
    canvas.style.height = wrap.clientHeight + 'px';
    requestDraw();
  }

  function draw(now) {
    drawQueued = false;
    const animating = stepAnim(now || performance.now());
    const dpr = window.devicePixelRatio || 1;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    const C = state.colors;
    ctx.fillStyle = C.bg;
    ctx.fillRect(0, 0, W(), H());
    if (!state.index) return;
    const { k } = state.cam;
    const s = CELL * k;

    drawAxes(s);

    // ghosts
    if (state.layout === 'table') {
      for (const g of state.ghosts) {
        const p = toScreen(g.x, g.y);
        if (p.x + s < 0 || p.y + s < 0 || p.x > W() || p.y > H()) continue;
        ctx.setLineDash([Math.max(2, s * 0.06), Math.max(2, s * 0.05)]);
        ctx.strokeStyle = C.lineStrong;
        ctx.lineWidth = 1;
        ctx.strokeRect(p.x + s * 0.06, p.y + s * 0.06, s * 0.88, s * 0.88);
        ctx.setLineDash([]);
        if (s >= 30) {
          ctx.fillStyle = C.muted;
          ctx.font = `${Math.max(9, s * 0.16)}px "IBM Plex Mono", monospace`;
          ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
          ctx.fillText('E', p.x + s / 2, p.y + s / 2);
        }
        if (state.selected && state.selected.kind === 'ghost' && state.selected.p === g.p && state.selected.g === g.g) {
          ctx.strokeStyle = C.accent; ctx.lineWidth = 2;
          ctx.strokeRect(p.x + 1, p.y + 1, s - 2, s - 2);
        }
      }
    }

    // elements
    for (const e of state.index.layout) {
      const f = state.frames.get(e.Z);
      const p = toScreen(f.x, f.y);
      if (p.x + s < 0 || p.y + s < 0 || p.x > W() || p.y > H()) continue;
      drawElement(e, p, s);
    }
    updateCrumbsPosition();
    if (animating) requestDraw();
  }

  function drawAxes(s) {
    const C = state.colors;
    if (s < 14) return;
    ctx.fillStyle = C.muted;
    ctx.font = `${Math.max(9, Math.min(13, s * 0.16))}px "IBM Plex Mono", monospace`;
    ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
    if (state.layout === 'table') {
      for (let g = 1; g <= 18; g++) {
        const p = toScreen((g - 0.5) * CELL, -0.35 * CELL);
        ctx.fillText(String(g), p.x, p.y);
      }
      ctx.textAlign = 'right';
      for (let per = 1; per <= 7; per++) {
        const p = toScreen(-0.25 * CELL, (per - 0.5) * CELL);
        ctx.fillText(String(per), p.x, p.y);
      }
      ctx.textAlign = 'left';
      let p = toScreen(17.2 * CELL, 9 * CELL); ctx.fillText('58–71 set aside', p.x, p.y);
      p = toScreen(17.2 * CELL, 10 * CELL); ctx.fillText('90–103 set aside', p.x, p.y);
      ctx.textAlign = 'right';
      p = toScreen(-0.25 * CELL, 7.5 * CELL); ctx.fillText('8', p.x, p.y);
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
    const inPath = sel && sel.Z === e.Z;
    ctx.fillStyle = e.populated ? (C.blk[e.block] || C.blk.none) : C.bg;
    ctx.fillRect(p.x, p.y, s, s);
    ctx.lineWidth = 1;
    if (e.populated) {
      ctx.strokeStyle = C.grid;
      ctx.strokeRect(p.x + 0.5, p.y + 0.5, s - 1, s - 1);
    } else {
      ctx.setLineDash([Math.max(2, s * 0.06), Math.max(2, s * 0.05)]);
      ctx.strokeStyle = C.csv;
      ctx.strokeRect(p.x + 0.5, p.y + 0.5, s - 1, s - 1);
      ctx.setLineDash([]);
    }
    if (isSel) { ctx.strokeStyle = C.accent; ctx.lineWidth = 2; ctx.strokeRect(p.x + 1, p.y + 1, s - 2, s - 2); }

    if (s >= 20) {
      ctx.fillStyle = C.text;
      ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
      const symSize = s >= 150 ? s * 0.11 : s * 0.3;
      ctx.font = `500 ${symSize}px "IBM Plex Sans", sans-serif`;
      const sy = s >= 150 ? p.y + s * 0.085 : p.y + s * 0.5;
      ctx.fillText(e.symbol, p.x + s / 2, sy);
    }
    if (s >= 48) {
      ctx.fillStyle = C.muted;
      ctx.textAlign = 'left'; ctx.textBaseline = 'top';
      ctx.font = `${s * 0.1}px "IBM Plex Mono", monospace`;
      ctx.fillText(String(e.Z), p.x + s * 0.06, p.y + s * 0.05);
      if (e.name) {
        ctx.textAlign = 'center'; ctx.textBaseline = 'bottom';
        ctx.font = `${s * 0.085}px "IBM Plex Sans", sans-serif`;
        ctx.fillText(e.name, p.x + s / 2, p.y + s * 0.96);
      }
      if (e.counts) {
        ctx.textAlign = 'right'; ctx.textBaseline = 'top';
        ctx.font = `${s * 0.075}px "IBM Plex Mono", monospace`;
        ctx.fillStyle = e.counts.measured ? C.measured : C.muted;
        ctx.fillText(e.counts.measured ? `${e.counts.measured} m` : `${e.counts.rows}`, p.x + s * 0.94, p.y + s * 0.06);
      }
    }
    if (s >= 150) {
      const cx = p.x + s / 2, cy = p.y + s * 0.53;
      const R = EL_R * state.cam.k;
      ctx.beginPath(); ctx.arc(cx, cy, R, 0, Math.PI * 2);
      ctx.strokeStyle = C.line; ctx.setLineDash([3, 4]); ctx.lineWidth = 1; ctx.stroke(); ctx.setLineDash([]);
      const tree = state.trees.get(e.Z);
      if (tree) {
        drawIons(e, tree, cx, cy);
      } else {
        ensureElement(e.Z).catch(() => {});
        ctx.fillStyle = C.muted;
        ctx.font = `${Math.max(10, s * 0.06)}px "IBM Plex Mono", monospace`;
        ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText('loading …', cx, cy);
      }
    }
  }

  // the element's inner circle is drawn at (cx, cy + 0.03 s) so the symbol has room above;
  // the same offset is used by hit-testing and flying via ionCentre()
  function ionOrigin(Z) {
    const f = state.frames.get(Z);
    return { x: f.cx, y: f.cy + CELL * 0.03 };
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
      const nMeas = ion.rec.reduce((a, ch) => a + ch.measured.filter((m) => m.grade === 'measured').length, 0);
      if (nMeas && rs >= 4) {
        ctx.beginPath(); ctx.arc(x, y, rs * 0.94, 0, Math.PI * 2);
        ctx.strokeStyle = C.measured; ctx.lineWidth = Math.max(1, rs * 0.05); ctx.stroke();
      }
      if (rs >= 13 && rs < 45) {
        ctx.fillStyle = C.text;
        ctx.font = `500 ${Math.max(9, rs * 0.42)}px "IBM Plex Sans", sans-serif`;
        ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText(roman(ion.charge), x, y);
      } else if (rs >= 45) {
        ctx.fillStyle = C.muted;
        ctx.font = `500 ${Math.max(10, rs * 0.11)}px "IBM Plex Sans", sans-serif`;
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
      const nM = ch.rec.measured.filter((m) => m.grade === 'measured').length;
      ctx.beginPath(); ctx.arc(x, y, rs, 0, Math.PI * 2);
      ctx.fillStyle = C.bg; ctx.fill();
      ctx.lineWidth = isSel ? 2 : 1;
      ctx.strokeStyle = isSel || inPath ? C.accent : (nM ? C.measured : C.lineStrong);
      ctx.stroke();
      if (rs >= 10 && rs < 40) {
        ctx.fillStyle = C.text;
        ctx.font = `500 ${Math.max(9, rs * 0.7)}px "IBM Plex Serif", serif`;
        ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText(LSYM[ch.l] || String(ch.l), x, y);
      } else if (rs >= 40) {
        ctx.fillStyle = C.muted;
        ctx.font = `500 ${Math.max(10, rs * 0.16)}px "IBM Plex Serif", serif`;
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
      if (c.rec.grade === 'measured') { ctx.fillStyle = C.measured; ctx.fill(); }
      else if (c.rec.grade === 'exact') { ctx.fillStyle = C.surface; ctx.fill(); ctx.strokeStyle = C.exact; ctx.lineWidth = Math.max(1, rs * 0.12); ctx.stroke(); }
      else { ctx.fillStyle = C.computed; ctx.globalAlpha = 0.55; ctx.fill(); ctx.globalAlpha = 1; }
      if (c.rec.witness === 'witnessed' && rs >= 6) {
        ctx.beginPath(); ctx.arc(x, y, rs * 1.25, 0, Math.PI * 2);
        ctx.strokeStyle = C.measured; ctx.lineWidth = 1; ctx.stroke();
      }
      if (isSel) { ctx.beginPath(); ctx.arc(x, y, rs + 3, 0, Math.PI * 2); ctx.strokeStyle = C.accent; ctx.lineWidth = 2; ctx.stroke(); }
      if (rs >= 9) {
        ctx.fillStyle = c.rec.grade === 'measured' ? C.surface : C.text;
        ctx.font = `500 ${Math.max(9, rs * 0.8)}px "IBM Plex Mono", monospace`;
        ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText(String(c.mult), x, y);
      }
    }
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
  async function select(node, opts = {}) {
    const { fly = true, ms = 650, setHash = true } = opts;
    state.selected = node;
    renderInspector(node);
    renderCrumbs(node);
    if (setHash) {
      const h = hashOf(node);
      state.lastHash = h;
      if (location.hash !== h) history.replaceState(null, '', h);
    }
    if (fly) {
      if (node.kind === 'root') flyTo(homeCam(), ms);
      else {
        const fill = node.kind === 'element' ? 0.78 : node.kind === 'ghost' ? 0.5 : 0.6;
        flyTo(camFor(frameFor(node), fill), ms);
      }
    }
    requestDraw();
  }

  async function goToPath(Z, charge, l, mult, opts = {}) {
    const el = elementNode(Z);
    if (!el) return false;
    if (charge === undefined) { await select(el, opts); return true; }
    await ensureElement(Z);
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
    if (parts[2]) out.l = LSYM.indexOf(parts[2].toLowerCase()) >= 0 ? LSYM.indexOf(parts[2].toLowerCase()) : parseInt(parts[2], 10);
    if (parts[3]) out.mult = parseInt(parts[3], 10);
    return out;
  }

  async function applyHash(fly = true, ms = 650) {
    const h = location.hash;
    if (h === state.lastHash) return;
    const p = parseHash(h);
    if (!p || p.root) return select(rootNode, { fly, ms });
    if (p.ghost) {
      const g = state.ghosts.find((x) => x.p === p.ghost.p && x.g === p.ghost.g);
      return g ? select({ kind: 'ghost', ...g }, { fly, ms }) : select(rootNode, { fly, ms });
    }
    return goToPath(p.Z, p.charge, p.l, p.mult, { fly, ms });
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
  function updateCrumbsPosition() { /* fixed overlay; nothing to move */ }

  // ---------------------------------------------------------------- inspector
  const AX = {};
  function axisStatus(name) { return AX[name] || null; }
  function badge(status, tip) {
    if (!status) return `<span class="badge st-NONE" title="no status carried">—</span>`;
    const t = tip || (state.index.status_legend[status] || '');
    return `<span class="badge st-${esc(status)}" title="${esc(t)}">${esc(status)}</span>`;
  }
  function row(k, v, status, tip, plain) {
    const val = plain ? `<span class="plain">${v}</span>` : v;
    return `<div class="f-k">${esc(k)}</div><div class="f-v">${val} ${status === undefined ? '' : badge(status, tip)}</div>`;
  }
  function axRow(k, v, axis, plain) {
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
      ${node.Z ? `<a href="${DATA}elements/${node.Z}.json" target="_blank" rel="noopener">data/elements/${node.Z}.json</a>` : ''}
    </div>
    <pre class="raw" hidden>${esc(raw)}</pre>
    <div class="cite">${esc(cite)}</div>`;
  }
  function citation(node) {
    const m = state.index.meta;
    const path = pathOf(node).map((n) => n.kind === 'root' ? 'The Method Index' : n.kind === 'channel' ? `ℓ=${n.l}` : n.kind === 'cell' ? `2S+1=${n.mult}` : label(n)).join(' › ');
    const src = state.index.sources.map((s) => `${s.file.split('/').pop()} ${s.md5_measured ? s.md5_measured.slice(0, 8) : '?'}`).join(', ');
    return `${path}. The Method 1.6, read by tools/populate.py and written by tools/webindex.py; commit ${m.commit || '?'}, built ${m.built}. Sources: ${src}. ${location.origin}${location.pathname}${hashOf(node)}`;
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
    body.scrollTop = 0;
    $('#btn-up').disabled = node.kind === 'root';
    body.querySelectorAll('[data-go]').forEach((el) => el.addEventListener('click', () => {
      const [Z, c, l, m] = el.dataset.go.split('/');
      goToPath(+Z, c === '' || c === undefined ? undefined : +c, l === '' || l === undefined ? undefined : +l, m === '' || m === undefined ? undefined : +m);
    }));
    body.querySelectorAll('[data-act]').forEach((b) => b.addEventListener('click', () => {
      const act = b.dataset.act;
      if (act === 'toggle-raw') { const pre = body.querySelector('pre.raw'); pre.hidden = !pre.hidden; }
      if (act === 'copy-json') copyText(body.querySelector('pre.raw').textContent, b);
      if (act === 'copy-link') copyText(location.href.split('#')[0] + hashOf(node), b);
      if (act === 'open-prov') $('#dlg-provenance').showModal();
    }));
  }
  function copyText(t, btn) {
    const done = () => { const old = btn.textContent; btn.textContent = 'Copied'; setTimeout(() => { btn.textContent = old; }, 1200); };
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(t).then(done, () => { btn.textContent = 'Copy failed'; });
    else btn.textContent = 'Copy unavailable';
  }

  function renderRoot() {
    const ix = state.index, t = ix.totals, c = ix.closure;
    const layoutNote = state.layout === 'table'
      ? `Section 6's drawn layout: <b>${c.held}</b> cells held, <b>${c.admitted}</b> admitted by ℛ, <b>E = ${c.E}</b>. The ${c.E} are the gaps in the short periods, drawn as dashed ghosts; ${c.set_aside} f-block elements are set aside below the table.`
      : `Register 1188's coordinate: Janet's cell is (n+ℓ, ℓ) of the differentiating electron, and on it E = 0. Elements without a cell (Z &gt; 108) sit on the bottom row.`;
    return `<div class="kind">the index</div>
      <h2 class="node-title">${esc(ix.meta.title)}</h2>
      <p class="node-sub">${esc(ix.meta.subtitle)}</p>
      <p class="note">${layoutNote}</p>
      <div class="stats">
        <div class="stat"><b>${t.populated}</b><span>elements populated</span></div>
        <div class="stat"><b>${t.csv_only}</b><span>spectra rows only (Z 109–120)</span></div>
        <div class="stat"><b>${t.rows.toLocaleString()}</b><span>channel cells</span></div>
        <div class="stat"><b>${t.measured}</b><span>measured</span></div>
        <div class="stat"><b>${t.exact}</b><span>exact</span></div>
        <div class="stat"><b>${t.computed.toLocaleString()}</b><span>computed</span></div>
      </div>
      ${section('How to read it', `<p class="note">Zoom into any element: its ions appear inside it in spectroscopic order (I is neutral), each ion opens into its ℓ channels, each channel into its cells, one per multiplicity, coloured by grade. Every value in this panel carries the status the corpus gives it: ${Object.keys(ix.status_legend).map((s) => badge(s)).join(' ')}. Nothing on the page is computed by the page.</p>`)}
      ${section('Closure of this layout', `<div class="fields">
        ${row('index', esc(c.index), 'PINNED', 'section 6', true)}
        ${row('operator', esc(c.operator), 'PINNED', 'section 32.4.1', true)}
        ${row('held', c.held, 'PINNED', 'section 6: ninety main-table cells')}
        ${row('admitted', c.admitted, 'PINNED', 'ℛ over the layout')}
        ${row('E', c.E, 'DERIVED', 'admitted − held')}
        ${row('set aside', c.set_aside, 'PINNED', 'the lanthanides and actinides, section 6')}
      </div>`)}
      ${section('Caveats that travel with every value', `<ul class="note">${ix.caveats.map((v) => `<li>${esc(v.text)}</li>`).join('')}</ul>`)}
      <div class="actions"><button type="button" data-act="open-prov">Provenance and sources</button></div>
      <div class="cite">${esc(citation(rootNode))}</div>`;
  }

  function renderGhost(node) {
    const c = state.index.closure;
    return `<div class="kind">admitted, not held</div>
      <h2 class="node-title">Period ${node.p}, group ${node.g}</h2>
      <p class="node-sub">one of the ${c.E} cells that make E = ${c.E}</p>
      <p class="note">ℛ, the order operator, admits this cell: the layout has a period ${node.p} and a group ${node.g}, so the downward closure of the held set reaches it. Section 6's table does not hold it. E counts what the operator admits and the object does not hold, and here it is a gap in a short period, not an element that is missing.</p>
      ${section('Closure', `<div class="fields">
        ${row('cell', `(${node.p}, ${node.g})`, 'DERIVED', 'admitted − held')}
        ${row('held', c.held, 'PINNED', 'section 6')}
        ${row('admitted', c.admitted, 'PINNED', 'ℛ over the layout')}
        ${row('E', c.E, 'DERIVED', 'admitted − held')}
      </div>`)}
      <div class="cite">${esc(citation(node))}</div>`;
  }

  function renderElement(node) {
    const e = node.e;
    const rec = state.elements.get(node.Z);
    const head = `<div class="kind">element · Z = ${e.Z}</div>
      <h2 class="node-title">${esc(e.symbol)} <span class="note" style="font-family:var(--font-body);font-size:15px;font-weight:400">${esc(e.name || '')}</span></h2>
      <p class="node-sub">${e.populated ? `${esc(e.shells)} · ${esc(e.level)}` : 'spectra rows only'}</p>`;
    if (!e.populated) {
      const cav = state.index.caveats.find((v) => v.id === 'above-108');
      const ions = rec ? state.trees.get(node.Z).ions : null;
      return head + `<div class="callout is-finding">${esc(cav.text)}</div>
        ${section('Layout', `<div class="fields">
          ${axRow('period', e.period, 'period')}
          ${axRow('group', fmt(e.group), 'group')}
          ${row('configuration', 'none carried', null, undefined, true)}
        </div>`)}
        ${section('Spectra rows', `<div class="fields">
          ${row('cells', e.counts.rows, 'READ', 'COORDINATES-2.13')}
          ${row('measured', e.counts.measured, 'READ', 'COORDINATES-2.13')}
          ${row('ions', e.counts.ions, 'READ', 'COORDINATES-2.13')}
        </div>`)}
        ${ions ? section('Ions', `<div class="chips">${ions.map((i) => `<button type="button" class="chip is-csv" data-go="${node.Z}/${i.charge}">${esc(e.symbol)} ${roman(i.charge)}</button>`).join('')}</div>`) : '<p class="note">loading ions …</p>'}
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
    if (rec) {
      html += section('Configuration', `<div class="tbl-wrap"><table class="t"><thead><tr><th>subshell</th><th class="num">n</th><th class="num">ℓ</th><th class="num">occ</th><th class="num">cap</th><th class="num">n+ℓ</th><th>full</th></tr></thead><tbody>
        ${rec.configuration.map((c) => `<tr><td>${esc(c.subshell)}</td><td class="num">${c.n}</td><td class="num">${c.l}</td><td class="num">${c.occupancy}</td><td class="num">${c.capacity}</td><td class="num">${c['n+l']}</td><td>${c.full ? '●' : '○'}</td></tr>`).join('')}
      </tbody></table></div>`, `${badge('READ', 'shells: LW1-ground.py, register 1306')} ${badge('DERIVED', 'n, ℓ, occupancy, n+ℓ')} ${badge('PINNED', 'capacity 2(2ℓ+1), section 7.1')}`);
      const tree = state.trees.get(node.Z);
      html += section('Ions', `<p class="note">${e.counts.ions} spectroscopic stages, ${e.counts.channels} channels, ${e.counts.rows.toLocaleString()} cells; ${e.counts.measured} measured, ${e.counts.exact} exact, ${e.counts.computed.toLocaleString()} computed.</p>
        <div class="chips">${tree.ions.map((i) => {
          const nM = i.rec.reduce((a, ch) => a + ch.measured.filter((m) => m.grade === 'measured').length, 0);
          return `<button type="button" class="chip" data-go="${node.Z}/${i.charge}" title="${nM} measured">${esc(e.symbol)} ${roman(i.charge)}${nM ? ` <span class="dot dot-measured" style="margin:0 0 0 4px"></span>` : ''}</button>`;
        }).join('')}</div>`);
      if (rec.lambda8.length) {
        html += section('Λ₈ ionisation ladder', `<div class="callout">${esc(state.index.caveats.find((v) => v.id === 'lambda8-mapping').text)}</div>
          <div class="tbl-wrap"><table class="t"><thead><tr><th>stage</th><th>transition</th><th>(n, ℓ, k, q, e, f, g, 2S)</th><th>7.1</th><th>within 7.4 caps</th></tr></thead><tbody>
          ${rec.lambda8.map((s) => {
            const holds = s.constraints.filter((c) => c.holds).length;
            const within = Object.values(s.within_caps).every(Boolean);
            const need = Object.entries(s.caps_needed).filter(([k, v]) => v > state.index.caps[k]).map(([k, v]) => `${k}≥${v}`).join(' ');
            return `<tr class="is-link" data-go="${node.Z}/${s.charge}"><td>${roman(s.charge)}</td><td>${esc(s.from)} → ${esc(s.to)}</td><td>(${s.cell.map((v) => v === null ? '·' : v).join(', ')})</td><td>${holds}/${s.constraints.length}</td><td>${within ? 'within' : `<span class="bad">outside</span> ${esc(need)}`}</td></tr>`;
          }).join('')}
          </tbody></table></div>`, badge('RECONSTRUCTED', axisStatus('Lambda_8 cell').source));
      }
      html += actions(node, { ...rec, channels: `${rec.channels.length} channels — see the ion nodes` });
    } else {
      html += '<p class="note">loading the element …</p>';
      ensureElement(node.Z).then(() => { if (state.selected === node) renderInspector(node); }).catch(() => {});
    }
    return html;
  }

  function renderIon(node) {
    const sym = symbolOf(node.Z);
    const e = state.index.layout.find((x) => x.Z === node.Z);
    const populated = e.populated;
    const first = node.rec[0];
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
        const r = ch.rec, nM = r.measured.filter((m) => m.grade === 'measured').length;
        return `<tr class="is-link" data-go="${node.Z}/${node.charge}/${ch.l}"><td>${LSYM[ch.l] || ch.l} <span class="note">ℓ=${ch.l}</span></td><td class="num">${fmt(r.p)}</td><td class="num">${fmt(r.n0)}</td><td class="num">${fmt(r.B_computed)}</td><td class="num">${fmt(r.C_of_Z, 3)}</td><td class="num">${fmt(r.delta_equation)}</td><td class="num">${r.measured.length}</td><td class="num">${nM ? `<span class="dot dot-measured"></span>${nM}` : '—'}</td></tr>`;
      }).join('')}
    </tbody></table></div>
    <p class="note" style="margin-top:6px">p ${badge('PINNED', axisStatus('p').source)} · n₀ ${badge('RECONSTRUCTED', axisStatus('n0').source)} · B ${badge('PINNED', axisStatus('B').source)} · C(Z) ${badge('RECONSTRUCTED', axisStatus('C(Z)').source)} · δ equation ${badge('PINNED', axisStatus('delta equation').source)}${populated ? '' : ' · none carried above Z = 108'}</p>`);
    if (node.step) {
      const s = node.step, cm = state.index.lambda_meaning || {};
      html += section('Λ₈ step at this stage', `<div class="fields">
        ${row('transition', `${esc(s.from)} → ${esc(s.to)}`, 'RECONSTRUCTED', axisStatus('Lambda_8 cell').source, true)}
        ${Object.entries(s.coords).map(([k, v]) => row(k, v === null ? '— (not carried)' : v, 'RECONSTRUCTED', cm[k] || 'Λ₈ coordinate')).join('')}
      </div>
      <div class="tbl-wrap" style="margin-top:8px"><table class="t"><thead><tr><th>constraint (§7.1)</th><th>holds</th><th>origin</th></tr></thead><tbody>
        ${s.constraints.map((c) => `<tr><td>${esc(c.rule)}</td><td class="${c.holds ? 'ok' : 'holds-false'}">${c.holds ? 'holds' : 'fails'}</td><td class="plain" style="font-family:var(--font-body)">${esc(c.origin)}</td></tr>`).join('')}
      </tbody></table></div>
      <div class="fields" style="margin-top:8px">
        ${row('within §7.4 caps', Object.entries(s.within_caps).map(([k, v]) => `${k}:${v ? '✓' : '✗'}`).join(' '), 'PINNED', axisStatus('caps').source)}
        ${row('caps needed', Object.entries(s.caps_needed).map(([k, v]) => `${k}≥${v}`).join(' '), 'DERIVED', 'the cap at which this cell would be admitted')}
      </div>`);
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
      ${axRow('ℓ', `${node.l} (${LSYM[node.l] || node.l})`, 'l')}
      ${axRow('p', fmt(r.p), 'p')}
      ${axRow('n₀', fmt(r.n0), 'n0')}
      ${axRow('B = min(p, n₀−ℓ−1)', fmt(r.B_computed), 'B')}
      ${axRow('C(Z, ℓ)', fmt(r.C_of_Z, 3), 'C(Z)')}
      ${axRow('δ by equation', fmt(r.delta_equation), 'delta equation')}
    </div>${populated ? '' : `<div class="callout is-finding">${esc(state.index.caveats.find((v) => v.id === 'above-108').text)}</div>`}`);
    html += section('Cells, one per multiplicity', `<div class="tbl-wrap"><table class="t"><thead><tr><th class="num">2S+1</th><th class="num">δ</th><th>grade</th><th class="num">residual</th><th class="num">B (csv)</th><th>agrees</th><th>witness</th></tr></thead><tbody>
      ${node.cells.map((c) => {
        const m = c.rec;
        return `<tr class="is-link" data-go="${node.Z}/${node.charge}/${node.l}/${c.mult}"><td class="num">${c.mult}</td><td class="num">${fmt(m.delta)}</td><td><span class="dot dot-${esc(m.grade)}"></span>${esc(m.grade)}</td><td class="num">${fmt(m.residual)}</td><td class="num">${m.B_csv_is_not_a_bound ? '<span class="bad">not a bound</span>' : fmt(m.B_csv)}</td><td>${m.B_agrees === null ? '—' : m.B_agrees ? '<span class="ok">yes</span>' : '<span class="bad">no</span>'}</td><td>${m.witness === 'witnessed' ? '<span class="ok">witnessed</span>' : '<span class="note">unwitnessed</span>'}</td></tr>`;
      }).join('')}
    </tbody></table></div>
    <p class="note" style="margin-top:6px">δ ${badge('READ', axisStatus('delta measured').source)} · residual = δ − δ equation ${badge('DERIVED')} · B (csv) ${badge('READ', 'COORDINATES-2.13, B column')}</p>`);
    html += actions(node, r);
    return html;
  }

  function renderCell(node) {
    const m = node.rec, ch = node.parent.rec, sym = symbolOf(node.Z);
    const cav = (id) => state.index.caveats.find((v) => v.id === id).text;
    let html = `<div class="kind">cell · ${esc(sym)} ${roman(node.charge)} ${LSYM[node.l] || node.l}</div>
      <h2 class="node-title">${esc(sym)} ${roman(node.charge)} ${LSYM[node.l] || node.l}, 2S+1 = ${node.mult}</h2>
      <p class="node-sub"><span class="dot dot-${esc(m.grade)}"></span>${esc(m.grade)} · ${esc(m.witness)}</p>`;
    html += section('Coordinates', `<div class="fields">
      ${axRow('Z', node.Z, 'Z')}
      ${axRow('charge', `${node.charge} (${roman(node.charge)})`, 'charge')}
      ${axRow('ℓ', node.l, 'l')}
      ${row('2S+1', node.mult, 'READ', 'COORDINATES-2.13, mult column')}
    </div>`);
    html += section('The value', `<div class="fields">
      ${axRow('δ', fmt(m.delta), 'delta measured')}
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
    ${m.B_csv_is_not_a_bound ? `<div class="callout is-finding">${esc(cav('b-overloaded'))}</div>` : ''}
    ${m.B_agrees === false ? `<div class="callout is-finding">${esc(cav('b-aufbau'))}</div>` : ''}`);
    html += section('Witness', `<div class="fields">
      ${axRow('witness', esc(m.witness), 'witness', true)}
      ${row('source', esc(m.source), 'READ', 'COORDINATES-2.13, source column', true)}
      ${axRow('bound note', esc(m.bound_note), 'bound', true)}
    </div>`);
    html += actions(node, { Z: node.Z, charge: node.charge, l: node.l, ...m, delta_equation: ch.delta_equation, B_computed: ch.B_computed });
    return html;
  }

  // ---------------------------------------------------------------- provenance
  function renderProvenance() {
    const ix = state.index, m = ix.meta, t = ix.totals;
    $('#provenance-body').innerHTML = `
      <p>${esc(m.generator)}. Commit <code>${esc(m.commit || 'unknown')}</code>, built ${esc(m.built)}. ${esc(m.names_note)}</p>
      <h3>Sources, with the md5 the store records and the md5 measured at build</h3>
      <div class="tbl-wrap"><table class="t"><thead><tr><th>file</th><th>role</th><th>recorded</th><th>measured</th><th></th></tr></thead><tbody>
        ${ix.sources.map((s) => `<tr><td>${esc(s.file)}</td><td style="white-space:normal;font-family:var(--font-body)">${esc(s.role)}</td><td>${esc((s.md5_recorded || '?').slice(0, 12))}</td><td>${esc((s.md5_measured || '?').slice(0, 12))}</td><td>${s.ok ? '<span class="ok">match</span>' : '<span class="bad">DRIFT</span>'}</td></tr>`).join('')}
      </tbody></table></div>
      <h3>Totals</h3>
      <div class="stats">
        <div class="stat"><b>${t.populated}</b><span>elements populated (LW1-ground.py)</span></div>
        <div class="stat"><b>${t.csv_only}</b><span>spectra rows only</span></div>
        <div class="stat"><b>${t.rows.toLocaleString()}</b><span>cells = COORDINATES-2.13 rows</span></div>
        <div class="stat"><b>${t.measured}</b><span>measured</span></div>
        <div class="stat"><b>${t.exact}</b><span>exact</span></div>
        <div class="stat"><b>${t.witnessed}</b><span>witnessed</span></div>
      </div>
      <h3>The equation and the collapse</h3>
      <div class="fields">
        ${row('channel equation', `A = ${ix.equation.A}, K = ${ix.equation.K}, H = ${ix.equation.H}`, ix.equation.status, ix.equation.source)}
        ${row('collapse C(Z, ℓ)', esc(ix.collapse.form), ix.collapse.status, 'registers 1188–1190; inverted out of the computed column')}
        ${row('Z₀(ℓ)', Object.entries(ix.collapse.Z0).map(([l, z]) => `ℓ=${l}: ${z}`).join(' · '), ix.collapse.status, 'the Janet block openings')}
        ${row('§7.4 caps', Object.entries(ix.caps).map(([k, v]) => `${k}≤${v}`).join(' '), 'PINNED', 'section 7.4')}
      </div>
      <h3>Every axis and its status</h3>
      <div class="tbl-wrap"><table class="t"><thead><tr><th>axis</th><th>status</th><th>source</th></tr></thead><tbody>
        ${ix.axes.map((a) => `<tr><td>${esc(a.axis)}</td><td>${badge(a.status)}</td><td style="white-space:normal;font-family:var(--font-body)">${esc(a.source)}</td></tr>`).join('')}
      </tbody></table></div>
      <h3>Status vocabulary</h3>
      <div class="fields">${Object.entries(ix.status_legend).map(([k, v]) => row(k, esc(v), k, undefined, true)).join('')}</div>
      <h3>Caveats</h3>
      <ul>${ix.caveats.map((v) => `<li>${esc(v.text)}</li>`).join('')}</ul>
      <h3>Element files</h3>
      <p class="note">${ix.manifest.length} files under <code>data/elements/</code>, ${(ix.manifest.reduce((a, x) => a + x.bytes, 0) / 1e6).toFixed(1)} MB, each md5 recorded in <code>data/index.json</code>; <code>python3 tools/webindex.py --verify</code> checks them.</p>`;
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
    const l = LSYM.indexOf(toks[2].toLowerCase()) >= 0 ? LSYM.indexOf(toks[2].toLowerCase()) : parseInt(toks[2], 10);
    if (Number.isNaN(l) || l < 0 || l > 7) return [{ path: `${e.symbol} ${roman(c)} ?`, note: 'ℓ = s p d f g h i k', go: [e.Z, c] }];
    if (toks.length === 3) return [{ path: `${e.symbol} ${roman(c)} ${LSYM[l]}`, note: `channel ℓ=${l}`, go: [e.Z, c, l] }];
    const mult = parseInt(toks[3], 10);
    return [{ path: `${e.symbol} ${roman(c)} ${LSYM[l]} ${mult || '?'}`, note: 'cell, 2S+1', go: [e.Z, c, l, mult || undefined] }];
  }
  function setupSearch() {
    const q = $('#q'), ul = $('#suggest');
    let items = [], active = -1;
    const render = () => {
      ul.innerHTML = items.map((it, i) => `<li role="option" class="${i === active ? 'is-active' : ''}"><span class="s-path">${esc(it.path)}</span><span class="s-note">${esc(it.note)}</span></li>`).join('');
      ul.hidden = items.length === 0;
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
    $('#search').addEventListener('submit', (ev) => { ev.preventDefault(); go(items[active] || items[0]); });
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
        pinch = { d: Math.hypot(a.x - b.x, a.y - b.y), k: state.cam.k };
      }
      canvas.classList.add('is-dragging');
    });
    canvas.addEventListener('pointermove', (ev) => {
      if (!pts.has(ev.pointerId)) return;
      pts.set(ev.pointerId, { x: ev.clientX, y: ev.clientY });
      const rect = canvas.getBoundingClientRect();
      if (pts.size === 2 && pinch) {
        const [a, b] = [...pts.values()];
        const d = Math.hypot(a.x - b.x, a.y - b.y);
        const mx = (a.x + b.x) / 2 - rect.left, my = (a.y + b.y) / 2 - rect.top;
        zoomAt(mx, my, (pinch.k * (d / pinch.d)) / state.cam.k);
        dragged = true;
        return;
      }
      if (pts.size === 1 && last) {
        const dx = ev.clientX - last.x, dy = ev.clientY - last.y;
        if (Math.abs(dx) + Math.abs(dy) > 2) dragged = true;
        state.cam.tx += dx; state.cam.ty += dy; state.anim = null;
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
        const node = hit(ev.clientX - rect.left, ev.clientY - rect.top);
        if (node) select(node);
      }
    };
    canvas.addEventListener('pointerup', up);
    canvas.addEventListener('pointercancel', up);
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
    window.addEventListener('keydown', (ev) => {
      const inField = /INPUT|TEXTAREA/.test(document.activeElement.tagName);
      if (ev.key === '/' && !inField) { ev.preventDefault(); $('#q').focus(); $('#q').select(); return; }
      if (inField) return;
      if (ev.key === 'Escape') { if (document.querySelector('dialog[open]')) return; goUp(); }
      else if (ev.key === 'h' || ev.key === 'H') select(rootNode);
      else if (ev.key === '+' || ev.key === '=') zoomAt(W() / 2, H() / 2, 1.5);
      else if (ev.key === '-' || ev.key === '_') zoomAt(W() / 2, H() / 2, 1 / 1.5);
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

  function setupChrome() {
    $('#z-in').addEventListener('click', () => zoomAt(W() / 2, H() / 2, 1.5));
    $('#z-out').addEventListener('click', () => zoomAt(W() / 2, H() / 2, 1 / 1.5));
    $('#z-home').addEventListener('click', () => select(rootNode));
    $('#btn-up').addEventListener('click', goUp);
    $('#btn-collapse').addEventListener('click', () => {
      const ins = $('#inspector');
      ins.classList.toggle('is-collapsed');
      $('#btn-collapse').textContent = ins.classList.contains('is-collapsed') ? '‹' : '›';
      resize();
    });
    $('#btn-provenance').addEventListener('click', () => $('#dlg-provenance').showModal());
    $('#btn-help').addEventListener('click', () => $('#dlg-help').showModal());
    document.querySelectorAll('.dlg-close').forEach((b) => b.addEventListener('click', () => $('#' + b.dataset.close).close()));
    document.querySelectorAll('dialog').forEach((d) => d.addEventListener('click', (ev) => { if (ev.target === d) d.close(); }));
    document.querySelectorAll('.seg-btn').forEach((b) => b.addEventListener('click', () => setLayout(b.dataset.layout)));
    $('#btn-theme').addEventListener('click', () => {
      const root = document.documentElement;
      const cur = root.getAttribute('data-theme');
      const next = cur === 'dark' ? 'light' : cur === 'light' ? null : 'dark';
      if (next) root.setAttribute('data-theme', next); else root.removeAttribute('data-theme');
      try { if (next) localStorage.setItem('theme', next); else localStorage.removeItem('theme'); } catch (e) { /* private window */ }
      readColors(); requestDraw();
    });
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => { readColors(); requestDraw(); });
    window.addEventListener('hashchange', () => applyHash());
    new ResizeObserver(resize).observe(wrap);
  }

  function setLayout(mode) {
    if (mode === state.layout) return;
    state.layout = mode;
    document.querySelectorAll('.seg-btn').forEach((b) => b.classList.toggle('is-on', b.dataset.layout === mode));
    buildFrames();
    const sel = state.selected || rootNode;
    if (sel.kind === 'ghost' && mode !== 'table') select(rootNode);
    else select(sel, { setHash: false });
  }

  // ---------------------------------------------------------------- boot
  async function boot() {
    try { const t = localStorage.getItem('theme'); if (t) document.documentElement.setAttribute('data-theme', t); } catch (e) { /* none */ }
    readColors();
    const r = await fetch(`${DATA}index.json`);
    if (!r.ok) {
      $('#inspector-body').innerHTML = `<p class="callout is-finding">data/index.json could not be loaded (${r.status}). Run <code>python3 tools/webindex.py</code> to write public/data/, then serve <code>public/</code>.</p>`;
      return;
    }
    state.index = await r.json();
    for (const a of state.index.axes) AX[a.axis] = a;
    $('#site-title').textContent = state.index.meta.title;
    $('#site-subtitle').textContent = state.index.meta.subtitle;
    document.title = state.index.meta.title;
    $('#n-measured').textContent = state.index.totals.measured;
    $('#n-exact').textContent = state.index.totals.exact;
    $('#n-computed').textContent = state.index.totals.computed.toLocaleString();
    buildFrames();
    resize();
    renderProvenance();
    setupSearch(); setupPointer(); setupKeys(); setupChrome();
    state.cam = homeCam();
    state.lastHash = null;
    if (location.hash && location.hash !== '#/') await applyHash(true, 0);
    else await select(rootNode, { fly: false });
    requestDraw();
  }

  boot().catch((err) => {
    console.error(err);
    $('#inspector-body').innerHTML = `<p class="callout is-finding">The index failed to start: ${esc(err.message)}</p>`;
  });
})();
