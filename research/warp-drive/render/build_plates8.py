#!/usr/bin/env python3
r"""
build_plates8.py -- the channel, entropy and octad plates.

Write the spectra, entropy and octad plates.

    python3 build_plates8.py             writes spx.html, ent.html, oct.html
    python3 build_plates8.py --selftest  fixtures

===============================================================================
0. IT COULD NOT RUN AT ALL, AND THE THREE INPUTS ARE RESTORED BY EXTRACTION
===============================================================================

**THIS FILE RAISED `FileNotFoundError` AT IMPORT.**  `style.css`, `w3d.js` and
`oct_pts.json` were never committed and nothing in the tree said so.  They are
RECOVERABLE, because `page()` INLINES all three into the plate it writes.
`build_plates.py` section 0 records the full search -- git history has never
held any of them, and the one `style.css` on disk (`recovered/style.css`, 700
bytes, an unrelated print stylesheet) is not this one.  Read that section for
the extraction rule; it is the same shape, and `style.css` is byte-identical
across all seven plates here.

THIS FILE'S OWN RECOVERY has one part the sibling does not: the octad's
`edges` array.  It is the second JSON literal in `oct.html`'s single
`scatter3d(...)` call, and `oct_pts.json` therefore holds `octad` as
`{"pts": [...], "edges": [...]}` while `spectra` and `entropy` are plain
lists -- which is what `D[key]['pts'] if extra else D[key]` already expected.

===============================================================================
1. `w3d.js` IS RE-PINNED TO `w3d-r2.js`, THE LATER OF THE TWO GENERATIONS
===============================================================================

**ONE NAME HELD TWO CONTENTS, AND THESE PLATES PIN THE SECOND.**  Measured off
the plates:

    generation   bytes   md5                                inlined by
    r1           5,753   f9348be9b963d26e2c63240fc974e060   ion, axs, rid
    r2           6,542   4154dde8161ec3e0dc154fadab88e7dd   spx, ent, oct, hexad
    scatter3d.js 7,975   07ceeb670663d6228b839648f4c915f4   every later plate

r2 is r1 plus the `opts.edges` pass and the hollow-point branch -- which is
why the octad, alone among the six, can draw its 28 threads.  A plate built
against r1 would silently lose them, and one built against `scatter3d.js`
would differ in the axis paint.  `scatter3d.js` is the living runtime and is
NOT a substitute here.

RE-PINNED, NOT LOOSENED: this file reads `w3d-r2.js`, the sibling reads
`w3d-r1.js`, and the ambiguous name is retired.  All three pages written here
are BYTE-IDENTICAL to the plates in the tree (`spx.html` == `spectra-plate.html`
and so on); the selftest rebuilds them in memory and compares md5s.

INPUTS RESOLVE AGAINST THIS FILE'S OWN DIRECTORY, not the working directory.
Outputs are unchanged and still land in the working directory.
"""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

STYLE = open(os.path.join(HERE, 'style.css')).read()
# RE-PINNED from 'w3d.js' -- see section 1.  That name held two generations of
# the widget and these three plates inline the second, the one with edges.
W3D = open(os.path.join(HERE, 'w3d-r2.js')).read()
D = json.load(open(os.path.join(HERE, 'oct_pts.json')))
COL = ("colour:p=>['--statistics','--geometry','--information',"
       "'--algebra','--order'][p.l]")


def page(title, body, script):
    return ("<title>%s</title>\n"
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
            'family=Spectral:ital,wght@0,300;0,400;0,600;0,800;1,400&'
            'family=IBM+Plex+Mono:wght@400;500;600&display=swap">\n'
            "%s\n<div class=\"wrap\">\n%s\n</div>\n"
            "<script>\n%s\n%s\n</script>\n" % (title, STYLE, body, W3D, script))


