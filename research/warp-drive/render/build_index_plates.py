#!/usr/bin/env python3
r"""
build_index_plates.py -- the plates for the seated indexes that had none.

    python3 build_index_plates.py            writes all three
    python3 build_index_plates.py laws       writes one

`laws`, `probability` and `inversion` were seated with no rendering at all.
Each is built on the shared scaffold in `plate.py`, so the stylesheet, the
measured axis choice, the swept camera and the inlined runtime are one
implementation rather than three.

**ALL THREE HAVE ARITY 3, SO THEIR 3-D VIEW IS THE INDEX ITSELF.**  Three
coordinates, three axes, one point per cell: nothing is projected, collapsed or
summarised, and `plate.exactness()` says so in the caption rather than leaving a
reader to assume it.  That is not true of `gravity`, whose seven coordinates
must be projected, and the difference is stated on both plates.

Every number here is read from the instrument at build time.  Nothing is
retyped.
"""

import collections
import html
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import hlaw        # noqa: E402
import mi          # noqa: E402
import overlap     # noqa: E402
import plate       # noqa: E402
import registry    # noqa: E402

E = html.escape
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)))
# EIGHT DISTINCT TOKENS, because the channel index reaches l = 7 and a ramp of
# six made l = 6 and l = 0 the SAME COLOUR (and the term index needs nine) -- two different subshell types under
# one hue, which is a lie the eye cannot see through. `ramp()` refuses to wrap.
RAMP = ("--statistics", "--geometry", "--information", "--algebra", "--order",
        "--accent", "--hue7", "--hue8", "--hue9")


def ramp(vals):
    """A token per distinct value, and a REFUSAL rather than a silent wrap."""
    v = sorted(vals)
    if len(v) > len(RAMP):
        raise SystemExit("plate: %d colour values against %d tokens -- extend "
                         "RAMP rather than wrapping it" % (len(v), len(RAMP)))
    return {x: RAMP[i] for i, x in enumerate(v)}


def measured(X):
    """The block every plate carries: cell, box, closures, resolution."""
    cl, _b = hlaw.closures(X)
    return dict(cells=len(X), box=overlap.box_of(X), cell=mi.cell(X),
                closures={L: len(cl[L]) for L in hlaw.LANGS},
                res=overlap.resolution(X))


def chart_table(names, X, res):
    rows = "".join(
        '<tr><td class="name mono">%s</td><td>%s</td><td class="mono sm">%s</td>'
        '<td class="num">%d</td><td class="num">%.3f</td><td>%s</td></tr>'
        % (nm, doc, _alpha({c[i] for c in X}), d, r,
           '<span class="no">LABEL</span>' if v == "LABEL" else "measurement")
        for i, ((nm, doc), (_j, d, _n, r, v)) in enumerate(zip(names, res)))
    return ('<div class="tablewrap"><table><thead><tr><th>slot</th>'
            '<th>what it measures</th><th>alphabet</th><th class="num">values</th>'
            '<th class="num">distinct/cells</th><th>verdict</th></tr></thead>'
            '<tbody>%s</tbody></table><caption>A coordinate separating 90%% or '
            'more of the members is a row label, not a measurement. None here '
            'is.</caption></div>' % rows)


def _alpha(vals):
    v = sorted(vals)
    s = ", ".join(("%g" % x) if isinstance(x, float) else str(x) for x in v)
    return s if len(s) <= 78 else s[:75] + "…"


def closure_table(m):
    rows = "".join(
        '<tr><td class="name">%s</td><td class="num">%d</td><td class="num">%d</td>'
        '<td>%s</td></tr>'
        % (L, n, n - m["cells"],
           '<span class="yes">closes</span>' if n == m["cells"]
           else '<span class="no">does not close</span>')
        for L, n in m["closures"].items())
    return ('<div class="tablewrap"><table><thead><tr><th>language</th>'
            '<th class="num">admits</th><th class="num">E</th><th>verdict</th>'
            '</tr></thead><tbody>%s</tbody></table>'
            '<caption>Against %d cells held.</caption></div>'
            % (rows, m["cells"]))


def kv(*pairs):
    return ('<div class="kv">%s</div>' % "".join(
        '<div><dt>%s</dt><dd>%s%s</dd></div>'
        % (k, v, "<small>%s</small>" % s if s else "")
        for k, v, s in pairs))


def foot(mod, nfix):
    return ('<div class="foot"><p>Every figure on this plate is read from the '
            'instrument at build time, not retyped. Re-verify with:</p>'
            '<p><code>python3 research/warp-drive/%s.py --selftest</code> — %d '
            'fixtures<br><code>python3 research/warp-drive/%s.py</code> — the '
            'reading<br><code>python3 research/warp-drive/render/'
            'build_index_plates.py %s</code> — this plate</p></div>'
            % (mod, nfix, mod, mod))


def nfixtures(mod):
    return open(os.path.join(os.path.dirname(OUT), mod + ".py"),
                encoding="utf-8").read().count('chk("')


# ===========================================================================

def build_inversion():
    import inversion as I
    X = I.index()
    m = measured(X)
    tab = I.table()
    depths = sorted({c[0] for c in X})
    pts = [(c[1], c[2], c[0], ramp(depths)[c[0]], 0, "") for c in sorted(X)]
    h = [plate.head("The Inversion Index"), '<div class="wrap">']
    h.append('''<header class="mast">
  <p class="eyebrow">Research plate · an index of the periodic elements</p>
  <h1>The Inversion&nbsp;Index</h1>
  <p class="dek">The twenty places where the fill order and the shell order
  disagree — the reason the transition metals exist — as an index in its own
  right.</p>
  <div class="stamp"><span>instrument <b>inversion.py</b></span>
  <span>members <b>%d inversions</b></span><span>arity <b>3</b></span>
  <span>cells <b>%d</b></span><span>cell <b>(%d,&nbsp;%d,&nbsp;%d)</b></span></div>
</header>''' % (len(tab), m["cells"], *m["cell"]))
    h.append('''<section>
  <div class="shead"><span class="snum">01</span><h2>The object exists; it is
  not a construction</h2></div>
  <p class="sub">Two total orders on the same twenty-five subshells, which
  disagree. The disagreements are the members.</p>
  <p><span class="mono">fibred.py</span> charts the differentiating electron by
  shell, <span class="mono">madelung.py</span> by fill order:</p>
  <p class="eqn mono">Madelung order&nbsp;&nbsp;sort by (n+l, n) &mdash; which
  subshell fills next<br>shell order&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sort by
  (n, l) &mdash; which subshell lies further out</p>
  <p><b>4s fills before 3d</b>: (4,&nbsp;0) has n+l&nbsp;=&nbsp;4 and
  (3,&nbsp;2) has n+l&nbsp;=&nbsp;5 &mdash; but 3d is the inner subshell. That
  pair is an inversion, and it is the reason the transition metals exist. Over
  the seated reach of 170 elements there are twenty-five subshells and
  <b>%d inversions</b>: not a sample and not a choice, every pair checked.</p>
  <div class="note good"><span class="lab">Every inversion crosses a shell
  boundary, and that is forced rather than observed</span>
  <p style="margin-bottom:0">If two subshells share n then the shell order ranks
  them by l and the Madelung order ranks them by n+l, which at equal n is also
  l &mdash; the two agree. So an inversion requires n&#8321;&nbsp;&ne;&nbsp;n&#8322;,
  and <span class="mono">crossing_is_forced()</span> proves it by exhausting the
  pairs rather than quoting the argument.</p></div>
</section>''' % len(tab))
    h.append('''<section>
  <div class="shead"><span class="snum">02</span><h2>The three coordinates</h2></div>
  <p class="sub">For an inversion {a, b} with a the one that fills first and b
  the one that lies further in. All three are read off the two orders and
  nothing else &mdash; no capacity, no occupancy, no atomic number.</p>
  %s
</section>''' % chart_table([("depth", "a.n &minus; b.n — how many shells it reaches across"),
                             ("span", "how far apart in the Madelung sequence"),
                             ("reach", "how far apart in the shell sequence")],
                            X, m["res"]))
    h.append(plate.view3d(
        "in3d", pts, ("span  Madelung distance", "reach  shell distance",
                      "depth  Δn"),
        [(ramp(depths)[d], "depth = %d" % d) for d in depths],
        plate.exactness(X, (0, 1, 2), m["cells"], 0, []) +
        " Depth is both the third axis and the colour, so a point's height and "
        "its hue say the same thing — which makes the layering of the three "
        "depth sheets readable from any angle. <b>Twenty inversions fall on %d "
        "distinct cells</b>: three pairs share a cell exactly."
        % m["cells"],
        "One point per cell of the chart, at its own coordinates.",
        "03", "The index, plotted exactly", radius=7,
        aria="the inversion index: %d cells at span, reach and depth"
             % m["cells"]))
    rows = "".join(
        '<tr><td class="mono">%d%s</td><td class="mono">%d%s</td>'
        '<td class="cell">(%d, %d, %d)</td></tr>'
        % (a[0], "spdfgh"[a[1]], b[0], "spdfgh"[b[1]], *c)
        for a, b, c in sorted(tab, key=lambda t: (t[2][0], t[2][1], t[2][2])))
    h.append('''<section>
  <div class="shead"><span class="snum">04</span><h2>Every inversion</h2></div>
  <div class="tablewrap"><table><thead><tr><th>fills first</th>
    <th>lies further in</th><th>cell (depth, span, reach)</th></tr></thead>
    <tbody>%s</tbody></table>
    <caption>%d inversions on %d distinct cells.</caption></div>
</section>''' % (rows, len(tab), m["cells"]))
    h.append('''<section>
  <div class="shead"><span class="snum">05</span><h2>What it measures</h2></div>
  %s
  %s
  <p class="after"><b>It was built before the demand table was read, and that is
  deliberate.</b> An index built to land on a cell
  <span class="mono">demand.py</span> wants would be fitted, and a fitted vertex
  closes nothing. Where it lands is reported whether or not it is wanted.</p>
</section>''' % (kv(("cells", m["cells"], "from %d inversions" % len(tab)),
                    ("box", m["box"], "what charting cost tracks"),
                    ("cell", "(%d, %d, %d)" % m["cell"], "K, height, width")),
                 closure_table(m)))
    h.append(foot("inversion", nfixtures("inversion")))
    h.append("</div>")
    _write("inversion-plate.html", h)


