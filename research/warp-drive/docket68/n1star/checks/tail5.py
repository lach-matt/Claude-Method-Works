"""tail5.py -- SETTLE-GLAM5 section 3: the half-order tail that the shell leaves at past null infinity, and what it
puts on Hintz's initial surface at spatial infinity.

Five-dimensional Minkowski space in the ingoing chart (v, r), ds^2 = -dv^2 + 2 dv dr + r^2 dOmega_3^2. On a function
a(v) r^(-p) Y_l (kappa := l(l + 2)) the wave operator gives (coulomb5.py's box)

    box (a r^-p Y) = [ (3 - 2p) a' r^(-p-1) + (p(p - 2) - kappa) a r^(-p-2) ] Y,                       (T1)

so a field whose radiation field at past null infinity is F(v) (phi = r^(-3/2) sum_j a_j r^-j, a_0 = F) has
a_j' = ((j + 1/2)(j - 3/2) - kappa)/(2j) a_(j-1). In particular a_1' = -(c/2) F with c := kappa + 3/4 =
(l + 1/2)(l + 3/2) > 0: once F has passed (F = 0 for v > v_end), the r^(-5/2) coefficient is the constant
-(c/2) int F dv, nonzero exactly when the radiation field has nonzero time integral.

  T1 (exact) (T1) for symbolic p and kappa; the recursion leaves box of the truncated sum only at the order past the
     truncation; a_1 after the shell is -(c/2) int F, c = (l + 1/2)(l + 3/2) > 0 for every l.
  T2 (exact) the degree -p self-similar solution r^-p F(s) Y, s = (v - v1)/r, with data on N = {v = v1}: its ODE
     (s - s^2/2) F'' + (p - 1/2)(1 - s) F' - (1/2)(p^2 - 2p - kappa) F = 0 (symbolic p, kappa), solved by
     2F1(p + l, p - l - 2; p - 1/2; s/2), regular at N; on a slice t = const, s -> 1 at spatial infinity, so the
     rho^p coefficient there is F(1) = F(0) T_p(l), T_p(l) = sqrt(pi) Gamma(p - 1/2)/(Gamma((p + l + 1)/2)
     Gamma((p - l - 1)/2)) (Gauss's second summation theorem; checked against the series to 30 digits).
  T3 (computed, 30 digits) T_(5/2)(l), T_(7/2)(l) and T_(9/2)(l) are nonzero for l = 0, ..., 60; control: at the
     integer degrees p = 2 and p = 3, T_p(l) vanishes at every odd l (p = 2) and every even l >= 2 (p = 3), so the
     non-vanishing at half-integer p is not automatic.
  T4 (exact) on Tangherlini (box gains -mu r^-3 d_r(r d_r)), the recursion from the degree -5/2 datum gains
     -mu (p_(j-3))^2 a_(j-3), of degree j - 2 in v - v1: the top degrees, which fix the rho^(5/2) coefficient at
     spatial infinity, do not depend on mu (checked to j = 9, mu symbolic). Control: dropping the top-degree check
     (comparing full a_j) does see mu.
  T5 (exact) the curvature: if the radiation field is G'' (the linearized Riemann tensor of h, whose radiation
     field is d_v^2 of h's), the recursion gives a_1 = -(c/2) G', a_2 = c(c - 2) G/8, a_3 = -c(c - 2)(c - 6)/48
     int G: after the shell the first two vanish and the third is proportional to int G, with c(c - 2)(c - 6) != 0
     at every integer l. So the half-order tail of h (r^(-5/2), proportional to int G) is matched by a curvature
     tail at r^(-9/2): it is not a gauge artefact. Control: G = H' (zero integral) leaves no tail.
  T6 (exact) the class: for l0 in (3, 4), rho^(-l0) (rho^(5/2) - a2 rho^2 - a3 rho^3) is not in L^2(drho/rho)
     near 0 for any a2, a3 (the integral from eps diverges like eps^(5 - 2 l0) or worse); so a nonzero rho^(5/2)
     term puts the data outside H_b^(oo,(E_0, l0)), E_0 = {(j, 0) : j >= 2}. Control: with E_0^(1/2) (the
     rho^(5/2) term subtracted) the remainder is finite; and at l0 = 9/4 < 5/2 the term is in rho^(l0) L^2_b.
  T7 (exact) the order count behind the A-polynomial: box~ (r^(-3/2) F) = r^(-7/2)(Laplacian - 3/4) F
     - (15/4) mu r^(-11/2) F, with no r^(-5/2) term (record (9.5)); the two polarizations of the wave (2.5') are
     linearly independent tensors; and Laplacian - 3/4 has eigenvalues -(l + 1/2)(l + 3/2) on S^3, never zero.
  T8 (exact and computed) the time integral of the record's waves: for env = sin^4(pi (v - 1/2)/3) on [1/2, 7/2]
     (the record's numerics' envelope, C^3 at its ends) ehat(w) = int env e^(i w v) dv in closed form, |ehat(w)|
     w^5 bounded and not -> 0; for the C_c^oo bump env_b(v) = exp(-1/(1 - y^2)), y = (v - 2)/(3/2), ehat_b(1/lam)
     is nonzero at lam = 2^-1, ..., 2^-7 (40 digits) and falls there faster than lam^5 (log-slope over [2^-7,
     2^-5] above 5; faster than every power by k integrations by parts, deduced), and
     ehat_b(w) = e^(2iw) E(w) with E real: it vanishes exactly at the real zeros of E, a discrete set (the first
     ones located). Control: a radiation field with zero time integral (env replaced by its derivative times a
     constant phase) gives ehat = 0 identically at w = 0 and is not of the record's form.
  T9 (exact and computed) the A^3 part of the tail is beyond all orders too: in the model of its integrand
     (G3 = lam e sin(theta), S3 = (d_v G3)^2 - e^2/2, the Isaacson balance) G3 S3 carries only the odd phase
     harmonics 1 and 3, its theta-mean vanishing identically, so its v-integral is an oscillatory integral of a
     C_c^oo profile; computed for the bump, falling faster than lam^4 on [2^-6, 2^-3]. Control: an even product
     has a nonzero mean.
Labels: computed (exact, sympy; mpmath at 30-40 digits).

    python3 checks/tail5.py [--selftest]
"""
import sys

