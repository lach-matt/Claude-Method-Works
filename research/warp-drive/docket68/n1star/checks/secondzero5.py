#!/usr/bin/env python3
"""secondzero5.py -- CERTIFY-10L5-RESULT.md section 1: is the second zero of the expansion physical?  Labels: computed
(floating point) on double-null runs; the deductions they test are in the note (D1, D2) with their exact identities in
sectexp5.py (X1, X2).

Two different 'second zeros' are on record, and they are different objects:
  (a) growth5.py's: the outgoing expansion T of the spheres {v, r} of its Bondi chart, along a Bondi column (fixed
      angular label, r varying), acquires a second zero at the excision boundary, from v = 1.50 (seed 1) and 1.583
      (seed 2);
  (b) CERTIFY-10L5.md D344's: R_v, the outgoing expansion of dnsolve5's double-null leaves, along an ingoing cone at a
      fixed node, acquired a second zero at v = 1.425.
By D1 (sectexp5.py X1: e^{-2W} R_v is nonincreasing along every outgoing generator in vacuum, and R_v < 0 on the first
cone for u > -1) the exact solution has R_v < 0 at every point with u > -1: a zero of type (b) there is not the exact
solution's.  By D2 (X2 (b)) no section of an ingoing cone with theta >= 0 at its innermost point has that point in
u > -1.  The checks measure the runs against these facts, and rebuild (a) in the double-null formulation.

  S1 every kept cell with u > -1, v <= 1.85, a valid v-stencil and at least k rows from the cut has R_v < 0
     (k = Nu/40); the violations, if any, lie within k rows of the cut.  The same count on (1.85, 2] is reported.  Control: the same test over u > -1.02, which includes leaves
     outside the seed's horizon generator, must fail.
  S2 every second (and further) zero of R_v along an ingoing cone at a fixed node lies at u > -1 within k rows of the
     cut, so by D1 none is the exact solution's.  Control: the classifier applied to the first zero must fail (the
     first zero is the apparent horizon, at u < -1 and far from the cut).
  S3 the Bondi spheres rebuilt on the seed (v = 0.3 < 1/2, exact Tangherlini there): X = xi, U constant and theta =
     the run's own 3 R_v/R at the same points, to 1e-9 (the error against exact Tangherlini is reported beside it).
  S4 the outer zero r_AH(x) of the Bondi spheres' expansion, per Bondi column, rebuilt from the double-null run, against
     growth5.py's own recorded zeros (data/growth5_runs.json, the deeper-excision run L100_lam1_28x16_d0_y1.6, whose
     exterior is fixed by its data until its own breakdown at v = 1.41, growth5's columns x = cos(pi k/16)): agreement
     within 0.1 r_h at v = 1.0, 1.2, 1.3, 1.35, 1.375.  Control: the leaves' expansion 3 R_v/R taken at the same
     points in place of theta must disagree with growth5 by more than 0.1 somewhere (the tilt matters).
  S5 the second zero itself: per Bondi column, the zeros of theta on r in [r_lo, 1.6]; the first v at which a column
     has more than one zero, or none, with the inner zero's radius; and the first v at which the sphere r = r_core
     (growth5's excision radius) has theta > 0 somewhere.  Reported (no pass/fail without a converged inner region).

  python3 checks/secondzero5.py RUNDIR [run names ...]
"""
import os, sys, json, warnings
import numpy as np
warnings.filterwarnings('ignore')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import bondisph5 as B                                                           # noqa: E402

G5 = os.path.join(os.path.dirname(HERE), 'data', 'growth5_runs.json')
XG = np.cos(np.pi * np.arange(17) / 16)
VMAX = 1.85                  # the record's converged region at seed 1 ends near v = 1.65-1.9 (CERTIFY-10L5.md 6b)


def rv_field(Z):
    R, v, mask = Z['R'], Z['v'], Z['mask']
    dv = v[1] - v[0]
    Rv = np.full_like(R, np.nan)
    Rv[:, 1:-1] = (R[:, 2:] - R[:, :-2]) / (2 * dv)
    ok = ~mask
    okv = np.zeros_like(ok); okv[:, 1:-1] = ok[:, 1:-1] & ok[:, 2:] & ok[:, :-2]
    return np.where(okv[..., None], Rv, np.nan), okv


def last_rows(Z):
    ok = ~Z['mask']
    return np.array([np.nonzero(ok[:, j])[0].max() if ok[:, j].any() else -1 for j in range(ok.shape[1])])


def s1(Z, umin=-1.0, vmax=VMAX, vmin=0.0):
    Rv, okv = rv_field(Z)
    u, v = Z['u'], Z['v']
    k = (len(u) - 1) // 40
    last = last_rows(Z)
    far = np.zeros_like(okv)
    for j in range(len(v)):
        far[:last[j] - k + 1, j] = True
    sel = okv & (u[:, None] > umin) & (v[None, :] <= vmax) & (v[None, :] > vmin)
    pos = sel[..., None] & (Rv > 0)
    n_far = int((pos & far[..., None]).sum()); n_near = int((pos & ~far[..., None]).sum())
    return n_far == 0, n_far, n_near, k, int(sel.sum())