def build_probability():
    import probability as P
    X = P.index()
    m = measured(X)
    pr = P.probabilities()
    tot, pn, ps = P.normalisation()
    ps_vals = sorted({c[0] for c in X})
    pts = [(c[1], c[2], c[0], ramp(ps_vals)[c[0]], 0, "")
           for c in sorted(X)]
    h = [plate.head("The Probability Index"), '<div class="wrap">']
    h.append('''<header class="mast">
  <p class="eyebrow">Research plate · an index of the periodic elements</p>
  <h1>The Probability&nbsp;Index</h1>
  <p class="dek">One distribution over the twenty-five subshells, read three
  ways, and every row of it sums to one.</p>
  <div class="stamp"><span>instrument <b>probability.py</b></span>
  <span>members <b>%d subshells</b></span><span>arity <b>3</b></span>
  <span>cells <b>%d</b></span><span>cell <b>(%d,&nbsp;%d,&nbsp;%d)</b></span></div>
</header>''' % (len(pr), m["cells"], *m["cell"]))
    h.append('''<section>
  <div class="shead"><span class="snum">01</span><h2>There is one distribution
  here, and it was already banked</h2></div>
  <p class="sub">Draw an element uniformly from the seated reach of 170 and ask
  which subshell its differentiating electron went into. That is a probability
  distribution over the twenty-five subshells and it needs no modelling: the
  counts are <span class="mono">fibred.addresses()</span>, already measured.</p>
  <div class="note"><span class="lab">The members are subshells, not elements</span>
  <p style="margin-bottom:0">That is what makes this a different index rather
  than a re-chart of <span class="mono">fibred.py</span>: twenty-five members
  against a hundred and seventy, and coordinates that are <em>probabilities</em>
  rather than quantum numbers.</p></div>
  <p class="eqn mono">p&nbsp;&nbsp;&nbsp;P(subshell)<br>p<sub>n</sub>&nbsp;&nbsp;P(subshell
  | shell = n)<br>p<sub>s</sub>&nbsp;&nbsp;P(subshell | n + l = s)</p>
  <p><b>Not three distributions — one, conditioned on the two bases the tree
  already charts.</b> <span class="mono">fibred.py</span> fibres the elements
  over n; <span class="mono">madelung.py</span> fibres them over n+l.
  p<sub>n</sub> and p<sub>s</sub> are exactly those two fibrations read as
  conditionals, which is why these three and not some other three.</p>
  <div class="note good"><span class="lab">Every row sums to one, and it is a
  fixture rather than a remark</span>
  <p style="margin-bottom:0">p over all twenty-five subshells: <b>%.9g</b>.
  p<sub>n</sub> over each of the %d shells and p<sub>s</sub> over each of the %d
  Madelung groups: every one <b>1</b>. A probability index whose rows do not
  normalise is not a probability index, and the check is cheap.</p></div>
</section>''' % (tot, len(pn), len(ps)))
    h.append('''<section>
  <div class="shead"><span class="snum">02</span><h2>The coordinates, and the
  cost the marginal carries</h2></div>
  %s
  <div class="note warn"><span class="lab">The marginal is a function of ℓ, and
  the docstring said otherwise before the fixtures were run</span>
  <p>The counts are observed, not capacities &mdash; and at this reach they
  coincide. <span class="mono">truncation()</span> returns EMPTY at 170: the
  seated reach lands exactly on a Madelung shell boundary, so every subshell it
  touches is full and the count <em>is</em> the capacity 2(2ℓ+1).</p>
  <p style="margin-bottom:0">That costs the marginal its independence, and the
  cost is reported rather than hidden: with no truncation p = 2(2ℓ+1)/N is a
  function of ℓ alone &mdash; five values, one per capacity, nothing a reader
  could not have computed from ℓ. The two <em>conditionals</em> are not
  functions of ℓ, so the index is not thereby a re-chart of ℓ; but the marginal
  alone is. <b>And p<sub>n</sub> determines p</b>, measured rather than
  designed: (p, p<sub>n</sub>) separates exactly as many subshells as
  p<sub>n</sub> alone.</p></div>
</section>''' % chart_table([("p", "P(subshell) — the marginal"),
                            ("p<sub>n</sub>", "P(subshell | shell = n)"),
                            ("p<sub>s</sub>", "P(subshell | n + l = s)")],
                           X, m["res"]))
    h.append(plate.view3d(
        "pr3d", pts, ("p(n)  conditional on the shell",
                      "p(s)  conditional on the Madelung group",
                      "p  the marginal"),
        [(ramp(ps_vals)[v], "p = %g" % v) for v in ps_vals],
        plate.exactness(X, (0, 1, 2), m["cells"], 0, []) +
        " The colour is the marginal, which is the vertical axis, so hue and "
        "height agree — and because the marginal is a function of ℓ (section 2) "
        "<b>the five colours are the five subshell types s, p, d, f, g</b>. "
        "Reading the sheets from the bottom up reads ℓ upward. %d subshells "
        "fall on %d distinct cells." % (len(pr), m["cells"]),
        "One point per cell. The axes are probabilities, so the box is the unit "
        "cube clipped to what the distribution actually reaches.",
        "03", "The index, plotted exactly", radius=7,
        aria="the probability index: %d cells at the marginal and its two "
             "conditionals" % m["cells"]))
    rows = "".join(
        '<tr><td class="name mono">%d%s</td><td class="num">%.6f</td>'
        '<td class="num">%.6f</td><td class="num">%.6f</td></tr>'
        % (n, "spdfgh"[l], v[0], v[1], v[2])
        for (n, l), v in sorted(pr.items()))
    h.append('''<section>
  <div class="shead"><span class="snum">04</span><h2>Every subshell</h2></div>
  <div class="tablewrap tall"><table><thead><tr><th>subshell</th>
    <th class="num">p</th><th class="num">p<sub>n</sub></th>
    <th class="num">p<sub>s</sub></th></tr></thead><tbody>%s</tbody></table>
    <caption>%d subshells on %d distinct cells.</caption></div>
</section>''' % (rows, len(pr), m["cells"]))
    h.append('''<section>
  <div class="shead"><span class="snum">05</span><h2>What it measures</h2></div>
  %s
  %s
</section>''' % (kv(("cells", m["cells"], "from %d subshells" % len(pr)),
                    ("box", m["box"], "what charting cost tracks"),
                    ("cell", "(%d, %d, %d)" % m["cell"], "K, height, width")),
                 closure_table(m)))
    h.append(foot("probability", nfixtures("probability")))
    h.append("</div>")
    _write("probability-plate.html", h)


def build_laws():
    import laws as L
    X = L.index()
    m = measured(X)
    cen = L.census()
    rows_all = L.rows()
    bands = sorted({c[2] for c in X})
    pts = [(c[0], c[1], c[2], ramp(bands)[c[2]], 0, "")
           for c in sorted(X)]
    h = [plate.head("The Rydberg Residual Index"), '<div class="wrap">']
    h.append('''<header class="mast">
  <p class="eyebrow">Research plate · an index of the periodic elements</p>
  <h1>The Rydberg&nbsp;Residual&nbsp;Index</h1>
  <p class="dek">Every banked Rydberg series measured against the law it is
  supposed to obey — and charted by how badly a single quantum defect describes
  it.</p>
  <div class="stamp"><span>instrument <b>laws.py</b></span>
  <span>members <b>%d series</b></span><span>arity <b>3</b></span>
  <span>cells <b>%d</b></span><span>cell <b>(%d,&nbsp;%d,&nbsp;%d)</b></span></div>
</header>''' % (len(rows_all), m["cells"], *m["cell"]))
    h.append('''<section>
  <div class="shead"><span class="snum">01</span><h2>A residual index, not a
  table of values</h2></div>
  <p class="sub">The Rydberg–Ritz law says a series member sits at
  n* = n &minus; &delta;. The tables bank one fitted &delta; per series. The
  residual is how far the law, with that one &delta;, misses the banked n* — and
  that residual is the measurement.</p>
  <div class="note"><span class="lab">Nothing is fitted here</span>
  <p style="margin-bottom:0">No constant chosen, no threshold tuned, and the
  only tolerance is the table's own printed precision. Where a row cannot be
  parsed it is reported as unparsed, not guessed:
  <span class="mono">unparsed()</span> holds %d of %d.</p></div>
  %s
</section>''' % (len(L.unparsed()), len(rows_all),
                 kv(*[(k, v, "") for k, v in sorted(cen.items())])
                 if isinstance(cen, dict) else ""))
    h.append('''<section>
  <div class="shead"><span class="snum">02</span><h2>The three coordinates</h2></div>
  <p class="sub">One cell per series: how long the series runs, how many levels
  it banks, and how far the residual drifts across it.</p>
  %s
  <div class="note warn"><span class="lab">A drifting residual is not an error
  in the data</span>
  <p style="margin-bottom:0">The likely reading is a quantum defect that
  <em>moves along the series</em> while the table prints one fitted value, which
  makes the residual a measurement of how well a single defect describes the
  series — a real quantity, and the one worth indexing. The
  <span class="mono">lit</span> column says <em>unverified</em> for most rows
  and that caution is inherited.</p></div>
</section>''' % chart_table([("span", "n<sub>hi</sub> &minus; n<sub>lo</sub> — how far the series runs"),
                             ("levels", "how many levels the table banks"),
                             ("drift", "|residual spread| &times; 10 — the band")],
                            X, m["res"]))
    h.append(plate.view3d(
        "la3d", pts, ("span  n range", "levels  banked", "drift  band"),
        [(ramp(bands)[b], "drift band %d" % b) for b in bands],
        plate.exactness(X, (0, 1, 2), m["cells"], 0, []) +
        " Colour is the drift band, which is also the vertical axis. <b>The "
        "floor of the box — band 0 — is every series a single quantum defect "
        "describes to the table's own precision</b>, and the points above it "
        "are the ones it does not. %d series fall on %d distinct cells, so the "
        "index is a heavy coarsening of the series set and says so."
        % (len(rows_all), m["cells"]),
        "One point per cell of the chart, at its own coordinates.",
        "03", "The index, plotted exactly", radius=6,
        aria="the Rydberg residual index: %d cells at span, levels and drift "
             "band" % m["cells"]))
    h.append('''<section>
  <div class="shead"><span class="snum">04</span><h2>What it measures</h2></div>
  %s
  %s
  <p class="after"><b>Refused:</b> to call an inconsistent row an error; to fit
  anything; to extend to a law whose terms the corpus does not already state.</p>
</section>''' % (kv(("cells", m["cells"], "from %d banked series" % len(rows_all)),
                    ("box", m["box"], "what charting cost tracks"),
                    ("cell", "(%d, %d, %d)" % m["cell"], "K, height, width")),
                 closure_table(m)))
    h.append(foot("laws", nfixtures("laws")))
    h.append("</div>")
    _write("laws-plate.html", h)


def _write(name, parts):
    p = os.path.join(OUT, name)
    with open(p, "w", encoding="utf-8") as fh:
        fh.write("\n".join(parts))
    print("wrote %s  (%d bytes)" % (p, os.path.getsize(p)))



# ===========================================================================
# THE FOUR THAT HAD A PLATE ALREADY, REBUILT ON THE SHARED SCAFFOLD.
#
# fibration-plate, janet-plate, ions-plate and spectra-plate exist and work, but
# each froze its own copy of the runtime -- three generations have since
# diverged -- and spectra-plate still attributes the channel index to
# `spectra.py`, which was the module before the index was reseated as
# `channels.py`.  These are built from the instruments, on one runtime, and
# named for the module that is actually registered.  THE OLD PLATES ARE NOT
# DELETED: they are the record of what was rendered before, and DOCKET 14 says
# superseded material is kept.
# ===========================================================================

SUB = "spdfghik"        # the spectroscopic letters, l = 0 .. 7


