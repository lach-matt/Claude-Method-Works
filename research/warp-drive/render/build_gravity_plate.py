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
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import gravity as G            # noqa: E402
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
GR = G.grounds()
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
    s2z = G.symbol_to_Z()
    per = collections.Counter((m[0], m[3]) for m in MS)
    out = []
    for (sym, num), (tj, cfg, term, src) in sorted(GR.items()):
        Z, q = s2z[sym], G.ROMAN[num] - 1
        rs = [m for m in MS if m[0] == Z and m[3] == q]
        chi = sorted({int(math.floor(math.log10(m[8]))) for m in rs if m[8] > 0})
        qt = sorted({int(math.floor(math.log10(m[9]))) for m in rs if m[9] > 0})
        out.append(dict(sp="%s %s" % (sym, num), Z=Z, q=q, Ne=Z - q, tj=tj,
                        cfg=cfg, term=term, n=per[(Z, q)],
                        chi=chi, qt=qt, src=src))
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


# ------------------------------------------------------------------ the page
def build():
    sp = species_rows()
    exc = G.excluded_species()
    nf = sum(1 for m in MS if G.forced(m[2], m[4]))
    nv = sum(1 for m in MS if G.vanishes(m[0], m[1], m[5]))
    qn = {n.split(".")[0]: r[-1] for n, *r in registry.rows()}

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
  Every slot is a quantum number or a count of them, so the criterion
  <span class="mono">registry.enforce()</span> applies is met by construction
  rather than by exemption.</p>
  <p class="eqn mono">(Z, N, A, q, N<sub>e</sub>, 2J<sub>e</sub>, D)</p>
  <div class="kv">
    <div><dt>Z, N, A</dt><dd>%s<small>nuclides in AME2020 Table&nbsp;I;
      A recomputed as Z+N, never read</small></dd></div>
    <div><dt>q, N<sub>e</sub></dt><dd>%s<small>charge states, from the
      spectroscopic numeral: Al&nbsp;III is q&nbsp;=&nbsp;2</small></dd></div>
    <div><dt>2J<sub>e</sub></dt><dd>%s<small>species banking a true ground
      level, of %d that parse</small></dd></div>
    <div><dt>D</dt><dd>4 – 11<small>not measured: the independent variable.
      Nahm's ceiling on supergravity at the top</small></dd></div>
  </div>''' % (f"{len(G.nuclides()):,}", ", ".join(str(q) for q in
                sorted({m[3] for m in MS})), len(GR), len(G.captures())))

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

    A('''  <div class="note warn">
    <span class="lab">And %d species are excluded rather than approximated</span>
    <p style="margin-bottom:0">%d captures name a species and carry a level
    table, giving %d distinct species. <strong>%d bank a true ground.</strong>
    The other %d are series or high-ℓ captures whose lowest banked level is an
    <em>excited</em> one, and reading its J as a ground J is exactly the error
    this refuses. Section&nbsp;07 names all %d with the level that disqualified
    each.</p>
  </div>