SPECTRA = """
<header class="mast">
  <p class="eyebrow">Research plate · master index seven</p>
  <h1>The Channel&nbsp;Index</h1>
  <p class="dek">The corpus's largest banked measurement set, which nothing had
  indexed — and a data fault sitting in its most authoritative rows.</p>
  <div class="stamp">
    <span>instrument <b>spectra.py</b></span>
    <span>source rows <b>104,832</b></span>
    <span>members <b>209 shapes</b></span>
    <span>channel <b>K0</b></span>
  </div>
</header>

<section style="margin-top:34px">
  <div class="shead"><span class="snum">01</span><h2>104,832 rows, 209 shapes</h2></div>
  <p class="sub">A row of COORDINATES-2.13 is a spectroscopic channel: an element, a
  charge stage, an angular momentum, a Pauli bound, a multiplicity, a quantum defect
  and two provenance columns. What the corpus's own channel equation turns on is the
  channel's <em>shape</em>.</p>
  <div class="kv">
    <div><dt>rows banked</dt><dd>104,832</dd></div>
    <div><dt>usable</dt><dd>104,807<small>25 dropped, §03</small></dd></div>
    <div><dt>channel shapes</dt><dd>209<small>3–3,124 rows apiece</small></dd></div>
    <div><dt>channel</dt><dd style="color:var(--faint)">K0<small>cell (0, 16, 24)</small></dd></div>
  </div>
  <div class="note">
    <span class="lab">First-order, which is why it earns a place</span>
    <p style="margin-bottom:0">Its members are <em>channels</em> — not elements, not
    transitions, and not functions of the seated inventory. So it is not a re-charting
    of anything the element-address census covered, and it qualifies by the same
    argument the ionisation ladder did: a new member set, not a new arrangement.
    Reporting 104,832 as a cell count would be counting observations and calling them
    channels.</p>
  </div>
</section>

<section>
  <div class="shead"><span class="snum">02</span><h2>The channel shapes in three dimensions</h2></div>
  <p class="sub">Pauli bound left to right, multiplicity bottom to top, angular momentum
  into the depth. Drag to rotate.</p>
  <figure class="plate">
    <div class="v3d"><canvas id="sp3d" aria-label="209 channel shapes in (B, multiplicity, angular momentum) space"></canvas></div>
    <div class="v3dbar">
      <button id="sp3d-spin" type="button">pause rotation</button>
      <span class="hint">drag to rotate</span>
      <span class="v3dkey">
        <span><i style="background:var(--statistics)"></i>ℓ=0</span>
        <span><i style="background:var(--geometry)"></i>ℓ=1</span>
        <span><i style="background:var(--information)"></i>ℓ=2</span>
        <span><i style="background:var(--algebra)"></i>ℓ=3</span>
        <span><i style="background:var(--order)"></i>ℓ≥4</span>
      </span>
    </div>
    <figcaption><b>The shapes stratify by angular momentum.</b> Each ℓ occupies its own
    layer in depth, and within a layer the bound and the multiplicity spread into a
    block. Nothing in the figure closes: the index sits at K0, meaning every one of the
    five operators generates a channel shape the table has no row for.</figcaption>
  </figure>
</section>

<section>
  <div class="shead"><span class="snum">03</span><h2>Twenty-five rows carry a decimal where an integer belongs</h2></div>
  <div class="note warn">
    <span class="lab">And all twenty-five are the best rows in the table</span>
    <p><span class="mono">B</span> is <span class="mono">min(p, n₀−ℓ−1)</span>, a Pauli
    bound, and an integer in 104,807 rows. In <strong>twenty-five</strong> it holds a
    decimal — 0.19569, 0.10803, 0.00449. <strong>Every one of them is graded
    <em>measured</em> and <em>witnessed</em></strong>: 25 of the 358 most authoritative
    rows the table has, seven per cent of them.</p>
    <p class="mono" style="font-size:.85rem;margin:14px 0">B 0.19569 · delta 0.53527 · Z 5 ·
    charge 1 · ℓ 1 · mult 2 · measured/witnessed<br>
    <span style="color:var(--muted)">source: NIST ASD fetched 2026-08-14 … BI 2P* n=2-9, 11 members</span></p>
    <p style="margin-bottom:0">B and delta are decimals of the same magnitude, which is
    what a column slip looks like. <strong>Recorded, not repaired.</strong> The twenty-five
    are dropped from the index, counted and described — the instrument does not guess what
    the true bound was.</p>
  </div>
</section>

<section>
  <div class="shead"><span class="snum">04</span><h2>Two columns carrying one distinction</h2></div>
  <div class="tablewrap">
  <table>
    <thead><tr><th>grade</th><th style="text-align:right">rows</th><th>witness</th><th style="text-align:right">rows</th></tr></thead>
    <tbody>
      <tr><td class="name">computed</td><td class="num">103,545</td><td class="name">unwitnessed</td><td class="num">104,474</td></tr>
      <tr><td class="name">exact</td><td class="num">929</td><td class="name">witnessed</td><td class="num">358</td></tr>
      <tr><td class="name">measured</td><td class="num">358</td><td></td><td></td></tr>
    </tbody>
    <caption>The witnessed rows are <b>exactly</b> the measured rows — the same set,
    checked row by row, not merely the same count.</caption>
  </table>
  </div>
  <div class="note good">
    <span class="lab">A live test of the chart criterion, on a source it never saw</span>
    <p>So <span class="mono">witness</span> is a function of <span class="mono">grade</span>
    — computed and exact are unwitnessed, measured is witnessed — and that function is
    <strong>monotone</strong>. The criterion says a monotone redundant coordinate cannot
    move the channel. Measured:</p>
    <p class="mono" style="margin:12px 0">(ℓ, grade) &nbsp;&nbsp;&nbsp;&nbsp;21 cells &nbsp; K3<br>
    (ℓ, grade, wit) &nbsp;21 cells &nbsp; K3 &nbsp;&nbsp;— unchanged</p>
    <p style="margin-bottom:0"><strong>The first confirmation of the chart criterion
    outside the element address</strong>, on a source it was never fitted to.</p>
  </div>
  <div class="note">
    <span class="lab">And the same source sits in two channels</span>
    <p style="margin-bottom:0">Charted by what a channel <em>is</em> — (ℓ, B, mult) — it is
    <strong>K0</strong>. Charted by how well it is <em>known</em> — (ℓ, grade, witness) —
    it is <strong>K3</strong>, geometry and statistics, at cell (3, 9, 3). Neither is the
    truer chart; they answer different questions.</p>
  </div>
</section>

<footer class="foot">
  <p style="margin-bottom:0">Produced by <code>python3 spectra.py</code>, pinned by
  <code>python3 spectra.py --selftest</code> (22 fixtures). 209 shapes · channel K0 ·
  25 malformed rows recorded, not repaired.</p>
</footer>
"""

