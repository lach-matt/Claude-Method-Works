#!/usr/bin/env python3
"""veryedge5.py -- the very edge of the equality layer (EQUALITY5-LAYER.md, Round 3, R3.2 (e)): where the expansion in
lam of the term linear in the wave stops being ordered, what it re-sums to, and why no expansion of the approximant
decides the causal character of x_K = 1 there.

  V1 (exact, every function; the record's operators, imported from layerlin5.py) The seed's linearised dRic^H and dD
     are of first order in d_v (the phase dv is null): for every T^2 x Z2 x Z2-invariant H(v, r, th),
         Q(H) := dRic^H(H) + i T(d_v H)   and   q(H) := dD(H) - Pol(d_v H)
     contain no v-derivative of H (T, Pol as tabulated in layerlin5 N1).  Hence R_X = -i T d_v + Q and D_X = Pol d_v +
     q.  This rests on g0^-1(dv, dv) = 0 (no d_v^2 term); a non-null covector, dv + dr/5, has g0^-1 = 2/5 + F/25.
     Control (a mutation of the computed path): T with its vv mass coupling halved leaves a v-derivative in Q.
  V2 (exact, a model with the same structure) A three-component system with T = -i P (P first order in r, a mass
     coupling), R_X = -i T d_v + Q, D_X = Pol d_v + q, Pol^+ a right inverse, H1 transported with Pol H1 = 0, run by
     the record's recursion T(H_{j+1}) = -R_X(H_j) with data H_{j+1} = i Pol^+(D_X H_j) on the slice r0 = v - tau0 (and
     again with decay at infinity in place of slice data).  Writing H_j = sum_k E^(k)(v) c_{j,k}(r, r0): c_{j,j-2} =
     i^(j-2) c_{2,0} and c_{j,j-3} = (j-2) i^(j-3) c_{3,0}, for j <= 9, in every component -- the deduction of R3.2 (e)
     (the top two derivative orders of the lam-series are those of lam (1 - i lam d_v)^-1 and lam^3 (1 - i lam d_v)^-2).
     Controls: R_X without its d_v part (the frozen operator) fails; slice data carrying i d_v of the wave fail.
  V3 (exact) nu_hom(r0): the homogeneous transport (T = 0) to r = sqrt(mu0) of the vv, vr, rr data of the third profile
     on Sigma_tau0, i Pol^+(D_X H2)(r0) (layerlin5 N2, N4), per A E d: nu_hom = -mu0^(5/4) r0^-6/4 = -mu0^(-7/4)/(4
     rho^6), rho = r0/sqrt(mu0): never zero.
     Control: nu_hom differs from the transported-with-source value nu(r0) of (0.2) (it has no root rho*).
  V4 (computed, mpmath; exact for exp(-1/x^k)) The scale of the very edge, x_b(lam) := the x where lam |env'/env| = 1,
     for the edge classes exp(-1/x^k) (k = 1, 2, 3: x_b = (k lam)^(1/(k+1))), exp(-e^(1/x)) (x_b ln(1/lam) decreases
     towards 1), the record's C_c^inf envelope (an exp(-3/(4x)) edge: exponent 1/2) and sin^4 (a finite-order edge:
     x_b ~ 4 lam, exponent 1); and that below x_b/2 the top terms of the lam-series increase (k = 0..6) and above
     3 x_b they decrease.
     Control: the claim "x_b ~ lam^(1/2) for every flat edge" fails for exp(-1/x^2), exp(-1/x^3) and exp(-e^(1/x)).
  V5 (computed, mpmath, a model with unit constants, A = mu0 = |d| = 1) For env = exp(-1/x), lam = 1e-6: the re-summed
     first-degree term F := lam (i/s)^2 E = -lam int_0^x (x - x') e^(-i (x - x')/lam) E(x') dx', s = d_v + i/lam,
     (a) agrees with its truncated binomial series lam^3 sum_(k<=K) (k+1) (i lam)^k E^(k) in the window (env = lam^14)
     and with the local form lam (i/s~)^2 E, s~ := E'/E + i/lam, at both points; (b) at the very edge x = 0.3 lam^(1/2)
     the truncated series is off by more than its own size and consecutive truncations differ by more than the first
     (no truncation is asymptotic), while the local form is within 2e-3, O(x); (c) Re[c F e^(i v/lam)] changes sign
     twice on
     every carrier period at the very edge for three phases c, and |F| exceeds the margin bound (E^2 + int E^2)/9 by a
     factor above 10^1000; (d) at the very edge |F| < the approximant's top slice-data term lam^(N+1) (N-1) |E^(N-2)|
     |nu_hom| < the record's bound on the correction U, lam^(N-2) eps_(2N+2) (N = 9): the record's own bounds leave the
     sign to U.  Controls: c = 0 (no first-degree term) leaves -m0 < 0 with no sign change; in the window the ordering
     of (d) fails (|F| exceeds the top data term there).

Labels: computed (V1-V3 exact, sympy and exact rationals; V4-V5 mpmath at 40-60 digits, sampled where it says so).
V2 and V5 are models: V2 checks the algebra of the deduction on a system with the record's structure, V5 the arithmetic
with unit constants; neither evaluates the record's constants.
Run: python3 checks/veryedge5.py   (about two minutes; imports layerlin5.py)
"""
import os
import sys
import textwrap
import time
from fractions import Fraction as Fr

