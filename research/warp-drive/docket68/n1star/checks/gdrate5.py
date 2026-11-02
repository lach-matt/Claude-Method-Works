#!/usr/bin/env python3
"""gdrate5.py -- GAUGEDECAY5.md Round 4, task 2: a rate better than t_*^(-1/2) for the harmonic-gauge vector -- where
the first obstruction is, computed.  Model computations near infinity; the labels in GAUGEDECAY5 say which statements
are deduced and which are formal.

  G1 (exact) The zero-energy family near the boundary, l = 0, in the outgoing time t_* = t - r.  On Cartesian
     components Box is the scalar operator up to rho^2-relative terms (gdext5.py E1-E2); at mu = 0, in (t_*, r),
     Box_0 = 2 d_r d_t* - d_r^2 - (n-1)/r d_r + (n-1)/r d_t*, so P-hat(sigma) = P-hat(0) - i sigma L_1 with L_1 = 2 d_r +
     (n-1)/r and no sigma^2 term; L_1 r^-q = -2 (q - (n-1)/2) r^(-q-1), at n = 4 the factor -2(q - 3/2).  With the mass,
     the sigma^2 coefficient is -g^-1(dt_*, dt_*) = 0, dt - dr being null for g (III.B's t_* differs by C - 8 mu/r,
     which gives L_2 in rho^2 C^oo, round 2's B1).  Control: in
     the static time t the sigma-linear term vanishes (L_1 = 0), so the factor -2(q - 3/2) is particular to t_*.
  G2 (exact) The first non-smooth term at zero energy.  P-hat(0) = -Delta on r^-q Y_l has the indicial roots q = -l,
     l + 2 (n = 4).  For P-hat(sigma) u = f with f compactly supported, the formal expansion u = u_0 + sigma u_1 + sigma^2
     u_2 + ... has u_0 = m r^-2, u_1 = -i m r^-1, and the equation for u_2 has the source m r^-2, at the indicial root
     0 of l = 0: no power solves it, -(m/2) log r does.  So the expansion carries sigma^2 log sigma (one sigma-derivative
     is bounded, two are not).  Control: at n = 3 the same chain gives L_1 u_0 = 0 (no log; e^(i sigma r)/r is analytic).
  G3 (exact series) The free outgoing kernel of -Delta - sigma^2 on R^4, (i sigma/(8 pi r)) H_1^(1)(sigma r), is 1/(4
     pi^2 r^2) - (1/(8 pi^2)) sigma^2 log sigma + (smooth in sigma at order 2, and higher): the sigma^2 log sigma
     coefficient -1/(8 pi^2) is G2's -(m/2) at m = 1/(4 pi^2), independent of r.  Control: the n = 3 kernel
     e^(i sigma r)/(4 pi r) has no log term.
  G4 (exact) The source side.  (a) A cone source (support r <= t/4, |F| <= r^-a (r/t)^b, b > kappa + 1/2) lies in the
     L^2-in-time class with K+-weight kappa and sf-weight beta iff a > beta + 5/2 + kappa (round 2's B7 at kappa = 0).
     (b) Its time-Fourier transform obeys |F-hat(sigma, x)| <= (4^(1-b)/(b-1)) r^(1-a), in rho^beta L^2(dx) iff
     a > beta + 3: pointwise use in sigma costs 1/2 more than the L^2 use.  (c) The harmonic-gauge source has a = lambda_#
     + 1 - eta = 5/2 + delta_# - eta (GAUGEDECAY5 Proposition R3.2): (a) holds iff kappa < delta_# - beta - eta, (b)
     fails whenever delta_# <= 1/2 + beta + eta.  (d) The quasi-stationary response at a fixed point to the cone source:
     with the l = 0 zero-energy kernel ~ r'^-2, int_1^(t/4) r'^-2 r'^-a (r'/t)^b r'^3 dr' ~ (4^(a-b-2)/(b+2-a)) t^(2-a);
     with the l = 2 kernel ~ r'^-4 it is ~ (4^(a-b)/(b-a)) t^-a.  At a = 5/2 + delta_#: t^(-1/2-delta_#) for l = 0.
     Controls: (a) at kappa = a - beta - 5/2 the integral diverges; (b) at a = beta + 3 it diverges; (d) the l = 0
     exponent is not -a.

Labels: computed (exact, sympy).  Run: python3 checks/gdrate5.py
"""
import sys
from fractions import Fraction as Fr

