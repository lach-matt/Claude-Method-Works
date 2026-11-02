#!/usr/bin/env python3
"""axisloss5: where the class Raychaudhuri closure (classchi5) degenerates: the axes (FAMILIES5-NONROUND.md section 4).

Near the axis {x3 = x4 = 0} (rho1 > 0, so away from the origin, which Omega excludes) a T^2 x Z2 x Z2-invariant metric is,
in the coordinates (tau, rho1, x3, x4) of the quotient by the free circle phi1 (the phi1-block G1 dphi1^2 decouples),

  g = h_AB dX^A dX^B + 2 (c_tau dtau + c_1 drho1)(x.dx) + a |dx|^2 + b (x.dx)^2,   x = (x3, x4), A, B in {tau, rho1},

every coefficient a smooth function of (tau, rho1, s), s = |x|^2 (the general invariant form: the Z2 reflections remove
x3 dx4 - x4 dx3 and the cross terms with dphi1), and an invariant phase is u = U(tau, rho1, s). Here the functions are
taken to first order in s (U to second), with arbitrary coefficient functions of (tau, rho1): exact for the limits
below. K2 = x3 d_4 - x4 d_3, psi2 = (1/2) log |K2|^2, kappa2 = g^-1(du, d psi2).

  X1 (exact, symbolic)
     (a) |K2|^2 = a s, and g(d_rho2, d_rho2) = a + b s -> a at the axis: elementary flatness holds automatically for a
         metric smooth in Cartesian form. Control (must fail): the conical metric drho^2 + c^2 rho^2 dphi^2, c != 1, has
         Cartesian components with different limits along the two coordinate axes (not continuous at the axis).
     (b) kappa2 is smooth across the axis and its value there is 2 U_s/a + (terms in U_tau, U_rho1 and the metric's
         1-jet): it carries U_s = (1/2) d_3^2 u, a second derivative of u, while du at the axis has no U_s
         (axisphase5 A1). So at the axis kappa2 is not a function of the 1-jets of u and g.
         Control (must fail): kappa1 = g^-1(du, d psi1) (the circle that does not degenerate there) has no U_s at the
         axis: it stays first order.
     (c) off the axis kappa2 is a function of the 1-jets, but the coefficient of d_3 u is 1/(a rho2) + O(1): unbounded
         as rho2 -> 0. The order-zero structure of classchi5's (R) has a coefficient ~ 1/dist(axis).
     (d) at (rho2, 0) the angular planar component is hess(u)(e4, e4) = kappa2 exactly (e4 = K2/|K2| there), and
         hess(u)(d3, d3)/g33 - kappa2 = (4 U_ss/a + other terms) rho2^2 + o(rho2^2): the planar anisotropy vanishes to
         second order at the axis, so th_h = kappa2 on the axis and |chi|^2 -> kappa1^2 + (th - kappa1)^2/2 pointwise
         there; its coefficient carries U_ss, two orders above the 1-jet. (Off the axis d3 is tilted off the section by
         g(d3, d_tau) = c_tau rho2, so the rho2^2 coefficient also holds the tilt's terms.)
  X2 (computed, mpmath quadrature) the size of the Hardy quotient: in the flat model (a = 1) kappa2 = d_rho u/rho; for
     the invariant family u_eps = exp(-rho^2/eps^2) concentrating at the axis, ||kappa2||/||grad u|| = sqrt(2)/eps in
     L^2(R^2) and grows like 1/eps in H^1 too: kappa2 is not bounded by any norm of du at the same order.
     Control (must fail to grow): the ring u_eps = exp(-(rho - rho0)^2/eps^2), rho0 = 1/2: the ratios stay near 1/rho0
     = 2 as eps -> 0.
  X3 (exact identity; mpmath) what would recover the planar shear: for a planar invariant u, s_pl := u_rhorho -
     u_rho/rho = f - 2 A f with f := u_rhorho + u_rho/rho (the planar Laplacian) and A f := rho^-2 int_0^rho r f dr
     (exact). A is bounded on L^2(R^2) uniformly up to the axis: ||A f||/||f|| and ||s_pl||/||f|| are scale-invariant
     and stay bounded for both families of X2 (an elliptic estimate: the integral runs in rho2, across the family's
     generators, which at the axis lie in span(d_tau, d_rho1), axisphase5 A1). In fact ||s_pl|| = ||f|| exactly (flat
     Bochner in the plane). Control: the pointwise route, bounding s_pl by f and the first-order quotient u_rho/rho
     against ||grad u||, is X2's blow-up.

Labels: computed (X1, X3's identity exact, sympy; X2, X3's bounds by mpmath quadrature at 30 digits). Run: python3
checks/axisloss5.py   (about a minute)
"""
import sys

