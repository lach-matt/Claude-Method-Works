#!/usr/bin/env python3
"""racslice5: band-localised constraint data across the shell's non-hyperbolic band, posed on a deformed slice
(FAMILIES5-R6.md section 2).

racglobal5 R1-R2: on Part I's Sigma_tau0 Racz's algebraic-hyperbolic split is hyperbolic (kappa K^l_l < 0) except on
a band R in [4.29, 4.53] inside the shell ([R7] the interpolated edges 4.2914, 4.5284), where K is negative
definite, so no foliation OF THAT SLICE is hyperbolic.
The obstruction is a property of the slice, not of the spacetime: here a different spacelike slice through the band,
equal to Sigma_tau0 outside a compact radial interval, is hyperbolic everywhere.

  S1 (exact, sympy) for every round slice vhat = V(R) of Part I's chart g0 = -e^(2 psi) f dvhat^2 + 2 e^psi dvhat dR +
     R^2 dOmega_3^2 (psi, f arbitrary functions of (vhat, R)), the radial extrinsic curvature kappa' = K(T, T)/g(T, T),
     T = V' d_vhat + d_R, and the sphere trace K'^l_l = 3 n^R/R are explicit in (E, f, psi_R, psi_vhat, f_R, f_vhat,
     V', V''); at V' = 1, V'' = 0 they are bandconst5 B2's kappa = -Nk/(E sqrt(2/E - f)(2 - E f)) and Kt = 3 (E f -
     1)/(E R sqrt(2/E - f)); and d kappa'/d V'' = 1/(E V' sqrt(V'(2 - E V' f)/E)(2 - E V' f)) > 0 on every spacelike
     round slice (V' > 0, E V' f < 2): a convex bend (V'' > 0) raises kappa' [R7: the bend used below has phi <= 0, so
     Sigma' lies to the past of Sigma_tau0 where they differ]. Control (must fail): the
     same formula with the Christoffel term dropped does not reduce to B2.
  S2 (computed, floating point; twobg5's background at n = 80 and 160) the slice Sigma' = {vhat - R - phi(R) = tau0},
     phi'' = A (b(R; 4.1, 4.7) - l1 b(R; 3.0, 4.0) - l2 b(R; 4.85, 5.75)) (b the C-infinity bump, A = 0.01, l1, l2 fixed
     by the zeroth and first moments so that phi and phi' vanish outside [3.0, 5.75]): Sigma' equals Sigma_tau0 outside
     R in [3.0, 5.75], is spacelike (0 < V' and E V' f < 2 at every slice point, the margins printed), and kappa' K'^l_l
     < 0 at every slice point of Sigma' in Omega_2 (R from a to the grid's edge): Racz's split is hyperbolic on the
     whole of Sigma'. Converged (max kappa' K'^l_l to 5 % between n = 80 and 160). [R7: sampled at the grid crossings;
     certified between them, for the linear interpolant of the crossing data, in intcert5 C2.] Controls (must fail):
     A = 0 (Sigma_tau0 itself) has kappa' K'^l_l > 0 on the band (racglobal5 R1); A -> -A (bent the other way) widens it.
  S3 (computed) the lens between Sigma' and Sigma_tau0 lies in {R in [3.0, 5.75]} with time thickness max |phi| in tau,
     so the domain of influence of a perturbation's support, carried from Sigma' to Sigma_tau0, widens its angular
     support by at most max |phi|/R_min (R |dOmega/dtau| <= 1, augment5 S7): printed. The lens is inside the computed
     domain (every slice point of Sigma' is a grid crossing).

Labels: computed (S1 exact; S2, S3 floating point). Run: python3 checks/racslice5.py   (a few minutes)
"""
import importlib.util
import math
import os
import sys

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
A_DEF = 0.01
P_IV, L_IV, R_IV = (4.1, 4.7), (3.0, 4.0), (4.85, 5.75)


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + '.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


SYMS = sp.symbols('E f psi_R psi_v f_R f_v V1 V2 R', real=True)


