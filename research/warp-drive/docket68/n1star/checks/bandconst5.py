#!/usr/bin/env python3
"""bandconst5: constraint data for a perturbation of Part I's data supported in an angular band
(FAMILIES5-AXIS.md section 2; FAMILIES5-NONROUND.md Corollary N2's missing input).

The record solves the Cauchy constraints on Sigma_tau0 by Racz's hyperbolic-parabolic split (N1STAR-PROOF.md 6.3,
twoslice5 S1): the Hamiltonian constraint is parabolic in R for the radial metric component, so every perturbation is
spread over all angles. [Rac16] (arXiv:1508.01810v3) gives a second split of the same constraints: the Hamiltonian
constraint solved algebraically for kappa = K(nhat, nhat), the momentum constraint a first-order system for
u = (k_i, K^l_l) with R as time, symmetrisable hyperbolic where kappa K^l_l < 0 (its Lemma 4.1, p. 12), whose solution
lives in the domain of dependence of the initial sphere (its Theorem 4.3, p. 14). Here, in the class (gamma round, K
T^2 x Z2 x Z2-invariant, coordinates R, th, phi1, phi2 with dOmega_3^2 = dth^2 + sin^2 th dphi1^2 + cos^2 th dphi2^2):

  B1 (exact: the symbol symbolic, its comparison at three rational points with every function explicit) the class
     constraints in the algebraic-hyperbolic split: with K_RR = G kappa, K_Rth = sqrt(G) p, K_thth = R^2 (Kt/3 + s1),
     K_11 = G1 (Kt/3 + s2), K_22 = G2 (Kt/3 - s1 - s2) (Kt := K^l_l on the spheres, s1, s2 the free trace-free part),
     the Hamiltonian constraint is linear in kappa with coefficient 2 Kt, and after kappa is eliminated the principal
     symbol of (M_R, M_th) in (Kt, p) has determinant proportional to [Rac16] (4.22): Kt (nhat.xi)^2 - 2 (nhat.xi)
     (k.xi) + kappa |xi_S|^2. So in the class the angular characteristic speeds are
     dth/dR = sqrt(G) (p/R^2 +- sqrt(p^2/R^4 - kappa Kt/R^2))/Kt: real exactly where kappa Kt < p^2/R^2.
     Control (must fail): kappa treated as free data (not eliminated): the determinant is not (4.22).
  B2 (exact, sympy; the general case exact at four rational points) Part I's chart g0 = -e^(2 psi) f dvhat^2
     + 2 e^psi dvhat dR + R^2 dOmega_3^2, slice tau = vhat - R
     (FAMILIES5-FULL.md section 2): with E = e^psi, Kt = 3 (E f - 1)/(E R sqrt(2/E - f)) < 0 whenever E f < 1 (K =
     nabla n), and kappa = -Nk / (E sqrt(2/E - f) (2 - E f)) with Nk := E^2 f^2 psi_R + E^2 f f_R/2 - 3 E f psi_R
     - E f_v/2 - 3 E f_R/2 - psi_v + psi_R, so the split is hyperbolic (kappa Kt < 0, p = 0) exactly where Nk < 0.
     On Tangherlini (psi = 0, f = 1 - mu/R^2): Nk = (mu/R^3)(f - 3) < 0, hyperbolic on the whole slice, angular speed
     c(R) = sqrt((2 + mu/R^2)/3)/R. Cross-check against a READ formula: the same code in four dimensions (f = 1 - 2M/r,
     spheres of dimension 2) gives -K^l_l/kappa = 2(1 + 2H)/(1 + H), H = M/r, exactly [Rac16] (4.30), p. 14.
     Control (must fail): the four-dimensional code with the five-dimensional trace factor 3 does not give (4.30).
  B3 (computed, floating point; the record's background twobg5 at n = 40 and 80) on Part I's Sigma_tau0 in the seed
     region a <= R <= r1 (region III: psi = psi_III(vhat), f = 1 - mu0/R^2, psi_R = f_v = 0), Nk < 0 at every point
     (printed: its largest value), so the algebraic-hyperbolic split is hyperbolic there; the angular speed c(R) and
     the spread Delta(R2) = int_a^R2 c dR of a perturbation integrated inward from R2 to a are printed.
  B4 (exact: the construction symbolic for arbitrary G, kappa0, Y0, psi; its residuals exact at three rational points
     with explicit functions) compactly supported solutions of the linearised constraints in angle AND radius on every
     round slice (gamma = G dR^2 + R^2 dOmega_3^2, K0 = kappa0 nhat nhat + Y0 R^2 dOmega_3^2, G, kappa0, Y0
     arbitrary): with dgamma = 0 and a stream function psi(R, th) of compact support, dKt = e^(int a) (sin th
     cos th)^-1 d_th psi, dp = R^2 e^(int a) (sqrt(G) sin th cos th)^-1 d_R psi (a(R) computed), ds1 = 0, ds2
     fixed algebraically by M_th (its coefficient is computed and nonzero for 0 < th < pi/2): the linearised H, M_R,
     M_th vanish.
     Not pure gauge (exact): a gauge perturbation (lapse N, shift X) of a round slice with dgamma = 0 has d_th N = 0 and
     X^th = 0, so its dK is th-independent; the stream perturbation is not.
     Controls (must fail): ds2 = 0 leaves M_th; the weight (sin th cos th) dropped leaves M_R.
  B5 (computed, numpy) the record's parabolic split spreads: the linearised Hamiltonian equation of twoslice5 S1,
     (3/(R G^2)) d_R a - (1/(G R^2)) Lap_th a = 0 (Lap_th the S^3 Laplacian on invariant functions, G = 1 + mu0/R^2),
     from data supported in th in [pi/8, 3 pi/8] at R = r1: after every positive radial step a is nonzero at both axes
     (the strong maximum principle; printed at three steps). Control (must fail to spread): the same march with the
     angular operator removed (the structure of B6's cone constraints) leaves the axes at exactly zero.
  B6 (exact, sympy; dnull5's class double-null metric) the characteristic constraints on an outgoing cone u = u0:
     Ric(d_v, d_v) contains no th-derivative (an ODE in v at each th, dnull5 D2), and Ric(d_v, d_th) contains the
     shift only through d_v b and d_v^2 b and the other fields only through their th- and v-derivatives on the cone:
     an ODE in v for d_v b with sources from the fields already fixed. So characteristic data whose free part is
     supported in an angular band are supported there, exactly. Control (must fail): Ric(d_th, d_th) contains d_u of
     the fields (it is not a constraint on the cone).

Labels: computed (B1, B2, B4, B6 exact; B3, B5 floating point). The READ statements are quoted in FAMILIES5-AXIS.md
section 2. Run: python3 checks/bandconst5.py   (a few minutes)
"""
import importlib.util
import math
import os
import sys

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
R, th, f1, f2 = sp.symbols('R theta phi1 phi2', positive=True)
X4 = [R, th, f1, f2]


