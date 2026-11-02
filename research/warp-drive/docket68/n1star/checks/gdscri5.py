#!/usr/bin/env python3
"""gdscri5.py -- GAUGEDECAY5.md Round 3, task 3: the harmonic gauge beyond the cone -- the source in II.F' (1.4)'s
class at null infinity, timelike infinity and K+, and what remains near the initial surface.  Computed.

Charts as in admbox5.py: the ingoing chart (v, r, th, phi1, phi2) and, near infinity, the outgoing chart of III.B
(3.4), (3.6) with T := t_*.  E^Ups k := -gam (2 iota_{g^-1 c} k - (2/3)(1 - e) c tr_g k) with c = |x|^-1 dt (III.B
(6.1)); Theta(k) = delta G k; Box := 2 delta G delta^* on 1-forms.

  S1 (exact) E^Ups G k sees no trace-free angular part.  For a general class tensor k (components arbitrary), with the
     angular block r^2 (tau gamma + s1 A1 + s2 A2), A1, A2 trace free, and c = |x|^-1 (dv + C(r) dr) for an arbitrary
     C (every t with dt in the orbit plane), E^Ups G k does not depend on s1, s2 (III.C's slot pi-slash_0, the only
     one with a radiation field at |x|^-3/2).  Control: Theta(k) does depend on them.
  S2 (exact, rational samples) The null-infinity order of the source.  With III.C (3.2)-(3.3)'s component exponents
     (pi_C > 3/2 + 2 gam, pi_01: 3/2 + (1 - e) gam, pi_1/: 3/2 + gam, pi_11: min(3/2 + (1 - e) gam, 3/2 + 2 gam),
     pi-slash_0: 3/2), the components entering E^Ups G have least exponent lambda_# = 3/2 + (1 - e) gam, so E^Ups G g'
     has I+-order lambda_# + 1 (the factor |x|^-1 of c).  Control: with pi-slash_0 admitted the least is 3/2.
  S3 (exact) II.F' weights.  With (1.1), rho_I rho_+ = 1/r, rho_+ rho_K = 1/t_*, t_* r^4 = rho_I^-4 rho_+^-5 rho_K^-1, so
     |dt dx| = rho_I^-4 rho_+^-5 rho_K^-1 mu_b and the weights (w_I, w_+, w_K) for |dt dx| are (w_I + 2, w_+ + 5/2,
     w_K + 1/2) for mu_b: (1.4)'s (alpha_I + 1, alpha_+ + 2, 0) is (b_I + 1, b_+ + 2, 1/2) of (1.7).  Control: the
     density with r^3 (n = 3) gives the shifts (3/2, 2, 1/2), the source's n = 3 values, not these.
  S4 (exact, rational samples) Membership.  A conormal f of pointwise orders p lies in rho^w L^2(mu_b) at a face iff
     p > w (int_0 rho^(2(p - w)) d rho / rho); and the source F_Y = -Theta(g') - mu' Box(chi_K W**_H) of Round 3 has
     orders I+: lambda_# + 1, iota+: (lambda_# + 1)- (min with 3 from the cut-off commutators), K+: (alpha - 2)-, all
     above (b_I + 1, b_+ + 2, 1/2) for beta = alpha_+ + 2 in (0, delta_#), b_+ = beta + 1/2 and b_I in (b_+, 3/2) (so
     (1.3) holds with S-bar = 0 for Box).  Controls: f of order p = w is not in rho^w L^2; the source without the W**
     cut-off term has K+-order 0 and fails (1.4) at K+.
  S5 (exact) The slab commutator at I+.  In the outgoing chart, for a cut-off chi(t_flat) with t_flat = T + kappa(T)/r
     (t_flat is smooth near I+ and equals t_* there; kappa arbitrary) and a 1-form Z = r^-p (a dT + b dr + r c dth),
     a, b, c arbitrary functions of (T, th), [Box, chi(t_flat)] Z is O(r^-(p+1)) in an orthonormal frame (p = 3/2, 1):
     one order gained at I+.  Control: chi(t), t = T + psi(r) the static time, gains nothing.
  S6 (exact) The cone commutator at iota+.  For chi(R), R = r/T, and Z = r^-p (a dT + b dr + r c dth), a, b, c
     explicit smooth functions of (R, th), [Box, chi(R)] Z = O(r^-(p+2)) at fixed R: two orders gained, so [Box,
     chi_K] lies in rho_+^2 Diff^1_b on the cone.  Control: a spatial cut-off chi(r) gains only one.
  S7 (exact, rational samples) The slab threshold.  [Box, chi(t_flat)] Z of I+-order p + 1 lies in (1.4) at I+ for
     some admissible b_I iff p > beta + 1/2; the radiation-field order 3/2 meets it for every beta in (0, 1).
     Control: p = beta + 1/2 fails.
  S8 (exact) W**_H's orders.  r d_mu T_mu -> 2 (III.B Lemma 3.5 (a)), r A -> 1/2, r B -> -1/4: on iota+-interior
     (r ~ t ~ v) W**_H has order 1, so [Box, chi_K] W**_H has iota+-order 3 (S6).  Control: at fixed r the term
     (v/2) W* grows in v, so W**_H has no K+-order (it is not cut off for nothing).

Labels: computed (exact, sympy).  Run: python3 checks/gdscri5.py   (several minutes)
"""
import itertools
import sys
from fractions import Fraction as Fr