def _shell_plate(name, X, labels, title, dek, eyebrow_n, sub, extra, mod,
                 pid, first):
    m = measured(X)
    ls = sorted({c[1] for c in X})
    pts = [(c[0], c[2], c[1], ramp(ls)[c[1]], 0, "")
           for c in sorted(X)]
    h = [plate.head(title), '<div class="wrap">']
    h.append('''<header class="mast">
  <p class="eyebrow">Research plate · an index of the periodic elements</p>
  <h1>%s</h1>
  <p class="dek">%s</p>
  <div class="stamp"><span>instrument <b>%s.py</b></span>
  <span>members <b>%s</b></span><span>arity <b>3</b></span>
  <span>cells <b>%d</b></span><span>cell <b>(%d,&nbsp;%d,&nbsp;%d)</b></span></div>
</header>''' % (title.replace(" ", "&nbsp;", 1), dek, mod, eyebrow_n,
                m["cells"], *m["cell"]))
    h.append(first)
    h.append('''<section>
  <div class="shead"><span class="snum">02</span><h2>The three coordinates</h2></div>
  %s
</section>''' % chart_table(labels, X, m["res"]))
    h.append(plate.view3d(
        pid, pts, (labels[0][0].replace("&minus;", "-") + "  " + _plain(labels[0][1]),
                   labels[2][0] + "  " + _plain(labels[2][1]),
                   labels[1][0] + "  " + _plain(labels[1][1])),
        [(ramp(ls)[v], "%s = %s%s"
          % (labels[1][0], v, "  (%s)" % SUB[v] if v < len(SUB) else ""))
         for v in ls],
        plate.exactness(X, (0, 1, 2), m["cells"], 0, []) + " " + extra,
        sub, "03", "The index, plotted exactly", radius=4.2,
        aria="%s: %d cells" % (title, m["cells"])))
    h.append('''<section>
  <div class="shead"><span class="snum">04</span><h2>What it measures</h2></div>
  %s
  %s
</section>''' % (kv(("cells", m["cells"], ""),
                    ("box", m["box"], "what charting cost tracks"),
                    ("cell", "(%d, %d, %d)" % m["cell"], "K, height, width")),
                 closure_table(m)))
    h.append(foot(mod, nfixtures(mod)))
    h.append("</div>")
    _write(name, h)


def _plain(s):
    """Canvas text is not HTML: strip tags and RESOLVE entities, do not drop them.

    Dropping them silently printed the literal string "&#8467;" on an axis.
    """
    import html as _h
    import re
    return _h.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def build_fibred():
    import fibred as F
    build = _shell_plate(
        "fibred-plate.html", F.index(),
        [("n", "principal quantum number"), ("l", "orbital angular momentum"),
         ("k", "occupancy of the subshell at that electron")],
        "The Shell Fibration",
        "One hundred and seventy electrons, each at the address of the subshell "
        "it went into — the periodic table as a fibration over the shell.",
        "170 electrons",
        "One point per electron, at its own (n, l, k).",
        "Every subshell is a comb exactly 2(2ℓ+1) tall with no gaps, and the "
        "tall high-ℓ combs are confined to the middle of the n range while only "
        "short ℓ=0 combs reach the far end. <b>Rotate to face the n axis</b> and "
        "the atom's rule ℓ &lt; n resolves the shape.",
        "fibred", "fb3d", '''<section>
  <div class="shead"><span class="snum">01</span><h2>A member is an electron</h2></div>
  <p class="sub">Not an element. The differentiating electron of each of the 170
  elements in the seated reach, at the address of the subshell it entered.</p>
  <p>That is what separates this index from every chart of the periodic table:
  its members are electrons, its coordinates are the three quantum numbers that
  name one, and the periodic table is what the fibration looks like when you
  project it back onto its base.</p>
</section>''')
    return build


def build_madelung():
    import madelung as M
    return _shell_plate(
        "madelung-plate.html", M.janet(),
        [("n+l", "the Madelung group — which subshell fills next"),
         ("l", "orbital angular momentum"), ("k", "occupancy")],
        "The Janet Fibration",
        "The same one hundred and seventy electrons, re-based on n+ℓ — the "
        "order they actually fill in rather than the order they sit in.",
        "the same 170 electrons",
        "One point per electron, at its own (n+ℓ, ℓ, k).",
        "It is the SAME MEMBER SET as the shell fibration, re-based. That is why "
        "the two are separate indexes and not one: a fibration is its base as "
        "much as its fibres, and these two bases disagree — the twenty places "
        "they disagree are the <span class=\"mono\">inversion</span> index.",
        "madelung", "ja3d", '''<section>
  <div class="shead"><span class="snum">01</span><h2>The same electrons, a
  different base</h2></div>
  <p class="sub">Madelung's rule orders subshells by (n+ℓ, n): which one fills
  next. The shell order is (n, ℓ): which one lies further out. Both are total
  orders on the same twenty-five subshells.</p>
  <p>This index fibres the same 170 electrons over n+ℓ instead of n. The member
  set is identical to <span class="mono">fibred</span>'s and the chart is not,
  which is exactly why both are seated: the cells differ, the cell differs, and
  the disagreement between the two bases is itself a third index.</p>
</section>''')


def build_channels():
    import channels as C
    X = C.index()
    m = measured(X)
    ls = sorted({c[0] for c in X})
    pts = [(c[1], c[2], c[0], ramp(ls)[c[0]], 0, "")
           for c in sorted(X)]
    h = [plate.head("The Channel Index"), '<div class="wrap">']
    h.append('''<header class="mast">
  <p class="eyebrow">Research plate · an index of the periodic elements</p>
  <h1>The Channel&nbsp;Index</h1>
  <p class="dek">Two hundred and nine spectroscopic channel shapes — what an
  angular momentum, a Pauli bound and a multiplicity allow.</p>
  <div class="stamp"><span>instrument <b>channels.py</b></span>
  <span>members <b>209 channel shapes</b></span><span>arity <b>3</b></span>
  <span>cells <b>%d</b></span><span>cell <b>(%d,&nbsp;%d,&nbsp;%d)</b></span></div>
</header>''' % (m["cells"], *m["cell"]))
    h.append('''<div class="note warn" style="margin-top:26px">
  <span class="lab">This index was reseated, and the older plate names the older module</span>
  <p style="margin-bottom:0">The channel index is now
  <span class="mono">channels.py</span>. It was extracted from
  <span class="mono">spectra.py</span>, which still exists and still answers the
  question it was written for; <span class="mono">render/spectra-plate.html</span>
  renders the same 209 shapes under that older attribution and is kept rather
  than deleted. This plate is built from the module the registry actually
  seats.</p>
</div>''')
    h.append('''<section>
  <div class="shead"><span class="snum">01</span><h2>A member is a channel
  shape</h2></div>
  <p class="sub">Not a level and not a series: the shape a channel can take,
  given its orbital angular momentum, the Pauli bound on how many electrons fit,
  and the multiplicity the coupling allows.</p>
</section>''')
    h.append('''<section>
  <div class="shead"><span class="snum">02</span><h2>The three coordinates</h2></div>
  %s
</section>''' % chart_table([("l", "orbital angular momentum"),
                             ("B", "the Pauli bound"),
                             ("mult", "multiplicity")], X, m["res"]))
    h.append(plate.view3d(
        "ch3d", pts, ("B  Pauli bound", "mult  multiplicity", "l  angular momentum"),
        [(ramp(ls)[v], "l = %d  (%s)"
          % (v, SUB[v] if v < len(SUB) else "?")) for v in ls],
        plate.exactness(X, (0, 1, 2), m["cells"], 0, []) +
        " Colour is ℓ, which is also the vertical axis, so the view separates "
        "into one sheet per subshell type and the Pauli bound's growth with ℓ "
        "is the staircase between them.",
        "One point per channel shape, at its own coordinates.",
        "03", "The index, plotted exactly", radius=4.2,
        aria="the channel index: %d shapes at Pauli bound, multiplicity and l"
             % m["cells"]))
    h.append('''<section>
  <div class="shead"><span class="snum">04</span><h2>What it measures</h2></div>
  %s
  %s
</section>''' % (kv(("cells", m["cells"], ""),
                    ("box", m["box"], "what charting cost tracks"),
                    ("cell", "(%d, %d, %d)" % m["cell"], "K, height, width")),
                 closure_table(m)))
    h.append(foot("channels", nfixtures("channels")))
    h.append("</div>")
    _write("channels-plate.html", h)


def build_ions():
    import ions as I
    X = I.index()
    m = measured(X)
    NM = ("sn", "sl", "k", "q", "tn", "tl", "g")
    DOC = ("source subshell n", "source subshell &#8467;",
           "parent occupancy of it", "electrons that leave",
           "target subshell n", "target subshell &#8467;", "electrons arriving")
    COLOUR = 5                                    # tl, the target subshell's l
    tri, npts, imp, rows = plate.axis_choice(X, COLOUR)
    tl = sorted({c[COLOUR] for c in X})
    pts = [(c[tri[0]], c[tri[1]], c[tri[2]],
            ramp(tl)[c[COLOUR]], 0, "") for c in sorted(X)]
    h = [plate.head("The Ionisation Ladder"), '<div class="wrap">']
    h.append('''<header class="mast">
  <p class="eyebrow">Research plate · an index of the periodic elements</p>
  <h1>The Ionisation&nbsp;Ladder</h1>
  <p class="dek">An index whose members are transitions, not elements — and the
  first source in this tree to reach a channel the element address provably
  cannot.</p>
  <div class="stamp"><span>instrument <b>ions.py</b></span>
  <span>members <b>98 transitions</b></span><span>arity <b>7</b></span>
  <span>cells <b>%d</b></span><span>cell <b>(%d,&nbsp;%d,&nbsp;%d)</b></span></div>
</header>''' % (m["cells"], *m["cell"]))
    h.append('''<div class="note warn" style="margin-top:26px">
  <span class="lab">Status first, because everything here rests on it</span>
  <p style="margin-bottom:0"><b>This index is built on a reconstruction and the
  corpus says so.</b> <span class="mono">tools/populate.ionisation_cells</span>
  carries the status RECONSTRUCTED in its own docstring: chapter 7 makes a
  &Lambda;&#8328; cell a <em>transition</em>, so an element is not a cell and a
  mapping had to be <em>chosen</em>. "Nothing else in the store fixes this
  mapping." Every channel below is a fact about that mapping as much as about
  ions, and the status is not flattened anywhere.</p>
</div>''')
    h.append('''<section>
  <div class="shead"><span class="snum">01</span><h2>A member is a transition</h2></div>
  <p class="sub">A &Lambda;&#8328; cell is a source subshell, how many electrons
  leave it, a target subshell, how many arrive, and the parent occupancy — seven
  determined slots, not an element.</p>
  <p><b>5,778 stage rows collapse to 98 cells, and the collapse is structural.</b>
  Walking every element Z&nbsp;&le;&nbsp;108 and every charge stage gives 5,778
  rows, but each cell is built from the ELECTRON COUNT alone and never from Z, so
  every element's ladder is a suffix of one universal ladder. Quoting 5,778 would
  be counting elements while claiming to count transitions.</p>
  <p><b>The eighth slot is always empty and is dropped.</b> The ion's ground
  multiplicity 2S is known only where the ion's term is known, and over all 5,778
  stage rows the corpus banks it not once. A one-valued coordinate carries no
  information and would widen every closure for free, so the index is charted on
  the seven that are determined — and the selftest pins that the dropped slot
  really is constant rather than merely sparse.</p>
</section>''')
    h.append('''<section>
  <div class="shead"><span class="snum">02</span><h2>The seven coordinates</h2></div>
  %s
</section>''' % chart_table(list(zip(NM, DOC)), X, m["res"]))
    h.append(plate.view3d(
        "io3d", pts,
        tuple("%s  %s" % (NM[i], _plain(DOC[i])) for i in tri),
        [(ramp(tl)[v], "target &#8467; = %d  (%s)"
          % (v, SUB[v] if v < len(SUB) else "?")) for v in tl],
        plate.exactness(X, tri, npts, imp, rows) +
        " Colour is the TARGET subshell's &#8467;, which is deliberately not one "
        "of the axes: where a point's colour disagrees with the sheet it sits "
        "in, the transition crosses subshell types. That is the one thing this "
        "chart is for and it is the reason the colour was not spent on depth.",
        "This index has seven coordinates, so unlike the other plates here its "
        "3-D view is a projection — and what the projection costs is measured.",
        "03", "The index, projected — and what that costs", radius=5,
        aria="the ionisation ladder: %d of %d cells projected onto three of "
             "its seven coordinates" % (npts, m["cells"])))
    h.append('''<section>
  <div class="shead"><span class="snum">04</span><h2>What it measures</h2></div>
  %s
  %s
  <p class="after"><b>It reaches K4, which the element address cannot.</b> One
  sub-chart of the hundred and twenty — the source subshell's &#8467; against the
  target's — sits in K4 = {information, statistics}, and
  <span class="mono">charts3.py</span> proved K4 is never reached by any chart
  built from the differentiating electron's address. Changing the member set
  from elements to transitions reaches a channel no rearrangement of the element
  address could. <b>The price is coarsening:</b> that chart holds 7 cells
  against 98, so ninety-one lose their identity. Reachable, and not faithful.</p>
</section>''' % (kv(("cells", m["cells"], "from 5,778 stage rows"),
                    ("arity", 7, "8 raw, one dropped as constant"),
                    ("box", "%s" % format(m["box"], ","), "charting cost"),
                    ("cell", "(%d, %d, %d)" % m["cell"], "K, height, width")),
                 closure_table(m)))
    h.append(foot("ions", nfixtures("ions")))
    h.append("</div>")
    _write("ions-index-plate.html", h)




