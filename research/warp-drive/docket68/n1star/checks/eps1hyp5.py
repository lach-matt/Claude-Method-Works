#!/usr/bin/env python3
"""eps1hyp5: Lemma 1.1 (e)'s eps1 at the paper's point, measured on the hypersurfaces themselves (CONSTANTS5.md, Round
2, item (i); a correction of round 1's value, which stays valid but is about 1140 times too small), and since D623 the
general condition and Lemma 2.3's (N1STAR-PROOF.md 0.3, the section 0-4 reader's Major).

Lemma 1.1 (e) asks, for every Lorentzian g with |g - g0| <= eps1 on Omega (|.| the Euclidean operator norm of the
Cartesian matrix, as in lzeroconst5.py Z2): Sigma_tau, {r = a} and the outer boundary {v + tau - tau_end = V + 1} stay
spacelike, J^-(p; g) cap {tau >= tau0} lies in Omega, and L0 stays transverse to Sigma_tau. A hypersurface {f = c} is
spacelike for g iff g restricted to ker df is positive definite; if lambda_min(g0|ker df) >= m (Euclidean-orthonormal
basis of ker df) and |g - g0| <= eps < m, then g|ker df >= m - eps > 0. Round 1 went through |g^-1 - g0^-1| <= n^2 eps
(n = sup |g0^-1| = 33.47), which costs n^2 = 1120. Labels: computed (exact rationals, certified roots from
lzeroconst5.py's geometry); deduced (the reduction to the hyperplanes, and the causal containment below).

  H1 (exact) g0 = eta + (mu/r^2) dv dv on the three hyperplanes, in Euclidean-orthonormal bases:
       ker dtau (all of Omega):         eigenvalues 1 (x3), 1 + mu/r^2                -> lambda_min = 1;
       ker dr (on r = a):               eigenvalues 1 (x3), mu/a^2 - 1 >= mu0/a^2 - 1  -> min(1, mu0/a^2 - 1);
       ker d(v + tau) (outer boundary): eigenvalues 1 (x3), (3 + mu/r^2)/5           -> lambda_min >= 3/5.
     Checked symbolically (sympy: the restricted Gram matrices for generic mu, r and unit xhat) and exactly at P*,
     where mu0/a^2 - 1 > 12 and so lambda_min = 1 on ker dr. (D623: the ker dr value is min(1, mu0/a^2 - 1) in
     general, and {r = a} is spacelike for g0 as long as mu0/a^2 > 1; until D623 H1 asked mu0/a^2 - 1 > 1.)
  H2 (exact, sympy; deduced) so every eps1 <= 3/5 with eps1 < mu0/a^2 - 1 serves Lemma 1.1 (e), by the direct cone
     argument (Round 3, after the verifier's m3, which found round 2's path argument assuming the intermediate metrics
     Lorentzian): |g - g0| <= eps gives g >= g0 - eps I as forms; at eps = 3/5 (at P*; where mu0/a^2 - 1 <= 3/5, at eps
     = (mu0/a^2 - 1)/2), g0 - eps I restricted to ker dtau, to ker dr at r = a and to ker d(v + tau) has least
     eigenvalues 1 - eps, min(1, mu0/a^2 - 1) - eps (2/5 and 2/5 at P*) and (3 + mu/r^2)/5 - eps > 0 (mu/(5 r^2) at
     3/5), so the hypersurfaces stay spacelike; and g0 - eps I has exactly one negative eigenvalue (m - eps - (1 +
     m^2)^(1/2), m = mu/r^2), so the g-causal vectors lie in its causal double cone, whose two halves are convex and on
     which dtau, dr (at r = a) and d(v + tau) do not vanish, hence keep the signs they have on g0's future cone: the
     time orientation, the containment and (L0(tau) = 1) the transversality follow.
  H3 (exact) sharpness: at the corner of the outer boundary, r = b(tau0) taken at the lower end b_lo of its certified
     interval (tau = tau0; v > v_end and mu = mu_end), the perturbation delta g = -lambda n (x) n, n the unit vector of
     ker d(v + tau) along (1, -2 xhat)/sqrt5, lambda = (3 + mu_end/r^2)/5 = 0.6013096..., keeps det < 0 (Lorentzian)
     and makes g|ker d(v + tau) degenerate (the boundary null): no eps1 above 0.6013096 serves (Round 3: the verifier's
     corner; round 2's r = 67/5 gave the weaker 0.6013169, still printed). eps1* lies in [3/5, 0.6013096] in the
     operator norm.
  H4 (exact; D623) the general condition, eps1 <= 3/5 and eps1 < mu0/a^2 - 1, at seven values of m0 := mu0/a^2 > 1
     (P*'s, 101/100, 13/10, 4/3, 8/5, 2, 5): (a) at the largest admissible eps (3/5 where m0 - 1 > 3/5, else (m0 - 1)
     (1 - 10^-3)) the three restricted forms of g0 - eps I are positive definite (at m = m0 on ker dr; every m >= 0 on
     the other two) and g0 - eps I has one negative eigenvalue; (b) at a point of {r = a} where mu = mu0 (tau = tau0:
     v = tau0 + a < v_start), g = g0 - (m0 - 1) e_tau e_tau^T is Lorentzian (det = -m0^2), |g - g0| = m0 - 1, and g
     restricted to ker dr is degenerate: {r = a} is null for it, so no eps1 >= m0 - 1 serves.
  H5 (exact; certified; computed, floating point; D623) Lemma 2.3's threshold s0 := inf over Omega of g0's least
     absolute eigenvalue. Exact: g0 = eta + m U U^T, U = (1, xhat), has eigenvalues 1 (x3) and m +- (m^2 + 1)^(1/2),
     its least absolute one s(m) = (m^2 + 1)^(1/2) - m decreases in m, so s0 = s(m*), m* := sup_Omega mu/r^2 =
     mu_end/a^2 at P* (the corner (tau_end, a) lies in Omega with v > v_end). By a grid: 41 slices tau (tau0 to
     tau_end), 161 radii (a to b(tau)), 4 directions xhat, mu(v) from envelope5.py's C_c^inf envelope (int env^2 =
     105/128, so mu_end = 227/192, checked); numpy's eigenvalues of the Cartesian 5 x 5 matrix: at every grid point the
     least absolute one is s(mu/r^2) to 10^-12, and the grid's minimum, on r = a where mu = mu_end to 10^-12 (the
     corner's value; the envelope is flat to that order from v = 3.1 on), equals s(m*) and lies in
     lzerotrace5.py T7's certified enclosure [0.030768559, 0.030768560] (to 10^-12). And s0 < s(1) = 2^(1/2) - 1 < 3/5
     (exact: m* >= mu0/a^2 > 1).
  H6 (computed, floating point; deduced: Weyl's inequality; D623) for eps1 < s0 every symmetric gt with |gt - g0| <=
     eps1 is Lorentzian with |gt^-1| <= (s0 - eps1)^-1: at the corner and at 30 random points of the grid, for eps1 =
     s0/2, 9 s0/10, 99 s0/100, 300 random symmetric perturbations of operator norm eps1 each give exactly one negative
     eigenvalue and |gt^-1| (s0 - eps1) <= 1 + 10^-9; the perturbation eps1 e e^T along the eigenvector e of -s0 at the
     corner attains it (|gt^-1| (s0 - eps1) = 1 to 10^-9), so the bound is sharp.
  Controls (must fail, and do): C1 (Round 3, now mutating H3's code path) H3's degeneracy test run with the
  perturbation's size lowered to 59/100 reports a non-degenerate restricted form, so the test does not certify a null
  boundary where there is none; C2 a perturbation of norm 0.59 of the same shape keeps the boundary spacelike, and 0.62
  does not (floating point, the sign of g^-1(d(v + tau), d(v + tau))); C3 the hyperplane test applied to ker dr at r =
  1.5 (where mu/r^2 < 1, dr spacelike: {r = 1.5} is timelike for g0) returns a negative eigenvalue, so the test does
  detect a non-spacelike hypersurface; C4 (Round 3) H2's test at eps = 0.61 finds a non-positive least eigenvalue on
  ker d(v + tau) at the corner: the cone argument does not pass a too-large eps. D623: C5 H4's test run on the old
  form, eps1 = 3/5 whatever mu0/a^2, at m0 = 13/10 (which Lemma 1.1's hypotheses allow) finds the least eigenvalue
  -3/10 on ker dr: the old form fails there, and H4's (eps1 < 3/10) passes; C6 H5's grid test run on Omega with the
  inner sphere cut away (r >= a + 1/10) finds a minimum above s(m*): the test detects a grid that misses the infimum;
  C7 (50 digits) at the corner, the perturbation (s0 - 10^-12) e e^T, of norm below s0, gives a Lorentzian gt with
  |gt^-1| = 10^12, which H6's test at eps1 = 99 s0/100 rejects: for eps1 >= s0 no bound on |gt^-1| holds; C8 H6's
  test with s0 replaced by g0's next eigenvalue in absolute value, 1, rejects the random perturbations.

    python3 checks/eps1hyp5.py
"""
import os
import sys
import textwrap
from fractions import Fraction as Fr

