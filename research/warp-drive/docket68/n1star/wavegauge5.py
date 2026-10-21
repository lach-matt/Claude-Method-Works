#!/usr/bin/env python3
"""wavegauge5.py -- the passage from the Regge-Wheeler-type gauge to the harmonic (wave) gauge on five-dimensional
Tangherlini, in the T^2-mirror class (N1STAR-PROOF.md section 10.4, Proposition 10.2; D42).  Labels: computed (exact,
sympy), deduced, READ.  The template is Hung's four-dimensional even part (P.-K. Hung, arXiv:1909.06733): the harmonic
gauge Gamma_b[h] := nabla^a (h_ab - (1/2) tr h g_ab) = 0, the gauge vector from the Regge-Wheeler gauge solving the
tensorial wave equation with the master quantity as source, and the l = 0 sector's two non-decaying solutions, the
stationary one-form W* and the gauge-fixed mass change K*.  Everything here is the five-dimensional counterpart,
computed on g = -f dt^2 + dr^2/f + r^2 (dth^2 + cos^2 th dphi1^2 + sin^2 th dphi2^2), f = 1 - mu/r^2.

  W1 (computed) The linearised Ricci tensor is dRic_ab = -(1/2)(box h_ab + 2 R_a^c_b^d h_cd) + (1/2)(nabla_a Gamma_b
     + nabla_b Gamma_a) -- checked on a tensor of the class (the eight components T^2 and both reflections allow, with
     explicit polynomial-trigonometric coefficients; the residual, which simplify() does not reduce, is evaluated at
     three rational points to forty digits and is below 1e-30; the general-function form takes an hour) -- so under
     Gamma[h] = 0 the linearised vacuum equation is the Lichnerowicz wave equation (Hung's (1.4)).  And for a one-form
     X of the class with general coefficients, Gamma[pi_X] = box X on the Ricci-flat background (pi_X := nabla_a X_b +
     nabla_b X_a), so a gauge vector carrying h to harmonic gauge solves box X = -Gamma[h].  Control: the identity
     fails with the curvature term's sign reversed.  The one-form identity is linear in the derivatives of X, and
     every coefficient is evaluated at the same points.
  W2 (computed, exact) The l = 0 stationary one-form: box W = 0 for W = W0(r) dt + W1(r) dr has W0 = a + b/r^2 and
     W1 = c/(r^3 f) + d r^3/(r^2 - mu); in ingoing coordinates (v = t + int dr/f) the combination regular at the horizon
     with finite energy is
         W* = dt/r^2 + sqrt(mu) dr/(r^3 f) = dv/r^2 - dr/(r (r + sqrt mu)),
     Hung's (8.1) in five dimensions.  Control: dt/r^2 alone is singular at the horizon in the ingoing chart.
  W3 (computed, exact) The gauge-fixed mass change.  K := d g/d mu has Gamma[K] = dr/(r^3 f) (the singular stationary
     solution), and K* := K + pi_{W**} with W** = t W* + A(r) dt + B(r) dr,
         A = (1/(2 sqrt mu)) (log f + mu/r^2),
         B = (3 mu^2 log(r^2 - mu) + 2 mu^2 + 3 mu r^2 - 2 r^4 log r + r^4 log(r^2 - mu)) / (8 mu r (r^2 - mu)),
     satisfies Gamma[K*] = 0 and K* = t pi_{W*} + (a stationary tensor): the mass change in harmonic gauge grows
     linearly in t, as Hung's (8.39).  Control: W** without its t W* term leaves Gamma[K + pi] != 0.
  W4 (computed, exact) The scalar modes.  For a T^2-invariant harmonic S(th) (S'' + (cot th - tan th) S' + k^2 S = 0,
     k^2 = l(l + 2)) and h_RW = F_ab S dx^a dx^b + 2 r^2 F S gamma_ij dz^i dz^j (the Regge-Wheeler-type gauge of
     Proposition 10.1), the scalar-type one-form X = X_t S dt + X_r S dr + X_L r S_i dz^i (S_i = -k^-1 D_i S) has
     box X + Gamma[h_RW] proportional to S (t, r components) and to S_i (angular), so box X = -Gamma[h_RW] is three
     1+1 equations for (X_t, X_r, X_L) with coefficients in (r, mu, k) alone: wave operators -f^-1 d_t^2 + f d_r^2 + ...
     coupled at first order, with sources linear in F, F_ab and their first derivatives.  Checked at l = 2 (S = cos 2th)
     and l = 4 (S = 3 cos^2 2th - 1), coefficient by coefficient at rational points: every coefficient is th-free,
     the principal part is the stated one, and the phi components carry no equation.  Control: a one-form with a
     vector-type angular part is not of this form (its angular equation has the wrong principal part and leaves a
     phi component).
  W5 (computed, exact) The tensor type is already in harmonic gauge: for h_ij = 2 r^2 H(t, r) T_ij(th) with T
     traceless and divergence-free on S^3 (the mirror-even T^2-invariant form T = diag(a, cos^2 th b, sin^2 th c),
     a + b + c = 0, D^i T_ij = 0), Gamma[h] = 0 identically.  Control: without the divergence condition it does not.
  W6 (computed, exact) The gauge-vector system is triangular.  With S := div X, F := dX, P := F_tr/S_l, Q_t := -F_{t
     th}/S_l' and Q_r := -F_{r th}/S_l' (S_l the harmonic) and box_l := -f^-1 d_t^2 + f d_r^2 + ((3r^2 - mu)/r^3) d_r -
     k^2/r^2 the scalar wave operator at mode l, seven identities hold in X, exactly (W6; at l = 2 in the selftest, at l
     = 4 under --l4, where all seven pass and the control fails, in 72 minutes): div(box X) = box_l(div
     X); (box X)_t = box_l X_t + (2 mu/r^3) P; (box X)_r = d_r S - f^-1 d_t P - (k^2/r^2) Q_r; r (box X)_L = box_l(r
     X_L) - (2 k f/r) Q_r; (box X)_t = d_t S - (f/r^3) d_r(r^3 P) - (k^2/r^2) Q_t; d(box X)_tr = box_l P - ((3 r^2 - 9
     mu)/r^4) P - (2 k^2/r^3) Q_t; and, the last two combined, box_l(r P) + (4 mu/r^4) r P = r d(box X)_tr + 2 (d_t S -
     (box X)_t). So for box X = J the system is triangular: S solves the free scalar wave equation with source div J; r
     P solves the scalar wave equation with the potential -4 mu/r^4 and a source in S and J (the Maxwell master equation
     of [KI03b] (5.20) at n = 3, A = -r^3 P/k^2, in another normalisation); X_t solves box_l X_t = J_t - (2 mu/r^3) P
     with no potential; r X_L solves the scalar wave equation with source (2 k f/r) Q_r + r J_L, Q_r = (r^2/k^2)(d_r S -
     f^-1 d_t P - J_r) algebraic in the rungs below; and X_r = Q_r - d_r(r X_L)/k is algebraic. Hung's condition (A.3),
     k^2/r^2 + V >= 0, holds on every rung: V = 0 for S, X_t and r X_L, and V = -4 mu/r^4 for r P gives k^2/r^2 - 4
     mu/r^4 >= 0 for r^2 >= 4 mu/k^2, true on the exterior for k^2 >= 8 (equality would need r^2 = mu/2). The
     counterpart of [Hun19] (4.21) carries no potential where four dimensions has 2M/r^3.  Control: the sign of the term
     2 mu/r^3 (and of 4 mu/r^4) reversed.
  W7 (computed, exact) Hung's Proposition 4.2 in five dimensions.  In his components -- H1 = (h_tt + f^2 h_rr)/2 + ((1 -
     f)/2) trs h, H2 = trs h/sqrt3, H3 = (h_tt/f - f h_rr)/2, H6 = f h_tr + ((1 - f)/2) trs h, H4 = f k h_rth/(r S'), H7
     = k h_tth/(r S'), hhat_ij = 2 r^2 H5 S_ij; (1 - f)/2 = mu/(2 r^2) is his M/r -- with the gauge condition Gamma[h] =
     0 admixed as 2 f f' Gamma_r in rows 1 and 6 and k f' Gamma_th/r in rows 4 and 7 (his Appendix C), the Lichnerowicz
     equation is boxhat H = A H + U H, boxhat := -f^-1 d_t^2 + f d_r^2 + ((3 r^2 - mu)/r^3) d_r the wave operator of the
     quotient (W6's box_l without its -k^2/r^2, so A carries the angular eigenvalues K/r^2 of W8(f) on its diagonal), A
     zeroth order and rational in r, mu, k, and U = (2f'/f) nabla_L (H6 - H1) in row 6, (f'/f) nabla_L (H7 - H4) in row 7
     and nothing else (his U with 2M/r^2 -> f').  r^2 A_main at k^2 = l(l+2) has the eigenvalues (l+a)(l+a+2), a = -2,
     -1, 0, 0, 0, 1, 2 (his Lemma 4.3 with (l+a)(l+a+1)): semi-positive for l >= 2; A - A_main/r^2 = O(mu/r^4).  In the
     regular variables H6' = (H6 - H1)/f^2 = -h(L', L')/2, H7' = (H7 - H4)/f every coefficient is regular at the horizon,
     rows 1-5 carry no first-order term, rows 6', 7' carry 2f' nabla_L' H6' and f' nabla_L' H7' and no nabla_L (his
     4M/r^2, 2M/r^2).  At l = 0 (H1, H2, H3, H6) the eigenvalues are 0, 0, 3, 8.  The harmonic is kept symbolic with its
     equation S'' = -2 cot 2th S' - k^2 S applied and the angle evaluated exactly at (cos, sin) = (3/5, 4/5) and (5/13,
     12/13); every coefficient is a rational function, cancelled.  Control: the sign of the gauge admixture reversed
     (first-order terms survive in rows 1-5).  hung4.py is the four-dimensional control: the same instrument on
     Schwarzschild reproduces his printed rows.
  W8 (computed, exact; the three divergence identities formally, on two components with the matrices symbolic) The
     identities of Hung's Proposition 4.1 in five dimensions (N1STAR-PROOF.md 10.5, Proposition 10.3).  (a) The radiation
     field Psi = r^(3/2) H: r^(3/2) boxhat(r^-3/2 Psi) = -f^-1 d_u d_v Psi - V0 Psi, V0 = (3/4 + 9 mu/(4 r^2))/r^2
     ([Sch13] (5.11)-(5.12) at n = 4), so the W7 system reads d_u d_v Psi = -f (Ahat + V0) Psi - f Uhat Psi in the
     rescaling Hhat = diag(sqrt2, 1, sqrt2, sqrt2, 2 n_S, sqrt2, sqrt2) H, n_S = sqrt(2 (k^2 - 3)/(3 k^2)); V_inf := lim
     r^2 (Ahat + V0) is symmetric with the eigenvalues (l+a+1/2)(l+a+3/2), a = -2, -1, 0, 0, 0, 1, 2: at least 3/4 at
     every l >= 2 (Hung's zero eigenvalue at l = 2 is lifted, and no Hardy inequality is needed) and at least (3/32)
     l(l+2); V - V_inf/r^2 = O(mu/r^4).  (b) Uhat Psi = (2f'/f) nabla_L (Psi6 - Psi1) - (3f'/r)(Psi6 - Psi1) in row 6,
     (f'/f) nabla_L (Psi7 - Psi4) - (3f'/(2r))(Psi7 - Psi4) in row 7, nothing else.  (c) The p-current J^p = r^(p-3) f^-1
     (T_ab[Psi] L^b - Psi . V_inf . Psi L_a/(2 r^2)): div J^p = r^(p-4) f^-2 (p f/2 - mu/r^2) |nabla_L Psi|^2 + (2 - p)/2
     r^(p-6) Psi . V_inf . Psi + r^(p-3) f^-1 nabla_L Psi . ((V - V_inf/r^2) Psi + Uhat Psi), J^p . L-bar = r^(p-5) Psi .
     V_inf . Psi >= 0, J^p . L = r^(p-3) f^-1 |nabla_L Psi|^2 (Hung's (4.5)).  (d) The red-shift divergence at r = r_h
     for Y = (sigma/2)(r - r_h) T + (2 + sigma (r - r_h)) L': (sigma/2)|Q_v|^2 + (2/r_h)|Q_R|^2 + (6/r_h) Q_R . Q_v +
     (sigma/2 + 1/r_h)|nabla-slash Q|^2 + c (sigma/mu + 2/mu^(3/2))|Q|^2 + (2c/mu) Q . Q_R + nabla_Y Q . (Acal Q - c
     Q/r^2) + 2 Q_R . beta Q_R (Hung's (2.13) with 2M -> r_h; the beta term, 2f' and f' in the system, has his sign).
     (e) The T-current with the r^-delta weight: div(r^-delta (T_ab - Q . V_inf . Q g_ab/(2 r^2)) T^b) = (delta/4)
     r^(-1-delta) (|nabla_L-bar Q|^2 - |nabla_L Q|^2) + r^-delta nabla_T Q . ((V - V_inf/r^2) Q + U Q) (Hung's (4.6)).
     (f) On S^3 the rough Laplacian has the eigenvalue -(k^2 - 2) on the one-form S_th dth and -(k^2 - 6) on the
     traceless tensor S_AB: the angular energies K = diag(k^2, k^2, k^2, k^2 - 2, k^2 - 6, k^2, k^2 - 2).  (g) A - K/r^2,
     its regular form A' - K/r^2 and A - A_main/r^2 have entries of degree at most one in k, A' - K/r^2 finite at r_h:
     one angular derivative bounds them.  (h) At l = 0, A0 - A0_main/r^2 = O(mu/r^4) and diag(sqrt2, 1, sqrt2, sqrt2)
     makes A0_main symmetric, so V_inf has the eigenvalues 3/4, 3/4, 15/4, 35/4.  Control: the sign of V0 reversed and
     L-bar for L in J^p (the spectrum and (c) fail).  The seven-component divergences in full were tried and exceeded
     thirty minutes; the formal identities carry the structure with the matrices as symbols, and the bounds on those
     matrices are (a), (b), (g).

READ (alphaXiv, 2026-10-20).  [Hun19] P.-K. Hung, arXiv:1909.06733v1, "The linear stability of the Schwarzschild
spacetime in the harmonic gauge: even part": abstract ("the energy decays at a rate tau^{-2+} for the solution of the
linearized Einstein equation after subtracting its spherically symmetric part ... The spherically symmetric part
converges to a linear combination of two special solutions.  One is the gauge-fixed mass change solution [19].  The
other is the deformation tensor of a stationary one form"); (1.3)-(1.5) pp. 2; Theorems 1.1-1.4 pp. 2-3; section 4.2,
(4.10)-(4.13), (4.21) p. 26-27 (the gauge vector to the Regge-Wheeler gauge and its wave equations with the Zerilli
source); (8.1) p. 58 W* = dt/r + 2M dr/(r^2 f); (8.38)-(8.39) p. 69 W** and K*.  READ 2026-10-21 (alphaXiv) for W7:
section 4.1 pp. 17-25 (Propositions 4.1, 4.2, A, B, U, Lemma 4.3, the red-shift paragraph p. 23 with H6', H7');
Appendix A pp. 70-71 ((A.3)-(A.8)); Appendix C pp. 75-79 ((C.1)-(C.12), (ME1)-(ME7), (HG1)-(HG3), the seven rows).
READ 2026-10-21 (alphaXiv) for W8: [Hun19] section 2 pp. 4-12 ((2.1)-(2.2), (2.6)-(2.8), (2.13)-(2.22)), Lemma 3.2 and
Corollaries 3.3-3.5 pp. 16-17, section 4.1 pp. 18-25 (Proposition 4.1 and (4.1), (4.3), Lemmas 4.3-4.4 with (4.4)-(4.6),
the red-shift paragraph with (4.7)-(4.8), the proof of Proposition 4.1 with (4.9), Remark 4.5), Appendix A pp. 70-72
((A.1)-(A.11)); [Sch13] V. Schlue, Decay of linear waves on higher dimensional Schwarzschild black holes,
arXiv:1012.5963v1, (2.17)-(2.20), Proposition 3.1, (5.8)-(5.17) (the radiation field r^((n-1)/2) psi and its potential).

sympy.  python3 wavegauge5.py [--selftest | --mutants]   (about seven and a half minutes; --l4 adds 72 minutes)
"""
import sys
import time

