#!/usr/bin/env python3
r"""
quasiparticle.py -- DOCKET 28.  THE ONE GAP DOCKET 27 LEFT OPEN, CLOSED WITH
TWO REFUSALS RATHER THAN A SEATING.

    python3 quasiparticle.py             the reading
    python3 quasiparticle.py --selftest  fixtures

`docket27.py` section 3 named quasiparticles as the one honest gap: phonons,
magnons, excitons and Cooper pairs WOULD pass `registry.py`'s criterion --
they carry quantum numbers -- and they are simply not in the PDG table.  The
docket said indexing them needs another source.  This file went and looked.

THE ANSWER IS THAT THERE IS NOTHING TO SEAT, FOR TWO SEPARATE REASONS, AND
NEITHER IS "WE COULD NOT FIND A FILE".  Both are measured here.

===============================================================================
1. THERE IS NO PDG FOR QUASIPARTICLES, AND THE REASON IS STRUCTURAL
===============================================================================

The Particle Data Group tabulates a meson's spin, parity and isospin because
THOSE ARE PROPERTIES OF THE MESON.  Ask the same of a phonon and the question
does not have an answer of the same kind:

    A phonon's universal quantum numbers are almost nothing -- a boson, spin
    0.  A magnon's are a boson, spin 1.  So does a Cooper pair.  A chart over
    "kinds of quasiparticle" on the numbers they carry UNIVERSALLY would put
    most of them in one cell, and the cell would be telling you about bosons
    rather than about quasiparticles.

    EVERYTHING THAT DISTINGUISHES ONE PHONON MODE FROM ANOTHER IS THE HOST'S.
    A lattice mode is labelled by an irreducible representation of the little
    group of its wavevector, and which group that is depends on the crystal:
    there are 230 space groups in 32 point groups and 73 arithmetic crystal
    classes, banked in `sgcapture.py` and measured there.  The SAME phonon in
    silicon (Fd-3m) and in rock salt (Fm-3m) carries different labels because
    the crystals differ, not because the phonons do.

SO "THE QUASIPARTICLES" IS NOT A MEMBER SET THE WAY "THE PARTICLES" IS.  The
member set would be (material, mode), and that is a materials database, not a
particle table.  This is a finding about the subject, not a failure to fetch:
a PDG for quasiparticles cannot exist in the form PDG takes, because the
quantum numbers are not carried by the thing being catalogued.

    AND A SPACE GROUP IS NOT AN INDEX EITHER.  It is a symmetry group and
    carries no quantum numbers of its own, so it fails the criterion exactly
    as `figure` and `axes` do.  `sgcapture.py` says so in its own header.

===============================================================================
2. ONE FAMILY IS EXACTLY SPECIFIED -- AND BOX INVARIANCE REFUSES IT
===============================================================================

There IS a quasiparticle family that needs no fetch at all, because it is
given by a closed form rather than by measurement: the ANYONS of SU(2)_k, the
topological excitations of a 2-D topologically ordered medium.  For level k
the labels are J = 2j = 0..k, and every quantum number follows:

    topological spin   h = j(j+1)/(k+2),  exactly, as a rational
    quantum dimension  d = sin((J+1)pi/(k+2)) / sin(pi/(k+2))
    fusion             j1 x j2 = |j1-j2| .. min(j1+j2, k-j1-j2)

Three spot checks, and they are in the fixtures rather than in this sentence:
k=1 J=1 gives h = 1/4, the SEMION; k=3 J=2 gives d = the golden ratio, which
is the FIBONACCI anyon; k=2 J=1 gives h = 3/16 and d = sqrt(2).

    THE LAST IS A TRAP AND THE FILE REFUSES TO WALK INTO IT.  SU(2)_2 is
    commonly called "Ising", and it is NOT the Ising category: the Ising anyon
    sigma has h = 1/16 and this has 3/16.  The two are related and distinct.
    `NOT_ISING` records it, because a fixture written against the remembered
    name rather than the computed value would have passed for the wrong
    reason.

THE COORDINATES, DECLARED BEFORE THE CHART WAS RUN.  (k, J) is the anyon's
ADDRESS, not its quantum numbers, and charting an address is a relabelling --
so the chart is on what the anyon DOES under fusion and braiding:

    STAT   0 boson, 1 fermion, 2 anyon, from h mod 1
    ORD    the order of the topological twist: the denominator of h
    NSELF  how many distinct outcomes j x j has
    AB     abelian, d = 1, or not

    AND THE CHART IS REFUSED.  `boxinvariance.py` states the rule: a chart
    whose MEMBERSHIP IS A PREDICATE OVER A BOX can be handed a different box,
    and if the channel never moves then the channel is a property of the rule
    and not of the data.  Swept over k <= 4, 6, 8, 10, 12, 16, 20, 24 the
    channel is K2 AT EVERY BOX.  `boxinvariance.verdict_of()` -- the tree's
    own test, imported and not reimplemented -- returns REFUSE-AS-THEOREM.

===============================================================================
3. WHAT THIS DOES AND DOES NOT CLOSE
===============================================================================

DOCKET 28 CLOSES.  The gap was "we have not looked".  We have looked, and the
answer is that the textbook quasiparticles have no member set of the right
shape, and the one family that does yields a theorem rather than an index.

    WHAT WOULD REOPEN IT.  A materials database -- the phonon-mode tables of
    a fixed set of crystals, with each mode's irrep -- IS a legitimate member
    set: a mode carries a symmetry label and a frequency, and those are
    quantum numbers.  It is (material, mode), it needs a real fetch, and it is
    NOT what DOCKET 27 asked for.  Named here so the door is visibly open
    rather than quietly shut.

    AND NOTE WHAT SECTION 2 DID NOT SHOW.  Box invariance refuses this chart;
    it does not show that no chart of anyons could ever be seated.  A
    different coordinate set over the same members might move with the box.
    The refusal is of the chart that was run, which is the only thing a
    measurement can refuse.
"""