import sympy as sp

ts, r, sig, m = sp.symbols("t_* r sigma m", positive=True)
mu = sp.Symbol("mu", positive=True)


def radial_box0_ts(phi, n, V=0, static=False):
    """scalar Box_0 = -|g|^-1/2 d_a |g|^1/2 g^ab d_b on phi(t_*, r) for the Kerr-Schild metric eta + V (dt - dr)^2 in
    spatial dimension n, written in (t_*, r) with t = t_* + r (outgoing); static=True: phi(t, r) in (t, r)"""
    gtt, gtr, grr = -1 - V, -V, 1 - V
    if static:
        Dt = lambda e: sp.diff(e, ts)
        Dr = lambda e: sp.diff(e, r)
    else:
        Dt = lambda e: sp.diff(e, ts)                 # d_t at fixed r = d_t*
        Dr = lambda e: sp.diff(e, r) - sp.diff(e, ts)  # d_r at fixed t = d_r|t* - d_t*
    pt_, pr_ = Dt(phi), Dr(phi)
    return -(Dt(r**(n - 1)*(gtt*pt_ + gtr*pr_)) + Dr(r**(n - 1)*(gtr*pt_ + grr*pr_)))/r**(n - 1)


def g1(control=False):
    u = sp.Function("u")(r)
    q = sp.Symbol("q", positive=True)
    out = {}
    for n in (4,):
        ex = sp.expand(sp.exp(sp.I*sig*ts)*radial_box0_ts(sp.exp(-sp.I*sig*ts)*u, n, static=control))
        ex = sp.expand(sp.simplify(ex))
        c1 = sp.simplify(ex.coeff(sig, 1))
        c2 = sp.simplify(ex.coeff(sig, 2))
        # L_1 := i * (coefficient of sigma), acting on u
        L1u = sp.simplify(sp.I*c1)
        L1rq = sp.simplify(L1u.subs(u, r**-q).doit()*r**(q + 1))
        out[n] = (L1u, c2, L1rq)
    L1u, c2, L1rq = out[4]
    ok = sp.simplify(L1rq + 2*(q - sp.Rational(3, 2))) == 0 and c2 == 0
    # with the mass: the sigma^2 coefficient
    exm = sp.expand(sp.simplify(sp.exp(sp.I*sig*ts)*radial_box0_ts(sp.exp(-sp.I*sig*ts)*u, 4, V=mu/r**2)))
    c2m = sp.simplify(exm.coeff(sig, 2))
    okm = c2m == 0 if not control else True             # dt - dr is null for g: no sigma^2 term in this t_*
    print("  G1%s: L_1 u = %s; L_1 r^-q = (%s) r^(-q-1), = -2(q - 3/2): %s; sigma^2 coefficient at mu = 0: %s; with the "
          "mass: %s" % (" control (static time t)" if control else "", L1u, L1rq, ok, c2, c2m), flush=True)
    return ok and okm