import sympy as sp

from rwgauge5 import GEO, N, X, r, s, th, zero
from hgauge5 import theta, box

def finite(lim):
    """a limit is finite if it is not a Limit object and contains no infinity or nan (symbols are finite jets)"""
    return not isinstance(lim, sp.Limit) and not lim.has(sp.oo, -sp.oo, sp.zoo, sp.nan)


# ---------------------------------------------------------------- S1


def class_tensor(G, fun=False):
    T_ = X[0]
    nm = ['kvv', 'kvr', 'krr', 'kvt', 'krt', 'tau', 's1', 's2']
    if fun:
        F = {n: sp.Function(n)(T_, r, th) for n in nm}
    else:
        F = {n: sp.Symbol(n) for n in nm}
    k = [[0]*N for _ in range(N)]
    k[0][0], k[1][1] = F['kvv'], F['krr']
    k[0][1] = k[1][0] = F['kvr']
    k[0][2] = k[2][0] = F['kvt']
    k[1][2] = k[2][1] = F['krt']
    k[2][2] = r**2*(F['tau'] + 2*F['s1'])
    k[3][3] = r**2*sp.cos(th)**2*(F['tau'] - F['s1'] + F['s2'])
    k[4][4] = r**2*sp.sin(th)**2*(F['tau'] - F['s1'] - F['s2'])
    return k, F


def eups(G, k, c, gam, e):
    cvec = [sum(G.gi[a, b]*c[b] for b in range(N)) for a in range(N)]
    trk = G.tr(k)
    iota = [sum(cvec[a]*k[a][m] for a in range(N)) for m in range(N)]
    return [-gam*(2*iota[m] - sp.Rational(2, 3)*(1 - e)*c[m]*trk) for m in range(N)]


def trace_reverse(G, k):
    t_ = G.tr(k)
    return [[k[a][b] - G.g[a, b]*t_/2 for b in range(N)] for a in range(N)]


def s1(control=False):
    gam, e = sp.symbols('gamma_Ups e_Ups', positive=True)
    C = sp.Function('C')(r)
    c = [1/r, C/r, 0, 0, 0]
    if control:
        k, F = class_tensor(GEO, fun=True)
        th_ = theta(GEO, k)
        deps = []
        for m in range(3):
            ex = sp.expand(th_[m])
            dep = any(ex.has(F[n]) for n in ('s1', 's2'))
            deps.append(dep)
        res = not any(deps)
        print("  S1 control: Theta(k) independent of the trace-free angular part: %s (dependence by component %s)"
              % (res, deps), flush=True)
        return res
    k, F = class_tensor(GEO)
    E = eups(GEO, trace_reverse(GEO, k), c, gam, e)
    ok = all(zero(sp.diff(E[m], F[n])) for m in range(N) for n in ('s1', 's2'))
    dep_other = any(not zero(sp.diff(E[m], F[n])) for m in range(N) for n in ('kvv', 'kvr', 'krr', 'tau'))
    print("  S1: E^Ups G k independent of the trace-free angular part (s1, s2): %s; it does see the orbit components "
          "and the angular trace: %s" % (ok, dep_other), flush=True)
    return ok and dep_other