import math
import sys
from fractions import Fraction

import boxinvariance
import hlaw
import mi
import sgcapture

NAMES = ("STAT", "ORD", "NSELF", "AB")
ARITY = len(NAMES)

# The boxes section 2 sweeps.  k = 1 is included and is DEGENERATE: SU(2)_1
# has two abelian anyons and no non-abelian one, so it cannot exhibit the
# distinction AB draws.  boxinvariance.channels_of() excludes a degenerate box
# from the verdict and still reports it.
BOXES = (4, 6, 8, 10, 12, 16, 20, 24)

# Section 2's trap, banked so a fixture tests the value and not the name.
NOT_ISING = ("SU(2)_2 is not the Ising category: its J=1 has h = 3/16, the "
             "Ising sigma has h = 1/16")

# The universal quantum numbers of the textbook quasiparticles -- section 1.
# NOT A CAPTURE AND NOT AN INDEX: four rows of textbook fact, here only to be
# counted, and the count is the point.  Every one of them is a boson.
UNIVERSAL = (("phonon", 0), ("magnon", 1), ("Cooper pair", 0), ("exciton", 0))


def anyons(k):
    """[J] -- J = 2j runs 0..k, so SU(2)_k has k+1 anyons."""
    return list(range(k + 1))


def spin(J, k):
    """The topological spin h = j(j+1)/(k+2), EXACT, as a Fraction."""
    return Fraction(J * (J + 2), 4 * (k + 2))


def dim(J, k):
    """The quantum dimension.  Irrational in general -- never a coordinate."""
    return math.sin((J + 1) * math.pi / (k + 2)) / math.sin(math.pi / (k + 2))


def fuse(J1, J2, k):
    """[J] in J1 x J2 -- the truncated Clebsch-Gordan series."""
    return list(range(abs(J1 - J2), min(J1 + J2, 2 * k - J1 - J2) + 1, 2))


