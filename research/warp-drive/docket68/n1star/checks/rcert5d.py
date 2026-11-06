#!/usr/bin/env python3
"""rcert5d.py -- CERTIFY-10L5-RESULT.md round 4 (task 3): the certified sup of the residual of rcert5.py's PINNED
approximant (data/rcert5_C3.npz, the tensors whose md5s rcert5c.py printed) over one whole interior box, by adaptive
bisection until every sub-box meets a target.  Labels: certified (Arb ball arithmetic, python-flint) for every bound;
computed for the timing and the extrapolation to the other boxes.

The method is rcert5.py's, unchanged: order-3 Taylor models in (t, sig, x) of the eight null-orthonormal frame
components of Ric[g_app] over sqrt(K_0), with the Lagrange remainder, on each box.  A box whose bound on any component
exceeds the target tau is split into its 2 x 2 x 2 children (evaluated as one tensor grid); a box whose eight bounds
are all <= tau is accepted.  The accepted boxes tile the box exactly (bisection), so the largest accepted bound is a
certified sup over the whole box, and sum(vol * sup^2) a certified bound on the box's share of a space-time L^2 norm.

  D0 the pinned tensors: their md5s must equal rcert5c.out's (the certificate is about those coefficients only).
  D1 (certified) for the box t in [-1/2, 0], sig in [-1/2, 0], x in [0, 1/4] (rcert5b.py's): the number of accepted
     sub-boxes, the depth reached, the largest certified sup per component, the largest certified centre value per
     component (a lower bound for the sup), and sum over sub-boxes of vol * max_k sup_k^2 (vol in (t, sig, x) units).
  D2 (certified) the lower bound: a certified centre value exceeding a target proves that NO bound on that box, of
     any method, meets it.  Reported for tau' = 3.0e-5 (the demand at 2(d)'s placeholder G = 10).
  Control C1 (mutation of the code under test): the Lagrange remainder dropped (the order-Q coefficients taken at the
     centre instead of over the box).  On the test functions T_3(t) T_3(sig) T_3(x) and t^4 + sig^4 + x^4 (rcert5b.py
     B3's), whose sups over the boxes are known, the mutated bound must fall below the true sup on some box (caught),
     and the real one must not.
  Control C2: the approximant with W + 0.01 v (rcert5.py's control) must be refused at tau on the box's first child:
     a certified centre value above tau.

  D3 (certified) the census over rcert5.py's whole box: K1's 16,128 certified point values (the pinned approximant)
     mapped to K2's 416 boxes (4 x 4 in (t, sig), 26 graded in x).  A box holding a point whose certified value
     exceeds tau cannot be certified at tau by any method; the count of such boxes at tau and at tau' is printed, with
     the rest (certifiable in principle) and the cost of the rest at this box's measured count.

  python3 checks/rcert5d.py --census [tau]          (D3 alone; writes its table to the checkpoint directory)
  python3 checks/rcert5d.py --worker w W [tau]     (chunk w of W of the box's 8 children; resumable checkpoints)
  python3 checks/rcert5d.py --collect W [tau]      (merge the W checkpoints, run D0-D2 and the controls, print)
  python3 checks/rcert5d.py --repartition W W2 [tau]   (stopped workers only: merge W checkpoints and split the queue
                                                    round-robin into W2; accepted boxes and counters go to chunk 0)
Checkpoints go to $RCERT5D_DIR (default: <tmp>/rcert5d; round 4 used the session's scratch directory).

[Round 5, the verifier of round 4, M-A: C1 exercised its own copy of the bound assembly, so a mutant with the
engine's Lagrange remainder dropped passed D1 with an unsound bound while C1 still printed "caught".  Repaired: the
engine and C1 now call ONE assembly, Engine.bound (C1 builds an Engine and bounds its test polynomials with it, so a
mutation of the engine's assembly or of its flag makes C1 fail); every float upper end is rounded upward
(up_float; the round-4 checkpoints' sups, rounded to nearest, are raised by one ulp in --collect); and --collect has a
gate on a code path independent of the engine (D4): the certified LOWER end of every component at the centre and the
eight corners of EVERY accepted sub-box, by the census's point evaluation (grid_values), must not exceed that box's
certified sup.]
"""
import os, sys, time, pickle, hashlib, itertools, math
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rcert5 as R5                                                              # noqa: E402
from flint import arb                                                             # noqa: E402
print = R5.print
FRL = ['ll', 'ln', 'nn', 'lx', 'nx', 'xx', '11', '22']
PIN = os.path.join(os.path.dirname(HERE), 'data', 'rcert5_C3.npz')
MD5 = {'R': 'be89d629886bf9c61c098a76c22ad7ae', 'm': '99434c1b9859c9fa03653b65148f8bdc',
       'n': '7a0ab510aec85e3329018558d5f76f91', 'W': '3427e2bfe9009ffff09650606d2837b3',
       's': '1faa82dee965590cfac4cdf14e460214'}
