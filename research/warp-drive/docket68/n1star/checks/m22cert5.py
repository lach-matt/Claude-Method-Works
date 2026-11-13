#!/usr/bin/env python3
"""m22cert5: the attempt at a certified lower bound m_lo on |M_22| by an a posteriori energy estimate (M22CERT5.md).
Labels: computed (exact, sympy), certified (exact rationals; Arb balls, python-flint), computed (floating point),
READ (cited values). It imports m22evol5.py (the system, the solver, the data) and changes nothing in it.

  X1 (exact) The tau-tau row of the lower-order operator. With eta = g0 - (mu/r^2) dv dv the flat metric of the
     Kerr-Schild Cartesian coordinates (in which the record's energy, Lemma 2.3 and Lemma 9.1, works componentwise),
     L := E - P_eta, P_eta(m) = -(1/2) g0^ab nabla^eta_a nabla^eta_b m, is the operator the estimate treats as forcing.
     Its tau-tau component, acting on the Cartesian scalar T = m(d_tau, d_tau) = m_vv (with m_vr = m_taur - T, m_rr =
     m_rr' - 2 m_taur + T), has no second derivative (the principal parts cancel), no d_th T, and
         L_tautau = (mu' r - mu/2)/r^3 e_tau T + (5 mu/2 - mu' r)/r^3 e_r T + z T + (other components),
     e_tau = d_tau, e_r = d_r at fixed tau (Euclidean unit vectors), z = (2 mu^3 - mu^2 r^2 + mu mu' r^3 - mu' r^5)/r^8.
  X2 (certified, exact rationals) An upper envelope rho^ >= rho of the outgoing null ray through X*, backwards from
     (tau*, a) in 2000 pieces with slopes (m_hi - 1)/(m_hi + 1), m_hi = mu_end/rho^2, rounded up.
  X3 (certified, Arb) The estimate's rate is at least (1/2) c_Y sup(||A|| q_lo^(-1/2)) with c_Y = 2^(1/2) exactly
     (stage1rate5 K2) and ||A|| >= |(5 mu/2 - mu' r)/r^3| (X1's e_r entry), evaluated on each piece at r = rho^ (a
     point of the slice), with mu >= 1, mu' <= (2/9) c^2 and q_lo, the least eigenvalue of Q (stage1rate5 K2), bounded
     above over m in [1/r^2, mu_end/r^2]. Its integral over [tau0, tau*] is a certified lower bound on the exponent of
     the estimate's Gronwall factor.
  X4 (computed, floating point; an indicator) The tau-tau component of the defect of the lifted semi-discrete state
     (the PDE applied to the spectral lift of the solver's nodal state, minus the lift of its semi-discrete d_tau^2),
     off the collocation nodes (on the grid with twice the nodes) at twelve times, at Nr x Nx = 32 x 12, 40 x 12,
     48 x 16, 64 x 20. It is not the residual of one space-time interpolant (psi is not d_r of the lifted m, and
     there is no time-interpolation error). With it in place of rho: int e^(Lambda(s)) ||rho(s)|| ds, and the
     resolution at which it would fall below the budget (extrapolated).
  X5 (computed) What m_lo buys (m22evol5's chain): the bounds at m_lo = 1 and 1/2.
  X6 (certified, Arb) That defect's tau-tau component at a slice of the 48 x 16 run (tau = -0.8): the lift
     (2D Chebyshev series through the nodal values) and the vv equation's coefficients evaluated in Arb balls, mu by
     certified quadrature of env^2 (python-flint's Petras integrator, the tails bounded) and c from its defining
     integral; at collocation nodes it reproduces the solver (|rho| < 1e-12), at midpoints it is certified nonzero;
     on boxes of half-width delta its enclosure grows as (slope) delta: the sharpness a certificate reaches, the
     boxes and time it would need.
  X7 (certified, Arb) The T-entries of the tau-tau row at X* (r = a, v = 2, mu(2) = 419/384 exactly by the
     envelope's symmetry, mu' = (2/9) c^2) and their sup over r in [a, 5], mu in [1, mu_end], mu' in [0, (2/9) c^2].
  X8 (deduced from X3 and the requirement; the data computed, floating point) The data requirement: Corollary 2
     carries E^(1/2)(tau0) with the full factor, so m_lo > 0 needs E^(1/2)(tau0) < |M_22|/(C_pt e^32.84); the data are
     cut at P_13(cos 2th), and the first omitted mode, P_15, alone contributes at least (q_lo)^(1/2) ||d_tau T_15|| to
     the data error's E^(1/2) (the modes are orthogonal in x; q_lo >= 0.196683, stage1rate5 K3).
  Controls (each mutates the computed path and must fail): C1 P_eta without its factor 1/2: X1's cancellation of the
  principal parts fails; C2 the envelope with each slope taken at the piece's end: X2's supersolution test fails; C3
  X3's bound evaluated at the outer boundary r = 3 - tau (a point of the slice, but where the coefficients are small):
  X3's threshold (a factor above 10^12) fails; C4 the interpolated d_tau^2 m_vv raised by 1e-6 of its maximum: X6's
  nodal test fails; C5 X8's requirement with C3's factor in place of X3's: the P_15 contribution falls below it, so
  X8's test fails.

    python3 checks/m22cert5.py [--selftest]       (every check; about 30 minutes)
"""
import builtins
import contextlib
import io
import math
import os
import sys
import textwrap
import time
from fractions import Fraction as Fr

import flint
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
with contextlib.redirect_stdout(io.StringIO()):
    import m22evol5 as ME              # noqa: E402  (the system, the solver, the Cauchy data)

OK = {}
T0 = time.time()
MU_END = Fr(227, 192)
C_HI = Fr(13241035, 10 ** 7)           # c <= 1.3241035 (envelope5.out E1, READ)
A_HI = Fr(26985880, 10 ** 8)           # a < 0.26985880, checked below from a^8 = 9/1250/2^8
NPIECE = 2000
KEEP = -0.8                            # the time of X6's slice (in X4's 48 x 16 run)