def coords(J, k):
    """(STAT, ORD, NSELF, AB) -- what the anyon DOES.  Section 2."""
    h = spin(J, k)
    frac = h - int(h)
    stat = 0 if frac == 0 else 1 if frac == Fraction(1, 2) else 2
    return (stat, h.denominator, len(fuse(J, J, k)),
            1 if abs(dim(J, k) - 1) < 1e-12 else 0)


def index(K=12):
    """The anyon chart over every SU(2)_k with k <= K.  REFUSED: section 2."""
    return frozenset(coords(J, k) for k in range(1, K + 1) for J in anyons(k))


def members(K=12):
    return sum(len(anyons(k)) for k in range(1, K + 1))


def closers(X):
    X = frozenset(X)
    cl, _b = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def sweep():
    """[(name, cells, K, closers, 0, 0, degenerate)] -- boxinvariance's shape.

    The row shape is `boxinvariance.box_sweep()`'s so that `channels_of()` and
    `verdict_of()` read it unchanged.  An instrument imports the test; it does
    not carry its own copy of the rule.
    """
    out = []
    for K in BOXES:
        X = index(K)
        out.append(("k <= %d" % K, len(X), mi.K(X), closers(X), 0, 0,
                    K < 3))
    return out


def verdict():
    """('SEAT'|'REFUSE-AS-THEOREM', why) -- boxinvariance's, not ours."""
    return boxinvariance.verdict_of(sweep())


def spot_checks():
    """[(what, computed, expected)] -- the three anyons everyone knows."""
    return [("semion h, SU(2)_1 J=1", spin(1, 1), Fraction(1, 4)),
            ("Fibonacci d, SU(2)_3 J=2", round(dim(2, 3), 9),
             round((1 + 5 ** 0.5) / 2, 9)),
            ("SU(2)_2 J=1 h", spin(1, 2), Fraction(3, 16)),
            ("SU(2)_2 J=1 d", round(dim(1, 2), 9), round(2 ** 0.5, 9))]


def host_carries_it():
    """(space groups, point groups, arithmetic classes) -- section 1.

    Read from `sgcapture.py`, which banks them from spglib.  This is the
    measurement behind "the label is the host's": there are this many distinct
    symmetry settings a crystal can have, and the mode label follows the
    setting.
    """
    c = sgcapture.counts()
    return (c["space groups"], c["point groups"],
            c["arithmetic crystal classes"])


def universal_is_almost_nothing():
    """(kinds, distinct (statistics, spin) pairs) -- section 1's first claim.

    Every one of the four is a boson, and three of the four share a spin, so
    the universal numbers put them on 2 cells.  A chart with that resolution
    is reporting on bosons.
    """
    return (len(UNIVERSAL), len({(0, s) for _n, s in UNIVERSAL}))


