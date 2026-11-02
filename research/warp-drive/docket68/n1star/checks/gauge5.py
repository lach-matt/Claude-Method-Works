#!/usr/bin/env python3
"""gauge5.py -- G1-G3: computational support for two deduced steps of RESPONSE-HL-5D.md about the gauge field D.

Row 1, paper section 5.5: "the approximant's stage data are chosen so that its data satisfy the constraints and D = 0 to
order N - 2, by a hierarchy that propagates the gauge order by order (supplement Lemmas 6.1-6.2)". Row 12, paper section
3: "The limit is vacuum because the gauge field of the approximant decays at past null infinity, so its energy tends to
zero there". Supplement N1STAR-PROOF.md 6.1-6.2, 9.1, 9.3 and the proof of Theorem P.

  G1 (exact, rational, random 4+1 metrics) the identity (6.2): on a slice where D = 0,
         2 G(n, .) = 2 Gt(E)(n, .) + Z,   Z := d_n D (lowered by g),
     E = Ric^H(g) = Ric - S(D), S(D)_mn = (1/2)(g_m rho Dh_n D^rho + g_n rho Dh_m D^rho), D^rho = g^ab (Gamma[g] -
     Gamma[g0])^rho_ab, Gt(T) = T - (1/2)(tr_g T) g, n the unit normal of {x0 = 0}. g = eta + random quadratic, g0 = eta
     + random quadratic (the background is arbitrary here), and D = 0 to first order along the slice at the point is
     imposed by solving for d_0 g_(0 rho) and d_i d_0 g_(0 rho) (two linear solves, exact). Also rerun: the record's own
     check of the Bianchi step (6.1) uses, response5.py R14 (imported), with its control.
     Controls (each must fail): (6.2) without Z -- the term (F2) sets to zero in mean, d_tau <D^(m)> = 0, so that
     the constraints are the mean of Gt(E); and (6.2) on a slice where D != 0 (no gauge adjustment).
  G2 (exact, sympy, lead5.py's coordinates) the order-lam gauge field D^(1) of the approximant
     g_app = G(X, u/lam), G = g0 + lam (W + m1) + lam^2 gh2, u = v + lam phi1, W = W_TT + chi dv dv (lead5.wave), with
     m1 (15 components) and gh2 (15) generic functions and phi1 generic: m1 is the O(lam) mean, OPEN in the record
     (ansatz5.py A5), so it stays a generic symbolic function throughout. Computed: (a) D^(-1) = D^(0) = 0 (lead5 L5 in
     this form); (b) gh2 enters D^(1) only as Pol(d_s gh2), Pol(Y) = Y(ell, .) - (1/2) dv tr_g0 Y, everywhere on Omega;
     then on Sigma = {tau = tau0} under Lemma 6.2's choices for stage 1 -- phi1 = 0, (m1)_(tau .) = 0 on Sigma (in these
     coordinates m1(d_v, .) = 0, d_tau = d_v at fixed r), d_tau phi1 = -(1/2) m1(ell, ell) (Lemma 5.3(b), q1 = 0),
     chi = 0 on Sigma (stage 0) with d_v chi there a second harmonic in s (its transport source is, lead5 L3-L4):
     (c) the oscillating part of D^(1) is Pol(d_s gh2) + an expression algebraic in m1 (no derivative of m1) + known;
     (d) Pol is onto (data5.py S1, imported) and d_s gh2 := -Pol^+(that) has zero s-mean and kills the oscillating
     part exactly, Pol^+ = Pol^T (Pol Pol^T)^-1 in these components (a right inverse; the supplement takes it in
     Cartesian components for equivariance, not tested here); (e) the mean of D^(1) is linear in the five d_tau
     (m1)_(tau .) with nonzero determinant, and solving kills it: D^(1) = 0 on Sigma, (F1) at m = 1, with m1's
     spatial part h1 and its d_tau (Q1) left generic. Not computed: (F2) at order 1 (the mean of the constraints, which
     Lemma 6.4 solves for h1, Q1), D^(2), and Lemma 6.1's propagation off Sigma.
     Controls (each must fail): the choices not made (d_s gh2 = 0, d_tau (m1)_(tau .) = 0); Pol^T in place of Pol^+.
  G3 (exact) the decay. (a) Supplement 9.1: A_P(tau) = {r_in <= |x| <= r_out} in R^4, r_in = t + a1, a1 > 0, width
     r_out - r_in <= d1. The flat L^2 norm on A_P(tau) of an amplitude r^-q is N_q(t), N_q^2 = vol(S^3) int r^(3-2q) dr,
     vol(S^3) = 2 pi^2 computed in the record's Hopf angles; at q = 2 (class E_2, the proof's D_j) exactly
     N_2^2 = 2 pi^2 log(1 + d/(t + a1)) <= 2 pi^2 d1 / t, so N_2 <= pi (2 d1)^(1/2) t^(-1/2) and t N_2^2 -> 2 pi^2 d:
     the rate the supplement states, "the energy of D(g_lam) on A_P(tau) is at most C t^(-1/2)", the energy being the
     norm (as its line "the L^2 norm of an E_q profile on A_P(tau) is at most C t^(3/2 - q)"). (b) D^(1) of G2, off
     Sigma, in the bounded frame (dv, dr, r dth, r c dphi1, r s dphi2) with the stage classes of Theorem A_P (9.6) put
     in as pure leading terms -- m1, gh2 frame components r^-2 F(v, th[, s]), phi1 = Phi(v, th)/r, chi = X(v, th, s)/
     r^2, W_TT as lead5 has it (r^(-3/2)) -- has r^2 D^(1) bounded as r -> oo: D_1 in E_2 at leading order, the slow
     d_v-divergence of W_TT cancelling by W(ell, .) = 0. Only the leading terms and no derivatives of D^(1) are tested.
     Controls (each must fail): amplitude r^-1 in (a) (N_1 -> oo, no decay); in (b) an oscillating dr dr component
     r^(-3/2) cos s added to W, so that W(ell, .) != 0.

Labels: computed (exact, sympy). m1 generic (OPEN in the record).

Run: python3 checks/gauge5.py   (several minutes)
"""
import os
import random
import sys
import time

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
N1 = os.path.dirname(HERE)
sys.path.insert(0, N1)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(N1)), "paper"))
import lead5 as L                                                               # noqa: E402
import data5                                                                    # noqa: E402
import response5                                                                # noqa: E402

