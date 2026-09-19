#!/usr/bin/env python3
r"""
mesons.py -- THE MESONS, CHARTED ON THE QUANTUM NUMBERS PDG PRINTS FOR THEM.
DOCKET 27.

    python3 mesons.py             the reading
    python3 mesons.py --selftest  fixtures

===============================================================================
1. THE MEMBERS
===============================================================================

One member is a meson in the PDG table: 250 of them, antiparticles counted
separately for the reason `fundamental.py` section 1 gives -- a chart that
merged a meson with its antiparticle would be charting an equivalence class it
had not declared.  Read from `captures/PDG-2026.tsv`; `pdgcapture.py` is the
provenance.

    EIGHT ARE NAMED AND SET ASIDE, not silently dropped.  PDG reports no
    parity for D(1)(2420)+-, D(0)*(2300)+-, D(s2)*(2573)+- and D(s)*+-, so a
    chart carrying P cannot place them.  `unplaced()` lists them by name.  This
    is a gap in the TABLE, not in physics: a later Review that measures those
    parities seats them with no change to this file but the count.  242 members
    are charted.

===============================================================================
2. THE COORDINATES, DECLARED BEFORE THE CHART WAS RUN
===============================================================================

    2J    spin, doubled.  Every meson here is an integer-spin boson, so 2J is
          even; it is doubled anyway so the column reads the same as it does
          for the baryons and the fundamental particles.
    P     parity, +1 or -1.
    2I    isospin, doubled: 0, 1 or 2 for I = 0, 1/2 or 1.
    Q3    electric charge in thirds.  -3, 0 or +3 -- a meson is integrally
          charged, and the thirds are kept so the column is the same column
          the quark chart uses.

    WHAT IS REFUSED, and each refusal is MEASURED here rather than asserted:

    C-PARITY IS NOT A COORDINATE, because it is not TOTAL: 168 of the 250 have
    no C at all.  And the reason is a theorem, not a missing measurement --
    `c_is_defined_iff()` checks it: C is printed for exactly the mesons that
    are their OWN antiparticle, and for no other, with exactly two exceptions.
    THE TWO EXCEPTIONS ARE K(L)0 AND K(S)0, and they are the sharpest thing in
    this file: both are self-conjugate neutrals, both are strangeness
    MIXTURES (`p(dS)-q(Ds)` and `p(dS)+q(Ds)`), and a mixture of that kind is
    a CP eigenstate and not a C eigenstate.  The data reproduces the textbook
    distinction with no help from this file.

    G-PARITY IS NOT A COORDINATE for the same reason and by a second theorem:
    it is printed for exactly the flavour-neutral mesons -- net strangeness,
    charm and beauty all zero -- and 132 of the 250 are not flavour-neutral.
    `g_is_defined_iff()` checks that too.

    STRANGENESS IS NOT A COORDINATE, and the obstruction is not arithmetic.
    59 of the 250 carry a quark content that is not a plain string of quark
    letters -- `(uU-dD)/sqrt(2)`, `x(uU+dD)+y(sS)`, `Maybe non-qQ` -- so no
    strangeness can be read off them, and for two of the 59 there is no
    strangeness to read: K(L)0 and K(S)0 are not strangeness eigenstates.
    `strangeness()` returns None on all 59 rather than guessing.  Contrast
    `baryons.py`, where every one of the 292 quark strings parses and S, C and
    B are all charted.

    MASS AND WIDTH are reported and not charted, for the reason
    `fundamental.py` section 2 gives about totality and for a second one: a
    resonance's width is a property of its decay, not a quantum number, and
    the criterion in `registry.py` is about quantum numbers.

===============================================================================
3. THE C-EIGENSTATE CHART IS MEASURED AND REFUSED
===============================================================================

The canonical PDG label for a meson is I^G(J^PC), and 82 of the 250 carry all
five.  Charting those 82 on (2I, G, 2J, P, C) gives 20 cells at K0.

    IT IS NOT SEATED.  The overlap ruling's first ground is a NOVEL CHANNEL,
    and K0 is carried by rows already seated -- so the chart earns no position
    the master index does not already hold, and seating it would be exactly
    the over-representation the ruling exists to prevent.  `ceigen_chart()`
    computes it so the refusal is on the record with its measurement, in the
    way `overlaprule.py` records its own three refusals.  The FINDING inside
    it -- which mesons carry a C at all, and why the two kaons do not -- is
    section 2's and is kept.
"""

