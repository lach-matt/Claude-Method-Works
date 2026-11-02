#!/usr/bin/env python3
"""rcert5b.py -- CERTIFY-10L5-RESULT.md round 3 (task 2): the certified sup of the residual over ONE sub-box of
rcert5.py's K2 grid, refined, to measure how fast the Taylor-model bound approaches the residual's own size.  Labels:
certified (Arb ball arithmetic, python-flint) for every bound; computed for the extrapolation.

Theorem 7.L's norm is a space-time L^2 norm of the reduced residual (reduce5.py R3), so a certificate is local: the
square of the norm is a sum over boxes, and a sup bound on one box bounds that box's share.  rcert5.py K2 bounded the
sup over 416 boxes (h_t = h_sig = 1/4) by 6.8e4 to 1.7e8 or not at all.  Here one interior box, (t, sig) = (-0.25,
-0.25), x in [0, 0.25] (half-widths 0.25, 0.25, 0.125; away from the corners where K2's worst boxes sat and from the
axes), is split into n^3 sub-boxes, n = 1, 2, 4, 8, with rcert5.py's order-3 Taylor models and Lagrange remainder
unchanged.

  B1 (certified) for each n: the largest certified sup bound over the n^3 sub-boxes, per frame component (scaled by
     sqrt(K_0) as in rcert5.py), and the largest certified value at the sub-box centres (a lower bound for the sup).
  B2 (computed) the ratio of the bound at n to that at n/2 (the order-3 remainder predicts about 8), and the n at which
     the bound would meet twice the centre values if that ratio held.
  Control: the same box for the approximant with W + 0.01 v (rcert5.py's control): its certified centre values at n = 4
     must exceed the approximant's tenfold.

  python3 checks/rcert5b.py RUNDIR [nmax]          (RUNDIR holding l1_M16_800.npz, the run resid5.py fits)
"""
import os, sys, time, itertools, importlib.util
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rcert5 as R5                                                              # noqa: E402
from flint import arb                                                             # noqa: E402
print = R5.print
FRL = ['ll', 'ln', 'nn', 'lx', 'nx', 'xx', '11', '22']


def certify_box(prep, frame, names, box, n, cache):
    """sup bound and centre values over the n^3 sub-boxes of box = (tc, ht, sc, hs, xc, hx)"""
    C3, g, _ = prep
    tc0, ht0, sc0, hs0, xc0, hx0 = box
    ht, hs, hx = ht0 / n, hs0 / n, hx0 / n
    tcs = [tc0 - ht0 + (2 * p + 1) * ht for p in range(n)]
    scs = [sc0 - hs0 + (2 * p + 1) * hs for p in range(n)]
    xcs = [xc0 - hx0 + (2 * p + 1) * hx for p in range(n)]
    hxs = [hx] * n
    Q = R5.Q
    fld_box, fld_pt = {}, {}
    for f in R5.RS.NAMES:
        if f not in cache:
            cache[f] = R5.deriv_tensors(C3[f], Q + 4)
        tens, l1 = cache[f]
        pt = R5.point_coeffs(tens, tcs, scs, xcs, Q + 3)
        fld_pt[f] = {b: a for b, a in pt.items() if sum(b) <= Q + 2}
        fld_box[f] = R5.box_coeffs(pt, l1, (ht, hs, hxs), Q + 2)
    hpows = {m: arb(ht) ** m[0] * arb(hs) ** m[1] * arb(hx) ** m[2] for m in R5.MONO}
    sup = [arb(0)] * 8; cen = [arb(0)] * 8
    for p, q, r in itertools.product(range(n), range(n), range(n)):
        jb = {f: R5.field_jet(fld_box[f], p, q, r) for f in R5.RS.NAMES}
        jp = {f: R5.field_jet(fld_pt[f], p, q, r) for f in R5.RS.NAMES}
        ib = R5.inputs(jb, g, arb(tcs[p], ht), scs[q], arb(xcs[r], hx), True)
        ip = R5.inputs(jp, g, arb(tcs[p]), scs[q], arb(xcs[r]), False)
        fb = frame(*[ib[k] for k in names])
        fp = frame(*[ip[k] for k in names])
        for k8 in range(8):
            bnd = arb(0)
            for i, m in enumerate(R5.MONO):
                cc = fp[k8].c[i] if sum(m) < Q else fb[k8].c[i]
                bnd = bnd + abs(cc) * hpows[m]
            up = arb(bnd.mid() + bnd.rad())
            sup[k8] = arb('inf') if not up.is_finite() else (up if up > sup[k8] else sup[k8])
            cv = abs(fp[k8].c[0]); cu = arb(cv.mid() + cv.rad())
            if cu > cen[k8]:
                cen[k8] = cu
    return sup, cen


