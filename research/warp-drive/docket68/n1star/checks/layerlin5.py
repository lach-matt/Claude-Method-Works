#!/usr/bin/env python3
"""layerlin5.py -- the term linear in the wave at the boundary x_K = 1 in the equality layer (EQUALITY5-LAYER.md,
Proposition L.2 and section 4).

Five-dimensional Schwarzschild-Tangherlini of mass mu0 (the seed; the background of the linear part) in the
Eddington-Finkelstein coordinates (v, r, th, phi1, phi2) of ansatz5.py, g = -F dv^2 + 2 dv dr + r^2 sigma, F = 1 -
mu0/r^2, sigma = dth^2 + cos^2 th dphi1^2 + sin^2 th dphi2^2; ell = g^-1 dv = d_r.  The linearised operators of the
paper's gauge (wave-map gauge relative to the background, section 2.5): dD^rho = g^ab dGamma^rho_ab and dRic^H = dRic
- (1/2)(g nabla dD + g nabla dD), dGamma built from nabla h, computed covariantly from scratch.  A profile is H(v, r,
th) e^(i v/lam); the two-scale parts are the coefficients of lam^-2, lam^-1, lam^0.  T^2 x Z2 x Z2 invariance leaves the
components vv, vr, rr, vth, rth, thth, phi1phi1, phi2phi2, all arbitrary functions of (v, r, th).  S := {h : h_vv =
h_vr = h_rr = 0, sigma^AB h_AB = 0}.  Zero tests are exact: derivatives of the free functions become symbols, sin th
and cos th become rational in t = tan(th/2), r = q^2, and the result is cancelled.

  N0 (exact) g1^-1 = g0^-1 - g0^-1 k g0^-1 + g0^-1 k g0^-1 k g1^-1 for k = g1 - g0 (Lemma L.1's expansion), on random
     rational symmetric 5x5 matrices.  Control: without the last term it fails.
  N1 (exact, every function) (a) for every h in S: (dRic^H h)_vv = 0 and tr_g dRic^H h = 0.  Control: h_vr != 0 gives
     (dRic^H h)_vv != 0.  (b) the two-scale operators: the lam^-2 part of dRic^H vanishes (g^-1(dv, dv) = 0); its
     lam^-1 part is T(H) := -i (nabla_ell + 3/(2r)) H, componentwise as tabulated in TAB below (vv: -i(d_r H_vv + 3
     H_vv/(2r) + 2 mu0 H_vr/r^3), ...); the lam^-1 part of dD is i Pol(H), Pol_v = -(1/2)(F H_rr + r^-2 tr_sigma H),
     Pol_r = H_rr, Pol_th = H_rth, the others 0.
  N2 (exact) Pol^+ of Lemma 6.2(i) (Pol^T (Pol Pol^T)^-1, transposes in the Euclidean structure of the Cartesian
     (tau, x), here the Frobenius product in a Euclidean-orthonormal Cartesian frame at the point): for a covector
     (V_v, V_r, V_th, 0, 0), Pol^+ V has vv = V_r/4, vr = -V_r/2, rr = V_r, trace -V_r - 2 V_v, vth = -V_th/2, rth =
     V_th, and the tangential V_th reaches no vv, vr, rr or trace.  Pol(Pol^+ V) = V; Pol^+ V is Frobenius-orthogonal
     to dv dv and dv dr + dr dv (two kernel directions).  Control: Pol^T without its trace term misses Pol(Pol^+ V) = V.
  N3 (exact, every angular profile a(th), b(th) and envelope E(v)) H1 := A E r^(1/2) diag(-(a + b), cos^2 a, sin^2 b)
     on (th, phi1, phi2) -- the wave of section 2.4 is the real part with a = 2 p1, b = 2 p2 per unit amplitude -- is
     polarised and transported; D_X H1 = A E r^(-3/2) tau dth, tau = ((a - b) - 3 (a + b) cos 2th)/sin 2th - (a + b)';
     R_X(H1) has no vv, vr, rr, vth component.  The supplement's next profile, data i Pol^+(D_X H1) on Sigma_tau0 (at
     r = r0 = v - tau0, Lemma 6.2(i)), is H2: rth = i A E tau r^(-3/2), vth = i A E tau r^(-1/2) beta(r), beta := -1/(2
     r0) + (mu0/3)(r^-3 - r0^-3), AB = -i r^(1/2) int_(r0)^r s^(-1/2) R_X(H1)_AB ds, others 0; it solves T(H2) +
     R_X(H1) = 0 (all 15 components) and i Pol(H2) + D_X H1 = 0 (all 5), and lies in S.  Control: beta without its
     mass term violates the vth equation.
  N4 (exact) D_X H2 = i A E d (r^(-5/2) beta, r^(-7/2), *, 0, 0) with d := (cos sin)^-1 d_th(cos sin tau) = div div T
     on S^3; R_X(H2)_vv = 0 and tr R_X(H2) = 0 (N1 (a)).  The scalar sector of H3 (vv, vr, rr, trace) built from the
     gauge, the trace transport and the vv transport with the data i Pol^+(D_X H2) at r0 satisfies T(H3) + R_X(H2) = 0
     in vv, vr, rr and trace, and i Pol(H3) + D_X H2 = 0 in v and r.  Control: H3_vv transported without the mass
     coupling 2 mu0 H_vr/r^3 violates the vv equation.
  N5 (exact) At the horizon r = sqrt(mu0): H3_vv = A E d K(r0), K = -mu0^(-7/4) (2 rho^3 - 3 rho^2 - 2)^2/(36 rho^6),
     rho := r0/sqrt(mu0) -- a negative square, zero only at rho* = 1.80644... (the real root, double), and -mu0^(-7/4)/9
     as r0 -> infinity (data at past null infinity).  K = -r_h^(-3/2) beta(r_h)^2 (beta(r_h): the radial factor of
     H2_vth at the horizon, squared).  Control: a transverse angular tensor (a, b) = ((1 + 3 cos 2th)/2, (1 - 3 cos
     2th)/2) has tau = 0, so d = 0 and no signal.
  N6 (exact) For the paper's wave, T = T^G - i T^F: d^F = sqrt2 P(zeta)/(1 + zeta^2)^(5/2), d^G = sqrt2 P(-zeta)/(1 +
     zeta^2)^(5/2), zeta = cos 2th, P = -2 zeta^5 - (20/3) zeta^3 - (20/3) zeta^2 - (38/3) zeta + 4/3; gcd(P(zeta),
     P(-zeta)) = 1, so |d|^2 = (d^F)^2 + (d^G)^2 > 0 at every angle.  Control: one quadrature alone vanishes at one
     angle (P has one root in [-1, 1]).

Labels: computed (exact, sympy).  The identification of H1, H2, H3 with the linear part of the supplement's approximant
is deduced in the note (Lemmas 5.1-5.3, 6.2 of N1STAR-PROOF.md, READ), not computed here.
Run: python3 checks/layerlin5.py   (about five minutes)
"""
import random
import sys
import time

