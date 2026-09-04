#!/usr/bin/env python3
"""tools/slopeaxis.py -- the occupation law of Chapter 34 as one object.

Section 34.4 states the rule as nu = n - a*sqrt(r), r = p + q/2(2l+1), and the
incoming electron takes the least nu.  Minimising n - a*sqrt(r) is minimising
y - a*x at the point (x, y) = (sqrt(r), n).  So every admissible subshell is a
POINT in a plane and `a` is a SLOPE: a line of slope a rising from below stops
at one point, and only vertices of the lower convex hull can ever be that
point.  An element's place on the axis is the interval between the two
hull-edge slopes flanking its observed entrant -- which is section 34.5's
corridor, arrived at from the other side.

That identity is not assumed here, it is asserted: --selftest checks the
corridor set against the hull-vertex set at all 106 steps in both forms and
fails on any mismatch.

    python3 tools/slopeaxis.py --selftest
    python3 tools/slopeaxis.py --json out/axis.json
    python3 tools/slopeaxis.py --html out/slope-axis.html
    python3 tools/slopeaxis.py --report

It IMPORTS the seated member method/members/r2-ch16y.py by path for the
observed ground configurations and the corridor machinery; it reimplements
neither.  Stdlib only, Python 3.9+.

Three things it refuses to do:

  1. It never draws a row past Z = 108.  Register 1304: there are FOUR edges,
     not two -- optical spectroscopy ends at 102, the NIST ASD listing holds no
     neutral ground configuration past 108, synthesis ends at 118, and Janet's
     lattice counts 120 cells.  A row beyond the listing would be an invented
     cell, which register 1288 already refused once.  The four edges are
     printed as an annotation and never as data.

  2. It never reports a coverage figure without naming the form AND the sign
     convention.  Coverage under a in R and under a > 0 are different numbers;
     the corpus records both and docket 20x is not closed by picking one.

  3. It never merges the two forms.  Node-only gives 17 distinct edge slopes
     and 14 forced emptyings; the finished form gives 121 and 11.  Averaging
     them, or silently defaulting to whichever is prettier, would flatten
     docket 37.  Both are computed, both are emitted, neither is preferred.
"""

from __future__ import annotations

import argparse
import contextlib
import io
import json
import math
import os
import runpy
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MEMBERS = os.path.join(ROOT, "method", "members")
INF = float("inf")

# the four edges of register 1304 -- annotation, never a row
EDGES = [
    (102, "optical spectroscopy ends (No)"),
    (108, "NIST ASD listing ends (Hs)"),
    (118, "synthesised ends (Og)"),
    (120, "Janet's cell count"),
]


def load_member():
    """Import r2-ch16y by path.  An instrument imports a seated member; it never copies one."""
    if MEMBERS not in sys.path:
        sys.path.insert(0, MEMBERS)
    path = os.path.join(MEMBERS, "r2-ch16y.py")
    if not os.path.exists(path):
        sys.exit("slopeaxis: seated member not found: %s" % path)
    with contextlib.redirect_stdout(io.StringIO()):
        return runpy.run_path(path)


class Store:
    def __init__(self):
        g = load_member()
        self.cap = g["cap"]
        self.nl = g["nl"]
        self.CONF = g["CONF"]
        self.ENT = g["ENT"]
        self.SYM = g["SYM"]
        LQ = g["LQ"]
        self.ALL = [
            "%d%s" % (n, l)
            for n in range(1, 8)
            for l in "spdfg"
            if LQ[l] < n and LQ[l] <= 3
        ]

    def p_of(self, s):
        n, l = self.nl(s)
        return n - l - 1

    def k_of(self, s):
        n, l = self.nl(s)
        return n + l

    def rad(self, s, q, form):
        return self.p_of(s) + (q / self.cap(s) if form == "q" else 0.0)

    def x(self, s, conf, form):
        return math.sqrt(self.rad(s, conf.get(s, 0), form))

    def y(self, s):
        return float(self.nl(s)[0])

    def admissible(self, Z):
        prev = self.CONF[Z - 1]
        return [s for s in self.ALL if prev.get(s, 0) < self.cap(s)]

    def corridor(self, conf, cand, S, form):
        """The interval of slopes on which cand is strictly least-nu against S."""
        Ps, ns = self.x(cand, conf, form), self.y(cand)
        lo, hi, infeasible = -INF, INF, False
        for r in S:
            if r == cand:
                continue
            Pr, nr = self.x(r, conf, form), self.y(r)
            c, d = Pr - Ps, nr - ns
            if abs(c) < 1e-12:
                if d <= 0:
                    infeasible = True
            elif c > 0:
                hi = min(hi, d / c)
            else:
                lo = max(lo, d / c)
        return lo, hi, infeasible

    def hull(self, conf, S, form):
        """Vertices of the LOWER convex hull of {(sqrt(r), n)}, left to right."""
        byx = {}
        for s in S:
            k = round(self.x(s, conf, form), 12)
            if k not in byx or self.y(s) < self.y(byx[k]):
                byx[k] = s
        Q = sorted(byx.values(), key=lambda s: self.x(s, conf, form))
        H = []
        for q in Q:
            while len(H) >= 2:
                x1, y1 = self.x(H[-2], conf, form), self.y(H[-2])
                x2, y2 = self.x(H[-1], conf, form), self.y(H[-1])
                x3, y3 = self.x(q, conf, form), self.y(q)
                if (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1) <= 0:
                    H.pop()
                else:
                    break
            H.append(q)
        return H

    def kpick(self, S):
        return min(S, key=lambda s: (self.k_of(s), self.nl(s)[0]))