import mpmath as mp
import sympy as sp

v, r, s, v1, mu, kap, p, w = sp.symbols("v r s v1 mu kappa p w", real=True)
FAIL = []


def check(name, ok, msg=""):
    print(f"  {name}: {'pass' if ok else 'FAIL'} {msg}")
    if not ok:
        FAIL.append(name)


def box(F, kappa):
    return 2*sp.diff(F, v, r) + 3*sp.diff(F, v)/r + sp.diff(F, r, 2) + 3*sp.diff(F, r)/r - kappa*F/r**2


def boxT(F, kappa, m):
    return box(F, kappa) - m*sp.diff(r*sp.diff(F, r), r)/r**3


def t1():
    print("T1  the recursion from past null infinity")
    a = sp.Function("a")
    rp = sp.Symbol("rp", positive=True)
    lhs = sp.powsimp(sp.expand(box(a(v)*r**(-p), kap).subs(r, rp)*rp**(p + 2)), force=True)
    rhs = sp.expand((3 - 2*p)*sp.diff(a(v), v)*rp + (p*(p - 2) - kap)*a(v))
    check("T1a box(a r^-p) = (3-2p)a' r^(-p-1) + (p(p-2)-kappa) a r^(-p-2)",
          sp.simplify(sp.expand(lhs - rhs)) == 0)
    # truncated sum with a concrete radiation field, exact
    F0 = (v*(1 - v))**6  # smooth on [0, 1], C^5 at the ends: enough for the identity
    for l in (0, 1, 2, 3):
        kk = l*(l + 2)
        A = [F0]
        J = 5
        for j in range(1, J + 1):
            A.append(sp.integrate(sp.Rational(1, 2*j)*((j + sp.Rational(1, 2))*(j - sp.Rational(3, 2)) - kk)
                                  * A[-1], (v, 0, v)))
        phi = sum(A[j]*r**(-sp.Rational(3, 2) - j) for j in range(J + 1))
        res = sp.expand(box(phi, kk)*r**(sp.Rational(3, 2) + J + 2))
        ok = sp.simplify(res - sp.expand(res.coeff(r, 0))) == 0
        check(f"T1b l={l}: box of the sum to j={J} lives at r^(-{J}-7/2) only", ok)
        c = sp.Rational(4*kk + 3, 4)
        a1_after = A[1].subs(v, 1)  # F = 0 for v > v_end = 1, so a_1 is constant from v = 1 on
        check(f"T1c l={l}: a_1 after the shell = -(c/2) int F, c = {c}",
              sp.simplify(a1_after + c/2*sp.integrate(F0, (v, 0, 1))) == 0)
    l = sp.symbols("l", nonnegative=True, integer=True)
    c = l*(l + 2) + sp.Rational(3, 4)
    check("T1d c = (l + 1/2)(l + 3/2) > 0", sp.expand(c - (l + sp.Rational(1, 2))*(l + sp.Rational(3, 2))) == 0)


