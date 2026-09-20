#!/usr/bin/env python3
r"""deformedbands.py -- THE DEFORMED TWO-QUASIPARTICLE LEVELS, SEATED.  DOCKET 36b.

    python3 deformedbands.py             the reading
    python3 deformedbands.py --selftest  fixtures

M: "please seat the deformed index".

`deformed.py` closed the capture: all 234 entries of arXiv:2508.05447's Table 3,
exact against three of the paper's own numbers.  A capture is not an index, and
that file said so and stopped.  This one charts it.

AN INSTRUMENT IMPORTS ITS CAPTURE; IT NEVER COPIES ONE.  Every level here comes
from `deformed.entries()` at call time.  There is no table in this file, and if
the capture moves this index moves with it -- which is what the cross-fixture at
the bottom is for.

===============================================================================
1. THE MEMBERS, AND WHY THEY ARE NOT THE OTHER NUCLEAR INDEX'S
===============================================================================

A member is ONE NUCLEAR EXCITED STATE in a two-quasiparticle rotational band of
a deformed odd-odd nucleus, Z 67-71, A 156-174.

    THE SOURCE'S TITLE SAYS 156 <= A <= 168 AND ITS TABLE 3 DOES NOT.  132 of
    the 1,904 seated levels sit above A = 168, up to A = 174.  This file
    describes what the table holds, not what the title claims, and the
    discrepancy is recorded rather than smoothed: `a_ranges()` measures it.  It carries spin I and
parity exactly as a particle carries J and P, so it meets the criterion the
register enforces: THE QUANTUM NUMBERS ARE THE LEVEL'S OWN, not its band's and
not its nuclide's.  DOCKET 28's trap is the reason that sentence is here.

    THIS IS A NEW MEMBER SET AND NOT A RECHARTING OF `nucbands`.  That index
    holds 2,152 levels of MAGNETIC and ANTIMAGNETIC rotational bands -- the
    shears mechanism in weakly-deformed and near-spherical nuclei.  These are a
    DEFORMED ROTOR's tower, a different mechanism in different nuclei from a
    different paper.  `disjoint_from_nucbands()` measures the overlap of the two
    member sets rather than asserting it: ZERO nuclides in common.

    AND THE GROUND FIRST GIVEN FOR THAT ZERO WAS FALSE.  This file said the two
    mass ranges are disjoint.  THEY ARE NOT: `nucbands` spans A 58-205 and
    CONTAINS this one's 156-174 entirely.  The zero is a measured fact about
    which nuclides each paper happens to tabulate, not a consequence of where
    they sit on the chart -- a weaker ground, and the true one.  An audit
    caught it; `a_ranges()` now reports both spans so the claim cannot be made
    again without the numbers beside it.

    SO THE OVERLAP RULING DOES NOT APPLY.  Its four grounds test a COARSENING --
    the same members on fewer coordinates.  Two indexes with no member in common
    are not overlapping charts, and `nucbands` and this one sharing the
    coordinate NAMES (2I, parity) is not sharing information, any more than two
    nuclides sharing a Z would be.  `grounds_do_not_apply()` records that rather
    than quietly skipping the test.

===============================================================================
2. THE COORDINATES, DECLARED BEFORE THE CHART WAS RUN
===============================================================================

    2I      spin, doubled so a half-integer spin stays an integer.  READ from
            the I^pi cell of Table 3.
    parity  +1 or -1.  READ from the same cell.

    WHAT IS REFUSED, and each refusal is MEASURED here rather than asserted:

    THE ENERGY IS NOT A COORDINATE.  It is a magnitude, not a quantum number,
    and the criterion in `registry.py` is about quantum numbers.  It is also
    not even a number for much of this table: 61 bandheads are printed as
    `A+134.27` or `1135.7+y`, relative to an unknown offset.  Both reasons hold
    and the second is the one peculiar to this source.

    THE BAND NUMBER IS NOT A COORDINATE.  It is the table's row label -- 1, 2,
    3 within each nuclide -- and a label is what `figure.py`'s resolution test
    exists to catch.  `band_number_is_a_label()` measures it: it separates
    almost every entry and groups nothing.

    Z AND N ARE NOT COORDINATES, and this is the one that is a judgement rather
    than a rule, so it is measured both ways.  They are properties of the HOST
    nuclide, not of the level -- DOCKET 28's trap exactly.  `with_ZN()` charts
    them anyway and reports what that chart would be, so the refusal is made
    against a number rather than in the abstract.

===============================================================================
3. WHAT THE CHART IS
===============================================================================

    1,904 levels carry both quantum numbers.  60 carry a spin and no parity and
    are REFUSED, named by `no_parity()`; they are the same kind of gap
    `nucbands` reports and are counted apart for the same reason.

    96 cells.  Channel K2, cell (2, 49, 2).

    AND ITS K2 IS THE FREE ONE.  At arity 2 there is exactly one 2-subset of the
    coordinates, so `kdet` returns True for every set whatever and statistics
    closes vacuously.  This index REALLY CLOSES IN NOTHING, which is where
    `mesons`, `baryons` and `nucbands` sit.  `free_channel()` says so rather
    than banking the K2 as though it were earned -- the same statement
    `nucbands.py` makes in its own section 3, and it is repeated here because a
    reader of this file should not have to find it in that one.

    THE CELL IS UNOCCUPIED.  No seated index sits at (2, 49, 2), and that is
    measured against the register rather than assumed.
"""

