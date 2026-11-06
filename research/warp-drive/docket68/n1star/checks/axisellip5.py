#!/usr/bin/env python3
"""axisellip5: the planar shear recovered at the axis, inside the class, by elliptic regularity of the eikonal's level
sets in the slice (FAMILIES5-AXIS.md section 3).

FAMILIES5-NONROUND.md section 4 located the loss at the axes: there kappa2 = g^-1(du, d psi2) is a second derivative of
u, and the planar shear s = th_h - kappa2 enters the class Raychaudhuri equation through |chi|^2 = kappa1^2 + (1/2)(th -
kappa1)^2 + (1/2) s^2 (axisloss5 X1 (e)). The flat recovery s = f - 2 A f (X3) loses nothing (the independent reader:
A is a dilation average); the question is the curved terms. Here they are computed, in the slice picture: on Sigma_tau
the section S_c = {u = c} cap Sigma_tau of the family's null hypersurface, and its planar leaf Sigma2 = S_c cap M3 in
the totally geodesic three-manifold M3 = Sigma_tau cap {phi1 = 0} (the fixed set of phi1 -> -phi1).

  E0 (exact at rational jets; classchi5's class metrics, three seeds) for X, Y tangent to M3:
         hess_g(u)(X, Y) = hess_M3(u)(X, Y) - n(u) K(X, Y)                                              (G)
     (n the unit normal of Sigma_tau, K its second fundamental form, K(X, Y) = g(nabla_X n, Y)), and for a null phase
     the trace of hess_g(u) over T Sigma2 (orthonormal, in M3) is box u - kappa1. So th - kappa1 = |grad u| H2 - n(u)
     tr K|Sigma2, H2 the mean curvature of the leaf Sigma2 in M3 (sign: k = hess_M3(u)/|grad_M3 u|), and the planar
     shear is |grad u| (k_r - k_ph) - n(u) (K_rr - K_phph): the slice's K (first order in g) and the leaf's trace-free
     second fundamental form. No torsion of the null hypersurface and no curvature component appears.
     Controls (must fail): (G) without the K term; the trace over the coordinate plane span(d_y1, d_ph2) in place of
     T Sigma2.
  E1 (exact, sympy) the leaf's equation at the axis. M3 near the axis, every smooth invariant metric: gamma3 = A dz^2 +
     2 C r dz dr + (B + D r^2) dr^2 + B r^2 dph^2, A, B, C, D functions of (z, r^2) (z along the axis, r the distance
     from it); the leaf z = h(r), h = h(r^2) smooth. With F = z - h, k = hess(F)/|grad F|:
     (a) H2 = k_r + k_ph is linear in h'' with coefficient a, and E := r H2 / a - (r h')' contains no h''; E and k_ph
         contain only first derivatives of A, B, C, D (read off the expressions);
     (b) on polynomial instances (three random metrics and leaves with rational coefficients, h a polynomial in r^2;
         evaluated at 50 digits at r = 1e-4, ..., 1e-8) E / r and k_ph settle to finite values at the axis (no 1/r):
         the leaf obeys the regular Volterra equation
             r h'(r) = int_0^r (rho H2 / a - E) d rho,                                                        (V)
         and the leaf's planar shear is sigma := (k_r - k_ph)/2 = H2/2 - k_ph[h, h'].
     So the map H2 -> sigma involves gamma3 and its first derivatives only: the curved, non-planar terms are first
     order in the metric, and the 1/r of kappa2 (X1 (c)) is absorbed by the integral from the axis.
     Controls (must fail): a metric with the non-smooth cross term C dz dr (for C r dz dr) has k_ph unbounded at the
     axis; the derivative reader applied to a Ricci component of gamma3 finds second derivatives (it can see them).
  E2 (computed, scipy quadrature; a curved invariant metric with A, B, C, D non-constant) the estimate behind it,
     for leaves concentrating at the axis, h_eps(r) = eps^2 exp(-r^2/eps^2), eps = 0.2, 0.1, 0.05, 0.025, measured
     against the background leaf z = 0 (which has O(1) mean curvature in this metric), on the disc r < 1/2 with the
     weight r dr: ||d sigma|| / ||d H2|| tends to the flat value 1/2 and ||d_r d sigma|| / ||d_r d H2|| stays bounded
     and converges (to 3 % between the last two), while the first-order route ||d k_ph|| / ||h'|| grows like 1/eps
     (X2's loss, here with curvature): control (must grow). (Round 5, the verifier of round 4, minor 6: these ratios
     are frozen-coefficient limits -- 1/(2 sqrt 3) = 0.2887 is the flat Gaussian value -- and show no loss at m = 0,
     1 only.)
     Reconstruction (scipy, DOP853): integrating the leaf's equation from the axis as an ODE for (h, h') with H2 given
     and the axis regularity h'(r0) = 0 (round 5: not the exact leaf's slope; h(r0) is the leaf parameter) recovers h'
     and sigma = H2/2 - k_ph to the integrator's tolerance. Control (must fail): the same integration with
     the flat equation h'' + h'/r = H2 misses h' by the size of the metric's gradient.

Labels: computed (E0 exact at jets, checks/jetpoly5.py and checks/classchi5.py; E1 (a) exact, sympy, (b) 50-digit
evaluation of exact expressions; E2 scipy).
Run: python3 checks/axisellip5.py   (a few minutes)
"""
from fractions import Fraction
import math
import os
import random
import sys

