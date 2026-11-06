#!/usr/bin/env python3
"""degtwo5.py -- the degree-two and localisation lemmas, the transition and the dips (EQUALITY5-LAYER.md, Round 5,
R5.2 and R5.4: Lemmas L.15_P (b), L.17, L.18 written in full; Theorem L.24 (one switch per column); Proposition L.25
(envelopes with dips); Round 6, R6.2: Proposition L.25'; Round 7, R7.4: Proposition L.25'' (a)).

  T1 (exact; a three-dimensional instance of a dimension-free identity) The reduced Ricci operator relative to a
     background gb is quasilinear: Ric^H(g) + (1/2) g^ab d_a d_b g_mn contains no second derivative of g, for a
     metric g(x, y) on R^3 with four free functions (g00, g01, g11, g22) against the flat background.  So the
     quadratic remainder
     N(u) := Ric^H(gb + u) - dRic^H(u) obeys |N(u)| <= C (|u| |d^2 u| + |du|^2 + |u|^2), with no (d^2 u)^2 term.
     Control: Ric itself (without the gauge term) keeps second derivatives outside g^ab d_a d_b.
  T2 (exact) The seed with mu(v) against the static seed mu0: every component of Gamma[g0] - Gamma[g0 deg] is a
     polynomial of degree <= 2 in (mu - mu0, mu') with coefficients functions of (r, th) and no constant term; so Ric^H
     relative to g0 and relative to g0deg differ by A(g), bounded by C (|mu - mu0| + |mu'| + |mu''|) with its
     derivatives, local in v (the mu-terms of L.17).  Control: against a
     wrong background (mu0 + 1 in place of mu0) the difference has a constant term.
  T3 (exact) The tilted face with any tilt: for alpha = dv + e psi' dtau, g0^-1(alpha, alpha) = -2 e psi' - e^2 psi'^2
     (1 + mu/r^2) and |alpha|_e^2 = (1 + e psi')^2 + 1; if |(g - g0)^-1(beta, beta)| <= D psi' |beta|_e^2 (the weight
     psi' = t^(-3/2) on P, 1 on Omega) and e >= 2 D, e psi' <= 1/2, then g^-1(alpha, alpha) < 0.  Control: e = D
     admits a positive value.
  T4 (computed, mpmath; unit constants, lam = 1e-6, N = 9, c = 30, C = 10^3) The descent of Lemma L.18: y_(k+1) defined
     by 1/kappa(v_s + y_(k+1)) = 6 delta_(k+1), delta_(k+1) := C kappa(v_s + 4 y_k)^c env(v_s + 4 y_k), from y_0 =
     10^-4 (x_D depends on the cost c: at y = 10^-2 the model's delta exceeds 1); for exp(-1/x) and the record's
     C_c^inf envelope, two steps, each y_(k+1) < y_k/2 (in fact log y_(k+1) of the order of -1/y_k: faster than any
     geometric sequence; the second step in logarithmic form, kappa ~ c_e/x^2 at the edge, checked at the first);
     hypothesis (H_D) sampled: kappa(v_s + y/2) kappa(v_s + 4y)^c env(v_s + 4y) below 1 and decreasing at y = 10^-4,
     3 10^-5, 10^-5.
     Control: env = x^40 (smooth, not flat at that order) stalls at once.
  T5 (computed; unit constants) The transition (Theorem L.24): with m0 = sqrt(mu/mu0) - 1 + 2 r_q', mu = 1 + (2/9) int
     env^2, A = mu0 = 1, the record's envelope and exp(-1/x): m0'/m0 >= 1.9 kappa where R in [0.9, 1.1], so m0' -
     |S'| >= 0.85 kappa m0 for S = lam^3 nu env (|S'| = kappa |S|); and in a model g^-1 = -m0 - Re[S e^(i v/lam)] + rho,
     rho a slowly varying degree-two term of size lam^(1/10) m0 plus a structureless one of size lam^3 m0, the maxima
     over consecutive carrier periods decrease through the band and change sign once (lam = 1e-6, exp(-1/x)).  Control:
     rho structureless of size m0/3 gives more than one sign change.
  T6 (computed with unit constants; rounds 6-7) Dips (Proposition L.25'' (a)): env := sum_n exp(-n^2) beta(2^(n+2) (x
     - 2^-n)) near v_s, beta = exp(-1/(1 - t^2)) on [-1, 1] (C_c^inf, flat at v_s, zero on the intervals J_n = (1.25,
     1.5) 2^-n between consecutive bumps).  (a) env vanishes on J_n (41 points), so every oscillating profile of g_app
     does.  (b) For delta = 1/10 and 1/2 and lam = 10^-E, E = 10^2, ..., 10^6, n the least index with h_n <=
     lam^(3+delta) (so h_n >= lam^(3.4+delta) below lam_h(delta), printed), the remaining terms of g_lam^-1(dPhi0,
     dPhi0) + m0 against m0's lower bound (2 A^2/(27 mu0)) h_n^2 int beta^2/s_n: Lemma L.4''s w (lam^(N-5) eps_(M*),
     N = 9, M* = 26), Lemma L.4_P's (lam^(N_P-3) eps_(M_P), N_P = 18, M_P = 44) and L.3 (b)'s means, j-resolved
     (max_j lam^j eps_(2j)^2, j <= N_P), with eps_k(v1) <= 2 h_n s_n^k B_k (the bumps m > n included), s_n = 2^(n+2),
     B_k = max_(i<=k) sup |beta^(i)|; and the two lemmas' hypotheses, eps_4(v1) <= lam (L.4') and eps_(M_P)(v1) <=
     lam^3 (L.4_P).  From some E of the grid on, every ratio is below 0 with both hypotheses and decreasing, and below
     -1000 at E = 10^6 (the ratios fall like lam^(N-8.4-delta) e^(c sqrt(log 1/lam))).  Unit constants: A = mu0 = 1 and
     the record's unknown constants set to 1.  Controls: round 5's bump choice h_n ~ lam^4 (the ratio grows), and J_n
     filled by an extra bump (no zero interval).
  T7 (exact; round 6, the verifier of round 5's m9) L.17 (2)'s four-derivative form of Lemma L.4's energy argument:
     bandL4p5 H1's ledger at levels 0-4 with eps_6 <= lam^5: every coefficient bounded, so the non-triangular rule
     closes (every coefficient into Gronwall).  Control: at eps_6 <= lam^4 a coefficient of level 4 is unbounded.

Labels: T1-T3, T7 computed (exact, sympy, exact rationals); T4, T6 computed (mpmath, bounds; T4 a model with unit
constants, T6 a computation with unit constants: mu0 = A = 1 and the record's constants set to 1); T5 computed
(mpmath; m0's formula exact, S a model).  Run: python3 checks/degtwo5.py   (about ten minutes)
"""
import math
import os
import sys
import textwrap
import time