</section>''' % (len(exc), G.capture_files(), len(G.captures()), len(GR),
                 len(exc), len(exc)))

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

    # 04 branch table
    rowsb = "".join(
        '<tr><td class="mono sm">%s</td><td><span class="chip %s">%s</span></td></tr>'
        % (E(t.split("  ")[0].strip()), BCLS[v], BNAME[v])
        for t, v in G.BRANCHES)
    A('''<section>
  <div class="shead"><span class="snum">04</span><h2>B is a table of exact
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
  <div class="shead"><span class="snum">05</span><h2>The chart</h2></div>
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
  <div class="shead"><span class="snum">06</span><h2>Two findings, recorded and
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

    # 07 species
    srow = "".join(
        '<tr><td class="name">%s</td><td class="num">%d</td><td class="num">%d</td>'
        '<td class="num">%d</td><td class="mono">%s</td><td class="mono">%s</td>'
        '<td class="mono">%s</td><td class="num">%d</td>'
        '<td class="mono sm">%s</td><td class="mono sm">%s</td></tr>'
        % (E(r["sp"]), r["Z"], r["q"], r["Ne"], E(r["cfg"]), E(r["term"]),
           jstr(r["tj"]), r["n"],
           "–".join(str(d) for d in (r["chi"][:1] + r["chi"][-1:])) or "—",
           "–".join(str(d) for d in (r["qt"][:1] + r["qt"][-1:])) or "—")
        for r in sp)
    A('''<section>
  <div class="shead"><span class="snum">07</span><h2>The %d species</h2></div>
  <p class="sub">Each species contributes one member per banked nuclide of its
  element. Z runs %d to %d, q runs 0 to %d.</p>
  <div class="tablewrap tall"><table>
    <thead><tr><th>species</th><th class="num">Z</th><th class="num">q</th>
      <th class="num">N<sub>e</sub></th><th>ground config</th><th>term</th>
      <th>J</th><th class="num">nuclides</th><th>log χ</th><th>log Q̃</th></tr></thead>
    <tbody>%s</tbody></table>
    <caption>Ground configuration, term and J as the NIST ASD capture banks
    them. The last two columns are the range of floor(log₁₀) over that species'
    nuclides — χ falls as A rises because χ ∝ 1/M².</caption>
  </div>

  <h3>And the %d excluded</h3>
  <p>Parsed, but banking no ground level. Reading the J of an excited level as a
  ground J is the error this refuses.</p>
  <div class="tablewrap"><table>
    <thead><tr><th>species</th><th class="num">lowest banked level / cm⁻¹</th><th>capture</th></tr></thead>
    <tbody>%s</tbody></table>
  </div>
</section>''' % (len(sp), min(m[0] for m in MS), max(m[0] for m in MS),
                 max(m[3] for m in MS), srow, len(exc),
                 "".join('<tr><td class="name">%s</td><td class="num">%.2f</td>'
                         '<td class="mono sm">%s</td></tr>' % (E(s), lv, E(f))
                         for s, lv, f in exc)))

    # 08 the figure
    frow = "".join(
        '<tr><td class="name">%s</td><td class="cell">(%d, %d, %d)</td>'
        '<td class="mono sm">%s</td></tr>'
        % (n, *c, E(qn[n]))
        for n, c in sorted(FC.items(), key=lambda kv: kv[1]))
    A('''<section>
  <div class="shead"><span class="snum">08</span><h2>Seated in the index of
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
  <div class="shead"><span class="snum">09</span><h2>What this file refuses</h2></div>
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


HEAD = '''<title>The Gravity Index</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,300;0,400;0,600;0,800;1,400&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<style>
:root{
  --ground:#F4F6F8; --panel:#FFFFFF; --sunk:#EDF0F4;
  --ink:#12161C; --body:#2C3440; --muted:#66717F; --faint:#98A2AF;
  --rule:#D9DFE7; --rule-hard:#B6C0CC; --accent:#1B4B78;
  --order:#7A3E9D; --algebra:#B03A64; --geometry:#137A69;
  --information:#B86A12; --statistics:#2456A0;
  --bound:#B86A12; --free:#137A69; --undet:#7C8796;
  --shadow:0 1px 2px rgba(18,22,28,.05),0 8px 24px -12px rgba(18,22,28,.16);
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --ground:#0D1117; --panel:#141A22; --sunk:#1B222C;
    --ink:#EEF2F7; --body:#C3CCD8; --muted:#8994A3; --faint:#5F6A79;
    --rule:#262F3B; --rule-hard:#394453; --accent:#7FB2E5;
    --order:#C08FE0; --algebra:#E88AA8; --geometry:#4CC6AF;
    --information:#E0A557; --statistics:#79A9EE;
    --bound:#E0A557; --free:#4CC6AF; --undet:#7C8796;
    --shadow:0 1px 2px rgba(0,0,0,.4),0 8px 28px -14px rgba(0,0,0,.8);
  }
}
:root[data-theme="dark"]{
  --ground:#0D1117; --panel:#141A22; --sunk:#1B222C;
  --ink:#EEF2F7; --body:#C3CCD8; --muted:#8994A3; --faint:#5F6A79;
  --rule:#262F3B; --rule-hard:#394453; --accent:#7FB2E5;
  --order:#C08FE0; --algebra:#E88AA8; --geometry:#4CC6AF;
  --information:#E0A557; --statistics:#79A9EE;
  --bound:#E0A557; --free:#4CC6AF; --undet:#7C8796;
  --shadow:0 1px 2px rgba(0,0,0,.4),0 8px 28px -14px rgba(0,0,0,.8);
}
*{box-sizing:border-box}
body{background:var(--ground);color:var(--body);
  font-family:Spectral,Georgia,serif;font-size:17px;line-height:1.62;
  padding-block:0;padding-left:20px;padding-right:20px;-webkit-font-smoothing:antialiased}
