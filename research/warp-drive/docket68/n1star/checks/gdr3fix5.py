#!/usr/bin/env python3
"""gdr3fix5.py -- GAUGEDECAY5.md Round 4, section R4.c: the round-3 verifier's findings on gdscri5.py and gdsk5.py,
computed.  Charts and helpers as in gdscri5.py, gdsk5.py, admbox5.py, hgauge5.py (outgoing chart with T := t_*).

  T1 (exact) S5 with the actual t_flat.  II.C Lemma 3.2 (a) at l = 1/2 (as I-CONE:31 fixes it) gives t_flat = T(1 -
     (T/r)^(1/2)), not T + kappa(T)/r.  For Z = r^-p (a dT + b dr + r c dth), a, b, c arbitrary functions of (T, th),
     r^(p+1) [Box, chi(t_flat)] Z is finite as r -> oo in an orthonormal frame at p = 3/2 and p = 1: one order is
     gained at I+, as round 3 said.  At p = 1 the gain is exactly one (r^(p+3/2) of it is not finite).  Control: the
     static time, chi(t), t = T + r, gains nothing (r^(p+1) of it is not finite).
  T2 (exact, q symbolic) K3 at every spatial order q.  For U = r^-q (a dT + b dr + r c dth) with a, b, c functions of th
     and q a real symbol, the coefficients A1 of d_T and A2 of d_T^2 in Box^Ups(phi(T) U), with c_Ups = |x|^-1 dt, are
     O(r^-(q+1)) and O(r^-(q+2)) in an orthonormal frame: K3's gain for every q, not only q in {3, 7/2}.  Control: with
     c_Ups = dt, A1 is not O(r^-(q+1)).
  T3 (exact, symbolic) The linear inequalities of K4, S2, S4 and S7, proved on the whole parameter box (not sampled):
     with beta = u d, eta = s (d - beta), u, s in (0, 1), d = (1 - e) gam in (0, 1/4) (I10:45-46), every condition is a
     sum of terms positive on the box (each difference is written as such a sum and checked equal).  Control: at
     s = 1 (eta = d - beta) the condition on h's iota+-order is an equality, not an inequality.
  T4 (exact) S8's control, computed: the components of W**_H at fixed r = 2 r_h grow in v (v^-1 W**_v -> 1/(8 r_h^2),
     not 0), so W**_H has no K+-order; round 3's control was a hand-written limit.  Control: W*'s components at fixed r
     are bounded in v.
  T5 (exact) S4's second control, computed: Theta(K) on {r <= 2R_1}, K = r^-2 dv^2 there (0.1), is r^-3 dv (H3's
     value with sign), stationary and nonzero, so of K+-order 0, below the 1/2 that (1.4) asks; round 3 set the order 0
     by hand.  Control: Theta of the stationary K* (Proposition 2.1 (d)) minus its linear part vanishes, so the
     source with the W** term carried has no stationary part.

Labels: computed (exact, sympy).  Run: python3 checks/gdr3fix5.py   (several minutes)
"""
import itertools
import sys

import sympy as sp

import gdscri5 as S
from rwgauge5 import N, X, r, s, th, v, mu
from admbox5 import outgoing_geo


def finite(lim):
    return S.finite(lim)


