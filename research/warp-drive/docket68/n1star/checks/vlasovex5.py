#!/usr/bin/env python3
"""vlasovex5: Theorem V is not vacuous -- an explicit family meeting its open conditions (FAMILIES5-R6.md section 3).

The background is the record's g0 with constant mass (five-dimensional Tangherlini, mu = 1) in its Kerr-Schild form
g0 = -dt^2 + dr^2 + r^2 dOmega_3^2 + (mu/r^2)(dt + dr)^2 (tau = t, v = t + r), on the record's domain (1.1) with
tau0 = 0, tau_end = 3, a = 0.8 < sqrt(mu), V = 5: Omega = {0 <= tau <= 3, r >= a, r <= b(tau) = V + 1 - tau +
(tau_end - tau)}. A restricted field is a family of dusts labelled by w; label w's eikonal has, on Sigma_0, the data
u_w = cos w rho(r) + sin w r_c th, rho' = sqrt(1 + mu/r^2) (so its gradient's angle in the orthonormal frame is
beta0 = atan2(r_c sin w/r, cos w)), and its density is supported on the ball B = {|r - r_c| <= 0.3, |th - pi/4| <=
0.15}, r_c = 3, for w in two label intervals I1 = [-0.5, 0.5] and I2 = [pi - 0.5, pi + 0.5] (the density a smooth
bump in w vanishing outside them, so it is smooth and periodic on S^1).

  X1 (exact, sympy) the record's open conditions for g0 on this Omega (N1STAR-PROOF.md Lemma 1.1 (a)-(c), (f)):
     g0^-1(dtau, dtau) = -1 - mu/r^2 < 0; at r = a, g0^-1(dr, dr) = 1 - mu/a^2 < 0 and g0^-1(dr, dtau) = mu/a^2 > 0;
     g0^-1(d(v + tau), d(v + tau)) = -3 - mu/r^2 < 0; b(tau) - a >= 1 + delta0 (delta0 = 0.05) on [0, 3]. And Lemma
     6.3 (a) at g0's data on Sigma_0 (the closed forms of twoslice5 S1 at G = 1 + mu/r^2): theta^3 H = 3/(r G^2) > 0
     and S A0 = diag(6, 1/(G r^2)) > 0. Control (must fail): an untrapped inner boundary a = 1.2 makes g0^-1(dr, dr)
     > 0 there.
  X2 (computed, numpy RK4 with central differences) the family's open conditions on Omega: for every label of I1 and
     I2 (81 labels each) and every initial point of a neighbourhood of B (the ball enlarged by 20 %, a 9 x 9 grid of
     rays), followed until it leaves Omega:
     (i)   caustic-free: the Jacobian det d(r, th)(t)/d(r0, th0) stays >= J_min > 0 (printed) on every ray, so each u_w
           has no caustic on a neighbourhood of its tube D_w;
     (ii)  direction-labelled: d beta0/d w = (r_c/r)/(cos^2 w + (r_c/r)^2 sin^2 w) >= b > 0 on B (exact formula,
           its least value printed);
     (iii) off the axes: every tube stays at angular distance >= 2 delta from th = 0 and th = pi/2 (delta printed);
     (iv)  the rays of I1 are outgoing and leave through the outer boundary, those of I2 ingoing, crossing the horizon
           r = 1 and leaving through r = a (printed).
     Control (must fail): a focusing family (data u = -|x - x_f| in the slice's (rho, r_c th) chart, focus at
     distance 1 ahead of B) has a Jacobian that changes sign on Omega: the caustic check rejects it.
  X3 (computed) the conditions are open, illustrated: with mu = 1.05 and the initial directions tilted by 0.05
     sin(2 th) (a different nearby metric and family), J_min, b and delta move by small amounts and stay positive.
     (The proof of openness is the continuous dependence of the ray flow and of its first variation on the metric in
     C^2 and the data in C^1, on the compact closure of Omega: FAMILIES5-R6.md section 3.)

Labels: computed (X1 exact; X2, X3 floating point). Run: python3 checks/vlasovex5.py   (a few minutes)
"""
import math
import sys

