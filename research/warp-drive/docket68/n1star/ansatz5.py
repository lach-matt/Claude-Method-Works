#!/usr/bin/env python3
"""ansatz5.py -- N1*, route W, step 1: the geometric-optics ansatz on five-dimensional Vaidya with the phase v.

Commissioned at item 522 (N1STAR-LOG.md).  Route W carries Touati's construction (Commun. Math. Phys. 402 (2023)
3109, arXiv:2206.12318) to 4+1 dimensions and to the large background.  Its first step, as the instructions state it:
"The ansatz to order lam^2 on Vaidya with the ingoing phase v (null for g0).  Find the 5D polarization conditions and
the 5D energy condition, the analogue of Touati's (2.28).  Check them against F3's computed dust identity."
Labels: computed (exact, sympy, unless marked), READ (verbatim at source, 2026-10-19), deduced, OPEN.

  A0 (READ) Touati's structure, arXiv:2206.12318v4.  Ricci in any coordinates (3.1): 2R = -box~ g + H d g
     + g d H + P(g)(dg, dg); the polarization tensor (3.5): Pol_s(S) = g0^{mn}(d_m u S_sn - (1/2) d_s u S_mn); the
     quadratic form Q(T, S) of section 3.1.2 and the identity (3.17): "Q(T, T) = E(T, T) du du + g^{ns} d_(a u
     Pol_s(T) T_b)n - Pol_a(T) Pol_b(T)", with (3.19) "E(T, S) = 1/4 (tr T)(tr S) - 1/2 |T.S|"; the polarization,
     energy and transport conditions of Theorem 2.2 ((2.27)-(2.29)): "(1/8)|F1|^2 - (1/16)(tr F1)^2 = F0^2",
     "2 du.D F1 + (box u) F1 = 0".
  A1 (computed, exact) The weak polarized null condition holds in 4+1 dimensions.  Touati's (3.17) and (3.18) are
     verified symbolically for a general symmetric T (and S) on five-dimensional Minkowski space with a null phase;
     with Pol(T) = 0, Q(T, T) = E(T, T) du du (fully non-tangential) and E(T, T) = -(1/2) |T_AB|^2 on the three
     transverse directions (Touati's Remark 3.1, with A, B now running over three).  Nothing in the identity uses
     the dimension.
  A2 (computed, exact) The background.  Five-dimensional Vaidya, g0 = -(1 - mu(v)/r^2) dv^2 + 2 dv dr
     + r^2 (dth^2 + cos^2 th dphi1^2 + sin^2 th dphi2^2): Ric(g0) = F0^2 dv dv with F0^2 = 3 mu'/(2 r^3); g0^-1(dv, dv)
     = 0; L0 = -g0^-1 dv = -d_r is null and geodesic; box v = 3/r.
  A3 (computed, exact) The record's first-order wave.  With y^6 = r^-3 and the record's free data
     (F = lam A env h sin(v/lam), G = lam A env h cos(v/lam)), P1 = y^3 (2 c^2 G - s^2 F)/3,
     P2 = y^3 (2 s^2 F - c^2 G)/3,
     the metric perturbation g1 = r^2 diag(-2(P1 + P2), 2 c^2 P1, 2 s^2 P2)/lam on (th, phi1, phi2) is traceless and
     transverse: Pol(g1) = 0 and g1(L0, .) = 0 -- Touati's (2.27) in 5D.  Its amplitude solves the transport (2.29),
     2 D_r F1 + (3/r) F1 = 0 (orthonormal amplitude ~ r^(-3/2)), and it is smooth at both axes (P1 + 2 P2 = 0 at
     th = 0, 2 P1 + P2 = 0 at th = pi/2).
  A4 (computed, exact; two-scale) The ansatz to order lam^2.  Ricci of g0 + lam g1 + lam^2 g2 is expanded in lam
     with the fast phase s = v/lam (d_v -> d_v + lam^-1 d_s).  R^(-1) = 0 in every component.  R^(0) = 0 in every
     component exactly when (a) mu' = (2/9) A^2 env^2 H^2 (c^4 + s^4) -- with the record's h, H^2 (c^4 + s^4) = 1, so
     mu' = (2/9) A^2 env^2: F3's dust identity and Isaacson's flux, now from the wave-type ansatz -- and (b) g2 carries
     two polarization terms: a second harmonic r^2 B (dth^2 + c^2 dphi1^2 + s^2 dphi2^2), B = bc cos 2s + bs sin 2s,
     bc = -A^2 E^2 H^2 cos 2th/(18 r^3), bs = A^2 E^2 H^2 (1 - cos 4th)/(144 r^3) (Touati's Pol(F^(2,2)) ~ E du), and a
     first harmonic K (dr dth + dth dr), K = kc cos s + ks sin s, kc = -(A E/(3 r^(3/2))) (5 H sin 2th
     + 2 sin^2 th H'), ks = (A E/(3 r^(3/2))) (-5 H sin 2th + 2 cos^2 th H').  Both are smooth on S^3 (B multiplies the
     round metric; K dth is a function of x = cos 2th times dx).  This is the 5D energy condition: Touati's (2.28)
     holds verbatim, with the two quadratures averaged, (1/16)(|F_c|^2 + |F_s|^2) = F0^2.
  A5 (computed, exact) What R^(1) holds, and what is new.  At order lam the tangential components (th th, phi phi)
     hold first harmonics only (the transport of g2's transverse-traceless part, Touati's (2.56)); the components
     with a v index hold first and second harmonics (non-tangential: Touati's Pol(g3), Remark 2.6).  And one
     non-oscillating term, absent from Touati's ansatz: R^(1)_v th = -A^2 E^2 H^2 sin 2th/(6 r^3).  It is
     F0^2 d_th phi with phi = (1/2) arctan(cos 2th), a smooth function on S^3: to order lam the averaged stress is
     F0^2 d(v + lam phi) d(v + lam phi), the dust's direction tilted at O(lam).  It comes from the two quadratures (the
     record needs both for a round average, F3); for Touati's single-cosine ansatz it vanishes identically (checked
     here).  It is not absorbed by any oscillating corrector: closing R^(1) needs a mean O(lam) metric correction lam m1
     solving the linearized equations on Vaidya with this source.  Its angular mean on S^3 vanishes (arctan is odd in
     x), consistent with the record's mean mass converging at O(lam^2) while the horizon converges at O(lam) (F4).
     Constructing m1 (with g2's transported parts and g3) is OPEN here.

So step 1 of route W is settled to order lam^0 (polarization, energy condition, dust identity, the second-order
polarization terms, axis regularity), and its order-lam structure is measured, with one new term named.  N1* itself
is not proved by this instrument (see N1STAR-STATUS.md).  Imports nothing from the tree.  sympy.
python3 ansatz5.py [--selftest | --mutants]
"""
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
MUT = set()
MUTANTS = {"trace_in_g1": "g1 given a trace on the transverse block: Pol(g1) != 0 (A3, A4: R^(-1) != 0)",
           "r_minus_1": "the amplitude ~ r^-1 in place of r^-3/2: the transport fails (A3, A4)",
           "no_pol_g2": "g2's polarization terms B and K dropped: R^(0) != 0 (A4)",
           "in_phase": "the two polarizations in phase, not a quarter turn apart: the average is not round (A4)",
           "identity_4d_only": "Touati's identity checked with a dimension-dependent coefficient (A1)"}

