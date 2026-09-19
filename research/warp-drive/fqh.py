#!/usr/bin/env python3
r"""
fqh.py -- THE QUASIPARTICLES OF THE FRACTIONAL QUANTUM HALL STATES.  DOCKET 30.

    python3 fqh.py             the reading
    python3 fqh.py --selftest  fixtures

===============================================================================
0. WHY THIS EXISTS: DOCKET 28 REFUSED THE WRONG OBJECT
===============================================================================

M: "And they need to be seated.  Why were the indexes not seated?"

DOCKET 28 refused an anyon chart on box invariance, and the refusal was sound
FOR THE CHART IT WAS RUN ON.  Re-examined, that chart was the wrong member set,
and the box-invariance result was telling us so rather than telling us anyone
had failed:

    IT CHARTED THE ANYONS OF SU(2)_k FOR EVERY k UP TO A CAP.  Each k is a
    DIFFERENT TOPOLOGICAL ORDER -- a different physical system, not more of the
    same one.  So the "box" was not a reach at all; it was a choice of HOW MANY
    UNIVERSES TO INCLUDE.  The Standard Model analogue would be charting the
    particles of every SU(2) gauge theory at once and calling it an index of
    matter.  Of course the channel did not move with that box: nothing about
    the data was being varied.

    THE TEST WAS RIGHT AND THE OBJECT WAS WRONG, and `boxinvariance.py` says
    exactly this in its own section 1 -- "CHECK whether a chart is enumerated
    before claiming it is" -- the same warning, pointed the other way.

THIS FILE CHARTS A REACH INSTEAD OF A UNION.  The members are quasiparticles of
the LAUGHLIN STATES, one family of one kind of system, indexed by the filling
fraction at which the plateau appears -- and the filling fraction is a
MEASUREMENT, the quantised Hall conductance.  Varying the reach is then the
same move as varying Z: more of the same thing, further out.

    AND IT PASSES.  The channel MOVES with the box -- K2 at m <= 5 and m <= 7,
    K0 from m <= 9 onward -- so `boxinvariance.verdict_of()` returns SEAT.
    `sweep()` is the measurement and it is the whole of section 3.

===============================================================================
1. THE MEMBERS
===============================================================================

One member is a quasiparticle of the Laughlin state at filling nu = 1/m, m
odd.  The state has exactly m of them, labelled j = 0 .. m-1, and j = 0 is the
vacuum.  Reach: m <= 25, declared, twelve states and 168 quasiparticles.

    THREE OF THE TWELVE STATES ARE OBSERVED -- nu = 1/3, 1/5 and 1/7 -- and
    the rest are the sequence's own continuation.  That is the same shape as
    `fibred`, which charts 170 electrons where 118 elements are known, and it
    is declared here for the same reason: a rule's continuation is not a
    measurement and must not be presented as one.  `observed_states()` names
    the three.

    THE e/3 QUASIPARTICLE IS NOT A PREDICTION.  Its fractional charge was
    measured directly by shot noise in 1997, and it is the single most
    consequential fact in this index: a quasiparticle carrying a FRACTION of
    the electron charge, in a system built only from electrons.  A fixture
    pins it.

===============================================================================
2. THE COORDINATES, DECLARED BEFORE THE CHART WAS RUN
===============================================================================

Every one is EXACT -- computed as a Fraction, never a float -- because the
whole content of this index is that these quantities are rational.

    Q = j/m           the electric charge, in units of e
    theta/pi = j^2/m  the statistics parameter: the phase, over pi, picked up
                      when two of them are exchanged

    STAT    0 boson, 1 fermion, 2 ANYON -- from theta/pi mod 1.  This is the
            coordinate the subject exists for: a value of 2 is a particle that
            is neither a boson nor a fermion, which cannot happen in three
            dimensions.

            AND IT NEVER TAKES THE VALUE 1.  Measured: 150 anyons, 18 bosons,
            ZERO fermions over the 168, and it is forced rather than observed
            -- theta/pi = j^2/m is a half-integer only if m divides 2j^2, and
            m is ODD, so m divides j^2 and the phase is a whole integer
            instead.  A Laughlin quasiparticle can be a boson or an anyon and
            there is no third case.  The fixture proves it over the reach
            rather than quoting the argument.
    ORD     the order of the exchange phase: the denominator of theta/pi.
    CHORD   the order of the charge: the denominator of Q, so 1 for an
            integrally charged quasiparticle and m for the fundamental one.
    M       the inverse filling fraction.  NOT an address: 1/m is the
            quantised Hall conductance in units of e^2/h, which is what the
            experiment actually reads off the plateau, and it is the most
            directly observed number in this index.

    WHAT IS REFUSED.  The label j is the anyon's ADDRESS within its state and
    is not charted -- charting it would be a relabelling, the overlap ruling's
    second ground.  Q and theta themselves are not charted either: they are
    rationals, near-injective over the members, and `overlap.py` calls a
    near-injective coordinate a row label.  Their ORDERS are charted instead,
    which is the part that says what kind of thing the quasiparticle is.
"""