import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from jetpoly5 import Jet, geometry  # noqa: E402
import classchi5 as CC  # noqa: E402

N5 = 5


def gram_schmidt(vecs, G):
    out = []
    for v in vecs:
        w = list(v)
        for e in out:
            c = sum(G[i][j] * w[i] * e[j] for i in range(len(w)) for j in range(len(w)))
            w = [wi - c * ei for wi, ei in zip(w, e)]
        nn = sum(G[i][j] * w[i] * w[j] for i in range(len(w)) for j in range(len(w)))
        out.append([sp.nsimplify(x) / sp.sqrt(sp.nsimplify(nn)) for x in w])
    return out


def e0():
    print("E0 (exact at jets) the Gauss formula (G) and the planar trace th - kappa1, in the class")
    ok = True
    for seed in (11, 23, 37):
        g, u = CC.build(seed, null_order=2)
        G = geometry(g, u)
        gi0, g0 = G['gi0'], G['g0']
        R = lambda q: sp.Rational(q.numerator, q.denominator)                    # noqa: E731
        H0 = [[R(G['H'][a][b].at0()) for b in range(N5)] for a in range(N5)]
        du0 = [R(x.at0()) for x in G['du']]
        Gam0 = [[[R(G['Gam'][c][a][b].at0()) for b in range(N5)] for a in range(N5)] for c in range(N5)]
        g0s = [[R(x) for x in row] for row in g0]
        gi0s = [[R(x) for x in row] for row in gi0]
        # slice y0 = const: n_c = -alpha delta_c^0, alpha = 1/sqrt(-g^00); K_ij = -n_c Gam^c_ij = alpha Gam^0_ij
        alpha = 1 / sp.sqrt(-gi0s[0][0])
        nup = [-alpha * gi0s[a][0] for a in range(N5)]
        nu = sum(nup[a] * du0[a] for a in range(N5))                              # n(u)
        K = lambda i, j: alpha * Gam0[0][i][j]                                    # noqa: E731
        # M3 = {y0 = const, phi1 = 0}: coordinates y1, y2, phi2 (indices 1, 2, 4); its metric and Christoffels
        idx = [1, 2, 4]
        gM = sp.Matrix(3, 3, lambda i, j: g0s[idx[i]][idx[j]])
        giM = gM.inv()
        # Christoffels of M3 at the point: from the jets of g restricted (derivatives in y1, y2 only)
        dgM = [[[R(g[idx[i]][idx[j]].d(idx[k]).at0()) for k in range(3)] for j in range(3)] for i in range(3)]
        GamM = [[[sum(giM[c, d] * (dgM[d][a][b] + dgM[d][b][a] - dgM[a][b][d]) for d in range(3)) / 2
                  for b in range(3)] for a in range(3)] for c in range(3)]
        d2u = [[R(u.d(idx[a]).d(idx[b]).at0()) for b in range(3)] for a in range(3)]
        duM = [du0[i] for i in idx]
        HM = [[d2u[a][b] - sum(GamM[c][a][b] * duM[c] for c in range(3)) for b in range(3)] for a in range(3)]
        # (G) on all pairs of M3 coordinate vectors
        okG = all(sp.simplify(H0[idx[a]][idx[b]] - (HM[a][b] - nu * K(idx[a], idx[b]))) == 0
                  for a in range(3) for b in range(3))
        badG = any(sp.simplify(H0[idx[a]][idx[b]] - HM[a][b]) != 0 for a in range(3) for b in range(3))
        # T Sigma2 in M3: the vector orthogonal (in M3) to grad_M3 u within span(d_y1, d_y2), and d_phi2
        gradM = [sum(giM[a, b] * duM[b] for b in range(3)) for a in range(3)]
        # t in span(d_y1, d_y2), M3-orthogonal to gradM: t^a g_ab gradM^b = 0 with t in span(d1, d2)
        c1 = sum(gM[0, b] * gradM[b] for b in range(3))
        c2 = sum(gM[1, b] * gradM[b] for b in range(3))
        t = [c2, -c1, 0]
        e = gram_schmidt([t, [0, 0, 1]], [[gM[i, j] for j in range(3)] for i in range(3)])
        tr = sum(H0[idx[a]][idx[b]] * v[a] * v[b] for v in e for a in range(3) for b in range(3))
        th = sum(gi0s[a][b] * H0[a][b] for a in range(N5) for b in range(N5))
        G1 = g[3][3]
        dpsi1 = [R(G1.d(k).at0()) / (2 * R(G1.at0())) for k in range(N5)]
        kap1 = sum(gi0s[a][b] * du0[a] * dpsi1[b] for a in range(N5) for b in range(N5))
        okT = sp.simplify(tr - (th - kap1)) == 0
        # control: trace over the coordinate plane span(d_y1, d_phi2) instead of T Sigma2
        ec = gram_schmidt([[1, 0, 0], [0, 0, 1]], [[gM[i, j] for j in range(3)] for i in range(3)])
        trc = sum(H0[idx[a]][idx[b]] * v[a] * v[b] for v in ec for a in range(3) for b in range(3))
        badT = sp.simplify(trc - (th - kap1)) != 0
        print("   seed %d: (G) %s; planar trace = box u - kappa1: %s; controls: without K %s, coordinate plane %s"
              % (seed, okG, okT, badG, badT))
        ok &= okG and okT and badG and badT
    return ok


