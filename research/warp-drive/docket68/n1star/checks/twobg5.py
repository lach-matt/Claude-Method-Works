#!/usr/bin/env python3
"""twobg5: the two-dust background on the whole domain, with the outgoing family's data stated (FAMILIES5-FULL.md
section 2).

The data. The record's seed (five-dimensional Tangherlini of mass mu0) and ingoing shell (dmu/dv = (2/9) A^2 env^2), and
an outgoing packet which, on the slice Sigma_tau0, lies between the seed's horizon and the shell. Before the shell
(v <= v_start) the background is then outgoing Vaidya with a mass m(u) that falls from mu0 + E2 outside the packet to
mu0 inside it; outside the packet (u <= u1) it is ingoing Vaidya. So the characteristic data on the cones N' = {v = 0}
(before the shell) and N = {u = 0} (outside the packet) are explicit Vaidya data, and the only region where both dusts
are present is the crossing diamond Q_x = [u1, u2] x [v_start, v_end]. Notation: g0 = -2 e^(2s) du dv + R^2 dOmega_3^2,
K_in R^3 = A(v), K_out R^3 = B(u) (twodust5 B1-B3), mu := R^2 (1 + 2 e^(-2s) R_u R_v).

  G1 (exact, sympy, modulo the evolution and both constraints) the identities the structure and the bounds rest on:
     (a) mu_u = -(2/3) B e^(-2s) R_v and mu_v = -(2/3) A e^(-2s) R_u: where B = 0 the mass is a function of v alone,
         where A = 0 of u alone;
     (b) with psi := ln(-e^(2s)/(R_u vhat')), psi_u = B/(3 R^2 R_u), and the mirror psit := ln(e^(2s)/(R_v uhat')) has
         psit_v = A/(3 R^2 R_v): where B = 0 the background is ingoing Vaidya in (vhat, R), vhat reparametrised, and
         where A = 0 and R_v != 0 it is outgoing Vaidya in (uhat, R);
     (c) mu_uv = (2/9) A B e^(-2s)/R^2, R_uv = -e^(2s) mu/R^3, s_uv = (3/2) e^(2s) mu/R^4;
     (d) where A = 0, (e^(-2s) R_v)_v = 0: the sign of R_v (trapped or not) is kept along the outgoing rays there.
     Control: with B depending on v the identity (c) for mu_uv leaves a residual.
  G2 (computed, floating point) the background from the stated data on the rectangle u in [0, U1], v in [0, V1], at n =
     40, 80, 160 steps per unit (twodomain5's diamond scheme, C-infinity bumps): corner mass 1.5 at R = 5; the outgoing
     packet B = 1.7 b(u; 5.7, 7.2) on N', where N' is untrapped (R_v > 0); the shell A = 3.6 b(v; 3, 4.5) on N; mu0 :=
     the mass on N' inside the packet (the seed). Checked:
     (i)   the structure: |mu - mu(0, v)| on u <= u1 - 0.1, |mu - mu(u2 + 0.1, v)| on u >= u2 + 0.1, |mu - mu(u, 0)|
           on v <= v_start - 0.1 and |mu - mu(u, v_end + 0.1)| on v >= v_end + 0.1, over the resolved cells (R >= a and
           v <= 2, or R^2 >= 1.05 mu), all fall with n: the background is Vaidya (ingoing or outgoing) off the diamond;
     (ii)  the mass bound: min(mu - mu0) over R >= a is either >= 0 or a deficit falling at second order with n (by
           3 or more per halving), so it is discretisation: mu >= mu0 everywhere;
     (iii) the inner sphere R = a = 0.7 is crossed in every v-column with v <= 2 (where the grid resolves the strip
           between the horizon and R -> 0) and is trapped there (R_v < 0), mu - a^2 >= mu0 - a^2 - tol; for all v, the
           mass of region III (u >= u2, ingoing Vaidya by G1), read at u = u2 + 0.1, is >= mu0 - tol > a^2, so R = a is
           trapped there by g0^-1(dR, dR) = 1 - mu/R^2;
     (iv)  past-closedness: at every cell with R >= a, the least R over its past rectangle is >= min(R, sqrt(mu0)) -
           tol;
     (v)   the diamond: least R on Q_x and whether Q_x is untrapped;
     (vi)  Sigma_tau0, tau := vhat - R (vhat fixed by psi = 0 on N), tau0 := -a + 0.02: on it the packet lies between the
           seed's horizon sqrt(mu0) and the shell's inner edge, and the shell's inner edge satisfies the record's rule
           v_start - tau0 > sqrt(mu0) + 1;
     (vii) the mixed symbol: with the phases vhat and u (the outgoing phase normalised by the affine parameter of
           the data cone N'; any lam-independent normalisation serves), |g0^-1(dvhat, du)| = e^(-2s) vhat'(v) is
           positive on every computed cell; off the trapped region (R^2 >= 1.5 mu) its least value is stable in n to
           10 %; on R = a it is converged (to 1 %) at v = 0.5, 1, 1.5 and halves with each 0.5 in v (printed): the
           outgoing rays that reach R = a later leave N' from an exponentially narrower range of u (the redshift at
           the horizon), so the lower bound is a positive constant on the compact Omega that degenerates exponentially
           with the time spent in the hole.
  Control (computed): the same run with B -> -B (a negative-energy outgoing dust, A B < 0): mu falls below mu0 by an
     amount that does not shrink with n, so (ii) fails; the bound needs A B >= 0, as G1 (c) says.

Reach: the numbers are one example of the stated data. The proof (FAMILIES5-FULL.md section 2) is deduced from G1 and the
record's twoext5 X1-X2, twodomain5 D1-D2; G2 illustrates it, and later v inside the hole (region u >= u2, which is
ingoing Vaidya by G1 (a)-(b)) is left to the explicit form, the double-null grid thinning there.

Run: python3 checks/twobg5.py   (about three minutes)
"""
import math
import os
import sys