import sympy as sp
import builtins                                                                   # noqa: E402
import textwrap                                                                   # noqa: E402


def print(*args, **kw):                                                           # noqa: A001
    """the builtin print, wrapped at 121 columns (Round 3: every file within 121 characters)"""
    builtins.print(textwrap.fill(" ".join(str(a) for a in args), width=121, subsequent_indent="      ",
                                 break_on_hyphens=False), **kw)

v, r, th, p1, p2 = sp.symbols('v r theta phi1 phi2', real=True)
mu0, lam, A, r0 = sp.symbols('mu0 lam A r0', positive=True)
q, t = sp.symbols('q t', positive=True)
I = sp.I
X = [v, r, th, p1, p2]
n = 5
F = 1 - mu0/r**2
c, s = sp.cos(th), sp.sin(th)
g = sp.diag(-F, 0, r**2, r**2*c**2, r**2*s**2)
g[0, 1] = g[1, 0] = 1
gi = sp.simplify(g.inv())
Gam = [[[sp.simplify(sum(gi[a_, d]*(sp.diff(g[d, b_], X[cc]) + sp.diff(g[d, cc], X[b_]) - sp.diff(g[b_, cc], X[d]))
                         for d in range(n))/2) for cc in range(n)] for b_ in range(n)] for a_ in range(n)]