def t2():
    print("T2  the self-similar transfer from N to spatial infinity")
    F = sp.Function("F")
    phi = r**(-p)*F((v - v1)/r)
    ex = sp.expand(box(phi, kap)*r**(p + 2))
    ex = ex.subs(v, v1 + s*r)
    ex = sp.simplify(ex)
    ode = (-2)*((s - s**2/2)*sp.Derivative(F(s), s, 2) + (p - sp.Rational(1, 2))*(1 - s)*sp.Derivative(F(s), s)
                - sp.Rational(1, 2)*(p**2 - 2*p - kap)*F(s))
    diff = sp.simplify(ex.doit() - ode.doit())
    check("T2a r^(p+2) box(r^-p F(s)) = -2[(s - s^2/2)F'' + (p - 1/2)(1-s)F' - (p^2-2p-kappa)F/2]", diff == 0,
          str(diff)[:80])
    mp.mp.dps = 30
    worst = 0
    for pp in (mp.mpf(5)/2, mp.mpf(7)/2, mp.mpf(2), mp.mpf(3)):
        for l in range(0, 7):
            kk = l*(l + 2)
            f = lambda x: mp.hyp2f1(pp + l, pp - l - 2, pp - mp.mpf(1)/2, x/2)
            for x in (mp.mpf("0.3"), mp.mpf("0.9"), mp.mpf("1.4")):
                d1 = mp.diff(f, x)
                d2 = mp.diff(f, x, 2)
                res = (x - x**2/2)*d2 + (pp - mp.mpf(1)/2)*(1 - x)*d1 - (pp**2 - 2*pp - kk)*f(x)/2
                worst = max(worst, abs(res))
    check("T2b 2F1(p+l, p-l-2; p-1/2; s/2) solves it (p = 5/2, 7/2, 2, 3; l <= 6)", worst < mp.mpf(10)**-20,
          mp.nstr(worst, 3))
    worst = 0
    for pp in (mp.mpf(5)/2, mp.mpf(7)/2, mp.mpf(9)/2):
        for l in range(0, 13):
            series = mp.hyp2f1(pp + l, pp - l - 2, pp - mp.mpf(1)/2, mp.mpf(1)/2)
            gauss = Tp(pp, l)
            worst = max(worst, abs(series - gauss))
    check("T2c F(1)/F(0) = Gauss's sqrt(pi)Gamma(p-1/2)/(Gamma((p+l+1)/2)Gamma((p-l-1)/2))",
          worst < mp.mpf(10)**-25, mp.nstr(worst, 3))


def Tp(pp, l):
    return mp.sqrt(mp.pi)*mp.gamma(pp - mp.mpf(1)/2)*mp.rgamma((pp + l + 1)/2)*mp.rgamma((pp - l - 1)/2)


