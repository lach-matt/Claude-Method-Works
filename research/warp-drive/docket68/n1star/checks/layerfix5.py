#!/usr/bin/env python3
"""layerfix5.py -- the repairs that the independent verifier of rounds 1-2 asked for (EQUALITY5-LAYER.md, Round 3,
R3.1), each with a control that must fail.

  F1 (exact integers) Lemma L.3's derivative costs with the data/energy step made explicit: the energy of d^i m_m on
     Omega_v needs the stage-m slice data at order i + 1 (D(m, i) = i + max(2m, D(m - 1, 2)), D(1, i) = i + 2), so
     c_mean(j, i) = i + 2j + 1 (not i + 2j), c_osc(j, i) = i + 2j - 2 (unchanged), c_delta(j, i) <= i + 2j + 1, the
     residual c_res(i) = i + 2N + 3 and the correction's data c_U(j) = j + 2N + 3; every cost Lemmas L.2 (a), L.3, L.4
     use (i <= 4, j <= 3) is at most 2N + 6 <= M* = 2N + 8, for N = 3, ..., 40.  Controls: without the data step the
     closed form c_mean = i + 2j + 1 fails; a stage source with three derivatives exceeds 2N + 8.
  F2 (exact) The horizon coefficient nu(r0) (round 1's K, renamed) depends on the convention of Pol^+: with the
     Frobenius product in a Euclidean frame of the Cartesian (tau, x) (the supplement's Lemma 6.2 (i)) it is (0.2),
     -mu0^(-7/4) (2 rho^3 - 3 rho^2 - 2)^2/(36 rho^6); with the frame of (v, x) it is -mu0^(-7/4) (rho^3 - 1)^2/(9
     rho^6), which vanishes only at rho = 1 (the horizon itself, outside the admissible rho > 1 + mu0^(-1/2)); both tend
     to -mu0^(-7/4)/9.  Control: the claim that the two conventions give the same nu fails.
  F3 (exact; mutations of the computed paths, replacing the four tautological controls the verifier named)
     (a) N5: nu from the horizon transport with the mass term of H2's vth factor beta dropped no longer equals (0.2);
     (b) N6: the closed form d^F = sqrt2 P(zeta)/(1 + zeta^2)^(5/2), checked at 7 angles against div div T computed
         from the record's quadrature, fails when P's coefficient 38/3 is mutated to 37/3;
     (c) P3: nu_inf from the transport from infinity with the vv mass coupling halved is not -mu0^(-7/4)/9;
     (d) D4: the sharper claim sup |Y| <= (1/2) sup |Z| for the zero-mean antiderivative is refuted by the square wave,
         whose antiderivative has amplitude pi/2 (exact).
     Each check passes unmutated and fails mutated.
  F4 (exact) The parts of D3, E3, E5 that were sampled, done exactly: (x - 1)/2 - (sqrt x - 1) and (x - 1)/4 - (x^(1/4)
     - 1) have derivative >= 0 on x >= 1 (solved as inequalities); -2 s + 4 s^3 < 0 on 0 < s <= 1/2 (and on 0 < s <
     1/sqrt2); min(x, y)^2 <= x y for x, y > 0.  Controls: (x - 1)/3 fails on x >= 1; s <= 1 fails.

Labels: computed (exact: integers, sympy).  Run: python3 checks/layerfix5.py   (about half a minute; imports layerlin5)
"""
import os
import sys
import textwrap
from functools import lru_cache

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import layerlin5 as L                                                             # noqa: E402

I = sp.I


def out(msg):
    print(textwrap.fill(msg, width=121, subsequent_indent="      ", break_on_hyphens=False), flush=True)


