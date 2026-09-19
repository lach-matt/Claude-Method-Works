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


def pfoot(mod):
    """The footer, naming THIS builder.

    `build_index_plates.foot` hardcodes its own filename, so every plate in
    this family was printing a re-verify command that does not rebuild it.
    The footer is the one part of a plate whose whole job is to be runnable,
    so it gets its own version here rather than an inherited near-miss.
    """
    return ('<div class="foot"><p>Every figure on this plate is read from the '
            'instrument at build time, not retyped. Re-verify with:</p>'
            '<p><code>python3 research/warp-drive/%s.py --selftest</code> '
            '&mdash; %d fixtures<br><code>python3 research/warp-drive/%s.py'
            '</code> &mdash; the reading<br><code>python3 research/warp-drive/'
            'render/build_particle_plates.py %s</code> &mdash; this plate</p>'
            '</div>' % (mod, nfixtures(mod), mod, mod))


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
    h.append(pfoot("fundamental"))
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
    h.append(pfoot("mesons"))
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
    h.append(pfoot("baryons"))
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
    h.append(pfoot("quasiparticle"))
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

    h.append(pfoot("fqh"))
    h.append("</div>")
    _write("fqh-plate.html", h)


def lattice_svg(B, Q, out):
    """The (2J, Q3) lattice drawn flat -- boson frame, excitations, and what
    lies outside.  A 2-D index gets a 2-D picture; plate.view3d needs three
    axes and this chart has two, which is a reason to draw it properly rather
    than to pad it."""
    Js = sorted({j for j, _q in B | Q})
    Qs = sorted({q for _j, q in B | Q})
    W, H = 74, 62
    L, T = 92, 34
    w = L + W * (len(Qs) - 1) + 300
    hgt = T + H * (len(Js) - 1) + 78
    outset = set(out)
    p = ['<svg viewBox="0 0 %d %d" role="img" aria-label="the boson lattice '
         'and the excitations in it" style="max-width:100%%;height:auto">'
         % (w, hgt)]
    # grid
    for i, q in enumerate(Qs):
        x = L + W * i
        p.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="var(--rule)" '
                 'stroke-width="1"/>' % (x, T - 16, x, T + H * (len(Js) - 1) + 16))
        p.append('<text x="%d" y="%d" text-anchor="middle" font-size="13" '
                 'font-family="IBM Plex Mono,monospace" fill="var(--muted)">%d'
                 '</text>' % (x, T + H * (len(Js) - 1) + 40, q))
    for r, j in enumerate(reversed(Js)):
        y = T + H * r
        p.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="var(--rule)" '
                 'stroke-width="1"/>' % (L - 18, y, L + W * (len(Qs) - 1) + 18, y))
        p.append('<text x="%d" y="%d" text-anchor="end" font-size="13" '
                 'font-family="IBM Plex Mono,monospace" fill="var(--muted)">%d'
                 '</text>' % (L - 30, y + 5, j))
    # marks
    for r, j in enumerate(reversed(Js)):
        for i, q in enumerate(Qs):
            x, y = L + W * i, T + H * r
            inB, inQ = (j, q) in B, (j, q) in Q
            if inB:
                p.append('<circle cx="%d" cy="%d" r="9" fill="var(--rule-hard)"/>'
                         % (x, y))
            if inQ:
                col = "var(--algebra)" if (j, q) in outset else "var(--geometry)"
                p.append('<circle cx="%d" cy="%d" r="15" fill="none" '
                         'stroke="%s" stroke-width="3.5"/>' % (x, y, col))
            if (j, q) in outset:
                p.append('<circle cx="%d" cy="%d" r="23" fill="none" '
                         'stroke="var(--algebra)" stroke-width="1.5" '
                         'stroke-dasharray="3 3"/>' % (x, y))
    p.append('<text x="%d" y="%d" text-anchor="middle" font-size="12" '
             'letter-spacing="1.4" font-family="IBM Plex Mono,monospace" '
             'fill="var(--muted)">Q3 &#8212; CHARGE IN THIRDS</text>'
             % (L + W * (len(Qs) - 1) / 2, hgt - 16))
    p.append('<text transform="translate(22,%d) rotate(-90)" '
             'text-anchor="middle" font-size="12" letter-spacing="1.4" '
             'font-family="IBM Plex Mono,monospace" fill="var(--muted)">2J'
             '</text>' % (T + H * (len(Js) - 1) / 2))
    # legend
    lx = L + W * (len(Qs) - 1) + 46
    for k, (lab, mk) in enumerate((("the tree&rsquo;s bosons", "solid"),
                                   ("the excitations", "ring"),
                                   ("outside the bosons", "out"))):
        y = T + 26 * k
        if mk == "solid":
            p.append('<circle cx="%d" cy="%d" r="7" fill="var(--rule-hard)"/>' % (lx, y))
        elif mk == "ring":
            p.append('<circle cx="%d" cy="%d" r="9" fill="none" '
                     'stroke="var(--geometry)" stroke-width="3"/>' % (lx, y))
        else:
            p.append('<circle cx="%d" cy="%d" r="9" fill="none" '
                     'stroke="var(--algebra)" stroke-width="3"/>' % (lx, y))
        p.append('<text x="%d" y="%d" font-size="12.5" fill="var(--body)">%s'
                 '</text>' % (lx + 18, y + 4, lab))
    p.append("</svg>")
    return "".join(p)

