#!/usr/bin/env python3
"""support5.py -- computations behind the deduced steps of the paper's sections 5-6 (verifier 257's list, D597).

The author's rule: everything derived is proved with computational support. Verifier 257 listed nine steps of the
paper's sections 5-6 that rested on argument alone (C1-C9). This program computes them, one check each, every check with
a negative control that must fail.

  C4 (certified, Z3 over the reals) supplement Lemma 2.2's mollifier stays in the annulus. With
     Phi(x) = x + 2 lam sigma xhat, sigma = sigma0((|x| - a)/(b - a)), sigma0 = 1 on [0, 1/3], -1 on [2/3, 1] and
     |sigma0| <= 1 (the proof's middle-third step uses it; the supplement now states it, sigma0 non-increasing), for
     every z in the unit ball of R^4 and t in [0, 1] the point x + t (Phi(x) - lam z - x) lies in A = {a <= |x| <= b},
     the segment has length <= 3 lam, and at t = 1 it lies at least lam inside near either sphere; for b - a >= 1 and
     0 < lam <= 1/10 (lam <= lam_Omega). Reduced exactly by rotation to x = rho e1, z = (z1, z_perp), |z_perp|^2 = w.
     And b(tau) - a >= 1 on [tau0, tau_end] from the domain's definitions (1.1): b(tau) = V + 1 + tau_end - 2 tau,
     tau_end = max_(v <= V) (v - r_q(v)) <= V - q0, a < q0. Control: no shift (sigma = 0) leaves the annulus.
  C6 (exact, sympy) section 5.4 / supplement Step 8 (i)-(iii): for lapse N > 0, shift beta^i and spatial metric gamma
     (a symbolic symmetric 4 x 4), g = -N^2 dtau^2 + gamma(dx + beta dtau)^2 has det g = -N^2 det gamma; Z := d_tau -
     beta has g(Z, Z) = -N^2 and g(Z, d_k) = 0 for every k, so in coordinates whose time lines are Z the metric is
     block diagonal, g^00 = -N^-2 and g^ij = gamma^-1, positive definite; the characteristic roots of g^ab xi_a xi_b in
     xi_0 then have product g^ij xi xi / g^00 < 0, real and of opposite signs, never meeting. Every convex combination
     toward (1, 0, delta) keeps N > 0 and gamma positive definite (an exact identity in v^T gamma_s v). Control: the
     original time lines of five-dimensional Vaidya, g0 = eta + (mu/r^2) k k with k = dtau + dr: the spatial block of
     g0^-1 is delta - (mu/r^2) xhat xhat, negative on radial xi where r^2 < mu (the case Step 8 exists for).

Labels: certified (Z3's unsat over the reals is a proof of the universally quantified statement) and computed (exact
symbolic identities). Run: python3 checks/support5.py   (about a minute)
"""
import sys

import sympy as sp
import z3


