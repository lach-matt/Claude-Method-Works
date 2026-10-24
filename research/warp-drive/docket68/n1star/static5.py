#!/usr/bin/env python3
"""static5.py -- the stationary solutions of the linearized Einstein equation on five-dimensional Tangherlini, the input
[Hin26] Proposition 8.11 takes from [AHW24] Theorem 6.1(2) on Kerr (N1STAR-PROOF.md section 10.33; ROUTES-OPEN.md 4.34;
D90).  Labels: computed (exact, sympy), deduced, READ.

[AHW24] (arXiv:2207.12952v1) Theorem 6.1 (p. 35): "Let 0 < a < m, sigma in C, Im sigma >= 0, and suppose g-dot = e^(-i
sigma t*) h-tilde, h-tilde in H-bar_b^(oo,q)(X; S^2 ...), q in (-3/2, -1/2) is an outgoing mode solution of the
linearized Einstein equation D Ric(g-dot) = 0.  Then there exist parameters m-dot in R, a-dot in R^3, and an outgoing
1-form omega in H-bar_b^(oo,q-1) such that g-dot - g-dot_(m,a)(m-dot, a-dot) = delta* omega."  It is one statement,
with no numbered parts; its case sigma = 0, which [Hin26] cites as Theorem 6.1(2), is what [Hin26] Proposition 8.11's
kernel count uses (N1STAR-PROOF.md 10.32(c)).  On five-dimensional Tangherlini, g = -f
dt^2 + dr^2/f + r^2 gamma, f = 1 - mu/r^2, it is computed here at sigma = 0 through the decomposition of [KI03] (H.
Kodama and A. Ishibashi, arXiv:hep-th/0305147v3; n = 3, K = 1), with the harmonics at a point of S^3 and the reduced
equations of gmodes5.py (G1-G4), there at sigma != 0, here with every coefficient independent of t.  The candidates the
statement leaves are the mass and the six rotations of so(4); everything else must be pure gauge.

  S1 (computed, exact) The tensor type, l >= 2.  For h_ij = 2 r^2 H(r) T_ij: D Ric(h)_ab = D Ric(h)_ai = 0 and D
     Ric(h)_ij = -r^2 ((1/r^3)(r^3 f H')' - l(l + 2) H/r^2) T_ij; Phi = r^(3/2) H turns it into f (f Phi')' = V_T Phi,
     V_T = (f/r^2)(l(l + 2) + 3/4 + 9 mu/(4 r^2)), V_T/f > 0 on r >= r_h, which is what the identity (f Phi Phi')' = f
     Phi'^2 + V_T Phi^2/f on solutions, true for any f and V_T, needs; the exponents of H are l, -(l + 2) at infinity
     and 0, 0 at r_h (so a second solution there carries a logarithm). Control: Phi = r^(1/2) H, where a
     first-derivative term survives.
  S2 (computed, exact) The vector type, l >= 2.  With f_t, f_r, H_T of r: E_r = (k_V^2 - 2) F_r/(2 r^2), E_T = -k_V (r^2
     f F_r)'/(2 r^3) and, F_t = r y, E_t = -(f (r^5 y')' - (k_V^2 - 2) r^3 y)/(2 r^4), k_V^2 - 2 = l(l + 2) - 3 >= 5,
     the sign the identity (r^5 y y')' = r^5 y'^2 + (k_V^2 - 2) r^3 y^2/f on solutions needs; the exponents of f_t = r y
     are l and -(l + 2) at infinity; in ingoing coordinates (dt = dv - dr/f) h_vi = r f_t V_i and h_ri = r (f_r - f_t/f)
     V_i.  Control: l = 1 (k_V^2 = 2), where E_r vanishes and F_r is not forced.
  S3 (computed, exact) The scalar type, l >= 2.  E_tr = k^2 F_tr/(2 r^2) and E_T = -(k^2/(4 r^2))(f F_rr - F_tt/f + 2
     F); in [KI03]'s X = r(-F_tt/f - 2 F), Y = r(f F_rr - 2 F) (E_T solved), E_r and the combination of E_tt, E_rr, E_L
     free of second derivatives give the flow Y' = mu (X - Y)/(r (r^2 - mu)) ([KI03] (2.24b) at sigma = 0) and X' = ...,
     on which all four even equations vanish: [KI03] section 4's static system (4.2) at n = 3 (p. 11), identically;
     Z~ := (f r^2/k^2)(X' - X/r - (f'/f - 2/r) Y) ((2.24a) at sigma = 0) has Z~' = X ((2.24c)); Phi := (3 Z~ - r (X +
     Y))/(r^(1/2) H) solves f (f Phi')' = V_S Phi with G3's V_S, is [KI03]'s static master variable (4.3), (Q_Y X -
     Q_X Y)/(2 k^2 r^(1/2) f' H), identically (the forty-second verifier; D92), and det[r^(1/2) Phi; r^(1/2) Phi'] =
     r^3/(k^2 mu); 3 Z~ - r (X + Y) is a combination of X and Y with coefficients
     polynomials in r of degrees 2 and 4 over k^2 mu r; r^2 V_S -> l(l + 2) + 3/4 at infinity, exponents 1/2 +- (l + 1);
     and with F_tr = 0, in ingoing components, X = r (F_vr - 2 F) and Y = r (f F'_rr + F_vr - 2 F).  Controls: Phi
     without the factor 1/H; [KI03]'s Q_X and Q_Y exchanged in (4.3) (D94).
  S4 (computed, exact) Scalar l = 0.  delta*(A_t dt + A_r dr) shifts H_L by f A_r/(2 r) and f_tr by (f/2)(A_t/f)'; f_tr
     enters no stationary equation; at H_L = 0 the equations give F_tt'' = -3 F_tt'/r and F_rr algebraic in F_tt, F_tt',
     so the stationary solutions are the span of (F_tt, F_rr) = (f, 0), the time rescaling t -> (1 + c) t, and (1/r^2,
     1/(r^2 f^2)), the mass; r^-2 (dt + dr/f)^2 solves, and is r^-2 dv^2 in ingoing coordinates.  Control: (1/r^2, 0).
  S5 (computed, exact) Vector l = 1 (V Killing).  D Ric(h)_ab = 0, E_r = 0 and E_t = -f (r^5 y')'/(2 r^4), so f_t = a r
     + b r^-3 with f_r free (the gauge (r/2) B'); f_t = a r is delta*(2 a t r^2 V_i dz^i) and f_t = r^-3, f_r = r^-3/f
     is r^-2 V_i dz^i dv in ingoing coordinates, h_ri = 0: the linearized rotation, regular.  Control: f_r = 0, singular
     at r_h.
  S6 (computed, exact) Scalar l = 1 (D_i D_j S = -gamma_ij S).  The stationary shifts of f_tt, f_t and H_L are free of
     derivatives with determinant -mu (r^2 - mu)/(4 r^6), so f_tt = f_t = H_L = 0 is reached; then the stationary
     equations force f_tr = f_rr = f_r = 0 (rank 3 of 3); and the shifts of f_rr and f_r are (A_r' + mu A_r/(r (r^2 -
     mu))) and (r^2 B' - 3^(1/2) A_r)/(2 r).  Control: f_t left free, where the rank is short.

Deduced, not computed here (N1STAR-PROOF.md 10.33): [AHW24] Theorem 6.1(2) on five-dimensional Tangherlini -- every
stationary solution of D Ric(h) = 0 smooth across the future horizon and O(r^-eps) at infinity, 0 < eps < 1, conormally,
is g-dot(mu-dot, A) + delta* omega with omega stationary, smooth across the horizon and O(r^(1 - eps)) -- by the energy
identities of S1-S3 with the potentials of gmodes5.py G5, the exponents, and the gauge 1-forms; and with it [Hin26]
Proposition 8.11 at Tangherlini, and near it on a reading (10.33(f)).

READ.  [AHW24] (L. Andersson, D. Hafner, B. F. Whiting, arXiv:2207.12952v1) pp. 1, 35 (Theorem 6.1), 41 (section 6.4,
its proof); [Hin26] pp. 155-157 (Proposition 8.11 and its proof, Corollary 8.13's proof); [KI03] pp. 4-10 ((2.1)-(2.24),
(3.1)-(3.7)), 11 ((4.1)-(4.3)), 13-15 ((5.1)-(5.17)); alphaXiv, 2026-10-23 and 2026-10-24.

sympy.  python3 static5.py [--selftest | --mutants]   (--verbose lists every sub-check)
"""
import sys
import time

