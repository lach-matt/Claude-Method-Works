#!/usr/bin/env python3
"""hgauge5.py -- GAUGEDECAY5.md section 2: the harmonic gauge in the class; the 1-form wave operator's horizon charge,
the forced linear growth and the horizon-regular gauge-fixed mass change, computed.

Background and class as in rwgauge5.py (ingoing chart, s = sqrt(mu) = r_h).  Box := 2 delta G delta^* on 1-forms
(III.D (1.1)), Theta(k) := delta G k with (delta k)_m = -nabla^a k_am (Part IX section 0); so Theta(L_X g) = Box X.
ell(J) := r_h^3 int_{S^3} J(d_v)|_{r = r_h} dw (III.D' (1.1)), and for a 1-form X near the horizon
    Q[X](v) := r_h^3 int_{S^3} (delta X + (dX)_{vr})|_{r = r_h} dw,
with delta X = -nabla^a X_a and (dX)_{vr} = d_v X_r - d_r X_v.

  H1 (exact) On the class, with general coefficients, Theta(L_X g) = (d delta + delta d) X = -nabla^a nabla_a X.
     Control: on the non-vacuum metric with f = 1 - mu/r the first identity fails (it needs Ric = 0).
  H2 (exact) The horizon charge.  For every class 1-form X with general coefficients, at r = r_h,
         r^3 (Box X)_v = d_v [ r^3 (delta X + (dX)_{vr}) ] - (r/(sin th cos th)) d_th ( sin th cos th (dX)_{th v} ),
     so, integrating over S^3, dQ[X]/dv = ell(Box X).  Control: at a general r the same identity fails.  Also: Q sees
     only the l = 0 part of X (checked on an l = 2 class 1-form, whose Q vanishes).
  H3 (exact) Values.  W* := dv/r^2 - dr/(r(r + s)) has Box W* = 0, delta W* = 0, (dW*)_{vr} = 2/r^3, Q[W*] = 4 pi^2;
     the Killing 1-form (d_v)^flat = -f dv + dr has Q = 4 pi^2 mu, and (d_v)^flat - mu W* is closed; ell([Box, v] W*)
     = 4 pi^2 (III.D' Lemma 3.1 (1)); Theta(dv^2/r^2) = -dv/r^3, so ell(Theta(dv^2/r^2)) = -2 pi^2; L_{W*} g != 0.
     Control: W* with the sign of its dr term reversed is not in the kernel.
  H4 (exact, with a 40-digit evaluation where simplify does not close) The horizon-regular gauge-fixed mass change.
         W** := (v/2) W* + A dv + B dr,   A = (s^2 + 2 r^2 log((r + s)/r))/(4 s r^2),
         B = (r^2 s - 3 r s^2 + 2 s^3 + 2 r^3 log r + 2 (s^3 - r^3) log(r + s) - 2 s^3 log s)/(4 r s (r^2 - s^2)),
     solves Box W** = -Theta(dv^2/r^2) = dv/r^3; B's numerator vanishes at r = s, so A and B are analytic across the
     horizon; r A and r B have finite limits at infinity; Q[W**](v) = 2 pi^2 v + const.  So K* := dv^2/r^2 + L_{W**} g
     is in harmonic gauge and equals (v/2) L_{W*} g plus a stationary tensor.  Control: the coefficient 1 in place of
     1/2 leaves Box W** - dv/r^3 != 0 (and Q's slope 4 pi^2 != ell(dv/r^3) = 2 pi^2).

Labels: computed (exact, sympy; H4's B-component residual at 40 digits).  Run: python3 checks/hgauge5.py
"""
import sys

import sympy as sp

from rwgauge5 import Geo, N, X, gam, legendre_S, mu, p1, p2, r, s, sqg, th, v, zero

GEO = Geo(1 - mu/r**2)
S3 = 2*sp.pi**2                                                  # |S^3|


def delta1(G, w):
    D = G.cov1(w)
    return -sum(G.gi[a, b]*D[a][b] for a in range(N) for b in range(N))


def dform(w):
    return [[sp.diff(w[b], X[a]) - sp.diff(w[a], X[b]) for b in range(N)] for a in range(N)]


def theta(G, h):
    t_ = G.tr(h)
    Gh = [[h[a][b] - G.g[a, b]*t_/2 for b in range(N)] for a in range(N)]
    D = G.cov2(Gh)
    return [-sum(G.gi[c, a]*D[c][a][m] for c in range(N) for a in range(N)) for m in range(N)]