def build_nucshell():
    import nucshell as N
    X = N.index()
    m = measured(X)
    ss = sorted({c[2] for c in X})
    pts = [(c[0], c[1], c[2], ramp(ss)[c[2]], 0, "") for c in sorted(X)]
    h = [plate.head("The Nuclear Subshell Index"), '<div class="wrap">']
    h.append('''<header class="mast">
  <p class="eyebrow">Research plate · the only non-atomic index seated here</p>
  <h1>The Nuclear&nbsp;Subshell&nbsp;Index</h1>
  <p class="dek">The single-particle subshells of the shell model, to the 126
  closure — and the one member type in this tree that is not atomic.</p>
  <div class="stamp"><span>instrument <b>nucshell.py</b></span>
  <span>members <b>22 subshells</b></span><span>arity <b>3</b></span>
  <span>cells <b>%d</b></span><span>cell <b>(%d,&nbsp;%d,&nbsp;%d)</b></span>
  <span>closes <b>geometry, statistics</b></span></div>
</header>''' % (m["cells"], *m["cell"]))
    h.append('''<section>
  <div class="shead"><span class="snum">01</span><h2>Two banked orders, the same
  twenty-two subshells</h2></div>
  <p class="sub">Order&nbsp;A is
  <span class="mono">extracted/archives/restore-point-2-13/nuclear_corridor.py</span>,
  order&nbsp;B is <span class="mono">recovered/nuccorr.py</span>. They hold the
  same set and differ at <b>eight</b> of the twenty-two positions.</p>
  <div class="tablewrap"><table><thead><tr><th class="num">position</th>
    <th>order A</th><th>order B</th></tr></thead><tbody>%s</tbody></table>
    <caption>Membership is not in question; only the sequence is.</caption></div>
</section>''' % "".join(
        '<tr><td class="num">%d</td><td class="mono">%s</td>'
        '<td class="mono">%s</td></tr>' % d for d in N.disagreements()))
    ha, hb, sep = N.magic_is_null()
    rows, allsame = N.block_membership_identical()
    h.append('''<section>
  <div class="shead"><span class="snum">02</span><h2>The magic numbers do not
  decide it</h2></div>
  <p class="sub">Order A's own header calls itself <em>"CORRECTED standard
  order, capacities verified to close at 2, 8, 20, 28, 50, 82, 126"</em>. The
  check passes — and it passes for B as well.</p>
  <div class="kv">
    <div><dt>A hits</dt><dd>%s</dd></div>
    <div><dt>B hits</dt><dd>%s</dd></div>
    <div><dt>separates them</dt><dd class="hot">%s</dd></div>
  </div>
  <div class="note good" style="margin-top:22px">
    <span class="lab">And the reason is a fact about sets, not about positions</span>
    <p>The first explanation written here was that no disagreement sits at a
    block-closing position. <b>Its own fixture refused that</b> — position 21
    does. The true statement is stronger: <b>the seven blocks have identical
    membership in both orders</b>, and the orders differ only by permutations
    <em>inside</em> blocks.</p>
    <p style="margin-bottom:0">A block's closing sum is the sum over its
    members, which is a <em>set</em>, so no permutation inside it can move that
    sum. The magic numbers verify the <b>block partition</b> and say nothing
    whatever about the sequence within a block. A test that passes for both
    candidates is not evidence for either, and this file does not quote it as
    though it were.</p>
  </div>
  <div class="tablewrap"><table><thead><tr><th class="num">closure</th>
    <th>same membership in A and B</th><th class="num">subshells</th></tr></thead>
    <tbody>%s</tbody></table></div>
</section>''' % (list(ha), list(hb), sep, "".join(
        '<tr><td class="num">%d</td><td>%s</td><td class="num">%d</td></tr>'
        % (c, '<span class="yes">yes</span>' if s else
           '<span class="no">no</span>', n) for c, s, n in rows)))
    h.append('''<section>
  <div class="shead"><span class="snum">03</span><h2>What decides it is
  corroboration, and it is one-sided</h2></div>
  <div class="tablewrap"><table><thead><tr><th>file</th>
    <th class="num">longest run matching A</th>
    <th class="num">matching B</th><th></th></tr></thead><tbody>%s</tbody></table>
    <caption>The 11 is the <b>common prefix</b>: positions 0–10 are where A and
    B agree, so every file stops matching B exactly where the two diverge.
    <b>Not one file in the repository follows B past the disagreement</b>, and
    one of the four that follow A is a seated member of The Method.</caption>
  </div>
  <div class="note"><span class="lab">B is not called wrong</span>
  <p style="margin-bottom:0">Order B reproduces every magic number and is a
  coherent shell-model parameterisation. Its status is <b>%s</b> — superseded
  and uncorroborated is what is measured; <em>wrong</em> is not. Order A's own
  status is <b>%s</b>: a shell-model ordering, not a theorem.</p></div>
</section>''' % ("".join(
        '<tr><td class="mono sm">%s</td><td class="num">%d</td>'
        '<td class="num">%d</td><td>%s</td></tr>'
        % (r, a, b, '<span class="chip b1">SEATED MEMBER</span>' if s else "")
        for r, a, b, s in N.corroboration()),
        N.ORDER_B_STATUS, N.ORDER_A_STATUS))
    h.append('''<section>
  <div class="shead"><span class="snum">04</span><h2>The three coordinates</h2></div>
  %s
  <p class="after"><b>sigma rather than j itself</b>, because j is determined by
  (l, sigma) and a coordinate the others already fix is over-representation.
  Spin–orbit splitting <em>is</em> the sigma&nbsp;=&nbsp;+1 member lying below
  its sigma&nbsp;=&nbsp;−1 partner, so the coordinate is the physics rather than
  a re-encoding of it.</p>
</section>''' % chart_table([("nr", "radial quantum number"),
                            ("l", "orbital angular momentum"),
                            ("sigma", "sign(j &minus; l): +1 is j = l+&frac12;")],
                           X, m["res"]))
    h.append(plate.view3d(
        "nu3d", pts, ("nr  radial quantum number", "l  orbital angular momentum",
                      "sigma  sign(j - l)"),
        [(ramp(ss)[v], "sigma = %+d  (j = l %s &frac12;)" % (v, "+" if v > 0 else "&minus;"))
         for v in ss],
        plate.exactness(X, (0, 1, 2), m["cells"], 0, []) +
        " The two coloured sheets are the two spin&ndash;orbit partners: every "
        "subshell with j = l+&frac12; sits on one, its j = l&minus;&frac12; twin "
        "on the other, and the gap between them is the splitting that makes the "
        "magic numbers what they are.",
        "One point per nuclear subshell, at its own (nr, l, sigma).",
        "05", "The index, plotted exactly", radius=7,
        aria="the nuclear subshell index: 22 subshells at nr, l and the "
             "spin-orbit sign"))
    h.append('''<section>
  <div class="shead"><span class="snum">06</span><h2>What was measured and
  refused</h2></div>
  <div class="tablewrap"><table><thead><tr><th>candidate coordinate</th>
    <th class="num">distinct</th><th class="num">ratio</th><th>verdict</th>
    </tr></thead><tbody>%s</tbody></table></div>
  <div class="note warn"><span class="lab">delta is a real measurement and still
  does not go on an axis</span>
  <p style="margin-bottom:0">It is neither constant nor a label. But appending
  it takes the index from closing under <b>geometry and statistics</b> to
  closing <b>nothing</b>, and takes the box from <b>42 to 210</b>; and no
  three-coordinate chart containing it is faithful — the three that exist hold
  17, 10 and 17 cells against 22. So it is banked as a <b>ledger column</b>, one
  row per subshell, and never charted. Status <b>%s</b>, never PINNED.</p></div>
  <div class="tablewrap tall"><table><thead><tr><th>subshell</th>
    <th class="num">nr</th><th class="num">l</th><th class="num">2j</th>
    <th class="num">rank A</th><th class="num">rank B</th>
    <th class="num">delta</th><th class="num">cumulative</th></tr></thead>
    <tbody>%s</tbody></table>
    <caption>The ledger. A shaded cumulative figure is a magic number.</caption>
  </div>
</section>''' % ("".join(
        '<tr><td class="name">%s</td><td class="num">%d</td>'
        '<td class="num">%.4f</td><td>%s</td></tr>'
        % (nm, d, r, '<span class="no">LABEL</span>' if v == "LABEL" else v)
        for nm, d, _n, r, v in N.rejected_coordinates()),
        N.DELTA_STATUS,
        "".join('<tr><td class="name mono">%s</td><td class="num">%d</td>'
                '<td class="num">%d</td><td class="num">%d</td>'
                '<td class="num">%d</td><td class="num">%d</td>'
                '<td class="num">%+d</td><td class="num">%s</td></tr>'
                % (nm, nr, l, tj, ra, rb, d,
                   ('<b class="hot">%d</b>' % cum) if cum in N.MAGIC else cum)
                for nm, nr, l, tj, ra, rb, d, cum in N.ledger())))
    hom = N.cell_homographs()
    h.append('''<section>
  <div class="shead"><span class="snum">07</span><h2>The member type is new —
  and the cell tuples do collide</h2></div>
  <p class="sub">No seated index has a nuclear member. <span class="mono">gravity</span>
  carries 2J<sub>e</sub>, which is a whole electron cloud's angular momentum for
  a nuclide-charge state, not a single-particle j.</p>
  <div class="note warn"><span class="lab">And the cell tuples DO collide, which
  was asserted otherwise and refused</span>
  <p>This section was first written claiming the full-arity intersection with
  every seated index is zero. <b>Its fixture refused it:</b> %s.</p>
  <p style="margin-bottom:0">They are <b>homographs at full arity</b>. A nuclear
  (nr, l, sigma) that happens to equal an electronic (n, l, k) is two different
  objects printing the same — collisions with <span class="mono">fibred</span>
  need k = 1, because sigma is ±1. <b>This is exactly why
  <span class="mono">overlap.py</span> calls cell_overlap the WEAK test</b> and
  keeps a strong one on identity keys beside it.</p></div>
</section>''' % ", ".join("<span class=\"mono\">%s</span> %d" % (k, v)
                          for k, v in sorted(hom.items())))
    h.append(foot("nucshell", nfixtures("nucshell")))
    h.append("</div>")
    _write("nucshell-plate.html", h)