import sympy as sp

from damping5 import Checklist
from gmodes5 import (t, r, mu, N, f, gam, gami, K, atpt, dric, dstar, jets, derivs, cov1, cov2, lap2, scalar_harmonic,
                     scalar_parts, scalar_E, vector_E, match, zero, algebraic_part, FN)

rh = sp.sqrt(mu)
lv = sp.Symbol("l", positive=True)


def static(e, funcs):
    """e with every f(t, r) of funcs replaced by f(r)"""
    return sp.sympify(e).subs({F: sp.Function(F.func.__name__)(r) for F in funcs}).doit()


def ef(h):
    """the components in ingoing coordinates (v, r, z) of a stationary h given in (t, r, z): dt = dv - dr/f"""
    J = sp.eye(N)
    J[0, 1] = -1 / f
    return (J.T * h * J).applyfunc(sp.cancel)


def exps_inf(op):
    """the exponents s at infinity of op (normalized as d^2/dr^2 + ...): the limit of r^2 op(r^s)/r^s, a polynomial in
    s"""
    s = sp.Symbol("s")
    e = sp.expand(sp.cancel(op(r**s) / r**s))
    return sp.Poly(sp.expand(sp.limit(e * r**2, r, sp.oo)), s), s


def exps_horizon(op):
    """the indicial polynomial of op at r = r_h: s (s - 1) + p0 s + q0, p0 = lim (r - r_h) a1/a2, q0 = lim (r - r_h)^2
    a0/a2 for op(U) = a2 U'' + a1 U' + a0 U"""
    U, s = sp.Function("U")(r), sp.Symbol("s")
    D2, D1, D0 = sp.symbols("D2 D1 D0")
    e = sp.expand(op(U).subs(sp.Derivative(U, (r, 2)), D2).subs(sp.Derivative(U, r), D1).subs(U, D0))
    a2, a1, a0 = e.coeff(D2), e.coeff(D1), e.coeff(D0)
    p0 = sp.limit(sp.cancel((r - rh) * a1 / a2), r, rh)
    q0 = sp.limit(sp.cancel((r - rh)**2 * a0 / a2), r, rh)
    return sp.Poly(s * (s - 1) + p0 * s + q0, s), s


