#!/usr/bin/env python3
r"""
DOCKET 67 -- re-derivation for key covering-space-lift-flat-quotient.

The tree's use (latticectc.py:25-26, 251-280): in R^{1,d} / L, L a rank-n
translation lattice, "a closed causal curve exists in the quotient IFF L
contains a nonzero causal vector", via (i) covering-space lifting: a closed
curve in the quotient lifts to a curve from p to p + V, V in L; (ii) the
reduction lemma: a causal curve from p to p + V exists iff V is future-causal
and nonzero (or past-causal, reversing direction).

Checks, each independent of the tree's own code except where marked:
  L1  path lifting on a flat quotient, numerically: random closed loops in the
      quotient (fundamental-domain coordinates, wrap-around) lift by
      continuity to curves whose endpoint difference is EXACTLY an element of L.
  L2  z3: the closed future cone is closed under addition, stated directly
      (not via the tree's scalar lemma), spatial dims 1, 2, 3.
  L3  z3: a nonzero future-causal vector has t > 0 (so V = 0 is impossible:
      the lift of a contractible loop cannot be a closed causal curve).
  L4  sympy: the Lagrange identity (Cauchy-Schwarz) for spatial dims 1..8
      (the tree checks d = 3 and states "any dimension").
  L5  z3, own encoding: for random exact-rational rank-2 lattices in R^{1,3},
      "a K = 2 closed causal chain exists with winding |n_i| <= 2" agrees with
      "a lattice vector with |n_i| <= 2 is causal", lattice by lattice.
  L6  sympy: rank-2 Gram criterion -- min of A t^2 + 2 H t + C is (AC - H^2)/A.
  L7  rank 3 (the tree's heading says n >= 2, its Gram proof is rank 2):
      random rank-3 lattices with spacelike generators; timelike span ->
      a timelike lattice vector found; spacelike span -> none.
  L8  THE BOUNDARY, exact: g1 = (1,1,sqrt2), g2 = (0,0,1): no causal lattice
      vector, and for every eps tested the cone-widened metric
      -(1+eps) dt^2 + dx^2 + dy^2 has a TIMELIKE lattice vector: not stably
      causal (Hawking-Ellis / Hubeny-Rangamani-Ross definition).
  L9  scope of the tree's DEGENERATE_SPAN label (latticectc.py:123), using the
      tree's own span_kind and chain_to read-only: two degenerate-span
      rational lattices for which "causal but not stably causal" is false.
"""
import itertools
import math
import os
import random
import sys
from fractions import Fraction as Fr

import sympy as sp
import z3

sys.dont_write_bytecode = True
OK = True


def chk(label, got, want):
    global OK
    good = got == want
    OK &= good
    print("  [%s] %s: got %r want %r" % ("ok" if good else "FAIL", label, got, want))


def nrm(v):
    return -v[0] * v[0] + sum(c * c for c in v[1:])


# ---------------------------------------------------------------- L1
def lift_loop(gens, steps, rng):
    """gens: n generators in R^{1,d} (floats), assumed R-independent.  Build a
    loop in the quotient in lattice coordinates u in [0,1)^n (+ transverse
    coords held fixed), random small steps, reduced mod 1 each step, closing
    at the start point in the quotient.  Lift by continuity (nearest
    representative).  Return the integer winding of the lift."""
    n = len(gens)
    u0 = [rng.random() for _ in range(n)]
    # a loop in the quotient: a straight-line path to u0 + w (w integer), with
    # noise, reduced mod 1 -- the reduction is what the quotient sees
    w = [rng.randint(-3, 3) for _ in range(n)]
    pts = []
    for k in range(steps + 1):
        s = k / steps
        noise = 0.0 if k in (0, steps) else 0.02
        q = [u0[i] + s * w[i] + noise * (rng.random() - 0.5) for i in range(n)]
        pts.append([x % 1.0 for x in q])        # quotient coordinates only
    # continuity lift: each step choose the representative nearest the last
    lift = [list(pts[0])]
    for q in pts[1:]:
        prev = lift[-1]
        lift.append([q[i] + round(prev[i] - q[i]) for i in range(n)])
    diff = [lift[-1][i] - lift[0][i] for i in range(n)]
    return w, diff


# ---------------------------------------------------------------- L2, L3
def cone_closed_under_addition(dim):
    s = z3.Solver()
    t1, t2 = z3.Reals("t1 t2")
    x = [z3.Real("x%d" % i) for i in range(dim)]
    y = [z3.Real("y%d" % i) for i in range(dim)]
    s.add(t1 >= 0, t2 >= 0)
    s.add(t1 * t1 >= z3.Sum([c * c for c in x]))
    s.add(t2 * t2 >= z3.Sum([c * c for c in y]))
    s.add((t1 + t2) * (t1 + t2) < z3.Sum([(a + b) * (a + b) for a, b in zip(x, y)]))
    s.set("timeout", 60000)
    return str(s.check())


