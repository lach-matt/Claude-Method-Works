#!/usr/bin/env python3
"""twodomainx5.py -- the two-dust background on a rectangle reaching Sigma_tau0 (verifier 259's item 7, D605;
FAMILIES5.md section 4c, "the background on Omega beyond the computed rectangle, which does not reach Sigma_tau0
(outgoing rays from R = a leave it through v = 0 at tau between -0.96 and -0.69, above the tau0 < -1.47 ...)").

checks/twodomain5.py D3b computes the seeded hole (corner mass mu0 = 1 at R = 4, an ingoing pulse A = sin^4 on v in
[0.5, 2], an outgoing one B = 0.4 sin^4 on u in [1, 2] posed on the cone v = 0) on u in [0, 8], v in [0, 2], with tau
:= vhat - R, vhat fixed by psi = 0 on the outer cone u = 0 (twodomain5 D1-D2), a = 0.7. The figures above were a
verifier's probe and no program computed them. Here:

  X1 (computed, floating point) the probe banked: along each v-column the last cell with R >= a (the inner boundary),
     the outgoing ray u = const through it meets v = 0 at tau = vhat(0) - R(u, 0), vhat(0) := 0; over the columns tau
     lies in [-0.960, -0.702] at n = 160 (FAMILIES5.md: -0.96 to -0.69, the verifier's probe at n = 320).
  X2 (computed) the rectangle moved down: the outgoing pulse's cone placed at v = V0 = -1 (the same pulse, the corner
     data continued down the ingoing cone, R = 4 + v/2 there), v in [-1, 1.5], u in [0, 8] with cells of R <= 0.3 left
     out as in twodomain5 D3b (v is stopped at 1.5: beyond it the strip between the horizon and the singularity thins
     and the coarse grids do not resolve it, twodomain5's own limit). Every outgoing ray from R = a now leaves through v
     = V0 at tau <= -1.5 (printed), below the -1.47 quoted, so the rectangle covers {R >= a} down to Sigma_-1.5.
     Convergence at n = 40, 80, 160 of the constraint residuals on R >= a (the evolution alone is solved, so they
     measure the error): their median and 90th percentile fall by 3 to 5 per halving (second order); their maximum sits
     at the steep inner boundary, where R_u is large, and converges more slowly there, as twodomain5 records for its own
     rectangle (printed with the maximum over R >= 1). The exit-tau range and min mu - a^2 on R = a move by less than
     10^-2 between n = 80 and 160, and every inner-boundary cell is trapped with mu > a^2.
  Control: the outgoing data with B's amplitude doubled on the cone, the residual measured with the old B (data off the
     constraint): the C_u residuals do not fall with n.

Reach: the outgoing family's characteristic data on v = V0 are a choice (the same pulse moved), not the record's, whose
outgoing data come from Sigma_tau0 or past null infinity (FAMILIES5.md section 4c); this computes the background on a
rectangle reaching Sigma_-1.5 for such data, converging at second order away from the steep inner boundary, and decides
nothing about which data the
problem poses. Labels: computed (floating point).

Run: python3 checks/twodomainx5.py   (a few minutes)
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import twodomain5 as T                                                          # noqa: E402

A0 = lambda x: T.bump(x, 0.5, 2.0)                                              # noqa: E731
B0 = lambda x: 0.4*T.bump(x, 1.0, 2.0)                                          # noqa: E731
AA = 0.7


def run(n, V0, U1=8.0, V1=2.0, Bdata=None):
    """twodomain5.solve with the corner at (0, V0), v in [V0, V1]; returns u, v (true), R, S"""
    Bdata = Bdata or B0
    A = lambda x: A0(x + V0)                                                    # noqa: E731
    uu, vv, R, S = T.solve(n, A, Bdata, mu0=1.0, R0=4.0 + V0/2, U1=U1, V1=V1 - V0)
    return uu, vv + V0, R, S


def corner_u(V0, V1=2.0, Rc=0.62):
    """twodomain5's rule: the last u at which R(u, V1) >= Rc, at n = 160"""
    uu, vv, R, S = run(160, V0, 8.0, V1)
    col = R[:, -1]
    return float(uu[np.where(np.isfinite(col) & (col >= Rc))[0][-1]])


def residuals(uu, vv, R, S, Bcon=None, Rcut=AA):
    """|C_u|, |C_v| on the cells whose stencil lies in R >= Rcut: (median, 90 %, 99 %, max) of each, and the max over
    R >= 1"""
    Bcon = Bcon or B0
    du, dv = uu[1] - uu[0], vv[1] - vv[0]
    with np.errstate(invalid="ignore"):
        Cu = ((R[2:, :] - 2*R[1:-1, :] + R[:-2, :])/du**2 - 2*(S[2:, :] - S[:-2, :])/(2*du)*(R[2:, :] - R[:-2, :])/(2*du)
              + Bcon(uu[1:-1])[:, None]/(3*R[1:-1, :]**2))
        Cv = ((R[:, 2:] - 2*R[:, 1:-1] + R[:, :-2])/dv**2 - 2*(S[:, 2:] - S[:, :-2])/(2*dv)*(R[:, 2:] - R[:, :-2])/(2*dv)
              + A0(vv[1:-1])[None, :]/(3*R[:, 1:-1]**2))
        ku = np.isfinite(Cu) & (R[1:-1, :] >= Rcut) & (R[2:, :] >= Rcut) & (R[:-2, :] >= Rcut)
        kv = np.isfinite(Cv) & (R[:, 1:-1] >= Rcut) & (R[:, 2:] >= Rcut) & (R[:, :-2] >= Rcut)
        ku1 = ku & (R[1:-1, :] >= 1.0)
    out = []
    for C, k in ((Cu, ku), (Cv, kv)):
        a = np.abs(C[k])
        out.append(tuple(np.percentile(a, [50, 90, 99])) + (float(a.max()),))
    return out[0], out[1], float(np.abs(Cu[ku1]).max())


