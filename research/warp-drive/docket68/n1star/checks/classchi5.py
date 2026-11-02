#!/usr/bin/env python3
"""classchi5: the null second fundamental form of an invariant null hypersurface in the T^2 x Z2 x Z2 class, and the
class Raychaudhuri equation (FAMILIES5-NONROUND.md section 2).

Off the axes the class metric is g = h_ab(y) dy^a dy^b + G1(y) dphi1^2 + G2(y) dphi2^2, y = (y0, y1, y2) coordinates of
the three-dimensional orbit spacetime, G_i = |K_i|^2 = e^(2 psi_i), K_i = d_(phi_i) the Killing fields (the paper's
Proposition 2.1 form; torusstress5's g3 + e^(2A) dphi1^2 + e^(2B) dphi2^2). A family's phase u is invariant (a function
of y), P := g^-1 du, and kappa_i := g^-1(du, d psi_i) = P(psi_i).

  C1 (exact, symbolic, general h, G1, G2, u) the Hessian of an invariant u has no mixed components, hess(u)(d_a,
     d_phi_i) = 0 and hess(u)(d_phi1, d_phi2) = 0, and its torus components are hess(u)(d_phi_i, d_phi_i) = G_i kappa_i:
     first order in g and u (the Killing identity hess(u)(K, K) = (1/2) g^-1(du, d|K|^2)). So in an orthonormal frame
     (e_th, e_phi1, e_phi2) of a section the second fundamental form chi = hess(u) restricted is diag(th_h, kappa1,
     kappa2), and only th_h := box u - kappa1 - kappa2 carries second derivatives of u.
     Controls (must fail): a metric with g_(phi1 phi2) != 0 (T^2-invariant, not Z2 x Z2) has hess(u)(d_phi1, d_phi2) !=
     0; a Kaluza-Klein term g_(y0 phi1) != 0 has hess(u)(d_y0, d_phi1) != 0; a phase depending on phi1 has a torus
     component carrying d_phi1^2 u.
  C2 (exact at Gaussian-rational jets, three seeds) where g^-1(du, du) vanishes to first order at the point (so
     hess(u)(P, .) = 0 there), |hess u|_g^2 = (box u - kappa1 - kappa2)^2 + kappa1^2 + kappa2^2 exactly: the shear of the
     family's null hypersurfaces is algebraic in its expansion th = box u and the first-order kappa_i.
     Controls (must fail): the same jets without the null condition; the metric with g_(phi1 phi2) != 0; the phase u +
     (eps/2) phi1^2.
  C3 (exact at jets) Bochner's identity P(box u) + |hess u|^2 + Ric(P, P) = (1/2) box (g^-1(du, du)) at every jet (a
     check of the code), hence, where g^-1(du, du) vanishes to second order (u an eikonal), the class Raychaudhuri
     equation
         P(th) = -(th - kappa1 - kappa2)^2 - kappa1^2 - kappa2^2 - Ric(P, P),     th := box u.             (R)
     With Ric = sum_B q_B du_B du_B (the dusts) its right side contains no derivative of th, of du beyond the first,
     or of g beyond the first: this is the closing structure.
     Controls (must fail): the shear-free right side -th^2/3 - Ric(P, P); and the null condition imposed only to first
     order (then (1/2) box g^-1(du, du) != 0 at the point).
  C4 (exact at jets, null to first order) the torus principal curvatures obey their own Riccati equations
     P(kappa_i) = -kappa_i^2 - Rm(P, e_i, P, e_i), e_i = K_i/|K_i|, Rm(X, Y, X, Y) := R_abcd X^a Y^b X^c Y^d: their source
     is a curvature component (second derivatives of psi_i). So kappa_i is first order by the Killing identity (C1), an
     algebraic fact, not by its transport; where |K_i| -> 0 (the axes) that algebraic fact degenerates (axisloss5).
     Control (must fail): the opposite sign of the curvature term.

Labels: computed (exact, sympy; rational arithmetic at polynomial jets truncated at total degree 3, every quantity used
at the point exact). Run: python3 checks/classchi5.py   (about a minute)
"""
import random
import sys

import sympy as sp

Y = sp.symbols('y0 y1 y2 f1 f2')                     # orbit coordinates y0..y2, torus angles f1 = phi1, f2 = phi2
DEG = 3
ZERO = {v: 0 for v in Y}


def trunc(e):
    e = sp.expand(e)
    if e == 0:
        return sp.Integer(0)
    p = sp.Poly(e, *Y)
    out = sp.Integer(0)
    for mon, c in p.terms():
        if sum(mon) <= DEG:
            out += c * sp.prod([v**k for v, k in zip(Y, mon)])
    return out


