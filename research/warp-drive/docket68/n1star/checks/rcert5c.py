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

  python3 checks/rcert5c.py RUNDIR          (RUNDIR holding l1_M16_800.npz, the run resid5.py fits)
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


def upper(b):
    return float(b.mid() + b.rad())


def main():
    t0 = time.time()
    frame, names = R5.frame_code()
    R5.certify_points.frame, R5.certify_points.names = frame, names
    Z = R5.B.load(os.path.join(sys.argv[1], 'l1_M16_800.npz'))
    C3, g, err = R5.prepare(Z)
    np.savez_compressed(OUT, **{k: np.ascontiguousarray(C3[k], dtype=np.float64) for k in R5.RS.NAMES})
    L = np.load(OUT)
    C3s = {k: np.array(L[k]) for k in R5.RS.NAMES}
    same = all(np.array_equal(C3s[k], C3[k]) for k in R5.RS.NAMES)
    print('P1 coefficient tensors written to %s and read back identical: %s (%.0f s)' % (
        os.path.relpath(OUT, os.path.dirname(os.path.dirname(HERE))), same, time.time() - t0))
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
    print('rcert5c (%.0f s):' % (time.time() - t0), 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