a = sp.Function('a')(th)
b = sp.Function('b')(th)
E = sp.Function('E')(v)
T0 = time.time()


def ops(H, twoscale=True):
    """(dRic^H, dD lowered) of h = H e^(i v/lam), divided by the phase (twoscale) or of h = H"""
    if twoscale:
        D = lambda e, k: sp.diff(e, X[k]) + (I/lam*e if k == 0 else 0)          # noqa: E731
    else:
        D = lambda e, k: sp.diff(e, X[k])                                         # noqa: E731
    Dh = [[[D(H[i, j], cc) - sum(Gam[d][cc][i]*H[d, j] + Gam[d][cc][j]*H[i, d] for d in range(n))
            for j in range(n)] for i in range(n)] for cc in range(n)]
    dG = [[[sum(gi[i, d]*(Dh[j][d][cc] + Dh[cc][d][j] - Dh[d][j][cc]) for d in range(n))/2 for cc in range(n)]
           for j in range(n)] for i in range(n)]
    DdG = [[[[D(dG[i][j][cc], e) + sum(Gam[i][e][d]*dG[d][j][cc] - Gam[d][e][j]*dG[i][d][cc]
                                       - Gam[d][e][cc]*dG[i][j][d] for d in range(n))
              for cc in range(n)] for j in range(n)] for i in range(n)] for e in range(n)]
    dRic = [[sum(DdG[i][i][j][cc] for i in range(n)) - sum(DdG[cc][i][i][j] for i in range(n)) for cc in range(n)]
            for j in range(n)]
    dD = [sum(gi[i, j]*dG[rho][i][j] for i in range(n) for j in range(n)) for rho in range(n)]
    dDl = [sum(g[m, rho]*dD[rho] for rho in range(n)) for m in range(n)]
    DD = [[D(dDl[m], nn) - sum(Gam[d][nn][m]*dDl[d] for d in range(n)) for m in range(n)] for nn in range(n)]
    R = sp.Matrix(n, n, lambda m, nn: dRic[m][nn] - (DD[nn][m] + DD[m][nn])/2)
    return R, sp.Matrix(dDl)


def is_zero(e):
    e = sp.expand(e)
    rep = {}
    ders = sorted(e.atoms(sp.Derivative), key=lambda x: -sum(cnt for _, cnt in x.variable_count))
    for k, dd in enumerate(ders):
        rep[dd] = sp.Symbol('D%d' % k)
    e = e.xreplace(rep)
    for f in e.atoms(sp.Function):
        if isinstance(f, sp.core.function.AppliedUndef):
            e = e.xreplace({f: sp.Symbol('F_' + str(f.func))})
    e = sp.expand_trig(e)
    e = e.xreplace({sp.sin(th): 2*t/(1 + t**2), sp.cos(th): (1 - t**2)/(1 + t**2), sp.tan(th): 2*t/(1 - t**2)})
    e = e.subs(r, q**2)
    return sp.cancel(sp.together(e)) == 0


def trace(M):
    return sum(gi[i, j]*M[i, j] for i in range(n) for j in range(n))


def tr_sigma(H):
    return H[2, 2] + H[3, 3]/c**2 + H[4, 4]/s**2