def zeros_along(Z, vmax=VMAX, vmin=0.0):
    """for every column j and node: the zeros of R_v in u, with their row index"""
    Rv, okv = rv_field(Z)
    u, v = Z['u'], Z['v']
    out = []
    for j in range(len(v)):
        if v[j] > vmax:
            break
        if v[j] <= vmin:
            continue
        for kx in range(len(Z['x'])):
            c = Rv[:, j, kx]; f = np.nonzero(np.isfinite(c))[0]
            if len(f) < 2:
                continue
            cc = c[f]
            idx = np.nonzero(np.sign(cc[1:]) != np.sign(cc[:-1]))[0]
            if len(idx):
                out.append((j, kx, [int(f[i]) for i in idx]))
    return out


def s2(Z, control=False, vmax=VMAX, vmin=0.0):
    u = Z['u']; k = (len(u) - 1) // 40
    last = last_rows(Z)
    bad, extra, first_near = 0, 0, 0
    first_v = None
    for j, kx, rows in zeros_along(Z, vmax, vmin):
        for q, i in enumerate(rows):
            near = (u[i] > -1) and (last[j] - i < k)
            if q == 0:
                first_near += near
            else:
                extra += 1
                first_v = Z['v'][j] if first_v is None else first_v
                bad += not near
    if control:
        return first_near > 0
    return bad == 0, extra, first_v, k


def s3(Z, F):
    """on the seed (v = 0.3 < 1/2) the rebuilt spheres must be the leaves: X = xi, U constant, and theta equal to the
    run's own 3 R_v/R at the same points (exactly, the tilt terms vanishing); the error against exact Tangherlini,
    3 (1 - 1/r^2)/(2 r), is the run's own (u, v) error and is reported beside it"""
    j = int(np.argmin(abs(Z['v'] - 0.3)))
    gen = B.generators(Z, F, j, 24)
    worst, exact = 0.0, 0.0
    for r in (3.0, 1.5, 1.0, 0.8):
        xi, U, X, th, leaf = B.sphere(Z, F, j, r, gen=gen, want_leaf=True)
        if U is None:
            continue
        worst = max(worst, np.abs(X - xi).max(), np.abs(U - U.mean()).max(), np.abs(th - leaf).max())
        exact = max(exact, np.abs(th - 3 * (1 - 1 / r ** 2) / (2 * r)).max())
    return worst, exact


def bondi_zeros(Z, F, j, rs, MB=32, leaf_only=False):
    gen = B.generators(Z, F, j, MB)
    TH, rr = [], []
    for r in rs:
        xi, U, X, th, leaf = B.sphere(Z, F, j, r, gen=gen, want_leaf=True)
        if U is None:
            continue
        if leaf_only:            # the control: the leaf expansion 3 R_v/R at the section's points, tilt ignored
            th = leaf
        TH.append(th); rr.append(r)
    return gen[0], np.array(rr), np.array(TH)


def outer_zero(xi, rr, TH):
    rz = np.full(TH.shape[1], np.nan)
    for b in range(TH.shape[1]):
        c = TH[:, b]; idx = np.nonzero(np.sign(c[1:]) != np.sign(c[:-1]))[0]
        if len(idx):
            i = idx[-1]; rz[b] = rr[i] + (rr[i + 1] - rr[i]) * c[i] / (c[i] - c[i + 1])
    return rz


def g5_outer(vv, key='L100_lam1_28x16_d0_y1.6'):
    st = json.load(open(G5))[key]['steps']
    s = min(st, key=lambda s: abs(s[0] - vv))
    return s[0], np.array([max(c) if c else np.nan for c in s[7]])


def s4(Z, F, leaf_only=False, show=True):
    rs = np.linspace(0.6, 1.6, 101)
    worst = 0.0
    for vv in (1.0, 1.2, 1.3, 1.35, 1.375):
        j = int(np.argmin(abs(Z['v'] - vv)))
        xi, rr, TH = bondi_zeros(Z, F, j, rs, leaf_only=leaf_only)
        rz = outer_zero(xi, rr, TH)
        if not np.isfinite(rz).all():
            if show:
                print('      v = %.3f: outer zero not found in every column' % Z['v'][j])
            worst = np.inf
            continue
        rzg = B.bary_matrix(xi, XG) @ rz
        vg, og = g5_outer(Z['v'][j])
        d = np.abs(rzg - og)
        worst = max(worst, np.nanmax(d))
        if show:
            print('      v = %.3f: max |r_AH(double null) - r_AH(growth5)| = %.3f (at x = %.2f); r_AH ranges %.3f-%.3f '
                  'and %.3f-%.3f' % (Z['v'][j], np.nanmax(d), XG[np.nanargmax(d)], rzg.min(), rzg.max(),
                                     np.nanmin(og), np.nanmax(og)), flush=True)
    return worst