def chain(n):
    """the formal expansion u_0 + sigma u_1 + sigma^2 u_2 for P-hat(sigma) = -Delta - i sigma L_1 (l = 0, mu = 0)"""
    Lap = lambda e: sp.diff(e, r, 2) + (n - 1)/r*sp.diff(e, r)
    L1 = lambda e: 2*sp.diff(e, r) + (n - 1)/r*e
    u0 = m*r**(2 - n)
    s1 = sp.simplify(sp.I*L1(u0))                       # -Delta u_1 = i L_1 u_0
    a = sp.Symbol("a")
    if s1 == 0:
        u1 = sp.Integer(0)
    else:
        # power ansatz: s1 = c r^-k  ->  u1 = A r^(2-k)
        k = -sp.degree(sp.Poly(sp.simplify(s1*r**10), r)) + 10
        sol = sp.solve(sp.Eq(-Lap(a*r**(2 - k)), s1), a)
        u1 = sol[0]*r**(2 - k) if sol else None
    s2 = sp.simplify(sp.I*L1(u1)) if u1 is not None else None
    return u0, u1, s1, s2, Lap


def g2(control=False):
    q, l = sp.symbols("q l")
    if control:
        u0, u1, s1, s2, Lap = chain(3)
        print("  G2 control (n = 3): u_0 = %s, i L_1 u_0 = %s, u_1 = %s, source of u_2 = %s: a log is forced: %s"
              % (u0, s1, u1, s2, s2 != 0), flush=True)
        return s2 != 0
    Y = sp.Function("Y")
    ind = sp.factor(sp.expand(-(sp.diff(r**-q, r, 2) + 3/r*sp.diff(r**-q, r))*r**(q + 2) + l*(l + 2)))
    roots = sp.solve(ind, q)
    ok_roots = set(roots) == {-l, l + 2}
    u0, u1, s1, s2, Lap = chain(4)
    ok_chain = sp.simplify(u1 + sp.I*m/r) == 0 and sp.simplify(s2 - m/r**2) == 0
    A = sp.Symbol("A")
    no_power = sp.solve(sp.Eq(sp.simplify(-Lap(A*r**0)), s2), A) == []
    logsol = sp.simplify(-Lap(-m/2*sp.log(r)) - s2) == 0
    print("  G2: indicial roots of -Delta on r^-q Y_l: %s = {-l, l + 2}: %s; u_0 = %s, u_1 = %s, source of u_2 = %s: "
          "%s; no power r^0 solves it: %s; -(m/2) log r does: %s" % (roots, ok_roots, u0, u1, s2, ok_chain, no_power,
                                                                     logsol), flush=True)
    return ok_roots and ok_chain and no_power and logsol


def g3(control=False):
    z = sp.Symbol("z", positive=True)
    if control:
        K = sp.exp(sp.I*sig*r)/(4*sp.pi*r)
        ser = sp.series(K, sig, 0, 4).removeO()
        has_log = ser.has(sp.log)
        print("  G3 control (n = 3 kernel e^(i sigma r)/(4 pi r)): the expansion has a log term: %s" % has_log,
              flush=True)
        return has_log
    H = sp.besselj(1, z) + sp.I*sp.bessely(1, z)
    ser = sp.series(H, z, 0, 4).removeO()
    K = sp.expand((sp.I*sig/(8*sp.pi*r))*ser.subs(z, sig*r))
    K = sp.expand(sp.expand_log(K, force=True))
    lead = sp.simplify(K.coeff(sig, 0))
    logc = sp.simplify(sp.expand(K).coeff(sp.log(sig)).coeff(sig, 2))
    ok = sp.simplify(lead - 1/(4*sp.pi**2*r**2)) == 0 and sp.simplify(logc + 1/(8*sp.pi**2)) == 0
    print("  G3: kernel at sigma^0: %s; coefficient of sigma^2 log sigma: %s (= -1/(8 pi^2), independent of r: %s); "
          "G2's -(m/2) at m = 1/(4 pi^2): %s" % (lead, logc, ok, -sp.Rational(1, 2)/(4*sp.pi**2)), flush=True)
    return ok