import mpmath as mp
import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import layerlin5 as L                                                             # noqa: E402

T0 = time.time()
I = sp.I


def out(msg):
    print(textwrap.fill(msg, width=121, subsequent_indent="      ", break_on_hyphens=False), flush=True)


# ------------------------------------------------------------------------------------------------------------ V1
def vfree(e):
    """True if e (linear in the derivatives of the free functions) has zero coefficient on every v-derivative"""
    e = sp.expand(e)
    ders = [d for d in e.atoms(sp.Derivative) if L.v in [x for x, _ in d.variable_count]]
    rep = {d: sp.Symbol('VD%d' % k) for k, d in enumerate(ders)}
    e2 = e.xreplace(rep)
    return all(L.is_zero(sp.diff(e2, sym)) for sym in rep.values())


def v1(control=False):
    Hg = L.general_H()
    if 'V1' not in CACHE:
        CACHE['V1'] = L.ops(Hg, twoscale=False)
    Lone, Done = CACHE['V1']
    dvH = Hg.applyfunc(lambda x: sp.diff(x, L.v))
    Tt = L.T_tab(dvH)
    if control:
        # a mutation of the computed path: the vv mass coupling 2 mu0 H_vr/r^3 of T halved
        Tm = Tt.copy()
        Tm[0, 0] = Tt[0, 0] + I*L.mu0*dvH[0, 1]/L.r**3
        return vfree(Lone[0, 0] + I*Tm[0, 0])
    pt = L.pol_tab(dvH)
    q_ok = all(vfree(Lone[i, j] + I*Tt[i, j]) for i in range(L.n) for j in range(i, L.n))
    d_ok = all(vfree(Done[k] - pt[k]) for k in range(L.n))
    xi = sp.Matrix([1, sp.Rational(1, 5), 0, 0, 0])
    null = sp.simplify(L.gi[0, 0]) == 0 and sp.simplify((xi.T*L.gi*xi)[0]) != 0
    out("  V1 dRic^H(H) + i T(d_v H) free of v-derivatives (15 components): %s; dD(H) - Pol(d_v H) free of"
        " v-derivatives (5): %s; g0^-1(dv, dv) = 0 while g0^-1 of dv + dr/5 is %s  [%.0f s]"
        % (q_ok, d_ok, sp.simplify((xi.T*L.gi*xi)[0]), time.time() - T0))
    return q_ok and d_ok and null


CACHE = {}


# ------------------------------------------------------------------------------------------------------------ V2
ZERO, ONE, IM = (Fr(0), Fr(0)), (Fr(1), Fr(0)), (Fr(0), Fr(1))


def cmul(a, b):
    return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])


def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def R_(x):
    return (Fr(x), Fr(0))


def add(*ds):
    res = {}
    for d in ds:
        for k, c in d.items():
            res[k] = cadd(res.get(k, ZERO), c)
    return {k: c for k, c in res.items() if c != ZERO}


def scale(d, c):
    return add({k: cmul(x, c) for k, x in d.items()})


def mono(d, a=0, b=0):
    """times q^a Q0^b, q = sqrt(r), Q0 = sqrt(r0); keys (power of q, power of Q0, derivative order of E)"""
    return {(k[0] + a, k[1] + b, k[2]): c for k, c in d.items()}