def T_tab(H):
    """the lam^-1 part of dRic^H, as tabulated (N1 (b) checks it against the computed operator)"""
    Dr = lambda e: sp.diff(e, r)                                                  # noqa: E731
    M = sp.zeros(n)
    M[0, 0] = -I*(Dr(H[0, 0]) + 3*H[0, 0]/(2*r) + 2*mu0*H[0, 1]/r**3)
    M[0, 1] = -I*(Dr(H[0, 1]) + 3*H[0, 1]/(2*r) + mu0*H[1, 1]/r**3)
    M[1, 1] = -I*(Dr(H[1, 1]) + 3*H[1, 1]/(2*r))
    M[0, 2] = -I*(Dr(H[0, 2]) + H[0, 2]/(2*r) + mu0*H[1, 2]/r**3)
    M[1, 2] = -I*(Dr(H[1, 2]) + H[1, 2]/(2*r))
    for k in (2, 3, 4):
        M[k, k] = -I*(Dr(H[k, k]) - H[k, k]/(2*r))
    for i in range(n):
        for j in range(i):
            M[i, j] = M[j, i]
    return M


def pol_tab(H):
    return sp.Matrix([-(F*H[1, 1] + tr_sigma(H)/r**2)/2, H[1, 1], H[1, 2], 0, 0])


def general_H(only=None):
    names = {(0, 0): 'Hvv', (0, 1): 'Hvr', (1, 1): 'Hrr', (0, 2): 'Hvt', (1, 2): 'Hrt', (2, 2): 'Htt',
             (3, 3): 'H11', (4, 4): 'H22'}
    H = sp.zeros(n)
    for (i, j), nm in names.items():
        if only is None or (i, j) in only:
            H[i, j] = H[j, i] = sp.Function(nm)(v, r, th)
    return H


# ------------------------------------------------------------------------------------------------------------ N0
def n0(control=False):
    rng = random.Random(5)
    ok = True
    for _ in range(3):
        def sym():
            M = sp.Matrix(5, 5, lambda i, j: 0)
            for i in range(5):
                for j in range(i, 5):
                    M[i, j] = M[j, i] = sp.Rational(rng.randint(-9, 9), rng.randint(1, 9))
            return M
        g0m = sym() + 10*sp.eye(5)
        km = sym()/7
        g1m = g0m + km
        i0, i1 = g0m.inv(), g1m.inv()
        rhs = i0 - i0*km*i0 + (sp.zeros(5) if control else i0*km*i0*km*i1)
        ok &= (i1 - rhs) == sp.zeros(5)
    return ok


# ------------------------------------------------------------------------------------------------------------ N1
def n1(control=False):
    if control:
        H = general_H(only=[(0, 1), (0, 2), (1, 2), (3, 3), (4, 4)])
    else:
        H = general_H(only=[(0, 2), (1, 2), (3, 3), (4, 4)])
    H[2, 2] = -(H[3, 3]/c**2 + H[4, 4]/s**2)
    R, _ = ops(H, twoscale=False)
    vv0, tr0 = is_zero(R[0, 0]), is_zero(trace(R))
    if control:
        return vv0
    Hg = general_H()
    R2, D2 = ops(Hg)
    m2 = all(is_zero(sp.expand(R2[i, j]).coeff(lam, -2)) for i in range(n) for j in range(i, n))
    Tt = T_tab(Hg)
    m1 = all(is_zero(sp.expand(R2[i, j]).coeff(lam, -1) - Tt[i, j]) for i in range(n) for j in range(i, n))
    pt = pol_tab(Hg)
    mp_ = all(is_zero(sp.expand(D2[k]).coeff(lam, -1) - I*pt[k]) for k in range(n))
    mp0 = all(is_zero(sp.expand(D2[k]).coeff(lam, -2)) for k in range(n))
    print("  N1 (a) on S: (dRic^H h)_vv = 0: %s, tr = 0: %s; (b) lam^-2 part 0: %s, lam^-1 part = T (15 comps): %s,"
          " dD: lam^-2 part 0: %s, lam^-1 part = i Pol: %s  [%.0f s]" % (vv0, tr0, m2, m1, mp0, mp_, time.time() - T0),
          flush=True)
    return vv0 and tr0 and m2 and m1 and mp_ and mp0


