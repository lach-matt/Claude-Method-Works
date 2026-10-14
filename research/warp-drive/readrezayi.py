#!/usr/bin/env python3
r"""
readrezayi.py -- THE NON-ABELIAN QUANTUM HALL QUASIPARTICLES.  DOCKET 32.

    python3 readrezayi.py             the reading
    python3 readrezayi.py --selftest  fixtures

M: "the non-abelian Hall states (Moore-Read at nu = 5/2, Read-Rezayi at 12/5)
are a further member set and are not in this index -- we do this next."

`fqh.py` seated the ABELIAN Hall quasiparticles, the Laughlin ones.  These are
the other kind: excitations whose exchange does not multiply the state by a
phase but ROTATES IT INSIDE A DEGENERATE SPACE, which is what "non-abelian"
means and is why they are the ones proposed for topological quantum computing.

===============================================================================
1. THE MEMBERS, AND WHY k IS A REACH AND NOT A CHOICE
===============================================================================

One member is a primary field of the Z_k parafermion theory that describes the
Read-Rezayi state RR_k.  Moore-Read IS RR_2; there is no separate construction
for it.  The series sits at

        nu = 2 + k/(k+2)        k = 2 -> 5/2,  k = 3 -> 13/5

    SO k IS TIED TO AN OBSERVED FILLING FRACTION, and that is the whole
    difference from DOCKET 28.  That docket charted SU(2)_k for every k and
    was refused, because varying k there varied WHICH THEORY you were in --
    a union over universes, with nothing about the data being varied.  Here
    each k names a plateau at a definite nu, so varying the reach is varying
    how far up the observed series you have got, exactly as varying Z is.

    THE OBSERVED ONES ARE k = 2 AND k = 3.  nu = 5/2 is Moore-Read; nu = 12/5
    and 13/5 are the k = 3 pair.  The rest of the reach is the series' own
    continuation and is declared as such, never as observation.

===============================================================================
2. THE WEIGHTS ARE VALIDATED AGAINST THE LITERATURE, NOT AGAINST THEMSELVES
===============================================================================

The primaries are Phi^l_m with 0 <= l <= k and l - m even, identified under
(l, m) ~ (k - l, m - k), and

        h = l(l+2) / (4(k+2))  -  m^2 / (4k)

    AND IT REPRODUCES BOTH FIXED POINTS EXACTLY.  These are not this file's to
    choose:

        k = 2   weights {0, 1/16, 1/2}      -- EXACTLY the Ising category, and
                                               1/16 is the sigma the
                                               Moore-Read literature fixes
        k = 3   2/5 among the weights       -- the FIBONACCI tau
        fundamental charge  e/(k+2)          -- e/4 at k=2, e/5 at k=3, both
                                               as published

    AND THAT CLOSES A LOOP ON DOCKET 28.  That docket flagged a trap: SU(2)_2
    is commonly called "Ising" and is not, because its j = 1/2 carries
    h = 3/16 where the Ising sigma carries 1/16.  THE REAL MOORE-READ STATE
    CARRIES 1/16, which this file computes.  So DOCKET 28's chart had the
    wrong PHYSICS as well as the wrong shape, and the caution written there
    against trusting the name turns out to have been the important half.

===============================================================================
3. THE COORDINATES ARE `fqh`'s, DELIBERATELY
===============================================================================

    STAT   0 boson, 1 fermion, 2 anyon, from h mod 1
    ORD    the order of the topological twist: the denominator of h
    CHORD  the order of the quasihole charge
    K      the level, which names the filling fraction

Same frame as the abelian index, so the two are directly comparable and
section 5 can ask whether either nests in the other.  A different frame would
have made that question unaskable, which is reason enough to keep this one.

===============================================================================
4. AND IT SEATS, WHERE DOCKET 28's CHART DID NOT
===============================================================================

The channel MOVES with the box -- K2 at k <= 3, K0 from k <= 4 onward -- so
`boxinvariance.verdict_of()` returns SEAT.  Same test, same tree, opposite
answer to DOCKET 28, and the reason is section 1: this box is a reach.

===============================================================================
5. TWO FINDINGS AGAINST THE ABELIAN INDEX, AND BOTH ARE NEGATIVE RESULTS
===============================================================================

    THE MAJORANA BREAKS DOCKET 30's THEOREM, EXACTLY WHERE IT SHOULD.
    `fqh.py` proved that NOT ONE Laughlin quasiparticle is ever a fermion,
    forced because theta/pi = j^2/m is a half only if m divides 2j^2 and m is
    odd.  THE NON-ABELIAN SERIES CONTAINS FERMIONS: the Ising psi at h = 1/2
    is one, and it is the neutral Majorana fermion of the Moore-Read state.
    So the theorem was never about Hall quasiparticles in general -- it was
    about the abelian ones, and the boundary is precisely where the two
    families part.  `fermions()` names them.

    AND NEITHER INDEX NESTS IN THE OTHER.  DOCKET 31 found the bosonic
    quasiparticles sitting in the boson lattice as a sublattice once it was
    extended by one cell.  Nothing of that kind happens here: on the three
    coordinates they share, the abelian chart has 15 cells and the
    non-abelian 57, they share 8, NEITHER CONTAINS THE OTHER, and neither is
    a sublattice on its own.  `nesting()` is the measurement.  A negative
    result, reported because the positive one at DOCKET 31 would otherwise
    read as a pattern.
"""