v, r, th, p1, p2, s, lam, A = sp.symbols("v r theta phi1 phi2 s lam A", real=True)
X = [v, r, th, p1, p2]
Mf = sp.Function("M")(v)
Ef = sp.Function("E")(v)
Hf = sp.Function("H")(th)
C, S = sp.cos(th), sp.sin(th)
H_REC = sp.sqrt(2/(1 + sp.cos(2*th)**2))           # the record's h(x), x = cos 2th


# ---------------------------------------------------------------------------------------------------------- A1
def a1():
    """Touati's (3.17)/(3.18) in d+1 dimensions for general symmetric T, S; Minkowski with the null phase t - x1"""
    out = {}
    for d in (3, 4):
        n = d + 1
        eta = sp.diag(*([-1] + [1]*d))
        ei = eta.inv()
        du = [1, -1] + [0]*(n - 2)                    # u = t - x1: null
        T = sp.Matrix(n, n, lambda i, j: sp.Symbol("T%d%d" % (min(i, j), max(i, j))))
        Sm = sp.Matrix(n, n, lambda i, j: sp.Symbol("S%d%d" % (min(i, j), max(i, j))))

        def Q(T_, S_, a, b):
            e = 0
            for m in range(n):
                for p in range(n):
                    for nn in range(n):
                        for sg in range(n):
                            gg = ei[m, p]*ei[nn, sg]
                            if gg == 0:
                                continue
                            e += gg*(du[a]*T_[p, sg]*du[m]*S_[b, nn] + du[b]*T_[p, sg]*du[m]*S_[a, nn]
                                     - sp.Rational(1, 2)*du[a]*T_[p, sg]*du[b]*S_[m, nn]
                                     - du[p]*T_[a, nn]*du[sg]*S_[b, m])
            return sp.expand(e)

        def pol(T_):
            tr = sum(ei[m, nn]*T_[m, nn] for m in range(n) for nn in range(n))
            return [sp.expand(sum(ei[m, nn]*du[m]*T_[sg, nn] for m in range(n) for nn in range(n))
                              - sp.Rational(1, 2)*du[sg]*tr) for sg in range(n)]

        def E(T_, S_):
            trT = sum(ei[m, nn]*T_[m, nn] for m in range(n) for nn in range(n))
            trS = sum(ei[m, nn]*S_[m, nn] for m in range(n) for nn in range(n))
            dot = sum(ei[a, b]*ei[m, nn]*T_[a, m]*S_[b, nn] for a in range(n) for b in range(n) for m in range(n)
                      for nn in range(n))
            k = sp.Rational(1, 4)*(sp.Rational(d, 3) if "identity_4d_only" in MUT and d == 4 else 1)
            return sp.expand(k*trT*trS - sp.Rational(1, 2)*dot)
        PT, PS = pol(T), pol(Sm)
        ok17 = ok18 = True
        for a in range(n):
            for b in range(a, n):
                rhs17 = (E(T, T)*du[a]*du[b] + sum(ei[nn, sg]*(du[a]*PT[sg]*T[b, nn] + du[b]*PT[sg]*T[a, nn])
                                                   for nn in range(n) for sg in range(n)) - PT[a]*PT[b])
                ok17 &= sp.expand(Q(T, T, a, b) - rhs17) == 0
                rhs18 = (2*E(T, Sm)*du[a]*du[b]
                         + sum(ei[nn, sg]*(du[a]*(PT[sg]*Sm[b, nn] + PS[sg]*T[b, nn])
                                           + du[b]*(PT[sg]*Sm[a, nn] + PS[sg]*T[a, nn]))
                               for nn in range(n) for sg in range(n))
                         - (PT[a]*PS[b] + PT[b]*PS[a]))
                ok18 &= sp.expand(Q(T, Sm, a, b) + Q(Sm, T, a, b) - rhs18) == 0
        # Pol(T) = 0 is n linear conditions; they force the transverse trace to vanish and leave T_00 free.  Solved for
        # T_01, T_0A and T_22; then E(T,T) = -1/2 |T_AB|^2 over the d-1 transverse directions (Touati's Remark 3.1)
        trans = list(range(2, n))
        unk = [sp.Symbol("T0%d" % i) for i in range(1, n)] + [sp.Symbol("T22")]
        sol = sp.solve(pol(T), unk, dict=True)
        Tq = T.subs(sol[0])
        Eq = E(Tq, Tq)
        tt = sum(Tq[i, j]**2 for i in trans for j in trans)
        out[d] = dict(ok17=ok17, ok18=ok18, energy=sp.expand(Eq + sp.Rational(1, 2)*tt) == 0,
                      pol_zero=all(sp.expand(x) == 0 for x in pol(Tq)))
    return out


