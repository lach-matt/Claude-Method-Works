#!/usr/bin/env python3
"""past5.py -- Theorem P (the construction from past null infinity): the exact facts its proof uses
(N1STAR-PROOF.md section 9).  Labels: computed (exact, sympy; P7's cross-check by quadrature, mpmath).

X = (tau, x) in R x R^4, r = |x|, v = tau + r, g0 = eta + (mu/r^2) dv dv, L0 = d_tau - xhat.d_x, box~ = g0^{ab} d_a d_b
componentwise; t := 1 + tau0 - tau on the past region.  A profile is in E_p when it and its derivatives in X, under the
rotations and in th are O(r^-p) (section 9.2).

  P1 The past domain.  With h(tau) = kappa t^(-1/4), kappa > 0, the outer boundary {v + h(tau) = V_P} has
     g0^-1(dPhi, dPhi) = -2 h' - h'^2 (1 + mu/r^2) < 0, h' = (kappa/4) t^(-5/4): spacelike, with a margin that decays
     like t^(-5/4).  Control: kappa < 0 makes it timelike.
  P2 The operator near past null infinity.  In (v, r), g0^-1 has g^vv = 0, g^vr = 1, g^rr = 1 - mu/r^2, and for every
     p, every M(v) and every spherical harmonic Y of degree n on S^3 (Delta Y = -n(n + 2) Y), in Cartesian coordinates,
       box~ (r^-p M(v) Y) = Y [ (3 - 2p) r^(-p-1) M' + (p(p - 2) - n(n + 2)) r^(-p-2) M - mu p (p + 1) r^(-p-4) M ].
     At p = 3/2 the r^(-5/2) term is absent.  Checked for n = 0, 1, 2 with p symbolic.  Control: the operator of eta.
  P3 The leading wave.  The Cartesian components of the record's W_TT are r^(-3/2) F_ij(v, s, xhat) with s = v/lam the
     phase: r^(3/2) W_ij does not depend on r at fixed (v, s, xhat).  With P2 at p = 3/2, box~ W_TT is in E_(7/2) and
     d_r|_v W_TT in E_(5/2).  Control: amplitude r^-1.
  P4 The transport from past null infinity.  For p > 5/2, Z = -r^(1 - p) M / (p - 5/2) solves (d_r|_v + 3/(2r)) Z =
     r^-p M and r^(3/2) Z -> 0 as r -> oo; at p = 5/2 the solutions are r^(-3/2) (c + M log r).  Control: p = 2, whose
     solution of that form grows against r^(-3/2).
  P5 The stage-0 source.  The vv second harmonic of R^(0) (lead5.py L3) is r^-3 times a function of (v, th): in E_3,
     so chi, its transport solution with no radiation at past null infinity, is -2 r^-2 times a function of (v, th, s):
     in E_2 (P4 with p = 3).  Control: lead5's amplitude-r^-1 mutant.
  P6 The rotations.  Omega = x1 d_2 - x2 d_1 annihilates v and r, commutes with L0 and with box~ (on any function).
     Control: the boost tau d_1 + x1 d_tau, a symmetry of eta and not of g0.
  P7 The flux at past null infinity.  With the record's free data, P1 = lam A E H (2 c^2 cos(v/lam) - s^2
     sin(v/lam))/3, P2 = lam A E H (2 s^2 sin(v/lam) - c^2 cos(v/lam))/3 (the r^(3/2)-normalised wave; H^2 (c^4 + s^4)
     = 1), the flux density (4/3)(P1_v^2 + P1_v P2_v + P2_v^2) (the normalisation of Proposition 2.3, whose phase mean
     is mu') is (4/9) A^2 H^2 (c^4 C^2 + s^4 S^2 - c^2 s^2 C S), C and S the v-derivatives of lam E cos(v/lam) and
     lam E sin(v/lam).  (a) The S^3 moments, each integrated term by term over its partial fractions in z = cos 2th,
     are <H^2 c^4> = <H^2 s^4> = 1/2 and <H^2 c^2 s^2> = pi/4 - 1/2.  (b) The quadratic form above.  (c) So the sphere
     mean, the expanded density integrated one additive term at a time and again through the moments, is exactly
     (2/9) A^2 [E^2 + lam^2 E'^2 + (1 - pi/2)(-(E^2 - lam^2 E'^2) sin(2v/lam)/2 + lam E E' cos(2v/lam))]: (9.10).
     (d) mpmath quadrature in th on S^3's measure (30 digits; the wave differentiated in v for an explicit envelope,
     at three points, one the readers' (lam, A, E, E', v) = (0.1, 1.3, 0.7, 0.4, 1.1)) agrees with it to 1e-20.  (e)
     Its phase mean is (2/9) A^2 (E^2 + lam^2 E'^2), and its integral in v is (2/9) A^2 int (E^2 + lam^2 E'^2) plus
     (1 - pi/2) times the boundary terms (2/9) A^2 ((lam/4) E^2 cos(2v/lam) + (lam^2/4) E E' sin(2v/lam)) and the
     integral of (2/9) A^2 (lam^2/4)(E'^2 - E E'') sin(2v/lam), which is the v-derivative of a lam^3 term plus a lam^3
     integrand.  (f) Pointwise, the density is (2/9) A^2 (E^2 + lam^2 E'^2) plus H^2 (c^4 - s^4) and H^2 c^2 s^2 times
     v-derivatives of terms vanishing with E and E' and lam^2 integrands of O(lam^3) integral: after the shell the
     aspect it integrates is th-independent to O(lam^3), so every mean of it there, a node mean included, is the
     sphere mean (N1STAR-PROOF.md section 11.4).
     [corrected D618: the first P7 integrated the expanded density over z at once; sympy 1.14.0 then drops the pi term
     of <H^2 c^2 s^2>, returning -1/2, and P7 passed the first (9.10), whose oscillating coefficient was 1.]
     Controls: (1) the two quadratures in phase; (2) the first (9.10)'s coefficient 1 for 1 - pi/2, which the
     quadrature rejects; (3) the first P7's route, the expanded sum integrated at once: under sympy 1.14.0 it returns
     the first (9.10), and the quadrature and the moments reject it (a sympy that integrates the sum correctly makes
     this control pass, and the selftest says so); (4) the quadrature on the flat measure (2/pi) dth for S^3's.

  P8 The mollifier's commutator.  In the coordinates (tau, v, xhat) of the past slices, L0 = d_tau at fixed (v, xhat)
     and the radial part of box~ is -(1 + mu(v)/r^2) L0^2 - 2 d_v L0 + (3/r) d_v (d_v at fixed tau, r = v - tau),
     which is (9.5)'s (checked on explicit functions).  For the shift C f(tau, v) := f(tau, psi(tau, v)), exactly,
       [box~_rad, C] f = -L0( 2 (psi_v - 1) C d_v f ) + (3 psi_v/r - 3/(psi - tau)) C d_v f
                         - mu(v) (1/r^2 - 1/(psi - tau)^2) C L0^2 f + (mu(psi) - mu(v))/(psi - tau)^2 C L0^2 f
                         - (1 + mu/r^2) psi_tt C d_v f - (2 + (1 + mu/r^2) psi_t) psi_t C d_v^2 f
                         - 2 (1 + mu/r^2) psi_t C d_v L0 f:
     the part of the commutator without a decaying factor (1/r, mu/r^2, mu' through mu(psi) - mu(v), psi_t) is an
     exact L0-derivative.  Checked as a polynomial identity on e^(a tau + b v) (which fixes every coefficient of a
     second-order operator), for symbolic psi and mu, and in the case psi = psi(v), mu constant.  Controls: psi
     depending on tau with the psi_t terms left out; the mu(psi) - mu(v) term left out.

python3 past5.py [--selftest | --mutants]
"""
import sys