def has_inv_f(e):
    """True if e carries a power of (r^2 - mu) in its denominator"""
    return sp.denom(sp.factor(sp.cancel(e))).has(mu)


# ------------------------------------------------------------------------------------------------- S1
def s1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    kT = K[0]
    H = sp.Function("H")(r)
    T = [[None] * 3 for _ in range(3)]
    syms = []
    for i in range(3):
        for j in range(i, 3):
            p, js = jets(f"T{i}{j}", 2)
            T[i][j] = T[j][i] = p
            syms += js
    tr = sum(gami[i, j] * T[i][j] for i in range(3) for j in range(3))
    DT = cov2(T)
    div = [sum(gami[i, k] * DT[k][i][j] for i in range(3) for k in range(3)) for j in range(3)]
    L2 = lap2(T)
    cons = derivs(tr, 2) + [atpt(L2[i][j] + kT**2 * T[i][j]) for i in range(3) for j in range(i, 3)]
    cons += sum((derivs(q, 1) for q in div), [])
    sol = sp.solve(cons, syms, dict=True)[0]
    h = sp.zeros(N, N)
    for i in range(3):
        for j in range(3):
            h[2 + i, 2 + j] = 2 * r**2 * H * T[i][j]
    if control == 0:
        Rh = dric(h).subs(sol)
        lam = -r**2 * (sp.diff(r**3 * f * sp.diff(H, r), r) / r**3 - (kT**2 + 2) * H / r**2)
        ok = all(zero(Rh[m, n]) for m in range(2) for n in range(N))
        ok &= all(zero(Rh[2 + i, 2 + j] - lam * atpt(T[i][j]).subs(sol)) for i in range(3) for j in range(i, 3))
        chk("tensor type, stationary: D Ric(h)_ab = D Ric(h)_ai = 0, D Ric(h)_ij = -r^2 ((1/r^3)(r^3 f H')' - (k_T^2 + "
            "2) H/r^2) T_ij", ok)
    l = lv
    op = lambda u: sp.diff(r**3 * f * sp.diff(u, r), r) / r**3 - l * (l + 2) * u / r**2      # k_T^2 + 2 = l(l + 2)
    Phi = sp.Function("Phi")(r)
    VT = f / r**2 * (l * (l + 2) + sp.Rational(3, 4) + 9 * mu / (4 * r**2))
    pw = sp.Rational(3, 2) if control != 1 else sp.Rational(1, 2)
    master = zero(sp.expand(f * r**pw * op(r**-pw * Phi)) - (f * sp.diff(f * sp.diff(Phi, r), r) - VT * Phi))
    xs = sp.Symbol("x", nonnegative=True)                                          # x = mu/r^2 in [0, 1]
    pos = all(c > 0 for c in sp.Poly(sp.expand(VT / f * r**2).subs(mu, xs * r**2), l, xs).coeffs())
    pos &= not has_inv_f(VT / f)
    chk("Phi = r^(3/2) H: f (f Phi')' = V_T Phi, V_T = (f/r^2)(l(l + 2) + 3/4 + 9 mu/(4 r^2)); V_T/f > 0 and bounded "
        "on r >= r_h, the sign the identity (f Phi Phi')' = f Phi'^2 + V_T Phi^2/f on solutions needs", master and pos)
    if control == 0:
        P, s = exps_inf(op)
        roots_inf = set(sp.solve(P.as_expr(), s))
        Ph, sh = exps_horizon(op)
        chk(f"exponents of H: {sorted(roots_inf, key=str)} at infinity, the roots of {sp.factor(Ph.as_expr())} at r_h",
            roots_inf == {l, -l - 2} and sp.roots(Ph) == {0: 2})
    return chk.ok


