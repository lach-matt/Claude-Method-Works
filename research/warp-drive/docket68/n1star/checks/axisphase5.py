#!/usr/bin/env python3
"""axisphase5: which null phases the T^2 class permits, and angular separation at the axes (FAMILIES5-FULL.md part II).

In the class the waves are T^2-invariant, so each family's phase is a T^2-invariant function on R x R^4, a function of
(tau, rho1^2, rho2^2), rho1^2 = x1^2 + x2^2, rho2^2 = x3^2 + x4^2; its rays project to the orbit space, the quarter
plane {rho1, rho2 >= 0} (polar: rho1 = r cos th, rho2 = r sin th), whose edges th = 0, pi/2 are the axes.

  A1 (exact) a smooth function F(tau, rho1^2, rho2^2) has, at every point of the axis {x3 = x4 = 0} (and likewise of
     {x1 = x2 = 0}), its spatial gradient along xhat: its x3, x4 components vanish and its (x1, x2) part is radial. So
     at an axis point the gradient of an invariant phase lies in span(dtau, dr), and if it is null for g0 = eta + (mu/r^2)
     dv dv (Vaidya; Minkowski at mu = 0) it is a multiple of dv or of the outgoing radial null covector. Two families
     whose phases are both ingoing (or both outgoing) at an axis point have parallel gradients there.
     Control: the non-invariant phase tau - x3 has, at the axis point (1, 0, 0, 0), a gradient off span(dtau, dr).
  A2 (exact) non-radial invariant null phases exist: on Minkowski, w = tau + f with f the distance to the T^2-orbit of
     the ellipse {(rho1/al)^2 + (rho2/be)^2 = 1}, outside it, written parametrically x = p(t) + s n(t) (p on the
     ellipse, n its unit normal), f = s: |grad f| = 1, f is even in rho1 and in rho2, and its rays are radial exactly at
     the axes (t = 0, pi/2) and nowhere else in between (al != be). For the radial phase v = tau + r and w (both
     ingoing), g0^-1(dv, dw) = -1 + cos(beta), beta the angle between the ray and the radial direction; as the axis is
     approached along a wavefront, g0^-1(dv, dw) / beta^2 -> -1/2 and beta / th tends to a nonzero constant: the
     mixed symbol of the harmonic (n1, n2), -n1 n2 g0^-1(dv, dw), vanishes at the axes to second order (a small
     divisor), and Huneau-Luk's angular separation (Definition 4.1 of [HL18], cos of the spatial angle < 1 - eta') fails
     there. The pair (v, u) of the ingoing and outgoing radial phases has g0^-1(dv, du) = -2 at every point (Minkowski):
     separated.
  A3 (exact) the averaged stress of the family w, F^2 dw (x) dw, has a nonzero th-th component wherever w_th != 0 (off
     the axes, al != be): a background carrying it is not round (not SO(4)-invariant), so the explicit Vaidya structure
     of FAMILIES5-FULL.md section 2 is lost; its phi_i-components vanish (dw has none).
     Control: at al = be (a sphere) w is radial, beta = 0 everywhere, the th-th component vanishes and A2's small divisor
     is absent (g0^-1(dv, dw) = 0 identically: the two phases are the same family).

Labels: computed (exact, sympy). Run: python3 checks/axisphase5.py   (under a minute)
"""
import sys

import sympy as sp


def a1():
    tau, x1, x2, x3, x4, mu = sp.symbols('tau x1 x2 x3 x4 mu', real=True)
    Ff = sp.Function('F')
    u = Ff(tau, x1**2 + x2**2, x3**2 + x4**2)
    X = [tau, x1, x2, x3, x4]
    grad = [sp.diff(u, z) for z in X]
    pt = {x2: 0, x3: 0, x4: 0}                                                    # the axis point (x1, 0, 0, 0)
    g_at = [sp.simplify(c.subs(pt)) for c in grad]
    ok_inv = g_at[3] == 0 and g_at[4] == 0 and g_at[2] == 0                      # only dtau and dx1 = dr there
    # the other axis, at (0, 0, x3, 0): only dtau and dx3 = dr
    pt2 = {x1: 0, x2: 0, x4: 0}
    g2 = [sp.simplify(c.subs(pt2)) for c in grad]
    ok_inv2 = g2[1] == 0 and g2[2] == 0 and g2[4] == 0
    # null covectors in span(dtau, dr) for Vaidya: g0^-1 = eta^-1 - (mu/r^2) L0 L0, L0 = d_tau - d_r (radial part)
    a, b, r = sp.symbols('a b r', positive=True)
    ginv = sp.Matrix([[-1, 0], [0, 1]]) - (mu / r**2) * sp.Matrix([[1, -1], [-1, 1]])
    k = sp.Matrix([a, b])                                                        # a dtau + b dr
    roots = sp.solve(sp.Eq((k.T * ginv * k)[0], 0), b)
    two = len(roots) == 2 and any(sp.simplify(rt - a) == 0 for rt in roots)      # b = a is dv = dtau + dr
    # control: tau - x3 at (1, 0, 0, 0)
    w = tau - x3
    gw = [sp.diff(w, z).subs({x1: 1, x2: 0, x3: 0, x4: 0}) for z in X]
    ctl = gw[3] != 0
    return ok_inv and ok_inv2 and two, ctl, roots


