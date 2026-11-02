#!/usr/bin/env python3
"""late5b.py -- CERTIFY-10L5-RESULT.md round 2, the late region: late5.py's Raychaudhuri test (L1) and D1's monotone
quantity (L2) on the record's own finest free runs, refined in the null grid and in angle separately.  Labels: computed
(floating point) on double-null runs; the properties are sectexp5.py X1's (exact).

late5.py measured, at seed 1, M = 16 and 24, cut 0.3: from v ~ 1.65 the Raychaudhuri residual
    rho := R_vv - 2 W_v R_v + (R/3)(P_v^2 + Q_v^2 + (P_v + Q_v)^2) = -(R/3) Ric_vv
is as large as its own terms and does not fall with the null step.  This program asks whether that survives the
resolutions the record ran (CERTIFY-10L5.md D418, D432: dnsolve5.py --run 1 0.9 M 800 360 out 0 ld 3, M = 24-56, and
the same at 1600 x 720 for M = 32 and 40; and r_cut = 0.7 at M = 24 and 32, which keep the smaller radii where late5's
failure sat, with a 1600 x 720 run at r_cut = 0.7, M = 32, to v = 1.85 made here by szrun5.py).  rho by centred
differences in v at every node; reported per band as max |rho| and, in brackets, max |rho| over the largest term
|R_vv| + |2 W_v R_v| + (R/3) shear on the same cells (the band's scale); cells at least Nu/40 rows from the cut (the
same physical distance at both null grids); the cells classed by the areal radius r_A = (int R^3 dx / 2)^(1/3) of
their section.

  L5 the null step: at M = 32 and at M = 40, max |rho| per v-band and class on the coarse cells kept by both null
     grids, 800 x 360 and 1600 x 720; the ratio coarse/fine (4 = second order).
  L6 angle: max |rho| per band and class at M = 24, 32, 40, 48, 56 (800 x 360, cut 0.9), on the cells all five keep.
  L7 the small radii: max |rho| per band on 0.6 <= r_A < 0.9 at cut 0.7, M = 24 and 32 (800 x 360), its location, and
     the null step there (with --small): M = 32 at 800 x 360 against 1600 x 720 (to v = 1.85, szrun5.py) on the
     coarse cells both keep.
  L8 D1's monotone quantity q = e^{-2W} R_v along outgoing generators: its largest increase between successive v-nodes
     per band, over the band's max |q| (a vacuum solution has none), at M = 32 and 40, both null grids.
  Claim (PASS/FAIL on [1.65, 1.8) only): on [1.65, 1.8) and r_A >= 1.0, the null-step ratio of L5 is at least 3 at both
  M, and max |rho| is below 1e-2 of the band's largest term at 1600 x 720.
  Control (L5): rho with W_v in place of 2 W_v must not converge (ratio below 2) on [1, 1.5), where L5's does.

  python3 checks/late5b.py RUNDIR        (RUNDIR holding the record's l1_rc0.9_M*.npz and l1_rc0.7_M*.npz)
  python3 checks/late5b.py RUNDIR --small RUN1600.npz      (L7's null step, output checks/late5b_small.out)
"""
import os, sys, warnings
import numpy as np
warnings.filterwarnings('ignore')
BANDS = [(0.5, 1.0), (1.0, 1.5), (1.5, 1.65), (1.65, 1.8), (1.8, 1.9), (1.9, 2.0), (2.0, 2.25)]
CLASSES = [('r_A >= 1.2', 1.2, 99.0), ('1.0 <= r_A < 1.2', 1.0, 1.2), ('0.9 <= r_A < 1.0', 0.9, 1.0)]