def report():
    print("=" * 74)
    print("DOCKET 28 -- the quasiparticle gap, closed with two refusals")
    print("=" * 74)
    print()
    print("1. THERE IS NO PDG FOR QUASIPARTICLES, AND THE REASON IS")
    print("   STRUCTURAL.")
    n, cells = universal_is_almost_nothing()
    print("   %d textbook kinds on %d cells of their UNIVERSAL numbers --"
          % (n, cells))
    print("   every one a boson.  A chart at that resolution reports on")
    print("   bosons, not on quasiparticles.")
    sg, pg, ac = host_carries_it()
    print()
    print("   What distinguishes one mode from another is THE HOST'S:")
    print("     %3d space groups" % sg)
    print("     %3d point groups" % pg)
    print("     %3d arithmetic crystal classes" % ac)
    print("   banked in sgcapture.py.  The member set would be")
    print("   (material, mode) -- a materials database, not a particle table.")
    print()
    print("2. THE ONE EXACTLY-SPECIFIED FAMILY: SU(2)_k ANYONS.")
    for what, got, want in spot_checks():
        print("   %-26s %-14s expected %-14s %s"
              % (what, got, want, "ok" if got == want else "DIFFERS"))
    print("   %s" % NOT_ISING)
    print()
    print("   THE BOX SWEEP.")
    print("   %-10s %-7s %-4s %-14s %s"
          % ("box", "cells", "K", "closes", "degenerate"))
    for nm, nc, k, cl, _j, _m, deg in sweep():
        print("   %-10s %-7d K%-3d %-14s %s"
              % (nm, nc, k, ", ".join(cl) or "NOTHING", deg))
    v, why = verdict()
    print()
    print("   VERDICT  %s" % v)
    print("   %s" % why)
    print("   boxinvariance.verdict_of() -- the tree's own test, imported.")
    print()
    print("3. WHAT WOULD REOPEN IT.  A materials database of phonon modes with")
    print("   each mode's irrep IS a legitimate member set.  It needs a real")
    print("   fetch and it is not what DOCKET 27 asked for.  Named so the door")
    print("   is visibly open rather than quietly shut.")
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    # -- section 1
    chk("four textbook kinds land on two cells of their universal numbers",
        universal_is_almost_nothing(), (4, 2))
    chk("and every one of them is a BOSON -- integer spin, no exception",
        sorted({s == int(s) for _n, s in UNIVERSAL}), [True])
    chk("the host's symmetry settings, from the banked capture",
        host_carries_it(), (230, 32, 73))

    # -- section 2, the anyon arithmetic, against values everyone knows
    for what, got, want in spot_checks():
        chk(what, got, want)
    chk("SU(2)_2 is NOT Ising, and the file says so rather than relying on "
        "the name", spin(1, 2) != Fraction(1, 16), True)
    chk("SU(2)_k has k+1 anyons", [len(anyons(k)) for k in (1, 2, 3, 10)],
        [2, 3, 4, 11])
    chk("the vacuum is a boson of dimension 1 at every level",
        sorted({(spin(0, k), round(dim(0, k), 9)) for k in range(1, 25)}),
        [(Fraction(0, 1), 1.0)])
    # FUSION TRUNCATION IS THE WHOLE DIFFERENCE from ordinary SU(2), so the
    # fixture picks a case where it actually bites.  j=1 with j=1 is 0,1,2
    # classically; at k=2 the level cuts it to the vacuum alone, at k=10 it
    # does not cut it at all.
    chk("fusion truncates: 1x1 is the vacuum alone at k=2", fuse(2, 2, 2), [0])
    chk("and the same fusion at k=10 keeps all three outcomes",
        fuse(2, 2, 10), [0, 2, 4])
    chk("the top anyon fuses with itself to the vacuum alone",
        [fuse(k, k, k) for k in (2, 3, 5)], [[0], [0], [0]])

    # -- the chart, and the refusal
    X = index(12)
    chk("90 members over 53 cells at k <= 12", (members(12), len(X)), (90, 53))
    chk("arity 4", len(next(iter(X))), 4)
    import overlap
    chk("no coordinate is a row LABEL -- the chart is not the address",
        [a for a, _d, _n, _r, v in overlap.resolution(X) if v == "LABEL"], [])
    rows = sweep()
    chk("eight boxes swept", len(rows), len(BOXES))
    chk("AND THE CHANNEL IS K2 AT EVERY ONE OF THEM",
        sorted({r[2] for r in rows}), [2])
    chk("so the tree's own test refuses it as a theorem", verdict()[0],
        "REFUSE-AS-THEOREM")
    chk("and the cell DOES move with the box, which is why the channel not "
        "moving is the finding",
        len({mi.cell(index(K)) for K in BOXES}) > 1, True)

    # the refusal is of a chart, not of a subject -- section 3
    chk("nothing here is seated in the registry",
        [r for r in __import__("registry").REGISTERED
         if r[0] in ("quasiparticle", "sgcapture")], [])
    chk("and the file says what would reopen the docket",
        "IS a legitimate member set" in " ".join(__doc__.split()), True)

    print("quasiparticle selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