ENTROPY = """
<header class="mast">
  <p class="eyebrow">Research plate · master index eight</p>
  <h1>The Entropy&nbsp;Index</h1>
  <p class="dek">How much each seated index says, in bits — and the first admissible
  coordinates this tree has found that are not counts of anything.</p>
  <div class="stamp">
    <span>instrument <b>entropy.py</b></span>
    <span>members <b>the nine</b></span>
    <span>channel <b>K2</b></span>
    <span>cell <b>(2, 4, 5)</b></span>
  </div>
</header>

<div class="note" style="margin-top:26px">
  <span class="lab">Second-order, and saying so first</span>
  <p style="margin-bottom:0">Its members are the nine seated indexes and its coordinates
  measure <em>them</em> — so it is a function of the inventory, like the master index and
  the refusal index, and unlike the fibrations, the ladder, provenance and the channel
  index. <strong>That matters for counting:</strong> the supply of second-order indexes is
  bounded only by the supply of admissible measurements, which is not a bound. Nothing
  here should be read as "the classification has one more member".</p>
</div>

<section>
  <div class="shead"><span class="snum">01</span><h2>Three coordinates, and no banding</h2></div>
  <div class="kv">
    <div><dt>H_max</dt><dd style="font-size:.95rem">largest marginal<small>Shannon entropy, bits</small></dd></div>
    <div><dt>H_min</dt><dd style="font-size:.95rem">smallest marginal</dd></div>
    <div><dt>H_joint</dt><dd style="font-size:.95rem">log₂|X|<small>uniform on members</small></dd></div>
  </div>
  <div class="note">
    <span class="lab">Why real values need no bands here</span>
    <p style="margin-bottom:0">Banding is where two earlier coordinates died. The closure
    operators take the <em>observed alphabet</em> as their chain, so a coordinate may take
    any values that order — the chain is simply the nine observed entropies. Nothing is cut
    into bands and no band edge is chosen.</p>
  </div>
</section>

<section>
  <div class="shead"><span class="snum">02</span><h2>All three pass the chart criterion</h2></div>
  <div class="tablewrap">
  <table>
    <thead><tr><th>coordinate</th><th style="text-align:right">moves on</th><th>verdict</th></tr></thead>
    <tbody>
      <tr><td class="name">H_max</td><td class="num">0 of 9</td><td class="yes">ADMISSIBLE</td></tr>
      <tr><td class="name">H_min</td><td class="num">0 of 9</td><td class="yes">ADMISSIBLE</td></tr>
      <tr><td class="name">H_joint</td><td class="num">0 of 9</td><td class="yes">ADMISSIBLE</td></tr>
      <tr style="opacity:.6"><td class="name">arity</td><td class="num">9 of 9</td><td class="no">disqualified</td></tr>
      <tr style="opacity:.6"><td class="name">density</td><td class="num">9 of 9</td><td class="no">disqualified</td></tr>
    </tbody>
    <caption>The same test that killed arity and density, applied to entropy.</caption>
  </table>
  </div>
  <div class="note good">
    <span class="lab">And it is not an accident</span>
    <p>Appending g(x) = x₀ adds a coordinate whose marginal is a <em>copy</em> of
    coordinate 0's, so it adds a duplicate to the multiset of marginal entropies — which
    cannot change the largest or the smallest. And the append is a bijection on members, so
    |X| and therefore H_joint are untouched.</p>
    <p style="margin-bottom:0"><strong>Density moves because the box grows. Entropy is
    computed on the members, and the members do not.</strong> These are the first
    admissible coordinates in this tree that are not counts — height, width, cells,
    comparable pairs and join-irreducibles are all counts of something.</p>
  </div>
</section>

<section>
  <div class="shead"><span class="snum">03</span><h2>The nine, in bits</h2></div>
  <figure class="plate">
    <div class="v3d"><canvas id="en3d" aria-label="The nine seated indexes in entropy space"></canvas></div>
    <div class="v3dbar">
      <button id="en3d-spin" type="button">pause rotation</button>
      <span class="hint">drag to rotate</span>
      <span class="hint">H_max → H_min → H_joint</span>
    </div>
    <figcaption><b>The two periodic charts stand apart.</b> Janet and the periodic layout
    carry three to four bits in their largest marginal where every other index carries one
    or two — they are the only indexes with hundreds of members. The remaining seven cluster
    tightly, which is why <span class="mono">(H_max, H_min)</span> alone already separates
    all nine.</figcaption>
  </figure>
</section>

<section>
  <div class="shead"><span class="snum">04</span><h2>One coordinate is notation, not evidence</h2></div>
  <div class="note warn">
    <span class="lab">H_joint is a relabelling of a coordinate the tree already had</span>
    <p style="margin-bottom:0">It is log₂ of the cell count, and log₂ is monotone — so it
    separates exactly the indexes <span class="mono">cells</span> separates, six values for
    six distinct sizes. It is kept because the triple is the natural statement of "how much
    does this index say", and it is <strong>flagged</strong> so a reader does not count it
    as new evidence. The genuinely new content is H_max and H_min, and that pair alone is
    already injective on the nine and already K2.</p>
  </div>
  <ul class="tight">
    <li><strong>Refused:</strong> to call this the entropy of anything <em>physical</em>.
    The corpus's physical entropy is the bounds index — Bekenstein, Bousso — which is a
    <em>member</em> of the master index. The two share a word and nothing else.</li>
    <li><strong>Refused:</strong> to treat the nine as a sample. The entropies are exact for
    those nine and estimate nothing wider.</li>
    <li><strong>Refused:</strong> to read K2 as agreement with the master index. Same
    channel, different cell — (2, 4, 5) against (2, 5, 2).</li>
  </ul>
</section>

<footer class="foot">
  <p style="margin-bottom:0">Produced by <code>python3 entropy.py</code>, pinned by
  <code>python3 entropy.py --selftest</code> (21 fixtures). Nine members · channel K2 ·
  three admissible coordinates, one of them flagged as notation.</p>
</footer>
"""

