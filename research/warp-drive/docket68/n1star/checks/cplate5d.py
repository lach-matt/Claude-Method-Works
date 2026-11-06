#!/usr/bin/env python3
"""cplate5d.py -- CERTIFY-10L5-RESULT.md round 3 (task 3): the constraint-preserving scheme at 1600 x 720 in angle,
M = 32 against M = 40, where cplate5c.py found the metric converging in the null step and the unimposed constraint not.
Labels: computed (floating point).

cplate5c.py C2: at areal radius 0.9-1.2 and v >= 1.9 the Ric_xx monitor no longer falls from 800 to 1600 rows at
M = 32, while P converges.  Either the angular resolution (or the scheme's axis defect, cpsolve5.py P3, which grows
like M^2 times the truncation error) is then the limiting error, or the limit is not a vacuum solution.  Here M = 40 on
the same null grid separates the first from the rest.  Compared on the cells both runs keep, at least Nu/40 rows from
the cut, per v-band and areal-radius class (radius from the M = 32 run):

  D1 the Ric_xx monitor (cpsolve5's cx), max over all nodes and max over the nodes with |x| <= 0.9, at M = 32 and 40.
  D2 max |P_32 - P_40|, the M = 40 field interpolated to the M = 32 nodes by its Chebyshev series.
  Verdict per band at 0.9 <= r_A < 1.2: "angle-limited" if the interior monitor falls at least twofold from M = 32 to
  40, "not angle-limited" if it changes by less than 20 %, "unclear" otherwise.
  Control: D2 with the record's free run at amplitude 7/8 (D445, M = 32, 800 x 360, every second row) in place of the
  M = 40 run, a different solution, must exceed the M = 32-40 difference on every band below v = 1.8.

  python3 checks/cplate5d.py CP1600_M32 CP1600_M40 AMP875
"""
import sys, warnings
import numpy as np
warnings.filterwarnings('ignore')


def print(*a, **k):
    """print, every line wrapped at 121 characters (the record's line limit)"""
    import builtins, textwrap
    s = (k.pop('sep', ' ')).join(str(q) for q in a)
    lines = []
    for ln in s.split('\n'):
        if len(ln) <= 121:
            lines.append(ln)
        else:
            ind = len(ln) - len(ln.lstrip()) + 4
            lines.extend(textwrap.wrap(ln, 121, subsequent_indent=' ' * ind, break_on_hyphens=False))
    builtins.print('\n'.join(lines), **k)


BANDS = [(0.5, 1.0), (1.0, 1.5), (1.5, 1.65), (1.65, 1.8), (1.8, 1.9), (1.9, 2.0), (2.0, 2.25)]
CLASSES = [('r_A >= 1.2', 1.2, 99.0), ('1.0 <= r_A < 1.2', 1.0, 1.2), ('0.9 <= r_A < 1.0', 0.9, 1.0)]


def load(path, step=1, nv=None):
    Z = np.load(path)
    x = Z['x']; M = len(x)
    sl = (slice(None, None, step), slice(None, (nv - 1) * step + 1 if nv else None, step))
    mask = Z['mask'][sl]
    m, n, R = Z['m'][sl], Z['n'][sl], Z['R'][sl]
    P = (2 * (1 + x) * m - (1 - x) * n) / 3
    rA = (np.nansum(R ** 3 * (np.pi / M * np.sqrt(1 - x ** 2)), -1) / 2) ** (1 / 3)
    ok = ~mask
    Nu = mask.shape[0]
    last = np.array([np.nonzero(ok[:, j])[0].max() if ok[:, j].any() else -1 for j in range(mask.shape[1])])
    far = np.zeros_like(ok)
    for j in range(mask.shape[1]):
        far[:max(last[j] - (Nu - 1) // 40 + 1, 0), j] = True
    out = dict(x=x, P=P, rA=rA, sel=ok & far, v=Z['v'][sl[1]], u=Z['u'][sl[0]])
    if 'cx' in Z.files:
        cx = np.abs(Z['cx'][sl])
        out['cx_all'] = np.nanmax(cx, -1)
        out['cx_in'] = np.nanmax(np.where((np.abs(x) <= 0.9)[None, None, :], cx, np.nan), -1)
    return out


def to_nodes(F, xs, xt):
    """values F[..., j] at Chebyshev-Gauss nodes xs -> their Chebyshev series evaluated at xt"""
    T = np.cos(np.outer(np.arange(len(xs)), np.arccos(xs)))
    c = np.linalg.solve(T.T, np.moveaxis(F, -1, 0).reshape(len(xs), -1))
    Tt = np.cos(np.outer(np.arange(len(xs)), np.arccos(xt)))
    return np.moveaxis((Tt.T @ c).reshape((len(xt),) + F.shape[:-1]), 0, -1)


def bmax(A, sel, v, band, rA, cls):
    s = sel & ((v >= band[0]) & (v < band[1]))[None, :] & (rA >= cls[1]) & (rA < cls[2])
    a = A[s]; a = a[np.isfinite(a)]
    return float(a.max()) if a.size else np.nan


def main():
    a32, a40 = load(sys.argv[1]), load(sys.argv[2])
    assert np.allclose(a32['u'], a40['u']) and np.allclose(a32['v'], a40['v'])
    nv = len(a32['v'])
    am = load(sys.argv[3], step=1, nv=(nv - 1) // 2 + 1)
    v, rA = a32['v'], a32['rA']
    sel = a32['sel'] & a40['sel']
    P40 = to_nodes(a40['P'], a40['x'], a32['x'])
    dP = np.nanmax(np.abs(a32['P'] - P40), -1)
    # control: the amplitude-7/8 free run lives on the 800-row grid; compare on every second row and column
    selc = sel[::2, ::2] & am['sel']
    dPc = np.nanmax(np.abs(a32['P'][::2, ::2] - am['P']), -1)
    ok, ctl_all = True, True
    verdict = []
    for cls in CLASSES:
        print('%s:' % cls[0], flush=True)
        for b in BANDS:
            r = [bmax(a[k], sel, v, b, rA, cls) for a in (a32, a40) for k in ('cx_all', 'cx_in')]
            d = bmax(dP, sel, v, b, rA, cls)
            dc = bmax(dPc, selc, v[::2], b, rA[::2, ::2], cls)
            print('   v in [%.2f, %.2f): D1 Ric_xx M32 %.2e (|x| <= 0.9: %.2e), M40 %.2e (%.2e), interior ratio %.2f; '
                  'D2 |P_32 - P_40| %.2e; control |P_32 - P_7/8| %.2e' % (*b, r[0], r[1], r[2], r[3],
                                                                          r[1] / r[3] if r[3] > 0 else np.nan, d, dc),
                  flush=True)
            if b[1] <= 1.8 and cls[1] >= 1.0 and not dc > d:
                ctl_all = False
            if cls[1] in (1.0, 0.9):
                q = r[1] / r[3] if r[3] > 0 else np.nan
                w = 'angle-limited' if q >= 2 else ('not angle-limited' if abs(q - 1) < 0.2 else 'unclear')
                verdict.append((cls[0], b, w, q))
    print('verdict (interior Ric_xx monitor, M = 32 against 40 at 1600 x 720):')
    for cl, b, w, q in verdict:
        print('   %s, [%.2f, %.2f): %s (M32/M40 = %.2f)' % (cl, *b, w, q))
    print('control (a different solution differs more than M = 32 from 40 on every band below v = 1.8):',
          'fails (good)' if ctl_all else 'passed (bad)')
    ok &= ctl_all
    print('cplate5d:', 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
