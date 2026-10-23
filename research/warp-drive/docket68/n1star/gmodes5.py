#!/usr/bin/env python3
"""gmodes5.py -- mode stability of the linearized Einstein operator on five-dimensional Tangherlini at sigma != 0, the
input [Hin26] Proposition 8.8 takes from [AHW24] Theorem 6.1(1) on Kerr, and with it his Proposition 8.8 in five
dimensions (N1STAR-PROOF.md section 10.27; ROUTES-OPEN.md 4.28; D78).  Labels: computed (exact, sympy), deduced, READ.

[Hin26] (arXiv:2606.28253v2) Proposition 8.8 (p. 153): for 0 != sigma, Im sigma >= 0, the kernel of L-hat_b(sigma) on
A^alpha is trivial.  His proof (pp. 153-154): eta := delta_{E^Ups}(sigma) G u solves box^C(sigma) eta = 0, so eta = 0 by
his Theorem 7.1(1); then D Ric(e^(-i sigma t*) u) = 0, and "By [AHW24, Theorem 6.1(1)], we obtain u = delta*(sigma)
omega where omega in A^alpha'"; then box^Ups(sigma) omega = 0 and his Proposition 6.12 gives omega = 0.  On
five-dimensional Tangherlini, g = -f dt^2 + dr^2/f + r^2 gamma, f = 1 - mu/r^2, gamma the round S^3, the input is
computed here through the Kodama-Ishibashi decomposition ([KI03] H. Kodama and A. Ishibashi, arXiv:hep-th/0305147v3, n =
3, K = 1, Lambda = 0, 2M = mu): h splits into tensor, vector and scalar types by the harmonics of S^3, and each type's
linearized vacuum equations reduce to one master equation f (f Phi')' + (sigma^2 - V) Phi = 0.

The harmonics are handled at a point of S^3 (chi, theta) with sin chi = 3/5, sin theta = 5/13: a harmonic enters
through its Taylor jets there, every jet free but for the harmonic's defining equations (trace, divergence, eigenvalue,
and their derivatives at the point; at scalar l = 1 the jets stop at order 2, the constraints at order 0, S's third jet
entering D Ric only through nabla^j (nabla_j nabla_i - nabla_i nabla_j) S, which vanishes), so that an identity checked
there holds for every harmonic of the type at that point, and so at every point, the isometries of S^3 acting
transitively and commuting with D Ric.  D Ric(h) is the linearized Ricci tensor, D Ric(h)_ab = nabla_c dGamma^c_ab -
nabla_b dGamma^c_ca, dGamma^c_ab = (1/2) g^cd (nabla_a h_bd + nabla_b h_ad - nabla_d h_ab); delta* omega =
(1/2)(nabla_a omega_b + nabla_b omega_a).

  G1 (computed, exact) The structure, and the tensor type.  D Ric(delta* omega) = 0 at the point for an omega with
     arbitrary jets (the operator's check).  For h_ij = 2 r^2 H T_ij, T any trace-free, divergence-free tensor harmonic
     with (Delta + k_T^2) T = 0: D Ric(h)_ab = D Ric(h)_ai = 0 and D Ric(h)_ij = -r^2 (box H + (3/r) Dr.DH - (k_T^2 +
     2) H/r^2) T_ij, [KI03] (5.3); with Phi = r^(3/2) H the master potential is V_T = (f/r^2)(k_T^2 + 2 + 3/4 + 9 mu/(4
     r^2)), k_T^2 = l(l + 2) - 2 (l >= 2), [KI03] (5.6) at n = 3.  Control: the divergence condition dropped, where
     D Ric(h)_ai is not zero.
  G2 (computed, exact) The vector type, V co-closed with (Delta + k_V^2) V = 0, V_ij = -(D_i V_j + D_j V_i)/(2 k_V),
     k_V^2 = l(l + 2) - 1: the gauge 1-form r^2 B V_i dz^i shifts h_ai = r f_a V_i by (r/2) D_a B and h_ij = 2 r^2 H_T
     V_ij by -k_V B/2, so B = -2 H_T/k_V leaves H_T = 0 and F_a = f_a + (r/k_V) D_a H_T, [KI03] (5.10); there D
     Ric(h)_ab = 0, D Ric(h)_ai = r E_a V_i and D Ric(h)_ij = 2 r^2 E_T V_ij with E_T = -(k_V/(2 r^3)) D_a(r^2 F^a),
     which [KI03] does not print, their (5.12) implying it.  At sigma != 0, with Omega := r^2 F^r/(i sigma): E_T = 0 iff
     r^2 F^t = Omega', and then E_a = 0 iff Phi = r^(-3/2) Omega solves the master equation with V_V = (f/r^2)(k_V^2 +
     1 + 3/4 - 27 mu/(4 r^2)), [KI03] (5.15); Phi = 0 forces F = 0.  Control: V_V with +27.
  G3 (computed, exact) The scalar type, l >= 2, S with (Delta + k^2) S = 0, S_i = -D_i S/k, S_ij = D_i D_j S/k^2 +
     gamma_ij S/3, h = f_ab S dy^a dy^b + 2 r f_a S_i dy^a dz^i + 2 r^2 (H_L gamma_ij S + H_T S_ij) dz^i dz^j: delta*
     of A_a S dy^a + r^2 B S_i dz^i shifts f_ab by D_(a A_b), f_a by (r^2 D_a B - k A_a)/(2 r), H_L by k B/6 + f A_r/(2
     r) and H_T by -k B/2, so the gauge 1-form -2 X_a S dy^a - (2 r^2/k) H_T S_i dz^i, X_a = (r/k)(f_a + (r/k) D_a H_T)
     of [KI03] (2.8), leaves f_a = H_T = 0 and their invariants F, F_ab of (2.7); there the seven reduced equations are
     computed, and at sigma != 0, in [KI03]'s X, Y, Z (2.20)-(2.21) with Z = i sigma Z~: E_t, E_r, E_tr give exactly
     [KI03] (2.24a-c); E_tt, E_rr, E_L then reduce to one linear constraint, which the flow preserves, so the solutions
     form a two-dimensional space; Phi := (3 Z~ - r (X + Y))/(r^(1/2) H), H = m + 6 mu/r^2, m = k^2 - 3, solves f (f
     Phi')' + (sigma^2 - V_S) Phi = 0 with V_S = f Q/(16 r^2 H^2), [KI03] (3.1)-(3.7) at n = 3, on that constraint; and
     det[r^(1/2) Phi; r^(1/2) Phi'; constraint] = -r^4 (r^2 - mu)^5 (the constraint as G3 normalizes it: a multiple of
     it by a function of r rescales the determinant by that function), so Phi = 0 forces X = Y = Z~ = 0. Control: Z =
     -i sigma Z~, where (2.24a-c) fail.

  G4 (computed, exact) The exceptional sectors at sigma != 0.  Scalar l = 0 (S = 1): delta*(A_t dt + A_r dr) shifts f_tt
     by d_t A_t - Gamma^r_tt A_r and H_L by f A_r/(2 r), so f_tt = H_L = 0 is reached algebraically; then the mode
     equations force f_tr = f_rr = 0.  Vector l = 1 (V Killing, V_ij = 0): D Ric(h)_ab = 0 and E_r = r^2 d_t F^(1)_tr/(2
     (r^2 - mu)), F^(1)_tr = r d_t(f_r/r) - r d_r(f_t/r) ([KI03] (5.16)), so a mode has F^(1) = 0 and f_a = (r/2) D_a
     B, B = 2 i f_t/(sigma r).  Scalar l = 1 (D_i D_j S = -gamma_ij S, S_ij = 0): the shifts of f_tt, f_t and H_L are
     free of derivatives, with determinant (r^2 - mu)(sigma^2 r^4 - mu)/(4 r^6), so f_tt = f_t = H_L = 0 is reached
     algebraically off the sphere sigma^2 r^4 = mu; then the mode equations force f_tr = f_rr = f_r = 0.  The
     eliminations (the equations and their r-derivatives, every derivative eliminated first) run over Q(3^(1/2), i)(r,
     sigma) at mu = 1 -- the homothety t, r -> lam t, lam r carries g_mu to lam^2 g_(mu/lam^2) and sigma to lam sigma
     -- and every pivot's factors free of r are powers of sigma.  Control: at l = 1, f_t left free, where the
     derivative-free rank is 2 of 4.
  G5 (computed, exact) The potentials and the horizon.  V_T > 0 and V_V >= (f/r^2)(l (l + 2) - 6) > 0 for l >= 2 on r >
     r_h; Q = 1296 x^3 + (624 m - 144) x^2 + 36 m (m - 12) x + 16 m^3 + 60 m^2, x = mu/r^2 in [0, 1], is at least 16 m
     (m - 3)(m + 9) for 3 < m <= 12 and at least 16 m^3 + 60 m^2 for m >= 12, the first bound alone failing beyond m =
     12, so Q > 0 and V_S > 0 for l >= 2 (m >= 5).  In ingoing Eddington-Finkelstein coordinates (v = t + r*, r)
     Gamma^lam_rr = 0, so (delta* xi)_rr = d_r xi_r and the r-row of delta* xi = u is a linear ODE in r for xi, its
     coefficients smooth across r = r_h; and the master fields, written in the ingoing components of the reduced field,
     are free of 1/f -- the scalar numerator 3 Z~ - r (X + Y) = (4 sigma r^3 F - sigma r^3 f F'_rr - 2 sigma r^3 F_vr -
     3 i r^2 f F_vr - 3 i r^2 F_vv)/(r sigma), the vector Omega = r^2 (f F'_r + F_v)/(i sigma) -- so each is e^(-i
     sigma r*) times a function smooth across r = r_h.  Control: V_V lowered by 6, where positivity fails.

Deduced, not computed here (N1STAR-PROOF.md 10.27): [AHW24] Theorem 6.1(1) on five-dimensional Tangherlini -- every mode
solution of D Ric = 0 at 0 != sigma, Im sigma >= 0, smooth across the future horizon and outgoing at infinity, is
delta* omega with omega in the same class -- by the master equations' positivity (the argument of 10.16), the gauge
1-forms of G2-G4, and G5's ODE along d_r; and with it [Hin26] Proposition 8.8 there, on the readings of 10.19-10.26.

READ.  [Hin26] pp. 25 (section 1.4.1), 153-154 (section 8.4: Proposition 8.8 and its proof); [KI03] pp. 4-10
(sections 2-3, (2.1)-(2.24), (3.1)-(3.14)), 13-15 (section 5, (5.1)-(5.17)), 19-20 (Appendix B, the l = 1 mode);
alphaXiv, 2026-10-23.

sympy.  python3 gmodes5.py [--selftest | --mutants]   (--verbose lists every sub-check)
"""
import itertools
import sys
import time