def slice_formulas(drop_christoffel=False):
    v, R = sp.symbols('vhat R', real=True)
    V1, V2 = sp.symbols('V1 V2', real=True)
    psi = sp.Function('psi')(v, R)
    f = sp.Function('f')(v, R)
    E = sp.exp(psi)
    h = sp.Matrix([[-E**2 * f, E], [E, 0]])
    hi = h.inv()
    X = [v, R]
    Gam = [[[sum(hi[a, d] * (sp.diff(h[d, b], X[c]) + sp.diff(h[d, c], X[b]) - sp.diff(h[b, c], X[d]))
                 for d in range(2)) / 2 for c in range(2)] for b in range(2)] for a in range(2)]
    T = sp.Matrix([V1, 1])
    dS = sp.Matrix([1, -V1])
    n_low = -dS / sp.sqrt(-(dS.T * hi * dS)[0])
    cf = 0 if drop_christoffel else 1
    acc = sp.Matrix([(V2 if c == 0 else 0) + cf * sum(Gam[c][a][b] * T[a] * T[b] for a in range(2) for b in range(2))
                     for c in range(2)])
    kap = -(n_low.T * acc)[0] / (T.T * h * T)[0]
    Kll = 3 * (hi * n_low)[1] / R
    Es, F0, pR, pv, fR, fv = SYMS[:6]

    def tosym(e):
        e = e.subs({sp.Derivative(psi, R): pR, sp.Derivative(psi, v): pv, sp.Derivative(f, R): fR,
                    sp.Derivative(f, v): fv})
        return e.subs({psi: sp.log(Es), f: F0}).subs({V1: SYMS[6], V2: SYMS[7], R: SYMS[8]})
    return tosym(kap), tosym(Kll)


def s1():
    print("S1 (exact) kappa' and K'^l_l on every round slice vhat = V(R); B2 at V' = 1; d kappa'/d V'' > 0")
    kap, Kll = slice_formulas()
    Es, F0, pR, pv, fR, fv, V1, V2, R = SYMS
    Nk = Es**2 * F0**2 * pR + Es**2 * F0 * fR / 2 - 3 * Es * F0 * pR - Es * fv / 2 - 3 * Es * fR / 2 - pv + pR
    kB2 = -Nk / (Es * sp.sqrt(2 / Es - F0) * (2 - Es * F0))
    KB2 = 3 * (Es * F0 - 1) / (Es * R * sp.sqrt(2 / Es - F0))
    red = sp.simplify(kap.subs({V1: 1, V2: 0}) - kB2) == 0 and sp.simplify(Kll.subs({V1: 1, V2: 0}) - KB2) == 0
    dk = sp.simplify(sp.diff(kap, V2))
    want = 1 / (Es * V1 * sp.sqrt(V1 * (2 - Es * V1 * F0) / Es) * (2 - Es * V1 * F0))
    dk_ok = sp.simplify(dk - want) == 0
    lin = sp.simplify(sp.diff(kap, V2, 2)) == 0
    kc, _ = slice_formulas(drop_christoffel=True)
    ctl = sp.simplify(kc.subs({V1: 1, V2: 0}) - kB2) != 0
    print("   reduces to B2's kappa and Kt at V' = 1, V'' = 0: %s; kappa' is affine in V'' with d kappa'/d V'' = "
          "1/(E V' sqrt(V'(2 - E V' f)/E)(2 - E V' f)): %s, %s; control: Christoffel term dropped, no reduction "
          "(rejected): %s" % (red, dk_ok, lin, ctl))
    return red and dk_ok and lin and ctl, kap, Kll


def bumpd(x, a, b):
    """the C-infinity bump and its first two derivatives, analytically."""
    x = np.asarray(x, float)
    c, h = 0.5 * (a + b), 0.5 * (b - a)
    y = (x - c) / h
    out = [np.zeros_like(y) for _ in range(3)]
    m = np.abs(y) < 1
    yy = y[m]
    g = 1 - yy**2
    b0 = np.exp(1 - 1 / g)
    d1 = b0 * (-2 * yy / g**2)                                        # d/dy
    d2 = b0 * ((2 * yy / g**2)**2 - (2 / g**2 + 8 * yy**2 / g**3))
    out[0][m], out[1][m], out[2][m] = b0, d1 / h, d2 / h**2
    return out


