#!/usr/bin/env python3
"""cp3grid5.py -- CERTIFY-10L5-RESULT.md round 5 (the late region): the regularised constraint-preserving scheme of
cpaxis5.py on three null grids, 400 x 180, 800 x 360 and 1600 x 720 (M = 32), with 1600 x 720 at M = 40 for the angle.
Labels: computed (floating point) throughout.

Round 4 (8.5, A5-A6) had two null grids, which give no order of convergence: from v = 1.8 r_h at areal radius 0.9-1.2
the unimposed Ric_xx monitor changed by a factor of only 1.03-1.6 from 400 to 800 rows, and a pre-asymptotic regime
could not be told from a non-vacuum limit.  The 1600-row runs are written from v = 1.4 only (cpaxis5.py --run ...
vsave 1.4); every comparison here is on the 400-row nodes, the finer grids sampled every second and fourth node in
(u, v) (the grids nest exactly; the v-offset of the 1600-row files is matched by value).

  A7 per band of v in [1.4, 2.25] and areal radius 0.9-1.0, 1.0-1.2, >= 1.2: the interior monitor max |Ric_xx|
     (|x| <= 0.9) at 400, 800 and 1600 rows; the ratios m400/m800 and m800/m1600 (4 at second order, 1 for a
     persistent violation); max |P_400 - P_800| and |P_800 - P_1600| and their ratio, with the observed order
     log2 of it; and at 1600 rows the monitor at M = 40 against M = 32.
     Verdict per band: 'second order' if both monitor ratios and the P ratio lie in [3, 5.5] and the M ratio in
     [1/1.5, 1.5]; 'converging' if the last monitor ratio and the P ratio are >= 2; 'not converging' if the last
     monitor ratio is below 1.5; otherwise 'undecided'.
  A8 the Kretschmann scalar (dnsolve5.kretschmann, as cpaxis5.py A6) on the same 24 u-rows, at x = 0.97, 0.5, 0,
     -0.5, -0.97, per band of v in [1.5, 2.25] at areal radius 1.0-1.4: dev = max |K/K_0 - 1| at 1600 rows M = 32,
     the null-step differences |K_400 - K_800| and |K_800 - K_1600| over K_0 with their ratio, and the angular
     difference |K_32 - K_40| at 1600 rows.  'resolved' where the finest null-step and angular differences are below
     5 % of dev and the null-step ratio is >= 2.
  Control: A7 run with the 800-row file given twice in place of 800 and 1600 must report a ratio of exactly 1 and
     'not converging' on every band (the verdict code cannot pass a persistent violation).

  python3 checks/cp3grid5.py --a7 M32_400.npz M32_800.npz M32_1600.npz M40_1600.npz
  python3 checks/cp3grid5.py --a8 M32_400.npz M32_800.npz M32_1600.npz M40_1600.npz
  python3 checks/cp3grid5.py --control M32_400.npz M32_800.npz M40_800.npz
"""
import os, sys, time, importlib.util
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('cpsolve5', os.path.join(HERE, 'cpsolve5.py'))
CP = importlib.util.module_from_spec(_s); _s.loader.exec_module(CP)
print = CP.print
d5 = CP.d5
BANDS7 = ((1.4, 1.5), (1.5, 1.65), (1.65, 1.8), (1.8, 1.9), (1.9, 2.0), (2.0, 2.25))
CLASSES = (('0.9-1.0', (0.9, 1.0)), ('1.0-1.2', (1.0, 1.2)), ('>= 1.2', (1.2, 99.0)))


def on400(z, v400, sub):
    """indices (rows, cols) of file z sampled on the 400-row nodes: rows every `sub`, columns matched by v"""
    vz = z['v']
    jv = np.full(len(v400), -1)
    for j, vv in enumerate(v400):
        k = np.nonzero(np.abs(vz - vv) < 1e-9)[0]
        if k.size:
            jv[j] = k[0]
    return slice(None, None, sub), jv


def field(z, name, rs, jv):
    A = z[name][rs]
    out = np.full((A.shape[0], len(jv)) + A.shape[2:], np.nan)
    ok = jv >= 0
    out[:, ok] = A[:, jv[ok]]
    return out