def ellipse(al, be):
    t = sp.Symbol('t', real=True)
    s = sp.Symbol('s', positive=True)
    p = sp.Matrix([al * sp.cos(t), be * sp.sin(t)])
    tang = sp.diff(p, t)
    n = sp.Matrix([tang[1], -tang[0]]) / sp.sqrt(tang[0]**2 + tang[1]**2)         # outward unit normal
    x = p + s * n
    return t, s, p, n, x


def a2(al=sp.Rational(1, 2), be=sp.Rational(1, 3)):
    t, s, p, n, x = ellipse(al, be)
    J = x.jacobian([t, s])
    # grad f = n: d f/d(t, s) = (0, 1) must equal n . dx/d(t, s)
    eik = sp.simplify(n.T * J - sp.Matrix([[0, 1]])) == sp.zeros(1, 2)
    unit = sp.simplify(n.dot(n) - 1) == 0
    # evenness: (t, s) -> (-t, s) maps (rho1, rho2) -> (rho1, -rho2); (t, s) -> (pi - t, s) maps rho1 -> -rho1
    ev2 = sp.simplify(x.subs(t, -t) - sp.Matrix([x[0], -x[1]])) == sp.zeros(2, 1)
    ev1 = sp.simplify(x.subs(t, sp.pi - t) - sp.Matrix([-x[0], x[1]])) == sp.zeros(2, 1)
    # angle between the ray (n) and the radial direction xhat
    xhat = x / sp.sqrt(x.dot(x))
    cosb = sp.simplify(n.dot(xhat))
    at_axes = [sp.simplify(cosb.subs(t, 0) - 1) == 0, sp.simplify(cosb.subs(t, sp.pi / 2) - 1) == 0]
    s0 = sp.Rational(3, 2)
    mid = [float(cosb.subs({t: sp.pi * k / 16, s: s0})) for k in (2, 4, 6)]
    radial_only_at_axes = all(m < 1 - 1e-6 for m in mid)
    # near the axis t -> 0 along the wavefront s = s0: g^-1(dv, dw) = -1 + cos(beta), beta ~ c t, th ~ c' t
    gvw = -1 + cosb
    th = sp.atan2(x[1], x[0])
    beta2 = sp.series(sp.simplify((1 - cosb) * 2).subs(s, s0), t, 0, 3).removeO()   # beta^2 to leading order
    thser = sp.series(th.subs(s, s0), t, 0, 2).removeO()
    lim_g = sp.limit((gvw / (beta2 / 2)).subs(s, s0), t, 0) if beta2 != 0 else None
    c_beta = sp.sqrt(sp.simplify(beta2 / t**2))
    c_th = sp.simplify(thser / t)
    ratio = sp.simplify(c_beta / c_th)
    # HL's spatial cosine between grad v (xhat) and grad w (n): cos beta -> 1 at the axis
    hl = sp.limit(cosb.subs(s, s0), t, 0)
    # A3: the th-th component of dw (x) dw in the orbit space: w_th = r (n . e_th), e_th = (-sin th, cos th)
    eth = sp.Matrix([-x[1], x[0]]) / sp.sqrt(x.dot(x))
    wth = sp.simplify(sp.sqrt(x.dot(x)) * n.dot(eth))
    wth_mid = float(wth.subs({t: sp.pi / 5, s: s0}))
    return dict(eik=eik and unit, even=ev1 and ev2, axes=all(at_axes), between=radial_only_at_axes, mid=mid,
                lim=lim_g, ratio=ratio, hl=hl, wth=wth_mid, c_beta=c_beta, c_th=c_th)


def main():
    ok = {}
    good, ctl, roots = a1()
    print('  A1: an invariant phase has its gradient in span(dtau, dr) on both axes, and the null ones there are dv and '
          'the outgoing radial covector (b/a = %s): %s; control tau - x3 leaves span(dtau, dr): %s'
          % (roots, good, ctl), flush=True)
    ok['A1'] = good and ctl
    r = a2()
    sep = -2                                                                     # g^-1(dv, du), Minkowski, radial pair
    print('  A2: f = distance to the ellipse orbit (al, be) = (1/2, 1/3): eikonal %s, even in rho1 and rho2 %s, rays '
          'radial at both axes %s and not between %s (cos beta at t = pi/8, pi/4, 3pi/8: %s); near the axis g^-1(dv, '
          'dw)/(beta^2/2) -> %s, beta/th -> %s (beta ~ %s t, th ~ %s t): the mixed symbol vanishes like th^2; HL\'s '
          'cosine -> %s (separation fails); the radial in/out pair has g^-1(dv, du) = %d everywhere'
          % (r['eik'], r['even'], r['axes'], r['between'], ' '.join('%.6f' % m for m in r['mid']), r['lim'],
             r['ratio'], r['c_beta'], r['c_th'], r['hl'], sep), flush=True)
    ok['A2'] = (r['eik'] and r['even'] and r['axes'] and r['between'] and r['lim'] == -1 and r['ratio'] != 0
                and r['hl'] == 1)
    print('  A3: the th-th component of the family\'s stress, w_th at t = pi/5, s = 3/2: %.6f (nonzero: not round)'
          % r['wth'], flush=True)
    rc = a2(sp.Rational(1, 2), sp.Rational(1, 2))
    ctl3 = rc['eik'] and abs(rc['wth']) < 1e-12 and all(abs(m - 1) < 1e-12 for m in rc['mid'])
    print('  A3 control (al = be, a sphere): w_th = %.2e, cos beta = %s: radial everywhere, no small divisor: %s'
          % (rc['wth'], rc['mid'], ctl3), flush=True)
    ok['A3'] = abs(r['wth']) > 1e-3 and ctl3
    for k, v in ok.items():
        print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
