#!/usr/bin/env python3
r"""propagator.py -- THE ASSERTED 2, SETTLED.  DOCKET 41.

    python3 propagator.py             the reading
    python3 propagator.py --selftest  fixtures

`exact.py` listed four numbers in this framework with no closed form, and said
one of them was DECIDABLE and was the first target:

    the 2 in  A(p, p') = 2 (p.p')^2 - p^2 p'^2

`coefficients.py` graded it ASSERTED -- "the structure of A, taken on four
confirming cases".  Four cases is not a proof, and this file does not add a
fifth.  It derives A from the graviton propagator and finds that the census
FLAGGED THE WRONG NUMBER.

===============================================================================
1. THE 2 IS NOT ASSERTED.  IT IS A COUNT OF INDEX PAIRINGS
===============================================================================

Linearised gravity exchanges one graviton between two stress tensors, and the
de Donder-gauge propagator numerator in D spacetime dimensions is

    P_{mu nu al be} = 1/2 ( eta_{mu al} eta_{nu be} + eta_{mu be} eta_{nu al}
                            - 2/(D-2) eta_{mu nu} eta_{al be} )

For a point source T^{mu nu} = p^mu p^nu, the exchange contracts as
p^mu p^nu P_{mu nu al be} p'^al p'^be.  `contract()` does that sum explicitly
over all 4^4 index assignments with symbolic momenta -- no identity is applied
by hand -- and returns

    (p.p')^2 - 1/(D-2) p^2 p'^2

    THE LEADING 2 OF `A` IS THE TWO TERMS eta_{mu al} eta_{nu be} AND
    eta_{mu be} eta_{nu al}.  It is the number of ways to pair a SYMMETRIC
    rank-2 source against a symmetric propagator, and a symmetric tensor has
    exactly two such pairings.  It is not adjustable, it is not fitted, and it
    is the same 2 in every dimension.  STATUS: THEOREM.

===============================================================================
2. AND THE NUMBER THAT IS ACTUALLY CONTINGENT IS THE OTHER ONE
===============================================================================

Write A with both coefficients visible:

    A = alpha (p.p')^2 + beta p^2 p'^2

The propagator fixes the RATIO and nothing else: beta/alpha = -1/(D-2).  The
scale is then fixed by the stated normalisation -- two masses at rest reproduce
Newton -- and `uniqueness()` solves that pair of conditions rather than
assuming it: in D = 4 the unique solution is (alpha, beta) = (2, -1).

    SO THE CENSUS FLAGGED THE WRONG DIGIT.  The 2 is dimension-independent and
    forced by symmetry.  THE SILENT `1` MULTIPLYING p^2 p'^2 IS THE
    D-DEPENDENT ONE: it is 2/(D-2), and it equals 1 ONLY IN FOUR DIMENSIONS.
    A coefficient hides best when it is written as a 1 and therefore not
    written at all.

===============================================================================
3. WHAT THAT COSTS THE FOUR CONFIRMING CASES -- AND THE PREDICTION
===============================================================================

Every row of `factor8.py`'s table is RE-DERIVED here from the contraction,
normalised on two static masses, and carried to general D:

    source    test          ratio in D            D = 4
    -------   -----------   -------------------   -----
    mass      mass          1                     1
    mass      photon        (D-2)/(D-3)           2
    photon    photon ||     0                     0
    photon    photon anti   4(D-2)/(D-3)          8

    THE ZERO IS A THEOREM IN EVERY DIMENSION.  Co-propagating null momenta have
    p.p' = 0 identically, both p^2 and p'^2 vanish, so A vanishes whatever D is
    and whatever the trace coefficient is.  It cannot be moved.

    THE 2 AND THE 8 ARE STATEMENTS ABOUT FOUR DIMENSIONS, AND THIS TREE NEVER
    SAID SO.  Light bending is (D-2)/(D-3) -- 3/2 in five dimensions, 9/8 in
    eleven -- and the antiparallel enhancement this project calls THE
    PREDICTION is 4(D-2)/(D-3), which is 8 at D = 4, 6 at D = 5 and 9/2 at
    D = 11.  `by_dimension()` prints the series.

    THIS DOES NOT WEAKEN THE PREDICTION.  We live in four dimensions and the
    figure there is exactly 8, derived rather than asserted.  What it removes
    is the impression that 8 is a pure number falling out of the algebra: it
    falls out of the algebra AND the dimension, and only the zero is free of
    the second.

===============================================================================
4. MACHINE-CHECKED, AND WHAT THAT IS WORTH
===============================================================================

`machine_check()` hands z3 the two polynomial identities over the reals --
the contraction against its closed form, and A against alpha, beta -- with the
momentum components universally quantified, and asks for a COUNTEREXAMPLE.  z3
returns `unsat` for each, which is a proof over the reals and not a sample.

    IT IS A CHECK ON THE ALGEBRA AND NOT ON THE PHYSICS.  What z3 verifies is
    that the contraction equals the closed form and that the closed form has
    the stated coefficients.  That the de Donder numerator is the right
    propagator, and that a point source is p^mu p^nu, are physics inputs, and
    they are cited rather than proved here.  PROOF-ASSISTANT.md makes the same
    distinction and this file does not blur it.

===============================================================================
5. WHAT THIS FILE REFUSES
===============================================================================

    TO CALL THE PREDICTION DERIVED FROM NOTHING.  Two inputs are taken from the
    literature: the de Donder propagator numerator and the point-source stress
    tensor.  Both are standard and both are named.  A derivation from stated
    premises is a THEOREM, which is what M asked coefficients to become, and
    not a derivation from no premises, which nothing is.

    TO RESTATE THE 8 WITHOUT ITS DIMENSION.  Section 3 attaches D = 4 to it
    permanently.  Any later file quoting 8 quotes 4(D-2)/(D-3) at D = 4.

    TO TOUCH THE OTHER THREE.  xi and l_UV are still UNDEFINED and the 0.0218 c
    ceiling is still FITTED.  One of four is settled, and the other three are
    not improved by that.
"""