import sympy as sp

tau, mu, kap, tau0 = sp.symbols("tau mu kappa tau0", real=True)
r, v, p = sp.symbols("r v p", positive=True)
x = sp.symbols("x1:5", real=True)
R = sp.sqrt(sum(xi**2 for xi in x))
V = tau + R


def p1(control=0):
    t = 1 + tau0 - tau
    h = (-kap if control == 1 else kap)*t**sp.Rational(-1, 4)
    hp = sp.diff(h, tau)
    # g0^-1 = eta^-1 - (mu/r^2) L0 L0 on span{dtau, dr}, with L0(tau) = 1, L0(r) = -1
    q = lambda a, b: (-a[0]*b[0] + a[1]*b[1]) - mu/r**2*(a[0] - a[1])*(b[0] - b[1])
    dPhi = (1 + hp, 1)                                         # d(v + h) = (1 + h') dtau + dr
    val = sp.simplify(q(dPhi, dPhi))
    identity = sp.simplify(val - (-2*hp - hp**2*(1 + mu/r**2))) == 0
    rate = sp.simplify(hp - (-kap if control == 1 else kap)/4*t**sp.Rational(-5, 4)) == 0
    sub = {kap: sp.Rational(1, 3), tau0: 0, tau: -5, mu: 7, r: 9}
    return bool(identity and rate and val.subs(sub) < 0)


