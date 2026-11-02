#!/usr/bin/env python3
"""layerpast5.py -- the term linear in the wave at x_K = 1 for Theorem 2's solution (data at past null infinity):
EQUALITY5-LAYER.md round 2, section R2.7 (open item O3 of round 1).

Theorem 2 (supplement section 9, Theorem P) solves every stage of the approximant with nothing coming in from past
null infinity (supplement Lemma 9.7 (d): the transport solution with r^(3/2) Z -> 0 along every generator, Cartesian
components).  Its first-degree profiles are therefore not those of round 1's N3-N5 (data i Pol^+(D_X H_j) on Sigma_tau0
at r0 = v - tau0) but the transport solutions from infinity.  This program computes them directly, with the operators of
layerlin5.py (imported, not copied: T, R_X, D_X, Pol, the free functions a(th), b(th), E(v)).

  P1 (exact) H2inf := the r0 -> infinity form of layerlin5's H2: rth = i A E tau r^(-3/2), vth = i A E tau (mu0/3)
     r^(-7/2), AB = -i r^(1/2) int_infinity^r s^(-1/2) R_X(H1)_AB ds, vv = vr = rr = 0.  It solves T(H2inf) + R_X(H1) = 0
     in all fifteen components, it is in S (vv = vr = rr = 0, sigma^AB H_AB = 0), it satisfies i Pol(H2inf) + D_X H1 = 0
     in all five, and r^(3/2) |H2inf|_cart -> 0 in every component (|.|_cart: an angular index costs a factor r).
     Control: H2inf without its vth component violates the vth transport.
  P2 (exact) Uniqueness: the homogeneous transport T(h) = 0 in the scalar sector (rr, vr, vv), the vector sector (rth,
     vth) and the tangential sector has, in every sector, solutions with r^(3/2) |h|_cart -> a nonzero constant times the
     free constant, so the condition "nothing coming in" fixes the solution.  Control: H2 with finite r0 (round 1's N3,
     data at r0 = 3 sqrt(mu0)) violates the decay condition in its vth component.
  P3 (exact) D_X H2inf = i A E d (r^(-5/2) beta_inf, r^(-7/2), *, 0, 0), beta_inf = (mu0/3) r^-3, d = div div T;
     R_X(H2inf)_vv = 0, tr R_X(H2inf) = 0.  The scalar sector of H3 with nothing coming in: tr = 0 (r^(3/2) tr is constant
     along ell), rr = -A E d r^(-7/2), vr = -(mu0/3) A E d r^(-11/2), vv = -(mu0^2/9) A E d r^(-15/2), which solve T(H3) +
     R_X(H2inf) = 0 in vv, vr, rr and trace, decay (r^(3/2) |.|_cart -> 0), and satisfy i Pol(H3) + D_X H2inf = 0 in v
     and r.  At the horizon: H3_vv(sqrt mu0) = A E d Kinf, Kinf = -mu0^(-7/4)/9, the r0 -> infinity limit of round 1's
     K(r0) (N5), now obtained without that limit.  Control: the vv transport without the mass coupling 2 mu0 H_vr/r^3
     gives H3_vv = 0 with nothing coming in (no signal).

Labels: computed (exact, sympy).  The identification of these profiles with the first-degree part of Theorem A_P's
approximant is deduced in the note (Lemma L.2_P), not computed here.
Run: python3 checks/layerpast5.py   (about five minutes; imports layerlin5.py)
"""
import os
import sys
import time

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import layerlin5 as L  # noqa: E402

T0 = time.time()
r, v, th, mu0, lam, A, I, n = L.r, L.v, L.th, L.mu0, L.lam, L.A, L.I, L.n
E, q, F, c, s = L.E, L.q, L.F, L.c, L.s
TAU, DIV2 = L.TAU, L.DIV2
WGT = [0, 0, 1, 1, 1]                          # angular indices: a factor r in the Cartesian size
BETA_INF = mu0/3*r**-3


def rint_inf(expr, hi, var):
    """int_infinity^hi of a Laurent polynomial in var^(1/2), termwise; a divergent term is refused"""
    e = sp.expand(expr.subs(var, q**2)*2*q)
    P = sp.Poly(sp.expand(e*q**60), q)
    out = 0
    for (k,), co in P.terms():
        p = k - 60
        if p >= -1:
            raise ValueError('divergent or logarithmic at infinity (power %d)' % p)
        out += co*sp.sqrt(hi)**(p + 1)/(p + 1)
    return sp.expand(out)


def lead_power(expr):
    """the largest power of r (half-integers allowed) in a Laurent polynomial in r^(1/2) with nonzero coefficient"""
    e = sp.expand(sp.expand(expr).subs(r, q**2))
    if e == 0:
        return None
    P = sp.Poly(sp.expand(e*q**80), q)
    best = None
    for (k,), co in P.terms():
        if L.is_zero(co):
            continue
        p = sp.Rational(k - 80, 2)
        best = p if best is None or p > best else best
    return best


