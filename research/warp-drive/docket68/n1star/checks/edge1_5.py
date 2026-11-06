#!/usr/bin/env python3
"""edge1_5.py -- the deep layer and the very edge for Theorem 1's solution (EQUALITY5-LAYER.md, Round 5, R5.3:
Lemma H_Sigma, Lemma L.21 (the first-degree constraint correction), Proposition L.22 (the two-term formula), Lemma W,
Theorem L_1E).

With stage N's data fixed by Lemma 6.2's rule (D615), the A-linear part h1 of g_lam is the linear solution of the
seed's reduced operator with the A-linear Cauchy data: those of h_app1 := Re sum_(j<=N+1) lam^j H_j e^(i v/lam) and
the A-linear part U1 of Proposition 6.5's correction.  On the deep layer the horizon value of h1 is the sum of two
terms: the stage term lam^3 A nu d env (Theorem L's) and a term carried by U1, which grows like lam^(N+1)
env^(N-1) and dominates once lam^(N-2) env^(N-1)/env >> 1.  This program computes the pieces of that formula.

  X1 (exact, every component) The characteristic form of the seed's linearised reduced operator in (v, r): with P :=
     i T (T of layerlin5's table) and L := d_v + (F/2) d_r (the outgoing null direction), dRic^H(h) + P(L h) contains
     no v-derivative and no second r-derivative (Q~ below), for every T^2 x Z2 x Z2-invariant h.  So along ell, P(L h)
     = Q~ h + source, and at the horizon L = d_v.  Control: L with F/4 in place of F/2 leaves d_r^2 terms.
  X2 (exact) The outgoing form: in the outgoing coordinates (u, r), g0 = -F du^2 - 2 du dr + r^2 sigma, dRic^H(h) has
     no d_u^2 and no d_u d_th, d_u d_phi terms (it is -P' d_u h + Q' h with P' of first order in r and Q' free of
     d_u): a leading outgoing solution e^(i psi(u)/lam) chi(u) c0(r; u), P' c0 = 0, has residual e^(i psi/lam) Q'(chi
     c0), free of 1/lam.  Control: in the Kerr-Schild (tau, r), where g0^-1(dtau, dtau) != 0, d_tau^2 terms occur.
  X3 (exact) The leading projection and transport: on Sigma the null covectors with tangential part s dr are s dtau
     (ingoing) and -F s/(2 - F) dtau (outgoing); the ingoing amplitude of data (X, Xdot) is (F X + (2 - F) Xdot/s)/2 =
     (L X)/s; and the T = 0 transport of the scalar sector (vv, vr, rr) from r0 to sqrt(mu0) gives H_vv(sqrt mu0) =
     mu0^(-3/4) r0^(3/2) [X_vv + F(r0) X_vr + F(r0)^2 X_rr/4] (closed form checked against layerlin5's T_tab, whose
     vv, vr, rr rows N1 (b) checks against the computed operator).  Control: the transport with the vv mass coupling
     dropped does not solve T_tab = 0.
  X4 (exact) The first-degree constraint residual, rho component: for a covector field D = e^(i v/lam) (E1(v) f(r)
     tau(th) dth + E0(v) d(th) (p(r) dv + q(r) dr)), 2 Gt(S(D))(n, n) has no s E1 term (s E := E' + i E/lam), its E1
     coefficient is f d/r^2 (d := (cos sin)^-1 d_th(cos sin tau)) and its s E0 coefficient d (2 (n.dv) D0(n) +
     g0^-1(dv, D0)); with the families of D_X H_(N+1) on Sigma (X5) it is lam^(N+1) i^N A d r0^(-7/2) [env^(N) - c_N
     s env^(N-1)], c_N := N mu0/(r0^2 + mu0).  Control: S(D) in place of Gt(S(D)) breaks the formula.
  X5 (exact) The families on Sigma: from L.13 (b) and the data rule i Pol(H_(m+1)) = -D_X H_m on Sigma, the scalar
     part of the next-to-top family of D_X H_(N+1) is N i^(N-1) q(c_20)_sc, q(c_20)_sc = i A d (r^(-5/2) beta, r^(-7/2))
     (layerlin5 N4, READ), and its top family is i^N A tau r^(-3/2) dth (layerlin5 N3, READ); recursion checked N = 2
     ... 40.  Control: the data rule without its factor i gives a different count.
  X6 (exact) alpha, the d_r a coefficient of the scalar constraint at the Kerr-Schild data, in the direction a dr dr:
     3 r^3/(r^2 + mu)^2, with no d_r^2 a (Lemma 6.3, recomputed).  Control: the conformal direction a gamma has d_r^2 a.
  X7 (exact) The data that U1's scalar part a gives on Sigma (spatial part a dr dr; d_tau of it from K fixed; d_tau of
     lapse and shift from D = 0), read with g_(tau mu) kept (reading 1) or with the ADM lapse and shift vector kept
     (reading 2, the supplement's convention, whose section 1 uses the shift as a vector, Z := d_tau - beta_ext): their
     ingoing amplitude, transported, gives H_vv(sqrt mu0) = K_R a with K_R = mu0^(-3/4) r0^(-5/2) (r0^2 - mu0)^2/4
     (reading 1) and mu0^(-3/4) r0^(3/2)/4 (reading 2), both > 0; a third reading (ADM lapse and shift covector kept,
     round 6, the verifier of round 5's m6) gives (r0^2 - 2 mu0)/(4 mu0^(3/4) r0^(1/2)); and K_R does not depend on the
     d_tau gamma_rr datum at all (D = 0 fixes the combination that reaches the horizon; so neither K's sign
     convention nor the shift term enters).  Control: D = 0 without its trace term changes K_R in both readings.
  X8 (exact) Xi(T) := [(1 - c) T - i c]/(T + i), T := lam kappa: |Xi|^2 = [(1 - c)^2 T^2 + c^2]/(T^2 + 1) >= min(c^2,
     (1 - c)^2), zero only as T -> infinity at c = 1; Xi = -c - i T + O(T^2); where the two real leading coefficients
     cancel, the quadrature part is T nu (2 - 1/c) (either relative sign), zero only at c = 1/2.  Control: a sign
     slip in Xi's numerator breaks the lower bound.
  X9 (computed, sampled) Lemma W (two signs on a window of length 4 pi lam) on 4000 random amplitudes, in both cases
     (|S| large with slowly varying phase; |S'| large with a zero inside the window).  Control: |S'| below the bound
     with an adversarial epsilon gives a window with one sign.
  X10 (computed, mpmath, sampled densely; round 6, the verifier of round 5's m2) The hypotheses (H_N) and (H_N') of
     Theorem L_1E and L.16 (c)'s bounds for exp(-1/x) and the record's C_c^inf envelope, at 401 points of [10^-3.5,
     10^-2] with exact derivatives (Bell polynomials in the derivatives of log env): env^(k), k <= 12, positive and
     log-concave with kappa_k/kappa in (1/2, 2); sup |kappa_k'|/kappa_k^(3/2) <= c_R = 3 (alpha = 1/2); sup
     |env^(j)|/(kappa^j env), j <= 13, printed (L.16 (c)'s c_j); and C_- k kappa^(1/2) <= |kappa_k - kappa| <= C_+ k
     kappa^(1/2) with C_- > 0 for 8 <= k <= 12.  Control: the mutant log env = -1/x + 10 sin^16(4 pi log10 x)/x, flat at
     the four points round 5 sampled, fails at the dense ones.
  X11 (computed, mpmath; a model with unit constants) The two-term formula with exp(-1/x), lam = 1e-6, mu0 = A = 1,
     nu = -1/9, Gamma = 1, r0 = 3: S(v) = nu env (1 + 2 i lam kappa) - i^N Xi lam^(N-2) env^(N-1) (exact derivatives,
     exact Xi) for N = 9 (quadrature) and N = 12 (the real parts cancel at the crossover), over 2400 windows from
     env = lam^4 to x = 0.2 lam^(1/2), with L.22's cutoff of the stage term at lam kappa > 1 (round 6, the verifier of
     round 5's m1): every window has both signs of -Re[S e^(i v/lam)] - m0 +- D2.  Control: S_U removed leaves windows
     with one sign (the U^(1) term is what decides the very edge).

  X12 (computed, mpmath; a model with unit constants; round 6, the verifier of round 5's MAJOR 1 (a)) The crossover
     for N = 12, lam = 1e-10, where the two real parts cancel, decided by Lemma W (B) applied to sigma := S/(lam^3 A d
     env), env factored out: with an adversarial O(T) relative error that cancels the quadrature part at the cancellation
     and a non-explicit error of size (lam + 1/kappa)|nu|, every window of the 81 around it has |sigma'| >= |nu|
     kappa^(1/2), |sigma''| <= |sigma'|/(80 pi lam) and the non-harmonic error below pi lam |sigma'|/5, and has both
     signs.  Control: Lambda frozen at its crossover value (no transversality) violates (B)'s first condition.

Labels: X1-X8 computed (exact, sympy); X9, X10 computed, sampled; X11, X12 computed (mpmath), models with unit
constants.
Inputs READ: layerlin5 N3, N4 (H_2, D_X H_2), L.13 (b) (round 3).  Run: python3 checks/edge1_5.py  (about 15 minutes)
"""
import os
import random
import sys
import textwrap
import time