def print(*a, **k):  # noqa: A001
    for line in ' '.join(str(q) for q in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False), **k)
    sys.stdout.flush()


def el():
    return '[%.0fs]' % (time.time() - T0)


def arb(q):
    return flint.arb(q.numerator) / q.denominator if isinstance(q, Fr) else flint.arb(q)


# ------------------------------------------------------------------------------------------------------------------
# X1: the tau-tau row of L = E - P_eta
def tautau_row(res, half=sp.Rational(1, 2)):
    v, r, th, C, S, M0, M1 = ME.v, ME.r, ME.th, ME.C, ME.S, ME.M0, ME.M1_
    X5 = [v, r, th, sp.Symbol('p1'), sp.Symbol('p2')]
    eta = sp.diag(-1, 0, r ** 2, r ** 2 * C ** 2, r ** 2 * S ** 2)
    eta[0, 1] = eta[1, 0] = 1
    ei = eta.inv()
    gam = [[[sp.simplify(sum(ei[a, d] * (sp.diff(eta[d, b], X5[c]) + sp.diff(eta[d, c], X5[b])
                                          - sp.diff(eta[b, c], X5[d])) for d in range(5)) / 2)
             for c in range(5)] for b in range(5)] for a in range(5)]
    _, g0i = ME.background()
    g0i = g0i.subs(ME.Mf, M0)
    second = {(1, 1, 0): -half * 2 * g0i[0, 1], (0, 2, 0): -half * g0i[1, 1], (0, 0, 2): -half * g0i[2, 2],
              (2, 0, 0): -half * g0i[0, 0]}
    first = [half * sum(g0i[a, b] * gam[c][a][b] for a in range(5) for b in range(5)) for c in range(3)]
    J = {}
    for (fn, jet), c in res[('vv', 0)]['coef'].items():
        w = {'m_vv': 1, 'm_vr': -1, 'm_rr': 1}.get(fn)
        if w is not None:
            J[jet] = J.get(jet, 0) + w * c
    cancel = all(sp.simplify(J.get(j, 0) - s_) == 0 for j, s_ in second.items())
    a_ = sp.simplify(J.get((1, 0, 0), 0) - first[0])
    b_ = sp.simplify(J.get((0, 1, 0), 0) - first[1])
    c_ = sp.simplify(J.get((0, 0, 1), 0) - first[2])
    z_ = sp.simplify(J.get((0, 0, 0), 0))
    return cancel, a_, b_, c_, z_


def check_x1(res):
    cancel, a_, b_, c_, z_ = tautau_row(res)
    M0, M1, r = ME.M0, ME.M1_, ME.r
    et, er = sp.simplify(a_ - b_), b_
    want = (sp.simplify(et - (M1 * r - M0 / 2) / r ** 3) == 0 and sp.simplify(er - (5 * M0 / 2 - M1 * r) / r ** 3) == 0
            and c_ == 0 and sp.simplify(z_ - (2 * M0 ** 3 - M0 ** 2 * r ** 2 + M0 * M1 * r ** 3 - M1 * r ** 5) / r ** 8)
            == 0)
    OK['X1'] = cancel and want
    print('  X1 (exact): L = E - P_eta on the Cartesian scalar T = m(d_tau, d_tau): the principal parts cancel: %s; '
          'the e_tau, e_r, e_th coefficients are %s, %s, %s and the zero-order one %s (mu = M0, mu\' = M1): %s %s'
          % (cancel, et, er, c_, z_, OK['X1'], el()))
    bad = tautau_row(res, half=1)[0]
    OK['C1'] = not bad
    print('  C1 (control): P_eta without its factor 1/2: the principal parts cancel: %s, so X1 fails: %s'
          % (bad, OK['C1']))


# ------------------------------------------------------------------------------------------------------------------
# X2: the certified upper envelope of the ray, s = tau* - tau
def g_up(R):
    m = MU_END / (R * R)
    return (m - 1) / (m + 1)