import mpmath as mp
import sympy as sp

T0 = time.time()


def out(msg):
    print(textwrap.fill(msg, width=121, subsequent_indent="      ", break_on_hyphens=False), flush=True)


# ------------------------------------------------------------------------------------------------------------ T1
def ricci(g, X):
    n = len(X)
    gi = g.inv()
    Gam = [[[sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                 for d in range(n))/2 for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.Matrix(n, n, lambda b, c: sum(sp.diff(Gam[a][b][c], X[a]) for a in range(n))
                    - sum(sp.diff(Gam[a][b][a], X[c]) for a in range(n))
                    + sum(Gam[a][a][d]*Gam[d][b][c] - Gam[a][c][d]*Gam[d][b][a] for a in range(n) for d in range(n)))
    return Ric, gi, Gam


def t1(control=False):
    x, y, z = sp.symbols('x y z')
    X = [x, y, z]
    g = sp.zeros(3)
    for (i, j) in ((0, 0), (0, 1), (1, 1), (2, 2)):
        g[i, j] = g[j, i] = sp.Function('g%d%d' % (i, j))(x, y)
    Ric, gi, Gam = ricci(g, X)
    # wave-map gauge against the flat background: D^r = g^ab Gamma^r_ab; Ric^H = Ric - (1/2)(g_mr d_n D^r + g_nr d_m D^r)
    D = [sum(gi[a, b]*Gam[r][a][b] for a in range(3) for b in range(3)) for r in range(3)]
    RH = sp.Matrix(3, 3, lambda m, n: Ric[m, n] - (sum(g[m, r]*sp.diff(D[r], X[n]) + g[n, r]*sp.diff(D[r], X[m])
                                                       for r in range(3)))/2)
    M = Ric if control else RH
    ok = True
    for m in range(3):
        for n in range(m, 3):
            e = sp.expand(M[m, n] + sum(gi[a, b]*sp.diff(g[m, n], X[a], X[b]) for a in range(3) for b in range(3))/2)
            sec = [d for d in e.atoms(sp.Derivative) if sum(c for _, c in d.variable_count) >= 2]
            rep = {d: sp.Symbol('S%d' % k) for k, d in enumerate(sec)}
            e2 = e.xreplace(rep)
            ok &= all(sp.cancel(sp.diff(e2, s_)) == 0 for s_ in rep.values())
    if control:
        return ok
    out("  T1 Ric^H(g) + (1/2) g^ab d_a d_b g_mn free of second derivatives (R^3, g with g00, g01, g11, g22 general"
        " functions of (x, y), flat background): %s  [%.0f s]" % (ok, time.time() - T0))
    return ok


# ------------------------------------------------------------------------------------------------------------ T2
def t2(control=False):
    v, r, th, p1, p2 = sp.symbols('v r theta phi1 phi2', real=True)
    mu0 = sp.Symbol('mu0', positive=True)
    mu = sp.Function('mu')(v)
    X = [v, r, th, p1, p2]
    c, s = sp.cos(th), sp.sin(th)

    def metric(m):
        g = sp.diag(-(1 - m/r**2), 0, r**2, r**2*c**2, r**2*s**2)
        g[0, 1] = g[1, 0] = 1
        return g
    g1, g0 = metric(mu), metric(mu0 + 1 if control else mu0)
    gi1, gi0 = g1.inv(), g0.inv()

    def gam(g, gi):
        return [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[cc]) + sp.diff(g[d, cc], X[b])
                                            - sp.diff(g[b, cc], X[d])) for d in range(5))/2)
                  for cc in range(5)] for b in range(5)] for a in range(5)]
    G1, G0 = gam(g1, gi1), gam(g0, gi0)
    dm, mp1 = sp.symbols('dm mp1')
    ok = True
    for a in range(5):
        for b in range(5):
            for cc in range(5):
                e = sp.simplify(G1[a][b][cc] - G0[a][b][cc])
                e = e.subs(sp.Derivative(mu, v), mp1).subs(mu, mu0 + dm)
                e = sp.expand(e)
                ok &= sp.simplify(e.subs({dm: 0, mp1: 0})) == 0
                try:
                    pl = sp.Poly(e, dm, mp1)
                    ok &= pl.total_degree() <= 2 and all(c_.free_symbols <= {r, th, mu0} for c_ in pl.coeffs())
                except sp.PolynomialError:
                    ok = False
    if control:
        return ok
    out("  T2 Gamma[g0] - Gamma[g0deg] a polynomial of degree <= 2 in (mu - mu0, mu') with coefficients in (r, th, mu0)"
        " and no constant term, every component: %s" % ok)
    return ok