def at0(e):
    return sp.nsimplify(sp.expand(e).subs(ZERO))


def mm(A, B):
    n = A.shape[0]
    return sp.Matrix(n, n, lambda i, j: trunc(sum(A[i, k] * B[k, j] for k in range(n))))


def inverse_series(g):
    """g^-1 as a truncated power series about the origin (Neumann series)."""
    g0 = g.subs(ZERO)
    i0 = g0.inv()
    E = sp.Matrix(g.shape[0], g.shape[1], lambda i, j: sp.expand(g[i, j] - g0[i, j]))
    term = i0
    tot = i0
    M = -mm(E, i0)
    for _ in range(DEG):
        term = mm(term, M)
        tot = tot + term
    return tot.applyfunc(trunc), i0


def rnd(rng, lo=-3, hi=3, den=7):
    return sp.Rational(rng.randint(lo * den, hi * den), den)


def geometry(g, u):
    """Christoffels, Hessian, box u (as truncated polynomials) and Ricci at 0."""
    n = 5
    gi, gi0 = inverse_series(g)
    dg = [[[sp.diff(g[a, b], Y[c]) for c in range(n)] for b in range(n)] for a in range(n)]
    Gam = [[[trunc(sum(gi[c, d] * (dg[d][b][a] + dg[d][a][b] - dg[a][b][d]) for d in range(n)) / 2)
             for b in range(n)] for a in range(n)] for c in range(n)]
    du = [sp.diff(u, Y[a]) for a in range(n)]
    H = sp.Matrix(n, n, lambda a, b: trunc(sp.diff(u, Y[a], Y[b]) - sum(Gam[c][a][b] * du[c] for c in range(n))))
    box = trunc(sum(gi[a, b] * H[a, b] for a in range(n) for b in range(n)))
    # Ricci at 0: R_bd = d_a Gam^a_bd - d_d Gam^a_ba + Gam^a_ae Gam^e_bd - Gam^a_de Gam^e_ba
    G0 = [[[at0(Gam[c][a][b]) for b in range(n)] for a in range(n)] for c in range(n)]
    dG0 = [[[[at0(sp.diff(Gam[c][a][b], Y[e])) for e in range(n)] for b in range(n)] for a in range(n)]
           for c in range(n)]
    Ric0 = sp.Matrix(n, n, lambda b, d: sum(dG0[a][b][d][a] - dG0[a][b][a][d] for a in range(n))
                     + sum(G0[a][a][e] * G0[e][b][d] - G0[a][d][e] * G0[e][b][a] for a in range(n) for e in range(n)))
    # Riemann at 0, R^a_bcd = d_c Gam^a_db - d_d Gam^a_cb + Gam^a_ce Gam^e_db - Gam^a_de Gam^e_cb
    def riem_up(a, b, c, d):
        return (dG0[a][d][b][c] - dG0[a][c][b][d]
                + sum(G0[a][c][e] * G0[e][d][b] - G0[a][d][e] * G0[e][c][b] for e in range(n)))
    g0m = g.subs(ZERO)
    return dict(gi=gi, gi0=gi0, Gam=Gam, du=du, H=H, box=box, Ric0=Ric0, riem_up=riem_up, g0m=g0m)


def make_metric(rng, phi12=0, kk=0):
    """Random class metric jet: h(y) quadratic, G_i(y) quadratic, optional g_(phi1 phi2) and g_(y0 phi1) terms.
    Returns g and a function setting h0 so that a given covector c is null."""
    ys = Y[:3]
    def quad(c0):
        e = c0
        for k in range(3):
            e += rnd(rng) * ys[k] / 5
        for k in range(3):
            for l in range(k, 3):
                e += rnd(rng) * ys[k] * ys[l] / 9
        return e
    return quad