def s5(Z, F, r_core, vlist, r_lo):
    rs = np.r_[np.linspace(r_lo, 1.0, 41), np.linspace(1.025, 1.6, 24)]
    rows = []
    for vv in vlist:
        j = int(np.argmin(abs(Z['v'] - vv)))
        xi, rr, TH = bondi_zeros(Z, F, j, rs)
        if len(rr) == 0:
            rows.append((Z['v'][j], None)); continue
        cnt = []
        inner = []
        for b in range(TH.shape[1]):
            c = TH[:, b]; idx = np.nonzero(np.sign(c[1:]) != np.sign(c[:-1]))[0]
            cnt.append(len(idx))
            if len(idx) > 1:
                inner.append(rr[idx[0]])
        core = None
        if abs(rr[0] - r_core) < 1e-9 or rr[0] <= r_core:
            ic = int(np.argmin(abs(rr - r_core)))
            core = float(TH[ic].max())
        rows.append((Z['v'][j], dict(r_min=float(rr.min()), counts=cnt, inner=inner, core_max=core,
                                     th_min_r=float(TH[0].max()))))
    return rows


def main():
    rundir = sys.argv[1]
    names = sys.argv[2:]
    ok = True
    for name in names:
        Z = B.load(os.path.join(rundir, name + '.npz'))
        lam = float(Z['lam']) if 'lam' in Z else 1.0
        print('== %s: lambda %.4g, M %d, %d x %d, cut %.2f' % (name, lam, len(Z['x']), len(Z['u']) - 1,
                                                                 round(4.5 / (Z['v'][1] - Z['v'][0])),
                                                                 float(Z['rcut']) if 'rcut' in Z else -1), flush=True)
        good, n_far, n_near, k, nsel = s1(Z)
        ctl = s1(Z, umin=-1.02)[0]
        print('  S1 R_v < 0 at u > -1, >= %d rows from the cut, v <= 2: violations %d far, %d near the cut, of %d '
              'cells -> %s; control (u > -1.02) %s' % (k, n_far, n_near, nsel, 'PASS' if good else 'FAIL',
                                                       'passed (bad)' if ctl else 'fails (good)'), flush=True)
        ok &= good and not ctl
        late = s1(Z, vmax=2.0, vmin=VMAX)
        print('     beyond, on (%.2f, 2]: violations %d far, %d near the cut' % (VMAX, late[1], late[2]), flush=True)
        good, extra, fv, k = s2(Z)
        ctl = s2(Z, control=True)
        print('  S2 further zeros of R_v along ingoing cones: %d, first at v = %s, all at u > -1 within %d rows of the '
              'cut: %s; control (first zero near the cut) %s' % (extra, fv, k, 'PASS' if good else 'FAIL',
                                                                 'passed (bad)' if ctl else 'fails (good)'), flush=True)
        ok &= good and not ctl
        late = s2(Z, vmax=2.0, vmin=VMAX)
        print('     beyond, on (%.2f, 2]: %d further zeros, all near the cut: %s' % (VMAX, late[1], late[0]), flush=True)
        F = B.derivatives(Z)
        w, ex = s3(Z, F)
        print('  S3 Bondi spheres on the seed (v = 0.3): max |X - xi|, |U - mean U|, |theta - 3 R_v/R| = %.1e -> %s '
              '(against exact Tangherlini: %.1e, the run\'s own error)' % (w, 'PASS' if w < 1e-9 else 'FAIL', ex),
              flush=True)
        ok &= w < 1e-9
        if abs(lam - 1) < 1e-6:
            w = s4(Z, F)
            wc = s4(Z, F, leaf_only=True, show=False)
            good = w <= 0.1 and wc > 0.1
            print('  S4 outer zero against growth5: max %.3f -> %s; control (leaf expansion, tilt ignored) max %.3f '
                  '%s' % (w, 'PASS' if good else 'FAIL', wc, 'fails (good)' if wc > 0.1 else 'passed (bad)'),
                  flush=True)
            ok &= good
            rows = s5(Z, F, 0.5397, (1.30, 1.35, 1.40, 1.425, 1.45, 1.475, 1.50, 1.525, 1.55), 0.42)
        else:
            rows = s5(Z, F, 0.3035, (1.40, 1.45, 1.50, 1.525, 1.55, 1.575, 1.60, 1.625), 0.25)
        print('  S5 (reported) per Bondi column, zeros of theta on [r_min, 1.6]:', flush=True)
        for vj, d in rows:
            if d is None:
                print('     v = %.3f: no usable sphere' % vj); continue
            c = d['counts']
            print('     v = %.3f r_min %.3f: columns with 0 / 1 / 2+ zeros: %d / %d / %d; inner zeros at r = %s; '
                  'max theta on r_min %.3f; on r_core %s' % (vj, d['r_min'], c.count(0), c.count(1),
                                                            sum(q > 1 for q in c),
                                                            np.round(sorted(d['inner'])[:4], 3).tolist(),
                                                            d['th_min_r'], 'n/a' if d['core_max'] is None else
                                                            '%.3f' % d['core_max']), flush=True)
    print('secondzero5:', 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