# ------------------------------------------------------------------------------------------------------------ T3
def t3(control=False):
    e, p, D, mu, r = sp.symbols('e p D mu r', positive=True)
    g0aa = -2*e*p - e**2*p**2*(1 + mu/r**2)
    norm = (1 + e*p)**2 + 1
    worst = g0aa + D*p*norm
    if control:
        val = worst.subs({e: D}).subs({D: sp.Rational(1, 10), p: 1, mu: 0, r: 1})
        return val < 0
    # with e = 2 D (1 + t), t >= 0, and e p <= 1/2: worst <= p (-2 e + D (9/4 + 1)) = p (-4 D (1 + t) + 13 D/4) < 0
    t = sp.Symbol('t', nonnegative=True)
    bound = sp.simplify(p*(-2*e + D*(sp.Rational(9, 4) + 1))).subs(e, 2*D*(1 + t))
    neg = sp.simplify(bound + p*D*(sp.Rational(3, 4) + 4*t)) == 0
    dom = sp.simplify(worst - (-2*e*p + D*p*norm)) == sp.simplify(-e**2*p**2*(1 + mu/r**2))
    out("  T3 g^-1(alpha, alpha) <= p (-2 e + (13/4) D) = -p D (3/4 + 4 t) < 0 for e = 2 D (1 + t), e p <= 1/2: %s; the"
        " dropped term -e^2 p^2 (1 + mu/r^2) <= 0: %s" % (neg, dom))
    return neg and dom


