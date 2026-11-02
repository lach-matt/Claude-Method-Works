#!/usr/bin/env python3
"""cover5: the covering constants of I.A section 7 and II.D section 5 (the COVER rows I-SPECTRAL:1570, 1602 and
II-D-REGULARITY:1032) made explicit on the model at b0, five-dimensional Tangherlini of mass mu (CONSTANTS5.md, Round
2, item (iii)).

Each COVER row is a compactness step: "finitely many" neighbourhoods, curves or B's, with no count. A count needs the
dynamics in closed form. On the model it is, and two of the three coverings are not needed at all: an exact escape
function (a function strictly monotone along the flow, with an explicit rate) gives the propagation in one positive
commutator. What stays non-explicit is the constant of each microlocal estimate itself (I.A Propositions 4.2, 4.6, 4.9,
5.1, 5.2; II.D Propositions 3.1-3.6, 4.2), which comes from the calculus. Labels: computed (sympy, exact; certified
rationals), deduced, READ (the lines cited).

  V1 (exact; READ I-SPECTRAL:1465-1489, 1564-1570) the sigma_0-covering (row 1570). Lemma 7.1 gives orders admissible
     on J(sigma_*) = {|sigma_0 - sigma_*| < |sigma_*|/4}. A compact I = [s_a, s_b] in (0, oo) is covered by the J's at
     sigma_k = s_a q^k, q in (1, 5/3), and needs N(I) = 1 + ceil(log(s_b/s_a)/log q) of them; for q -> 5/3 that is the
     least count up to one. Checked exactly at I = [1/100, 100], q = 8/5: 21 intervals, consecutive ones overlapping.
  V2 (exact; READ I-SPECTRAL:103-112, 1599-1602) region (B), fibre infinity (row 1602). On Tangherlini at fibre infinity
     G0 = f xi^2 + |eta|^2/r^2, f = 1 - mu/r^2 (g^-1 on the annihilator of d_t*; g^rr = f for every t* = t + F(r)), so
     the characteristic set lies over r <= r_h = mu^(1/2) and, on it, Hamilton's equations give xi' = -2 xi^2/r and,
     rescaled by rho_inf = 1/|xi|, H r = 2 f sgn(xi): |H r| = 2 (mu/r^2 - 1) > 0 for r < r_h. So r is an
     exact escape function on {r <= r_h - eps}: the "finitely many curves" become one commutant chi(r), and the time from
     r_h - eps to r0 - delta0 is int r^2 dr / (2 (mu - r^2)), computed.
  V3 (exact; READ I-SPECTRAL:1384-1404 (4.5)-(4.7), 1603-1606) region (D), the boundary face (row 1602's second
     covering). On Sigma^d = {(xi + sigma0)^2 + |eta|^2 = sigma0^2}, write xi + sigma0 = sigma0 cos phi, |eta| =
     |sigma0| sin phi; (4.5) gives H xi = 2|eta|^2, H |eta|^2 = -4 (sigma0 + xi)|eta|^2, hence phi' = -2 sigma0 sin phi
     and H log tan(phi/2) = -2 sigma0 exactly: an exact time function. The backward time from {phi <= th_out} to
     {phi >= pi - th_in} is (log tan((pi - th_in)/2) - log tan(th_out/2))/(2|sigma0|).
  V4 (exact; READ II-D-REGULARITY:1015-1032) II.D's cover at the trapped set (row 1032). Five-dimensional Tangherlini's
     photon sphere is r_c = (2 mu)^(1/2) and its radial instability, in Schwarzschild time, has Lyapunov exponent
     lambda_L = (F''(r_c)/2)^(1/2), F = f^2 (1 - f b^2/r^2), b^2 = r_c^2/f(r_c): lambda_L^2 = 1/(2 mu); so a
     backward segment starting at distance delta from the trapped set within distance D of it leaves it
     after at most log(D/delta)/lambda_L (to first order), the "bounded times" of row 1032 made explicit.
  V5 (deduced) what remains: the per-piece constants, the counts above giving how many of them are multiplied (I.A
     (7.1): the chain A -> B -> C -> D -> E -> F adds one constant per piece, so C(7.1) <= sum over the chain of
     products of the pieces' constants, with N(I) chains for the sigma_0-covering).
  Controls (must fail, and do): C1 q = 5/3 exactly leaves the endpoints 5 s/4 = 3 q s/4 uncovered (open intervals): the
  count fails to cover; C2 outside the horizon (r = 2 r_h) G0 > 0 on every nonzero (xi, eta): the characteristic set is
  empty there, so V2's region is the whole of (B); C3 the function phi itself (not log tan(phi/2)) has a non-constant
  rate, so it is not a time function; C4 off the critical impact parameter (b^2 = 11/10 of it) F(r_c) < 0, no orbit
  reaches r_c: the double root, and the exponent, belong to the critical orbit.

    python3 checks/cover5.py
"""
import math
import sys
import textwrap
from fractions import Fraction as Fr