OCTAD = """
<header class="mast">
  <p class="eyebrow">Research plate · the figure, revised</p>
  <h1>The&nbsp;Octad</h1>
  <p class="dek">It was a hexad. Two more indexes were seated, and every one of the
  six-vertex properties failed.</p>
  <div class="stamp">
    <span>instrument <b>hexad.py</b></span>
    <span>vertices <b>8</b></span>
    <span>threads <b>28</b></span>
    <span>channel <b>K0</b></span>
  </div>
</header>

<div class="note warn" style="margin-top:26px">
  <span class="lab">This plate corrects its own earlier version</span>
  <p style="margin-bottom:0">The six-vertex figure closed in statistics, had a
  diagonal-to-deficit correspondence, and seated itself at a fixed point. <strong>All three
  were properties of those six.</strong> At eight the channel is gone, the correspondence
  fails, and the self-seating cycles. The instrument keeps the name
  <span class="mono">hexad.py</span> because the finding is precisely that the figure
  grows.</p>
</div>

<section>
  <div class="shead"><span class="snum">01</span><h2>Eight vertices</h2></div>
  <div class="tablewrap">
  <table>
    <thead><tr><th>master index</th><th>cell (K, h, w)</th><th>order</th><th>members are</th></tr></thead>
    <tbody>
      <tr><td class="name">the refusal index</td><td class="cell">(0, 5, 4)</td><td>second</td><td>refusal sets</td></tr>
      <tr><td class="name">provenance</td><td class="cell">(0, 5, 5)</td><td>first</td><td>the 26 axes</td></tr>
      <tr style="background:color-mix(in srgb,var(--geometry) 8%,transparent)"><td class="name">the channel index</td><td class="cell">(0, 16, 24)</td><td>first</td><td>209 channel shapes</td></tr>
      <tr><td class="name">the ionisation ladder</td><td class="cell">(0, 18, 16)</td><td>first</td><td>98 transitions</td></tr>
      <tr style="background:color-mix(in srgb,var(--geometry) 8%,transparent)"><td class="name">the entropy index</td><td class="cell">(2, 4, 5)</td><td>second</td><td>the nine, in bits</td></tr>
      <tr><td class="name">MI — the nine</td><td class="cell">(2, 5, 2)</td><td>second</td><td>nine indexes</td></tr>
      <tr><td class="name">the shell fibration</td><td class="cell">(3, 26, 17)</td><td>first</td><td>170 elements</td></tr>
      <tr><td class="name">the Janet fibration</td><td class="cell">(7, 30, 12)</td><td>first</td><td>the same 170</td></tr>
    </tbody>
    <caption>The two highlighted rows are the new ones. Five first-order, three
    second-order.</caption>
  </table>
  </div>
</section>

<section>
  <div class="shead"><span class="snum">02</span><h2>The figure, and its threads</h2></div>
  <p class="sub">Height left to right, width bottom to top, channel K into the depth. A
  thread between two vertices is their join. Drag to rotate.</p>
  <figure class="plate">
    <div class="v3d"><canvas id="oc3d" aria-label="Eight master indexes as eight points with twenty-eight join threads"></canvas></div>
    <div class="v3dbar">
      <button id="oc3d-spin" type="button">pause rotation</button>
      <span class="hint">drag to rotate</span>
      <span class="v3dkey">
        <span><i style="background:var(--accent)"></i>thread lands on a vertex</span>
        <span><i style="background:var(--algebra)"></i>thread escapes</span>
        <span><i style="border:2px dashed var(--algebra);background:none"></i>where it lands instead</span>
      </span>
    </div>
    <figcaption><b>Fourteen of the twenty-eight threads land; fourteen escape.</b> At six
    it was ten of fifteen. The hollow rings are the nine distinct cells the escaping threads
    land on — fewer than fourteen, because several escapes share a destination.</figcaption>
  </figure>
</section>

<section>
  <div class="shead"><span class="snum">03</span><h2>Three properties, and all three fail</h2></div>
  <div class="tablewrap">
  <table>
    <thead><tr><th>vertices</th><th>channel</th><th>own cell</th><th style="text-align:right">escapes</th><th style="text-align:right">distinct</th><th style="text-align:right">E(info)</th><th style="text-align:right">rounds</th><th>self-seating</th></tr></thead>
    <tbody>
      <tr><td class="name">six</td><td><span class="chip c3">K2</span></td><td class="cell">(2, 4, 2)</td><td class="num">5</td><td class="num">5</td><td class="num">5</td><td class="num">1</td><td class="yes">FIXED POINT</td></tr>
      <tr><td class="name">seven</td><td><span class="chip" style="color:var(--faint)">K0</span></td><td class="cell">(0, 4, 3)</td><td class="num">9</td><td class="num">5</td><td class="num">5</td><td class="num">1</td><td class="yes">FIXED POINT</td></tr>
      <tr style="background:color-mix(in srgb,var(--algebra) 8%,transparent)"><td class="name">eight</td><td><span class="chip" style="color:var(--faint)">K0</span></td><td class="cell">(0, 4, 4)</td><td class="num">14</td><td class="num">9</td><td class="num">10</td><td class="num">2</td><td class="no">CYCLE, period 2</td></tr>
    </tbody>
  </table>
  </div>

  <div class="note warn">
    <span class="lab">The channel: destroyed by the seventh vertex alone</span>
    <p style="margin-bottom:0">At six the figure closed in <strong>statistics</strong> — the
    master index's own channel, which read as a striking invariance of level. Adding the
    entropy index alone takes it to K0, and it does not come back. That K2 was a fact about
    those six, not about the construction.</p>
  </div>

  <div class="note warn">
    <span class="lab">The correspondence: true at six, and now explained</span>
    <p>"The escaping diagonals are exactly what the index fails to know" held at six — five
    escapes, five distinct cells, deficit five. <strong>The reason is a one-round
    closure.</strong> Join-closure iterates: the joins of the new cells with the old must be
    added too. At six the second round adds nothing, so the pairwise diagonals are the whole
    deficit. At eight the second round adds one more, and nine distinct diagonals stand
    against a deficit of ten.</p>
    <p style="margin-bottom:0">What is <em>always</em> true is that the full join-closure is
    the information deficit — which is definitional, and says less.</p>
  </div>

  <div class="note warn">
    <span class="lab">The fixed point: lost, and the explanation refuted</span>
    <p style="margin-bottom:0">At six the figure seated itself at a fixed point where the
    refusal index cycled, and the explanation offered was that the figure's members are
    <em>cells already computed</em>, so a new one disturbs nothing. <strong>That explanation
    predicted convergence at every size, and eight cycles.</strong> Self-seating converges
    for some seated sets and not others, and nothing here says which in advance.</p>
  </div>
</section>

<section>
  <div class="shead"><span class="snum">04</span><h2>So no polygon is the classification</h2></div>
  <div class="note">
    <span class="lab">Eighty-four more are a comprehension away</span>
    <p>Nine per-index measurements all pass the chart criterion. Three-coordinate charts
    from them give <strong>84 further second-order indexes on 21 distinct vertices, 20 of
    which this figure does not have</strong> — and arity two gives 36 more, arity four 126.
    Counting them is counting one's own measurements.</p>
    <p style="margin-bottom:0"><strong>The rules are complete; the figure is not.</strong>
    Eight lawful channels and no more, the chart criterion fixed, the reachability law
    without exception — none of that moves when a new index is built. The vertex set moves
    every time. <em>The classification is of kinds, not of members.</em></p>
  </div>
</section>

<footer class="foot">
  <p style="margin-bottom:0">Produced by <code>python3 hexad.py</code>, pinned by
  <code>python3 hexad.py --selftest</code> (25 fixtures) and
  <code>python3 sources.py --selftest</code> (16). Eight vertices · 28 threads ·
  three corrected claims.</p>
</footer>
"""