import sys
from fractions import Fraction

import boxinvariance
import decomposable as D
import fqh
import hlaw
import mi

SOURCE = (
    "COMPUTED from the Z_k parafermion closed form -- Zamolodchikov and "
    "Fateev (1985); Moore and Read, Nucl. Phys. B 360, 362 (1991); Read and "
    "Rezayi, Phys. Rev. B 59, 8084 (1999).  No table is read.  The weights "
    "are validated against the two values the literature fixes: the Ising "
    "sigma at h = 1/16 and the Fibonacci tau at h = 2/5.",
    (),
)

NAMES = ("STAT", "ORD", "CHORD", "K")
ARITY = len(NAMES)
REACH = 12

# The levels with a reported plateau.  k = 2 is Moore-Read at nu = 5/2; k = 3
# is the 12/5 and 13/5 pair.  NAMED, never used to build the chart.
OBSERVED = {2: ("5/2", "Moore-Read"), 3: ("12/5 and 13/5", "Read-Rezayi k=3")}

# What the literature fixes, and what section 2 checks the formula against.
FIXED_POINTS = (
    ("k=2 is the Ising category", 2, (Fraction(0), Fraction(1, 16),
                                      Fraction(1, 2))),
    ("k=3 carries the Fibonacci tau at 2/5", 3, Fraction(2, 5)),
)

BOXES = (3, 4, 5, 6, 8, 10, 12, 14)

_C = {}


def levels(reach=REACH):
    return list(range(2, reach + 1))


def filling(k):
    """nu = 2 + k/(k+2) -- the plateau RR_k sits at."""
    return 2 + Fraction(k, k + 2)


def fundamental_charge(k):
    """The quasihole charge in units of e: 1/(k+2).  e/4 at k=2, e/5 at k=3."""
    return Fraction(1, k + 2)


def primaries(k):
    """{(l, m): h} -- the Z_k parafermion primaries, identified.

    h = l(l+2)/(4(k+2)) - m^2/(4k), with (l, m) ~ (k-l, m-k).  EXACT: every
    weight is a Fraction, because the content of the index is that they are
    rational.
    """
    key = ("p", k)
    if key not in _C:
        seen = {}
        for l in range(k + 1):
            for m in range(-l, l + 1):
                if (l - m) % 2:
                    continue
                h = Fraction(l * (l + 2), 4 * (k + 2)) - Fraction(m * m, 4 * k)
                ident = min((l, m % (2 * k)), (k - l, (m - k) % (2 * k)))
                seen[ident] = h
        _C[key] = seen
    return _C[key]


def stat(h):
    f = h - int(h)
    return 0 if f == 0 else 1 if f == Fraction(1, 2) else 2


def rows(reach=REACH):
    """[(k, l, m, h, charge, STAT, ORD, CHORD)]."""
    key = ("r", reach)
    if key not in _C:
        out = []
        for k in levels(reach):
            for (l, m), h in sorted(primaries(k).items()):
                Q = Fraction(l, k + 2)
                out.append((k, l, m, h, Q, stat(h), h.denominator,
                            Q.denominator))
        _C[key] = out
    return _C[key]