import mpmath as mp
import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import layerlin5 as L                                                             # noqa: E402

T0 = time.time()
I = sp.I


def out(msg):
    print(textwrap.fill(msg, width=121, subsequent_indent="      ", break_on_hyphens=False), flush=True)


def ders(e, bad_if):
    """the derivative atoms d of the free functions in e with bad_if({variable: count}) and a coefficient that is not
    identically zero (exact test of layerlin5, after cancelling trigonometric identities)"""
    e = sp.expand(e)
    atoms = list(e.atoms(sp.Derivative))
    rep = {d: sp.Symbol('DD%d' % k) for k, d in enumerate(atoms)}
    e2 = e.xreplace(rep)
    res = []
    for d in atoms:
        vc = dict((str(vv), cnt) for vv, cnt in d.variable_count)
        if bad_if(vc) and not L.is_zero(sp.diff(e2, rep[d])):
            res.append((str(d.expr.func), tuple(sorted(vc.items()))))
    return res


# ------------------------------------------------------------------------------------------------------------ X1
CACHE = {}


def e1(control=False):
    Hg = L.general_H()
    if 'R' not in CACHE:
        CACHE['R'] = L.ops(Hg, twoscale=False)[0]
    R = CACHE['R']
    half = sp.Rational(1, 4) if control else sp.Rational(1, 2)
    LH = Hg.applyfunc(lambda x: sp.diff(x, L.v) + half*L.F*sp.diff(x, L.r))
    PL = (I*L.T_tab(LH)).applyfunc(sp.expand)
    bad = []
    for i in range(L.n):
        for j in range(i, L.n):
            for nm, vc in ders(R[i, j] + PL[i, j], lambda vc: vc.get('v', 0) > 0 or vc.get('r', 0) > 1):
                bad.append((i, j, nm, vc))
    if control:
        return not bad
    out("  X1 dRic^H(h) + P(L h), L = d_v + (F/2) d_r, P = i T: v-derivatives or d_r^2 in any of the 15 components:"
        " %s  [%.0f s]" % (bad or "none", time.time() - T0))
    return not bad