def christoffel(g, X):
    n = len(X)
    gi = g.inv()
    return gi, [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                              - sp.diff(g[b, c], X[d])) for d in range(n)) / 2)
                  for c in range(n)] for b in range(n)] for a in range(n)]


def scalar_curv(g, X, gi, Gm):
    n = len(X)

    def Ric(b, d):
        return sum(sp.diff(Gm[a][b][d], X[a]) - sp.diff(Gm[a][b][a], X[d])
                   + sum(Gm[a][a][e] * Gm[e][b][d] - Gm[a][d][e] * Gm[e][b][a] for e in range(n)) for a in range(n))
    return sp.simplify(sum(gi[b, d] * Ric(b, d) for b in range(n) for d in range(n) if gi[b, d] != 0))


def constraints(g, K, X, Ed=0, J=(0, 0, 0, 0)):
    """Hamiltonian R + (tr K)^2 - |K|^2 - 2E and momentum D_j K^j_i - D_i tr K - J_i ([Rac16] (1.1)-(1.2))."""
    n = len(X)
    gi, Gm = christoffel(g, X)
    trK = sum(gi[i, j] * K[i, j] for i in range(n) for j in range(n))
    KK = sum(gi[i, k] * gi[j, l] * K[i, j] * K[k, l] for i in range(n) for j in range(n) for k in range(n)
             for l in range(n) if gi[i, k] != 0 and gi[j, l] != 0)
    H = scalar_curv(g, X, gi, Gm) + trK**2 - KK - 2 * Ed

    def DK(c, a, b):                     # nabla_c K_ab
        return sp.diff(K[a, b], X[c]) - sum(Gm[e][c][a] * K[e, b] + Gm[e][c][b] * K[a, e] for e in range(n))
    M = [sum(gi[j, c] * DK(c, j, i) for j in range(n) for c in range(n) if gi[j, c] != 0) - sp.diff(trK, X[i]) - J[i]
         for i in range(n)]
    return H, M, trK