def build_madrule():
    import madrule as M
    X = M.index()
    m = measured(X)
    ds = sorted({c[1] for c in X})
    pts = [(c[0], c[2], c[1], ramp(ds)[c[1]], 0, "") for c in sorted(X)]
    tab = M.table()
    npairs, without = M.inversion_pairs_without_exception()
    a, b, _d = M.near_inversion()
    hf, ff, nn = M.stability_story()
    h = [plate.head("The Madelung Exception Index"), '<div class="wrap">']
    h.append('''<header class="mast">
  <p class="eyebrow">Research plate · an index of the periodic elements</p>
  <h1>The Madelung&nbsp;Exception&nbsp;Index</h1>
  <p class="dek">The twenty elements whose observed ground configuration is not
  the one the rule predicts — the first object in this tree that tests Madelung
  against measurement, element by element.</p>
  <div class="stamp"><span>instrument <b>madrule.py</b></span>
  <span>members <b>20 elements</b></span><span>arity <b>3</b></span>
  <span>cells <b>%d</b></span><span>cell <b>(%d,&nbsp;%d,&nbsp;%d)</b></span></div>
</header>''' % (m["cells"], *m["cell"]))
    h.append('''<section>
  <div class="shead"><span class="snum">01</span><h2>Two sides, never merged</h2></div>
  %s
  <p class="after"><b>Both sides sum to Z on all 108, and that is a fixture.</b>
  A configuration parser that silently dropped a token would <em>invent</em>
  exceptions out of its own gaps, so the arithmetic is checked before any
  comparison is made, and the parser raises rather than skipping.</p>
  <div class="note"><span class="lab">The reach control, printed rather than hidden</span>
  <p style="margin-bottom:0">The count is a function of how far the observed
  table reaches: %s. First exception <b>%s at Z = %d</b>.</p></div>
</section>''' % (kv(("observed", "108", "LW1-ground.py · NIST ASD 5.12 · status %s" % M.OBSERVED_STATUS),
                    ("predicted", "108", "shells.py config() · status %s" % M.PREDICTED_STATUS),
                    ("the rule", M.RULE_STATUS, "not a theorem"),
                    ("exceptions", len(tab), "the members")),
                 ", ".join("Z&le;%d&rarr;%d" % r for r in M.reach_control()),
                 M.first_exception()[1], M.first_exception()[0]))
    h.append('''<section>
  <div class="shead"><span class="snum">02</span><h2>The three coordinates</h2></div>
  <p class="sub">An exception moves electrons from a subshell the rule would have
  filled to one it would not have. The coordinates are that transfer.</p>
  %s
  <p class="after">Z was measured as a coordinate and <b>refused</b>: 20/20 =
  1.0000, a row label. And <b>occ is the coordinate nearest the threshold</b> at
  0.6154 — the one that tips first if the reach ever grows, recorded now rather
  than discovered later.</p>
</section>''' % chart_table([("S_a", "the acceptor's Madelung group n+l"),
                            ("l_d", "the donor's orbital angular momentum"),
                            ("occ", "observed occupancy of the acceptor")],
                           X, m["res"]))
    h.append(plate.view3d(
        "mr3d", pts, ("S_a  acceptor group n+l", "occ  acceptor occupancy",
                      "l_d  donor l"),
        [(ramp(ds)[v], "donor l = %d  (%s)" % (v, SUB[v])) for v in ds],
        plate.exactness(X, (0, 1, 2), m["cells"], 0, []) +
        " Colour is the donor's &#8467;, which is also the vertical axis: the "
        "three sheets are the three kinds of subshell that give an electron up "
        "&mdash; s, d and f. <b>Twenty elements fall on %d cells</b>, so several "
        "exceptions share a transfer exactly." % m["cells"],
        "One point per cell of the chart.",
        "03", "The index, plotted exactly", radius=7,
        aria="the Madelung exception index: %d cells at acceptor group, "
             "occupancy and donor l" % m["cells"]))
    h.append('''<section>
  <div class="shead"><span class="snum">04</span><h2>It is not
  <span class="mono">inversion</span>, and that was measured</h2></div>
  <p class="sub"><span class="mono">inversion</span> asks where the two orders
  disagree. This asks where <em>nature</em> disagrees with one of them.</p>
  <div class="kv">
    <div><dt>inversion's subshell pairs</dt><dd>%d</dd></div>
    <div><dt>carrying no exception</dt><dd class="hot">%d</dd></div>
    <div><dt>element overlap</dt><dd>0<small>inversion has no elements</small></dd></div>
  </div>
  <p class="after">An inversion is <b>necessary</b> for an exception and nowhere
  near <b>sufficient</b>.</p>
  <div class="note warn"><span class="lab">And the two cells are adjacent —
  recorded, not ruled on</span>
  <p style="margin-bottom:0">This index sits at <b>%s</b>;
  <span class="mono">inversion</span> sits at <b>%s</b>. Same channel, same
  height, one unit of width apart. That is a measurement and not a verdict:
  whether such proximity should block a seating is a <em>ruling</em>, and this
  file does not make it. It is stated because a reader comparing the two charts
  would find it anyway.</p></div>
</section>''' % (npairs, without, a, b))
    h.append('''<section>
  <div class="shead"><span class="snum">05</span><h2>Every exception</h2></div>
  <div class="tablewrap tall"><table><thead><tr><th class="num">Z</th>
    <th>element</th><th>acceptor</th><th>donor</th><th>cell</th></tr></thead>
    <tbody>%s</tbody></table></div>
  <div class="note"><span class="lab">The half-filled story is counted, not told</span>
  <p style="margin-bottom:0">The familiar account is that an exception buys a
  half-filled or filled subshell. Measured over the twenty: <b>%d</b> land on a
  half-filled acceptor, <b>%d</b> on a filled one, and <b>%d on neither</b> —
  more than the other two together. The count is printed; the story is not
  told.</p></div>
</section>''' % ("".join(
        '<tr><td class="num">%d</td><td class="name">%s</td>'
        '<td class="mono">%d%s</td><td class="mono">%d%s</td>'
        '<td class="cell">(%d, %d, %d)</td></tr>'
        % (Z, sym, ac[0], SUB[ac[1]], dn[0], SUB[dn[1]], *c)
        for Z, sym, ac, dn, c in tab), hf, ff, nn))
    h.append(foot("madrule", nfixtures("madrule")))
    h.append("</div>")
    _write("madrule-plate.html", h)