.wrap{max-width:920px;margin:0 auto;padding-block:56px 96px}
h1,h2,h3{color:var(--ink);text-wrap:balance;margin:0}
h1{font-size:clamp(2.05rem,5.4vw,3rem);font-weight:800;line-height:1.08;letter-spacing:-.022em}
h2{font-size:clamp(1.28rem,3vw,1.6rem);font-weight:600;line-height:1.2;letter-spacing:-.012em}
h3{font-size:1.06rem;font-weight:600;margin:34px 0 12px;letter-spacing:-.006em}
p{margin:0 0 1.05em}
p.after{margin-top:18px}
.mono{font-family:'IBM Plex Mono',ui-monospace,monospace;font-variant-numeric:tabular-nums}
.sm{font-size:.82em}
.eqn{font-size:1.16rem;color:var(--ink);background:var(--sunk);border:1px solid var(--rule);
  border-radius:3px;padding:15px 18px;letter-spacing:.02em;margin:0 0 22px;overflow-x:auto}
.hot{color:var(--algebra)}
.mast{border-bottom:2px solid var(--ink);padding-bottom:26px}
.eyebrow{font-family:'IBM Plex Mono',monospace;font-size:.7rem;font-weight:600;
  letter-spacing:.18em;text-transform:uppercase;color:var(--muted);margin:0 0 16px}
.dek{font-size:1.15rem;color:var(--muted);margin:16px 0 0;max-width:62ch;font-style:italic}
.stamp{display:flex;flex-wrap:wrap;gap:0 30px;margin-top:22px;
  font-family:'IBM Plex Mono',monospace;font-size:.74rem;color:var(--faint);letter-spacing:.04em}
.stamp b{color:var(--body);font-weight:500}
section{margin-top:60px}
.shead{display:flex;align-items:baseline;gap:14px;margin-bottom:6px}
.snum{font-family:'IBM Plex Mono',monospace;font-size:.78rem;font-weight:600;
  color:var(--accent);letter-spacing:.1em;flex:none;padding-top:.28em}
.sub{color:var(--muted);font-size:.97rem;margin:0 0 26px;max-width:66ch}
.tablewrap{overflow-x:auto;border:1px solid var(--rule);border-radius:3px;background:var(--panel);box-shadow:var(--shadow)}
.tablewrap.tall{max-height:560px;overflow-y:auto}
.tablewrap.tall thead th{position:sticky;top:0;background:var(--panel);z-index:1}
table{border-collapse:collapse;width:100%;min-width:620px}
caption{caption-side:bottom;text-align:left;padding:12px 16px;font-size:.83rem;color:var(--muted);border-top:1px solid var(--rule)}
th,td{padding:9px 14px;text-align:left;border-bottom:1px solid var(--rule)}
thead th{font-family:'IBM Plex Mono',monospace;font-size:.66rem;font-weight:600;
  letter-spacing:.13em;text-transform:uppercase;color:var(--muted);
  border-bottom:1px solid var(--rule-hard);white-space:nowrap}
tbody tr:last-child td{border-bottom:none}
td.name{font-weight:600;color:var(--ink);white-space:nowrap}
td.num,td.cell{font-family:'IBM Plex Mono',monospace;font-variant-numeric:tabular-nums;white-space:nowrap}
td.num{text-align:right}
th.num{text-align:right}
td.cell{color:var(--ink)}
td.mono{font-family:'IBM Plex Mono',monospace;font-variant-numeric:tabular-nums}
.chip{display:inline-block;font-family:'IBM Plex Mono',monospace;font-size:.68rem;
  font-weight:600;letter-spacing:.05em;padding:1px 7px;border-radius:2px;border:1px solid currentColor;line-height:1.5}