# ------------------------------------------------------------------------------------------------------------ X2
def ops_metric(g, X, H):
    """dRic^H of h = H (no phase) for the background g in the coordinates X (wave-map gauge relative to g)"""
    n = len(X)
    gi = sp.simplify(g.inv())
    Gam = [[[sp.simplify(sum(gi[a_, d]*(sp.diff(g[d, b_], X[cc]) + sp.diff(g[d, cc], X[b_]) - sp.diff(g[b_, cc], X[d]))
                             for d in range(n))/2) for cc in range(n)] for b_ in range(n)] for a_ in range(n)]
    D = lambda e, k: sp.diff(e, X[k])                                             # noqa: E731
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
    return sp.Matrix(n, n, lambda m, nn: dRic[m][nn] - (DD[nn][m] + DD[m][nn])/2)


def e2(control=False):
    u = sp.Symbol('u', real=True)
    r, th, p1, p2, mu0 = L.r, L.th, L.p1, L.p2, L.mu0
    F = 1 - mu0/r**2
    c, s = sp.cos(th), sp.sin(th)
    X = [u, r, th, p1, p2]
    g = sp.diag(-F, 0, r**2, r**2*c**2, r**2*s**2)
    if control:          # Kerr-Schild time tau (v = tau + r): g = -F dtau^2 + 2 (1 - F) dtau dr + (2 - F) dr^2 + ...
        g[1, 1] = 2 - F
        g[0, 1] = g[1, 0] = 1 - F
    else:
        g[0, 1] = g[1, 0] = -1
    names = {(0, 0): 'Huu', (0, 1): 'Hur', (1, 1): 'Hrr', (0, 2): 'Hut', (1, 2): 'Hrt', (2, 2): 'Htt',
             (3, 3): 'H11', (4, 4): 'H22'}
    H = sp.zeros(5)
    for (i, j), nm in names.items():
        H[i, j] = H[j, i] = sp.Function(nm)(u, r, th)
    R = ops_metric(g, X, H)
    bad = []
    for i in range(5):
        for j in range(i, 5):
            for nm, vc in ders(R[i, j], lambda vc: vc.get('u', 0) > 1 or (vc.get('u', 0) == 1
                                                                          and vc.get('theta', 0) > 0)):
                bad.append((i, j, nm, vc))
    if control:
        return not bad
    out("  X2 outgoing (u, r): d_u^2 or d_u d_th terms in dRic^H (15 components): %s  [%.0f s]"
        % (bad or "none", time.time() - T0))
    return not bad


# ------------------------------------------------------------------------------------------------------------ X3
r_, mu_ = sp.symbols('r mu', positive=True)
F_ = 1 - mu_/r_**2


def transport_vv(W, V, R0, r0, mass=True):
    """the T = 0 transport of the scalar sector from r0 to sqrt(mu): h~ = r^(3/2) H, data (W, V, R0) = (vv, vr, rr)"""
    x = sp.Symbol('x', positive=True)
    hrr = r0**sp.Rational(3, 2)*R0
    hvr = lambda y: r0**sp.Rational(3, 2)*V + mu_*hrr/2*(y**-2 - r0**-2)                 # noqa: E731
    k = 2 if mass else 0
    hvv = r0**sp.Rational(3, 2)*W - k*mu_*sp.integrate(hvr(x)*x**-3, (x, r0, sp.sqrt(mu_)))
    return sp.simplify(hvv*mu_**sp.Rational(-3, 4)), hrr, hvr, hvv


def e3(control=False):
    s, X_, Xd, xt = sp.symbols('s X Xdot xi_tau')
    # null covectors xi_tau dtau + s dr in (tau, r): g^tautau = -(2 - F), g^taur = 1 - F, g^rr = F
    roots = sp.solve(-(2 - F_)*xt**2 + 2*(1 - F_)*xt*s + F_*s**2, xt)
    ok_roots = set(sp.simplify(z - w) for z in roots for w in (s, -F_*s/(2 - F_))) >= {0}
    a_in, a_out = sp.symbols('a_in a_out')
    sol = sp.solve([a_in + a_out - X_, s*a_in - F_*s/(2 - F_)*a_out - Xd], [a_in, a_out])
    proj = sp.simplify(sol[a_in] - (F_*X_ + (2 - F_)*Xd/s)/2) == 0
    # L X / s with L = d_v + (F/2) d_r|_v, d_v = d_tau, d_r|_v = s - d_tau on the data
    projL = sp.simplify((Xd + F_/2*(s*X_ - Xd))/s - (F_*X_ + (2 - F_)*Xd/s)/2) == 0
    # the transport closed form against layerlin5's T_tab (the lam^-1 part of dRic^H, N1 (b))
    W, V, R0 = sp.symbols('W V R0')
    r0 = sp.Symbol('r0', positive=True)
    hvv_h, hrr, hvr, _ = transport_vv(W, V, R0, r0, mass=not control)
    y = sp.Symbol('y', positive=True)
    x = sp.Symbol('x', positive=True)
    k = 2 if not control else 0
    Hvv = (r0**sp.Rational(3, 2)*W - k*mu_*sp.integrate(hvr(x)*x**-3, (x, r0, y)))*y**sp.Rational(-3, 2)
    Hm = sp.zeros(5)
    Hm[0, 0] = Hvv
    Hm[0, 1] = Hm[1, 0] = hvr(y)*y**sp.Rational(-3, 2)
    Hm[1, 1] = hrr*y**sp.Rational(-3, 2)
    Hm = Hm.subs({y: L.r, mu_: L.mu0})
    Tt = L.T_tab(Hm)
    eq = [Tt[0, 0], Tt[0, 1], Tt[1, 1]]
    sat = all(sp.simplify(e) == 0 for e in eq)
    if control:
        return sat
    out("  X3 null covectors on Sigma: s dtau and -F s/(2 - F) dtau: %s; ingoing amplitude (F X + (2 - F) Xdot/s)/2: %s;"
        " = (L X)/s: %s; transport closed form solves T = 0 (vv, vr, rr): %s; H_vv(sqrt mu) = %s" % (
            ok_roots, proj, projL, sat, sp.factor(hvv_h)))
    return ok_roots and proj and projL and sat