# ---------------------------------------------------------------- S2


def iplus_components(gam, e):
    d = (1 - e)*gam
    return {'pi_C': Fr(3, 2) + 2*gam + Fr(1, 10**6),      # min Re E^C_I > 3/2 + 2 gam (a strict lower bound)
            'pi_01': Fr(3, 2) + d, 'pi_1/': Fr(3, 2) + gam, 'pi_11': min(Fr(3, 2) + d, Fr(3, 2) + 2*gam),
            'pi-slash_0': Fr(3, 2)}


GAMS = [Fr(1, 100), Fr(1, 20), Fr(1, 8), Fr(1, 5), Fr(249, 1000)]
ES = [Fr(1, 100), Fr(1, 3), Fr(1, 2), Fr(9, 10), Fr(99, 100)]


def s2(control=False):
    ok = True
    for gam, e in itertools.product(GAMS, ES):
        comps = iplus_components(gam, e)
        used = [v for k_, v in comps.items() if control or k_ != 'pi-slash_0']
        ok &= min(used) == Fr(3, 2) + (1 - e)*gam
    print("  S2%s: the least I+-exponent of the components in E^Ups G is lambda_# = 3/2 + (1 - e) gam at all %d "
          "samples: %s" % (" control (pi-slash_0 admitted)" if control else "", len(GAMS)*len(ES), ok), flush=True)
    return ok

# ---------------------------------------------------------------- S3


def s3(control=False):
    t, rr = sp.symbols('t_* r', positive=True)
    rI = t/(t + rr)
    rp = (t + rr)/(t*rr)
    rK = rr/(t + rr)
    ok = sp.simplify(rI*rp - 1/rr) == 0 and sp.simplify(rp*rK - 1/t) == 0
    dens = t*rr**3 if control else t*rr**4
    ratio = sp.simplify(dens*rI**4*rp**5*rK)
    ok_d = sp.simplify(ratio - 1) == 0
    # weights: f in rho^w L^2(|dt dx|) iff rho^-w f in L^2(dens mu_b) iff rho^(-w - shift) f in L^2(mu_b)
    a, b_, c_ = sp.symbols('a b c')
    sol = sp.solve([sp.Eq(sp.log(sp.simplify(dens.subs({t: 1/(rp*rK), rr: 1/(rI*rp)}))), 0)], [])  # unused
    shifts = None
    if not control:
        shifts = (2, sp.Rational(5, 2), sp.Rational(1, 2))       # half of the exponents 4, 5, 1
    else:
        # t r^3 = rho_I^-3 rho_+^-4 rho_K^-1 (rho_I rho_+ = 1/r, rho_+ rho_K = 1/t)
        ok_d = sp.simplify(t*rr**3*rI**3*rp**4*rK - 1) == 0
        shifts = (sp.Rational(3, 2), 2, sp.Rational(1, 2))
    aI, ap = sp.symbols('alpha_I alpha_+')
    bI, bp = aI + 2, ap + sp.Rational(5, 2)
    want = (bI + 1, bp + 2, sp.Rational(1, 2))
    got = (aI + 1 + shifts[0], ap + 2 + shifts[1], 0 + shifts[2])
    ok_w = all(sp.simplify(g_ - w_) == 0 for g_, w_ in zip(got, want))
    print("  S3%s: rho_I rho_+ = 1/r, rho_+ rho_K = 1/t_*: %s; density factorises: %s; (1.4) weights for mu_b = "
          "(b_I + 1, b_+ + 2, 1/2): %s" % (" control (n = 3 density t r^3)" if control else "", ok, ok_d, ok_w),
          flush=True)
    return ok and ok_d and ok_w

# ---------------------------------------------------------------- S4


def in_class(p, w):
    return p > w