def decays(H):
    """r^(3/2) |H_ij|_cart -> 0 for every component: the leading power of r^(3/2) H_ij / r^(w_i + w_j) is negative"""
    out = {}
    for i in range(n):
        for j in range(i, n):
            if H[i, j] == 0:
                continue
            p = lead_power(r**sp.Rational(3, 2)*H[i, j]/r**(WGT[i] + WGT[j]))
            out[(i, j)] = p
    return all(p is None or p < 0 for p in out.values()), out


STATE = {}


def p1(control=False):
    if control:
        # H2inf without its vth component (no mass-driven vth): the vth transport fails
        H2m = STATE['H2'].copy()
        H2m[0, 2] = H2m[2, 0] = 0
        return L.is_zero(L.T_tab(H2m)[0, 2] + STATE['RX1'][0, 2])
    T = sp.diag(0, 0, -(L.a + L.b), c**2*L.a, s**2*L.b)
    H1 = A*E*sp.sqrt(r)*T
    R1, D1 = L.ops(H1)
    RX1 = R1.applyfunc(lambda e: sp.expand(e).coeff(lam, 0))
    DX1 = D1.applyfunc(lambda e: sp.expand(e).coeff(lam, 0))
    H2 = sp.zeros(n)
    H2[1, 2] = H2[2, 1] = I*A*E*TAU*r**sp.Rational(-3, 2)
    H2[0, 2] = H2[2, 0] = I*A*E*TAU*BETA_INF/sp.sqrt(r)
    sR = sp.Symbol('sR', positive=True)
    for k in (2, 3, 4):
        H2[k, k] = -I*sp.sqrt(r)*rint_inf(RX1[k, k].subs(r, sR)/sp.sqrt(sR), r, sR)
    Tt = L.T_tab(H2)
    eqR = all(L.is_zero(Tt[i, j] + RX1[i, j]) for i in range(n) for j in range(i, n))
    pt = L.pol_tab(H2)
    eqD = all(L.is_zero(I*pt[k] + DX1[k]) for k in range(n))
    inS = all(H2[i, j] == 0 for (i, j) in ((0, 0), (0, 1), (1, 1))) and L.is_zero(L.tr_sigma(H2))
    dec, pw = decays(H2)
    STATE.update(H2=H2, RX1=RX1)
    print("  P1 H2inf: T(H2inf) + R_X(H1) = 0 (15): %s; i Pol(H2inf) + D_X H1 = 0 (5): %s; in S: %s; r^(3/2)|H|_cart"
          " -> 0: %s (leading powers %s)  [%.0f s]" % (eqR, eqD, inS, dec, {k: str(p) for k, p in pw.items()},
                                                     time.time() - T0), flush=True)
    return eqR and eqD and inS and dec


def p2(control=False):
    if control:
        # round 1's H2 with data at r0 = 3 sqrt(mu0): its vth component carries the incoming r^(-1/2) solution
        r0v = 3*sp.sqrt(mu0)
        beta = -1/(2*r0v) + mu0/3*(r**-3 - r0v**-3)
        h = I*A*E*TAU*beta/sp.sqrt(r)
        p = lead_power(r**sp.Rational(3, 2)*h/r)
        return p is not None and p < 0
    cc = sp.symbols('c1:7')
    hr = sp.Function('h')
    res = []
    # scalar sector: rr, then vr (driven by rr), then vv (driven by vr)
    hrr = cc[0]*r**sp.Rational(-3, 2)
    sol_vr = sp.dsolve(sp.diff(hr(r), r) + 3*hr(r)/(2*r) + mu0*hrr/r**3, hr(r)).rhs.subs('C1', cc[1])
    sol_vv = sp.dsolve(sp.diff(hr(r), r) + 3*hr(r)/(2*r) + 2*mu0*sol_vr/r**3, hr(r)).rhs.subs('C1', cc[2])
    # vector sector: rth, then vth (driven by rth)
    hrt = cc[3]*r**sp.Rational(-1, 2)
    sol_vt = sp.dsolve(sp.diff(hr(r), r) + hr(r)/(2*r) + mu0*hrt/r**3, hr(r)).rhs.subs('C1', cc[4])
    # tangential: (d_r - 1/(2r)) H_AB = 0
    hab = cc[5]*sp.sqrt(r)
    for expr, w, const in ((hrr, 0, cc[0]), (sol_vr, 0, cc[1]), (sol_vv, 0, cc[2]), (hrt, 1, cc[3]),
                           (sol_vt, 1, cc[4]), (hab, 2, cc[5])):
        lim = sp.limit(r**sp.Rational(3, 2)*expr/r**w, r, sp.oo)
        res.append(sp.simplify(lim - const) == 0)
    ok = all(res)
    print("  P2 homogeneous solutions of T: r^(3/2)|h|_cart -> its free constant in rr, vr, vv, rth, vth, AB: %s"
          % res, flush=True)
    return ok


