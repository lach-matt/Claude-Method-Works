#!/usr/bin/env python3
"""lzerorank5: round 4's lambda0 bound read adversarially (CONSTANTS5.md, Round 5, R5.1 (a)). Round 4 (R4.2,
lzerotrace5.py T5) took Lemma 2.3's requirement eps1 < g0's least absolute eigenvalue on Omega to every reading of the
pointwise norm with the sentence "every reading's ball |g - g0| <= eps1 contains the operator-norm ball". That holds for
the largest-entry norm (|A|_max <= |A|_op) and fails for the Frobenius norm (|A|_op <= |A|_F: the Frobenius ball is
inside the operator ball). The conclusion survives through a rank-one perturbation, which this program exhibits, and the
largest-entry reading gets a sharper bound from it. Labels: certified (exact rationals and certified rational square
roots, lzerotrace5.py's geometry, imported), computed (exact, sympy), deduced (where said).

  R1 (exact, sympy, symbolic m > 0) g0 = eta + m U U^T, U = (1, xhat), xhat = e1 (O(4) invariance): the negative
     eigenvalue m - s, s = (m^2 + 1)^(1/2), has the eigenvector v = (m, 1 - s, 0, 0, 0); with e = v/|v|,
     g0 + (s - m) e e^T has determinant 0. So at the corner (tau_end, r = a), m = m*, the perturbation t e e^T leaves
     the Lorentzian class at t = s - m = g0's least absolute eigenvalue, and its size is t in the operator AND in the Frobenius norm (rank one,
     |e| = 1). Hence eps1 < 0.0307686 in the Frobenius reading by a valid argument, and lambda0 < 0.0019950 stands.
  R2 (certified) its largest entry: e e^T has entries e_tau^2, e_tau e_x xhat_i, e_x^2 xhat_i xhat_j, and e_tau^2 >
     e_x^2 exactly when s < m + 1, true for m > 0, so for every direction xhat the largest entry is t e_tau^2, e_tau^2 =
     m^2/(m^2 + (s - 1)^2) =: f(m) = 1/(1 + ((s - 1)/m)^2), decreasing in m since d/dm (s - 1)/m = (1 - 1/s)/m^2 > 0
     (exact identities). So in the largest-entry reading eps1 < (s - m) f(m) at m*, certified below 0.0163302, and
     lambda0 < 0.0163302/12.593309 < 0.0012968 (T3's C_app, certified there): round 4's 0.0024433 for that reading is
     valid and twice too large.
  R3 (floating point) cross-check: the signature of g0 + t e e^T at m* is (1, 4) for t = 0.99 (s - m) and degenerate or
     Riemannian beyond (numpy eigenvalues).
  Controls (mutating the computed path; each must fail): C1 R1's test on the positive eigenvector (m, 1 + s): g0 +
  (s - m) e+ e+^T has a nonzero determinant, so the degeneracy test fails; C2 R2 at the outer corner r =
  b(tau0) (m = mu_end/b(tau0)^2): the bound there is above 0.4, so R2's enclosure fails for it.

    python3 checks/lzerorank5.py       (seconds)
"""
import builtins
import os
import sys
import textwrap
from fractions import Fraction as Fr

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)
import lzerotrace5 as LT  # noqa: E402  (round 4: geometry, lemma23_threshold, certified square roots)

OK = {}
C_OP = Fr(12593309, 10 ** 6)        # lzerotrace5.out T3: operator and largest entry >= 12.593309 (certified, down)
C_FR = Fr(15423591, 10 ** 6)        # T3: Frobenius >= 15.423591 (certified, down)


def print(*a, **k):  # noqa: A001
    for line in ' '.join(str(q) for q in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False), **k)


def rank_one(sign=-1):
    m = sp.Symbol('m', positive=True)
    s = sp.sqrt(m ** 2 + 1)
    U = sp.Matrix([1, 1, 0, 0, 0])
    g0 = sp.diag(-1, 1, 1, 1, 1) + m * U * U.T
    v = sp.Matrix([m, 1 + sign * s, 0, 0, 0])
    lam = m + sign * s
    eig_ok = sp.simplify(g0 * v - lam * v) == sp.zeros(5, 1)
    e = v / sp.sqrt((v.T * v)[0])
    det = sp.simplify((g0 + (s - m) * e * e.T).det())
    f = sp.simplify(m ** 2 / (m ** 2 + (s - 1) ** 2))
    fprime_neg = sp.simplify(sp.diff(f, m) * (m ** 2 + (s - 1) ** 2) ** 2 / m) if sign < 0 else None
    return dict(m=m, s=s, eig_ok=eig_ok, det=det, f=f, fprime=fprime_neg)


