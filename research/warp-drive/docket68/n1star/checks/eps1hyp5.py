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
  H2 (exact, sympy; deduced) so every eps1 <= 3/5 serves Lemma 1.1 (e), by the direct cone argument (Round 3, after
     the verifier's m3, which found round 2's path argument assuming the intermediate metrics Lorentzian): |g - g0| <=
     eps gives g >= g0 - eps I as forms; at eps = 3/5, g0 - eps I restricted to ker dtau, to ker dr at r = a and to
     ker d(v + tau) has least eigenvalues 2/5, 2/5 (P*) and mu/(5 r^2) > 0, so the hypersurfaces stay spacelike; and
     g0 - eps I has exactly one negative eigenvalue (m - eps - (1 + m^2)^(1/2), m = mu/r^2), so the g-causal vectors
     lie in its causal double cone, whose two halves are convex and on which dtau, dr (at r = a) and d(v + tau) do not
     vanish, hence keep the signs they have on g0's future cone: the time orientation, the containment and (L0(tau) =
     1) the transversality follow.
  H3 (exact) sharpness: at the corner of the outer boundary, r = b(tau0) taken at the lower end b_lo of its certified
     interval (tau = tau0; v > v_end and mu = mu_end), the perturbation delta g = -lambda n (x) n, n the unit vector of
     ker d(v + tau) along (1, -2 xhat)/sqrt5, lambda = (3 + mu_end/r^2)/5 = 0.6013096..., keeps det < 0 (Lorentzian)
     and makes g|ker d(v + tau) degenerate (the boundary null): no eps1 above 0.6013096 serves (Round 3: the verifier's
     corner; round 2's r = 67/5 gave the weaker 0.6013169, still printed). eps1* lies in [3/5, 0.6013096] in the
     operator norm.
  Controls (must fail, and do): C1 (Round 3, now mutating H3's code path) H3's degeneracy test run with the
  perturbation's size lowered to 59/100 reports a non-degenerate restricted form, so the test does not certify a null
  boundary where there is none; C2 a perturbation of norm 0.59 of the same shape keeps the boundary spacelike, and 0.62
  does not (floating point, the sign of g^-1(d(v + tau), d(v + tau))); C3 the hyperplane test applied to ker dr at r =
  1.5 (where mu/r^2 < 1, dr spacelike: {r = 1.5} is timelike for g0) returns a negative eigenvalue, so the test does
  detect a non-spacelike hypersurface; C4 (Round 3) H2's test at eps = 0.61 finds a non-positive least eigenvalue on
  ker d(v + tau) at the corner: the cone argument does not pass a too-large eps.

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

    # H2 (Round 3): the direct cone argument at eps = 3/5, exact in m = mu/r^2
    m_, e_ = sp.symbols('m eps', nonnegative=True)
    U5 = sp.Matrix([1, 1, 0, 0, 0])
    g0m = sp.diag(-1, 1, 1, 1, 1) + m_ * U5 * U5.T

    def restricted_eps(cov):
        Kc = sp.Matrix.hstack(*sp.Matrix([cov]).nullspace())
        Qc, _ = Kc.QRdecomposition()
        return sp.simplify(Qc.T * (g0m - e_ * sp.eye(5)) * Qc)

    def least_restricted(cov, eps, mval):
        return min(restricted_eps(cov).subs({e_: eps, m_: mval}).eigenvals(multiple=True), key=lambda z: float(z))

    rest = {name: sorted({sp.simplify(z) for z in restricted_eps(cov).eigenvals()}, key=str)
            for name, cov in (('dtau', dtau), ('dr', dr), ('d(v+tau)', dvt))}
    full = [sp.simplify(z) for z in (g0m - e_ * sp.eye(5)).eigenvals()]
    one_neg = all(sum(1 for z in full if sp.simplify(z.subs({e_: sp.Rational(3, 5), m_: mv})).is_negative) == 1
                  for mv in (0, sp.Rational(1, 100), 1, 13, 1000))     # exact signs (Round 4, m6)
    m_a = sp.Rational((LZ.MU0 / a_hi ** 2).numerator, (LZ.MU0 / a_hi ** 2).denominator)
    l_dt = min((sp.nsimplify(sp.simplify(z.subs({e_: sp.Rational(3, 5), m_: 0}))) for z in rest['dtau']), key=float)
    l_dr = min((sp.simplify(z.subs({e_: sp.Rational(3, 5), m_: m_a})) for z in rest['dr']), key=float)
    l_dv = [sp.simplify(z.subs(e_, sp.Rational(3, 5))) for z in rest['d(v+tau)']]
    ok['H2'] = l_dt == sp.Rational(2, 5) and l_dr == sp.Rational(2, 5) and m_ / 5 in l_dv and one_neg
    say('  H2: g0 - eps I on the kernels (exact, m = mu/r^2): %s; at eps = 3/5: least %.4f on ker dtau (m >= 0), %.4f '
        'on ker dr at r = a (P*), %s on ker d(v + tau); one negative eigenvalue of g0 - (3/5) I at m = 0, 1/100, 1, 13, '
        '1000 (exact signs; every m >= 0 from the closed form, deduced): %s; '
        'so eps1 = 3/5 serves (direct cone argument)' % ({k: [str(z) for z in v] for k, v in rest.items()}, float(l_dt),
                                                           float(l_dr), [str(z) for z in l_dv], one_neg))

    # H3: sharpness at the outer boundary on Sigma_tau0
    b_lo, b_hi = g['b0']
    mu_e = g['mu_end']
    lam_lo = (3 + mu_e / b_hi ** 2) / 5
    lam_hi = (3 + mu_e / b_lo ** 2) / 5
    lam = lam_hi                                        # a rational at least lambda_min, used below exactly
    # exact check with r replaced by the rational b_lo (the boundary radius within 1e-25): build g at xhat = e1
    def h3_null(rr, lam_override=None):
        mue = sp.Rational(mu_e.numerator, mu_e.denominator)
        rq = sp.Rational(rr.numerator, rr.denominator)
        g0x = sp.diag(-1, 1, 1, 1, 1) + (mue / rq ** 2) * sp.Matrix([1, 1, 0, 0, 0]) * sp.Matrix([1, 1, 0, 0, 0]).T
        nx = sp.Matrix([1, -2, 0, 0, 0]) / sp.sqrt(5)
        lam_x = (3 + mue / rq ** 2) / 5 if lam_override is None else lam_override
        gpx = g0x - lam_x * nx * nx.T
        # the boundary is null for g iff g restricted to ker xi is degenerate (determinant 0)
        Kx = sp.Matrix.hstack(*sp.Matrix([[2, 1, 0, 0, 0]]).nullspace())
        Qx, _ = Kx.QRdecomposition()
        return sp.simplify((Qx.T * gpx * Qx).det()), sp.simplify(gpx.det()), lam_x, g0x

    rr = b_lo                                          # the corner, tau = tau0 at b_lo (Round 3)
    assert (LZ.VE + LZ.T + 1 + g['tau_end'][0] - rr) / 2 >= LZ.TAU0 and LZ.TAU0 + rr > LZ.VE
    det_restr, det_full, lam_exact, g0 = h3_null(rr)
    det67, _, lam67, _ = h3_null(Fr(67, 5))
    ok['H3'] = (det_restr == 0 and det_full < 0 and Fr(3, 5) < lam_lo and lam_exact < sp.Rational(60131, 100000)
                and det67 == 0 and lam67 == sp.Rational(2591339, 4309440))
    say('  H3: lambda_min on the outer boundary: at tau0 (3 + mu_end/b(tau0)^2)/5 in [%.8f, %.8f]; at the corner r = '
        'b_lo it is %.8f, and -lambda n n^T there makes g|ker d(v + tau) degenerate (det = %s), with det g = %.4f < 0 '
        '(Lorentzian): eps1* in [3/5, %.7f] (round 2\'s r = 67/5: %s = %.7f, also null); round 1\'s eps1 = %.4e is '
        '%.0f times smaller than 3/5' % (float(lam_lo), float(lam_hi), float(lam_exact), det_restr, float(det_full),
                                         float(lam_exact) + 5e-8, lam67, float(lam67), EPS1_R1, 0.6 / EPS1_R1))
    det_m, _, _, _ = h3_null(rr, sp.Rational(59, 100))
    ok['C1'] = not (det_m == 0)
    say('  C1 (control): H3\'s test with the size lowered to 59/100: restricted determinant %.4e != 0, the boundary '
        'stays spacelike: the test fails, as it must' % float(det_m))
    l_dv61 = least_restricted(dvt, sp.Rational(61, 100), sp.Rational(mu_e.numerator, mu_e.denominator)
                              / sp.Rational(rr.numerator, rr.denominator) ** 2)
    ok['C4'] = float(l_dv61) <= 0
    say('  C4 (control): H2\'s test at eps = 0.61 on ker d(v + tau) at the corner: least eigenvalue %.4e <= 0: the cone '
        'argument does not pass eps = 0.61' % float(l_dv61))
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
