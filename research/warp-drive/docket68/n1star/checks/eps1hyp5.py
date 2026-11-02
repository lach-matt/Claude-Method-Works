#!/usr/bin/env python3
"""eps1hyp5: Lemma 1.1 (e)'s eps1 at the paper's point, measured on the hypersurfaces themselves (CONSTANTS5.md, Round
2, item (i); a correction of round 1's value, which stays valid but is about 1140 times too small).

Lemma 1.1 (e) asks, for every Lorentzian g with |g - g0| <= eps1 on Omega (|.| the Euclidean operator norm of the
Cartesian matrix, as in lzeroconst5.py Z2): Sigma_tau, {r = a} and the outer boundary {v + tau - tau_end = V + 1} stay
spacelike, J^-(p; g) cap {tau >= tau0} lies in Omega, and L0 stays transverse to Sigma_tau. A hypersurface {f = c} is
spacelike for g iff g restricted to ker df is positive definite; if lambda_min(g0|ker df) >= m (Euclidean-orthonormal
basis of ker df) and |g - g0| <= eps < m, then g|ker df >= m - eps > 0. Round 1 went through |g^-1 - g0^-1| <= n^2 eps
(n = sup |g0^-1| = 33.47), which costs n^2 = 1120. Labels: computed (exact rationals, certified roots from
lzeroconst5.py's geometry); deduced (the reduction to the hyperplanes, and the causal containment below).

  H1 (exact) g0 = eta + (mu/r^2) dv dv on the three hyperplanes, in Euclidean-orthonormal bases:
       ker dtau (all of Omega):          eigenvalues 1 (x3), 1 + mu/r^2                 -> lambda_min = 1;
       ker dr (on r = a):                eigenvalues 1 (x3), mu/a^2 - 1 >= mu0/a^2 - 1   -> lambda_min = 1 at P*;
       ker d(v + tau) (outer boundary):  eigenvalues 1 (x3), (3 + mu/r^2)/5            -> lambda_min >= 3/5.
     Checked symbolically (sympy: the restricted Gram matrices for generic mu, r and unit xhat) and exactly at P*.
  H2 (deduced) so every eps1 < 3/5 serves Lemma 1.1 (e): the three hypersurfaces stay spacelike; along g0 + t(g - g0),
     t in [0, 1], the covectors dtau, dr (at r = a) and d(v + tau) (outer) stay timelike, so the signs of g^-1(dr,
     dtau) and g^-1(d(v + tau), dtau) (two timelike covectors are never orthogonal) and the time orientation are those
     of g0; past causal curves then cannot leave Omega through {r = a}, the outer boundary or Sigma_tau_end, which is
     the containment; L0(tau) = 1 does not involve g.
  H3 (certified) sharpness: at the outer boundary on Sigma_tau0 (r = b(tau0), mu = mu_end = 227/192) the perturbation
     delta g = -lambda_min n (x) n, n the unit vector of ker d(v + tau) along (1, -2 xhat)/sqrt5, has operator norm
     lambda_min = (3 + mu_end/b(tau0)^2)/5 in [0.601313, 0.601314], keeps det < 0 (Lorentzian), and makes d(v + tau)
     null: so no eps1 above 0.60132 serves. eps1* lies in [3/5, 0.60132].
  Controls (must fail, and do): C1 the claim "eps1 = 0.61 serves" is refuted by H3's perturbation (exact rational
  check that d(v + tau) is null for g); C2 a perturbation of norm 0.59 of the same shape keeps the boundary spacelike,
  and 0.62 does not (floating point, the sign of g^-1(d(v + tau), d(v + tau))); C3 the hyperplane test applied to
  ker dr at r = 1.5 (where mu/r^2 < 1, dr spacelike: {r = 1.5} is timelike for g0) returns a negative eigenvalue, so
  the test does detect a non-spacelike hypersurface.

    python3 checks/eps1hyp5.py
"""
import os
import sys
import textwrap
from fractions import Fraction as Fr

import numpy as np
import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lzeroconst5 as LZ  # noqa: E402  (round 1's certified geometry at P*, imported, not copied)

EPS1_R1 = 5.2617e-4                                  # READ: CONSTANTS5.md 1.4 (round 1)


def say(s):
    for line in s.split('\n'):
        print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False, break_on_hyphens=False))


def restricted_gram(xi, mu, r, xhat):
    """g0 on ker xi in a Euclidean-orthonormal basis (sympy, exact); xi a covector on (tau, x)"""
    g0 = sp.diag(-1, 1, 1, 1, 1) + (mu / r ** 2) * sp.Matrix([1, *xhat]) * sp.Matrix([1, *xhat]).T
    K = sp.Matrix([xi]).nullspace()
    B = sp.Matrix.hstack(*K)
    Q, _ = B.QRdecomposition()
    return sp.simplify(Q.T * g0 * Q)