def index(reach=REACH):
    return frozenset((s, o, c, k) for k, _l, _m, _h, _Q, s, o, c
                     in rows(reach))


def weights(k):
    """The distinct conformal weights of RR_k -- section 2's validation."""
    return sorted(set(primaries(k).values()))


def validation():
    """[(what, computed, expected, agrees)] against the literature."""
    out = []
    w2 = tuple(weights(2))
    out.append((FIXED_POINTS[0][0], w2, FIXED_POINTS[0][2],
                w2 == FIXED_POINTS[0][2]))
    w3 = weights(3)
    out.append((FIXED_POINTS[1][0], Fraction(2, 5) in w3, True,
                Fraction(2, 5) in w3))
    out.append(("the Moore-Read quasihole carries e/4",
                fundamental_charge(2), Fraction(1, 4),
                fundamental_charge(2) == Fraction(1, 4)))
    out.append(("the Read-Rezayi k=3 quasihole carries e/5",
                fundamental_charge(3), Fraction(1, 5),
                fundamental_charge(3) == Fraction(1, 5)))
    out.append(("and the plateaux are nu = 5/2 and 13/5",
                (filling(2), filling(3)),
                (Fraction(5, 2), Fraction(13, 5)),
                (filling(2), filling(3)) == (Fraction(5, 2),
                                             Fraction(13, 5))))
    return out


def fermions(reach=REACH):
    """[(k, l, m, h)] -- section 5.  `fqh` has none of these and cannot."""
    return [(k, l, m, h) for k, l, m, h, _Q, s, _o, _c in rows(reach)
            if s == 1]


def nesting():
    """(abelian cells, non-abelian cells, shared, A in N, N in A, A sub, N sub).

    On the three coordinates the two indexes share.  Section 5's negative
    result, measured rather than assumed from DOCKET 31's positive one.
    """
    A = frozenset(c[:3] for c in fqh.index())
    N = frozenset(c[:3] for c in index())
    return (len(A), len(N), len(A & N), A <= N, N <= A,
            D.gen(A) == A, D.gen(N) == N)


def closers(X):
    X = frozenset(X)
    cl, _b = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def cell(reach=REACH):
    return mi.cell(index(reach))


def sweep():
    out = []
    for K in BOXES:
        X = index(K)
        out.append(("k <= %d" % K, len(X), mi.K(X), closers(X), 0, 0, K < 3))
    return out


def verdict():
    return boxinvariance.verdict_of(sweep())