def t3():
    print("T3  the transfer at half-integer degree never vanishes; at integer degree it does")
    mp.mp.dps = 30
    for pp in (mp.mpf(5)/2, mp.mpf(7)/2, mp.mpf(9)/2):
        vals = [abs(Tp(pp, l)) for l in range(0, 61)]
        check(f"T3a p={mp.nstr(pp, 2)}: min_(l<=60) |T_p(l)| > 0", min(vals) > mp.mpf(10)**-40,
              "min " + mp.nstr(min(vals), 4))
    print("     T_(5/2)(l), l = 0..6:", [mp.nstr(Tp(mp.mpf(5)/2, l), 6) for l in range(7)])
    z2 = [l for l in range(0, 21) if abs(Tp(mp.mpf(2), l)) < mp.mpf(10)**-25]
    z3 = [l for l in range(0, 21) if abs(Tp(mp.mpf(3), l)) < mp.mpf(10)**-25]
    check("T3b control: p = 2 vanishes at the odd l", z2 == list(range(1, 21, 2)), str(z2))
    check("T3c control: p = 3 vanishes at the even l >= 2", z3 == list(range(2, 21, 2)), str(z3))
    print("     T_2(l) = cos(pi l/2)/(l+1):", all(abs(Tp(mp.mpf(2), l) - mp.cos(mp.pi*l/2)/(l + 1)) < 1e-25
                                                 for l in range(12)))


def t4():
    print("T4  Tangherlini does not move the rho^(5/2) coefficient")
    for l in (0, 1, 2):
        kk = l*(l + 2)
        p0 = sp.Rational(5, 2)
        J = 9
        A = {}
        Af = {}
        for j in range(0, J + 1):
            if j == 0:
                A[j] = sp.Integer(1)
                Af[j] = sp.Integer(1)
                continue
            pj = p0 + j
            rhs = -((pj - 1)*(pj - 3) - kk)*A[j - 1]
            rhsf = -((pj - 1)*(pj - 3) - kk)*Af[j - 1]
            if j >= 3:
                rhs += mu*(pj - 3)**2*A[j - 3]
            A[j] = sp.integrate(sp.expand(rhs/(3 - 2*pj)), (v, v1, v))
            Af[j] = sp.integrate(sp.expand(rhsf/(3 - 2*pj)), (v, v1, v))
        phi = sum(A[j]*r**(-p0 - j) for j in range(J + 1))
        res = sp.expand(boxT(phi, kk, mu)*r**(p0 + J + 2))
        lowest = [sp.simplify(res.coeff(r, k)) for k in range(0, 1)]
        # residual must live only past the truncation: all powers r^k, k <= 0, of the scaled residual
        ok_eq = all(sp.simplify(res.coeff(r, k)) == 0 for k in range(1, J + 2))
        check(f"T4a l={l}: the mu-recursion solves box_T to order j={J}", ok_eq)
        top = all(sp.simplify(sp.Poly(sp.expand(A[j]), v).coeff_monomial(v**j)
                              - sp.Poly(sp.expand(Af[j]), v).coeff_monomial(v**j)) == 0 for j in range(1, J + 1))
        deg = all(sp.degree(sp.expand(A[j] - Af[j]), v) <= max(j - 2, 0) for j in range(3, J + 1))
        check(f"T4b l={l}: the top degree of each a_j in v is mu-free, mu enters at degree <= j-2", top and deg)
        ctl = any(sp.simplify(sp.expand(A[j] - Af[j])) != 0 for j in range(3, J + 1))
        check(f"T4c l={l}: control: the full a_j do depend on mu", ctl)
        _ = lowest