def box(G, w):
    return theta(G, G.lie(w))


def hodge(G, w):
    F = dform(w)
    dF = G.cov2(F)                                               # nabla_c F_ab (F antisymmetric; cov2 is linear)
    dd = [-sum(G.gi[a, c]*dF[c][a][nu] for a in range(N) for c in range(N)) for nu in range(N)]
    de = delta1(G, w)
    return [sp.diff(de, X[nu]) + dd[nu] for nu in range(N)]


def bochner(G, w):
    D = G.cov1(w)
    DD = G.cov2(D)                                               # nabla_c (nabla_a w_b)
    return [-sum(G.gi[a, c]*DD[c][a][nu] for a in range(N) for c in range(N)) for nu in range(N)]


def class_form():
    return [sp.Function(n)(v, r, th) for n in ("Xv", "Xr", "Xth")] + [0, 0]


def h1(control=False):
    G = Geo(1 - mu/r) if control else GEO
    W = class_form()
    b = box(G, W)
    hd = hodge(G, W)
    ok1 = all(zero(b[i] - hd[i]) for i in range(N))
    if control:
        print("  H1 control (f = 1 - mu/r, not vacuum): Theta(L_X g) = (d delta + delta d) X: %s" % ok1, flush=True)
        return ok1
    bo = bochner(G, W)
    ok2 = all(zero(b[i] - bo[i]) for i in range(N))
    print("  H1: Theta(L_X g) = (d delta + delta d) X: %s; = -nabla^a nabla_a X: %s" % (ok1, ok2), flush=True)
    return ok1 and ok2


def charge_density(G, w):
    """r^3 (delta X + (dX)_{vr})"""
    return r**3*(delta1(G, w) + dform(w)[0][1])


def h2(control=False):
    W = class_form()
    b = box(GEO, W)
    F = dform(W)
    res = r**3*b[0] - sp.diff(charge_density(GEO, W), v) + r*sp.diff(sqg*F[2][0], th)/sqg
    if control:
        ok = zero(res.subs(r, 2*s).doit())
        print("  H2 control: the identity at r = 2 r_h: %s" % ok, flush=True)
        return ok
    ok = zero(res.subs(r, s).doit())
    print("  H2: r^3 (Box X)_v = d_v[r^3 (delta X + (dX)_vr)] - (r/sqrt gamma) d_th(sqrt gamma (dX)_{th v}) at r_h: %s"
          % ok, flush=True)
    a, bb, c = [sp.Function(n)(v, r) for n in ("a", "b", "c")]
    S = legendre_S(1)
    W2 = [a*S, bb*S, c*sp.diff(S, th), 0, 0]
    q2 = sp.integrate(sp.expand(charge_density(GEO, W2).subs(r, s).doit()*sqg), (th, 0, sp.pi/2))
    ok2 = zero(q2)
    print("  H2: Q of an l = 2 class 1-form vanishes (Q sees only the l = 0 part): %s" % ok2, flush=True)
    return ok and ok2


def Q_l0(G, w):
    """Q for a spherically symmetric 1-form: r_h^3 |S^3| (delta X + (dX)_vr) at r_h"""
    return sp.simplify(S3*charge_density(G, w).subs(r, s))


def ell_l0(J):
    return sp.simplify(S3*s**3*J[0].subs(r, s))


WSTAR = [1/r**2, -1/(r*(r + s)), 0, 0, 0]


def h3(control=False):
    f = 1 - mu/r**2
    if control:
        Wc = [1/r**2, 1/(r*(r + s)), 0, 0, 0]
        ok = all(zero(e) for e in box(GEO, Wc))
        print("  H3 control: dv/r^2 + dr/(r(r+s)) in the kernel of Box: %s" % ok, flush=True)
        return ok
    ok = all(zero(e) for e in box(GEO, WSTAR)) and zero(delta1(GEO, WSTAR)) and zero(dform(WSTAR)[0][1] - 2/r**3)
    qW = Q_l0(GEO, WSTAR)
    Kil = [-f, 1, 0, 0, 0]
    qK = Q_l0(GEO, Kil)
    diff = [Kil[i] - mu*WSTAR[i] for i in range(N)]
    closed = all(zero(e) for row in dform(diff) for e in row)
    vW = [v*e for e in WSTAR]
    comm = [sp.simplify(e) for e in box(GEO, vW)]                  # = [Box, v] W* as Box W* = 0
    ellc = ell_l0(comm)
    K = [[0]*N for _ in range(N)]
    K[0][0] = 1/r**2
    TK = [sp.simplify(e) for e in theta(GEO, K)]
    ellK = ell_l0(TK)
    LW = GEO.lie(WSTAR)
    nonzero = any(not zero(e) for row in LW for e in row)
    ok &= qW == 4*sp.pi**2 and zero(qK - 4*sp.pi**2*mu) and closed and zero(ellc - 4*sp.pi**2)
    ok &= zero(TK[0] + 1/r**3) and all(zero(e) for e in TK[1:]) and zero(ellK + 2*sp.pi**2) and nonzero
    print("  H3: Box W* = 0, delta W* = 0, (dW*)_vr = 2/r^3; Q[W*] = %s; Q[(d_v)^flat] = %s; (d_v)^flat - mu W* closed: "
          "%s; ell([Box, v] W*) = %s; Theta(dv^2/r^2) = %s, ell = %s; L_{W*} g != 0: %s"
          % (qW, qK, closed, ellc, TK[0], ellK, nonzero), flush=True)
    return ok