def nonzero_causal_has_positive_t(dim):
    s = z3.Solver()
    t = z3.Real("t")
    x = [z3.Real("x%d" % i) for i in range(dim)]
    s.add(t >= 0, t * t >= z3.Sum([c * c for c in x]))
    s.add(z3.Or(t != 0, *[c != 0 for c in x]))
    s.add(t <= 0)
    return str(s.check())


# ---------------------------------------------------------------- L5
def chain_exists(V, K):
    """own encoding: K future-causal legs summing to V (or to -V, reversed
    orientation), total dt > 0."""
    out = False
    for sign in (1, -1):
        s = z3.Solver()
        s.set("timeout", 20000)
        legs = [[z3.Real("l%d_%d" % (i, k)) for k in range(len(V))] for i in range(K)]
        for L in legs:
            s.add(L[0] >= 0, L[0] * L[0] >= z3.Sum([c * c for c in L[1:]]))
        for k in range(len(V)):
            s.add(z3.Sum([L[k] for L in legs]) == z3.RealVal(str(sign * V[k])))
        s.add(z3.Sum([L[0] for L in legs]) > 0)
        r = s.check()
        if r == z3.unknown:
            return "unknown"
        out |= (r == z3.sat)
    return out


def rand_vec(rnd, dim=4):
    return tuple(Fr(rnd.randint(-9, 9), rnd.randint(1, 5)) for _ in range(dim))