# ------------------------------------------------------------------------------------------------------------ N2
J = sp.zeros(5)
J[0, 0] = 1
J[0, 1] = -1
J[1, 1] = 1
J[2, 2] = r
J[3, 3] = r*c
J[4, 4] = r*s
Jinv = J.inv()
dvE = sp.Matrix([1, 0, 0, 0, 0])
ellE = gi*dvE
ellB = J*ellE
GB = J*gi*J.T
dvB = Jinv.T*dvE


def polT(psi, mut=False):
    return (ellB*psi.T + psi*ellB.T)/2 - (0 if mut else 1)*(dvB.T*psi)[0]*GB/2


def polB(YB):
    tr = sum(GB[i, j]*YB[i, j] for i in range(5) for j in range(5))
    return sp.Matrix([sum(ellB[i]*YB[i, k] for i in range(5)) - dvB[k]*tr/2 for k in range(5)])


def polplus(VEF, mut=False):
    VB = Jinv.T*VEF
    PP = sp.Matrix.hstack(*[polB(polT(sp.Matrix([1 if k == m else 0 for k in range(5)]), mut)) for m in range(5)])
    ZB = polT(PP.LUsolve(VB), mut)
    return (J.T*ZB*J).applyfunc(sp.simplify), ZB


Vv, Vr, Vt = sp.symbols('V_v V_r V_t')


def n2(control=False):
    Z, ZB = polplus(sp.Matrix([Vv, Vr, Vt, 0, 0]), mut=control)
    tr = sp.simplify(trace(Z))
    back = pol_tab(Z)
    inv_ok = all(sp.simplify(back[k] - [Vv, Vr, Vt, 0, 0][k]) == 0 for k in range(5))
    if control:
        return inv_ok
    vals = [Z[0, 0] - Vr/4, Z[0, 1] + Vr/2, Z[1, 1] - Vr, tr + Vr + 2*Vv, Z[0, 2] + Vt/2, Z[1, 2] - Vt]
    tab = all(sp.simplify(x) == 0 for x in vals)
    # Frobenius orthogonality (in the frame B) to two kernel directions of Pol
    k1 = Jinv.T*(dvE*dvE.T)*Jinv
    drE = sp.Matrix([0, 1, 0, 0, 0])
    k2 = Jinv.T*(dvE*drE.T + drE*dvE.T)*Jinv
    kern = all(sp.simplify(polB(k)[m]) == 0 for k in (k1, k2) for m in range(5))
    orth = all(sp.simplify(sum(ZB[i, j]*k[i, j] for i in range(5) for j in range(5))) == 0 for k in (k1, k2))
    print("  N2 Pol^+ (V_v, V_r, V_th): vv %s, vr %s, rr %s, trace %s, vth %s, rth %s; table: %s; Pol Pol^+ = 1: %s;"
          " kernel directions: %s, orthogonal to them: %s" % (Z[0, 0], Z[0, 1], Z[1, 1], tr, Z[0, 2], Z[1, 2], tab,
                                                              inv_ok, kern, orth), flush=True)
    return tab and inv_ok and kern and orth


# ------------------------------------------------------------------------------------------------------------ N3
TAU = ((a - b) - 3*(a + b)*sp.cos(2*th))/sp.sin(2*th) - sp.diff(a + b, th)
DIV2 = sp.diff(c*s*TAU, th)/(c*s)
BETA = -1/(2*r0) + mu0/3*(r**-3 - r0**-3)
STATE = {}


def rint(expr, lo, hi, var):
    """integral of a Laurent polynomial in var^(1/2), termwise; a logarithm is refused"""
    e = sp.expand(expr.subs(var, q**2)*2*q)
    P = sp.Poly(sp.expand(e*q**40), q)
    out = 0
    for (k,), co in P.terms():
        p = k - 40
        if p == -1:
            raise ValueError('logarithm')
        out += co*(sp.sqrt(hi)**(p + 1) - sp.sqrt(lo)**(p + 1))/(p + 1)
    return sp.expand(out)


