#!/usr/bin/env python3
r"""
spin4.py -- THE SPIN-4 MESONS.  THE TREE'S ONLY K4, AND THE LAST EMPTY
CHANNEL FILLED.  DOCKET 34.

    python3 spin4.py             the reading
    python3 spin4.py --selftest  fixtures

M, on the candidate DOCKET 33 found and refused: "still indexable.  Just
contains no mass.  But a legitimate index.  Build it and seat it."

===============================================================================
0. WHAT WAS REFUSED, AND WHY THE REFUSAL WAS THE WRONG SHAPE
===============================================================================

DOCKET 33's member sub-population sweep found this chart and turned it down on
the reach gate: two of the ten members carry no printed mass, so a mass-cut
sweep never reaches the full set and the K4 "rested on rows PDG cannot place
in a reach."

    THAT ARGUMENT USED THE WRONG REACH.  Mass is not a reach for this member
    set -- it is not even total over it, and `mesons.py` already refuses mass
    as a coordinate for exactly that reason.  Refusing an index because a
    variable it never claimed fails to order it is not a test of the index.

    THE REACH THIS SET ACTUALLY HAS IS PDG's OWN STATUS, and it is TOTAL: every
    row carries one.  Status orders states by how established they are, which
    is what a reach is for -- how much of the table you admit.  Swept on it,
    section 3 is the answer, and it is not the answer the mass sweep gave.

===============================================================================
1. THE MEMBERS
===============================================================================

The ten mesons of spin 4 -- 2J = 8 -- read from `mesons.rows()`, which reads
the PDG capture.  Four states and their charge partners:

    a(4)(1970)      isovector, three charges
    f(4)(2050)      isoscalar, neutral
    K(4)*(2045)     isodoublet, four charges
    K(4)(2500)      isodoublet, two charges, PDG STATUS 2

The last is the one the mass sweep tripped on.  It is in the table, it has a
spin, a parity, an isospin and a charge; what it does not have is a mass
entry.  An index of quantum numbers does not need one.

===============================================================================
2. THE COORDINATES
===============================================================================

    P     parity
    2I    isospin, doubled
    Q3    electric charge in thirds

2J IS NOT A COORDINATE HERE and could not be: it is constant at 8 over the
whole member set, and a constant carries no information.  Dropping it is what
makes the EFFECTIVE ARITY 3 rather than 4, and that number is the whole reason
this index matters -- see section 4.

===============================================================================
3. THE REACH SWEEP, ON THE REACH THIS SET HAS
===============================================================================

    status <= 0    8 members   7 cells   K5
    status <= 1    8 members   7 cells   K5
    status <= 2   10 members   9 cells   K4
    status <= 3   10 members   9 cells   K4
    status <= 4   10 members   9 cells   K4

    THE CHANNEL MOVES WITH THE REACH, so `boxinvariance` SEATS it: K4 is a
    property of the data and not of the construction.

    AND THE MOVE IS ITSELF THE FINDING, recorded rather than smoothed.  On the
    ESTABLISHED states alone this index is K5.  It is K4 only once PDG's
    status-2 states are admitted.  BOTH READINGS ARE TRUE and which one you
    get depends on how much of the table you accept -- so anyone quoting the
    K4 must quote the condition with it.  `reach()` prints both.

    THE TWO TESTS DISAGREE HERE AND THE FILE SAYS SO.  `boxinvariance` wants
    the channel to MOVE and it does.  The overlap ruling's reach gate wants it
    STABLE, and a channel arriving at the last cut is a late arrival by that
    gate's own wording.  The gate governs coarsenings of a seated member set;
    this is a new member set, as `fundamental`, `mesons` and `baryons` were.
    That is the ground for seating it, and the disagreement is on the record
    rather than resolved by picking the convenient test.

===============================================================================
4. WHY THIS ONE IS DIFFERENT: K4 IS THE CHANNEL ARITY CANNOT BUY
===============================================================================

`overlaprule.py` section 3c: `statistics` closes for EVERY arity-2 chart,
measured at 105 of 105 across this tree, because `kdet` returns True when
k >= d.  K4 = {information, statistics} is the one channel above K1 whose
extra content over K1 is exactly that free bit, and nothing in `hlaw.LAWFUL`
forces statistics from information.

    SO EVERY K4 BEFORE THIS ONE WAS ARITY 2 AND EVERY ONE WAS REFUSED --
    `ions (sl, tl)`, `madrule (S_a, l_d)`, `fundamental (Q3, GEN)` and
    `madrule at l_d = 0`.  Four charts, four refusals, one reason.

    THIS CHART IS ARITY 3, where statistics closes 59 of 125.  The bit is
    EARNED.  It is the first arity-3-or-more chart to reach K4 anywhere in
    this tree, and seating it fills the last empty channel: ALL EIGHT ARE NOW
    OCCUPIED.

    WHAT THAT DOES AND DOES NOT MEAN.  It means the channel census is
    complete: every down-set of the hierarchy law is carried by something.  It
    does NOT mean the master index is complete -- `registry.COMPLETE` is False
    and stays False, and a full channel census is a statement about eight
    cells, not about how many indexes exist.
"""