def main():
    print("L1  path lifting on a flat quotient (numeric)")
    rng = random.Random(1)
    agree = 0
    T = 400
    for _ in range(T):
        n = rng.choice([1, 2, 3])
        w, diff = lift_loop([None] * n, 200, rng)
        agree += all(abs(d - wi) < 1e-9 and abs(d - round(d)) < 1e-9 for d, wi in zip(diff, w))
    chk("lift endpoint difference is the integer winding w (an element of L), %d loops" % T,
        agree, T)

    print("L2  z3: closed future cone is closed under addition (direct statement)")
    for d in (1, 2):
        chk("spatial dim %d, direct" % d, cone_closed_under_addition(d), "unsat")
    # spatial dim 3 direct: z3 nlsat returns 'unknown' at 60 s and at 240 s
    # (probed); that is a solver limit, not a counterexample.  The dimension-
    # free route: a = |x|, b = |y|, d = x.y with d^2 <= a^2 b^2 (Cauchy-Schwarz,
    # L4's Lagrange identity) -- NOT the tree's premise d <= ab, which z3 must
    # here derive from d^2 <= a^2 b^2 and a, b >= 0.
    s = z3.Solver()
    t1, t2, a, b, dd = z3.Reals("t1 t2 a b dd")
    s.add(a >= 0, b >= 0, t1 >= a, t2 >= b, dd * dd <= a * a * b * b)
    s.add((t1 + t2) * (t1 + t2) < a * a + b * b + 2 * dd)
    chk("any spatial dim, via Cauchy-Schwarz d^2 <= a^2 b^2", str(s.check()), "unsat")

    print("L3  z3: nonzero future-causal vector has t > 0")
    for d in (1, 2, 3, 4):
        chk("spatial dim %d" % d, nonzero_causal_has_positive_t(d), "unsat")

    print("L4  sympy: Lagrange identity, spatial dims 1..8")
    for d in range(1, 9):
        x = sp.symbols("x0:%d" % d, real=True)
        y = sp.symbols("y0:%d" % d, real=True)
        lag = sum((x[i] * y[j] - x[j] * y[i]) ** 2 for i in range(d) for j in range(i + 1, d))
        r = sp.expand(sum(c * c for c in x) * sum(c * c for c in y)
                      - sum(a * b for a, b in zip(x, y)) ** 2 - lag)
        chk("d = %d residual" % d, r, 0)

    print("L5  z3 (own encoding): chain existence == causal lattice vector, rank 2, R^{1,3}")
    rnd = random.Random(11)
    mism, unk, cases, pos = 0, 0, 0, 0
    for _ in range(30):
        g1, g2 = rand_vec(rnd), rand_vec(rnd)
        for m, n in itertools.product(range(-2, 3), repeat=2):
            if (m, n) == (0, 0):
                continue
            V = tuple(m * a + n * b for a, b in zip(g1, g2))
            want = nrm(V) <= 0          # nonzero V; causal (either time orientation)
            got = chain_exists(V, 2)
            cases += 1
            pos += want
            if got == "unknown":
                unk += 1
            elif got != want:
                mism += 1
    chk("mismatches over %d (lattice, winding) cases (%d causal)" % (cases, pos), mism, 0)
    chk("z3 unknowns", unk, 0)

    print("L6  sympy: rank-2 Gram criterion")
    A, C, H, t = sp.symbols("A C H t", real=True)
    q = A * t ** 2 + 2 * H * t + C
    tmin = sp.solve(sp.diff(q, t), t)[0]
    chk("min_t (A t^2 + 2Ht + C) - (AC - H^2)/A", sp.simplify(q.subs(t, tmin) - (A * C - H ** 2) / A), 0)

    print("L7  rank 3: timelike span <-> timelike lattice vector (search), R^{1,3}")
    rnd = random.Random(3)
    tl_found, tl_n, sl_hit, sl_n = 0, 0, 0, 0
    while tl_n < 60 or sl_n < 60:
        gs = [rand_vec(rnd) for _ in range(3)]
        if not all(nrm(g) > 0 for g in gs):
            continue
        G = sp.Matrix(3, 3, lambda i, j: -gs[i][0] * gs[j][0]
                      + sum(gs[i][k] * gs[j][k] for k in range(1, 4)))
        if G.det() == 0:
            continue
        import numpy as np
        ev = list(np.linalg.eigvalsh(np.array(G.tolist(), dtype=float)))
        neg = sum(1 for e in ev if e < 0)
        found = False
        for R in (8, 16, 32):      # escalate: a thin timelike cone needs a larger box
            found = any(nrm(tuple(a * gs[0][k] + b * gs[1][k] + c * gs[2][k] for k in range(4))) < 0
                        for a, b, c in itertools.product(range(-R, R + 1), repeat=3)
                        if (a, b, c) != (0, 0, 0))
            if found or neg == 0:
                break
        if neg >= 1 and tl_n < 60:
            tl_n += 1
            tl_found += found
        elif neg == 0 and sl_n < 60:
            sl_n += 1
            sl_hit += any(nrm(tuple(a * gs[0][k] + b * gs[1][k] + c * gs[2][k] for k in range(4))) <= 0
                          for a, b, c in itertools.product(range(-8, 9), repeat=3) if (a, b, c) != (0, 0, 0))
    chk("timelike-span rank-3 lattices with a timelike vector in box |n|<=8, escalating to 32 (of %d)" % tl_n,
        tl_found, tl_n)
    chk("spacelike-span rank-3 lattices with ANY causal vector in box (of %d)" % sl_n, sl_hit, 0)

    print("L8  THE BOUNDARY, exact: g1 = (1,1,sqrt2), g2 = (0,0,1) in R^{1,2}")
    s2 = sp.sqrt(2)
    # norm of m g1 + n g2 is (m sqrt2 + n)^2, zero only at m = n = 0 (sqrt2 irrational)
    m_, n_ = sp.symbols("m n", integer=True)
    v = (m_, m_, m_ * s2 + n_)
    chk("norm(m g1 + n g2) - (m sqrt2 + n)^2", sp.expand(-v[0] ** 2 + v[1] ** 2 + v[2] ** 2
                                                        - (m_ * s2 + n_) ** 2), 0)
    chk("span contains the null vector (1,1,0) = g1 - sqrt2 g2", -1 + 1 + 0, 0)
    ctc_all = True
    for eps in (sp.Rational(1, 10), sp.Rational(1, 100), sp.Rational(1, 10 ** 4), sp.Rational(1, 10 ** 6)):
        m = int(sp.ceiling(1 / (2 * sp.sqrt(eps)))) + 1
        n = -int(sp.floor(m * s2 + sp.Rational(1, 2)))
        widened = -(1 + eps) * m ** 2 + m ** 2 + (m * s2 + n) ** 2   # exact
        neg = bool(sp.simplify(widened) < 0)
        print("     eps = %s: lattice vector (m,n) = (%d,%d), widened norm = %s (< 0: %s)"
              % (eps, m, n, sp.N(widened, 8), neg))
        ctc_all &= neg
    chk("every widened metric tested has a timelike lattice vector (CTC): not stably causal",
        ctc_all, True)

    print("L9  scope of DEGENERATE_SPAN (tree read-only: span_kind, chain_to)")
    here = "/home/user/Claude-Method-Works/research/warp-drive"
    sys.path.insert(0, here)
    import latticectc as T
    g1, g2 = (Fr(1), Fr(1), Fr(0), Fr(0)), (Fr(0), Fr(0), Fr(1), Fr(0))
    chk("tree span_kind of g1=(1,1,0,0), g2=(0,0,1,0)", T.span_kind(g1, g2), "degenerate")
    chk("tree chain_to: closing vector g1 (null), K = 1 -> closed causal chain",
        str(T.chain_to(z3, [-c for c in g1], 1)) + "|" + str(T.chain_to(z3, list(g1), 1)), "unsat|sat")
    print("     -> quotient has a closed NULL curve: NOT causal, against DEGENERATE_SPAN =",
          repr(T.DEGENERATE_SPAN))
    p1, p2 = (Fr(0), Fr(1), Fr(0), Fr(0)), (Fr(0), Fr(2), Fr(0), Fr(0))
    chk("tree span_kind of parallel spacelike generators (0,1,0,0), (0,2,0,0)", T.span_kind(p1, p2),
        "degenerate")
    print("     -> the Z-span is the rank-1 lattice Z(0,1,0,0); t is an invariant time function:"
          " STABLY causal, against the same label")
    chk("t is invariant under the lattice (t-components zero)", (p1[0], p2[0]), (0, 0))

    print("\nREDERIVATION %s" % ("OK" if OK else "FAILED"))
    return 0 if OK else 1


if __name__ == "__main__":
    sys.exit(main())