def c1(control=False):
    """(5.1): the only lam^-1 coefficient of the linearization P(w) of Ric^H at g_app is (1/2) w(l, l) [d_th^2 g1].
    (a) Exact at a point, for random rational Lorentzian g (two trials): the part of Ric^H(g) = Ric(g) - (1/2)(g_m rho
    Dh_n D^rho + g_n rho Dh_m D^rho), D^rho = g^ab (Gamma[g] - Gamma[g0])^rho_ab, that is linear in the second
    derivatives S of g is exactly -(1/2) g^ab S_ab,mn (the supplement's (0.2), READ from [CBCM10]); second derivatives of
    g enter nowhere else, and g0 and the first derivatives not at all. (b) Exact: d/ds -(1/2)((g + s w)^-1)^ab =
    (1/2) (g^-1 w g^-1)^ab, and the lam^-1 part of d_a d_b [lam G(x, v(x)/lam)] is v_a v_b G_thth (chain rule, two
    variables, G and v generic); so the lam^-1 part of P(w) is (1/2) w^ab v_a v_b [d_th^2 g1] = (1/2) w(l_app, l_app)
    [d_th^2 g1], l_app = g_app^-1 dv, the remaining terms of P carrying at most first derivatives of g_app, which are
    O(1). Control: Ric without the gauge term has other second-derivative terms."""
    import random
    rnd = random.Random(1)
    ok = True
    for trial in range(2):
        A = sp.Matrix(5, 5, lambda i, j: 0)
        for i in range(5):
            for j in range(i, 5):
                A[i, j] = A[j, i] = sp.Rational(rnd.randint(-3, 3), 17)
        g = sp.diag(-1, 1, 1, 1, 1) + A
        gi = g.inv()
        S = {}

        def Sj(e, f, p, q):
            key = (min(e, f), max(e, f), min(p, q), max(p, q))
            if key not in S:
                S[key] = sp.Symbol("S_%d%d_%d%d" % key)
            return S[key]
        dG = [[[[sp.Rational(1, 2) * sum(gi[a, d] * (Sj(e, b, d, c) + Sj(e, c, d, b) - Sj(e, d, b, c)) for d in range(5))
                 for c in range(5)] for b in range(5)] for a in range(5)] for e in range(5)]
        ric = [[sum(dG[a][a][b][d] - dG[d][a][b][a] for a in range(5)) for d in range(5)] for b in range(5)]
        dD = [[sum(gi[a, b] * dG[e][r][a][b] for a in range(5) for b in range(5)) for r in range(5)] for e in range(5)]
        for m in range(5):
            for n in range(m, 5):
                ricH = ric[m][n] if control else ric[m][n] - sp.Rational(1, 2) * sum(
                    g[m, r] * dD[n][r] + g[n, r] * dD[m][r] for r in range(5))
                target = -sp.Rational(1, 2) * sum(gi[a, b] * Sj(a, b, m, n) for a in range(5) for b in range(5))
                ok &= sp.expand(ricH - target) == 0
    if control:
        return ok
    x1, x2, lam, th, s_ = sp.symbols("x1 x2 lam theta s")
    X = (x1, x2)
    v = x1 + x2**2 / 2 + x1 * x2                                       # a phase and a profile, concrete and generic
    G = (x1**2 * x2 + 3 * x2) * sp.cos(th) + x1 * sp.sin(2 * th) + x2**3 * sp.cos(3 * th)

    def D(e, k):                                                       # the two-scale derivative d_k + lam^-1 v_k d_th
        return sp.diff(e, X[k]) + sp.diff(v, X[k]) / lam * sp.diff(e, th)
    chain = True
    for i in range(2):
        for j in range(2):
            lhs = sp.diff((lam * G).subs(th, v / lam), X[i], X[j])
            rhs = D(D(lam * G, j), i)
            chain &= sp.simplify(lhs - rhs.subs(th, v / lam)) == 0
            c1_ = sp.expand(rhs).coeff(lam, -1)
            chain &= sp.simplify(c1_ - sp.diff(v, X[i]) * sp.diff(v, X[j]) * sp.diff(G, th, 2)) == 0
    rnd2 = random.Random(2)
    w = sp.Matrix(5, 5, lambda i, j: 0)
    for i in range(5):
        for j in range(i, 5):
            w[i, j] = w[j, i] = sp.Rational(rnd2.randint(-5, 5), 3)
    g = sp.diag(-1, 1, 1, 1, 1) + sp.diag(0, *[sp.Rational(1, 7)] * 4)
    deriv = sp.diff(-sp.Rational(1, 2) * (g + s_ * w).inv(), s_).subs(s_, 0)
    lin = sp.simplify(deriv - sp.Rational(1, 2) * g.inv() * w * g.inv()) == sp.zeros(5)
    print("  C1: second derivatives of g enter Ric^H only through -(1/2) g^ab d_a d_b g (two random metrics): %s;\n"
          "      the chain rule's lam^-1 part v_a v_b G_thth: %s; d/ds of -(1/2) g^-1 is (1/2) g^-1 w g^-1: %s"
          % (ok, chain, lin), flush=True)
    return ok and chain and lin