def report():
    X = index()
    print("=" * 74)
    print("THE NON-ABELIAN HALL QUASIPARTICLES -- DOCKET 32")
    print("=" * 74)
    print()
    print("1. THE SERIES.  Moore-Read IS RR_2; there is no separate one.")
    print("   %-4s %-8s %-10s %-11s %s"
          % ("k", "nu", "charge", "primaries", "observed"))
    for k in levels():
        p = OBSERVED.get(k)
        print("   %-4d %-8s e/%-8d %-11d %s"
              % (k, filling(k), k + 2, len(primaries(k)),
                 "%s (%s)" % p if p else ""))
    print()
    print("2. VALIDATED AGAINST THE LITERATURE, not against itself.")
    for what, got, want, good in validation():
        print("   [%s] %-42s %s" % ("ok" if good else "XX", what, got))
    print()
    print("   DOCKET 28 warned that SU(2)_2 is NOT Ising -- its j=1/2 carries")
    print("   h = 3/16 where the Ising sigma carries 1/16.  The real")
    print("   Moore-Read state carries 1/16, computed above.  So that chart")
    print("   had the wrong PHYSICS as well as the wrong shape.")
    print()
    print("3. THE BOX SWEEP.")
    print("   %-10s %-7s %-5s %s" % ("box", "cells", "K", "closes"))
    for nm, nc, k, cl, _j, _m, _d in sweep():
        print("   %-10s %-7d K%-4d %s" % (nm, nc, k, ", ".join(cl) or "NOTHING"))
    v, why = verdict()
    print("   VERDICT  %s -- %s" % (v, why))
    print()
    print("4. THE CHART.  %d cells of %d members, cell %s, closes %s"
          % (len(X), len(rows()), cell(), ", ".join(closers(X)) or "NOTHING"))
    print()
    F = fermions()
    print("5. THE MAJORANA BREAKS DOCKET 30's THEOREM, WHERE IT SHOULD.")
    print("   fqh.py: NOT ONE Laughlin quasiparticle is a fermion.")
    print("   here: %d are.  The first is the Ising psi at h = 1/2 -- the"
          % len(F))
    print("   neutral Majorana fermion of the Moore-Read state.")
    for k, l, m, h in F[:5]:
        print("     k=%-3d (l,m)=(%d,%-3d)  h = %s" % (k, l, m, h))
    print("   So the theorem was about the ABELIAN ones, and this is the")
    print("   boundary.")
    print()
    na, nn, sh, ain, nin, asub, nsub = nesting()
    print("6. AND NEITHER INDEX NESTS IN THE OTHER.")
    print("   abelian %d cells, non-abelian %d, shared %d" % (na, nn, sh))
    print("   abelian inside non-abelian? %s    the reverse? %s" % (ain, nin))
    print("   is either a sublattice on its own? %s / %s" % (asub, nsub))
    print("   DOCKET 31 found the bosonic quasiparticles nesting in the boson")
    print("   lattice.  Nothing of that kind happens here, and it is reported")
    print("   so the one positive result is not read as a pattern.")
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    # -- section 2: the literature, which is not this file's to choose
    for what, got, want, _g in validation():
        chk(what, got, want)
    chk("k=2 has three primaries -- Ising has three fields",
        len(primaries(2)), 3)
    chk("and the Moore-Read state IS RR_2, not a separate construction",
        filling(2), Fraction(5, 2))
    chk("SU(2)_2's 3/16 is NOT among the real Moore-Read weights, which is "
        "DOCKET 28's trap closing", Fraction(3, 16) in weights(2), False)

    # -- the members
    R = rows()
    chk("eleven levels in reach, k = 2 to 12", len(levels()), 11)
    chk("RR_k has k(k+1)/2 primaries",
        [len(primaries(k)) for k in (2, 3, 4, 5)], [3, 6, 10, 15])
    chk("two levels have a reported plateau", sorted(OBSERVED), [2, 3])
    chk("and the reach is declared past them", len(levels()) > len(OBSERVED),
        True)

    # -- section 4: the test DOCKET 28's chart failed
    S = sweep()
    chk("THE CHANNEL MOVES WITH THE BOX", sorted({r[2] for r in S}), [0, 2])
    chk("so the tree's own test SEATS it", verdict()[0], "SEAT")
    chk("while DOCKET 28's chart is still refused",
        __import__("quasiparticle").verdict()[0], "REFUSE-AS-THEOREM")

    # -- the chart
    X = index()
    chk("arity 4", len(next(iter(X))), 4)
    chk("363 members over 78 cells", (len(R), len(X)), (363, 78))
    chk("channel K0", mi.K(X), 0)
    import overlap
    chk("no coordinate is a row LABEL",
        [a for a, _d, _n, _r, v in overlap.resolution(X) if v == "LABEL"], [])

    # -- section 5: the Majorana, and the theorem it bounds
    F = fermions()
    chk("THE NON-ABELIAN SERIES CONTAINS FERMIONS where the abelian cannot",
        len(F) > 0, True)
    # TESTED BY WEIGHT, NOT BY LABEL.  Which (l, m) survives the
    # identification is an artefact of this file's canonical-rep choice; the
    # weight is the physics.
    chk("exactly one fermion at k=2, and it is the Ising psi at h = 1/2 -- "
        "the neutral Majorana of the Moore-Read state",
        [h for k, _l, _m, h in F if k == 2], [Fraction(1, 2)])
    chk("six fermions over the whole reach, and none at k=3",
        (len(F), [1 for k, _l, _m, _h in F if k == 3]), (6, []))
    chk("fqh has none, and that theorem is unchanged",
        [1 for _m, _j, _Q, t, _s, _o, _c in fqh.rows()
         if (t - int(t)) == Fraction(1, 2)], [])

    # -- section 5's negative result
    na, nn, sh, ain, nin, asub, nsub = nesting()
    chk("neither index nests in the other", (ain, nin), (False, False))
    chk("they share eight cells and neither is a sublattice",
        (na, nn, sh, asub, nsub), (15, 57, 8, False, False))

    print("readrezayi selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