BOX = (-0.25, 0.25, -0.25, 0.25, 0.125, 0.125)            # (tc, ht, sc, hs, xc, hx): t, sig in [-1/2, 0], x in [0, 1/4]
SCR = os.environ.get('RCERT5D_DIR', os.path.join(__import__('tempfile').gettempdir(), 'rcert5d'))
TAU_G10 = 3.0e-5


def load_pinned():
    L = np.load(PIN)
    C3 = {k: np.array(L[k]) for k in R5.RS.NAMES}
    md5s = {k: hashlib.md5(np.ascontiguousarray(C3[k], dtype=np.float64).tobytes()).hexdigest() for k in C3}
    a = R5.ARGS
    xa, xb = np.arcsinh((a[0] + 1) / R5.RS.A_GRID), np.arcsinh((a[1] + 1) / R5.RS.A_GRID)
    hv = (a[3] - a[2]) / 2
    g = dict(hxi=(xb - xa) / 2, a=R5.RS.A_GRID, psi=1 / hv, xa=xa, M=C3['R'].shape[2], hv=hv)
    return C3, g, md5s


def up_float(b):
    """a float >= the upper end of the arb b (inf if b is not finite)"""
    u = b.upper() if hasattr(b, 'upper') else arb(b)
    if not u.is_finite():
        return float('inf')
    f = float(u)
    while arb(f) < u:
        f = math.nextafter(f, float('inf'))
    return f


def children(b):
    tc, ht, sc, hs, xc, hx = b
    return [(tc + i * ht / 2, ht / 2, sc + j * hs / 2, hs / 2, xc + k * hx / 2, hx / 2)
            for i in (-1, 1) for j in (-1, 1) for k in (-1, 1)]


class Engine:
    """rcert5.py's Taylor models on the 2 x 2 x 2 children of one box (one tensor grid)"""

    def __init__(self, C3, g, frame, names, drop_remainder=False):
        self.C3, self.g, self.frame, self.names = C3, g, frame, names
        self.cache = {f: R5.deriv_tensors(C3[f], R5.Q + 4) for f in R5.RS.NAMES}
        self.hp = {}
        self.drop = drop_remainder

    def bound(self, vp, vb, hpow):
        """THE Taylor-model bound, used by kids() and by control C1 alike: sum_{|alpha| < Q} |f_alpha(c)| h^alpha +
        sum_{|alpha| = Q} sup_B |f_alpha| h^alpha (the Lagrange remainder), as a float rounded upward; with
        self.drop (the mutant) the point coefficients are used at order Q too"""
        bnd = arb(0)
        for i, m in enumerate(R5.MONO):
            cc = vp.c[i] if (sum(m) < R5.Q or self.drop) else vb.c[i]
            bnd = bnd + abs(cc) * hpow[m]
        return up_float(bnd)

    def kids(self, b):
        """bounds (sup per component) and centre values for the 8 children of box b"""
        tc0, ht0, sc0, hs0, xc0, hx0 = b
        ht, hs, hx = ht0 / 2, hs0 / 2, hx0 / 2
        tcs, scs, xcs = [tc0 - ht, tc0 + ht], [sc0 - hs, sc0 + hs], [xc0 - hx, xc0 + hx]
        Q = R5.Q
        fb, fp = {}, {}
        for f in R5.RS.NAMES:
            tens, l1 = self.cache[f]
            pt = R5.point_coeffs(tens, tcs, scs, xcs, Q + 3)
            fp[f] = {k: a for k, a in pt.items() if sum(k) <= Q + 2}
            fb[f] = R5.box_coeffs(pt, l1, (ht, hs, [hx, hx]), Q + 2)
        key = (ht, hs, hx)
        if key not in self.hp:
            self.hp[key] = {m: arb(ht) ** m[0] * arb(hs) ** m[1] * arb(hx) ** m[2] for m in R5.MONO}
        hpow = self.hp[key]
        out = []
        for p, q, r in itertools.product(range(2), range(2), range(2)):
            jb = {f: R5.field_jet(fb[f], p, q, r) for f in R5.RS.NAMES}
            jp = {f: R5.field_jet(fp[f], p, q, r) for f in R5.RS.NAMES}
            ib = R5.inputs(jb, self.g, arb(tcs[p], ht), scs[q], arb(xcs[r], hx), True)
            ip = R5.inputs(jp, self.g, arb(tcs[p]), scs[q], arb(xcs[r]), False)
            vb = self.frame(*[ib[k] for k in self.names])
            vp = self.frame(*[ip[k] for k in self.names])
            sup, cen = [], []
            for k8 in range(8):
                sup.append(self.bound(vp[k8], vb[k8], hpow))
                cen.append(up_float(abs(vp[k8].c[0])))
            out.append(((tcs[p], ht, scs[q], hs, xcs[r], hx), sup, cen))
        return out