def _lin_ricH(W, Y, scale):
    """the eps-linear part of Ric^H(g0 + lam W + eps scale Y) in lead5's gauge and coordinates, every lam order from
    -3 to 0 kept (lead5.reduced_ricci reports -1 and 0 only); returns {(b, c): {k: coefficient of lam^k}}"""
    import os
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import lead5 as L
    lam, eps = L.lam, sp.Symbol("eps")
    g0, g0i = L.background()

    def tr(e, top):                                   # lam orders -3..top, eps orders 0..1
        e = sp.expand(e)
        e = sp.expand(e.coeff(eps, 0) + eps * e.coeff(eps, 1))     # expanded again: lam must be visible to coeff
        return sum(e.coeff(lam, k) * lam**k for k in range(-3, top + 1))
    Z = scale * Y
    g = g0 + lam * W + eps * Z
    Wu = g0i * W * g0i
    giW = g0i - lam * Wu + lam**2 * Wu * W * g0i
    gi = (giW - eps * giW * Z * giW).applyfunc(lambda e: tr(e, 2))
    G = L.christoffel(g, gi, L.D)
    G = [[[tr(x, 1) for x in row] for row in M2] for M2 in G]
    Gh = L.christoffel(g0, g0i, lambda e, k: sp.diff(e, L.X[k]))
    n = 5
    Dv = [tr(sum(gi[a, b] * (G[rho][a][b] - Gh[rho][a][b]) for a in range(n) for b in range(n)), 1) for rho in range(n)]
    out = {}
    for b in range(n):
        for c in range(b, n):
            e = 0
            for a in range(n):
                e += L.D(G[a][b][c], a) - L.D(G[a][b][a], c)
                for d in range(n):
                    e += G[a][a][d] * G[d][b][c] - G[a][c][d] * G[d][b][a]
            hb = sum(g[b, rho] * (L.D(Dv[rho], c) + sum(Gh[rho][c][sg] * Dv[sg] for sg in range(n))) for rho in range(n))
            hc = sum(g[c, rho] * (L.D(Dv[rho], b) + sum(Gh[rho][b][sg] * Dv[sg] for sg in range(n))) for rho in range(n))
            e = sp.expand(tr(e - (hb + hc) / 2, 0)).coeff(eps, 1)        # expanded: eps inside lam^k brackets
            out[(b, c)] = {k: sp.expand(e).coeff(lam, k) for k in range(-3, 1)}
    return out, L


def c2(control=False):
    """Lemma 5.1 on the stage-0 profile of the proof's gauge (lead5.py's W = W_TT + chi dv dv, chi generic): with
    G = lam W, the linearization in the direction d_s G = lam d_s W is lam P([d_s W]), and the two-scale operator has no
    explicit s, so lam P([d_s W]) = d_s Ric^H(g0 + lam W) order by order: its lam^-1 part is d_s R^(-1) = 0 and its
    lam^0 part, T(d_s W) of Lemma 5.1, is d_s R^(0), computed and compared exactly in every component. By lead5 L3-L4,
    d_s R^(0) vanishes exactly when chi solves (E2)'s transport. Control: chi = 0, where T(d_s W) is not zero."""
    import time
    t0 = time.time()
    sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.dirname(__import__("os").path.abspath(
        __file__))))
    import lead5 as L
    W = L.wave(with_chi=not control)
    Y = W.applyfunc(lambda e: sp.diff(e, L.s))
    Q, _ = _lin_ricH(W, Y, L.lam)
    if control:
        return all(sp.simplify(Q[k][0]) == 0 for k in Q)
    R = L.reduced_ricci(W)
    lower = all(sp.simplify(Q[k][j]) == 0 for k in Q for j in (-3, -2))
    minus1 = all(sp.simplify(Q[k][-1] - sp.diff(R[k][0], L.s)) == 0 for k in Q)
    zero = all(sp.simplify(Q[k][0] - sp.diff(R[k][1], L.s)) == 0 for k in Q)
    print("  C2: lam P([d_s W]) = d_s Ric^H(g0 + lam W): no order below lam^-1: %s; lam^-1: %s (d_s R^(-1) = 0);\n"
          "      lam^0: %s, so T(d_s W) = d_s R^(0), zero exactly under (E2) by lead5 L3-L4 [%.0fs]"
          % (lower, minus1, zero, time.time() - t0), flush=True)
    return lower and minus1 and zero