# ---------------------------------------------------------------------------------------------------------- A2
def _christoffel(g, gi, n, D):
    dg = [[[D(g[a, b], k) for k in range(n)] for b in range(n)] for a in range(n)]
    return [[[sum(gi[a, d_]*(dg[d_][b][c] + dg[d_][c][b] - dg[b][c][d_]) for d_ in range(n))/2 for c in range(n)]
             for b in range(n)] for a in range(n)]


def _ricci(G, n, D, post=lambda e: e):
    def R(b, c):
        e = 0
        for a in range(n):
            e += D(G[a][b][c], a) - D(G[a][b][a], c)
            for d_ in range(n):
                e += G[a][a][d_]*G[d_][b][c] - G[a][c][d_]*G[d_][b][a]
        return post(e)
    return R


def background():
    f = 1 - Mf/r**2
    g = sp.diag(-f, 0, r**2, r**2*C**2, r**2*S**2)
    g[0, 1] = g[1, 0] = 1
    return g, f


def a2():
    g, f = background()
    gi = sp.simplify(g.inv())
    D = lambda e, k: sp.diff(e, X[k])
    G = _christoffel(g, gi, 5, D)
    G = [[[sp.simplify(x) for x in row] for row in M2] for M2 in G]
    R = _ricci(G, 5, D, sp.simplify)
    ric = {(i, j): sp.simplify(R(i, j)) for i in range(5) for j in range(i, 5)}
    F02 = sp.Rational(3, 2)*sp.diff(Mf, v)/r**3
    dust = all(sp.simplify(e - (F02 if k == (0, 0) else 0)) == 0 for k, e in ric.items())
    eik = sp.simplify(gi[0, 0]) == 0
    L = [-gi[0, k] for k in range(5)]                 # L0^a = -g^{a v}
    geo = all(sp.simplify(sum(L[b]*sp.diff(L[a], X[b]) for b in range(5))
                          + sum(G[a][b][c]*L[b]*L[c] for b in range(5) for c in range(5))) == 0 for a in range(5))
    sq = r**3*C*S
    boxv = sp.simplify(sum(sp.diff(sq*gi[m, 0], X[m]) for m in range(5))/sq)
    return dict(dust=dust, eik=eik, L=[sp.simplify(x) for x in L], geodesic=geo, boxv=boxv)