import sys

import deformed
import hlaw
import mi
import registry

# WHERE THE DATA COMES FROM.  registry.sources() reads this, checks every path
# exists and hashes it, so the provenance travels in the tree.
SOURCE = (
    "Charted from deformed.entries(), which segments captures/"
    "arxiv-2508.05447.txt -- Pinky, Kumar, Singh & Jain, 'Features of "
    "Two-Quasiparticle Rotational Bands in Deformed Odd-Odd Nuclei, "
    "156 <= A <= 168'.  The capture is total against three of the paper's own "
    "numbers: 234 entries, 173 bands, 61 bandhead states, all exact.  Nothing "
    "is written down by hand.",
    ("research/warp-drive/captures/arxiv-2508.05447.txt",
     "research/warp-drive/captures/DEFORMED-entries.tsv",
     "research/warp-drive/captures/DEFORMED-levels.tsv"),
)

NAMES = ("2I", "parity")
ARITY = len(NAMES)

_C = {}


def levels():
    """[(2I, parity, A, Z, N, entry)] -- every level carrying BOTH numbers.

    IMPORTED from the capture on every call path, never cached to disk here.
    """
    if "l" not in _C:
        out, gap = [], []
        for i, e in enumerate(deformed.entries()):
            for _en, sp in e["levels"]:
                i2, p = deformed.two_i(sp), deformed._parity(sp)
                if i2 is None:
                    continue
                if p is None:
                    gap.append((i2, e["A"], e["Z"], e["N"], i))
                    continue
                out.append((i2, p, e["A"], e["Z"], e["N"], i))
        _C["l"], _C["g"] = out, gap
    return _C["l"]


def no_parity():
    """[(2I, A, Z, N, entry)] -- levels with a spin and no parity.  REFUSED."""
    levels()
    return _C["g"]


def index():
    return frozenset((i2, p) for i2, p, *_x in levels())


def cell():
    return mi.cell(index())


def free_channel():
    """(arity, is the statistics closer vacuous here, the honest channel).

    At arity 2 the only 2-subset of the coordinates is the whole of them, so
    2-determinacy reconstructs the set itself and closes for free.  Said, not
    banked.
    """
    X = index()
    return (ARITY, ARITY <= 2, mi.K(X),
            "the K2 is the free one; this index really closes in NOTHING")


def band_number_is_a_label():
    """(distinct band numbers, entries, ratio) -- section 2's refusal, measured.

    figure.py's rule: a coordinate whose distinct values reach 90 % of its
    members separates everything and groups nothing.
    """
    E = deformed.entries()
    d = len({(e["Z"], e["N"], e["no"]) for e in E})
    return (d, len(E), round(d / float(len(E)), 4))