import numpy as np
import sympy as sp

MU, A_IN, TAU_END, V_ = 1.0, 0.8, 3.0, 5.0
RC, TH_C, DR, DTH = 3.0, math.pi / 4, 0.3, 0.15


def b_out(t):
    return V_ + 1 - t + (TAU_END - t)


def x1():
    print("X1 (exact) the record's open conditions for g0 on Omega, and Lemma 6.3 (a) at its data")
    r, mu, a, tau = sp.symbols('r mu a tau', positive=True)
    f = mu / r**2
    # g0^-1 = eta^-1 - (mu/r^2) l l, l = eta^-1 dv = (-1, 1) in (t, r)
    gi = sp.Matrix([[-1 - f, f], [f, 1 - f]])
    dtau, dr_, dv = sp.Matrix([1, 0]), sp.Matrix([0, 1]), sp.Matrix([1, 1])
    q = lambda x, y: sp.simplify((x.T * gi * y)[0])                                 # noqa: E731
    sub = {mu: 1, a: sp.Rational(4, 5)}
    ok_a = sp.simplify(q(dtau, dtau) + 1 + mu / r**2) == 0
    ok_b = q(dr_, dr_).subs(r, a).subs(sub) < 0 and q(dr_, dtau).subs(r, a).subs(sub) > 0
    ok_c = sp.simplify(q(dv + dtau, dv + dtau) + 3 + mu / r**2) == 0
    bmin = min(b_out(t) for t in np.linspace(0, TAU_END, 301)) - A_IN
    ok_f = bmin >= 1.05
    G = 1 + mu / r**2
    lemma63 = all(float(e.subs({mu: 1, r: rv})) > 0 for rv in (0.8, 1, 2, 5, 9) for e in (3 / (r * G**2),
                                                                                         1 / (G * r**2)))
    ctl = q(dr_, dr_).subs(r, sp.Rational(6, 5)).subs({mu: 1}) > 0
    print("   (a) g0^-1(dtau, dtau) = -1 - mu/r^2: %s; (b) at a = 0.8: g^rr = %s < 0, g^r tau = %s > 0: %s; (c) "
          "g0^-1(d(v + tau), .) = -3 - mu/r^2: %s; (f) min b - a = %.2f >= 1.05: %s; Lemma 6.3 (a) signs: %s; "
          "control: untrapped a = 1.2 has g^rr > 0 (rejected): %s" %
          (ok_a, q(dr_, dr_).subs(r, a).subs(sub), q(dr_, dtau).subs(r, a).subs(sub), ok_b, ok_c, bmin, ok_f,
           lemma63, ctl))
    return ok_a and bool(ok_b) and ok_c and ok_f and lemma63 and bool(ctl)


def ginv(r, mu):
    f = mu / r**2
    return -1 - f, f, 1 - f                                      # g^tt, g^tr, g^rr; g^thth = 1/r^2


def initial(r0, th0, w, mu, tilt=0.0, focus=None):
    """the spatial covector of label w at (r0, th0) on Sigma_0 and its future null completion"""
    G = 1 + mu / r0**2
    if focus is None:
        kr = np.cos(w) * np.sqrt(G)
        kth = np.sin(w + tilt * np.sin(2 * th0)) * RC
    else:                                                        # u = -|x - x_f| in the (rho, r_c th) chart
        rf, thf = focus
        X = (r0 - rf) * np.sqrt(G)
        Y = RC * (th0 - thf)
        d = np.sqrt(X**2 + Y**2)
        kr, kth = -X / d * np.sqrt(G), -Y / d * RC
    gtt, gtr, grr = ginv(r0, mu)
    # g^tt pt^2 + 2 g^tr pt kr + g^rr kr^2 + kth^2/r^2 = 0; the future root (dt/ds = g^tt pt + g^tr kr > 0)
    A, Bq, C = gtt, 2 * gtr * kr, grr * kr**2 + kth**2 / r0**2
    disc = np.sqrt(Bq**2 - 4 * A * C)
    roots = [(-Bq + disc) / (2 * A), (-Bq - disc) / (2 * A)]
    pt = np.where(gtt * roots[0] + gtr * kr > 0, roots[0], roots[1])
    return pt, kr, kth


