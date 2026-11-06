#!/usr/bin/env python3
"""degtwo5.py -- the degree-two and localisation lemmas, the transition and the dips (EQUALITY5-LAYER.md, Round 5,
R5.2 and R5.4: Lemmas L.15_P (b), L.17, L.18 written in full; Theorem L.24 (one switch per column); Proposition L.25
(envelopes with dips)).

  T1 (exact; a three-dimensional instance of a dimension-free identity) The reduced Ricci operator relative to a
     background gb is quasilinear: Ric^H(g) + (1/2) g^ab d_a d_b g_mn contains no second derivative of g, for a
     general metric g(x, y) on R^3 (six free functions) against the flat background.  So the quadratic remainder
     N(u) := Ric^H(gb + u) - dRic^H(u) obeys |N(u)| <= C (|u| |d^2 u| + |du|^2 + |u|^2), with no (d^2 u)^2 term.
     Control: Ric itself (without the gauge term) keeps second derivatives outside g^ab d_a d_b.
  T2 (exact) The seed with mu(v) against the static seed mu0: every component of Gamma[g0] - Gamma[g0 deg] is
     (mu - mu0) times a function of (r, th) plus mu' times one, and nothing else; so Ric^H relative to g0 and relative
     to g0deg differ by A(g), linear in (mu - mu0, mu', mu''), local in v (the mu-terms of L.17).  Control: against a
     wrong background (mu0 + 1 in place of mu0) the difference has a constant term.
  T3 (exact) The tilted face with any tilt: for alpha = dv + e psi' dtau, g0^-1(alpha, alpha) = -2 e psi' - e^2 psi'^2
     (1 + mu/r^2) and |alpha|_e^2 = (1 + e psi')^2 + 1; if |(g - g0)^-1(beta, beta)| <= D psi' |beta|_e^2 (the weight
     psi' = t^(-3/2) on P, 1 on Omega) and e >= 2 D, e psi' <= 1/2, then g^-1(alpha, alpha) < 0.  Control: e = D
     admits a positive value.
  T4 (computed, mpmath; unit constants, lam = 1e-6, N = 9, c = 30, C = 10^3) The descent of Lemma L.18: y_(k+1) defined
     by 1/kappa(v_s + y_(k+1)) = 6 delta_(k+1), delta_(k+1) := C kappa(v_s + 3 y_k)^c env(v_s + 3 y_k), from y_0 =
     10^-2; for exp(-1/x) and the record's C_c^inf envelope, y_(k+1) < y_k/2 for k < 8 and y_k -> 0 faster than any
     geometric sequence; hypothesis (H_D) sampled: kappa(v_s + y/2) kappa(v_s + 3y)^c env(v_s + 3y) decreasing to 0.
     Control: env = x^40 (smooth, not flat at that order) stalls (y_1 > y_0/2).
  T5 (computed; unit constants) The transition (Theorem L.24): with m0 = sqrt(mu/mu0) - 1 + 2 r_q', mu = 1 + (2/9) int
     env^2, A = mu0 = 1, the record's envelope and exp(-1/x): m0'/m0 >= 1.9 kappa where R in [0.9, 1.1], so m0' -
     |S'| >= 0.85 kappa m0 for S = lam^3 nu env (|S'| = kappa |S|); and in a model g^-1 = -m0 - Re[S e^(i v/lam)] + rho,
     rho a slowly varying degree-two term of size lam^(1/10) m0 plus a structureless one of size lam^3 m0, the maxima
     over consecutive carrier periods decrease through the band and change sign once (lam = 1e-6, exp(-1/x)).  Control:
     rho structureless of size m0/3 gives more than one sign change.
  T6 (computed, bounds) Dips (Proposition L.25): env := sum_n exp(-4^n) beta(2^(n+2) (x - 2^-n)) near v_s (beta the
     standard bump on [-1, 1]; C_c^inf, zero on intervals J_n between the bumps); at lam = 1e-6 the bump with height
     in [lam^3.5, lam^3.1] has n = 6; on J_6 the first-degree term is at most lam^5 sup|d_u^4 (u bump)| (four
     integrations by parts of I_2) and the U1-memory at most lam^(N+1) lam^4 sup|bump^(N+4)| (Lemma 6.4's Green's
     function is lam-independent), while m0 >= (1/9) int bump^2: the boundary is spacelike on every window of J_6 at
     every angle.  Control: on the bump itself (env = h_6 at its top) the margin does not dominate (timelike points).

Labels: T1-T3 computed (exact, sympy); T4, T6 computed (mpmath, bounds; T4 a model with unit constants); T5 computed
(mpmath; m0's formula exact, S a model).  Run: python3 checks/degtwo5.py   (a few minutes)
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
    f = {}
    g = sp.zeros(3)
    for i in range(3):
        for j in range(i, 3):
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
            e = M[m, n] + sum(gi[a, b]*sp.diff(g[m, n], X[a], X[b]) for a in range(3) for b in range(3))/2
            e = sp.expand(sp.together(e))
            sec = [d for d in e.atoms(sp.Derivative) if sum(c for _, c in d.variable_count) >= 2]
            num = sp.numer(sp.together(e))
            num = sp.expand(num)
            rep = {d: sp.Symbol('S%d' % k) for k, d in enumerate(sec)}
            num2 = num.xreplace(rep)
            ok &= all(sp.expand(sp.diff(num2, s_)) == 0 for s_ in rep.values())
    if control:
        return ok
    out("  T1 Ric^H(g) + (1/2) g^ab d_a d_b g_mn free of second derivatives (R^3, general g(x, y), flat background): %s"
        "  [%.0f s]" % (ok, time.time() - T0))
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
                ok &= sp.simplify(sp.diff(e, dm, 2)) == 0 and sp.simplify(sp.diff(e, mp1, 2)) == 0
                ok &= sp.simplify(sp.diff(e, dm, mp1)) == 0 and sp.simplify(e.subs({dm: 0, mp1: 0})) == 0
    if control:
        return ok
    out("  T2 Gamma[g0] - Gamma[g0deg] linear in (mu - mu0, mu') with no constant term, every component: %s" % ok)
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


def t4(control=False):
    mp.mp.dps = 40
    C, c = mp.mpf(10)**3, 30
    edges = [("exp(-1/x)", lambda x: -1/x), ("record C_c^inf", rec_ell)]
    if control:
        edges = [("x^40", lambda x: 40*mp.log(x))]
    rows, ok = [], True
    for nm, ell in edges:
        kap = lambda x: mp.diff(ell, x)                                            # noqa: E731
        y = mp.mpf('0.01')
        ys = [y]
        good = True
        for k in range(8):
            ldel = mp.log(C) + c*mp.log(kap(3*y)) + ell(3*y)                     # log delta_(k+1)
            # y_(k+1): 1/kappa(y) = 6 delta, i.e. log kappa(y) = -log 6 - log delta; kappa decreasing in y
            target = -mp.log(6) - ldel
            lo, hi = mp.mpf('1e-300'), y
            if mp.log(kap(hi)) >= target:
                yn = hi
            else:
                for _ in range(400):
                    mid = mp.sqrt(lo*hi) if lo > 0 else hi/2
                    if mp.log(kap(mid)) > target:
                        lo = mid
                    else:
                        hi = mid
                yn = hi
            good &= yn < y/2
            y = yn
            ys.append(y)
            if y < mp.mpf('1e-250'):
                break
        hd = [kap(t/2)*kap(3*t)**c*mp.exp(ell(3*t)) for t in (mp.mpf('0.01'), mp.mpf('0.003'), mp.mpf('0.001'))]
        dec = hd[0] > hd[1] > hd[2]
        ok &= good and (dec or control)
        rows.append("%s: y_k = %s; y_(k+1) < y_k/2 throughout: %s; (H_D) quantity at 0.01, 0.003, 0.001: %s" % (
            nm, [mp.nstr(t, 3) for t in ys[:5]], good, [mp.nstr(h, 3) for h in hd]))
    if control:
        return ok
    out("  T4 descent (unit constants C = 10^3, c = 30): " + "; ".join(rows))
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
def bump(t):
    return mp.exp(-1/(1 - t*t)) if abs(t) < 1 else mp.mpf(0)


def t6(control=False):
    mp.mp.dps = 40
    lam = mp.mpf(10)**-6
    N = 9
    n = None
    for k in range(1, 12):
        h = mp.exp(-mp.mpf(4)**k)*bump(0)
        if lam**mp.mpf('3.5') <= h <= lam**mp.mpf('3.1'):
            n = k
            break
    if n is None:
        return False
    hn = mp.exp(-mp.mpf(4)**n)
    s = mp.mpf(2)**(n + 2)
    # sup |d_u^4 (u b(s u))| on the bump's support (u <= 2^-n + 1/s): Leibniz, sup |b^(j)| sampled finely
    supb = []
    for j in range(N + 5):
        supb.append(max(abs(mp.diff(bump, t, j)) for t in [mp.mpf(i)/200 - mp.mpf(0.995) for i in range(399)]))
    umax = mp.mpf(2)**(1 - n)
    d4 = hn*(umax*s**4*supb[4] + 4*s**3*supb[3])
    first = lam*lam**4*d4/9                                    # lam |I_2| |nu_inf d| <= lam * lam^4 int|d^4(...)| / 9
    umem = lam**(N + 1)*lam**4*hn*s**(N + 4)*supb[N + 4]*(2/s)
    width = 2/s
    l2 = hn**2*mp.quad(lambda t: bump(t)**2, [-1, 1])/s
    m0low = 2*l2/27                                            # m0 >= (mu - mu0)/(3 mu0) = (2/27) int env^2
    if control:
        # on the bump's top: env = h_n, the first-degree term lam^3 env/9 against m0 <= (h_n^2 (1 + 2/s))/9
        return lam**3*hn*bump(0)/9 < hn**2*(1 + width)/9
    ok = first + umem < m0low/2
    out("  T6 the bump with height in [lam^3.5, lam^3.1] at lam = 1e-6: n = %d (h = %s = lam^%s); on J_n: first-degree"
        " term <= %s, U1-memory <= %s, m0 >= %s: spacelike throughout: %s" % (
            n, mp.nstr(hn*bump(0), 4), mp.nstr(mp.log(hn*bump(0))/mp.log(lam), 4), mp.nstr(first, 3),
            mp.nstr(umem, 3), mp.nstr(m0low, 3), ok))
    return ok


def main():
    ok = True
    for name, f in (("T1", t1), ("T2", t2), ("T3", t3), ("T4", t4), ("T5", t5), ("T6", t6)):
        good = f()
        ctl = f(control=True)
        out("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""))
        ok &= good and not ctl
    out("degtwo5: %s  [%.0f s]" % ("all checks pass, every control fails" if ok else "FAILURES", time.time() - T0))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
