#!/usr/bin/env python3
"""rich5.py -- CERTIFY-10L5-RESULT.md round 5, item 3: a Richardson-improved approximant, pinned, and its residual
certified at K1's points and as a sup on boxes where the pinned approximant of rcert5c.py provably cannot be certified.
Labels: certified (Arb ball arithmetic, python-flint) for every value and bound; computed (floating point) for the fit
that defines the coefficients and for R1.

The approximant.  rcert5.py's construction exactly (resid5.fit on u in [-4, -1.1], v in [0.55, 1.6], degrees 24 x 30
in (t, sig), the run's 16-node interpolant in x), applied not to one run but to the Richardson combination
    F_R = (4 F_800 - F_400)/3  at the 400-row nodes,
F_400, F_800 the fields of the two seed-1 runs at M = 16 (cut 0.3) that resid5.py and rcert5.py use, whose nodes nest
(every second 800-row node is a 400-row node, the same 16 angular nodes).  The runs are second order in the null step
(resid5.py: residual ratio 3.92 from 400 to 800 rows), so F_R cancels the leading error.  Whatever the expansion does,
F_R is an explicit smooth metric of the class: its coefficients are saved (data/rcert5_C3R.npz) with the md5 of each
tensor's float64 bytes, and every statement below is about those coefficients and no others.

  R0 the pinned tensors: data/rcert5_C3R.npz's five md5s equal PINNED_R; data/rcert5_C3.npz (the round-3 approximant)
     is read only, and its md5 is the committed one before and after.
  R2 (certified) K1 for the Richardson approximant: the eight scaled frame components (over sqrt(K_0)) at rcert5d.py
     D3's 16,128 points, certified LOWER and UPPER ends; the census over K2's 416 boxes at tau = 5.3e-4 (round 3's most
     favourable conditional demand) and tau' = 3.0e-5 (the demand at 2(d)'s G = 10).  Regression: the same census code
     on the round-3 tensors must reproduce rcert5d.out D3 (193 and 337 of 416, largest 2.414e-3).
  R3 (certified) the sup over boxes by rcert5d.py's engine (order-3 Taylor models with the Lagrange remainder,
     adaptive bisection, the accepted sub-boxes tiling the box).  The boxes: in each of the K2 boxes holding the three
     largest certified point values of the round-3 approximant (each above tau, so that box cannot be certified for it
     by any method), the depth-2 sub-box (1/64 of the K2 box) containing that point.  Pass: the Richardson approximant's
     certified sup there is <= tau, below the round-3 approximant's certified point value inside the same sub-box.
  Controls (each must fail where it should):
     C1 (rcert5d.py's): the bound assembly with the Lagrange remainder dropped under-bounds a known polynomial.
     C2 (rcert5.py's): the Richardson approximant with W + 0.01 v: its certified point values exceed tau (refused).
     C3 the census code: on the round-3 tensors it must find points above tau (the regression of R2) -- a census that
        under-reports would pass the Richardson approximant vacuously.

  python3 checks/rich5.py                  (read only: R0, R2, R3 and the controls)
  python3 checks/rich5.py --runs RUNDIR    (R1, computed: the floating-point residual at the 400-row cell midpoints,
                                           refitting from RUNDIR's l1_M16_400.npz and l1_M16_800.npz (md5s checked):
                                           the 400 and 800 fits, F_R, and the control F_2 = 2 F_800 - F_400 (a first-
                                           order combination, which must NOT improve on F_800), and F_R at degrees
                                           30 x 36)
  python3 checks/rich5.py --write RUNDIR   (build F_R from RUNDIR's runs, fit, and write data/rcert5_C3R.npz; the fit is
                                           not bit-reproducible (rcert5c.py), so its md5s are then pinned below)
"""
import os, sys, time, hashlib, itertools
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rcert5 as R5                                                              # noqa: E402
import rcert5d as RD                                                             # noqa: E402
from flint import arb                                                             # noqa: E402
print = R5.print
FRL = RD.FRL
DATA = os.path.join(os.path.dirname(HERE), 'data')
OUT_R = os.path.join(DATA, 'rcert5_C3R.npz')
OLD = os.path.join(DATA, 'rcert5_C3.npz')
OLD_MD5 = '698569f6faaab4420fe2e67abc860561'
RUN_MD5 = {'l1_M16_400.npz': '9a0ecfbbfbd989ac0086ba8e3f389cd3', 'l1_M16_800.npz': 'cd9df99856c2c5a2591d7f135639f123'}
PINNED_R = {'R': '38d56f2c0e74ca1f98464535fc772b68', 'm': '823816695d383bbaccd88cd05cec3102',
            'n': '25ca367fb31a26a7727b8272b3197f66', 'W': 'd6c979afce76ef042af7d73743b93f2e',
            's': 'eb5158067377eee0c20bf4758868af73'}