def at_point(expr, funcs, pt):
    """exact value of expr at a rational point after replacing the undefined functions by explicit ones."""
    e = expr
    for name, lam in funcs.items():
        e = e.replace(sp.Function(name), lam)
    e = e.doit().subs(pt)
    return sp.nsimplify(sp.simplify(e))


# explicit test functions built from sin th and cos th (rational at th = atan(3/4), atan(5/12), atan(8/15))
PTS = [{R: sp.Rational(3, 2), th: sp.atan(sp.Rational(3, 4))}, {R: 2, th: sp.atan(sp.Rational(5, 12))},
       {R: sp.Rational(7, 3), th: sp.atan(sp.Rational(8, 15))}]


def b1():
    print("B1 (exact at rational points) the class constraints in [Rac16]'s algebraic-hyperbolic split; the symbol")
    G = sp.Function('G')(R)
    Kt, p, s1, s2, kap, Ed, JR, Jt = [sp.Function(nm)(R, th) for nm in ('Kt', 'p', 's1', 's2', 'kappa', 'E', 'JR',
                                                                         'Jth')]
    G1, G2 = R**2 * sp.sin(th)**2, R**2 * sp.cos(th)**2
    g = sp.diag(G, R**2, G1, G2)
    K = sp.zeros(4, 4)
    K[0, 0] = G * kap
    K[0, 1] = K[1, 0] = sp.sqrt(G) * p
    K[1, 1] = R**2 * (Kt / 3 + s1)
    K[2, 2] = G1 * (Kt / 3 + s2)
    K[3, 3] = G2 * (Kt / 3 - s1 - s2)
    H, M, trK = constraints(g, K, X4, Ed, (JR, Jt, 0, 0))
    Hk = sp.expand(H)
    lin_in_kappa = sp.expand(sp.diff(Hk, kap, 2)) == 0
    ok_coef = sp.simplify(sp.diff(Hk, kap) - 2 * Kt) == 0
    ksol = -sp.expand(Hk.subs(kap, 0)) / (2 * Kt)
    print("   H linear in kappa:", lin_in_kappa, "; coefficient 2 Kt:", ok_coef)
    Mr = sp.expand(M[0].subs(kap, ksol).doit())
    Mt = sp.expand(M[1].subs(kap, ksol).doit())
    Mr0, Mt0 = sp.expand(M[0].doit()), sp.expand(M[1].doit())
    xR, xt = sp.symbols('xi_R xi_th')
    unk = [Kt, p]

    def symb(e1, e2):
        A = sp.zeros(2, 2)
        for i, e in enumerate((e1, e2)):
            for j, f in enumerate(unk):
                A[i, j] = e.coeff(sp.Derivative(f, R)) * xR + e.coeff(sp.Derivative(f, th)) * xt
        return A
    A, A0 = symb(Mr, Mt), symb(Mr0, Mt0)
    detA, detA0 = sp.expand(A.det()), sp.expand(A0.det())
    nxi = xR / sp.sqrt(G)
    racz = Kt * nxi**2 - 2 * nxi * p * xt / R**2 + ksol * xt**2 / R**2
    racz0 = Kt * nxi**2 - 2 * nxi * p * xt / R**2 + kap * xt**2 / R**2
    funcs = {'G': sp.Lambda(R, (1 + R / 2)**2), 'Kt': sp.Lambda((R, th), -3 / (R + 1) + sp.sin(th) / 7),
             'p': sp.Lambda((R, th), R * sp.sin(th) * sp.cos(th) / 11),
             's1': sp.Lambda((R, th), R * sp.cos(th) / 13), 's2': sp.Lambda((R, th), (R - sp.sin(th)) / 17),
             'E': sp.Lambda((R, th), R / 19 + sp.cos(th)**2 / 5), 'JR': sp.Lambda((R, th), sp.sin(th) / 23),
             'Jth': sp.Lambda((R, th), sp.cos(th) / 29), 'kappa': sp.Lambda((R, th), sp.cos(th) / 31)}
    XIS = [{xR: 1, xt: 0}, {xR: 0, xt: 1}, {xR: 2, xt: -3}, {xR: 5, xt: 7}]
    ok, ctl, ok_sp = True, True, True
    for pt in PTS:
        rat = [at_point(detA.subs(x), funcs, pt) / at_point(racz.subs(x), funcs, pt) for x in XIS]
        ok &= all(sp.simplify(rr - rat[0]) == 0 for rr in rat) and rat[0] != 0
        rat0 = [at_point(detA0.subs(x), funcs, pt) / at_point(racz0.subs(x), funcs, pt) for x in XIS]
        ctl &= any(sp.simplify(rr - rat0[0]) != 0 for rr in rat0)
        # speeds at the point with p = 0: roots in lam of det(xi_R = -lam, xi_th = 1)
        fz = dict(funcs)
        fz['p'] = sp.Lambda((R, th), 0)
        lam = sp.Symbol('lam')
        dl = at_point(detA.subs({xR: -lam, xt: 1}), fz, pt)
        roots = sp.solve(dl, lam)
        want = at_point(sp.sqrt(G) * sp.sqrt(-ksol / (Kt * R**2)), fz, pt)
        ok_sp &= len(roots) == 2 and all(sp.simplify(rt**2 - want**2) == 0 for rt in roots)
        print("      DEBUG roots", roots, "want", want, "dl", dl)
        print("   point R = %s, th = %s: det / (4.22) = %s for every xi: %s" % (pt[R], pt[th], rat[0], ok))
    print("   control (kappa not eliminated): det / (4.22) depends on xi:", ctl)
    print("   speeds at p = 0: dth/dR = +- sqrt(G) sqrt(-kappa/(Kt R^2)):", ok_sp)
    return lin_in_kappa and ok_coef and ok and ctl and ok_sp