def exits(uu, vv, R, S, a=AA):
    """the inner boundary R = a per v-column, the exit tau of its outgoing ray at the lower edge, mu - a^2, trapping"""
    du, dv = uu[1] - uu[0], vv[1] - vv[0]
    Ru = np.gradient(R, du, axis=0, edge_order=2)
    Rv = np.gradient(R, dv, axis=1, edge_order=2)
    mu = R**2*(1 + 2*np.exp(-2*S)*Ru*Rv)
    vhp = -np.exp(2*S[0])/Ru[0]                                                 # vhat' on u = 0 (psi = 0 there)
    vh = np.concatenate([[0.0], np.cumsum((vhp[1:] + vhp[:-1])/2*dv)])
    j0 = int(np.argmin(np.abs(vv)))                                              # normalise vhat = 0 at v = 0
    vh = vh - vh[j0]
    taus, mua, trapped = [], [], True
    for j in range(R.shape[1]):
        idx = np.where(np.isfinite(R[:, j]) & (R[:, j] < a))[0]
        if len(idx) == 0 or idx[0] < 2 or not np.isfinite(mu[idx[0] - 1, j]):
            continue
        i = idx[0] - 1
        taus.append(vh[0] - R[i, 0])
        mua.append(mu[i, j] - a*a)
        trapped &= bool(Rv[i, j] < 0)
    return min(taus), max(taus), min(mua), trapped, len(taus), R.shape[1]


def x1(control=False):
    if control:
        return False
    out = {}
    for n in (80, 160):
        out[n] = exits(*run(n, 0.0))
    lo, hi = out[160][0], out[160][1]
    print("  X1: the rectangle v in [0, 2], u in [0, 8]: exit tau of the outgoing rays from R = a in [%.3f, %.3f] (n ="
          " 80), [%.3f, %.3f] (n = 160)" % (out[80][0], out[80][1], lo, hi), flush=True)
    return abs(lo + 0.96) < 0.03 and abs(hi + 0.69) < 0.03


def x2(control=False, V0=-1.0, V1=1.5):
    U1 = 8.0
    if control:
        Bd = lambda x: 0.8*T.bump(x, 1.0, 2.0)                                  # noqa: E731
        r = [residuals(*run(n, V0, U1, V1, Bdata=Bd), Bcon=B0)[0][1] for n in (40, 80)]
        return r[1] < r[0]/3
    res, ex = {}, {}
    for n in (40, 80, 160):
        sol = run(n, V0, U1, V1)
        res[n] = residuals(*sol)
        ex[n] = exits(*sol)
        cu, cv, cu1 = res[n]
        print("    n = %d: |C_u| median %.2e, 90%% %.2e, 99%% %.2e, max %.2e (max over R >= 1: %.2e); |C_v| median %.2e,"
              " 90%% %.2e, max %.2e; exit tau in [%.4f, %.4f] over %d of %d columns; min mu - a^2 %.4f; trapped %s"
              % (n, cu[0], cu[1], cu[2], cu[3], cu1, cv[0], cv[1], cv[3], ex[n][0], ex[n][1], ex[n][4], ex[n][5],
                 ex[n][2], ex[n][3]), flush=True)
    q = [res[40][0][k]/res[80][0][k] for k in (0, 1)] + [res[80][0][k]/res[160][0][k] for k in (0, 1)]
    qv = [res[40][1][k]/res[80][1][k] for k in (0, 1)] + [res[80][1][k]/res[160][1][k] for k in (0, 1)]
    conv = all(3.0 < x < 5.0 for x in q + qv)
    stable = all(abs(ex[80][k] - ex[160][k]) < 1e-2 for k in (0, 1, 2))
    reach = ex[160][1] <= -1.5
    inner = ex[160][3] and ex[160][2] > 0
    print("  X2: V0 = %g, u in [0, %.3f] (cells with R <= 0.3 left out), v in [%g, %g]: median and 90 %% residual ratios"
          " per halving %s (C_u), %s (C_v): second order %s; exit tau at most %.3f <= -1.5: %s; exit range and min mu -"
          " a^2 stable to 10^-2 between n = 80 and 160: %s; inner boundary trapped with mu > a^2: %s"
          % (V0, U1, V0, V1, " ".join("%.2f" % x for x in q), " ".join("%.2f" % x for x in qv), conv, ex[160][1], reach,
             stable, inner), flush=True)
    return conv and reach and stable and inner


CHECKS = [("X1", x1), ("X2", x2)]


def main():
    ok = True
    for name, f in CHECKS:
        good = f()
        ctl = f(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