import sympy as sp

from damping5 import Checklist

t, r = sp.symbols("t r", real=True)
mu, sig = sp.symbols("mu sigma", positive=True)
c0, th0 = sp.symbols("chi_0 theta_0", positive=True)
a, b, d = sp.symbols("a b d", real=True)                   # angular offsets from the point
X = [t, r, a, b, d]
f = 1 - mu / r**2
s1, s2 = sp.sin(c0 + a), sp.sin(th0 + b)
gdiag = [-f, 1 / f, r**2, r**2 * s1**2, r**2 * s1**2 * s2**2]
g = sp.diag(*gdiag)
gi = sp.diag(*[1 / q for q in gdiag])
N = 5
GAM = [[[sp.expand(sum(gi[l, k] * (sp.diff(g[k, m], X[n]) + sp.diff(g[k, n], X[m]) - sp.diff(g[m, n], X[k]))
                       for k in range(N)) / 2) for n in range(N)] for m in range(N)] for l in range(N)]
Y = [a, b, d]
gam = sp.diag(1, s1**2, s1**2 * s2**2)
gami = sp.diag(1, 1 / s1**2, 1 / (s1**2 * s2**2))
G3 = [[[sp.expand(sum(gami[l, k] * (sp.diff(gam[k, m], Y[n]) + sp.diff(gam[k, n], Y[m]) - sp.diff(gam[m, n], Y[k]))
                      for k in range(3)) / 2) for n in range(3)] for m in range(3)] for l in range(3)]
PT = {a: 0, b: 0, d: 0}
TRIG = {sp.sin(c0): sp.Rational(3, 5), sp.cos(c0): sp.Rational(4, 5), sp.sin(th0): sp.Rational(5, 13),
        sp.cos(th0): sp.Rational(12, 13)}
K = [sp.Symbol("k_T", positive=True), sp.Symbol("k_V", positive=True), sp.Symbol("k", positive=True)]


def atpt(e):
    """value at the point of S^3"""
    return sp.expand(sp.sympify(e).subs(PT).subs(TRIG))