def box(f, flat=False):
    """box~ f = eta^ab d_a d_b f - (mu/r^2) L0 L0 f in Cartesian (tau, x)"""
    out = -sp.diff(f, tau, 2) + sum(sp.diff(f, xi, 2) for xi in x)
    if not flat:
        L0 = lambda u: sp.diff(u, tau) - sum(xi/R*sp.diff(u, xi) for xi in x)
        out -= mu/R**2*L0(L0(f))
    return out


def p2(control=0):
    Mf = sp.Function("M")
    ok = True
    for n, Y in ((0, sp.Integer(1)), (1, x[0]/R), (2, x[0]*x[1]/R**2)):
        f = R**-p*Mf(V)*Y
        lhs = box(f, flat=(control == 1))
        Mp = sp.Derivative(Mf(V), tau)                         # M'(v), as d_tau of M(tau + r)
        rhs = Y*((3 - 2*p)*R**(-p - 1)*Mp + (p*(p - 2) - n*(n + 2))*R**(-p - 2)*Mf(V)
                 - mu*p*(p + 1)*R**(-p - 4)*Mf(V))
        ok &= sp.simplify(sp.expand(lhs - rhs.doit())) == 0
    # the inverse metric in (v, r): g0 = -(1 - mu/r^2) dv^2 + 2 dv dr
    g = sp.Matrix([[-(1 - mu/r**2), 1], [1, 0]])
    ok &= sp.simplify(g.inv() - sp.Matrix([[0, 1], [1, 1 - mu/r**2]])) == sp.zeros(2)
    return bool(ok)


def p3(control=0):
    th, f1, f2, s, A, lam = sp.symbols("theta phi1 phi2 s A lam", real=True)
    E = sp.Function("E")(v)
    H = sp.Function("H")(th)
    c, sn = sp.cos(th), sp.sin(th)
    amp = r**-1 if control == 1 else r**sp.Rational(-3, 2)
    P1 = A*E*H*amp*(2*c**2*sp.cos(s) - sn**2*sp.sin(s))/3
    P2 = A*E*H*amp*(2*sn**2*sp.sin(s) - c**2*sp.cos(s))/3
    Wang = sp.diag(-2*r**2*(P1 + P2), 2*r**2*c**2*P1, 2*r**2*sn**2*P2)        # on (th, phi1, phi2)
    X4 = [r*c*sp.cos(f1), r*c*sp.sin(f1), r*sn*sp.cos(f2), r*sn*sp.sin(f2)]
    J = sp.Matrix(4, 4, lambda i, a: sp.diff(X4[i], [r, th, f1, f2][a]))      # dx^i / dy^a
    Ji = sp.simplify(J.inv())                                                 # dy^a / dx^i
    Wc = sp.zeros(4)
    for i in range(4):
        for j in range(4):
            Wc[i, j] = sum(Wang[a, b]*Ji[a + 1, i]*Ji[b + 1, j] for a in range(3) for b in range(3))
    # r^(3/2) W_ij at fixed (v, s, angles): no r-dependence (v enters only through E and s is held fixed)
    return all(sp.simplify(sp.diff(sp.simplify(Wc[i, j]*r**sp.Rational(3, 2)), r)) == 0
               for i in range(4) for j in range(i, 4))


