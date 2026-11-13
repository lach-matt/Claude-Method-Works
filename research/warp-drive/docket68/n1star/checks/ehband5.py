#!/usr/bin/env python3
"""ehband5: vacuum bands of Part I's slice that meet the black-hole region where f > 0 (FAMILIES5-R11.md, R11.0;
FAMILIES5-MB.md's [R10] status note).

The argument (deduced). On Sigma_tau0 the seed region R < 1.861 lies in region III (u >= u2, v < 3), vacuum of mass
mu3, so R = sqrt(mu3) = 0.9067 is its apparent horizon: there f = 0, the outgoing ray through it has R_v = 0 and stays
at R = sqrt(mu3) until the ingoing shell (v in [3, 4.5]) arrives. lambda := e^(-2s) R_v obeys d_v lambda = -(R/3)
e^(-2s) T_vv-type term, proportional to -A <= 0 (the v-Raychaudhuri equation; twobg5's A >= 0), strictly negative where
A > 0. So that ray becomes trapped in the shell and, lambda never increasing again, stays trapped: it does not reach
infinity, and its starting point is in the black-hole region. Trappedness at v = 4.5 is an open condition in the
starting radius (continuous dependence of the rays), so the rays from R in (sqrt(mu3), sqrt(mu3) + delta) are trapped
too, for some delta > 0: those slice points lie in the black-hole region with f > 0. Theorem P applies to vacuum bands
there; Theorem X to bands meeting {f < 0}.

  H1 (computed, floating point, the computed background twobg5 at n = 80 and 160) the grid rows (outgoing rays u =
     const) crossing Sigma_tau0 at R in (sqrt(mu3), 1.2): R_v > 0 at the crossing (untrapped there, f > 0), and R_v at
     each row's last computed point (v = 5, or earlier where the row leaves the domain at its inner edge R = 0.3)
     negative for every row crossing below a radius R_x, positive above it. Once R_v < 0 it stays so (the argument
     above), so those rows are trapped for good. R_x estimates the event horizon's radius on the slice from below,
     the band (sqrt(mu3), R_x) is non-empty, and R_x is converged between n = 80 and 160.
  Control (must fail): the same with the ingoing shell removed (A = 0): every row crossing above sqrt(mu3) ends
     untrapped, so no such band.

Labels: the argument deduced; H1 computed (floating point; not certified). Run: python3 checks/ehband5.py   (minutes)
"""
import importlib.util
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + '.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


tb = load('twobg5')


def grid(n, shell=True):
    if shell:
        return tb.run(n)
    A = lambda x: 0.0 * tb.sbump(x, tb.V1S, tb.V2S)                                # noqa: E731
    B = lambda x: tb.BAMP * tb.sbump(x, tb.U1P, tb.U2P)                            # noqa: E731
    uu, vv, R, S = tb.TD.solve(n, A, B, mu0=tb.MUC, R0=tb.R0, U1=9.6, V1=5.0, Rmin=0.3)
    du, dv = uu[1] - uu[0], vv[1] - vv[0]
    Ru = np.gradient(R, du, axis=0, edge_order=2)
    Rv = np.gradient(R, dv, axis=1, edge_order=2)
    mu = R**2 * (1 + 2 * np.exp(-2 * S) * Ru * Rv)
    return uu, vv, R, S, Ru, Rv, mu


def rows(n, shell=True):
    uu, vv, R, S, Ru, Rv, mu = grid(n, shell)
    ia = uu >= tb.U2P + 0.1
    mu3 = float(np.nanmedian(mu[ia, 0][np.isfinite(mu[ia, 0])]))
    dv = vv[1] - vv[0]
    vhp = -np.exp(2 * S[0]) / Ru[0]
    vh = np.concatenate([[0.0], np.cumsum((vhp[1:] + vhp[:-1]) / 2 * dv)])
    tau0 = -tb.AA + 0.02
    out = []
    for i in range(len(uu)):
        if uu[i] < tb.U2P:
            continue
        tau = vh - R[i]
        m = np.isfinite(tau) & np.isfinite(Rv[i])
        if m.sum() < 3:
            continue
        j = np.where(m)[0]
        t = tau[m]
        k = np.searchsorted(t, tau0)
        if k == 0 or k >= len(t):
            continue
        j0, j1 = j[k - 1], j[k]
        w = (tau0 - tau[j0]) / (tau[j1] - tau[j0])
        Rc = (1 - w) * R[i, j0] + w * R[i, j1]
        Rvc = (1 - w) * Rv[i, j0] + w * Rv[i, j1]
        last = j[-1]
        out.append((Rc, Rvc, Rv[i, last], vv[last]))
    return mu3, np.array(out)


def h1(n, shell=True):
    mu3, o = rows(n, shell)
    rh = np.sqrt(mu3)
    sel = o[(o[:, 0] > rh) & (o[:, 0] < 1.2)]
    sel = sel[np.argsort(sel[:, 0])]
    untrapped_at_slice = bool(np.all(sel[:, 1] > 0))
    trapped = sel[sel[:, 2] < 0]
    free = sel[sel[:, 2] > 0]
    rx = float(trapped[:, 0].max()) if len(trapped) else float('nan')
    ordered = len(trapped) == 0 or len(free) == 0 or trapped[:, 0].max() < free[:, 0].min()
    return dict(mu3=mu3, rh=rh, n=len(sel), slice_ok=untrapped_at_slice, ntrap=len(trapped), rx=rx, ordered=ordered,
                vend=float(trapped[:, 3].min()) if len(trapped) else float('nan'),
                rfree=float(free[:, 0].min()) if len(free) else float('nan'))


def main():
    print("ehband5: the band sqrt(mu3) < R < R_EH of Part I's slice, on the computed background", flush=True)
    res = {}
    for n in (80, 160):
        r = h1(n)
        res[n] = r
        print("   n = %d: sqrt(mu3) = %.4f; %d rows cross Sigma_tau0 at R in (sqrt(mu3), 1.2), all untrapped there "
              "(R_v > 0): %s; %d of them end trapped (R_v < 0 at their last computed point, v >= %.2f), every one "
              "crossing below R_x = %.4f, the rest from %.4f up (ordered: %s)" %
              (n, r['rh'], r['n'], r['slice_ok'], r['ntrap'], r['vend'], r['rx'], r['rfree'], r['ordered']),
              flush=True)
    ok = all(r['slice_ok'] and r['ntrap'] > 0 and r['ordered'] for r in res.values())
    conv = abs(res[80]['rx'] - res[160]['rx']) < 0.02
    print("   the band (sqrt(mu3), R_x) is non-empty at both n, R_x = %.3f and %.3f (converged to 0.02: %s)"
          % (res[80]['rx'], res[160]['rx'], conv))
    c = h1(160, shell=False)
    ctl = c['ntrap'] == 0
    print("   control: without the ingoing shell (A = 0), %d of %d rows crossing above sqrt(mu3) end trapped (none, "
          "rejected): %s" % (c['ntrap'], c['n'], ctl))
    print("H1", "PASS" if ok and conv else "FAIL")
    print("control rejected:", "PASS" if ctl else "FAIL")
    return 0 if ok and conv and ctl else 1


if __name__ == '__main__':
    sys.exit(main())