def build(store, form):
    steps, ends = [], set()
    for Z in range(3, 109):
        conf = store.CONF[Z - 1]
        S = store.admissible(Z)
        H = store.hull(conf, S, form)
        lo, hi, bad = store.corridor(conf, store.ENT[Z], S, form)
        A = [
            s
            for s in S
            if (lambda t: (not t[2]) and t[0] < t[1])(store.corridor(conf, s, S, form))
        ]
        for e in (lo, hi):
            if e not in (INF, -INF):
                ends.add(round(e, 7))
        steps.append(
            {
                "Z": Z,
                "sym": store.SYM[Z - 1],
                "ent": store.ENT[Z],
                "L": None if lo == -INF else round(lo, 7),
                "U": None if hi == INF else round(hi, 7),
                "ok": (not bad) and lo < hi,
                "nA": len(A),
                "A": A,
                "k": store.kpick(S),
                "hull": [
                    {"s": s, "x": round(store.x(s, conf, form), 6), "y": store.y(s)}
                    for s in H
                ],
                "pts": [
                    {"s": s, "x": round(store.x(s, conf, form), 6), "y": store.y(s)}
                    for s in S
                ],
            }
        )

    # the walk of register 1328: hold a if inside, else the nearest endpoint
    a = None
    for st in steps:
        lo = -INF if st["L"] is None else st["L"]
        hi = INF if st["U"] is None else st["U"]
        if a is None or not (lo < a < hi):
            new = (lo if lo != -INF else (hi if hi != INF else 0.0)) if a is None \
                else (lo if a <= lo else hi)
            if new in (INF, -INF):
                new = 0.0
            if abs(new) < 1e-12:
                new = 0.0
            st["reset"] = (a is None) or abs(new - a) > 1e-12
            a = new
        else:
            st["reset"] = False
        st["a"] = round(a, 7)

    grid = [i / 1000.0 for i in range(-1000, 5001)]
    cov = [
        sum(
            1
            for st in steps
            if (st["L"] is None or g > st["L"]) and (st["U"] is None or g < st["U"])
        )
        for g in grid
    ]
    bi = max(range(len(grid)), key=lambda i: cov[i])

    lo_r, hi_r, empties = -INF, INF, []
    for st in steps:
        lo = -INF if st["L"] is None else st["L"]
        hi = INF if st["U"] is None else st["U"]
        nlo, nhi = max(lo_r, lo), min(hi_r, hi)
        if nlo >= nhi:
            empties.append(st["Z"])
            lo_r, hi_r = lo, hi
        else:
            lo_r, hi_r = nlo, nhi

    return {
        "steps": steps,
        "ends": sorted(ends),
        "cov": cov,
        "gridMin": -1.0,
        "gridStep": 0.001,
        "bestA": round(grid[bi], 4),
        "bestCov": cov[bi],
        "empties": empties,
    }


def object_for(store):
    return {
        "forms": {f: build(store, f) for f in ("p", "q")},
        "edges": [{"z": z, "label": t} for z, t in EDGES],
    }