# ------------------------------------------------------------------------------------------------------------ T4
def rec_ell(x):
    t = 2*x/3
    return 12*mp.log(mp.sin(mp.pi*t/2)) + 1 - 1/(t*(2 - t))


def rec_kap(x):
    t = 2*x/3
    return mp.mpf(2)/3*(6*mp.pi*mp.cot(mp.pi*t/2) + 2*(1 - t)/(t**2*(2 - t)**2))


def t4(control=False):
    mp.mp.dps = 40
    C, c = mp.mpf(10)**3, 30
    # (name, log env, kappa, the constant c_e of kappa ~ c_e/x^2 as x -> 0 (None: not of that form))
    edges = [("exp(-1/x)", lambda x: -1/x, lambda x: 1/x**2, mp.mpf(1)),
             ("record C_c^inf", rec_ell, rec_kap, mp.mpf(3)/4)]
    if control:
        edges = [("x^40", lambda x: 40*mp.log(x), lambda x: 40/x, None)]
    rows, ok = [], True
    for nm, ell, kap, ce in edges:
        z = -mp.log(mp.mpf('1e-4'))                     # y = e^-z, kept in logarithmic form
        zs = [z]
        good = True
        for k in range(2):
            y4 = 4*mp.exp(-z)
            ldel = mp.log(C) + c*mp.log(kap(y4)) + ell(y4)                         # log delta_(k+1)
            target = -mp.log(6) - ldel                                              # need log kappa(y') <= target
            if mp.log(kap(mp.exp(-z))) > target:                                    # even y itself is not local
                good = False
                break
            if ce is None:
                good = False
                break
            # for the deep steps log kappa(e^-z') = log c_e + 2 z' + O(e^-z') (checked at the first step below)
            zn = (target - mp.log(ce))/2
            if k == 0:
                yn = mp.exp(-zn)
                good &= abs(mp.log(kap(yn)) - target) < mp.mpf('1e-6')*abs(target)
            good &= zn > z + mp.log(2)
            z = zn
            zs.append(z)
        hd = [kap(t/2)*kap(4*t)**c*mp.exp(ell(4*t)) for t in (mp.mpf('1e-4'), mp.mpf('3e-5'), mp.mpf('1e-5'))]
        dec = hd[0] > hd[1] > hd[2] and hd[0] < 1
        ok &= good and dec
        rows.append("%s: log10 y_k = %s; y_(k+1) < y_k/2: %s; (H_D) quantity at 1e-4, 3e-5, 1e-5: %s" % (
            nm, [mp.nstr(-t/mp.log(10), 4) for t in zs], good, [mp.nstr(h, 3) for h in hd]))
    if control:
        return ok
    out("  T4 descent (unit constants C = 10^3, c = 30, from y_0 = 10^-4): " + "; ".join(rows))
    return ok