# ---------------------------------------------------------------------------------------------------------- A3/A4
def _waves(H=Hf):
    y3 = r**sp.Rational(-3, 2)
    if "r_minus_1" in MUT:
        y3 = r**-1
    cf, sf = sp.cos(s), sp.sin(s)
    Gq, Fq = cf, sf                                   # G ~ cos(v/lam), F ~ sin(v/lam)
    if "in_phase" in MUT:
        Fq = cf
    a1_ = A*Ef*H*y3*(2*C**2*Gq - S**2*Fq)/3
    a2_ = A*Ef*H*y3*(2*S**2*Fq - C**2*Gq)/3
    return a1_, a2_


def g2_terms(H=Hf):
    Hp = sp.diff(H, th)
    bc = -A**2*Ef**2*H**2*sp.cos(2*th)/(18*r**3)
    bs = A**2*Ef**2*H**2*(1 - sp.cos(4*th))/(144*r**3)
    kc = -(A*Ef/(3*r**sp.Rational(3, 2)))*(5*H*sp.sin(2*th) + 2*S**2*Hp)
    ks = (A*Ef/(3*r**sp.Rational(3, 2)))*(-5*H*sp.sin(2*th) + 2*C**2*Hp)
    return bc, bs, kc, ks


def approximant(order=2, H=Hf, single_cos=False):
    """g0 + lam g1 + lam^2 g2 in the torus frame, exponentials truncated at the order needed"""
    a1_, a2_ = _waves(H)
    if single_cos:
        a1_, a2_ = a1_.subs(sp.sin(s), 0), a2_.subs(sp.sin(s), 0)
    P1, P2 = lam*a1_, lam*a2_
    bc, bs, kc, ks = g2_terms(H)
    B = lam**2*(bc*sp.cos(2*s) + bs*sp.sin(2*s))
    K = lam**2*(kc*sp.cos(s) + ks*sp.sin(s))
    if "no_pol_g2" in MUT or single_cos:
        B = K = 0
    ex = (lambda P: 1 + 2*P + 2*P**2) if order <= 2 else (lambda P: 1 + 2*P + 2*P**2 + sp.Rational(4, 3)*P**3)
    tr = 0
    if "trace_in_g1" in MUT:
        tr = lam*A*Ef*H*r**sp.Rational(-3, 2)*sp.cos(s)
    g, f = background()
    g = g.as_mutable()
    g[2, 2] = r**2*(ex(-(P1 + P2)) + B + tr)
    g[3, 3] = r**2*C**2*(ex(P1) + B + tr)
    g[4, 4] = r**2*S**2*(ex(P2) + B + tr)
    g[1, 2] = g[2, 1] = K
    return g, (a1_, a2_)