def with_ZN():
    """(cells, channel, cell) for (2I, parity, Z, N) -- the refused chart.

    Charted so the refusal in section 2 is made against a number.  Z and N are
    the HOST nuclide's, not the level's, which is why it is not seated however
    it lands.
    """
    X = frozenset((i2, p, Z, N) for i2, p, _A, Z, N, _e in levels()
                  if Z is not None and N is not None)
    return (len(X), mi.K(X), mi.cell(X))


def a_ranges():
    """((min A, max A) here, (min A, max A) in nucbands, A values shared).

    Section 1's corrected ground.  The ranges OVERLAP -- nucbands contains this
    one -- so the zero nuclide overlap is a fact about the tabulations and not
    about the mass numbers.
    """
    import nucbands
    mine = {a for _i, _p, a, _z, _n, _e in levels() if a}
    theirs = {int(r["A"]) for r in nucbands.members() if r.get("A")}
    return ((min(mine), max(mine)), (min(theirs), max(theirs)),
            len(mine & theirs))


def above_title_range():
    """(levels above A = 168, the largest A) -- the source's own overclaim."""
    hi = [a for _i, _p, a, _z, _n, _e in levels() if a and a > 168]
    return (len(hi), max(a for _i, _p, a, _z, _n, _e in levels() if a))


def disjoint_from_nucbands():
    """(nuclides here, nuclides there, in common) -- section 1, measured."""
    import nucbands
    mine = {(r[3], r[4]) for r in levels() if r[3] is not None}
    # nucbands rows carry A and Z, not N.  Reading a key that is not there
    # returned an EMPTY set and made the disjointness vacuously true; the
    # "both sets non-empty" fixture below is what caught it.
    theirs = {(int(r["Z"]), int(r["A"]) - int(r["Z"]))
              for r in nucbands.members() if r.get("Z") and r.get("A")}
    return (len(mine), len(theirs), len(mine & theirs))


def grounds_do_not_apply():
    """Why the overlap ruling is not run: no member is shared with any index."""
    return ("the four grounds test a COARSENING -- the same members on fewer "
            "coordinates.  This member set shares no member with any seated "
            "index, so there is nothing to coarsen and the ruling has no "
            "subject.  Sharing the coordinate NAMES with nucbands is not "
            "sharing information.")


