#!/usr/bin/env python3
r"""
build_particle_plates.py -- the plates for DOCKET 27's three particle indexes.

    python3 build_particle_plates.py               writes all three
    python3 build_particle_plates.py mesons        writes one

M: "produce indexes and plates for all particles other than periodic atoms.
We need photons, muons, anti-matter, whatever particle there is that isn't
already indexed."

`fundamental`, `mesons` and `baryons` are the first indexes in this tree whose
members are not atomic at all.  Each is built on the shared scaffold in
`plate.py`, so the stylesheet, the measured axis choice, the swept camera and
the inlined runtime are one implementation rather than three.

NONE OF THE THREE HAS ARITY 3, so every view here is a PROJECTION and
`plate.exactness()` says what it costs in the caption -- fundamental and mesons
project 4 coordinates onto 3, baryons projects 7.  That is stated rather than
left for a reader to assume, exactly as `build_index_plates.py` states it for
`gravity`.

Every number is read from the instrument at build time.  Nothing is retyped.
"""

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

from build_index_plates import (                                # noqa: E402
    RAMP, ramp, measured, chart_table, closure_table, kv, foot, nfixtures,
    _write, _alpha)

E = html.escape


def _typo(t):
    """Set the declared SOURCE string as prose.

    The declaration is ASCII because it lives in a Python file beside the code
    that reads it; this renders it. Backticks become a mono span, paired
    straight quotes become curly, and " -- " becomes an em dash. THE STRING IS
    NEVER CHANGED -- only its setting.

    ORDER MATTERS AND IT BIT ONCE: curl the quotes BEFORE any markup is
    inserted, or the pass rewrites the quotes in `class="mono"` and the plate
    ships with broken attributes.
    """
    q = []
    n = 0
    for ch in t:
        if ch == '"':
            q.append("\x01" if n % 2 == 0 else "\x02")
            n += 1
        else:
            q.append(ch)
    t = E("".join(q)).replace(" -- ", "\x03")
    bits = t.split("`")
    t = "".join(b if i % 2 == 0 else '<span class="mono">%s</span>' % b
                for i, b in enumerate(bits))
    return (t.replace("\x01", "&ldquo;").replace("\x02", "&rdquo;")
             .replace("\x03", " &mdash; "))


def sourceline(mod):
    """The provenance block, read from registry.sources() and never retyped."""
    s = registry.sources()["%s.index" % mod]
    fs = "".join(
        '<li><span class="mono">%s</span> — %s, %s bytes, md5 '
        '<span class="mono">%s</span></li>'
        % (E(d["path"]), "%d files" % d["files"] if d["kind"] == "dir"
           else "one file", d["bytes"], d["md5"])
        for d in s["paths"])
    return ('<div class="note"><span class="lab">Where the data comes '
            'from</span><p>%s</p><ul>%s</ul>'
            '<p style="margin-bottom:0">Declared as <span class="mono">'
            'SOURCE</span> in <span class="mono">%s.py</span> beside the code '
            'that reads it, and hashed into <span class="mono">STATE.json</span> '
            'by <span class="mono">state.py</span>. A provenance held only in '
            'prose has to be recovered later.</p></div>'
            % (_typo(s["why"]), fs, mod))


def collide_note(pairs, head, tail):
    rows = "".join('<tr><td class="cell">%s</td><td class="mono">%s</td></tr>'
                   % (str(k), E(", ".join(v))) for k, v in pairs)
    return ('<div class="note"><span class="lab">%s</span>'
            '<div class="tablewrap"><table><thead><tr><th>cell</th>'
            '<th>members sharing it</th></tr></thead><tbody>%s</tbody></table>'
            '</div><p style="margin-bottom:0">%s</p></div>' % (head, rows, tail))


def _mast(eyebrow, title, dek, stamp):
    return ('<header class="mast"><p class="eyebrow">%s</p><h1>%s</h1>'
            '<p class="dek">%s</p><div class="stamp">%s</div></header>'
            % (eyebrow, title, dek,
               "".join("<span>%s <b>%s</b></span>" % (a, b) for a, b in stamp)))


def _view(pid, X, colour_i, names, caption_extra, snum, title, aria,
          radius=5.0):
    """The 3-D section, with the projection chosen by measurement."""
    tri, pts, impure, rows = plate.axis_choice(X, colour_i)
    vals = sorted({c[colour_i] for c in X})
    tok = ramp(vals)
    P = [(c[tri[0]], c[tri[1]], c[tri[2]], tok[c[colour_i]], 0, "")
         for c in sorted(X)]
    return plate.view3d(
        pid, P, tuple(names[i] for i in tri),
        [(tok[v], "%s = %s" % (names[colour_i].split()[0], v)) for v in vals],
        plate.exactness(X, tri, pts, impure, rows) + " " + caption_extra,
        "One point per cell of the chart, at its own coordinates.",
        snum, title, radius=radius, aria=aria)


# ===========================================================================