def dric(h):
    """the linearized Ricci tensor of the symmetric 5 x 5 field h, at the point"""
    dG = [[[None] * N for _ in range(N)] for _ in range(N)]
    for l in range(N):
        for m in range(N):
            for n in range(m, N):
                e = gi[l, l] * (sp.diff(h[n, l], X[m]) + sp.diff(h[m, l], X[n]) - sp.diff(h[m, n], X[l])) / 2
                e -= gi[l, l] * sum(GAM[s][m][n] * h[s, l] for s in range(N) if GAM[s][m][n] != 0)
                dG[l][m][n] = dG[l][n][m] = e
    tr = [sum(dG[l][l][m] for l in range(N)) for m in range(N)]
    R = sp.zeros(N, N)
    for m in range(N):
        for n in range(m, N):
            e = sum(sp.diff(dG[l][m][n], X[l]) for l in range(N))
            e += sum(GAM[l][l][s] * dG[s][m][n] for l in range(N) for s in range(N) if GAM[l][l][s] != 0)
            e -= sum(GAM[s][l][m] * dG[l][s][n] + GAM[s][l][n] * dG[l][m][s] for l in range(N) for s in range(N))
            e -= sp.diff(tr[m], X[n]) - sum(GAM[s][n][m] * tr[s] for s in range(N) if GAM[s][n][m] != 0)
            R[m, n] = R[n, m] = atpt(e)
    return R


def dstar(w, at=True):
    """delta* of the 1-form w (list of 5), at the point (or as a field)"""
    M = sp.Matrix(N, N, lambda m, n: (sp.diff(w[n], X[m]) + sp.diff(w[m], X[n])) / 2
                  - sum(GAM[l][m][n] * w[l] for l in range(N)))
    return M.applyfunc(atpt) if at else M


def jets(name, order):
    """a polynomial in the offsets with free jet symbols up to the given order"""
    syms, poly = [], 0
    for k in range(order + 1):
        for al in itertools.product(range(k + 1), repeat=3):
            if sum(al) != k:
                continue
            s = sp.Symbol(f"{name}_{al[0]}{al[1]}{al[2]}")
            syms.append(s)
            fac = sp.factorial(al[0]) * sp.factorial(al[1]) * sp.factorial(al[2])
            poly += s * a**al[0] * b**al[1] * d**al[2] / fac
    return poly, syms


def derivs(e, order):
    """e and all its angular derivatives up to the given order, at the point"""
    out = []
    for k in range(order + 1):
        for al in itertools.combinations_with_replacement(range(3), k):
            q = e
            for i in al:
                q = sp.diff(q, Y[i])
            out.append(atpt(q))
    return out


def cov1(w):
    return [[sp.diff(w[j], Y[i]) - sum(G3[k][i][j] * w[k] for k in range(3)) for j in range(3)] for i in range(3)]


def cov2(T):
    return [[[sp.diff(T[j][k], Y[i]) - sum(G3[l][i][j] * T[l][k] + G3[l][i][k] * T[j][l] for l in range(3))
              for k in range(3)] for j in range(3)] for i in range(3)]


def lap1(w):
    Dw = cov1(w)
    return [sum(gami[k, l] * (sp.diff(Dw[l][j], Y[k]) - sum(G3[m][k][l] * Dw[m][j] + G3[m][k][j] * Dw[l][m]
                                                           for m in range(3))) for k in range(3) for l in range(3))
            for j in range(3)]


def lap2(T):
    DT = cov2(T)
    return [[sum(gami[k, l] * (sp.diff(DT[l][i][j], Y[k]) - sum(G3[m][k][l] * DT[m][i][j] + G3[m][k][i] * DT[l][m][j]
                                                               + G3[m][k][j] * DT[l][i][m] for m in range(3)))
                 for k in range(3) for l in range(3)) for j in range(3)] for i in range(3)]


def scalar_harmonic(k, order=2, hessian=None):
    """S with free jets but for (Delta + k^2) S = 0 at the point (and the given Hessian law, if any)"""
    S, syms = jets("S", order)
    DS = [sp.diff(S, y) for y in Y]
    DDS = [[sp.diff(DS[j], Y[i]) - sum(G3[m][i][j] * DS[m] for m in range(3)) for j in range(3)] for i in range(3)]
    lap = sum(gami[i, j] * DDS[i][j] for i in range(3) for j in range(3))
    cons = derivs(lap + k**2 * S, order - 2)
    if hessian is not None:                                # l = 1: D_i D_j S = -gamma_ij S
        cons += sum((derivs(DDS[i][j] + gam[i, j] * S, order - 2) for i in range(3) for j in range(i, 3)), [])
    sol = sp.solve(cons, syms, dict=True)[0]
    return S, DS, DDS, sol


def match(R, sol, parts):
    """solve R = sum_k c_k P_k at the point for the unknown coefficients c_k; parts: list of (symbol, 5x5 pattern);
    returns (coefficients, residual zero)"""
    unknowns = [p[0] for p in parts]
    Rs = R.subs(sol)
    model = sum((p[0] * p[1].subs(sol) for p in parts), sp.zeros(N, N))
    eqs = [sp.cancel(sp.together(Rs[m, n] - model[m, n])) for m in range(N) for n in range(m, N)]
    eqs = [sp.numer(q) for q in eqs if q != 0]
    cs = sp.solve(eqs, unknowns, dict=True)
    if not cs:
        return None, False
    cs = cs[0]
    ok = all(zero(q.subs(cs)) for q in eqs)
    return cs, ok


def zero(e):
    return sp.cancel(sp.together(e)) == 0


def box2(u):
    """the orbit-space wave operator on u(t, r)"""
    return -sp.diff(u, t, 2) / f + sp.diff(f * sp.diff(u, r), r)


# ------------------------------------------------------------------------------------------------- G1
def g1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    if control == 0:
        w, syms = [], []
        for m in range(N):
            p, js = jets(f"w{m}", 2)
            w.append(p * sp.Function(f"W{m}")(t, r))
        chk("D Ric(delta* omega) = 0 at the point, omega with arbitrary jets",
            all(zero(q) for q in dric(dstar(w, at=False))))
    kT = K[0]
    H = sp.Function("H")(t, r)
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
    if control != 1:
        cons += sum((derivs(q, 1) for q in div), [])
    sol = sp.solve(cons, syms, dict=True)[0]
    h = sp.zeros(N, N)
    for i in range(3):
        for j in range(3):
            h[2 + i, 2 + j] = 2 * r**2 * H * T[i][j]
    Rh = dric(h).subs(sol)
    lam = -r**2 * (box2(H) + 3 * f * sp.diff(H, r) / r - (kT**2 + 2) * H / r**2)
    ok = all(sp.simplify(Rh[m, n]) == 0 for m in range(2) for n in range(N))
    ok &= all(sp.simplify(Rh[2 + i, 2 + j] - lam * atpt(T[i][j]).subs(sol)) == 0 for i in range(3) for j in range(i, 3))
    Phi = sp.Function("Phi")(t, r)
    Hp = r**sp.Rational(-3, 2) * Phi
    VT = f / r**2 * (kT**2 + 2 + sp.Rational(3, 4) + 9 * mu / (4 * r**2))
    master = sp.simplify(sp.expand(f * r**sp.Rational(3, 2) * (box2(Hp) + 3 * f * sp.diff(Hp, r) / r - (kT**2 + 2) * Hp
                                                                 / r**2))
                         - (-sp.diff(Phi, t, 2) + f * sp.diff(f * sp.diff(Phi, r), r) - VT * Phi)) == 0
    chk("tensor type: D Ric(h)_ab = D Ric(h)_ai = 0, D Ric(h)_ij = -r^2 (box H + (3/r) Dr.DH - (k_T^2 + 2) H/r^2) T_ij "
        "([KI03] (5.3)); Phi = r^(3/2) H has V_T = (f/r^2)(k_T^2 + 11/4 + 9 mu/(4 r^2)) ([KI03] (5.6))", ok and master)
    return chk.ok


