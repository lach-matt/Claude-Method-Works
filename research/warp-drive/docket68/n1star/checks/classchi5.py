#!/usr/bin/env python3
"""classchi5: the null second fundamental form of an invariant null hypersurface in the T^2 x Z2 x Z2 class, and the
class Raychaudhuri equation (FAMILIES5-NONROUND.md section 2).

Off the axes the class metric is g = h_ab(y) dy^a dy^b + G1(y) dphi1^2 + G2(y) dphi2^2, y = (y0, y1, y2) coordinates of
the three-dimensional orbit spacetime, G_i = |K_i|^2 = e^(2 psi_i), K_i = d_(phi_i) the Killing fields (the paper's
Proposition 2.1 form; torusstress5's g3 + e^(2A) dphi1^2 + e^(2B) dphi2^2). A family's phase u is invariant (a function
of y), P := g^-1 du, and kappa_i := g^-1(du, d psi_i) = P(psi_i).

  C1 (exact, symbolic: h, its inverse, G1, G2, u arbitrary functions of y) the Hessian of an invariant u has no mixed
     components, hess(u)(d_a, d_phi_i) = 0 and hess(u)(d_phi1, d_phi2) = 0, and its torus components are
     hess(u)(d_phi_i, d_phi_i) = G_i kappa_i: first order in g and u (the Killing identity hess(u)(K, K) = (1/2)
     g^-1(du, d|K|^2)). So in an orthonormal frame (e_th, e_phi1, e_phi2) of a section the second fundamental form chi
     = hess(u) restricted is diag(th_h, kappa1, kappa2), and only th_h := box u - kappa1 - kappa2 carries second
     derivatives of u.
     Controls (must fail): a metric with g_(phi1 phi2) != 0 (T^2-invariant, not Z2 x Z2) has hess(u)(d_phi1, d_phi2) !=
     0; a Kaluza-Klein term g_(t phi1) != 0 has hess(u)(d_t, d_phi1) != 0; a phase u + w(y) cos(phi1) has a torus
     component depending on phi1 (it carries d_phi1^2 u).
  C2 (exact at rational jets, three seeds) where g^-1(du, du) vanishes to first order at the point (so hess(u)(P, .) =
     0 there), |hess u|_g^2 = (box u - kappa1 - kappa2)^2 + kappa1^2 + kappa2^2 exactly: the shear of the family's null
     hypersurfaces is algebraic in its expansion th = box u and the first-order kappa_i.
     Controls (must fail): the same jets without the null condition; the metric with g_(phi1 phi2) = 1/3; the phase u +
     (1/5) phi1^2 (not invariant).
  C3 (exact at jets) Bochner's identity P(box u) + |hess u|^2 + Ric(P, P) = (1/2) box (g^-1(du, du)) at a non-null
     jet (a check of the code), hence, where g^-1(du, du) vanishes to second order (u an eikonal), the class
     Raychaudhuri equation
         P(th) = -(th - kappa1 - kappa2)^2 - kappa1^2 - kappa2^2 - Ric(P, P),     th := box u.             (R)
     With Ric = sum_B q_B du_B du_B (the dusts) its right side contains no derivative of th, no derivative of du beyond
     the first through kappa_i, and no derivative of g beyond the first: this is the closing structure.
     Controls (must fail): the shear-free right side -th^2/3 - Ric(P, P); and the null condition imposed only to first
     order (then (1/2) box g^-1(du, du) != 0 at the point, and (R) fails while C2 still holds).
  C4 (exact at jets, null to first order) the torus principal curvatures obey their own Riccati equations
     P(kappa_i) = -kappa_i^2 - Rm(P, e_i, P, e_i), e_i = K_i/|K_i|, Rm(X, Y, X, Y) := R_abcd X^a Y^b X^c Y^d (R^a_bcd
     = d_c Gam^a_db - ...): their source is a curvature component (second derivatives of psi_i). So kappa_i is first
     order by the Killing identity (C1), an algebraic fact, not by its transport; where |K_i| -> 0 (the axes) that
     algebraic fact degenerates (axisloss5).
     Control (must fail): the opposite sign of the curvature term.

Labels: computed (exact, sympy for C1; exact Fractions at polynomial jets truncated at total degree 3 for C2-C4, every
quantity used at the point exact; checks/jetpoly5.py). Run: python3 checks/classchi5.py   (under a minute)
"""
from fractions import Fraction
import os
import random
import sys

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from jetpoly5 import Jet, geometry, monomials, NV  # noqa: E402