FILE_MD5_R = '88e16664187868e47eaaaa18709cfc61'
TAU, TAU2 = 5.3e-4, RD.TAU_G10


def fmd5(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()


def tmd5(C3):
    return {k: hashlib.md5(np.ascontiguousarray(C3[k], dtype=np.float64).tobytes()).hexdigest() for k in C3}


def load_runs(rundir):
    for nm, m in RUN_MD5.items():
        got = fmd5(os.path.join(rundir, nm))
        assert got == m, '%s md5 %s, not the record\'s %s' % (nm, got, m)
    a = R5.B.load(os.path.join(rundir, 'l1_M16_400.npz')); b = R5.B.load(os.path.join(rundir, 'l1_M16_800.npz'))
    assert np.array_equal(b['u'][::2], a['u']) and np.array_equal(b['v'][::2], a['v']) and np.array_equal(a['x'], b['x'])
    return a, b


def combo(a, b, wgt):
    """(wgt F_800 - F_400)/(wgt - 1) at the 400-row nodes"""
    Z = dict(a)
    for k in R5.RS.NAMES:
        Z[k] = (wgt * b[k][::2, ::2] - a[k]) / (wgt - 1)
    Z['mask'] = a['mask'] | b['mask'][::2, ::2]
    return Z


def geometry(M):
    a = R5.ARGS
    xa, xb = np.arcsinh((a[0] + 1) / R5.RS.A_GRID), np.arcsinh((a[1] + 1) / R5.RS.A_GRID)
    hv = (a[3] - a[2]) / 2
    return dict(hxi=(xb - xa) / 2, a=R5.RS.A_GRID, psi=1 / hv, xa=xa, M=M, hv=hv)


def load(path):
    L = np.load(path)
    C3 = {k: np.array(L[k]) for k in R5.RS.NAMES}
    return C3, geometry(C3['R'].shape[2])


def point_values(C3, g, frame, names):
    """rcert5d.py D3's points: certified lower and upper ends of |component| (Nt x Ns x Nx x 8)"""
    Nt = Ns = 24
    x1 = float(np.cos(np.pi / (2 * g['M'])))
    tcs = [-1 + (2 * p + 1) / Nt for p in range(Nt)]
    scs = [-1 + (2 * q + 1) / Ns for q in range(Ns)]
    xcs, _ = R5.x_boxes(x1, n_mid=8)
    pts = {}
    for f in R5.RS.NAMES:
        tens, _ = R5.deriv_tensors(C3[f], 2)
        pts[f] = R5.point_coeffs(tens, tcs, scs, xcs, 2)
    hxi, a, psi = arb(g['hxi']), arb(g['a']), arb(g['psi'])
    lo = np.zeros((Nt, Ns, len(xcs), 8)); hi = np.zeros_like(lo)
    for p, q, r in itertools.product(range(Nt), range(Ns), range(len(xcs))):
        xi = arb(g['xa']) + (arb(tcs[p]) + 1) * hxi
        ch, th = xi.cosh(), xi.tanh()
        phi1 = 1 / (hxi * a * ch); phi2 = -phi1 * phi1 * hxi * th
        e = {'x': arb(xcs[r])}
        for f in R5.RS.NAMES:
            c = lambda al: pts[f][al][p, q, r]
            e[f] = c((0, 0, 0)); Ft = c((1, 0, 0))
            e[f + '_u'] = phi1 * Ft; e[f + '_v'] = psi * c((0, 1, 0)); e[f + '_x'] = c((0, 0, 1))
            e[f + '_uu'] = phi1 * phi1 * 2 * c((2, 0, 0)) + phi2 * Ft
            e[f + '_uv'] = phi1 * psi * c((1, 1, 0)); e[f + '_ux'] = phi1 * c((1, 0, 1))
            e[f + '_vv'] = psi * psi * 2 * c((0, 2, 0)); e[f + '_vx'] = psi * c((0, 1, 1))
            e[f + '_xx'] = 2 * c((0, 0, 2))
        vv_ = frame(*[e[k] for k in names])
        for k8 in range(8):
            av = abs(vv_[k8])
            lo[p, q, r, k8] = float(av.mid() - av.rad()); hi[p, q, r, k8] = float(av.mid() + av.rad())
    return lo, hi, (tcs, scs, xcs)


def census(vals, grid, x1, tau):
    """max over K2's boxes (4 x 4 in (t, sig), rcert5.x_boxes(n_mid=6) in x) of the given point values"""
    tcs, scs, xcs = grid
    xb, hb = R5.x_boxes(x1, n_mid=6)
    boxes = {}
    for p, q, r in itertools.product(range(len(tcs)), range(len(scs)), range(len(xcs))):
        bt, bs = min(int((tcs[p] + 1) / 0.5), 3), min(int((scs[q] + 1) / 0.5), 3)
        for b_ in [i for i, (c_, h_) in enumerate(zip(xb, hb)) if c_ - h_ <= xcs[r] <= c_ + h_]:
            key = (bt, bs, b_)
            boxes[key] = max(boxes.get(key, 0.0), vals[p, q, r].max())
    return boxes, sum(1 for v_ in boxes.values() if v_ > tau), (xb, hb)


def subbox(k2, pt, xbh, depth=2):
    """the depth-`depth` sub-box of K2 box k2 = (bt, bs, b_) containing the point pt = (t, sig, x)"""
    bt, bs, b_ = k2
    xb, hb = xbh
    lo = [-1 + 0.5 * bt, -1 + 0.5 * bs, xb[b_] - hb[b_]]
    wd = [0.5, 0.5, 2 * hb[b_]]
    n = 2 ** depth
    out = []
    for d in range(3):
        i = min(int((pt[d] - lo[d]) / (wd[d] / n)), n - 1)
        h = wd[d] / n / 2
        out += [lo[d] + (2 * i + 1) * h, h]
    return tuple(out)


def sup_box(eng, box, tau, cap=4000):
    """rcert5d.py's adaptive bisection on one box, in process: accepted sub-boxes, counts, max sup and centre"""
    queue, acc, npar, t0 = [(box, 0)], [], 0, time.process_time()
    while queue and npar < cap:
        queue.sort(key=lambda e: e[1])
        b, d = queue.pop(0)
        npar += 1
        for kb, sup, cen in eng.kids(b):
            (acc.append((kb, sup, cen, d + 1)) if max(sup) <= tau else queue.append((kb, d + 1)))
    vol0 = 8 * box[1] * box[3] * box[5]
    vol = sum(8 * b[1] * b[3] * b[5] for b, _, _, _ in acc)
    done = not queue and abs(vol - vol0) < 1e-12 * vol0
    sup = [max([s[k] for _, s, _, _ in acc] or [float('inf')]) for k in range(8)]
    cen = [max([c[k] for _, _, c, _ in acc] or [0.0]) for k in range(8)]
    depths = sorted(set(d for _, _, _, d in acc))
    return dict(done=done, nacc=len(acc), nev=8 * npar, sup=sup, cen=cen, depths=depths,
                cpu=time.process_time() - t0, left=len(queue))


def write(rundir):
    t0 = time.time()
    a, b = load_runs(rundir)
    C3, g, err = R5.prepare(combo(a, b, 4.0))
    np.savez_compressed(OUT_R, **{k: np.ascontiguousarray(C3[k], dtype=np.float64) for k in R5.RS.NAMES})
    L, _ = load(OUT_R)
    same = all(np.array_equal(L[k], C3[k]) for k in R5.RS.NAMES)
    print('--write: F_R fitted (fit errors %s), written to data/rcert5_C3R.npz and read back identical: %s (%.0f s)'
          % (', '.join('%s %.1e' % kv for kv in err.items()), same, time.time() - t0))
    print('   file md5 %s; tensor md5s %s' % (fmd5(OUT_R), tmd5(L)))
    return 0 if same else 1


def runs(rundir):
    t0 = time.time()
    a, b = load_runs(rundir)
    ricf, names = R5.RS.ricci_funcs()
    out = {}
    cases = [('F_400', a, None), ('F_800', b, None), ('F_R', combo(a, b, 4.0), None),
             ('F_2 (control)', combo(a, b, 2.0), None), ('F_R at 30 x 36', combo(a, b, 4.0), (30, 36))]
    for lab, Z, deg in cases:
        args = R5.ARGS[:4] + (list(deg) if deg else R5.ARGS[4:])
        res, err = R5.RS.residual(Z, args, ricf, names)
        out[lab] = max(v_[1] for v_ in res.values())
        print('R1 (computed) %s: fit error <= %.1e; worst residual/sqrt(K_0) at the 400-row cell midpoints %.3e (%s); '
              '%s (%.0f s)' % (lab, max(err.values()), out[lab], max(res, key=lambda k: res[k][1]),
                               ', '.join('%s %.2e' % (k, v_[1]) for k, v_ in res.items()), time.time() - t0),
              flush=True)
    imp = out['F_800'] / out['F_R']
    ctl = out['F_2 (control)'] >= out['F_800']
    print('R1 F_R improves on F_800 by %.1f-fold; the control F_2 does %s (%.2e against %.2e) -> %s'
          % (imp, 'not improve (good)' if ctl else 'improve (bad)', out['F_2 (control)'], out['F_800'],
             'PASS' if imp > 10 and ctl else 'FAIL'))
    return 0 if imp > 10 and ctl else 1


def main():
    t0 = time.time(); ok = True
    old_before = fmd5(OLD)
    CR, g = load(OUT_R)
    md5R = tmd5(CR)
    r0 = md5R == PINNED_R
    print('R0 data/rcert5_C3R.npz (file md5 %s): its five tensors\' md5s equal PINNED_R: %s; data/rcert5_C3.npz md5 %s '
          '(%s the committed %s)' % (fmd5(OUT_R), r0, old_before, 'equal to' if old_before == OLD_MD5 else 'DIFFERENT '
                                     'from', OLD_MD5))
    for k in R5.RS.NAMES:
        print('   %s: shape %s, md5 %s' % (k, CR[k].shape, md5R[k]))
    C3, _ = load(OLD)
    r0 &= tmd5(C3) == RD.MD5 and old_before == OLD_MD5
    ok &= r0
    frame, names = RD.frame_cached()
    x1 = float(np.cos(np.pi / (2 * g['M'])))
    # R2 and C3
    loO, hiO, grid = point_values(C3, g, frame, names)
    bxO, nO, xbh = census(loO, grid, x1, TAU)
    nO2 = sum(1 for v_ in bxO.values() if v_ > TAU2)
    c3 = (nO, nO2, len(bxO)) == (193, 337, 416) and abs(loO.max() - 2.414e-3) < 5e-7
    print('C3 (census regression) round-3 tensors: boxes above tau %d, above tau\' %d, of %d; largest certified lower '
          'end %.4e (rcert5d.out D3: 193, 337, 416, 2.414e-3) -> %s (%.0f s)' % (nO, nO2, len(bxO), loO.max(),
                                                                             'reproduced' if c3 else 'NOT reproduced',
                                                                             time.time() - t0), flush=True)
    ok &= c3
    loR, hiR, _ = point_values(CR, g, frame, names)
    bxR, nR, _ = census(hiR, grid, x1, TAU)
    nR2 = sum(1 for v_ in bxR.values() if v_ > TAU2)
    bxRl, nRl, _ = census(loR, grid, x1, TAU)
    nRl2 = sum(1 for v_ in bxRl.values() if v_ > TAU2)
    print('R2 (certified) Richardson approximant at the %d points: largest certified UPPER end %.4e; per component %s'
          % (loR[..., 0].size, hiR.max(), ', '.join('%s %.2e' % (k, hiR[..., i].max()) for i, k in enumerate(FRL))))
    print('   against the round-3 approximant\'s largest certified lower end %.4e: %.1f-fold lower' % (
        loO.max(), loO.max() / hiR.max()))
    print('   boxes holding a point whose UPPER end exceeds tau = %.1e: %d of %d; exceeds tau\' = %.1e: %d (lower '
          'ends: %d and %d, so at least %d boxes cannot be certified at tau\' for it)' % (TAU, nR, len(bxR), TAU2, nR2,
                                                                                          nRl, nRl2, nRl2))
    print('   (the round-3 approximant: %d and %d boxes above tau and tau\' by lower ends)' % (nO, nO2))
    r2 = nR == 0 and hiR.max() < TAU
    print('R2 %s (every certified point value of the Richardson approximant is below tau)' % ('PASS' if r2 else 'FAIL'),
          flush=True)
    ok &= r2
    # C2
    Cs = R5.shifted(CR, g, 0.01)
    loS, _, _ = point_values(Cs, g, frame, names)
    c2 = loS.max() > TAU
    print('C2 (control, W + 0.01 v) certified lower ends up to %.3e against tau -> %s' % (
        loS.max(), 'refused (good)' if c2 else 'accepted (bad)'), flush=True)
    ok &= c2
    # R3: the three largest round-3 point values, their K2 boxes and depth-2 sub-boxes
    tcs, scs, xcs = grid
    flat = np.argsort(loO.max(axis=3), axis=None)[::-1]
    picked, seen = [], set()
    for ix in flat:
        p, q, r = np.unravel_index(ix, loO.shape[:3])
        pt = (tcs[p], scs[q], xcs[r])
        bt, bs = min(int((pt[0] + 1) / 0.5), 3), min(int((pt[1] + 1) / 0.5), 3)
        k2 = [(bt, bs, i) for i, (c_, h_) in enumerate(zip(*xbh)) if c_ - h_ <= pt[2] <= c_ + h_][0]
        if k2 in seen:
            continue
        seen.add(k2); picked.append((k2, pt, loO[p, q, r].max(), FRL[int(loO[p, q, r].argmax())]))
        if len(picked) == 3:
            break
    engR = RD.Engine(CR, g, frame, names)
    r3 = True
    for k2, pt, val, comp in picked:
        sb = subbox(k2, pt, xbh)
        res = sup_box(engR, sb, TAU)
        tag = 't %.4f +- %.4f, sig %.4f +- %.4f, x %.4f +- %.4f' % sb
        print('R3 (certified) K2 box %s holds the round-3 point (t, sig, x) = (%.4f, %.4f, %.4f) with certified |%s| >= '
              '%.3e > tau; its depth-2 sub-box %s:' % (k2, pt[0], pt[1], pt[2], comp, val, tag))
        print('   Richardson approximant: %s, %d sub-boxes accepted (depths %s), %d evaluated, cpu %.0f s; certified '
              'sup %s; largest centre %.3e' % ('finished, tiles the box' if res['done'] else 'NOT finished (%d left)' %
                                                res['left'], res['nacc'], res['depths'], res['nev'], res['cpu'],
                                                ', '.join('%s <= %.2e' % kv for kv in zip(FRL, res['sup'])),
                                                max(res['cen'])), flush=True)
        good = res['done'] and max(res['sup']) <= TAU and max(res['sup']) < val
        print('   -> %s (sup %.3e against the round-3 point value %.3e: %.1f-fold lower)' % (
            'PASS' if good else 'FAIL', max(res['sup']), val, val / max(res['sup'])), flush=True)
        r3 &= good
    ok &= r3
    w_real, w_mut = RD.test_poly_control(False), RD.test_poly_control(True)
    c1 = w_real <= 1.0 and w_mut > 1.0
    print('C1 (control, remainder dropped) largest true/bound %.4f with the remainder, %.4f without -> %s'
          % (w_real, w_mut, 'the mutation is caught (good)' if c1 else 'BAD'))
    ok &= c1
    old_after = fmd5(OLD)
    print('   data/rcert5_C3.npz md5 after: %s (%s)' % (old_after, 'unchanged' if old_after == old_before else 'CHANGED'))
    ok &= old_after == OLD_MD5
    print('rich5 (%.0f s): %s' % (time.time() - t0, 'all checks pass' if ok else 'A CHECK FAILED'))
    return 0 if ok else 1


if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == '--write':
        sys.exit(write(sys.argv[2]))
    if len(sys.argv) > 2 and sys.argv[1] == '--runs':
        sys.exit(runs(sys.argv[2]))
    sys.exit(main())
