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
  A8 the Kretschmann scalar (dnsolve5.kretschmann, as cpaxis5.py A6) on 32 u-rows of the 400-row grid crossing kept
     cells with areal radius in [0.85, 1.5], at x = 0.97, 0.5, 0, -0.5, -0.97, per band of v in [1.5, 2.25] and per
     areal-radius class 0.9-1.0, 1.0-1.2, 1.2-1.4 (the verifier of round 4, m3: A6 merged 1.0-1.4): dev = max
     |K/K_0 - 1| at the finest null grid (M = 32), the successive null-step differences over K_0 (with their ratio
     when three grids are given), and the angular difference M = 32-40 at the finest grid.  'resolved' where the
     finest null-step and angular differences are below 5 % of dev (and, with three grids, the ratio is >= 2).  It
     takes the M = 32 null grids coarse to fine, then the M = 40 run: two grids (round 4's 400, 800 and 800 at M = 40)
     or three.
  A9 |P_32 - P_40| per areal-radius class and v-band at one null grid, M = 40 interpolated to M = 32's nodes by its
     Chebyshev series (the verifier of round 4's pm_class.py, re-derived).
  A10 (the verifier of round 4, m4) the regularisation's correction d_-, d_+ (cpaxis5.py solve_reg), replayed at every
     cell from the stored solution by the same formula on the same corner values: max |d+-| per band and areal-radius
     class, with max |d+-|/max |R_uv|, at each grid given, and the ratios between successive grids (4 if it is
     O(the truncation error) at second order; near 1 if it persists).
  [Round 7: the M = 32 run at 1600 rows finished first.  --a7 without the M = 40 file, and --a8m32, give every
     null-step quantity and verdict as before and print the M = 40 comparison as pending; with the M = 40 file the
     code paths and verdicts are those of round 5.  --dpm compares a vsave file (v >= 1.4) only on bands it covers
     whole.]
  Control: A7 run with the 800-row file given twice in place of 800 and 1600 must report a ratio of exactly 1 and
     'not converging' on every band (the verdict code cannot pass a persistent violation).

  python3 checks/cp3grid5.py --a7 M32_400.npz M32_800.npz M32_1600.npz [M40_1600.npz]
  python3 checks/cp3grid5.py --a8 M32_400.npz M32_800.npz [M32_1600.npz] M40_finest.npz
  python3 checks/cp3grid5.py --a8m32 M32_400.npz M32_800.npz M32_1600.npz       (A8 with the M = 40 run pending)
  python3 checks/cp3grid5.py --pclass M32.npz M40.npz                  (A9)
  python3 checks/cp3grid5.py --dpm M32_400.npz M32_800.npz [M32_1600.npz]   (A10)
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
    keep = np.ones(Z[0]['mask'].shape, bool)
    for z, ix in zip(Z, idx):
        keep &= ~mask(z, *ix)
    Rm = Z[0]['R'][..., len(x) // 2]
    m40 = len(Z) == 4                  # round 7: without the M = 40 file the M ratio is pending, the rest unchanged
    print('%s the regularised scheme, cut 0.9, on three null grids (M = 32)%s; every quantity on the 400-row nodes kept '
          'by all %d runs:' % (label, ' and at 1600 rows M = 40' if m40 else ' (M = 40 at 1600 rows pending)', len(Z)))
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
            rm = mon[3] / mon[2] if m40 else np.nan
            if 3 <= r1 <= 5.5 and 3 <= r2 <= 5.5 and 3 <= rp <= 5.5 and (not m40 or 1 / 1.5 <= rm <= 1.5):
                vd = 'second order' if m40 else 'second order in the null step (M pending)'
            elif r2 >= 2 and rp >= 2:
                vd = 'converging'
            elif r2 < 1.5:
                vd = 'not converging'
            else:
                vd = 'undecided'
            verdicts[(cls, vb)] = vd
            print('   v in [%.2f, %.2f): monitor %.3g, %.3g, %.3g (ratios %.2f, %.2f); M40/M32 at 1600: %s; |dP| '
                  '%.2e, %.2e (ratio %.2f, order %.2f) -> %s' % (vb[0], vb[1], mon[0], mon[1], mon[2], r1, r2,
                                                                '%.2f' % rm if m40 else 'pending', d1, d2, rp,
                                                                np.log2(rp) if rp > 0 else np.nan, vd))
    return verdicts


def a8(paths, m40=True):
    """the Kretschmann scalar on the null grids paths[:-1] (M = 32, coarse to fine) and paths[-1] (M = 40, at the
    finest null grid), per areal-radius class (the verifier of round 4, m3: A6 merged 1.0-1.4); with m40 False
    (round 7, --a8m32) every path is an M = 32 null grid and the angular difference is pending"""
    Z4 = np.load(paths[0])
    R4, mask4, v4 = Z4['R'], Z4['mask'], Z4['v']
    Rm = np.nanmean(R4, axis=2)
    vin = (v4 >= 1.5) & (v4 <= 2.25)
    ok_rows = [i for i in range(1, R4.shape[0] - 1) if np.any(~mask4[i] & vin & (Rm[i] >= 0.85) & (Rm[i] <= 1.5))]
    rows4 = [ok_rows[k] for k in np.linspace(0, len(ok_rows) - 1, 32).round().astype(int)] \
        if len(ok_rows) > 32 else ok_rows
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
    ng = len(paths) - 1 if m40 else len(paths)

    def cheb_x(Kc, xn, xe):
        M_ = len(xn); j = np.arange(M_)
        t = (-1.0) ** j * np.sin((2 * j + 1) * np.pi / (2 * M_)) / (xe - xn)
        return Kc @ (t / t.sum())
    print('A8 the Kretschmann scalar on %d u-rows, at %d null grids (M = 32)%s: dev = max '
          '|K/K_0 - 1| (finest, M = 32); the successive null-step differences and the angular difference, over K_0; '
          'per areal-radius class (K_0 = 72/R^8):' % (len(rows4), ng, ' and M = 40 at the finest' if m40 else
                                                     ', M = 40 at the finest pending'))
    out = {}
    for cls, (lo, hi) in (('0.9-1.0', (0.9, 1.0)), ('1.0-1.2', (1.0, 1.2)), ('1.2-1.4', (1.2, 1.4))):
        print(' areal radius %s:' % cls)
        for xe in xs:
            print('  x = %+.2f:' % xe)
            for vb in bands:
                jv = (v4 >= vb[0]) & (v4 < vb[1])
                k = [cheb_x(Kp, xn, xe) for Kp, _, _, xn in Ks]
                Rr = np.nanmean(Ks[ng - 1][1], axis=2)
                K0 = 72.0 / Rr ** 8
                sel = jv[None, :] & (Rr >= lo) & (Rr < hi)
                for _, _, Mp, _ in Ks:
                    sel &= ~Mp
                sel &= np.all(np.isfinite(np.stack(k)), axis=0)
                if not sel.any():
                    print('   v in [%.2f, %.2f): no cells' % vb); continue
                dev = float(np.nanmax(np.abs(k[ng - 1] / K0 - 1)[sel]))
                dn = [float(np.nanmax(np.abs(k[i] - k[i + 1])[sel] / K0[sel])) for i in range(ng - 1)]
                dm = float(np.nanmax(np.abs(k[ng - 1] - k[ng])[sel] / K0[sel])) if m40 else np.nan
                rr = dn[-2] / dn[-1] if ng >= 3 and dn[-1] > 0 else np.nan
                vd = 'resolved' if (max(dn[-1], dm if m40 else 0.0) < 0.05 * max(dev, 1e-3) and (ng < 3 or rr >= 2)) \
                    else 'not resolved'
                if not m40:
                    vd += ' in the null step'
                out[(cls, xe, vb)] = vd
                print('   v in [%.2f, %.2f): dev %.3g; null step %s%s; in M %s -> %s' % (
                    vb[0], vb[1], dev, ', '.join('%.2e' % q for q in dn),
                    ' (ratio %.2f)' % rr if ng >= 3 else '', '%.2e' % dm if m40 else 'pending', vd))
    return out


def pclass(pa, pb):
    """|P_32 - P_40| per areal-radius class and v-band, M = 40 interpolated to M = 32's nodes by its Chebyshev series
    (the verifier of round 4's pm_class.py, re-derived), on all kept cells of the finer file's common nodes"""
    za, zb = np.load(pa), np.load(pb)
    xa, xb = za['x'], zb['x']; Mb = len(xb)
    Tbi = np.linalg.inv(np.cos(np.outer(np.arange(Mb), np.arccos(xb))).T)
    Ta = np.cos(np.outer(np.arange(Mb), np.arccos(xa)))
    keep = (~za['mask']) & (~zb['mask'])
    Pa = (2 * (1 + xa) * za['m'] - (1 - xa) * za['n']) / 3
    Pb = (2 * (1 + xb) * zb['m'] - (1 - xb) * zb['n']) / 3
    Pbi = np.einsum('...j,kj,ki->...i', Pb, Tbi, Ta)
    R = za['R'][..., len(xa) // 2]; v = za['v']
    print('A9 |P_32 - P_40| (M = 40 interpolated to M = 32\'s nodes), %d rows, per areal-radius class and v-band:'
          % (len(za['u']) - 1))
    for cls, (lo, hi) in CLASSES:
        row = []
        for vb in ((0.5, 1.0), (1.0, 1.5), (1.5, 1.65), (1.65, 1.8), (1.8, 1.9), (1.9, 2.0), (2.0, 2.25)):
            jv = (v >= vb[0]) & (v < vb[1])
            if not jv.any():
                continue
            sel = keep[:, jv] & (R[:, jv] >= lo) & (R[:, jv] < hi)
            d = np.abs(Pa[:, jv][sel] - Pbi[:, jv][sel])
            row.append('[%.2f, %.2f) %.1e' % (vb[0], vb[1], d.max() if d.size else np.nan))
        print('   %s: %s' % (cls, '; '.join(row)))


def dpm(path, ld=3):
    """the regularisation's correction d_-, d_+ (cpaxis5.solve_reg) replayed at every cell from the stored solution:
    the same formula on the same corner values, so the correction the scheme's last iteration applied (up to that
    iteration's convergence); per band and areal-radius class, max |d+-| and max |d+-|/max |R_uv|"""
    import importlib.util as iu
    sp_ = iu.spec_from_file_location('cpaxis5', os.path.join(HERE, 'cpaxis5.py'))
    CA = iu.module_from_spec(sp_); sp_.loader.exec_module(CA)
    Z = np.load(path)
    u, v, x = Z['u'], Z['v'], Z['x']
    M = len(x); Nu = len(u) - 1
    dv = v[1] - v[0]
    nv_full = int(round(2.25 / dv))
    G = d5.Grid(M, -10.0, float(-Z['rcut']), Nu, 0.0, 2.25, nv_full, a=0.002, ld=ld)
    assert np.allclose(G.u, u) and np.allclose(G.v[-len(v):], v), 'grid mismatch'
    E = d5.Eqs()
    A = {f: Z[f] for f in CP.ALL}
    mask = Z['mask']
    acc = {}
    for n1 in range(1, Nu + 1):
        m1 = np.arange(1, len(v))
        S = (n1 - 1, m1 - 1); Ec = (n1 - 1, m1); Wc = (n1, m1 - 1); Nc = (n1, m1)
        ok = ~(mask[S] | mask[Ec] | mask[Wc] | mask[Nc])
        if not ok.any():
            continue
        m1 = m1[ok]
        S = (n1 - 1, m1 - 1); Ec = (n1 - 1, m1); Wc = (n1, m1 - 1); Nc = (n1, m1)
        s_, e_, w_, nn = ({f: A[f][S] for f in CP.ALL}, {f: A[f][Ec] for f in CP.ALL}, {f: A[f][Wc] for f in CP.ALL},
                          {f: A[f][Nc] for f in CP.ALL})
        du = G.du[n1 - 1]
        c = {f: 0.25 * (s_[f] + e_[f] + w_[f] + nn[f]) for f in CP.ALL}
        fu = {f: (w_[f] - s_[f] + nn[f] - e_[f]) / (2 * du) for f in CP.FIELDS}
        fv = {f: (e_[f] - s_[f] + nn[f] - w_[f]) / (2 * G.dv) for f in CP.FIELDS}
        env = d5.env_from(G, c, fu, fv, c['sv'])
        Ruv = (nn['R'] - e_['R'] - w_['R'] + s_['R']) / (du * G.dv)
        sol, _ = CA._orig_solve(E, env, Ruv, G)
        sol1, _ = CA._orig_solve(E, env, Ruv + 1.0, G)
        sig = sol1 - sol
        gm = (1 + x) * sol[..., 0]; gs_m = (1 + x) * sig[..., 0]
        gn = (1 - x) * sol[..., 1]; gs_n = (1 - x) * sig[..., 1]
        Sm, Sigm = CA.cheb_at(gm, x, -1.0), CA.cheb_at(gs_m, x, -1.0)
        Sn, Sign_ = CA.cheb_at(gn, x, 1.0), CA.cheb_at(gs_n, x, 1.0)
        with np.errstate(all='ignore'):
            dm = np.where(np.abs(Sigm) > 0, -Sm / Sigm, 0.0)
            dp = np.where(np.abs(Sign_) > 0, -Sn / Sign_, 0.0)
        Rc = c['R'][..., M // 2]
        vc = 0.5 * (v[m1 - 1] + v[m1])
        for cls, (lo, hi) in CLASSES:
            for vb in BANDS_D:
                selc = (vc >= vb[0]) & (vc < vb[1]) & (Rc >= lo) & (Rc < hi)
                if not selc.any():
                    continue
                key = (cls, vb)
                a_ = acc.get(key, [0.0, 0.0])
                a_[0] = max(a_[0], float(np.nanmax(np.maximum(np.abs(dm[selc]), np.abs(dp[selc])))))
                a_[1] = max(a_[1], float(np.nanmax(np.abs(Ruv[selc]))))
                acc[key] = a_
    return acc, Nu


BANDS_D = ((0.5, 1.0), (1.0, 1.5), (1.5, 1.65), (1.65, 1.8), (1.8, 1.9), (1.9, 2.0), (2.0, 2.25))


def dpm_report(paths):
    res = [dpm(p_) for p_ in paths]
    # round 7: a file written from vsave on (the 1600-row runs, v >= 1.4) is compared only on bands it covers whole
    vmin = max(float(np.load(p_)['v'][0]) for p_ in paths)
    print('A10 the regularisation\'s correction d+- (cpaxis5.py A3), replayed at every cell from the stored solution: '
          'max |d+-| per band and areal-radius class, with max |d+-|/max |R_uv| in brackets, at %s rows, and the '
          'successive ratios:' % ', '.join(str(n) for _, n in res))
    for cls, _ in CLASSES:
        print('  areal radius %s:' % cls)
        for vb in BANDS_D:
            vals = [r.get((cls, vb)) for r, _ in res]
            if any(q is None for q in vals) or vb[0] < vmin - 1e-9:
                continue
            rat = ['%.2f' % (vals[i][0] / vals[i + 1][0]) if vals[i + 1][0] > 0 else 'inf' for i in range(len(vals) - 1)]
            print('   v in [%.2f, %.2f): %s; ratios %s' % (vb[0], vb[1], ', '.join('%.2e [%.1e]' % (q[0], q[0] / q[1])
                                                                                 for q in vals), ', '.join(rat)))


def main():
    a = sys.argv[1:]
    t0 = time.time()
    if a[0] == '--a7':
        a7(a[1:5])
    elif a[0] == '--a8':
        a8(a[1:])
    elif a[0] == '--a8m32':
        a8(a[1:], m40=False)
    elif a[0] == '--pclass':
        pclass(a[1], a[2])
    elif a[0] == '--dpm':
        dpm_report(a[1:])
    elif a[0] == '--control':
        # the 800-row file twice (and the M = 40 800-row file as the 'angle' run): every last ratio is exactly 1
        v = a7([a[1], a[2], a[2], a[3]], label='control (A7 with 800 given for 1600)')
        bad = [k for k, vd in v.items() if vd != 'not converging']
        print('control: %d bands, verdicts other than \'not converging\': %d -> %s' % (
            len(v), len(bad), 'the verdict code refuses a persistent violation (good)' if not bad else 'BAD'))
    print('cp3grid5 %s (%.0f s)' % (a[0], time.time() - t0))


if __name__ == '__main__':
    sys.exit(main())