def frame_cached():
    """rcert5.frame_code(), whose generated source is deterministic; generated afresh every run"""
    return R5.frame_code()


def worker(w, W, tau):
    os.makedirs(SCR, exist_ok=True)
    ck = os.path.join(SCR, 'ck_%d_of_%d_tau%.1e.pkl' % (w, W, tau))
    t0 = time.time()
    C3, g, md5s = load_pinned()
    assert md5s == MD5, 'the pinned tensors are not the record\'s'
    frame, names = frame_cached()
    eng = Engine(C3, g, frame, names)
    if os.path.exists(ck):
        with open(ck, 'rb') as fh:
            st = pickle.load(fh)
    else:
        st = dict(queue=[(c, 1) for i, c in enumerate(children(BOX)) if i % W == w], acc=[], nparents=0,
                  nboxes=0, cpu=0.0, wall=0.0, maxdepth=1, rounded_up=True)
        # the 8 children of BOX are evaluated by their parent, BOX, inside the loop below
        st['queue'] = [(BOX, 0)] if w == 0 and W == 1 else st['queue']
    print('worker %d/%d: %d queued, %d accepted, setup %.0f s' % (w, W, len(st['queue']), len(st['acc']),
                                                                 time.time() - t0), flush=True)
    last = time.time()
    c0, w0 = time.process_time(), time.time()
    while st['queue']:
        st['queue'].sort(key=lambda e: e[1])
        b, d = st['queue'].pop(0)
        kids = eng.kids(b)
        st['nparents'] += 1; st['nboxes'] += 8
        for kb, sup, cen in kids:
            if max(sup) <= tau:
                st['acc'].append((kb, sup, cen, d + 1))
            else:
                st['queue'].append((kb, d + 1))
                st['maxdepth'] = max(st['maxdepth'], d + 1)
        if time.time() - last > 300 or not st['queue']:
            st['cpu'] += time.process_time() - c0; st['wall'] += time.time() - w0
            c0, w0 = time.process_time(), time.time()
            with open(ck + '.tmp', 'wb') as fh:
                pickle.dump(st, fh)
            os.replace(ck + '.tmp', ck)
            last = time.time()
            print('  %s: parents %d, boxes evaluated %d, accepted %d, queued %d (depth <= %d), cpu %.0f s, wall %.0f s'
                  % (time.strftime('%H:%M:%S'), st['nparents'], st['nboxes'], len(st['acc']), len(st['queue']),
                     max([e[1] for e in st['queue']] or [0]), st['cpu'], st['wall']), flush=True)
    print('worker %d/%d done' % (w, W), flush=True)