import sys

import hlaw
import mesons
import mi
import pdgcapture

SOURCE = (
    "Read from `mesons.rows()`, the seated meson index, which reads "
    "captures/PDG-2026.tsv.  The PDG status used as the reach comes from the "
    "same capture.  Nothing is written down here.",
    ("research/warp-drive/captures/PDG-2026.tsv",),
)

NAMES = ("P", "2I", "Q3")
ARITY = len(NAMES)
SPIN2 = 8                       # 2J = 8, spin 4
STATUS_CUTS = (0, 1, 2, 3, 4)

_C = {}


def _status():
    if "st" not in _C:
        _C["st"] = {int(r["pdgid"]): int(r["status"])
                    for r in pdgcapture.read()}
    return _C["st"]


def rows(status=None):
    """[(name, pdgid, P, 2I, Q3, status)] -- the spin-4 mesons.

    `status` caps PDG's own confidence flag, which is this set's reach.
    """
    st = _status()
    return [(n, p, P, i, q, st[p])
            for n, p, j, P, i, q in mesons.rows()
            if j == SPIN2 and (status is None or st[p] <= status)]


def index(status=None):
    return frozenset((P, i, q) for _n, _p, P, i, q, _s in rows(status))


def massless():
    """[name] -- the members PDG prints no mass for.  Charted anyway."""
    by = {int(r["pdgid"]): r["mass_MeV"] for r in pdgcapture.read()}
    return sorted(n for n, p, _P, _i, _q, _s in rows() if by[p] == "?")


def spin_is_constant():
    """(the one value of 2J, is it constant?) -- why 2J is not a coordinate."""
    v = {j for _n, _p, j, _P, _i, _q in mesons.rows() if j == SPIN2}
    return (sorted(v), len(v) == 1)


def closers(X=None):
    X = frozenset(index() if X is None else X)
    cl, _b = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def cell(status=None):
    return mi.cell(index(status))


def reach():
    """[(status cut, members, cells, K)] -- section 3, on a TOTAL reach."""
    out = []
    for c in STATUS_CUTS:
        R = rows(c)
        X = index(c)
        out.append((c, len(R), len(X), mi.K(X) if len(X) > 1 else None))
    return out


def channel_moves():
    """(does the channel move with the reach?, the channels seen)."""
    ks = sorted({k for _c, _n, _x, k in reach() if k is not None})
    return (len(ks) > 1, ks)


def established_reading():
    """(cells, K) on PDG's established states alone -- the other true answer."""
    X = index(1)
    return (len(X), mi.K(X))


def arity_freeness():
    """{language: (closes, charts)} at arity 2 -- overlaprule's measurement,
    imported so this file does not restate it."""
    import overlaprule as OR
    return OR.arity2_freeness()