z, r, s = sp.symbols('z r s', positive=True)


def leaf_quantities(A, B, C, D, h, cross=1):
    """the principal curvatures k_r, k_ph of the leaf z = h(r) in gamma3 (A, B, C, D functions of z, s = r^2); cross = 0
    replaces the smooth cross term C r dz dr by the non-smooth C dz dr (the control)."""
    X = [z, r]
    sub = {s: r**2}
    m = sp.Matrix([[A, C * r**cross], [C * r**cross, B + D * r**2]]).subs(sub)
    l2 = (B * r**2).subs(sub)
    g3 = sp.diag(m, l2)
    Y = [z, r, sp.Symbol('ph')]
    gi = g3.inv()

    def Gam(c, a, b):
        return sum(gi[c, d] * (sp.diff(g3[d, a], Y[b]) + sp.diff(g3[d, b], Y[a]) - sp.diff(g3[a, b], Y[d]))
                   for d in range(3)) / 2
    F = z - h
    dF = [sp.diff(F, v) for v in Y]
    Hs = lambda a, b: sp.diff(F, Y[a], Y[b]) - sum(Gam(c, a, b) * dF[c] for c in range(3))   # noqa: E731
    nF = sp.sqrt(sum(gi[a, b] * dF[a] * dF[b] for a in range(3) for b in range(3)))
    T = [sp.diff(h, r), 1, 0]
    nT2 = sum(g3[a, b] * T[a] * T[b] for a in range(3) for b in range(3))
    kr = sum(Hs(a, b) * T[a] * T[b] for a in range(3) for b in range(3)) / (nT2 * nF)
    kph = Hs(2, 2) / (g3[2, 2] * nF)
    return kr, kph, X