def p4(control=0):
    Mv = sp.Symbol("M")
    pv = sp.Integer(2) if control == 1 else p
    Z = -r**(1 - pv)*Mv/(pv - sp.Rational(5, 2))
    solves = sp.simplify(sp.diff(Z, r) + 3*Z/(2*r) - r**-pv*Mv) == 0
    decays = sp.limit((r**sp.Rational(3, 2)*Z).subs(p, 3), r, sp.oo) == 0 if control == 0 else \
        sp.limit(r**sp.Rational(3, 2)*Z, r, sp.oo) == 0
    cc = sp.Symbol("c")
    Zlog = r**sp.Rational(-3, 2)*(cc + Mv*sp.log(r))
    log_ok = sp.simplify(sp.diff(Zlog, r) + 3*Zlog/(2*r) - r**sp.Rational(-5, 2)*Mv) == 0
    return bool(solves and decays and log_ok)


def p5(control=0):
    import lead5
    lead5.MUT.clear()
    if control == 1:
        lead5.MUT.add("r_minus_1")
    try:
        R0 = lead5.reduced_ricci(lead5.wave(with_chi=False))
        m = lead5.modes(R0[(0, 0)][1])
        return all(sp.simplify(sp.diff(sp.expand(cf*lead5.r**3), lead5.r)) == 0 and sp.simplify(cf) != 0
                   for cf in m[2])
    finally:
        lead5.MUT.clear()


def p6(control=0):
    F = sp.Function("F")(tau, *x)
    if control == 1:
        Om = lambda u: tau*sp.diff(u, x[0]) + x[0]*sp.diff(u, tau)
    else:
        Om = lambda u: x[0]*sp.diff(u, x[1]) - x[1]*sp.diff(u, x[0])
    L0 = lambda u: sp.diff(u, tau) - sum(xi/R*sp.diff(u, xi) for xi in x)
    ok = sp.simplify(Om(V)) == 0 and sp.simplify(Om(R)) == 0 if control == 0 else True
    ok &= sp.simplify(Om(L0(F)) - L0(Om(F))) == 0
    ok &= sp.simplify(sp.expand(Om(box(F)) - box(Om(F)))) == 0
    return bool(ok)