def main():
    ok = {}
    mu, r = sp.symbols('mu r', positive=True)
    xhat = (1, 0, 0, 0)          # O(4) acts transitively on the directions and fixes eta, dtau, dr, dv: one suffices
    dtau = [1, 0, 0, 0, 0]
    dr = [0, *xhat]
    dvt = [2, *xhat]
    lx = sp.Symbol('x')
    want = {'dtau': [1, 1, 1, 1 + mu / r ** 2], 'dr': [1, 1, 1, mu / r ** 2 - 1],
            'd(v+tau)': [1, 1, 1, (3 + mu / r ** 2) / 5]}
    ev = {}
    same = True
    for name, xi in (('dtau', dtau), ('dr', dr), ('d(v+tau)', dvt)):
        G = restricted_gram(xi, mu, r, xhat)
        ev[name] = list(G.eigenvals(multiple=True))
        same &= sp.simplify(G.charpoly(lx).as_expr() - sp.prod([lx - w for w in want[name]])) == 0
    g = LZ.geometry()
    a_hi = g['a'][1]
    m_dr = LZ.MU0 / a_hi ** 2 - 1                      # mu >= mu0 on r = a
    ok['H1'] = same and m_dr > 1
    say('  H1: eigenvalues of g0 on the hyperplanes (sympy, generic mu, r): %s; equal to the closed forms: %s; on r = a '
        'at P*: mu/a^2 - 1 >= %.4f > 1, so lambda_min = 1, 1 and >= 3/5' % (
            {k: [str(e) for e in v] for k, v in ev.items()}, same, float(m_dr)))

    # H3: sharpness at the outer boundary on Sigma_tau0
    b_lo, b_hi = g['b0']
    mu_e = g['mu_end']
    lam_lo = (3 + mu_e / b_hi ** 2) / 5
    lam_hi = (3 + mu_e / b_lo ** 2) / 5
    lam = lam_hi                                        # a rational at least lambda_min, used below exactly
    # exact check with r replaced by the rational b_lo (the boundary radius within 1e-25): build g at xhat = e1
    rr = b_lo
    g0 = sp.diag(-1, 1, 1, 1, 1) + (sp.Rational(mu_e.numerator, mu_e.denominator) / sp.Rational(rr.numerator,
                                                                                             rr.denominator) ** 2) \
        * sp.Matrix([1, 1, 0, 0, 0]) * sp.Matrix([1, 1, 0, 0, 0]).T
    n = sp.Matrix([1, -2, 0, 0, 0]) / sp.sqrt(5)
    lam_exact = (3 + sp.Rational(mu_e.numerator, mu_e.denominator) / sp.Rational(rr.numerator, rr.denominator) ** 2) / 5
    gp = g0 - lam_exact * n * n.T
    # the boundary is null for g iff g restricted to ker xi is degenerate (determinant 0)
    K = sp.Matrix.hstack(*sp.Matrix([[2, 1, 0, 0, 0]]).nullspace())
    Q, _ = K.QRdecomposition()
    det_restr = sp.simplify((Q.T * gp * Q).det())
    det_full = sp.simplify(gp.det())
    ok['H3'] = det_restr == 0 and det_full < 0 and lam_lo > Fr(6013, 10000) and lam_hi < Fr(60132, 100000)
    say('  H3: lambda_min on the outer boundary at tau0 = (3 + mu_end/b(tau0)^2)/5 in [%.7f, %.7f]; the perturbation '
        '-lambda_min n n^T: g|ker d(v + tau) degenerate (det = %s), det g = %.4f < 0 (Lorentzian): eps1* in [3/5, '
        '0.60132]; round 1\'s eps1 = %.4e is %.0f times smaller' % (float(lam_lo), float(lam_hi), det_restr,
                                                                   float(det_full), EPS1_R1,
                                                                   0.6 / EPS1_R1))
    ok['C1'] = det_restr == 0 and float(lam_exact) < 0.61
    say('  C1 (control): "eps1 = 0.61 serves" refuted: a perturbation of norm %.6f < 0.61 makes the outer boundary null'
        % float(lam_exact))
    G0 = np.array(g0.evalf(30).tolist(), dtype=float)
    nn = np.array([1, -2, 0, 0, 0]) / np.sqrt(5)
    xv = np.array([2.0, 1, 0, 0, 0])
    side = {}
    for t in (0.59, 0.62):
        Gt = G0 - t * np.outer(nn, nn)
        side[t] = xv @ np.linalg.inv(Gt) @ xv
    ok['C2'] = side[0.59] < 0 < side[0.62]
    say('  C2 (control): g^-1(d(v + tau), d(v + tau)) after a perturbation of norm 0.59: %.3e (timelike), 0.62: '
        '%.3e (spacelike covector: the boundary is timelike) (floating point)' % (side[0.59], side[0.62]))
    G3 = restricted_gram(dr, sp.Rational(227, 192), sp.Rational(3, 2), xhat)
    neg = min(sp.N(e) for e in G3.eigenvals(multiple=True)) < 0
    ok['C3'] = bool(neg)
    say('  C3 (control): ker dr at r = 3/2, mu = mu_end: eigenvalues %s: a negative one, the test detects a '
        'timelike hypersurface' % [str(e) for e in G3.eigenvals(multiple=True)])
    for k, v in ok.items():
        print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