# ------------------------------------------------------------------------------------------------------------ X4
def e4(control=False):
    v, r, th, lam, A, mu0 = L.v, L.r, L.th, L.lam, L.A, L.mu0
    g, gi, Gam, n = L.g, L.gi, L.Gam, L.n
    E1f, E0f = sp.Function('E1')(v), sp.Function('E0')(v)
    f, p, q = sp.Function('f')(r), sp.Function('p')(r), sp.Function('q')(r)
    tau = sp.Function('tau')(th)
    c, s_ = sp.cos(th), sp.sin(th)
    dd = sp.diff(c*s_*tau, th)/(c*s_)
    ph = sp.exp(I*v/lam)
    Dl = [ph*E0f*dd*p, ph*E0f*dd*q, ph*E1f*f*tau, 0, 0]
    nab = [[sp.diff(Dl[b], L.X[a]) - sum(Gam[cc][a][b]*Dl[cc] for cc in range(n)) for b in range(n)] for a in range(n)]
    S = sp.Matrix(n, n, lambda a, b: (nab[a][b] + nab[b][a])/2)
    trS = sum(gi[a, b]*S[a, b] for a in range(n) for b in range(n))
    F = L.F
    Nl = 1/sp.sqrt(2 - F)
    nv = sp.Matrix([Nl, -Nl*(1 - F), 0, 0, 0])
    nlow = g*nv
    unit = sp.simplify((nv.T*g*nv)[0] + 1) == 0 and sp.simplify(nlow[0] + nlow[1]) == 0
    Snn = (nv.T*S*nv)[0]
    G = Snn if control else Snn + trS/2
    rho = sp.expand(2*G/ph)
    sym = sp.Symbol
    e1d, e0d, e1s, e0s = sym('e1d'), sym('e0d'), sym('e1s'), sym('e0s')
    rho = rho.subs({sp.Derivative(E1f, v): e1d, sp.Derivative(E0f, v): e0d}).subs({E1f: e1s, E0f: e0s})
    cs1 = sp.simplify(rho.coeff(e1d))                       # coefficient of s E1
    c1 = sp.simplify(rho.coeff(e1s) - I/lam*cs1)            # E1 alone
    cs0 = sp.simplify(rho.coeff(e0d))                       # coefficient of s E0
    # the families (X5): f = i^N A r^(-3/2), (p, q) = N i^N A (r^(-5/2) beta(r0), r^(-7/2)), beta(r0) = -1/(2 r0),
    # evaluated on Sigma (r = r0); E1 = env^(N), E0 = env^(N-1)
    N = sp.Symbol('N', positive=True)
    fam = {f: I**N*A*r**sp.Rational(-3, 2), p: N*I**N*A*r**sp.Rational(-7, 2)*sp.Rational(-1, 2),
           q: N*I**N*A*r**sp.Rational(-7, 2)}
    c1f = sp.simplify(c1.subs(fam).doit())
    cs0f = sp.simplify(cs0.subs(fam).doit())
    want1 = I**N*A*dd*r**sp.Rational(-7, 2)
    want0 = -N*mu0/(r**2 + mu0)*I**N*A*dd*r**sp.Rational(-7, 2)
    ok = (sp.simplify(cs1) == 0 and sp.simplify(c1f - want1) == 0 and sp.simplify(cs0f - want0) == 0)
    if control:
        return ok
    out("  X4 n unit and normal to Sigma: %s; 2 Gt(S(D))(n, n): s E1 coefficient %s; E1 coefficient with the families"
        " %s; s E0 coefficient %s; equal to i^N A d r^(-7/2) [E1 - c_N s E0], c_N = N mu0/(r^2 + mu0): %s"
        % (unit, sp.simplify(cs1), sp.factor(c1f), sp.factor(cs0f), ok))
    return unit and ok


# ------------------------------------------------------------------------------------------------------------ X5
def e5(control=False):
    Q = sp.Symbol('Q')
    ok = True
    rows = []
    for N in range(2, 41):
        # x_j := scalar part of family j-2 of D_X H_j on Sigma; x_2 = q(c_20)_sc = Q;
        # x_j = Pol(c_(j,j-3))_sc + q(c_(j,j-2))_sc, Pol(c_(j,j-3))_sc = i x_(j-1) (data rule), q(c_(j,j-2)) = i^(j-2) Q
        x = Q
        for j in range(3, N + 2):
            x = (1 if control else I)*x + I**(j - 2)*Q
        ok &= sp.simplify(x - N*I**(N - 1)*Q) == 0
        if N in (9, 12, 40):
            rows.append("N = %d: %s" % (N, sp.simplify(x)))
    if control:
        return ok
    out("  X5 scalar part of the next-to-top family of D_X H_(N+1) on Sigma = N i^(N-1) q(c_20)_sc for N = 2..40: %s"
        " (%s); top family i^N A tau r^(-3/2) dth (from H_2, rth = i A E tau r^(-3/2): layerlin5 N3, READ)"
        % (ok, "; ".join(rows)))
    return ok