X5 = sp.symbols("x0:5")
ETA = sp.diag(-1, 1, 1, 1, 1)


def _tr(e, d):
    p = sp.Poly(sp.expand(e), *X5)
    return sum((c*sp.Mul(*[x**k for x, k in zip(X5, m)]) for m, c in p.terms() if sum(m) <= d), sp.Integer(0))


def _at0(e):
    return sp.expand(e).subs({x: 0 for x in X5})


def _inv2(g):                                       # g = eta + A, A(0) = 0: inverse through degree 2
    A = g - ETA
    eAe = ETA*A*ETA
    return (ETA - eAe + eAe*A*ETA).applyfunc(lambda e: _tr(e, 2))


def _gamma(g, gi):
    dg = [[[_tr(sp.diff(g[a, b], X5[c]), 1) for c in range(5)] for b in range(5)] for a in range(5)]
    return [[[_tr(sum(gi[a, d]*(dg[d][b][c] + dg[d][c][b] - dg[b][c][d]) for d in range(5))/2, 1)
              for c in range(5)] for b in range(5)] for a in range(5)]


def g1(control=False, seed=62):
    t0 = time.time()
    rnd = random.Random(seed)
    mons = [m for d in (1, 2) for m in sp.itermonomials(X5, d, d)]

    def rmat():
        M = sp.zeros(5)
        for a in range(5):
            for b in range(a, 5):
                M[a, b] = M[b, a] = sum(sp.Rational(rnd.randint(-4, 4), 7)*m for m in mons)
        return M
    al = sp.symbols("al0:5")
    be = sp.symbols("be1:5_0:5")
    g = ETA + rmat()
    for rho in range(5):
        add = X5[0]*al[rho] + sum(X5[0]*X5[i]*be[5*(i - 1) + rho] for i in range(1, 5))
        g[0, rho] += add
        if rho:
            g[rho, 0] += add
    g0 = ETA + rmat()
    G0 = _gamma(g0, _inv2(g0))

    def gauge(gg):
        gi = _inv2(gg)
        G = _gamma(gg, gi)
        D = [_tr(sum(gi[a, b]*(G[r][a][b] - G0[r][a][b]) for a in range(5) for b in range(5)), 1) for r in range(5)]
        return gi, G, D
    gi, G, D = gauge(g)
    sol = sp.solve([_at0(e) for e in D], al, dict=True)[0]
    g = g.subs(sol)
    gi, G, D = gauge(g)
    sol = sp.solve([_at0(sp.diff(D[r], X5[i])) for r in range(5) for i in range(1, 5)], be, dict=True)[0]
    gfix = g.subs(sol)
    gfree = g.subs({b: 0 for b in be})                                 # D(0) = 0 kept, d_i D(0) != 0

    def residual(gg, withZ):
        gi, G, D = gauge(gg)
        Ric = [[_at0(sum(sp.diff(G[a][b][d], X5[a]) - sp.diff(G[a][b][a], X5[d])
                         + sum(G[a][a][e]*G[e][b][d] - G[a][d][e]*G[e][b][a] for e in range(5)) for a in range(5)))
                for d in range(5)] for b in range(5)]
        g00, gi0 = gg.applyfunc(_at0), gi.applyfunc(_at0)
        D0 = [_at0(e) for e in D]
        DhD = [[_at0(sp.diff(D[r], X5[n])) + sum(_at0(G0[r][n][q])*D0[q] for q in range(5)) for r in range(5)]
               for n in range(5)]                                                # DhD[n][rho] = Dh_n D^rho
        S = [[(sum(g00[m, r]*DhD[n][r] + g00[n, r]*DhD[m][r] for r in range(5)))/2 for n in range(5)]
             for m in range(5)]
        E = [[Ric[m][n] - S[m][n] for n in range(5)] for m in range(5)]
        nl = [-1/sp.sqrt(-gi0[0, 0])] + [0]*4
        nu = [sum(gi0[a, b]*nl[b] for b in range(5)) for a in range(5)]
        Zu = [sum(nu[a]*_at0(sp.diff(D[r], X5[a])) for a in range(5)) for r in range(5)]
        Zl = [sum(g00[m, r]*Zu[r] for r in range(5)) for m in range(5)]

        def gtn(T):
            trT = sum(gi0[a, b]*T[a][b] for a in range(5) for b in range(5))
            return [sum(nu[a]*T[a][m] for a in range(5)) - trT*nl[m]/2 for m in range(5)]
        lhs, rhs = gtn(Ric), gtn(E)
        res = [sp.nsimplify(2*lhs[m] - 2*rhs[m] - (Zl[m] if withZ else 0)) for m in range(5)]
        return all(sp.simplify(x) == 0 for x in res), sum(abs(x) for x in Zl)
    if control:
        noZ, _ = residual(gfix, False)
        nogauge, _ = residual(gfree, True)
        r14c = response5.r14(control=True)
        print("  G1 control: (6.2) without Z holds: %s; (6.2) where d_i D != 0 holds: %s; R14 control holds: %s"
              % (noZ, nogauge, r14c), flush=True)
        return noZ or nogauge or r14c
    ok, zsize = residual(gfix, True)
    r14 = response5.r14()
    print("  G1: (6.2) 2 G(n, .) = 2 Gt(E)(n, .) + d_n D, exact, at a point of a random 4+1 metric with D = 0 along the"
          " slice: %s (sum |Z_m| = %s, so Z is live); response5 R14 (6.1's Bianchi step) rerun: %s [%.0fs]"
          % (ok, zsize, r14, time.time() - t0), flush=True)
    return ok and r14 and zsize != 0


