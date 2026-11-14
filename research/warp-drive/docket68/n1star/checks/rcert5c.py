#!/usr/bin/env python3
"""rcert5c.py -- CERTIFY-10L5-RESULT.md round 3, the verifier of round 2's M5: rcert5.py's approximant pinned.  Labels:
certified (Arb ball arithmetic, python-flint) for the enclosures; computed for the fit that defines the coefficients.

rcert5.py fits its approximant afresh on every run (a floating-point least-squares fit), and the verifier of round 2
found the fit not bit-reproducible: K2 moved on a rerun, and a 1e-9 change to one coefficient moved the ln maximum by
2.3 %.  A certificate is a statement about explicit coefficients, so they are saved here, with the md5 of each tensor's
bytes, and K1 is recomputed from the saved file.

  P1 the fit's coefficient tensors C3 (fields R, m, n, W, s) written to data/rcert5_C3.npz, read back, and the md5 of
     every tensor's float64 bytes printed (the identity of the approximant).
  P2 (certified) K1 from the saved tensors: the eight scaled frame components at the 16,128 centres, each maximum
     printed with its ball's upper end to 6 digits.  ll's upper end must exceed 2.41e-3 and stay below 2.42e-3 (so
     "<= 2.41e-3" is false and "<= 2.42e-3" true).
  Control: the same with C3['m'][0, 0, 0] changed by 1e-9: the maxima must move (the certificate belongs to the saved
     coefficients and to no others); the relative shift of each is printed.

  python3 checks/rcert5c.py                  (default, read only: load data/rcert5_C3.npz, check its five md5s
                                             against PINNED below, then P2 and the control on those tensors)
  python3 checks/rcert5c.py --write RUNDIR   (refit from RUNDIR's l1_M16_800.npz and OVERWRITE the npz; P1 then
                                             prints the new md5s, which will not match PINNED: the fit is not
                                             bit-reproducible.  Never run on the committed file.)

[Round 4, the verifier of round 3, M-1: the round-3 version wrote the npz on every run, so its P2 certified a fresh,
unsaved fit rather than the committed file (md5 698569f6faaab4420fe2e67abc860561).  The default is now read only.]
"""
import os, sys, time, hashlib
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rcert5 as R5                                                              # noqa: E402
from flint import arb                                                             # noqa: E402
print = R5.print
FRL = ['ll', 'ln', 'nn', 'lx', 'nx', 'xx', '11', '22']
OUT = os.path.join(os.path.dirname(HERE), 'data', 'rcert5_C3.npz')
PINNED = {'R': 'be89d629886bf9c61c098a76c22ad7ae', 'm': '99434c1b9859c9fa03653b65148f8bdc',
          'n': '7a0ab510aec85e3329018558d5f76f91', 'W': '3427e2bfe9009ffff09650606d2837b3',
          's': '1faa82dee965590cfac4cdf14e460214'}
FILE_MD5 = '698569f6faaab4420fe2e67abc860561'


def geometry(M):
    """the coordinate data rcert5.prepare returns, from rcert5.ARGS alone (no run, no fit)"""
    a = R5.ARGS
    xa, xb = np.arcsinh((a[0] + 1) / R5.RS.A_GRID), np.arcsinh((a[1] + 1) / R5.RS.A_GRID)
    hv = (a[3] - a[2]) / 2
    return dict(hxi=(xb - xa) / 2, a=R5.RS.A_GRID, psi=1 / hv, xa=xa, M=M, hv=hv)


def upper(b):
    return float(b.mid() + b.rad())


def main():
    t0 = time.time()
    frame, names = R5.frame_code()
    R5.certify_points.frame, R5.certify_points.names = frame, names
    rel = os.path.relpath(OUT, os.path.dirname(os.path.dirname(HERE)))
    fmd5 = lambda: hashlib.md5(open(OUT, 'rb').read()).hexdigest()
    if len(sys.argv) > 2 and sys.argv[1] == '--write':
        Z = R5.B.load(os.path.join(sys.argv[2], 'l1_M16_800.npz'))
        C3, g, err = R5.prepare(Z)
        np.savez_compressed(OUT, **{k: np.ascontiguousarray(C3[k], dtype=np.float64) for k in R5.RS.NAMES})
        L = np.load(OUT)
        C3s = {k: np.array(L[k]) for k in R5.RS.NAMES}
        same = all(np.array_equal(C3s[k], C3[k]) for k in R5.RS.NAMES)
        print('P1 (--write) coefficient tensors refitted, written to %s and read back identical: %s (%.0f s)' % (
            rel, same, time.time() - t0))
    else:
        before = fmd5()
        L = np.load(OUT)
        C3s = {k: np.array(L[k]) for k in R5.RS.NAMES}
        g = geometry(C3s['R'].shape[2])
        same = all(hashlib.md5(C3s[k].tobytes()).hexdigest() == PINNED[k] for k in R5.RS.NAMES)
        print('P1 (read only) %s loaded, file md5 %s (%s the committed %s); its five tensors\' md5s equal the pinned '
              'ones: %s' % (rel, before, 'equal to' if before == FILE_MD5 else 'DIFFERENT from', FILE_MD5, same))
    for k in R5.RS.NAMES:
        md5 = hashlib.md5(C3s[k].tobytes()).hexdigest()
        print('   %s: shape %s, md5 of the float64 bytes %s' % (k, C3s[k].shape, md5))
    best, npts = R5.certify_points(C3s, g, 24, 24, 8)
    ups = [upper(b) for b in best]
    print('P2 K1 from the saved tensors, %d points: ' % npts
          + ', '.join('%s <= %.6g' % (k, u) for k, u in zip(FRL, ups)))
    good = same and 2.41e-3 < ups[0] < 2.42e-3
    print('   ll: upper end %.7g -> "<= 2.41e-3" false, "<= 2.42e-3" true:' % ups[0], 'PASS' if good else 'FAIL')
    C3p = dict(C3s); C3p['m'] = C3s['m'].copy(); C3p['m'][0, 0, 0] += 1e-9
    bp, _ = R5.certify_points(C3p, g, 24, 24, 8)
    upp = [upper(b) for b in bp]
    moved = [abs(a - b) / b for a, b in zip(upp, ups)]
    ctl = max(moved) > 0
    print('   control (C3[m][0, 0, 0] + 1e-9): relative shifts of the maxima ' +
          ', '.join('%s %.2g' % (k, m_) for k, m_ in zip(FRL, moved)), '->', 'they move (good)' if ctl else
          'unchanged (bad)')
    ok = good and ctl
    if not (len(sys.argv) > 2 and sys.argv[1] == '--write'):
        after = fmd5()
        unchanged = after == before == FILE_MD5
        print('   the npz after the run: md5 %s, unchanged and the committed one: %s' % (after, unchanged))
        ok &= unchanged
    print('rcert5c (%.0f s):' % (time.time() - t0), 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