def p3(control=False):
    if control:
        H3 = STATE['H3']
        # the vv transport without the mass coupling: (d_r + 3/(2r)) H_vv = 0, nothing coming in: the integral of 0
        sR = sp.Symbol('sR', positive=True)
        hvv = rint_inf(sp.S(0)*sR, r, sR)*r**sp.Rational(-3, 2)
        return L.is_zero(sp.expand(hvv).subs(r, sp.sqrt(mu0)) - STATE['Kinf_val'])
    H2 = STATE['H2']
    R2, D2 = L.ops(H2)
    RX2 = R2.applyfunc(lambda e: sp.expand(e).coeff(lam, 0))
    DX2 = D2.applyfunc(lambda e: sp.expand(e).coeff(lam, 0))
    dv_ = L.is_zero(DX2[0] - I*A*E*DIV2*r**sp.Rational(-5, 2)*BETA_INF)
    dr_ = L.is_zero(DX2[1] - I*A*E*DIV2*r**sp.Rational(-7, 2))
    rvv, rtr = L.is_zero(RX2[0, 0]), L.is_zero(L.trace(RX2))
    H3 = sp.zeros(n)
    H3[1, 1] = -A*E*DIV2*r**sp.Rational(-7, 2)
    H3[0, 1] = H3[1, 0] = -mu0/3*A*E*DIV2*r**sp.Rational(-11, 2)
    phi = (0 - 2*H3[0, 1] - F*H3[1, 1])/3                      # trace zero: the angular trace part
    H3[2, 2], H3[3, 3], H3[4, 4] = phi*r**2, phi*r**2*c**2, phi*r**2*s**2
    sR = sp.Symbol('sR', positive=True)
    H3[0, 0] = rint_inf((-(2*mu0/r**3)*r**sp.Rational(3, 2)*H3[0, 1]).subs(r, sR), r, sR)*r**sp.Rational(-3, 2)
    closed = L.is_zero(H3[0, 0] + mu0**2/9*A*E*DIV2*r**sp.Rational(-15, 2))
    Tt = L.T_tab(H3)
    eqs = [L.is_zero(Tt[i, j] + RX2[i, j]) for (i, j) in ((0, 0), (0, 1), (1, 1))]
    eqtr = L.is_zero(L.trace(Tt)) and L.is_zero(L.trace(H3))
    pt = L.pol_tab(H3)
    eqD = [L.is_zero(I*pt[k] + DX2[k]) for k in (0, 1)]
    sc = sp.zeros(n)
    for (i, j) in ((0, 0), (0, 1), (1, 1)):
        sc[i, j] = sc[j, i] = H3[i, j]
    dec, pw = decays(sc)
    val = sp.simplify(H3[0, 0].subs(r, sp.sqrt(mu0))/(A*E*DIV2))
    kinf = sp.simplify(val + mu0**sp.Rational(-7, 4)/9) == 0
    STATE.update(H3=H3, Kinf_val=sp.expand(H3[0, 0].subs(r, sp.sqrt(mu0))))
    print("  P3 D_X H2inf = i A E d (r^-5/2 beta_inf, r^-7/2): %s, %s; R_X(H2inf) vv = 0: %s, trace 0: %s;"
          " H3 scalar sector: vv = -(mu0^2/9) A E d r^(-15/2): %s; T(H3) + R_X(H2inf) = 0 in vv, vr, rr: %s, trace: %s;"
          " i Pol(H3) + D_X H2inf = 0 in v, r: %s; decays: %s %s; H3_vv(sqrt mu0)/(A E d) = %s, = -mu0^(-7/4)/9: %s"
          "  [%.0f s]" % (dv_, dr_, rvv, rtr, closed, eqs, eqtr, eqD, dec, {k: str(p) for k, p in pw.items()}, val,
                          kinf, time.time() - T0), flush=True)
    return dv_ and dr_ and rvv and rtr and closed and all(eqs) and eqtr and all(eqD) and dec and kinf


def main():
    ok = True
    g = p1()
    ctl = p1(control=True)
    print("P1 %s%s" % ("PASS" if g and not ctl else "FAIL", " (control passed)" if ctl else ""), flush=True)
    ok &= g and not ctl
    g, ctl = p2(), p2(control=True)
    print("P2 %s%s" % ("PASS" if g and not ctl else "FAIL", " (control passed)" if ctl else ""), flush=True)
    ok &= g and not ctl
    g = p3()
    ctl = p3(control=True)
    print("P3 %s%s" % ("PASS" if g and not ctl else "FAIL", " (control passed)" if ctl else ""), flush=True)
    ok &= g and not ctl
    print("layerpast5: %s  [%.0f s]" % ("all checks pass, every control fails" if ok else "FAILURES", time.time() - T0))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
