#!/usr/bin/env python3
"""cplate5c.py -- CERTIFY-10L5-RESULT.md round 3 (task 3): the constraint-preserving scheme on a third null grid in the
late region.  Labels: computed (floating point).

cplate5.py (round 2) compared the constraint-preserving runs (cpsolve5.py: Ric_vv imposed, Ric_xx dropped and
monitored as cx) at 400 x 180 and 800 x 360 with the record's free runs, and left open whether they converge from
v ~ 1.9 at areal radius 1.0-1.2 (CERTIFY-10L5-RESULT.md 6.4): two grids give no order.  Here the third grid,
1600 x 720 (seed 1, cut 0.9, ld 3, M = 32, v <= 2.25), is added.  Everything is compared on the 400-row run's nodes
(every second node of the 800-row run, every fourth of the 1600-row run) that all runs keep, at least Nu/40 rows from
the cut, per v-band and areal-radius class, in P (cplate5.py's field).

  C1 the null step, three grids: d1 = max |P_400 - P_800|, d2 = max |P_800 - P_1600| per band, and d1/d2 (4 = second
     order, 1 = no convergence).
  C2 the Ric_xx monitor (unimposed) at the three grids, max per band, and its ratios.
  C3 the two formulations at 1600 rows: max |P_cp - P_free| (the record's free run, D432), beside each scheme's own
     null-step difference (cp: d2; free: 800 against 1600).
  Verdict (reported, not gated) per band at 1.0 <= r_A < 1.2: "converges" if d1/d2 >= 3 and d2 < 1e-2, "not shown"
  otherwise.
  Control: C1 with the free run at amplitude 7/8 (D445, a different solution, M = 32, 800 x 360) in place of the 800-row
  cp run must not show convergence (d1/d2 < 3 on some band below v = 1.8): a ratio test that any pair of runs passes
  would mean nothing.

  python3 checks/cplate5c.py CPDIR CP1600 FREEDIR
"""
import os, sys, importlib.util, warnings
import numpy as np
warnings.filterwarnings('ignore')
HERE = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('cplate5', os.path.join(HERE, 'cplate5.py'))
C5 = importlib.util.module_from_spec(_s); _s.loader.exec_module(C5)
print = C5.print


def main():
    cpd, cp16p, frd = sys.argv[1], sys.argv[2], sys.argv[3]
    c4 = C5.load(os.path.join(cpd, 'cp_M32_400.npz'), cx=True)
    nv = len(c4['v'])
    c8 = C5.load(os.path.join(cpd, 'cp_M32_800.npz'), nv=nv, step=2, cx=True)
    c16 = C5.load(cp16p, nv=nv, step=4, cx=True)
    f8 = C5.load(os.path.join(frd, 'l1_rc0.9_M32.npz'), nv=nv, step=2)
    f16 = C5.load(os.path.join(frd, 'l1_rc0.9_M32_1600.npz'), nv=nv, step=4)
    a8 = C5.load(os.path.join(frd, 'ld3', 'amp0.875_M32.npz'), nv=nv, step=2)
    v, rA = c4['v'], c4['rA']
    sel = c4['sel'] & c8['sel'] & c16['sel'] & f8['sel'] & f16['sel']
    mx = lambda A, B: np.nanmax(np.abs(A - B), -1)
    ok = True
    ctl_hit = False
    verdict = []
    for cls in C5.CLASSES:
        print('%s:' % cls[0], flush=True)
        for b in C5.BANDS:
            d1 = C5.bmax(mx(c4['P'], c8['P']), sel, v, b, rA, cls)
            d2 = C5.bmax(mx(c8['P'], c16['P']), sel, v, b, rA, cls)
            x4, x8, x16 = (C5.bmax(c['cx'], sel, v, b, rA, cls) for c in (c4, c8, c16))
            dcf = C5.bmax(mx(c16['P'], f16['P']), sel, v, b, rA, cls)
            dfr = C5.bmax(mx(f8['P'], f16['P']), sel, v, b, rA, cls)
            ca = C5.bmax(mx(c4['P'], a8['P']), sel & a8['sel'], v, b, rA, cls)
            cb = C5.bmax(mx(a8['P'], c16['P']), sel & a8['sel'], v, b, rA, cls)
            r = d1 / d2 if d2 > 0 else np.nan
            print('   v in [%.2f, %.2f): C1 |dP| 400-800 %.2e, 800-1600 %.2e, ratio %.2f; C2 Ric_xx %.2e -> %.2e -> %.2e'
                  ' (%.1f, %.1f); C3 |P_cp - P_free| at 1600 %.2e, free 800-1600 %.2e; control ratio %.2f' % (
                      *b, d1, d2, r, x4, x8, x16, x4 / x8 if x8 > 0 else np.nan, x8 / x16 if x16 > 0 else np.nan,
                      dcf, dfr, ca / cb if cb > 0 else np.nan), flush=True)
            if b[1] <= 1.8 and cls[1] >= 1.0 and cb > 0 and ca / cb < 3:
                ctl_hit = True
            if cls[1] == 1.0:
                verdict.append((b, 'converges' if (r >= 3 and d2 < 1e-2) else 'not shown', r, d2))
    print('verdict at 1.0 <= r_A < 1.2 (C1: ratio >= 3 and |dP| 800-1600 < 1e-2):')
    for b, w, r, d2 in verdict:
        print('   [%.2f, %.2f): %s (ratio %.2f, |dP| %.2e)' % (*b, w, r, d2))
    print('control (amplitude 7/8 in place of the 800-row cp run shows no convergence on some band below v = 1.8):',
          'fails (good)' if ctl_hit else 'passed (bad)')
    ok &= ctl_hit
    print('cplate5c:', 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