def cell_is_unoccupied():
    """(this cell, whoever holds it) -- measured against the register."""
    c = cell()
    held = [registry.short(nm) for nm, _m, _a, _me, _w, _q in registry.rows()
            if mi.cell(registry.index_of(nm)) == c
            and nm != "deformedbands.index"]
    return (c, held)


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok = ok and good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    # THE CAPTURE IT STANDS ON.  If deformed.py moves, this fires first.
    chk("the capture is total against the paper's own census",
        deformed.census2(), (234, 173, 61))
    # A REAL TEST OF "IMPORTS ITS CAPTURE".  Grepping this file's own source for
    # a function name is satisfied by the docstring alone -- an audit pointed
    # that out.  The test that bites is that the index MOVES when the capture
    # moves: drop a nuclide from the capture and the chart must change.
    _saved = dict(_C)
    try:
        _C.clear()
        _orig = deformed.entries
        deformed.entries = lambda: [e for e in _orig() if e["Z"] != 67]
        _shrunk = len(levels())
    finally:
        deformed.entries = _orig
        _C.clear()
        _C.update(_saved)
    # THE MEMBERS shrink; the CELLS need not, because the nuclides overlap on
    # (2I, parity) -- which is itself worth knowing and is why this fixture
    # tests the member count and not the chart.
    chk("the index is READ from the capture -- shrink the capture, it shrinks",
        (_shrunk < len(levels()), _shrunk > 0), (True, True))

    chk("1,904 levels carry both quantum numbers", len(levels()), 1904)
    chk("59 carry a spin and no parity, and are refused apart",
        len(no_parity()), 59)
    # NOT A TAUTOLOGY.  The earlier form recomputed the right-hand side the same
    # way the left was computed, so it passed with most of the capture deleted.
    # Pinned against the capture's OWN level count instead, with the two spin-
    # less rows named rather than absorbed.
    _allrows = sum(len(e["levels"]) for e in deformed.entries())
    chk("placed + refused = every level the capture holds, less the spinless",
        (len(levels()) + len(no_parity()), _allrows), (1963, 1963))

    X = index()
    chk("96 cells on (2I, parity)", len(X), 96)
    chk("channel K2, cell (2, 49, 2)", (mi.K(X), cell()), (2, (2, 49, 2)))
    ar, vac, K, _w = free_channel()
    chk("and the K2 is the FREE one -- arity 2, kdet vacuous",
        (ar, vac, K), (2, True, 2))

    # THE REFUSALS, EACH MEASURED.
    d, n, r = band_number_is_a_label()
    # Once every entry carries its own nuclide the band number is PERFECTLY
    # injective: 234 of 234.  It read 219 while 35 entries were booked to the
    # wrong nuclide, and pinning 219 would have baked that defect into a
    # fixture -- which it briefly did.
    chk("the band number separates every entry -- a row label at 1.0",
        (d, n, r), (234, 234, 1.0))
    chk("the refused (2I, parity, Z, N) chart is reported, not hidden",
        with_ZN()[0] > len(X), True)

    # THE MEMBER SET IS NEW.
    mine, theirs, common = disjoint_from_nucbands()
    chk("no nuclide is shared with nucbands -- a different member set",
        common, 0)
    chk("and 23 of the 24 nuclides carry a level with BOTH numbers",
        mine, 23)
    # THE GROUND FOR THE ZERO, CORRECTED.  The ranges are NOT disjoint.
    (lo, hi), (tlo, thi), shared_A = a_ranges()
    chk("the two mass ranges OVERLAP -- nucbands contains this one",
        (tlo <= lo and hi <= thi), True)
    chk("so the zero is about the tabulations, not the ranges: 0 shared A",
        shared_A, 0)
    chk("and the source's title understates its own table: 132 levels above 168",
        above_title_range(), (132, 174))
    chk("and both sets are non-empty, so the zero means something",
        (mine > 0, theirs > 0), (True, True))

    # SEATING.
    c, held = cell_is_unoccupied()
    chk("no seated index holds this cell", held, [])
    chk("it is registered", "deformedbands.index" in
        [nm for nm, *_r in registry.rows()], True)
    chk("and registry no longer excuses it", "deformed" in registry.NOT_AN_INDEX
        and "deformedbands" in registry.NOT_AN_INDEX, False)

    print("deformedbands selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


def report():
    X = index()
    print("=" * 79)
    print("DOCKET 36b -- THE DEFORMED TWO-QUASIPARTICLE LEVELS, SEATED")
    print("=" * 79)
    print()
    print("SOURCE  %s" % SOURCE[0].split(".")[0])
    print("        the capture is total: %s entries, bands, bandhead states"
          % (deformed.census2(),))
    print()
    print("1. THE MEMBERS")
    print("     levels carrying both quantum numbers   %5d" % len(levels()))
    print("     levels with a spin and no parity       %5d   REFUSED"
          % len(no_parity()))
    mine, theirs, common = disjoint_from_nucbands()
    print("     nuclides here / in nucbands / shared   %3d / %3d / %d"
          % (mine, theirs, common))
    print("   A NEW MEMBER SET, not a recharting: no nuclide in common.")
    print()
    print("2. THE CHART")
    print("     cells    %d" % len(X))
    print("     channel  K%d" % mi.K(X))
    print("     cell     %s" % (cell(),))
    ar, vac, K, why = free_channel()
    print("   %s." % why.upper())
    print()
    print("3. WHAT IS REFUSED, EACH AGAINST A NUMBER")
    d, n, r = band_number_is_a_label()
    print("     band number   %d distinct over %d entries, ratio %.4f -- a "
          "row label" % (d, n, r))
    print("     energy        a magnitude, and 61 bandheads are printed")
    print("                   relative to an unknown offset")
    zn = with_ZN()
    print("     Z and N       the HOST nuclide's, not the level's.  Charted")
    print("                   anyway: %d cells, K%d, cell %s -- and still "
          "refused." % zn)
    print()
    print("4. SEATING")
    c, held = cell_is_unoccupied()
    print("     cell %s held by: %s" % (c, ", ".join(held) or "NOBODY"))
    print("   %s" % grounds_do_not_apply())
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
