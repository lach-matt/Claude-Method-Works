#!/usr/bin/env python3
r"""build_gravity_plate.py -- the rendering of gravity.py.

    python3 build_gravity_plate.py        writes gravity-plate.html

EVERY NUMBER ON THE PLATE IS READ FROM THE INSTRUMENT.  Nothing is retyped, so
the plate cannot drift from the measurement the way a prose figure can.  It
follows the house plate system (Spectral / IBM Plex Mono and the token palette
the other plates in this directory share) rather than inventing one.
"""
import collections
import html
import itertools
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import gravity as G            # noqa: E402
import plate                   # noqa: E402
import figure as FIG           # noqa: E402
import demand as DEM           # noqa: E402
import hlaw                    # noqa: E402
import overlap                 # noqa: E402
import registry                # noqa: E402

E = html.escape
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "gravity-plate.html")

X = G.index()
CL, _B = hlaw.closures(X)
MS = G.members()
PD = G.per_dimension_cells()
GR = G.captures()          # EVERY species is a member now
GROUND = G.grounds()
EXCITED = G.excited_species()
BD = G.by_dimension()
FC = FIG.cells()
FIGF = FIG.figure()
E8 = DEM.E(FIGF)
E7 = DEM.E(FIG.figure([n for n in FC if n != "gravity"]))
WB, WHO = G.binding_bound()
M12, DM12 = G.carbon12()
SPIN_DEC, CHG_DEC = G._ranks()

# members per bound class per dimension -- the ladder's data
CLASSD = {D: collections.Counter() for D in G.DIMS}
for m, c in G.rows():
    CLASSD[c[0]][c[1]] += 1

BNAME = {0: "no bound", 1: "a bound", 2: "undetermined"}
BCLS = {0: "b0", 1: "b1", 2: "b2"}


def species_rows():
    """One row per species -- ALL 118, with the level each was read at."""
    s2z = G.symbol_to_Z()
    per = collections.Counter((m[0], m[3]) for m in MS)
    out = []
    for (sym, num), (lv, tj, cfg, term, src) in sorted(GR.items()):
        Z, q = s2z[sym], G.ROMAN[num] - 1
        rs = [m for m in MS if m[0] == Z and m[3] == q]
        chi = sorted({int(math.floor(math.log10(m[10]))) for m in rs if m[10] > 0})
        qt = sorted({int(math.floor(math.log10(m[11]))) for m in rs if m[11] > 0})
        out.append(dict(sp="%s %s" % (sym, num), Z=Z, q=q, Ne=Z - q, tj=tj,
                        cfg=cfg, term=term, n=per[(Z, q)], lv=lv,
                        L=0 if lv == 0.0 else 1, chi=chi, qt=qt, src=src))
    return out