def p7(control=0):
    lam, A = sp.symbols("lam A", positive=True)
    z = sp.Symbol("z", real=True)                              # z = cos 2 th: c^2 = (1 + z)/2, s^2 = (1 - z)/2
    Ef = sp.Function("E")(v)
    E, Ep = sp.symbols("E Ep", real=True)                      # E(v) and E'(v), restored below
    ph = v/lam
    c2, s2 = (1 + z)/2, (1 - z)/2
    H2 = 2/(1 + z**2)                                          # the record's H: H^2 (c^4 + s^4) = 1

    def dv(a, b):                                              # d_v of lam E (a cos + b sin)(v/lam), over A H
        return E*(b*sp.cos(ph) - a*sp.sin(ph)) + lam*Ep*(a*sp.cos(ph) + b*sp.sin(ph))
    f = (1, 0) if control == 1 else (0, 1)                     # F = sin(v/lam), or cos in the control
    g = (1, 0)                                                 # G = cos(v/lam)
    P1v = dv(*[(2*c2*g[i] - s2*f[i])/3 for i in range(2)])
    P2v = dv(*[(2*s2*f[i] - c2*g[i])/3 for i in range(2)])
    q = sp.expand(sp.Rational(4, 3)*A**2*H2*(P1v**2 + P1v*P2v + P2v**2))
    ok = {}

    # the S^3 mean: cos th sin th dth = -dz/4 on [0, pi/2], total 1/2, so the mean is (1/2) int_{-1}^{1} dz, taken one
    # additive term at a time (the first P7 integrated the expanded sum at once: sympy 1.14.0 drops its pi term)
    def zmean(e):
        return sum(sp.integrate(t, (z, -1, 1)) for t in sp.Add.make_args(sp.expand(e)))/2
    if control == 3:
        def zmean(e):                                          # noqa: F811 -- the first P7's route
            return sp.integrate(sp.expand(e), (z, -1, 1))/2
    # (a) the three angular moments, each integrated over its partial fractions in z
    mom = [sum(sp.integrate(t, (z, -1, 1)) for t in sp.Add.make_args(sp.apart(sp.expand(H2*w), z)))/2
           for w in (c2**2, s2**2, c2*s2)]
    exact = (sp.Rational(1, 2), sp.Rational(1, 2), sp.pi/4 - sp.Rational(1, 2))
    ok["a moments"] = all(sp.simplify(m - w) == 0 for m, w in zip(mom, exact))
    # (b) the quadratic form: (4/3)(a^2 + ab + b^2) = (4/9) A^2 H^2 (c^4 C^2 + s^4 S^2 - c^2 s^2 C S), C and S the
    # v-derivatives of lam E cos(v/lam) and lam E sin(v/lam)
    Cv, Sv = dv(1, 0), dv(0, 1)
    ok["b form"] = sp.simplify(q - sp.expand(sp.Rational(4, 9)*A**2*H2*(c2**2*Cv**2 + s2**2*Sv**2 - c2*s2*Cv*Sv))) == 0
    # (c) the sphere mean, term by term, is the formula, and is the moments' route
    mean = zmean(q)
    k = sp.Rational(2, 9)*A**2
    kap = 1 if control == 2 else 1 - sp.pi/2                   # 1 - 2 <H^2 c^2 s^2>; control 2: the first (9.10)'s 1
    osc = -(E**2 - lam**2*Ep**2)*sp.sin(2*ph)/2 + lam*E*Ep*sp.cos(2*ph)
    want = k*(E**2 + lam**2*Ep**2 + kap*osc)
    ok["c mean = (9.10)"] = sp.simplify(sp.expand_trig(mean - want)) == 0
    momroute = sp.Rational(4, 9)*A**2*(mom[0]*Cv**2 + mom[1]*Sv**2 - mom[2]*Cv*Sv)
    ok["c mean = moments"] = sp.simplify(sp.expand_trig(mean - momroute)) == 0
    # (d) the cross-check by quadrature in th on S^3's measure 2 cos th sin th dth (control 4: the flat measure
    # (2/pi) dth), with H = (c^4 + s^4)^(-1/2) and the wave differentiated in v for an explicit envelope: at the
    # readers' point (lam, A, E, E', v) = (1/10, 13/10, 7/10, 2/5, 11/10) through a linear one, and at two more
    import mpmath as mp
    th = sp.Symbol("th", real=True)
    c, sn = sp.cos(th), sp.sin(th)
    Hth = (c**4 + sn**4)**sp.Rational(-1, 2)
    trig = (sp.cos(ph), sp.sin(ph))
    Fw, Gw = sum(f[i]*trig[i] for i in range(2)), sum(g[i]*trig[i] for i in range(2))
    wavy = sp.exp(sp.sin(v)/2)*(2 + sp.cos(3*v))
    pts = [({lam: sp.Rational(1, 10), A: sp.Rational(13, 10), v: sp.Rational(11, 10)},
            sp.Rational(7, 10) + sp.Rational(2, 5)*(v - sp.Rational(11, 10))),
           ({lam: sp.Rational(37, 100), A: sp.Rational(4, 5), v: sp.Rational(-3, 10)}, wavy),
           ({lam: sp.Rational(1, 7), A: sp.Integer(2), v: sp.Rational(5, 2)}, wavy)]
    dev, first = [], None
    with mp.workdps(30):
        wq = (lambda t: 2/mp.pi) if control == 4 else (lambda t: 2*mp.cos(t)*mp.sin(t))
        for pt, env in pts:
            P1 = lam*A*env*Hth*(2*c**2*Gw - sn**2*Fw)/3
            P2 = lam*A*env*Hth*(2*sn**2*Fw - c**2*Gw)/3
            dens = sp.Rational(4, 3)*(sp.diff(P1, v)**2 + sp.diff(P1, v)*sp.diff(P2, v) + sp.diff(P2, v)**2)
            fq = sp.lambdify(th, dens.subs(pt), "mpmath")
            quad = mp.quad(lambda t: fq(t)*wq(t), [0, mp.pi/4, mp.pi/2])
            ev = {E: env.subs(v, pt[v]), Ep: sp.diff(env, v).subs(v, pt[v]), **pt}
            dev += [abs(quad - mp.mpf(sp.N(mean.subs(ev), 40))), abs(quad - mp.mpf(sp.N(want.subs(ev), 40)))]
            if first is None:
                first = (mp.nstr(quad, 12), mp.nstr(mp.mpf(sp.N(want.subs(ev), 40)), 12),
                         mp.nstr(mp.mpf(sp.N((k*(E**2 + lam**2*Ep**2 + osc)).subs(ev), 40)), 12))
        devmax = mp.nstr(max(dev), 3)
    ok["d quadrature"] = max(dev) < 1e-20
    # (e) its integral in v: k int (E^2 + lam^2 E'^2) plus kap times the boundary terms k (lam/4) E^2 cos(2v/lam) + k
    # (lam^2/4) E E' sin(2v/lam) and the integral of k (lam^2/4)(E'^2 - E E'') sin(2v/lam); that integrand is the
    # v-derivative of -k (lam^3/8)(E'^2 - E E'') cos(2v/lam) plus k (lam^3/8)(E'^2 - E E'')' cos(2v/lam): O(lam^3)
    meanf = mean.subs({E: Ef, Ep: sp.diff(Ef, v)})
    bound = k*(lam/4*Ef**2*sp.cos(2*ph) + lam**2/4*Ef*sp.diff(Ef, v)*sp.sin(2*ph))
    gg = sp.diff(Ef, v)**2 - Ef*sp.diff(Ef, v, 2)
    rest = k*lam**2/4*gg*sp.sin(2*ph)
    ok["e integral"] = sp.simplify(sp.expand(meanf - k*(Ef**2 + lam**2*sp.diff(Ef, v)**2) - kap*sp.diff(bound, v)
                                             - kap*rest)) == 0
    ok["e lam^3"] = sp.simplify(sp.expand(rest - sp.diff(-k*lam**3/8*gg*sp.cos(2*ph), v)
                                          - k*lam**3/8*sp.diff(gg, v)*sp.cos(2*ph))) == 0
    # (f) pointwise: q = k (E^2 + lam^2 E'^2) + k H^2 ((c^4 - s^4) (B1' + (lam^2/2) gg cos(2v/lam)) - 2 c^2 s^2 (B2'
    # + (lam^2/4) gg sin(2v/lam))), B1 = -(lam/2) E^2 sin(2v/lam) + (lam^2/2) E E' cos(2v/lam), B2 = bound/k: after
    # the shell (E = E' = 0) the aspect is th-independent to O(lam^3), so every mean of it is the sphere mean there
    qf = q.subs({E: Ef, Ep: sp.diff(Ef, v)})
    B1 = -lam/2*Ef**2*sp.sin(2*ph) + lam**2/2*Ef*sp.diff(Ef, v)*sp.cos(2*ph)
    point = k*(Ef**2 + lam**2*sp.diff(Ef, v)**2) + k*H2*((c2**2 - s2**2)*(sp.diff(B1, v) + lam**2/2*gg*sp.cos(2*ph))
                                                         - 2*c2*s2*(sp.diff(bound/k, v) + lam**2/4*gg*sp.sin(2*ph)))
    ok["f pointwise"] = sp.simplify(sp.expand(qf - sp.expand(point))) == 0
    import textwrap

    def say(msg):
        print(textwrap.fill(msg, width=121, initial_indent="      ", subsequent_indent="        ",
                            break_on_hyphens=False), flush=True)
    if control == 0:
        say("P7: <H^2 c^4>, <H^2 s^4>, <H^2 c^2 s^2> = %s (term by term, partial fractions in z)"
            % ", ".join(str(sp.simplify(m)) for m in mom))
        say("P7: the oscillating coefficient 1 - 2 <H^2 c^2 s^2> = 1 - pi/2 = %.10f; quadrature on S^3 at three points: "
            "max deviation %s at 30 digits (tolerance 1e-20)" % (float(1 - sp.pi/2), devmax))
        say("P7: at (lam, A, E, E', v) = (0.1, 1.3, 0.7, 0.4, 1.1): quadrature %s, (9.10) %s, the first (9.10) %s"
            % first)
        say("P7: checks " + ", ".join(f"{a} {b}" for a, b in ok.items()))
    else:
        say("P7 control %d: failing checks %s" % (control, [a for a, b in ok.items() if not b]))
    return bool(all(ok.values()))