import sys

import hlaw
import mi
import pdgcapture

NAMES = ("2J", "P", "2I", "Q3")
ARITY = len(NAMES)
FAMILY = "meson"

# The capture writes a quark content as letters, uppercase for a quark and
# lowercase for an antiquark.  A string outside this alphabet is a mixture or
# an exotic candidate and is not parsed.
QUARK_LETTERS = "UDSCBTudscbt"

_C = {}


def all_rows():
    """Every meson in the capture, 250 of them, before section 1's setting
    aside.  [(name, pdgid, 2J, P, 2I, Q3, C, G, quarks)] with None for a
    quantum number the table does not print."""
    if "a" not in _C:
        out = []
        for r in pdgcapture.read():
            if r["family"] != FAMILY:
                continue
            def g(k):
                return None if r[k] == "?" else int(r[k])
            out.append((r["name"], int(r["pdgid"]), int(r["J2"]), g("P"),
                        int(r["I2"]), int(r["Q3"]), g("C"), g("G"),
                        r["quarks"]))
        _C["a"] = sorted(out, key=lambda t: (t[2], t[4], t[5], t[1]))
    return _C["a"]


def unplaced():
    """[name] -- section 1's eight, set aside because PDG prints no parity."""
    return sorted(n for n, _p, _j, P, *_x in all_rows() if P is None)


def rows():
    """The 242 charted members: [(name, pdgid, 2J, P, 2I, Q3)]."""
    return [(n, p, j, P, i, q)
            for n, p, j, P, i, q, _c, _g, _k in all_rows() if P is not None]


def index():
    return frozenset((j, P, i, q) for _n, _p, j, P, i, q in rows())


def self_conjugate(pdgid):
    """Is this meson its own antiparticle?  The capture's `anti` column reads
    0 for a self-conjugate state; it is re-derived here from the capture so
    the theorem in section 2 is tested against the source and not a cache."""
    return _anti()[pdgid] == 0


def _anti():
    if "n" not in _C:
        _C["n"] = {int(r["pdgid"]): int(r["anti"])
                   for r in pdgcapture.read() if r["family"] == FAMILY}
    return _C["n"]


def c_is_defined_iff():
    """(agree, [exceptions]) -- C is printed exactly for the self-conjugate.

    Section 2's first theorem, checked rather than claimed.  An exception is
    (name, is self-conjugate, has a C).
    """
    bad = []
    for n, p, _j, _P, _i, _q, C, _g, _k in all_rows():
        sc = self_conjugate(p)
        if sc != (C is not None):
            bad.append((n, sc, C is not None))
    return (not bad, sorted(bad))


def flavour(quarks):
    """(S, C, B) net flavour from the quark string, or None if it does not
    parse.

    THE CASE CONVENTION IS THE OPPOSITE OF THE OBVIOUS ONE AND IT WAS READ OFF
    THE PARTICLES, NOT GUESSED.  In this capture LOWERCASE IS THE QUARK and
    UPPERCASE THE ANTIQUARK: the proton is `uud` and the antiproton `UUD`, the
    Lambda is `uds` and the anti-Lambda `UDS`.  `case_convention()` pins it
    against six named states whose flavour every textbook prints, because
    getting this backwards silently negates S, C and B on every member and the
    flavour-neutral rows -- where the G-parity theorem lives -- would not
    notice.

    The signs are the standard ones: an s quark carries S = -1, a c quark
    C = +1, a b quark B = -1, and an antiquark the opposite of its quark.
    """
    if not quarks or any(ch not in QUARK_LETTERS for ch in quarks):
        return None
    def net(a):
        """(quarks of this flavour) - (antiquarks of it)."""
        return sum(-1 if ch.isupper() else 1
                   for ch in quarks if ch.upper() == a)
    return (-net("S"), net("C"), -net("B"))


# (name, pdgid, quark content, the flavour every textbook prints)
CONVENTION_SPOTS = (
    ("Omega-", 3334, "sss", (-3, 0, 0)),
    ("Lambda", 3122, "uds", (-1, 0, 0)),
    ("K+", 321, "uS", (1, 0, 0)),
    ("K-", -321, "Us", (-1, 0, 0)),
    ("D+", 411, "cD", (0, 1, 0)),
    ("B+", 521, "uB", (0, 0, 1)),
)