def report():
    X = index()
    print("=" * 74)
    print("THE SPIN-4 MESONS -- the tree's only K4.  DOCKET 34")
    print("=" * 74)
    print()
    print("M: \"still indexable.  Just contains no mass.  But a legitimate")
    print("index.  Build it and seat it.\"")
    print()
    print("1. THE MEMBERS: %d mesons of spin 4." % len(rows()))
    print("   %-16s %-8s %-4s %-5s %-5s %s"
          % ("name", "pdgid", "P", "2I", "Q3", "status"))
    for n, p, P, i, q, s in sorted(rows()):
        print("   %-16s %-8d %-4d %-5d %-5d %d" % (n, p, P, i, q, s))
    print()
    print("   PDG prints no mass for: %s" % ", ".join(massless()))
    print("   Charted anyway.  An index of quantum numbers does not need one,")
    print("   and mesons.py already refuses mass as a coordinate.")
    print()
    print("2. THE CHART on %s.  2J is constant at %d and so is not a"
          % (", ".join(NAMES), SPIN2))
    print("   coordinate -- which makes the EFFECTIVE ARITY %d." % ARITY)
    print("   cells    %d of %d members" % (len(X), len(rows())))
    print("   cell     %s" % (cell(),))
    print("   closes   %s" % (", ".join(closers()) or "NOTHING"))
    print()
    print("3. THE REACH SWEEP, on PDG STATUS -- which is TOTAL, unlike mass.")
    print("   %-12s %-9s %-7s %s" % ("status <=", "members", "cells", "K"))
    for c, n, x, k in reach():
        print("   %-12d %-9d %-7d %s" % (c, n, x, "K%d" % k if k is not None else "-"))
    moves, ks = channel_moves()
    print("   the channel MOVES with the reach: %s  %s" % (moves, ks))
    print("   so boxinvariance SEATS it -- K4 is a property of the data.")
    ec, ek = established_reading()
    print()
    print("   AND THE MOVE IS THE FINDING.  On PDG's ESTABLISHED states alone")
    print("   this index is %d cells at K%d.  It is K4 only once the status-2"
          % (ec, ek))
    print("   states are admitted.  Both readings are true; quote the K4 with")
    print("   its condition.")
    print()
    print("4. WHY THIS ONE IS DIFFERENT.")
    f = arity_freeness()
    print("   at arity 2, statistics closes %d of %d charts -- FREE"
          % f["statistics"])
    print("   K4's extra content over K1 is exactly that bit, and no law")
    print("   forces it.  Every K4 before this was arity 2 and every one was")
    print("   refused.  THIS IS ARITY %d." % ARITY)
    print()
    print("   ALL EIGHT CHANNELS ARE NOW OCCUPIED.  That is a statement about")
    print("   eight cells.  registry.COMPLETE is still False.")
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    R = rows()
    chk("ten spin-4 mesons", len(R), 10)
    chk("and every one really is spin 4 -- read from the seated index",
        sorted({j for _n, _p, j, _P, _i, _q in mesons.rows()
                if j == SPIN2}), [8])
    chk("four states: a(4), f(4), K(4)* and K(4)",
        sorted({n.split("(")[0] + "(4)" for n, *_x in R}),
        ["K(4)", "a(4)", "f(4)"])
    chk("PDG prints no mass for exactly two of them", massless(),
        ["K(4)(2500)+", "K(4)(2500)-"])
    chk("and they are charted anyway -- mass is not a coordinate",
        "mass" in NAMES, False)

    # section 2
    chk("2J is constant over the member set, so it is not a coordinate",
        spin_is_constant(), ([8], True))
    chk("EFFECTIVE ARITY 3", ARITY, 3)
    X = index()
    chk("nine cells over ten members", (len(X), len(R)), (9, 10))
    chk("cell (4, 5, 3)", cell(), (4, 5, 3))
    chk("AND IT CLOSES information AND statistics -- K4", closers(),
        ["information", "statistics"])
    chk("K4 is the channel number", mi.K(X), 4)

    # section 3, on the reach this set HAS
    Rc = reach()
    chk("five status cuts swept", len(Rc), len(STATUS_CUTS))
    chk("THE CHANNEL MOVES WITH THE REACH -- K5 then K4",
        channel_moves(), (True, [4, 5]))
    chk("on the established states alone it is 7 cells at K5",
        established_reading(), (7, 5))
    chk("and the two status-2 rows are what take it to K4",
        sorted({s for _n, _p, _P, _i, _q, s in R}), [0, 2])
    chk("the mass sweep could not see this because mass is NOT TOTAL here",
        len(massless()) > 0, True)

    # section 4, the thing that makes it matter
    f = arity_freeness()
    # RE-PINNED 105 -> 135.  Thirty arity-2 charts arrived since this was
    # pinned; six of them are DOCKET 51's, from declaring NAMES on `phonondex`
    # and `kpointdex`.  THE READING IS UNMOVED -- statistics still closes every
    # one, which is the whole of what this fixture is for, and the next line's
    # conclusion about K4 at arity 2 stands on that unchanged fact.
    chk("statistics closes every arity-2 chart in the tree -- free",
        f["statistics"], (135, 135))
    chk("so K4 at arity 2 shows join-closure only; THIS is arity 3",
        (ARITY >= 3, f["statistics"][0] == f["statistics"][1]), (True, True))

    import overlap
    chk("no coordinate is a row LABEL",
        [a for a, _d, _n, _r, v in overlap.resolution(X) if v == "LABEL"], [])

    # what is not claimed
    import registry
    chk("COMPLETE stays False -- eight channels is not every index",
        registry.COMPLETE, False)

    print("spin4 selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