import numpy as np
import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import twodomain5 as TD                                                         # noqa: E402

AA = 0.7
VRES = 2.0                   # the interior strip near R = a is resolved by the double-null grid for v <= VRES
U1P, U2P = 5.7, 7.2          # the outgoing packet on N' = {v = 0}
V1S, V2S = 3.0, 4.5          # the shell on N = {u = 0}
BAMP, AAMP = 1.7, 3.6
MUC, R0 = 1.5, 5.0


def sbump(x, a, b):
    """C-infinity bump on (a, b), max 1"""
    w = 2 * (np.asarray(x, float) - a) / (b - a) - 1
    out = np.zeros_like(w)
    m = np.abs(w) < 1
    out[m] = np.exp(1 - 1 / (1 - w[m]**2))
    return out


def g1():
    u, v = sp.symbols('u v')
    R, s = sp.Function('R')(u, v), sp.Function('s')(u, v)
    A, Bu, Bv = sp.Function('A')(v), sp.Function('B')(u), sp.Function('B')(u, v)
    vh, uh = sp.Function('vh')(v), sp.Function('uh')(u)
    Ru, Rv = sp.diff(R, u), sp.diff(R, v)
    F = -(sp.exp(2 * s) + 2 * Ru * Rv) / R
    G = 3 * (sp.exp(2 * s) + 2 * Ru * Rv) / (2 * R**2)
    mu = R**2 * (1 + 2 * sp.exp(-2 * s) * Ru * Rv)

    def onshell(e, B):
        Ruu = 2 * sp.diff(s, u) * Ru - B / (3 * R**2)
        Rvv = 2 * sp.diff(s, v) * Rv - A / (3 * R**2)
        rep = [(sp.Derivative(R, (u, 2), v), sp.diff(Ruu, v)), (sp.Derivative(R, u, (v, 2)), sp.diff(Rvv, u))]
        for _ in range(3):
            e = e.subs(rep).subs({sp.Derivative(R, u, v): F, sp.Derivative(s, u, v): G,
                                  sp.Derivative(R, (u, 2)): Ruu, sp.Derivative(R, (v, 2)): Rvv})
        return sp.simplify(e)

    ok = {}
    ok['a'] = (onshell(sp.diff(mu, u) + sp.Rational(2, 3) * Bu * sp.exp(-2 * s) * Rv, Bu) == 0
               and onshell(sp.diff(mu, v) + sp.Rational(2, 3) * A * sp.exp(-2 * s) * Ru, Bu) == 0)
    psi = sp.log(-sp.exp(2 * s) / (Ru * sp.diff(vh, v)))
    psit = sp.log(sp.exp(2 * s) / (Rv * sp.diff(uh, u)))
    ok['b'] = (onshell(sp.diff(psi, u) - Bu / (3 * R**2 * Ru), Bu) == 0
               and onshell(sp.diff(psit, v) - A / (3 * R**2 * Rv), Bu) == 0)
    ok['c'] = (onshell(sp.diff(mu, u, v) - sp.Rational(2, 9) * A * Bu * sp.exp(-2 * s) / R**2, Bu) == 0
               and sp.simplify(F + sp.exp(2 * s) * mu / R**3) == 0
               and sp.simplify(G - sp.Rational(3, 2) * sp.exp(2 * s) * mu / R**4) == 0)
    ok['d'] = onshell(sp.diff(sp.exp(-2 * s) * Rv, v), Bu).subs(A, 0) == 0
    ctl = onshell(sp.diff(mu, u, v) - sp.Rational(2, 9) * A * Bv * sp.exp(-2 * s) / R**2, Bv) != 0
    return ok, ctl


