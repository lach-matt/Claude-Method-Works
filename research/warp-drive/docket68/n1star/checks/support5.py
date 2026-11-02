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


CHECKS = [("C4", c4), ("C6", c6), ("C8", c8)]


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