# ------------------------------------------------------------------------------------------------- G2
def vector_harmonic(kV):
    V, syms = [], []
    for i in range(3):
        p, js = jets(f"V{i}", 2)
        V.append(p)
        syms += js
    DV = cov1(V)
    div = sum(gami[i, j] * DV[i][j] for i in range(3) for j in range(3))
    L1 = lap1(V)
    cons = derivs(div, 1) + [atpt(L1[j] + kV**2 * V[j]) for j in range(3)]
    sol = sp.solve(cons, syms, dict=True)[0]
    Vij = [[-(DV[i][j] + DV[j][i]) / (2 * kV) for j in range(3)] for i in range(3)]
    return V, Vij, sol


def vector_parts(V, Vij):
    ct, cr, cT = sp.symbols("c_t c_r c_T")
    P = [sp.zeros(N, N) for _ in range(3)]
    for i in range(3):
        for a_, M in ((0, P[0]), (1, P[1])):
            M[a_, 2 + i] = M[2 + i, a_] = r * atpt(V[i])
        for j in range(3):
            P[2][2 + i, 2 + j] = 2 * r**2 * atpt(Vij[i][j])
    return [(ct, P[0]), (cr, P[1]), (cT, P[2])]


def vector_E(kV):
    V, Vij, sol = vector_harmonic(kV)
    parts = vector_parts(V, Vij)
    Ft, Fr = sp.Function("F_t")(t, r), sp.Function("F_r")(t, r)
    h = sp.zeros(N, N)
    for i in range(3):
        h[0, 2 + i] = h[2 + i, 0] = r * Ft * V[i]
        h[1, 2 + i] = h[2 + i, 1] = r * Fr * V[i]
    cs, ok = match(dric(h), sol, parts)
    B = sp.Function("B")(t, r)
    gs, okg = match(dstar([0, 0] + [r**2 * B * V[i] for i in range(3)]), sol, parts)
    return cs, ok, gs, okg, (Ft, Fr, B), parts


def g2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    kV = K[1]
    cs, ok, gs, okg, (Ft, Fr, B), parts = vector_E(kV)
    ct, cr, cT = [p[0] for p in parts]
    gauge = okg and all(sp.simplify(gs[c] - w) == 0 for c, w in ((ct, r * sp.diff(B, t) / 2),
                                                               (cr, r * sp.diff(B, r) / 2), (cT, -kV * B / 2)))
    chk("vector type: delta*(r^2 B V_i dz^i) shifts f_a by (r/2) D_a B and H_T by -k_V B/2", gauge)
    divF = sp.diff(r**2 * (-Ft / f), t) + sp.diff(r**2 * f * Fr, r)                # D_a(r^2 F^a)
    eT = sp.simplify(cs[cT] + kV * divF / (2 * r**3)) == 0
    chk("in the gauge H_T = 0: D Ric(h)_ab = 0, D Ric(h)_ai = r E_a V_i, D Ric(h)_ij = 2 r^2 E_T V_ij, E_T = -(k_V/(2 "
        "r^3)) D_a(r^2 F^a)", ok and eT)
    # modes e^(-i sigma t): Omega := r^2 F^r/(i sigma); E_T = 0 iff r^2 F^t = Omega'
    Om = sp.Function("Omega")(r)
    ex = sp.exp(-sp.I * sig * t)
    sub = {Ft: ex * (-f * sp.diff(Om, r) / r**2), Fr: ex * (sp.I * sig * Om / (r**2 * f))}
    Et = sp.simplify((cs[ct].subs(sub).doit()) / ex)
    Er = sp.simplify((cs[cr].subs(sub).doit()) / ex)
    eT0 = sp.simplify(cs[cT].subs(sub).doit() / ex) == 0
    Phi = r**sp.Rational(-3, 2) * Om
    coef = 27 if control != 1 else -27
    VV = f / r**2 * (kV**2 + 1 + sp.Rational(3, 4) - coef * mu / (4 * r**2))
    M = sp.expand((f * sp.diff(f * sp.diff(Phi, r), r) + (sig**2 - VV) * Phi) * r**sp.Rational(3, 2))
    om2 = sp.solve(sp.Eq(M, 0), sp.diff(Om, r, 2))[0]
    red = lambda e: sp.simplify(sp.expand(e).subs(sp.Derivative(Om, r, 3), sp.diff(om2, r)).subs(
        sp.Derivative(Om, r, 2), om2).subs(sp.Derivative(Om, r, 2), om2))
    master = red(Et) == 0 and red(Er) == 0 and sp.simplify(sp.diff(Er, sp.Derivative(Om, r, 2))) != 0
    chk("at sigma != 0: with Omega = r^2 F^r/(i sigma) the equation E_T = 0 is r^2 F^t = Omega', and then E_a = 0 iff "
        "Phi = r^(-3/2) Omega solves f (f Phi')' + (sigma^2 - V_V) Phi = 0, V_V = (f/r^2)(k_V^2 + 7/4 - 27 mu/(4 r^2)) "
        "([KI03] (5.14)-(5.15))", eT0 and master)
    return chk.ok


# ------------------------------------------------------------------------------------------------- G3
def scalar_parts(k, S, DS, DDS):
    cs = sp.symbols("c_tt c_tr c_rr c_t c_r c_L c_T")
    P = [sp.zeros(N, N) for _ in range(7)]
    S0 = atpt(S)
    P[0][0, 0] = S0
    P[1][0, 1] = P[1][1, 0] = S0
    P[2][1, 1] = S0
    for i in range(3):
        Si = atpt(-DS[i] / k)
        for a_, M in ((0, P[3]), (1, P[4])):
            M[a_, 2 + i] = M[2 + i, a_] = r * Si
        for j in range(3):
            P[5][2 + i, 2 + j] = 2 * r**2 * atpt(gam[i, j] * S)
            P[6][2 + i, 2 + j] = 2 * r**2 * atpt(DDS[i][j] / k**2 + gam[i, j] * S / 3)
    return list(zip(cs, P))