# ------------------------------------------------------------------------------------------------------------ T5
def t5(control=False):
    mp.mp.dps = 30
    lam = mp.mpf(10)**-6
    nu = mp.mpf(1)/9
    ok = True
    rows = []
    for nm, ell in (("exp(-1/x)", lambda x: -1/x), ("record C_c^inf", rec_ell)):
        env = lambda x: mp.exp(ell(x))                                            # noqa: E731
        kap = lambda x: mp.diff(ell, x)                                            # noqa: E731

        def m0(x):
            I2 = mp.quad(lambda t: env(t)**2, [0, x/4, x/2, x])
            mu = 1 + mp.mpf(2)/9*I2
            rqp = mu**mp.mpf(-0.75)*(mp.mpf(2)/9*env(x)**2)/4
            return mp.sqrt(mu) - 1 + 2*rqp
        # the band where R = lam^3 nu env/m0 lies in [1/2, 2]
        lo, hi = mp.mpf('1e-4'), mp.mpf('0.3')
        for _ in range(200):
            mid = (lo + hi)/2
            if lam**3*nu*env(mid)/m0(mid) > 1:
                lo = mid
            else:
                hi = mid
        xs = [lo*(1 + mp.mpf(k)/4000) for k in range(-6, 7)]
        rat = []
        for x in xs:
            dm0 = mp.diff(m0, x)
            R = lam**3*nu*env(x)/m0(x)
            rat.append((dm0/(m0(x)*kap(x)), R, (dm0 - lam**3*nu*env(x)*kap(x))/(kap(x)*m0(x))))
        sel = [(a_, R_, b_) for a_, R_, b_ in rat if mp.mpf('0.9') <= R_ <= mp.mpf('1.1')]
        ok &= len(sel) >= 3 and all(a_ >= mp.mpf('1.9') and b_ >= mp.mpf('0.85') for a_, _, b_ in sel)
        rat = sel
        rows.append("%s: R = 1 at x = %s; m0'/(kappa m0) >= %s, (m0' - |S'|)/(kappa m0) >= %s on R in [0.9, 1.1]" % (
            nm, mp.nstr(lo, 5), mp.nstr(min(a_ for a_, _, b_ in rat), 4), mp.nstr(min(b_ for a_, _, b_ in rat), 4)))
    # the model: one sign change of the maxima over consecutive carrier periods, exp(-1/x)
    ell = lambda x: -1/x                                                            # noqa: E731
    env = lambda x: mp.exp(ell(x))                                                 # noqa: E731
    xc = None
    lo, hi = mp.mpf('1e-4'), mp.mpf('0.3')
    m0s = lambda x: env(x)**2/9*(1 + x**2/2)                                        # the margin's model (exp edge)
    for _ in range(200):
        mid = (lo + hi)/2
        if lam**3*nu*env(mid)/m0s(mid) > 1:
            lo = mid
        else:
            hi = mid
    xc = lo
    maxima = []
    per = 2*mp.pi*lam
    x = xc - 40*per
    for k in range(80):
        best = -mp.inf
        for j in range(48):
            t = x + per*j/48
            S = lam**3*nu*env(t)
            m = m0s(t)
            rho = lam**mp.mpf(0.1)*m*mp.cos(2*t/lam + t*1000)
            rho += (m/3 if control else lam**3*m)*mp.sin(mp.mpf(7.3)*k + j)        # structureless
            val = -m - S*mp.cos(t/lam) + rho
            best = max(best, val)
        maxima.append(best)
        x += per
    changes = sum(1 for a_, b_ in zip(maxima, maxima[1:]) if (a_ > 0) != (b_ > 0))
    mono = all(b_ < a_ for a_, b_ in zip(maxima, maxima[1:]))
    if control:
        return changes == 1
    ok &= changes == 1 and mono
    out("  T5 " + "; ".join(rows) + ".  Model (exp(-1/x), lam = 1e-6): maxima over 80 consecutive carrier periods"
        " around R = 1 strictly decreasing: %s, sign changes: %d" % (mono, changes))
    return ok


# ------------------------------------------------------------------------------------------------------------ T6
def bump_sups(kmax):
    """B_k := max_(i<=k) sup |beta^(i)|, beta = exp(-1/(1 - t^2)): beta^(k) = e^(-1/(1-t^2)) p_k(t)/(1 - t^2)^(2k) with
    p_(k+1) = (1 - t^2)^2 p_k' + (4 k t (1 - t^2) - 2 t) p_k; sup on 4000 points and a local refinement"""
    t = sp.Symbol('t')
    p = sp.Poly(1, t)
    sups = []
    mp.mp.dps = 40
    for k in range(kmax + 1):
        f = sp.lambdify(t, p.as_expr(), 'mpmath')
        g = lambda x, f=f, k=k: abs(mp.exp(-1/(1 - x*x))*f(x)/(1 - x*x)**(2*k))          # noqa: E731
        grid = [mp.mpf(i)/2000 - 1 for i in range(1, 4000)]
        vals = [g(x) for x in grid]
        i0 = max(range(len(vals)), key=lambda i: vals[i])
        best = vals[i0]
        a_, b_ = grid[max(i0 - 1, 0)], grid[min(i0 + 1, len(grid) - 1)]
        for j in range(201):
            best = max(best, g(a_ + (b_ - a_)*j/200))
        sups.append(best)
        p = sp.Poly(sp.expand((1 - t**2)**2*sp.diff(p.as_expr(), t) + (4*k*t*(1 - t**2) - 2*t)*p.as_expr()), t)
    B = []
    for k in range(kmax + 1):
        B.append(max(sups[:k + 1]))
    return B