def flow(r0, th0, w, mu, T=TAU_END, nst=600, tilt=0.0, focus=None):
    """rays parametrised by t; returns arrays (steps, ...) of r, th"""
    pt, pr, pth = initial(r0, th0, w, mu, tilt, focus)
    r, th = np.array(r0, float), np.array(th0, float)
    pr = np.array(pr, float)

    def rhs(r, th, pr):
        f = mu / r**2
        fp = -2 * mu / r**3
        xt = (-1 - f) * pt + f * pr
        xr = f * pt + (1 - f) * pr
        xth = pth / r**2
        dH = 0.5 * (-fp * pt**2 + 2 * fp * pt * pr - fp * pr**2 - 2 * pth**2 / r**3)
        return xr / xt, xth / xt, -dH / xt
    h = T / nst
    out = [(r.copy(), th.copy())]
    for _ in range(nst):
        k1 = rhs(r, th, pr)
        k2 = rhs(r + h / 2 * k1[0], th + h / 2 * k1[1], pr + h / 2 * k1[2])
        k3 = rhs(r + h / 2 * k2[0], th + h / 2 * k2[1], pr + h / 2 * k2[2])
        k4 = rhs(r + h * k3[0], th + h * k3[1], pr + h * k3[2])
        r = r + h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        th = th + h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        pr = pr + h / 6 * (k1[2] + 2 * k2[2] + 2 * k3[2] + k4[2])
        out.append((r.copy(), th.copy()))
    return np.array([o[0] for o in out]), np.array([o[1] for o in out])


def family_margins(ws, mu, tilt=0.0, focus=None, enlarge=1.2, ng=9, nst=600):
    """least Jacobian, least axis distance, and exit data over labels ws and a grid of initial points"""
    rr = np.linspace(RC - enlarge * DR, RC + enlarge * DR, ng)
    tt = np.linspace(TH_C - enlarge * DTH, TH_C + enlarge * DTH, ng)
    R0, T0 = np.meshgrid(rr, tt, indexing='ij')
    W = np.broadcast_to(np.asarray(ws)[:, None, None], (len(ws),) + R0.shape)
    R0b, T0b = np.broadcast_to(R0, W.shape), np.broadcast_to(T0, W.shape)
    e = 1e-5
    ts = np.linspace(0, TAU_END, nst + 1)
    base = flow(R0b, T0b, W, mu, nst=nst, tilt=tilt, focus=focus)
    pr_ = flow(R0b + e, T0b, W, mu, nst=nst, tilt=tilt, focus=focus)
    mr_ = flow(R0b - e, T0b, W, mu, nst=nst, tilt=tilt, focus=focus)
    pt_ = flow(R0b, T0b + e, W, mu, nst=nst, tilt=tilt, focus=focus)
    mt_ = flow(R0b, T0b - e, W, mu, nst=nst, tilt=tilt, focus=focus)
    drr, dthr = (pr_[0] - mr_[0]) / (2 * e), (pr_[1] - mr_[1]) / (2 * e)
    drt, dtht = (pt_[0] - mt_[0]) / (2 * e), (pt_[1] - mt_[1]) / (2 * e)
    J = drr * dtht - drt * dthr
    r, th = base
    inside = (r >= A_IN) & (r <= b_out(ts)[:, None, None, None])
    alive = np.cumprod(inside, axis=0).astype(bool)              # until the ray first leaves Omega
    Jmin = float(np.min(np.where(alive, J, np.inf)))
    Jneg = bool(np.any(alive & (J <= 0)))
    axis = float(np.min(np.where(alive, np.minimum(th, math.pi / 2 - th), np.inf)))
    last = alive.sum(axis=0) - 1
    rexit = np.take_along_axis(r, last[None], axis=0)[0]
    return Jmin, Jneg, axis, rexit


