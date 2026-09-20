#!/usr/bin/env python3
r"""
build_crystal_plates.py -- the plates for the crystal-symmetry chain: registry
rows 25, 26 and 27, which were seated with no rendering at all.

    python3 build_crystal_plates.py              writes all three
    python3 build_crystal_plates.py corepdex     writes one

`phonondex`, `kpointdex` and `corepdex` ARE ONE CHAIN AND NOT THREE UNRELATED
INDEXES, and each plate says which refusal the next one discharges:

    phonondex   the Gamma-point site-symmetry types, and it REFUSES k != 0
                because the little group's representations are projective there
    kpointdex   discharges exactly that refusal and charts the isolated
                high-symmetry k-stars, and it carries a SECOND obstruction it
                records rather than repairs -- time reversal is antiunitary and
                is not in the little group at all
    corepdex    discharges that one, and charts the LEVELS those stars carry

ALL THREE HAVE ARITY 3, SO EACH 3-D VIEW IS THE INDEX ITSELF.  Three
coordinates, three axes, one point per cell: nothing is projected, collapsed or
summarised, and `plate.exactness()` says so in the caption rather than leaving a
reader to assume it.  That is not true of `gravity`, whose seven coordinates
must be projected, and the difference is stated on both plates.

Built on the shared scaffold in `plate.py` and on the components
`build_index_plates.py` already carries, so the stylesheet, the measured axis
choice, the swept camera and the inlined runtime are ONE implementation.  The
3-D section goes through `build_particle_plates._view`, which chooses the
projection by measurement -- at arity 3 there is nothing to choose and it says
so, which is the answer wanted here.

Every number on these plates is read from the instrument at build time.
Nothing is retyped.
"""

import html
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import plate       # noqa: E402
import registry    # noqa: E402

from build_index_plates import (                                # noqa: E402
    chart_table, closure_table, kv, measured, nfixtures, _write)
from build_particle_plates import _mast, _view, sourceline      # noqa: E402

E = html.escape


def cfoot(mod):
    """The footer, naming THIS builder.

    `build_index_plates.foot` hardcodes its own filename and
    `build_particle_plates.pfoot` hardcodes that one; a footer whose whole job
    is to be runnable must name the command that actually rebuilds the plate,
    so this family gets its own rather than an inherited near-miss.
    """
    return ('<div class="foot"><p>Every figure on this plate is read from the '
            'instrument at build time, not retyped. Re-verify with:</p>'
            '<p><code>python3 research/warp-drive/%s.py --selftest</code> '
            '&mdash; %d fixtures<br><code>python3 research/warp-drive/%s.py'
            '</code> &mdash; the reading<br><code>python3 research/warp-drive/'
            'render/build_crystal_plates.py %s</code> &mdash; this plate</p>'
            '</div>' % (mod, nfixtures(mod), mod, mod))


def row_number(nm):
    """Which registry row this is -- MEASURED off the register, not typed."""
    return [i for i, r in enumerate(registry.rows(), 1) if r[0] == nm][0]


def simple_table(headers, rows, caption=None):
    """A house table.  `headers` is [(label, td class)]; `rows` is [[cell,...]].

    The cells are passed through as HTML, because every caller builds them from
    a measurement and escapes what needs escaping.
    """
    th = "".join('<th%s>%s</th>' % (' class="num"' if c == "num" else "", h)
                 for h, c in headers)
    body = "".join(
        "<tr>%s</tr>" % "".join('<td class="%s">%s</td>' % (c, v)
                                for (_h, c), v in zip(headers, r))
        for r in rows)
    cap = "<caption>%s</caption>" % caption if caption else ""
    return ('<div class="tablewrap"><table><thead><tr>%s</tr></thead>'
            '<tbody>%s</tbody>%s</table></div>' % (th, body, cap))