FN = ("F_tt", "F_tr", "F_rr", "F")


def scalar_E(k):
    S, DS, DDS, sol = scalar_harmonic(k)
    parts = scalar_parts(k, S, DS, DDS)
    Ftt, Ftr, Frr, F = [sp.Function(nm)(t, r) for nm in FN]
    h = sp.zeros(N, N)
    h[0, 0], h[0, 1], h[1, 1] = Ftt * S, Ftr * S, Frr * S
    h[1, 0] = h[0, 1]
    for i in range(3):
        for j in range(3):
            h[2 + i, 2 + j] = 2 * r**2 * F * gam[i, j] * S
    cs, ok = match(dric(h), sol, parts)
    At, Ar, B = [sp.Function(nm)(t, r) for nm in ("A_t", "A_r", "B")]
    gs, okg = match(dstar([At * S, Ar * S] + [r**2 * B * (-DS[i] / k) for i in range(3)]), sol, parts)
    return cs, ok, gs, okg, parts


def scalar_gauge_check(k, gs, parts):
    """the gauge 1-form that removes f_a and H_T leaves [KI03] (2.7)'s F, F_ab with X_a of (2.8)"""
    c = dict((p[0].name, p[0]) for p in parts)
    At, Ar, B = [sp.Function(nm)(t, r) for nm in ("A_t", "A_r", "B")]
    fab = [sp.Function(nm)(t, r) for nm in ("f_tt", "f_tr", "f_rr")]
    fa = [sp.Function(nm)(t, r) for nm in ("f_t", "f_r")]
    HL, HT = sp.Function("H_L")(t, r), sp.Function("H_T")(t, r)
    Bs = sp.solve(sp.Eq(gs[c["c_T"]], HT), B)[0]                 # H_T removed
    sub = {B: Bs}
    Aeq = [sp.Eq(gs[c["c_t"]].subs(B, Bs).doit(), fa[0]), sp.Eq(gs[c["c_r"]].subs(B, Bs).doit(), fa[1])]
    As = sp.solve(Aeq, [At, Ar], dict=True)[0]                  # f_a removed
    sub = {B: Bs, At: As[At], Ar: As[Ar]}
    res = lambda key: sp.simplify(gs[c[key]].subs(sub).doit())
    Xa = [r / k * (fa[0] + r / k * sp.diff(HT, t)), r / k * (fa[1] + r / k * sp.diff(HT, r))]
    g2_ = sp.diag(-f, 1 / f)
    Gm = lambda l, a_, b_: sum(g2_.inv()[l, kk] * (sp.diff(g2_[kk, a_], [t, r][b_]) + sp.diff(g2_[kk, b_], [t, r][a_])
                                                   - sp.diff(g2_[a_, b_], [t, r][kk])) for kk in range(2)) / 2
    DX = lambda a_, b_: sp.diff(Xa[b_], [t, r][a_]) - sum(Gm(l, a_, b_) * Xa[l] for l in range(2))
    Fab_KI = [fab[0] + 2 * DX(0, 0), fab[1] + DX(0, 1) + DX(1, 0), fab[2] + 2 * DX(1, 1)]
    F_KI = HL + HT / 3 + f * Xa[1] / r
    ok = all(zero(fab[i] - res(key) - Fab_KI[i]) for i, key in enumerate(("c_tt", "c_tr", "c_rr")))
    ok &= zero(HL - res("c_L") - F_KI)
    return ok


def scalar_flow(Es, k, sZ=1):
    """[KI03] (2.20)-(2.24) at sigma != 0 from the computed equations: returns (flow ok, constraint, rank1, preserved,
    master, det)"""
    n = 3
    ex = sp.exp(-sp.I * sig * t)
    Xf, Yf, Zf = [sp.Function(nm)(r) for nm in ("X", "Y", "Zt")]
    Z = sZ * sp.I * sig * Zf
    sub = {"F_tt": -f * ((n - 1) * Xf - Yf) / (n * r**(n - 2)), "F_rr": (-Xf + (n - 1) * Yf) / (n * r**(n - 2)) / f,
           "F_tr": Z / r**(n - 2) / f, "F": -(Xf + Yf) / (2 * n * r**(n - 2))}
    Xs, Ys, Zs = sp.symbols("X0:3"), sp.symbols("Y0:3"), sp.symbols("Z0:3")

    def jet(e):
        e = e.subs({sp.Function(nm)(t, r): ex * sub[nm] for nm in FN}).doit()
        e = sp.expand(sp.together(e / ex))
        for F_, S_ in ((Xf, Xs), (Yf, Ys), (Zf, Zs)):
            e = e.subs(sp.Derivative(F_, r, 2), S_[2]).subs(sp.Derivative(F_, r), S_[1]).subs(F_, S_[0])
        return sp.together(e)
    J = {key: jet(v) for key, v in Es.items()}
    X0, X1, X2 = Xs
    Y0, Y1, Y2 = Ys
    Z0, Z1, Z2 = Zs
    fl = sp.solve([sp.numer(J["t"]), sp.numer(J["r"]), sp.numer(J["tr"])], [X1, Y1, Z1], dict=True)
    if not fl:
        return False, None, False, False, False, None
    fl = {v: sp.cancel(e) for v, e in fl[0].items()}
    ki = {X1: (n - 2) / r * X0 + (sp.diff(f, r) / f - 2 / r) * Y0 + (k**2 / (f * r**2) - sig**2 / f**2) * Z0,
          Y1: sp.diff(f, r) / (2 * f) * (X0 - Y0) + sig**2 / f**2 * Z0, Z1: X0}
    flow_ok = all(zero(fl[v] - ki[v]) for v in (X1, Y1, Z1))

    def dr(e):
        return sp.cancel(sp.diff(e, r) + sp.diff(e, X0) * fl[X1] + sp.diff(e, Y0) * fl[Y1] + sp.diff(e, Z0) * fl[Z1])
    sec = {X2: dr(fl[X1]), Y2: dr(fl[Y1]), Z2: dr(fl[Z1])}
    forms = {}
    for key in ("tt", "rr", "L", "t", "r", "tr", "T"):
        e = sp.expand(sp.cancel(sp.numer(J[key]).subs(sec).subs(fl)))
        forms[key] = [sp.cancel(e.coeff(v)) for v in (X0, Y0, Z0)]
    nz = [key for key in forms if any(c_ != 0 for c_ in forms[key])]
    C = forms[nz[0]] if nz else [0, 0, 0]
    prop = lambda u, v: all(zero(u[i] * v[j] - u[j] * v[i]) for i in range(3) for j in range(3))
    rank1 = bool(nz) and all(prop(forms[key], C) for key in nz) and set(nz) <= {"tt", "rr", "L"}
    dC = sp.expand(dr(C[0] * X0 + C[1] * Y0 + C[2] * Z0))
    preserved = prop([sp.cancel(dC.coeff(v)) for v in (X0, Y0, Z0)], C)
    m_ = k**2 - n
    x = mu / r**2
    H = m_ + sp.Rational(n * (n + 1), 2) * x
    Q = (n**4 * (n + 1)**2 * x**3 + n * (n + 1) * (4 * (2 * n**2 - 3 * n + 4) * m_ + n * (n - 2) * (n - 4) * (n + 1))
         * x**2 - 12 * n * ((n - 4) * m_ + n * (n + 1) * (n - 2)) * m_ * x + 16 * m_**3 + 4 * n * (n + 2) * m_**2)
    VS = f * Q / (16 * r**2 * H**2)
    Phi = (n * Z0 - r * (X0 + Y0)) / (r**(sp.Rational(n, 2) - 1) * H)
    P1 = dr(Phi)
    ME = sp.expand(sp.cancel((f * dr(f * P1) + (sig**2 - VS) * Phi) * sp.sqrt(r)))
    master = prop([sp.cancel(ME.coeff(v)) for v in (X0, Y0, Z0)], C)
    Ps, P1s = sp.expand(sp.cancel(Phi * sp.sqrt(r))), sp.expand(sp.cancel(P1 * sp.sqrt(r)))
    det = sp.factor(sp.cancel(sp.Matrix([[sp.cancel(Ps.coeff(v)) for v in (X0, Y0, Z0)],
                                         [sp.cancel(P1s.coeff(v)) for v in (X0, Y0, Z0)], C]).det()))
    return flow_ok, C, rank1, preserved, master, det


