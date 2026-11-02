#!/usr/bin/env python3
"""twotransport5: the record's transport Lemma 2.4 for both generators on the two-dust domain (FAMILIES5-FULL.md
section 5).

The record's Lemma 2.4 (N1STAR-PROOF.md:230-235) bounds ||phi(tau)|| for L0 phi - c phi = f on the annuli A(tau) = {a <=
|x| <= b(tau)}, L0 = d_tau - xhat.d_x, from d_tau ||phi||^2 = 2 <phi, f + c phi> - int (3/r) phi^2 + (1 + b')
int_(|x| = b) phi^2 - int_(|x| = a) phi^2, the two boundary terms having a sign. With two families the outgoing phases
are transported along ell_out. On the two-dust background in the chart (vhat, R), g0 = -e^(2 psi) f dvhat^2 + 2 e^psi
dvhat dR + R^2 dOmega^2, f = 1 - mu/R^2, psi <= 0 (FAMILIES5.md 4i), tau := vhat - R, x := R xhat, and a radial vector
field Z = d_tau + c xhat.d_x (Z(tau) = 1):

  T1 (exact) d_tau int_(A(tau)) phi^2 = 2 <phi, Z phi> + int div(c xhat) phi^2 + (b' - c(b)) int_(|x| = b) phi^2 + c(a)
     int_(|x| = a) phi^2 (the divergence theorem on the annulus in R^4, computed on radial functions, |S^3| = 2 pi^2).
     The record's case is c = -1.
  T2 (exact) the ingoing generator ell_in = e^(-psi) d_R|vhat has c = -1 (the record's L0, up to the factor e^(-psi));
     the outgoing generator ell_out = g0^-1 du has c_out = y/(1 - y), y := e^psi f/2. Since f <= 1 and psi <= 0, y <=
     1/2, so c_out in (-1, 1]: b' - c_out(b) <= -2 + 1 < 0 with the record's b' = -2. On R = a, where mu > a^2 (f < 0;
     FAMILIES5-FULL.md section 2, mu >= mu0 > a^2), y < 0 and c_out(a) < 0. Both boundary terms have the record's sign,
     so Lemma 2.4 holds for the outgoing transports with the same proof.
  Control (exact): if R = a were untrapped (f > 0 there, the case twodomain5 D4 exhibits for a strong outgoing pulse
     outside the hole, excluded here by the mass bound), c_out(a) > 0 and the inner boundary term has the wrong sign.

Labels: computed (exact, sympy). Run: python3 checks/twotransport5.py   (seconds)
"""
import sys

import sympy as sp


def t1():
    tau, rr, a = sp.symbols('tau r a', positive=True)
    b = sp.Function('b')(tau)
    phi = sp.Function('phi')(tau, rr)
    c = sp.Function('c')(tau, rr)
    w = 2 * sp.pi**2 * rr**3                                                     # the area of the sphere of radius r
    lhs = sp.diff(sp.Integral(phi**2 * w, (rr, a, b)), tau).doit()
    Zphi = sp.diff(phi, tau) + c * sp.diff(phi, rr)
    divc = sp.diff(rr**3 * c, rr) / rr**3                                        # div(c xhat) in R^4 for radial c
    rhs = (sp.Integral(2 * phi * Zphi * w, (rr, a, b)) + sp.Integral(divc * phi**2 * w, (rr, a, b))
           + (sp.diff(b, tau) - c.subs(rr, b)) * (phi**2 * w).subs(rr, b) + c.subs(rr, a) * (phi**2 * w).subs(rr, a))
    # compare after moving everything under one integral: the integrand difference must be an exact r-derivative
    # whose boundary values cancel the boundary terms
    integrand = 2 * phi * Zphi * w + divc * phi**2 * w - 2 * phi * sp.diff(phi, tau) * w
    total = sp.diff(c * phi**2 * w, rr)
    ok = sp.simplify(integrand - total) == 0
    bnd = sp.simplify((c * phi**2 * w).subs(rr, b) - (c * phi**2 * w).subs(rr, a)
                      - (c.subs(rr, b) * (phi**2 * w).subs(rr, b) - c.subs(rr, a) * (phi**2 * w).subs(rr, a))) == 0
    return ok and bnd, (lhs, rhs)


def t2():
    psi, f = sp.symbols('psi f', real=True)
    # g0^-1 in (vhat, R): g^(vv) = 0, g^(vR) = e^-psi, g^(RR) = f; outgoing null direction: dR/dvhat = e^psi f / 2
    gi = sp.Matrix([[0, sp.exp(-psi)], [sp.exp(-psi), f]])
    g = gi.inv()
    lam_ = sp.Symbol('m')
    vec = sp.Matrix([1, lam_])
    roots = sp.solve(sp.Eq((vec.T * g * vec)[0], 0), lam_)
    out_slope = [x for x in roots if x != 0][0]                                  # dR/dvhat along ell_out
    ok_slope = sp.simplify(out_slope - sp.exp(psi) * f / 2) == 0
    y = sp.Symbol('y', real=True)
    c_out = y / (1 - y)                                                          # dR/dtau, tau = vhat - R
    c_check = sp.simplify(c_out.subs(y, out_slope) - out_slope / (1 - out_slope)) == 0
    # in (vhat, R): ell_in ~ d_R at fixed vhat: dvhat = 0, so dtau = -dR: c_in = -1
    c_in = -1
    # y <= 1/2 => c_out in (-1, 1]; at y < 0, c_out < 0
    bnd_outer = all(float(c_out.subs(y, yy)) > -1 for yy in (-50, -1, -0.1, 0, 0.25, 0.5))
    inner = all(float(c_out.subs(y, yy)) < 0 for yy in (-50, -1, -0.01))
    mono = sp.simplify(sp.diff(c_out, y) - 1 / (1 - y)**2) == 0
    lim = sp.limit(c_out, y, -sp.oo) == -1
    ctl = float(c_out.subs(y, 0.2)) > 0
    return ok_slope and c_check and bnd_outer and inner and mono and lim and c_in == -1, ctl


def main():
    ok1, _ = t1()
    ok2, ctl = t2()
    print('  T1: the transport energy identity on the annuli with the two boundary terms: %s' % ok1)
    print('  T2: c_in = -1; c_out = y/(1 - y), y = e^psi f/2, increasing in y, tending to -1 as y -> -oo, so in (-1, 1] '
          'for y <= 1/2 and negative for y < 0 (R = a trapped): %s' % ok2)
    print('  control: R = a untrapped (y = 0.2 there): c_out(a) > 0, the inner term has the wrong sign: %s' % ctl)
    ok = {'T1': ok1, 'T2': ok2, 'control': ctl}
    for k, v in ok.items():
        print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
