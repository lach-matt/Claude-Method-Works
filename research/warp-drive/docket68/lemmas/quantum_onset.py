#!/usr/bin/env python3
"""quantum_onset.py -- item 415: where 273's quantum region begins, derived rather than asked.

M, 415: "how am I supposed to know this? It's a conjecture. If it is the likely solution, then let's prove that it is."
The record placed the region's boundary where the curvature reaches the bulk's Planck scale (interior_large.py I2,
from 273's reading (b): Haggard and Rovelli's order-of-magnitude rule carried to 5D, an estimate).  Here that placement
is derived.  Labels: computed (exact unless marked), deduced, READ, estimate.

The premises, each named so that it can be refused:
  P1  the bulk's constants are G5, hbar and c, with Lambda5 = -6/ell^2 classical; no other scale;
  P2  the classical part is Einstein's law, exact at two derivatives (324-328: Lovelock, the Gauss-Bonnet coupling zero),
      so everything beyond it carries hbar and vanishes as hbar -> 0;
  P3  decoupling: where the curvature is far above 1/ell^2, the corrections do not grow with ell (local physics does
      not depend on the far-off AdS scale);
  P4  M's 405, no coefficients: no pure number is chosen.

  Q1 (computed, exact) Buckingham's theorem on {G5, hbar, c, ell, R}: in (mass, length, time) the dimension matrix has
     rank 3, so exactly two independent dimensionless numbers exist: x2 = l5^2 R, with l5^3 = G5 hbar / c^3, and
     y2 = ell^2 R.  (l5/ell is their quotient.)
  Q2 (deduced from Q1 and P2-P3) x2 carries hbar (as hbar^(2/3)); y2 does not, and enters only through the classical
     Lambda term.  So the size of every correction against the Einstein term is a function F of x = l5^2 sqrt(K)
     alone (K the Kretschmann scalar, the curvature's scale; at x ~ 1 its Lambda part 40/ell^4 is negligible), with
     F(0) = 0 and each term a positive power of x.  Classical GR holds exactly where x << 1 and fails where x reaches
     order one: whatever the power, a positive power of x is small if and only if x is.  With no coefficient (P4) the
     boundary is x = 1.  What P4 adds is the 1: nature's own order-one factor (the unknown coefficients of the
     higher-curvature terms) is not derived here, and the board does not choose one.
  Q3 (computed; reproduces I2) On the 4D stretch's form, K = 12 r0^2 / r^6, so x = 1 at r_q = (12 r0^2 l5^4)^(1/6), and
     r_q / R_5 = (l5/ell)^(2/3) = 4.95e-14 with ell at its ceiling and l5 = (l_P^2 ell)^(1/3).
  Q4 (computed; Haggard and Rovelli's time READ through b_bounce Q3, their eq. (2)) Their second, long-time criterion
     cannot act inside.  Their time is of order m^2/l_P; between our face and any radius the interior's clock spans less
     than pi r0/2 (I1), and the ratio of the two is 2 pi l_P / r0 -- below 1e-29 for any hole with r0 >= ell.  Inside the
     hole only x decides.
  Q5 (deduced) (c1): before the boundary x < 1, so sqrt(K) < 1/l5^2 and curvature is finite there, given (b) (the
     classical development does not end earlier at a Cauchy horizon).
  Q6 (computed; a counterfactual that shows what P3 does) If a term l5 ell R were admitted -- growing with ell, against
     P3 -- it would reach one at x = (l5/ell)^(1/2), far before x = 1.  P3 is what excludes it.

What this does not prove: P1-P3 are premises of effective field theory, not theorems; nature's order-one factor is
not derived (P4 sets it to one by M's rule); which curvature invariant measures the scale moves the boundary by order
one (Kretschmann taken).  python3 quantum_onset.py [--selftest | --mutants]
"""
import os, sys, importlib.util
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
MUT = set()


def _load(name, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, name))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def buckingham():
    """Q1: the dimension matrix of G5, hbar, c, ell, R in (M, L, T) and its null space"""
    dims = {"G5": (-1, 4, -2), "hbar": (1, 2, -1), "c": (0, 1, -1), "ell": (0, 1, 0), "R": (0, -2, 0)}
    names = list(dims)
    A = sp.Matrix([[dims[n][k] for n in names] for k in range(3)])
    ns = A.nullspace()
    return names, A, ns


def groups():
    """the two named groups as exponent vectors over (G5, hbar, c, ell, R)"""
    x2 = sp.Matrix([sp.Rational(2, 3), sp.Rational(2, 3), -2, 0, 1])     # l5^2 R = (G5 hbar / c^3)^(2/3) R
    y2 = sp.Matrix([0, 0, 0, 2, 1])                                       # ell^2 R
    if "hbar_in_y" in MUT:
        y2 = sp.Matrix([0, sp.Rational(1, 3), 0, 2, 1])
    return x2, y2


