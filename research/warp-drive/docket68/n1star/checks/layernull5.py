#!/usr/bin/env python3
"""layernull5.py -- the identities and inequalities of the energy, transport and remainder arguments of
EQUALITY5-LAYER.md round 2 (Lemmas L.8-L.10, L.3, L.4 and L.4_P).

Coordinates (v, r, th, phi1, phi2) of EQUALITY5 (0.1): g0 = -F dv^2 + 2 dv dr + r^2 sigma, F = 1 - mu(v)/r^2; tau =
v - r; ell = g0^-1 dv = d_r (past null), L0 = -ell (future null), Y := -g0^-1 dtau (the multiplier of the supplement's
Lemma 2.3).  T(X, Z) := (X u)(Z u) - (1/2) g0(X, Z) g0^-1(du, du), the energy tensor of a component u.

  E1 (exact, every mu(v)) The flux density through a null face {v = const}: T(L0, Y) = (1/2)(1 + mu/r^2)(ell u)^2 +
     (1/(2 r^2)) |dring u|^2 (dring u: the derivatives on the unit S^3), with no transverse derivative d_v u; the volume
     density is r^3 cos th sin th; Y is future timelike (g0(Y, Y) = -1 - mu/r^2, dtau(Y) = 1 + mu/r^2) and L0 future
     null (dtau(L0) = 1).  So the flux of the energy current through {v = const}, on the side of the region to its past,
     is int T(L0, Y) r^3 dr domega >= 0 and controls ell u and the angular derivatives there.  Control: the normal of
     {r = const}, g0^-1 dr, in place of L0 gives a form that is indefinite at r > sqrt(mu) (a timelike face's flux has
     no sign).
  E2 (exact) The L^2 transport identity on a slice {a <= r <= b(tau)} (radial model; the angles integrate out): with
     d_tau = L0 + d_r in (tau, r), d_tau int phi^2 r^3 dr = 2 int phi (L0 phi) r^3 dr - 3 int phi^2 r^2 dr + (1 + b')
     phi(b)^2 b^3 - phi(a)^2 a^3; for the slices of Omega_v := Omega cap {v' <= v}, b = v - tau, the outer term is
     exactly zero (L0 is tangent to {v' = v}); for the energy's L^2 term the outer coefficient is b' = -1 <= 0.
     Control: a slice with fixed outer radius (b' = 0) leaves the outer term phi(b)^2 b^3 with the wrong sign.
  E3 (exact) The tilted face of Lemma L.4: g0^-1(dv, dv) = 0, g0^-1(dv, dtau) = -1, g0^-1(dtau, dtau) = -1 - mu/r^2, so
     for alpha := dv + eps dtau, g0^-1(alpha, alpha) = -2 eps - eps^2 (1 + mu/r^2); |alpha|_e^2 = (1 + eps)^2 + 1 in
     Cartesian components; with |(g_lam^-1 - g0^-1)(alpha, alpha)| <= C1 lam |alpha|_e^2 and eps := 2 C1 lam =: 2 s, the
     worst case is -2 s + 4 s^3 - 4 s^2 mu/r^2 < 0 for 0 < s <= 1/2: alpha is g_lam-timelike; alpha(Y) = 1 + eps (1 +
     mu/r^2) > 0 (future side); the slices' outer radius v1 - eps (tau - tau0) - tau has derivative -1 - eps < 0.
     Control: eps := C1 lam/2 makes the worst case positive.
  E4 (exact) The past tilted face of Lemma L.4_P: psi(tau) := 2 t^(-1/2), t := 1 + tau0 - tau, on tau <= tau0, and
     psi := 2 + tau - tau0 on tau >= tau0: C^1 at tau0 (psi = 2, psi' = 1 from both sides), increasing, bounded by 2
     on the past side, psi' = t^(-3/2).  With the perturbation C_P lam t^(-3/2) |alpha|_e^2 on P and eps := 2 C_P lam
     =: 2 s, alpha := dv + eps psi' dtau has worst case -2 s psi' + 2 s^3 psi'^3 - 4 s^2 psi'^2 mu/r^2 < 0 for s psi' <=
     1/2.  Control: psi' = t^-2 (a tilt decaying faster than the perturbation) is positive at t = 100, s = 1/10.
  E5 (exact) The integrals: int_r^oo r'^-3 dr' = 1/(2 r^2) (the null-face Cauchy-Schwarz); int_(-oo)^(tau0) t^(-3/2)
     dtau = 2 (the far kernel); the L^2 norm of r^-3 on {t + a1 <= r <= t + a2} with measure r^3 dr is at most (a2 -
     a1)^(1/2) t^(-3/2); the transport from infinity, r^(-3/2) int_r^oo r'^(3/2) r'^-q dr' = r^(1-q)/(q - 5/2) for q >
     5/2, at q = 13/4: (4/3) r^(-9/4); min(x, y) <= (x y)^(1/2).  Control: q = 5/2 diverges.
  E6 (exact) The equation for the remainder: if Ric^H(g) = -(1/2) G(g) H(g) + Q(g) (G the inverse metric, H the second
     derivatives, Q the rest) and Ric^H(g_app + w) = 0, then -(1/2) G(g_lam) H(w) = -Ric^H(g_app) + (1/2)(G(g_lam) -
     G(g_app)) H(g_app) - (Q(g_lam) - Q(g_app)).  Control: the middle term with the opposite sign fails.

Labels: computed (exact, sympy).  Run: python3 checks/layernull5.py   (about ten seconds)
"""
import sys