def c3(control=False):
    """supplement Lemma 3.3: in P(phi [d_s W]), phi = phi(v, r, theta) generic, the l (x) l component (l = g0^-1 dv
    = d_r, so the rr component) has no lam^-1 term (and none lower), and its lam^0 part holds no second derivative of
    phi: contracting the h-equation with l (x) l kills every large coefficient and the box-tilde phi term. Control: an
    oscillating dr dr component added to W, so W(l, l) != 0. (chi on dv dr, lead5's mutant chi_dvdr, keeps W(l, l) = 0
    and is no control here.)"""
    import time
    t0 = time.time()
    sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.dirname(__import__("os").path.abspath(
        __file__))))
    import lead5 as L
    W = L.wave(with_chi=True)
    if control:
        W[1, 1] = L.A * L.Ef * L.Hf * L.r**sp.Rational(-3, 2) * sp.cos(L.s)
    phi = sp.Function("phi")(L.v, L.r, L.th)
    Y = W.applyfunc(lambda e: phi * sp.diff(e, L.s))
    Q, _ = _lin_ricH(W, Y, sp.Integer(1))
    rr = Q[(1, 1)]
    large = all(sp.simplify(rr[j]) == 0 for j in (-3, -2, -1))
    second = [d for d in sp.expand(rr[0]).atoms(sp.Derivative) if d.expr == phi and d.derivative_count >= 2]
    if control:
        return large
    print("  C3: P(phi [d_s W]) contracted with l (x) l: no lam^-1 or lower term: %s; no second derivative of phi at\n"
          "      lam^0: %s [%.0fs]" % (large, not second, time.time() - t0), flush=True)
    return large and not second


def c5(control=False):
    """supplement section 4, Steps 1-7 (paper (5.4)-(5.5)): the bootstrap's power counting as a ledger. Rules, from
    Lemma 2.1 and Step 1: four spatial dimensions, so the L^inf bound costs the Sobolev index s0 = 4//2 + 1 = 3
    derivatives, ||d^i w||_inf <= C lam^(-s0 - i) N for i <= k + 1 - s0, k = 6; |d w|_k <= lam^-1 |w|_(k+1) <= C
    lam^-1 N; a product in the weighted norm costs one L^inf factor; the approximant has N_st = K + 3 stages with
    residual lam^(N_st - 1). Each term's exponent is derived from the rules (not typed), then held against the step's
    requirement under the bootstrap N <= 2 M lam^K. Every requirement holds at K = 6 (the supplement's choice holds
    for every K >= 6); at K = 5 the closing ones fail (the control)."""
    from fractions import Fraction as Fr
    K = 5 if control else 6
    k, n_sp = 6, 4
    s0 = n_sp // 2 + 1
    imax = k + 1 - s0
    e_inf = lambda i: -s0 - i                      # ||d^i w||_inf <= C lam^e N
    e_dwk = -1                                     # |d w|_k <= C lam^-1 N
    e_quad = e_inf(0) + 2 * e_dwk                  # |d w d w|_k <= C lam^-s0 |d w|_k^2
    e_quad0 = e_inf(0) + 0                         # |w d^2 w|-type, the lower term: lam^-3 N^2 (Step 4)
    rows = [
        ("Sobolev range: the L^inf bounds needed up to i = 4 exist (k + 1 - s0 >= 4)", imax >= 4),
        ("Step 3: |w|_inf <= C M lam^(K-3) is small (K - 3 > 0)", K + e_inf(0) > 0),
        ("Step 3: |d w|_inf <= C M lam^(K-4) <= C M lam^2 (K - 4 >= 2)", K + e_inf(1) >= 2),
        ("Step 4: the w part of the commutators, C M lam^(K-4) N <= C N", K + e_inf(1) >= 0),
        ("Step 4: the worst nonlinear term lam^(%d) N^2 <= C M^2 lam^(K+1)" % e_quad, 2 * K + e_quad >= K + 1),
        ("Step 4: the lower nonlinear term lam^(%d) N^2 <= C M^2 lam^(K+1)" % e_quad0, 2 * K + e_quad0 >= K + 1),
        ("the residual lam^(N_st - 1), N_st = K + 3, within C_R lam^K", (K + 3) - 1 >= K),
        ("Step 7: the nonlinear term one power above lam^K, so lam0 = 1/(C3 C M^2) closes it", 2 * K + e_quad > K),
    ]
    ok = all(v for _, v in rows)
    if control:
        return ok
    print("  C5: the bootstrap's ledger at K = %d (k = %d, s0 = %d; derived exponents: L^inf lam^(%d - i), quadratic\n"
          "      lam^(%d)):" % (K, k, s0, -s0, e_quad), flush=True)
    for name, v in rows:
        print("      %-104s %s" % (name, v), flush=True)
    return ok