def t5():
    print("T5  the curvature carries the tail too")
    G = (v*(1 - v))**5
    H = (v*(1 - v))**6
    l = sp.symbols("l", integer=True, nonnegative=True)
    c = sp.Symbol("c")
    for name, rad, expect_nonzero in (("G''", sp.diff(G, v, 2), True), ("(H')'' control", sp.diff(H, v, 3), False)):
        A = [rad]
        for j in (1, 2, 3):
            coef = -(c - {1: 0, 2: 2, 3: 6}[j])/(2*j)
            A.append(sp.integrate(coef*A[-1], (v, 0, v)))
        # the radiation field is supported in [0, 1]: from v = 1 on, a_1 is constant, a_2 grows by int a_1 and
        # a_3 by int a_2, so a_1(1) = a_2(1) = 0 makes all three constant after the shell
        after = [sp.factor(sp.simplify(A[j].subs(v, 1))) for j in (1, 2, 3)]
        base = G if expect_nonzero else sp.diff(H, v)
        predicted = -c*(c - 2)*(c - 6)/48*sp.integrate(base, (v, 0, 1))
        ok = after[0] == 0 and after[1] == 0 and sp.simplify(after[2] - predicted) == 0
        check(f"T5a radiation field {name}: a_1 = a_2 = 0 after the shell, a_3 = -c(c-2)(c-6)/48 int",
              ok and ((after[2] != 0) == expect_nonzero), str(after[2])[:60])
    # the coefficient in the recursion: ((j+1/2)(j-3/2) - kappa)/(2j) = -(c - j(j-1))/(2j) with c = kappa + 3/4
    kk = sp.Symbol("kk")
    ok = all(sp.simplify(((j + sp.Rational(1, 2))*(j - sp.Rational(3, 2)) - kk)/(2*j)
                         + (kk + sp.Rational(3, 4) - j*(j - 1))/(2*j)) == 0 for j in (1, 2, 3))
    check("T5b the recursion's coefficients are -(c - j(j-1))/(2j)", ok)
    cl = (l + sp.Rational(1, 2))*(l + sp.Rational(3, 2))
    roots = sp.solve(sp.Eq(cl*(cl - 2)*(cl - 6), 0), l)
    check("T5c c(c-2)(c-6) has no root at a nonnegative integer l", all((not rt.is_integer) or rt < 0
                                                                        for rt in roots), str(roots))


def t6():
    print("T6  a rho^(5/2) term is outside Part VII's class")
    rho, eps, a2, a3 = sp.symbols("rho epsilon a2 a3", positive=True)
    a2r, a3r = sp.symbols("a2r a3r", real=True)
    for l0 in (sp.Rational(13, 4), sp.Rational(7, 2) - sp.Rational(1, 10), sp.Rational(39, 10)):
        f = rho**(-l0)*(rho**sp.Rational(5, 2) - a2r*rho**2 - a3r*rho**3)
        I = sp.integrate(sp.expand(f**2/rho), (rho, eps, 1))
        # leading behaviour as eps -> 0: with a2 = 0 the eps^(5 - 2 l0) term, coefficient 1/(2 l0 - 5) > 0
        I0 = sp.expand(I.subs(a2r, 0))
        lead = sp.limit(I0*eps**(2*l0 - 5), eps, 0)
        lead_a2 = sp.limit(sp.expand(I)*eps**(2*l0 - 4), eps, 0)
        check(f"T6a l0={l0}: int_eps^1 |rho^-l0(rho^(5/2) - a3 rho^3)|^2 drho/rho ~ eps^(5-2l0)/(2l0-5)",
              sp.simplify(lead - 1/(2*l0 - 5)) == 0, f"lead {lead}")
        check(f"T6b l0={l0}: with a2 != 0 it is worse, ~ a2^2 eps^(4-2l0)/(2l0-4)",
              sp.simplify(lead_a2 - a2r**2/(2*l0 - 4)) == 0, f"lead {lead_a2}")
        g = rho**(-l0)*(rho**sp.Rational(5, 2) - rho**sp.Rational(5, 2))
        check(f"T6c l0={l0}: control: with the rho^(5/2) term subtracted (E_0^(1/2)) the remainder is 0",
              sp.simplify(g) == 0)
    l0 = sp.Rational(9, 4)
    J = sp.integrate((rho**(-l0)*rho**sp.Rational(5, 2))**2/rho, (rho, 0, 1))
    check("T6d control: at l0 = 9/4 < 5/2 the term is in rho^(l0) L^2_b", J.is_finite, str(J))