def s4(control=False):
    x, eps = sp.symbols('x epsilon', positive=True)
    conv = sp.integrate(x**(2*eps - 1), (x, 0, 1))
    div = sp.integrate(x**(-1), (x, 0, 1))
    ok_int = conv == 1/(2*eps) and div == sp.oo
    ok = True
    n = 0
    for gam, e in itertools.product(GAMS, ES):
        d = (1 - e)*gam
        lam = Fr(3, 2) + d
        alpha = 4 + d/2
        eta = d/8
        for frac in (Fr(1, 100), Fr(1, 2), Fr(9, 10)):
            beta = frac*d
            b_plus = beta + Fr(1, 2)
            b_I = (b_plus + Fr(3, 2))/2
            alpha_I, alpha_p = b_I - 2, beta - 2
            cond13 = alpha_I < Fr(-1, 2) and alpha_p < alpha_I - Fr(1, 2)
            src_I = lam + 1
            src_iota = min(lam + 1 - min(eta, beta/4 if beta < d else eta), 3)
            src_K = Fr(0) if control else alpha - 2 - eta
            ok &= cond13 and in_class(src_I, b_I + 1) and in_class(src_iota, b_plus + 2) and in_class(src_K, Fr(1, 2))
            n += 1
    if control:
        print("  S4 control (no W** cut-off term: K+-order 0): the source lies in (1.4) at the samples: %s; "
              "int_0^1 x^-1 dx = %s" % (ok, div), flush=True)
        return ok
    print("  S4: int_0^1 x^(2 eps - 1) dx = %s, = oo at eps = 0: %s; (1.3) and the source in (1.4) at I+, iota+, K+ "
          "at %d samples: %s" % (conv, ok_int, n, ok), flush=True)
    return ok and ok_int

# ---------------------------------------------------------------- S5, S6


def commutator(G, chi_arg, Z, rep):
    """[Box, chi(arg)] Z with chi an arbitrary function; chi, chi', chi'' replaced by symbols"""
    chi = sp.Function('chi')
    w1 = [chi(chi_arg)*z for z in Z]
    B1 = box(G, w1)
    B0 = box(G, Z)
    out = [sp.expand(B1[m] - chi(chi_arg)*B0[m]) for m in range(N)]
    X0, X1, X2 = sp.symbols('X0 X1 X2')
    u = sp.Symbol('u_')
    rp = {sp.Subs(sp.Derivative(chi(u), (u, 2)), u, chi_arg): X2, sp.Subs(sp.Derivative(chi(u), u), u, chi_arg): X1}
    res = []
    for e_ in out:
        e_ = e_.replace(lambda ex: isinstance(ex, sp.Subs), lambda ex: X2 if ex.expr.diff(u, 2) == 0 and False else ex)
        e_ = e_.subs(rp).subs(chi(chi_arg), X0)
        e_ = e_.subs(rep)
        res.append(sp.expand(e_))
    return res


def jets_of(funcs, args):
    rep = {}
    for fn in funcs:
        for a in args:
            for b in args:
                rep[sp.diff(fn, a, b)] = sp.Symbol('J_%s_%s%s' % (fn.func.__name__, a, b))
        for a in args:
            rep[sp.diff(fn, a)] = sp.Symbol('J_%s_%s' % (fn.func.__name__, a))
        rep[fn] = sp.Symbol('J_%s' % fn.func.__name__)
    return rep


def s5(control=False):
    from admbox5 import outgoing_geo
    G, p_ = outgoing_geo()
    T = X[0]
    kap = sp.Function('kappa')(T)
    a, b, c = [sp.Function(n)(T, th) for n in ('a', 'b', 'c')]
    arg = (T + r) if control else (T + kap/r)
    report = []
    ok = True
    for p in (sp.Rational(3, 2), 1):
        Z = [r**(-p)*a, r**(-p)*b, r**(1 - p)*c, 0, 0]
        rep = {}
        rep.update(jets_of([a, b, c], [T, th]))
        rep.update({sp.diff(kap, T, 2): sp.Symbol('k2'), sp.diff(kap, T): sp.Symbol('k1'), kap: sp.Symbol('k0')})
        Cm = commutator(G, arg, Z, rep)
        frame = [1, 1, 1/r]
        lims = [sp.limit(sp.simplify(Cm[m]*frame[m]*r**(p + 1)), r, sp.oo) for m in range(3)]
        fin = all(finite(l_) for l_ in lims)
        report.append((str(p), fin))
        ok &= fin
    print("  S5%s: r^(p+1) [Box, chi(t_flat)] Z finite in an orthonormal frame, (p, finite): %s"
          % (" control (chi(t), t = T + r)" if control else "", report), flush=True)
    return ok