def rho_run(path, wcoef=2.0, chunk=100):
    """rho/scale, rho, the monotone quantity's increase (relative), r_A, far-from-cut flags; on the run's own grid"""
    Z = np.load(path)
    u, v, x, mask = Z['u'], Z['v'], Z['x'], Z['mask']
    M = len(x); dv = v[1] - v[0]
    wq = np.pi / M * np.sqrt(1 - x ** 2)
    Nu, Nv = mask.shape
    out = {k: np.full((Nu, Nv), np.nan) for k in ('rel', 'abs', 'term', 'mono', 'qabs', 'rA')}
    ok = ~mask
    last = np.array([np.nonzero(ok[:, j])[0].max() if ok[:, j].any() else -1 for j in range(Nv)])
    k = (Nu - 1) // 40
    far = np.zeros_like(ok)
    for j in range(Nv):
        far[:max(last[j] - k + 1, 0), j] = True
    full = {f: Z[f] for f in ('R', 'W', 'm', 'n')}          # each decompressed once
    for i0 in range(0, Nu, chunk):
        sl = slice(i0, min(i0 + chunk, Nu))
        mk = mask[sl][..., None]
        R, W, m, n = [np.where(mk, np.nan, full[f][sl]) for f in ('R', 'W', 'm', 'n')]
        P = (2 * (1 + x) * m - (1 - x) * n) / 3; Q = (2 * (1 - x) * n - (1 + x) * m) / 3
        d1 = lambda A: (A[:, 2:] - A[:, :-2]) / (2 * dv)
        d2 = lambda A: (A[:, 2:] - 2 * A[:, 1:-1] + A[:, :-2]) / dv ** 2
        Rv, Rvv, Wv, Pv, Qv = d1(R), d2(R), d1(W), d1(P), d1(Q)
        Rc = R[:, 1:-1]
        sh = Pv ** 2 + Qv ** 2 + (Pv + Qv) ** 2
        rho = Rvv - wcoef * Wv * Rv + Rc / 3 * sh
        term = np.abs(Rvv) + np.abs(2 * Wv * Rv) + Rc / 3 * sh
        q = np.exp(-2 * W[:, 1:-1]) * Rv
        inc = np.full_like(q, np.nan); inc[:, 1:] = q[:, 1:] - q[:, :-1]
        out['abs'][sl, 1:-1] = np.nanmax(np.abs(rho), -1)
        out['term'][sl, 1:-1] = np.nanmax(term, -1)
        out['rel'][sl, 1:-1] = np.nanmax(np.abs(rho) / np.maximum(term, 1e-12), -1)
        out['mono'][sl, 1:-1] = np.nanmax(inc, -1)
        out['qabs'][sl, 1:-1] = np.nanmax(np.abs(q), -1)
        out['rA'][sl] = (np.nansum(R ** 3 * wq, -1) / 2) ** (1 / 3)
    del full
    out['far'] = far; out['ok'] = ok; out['u'] = u; out['v'] = v
    return out


def band_cls(F, sel, key, band, cls):
    v = F['v']
    vs = (v >= band[0]) & (v < band[1])
    s = sel & vs[None, :] & (F['rA'] >= cls[1]) & (F['rA'] < cls[2])
    vals = F[key][s]
    vals = vals[np.isfinite(vals)]
    return float(vals.max()) if vals.size else np.nan


def sub(F, s):
    return {k: (a[::s, ::s] if isinstance(a, np.ndarray) and a.ndim == 2 else (a[::s] if k in ('u', 'v') else a))
            for k, a in F.items()}