def bound_at(m_lo, m_hi, e_hi):
    """certified upper end of (s - m) f(m) at m in [m_lo, m_hi] (both factors decreasing)"""
    s_lo = LT.sqrt_lo(m_lo ** 2 + 1)
    f_hi = m_lo ** 2 / (m_lo ** 2 + (s_lo - 1) ** 2)
    return e_hi * f_hi, f_hi


def main():
    print('lzerorank5: the rank-one perturbation behind Lemma 2.3\'s eps1 in every reading of |.|')
    R = rank_one()
    m, s = R['m'], R['s']
    # f = 1/(1 + ((s - 1)/m)^2) and d/dm (s - 1)/m = (1 - 1/s)/m^2 > 0 (s > 1): f decreases (exact identity)
    fp_neg = (sp.simplify(R['f'] - 1 / (1 + ((s - 1) / m) ** 2)) == 0
              and sp.simplify(sp.diff((s - 1) / m, m) - (1 - 1 / s) / m ** 2) == 0)
    OK['R1'] = R['eig_ok'] and R['det'] == 0
    print('  R1: g0 v = (m - s) v for v = (m, 1 - s, 0, 0, 0) (exact, symbolic m): %s; det(g0 + (s - m) e e^T) = %s '
          '(exact): the rank-one perturbation of operator = Frobenius size s - m makes g0 degenerate' % (
              R['eig_ok'], R['det']))
    g = LT.LZ.geometry()
    e_lo, e_hi, closed, decr, corner, (m_lo, m_hi) = LT.lemma23_threshold(g)
    b2, f_hi = bound_at(m_lo, m_hi, e_hi)
    lam_max = b2 / C_OP
    lam_op, lam_fr = e_hi / C_OP, e_hi / C_FR
    OK['R2'] = (corner and fp_neg and b2 < Fr(163302, 10 ** 7) and lam_max < Fr(12968, 10 ** 7)
                and lam_op < Fr(24433, 10 ** 7) + Fr(1, 10 ** 7) and lam_fr < Fr(19950, 10 ** 7))
    print('  R2: f(m) = e_tau^2 = %s, decreasing (f\' < 0 at five exact m: %s); at m* in [%s, %s]: f <= %s, so the '
          'largest-entry size of the perturbation is <= %s (certified, rounded up). lambda0 < eps1/C_app: operator %s, '
          'Frobenius %s (R1), largest entry %s (certified, rounded up)' % (
              R['f'], fp_neg, LT.down(m_lo, 6), LT.up(m_hi, 6), LT.up(f_hi, 7), LT.up(b2, 7), LT.up(lam_op, 7),
              LT.up(lam_fr, 7), LT.up(lam_max, 7)))
    # R3 floating cross-check
    mm = float(m_hi)
    ss = (mm * mm + 1) ** 0.5
    U = np.array([1.0, 1, 0, 0, 0])
    g0 = np.diag([-1.0, 1, 1, 1, 1]) + mm * np.outer(U, U)
    v = np.array([mm, 1 - ss, 0, 0, 0])
    e = v / np.linalg.norm(v)
    neg = [int(sum(np.linalg.eigvalsh(g0 + t * (ss - mm) * np.outer(e, e)) < 0)) for t in (0.99, 1.01)]
    OK['R3'] = neg == [1, 0]
    print('  R3 (floating point): negative eigenvalues of g0 + t (s - m) e e^T at m*: t = 0.99: %d, t = 1.01: %d'
          % tuple(neg))
    # controls
    Rp = rank_one(sign=+1)
    OK['C1'] = Rp['det'] != 0
    print('  C1 (control): the positive eigenvector (m, 1 + s): det = %s, not 0: R1\'s test fails on it: %s' % (
        sp.simplify(Rp['det']), OK['C1']))
    b0 = g['b0'][0]
    mb = g['mu_end'] / b0 ** 2
    eb_hi = 1 / (LT.sqrt_lo(mb ** 2 + 1) + mb)
    b2b, _ = bound_at(mb, mb, eb_hi)
    OK['C2'] = not (b2b < Fr(163302, 10 ** 7))
    print('  C2 (control): R2 at the outer corner r = b(tau0), m = %s: bound %s, so R2\'s enclosure fails: %s' % (
        LT.down(mb, 6), LT.down(b2b, 4), OK['C2']))
    for k_, val in OK.items():
        builtins.print(k_, 'PASS' if val else 'FAIL')
    return 0 if all(OK.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