def build(seed, null_order=2, phi12=0, kk=0, phi_dep=0):
    rng = random.Random(seed)
    ys = Y[:3]
    quad = make_metric(rng)
    c = [sp.Rational(1), rnd(rng, 1, 3), rnd(rng, -2, 2)]          # du at 0 in the orbit directions (c0 != 0)
    # inverse orbit metric at 0: near diag(-1, 1, 1), H00 adjusted so that c is null
    Hi = sp.Matrix(3, 3, lambda i, j: 0)
    base = [-1, 1, 1]
    for i in range(3):
        for j in range(i, 3):
            v = (base[i] if i == j else 0) + rnd(rng, -1, 1, 11) / 4
            Hi[i, j] = Hi[j, i] = v
    rest = 2 * c[0] * (Hi[0, 1] * c[1] + Hi[0, 2] * c[2]) + Hi[1, 1] * c[1]**2 + 2 * Hi[1, 2] * c[1] * c[2] \
        + Hi[2, 2] * c[2]**2
    Hi[0, 0] = -rest / c[0]**2
    assert Hi.det() < 0 and Hi[1:, 1:].det() > 0 and Hi[0, 0] < 0, "orbit metric not Lorentzian; change seed"
    h0 = Hi.inv()
    g = sp.zeros(5, 5)
    for i in range(3):
        for j in range(i, 3):
            g[i, j] = g[j, i] = quad(h0[i, j]) if True else 0
    # the quad() call adds random linear and quadratic parts to the value h0[i, j]
    g[3, 3] = quad(sp.Rational(3, 2) + rnd(rng, 0, 1, 5) / 3)
    g[4, 4] = quad(sp.Rational(5, 4) + rnd(rng, 0, 1, 5) / 3)
    if phi12:
        g[3, 4] = g[4, 3] = phi12 * (1 + ys[0] / 3 + ys[1] * ys[2] / 5)
    if kk:
        g[0, 3] = g[3, 0] = kk * (ys[1] + ys[2] / 2)
    # the phase: u = c.y + (1/2) U2 y y + (1/6) U3 y y y (+ phi-dependence for the control)
    U2 = {}
    syms2 = []
    for k in range(3):
        for l in range(k, 3):
            if k == 0:
                s = sp.Symbol('U2_%d%d' % (k, l)); syms2.append(s); U2[(k, l)] = s
            else:
                U2[(k, l)] = rnd(rng)
    U3 = {}
    syms3 = []
    for k in range(3):
        for l in range(k, 3):
            for m in range(l, 3):
                if k == 0:
                    s = sp.Symbol('U3_%d%d%d' % (k, l, m)); syms3.append(s); U3[(k, l, m)] = s
                else:
                    U3[(k, l, m)] = rnd(rng)
    def U2f(k, l):
        return U2[tuple(sorted((k, l)))]
    def U3f(k, l, m):
        return U3[tuple(sorted((k, l, m)))]
    u = sum(c[k] * ys[k] for k in range(3))
    u += sp.Rational(1, 2) * sum(U2f(k, l) * ys[k] * ys[l] for k in range(3) for l in range(3))
    u += sp.Rational(1, 6) * sum(U3f(k, l, m) * ys[k] * ys[l] * ys[m] for k in range(3) for l in range(3)
                                 for m in range(3))
    if phi_dep:
        u += phi_dep * Y[3]**2 / 2
    # impose the null condition order by order
    gi, _ = inverse_series(g)
    du = [sp.diff(u, v) for v in Y]
    N = trunc(sum(gi[a, b] * du[a] * du[b] for a in range(5) for b in range(5)))
    assert at0(N) == 0
    sub = {}
    if null_order >= 1:
        eqs = [at0(sp.diff(N, ys[k])) for k in range(3)]
        sol = sp.solve(eqs, syms2, dict=True)
        assert len(sol) == 1
        sub.update(sol[0])
    else:
        for s in syms2:
            sub[s] = rnd(rng)
    u = u.subs(sub)
    if null_order >= 2:
        du = [sp.diff(u, v) for v in Y]
        N = trunc(sum(gi[a, b] * du[a] * du[b] for a in range(5) for b in range(5)))
        eqs = [at0(sp.diff(N, ys[k], ys[l])) for k in range(3) for l in range(k, 3)]
        sol = sp.solve(eqs, syms3, dict=True)
        assert len(sol) == 1
        u = u.subs(sol[0])
    else:
        u = u.subs({s: rnd(rng) for s in syms3})
    return g, sp.expand(u)


def quantities(g, u):
    G = geometry(g, u)
    gi0 = G['gi0']
    H0 = G['H'].subs(ZERO)
    du0 = [at0(x) for x in G['du']]
    P0 = [sum(gi0[a, b] * du0[b] for b in range(5)) for a in range(5)]
    th = at0(G['box'])
    hess2 = sp.nsimplify(sum(gi0[a, c] * gi0[b, d] * H0[a, b] * H0[c, d] for a in range(5) for b in range(5)
                             for c in range(5) for d in range(5)))
    # kappa_i = g^-1(du, d psi_i), psi_i = (1/2) log g(K_i, K_i)
    kap = []
    for i in (3, 4):
        dpsi = [at0(sp.diff(g[i, i], v)) / (2 * at0(g[i, i])) for v in Y]
        kap.append(sp.nsimplify(sum(gi0[a, b] * du0[a] * dpsi[b] for a in range(5) for b in range(5))))
    Pbox = sp.nsimplify(sum(P0[a] * at0(sp.diff(G['box'], Y[a])) for a in range(5)))
    RicPP = sp.nsimplify(sum(G['Ric0'][a, b] * P0[a] * P0[b] for a in range(5) for b in range(5)))
    return G, dict(P0=P0, th=th, hess2=hess2, kap=kap, Pbox=Pbox, RicPP=RicPP, du0=du0, H0=H0)