def two_scale_ricci(g, top, comps):
    """Ricci of a metric depending on (v, r, th, s = v/lam), expanded in lam through order lam^top"""
    g0 = g.subs(lam, 0)
    f = 1 - Mf/r**2
    g0i = sp.zeros(5)
    g0i[0, 1] = g0i[1, 0] = 1
    g0i[1, 1] = f
    for i, w in zip((2, 3, 4), (r**2, r**2*C**2, r**2*S**2)):
        g0i[i, i] = 1/w
    Dm = g - g0
    gi = g0i - g0i*Dm*g0i + g0i*Dm*g0i*Dm*g0i - g0i*Dm*g0i*Dm*g0i*Dm*g0i
    gi = gi.applyfunc(lambda e: sum(sp.expand(e).coeff(lam, k)*lam**k for k in range(0, top + 3)))

    def D(e, k):
        out = sp.diff(e, X[k])
        if k == 0:
            out += sp.diff(e, s)/lam
        return out

    def trunc(e, order):
        e = sp.expand(e)
        return sum(e.coeff(lam, k)*lam**k for k in range(-3, order + 1))
    G = _christoffel(g, gi, 5, D)
    G = [[[trunc(x, top + 1) for x in row] for row in M2] for M2 in G]
    R = _ricci(G, 5, D, lambda e: trunc(e, top))
    return {k: R(*k) for k in comps}


def modes(e):
    """Fourier modes in s of a trigonometric polynomial: {0: mean, ('cos', k): ..., ('sin', k): ...}"""
    z = sp.Symbol("z")
    sub = {}
    for k in range(4, 0, -1):
        sub[sp.sin(k*s)] = (z**k - z**-k)/(2*sp.I)
        sub[sp.cos(k*s)] = (z**k + z**-k)/2
    e = sp.expand(sp.expand(e).subs(sub))
    P = sp.Poly(sp.expand(e*z**8), z)
    out = {}
    for k in range(0, 9):
        ck, cm = P.coeff_monomial(z**(8 + k)), P.coeff_monomial(z**(8 - k))
        if k == 0:
            out[0] = sp.simplify(ck)
        else:
            out[("cos", k)] = sp.simplify(ck + cm)
            out[("sin", k)] = sp.simplify(sp.I*(ck - cm))
    return {k: x for k, x in out.items() if x != 0}


