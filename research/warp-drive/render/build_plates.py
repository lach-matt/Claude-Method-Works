#!/usr/bin/env python3
r"""
build_plates.py -- the ionisation, provenance and refusal plates.

Write the three new plates, sharing the style and the 3-D widget.

    python3 build_plates.py             writes ion.html, axs.html, rid.html
    python3 build_plates.py --selftest  fixtures

===============================================================================
0. IT COULD NOT RUN AT ALL, AND THE FOUR INPUTS ARE RESTORED BY EXTRACTION
===============================================================================

**THIS FILE RAISED `FileNotFoundError` AT IMPORT.**  Its four inputs --
`style.css`, `w3d.js`, `new_pts.json` and (for the sibling) `oct_pts.json` --
were never committed, and nothing in the tree said so.  They are RECOVERABLE
and are now restored, because `page()` INLINES every one of them into the
plate it writes: the plate is a complete record of its own inputs.

WHAT WAS SEARCHED, and found nothing:

    git log --all --diff-filter=D -- 'research/warp-drive/render/style.css'
    git log --all -- 'research/warp-drive/render/*.css' \
                     'research/warp-drive/render/*.js'
    git log --all --diff-filter=A --name-only --pretty=format: \
        | grep -E '(style\.css|w3d\.js|new_pts\.json|oct_pts\.json)$'
    find . -name style.css -o -name w3d.js -o -name new_pts.json \
                                          -o -name oct_pts.json

NO PATH UNDER `render/` HAS EVER HELD ANY OF THE FOUR -- both `--diff-filter=D`
and `--diff-filter=A` come back empty.  Two other `style.css` turn up and NEITHER IS
THIS ONE, checked rather than assumed: `recovered/style.css`, on disk, 700
bytes, md5 0c191a7d011a80a8fac20db3560615a8, a DejaVu print stylesheet out of an
unrelated chat; and `public/style.css`, in history only and not on disk now, the
website's own sheet, whose 16 committed versions were each hashed against
bfec0696c0e551145759a290ad5d500a and none matches.  No
file anywhere is named `w3d.js`, `new_pts.json` or `oct_pts.json`, and nothing
in the tree references those names but these two programs.  So the plates are
the only source, and extraction is the only route.

HOW EACH INPUT WAS RECOVERED, from the shape `page()` writes:

    line 1          <title>
    line 2          the Google-Fonts <link>
    lines 3..N      STYLE            -> style.css      (no trailing newline:
                                        page() supplies the \n, and the plates
                                        have no blank line before the wrap div)
    <div class="wrap"> ... </div>     the body, per plate
    <script>
      W3D                             -> w3d-r?.js     (keeps its trailing \n)
      <blank>
      scatter3d({...});               -> the points, and the octad's edges
    </script>

`style.css` is IDENTICAL in all seven plates in this directory -- md5
bfec0696c0e551145759a290ad5d500a, 7,280 bytes -- so it is one file and not a
per-plate copy.  The points are the JSON literal in each plate's single
`scatter3d(...)` call, read back out by bracket matching.

===============================================================================
1. `w3d.js` IS RE-PINNED TO `w3d-r1.js`, BECAUSE ONE NAME HELD TWO FILES
===============================================================================

**THE NAME `w3d.js` CANNOT BE RESTORED, BECAUSE IT DENOTED TWO DIFFERENT
CONTENTS AND THIS FILE'S PLATES PIN THE EARLIER ONE.**  Measured off the
plates, not argued:

    generation   bytes   md5                                inlined by
    r1           5,753   f9348be9b963d26e2c63240fc974e060   ion, axs, rid
    r2           6,542   4154dde8161ec3e0dc154fadab88e7dd   spx, ent, oct, hexad
    scatter3d.js 7,975   07ceeb670663d6228b839648f4c915f4   every later plate

r2 adds the `opts.edges` pass and the hollow-point branch; `scatter3d.js` adds
the two-pass axis paint and the label ground.  Each is a superset of the last,
so this file WOULD run against r2 -- and would then write a plate that is not
the one in the tree.  `plate.py` already records the count from the other side:
"The older plates each froze their own copy and THREE GENERATIONS have since
diverged."  These are those three.

RE-PINNED, NOT LOOSENED: this file reads `w3d-r1.js` and the sibling reads
`w3d-r2.js`.  The ambiguous name is retired rather than given one of its two
meanings.  `scatter3d.js` is the living runtime and is NOT a substitute here --
a plate built against it is a different plate.

WHAT IS VERIFIED: all three pages this file writes are BYTE-IDENTICAL to the
plates already in the tree (`ion.html` == `ions-plate.html` and so on; the
`-plate` names are a rename that happened outside this program).  The selftest
below rebuilds all three in memory and compares md5s; run it before trusting
any edit here.

INPUTS RESOLVE AGAINST THIS FILE'S OWN DIRECTORY, not the working directory,
which is new -- `open('style.css')` only worked when run from inside `render/`.
Outputs are unchanged and still land in the working directory.
"""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