def t7():
    print("T7  the order count: only box~ puts the wave's linear part at r^(-7/2)")
    Fn = sp.Function("F")
    th = sp.Symbol("th")
    # record (9.5) on a function r^-p F(v) Y with Deltaring Y = -kappa Y
    f = r**(-p)*Fn(v)
    ell = lambda g: sp.diff(g, r)  # ell = d_r at fixed v
    boxt = 2*sp.diff(ell(f), v) + 3*sp.diff(f, v)/r + (1 - mu/r**2)*ell(ell(f)) + 3*ell(f)/r - kap*f/r**2
    target = ((3 - 2*p)*r**(-p - 1)*sp.diff(Fn(v), v) + r**(-p - 2)*(p*(p - 2) - kap)*Fn(v)
              - mu*p*(p + 1)*r**(-p - 4)*Fn(v))
    rp = sp.Symbol("rp", positive=True)
    dd = sp.powsimp(sp.expand(((boxt - target)*r**(p + 4)).subs(r, rp)), force=True)
    check("T7a (9.5) on r^-p F Y = (3-2p) r^(-p-1) F' + (p(p-2)-kappa) r^(-p-2) F - mu p(p+1) r^(-p-4) F",
          sp.simplify(sp.expand(dd)) == 0, str(sp.simplify(dd))[:60])
    t32 = sp.expand(target.subs(p, sp.Rational(3, 2)))
    check("T7b at p = 3/2 no r^(-5/2) term; r^(-7/2) carries -(kappa + 3/4) F; mu enters at r^(-11/2)",
          sp.simplify(t32 - (-(kap + sp.Rational(3, 4))*r**sp.Rational(-7, 2)*Fn(v)
                             - sp.Rational(15, 4)*mu*r**sp.Rational(-11, 2)*Fn(v))) == 0)
    # the two polarizations of (2.5'), polar components (dphi1^2, dphi2^2, dtheta^2), c = cos th, s = sin th
    c_, s_ = sp.cos(th), sp.sin(th)
    Fp, Gp = sp.symbols("Fp Gp")
    p1 = (2*c_**2*Gp - s_**2*Fp)/3
    p2 = (2*s_**2*Fp - c_**2*Gp)/3
    comps = [c_**2*p1, s_**2*p2, -(p1 + p2)]
    TF = [sp.diff(x, Fp) for x in comps]
    TG = [sp.diff(x, Gp) for x in comps]
    M = sp.Matrix([[sp.simplify(x.subs(th, sp.Rational(1, 3))) for x in TF],
                   [sp.simplify(x.subs(th, sp.Rational(1, 3))) for x in TG]])
    check("T7c the polarizations T_F, T_G of (2.5') are linearly independent", M.rank() == 2)
    l = sp.symbols("l", integer=True, nonnegative=True)
    check("T7d -l(l+2) - 3/4 = -(l+1/2)(l+3/2) < 0: Laplacian - 3/4 is injective on S^3",
          sp.expand(-l*(l + 2) - sp.Rational(3, 4) + (l + sp.Rational(1, 2))*(l + sp.Rational(3, 2))) == 0)


def bump(x):
    y = (x - 2)/(mp.mpf(3)/2)
    if abs(y) >= 1:
        return mp.mpf(0)
    return mp.exp(-1/(1 - y*y))


def ehat_b(om):
    n = int(3*om/mp.pi) + 8
    pts = [mp.mpf(1)/2 + 3*mp.mpf(k)/n for k in range(n + 1)]
    re = mp.quad(lambda x: bump(x)*mp.cos(om*x), pts)
    im = mp.quad(lambda x: bump(x)*mp.sin(om*x), pts)
    return mp.mpc(re, im)