N5 = 5                       # coordinates y0, y1, y2, phi1, phi2


def c1():
    print("C1 (exact, symbolic): the Hessian of an invariant phase in the class")
    yv = sp.symbols('t r s')
    f1, f2 = sp.symbols('phi1 phi2')
    X = list(yv) + [f1, f2]
    G1 = sp.Function('G1')(*yv)
    G2 = sp.Function('G2')(*yv)
    u = sp.Function('u')(*yv)
    hf = [[sp.Function('h%d%d' % (min(i, j), max(i, j)))(*yv) for j in range(3)] for i in range(3)]
    hi = [[sp.Function('k%d%d' % (min(i, j), max(i, j)))(*yv) for j in range(3)] for i in range(3)]
    g = sp.zeros(5, 5)
    gi = sp.zeros(5, 5)
    for i in range(3):
        for j in range(3):
            g[i, j] = hf[i][j]
            gi[i, j] = hi[i][j]                 # the inverse of h: any functions (block form of g^-1 is all used)
    g[3, 3], g[4, 4] = G1, G2
    gi[3, 3], gi[4, 4] = 1 / G1, 1 / G2

    def hes(g, gi, uu, a, b):
        return sp.expand(sp.diff(uu, X[a], X[b]) - sum(
            sum(gi[c, d] * (sp.diff(g[d, b], X[a]) + sp.diff(g[d, a], X[b]) - sp.diff(g[a, b], X[d]))
                for d in range(5)) / 2 * sp.diff(uu, X[c]) for c in range(5)))
    mixed = [hes(g, gi, u, a, i) for a in range(3) for i in (3, 4)] + [hes(g, gi, u, 3, 4)]
    ok_mixed = all(sp.simplify(m) == 0 for m in mixed)
    ok_tor = True
    for i, Gi in ((3, G1), (4, G2)):
        kap = sum(gi[a, b] * sp.diff(u, X[a]) * sp.diff(sp.log(Gi) / 2, X[b]) for a in range(3) for b in range(3))
        ok_tor &= sp.simplify(hes(g, gi, u, i, i) - Gi * kap) == 0
    print("   mixed components zero:", ok_mixed, "; torus components = G_i kappa_i (first order):", ok_tor)
    # controls, on explicit metrics (inverses computed)
    Nf, A, B = [sp.Function(n)(*yv) for n in ('N', 'A', 'B')]
    c12 = sp.Function('c12')(*yv)
    gc = sp.diag(-Nf**2, A, B, G1, G2)
    gc[3, 4] = gc[4, 3] = c12
    bad1 = sp.simplify(hes(gc, gc.inv(), u, 3, 4)) != 0
    beta = sp.Function('beta')(*yv)
    gk = sp.diag(-Nf**2, A, B, G1, G2)
    gk[0, 3] = gk[3, 0] = beta
    bad2 = sp.simplify(hes(gk, gk.inv(), u, 0, 3)) != 0
    w = sp.Function('w')(*yv)
    gd = sp.diag(-Nf**2, A, B, G1, G2)
    hph = sp.simplify(hes(gd, gd.inv(), u + w * sp.cos(f1), 3, 3))
    bad3 = sp.simplify(sp.diff(hph, f1)) != 0
    print("   controls: g_(phi1 phi2) != 0 gives a mixed torus component:", bad1, "; g_(t phi1) != 0 gives a mixed "
          "component:", bad2, "; a phi1-dependent phase has a phi1-dependent torus component:", bad3)
    return ok_mixed and ok_tor and bad1 and bad2 and bad3