def main():
    rundir = sys.argv[1]
    nmax = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    t0 = time.time()
    frame, names = R5.frame_code()
    Z = R5.B.load(os.path.join(rundir, 'l1_M16_800.npz'))
    prep = R5.prepare(Z)
    print('approximant fitted and frame code generated (%.0f s)' % (time.time() - t0), flush=True)
    box = (-0.25, 0.25, -0.25, 0.25, 0.125, 0.125)
    print('the box: t in [-0.5, 0], sig in [-0.5, 0], x in [0, 0.25] (rcert5.py coordinates)')
    cache, hist = {}, []
    n = 1
    while n <= nmax:
        t1 = time.time()
        sup, cen = certify_box(prep, frame, names, box, n, cache)
        hist.append((n, sup, cen))
        print('B1 n = %d (%d sub-boxes, %.0f s):' % (n, n ** 3, time.time() - t1), flush=True)
        print('   ' + '  '.join('%s: sup <= %s, centres <= %s' % (k, s_.str(3), c_.str(3))
                                for k, s_, c_ in zip(FRL, sup, cen)))
        n *= 2
    print('B2 the ratio of the bound at n to that at n/2, per component, and the n at which the bound would reach twice '
          'the centre values at that ratio (computed):')
    ok = True
    for k8, k in enumerate(FRL):
        rats = []
        for (n0, s0, _), (n1, s1, c1) in zip(hist[:-1], hist[1:]):
            if s0[k8].is_finite() and s1[k8].is_finite():
                rats.append(float((s0[k8] / s1[k8]).mid()))
        last_n, last_s, last_c = hist[-1]
        if rats and last_s[k8].is_finite() and rats[-1] > 1:
            gap = float((last_s[k8] / (2 * last_c[k8])).mid())
            need = last_n * gap ** (np.log(2) / np.log(rats[-1])) if gap > 1 else last_n
            print('   %s: ratios %s; at n = %d bound/centre = %.3g; reaches 2x the centre values at n ~ %.3g '
                  '(%.2g sub-boxes for this one box)' % (k, ', '.join('%.2f' % r_ for r_ in rats), last_n,
                                                        float((last_s[k8] / last_c[k8]).mid()), need, need ** 3))
        else:
            print('   %s: ratios %s; bound at n = %d: %s' % (k, ', '.join('%.2f' % r_ for r_ in rats), last_n,
                                                            last_s[k8].str(3)))
    # control
    Cs = R5.shifted(prep[0], prep[1], 0.01)
    _, cen_s = certify_box((Cs, prep[1], prep[2]), frame, names, box, 4, {})
    c_ok = max(cen_s) > 10 * max(hist[min(2, len(hist) - 1)][2])
    print('control (W + 0.01 v, n = 4): centre values up to %s against %s -> %s' % (
        max(cen_s).str(3), max(hist[min(2, len(hist) - 1)][2]).str(3), 'fails (good)' if c_ok else 'passed (bad)'))
    ok &= c_ok
    print('rcert5b (%.0f s):' % (time.time() - t0), 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