# ------------------------------------------------------------------------------------------------------------ X6
def e6(control=False):
    r, th, p1, p2 = sp.symbols('r theta phi1 phi2', positive=True)
    mu, eps = sp.symbols('mu epsilon', positive=True)
    af = sp.Function('a')(r, th)
    Y = [r, th, p1, p2]
    c, s = sp.cos(th), sp.sin(th)
    gam0 = sp.diag(1 + mu/r**2, r**2, r**2*c**2, r**2*s**2)
    if control:
        gam = gam0*(1 + eps*af)
    else:
        gam = gam0 + sp.diag(eps*af, 0, 0, 0)
    Nl = r/sp.sqrt(r**2 + mu)
    beta_low = [mu/r**2, 0, 0, 0]

    def chris(gm):
        gi = gm.inv()
        return gi, [[[sum(gi[a, d]*(sp.diff(gm[d, b], Y[cc]) + sp.diff(gm[d, cc], Y[b]) - sp.diff(gm[b, cc], Y[d]))
                          for d in range(4))/2 for cc in range(4)] for b in range(4)] for a in range(4)]
    gi0, G0 = chris(gam0)
    K = sp.Matrix(4, 4, lambda i, j: -(sp.diff(beta_low[j], Y[i]) + sp.diff(beta_low[i], Y[j])
                                       - 2*sum(G0[k][i][j]*beta_low[k] for k in range(4)))/(2*Nl))
    gi, G = chris(gam)
    Ric = sp.Matrix(4, 4, lambda b, cc: sum(sp.diff(G[a][b][cc], Y[a]) for a in range(4))
                    - sum(sp.diff(G[a][b][a], Y[cc]) for a in range(4))
                    + sum(G[a][a][d]*G[d][b][cc] - G[a][cc][d]*G[d][b][a] for a in range(4) for d in range(4)))
    R = sum(gi[b, cc]*Ric[b, cc] for b in range(4) for cc in range(4))
    Kup = gi*K*gi
    K2 = sum(Kup[i, j]*K[i, j] for i in range(4) for j in range(4))
    trK = sum(gi[i, j]*K[i, j] for i in range(4) for j in range(4))
    rho = R - K2 + trK**2
    lin = sp.expand(sp.diff(rho, eps).subs(eps, 0))
    lin = lin.subs({sp.Derivative(af, (r, 2)): sp.Symbol('arr'), sp.Derivative(af, r): sp.Symbol('ar')})
    arr = sp.simplify(lin.coeff(sp.Symbol('arr')))
    ar = sp.simplify(lin.coeff(sp.Symbol('ar')))
    if control:
        return arr == 0
    ok = arr == 0 and sp.simplify(ar - 3*r**3/(r**2 + mu)**2) == 0
    out("  X6 scalar constraint at the Kerr-Schild data, direction a dr dr: d_r^2 a coefficient %s, d_r a coefficient"
        " %s (= 3 r^3/(r^2 + mu)^2: %s)  [%.0f s]" % (arr, sp.factor(ar), ok, time.time() - T0))
    return ok


# ------------------------------------------------------------------------------------------------------------ X7
def chain(reading, shift=True, trace=True):
    a, s = sp.symbols('a s')
    r, mu = r_, mu_
    F = F_
    br = mu/(r**2 + mu)
    Xvv, Xvr, Xrr = sp.symbols('Xvv Xvr Xrr')
    if reading == 1:
        X = (0, 0, a)
        dsp = -br*s*a if shift is True else shift
    elif reading == 3:                       # ADM lapse N and shift covector beta_i = g_(tau i) kept
        X = (-a*br**2, a*br**2, a - a*br**2)
        dsp = -br*s*a if shift is True else shift
    else:
        X = (a*br**2, a*br - a*br**2, a*(1 - br)**2)
        dsp = br*s*a if shift is True else shift
    dX = (Xvv, Xvr, Xrr)
    dr = lambda i: s*X[i] - dX[i]                                                  # noqa: E731
    k = 1 if trace else 0
    eqs = [dX[2] + (F/2 if trace else F)*dr(2),                  # dD_r = 0 (top order)
           dr(0) + F*dr(1) - k*F/2*dX[2],                        # dD_v = 0
           dX[0] + 2*dX[1] + dX[2] - dsp]                        # d_tau of the spatial rr component
    sol = sp.solve(eqs, dX, dict=True)[0]
    Xin = [sp.simplify((F*X[i] + (2 - F)*sol[dX[i]]/s)/2) for i in range(3)]
    hvv, _, _, _ = transport_vv(Xin[0], Xin[1], Xin[2], r)
    return Xin, sp.factor(sp.simplify(hvv/a))


def e7(control=False):
    r, mu = r_, mu_
    want = {1: mu**sp.Rational(-3, 4)*r**sp.Rational(-5, 2)*(r**2 - mu)**2/4,
            2: mu**sp.Rational(-3, 4)*r**sp.Rational(3, 2)/4,
            3: (r**2 - 2*mu)/(4*mu**sp.Rational(3, 4)*sp.sqrt(r))}
    if control:
        a1 = chain(1, trace=False)[1]
        a2 = chain(2, trace=False)[1]
        return sp.simplify(a1 - want[1]) == 0 or sp.simplify(a2 - want[2]) == 0
    res = {}
    Zs = sp.Symbol('Z')
    free = True
    for k in (1, 2, 3):
        Xin, KR = chain(k)
        res[k] = (Xin, KR, sp.simplify(KR - want[k]) == 0)
        free &= sp.simplify(chain(k, shift=Zs)[1] - KR) == 0       # any d_tau gamma_rr datum Z gives the same K_R
    ok = all(v_[2] for v_ in res.values()) and free
    out("  X7 the ingoing amplitude of U1's scalar data (vv, vr, rr) per unit a and K_R = H_vv(sqrt mu0)/a: reading 1"
        " (g_(tau mu) kept): %s, K_R = %s; reading 2 (ADM lapse and shift vector kept, the supplement's convention:"
        " Z := d_tau - beta_ext): %s, K_R = %s; reading 3 (ADM lapse and shift covector kept): %s, K_R = %s, zero at"
        " r0^2 = 2 mu0 and negative below; all three as claimed: %s; K_R does not depend on the d_tau gamma_rr datum"
        " (any Z): %s" % ([sp.factor(x) for x in res[1][0]], res[1][1], [sp.factor(x) for x in res[2][0]], res[2][1],
                          [sp.factor(x) for x in res[3][0]], res[3][1], ok, free))
    return ok