def rnd(rng, lo=-3, hi=3, den=7):
    return Fraction(rng.randint(lo * den, hi * den), den)


def build(seed, null_order=2, phi12=None, phi_dep=None):
    """Random class metric jet (h quadratic in y, G_i quadratic, optional g_(phi1 phi2)) and a phase u (cubic in y)
    with g^-1(du, du) vanishing to order null_order at 0. Returns lists of Jets."""
    rng = random.Random(seed)
    y = [Jet.var(i) for i in range(NV)]

    def quad(c0):
        e = Jet.const(c0)
        for k in range(3):
            e = e + y[k] * (rnd(rng) / 5)
        for k in range(3):
            for l in range(k, 3):
                e = e + y[k] * y[l] * (rnd(rng) / 9)
        return e
    c = [Fraction(1), rnd(rng, 1, 3), rnd(rng, -2, 2)]          # du at 0 (orbit components), c0 != 0
    Hi = sp.zeros(3, 3)
    base = [-1, 1, 1]
    for i in range(3):
        for j in range(i, 3):
            v = (base[i] if i == j else 0) + sp.Rational(rng.randint(-11, 11), 44)
            Hi[i, j] = Hi[j, i] = v
    cc = [sp.Rational(x.numerator, x.denominator) for x in c]
    rest = 2 * cc[0] * (Hi[0, 1] * cc[1] + Hi[0, 2] * cc[2]) + Hi[1, 1] * cc[1]**2 + 2 * Hi[1, 2] * cc[1] * cc[2] \
        + Hi[2, 2] * cc[2]**2
    Hi[0, 0] = -rest / cc[0]**2                                   # make c null for the inverse orbit metric at 0
    assert Hi.det() < 0 and Hi[1:, 1:].det() > 0 and Hi[0, 0] < 0
    h0 = Hi.inv()
    fr = lambda q: Fraction(int(sp.fraction(q)[0]), int(sp.fraction(q)[1]))
    g = [[Jet() for _ in range(N5)] for _ in range(N5)]
    for i in range(3):
        for j in range(i, 3):
            g[i][j] = quad(fr(h0[i, j]))
            g[j][i] = g[i][j]
    g[3][3] = quad(Fraction(3, 2) + rnd(rng, 0, 1, 5) / 3)
    g[4][4] = quad(Fraction(5, 4) + rnd(rng, 0, 1, 5) / 3)
    if phi12 is not None:
        g[3][4] = g[4][3] = Jet.const(phi12) * (Jet.const(1) + y[0] * Fraction(1, 3) + y[1] * y[2] * Fraction(1, 5))
    # the phase: Taylor coefficients; those with a y0 factor at degrees 2 and 3 are fixed by the null condition
    coef = {}
    for k in range(3):
        coef[monomials(3, 1)[k]] = c[k]
    free2 = [m for m in monomials(3, 2) if m[0] == 0]
    free3 = [m for m in monomials(3, 3) if m[0] == 0]
    unk2 = [m for m in monomials(3, 2) if m[0] > 0]
    unk3 = [m for m in monomials(3, 3) if m[0] > 0]
    for m in free2 + free3:
        coef[m] = rnd(rng) / 2
    extra = Jet() if phi_dep is None else y[3] * y[3] * (Fraction(phi_dep) / 2)

    def phase(cf):
        return Jet(dict(cf)) + extra

    def Nnull(cf):
        u = phase(cf)
        gi = geometry_inv(g)
        du = [u.d(a) for a in range(N5)]
        return sum((gi[a][b] * du[a] * du[b] for a in range(N5) for b in range(N5)), Jet())

    def solve_order(unk, order, cf):
        mons = monomials(3, order - 1)          # N vanishes to order (order - 1): its coefficients there
        base_cf = dict(cf)
        for m in unk:
            base_cf[m] = Fraction(0)
        b0 = Nnull(base_cf)
        rows = []
        for m in unk:
            cf1 = dict(base_cf)
            cf1[m] = Fraction(1)
            n1 = Nnull(cf1)
            rows.append([n1.c.get(mm, 0) - b0.c.get(mm, 0) for mm in mons])
        Amat = sp.Matrix(len(mons), len(unk), lambda i, j: sp.Rational(rows[j][i].numerator, rows[j][i].denominator))
        bvec = sp.Matrix(len(mons), 1, lambda i, j: -sp.Rational(b0.c.get(mons[i], Fraction(0)).numerator,
                                                                   b0.c.get(mons[i], Fraction(0)).denominator))
        sol = Amat.LUsolve(bvec)
        assert Amat * sol == bvec
        out = dict(base_cf)
        for j, m in enumerate(unk):
            out[m] = fr(sol[j])
        return out
    if null_order >= 1:
        coef = solve_order(unk2, 2, coef)
    else:
        for m in unk2:
            coef[m] = rnd(rng) / 2
    if null_order >= 2:
        coef = solve_order(unk3, 3, coef)
    else:
        for m in unk3:
            coef[m] = rnd(rng) / 2
    u = phase(coef)
    assert Nnull(coef).at0() == 0
    return g, u