def e1():
    print("E1 (exact) the leaf's equation at the axis: a regular Volterra equation with first-order coefficients")
    A, B, C, D = [sp.Function(nm)(z, s) for nm in ('A', 'B', 'C', 'D')]
    hf = sp.Function('h')(r)
    kr, kph, _ = leaf_quantities(A, B, C, D, hf)
    zh = {z: hf}
    kr, kph = kr.subs(zh), kph.subs(zh)
    H2 = kr + kph
    hpp = sp.Derivative(hf, (r, 2))
    Hx = sp.expand(H2.doit())
    W = sp.Symbol('W')
    Hw = Hx.subs(hpp, W)
    a = sp.simplify(sp.diff(Hw, W))
    lin = sp.simplify(sp.diff(Hw, W, 2)) == 0
    rest = sp.simplify(Hw - a * W)
    E = sp.simplify(r * rest / a - sp.Derivative(hf, r))
    noh2 = not E.has(hpp) and not kph.doit().has(hpp)

    def max_metric_order(e):
        mo = 0
        for d in e.atoms(sp.Derivative):
            if d.expr.func.__name__ in ('A', 'B', 'C', 'D'):
                mo = max(mo, sum(k for _, k in d.variable_count))
        return mo
    oE, oK = max_metric_order(E.doit()), max_metric_order(kph.doit())
    print("   H2 linear in h'': %s; E and k_ph free of h'': %s; highest metric derivative in E: %d, in k_ph: %d"
          % (lin, noh2, oE, oK))
    # control for the reader: the scalar curvature of gamma3 has second derivatives
    m3 = sp.Matrix([[A, C * r, 0], [C * r, B + D * r**2, 0], [0, 0, B * r**2]]).subs(s, r**2)
    Y = [z, r, sp.Symbol('ph')]
    gi = m3.inv()
    Gm = [[[sum(gi[c, d] * (sp.diff(m3[d, a_], Y[b]) + sp.diff(m3[d, b], Y[a_]) - sp.diff(m3[a_, b], Y[d]))
                for d in range(3)) / 2 for b in range(3)] for a_ in range(3)] for c in range(3)]
    Ric00 = sum(sp.diff(Gm[c][0][0], Y[c]) - sp.diff(Gm[c][0][c], Y[0]) for c in range(3))
    ctl_ord = max_metric_order(Ric00.doit()) == 2
    print("   control: the reader finds second derivatives in a Ricci component of gamma3:", ctl_ord)
    # (b) regularity at the axis on polynomial instances
    rng = random.Random(5)

    def rp(c0):
        return c0 + sum(sp.Rational(rng.randint(-6, 6), 13) * z**i * s**j for i in range(3) for j in range(2)
                        if i + j > 0)

    def instance(Ai, Bi, Ci, Di, hh, cross):
        hq = sp.Function('hq')(r)
        krq, kphq, _ = leaf_quantities(Ai, Bi, Ci, Di, hq, cross)
        Hq = (krq + kphq).subs(z, hq).doit()
        Hqw = Hq.subs(sp.Derivative(hq, (r, 2)), W)
        aq = sp.diff(Hqw, W)
        Eq = (r * (Hqw - aq * W) / aq - sp.Derivative(hq, r)).subs(hq, hh).doit()
        return Eq, kphq.subs(z, hq).subs(hq, hh).doit()
    okb, ctl_con = True, True
    for trial in range(3):
        Ai, Bi = rp(sp.Rational(3, 2)), rp(sp.Rational(5, 4))
        Ci, Di = rp(sp.Rational(1, 5)), rp(sp.Rational(1, 7))
        hh = sp.Rational(rng.randint(1, 5), 10) + sum(sp.Rational(rng.randint(-5, 5), 11) * (r**2)**j
                                                       for j in range(1, 3))
        Ei, Ki = instance(Ai, Bi, Ci, Di, hh, 1)
        Ec, Kc = instance(Ai, Bi, Ci, Di, hh, 0)
        fE, fK, fKc = [sp.lambdify(r, x, 'mpmath') for x in (Ei / r, Ki, Kc)]
        mp.mp.dps = 50
        rs = [mp.mpf(10)**(-k) for k in (4, 5, 6, 7, 8)]
        vE, vK, vC = [[f(q) for q in rs] for f in (fE, fK, fKc)]
        settle = all(abs(v[-1] - v[-2]) < mp.mpf('1e-12') for v in (vE, vK))
        okb &= settle
        ctl_con &= all(abs(vC[i + 1]) > 5 * abs(vC[i]) for i in range(len(rs) - 1))
        mp.mp.dps = 30
        print("   instance %d: E/r -> %s, k_ph -> %s (settled to 1e-12 at r = 1e-8: %s); control (cross term C dz dr): "
              "k_ph = %s at r = 1e-8, growing like 1/r: %s" % (trial, mp.nstr(vE[-1], 10), mp.nstr(vK[-1], 10), settle,
                                                              mp.nstr(vC[-1], 4), ctl_con))
    return lin and noh2 and oE <= 1 and oK <= 1 and ctl_ord and okb and ctl_con