# ------------------------------------------------------------------------------------------------------------ X8
def e8(control=False):
    T, c, nu = sp.symbols('T c nu', positive=True)
    Xi = ((1 - c)*T - I*c)/(T + I) if not control else ((1 - c)*T + I*c)/(T - 2*I)
    m2 = sp.simplify(sp.expand(Xi*sp.conjugate(Xi)))
    want = ((1 - c)**2*T**2 + c**2)/(T**2 + 1)
    form = sp.simplify(m2 - want) == 0
    if control:
        return form
    lower = all(want.subs({T: tv, c: cv}) >= min(cv**2, (1 - cv)**2)
                for tv in (sp.Rational(1, 100), 1, 100) for cv in (sp.Rational(1, 10), sp.Rational(9, 10), 2))
    # weighted mean of (1 - c)^2 and c^2, so >= the smaller: exact
    wm = sp.simplify(want - ((T**2/(T**2 + 1))*(1 - c)**2 + (1/(T**2 + 1))*c**2)) == 0
    ser = sp.simplify(sp.series(Xi, T, 0, 2).removeO() - (-c - I*T)) == 0
    # crossover: real parts nu + G c L = 0 (or nu - G c L = 0), quadrature parts 2 T nu + T G L (resp. - T G L)
    G, Lm = sp.symbols('G Lambda', positive=True)
    q1 = sp.simplify((2*T*nu + T*G*Lm).subs(G*Lm, -nu/c).subs(G, -nu/(c*Lm)) - T*nu*(2 - 1/c)) == 0
    q2 = sp.simplify((2*T*nu - T*G*Lm).subs(G, nu/(c*Lm)) - T*nu*(2 - 1/c)) == 0
    out("  X8 |Xi|^2 = [(1 - c)^2 T^2 + c^2]/(T^2 + 1): %s, a weighted mean of (1 - c)^2 and c^2: %s (so >= min: %s);"
        " Xi = -c - i T + O(T^2): %s; at a real cancellation the quadrature part is T nu (2 - 1/c), both signs: %s"
        % (form, wm, lower, ser, q1 and q2))
    return form and wm and lower and ser and q1 and q2


# ------------------------------------------------------------------------------------------------------------ X9
def lemma_w(S0, S1, S2, eps, lam=1.0, pts=4000):
    """does f(t) = Re[(S0 + S1 t + S2 t^2/2) e^(i t/lam)] + eps(t) take both signs on [0, 4 pi lam]?"""
    import cmath
    import math
    pos = neg = False
    for k in range(pts + 1):
        t = 4*math.pi*lam*k/pts
        val = ((S0 + S1*t + S2*t*t/2)*cmath.exp(1j*t/lam)).real + eps(t)
        pos |= val > 0
        neg |= val < 0
    return pos and neg


def e9(control=False):
    import cmath
    import math
    rng = random.Random(9)
    fails = 0
    for k in range(2000):
        # case B: |S'| = L0 >= 1, |S''| <= L0/(80 pi), a zero of the linear part inside the window, |eps| <= pi L0/5
        L0 = 1.0
        ph = cmath.exp(1j*rng.uniform(0, 2*math.pi))
        t0 = rng.uniform(0, 4*math.pi) + 1j*rng.uniform(-0.3, 0.3)
        S1 = L0*ph
        S0 = -S1*t0
        S2 = (L0/(80*math.pi))*cmath.exp(1j*rng.uniform(0, 2*math.pi))
        e = rng.choice((1, -1))*math.pi/5*L0
        epsf = (lambda t, e=e: e) if not control else (lambda t, S0=S0, S1=S1: -abs(S0 + S1*t) - 1e-3)
        if not lemma_w(S0, S1, S2, epsf):
            fails += 1
    for k in range(2000):
        # case A: |S| >= m on the window, phase moving by less than pi/6, |eps| <= m/4
        m = 1.0
        ph = cmath.exp(1j*rng.uniform(0, 2*math.pi))
        S0 = 2*m*ph
        S1 = (m/(8*math.pi))*cmath.exp(1j*rng.uniform(0, 2*math.pi))
        e = rng.choice((1, -1))*m/4
        if not lemma_w(S0, S1, 0, lambda t, e=e: e):
            fails += 1
    if control:
        return fails == 0
    out("  X9 Lemma W on 4000 random amplitudes (2000 with a zero of S inside the window, 2000 with |S| >= m): windows"
        " with one sign only: %d" % fails)
    return fails == 0


# ------------------------------------------------------------------------------------------------------------ X10
def rec_ell(x):
    t = 2*x/3
    return 12*mp.log(mp.sin(mp.pi*t/2)) + 1 - 1/(t*(2 - t))


def env_derivs(ell, x, kmax):
    """env^(k)(x)/env(x), k <= kmax, from the Taylor coefficients of exp(ell(x + h) - ell(x))"""
    co = mp.taylor(lambda h: mp.exp(ell(x + h) - ell(x)), 0, kmax + 1)
    return [co[k]*mp.factorial(k) for k in range(kmax + 2)]