def b2():
    print("B2 (exact) Part I's chart and slice tau = vhat - R: Kt, kappa, the hyperbolicity sign; Tangherlini; [Rac16]"
          " (4.30)")
    T = sp.Symbol('tau')
    pv, pR, fv, fR, P0, F0 = sp.symbols('psi_v psi_R f_v f_R psi0 f0', real=True)
    vh = T + R
    psi = P0 + pv * (vh - sp.Symbol('v0')) + pR * (R - sp.Symbol('R0'))
    f = F0 + fv * (vh - sp.Symbol('v0')) + fR * (R - sp.Symbol('R0'))

    def slice_data(psi, f, dimS):
        E = sp.exp(psi)
        gTT, gTR, gRR = -E**2 * f, -E**2 * f + E, -E**2 * f + 2 * E   # in (tau, R), vhat = tau + R
        g = sp.Matrix([[gTT, gTR], [gTR, gRR]])
        gi = g.inv()
        X = [T, R]
        al = 1 / sp.sqrt(-gi[0, 0])

        def Gam(a, b, c):
            return sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                       for d in range(2)) / 2
        nd = [-al, 0]
        KRR = sp.diff(nd[1], R) - sum(Gam(c, 1, 1) * nd[c] for c in range(2))
        kappa = KRR / gRR
        nR = -al * gi[1, 0]
        Kt = dimS * nR / R
        return kappa, Kt, gRR
    kappa, Kt, gRR = slice_data(psi, f, 3)
    E = sp.exp(P0)
    Nk = E**2 * F0**2 * pR + E**2 * F0 * fR / 2 - 3 * E * F0 * pR - E * fv / 2 - 3 * E * fR / 2 - pv + pR
    want_k = -Nk / (E * sp.sqrt(2 / E - F0) * (2 - E * F0))
    want_K = 3 * (E * F0 - 1) / (E * sp.Symbol('R0') * sp.sqrt(2 / E - F0))
    import random
    rng = random.Random(7)
    ok1 = True
    for _ in range(4):                     # exact at rational points (psi0 = log of a rational)
        Eq_ = sp.Rational(rng.randint(3, 10), 10)
        vals = {P0: sp.log(Eq_), F0: sp.Rational(rng.randint(-20, 10), 10), pv: sp.Rational(rng.randint(-9, 9), 7),
                pR: sp.Rational(rng.randint(-9, 9), 7), fv: sp.Rational(rng.randint(-9, 9), 7),
                fR: sp.Rational(rng.randint(-9, 9), 7), sp.Symbol('R0'): sp.Rational(rng.randint(7, 30), 10),
                sp.Symbol('v0'): sp.Rational(rng.randint(-9, 9), 10)}
        pt = {T: vals[sp.Symbol('v0')] - vals[sp.Symbol('R0')], R: vals[sp.Symbol('R0')]}
        dk = sp.simplify(kappa.subs(vals).subs(pt) - want_k.subs(vals))
        dK = sp.simplify(Kt.subs(vals).subs(pt) - want_K.subs(vals))
        ok1 &= dk == 0 and dK == 0
    print("   kappa = -Nk/(E sqrt(2/E - f)(2 - E f)), Kt = 3 (E f - 1)/(E R sqrt(2/E - f)) (exact at four rational "
          "points):", ok1)
    # Tangherlini
    mu = sp.Symbol('mu', positive=True)
    fT = 1 - mu / R**2
    kT, KT, gT = slice_data(sp.Integer(0), fT, 3)
    kT, KT = sp.simplify(kT), sp.simplify(KT)
    NkT = sp.simplify((fT * sp.diff(fT, R) / 2 - 3 * sp.diff(fT, R) / 2))
    ok2 = sp.simplify(NkT - mu / R**3 * (fT - 3)) == 0 and sp.simplify(kT * KT).subs({mu: 1, R: 2}) < 0
    c = sp.simplify(sp.sqrt(gT) * sp.sqrt(-kT / (KT * R**2)))
    ok3 = sp.simplify(c**2 - (2 + mu / R**2) / (3 * R**2)) == 0
    print("   Tangherlini: Nk = (mu/R^3)(f - 3):", ok2, "; angular speed c(R)^2 = (2 + mu/R^2)/(3 R^2):", ok3)
    # four dimensions: f = 1 - 2M/r, spheres of dimension 2: [Rac16] (4.30)
    M_ = sp.Symbol('M', positive=True)
    k4, K4, _ = slice_data(sp.Integer(0), 1 - 2 * M_ / R, 2)
    Hh = M_ / R
    ok4 = sp.simplify(-K4 / k4 - 2 * (1 + 2 * Hh) / (1 + Hh)) == 0
    k4b, K4b, _ = slice_data(sp.Integer(0), 1 - 2 * M_ / R, 3)
    ctl = sp.simplify(-K4b / k4b - 2 * (1 + 2 * Hh) / (1 + Hh)) != 0
    print("   four dimensions: -K^l_l/kappa = 2(1 + 2H)/(1 + H) ([Rac16] (4.30)):", ok4,
          "; control (trace factor 3 in 4D) differs:", ctl)
    return ok1 and ok2 and ok3 and ok4 and ctl