def run(n, sign=1.0, U1=9.6, V1=5.0):
    A = lambda x: AAMP * sbump(x, V1S, V2S)                                     # noqa: E731
    B = lambda x: sign * BAMP * sbump(x, U1P, U2P)                              # noqa: E731
    uu, vv, R, S = TD.solve(n, A, B, mu0=MUC, R0=R0, U1=U1, V1=V1, Rmin=0.3)
    du, dv = uu[1] - uu[0], vv[1] - vv[0]
    Ru = np.gradient(R, du, axis=0, edge_order=2)
    Rv = np.gradient(R, dv, axis=1, edge_order=2)
    mu = R**2 * (1 + 2 * np.exp(-2 * S) * Ru * Rv)
    return uu, vv, R, S, Ru, Rv, mu


def measure(n, sign=1.0):
    uu, vv, R, S, Ru, Rv, mu = run(n, sign)
    fin = np.isfinite(R) & np.isfinite(mu)
    ia = uu >= U2P + 0.1
    mu0 = float(np.nanmedian(mu[ia, 0][np.isfinite(mu[ia, 0])]))
    good = fin & (R >= AA)
    # interior cells: one-sided stencils at the excision edge spoil mu; keep cells whose neighbours are finite
    nb = np.zeros_like(good)
    nb[1:-1, 1:-1] = (fin[2:, 1:-1] & fin[:-2, 1:-1] & fin[1:-1, 2:] & fin[1:-1, :-2])
    good &= nb | (np.arange(R.shape[0])[:, None] == 0) | (np.arange(R.shape[1])[None, :] == 0)
    out = {'mu0': mu0}
    res_ = good & ((vv[None, :] <= VRES) | (R**2 >= 1.05 * mu))  # resolved: before the strip thins, or untrapped
    good_all, good = good, res_
    # (i) structure
    iI = uu <= U1P - 0.1
    e1 = np.abs(mu[iI, :] - mu[0][None, :])[good[iI, :]].max()
    k3 = int(np.argmin(np.abs(uu - (U2P + 0.1))))
    e2 = np.abs(mu[ia, :] - mu[k3][None, :])[good[ia, :] & np.isfinite(mu[k3])[None, :]].max()
    jb = vv <= V1S - 0.1
    e3 = np.abs(mu[:, jb] - mu[:, :1])[good[:, jb]].max()
    ja = vv >= V2S + 0.1
    k4 = int(np.argmin(np.abs(vv - (V2S + 0.1))))
    m4 = good[:, ja] & np.isfinite(mu[:, k4])[:, None]
    e4 = np.abs(mu[:, ja] - mu[:, k4][:, None])[m4].max()
    out['struct'] = (float(e1), float(e2), float(e3), float(e4))
    # (ii) mass bound
    out['minmu'] = float((mu - mu0)[good_all].min())
    # (iii) inner sphere
    cols, trapped, mua = 0, True, []
    jres = np.where(vv <= VRES)[0]
    for j in jres:
        idx = np.where(np.isfinite(R[:, j]) & (R[:, j] < AA))[0]
        if len(idx) == 0 or idx[0] < 2:
            continue
        i = idx[0] - 1
        if not np.isfinite(mu[i, j]):
            continue
        cols += 1
        trapped &= bool(Rv[i, j] < 0)
        mua.append(mu[i, j] - AA * AA)
    out['inner'] = (cols, len(jres), trapped, float(min(mua)))
    out['muIII'] = float(np.nanmin(mu[k3]))
    # (iv) past-closedness on the grid
    Rf = np.where(np.isfinite(R), R, -1.0)
    cm = np.minimum.accumulate(np.minimum.accumulate(Rf, axis=0), axis=1)
    target = np.minimum(R, math.sqrt(mu0))
    out['pastc'] = float((cm - target)[good_all].min())
    # (v) the diamond
    dq = (uu[:, None] >= U1P) & (uu[:, None] <= U2P) & (vv[None, :] >= V1S) & (vv[None, :] <= V2S)
    out['diamond'] = (float(R[dq & fin].min()), bool((Rv[dq & fin] > 0).all()), float(mu[dq & fin].max()))
    # (vi) Sigma_tau0 and (vii) the mixed symbol
    dvv = vv[1] - vv[0]
    vhp = -np.exp(2 * S[0]) / Ru[0]                                              # psi = 0 on N
    vh = np.concatenate([[0.0], np.cumsum((vhp[1:] + vhp[:-1]) / 2 * dvv)])
    tau0 = -AA + 0.02
    tau = vh[None, :] - R
    Rsig = np.full(R.shape[0], np.nan)                                          # R where the ray u meets Sigma_tau0
    for i in range(R.shape[0]):
        row = tau[i]
        m = np.isfinite(row)
        jj = np.where(m[:-1] & m[1:] & ((row[:-1] - tau0) * (row[1:] - tau0) <= 0))[0]
        if len(jj):
            j = jj[0]
            t = (tau0 - row[j]) / (row[j + 1] - row[j])
            Rsig[i] = R[i, j] + t * (R[i, j + 1] - R[i, j])
    pk = (uu >= U1P) & (uu <= U2P) & np.isfinite(Rsig)
    shell_in = float(np.interp(V1S, vv, vh)) - tau0                            # R of the shell's inner edge on it
    out['sigma'] = (float(np.nanmin(Rsig[pk])), float(np.nanmax(Rsig[pk])), math.sqrt(mu0), shell_in,
                    shell_in > math.sqrt(mu0) + 1)
    sym = np.exp(-2 * S) * vhp[None, :]                                         # the outgoing phase normalised by u

    ext = good & np.isfinite(sym) & (R**2 >= 1.5 * mu)
    ma = good_all & np.isfinite(sym)
    ona = []                                                                    # on R = a at v = 0.5, 1, 1.5, 2
    for vt in (0.5, 1.0, 1.5):
        j = int(np.argmin(np.abs(vv - vt)))
        i = int(np.where(np.isfinite(R[:, j]) & (R[:, j] < AA))[0][0]) - 1    # R[i] >= a > R[i + 1]
        w = (R[i, j] - AA) / (R[i, j] - R[i + 1, j])
        ona.append(float(math.exp((1 - w) * math.log(abs(sym[i, j])) + w * math.log(abs(sym[i + 1, j])))))
    out['symbol'] = (float(np.abs(sym[ext]).min()), float(np.abs(sym[ext]).max()), float(np.abs(sym[ma]).min()), ona)
    out['muend'] = float(mu[0, -1])
    # G5: the packet's distance from the background horizon of its columns, R(u2, v) - sqrt(mu_III(v)), v <= V1
    i2 = int(np.argmin(np.abs(uu - U2P)))
    gap = R[i2] - np.sqrt(mu[k3])
    okg = np.isfinite(gap)
    out['gap6'] = (float(gap[okg].min()), float(vv[okg][np.argmin(gap[okg])]), bool((Rv[i2][okg] > 0).all()))
    out['grid'] = dict(uu=uu, vv=vv, R=R, S=S, Ru=Ru, mu=mu, k3=k3, vh=vh, vhp=vhp, tau0=tau0, mu0=mu0)
    return out