import sys
from fractions import Fraction

import boxinvariance
import hlaw
import mi

SOURCE = (
    "COMPUTED from the Laughlin wavefunction's closed form -- R. B. Laughlin, "
    "Phys. Rev. Lett. 50, 1395 (1983).  No table is read.  The three observed "
    "filling fractions are named in OBSERVED, not fetched.",
    (),
)

NAMES = ("STAT", "ORD", "CHORD", "M")
ARITY = len(NAMES)
REACH = 25

# The Laughlin filling fractions with an experimentally reported plateau.
# NAMED, not fetched, and never used to build the chart -- section 1.
OBSERVED = (3, 5, 7)

# The boxes section 3 sweeps.  m <= 3 is DEGENERATE: a single state cannot
# exhibit a chart whose fourth coordinate is which state you are in.
BOXES = (5, 7, 9, 11, 13, 15, 19, 25)

_C = {}


def states(reach=REACH):
    """[m] -- the odd inverse filling fractions in reach.  m = 1 is the
    integer quantum Hall state and is not a Laughlin state; the sequence
    starts at 3."""
    return list(range(3, reach + 1, 2))


def charge(j, m):
    """The electric charge in units of e.  EXACT."""
    return Fraction(j, m)


def theta(j, m):
    """The statistics parameter theta/pi.  EXACT."""
    return Fraction(j * j, m)


def stat(j, m):
    """0 boson, 1 fermion, 2 anyon -- from theta/pi mod 1."""
    f = theta(j, m) - int(theta(j, m))
    return 0 if f == 0 else 1 if f == Fraction(1, 2) else 2


def rows(reach=REACH):
    """[(m, j, Q, theta, STAT, ORD, CHORD)] -- every quasiparticle in reach."""
    key = ("r", reach)
    if key not in _C:
        out = []
        for m in states(reach):
            for j in range(m):
                Q, th = charge(j, m), theta(j, m)
                out.append((m, j, Q, th, stat(j, m), th.denominator,
                            Q.denominator))
        _C[key] = out
    return _C[key]


def index(reach=REACH):
    return frozenset((s, o, c, m) for m, _j, _Q, _t, s, o, c in rows(reach))


def observed_states():
    """[(m, filling fraction, the fundamental charge it carries)] -- the three
    with a reported plateau.  Reported, never used to build the chart."""
    return [(m, "1/%d" % m, "e/%d" % m) for m in OBSERVED]


def laughlin_state(m):
    """[(j, Q, theta/pi, STAT)] -- one state, in full."""
    return [(j, charge(j, m), theta(j, m), stat(j, m)) for j in range(m)]


def closers(X):
    X = frozenset(X)
    cl, _b = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def cell(reach=REACH):
    return mi.cell(index(reach))