def p8(control=0):
    t_, v_, y, a, b, mu0 = sp.symbols("t_ v_ y a b mu0", real=True)
    M = sp.Function("mu")

    def identity(time_dep, mu_dep, with_resid=True, drop=None):
        P = sp.Function("psi")(t_, v_) if time_dep else sp.Function("psi")(v_)
        mu = (lambda q: M(q)) if mu_dep else (lambda q: mu0)            # noqa: E731
        rr = v_ - t_
        g = sp.exp(a*t_ + b*y)
        box_rad = lambda w: -(1 + mu(v_)/rr**2)*sp.diff(w, t_, 2) - 2*sp.diff(w, v_, t_) + 3/rr*sp.diff(w, v_)  # noqa
        lhs = box_rad(g.subs(y, P))
        fb = (-(1 + mu(y)/(y - t_)**2)*sp.diff(g, t_, 2) - 2*sp.diff(g, y, t_) + 3/(y - t_)*sp.diff(g, y)).subs(y, P)
        C = lambda e: e.subs(y, P)                                        # noqa: E731
        dv, dv2, dvL0, L02 = C(sp.diff(g, y)), C(sp.diff(g, y, 2)), C(sp.diff(g, y, t_)), C(sp.diff(g, t_, 2))
        psv, pst, pstt = sp.diff(P, v_), sp.diff(P, t_), sp.diff(P, t_, 2)
        pred = (-sp.diff(2*(psv - 1)*dv, t_) + (3*psv/rr - 3/(P - t_))*dv - mu(v_)*(1/rr**2 - 1/(P - t_)**2)*L02)
        terms = [(mu(P) - mu(v_))/(P - t_)**2*L02, -(1 + mu(v_)/rr**2)*pstt*dv,
                 -(2 + (1 + mu(v_)/rr**2)*pst)*pst*dv2, -2*(1 + mu(v_)/rr**2)*pst*dvL0]
        if with_resid:
            pred += sum(q for i, q in enumerate(terms) if i != drop)
        return sp.simplify(sp.expand((lhs - fb - pred)*sp.exp(-a*t_ - b*P))) == 0
    if control == 1:
        ok = identity(True, False, with_resid=False)
    elif control == 2:
        ok = identity(True, True, drop=0)
    else:
        ok = identity(True, True) and identity(False, False, with_resid=False)
    V, R = sp.symbols("V R", real=True)
    rr = v_ - t_
    box_c = lambda w: -(1 + mu0/rr**2)*sp.diff(w, t_, 2) - 2*sp.diff(w, v_, t_) + 3/rr*sp.diff(w, v_)  # noqa: E731
    for G in (sp.exp(t_/3)*sp.sin(2*v_) + t_**3*v_**2, sp.cos(t_*v_) + v_/(1 + t_**2)):
        W = G.subs({t_: V - R, v_: V}, simultaneous=True)
        f95 = 2*sp.diff(W, R, V) + 3/R*(sp.diff(W, V) + sp.diff(W, R)) + (1 - mu0/R**2)*sp.diff(W, R, 2)
        ok &= sp.simplify(f95 - box_c(G).subs({t_: V - R, v_: V}, simultaneous=True)) == 0
    return bool(ok)