def d_r(d):
    return add({(k[0] - 2, k[1], k[2]): cmul(c, R_(Fr(k[0], 2))) for k, c in d.items()})


def d_v(d):
    """d_v at fixed r: E^(k) -> E^(k+1), and the slice radius r0 = v - tau0 moves: d/dr0 = (1/(2 Q0)) d/dQ0"""
    return add({(k[0], k[1], k[2] + 1): c for k, c in d.items()},
               {(k[0], k[1] - 2, k[2]): cmul(c, R_(Fr(k[1], 2))) for k, c in d.items()})


def at_r0(d):
    return add(*[{(0, k[1] + k[0], k[2]): c} for k, c in d.items()])


def integ(d, past):
    """int_(r0)^r f ds (slice) or -int_r^oo f ds (past), f a Laurent polynomial in q, ds = 2 t dt"""
    res = {}
    for (n, m, k), c in d.items():
        p = n + 2
        if p == 0:
            raise ValueError('logarithm')
        cc = cmul(c, R_(Fr(2, p)))
        if past:
            if p >= 0:
                raise ValueError('no decay')
            res = add(res, {(p, m, k): cc})
        else:
            res = add(res, {(p, m, k): cc}, {(0, m + p, k): cmul(cc, R_(-1))})
    return res


MU, Q1, Q2, Q3, K1, K2, SIG = Fr(1), Fr(1, 3), Fr(2, 5), Fr(1, 7), Fr(1, 2), Fr(3, 4), Fr(1, 2)


def P_(Z):
    a, b, c = Z
    return [add(d_r(a), scale(mono(a, -2), R_(Fr(3, 2))), scale(mono(b, -6), R_(2*MU))),
            add(d_r(b), scale(mono(b, -2), R_(Fr(3, 2)))), add(d_r(c), scale(mono(c, -2), R_(Fr(1, 2))))]


def Q_(Z):
    a, b, c = Z
    return [add(scale(mono(a, -4), R_(Q1)), scale(mono(c, -5), R_(K1))),
            add(scale(mono(b, -4), R_(Q2)), scale(mono(c, -5), R_(K2))), scale(mono(c, -4), R_(Q3))]


def solveP(S, Z0, past):
    """P Z = S: r^(3/2) b, r^(1/2) c, r^(3/2) a (with the coupling 2 mu b/r^3) integrated along r"""
    Sa, Sb, Sc = S
    if past:
        b = mono(integ(mono(Sb, 3), True), -3)
        c = mono(integ(mono(Sc, 1), True), -1)
        a = mono(integ(mono(add(Sa, scale(mono(b, -6), R_(-2*MU))), 3), True), -3)
    else:
        b = mono(add(mono(Z0[1], 0, 3), integ(mono(Sb, 3), False)), -3)
        c = mono(add(mono(Z0[2], 0, 1), integ(mono(Sc, 1), False)), -1)
        a = mono(add(mono(Z0[0], 0, 3), integ(mono(add(Sa, scale(mono(b, -6), R_(-2*MU))), 3), False)), -3)
    return [a, b, c]


def run_model(J, past=False, frozen=False, ttdata=False):
    H = [[{}, {}, {(-1, 0, 0): ONE}]]                       # H1 = (0, 0, E r^-1/2): P H1 = 0, Pol H1 = 0
    for _ in range(1, J):
        Hj = H[-1]
        dvH = [d_v(x) for x in Hj]
        # P H_(j+1) = i P(d_v H_j) - i Q(H_j)   <=>   T(H_(j+1)) = -R_X(H_j), T = -i P, R_X = -i T d_v + Q
        if frozen:
            S = [scale(x, (Fr(0), Fr(-1))) for x in Q_(Hj)]
        else:
            S = [add(scale(x, IM), scale(y, (Fr(0), Fr(-1)))) for x, y in zip(P_(dvH), Q_(Hj))]
        V0 = at_r0(add(dvH[1], scale(mono(Hj[2], -3), R_(SIG))))     # D_X = Pol d_v + q, Pol Z = b, q Z = SIG c/r^(3/2)
        Z0 = [scale(V0, (Fr(0), Fr(1, 4))), scale(V0, IM), {}]        # i Pol^+(V), Pol^+ V = (V/4, V, 0)
        if ttdata:
            Z0[2] = scale(at_r0(dvH[2]), IM)
        H.append(solveP(S, Z0, past))
    return H