import sympy as sp


def say(s):
    for line in s.split('\n'):
        print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False, break_on_hyphens=False))


def cover_count(sa, sb, q):
    """the J-intervals at sigma_k = sa q^k cover [sa, sb] (exact, with the open intervals' overlaps); returns the count
    or None when consecutive intervals do not overlap"""
    k = 0
    covered_to = Fr(3, 4) * sa                  # J(sa) = (3 sa/4, 5 sa/4)
    s = sa
    n = 0
    while True:
        lo, hi = Fr(3, 4) * s, Fr(5, 4) * s
        if lo >= covered_to and n > 0:
            return None
        covered_to = hi
        n += 1
        if hi > sb:
            return n
        s = s * q
        k += 1


def main():
    ok = {}
    # V1
    sa, sb = Fr(1, 100), Fr(100)
    n = cover_count(sa, sb, Fr(8, 5))
    want = 1 + math.ceil(math.log(float(sb / sa)) / math.log(1.6))
    ok['V1'] = n == want == 21
    say('  V1: [1/100, 100] by J(sigma_k), sigma_k = q^k/100, q = 8/5: %d intervals (formula 1 + ceil(log(s_b/s_a)/'
        'log q) = %d), consecutive ones overlapping' % (n, want))
    nbad = cover_count(sa, sb, Fr(5, 3))
    ok['C1'] = nbad is None
    say('  C1 (control): q = 5/3: consecutive open intervals (3 s/4, 5 s/4), (5 s/4, ...) only touch: no cover: %s'
        % ok['C1'])

    # V2: fibre infinity on Tangherlini
    r, xi, et, mu, s_ = sp.symbols('r xi eta mu s', positive=True)
    f = 1 - mu / r ** 2
    G0 = f * xi ** 2 + et ** 2 / r ** 2
    rdot = sp.diff(G0, xi)                                    # Hamilton's equations (|eta| conserved: H_G0 |eta| = 0)
    xidot = -sp.diff(G0, r)
    on = {et: sp.sqrt(-f) * r * xi}                           # on G0 = 0 (inside the horizon, f < 0)
    xid_on = sp.simplify(xidot.subs(on))
    Hr = sp.simplify(rdot / xi)                               # rescaled by rho_inf = 1/xi (xi > 0 component)
    ok['V2'] = sp.simplify(xid_on + 2 * xi ** 2 / r) == 0 and sp.simplify(Hr - 2 * f) == 0
    T = sp.integrate(r ** 2 / (2 * (mu - r ** 2)), r)
    Tval = (T.subs({mu: 1, r: sp.Rational(9, 10)}) - T.subs({mu: 1, r: sp.Rational(1, 2)}))
    say('  V2: on Sigma_0 at fibre infinity, xi\' = %s, H r = %s (= 2 f < 0 for r < r_h): r is an exact escape '
        'function; the time from r = r_h - eps to r0 - delta0 is int r^2 dr/(2 (mu - r^2)) = [%s]; at mu = 1 from 9/10 '
        'to 1/2: %s = %.6f' % (xid_on, Hr, sp.simplify(T), sp.nsimplify(Tval), float(Tval)))
    outside = sp.simplify(G0.subs({mu: 1, r: 2}))
    ok['C2'] = all(outside.subs({xi: a, et: b}) > 0 for a, b in ((1, 0), (0, 1), (Fr(1, 3), Fr(5, 7))))
    say('  C2 (control): at r = 2 r_h (mu = 1), G0 = %s > 0 off the zero section: no characteristic point there' % outside)

    # V3: the boundary face
    sg, ph = sp.symbols('sigma0 phi', positive=True)
    xi_ = -sg + sg * sp.cos(ph)
    eta2 = sg ** 2 * sp.sin(ph) ** 2
    on_circle = sp.simplify(2 * sg * xi_ + xi_ ** 2 + eta2) == 0
    # H xi = 2 |eta|^2 and xi = -sg + sg cos(phi) give phi' = -2 |eta|^2/(sg sin phi)
    phidot = sp.simplify(-2 * eta2 / (sg * sp.sin(ph)))
    eta2dot_flow = sp.simplify(-4 * (sg + xi_) * eta2)
    eta2dot_chain = sp.simplify(sp.diff(eta2, ph) * phidot)
    rate = sp.simplify(sp.diff(sp.log(sp.tan(ph / 2)), ph) * phidot)
    ok['V3'] = on_circle and sp.simplify(eta2dot_flow - eta2dot_chain) == 0 and sp.simplify(rate + 2 * sg) == 0
    say('  V3: the circle is the characteristic set: %s; phi\' = %s, consistent with H |eta|^2 = -4 (sigma0 + xi)|eta|^2: '
        '%s; H log tan(phi/2) = %s: an exact time function' % (on_circle, phidot, sp.simplify(eta2dot_flow
                                                                                            - eta2dot_chain) == 0,
                                                                rate))
    rate_phi = sp.simplify(phidot)
    ok['C3'] = sp.simplify(sp.diff(rate_phi, ph)) != 0
    say('  C3 (control): H phi = %s is not constant: phi alone is not a time function' % rate_phi)

    # V4: the trapped set
    b2 = sp.Symbol('b2', positive=True)
    F = f ** 2 * (1 - f * b2 / r ** 2)
    rc = sp.sqrt(2 * mu)
    fc = f.subs(r, rc)
    b2c = sp.simplify(rc ** 2 / fc)
    Fc = F.subs(b2, b2c)
    photon = sp.simplify(sp.diff(f / r ** 2, r).subs(r, rc)) == 0
    crit = sp.simplify(Fc.subs(r, rc)) == 0 and sp.simplify(sp.diff(Fc, r).subs(r, rc)) == 0
    lam2 = sp.simplify(sp.diff(Fc, r, 2).subs(r, rc) / 2)
    lamL = sp.sqrt(lam2)
    ok['V4'] = photon and crit and sp.simplify(lam2 - 1 / (2 * mu)) == 0
    say('  V4: photon sphere r_c = (2 mu)^(1/2): %s; dr/dt = 0 and its derivative vanish there on the critical orbit: '
        '%s; Lyapunov exponent (Schwarzschild time) lambda_L^2 = F\'\'(r_c)/2 = %s, lambda_L = %s; a backward segment '
        'from distance delta leaves the D-neighbourhood after about log(D/delta) (2 mu)^(1/2)' % (
            photon, crit, lam2, sp.simplify(lamL)))
    Foff = F.subs(b2, sp.Rational(11, 10) * b2c)
    v0 = sp.simplify(Foff.subs(r, rc).subs(mu, 1))
    ok['C4'] = v0 < 0
    say('  C4 (control): with b^2 = 11/10 of the critical value (mu = 1) F(r_c) = %s < 0: no orbit reaches r_c, so the '
        'double root, and the exponent, belong to the critical orbit only' % v0)
    say('  V5: the counts: I.A (7.1) is a chain of six pieces (A)-(F) at each of N(I) sigma_0-neighbourhoods, with (B) and '
        '(D) replaced by single commutators (V2, V3); II.D\'s cover at the trapped set has explicit escape times (V4). '
        'Not explicit: the constants of the microlocal estimates of each piece (calculus constants).')
    for k, v in ok.items():
        print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
