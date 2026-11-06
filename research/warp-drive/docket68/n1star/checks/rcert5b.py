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

  B3 (round 4; the soundness gate the verifier of round 3 asked for) for each n, the certified sup of each component
     must be at least (a) the certified values at the centres of the finer (2n)^3 grid and (b) the certified values at
     500 random points of the box (both lower bounds of the true sup).  And the bound assembly itself is tested: on
     f = T_3(t) T_3(sig) T_3(x), whose sup on a box is known, the same assembly must bound it, and with the Lagrange
     remainder replaced by the point Taylor coefficients (the unsound mutant, which on the residual itself passes
     (a) and (b)) it must not.

  python3 checks/rcert5b.py [nmax]          (round 4: the PINNED approximant data/rcert5_C3.npz, read only, its five
                                            md5s checked; round 3 refitted from RUNDIR, an unsaved fit)
"""
import os, sys, time, itertools, importlib.util
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rcert5 as R5                                                              # noqa: E402
import rcert5c as R5C                                                            # noqa: E402
from flint import arb                                                             # noqa: E402
print = R5.print
FRL = ['ll', 'ln', 'nn', 'lx', 'nx', 'xx', '11', '22']


def assemble(cp, cb, hpow, drop=False):
    """the Taylor-model bound: sum_{|alpha| < Q} |f_alpha(c)| h^alpha + sum_{|alpha| = Q} sup_B |f_alpha| h^alpha (the
    Lagrange remainder); drop=True is the unsound mutant (point coefficients at order Q too)"""
    bnd = arb(0)
    for i, m in enumerate(R5.MONO):
        cc = cp.c[i] if (sum(m) < R5.Q or drop) else cb.c[i]
        bnd = bnd + abs(cc) * hpow[m]
    up = arb(bnd.mid() + bnd.rad())
    return up


def poly_test(drop):
    """the bound assembly on two known functions: f1 = T_3(t) T_3(sig) T_3(x) on 27 boxes of half-width 0.3, and
    f2 = t^4 + sig^4 + x^4 on the box of half-width 1/2 about the origin, whose Taylor coefficients of order <= 3 vanish
    there (so the point Taylor polynomial bounds it by 0, while its sup is 3/16).  Returns the largest (grid lower
    bound of the true sup)/(bound): <= 1 for a sound assembly"""
    from rcert5 import TJ, MONO, Q
    worst = 0.0
    cases = [(c, 0.3, 'T3') for c in itertools.product((-0.6, 0.0, 0.55), repeat=3)] + [((0.0, 0.0, 0.0), 0.5, 'P4')]
    for c, h, kind in cases:
        lin = lambda c0, ax, box: TJ([arb(c0, h if box else 0)] + [arb(1) if MONO[i] == tuple(int(k == ax) for k in
                                                                                             range(3)) else arb(0)
                                                                for i in range(1, len(MONO))])
        if kind == 'T3':
            F = lambda t, s_, x: (t * t * t * 4 - t * 3) * (s_ * s_ * s_ * 4 - s_ * 3) * (x * x * x * 4 - x * 3)
            Fn = lambda t, s_, x: (4 * t ** 3 - 3 * t) * (4 * s_ ** 3 - 3 * s_) * (4 * x ** 3 - 3 * x)
        else:
            F = lambda t, s_, x: t * t * t * t + s_ * s_ * s_ * s_ + x * x * x * x
            Fn = lambda t, s_, x: t ** 4 + s_ ** 4 + x ** 4
        vb = F(lin(c[0], 0, True), lin(c[1], 1, True), lin(c[2], 2, True))
        vp = F(lin(c[0], 0, False), lin(c[1], 1, False), lin(c[2], 2, False))
        up = float(assemble(vp, vb, {m: arb(h) ** sum(m) for m in MONO}, drop))
        g = np.linspace(-h, h, 61)
        tt, ss, xx = np.meshgrid(c[0] + g, c[1] + g, c[2] + g, indexing='ij')
        true = float(np.abs(Fn(tt, ss, xx)).max())
        worst = max(worst, true / up if up > 0 else float('inf'))
    return worst

def point_values(prep, frame, names, pts, cache):
    """certified lower bounds of |component| at the points (t, sig, x)"""
    C3, g, _ = prep
    out = np.zeros((len(pts), 8))
    for j, (t_, s_, x_) in enumerate(pts):
        fp = {}
        for f in R5.RS.NAMES:
            tens, l1 = cache[f]
            pt = R5.point_coeffs(tens, [t_], [s_], [x_], R5.Q + 2)
            fp[f] = R5.field_jet({k: a for k, a in pt.items() if sum(k) <= R5.Q + 2}, 0, 0, 0)
        ip = R5.inputs(fp, g, arb(t_), s_, arb(x_), False)
        vp = frame(*[ip[k] for k in names])
        for k8 in range(8):
            av = abs(vp[k8].c[0])
            out[j, k8] = float(av.mid() - av.rad())
    return out


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
            up = assemble(fp[k8], fb[k8], hpows, certify_box.drop)
            sup[k8] = arb('inf') if not up.is_finite() else (up if up > sup[k8] else sup[k8])
            cv = abs(fp[k8].c[0]); cu = arb(cv.mid() + cv.rad())
            if cu > cen[k8]:
                cen[k8] = cu
    return sup, cen


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    t0 = time.time()
    frame, names = R5.frame_code()
    import hashlib
    L = np.load(R5C.OUT)
    C3 = {k: np.array(L[k]) for k in R5.RS.NAMES}
    pinned = all(hashlib.md5(C3[k].tobytes()).hexdigest() == R5C.PINNED[k] for k in R5.RS.NAMES)
    prep = (C3, R5C.geometry(C3['R'].shape[2]), None)
    print('the pinned approximant %s loaded read only, its five md5s equal rcert5c.py\'s: %s; frame code generated '
          '(%.0f s)' % (os.path.relpath(R5C.OUT, os.path.dirname(os.path.dirname(HERE))), pinned, time.time() - t0),
          flush=True)
    if not pinned:
        print('rcert5b: FAILURES (not the pinned approximant)')
        return 1
    box = (-0.25, 0.25, -0.25, 0.25, 0.125, 0.125)
    print('the box: t in [-0.5, 0], sig in [-0.5, 0], x in [0, 0.25] (rcert5.py coordinates)')
    cache, hist, gates = {}, [], []
    n = 1
    while n <= nmax:
        t1 = time.time()
        sup, cen = certify_box(prep, frame, names, box, n, cache)
        hist.append((n, sup, cen))
        tc0, ht0, sc0, hs0, xc0, hx0 = box
        m2 = 2 * n
        fine = [(tc0 - ht0 + (2 * p + 1) * ht0 / m2, sc0 - hs0 + (2 * q + 1) * hs0 / m2,
                 xc0 - hx0 + (2 * r + 1) * hx0 / m2)
                for p in range(m2) for q in range(m2) for r in range(m2)] if n <= 4 else []
        rng = np.random.default_rng(20261106 + n)
        rand = [(tc0 + ht0 * a_, sc0 + hs0 * b_, xc0 + hx0 * c_) for a_, b_, c_ in rng.uniform(-1, 1, (500, 3))]
        pv = point_values(prep, frame, names, fine + rand, cache)
        gate = all(float(sup[k8].mid() + sup[k8].rad()) >= pv[:, k8].max() for k8 in range(8)
                   if sup[k8].is_finite())
        gates.append(gate)
        print('B3 n = %d gate: certified sup >= the certified values at %d finer centres and 500 random points: %s '
              '(largest point value %.3e)' % (n, len(fine), gate, pv.max()), flush=True)
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
    w_sound, w_mut = poly_test(False), poly_test(True)
    t_ok = w_sound <= 1.0 and w_mut > 1.0
    print('B3 the assembly on T_3 T_3 T_3: largest true/bound %.4f (sound, must be <= 1), %.4f with the point Taylor '
          'polynomial in place of the remainder (the mutant, must exceed 1) -> %s' % (
              w_sound, w_mut, 'the mutant is caught (good)' if t_ok else 'BAD'))
    ok &= t_ok and all(gates)
    # control
    Cs = R5.shifted(prep[0], prep[1], 0.01)
    _, cen_s = certify_box((Cs, prep[1], prep[2]), frame, names, box, 4, {})
    c_ok = max(cen_s) > 10 * max(hist[min(2, len(hist) - 1)][2])
    print('control (W + 0.01 v, n = 4): centre values up to %s against %s -> %s' % (
        max(cen_s).str(3), max(hist[min(2, len(hist) - 1)][2]).str(3), 'fails (good)' if c_ok else 'passed (bad)'))
    ok &= c_ok
    print('rcert5b (%.0f s):' % (time.time() - t0), 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


certify_box.drop = False

if __name__ == '__main__':
    sys.exit(main())
