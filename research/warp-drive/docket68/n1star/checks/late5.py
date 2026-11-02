#!/usr/bin/env python3
"""late5.py -- CERTIFY-10L5-RESULT.md section 3: the late region of the first seed against two exact properties of every
vacuum solution in dnsolve5.py's gauge.  Labels: computed (floating point) on double-null runs; the properties are
sectexp5.py X1 (exact).

  L1 the Raychaudhuri constraint.  dnsolve5 evolves Ric_11, Ric_22, Ric_xx, Ric(Y, d_v) and Ric_vx and never imposes
     Ric_vv; on a vacuum solution it vanishes.  rho := R_vv - 2 W_v R_v + (R/3)(P_v^2 + Q_v^2 + (P_v + Q_v)^2) (= -(R/3)
     Ric_vv, sectexp5.py X1), by centred differences in v, over kept cells at least k rows from the cut (k = Nu/40),
     per v-band; scaled by the size of its largest term, |R_vv| + |2 W_v R_v| + (R/3) shear.  Reported per band at
     each resolution, with the ratio between successive resolutions (4 = second order).
  L2 the monotone quantity.  e^{-2W} R_v is nonincreasing along every outgoing generator of a vacuum solution
     (X1).  Its largest increase between successive v-nodes, over the same cells, per band, scaled by its own size.
  L3 gauge indicators where L1-L2 fail: the largest |W| and P + Q (Gx ~ e^{-2(P+Q)}: a caustic of the outgoing cones
     would send Gx to 0) per band.
  Control (L1): the same residual with the coefficient 2 W_v replaced by W_v does not converge (ratio below 2 in the
  bands where L1's converges), so L1 is not a smoothness test that any field passes.

  python3 checks/late5.py RUNDIR run_coarse run_mid run_fine
"""
import os, sys, warnings
import numpy as np
warnings.filterwarnings('ignore')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import bondisph5 as B                                                           # noqa: E402

BANDS = [(0.5, 1.0), (1.0, 1.5), (1.5, 1.65), (1.65, 1.8), (1.8, 1.9), (1.9, 1.975)]


def fields(Z, kfac=40, wcoef=2.0):
    u, v, x, mask = Z['u'], Z['v'], Z['x'], Z['mask']
    dv = v[1] - v[0]
    R, W, m, n = [np.where(mask[..., None], np.nan, Z[k]) for k in ('R', 'W', 'm', 'n')]
    P = (2 * (1 + x) * m - (1 - x) * n) / 3; Q = (2 * (1 - x) * n - (1 + x) * m) / 3
    d1 = lambda A: (A[:, 2:] - A[:, :-2]) / (2 * dv)
    d2 = lambda A: (A[:, 2:] - 2 * A[:, 1:-1] + A[:, :-2]) / dv ** 2
    Rv, Rvv, Wv, Pv, Qv = d1(R), d2(R), d1(W), d1(P), d1(Q)
    Rc = R[:, 1:-1]
    sh = Pv ** 2 + Qv ** 2 + (Pv + Qv) ** 2
    rho = Rvv - wcoef * Wv * Rv + Rc / 3 * sh
    scale = np.abs(Rvv) + np.abs(2 * Wv * Rv) + Rc / 3 * sh
    q = np.exp(-2 * W) * np.where(np.isfinite(R), (np.roll(R, -1, 1) - np.roll(R, 1, 1)) / (2 * dv), np.nan)
    q[:, 0] = np.nan; q[:, -1] = np.nan
    inc = np.full_like(q, np.nan); inc[:, 1:] = q[:, 1:] - q[:, :-1]
    ok = ~mask
    last = np.array([np.nonzero(ok[:, j])[0].max() if ok[:, j].any() else -1 for j in range(len(v))])
    k = (len(u) - 1) // kfac
    far = np.zeros_like(ok)
    for j in range(len(v)):
        far[:max(last[j] - k + 1, 0), j] = True
    return dict(v=v[1:-1], rho=rho, scale=scale, far=far[:, 1:-1], inc=inc[:, 1:-1], q=q[:, 1:-1], W=W[:, 1:-1],
                PQ=(P + Q)[:, 1:-1], u=u)