def build_H2(RX1, mass=True):
    beta = BETA if mass else -1/(2*r0)
    H2 = sp.zeros(n)
    H2[1, 2] = H2[2, 1] = I*A*E*TAU*r**sp.Rational(-3, 2)
    H2[0, 2] = H2[2, 0] = I*A*E*TAU*beta/sp.sqrt(r)
    sR = sp.Symbol('sR', positive=True)
    for k in (2, 3, 4):
        H2[k, k] = -I*sp.sqrt(r)*rint(RX1[k, k].subs(r, sR)/sp.sqrt(sR), r0, r, sR)
    return H2


def n3(control=False):
    if control:
        RX1 = STATE['RX1']
        H2m = build_H2(RX1, mass=False)
        return is_zero(T_tab(H2m)[0, 2] + RX1[0, 2])
    T = sp.diag(0, 0, -(a + b), c**2*a, s**2*b)
    H1 = A*E*sp.sqrt(r)*T
    R1, D1 = ops(H1)
    h1 = all(is_zero(sp.expand(R1[i, j]).coeff(lam, k)) for i in range(n) for j in range(i, n) for k in (-2, -1))
    h1 &= all(is_zero(sp.expand(D1[k]).coeff(lam, -1)) for k in range(n))
    RX1 = R1.applyfunc(lambda e: sp.expand(e).coeff(lam, 0))
    DX1 = D1.applyfunc(lambda e: sp.expand(e).coeff(lam, 0))
    dx1 = all(is_zero(DX1[k] - [0, 0, A*E*r**sp.Rational(-3, 2)*TAU, 0, 0][k]) for k in range(n))
    rx1 = all(is_zero(RX1[i, j]) for (i, j) in ((0, 0), (0, 1), (1, 1), (0, 2)))
    H2 = build_H2(RX1)
    Z, _ = polplus(sp.Matrix([Vv, Vr, Vt, 0, 0]))
    dat = Z.subs({Vv: DX1[0], Vr: DX1[1], Vt: DX1[2]}).subs(r, r0)
    data = all(is_zero(H2.subs(r, r0)[i, j] - I*dat[i, j]) for i in range(n) for j in range(n))
    Tt = T_tab(H2)
    eqR = all(is_zero(Tt[i, j] + RX1[i, j]) for i in range(n) for j in range(i, n))
    pt = pol_tab(H2)
    eqD = all(is_zero(I*pt[k] + DX1[k]) for k in range(n))
    inS = all(H2[i, j] == 0 for (i, j) in ((0, 0), (0, 1), (1, 1))) and is_zero(tr_sigma(H2))
    STATE.update(RX1=RX1, H2=H2)
    print("  N3 H1 polarised and transported: %s; D_X H1 = A E r^-3/2 tau dth: %s; R_X(H1) vv, vr, rr, vth = 0: %s;"
          " H2 has the data i Pol^+(D_X H1) at r0: %s; T(H2) + R_X(H1) = 0 (15): %s; i Pol(H2) + D_X H1 = 0 (5): %s;"
          " H2 in S: %s  [%.0f s]" % (h1, dx1, rx1, data, eqR, eqD, inS, time.time() - T0), flush=True)
    return h1 and dx1 and rx1 and data and eqR and eqD and inS