def coef(d, k):
    return {kk[:2]: c for kk, c in d.items() if kk[2] == k}


def ipow(n):
    return [ONE, IM, (Fr(-1), Fr(0)), (Fr(0), Fr(-1))][n % 4]


def model_ok(H, J):
    ok = True
    for j in range(2, J + 1):
        for comp in range(3):
            ok &= add(coef(H[j - 1][comp], j - 2), scale(coef(H[1][comp], 0), cmul(ipow(j - 2), R_(-1)))) == {}
            ok &= all(kk[2] <= j - 2 for kk in H[j - 1][comp])
            if j >= 3:
                ok &= add(coef(H[j - 1][comp], j - 3),
                          scale(coef(H[2][comp], 0), cmul(ipow(j - 3), R_(-(j - 2))))) == {}
    return ok


def v2(control=False):
    J = 9
    if control:
        return (model_ok(run_model(J, frozen=True), J) or model_ok(run_model(J, ttdata=True), J)
                or model_ok(run_model(J, past=True, frozen=True), J))
    res = {}
    for past in (False, True):
        H = run_model(J, past=past)
        nz = any(H[1]) and any(coef(H[2][c], 0) for c in range(3))
        res['past' if past else 'slice'] = model_ok(H, J) and nz
    out("  V2 model, j <= %d: c_(j,j-2) = i^(j-2) c_(2,0) and c_(j,j-3) = (j-2) i^(j-3) c_(3,0) in every component,"
        " slice data: %s, data from infinity: %s; frozen control: %s; data carrying i d_v of the wave: %s"
        % (J, res['slice'], res['past'], model_ok(run_model(J, frozen=True), J),
           model_ok(run_model(J, ttdata=True), J)))
    return all(res.values())


# ------------------------------------------------------------------------------------------------------------ V3
def nu_hom_closed():
    r, mu0, r0, A, E, d = L.r, L.mu0, L.r0, L.A, sp.Symbol('E'), sp.Symbol('d')
    beta0 = L.BETA.subs(r, r0)
    Vr = I*A*E*d*r0**sp.Rational(-7, 2)                   # (D_X H2)_r at r0 (layerlin5 N4)
    Vv = I*A*E*d*r0**sp.Rational(-5, 2)*beta0              # (D_X H2)_v at r0
    Z, _ = L.polplus(sp.Matrix([L.Vv, L.Vr, L.Vt, 0, 0]))
    sub = {L.Vv: Vv, L.Vr: Vr, L.Vt: 0}
    dvv, dvr, drr = [sp.simplify(I*Z[i, j].subs(r, r0).subs(sub)) for (i, j) in ((0, 0), (0, 1), (1, 1))]
    x = sp.Symbol('x', positive=True)
    rr_ = r0**sp.Rational(3, 2)*drr*r**sp.Rational(-3, 2)
    vr_ = (r0**sp.Rational(3, 2)*dvr - sp.integrate(mu0*x**-3*(x**sp.Rational(3, 2)*rr_.subs(r, x)), (x, r0, r))
           )*r**sp.Rational(-3, 2)
    vv_ = (r0**sp.Rational(3, 2)*dvv - sp.integrate(2*mu0*x**-3*(x**sp.Rational(3, 2)*vr_.subs(r, x)), (x, r0, r))
           )*r**sp.Rational(-3, 2)
    H = sp.zeros(L.n)
    H[0, 0], H[0, 1], H[1, 0], H[1, 1] = vv_, vr_, vr_, rr_
    Tt = L.T_tab(H)
    hom = all(sp.simplify(Tt[i, j]) == 0 for (i, j) in ((0, 0), (0, 1), (1, 1)))
    nu = sp.simplify(vv_.subs(r, sp.sqrt(mu0))/(A*E*d))
    return nu, hom