_CACHE = {}
v, r, th, s, lam = L.v, L.r, L.th, L.s, L.lam
MF = [[sp.Function("m%d%d" % (min(a, b), max(a, b)))(v, r, th) for b in range(5)] for a in range(5)]
GF = [[sp.Function("G%d%d" % (min(a, b), max(a, b)))(v, r, th, s) for b in range(5)] for a in range(5)]
PHI = sp.Function("phi1")(v, r, th)


def d1_general(rr=False):
    """lam^-1, lam^0, lam^1 coefficients of D(g_app) lowered by g0, in lead5's (v, r, th, phi1, phi2)"""
    if rr in _CACHE:
        return _CACHE[rr]
    g0, g0i = L.background()
    W = L.wave(with_chi=True)
    if rr:
        W[1, 1] += L.A*L.Ef*L.Hf*r**sp.Rational(-3, 2)*sp.cos(s)
    m, G2 = sp.Matrix(MF), sp.Matrix(GF)

    def d(e, k):
        out = sp.diff(e, L.X[k]) + sp.diff(e, s)*sp.diff(PHI, L.X[k])
        return out + sp.diff(e, s)/lam if k == 0 else out
    g = g0 + lam*(W + m) + lam**2*G2
    gi = (g0i - lam*g0i*(W + m)*g0i).applyfunc(lambda e: L.trunc(e, 1))
    Gm = L.christoffel(g, gi, d)
    Gh = L.christoffel(g0, g0i, lambda e, k: sp.diff(e, L.X[k]))
    Du = [L.trunc(sum(gi[a, b]*L.trunc(Gm[q][a][b] - Gh[q][a][b], 1) for a in range(5) for b in range(5)), 1)
          for q in range(5)]
    Dl = [sp.expand(sum(g0[c, q]*Du[q] for q in range(5))) for c in range(5)]
    out = {k: [e.coeff(lam, k) for e in Dl] for k in (-1, 0, 1)}
    _CACHE[rr] = (out, g0, g0i)
    return _CACHE[rr]


