#!/usr/bin/env python3
"""szconv5.py -- CERTIFY-10L5-RESULT.md round 9 (the paper's "Physical wavelengths" item): is the rebuilt outer zero's
difference from growth5's, from v = 1.3, the double-null grid's?  Labels: computed (floating point) on double-null runs
at the first seed, M = 16, at 400 x 180, 800 x 360 and 1600 x 720 rows, with the data cone at R0 = 10 and 20.

secondzero5.py S6 measured max |r_AH - r_AH(growth5)| on growth5's 17 columns at v = 1.0, 1.2, 1.3, 1.35, 1.375, at 400
and 800 rows; from v = 1.3 the difference grew from 400 to 800 rows, so it was not resolved in (u, v) (section 0).
  Z1 the rebuilt outer zero's own change under the null step: max |r_AH(800) - r_AH(400)| and max |r_AH(1600) -
     r_AH(800)| on the same columns and v, against max |r_AH(1600) - r_AH(growth5)|.  Resolved in (u, v) where the last
     change is below a fifth of the difference from growth5.
  Control: the leaves' expansion 3 R_v/R in place of the Bondi spheres' theta (secondzero5.py's control) must disagree
     with growth5 by more than 0.1 somewhere at 1600 rows (the comparison tells the two expansions apart).

  python3 checks/szconv5.py RUNDIR      (RUNDIR holding l1_M16_{400,800,1600}[_R20].npz, made by checks/szrun5.py)
"""
import os, sys, importlib.util
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
_s = importlib.util.spec_from_file_location('secondzero5', os.path.join(HERE, 'secondzero5.py'))
SZ = importlib.util.module_from_spec(_s); _s.loader.exec_module(SZ)
B = SZ.B
print = SZ.print


def rows(rundir, name, leaf_only=False):
    Z = B.load(os.path.join(rundir, name + '.npz')); F = B.derivatives(Z)
    out = []
    for vv in SZ.G5KEY[1][1]:
        j = int(np.argmin(abs(Z['v'] - vv)))
        xi, rr, TH = SZ.bondi_zeros(Z, F, j, np.linspace(0.6, 1.6, 101), leaf_only=leaf_only)
        r17 = B.bary_matrix(xi, SZ.XG) @ SZ.outer_zero(xi, rr, TH)
        out.append((float(Z['v'][j]), r17, SZ.g5_outer(Z['v'][j])[1]))
    return out


def main():
    rundir = sys.argv[1]
    ok = True
    for tag, names in (('R0 = 10', ('l1_M16_400', 'l1_M16_800', 'l1_M16_1600')),
                       ('R0 = 20', ('l1_M16_400_R20', 'l1_M16_800_R20', 'l1_M16_1600_R20'))):
        a, b, c = [rows(rundir, n) for n in names]
        d1 = [float(np.nanmax(abs(b[i][1] - a[i][1]))) for i in range(len(c))]
        d2 = [float(np.nanmax(abs(c[i][1] - b[i][1]))) for i in range(len(c))]
        dg = [float(np.nanmax(abs(c[i][1] - c[i][2]))) for i in range(len(c))]
        res = [d2[i] < dg[i] / 5 for i in range(len(c))]
        print('Z1 (computed) %s, v = %s:' % (tag, ', '.join('%.3f' % r[0] for r in c)))
        print('   max |r_AH(800) - r_AH(400)|:  %s' % ', '.join('%.4f' % q for q in d1))
        print('   max |r_AH(1600) - r_AH(800)|: %s' % ', '.join('%.4f' % q for q in d2))
        print('   max |r_AH(1600) - growth5|:   %s' % ', '.join('%.4f' % q for q in dg))
        print('   resolved in (u, v) (last change below a fifth of the difference from growth5), from v = 1.3: %s' % (
            all(r for r, row in zip(res, c) if row[0] >= 1.29)))
        ok &= all(r for r, row in zip(res, c) if row[0] >= 1.29)
    ctl = rows(rundir, 'l1_M16_1600', leaf_only=True)
    worst = max(float(np.nanmax(abs(r[1] - r[2]))) for r in ctl)
    print('   control: the leaves\' expansion in place of theta disagrees with growth5 by %.3f at 1600 rows (must '
          'exceed 0.1) -> %s' % (worst, 'fails (good)' if worst > 0.1 else 'passes (bad)'))
    ok &= worst > 0.1
    print('szconv5: %s' % ('all checks pass' if ok else 'FAILURES'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