import sympy as sp

t, r, th, p1, p2 = sp.symbols("t r theta phi1 phi2", real=True)
X = [t, r, th, p1, p2]
mu = sp.symbols("mu", positive=True)
kk = sp.symbols("k", positive=True)
f = 1 - mu/r**2
cs, sn = sp.cos(th), sp.sin(th)
g = sp.diag(-f, 1/f, r**2, r**2*cs**2, r**2*sn**2)
gi = g.inv()
N = 5
Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                         for d in range(N))/2) for c in range(N)] for b in range(N)] for a in range(N)]
_RIEM = {}


def riem(a, b, c, d):
    """R^a_{bcd} = d_c Gam^a_{db} - d_d Gam^a_{cb} + Gam^a_{ce} Gam^e_{db} - Gam^a_{de} Gam^e_{cb}"""
    if (a, b, c, d) not in _RIEM:
        _RIEM[(a, b, c, d)] = sp.simplify(sp.diff(Gam[a][d][b], X[c]) - sp.diff(Gam[a][c][b], X[d])
                                          + sum(Gam[a][c][e]*Gam[e][d][b] - Gam[a][d][e]*Gam[e][c][b] for e in range(N)))
    return _RIEM[(a, b, c, d)]


def riem_low(a, e, b, ff):
    return sp.simplify(sum(g[a, gg]*riem(gg, e, b, ff) for gg in range(N) if g[a, gg] != 0))


def D1(W, c, a):
    """(nabla_c W)_a for a one-form"""
    return sp.diff(W[a], X[c]) - sum(Gam[e][c][a]*W[e] for e in range(N))


def box1(W, simp=True):
    """(box W)_a = g^{cd} nabla_d nabla_c W_a (simplify() is skipped for general functions: on them it can run for an
    hour in trigsimp's factoring, and the checks that use them evaluate coefficients at rational points instead)"""
    S = sp.simplify if simp else (lambda e: e)
    DW = [[D1(W, c, a) for a in range(N)] for c in range(N)]
    out = []
    for a in range(N):
        s = 0
        for c in range(N):
            for d in range(N):
                if gi[c, d] == 0:
                    continue
                s += gi[c, d]*(sp.diff(DW[c][a], X[d]) - sum(Gam[e][d][c]*DW[e][a] + Gam[e][d][a]*DW[c][e]
                                                            for e in range(N)))
        out.append(S(s))
    return out


def pi_of(W, simp=True):
    S = sp.simplify if simp else (lambda e: e)
    return sp.Matrix(N, N, lambda a, b: S(D1(W, a, b) + D1(W, b, a)))


def Dh(h, c, a, b):
    return sp.diff(h[a, b], X[c]) - sum(Gam[e][c][a]*h[e, b] + Gam[e][c][b]*h[a, e] for e in range(N))


def gamma_of(h, simp=True):
    """the harmonic gauge one-form Gamma_b = nabla^a (h_ab - (1/2) tr h g_ab)"""
    S = sp.simplify if simp else (lambda e: e)
    trh = sum(gi[a, b]*h[a, b] for a in range(N) for b in range(N))
    return [S(sum(gi[a, c]*Dh(h, c, a, b) for a in range(N) for c in range(N) if gi[a, c] != 0)
              - sp.diff(trh, X[b])/2) for b in range(N)]


def class_tensor(dep=(t, r, th)):
    names = {(0, 0): "htt", (0, 1): "htr", (1, 1): "hrr", (0, 2): "hta", (1, 2): "hra", (2, 2): "haa", (3, 3): "h11",
             (4, 4): "h22"}
    h = sp.zeros(N)
    for (i, j), nm in names.items():
        h[i, j] = h[j, i] = sp.Function(nm)(*dep)
    return h


class Checklist:
    def __init__(self, verbose, quiet=False):
        self.ok, self.verbose, self.quiet = True, verbose, quiet

    def __call__(self, name, good):
        self.ok &= bool(good)
        if self.verbose or (not good and not self.quiet):
            print("      [%s] %s" % ("ok" if good else "FAIL", name), flush=True)


# ---------------------------------------------------------------------------------------------------------- W1
def sample_tensor():
    """a tensor of the class with explicit coefficients (polynomials in t, r times trigonometric functions of theta):
    the identity is then a rational-trigonometric expression and reduces exactly, where eight general functions take
    an hour"""
    h = sp.zeros(N)
    h[0, 0] = (t*r + r**2)*sp.cos(2*th)
    h[0, 1] = h[1, 0] = (t**2 + r)*sp.sin(th)**2
    h[1, 1] = (r**3 + t)*sp.cos(th)**2
    h[0, 2] = h[2, 0] = t*r**2*sp.sin(2*th)
    h[1, 2] = h[2, 1] = (t + r)*sp.sin(2*th)*sp.cos(2*th)
    h[2, 2] = r**2*(t + 1)*sp.cos(4*th)
    h[3, 3] = r**2*cs**2*(t**2 - r)*(1 + sp.cos(2*th))
    h[4, 4] = r**2*sn**2*(t - r**2)*(1 - 2*sp.cos(2*th))
    return h