def pol_matrix(g0i):
    ell = [g0i[a, 0] for a in range(5)]
    basis = []
    for i in range(5):
        for j in range(i, 5):
            h = sp.zeros(5)
            h[i, j] = h[j, i] = 1
            basis.append(h)
    cols = []
    for h in basis:
        tr = sum(g0i[a, b]*h[a, b] for a in range(5) for b in range(5))
        cols.append([sum(ell[a]*h[a, c] for a in range(5)) - (tr/2 if c == 0 else 0) for c in range(5)])
    return sp.Matrix(cols).T, basis


def g2(control=False):
    t0 = time.time()
    o, g0, g0i = d1_general()
    D1 = o[1]
    zero01 = all(sp.simplify(e) == 0 for k in (-1, 0) for e in o[k])
    P, basis = pol_matrix(g0i)
    Ysym = sp.symbols("Y0:15")
    Ymat = sum((y*h for y, h in zip(Ysym, basis)), sp.zeros(5))
    rep = {sp.Derivative(GF[a][b], s): Ymat[a, b] for a in range(5) for b in range(5)}
    D1Y = [sp.expand(e.subs(rep)) for e in D1]
    polY = P*sp.Matrix(Ysym)
    only_pol = all(not (D1Y[c] - polY[c]).has(*[GF[a][b].func for a in range(5) for b in range(5)])
                   and sp.simplify(sp.expand(D1Y[c] - polY[c]).subs({y: 0 for y in Ysym}) - (D1Y[c] - polY[c])) == 0
                   for c in range(5))
    # Sigma = {v - r = tau0}: Lemma 6.2's stage-1 choices
    Pv = sp.symbols("Pv0:5")                        # d_tau (m1)_(tau a) = d_v m_(v a) on Sigma, the unknowns of (ii)
    c2, s2 = sp.Function("c2")(r, th), sp.Function("s2")(r, th)
    chiv = c2*sp.cos(2*s) + s2*sp.sin(2*s)
    mll = MF[1][1]                                  # m1(ell, ell), ell = d_r
    sub = {}
    for a in range(5):
        f = MF[0][a]
        sub[sp.Derivative(f, v)], sub[sp.Derivative(f, r)], sub[sp.Derivative(f, th)] = Pv[a], -Pv[a], 0
    sub.update({sp.Derivative(PHI, v): -mll/2, sp.Derivative(PHI, r): mll/2, sp.Derivative(PHI, th): 0})
    sub.update({sp.Derivative(L.chi, s): 0, sp.Derivative(L.chi, th): 0, sp.Derivative(L.chi, v): chiv,
                sp.Derivative(L.chi, r): -chiv})
    zero = {MF[0][a]: 0 for a in range(5)}
    zero.update({PHI: 0, L.chi: 0})
    DS = [sp.expand(e.subs(sub).subs(zero)) for e in D1Y]
    rest = [e.subs({y: 0 for y in Ysym}) for e in DS]
    mean = [L.modes(e)[0] for e in rest]
    osc = [sp.expand(rest[c] - mean[c]) for c in range(5)]
    mfun = {MF[a][b].func for a in range(5) for b in range(5)}
    algebraic = not any(dd.expr.func in mfun for e in osc for dd in e.atoms(sp.Derivative))
    onto = data5.s1()
    PPt = (P*P.T).applyfunc(sp.simplify)
    Pplus = P.T*PPt.inv()
    yv = -(P.T if control else Pplus)*sp.Matrix(osc)
    ymean0 = not Pplus.has(s) and all(sp.simplify(L.modes(e)[0]) == 0 for e in osc)  # <yv> = -Pol^+ <osc>
    killed_osc = all(sp.simplify(osc[c] + (P*yv)[c]) == 0 for c in range(5))
    J = sp.Matrix([[sp.diff(mean[c], p) for p in Pv] for c in range(5)])
    det = sp.simplify(J.det())
    psol = sp.solve(mean, Pv, dict=True)
    killed_mean = bool(psol) and all(sp.simplify(e.subs(psol[0])) == 0 for e in mean)
    nochoice = all(sp.simplify(e.subs({y: 0 for y in Ysym}).subs({p: 0 for p in Pv})) == 0 for e in DS)
    if control:
        print("  G2 control: D^(1) = 0 on Sigma with no choices: %s; Pol^T in place of Pol^+ kills the oscillating"
              " part: %s" % (nochoice, killed_osc), flush=True)
        return nochoice or killed_osc
    print("  G2: D^(-1) = D^(0) = 0: %s; gh2 enters D^(1) only as Pol(d_s gh2): %s; on Sigma the rest of the"
          " oscillating part is algebraic in m1: %s; Pol onto (data5 S1): %s; d_s gh2 := -Pol^+(rest) has zero mean:"
          " %s and kills the oscillating part: %s; mean linear in d_tau (m1)_(tau .), det = %s, solved, mean killed: %s"
          " [%.0fs]" % (zero01, only_pol, algebraic, onto, ymean0, killed_osc, det, killed_mean, time.time() - t0),
          flush=True)
    return zero01 and only_pol and algebraic and onto and ymean0 and killed_osc and det != 0 and killed_mean