TEMPLATE = """<title>The Slope Axis</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,300;0,400;0,600;0,700;1,400&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<style>
:root{
  --ink:#191b21; --ink-2:#4a4f59; --ink-3:#787d86;
  --paper:#ecefe9; --panel:#f5f7f2; --rule:#c8ccc3; --rule-2:#dde0d8;
  --indigo:#2e3c6b; --sodium:#b3760f; --halpha:#a93a33; --teal:#2f6b72;
  --covered:#2e3c6b; --on-accent:#ecefe9; --font-d:"Spectral",Georgia,"Times New Roman",serif;
  --font-m:"IBM Plex Mono",ui-monospace,"SFMono-Regular",Menlo,monospace;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --ink:#dfe3da; --ink-2:#a2a89c; --ink-3:#767d72;
  --paper:#111318; --panel:#181b21; --rule:#333944; --rule-2:#252a32;
  --indigo:#8ea3e0; --sodium:#e0a33f; --halpha:#e0716a; --teal:#63b3b9;
  --covered:#8ea3e0; --on-accent:#111318;
}}
:root[data-theme="dark"]{
  --ink:#dfe3da; --ink-2:#a2a89c; --ink-3:#767d72;
  --paper:#111318; --panel:#181b21; --rule:#333944; --rule-2:#252a32;
  --indigo:#8ea3e0; --sodium:#e0a33f; --halpha:#e0716a; --teal:#63b3b9;
  --covered:#8ea3e0; --on-accent:#111318;
}
*{box-sizing:border-box}
body{background:var(--paper);color:var(--ink);font-family:var(--font-d);
  font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased}
.wrap{max-width:1180px;margin:0 auto;padding:40px 28px 80px}
h1{font-size:clamp(30px,4.4vw,50px);font-weight:600;letter-spacing:-.02em;margin:0 0 6px;
  text-wrap:balance;line-height:1.08}
.sub{font-family:var(--font-m);font-size:11px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--ink-3);margin:0 0 26px}
.lede{max-width:64ch;color:var(--ink-2);font-size:17.5px;margin:0 0 30px}
.lede em{color:var(--ink);font-style:italic}
h2{font-size:12px;font-family:var(--font-m);font-weight:600;letter-spacing:.15em;
  text-transform:uppercase;color:var(--ink-3);margin:0 0 14px;
  padding-bottom:8px;border-bottom:1px solid var(--rule)}
.defn{display:grid;grid-template-columns:repeat(auto-fit,minmax(228px,1fr));gap:0;
  border:1px solid var(--rule);background:var(--panel);margin:0 0 40px}
.defn>div{padding:20px 22px;border-right:1px solid var(--rule-2)}
.defn>div:last-child{border-right:0}
.defn h3{font-family:var(--font-m);font-size:10.5px;letter-spacing:.13em;text-transform:uppercase;
  color:var(--ink-3);margin:0 0 10px;font-weight:600}
.defn p{margin:0;font-size:14.5px;line-height:1.55;color:var(--ink-2)}
.defn b{color:var(--ink);font-weight:600}
.eq{font-family:var(--font-m);font-size:15px;color:var(--indigo);display:block;margin:0 0 9px}
.stage{display:grid;grid-template-columns:1fr 380px;gap:34px;align-items:start}
@media(max-width:960px){.stage{grid-template-columns:1fr}}
.side{position:sticky;top:22px;display:flex;flex-direction:column;gap:22px}
@media(max-width:960px){.side{position:static}}
.ctl{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:0 0 16px}
button{font-family:var(--font-m);font-size:11px;letter-spacing:.05em;
  background:var(--panel);color:var(--ink-2);border:1px solid var(--rule);padding:7px 12px;
  cursor:pointer;transition:.12s}
button:hover{color:var(--ink);border-color:var(--ink-3)}
button[aria-pressed="true"]{background:var(--indigo);border-color:var(--indigo);color:var(--on-accent)}
button:focus-visible{outline:2px solid var(--sodium);outline-offset:2px}
.readout{border:1px solid var(--rule);background:var(--panel)}
.readout .r{display:flex;justify-content:space-between;align-items:baseline;gap:12px;
  padding:9px 16px;border-bottom:1px solid var(--rule-2)}
.readout .r:last-child{border-bottom:0}
.readout .k{font-family:var(--font-m);font-size:10.5px;letter-spacing:.08em;color:var(--ink-3)}
.readout .v{font-family:var(--font-m);font-size:14px;font-weight:500;color:var(--ink);
  font-variant-numeric:tabular-nums;text-align:right}
.big{font-family:var(--font-m);font-size:30px;font-weight:600;color:var(--indigo);
  font-variant-numeric:tabular-nums;line-height:1}
figure{margin:0}
figcaption{font-size:13.5px;color:var(--ink-3);margin-top:10px;max-width:62ch;line-height:1.5}
svg{display:block;width:100%;height:auto;overflow:visible}
.scroller{overflow-x:auto}
.legend{display:flex;flex-wrap:wrap;gap:16px;margin:14px 0 0;
  font-family:var(--font-m);font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-3)}
.legend span{display:flex;align-items:center;gap:6px}
.legend i{flex:none}
.sw{width:15px;height:3px;display:inline-block}
.note{border-left:2px solid var(--sodium);padding:2px 0 2px 16px;margin:38px 0 0;
  max-width:66ch;color:var(--ink-2);font-size:15.5px}
.note b{color:var(--ink)}
table{border-collapse:collapse;width:100%;font-size:14px;margin-top:6px}
th,td{text-align:left;padding:8px 12px;border-bottom:1px solid var(--rule-2)}
th{font-family:var(--font-m);font-size:10px;letter-spacing:.11em;text-transform:uppercase;
  color:var(--ink-3);font-weight:600}
td.n{font-family:var(--font-m);font-variant-numeric:tabular-nums;text-align:right;white-space:nowrap}
tr.hi td{background:color-mix(in srgb,var(--sodium) 11%,transparent)}
@media(prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
</style>
<div class="wrap">
<header>
  <h1>The Slope Axis</h1>
  <p class="sub">The Method 1.6 · §34.4–34.6 · Z = 3 to 108, four edges to 120</p>
  <p class="lede">Every element in the index sits on one axis, and the axis is <em>a</em> — not a
  fitted constant but a <em>slope</em>. Each candidate subshell is a point in a plane; the incoming
  electron takes the point a line of slope <em>a</em> touches first, sweeping up from below. An
  element's place on the axis is the wedge of slopes for which its observed entrant is that first
  point of contact.</p>
</header>

<section class="defn">
  <div>
    <h3>The rule</h3>
    <span class="eq">ν = n − a·√r</span>
    <p>with <b>r = p + q/2(2ℓ+1)</b>, the node count and the filled fraction of capacity. Least ν
    takes the electron (§34.4).</p>
  </div>
  <div>
    <h3>The plane</h3>
    <span class="eq">s ↦ ( √r , n )</span>
    <p>Minimising <b>n − a·√r</b> is minimising <b>y − a·x</b>. Each admissible subshell is a
    <b>point</b>; nothing else about it enters.</p>
  </div>
  <div>
    <h3>The axis</h3>
    <span class="eq">a ∈ ℝ — a slope</span>
    <p>A line of slope <i>a</i> rising from below stops at one point. Only <b>vertices of the lower
    convex hull</b> can ever be that point.</p>
  </div>
  <div>
    <h3>The element's place</h3>
    <span class="eq">L(Z) &lt; a &lt; U(Z)</span>
    <p>The two <b>hull-edge slopes</b> flanking the observed entrant. Verified identical to the
    corridor at 106 of 106 steps, both forms.</p>
  </div>
</section>

<div class="ctl">
  <button id="fp" aria-pressed="true">node-only&nbsp; ν = n − a√p</button>
  <button id="fq" aria-pressed="false">finished&nbsp; ν = n − a√(p+q/cap)</button>
  <button id="best">go to best fixed a</button>
  <button id="walkbtn" aria-pressed="true">show the walk</button>
</div>

<div class="stage">
  <figure>
    <h2>The index on one axis</h2>
    <div class="scroller"><svg id="stack" viewBox="0 0 760 660" role="img"
      aria-label="106 elements as intervals on the slope axis a"></svg></div>
    <div class="legend">
      <span><i class="sw" style="background:var(--covered)"></i>covered at this a</span>
      <span><i class="sw" style="background:var(--rule)"></i>not covered</span>
      <span><i class="sw" style="background:var(--sodium)"></i>the walk</span>
      <span><i class="sw" style="background:var(--halpha)"></i>intersection empties</span>
    </div>
    <figcaption>Drag the vertical rule, or click any element. Each bar is one element's wedge of
    admissible slopes. A bar running off an edge is one-sided — no rival bounds it on that side.</figcaption>
  </figure>

  <div class="side">
    <div>
      <h2>At this slope</h2>
      <div class="readout">
        <div class="r"><span class="k">slope a</span><span class="v big" id="aVal">0.5780</span></div>
        <div class="r"><span class="k">elements covered</span><span class="v" id="cov">86 / 106</span></div>
        <div class="r"><span class="k">best any fixed a</span><span class="v" id="bestv">86 at a = 0.5780</span></div>
        <div class="r"><span class="k">distinct edge slopes</span><span class="v" id="ends">17</span></div>
        <div class="r"><span class="k">running intersection empties</span><span class="v" id="emp">14×</span></div>
      </div>
    </div>
    <figure>
      <h2>The plane at <span id="elName" style="font-family:var(--font-m);font-size:12px">Z = 57 La</span></h2>
      <svg id="plane" viewBox="0 0 380 300" role="img" aria-label="point set and lower convex hull"></svg>
      <figcaption id="planeCap"></figcaption>
    </figure>
    <div>
      <h2>Hull vertices here</h2>
      <table id="hullTab"><thead><tr><th>subshell</th><th>√r</th><th>n</th><th>k</th></tr></thead><tbody></tbody></table>
    </div>
  </div>
</div>

<div class="note">
  <b>What the picture says about state.</b> A single <i>a</i> is a single vertical rule. The rule
  never crosses all 106 bars — the best it reaches is 86 (node-only) or 90 (finished), and the
  running intersection empties 14 times, resp. 11. That is what “the state is necessary” establishes:
  necessary <b>to this rule</b>, so that <i>a</i> may be re-set and remain exact. It is not a claim
  about the periodic table, and the index does not support one — the memoryless least-(n+ℓ) rule
  carries nothing and scores <b>96 of 106</b>, and its pick lies inside the corridor at every step.
</div>

<div class="note" style="border-left-color:var(--teal)">
  <b>Why no fixed slope reproduces Madelung.</b> k = n + ℓ and p = n − ℓ − 1, so <b>k = 2n − p − 1</b>
  — and with x = √p, that is <b>k = 2y − x² − 1</b>. In this plane ν sweeps a family of <i>lines</i>
  and the Madelung rule sweeps a family of <i>parabolas</i>. They agree over most of the occupied
  region and cannot agree everywhere: the best fixed <i>a</i> matches the k-rule at 88 of 106
  (node-only), 91 (finished).
</div>

<div class="note" style="border-left-color:var(--halpha)">
  <b>Four edges, not two</b> (register 1304). Optical spectroscopy ends at <b>Z = 102</b>, No.
  NIST ASD lists no neutral ground configuration past <b>Z = 108</b>, Hs. Synthesis ends at
  <b>Z = 118</b>, Og. Janet's lattice counts <b>120</b> cells. The axis above is drawn on the 106
  steps the collection holds; everything beyond 108 is a different kind of row, and the plate does
  not pretend otherwise.
</div>
</div>
<script id="axisdata" type="application/json">@@DATA@@</script>
<script>
(function(){
const D=JSON.parse(document.getElementById('axisdata').textContent);
const NS='http://www.w3.org/2000/svg';
let form='p', A=0.578, sel=57, showWalk=true;

const el=id=>document.getElementById(id);
const mk=(t,at)=>{const n=document.createElementNS(NS,t);for(const k in at)n.setAttribute(k,at[k]);return n;};
const F=()=>D.forms[form];
const lo=s=>s.L===null?-1e9:s.L, hi=s=>s.U===null?1e9:s.U;

// ---- domain of the slope axis, from the data
function domain(){
  let mn=Infinity,mx=-Infinity;
  F().steps.forEach(s=>{if(s.L!==null){mn=Math.min(mn,s.L);mx=Math.max(mx,s.L);}
                        if(s.U!==null){mn=Math.min(mn,s.U);mx=Math.max(mx,s.U);}});
  const pad=(mx-mn)*0.07; return [mn-pad, mx+pad];
}
const M={l:46,r:20,t:26,b:44}, W=760, H=660;
let dom=domain();
const px=a=>M.l+(a-dom[0])/(dom[1]-dom[0])*(W-M.l-M.r);
const ax=x=>dom[0]+(x-M.l)/(W-M.l-M.r)*(dom[1]-dom[0]);
const rowH=(H-M.t-M.b)/106, py=i=>M.t+i*rowH;

function coverage(a){let c=0;F().steps.forEach(s=>{if(a>lo(s)&&a<hi(s))c++;});return c;}

// ---------------------------------------------------------------- the stack
function drawStack(){
  const svg=el('stack'); svg.textContent=''; dom=domain();
  const emp=new Set(F().empties);

  // axis ticks at every distinct edge slope, labelled sparsely
  const g0=mk('g',{}); svg.appendChild(g0);
  F().ends.forEach(e=>{
    if(e<dom[0]||e>dom[1])return;
    g0.appendChild(mk('line',{x1:px(e),x2:px(e),y1:M.t-6,y2:H-M.b,
      stroke:'var(--rule-2)','stroke-width':1}));
  });
  for(let v=Math.ceil(dom[0]);v<=Math.floor(dom[1]);v++){
    g0.appendChild(mk('line',{x1:px(v),x2:px(v),y1:M.t-6,y2:H-M.b+6,stroke:'var(--rule)','stroke-width':1}));
    const t=mk('text',{x:px(v),y:H-M.b+22,'text-anchor':'middle',fill:'var(--ink-3)',
      'font-family':'var(--font-m)','font-size':11}); t.textContent=v.toFixed(0); g0.appendChild(t);
  }
  const al=mk('text',{x:W-M.r,y:H-M.b+38,'text-anchor':'end',fill:'var(--ink-3)',
    'font-family':'var(--font-m)','font-size':10.5,'letter-spacing':'0.12em'});
  al.textContent='SLOPE  a  →'; svg.appendChild(al);

  // bars
  const gb=mk('g',{}); svg.appendChild(gb);
  F().steps.forEach((s,i)=>{
    const y=py(i), cov=(A>lo(s)&&A<hi(s));
    const x1=Math.max(M.l, px(Math.max(lo(s),dom[0]-1)));
    const x2=Math.min(W-M.r, px(Math.min(hi(s),dom[1]+1)));
    gb.appendChild(mk('rect',{x:x1,y:y+0.6,width:Math.max(1.2,x2-x1),height:rowH-1.3,
      fill:cov?'var(--covered)':'var(--rule)',opacity:cov?0.82:0.5,
      'data-z':s.Z,class:'bar'}));
    if(s.Z===sel){
      gb.appendChild(mk('rect',{x:M.l,y:y,width:W-M.l-M.r,height:rowH,
        fill:'var(--sodium)',opacity:0.16}));
      gb.appendChild(mk('path',{d:'M'+(M.l-9)+' '+(y+rowH/2-3.4)+'L'+(M.l-3)+' '+(y+rowH/2)+
        'L'+(M.l-9)+' '+(y+rowH/2+3.4)+'Z',fill:'var(--sodium)'}));
    }
    if(emp.has(s.Z)) gb.appendChild(mk('circle',{cx:M.l-13,cy:y+rowH/2,r:2.1,fill:'var(--halpha)'}));
    if(s.Z%10===0||s.Z===3){
      const t=mk('text',{x:M.l-20,y:y+rowH/2+3.4,'text-anchor':'end',fill:'var(--ink-3)',
        'font-family':'var(--font-m)','font-size':9.5}); t.textContent=s.Z; gb.appendChild(t);
    }
  });

  // the walk
  if(showWalk){
    let d='';
    F().steps.forEach((s,i)=>{const x=px(s.a),y=py(i)+rowH/2;
      d+=(i===0?'M':(s.reset?'M':'L'))+x.toFixed(1)+' '+y.toFixed(1)+' ';
      if(s.reset&&i>0){ // vertical jump drawn faintly
        const pv=F().steps[i-1];
        svg.appendChild(mk('line',{x1:px(pv.a),y1:py(i-1)+rowH/2,x2:x,y2:y,
          stroke:'var(--sodium)','stroke-width':0.9,'stroke-dasharray':'2 2',opacity:0.55}));
      }});
    svg.appendChild(mk('path',{d:d,fill:'none',stroke:'var(--sodium)','stroke-width':1.6,opacity:0.95}));
  }

  // the scrubber
  const gs=mk('g',{id:'scrub'}); svg.appendChild(gs);
  gs.appendChild(mk('line',{x1:px(A),x2:px(A),y1:M.t-14,y2:H-M.b+6,
    stroke:'var(--ink)','stroke-width':1.6}));
  gs.appendChild(mk('rect',{x:px(A)-15,y:M.t-30,width:30,height:17,fill:'var(--ink)'}));
  const lt=mk('text',{x:px(A),y:M.t-18,'text-anchor':'middle',fill:'var(--paper)',
    'font-family':'var(--font-m)','font-size':10,'font-weight':600});
  lt.textContent=A.toFixed(3); gs.appendChild(lt);

  // hit layer
  const hit=mk('rect',{x:0,y:0,width:W,height:H,fill:'transparent',style:'cursor:col-resize'});
  svg.appendChild(hit);
  const move=ev=>{
    const r=svg.getBoundingClientRect();
    const cx=((ev.touches?ev.touches[0].clientX:ev.clientX)-r.left)/r.width*W;
    A=Math.max(dom[0],Math.min(dom[1],ax(cx)));
    const ry=((ev.touches?ev.touches[0].clientY:ev.clientY)-r.top)/r.height*H;
    const i=Math.floor((ry-M.t)/rowH);
    if(i>=0&&i<106) sel=F().steps[i].Z;
    render();
  };
  let down=false;
  hit.addEventListener('pointerdown',e=>{down=true;hit.setPointerCapture(e.pointerId);move(e);});
  hit.addEventListener('pointermove',e=>{if(down)move(e);});
  hit.addEventListener('pointerup',e=>{down=false;});
  hit.addEventListener('click',move);
}

// ---------------------------------------------------------------- the plane
function drawPlane(){
  const svg=el('plane'); svg.textContent='';
  const s=F().steps.find(t=>t.Z===sel); if(!s)return;
  const m={l:38,r:16,t:16,b:34}, w=380, h=300;
  const xs=s.pts.map(p=>p.x), ys=s.pts.map(p=>p.y);
  const xmax=Math.max(...xs)*1.12+0.12, ymin=Math.min(...ys)-0.55, ymax=Math.max(...ys)+0.55;
  const X=v=>m.l+v/xmax*(w-m.l-m.r);
  const Y=v=>h-m.b-(v-ymin)/(ymax-ymin)*(h-m.t-m.b);

  // frame
  svg.appendChild(mk('line',{x1:m.l,y1:h-m.b,x2:w-m.r,y2:h-m.b,stroke:'var(--rule)','stroke-width':1}));
  svg.appendChild(mk('line',{x1:m.l,y1:m.t,x2:m.l,y2:h-m.b,stroke:'var(--rule)','stroke-width':1}));
  for(let n=Math.ceil(ymin);n<=Math.floor(ymax);n++){
    svg.appendChild(mk('line',{x1:m.l,y1:Y(n),x2:w-m.r,y2:Y(n),stroke:'var(--rule-2)','stroke-width':1}));
    const t=mk('text',{x:m.l-8,y:Y(n)+3.5,'text-anchor':'end',fill:'var(--ink-3)',
      'font-family':'var(--font-m)','font-size':10}); t.textContent=n; svg.appendChild(t);
  }
  for(let v=0;v<=Math.floor(xmax);v++){
    const t=mk('text',{x:X(v),y:h-m.b+16,'text-anchor':'middle',fill:'var(--ink-3)',
      'font-family':'var(--font-m)','font-size':10}); t.textContent=v; svg.appendChild(t);
  }
  const xl=mk('text',{x:w-m.r,y:h-m.b+30,'text-anchor':'end',fill:'var(--ink-3)',
    'font-family':'var(--font-m)','font-size':9.5,'letter-spacing':'0.1em'});
  xl.textContent='√r →'; svg.appendChild(xl);
  const yl=mk('text',{x:m.l-8,y:m.t-4,'text-anchor':'end',fill:'var(--ink-3)',
    'font-family':'var(--font-m)','font-size':9.5}); yl.textContent='n'; svg.appendChild(yl);

  // the sweep line of slope A, tangent to the hull
  let c=Infinity, touch=null;
  s.pts.forEach(p=>{const v=p.y-A*p.x; if(v<c){c=v;touch=p;}});
  svg.appendChild(mk('line',{x1:X(0),y1:Y(c),x2:X(xmax),y2:Y(c+A*xmax),
    stroke:'var(--ink-3)','stroke-width':1.1,'stroke-dasharray':'4 3'}));

  // the lower hull
  let d='';
  s.hull.forEach((p,i)=>{d+=(i?'L':'M')+X(p.x).toFixed(1)+' '+Y(p.y).toFixed(1)+' ';});
  svg.appendChild(mk('path',{d:d,fill:'none',stroke:'var(--indigo)','stroke-width':1.8,opacity:0.9}));

  // points
  s.pts.forEach(p=>{
    const onHull=s.hull.some(q=>q.s===p.s);
    const isEnt=(p.s===s.ent), isK=(p.s===s.k);
    svg.appendChild(mk('circle',{cx:X(p.x),cy:Y(p.y),r:isEnt?5:(onHull?3.6:2.4),
      fill:isEnt?'var(--sodium)':(onHull?'var(--indigo)':'var(--rule)'),
      stroke:isK&&!isEnt?'var(--teal)':'none','stroke-width':2}));
    if(onHull||isEnt||isK){
      const nearY=p.x<xmax*0.06;
      const t=mk('text',{x:nearY?X(p.x)+10:X(p.x),y:nearY?Y(p.y)+3.5:Y(p.y)-9,
        'text-anchor':nearY?'start':'middle',
        fill:isEnt?'var(--sodium)':'var(--ink-2)','font-family':'var(--font-m)','font-size':10,
        'font-weight':isEnt?600:400}); t.textContent=p.s; svg.appendChild(t);
    }
  });
  if(touch) svg.appendChild(mk('circle',{cx:X(touch.x),cy:Y(touch.y),r:8.5,fill:'none',
    stroke:'var(--ink)','stroke-width':1.2,opacity:0.75}));

  el('elName').textContent='Z = '+s.Z+' '+s.sym;
  const hit=(touch&&touch.s===s.ent);
  el('planeCap').innerHTML='Observed entrant <b style="color:var(--sodium)">'+s.ent+'</b>; '+
    s.hull.length+' hull vertices of '+s.pts.length+' admissible. At a = '+A.toFixed(3)+
    ' the line touches <b>'+(touch?touch.s:'—')+'</b> — '+
    (hit?'the observed subshell.':'not the observed one.')+
    ' k-rule picks <b style="color:var(--teal)">'+s.k+'</b>.';

  const tb=el('hullTab').querySelector('tbody'); tb.textContent='';
  s.hull.forEach(p=>{
    const n=parseInt(p.s[0],10), l='spdf'.indexOf(p.s[1]);
    const tr=document.createElement('tr'); if(p.s===s.ent) tr.className='hi';
    tr.innerHTML='<td>'+p.s+'</td><td class="n">'+p.x.toFixed(4)+'</td><td class="n">'+
      p.y+'</td><td class="n">'+(n+l)+'</td>';
    tb.appendChild(tr);
  });
}

function render(){
  drawStack(); drawPlane();
  el('aVal').textContent=A.toFixed(4);
  el('cov').textContent=coverage(A)+' / 106';
  el('bestv').textContent=F().bestCov+' at a = '+F().bestA.toFixed(4);
  el('ends').textContent=F().ends.length;
  el('emp').textContent=F().empties.length+'×';
}
el('fp').onclick=()=>{form='p';A=Math.min(Math.max(A,-0.3),4.9);
  el('fp').setAttribute('aria-pressed','true');el('fq').setAttribute('aria-pressed','false');render();};
el('fq').onclick=()=>{form='q';
  el('fq').setAttribute('aria-pressed','true');el('fp').setAttribute('aria-pressed','false');render();};
el('best').onclick=()=>{A=F().bestA;render();};
el('walkbtn').onclick=()=>{showWalk=!showWalk;
  el('walkbtn').setAttribute('aria-pressed',showWalk?'true':'false');render();};
render();
})();
</script>
"""