# ------------------------------------------------------------------------------------------------- S2
def s2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    kV = K[1]
    cs, ok, gs, okg, (Ft, Fr, B), parts = vector_E(kV)
    ct, cr, cT = [p[0] for p in parts]
    v, w = sp.Function("v")(r), sp.Function("w")(r)
    sub = lambda e: static(e, [Ft, Fr]).subs({sp.Function("F_t")(r): r * v, sp.Function("F_r")(r): w}).doit()
    Et, Er, ET = [sub(cs[c]) for c in (ct, cr, cT)]
    k2 = kV**2 if control != 1 else 2
    Er, Et, ET = [e.subs(kV**2, k2) if control == 1 else e for e in (Er, Et, ET)]
    lam = k2 - 2
    okE = zero(Er - lam * w / (2 * r**2)) and zero(ET + kV * sp.diff(r**2 * f * w, r) / (2 * r**3))
    okE &= zero(Et + (f * sp.diff(r**5 * sp.diff(v, r), r) - lam * r**3 * v) / (2 * r**4))
    forced = not zero(lam)
    chk("vector type, stationary: E_r = (k_V^2 - 2) F_r/(2 r^2) (F_r = 0 forced at l >= 2), E_T = -k_V (r^2 f F_r)'/(2 "
        "r^3), E_t = -(f (r^5 y')' - (k_V^2 - 2) r^3 y)/(2 r^4) with F_t = r y", ok and okE and forced)
    if control == 0:
        l = lv
        lam_l = l * (l + 2) - 3
        P, s = exps_inf(lambda u: sp.diff(r**5 * sp.diff(u / r, r), r) / r**4 - lam_l * u / (r**2 * f))
        roots = set(sp.solve(P.as_expr(), s))
        low = sp.expand(lam_l.subs(l, l + 2))
        chk(f"k_V^2 - 2 = l(l + 2) - 3 >= 5 at l >= 2, the sign the identity (r^5 y y')' = r^5 y'^2 + (k_V^2 - 2) r^3 "
            f"y^2/f on solutions needs; the exponents of f_t = r y at infinity {sorted(roots, key=str)}",
            roots == {l, -l - 2} and all(c > 0 for c in sp.Poly(low, l).coeffs()))
        Vp = sp.symbols("V0:3")
        h = sp.zeros(N, N)
        ft, fr = sp.symbols("f_t f_r")
        for i in range(3):
            h[0, 2 + i] = h[2 + i, 0] = r * ft * Vp[i]
            h[1, 2 + i] = h[2 + i, 1] = r * fr * Vp[i]
        he = ef(h)
        okef = all(zero(he[0, 2 + i] - r * ft * Vp[i]) and zero(he[1, 2 + i] - r * (fr - ft / f) * Vp[i])
                   for i in range(3))
        chk("ingoing coordinates: h_vi = r f_t V_i and h_ri = r (f_r - f_t/f) V_i", okef)
    return chk.ok