CACHE6 = {}


def t6_ratios(delta, bump="least", L10s=(10**2, 10**3, 10**4, 10**5, 10**6)):
    """the log10 ratios of Proposition L.25' (a) at lam = 10^-E; bump n the least with h_n <= lam^(3 + delta)
    (bump = "lam4": round 5's choice h_n ~ lam^4, the mutation of minor 5)"""
    B, ib2 = CACHE6['B'], CACHE6['ib2']
    N, Ms = 9, 26                                          # Theorem 1 at K = 6: N = K + 3, M* = 2N + 8
    NP, MP = 18, 44                                        # Theorem 2 at K = 6, beta_P = 2: N_P = K + 4 + 8, 2 N_P + 8
    l2 = mp.log10(2)
    out_ = []
    for E in L10s:
        L10 = mp.mpf(E)
        Ln = L10*mp.log(10)
        p = 4 if bump == "lam4" else 3 + delta
        n = int(mp.ceil(mp.sqrt(p*Ln)))                    # the least n with e^(-n^2) <= lam^p
        lh = -n*n/mp.log(10)                               # log10 h_n
        window = lh >= -(mp.mpf('3.4') + delta)*L10 and lh <= -(3 + delta)*L10
        tails = mp.e**(2*n + 1) >= 2**(MP + 1)
        ls = (n + 2)*l2                                    # log10 s_n, s_n = 2^(n+2)
        le = lambda k: l2 + lh + k*ls + mp.log10(B[k])     # noqa: E731  log10 of the bound of eps_k(v1)
        lm0 = mp.log10(mp.mpf(2)/27*ib2) + 2*lh - ls       # log10 of m0's lower bound
        lw1 = -(N - 5)*L10 + le(Ms) - lm0                  # L.4': lam^(N-5) eps_(M*) / m0
        lw2 = -(NP - 3)*L10 + le(MP) - lm0                 # L.4_P: lam^(N_P-3) eps_(M_P) / m0
        lme = max(-j*L10 + 2*le(2*j) - lm0 for j in range(1, NP + 1))                  # L.3 (b), j-resolved
        h1 = le(4) <= -L10                                 # L.4''s hypothesis eps_4(v1) <= lam
        h2 = le(MP) <= -3*L10                              # L.4_P's hypothesis eps_(M_P)(v1) <= lam^3
        out_.append(dict(E=E, n=n, window=window, tails=tails, lw1=lw1, lw2=lw2, lme=lme, h1=h1, h2=h2))
    return out_