def emit_html(obj, path):
    html = TEMPLATE.replace("@@DATA@@", json.dumps(obj, separators=(",", ":")))
    d = os.path.dirname(os.path.abspath(path))
    if d:
        os.makedirs(d, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(html)
    return len(html)


def report(store, obj):
    print("THE SLOPE AXIS -- Chapter 34's occupation law as one object")
    print("  the axis is `a`, a SLOPE; each subshell is the point (sqrt(r), n)")
    print("  an element's place is the interval between the hull-edge slopes flanking its entrant")
    for form, name in (("p", "node-only  nu = n - a*sqrt(p)"),
                       ("q", "finished   nu = n - a*sqrt(p + q/cap)")):
        F = obj["forms"][form]
        ne = sum(1 for s in F["steps"] if s["ok"])
        print("\n  FORM: %s" % name)
        print("    steps                                    : %d" % len(F["steps"]))
        print("    entrant corridor non-empty               : %d of 106" % ne)
        print("    distinct hull-edge slopes                : %d" % len(F["ends"]))
        print("    best coverage by ONE fixed a (a in R)    : %d of 106 at a = %.4f"
              % (F["bestCov"], F["bestA"]))
        print("    running intersection empties             : %d times at %s"
              % (len(F["empties"]), " ".join(map(str, F["empties"]))))
        print("    walk resets (register 1328 discipline)   : %d"
              % sum(1 for s in F["steps"] if s["reset"]))
        h = {}
        for s in F["steps"]:
            h[s["nA"]] = h.get(s["nA"], 0) + 1
        print("    |A| histogram (a in R)                   : %s ; steps with |A| = 1: %d"
              % (dict(sorted(h.items())), h.get(1, 0)))
    print("\n  FOUR EDGES (register 1304) -- annotation, not rows:")
    for z, t in EDGES:
        print("    Z = %-3d  %s" % (z, t))


def selftest(store):
    """Fixtures are the corpus's own recorded numbers."""
    obj = object_for(store)
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok = ok and good
        print("  %-58s %-26s %s" % (label, got, "OK" if good else "FAIL want %s" % (want,)))

    # the identity this instrument exists to assert
    for form in ("p", "q"):
        mism = 0
        for Z in range(3, 109):
            conf = store.CONF[Z - 1]
            S = store.admissible(Z)
            cor = {
                s for s in S
                if (lambda t: (not t[2]) and t[0] < t[1])(store.corridor(conf, s, S, form))
            }
            if cor != set(store.hull(conf, S, form)):
                mism += 1
        chk("form %s: corridor set vs lower-hull vertices, mismatches" % form, mism, 0)

    for form, ends, emp, res, best in (("p", 17, 14, 10, 86), ("q", 121, 11, 15, 90)):
        F = obj["forms"][form]
        chk("form %s: distinct hull-edge slopes" % form, len(F["ends"]), ends)
        chk("form %s: running intersection empties (register 1463)" % form, len(F["empties"]), emp)
        chk("form %s: walk resets (register 1328)" % form,
            sum(1 for s in F["steps"] if s["reset"]), res)
        chk("form %s: best coverage by one fixed a" % form, F["bestCov"], best)
        chk("form %s: steps with |A| = 1" % form,
            sum(1 for s in F["steps"] if s["nA"] == 1), 0)
        chk("form %s: entrant corridor non-empty" % form,
            sum(1 for s in F["steps"] if s["ok"]), 106)
        chk("form %s: observed entrant is a hull vertex" % form,
            sum(1 for s in F["steps"] if s["ent"] in [h["s"] for h in s["hull"]]), 106)

    # register 1463 names the fourteen emptying points of the node-only form
    chk("node-only emptying points (register 1463)",
        obj["forms"]["p"]["empties"],
        [37, 42, 43, 45, 55, 58, 64, 65, 80, 91, 96, 97, 103, 104])

    # section 34.5 prints La's corridor; it must equal the flanking hull-edge slopes
    conf = store.CONF[56]
    S = store.admissible(57)
    H = store.hull(conf, S, "p")
    i = H.index("5d")
    sl = lambda A, B: (store.y(B) - store.y(A)) / (store.x(B, conf, "p") - store.x(A, conf, "p"))
    lo, hi, _ = store.corridor(conf, "5d", S, "p")
    chk("La 5d: lower hull-edge slope == corridor L",
        round(sl(H[i - 1], H[i]), 7), round(lo, 7))
    chk("La 5d: upper hull-edge slope == corridor U",
        round(sl(H[i], H[i + 1]), 7), round(hi, 7))

    # k = 2n - p - 1 : the Madelung number is a function of the pair nu already uses
    chk("k = 2n - p - 1 on every subshell, exceptions",
        sum(1 for s in store.ALL if store.k_of(s) != 2 * store.nl(s)[0] - store.p_of(s) - 1), 0)

    # register 1437: the memoryless least-(n+l) rule scores 96
    chk("memoryless k-rule score (register 1437)",
        sum(1 for Z in range(3, 109) if store.kpick(store.admissible(Z)) == store.ENT[Z]), 96)

    print("\n%s" % ("SELFTEST OK" if ok else "SELFTEST FAILED"))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description="the occupation law of Chapter 34 as one object")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--json", metavar="PATH")
    ap.add_argument("--html", metavar="PATH")
    a = ap.parse_args()
    store = Store()
    if a.selftest:
        return selftest(store)
    obj = object_for(store)
    if a.json:
        d = os.path.dirname(os.path.abspath(a.json))
        if d:
            os.makedirs(d, exist_ok=True)
        with open(a.json, "w", encoding="utf-8") as fh:
            json.dump(obj, fh, separators=(",", ":"))
        print("wrote %s" % a.json)
    if a.html:
        n = emit_html(obj, a.html)
        print("wrote %s (%d bytes)" % (a.html, n))
    if a.report or not (a.json or a.html):
        report(store, obj)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