# ------------------------------------------------------------------------------------------------------------ N4
def n4():
    H2 = STATE['H2']
    R2, D2 = ops(H2)
    RX2 = R2.applyfunc(lambda e: sp.expand(e).coeff(lam, 0))
    DX2 = D2.applyfunc(lambda e: sp.expand(e).coeff(lam, 0))
    dv_ = is_zero(DX2[0] - I*A*E*DIV2*r**sp.Rational(-5, 2)*BETA)
    dr_ = is_zero(DX2[1] - I*A*E*DIV2*r**sp.Rational(-7, 2))
    rvv, rtr = is_zero(RX2[0, 0]), is_zero(trace(RX2))
    # the scalar sector is built from the closed forms just verified (dv_, dr_), so that N5 handles small expressions
    dd = sp.Symbol('dd')
    DXv = I*A*E*dd*r**sp.Rational(-5, 2)*BETA
    DXr = I*A*E*dd*r**sp.Rational(-7, 2)
    Z, _ = polplus(sp.Matrix([Vv, Vr, Vt, 0, 0]))
    sub0 = {Vv: DXv.subs(r, r0), Vr: DXr.subs(r, r0), Vt: 0}
    Z0 = (I*Z.subs(r, r0)).subs(sub0)
    tr0 = I*(-Vr - 2*Vv).subs(sub0)
    H3 = sp.zeros(n)
    H3[1, 1] = I*DXr
    trH3 = r0**sp.Rational(3, 2)*tr0*r**sp.Rational(-3, 2)
    H3[0, 1] = H3[1, 0] = trH3/2 + I*DXv
    phi = (trH3 - 2*H3[0, 1] - F*H3[1, 1])/3
    H3[2, 2], H3[3, 3], H3[4, 4] = phi*r**2, phi*r**2*c**2, phi*r**2*s**2
    sR = sp.Symbol('sR', positive=True)
    integrand = (-(2*mu0/r**3)*r**sp.Rational(3, 2)*H3[0, 1]).subs(r, sR)
    H3[0, 0] = (r0**sp.Rational(3, 2)*Z0[0, 0] + rint(integrand, r0, r, sR))*r**sp.Rational(-3, 2)
    STATE.update(H3sym=H3.copy(), dd=dd)
    H3 = H3.subs(dd, DIV2)
    Z0 = Z0.subs(dd, DIV2)
    tr0 = tr0.subs(dd, DIV2)
    data = (is_zero(H3[0, 0].subs(r, r0) - Z0[0, 0]) and is_zero(H3[0, 1].subs(r, r0) - Z0[0, 1])
            and is_zero(H3[1, 1].subs(r, r0) - Z0[1, 1]) and is_zero(trace(H3).subs(r, r0) - tr0))
    Tt = T_tab(H3)
    eqs = [is_zero(Tt[i, j] + RX2[i, j]) for (i, j) in ((0, 0), (0, 1), (1, 1))]
    eqtr = is_zero(trace(Tt))                       # and tr R_X(H2) = 0 above
    pt = pol_tab(H3)
    eqD = [is_zero(I*pt[k] + DX2[k]) for k in (0, 1)]
    # control: the vv transport without its mass coupling 2 mu0 H_vr/r^3 (the source of the signal) must fail
    Hm = STATE['H3sym'].copy()
    Hm[0, 0] = (r0**sp.Rational(3, 2)*STATE['H3sym'][0, 0].subs(r, r0))*r**sp.Rational(-3, 2)
    ctl = is_zero(T_tab(Hm.subs(dd, DIV2))[0, 0] + RX2[0, 0])
    STATE.update(H3=H3, n4ctl=ctl)
    print("  N4 D_X H2 = i A E d (r^-5/2 beta, r^-7/2): %s, %s; R_X(H2) vv = 0: %s, trace 0: %s; H3 data at r0: %s;"
          " T(H3) + R_X(H2) = 0 in vv, vr, rr: %s, trace: %s; i Pol(H3) + D_X H2 = 0 in v, r: %s  [%.0f s]"
          % (dv_, dr_, rvv, rtr, data, eqs, eqtr, eqD, time.time() - T0), flush=True)
    return dv_ and dr_ and rvv and rtr and data and all(eqs) and eqtr and all(eqD)


# ------------------------------------------------------------------------------------------------------------ N5
rho = sp.Symbol('rho', positive=True)
KCLOSED = -mu0**sp.Rational(-7, 4)*(2*rho**3 - 3*rho**2 - 2)**2/(36*rho**6)