COMPS = [(0, 0), (0, 1), (1, 1), (0, 2), (1, 2), (2, 2), (3, 3), (4, 4), (0, 3), (2, 3)]


def a3():
    a1_, a2_ = _waves()
    t1, t2 = a1_, a2_
    trT = (-2*(t1 + t2) + 2*t1 + 2*t2)                 # orthonormal trace of diag(-2(P1+P2), 2P1, 2P2)
    if "trace_in_g1" in MUT:
        trT += 3*A*Ef*Hf*r**sp.Rational(-3, 2)*sp.cos(s)
    # transport 2 D_r F + (3/r) F = 0 on the coordinate components F_AB = r^2 (orthonormal amplitude)
    amp = r**2*t1
    Dr = sp.diff(amp, r) - 2*amp/r                    # D_r F_AB = d_r F_AB - 2 Gamma^C_{rA} F_CB, Gamma^C_{rA} = delta/r
    transport = sp.simplify(2*Dr + 3*amp/r)
    ax0 = sp.simplify((t1 + 2*t2).subs(th, 0))
    ax1 = sp.simplify((2*t1 + t2).subs(th, sp.pi/2))
    return dict(traceless=sp.simplify(trT) == 0, transport=transport == 0, axis0=ax0 == 0, axis1=ax1 == 0)


def a4():
    g, _ = approximant(2)
    R = two_scale_ricci(g, 0, COMPS)
    inv = {k: sp.simplify(e.coeff(lam, -1)) for k, e in R.items()}
    m0 = {k: modes(e.coeff(lam, 0)) for k, e in R.items()}
    mean_vv = m0[(0, 0)].get(0, 0)
    mudot = sp.solve(sp.Eq(mean_vv, 0), sp.diff(Mf, v))
    flux = sp.simplify(mudot[0]) if mudot else None
    rest = {k: {kk: x for kk, x in md.items() if not (k == (0, 0) and kk == 0)} for k, md in m0.items()}
    # the record's h makes H^2 (c^4 + s^4) = 1
    rec = sp.simplify(sp.fu(H_REC**2*(C**4 + S**4)))
    # g2 on S^3: B multiplies the round metric and is a function of x = cos 2th; K is the coefficient of dr dth, smooth
    # at the axes iff odd about th = 0 and th = pi/2
    bc, bs, kc, ks = g2_terms(H_REC)
    odd = all(sp.simplify(e.subs(th, -th) + e) == 0 and sp.simplify(e.subs(th, sp.pi - th) + e) == 0
              for e in (kc, ks))
    return dict(inv=inv, flux=flux, rest=rest, rec=rec, odd=odd)


def a5():
    g, _ = approximant(3)
    R = two_scale_ricci(g, 1, COMPS)
    m1 = {k: modes(e.coeff(lam, 1)) for k, e in R.items()}
    mean = {k: md.get(0, 0) for k, md in m1.items()}
    tang = [(2, 2), (3, 3), (4, 4), (1, 1), (1, 2), (2, 3)]
    tang_first_only = all(set(md) <= {("cos", 1), ("sin", 1)} for k, md in m1.items() if k in tang)
    F02 = A**2*Ef**2/(3*r**3)
    phi = sp.atan(sp.cos(2*th))/2
    tilt = sp.simplify(mean[(0, 2)].subs(Hf, H_REC).doit() - F02*sp.diff(phi, th))
    others0 = all(sp.simplify(x) == 0 for k, x in mean.items() if k != (0, 2))
    gs, _ = approximant(3, single_cos=True)
    Rs = two_scale_ricci(gs, 1, [(0, 2)])
    single = modes(Rs[(0, 2)].coeff(lam, 1)).get(0, 0)
    # angular mean of phi on S^3: the volume cos th sin th dth is -dx/4 with x = cos 2th, so the mean is
    # (1/2) int_{-1}^{1} (arctan(x)/2) dx
    xx = sp.Symbol("x")
    avg = sp.integrate(sp.atan(xx)/2, (xx, -1, 1))/2
    return dict(mean_vth=sp.factor(mean[(0, 2)]), tilt=tilt == 0, others0=others0, tang_first_only=tang_first_only,
                single=sp.simplify(single), avg=sp.simplify(avg))