# ------------------------------------------------------------------------------------------------- S3
def s3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    k = K[2]
    cs, ok, gs, okg, parts = scalar_E(k)
    names = {"c_tt": "tt", "c_tr": "tr", "c_rr": "rr", "c_t": "t", "c_r": "r", "c_L": "L", "c_T": "T"}
    funcs = [sp.Function(nm)(t, r) for nm in FN]
    E = {names[p[0].name]: static(cs[p[0]], funcs) for p in parts}
    Ftt, Ftr, Frr, F = [sp.Function(nm)(r) for nm in FN]
    if control == 0:
        okodd = zero(E["tr"] - k**2 * Ftr / (2 * r**2)) and not any(E[key].has(Ftr) for key in ("tt", "rr", "r", "L"))
        okT = zero(E["T"] + k**2 / (4 * r**2) * (f * Frr - Ftt / f + 2 * F))
        chk("scalar type, stationary: E_tr = k^2 F_tr/(2 r^2), F_tr in no even equation; E_T = -(k^2/(4 r^2))(f F_rr - "
            "F_tt/f + 2 F)", ok and okodd and okT)
    Xf, Yf = sp.Function("X")(r), sp.Function("Y")(r)
    sub = {Ftt: -f * (2 * Xf - Yf) / (3 * r), Frr: (-Xf + 2 * Yf) / (3 * r * f), F: -(Xf + Yf) / (6 * r)}
    Xs, Ys = sp.symbols("X0:3"), sp.symbols("Y0:3")

    def jet(e):
        e = sp.expand(sp.numer(sp.together(e.subs(sub).doit())))
        for F_, S_ in ((Xf, Xs), (Yf, Ys)):
            e = e.subs(sp.Derivative(F_, r, 2), S_[2]).subs(sp.Derivative(F_, r), S_[1]).subs(F_, S_[0])
        return sp.expand(e)
    J = {key: jet(E[key]) for key in ("tt", "rr", "r", "L", "T")}
    X0, X1, X2 = Xs
    Y0, Y1, Y2 = Ys
    a_, b_ = sp.symbols("a b")
    comb = sp.expand(a_ * J["tt"] + b_ * J["rr"] + J["L"])
    cw = sp.solve([comb.coeff(X2), comb.coeff(Y2)], [a_, b_], dict=True)[0]
    first = sp.expand(comb.subs(cw))
    M2 = sp.Matrix([[sp.cancel(q.coeff(v)) for v in (X1, Y1)] for q in (J["r"], first)])
    fl = sp.solve([J["r"], first], [X1, Y1], dict=True)[0]
    fl = {v_: sp.factor(e) for v_, e in fl.items()}

    def dr(e):
        return sp.cancel(sp.diff(e, r) + sp.diff(e, X0) * fl[X1] + sp.diff(e, Y0) * fl[Y1])
    sec = {X2: dr(fl[X1]), Y2: dr(fl[Y1])}
    allv = all(zero(J[key].subs(sec).subs(fl)) for key in ("tt", "rr", "r", "L", "T"))
    kiY = zero(fl[Y1] - sp.diff(f, r) / (2 * f) * (X0 - Y0))
    if control == 0:
        chk(f"in X, Y (E_T = 0 identically: {zero(J['T'])}): E_r and the combination of E_tt, E_rr, E_L free of second "
            f"derivatives solve for (X', Y') (determinant {sp.factor(M2.det())}); Y' = f'(X - Y)/(2 f) ([KI03] (2.24b) "
            f"at sigma = 0); all four even equations vanish on the flow",
            zero(J["T"]) and not zero(M2.det()) and kiY and allv)
    n = 3
    Zt = sp.cancel(f * r**2 / k**2 * (fl[X1] - (n - 2) / r * X0 - (sp.diff(f, r) / f - 2 / r) * Y0))
    m_ = k**2 - n
    x = mu / r**2
    H = m_ + 6 * x
    Q = (n**4 * (n + 1)**2 * x**3 + n * (n + 1) * (4 * (2 * n**2 - 3 * n + 4) * m_ + n * (n - 2) * (n - 4) * (n + 1))
         * x**2 - 12 * n * ((n - 4) * m_ + n * (n + 1) * (n - 2)) * m_ * x + 16 * m_**3 + 4 * n * (n + 2) * m_**2)
    VS = f * Q / (16 * r**2 * H**2)
    num = sp.expand(sp.cancel(n * Zt - r * (X0 + Y0)))
    Phi = num / (sp.sqrt(r) * (H if control != 1 else 1))
    P1 = dr(Phi)
    ME = sp.cancel((f * dr(f * P1) - VS * Phi) * sp.sqrt(r))
    Ps, P1s = sp.expand(sp.cancel(Phi * sp.sqrt(r))), sp.expand(sp.cancel(P1 * sp.sqrt(r)))
    det = sp.factor(sp.Matrix([[sp.cancel(Ps.coeff(v_)) for v_ in (X0, Y0)],
                               [sp.cancel(P1s.coeff(v_)) for v_ in (X0, Y0)]]).det())
    chk(f"Z~ := (f r^2/k^2)(X' - X/r - (f'/f - 2/r) Y) has Z~' = X on the flow; Phi = (3 Z~ - r (X + Y))/(r^(1/2) H) "
        f"solves f (f Phi')' = V_S Phi; det[r^(1/2) Phi; r^(1/2) Phi'] = {det}",
        zero(dr(Zt) - X0) and zero(ME) and zero(det - r**3 / (k**2 * mu)))
    if control in (0, 2):                               # [KI03] section 4, p. 11, at n = 3, K = 1, Lambda = 0 (D92)
        fp, fpp = sp.diff(f, r), sp.diff(f, r, 2)
        cXk = 2 * (n - 1) * (f - 1) / r**2 + 2 * fp / r - fp**2 / (2 * f) + 2 * fpp / n
        cYk = 2 * (f - 1) / r**2 + 2 * (n - 1) * fp / r - fp**2 / (2 * f) + 2 * (n - 1) * fpp / n - 2 * m_ / r**2
        QX = n * (n + 1)**2 * x**2 + 2 * ((3 * n - 1) * m_ - n * (n + 1)) * x - 4 * n * m_
        QY = n * (n - 1) * (n + 1) * x**2 - 2 * (n - 1) * (m_ + n * (n + 1)) * x
        if control == 2:
            QX, QY = QY, QX
        PhiKI = (QY * X0 - QX * Y0) / (2 * k**2 * sp.sqrt(r) * fp * H)
        chk("[KI03] section 4 (p. 11): the flow is their static system (4.2a), (4.2b), and Phi their (4.3), (Q_Y X - "
            "Q_X Y)/(2 k^2 r^(1/2) f' H), identically",
            zero(fl[X1] - (cXk * X0 - cYk * Y0) / fp) and kiY and zero(sp.cancel((Phi - PhiKI) * sp.sqrt(r))))
    if control == 0:
        cX, cY = [sp.factor(sp.cancel(num.coeff(v_) * k**2 * mu * r)) for v_ in (X0, Y0)]
        poly = [sp.Poly(c_, r).degree() for c_ in (cX, cY)] == [2, 4] and not any(has_inv_f(c_) for c_ in (cX, cY))
        lim = sp.factor(sp.limit(VS * r**2, r, sp.oo))
        P = sp.Poly(sp.expand(sp.Symbol("s") * (sp.Symbol("s") - 1) - lim.subs(k**2, lv * (lv + 2))), sp.Symbol("s"))
        roots = set(sp.solve(P.as_expr(), sp.Symbol("s")))
        Fvv, Fvr, Frr_ = sp.symbols("F_vv F_vr F'_rr")
        Fs_ = sp.Symbol("F")
        J1 = sp.eye(2)
        J1[0, 1] = -1 / f
        Ji = J1.inv()
        Fsch = (Ji.T * sp.Matrix([[Fvv, Fvr], [Fvr, Frr_]]) * Ji).applyfunc(sp.cancel)
        fvv = sp.solve(Fsch[0, 1], Fvv)[0]
        Xe = sp.cancel((r * (-Fsch[0, 0] / f - 2 * Fs_)).subs(Fvv, fvv))
        Ye = sp.cancel((r * (f * Fsch[1, 1] - 2 * Fs_)).subs(Fvv, fvv))
        reg = zero(Xe - r * (Fvr - 2 * Fs_)) and zero(Ye - r * (f * Frr_ + Fvr - 2 * Fs_))
        chk(f"3 Z~ - r (X + Y) = (({cX}) X + ({cY}) Y)/(k^2 mu r); r^2 V_S -> {lim}, exponents "
            f"{sorted(roots, key=str)} at infinity; with F_tr = 0 (F_vv = {fvv}) X = r (F_vr - 2 F), Y = r (f F'_rr + "
            f"F_vr - 2 F)",
            poly and roots == {lv + sp.Rational(3, 2), -lv - sp.Rational(1, 2)} and reg)
    return chk.ok