A_EXPR = (s**2 + 2*r**2*sp.log((r + s)/r))/(4*s*r**2)
B_NUM = r**2*s - 3*r*s**2 + 2*s**3 + 2*r**3*sp.log(r) + 2*(s**3 - r**3)*sp.log(r + s) - 2*s**3*sp.log(s)
B_EXPR = B_NUM/(4*r*s*(r**2 - s**2))
POINTS = [(sp.Rational(5, 3), sp.Rational(3, 2)), (sp.Rational(11, 4), sp.Rational(3, 2)), (sp.Integer(9), 1),
          (sp.Rational(7, 5), sp.Rational(4, 3)), (sp.Rational(3, 2), sp.Rational(1, 2)), (sp.Integer(40), 3)]


def h4(control=False):
    c = 1 if control else sp.Rational(1, 2)
    W = [c*v*WSTAR[0] + A_EXPR, c*v*WSTAR[1] + B_EXPR, 0, 0, 0]
    bW = box(GEO, W)
    res = [bW[0] - 1/r**3, bW[1]] + bW[2:]
    vals = []
    for rr, ss in POINTS:
        for e in res[:2]:
            vals.append(abs(sp.N(e.subs({v: sp.Rational(7, 3), r: rr, s: ss}), 40)))
    small = max(vals) < sp.Float("1e-30")
    if control:
        print("  H4 control (coefficient 1): residual max %.3e, solves: %s" % (float(max(vals)), small), flush=True)
        return small
    exact_v = zero(res[0])
    ang = all(zero(e) for e in res[2:])
    regular = zero(B_NUM.subs(r, s))
    inf = [sp.limit(r*A_EXPR, r, sp.oo), sp.limit(r*B_EXPR, r, sp.oo)]
    near = [sp.N(B_EXPR.subs({s: sp.Rational(3, 2), r: sp.Rational(3, 2) + d}), 25) for d in (sp.Rational(1, 10**8),
                                                                                       -sp.Rational(1, 10**8))]
    cd = charge_density(GEO, W)
    slope = sp.simplify(S3*sp.diff(cd, v).subs(r, s))            # A, B are v-free: Q's v-dependence
    stat_q = [sp.N(S3*cd.subs({v: 0, s: sp.Rational(3, 2), r: sp.Rational(3, 2) + d}), 20)
              for d in (sp.Rational(1, 10**8), -sp.Rational(1, 10**8))]
    LW = GEO.lie(WSTAR)
    Ks = GEO.lie(W)
    stat = all(zero(sp.diff(Ks[a][b] - v*LW[a][b]/2, v)) for a in range(N) for b in range(N))
    ok = exact_v and small and ang and regular and all(x.is_finite for x in inf) and zero(slope - 2*sp.pi**2) and stat
    print("  H4: Box W** = dv/r^3: v-component exact %s, all components at 6 points to 40 digits (max %.2e) %s; "
          "B's numerator at r = s vanishes: %s (B at r_h -+ 1e-8: %s, %s); r A, r B -> %s; dQ[W**]/dv = %s (Q at v = 0, "
          "r_h -+ 1e-8, s = 3/2: %s, %s); L_{W**} g - (v/2) L_{W*} g stationary: %s"
          % (exact_v, float(max(vals)), small, regular, near[1], near[0], inf, slope, stat_q[1], stat_q[0], stat),
          flush=True)
    return ok


CHECKS = [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]


def main():
    ok = True
    for name, fn in CHECKS:
        good = fn()
        ctl = fn(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