def g3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    k = K[2]
    cs, ok, gs, okg, parts = scalar_E(k)
    if control == 0:
        chk("scalar type: delta* of A_a S dy^a + r^2 B S_i dz^i removes f_a and H_T and leaves [KI03] (2.7)'s F, F_ab "
            "with X_a = (r/k)(f_a + (r/k) D_a H_T) of (2.8)", okg and scalar_gauge_check(k, gs, parts))
        chk("in that gauge D Ric(h) = (E_ab S, r E_a S_i, 2 r^2 (E_L gamma_ij S + E_T S_ij)): the seven reduced "
            "equations",
            ok)
    names = {"c_tt": "tt", "c_tr": "tr", "c_rr": "rr", "c_t": "t", "c_r": "r", "c_L": "L", "c_T": "T"}
    Es = {names[p[0].name]: cs[p[0]] for p in parts}
    flow_ok, C, rank1, preserved, master, det = scalar_flow(Es, k, sZ=-1 if control == 1 else 1)
    chk(f"at sigma != 0, Z = i sigma Z~: E_t, E_r, E_tr give [KI03] (2.24a-c); E_tt, E_rr, E_L reduce to one constraint "
        f"(rank 1: {rank1}), preserved by the flow ({preserved}); Phi = (3 Z~ - r (X + Y))/(r^(1/2) H) solves (3.5) "
        f"with "
        f"V_S = f Q/(16 r^2 H^2) on it ({master}); det[Phi; Phi'; C] = {det}",
        flow_ok and rank1 and preserved and master and det is not None and zero(det + r**4 * (r**2 - mu)**5))
    return chk.ok


# ------------------------------------------------------------------------------------------------- G4
EX = sp.exp(-sp.I * sig * t)


def mode_eqs(R, funcs):
    """the nonzero components of R as numerators at the mode level, funcs(t, r) -> e^(-i sigma t) U(r)"""
    out = []
    unk = [sp.Function(F.func.__name__ + "_m")(r) for F in funcs]
    for q in R:
        if zero(q):
            continue
        q = q.subs({F: EX * U for F, U in zip(funcs, unk)}).doit()
        out.append(sp.numer(sp.together(sp.expand(q / EX))))
    return out, unk


def algebraic_part(eqs, unk):
    """prolong once, eliminate every derivative column first, then the unknowns among the derivative-free rows, by
    Gaussian elimination over Q(3^(1/2), i)(r, sigma) at mu = 1 (the homothety t, r -> lam t, lam r carries g_mu to lam^2
    g_(mu/lam^2) and sigma to lam sigma, and D Ric of lam^2 g is that of g); returns (derivative-free rank, every
    pivot's factors free of r)"""
    J = [[sp.Symbol(f"{U.func.__name__}_{j}") for j in range(4)] for U in unk]

    def jet(e):
        e = sp.expand(e.subs(mu, 1))
        for U, js in zip(unk, J):
            for j in (3, 2, 1):
                e = e.subs(sp.Derivative(U, r, j), js[j])
            e = e.subs(U, js[0])
        return sp.expand(e)
    rows = [jet(e) for e in eqs] + [jet(sp.diff(e, r)) for e in eqs]
    cols = [js[j] for j in (3, 2, 1) for js in J] + [js[0] for js in J]
    nd = 3 * len(unk)
    Kf = sp.QQ.algebraic_field(sp.sqrt(3), sp.I).frac_field(r, sig)
    M = [[Kf.from_sympy(sp.cancel(rw.coeff(v))) for v in cols] for rw in rows]
    used, pivots, rank0 = set(), [], 0
    for col in range(len(cols)):
        cand = [i for i in range(len(M)) if i not in used and M[i][col] != Kf.zero]
        if not cand:
            continue
        p_ = min(cand, key=lambda i: len(str(M[i][col])))
        used.add(p_)
        pivots.append(Kf.to_sympy(M[p_][col]))
        rank0 += col >= nd
        for i in range(len(M)):
            if i != p_ and M[i][col] != Kf.zero:
                q = M[i][col] / M[p_][col]
                M[i] = [x - q * y for x, y in zip(M[i], M[p_])]
    free = set()
    for pv in pivots:
        num, den = sp.fraction(sp.factor(pv))
        for part in (num, den):
            for fac, _ in sp.factor_list(part)[1]:
                if not fac.has(r):
                    free.add(fac)
    return rank0, free