def sweep():
    """boxinvariance's row shape, so its own test reads this unchanged."""
    out = []
    for M in BOXES:
        X = index(M)
        out.append(("m <= %d" % M, len(X), mi.K(X), closers(X), 0, 0, M < 5))
    return out


def verdict():
    """('SEAT'|'REFUSE-AS-THEOREM', why) -- boxinvariance's, not ours."""
    return boxinvariance.verdict_of(sweep())


def anyon_fraction(reach=REACH):
    """(anyons, fermions, bosons) -- how much of the index is neither."""
    c = {0: 0, 1: 0, 2: 0}
    for _m, _j, _Q, _t, s, _o, _ch in rows(reach):
        c[s] += 1
    return (c[2], c[1], c[0])


def fractional_charges(reach=REACH):
    """[(m, the distinct charge denominators the state carries)]."""
    out = {}
    for m, _j, Q, _t, _s, _o, _ch in rows(reach):
        out.setdefault(m, set()).add(Q.denominator)
    return [(m, sorted(v)) for m, v in sorted(out.items())]


def report():
    X = index()
    print("=" * 74)
    print("THE FRACTIONAL QUANTUM HALL QUASIPARTICLES -- DOCKET 30")
    print("=" * 74)
    print()
    print("0. DOCKET 28 REFUSED THE WRONG OBJECT.")
    print("   It charted SU(2)_k for every k -- a UNION OVER THEORIES, not a")
    print("   reach over data, so of course the channel did not move.  This")
    print("   charts one family of one kind of system, indexed by a")
    print("   MEASURED filling fraction.")
    print()
    print("1. THE MEMBERS: %d quasiparticles over %d Laughlin states, m <= %d."
          % (len(rows()), len(states()), REACH))
    print("   observed plateaux, named and NOT used to build the chart:")
    for m, nu, q in observed_states():
        print("     nu = %-5s carries a quasiparticle of charge %s" % (nu, q))
    print()
    print("2. THE nu = 1/3 STATE IN FULL -- the one whose e/3 charge was")
    print("   measured by shot noise in 1997.")
    print("   %-4s %-8s %-10s %s" % ("j", "Q/e", "theta/pi", "statistics"))
    for j, Q, th, s in laughlin_state(3):
        print("   %-4d %-8s %-10s %s"
              % (j, Q, th, ("boson", "fermion", "ANYON")[s]))
    print()
    print("3. THE BOX SWEEP -- and this is why it seats where DOCKET 28's")
    print("   chart did not.")
    print("   %-10s %-7s %-5s %s" % ("box", "cells", "K", "closes"))
    for nm, nc, k, cl, _j, _m, deg in sweep():
        print("   %-10s %-7d K%-4d %s%s"
              % (nm, nc, k, ", ".join(cl) or "NOTHING",
                 "   (degenerate)" if deg else ""))
    v, why = verdict()
    print()
    print("   VERDICT  %s" % v)
    print("   %s" % why)
    print()
    print("4. THE CHART.")
    print("   cells    %d of %d members" % (len(X), len(rows())))
    print("   cell     %s" % (cell(),))
    print("   closes   %s" % (", ".join(closers(X)) or "NOTHING"))
    print()
    a, f, b = anyon_fraction()
    print("5. WHAT THE INDEX IS MADE OF, AND WHAT IT CONTAINS NONE OF.")
    print("   %d anyons, %d bosons, and %d FERMIONS -- %.0f%% of the members"
          % (a, b, f, 100.0 * a / len(rows())))
    print("   are neither a boson nor a fermion, which cannot happen in three")
    print("   dimensions.  That is the subject, not a curiosity.")
    print("   THE ZERO IS FORCED, not observed: theta/pi = j^2/m is a half")
    print("   only if m divides 2j^2, and m is odd, so m divides j^2 and the")
    print("   phase is a whole integer instead.  There is no third case.")
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    # -- the physics, against values that are not this file's to choose
    chk("the nu = 1/3 state has three quasiparticles", len(laughlin_state(3)), 3)
    chk("THE FUNDAMENTAL ONE CARRIES CHARGE e/3 -- measured by shot noise in "
        "1997, not predicted here", charge(1, 3), Fraction(1, 3))
    chk("and nu = 1/5 carries e/5, nu = 1/7 carries e/7",
        [charge(1, m) for m in (5, 7)], [Fraction(1, 5), Fraction(1, 7)])
    chk("its exchange phase is theta = pi/3, neither 0 nor pi",
        theta(1, 3), Fraction(1, 3))
    chk("so it is an ANYON -- neither boson nor fermion", stat(1, 3), 2)
    chk("the vacuum is a boson of zero charge in every state",
        sorted({(charge(0, m), theta(0, m), stat(0, m)) for m in states()}),
        [(Fraction(0), Fraction(0), 0)])
    chk("a Laughlin state at 1/m has exactly m quasiparticles",
        [len(laughlin_state(m)) for m in (3, 5, 7, 9)], [3, 5, 7, 9])
    chk("the charge is always a multiple of the fundamental one",
        sorted({(charge(j, 5) * 5).denominator for j in range(5)}), [1])
    chk("EVERY Laughlin state carries a genuinely fractional charge",
        [m for m, dens in fractional_charges() if m not in dens], [])

    # -- the members
    R = rows()
    chk("twelve states, 168 quasiparticles, m <= 25",
        (len(states()), len(R), REACH), (12, 168, 25))
    chk("three of the twelve have a reported plateau",
        [m for m, _nu, _q in observed_states()], [3, 5, 7])
    chk("and the reach is DECLARED beyond them, not claimed as observed",
        len(states()) > len(OBSERVED), True)

    # -- section 3: the test DOCKET 28's chart failed and this one passes
    S = sweep()
    chk("eight boxes swept", len(S), len(BOXES))
    chk("THE CHANNEL MOVES WITH THE BOX -- K2 then K0",
        sorted({r[2] for r in S}), [0, 2])
    chk("so the tree's own test SEATS it", verdict()[0], "SEAT")
    chk("and DOCKET 28's chart is still refused -- this does not overturn it",
        __import__("quasiparticle").verdict()[0], "REFUSE-AS-THEOREM")

    # -- the chart
    X = index()
    chk("arity 4", len(next(iter(X))), 4)
    chk("30 cells over 168 members", (len(X), len(R)), (30, 168))
    chk("channel K0", mi.K(X), 0)
    chk("cell (K, height, width)", cell(), (0, 15, 4))
    chk("and |X| <= height x width, Dilworth",
        len(X) <= cell()[1] * cell()[2], True)

    import overlap
    chk("no coordinate is a row LABEL",
        [a for a, _d, _n, _r, v in overlap.resolution(X) if v == "LABEL"], [])
    chk("the anyon's ADDRESS j is not among the coordinates", "j" in NAMES,
        False)

    # -- what the index is
    a, f, b = anyon_fraction()
    chk("150 anyons, 18 bosons -- and NOT ONE FERMION", (a, f, b),
        (150, 0, 18))
    chk("no Laughlin quasiparticle is EVER a fermion, and it is forced: "
        "theta/pi = j^2/m is a half only if m | 2j^2, and m is odd, so m | "
        "j^2 and the phase is an integer instead",
        [(m, j) for m, j, _Q, t, _s, _o, _c in R
         if (t - int(t)) == Fraction(1, 2)], [])
    chk("the bosons are exactly the j with m dividing j^2",
        sorted({(m, j) for m, j, _Q, _t, s, _o, _c in R if s == 0}) ==
        sorted({(m, j) for m in states() for j in range(m)
                if (j * j) % m == 0}), True)
    chk("so every state's fundamental quasiparticle is an anyon, no exception",
        sorted({stat(1, m) for m in states()}), [2])

    print("fqh selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
