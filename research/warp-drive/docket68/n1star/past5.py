#!/usr/bin/env python3
"""past5.py -- Theorem P (the construction from past null infinity): the exact facts its proof uses
(N1STAR-PROOF.md section 9).  Labels: computed (exact, sympy).

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
     sin(v/lam))/3, P2 = lam A E H (2 s^2 sin(v/lam) - c^2 cos(v/lam))/3 (the r^(3/2)-normalised wave), the sphere
     mean of the flux density (4/3)(P1_v^2 + P1_v P2_v + P2_v^2) (the normalisation of Proposition 2.3, whose phase
     mean is mu') is exactly (2/9) A^2 [E^2 + lam^2 E'^2 - (E^2 - lam^2 E'^2) sin(2v/lam)/2 + lam E E' cos(2v/lam)];
     its phase mean is (2/9) A^2 (E^2 + lam^2 E'^2), and its integral in v is (2/9) A^2 int (E^2 + lam^2 E'^2) plus
     the boundary terms (2/9) A^2 ((lam/4) E^2 cos(2v/lam) + (lam^2/4) E E' sin(2v/lam)) plus the integral of
     (2/9) A^2 (lam^2/4)(E'^2 - E E'') sin(2v/lam), which is O(lam^3).  Control: the two quadratures in phase.

  P8 The mollifier's commutator.  In the coordinates (tau, v, xhat) of the past slices, L0 = d_tau at fixed (v, xhat)
     and the radial part of box~ is -(1 + mu/r^2) L0^2 - 2 d_v L0 + (3/r) d_v (d_v at fixed tau, r = v - tau), which is
     (9.5)'s (checked on explicit functions).  The shift of Lemma 9.4, C f(tau, v) := f(tau, psi(v)) with psi independent
     of tau, satisfies exactly
       [box~_rad, C] f = -L0( 2 (psi' - 1) C d_v f ) + (3 psi'/r - 3/(psi - tau)) C d_v f
                         - mu (1/r^2 - 1/(psi - tau)^2) C L0^2 f:
     the part of the commutator without a decaying factor is an exact L0-derivative.  Control: psi depending on tau.

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
    H2 = 2/(1 + z**2)

    def dv(a, b):                                              # d_v of lam E (a cos + b sin)(v/lam), over A H
        return E*(b*sp.cos(ph) - a*sp.sin(ph)) + lam*Ep*(a*sp.cos(ph) + b*sp.sin(ph))
    f = (1, 0) if control == 1 else (0, 1)                     # F = sin(v/lam), or cos in the control
    g = (1, 0)                                                 # G = cos(v/lam)
    P1v = dv(*[(2*c2*g[i] - s2*f[i])/3 for i in range(2)])
    P2v = dv(*[(2*s2*f[i] - c2*g[i])/3 for i in range(2)])
    q = sp.Rational(4, 3)*A**2*H2*(P1v**2 + P1v*P2v + P2v**2)
    # the S^3 mean: cos th sin th dth = -dz/4 on [0, pi/2], total 1/2, so the mean is (1/2) int_{-1}^{1} dz
    mean = sp.integrate(sp.expand(q), (z, -1, 1))/2
    k = sp.Rational(2, 9)*A**2
    want = k*(E**2 + lam**2*Ep**2 - (E**2 - lam**2*Ep**2)*sp.sin(2*ph)/2 + lam*E*Ep*sp.cos(2*ph))
    ok = sp.simplify(sp.expand_trig(mean - want)) == 0
    # its integral in v: k int (E^2 + lam^2 E'^2), the boundary terms k (lam/4) E^2 cos(2v/lam) + k (lam^2/4) E E'
    # sin(2v/lam), and the integral of k (lam^2/4)(E'^2 - E E'') sin(2v/lam), which is O(lam^3)
    meanf = mean.subs({E: Ef, Ep: sp.diff(Ef, v)})
    bound = k*(lam/4*Ef**2*sp.cos(2*ph) + lam**2/4*Ef*sp.diff(Ef, v)*sp.sin(2*ph))
    rest = k*lam**2/4*(sp.diff(Ef, v)**2 - Ef*sp.diff(Ef, v, 2))*sp.sin(2*ph)
    ok &= sp.simplify(sp.expand(meanf - k*(Ef**2 + lam**2*sp.diff(Ef, v)**2) - sp.diff(bound, v) - rest)) == 0
    return bool(ok)


def p8(control=0):
    t_, v_, mu_, y = sp.symbols("t_ v_ mu_ y", real=True)
    f = sp.Function("f")
    P = sp.Function("psi")(t_, v_) if control == 1 else sp.Function("psi")(v_)
    rr = v_ - t_
    box_rad = lambda w: -(1 + mu_/rr**2)*sp.diff(w, t_, 2) - 2*sp.diff(w, v_, t_) + 3/rr*sp.diff(w, v_)  # noqa: E731
    lhs = box_rad(f(t_, P))
    fb = -(1 + mu_/(y - t_)**2)*sp.diff(f(t_, y), t_, 2) - 2*sp.diff(f(t_, y), y, t_) + 3/(y - t_)*sp.diff(f(t_, y), y)
    Cdvf = sp.diff(f(t_, y), y).subs(y, P)
    CL02 = sp.diff(f(t_, y), t_, 2).subs(y, P)
    pred = (-sp.diff(2*(sp.diff(P, v_) - 1)*Cdvf, t_) + (3*sp.diff(P, v_)/rr - 3/(P - t_))*Cdvf
            - mu_*(1/rr**2 - 1/(P - t_)**2)*CL02)
    ok = sp.simplify(sp.expand(lhs - fb.subs(y, P) - pred)) == 0
    V, R = sp.symbols("V R", real=True)
    for G in (sp.exp(t_/3)*sp.sin(2*v_) + t_**3*v_**2, sp.cos(t_*v_) + v_/(1 + t_**2)):
        W = G.subs({t_: V - R, v_: V}, simultaneous=True)
        f95 = 2*sp.diff(W, R, V) + 3/R*(sp.diff(W, V) + sp.diff(W, R)) + (1 - mu_/R**2)*sp.diff(W, R, 2)
        ok &= sp.simplify(f95 - box_rad(G).subs({t_: V - R, v_: V}, simultaneous=True)) == 0
    return bool(ok)


CHECKS = [("P1 the outer boundary of the past domain is spacelike, margin (kappa/2) t^(-5/4)", p1, 1),
          ("P2 box~ (r^-p M(v) Y): no r^(-5/2) term at p = 3/2; g0^-1 in (v, r)", p2, 1),
          ("P3 the Cartesian components of W_TT are r^(-3/2) F(v, s, xhat)", p3, 1),
          ("P4 the transport from past null infinity: r^-p source, p > 5/2, gives r^(1-p); a log at 5/2", p4, 1),
          ("P5 the stage-0 vv second harmonic is r^-3 times a function of (v, th): chi in E_2", p5, 1),
          ("P6 the rotations annihilate v and r and commute with L0 and box~", p6, 1),
          ("P7 the sphere-mean flux of the record's radiation field, and its integral in v", p7, 1),
          ("P8 the shift's commutator with box~ is -L0(X) plus terms with decaying factors", p8, 1)]


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