def g4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    # scalar l = 0 (S = 1): delta*(A_t dt + A_r dr) shifts f_tt by -i sigma A_t - Gamma^r_tt A_r and H_L by f A_r/(2 r),
    # so f_tt = H_L = 0 is reached algebraically at sigma != 0; then D Ric = 0 forces f_tr = f_rr = 0
    if control == 0:
        At, Ar = sp.Function("A_t")(t, r), sp.Function("A_r")(t, r)
        Mg = dstar([At, Ar, 0, 0, 0])
        okg = zero(Mg[2, 2] / (2 * r**2 * atpt(gam[0, 0])) - f * Ar / (2 * r))
        okg &= zero(Mg[0, 0] - (sp.diff(At, t) - atpt(GAM[1][0][0]) * Ar))
        ftr, frr = sp.Function("f_tr")(t, r), sp.Function("f_rr")(t, r)
        h = sp.zeros(N, N)
        h[0, 1] = h[1, 0] = ftr
        h[1, 1] = frr
        eqs, unk = mode_eqs(dric(h), [ftr, frr])
        rk, free = algebraic_part(eqs, unk)
        chk(f"scalar l = 0: the gauge f_tt = H_L = 0 is algebraic at sigma != 0; then the mode equations force (f_tr, "
            f"f_rr) = 0 (derivative-free rank {rk} of 2; pivot factors free of r: {sorted(map(str, free))})",
            okg and rk == 2 and free <= {sig})
    # vector l = 1: V Killing (k_V^2 = 2, V_ij = 0); E_r = r^2 d_t F^(1)_tr/(2 (r^2 - mu)), F^(1)_tr = r d_t(f_r/r) -
    # r d_r(f_t/r), so a mode has F^(1) = 0 and f_a = (r/2) D_a B with B = 2 i f_t/(sigma r)
    if control == 0:
        V, syms = [], []
        for i in range(3):
            p, js = jets(f"V{i}", 2)
            V.append(p)
            syms += js
        DV = cov1(V)
        sol = sp.solve(sum((derivs(DV[i][j] + DV[j][i], 1) for i in range(3) for j in range(i, 3)), []), syms,
                       dict=True)[0]
        Ft, Fr = sp.Function("f_t")(t, r), sp.Function("f_r")(t, r)
        h = sp.zeros(N, N)
        for i in range(3):
            h[0, 2 + i] = h[2 + i, 0] = r * Ft * V[i]
            h[1, 2 + i] = h[2 + i, 1] = r * Fr * V[i]
        R = dric(h).subs(sol)
        F1 = sp.diff(Fr, t) - sp.diff(Ft, r) + Ft / r
        i0 = [i for i in range(3) if atpt(V[i]).subs(sol) != 0][0]
        Er = R[1, 2 + i0] / (r * atpt(V[i0]).subs(sol))
        okv = zero(Er - r**2 * sp.diff(F1, t) / (2 * (r**2 - mu))) and all(zero(R[m, n]) for m in range(2)
                                                                          for n in range(2))
        # a mode f_a = e^(-i sigma t) g_a(r) with F^(1) = 0: g_r from g_t, and f_a = (r/2) D_a B, B = 2 i f_t/(sigma r)
        gt, gr = sp.Function("g_t")(r), sp.Function("g_r")(r)
        ex = sp.exp(-sp.I * sig * t)
        grs = sp.solve(sp.diff(ex * gr, t) - sp.diff(ex * gt, r) + ex * gt / r, gr)[0]
        Bm = 2 * sp.I * ex * gt / (sig * r)
        okB = zero(r / 2 * sp.diff(Bm, t) - ex * gt) and zero(r / 2 * sp.diff(Bm, r) - ex * grs)
        chk("vector l = 1: D Ric(h)_ab = 0 and E_r = r^2 d_t F^(1)_tr/(2 (r^2 - mu)), so a mode at sigma != 0 has "
            "F^(1) = 0, f_a = (r/2) D_a B with B = 2 i f_t/(sigma r)", okv and okB)
    # scalar l = 1: S with D_i D_j S = -gamma_ij S (k^2 = 3, S_ij = 0); the gauge f_tt = f_t = H_L = 0 is algebraic at
    # sigma != 0; then D Ric = 0 forces (f_tr, f_rr, f_r) = 0
    k = sp.sqrt(3)
    S, DS, DDS, sol = scalar_harmonic(k, order=2, hessian=True)
    parts = [p for p in scalar_parts(k, S, DS, DDS) if p[0].name != "c_T"]
    At, Ar, B = [sp.Function(nm)(t, r) for nm in ("A_t", "A_r", "B")]
    gs, okg = match(dstar([At * S, Ar * S] + [r**2 * B * (-DS[i] / k) for i in range(3)]), sol, parts)
    c = dict((p[0].name, p[0]) for p in parts)
    lin = [gs[c[nm]] for nm in ("c_tt", "c_t", "c_L")]
    modev = [sp.Function(nm + "_m")(r) for nm in ("A_t", "A_r", "B")]
    lin_m = [sp.expand(q.subs({F: EX * U for F, U in zip((At, Ar, B), modev)}).doit() / EX) for q in lin]
    Jm = sp.Matrix([[sp.cancel(q.coeff(U)) for U in modev] for q in lin_m])
    derivfree = all(not q.has(sp.Derivative) for q in lin_m)
    gdet = sp.factor(Jm.det())
    ftr, frr, fr, ft = [sp.Function(nm)(t, r) for nm in ("f_tr", "f_rr", "f_r", "f_t")]
    h = sp.zeros(N, N)
    h[0, 1] = h[1, 0] = ftr * S
    h[1, 1] = frr * S
    for i in range(3):
        Si = -DS[i] / k
        h[1, 2 + i] = h[2 + i, 1] = r * fr * Si
        if control == 1:                                   # control: f_t left free, one gauge condition dropped
            h[0, 2 + i] = h[2 + i, 0] = r * ft * Si
    funcs = [ftr, frr, fr] + ([ft] if control == 1 else [])
    Es, okE = match(dric(h), sol, parts)                     # the radial coefficients, free of the harmonic's jets
    eqs, unk = mode_eqs([Es[p[0]] for p in parts], funcs)
    rk, free = algebraic_part(eqs, unk)
    chk(f"scalar l = 1: the gauge f_tt = f_t = H_L = 0 is algebraic at sigma != 0 (derivative-free {derivfree}, "
        f"determinant {gdet}); then the mode equations force (f_tr, f_rr, f_r) = 0 (rank {rk} of {len(unk)}; pivot "
        f"factors free of r: {sorted(map(str, free))})",
        okg and okE and derivfree and not zero(gdet) and rk == len(unk) and free <= {sig})
    return chk.ok