import sympy as sp

v, r, th, p1, p2 = sp.symbols('v r theta phi1 phi2', real=True)
mu = sp.Function('mu')(v)
F = 1 - mu/r**2
c, s_ = sp.cos(th), sp.sin(th)
g = sp.Matrix([[-F, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, r**2, 0, 0], [0, 0, 0, r**2*c**2, 0],
               [0, 0, 0, 0, r**2*s_**2]])
gi = sp.simplify(g.inv())
dv = sp.Matrix([1, 0, 0, 0, 0])
dr = sp.Matrix([0, 1, 0, 0, 0])
dtau = dv - dr
u = sp.Matrix(sp.symbols('u_v u_r u_t u_1 u_2', real=True))


def T(Xv, Zv):
    return (u.T*Xv)[0]*(u.T*Zv)[0] - sp.Rational(1, 2)*(Xv.T*g*Zv)[0]*(u.T*gi*u)[0]


def e1(control=False):
    L0 = -gi*dv
    Y = -gi*dtau
    if control:
        N = gi*dr
        Q = sp.hessian(T(N, Y), list(u))/2
        Qn = Q.subs({mu: 1, r: 2, th: sp.pi/5})
        ev = [sp.N(x) for x in Qn.eigenvals()]
        return all(x >= -1e-12 for x in ev)
    flux = sp.simplify(T(L0, Y))
    target = (1 + mu/r**2)*u[1]**2/2 + (u[2]**2 + u[3]**2/c**2 + u[4]**2/s_**2)/(2*r**2)
    ok = sp.simplify(flux - target) == 0
    vol = sp.simplify(sp.sqrt(-g.det()) - r**3*c*s_) == 0
    YY = sp.simplify((Y.T*g*Y)[0] + 1 + mu/r**2) == 0
    tY = sp.simplify((dtau.T*Y)[0] - 1 - mu/r**2) == 0
    tL = sp.simplify((dtau.T*L0)[0] - 1) == 0 and sp.simplify((L0.T*g*L0)[0]) == 0
    print("  E1 T(L0, Y) = (1/2)(1 + mu/r^2)(ell u)^2 + |dring u|^2/(2 r^2): %s; volume density r^3 c s: %s; g0(Y, Y) ="
          " -1 - mu/r^2: %s, dtau(Y) = 1 + mu/r^2: %s; L0 future null: %s" % (ok, vol, YY, tY, tL), flush=True)
    return ok and vol and YY and tY and tL