def s6(control=False):
    from admbox5 import outgoing_geo
    G, p_ = outgoing_geo()
    T = X[0]
    R0 = sp.Symbol('R0', positive=True)
    R = r/T
    a = sp.exp(R)*sp.cos(2*th)
    b = R/(1 + R)*sp.sin(th)**2
    c = R**2*sp.sin(th)*sp.cos(th)
    arg = r if control else R
    ok = True
    report = []
    for p in (2, sp.Rational(5, 2)):
        Z = [r**(-p)*a, r**(-p)*b, r**(1 - p)*c, 0, 0]
        Cm = commutator(G, arg, Z, {})
        frame = [1, 1, 1/r]
        lims = []
        for m in range(3):
            ex = sp.simplify((Cm[m]*frame[m]*r**(p + 2)).subs(T, r/R0))
            lims.append(sp.limit(ex, r, sp.oo))
        fin = all(finite(l_) for l_ in lims)
        report.append((str(p), fin))
        ok &= fin
    print("  S6%s: r^(p+2) [Box, chi] Z finite at fixed R = r/T, (p, finite): %s"
          % (" control (chi(r))" if control else "", report), flush=True)
    return ok

# ---------------------------------------------------------------- S7, S8


def s7(control=False):
    ok = True
    for beta in (Fr(1, 100), Fr(1, 10), Fr(1, 2), Fr(9, 10)):
        p = beta + Fr(1, 2) if control else Fr(3, 2)
        # exists b_I in (beta + 1/2, 3/2) with p + 1 > b_I + 1  iff  p > beta + 1/2
        exists = p > beta + Fr(1, 2)
        if exists:
            b_I = (beta + Fr(1, 2) + min(p, Fr(3, 2)))/2
            exists = beta + Fr(1, 2) < b_I < Fr(3, 2) and p + 1 > b_I + 1
        ok &= exists
    print("  S7%s: the slab commutator lies in (1.4) at I+ for beta in (0, 1): %s"
          % (" control (p = beta + 1/2)" if control else " (p = 3/2)", ok), flush=True)
    return ok


def s8(control=False):
    mu_, rho, vv = sp.symbols('mu rho v', positive=True)
    Tm = sp.sqrt(mu_)*sp.log((rho + sp.sqrt(mu_))/(rho - sp.sqrt(mu_)))
    dmuT = sp.diff(Tm, mu_)
    from hgauge5 import A_EXPR, B_EXPR
    if control:
        lim = sp.limit((vv/2)*(1/r**2)*r, vv, sp.oo)            # (v/2) W*_v at fixed r, times r
        print("  S8 control: r (v/2) W*_v at fixed r bounded as v -> oo: %s" % finite(lim), flush=True)
        return finite(lim)
    l1 = sp.limit(rho*dmuT, rho, sp.oo)
    l2 = sp.limit(r*A_EXPR, r, sp.oo)
    l3 = sp.limit(r*B_EXPR, r, sp.oo)
    R0 = sp.Symbol('R0', positive=True)
    # on iota+-interior: r = R0 t, v = t + r + O(log): r (v/2) |W*| -> (1 + R0)/(2 R0)
    t_ = sp.Symbol('t', positive=True)
    l4 = sp.limit(((t_ + R0*t_)/2)*(1/(R0*t_)**2)*(R0*t_), t_, sp.oo)
    ok = l1 == 2 and l2 == sp.Rational(1, 2) and l3 == sp.Rational(-1, 4) and finite(l4)
    print("  S8: rho d_mu T_mu -> %s, r A -> %s, r B -> %s, r (v/2) W*_v on iota+-interior -> %s: %s"
          % (l1, l2, l3, l4, ok), flush=True)
    return ok


CHECKS = [("S1", s1), ("S2", s2), ("S3", s3), ("S4", s4), ("S5", s5), ("S6", s6), ("S7", s7), ("S8", s8)]


def main():
    only = sys.argv[1:]
    ok = True
    for name, fn in CHECKS:
        if only and name not in only:
            continue
        good = fn()
        ctl = fn(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    print("EXIT %d" % (0 if ok else 1))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
