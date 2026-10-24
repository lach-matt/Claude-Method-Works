#!/usr/bin/env python3
"""general5.py -- settling without the class: [Hin26]'s bookkeeping over every type with his two orders of loss, and
the Poincare charges of the translated, rotated and boosted Myers-Perry family at Tangherlini (N1STAR-PROOF.md sections
10.61-10.63; ROUTES 4.61-4.63; D130-D132).  Labels: computed (exact, sympy).

Without the T^2-mirror class the boosts and translations return (10.43): the zero energy pole is second order and
forward solutions lose two orders at K+ ([Hin26] p. 25), so his Theorem 11.59 records every term below K+ order 4 +
eps_K, as in four dimensions, where the class needed 3 + eps_K (sharp5.py K3).  And the solutions of Theorem 1 with a
perturbation that breaks the class are glued at large radius not to Tangherlini but to a member of the translated,
rotated and boosted Myers-Perry family, matched by its Poincare charges ([CD03] section 8.1; its Remark 8.2: "the only
element missing is an equivalent of Proposition F.1 for the family of translated, rotated, and boosted Myers-Perry
metrics").

  G1 (computed, exact) The bookkeeping, every type of window5.py's five-dimensional lists (its W1 computes their roots
     in [-3, 0] at lin5.py's point), at every iota+ exponent on a grid of [alpha_min, 4] (251 points, the orders linear
     in alpha), with sharp5.py's rule and K+ threshold 4: eliminated, the six pure gauge classes s0 c0, s0 e0, s1 c0,
     s1 e-1, s2 e0, v1 e-1; recorded, fourteen classes, each of a kind his (12.14)-(12.15) parameterizes; physical, s2,
     v2 and t2 at -2, with no companion, and only while alpha <= 2; every recorded term's L_b-image above 4.  Control:
     four dimensions at alpha = 1 gives his eight eliminated parameters and his physical s2, v2, s3, v3 with 1, 1, 0, 0
     companions (sharp5.py K3's).  Mutant: the class's threshold 3, where no physical state is recorded.
  G2 (computed, exact) The charges.  On the linearizations at Tangherlini of the static spatial metric in the mass, of
     the shift mu (W x)_i / r^4 in the rotation W in so(4) (mp5.py M3's leading term), of the translation and of the
     boost, the ADM energy, momentum, angular momentum and centre-of-mass fluxes (G = 1) are, exactly: E = 3 pi mu/8,
     dE/dmu = 3 pi/8; J(W) = (pi mu/4) W, 2/3 of E per unit spin, on all six generators; P = -E v; E C = E c; every
     other entry 0.  The 15 x 15 Jacobian is diagonal with determinant (3 pi/8) (pi mu/4)^6 (3 pi mu/8)^8, nonzero for
     mu > 0.  Control: four dimensions, E = m, J = m a, P = -m v, E C = m c ([CD03] (F.4)-(F.6)).  Mutant: mu = 0.

sympy; imports sharp5.py, window5.py, iplus5.py.  python3 general5.py [--selftest | --mutants]   (under a minute)
"""
import sys
import time

import sympy as sp

from damping5 import Checklist
import sharp5 as S5
import window5 as W

# ------------------------------------------------------------------------------------------------- G1
ELIM5 = {("s0", "c0"), ("s0", "e0"), ("s1", "c0"), ("s1", "e-1"), ("s2", "e0"), ("v1", "e-1")}
REC5 = ELIM5 | {("s1", "c-1"), ("s2", "c-1"), ("s2", "c-2"), ("s3", "c-2"), ("s3", "e-1"), ("s4", "e-2"),
                ("v2", "e-1"), ("v3", "e-2")}
PHYS5 = {("s2", "e-2"), ("v2", "e-2"), ("t2", "e-2")}
ELIM4 = {("s0", "c0"), ("s0", "e0"), ("s1", "c0"), ("s1", "e-1"), ("s2", "e0"), ("s3", "e-1"), ("v1", "e-1"),
         ("v2", "e-1")}
PHYS4 = {("s2", "e-2"): 1, ("v2", "e-2"): 1, ("s3", "e-3"): 0, ("v3", "e-3"): 0}


def kind_of(s, t):
    if t[0] == "c":
        return "class"
    if (s, t) in (("s1", "e-1"), ("v1", "e-1")):
        return s
    return "gauge"