def class_rhs(q):
    k1, k2 = q['kap']
    return (q['th'] - k1 - k2)**2 + k1**2 + k2**2


def c1():
    print("C1 (exact, symbolic): the Hessian of an invariant phase in the class")
    yv = sp.symbols('t r s')
    f1, f2 = sp.symbols('phi1 phi2')
    X = list(yv) + [f1, f2]
    hf = [[sp.Function('h%d%d' % (min(i, j), max(i, j)))(*yv) for j in range(3)] for i in range(3)]
    G1 = sp.Function('G1')(*yv)
    G2 = sp.Function('G2')(*yv)
    u = sp.Function('u')(*yv)
    def hessian(g, uu):
        gi = g.inv()
        n = 5
        Gam = [[[sum(gi[c, d] * (sp.diff(g[d, b], X[a]) + sp.diff(g[d, a], X[b]) - sp.diff(g[a, b], X[d]))
                     for d in range(n)) / 2 for b in range(n)] for a in range(n)] for c in range(n)]
        return lambda a, b: sp.simplify(sp.diff(uu, X[a], X[b]) - sum(Gam[c][a][b] * sp.diff(uu, X[c])
                                                                      for c in range(n))), gi
    g = sp.zeros(5, 5)
    for i in range(3):
        for j in range(3):
            g[i, j] = hf[i][j]
    g[3, 3] = G1
    g[4, 4] = G2
    hs, gi = hessian(g, u)
    mixed = [hs(a, 3) for a in range(3)] + [hs(a, 4) for a in range(3)] + [hs(3, 4)]
    ok_mixed = all(sp.simplify(m) == 0 for m in mixed)
    ok_tor = True
    for i, Gi in ((3, G1), (4, G2)):
        kap = sum(gi[a, b] * sp.diff(u, X[a]) * sp.diff(sp.log(Gi) / 2, X[b]) for a in range(3) for b in range(3))
        ok_tor &= sp.simplify(hs(i, i) - Gi * kap) == 0
    print("   mixed components zero:", ok_mixed, "; torus components = G_i kappa_i (first order):", ok_tor)
    # controls
    gc = g.copy()
    c12 = sp.Function('c12')(*yv)
    gc[3, 4] = gc[4, 3] = c12
    hsc, _ = hessian(gc, u)
    bad1 = sp.simplify(hsc(3, 4)) != 0
    gk = g.copy()
    bfun = sp.Function('beta')(*yv)
    gk[0, 3] = gk[3, 0] = bfun
    hsk, _ = hessian(gk, u)
    bad2 = sp.simplify(hsk(0, 3)) != 0
    uphi = u + sp.Function('w')(*yv) * sp.cos(f1)
    hsp, _ = hessian(g, uphi)
    bad3 = sp.diff(sp.simplify(hsp(3, 3)), f1) != 0 or sp.simplify(hsp(3, 3)).has(sp.cos(f1))
    print("   controls: g_(phi1 phi2) != 0 gives a mixed torus component:", bad1, "; g_(t phi1) != 0 gives a "
          "mixed component:", bad2, "; a phi1-dependent phase changes the torus component:", bad3)
    return ok_mixed and ok_tor and bad1 and bad2 and bad3