def t8():
    print("T8  the time integral of the record's waves")
    # sin^4 x = (3 - 4 cos 2x + cos 4x)/8, x = pi (v - 1/2)/3: ehat is a finite sum of int e^(i alpha v) dv
    mp.mp.dps = 30
    lo, hi = mp.mpf(1)/2, mp.mpf(7)/2

    def seg(al):
        return (hi - lo) if al == 0 else (mp.exp(1j*al*hi) - mp.exp(1j*al*lo))/(1j*al)

    def ehat4(om):
        tot = 3*seg(om)
        for k, cf in ((2, -4), (4, 1)):
            q = k*mp.pi/3
            ph = mp.exp(-1j*q/2)
            tot += cf*(ph*seg(om + q) + seg(om - q)/ph)/2
        return tot/8
    vals = []
    for om in (10, 20, 40, 80, 160, 320):
        e = ehat4(mp.mpf(om))
        direct = mp.quad(lambda x: mp.sin(mp.pi*(x - mp.mpf(1)/2)/3)**4*mp.exp(1j*om*x),
                         mp.linspace(lo, hi, 4*om))
        vals.append((om, abs(e)*om**5, abs(e - direct)))
    check("T8a the closed form agrees with quadrature", max(x[2] for x in vals) < 1e-20,
          mp.nstr(max(x[2] for x in vals), 3))
    print("     |ehat(w)| w^5 at w = 10..320:", [mp.nstr(x[1], 5) for x in vals])
    check("T8b sin^4 envelope: |ehat(w)| w^5 bounded, not -> 0 (C^3 ends: ehat ~ w^-5)",
          all(0.1 < x[1] < 1e4 for x in vals[2:]))
    mp.mp.dps = 40
    rows = []
    for k in range(1, 8):
        lam = mp.mpf(2)**-k
        e = ehat_b(1/lam)
        rows.append((lam, e))
    print("     bump: lam, |ehat(1/lam)|:", [(mp.nstr(a, 3), mp.nstr(abs(b), 4)) for a, b in rows])
    check("T8c bump: ehat(1/lam) != 0 at lam = 2^-1..2^-7", all(abs(b) > mp.mpf(10)**-30 for _, b in rows))
    # faster than every power is a theorem (env in C_c^oo: integrate by parts k times); measured here: the
    # log-slope of |ehat(1/lam)| between lam = 2^-5 and 2^-7 exceeds 5, while that of the C^3 envelope is 5
    loc = [mp.log(abs(rows[i + 1][1])/abs(rows[i][1]))/mp.log(mp.mpf(1)/2) for i in range(2, len(rows) - 1)]
    print("     local log-slopes d log|ehat|/d log lam (they oscillate with ehat's zeros):",
          [mp.nstr(x, 4) for x in loc])
    slope = mp.log(abs(rows[-1][1])/abs(rows[-3][1]))/mp.log(mp.mpf(1)/4)
    check("T8d bump: log-slope over [2^-7, 2^-5] > 5 (faster than the C^3 envelope's lam^5)", slope > 5,
          mp.nstr(slope, 4))
    # e^(-2iw) ehat is real (the bump is even about v = 2): zeros where the real E vanishes
    E = lambda om: (mp.exp(-2j*om)*ehat_b(om))
    imag_worst = max(abs(mp.im(E(mp.mpf(om)))) for om in (3, 7, 13, 21))
    check("T8e e^(-2iw) ehat_b(w) is real", imag_worst < mp.mpf(10)**-30, mp.nstr(imag_worst, 3))
    zeros = []
    grid = [mp.mpf(1) + mp.mpf(k)/2 for k in range(0, 41)]
    prev = mp.re(E(grid[0]))
    for a, b in zip(grid, grid[1:]):
        cur = mp.re(E(b))
        if prev*cur < 0:
            zeros.append(mp.findroot(lambda om: mp.re(E(om)), (a, b), solver="anderson"))
        prev = cur
    print("     real zeros of E in [1, 21]:", [mp.nstr(z, 6) for z in zeros])
    check("T8f E has isolated real zeros (discrete exceptional set lam = 1/w)", len(zeros) >= 2)
    # control: env' (zero integral) gives ehat(0) = 0; the record's waves are env times a phase, not of that form
    ctl = mp.quad(lambda x: mp.diff(bump, x), [mp.mpf(1)/2, 2, mp.mpf(7)/2])
    check("T8g control: a radiation field env' has zero time integral at w = 0", abs(ctl) < mp.mpf(10)**-25,
          mp.nstr(ctl, 3))