def e2(control=False):
    tau, a, V = sp.symbols('tau a V', real=True)
    cs = sp.symbols('k0:12')
    phi = sum(cs[3*i + j]*tau**i*r**j for i in range(4) for j in range(3))
    b = sp.Symbol('B') if control else V - tau
    I_ = sp.integrate(phi**2*r**3, (r, a, b))
    lhs = sp.diff(I_, tau)
    L0phi = sp.diff(phi, tau) - sp.diff(phi, r)
    rhs = (2*sp.integrate(phi*L0phi*r**3, (r, a, b)) - 3*sp.integrate(phi**2*r**2, (r, a, b))
           - (phi**2*r**3).subs(r, a))
    outer = sp.simplify(lhs - rhs)                       # what is left: (1 + b') phi(b)^2 b^3
    if control:
        return sp.simplify(outer) == 0
    ok = outer == 0
    # the energy's L^2 term: d_tau int u^2 r^3 = 2 int u d_tau u r^3 + b' u(b)^2 b^3, b' = -1
    ok2 = sp.diff(b, tau) == -1
    print("  E2 d_tau int_a^(v-tau) phi^2 r^3 = 2 <phi, L0 phi> - 3 int phi^2 r^2 - phi(a)^2 a^3 (outer term zero): %s;"
          " the energy slices' outer radius derivative -1: %s" % (ok, ok2), flush=True)
    return ok and ok2


def e3(control=False):
    eps, s, mu_ = sp.symbols('epsilon s mu_', positive=True)
    gvv = (dv.T*gi*dv)[0]
    gvt = sp.simplify((dv.T*gi*dtau)[0])
    gtt = sp.simplify((dtau.T*gi*dtau)[0])
    al = dv + eps*dtau
    galal = sp.simplify((al.T*gi*al)[0])
    form = sp.simplify(galal - (-2*eps - eps**2*(1 + mu/r**2))) == 0
    contr = gvv == 0 and sp.simplify(gvt + 1) == 0 and sp.simplify(gtt + 1 + mu/r**2) == 0
    norm2 = (1 + eps)**2 + 1                            # alpha = (1 + eps) dtau + xhat.dx in Cartesian components
    e_ = s/2 if control else 2*s
    worst = sp.expand((galal + s*norm2).subs(eps, e_))
    if control:
        return bool(worst.subs({mu: 1, r: 2, s: sp.Rational(1, 10)}) < 0)
    closed = sp.simplify(worst - (-2*s + 4*s**3 - 4*s**2*mu/r**2)) == 0
    neg = all(sp.Rational(j, 20)*(-2 + 4*sp.Rational(j, 20)**2) < 0 for j in range(1, 11))
    Y = -gi*dtau
    aY = sp.simplify((al.T*Y)[0] - (1 + eps*(1 + mu/r**2))) == 0
    print("  E3 contractions: %s; g0^-1(alpha, alpha) = -2 eps - eps^2 (1 + mu/r^2): %s; worst case at eps = 2 C1 lam:"
          " -2 s + 4 s^3 - 4 s^2 mu/r^2: %s, negative on (0, 1/2]: %s; alpha(Y) = 1 + eps (1 + mu/r^2): %s"
          % (contr, form, closed, neg, aY), flush=True)
    return contr and form and closed and neg and aY


def e4(control=False):
    tau, tau0, s = sp.symbols('tau tau0 s', positive=True)
    t = 1 + tau0 - tau
    psi = 2*t**sp.Rational(-1, 2)
    dpsi = sp.simplify(sp.diff(psi, tau))
    c1 = sp.simplify(dpsi - t**sp.Rational(-3, 2)) == 0
    at0 = sp.simplify(psi.subs(tau, tau0) - 2) == 0 and sp.simplify(dpsi.subs(tau, tau0) - 1) == 0
    lim = sp.limit(psi.subs(tau, tau0 - sp.Symbol('T', positive=True)), sp.Symbol('T', positive=True), sp.oo) == 0
    tt = sp.Symbol('t', positive=True)
    pp = tt**-2 if control else tt**sp.Rational(-3, 2)
    eps = 2*s
    al = dv + eps*pp*dtau
    galal = sp.simplify((al.T*gi*al)[0])
    worst = sp.expand(galal + s*tt**sp.Rational(-3, 2)*((1 + eps*pp)**2 + 1))
    if control:
        return bool(worst.subs({mu: 1, r: 2, s: sp.Rational(1, 10), tt: 100}) < 0)
    closed = sp.simplify(worst - (-2*s*pp + 2*s**3*pp**3 - 4*s**2*pp**2*mu/r**2)) == 0
    print("  E4 psi' = t^(-3/2): %s; psi(tau0) = 2, psi'(tau0) = 1 (C^1 with 2 + tau - tau0): %s; psi -> 0 at the past:"
          " %s; worst case -2 s psi' + 2 s^3 psi'^3 - 4 s^2 psi'^2 mu/r^2: %s (negative for s psi' <= 1/2)"
          % (c1, at0, lim, closed), flush=True)
    return c1 and at0 and lim and closed