# ------------------------------------------------------------------------------------------------- S4
def s4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    Ftt, Frr, Ftr = [sp.Function(nm)(r) for nm in ("F_tt", "F_rr", "F_tr")]
    if control == 0:
        At, Ar = sp.Function("A_t")(r), sp.Function("A_r")(r)
        Mg = dstar([At, Ar, 0, 0, 0])
        okg = zero(Mg[2, 2] / (2 * r**2 * atpt(gam[0, 0])) - f * Ar / (2 * r))
        okg &= zero(Mg[0, 1] - f / 2 * sp.diff(At / f, r))
        chk("scalar l = 0: delta*(A_t dt + A_r dr) shifts H_L by f A_r/(2 r) and f_tr by (f/2)(A_t/f)'", okg)
    h = sp.zeros(N, N)
    h[0, 0], h[1, 1] = Ftt, Frr
    h[0, 1] = h[1, 0] = Ftr
    R = dric(h)
    eqs = [sp.numer(sp.together(R[m, n])) for (m, n) in ((0, 0), (1, 1), (2, 2))]
    T_, P_ = sp.symbols("T0:3"), sp.symbols("P0:3")

    def jet(e):
        e = sp.expand(e)
        for U, js in zip((Ftt, Frr), (T_, P_)):
            for j in (2, 1):
                e = e.subs(sp.Derivative(U, r, j), js[j])
            e = e.subs(U, js[0])
        return sp.expand(e)
    sol = sp.solve([jet(e) for e in eqs], [T_[2], P_[1], P_[0]], dict=True)
    if control == 0:
        absent = zero(R[0, 1]) and all(not q.has(Ftr) for q in eqs) and zero(R[3, 3] / atpt(gam[1, 1]) - R[2, 2])
        form = len(sol) == 1 and zero(sol[0][T_[2]] + 3 * T_[1] / r)
        chk(f"f_tr enters no stationary equation; at H_L = 0 they give F_tt'' = -3 F_tt'/r and F_rr = "
            f"{sp.factor(sol[0][P_[0]]) if sol else None}", absent and form)
    cands = [(f, 0), (1 / r**2, 1 / (r**2 * f**2))] if control != 1 else [(f, 0), (1 / r**2, 0)]
    solves = all(zero(q.subs({Ftt: a1, Frr: a2}).doit()) for a1, a2 in cands for q in eqs)
    indep = not zero(sp.Matrix([[c[0], sp.diff(c[0], r)] for c in cands]).det())
    chk("the stationary solutions are spanned by (F_tt, F_rr) = (f, 0), the time rescaling, and (1/r^2, 1/(r^2 f^2)), "
        "the mass", solves and indep)
    if control == 0:
        hm = sp.zeros(N, N)
        hm[0, 0], hm[0, 1], hm[1, 0], hm[1, 1] = 1 / r**2, 1 / (r**2 * f), 1 / (r**2 * f), 1 / (r**2 * f**2)
        he = ef(hm)
        okm = zero(he[0, 0] - 1 / r**2) and all(zero(he[m, n]) for m in range(N) for n in range(N) if (m, n) != (0, 0))
        chk("r^-2 (dt + dr/f)^2 solves (f_tr enters nothing) and is r^-2 dv^2 in ingoing coordinates", okm)
    return chk.ok