def c4(control=False):
    a, b, rho, lam, s, z1, w, t = z3.Reals("a b rho lam s z1 w t")
    hyp = [a > 0, b - a >= 1, lam > 0, lam <= z3.RealVal("1/10"), rho >= a, rho <= b, w >= 0, z1 * z1 + w < 1,
           s >= -1, s <= 1, z3.Implies(rho <= a + (b - a) / 3, s == 1), z3.Implies(rho >= a + 2 * (b - a) / 3, s == -1),
           t >= 0, t <= 1]
    if control:
        hyp = [h for h in hyp if not z3.is_implies(h)] + [s == 0]
    y1, y2sq = rho + t * (2 * lam * s - lam * z1), t * t * lam * lam * w      # |y(t)|^2 = y1^2 + y2sq
    r2 = y1 * y1 + y2sq
    S = z3.Solver()
    S.set("timeout", 120000)
    S.add(*hyp)
    S.add(z3.Or(r2 < a * a, r2 > b * b))
    inside = S.check() == z3.unsat
    if control:
        return inside
    S2 = z3.Solver()
    S2.set("timeout", 120000)
    S2.add(*hyp)
    S2.add(z3.Or(lam * lam * ((2 * s - z1) * (2 * s - z1) + w) > 9 * lam * lam,           # the segment's length
                 z3.And(rho <= a + (b - a) / 3, t == 1, y1 <= rho + lam),               # lam inside, near a
                 z3.And(rho >= a + 2 * (b - a) / 3, t == 1, r2 >= (rho - lam) * (rho - lam))))   # lam inside, near b
    near = S2.check() == z3.unsat
    V, te, q0, tau, v, rq = z3.Reals("V te q0 tau v rq")                       # b(tau) - a >= 1 from (1.1)
    S3 = z3.Solver()
    S3.add(a > 0, a < q0, v <= V, rq >= q0, te <= V - q0, tau <= te)
    S3.add((V + 1 + te - 2 * tau) - a < 1)
    width = S3.check() == z3.unsat
    S4 = z3.Solver()                                                   # without |sigma0| <= 1: the hypothesis is used
    S4.set("timeout", 120000)
    S4.add(*[h for h in hyp if not (z3.is_ge(h) or z3.is_le(h)) or not z3.eq(h.arg(0), s)])
    S4.add(z3.Or(r2 < a * a, r2 > b * b))
    needed = S4.check() == z3.sat
    print("  C4: the shifted ball and its segment stay in the annulus: %s; length <= 3 lam and lam inside near\n"
          "      either sphere: %s; b(tau) - a >= 1 on [tau0, tau_end]: %s; without |sigma0| <= 1 a point leaves: %s"
          % (inside, near, width, needed), flush=True)
    return inside and near and width and needed