def e5(control=False):
    rr, rp, t, a1, a2, qq = sp.symbols('rr rp t a1 a2 q', positive=True)
    if control:
        val = sp.integrate(rp**sp.Rational(3, 2)*rp**sp.Rational(-5, 2), (rp, rr, sp.oo))
        return val.is_finite
    i1 = sp.simplify(sp.integrate(rp**-3, (rp, rr, sp.oo)) - 1/(2*rr**2)) == 0
    tau, tau0 = sp.symbols('tau tau0', real=True)
    i2 = sp.simplify(sp.integrate((1 + tau0 - tau)**sp.Rational(-3, 2), (tau, -sp.oo, tau0)) - 2) == 0
    l2 = sp.integrate(rp**-6*rp**3, (rp, t + a1, t + a2))
    i3 = sp.simplify(l2 - ((t + a1)**-2 - (t + a2)**-2)/2) == 0           # <= (a2 - a1) (t + a1)^-3 <= (a2 - a1) t^-3
    q0 = sp.Rational(13, 4)
    tr = sp.simplify(rr**sp.Rational(-3, 2)*sp.integrate(rp**sp.Rational(3, 2)*rp**-q0, (rp, rr, sp.oo))
                     - rr**(1 - q0)/(q0 - sp.Rational(5, 2))) == 0
    x, y = sp.symbols('x y', positive=True)
    mm = all(min(xa, ya) <= sp.sqrt(xa*ya) for xa in (sp.Rational(1, 3), 2, 7) for ya in (sp.Rational(1, 5), 3))
    print("  E5 int_r^oo r'^-3 = 1/(2 r^2): %s; int t^(-3/2) dtau = 2: %s; int r^-6 r^3 dr = ((t+a1)^-2 - (t+a2)^-2)/2:"
          " %s; transport from infinity at q = 13/4: (4/3) r^(-9/4): %s; min <= geometric mean: %s"
          % (i1, i2, i3, tr, mm), flush=True)
    return i1 and i2 and i3 and tr and mm


def e6(control=False):
    Gl, Ga, Ha, Hw, Ql, Qa = sp.symbols('G_lam G_app H_app H_w Q_lam Q_app')
    ricH_lam = -sp.Rational(1, 2)*Gl*(Ha + Hw) + Ql
    ricH_app = -sp.Rational(1, 2)*Ga*Ha + Qa
    sgn = -1 if control else 1
    rhs = -ricH_app + sgn*sp.Rational(1, 2)*(Gl - Ga)*Ha - (Ql - Qa)
    lhs = -sp.Rational(1, 2)*Gl*Hw
    ok = sp.simplify(lhs - rhs - ricH_lam) == 0
    if not control:
        print("  E6 -(1/2) G(g_lam) H(w) = -Ric^H(g_app) + (1/2)(G(g_lam) - G(g_app)) H(g_app) - (Q(g_lam) - Q(g_app)),"
              " given Ric^H(g_lam) = 0: %s" % ok, flush=True)
    return ok


def main():
    ok = True
    for name, f in (("E1", e1), ("E2", e2), ("E3", e3), ("E4", e4), ("E5", e5), ("E6", e6)):
        good = f()
        ctl = f(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    print("layernull5: %s" % ("all checks pass, every control fails" if ok else "FAILURES"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