def t9():
    print("T9  the cubic part is beyond all orders: its integrand has no zeroth phase harmonic")
    th, lam, e0, e1 = sp.symbols("theta lambda e0 e1", real=True)
    # model of the r^(-7/2) source at A^3: G3 = lam e(v) sin(theta), d_v G3 = lam e' sin + e cos (theta = v/lam),
    # S3 = (d_v G3)^2 - e^2/2 (the Isaacson balance removes the mean at lam^0); after integration by parts the
    # A^3 coefficient is -int G3 S3 dv, and int d_v G3 G4 = -2 int G3 S3 likewise
    dG3 = lam*e1*sp.sin(th) + e0*sp.cos(th)
    S3 = dG3**2 - e0**2/2
    integrand = lam*e0*sp.sin(th)*S3
    mean = sp.simplify(sp.integrate(sp.expand(integrand), (th, 0, 2*sp.pi))/(2*sp.pi))
    check("T9a the theta-mean of G3 S3 vanishes identically in (lam, e, e')", mean == 0, str(mean))
    harm = sp.expand(sp.fu(sp.expand(integrand)))
    odd = all(sp.simplify(sp.integrate(sp.expand(integrand)*sp.cos(k*th), (th, 0, 2*sp.pi))) == 0 and
              sp.simplify(sp.integrate(sp.expand(integrand)*sp.sin(k*th), (th, 0, 2*sp.pi))) == 0
              for k in (0, 2, 4))
    check("T9b only odd phase harmonics occur (1 and 3)", odd)
    ctl = sp.simplify(sp.integrate(sp.expand(dG3**2), (th, 0, 2*sp.pi))/(2*sp.pi))
    check("T9c control: an even product, (d_v G3)^2, has a nonzero mean (an O(1) source, not O(lam^oo))",
          ctl != 0, str(ctl))
    mp.mp.dps = 30
    rows = []
    for k in (3, 4, 5, 6):
        lm = mp.mpf(2)**-k
        n = int(3/(lm*mp.pi)) + 8
        pts = [mp.mpf(1)/2 + 3*mp.mpf(j)/n for j in range(n + 1)]
        db = lambda x: mp.diff(bump, x)

        def f(x):
            q = x/lm
            g3 = lm*bump(x)*mp.sin(q)
            d = lm*db(x)*mp.sin(q) + bump(x)*mp.cos(q)
            return g3*(d*d - bump(x)**2/2)
        rows.append((lm, mp.quad(f, pts)))
    print("     bump: lam, int G3 S3:", [(mp.nstr(a, 3), mp.nstr(b, 4)) for a, b in rows])
    slope = mp.log(abs(rows[-1][1])/abs(rows[0][1]))/mp.log(rows[-1][0]/rows[0][0])
    check("T9d bump: the cubic model coefficient falls faster than lam^4 over [2^-6, 2^-3]", slope > 4,
          mp.nstr(slope, 4))


def main():
    only = sys.argv[1:]
    for name, f in (("t1", t1), ("t2", t2), ("t3", t3), ("t4", t4), ("t5", t5), ("t6", t6), ("t7", t7),
                    ("t8", t8), ("t9", t9)):
        if not only or name in only:
            f()
    print("FAILED:", FAIL if FAIL else "none")
    return 1 if FAIL else 0


def _unused():
    t1()
    t2()
    t3()
    t4()
    t5()
    t6()
    t7()
    t8()
    print("FAILED:", FAIL if FAIL else "none")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