# ------------------------------------------------------------------------------------------------- S5
def s5(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    V, syms = [], []
    for i in range(3):
        p, js = jets(f"V{i}", 2)
        V.append(p)
        syms += js
    DV = cov1(V)
    sol = sp.solve(sum((derivs(DV[i][j] + DV[j][i], 1) for i in range(3) for j in range(i, 3)), []), syms,
                   dict=True)[0]
    i0 = [i for i in range(3) if atpt(V[i]).subs(sol) != 0][0]
    v, fr = sp.Function("v")(r), sp.Function("f_r")(r)
    if control == 0:
        h = sp.zeros(N, N)
        for i in range(3):
            h[0, 2 + i] = h[2 + i, 0] = r * (r * v) * V[i]
            h[1, 2 + i] = h[2 + i, 1] = r * fr * V[i]
        R = dric(h).subs(sol)
        Vi0 = atpt(V[i0]).subs(sol)
        Et, Er = R[0, 2 + i0] / (r * Vi0), R[1, 2 + i0] / (r * Vi0)
        ok = all(zero(R[m, n]) for m in range(2) for n in range(2)) and zero(Er)
        ok &= zero(Et + f * sp.diff(r**5 * sp.diff(v, r), r) / (2 * r**4))
        ok &= all(zero(R[2 + i, 2 + j]) for i in range(3) for j in range(3))
        sv = sp.dsolve(sp.diff(r**5 * sp.diff(v, r), r), v).rhs
        B = sp.Function("B")(t, r)
        g_ = dstar([0, 0] + [r**2 * B * V[i] for i in range(3)]).subs(sol)
        okB = zero(g_[0, 2 + i0] - r**2 / 2 * sp.diff(B, t) * Vi0)
        okB &= zero(g_[1, 2 + i0] - r**2 / 2 * sp.diff(B, r) * Vi0)
        chk(f"vector l = 1: D Ric(h)_ab = 0, E_r = 0, E_t = -f (r^5 y')'/(2 r^4), D Ric(h)_ij = 0: y = {sv}, f_t = r y; "
            f"delta*(r^2 B V) shifts f_t by (r/2) d_t B and f_r by (r/2) B', so f_t = a r is delta*(2 a t r^2 V)",
            ok and okB and sp.simplify(sp.diff(r**5 * sp.diff(sv, r), r)) == 0)
    Vp = sp.symbols("V0:3")
    hr = sp.zeros(N, N)
    frot = 1 / (r**3 * f) if control != 1 else 0
    for i in range(3):
        hr[0, 2 + i] = hr[2 + i, 0] = r * r**-3 * Vp[i]
        hr[1, 2 + i] = hr[2 + i, 1] = r * frot * Vp[i]
    he = ef(hr)
    reg = all(zero(he[0, 2 + i] - r**-2 * Vp[i]) and zero(he[1, 2 + i]) for i in range(3))
    chk("the rotation f_t = r^-3, f_r = r^-3/f is r^-2 V_i dz^i dv in ingoing coordinates, h_ri = 0", reg)
    return chk.ok


# ------------------------------------------------------------------------------------------------- S6
def s6(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    k = sp.sqrt(3)
    S, DS, DDS, sol = scalar_harmonic(k, order=2, hessian=True)
    parts = [p for p in scalar_parts(k, S, DS, DDS) if p[0].name != "c_T"]
    c = dict((p[0].name, p[0]) for p in parts)
    At, Ar, B = [sp.Function(nm)(r) for nm in ("A_t", "A_r", "B")]
    gs, okg = match(dstar([At * S, Ar * S] + [r**2 * B * (-DS[i] / k) for i in range(3)]), sol, parts)
    if control == 0:
        lin = [gs[c[nm]] for nm in ("c_tt", "c_t", "c_L")]
        Jm = sp.Matrix([[sp.cancel(q.coeff(U)) for U in (At, Ar, B)] for q in lin])
        derivfree = all(not q.has(sp.Derivative) for q in lin)
        gdet = sp.factor(Jm.det())
        shifts = zero(gs[c["c_rr"]] - (sp.diff(Ar, r) + mu * Ar / (r * (r**2 - mu))))
        shifts &= zero(gs[c["c_r"]] - (r**2 * sp.diff(B, r) - k * Ar) / (2 * r))
        chk(f"scalar l = 1: the stationary shifts of f_tt, f_t, H_L are free of derivatives, determinant {gdet}; the "
            f"shifts of f_rr and f_r are A_r' + mu A_r/(r (r^2 - mu)) and (r^2 B' - 3^(1/2) A_r)/(2 r)",
            okg and derivfree and zero(gdet + mu * (r**2 - mu) / (4 * r**6)) and shifts)
    ftr, frr, fr, ft = [sp.Function(nm)(r) for nm in ("f_tr", "f_rr", "f_r", "f_t")]
    h = sp.zeros(N, N)
    h[0, 1] = h[1, 0] = ftr * S
    h[1, 1] = frr * S
    for i in range(3):
        Si = -DS[i] / k
        h[1, 2 + i] = h[2 + i, 1] = r * fr * Si
        if control == 1:
            h[0, 2 + i] = h[2 + i, 0] = r * ft * Si
    funcs = [ftr, frr, fr] + ([ft] if control == 1 else [])
    Es, okE = match(dric(h), sol, parts)
    eqs = [sp.numer(sp.together(Es[p[0]])) for p in parts if not zero(Es[p[0]])]
    rk, free = algebraic_part(eqs, funcs)
    chk(f"at f_tt = f_t = H_L = 0 the stationary equations force (f_tr, f_rr, f_r) = 0 (rank {rk} of {len(funcs)}; "
        f"pivot factors free of r: {sorted(map(str, free))})", okE and rk == len(funcs) and not free)
    return chk.ok


CHECKS = [("S1 the tensor type, l >= 2: the stationary equation, Phi, V_T/f > 0, exponents", s1, 1),
          ("S2 the vector type, l >= 2: E_r forces F_r = 0, (r^5 v')' = (k_V^2 - 2) r^3 v/f, exponents, horizon", s2, 1),
          ("S3 the scalar type, l >= 2: F_tr = 0, the flow, Z~, the master equation at sigma = 0, det, horizon", s3, 2),
          ("S4 scalar l = 0: the time rescaling and the mass, f_tr pure gauge, the mass regular in ingoing form", s4, 1),
          ("S5 vector l = 1: f_t = a r + b r^-3, the rigid rotation's gauge, the rotation regular, ingoing", s5, 1),
          ("S6 scalar l = 1: the stationary gauge f_tt = f_t = H_L = 0, then the equations force the rest to 0", s6, 1)]


def selftest(verbose=False):
    ok_all = True
    for name, fn, nc in CHECKS:
        t0 = time.time()
        good = fn(verbose=verbose)
        control = any(fn(control=k) for k in range(1, nc + 1))
        state = "PASS" if good and not control else "FAIL"
        ok_all &= state == "PASS"
        print(f"{name:<112} {state}  {time.time() - t0:.0f}s" + ("" if not control else "  (control passed: vacuous)"),
              flush=True)
    print(f"static5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"static5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest(verbose="--verbose" in args) else 1)
