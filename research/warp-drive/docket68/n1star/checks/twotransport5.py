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
     The record's case is c = -1. (Round 5, the verifier's minor 2: lhs and rhs are now compared -- lhs - rhs is
     reduced to an r-integral of zero -- and the mutations "sign of b' - c(b) flipped" and "lhs = 0" are rejected.)
  T2 (exact) the ingoing generator ell_in = e^(-psi) d_R|vhat has c = -1 (the record's L0, up to the factor e^(-psi));
     the outgoing generator ell_out = g0^-1 du has c_out = y/(1 - y), y := e^psi f/2. Since f <= 1 and psi <= 0, y <=
     1/2, so c_out in (-1, 1]: b' - c_out(b) <= -2 + 1 < 0 with the record's b' = -2. On R = a, where mu > a^2 (f < 0;
     FAMILIES5-FULL.md section 2, mu >= mu0 > a^2), y < 0 and c_out(a) < 0. Both boundary terms have the record's sign,
     so Lemma 2.4 holds for the outgoing transports with the same proof.
  T3 (computed, RK4; replaces round 1's sign at a typed y, the verifier's item 4) the domain-of-dependence form of
     the inner boundary term's sign, on the example's region III (Tangherlini of the seed's mass mu0 = 0.82211 > a^2 =
     0.49, psi = 0): the outgoing characteristics dR/dtau = c_out(R), c_out = y/(1 - y), y = f/2, traced back from 40
     points of {a < R <= a + 0.4} at tau1 = tau0 + 1 to tau0, never reach R = a: no outgoing ray enters the annulus
     through R = a, which is what c(a) int_(|x|=a) phi^2 <= 0 says. c_out(a) is computed from mu0, not typed.
  Control (computed, must fail): the same with an untrapped inner sphere, mu = 0.3 < a^2 (the case twodomain5 D4
     exhibits for a strong outgoing pulse outside the hole, excluded here by the mass bound): c_out(a) > 0 and rays from
     the annulus traced back leave it through R = a, so data on {R = a} enter and the estimate from Sigma_tau0 alone
     fails.

Labels: computed (T1, T2 exact, sympy; T3 RK4 in floating point). Run: python3 checks/twotransport5.py   (seconds)
"""
import sys

import sympy as sp


def t1(mutate=None):
    """T1, with lhs and rhs compared: lhs - rhs, written as one integral over (a, b(tau)) plus boundary terms, must be
    the integral of an exact r-derivative whose boundary values cancel the boundary terms (round 5, the verifier's
    minor 2: the earlier version never compared them)."""
    tau, rr, a = sp.symbols('tau r a', positive=True)
    b = sp.Function('b')(tau)
    phi = sp.Function('phi')(tau, rr)
    c = sp.Function('c')(tau, rr)
    w = 2 * sp.pi**2 * rr**3                                                     # the area of the sphere of radius r
    lhs = sp.diff(sp.Integral(phi**2 * w, (rr, a, b)), tau).doit()
    if mutate == 'lhs0':
        lhs = sp.Integer(0)
    Zphi = sp.diff(phi, tau) + c * sp.diff(phi, rr)
    divc = sp.diff(rr**3 * c, rr) / rr**3                                        # div(c xhat) in R^4 for radial c
    sgn = -1 if mutate == 'flip' else 1
    rhs = (sp.Integral(2 * phi * Zphi * w, (rr, a, b)) + sp.Integral(divc * phi**2 * w, (rr, a, b))
           + sgn * (sp.diff(b, tau) - c.subs(rr, b)) * (phi**2 * w).subs(rr, b)
           + c.subs(rr, a) * (phi**2 * w).subs(rr, a))
    D = sp.expand(lhs - rhs)
    # split D into its integrals over (a, b) and the rest (boundary terms)
    integrand, bnd = sp.Integer(0), sp.Integer(0)
    for term in sp.Add.make_args(D):
        ints = [x for x in term.atoms(sp.Integral)]
        if ints:
            assert len(ints) == 1 and ints[0].limits == ((rr, a, b),)
            coef = sp.simplify(term / ints[0])
            integrand += coef * ints[0].function
        else:
            bnd += term
    # lhs - rhs = int_a^b I dr + B must vanish: I = -d_r(F) with F(b) - F(a) = B, F = c phi^2 w
    Fp = c * phi**2 * w
    ok_int = sp.simplify(integrand + sp.diff(Fp, rr)) == 0
    ok_bnd = sp.simplify(bnd - (Fp.subs(rr, b) - Fp.subs(rr, a))) == 0
    return ok_int and ok_bnd, (lhs, rhs)


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
    return ok_slope and c_check and bnd_outer and inner and mono and lim and c_in == -1


def t3(mu, a=0.7, n=40, steps=2000):
    """trace the outgoing characteristics of Z_out back from tau1 = tau0 + 1 on Tangherlini of mass mu (psi = 0);
    returns c_out(a) and how many of the n starting points reach R = a"""
    def c_out(R):
        y = (1 - mu / R**2) / 2
        return y / (1 - y)

    def rhs(R):
        return -c_out(R)                                              # backward in tau
    exits = 0
    for i in range(n):
        R = a + 0.4 * (i + 1) / n
        h = 1.0 / steps
        for _ in range(steps):
            k1 = rhs(R)
            k2 = rhs(R + h * k1 / 2)
            k3 = rhs(R + h * k2 / 2)
            k4 = rhs(R + h * k3)
            R += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
            if R <= a:
                exits += 1
                break
    return c_out(a), exits


def main():
    ok1, _ = t1()
    ok2 = t2()
    ca, ex = t3(0.82211)
    cb, exb = t3(0.3)
    ok3 = ca < 0 and ex == 0
    ctl = cb > 0 and exb > 0                                           # True: the untrapped case is rejected
    okf, _ = t1('flip')
    ok0, _ = t1('lhs0')
    print('  T1: the transport energy identity on the annuli with the two boundary terms (lhs - rhs reduces to the\n'
          '      integral of -d_r(c phi^2 w) plus its boundary values, which cancel): %s; mutations rejected: the sign\n'
          '      of b\' - c(b) flipped %s, lhs = 0 %s' % (ok1, not okf, not ok0))
    ok1 = ok1 and not okf and not ok0
    print('  T2: c_in = -1; c_out = y/(1 - y), y = e^psi f/2, increasing in y, tending to -1 as y -> -oo,\n'
          '      so in (-1, 1] for y <= 1/2 and negative for y < 0 (R = a trapped): %s' % ok2)
    print('  T3: mu0 = 0.82211 > a^2: c_out(a) = %.4f < 0, and of 40 rays traced back from the annulus %d reach R = a: '
          '%s' % (ca, ex, ok3))
    print('  control: mu = 0.3 < a^2 (R = a untrapped): c_out(a) = %.4f > 0, %d of 40 rays leave through R = a: '
          'rejected %s' % (cb, exb, ctl))
    ok = {'T1': ok1, 'T2': ok2, 'T3': ok3, 'control': ctl}
    for k, v in ok.items():
        print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