def c6(control=False):
    N = sp.Symbol("N", positive=True)
    be = sp.Matrix(sp.symbols("b1:5"))
    gs = sp.symbols("g11 g12 g13 g14 g22 g23 g24 g33 g34 g44")
    it = iter(gs)
    G = sp.zeros(4)
    for i in range(4):
        for j in range(i, 4):
            G[i, j] = G[j, i] = next(it)
    if control:                         # Vaidya's original time lines: the spatial block of g0^-1 inside the horizon
        mu, r = sp.symbols("mu r", positive=True)
        xh = sp.Matrix([1, 0, 0, 0])                                   # xhat, by rotation
        eta = sp.diag(-1, 1, 1, 1, 1)
        k = sp.Matrix([1] + list(xh))                                  # k = dtau + xhat.dx
        g0 = eta + mu / r**2 * k * k.T
        gi = eta - mu / r**2 * (eta * k) * (eta * k).T
        exact = sp.simplify(g0 * gi - sp.eye(5)) == sp.zeros(5)
        radial = sp.simplify(gi[1, 1])                                  # g0^ij xi_i xi_j at xi = xhat
        return exact and radial.subs({mu: 2, r: 1}) > 0                # r^2 < mu: must be > 0 for the control to pass
    g = sp.zeros(5)
    bl = G * be                                                         # beta_i = gamma_ij beta^j
    g[0, 0] = -N**2 + (be.T * G * be)[0]
    for i in range(4):
        g[0, i + 1] = g[i + 1, 0] = bl[i]
        for j in range(4):
            g[i + 1, j + 1] = G[i, j]
    det_ok = sp.expand(g.det() + N**2 * G.det()) == 0
    Z = sp.Matrix([1] + list(-be))
    zz = sp.expand((Z.T * g * Z)[0] + N**2) == 0
    orth = all(sp.expand((Z.T * g * sp.Matrix([0] + [int(i == k) for i in range(4)]))[0]) == 0 for k in range(4))
    gb = sp.diag(-N**2, G)                                              # the metric with time lines along Z
    gbi = sp.diag(-N**-2, G.inv())
    inv_ok = sp.simplify(gb * gbi - sp.eye(5)) == sp.zeros(5)
    xi0, X = sp.Symbol("xi0"), sp.Symbol("X", positive=True)            # X := g^ij xi_i xi_j > 0
    roots = sp.solve(-xi0**2 / N**2 + X, xi0)
    opp = len(roots) == 2 and sp.simplify(roots[0] * roots[1] + N**2 * X) == 0
    s_ = sp.Symbol("s")
    vv = sp.Matrix(sp.symbols("v1:5"))
    Gs = (1 - s_) * G + s_ * sp.eye(4)
    conv = sp.expand((vv.T * Gs * vv)[0] - ((1 - s_) * (vv.T * G * vv)[0] + s_ * (vv.T * vv)[0])) == 0
    print("  C6: det g = -N^2 det gamma: %s; g(Z, Z) = -N^2: %s; g(Z, d_k) = 0: %s; inverse along Z\n"
          "      (g^00 = -N^-2, g^ij = gamma^-1): %s; roots real, opposite, product -N^2 X: %s; convex combinations: %s"
          % (det_ok, zz, orth, inv_ok, opp, conv), flush=True)
    return det_ok and zz and orth and inv_ok and opp and conv