# ------------------------------------------------------------------------------------------------- G5
def g5(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    l, x = sp.symbols("l x", positive=True)
    # V_T and V_V at l >= 2: positive on r > r_h, x = mu/r^2 in (0, 1)
    VT = l * (l + 2) + sp.Rational(3, 4) + sp.Rational(9, 4) * x
    VV = l * (l + 2) + sp.Rational(3, 4) - sp.Rational(27, 4) * x
    if control == 1:
        VV = l * (l + 2) + sp.Rational(3, 4) - sp.Rational(27, 4) * x - 6        # control: shifted by -6
    okT = all(cf > 0 for cf in sp.Poly(sp.expand(VT.subs(l, l + 2)), l, x).coeffs())
    lowV = sp.expand(VV.subs(x, 1).subs(l, l + 2))                      # x <= 1 and the x-coefficient < 0
    okV = sp.Poly(VV, x).coeffs()[0] < 0 and all(cf > 0 for cf in sp.Poly(lowV, l).coeffs())
    chk("V_T > 0 and V_V >= (f/r^2)(l (l + 2) - 6) > 0 for l >= 2 on r > r_h", okT and okV)
    # V_S: Q > 0 for m > 3, 0 <= x <= 1 -- Q = 1296 x^3 + (624 m - 144) x^2 + 36 m (m - 12) x + 16 m^3 + 60 m^2 is at
    # least 16 m (m - 3)(m + 9) for 3 < m <= 12 and at least 16 m^3 + 60 m^2 for m >= 12 (the first bound alone fails
    # beyond m = 12), and H = m + 6 x > 0; m = l (l + 2) - 3 >= 5 at l >= 2
    m, p = sp.Symbol("m", positive=True), sp.Symbol("p", nonnegative=True)
    n = 3
    Q = (n**4 * (n + 1)**2 * x**3 + n * (n + 1) * (4 * (2 * n**2 - 3 * n + 4) * m + n * (n - 2) * (n - 4) * (n + 1))
         * x**2 - 12 * n * ((n - 4) * m + n * (n + 1) * (n - 2)) * m * x + 16 * m**3 + 4 * n * (n + 2) * m**2)
    form = sp.expand(Q - (1296 * x**3 + (624 * m - 144) * x**2 + 36 * m * (m - 12) * x + 16 * m**3 + 60 * m**2)) == 0
    # 3 < m <= 12: Q - 16 m (m - 3)(m + 9) = 1296 x^3 + (624 m - 144) x^2 + 36 m (12 - m)(1 - x), every term >= 0;
    # m = 12 + p, p >= 0: every coefficient in (p, x) is >= 0, so Q >= Q(x = 0) = 16 m^3 + 60 m^2
    low = sp.factor(16 * m**3 + 60 * m**2 + 36 * m * (m - 12))
    brA = low == 16 * m * (m - 3) * (m + 9) and 624 * 3 - 144 > 0 and sp.expand(
        Q - low - (1296 * x**3 + (624 * m - 144) * x**2 + 36 * m * (12 - m) * (1 - x))) == 0
    brB = all(cf >= 0 for cf in sp.Poly(sp.expand(Q.subs(m, 12 + p)), p, x).coeffs())
    brB &= sp.expand(Q.subs(x, 0) - 16 * m**3 - 60 * m**2) == 0
    q21, l21 = Q.subs({m: 21, x: 0}), low.subs(m, 21)                    # l = 4: the first bound alone fails
    okS = form and brA and brB and q21 < l21
    chk(f"Q = 1296 x^3 + (624 m - 144) x^2 + 36 m (m - 12) x + 16 m^3 + 60 m^2 >= {low} for 3 < m <= 12 and >= 16 "
        f"m^3 + 60 m^2 for m >= 12, x in [0, 1] (the first alone fails at m = 21: {q21} < {l21}): V_S > 0 on r > r_h "
        f"for l >= 2", okS)
    # ingoing Eddington-Finkelstein: Gamma^lam_rr = 0, so the r-row of delta* xi = u is an ODE in r along d_r
    v = sp.Symbol("v", real=True)
    Xe = [v, r, a, b, d]
    ge = sp.zeros(N, N)
    ge[0, 0], ge[0, 1], ge[1, 0] = -f, 1, 1
    ge[2, 2], ge[3, 3], ge[4, 4] = r**2, r**2 * s1**2, r**2 * s1**2 * s2**2
    gei = ge.inv()
    Gr = [sp.simplify(sum(gei[l_, k_] * (2 * sp.diff(ge[k_, 1], Xe[1]) - sp.diff(ge[1, 1], Xe[k_])) for k_ in range(N))
                      / 2) for l_ in range(N)]
    okE = all(q == 0 for q in Gr) and sp.simplify(ge.det() + r**6 * s1**4 * s2**2) == 0
    chk("ingoing Eddington-Finkelstein (v = t + r*): Gamma^lam_rr = 0 and det g = -r^6 sin^4 chi sin^2 theta, regular "
        "across r = r_h", okE)
    # the master fields in ingoing components (dt = dv - dr/f): F_tt = F_vv, F_tr = F_vr + F_vv/f, F_rr = F'_rr + 2
    # F_vr/f + F_vv/f^2 and F_r = F'_r + F_v/f; with e^(-i sigma t) = e^(-i sigma v) e^(i sigma r*), each master field is
    # e^(-i sigma r*) times the expression below, free of 1/f
    Fvv, Fvr, Frr_, FF, Fv, Fr_ = sp.symbols("F_vv F_vr F'_rr F F_v F'_r")
    Ftt, Ftr = Fvv, Fvr + Fvv / f
    Frr = Frr_ + 2 * Fvr / f + Fvv / f**2
    Xk, Yk, Zk = r * (-Ftt / f - 2 * FF), r * (f * Frr - 2 * FF), r * f * Ftr                 # [KI03] (2.20), n = 3
    num_S = sp.cancel(3 * Zk / (sp.I * sig) - r * (Xk + Yk))
    num_V = sp.cancel(r**2 * f * (Fr_ + Fv / f) / (sp.I * sig))                               # Omega = r^2 F^r/(i sigma)
    regular = all(not sp.denom(q).has(mu) for q in (num_S, num_V))
    chk(f"in ingoing components the scalar master field's numerator 3 Z~ - r (X + Y) = {sp.factor(num_S)} and the "
        f"vector Omega = {sp.factor(num_V)}: free of 1/f, so smooth across r = r_h", regular)
    return chk.ok


CHECKS = [("G1 the operator's check; the tensor type: [KI03] (5.3), V_T", g1, 1),
          ("G2 the vector type, l >= 2: gauge, reduction, Omega, the master equation with V_V", g2, 1),
          ("G3 the scalar type, l >= 2: [KI03]'s gauge, (2.24), one constraint, the master equation, det", g3, 1),
          ("G4 the exceptional sectors at sigma != 0: scalar l = 0 and 1, vector l = 1, pure gauge", g4, 1),
          ("G5 the potentials positive for l >= 2; Eddington-Finkelstein: the r-row, the master fields", g5, 1)]


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
    print(f"gmodes5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"gmodes5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest(verbose="--verbose" in args) else 1)