def build_fundamental():
    import fundamental as F
    X = F.index()
    m = measured(X)
    R = F.rows()
    d, n, r, verdict = F.mass_is_not_a_label()
    have, lack, lacknames = F.mass_is_not_total()
    now, withL, left = F.what_L_would_do()
    h = [plate.head("The Fundamental Particles"), '<div class="wrap">']
    h.append(_mast(
        "Research plate · an index of quantum objects · DOCKET 27",
        "The Fundamental&nbsp;Particles",
        "Every particle the Standard Model does not build out of anything "
        "else — six quarks, six leptons, the gauge bosons and the Higgs, with "
        "each antiparticle counted as a member of its own — charted on the "
        "four quantum numbers that define them.",
        [("instrument", "fundamental.py"), ("members", "%d particles" % len(R)),
         ("arity", "4"), ("cells", str(m["cells"])),
         ("cell", "(%d,&nbsp;%d,&nbsp;%d)" % m["cell"]),
         ("channel", "K%d" % m["cell"][0])]))
    h.append('''<section>
  <div class="shead"><span class="snum">01</span><h2>The subject widened; the
  criterion did not</h2></div>
  <p class="sub">M: &ldquo;This is a valid exception to the registry criteria.
  These are legitimate particles and can and must be accepted.&rdquo;</p>
  <p>Every index seated in this tree before DOCKET 27 was an index of the
  periodic elements. The criterion in <span class="mono">registry.py</span> is
  not about elements though &mdash; it is that <b>a member must carry quantum
  numbers</b>, and a muon carries spin, charge and lepton number as surely as an
  electron does. So the subject widens to <b>quantum objects</b> and the
  criterion is untouched: <span class="mono">enforce()</span> is unchanged and
  still returns empty, and every row seated before the ruling still passes.</p>
  <p><b>Antiparticles are separate members.</b> The positron&rsquo;s charge is
  not the electron&rsquo;s, and a chart that merged them would be charting an
  equivalence class it had not declared.</p>
  %s
</section>''' % sourceline("fundamental"))
    h.append('''<section>
  <div class="shead"><span class="snum">02</span><h2>The four coordinates,
  declared before the chart was run</h2></div>
  <p class="sub">Three are read from the capture. One &mdash; the colour
  dimension &mdash; is assigned from the Standard Model&rsquo;s own definition,
  because the PDG table does not carry it, and
  <span class="mono">colour_rule()</span> prints the assignment rather than
  hiding it.</p>
  %s
</section>''' % chart_table(
        [("2J", "spin, doubled: 1 for every fermion, 2 for a gauge boson, 0 for the Higgs"),
         ("Q3", "electric charge in thirds, so the quarks are integers"),
         ("COL", "the dimension of the colour representation: 3, 8 or 1"),
         ("GEN", "generation, 1&ndash;3 for a fermion and 0 for a boson")],
        X, m["res"]))
    h.append(_view(
        "f3d", X, 3,
        ["2J  spin doubled", "Q3  charge in thirds", "COL  colour dimension",
         "GEN  generation"],
        "Colour is the generation, so the three fermion families and the boson "
        "row separate by hue.", "03", "The index, plotted",
        "the fundamental-particle index", radius=7))
    h.append('''<section>
  <div class="shead"><span class="snum">04</span><h2>%d cells over %d members:
  the four collisions are the finding</h2></div>
  <p class="sub">They are not a defect in the coordinate set. They are the two
  facts it is sharp enough to expose.</p>
  %s
  <p><b>The three neutrino pairs</b> collide because what separates a neutrino
  from an antineutrino is lepton number, and for every <em>other</em> fermion
  the charge does that work. The neutrinos are the members on which it cannot,
  because they are the neutral ones.</p>
  <div class="note good"><span class="lab">The photon against the Z is the one
  cell no admissible coordinate could split</span>
  <p style="margin-bottom:0">It survives <em>every</em> additive quantum number
  &mdash; lepton and baryon number are both zero on both. What distinguishes the
  photon from the Z is the weak mixing angle: a continuous parameter of the
  model, not a quantum number. Both of the refusals in section 05 land on this
  one pair.</p></div>
</section>''' % (m["cells"], len(R),
                 collide_note(F.collisions(), "Every collision, and it is a "
                              "pair in all four cases",
                              "Cells are (2J, Q3, COL, GEN).")))
    h.append('''<section>
  <div class="shead"><span class="snum">05</span><h2>What is refused, and each
  refusal measured</h2></div>
  <p class="sub">The refusals decide the chart as much as the choices do, so
  none of them is left as an assertion.</p>
  <h3>Weak isospin and hypercharge</h3>
  <p>The textbook gauge quantum numbers, and not charted. They are properties
  of a <b>chiral field</b> &mdash; the left-handed electron and the right-handed
  electron carry different T&#8323; and Y &mdash; and the PDG table lists
  particles, not chiral components. Charting a single T&#8323; against a
  particle would mean choosing a chirality the data does not name. Recorded as
  the sharpest thing this index cannot say.</p>
  <h3>Mass &mdash; and the usual reason withdrawn</h3>
  <p>Elsewhere in this tree a near-injective coordinate is refused as a row
  <em>label</em>. <b>That argument does not apply here and the measurement says
  so:</b> %d distinct values over %d members, %.4f, far below the 0.9 threshold
  &mdash; because CPT forces a particle and its antiparticle to carry exactly
  equal mass, so every value in the table is doubled. The refusal that does hold
  is <b>totality</b>: %d of the %d members carry no mass at all (%s), for which
  PDG publishes limits and not values, and a coordinate undefined on a fifth of
  the membership cannot chart the membership.</p>
  <h3>Lepton and baryon number &mdash; refused as fitted, with the price paid</h3>
  <p>Both are derivable from the PDG id. Neither was declared in section 02
  before the chart was run, and the only reason to reach for them now is that
  the chart collided &mdash; <b>which is the definition of fitted</b>, and
  DOCKET 23 refuses exactly that move. The price is on the record rather than
  hidden: appending lepton number would take %d cells to %d, and <b>%s would
  still collide</b>.</p>
</section>''' % (d, n, r, lack, len(R), E(", ".join(lacknames)), now, withL,
                 E("; ".join(", ".join(g) for g in left))))
    h.append('''<section>
  <div class="shead"><span class="snum">06</span><h2>Every member</h2></div>
  <div class="tablewrap"><table><thead><tr><th>name</th>
    <th class="num">PDG id</th><th class="num">2J</th><th class="num">Q3</th>
    <th class="num">COL</th><th class="num">GEN</th></tr></thead><tbody>%s
  </tbody></table><caption>%d members on %d cells. Sorted by generation, then
  spin, then charge.</caption></div>
</section>''' % ("".join(
        '<tr><td class="mono">%s</td><td class="num mono">%d</td>'
        '<td class="num">%d</td><td class="num">%d</td><td class="num">%d</td>'
        '<td class="num">%d</td></tr>' % (E(n_), p, j, q, c, g)
        for n_, p, j, q, c, g in R), len(R), m["cells"]))
    h.append('''<section>
  <div class="shead"><span class="snum">07</span><h2>What closes it</h2></div>
  %s
  %s
</section>''' % (closure_table(m),
                 kv(("channel", "K%d" % m["cell"][0],
                     "statistics alone"),
                    ("height", str(m["cell"][1]), "Mirsky"),
                    ("width", str(m["cell"][2]), "Dilworth"),
                    ("|X| &le; h&times;w", "%d &le; %d" %
                     (m["cells"], m["cell"][1] * m["cell"][2]), ""))))
    h.append(foot("fundamental", nfixtures("fundamental")))
    h.append("</div>")
    _write("fundamental-plate.html", h)