def g1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    import iplus5
    thr = 3 if control == 1 else 4
    a0 = S5.alpha_min().subs(iplus5.POINT)
    grid = [a0 + (4 - a0) * sp.Rational(m, 250) for m in range(251)]
    el_all, rec_all, ph_all, ok_ph, lb = set(), set(), set(), True, True
    for al in grid:
        el, rec, ph = S5.book(W.SPEC5, al, thr=thr)
        el_all |= el
        rec_all |= set(rec)
        ph_all |= set(ph)
        ok_ph &= (set(ph) == PHYS5 and all(k == 0 for k in ph.values())) if al <= 2 else not ph
        lb &= all(W.order(al, t, kind_of(s, t)).subs(S5.EPS, 0) + k + 1 > thr for (s, t), k in rec.items())
    chk(f"eliminated over [alpha_min, 4]: {sorted(el_all)}", el_all == ELIM5)
    chk(f"recorded (pure gauge and class roots): {len(rec_all)} classes", rec_all == REC5)
    chk(f"physical: {sorted(ph_all)}, no companion, exactly while alpha <= 2", ph_all == PHYS5 and ok_ph)
    chk("every recorded term's L_b-image of K+ order above 4", lb)
    el, rec, ph = S5.book(W.SPEC4, sp.Integer(1), thr=4)
    chk(f"control, four dimensions at alpha = 1: eliminated {len(el)}, physical {sorted(ph.items())}",
        el == ELIM4 and ph == PHYS4)
    return chk.ok


# ------------------------------------------------------------------------------------------------- G2
def sphere_int(poly, xs):
    """the integral of a polynomial over the unit sphere S^(n-1) in R^n"""
    n = len(xs)
    tot = sp.Integer(0)
    for mon, co in sp.Poly(sp.expand(poly), *xs).terms():
        if any(m % 2 for m in mon):
            continue
        tot += co * 2 * sp.prod([sp.gamma(sp.Rational(m + 1, 2)) for m in mon]) / sp.gamma(sp.Rational(sum(mon) + n, 2))
    return sp.simplify(tot)


def charges(n, data):
    """ADM E, P_i, J_ab, E C_k of linearized data (h_ij, beta_i = g_ti, d_t h_ij) as R -> oo, each flux split into
    homogeneous parts: the part of degree -(n - 1) gives the limit, higher parts must integrate to 0, lower vanish"""
    xs = sp.symbols(f"x1:{n + 1}", real=True)
    r, s = sp.symbols("r s", positive=True)
    h, beta, dth = data(xs, r)

    def d(f, i):
        return sp.diff(f, xs[i]) + sp.diff(f, r) * xs[i] / r

    nv = [x / r for x in xs]

    def flux(G):
        Gs = sp.expand(sp.expand(G).subs({**{x: s * x for x in xs}, r: s * r}, simultaneous=True) * s**40)
        tot = 0
        for (k,), co in sp.Poly(Gs, s).terms():
            dg = k - 40 + n - 1
            if dg < 0:
                continue
            val = sphere_int(sp.expand(co.subs(r, 1)), xs)
            if dg > 0:
                assert val == 0, ("divergent flux", dg, val)
            else:
                tot += val
        return sp.simplify(tot)

    tr = lambda M: sum(M[i][i] for i in range(n))
    div = [sum(d(h[i][j], j) for j in range(n)) - d(tr(h), i) for i in range(n)]
    E = flux(sum(div[i] * nv[i] for i in range(n))) / (16 * sp.pi)
    K = [[-(dth[i][j] - d(beta[j], i) - d(beta[i], j)) / 2 for j in range(n)] for i in range(n)]
    pi_ = [[K[i][j] - (tr(K) if i == j else 0) for j in range(n)] for i in range(n)]
    P = [flux(sum(pi_[i][j] * nv[j] for j in range(n))) / (8 * sp.pi) for i in range(n)]
    J = [flux(sum((xs[a] * pi_[b][j] - xs[b] * pi_[a][j]) * nv[j] for j in range(n))) / (8 * sp.pi)
         for a in range(n) for b in range(a + 1, n)]
    C = [flux(sum(xs[k] * div[i] * nv[i] for i in range(n)) - (sum(h[i][k] * nv[i] for i in range(n))
                                                                - tr(h) * nv[k])) / (16 * sp.pi) for k in range(n)]
    return [E] + P + J + C