def main():
    D = sys.argv[1]
    if len(sys.argv) > 3 and sys.argv[2] == '--small':
        print('L7 the null step at the small radii (M = 32, cut 0.7; 800 x 360 against %s)' % sys.argv[3], flush=True)
        return small(D, sys.argv[3])
    ok = True
    print('L5 the null step: max |rho| per band (absolute; relative to its largest term in brackets), coarse cells kept'
          ' by both grids, >= Nu/40 rows from the cut', flush=True)
    claim = True
    for M in (32, 40):
        Fc = rho_run(os.path.join(D, 'l1_rc0.9_M%d.npz' % M))
        Ff = sub(rho_run(os.path.join(D, 'l1_rc0.9_M%d_1600.npz' % M)), 2)
        sel = Fc['far'] & Ff['far'] & Fc['ok'] & Ff['ok']
        for cls in CLASSES[:2]:
            print('  M = %d, %s:' % (M, cls[0]), flush=True)
            for b in BANDS:
                a, f_ = band_cls(Fc, sel, 'abs', b, cls), band_cls(Ff, sel, 'abs', b, cls)
                ra, rf = a / band_cls(Fc, sel, 'term', b, cls), f_ / band_cls(Ff, sel, 'term', b, cls)
                print('     v in [%.2f, %.2f): 800 %.2e (%.1e)  1600 %.2e (%.1e)  ratio %.2f' % (
                    *b, a, ra, f_, rf, a / f_ if f_ > 0 else np.nan), flush=True)
                if b == (1.65, 1.8) and cls[1] == 1.0:
                    claim &= (a / f_ >= 3) and (rf < 1e-2)
        if M == 32:
            Cc = rho_run(os.path.join(D, 'l1_rc0.9_M32.npz'), wcoef=1.0)
            Cf = sub(rho_run(os.path.join(D, 'l1_rc0.9_M32_1600.npz'), wcoef=1.0), 2)
            a = band_cls(Cc, sel, 'abs', (1.0, 1.5), CLASSES[0]); f_ = band_cls(Cf, sel, 'abs', (1.0, 1.5), CLASSES[0])
            ctl = a / f_ >= 2
            print('  control (W_v for 2 W_v), M = 32, [1, 1.5), r_A >= 1.2: %.2e -> %.2e, ratio %.2f -> %s' % (
                a, f_, a / f_, 'passed (bad)' if ctl else 'fails (good)'), flush=True)
            ok &= not ctl
            del Cc, Cf
        mono = []
        for F_ in (Fc, Ff):
            mono.append([band_cls(F_, sel, 'mono', b, CLASSES[1]) / band_cls(F_, sel, 'qabs', b, CLASSES[1])
                         for b in BANDS])
        print('  L8 M = %d, 1.0 <= r_A < 1.2: largest increase of e^{-2W} R_v over the band\'s max |e^{-2W} R_v|,'
              ' 800 / 1600: %s' % (M, '; '.join('%.1e / %.1e' % (p, q) for p, q in zip(*mono))), flush=True)
        del Fc, Ff
    print('L5 claim on [1.65, 1.8), r_A >= 1.0 (ratio >= 3 at M = 32 and 40, relative residual < 1e-2 at 1600):',
          'PASS' if claim else 'FAIL', flush=True)
    ok &= claim
    print('L6 angle (800 x 360, cut 0.9): max |rho| per band on the cells all of M = 24, 32, 40, 48, 56 keep', flush=True)
    Fs = {}
    for M in (24, 32, 40, 48, 56):
        p = os.path.join(D, 'l1_rc0.9_M%d.npz' % M)
        if os.path.exists(p):
            Fs[M] = rho_run(p)
    sel = np.logical_and.reduce([F_['far'] & F_['ok'] for F_ in Fs.values()])
    for cls in CLASSES[:2]:
        print('  %s:' % cls[0], flush=True)
        for b in BANDS:
            print('     v in [%.2f, %.2f): %s' % (*b, '  '.join('M%d %.2e' % (M, band_cls(F_, sel, 'abs', b, cls))
                                                         for M, F_ in Fs.items())), flush=True)
    del Fs
    print('L7 the small radii (cut 0.7, 800 x 360): max |rho| per band on 0.6 <= r_A < 0.9 (over the largest term)',
          flush=True)
    small = ('', 0.6, 0.9)
    for M in (24, 32):
        F_ = rho_run(os.path.join(D, 'l1_rc0.7_M%d.npz' % M))
        sel = F_['far'] & F_['ok']
        row = []
        for b in BANDS:
            a = band_cls(F_, sel, 'abs', b, small)
            row.append('%.2e (%.1e)' % (a, a / band_cls(F_, sel, 'term', b, small)))
        print('  M = %d: %s' % (M, '  '.join(row)), flush=True)
        vs = (F_['v'] >= 1.65) & (F_['v'] < 1.8)
        A = np.where(sel & vs[None, :] & (F_['rA'] < 0.9), F_['abs'], -1)
        i, j = np.unravel_index(np.argmax(A), A.shape)
        print('     largest on [1.65, 1.8): %.2e at u = %.4f, v = %.3f, r_A = %.3f' % (
            A[i, j], F_['u'][i], F_['v'][j], F_['rA'][i, j]), flush=True)
    print('late5b:', 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


def small(D, pf):
    """L7's null step at the small radii: M = 32, cut 0.7, 800 x 360 against 1600 x 720 (to v = 1.85)"""
    sm = ('', 0.6, 0.9)
    if True:
        Fc = rho_run(os.path.join(D, 'l1_rc0.7_M32.npz'))
        Ff = sub(rho_run(pf), 2)
        nv = Ff['abs'].shape[1]
        Fc = {k: (a[:, :nv] if isinstance(a, np.ndarray) and a.ndim == 2 else (a[:nv] if k == 'v' else a))
              for k, a in Fc.items()}
        sel = Fc['far'] & Ff['far'] & Fc['ok'] & Ff['ok']
        print('  null step at M = 32 (800 against 1600 rows), 0.6 <= r_A < 0.9 and 0.9 <= r_A < 1.0:', flush=True)
        for cls in (sm, CLASSES[2]):
            for b in BANDS[:5]:
                a, f_ = band_cls(Fc, sel, 'abs', b, cls), band_cls(Ff, sel, 'abs', b, cls)
                tf = band_cls(Ff, sel, 'term', b, cls)
                print('     %s, v in [%.2f, %.2f): 800 %.2e  1600 %.2e (%.1e of the largest term)  ratio %.2f' % (
                    cls[0] or '0.6 <= r_A < 0.9', *b, a, f_, f_ / tf, a / f_ if f_ > 0 else np.nan), flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