def t6(control=False):
    """Proposition L.25' (a), round 7: 0 < delta <= 1/2, n the least index with h_n <= lam^(3 + delta), so that h_n >=
    lam^(3.4 + delta) once lam <= lam_h(delta); on J_n' every term of g_lam^-1(dPhi0, dPhi0) + m0 is a mean of g_app
    (L.3 (b)) or the remainder w (L.4', L.4_P); their bounds against m0's lower bound (2 A^2/(27 mu0)) int env^2, in
    log10, A = mu0 = 1 and the record's unknown constants set to 1 (a computation with unit constants).
    eps_k(v1) <= 2 h_n s_n^k B_k (the bumps m > n included).  Controls: round 5's bump choice h_n ~ lam^4 (the ratio
    grows) and the zero intervals removed"""
    mp.mp.dps = 40
    if 'B' not in CACHE6:
        CACHE6['B'] = bump_sups(44)
        CACHE6['ib2'] = mp.quad(lambda t: mp.exp(-2/(1 - t*t)), [-1, 0, 1])
    rows, ok = [], True
    lamh = {}
    for delta in (mp.mpf(1)/10, mp.mpf(1)/2):
        # 2 sqrt((3 + delta) L) + 1 <= 0.4 L  <=>  sqrt(L) >= y_h: then h_n >= lam^(3.4 + delta)
        yh = (2*mp.sqrt(3 + delta) + mp.sqrt(4*(3 + delta) + mp.mpf('1.6')))/mp.mpf('0.8')
        lamh[delta] = -yh**2/mp.log(10)                    # log10 lam_h(delta)
        res = t6_ratios(delta, "lam4" if control else "least")
        hyp_from, good = None, True
        worsts = [max(d['lw1'], d['lw2'], d['lme']) for d in res]
        for i, d in enumerate(res):
            good &= d['tails'] and (d['window'] or control)
            tail_ok = all(res[j]['h1'] and res[j]['h2'] and worsts[j] < 0 for j in range(i, len(res)))
            tail_ok &= all(worsts[j + 1] < worsts[j] for j in range(i, len(res) - 1))
            if tail_ok and hyp_from is None:
                hyp_from = d['E']
            rows.append("delta = %s, lam = 10^-%d: n = %d, log10 of w/m0 (Theorem 1) %s, (Theorem 2) %s, max_j"
                        " lam^j eps_(2j)^2/m0 %s; eps_4 <= lam: %s, eps_(M_P) <= lam^3: %s"
                        % (mp.nstr(delta, 2), d['E'], d['n'], mp.nstr(d['lw1'], 6), mp.nstr(d['lw2'], 6),
                           mp.nstr(d['lme'], 6), d['h1'], d['h2']))
        good &= worsts[-1] < -1000 and hyp_from is not None
        ok &= good
    # the local first-degree profiles on J_n: env and every derivative vanish there when the bumps are disjoint.
    L10 = mp.mpf(100)
    n = int(mp.ceil(mp.sqrt(mp.mpf('3.1')*L10*mp.log(10))))
    h = lambda m: mp.exp(-m*m)                                                     # noqa: E731
    beta = lambda t: mp.exp(-1/(1 - t*t)) if abs(t) < 1 else mp.mpf(0)            # noqa: E731

    def env(x, extra):
        tot = mp.mpf(0)
        for m in range(n - 3, n + 4):
            tot += h(m)*beta(2**(m + 2)*(x - mp.mpf(2)**-m))
        if extra:
            tot += h(n)/2*beta(10*mp.mpf(2)**n*(x - mp.mpf('1.375')*mp.mpf(2)**-n))
        return tot
    pts = [mp.mpf(2)**-n*(mp.mpf('1.26') + mp.mpf('0.23')*k/40) for k in range(41)]
    zero_on_J = all(env(x, False) == 0 for x in pts)
    if control:
        return ok or all(env(x, True) == 0 for x in pts)
    ok &= zero_on_J
    out("  T6 (round 7) L.25' (a) on J_n' (between bump n and bump n - 1): env vanishes at all 41 sample points: %s, so"
        " every oscillating profile of g_app vanishes there; lam_h(delta), below which h_n >= lam^(3.4 + delta): 10^%s"
        " (delta = 1/10), 10^%s (delta = 1/2); the means (L.3 (b), j-resolved) and the remainder w (L.4', L.4_P)"
        " against m0's lower bound, in log10, unit constants: " % (zero_on_J, mp.nstr(lamh[mp.mpf(1)/10], 4),
                                                                    mp.nstr(lamh[mp.mpf(1)/2], 4))
        + "; ".join(rows) + "; for each delta, from some lam of the grid on, every ratio below 0 with both"
        " hypotheses and decreasing, and below -1000 at the last: %s" % ok)
    return ok


# ------------------------------------------------------------------------------------------------------------ T7
def t7(control=False):
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import bandL4p5 as BL
    from fractions import Fraction as Fr
    h = Fr(4) if control else Fr(5)
    bad = {i: BL.admissible(i, h, triangular=False) for i in range(5)}
    nterms = sum(len(BL.terms(i, h)) for i in range(5))
    ok = all(not b for b in bad.values())
    if control:
        return ok
    out("  T7 L.17 (2): Lemma L.4's energy argument at levels 0-4 (the remainder w and its derivatives up to order 5)"
        " with eps_6 <= lam^5 (L.17's hypothesis eps_M <= lam^5): %d terms, every coefficient bounded (the"
        " non-triangular rule, every coefficient into Gronwall): %s" % (nterms, ok))
    return ok


def main():
    ok = True
    for name, f in (("T1", t1), ("T2", t2), ("T3", t3), ("T4", t4), ("T5", t5), ("T6", t6), ("T7", t7)):
        good = f()
        ctl = f(control=True)
        out("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""))
        ok &= good and not ctl
    out("degtwo5: %s  [%.0f s]" % ("all checks pass, every control fails" if ok else "FAILURES", time.time() - T0))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