def rk4(f, y, t0, t1, n):
    h = (t1 - t0) / n
    t = t0
    for _ in range(n):
        k1 = f(t, y)
        k2 = f(t + h / 2, [a + h / 2 * b for a, b in zip(y, k1)])
        k3 = f(t + h / 2, [a + h / 2 * b for a, b in zip(y, k2)])
        k4 = f(t + h, [a + h * b for a, b in zip(y, k3)])
        y = [a + h / 6 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(y, k1, k2, k3, k4)]
        t += h
    return y


def g3(G, T=1.0, delta0=0.05):
    """the outer data cone N = {u = u0} against the domain's outer boundary R = b(tau), tau in [tau0, tau_end]"""
    vv, R, vh, tau0, mu0 = G['vv'], G['R'], G['vh'], G['tau0'], G['mu0']
    q0 = AA + delta0                                                            # r_q(mu0) = q0 fixes l5
    l5sq = q0**4 / (math.sqrt(72) * mu0)
    seed = mu0 >= math.sqrt(72) * l5sq and AA < q0 <= math.sqrt(mu0)
    vh_end = float(np.interp(V2S, vv, vh))
    V = vh_end + T
    tau_end = V - q0                       # r_q(mu) >= r_q(mu0) = q0 (mu >= mu0): an upper bound, so b is overstated
    b = lambda tau: V + 1 - tau + (tau_end - tau)                              # noqa: E731
    muI = G['mu'][0]                                                            # region I: ingoing Vaidya, mu(vhat)
    mu_end = float(muI[-1])

    def mu_of(x):
        return float(np.interp(x, vh, muI)) if x <= vh[-1] else mu_end

    def ray(R0):
        """the outgoing ray of region I from (vhat, R) = (0, R0): dR/dvhat = (1 - mu/R^2)/2; R - b at tau0 and the
        least of R - b over [tau0, tau_end] (tau = vhat - R increases along it while it is untrapped)"""
        y, x, h, worst, at0 = [R0], 0.0, 0.01, None, None
        while True:
            tau = x - y[0]
            if at0 is None and tau >= tau0:
                at0 = y[0] - b(tau)
            if tau >= tau0:
                worst = y[0] - b(tau) if worst is None else min(worst, y[0] - b(tau))
            if tau > tau_end:
                return at0, worst
            y = rk4(lambda t, z: [(1 - mu_of(t) / z[0]**2) / 2], y, x, x + h, 1)
            x += h
    ex_at0, ex_worst = ray(float(R[0, 0]))                                      # the example's N: u0 = 0, R = 5
    lo, hi = float(R[0, 0]), 60.0                                               # the least R0 with R - b >= 1
    for _ in range(40):
        mid = (lo + hi) / 2
        if ray(mid)[1] >= 1.0:
            hi = mid
        else:
            lo = mid
    new_at0, new_worst = ray(hi)
    return dict(seed=seed, l5=math.sqrt(l5sq), V=V, tau_end=tau_end, b0=b(tau0), ex=(ex_at0, ex_worst),
                R0new=hi, new=(new_at0, new_worst))