def g3(control=False):
    t0 = time.time()
    t, a1, dd, d1 = sp.symbols("t a1 d d1", positive=True)
    rho, q = sp.symbols("rho q", positive=True)
    vol = sp.integrate(sp.cos(th)*sp.sin(th), (th, 0, sp.pi/2))*(2*sp.pi)**2
    N2 = lambda qq: sp.simplify(vol*sp.integrate(rho**(3 - 2*qq), (rho, t + a1, t + a1 + dd)))  # noqa: E731
    n2 = N2(2)
    exact = sp.simplify(n2 - 2*sp.pi**2*sp.log(1 + dd/(t + a1))) == 0
    x = sp.Symbol("x", positive=True)                               # log(1 + x) <= x, d <= d1, t + a1 >= t
    bound = sp.simplify(sp.diff(x - sp.log(1 + x), x) - x/(x + 1)) == 0 and (x - sp.log(1 + x)).subs(x, 0) == 0
    lim = sp.limit(t*n2, t, sp.oo)
    rate = sp.simplify(lim - 2*sp.pi**2*dd) == 0
    n1lim = sp.limit(N2(1), t, sp.oo)
    n32 = sp.simplify(N2(sp.Rational(3, 2)))
    # (b) D^(1) in the bounded frame with the classes (9.6) at leading order
    z = sp.Symbol("z", positive=True)
    res = []
    for rr in ((True,) if control else (False,)):
        o, g0, g0i = d1_general(rr)
        sc = [1, 1, r, r*L.C, r*L.S]
        rep = {}
        for a in range(5):
            for b in range(a, 5):
                rep[MF[a][b]] = sc[a]*sc[b]*sp.Function("F%d%d" % (a, b))(v, th)/r**2
                rep[GF[a][b]] = sc[a]*sc[b]*sp.Function("K%d%d" % (a, b))(v, th, s)/r**2
        rep[PHI] = sp.Function("Phi")(v, th)/r
        rep[L.chi] = sp.Function("Xc")(v, th, s)/r**2
        worst = sp.oo
        for c in range(5):
            e = (o[1][c].xreplace(rep).doit()*r**2/sc[c]).subs(r, z**-2)
            co = sp.collect(sp.expand(e), z, evaluate=False)
            for key, val in co.items():
                p = key.as_base_exp()[1] if key.has(z) else 0
                if p < worst and sp.simplify(val) != 0:
                    worst = p
        res.append(worst)
    if control:
        print("  G3 control: amplitude r^-1: N_1 -> %s as t -> oo (decays: %s); W(ell, .) != 0: r^2 D^(1) bounded: %s"
              % (n1lim, n1lim == 0, res[0] >= 0), flush=True)
        return n1lim == 0 or res[0] >= 0
    print("  G3: vol(S^3) = %s; N_2^2 = 2 pi^2 log(1 + d/(t + a1)) exactly: %s; log(1 + x) <= x: %s, so N_2 <= pi"
          " (2 d1)^(1/2) t^(-1/2); t N_2^2 -> %s (rate t^(-1/2) sharp): %s; N_(3/2)^2 = %s (no decay at r^(-3/2));"
          " r^2 D^(1) (frame, classes (9.6), m1 generic) has lowest power z^%s of z = r^(-1/2): bounded: %s [%.0fs]"
          % (vol, exact, bound, lim, rate, n32, res[0], res[0] >= 0, time.time() - t0), flush=True)
    return vol == 2*sp.pi**2 and exact and bound and rate and res[0] >= 0


CHECKS = [("G1", g1), ("G2", g2), ("G3", g3)]


def main():
    ok = True
    for name, f in CHECKS:
        good = f()
        ctl = f(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