def family(n, mu):
    """the 1 + n + n(n-1)/2 + n linearized directions at Tangherlini (static spatial metric), mass mu"""
    zero = lambda: [[0] * n for _ in range(n)]
    base = lambda xs, r: [[mu * xs[i] * xs[j] / r**n for j in range(n)] for i in range(n)]

    def dd(f, xs, r, k):
        return sp.diff(f, xs[k]) + sp.diff(f, r) * xs[k] / r

    dirs = [lambda xs, r: ([[xs[i] * xs[j] / r**n for j in range(n)] for i in range(n)], [0] * n, zero())]
    for k in range(n):
        dirs.append(lambda xs, r, k=k: (zero(), [mu * int(i == k) / r**(n - 2) + mu * xs[i] * xs[k] / r**n
                                                 for i in range(n)],
                                        [[dd(g, xs, r, k) for g in row] for row in base(xs, r)]))
    for a in range(n):
        for b in range(a + 1, n):
            def rot(xs, r, a=a, b=b):
                wx = [0] * n
                wx[a], wx[b] = xs[b], -xs[a]
                return zero(), [mu * wx[i] / r**n for i in range(n)], zero()
            dirs.append(rot)
    for k in range(n):
        dirs.append(lambda xs, r, k=k: ([[-dd(g, xs, r, k) for g in row] for row in base(xs, r)], [0] * n, zero()))
    return dirs


def jacobian(n, mu):
    return sp.Matrix([charges(n, f) for f in family(n, mu)]).T


def g2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    mu = sp.Integer(0) if control == 1 else sp.Symbol("mu", positive=True)
    m = sp.Symbol("m", positive=True)
    E0 = charges(4, lambda xs, r: ([[mu * xs[i] * xs[j] / r**4 for j in range(4)] for i in range(4)], [0] * 4,
                                   [[0] * 4 for _ in range(4)]))
    chk(f"Tangherlini's charges: E = {E0[0]}, all others {set(E0[1:])}", E0[0] == 3 * sp.pi * mu / 8 and
        set(E0[1:]) == {0})
    Jm = jacobian(4, mu)
    want = sp.diag(*([3 * sp.pi / 8] + [-3 * sp.pi * mu / 8] * 4 + [sp.pi * mu / 4] * 6 + [3 * sp.pi * mu / 8] * 4))
    det = sp.factor(Jm.det())
    chk(f"the 15 x 15 Jacobian (E, P, J, E C) by (mu, boost, rotation, translation): diagonal, det = {det}",
        sp.simplify(Jm - want) == sp.zeros(15) and det != 0)
    J3 = jacobian(3, 2 * m)
    chk("control, four dimensions with mu = 2m: E = mu/2 = m, P = -m v, J = m a, E C = m c ([CD03] (F.4)-(F.6))",
        sp.simplify(J3 - sp.diag(sp.Rational(1, 2), *([-m] * 3 + [m] * 3 + [m] * 3))) == sp.zeros(10))
    return chk.ok


CHECKS = [("G1 the bookkeeping without the class: threshold 4, every type; physical s2, v2, t2 at -2 only", g1),
          ("G2 the charges of the translated, rotated, boosted Myers-Perry family at Tangherlini: invertible", g2)]


def run(only=None, verbose=False):
    ok = True
    for k, (name, f) in enumerate(CHECKS, 1):
        if only and k != only:
            continue
        t0 = time.time()
        res = f(0, verbose)
        ok &= res
        print(f"{name[:104]:<104} {'PASS' if res else 'FAIL'} {time.time() - t0:3.0f}s", flush=True)
    n = 1 if only else len(CHECKS)
    print(f"general5.py: {n if ok else 'not all'}/{n}")
    return ok


def mutants():
    caught = total = 0
    for name, f in CHECKS:
        total += 1
        res = f(1, False)
        caught += not res
        print(f"mutant 1 of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"general5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    vb = "--verbose" in args
    if "--selftest" in args:
        sys.exit(0 if run(verbose=vb) else 1)
    elif "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    elif "--only" in args:
        sys.exit(0 if run(int(args[args.index("--only") + 1]), vb) else 1)
    print(__doc__)