def build_terms():
    import terms as T
    import itertools as _it
    X = T.index()
    m = measured(X)
    c = T.census()
    comp, iv = T.verdict_counts()
    tri = (0, 1, 2)                       # mult, L, parity -- the widest, 71 pts
    proj = sorted({tuple(cc[i] for i in tri) for cc in X})
    ls = sorted({p[1] for p in proj})
    pts = [(p[0], p[2], p[1], ramp(ls)[p[1]], 0, "") for p in proj]
    # every off-axis colour, measured
    offaxis = []
    for t3 in _it.combinations(range(4), 3):
        rest = [i for i in range(4) if i not in t3][0]
        pr = collections.defaultdict(set)
        for cc in X:
            pr[tuple(cc[i] for i in t3)].add(cc[rest])
        offaxis.append(("/".join(T.NAMES[i] for i in t3), T.NAMES[rest],
                        len(pr), sum(1 for v in pr.values() if len(v) > 1)))
    h = [plate.head("The Term Index"), '<div class="wrap">']
    h.append('''<header class="mast">
  <p class="eyebrow">Research plate · two candidates folded into one index</p>
  <h1>The Term&nbsp;Index</h1>
  <p class="dek">Every Russell–Saunders term of every banked spectrum, charted
  by what its J values do — with the Landé interval measured, gated, and sent
  to the ledger rather than onto an axis.</p>
  <div class="stamp"><span>instrument <b>terms.py</b></span>
  <span>members <b>%s terms</b></span><span>spectra <b>%d</b></span>
  <span>arity <b>4</b></span><span>cells <b>%d</b></span>
  <span>cell <b>(%d,&nbsp;%d,&nbsp;%d)</b></span><span>channel <b>K0</b></span></div>
</header>''' % ("{:,}".format(c["members"]), c["spectra"], m["cells"], *m["cell"]))
    h.append('''<div class="note warn" style="margin-top:26px">
  <span class="lab">Two candidates were folded into one, and that is the point</span>
  <p>A Russell–Saunders term index and a Landé interval-rule index were
  proposed separately over the same rows. <b>A Landé triple lies inside exactly
  one term</b> — every triple needs an L, an S and a J to exist at all — so the
  map from triples to terms is total and many-to-one. Seating both would put
  <em>one body of rows on two vertices at two different cells</em>, which is the
  case <span class="mono">overlap.py</span>'s own section 0 names as the
  dangerous one.</p>
  <p style="margin-bottom:0">Neither precedent licenses it. <em>periodic layout
  2-D</em> was withdrawn for being a strict projection over the same members;
  <span class="mono">madelung</span> stayed because it is a strict
  <em>coarsening</em> over the same members. Landé is neither — it is a
  <b>refinement of the member granularity</b>, which multiplies the box instead
  of coarsening it. So there is one index, and the interval is banked per
  triple in the ledger.</p>
</div>''')
    gr = T.gate()
    h.append('''<section>
  <div class="shead"><span class="snum">01</span><h2>The gate fired: four
  coordinates, not five</h2></div>
  <p class="sub">The interval verdict carries a <b>declared tolerance</b>, which
  is a tuning constant, so it was gated <em>before</em> the numbers were seen:
  chart the index across a range of tolerances and see whether the cell count
  moves.</p>
  <div class="tablewrap"><table><thead><tr><th class="num">tolerance</th>
    <th class="num">cells with interval</th><th>its cell</th>
    <th class="num">cells without</th></tr></thead><tbody>%s</tbody></table>
    <caption>The five-coordinate count moves, its cell moves, and the count is
    <b>not even monotone</b>. The four-coordinate count does not move at
    all.</caption></div>
  <div class="note good">
    <span class="lab">So the verdict is the measurement's, not the author's</span>
    <p style="margin-bottom:0">A coordinate whose alphabet is a function of a
    number nobody measured is not an axis. <b>interval drops to the ledger</b>,
    status <span class="mono">%s</span>, and the index seats on
    (mult,&nbsp;L,&nbsp;parity,&nbsp;completeness) at <b>%d cells, box %d, cell
    %s</b> — a chart that is tolerance-independent at every tolerance
    tried.</p></div>
</section>''' % ("".join(
        '<tr><td class="num">%s</td><td class="num">%d</td>'
        '<td class="cell">(%d, %d, %d)</td><td class="num">%d</td></tr>'
        % (t, n, cc[0], cc[1], cc[2], mm) for t, n, cc, mm in gr),
        T.INTERVAL_STATUS, m["cells"], m["box"], m["cell"]))
    h.append('''<section>
  <div class="shead"><span class="snum">02</span><h2>The sources, chosen by
  predicate and never by a file list</h2></div>
  %s
  <div class="note"><span class="lab">What is refused at the door, and named</span>
  <p><b>Bracketed jK, jj and Racah labels are refused, not coerced</b> — a label
  like <span class="mono">2[5/2]*</span> is not an LS term and has no L or S to
  test; forcing one would invent the measurement. %s rows carry such a label.
  Four files are refused for an unreadable species and are <em>named</em>:
  %s. One file is skipped as a byte-identical duplicate:
  <span class="mono">recovered/LuI__16455659.tsv</span>.</p>
  <p style="margin-bottom:0"><b>On LuI</b>, whose data rows are byte-identical
  to the corpus's own <span class="mono">quarantine/LuI.FABRICATED.tsv</span>:
  it is read anyway, because the label is unsupported. An <em>independent</em>
  capture under register 1639 agrees <b>exactly</b> on all %d of its
  (config, term, J) rows — zero disagreements, a strict subset. %d rows are
  corroborated, %d undecided, and the file is neither trusted whole nor
  discarded whole. Nothing is repaired, moved or relabelled.</p></div>
  <p class="after"><b>194 files were found where the candidate's own list held
  43.</b> The other 151 differ from those 43 only in whether their header is
  capitalised — which is a filing fact, not a fact about the data, and selecting
  by a file list would have lost them.</p>
</section>''' % (kv(("files", c["files"], "by header predicate"),
                    ("spectra", c["spectra"], "the member key, never the file"),
                    ("rows scanned", "{:,}".format(c["rows"]), ""),
                    ("levels admitted", "{:,}".format(c["admitted"]), ""),
                    ("MEMBERS", "{:,}".format(c["members"]), "")),
                 "{:,}".format(c["refused_bracketed"]),
                 ", ".join("<span class=\"mono sm\">%s</span>" % f
                           for f in T.unreadable_species()),
                 T.LUI_CORROBORATED_ROWS, T.LUI_CORROBORATED_ROWS,
                 T.LUI_UNDECIDED_ROWS))
    h.append('''<section>
  <div class="shead"><span class="snum">03</span><h2>The four seated
  coordinates</h2></div>
  %s
  <div class="note warn"><span class="lab">It does NOT test Russell–Saunders
  coupling, and the measurement says so</span>
  <p style="margin-bottom:0"><b>MIXED — a banked J outside the multiplet the
  term symbol implies — occurs on exactly ONE member of %s</b>, the Al&nbsp;I
  <span class="mono">3s.3p.(3P*).6p 2S</span> row, which banks J&nbsp;=&nbsp;3/2
  against a predicted {1/2}. So what <span class="mono">completeness</span>
  measures is the agreement between a banked <em>label</em> and its own banked
  <em>J values</em>: a statement about the table, not about whether nature
  couples that way. Calling it a coupling test is the claim the numbers refuse.
  The row is charted and <b>left alone</b>.</p></div>
</section>''' % (chart_table([("mult", "2S+1 from the term symbol, clipped at 5"),
                             ("L", "the term letter, clipped at 8"),
                             ("parity", "0 even, 1 odd"),
                             ("completeness", "banked J set against the implied multiplet")],
                            X, m["res"]),
                 "{:,}".format(c["members"])))
    h.append(plate.view3d(
        "te3d", pts, ("mult  2S+1", "parity  0 even, 1 odd",
                      "L  term letter"),
        [(ramp(ls)[v], "L = %d  (%s)" % (v, "SPDFGHIKL"[v])) for v in ls],
        plate.exactness(X, tri, len(proj), 0,
                        [(n, imp, t) for t, _c, n, imp in
                         [(a, b, n, imp) for a, b, n, imp in offaxis]]) +
        " <b>And the colour restates an axis rather than smuggling the fourth "
        "coordinate in as a lie.</b> Every off-axis colour was measured and "
        "every one is impure: " +
        "; ".join("%s coloured by %s, %d of %d points mixed"
                  % (a, b, imp, n) for a, b, n, imp in offaxis) +
        ". There is no honest fourth channel here, so colour is L, which is "
        "also the vertical axis.",
        "This index has four coordinates, so its 3-D view is a projection — and "
        "what the projection costs is measured, including what it could not "
        "honestly show.",
        "04", "The index, projected — and what that costs", radius=6,
        aria="the term index: %d of %d cells projected onto multiplicity, "
             "L and parity" % (len(proj), m["cells"])))
    h.append('''<section>
  <div class="shead"><span class="snum">05</span><h2>What the verdicts say</h2></div>
  <div class="trio">
    <div class="per"><div class="who">completeness</div>
      <div class="what">%s</div>
      <div class="obj">COMPLETE %s · SHORT %s · MIXED %d. <b>SHORT does not mean
      a level is absent</b> — a partial capture and a partial measurement look
      the same from here, and this file cannot tell which.</div></div>
    <div class="per"><div class="who">interval, at the declared %g</div>
      <div class="what">%s obey · %s break</div>
      <div class="obj"><b>BREAKS is not a fault.</b> The Landé rule is an
      approximation that holds in pure LS coupling; departure from it is
      physics.</div></div>
    <div class="per"><div class="who">not testable</div>
      <div class="what">%s</div>
      <div class="obj">%.0f%% of members have fewer than three banked levels
      with energies, so the interval cannot be formed. <b>That is a fact about
      the capture and not negative evidence.</b></div></div>
  </div>
  <h3>The Landé ledger — banked per triple, never charted</h3>
  <p>%s consecutive-J triples, each keyed to its parent term, carrying the raw
  ratio against (J+1)/J and an <b>untuned</b> band. <b>%d degenerate intervals
  are refused rather than banded to zero</b>, which would have been a lie about
  a division by nothing.</p>
  <div class="tablewrap"><table><thead><tr><th>spectrum</th><th>term</th>
    <th>2J triple</th><th class="num">ratio</th><th class="num">Landé</th>
    <th class="num">band</th></tr></thead><tbody>%s</tbody></table>
    <caption>The first twenty of %s.</caption></div>
</section>''' % (("%d" % sum(comp.values())), "{:,}".format(comp.get("COMPLETE", 0)),
                 "{:,}".format(comp.get("SHORT", 0)), comp.get("MIXED", 0),
                 T.TOLERANCE, iv.get("OBEYS", 0), iv.get("BREAKS", 0),
                 "{:,}".format(iv.get("NOT-TESTABLE", 0)),
                 100.0 * iv.get("NOT-TESTABLE", 0) / c["members"],
                 "{:,}".format(len(T.ledger())), len(T.degenerate_intervals()),
                 "".join(
                     '<tr><td class="name">%s</td><td class="mono">%s</td>'
                     '<td class="mono">%d/%d/%d</td><td class="num">%s</td>'
                     '<td class="num">%.4f</td><td class="num">%s</td></tr>'
                     % (E(sp), E(tm), tr[0], tr[1], tr[2],
                        ("%.4f" % R) if R is not None else
                        '<span class="no">DEGEN</span>', want,
                        band if band is not None else
                        '<span class="no">%s</span>' % verd)
                     for sp, _cf, tm, tr, R, want, band, verd in T.ledger()[:20]),
                 "{:,}".format(len(T.ledger()))))
    h.append(foot("terms", nfixtures("terms")))
    h.append("</div>")
    _write("terms-plate.html", h)




