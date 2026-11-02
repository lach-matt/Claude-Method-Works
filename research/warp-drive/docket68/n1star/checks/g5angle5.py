#!/usr/bin/env python3
"""g5angle5.py -- CERTIFY-10L5-RESULT.md sections 1.4-1.5: growth5.py's Bondi scheme re-run with every zero of the
round spheres' expansion recorded (checks/g5zeros5.py), read here.  Labels: computed (floating point).

  A1 the Nx = 16 re-run (Ny = 20) reproduces the pinned breakdown of L100_lam1_20x16_d0 (v = 1.5, growth5.py PINNED).
     Control: the same comparison for the Nx = 24 run must fail.
  A2 at growth5's own step the scheme is unstable in angle at Nx = 24 and 32 on the seed itself (v < 1/2, where the
     exact solution is Tangherlini and every field vanishes): K_all exceeds 1 there, growing step by step, while at
     Nx = 16 it stays below 1e-6.  Control: the instability test applied to the Nx = 16 run must not flag it.
  A3 per v, the Bondi columns with no zero of the expansion on r >= r_min (r_min = 0.54, the excision, and 0.64, the
     double-null rebuild's reach at v = 1.4): the first v at which one appears, and the counts at v = 1.40-1.55; the
     claim is that none appears before v = 1.4 at either r_min.  Control: at r_min = 1.25, above the outer zero of
     most columns, the same claim must fail.

  python3 checks/g5angle5.py RUN16.json RUN24.json RUN32.json
"""
import os, sys, json
import numpy as np

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
import growth5 as G                                                             # noqa: E402


def a1(rec):
    return G.breakdown(rec) is not None and abs(G.breakdown(rec) - G.PINNED['L100_lam1_20x16_d0']['v_break']) < 1e-6


def seed_growth(rec):
    st = [s for s in rec['steps'] if s[0] < 0.5]
    K = np.array([s[2] for s in st])
    return float(K.max()) if len(K) else np.nan, len(st), (st[-1][0] if st else None)


def unstable(rec):
    Kmax, n, vlast = seed_growth(rec)
    return Kmax > 1.0


def zero_less(rec, rmin):
    out = []
    for s in rec['steps']:
        n = sum(1 for c in s[7] if not any(r >= rmin for r in c))
        out.append((s[0], n))
    return out


def a3(rec, rmin, show=False):
    zl = zero_less(rec, rmin)
    first = next((v for v, n in zl if n > 0), None)
    if show:
        counts = []
        for vv in (1.40, 1.425, 1.45, 1.50, 1.55):
            v, n = min(zl, key=lambda q: abs(q[0] - vv))
            counts.append('%d at v = %.3f' % (n, v))
        print('     r >= %.2f: first column with no zero at v = %s; of 17:' % (rmin, first))
        print('        ' + ', '.join(counts))
    return first is not None and first >= 1.4


def main():
    r16, r24, r32 = [json.load(open(p)) for p in sys.argv[1:4]]
    ok = True
    good, ctl = a1(r16), a1(r24)
    print('A1 Nx = 16 breakdown %s (pinned 1.5): %s;\n   control Nx = 24 breakdown %s: %s' % (
        G.breakdown(r16), 'PASS' if good else 'FAIL', G.breakdown(r24), 'fails (good)' if not ctl else 'passed (bad)'))
    ok &= good and not ctl
    for name, rec in (('Nx = 16', r16), ('Nx = 24', r24), ('Nx = 32', r32)):
        Kmax, n, vlast = seed_growth(rec)
        st = rec['steps']
        print('   %s: %d steps on v < 1/2, max K_all %.3g; step dv %.5f;' % (name, n, Kmax, rec['cfg']['dv']))
        print('      run ended: %s' % rec['end'])
        if name != 'Nx = 16':
            K = [s[2] for s in st[-6:]]
            print('      last K_all: %s (ratios %s)' % (', '.join('%.3g' % k for k in K),
                                                      ', '.join('%.1f' % (K[i + 1] / K[i]) for i in range(len(K) - 1)
                                                                if K[i] > 0)))
    good = unstable(r24) and unstable(r32)
    ctl = unstable(r16)
    print('A2 unstable on the seed at Nx = 24 and 32: %s; control (Nx = 16 flagged) %s' % (
        'PASS' if good else 'FAIL', 'passed (bad)' if ctl else 'fails (good)'))
    ok &= good and not ctl
    print('A3 Bondi columns with no zero of the expansion (Nx = 16 run):')
    good = a3(r16, 0.54, True) and a3(r16, 0.64, True)
    ctl = a3(r16, 1.25, True)
    print('   none before v = 1.4 at r_min = 0.54 and 0.64: %s; control (r_min = 1.25) %s' % (
        'PASS' if good else 'FAIL', 'passed (bad)' if ctl else 'fails (good)'))
    ok &= good and not ctl
    print('g5angle5:', 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