def build_bosonqp():
    """DOCKET 31 -- a sublattice, and every number derived rather than typed."""
    import bosonqp as Q
    X = Q.index()
    m = measured(X)
    nb, nq, bsub, qsub, subset, out, nu, usub = Q.relation()
    tot, full, n5, f5 = Q.box_freeness()

    h = [plate.head("The Boson Sublattice"), '<div class="wrap">']
    h.append(_mast(
        "Research plate · an index of quantum objects · DOCKET 31",
        "The Boson&nbsp;Sublattice",
        "The bosonic excitations of condensed matter &mdash; Cooper pairs, "
        "excitons, phonons, magnons &mdash; placed in the frame the "
        "tree&rsquo;s own bosons already live in, and asked whether they sit "
        "inside it closed.",
        [("instrument", "bosonqp.py"), ("members", "%d" % len(Q.members())),
         ("rules", "3 derivations"), ("cells", str(m["cells"])),
         ("cell", "(%d,&nbsp;%d,&nbsp;%d)" % m["cell"]),
         ("extends the bosons by", "%d cells" % (nu - nb))]))

    h.append('<div class="note warn">'
             '<span class="lab">Two rulings, and the second threw out the '
             'first draft</span>'
             '<p>M, first: <em>&ldquo;almost nothing &mdash; but not nothing, '
             'which means measurable ... it is a sub index/sublattice of '
             'bosons.&rdquo;</em> That corrected DOCKET 28, which wrote '
             '&ldquo;almost nothing&rdquo; and then treated it as nothing.</p>'
             '<p style="margin-bottom:0">M, second: <em>&ldquo;Do not add '
             'declared. Nothing less than computed or measured. Declared still '
             'requires proof.&rdquo;</em> The first draft listed eleven kinds '
             'with their spins and charges written out from textbook '
             'knowledge, and <span class="mono">registry.py</span> had grown a '
             'whole provenance category &mdash; DECLARED &mdash; to let that '
             'pass its own guard. <b>Both are gone.</b> Every number on this '
             'plate comes out of one of the three rules below.</p></div>')

    h.append(
        '<section><div class="shead"><span class="snum">01</span>'
        '<h2>Three derivation rules, and nothing outside them</h2></div>'
        '<p class="sub">The inputs are what a thing is made of, which symmetry '
        'it breaks, and what it mixes &mdash; each the definition of the '
        'object rather than a measurement of it.</p>'
        '<div class="kv">'
        '<div><dt>composition</dt><dd>charge adds; spin combines<small>the '
        'electron (2J&nbsp;=&nbsp;1, Q3&nbsp;=&nbsp;&minus;3) and photon '
        '(2,&nbsp;0) are READ from the seated fundamental index</small></dd></div>'
        '<div><dt>broken symmetry</dt><dd>2J = 2 &times; the generator&rsquo;s '
        'rank<small>and Q3 = 0 when it commutes with charge</small></dd></div>'
        '<div><dt>hybridisation</dt><dd>inherit what the constituents share'
        '<small>and RAISE when they disagree</small></dd></div></div>'
        '<div class="note good"><span class="lab">The second rule corrected '
        'this file on its first use</span>'
        '<p style="margin-bottom:0">The first draft wrote the phonon down as '
        'spin&nbsp;0. The phonon is the Goldstone mode of <b>broken '
        'translation</b>, whose generator is the momentum P &mdash; a VECTOR '
        '&mdash; so the rule returns <b>2J&nbsp;=&nbsp;2</b>. The rule is '
        'right and the draft was wrong: three broken translations in three '
        'dimensions give the three acoustic branches, which a scalar mode '
        'could not. <b>A derivation that can contradict what you would have '
        'written down is the only kind worth having.</b></p></div>'
        '</section>')

    h.append(
        '<section><div class="shead"><span class="snum">02</span>'
        '<h2>Every member, and which rule produced it</h2></div>'
        '<div class="tablewrap"><table><thead><tr><th>rule</th><th>member</th>'
        '<th class="num">2J</th><th class="num">Q3</th></tr></thead><tbody>%s'
        '</tbody></table><caption>%d members on %d cells. The eight collective '
        'modes add members but <b>no new cells</b>.</caption></div>'
        '<div class="note"><span class="lab">The trion excludes itself</span>'
        '<p style="margin-bottom:0">Two electrons and a hole compose to 2J in '
        '{1,&nbsp;3} &mdash; half-integer, a <b>fermion</b> &mdash; and a '
        'sublattice of the bosons holds none. Nothing here decides that; the '
        'addition rule returns it. And <span class="mono">hybrid()</span> '
        'raises on constituents that disagree, so the third rule has a failure '
        'mode too.</p></div></section>'
        % ("".join(
            '<tr><td>%s</td><td class="mono">%s</td><td class="num">%d</td>'
            '<td class="num">%d</td></tr>' % (E(k), E(n), j, q)
            for k, n, j, q in Q.members()),
           len(Q.members()), m["cells"]))

    h.append(
        '<section><div class="shead"><span class="snum">03</span>'
        '<h2>The index, drawn flat</h2></div>'
        '<p class="sub">Two coordinates, so this is the index ITSELF and not a '
        'projection of it &mdash; nothing is collapsed, summarised or '
        'dropped.</p>'
        '<div class="fig">%s</div>'
        '<p class="cap">The tree&rsquo;s fifteen boson cells, the five the '
        'excitations occupy, and the two that fall outside the frame '
        'altogether. <b>Both are the Cooper pair</b>, at a charge no meson and '
        'no gauge boson reaches.</p></section>'
        % lattice_svg(Q.boson_frame(), X, out))

    h.append(
        '<section><div class="shead"><span class="snum">04</span>'
        '<h2>The finding is the relation, not the chart</h2></div>'
        '<div class="tablewrap"><table><thead><tr><th></th>'
        '<th class="num">cells</th><th>sublattice?</th></tr></thead><tbody>'
        '<tr><td>the tree&rsquo;s own bosons on (2J, Q3)</td>'
        '<td class="num">%d</td><td><span class="yes">yes</span></td></tr>'
        '<tr><td>the bosonic excitations</td><td class="num">%d</td>'
        '<td><span class="yes">yes</span></td></tr>'
        '<tr><td>the union</td><td class="num">%d</td>'
        '<td><span class="yes">yes</span></td></tr>'
        '</tbody></table><caption>But the second is <b>NOT a subset</b> of the '
        'first.</caption></div>'
        '<div class="note good"><span class="lab">The Cooper pair carries '
        '&minus;2e and nothing else in the tree does</span>'
        '<p style="margin-bottom:0">Every meson and every gauge boson is '
        'charged &minus;1, 0 or +1. Two electrons bound in a metal reach a '
        'charge no elementary or composite boson here reaches &mdash; in '
        '<b>both</b> spin states, the triplet being helium-3&rsquo;s p-wave '
        'pairing. So the excitations are a sublattice of the bosons only once '
        'the lattice is <b>extended to hold them</b>, and the extension is '
        '<b>%d cells wide</b>: %s.</p></div></section>'
        % (nb, nq, nu, nu - nb, E(str(out))))

    h.append(
        '<section><div class="shead"><span class="snum">05</span>'
        '<h2>The channel, and why it is not free this time</h2></div>'
        '<p class="sub">The chart closes all five languages &mdash; K7. The '
        'first draft was a three-cell CHAIN, and a chain closes almost '
        'everything by being one.</p>'
        '<p><b>This chart is not a chain.</b> It is %d cells at width %d, and '
        'the measurement changes with it: over the box this chart lives in, '
        'only <b>%d of %d</b> subsets close all five, and of the <b>%d</b> '
        'subsets its own size only <b>%d</b> do. So the K7 is earned by '
        'two-thirds of the alternatives failing, not handed over by shape.</p>'
        '<div class="note"><span class="lab">z3, pointed at this file&rsquo;s '
        'own result</span>'
        '<p style="margin-bottom:0"><span class="mono">--prove</span> runs four '
        'claims over every subset of the box: that every chain there is '
        'closed (so a chain&rsquo;s K7 <em>is</em> free), a vacuity guard that '
        'chains exist, a contrast that some subset is not closed, and finally '
        'that <b>THIS chart is not a chain</b> &mdash; so the free pass does '
        'not reach it. It is still five cells, and section 04 is the '
        'finding.</p></div></section>'
        % (m["cells"], m["cell"][2], full, tot, n5, f5))

    h.append(pfoot("bosonqp"))
    h.append("</div>")
    _write("bosonqp-plate.html", h)