import mpmath as mp
import sympy as sp


def x1():
    tau, r1, x3, x4, rho = sp.symbols('tau rho1 x3 x4 rho2', real=True)
    s = x3**2 + x4**2
    F = lambda n: sp.Function(n)(tau, r1)
    htt, ht1, h11 = F('htt'), F('ht1'), F('h11')
    ct0, c10 = F('ct'), F('c1')
    a0, a1, b0 = F('a0'), F('a1'), F('b0')
    G10, G11 = F('G10'), F('G11')
    U0, U1, U2 = F('U0'), F('U1'), F('U2')
    a = a0 + a1 * s
    b = b0
    X = [tau, r1, x3, x4]
    g = sp.Matrix([[htt, ht1, ct0 * x3, ct0 * x4],
                   [ht1, h11, c10 * x3, c10 * x4],
                   [ct0 * x3, c10 * x3, a + b * x3**2, b * x3 * x4],
                   [ct0 * x4, c10 * x4, b * x3 * x4, a + b * x4**2]])
    u = U0 + U1 * s + U2 * s**2 / 2
    G1 = G10 + G11 * s
    K2 = sp.Matrix([0, 0, -x4, x3])
    K2sq = sp.simplify((K2.T * g * K2)[0])
    ok_a = sp.simplify(K2sq - a * s) == 0
    # g(d_rho2, d_rho2) with d_rho2 = (x3 d_3 + x4 d_4)/rho2
    R = sp.Matrix([0, 0, x3, x4]) / sp.sqrt(s)
    grr = sp.simplify((R.T * g * R)[0])
    ok_a2 = sp.simplify(grr - (a + b * s)) == 0
    print("X1 (a) |K2|^2 = a s:", ok_a, "; g(d_rho2, d_rho2) = a + b s (-> a = |K2|^2/s at the axis):", ok_a2)
    # control: conical metric in Cartesian components: drho^2 + c^2 rho^2 dphi^2 = |dx|^2 + (c^2-1)(x dy - y dx)^2/rho^2
    xx, yy, cc = sp.symbols('x y c', real=True)
    gxx = 1 + (cc**2 - 1) * yy**2 / (xx**2 + yy**2)
    lim_x = sp.limit(gxx.subs(yy, 0), xx, 0)
    lim_y = sp.limit(gxx.subs(xx, 0), yy, 0)
    ctl_a = sp.simplify(lim_x - lim_y.subs(cc, sp.Rational(3, 2))) != 0 and lim_x == 1
    print("   control: conical c = 3/2, g_xx -> %s along the x-axis, %s along the y-axis: discontinuous: %s"
          % (lim_x, lim_y.subs(cc, sp.Rational(3, 2)), ctl_a))
    # inverse metric at the point (rho2, 0); every quantity below is evaluated there, then rho2 -> 0
    pt = {x3: rho, x4: 0}
    gi = g.subs(pt).inv().applyfunc(sp.cancel)
    du = [sp.diff(u, v).subs(pt) for v in X]
    psi2 = sp.log(K2sq) / 2
    dpsi2 = [sp.cancel(sp.diff(psi2, v).subs(pt)) for v in X]
    psi1 = sp.log(G1) / 2
    dpsi1 = [sp.cancel(sp.diff(psi1, v).subs(pt)) for v in X]
    at_axis = lambda e: sp.cancel(sp.cancel(e).subs(rho, 0))
    kap2 = sp.cancel(sum(gi[i, j] * du[i] * dpsi2[j] for i in range(4) for j in range(4)))
    kap1 = sp.cancel(sum(gi[i, j] * du[i] * dpsi1[j] for i in range(4) for j in range(4)))
    kap2_axis = at_axis(kap2)
    kap1_axis = at_axis(kap1)
    du_axis = [at_axis(d) for d in du]
    coefU1 = sp.cancel(sp.diff(kap2_axis, U1))
    ok_b = sp.cancel(coefU1 - 2 / a0) == 0 and all(not d.has(U1) for d in du_axis)
    ctl_b = not kap1_axis.has(U1)
    print("X1 (b) kappa2 on the axis: d/dU_s =", coefU1, "; du on the axis free of U_s:",
          all(not d.has(U1) for d in du_axis), "->", ok_b)
    print("   (U_s = (1/2) d_3^2 u on the axis:", sp.expand(sp.diff(u, x3, 2).subs({x3: 0, x4: 0}) - 2 * U1) == 0,
          ")")
    print("   control: kappa1 on the axis free of U_s (stays first order):", ctl_b)
    # (c) off the axis: kappa2 as a function of the Cartesian 1-jet; coefficient of d_3 u
    coef3 = sp.cancel(sum(gi[2, j] * dpsi2[j] for j in range(4)))
    lead = at_axis(rho * coef3)
    ok_c = sp.cancel(lead - 1 / a0) == 0
    print("X1 (c) off the axis, coefficient of d_3 u in kappa2 ~ 1/(a rho2): lim rho2 * coef =", lead, "->", ok_c)
    # (d) planar Hessian at (rho2, 0): Christoffels at the point from g^-1 there and dg there
    n = 4
    dg = [[[sp.diff(g[i, j], X[k]).subs(pt) for k in range(n)] for j in range(n)] for i in range(n)]
    Gam = [[[sum(gi[c, d] * (dg[d][j][i] + dg[d][i][j] - dg[i][j][d]) for d in range(n)) / 2 for j in range(n)]
            for i in range(n)] for c in range(n)]

    def hess(i, j):
        return sp.cancel(sp.diff(u, X[i], X[j]).subs(pt) - sum(Gam[c][i][j] * du[c] for c in range(n)))
    g33 = g[2, 2].subs(pt)
    g44 = g[3, 3].subs(pt)
    chi44 = sp.cancel(hess(3, 3) / g44)
    ok_d1 = sp.cancel(chi44 - kap2) == 0
    shear = sp.cancel(hess(2, 2) / g33 - kap2)
    sh0 = at_axis(shear)
    sh2 = at_axis(shear / rho**2)
    dU2 = sp.cancel(sp.diff(sh2, U2))
    ok_d2 = sh0 == 0 and sp.cancel(dU2 - 4 / a0) == 0
    print("X1 (d) chi(e4, e4) = kappa2 exactly:", ok_d1, "; chi(d3,d3)/g33 - kappa2 -> 0 on the axis:", sh0 == 0,
          "; its rho2^2 coefficient has d/dU_ss =", dU2, "->", ok_d2)
    return ok_a and ok_a2 and ctl_a and ok_b and ctl_b and ok_c and ok_d1 and ok_d2