def c2_c3_c4():
    ok = True
    print("C2-C4 (exact at rational jets): the class identity, the class Raychaudhuri equation, the torus Riccati")
    for seed in (11, 23, 37):
        g, u = build(seed, null_order=2)
        G, q = quantities(g, u)
        lhs = q['hess2']
        rhs = class_rhs(q)
        c2 = sp.simplify(lhs - rhs) == 0
        # C3: Bochner at this jet (u null to second order): P(box u) + |hess u|^2 + Ric(P,P) = 0
        boch = sp.simplify(q['Pbox'] + q['hess2'] + q['RicPP']) == 0
        ray = sp.simplify(q['Pbox'] + class_rhs(q) + q['RicPP']) == 0
        shearfree = sp.simplify(q['Pbox'] + q['th']**2 / 3 + q['RicPP']) != 0
        # C4: P(kappa_i) = -kappa_i^2 - Rm(P, e_i, P, e_i)
        gi = G['gi']
        du = G['du']
        P0 = q['P0']
        c4 = True
        c4ctl = True
        g0m = G['g0m']
        for idx, i in enumerate((3, 4)):
            Gi = g[i, i]
            Gi0 = at0(Gi)
            invG = sum((-(Gi - Gi0) / Gi0)**k for k in range(DEG + 1)) / Gi0
            dpsi = [trunc(sp.diff(Gi, v) * invG / 2) for v in Y]
            kap = trunc(sum(gi[a, b] * du[a] * dpsi[b] for a in range(5) for b in range(5)))
            Pk = sp.nsimplify(sum(P0[a] * at0(sp.diff(kap, Y[a])) for a in range(5)))
            e = [0] * 5
            e[i] = 1 / sp.sqrt(Gi0)
            Rm = 0
            for a in range(5):
                for b in range(5):
                    for cc in range(5):
                        for d in range(5):
                            if P0[a] == 0 or e[b] == 0 or P0[cc] == 0 or e[d] == 0:
                                continue
                            Rlow = sum(g0m[a, f] * G['riem_up'](f, b, cc, d) for f in range(5))
                            Rm += Rlow * P0[a] * e[b] * P0[cc] * e[d]
            Rm = sp.nsimplify(sp.simplify(Rm))
            c4 &= sp.simplify(Pk + q['kap'][idx]**2 + Rm) == 0
            c4ctl &= sp.simplify(Pk + q['kap'][idx]**2 - Rm) != 0
        print("   seed %d: |hess u|^2 = (th-k1-k2)^2+k1^2+k2^2: %s; Bochner/Raychaudhuri: %s; class form (R): %s; "
              "shear-free form rejected: %s; torus Riccati: %s (wrong sign rejected: %s)"
              % (seed, c2, boch, ray, shearfree, c4, c4ctl))
        print("      th = %s, kappa = %s, |hess u|^2 = %s" % (q['th'], q['kap'], q['hess2']))
        ok &= c2 and boch and ray and shearfree and c4 and c4ctl
    # Bochner identity at a jet that is NOT null (code check): P(box u) + |hess|^2 + Ric(P,P) = (1/2) box N
    g, u = build(5, null_order=0)
    G, q = quantities(g, u)
    gi = G['gi']
    du = G['du']
    N = trunc(sum(gi[a, b] * du[a] * du[b] for a in range(5) for b in range(5)))
    Gam = G['Gam']
    boxN = at0(sum(gi[a, b] * (sp.diff(N, Y[a], Y[b]) - sum(Gam[c][a][b] * sp.diff(N, Y[c]) for c in range(5)))
                   for a in range(5) for b in range(5)))
    gen = sp.simplify(q['Pbox'] + q['hess2'] + q['RicPP'] - boxN / 2) == 0
    print("   Bochner's identity at a non-null jet, P(box u) + |hess u|^2 + Ric(P,P) = (1/2) box N:", gen)
    ok &= gen
    return ok


def controls():
    ok = True
    print("Controls (each must reject the class identity or the Raychaudhuri form)")
    g, u = build(11, null_order=0)
    _, q = quantities(g, u)
    r1 = sp.simplify(q['hess2'] - class_rhs(q)) != 0
    print("   no null condition: identity fails:", r1)
    g, u = build(11, null_order=2, phi12=sp.Rational(1, 3))
    _, q = quantities(g, u)
    r2 = sp.simplify(q['hess2'] - class_rhs(q)) != 0
    print("   g_(phi1 phi2) = 1/3 (T^2-invariant, not Z2 x Z2): identity fails:", r2)
    g, u = build(11, null_order=2, phi_dep=sp.Rational(2, 5))
    _, q = quantities(g, u)
    r3 = sp.simplify(q['hess2'] - class_rhs(q)) != 0
    print("   phase u + (1/5) phi1^2 (not invariant): identity fails:", r3)
    g, u = build(23, null_order=1)
    _, q = quantities(g, u)
    r4 = sp.simplify(q['Pbox'] + class_rhs(q) + q['RicPP']) != 0
    r4b = sp.simplify(q['hess2'] - class_rhs(q)) == 0
    print("   null only to first order: (R) fails at the point:", r4, "(while C2 still holds:", r4b, ")")
    ok = r1 and r2 and r3 and r4 and r4b
    return ok


if __name__ == '__main__':
    res = [c1(), c2_c3_c4(), controls()]
    print("PASS" if all(res) else "FAIL")
    sys.exit(0 if all(res) else 1)