def case_convention():
    """[(name, quarks in the capture, flavour computed, flavour expected)].

    Reads each spot's quark string BACK OUT OF THE CAPTURE rather than trusting
    the copy in CONVENTION_SPOTS, so the check fails if the capture changes.
    """
    by = {int(r["pdgid"]): r["quarks"] for r in pdgcapture.read()}
    return [(n, by.get(pid), flavour(by.get(pid)), want)
            for n, pid, _q, want in CONVENTION_SPOTS]


def strangeness(quarks):
    f = flavour(quarks)
    return None if f is None else f[0]


def g_is_defined_iff():
    """(agree, [exceptions]) -- G is printed exactly for the flavour-neutral.

    Section 2's second theorem.  A meson whose quark string does not parse is
    flavour-neutral iff it is one of the mixtures or exotic candidates, which
    is what `unparsed_are_neutral()` reports; here they are judged by whether
    the table prints a G, so the test is run only on the ones that parse.
    """
    bad = []
    for n, _p, _j, _P, _i, _q, _c, G, k in all_rows():
        f = flavour(k)
        if f is None:
            continue
        if (f == (0, 0, 0)) != (G is not None):
            bad.append((n, f, G is not None))
    return (not bad, sorted(bad))


def unparsed():
    """[(name, quark content)] -- the 59 whose content is a mixture."""
    return sorted((n, k) for n, _p, _j, _P, _i, _q, _c, _g, k in all_rows()
                  if flavour(k) is None)


def kaon_exceptions():
    """[(name, quarks, self-conjugate, has C)] -- K(L)0 and K(S)0.

    Section 2's point: self-conjugate neutrals with no C, because a
    strangeness mixture is a CP eigenstate and not a C eigenstate.
    """
    return sorted((n, k, self_conjugate(p), C is not None)
                  for n, p, _j, _P, _i, _q, C, _g, k in all_rows()
                  if self_conjugate(p) and C is None)


def ceigen_rows():
    """The 82 with a C -- section 3's refused chart, computed not seated."""
    return [(n, i, G, j, P, C)
            for n, _p, j, P, i, _q, C, G, _k in all_rows() if C is not None]


def ceigen_chart():
    """(cells, cell, closers) for I^G(J^PC) over the 82.  REFUSED: section 3."""
    Z = frozenset((i, G, j, P, C) for _n, i, G, j, P, C in ceigen_rows()
                  if G is not None and P is not None)
    return (len(Z), mi.cell(Z), closers(Z))


def conjugation():
    """(pairs, collided, split, charges of the collided, charges of the split).

    THE ANTIPARTICLE MAP IS NOT SEATED AS AN INDEX.  Its members would be
    pairs, and a pair carries the quantum numbers of its members rather than
    any of its own, so it fails registry.py's criterion by construction.  It
    is MEASURED here instead, because the question "does the chart see
    antimatter" has an answer and the answer belongs on the record.

    THE ANSWER IS A THEOREM AND THE DATA MEETS IT EXACTLY.  Of the four
    coordinates, conjugation leaves 2J, P and 2I alone and flips only Q3 --
    so the chart separates a pair IF AND ONLY IF the meson is charged.  79
    pairs: 51 charged and split, 28 neutral and collided, no exception in
    either direction.  `fundamental.py` collides on the same rule: the three
    neutrino pairs are its only neutral fermion pairs.
    """
    cellof = {p: (j, P, i, q) for _n, p, j, P, i, q in rows()}
    same, split = [], []
    for p in cellof:
        if p < 0 or -p not in cellof:
            continue
        (same if cellof[p] == cellof[-p] else split).append(cellof[p])
    return (len(same) + len(split), len(same), len(split),
            sorted({c[3] for c in same}), sorted({c[3] for c in split}))


def closers(X=None):
    X = frozenset(index() if X is None else X)
    cl, _b = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def cell():
    return mi.cell(index())