STYLE = open(os.path.join(HERE, 'style.css')).read()
# RE-PINNED from 'w3d.js' -- see section 1.  That name held two generations of
# the widget and these three plates inline the first of them.
W3D = open(os.path.join(HERE, 'w3d-r1.js')).read()
PTS = json.load(open(os.path.join(HERE, 'new_pts.json')))
COLJS = ("colour:p=>['--statistics','--geometry','--information',"
         "'--algebra','--order'][p.l]")


def page(title, body, script):
    return ("<title>%s</title>\n"
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
            'family=Spectral:ital,wght@0,300;0,400;0,600;0,800;1,400&'
            'family=IBM+Plex+Mono:wght@400;500;600&display=swap">\n'
            "%s\n<div class=\"wrap\">\n%s\n</div>\n"
            "<script>\n%s\n%s\n</script>\n" % (title, STYLE, body, W3D, script))


# ============================================================ MI-4
IONS = """
<header class="mast">
  <p class="eyebrow">Research plate · master index four</p>
  <h1>The Ionisation&nbsp;Ladder</h1>
  <p class="dek">An index whose members are transitions, not elements — and the
  first source in this tree to reach a channel the element address provably
  cannot.</p>
  <div class="stamp">
    <span>instrument <b>ions.py</b></span>
    <span>members <b>98 transitions</b></span>
    <span>arity <b>7</b></span>
    <span>channel <b>K0</b></span>
  </div>
</header>

<div class="note warn" style="margin-top:26px">
  <span class="lab">Status first, because everything here rests on it</span>
  <p style="margin-bottom:0"><strong>This index is built on a reconstruction and
  the corpus says so.</strong> <span class="mono">populate.ionisation_cells</span>
  carries the status RECONSTRUCTED in its own docstring: chapter 7 makes a Λ₈ cell
  a <em>transition</em>, so an element is not a cell and a mapping had to be
  <em>chosen</em>. "Nothing else in the store fixes this mapping." Every channel
  below is a fact about that mapping as much as about ions.</p>
</div>

<section>
  <div class="shead"><span class="snum">01</span><h2>5,778 rows, 98 transitions</h2></div>
  <p class="sub">A Λ₈ cell is (sn, sl, k, q, tn, tl, g, 2S): the source subshell the
  electrons leave, its parent occupancy, how many leave, the target subshell, how
  many arrive, and the ion's ground multiplicity.</p>

  <div class="kv">
    <div><dt>stage rows</dt><dd>5,778<small>element × charge</small></dd></div>
    <div><dt>distinct cells</dt><dd>98<small>the index</small></dd></div>
    <div><dt>electron counts</dt><dd>107<small>nine collide</small></dd></div>
    <div><dt>charted arity</dt><dd>7 of 8<small>2S dropped</small></dd></div>
  </div>

  <div class="note">
    <span class="lab">Two things the construction had to settle</span>
    <p><strong>The eighth slot is always None.</strong> 2S is known only where the
    ion's term is known, and over all 5,778 rows the corpus banks it
    <em>not once</em>. A one-valued coordinate carries no information and would
    widen every closure for free, so the index is charted on the seven that are
    determined — recorded, not silent, and the selftest pins that the slot really
    is constant rather than merely sparse.</p>
    <p style="margin-bottom:0"><strong>The collapse is structural.</strong>
    <span class="mono">ionisation_cells</span> builds each cell from the electron
    count alone — never from Z — so every element's ladder is a suffix of one
    universal ladder. Quoting 5,778 as a cell count would be counting elements
    while claiming to count transitions.</p>
  </div>
</section>

<section>
  <div class="shead"><span class="snum">02</span><h2>The ladder in three dimensions</h2></div>
  <p class="sub">Source shell left to right, the parent occupancy bottom to top, the
  source subshell into the depth — coloured by the <em>target</em> subshell. Drag to
  rotate.</p>
  <figure class="plate">
    <div class="v3d"><canvas id="io3d" aria-label="98 ionisation transitions in (source shell, occupancy, source subshell) space"></canvas></div>
    <div class="v3dbar">
      <button id="io3d-spin" type="button">pause rotation</button>
      <span class="hint">drag to rotate</span>
      <span class="v3dkey">
        <span><i style="background:var(--statistics)"></i>target ℓ=0 s</span>
        <span><i style="background:var(--geometry)"></i>tℓ=1 p</span>
        <span><i style="background:var(--information)"></i>tℓ=2 d</span>
        <span><i style="background:var(--algebra)"></i>tℓ=3 f</span>
      </span>
    </div>
    <figcaption><b>A comb per subshell, shell by shell — and the colour is the
    <em>target</em>.</b> Source shell runs left to right, the parent occupancy the
    electrons leave from bottom to top, the source subshell into the depth. Plotting
    source shell against <em>target</em> shell was tried first and collapsed to a
    line: an electron almost always leaves and arrives in the same shell, so that
    projection is degenerate and says only that. Carrying the target as colour
    instead keeps it visible — a point whose colour disagrees with its depth is a
    transition that crosses subshells.</figcaption>
  </figure>
</section>

<section>
  <div class="shead"><span class="snum">03</span><h2>It closes nothing, and faithfully it can close nothing</h2></div>
  <div class="kv">
    <div><dt>channel</dt><dd style="color:var(--faint)">K0<small>no language closes it</small></dd></div>
    <div><dt>cell</dt><dd style="font-size:1rem">(0, 18, 16)<small>admissible chart</small></dd></div>
    <div><dt>sub-charts</dt><dd>120<small>arity 2 to 7</small></dd></div>
    <div><dt>faithful ones</dt><dd>32<small>all K0</small></dd></div>
  </div>
  <div class="tablewrap" style="margin-top:24px">
  <table>
    <thead><tr><th>reached by</th><th>channels</th></tr></thead>
    <tbody>
      <tr><td class="name">any sub-chart</td><td class="cell">K0, K2, K3, <b>K4</b>, K7</td></tr>
      <tr><td class="name">injectively</td><td class="cell">K0 — and nothing else</td></tr>
      <tr><td class="name">never</td><td class="cell">K1, K5, K6</td></tr>
    </tbody>
    <caption>Thirty-two sub-charts keep all 98 cells distinct and every one closes
    nothing. As a <em>faithful</em> index the ladder is flatly K0, with no
    alternative chart available.</caption>
  </table>
  </div>
</section>

<section>
  <div class="shead"><span class="snum">04</span><h2>And it reaches K4</h2></div>
  <p class="sub">The census over the element address proved K1, K4 and K5 unreachable
  — by any of 372 charts. This source reaches one of them.</p>

  <div class="note good">
    <span class="lab">A new source, not a new arrangement — demonstrated</span>
    <p><span class="mono">(sℓ, tℓ)</span> — the source subshell's ℓ against the
    target's — gives <strong>7 cells closing {information, statistics} = K4</strong>.
    One chart of the hundred and twenty, and the only one. It is the first object
    in this tree to sit in K4.</p>
    <p style="margin-bottom:0">The earlier negative result stands unaltered: it was
    a statement about the element-address pool, and this is a different pool.
    Changing what a <em>member is</em> reaches a channel that no rearrangement
    could.</p>
  </div>

  <div class="note warn">
    <span class="lab">And the price is the same price K6 paid</span>
    <p style="margin-bottom:0">That chart holds 7 cells against 98 —
    <strong>ninety-one transitions lose their identity.</strong> K4 here is
    reachable and <em>not faithful</em>, exactly as K6 is on the Janet side. Two
    channels now sit in that category, which is a pattern worth a ruling and not
    yet a ruling.</p>
  </div>
</section>

<footer class="foot">
  <p style="margin-bottom:0">Produced by <code>python3 ions.py</code>, pinned by
  <code>python3 ions.py --selftest</code>. 98 transitions · channel K0 ·
  K4 reachable, unfaithful · the mapping RECONSTRUCTED throughout.</p>
</footer>
"""