SAMPLE_POINTS = [{t: sp.Rational(3, 7), r: sp.Rational(9, 4), th: sp.Rational(5, 11), mu: sp.Rational(2, 3)},
                 {t: sp.Rational(-1, 3), r: sp.Rational(17, 5), th: sp.Rational(7, 9), mu: sp.Rational(5, 4)},
                 {t: sp.Rational(5, 2), r: sp.Rational(13, 3), th: sp.Rational(2, 7), mu: sp.Rational(7, 3)}]


def w1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    h = sample_tensor()
    sign = -1 if control == 1 else 1
    trh = sum(gi[a, b]*h[a, b] for a in range(N) for b in range(N))
    DhT = [[[Dh(h, c, a, b) for b in range(N)] for a in range(N)] for c in range(N)]

    def DDh(d, c, a, b):
        return (sp.diff(DhT[c][a][b], X[d]) - sum(Gam[e][d][c]*DhT[e][a][b] + Gam[e][d][a]*DhT[c][e][b]
                                                   + Gam[e][d][b]*DhT[c][a][e] for e in range(N)))
    G = gamma_of(h)

    def nabla_gamma(a, b):
        return sp.diff(G[b], X[a]) - sum(Gam[e][a][b]*G[e] for e in range(N))
    ok = True
    for (a, b) in [(0, 0), (0, 1), (1, 1), (0, 2), (1, 2), (2, 2), (3, 3), (4, 4)]:
        box = sum(gi[c, d]*DDh(d, c, a, b) for c in range(N) for d in range(N) if gi[c, d] != 0)
        nab_trh = sp.diff(sp.diff(trh, X[b]), X[a]) - sum(Gam[e][a][b]*sp.diff(trh, X[e]) for e in range(N))
        cross = sum(gi[c, d]*(DDh(d, a, c, b) + DDh(d, b, c, a)) for c in range(N) for d in range(N) if gi[c, d] != 0)
        dric = (-box - nab_trh + cross)/2
        rh = sum(gi[c, e]*gi[d, ff]*riem_low(a, e, b, ff)*h[c, d] for c in range(N) for d in range(N)
                 for e in range(N) for ff in range(N) if gi[c, e] != 0 and gi[d, ff] != 0 and h[c, d] != 0)
        res = dric - (-(box + sign*2*rh)/2 + (nabla_gamma(a, b) + nabla_gamma(b, a))/2)
        # the residual is a rational-trigonometric expression that simplify() does not reduce; evaluate it exactly
        # (rational points, 40 digits): the identity gives < 1e-30, the control gives O(1)
        ok &= all(abs(sp.N(res.subs(pt), 40)) < sp.Float("1e-30") for pt in SAMPLE_POINTS)
    chk("dRic = -(1/2)(box h + 2 Riem h) + sym nabla Gamma on a tensor of the class (three sample points)", ok)
    # Gamma[pi_X] = box X for a one-form of the class, with general coefficients: the difference is linear in the
    # derivatives of (Xt, Xr, XL) with coefficients in (r, th), and each coefficient is evaluated at the sample points
    # (simplify() on the whole difference, or inside the helpers on general functions, can run for an hour)
    Xt, Xr, XL = [sp.Function(nm)(t, r, th) for nm in ("Xt", "Xr", "XL")]
    W = [Xt, Xr, XL, 0, 0]
    ok = True
    for a_, b_ in zip(gamma_of(pi_of(W, simp=False), simp=False), box1(W, simp=False)):
        e = sp.expand((a_ - b_).doit())
        rep = {d: sp.Symbol("D%d" % i) for i, d in enumerate(sorted(e.atoms(sp.Derivative), key=str))}
        rep.update({Xt: sp.Symbol("F0"), Xr: sp.Symbol("F1"), XL: sp.Symbol("F2")})
        lin = sp.expand(e.xreplace(rep))
        syms = [q for q in rep.values() if lin.has(q)]
        if not syms:
            ok &= lin == 0
            continue
        for c in sp.Poly(lin, *syms).coeffs():
            ok &= all(abs(sp.N(c.subs(pt), 40)) < sp.Float("1e-30") for pt in SAMPLE_POINTS)
    chk("Gamma[pi_X] = box X for a one-form in the class (every coefficient, at the sample points)", ok)
    return chk.ok


# ---------------------------------------------------------------------------------------------------------- W2
def w2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    W0, W1 = sp.Function("W0")(r), sp.Function("W1")(r)
    bw = box1([W0, W1, 0, 0, 0])
    chk("the t and r equations decouple", not bw[0].has(W1) and not bw[1].has(W0))
    a, b, c, d = sp.symbols("a b c d")
    gen0 = a + b/r**2
    gen1 = c/(r**3*f) + d*r**3/(r**2 - mu)
    chk("W0 = a + b/r^2 solves the t equation", sp.simplify(bw[0].subs(W0, gen0).doit()) == 0)
    chk("W1 = c/(r^3 f) + d r^3/(r^2 - mu) solves the r equation", sp.simplify(bw[1].subs(W1, gen1).doit()) == 0)
    smu = sp.sqrt(mu)
    Wst = [1/r**2, smu/(r**3*f), 0, 0, 0] if control != 1 else [1/r**2, 0, 0, 0, 0]
    chk("box W* = 0", all(sp.simplify(e) == 0 for e in box1(Wst)))
    WR = sp.simplify(Wst[1] - Wst[0]/f)                       # the dr component in the ingoing chart
    chk("W*_R = -1/(r (r + sqrt mu)): regular at the horizon", sp.simplify(WR + 1/(r*(r + smu))) == 0)
    return chk.ok


def Wstar():
    return [1/r**2, sp.sqrt(mu)/(r**3*f), 0, 0, 0]


def Wss():
    smu = sp.sqrt(mu)
    A = (sp.log(f) + mu/r**2)/(2*smu)
    B = ((3*mu**2*sp.log(r**2 - mu) + 2*mu**2 + 3*mu*r**2 - 2*r**4*sp.log(r) + r**4*sp.log(r**2 - mu))
         / (8*mu*r*(r**2 - mu)))
    Ws = Wstar()
    return [t*Ws[0] + A, t*Ws[1] + B, 0, 0, 0]


# ---------------------------------------------------------------------------------------------------------- W3
def w3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    K = g.diff(mu)
    GK = gamma_of(K)
    chk("Gamma[K] = dr/(r^3 f)",
        sp.simplify(GK[1] - 1/(r**3*f)) == 0 and all(e == 0 for e in (GK[0], GK[2], GK[3], GK[4])))
    W = Wss()
    if control == 1:
        W = [W[0] - t*Wstar()[0], W[1] - t*Wstar()[1], 0, 0, 0]
    Kst = K + pi_of(W)
    GKs = [sp.simplify(e) for e in gamma_of(Kst)]
    chk("Gamma[K + pi_{W**}] = 0", all(e == 0 for e in GKs))
    chk("K* - t pi_{W*} is stationary", not sp.simplify(Kst - t*pi_of(Wstar())).has(t))
    return chk.ok


# ---------------------------------------------------------------------------------------------------------- W4
def harmonic(l):
    """the T^2-invariant, mirror-even scalar harmonics of S^3 at l = 2, 4 (Jacobi polynomials in cos 2th)"""
    x = sp.cos(2*th)
    return {2: x, 4: (3*x**2 - 1)/2}[l], l*(l + 2)


def w4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    gam = sp.diag(1, cs**2, sn**2)
    Ftt, Ftr, Frr, F = [sp.Function(nm)(t, r) for nm in ("Ftt", "Ftr", "Frr", "F")]
    Xt, Xr, XL = [sp.Function(nm)(t, r) for nm in ("Xt", "Xr", "XL")]
    pts = [{r: sp.Rational(9, 4), mu: sp.Rational(2, 3)}, {r: sp.Rational(17, 5), mu: sp.Rational(5, 4)}]
    ths = [sp.Rational(3, 10), sp.Rational(11, 10), sp.Rational(7, 10)]
    small = sp.Float("1e-30")

    def tiny(e, v):
        return abs(sp.N(e.subs(v), 40)) < small
    for l in (2, 4):
        S, k2 = harmonic(l)
        lap = sp.simplify(sp.diff(S, th, 2) + (cs/sn - sn/cs)*sp.diff(S, th))
        chk("S at l = %d is a harmonic with k^2 = %d" % (l, k2), sp.simplify(lap + k2*S) == 0)
        k = sp.sqrt(k2)
        Si = -sp.diff(S, th)/k
        hRW = sp.zeros(N)
        hRW[0, 0] = Ftt*S; hRW[0, 1] = hRW[1, 0] = Ftr*S; hRW[1, 1] = Frr*S
        for i in range(3):
            hRW[2 + i, 2 + i] = 2*r**2*F*S*gam[i, i]
        GRW = gamma_of(hRW, simp=False)
        Xv = [Xt*S, Xr*S, XL*r*Si, 0, 0] if control != 1 else [Xt*S, Xr*S, 0, XL*r*cs**2*sn, 0]
        bX = box1(Xv, simp=False)
        # each component is linear in the derivatives of (X, F); its coefficients are checked one by one at rational
        # points (simplify() on the whole component misreads the l = 2 case as theta-dependent)
        good = True
        for i in range(N):
            e = sp.expand((bX[i] + GRW[i]).doit())
            rep = {d: sp.Symbol("D%d" % n) for n, d in enumerate(sorted(e.atoms(sp.Derivative), key=str))}
            rep.update({fn: sp.Symbol("F%d" % n) for n, fn in enumerate((Xt, Xr, XL, Ftt, Ftr, Frr, F))})
            lin = sp.expand(e.xreplace(rep))
            syms = [q for q in rep.values() if lin.has(q)]
            if i >= 3:                                   # the phi components: no equation there
                good &= lin == 0 or all(tiny(c.subs(pt), {th: v})
                                        for c in sp.Poly(lin, *syms).coeffs() for pt in pts for v in ths)
                continue
            basis = (S, S, r*Si)[i]
            poly = sp.Poly(lin, *syms)
            for c in poly.coeffs():                      # theta-free after division by the mode's angular factor
                for pt in pts:
                    vals = [sp.N((c/basis).subs(pt).subs(th, v), 40) for v in ths]
                    good &= abs(vals[0] - vals[1]) < small and abs(vals[0] - vals[2]) < small
            var = (Xt, Xr, XL)[i]
            Dtt = rep.get(sp.Derivative(var, (t, 2))); Drr = rep.get(sp.Derivative(var, (r, 2)))
            ctt = poly.coeff_monomial(Dtt) if Dtt is not None else sp.Integer(0)
            crr = poly.coeff_monomial(Drr) if Drr is not None else sp.Integer(0)
            good &= all(tiny(ctt/basis + 1/f, {**pt, th: ths[0]}) and tiny(crr/basis - f, {**pt, th: ths[0]})
                        for pt in pts)
        chk("l = %d: box X + Gamma[h_RW] is three th-free 1+1 equations with principal part -f^-1 d_t^2 + f d_r^2" % l,
            good)
    return chk.ok



