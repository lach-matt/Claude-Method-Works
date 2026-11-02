#!/usr/bin/env python3
"""cplate5.py -- CERTIFY-10L5-RESULT.md round 2 (R): the constraint-preserving runs of the late region against the free
ones.  Labels: computed (floating point).

cpsolve5.py imposes the Raychaudhuri constraint Ric_vv = 0 along every outgoing generator and drops Ric_xx, which it
monitors (field cx); its principal part has no Jordan block (symbol5.py Y2).  Runs: seed 1, cut 0.9, ld 3, M = 32,
v <= 2.25, at 400 x 180 and 800 x 360 (dnsolve5's grid numbers); the free runs are the record's (D432) at M = 32,
800 x 360 and 1600 x 720.  Compared per v-band on the coarse cells all runs keep, at least Nu/40 rows from the cut, by
areal radius class (r_A >= 1.2; 1.0 <= r_A < 1.2; 0.9 <= r_A < 1.0), in the metric's value P (the field the record
compares, D432), and in the monitored Ric_xx.

  E1 the constraint-preserving scheme in the null step: max |P_400 - P_800| per band (its own (u, v) error), and
     max |Ric_xx monitor| at both grids with their ratio (4 = second order).
  E2 the two formulations against each other: max |P_cp,800 - P_free,800| per band, beside the free scheme's own null-
     step difference max |P_free,800 - P_free,1600| (D432).  Where both converge they must agree within their errors.
  Claim (PASS/FAIL): on every band below v = 1.8 and r_A >= 1.0, |P_cp - P_free| at 800 rows is at most 3 times the
     larger of the two schemes' own null-step differences, and the Ric_xx monitor falls at least threefold from 400 to
     800 rows: one solution, two formulations.  Reported beyond v = 1.8.
  Control: the same E2 comparison against the record's free run at amplitude 7/8 (D445, M = 32, 800 x 360, ld 3), a
     different solution, must exceed that bound on some band below v = 1.8.

  python3 checks/cplate5.py CPDIR FREEDIR
"""
import os, sys, warnings
import numpy as np
warnings.filterwarnings('ignore')
BANDS = [(0.5, 1.0), (1.0, 1.5), (1.5, 1.65), (1.65, 1.8), (1.8, 1.9), (1.9, 2.0), (2.0, 2.25)]
CLASSES = [('r_A >= 1.2', 1.2, 99.0), ('1.0 <= r_A < 1.2', 1.0, 1.2), ('0.9 <= r_A < 1.0', 0.9, 1.0)]


def load(path, nv=None, step=1, cx=False):
    Z = np.load(path)
    x = Z['x']; M = len(x)
    sl = (slice(None, None, step), slice(None, (nv - 1) * step + 1 if nv else None, step))
    mask = Z['mask'][sl]
    m, n, R = Z['m'][sl], Z['n'][sl], Z['R'][sl]
    P = (2 * (1 + x) * m - (1 - x) * n) / 3
    rA = (np.nansum(R ** 3 * (np.pi / M * np.sqrt(1 - x ** 2)), -1) / 2) ** (1 / 3)
    ok = ~mask
    Nu = mask.shape[0]
    last = np.array([np.nonzero(ok[:, j])[0].max() if ok[:, j].any() else -1 for j in range(mask.shape[1])])
    far = np.zeros_like(ok)
    for j in range(mask.shape[1]):
        far[:max(last[j] - (Nu - 1) // 40 + 1, 0), j] = True
    out = dict(P=P, rA=rA, sel=ok & far, v=Z['v'][sl[1]])
    if cx:
        out['cx'] = np.nanmax(np.abs(Z['cx'][sl]), -1)
    return out


def bmax(A, sel, v, band, rA, cls):
    s = sel & ((v >= band[0]) & (v < band[1]))[None, :] & (rA >= cls[1]) & (rA < cls[2])
    a = A[s]; a = a[np.isfinite(a)]
    return float(a.max()) if a.size else np.nan


def main():
    cpd, frd = sys.argv[1], sys.argv[2]
    c8 = load(os.path.join(cpd, 'cp_M32_800.npz'), cx=True)
    nv = len(c8['v'])
    c4 = load(os.path.join(cpd, 'cp_M32_400.npz'), cx=True)
    f8 = load(os.path.join(frd, 'l1_rc0.9_M32.npz'), nv=nv)
    f16 = load(os.path.join(frd, 'l1_rc0.9_M32_1600.npz'), nv=nv, step=2)
    a8 = load(os.path.join(frd, 'ld3', 'amp0.875_M32.npz'), nv=nv)
    v = c8['v']; rA = c8['rA']
    # the 400-row run on the 800 grid's even nodes: compare at the coarse cells
    sel_c = c4['sel'] & c8['sel'][::2, ::2] & f8['sel'][::2, ::2] & f16['sel'][::2, ::2]
    sel = c8['sel'] & f8['sel'] & f16['sel']
    ok = True
    for cls in CLASSES:
        print('%s:' % cls[0], flush=True)
        for b in BANDS:
            e_cp = bmax(np.nanmax(np.abs(c4['P'] - c8['P'][::2, ::2]), -1), sel_c, v[::2], b, rA[::2, ::2], cls)
            e_fr = bmax(np.nanmax(np.abs(f8['P'] - f16['P']), -1), sel, v, b, rA, cls)
            d = bmax(np.nanmax(np.abs(c8['P'] - f8['P']), -1), sel, v, b, rA, cls)
            dc = bmax(np.nanmax(np.abs(c8['P'] - a8['P']), -1), sel & a8['sel'], v, b, rA, cls)
            x4 = bmax(c4['cx'], sel_c, v[::2], b, rA[::2, ::2], cls); x8 = bmax(c8['cx'][::2, ::2], sel_c, v[::2], b,
                                                                               rA[::2, ::2], cls)
            print('   v in [%.2f, %.2f): E1 cp null step |dP| %.2e; Ric_xx monitor %.2e -> %.2e (ratio %.2f);'
                  ' E2 |P_cp - P_free| %.2e, free null step %.2e; control (amplitude 7/8) %.2e' % (
                      *b, e_cp, x4, x8, x4 / x8 if x8 > 0 else np.nan, d, e_fr, dc), flush=True)
            if b[1] <= 1.8 and cls[1] >= 1.0:
                bound = 3 * max(e_cp, e_fr)
                good = d <= bound and x4 / x8 >= 3
                ctl = dc > bound
                ok &= good
                if not good:
                    print('      claim fails here', flush=True)
                if b == (1.0, 1.5) and cls[1] == 1.2:
                    ctl_any = ctl
                elif b[1] <= 1.8 and cls[1] >= 1.0:
                    ctl_any = ctl_any or ctl
    print('claim (one solution, two formulations, v < 1.8, r_A >= 1.0):', 'PASS' if ok else 'FAIL')
    print('control (amplitude 7/8 exceeds the bound somewhere):', 'fails (good)' if ctl_any else 'passed (bad)')
    ok &= ctl_any
    print('cplate5:', 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