def b_label(ws):
    rr = np.linspace(RC - DR, RC + DR, 41)
    W, Rr = np.meshgrid(np.asarray(ws), rr, indexing='ij')
    q = RC / Rr
    return float(np.min(q / (np.cos(W)**2 + q**2 * np.sin(W)**2)))


def x2():
    print("X2 (computed) the explicit family: caustic-free, direction-labelled, off the axes, on Omega")
    I1 = np.linspace(-0.5, 0.5, 81)
    I2 = np.linspace(math.pi - 0.5, math.pi + 0.5, 81)
    res = {}
    for nm, I in (('I1', I1), ('I2', I2)):
        Jmin, Jneg, axis, rexit = family_margins(I, MU)
        res[nm] = (Jmin, Jneg, axis, float(rexit.min()), float(rexit.max()), b_label(I))
        print("   %s: least Jacobian on the tubes' neighbourhood %.4f > 0 (no sign change: %s); least axis distance "
              "%.4f (delta = %.4f); exit radii in [%.3f, %.3f]; least d beta0/d w on B = %.4f" %
              (nm, Jmin, not Jneg, axis, axis / 2, res[nm][3], res[nm][4], res[nm][5]))
    out_nm = 'I1' if res['I1'][3] > RC else 'I2'
    in_nm = 'I2' if out_nm == 'I1' else 'I1'
    dirs = res[out_nm][3] > RC and res[in_nm][4] < A_IN + 0.05             # out through r = b, in through r = a
    ok = all(res[k][0] > 0 and not res[k][1] and res[k][2] > 0 and res[k][5] > 0 for k in res) and dirs
    # control: a focusing family, its focus at distance 1 ahead in the direction the outgoing rays move
    sgn = 1.0 if out_nm == 'I1' else -1.0
    Jf, Jfneg, _, _ = family_margins(np.array([0.0]), MU, focus=(RC + sgn * (DR + 1.0), TH_C))
    ctl = Jfneg
    print("   %s outgoing (leaves through r = b), %s ingoing (through r = a): %s; control: a family focused at "
          "distance 1 ahead has a Jacobian changing sign (least %.4f; rejected): %s" % (out_nm, in_nm, dirs, Jf, ctl))
    return ok and ctl, res


def x3(res0):
    print("X3 (computed) openness, illustrated: a nearby metric (mu = 1.05) and tilted directions")
    ok = True
    for nm, I in (('I1', np.linspace(-0.5, 0.5, 41)), ('I2', np.linspace(math.pi - 0.5, math.pi + 0.5, 41))):
        Jmin, Jneg, axis, rexit = family_margins(I, 1.05, tilt=0.05)
        bl = b_label(I)
        J0, _, ax0, _, _, b0 = res0[nm]
        print("   %s: least Jacobian %.4f (was %.4f), axis distance %.4f (was %.4f), d beta0/d w %.4f (was %.4f): all "
              "positive: %s" % (nm, Jmin, J0, axis, ax0, bl, b0, Jmin > 0 and not Jneg and axis > 0))
        ok &= Jmin > 0 and not Jneg and axis > 0 and abs(Jmin - J0) < 0.5 * J0 and abs(axis - ax0) < 0.5 * ax0
    return ok


def main():
    res = {}
    res['X1'] = x1()
    print('X1', 'PASS' if res['X1'] else 'FAIL', flush=True)
    ok2, r2 = x2()
    res['X2'] = ok2
    print('X2', 'PASS' if ok2 else 'FAIL', flush=True)
    res['X3'] = x3(r2)
    print('X3', 'PASS' if res['X3'] else 'FAIL', flush=True)
    return 0 if all(res.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