def v3(control=False):
    nu, hom = nu_hom_closed()
    mu0, r0 = L.mu0, L.r0
    rho = sp.Symbol('rho', positive=True)
    nur = sp.simplify(nu.subs(r0, rho*sp.sqrt(mu0)))
    K = L.KCLOSED
    if control:
        return sp.simplify(nur - K) == 0
    closed = sp.simplify(nu + mu0**sp.Rational(5, 4)*r0**-6/4) == 0
    noroot = sp.solve(sp.numer(sp.together(nur)), rho) == []
    out("  V3 nu_hom(r0) = %s (closed form -mu0^(5/4) r0^-6/4: %s), homogeneous transport: %s, no zero: %s;"
        " at P* (mu0 = 1, r0 = 5/2): nu_hom = %s, nu = %s" % (nu, closed, hom, noroot, sp.nsimplify(nu.subs(
            {mu0: 1, r0: sp.Rational(5, 2)})), sp.N(K.subs({mu0: 1, rho: sp.Rational(5, 2)}), 8)))
    return closed and hom and noroot


# ------------------------------------------------------------------------------------------------------------ V4
mp.mp.dps = 60


def logderiv(f, x):
    return mp.diff(lambda t: mp.log(f(t)), x)


def substitute_env(x):
    """CONSTANTS5's C_c^inf envelope at v = 1/2 + x (its edge), up to the factor c: beta(y), y = -1 + t, t = 2x/3;
    with 1 - y^2 = t (2 - t) and cos(pi y/2) = sin(pi t/2), so no cancellation near the edge"""
    t = 2*x/3
    return mp.sin(mp.pi*t/2)**12*mp.exp(1 - 1/(t*(2 - t)))


def substitute_se(x):
    """its logarithmic derivative in v: (2/3) (6 pi cot(pi t/2) + 2 (1 - t)/(t^2 (2 - t)^2))"""
    t = 2*x/3
    return mp.mpf(2)/3*(6*mp.pi*mp.cot(mp.pi*t/2) + 2*(1 - t)/(t**2*(2 - t)**2))


def ders_poly(kind, K):
    """E^(k) = P_k(1/x) E: exp(-1/x): P' = u^2 (P - P'); exp(-1/x^2): P' = 2 u^3 P - u^2 P'"""
    u = sp.Symbol('u')
    Ps = [sp.Integer(1)]
    for _ in range(K):
        p = Ps[-1]
        Ps.append(sp.expand(u**2*(p - sp.diff(p, u))) if kind == 1 else sp.expand(2*u**3*p - u**2*sp.diff(p, u)))
    return [sp.lambdify(u, q, 'mpmath') for q in Ps]


DP = {"exp(-1/x)": ders_poly(1, 8), "exp(-1/x^2)": ders_poly(2, 8)}


def ders_at(name, x, K):
    """|E^(k)(x)|/E(x), k <= K: exact polynomials for the two model edges, step-x^2/1000 differences otherwise"""
    if name in DP:
        return [abs(DP[name][k](1/x)) for k in range(K + 1)]
    f = CLASSES[name][0]
    f0 = f(x)
    return [abs(mp.diff(f, x, k, h=x**2/1000))/f0 for k in range(K + 1)]


CLASSES = {
    "exp(-1/x)": (lambda x: mp.exp(-1/x), lambda x: 1/x**2),
    "exp(-1/x^2)": (lambda x: mp.exp(-1/x**2), lambda x: 2/x**3),
    "exp(-1/x^3)": (lambda x: mp.exp(-1/x**3), lambda x: 3/x**4),
    "exp(-e^(1/x))": (lambda x: mp.exp(-mp.exp(1/x)), lambda x: mp.exp(1/x)/x**2),
    "record C_c^inf": (substitute_env, substitute_se),
    "sin^4 (paper)": (lambda x: mp.sin(mp.pi*x/3)**4, lambda x: 4*(mp.pi/3)*mp.cot(mp.pi*x/3)),
}


def x_break(se, lam):
    """the x where lam se(x) = 1 (se decreasing near 0): bisection on a log scale"""
    lo, hi = mp.mpf('1e-40'), mp.mpf('0.4')
    for _ in range(400):
        mid = mp.sqrt(lo*hi)
        if lam*se(mid) > 1:
            lo = mid
        else:
            hi = mid
    return hi