import mpmath
import numpy as np
import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lzeroconst5 as LZ  # noqa: E402  (round 1's certified geometry at P*, imported, not copied)
import envelope5 as EV  # noqa: E402  (round 2's C_c^inf envelope: MPOW, the shape of beta)

EPS1_R1 = 5.2617e-4                                  # READ: CONSTANTS5.md 1.4 (round 1)
E_LO, E_HI = Fr(30768559, 10 ** 9), Fr(30768560, 10 ** 9)   # READ: lzerotrace5.out T7, the certified enclosure of s0
TOL = 1e-12


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


M_, E_ = sp.symbols('m eps', nonnegative=True)
U5 = sp.Matrix([1, 1, 0, 0, 0])
G0M = sp.diag(-1, 1, 1, 1, 1) + M_ * U5 * U5.T
DTAU, DR, DVT = [1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [2, 1, 0, 0, 0]


def restricted_eps(cov):
    """g0 - eps I on ker cov (xhat = e1), Euclidean-orthonormal basis, exact in (m, eps)"""
    Kc = sp.Matrix.hstack(*sp.Matrix([cov]).nullspace())
    Qc, _ = Kc.QRdecomposition()
    return sp.simplify(Qc.T * (G0M - E_ * sp.eye(5)) * Qc)


REST = {}


def rest_eigs(name):
    if name not in REST:
        cov = {'dtau': DTAU, 'dr': DR, 'd(v+tau)': DVT}[name]
        REST[name] = sorted({sp.simplify(z) for z in restricted_eps(cov).eigenvals()}, key=str)
    return REST[name]


def least_at(name, eps, m):
    return min((sp.simplify(z.subs({E_: eps, M_: m})) for z in rest_eigs(name)), key=float)


FULL = []


def one_negative(eps, ms=(0, sp.Rational(1, 100), 1, 13, 1000)):
    if not FULL:
        FULL.extend(sp.simplify(z) for z in (G0M - E_ * sp.eye(5)).eigenvals())
    full = FULL
    return all(sum(1 for z in full if sp.simplify(z.subs({E_: eps, M_: mv})).is_negative) == 1 for mv in ms)


def eps_rule(m0, old=False):
    """the largest eps Lemma 1.1 (e) admits at m0 = mu0/a^2 (attained at 3/5; approached below m0 - 1); old=True is
    the form before D623, eps1 = 3/5 whatever m0"""
    m0 = sp.nsimplify(m0)
    if old or m0 - 1 > sp.Rational(3, 5):
        return sp.Rational(3, 5)
    return (m0 - 1) * (1 - sp.Rational(1, 1000))


def h4_point(m0, old=False):
    """H4 at one m0: (a) the cone argument at eps_rule(m0); (b) the sharp perturbation at eps = m0 - 1"""
    m0 = sp.nsimplify(m0)
    eps = eps_rule(m0, old)
    l_dt = least_at('dtau', eps, 0)                    # increasing in m: m = 0 is the worst
    l_dr = least_at('dr', eps, m0)                     # on r = a, mu >= mu0: m >= m0, increasing
    l_dv = least_at('d(v+tau)', eps, 0)                # increasing in m
    cone = l_dt > 0 and l_dr > 0 and l_dv >= 0 and (l_dv > 0 or eps == sp.Rational(3, 5)) and one_negative(eps)
    et = sp.eye(5)[:, 0]
    g = (G0M - (M_ - 1) * et * et.T).subs(M_, m0)
    Kdr = sp.Matrix.hstack(*sp.Matrix([DR]).nullspace())
    evg = list(g.eigenvals(multiple=True))
    sharp = (sp.simplify(g.det() + m0 ** 2) == 0 and sum(1 for z in evg if sp.N(z) < 0) == 1
             and sp.simplify((Kdr.T * g * Kdr).det()) == 0)
    return dict(eps=eps, l_dt=l_dt, l_dr=l_dr, l_dv=l_dv, cone=bool(cone), sharp=bool(sharp))


def s_closed(m):
    return np.sqrt(m * m + 1) - m


def mu_of_v(g, n=40001):
    """mu(v) = mu0 + (2/9) A^2 int_{v_start}^{v} env^2, env the C_c^inf envelope of envelope5.py (computed, floating
    point: the shape beta and its normalisation c, int env^2 = 105/128, by the trapezoid rule on n points)"""
    vs, ve = float(LZ.VS), float(LZ.VE)
    v = np.linspace(vs, ve, n)
    y = (2 * v - 4) / 3
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        beta = np.where(np.abs(y) < 1, np.cos(np.pi * y / 2) ** EV.MPOW * np.exp(-y * y / (1 - y * y)), 0.0)
    b2 = beta ** 2
    ib2 = np.trapezoid(b2, y)
    c2 = (105 / 128) / (1.5 * ib2)
    cum = np.concatenate([[0.0], np.cumsum((b2[1:] + b2[:-1]) / 2 * np.diff(v))]) * c2
    mu = float(LZ.MU0) + 2 / 9 * float(LZ.A_AMP) ** 2 * cum
    return lambda vv: np.interp(vv, v, mu, left=float(LZ.MU0), right=mu[-1]), mu[-1]


def g0_cart(m, xh):
    """the Cartesian g0 = eta + m U U^T, U = (1, xhat), stacked over points (floating point)"""
    U = np.concatenate([np.ones((len(m), 1)), xh], axis=1)
    G = np.einsum('i,jk->ijk', np.ones(len(m)), np.diag([-1.0, 1, 1, 1, 1]))
    return G + m[:, None, None] * np.einsum('ij,ik->ijk', U, U)


def grid(g, r_cut=0.0, nt=41, nr=161):
    """(tau, r, xhat) over Omega at P*, with mu(v); returns m = mu/r^2, the directions, and the corner's index"""
    rng = np.random.default_rng(623)
    dirs = [np.array([1.0, 0, 0, 0]), np.array([0.5, 0.5, 0.5, 0.5])]
    for _ in range(2):
        d = rng.standard_normal(4)
        dirs.append(d / np.linalg.norm(d))
    a = float(g['a'][1])
    te = float(g['tau_end'][0])
    V = float(g['V'])
    mu, mu_end_num = mu_of_v(g)
    pts = []
    for tau in np.linspace(float(LZ.TAU0), te, nt):
        b = V + 1 + te - 2 * tau
        for r in np.linspace(a + r_cut, b, nr):
            for d in dirs:
                pts.append((tau, r, d))
    tau = np.array([p[0] for p in pts])
    r = np.array([p[1] for p in pts])
    xh = np.array([p[2] for p in pts])
    m = mu(tau + r) / r ** 2
    return m, xh, (tau, r), mu_end_num


def h5(g, r_cut=0.0):
    """the closed form (exact) and the grid (floating point) for s0"""
    mm = sp.Symbol('m', positive=True)
    ev = (sp.diag(-1, 1, 1, 1, 1) + mm * U5 * U5.T).eigenvals()
    closed = (ev.get(sp.Integer(1)) == 3 and any(sp.simplify(k - (mm - sp.sqrt(mm ** 2 + 1))) == 0 for k in ev)
              and any(sp.simplify(k - (mm + sp.sqrt(mm ** 2 + 1))) == 0 for k in ev))
    sm = sp.sqrt(mm ** 2 + 1) - mm
    decr = sp.simplify(sp.diff(sm, mm) + sm / sp.sqrt(mm ** 2 + 1)) == 0      # s' = -s/(m^2 + 1)^(1/2) < 0
    m, xh, (tau, r), mu_end_num = grid(g, r_cut)
    G = g0_cart(m, xh)
    lam = np.linalg.eigvalsh(G)
    least = np.min(np.abs(lam), axis=1)
    pointwise = float(np.max(np.abs(least - s_closed(m))))
    i = int(np.argmin(least))
    gmin = float(least[i])
    m_star = float(g['mu_end'] / g['a'][1] ** 2)
    corner = abs(r[i] - float(g['a'][1])) < 1e-12 and abs(m[i] * r[i] ** 2 - mu_end_num) < TOL   # mu = mu_end there
    m_lo = LZ.MU0 / g['a'][1] ** 2
    below = m_lo > 1 and sp.sqrt(2) - 1 < sp.Rational(3, 5)
    return dict(closed=closed, decr=decr, pointwise=pointwise, gmin=gmin, s_star=float(s_closed(np.array([m_star]))[0]),
                corner=corner, below=bool(below), mu_end_num=mu_end_num, n=len(m), m=m, xh=xh, i=i, G=G)


def weyl_test(G, s0, eps1, rng, trials=300, bound_s=None):
    """random symmetric E with |E|_op = eps1: (one negative eigenvalue, max |gt^-1| (bs - eps1)); bs = s0 unless set"""
    bs = s0 if bound_s is None else bound_s
    E = rng.standard_normal((trials, 5, 5))
    E = E + np.transpose(E, (0, 2, 1))
    E *= (eps1 / np.max(np.abs(np.linalg.eigvalsh(E)), axis=1))[:, None, None]
    lam = np.linalg.eigvalsh(G[None] + E)
    neg = np.all(np.sum(lam < 0, axis=1) == 1)
    worst = float(np.max((bs - eps1) / np.min(np.abs(lam), axis=1)))
    return bool(neg), worst


def h6(r5, s0, bound_s=None):
    rng = np.random.default_rng(6230)
    idx = [r5['i']] + list(rng.choice(r5['n'], 30, replace=False))
    ok_neg, worst = True, 0.0
    for eps1 in (s0 / 2, 0.9 * s0, 0.99 * s0):
        for j in idx:
            n_, w_ = weyl_test(r5['G'][j], s0, eps1, rng, bound_s=bound_s)
            ok_neg &= n_
            worst = max(worst, w_)
    G = r5['G'][r5['i']]
    lam, Q = np.linalg.eigh(G)
    k = int(np.argmin(np.abs(lam)))
    e = Q[:, k]
    eps1 = 0.9 * s0
    att = (s0 - eps1) / np.min(np.abs(np.linalg.eigvalsh(G + eps1 * np.outer(e, e))))
    return ok_neg, worst, float(att)


def c7_control(g):
    """the aligned perturbation of norm s0 - 1e-12 at the corner, at 50 digits"""
    with mpmath.workdps(50):
        ms = mpmath.mpf(g['mu_end'].numerator) / g['mu_end'].denominator
        a = (mpmath.mpf(9) / 1250) ** (mpmath.mpf(1) / 8) / 2              # a = q0/2, q0^8 = 9/1250 (T1)
        m = ms / a ** 2
        G = mpmath.matrix([[-1 + m, m, 0, 0, 0], [m, 1 + m, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0],
                           [0, 0, 0, 0, 1]])
        s0 = mpmath.sqrt(m ** 2 + 1) - m
        E, Q = mpmath.eigsy(G)
        k = min(range(5), key=lambda j: abs(E[j]))
        e = Q[:, k]
        size = s0 - mpmath.mpf(10) ** -12
        Gp = G + size * (e * e.T)
        E2, _ = mpmath.eigsy(Gp)
        inv = 1 / min(abs(x) for x in E2)
        neg = sum(1 for x in E2 if x < 0)
        bound = 1 / (s0 - mpmath.mpf('0.99') * s0)
        return dict(neg=neg, inv=float(inv), size=float(size), s0=float(s0), bound=float(bound),
                    rejected=bool(inv > bound), lorentz=neg == 1)


def main():
    ok = {}
    mu, r = sp.symbols('mu r', positive=True)
    xhat = (1, 0, 0, 0)          # O(4) acts transitively on the directions and fixes eta, dtau, dr, dv: one suffices
    lx = sp.Symbol('x')
    want = {'dtau': [1, 1, 1, 1 + mu / r ** 2], 'dr': [1, 1, 1, mu / r ** 2 - 1],
            'd(v+tau)': [1, 1, 1, (3 + mu / r ** 2) / 5]}
    ev = {}
    same = True
    for name, xi in (('dtau', DTAU), ('dr', DR), ('d(v+tau)', DVT)):
        G = restricted_gram(xi, mu, r, xhat)
        ev[name] = list(G.eigenvals(multiple=True))
        same &= sp.simplify(G.charpoly(lx).as_expr() - sp.prod([lx - w for w in want[name]])) == 0
    g = LZ.geometry()
    a_hi = g['a'][1]
    m_dr = LZ.MU0 / a_hi ** 2 - 1                      # mu >= mu0 on r = a
    ok['H1'] = same and m_dr > 0
    say('  H1: eigenvalues of g0 on the hyperplanes (sympy, generic mu, r): %s; equal to the closed forms: %s; on r = a '
        'at P*: mu/a^2 - 1 >= %.4f > 0, so lambda_min = 1, min(1, mu0/a^2 - 1) = %.4f and >= 3/5' % (
            {k: [str(e) for e in v] for k, v in ev.items()}, same, float(m_dr), float(min(Fr(1), m_dr))))

    # H2 (Round 3; D623 general): the direct cone argument at an admissible eps, exact in m = mu/r^2
    m_a = sp.Rational((LZ.MU0 / a_hi ** 2).numerator, (LZ.MU0 / a_hi ** 2).denominator)
    eps_h2 = sp.Rational(3, 5) if m_a - 1 > sp.Rational(3, 5) else (m_a - 1) / 2
    rest = {name: rest_eigs(name) for name in ('dtau', 'dr', 'd(v+tau)')}
    one_neg = one_negative(eps_h2)                                       # exact signs (Round 4, m6)
    l_dt = least_at('dtau', eps_h2, 0)
    l_dr = least_at('dr', eps_h2, m_a)
    l_dv = [sp.simplify(z.subs(E_, eps_h2)) for z in rest['d(v+tau)']]
    ok['H2'] = (l_dt == 1 - eps_h2 and l_dr == min(1, m_a - 1) - eps_h2 and l_dr > 0
                and sp.simplify(M_ / 5 + sp.Rational(3, 5) - eps_h2) in l_dv and one_neg)
    say('  H2: g0 - eps I on the kernels (exact, m = mu/r^2): %s; at eps = %s: least %.4f on ker dtau (m >= 0), %.4f '
        'on ker dr at r = a, %s on ker d(v + tau); one negative eigenvalue of g0 - eps I at m = 0, 1/100, 1, 13, '
        '1000 (exact signs; every m >= 0 from the closed form, deduced): %s; '
        'so every eps1 <= 3/5 with eps1 < mu0/a^2 - 1 = %.4f serves (direct cone argument)' % (
            {k: [str(z) for z in v] for k, v in rest.items()}, eps_h2, float(l_dt), float(l_dr),
            [str(z) for z in l_dv], one_neg, float(m_a - 1)))

    # H3: sharpness at the outer boundary on Sigma_tau0
    b_lo, b_hi = g['b0']
    mu_e = g['mu_end']
    lam_lo = (3 + mu_e / b_hi ** 2) / 5
    lam_hi = (3 + mu_e / b_lo ** 2) / 5

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

    # H4 (D623): the general condition
    m0s = [m_a, sp.Rational(101, 100), sp.Rational(13, 10), sp.Rational(4, 3), sp.Rational(8, 5), 2, 5]
    h4 = [(m0, h4_point(m0)) for m0 in m0s]
    v_r_a = LZ.TAU0 + a_hi                                     # the point (tau0, a): v < v_start, mu = mu0
    ok['H4'] = all(p['cone'] and p['sharp'] for _, p in h4) and v_r_a < LZ.VS
    say('  H4 (D623): Lemma 1.1 (e) at m0 = mu0/a^2: at the largest admissible eps (min(3/5, ~(m0 - 1))) the cone '
        'argument passes, and g0 - (m0 - 1) e_tau e_tau^T (Lorentzian, det -m0^2) makes {r = a} null at (tau0, a), '
        'where v = %.4f < v_start (mu = mu0) (exact): %s' % (float(v_r_a), '; '.join(
            'm0 = %s: eps %s, least on ker dr %s, cone %s, null at m0 - 1 %s' % (
                ('P* %.4f' % float(m0)) if m0 == m_a else str(m0), str(p['eps']) if p['eps'] == sp.Rational(3, 5)
                else '%.6f' % float(p['eps']), sp.nsimplify(p['l_dr']) if m0 != m_a else '%.4f' % float(p['l_dr']),
                p['cone'], p['sharp']) for m0, p in h4)))

    # H5 (D623): s0, by the closed form and by a grid
    r5 = h5(g)
    s_star = r5['s_star']
    ok['H5'] = (r5['closed'] and r5['decr'] and r5['pointwise'] < TOL and abs(r5['gmin'] - s_star) < TOL
                and r5['corner'] and float(E_LO) - TOL <= r5['gmin'] <= float(E_HI) + TOL and r5['below']
                and abs(r5['mu_end_num'] - 227 / 192) < 1e-9)
    say('  H5 (D623): g0 = eta + m U U^T has eigenvalues 1 (x3), m +- (m^2 + 1)^(1/2) (exact): %s; s(m) = (m^2 + '
        '1)^(1/2) - m decreases (exact): %s; grid of %d points over Omega (mu(v) from the envelope, mu_end = %.12f '
        'against 227/192): least |eigenvalue| = s(mu/r^2) at every point to %.1e; grid minimum %.12f on r = a with mu '
        '= mu_end to 1e-12 (the corner\'s value): %s; s(m*) = %.12f; in T7\'s enclosure [%s, %s]: %s; s0 < 2^(1/2) '
        '- 1 < 3/5 (m* > 1, exact): %s' % (
            r5['closed'], r5['decr'], r5['n'], r5['mu_end_num'], r5['pointwise'], r5['gmin'], r5['corner'], s_star,
            float(E_LO), float(E_HI), float(E_LO) - TOL <= r5['gmin'] <= float(E_HI) + TOL, r5['below']))

    # H6 (D623): Weyl's inequality, |gt^-1| <= (s0 - eps1)^-1
    s0 = r5['gmin']
    neg6, worst6, att6 = h6(r5, s0)
    ok['H6'] = neg6 and worst6 <= 1 + 1e-9 and abs(att6 - 1) < 1e-9
    say('  H6 (D623): 31 points (the corner and 30 random), eps1 = s0/2, 9 s0/10, 99 s0/100, 300 random symmetric '
        'perturbations of norm eps1 each: one negative eigenvalue always: %s; max |gt^-1| (s0 - eps1) = %.12f <= 1 '
        '(Weyl); along the eigenvector of -s0 at the corner, eps1 = 9 s0/10: |gt^-1| (s0 - eps1) = %.12f (sharp) '
        '(floating point)' % (neg6, worst6, att6))

    # controls
    det_m, _, _, _ = h3_null(rr, sp.Rational(59, 100))
    ok['C1'] = not (det_m == 0)
    say('  C1 (control): H3\'s test with the size lowered to 59/100: restricted determinant %.4e != 0, the boundary '
        'stays spacelike: the test fails, as it must' % float(det_m))
    l_dv61 = least_at('d(v+tau)', sp.Rational(61, 100), sp.Rational(mu_e.numerator, mu_e.denominator)
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
    G3 = restricted_gram(DR, sp.Rational(227, 192), sp.Rational(3, 2), xhat)
    neg = min(sp.N(e) for e in G3.eigenvals(multiple=True)) < 0
    ok['C3'] = bool(neg)
    say('  C3 (control): ker dr at r = 3/2, mu = mu_end: eigenvalues %s: a negative one, the test detects a '
        'timelike hypersurface' % [str(e) for e in G3.eigenvals(multiple=True)])
    old13 = h4_point(sp.Rational(13, 10), old=True)
    new13 = h4_point(sp.Rational(13, 10))
    ok['C5'] = not old13['cone'] and old13['l_dr'] == -sp.Rational(3, 10) and new13['cone']
    say('  C5 (control, D623): H4\'s test on the old form (eps1 = 3/5 whatever mu0/a^2) at m0 = 13/10: least '
        'eigenvalue on ker dr %s, cone %s: the old form fails, as it must; H4\'s eps %.6f < 3/10 passes: %s' % (
            old13['l_dr'], old13['cone'], float(new13['eps']), new13['cone']))
    r5c = h5(g, r_cut=0.1)
    ok['C6'] = abs(r5c['gmin'] - s_star) > 1e3 * TOL
    say('  C6 (control, D623): H5\'s grid test on Omega cut to r >= a + 1/10: minimum %.9f against s(m*) = %.9f: '
        'rejected: %s' % (r5c['gmin'], s_star, ok['C6']))
    c7 = c7_control(g)
    ok['C7'] = c7['lorentz'] and c7['rejected'] and c7['size'] < c7['s0'] and c7['inv'] > 1e11
    say('  C7 (control, D623): at the corner, (s0 - 1e-12) e e^T (norm %.13f < s0 = %.13f; 50 digits): Lorentzian '
        '(%d negative eigenvalue), |gt^-1| = %.4e > (s0 - 99 s0/100)^-1 = %.1f: H6\'s test rejects it: %s; for eps1 >= '
        's0 no bound holds' % (c7['size'], c7['s0'], c7['neg'], c7['inv'], c7['bound'], c7['rejected']))
    _, worst8, _ = h6(r5, s0, bound_s=1.0)
    ok['C8'] = worst8 > 1 + 1e-9
    say('  C8 (control, D623): H6\'s test with the bound (1 - eps1)^-1 (g0\'s next eigenvalue for s0): max |gt^-1| (1 - '
        'eps1) = %.3f > 1: rejected: %s' % (worst8, ok['C8']))
    for k, v in ok.items():
        print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