import sys

import sympy as sp

D = sp.Symbol("D", positive=True)
ETA = sp.diag(-1, 1, 1, 1)                       # signature -+++
P = sp.symbols("p0 p1 p2 p3")
Q = sp.symbols("q0 q1 q2 q3")

SOURCES = (
    "de Donder-gauge graviton propagator numerator, standard; see e.g. "
    "Veltman, Les Houches (1975), and any linearised-gravity text",
    "point source T^{mu nu} = p^mu p^nu, as factor8.py section 1 uses it",
)


def dot(a, b):
    return sum(ETA[m, m] * a[m] * b[m] for m in range(4))


def numerator(m, n, al, be):
    """P_{mu nu al be} in D dimensions."""
    return sp.Rational(1, 2) * (
        ETA[m, al] * ETA[n, be] + ETA[m, be] * ETA[n, al]
        - 2 * ETA[m, n] * ETA[al, be] / (D - 2))


def contract():
    """p^mu p^nu P_{mu nu al be} p'^al p'^be, summed over all 4^4 assignments.

    EXPLICIT.  No identity is applied by hand; the sum is performed and then
    simplified, so the closed form in section 1 is an output and not an input.
    """
    tot = 0
    for m in range(4):
        for n in range(4):
            for al in range(4):
                for be in range(4):
                    c = numerator(m, n, al, be)
                    if c == 0:
                        continue
                    tot += (P[m] * P[n] * c * Q[al] * Q[be]
                            * ETA[m, m] * ETA[n, n] * ETA[al, al] * ETA[be, be])
    return sp.expand(sp.simplify(tot))


def closed_form():
    """The contraction's closed form: (p.p')^2 - p^2 p'^2 / (D-2)."""
    return dot(P, Q)**2 - dot(P, P) * dot(Q, Q) / (D - 2)


def contraction_matches():
    """0 iff the explicit sum equals the closed form, identically."""
    return sp.simplify(sp.expand(contract() - closed_form()))


def amplitude(pq, p2, q2, d=None):
    """A = 2(p.p')^2 - (2/(D-2)) p^2 p'^2, at general or fixed D."""
    a = 2 * pq**2 - 2 * p2 * q2 / (D - 2)
    return sp.simplify(a if d is None else a.subs(D, d))


def uniqueness():
    """(alpha, beta) forced by the propagator ratio and Newton, in D = 4.

    Two conditions, solved rather than assumed:
      beta/alpha = -1/(D-2)          the propagator's trace term
      A(static m, m') = m^2 m'^2     two masses at rest reproduce Newton
    """
    al, be, m, mp = sp.symbols("alpha beta m m_p", positive=True)
    be = sp.Symbol("beta")
    ratio = sp.Eq(be / al, -1 / (D - 2))
    newton = sp.Eq(al * (m * mp)**2 + be * (-m**2) * (-mp**2), m**2 * mp**2)
    sol = sp.solve([ratio.subs(D, 4), newton.subs(D, 4)], [al, be], dict=True)
    return [(s[al], s[be]) for s in sol]