def mask(z, rs, jv):
    A = z['mask'][rs]
    out = np.ones((A.shape[0], len(jv)), bool)
    ok = jv >= 0
    out[:, ok] = A[:, jv[ok]]
    return out


def a7(paths, label='A7'):
    Z = [np.load(p_) for p_ in paths]
    v4 = Z[0]['v']
    n4 = len(Z[0]['u'])
    subs = [(len(z['u']) - 1) // (n4 - 1) for z in Z]
    assert all(np.allclose(z['u'][::s_], Z[0]['u']) for z, s_ in zip(Z, subs)), 'the grids do not nest'
    idx = [on400(z, v4, s_) for z, s_ in zip(Z, subs)]
    x = Z[0]['x']
    P = []
    for z, (rs, jv) in zip(Z, idx):
        m_, n_ = field(z, 'm', rs, jv), field(z, 'n', rs, jv)
        xx = z['x']
        P.append((2 * (1 + xx) * m_ - (1 - xx) * n_) / 3)
    keep = ~mask(Z[0], *idx[0]) & ~mask(Z[1], *idx[1]) & ~mask(Z[2], *idx[2]) & ~mask(Z[3], *idx[3])
    Rm = Z[0]['R'][..., len(x) // 2]
    print('%s the regularised scheme, cut 0.9, on three null grids (M = 32) and at 1600 rows M = 40; every quantity on '
          'the 400-row nodes kept by all four runs:' % label)
    verdicts = {}
    for cls, (lo, hi) in CLASSES:
        print('  areal radius %s:' % cls)
        for vb in BANDS7:
            jv = (v4 >= vb[0]) & (v4 < vb[1])
            sel = keep[:, jv] & (Rm[:, jv] >= lo) & (Rm[:, jv] < hi)
            if not sel.any():
                print('   v in [%.2f, %.2f): no cells' % vb); continue
            mon = []
            for z, (rs, jvz) in zip(Z, idx):
                cx = field(z, 'cx', rs, jvz)[:, jv][sel]
                xz = z['x']
                mon.append(float(np.nanmax(np.abs(cx[:, np.abs(xz) <= 0.9]))))
            d1 = float(np.nanmax(np.abs(P[0][:, jv][sel] - P[1][:, jv][sel])))
            d2 = float(np.nanmax(np.abs(P[1][:, jv][sel] - P[2][:, jv][sel])))
            r1, r2 = mon[0] / mon[1], mon[1] / mon[2]
            rp = d1 / d2 if d2 > 0 else np.inf
            rm = mon[3] / mon[2]
            if 3 <= r1 <= 5.5 and 3 <= r2 <= 5.5 and 3 <= rp <= 5.5 and 1 / 1.5 <= rm <= 1.5:
                vd = 'second order'
            elif r2 >= 2 and rp >= 2:
                vd = 'converging'
            elif r2 < 1.5:
                vd = 'not converging'
            else:
                vd = 'undecided'
            verdicts[(cls, vb)] = vd
            print('   v in [%.2f, %.2f): monitor %.3g, %.3g, %.3g (ratios %.2f, %.2f); M40/M32 at 1600: %.2f; |dP| '
                  '%.2e, %.2e (ratio %.2f, order %.2f) -> %s' % (vb[0], vb[1], mon[0], mon[1], mon[2], r1, r2, rm, d1,
                                                                d2, rp, np.log2(rp) if rp > 0 else np.nan, vd))
    return verdicts


def a8(paths):
    Z4 = np.load(paths[0])
    R4, mask4, v4 = Z4['R'], Z4['mask'], Z4['v']
    Rm = np.nanmean(R4, axis=2)
    vin = (v4 >= 1.5) & (v4 <= 2.25)
    ok_rows = [i for i in range(1, R4.shape[0] - 1) if np.any(~mask4[i] & vin & (Rm[i] >= 0.95) & (Rm[i] <= 1.5))]
    rows4 = [ok_rows[k] for k in np.linspace(0, len(ok_rows) - 1, 24).round().astype(int)] \
        if len(ok_rows) > 24 else ok_rows
    Ks = []
    for path in paths:
        with np.load(path) as F:
            Nu = F['u'].shape[0]
            fac = (Nu - 1) // (R4.shape[0] - 1)
            rows = [fac * r for r in rows4]
            ridx = np.array([r + d for r in rows for d in (-1, 0, 1)])
            Zr = {k: (F[k][ridx] if (F[k].ndim >= 1 and F[k].shape[0] == Nu) else F[k]) for k in F.files}
        sub = [3 * k + 1 for k in range(len(rows))]
        K = d5.kretschmann(Zr, rows=sub)[sub]
        vz = Zr['v']
        jv = np.full(len(v4), -1)
        for j, vv in enumerate(v4):
            k_ = np.nonzero(np.abs(vz - vv) < 1e-9)[0]
            if k_.size:
                jv[j] = k_[0]
        okc = jv >= 0
        Kp = np.full((K.shape[0], len(v4), K.shape[2]), np.nan); Kp[:, okc] = K[:, jv[okc]]
        Rp = np.full_like(Kp, np.nan); Rp[:, okc] = Zr['R'][sub][:, jv[okc]]
        Mp = np.ones((K.shape[0], len(v4)), bool); Mp[:, okc] = Zr['mask'][sub][:, jv[okc]]
        Ks.append((Kp, Rp, Mp, Zr['x']))
    bands = ((1.5, 1.65), (1.65, 1.8), (1.8, 1.9), (1.9, 2.0), (2.0, 2.25))
    xs = (0.97, 0.5, 0.0, -0.5, -0.97)

    def cheb_x(Kc, xn, xe):
        M_ = len(xn); j = np.arange(M_)
        t = (-1.0) ** j * np.sin((2 * j + 1) * np.pi / (2 * M_)) / (xe - xn)
        return Kc @ (t / t.sum())
    print('A8 the Kretschmann scalar on %d u-rows: dev = max |K/K_0 - 1| (1600 rows, M = 32); the null-step '
          'differences 400-800 and 800-1600 (M = 32) and the angular difference M = 32-40 (1600 rows), over K_0, at '
          'areal radius 1.0-1.4:' % len(rows4))
    out = {}
    for xe in xs:
        print('  x = %+.2f:' % xe)
        for vb in bands:
            jv = (v4 >= vb[0]) & (v4 < vb[1])
            k = [cheb_x(Kp, xn, xe) for Kp, _, _, xn in Ks]
            Rr = np.nanmean(Ks[2][1], axis=2)
            K0 = 72.0 / Rr ** 8
            sel = jv[None, :] & (Rr >= 1.0) & (Rr <= 1.4)
            for _, _, Mp, _ in Ks:
                sel &= ~Mp
            sel &= np.all(np.isfinite(np.stack(k)), axis=0)
            if not sel.any():
                print('   v in [%.2f, %.2f): no cells' % vb); continue
            dev = float(np.nanmax(np.abs(k[2] / K0 - 1)[sel]))
            n1 = float(np.nanmax(np.abs(k[0] - k[1])[sel] / K0[sel]))
            n2 = float(np.nanmax(np.abs(k[1] - k[2])[sel] / K0[sel]))
            dm = float(np.nanmax(np.abs(k[2] - k[3])[sel] / K0[sel]))
            rr = n1 / n2 if n2 > 0 else np.inf
            vd = 'resolved' if (max(n2, dm) < 0.05 * max(dev, 1e-3) and rr >= 2) else 'not resolved'
            out[(xe, vb)] = vd
            print('   v in [%.2f, %.2f): dev %.3g; null step %.2e, %.2e (ratio %.2f); in M %.2e -> %s' % (
                vb[0], vb[1], dev, n1, n2, rr, dm, vd))
    return out


def main():
    a = sys.argv[1:]
    t0 = time.time()
    if a[0] == '--a7':
        a7(a[1:5])
    elif a[0] == '--a8':
        a8(a[1:5])
    elif a[0] == '--control':
        # the 800-row file twice (and the M = 40 800-row file as the 'angle' run): every last ratio is exactly 1
        v = a7([a[1], a[2], a[2], a[3]], label='control (A7 with 800 given for 1600)')
        bad = [k for k, vd in v.items() if vd != 'not converging']
        print('control: %d bands, verdicts other than \'not converging\': %d -> %s' % (
            len(v), len(bad), 'the verdict code refuses a persistent violation (good)' if not bad else 'BAD'))
    print('cp3grid5 %s (%.0f s)' % (a[0], time.time() - t0))


if __name__ == '__main__':
    sys.exit(main())