# ------------------------------------------------------------------------------------------------------------ F1
def costs(N, data_step=True, three=False):
    def c_osc(j, i):
        if j == 1:
            return i
        return max(c_osc(j - 1, i + (3 if three else 2)), c_osc(j - 1, i + 1), i + 2)

    @lru_cache(maxsize=None)
    def D(m, i):
        """the stage-m slice data (h_m, Q_m, d_tau m_m) with i radial derivatives (L.3 (e))"""
        return i + (2 if m == 1 else max(2*m, D(m - 1, 2)))

    @lru_cache(maxsize=None)
    def c_mean(j, i):
        if j == 0:
            return -1
        c = max(c_osc(j + 1, i), i + 2*j, c_mean(j - 1, i + 2))
        return max(c, D(j, i + 1)) if data_step else c

    def c_psi(j, i):
        return c_mean(j, i + 2)

    @lru_cache(maxsize=None)
    def c_delta(j, i):
        if j == 1:
            return i
        m = j - 1
        return max(c_delta(m, i + 2), c_delta(m, i + 1), c_psi(m, i), c_mean(m, i + 2), c_osc(m, i + 2), D(m, i + 1))

    c_res = lambda i: max(c_osc(N + 1, i + 2), c_mean(N, i + 2))                 # noqa: E731
    used = [c_osc(j, i) for j in range(1, N + 2) for i in range(5)]
    used += [c_mean(j, i) for j in range(1, N + 1) for i in range(5)]
    used += [c_delta(j, i) for j in range(1, N + 1) for i in range(5)]
    used += [c_res(i) for i in range(3)] + [j + c_res(0) for j in range(4)]
    closed = all(c_osc(j, i) == i + 2*j - 2 for j in range(1, N + 2) for i in range(6))
    closed &= all(c_mean(j, i) == i + 2*j + 1 for j in range(1, N + 1) for i in range(6))
    closed &= all(c_delta(j, i) <= i + 2*j + 1 for j in range(1, N + 1) for i in range(6))
    closed &= all(c_res(i) == i + 2*N + 3 for i in range(3))
    return max(used), closed


def f1(control=False):
    if control:
        a = all(costs(N, data_step=False)[1] for N in range(3, 41))
        b = all(costs(N, three=True)[0] <= 2*N + 8 for N in range(3, 41))
        return a or b
    ok, worst = True, {}
    for N in range(3, 41):
        mx, closed = costs(N)
        ok &= closed and mx <= 2*N + 6
        worst[N] = mx
    out("  F1 closed forms c_osc = i + 2j - 2, c_mean = i + 2j + 1, c_delta <= i + 2j + 1, c_res = i + 2N + 3, and every"
        " used cost <= 2N + 6 for N in [3, 40]: %s (N = 9: largest %d <= 24 <= M* = 26)" % (ok, worst[9]))
    return ok


# ------------------------------------------------------------------------------------------------------------ F2
def pplus_frame(Jf):
    """Pol^+ = Pol^T (Pol Pol^T)^-1, transposes in the Frobenius product of the frame Jf (rows: frame covectors)"""
    Ji = Jf.inv()
    ellB = Jf*L.ellE
    GB = Jf*L.gi*Jf.T
    dvB = Ji.T*L.dvE

    def polT(psi):
        return (ellB*psi.T + psi*ellB.T)/2 - (dvB.T*psi)[0]*GB/2

    def polB(YB):
        tr = sum(GB[i, j]*YB[i, j] for i in range(5) for j in range(5))
        return sp.Matrix([sum(ellB[i]*YB[i, k] for i in range(5)) - dvB[k]*tr/2 for k in range(5)])
    VB = Ji.T*sp.Matrix([L.Vv, L.Vr, L.Vt, 0, 0])
    PP = sp.Matrix.hstack(*[polB(polT(sp.Matrix([1 if k == m else 0 for k in range(5)]))) for m in range(5)])
    ZB = polT(PP.LUsolve(VB))
    return (Jf.T*ZB*Jf).applyfunc(sp.simplify)