PLATES = (
    ('spx.html', 'The Channel Index', SPECTRA, 'sp3d', 'spectra',
     'B', 'multiplicity', 'ℓ', 3.6, False, None),
    ('ent.html', 'The Entropy Index', ENTROPY, 'en3d', 'entropy',
     'H_max', 'H_min', 'H_joint', 8, True, None),
    ('oct.html', 'The Octad', OCTAD, 'oc3d', 'octad',
     'height', 'width', 'K', 8, True, 'edges'),
)

# THE PLATE EACH ONE IS THE SOURCE OF, under the name the tree keeps it by.
# The rename happened outside this program; the selftest pins the pairing.
ARCHIVED = {'spx.html': 'spectra-plate.html',
            'ent.html': 'entropy-plate.html',
            'oct.html': 'octad-plate.html'}


def render(spec):
    """Build one plate in memory.  Returns (filename, page text)."""
    fn, title, body, sid, key, xl, yl, zl, r, lab, extra = spec
    src = D[key]
    pts = src['pts'] if extra else src
    js = ("scatter3d({id:'%s',points:%s,%sxlab:'%s',ylab:'%s',zlab:'%s',"
          "r:%s,height:470,scale:0.215,%s%s});"
          % (sid, json.dumps(pts, separators=(',', ':')),
             ("edges:%s," % json.dumps(src['edges'], separators=(',', ':'))
              if extra else ""),
             xl, yl, zl, r,
             ("stroke:true,labels:true," if lab else ""),
             ("colour:p=>p.c" if extra else COL)))
    return fn, page(title, body, js)