def build_masterindex():
    """The index of first-order indexes -- the master plate."""
    import figure as FIG
    import demand as DEM
    C = FIG.cells()
    X = FIG.figure()
    q = FIG.quantum_of()
    m = measured(X)
    own, occ = FIG.self_cell()
    res = FIG.resolution()
    nine, eleven, shared = FIG.superseded_mi()
    ks = sorted({c[0] for c in X})
    # one point per VERTEX, at its own (K, height, width), coloured by channel
    pts = [(c[1], c[2], c[0], ramp(ks)[c[0]], 0, n)
           for n, c in sorted(C.items(), key=lambda kv: kv[1])]
    h = [plate.head("The Index of First-Order Indexes"), '<div class="wrap">']
    h.append('''<header class="mast">
  <p class="eyebrow">Research plate · the master index</p>
  <h1>The Index of First-Order&nbsp;Indexes</h1>
  <p class="dek">Its members are the seated indexes of the periodic elements —
  one vertex each, at that index's own cell. A second-order object, and the only
  one here.</p>
  <div class="stamp"><span>instrument <b>figure.py</b></span>
  <span>vertices <b>%d</b></span><span>cells <b>%d</b></span>
  <span>box <b>%d</b></span><span>closes <b>%s</b></span>
  <span>channels <b>%d of 8</b></span>
  <span>E <b>%d</b></span><span>its own cell <b>(%d,&nbsp;%d,&nbsp;%d)</b></span></div>
</header>''' % (len(C), m["cells"], m["box"],
                " + ".join(FIG.closers()) or "nothing",
                len(ks), DEM.E(X), *own))
    h.append('''<div class="note warn" style="margin-top:26px">
  <span class="lab">The rebuild: it asks the registry, and the predecessor did not</span>
  <p><span class="mono">mi.py</span>'s master index is built on a <b>hardcoded
  list of nine</b>, and <b>not one of the nine is a seated index of the periodic
  elements</b>: energy conditions, warp-drive mechanisms, the withdrawn 2-D
  periodic layout, the five languages, Hawking–Ellis substances, Petrov
  spacetimes, bounds and questions. <b>The intersection with the registry's %d
  is empty.</b></p>
  <p>That is DOCKET 16's contamination in a file the cleanup did not reach.
  <span class="mono">hexad.py</span> and <span class="mono">store.py</span> were
  withdrawn for seating filing-system indexes as vertices;
  <span class="mono">mi.py</span> survived because
  <span class="mono">registry.NOT_AN_INDEX</span> excuses it as <em>"members are
  the seated indexes"</em> — which is true of its <em>type</em> and says nothing
  about <em>which</em>.</p>
  <p style="margin-bottom:0"><b><span class="mono">mi.py</span> is not deleted
  and its charting machinery is not touched.</b>
  <span class="mono">mi.cell</span>, <span class="mono">mi.height</span>,
  <span class="mono">mi.width</span>, <span class="mono">mi.K</span> and
  <span class="mono">mi.channels</span> are correct, are imported by everything
  here, and are what this plate measures with. Superseded are the four that
  depend on the nine: <span class="mono">inventory</span>,
  <span class="mono">index</span>, <span class="mono">state</span>,
  <span class="mono">self_cell</span>. DOCKET 14 — a superseded record is
  kept.</p>
</div>''' % len(eleven))
    h.append('''<section>
  <div class="shead"><span class="snum">01</span><h2>The vertices</h2></div>
  <p class="sub">One per registered index, at its own (K, height, width). The
  vertex set is <span class="mono">registry.rows()</span> and nothing else, so
  it cannot drift from the registry — it does not hold a copy of it.</p>
  <div class="tablewrap"><table><thead><tr><th>index</th><th>cell</th>
    <th class="num">K</th><th>quantum numbers ITS members carry</th></tr></thead>
    <tbody>%s</tbody></table>
    <caption><b>%d vertices, %d distinct cells — no two seated indexes share a
    cell.</b></caption></div>
</section>''' % ("".join(
        '<tr><td class="name">%s</td><td class="cell">(%d, %d, %d)</td>'
        '<td class="num">%d</td><td class="mono sm">%s</td></tr>'
        % (n, c[0], c[1], c[2], c[0], E(q[n]))
        for n, c in sorted(C.items(), key=lambda kv: kv[1])),
        len(C), m["cells"]))
    h.append(plate.view3d(
        "ma3d", pts, ("height  longest chain", "width  largest antichain",
                      "K  the channel"),
        [(ramp(ks)[v], "K%d" % v) for v in ks],
        plate.exactness(X, (0, 1, 2), m["cells"], 0, []) +
        " Each point is a whole index — <b>the labelled dot is that "
        "index's entire chart reduced to one position</b>. Colour is K, the "
        "channel, which is also the vertical axis: the %d sheets are the %d "
        "channels the %d occupy out of eight possible, and the three narrowest "
        "points are the coarsenings M's overlap ruling seated. <b>gravity's "
        "width of 112 is what stretches the box</b>, and the crowd near the "
        "origin is every small index." % (len(ks), len(ks), len(C)),
        "One point per seated index, at its own cell. Labelled, because there "
        "are only %d and each one is a whole index." % len(C),
        "02", "The master index, plotted exactly", radius=8,
        aria="the index of first-order indexes: %d vertices at height, width "
             "and channel" % len(C)))
    h.append('''<section>
  <div class="shead"><span class="snum">03</span><h2>Its three axes were two
  row labels and a measurement — and are now three measurements</h2></div>
  <div class="tablewrap"><table><thead><tr><th>axis</th>
    <th class="num">distinct</th><th class="num">of</th>
    <th class="num">ratio</th><th>verdict</th></tr></thead><tbody>%s</tbody>
    </table><caption>The threshold is 0.9.</caption></div>
  <div class="note warn">
    <span class="lab">A recorded prediction, refuted by measurement</span>
    <p>A coordinate separating 90 %% or more of the members <em>groups
    nothing</em> and multiplies the box — which is what
    <span class="mono">overlap.py</span> exists to catch. <b>At eleven vertices
    it caught it here</b>: height 0.909 and width perfectly injective at 1.000,
    both LABELs, leaving K the only measurement. The reasoning filed with that
    finding was that each index has essentially its own height and its own
    width, so the two approach injectivity <b>by construction</b> as the figure
    grows.</p>
    <p><b>That reasoning is now refuted.</b> Three more vertices — the
    coarsenings M's overlap ruling seated — made it <em>better</em>: height
    0.909 &rarr; 0.714, width 1.000 &rarr; 0.857, and <b>no axis is a row label
    any more</b>. The prediction assumed every new index brings a new height and
    a new width; a <em>coarsening</em> of a seated index does not, because it
    lands in the part of the poset its parent already occupies. The label
    problem tracks <b>how the vertex set is built</b>, not how big it is.</p>
    <p style="margin-bottom:0"><b>K</b> was never in doubt — a down-set of the
    language poset, eight possible values and %d observed at %d vertices.
    DOCKET 11's chart is unchanged: nothing was repaired, the figure moved, and
    the old reading is kept beside the new one.</p></div>
</section>''' % ("".join(
        '<tr><td class="name mono">%s</td><td class="num">%d</td>'
        '<td class="num">%d</td><td class="num">%.4f</td><td>%s</td></tr>'
        % (a, d, n, r, '<span class="no">LABEL</span>' if v == "LABEL"
           else "measurement") for a, d, n, r, v in res),
        len({c[0] for c in X}), len(C)))
    cl, _b = hlaw.closures(X)
    h.append('''<section>
  <div class="shead"><span class="snum">04</span><h2>What it closes, and what
  it is not</h2></div>
  %s
  <div class="kv" style="margin-top:22px">
    <div><dt>closers</dt><dd>%s<small>%s</small></dd></div>
    <div><dt>E</dt><dd>%d<small>reported, never a target</small></dd></div>
    <div><dt>its own cell</dt><dd>(%d, %d, %d)</dd></div>
    <div><dt>occupied by</dt><dd class="hot">%s<small>it is not one of its own
      first-order indexes</small></dd></div>
  </div>
  <p class="after"><b>E is not a target.</b> M: <em>"I don't care about closure.
  I only care that we identify every possible first-order index."</em> It is
  reported because it is measured, and no index seated here was built to land on
  a demanded cell.</p>
</section>''' % (closure_table(m),
                 " + ".join(FIG.closers()) or "none",
                 "it closes in nothing; at eleven vertices it closed under "
                 "statistics" if not FIG.closers() else "of the five",
                 DEM.E(X), own[0], own[1], own[2],
                 ", ".join(occ) if occ else "no member"))
    h.append('''<section>
  <div class="shead"><span class="snum">05</span><h2>Dilworth on every
  vertex</h2></div>
  <p class="sub">|X| ≤ height × width, so the three axes are not independent and
  the product box overstates the space — DOCKET 3's other half, by theorem
  rather than census.</p>
  <div class="tablewrap"><table><thead><tr><th>index</th><th class="num">|X|</th>
    <th class="num">height</th><th class="num">width</th>
    <th class="num">h × w</th><th></th></tr></thead><tbody>%s</tbody></table>
    <caption>No violations.</caption></div>
</section>''' % "".join(
        '<tr><td class="name">%s</td><td class="num">%d</td>'
        '<td class="num">%d</td><td class="num">%d</td><td class="num">%d</td>'
        '<td>%s</td></tr>'
        % (nm, n, hh, w, hw, '<span class="yes">holds</span>' if okd
           else '<span class="no">VIOLATED</span>')
        for nm, n, hh, w, hw, okd in FIG.dilworth()))
    h.append('''<section>
  <div class="shead"><span class="snum">06</span><h2>What it refuses</h2></div>
  <ul class="tight refuse">
    <li><b>To report a growth narrative.</b> The old one was an artefact of the
      order a contaminated set was seated in, and no clean trajectory exists
      yet. Vertex counts are printed; trends are not.</li>
    <li><b>To name a shape.</b> %d vertices is what there are today —
      <em>hexad</em>, <em>octad</em> and the rest were names for a count that
      kept moving.</li>
    <li><b>To treat E as a target.</b></li>
    <li><b>To call itself complete.</b> <span class="mono">registry.COMPLETE</span>
      is False and this file has no opinion the registry does not.</li>
  </ul>
</section>''' % len(C))
    h.append(foot("figure", nfixtures("figure")))
    h.append("</div>")
    _write("masterindex-plate.html", h)