def onset_4d():
    """Q3: x = 1 on the 4D stretch's form, against R_5 (K = 1/ell^4) -- I2's numbers"""
    r, r0, ell, l5 = sp.symbols("r r_0 ell l_5", positive=True)
    K = 12 * r0 ** 2 / r ** 6
    thr = 10 if "threshold" in MUT else 1
    rq = sp.solve(sp.Eq(l5 ** 2 * sp.sqrt(K), thr), r)[0]
    R5 = sp.solve(sp.Eq(K, 1 / ell ** 4), r)[0]
    PG = _load("p2_gravity.py", "qo_pg")
    lP = (PG.HBAR * PG.G / PG.C ** 3) ** 0.5
    l5v = lP if "lP_for_l5" in MUT else (lP ** 2 * PG.ELL_MAX) ** (1 / 3)
    ratio = sp.simplify(rq / R5)
    return dict(rq=rq, R5=R5, ratio=ratio, value=float(ratio.subs({l5: l5v, ell: PG.ELL_MAX})), l5=l5v, lP=lP,
                ell=PG.ELL_MAX)


def long_time():
    """Q4: the interior's clock span (pi r0 / 2, I1) against Haggard and Rovelli's m^2/l_P, m = r0/2"""
    r0, lP = sp.symbols("r_0 l_P", positive=True)
    ratio = sp.simplify((sp.pi * r0 / 2) / ((r0 / 2) ** 2 / lP))
    o = onset_4d()
    return dict(ratio=ratio, at_ell=float(ratio.subs({r0: o["ell"], lP: o["lP"]})))


def counterfactual():
    """Q6: a term l5 ell R (against P3) reaches one at l5^2 R = l5/ell"""
    l5, ell, R = sp.symbols("l_5 ell R", positive=True)
    Rstar = sp.solve(sp.Eq(l5 * ell * R, 1), R)[0]
    return sp.simplify(sp.sqrt(l5 ** 2 * Rstar))


def report():
    names, A, ns = buckingham(); x2, y2 = groups(); o = onset_4d(); lt = long_time()
    print("Q1 dimension matrix rank %d over %s; %d dimensionless numbers" % (A.rank(), names, len(ns)))
    print("Q2 l5^2 R carries hbar^%s; ell^2 R carries hbar^%s" % (x2[1], y2[1]))
    print("Q3 r_q/R_5 = %s = %.3g (l5 = %.3g m, ell = %.4g m)" % (o["ratio"], o["value"], o["l5"], o["ell"]))
    print("Q4 interior clock / Haggard-Rovelli time = %s = %.2g at r0 = ell" % (lt["ratio"], lt["at_ell"]))
    print("Q6 with a term l5 ell R admitted, onset at x = %s" % counterfactual())


def selftest(quiet=False):
    ok = []
    def say(m):
        if not quiet:
            print(m, flush=True)
    names, A, ns = buckingham(); x2, y2 = groups()
    span = sp.Matrix.hstack(*ns)
    inspan = lambda v: sp.Matrix.hstack(span, v).rank() == span.rank()
    s1 = A.rank() == 3 and len(ns) == 2 and inspan(x2) and inspan(y2) and sp.Matrix.hstack(x2, y2).rank() == 2
    ok.append(s1); say("S1 rank 3, two dimensionless numbers, spanned by l5^2 R and ell^2 R: %s" % s1)
    s2 = x2[1] == sp.Rational(2, 3) and y2[1] == 0 and (A * x2).is_zero_matrix and (A * y2).is_zero_matrix
    ok.append(s2); say("S2 l5^2 R carries hbar^(2/3), ell^2 R none, both dimensionless: %s" % s2)
    o = onset_4d(); ell, l5 = sp.symbols("ell l_5", positive=True)
    s3 = sp.simplify(o["ratio"] - (l5 / ell) ** sp.Rational(2, 3)) == 0 and abs(o["value"] - 4.95e-14) < 0.01e-14
    ok.append(s3); say("S3 r_q/R_5 = (l5/ell)^(2/3) = %.3g, I2's 4.95e-14: %s" % (o["value"], s3))
    lt = long_time()
    s4 = lt["at_ell"] < 1e-29
    ok.append(s4); say("S4 the interior lasts %.2g of Haggard-Rovelli's time at r0 = ell, below 1e-29: %s" % (
        lt["at_ell"], s4))
    l5s, ells = sp.symbols("l_5 ell", positive=True)
    s5 = sp.simplify(counterfactual() - sp.sqrt(l5s / ells)) == 0
    ok.append(s5); say("S5 the counterfactual onset (against P3) is x = (l5/ell)^(1/2): %s" % s5)
    return all(ok)


def mutants():
    caught = 0; names = ["lP_for_l5", "hbar_in_y", "threshold"]
    for m in names:
        MUT.clear(); MUT.add(m)
        try:
            r = selftest(quiet=True)
        except Exception:
            r = False
        caught += not r; print("mutant %-10s %s" % (m, "caught" if not r else "SURVIVED"), flush=True)
    MUT.clear(); print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--selftest":
        sys.exit(0 if selftest() else 1)
    if a and a[0] == "--mutants":
        sys.exit(0 if mutants() else 1)
    report()