# ============================================================ MI-5
AXES = """
<header class="mast">
  <p class="eyebrow">Research plate · master index five</p>
  <h1>The Provenance&nbsp;Index</h1>
  <p class="dek">Twenty-six measurements as members, charted by where each value
  comes from and how much you must know to fix it. The only index here whose
  members are ways of knowing.</p>
  <div class="stamp">
    <span>instrument <b>axes.py</b></span>
    <span>members <b>26 axes</b></span>
    <span>cells <b>14</b></span>
    <span>channel <b>K0</b></span>
  </div>
</header>

<section style="margin-top:34px">
  <div class="shead"><span class="snum">01</span><h2>Four coordinates, and one of them is mine</h2></div>
  <div class="tablewrap">
  <table>
    <thead><tr><th>coordinate</th><th>what it is</th><th>provenance</th></tr></thead>
    <tbody>
      <tr><td class="name">status</td><td>READ / DERIVED / PINNED / RECONSTRUCTED</td><td><b style="color:var(--algebra)">GIVEN, ordering RECONSTRUCTED</b></td></tr>
      <tr><td class="name">args</td><td>how many arguments fix the value: 0, 1, 2</td><td class="yes">MEASURED</td></tr>
      <tr><td class="name">reg</td><td>the description cites a Register entry</td><td class="yes">MEASURED</td></tr>
      <tr><td class="name">sec</td><td>the description cites a volume section</td><td class="yes">MEASURED</td></tr>
    </tbody>
    <caption>Three of four are measured. The fourth is not, and it is named.</caption>
  </table>
  </div>

  <div class="note warn">
    <span class="lab">The ordering I supplied, and what depends on it</span>
    <p>The four provenance words are given by the corpus, but a closure operator
    needs an <em>order</em> on them and the corpus states none. The order used —
    READ &lt; DERIVED &lt; PINNED &lt; RECONSTRUCTED, read as distance from the
    observed data — is <strong>RECONSTRUCTED</strong>.
    <span class="mono">STATUS_ORDER_IS_RECONSTRUCTED</span> is True in the
    instrument, and a reader who rejects the ordering should reject the channel
    with it.</p>
    <p style="margin-bottom:0"><strong><span class="mono">args</span> needs no such
    apology, because it is a count.</strong> 0 &lt; 1 &lt; 2 is the ordering of the
    integers. And it is measured rather than read off the names: the probe calls
    <span class="mono">populate</span> over eight elements and five charge stages
    and asks which keys actually move. An early version probed iron against cobalt
    and reported <em>period</em> and <em>block</em> constant — they are not, the two
    elements simply share them.</p>
  </div>
</section>

<section>
  <div class="shead"><span class="snum">02</span><h2>The census of provenance</h2></div>
  <figure class="plate">
    <svg viewBox="0 0 860 210" role="img" aria-label="Provenance census of the 26 axes">
      <text x="24" y="20" font-size="9.5" fill="var(--muted)" letter-spacing="1.4">STATUS — WHAT KIND OF KNOWLEDGE</text>
      <g font-size="11">
        <text x="24" y="52" fill="var(--statistics)">READ</text>
        <rect x="140" y="43" width="279" height="12" rx="2" fill="var(--statistics)"/><text x="429" y="53" font-size="10" fill="var(--body)">9</text>
        <text x="24" y="80" fill="var(--geometry)">DERIVED</text>
        <rect x="140" y="71" width="279" height="12" rx="2" fill="var(--geometry)"/><text x="429" y="81" font-size="10" fill="var(--body)">9</text>
        <text x="24" y="108" fill="var(--information)">PINNED</text>
        <rect x="140" y="99" width="155" height="12" rx="2" fill="var(--information)"/><text x="305" y="109" font-size="10" fill="var(--body)">5</text>
        <text x="24" y="136" fill="var(--algebra)">RECONSTRUCTED</text>
        <rect x="140" y="127" width="93" height="12" rx="2" fill="var(--algebra)"/><text x="243" y="137" font-size="10" fill="var(--body)">3</text>
      </g>
      <text x="470" y="20" font-size="9.5" fill="var(--muted)" letter-spacing="1.4">ARGUMENTS THAT FIX THE VALUE</text>
      <g font-size="11">
        <text x="470" y="52" fill="var(--body)">0 constant</text>
        <rect x="600" y="43" width="31" height="12" rx="2" fill="var(--faint)"/><text x="641" y="53" font-size="10" fill="var(--body)">2</text>
        <text x="470" y="80" fill="var(--body)">1 element</text>
        <rect x="600" y="71" width="232" height="12" rx="2" fill="var(--faint)"/><text x="700" y="81" font-size="10" fill="var(--panel)">15</text>
        <text x="470" y="108" fill="var(--body)">2 element + one more</text>
        <rect x="600" y="99" width="139" height="12" rx="2" fill="var(--faint)"/><text x="749" y="109" font-size="10" fill="var(--body)">9</text>
      </g>
      <line x1="24" y1="158" x2="836" y2="158" stroke="var(--rule)"/>
      <text x="24" y="180" font-size="11" fill="var(--body)">cites a Register: <tspan font-weight="600">7 of 26</tspan></text>
      <text x="260" y="180" font-size="11" fill="var(--body)">cites a section: <tspan font-weight="600">3 of 26</tspan></text>
      <text x="470" y="180" font-size="11" fill="var(--algebra)" font-weight="600">cites neither: 16 of 26</text>
      <text x="24" y="200" font-size="9.5" fill="var(--faint)">the table records what KIND of knowledge an axis is far more often than WHERE it comes from</text>
    </svg>
    <figcaption><b>Sixteen of twenty-six cite neither</b>, and that is not an
    accusation — an axis like <span class="mono">Z</span> or
    <span class="mono">occupancy</span> needs no citation, being the input or a
    definition. It does mean the provenance record is thin.</figcaption>
  </figure>
</section>

<section>
  <div class="shead"><span class="snum">03</span><h2>The index in three dimensions</h2></div>
  <p class="sub">Status left to right, argument count bottom to top, citation
  pattern into the depth. Fourteen cells for twenty-six axes. Drag to rotate.</p>
  <figure class="plate">
    <div class="v3d"><canvas id="ax3d" aria-label="26 axes on 14 provenance cells"></canvas></div>
    <div class="v3dbar">
      <button id="ax3d-spin" type="button">pause rotation</button>
      <span class="hint">drag to rotate</span>
      <span class="v3dkey">
        <span><i style="background:var(--statistics)"></i>READ</span>
        <span><i style="background:var(--geometry)"></i>DERIVED</span>
        <span><i style="background:var(--information)"></i>PINNED</span>
        <span><i style="background:var(--algebra)"></i>RECONSTRUCTED</span>
      </span>
    </div>
    <figcaption><b>A label of the form "Z +2" is a cell holding three axes.</b>
    Six cells hold more than one, and between them they hold eighteen of the
    twenty-six.</figcaption>
  </figure>
</section>

<section>
  <div class="shead"><span class="snum">04</span><h2>The coarseness is the finding</h2></div>
  <div class="note">
    <span class="lab">Twenty-six axes, fourteen cells, no injective chart</span>
    <p><strong>Six cells hold more than one axis and between them they hold
    eighteen of the twenty-six</strong>, the largest holding four. There is no
    injective chart in these coordinates and there cannot be — the box is
    4 × 3 × 2 × 2 = 48 and the coordinates simply do not separate. Two axes with
    the same status, argument count and citation pattern are
    <em>indistinguishable</em> to this index.</p>
    <p style="margin-bottom:0">That is a true statement about the corpus's
    provenance record rather than a defect of the chart. And it
    <strong>closes nothing — K0</strong>: every one of the five operators generates
    a provenance cell the corpus has no axis for.</p>
  </div>
  <div class="note warn">
    <span class="lab">The coordinate I refused to add</span>
    <p style="margin-bottom:0">Adding each axis's <em>position</em> in the table
    would make the index injective at a stroke. That is exactly why it is not
    added: position is an identifier, not a property, and an index charted on its
    own row numbers measures nothing. A first draft also harvested "mentions None"
    and "says see" from the descriptions by regex — both are artefacts of how a
    sentence was written, and both were withdrawn.</p>
  </div>
</section>

<footer class="foot">
  <p style="margin-bottom:0">Produced by <code>python3 axes.py</code>, pinned by
  <code>python3 axes.py --selftest</code>. 26 axes · 14 cells · channel K0 ·
  one coordinate ordering RECONSTRUCTED and named.</p>
</footer>
"""