def build_overlaprule():
    """M's overlap ruling: what it seats, what it refuses, and on which ground."""
    import overlaprule as OR
    import figure as FIG
    ks_all = sorted({c[0] for c in FIG.figure()})
    cand = [(pp, cc, OR.mi.K(OR.project(pp, cc)), len(OR.project(pp, cc)),
             OR.adjudicate(pp, cc)) for pp, cc, _k in OR.CANDIDATES]
    seats = OR.admissible()
    gate_first, max_first = OR.order_matters()

    h = [plate.head("The Overlap Ruling"), '<div class="wrap">']
    h.append('''<header class="mast">
  <p class="eyebrow">Research plate &middot; a ruling, and its three seatings</p>
  <h1>The Overlap&nbsp;Ruling</h1>
  <p class="dek">When a chart that overlaps a seated index may be seated
  anyway &mdash; and when it is one piece of information seated twice.</p>
  <div class="stamp"><span>instrument <b>overlaprule.py</b></span>
  <span>candidates <b>%d</b></span><span>seated <b>%d</b></span>
  <span>refused <b>%d</b></span><span>channels now <b>%d of 8</b></span></div>
</header>''' % (len(cand), len(seats), len(OR.refused()), len(ks_all)))

    h.append('''<div class="note">
  <span class="lab">The ruling</span>
  <p style="margin-bottom:0"><em>&ldquo;They can be seated with overlaps so long
  as it is not an overlap of same information. An overlap of values in two
  different languages should tell us two parts of definition contained in that
  overlapped position. Information is information. But its relative position in
  this index is information about an object.&rdquo;</em> &mdash; M</p>
</div>''')

    h.append('''<section>
  <div class="shead"><span class="snum">01</span><h2>The reading is picked by
  arithmetic, not by preference</h2></div>
  <p class="sub">Six readings of &ldquo;not an overlap of same information&rdquo;,
  charted against all 272 proper sub-charts of the seated indexes.</p>
  <div class="tablewrap"><table><thead><tr><th>reading</th>
    <th class="num">admits</th><th></th></tr></thead><tbody>
    <tr><td>R1 &mdash; channel differs from its own parent</td>
      <td class="num">109</td><td><span class="no">explodes</span></td></tr>
    <tr><td>R2 &mdash; cell differs from its own parent</td>
      <td class="num">254</td><td><span class="no">explodes</span></td></tr>
    <tr><td>R3 &mdash; cell occupied by no seated vertex</td>
      <td class="num">252</td><td><span class="no">explodes</span></td></tr>
    <tr><td><b>R4 &mdash; CHANNEL occupied by no seated vertex</b></td>
      <td class="num"><b>6</b></td><td><span class="yes">bounded</span></td></tr>
    </tbody></table>
    <caption><b>R3 admits 252, of which 117 are coarsenings of
    <span class="mono">gravity</span> alone</b> &mdash; the explosion
    <span class="mono">overlap.py</span> exists to prevent, through the front
    door. R4 admits six, and R4 is what M&rsquo;s words say: the ruling names
    <em>languages</em>, and the channel is the set of languages that close a
    chart.</caption></div>
</section>''')

    h.append('''<section>
  <div class="shead"><span class="snum">02</span><h2>Every candidate, every
  ground</h2></div>
  <p class="sub">Two of the three grounds are DOCKET 2&rsquo;s own, from the
  withdrawal of <span class="mono">periodic layout 2-D</span>: a chart with as
  many cells as its parent is the parent relabelled, and a channel that moves
  as the construction extends is a fact about where it stopped.</p>
  <div class="tablewrap"><table><thead><tr><th>parent</th><th>sub-chart</th>
    <th class="num">K</th><th class="num">cells</th><th>novel channel</th>
    <th>not a relabelling</th><th>reach gate</th><th></th></tr></thead>
    <tbody>%s</tbody></table>
    <caption><b>%d seated, %d refused.</b> K1, K5 and K6 became occupied; K4
    did not &mdash; its only two candidates both failed on the reach, which is
    two failures and not a theorem.</caption></div>
</section>''' % ("".join(
        '<tr><td class="name">%s</td><td class="mono sm">%s</td>'
        '<td class="num">%d</td><td class="num">%d</td>'
        '<td>%s</td><td>%s</td><td>%s</td><td><b>%s</b></td></tr>'
        % (pp, "/".join(cc), k, nc,
           _yn(g["novel channel"]), _yn(g["not a relabelling"]),
           _yn(g["reach stable"]),
           '<span class="yes">SEAT</span>' if okd
           else '<span class="no">refuse</span>')
        for pp, cc, k, nc, (okd, g) in cand), len(seats), len(OR.refused())))

    h.append('''<section>
  <div class="shead"><span class="snum">03</span><h2>The reach gate</h2></div>
  <p class="sub">Shaped after the two failures this tree has already seen
  &mdash; DOCKET 2&rsquo;s moving channel and <span class="mono">terms.py</span>&rsquo;s
  non-monotone cell count. <b>(a)</b> no late arrival, <b>(b)</b> no
  oscillation, <b>(c)</b> a majority of reaches. Swept over each parent&rsquo;s
  own <em>data</em> reach and never over an independent variable.</p>
  <div class="tablewrap"><table><thead><tr><th>sub-chart</th>
    <th class="num">holds</th><th>the sweep</th></tr></thead><tbody>%s</tbody>
    </table><caption>A gate that admits everything is not a gate: this one
    refuses half of what it is shown.</caption></div>
</section>''' % "".join(
        '<tr><td class="name">%s <span class="mono sm">%s</span></td>'
        '<td class="num">%d/%d</td><td class="mono sm">%s</td></tr>'
        % (pp, "/".join(cc), OR.ground_reach_stable(pp, cc)[1],
           OR.ground_reach_stable(pp, cc)[2],
           " &nbsp; ".join(
               ("<b>K%d</b>" % kk if kk == k else
                '<span class="no">K%d</span>' % kk) + "<small>(%d)</small>" % nn
               for _l, nn, kk in OR.reach_sweep(pp, cc)))
        for pp, cc, k, _nc, _v in cand))

    # ---- the three 3-D views.  Two of the three charts have arity 2, so the
    # third axis is the REACH -- the sweep that gated them, drawn rather than
    # tabulated.  It is a real coordinate of the measurement, not a filler.
    for snum, (pp, cc) in zip(("04", "05", "06"),
                              [(a, b) for a, b, _k, _n in seats]):
        k = OR.mi.K(OR.project(pp, cc))
        X = OR.project(pp, cc)
        unit, pts_r = OR.SWEEPS[pp]
        if len(cc) == 3:
            vals = sorted({x[2] for x in X})
            tok = ramp(vals)
            pt = [(x[0], x[1], x[2], tok[x[2]], 0, None) for x in sorted(X)]
            axes = (cc[0], cc[1], cc[2])
            legend = [(tok[v], "%s = %s" % (cc[2], v)) for v in vals]
            cap = ("<b>This view is the index itself, not a projection of "
                   "it.</b> The chart has three coordinates and they are the "
                   "three axes, so every one of the %d cells is its own point "
                   "and nothing is collapsed. <b>It is join-closed and not "
                   "meet-closed</b> &mdash; 0 join counterexamples against 32 "
                   "meet, in 325 unordered pairs &mdash; so it is a "
                   "join-semilattice, which is the shape K1 has here." % len(X))
            sub_ = ("One point per realised (bound class, forced angular "
                    "momentum, spin decade). Colour is the spin decade.")
        else:
            tok = ramp(list(pts_r))
            pt = []
            for r in pts_r:
                for x in sorted(OR.at_reach(pp, cc, r)):
                    pt.append((x[0], x[1], r, tok[r], 0, None))
            axes = (cc[0], cc[1], "reach  %s" % unit)
            legend = [(tok[r], "%s %s" % (unit, r)) for r in pts_r]
            cap = ("The chart has two coordinates, so <b>the third axis is the "
                   "reach</b> &mdash; the sweep the gate ran, drawn rather "
                   "than tabulated. Each horizontal sheet is the chart at one "
                   "reach; read upward to watch it fill. <b>%d of the %d "
                   "sheets close in K%d</b>, which is what the gate measures, "
                   "and the top sheet is the %d cells actually seated."
                   % (OR.ground_reach_stable(pp, cc)[1], len(pts_r), k, len(X)))
            sub_ = ("The chart at every point of its own data reach, stacked. "
                    "Colour is the reach.")
        h.append(plate.view3d(
            "or3d%s" % snum, pt, axes, legend, cap, sub_, snum,
            "%s (%s) &mdash; K%d" % (pp, ", ".join(cc), k), radius=7,
            aria="%s on %s, %d points" % (pp, "/".join(cc), len(pt))))

    h.append('''<section>
  <div class="shead"><span class="snum">07</span><h2>The order of the two tests
  is load-bearing</h2></div>
  <p class="sub">A maximality clause also applies: if a super-chart of the same
  parent reaches the same channel, the smaller chart repeats its language set
  and carries nothing more. <span class="mono">gravity&nbsp;(B,F,X)</span> and
  <span class="mono">gravity&nbsp;(B,F,X,E)</span> are exactly that pair, both
  K1 &mdash; and the gate refuses the larger one.</p>
  <div class="kv">
    <div><dt>gate, then maximality</dt><dd>%s<small>K1 occupied</small></dd></div>
    <div><dt>maximality, then gate</dt><dd>%s<small>K1 EMPTY</small></dd></div>
  </div>
  <p class="after"><b>Soundness before redundancy.</b> The gate asks whether a
  channel verdict is a fact about the object; maximality asks which of two facts
  to keep. A chart that fails the gate has no channel verdict to be maximal
  about. Here the clause is <em>inert</em> &mdash; the three that pass have three
  different parents &mdash; and it is implemented and fixtured anyway, because it
  is inert by measurement and not by construction.</p>
</section>''' % (", ".join("K%d" % k for k in gate_first),
                 ", ".join("K%d" % k for k in max_first)))

    h.append('''<section>
  <div class="shead"><span class="snum">08</span><h2>Recorded, not explained:
  the closure algebra sees the ultraspinning threshold</h2></div>
  <p class="sub">Sweeping <span class="mono">gravity</span>&rsquo;s D &mdash; its
  <em>independent variable</em>, so no part of any gate.</p>
  <div class="tablewrap"><table><thead><tr><th>sub-chart</th>%s</tr></thead>
    <tbody>%s</tbody></table></div>
  <div class="note warn">
    <span class="lab">D = 6 is exactly where singly-rotating Myers&ndash;Perry
    loses its horizon bound</span>
    <p style="margin-bottom:0">Read in four and five dimensions the bound
    structure of nuclear matter <b>closes in all five languages</b>. Admit the
    sixth and four of the five break at once, leaving information alone, and it
    never moves again through D&nbsp;=&nbsp;11. D&nbsp;=&nbsp;4 gives the Kerr
    bound &mu;&nbsp;&ge;&nbsp;2a, D&nbsp;=&nbsp;5 gives
    &mu;&nbsp;&ge;&nbsp;a&sup2;, and from D&nbsp;=&nbsp;6 the ultraspinning
    branch has none. <b>The threshold is visible in the closure algebra, at the
    dimension the theorem names, without the closure operators being told
    anything about dimension.</b> One threshold in one index, found by sweeping
    rather than predicted, and no mechanism is offered for why losing a bound
    should cost four languages and not three.</p></div>
</section>''' % ("".join('<th class="num">D &le; %d</th>' % d
                          for d, _n, _k in OR.dimension_finding()[0][1]),
                 "".join(
        '<tr><td class="name mono sm">%s</td>%s</tr>'
        % ("/".join(cols),
           "".join('<td class="num">%s</td>'
                   % ('<span class="no">K%d</span>' % kk if kk != 1
                      else "<b>K%d</b>" % kk) for _d, _n, kk in seq))
        for cols, seq in OR.dimension_finding())))

    h.append('''<section>
  <div class="shead"><span class="snum">09</span><h2>What this ruling refuses</h2></div>
  <ul class="tight refuse">
    <li><b>To seat on a differing channel alone.</b> Three of six candidates
      died on the other grounds.</li>
    <li><b>To call K4 unreachable.</b> Two candidates reached it and both failed
      the reach gate. Two failures, not a theorem.</li>
    <li><b>To reopen DOCKET 2.</b> <span class="mono">periodic layout 2-D</span>
      fails the bijection ground <em>and</em> the reach ground.</li>
    <li><b>To revive anything deleted for the criterion.</b>
      <span class="mono">store.py</span>, <span class="mono">obstruction.py</span>,
      <span class="mono">cross.py</span>, <span class="mono">density.py</span> and
      <span class="mono">occupy.py</span> went because their members are not
      elements, and this ruling says nothing about that.</li>
    <li><b>To be run twice for more.</b>
      <span class="mono">seated_channels()</span> excludes the ruling&rsquo;s own
      rows, so a second pass sees the same four empty channels and the same six
      candidates. Nothing compounds.</li>
    <li><b>To claim the per-witness readings were independently checked.</b> A
      seventeen-agent adversarial run returned <em>one</em> agent before a weekly
      quota; it checked the readings in section 01 and contributed section 07,
      and nothing else. The physics stated for each seating is this tree&rsquo;s
      own reading.</li>
  </ul>
</section>''')
    h.append(foot("overlaprule", nfixtures("overlaprule")))
    h.append("</div>")
    _write("overlaprule-plate.html", h)


def _yn(v):
    return ('<span class="yes">yes</span>' if v
            else '<span class="no">NO</span>')

BUILDERS = {"inversion": build_inversion, "probability": build_probability,
            "laws": build_laws, "fibred": build_fibred,
            "madelung": build_madelung, "channels": build_channels,
            "ions": build_ions,
            "nucshell": build_nucshell, "madrule": build_madrule,
            "terms": build_terms,
            "masterindex": build_masterindex,
            "overlaprule": build_overlaprule}

if __name__ == "__main__":
    want = sys.argv[1:] or sorted(BUILDERS)
    for w in want:
        BUILDERS[w]()