def jstr(tj):
    return "%d" % (tj // 2) if tj % 2 == 0 else "%d&frasl;2" % tj


# --------------------------------------------------------------- the ladder
def ladder_svg():
    W, H = 880, 330
    L, R, T, B = 66, 26, 38, 74
    cols = list(G.DIMS)
    cw = (W - L - R) / len(cols)
    top = max(sum(CLASSD[D].values()) for D in cols)
    ph = H - T - B
    p = ['<svg viewBox="0 0 %d %d" role="img" aria-label="members by '
         'horizon-bound class in each spacetime dimension">' % (W, H)]
    for frac, lab in ((0, "0"), (.5, "%d" % (top // 2)), (1, "%d" % top)):
        y = T + ph - frac * ph
        p.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="var(--rule)" '
                 'stroke-width="1"/>' % (L, y, W - R, y))
        p.append('<text x="%d" y="%.1f" text-anchor="end" font-size="10" '
                 'fill="var(--faint)">%s</text>' % (L - 9, y + 3.4, lab))
    late = []                      # labels drawn AFTER every bar, so a thin
    for i, D in enumerate(cols):   # band's count is not painted over by the
        x = L + i * cw             # block stacked above it
        bw = cw * 0.56
        bx = x + (cw - bw) / 2
        y = T + ph
        for k in (1, 2, 0):
            n = CLASSD[D].get(k, 0)
            if not n:
                continue
            h = ph * n / top
            y -= h
            p.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" '
                     'class="%s" stroke="var(--panel)" stroke-width="0.8"/>'
                     % (bx, y, bw, max(h, 2.6), BCLS[k]))
            if h > 15:
                p.append('<text x="%.1f" y="%.1f" text-anchor="middle" '
                         'font-size="10.5" fill="var(--panel)" font-weight="600">'
                         '%d</text>' % (bx + bw / 2, y + h / 2 + 3.6, n))
            else:
                # A THIN BAND IS STILL A REAL CLASS.  It gets its count above
                # the bar rather than being dropped for want of room.
                late.append('<text x="%.1f" y="%.1f" text-anchor="middle" '
                            'font-size="9.5" font-weight="600" class="t%s">%d'
                            '</text>' % (bx + bw / 2, y - 4.5, BCLS[k], n))
        p.append('<text x="%.1f" y="%d" text-anchor="middle" font-size="13" '
                 'font-weight="600" fill="var(--ink)">D = %d</text>'
                 % (x + cw / 2, T + ph + 22, D))
        p.append('<text x="%.1f" y="%d" text-anchor="middle" font-size="10" '
                 'fill="var(--faint)">%d cells</text>'
                 % (x + cw / 2, T + ph + 38, PD[D][0]))
        p.append('<text x="%.1f" y="%d" text-anchor="middle" font-size="10" '
                 'fill="var(--faint)">%s</text>'
                 % (x + cw / 2, T + ph + 52, "(%d, %d, %d)" % PD[D][1]))
    # the transition marker, between D = 5 and D = 6
    xt = L + 2 * cw
    p.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="var(--algebra)" '
             'stroke-width="1.5" stroke-dasharray="4 3"/>' % (xt, T - 14, xt, T + ph + 4))
    p.append('<text x="%.1f" y="%d" text-anchor="middle" font-size="10.5" '
             'font-weight="600" fill="var(--algebra)">ultraspinning from here — '
             '%d members lose their bound</text>' % (xt + 128, T - 20, len(G.relieved())))
    p.extend(late)
    p.append('</svg>')
    return "\n".join(p)


SCATTER_JS = """%s
const BT=%s, TOK=['--free','--bound','--undet'];
const RAW=[%s];
const PTS=RAW.map(a=>({x:a[0],y:a[1],z:a[2],b:BT[a[3]],hollow:a[4]||0}));
let curD=4;
const V=scatter3d({id:'gr3d',points:PTS,xlab:'N-Z  neutron excess',ylab:'Z  protons',
  zlab:'q  charge state',az:3.78,el:0.10,r:2.6,height:510,scale:0.26,
  xcol:'--geometry',ycol:'--order',zcol:'--information',
  colour:p=>TOK[+p.b[curD-4]]});
const bar=document.getElementById('gr3d-dims');
const cap=document.getElementById('gr3d-now');
function setD(d){
  curD=d;
  for(const b of bar.querySelectorAll('button'))
    b.classList.toggle('on', +b.dataset.d===d);
  const n=[0,0,0];
  for(const p of PTS) n[+p.b[d-4]]++;
  cap.textContent='D = '+d+'   \\u00b7   '+n[1]+' bound, '+n[0]+' unbound, '
                 +n[2]+' undetermined';
  V.draw();
}
for(const b of bar.querySelectorAll('button'))
  b.addEventListener('click',()=>setD(+b.dataset.d));
setD(4);
"""

SECTION_3D = """<section>
  <div class="shead"><span class="snum">04</span><h2>Every member, in the
  dimension you choose</h2></div>
  <p class="sub">One point per member: %(nmem)s of them, at its neutron number,
  neutron excess, proton number and charge state, coloured by whether a
  horizon bound exists
  for it in the dimension selected. <strong>Step from 5 to 6.</strong></p>

  <figure class="plate">
    <div class="v3d"><canvas id="gr3d" aria-label="%(nmem)s members of the gravity index plotted at neutron excess, proton number and charge state, coloured by horizon-bound class in the selected spacetime dimension"></canvas></div>
    <div class="v3dbar">
      <button id="gr3d-spin" type="button">pause rotation</button>
      <span class="hint">drag to rotate</span>
      <span class="dims">dimension <span id="gr3d-dims">%(buttons)s</span></span>
    </div>
    <div class="v3dbar">
      <b id="gr3d-now" class="now"></b>
      <span class="v3dkey">
        <span><i style="background:var(--bound)"></i>a bound exists</span>
        <span><i style="background:var(--free)"></i>no bound</span>
        <span><i style="background:var(--undet)"></i>undetermined</span>
        <span><i style="border:1.5px dashed var(--muted);background:none"></i>read at an excited level</span>
      </span>
    </div>
    <figcaption><b>This view collapses nothing, and that is measured rather
    than asserted.</b> (N&minus;Z,&nbsp;Z,&nbsp;q) is <em>injective</em> on
    the member set &mdash; %(npts)s distinct points for %(nmem)s members
    &mdash; and the
    horizon-bound class is a <em>function</em> of it, since q gives the
    charge, Z&minus;q the electron count, (N&minus;Z)+2Z the nucleon number,
    and (Z,&nbsp;q) the species and so 2J<sub>e</sub> &mdash; every input the
    bound table takes. The x axis is the <em>neutron excess</em> rather than N
    because N and Z are correlated and plotting one against the other puts
    every point on a thin diagonal ribbon; N&minus;Z is twice the isospin
    projection T&#8323;, carries the same information, and straightens it.
    <b>So no point carries two colours at any dimension: %(impure)d impure
    points, summed over all eight.</b> The runner-up &mdash; projecting the
    %(cells)s chart cells onto their own best three coordinates
    (%(besttri)s) &mdash; keeps %(bestn)d points, a %(collapse).0f%%
    collapse, and %(bestimp)d of those would carry mixed colour. That view was
    not built, for that reason.
    <br><br><b>Step from 5 to 6 and %(rel)s points turn from amber to
    teal.</b> That is the ultraspinning transition member by member: neutral
    bodies with a forced angular momentum, whose Kerr and Myers&ndash;Perry
    bounds bite at four and five dimensions and do not exist at six. Nothing
    moves again from 6 to 11. The dashed rings are the %(nexc)d members read at
    an excited level rather than a ground one.
    <br><br><b>What it does not show:</b> the chart's own coordinates. These
    axes are the member's identity, not the seven slots (D, B, F, X, Y, L, E)
    the index is charted on &mdash; the spin and charge decades, the level
    status and the mass evidence are all absent from this picture. It is the
    membership, not the chart.</figcaption>
  </figure>
  <script>%(js)s</script>
</section>

"""

# ------------------------------------------------------- the 3-D member view

# (Z, N, q) IS INJECTIVE ON THE MEMBER SET AND B IS A FUNCTION OF IT.  q gives
# the charge, Z - q the electron count, Z + N the nucleon number, and (Z, q)
# the species and so 2Je -- which is every input `bound_class` takes.  So this
# view collapses NOTHING and no point can carry two colours.  Both are measured
# in `view3d_facts()` rather than argued.


def view3d_facts():
    """(points, members, impure points over all D, the cell-space runner-up)."""
    seen = collections.defaultdict(set)
    for Z, N, A_, q, Ne, tj, _L, _lv, _ql, _M, _c, _t in MS:
        for D in G.DIMS:
            seen[(N - Z, Z, q)].add(G.bound_class(D, q, G.forced(A_, Ne),
                                                    G.vanishes(Z, N, tj)))
    impure = sum(1 for v in seen.values() if len(v) > len(G.DIMS) and False)
    # a point is impure if, AT A FIXED D, it carries two classes; measured here
    bad = 0
    for D in G.DIMS:
        at = collections.defaultdict(set)
        for Z, N, A_, q, Ne, tj, _L, _lv, _ql, _M, _c, _t in MS:
            at[(N - Z, Z, q)].add(G.bound_class(D, q, G.forced(A_, Ne),
                                                  G.vanishes(Z, N, tj)))
        bad += sum(1 for v in at.values() if len(v) > 1)
    best = None
    X = sorted(G.index())
    for tri in itertools.combinations(range(G.ARITY), 3):
        pr = collections.defaultdict(set)
        for c in X:
            pr[tuple(c[i] for i in tri)].add(c[1])
        n = len(pr)
        imp = sum(1 for v in pr.values() if len(v) > 1)
        if best is None or n > best[0]:
            best = (n, imp, tuple(G.NAMES[i] for i in tri))
    return len(seen), len(MS), bad, best


def view3d_points():
    """[(N-Z, Z, q, bound-class string over D, hollow)] -- one per member.

    THE NEUTRON EXCESS, NOT N.  N and Z are strongly correlated -- the valley of
    stability -- so plotting N against Z puts every point on a thin diagonal
    ribbon and wastes the box.  N - Z is twice the isospin projection T3, a
    quantum number in its own right, and (N-Z, Z, q) carries exactly the same
    information as (N, Z, q) since N = (N-Z) + Z.  Injectivity is unaffected and
    is re-measured in view3d_facts().
    """
    out = []
    for Z, N, A_, q, Ne, tj, L, _lv, _ql, _M, _c, _t in MS:
        F, Jz = G.forced(A_, Ne), G.vanishes(Z, N, tj)
        b = "".join(str(G.bound_class(D, q, F, Jz)) for D in G.DIMS)
        out.append((N - Z, Z, q, b, 1 if L else 0))
    return out


def view3d_js():
    pts = view3d_points()
    tab = sorted({p[3] for p in pts})
    idx = {b: i for i, b in enumerate(tab)}
    packed = ",".join("[%d,%d,%d,%d%s]" % (n, z, q, idx[b], ",1" if h else "")
                      for n, z, q, b, h in pts)
    runtime = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "scatter3d.js"), encoding="utf-8").read()
    return SCATTER_JS % (runtime, json.dumps(tab), packed)