# ---------------------------------------------------------------------------------------------------------- W5
def w5(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    a_, b_ = sp.Function("a")(th), sp.Function("b")(th)
    c_ = -a_ - b_
    gam = sp.diag(1, cs**2, sn**2); gami = gam.inv(); Y = [th, p1, p2]
    Gs = [[[sp.simplify(sum(gami[i, m]*(sp.diff(gam[m, j], Y[q]) + sp.diff(gam[m, q], Y[j]) - sp.diff(gam[j, q], Y[m]))
                            for m in range(3))/2) for q in range(3)] for j in range(3)] for i in range(3)]
    T = sp.diag(a_, cs**2*b_, sn**2*c_)

    def DT(q, i, j):
        return sp.diff(T[i, j], Y[q]) - sum(Gs[m][q][i]*T[m, j] + Gs[m][q][j]*T[i, m] for m in range(3))
    divT = [sp.simplify(sum(gami[i, q]*DT(q, i, j) for i in range(3) for q in range(3))) for j in range(3)]
    ap = sp.solve(sp.Eq(divT[0], 0), sp.Derivative(a_, th))[0]
    H = sp.Function("H")(t, r)
    h = sp.zeros(N)
    for i in range(3):
        for j in range(3):
            h[2 + i, 2 + j] = 2*r**2*H*T[i, j]
    G = gamma_of(h)
    if control != 1:
        G = [e.subs(sp.Derivative(a_, th), ap) for e in G]
    chk("Gamma[h_T] = 0 for T traceless and divergence-free", all(sp.simplify(e) == 0 for e in G))
    return chk.ok


# ---------------------------------------------------------------------------------------------------------- W6
def w6(control=0, verbose=False, ls=(2,)):
    """the structure of box X = J for the scalar-type one-form of W4: with S := div X, F := dX, P := F_tr/S_l,
    Q_t := -F_{t th}/S_l', Q_r := -F_{r th}/S_l' and box_l the scalar wave operator at mode l, seven identities in X,
    every coefficient evaluated at the three sample points to forty digits (as W1); l = 2 by default (about half a
    minute), l = 2 and 4 under --l4 (about 72 minutes with the control)"""
    chk = Checklist(verbose, quiet=control != 0)
    D = sp.diff

    def vanishes(e, funcs):                  # e linear in the derivatives of funcs: every coefficient is zero,
        for pt in SAMPLE_POINTS:             # evaluated at the sample points to forty digits (as W1 does); the
            ep = sp.expand(e.subs(th, pt[th]).doit())            # angle goes in first, which keeps the expansion small
            rep = {d: sp.Symbol("D%d" % n) for n, d in enumerate(sorted(ep.atoms(sp.Derivative), key=str))}
            rep.update({fn: sp.Symbol("F%d" % n) for n, fn in enumerate(funcs)})
            lin = sp.expand(ep.xreplace(rep))
            syms = [q for q in rep.values() if lin.has(q)]
            coeffs = sp.Poly(lin, *syms).coeffs() if syms else [lin]
            if not all(abs(sp.N(c.subs(pt), 40)) < sp.Float("1e-30") for c in coeffs):
                return False
        return True
    sign = -1 if control == 1 else 1
    for l in ls:
        S, k2 = harmonic(l)
        k = sp.sqrt(k2)
        Sth = D(S, th)
        Si = -Sth/k
        Xt, Xr, XL = [sp.Function(nm)(t, r) for nm in ("Xt", "Xr", "XL")]
        Xv = [Xt*S, Xr*S, XL*r*Si, 0, 0]
        bX = box1(Xv, simp=False)
        box_l = lambda u: -D(u, t, 2)/f + f*D(u, r, 2) + (3*r**2 - mu)/r**3*D(u, r) - k2/r**2*u    # noqa: E731
        Sd = sum(gi[a, b]*D1(Xv, a, b) for a in range(N) for b in range(N) if gi[a, b] != 0)/S
        P = D(Xr, t) - D(Xt, r)
        Qt = (D(Xv[2], t) - D(Xv[0], th))/(-Sth)
        Qr = (D(Xv[2], r) - D(Xv[1], th))/(-Sth)
        Jt, Jr = bX[0]/S, bX[1]/S
        divbox = sum(gi[a, b]*D1(bX, a, b) for a in range(N) for b in range(N) if gi[a, b] != 0)/S
        items = [
            ("div(box X) = box_l(div X)", divbox - box_l(Sd)),
            ("(box X)_t = box_l X_t + (2 mu/r^3) F_tr", Jt - box_l(Xt) - sign*2*mu/r**3*P),
            ("(box X)_r = d_r S - f^-1 d_t F_tr - (k^2/r^2) Q_r", Jr - (D(Sd, r) - D(P, t)/f - k2/r**2*Qr)),
            ("r (box X)_L = box_l(r X_L) - (2 k f/r) Q_r", r*bX[2]/(r*Si) - box_l(r*XL) + 2*k*f/r*Qr),
            ("(box X)_t = d_t S - (f/r^3) d_r(r^3 F_tr) - (k^2/r^2) Q_t",
             Jt - (D(Sd, t) - f/r**3*D(r**3*P, r) - k2/r**2*Qt)),
            ("d(box X)_tr = box_l F_tr - ((3 r^2 - 9 mu)/r^4) F_tr - (2 k^2/r^3) Q_t",
             D(Jr, t) - D(Jt, r) - (box_l(P) - (3*r**2 - 9*mu)/r**4*P - 2*k2/r**3*Qt)),
            ("box_l(r F_tr) + (4 mu/r^4) r F_tr = r d(box X)_tr + 2 (d_t S - (box X)_t)",
             box_l(r*P) + sign*4*mu/r**4*r*P - r*(D(Jr, t) - D(Jt, r)) - 2*(D(Sd, t) - Jt)),
        ]
        for name, e in items:
            chk("l = %d: %s" % (l, name), vanishes(e, (Xt, Xr, XL)))
    return chk.ok


# ---------------------------------------------------------------------------------------------------------- W7
_S = sp.Function("S")(th)
_Sp = sp.diff(_S, th)
_RULE2 = -2*sp.cot(2*th)*_Sp - kk**2*_S                  # the harmonic ODE on S^3 for a T^2-invariant S: S'' = ...
_PYTH = [(sp.Rational(3, 5), sp.Rational(4, 5)), (sp.Rational(5, 13), sp.Rational(12, 13))]   # exact (cos, sin)
_s0, _s1 = sp.symbols("s0 s1")
_fp = sp.diff(f, r)


def _red(e):
    """apply the harmonic's ODE to every second and higher derivative of S"""
    e = e.doit()
    for _ in range(8):
        ds = [d for d in e.atoms(sp.Derivative) if d.expr == _S and d.derivative_count >= 2]
        if not ds:
            break
        e = e.xreplace({d: sp.diff(_RULE2, th, d.derivative_count - 2) for d in ds}).doit()
    return e


def _at_angle(e, cs0, sn0):
    """the angle evaluated exactly at a Pythagorean pair, every trigonometric multiple reduced first"""
    for _ in range(3):
        rep = {}
        for atom in e.atoms(sp.cos, sp.sin, sp.tan, sp.cot):
            if atom.args[0] != th:
                rep[atom] = sp.expand_trig(atom)
        rep.update({sp.tan(th): sn/cs, sp.cot(th): cs/sn})
        e = e.xreplace(rep)
    e = e.xreplace({cs: cs0, sn: sn0})
    assert not e.has(th), "angle left"
    return e


def _lin(e, V):
    """e linear in V and their t, r derivatives: {(j, nt, nr): coefficient}, cancelled, zeros dropped"""
    e = sp.expand(e)
    rep, keys = {}, {}
    for dd in e.atoms(sp.Derivative):
        if dd.expr in V:
            nt = sum(c for v_, c in dd.variable_count if v_ == t)
            nr = sum(c for v_, c in dd.variable_count if v_ == r)
            s_ = sp.Symbol("D%d_%d%d" % (V.index(dd.expr), nt, nr))
            rep[dd] = s_
            keys[s_] = (V.index(dd.expr), nt, nr)
    for j, v_ in enumerate(V):
        s_ = sp.Symbol("D%d_00" % j)
        rep[v_] = s_
        keys[s_] = (j, 0, 0)
    ee = sp.expand(e.xreplace(rep))
    syms = [q for q in rep.values() if ee.has(q)]
    out = {}
    if syms:
        P = sp.Poly(ee, *syms)
        assert P.total_degree() <= 1
        for m, c in zip(P.monoms(), P.coeffs()):
            idx = [i for i, e_ in enumerate(m) if e_ == 1]
            c = sp.cancel(c)
            if idx and c != 0:
                out[keys[syms[idx[0]]]] = c
    return out


def _ang(e, which, V):
    """the coefficient of S (which 0) or of its derivative (which 1) in e, the other one vanishing and the angle
    dropping out (two Pythagorean points agree): the scalar sector closes"""
    out = []
    for cs0, sn0 in _PYTH:
        ee = _at_angle(_red(e).xreplace({_Sp: _s1}).xreplace({_S: _s0}), cs0, sn0)
        rep = {}
        for dd in ee.atoms(sp.Derivative):
            if dd.expr in V:
                nt = sum(c for v_, c in dd.variable_count if v_ == t)
                nr = sum(c for v_, c in dd.variable_count if v_ == r)
                rep[dd] = sp.Symbol("D%d_%d%d" % (V.index(dd.expr), nt, nr))
        for j, v_ in enumerate(V):
            rep[v_] = sp.Symbol("D%d_00" % j)
        ee = sp.expand(ee.xreplace(rep))
        syms = [q for q in rep.values() if ee.has(q)]
        P = sp.Poly(ee, _s0, _s1, *syms)
        other, mine = 0, 0
        for m, c in zip(P.monoms(), P.coeffs()):
            mono = sp.Mul(*[q**e_ for q, e_ in zip(syms, m[2:])])
            if m[(which + 1) % 2] == 1:
                other += sp.cancel(c)*mono
            elif m[which] == 1:
                mine += sp.cancel(c)*mono
        assert sp.cancel(other) == 0, "the other angular factor survives"
        out.append(mine)
    assert sp.cancel(sp.expand(out[0] - out[1])) == 0, "angle dependence"
    back = {sp.Symbol("D%d_%d%d" % (j, nt, nr)): (sp.diff(V[j], *([t]*nt + [r]*nr)) if nt + nr else V[j])
            for j in range(len(V)) for nt in range(3) for nr in range(3)}
    return out[0].xreplace(back)


def _lich(h):
    """the Lichnerowicz operator box h + 2 Riem h, components (tt, tr, rr, t th, r th, th th, 11, 22)"""
    DhT = [[[Dh(h, c, a, b) for b in range(N)] for a in range(N)] for c in range(N)]

    def DDh(d, c, a, b):
        return (sp.diff(DhT[c][a][b], X[d]) - sum(Gam[e][d][c]*DhT[e][a][b] + Gam[e][d][a]*DhT[c][e][b]
                                                   + Gam[e][d][b]*DhT[c][a][e] for e in range(N)))
    E = {}
    for (a, b) in [(0, 0), (0, 1), (1, 1), (0, 2), (1, 2), (2, 2), (3, 3), (4, 4)]:
        box = sum(gi[c, d]*DDh(d, c, a, b) for c in range(N) for d in range(N) if gi[c, d] != 0)
        rh = sum(gi[c, e]*gi[d, ff]*riem_low(a, e, b, ff)*h[c, d] for c in range(N) for d in range(N)
                 for e in range(N) for ff in range(N) if gi[c, e] != 0 and gi[d, ff] != 0 and h[c, d] != 0)
        E[(a, b)] = box + 2*rh
    return E


def _hung_ansatz(H, l0=False):
    """h in Hung's components, five-dimensional: H1 = (h_tt + f^2 h_rr)/2 + ((1 - f)/2) trs h, H2 = trs h/sqrt3,
    H3 = (h_tt/f - f h_rr)/2, H6 = f h_tr + ((1 - f)/2) trs h, H4 = f k h_rth/(r S_th), H7 = k h_tth/(r S_th),
    hhat_AB = 2 r^2 H5 S_AB (S_AB = D_A D_B S/k^2 + gamma_AB S/3); l0: the l = 0 sector, S = 1"""
    H1, H2, H3, H4, H5, H6, H7 = H
    gam = sp.diag(1, cs**2, sn**2)
    a = (1 - f)/2
    trs = sp.sqrt(3)*H2
    Sl, Spl = (sp.Integer(1), sp.Integer(0)) if l0 else (_S, _Sp)
    h = sp.zeros(N)
    h[0, 0] = (H1 - a*trs + f*H3)*Sl
    h[1, 1] = (H1 - a*trs - f*H3)*Sl/f**2
    h[0, 1] = h[1, 0] = (H6 - a*trs)*Sl/f
    if not l0:
        h[0, 2] = h[2, 0] = r*H7*Spl/kk
        h[1, 2] = h[2, 1] = r*H4*Spl/(kk*f)
        DDS = sp.diag(sp.diff(_S, th, 2), -cs*sn*_Sp, sn*cs*_Sp)
        SAB = DDS/kk**2 + gam*_S/3
    for i in range(3):
        h[2 + i, 2 + i] = r**2*(trs*Sl*gam[i, i]/3 + (0 if l0 else 2*H5*SAB[i, i]))
    return h


_ROWS_CACHE, _L0_CACHE = {}, {}


def _hung_rows(sign=1):
    """box H_i = sum_j A_ij H_j + U_i for Hung's seven components on five-dimensional Tangherlini, from the
    Lichnerowicz components LW and the gauge one-form Gamma (admixtures times sign): returns A (7x7, rational in
    r, mu, k), the first-order residuals of the seven rows ({(j, nt, nr): coefficient} each) after the nabla_L terms
    rho_6 L(H6 - H1), rho_7 L(H7 - H4) with rho_6 = 2f'/f, rho_7 = f'/f are removed, and the second-order residuals"""
    if sign in _ROWS_CACHE:
        return _ROWS_CACHE[sign]
    H = [sp.Function("H%d" % i)(t, r) for i in range(1, 8)]
    h = _hung_ansatz(H)
    E = _lich(h)
    G = gamma_of(h, simp=False)
    gam = sp.diag(1, cs**2, sn**2)
    trE = sum(E[(2 + i, 2 + i)]/gam[i, i] for i in range(3))/r**2
    TF = E[(2, 2)] - r**2*trE/3
    outs = []
    for cs0, sn0 in _PYTH:                   # hat LW_thth = 2 r^2 e5 S_thth, S_thth = -2 cot(2th) S_th/k^2 - 2 S/3
        ee = _at_angle(_red(TF).xreplace({_Sp: _s1}).xreplace({_S: _s0}), cs0, sn0)
        cot2 = (cs0**2 - sn0**2)/(2*cs0*sn0)
        a0 = sp.expand(ee.xreplace({_s1: 0}).xreplace({_s0: 1}))/(2*r**2*sp.Rational(-2, 3))
        a1 = sp.expand(ee.xreplace({_s0: 0}).xreplace({_s1: 1}))/(2*r**2*(-2*cot2/kk**2))
        assert not _lin(sp.expand(a0 - a1), H), "traceless part not proportional to S_AB"
        outs.append(a0)
    assert not _lin(sp.expand(outs[0] - outs[1]), H), "angle dependence"
    LW5 = outs[0]
    LWtt, LWtr, LWrr = _ang(E[(0, 0)], 0, H), _ang(E[(0, 1)], 0, H), _ang(E[(1, 1)], 0, H)
    LWt, LWr, trLW = _ang(E[(0, 2)], 1, H), _ang(E[(1, 2)], 1, H), _ang(trE, 0, H)
    Gr, Gth = _ang(G[1], 0, H), _ang(G[2], 1, H)
    a = (1 - f)/2
    boxhat = lambda u: -sp.diff(u, t, 2)/f + f*sp.diff(u, r, 2) + (_fp + 3*f/r)*sp.diff(u, r)   # noqa: E731
    Lop = lambda u: sp.diff(u, t) + f*sp.diff(u, r)                                               # noqa: E731
    b1, b4 = sign*2*f*_fp, sign*kk*_fp/r
    combo = [(LWtt + f**2*LWrr)/2 + a*trLW + b1*Gr, trLW/sp.sqrt(3), (LWtt/f - f*LWrr)/2, f*kk*LWr/r + b4*Gth, LW5,
             f*LWtr + a*trLW + b1*Gr, kk*LWt/r + b4*Gth]
    rho = {5: 2*_fp/f, 6: _fp/f}
    dvar = {5: H[5] - H[0], 6: H[6] - H[3]}
    A = sp.zeros(7)
    first, second = {}, {}
    for i in range(7):
        res = sp.expand(boxhat(H[i]) - combo[i])
        if i in dvar:
            res = sp.expand(res - rho[i]*Lop(dvar[i]))
        parts = _lin(res, H)
        first[i] = {key: c for key, c in parts.items() if key[1] + key[2] == 1}
        second[i] = {key: c for key, c in parts.items() if key[1] + key[2] == 2}
        for key, c in parts.items():
            if key[1] + key[2] == 0:
                A[i, key[0]] = c
    _ROWS_CACHE[sign] = (A, first, second)
    return A, first, second


def _hung_l0(sign=1):
    """the l = 0 sector (H1, H2, H3, H6; S = 1): the zeroth-order matrix after the same admixtures"""
    if sign in _L0_CACHE:
        return _L0_CACHE[sign]
    H = [sp.Function("H%d" % i)(t, r) for i in range(1, 8)]
    h = _hung_ansatz(H, l0=True)
    E = _lich(h)
    G = gamma_of(h, simp=False)
    gam = sp.diag(1, cs**2, sn**2)
    trE = sum(E[(2 + i, 2 + i)]/gam[i, i] for i in range(3))/r**2

    def flat(e):
        out = [_at_angle(e.doit(), cs0, sn0) for cs0, sn0 in _PYTH]
        assert not _lin(sp.expand(out[0] - out[1]), H)
        return out[0]
    LWtt, LWtr, LWrr, trLW, Gr = flat(E[(0, 0)]), flat(E[(0, 1)]), flat(E[(1, 1)]), flat(trE), flat(G[1])
    a = (1 - f)/2
    boxhat = lambda u: -sp.diff(u, t, 2)/f + f*sp.diff(u, r, 2) + (_fp + 3*f/r)*sp.diff(u, r)   # noqa: E731
    Lop = lambda u: sp.diff(u, t) + f*sp.diff(u, r)                                               # noqa: E731
    b1 = sign*2*f*_fp
    combo = {0: (LWtt + f**2*LWrr)/2 + a*trLW + b1*Gr, 1: trLW/sp.sqrt(3), 2: (LWtt/f - f*LWrr)/2,
             5: f*LWtr + a*trLW + b1*Gr}
    idx = [0, 1, 2, 5]
    A0 = sp.zeros(4)
    ok = True
    for ii, i in enumerate(idx):
        res = sp.expand(boxhat(H[i]) - combo[i])
        if i == 5:
            res = sp.expand(res - (2*_fp/f)*Lop(H[5] - H[0]))
        parts = _lin(res, H)
        ok &= not any(key[1] + key[2] >= 1 for key in parts)
        for key, c in parts.items():
            if key[1] + key[2] == 0:
                A0[ii, idx.index(key[0])] = c
    _L0_CACHE[sign] = (A0, ok)
    return A0, ok


def w7(control=0, verbose=False):
    """the five-dimensional form of Hung's Proposition 4.2 (arXiv:1909.06733): in his seven components, with the
    harmonic gauge condition admixed, box H = A H + U H with U along nabla_L in rows 6, 7 only; the leading matrix's
    spectrum; the horizon-regular variables and their nabla_L' coefficients; the l = 0 sector (about two minutes)"""
    chk = Checklist(verbose, quiet=control != 0)
    sign = -1 if control == 1 else 1
    try:
        A, first, second = _hung_rows(sign)
    except AssertionError as exc:
        chk("the scalar sector closes (every component projects on S, its derivative or S_AB alone): %s" % exc, False)
        return chk.ok
    chk("the scalar sector closes: every Lichnerowicz and gauge component projects on S, S_th or S_AB alone", True)
    chk("every row has the scalar wave operator as principal part", all(not second[i] for i in range(7)))
    chk("rows 1-5 have no first-order term: (1 - f)/2 trs h in H1, H6; 2 f f' Gamma_r in rows 1, 6; k f'/r Gamma_th in "
        "rows 4, 7", all(not first[i] for i in range(5)))
    chk("rows 6, 7: the first-order terms are (2f'/f) nabla_L (H6 - H1) and (f'/f) nabla_L (H7 - H4), Hung's U with "
        "2M/r^2 -> f'", not first[5] and not first[6])
    if control and not chk.ok:                        # the control has failed already; the rest costs minutes
        return chk.ok
    l = sp.symbols("l", positive=True)
    lam = sp.symbols("lambda")
    Amain = (A*r**2).applyfunc(lambda x: sp.cancel(sp.limit(x, r, sp.oo)))
    cp = sp.expand(Amain.subs(kk, sp.sqrt(l*(l + 2))).charpoly(lam).as_expr())
    want = sp.expand(sp.prod([(lam - (l + aa)*(l + aa + 2)) for aa in (-2, -1, 0, 0, 0, 1, 2)]))
    chk("r^2 A_main at k^2 = l(l+2) has the eigenvalues (l+a)(l+a+2), a = -2, -1, 0, 0, 0, 1, 2: semi-positive for "
        "l >= 2, Hung's Lemma 4.3 with (l+a)(l+a+1) -> (l+a)(l+a+2)", sp.expand(cp - want) == 0)
    sub = ((A - Amain/r**2)*r**4).applyfunc(lambda x: sp.cancel(sp.limit(x, r, sp.oo)))
    chk("A - A_main/r^2 = O(mu/r^4): the sub-leading part decays two powers faster, as Hung's A_sub does one",
        all(x.is_finite for x in sub) and sub != sp.zeros(7))
    # the regular variables H' = (H1, ..., H5, H6' = (H6 - H1)/f^2, H7' = (H7 - H4)/f): H = R H', so that
    # box H' = R^-1 (A R - f R'' - c1 R') H' + R^-1 (U - 2 f R' d_r H'), c1 = f' + 3f/r; rows 1-5 of R^-1 are the
    # identity's, so rows 1'-5' keep no first-order term; row 6': rho_6 L(f^2 H6')/f^2 - 4 f' d_r H6' =
    # 2 f' (f^-1 d_t - d_r) H6' = 2 f' nabla_L' H6' plus rho_6 L(f^2) H6'/f^2 = 4 f'^2/f H6' at zeroth order, which
    # cancels a singular term of R^-1 A R; row 7' likewise with f'
    R = sp.eye(7)
    R[5, 0] = 1
    R[5, 5] = f**2
    R[6, 3] = 1
    R[6, 6] = f
    Ri = R.inv()
    c1 = _fp + 3*f/r
    Rd, Rdd = R.diff(r), R.diff(r, 2)
    Ap = (Ri*(A*R - f*Rdd - c1*Rd)).applyfunc(sp.cancel)
    Ap[5, 5] = sp.cancel(Ap[5, 5] + (2*_fp/f)*(2*f**2*_fp)/f**2)     # rho_6 L(f^2) H6' / f^2 = 4 f'^2/f H6'
    Ap[6, 6] = sp.cancel(Ap[6, 6] + (_fp/f)*(f*_fp)/f)                  # rho_7 L(f) H7' / f = f'^2/f H7'
    at6, ar6 = 2*_fp/f, 2*_fp - 4*_fp                 # coefficients of d_t H6', d_r H6' in row 6'
    at7, ar7 = _fp/f, _fp - 2*_fp
    alpha6, beta6 = sp.cancel((ar6 + f*at6)/(2*f)), sp.cancel((f*at6 - ar6)/2)
    alpha7, beta7 = sp.cancel((ar7 + f*at7)/(2*f)), sp.cancel((f*at7 - ar7)/2)
    rh = sp.sqrt(mu)
    regular = all(sp.fraction(sp.cancel(x))[1].subs(r, rh) != 0 for x in Ap)
    chk("in the regular variables H6' = (H6 - H1)/f^2, H7' = (H7 - H4)/f every coefficient is regular at the "
        "horizon", regular)
    chk("rows 6', 7' carry 2f' nabla_L' H6' and f' nabla_L' H7' (f' = 2 mu/r^3 > 0) and no nabla_L; rows 1'-5' no "
        "first-order term: Hung's 4M/r^2, 2M/r^2 with 2M/r^2 -> f'",
        alpha6 == 0 and alpha7 == 0 and sp.cancel(beta6 - 2*_fp) == 0 and sp.cancel(beta7 - _fp) == 0)
    A0, ok0 = _hung_l0(sign)
    A0main = (A0*r**2).applyfunc(lambda x: sp.cancel(sp.limit(x, r, sp.oo)))
    cp0 = sp.expand(A0main.charpoly(lam).as_expr())
    chk("l = 0 (H1, H2, H3, H6): no first-order term but the U row, r^2 A_main with eigenvalues 0, 0, 3, 8",
        ok0 and sp.expand(cp0 - lam**2*(lam - 3)*(lam - 8)) == 0)
    return chk.ok


# ---------------------------------------------------------------------------------------------------------- W8
def _lin_syms(e, funcs, coords):
    """e polynomial in funcs and their derivatives: {monomial string: coefficient}, derivatives as symbols"""
    rep = {}
    for dd in e.atoms(sp.Derivative):
        rep[dd] = sp.Symbol("d_" + str(dd).replace("Derivative(", "").replace(")", "").replace("(", "_")
                            .replace(", ", "_").replace(" ", ""))
    for fn in funcs:
        rep[fn] = sp.Symbol(fn.func.__name__)
    e2 = sp.expand(e.xreplace(rep))
    gens = sorted(set(rep.values()), key=str)
    P = sp.Poly(e2, *gens)
    out = {}
    for m, c in zip(P.monoms(), P.coeffs()):
        c = sp.simplify(c)
        if c != 0:
            out[str(sp.Mul(*[g_**mm for g_, mm in zip(gens, m)]))] = sp.factor(c)
    return out


def _radiation_potential(sign=1):
    """the W7 system in the orthonormal-leading rescaling Hhat = Dm H, and the radiation field's potential
    V = Ahat + V0 I, V0 = (3/4 + 9 mu/(4 r^2))/r^2 (sign: the control reverses V0)"""
    A, first, second = _hung_rows(1)
    nS = sp.sqrt(sp.Rational(2, 3)*(kk**2 - 3)/kk**2)
    Dm = sp.diag(sp.sqrt(2), 1, sp.sqrt(2), sp.sqrt(2), 2*nS, sp.sqrt(2), sp.sqrt(2))
    V0 = sign*(sp.Rational(3, 4) + 9*mu/(4*r**2))/r**2
    Vr = (A + V0*sp.eye(7)).applyfunc(sp.cancel)                       # Hung's variables (rational)
    Ah = (Dm*A*Dm.inv()).applyfunc(sp.cancel)
    Vh = (Ah + V0*sp.eye(7)).applyfunc(sp.cancel)                      # rescaled (symmetric leading part)
    return Vr, Vh


def w8(control=0, verbose=False):
    """the identities of Hung's Proposition 4.1 (arXiv:1909.06733, Lemma 4.4, (4.8), (4.9)) in five dimensions,
    on the W7 system: the radiation field's potential and its spectrum; the first-order term; the p-current's
    divergence (formal, two components); the red-shift divergence at the horizon (formal); the T-current with the
    s^-delta weight (formal); the angular eigenvalues of the one-form and tensor components; the k-degree of the
    matrices and the l = 0 sector (about two minutes after W7, whose matrices it reuses; six alone)"""
    chk = Checklist(verbose, quiet=control != 0)
    D = sp.diff
    sign = -1 if control == 1 else 1
    # (a) the radiation field: r^(3/2) boxhat(r^-3/2 Psi) = -f^-1 d_u d_v Psi - V0 Psi, so the system reads
    #     d_u d_v Psi = -f (Ahat + V0) Psi - f Uhat Psi
    Psi = sp.Function("Psi")(t, r)
    boxhat = lambda u: -D(u, t, 2)/f + f*D(u, r, 2) + (_fp + 3*f/r)*D(u, r)                 # noqa: E731
    dudv = lambda u: D(u, t, 2) - f*D(f*D(u, r), r)                                           # noqa: E731
    V0 = (sp.Rational(3, 4) + 9*mu/(4*r**2))/r**2
    rad = sp.simplify(r**sp.Rational(3, 2)*boxhat(r**sp.Rational(-3, 2)*Psi) - (-dudv(Psi)/f - V0*Psi))
    chk("the radiation field Psi = r^(3/2) H: r^(3/2) box(r^-3/2 Psi) = -f^-1 d_u d_v Psi - (3/4 + 9 mu/(4 r^2)) "
        "Psi/r^2 "
        "([Sch13] (5.11)-(5.12) at n = 4)", rad == 0)
    Vr, Vh = _radiation_potential(sign)
    l = sp.symbols("l", positive=True)
    lam = sp.Symbol("lambda")
    Vinf = (Vr*r**2).applyfunc(lambda x: sp.cancel(sp.limit(x, r, sp.oo)))
    cp = sp.expand(Vinf.subs(kk, sp.sqrt(l*(l + 2))).charpoly(lam).as_expr())
    want = sp.expand(sp.prod([(lam - (l + a + sp.Rational(1, 2))*(l + a + sp.Rational(3, 2)))
                              for a in (-2, -1, 0, 0, 0, 1, 2)]))
    chk("V_inf := lim r^2 (Ahat + V0) has the eigenvalues (l+a+1/2)(l+a+3/2), a = -2, -1, 0, 0, 0, 1, 2: at "
        "least 3/4 at every l >= 2 (Hung's l = 2 zero eigenvalue is lifted) and at least (3/32) l(l+2)",
        sp.expand(cp - want) == 0)
    Vhinf = (Vh*r**2).applyfunc(lambda x: sp.simplify(sp.limit(x, r, sp.oo)))
    x = sp.Symbol("x", positive=True)
    ok = sp.simplify(Vhinf - Vhinf.T) == sp.zeros(7)
    for e in (Vh - Vhinf/r**2):
        ser = sp.expand(sp.series(sp.cancel(e).subs(r, 1/x), x, 0, 5).removeO())
        ok &= (ser == 0) or all(m[0] >= 4 for m in sp.Poly(ser, x).monoms())
    chk("V_inf is symmetric in the rescaled variables and V - V_inf/r^2 = O(mu/r^4)", ok)
    # (b) the first-order term in the Psi variables: rows 6 and 7 only
    H = [sp.Function("H%d" % i)(t, r) for i in range(1, 8)]
    Lop = lambda u: D(u, t) + f*D(u, r)                                                        # noqa: E731
    nS = sp.sqrt(sp.Rational(2, 3)*(kk**2 - 3)/kk**2)
    Dm = sp.diag(sp.sqrt(2), 1, sp.sqrt(2), sp.sqrt(2), 2*nS, sp.sqrt(2), sp.sqrt(2))
    Uvec = sp.zeros(7, 1)
    Uvec[5] = (2*_fp/f)*Lop(H[5] - H[0])
    Uvec[6] = (_fp/f)*Lop(H[6] - H[3])
    Ps = [sp.Function("P%d" % i)(t, r) for i in range(1, 8)]
    subsH = {H[i]: sum(Dm.inv()[i, j]*Ps[j] for j in range(7))*r**sp.Rational(-3, 2) for i in range(7)}
    Uhat = (r**sp.Rational(3, 2)*Dm*Uvec).subs(subsH).doit().applyfunc(sp.expand)
    want6 = sp.expand((2*_fp/f)*Lop(Ps[5] - Ps[0]) - (3*_fp/r)*(Ps[5] - Ps[0]))
    want7 = sp.expand((_fp/f)*Lop(Ps[6] - Ps[3]) - (3*_fp/(2*r))*(Ps[6] - Ps[3]))
    ok = all(not _lin(sp.expand(Uhat[i]), Ps) for i in (0, 1, 2, 3, 4))
    ok &= not _lin(sp.expand(Uhat[5] - want6), Ps) and not _lin(sp.expand(Uhat[6] - want7), Ps)
    chk("Uhat Psi = (2f'/f) nabla_L (Psi_6 - Psi_1) - (3f'/r)(Psi_6 - Psi_1) in row 6, (f'/f) nabla_L (Psi_7 - Psi_4) "
        "- (3f'/(2r))(Psi_7 - Psi_4) in row 7, nothing else", ok)
    # (c) the p-current identity, formal: two components, V_inf constant symmetric, V(r) and Uhat arbitrary
    p = sp.Symbol("p", positive=True)
    m11, m12, m22 = sp.symbols("m11 m12 m22")
    Vc = sp.Matrix([[m11, m12], [m12, m22]])
    Vf = sp.Matrix(2, 2, lambda i, j: sp.Function("V%d%d" % (i + 1, j + 1))(r))
    P2 = sp.Matrix([sp.Function("P1")(t, r), sp.Function("P2")(t, r)])
    U2 = sp.Matrix([sp.Function("U1")(t, r), sp.Function("U2")(t, r)])
    Ptt = (f*(f*P2.diff(r)).diff(r) - f*Vf*P2 - f*U2).applyfunc(sp.expand)
    gQ = sp.diag(-f, 1/f)
    gQi = gQ.inv()
    grad = [P2.diff(t), P2.diff(r)]
    sq = sum(gQi[a, b]*(grad[a].T*grad[b])[0, 0] for a in range(2) for b in range(2))
    TT = sp.Matrix(2, 2, lambda a, b: (grad[a].T*grad[b])[0, 0] - gQ[a, b]*sq/2)
    Lvec = sp.Matrix([1, f]) if control != 1 else sp.Matrix([1, -f])
    Llow = gQ*Lvec
    Q = (P2.T*Vc*P2)[0, 0]/r**2
    w = r**(p - 3)
    Jlow = sp.Matrix([w/f*(sum(TT[a, b]*Lvec[b] for b in range(2)) - Q*Llow[a]/2) for a in range(2)])
    Jup = gQi*Jlow
    div = (D(r**3*Jup[0], t) + D(r**3*Jup[1], r))/r**3
    div = sp.expand(div.subs({D(P2[i], t, 2): Ptt[i] for i in range(2)}).doit())
    LP = sp.Matrix([Lop(P2[i]) for i in range(2)])
    alpha = r**(p - 4)*(p*f/2 - mu/r**2)/f**2
    beta = (2 - p)*r**(p - 4)/2
    cross = (w/f)*(LP.T*((Vf - Vc/r**2)*P2 + U2))[0, 0]
    resid = sp.expand(div - alpha*(LP.T*LP)[0, 0] - beta*Q - cross)
    funcs = list(P2) + list(U2) + list(Vf)
    chk("div J^p = r^(p-4) f^-2 (p f/2 - mu/r^2) |nabla_L Psi|^2 + (2 - p)/2 r^(p-6) Psi.V_inf.Psi + r^(p-3) f^-1 "
        "nabla_L Psi . ((V - V_inf/r^2) Psi + Uhat Psi), for J^p = r^(p-3) f^-1 (T_ab[Psi] L^b "
        "- Psi.V_inf.Psi L_a/(2 r^2)) "
        "([Hun19] (4.5))", not _lin_syms(resid, funcs, (t, r)))
    JLbar = sp.simplify(sum(Jlow[a]*sp.Matrix([1, -f])[a] for a in range(2)) - r**(p - 5)*(P2.T*Vc*P2)[0, 0])
    JL = sp.simplify(sum(Jlow[a]*sp.Matrix([1, f])[a] for a in range(2)) - r**(p - 3)/f*(LP.T*LP)[0, 0])
    chk("J^p . L-bar = r^(p-5) Psi.V_inf.Psi >= 0 at null infinity and J^p . L = r^(p-3) f^-1 |nabla_L Psi|^2 on Sigma'",
        JLbar == 0 and JL == 0)
    # (d) the red-shift divergence at the horizon, formal: Q a 2-vector in the ingoing chart (v, R), the angular energy
    #     Q.K.Q/r^2 in T_ab, box-hat Q = (K/r^2 + Acal) Q + beta L' Q, L' = -d_R,
    #     Y = (sigma/2)(r - r_h) T + (2 + sigma (r - r_h)) L'
    v = sp.Symbol("v", real=True)
    Qv = sp.Matrix([sp.Function("Q1")(v, r), sp.Function("Q2")(v, r)])
    a11, a12, a21, a22, b1, b2, k1, k2 = sp.symbols("a11 a12 a21 a22 b1 b2 k1 k2")
    Acal = sp.Matrix([[a11, a12], [a21, a22]])
    betaM = sp.diag(b1, b2)
    Kmat = sp.diag(k1, k2)
    rh = sp.sqrt(mu)
    Qvr = (((Kmat/r**2 + Acal)*Qv - betaM*Qv.diff(r) - f*Qv.diff(r, 2) - 3*(Qv.diff(v) + f*Qv.diff(r))/r
            - _fp*Qv.diff(r))/2).applyfunc(sp.expand)
    sigma, cc = sp.symbols("sigma c", positive=True)
    Yvec = sp.Matrix([sigma/2*(r - rh), -(2 + sigma*(r - rh))])
    gV = sp.Matrix([[-f, 1], [1, 0]])
    gVi = gV.inv()
    gradQ = [Qv.diff(v), Qv.diff(r)]
    sqQ = sum(gVi[a, b]*(gradQ[a].T*gradQ[b])[0, 0] for a in range(2) for b in range(2)) + (Qv.T*Kmat*Qv)[0, 0]/r**2
    TTv = sp.Matrix(2, 2, lambda a, b: (gradQ[a].T*gradQ[b])[0, 0] - gV[a, b]*sqQ/2)
    Ylow = gV*Yvec
    Jl = sp.Matrix([sum(TTv[a, b]*Yvec[b] for b in range(2)) - cc/r**2*(Qv.T*Qv)[0, 0]*Ylow[a] for a in range(2)])
    Ju = gVi*Jl
    divY = (D(r**3*Ju[0], v) + D(r**3*Ju[1], r))/r**3
    repv = {}
    for i in range(2):
        repv[D(Qv[i], v, r)] = Qvr[i]
        repv[D(Qv[i], r, v)] = Qvr[i]
    divY = sp.expand(divY.subs(repv).doit())
    rep3 = {}
    for dd in divY.atoms(sp.Derivative):
        rep3[dd] = sp.Symbol("d_" + str(dd).replace("(v, r)", "").replace("Derivative(", "").replace(")", "")
                             .replace(", ", "_").replace(" ", ""))
    for i in range(2):
        rep3[Qv[i]] = sp.Symbol("Q%d" % (i + 1))
    divYh = sp.expand(sp.expand(divY.xreplace(rep3)).subs(r, rh))
    Qs = sp.Matrix([rep3[Qv[0]], rep3[Qv[1]]])
    Qvs = sp.Matrix([rep3[D(Qv[0], v)], rep3[D(Qv[1], v)]])
    Qrs = sp.Matrix([rep3[D(Qv[0], r)], rep3[D(Qv[1], r)]])
    Yh = Yvec.subs(r, rh)
    nablaY = Yh[0]*Qvs + Yh[1]*Qrs
    template = (sigma/2*(Qvs.T*Qvs)[0, 0] + 2/rh*(Qrs.T*Qrs)[0, 0] + 6/rh*(Qrs.T*Qvs)[0, 0]
                + (sigma/2 + 1/rh)*(Qs.T*Kmat*Qs)[0, 0]/rh**2 + cc*(sigma/mu + 2/mu**sp.Rational(3, 2))*(Qs.T*Qs)[0, 0]
                + 2*cc/mu*(Qs.T*Qrs)[0, 0] + (nablaY.T*(Acal*Qs - cc/rh**2*Qs))[0, 0] + 2*(Qrs.T*betaM*Qrs)[0, 0])
    rest = sp.expand(divYh - template)
    chk("at r = r_h, div(T_ab[Q] Y^b - c |Q|^2 Y_a/r^2) = (sigma/2)|Q_v|^2 + (2/r_h)|Q_R|^2 + (6/r_h) Q_R.Q_v + "
        "(sigma/2 + 1/r_h)|nabla-slash Q|^2 + c (sigma/mu + 2/mu^(3/2))|Q|^2 + (2c/mu) Q.Q_R "
        "+ nabla_Y Q.(Acal Q - c Q/r^2) "
        "+ 2 Q_R.beta.Q_R ([Hun19] (2.13) with 2M -> r_h; the beta term has Hung's sign)", rest == 0)
    # (e) the T-current with the s^-delta weight, formal: J = r^-delta (T_ab[Q] - Q.V_inf.Q g_ab/(2 r^2)) T^b on the
    #     quotient (angular energy in T), with box-hat Q = V Q + U Q, V = K/r^2 + ... as the full potential
    delta = sp.Symbol("delta", positive=True)
    Pd = sp.Matrix([sp.Function("P1")(t, r), sp.Function("P2")(t, r)])
    Ud = sp.Matrix([sp.Function("U1")(t, r), sp.Function("U2")(t, r)])
    Vfd = sp.Matrix(2, 2, lambda i, j: sp.Function("V%d%d" % (i + 1, j + 1))(r))
    # box-hat P = V P + U with box-hat = -f^-1 d_t^2 + f d_r^2 + (f' + 3f/r) d_r, so that
    # d_t^2 P = f (f P_rr + (f' + 3f/r) P_r - V P - U)
    Pdtt = (f*(f*Pd.diff(r, 2) + (_fp + 3*f/r)*Pd.diff(r) - Vfd*Pd - Ud)).applyfunc(sp.expand)
    gradd = [Pd.diff(t), Pd.diff(r)]
    sqd = sum(gQi[a, b]*(gradd[a].T*gradd[b])[0, 0] for a in range(2) for b in range(2)) + (Pd.T*Vc*Pd)[0, 0]/r**2
    TTd = sp.Matrix(2, 2, lambda a, b: (gradd[a].T*gradd[b])[0, 0] - gQ[a, b]*sqd/2)
    Tvec = sp.Matrix([1, 0])
    Jd_low = sp.Matrix([r**(-delta)*sum(TTd[a, b]*Tvec[b] for b in range(2)) for a in range(2)])
    Jd_up = gQi*Jd_low
    divd = (D(r**3*Jd_up[0], t) + D(r**3*Jd_up[1], r))/r**3
    divd = sp.expand(divd.subs({D(Pd[i], t, 2): Pdtt[i] for i in range(2)}).doit())
    LPd = sp.Matrix([Lop(Pd[i]) for i in range(2)])
    LbPd = sp.Matrix([D(Pd[i], t) - f*D(Pd[i], r) for i in range(2)])
    templ = (delta/4*r**(-1 - delta)*((LbPd.T*LbPd)[0, 0] - (LPd.T*LPd)[0, 0])
             + r**(-delta)*(Pd.diff(t).T*((Vfd - Vc/r**2)*Pd + Ud))[0, 0])
    restd = sp.expand(divd - templ)
    chk("div(r^-delta (T_ab[Q] - Q.V_inf.Q g_ab/(2 r^2)) T^b) = (delta/4) r^(-1-delta) (|nabla_L-bar Q|^2 "
        "- |nabla_L Q|^2) "
        "+ r^-delta nabla_T Q . ((V - V_inf/r^2) Q + U Q) ([Hun19] p. 23, the J_{H,delta} current)",
        not _lin_syms(restd, list(Pd) + list(Ud) + list(Vfd), (t, r)))
    # (g) the k-degree: A - K/r^2, its regular form A' - K/r^2 and A - A_main/r^2 are of degree at most one in k, and
    #     A' - K/r^2 is finite at the horizon -- one angular derivative bounds them (N1STAR-PROOF.md (10.9))
    A, _, _ = _hung_rows(1)
    Kmat7 = sp.diag(kk**2, kk**2, kk**2, kk**2 - 2, kk**2 - 6, kk**2, kk**2 - 2)

    def kdeg(M):
        out = []
        for x in M:
            x = sp.cancel(x)
            if x != 0:
                num, den = sp.fraction(x)
                out.append(sp.Poly(num, kk).degree() - sp.Poly(den, kk).degree())
        return max(out)
    Amain = (A*r**2).applyfunc(lambda x: sp.cancel(sp.limit(x, r, sp.oo)))
    Rm = sp.eye(7)
    Rm[5, 0], Rm[5, 5], Rm[6, 3], Rm[6, 6] = 1, f**2, 1, f
    Ap = (Rm.inv()*(A*Rm - f*Rm.diff(r, 2) - (_fp + 3*f/r)*Rm.diff(r))).applyfunc(sp.cancel)
    Ap[5, 5] = sp.cancel(Ap[5, 5] + (2*_fp/f)*(2*f**2*_fp)/f**2)
    Ap[6, 6] = sp.cancel(Ap[6, 6] + (_fp/f)*(f*_fp)/f)
    Acal = (Ap - Kmat7/r**2).applyfunc(sp.cancel)
    ok = kdeg(A - Kmat7/r**2) <= 1 and kdeg(Acal) <= 1 and kdeg(A - Amain/r**2) <= 1
    ok &= all(sp.fraction(x)[1].subs(r, rh) != 0 for x in Acal)
    chk("A - K/r^2, its horizon-regular form A' - K/r^2 and the sub-leading part A - A_main/r^2 have entries of "
        "degree at most one in k, and A' - K/r^2 is finite at r = r_h: one angular derivative bounds them ((10.9))", ok)
    # (h) l = 0: the sub-leading part decays as O(mu/r^4) and the rescaling diag(sqrt2, 1, sqrt2, sqrt2) makes A0_main
    #     symmetric, so V_inf = A0_main + 3/4 has the eigenvalues 3/4, 3/4, 15/4, 35/4
    A0, ok0 = _hung_l0(1)
    A0main = (A0*r**2).applyfunc(lambda x: sp.cancel(sp.limit(x, r, sp.oo)))
    sub0 = ((A0 - A0main/r**2)*r**4).applyfunc(lambda x: sp.cancel(sp.limit(x, r, sp.oo)))
    D0 = sp.diag(sp.sqrt(2), 1, sp.sqrt(2), sp.sqrt(2))
    S0 = (D0*A0main*D0.inv()).applyfunc(sp.simplify)
    cp0 = sp.expand((S0 + sp.Rational(3, 4)*sp.eye(4)).charpoly(lam).as_expr())
    want0 = sp.expand((lam - sp.Rational(3, 4))**2*(lam - sp.Rational(15, 4))*(lam - sp.Rational(35, 4)))
    chk("l = 0: A0 - A0_main/r^2 = O(mu/r^4), diag(sqrt2, 1, sqrt2, sqrt2) A0_main diag(...)^-1 is symmetric, "
        "and V_inf = A0_main + 3/4 has the eigenvalues 3/4, 3/4, 15/4, 35/4 > 0 (Proposition 10.3's remark)",
        ok0 and all(x.is_finite for x in sub0) and S0 == S0.T and sp.expand(cp0 - want0) == 0)
    # (f) the angular eigenvalues on S^3 of the one-form S_th dth and of the traceless tensor S_AB: k^2 - 2 and k^2 - 6
    gam = sp.diag(1, cs**2, sn**2)
    gami = gam.inv()
    Y3 = [th, p1, p2]
    Gs = [[[sp.simplify(sum(gami[i, m]*(sp.diff(gam[m, j], Y3[q]) + sp.diff(gam[m, q], Y3[j])
                                        - sp.diff(gam[j, q], Y3[m])) for m in range(3))/2)
            for q in range(3)] for j in range(3)] for i in range(3)]
    xi = [_Sp, 0, 0]
    Dxi = [[sp.diff(xi[j], Y3[q]) - sum(Gs[m][q][j]*xi[m] for m in range(3)) for j in range(3)] for q in range(3)]
    DDxi = [[[sp.diff(Dxi[q][j], Y3[s_]) - sum(Gs[m][s_][q]*Dxi[m][j] + Gs[m][s_][j]*Dxi[q][m] for m in range(3))
              for j in range(3)] for q in range(3)] for s_ in range(3)]
    lap1 = [sum(gami[q, s_]*DDxi[s_][q][j] for q in range(3) for s_ in range(3)) for j in range(3)]
    e1 = _red(lap1[0] - (-kk**2 + 2)*_Sp)
    ok1 = all(sp.simplify(_at_angle(e1.xreplace({_Sp: _s1}).xreplace({_S: _s0}), c0, s0)) == 0 for c0, s0 in _PYTH)
    ok1 &= all(sp.simplify(_at_angle(_red(lap1[j]).xreplace({_Sp: _s1}).xreplace({_S: _s0}), c0, s0)) == 0
               for j in (1, 2) for c0, s0 in _PYTH)
    DDS = sp.diag(sp.diff(_S, th, 2), -cs*sn*_Sp, sn*cs*_Sp)
    SAB = DDS/kk**2 + gam*_S/3
    DS = [[[sp.diff(SAB[i, j], Y3[q]) - sum(Gs[m][q][i]*SAB[m, j] + Gs[m][q][j]*SAB[i, m] for m in range(3))
            for j in range(3)] for i in range(3)] for q in range(3)]
    DDSab = [[[[sp.diff(DS[q][i][j], Y3[s_]) - sum(Gs[m][s_][q]*DS[m][i][j] + Gs[m][s_][i]*DS[q][m][j]
                                                       + Gs[m][s_][j]*DS[q][i][m] for m in range(3))
                for j in range(3)] for i in range(3)] for q in range(3)] for s_ in range(3)]
    lap2 = sp.Matrix(3, 3, lambda i, j: sum(gami[q, s_]*DDSab[s_][q][i][j] for q in range(3) for s_ in range(3)))
    e2 = (lap2 - (-kk**2 + 6)*SAB).applyfunc(_red)
    ok2 = all(sp.simplify(_at_angle(e2[i, j].xreplace({_Sp: _s1}).xreplace({_S: _s0}), c0, s0)) == 0
              for i in range(3) for j in range(3) for c0, s0 in _PYTH)
    chk("on S^3 the rough Laplacian has eigenvalue -(k^2 - 2) on the one-form S_th dth and -(k^2 - 6) on the traceless "
        "tensor S_AB: the angular energies K = diag(k^2, k^2, k^2, k^2 - 2, k^2 - 6, k^2, k^2 - 2)", ok1 and ok2)
    return chk.ok


CHECKS = [("W1 the Lichnerowicz identity in the class, and Gamma[pi_X] = box X", w1, 1),
          ("W2 the l = 0 stationary one-form W* = dt/r^2 + sqrt(mu) dr/(r^3 f), regular at the horizon", w2, 1),
          ("W3 the gauge-fixed mass change K* = K + pi_{W**}, harmonic and linear in t", w3, 1),
          ("W4 the scalar gauge vector: three 1+1 wave equations per mode, sources in F, F_ab (l = 2, 4)", w4, 1),
          ("W5 the tensor type is in harmonic gauge already", w5, 1),
          ("W6 the gauge-vector system is triangular: S, then F_tr, then X_t and r X_L, X_r algebraic", w6, 1),
          ("W7 Hung's Proposition 4.2 in five dimensions: box H = A H + U H, the spectrum, the horizon, l = 0", w7, 1),
          ("W8 Hung's Proposition 4.1 in five dimensions: radiation field, p-current, red-shift, T-current, l = 0",
           w8, 1)]


def selftest(verbose=False):
    ok_all = True
    for name, fn, nc in CHECKS:
        t0 = time.time()
        good = fn(verbose=verbose)
        control = any(fn(control=k) for k in range(1, nc + 1))
        state = "PASS" if good and not control else "FAIL"
        ok_all &= state == "PASS"
        print(f"{name:<100} {state}  {time.time() - t0:.0f}s" + ("" if not control else "  (control passed: vacuous)"),
              flush=True)
    print(f"wavegauge5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            m = fn(control=k)
            caught += (not m)
            print(f"mutant {k} of {name[:2]}: {'caught' if not m else 'NOT caught'}")
    print(f"wavegauge5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    if "--l4" in sys.argv:
        w6.__defaults__ = (0, False, (2, 4))
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest("--verbose" in sys.argv) else 1)