# --------------------------------------------------------------------------------------------------------------- T1
def t1(control=False):
    G, _ = outgoing_geo()
    T = X[0]
    a, b, c = [sp.Function(n)(T, th) for n in ('a', 'b', 'c')]
    arg = (T + r) if control else T*(1 - sp.sqrt(T/r))
    rep = S.jets_of([a, b, c], [T, th])
    rows = []
    ok = True
    for p in (sp.Rational(3, 2), sp.Integer(1)):
        Z = [r**(-p)*a, r**(-p)*b, r**(1 - p)*c, 0, 0]
        Cm = S.commutator(G, arg, Z, rep)
        frame = [1, 1, 1/r]
        fin1 = all(finite(sp.limit(sp.simplify(Cm[m]*frame[m]*r**(p + 1)), r, sp.oo)) for m in range(3))
        row = [str(p), fin1]
        if p == 1 and not control:
            fin32 = all(finite(sp.limit(sp.simplify(Cm[m]*frame[m]*r**(p + sp.Rational(3, 2))), r, sp.oo))
                        for m in range(3))
            row.append(fin32)
            ok &= fin1 and not fin32
        else:
            ok &= fin1
        rows.append(tuple(row))
    print("  T1%s: (p, r^(p+1) [Box, chi(t_flat)] Z finite[, at p = 1: r^(p+3/2) finite]): %s"
          % (" control (chi(t), t = T + r)" if control else " (t_flat = T(1 - (T/r)^(1/2)))", rows), flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- T2
def t2(control=False):
    from hgauge5 import theta
    T = X[0]
    G, p = outgoing_geo()
    gam_, e_ = sp.symbols('gamma_Ups e_Ups', positive=True)
    q = sp.Symbol('q', real=True)
    cU = [1, p, 0, 0, 0] if control else [1/r, p/r, 0, 0, 0]
    cvec = [sum(G.gi[a, b]*cU[b] for b in range(N)) for a in range(N)]

    def Eups(k):
        trk = G.tr(k)
        iota = [sum(cvec[a]*k[a][m] for a in range(N)) for m in range(N)]
        return [-gam_*(2*iota[m] - sp.Rational(2, 3)*(1 - e_)*cU[m]*trk) for m in range(N)]

    def boxU(w):
        L = G.lie(w)
        trL = G.tr(L)
        GL = [[L[a][b] - G.g[a, b]*trL/2 for b in range(N)] for a in range(N)]
        th_ = theta(G, L)
        E_ = Eups(GL)
        return [th_[m] + E_[m] for m in range(N)]
    phi = sp.Function('phi')(T)
    P0, P1, P2 = sp.symbols('P0 P1 P2')
    a, b, c = [sp.Function(n)(th) for n in ('a', 'b', 'c')]
    U = [r**(-q)*a, r**(-q)*b, r**(1 - q)*c, 0, 0]
    E = boxU([phi*u for u in U])
    rep = {sp.Derivative(phi, (T, 2)): P2, sp.Derivative(phi, T): P1}
    E = [sp.expand(e.subs(rep).subs(phi, P0)) for e in E]
    jets = {}
    for fn in (a, b, c):
        for k in range(3):
            jets[sp.diff(fn, th, k) if k else fn] = sp.Symbol('%s%d' % (fn.func.__name__, k))
    frame = [1, 1, 1/r, 1, 1]
    rows = []
    ok = True
    for coef, gain in ((P1, 1), (P2, 2)):
        fins = []
        for m in range(3):
            ex = sp.diff(E[m], coef)*frame[m]
            ex = ex.subs({sp.Derivative(fn, (th, k)): jets[sp.diff(fn, th, k)] for fn in (a, b, c)
                          for k in (2, 1)}).subs({fn: jets[fn] for fn in (a, b, c)})
            ex = sp.powsimp(sp.expand(ex*r**(q + gain)), force=True)
            ex = sp.simplify(ex)
            lim = sp.limit(ex, r, sp.oo)
            fins.append(finite(lim) and not lim.has(q) or (finite(lim) and lim.has(q)))
        rows.append(('A1' if coef == P1 else 'A2', all(fins)))
        if control and coef == P2:
            continue
        ok &= all(fins)
    print("  T2%s: Box^Ups(phi(t_*) U), U of spatial order q (symbolic): (coefficient, r^(q+1) A1 U resp. r^(q+2) A2 U "
          "finite for every q): %s" % (" control (c_Ups = dt)" if control else "", rows), flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- T3
def positive_sum(expr, pos):
    """expr, after substitution, equals a polynomial in the 'pos' symbols (each in (0, 1) or (0, oo) as declared) with
    positive coefficients times a positive monomial: a sufficient, exact test of positivity on the open box"""
    num, den = sp.fraction(sp.factor(sp.together(expr)))
    def pos_poly(P):
        P = sp.Poly(sp.expand(P), *pos)
        return not P.is_zero and all(cf > 0 for cf in P.coeffs())
    return pos_poly(num) and pos_poly(den)


def t3(control=False):
    # parametrise the box by positive symbols: d = D/(4(1 + D)) in (0, 1/4), u = U/(1 + U), s = S/(1 + S) in (0, 1)
    D, U, Sg, E = sp.symbols('D U S E', positive=True)
    d = D/(4*(1 + D))
    u = U/(1 + U)
    sv = 1 if control else Sg/(1 + Sg)
    beta = u*d
    eta = sv*(d - beta)
    lam = sp.Rational(3, 2) + d
    alpha = 4 + d/2
    pos = [D, U, Sg]
    conds = {
        # K4 (S_K): h's iota+-order lam - eta > 3/2 + beta; K+-order alpha - 2 - eta > 1/2; rows lam + 1 - eta > 5/2 +
        # beta; J_h's iota+-order > beta + 5/2
        'K4 h iota+': (lam - eta) - (sp.Rational(3, 2) + beta),
        'K4 h K+': (alpha - 2 - eta) - sp.Rational(1, 2),
        'K4 rows iota+': (lam + 1 - eta) - (sp.Rational(5, 2) + beta),
        # S2: the least exponent seen by E^Ups G is lam = 3/2 + d, below 3/2 + gam (pi_1/) and 3/2 + 2 gam, at e in (0,1)
        'S2 pi_1/ - lam': (sp.Rational(3, 2) + d/(1 - E/(1 + E))) - lam,
        # S4 / S7: b_+ = beta + 1/2, b_I = (b_+ + 3/2)/2: (1.3) b_I < 3/2, b_+ < b_I; source orders above the weights
        'S4 b_I < 3/2': sp.Rational(3, 2) - (beta + sp.Rational(1, 2) + sp.Rational(3, 2))/2,
        'S4 b_+ < b_I': (beta + sp.Rational(1, 2) + sp.Rational(3, 2))/2 - (beta + sp.Rational(1, 2)),
        'S4 I+': (lam + 1) - ((beta + 2)/2 + 1),
        'S4 iota+': (lam + 1 - eta) - (beta + sp.Rational(5, 2)),
        'S4 K+': (alpha - 2 - eta) - sp.Rational(1, 2),
        # S7: p = 3/2 against b_I
        'S7 p > b_I': sp.Rational(3, 2) - (beta + 2)/2,
    }
    res = {}
    for k, ex in conds.items():
        ex = sp.simplify(ex)
        if ex.has(E):
            res[k] = positive_sum(ex, pos + [E])
        else:
            res[k] = positive_sum(ex, pos) if ex.free_symbols else bool(ex > 0)
    if control:
        k = 'K4 h iota+'
        print("  T3 control (eta = d - beta): %s is positive on the box: %s (it is %s)"
              % (k, res[k], sp.simplify(conds[k])), flush=True)
        return res[k]
    print("  T3: each condition is a positive sum on the whole box: %s" % res, flush=True)
    return all(res.values())


# --------------------------------------------------------------------------------------------------------------- T4
def t4(control=False):
    from hgauge5 import A_EXPR, B_EXPR, WSTAR
    W = [v/2*WSTAR[0] + A_EXPR, v/2*WSTAR[1] + B_EXPR] if not control else [WSTAR[0], WSTAR[1]]
    vals = [sp.limit(sp.simplify(w.subs(r, 2*s)/v), v, sp.oo) for w in W]
    grows = any(vv != 0 for vv in vals)
    bounded = all(finite(sp.limit(sp.simplify(w.subs(r, 2*s)), v, sp.oo)) for w in W)
    if control:
        print("  T4 control (W*): components at r = 2 r_h bounded in v: %s; v^-1 times them -> %s" % (bounded, vals),
              flush=True)
        return not bounded
    print("  T4: W**_H's components at r = 2 r_h (V^flat is stationary and drops out), v^-1 times them -> %s: grow "
          "linearly, no K+-order: %s" % (vals, grows), flush=True)
    return grows


# --------------------------------------------------------------------------------------------------------------- T5
def t5(control=False):
    from hgauge5 import GEO, theta, A_EXPR, B_EXPR, WSTAR
    K = [[0]*N for _ in range(N)]
    K[0][0] = 1/r**2
    th_ = theta(GEO, K)
    stat = all(sp.diff(e, v) == 0 for e in th_)
    vals = [sp.simplify(e) for e in th_]
    nonzero = any(vv != 0 for vv in vals)
    if control:
        W = [v/2*WSTAR[0] + A_EXPR, v/2*WSTAR[1] + B_EXPR, 0, 0, 0]
        L = GEO.lie(W)
        Ks = [[K[a][b] + L[a][b] for b in range(N)] for a in range(N)]
        tk = theta(GEO, Ks)
        z = all(sp.simplify(sp.expand_log(sp.simplify(e), force=True)) == 0 for e in tk)
        print("  T5 control: Theta(r^-2 dv^2 + L_{W**} g) has a nonzero (stationary) part: %s" % (not z), flush=True)
        return not z
    ok = stat and nonzero and sp.simplify(vals[0] + 1/r**3) == 0
    print("  T5: Theta(r^-2 dv^2) = %s: stationary %s, nonzero %s: K+-order 0, below the 1/2 of (1.4): %s"
          % (vals[:2], stat, nonzero, ok), flush=True)
    return ok


CHECKS = [("T1", t1), ("T2", t2), ("T3", t3), ("T4", t4), ("T5", t5)]


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