def build():
    for spec in PLATES:
        fn, out = render(spec)
        open(fn, 'w').write(out)
        print("wrote", fn)


def md5(b):
    return hashlib.md5(b if isinstance(b, bytes) else b.encode()).hexdigest()


def selftest():
    """Every figure here was MEASURED by running this file, never chosen."""
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-52s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    # THE INPUTS, pinned by md5.  style.css is the same file the sibling reads
    # and carries the same hash; that is the claim, not a coincidence.
    for name, want, size in (('style.css', 'bfec0696c0e551145759a290ad5d500a', 7280),
                             ('w3d-r2.js', '4154dde8161ec3e0dc154fadab88e7dd', 6542),
                             ('oct_pts.json', '604eb92e920b965623cc531e11fdbb08', 8544)):
        b = open(os.path.join(HERE, name), 'rb').read()
        chk("%s is present, %d bytes" % (name, size), len(b), size)
        chk("%s md5" % name, md5(b), want)

    chk("style.css ends without a newline", STYLE.endswith('\n'), False)
    chk("w3d-r2.js ends with one", W3D.endswith('\n'), True)

    # r2 IS THE GENERATION WITH EDGES, and the octad is why this file needs it.
    chk("w3d-r2.js carries the edges pass", 'opts.edges' in W3D, True)
    chk("and is not the r1 the sibling pins",
        md5(W3D) == 'f9348be9b963d26e2c63240fc974e060', False)

    # THE POINT SETS, measured off the restored file.
    chk("spectra points", len(D['spectra']), 209)
    chk("entropy points", len(D['entropy']), 9)
    chk("octad points", len(D['octad']['pts']), 17)
    chk("octad edges", len(D['octad']['edges']), 28)

    # THE WHOLE CLAIM: each page is byte-identical to the plate in the tree.
    for spec in PLATES:
        fn, out = render(spec)
        want = open(os.path.join(HERE, ARCHIVED[fn]), 'rb').read()
        chk("%s reproduces %s byte for byte" % (fn, ARCHIVED[fn]),
            (len(out.encode()), md5(out)), (len(want), md5(want)))

    print("build_plates8 selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    build()