mp.mp.dps = 30


def norms(urho, urhorho, kap, dkap, lo, hi):
    """L^2(R^2) and H^1 norms (radial functions; weight 2 pi rho) on [lo, hi]."""
    w = lambda f: mp.quad(lambda r: 2 * mp.pi * r * f(r)**2, [lo, (lo + hi) / 2, hi])
    gu0 = w(urho)
    gu1 = gu0 + w(urhorho) + w(lambda r: urho(r) / r)
    k0 = w(kap)
    k1 = k0 + w(dkap)
    return mp.sqrt(k0 / gu0), mp.sqrt(k1 / gu1)


def x2():
    ok = True
    print("X2 (mpmath) ||kappa2|| / ||grad u|| for families concentrating at the axis and on a ring")
    axis = []
    for eps in (mp.mpf('0.2'), mp.mpf('0.1'), mp.mpf('0.05'), mp.mpf('0.025')):
        ur = lambda r, e=eps: -2 * r / e**2 * mp.exp(-r**2 / e**2)
        urr = lambda r, e=eps: (-2 / e**2 + 4 * r**2 / e**4) * mp.exp(-r**2 / e**2)
        kap = lambda r, e=eps: -2 / e**2 * mp.exp(-r**2 / e**2)
        dk = lambda r, e=eps: 4 * r / e**4 * mp.exp(-r**2 / e**2)
        r0, r1 = norms(ur, urr, kap, dk, mp.mpf(0), 12 * eps)
        axis.append((eps, r0, r1))
        print("   axis eps = %s: L2 ratio %s (sqrt(2)/eps = %s), H1 ratio %s"
              % (mp.nstr(eps, 3), mp.nstr(r0, 8), mp.nstr(mp.sqrt(2) / eps, 8), mp.nstr(r1, 8)))
        ok &= abs(r0 - mp.sqrt(2) / eps) < mp.mpf('1e-12') * r0
    grow = all(axis[i + 1][2] > 1.8 * axis[i][2] for i in range(len(axis) - 1))
    print("   H1 ratio roughly doubles as eps halves:", grow)
    ok &= grow
    rho0 = mp.mpf('0.5')
    ring = []
    for eps in (mp.mpf('0.05'), mp.mpf('0.025'), mp.mpf('0.0125')):
        f = lambda r, e=eps: mp.exp(-(r - rho0)**2 / e**2)
        ur = lambda r, e=eps: -2 * (r - rho0) / e**2 * f(r, e)
        urr = lambda r, e=eps: (-2 / e**2 + 4 * (r - rho0)**2 / e**4) * f(r, e)
        kap = lambda r, e=eps: ur(r, e) / r
        dk = lambda r, e=eps: urr(r, e) / r - ur(r, e) / r**2
        r0, r1 = norms(ur, urr, kap, dk, rho0 - 10 * eps, rho0 + 10 * eps)
        ring.append((eps, r0, r1))
        print("   ring rho0 = 1/2, eps = %s: L2 ratio %s, H1 ratio %s" % (mp.nstr(eps, 3), mp.nstr(r0, 8),
                                                                       mp.nstr(r1, 8)))
    bounded = all(r0 < 2.5 and r1 < 2.5 for _, r0, r1 in ring)
    print("   control: ring ratios bounded (near 1/rho0 = 2), do not grow:", bounded)
    return ok and bounded