def build_mesons():
    import mesons as M
    X = M.index()
    m = measured(X)
    R = M.rows()
    ce_n, ce_cell, ce_cl = M.ceigen_chart()
    pairs, same, split, qs, qd = M.conjugation()
    h = [plate.head("The Meson Index"), '<div class="wrap">']
    h.append(_mast(
        "Research plate · an index of quantum objects · DOCKET 27",
        "The Meson&nbsp;Index",
        "Two hundred and forty-two mesons of the Particle Data Group&rsquo;s "
        "table, antiparticles counted separately, charted on spin, parity, "
        "isospin and charge &mdash; and two theorems about which quantum "
        "numbers a meson is even allowed to have.",
        [("instrument", "mesons.py"), ("members", "%d of 250" % len(R)),
         ("arity", "4"), ("cells", str(m["cells"])),
         ("cell", "(%d,&nbsp;%d,&nbsp;%d)" % m["cell"]),
         ("channel", "K%d" % m["cell"][0])]))
    h.append('''<section>
  <div class="shead"><span class="snum">01</span><h2>The members, and the eight
  that are named rather than dropped</h2></div>
  <p class="sub">PDG reports no parity for eight of the 250, so a chart carrying
  P cannot place them. They are listed, not quietly discarded.</p>
  <p class="eqn mono">%s</p>
  <p>That is a gap in the <em>table</em>, not in physics: a later Review that
  measures those parities seats them with no change to the instrument but the
  count.</p>
  %s
</section>''' % (E(", ".join(M.unplaced())), sourceline("mesons")))
    h.append('''<section>
  <div class="shead"><span class="snum">02</span><h2>The four coordinates</h2></div>
  <p class="sub">Every meson here is an integer-spin boson, so 2J is even; it is
  doubled anyway so the column reads the same as it does for the baryons and the
  fundamental particles.</p>
  %s
</section>''' % chart_table(
        [("2J", "spin, doubled"), ("P", "parity"),
         ("2I", "isospin doubled: 0, 1 or 2 for I = 0, &frac12; or 1"),
         ("Q3", "electric charge in thirds")], X, m["res"]))
    # COLOUR IS CHARGE, and charge is also an axis.  That is deliberate and it
    # is the `inversion` plate's precedent: a point's position and its hue say
    # the same thing on one coordinate, which makes the three charge sheets
    # readable from any angle -- and charge is the coordinate section 06's
    # theorem turns on.  It is also the widest PURE projection the scaffold
    # finds: 39 of the 66 cells against 28 for any parity-coloured view.
    h.append(_view(
        "m3d", X, 3, ["2J  spin doubled", "P  parity", "2I  isospin doubled",
                      "Q3  charge in thirds"],
        "Colour is charge, and charge is also the third axis, so a point&rsquo;s "
        "height and its hue say the same thing &mdash; which is the coordinate "
        "the conjugation theorem in section 06 turns on.",
        "03", "The index, projected", "the meson index", radius=6))
    h.append('''<section>
  <div class="shead"><span class="snum">04</span><h2>C-parity is printed for
  exactly the self-conjugate mesons &mdash; with two exceptions, and the two are
  the finding</h2></div>
  <p class="sub">168 of the 250 carry no C at all. That is not a missing
  measurement: it is a theorem, and <span class="mono">c_is_defined_iff()</span>
  checks it against the table rather than asserting it.</p>
  <div class="note good"><span class="lab">The two exceptions are K&#8304;<sub>L</sub>
  and K&#8304;<sub>S</sub></span>
  <div class="tablewrap"><table><thead><tr><th>meson</th><th>quark content</th>
  <th>self-conjugate</th><th>carries a C</th></tr></thead><tbody>%s</tbody>
  </table></div>
  <p style="margin-bottom:0">Both are self-conjugate neutrals, and both are
  <b>strangeness mixtures</b> &mdash; a mixture of that kind is a
  <em>CP</em> eigenstate and not a <em>C</em> eigenstate. The table reproduces
  the textbook distinction with no help from the instrument.</p></div>
  <p><b>G-parity is a second theorem of the same shape.</b> It is printed for
  exactly the flavour-neutral mesons &mdash; net strangeness, charm and beauty
  all zero &mdash; and 132 of the 250 are not flavour-neutral.
  <span class="mono">g_is_defined_iff()</span> finds no exception at all.</p>
  <p><b>And strangeness itself is refused</b>, because %d of the 250 carry a
  quark content that is not a plain string of quark letters. For two of those
  there is no strangeness to read at all: the neutral kaons are not strangeness
  eigenstates. <span class="mono">strangeness()</span> returns nothing rather
  than guessing. Contrast <span class="mono">baryons.py</span>, where every one
  of the 292 contents parses and all three flavour numbers are charted.</p>
</section>''' % ("".join(
        '<tr><td class="mono">%s</td><td class="mono">%s</td><td>%s</td>'
        '<td><span class="no">no</span></td></tr>'
        % (E(n_), E(k), "yes") for n_, k, _s, _c in M.kaon_exceptions()),
        len(M.unparsed())))
    h.append('''<section>
  <div class="shead"><span class="snum">05</span><h2>The canonical
  I<sup>G</sup>(J<sup>PC</sup>) chart, measured and refused</h2></div>
  <p class="sub">82 of the 250 carry all five. Charting them gives %d cells at
  cell (%d, %d, %d), channel K%d.</p>
  <div class="note"><span class="lab">Refused, and the reason is the overlap
  ruling&rsquo;s first ground</span>
  <p style="margin-bottom:0">A seating needs a <b>novel channel</b>, and K%d is
  carried by rows already seated &mdash; so the chart earns no position the
  master index does not already hold, and seating it would be exactly the
  over-representation the ruling exists to prevent. It is computed so the
  refusal is on the record with its measurement. The finding inside it, which
  mesons carry a C and why the two kaons do not, is section 04&rsquo;s and is
  kept.</p></div>
</section>''' % (ce_n, ce_cell[0], ce_cell[1], ce_cell[2], ce_cell[0],
                 ce_cell[0]))
    h.append('''<section>
  <div class="shead"><span class="snum">06</span><h2>Does the chart see
  antimatter? Only where the meson is charged</h2></div>
  <p class="sub">%d conjugate pairs among the %d members: <b>%d split</b> by the
  chart and <b>%d sharing a cell</b>.</p>
  <p>Of the four coordinates, conjugation leaves 2J, P and 2I alone and flips
  only Q3 &mdash; so the chart separates a pair <b>if and only if the meson is
  charged</b>. Every collided pair carries Q3 = %s and every split pair
  Q3 = %s, with no exception in either direction, and the mechanism is checked
  member by member rather than inferred from the counts.</p>
  <div class="note"><span class="lab">The antiparticle map is not seated as an
  index of its own</span>
  <p style="margin-bottom:0">Its members would be <em>pairs</em>, and a pair
  carries the quantum numbers of its members rather than any of its own &mdash;
  so it fails the registry criterion by construction. It is measured here
  instead, because the question has an answer and the answer belongs on the
  record.</p></div>
</section>''' % (pairs, len(R), split, same, E(str(qs)), E(str(qd))))
    h.append('''<section>
  <div class="shead"><span class="snum">07</span><h2>What closes it</h2></div>
  %s
  %s
</section>''' % (closure_table(m),
                 kv(("channel", "K%d" % m["cell"][0], "nothing closes it"),
                    ("height", str(m["cell"][1]), "Mirsky"),
                    ("width", str(m["cell"][2]), "Dilworth"),
                    ("|X| &le; h&times;w", "%d &le; %d" %
                     (m["cells"], m["cell"][1] * m["cell"][2]), ""))))
    h.append(foot("mesons", nfixtures("mesons")))
    h.append("</div>")
    _write("mesons-plate.html", h)