_inv_cache = {}


def geometry_inv(g):
    key = id(g)
    if key not in _inv_cache:
        from jetpoly5 import matinv
        _inv_cache[key] = (g, matinv(g))
    return _inv_cache[key][1]


def quantities(g, u):
    G = geometry(g, u)
    gi0 = G['gi0']
    H0 = [[G['H'][a][b].at0() for b in range(N5)] for a in range(N5)]
    du0 = [x.at0() for x in G['du']]
    P0 = [sum(gi0[a][b] * du0[b] for b in range(N5)) for a in range(N5)]
    th = G['box'].at0()
    hess2 = sum(gi0[a][c] * gi0[b][d] * H0[a][b] * H0[c][d] for a in range(N5) for b in range(N5)
                for c in range(N5) for d in range(N5))
    kap = []
    for i in (3, 4):
        Gi = g[i][i]
        dpsi = [Gi.d(v).at0() / (2 * Gi.at0()) for v in range(N5)]
        kap.append(sum(gi0[a][b] * du0[a] * dpsi[b] for a in range(N5) for b in range(N5)))
    Pbox = sum(P0[a] * G['box'].d(a).at0() for a in range(N5))
    RicPP = sum(G['Ric0'][a][b] * P0[a] * P0[b] for a in range(N5) for b in range(N5))
    return G, dict(P0=P0, th=th, hess2=hess2, kap=kap, Pbox=Pbox, RicPP=RicPP)


def class_rhs(q):
    k1, k2 = q['kap']
    return (q['th'] - k1 - k2)**2 + k1**2 + k2**2


def torus_riccati(g, G, q):
    """P(kappa_i) + kappa_i^2 + s Rm(P, e_i, P, e_i) at 0 for s = +1 (claim) and s = -1 (control)."""
    out = []
    gi = G['gi']
    du = G['du']
    P0 = q['P0']
    for idx, i in enumerate((3, 4)):
        Gi = g[i][i]
        dpsi = [Gi.d(v) * Gi.inv() * Fraction(1, 2) for v in range(N5)]
        kap = sum((gi[a][b] * du[a] * dpsi[b] for a in range(N5) for b in range(N5)), Jet())
        Pk = sum(P0[a] * kap.d(a).at0() for a in range(N5))
        RmK = Fraction(0)                         # Rm(P, K_i, P, K_i), K_i = d_(phi_i); then divide by G_i
        for a in range(N5):
            if P0[a] == 0:
                continue
            for cc in range(N5):
                if P0[cc] == 0:
                    continue
                Rlow = sum(G['g0'][a][f] * G['riem_up'](f, i, cc, i) for f in range(N5))
                RmK += Rlow * P0[a] * P0[cc]
        Rm = RmK / Gi.at0()
        out.append((Pk + q['kap'][idx]**2 + Rm, Pk + q['kap'][idx]**2 - Rm))
    return out