def x3():
    r = sp.symbols('rho', positive=True)
    U = sp.Function('U')
    up = sp.diff(U(r), r)
    f = sp.diff(U(r), r, 2) + up / r
    # int_0^rho r' f dr' = rho U'(rho) (for U' bounded at 0): check d/drho of rho U' equals rho f
    ok_int = sp.simplify(sp.diff(r * up, r) - r * f) == 0
    Af = (r * up) / r**2
    s_pl = sp.diff(U(r), r, 2) - up / r
    ok_id = sp.simplify(s_pl - (f - 2 * Af)) == 0
    print("X3 (exact) int_0^rho r f = rho U':", ok_int, "; s_pl = f - 2 A f:", ok_id)
    ok = ok_int and ok_id
    print("   (mpmath) ||A f||/||f|| and ||s_pl||/||f|| in L^2(R^2): uniformly bounded up to the axis")
    res = []
    for kind, eps in (('axis', mp.mpf('0.1')), ('axis', mp.mpf('0.025')), ('ring', mp.mpf('0.05')),
                      ('ring', mp.mpf('0.0125'))):
        if kind == 'axis':
            ur = lambda q, e=eps: -2 * q / e**2 * mp.exp(-q**2 / e**2)
            urr = lambda q, e=eps: (-2 / e**2 + 4 * q**2 / e**4) * mp.exp(-q**2 / e**2)
            lo, hi = mp.mpf(0), 12 * eps
        else:
            rho0 = mp.mpf('0.5')
            ur = lambda q, e=eps: -2 * (q - rho0) / e**2 * mp.exp(-(q - rho0)**2 / e**2)
            urr = lambda q, e=eps: (-2 / e**2 + 4 * (q - rho0)**2 / e**4) * mp.exp(-(q - rho0)**2 / e**2)
            lo, hi = mp.mpf('0.5') - 10 * eps, mp.mpf('0.5') + 10 * eps
        ff = lambda q: urr(q) + (ur(q) / q if q != 0 else urr(q))
        Aq = lambda q: (ur(q) / q if q != 0 else urr(q))
        sq = lambda q: urr(q) - (ur(q) / q if q != 0 else urr(q))
        w = lambda h: mp.quad(lambda q: 2 * mp.pi * q * h(q)**2, [lo, (lo + hi) / 2, hi])
        nf = mp.sqrt(w(ff))
        ra, rs = mp.sqrt(w(Aq)) / nf, mp.sqrt(w(sq)) / nf
        res.append((kind, eps, ra, rs))
        print("   %s eps = %s: ||A f||/||f|| = %s, ||s_pl||/||f|| = %s" % (kind, mp.nstr(eps, 3), mp.nstr(ra, 8),
                                                                       mp.nstr(rs, 8)))
    bnd = all(ra < 2 and rs < 3 for _, _, ra, rs in res)
    scale_inv = abs(res[0][2] - res[1][2]) < mp.mpf('1e-15')
    print("   bounded:", bnd, "; scale-invariant at the axis (same ratio at both eps):", scale_inv)
    return ok and bnd and scale_inv


if __name__ == '__main__':
    res = [x1(), x2(), x3()]
    print("PASS" if all(res) else "FAIL")
    sys.exit(0 if all(res) else 1)