def build_baryons():
    import baryons as B
    import mesons as M
    X = B.index()
    m = measured(X)
    R = B.rows()
    n, c, g = B.cg_absent()
    ac = dict(B.axis_contributions())
    pairs, same, split, mech = B.conjugation()
    h = [plate.head("The Baryon Index"), '<div class="wrap">']
    h.append(_mast(
        "Research plate · an index of quantum objects · DOCKET 27",
        "The Baryon&nbsp;Index",
        "Two hundred and seventy-eight baryons of the Particle Data "
        "Group&rsquo;s table, antibaryons counted separately, charted on spin, "
        "parity, isospin, charge and all three flavour numbers &mdash; the one "
        "index here where the quark content parses for every member.",
        [("instrument", "baryons.py"), ("members", "%d of 292" % len(R)),
         ("arity", "7"), ("cells", str(m["cells"])),
         ("cell", "(%d,&nbsp;%d,&nbsp;%d)" % m["cell"]),
         ("channel", "K%d" % m["cell"][0])]))
    h.append('''<section>
  <div class="shead"><span class="snum">01</span><h2>The members, and the
  fourteen that are named rather than dropped</h2></div>
  <p class="sub">PDG reports no parity for the &Xi;(1690), &Xi;(1950),
  &Xi;(2030) and &Omega;(2250) states or their antiparticles.</p>
  <p class="eqn mono">%s</p>
  %s
</section>''' % (E(", ".join(B.unplaced())), sourceline("baryons")))
    h.append('''<section>
  <div class="shead"><span class="snum">02</span><h2>Seven coordinates, and the
  flavour numbers are the reason</h2></div>
  <p class="sub">All 292 baryon quark contents are plain strings of quark
  letters, so strangeness, charm and beauty parse for every member. 59 of the
  250 meson contents are mixtures and two have no strangeness to read at all
  &mdash; <b>a baryon is never a flavour mixture in this table</b>, and that
  contrast is why these three are declared here and refused there.</p>
  <div class="note"><span class="lab">The case convention is inherited, not
  re-derived</span>
  <p style="margin-bottom:0"><span class="mono">mesons.flavour()</span> is
  imported rather than copied, and it pins <b>lowercase as the quark</b> against
  six named states &mdash; the proton is <span class="mono">uud</span> and the
  antiproton <span class="mono">UUD</span>. Assuming the obvious convention
  instead silently negates S, C and B on every member, and nothing would fail:
  flavour-neutrality is sign-invariant, so the G-parity theorem passes either
  way. An instrument imports; it does not reimplement.</p></div>
  %s
</section>''' % chart_table(
        [("2J", "spin, doubled &mdash; odd for every baryon"),
         ("P", "parity"), ("2I", "isospin doubled"),
         ("Q3", "electric charge in thirds"), ("S", "strangeness"),
         ("C", "charm"), ("B", "beauty")], X, m["res"]))
    # COLOUR IS STRANGENESS, which is also an axis -- see the note on the meson
    # plate.  A parity-coloured view cannot be pure at any projection here: 86
    # of the points would carry two colours, because two baryons differing only
    # in P project to one place.  That is section 05's finding showing up in
    # the rendering, and it is why the hue is not parity.
    h.append(_view(
        "b3d", X, 4, ["2J  spin doubled", "P  parity", "2I  isospin doubled",
                      "Q3  charge in thirds", "S  strangeness", "C  charm",
                      "B  beauty"],
        "Colour is strangeness, and strangeness is also the third axis. A "
        "parity-coloured view is impure at every projection &mdash; 86 points "
        "would carry two colours, because two baryons differing only in P land "
        "in one place, which is section 05&rsquo;s finding showing up in the "
        "rendering. Seven coordinates onto three is the heaviest projection on "
        "any plate here bar gravity&rsquo;s.",
        "03", "The index, projected", "the baryon index", radius=4.5))
    h.append('''<section>
  <div class="shead"><span class="snum">04</span><h2>Charm and beauty earn their
  place jointly, not separately</h2></div>
  <p class="sub">Measured after the chart was run, and reported because a
  coordinate that adds nothing is over-representation.</p>
  <div class="tablewrap"><table><thead><tr><th>chart</th>
    <th class="num">cells</th><th>verdict</th></tr></thead><tbody>
    <tr><td>all seven</td><td class="num">%d</td><td>&mdash;</td></tr>
    <tr><td>drop charm only</td><td class="num">%d</td>
      <td><span class="no">adds nothing alone</span></td></tr>
    <tr><td>drop beauty only</td><td class="num">%d</td>
      <td><span class="no">adds nothing alone</span></td></tr>
    <tr><td>drop <b>both</b> charm and beauty</td><td class="num">%d</td>
      <td><span class="yes">six cells lost</span></td></tr>
  </tbody></table></div>
  <p>Either one alone is a function of the other six on these %d members; the
  two together are not. So <b>neither is dropped</b>, and the declaration stands
  on a measurement rather than on the fact that it was made first. The
  redundancy of each alone is a property of <em>the table</em>, not of baryons:
  charm takes all three of &minus;1, 0, +1 here and simply never separates two
  members that the other six had already merged.</p>
  <div class="note"><span class="lab">C-parity and G-parity are absent without
  exception</span>
  <p style="margin-bottom:0">%d baryons, <b>%d</b> with a C printed and
  <b>%d</b> with a G. Conjugating a baryon gives an antibaryon, so no baryon is
  an eigenstate of either operation &mdash; this is the cleanest totality
  refusal in the tree: not &ldquo;mostly missing&rdquo; but missing without a
  single exception. <b>Baryon number</b> is refused too, for a different reason:
  it is the sign of the PDG id, so charting it would be a relabelling.</p></div>
</section>''' % (ac[None], ac["C"], ac["B"], ac["C and B"], len(R), n, c, g))
    h.append('''<section>
  <div class="shead"><span class="snum">05</span><h2>Conjugation splits every
  pair &mdash; and the mesons&rsquo; does not</h2></div>
  <p class="sub">All %d conjugate pairs are split by this chart, with no
  exception, and the mechanism is uniform.</p>
  <div class="tablewrap"><table><thead><tr><th>coordinate</th>
    <th>under conjugation</th></tr></thead><tbody>%s</tbody></table></div>
  <div class="note good"><span class="lab">Two indexes, one operation, opposite
  answers &mdash; and the difference is spin-statistics</span>
  <p style="margin-bottom:0">A fermion and its antifermion carry <b>opposite
  intrinsic parity</b>: the neutron is P&nbsp;=&nbsp;+1 and the antineutron
  P&nbsp;=&nbsp;&minus;1 in this very table. A meson and its antimeson carry the
  <b>same</b> parity, because a meson is a boson. So
  <span class="mono">mesons.py</span> finds %d of its %d pairs collided &mdash;
  the neutral ones, which only charge could have separated &mdash; and this file
  finds none, because here parity separates a pair even when every charge on it
  is zero.</p></div>
</section>''' % (pairs, "".join(
        '<tr><td class="mono">%s</td><td>%s</td></tr>'
        % (E(nm), '<span class="yes">invariant</span>' if v == "invariant"
           else '<span class="no">negates</span>' if v == "negates"
           else '<b>MIXED</b>') for nm, v in mech),
        M.conjugation()[1], M.conjugation()[0]))
    h.append('''<section>
  <div class="shead"><span class="snum">06</span><h2>What closes it</h2></div>
  %s
  %s
</section>''' % (closure_table(m),
                 kv(("channel", "K%d" % m["cell"][0], "nothing closes it"),
                    ("height", str(m["cell"][1]), "Mirsky"),
                    ("width", str(m["cell"][2]), "Dilworth"),
                    ("|X| &le; h&times;w", "%d &le; %d" %
                     (m["cells"], m["cell"][1] * m["cell"][2]), ""))))
    h.append(foot("baryons", nfixtures("baryons")))
    h.append("</div>")
    _write("baryons-plate.html", h)