def g4(control=False):
    tt, rr = sp.symbols("t r", positive=True)
    ok = True
    rows = []
    for (a, b, beta, kap) in [(Fr(27, 10), Fr(5, 2), Fr(1, 20), Fr(1, 10)), (Fr(26, 10), Fr(3), Fr(1, 50), Fr(1, 20)),
                              (Fr(33, 10), Fr(4), Fr(1, 4), Fr(1, 2))]:
        A, B, BE, KA = [sp.Rational(x.numerator, x.denominator) for x in (a, b, beta, kap)]
        if control:
            KA = A - BE - sp.Rational(5, 2)                        # (a) at the edge
        it = sp.integrate(tt**(2*KA)*(rr/tt)**(2*B), (tt, 2*rr, sp.oo))
        rexp = sp.simplify(sp.log(sp.simplify(rr**(2*BE - 2*A + 3)*it/it.subs(rr, 1)))/sp.log(rr))
        conv_a = rexp < -1
        pred_a = A > BE + sp.Rational(5, 2) + KA
        # (b) pointwise in sigma
        Fhat = sp.integrate(rr**(-A)*(rr/tt)**B, (tt, 4*rr, sp.oo))
        okF = sp.simplify(Fhat - 4**(1 - B)/(B - 1)*rr**(1 - A)) == 0
        AB = BE + 3 if control else A
        conv_b = 2*BE + 2*(1 - AB) + 3 < -1
        pred_b = AB > BE + 3
        # (d) quasi-stationary response
        I0 = sp.integrate(rr**-2*rr**(-A)*(rr/tt)**B*rr**3, (rr, 1, tt/4))
        c0 = sp.limit(sp.simplify(I0*tt**(A - 2)), tt, sp.oo)
        I2 = sp.integrate(rr**-4*rr**(-A)*(rr/tt)**B*rr**3, (rr, 1, tt/4))
        c2 = sp.limit(sp.simplify(I2*tt**A), tt, sp.oo)
        okd = sp.simplify(c0 - sp.Integer(4)**(A - B - 2)/(B + 2 - A)) == 0 and \
            (B <= A or sp.simplify(c2 - sp.Integer(4)**(A - B)/(B - A)) == 0)
        lzero_is_minus_a = sp.limit(sp.simplify(I0*tt**A), tt, sp.oo) not in (sp.oo,)
        rows.append((str(a), str(b), str(beta), str(KA), conv_a, pred_a, okF, conv_b, pred_b, okd))
        if control:
            ok &= conv_a or conv_b or lzero_is_minus_a
        else:
            ok &= conv_a == pred_a and conv_a and okF and conv_b == pred_b and okd
    # (c) the harmonic-gauge source
    okc = True
    for gam, e in [(Fr(1, 10), Fr(0)), (Fr(1, 5), Fr(1, 2)), (Fr(1, 3), Fr(1, 4))]:
        dsh = (1 - e)*gam
        for k in (1, 3, 5):
            beta, eta = dsh*Fr(k, 12), dsh*Fr(1, 12)
            a = Fr(5, 2) + dsh - eta
            kmax = a - beta - Fr(5, 2)
            okc &= kmax == dsh - beta - eta and kmax > 0
            okc &= (a > beta + 3) == (dsh > Fr(1, 2) + beta + eta)
    if control:
        print("  G4 control: at the edges the integrals converge, or the l = 0 response decays like t^-a: %s" % ok,
              flush=True)
        return ok
    print("  G4: (a, b, beta, kappa, (a) converges, predicted, (b) F-hat bound exact, (b) converges, predicted, (d) "
          "leading constants) = %s; (c) kappa_max = delta_# - beta - eta and the pointwise criterion at samples: %s"
          % (rows, okc), flush=True)
    return ok and okc


CHECKS = [("G1", g1), ("G2", g2), ("G3", g3), ("G4", g4)]


def main():
    only = sys.argv[1:]
    ok = True
    for name, fn in CHECKS:
        if only and name not in only:
            continue
        good = fn()
        ctl = fn(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    print("EXIT %d" % (0 if ok else 1))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