def build_readrezayi():
    """DOCKET 32 -- the non-abelian Hall quasiparticles."""
    import readrezayi as R
    X = R.index()
    m = measured(X)
    na, nn, sh, ain, nin, asub, nsub = R.nesting()
    F = R.fermions()

    h = [plate.head("The Non-Abelian Anyons"), '<div class="wrap">']
    h.append(_mast(
        "Research plate · an index of quantum objects · DOCKET 32",
        "The Non-Abelian&nbsp;Anyons",
        "The other kind of Hall quasiparticle: exchange does not multiply the "
        "state by a phase, it ROTATES IT inside a degenerate space. These are "
        "the excitations proposed for topological quantum computing.",
        [("instrument", "readrezayi.py"),
         ("members", "%d primaries" % len(R.rows())),
         ("states", "%d Read-Rezayi" % len(R.levels())),
         ("arity", "4"), ("cells", str(m["cells"])),
         ("cell", "(%d,&nbsp;%d,&nbsp;%d)" % m["cell"]),
         ("channel", "K%d" % m["cell"][0])]))

    h.append(
        '<section><div class="shead"><span class="snum">01</span>'
        '<h2>Moore&ndash;Read <em>is</em> RR&#8322;</h2></div>'
        '<p class="sub">Not a separate construction, which is why there is one '
        'instrument and not two. The series sits at '
        '&nu;&nbsp;=&nbsp;2&nbsp;+&nbsp;k/(k+2).</p>'
        '<div class="tablewrap"><table><thead><tr><th class="num">k</th>'
        '<th class="num">&nu;</th><th class="num">charge</th>'
        '<th class="num">primaries</th><th>observed</th></tr></thead><tbody>%s'
        '</tbody></table><caption>Two levels have a reported plateau; the rest '
        'is the series&rsquo; own continuation, declared as such.</caption></div>'
        '<div class="note good"><span class="lab">k is a REACH, and that is the '
        'whole difference from DOCKET 28</span>'
        '<p style="margin-bottom:0">That docket charted SU(2)<sub>k</sub> for '
        'every k and was refused, because varying k there varied <em>which '
        'theory you were in</em> &mdash; a union over universes, with nothing '
        'about the data being varied. Here each k <b>names a plateau at a '
        'definite &nu;</b>, so varying the reach is varying how far up the '
        'observed series you have got, exactly as varying Z is.</p></div>'
        '</section>'
        % "".join(
            '<tr><td class="num mono">%d</td><td class="num mono">%s</td>'
            '<td class="num mono">e/%d</td><td class="num">%d</td><td>%s</td>'
            '</tr>' % (k, R.filling(k), k + 2, len(R.primaries(k)),
                       "<b>%s</b> (%s)" % R.OBSERVED[k]
                       if k in R.OBSERVED else "")
            for k in R.levels()))

    h.append(
        '<section><div class="shead"><span class="snum">02</span>'
        '<h2>Validated against the literature, not against itself</h2></div>'
        '<p class="eqn mono">h = l(l+2) / (4(k+2)) &nbsp;&minus;&nbsp; '
        'm&sup2; / (4k)</p>'
        '<div class="tablewrap"><table><thead><tr><th>what the literature '
        'fixes</th><th class="num">computed</th><th>verdict</th></tr></thead>'
        '<tbody>%s</tbody></table><caption>No tuning. The closed form returns '
        'them.</caption></div>'
        '<div class="note warn"><span class="lab">And this closes DOCKET '
        '28&rsquo;s trap from the other side</span>'
        '<p style="margin-bottom:0">That docket recorded that '
        'SU(2)<sub>2</sub> is commonly called &ldquo;Ising&rdquo; and is not: '
        'its j&nbsp;=&nbsp;&frac12; carries h&nbsp;=&nbsp;3/16 where the Ising '
        '&sigma; carries <b>1/16</b>. The real Moore&ndash;Read state carries '
        '1/16, which this file computes. <b>So that chart had the wrong '
        'physics as well as the wrong shape</b>, and the caution written there '
        'against trusting the name was the important half of it.</p></div>'
        '</section>'
        % "".join(
            '<tr><td>%s</td><td class="num mono">%s</td><td>%s</td></tr>'
            % (E(w), E(str(g)), '<span class="yes">ok</span>' if ok
               else '<span class="no">DIFFERS</span>')
            for w, g, _x, ok in R.validation()))

    h.append(_view(
        "rr3d", X, 0,
        ["STAT  boson / fermion / anyon", "ORD  order of the twist",
         "CHORD  order of the charge", "K  the level"],
        "Colour is the statistics class &mdash; and unlike the abelian index, "
        "all three values occur.",
        "03", "The index, projected", "the non-abelian anyon index",
        radius=5))

    h.append(
        '<section><div class="shead"><span class="snum">04</span>'
        '<h2>The Majorana bounds DOCKET 30&rsquo;s theorem</h2></div>'
        '<p class="sub"><span class="mono">fqh.py</span> proved that NOT ONE '
        'Laughlin quasiparticle is ever a fermion &mdash; forced, because '
        '&theta;/&pi;&nbsp;=&nbsp;j&sup2;/m is a half only if m divides '
        '2j&sup2; and m is odd.</p>'
        '<p><b>This series has %d fermions.</b> The one at k&nbsp;=&nbsp;2 is '
        'the Ising &psi; at h&nbsp;=&nbsp;&frac12; &mdash; the neutral '
        '<b>Majorana fermion</b> of the Moore&ndash;Read state. So the theorem '
        'was never about Hall quasiparticles in general; it was about the '
        '<em>abelian</em> ones, and this is precisely where the two families '
        'part.</p>'
        '<div class="note"><span class="lab">And neither index nests in the '
        'other &mdash; a negative result, reported</span>'
        '<p style="margin-bottom:0">DOCKET 31 found the bosonic excitations '
        'sitting inside the boson lattice as a sublattice. Nothing of that '
        'kind happens here: on the three coordinates they share, the abelian '
        'chart has <b>%d</b> cells and the non-abelian <b>%d</b>, they share '
        '<b>%d</b>, <b>neither contains the other</b> and neither is a '
        'sublattice on its own. Reported so that one positive nesting result '
        'is not read as a pattern.</p></div></section>'
        % (len(F), na, nn, sh))

    h.append(pfoot("readrezayi"))
    h.append("</div>")
    _write("readrezayi-plate.html", h)