def compute(with_order1=True):
    out = dict(a1=a1(), a2=a2(), a3=a3(), a4=a4())
    if with_order1:
        out["a5"] = a5()
    return out


def checks(o):
    c = {}
    q = o["a1"]
    c["A1 Touati's (3.17), (3.18) hold for general T, S in 3+1 and 4+1; Pol(T)=0 gives E(T,T) = -1/2 |T_AB|^2"] = all(
        q[d]["ok17"] and q[d]["ok18"] and q[d]["energy"] and q[d]["pol_zero"] for d in (3, 4))
    q = o["a2"]
    c["A2 5D Vaidya: Ric = F0^2 dv dv, F0^2 = 3 mu'/(2 r^3); v eikonal; L0 = -d_r null geodesic; box v = 3/r"] = (
        q["dust"] and q["eik"] and q["geodesic"] and q["L"] == [0, -1, 0, 0, 0] and sp.simplify(q["boxv"] - 3/r) == 0)
    q = o["a3"]
    c["A3 the record's g1: traceless and transverse (Pol = 0), transported as r^-3/2, smooth at both axes"] = (
        q["traceless"] and q["transport"] and q["axis0"] and q["axis1"])
    q = o["a4"]
    flux_ok = q["flux"] is not None and sp.simplify(
        q["flux"] - sp.Rational(2, 9)*A**2*Ef**2*Hf**2*(C**4 + S**4)) == 0
    c["A4 R^(-1) = 0; R^(0) = 0 with g2's polarization terms iff mu' = (2/9) A^2 env^2 (F3's dust); g2 axis-regular"] = (
        all(x == 0 for x in q["inv"].values()) and flux_ok and all(not md for md in q["rest"].values())
        and q["rec"] == 1 and q["odd"])
    if "a5" in o:
        q = o["a5"]
        c["A5 R^(1): tangential comps first harmonic only; one mean term R_vth = F0^2 d_th phi, "
          "phi = arctan(cos 2th)/2, absent for one cosine"] = (
            q["tang_first_only"] and q["tilt"] and q["others0"] and q["single"] == 0 and q["avg"] == 0)
    return c


def report(o=None):
    o = o or compute()
    for k, v_ in checks(o).items():
        print("%-118s %s" % (k[:118], "PASS" if v_ else "FAIL"))
    q = o["a4"]
    print("  A4 mu' from R^(0)_vv mean: %s;  H^2 (c^4 + s^4) with the record's h: %s" % (q["flux"], q["rec"]))
    if "a5" in o:
        print("  A5 the order-lam mean term R_vth = %s; angular mean of phi on S^3: %s; single cosine: %s" % (
            o["a5"]["mean_vth"], o["a5"]["avg"], o["a5"]["single"]))
    return o


def selftest():
    o = compute()
    c = checks(o)
    report(o)
    print("%s: %d/%d" % (os.path.basename(__file__), sum(c.values()), len(c)))
    return all(c.values())


def mutants():
    caught = 0
    for m_, desc in MUTANTS.items():
        MUT.clear()
        MUT.add(m_)
        try:
            c = checks(compute(with_order1=False))
            failed = [k[:40] for k, v_ in c.items() if not v_]
        except Exception as ex:                       # noqa: BLE001
            failed = ["raised %s" % type(ex).__name__]
        caught += bool(failed)
        print("mutant %-18s %s  (%s)  failing: %s" % (m_, "caught" if failed else "MISSED", desc, "; ".join(failed)))
    MUT.clear()
    print("mutants: %d/%d" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest() else 1)