CHECKS = [("P1 the outer boundary of the past domain is spacelike, margin (kappa/2) t^(-5/4)", p1, 1),
          ("P2 box~ (r^-p M(v) Y): no r^(-5/2) term at p = 3/2; g0^-1 in (v, r)", p2, 1),
          ("P3 the Cartesian components of W_TT are r^(-3/2) F(v, s, xhat)", p3, 1),
          ("P4 the transport from past null infinity: r^-p source, p > 5/2, gives r^(1-p); a log at 5/2", p4, 1),
          ("P5 the stage-0 vv second harmonic is r^-3 times a function of (v, th): chi in E_2", p5, 1),
          ("P6 the rotations annihilate v and r and commute with L0 and box~", p6, 1),
          ("P7 the sphere-mean flux of the record's radiation field (term by term; quadrature), its v-integral", p7, 4),
          ("P8 the shift's commutator with box~ is -L0(X) plus terms with decaying factors", p8, 2)]


def selftest():
    ok_all = True
    for name, f, nc in CHECKS:
        good = f()
        control = any(f(control=k) for k in range(1, nc + 1))
        state = "PASS" if good and not control else "FAIL"
        ok_all &= state == "PASS"
        print(f"{name:<100} {state}" + ("" if not control else "  (control passed: vacuous)"), flush=True)
    print(f"past5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, f, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            m = f(control=k)
            caught += (not m)
            print(f"mutant {k} of {name[:2]}: {'caught' if not m else 'NOT caught'}")
    print(f"past5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest() else 1)