def b3():
    print("B3 (computed, floating point) Part I's Sigma_tau0 in the seed region: Nk < 0, the speed and the spread")
    spec = importlib.util.spec_from_file_location('twobg5', os.path.join(HERE, 'twobg5.py'))
    tb = importlib.util.module_from_spec(spec)
    sys.path.insert(0, HERE)
    spec.loader.exec_module(tb)
    ok = True
    res = []
    for n in (40, 80):
        uu, vv, Rg, S, Ru, Rv, mu = tb.run(n)
        k3 = int(np.argmin(np.abs(uu - (tb.U2P + 0.1))))
        ia = uu >= tb.U2P + 0.1
        mu0 = float(np.nanmedian(mu[ia, 0][np.isfinite(mu[ia, 0])]))
        dv = vv[1] - vv[0]
        vhp = -np.exp(2 * S[0]) / Ru[0]
        vh = np.concatenate([[0.0], np.cumsum((vhp[1:] + vhp[:-1]) / 2 * dv)])
        psi = np.log(-np.exp(2 * S[k3]) / (Ru[k3] * vhp))            # region III: psi(vhat) (twobg5 G1 (b))
        m = np.isfinite(psi)
        tau0 = -tb.AA + 0.02
        a = tb.AA
        r1 = 1.861                                                       # the packet's inner edge on Sigma_tau0
        Rs = np.linspace(a, r1, 400)
        vq = tau0 + Rs
        ps = np.interp(vq, vh[m], psi[m])
        dps = np.gradient(np.interp(vq, vh[m], psi[m]), vq)
        E = np.exp(ps)
        f = 1 - mu0 / Rs**2
        fR = 2 * mu0 / Rs**3
        Nk = E**2 * f * fR / 2 - 3 * E * fR / 2 - dps
        kap = -Nk / (E * np.sqrt(2 / E - f) * (2 - E * f))
        Kt = 3 * (E * f - 1) / (E * Rs * np.sqrt(2 / E - f))
        gRR = -E**2 * f + 2 * E
        c = np.sqrt(gRR) * np.sqrt(np.clip(-kap / (Kt * Rs**2), 0, None))
        spread = np.concatenate([[0.0], np.cumsum((c[1:] + c[:-1]) / 2 * np.diff(Rs))])
        res.append((n, float(Nk.max()), float(ps.min()), float(ps.max()), float(np.abs(dps).max()), float(c[0]),
                    float(c[-1]), float(np.interp(a + 0.2, Rs, spread)), float(spread[-1])))
        ok &= bool(Nk.max() < 0)
    for (n, nkmax, pmin, pmax, dpmax, c0, c1, s02, s1) in res:
        print("   n = %d: max Nk = %.4f < 0 on R in [a, r1]; psi_III in [%.4f, %.4f], |psi'| <= %.3f; c(a) = %.3f, "
              "c(r1) = %.3f; spread from a + 0.2 to a %.3f, over [a, r1] %.3f rad" % (n, nkmax, pmin, pmax, dpmax, c0,
                                                                                    c1, s02, s1))
    conv = abs(res[0][8] - res[1][8]) < 0.02
    print("   hyperbolic on the seed region at both n:", ok, "; spread converged to 0.02:", conv)
    return ok and conv