# ============================================================ MI-6
RIDX = """
<header class="mast">
  <p class="eyebrow">Research plate · master index six</p>
  <h1>The Refusal&nbsp;Index</h1>
  <p class="dek">The index the tree declined to seat, built at last — and the
  fixed-point question it was declined over, settled.</p>
  <div class="stamp">
    <span>instrument <b>rindex.py</b></span>
    <span>members <b>9 refusal sets</b></span>
    <span>channel <b>K0</b></span>
    <span>fixed point <b>chart-dependent</b></span>
  </div>
</header>

<div class="note" style="margin-top:26px">
  <span class="lab">What was refused, and why this is not an overruling</span>
  <p style="margin-bottom:0"><em>"R is computed FROM the inventory. Seating it as a
  member changes the inventory, which changes R, which changes what was seated.
  That is a fixed-point problem and not a formality… <strong>Whether the iteration
  converges is open here and is the first thing to settle next.</strong>"</em>
  — the earlier instrument's own words. It is settled below, and
  <strong>the refusal survives</strong>.</p>
</div>

<section>
  <div class="shead"><span class="snum">01</span><h2>The map whose fixed point is in question</h2></div>
  <p class="sub">R(X) is a <em>set</em> of refusal kinds. To be an index it must be a
  set of <em>cells</em>, so each member's refusal set is charted — and the choice of
  chart turns out to be the whole story.</p>
  <div class="note">
    <span class="lab">F(R) = the refusal index rebuilt over an inventory containing R</span>
    <p style="margin-bottom:0">A fixed point is <span class="mono">F(R) = R</span>:
    an R unchanged by its own seating. The <strong>indicator</strong> chart — the
    8-bit vector, 1 where a kind occurs — loses nothing, and since the nine refusal
    sets are pairwise distinct it charts nine indexes onto nine cells. It is the
    obvious chart. The other three are coarsenings kept as controls.</p>
  </div>
</section>

<section>
  <div class="shead"><span class="snum">02</span><h2>The nine, in three dimensions</h2></div>
  <p class="sub">The occupancy lattice: one point wherever a seated index carries a
  refusal kind. Indexes left to right, ordered by how many kinds they carry; the eight
  kinds K0–K7 bottom to top. Drag to rotate.</p>
  <figure class="plate">
    <div class="v3d"><canvas id="ri3d" aria-label="The nine seated indexes by refusal-set size, least and greatest kind"></canvas></div>
    <div class="v3dbar">
      <button id="ri3d-spin" type="button">pause rotation</button>
      <span class="hint">drag to rotate</span>
      <span class="hint">one point per (index, kind)</span>
      <span class="v3dkey">
        <span><i style="background:var(--faint)"></i>K0 / K7 — universal</span>
        <span><i style="background:var(--accent)"></i>K2–K6 — discriminating</span>
      </span>
    </div>
    <figcaption><b>Two full rows and one empty one.</b> The K0 and K7 rows are
    continuous — both kinds are universal across all nine indexes — and the
    <b>K1 row is empty</b>: no seated index carries it. Everything that
    discriminates lives in the middle band, K2 to K6, which is why
    <span class="mono">(min, max)</span> collapses all nine to a single cell and is
    kept only as a control. Forty-two points for nine indexes.</figcaption>
  </figure>
</section>

<section>
  <div class="shead"><span class="snum">03</span><h2>The answer: chart-dependent, and the faithful charts disagree</h2></div>
  <div class="tablewrap">
  <table>
    <thead><tr><th>chart</th><th style="text-align:right">cells</th><th>faithful</th><th>channel</th><th style="text-align:right">period</th><th>verdict</th></tr></thead>
    <tbody>
      <tr style="background:color-mix(in srgb,var(--algebra) 8%,transparent)"><td class="name">indicator</td><td class="num">9</td><td class="yes">yes</td><td><span class="chip" style="color:var(--faint)">K0</span></td><td class="num">2</td><td class="no">CYCLES — no fixed point</td></tr>
      <tr><td class="name">(|R|, min, max)</td><td class="num">6</td><td class="no">no</td><td><span class="chip c7">K7</span></td><td class="num">2</td><td class="no">CYCLES — no fixed point</td></tr>
      <tr style="background:color-mix(in srgb,var(--geometry) 8%,transparent)"><td class="name">(|R|, sum)</td><td class="num">9</td><td class="yes">yes</td><td><span class="chip c7">K7</span></td><td class="num">1</td><td class="yes">FIXED POINT</td></tr>
      <tr><td class="name">(min, max)</td><td class="num">1</td><td class="no">no</td><td><span class="chip c7">K7</span></td><td class="num">1</td><td class="yes">FIXED POINT</td></tr>
    </tbody>
    <caption>Period 1 is a fixed point; any period above 1 means no R survives its
    own seating on that chart. The two highlighted rows are both faithful.</caption>
  </table>
  </div>

  <div class="note warn">
    <span class="lab">Two faithful charts, opposite answers</span>
    <p style="margin-bottom:0">Both keep nine indexes on nine cells. The indicator
    cycles; <span class="mono">(|R|, sum)</span> is a fixed point from the first
    step. So <em>"does the refusal index converge when seated?"</em>
    <strong>has no answer independent of the chart</strong> — the same shape as the
    chart-criterion finding about the master cell. Faithfulness does not settle it;
    coarseness does not settle it; only naming a chart settles it.</p>
  </div>
</section>

<section>
  <div class="shead"><span class="snum">04</span><h2>And the cycle is one bit wide</h2></div>
  <figure class="plate">
    <svg viewBox="0 0 860 230" role="img" aria-label="The two-cycle differs in the K5 bit alone">
      <text x="30" y="24" font-size="9.5" fill="var(--muted)" letter-spacing="1.4">THE TWO STATES OF THE CYCLE, AS 8-BIT REFUSAL VECTORS</text>
      <g font-size="11" fill="var(--muted)" text-anchor="middle">
        <text x="150" y="58">K0</text><text x="230" y="58">K1</text><text x="310" y="58">K2</text>
        <text x="390" y="58">K3</text><text x="470" y="58">K4</text>
        <text x="550" y="58" fill="var(--algebra)" font-weight="600">K5</text>
        <text x="630" y="58">K6</text><text x="710" y="58">K7</text>
      </g>
      <text x="100" y="94" text-anchor="end" font-size="12" fill="var(--ink)" font-weight="600">A</text>
      <g>
        <circle cx="150" cy="89" r="13" fill="var(--geometry)"/><circle cx="230" cy="89" r="13" fill="var(--geometry)"/>
        <circle cx="310" cy="89" r="13" fill="none" stroke="var(--rule-hard)"/><circle cx="390" cy="89" r="13" fill="var(--geometry)"/>
        <circle cx="470" cy="89" r="13" fill="none" stroke="var(--rule-hard)"/>
        <circle cx="550" cy="89" r="13" fill="var(--algebra)"/>
        <circle cx="630" cy="89" r="13" fill="none" stroke="var(--rule-hard)"/><circle cx="710" cy="89" r="13" fill="var(--geometry)"/>
      </g>
      <text x="100" y="154" text-anchor="end" font-size="12" fill="var(--ink)" font-weight="600">B</text>
      <g>
        <circle cx="150" cy="149" r="13" fill="var(--geometry)"/><circle cx="230" cy="149" r="13" fill="var(--geometry)"/>
        <circle cx="310" cy="149" r="13" fill="none" stroke="var(--rule-hard)"/><circle cx="390" cy="149" r="13" fill="var(--geometry)"/>
        <circle cx="470" cy="149" r="13" fill="none" stroke="var(--rule-hard)"/>
        <circle cx="550" cy="149" r="13" fill="none" stroke="var(--algebra)" stroke-width="2" stroke-dasharray="3 2"/>
        <circle cx="630" cy="149" r="13" fill="none" stroke="var(--rule-hard)"/><circle cx="710" cy="149" r="13" fill="var(--geometry)"/>
      </g>
      <rect x="528" y="66" width="44" height="106" rx="4" fill="none" stroke="var(--algebra)" stroke-width="1.5" stroke-dasharray="4 3"/>
      <text x="550" y="196" text-anchor="middle" font-size="10.5" fill="var(--algebra)" font-weight="600">the only difference</text>
      <text x="430" y="218" text-anchor="middle" font-size="10" fill="var(--muted)">A → B → A → B …   seating R makes K5 occur; recomputing with K5 present makes it stop</text>
    </svg>
    <figcaption><b>The two states of the cycle differ in exactly one cell, and those
    two cells differ in exactly one coordinate: the K5 bit.</b> K5 is one of the three
    channels proved unreachable from the element address. It is not reached here
    either — <em>it flickers</em>. A kind that appears on even iterations and vanishes
    on odd ones is not present in the corpus; it is the signature of a construction
    that does not settle.</figcaption>
  </figure>
</section>

<section>
  <div class="shead"><span class="snum">05</span><h2>So the refusal is upheld, and sharpened</h2></div>
  <div class="note good">
    <span class="lab">Nothing is seated</span>
    <p>On the faithful, obvious chart there is <strong>no R that survives its own
    seating</strong>. Seating it would mean choosing the chart that happens to
    converge — which is choosing the answer. The earlier refusal was right, and it
    is now right for a measured reason rather than a cautious one.</p>
    <p style="margin-bottom:0">What this plate offers as <em>the sixth master
    index</em> is <span class="mono">R₀</span>: the refusal index over the nine,
    before any seating — 9 cells, channel K0, cell (0, 5, 4). A perfectly good
    object with a cell of its own. What is <em>not</em> claimed is that it is a
    <strong>member</strong> of the master index.</p>
  </div>
  <ul class="tight">
    <li><strong>Refused:</strong> to call the <span class="mono">(|R|, sum)</span>
    fixed point a resolution. It is one chart of four, and the chart that disagrees
    is at least as faithful. Quoting the convergent one alone would be choosing
    evidence.</li>
    <li><strong>Refused:</strong> to read the flickering K5 as an occurrence.</li>
    <li><strong>Refused:</strong> to seat R. Nothing is added to the inventory.</li>
  </ul>
</section>

<footer class="foot">
  <p style="margin-bottom:0">Produced by <code>python3 rindex.py</code>, pinned by
  <code>python3 rindex.py --selftest</code>. 9 refusal sets · channel K0 ·
  a two-cycle one bit wide · the seating still refused.</p>
</footer>
"""