def v4(control=False):
    lams = [mp.mpf(10)**-8, mp.mpf(10)**-16, mp.mpf(10)**-32]
    expo = {}
    for name, (f, se) in CLASSES.items():
        xb = [x_break(se, lam) for lam in lams]
        expo[name] = (mp.log(xb[2]/xb[1])/mp.log(lams[2]/lams[1]), xb)
    if control:
        return all(abs(expo[nm][0] - mp.mpf(1)/2) < mp.mpf('0.02') for nm in
                   ("exp(-1/x^2)", "exp(-1/x^3)", "exp(-e^(1/x))"))
    ok = True
    for k, nm in ((1, "exp(-1/x)"), (2, "exp(-1/x^2)"), (3, "exp(-1/x^3)")):
        exact = all(abs(xb/((k*lam)**(mp.mpf(1)/(k + 1))) - 1) < mp.mpf(10)**-30 for xb, lam in zip(expo[nm][1], lams))
        ok &= exact and abs(expo[nm][0] - mp.mpf(1)/(k + 1)) < mp.mpf(10)**-20
    dexp = [xb*mp.log(1/lam) for xb, lam in zip(expo["exp(-e^(1/x))"][1], lams)]
    ok &= dexp[0] > dexp[1] > dexp[2] > 1 and dexp[2] < mp.mpf('1.2')
    ok &= abs(expo["record C_c^inf"][0] - mp.mpf(1)/2) < mp.mpf('0.01')
    ok &= abs(expo["sin^4 (paper)"][0] - 1) < mp.mpf('1e-6')
    ok &= abs(expo["sin^4 (paper)"][1][2]/(4*lams[2]) - 1) < mp.mpf('1e-6')
    # the top binomial terms (k + 2)/(k + 1) lam |E^(k+1)/E^(k)| at x_b/2 (all > 1) and 3 x_b (first < 1), lam = 1e-16
    lam = lams[1]
    incr = {}
    for nm in ("exp(-1/x)", "exp(-1/x^2)", "record C_c^inf"):
        xb = expo[nm][1][1]
        ders = ders_at(nm, xb/2, 7)
        up = all(lam*(k + 2)/(k + 1)*ders[k + 1]/ders[k] > 1 for k in range(7))
        ders3 = ders_at(nm, 3*xb, 1)
        down = lam*2*ders3[1]/ders3[0] < 1
        incr[nm] = up and down
    ok &= all(incr.values())
    out("  V4 exponents d log x_b / d log lam at lam = 1e-16..1e-32: " + "; ".join(
        "%s %s" % (nm, mp.nstr(e[0], 6)) for nm, e in expo.items()) + "; x_b = (k lam)^(1/(k+1)) exactly for"
        " exp(-1/x^k): True; exp(-e^(1/x)): x_b ln(1/lam) = %s (decreasing to 1); sin^4: x_b/(4 lam) = %s; top terms"
        " increase below"
        " x_b/2 and decrease above 3 x_b: %s" % (", ".join(mp.nstr(d, 5) for d in dexp),
                                                mp.nstr(expo["sin^4 (paper)"][1][2]/(4*lams[2]), 8), incr))
    return ok


# ------------------------------------------------------------------------------------------------------------ V5
def poly_ders(K):
    """E^(k) = P_k(1/x) e^(-1/x) for E = exp(-1/x): P_(k+1)(u) = u^2 (P_k(u) - P_k'(u)), integer coefficients"""
    u = sp.Symbol('u')
    Ps = [sp.Integer(1)]
    for _ in range(K):
        Ps.append(sp.expand(u**2*(Ps[-1] - sp.diff(Ps[-1], u))))
    return [sp.lambdify(u, p, 'mpmath') for p in Ps]


PK = poly_ders(24)


def F_over_E(x, lam):
    """F/E = -lam int_0^U w e^(-i w/lam) exp(1/x - 1/(x - w)) dw (the integrand is negligible beyond U)"""
    U = min(x*mp.mpf('0.999'), 120*x**2)
    period = 2*mp.pi*lam
    n = int(mp.ceil(U/period))
    pts = [U*k/max(n, 1) for k in range(0, max(n, 1) + 1)] if n > 1 else [0, U/4, U/2, U]
    g = lambda w: w*mp.expj(-w/lam)*mp.exp(1/x - 1/(x - w))                     # noqa: E731
    return -lam*mp.quad(g, pts)


def series_over_E(x, lam, K):
    return lam**3*sum((k + 1)*(1j*lam)**k*PK[k](1/x) for k in range(K + 1))