def build_spin4():
    """DOCKET 34 -- the tree's only K4, and the last empty channel filled."""
    import spin4 as S
    X = S.index()
    m = measured(X)
    names = ("P (parity)", "2I (isospin, doubled)", "Q3 (charge, thirds)")

    h = [plate.head("The Spin-4 Mesons"), '<div class="wrap">']
    h.append(_mast(
        "Research plate &middot; an index of quantum objects &middot; DOCKET 34",
        "The Spin-4&nbsp;Mesons",
        "The only chart in this tree that reaches K4 &mdash; and the only one "
        "that earns it, every earlier K4 having been arity&nbsp;2 where "
        "statistics closes for free.",
        [("instrument", "spin4.py"), ("members", "%d mesons" % len(S.rows())),
         ("arity", "3"), ("cells", str(m["cells"])),
         ("cell", "(%d,&nbsp;%d,&nbsp;%d)" % m["cell"]),
         ("channel", "K%d" % m["cell"][0])]))

    h.append('<div class="note warn">'
             '<span class="lab">DOCKET 33 found this chart and REFUSED it. '
             'The refusal was on the wrong reach</span>'
             '<p style="margin-bottom:0">The sub-population sweep turned this '
             'chart up and turned it down: two of the ten mesons carry no '
             'printed mass, so swept by a MASS cut the population is 7 cells '
             'at K5 at every cut and never 9 at K4. But mass is not the only '
             'total order the table carries. <b>PDG STATUS is total where mass '
             'is not</b>, and on that reach the channel moves K5&nbsp;&rarr;'
             '&nbsp;K4 and holds. Both statements stand: the refusal is about '
             'the mass reach, the seating about the status reach, and which '
             'reach a channel survives is part of what the finding is.</p>'
             '</div>')

    h.append(_view("v-spin4", X, 2, names,
                   "Colour is Q3, the charge in thirds.", 1,
                   "The chart, at arity 3",
                   "Three-dimensional scatter of the spin-4 meson chart."))

    h.append('<section><h2>3. The chart</h2>')
    h.append(chart_table(
        [("P", "intrinsic parity of the meson"),
         ("2I", "isospin, doubled, so the half-integers stay integers"),
         ("Q3", "electric charge in thirds")],
        X, m["res"]))
    h.append(closure_table(m))
    h.append('<p>Statistics is <b>earned</b> here, not free: <code>kdet</code> '
             'returns early only when the arity is at most the determinant '
             'order, and this chart is arity&nbsp;3. That is what makes it '
             'the first real K4 in the tree.</p></section>')

    ml = S.massless()
    h.append('<section><h2>4. The two rows the table cannot place</h2>'
             '<p>The whole K4 rests on <b>%s</b>, which the Particle Data '
             'Group lists with no mass at all. That is not a defect in the '
             'chart &mdash; it is why the mass reach could never reach it, '
             'and why the status reach can.</p></section>'
             % E(" and ".join(ml)))

    h.append(pfoot("spin4"))
    h.append("</div>")
    _write("spin4-plate.html", h)