PLATES = (
    ('ion.html', 'The Ionisation Ladder', IONS, 'io3d', 'ions',
     'source n', 'occupancy k', 'source ℓ', 3.6, False),
    ('axs.html', 'The Provenance Index', AXES, 'ax3d', 'axes',
     'status', 'args', 'cites', 8, True),
    ('rid.html', 'The Refusal Index', RIDX, 'ri3d', 'rindex',
     'index', 'refusal kind', '|R|', 5, False),
)

# THE PLATE EACH ONE IS THE SOURCE OF, under the name the tree keeps it by.
# The rename happened outside this program; the selftest pins the pairing so it
# cannot quietly stop holding.
ARCHIVED = {'ion.html': 'ions-plate.html',
            'axs.html': 'axes-plate.html',
            'rid.html': 'rindex-plate.html'}


def render(spec):
    """Build one plate in memory.  Returns (filename, page text)."""
    fn, title, body, sid, pk, xl, yl, zl, r, lab = spec
    col = (COLJS if pk != 'rindex' else
           "colour:p=>(p.y===0||p.y===7)?'--faint':'--accent'")
    script = ("scatter3d({id:'%s',points:%s,xlab:'%s',ylab:'%s',zlab:'%s',"
              "r:%s,height:470,scale:0.225,%s%s});"
              % (sid, json.dumps(PTS[pk], separators=(',', ':')), xl, yl, zl,
                 r, ("stroke:true,labels:true," if lab else ""), col))
    return fn, page(title, body, script)


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

    # THE INPUTS, pinned by md5 -- these are the bytes extracted from the
    # plates, and a plate is only reproducible if they are exactly these.
    for name, want, size in (('style.css', 'bfec0696c0e551145759a290ad5d500a', 7280),
                             ('w3d-r1.js', 'f9348be9b963d26e2c63240fc974e060', 5753),
                             ('new_pts.json', '7b827facb5d6d2dc9a0c63293034c159', 4715)):
        b = open(os.path.join(HERE, name), 'rb').read()
        chk("%s is present, %d bytes" % (name, size), len(b), size)
        chk("%s md5" % name, md5(b), want)

    # style.css CARRIES NO TRAILING NEWLINE, because page() supplies the one
    # separator and the plates have no blank line before the wrap div.
    chk("style.css ends without a newline", STYLE.endswith('\n'), False)
    chk("w3d-r1.js ends with one", W3D.endswith('\n'), True)

    # THE POINT SETS, measured off the restored file.
    chk("ions points", len(PTS['ions']), 98)
    chk("axes points", len(PTS['axes']), 14)
    chk("rindex points", len(PTS['rindex']), 42)

    # THE WHOLE CLAIM: each page is byte-identical to the plate in the tree.
    for spec in PLATES:
        fn, out = render(spec)
        arch = os.path.join(HERE, ARCHIVED[fn])
        want = open(arch, 'rb').read()
        chk("%s reproduces %s byte for byte" % (fn, ARCHIVED[fn]),
            (len(out.encode()), md5(out)), (len(want), md5(want)))

    print("build_plates selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    build()