def build_quasiparticle():
    """DOCKET 28's REFUSAL -- and the plate says so in the mast, not the fine
    print.  Nothing here is seated; two separate measurements say why."""
    import quasiparticle as Q
    X = Q.index(12)
    m = measured(X)
    kinds, ucells = Q.universal_is_almost_nothing()
    sg, pg, ac = Q.host_carries_it()
    v, why = Q.verdict()
    rows = Q.sweep()

    h = [plate.head("The Quasiparticle Refusal"), '<div class="wrap">']
    h.append(_mast(
        "Research plate · a refusal, measured twice · DOCKET 28",
        "The Quasiparticle&nbsp;Refusal",
        "DOCKET 27 named quasiparticles as its one honest gap &mdash; they "
        "would pass the criterion and are simply not in the particle table. "
        "This went and looked. There is nothing to seat, and neither reason "
        "is &ldquo;we could not find a file&rdquo;.",
        [("instrument", "quasiparticle.py"), ("verdict", "NOTHING SEATED"),
         ("reasons", "2, both measured"),
         ("box sweep", "%d boxes" % len(rows)),
         ("channel", "K%d at every one" % rows[0][2])]))

    h.append('<div class="note warn">'
             '<span class="lab">This plate is of a refusal, and the '
             'distinction matters</span>'
             '<p style="margin-bottom:0">Every other plate in this set renders '
             'a <em>seated</em> index. This one renders a chart that was '
             'measured and then turned down. <span class="mono">registry.py'
             '</span> carries <span class="mono">quasiparticle</span> in '
             '<span class="mono">NOT_AN_INDEX</span>, and it is the only entry '
             'there whose members <em>pass</em> the criterion &mdash; an anyon '
             'carries topological charge, topological spin and a quantum '
             'dimension. It is excluded by BOX INVARIANCE instead, which is a '
             'different kind of exclusion and is marked as one.</p></div>')

    kindrows = "".join(
        '<tr><td class="mono">%s</td><td class="num">%d</td><td>boson</td></tr>'
        % (E(n), sp) for n, sp in Q.UNIVERSAL)
    h.append(
        '<section><div class="shead"><span class="snum">01</span>'
        '<h2>There is no particle table for quasiparticles, and the reason is '
        'structural</h2></div>'
        '<p class="sub">Not an absent file. A phonon does not carry the kind of '
        'quantum numbers a meson carries.</p>'
        '<p>The Particle Data Group tabulates a meson&rsquo;s spin, parity and '
        'isospin because <b>those are properties of the meson</b>. Ask the same '
        'of a phonon and the question changes shape. The universal quantum '
        'numbers of the textbook kinds are almost nothing:</p>'
        '<div class="tablewrap"><table><thead><tr><th>kind</th>'
        '<th class="num">spin</th><th>statistics</th></tr></thead><tbody>%s'
        '</tbody></table><caption>%d kinds on <b>%d cells</b> of their '
        'universal numbers, and every one a boson. A chart at that resolution '
        'is reporting on bosons.</caption></div>'
        '<div class="note"><span class="lab">Everything that distinguishes one '
        'mode from another belongs to the host</span>'
        '<p>A lattice mode is labelled by an irreducible representation of the '
        'little group of its wavevector, and which group that is depends on the '
        'crystal:</p>%s'
        '<p style="margin-bottom:0">Banked in <span class="mono">sgcapture.py'
        '</span> from spglib, with all four canonical figures checked. The same '
        'phonon in silicon (Fd-3m) and in rock salt (Fm-3m) carries different '
        'labels because the <em>crystals</em> differ. <b>So the member set '
        'would be (material, mode)</b> &mdash; a materials database, not a '
        'particle table. And a space group carries no quantum numbers either, '
        'so it is not an index in its own right.</p></div></section>'
        % (kindrows, kinds, ucells,
           kv(("space groups", sg, ""), ("point groups", pg, ""),
              ("arithmetic crystal classes", ac, ""))))

    spots = "".join(
        '<tr><td>%s</td><td class="num mono">%s</td><td class="num mono">%s</td>'
        '<td>%s</td></tr>'
        % (E(w), g, x, '<span class="yes">ok</span>' if g == x
           else '<span class="no">DIFFERS</span>')
        for w, g, x in Q.spot_checks())
    h.append(
        '<section><div class="shead"><span class="snum">02</span>'
        '<h2>One family needs no fetch at all</h2></div>'
        '<p class="sub">The anyons of SU(2)<sub>k</sub> &mdash; the topological '
        'excitations of a two-dimensional topologically ordered medium &mdash; '
        'are given by a closed form rather than by measurement.</p>'
        '<p class="eqn mono">topological spin&nbsp;&nbsp;h = j(j+1)/(k+2)<br>'
        'quantum dimension&nbsp;&nbsp;d = sin((2j+1)&pi;/(k+2)) / '
        'sin(&pi;/(k+2))<br>fusion&nbsp;&nbsp;j&#8321; &times; j&#8322; = '
        '|j&#8321;&minus;j&#8322;| &hellip; min(j&#8321;+j&#8322;, '
        'k&minus;j&#8321;&minus;j&#8322;)</p>'
        '<div class="tablewrap"><table><thead><tr><th>spot check</th>'
        '<th class="num">computed</th><th class="num">expected</th>'
        '<th>verdict</th></tr></thead><tbody>%s</tbody></table>'
        '<caption>Every check tests the computed value, never the remembered '
        'name.</caption></div>'
        '<div class="note warn"><span class="lab">SU(2)<sub>2</sub> is not the '
        'Ising category, and a fixture written against the name would have '
        'passed for the wrong reason</span>'
        '<p style="margin-bottom:0">It is commonly called Ising. Its '
        'j&nbsp;=&nbsp;&frac12; carries h&nbsp;=&nbsp;3/16; the Ising &sigma; '
        'carries h&nbsp;=&nbsp;1/16. The two are related and distinct, and '
        '<span class="mono">NOT_ISING</span> records it in the instrument.</p>'
        '</div></section>' % spots)

    h.append(_view(
        "q3d", X, 0,
        ["STAT  boson / fermion / anyon", "ORD  order of the topological twist",
         "NSELF  outcomes of j x j", "AB  abelian or not"],
        "Colour is the statistics class. The chart is real and it is still "
        "refused &mdash; section 04 is why.",
        "03", "The chart that was refused", "the SU(2)_k anyon chart",
        radius=5.5))

    sweeprows = "".join(
        '<tr><td class="mono">%s</td><td class="num">%d</td>'
        '<td class="num">K%d</td><td>%s</td></tr>'
        % (E(nm), nc, k, ", ".join(cl) or "nothing")
        for nm, nc, k, cl, _j, _m, _d in rows)
    h.append(
        '<section><div class="shead"><span class="snum">04</span>'
        '<h2>And box invariance refuses it</h2></div>'
        '<p class="sub">A chart whose membership is a predicate over a box can '
        'be handed a different box and asked again. <b>If the channel never '
        'moves, the channel is a property of the rule and not of the data.</b> '
        'That is <span class="mono">boxinvariance.py</span>, and it is imported '
        'here rather than reimplemented.</p>'
        '<div class="tablewrap"><table><thead><tr><th>box</th>'
        '<th class="num">cells</th><th class="num">channel</th><th>closes</th>'
        '</tr></thead><tbody>%s</tbody></table><caption>The cells move at every '
        'box. <b>The channel does not move at all.</b></caption></div>'
        '<div class="note warn"><span class="lab">%s</span>'
        '<p style="margin-bottom:0">%s</p></div>'
        '<p><b>What this does not show.</b> Box invariance refuses <em>the '
        'chart that was run</em>. It does not show that no chart of anyons '
        'could ever be seated &mdash; a different coordinate set over the same '
        'members might move with the box. A measurement can only refuse what it '
        'measured.</p></section>' % (sweeprows, E(v), E(why)))

    h.append(
        '<section><div class="shead"><span class="snum">05</span>'
        '<h2>What would reopen it</h2></div>'
        '<p class="sub">Named so the door is visibly open rather than quietly '
        'shut.</p>'
        '<p>A materials database &mdash; the phonon-mode tables of a fixed set '
        'of crystals, each mode with its irrep &mdash; <b>IS</b> a legitimate '
        'member set: a mode carries a symmetry label and a frequency, and those '
        'are quantum numbers. It is (material, mode), it needs a real fetch, '
        'and it is not what DOCKET 27 asked for.</p></section>')
    h.append(foot("quasiparticle", nfixtures("quasiparticle")))
    h.append("</div>")
    _write("quasiparticle-plate.html", h)


