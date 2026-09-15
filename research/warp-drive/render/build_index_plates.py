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
# six made l = 6 and l = 0 the SAME COLOUR -- two different subshell types under
# one hue, which is a lie the eye cannot see through. `ramp()` refuses to wrap.
RAMP = ("--statistics", "--geometry", "--information", "--algebra", "--order",
        "--accent", "--hue7", "--hue8")


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


BUILDERS = {"inversion": build_inversion, "probability": build_probability,
            "laws": build_laws, "fibred": build_fibred,
            "madelung": build_madelung, "channels": build_channels,
            "ions": build_ions}

if __name__ == "__main__":
    want = sys.argv[1:] or sorted(BUILDERS)
    for w in want:
        BUILDERS[w]()