def bell_ratios(kmax):
    """Y_k = env^(k)/env as polynomials in L_j = (log env)^(j): Y_(k+1) = Y_k' + L_1 Y_k (complete Bell polynomials)"""
    Ls = sp.symbols('L1:%d' % (kmax + 3))
    Y = [sp.Integer(1)]
    for _ in range(kmax + 1):
        y = Y[-1]
        dy = sum(sp.diff(y, Ls[j])*Ls[j + 1] for j in range(kmax + 1))
        Y.append(sp.expand(dy + Ls[0]*y))
    return Ls, Y


XS = sp.Symbol('x', positive=True)
ELLS = {"exp(-1/x)": -1/XS,
        "record C_c^inf": 12*sp.log(sp.sin(sp.pi*(2*XS/3)/2)) + 1 - 1/((2*XS/3)*(2 - 2*XS/3)),
        "sin^16 mutant": -1/XS + 10*sp.sin(4*sp.pi*sp.log(XS)/sp.log(10))**16/XS}
C_R_STATED = 3                      # |kappa_k'| <= c_R kappa_k^(3/2), alpha = 1/2


def e10(control=False):
    mp.mp.dps = 50
    kmax = 13
    Ls, Y = bell_ratios(kmax + 2)
    Yf = [sp.lambdify(Ls, y, 'mpmath') for y in Y]
    names = ["sin^16 mutant"] if control else ["exp(-1/x)", "record C_c^inf"]
    xs = [mp.mpf(10)**(-2 - mp.mpf(3)*k/800) for k in range(401)]        # 401 points on [10^-3.5, 10^-2]
    rows, ok = [], True
    for nm in names:
        dl = [sp.lambdify(XS, sp.diff(ELLS[nm], XS, j), 'mpmath') for j in range(1, len(Ls) + 1)]
        good, cR, cj, Cup = True, mp.mpf(0), mp.mpf(0), mp.mpf(0)
        for x in xs:
            Lv = [f(x) for f in dl]
            Yv = [f(*Lv) for f in Yf]
            kap = Yv[1]
            for k in range(kmax + 1):
                kk = Yv[k + 1]/Yv[k]
                lc = Yv[k + 2]/Yv[k] - kk**2                     # (log env^(k))'' = kappa_k'
                good &= Yv[k] > 0 and lc < 0 and mp.mpf(1)/2 < kk/kap < 2
                if Yv[k] > 0 and kk > 0:
                    cR = max(cR, abs(lc)/kk**mp.mpf(1.5))
                if kap > 0 and k >= 1:
                    Cup = max(Cup, abs(kk - kap)/(k*mp.sqrt(kap)))
            cj = max(cj, max(abs(Yv[j])/kap**j for j in range(kmax + 2)))
        # kappa_k - kappa_(k-1) = kappa_(k-1)'/kappa_(k-1), so (H_N) gives |kappa_k - kappa| <= k c_R 2^alpha kappa^alpha
        derived = C_R_STATED*mp.sqrt(2)
        good &= cR <= C_R_STATED and Cup <= derived
        ok &= good
        rows.append("%s: env^(k) > 0, log-concave, kappa_k/kappa in (1/2, 2), k <= %d, at all 401 points: %s; sup"
                    " |kappa_k'|/kappa_k^(3/2) = %s <= c_R = %d; L.16 (c): max_(j<=%d) sup |env^(j)|/(kappa^j env) ="
                    " %s; |kappa_k - kappa| <= %s k kappa^(1/2), below the bound c_R 2^(1/2) = %s that (H_N) implies"
                    % (nm, kmax, good, mp.nstr(cR, 4), C_R_STATED, kmax + 1, mp.nstr(cj, 4), mp.nstr(Cup, 4),
                       mp.nstr(derived, 4)))
    if control:
        return ok
    out("  X10 hypotheses (H_N) and L.16 (c) on x in [10^-3.5, 10^-2], 401 points, exact derivatives (Bell polynomials"
        " in the derivatives of log env): " + "; ".join(rows) + "  [%.0f s]" % (time.time() - T0))
    return ok


# ------------------------------------------------------------------------------------------------------------ X11
def e11(control=False):
    mp.mp.dps = 50
    lam = mp.mpf(10)**-6
    r0, mu0 = mp.mpf(3), mp.mpf(1)
    nu = -mp.mpf(1)/9
    worst = []
    ok = True
    u = sp.Symbol('u')
    Ps = [sp.Integer(1)]
    for _ in range(13):
        Ps.append(sp.expand(u**2*(Ps[-1] - sp.diff(Ps[-1], u))))      # env^(k)/env = P_k(1/x) for exp(-1/x)
    Pf = [sp.lambdify(u, pp, 'mpmath') for pp in Ps]
    for N in (9, 12):
        cN = N*mu0/(r0**2 + mu0)
        x_top = 1/(4*mp.log(1/lam))                        # env = lam^4 at the top
        x_bot = mp.mpf('0.2')*mp.sqrt(lam)
        nwin = 1200
        bad = 0
        for k in range(nwin):
            x = x_top*(x_bot/x_top)**(mp.mpf(k)/(nwin - 1))
            pos = {1: False, -1: False}
            neg = {1: False, -1: False}
            for j in range(64):
                xx = x + 4*mp.pi*lam*j/63
                envk = [Pf[i](1/xx) for i in range(N + 1)]
                env = mp.exp(-1/xx)
                kap = envk[1]
                kN = envk[N]/envk[N - 1]
                T = lam*kN
                Xi = ((1 - cN)*T - 1j*cN)/(T + 1j)
                Lam = lam**(N - 2)*envk[N - 1]
                Sst = nu*(1 + 2j*lam*kap) if lam*kap <= 1 else 0          # L.22: the stage term cut off at lam kappa > 1
                S = Sst - (0 if control else 1)*(1j)**N*Xi*Lam
                m0 = env/9
                D2 = 10*(1 + lam*kap)**2*env
                val = -lam**3*(S*mp.exp(1j*xx/lam)).real
                for sg in (1, -1):
                    w = val - m0 + sg*D2
                    pos[sg] |= w > 0
                    neg[sg] |= w < 0
            if not all(pos[sg] and neg[sg] for sg in (1, -1)):
                bad += 1
        worst.append("N = %d (c_N = %s): windows with one sign %d of %d" % (N, mp.nstr(cN, 3), bad, nwin))
        ok &= bad == 0
    if control:
        return ok
    out("  X11 model (exp(-1/x), lam = 1e-6, r0 = 3, nu = -1/9, Gamma = 1, x from env = lam^4 down to 0.2 lam^(1/2); "
        "values per env): " + "; ".join(worst) + "  [%.0f s]" % (time.time() - T0))
    return ok