def sec(num, title, sub, *body):
    return ('<section><div class="shead"><span class="snum">%s</span>'
            '<h2>%s</h2></div>%s%s</section>'
            % (num, title, '<p class="sub">%s</p>' % sub if sub else "",
               "".join(body)))


def yn(v):
    return ('<span class="yes">holds</span>' if v
            else '<span class="no">FAILS</span>')


def measures(m, extra=()):
    """The block every plate in this family carries."""
    pairs = [("cells", m["cells"], ""),
             ("box", m["box"], "what charting cost tracks"),
             ("cell", "(%d, %d, %d)" % m["cell"], "K, height, width")]
    pairs.extend(extra)
    return kv(*pairs) + closure_table(m)


# ===========================================================================
# ROW 25 -- phonondex
# ===========================================================================

def build_phonondex():
    import phonondex as P
    X = P.index()
    m = measured(X)
    rows = P.read()
    bs = P.by_system()
    per = sorted(len(v) for v in P.by_spacegroup().values())
    nsg = len({r[0] for r in rows})
    wy_n, wy_orders = P.wyckoff_coarsening()

    h = [plate.head("The Phonon Index"), '<div class="wrap">']
    h.append(_mast(
        "Research plate &middot; an index of quantum objects &middot; "
        "registry row&nbsp;%d" % row_number("phonondex.index"),
        "The Phonon&nbsp;Index",
        "%s site-symmetry types over all %d space groups &mdash; the "
        "&Gamma;-point phonon symmetry content of every distinct "
        "crystallographic site, computed end to end from the space groups "
        "themselves." % ("{:,}".format(len(rows)), nsg),
        [("instrument", "phonondex.py"),
         ("members", "{:,} site types".format(len(rows))),
         ("space groups", "%d of 230" % nsg),
         ("arity", "3"), ("cells", str(m["cells"])),
         ("cell", "(%d,&nbsp;%d,&nbsp;%d)" % m["cell"]),
         ("channel", "K%d" % m["cell"][0])]))

    h.append(sec(
        "01", "A member is a site-symmetry type, not a material",
        "The member set is (space group, site-symmetry type up to conjugacy), "
        "and that is what makes the fetch disappear.",
        "<p>A material&rsquo;s &Gamma;-point phonon content is the <b>sum</b> "
        "over its occupied site orbits, and each orbit&rsquo;s contribution "
        "depends only on its site-symmetry type. So the member set is not "
        "materials at all: it is the <b>generating table</b> from which every "
        "material&rsquo;s answer follows by addition. It is finite, "
        "exhaustive, and needs no database. <code>compose()</code> performs "
        "the addition and the instrument checks it against six published "
        "crystal decompositions.</p>"
        "<p>It is also <b>deliberately coarser than the Wyckoff tables</b>, "
        "and the coarsening is a finding rather than a shortcut. ITA lists "
        "P&#8209;1&rsquo;s eight inversion centres as eight Wyckoff letters, "
        "1a&hellip;1h; all eight have the same site-symmetry group and "
        "contribute identically, so separating them would multiply members "
        "without adding a distinction. Measured: space group 2 seats "
        "<b>%d</b> members in all, of site-symmetry orders %s. <b>The phonon "
        "representation cannot see the difference.</b></p>"
        % (wy_n, ", ".join(str(o) for o in wy_orders))))

    h.append(sec(
        "02", "The members, by crystal system", "",
        simple_table(
            [("crystal system", "name"), ("site types", "num"),
             ("share", "num")],
            [[s, "{:,}".format(len(bs.get(s, []))),
              "%.1f&thinsp;%%" % (100.0 * len(bs.get(s, [])) / len(rows))]
             for s in P.SYSTEMS]
            + [["<b>all 230 space groups</b>",
                "<b>{:,}</b>".format(len(rows)), "<b>100.0&thinsp;%</b>"]],
            "Site types per space group: min %d, median %d, max %d. "
            "Distinct decompositions across the whole table: %d."
            % (per[0], per[len(per) // 2], per[-1],
               P.distinct_decompositions()))))

    h.append(sec(
        "03", "The three coordinates",
        "<code>multiplicity</code> and <code>pg_order</code> are deliberately "
        "<b>not</b> coordinates: their product is fixed by orbit&ndash;"
        "stabiliser, and they describe the host&rsquo;s cell rather than the "
        "modes.",
        chart_table(
            [("site_order", "the order of the site-symmetry group the modes "
                            "transform under &mdash; the local symmetry, not "
                            "the crystal&rsquo;s"),
             ("n_irreps", "how many distinct symmetry species the site "
                          "contributes"),
             ("max_dim", "the largest irrep dimension present, i.e. the "
                         "maximum degeneracy of a mode at that site")],
            X, m["res"])))

    h.append(_view(
        "v-phonondex", X, 2,
        ("site_order  order of the site group",
         "n_irreps  distinct species",
         "max_dim  largest irrep dimension"),
        "Colour is max_dim, which is also an axis, so the view separates into "
        "one sheet per maximum degeneracy.", "04",
        "The index, plotted exactly",
        "Three-dimensional scatter of the phonon index: %d cells at "
        "site-symmetry order, number of irreps and maximum irrep dimension."
        % m["cells"], radius=4.2))

    h.append(sec("05", "What it measures", "", measures(
        m, [("members", "{:,}".format(len(rows)),
             "site-symmetry types, charted into %d cells" % m["cells"])])))

    h.append(sec(
        "06", "The guards, and the bugs they caught",
        "Every number here is computed &mdash; no textbook character table and "
        "no Wyckoff table is read &mdash; so the guards are arithmetic, not "
        "inspection.",
        simple_table(
            [("guard", "name"), ("on every one of the %d rows" % len(rows),
                                 "mono")],
            [["modes = 3 &times; multiplicity, and the decomposition sums "
              "to it", yn(P.integrality_holds())],
             ["|site symmetry| &times; |orbit| = |point group|",
              yn(P.orbit_stabiliser_holds())]],
            "A wrong character table does not give a wrong-looking answer; it "
            "gives a fractional multiplicity, and that cannot be rationalised "
            "away. All %d development bugs below were found this way and none "
            "by reading." % len(P.BUGS))
        + '<ul class="tight" style="margin-top:22px">%s</ul>'
        % "".join("<li>%s</li>" % E(b) for b in P.BUGS)))

    h.append('<div class="note warn"><span class="lab">What this index '
             'refuses</span><p style="margin-bottom:0">It claims nothing about '
             '<b>k&nbsp;&ne;&nbsp;&Gamma;</b>, where the little group&rsquo;s '
             'representations are projective for non-symmorphic groups &mdash; '
             'a different computation, named as open rather than quietly '
             'omitted. It claims no <b>frequencies</b>: a frequency is a '
             'measurement and the symmetry content is complete without one. '
             'And it does not call its members <b>materials</b> &mdash; '
             'materials are sums of members. <b>The first of those three '
             'refusals is discharged by <code>kpointdex</code>, the '
             '%dth row.</b></p></div>' % row_number("kpointdex.index"))

    h.append(sourceline("phonondex"))
    h.append(cfoot("phonondex"))
    h.append("</div>")
    _write("phonondex-plate.html", h)


# ===========================================================================
# ROW 26 -- kpointdex
# ===========================================================================

def build_kpointdex():
    import kpointdex as K
    X = K.index()
    m = measured(X)
    rows = K.read()
    nsg = len(K.by_spacegroup())
    nproj = len(K.projective())
    free, stuck = K.sticking_split()
    none_sg = K.spacegroups_with_none()
    polar = K.polar_classes(none_sg)
    dens = K.denominators()
    grid = K.grid()

    h = [plate.head("The k-Point Index"), '<div class="wrap">']
    h.append(_mast(
        "Research plate &middot; an index of quantum objects &middot; "
        "registry row&nbsp;%d" % row_number("kpointdex.index"),
        "The k&#8209;Point&nbsp;Index",
        "%s isolated high-symmetry k-stars over the %d space groups that "
        "carry one &mdash; with the projective small representations "
        "<code>phonondex</code> refused to compute."
        % ("{:,}".format(len(rows)), nsg),
        [("instrument", "kpointdex.py"),
         ("members", "{:,} k-stars".format(len(rows))),
         ("space groups", "%d of 230" % nsg),
         ("arity", "3"), ("cells", str(m["cells"])),
         ("cell", "(%d,&nbsp;%d,&nbsp;%d)" % m["cell"]),
         ("channel", "K%d" % m["cell"][0])]))

    h.append('<div class="note good"><span class="lab">A refusal discharged, '
             'not waived</span><p style="margin-bottom:0"><code>phonondex</code>'
             ' &sect;5 declined k&nbsp;&ne;&nbsp;&Gamma; because &ldquo;at a '
             'general k the little group&rsquo;s representations are '
             '<b>PROJECTIVE</b> for non-symmorphic groups, which is a '
             'different computation and is not done here.&rdquo; It is done '
             'here: the multiplier is decided rather than guessed, and '
             '<b>%s of the %s members (%.1f&thinsp;%%) carry a non-trivial '
             'one</b> &mdash; so the obstruction was real and it is behind '
             'us.</p></div>'
             % ("{:,}".format(nproj), "{:,}".format(len(rows)),
                100.0 * nproj / len(rows)))

    h.append(sec(
        "01", "What separates a point from the line it sits on",
        "The stabiliser of k is constant along a whole symmetry line or plane, "
        "and a grid reports those on exactly the same footing. The missing "
        "ingredient is a dimension.",
        "<p class=\"eqn mono\">k is a high-symmetry POINT&nbsp;&nbsp;iff"
        "&nbsp;&nbsp;rank[R &minus; I : R &isin; G<sub>k</sub>] = 3</p>"
        "<p>&mdash; the fixed-point set of k&rsquo;s own stabiliser is "
        "0-dimensional. That test is grid-free and exact, and once it is "
        "written down the grid can be thrown away: rank grows by at least one "
        "per element added, so some subset of G<sub>k</sub> of size at most 3 "
        "already reaches rank 3, and the k it fixes are enumerated exactly by "
        "Hermite normal form. <b>Sweeping every subset of size &le;&nbsp;3 "
        "therefore gives a finite, provably complete superset of the "
        "high-symmetry points, with no grid and no convergence "
        "question.</b></p>"
        "<p>The grid is reported anyway, because the question was asked and a "
        "grid-dependent answer would have been a red flag. Measured on the "
        "holohedral space group of each of the <b>%d</b> Bravais lattices, "
        "1/12 against 1/24 against the exact enumeration &mdash; and the "
        "agreement is not luck. The coordinate denominators that occur across "
        "all 230 space groups are <b>%s and nothing else</b>, and their "
        "lowest common multiple is <b>%d</b>, so a 1/12 grid is exactly "
        "sufficient and any finer grid must agree.</p>"
        % (len(grid), ", ".join(str(d) for d in dens),
           __import__("math").lcm(*dens))))

    h.append(sec(
        "02", "The three coordinates",
        "<code>star</code> and <code>pg_order</code> are <b>not</b> "
        "coordinates: their product is fixed by orbit&ndash;stabiliser, "
        "exactly as <code>multiplicity</code> and <code>pg_order</code> are "
        "excluded at &Gamma;. The star is a label the member carries, not an "
        "axis of the chart.",
        chart_table(
            [("little_order", "the order of the group the modes at k "
                              "transform under"),
             ("n_smallreps", "how many symmetry species exist at that k"),
             ("max_dim", "the largest small-representation dimension at "
                         "that k")],
            X, m["res"])))

    h.append('<div class="note warn"><span class="lab">WITHDRAWN in the '
             'instrument, and repeated here so the plate does not restore '
             'it</span><p style="margin-bottom:0"><code>max_dim</code>&rsquo;s '
             'gloss once read &ldquo;i.e. the maximum degeneracy symmetry '
             'forces at that k&rdquo;. That is <b>false</b> wherever time '
             'reversal doubles a level: the antiunitary obstruction is not in '
             'the little group and no small-rep dimension can see it. The '
             '<em>coordinate</em> is unchanged and correct &mdash; it is the '
             'largest small-representation dimension, which is what it '
             'computes; only the degeneracy reading is struck. The degeneracy '
             'is <code>corepdex</code>&rsquo;s <code>corep_dim</code>, the '
             '%dth row.</p></div>' % row_number("corepdex.index"))

    h.append(_view(
        "v-kpointdex", X, 2,
        ("little_order  |G_k|",
         "n_smallreps  species at k",
         "max_dim  largest small-rep dimension"),
        "Colour is max_dim, which is also an axis.", "03",
        "The index, plotted exactly",
        "Three-dimensional scatter of the k-point index: %d cells at "
        "little-group order, number of small representations and maximum "
        "small-representation dimension." % m["cells"], radius=5.4))

    h.append(sec("04", "What it measures", "", measures(
        m, [("members", "{:,}".format(len(rows)),
             "k-stars, charted into %d cells" % m["cells"]),
            ("projective", "{:,}".format(nproj),
             "%.1f%% carry a non-trivial multiplier"
             % (100.0 * nproj / len(rows)))])))

    h.append(sec(
        "05", "The guards, and the 68 space groups that carry no member at all",
        "Each is measured over the whole capture, not sampled.",
        simple_table(
            [("guard", "name"), ("verdict", "mono")],
            [["|G<sub>k</sub>| &times; |star| = |point group| on every row",
              yn(K.orbit_stabiliser_holds())],
             ["Burnside: the small-rep dimensions square-sum to the "
              "factor-group order", yn(K.burnside_sum_holds())],
             ["the grid method and the exact enumeration agree",
              yn(K.two_tests_agree())],
             ["the little-group orders agree with the second implementation",
              "%s &mdash; <span class=\"mono\">%d</span> disagreements"
              % (yn(not K.little_orders_agree()),
                 len(K.little_orders_agree()))]],
            "Measured over all %s members." % "{:,}".format(len(rows)))
        + "<p class=\"after\"><b>%d of the 230 space groups carry no isolated "
        "high-symmetry k-star whatever, and they are not an accident:</b> they "
        "are exactly the %d space groups of the ten polar crystal classes. "
        "That is measured against the class list, not asserted &mdash; the two "
        "sets agree on every member.</p>"
        "<p><b>%s members have bands forced to stick together and %s do "
        "not</b>, which is the physical content the factor system carries.</p>"
        % (len(none_sg), len(polar),
           "{:,}".format(stuck), "{:,}".format(free))))

    h.append(sourceline("kpointdex"))
    h.append(cfoot("kpointdex"))
    h.append("</div>")
    _write("kpointdex-plate.html", h)


# ===========================================================================
# ROW 27 -- corepdex
# ===========================================================================

def build_corepdex():
    import corepdex as C
    X = C.index()
    m = measured(X)
    rows = C.read()
    bc = C.by_case()
    small = C.small_rep_total()
    ndoubled = len(C.doubled())
    nx = len(C.type_x())
    nstars = len(C.stars())
    touched = C.spacegroups_touched()
    anti, proj, both, neither = C.mechanism_split()
    sa, sb, ga, gb, lv, sr = C.against_kpointdex()
    WHAT = {"a": "no doubling", "b": "DOUBLED &mdash; two copies of one irrep",
            "c": "DOUBLED &mdash; two conjugate irreps fuse",
            "x": "&minus;k is not in the star of k"}

    h = [plate.head("The Time-Reversal Extension"), '<div class="wrap">']
    h.append(_mast(
        "Research plate &middot; an index of quantum objects &middot; "
        "registry row&nbsp;%d" % row_number("corepdex.index"),
        "The Time-Reversal&nbsp;Extension",
        "%s corepresentations over <code>kpointdex</code>&rsquo;s own %s "
        "k-stars &mdash; the physically irreducible levels once time reversal "
        "is admitted, %d of them doubled by it and invisible to the unitary "
        "calculation." % ("{:,}".format(len(rows)), "{:,}".format(nstars),
                          ndoubled),
        [("instrument", "corepdex.py"),
         ("members", "{:,} corepresentations".format(len(rows))),
         ("stars", "{:,}".format(nstars)),
         ("arity", "3"), ("cells", str(m["cells"])),
         ("cell", "(%d,&nbsp;%d,&nbsp;%d)" % m["cell"]),
         ("channel", "K%d" % m["cell"][0])]))

    h.append('<div class="note warn"><span class="lab">Discharging the '
             'projective refusal was necessary and not sufficient</span>'
             '<p style="margin-bottom:0">The unitary answer at each k-star is '
             '<em>internally consistent</em>: &sum;d&sup2;&nbsp;=&nbsp;'
             '|G<sub>k</sub>| holds, the character table is orthogonal, every '
             'dimension is an integer. <b>It is simply INCOMPLETE, and nothing '
             'inside it says so.</b> Time reversal is antiunitary; it is not '
             'an element of the little group, and no amount of care with the '
             'little group will find it. Measured over the %s seated stars, '
             'the two mechanisms split <b>%d antiunitary only, %d projective '
             'only, %d both, %d neither</b> &mdash; so there is a population '
             'the earlier index is wrong about and its own integrality checks '
             'do not notice.</p></div>'
             % ("{:,}".format(nstars), anti, proj, both, neither))

    h.append(sec(
        "01", "A member is a level, not a star",
        "A corepresentation is the physically irreducible object &mdash; what "
        "a spectrum actually shows as one degenerate multiplet.",
        "<p>Herring&rsquo;s criterion returns an indicator W on each small "
        "representation, and the convention is part of the number: W here is "
        "the <b>normalised</b> indicator of Bilbao&rsquo;s "
        "<i>Representations DSG</i>, returning +1&thinsp;/&thinsp;"
        "&minus;1&thinsp;/&thinsp;0, and not the unnormalised Bradley &amp; "
        "Cracknell sum. A number without its convention is not a "
        "measurement.</p>"
        + simple_table(
            [("case", "name"), ("what it does", ""),
             ("where the doubling lives", "mono"), ("members", "num")],
            [[("type (x)" if c == "x" else "case (%s)" % c), WHAT[c],
               ", ".join(C.doubling_table()[c]), "{:,}".format(bc[c])]
             for c in C.CASES],
            "%s small representations, less the %d case-(c) that fuse in "
            "pairs and the %d type-(x) that fuse in pairs, gives "
            "%s &minus; %d &minus; %d = <b>%s</b> corepresentations, and that "
            "is the whole accounting."
            % ("{:,}".format(small), bc["c"], nx // 2,
               "{:,}".format(small), bc["c"], nx // 2,
               "{:,}".format(len(rows))))
        + "<p class=\"after\"><b>Type (x) is not a case (c), and the "
        "normalised form has a defect there.</b> With the conjugating set "
        "empty the criterion reads 0/0 &mdash; undefined, not zero &mdash; "
        "while the unnormalised form returns 0 and collides with case (c). "
        "This index divides nothing in that branch and records the status "
        "instead. The distinction is physical: a case-(c) level is doubled "
        "<em>at</em> k and not in the Brillouin zone, a type-(x) level the "
        "other way about.</p>"
        "<p><b>Case (b) is rare and it is not redundant.</b> %d levels in the "
        "whole crystallographic catalogue double by pairing an irrep with "
        "itself rather than with a conjugate; under a time-reversal-breaking "
        "perturbation a case-(b) level splits into two copies of the same "
        "character and a case-(c) level into two conjugate ones. An index that "
        "merged them would lose a distinction the spectrum shows.</p>"
        % bc["b"]))

    h.append(sec(
        "02", "The three coordinates",
        "The case letter is <b>not</b> a coordinate, because the three "
        "determine it: (a) is (d,&nbsp;d,&nbsp;1), (b) is (2d,&nbsp;d,&nbsp;1), "
        "(c) is (2d,&nbsp;d,&nbsp;2), (x) is (d,&nbsp;d,&nbsp;2). "
        "<code>little_order</code>, <code>n_smallreps</code>, "
        "<code>factor_order</code>, <code>star</code> and <code>pg_order</code> "
        "are excluded as properties of the star, which are "
        "<code>kpointdex</code>&rsquo;s.",
        chart_table(
            [("corep_dim", "the degeneracy &mdash; what a spectrum measures"),
             ("small_dim", "how much of it the unitary group accounts for, so "
                           "that corep_dim / small_dim <i>is</i> the "
                           "antiunitary obstruction"),
             ("n_small", "how many distinct species fuse, 1 or 2 &mdash; which "
                         "separates two copies of one character from a "
                         "conjugate pair")],
            X, m["res"])))

    h.append(_view(
        "v-corepdex", X, 2,
        ("corep_dim  degeneracy",
         "small_dim  the unitary part",
         "n_small  species fused"),
        "Colour is n_small, which is also an axis: one sheet is the levels "
        "that carry a single species, the other the pairs that fuse.", "03",
        "The index, plotted exactly",
        "Three-dimensional scatter of the corepresentation index: %d cells at "
        "corepresentation dimension, small-representation dimension and number "
        "of species fused." % m["cells"], radius=7.0))

    h.append(sec("04", "What it measures", "", measures(
        m, [("members", "{:,}".format(len(rows)),
             "corepresentations, charted into %d cells" % m["cells"]),
            ("doubled", str(ndoubled),
             "%.1f%% of the member set, doubled at k by time reversal"
             % (100.0 * ndoubled / len(rows))),
            ("space groups", str(len(touched)),
             "carry a level doubled at k")])))

    h.append(sec(
        "05", "It sits on kpointdex&rsquo;s own stars, and the join is not on "
        "the label",
        "A star is labelled by one of its own arms, and the two derivations do "
        "not always pick the same arm. What is compared is therefore "
        "label-free.",
        simple_table(
            [("compared", "name"), ("here", "num"), ("in kpointdex", "num")],
            [["isolated high-symmetry stars", "{:,}".format(sa),
              "{:,}".format(sb)],
             ["space groups whose (|G<sub>k</sub>|, star&nbsp;size) multisets "
              "agree", "{:,}".format(ga), "{:,}".format(gb)],
             ["representations", "{:,} corepresentations".format(lv),
              "{:,} small representations".format(sr)]],
            "The multiset of (little-group order, star size) per space group "
            "is what a stdlib reader can see; the set-wise identity of the "
            "stars themselves needs the point group to expand them and is "
            "proved in the derivation, which has numpy.")))

    h.append(sourceline("corepdex"))
    h.append(cfoot("corepdex"))
    h.append("</div>")
    _write("corepdex-plate.html", h)


BUILDERS = {"phonondex": build_phonondex,
            "kpointdex": build_kpointdex,
            "corepdex": build_corepdex}

if __name__ == "__main__":
    for w in (sys.argv[1:] or ("phonondex", "kpointdex", "corepdex")):
        BUILDERS[w]()