def g4(G, redshift=True, npts=(0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 4.9), steps=4000):
    """the mixed symbol |g0^-1(dvhat, du)| = e^(-psi)/|R_u| on R = a, along region III's outgoing rays: in u >= u2
    (B = 0) psi and mu depend on v alone, dR/dv = vhat' e^psi (1 - mu/R^2)/2 and d ln|R_u|/dv = vhat' e^psi mu/R^3
    (G1 (b) and R_uv = -e^(2s) mu/R^3); the coefficients are read on u = u2 + 0.1 and on N, the rays start on N'"""
    uu, vv, R, S, Ru, mu, k3, vhp = (G[k] for k in ('uu', 'vv', 'R', 'S', 'Ru', 'mu', 'k3', 'vhp'))
    psiIII = np.log(-np.exp(2 * S[k3]) / (Ru[k3] * vhp))
    muIII = mu[k3]
    ok = np.isfinite(psiIII) & np.isfinite(muIII)
    vgrid = vv[ok]
    cof = lambda x, arr: float(np.interp(x, vgrid, arr[ok]))                   # noqa: E731
    iN = np.where(uu >= U2P + 0.1)[0]
    uN, RN, RuN = uu[iN], R[iN, 0], Ru[iN, 0]

    def cross(u0):
        """v at which the ray from (u0, 0) reaches R = a (inf if not by v = V1), and the symbol there"""
        R0 = float(np.interp(u0, uN, RN))
        L0 = math.log(-float(np.interp(u0, uN, RuN)))
        y, x, h = [R0, L0], 0.0, vv[-1] / steps
        for _ in range(steps):
            def f(t, z):
                e = cof(t, vhp) * math.exp(cof(t, psiIII))
                return [e * (1 - cof(t, muIII) / z[0]**2) / 2, e * cof(t, muIII) / z[0]**3 if redshift else 0.0]
            yn = rk4(f, y, x, x + h, 1)
            if yn[0] < AA:
                w = (y[0] - AA) / (y[0] - yn[0])
                xc = x + w * h
                Lc = y[1] + w * (yn[1] - y[1])
                return xc, math.exp(-cof(xc, psiIII) - Lc)
            y, x = yn, x + h
        return math.inf, None
    out = []
    for vt in npts:                                                             # bisection in u for the crossing v
        lo, hi = float(uN[0]), float(uN[-1])
        if not (cross(lo)[0] > vt > cross(hi)[0]):
            out.append((vt, None))
            continue
        for _ in range(40):
            mid = (lo + hi) / 2
            if cross(mid)[0] > vt:
                lo = mid
            else:
                hi = mid
        out.append((vt, cross(hi)[1]))
    return out