def n5(control=False):
    if control:
        ac, bc = (1 + 3*sp.cos(2*th))/2, (1 - 3*sp.cos(2*th))/2
        tau_c = sp.simplify(TAU.subs({a: ac, b: bc}).doit())
        return tau_c != 0
    K = sp.simplify(STATE['H3sym'][0, 0].subs(r, sp.sqrt(mu0))/(A*E*STATE['dd']))
    Kr = sp.simplify(K.subs(r0, rho*sp.sqrt(mu0)))
    closed = sp.simplify(Kr - KCLOSED) == 0
    rh = sp.sqrt(mu0)
    viabeta = sp.simplify(Kr + rh**sp.Rational(-3, 2)*(BETA.subs(r, rh).subs(r0, rho*rh))**2) == 0
    clean = sp.simplify(sp.limit(Kr, rho, sp.oo) + mu0**sp.Rational(-7, 4)/9) == 0
    P = sp.Poly(2*rho**3 - 3*rho**2 - 2, rho)
    roots = [x for x in P.nroots() if abs(sp.im(x)) < 1e-30]
    rstar = roots[0]
    d2 = sp.diff(Kr*mu0**sp.Rational(7, 4), rho, 2).subs(rho, rstar)
    print("  N5 K(r0) = H3_vv(sqrt mu0)/(A E d) = %s; the closed form: %s; = -r_h^-3/2 beta(r_h)^2: %s;"
          " r0 -> oo: -mu0^-7/4/9: %s; real root rho* = %s (one real root, double in K), K'' there %s"
          % (sp.factor(Kr), closed, viabeta, clean, sp.N(rstar, 12), sp.N(d2, 6)), flush=True)
    return closed and viabeta and clean and len(roots) == 1 and abs(d2) > 0


# ------------------------------------------------------------------------------------------------------------ N6
def n6(control=False):
    U = sp.Symbol('U', positive=True)
    z = sp.Symbol('zeta')
    h = sp.sqrt(2)/sp.sqrt(1 + sp.cos(2*th)**2)
    P = -2*z**5 - sp.Rational(20, 3)*z**3 - sp.Rational(20, 3)*z**2 - sp.Rational(38, 3)*z + sp.Rational(4, 3)
    quads = {'F': (2*(-s**2*h)/3, 2*(2*s**2*h)/3, P), 'G': (2*(2*c**2*h)/3, 2*(-c**2*h)/3, P.subs(z, -z))}
    if control:
        return sp.Poly(P, z).count_roots(-1, 1) == 0
    ok = True
    for nm, (aa, bb, PP) in quads.items():
        dq = DIV2.subs({a: aa, b: bb}).doit()
        e = dq - sp.sqrt(2)*PP.subs(z, sp.cos(2*th))/(1 + sp.cos(2*th)**2)**sp.Rational(5, 2)
        e = sp.expand(e).subs(1 + sp.cos(2*th)**2, U)
        e = sp.expand(sp.powsimp(sp.expand(e*U**sp.Rational(5, 2)), force=True)).subs(U, 1 + sp.cos(2*th)**2)
        ok &= is_zero(e)
    gcd = sp.gcd(sp.Poly(P, z), sp.Poly(P.subs(z, -z), z))
    nroot = sp.Poly(P, z).count_roots(-1, 1)
    print("  N6 d^F, d^G = sqrt2 P(+-zeta)/(1 + zeta^2)^(5/2) exactly: %s; gcd(P(zeta), P(-zeta)) = %s; roots of P in"
          " [-1, 1]: %d" % (ok, gcd.as_expr(), nroot), flush=True)
    return ok and gcd.as_expr() == 1 and nroot == 1


def main():
    ok = True
    for name, f in (("N0", n0), ("N1", n1), ("N2", n2), ("N3", n3)):
        good = f()
        ctl = f(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    good = n4()
    ctl = STATE['n4ctl']
    print("N4 %s%s" % ("PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""), flush=True)
    ok &= good and not ctl
    for name, f in (("N5", n5), ("N6", n6)):
        good = f()
        ctl = f(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    print("layerlin5: %s  [%.0f s]" % ("all checks pass, every control fails" if ok else "FAILURES", time.time() - T0))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