def nu_of(Z, mass=True, past=False, half=False):
    """the horizon value per A E d of the third profile's vv component, from the Pol^+ table Z (N3-N5's path)"""
    r, mu0, r0 = L.r, L.mu0, L.r0
    x = sp.Symbol('x', positive=True)
    cpl = sp.Rational(1, 2) if half else 1
    if past:
        Hrr = -r**sp.Rational(-7, 2)
        Hvr = -mu0/3*r**sp.Rational(-11, 2)
        hv = -sp.integrate(-2*cpl*mu0*x**-3*x**sp.Rational(3, 2)*Hvr.subs(r, x), (x, r, sp.oo))
        return sp.simplify((hv*r**sp.Rational(-3, 2)).subs(r, sp.sqrt(mu0)))
    c1 = sp.simplify(sp.diff(Z[0, 2], L.Vt))                  # vth = c1 V_th: beta(r0) = c1/r0
    beta = c1/r0 + (mu0/3*(r**-3 - r0**-3) if mass else 0)
    DXv, DXr = I*r**sp.Rational(-5, 2)*beta, I*r**sp.Rational(-7, 2)
    sub = {L.Vv: DXv.subs(r, r0), L.Vr: DXr.subs(r, r0), L.Vt: 0}
    Hvv0 = sp.simplify((I*Z[0, 0]).subs(r, r0).subs(sub))
    tr0 = sp.simplify((I*L.trace(Z)).subs(r, r0).subs(sub))
    Hvr = tr0*(r0/r)**sp.Rational(3, 2)/2 + I*DXv
    hv = r0**sp.Rational(3, 2)*Hvv0 - sp.integrate(2*cpl*mu0*x**-3*x**sp.Rational(3, 2)*Hvr.subs(r, x), (x, r0, r))
    return sp.simplify((hv*r**sp.Rational(-3, 2)).subs(r, sp.sqrt(L.mu0)))


RHO = sp.Symbol('rho', positive=True)


def in_rho(e):
    return sp.factor(sp.simplify(e.subs(L.r0, RHO*sp.sqrt(L.mu0))))


def f2(control=False):
    J_vx = sp.diag(1, 1, L.r, L.r*L.c, L.r*L.s)
    nu_tx = in_rho(nu_of(L.polplus(sp.Matrix([L.Vv, L.Vr, L.Vt, 0, 0]))[0]))
    nu_vx = in_rho(nu_of(pplus_frame(J_vx)))
    if control:
        return sp.simplify(nu_tx - nu_vx) == 0
    rec = sp.simplify(nu_tx - L.KCLOSED) == 0
    alt = sp.simplify(nu_vx + L.mu0**sp.Rational(-7, 4)*(RHO**3 - 1)**2/(9*RHO**6)) == 0
    lim = all(sp.simplify(sp.limit(e*L.mu0**sp.Rational(7, 4), RHO, sp.oo) + sp.Rational(1, 9)) == 0
              for e in (nu_tx, nu_vx))
    out("  F2 nu with the (tau, x) frame [supplement]: %s (= (0.2): %s); with the (v, x) frame: %s (= -mu0^(-7/4)"
        " (rho^3 - 1)^2/(9 rho^6): %s); both -> -mu0^(-7/4)/9: %s" % (nu_tx, rec, nu_vx, alt, lim))
    return rec and alt and lim