def make_phi(A):
    """phi, phi', phi'' on a fine grid: phi'' a bump over the band minus two bumps, moments balanced."""
    from scipy.integrate import cumulative_trapezoid
    x = np.linspace(2.9, 5.9, 30001)
    bP, bL, bR = [bumpd(x, *iv)[0] for iv in (P_IV, L_IV, R_IV)]
    I = lambda y: np.trapezoid(y, x)                                          # noqa: E731
    lam = np.linalg.solve(np.array([[I(bL), I(bR)], [I(x * bL), I(x * bR)]]), np.array([I(bP), I(x * bP)]))
    pp = A * (bP - lam[0] * bL - lam[1] * bR)
    p1 = cumulative_trapezoid(pp, x, initial=0)
    p0 = cumulative_trapezoid(p1, x, initial=0)
    return x, p0, p1, pp, lam


def crossing(tb, bgd, A):
    uu, vv, R, S, Ru, Rv, mu = bgd
    dv = vv[1] - vv[0]
    vhp = -np.exp(2 * S[0]) / Ru[0]
    vh = np.concatenate([[0.0], np.cumsum((vhp[1:] + vhp[:-1]) / 2 * dv)])
    tau0 = -tb.AA + 0.02
    Aa = tb.AAMP * tb.sbump(vv, tb.V1S, tb.V2S)
    B = tb.BAMP * tb.sbump(uu, tb.U1P, tb.U2P)
    Sv = np.gradient(S, dv, axis=1, edge_order=2)
    lvpp = np.gradient(np.log(vhp), dv, edge_order=2)
    x, p0, p1, pp, _ = make_phi(A)
    ph = lambda r, arr: np.interp(r, x, arr, left=0.0, right=0.0)         # noqa: E731
    out = []
    for i in range(len(uu)):
        Ri = R[i]
        tau = vh - Ri - ph(Ri, p0)                                     # vhat - R - phi(R)
        m = np.isfinite(tau)
        if not m.any():
            continue
        t = tau[m]
        j = np.where(m)[0]
        k = np.searchsorted(t, tau0)
        if k == 0 or k >= len(t):
            continue
        j0, j1 = j[k - 1], j[k]
        if not (t[k - 1] <= tau0 <= t[k]):
            continue
        ww = (tau0 - tau[j0]) / (tau[j1] - tau[j0])
        I = lambda F: (1 - ww) * F[i, j0] + ww * F[i, j1]                   # noqa: E731
        I1 = lambda F: (1 - ww) * F[j0] + ww * F[j1]                         # noqa: E731
        Rr, s, ru, rv, M = I(R), I(S), I(Ru), I(Rv), I(mu)
        sv, vp, vpp, a_, b_ = I(Sv), I1(vhp), I1(lvpp), I1(Aa), B[i]
        E = np.exp(2 * s) / (-ru * vp)
        f = 1 - M / Rr**2
        psi_u = b_ / (3 * Rr**2 * ru)                                        # twobg5 G1 (b)
        psi_v = 2 * sv + np.exp(2 * s) * M / Rr**3 / ru - vpp
        psi_R, psi_vh = psi_u / ru, (psi_v - rv / ru * psi_u) / vp
        mu_u = -(2 / 3) * b_ * np.exp(-2 * s) * rv                           # G1 (a)
        mu_v = -(2 / 3) * a_ * np.exp(-2 * s) * ru
        mu_R, mu_vh = mu_u / ru, (mu_v - rv / ru * mu_u) / vp
        fR, fv = 2 * M / Rr**3 - mu_R / Rr**2, -mu_vh / Rr**2
        V1, V2 = 1 + ph(Rr, p1), ph(Rr, pp)
        out.append((Rr, E, f, psi_R, psi_vh, fR, fv, V1, V2, ph(Rr, p0)))
    return np.array(out)