def main():
    ok = {}
    gk, gctl = g1()
    ok['G1'] = all(gk.values()) and gctl
    print('  G1: (a) mass fluxes %s, (b) ingoing and outgoing Vaidya off the other dust %s, (c) mu_uv, R_uv, s_uv %s, '
          '(d) trapping kept along outgoing rays where A = 0 %s; control (B depending on v) fails as it must: %s'
          % (gk['a'], gk['b'], gk['c'], gk['d'], gctl), flush=True)
    res = {}
    for n in (40, 80, 160):
        r = measure(n)
        res[n] = r
        print('    n = %d: mu0 = %.5f, outer mass after the shell %.4f; structure errors (I, III, before, after) %s; '
              'min(mu - mu0) on R >= a %.2e; R = a: %d of %d columns v <= 2, trapped %s, min mu - a^2 %.4f; '
              'mu_III >= %.5f; '
              'past-closedness '
              'margin %.2e; diamond: min R %.3f, untrapped %s, max mu %.4f; Sigma_tau0: packet at R in [%.3f, %.3f], '
              'horizon %.3f, shell from R = %.3f (rule %s); |g^-1(dvhat, du)| in [%.4f, %.4f] where R^2 >= 1.5 mu, '
              'least %.4f over every computed cell, on R = a at v = 0.5, 1, 1.5: %s'
              % (n, r['mu0'], r['muend'], ' '.join('%.1e' % x for x in r['struct']), r['minmu'], *r['inner'],
                 r['muIII'], r['pastc'], *r['diamond'], *r['sigma'], *r['symbol'][:3],
                 ' '.join('%.4f' % x for x in r['symbol'][3])), flush=True)
    s40, s80, s160 = (np.array(res[n]['struct']) for n in (40, 80, 160))
    struct = bool(np.all(s160 < s80) and np.all(s80 < s40) and np.all(s160 < 2e-2))
    m4, m8, m16 = (res[n]['minmu'] for n in (40, 80, 160))
    massb = m16 > -5e-3 and (m16 >= 0 or (m8 / m16 > 3 and m4 / m8 > 3))       # >= 0, or a deficit falling at order 2
    inner = all(res[n]['inner'][0] == res[n]['inner'][1] and res[n]['inner'][2] and
                res[n]['inner'][3] > res[n]['mu0'] - AA**2 - 2e-2 and res[n]['muIII'] > res[n]['mu0'] - 2e-3
                for n in (80, 160))
    pastc = res[160]['pastc'] > -2e-3
    diam = res[160]['diamond'][1] and res[160]['diamond'][0] > AA
    lo, hi, hor, sh, rule = res[160]['sigma']
    sig = hor < lo and hi < sh and rule
    s8, s16 = res[80]['symbol'], res[160]['symbol']
    symb = (s16[0] > 0 and abs(s16[0] - s8[0]) < 0.1 * s16[0]
            and all(abs(x - y) < 0.01 * y for x, y in zip(s8[3], s16[3]))
            and all(x > y > 0 for x, y in zip(s16[3][:-1], s16[3][1:])))
    ok['G2'] = struct and massb and inner and pastc and diam and sig and symb
    print('  G2: structure (Vaidya off the diamond, errors falling) %s; mu >= mu0 %s; R = a trapped with mu > a^2 %s; '
          'past-closed %s; diamond untrapped above R = a %s; Sigma_tau0 as stated %s; mixed symbol bounded below %s'
          % (struct, massb, inner, pastc, diam, sig, symb), flush=True)
    # G3: the outer data cone (round 2, the verifier's item 1)
    r3 = g3(res[160]['grid'])
    g3ok = r3['seed'] and r3['ex'][0] < 0 and r3['new'][0] >= 1.0 and r3['new'][1] >= 1.0 - 1e-9
    print('  G3: the domain (T = 1, delta0 = 0.05, so l5 = %.4f with the seed condition %s): V = %.3f, tau_end <= %.3f,\n'
          '      b(tau0) = %.3f. The example\'s own N (u0 = 0, R = 5 at v = 0) meets Sigma_tau0 at R - b = %.3f: inside\n'
          '      the domain, the verifier\'s case (rejected, as it must be). Moving N out inside region I (explicit\n'
          '      ingoing Vaidya, the same solution there): from R = %.3f at v = 0 the cone has R - b >= %.3f on all of\n'
          '      [tau0, tau_end] (%.3f at tau0): N cap {tau >= tau0} lies in {R > b(tau)}: %s'
          % (r3['l5'], r3['seed'], r3['V'], r3['tau_end'], r3['b0'], r3['ex'][0], r3['R0new'], r3['new'][1],
             r3['new'][0], g3ok), flush=True)
    ok['G3'] = g3ok
    # G4: the mixed symbol on R = a, resolved along region III's rays (round 2, the verifier's nit 5)
    least = [res[n]['symbol'][2] for n in (40, 80, 160)]
    r4 = {n: g4(res[n]['grid']) for n in (80, 160)}
    r4c = g4(res[160]['grid'], redshift=False, npts=(0.5, 1.0, 1.5))
    grid_ona = res[160]['symbol'][3]
    val = [x for _, x in r4[160]]
    agree = all(abs(r4[160][i][1] - grid_ona[i]) < 0.01 * grid_ona[i] for i in range(3))
    conv = all(x is not None and y is not None and abs(x - y) < 0.02 * y for (_, x), (_, y) in zip(r4[80], r4[160]))
    mono = all(x is not None and x > 0 for x in val) and all(x > y for x, y in zip(val[:-1], val[1:]))
    rates = [math.log(val[i] / val[i + 1]) / (r4[160][i + 1][0] - r4[160][i][0]) for i in range(len(val) - 1)]
    ctl4 = all(abs(x - y) < 0.05 * y for (_, x), y in zip(r4c, grid_ona))
    mu_max = max(res[160]['muend'], res[160]['mu0'])
    print('  G4: least |g^-1(dvhat, du)| over every computed cell with R >= a: %s at n = 40, 80, 160: NOT converged\n'
          '      (each finer grid reaches further into the late-v strip near R = a, where the grid thins). Resolved on\n'
          '      R = a by region III\'s rays (n = 160 coefficients): %s;\n'
          '      agrees with the grid at v = 0.5, 1, 1.5 to 1 %%: %s; n = 80 vs 160 coefficients agree to 2 %%: %s;\n'
          '      positive and decreasing in v: %s; decay rate per unit v %s (redshift; the analytic bound\n'
          '      d ln(sym)/dvhat >= -psi\' - mu_max/a^3 = -psi\' - %.2f on R >= a gives a positive lower bound on Omega)'
          % (' '.join('%.4f' % x for x in least),
             ' '.join('v = %.1f: %.3e' % (vt, x) for vt, x in r4[160]), agree, conv, mono,
             ' '.join('%.2f' % x for x in rates), mu_max / AA**3), flush=True)
    print('  G4 control: the same rays without the redshift term (d ln|R_u|/dv := 0) give %s on R = a at v = 0.5, 1,\n'
          '      1.5 against the grid\'s %s: agreement %s (it must fail)'
          % (' '.join('%.4f' % x for _, x in r4c), ' '.join('%.4f' % x for x in grid_ona), ctl4), flush=True)
    ok['G4'] = agree and conv and mono and not ctl4
    # G5: the packet stays outside the background horizon band (item 6)
    gaps = {n: res[n]['gap6'] for n in (40, 80, 160)}
    g5 = all(g[0] > 0.1 and g[2] for g in gaps.values()) and abs(gaps[160][0] - gaps[80][0]) < 0.02 * gaps[160][0]
    print('  G5: min over v <= 5 of R(u2, v) - sqrt(mu_III(v)) (the packet\'s inner edge against its columns\'\n'
          '      background horizon), at n = 40, 80, 160: %s (attained at v = %s); the inner edge untrapped\n'
          '      (R_v > 0) at every v: %s; positive and converged: %s'
          % (' '.join('%.4f' % g[0] for g in gaps.values()), ' '.join('%.2f' % g[1] for g in gaps.values()),
             all(g[2] for g in gaps.values()), g5), flush=True)
    ok['G5'] = g5
    c = {n: measure(n, sign=-1.0)['minmu'] for n in (40, 80)}
    ctl = c[80] < -0.05 and abs(c[80] - c[40]) < 0.2 * abs(c[80])
    print('  control (B -> -B): min(mu - mu0) = %.4f (n = 40), %.4f (n = 80): the bound fails, not a discretisation '
          'effect: %s' % (c[40], c[80], ctl), flush=True)
    ok['control'] = ctl
    global AAMP
    keep, AAMP = AAMP, 7.0
    hv = {n: measure(n)['gap6'] for n in (40, 80)}
    AAMP = keep
    ctl5 = all(g[0] < 0 for g in hv.values())
    print('  G5 control (a heavier shell, amplitude 7 for 3.6): the gap is %s at n = 40, 80: the packet is trapped by\n'
          '      the shell and crosses its columns\' horizon band, so G5 fails for it: %s'
          % (' '.join('%.4f' % g[0] for g in hv.values()), ctl5), flush=True)
    ok['G5 control'] = ctl5
    for k, v in ok.items():
        print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