def local_over_E(x, lam):
    st = 1/x**2 + 1j/lam
    return -lam/st**2


def v5(control=False):
    mp.mp.dps = 40
    lam = mp.mpf(10)**-6
    xw = 1/(14*mp.log(1/lam))                    # env = lam^14: the window of Theorem L
    xe = mp.mpf('0.3')*mp.sqrt(lam)              # the very edge
    res = {}
    for nm, x in (("window", xw), ("edge", xe)):
        F = F_over_E(x, lam)
        S5, S6 = series_over_E(x, lam, 5), series_over_E(x, lam, 6)
        loc = local_over_E(x, lam)
        res[nm] = (F, abs(S5/F - 1), abs(S6 - S5)/abs(S5), abs(loc/F - 1))
    # (c) sign changes over one carrier period at the edge, three phases c; the margin bound
    nu_h = mp.mpf(1)/(4*mp.mpf('2.5')**6)
    N = 9
    vs = [xe + 2*mp.pi*lam*k/48 for k in range(49)]
    Fs = [F_over_E(v, lam)*mp.exp(-1/v) for v in vs]
    margin = [(mp.exp(-2/v)*(1 + v))/9 for v in vs]         # (E^2 + int_0^v E^2)/9 <= (1 + v) E^2/9
    changes = {}
    for cname, cc in (("1", 1), ("i", 1j), ("e^(i pi/4)", mp.expjpi(mp.mpf(1)/4)), ("0 (control)", 0)):
        vals = [-m - mp.re(cc*F*mp.expj(v/lam)) for F, m, v in zip(Fs, margin, vs)]
        changes[cname] = sum(1 for a, b in zip(vals, vals[1:]) if (a > 0) != (b > 0))
    ratio_log10 = min(mp.log10(abs(F)/m) for F, m in zip(Fs, margin))
    # (d) the ordering natural < top slice data < bound on U, at the edge and (control) in the window
    order = {}
    for nm, x in (("edge", xe), ("window", xw)):
        Fn = abs(res[nm][0])
        top = lam**(N + 1)*(N - 1)*abs(PK[N - 2](1/x))*nu_h
        bU = lam**(N - 2)*sum(abs(PK[i](1/x)) for i in range(2*N + 3))
        order[nm] = (Fn < top < bU, Fn, top, bU)
    if control:
        return changes["0 (control)"] > 0 or order["window"][0]
    ok = res["window"][1] < mp.mpf('1e-3') and res["window"][3] < mp.mpf('1e-2')
    ok &= res["edge"][1] > 1 and res["edge"][2] > 1 and res["edge"][3] < 10*xe
    ok &= all(changes[c] == 2 for c in ("1", "i", "e^(i pi/4)")) and ratio_log10 > 1000
    ok &= order["edge"][0]
    out("  V5 lam = 1e-6. Window (x = %s): |S_5/F - 1| = %s, |local/F - 1| = %s. Very edge (x = 0.3 lam^(1/2)):"
        " |S_5/F - 1| = %s, |S_6 - S_5|/|S_5| = %s, |local/F - 1| = %s. Sign changes of -m0 - Re[c F e^(i v/lam)] on"
        " one period at the edge: %s; log10 min |F|/margin = %s. Ordering at the edge |F| < top data < U-bound: %s"
        " (%s, %s, %s per E); in the window (control): %s"
        % (mp.nstr(xw, 5), mp.nstr(res["window"][1], 3), mp.nstr(res["window"][3], 3), mp.nstr(res["edge"][1], 3),
           mp.nstr(res["edge"][2], 3), mp.nstr(res["edge"][3], 3), changes, mp.nstr(ratio_log10, 6),
           order["edge"][0], mp.nstr(order["edge"][1], 3), mp.nstr(order["edge"][2], 3), mp.nstr(order["edge"][3], 3),
           order["window"][0]))
    return ok


def main():
    ok = True
    for name, f in (("V1", v1), ("V2", v2), ("V3", v3), ("V4", v4), ("V5", v5)):
        good = f()
        ctl = f(control=True)
        out("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""))
        ok &= good and not ctl
    out("veryedge5: %s  [%.0f s]" % ("all checks pass, every control fails" if ok else "FAILURES", time.time() - T0))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