def band_max(F, key, band, rel=None):
    sel = (F['v'] >= band[0]) & (F['v'] < band[1])
    A = F[key][:, sel]
    msk = F['far'][:, sel][..., None] & np.isfinite(A)
    if rel is not None:
        A = np.abs(A) / np.maximum(np.abs(F[rel][:, sel]), 1e-12)
    vals = np.abs(A)[msk]
    return float(vals.max()) if vals.size else np.nan


def common(Fs, key, band):
    """max of |key| over the coarse grid's points, each run sampled at the coarse nodes (nested grids)"""
    out = []
    for lvl, F in enumerate(Fs):
        s = 2 ** lvl
        sub = {kk: (vv[::s, ::s] if isinstance(vv, np.ndarray) and vv.ndim >= 2 else vv) for kk, vv in F.items()}
        sub['v'] = F['v'][::s] if s > 1 else F['v']
        out.append(band_max(sub, key, band))
    return out


def main():
    rundir, names = sys.argv[1], sys.argv[2:5]
    Zs = [B.load(os.path.join(rundir, nm + '.npz')) for nm in names]
    ok = True
    for wcoef, label in ((2.0, 'L1 rho'), (1.0, 'control (W_v in place of 2 W_v)')):
        Fs = [fields(Z, wcoef=wcoef) for Z in Zs]
        print('%s: max |rho| per band, at %s (coarse nodes of each run)' % (label, ', '.join(names)), flush=True)
        conv = []
        for band in BANDS:
            # the v-nodes of the runs nest: run l has 2^l columns per coarse column; centred stencils are shifted by
            # one fine column, so compare band maxima rather than node values
            m = [band_max(F, 'rho', band) for F in Fs]
            sc = band_max(Fs[-1], 'scale', band)
            r1 = m[0] / m[1] if m[1] > 0 else np.nan
            r2 = m[1] / m[2] if m[2] > 0 else np.nan
            conv.append((band, r1, r2))
            print('   v in [%.3f, %.3f): %s  ratios %.2f %.2f   (largest term on the fine run %.2e)' % (
                band[0], band[1], '  '.join('%.2e' % a for a in m), r1, r2, sc), flush=True)
        if wcoef == 2.0:
            good = all(r2 > 3 for band, r1, r2 in conv if band[1] <= 1.65)
            ok &= good
            print('   L1 second order (fine ratio > 3) on every band before v = 1.65: %s' % good)
            l1conv = conv
        else:
            ctl = all(r2 > 3 for band, r1, r2 in conv if band[1] <= 1.65)
            print('   control converges at second order before v = 1.65: %s (must be False)' % ctl)
            ok &= not ctl
    F = fields(Zs[-1])
    print('L2 largest increase of e^{-2W} R_v between successive v-nodes along a generator, over its own size:')
    for band in BANDS:
        sel = (F['v'] >= band[0]) & (F['v'] < band[1])
        inc = F['inc'][:, sel]; qq = np.abs(F['q'][:, sel]); fr = F['far'][:, sel][..., None]
        good = fr & np.isfinite(inc)
        rel = np.where(good, inc / np.maximum(qq, 1e-3), -np.inf)
        print('   v in [%.3f, %.3f): max increase %.2e, relative %.2e' % (band[0], band[1],
                                                                       np.nanmax(np.where(good, inc, -np.inf)),
                                                                       rel.max()), flush=True)
    print('L3 gauge indicators on the fine run: max |W|, max (P + Q), min (P + Q) per band:')
    for band in BANDS:
        sel = (F['v'] >= band[0]) & (F['v'] < band[1])
        fr = F['far'][:, sel][..., None]
        W = np.where(fr, F['W'][:, sel], np.nan); PQ = np.where(fr, F['PQ'][:, sel], np.nan)
        print('   v in [%.3f, %.3f): %.3f %.3f %.3f' % (band[0], band[1], np.nanmax(np.abs(W)), np.nanmax(PQ),
                                                       np.nanmin(PQ)), flush=True)
    print('late5:', 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