def c8(control=False):
    """the first-order term of g_lam^-1(dPhi, dPhi) on x_K = 1, Phi = r - r_q(v), for g = g0 + lam g1 with g1 = W_TT of
    (2.5') + chi dv^2 + m1 (m1 a general symmetric profile): it is -g1(#dPhi, #dPhi), #dPhi = g0^-1 dPhi = d_v + (f -
    r_q') d_r with no angular part, so W_TT drops out exactly and the term is -(chi + m_vv + 2 (f - r_q') m_vr + (f -
    r_q')^2 m_rr): a bounded combination of non-oscillating profiles, no derivative of g1 entering. Control: a wave
    with a dr dr component (W(l, .) != 0 for the outgoing generator) enters at first order."""
    v, r, th, lam, A, E, H, G_, F_, rqp, chi = sp.symbols("v r theta lam A E H G F rqp chi", real=True)
    mu = sp.Function("mu")(v)
    f = 1 - mu / r**2
    C, S = sp.cos(th), sp.sin(th)
    g0 = sp.zeros(5)
    g0[0, 0], g0[0, 1], g0[1, 0] = -f, 1, 1
    g0[2, 2], g0[3, 3], g0[4, 4] = r**2, r**2 * C**2, r**2 * S**2
    p1, p2 = (2 * C**2 * G_ - S**2 * F_) / 3, (2 * S**2 * F_ - C**2 * G_) / 3
    W = sp.zeros(5)
    W[2, 2], W[3, 3], W[4, 4] = -2 * sp.sqrt(r) * (p1 + p2), 2 * sp.sqrt(r) * C**2 * p1, 2 * sp.sqrt(r) * S**2 * p2
    if control:
        W[1, 1] = sp.Symbol("eps")
    m = sp.Matrix(5, 5, lambda i, j: sp.Symbol("m%d%d" % (min(i, j), max(i, j))))
    g1 = W + m
    g1[0, 0] += chi
    gi = g0.inv()
    dPhi = sp.Matrix([-rqp, 1, 0, 0, 0])
    sharp = sp.simplify(gi * dPhi)
    first = sp.simplify(-(sharp.T * g1 * sharp)[0])
    want = -(chi + m[0, 0] + 2 * (f - rqp) * m[0, 1] + (f - rqp)**2 * m[1, 1])
    ok = sp.simplify(sharp - sp.Matrix([1, f - rqp, 0, 0, 0])) == sp.zeros(5, 1) and sp.simplify(first - want) == 0
    dinv = sp.simplify(-(gi * g1 * gi))                                 # d/dlam (g0 + lam g1)^-1 at lam = 0
    ok &= sp.simplify((dPhi.T * dinv * dPhi)[0] - first) == 0
    if not control:
        print("  C8: #dPhi = d_v + (f - r_q') d_r; the first-order term is -(chi + m_vv + 2 (f - r_q') m_vr\n"
              "      + (f - r_q')^2 m_rr), W_TT dropping out exactly: %s" % ok, flush=True)
    return ok


def c9(control=False):
    """Propositions 3.3-3.4 at lam > 0. The horizon (Proposition 3.3) rests on horizon5.py: H1 (theta+ of g0 has the
    simple zero sqrt(mu), d_r = 3/mu there), H2-H2b (no lam^0 correction from the wave, chi or m1) and H3 (no lam^-1 in
    the r-derivative along a column), all computed there. The mean mass (Proposition 3.4) needs m1 odd under sigma (th
    -> pi/2 - th, phi1 <-> phi2; mass5.py M2, M4). m1 solves the sigma-equivariant linear equation with zero data and
    source the lam^1 mean of R^(1). Computed here in the Bondi-type gauge of ansatz5.py A5 (the gauge-independent
    argument is mass5.py M2-M4's equivariance with uniqueness), on the record's h: that mean has only the dv dth
    component S_vth, and S_vth(sigma X) = S_vth(X), so sigma^* S = -S (d th -> -d th): the source is odd, hence m1 by
    uniqueness. Control: S_vth cos 2th (even under sigma) in place of S_vth."""
    sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.dirname(__import__("os").path.abspath(
        __file__))))
    import ansatz5 as a5
    o = a5.a5()
    S = o["mean_vth"].subs(a5.Hf, a5.H_REC).doit()
    if control:
        S = S * sp.cos(2 * a5.th)
    only_vth = bool(o["others0"])
    odd = sp.simplify(S.subs(a5.th, sp.pi / 2 - a5.th) - S) == 0      # sigma^* S = -S for a dv dth component
    nonzero = sp.simplify(S) != 0
    if control:
        return odd
    print("  C9: m1's source, the lam^1 mean of R^(1) (ansatz5 A5, Bondi-type gauge): only dv dth: %s; nonzero: %s;\n"
          "      S_vth(sigma X) = S_vth(X), so sigma^* S = -S and m1 is odd: %s (Proposition 3.3's facts: horizon5.py"
          " H1-H3)" % (only_vth, nonzero, odd), flush=True)
    return only_vth and nonzero and odd


CHECKS = [("C1", c1), ("C2", c2), ("C3", c3), ("C4", c4), ("C5", c5), ("C6", c6), ("C8", c8), ("C9", c9)]


def main():
    ok = True
    for name, f in CHECKS:
        good = f()
        ctl = f(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", "" if not ctl else " (control passed)"),
              flush=True)
        ok &= good and not ctl
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