# ------------------------------------------------------------------------------------------------------------ X12
def e12(control=False):
    mp.mp.dps = 50
    lam = mp.mpf(10)**-10
    N, r0, mu0, nu, Gam = 12, mp.mpf(3), mp.mpf(1), -mp.mpf(1)/9, mp.mpf(1)
    cN = N*mu0/(r0**2 + mu0)
    u = sp.Symbol('u')
    Ps = [sp.Integer(1)]
    for _ in range(N + 2):
        Ps.append(sp.expand(u**2*(Ps[-1] - sp.diff(Ps[-1], u))))
    Pf = [sp.lambdify(u, pp, 'mpmath') for pp in Ps]

    def parts(x):
        envk = [Pf[i](1/x) for i in range(N + 1)]
        T = lam*envk[N]/envk[N - 1]
        Xi = ((1 - cN)*T - 1j*cN)/(T + 1j)
        return envk[1], lam**(N - 2)*envk[N - 1], Xi

    lo, hi = mp.mpf('1e-7'), mp.mpf('2e-2')                  # Re sigma_main = 0: nu + Gam Re(-Xi) Lam = 0
    for _ in range(200):
        mid = mp.sqrt(lo*hi)
        kap, Lam, Xi = parts(mid)
        if (nu*(1 + 2j*lam*kap) - Gam*Xi*Lam).real > 0:
            lo = mid
        else:
            hi = mid
    xc = hi
    kc, Lc, Xc = parts(xc)

    def sigma(x):
        kap, Lam, Xi = parts(x)
        if control:
            Lam = Lc                                          # a mutation: Lambda frozen (no transversality)
        sm = nu*(1 + 2j*lam*kap) - Gam*Xi*Lam                 # i^12 = 1
        qc = (nu*(1 + 2j*lam*kc) - Gam*Xc*Lc).imag            # the quadrature part at the cancellation
        theta = -1j*qc*(Lam/Lc)*(lam*kap/(lam*kc))            # an O(T) relative error that cancels it there
        ene = (lam + 1/kap)*abs(nu)*mp.cos(kc*x)              # a non-explicit error, size (lam + 1/kappa)|nu|
        return sm + theta + ene

    per = 4*mp.pi*lam
    worst_L0, worst_cond, bad_sign = mp.inf, True, 0
    for k in range(-40, 41):
        x0 = xc + k*per/2
        ts = [x0 + per*j/96 for j in range(97)]
        d1 = [mp.diff(sigma, t) for t in ts[::8]]
        d2 = [mp.diff(sigma, t, 2) for t in ts[::8]]
        L0 = min(abs(d) for d in d1)
        eps = max(10*(1 + lam*kc)**2*mp.exp(-1/t)/lam**3 for t in ts)     # non-harmonic, per lam^3 A |d| env
        cond = L0 >= abs(nu)*mp.sqrt(kc) and max(abs(d) for d in d2) <= L0/(80*mp.pi*lam) and eps <= mp.pi*lam*L0/5
        worst_L0 = min(worst_L0, L0/(abs(nu)*mp.sqrt(kc)))
        worst_cond &= cond
        vals = [(sigma(t)*mp.exp(1j*t/lam)).real for t in ts]
        if not (any(vv_ > eps for vv_ in vals) and any(vv_ < -eps for vv_ in vals)):
            bad_sign += 1
    if control:
        return worst_cond
    out("  X12 the crossover by Lemma W (B), N = 12 (the real parts cancel: nu < 0, Gamma > 0, i^N = 1), exp(-1/x),"
        " lam = 1e-10, r0 = 3: Re sigma_main = 0 at x_c = %s (lam kappa = %s); with an O(T) relative error that cancels"
        " the quadrature part at x_c and a non-explicit error of size (lam + 1/kappa)|nu|, on the 81 windows around x_c:"
        " min |sigma'|/(|nu| kappa^(1/2)) = %s, Lemma W (B)'s conditions hold on every one: %s, windows without both"
        " signs: %d (at lam = 1e-6 the margin lam (kappa_(N-1) - kappa) < 1/(80 pi) of (B)'s second condition is not"
        " yet met; it tends to 0 like lam^(1 - (N-2)/(2(N-1))))"
        % (mp.nstr(xc, 6), mp.nstr(lam*kc, 4), mp.nstr(worst_L0, 4), worst_cond, bad_sign))
    return worst_cond and bad_sign == 0


def main():
    ok = True
    for name, f in (("X1", e1), ("X2", e2), ("X3", e3), ("X4", e4), ("X5", e5), ("X6", e6), ("X7", e7), ("X8", e8),
                    ("X9", e9), ("X10", e10), ("X11", e11), ("X12", e12)):
        good = f()
        ctl = f(control=True)
        out("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""))
        ok &= good and not ctl
    out("edge1_5: %s  [%.0f s]" % ("all checks pass, every control fails" if ok else "FAILURES", time.time() - T0))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