# ------------------------------------------------------------------------------------------------------------ F3
def f3(control=False):
    import mpmath as mp
    mp.mp.dps = 30
    Z = L.polplus(sp.Matrix([L.Vv, L.Vr, L.Vt, 0, 0]))[0]
    rec = lambda e: sp.simplify(in_rho(e) - L.KCLOSED) == 0                     # noqa: E731
    a_ok = rec(nu_of(Z)) and not rec(nu_of(Z, mass=False))
    kinf = -L.mu0**sp.Rational(-7, 4)/9
    c_ok = sp.simplify(nu_of(Z, past=True) - kinf) == 0 and sp.simplify(nu_of(Z, past=True, half=True) - kinf) != 0
    zt = sp.Symbol('zeta')
    Pz = -2*zt**5 - sp.Rational(20, 3)*zt**3 - sp.Rational(20, 3)*zt**2 - sp.Rational(38, 3)*zt + sp.Rational(4, 3)
    Pm = Pz + sp.Rational(1, 3)*zt                                    # 38/3 -> 37/3
    h = sp.sqrt(2)/sp.sqrt(1 + sp.cos(2*L.th)**2)
    aa, bb = 2*(-L.s**2*h)/3, 2*(2*L.s**2*h)/3                        # the F quadrature of N6
    dF = sp.lambdify(L.th, L.DIV2.subs({L.a: aa, L.b: bb}).doit(), 'mpmath')

    def matches(PP):
        f = sp.lambdify(zt, PP, 'mpmath')
        return all(abs(dF(t) - mp.sqrt(2)*f(mp.cos(2*t))/(1 + mp.cos(2*t)**2)**mp.mpf(2.5)) < mp.mpf(10)**-20
                   for t in [mp.pi*k/17 + mp.mpf(1)/7 for k in range(7)])
    b_ok = matches(Pz) and not matches(Pm)
    t = sp.Symbol('t', real=True)
    # square wave Z = 1 on (0, pi), -1 on (pi, 2 pi): Y = t - pi/2 on [0, pi], 3 pi/2 - t on [pi, 2 pi], mean 0
    Y1, Y2 = t - sp.pi/2, 3*sp.pi/2 - t
    mean = (sp.integrate(Y1, (t, 0, sp.pi)) + sp.integrate(Y2, (t, sp.pi, 2*sp.pi)))/(2*sp.pi)
    supY = sp.Max(*[abs(Y1.subs(t, 0)), abs(Y1.subs(t, sp.pi)), abs(Y2.subs(t, 2*sp.pi))])
    d_ok = mean == 0 and sp.simplify(supY - sp.pi/2) == 0 and (supY <= sp.Rational(1, 2)) == sp.false
    if control:
        return not (a_ok and b_ok and c_ok and d_ok)
    out("  F3 (a) nu = (0.2), and not with beta's mass term dropped: %s; (b) d^F's closed form at 7 angles, and not with"
        " 38/3 -> 37/3: %s; (c) nu_inf = -mu0^(-7/4)/9, and not with the vv coupling halved: %s; (d) square wave:"
        " mean-zero antiderivative of amplitude pi/2, refuting sup|Y| <= sup|Z|/2: %s" % (a_ok, b_ok, c_ok, d_ok))
    return a_ok and b_ok and c_ok and d_ok


# ------------------------------------------------------------------------------------------------------------ F4
def f4(control=False):
    x = sp.Symbol('x', positive=True)
    s = sp.Symbol('s', positive=True)
    dom = sp.Interval(1, sp.oo)
    den = 3 if control else 2
    f1_ = (x - 1)/den - (sp.sqrt(x) - 1)
    f2_ = (x - 1)/4 - (x**sp.Rational(1, 4) - 1)
    d1 = sp.solveset(sp.diff(f1_, x) < 0, x, dom) == sp.EmptySet and f1_.subs(x, 1) == 0
    d2 = sp.solveset(sp.diff(f2_, x) < 0, x, dom) == sp.EmptySet and f2_.subs(x, 1) == 0
    smax = 1 if control else sp.Rational(1, 2)
    e3 = sp.solveset(-2*s + 4*s**3 >= 0, s, sp.Interval.Lopen(0, smax)) == sp.EmptySet
    e3b = sp.solveset(-2*s + 4*s**3 >= 0, s, sp.Interval.open(0, 1/sp.sqrt(2))) == sp.EmptySet
    y = sp.Symbol('y', positive=True)
    e5 = sp.simplify(x*y - sp.Min(x, y)**2).is_nonnegative is not False and \
        sp.simplify((x*y - x**2).subs(y, x + s)) == sp.expand(x*s) and sp.simplify((x*y - y**2).subs(x, y + s)) == y*s
    if control:
        return d1 or e3
    out("  F4 D3: derivatives >= 0 on x >= 1 (no solution of < 0): %s, %s; E3: -2 s + 4 s^3 < 0 on (0, 1/2] and on (0,"
        " 1/sqrt2): %s, %s; E5: x y - min(x, y)^2 = min * (max - min) >= 0: %s" % (d1, d2, e3, e3b, e5))
    return d1 and d2 and e3 and e3b and e5


def main():
    ok = True
    for name, f in (("F1", f1), ("F2", f2), ("F3", f3), ("F4", f4)):
        good = f()
        ctl = f(control=True)
        out("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""))
        ok &= good and not ctl
    out("layerfix5: %s" % ("all checks pass, every control fails" if ok else "FAILURES"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