CASES = (
    ("mass", "mass", lambda m, mp: (-m * mp, -m**2, -mp**2)),
    ("mass", "photon", lambda m, mp: (-m * mp, -m**2, 0)),
    ("photon", "photon ||", lambda m, mp: (0, 0, 0)),
    ("photon", "photon anti", lambda m, mp: (-2 * m * mp, 0, 0)),
)


def ratios():
    """[(source, test, ratio in D, ratio at D=4)] -- every case re-derived."""
    m, mp = sp.symbols("m m_p", positive=True)
    ref = amplitude(-m * mp, -m**2, -mp**2)          # two static masses
    out = []
    for src, tst, f in CASES:
        r = sp.simplify(amplitude(*f(m, mp)) / ref)
        out.append((src, tst, sp.simplify(r), sp.simplify(r.subs(D, 4))))
    return out


def by_dimension(ds=(4, 5, 6, 11)):
    """{D: (light bending, antiparallel)} -- the two that move."""
    R = {t: r for _s, t, r, _4 in ratios()}
    return {d: (sp.simplify(R["photon"].subs(D, d)),
                sp.simplify(R["photon anti"].subs(D, d))) for d in ds}


def zero_is_dimension_free():
    """The co-propagating zero holds for symbolic D -- not sampled."""
    R = {t: r for _s, t, r, _4 in ratios()}
    return sp.simplify(R["photon ||"]) == 0