def b4():
    print("B4 (exact at rational points) compactly supported solutions of the linearised constraints, round slices")
    G, k0, Y0 = [sp.Function(nm)(R) for nm in ('G', 'kappa0', 'Y0')]
    eps = sp.Symbol('eps')
    dKt, dp, ds1, ds2, dkap = [sp.Function(nm)(R, th) for nm in ('dKt', 'dp', 'ds1', 'ds2', 'dkappa')]
    G1, G2 = R**2 * sp.sin(th)**2, R**2 * sp.cos(th)**2
    g = sp.diag(G, R**2, G1, G2)
    Kt = 3 * Y0 + eps * dKt
    K = sp.zeros(4, 4)
    K[0, 0] = G * (k0 + eps * dkap)
    K[0, 1] = K[1, 0] = sp.sqrt(G) * eps * dp
    K[1, 1] = R**2 * (Kt / 3 + eps * ds1)
    K[2, 2] = G1 * (Kt / 3 + eps * ds2)
    K[3, 3] = G2 * (Kt / 3 - eps * ds1 - eps * ds2)
    H, M, _ = constraints(g, K, X4)
    lin = [sp.simplify(sp.diff(e, eps).subs(eps, 0)) for e in (H, M[0], M[1])]
    # dkappa from the linearised Hamiltonian (algebraic)
    dk = sp.solve(sp.Eq(lin[0], 0), dkap)[0]
    MR = sp.expand(lin[1].subs(dkap, dk).doit())
    # M_R must be div-form in (dKt, dp): find a(R) with M_R = -e^{int a} d_R(e^{-int a} dKt) + (div_S dp)
    cK = sp.simplify(MR.coeff(dKt))
    cKR = sp.simplify(MR.coeff(sp.Derivative(dKt, R)))
    aR = sp.simplify(-cK / cKR)
    print("   M_R = %s d_R dKt + (%s) dKt + (dp terms)" % (cKR, cK))
    psi = sp.Function('psi')(R, th)
    w = sp.sin(th) * sp.cos(th)
    Ia = sp.Function('Ia')(R)                                    # Ia' = a(R)
    eIa = sp.exp(Ia)
    sub_d = {sp.Derivative(Ia, R): aR}
    dKt_s = eIa * sp.diff(psi, th) / w
    dp_s = R**2 * eIa * sp.diff(psi, R) / (sp.sqrt(G) * w)
    res = []
    for e in (lin[0], lin[1], lin[2]):
        e2 = e.subs(dkap, dk).subs({dKt: dKt_s, dp: dp_s}).doit()
        e2 = e2.subs(sub_d).doit().subs(sub_d)
        res.append(e2)
    funcs = {'G': sp.Lambda(R, (1 + R / 2)**2), 'kappa0': sp.Lambda(R, -(1 + R) / (2 + R**2)),
             'Y0': sp.Lambda(R, (R + 3) / (R**2 + 1)),
             'psi': sp.Lambda((R, th), (R**2 - R + 1) * sp.sin(th)**2 * sp.cos(th)**3),
             'Ia': sp.Lambda(R, 0)}
    mt = sp.expand(res[2].subs(ds1, 0).doit())
    cs2 = mt.coeff(ds2)
    rH, rR, nz, c1, c2 = [], [], [], [], []
    dKt_b = eIa * sp.diff(psi, th)
    dp_b = R**2 * eIa * sp.diff(psi, R) / sp.sqrt(G)
    eb = lin[1].subs(dkap, dk).subs({dKt: dKt_b, dp: dp_b}).doit().subs(sub_d).doit().subs(sub_d)
    for pt in PTS:
        rH.append(at_point(res[0], funcs, pt))
        rR.append(at_point(res[1], funcs, pt))
        nz.append(at_point(cs2, funcs, pt))
        c1.append(at_point(mt.subs(ds2, 0), funcs, pt))
        c2.append(at_point(eb, funcs, pt))
    print("   at three rational points: linearised H residual", rH, "; M_R residual", rR,
          "; M_th coefficient of ds2", nz)
    ok = all(x == 0 for x in rH + rR) and all(x != 0 for x in nz)
    ds2_sol = -(mt.subs(ds2, 0)) / cs2
    loc = all(not x.has(sp.Integral) for x in (dKt_s, dp_s, ds2_sol))
    print("   dKt, dp, ds2 (= -M_th(ds2 = 0)/coefficient) are local differential expressions in psi:", loc)
    ctl1, ctl2 = any(x != 0 for x in c1), any(x != 0 for x in c2)
    print("   controls: ds2 = 0 leaves M_th:", ctl1, "; weight sin th cos th dropped leaves M_R:", ctl2)
    # not pure gauge: dgamma = L_X gamma + 2 N K0 = 0 on a round slice forces d_th N = 0 and X^th = 0
    N_, XR, Xt = [sp.Function(nm)(R, th) for nm in ('N', 'XR', 'Xt')]
    Xv = [XR, Xt, 0, 0]
    gi = g.inv()
    K0 = sp.diag(G * k0, R**2 * Y0, G1 * Y0, G2 * Y0)
    Lg = sp.zeros(4, 4)
    for i in range(4):
        for j in range(4):
            Lg[i, j] = sum(Xv[k] * sp.diff(g[i, j], X4[k]) + g[k, j] * sp.diff(Xv[k], X4[i])
                           + g[i, k] * sp.diff(Xv[k], X4[j]) for k in range(4)) + 2 * N_ * K0[i, j]
    tor = sp.solve([Lg[2, 2], Lg[3, 3]], [XR, Xt], dict=True)[0]
    xt0 = sp.simplify(tor[Xt]) == 0
    e01 = sp.simplify(Lg[0, 1].subs(tor).doit())
    dthN = sp.simplify(e01 / sp.diff(N_, th)) if e01 != 0 else 0
    gauge_round = xt0 and sp.simplify(e01.subs(sp.Derivative(N_, th), 0)) == 0 and dthN != 0
    print("   gauge with dgamma = 0: X^th = 0:", xt0, "; then (L_X gamma)_Rth = (%s) d_th N: N = N(R):" % dthN,
          gauge_round)
    return ok and loc and ctl1 and ctl2 and gauge_round