def s2(kap, Kll):
    print("S2 (computed) a deformed slice through the band on which Racz's split is hyperbolic everywhere")
    tb = load('twobg5')
    fk = sp.lambdify(SYMS, kap, 'numpy')
    fK = sp.lambdify(SYMS, Kll, 'numpy')
    rows, ok, store = [], True, {}
    for n in (80, 160):
        bgd = tb.run(n)
        for A in (A_DEF, 0.0, -A_DEF):
            o = crossing(tb, bgd, A)
            Rr, E, f, pR, pv, fR, fv, V1, V2, dt = o.T
            k_ = fk(E, f, pR, pv, fR, fv, V1, V2, Rr)
            K_ = fK(E, f, pR, pv, fR, fv, V1, V2, Rr)
            prod = k_ * K_
            pos = Rr[prod > 0]
            band = (float(pos.min()), float(pos.max())) if len(pos) else None
            spacelike = float(np.min(V1)), float(np.max(E * V1 * f))
            rows.append((n, A, len(o), float(Rr.min()), float(Rr.max()), float(prod.max()), band, spacelike,
                         float(np.max(np.abs(dt)))))
            store[(n, A)] = o
    for (n, A, npts, rmin, rmax, mx, band, spl, dt) in rows:
        print("   n = %d, A = %+.3f: %d slice points, R in [%.3f, %.3f]; max kappa' K'^l_l = %.4e; positive on %s; "
              "min V' = %.4f > 0, max E V' f = %.4f < 2; max |tau' - tau0| = %.3f" %
              (n, A, npts, rmin, rmax, mx, ('R in [%.4f, %.4f]' % band) if band else 'no point', spl[0], spl[1], dt))
    get = {(r[0], r[1]): r for r in rows}
    hyp = all(get[(n, A_DEF)][5] < 0 and get[(n, A_DEF)][6] is None for n in (80, 160))
    spacel = all(get[(n, A_DEF)][7][0] > 0 and get[(n, A_DEF)][7][1] < 2 for n in (80, 160))
    conv = abs(get[(160, A_DEF)][5] - get[(80, A_DEF)][5]) < 0.05 * abs(get[(160, A_DEF)][5])
    ctl0 = all(get[(n, 0.0)][6] is not None for n in (80, 160))
    b0, bm = get[(160, 0.0)][6], get[(160, -A_DEF)][6]
    ctlm = bm is not None and (bm[1] - bm[0]) > (b0[1] - b0[0])
    print("   hyperbolic on all of Sigma' (A = %.2f): %s; spacelike: %s; converged: %s; controls: A = 0 has the band "
          "(rejected): %s; A -> -A widens it (rejected): %s" % (A_DEF, hyp, spacel, conv, ctl0, ctlm))
    return hyp and spacel and conv and ctl0 and ctlm, store


def s3(store):
    print("S3 (computed) the lens between Sigma' and Sigma_tau0, and the angular widening it causes")
    o = store[(160, A_DEF)]
    Rr, dt = o[:, 0], o[:, 9]
    inlens = np.abs(dt) > 1e-12
    rmin, rmax = float(Rr[inlens].min()), float(Rr[inlens].max())
    thick = float(np.abs(dt).max())
    spread = thick / rmin
    ok = rmin >= L_IV[0] - 1e-9 and rmax <= R_IV[1] + 1e-9 and thick < 0.01
    print("   the lens: R in [%.3f, %.3f] (inside [%.2f, %.2f]), thickness %.5f in tau; angular widening <= "
          "max |phi|/R_min = %.5f rad: %s" % (rmin, rmax, L_IV[0], R_IV[1], thick, spread, ok))
    return ok


def main():
    res = {}
    ok1, kap, Kll = s1()
    res['S1'] = ok1
    print('S1', 'PASS' if ok1 else 'FAIL', flush=True)
    ok2, store = s2(kap, Kll)
    res['S2'] = ok2
    print('S2', 'PASS' if ok2 else 'FAIL', flush=True)
    res['S3'] = s3(store)
    print('S3', 'PASS' if res['S3'] else 'FAIL', flush=True)
    return 0 if all(res.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