def test_poly_control(eng):
    """the engine's own bound assembly (eng.bound) on two known functions: f1 = T_3(t) T_3(sig) T_3(x) on 27 boxes
    of half-width 0.3, and
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
        up = eng.bound(vp, vb, {m: arb(h) ** sum(m) for m in MONO})
        g = np.linspace(-h, h, 61)
        tt, ss, xx = np.meshgrid(c[0] + g, c[1] + g, c[2] + g, indexing='ij')
        true = float(np.abs(Fn(tt, ss, xx)).max())
        worst = max(worst, true / up if up > 0 else float('inf'))
    return worst

def collect(W, tau):
    t0 = time.time()
    C3, g, md5s = load_pinned()
    ok0 = md5s == MD5
    print('D0 the pinned tensors %s: md5s %s the record\'s (rcert5c.out)' % (
        os.path.relpath(PIN, os.path.dirname(os.path.dirname(HERE))), 'equal' if ok0 else 'DIFFER from'))
    acc, nb, npar, cpu, wall, depth, wall0 = [], 0, 0, 0.0, 0.0, 0, 0.0
    done = True
    for w in range(W):
        ck = os.path.join(SCR, 'ck_%d_of_%d_tau%.1e.pkl' % (w, W, tau))
        with open(ck, 'rb') as fh:
            st = pickle.load(fh)
        acc += st['acc']; nb += st['nboxes']; npar += st['nparents']; cpu += st['cpu']
        wall = max(wall, st['wall']); wall0 = max(wall0, st.get('wall0', 0.0))
        depth = max(depth, st['maxdepth']); done &= not st['queue']
        print('   checkpoint %d/%d: %d accepted, %d queued, cpu %.0f s, wall %.0f s' % (
            w, W, len(st['acc']), len(st['queue']), st['cpu'], st['wall']))
    wall += wall0
    vol0 = 8 * BOX[1] * BOX[3] * BOX[5]
    vol = sum(8 * b[1] * b[3] * b[5] for b, _, _, _ in acc)
    tiles = abs(vol - vol0) < 1e-12 * vol0
    if not st.get('rounded_up'):     # round-4 checkpoints: sups rounded to nearest, so one ulp up bounds them
        acc = [(b, [math.nextafter(x_, float('inf')) for x_ in s_], c_, d) for b, s_, c_, d in acc]
    sup = [max(s[k] for _, s, _, _ in acc) for k in range(8)]
    cen = [max(c[k] for _, _, c, _ in acc) for k in range(8)]
    l2 = sum(8 * b[1] * b[3] * b[5] * max(s) ** 2 for b, s, _, _ in acc)
    dist = {}
    for _, _, _, d in acc:
        dist[d] = dist.get(d, 0) + 1
    print('D1 (certified) the box t in [-1/2, 0], sig in [-1/2, 0], x in [0, 1/4], target tau = %.2e:' % tau)
    print('   %s; %d sub-boxes accepted (by depth: %s), %d evaluated (%d parents), the accepted tile the box: %s' % (
        'finished' if done else 'NOT finished', len(acc), ', '.join('%d: %d' % kv for kv in sorted(dist.items())),
        nb, npar, tiles))
    print('   certified sup over the box: ' + ', '.join('%s <= %.3e' % (k, s_) for k, s_ in zip(FRL, sup)))
    print('   largest certified centre values (lower bounds for the sup): ' +
          ', '.join('%s %.3e' % (k, c_) for k, c_ in zip(FRL, cen)))
    print('   sum vol * max_k sup_k^2 = %.4e over vol %.4e (rms bound %.3e); cpu %.0f s, wall %.0f s (%.2f s per box)'
          % (l2, vol0, (l2 / vol0) ** 0.5, cpu, wall, cpu / max(nb, 1)))
    ok1 = done and tiles and max(sup) <= tau
    print('D1 %s' % ('PASS (every component certified <= tau on the whole box)' if ok1 else 'FAIL'))
    over = [k for k, c_ in zip(FRL, cen) if c_ > TAU_G10]
    print('D2 (certified) components whose certified centre value exceeds tau\' = %.1e somewhere in the box: %s; so no '
          'bound of any method meets tau\' there' % (TAU_G10, ', '.join(over) or 'none'))
    frame, names = frame_cached()
    w_real = test_poly_control(Engine(C3, g, frame, names))
    w_mut = test_poly_control(Engine(C3, g, frame, names, drop_remainder=True))
    c1 = w_real <= 1.0 and w_mut > 1.0
    print('C1 (control) the ENGINE\'s own assembly (Engine.bound) on the test polynomials: largest true/bound %.4f '
          '(must be <= 1); the same engine with the remainder dropped: %.4f (must exceed 1) -> %s' % (
              w_real, w_mut, 'sound, and the mutation is caught (good)' if c1 else 'BAD'))
    t4 = time.time()
    worst, viol, npts = box_gate(C3, g, frame, names, acc)
    d4 = viol == 0
    print('D4 (certified, independent of the engine) certified lower ends at the centre and 8 corners of every one of '
          'the %d accepted sub-boxes (%d points, grid_values): largest (point value)/(box sup) %.3f, violations %d -> '
          '%s (%.0f s)' % (len(acc), npts, worst, viol, 'PASS' if d4 else 'FAIL', time.time() - t4))
    Cs = R5.shifted(C3, g, 0.01)
    eng = Engine(Cs, g, frame, names)
    kids = eng.kids(children(BOX)[0])
    cmax = max(max(c) for _, _, c in kids)
    c2 = cmax > tau
    print('C2 (control, W + 0.01 v) certified centre values up to %.3e on the first child\'s children against tau -> %s'
          % (cmax, 'refused (good)' if c2 else 'accepted (bad)'))
    ok = ok0 and ok1 and c1 and c2 and d4
    print('rcert5d --collect (%.0f s): %s' % (time.time() - t0, 'all checks pass' if ok else 'FAILURES'))
    return 0 if ok else 1


def grid_values(C3, g, frame, names, tcs, scs, xcs):
    """certified LOWER and UPPER ends of |component| on the tensor grid tcs x scs x xcs, by point coefficients of
    order 2 (rcert5.py's K1 path: no Taylor model, no box assembly; independent of Engine)"""
    pts = {}
    for f in R5.RS.NAMES:
        tens, _ = R5.deriv_tensors(C3[f], 2)
        pts[f] = R5.point_coeffs(tens, tcs, scs, xcs, 2)
    hxi, a, psi = arb(g['hxi']), arb(g['a']), arb(g['psi'])
    lo = np.zeros((len(tcs), len(scs), len(xcs), 8)); hi = np.zeros_like(lo)
    for p, q, r in itertools.product(range(len(tcs)), range(len(scs)), range(len(xcs))):
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
            lo[p, q, r, k8] = float(av.mid() - av.rad())           # a certified LOWER bound for |value|
            hi[p, q, r, k8] = up_float(av)
    return lo, hi


def box_gate(C3, g, frame, names, acc):
    """D4: for every accepted box, the certified lower ends at its centre and its 8 corners (grid_values on the lattice
    of the box's size) against the box's certified sup; returns (largest ratio, violations, points evaluated)"""
    worst, viol, npts = 0.0, 0, 0
    bysize = {}
    for b, sup, cen, d in acc:
        bysize.setdefault((b[1], b[3], b[5]), []).append((b, sup))
    key = lambda v: round(v, 13)
    for (ht, hs, hx), boxes in bysize.items():
        for offs in ((0.0,), (-1.0, 1.0)):
            T = sorted({key(b[0] + o * ht) for b, _ in boxes for o in offs})
            S = sorted({key(b[2] + o * hs) for b, _ in boxes for o in offs})
            X = sorted({key(b[4] + o * hx) for b, _ in boxes for o in offs})
            lo, _ = grid_values(C3, g, frame, names, T, S, X)
            npts += lo[..., 0].size
            it = {v: i for i, v in enumerate(T)}; is_ = {v: i for i, v in enumerate(S)}
            ix = {v: i for i, v in enumerate(X)}
            for b, sup in boxes:
                for ot, os_, ox in itertools.product(offs, offs, offs):
                    vals = lo[it[key(b[0] + ot * ht)], is_[key(b[2] + os_ * hs)], ix[key(b[4] + ox * hx)]]
                    for k8 in range(8):
                        r_ = vals[k8] / sup[k8] if sup[k8] > 0 else (np.inf if vals[k8] > 0 else 0.0)
                        worst = max(worst, r_)
                        viol += int(r_ > 1)
    return worst, viol, npts


def census(tau):
    """D3: certified values at K1's points, every one kept, mapped to K2's boxes"""
    t0 = time.time()
    C3, g, md5s = load_pinned()
    assert md5s == MD5
    frame, names = frame_cached()
    Nt = Ns = 24
    M = g['M']
    x1 = float(np.cos(np.pi / (2 * M)))
    tcs = [-1 + (2 * p + 1) / Nt for p in range(Nt)]
    scs = [-1 + (2 * q + 1) / Ns for q in range(Ns)]
    xcs, _ = R5.x_boxes(x1, n_mid=8)
    vals, _ = grid_values(C3, g, frame, names, tcs, scs, xcs)
    xb, hb = R5.x_boxes(x1, n_mid=6)
    boxes = {}
    for p, q, r in itertools.product(range(Nt), range(Ns), range(len(xcs))):
        bt, bs = min(int((tcs[p] + 1) / 0.5), 3), min(int((scs[q] + 1) / 0.5), 3)
        br = [i for i, (c_, h_) in enumerate(zip(xb, hb)) if c_ - h_ <= xcs[r] <= c_ + h_]
        for b_ in br:
            key = (bt, bs, b_)
            boxes[key] = max(boxes.get(key, 0.0), vals[p, q, r].max())
    over = sum(1 for v_ in boxes.values() if v_ > tau)
    over2 = sum(1 for v_ in boxes.values() if v_ > TAU_G10)
    inner = [k for k in boxes if k[0] == 1 and k[1] == 1 and xb[k[2]] - hb[k[2]] >= -1e-12 and
             xb[k[2]] + hb[k[2]] <= 0.25 + 1e-12]
    np.save(os.path.join(SCR, 'census_vals.npy'), vals)
    print('D3 (certified) K1\'s %d points, certified lower bounds of |component|, over K2\'s %d boxes with points '
          '(%.0f s):' % (vals[..., 0].size, len(boxes), time.time() - t0))
    print('   boxes holding a point above tau = %.1e: %d of %d (no certificate at tau possible there); above tau\' = '
          '%.1e: %d of %d' % (tau, over, len(boxes), TAU_G10, over2, len(boxes)))
    print('   largest certified lower bound over all points: %.3e; per component: %s' % (
        vals.max(), ', '.join('%s %.2e' % (k, vals[..., i].max()) for i, k in enumerate(FRL))))
    return boxes


if __name__ == '__main__':
    if sys.argv[1] == '--worker':
        worker(int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]) if len(sys.argv) > 4 else 5.3e-4)
    elif sys.argv[1] == '--repartition':
        W, W2 = int(sys.argv[2]), int(sys.argv[3]); tau = float(sys.argv[4]) if len(sys.argv) > 4 else 5.3e-4
        sts = []
        for w in range(W):
            with open(os.path.join(SCR, 'ck_%d_of_%d_tau%.1e.pkl' % (w, W, tau)), 'rb') as fh:
                sts.append(pickle.load(fh))
        queue = sorted(sum((st['queue'] for st in sts), []), key=lambda e: e[1])
        for w2 in range(W2):
            st = dict(queue=queue[w2::W2], acc=[], nparents=0, nboxes=0, cpu=0.0, wall=0.0, maxdepth=1, wall0=0.0)
            if w2 == 0:
                st['acc'] = sum((s_['acc'] for s_ in sts), [])
                for k_ in ('nparents', 'nboxes', 'cpu'):
                    st[k_] = sum(s_[k_] for s_ in sts)
                st['wall0'] = max(s_['wall'] + s_.get('wall0', 0.0) for s_ in sts)
                st['maxdepth'] = max(s_['maxdepth'] for s_ in sts)
                st['history'] = [(W, s_['nboxes'], s_['cpu'], s_['wall']) for s_ in sts]
            with open(os.path.join(SCR, 'ck_%d_of_%d_tau%.1e.pkl' % (w2, W2, tau)), 'wb') as fh:
                pickle.dump(st, fh)
        print('repartitioned %d checkpoints (%d queued, %d accepted) into %d' % (W, len(queue), sum(
            len(s_['acc']) for s_ in sts), W2))
    elif sys.argv[1] == '--census':
        os.makedirs(SCR, exist_ok=True)
        census(float(sys.argv[2]) if len(sys.argv) > 2 else 5.3e-4)
    elif sys.argv[1] == '--collect':
        sys.exit(collect(int(sys.argv[2]), float(sys.argv[3]) if len(sys.argv) > 3 else 5.3e-4))