def report():
    X = index()
    print("=" * 74)
    print("THE MESONS -- the PDG table, charted")
    print("=" * 74)
    print()
    print("1. THE MEMBERS.")
    print("   in the table   %d" % len(all_rows()))
    print("   set aside      %d, no parity printed: %s"
          % (len(unplaced()), ", ".join(unplaced())))
    print("   charted        %d" % len(rows()))
    print()
    print("2. THE CHART on %s." % (", ".join(NAMES)))
    print("   cells    %d of %d members" % (len(X), len(rows())))
    print("   cell     %s" % (cell(),))
    print("   closes   %s" % (", ".join(closers()) or "NOTHING"))
    print()
    print("3. C-PARITY IS NOT TOTAL, and the reason is a theorem.")
    ok, bad = c_is_defined_iff()
    print("   C is printed for exactly the self-conjugate mesons: %s"
          % ("EXACTLY" if ok else "%d exceptions" % len(bad)))
    for n, sc, hc in bad:
        print("     %-14s self-conjugate %-5s has a C %s" % (n, sc, hc))
    print("   the two exceptions, and why they are not C eigenstates:")
    for n, k, _sc, _hc in kaon_exceptions():
        print("     %-10s %s -- a strangeness MIXTURE, so a CP eigenstate"
              % (n, k))
    print()
    print("4. G-PARITY IS NOT TOTAL either, by a second theorem.")
    ok, bad = g_is_defined_iff()
    print("   over the %d whose quark content parses, G is printed for exactly"
          % (len(all_rows()) - len(unparsed())))
    print("   the flavour-neutral: %s"
          % ("EXACTLY" if ok else "%d exceptions" % len(bad)))
    print()
    print("5. STRANGENESS IS NOT TOTAL: %d quark contents do not parse."
          % len(unparsed()))
    seen = {}
    for _n, k in unparsed():
        seen[k] = seen.get(k, 0) + 1
    for k in sorted(seen):
        print("     %-24s %d" % (k, seen[k]))
    print()
    n, c, cl = ceigen_chart()
    print("6. THE I^G(J^PC) CHART, MEASURED AND REFUSED.")
    print("   82 members, %d cells, cell %s, closes %s"
          % (n, c, ", ".join(cl) or "NOTHING"))
    print("   REFUSED: K0 is not a novel channel, so the overlap ruling's")
    print("   first ground fails and seating it would over-represent.")
    print()
    pairs, same, split, qs, qd = conjugation()
    print("7. DOES THE CHART SEE ANTIMATTER?  Only where the meson is charged.")
    print("   %d conjugate pairs: %d split, %d sharing a cell" % (pairs, split, same))
    print("   the collided pairs carry Q3 in %s; the split pairs Q3 in %s"
          % (qs, qd))
    print("   Conjugation leaves 2J, P and 2I alone and flips only Q3, so the")
    print("   chart separates a pair iff the meson is charged.  No exception.")
    print("   The antiparticle map is NOT seated: its members would be pairs,")
    print("   and a pair carries no quantum numbers of its own.")
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    A = all_rows()
    R = rows()
    chk("250 mesons in the table", len(A), 250)
    chk("eight carry no parity and are set aside", len(unplaced()), 8)
    chk("and they are the four charm-strange states and their antiparticles",
        unplaced(),
        ["D(0)*(2300)+", "D(0)*(2300)-", "D(1)(2420)+", "D(1)(2420)-",
         "D(s)*+", "D(s)*-", "D(s2)*(2573)+", "D(s2)*(2573)-"])
    chk("242 charted", len(R), 242)

    # the quantum numbers, against the physics
    chk("every meson has integer spin -- 2J is even",
        sorted({j % 2 for _n, _p, j, *_x in A}), [0])
    chk("parity is +1 or -1 and nothing else",
        sorted({P for _n, _p, _j, P, *_x in R}), [-1, 1])
    chk("isospin is 0, 1/2 or 1 -- 2I in 0, 1, 2",
        sorted({i for _n, _p, _j, _P, i, _q in R}), [0, 1, 2])
    chk("a meson is integrally charged -- Q3 in -3, 0, +3",
        sorted({q for _n, _p, _j, _P, _i, q in R}), [-3, 0, 3])

    # THE FIRST THEOREM: C is defined iff self-conjugate, bar two
    agree, bad = c_is_defined_iff()
    chk("C is printed for the self-conjugate mesons and for no other, with "
        "two exceptions", (agree, len(bad)), (False, 2))
    chk("and the two exceptions are the neutral kaons",
        sorted(n for n, _s, _h in bad), ["K(L)0", "K(S)0"])
    chk("both are self-conjugate neutrals that carry NO C",
        sorted(kaon_exceptions()),
        [("K(L)0", "p(dS)-q(Ds)", True, False),
         ("K(S)0", "p(dS)+q(Ds)", True, False)])
    chk("82 mesons carry a C", len(ceigen_rows()), 82)
    chk("168 do not", len(A) - len(ceigen_rows()), 168)

    # THE SECOND THEOREM: G is defined iff flavour-neutral
    agree, bad = g_is_defined_iff()
    chk("over the parsing quark contents, G is printed for exactly the "
        "flavour-neutral", (agree, bad), (True, []))
    chk("132 mesons carry no G",
        sum(1 for _n, _p, _j, _P, _i, _q, _c, G, _k in A if G is None), 132)

    # flavour, and the refusal of strangeness
    chk("59 quark contents do not parse", len(unparsed()), 59)
    # THE CASE CONVENTION, pinned against named particles.  Lowercase is the
    # quark here; assuming otherwise negates S, C and B on every member.
    chk("the capture still spells the six spot particles as recorded",
        [(n, q) for n, q, _f, _w in case_convention()],
        [(n, q) for n, _p, q, _w in CONVENTION_SPOTS])
    chk("and each one's flavour comes out as the textbook prints it",
        [(n, f == w) for n, _q, f, w in case_convention()],
        [(n, True) for n, _p, _q, _w in CONVENTION_SPOTS])
    chk("lowercase is the quark: sss is S = -3 and SSS is S = +3",
        (flavour("sss"), flavour("SSS")), ((-3, 0, 0), (3, 0, 0)))
    chk("a c quark carries charm +1 and a b quark beauty -1",
        (flavour("cud"), flavour("bud")), ((0, 1, 0), (0, 0, -1)))
    chk("an antiquark carries the opposite of its quark",
        (flavour("Us"), flavour("uS")), ((-1, 0, 0), (1, 0, 0)))
    chk("a mixture returns None rather than a guess",
        [strangeness(k) for k in ("p(dS)+q(Ds)", "x(uU+dD)+y(sS)",
                                  "Maybe non-qQ")], [None, None, None])
    chk("and the neutral kaons are among the 59 -- they are not strangeness "
        "eigenstates",
        sorted(n for n, _k in unparsed() if n.startswith("K(")),
        ["K(L)0", "K(S)0"])

    # the chart
    X = index()
    chk("arity 4", len(next(iter(X))), 4)
    chk("66 cells over 242 members", (len(X), len(R)), (66, 242))
    chk("channel K0 -- nothing closes it", closers(), [])
    chk("cell (K, height, width)", cell(), (0, 10, 14))
    chk("and |X| <= height x width, Dilworth",
        len(X) <= cell()[1] * cell()[2], True)

    # no coordinate is a row label
    import overlap
    chk("no coordinate is a row LABEL",
        [a for a, _d, _n, _r, v in overlap.resolution(X) if v == "LABEL"], [])

    # section 3's refusal, measured
    n, c, cl = ceigen_chart()
    chk("the I^G(J^PC) chart over the 82 gives 20 cells", n, 20)
    chk("at K0, which is NOT a novel channel -- ground 1 fails", cl, [])
    chk("so it is refused, and `mesons.ceigen_chart` is not in the registry",
        "ceigen_chart" in {a for _m, a, *_x in __import__("registry").REGISTERED
                           if _m == "mesons"}, False)

    # antimatter: the chart sees it iff the meson is charged
    pairs, same, split, qs, qd = conjugation()
    chk("79 conjugate pairs among the 242", pairs, 79)
    chk("51 are split by the chart and 28 collide", (split, same), (51, 28))
    chk("EVERY collided pair is neutral and EVERY split pair is charged",
        (qs, qd), ([0], [3]))
    # the MECHANISM, not just the outcome: over every pair in the table, the
    # first three coordinates agree and the fourth negates.
    cellof = {pid: (j, P, i, q) for _n, pid, j, P, i, q in R}
    mech = [(cellof[pid][:3] == cellof[-pid][:3],
             cellof[pid][3] == -cellof[-pid][3])
            for pid in cellof if pid > 0 and -pid in cellof]
    chk("and the MECHANISM holds member by member -- 2J, P and 2I agree "
        "across every pair and Q3 negates", sorted(set(mech)), [(True, True)])

    print("mesons selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
