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
  W7 (computed, exact) Hung's Proposition 4.2 in five dimensions.  In his components -- H1 = (h_tt + f^2 h_rr)/2 +
     ((1 - f)/2) trs h, H2 = trs h/sqrt3, H3 = (h_tt/f - f h_rr)/2, H6 = f h_tr + ((1 - f)/2) trs h, H4 = f k h_rth/(r
     S'), H7 = k h_tth/(r S'), hhat_ij = 2 r^2 H5 S_ij; (1 - f)/2 = mu/(2 r^2) is his M/r -- with the gauge condition
     Gamma[h] = 0 admixed as 2 f f' Gamma_r in rows 1 and 6 and k f' Gamma_th/r in rows 4 and 7 (his Appendix C), the
     Lichnerowicz equation is box_l H = A H + U H with A zeroth order and rational in r, mu, k and U = (2f'/f) nabla_L
     (H6 - H1) in row 6, (f'/f) nabla_L (H7 - H4) in row 7 and nothing else (his U with 2M/r^2 -> f').  r^2 A_main at
     k^2 = l(l+2) has the eigenvalues (l+a)(l+a+2), a = -2, -1, 0, 0, 0, 1, 2 (his Lemma 4.3 with (l+a)(l+a+1)):
     semi-positive for l >= 2; A - A_main/r^2 = O(mu/r^4).  In the regular variables H6' = (H6 - H1)/f^2 =
     -h(L', L')/2, H7' = (H7 - H4)/f every coefficient is regular at the horizon, rows 1-5 carry no first-order term,
     rows 6', 7' carry 2f' nabla_L' H6' and f' nabla_L' H7' and no nabla_L (his 4M/r^2, 2M/r^2).  At l = 0 (H1, H2,
     H3, H6) the eigenvalues are 0, 0, 3, 8.  The harmonic is kept symbolic with its equation S'' = -2 cot 2th S' -
     k^2 S applied and the angle evaluated exactly at (cos, sin) = (3/5, 4/5) and (5/13, 12/13); every coefficient is a
     rational function, cancelled.  Control: the sign of the gauge admixture reversed (first-order terms survive in rows
     1-5).  hung4.py is the four-dimensional control: the same instrument on Schwarzschild reproduces his printed rows.

READ (alphaXiv, 2026-10-20).  [Hun19] P.-K. Hung, arXiv:1909.06733v1, "The linear stability of the Schwarzschild
spacetime in the harmonic gauge: even part": abstract ("the energy decays at a rate tau^{-2+} for the solution of the
linearized Einstein equation after subtracting its spherically symmetric part ... The spherically symmetric part
converges to a linear combination of two special solutions.  One is the gauge-fixed mass change solution [19].  The
other is the deformation tensor of a stationary one form"); (1.3)-(1.5) pp. 2; Theorems 1.1-1.4 pp. 2-3; section 4.2,
(4.10)-(4.13), (4.21) p. 26-27 (the gauge vector to the Regge-Wheeler gauge and its wave equations with the Zerilli
source); (8.1) p. 58 W* = dt/r + 2M dr/(r^2 f); (8.38)-(8.39) p. 69 W** and K*.  READ 2026-10-21 (alphaXiv) for W7:
section 4.1 pp. 17-25 (Propositions 4.1, 4.2, A, B, U, Lemma 4.3, the red-shift paragraph p. 23 with H6', H7');
Appendix A pp. 70-71 ((A.3)-(A.8)); Appendix C pp. 75-79 ((C.1)-(C.12), (ME1)-(ME7), (HG1)-(HG3), the seven rows).

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


def _hung_rows(sign=1):
    """box H_i = sum_j A_ij H_j + U_i for Hung's seven components on five-dimensional Tangherlini, from the
    Lichnerowicz components LW and the gauge one-form Gamma (admixtures times sign): returns A (7x7, rational in
    r, mu, k), the first-order residuals of the seven rows ({(j, nt, nr): coefficient} each) after the nabla_L terms
    rho_6 L(H6 - H1), rho_7 L(H7 - H4) with rho_6 = 2f'/f, rho_7 = f'/f are removed, and the second-order residuals"""
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
    return A, first, second


def _hung_l0(sign=1):
    """the l = 0 sector (H1, H2, H3, H6; S = 1): the zeroth-order matrix after the same admixtures"""
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


CHECKS = [("W1 the Lichnerowicz identity in the class, and Gamma[pi_X] = box X", w1, 1),
          ("W2 the l = 0 stationary one-form W* = dt/r^2 + sqrt(mu) dr/(r^3 f), regular at the horizon", w2, 1),
          ("W3 the gauge-fixed mass change K* = K + pi_{W**}, harmonic and linear in t", w3, 1),
          ("W4 the scalar gauge vector: three 1+1 wave equations per mode, sources in F, F_ab (l = 2, 4)", w4, 1),
          ("W5 the tensor type is in harmonic gauge already", w5, 1),
          ("W6 the gauge-vector system is triangular: S, then F_tr, then X_t and r X_L, X_r algebraic", w6, 1),
          ("W7 Hung's Proposition 4.2 in five dimensions: box H = A H + U H, the spectrum, the horizon, l = 0", w7, 1)]


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