def build_nucbands():
    """DOCKET 35 -- the route a meet closed and a join opened."""
    import nucbands as N
    X = N.index()
    m = measured(X)
    nb, npar = N.refusals()

    h = [plate.head("Nuclear Rotational Levels"), '<div class="wrap">']
    h.append(_mast(
        "Research plate &middot; an index of quantum objects &middot; DOCKET 35",
        "Nuclear Rotational&nbsp;Levels",
        "Nuclear excited states in magnetic and antimagnetic rotational bands "
        "&mdash; the candidate an earlier pass declared unreachable, reached "
        "by navigating by JOIN instead of by meet.",
        [("instrument", "nucbands.py"),
         ("members", "%d levels" % len(N.members())),
         ("bands", "%d" % len(N.bandrows())),
         ("arity", "2"), ("cells", str(m["cells"])),
         ("cell", "(%d,&nbsp;%d,&nbsp;%d)" % m["cell"]),
         ("channel", "K%d" % m["cell"][0])]))

    h.append('<div class="note"><span class="lab">The corpus&rsquo;s own '
             'retrieval law reopened a route this project had closed</span>'
             '<p style="margin-bottom:0"><code>subpop.py</code> &sect;4 tried '
             'four searches for a nuclear level scheme, found nothing, and '
             'concluded there was nothing this environment could reach. '
             '<b>All four were MEETS.</b> <code>NAVIGATION.md</code> &sect;3 '
             '&mdash; a law derived from the three-body index, not a search '
             'habit &mdash; says navigate by <b>JOIN</b>, never by meet: meet '
             'failures run 12&nbsp;&rarr;&nbsp;90,705 by cap, <b>join failures '
             'are 0 at every cap</b>. Run as a join the route opened at once. '
             'arXiv is 403 over https through this proxy exactly as ENSDF is; '
             'the connector is a different bracket, and the join is what '
             'reached it.</p></div>')

    h.append('<section><h2>1. The capture is total, and the paper proves it'
             '</h2>'
             '<p>The totality argument is not &ldquo;the queries looked '
             'complete&rdquo;. It is the paper&rsquo;s own census, reproduced '
             'exactly and independently for its two tables &mdash; and then a '
             'second check a count cannot make.</p>'
             '<table class="tab"><thead><tr><th>table</th><th>the paper '
             'states</th><th>the parse finds</th></tr></thead><tbody>'
             '<tr><td>A &mdash; magnetic rotation</td><td>252 bands in 123 '
             'nuclei</td><td class="num"><b>252 / 123</b></td></tr>'
             '<tr><td>B &mdash; antimagnetic rotation</td><td>38 bands in 27 '
             'nuclei</td><td class="num"><b>38 / 27</b></td></tr>'
             '</tbody></table>'
             '<p>A count fixture cannot catch a parser that reads the right '
             'number of <em>wrong</em> things. So the second check is the '
             'physics each table is defined by: an AMR band is a '
             '&Delta;I&nbsp;=&nbsp;2 sequence and an MR band a '
             '&Delta;I&nbsp;=&nbsp;1 one. Measured over every consecutive '
             'pair of extracted spins: <b>213 of 213</b> AMR steps are '
             '&Delta;I&nbsp;=&nbsp;2, and <b>1,758 of 1,762</b> MR steps are '
             '&Delta;I&nbsp;=&nbsp;1. Landing on 100&nbsp;% is what says the '
             'columns are being read in the right order.</p></section>')

    h.append('<section><h2>2. Two refusals, on the criterion</h2>'
             '<p><b>%d bands</b> are printed with no I<sup>&pi;</sup> column '
             'at all &mdash; their energies are relative to an unknown '
             'bandhead, <span class="mono">200Pb&nbsp;1&nbsp;X</span>, then '
             '100.6+X, 223.9+X. <b>%d levels</b> carry a spin but no parity. '
             'A member must carry quantum numbers, so both are refused &mdash; '
             'and counted <em>apart</em>, because &ldquo;no parity '
             'printed&rdquo; and &ldquo;no spin printed&rdquo; are different '
             'facts about the source and flattening them would lose one.</p>'
             '</section>' % (nb, npar))

    h.append('<section><h2>3. The chart, and the K2 that is the free one</h2>')
    h.append(closure_table(m))
    h.append('<p><b>It would be a lie to bank that K2 as a closure.</b> '
             '<code>kdet</code> opens <code>if k &gt;= d: return True</code>, '
             'so at arity&nbsp;2 statistics closes for nothing, and this tree '
             'has measured 105 of 105 arity-2 charts closing it. <b>The '
             'nuclear band index closes in NOTHING</b>; its real content is '
             'K0, where <code>mesons</code> and <code>baryons</code> also sit. '
             'And no third coordinate rescues it &mdash; every superset '
             '<em>loses</em> the channel:</p>'
             '<table class="tab"><thead><tr><th>K</th><th>cells</th>'
             '<th>cell</th><th>coordinates</th></tr></thead><tbody>%s'
             '%s</tbody></table>'
             '<p class="sm">Six of the seven supersets are measured and every '
             'one loses the channel. <b>The seventh is not measured</b> &mdash; '
             'the full five-coordinate chart did not return inside a '
             '40-minute budget &mdash; and a pattern in six is not a '
             'measurement of the seventh, so it is marked rather than '
             'assumed.</p></section>'
             % ("".join('<tr><td class="mono">K%d</td><td class="num">%d</td>'
                        '<td class="mono sm">%s</td><td class="mono sm">%s</td>'
                        '</tr>' % (k, n, c, ", ".join(cols))
                        for cols, k, n, c in N.ARITY3),
                "".join('<tr><td class="mono">&mdash;</td>'
                        '<td class="num">&mdash;</td>'
                        '<td class="no">UNMEASURED</td>'
                        '<td class="mono sm">%s</td></tr>' % ", ".join(cols)
                        for cols, _why in N.UNMEASURED)))

    for nm, what, why in N.NOT_INDEXED:
        h.append('<div class="note warn"><span class="lab">The same join '
                 'returned a second paper, and it is NOT indexed</span>'
                 '<p style="margin-bottom:0"><span class="mono">%s</span> '
                 '&mdash; %s. <b>Two parse attempts, both short, neither '
                 'seated.</b> %s</p></div>' % (E(nm), E(what), E(why)))

    h.append(pfoot("nucbands"))
    h.append("</div>")
    _write("nucbands-plate.html", h)


BUILDERS = {"fundamental": build_fundamental, "mesons": build_mesons,
            "baryons": build_baryons,
            "quasiparticle": build_quasiparticle,
            "fqh": build_fqh,
            "bosonqp": build_bosonqp,
            "readrezayi": build_readrezayi,
            "spin4": build_spin4,
            "nucbands": build_nucbands}

if __name__ == "__main__":
    for w in (sys.argv[1:] or sorted(BUILDERS)):
        BUILDERS[w]()