mp.mp.dps = 30


def e2():
    print("E2 (scipy) the estimate on a curved metric, for the perturbation of the background leaf; reconstruction")
    import numpy as np
    from scipy.integrate import quad
    Am = 1 + sp.Rational(3, 10) * z + sp.Rational(1, 5) * s
    Bm = 1 + sp.Rational(1, 10) * z**2 + sp.Rational(3, 20) * s
    Cm = sp.Rational(1, 5) + sp.Rational(1, 10) * z
    Dm = sp.Rational(1, 10) - sp.Rational(1, 20) * s
    ep = sp.Symbol('ep', positive=True)
    hh = ep**2 * sp.exp(-r**2 / ep**2)
    kr, kph, _ = leaf_quantities(Am, Bm, Cm, Dm, hh)
    kr, kph = kr.subs(z, hh), kph.subs(z, hh)
    kr0, kph0, _ = leaf_quantities(Am, Bm, Cm, Dm, sp.Integer(0))              # the background leaf z = 0
    kr0, kph0 = kr0.subs(z, 0), kph0.subs(z, 0)
    H2 = kr + kph
    sig = (kr - kph) / 2
    dH = H2 - (kr0 + kph0)
    dS = sig - (kr0 - kph0) / 2
    dK = kph - kph0
    L = lambda e: sp.lambdify((r, ep), e, 'numpy')                                # noqa: E731
    fdH, fdS, fdK = L(dH), L(dS), L(dK)
    fddH, fddS, fhp = L(sp.diff(dH, r)), L(sp.diff(dS, r)), L(sp.diff(hh, r))
    out = []
    for e in (0.2, 0.1, 0.05, 0.025):
        pts = [e / 2, e, 3 * e]
        w = lambda f: math.sqrt(quad(lambda q: q * f(q, e)**2, 1e-12, 0.5, points=pts, limit=400,   # noqa: E731
                                     epsabs=1e-14, epsrel=1e-10)[0])
        r0, r1, rk = w(fdS) / w(fdH), w(fddS) / w(fddH), w(fdK) / w(fhp)
        out.append((e, r0, r1, rk))
        print("   eps = %s: ||d sigma||/||d H2|| = %.6f, ||d_r d sigma||/||d_r d H2|| = %.6f; control ||d k_ph||/||h'|| "
              "= %.4f" % (e, r0, r1, rk))
    flat = abs(out[-1][1] - 0.5) < 0.05 and abs(out[-1][1] - 0.5) < abs(out[0][1] - 0.5)
    bounded = all(o[1] < 2 and o[2] < 2 for o in out) and abs(out[-1][2] / out[-2][2] - 1) < 0.03
    grows = all(out[i + 1][3] > 1.8 * out[i][3] for i in range(len(out) - 1))
    print("   bounded, the derivative ratio converged to 3 %%: %s; the ratio tends to the flat value 1/2: %s; control "
          "grows like 1/eps: %s" % (bounded, flat, grows))
    # reconstruction: integrate the leaf equation from the axis as an ODE for (h, h') with H2 given, eps = 0.1
    import numpy as np
    from scipy.integrate import solve_ivp
    W, P1, P0 = sp.symbols('W P1 P0')
    hq = sp.Function('hq')(r)
    krq, kphq, _ = leaf_quantities(Am, Bm, Cm, Dm, hq)
    Hq = (krq + kphq).subs(z, hq).doit()
    rep = lambda e: e.subs(sp.Derivative(hq, (r, 2)), W).subs(sp.Derivative(hq, r), P1).subs(hq, P0)  # noqa: E731
    Hw = rep(Hq)
    a_ = sp.diff(Hw, W)
    rest = Hw - a_ * W
    Kw = rep(kphq.subs(z, hq).doit())
    Hval = sp.Symbol('Hval')
    hpp_c = sp.lambdify((r, P0, P1, Hval), (Hval - rest) / a_, 'numpy')
    hpp_f = sp.lambdify((r, P0, P1, Hval), Hval - P1 / r, 'numpy')
    kph_n = sp.lambdify((r, P0, P1), Kw, 'numpy')
    e_ = 0.1
    fHn = sp.lambdify(r, H2.subs(ep, sp.Rational(1, 10)), 'numpy')
    fhn = sp.lambdify(r, hh.subs(ep, sp.Rational(1, 10)), 'numpy')
    fhpn = sp.lambdify(r, sp.diff(hh, r).subs(ep, sp.Rational(1, 10)), 'numpy')
    fSn = sp.lambdify(r, sig.subs(ep, sp.Rational(1, 10)), 'numpy')
    r_0, r_1 = 1e-6, 0.3
    qs = np.array([0.05, 0.1, 0.2, 0.3])
    errs = {}
    for name, rhs in (('curved', hpp_c), ('flat', hpp_f)):
        sol = solve_ivp(lambda q, y: [y[1], rhs(q, y[0], y[1], fHn(q))], (r_0, r_1), [fhn(r_0), 0.0],
                        method='DOP853', rtol=1e-13, atol=1e-16, dense_output=True)
        yy = sol.sol(qs)
        eh = float(np.max(np.abs(yy[1] - fhpn(qs))))
        es = float(np.max(np.abs(fHn(qs) / 2 - kph_n(qs, yy[0], yy[1]) - fSn(qs))))
        errs[name] = (eh, es)
    print("   reconstruction from the axis with H2 given: max error in h' %.2e, in sigma %.2e; flat equation "
          "(control): %.2e, %.2e" % (errs['curved'] + errs['flat']))
    rec = errs['curved'][0] < 1e-9 and errs['curved'][1] < 1e-8 and errs['flat'][0] > 1e-4
    # round 5 (the verifier of round 4, minor 6): the integration starts from axis regularity, h'(r0) = 0, not from the
    # exact leaf's slope; h(r0) is the leaf parameter (where the leaf meets the axis)
    return bounded and flat and grows and rec


if __name__ == '__main__':
    res = [e0(), e1(), e2()]
    print("PASS" if all(res) else "FAIL")
    sys.exit(0 if all(res) else 1)