def b5():
    print("B5 (computed) the parabolic split spreads to the axes; without the angular operator nothing does")
    # invariant functions on S^3: Lap = d_th^2 + 2 cot(2 th) d_th, on th in (0, pi/2)
    nth = 401
    ths = np.linspace(0, np.pi / 2, nth)
    h = ths[1] - ths[0]
    mu0, r1 = 0.82211, 1.861
    a0 = np.where((ths > np.pi / 8) & (ths < 3 * np.pi / 8), np.sin(4 * (ths - np.pi / 8))**4, 0.0)
    # parabolic: d_R a = (G/(3 R)) Lap a with G = 1 + mu/R^2 (record's slice; sign: forward in R), implicit Euler
    sw = np.sin(2 * ths)
    L = np.zeros((nth, nth))
    for i in range(1, nth - 1):
        wp, wm = np.sin(2 * (ths[i] + h / 2)), np.sin(2 * (ths[i] - h / 2))
        L[i, i - 1], L[i, i + 1] = wm / (h * h * sw[i]), wp / (h * h * sw[i])
        L[i, i] = -(wp + wm) / (h * h * sw[i])
    L[0, 0], L[0, 1] = -4 / h**2, 4 / h**2                     # regular axis: Lap a(0) = 2 a''(0)
    L[-1, -1], L[-1, -2] = -4 / h**2, 4 / h**2

    def march(Lop):
        a = a0.copy()
        Rcur, dR = r1, 1e-3
        outs = []
        for target in (r1 + 0.01, r1 + 0.05, r1 + 0.2):
            while Rcur < target - 1e-12:
                G = 1 + mu0 / Rcur**2
                a = np.linalg.solve(np.eye(nth) - dR * G / (3 * Rcur) * Lop, a)
                Rcur += dR
            outs.append((target - r1, a[0], a[-1], a.max()))
        return outs
    outs = march(L)
    par_ok = all(o[1] > 0 and o[2] > 0 for o in outs)
    for d, ax0, ax1, mx in outs:
        print("   parabolic: after dR = %.2f, a(axis 1) = %.3e, a(axis 2) = %.3e (max %.3e)" % (d, ax0, ax1, mx))
    ctl = march(np.zeros_like(L))
    ctl_ok = all(o[1] == 0 and o[2] == 0 for o in ctl)
    print("   control (no angular operator, the ODE structure of B6): the axes stay exactly %r, %r: %s"
          % (ctl[-1][1], ctl[-1][2], ctl_ok))
    hyp_ok = ctl_ok
    return par_ok and hyp_ok