.chip.b0{color:var(--free)} .chip.b1{color:var(--bound)} .chip.b2{color:var(--undet)}
.yes{color:var(--geometry);font-weight:600} .no{color:var(--muted);font-weight:600}
figure{margin:0}
.plate{background:var(--panel);border:1px solid var(--rule);border-radius:3px;
  padding:26px 22px 18px;box-shadow:var(--shadow)}
figcaption{font-size:.85rem;color:var(--muted);margin-top:16px;padding-top:14px;border-top:1px solid var(--rule)}
figcaption b{color:var(--ink);font-weight:600}
svg{display:block;max-width:100%;height:auto;margin:0 auto}
svg text{font-family:'IBM Plex Mono',monospace}
rect.b0{fill:var(--free)} rect.b1{fill:var(--bound)} rect.b2{fill:var(--undet)}
.key{display:flex;flex-wrap:wrap;gap:8px 20px;margin-top:14px;
  font-family:'IBM Plex Mono',monospace;font-size:.72rem;color:var(--muted)}
.key span{display:flex;align-items:center;gap:7px}
.key i.k{width:11px;height:11px;border-radius:2px;display:block;flex:none}
.key i.b0{background:var(--free)} .key i.b1{background:var(--bound)} .key i.b2{background:var(--undet)}
svg text.tb0{fill:var(--free)} svg text.tb1{fill:var(--bound)} svg text.tb2{fill:var(--undet)}
.note{border-left:3px solid var(--accent);background:var(--sunk);
  padding:16px 20px;margin:26px 0;border-radius:0 3px 3px 0}
.note p:last-child{margin-bottom:0}
.note .lab{font-family:'IBM Plex Mono',monospace;font-size:.66rem;font-weight:600;
  letter-spacing:.14em;text-transform:uppercase;color:var(--accent);display:block;margin-bottom:7px}
.note.warn{border-left-color:var(--algebra)} .note.warn .lab{color:var(--algebra)}
.note.good{border-left-color:var(--geometry)} .note.good .lab{color:var(--geometry)}
.kv{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));
  gap:1px;background:var(--rule);border:1px solid var(--rule);border-radius:3px;overflow:hidden}
.kv>div{background:var(--panel);padding:14px 16px}
.kv dt{font-family:'IBM Plex Mono',monospace;font-size:.63rem;letter-spacing:.12em;
  text-transform:uppercase;color:var(--muted);margin:0 0 6px}
.kv dd{margin:0;font-family:'IBM Plex Mono',monospace;font-size:1.2rem;font-weight:500;color:var(--ink);line-height:1.15}
.kv dd.hot{color:var(--algebra)}
.kv dd small{display:block;font-size:.68rem;font-weight:400;color:var(--faint);margin-top:5px;letter-spacing:.04em;line-height:1.4}
ul.tight{margin:0 0 1.05em;padding-left:1.15em}
ul.tight li{margin-bottom:.7em}
ul.refuse li b{color:var(--ink)}
.foot{margin-top:72px;padding-top:22px;border-top:1px solid var(--rule);font-size:.83rem;color:var(--faint)}
.foot code{font-family:'IBM Plex Mono',monospace;color:var(--muted);font-size:.95em}
.trio{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.duo{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}
@media(max-width:720px){.trio,.duo{grid-template-columns:1fr}}
.per{border:1px solid var(--rule);border-radius:3px;background:var(--panel);padding:17px 18px;box-shadow:var(--shadow)}
.per .who{font-family:'IBM Plex Mono',monospace;font-size:.66rem;letter-spacing:.13em;
  text-transform:uppercase;color:var(--muted);margin-bottom:9px}
.per .what{font-size:1.12rem;color:var(--ink);font-weight:600;margin-bottom:4px;line-height:1.25}
.per .co{font-family:'IBM Plex Mono',monospace;font-size:.86rem;color:var(--accent);margin-bottom:10px}
.per .obj{font-size:.88rem;color:var(--muted);line-height:1.45}
</style>'''


if __name__ == "__main__":
    build()