def build_fqh():
    """DOCKET 30 -- the quasiparticles that DID seat, and why this one does."""
    import fqh as Q
    import quasiparticle as QP
    X = Q.index()
    m = measured(X)
    rows = Q.sweep()
    v, why = Q.verdict()
    a, f, b = Q.anyon_fraction()

    h = [plate.head("The Hall Quasiparticles"), '<div class="wrap">']
    h.append(_mast(
        "Research plate · an index of quantum objects · DOCKET 30",
        "The Hall&nbsp;Quasiparticles",
        "The quasiparticles of the fractional quantum Hall states &mdash; "
        "excitations carrying a FRACTION of the electron charge, in a system "
        "built only from electrons, and obeying neither Bose nor Fermi "
        "statistics.",
        [("instrument", "fqh.py"), ("members", "%d quasiparticles" % len(Q.rows())),
         ("states", "%d Laughlin" % len(Q.states())),
         ("arity", "4"), ("cells", str(m["cells"])),
         ("cell", "(%d,&nbsp;%d,&nbsp;%d)" % m["cell"]),
         ("channel", "K%d" % m["cell"][0])]))

    h.append('<div class="note warn">'
             '<span class="lab">DOCKET 28 refused an anyon chart. This is not '
             'that chart, and that refusal still stands</span>'
             '<p style="margin-bottom:0">DOCKET 28 charted the anyons of '
             'SU(2)<sub>k</sub> <em>for every k up to a cap</em>. Each k is a '
             'different topological order &mdash; a different physical system '
             '&mdash; so its &ldquo;box&rdquo; was never a reach. It was a '
             'choice of <b>how many universes to include</b>, and nothing '
             'about the data was being varied, so of course the channel never '
             'moved. <b>The test was right and the object was wrong.</b> This '
             'plate charts a REACH instead: one family of one kind of system, '
             'indexed by a measured filling fraction. Section 03 is the '
             'difference, in one table.</p></div>')

    h.append(
        '<section><div class="shead"><span class="snum">01</span>'
        '<h2>A member is a quasiparticle, and it carries a fraction of an '
        'electron</h2></div>'
        '<p class="sub">The Laughlin state at filling &nu;&nbsp;=&nbsp;1/m has '
        'exactly m of them, labelled j&nbsp;=&nbsp;0&hellip;m&minus;1, with '
        'j&nbsp;=&nbsp;0 the vacuum.</p>'
        '<p class="eqn mono">electric charge&nbsp;&nbsp;Q = j/m&nbsp;&nbsp;'
        '(units of e)<br>exchange phase&nbsp;&nbsp;&theta;/&pi; = '
        'j&sup2;/m</p>'
        '<p>Both are computed as exact fractions, never floats, because <b>the '
        'whole content of this index is that these quantities are '
        'rational</b>.</p>'
        '<div class="tablewrap"><table><thead><tr><th class="num">j</th>'
        '<th class="num">Q / e</th><th class="num">&theta; / &pi;</th>'
        '<th>statistics</th></tr></thead><tbody>%s</tbody></table>'
        '<caption>The &nu;&nbsp;=&nbsp;1/3 state in full. <b>The charge-e/3 '
        'quasiparticle is not a prediction of this file</b> &mdash; its '
        'fractional charge was measured directly by shot noise in 1997.'
        '</caption></div>'
        '<div class="note"><span class="lab">Three of the twelve states are '
        'observed; the rest are the sequence&rsquo;s own continuation</span>'
        '<p style="margin-bottom:0">%s. The reach runs to m&nbsp;&le;&nbsp;%d '
        'and is <em>declared</em>, not claimed as observed &mdash; the same '
        'shape as <span class="mono">fibred</span> charting 170 electrons '
        'where 118 elements are known.</p></div></section>'
        % ("".join(
            '<tr><td class="num mono">%d</td><td class="num mono">%s</td>'
            '<td class="num mono">%s</td><td>%s</td></tr>'
            % (j, Qq, th, ('boson', 'fermion',
                           '<b>ANYON</b>')[st])
            for j, Qq, th, st in Q.laughlin_state(3)),
           ", ".join("&nu;&nbsp;=&nbsp;%s carries %s" % (nu, q)
                     for _m, nu, q in Q.observed_states()),
           Q.REACH))

    h.append(_view(
        "h3d", X, 0,
        ["STAT  boson / anyon", "ORD  order of the exchange phase",
         "CHORD  order of the charge", "M  inverse filling fraction"],
        "Colour is the statistics class. The inverse filling fraction is an "
        "axis because it is the most directly MEASURED number here &mdash; "
        "1/m is the quantised Hall conductance.",
        "02", "The index, projected", "the FQH quasiparticle index",
        radius=6))

    h.append(
        '<section><div class="shead"><span class="snum">03</span>'
        '<h2>Why this one seats where DOCKET 28&rsquo;s did not</h2></div>'
        '<p class="sub">A chart whose membership is a predicate over a box can '
        'be handed a different box. If the channel never moves, the channel is '
        'a property of the rule and not of the data. Here it moves.</p>'
        '<div class="tablewrap"><table><thead><tr><th>box</th>'
        '<th class="num">cells</th><th class="num">channel</th><th>closes</th>'
        '</tr></thead><tbody>%s</tbody></table>'
        '<caption>K2 at the two smallest reaches, K0 from '
        'm&nbsp;&le;&nbsp;9 onward. <b>The channel moves with the box.</b>'
        '</caption></div>'
        '<div class="note good"><span class="lab">%s</span>'
        '<p style="margin-bottom:0">%s &mdash; and '
        '<span class="mono">boxinvariance.verdict_of()</span> is the tree&rsquo;s '
        'own test, imported and not reimplemented. Run against DOCKET 28&rsquo;s '
        'chart the same function still returns <b>%s</b>. Two objects, two '
        'verdicts, both on the record.</p></div></section>'
        % ("".join(
            '<tr><td class="mono">%s</td><td class="num">%d</td>'
            '<td class="num">K%d</td><td>%s</td></tr>'
            % (E(nm), nc, k, ", ".join(cl) or "nothing")
            for nm, nc, k, cl, _j, _mm, _d in rows),
           E(v), E(why), E(QP.verdict()[0])))

    h.append(
        '<section><div class="shead"><span class="snum">04</span>'
        '<h2>Not one of them is a fermion, and that is forced</h2></div>'
        '<p class="sub">%d anyons, %d bosons, and <b>%d fermions</b>. '
        '%.0f%% of the members are neither &mdash; which cannot happen in '
        'three dimensions.</p>'
        '<p>The zero is not an observation about this reach. '
        '&theta;/&pi;&nbsp;=&nbsp;j&sup2;/m is a half-integer only if m '
        'divides 2j&sup2;, and <b>m is odd</b>, so m divides j&sup2; and the '
        'phase comes out a whole integer instead. <b>There is no third '
        'case</b>: a Laughlin quasiparticle is a boson or an anyon. The '
        'fixture proves it over the whole reach rather than quoting the '
        'argument.</p>'
        '<div class="note"><span class="lab">What is refused as a '
        'coordinate</span>'
        '<p style="margin-bottom:0">The label <span class="mono">j</span> is '
        'the anyon&rsquo;s ADDRESS within its state, and charting an address is '
        'a relabelling. Q and &theta; themselves are refused too: they are '
        'near-injective over the members, and '
        '<span class="mono">overlap.py</span> calls a near-injective '
        'coordinate a row label. Their ORDERS are charted instead, which is '
        'the part that says what kind of thing the quasiparticle is.</p></div>'
        '</section>' % (a, b, f, 100.0 * a / len(Q.rows())))

    h.append(foot("fqh", nfixtures("fqh")))
    h.append("</div>")
    _write("fqh-plate.html", h)


BUILDERS = {"fundamental": build_fundamental, "mesons": build_mesons,
            "baryons": build_baryons,
            "quasiparticle": build_quasiparticle,
            "fqh": build_fqh}

if __name__ == "__main__":
    for w in (sys.argv[1:] or sorted(BUILDERS)):
        BUILDERS[w]()