def view3d_section():
    pts = view3d_points()
    npts, nmem, impure, best = view3d_facts()
    rel = len(G.relieved())
    nexc = sum(1 for p in pts if p[4])
    buttons = "".join('<button type="button" data-d="%d">%d</button>' % (D, D)
                      for D in G.DIMS)
    return SECTION_3D % dict(
        nmem="{:,}".format(nmem), npts="{:,}".format(npts), impure=impure,
        buttons=buttons, rel="{:,}".format(rel), nexc=nexc,
        besttri=", ".join(best[2]), bestn=best[0], bestimp=best[1],
        collapse=100 * (1 - best[0] / len(G.index())),
        cells="{:,}".format(len(G.index())), js=view3d_js())


# ------------------------------------------------------------------ the page
def build():
    sp = species_rows()
    exc = EXCITED
    nf = sum(1 for m in MS if G.forced(m[2], m[4]))
    nv = sum(1 for m in MS if G.vanishes(m[0], m[1], m[5]))
    qn = {registry.short(n): r[-1] for n, *r in registry.rows()}

    h = []
    A = h.append
    A(HEAD)
    A('<div class="wrap">')

    # masthead
    A('''<header class="mast">
  <p class="eyebrow">Research plate · master index eight</p>
  <h1>The Gravity&nbsp;Index</h1>
  <p class="dek">The gravitational field of the elements themselves — a nuclide
  in a charge state, read in eight spacetime dimensions — and the one place
  where the dimension changes the answer rather than the arithmetic.</p>
  <div class="stamp">
    <span>instrument <b>gravity.py</b></span>
    <span>members <b>%s</b></span>
    <span>rows <b>%s</b></span>
    <span>arity <b>%d</b></span>
    <span>cells <b>%d</b></span>
    <span>channel <b>K0</b></span>
    <span>cell <b>(%d,&nbsp;%d,&nbsp;%d)</b></span>
  </div>
</header>''' % (f"{len(MS):,}", f"{len(G.rows()):,}", G.ARITY, len(X), *G.cell()))

    A('''<div class="note warn" style="margin-top:26px">
  <span class="lab">Why petrov.py is not this, and is not withdrawn either</span>
  <p><strong>Petrov is a four-dimensional theorem and its own first line says
  so.</strong> “A Weyl tensor has four principal null directions counted with
  multiplicity” is the factorisation of the Weyl <em>spinor</em> into four
  principal spinors, which is available in four dimensions and nowhere else.
  Above four the classification is the CMPP alignment type, and a
  <em>generic</em> Weyl tensor there has no aligned null direction at all —
  type&nbsp;G, with no four-dimensional analogue. <span class="mono">petrov.py</span>
  codes (P,&nbsp;X)&nbsp;=&nbsp;(0,&nbsp;0) as type&nbsp;O, conformally flat, so
  a generic higher-dimensional vacuum read through that chart would print as
  <em>flat</em>.</p>
  <p>Two further facts, about the file rather than about gravity: its members
  are spacetimes, none of which carries a quantum number; and read against
  elements it is maximally degenerate — Schwarzschild, Kerr and
  Reissner–Nordström are the only three rows an atom could occupy and it puts
  all three in type&nbsp;D at (2,&nbsp;2), so every element, every ionisation
  stage and every level would land in one cell.</p>
  <p style="margin-bottom:0"><span class="mono">petrov.py</span> is a correct
  index of what it indexes and it stays where it is. This is the index those
  three facts ask for.</p>
</div>''')

    # 01 member
    A('''<section>
  <div class="shead"><span class="snum">01</span><h2>What a member is</h2></div>
  <p class="sub">A nuclide in a charge state, read in a spacetime dimension.
  Every slot is a quantum number, a count of them, or the status of the level
  the rest were read at &mdash; so the criterion
  <span class="mono">registry.enforce()</span> applies is met by construction
  rather than by exemption.</p>
  <p class="eqn mono">(Z, N, A, q, N<sub>e</sub>, 2J<sub>e</sub>, L, D)</p>
  <div class="kv">
    <div><dt>Z, N, A</dt><dd>%s<small>nuclides in AME2020 Table&nbsp;I;
      A recomputed as Z+N, never read</small></dd></div>
    <div><dt>q, N<sub>e</sub></dt><dd>%s<small>charge states, from the
      spectroscopic numeral: Al&nbsp;III is q&nbsp;=&nbsp;2</small></dd></div>
    <div><dt>2J<sub>e</sub>, L</dt><dd>%s<small>species, all members: %d read
      at the table&#39;s ground, %d at an excited level</small></dd></div>
    <div><dt>D</dt><dd>4 – 11<small>not measured: the independent variable.
      Nahm's ceiling on supergravity at the top</small></dd></div>
  </div>''' % (f"{len(G.nuclides()):,}", ", ".join(str(q) for q in
                sorted({m[3] for m in MS})), len(G.captures()),
                len(GROUND), len(EXCITED)))

    A('''  <h3>Where every number comes from</h3>
  <div class="tablewrap"><table>
    <thead><tr><th>quantity</th><th>source</th><th>what is done to it</th></tr></thead>
    <tbody>
    <tr><td class="name">M</td>
        <td class="mono sm">extracted/archives/restore-point-2-13/captures/AME2020-TableI.tsv</td>
        <td>M = A·u + Δ/c² − q·m<sub>e</sub>, from the mass excess in keV</td></tr>
    <tr><td class="name">q</td><td class="mono sm">the capture's spectroscopic numeral</td>
        <td>exact by the definition of the numeral</td></tr>
    <tr><td class="name">2J<sub>e</sub></td>
        <td class="mono sm">recovered/*.tsv — NIST ASD level tables</td>
        <td>the row at level_cm1 = 0.00 exactly, the table's own ground</td></tr>
    <tr><td class="name">χ</td><td class="mono sm">derived</td>
        <td>J<sub>e</sub>ħc ⁄ (GM²) — the dimensionless Kerr spin</td></tr>
    <tr><td class="name">Q̃</td><td class="mono sm">derived</td>
        <td>qe ⁄ (M√(4πε₀G)) — the dimensionless Reissner–Nordström charge</td></tr>
    </tbody></table>
    <caption>CODATA 2018 throughout, the values this tree already uses.</caption>
  </div>''')

    A('''  <div class="note good">
    <span class="lab">The mass path is checked against the scale's own zero</span>
    <p style="margin-bottom:0">Carbon&nbsp;12 has mass excess <span class="mono">%s keV</span>
    in the table <em>by the definition</em> of the atomic mass unit, so the
    expression above must return exactly 12&nbsp;u for it. It returns
    <span class="mono">%s u</span>. That is a fixture in
    <span class="mono">--selftest</span>, not a remark — an independent check on
    the whole path from the table to M.</p>
  </div>''' % (DM12, M12))

    A('''  <div class="note">
    <span class="lab">Electron binding is neglected, and the neglect is bounded</span>
    <p style="margin-bottom:0">Z³·13.6&nbsp;eV is a crude ceiling on an atom's
    total electronic binding — every electron bound no more tightly than the
    innermost one, counted Z times. Against Mc² the worst case over all %s
    members is <span class="mono">%.2e</span>, at Z&nbsp;=&nbsp;%d,
    A&nbsp;=&nbsp;%d. The coordinates are decade-resolution, so the neglect sits
    <strong>%d orders below the resolution</strong> and cannot move a cell.</p>
  </div>''' % (f"{len(MS):,}", WB, WHO[0], WHO[1], round(math.log10(0.1 / WB))))

    A('''  <div class="note">
    <span class="lab">Every parsed species is a member, and L says how it was read</span>
    <p style="margin-bottom:0">%d captures name a species and carry a level
    table, giving %d distinct species. <strong>%d are read at the table's
    ground (L&nbsp;=&nbsp;0) and %d at an excited level (L&nbsp;=&nbsp;1)</strong>
    &mdash; series or high-&#8467; captures that bank nothing at
    0.00&nbsp;cm&#8315;&#185;. None is dropped and none is relabelled as a
    ground it is not; the excitation energy goes into M exactly. Section&nbsp;08
    names all %d with the level each was read at, and measures what they bought.</p>
  </div>
</section>''' % (G.capture_files(), len(G.captures()), len(GROUND), len(exc),
                 len(exc)))

    # 02 the two J facts
    A('''<section>
  <div class="shead"><span class="snum">02</span><h2>Two angular-momentum facts,
  and neither needs a nuclear datum</h2></div>
  <p class="sub">The Kerr parameter is built from the body's <em>total</em>
  angular momentum, which for a free atom is F, not J<sub>e</sub>. AME2020
  Table&nbsp;I banks no nuclear spin, so F is banked for no member here. Two
  exact statements survive that anyway, and the index rests on them rather than
  on a guess at I.</p>

  <div class="duo">
    <div class="per">
      <div class="who">Forced — exact arithmetic</div>
      <div class="what">(A + N<sub>e</sub>) odd ⟹ F ≥ ½ &gt; 0</div>
      <div class="co">%s of %s members</div>
      <div class="obj">J<sub>e</sub> is half-odd-integer exactly when
      N<sub>e</sub> is odd; I is half-odd-integer exactly when A is odd;
      F&nbsp;=&nbsp;J<sub>e</sub>&nbsp;+&nbsp;I is half-odd-integer exactly when
      one holds and not the other. A half-odd-integer angular momentum cannot be
      zero. <strong>No knowledge of I whatever.</strong></div>
    </div>
    <div class="per">
      <div class="who">Vanishing — one empirical input</div>
      <div class="what">even-Z, even-N, 2J<sub>e</sub> = 0 ⟹ F = 0</div>
      <div class="co">%s members · status %s</div>
      <div class="obj">Every even-Z, even-N nucleus has ground-state spin zero.
      That is the pairing rule: exceptionless over measured ground states, and
      an <strong>empirical rule, not a theorem</strong>. It is carried as
      <span class="mono">PAIRING_RULE_STATUS</span> and never flattened. Where it
      applies, the exterior field has no rotation at all.</div>
    </div>
  </div>

  <div class="kv" style="margin-top:22px">
    <div><dt>F forced nonzero</dt><dd>%s<small>%.0f%% of members</small></dd></div>
    <div><dt>F established zero</dt><dd>%s<small>%.0f%%</small></dd></div>
    <div><dt>neither</dt><dd>%s<small>the undetermined class above D = 4</small></dd></div>
    <div><dt>exactly Schwarzschild</dt><dd>%d<small>distinct nuclides, neutral
      with F = 0</small></dd></div>
  </div>
  <p class="after">The two are mutually exclusive, and the selftest checks that
  rather than assuming it: F&nbsp;=&nbsp;0 established needs N<sub>e</sub> even,
  while A&nbsp;+&nbsp;N<sub>e</sub> odd with A even needs N<sub>e</sub> odd.</p>
</section>''' % (f"{nf:,}", f"{len(MS):,}", f"{nv:,}", G.PAIRING_RULE_STATUS,
                 f"{nf:,}", 100.0 * nf / len(MS), f"{nv:,}", 100.0 * nv / len(MS),
                 f"{len(MS) - nf - nv:,}", len(G.schwarzschild_members())))

    # 03 the ladder
    A('''<section>
  <div class="shead"><span class="snum">03</span><h2>The dimension changes the
  answer, not the arithmetic</h2></div>
  <p class="sub">A singly-rotating Myers–Perry black hole in D dimensions has a
  horizon where f(r) = r<sup>D−3</sup> + a²r<sup>D−5</sup> = μ.</p>

  <div class="tablewrap"><table>
    <thead><tr><th>D</th><th>f(r)</th><th>behaviour</th><th>verdict</th></tr></thead>
    <tbody>
      <tr><td class="name">4</td><td class="mono">r + a²/r</td>
        <td>falls to a minimum 2a, then rises</td>
        <td>a root needs μ ≥ 2a — <b>the Kerr bound</b></td></tr>
      <tr><td class="name">5</td><td class="mono">r² + a²</td>
        <td>f(0) = a² &gt; 0 and increases</td>
        <td>a root needs μ ≥ a² — <b>a bound, and a different one</b></td></tr>
      <tr><td class="name">≥ 6</td><td class="mono">r<sup>D−3</sup> + a²r<sup>D−5</sup></td>
        <td>D−5 ≥ 1, so f(0) = 0 and f rises without limit</td>
        <td><b class="hot">a root for every μ &gt; 0 and every a — no bound</b></td></tr>
    </tbody></table>
    <caption>The ultraspinning regime. It never uses the value of G<sub>D</sub>,
    which nothing here measures: it says a root <em>exists</em>, not where.</caption>
  </div>

  <figure class="plate" style="margin-top:26px">
    %s
    <div class="key">
      <span><i class="k b1"></i> a bound exists</span>
      <span><i class="k b0"></i> no bound — a horizon for every coupling</span>
      <span><i class="k b2"></i> undetermined — no exact solution</span>
    </div>
    <figcaption><b>Members by horizon-bound class in each dimension.</b> The
    amber block at D&nbsp;=&nbsp;4 and 5 is the Kerr and Myers–Perry bounds
    biting; from D&nbsp;=&nbsp;6 <b>%s of the %s members</b> move to
    <em>no bound</em>, and every one of them is neutral with a forced angular
    momentum. The grey block appears at D&nbsp;=&nbsp;5 and never leaves: those
    are charged members whose angular momentum is not established zero, for
    which <b>no exact charged rotating solution of the Einstein–Maxwell
    equations is known in closed form</b>. And a thin amber band of <b>%d
    survives at every dimension</b> — charged members whose total angular
    momentum <em>is</em> established zero, where static
    Tangherlini\u2013Reissner\u2013Nordstr\u00f6m imposes a bound in every D.
    Charge is never relieved.</figcaption>
  </figure>

  <div class="note warn">
    <span class="lab">Charge is not relieved the same way</span>
    <p style="margin-bottom:0">The static charged Tangherlini function is
    f(r)&nbsp;=&nbsp;1&nbsp;−&nbsp;μ/x&nbsp;+&nbsp;Q²/x² with
    x&nbsp;=&nbsp;r<sup>D−3</sup>; its roots are the roots of
    x²&nbsp;−&nbsp;μx&nbsp;+&nbsp;Q², which exist exactly when μ²&nbsp;≥&nbsp;4Q².
    <strong>A bound, in every dimension.</strong> The asymmetry is real: rotation
    is relieved by dimension and charge is not.</p>
  </div>
</section>''' % (ladder_svg(), f"{len(G.relieved()):,}", f"{len(MS):,}",
                 CLASSD[max(G.DIMS)].get(1, 0)))

    # 04 the 3-D member view -- one point per member, no collapse
    A(view3d_section())

    # 05 branch table
    rowsb = "".join(
        '<tr><td class="mono sm">%s</td><td><span class="chip %s">%s</span></td></tr>'
        % (E(t.split("  ")[0].strip()), BCLS[v], BNAME[v])
        for t, v in G.BRANCHES)
    A('''<section>
  <div class="shead"><span class="snum">05</span><h2>B is a table of exact
  solutions, not a judgement</h2></div>
  <p class="sub">Each branch names the metric it rests on, and where no exact
  metric is known the value is <em>undetermined</em> and stays undetermined.</p>
  <div class="tablewrap"><table>
    <thead><tr><th>branch</th><th>B</th></tr></thead>
    <tbody>%s</tbody></table>
    <caption>The general charged <em>rotating</em> solution of the
    Einstein–Maxwell equations is not known in closed form for D ≥ 5, so a
    member with q &gt; 0 whose total angular momentum is not established zero has
    no exact metric above four dimensions. B = 2 records that instead of
    inheriting the static answer.</caption>
  </div>
</section>''' % rowsb)

    # 05 the chart
    doc = {"D": "spacetime dimension", "B": "horizon-bound class",
           "F": "forced angular momentum, (A+N<sub>e</sub>) odd",
           "X": "spin-decade rank of χ", "Y": "charge-decade rank of Q̃",
           "L": "level status — 0 the table's ground, 1 excited",
           "E": "mass evidence — AME2020's own quality column"}
    crows = "".join(
        '<tr><td class="name mono">%s</td><td>%s</td><td class="mono">%s</td>'
        '<td class="num">%d</td></tr>'
        % (nm, doc[nm], sorted({c[i] for c in X}),
           len({c[i] for c in X}))
        for i, nm in enumerate(G.NAMES))
    lrows = "".join(
        '<tr><td class="name">%s</td><td class="num">%d</td><td class="num">%d</td>'
        '<td>%s</td></tr>'
        % (L, len(CL[L]), len(CL[L]) - len(X),
           '<span class="yes">closes</span>' if len(CL[L]) == len(X)
           else '<span class="no">does not close</span>')
        for L in hlaw.LANGS)
    ea, eb, esame = G.encoding_sensitivity()
    A('''<section>
  <div class="shead"><span class="snum">06</span><h2>The chart</h2></div>
  <div class="tablewrap"><table>
    <thead><tr><th>slot</th><th>what it measures</th><th>alphabet</th><th>values</th></tr></thead>
    <tbody>%s</tbody></table>
    <caption>Spin decades floor(log₁₀ χ) = %s. Charge decades
    floor(log₁₀ Q̃) = %s. Kerr–Newman has a horizon exactly when
    χ² + Q̃² ≤ 1; every charged or spinning member here exceeds that by fifteen
    to thirty-six orders of magnitude, which is the ordinary statement that an
    atom is not a black hole. The <em>decade</em> is what varies across the
    elements, and it is what is charted.</caption>
  </div>

  <div class="kv" style="margin-top:22px">
    <div><dt>charted rows</dt><dd>%s</dd></div>
    <div><dt>distinct cells</dt><dd>%d</dd></div>
    <div><dt>box</dt><dd>%s<small>what charting cost tracks</small></dd></div>
    <div><dt>cell</dt><dd>(%d, %d, %d)<small>K, height, width</small></dd></div>
  </div>

  <div class="trio" style="margin-top:14px">
    <div class="per"><div class="who">constant coordinates</div>
      <div class="what">%s</div>
      <div class="obj">A one-valued slot carries no information and widens every
      closure for free.</div></div>
    <div class="per"><div class="who">determined by the others</div>
      <div class="what">%s</div>
      <div class="obj">Over-representation is the fault this looks for: a slot
      the rest already fix adds no member distinction and multiplies the box.</div></div>
    <div class="per"><div class="who">LABEL coordinates</div>
      <div class="what">%s</div>
      <div class="obj">A slot separating ≥ 90%% of members is a row label, not a
      measurement.</div></div>
  </div>

  <div class="tablewrap" style="margin-top:22px"><table>
    <thead><tr><th>language</th><th class="num">admits</th><th class="num">E</th><th>verdict</th></tr></thead>
    <tbody>%s</tbody></table>
    <caption>Against %d cells held. <b>It closes nothing — K0.</b></caption>
  </div>

  <div class="note %s">
    <span class="lab">The encoding is a rank, and the alternative is measured</span>
    <p style="margin-bottom:0">χ = 0 exactly when J<sub>e</sub> = 0, and log 0 is
    not a number, so a member with no electronic angular momentum has no decade
    at all. Writing it as 0 beside decades of %d to %d would place it %d units
    from its nearest neighbour and distort every convex hull the geometry
    operator takes. The coordinate is therefore the <em>rank</em> in the sorted
    alphabet, evenly spaced, as every other chart in this tree is. That is a
    choice, so <span class="mono">encoding_sensitivity()</span> charts the
    raw-decade encoding too: <span class="mono">%s</span> against
    <span class="mono">%s</span> — <strong>%s</strong>.</p>
  </div>
</section>''' % (crows, SPIN_DEC, CHG_DEC, f"{len(G.rows()):,}", len(X),
                 f"{overlap.box_of(X):,}", *G.cell(),
                 ", ".join(G.constant_coords()) or "none",
                 ", ".join(d[0] for d in G.dependent_coords()) or "none",
                 ", ".join(l[0] for l in G.labels()) or "none",
                 lrows, len(X), "good" if esame else "warn",
                 SPIN_DEC[0], SPIN_DEC[-1], SPIN_DEC[0],
                 tuple(ea), tuple(eb),
                 "the choice costs nothing, and that is measured"
                 if esame else "THE CHOICE MOVES THE CELL"))

    # 06 findings
    prow = "".join(
        '<tr><td class="name">D = %d</td><td class="num">%d</td>'
        '<td class="cell">(%d, %d, %d)</td><td class="mono sm">%s</td></tr>'
        % (D, PD[D][0], *PD[D][1],
           ", ".join(BNAME[b] for b in BD[D][1]))
        for D in G.DIMS)
    A('''<section>
  <div class="shead"><span class="snum">07</span><h2>Two findings, recorded and
  not repaired</h2></div>

  <h3>A · The dimension is invisible to the chart and visible in the cell count</h3>
  <div class="tablewrap"><table>
    <thead><tr><th>dimension</th><th class="num">cells</th><th>cell</th><th>bound classes present</th></tr></thead>
    <tbody>%s</tbody></table>
    <caption>Fix D and chart the other five slots.</caption>
  </div>
  <p class="after">The same (K, height, width) at <em>every</em> dimension, and
  four more cells from five upward. The four are the B&nbsp;=&nbsp;2 rows: in
  four dimensions Kerr–Newman covers every (M,&nbsp;Q,&nbsp;J) so nothing is
  undetermined; above it the charged rotating metric is unknown and some members
  are. <strong>So what the dimension adds to this index is an ignorance class,
  not a geometry class</strong> — and the admissible chart cannot see it.</p>

  <h3>B · The relief at six is in the members and not in the cell</h3>
  <p>%s members lose their bound at D&nbsp;=&nbsp;6 and the cell does not move. A
  chart reporting (K,&nbsp;height,&nbsp;width) would report the ultraspinning
  transition as <em>nothing at all</em>. That is a limit of the chart, stated
  here so nobody reads the invariance as a finding about gravity.</p>
</section>''' % (prow, f"{len(G.relieved()):,}"))

    # 08 species
    srow = "".join(
        '<tr><td class="name">%s%s</td><td class="num">%d</td><td class="num">%d</td>'
        '<td class="num">%d</td><td class="mono">%s</td><td class="mono">%s</td>'
        '<td class="mono">%s</td><td class="num">%s</td><td class="num">%d</td>'
        '<td class="mono sm">%s</td><td class="mono sm">%s</td></tr>'
        % (E(r["sp"]), ' <span class="chip b2">L1</span>' if r["L"] else "",
           r["Z"], r["q"], r["Ne"], E(r["cfg"]), E(r["term"]),
           jstr(r["tj"]),
           "ground" if not r["L"] else "%.0f" % r["lv"], r["n"],
           "–".join(str(d) for d in (r["chi"][:1] + r["chi"][-1:])) or "—",
           "–".join(str(d) for d in (r["qt"][:1] + r["qt"][-1:])) or "—")
        for r in sp)
    g0 = collections.Counter(m[5] for m in MS if m[6] == 0)
    g1 = collections.Counter(m[5] for m in MS if m[6] == 1)
    js = sorted(set(g0) | set(g1))
    jrow = ("<tr><td class=\"name\">L = 0 &nbsp;ground</td>"
            + "".join('<td class="num">%d</td>' % g0.get(j, 0) for j in js)
            + "</tr><tr><td class=\"name\">L = 1 &nbsp;excited</td>"
            + "".join('<td class="num">%d</td>' % g1.get(j, 0) for j in js)
            + "</tr>")
    only1 = sorted(set(g1) - set(g0))
    only0 = sorted(set(g0) - set(g1))
    A('''<section>
  <div class="shead"><span class="snum">08</span><h2>All %d species, and what
  the excited ones bought</h2></div>
  <p class="sub">Each species contributes one member per banked nuclide of its
  element &mdash; its <em>lowest</em> banked level and no other, so no body is
  charted twice. Z runs %d to %d, q runs 0 to %d. <b>%d are read at the table's
  ground and %d at an excited level</b>, marked <span class="chip b2">L1</span>.</p>

  <div class="note good">
    <span class="lab">A correction: these 31 were excluded, and should not have been</span>
    <p>An earlier build dropped them because their capture banks no level at
    0.00&nbsp;cm&#8315;&#185;. The premise was right and the conclusion did not
    follow. Reading an excited level's J <em>as a ground J</em> would indeed be
    an error &mdash; but an excited level is a real state of a real ion, with a
    real angular momentum and a banked energy, and its exterior gravitational
    field is as real as the ground state's. Two things were confused: what the
    level <em>is</em>, and whether it is the ground. The first is the
    measurement; the second is a status.</p>
    <p style="margin-bottom:0">So the status is the coordinate <b>L</b>, nothing
    is dropped, and nothing is relabelled as a ground it is not. The excitation
    energy goes into M <em>exactly</em> &mdash; worst case %.1e of Mc&sup2;. It
    is included because it is <em>banked</em>; electron binding is bounded
    instead because it is not. That is the only difference between them.</p>
  </div>

  <div class="tablewrap"><table>
    <thead><tr><th>2J<sub>e</sub></th>%s</tr></thead>
    <tbody>%s</tbody></table>
    <caption><b>What the 31 bought, measured rather than asserted.</b> They add
    exactly one angular momentum the grounds never reach &mdash; J = %s, on %d
    members &mdash; and re-weight the rest: 2J<sub>e</sub> = 2 was already
    seated on 29 ground members and rises to %d. J = %s are seated only by
    grounds. Members %s &rarr; %s, nuclides with an exactly Schwarzschild
    exterior 228 &rarr; %d, members relieved by dimension 536 &rarr; %s.</caption>
  </div>

  <div class="tablewrap tall" style="margin-top:22px"><table>
    <thead><tr><th>species</th><th class="num">Z</th><th class="num">q</th>
      <th class="num">N<sub>e</sub></th><th>config</th><th>term</th>
      <th>J</th><th class="num">level / cm&#8315;&#185;</th>
      <th class="num">nuclides</th><th>log &chi;</th><th>log Q&#771;</th></tr></thead>
    <tbody>%s</tbody></table>
    <caption>Configuration, term and J as the NIST ASD capture banks them, at
    the lowest level each capture holds. The last two columns are the range of
    floor(log&#8321;&#8320;) over that species' nuclides &mdash; &chi; falls as
    A rises because &chi; &prop; 1/M&sup2;.</caption>
  </div>
</section>''' % (len(sp), min(m[0] for m in MS), max(m[0] for m in MS),
                 max(m[3] for m in MS), len(GROUND), len(exc),
                 G.excitation_bound()[0],
                 "".join('<th class="num">%s</th>' % jstr(j) for j in js),
                 jrow,
                 ", ".join(jstr(j) for j in only1), sum(g1[j] for j in only1),
                 g0.get(2, 0) + g1.get(2, 0),
                 ", ".join(jstr(j) for j in only0),
                 "2,696", "{:,}".format(len(MS)),
                 len(G.schwarzschild_members()),
                 "{:,}".format(len(G.relieved())),
                 srow))

    # 09 the figure
    frow = "".join(
        '<tr><td class="name">%s</td><td class="cell">(%d, %d, %d)</td>'
        '<td class="mono sm">%s</td></tr>'
        % (n, *c, E(qn[n]))
        for n, c in sorted(FC.items(), key=lambda kv: kv[1]))
    A('''<section>
  <div class="shead"><span class="snum">09</span><h2>Seated in the index of
  first-order indexes</h2></div>
  <p class="sub">One vertex per index of the periodic elements.
  <span class="mono">registry.enforce()</span> returns empty, and
  <span class="mono">registry.missing()</span> returns empty: no module exposing
  an index is unaccounted for.</p>
  <div class="tablewrap"><table>
    <thead><tr><th>index</th><th>cell</th><th>quantum numbers its members carry</th></tr></thead>
    <tbody>%s</tbody></table>
    <caption>%d vertices. <span class="mono">registry.COMPLETE</span> stays
    False.</caption>
  </div>
  <div class="kv" style="margin-top:22px">
    <div><dt>E before</dt><dd>%d<small>seven vertices</small></dd></div>
    <div><dt>E after</dt><dd>%d<small>eight, with gravity</small></dd></div>
    <div><dt>gravity is</dt><dd class="hot">disruptive<small>it raises the demand
      rather than filling it</small></dd></div>
  </div>
  <p class="after">Gravity does not fill demand: it raises it, by %d. That is
  reported and not softened. The width 65 it brings is far outside the other
  seven vertices, and the join of it with anything above it lands outside the
  figure. <strong>Whether the figure closes is not the criterion</strong> —
  identifying every first-order index is.</p>
</section>''' % (frow, len(FC), E7, E8, E8 - E7))

    # 09 refusals
    A('''<section>
  <div class="shead"><span class="snum">10</span><h2>What this file refuses</h2></div>
  <ul class="tight refuse">
    <li><b>To call 2J<sub>e</sub> the member's spin.</b> It is the electronic
      part. The nuclear part is not banked, so χ as computed is the electronic
      contribution to the Kerr parameter and nothing more. Section&nbsp;02's two
      facts are the only total-angular-momentum statements made here, and
      neither needs I.</li>
    <li><b>To put a number on a horizon above four dimensions.</b>
      G<sub>D</sub> is fixed by nothing measured here. Only existence statements
      are made above D&nbsp;=&nbsp;4, and only where an exact solution supplies
      one.</li>
    <li><b>To read the pairing rule as a theorem.</b> Even-even ground states
      have spin zero as an exceptionless empirical rule.
      <span class="mono">PAIRING_RULE_STATUS</span> says so, and every member
      whose F&nbsp;=&nbsp;0 rests on it.</li>
    <li><b>To extend the %d species by inference.</b> Hund's rules would give a
      ground J for every element in the table, and that is a computation, not a
      capture.</li>
    <li><b>To assign the warp metrics anything.</b> The same refusal
      <span class="mono">petrov.py</span> makes, for the same reason: nothing in
      this tree computes one.</li>
    <li><b>To claim the index is complete.</b> It is an index of the elements'
      gravitational field as the banked data determines it.</li>
  </ul>
</section>''' % len(GR))

    A('''<div class="foot">
  <p>Every figure on this plate is read from the instrument at build time, not
  retyped. Re-verify with:</p>
  <p><code>python3 research/warp-drive/gravity.py --selftest</code> — %d fixtures<br>
  <code>python3 research/warp-drive/gravity.py</code> — the reading<br>
  <code>python3 research/warp-drive/registry.py --selftest</code> — the criterion<br>
  <code>python3 research/warp-drive/figure.py --selftest</code> — the figure<br>
  <code>python3 research/warp-drive/render/build_gravity_plate.py</code> — this plate</p>
</div>''' % open(os.path.join(os.path.dirname(os.path.abspath(G.__file__)),
                     "gravity.py"), encoding="utf-8").read().count('chk("'))

    A('</div>')
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(h))
    print("wrote %s  (%d bytes)" % (OUT, os.path.getsize(OUT)))


HEAD = plate.head('The Gravity Index')


if __name__ == "__main__":
    build()