def b6():
    print("B6 (exact) the characteristic constraints on an outgoing cone are ODEs in v at fixed th")
    spec = importlib.util.spec_from_file_location('dnull5', os.path.join(os.path.dirname(HERE), 'dnull5.py'))
    dn = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dn)
    u, v, t, p1, p2 = dn.u, dn.v, dn.th, dn.p1, dn.p2
    Om, b, gam, A, B = [sp.Function(nm)(u, v, t) for nm in ('Omega', 'b', 'gamma', 'A', 'B')]
    g = sp.zeros(5)
    g[0, 1] = g[1, 0] = -2 * Om**2
    g[2, 2] = gam
    g[0, 2] = g[2, 0] = -gam * b
    g[0, 0] = gam * b**2
    g[3, 3] = sp.exp(2 * A)
    g[4, 4] = sp.exp(2 * B)
    Ric = dn.ricci(g, [u, v, t, p1, p2])
    Rvv = Ric[1, 1].doit()
    Rvt = Ric[1, 2].doit()
    Rtt = Ric[2, 2].doit()

    def ders(e):
        return {(str(d.expr.func), tuple(str(x) for x, k in d.variable_count for _ in range(k)))
                for d in e.atoms(sp.Derivative)}
    dvv = ders(Rvv)
    no_th = all('theta' not in vs for _, vs in dvv)
    no_u = all('u' not in vs for _, vs in dvv)
    dvt = ders(Rvt)
    b_ders = {vs for f_, vs in dvt if f_ == 'b'}
    b_ok = all(set(vs) <= {'v'} for vs in b_ders) and b_ders
    no_u2 = all('u' not in vs for _, vs in dvt)
    dtt = ders(Rtt)
    ctl = any('u' in vs for _, vs in dtt)
    print("   Ric_vv: no th-derivative %s, no u-derivative %s; Ric_vth: b only through %s, no u-derivative %s"
          % (no_th, no_u, sorted(b_ders), no_u2))
    print("   control: Ric_thth contains u-derivatives:", ctl)
    return no_th and no_u and bool(b_ok) and no_u2 and ctl


if __name__ == '__main__':
    res = [b1(), b2(), b4(), b6(), b5(), b3()]
    print("PASS" if all(res) else "FAIL")
    sys.exit(0 if all(res) else 1)