def round_up(q, den=10 ** 12):
    return Fr(-((-q.numerator * den) // q.denominator), den)


def envelope_pieces(s_tot, at_end=False):
    ds = s_tot / NPIECE
    R, out = A_HI, []
    for _ in range(NPIECE):
        sl = g_up(R + ds) if at_end else g_up(R)
        R1 = round_up(R + ds * sl)
        out.append((R, R1, ds))
        R = R1
    return out


def super_ok(pieces):
    """each piece is linear from R0 to R1 with slope (R1 - R0)/ds >= g_up at every point of it (g_up decreasing in R,
    R nondecreasing on the piece, so the condition at R0 suffices), and stays in m_hi > 1 where g_up >= 0"""
    return all((R1 - R0) / ds >= g_up(R0) and R1 >= R0 for R0, R1, ds in pieces)


def check_x2():
    a_ok = (2 * A_HI) ** 8 > Fr(9, 1250)
    s_tot = 4 - Fr(26985878, 10 ** 8)                 # tau* - tau0 = 4 - a <= 4 - a_lo
    pieces = envelope_pieces(s_tot)
    ok = super_ok(pieces)
    OK['X2'] = a_ok and ok
    print('  X2 (certified, exact rationals): a < %s: %s; rho^ from (tau*, a^) back over %s in %d pieces is a '
          'supersolution of the backward ray equation with m <= mu_end/rho^2, so rho <= rho^: %s; rho^(tau0) = %.6f: '
          '%s' % (float(A_HI), a_ok, float(s_tot), NPIECE, ok, float(pieces[-1][1]), OK['X2']))
    OK['C2'] = not super_ok(envelope_pieces(s_tot, at_end=True))
    print('  C2 (control): each slope taken at the piece\'s end (where g_up is smaller): the supersolution test fails: '
          '%s' % OK['C2'])
    return pieces, s_tot


# ------------------------------------------------------------------------------------------------------------------
# X3: the certified lower bound on the estimate's exponent
def qlo_hi(r, n=16):
    """an upper bound of q_lo(m) over m in [1/r^2, mu_end/r^2]: the least eigenvalue of the (tau, x1) block of Q
    (trace m^2 + m + 1, det (m + 1)^2/4, so tr^2 - 4 det = m^2 (m^2 + 2 m + 2); the angular eigenvalue (1 + m)/2 is
    larger), in Arb on n sub-intervals of m, the largest upper end taken (rounded up)"""
    lo, hi = 1 / (r * r), MU_END / (r * r)
    best = 0.0
    for i in range(n):
        a_, b_ = lo + (hi - lo) * Fr(i, n), lo + (hi - lo) * Fr(i + 1, n)
        m = flint.arb((arb(a_) + arb(b_)) / 2, (arb(b_) - arb(a_)) / 2)
        tr, det = m * m + m + 1, (m + 1) ** 2 / 4
        lam = 2 * det / (tr + m * (m * m + 2 * m + 2).sqrt())
        best = max(best, float(lam.upper()) * (1 + 1e-12))
    return best


def k_lo(r):
    """(1/2) c_Y |b| / q_lo^(1/2) >= (1/2) 2^(1/2) (5/2 - (2/9) c^2 r)/r^3 / q_lo_hi^(1/2), at the point r of the
    slice"""
    rr = arb(r)
    b = (flint.arb(5) / 2 - flint.arb(2) / 9 * arb(C_HI) ** 2 * rr) / rr ** 3
    return (flint.arb(2).sqrt() / 2 * b / flint.arb(qlo_hi(r)).sqrt()).lower()


def check_x3(pieces, outer=False):
    tau_star_hi = 2 - Fr(26985878, 10 ** 8)
    tot, prof, s = flint.arb(0), [], Fr(0)
    inside = True
    for R0, R1, ds in pieces:
        if outer:
            pt = 3 - tau_star_hi + s          # r = 3 - tau at the piece's later end (smallest outer radius)
        else:
            pt = R1                           # >= rho(tau) on the whole piece
            inside &= pt <= 3 - tau_star_hi + s
        tot += k_lo(pt) * arb(ds)
        s += ds
        prof.append((float(s), float(tot.lower())))
    return tot.lower(), prof, inside


# ------------------------------------------------------------------------------------------------------------------
# X4: the residual, measured off the nodes
def bary_lobatto(xs, xt):
    n = len(xs)
    w = np.array([(-1.0) ** j * (0.5 if j in (0, n - 1) else 1.0) for j in range(n)])
    P = np.zeros((len(xt), n))
    for i, x in enumerate(xt):
        d = x - xs
        k = np.where(np.abs(d) < 1e-14)[0]
        if len(k):
            P[i, k[0]] = 1.0
        else:
            q = w / d
            P[i] = q / q.sum()
    return P


def cc_weights(N):
    xg = np.cos(np.pi * np.arange(N) / (N - 1))
    V = np.polynomial.chebyshev.chebvander(xg, N - 1)
    mom = np.array([0.0 if k % 2 else 2.0 / (1 - k * k) for k in range(N)])
    return np.linalg.solve(V.T, mom)


def xreg(Sv, tau, st):
    out = Sv.rhs(tau, st)
    _, L, speed = Sv.grid(tau)
    return out[1][0] - speed[:, None] * Sv.dr(st[1][0], L)


def residual_norm(Sv, Sf, tau, st):
    """|| alpha (I X_c - X(I u)) || over the slice in the measure pi^2 r^3 dx dr (the tau-tau component)"""
    xi_c = (1 - np.cos(np.pi * np.arange(Sv.Nr) / (Sv.Nr - 1))) / 2
    xi_f = (1 - np.cos(np.pi * np.arange(Sf.Nr) / (Sf.Nr - 1))) / 2
    Pr = bary_lobatto(xi_c, xi_f)
    Vc = np.polynomial.chebyshev.chebvander(Sv.x, Sv.Nx - 1)
    Ix = np.polynomial.chebyshev.chebvander(Sf.x, Sv.Nx - 1) @ np.linalg.inv(Vc)
    lift = lambda u: Pr @ u @ Ix.T                                  # noqa: E731
    m, pi, psi, phi, G = st
    stf = ([lift(u) for u in m], [lift(u) for u in pi], [lift(u) for u in psi], lift(phi), [lift(u) for u in G])
    Xc, Xf = xreg(Sv, tau, st), xreg(Sf, tau, stf)
    r1, L, _ = Sf.grid(tau)
    rr = r1[:, None] * np.ones((1, Sf.Nx))
    mm = Sf.mu(tau + rr) / rr ** 2
    rho = (1 + mm) / 2 * (lift(Xc) - Xf)
    wr = cc_weights(Sf.Nr) / 2 * L
    wx = np.pi / Sf.Nx * np.sqrt(1 - Sf.x ** 2)
    return float(np.sqrt(np.pi ** 2 * np.einsum('i,j,ij->', wr, wx, rho ** 2 * rr ** 3)))


# ------------------------------------------------------------------------------------------------------------------
# X6: the residual in Arb balls, at points and on boxes (the sharpness a certificate would reach)
RAT = sp.Function('RAT')


def exact_rationals(e):
    return e.replace(lambda q: q.is_Rational and not q.is_Integer, lambda q: RAT(q.p, q.q))


ACB_NS = {'sin': lambda z: z.sin(), 'cos': lambda z: z.cos(), 'sqrt': lambda z: z.sqrt(), 'exp': lambda z: z.exp(),
          'tan': lambda z: z.tan(), 'I': flint.acb(0, 1), 'pi': flint.acb.pi(),
          'RAT': lambda p, q: flint.acb(p) / q}


def acb_fn(exprs, syms):
    ACB_NS['pi'] = flint.acb.pi()                         # at the working precision
    return sp.lambdify(syms, [exact_rationals(sp.sympify(e)) for e in exprs], modules=[ACB_NS])


class ArbEnv:
    """the envelope, mu and H in Arb balls: c from int beta^2 by certified quadrature (Petras, python-flint) with the
    tails beyond |y| = 1 - eta bounded by exp(-2 (1 - eta)^2/(eta (2 - eta))); mu(v) = 1 + (2/9) int_(1/2)^v env^2"""

    def __init__(self, eta=Fr(1, 10 ** 4)):
        y, t = sp.Symbol('y'), sp.Symbol('t')
        beta = sp.cos(sp.pi * y / 2) ** 12 * sp.exp(-y ** 2 / (1 - y ** 2))
        self.bk = acb_fn([sp.diff(beta, y, k) for k in range(3)], [y])
        hs = (sp.cos(t) ** 4 + sp.sin(t) ** 4) ** sp.Rational(-1, 2)
        self.hk = acb_fn([sp.diff(hs, t, k) for k in range(3)], [t])
        self.eta = flint.arb(eta.numerator) / eta.denominator
        e_ = self.eta
        self.tail = 2 * e_ * (-2 * (1 - e_) ** 2 / (e_ * (2 - e_))).exp()      # >= int of beta^2 over both tails
        ib = self.beta2_int(-1 + e_, 1 - e_)
        ib = flint.arb(ib.mid(), ib.rad() + self.tail)
        self.c = ((flint.arb(105) / 128) / (flint.arb(3) / 2 * ib)).sqrt()

    @staticmethod
    def b2(z, analytic):
        return (flint.acb.pi() * z / 2).cos() ** 24 * (-2 * z * z / (1 - z * z)).exp()

    def beta2_int(self, a_, b_):
        val = flint.acb.integral(self.b2, flint.acb(a_), flint.acb(b_), rel_tol=flint.arb(2) ** -90)
        return val.real

    def E(self, v):
        """[E, E', E''](v) for a real ball v inside (1/2, 7/2)"""
        y = (2 * v - 4) / 3
        b = self.bk(flint.acb(y))
        return [self.c * b[k].real * (flint.arb(2) / 3) ** k for k in range(3)]

    def mu(self, v):
        """mu over the ball v: it is increasing, so mu([lo, hi]) lies in [mu(lo), mu(hi)]"""
        out = []
        for end in (v.lower(), v.upper()):
            y = (2 * end - 4) / 3
            it = self.beta2_int(-1 + self.eta, y)
            it = flint.arb(it.mid(), it.rad() + self.tail)
            out.append(1 + flint.arb(2) / 9 * self.c ** 2 * flint.arb(3) / 2 * it)
        lo, hi = out[0].lower(), out[1].upper()
        return flint.arb((lo + hi) / 2, (hi - lo) / 2)

    def H(self, th):
        h = self.hk(flint.acb(th))
        return [q.real for q in h]


def cheb2(U, Sv):
    """the 2D Chebyshev coefficients of the interpolant through the nodal values (y = 1 - 2 xi Lobatto, x Gauss)"""
    yg = np.cos(np.pi * np.arange(Sv.Nr) / (Sv.Nr - 1))
    Vr = np.polynomial.chebyshev.chebvander(yg, Sv.Nr - 1)
    Vx = np.polynomial.chebyshev.chebvander(Sv.x, Sv.Nx - 1)
    return np.linalg.solve(Vr, np.linalg.solve(Vx, U.T).T)


def tvec(z, n):
    """T_k(z), T_k'(z), T_k''(z), k < n, by the differentiated three-term recurrence (exact in Arb)"""
    T, T1, T2 = [flint.arb(1), z], [flint.arb(0), flint.arb(1)], [flint.arb(0), flint.arb(0)]
    for k in range(1, n - 1):
        T.append(2 * z * T[k] - T[k - 1])
        T1.append(2 * T[k] + 2 * z * T1[k] - T1[k - 1])
        T2.append(4 * T1[k] + 2 * z * T2[k] - T2[k - 1])
    return T[:n], T1[:n], T2[:n]


def ev2(C, ty, tx):
    """sum_kl C_kl A_k B_l for A in ty, B in tx (floats exact as binary numbers)"""
    tot = flint.arb(0)
    for k in range(C.shape[0]):
        row = flint.arb(0)
        for l_ in range(C.shape[1]):
            if C[k, l_] != 0.0:
                row += float(C[k, l_]) * tx[l_]
        tot += ty[k] * row
    return tot


def arb_residual(Sv, tau, st, X0, coef, aenv, y0, x0, dy=0.0, dx=0.0):
    """the tau-tau (vv) residual alpha X_interp + beta of the interpolant, in Arb, at the ball (y0 +- dy, x0 +- dx)"""
    m, pi, psi, phi, G = st
    yb, xb = flint.arb(y0, dy), flint.arb(x0, dx)
    rho_in = float(Sv.raysol.sol(tau)[0])
    L = Sv.vout - tau - rho_in
    xi = (1 - yb) / 2
    r = rho_in + L * xi
    v = tau + r
    dr_ = -2 / flint.arb(L)                                       # d/dr = (-2/L) d/dy
    Ty, Ty1, _ = tvec(yb, Sv.Nr)
    Tx, Tx1, Tx2 = tvec(xb, Sv.Nx)
    s2 = (1 - xb * xb).sqrt()
    S2, C2 = (1 - xb) / 2, (1 + xb) / 2
    one = (flint.arb(1), flint.arb(0), flint.arb(0))
    fs = (s2, 2 * xb, -4 * s2)
    fS2, fS4 = (S2, s2, 2 * xb), (S2 ** 2, 2 * S2 * s2, 2 * s2 ** 2 + 4 * xb * S2)
    fC2, fC4 = (C2, -s2, -2 * xb), (C2 ** 2, -2 * C2 * s2, 2 * s2 ** 2 - 4 * xb * C2)
    neg = lambda f: tuple(-q for q in f)                         # noqa: E731
    FT = {'vv': [(0, one)], 'vr': [(1, one)], 'rr': [(2, one)], 'vt': [(3, fs)], 'rt': [(4, fs)], 'tt': [(5, one)],
          'p1': [(5, fC2), (7, neg(fC4))], 'p2': [(5, fS2), (6, neg(fS4))]}

    def jets(U, want):
        Cf = cheb2(U, Sv)
        out = {}
        if 'v' in want:
            out['v'] = ev2(Cf, Ty, Tx)
        if 'x' in want:
            out['x'] = ev2(Cf, Ty, Tx1)
        if 'xx' in want:
            out['xx'] = ev2(Cf, Ty, Tx2)
        if 'r' in want:
            out['r'] = dr_ * ev2(Cf, Ty1, Tx)
        if 'rx' in want:
            out['rx'] = dr_ * ev2(Cf, Ty1, Tx1)
        return out
    Mj = [jets(u, ('v', 'x', 'xx')) for u in m]
    Pj = [jets(u, ('v', 'x', 'r', 'rx')) for u in pi]
    Qj = [jets(u, ('v', 'x', 'r', 'rx')) for u in psi]
    Fj = jets(phi, ('v', 'r'))
    Gj = [(jets(np.real(u), ('v',))['v'], jets(np.imag(u), ('v',))['v']) for u in G]
    X = jets(X0, ('v',))['v']

    def pj(flist, W, d='v', dx_='x', dxx='xx'):
        val, d1, d2 = flint.arb(0), flint.arb(0), flint.arb(0)
        for idx, (F, Fp, Fpp) in flist:
            w = W[idx][d]
            wx = W[idx][dx_] if dx_ in W[idx] else flint.arb(0)
            wxx = W[idx][dxx] if dxx in W[idx] else flint.arb(0)
            wt = -2 * s2 * wx
            wtt = -4 * xb * wx + 4 * (1 - xb * xb) * wxx
            val, d1, d2 = val + F * w, d1 + Fp * w + F * wt, d2 + Fpp * w + 2 * Fp * wt + F * wtt
        return val, d1, d2
    J = {}
    for nm in ME.NM:
        fl = FT[nm]
        val, ut, utt = pj(fl, Mj)
        ur, urt, _ = pj(fl, Qj)
        urr, _, _ = pj(fl, Qj, d='r', dx_='rx', dxx='-')
        pv, pt, _ = pj(fl, Pj)
        pr, _, _ = pj(fl, Pj, d='r', dx_='rx', dxx='-')
        J[nm] = dict(val=val, ur=ur, ut=ut, urr=urr, urt=urt, utt=utt, pv=pv, pr=pr, pt=pt)
    PH = {(1, 0, 0): Fj['r'] - J['rr']['val'] / 2}
    Greg = {4: Gj[0], 5: Gj[1], 7: Gj[2], 6: Gj[3]}
    Gv = {}
    for nm in ME.GC:
        re_ = sum((F[0] * Greg[i][0] for i, F in FT[nm]), flint.arb(0))
        im_ = sum((F[0] * Greg[i][1] for i, F in FT[nm]), flint.arb(0))
        Gv[nm] = flint.acb(re_, im_)
    E = aenv.E(v)
    th = xb.acos() / 2
    Hv = aenv.H(th)
    mu = aenv.mu(v)
    args = [flint.acb(q) for q in (v, r, th, E[0], E[1], E[2], mu, flint.arb(2) / 9 * E[0] ** 2,
                                   flint.arb(4) / 9 * E[0] * E[1], Hv[0], Hv[1], Hv[2])]
    ks, f = coef
    vals = f(*args)
    KN = {(0, 0, 0): 'val', (1, 0, 0): 'pv', (0, 0, 1): 'ut', (1, 0, 1): 'pt', (0, 0, 2): 'utt'}

    def known(nm, jet):
        j = J[nm]
        if jet in KN:
            return j[KN[jet]]
        return {(0, 1, 0): j['ur'] - j['pv'], (0, 1, 1): j['urt'] - j['pt'], (1, 1, 0): j['pr'],
                (0, 2, 0): j['urr'] - 2 * j['pr'], (2, 0, 0): flint.arb(0)}[jet]
    alpha, beta = flint.acb(0), vals[-1]
    for (fname, jet), cval in zip(ks, vals[:-1]):
        if fname.startswith('m_'):
            nm = fname[2:]
            beta += cval * flint.acb(known(nm, jet))
            if nm == 'vv' and jet in ((2, 0, 0), (0, 2, 0), (1, 1, 0)):
                alpha += cval if jet != (1, 1, 0) else -cval
        elif fname == 'phi':
            beta += cval * flint.acb(PH[jet])
        elif fname[:4] in ('Gp1_', 'Gm1_'):
            nm = fname[4:]
            if nm != 'rr':
                beta += cval * (Gv[nm] if fname[:4] == 'Gp1_' else Gv[nm].conjugate())
    return alpha * flint.acb(X) + beta


def run_with_samples(funcs, env, fode, Nr, Nx, cfl, targets, keep_at=None):
    Sv = ME.Solver(Nr, Nx, funcs, env)
    st = ME.cauchy_data(Sv, fode)
    steps, t = [], ME.TAU0
    while t < ME.TAU_STAR - 1e-14:
        _, Lt, _ = Sv.grid(t)
        h = min(cfl * Lt / Nr ** 2, ME.TAU_STAR - t)
        steps.append(h)
        t += h
    tau, out, ti, kept = ME.TAU0, [], 0, None
    Sf = ME.Solver(2 * Nr, 2 * Nx, funcs, env)
    out.append((tau, residual_norm(Sv, Sf, tau, st)))
    with np.errstate(all='ignore'):
        for i, h in enumerate(steps):
            k1 = Sv.rhs(tau, st)
            k2 = Sv.rhs(tau + h / 2, ME.axpy(st, k1, h / 2))
            k3 = Sv.rhs(tau + h / 2, ME.axpy(st, k2, h / 2))
            k4 = Sv.rhs(tau + h, ME.axpy(st, k3, h))
            comb = tuple([(p + 2 * q + 2 * s_ + w) / 6 for p, q, s_, w in zip(a, b, c, d)] if isinstance(a, list)
                         else (a + 2 * b + 2 * c + d) / 6 for a, b, c, d in zip(k1, k2, k3, k4))
            st = ME.axpy(st, comb, h)
            tau += h
            while ti < len(targets) and tau >= targets[ti] - 1e-12:
                out.append((tau, residual_norm(Sv, Sf, tau, st)))
                if keep_at is not None and kept is None and tau >= keep_at - 1e-12:
                    kept = (Sv, tau, st)
                ti += 1
    return out, ME.m22(Sv, st), kept


def check_x4(funcs, env, fode, prof, s_tot):
    targets = list(np.linspace(-1.6, 1.6, 9)) + [1.7, float(ME.TAU_STAR) - 1e-9]
    s_arr, l_arr = np.array([p[0] for p in prof]), np.array([p[1] for p in prof])
    rows = {}
    for cfg in ((32, 12, 1.0), (40, 12, 1.0), (48, 16, 1.0), (64, 20, 1.0)):
        t1 = time.time()
        smp, m22v, kept = run_with_samples(funcs, env, fode, *cfg, targets, keep_at=KEEP if cfg == (48, 16, 1.0)
                                           else None)
        if kept is not None:
            rows['kept'] = kept
        taus = np.array([q[0] for q in smp])
        rn = np.array([q[1] for q in smp])
        # Lambda(tau) = int_tau^tau* k_lo: prof is cumulative from tau* backwards in s = tau* - tau
        lam = np.interp(ME.TAU_STAR - taus, s_arr, l_arr)
        route = float(np.trapezoid(np.exp(lam) * rn, taus))
        rows[cfg] = (taus, rn, lam, route, m22v, time.time() - t1)
        print('    %d x %d: M_22 = %.9f; ||rho_tautau|| at tau = %s: %s; Lambda there %s; the route\'s bound int '
              'e^Lambda ||rho|| ds = %.3e (%.0fs) %s'
              % (cfg[0], cfg[1], m22v, ', '.join('%.2f' % t for t in taus), ', '.join('%.1e' % x for x in rn),
                 ', '.join('%.1f' % x for x in lam), route, time.time() - t1, el()))
    return rows


# ------------------------------------------------------------------------------------------------------------------
def check_x6(res, kept, need_pt):
    Sv, tau, st = kept
    aenv = ArbEnv()
    d = res[('vv', 0)]
    ks = list(d['coef'].keys())
    coef = (ks, acb_fn([d['coef'][k].subs(ME.A, 1) for k in ks] + [d['src'].subs(ME.A, 1)], ME.SYMS))
    X0 = xreg(Sv, tau, st)
    yg = np.cos(np.pi * np.arange(Sv.Nr) / (Sv.Nr - 1))
    i0 = int(np.argmin(np.abs(yg + 0.3)))                     # v near 2 at this tau, where the solution is large
    pts = [(i0, j) for j in (1, 3, 5)]
    nodes, mids = [], []
    t1 = time.time()
    for i, j in pts:
        nodes.append(abs(arb_residual(Sv, tau, st, X0, coef, aenv, yg[i], Sv.x[j]).real.mid()))
        rm = arb_residual(Sv, tau, st, X0, coef, aenv, (yg[i] + yg[i + 1]) / 2, (Sv.x[j] + Sv.x[j + 1]) / 2)
        mids.append(rm.real)
    per = (time.time() - t1) / (2 * len(pts))
    ok_nodes = max(float(q) for q in nodes) < 1e-12
    real = sum(1 for q in mids if abs(float(q.mid())) > 1e3 * max(float(n) for n in nodes)
               and abs(float(q.mid())) > 1e6 * float(q.rad()))
    OK['X6'] = ok_nodes and real >= 2
    print('  X6 (certified, Arb): the tau-tau defect of the lifted 48 x 16 state at tau = %.3f, in Arb balls with mu '
          'by certified quadrature and c from its defining integral (%s): at three collocation nodes it is at most %.1e '
          '(the evaluator reproduces the solver there), at the three midpoints next to them %s; certified nonzero '
          'values where the solution is large: %s %s'
          % (tau, '%.15f +/- %.1e' % (float(aenv.c.mid()), float(aenv.c.rad())), max(float(n) for n in nodes),
             ', '.join('%.4e +/- %.1e' % (float(q.mid()), float(q.rad())) for q in mids), OK['X6'], el()))
    X0p = X0 + 1e-6 * np.max(np.abs(X0))
    bad = abs(arb_residual(Sv, tau, st, X0p, coef, aenv, yg[i0], Sv.x[1]).real.mid())
    OK['C4'] = not float(bad) < 1e-12
    print('  C4 (control): the interpolated d_tau^2 m_vv raised by 1e-6 of its maximum: the nodal residual is %.1e, so '
          'X6\'s nodal test fails: %s' % (float(bad), OK['C4']))
    i, j = pts[0]
    ym, xm = (yg[i] + yg[i + 1]) / 2, (Sv.x[j] + Sv.x[j + 1]) / 2
    rads = []
    for dl in (1e-4, 1e-6, 1e-8, 1e-10):
        rads.append((dl, float(arb_residual(Sv, tau, st, X0, coef, aenv, ym, xm, dl, dl).real.rad())))
    slope = rads[-1][1] / rads[-1][0]
    print('  X6 (sharpness): on a box of half-width delta in (y, x) around the first midpoint the enclosure\'s radius '
          'is %s: it grows as %.2f delta (first-order wrapping of the Chebyshev recurrences and coefficient functions), '
          'while the residual there is %.1e. One evaluation takes %.3f s.' % (
              ', '.join('%.1e at %.0e' % (r_, d_) for d_, r_ in rads), slope, abs(float(mids[0].mid())), per))
    nstep, t = 0, ME.TAU0
    while t < ME.TAU_STAR - 1e-14:
        t += min(Sv.grid(t)[1] / Sv.Nr ** 2, ME.TAU_STAR - t)
        nstep += 1
    for target in (need_pt, 1e-6):
        dl = target / slope
        boxes = (1 / dl) ** 2
        print('    radius <= %.0e needs delta <= %.1e: about %.1e boxes per slice, %.1e over the run\'s ~%d slices, '
              'about %.1e s at this rate' % (target, dl, boxes, boxes * nstep, nstep, boxes * nstep * per))
    return slope, per


def check_x7():
    """the T-entries of the tau-tau row (X1) at X* and their sup over the domain, in Arb"""
    c_lo, c_hi = flint.arb('1.32407110621'), flint.arb('1.3241034918')        # envelope5.out E1 (READ)
    c = flint.arb((c_lo + c_hi) / 2, (c_hi - c_lo) / 2)
    q0 = (flint.arb(9) / 1250) ** (flint.arb(1) / 8)
    a = q0 / 2
    mu, mup = flint.arb(419) / 384, flint.arb(2) / 9 * c ** 2
    er = (5 * mu / 2 - mup * a) / a ** 3
    et = (mup * a - mu / 2) / a ** 3
    z = (2 * mu ** 3 - mu ** 2 * a ** 2 + mu * mup * a ** 3 - mup * a ** 5) / a ** 8
    mue = arb(MU_END)
    er_sup = (5 * mue / 2) / a ** 3
    et_sup = (mue / 2 + flint.arb(2) / 9 * c ** 2 * a) / a ** 3
    z_sup = (2 * mue ** 3 + mue ** 2 * a ** 2 + mue * flint.arb(2) / 9 * c ** 2 * a ** 3
             + flint.arb(2) / 9 * c ** 2 * a ** 5) / a ** 8
    OK['X7'] = flint.arb(133) < er < flint.arb(134) and er < er_sup
    print('  X7 (certified, Arb): at X* (r = a, mu(2) = 419/384 by the envelope\'s symmetry about v = 2, mu\' = (2/9) '
          'c^2) the T-entries of the tau-tau row are e_r: %s, e_tau: %s, zero order: %s; over r in [a, 5], mu in [1, '
          'mu_end], mu\' in [0, (2/9) c^2] each is at most %s, %s, %s in modulus (bounds by the moduli of their terms, '
          'each decreasing in r, taken at r = a with mu = mu_end). The other entries of the row and the other rows are '
          'not computed: %s'
          % (er.str(6), et.str(6), z.str(6), er_sup.upper().str(6), et_sup.upper().str(6), z_sup.upper().str(6),
             OK['X7']))


def check_x8(funcs, env, fode, lam, lam_o, cpt):
    """the data requirement against the first omitted mode, P_15"""
    req = 2.207738 / (cpt * math.exp(lam))
    Sv = ME.Solver(48, 32, funcs, env)
    r1, L, _ = Sv.grid(ME.TAU0)
    wr = cc_weights(Sv.Nr) / 2 * L
    wx = np.pi / Sv.Nx * np.sqrt(1 - Sv.x ** 2)
    rr = r1[:, None] * np.ones((1, Sv.Nx))
    keep = ME.KS
    out = {}
    try:
        for ks in ((1, 3, 5, 7, 9, 11, 13), (15,)):
            ME.KS = ks
            T = ME.cauchy_data(Sv, fode)[1][0]                    # d_tau m_vv on Sigma (step (ii))
            out[ks] = math.sqrt(0.196683 * math.pi ** 2 * float(np.einsum('i,j,ij->', wr, wx, T ** 2 * rr ** 3)))
    finally:
        ME.KS = keep
    e13, e15 = out[(1, 3, 5, 7, 9, 11, 13)], out[(15,)]
    s15, s1 = float(ME.L5.sigma_k(15)), float(ME.L5.sigma_k(1))
    OK['X8'] = e15 > req
    print('  X8 (the data requirement): Corollary 2 carries the data error with the full factor, so m_lo > 0 needs '
          'E^(1/2)(tau0) < |M_22|/(C_pt e^%.4f) = %.2e (deduced from X3 and the requirement). The data are cut at P_13; '
          'the first omitted mode, P_15 (|sigma_15/sigma_1| = %.1e), alone gives the data error an E^(1/2) of at least '
          'q_lo^(1/2) ||d_tau T_15|| = %.2e (computed, floating point, on 48 x 32; the kept modes give %.2e), %.1e '
          'times the requirement, on every grid: %s' % (lam, req, abs(s15 / s1), e15, e13, e15 / req, OK['X8']))
    req_o = 2.207738 / (cpt * math.exp(lam_o))
    OK['C5'] = not e15 > req_o
    print('  C5 (control): the requirement with C3\'s factor e^%.4f in place of X3\'s: %.2e, above the P_15 '
          'contribution, so X8\'s test fails: %s' % (lam_o, req_o, OK['C5']))


def main():
    print('m22cert5: the attempt at a certified lower bound m_lo on |M_22| (M22CERT5.md)')
    flint.ctx.prec = 120
    with contextlib.redirect_stdout(io.StringIO()):
        out, unk = ME.ric_h()
        res = ME.extract(out, unk)
    check_x1(res)
    pieces, s_tot = check_x2()
    lam, prof, inside = check_x3(pieces)
    lam_o, _, _ = check_x3(pieces, outer=True)
    a1 = arb(A_HI)
    vol = (flint.arb.pi() ** 2 / 2 * ((1 + a1) ** 4 - a1 ** 4)).upper()
    volm = (flint.arb(vol) + flint.arb.pi() ** 2 * arb(MU_END) * ((1 + a1) ** 2 - a1 ** 2)).upper()
    cpt = 1 / math.sqrt(float(volm)) * (1 - 1e-12)
    need = 2.207738 / (cpt / math.sqrt(2))
    fac = math.exp(float(lam))
    OK['X3'] = inside and fac > 1e12
    print('  X3 (certified, Arb): every evaluation point lies in its slice: %s; int_(tau0)^(tau*) k dtau >= %.4f, so '
          'the estimate\'s Gronwall factor for E^(1/2) from tau0 is >= e^%.4f = %.3e (from X1\'s e_r entry alone; the '
          'other rows, the zero-order terms, the couplings, the transports and the commuted energies only add); half '
          'of the exponent is gathered after tau = %.2f: %s %s'
          % (inside, float(lam), float(lam), fac,
             float(ME.TAU_STAR) - next(s_ for s_, l_ in prof if l_ >= float(lam) / 2), OK['X3'], el()))
    OK['C3'] = not math.exp(float(lam_o)) > 1e12
    print('  C3 (control): the same bound evaluated at the outer boundary r = 3 - tau: e^%.4f = %.3e: X3\'s threshold '
          'fails: %s' % (float(lam_o), math.exp(float(lam_o)), OK['C3']))
    print('  The requirement (deduced from X3): the route\'s point-evaluation constant, |e(X*)| <= C_pt E_s(tau*)^(1/2) '
          'with E_s containing int (1 + m) |e|^2 (the zero-order current), is >= (int over the tau* slice of (1 + '
          'm))^(-1/2) '
          '>= %.4f (the constant field; vol = %.3f, with m: %.3f); the forcing enters with c_Y/2 = 2^(-1/2); so the '
          'route certifies m_lo > 0 only if int_(tau0)^(tau*) e^(Lambda(s)) ||rho(s)|| ds < |M_22| 2^(1/2)/C_pt <= '
          '%.2f, '
          'Lambda(s) the exponent gathered from s to tau* (>= X3\'s profile), rho the residual (every component; its '
          'tau-tau part is a lower bound)' % (cpt, float(vol), float(volm), need))
    funcs, env = ME.load_system(res), ME.envelope()
    with contextlib.redirect_stdout(io.StringIO()):
        fode = ME.mode_setup()
    rows = check_x4(funcs, env, fode, prof, s_tot)
    lam_keep = float(np.interp(ME.TAU_STAR - KEEP, [p[0] for p in prof], [p[1] for p in prof]))
    check_x6(res, rows['kept'], need / (ME.TAU_STAR - ME.TAU0) / math.exp(lam_keep))
    b48, b64 = rows[(48, 16, 1.0)][3], rows[(64, 20, 1.0)][3]
    OK['X4'] = all(np.isfinite(rows[c][3]) for c in rows if c != 'kept') and b64 < b48 and b64 > need
    print('  X4 (computed, floating point; an indicator): with the tau-tau defect of the lifted semi-discrete state in '
          'place of rho (not the residual of one space-time interpolant), int e^Lambda ||rho|| ds is %.2e at 32 x 12, '
          '%.2e at 40 x 12, '
          '%.2e at 48 x 16 and %.2e at 64 x 20, against the %.2f it must stay below: still a factor %.1e above it at '
          'the finest grid, though falling: %s' % (rows[(32, 12, 1.0)][3], rows[(40, 12, 1.0)][3], b48, b64, need,
                                                  b64 / need, OK['X4']))
    step = b48 / b64
    k = math.log(b64 / need) / math.log(step)
    kk = math.ceil(k)
    Nr, Nx = 64 + 16 * kk, 20 + 4 * kk
    t64 = rows[(64, 20, 1.0)][5]
    cost = t64 * (Nr / 64) ** 2 * (Nr * Nx * (Nr + Nx)) / (64 * 20 * 84)
    print('  Resolution and cost (extrapolated from the last two grids, floating point): one step (+16 in r, +4 in x) '
          'divides the bound by %.1f, so it would fall below %.2f after %.1f more steps, at about %d x %d; the run with '
          'its defect took %.0f s at 64 x 20, and scales as Nr^3 Nx (Nr + Nx), so about %.0f s there. An indicator '
          'only, and not the whole condition: X8\'s data requirement fails at the data\'s own truncation'
          % (step, need, k, Nr, Nx, t64, cost))
    m1, mh = ME.lam_of(1.0), ME.lam_of(0.5)
    OK['X5'] = m1[0] < 0.0024433 and mh[0] < 0.0024433
    print('  X5 (computed): a certified m_lo would give lambda0 < %s at m_lo = 1 and %s at m_lo = 1/2 (operator norm, '
          'Frobenius, largest entry), against the certified 0.0024433, 0.0019079, 0.0012228, which stand: %s'
          % (', '.join('%.7f' % x for x in m1), ', '.join('%.7f' % x for x in mh), OK['X5']))
    check_x7()
    check_x8(funcs, env, fode, float(lam), float(lam_o), cpt)
    for k, val in OK.items():
        builtins.print(k, 'PASS' if val else 'FAIL')
    builtins.print('m22cert5: %d/%d %s' % (sum(OK.values()), len(OK), el()))
    return 0 if all(OK.values()) else 1


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] not in ('--selftest',):
        builtins.print('usage: python3 checks/m22cert5.py [--selftest]   (both run every check)')
        sys.exit(2)
    sys.exit(main())