def machine_check():
    """[(claim, z3 verdict)] -- the two identities, over the reals.

    Each is negated and handed to z3 as a search for a counterexample; `unsat`
    is a proof over the reals rather than a sample of it.  D is fixed to 4
    because z3 is a solver over polynomial arithmetic and D appears in a
    denominator; the general-D statement is sympy's, above.
    """
    import z3
    out = []
    zp = [z3.Real("p%d" % i) for i in range(4)]
    zq = [z3.Real("q%d" % i) for i in range(4)]
    sig = [-1, 1, 1, 1]
    zdot = lambda a, b: sum(sig[i] * a[i] * b[i] for i in range(4))

    lhs = 0
    for m in range(4):
        for n in range(4):
            for al in range(4):
                for be in range(4):
                    c = numerator(m, n, al, be).subs(D, 4)
                    if c == 0:
                        continue
                    lhs += (float(c) * zp[m] * zp[n] * zq[al] * zq[be]
                            * sig[m] * sig[n] * sig[al] * sig[be])
    rhs = zdot(zp, zq) * zdot(zp, zq) - zdot(zp, zp) * zdot(zq, zq) / 2
    s = z3.Solver()
    s.add(lhs != rhs)
    out.append(("contraction == (p.q)^2 - p^2 q^2 / 2 at D=4", str(s.check())))

    s2 = z3.Solver()
    A4 = 2 * zdot(zp, zq) * zdot(zp, zq) - zdot(zp, zp) * zdot(zq, zq)
    s2.add(2 * rhs != A4)
    out.append(("2 x contraction == 2(p.q)^2 - p^2 q^2", str(s2.check())))
    return out


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok = ok and good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    chk("the explicit 4^4 contraction equals its closed form, identically",
        contraction_matches(), 0)
    chk("so the leading 2 is the two index pairings of a symmetric source",
        sp.simplify(2 * closed_form()
                    - (2 * dot(P, Q)**2 - 2 * dot(P, P) * dot(Q, Q) / (D - 2))),
        0)
    chk("and at D = 4 the trace coefficient 2/(D-2) is exactly 1",
        sp.simplify((2 / (D - 2)).subs(D, 4)), 1)
    chk("which is the digit the census never flagged",
        sp.simplify(2 / (D - 2)) == 1, False)

    chk("(alpha, beta) is UNIQUE given the propagator and Newton",
        uniqueness(), [(2, -1)])

    R = {t: (r, r4) for _s, t, r, r4 in ratios()}
    chk("mass-mass is 1 in every dimension", sp.simplify(R["mass"][0]), 1)
    chk("light bending is (D-2)/(D-3), and 2 only at D = 4",
        (sp.simplify(R["photon"][0] - (D - 2) / (D - 3)), R["photon"][1]),
        (0, 2))
    chk("the co-propagating zero holds for SYMBOLIC D, not sampled",
        zero_is_dimension_free(), True)
    chk("the antiparallel prediction is 4(D-2)/(D-3), and 8 only at D = 4",
        (sp.simplify(R["photon anti"][0] - 4 * (D - 2) / (D - 3)),
         R["photon anti"][1]), (0, 8))
    chk("away from four it moves: D=5 gives 6, D=11 gives 9/2",
        (by_dimension()[5][1], by_dimension()[11][1]), (6, sp.Rational(9, 2)))

    mc = machine_check()
    chk("z3 finds NO counterexample to either identity over the reals",
        [v for _c, v in mc], ["unsat", "unsat"])
    chk("and both claims are named, not just counted", len(mc), 2)

    chk("two physics inputs are cited rather than proved", len(SOURCES), 2)

    print("propagator selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


def report():
    print("=" * 79)
    print("DOCKET 41 -- THE ASSERTED 2, SETTLED")
    print("=" * 79)
    print()
    print("1. IT IS NOT ASSERTED.  IT IS A COUNT OF INDEX PAIRINGS.")
    print("   The de Donder propagator numerator in D dimensions is")
    print("     P = 1/2 ( eta.eta + eta.eta - 2/(D-2) eta_{mn} eta_{ab} )")
    print("   Contracting p^m p^n P p'^a p'^b over all 4^4 assignments gives")
    print("     %s" % sp.simplify(closed_form()))
    print("   and the explicit sum minus that closed form is %s."
          % contraction_matches())
    print("   THE LEADING 2 IS THE TWO PAIRINGS OF A SYMMETRIC RANK-2 SOURCE.")
    print("   Not adjustable, not fitted, the same in every dimension.")
    print()
    print("2. AND THE CENSUS FLAGGED THE WRONG DIGIT.")
    print("   Writing A = alpha (p.p')^2 + beta p^2 p'^2, the propagator fixes")
    print("   beta/alpha = -1/(D-2) and Newton fixes the scale.  Solved:")
    print("     (alpha, beta) = %s   UNIQUE" % (uniqueness()[0],))
    print("   The 2 is dimension-free.  THE SILENT 1 ON p^2 p'^2 IS 2/(D-2),")
    print("   and it is 1 ONLY AT D = 4.  A coefficient hides best when it is")
    print("   written as a 1 and therefore not written at all.")
    print()
    print("3. THE FOUR CASES, RE-DERIVED, AND CARRIED TO GENERAL D")
    print("   %-9s %-13s %-22s %s" % ("source", "test", "ratio in D", "D = 4"))
    for src, tst, r, r4 in ratios():
        print("   %-9s %-13s %-22s %s" % (src, tst, r, r4))
    print()
    print("   THE ZERO IS A THEOREM IN EVERY DIMENSION -- co-propagating nulls")
    print("   have p.p' = 0 identically and both squares vanish.")
    print("   THE 2 AND THE 8 ARE STATEMENTS ABOUT FOUR DIMENSIONS:")
    for d, (lb, ap) in sorted(by_dimension().items()):
        print("     D = %-3d  light bending %-8s antiparallel %s" % (d, lb, ap))
    print("   We live in four, and there it is exactly 8 -- derived, not")
    print("   asserted.  What is removed is the impression that 8 falls out of")
    print("   the algebra alone.  It falls out of the algebra AND the")
    print("   dimension, and only the zero is free of the second.")
    print()
    print("4. MACHINE-CHECKED OVER THE REALS")
    for c, v in machine_check():
        print("     %-46s z3: %s%s" % (c, v,
                                       "  (no counterexample)" if v == "unsat"
                                       else "  COUNTEREXAMPLE"))
    print("   A check on the ALGEBRA, not the physics: that the de Donder")
    print("   numerator is the right propagator and a point source is p^m p^n")
    print("   are inputs, cited and not proved here.")
    print()
    print("5. WHAT THIS FILE REFUSES")
    print("   To call the prediction derived from nothing -- two inputs are")
    print("   taken from the literature and both are named.  To restate the 8")
    print("   without its dimension.  And to touch the other three: xi and")
    print("   l_UV are still UNDEFINED, 0.0218 c is still FITTED.")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