def c2_c4():
    ok = True
    print("C2-C4 (exact at rational jets): the class identity, the class Raychaudhuri equation, the torus Riccati")
    for seed in (11, 23, 37):
        g, u = build(seed, null_order=2)
        G, q = quantities(g, u)
        c2 = q['hess2'] == class_rhs(q)
        boch = q['Pbox'] + q['hess2'] + q['RicPP'] == 0
        ray = q['Pbox'] + class_rhs(q) + q['RicPP'] == 0
        shearfree = q['Pbox'] + q['th']**2 / 3 + q['RicPP'] != 0
        tr = torus_riccati(g, G, q)
        c4 = all(x[0] == 0 for x in tr)
        c4ctl = all(x[1] != 0 for x in tr)
        print("   seed %d: C2 %s; Bochner %s; (R) %s; shear-free form rejected %s; torus Riccati %s (wrong sign "
              "rejected %s)" % (seed, c2, boch, ray, shearfree, c4, c4ctl))
        print("      th = %s, kappa1 = %s, kappa2 = %s, |hess u|^2 = %s, Ric(P,P) = %s"
              % (q['th'], q['kap'][0], q['kap'][1], q['hess2'], q['RicPP']))
        ok &= c2 and boch and ray and shearfree and c4 and c4ctl
    # Bochner's identity at a jet that is NOT null (a check of the code)
    g, u = build(5, null_order=0)
    G, q = quantities(g, u)
    gi = G['gi']
    du = G['du']
    Nj = sum((gi[a][b] * du[a] * du[b] for a in range(N5) for b in range(N5)), Jet())
    Gam = G['Gam']
    boxN = sum((gi[a][b] * (Nj.d(a).d(b) - sum((Gam[c][a][b] * Nj.d(c) for c in range(N5)), Jet()))).at0()
               for a in range(N5) for b in range(N5))
    gen = q['Pbox'] + q['hess2'] + q['RicPP'] - boxN / 2 == 0
    nonzero = boxN != 0
    print("   Bochner at a non-null jet: P(box u) + |hess u|^2 + Ric(P,P) = (1/2) box N:", gen,
          "(box N = %s, nonzero: %s)" % (boxN, nonzero))
    return ok and gen and nonzero


def controls():
    print("Controls (each must reject)")
    g, u = build(11, null_order=0)
    _, q = quantities(g, u)
    r1 = q['hess2'] != class_rhs(q)
    print("   no null condition: C2 fails:", r1, "(difference %s)" % (q['hess2'] - class_rhs(q)))
    g, u = build(11, null_order=2, phi12=Fraction(1, 3))
    _, q = quantities(g, u)
    r2 = q['hess2'] != class_rhs(q)
    print("   g_(phi1 phi2) = 1/3: C2 fails:", r2, "(difference %s)" % (q['hess2'] - class_rhs(q)))
    g, u = build(11, null_order=2, phi_dep=Fraction(2, 5))
    _, q = quantities(g, u)
    r3 = q['hess2'] != class_rhs(q)
    print("   phase u + (1/5) phi1^2: C2 fails:", r3, "(difference %s)" % (q['hess2'] - class_rhs(q)))
    g, u = build(23, null_order=1)
    _, q = quantities(g, u)
    r4 = q['Pbox'] + class_rhs(q) + q['RicPP'] != 0
    r4b = q['hess2'] == class_rhs(q)
    print("   null only to first order: (R) fails:", r4, "; C2 still holds:", r4b)
    return r1 and r2 and r3 and r4 and r4b


if __name__ == '__main__':
    res = [c1(), c2_c4(), controls()]
    print("PASS" if all(res) else "FAIL")
    sys.exit(0 if all(res) else 1)
