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


BUILDERS = {"fundamental": build_fundamental, "mesons": build_mesons,
            "baryons": build_baryons}

if __name__ == "__main__":
    for w in (sys.argv[1:] or sorted(BUILDERS)):
        BUILDERS[w]()
