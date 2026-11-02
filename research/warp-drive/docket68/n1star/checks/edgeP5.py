#!/usr/bin/env python3
"""edgeP5.py -- the very edge of the equality layer for Theorem 2's solution (EQUALITY5-LAYER.md, Round 4, R4.1:
Lemma L.15_P, the exact re-summation; Lemma L.16, the kernel lemma; Theorem L_E).

Theorem 2's first-degree solution has nothing coming in but the wave, its operators are the static seed's, and B :=
P^-1 Q (P^-1 the transport from past null infinity) commutes with d_v.  So the first-degree term is, exactly,
lam e^(i v/lam) (s - B)^-1 s H_1 with s = d_v + i/lam acting on the envelope, and at the horizon its scalar part is
lam A sum_n I_n(v) b_n plus a remainder bounded by an energy estimate, I_n := s^-n env.  Everything about the very edge
then reduces to one-dimensional integrals of env.

  Q1 (exact; the three-component model of veryedge5 V2, which has the record's structure, data from infinity) The
     record's recursion T(H_(j+1)) = -R_X(H_j) with nothing coming in equals, in every component and for j <= 10, the
     closed form H_2 = -i B H_1, H_(j+1) = i (d_v - B) H_j (j >= 2): the series sum_j lam^j H_j is the lam-expansion
     of lam (s - B)^-1 s H_1.  And with P B^n H_1 = Q B^(n-1) H_1, P H_1 = 0 (computed), the partial sums X_M :=
     sum_(n<=M) s^-n B^n H_1 satisfy P(s X_M) - Q X_M = -s^-M Q B^M H_1 for every M (the telescoping, here at M = 6
     with s a formal symbol).  Controls (mutations of the computed path): slice data (r0 = v - tau0) break the closed
     form; B built with P's mass coupling dropped breaks it.
  Q2 (computed, mpmath; sampled) Lemma L.16 for three log-concave flat edges -- exp(-1/x), exp(-1/x^2) and the
     record's C_c^inf envelope near v_s -- at lam = 1e-3 and 1e-6 and lam kappa = 1e-2 ... 1e4 (kappa := env'/env):
     (a) |I_n| <= env/kappa^n and |I_n| <= 2 env min(lam, 1/kappa)^n (n = 2, 3); (b) rho_2 := I_2 s~^2/env - 1, s~ :=
     kappa + i/lam, obeys |rho_2| <= R_2(v) := int_0^x [kappa^-1 (psi'' + psi'^2) + psi' + u (psi'' + psi'^2)] env(v -
     u)/env(v) du, psi' = kappa(v - u) - kappa(v), psi'' = |kappa'(v - u)| (the bound the proof gives, independent of
     lam), and R_2(v) kappa^(1-a) stays bounded (a = 1/2, 1/3, 1/2).  Controls: the frozen local form (s~ := i/lam,
     the lam-expansion's leading term) is off by more than 1 at the very edge; a flat edge that is not log-concave,
     exp(-1/x)(2 + sin(1/x)), violates (b).
  Q3 (computed, mpmath; a model with unit constants) Alternation: a(v) := Re[c lam J_2(v)]/9 - m0(v) -+ D2(v), J_2 :=
     e^(i v/lam) I_2 (the exact first-degree term at the horizon for |nu_inf d| = 1/9, mu0 = A = 1), m0 := (env^2 + x
     env^2)/9, D2 := 10 (1 + lam kappa)^2 env^2 (a degree-two term, generous), over three carrier periods at five depths
     from the ordered regime (env = lam^4) to lam kappa = 1000, for c = 1, i, e^(i pi/4) and both signs of D2: every
     period has points with a > 0 (timelike) and points with a < 0.  J_2 by exact Taylor steps J_2(v + h) = J_2(v) +
     h J_1(v) + int (v + h - v') e^(i v'/lam) env(v') dv'.  Controls: c = 0 (no first-degree term) gives no positive
     point; D2 multiplied by 10^6 lam^-3 gives none.
  Q4 (computed, mpmath) Why Lemma L.18_P (localisation) is needed at depths below lam: at x = lam/10 (exp(-1/x),
     lam = 1e-6) the remainder bound of Lemma L.4_P, which reaches env at v + c lam, squared, exceeds the first-degree
     term by a factor above 10^100000, while the localised bound (1 + lam kappa)^2 env(v)^2 lies below it by a factor
     below 10^-1000.  Control: at x = 10 lam the nonlocal bound is below the term (the localisation is needed only in
     the deepest part).

Labels: Q1 computed (exact rationals); Q2 computed, sampled (a check of the deduced Lemma L.16 on three classes);
Q3, Q4 computed (mpmath), models with unit constants.  Run: python3 checks/edgeP5.py   (about four minutes)
"""
import os
import sys
import textwrap
import time

import mpmath as mp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import veryedge5 as V                                                             # noqa: E402

T0 = time.time()


def out(msg):
    print(textwrap.fill(msg, width=121, subsequent_indent="      ", break_on_hyphens=False), flush=True)


# ------------------------------------------------------------------------------------------------------------ Q1
def B_inf(Z, mass=True):
    """B Z := P^-1 Q Z, P^-1 the transport from infinity (decay), in the model"""
    if mass:
        return V.solveP(V.Q_(Z), None, True)
    S = V.Q_(Z)
    Sa, Sb, Sc = S
    b = V.mono(V.integ(V.mono(Sb, 3), True), -3)
    c = V.mono(V.integ(V.mono(Sc, 1), True), -1)
    a = V.mono(V.integ(V.mono(Sa, 3), True), -3)          # mutation: P's mass coupling 2 mu b/r^3 dropped
    return [a, b, c]


def P_apply(Z):
    return V.P_(Z)


def eq(X, Y):
    return all(V.add(x, V.scale(y, V.R_(-1))) == {} for x, y in zip(X, Y))


def closed_form(J, mass=True):
    H1 = [{}, {}, {(-1, 0, 0): V.ONE}]
    G = [H1, [V.scale(x, (V.Fr(0), V.Fr(-1))) for x in B_inf(H1, mass)]]
    for _ in range(2, J):
        Gj = G[-1]
        dv = [V.d_v(x) for x in Gj]
        BG = B_inf(Gj, mass)
        G.append([V.scale(V.add(x, V.scale(y, V.R_(-1))), V.IM) for x, y in zip(dv, BG)])
    return G


def q1(control=False):
    J = 10
    if control:
        Hs = V.run_model(J, past=False)
        Hp = V.run_model(J, past=True)
        Gm = closed_form(J, mass=False)
        G = closed_form(J)
        return all(eq(Hs[j], G[j]) for j in range(J)) or all(eq(Hp[j], Gm[j]) for j in range(J))
    H = V.run_model(J, past=True)
    G = closed_form(J)
    match = all(eq(H[j], G[j]) for j in range(J))
    nontriv = any(H[J - 1][k] for k in range(3)) and any(G[2][k] for k in range(3))
    # telescoping: P B^n H1 = Q B^(n-1) H1 and P H1 = 0, hence P(s X_M) - Q X_M = -s^-M Q B^M H1
    H1 = [{}, {}, {(-1, 0, 0): V.ONE}]
    Bn = [H1]
    for _ in range(6):
        Bn.append(B_inf(Bn[-1]))
    tele = all(V.add(*x) == {} for x in P_apply(H1)) if False else all(x == {} for x in P_apply(H1))
    tele &= all(eq(P_apply(Bn[k]), V.Q_(Bn[k - 1])) for k in range(1, 7))
    # the formal identity, coefficient of s^(1-n): P B^n H1 - Q B^(n-1) H1 = 0 (n = 1..M); of s^-M: -Q B^M H1
    decay = all(all(k[0] < -1 for k in comp) for b in Bn[1:] for comp in b)
    out("  Q1 model, data from infinity, j <= %d: record's recursion = closed form H_2 = -i B H_1, H_(j+1) = i (d_v -"
        " B) H_j in every component: %s (nontrivial: %s); P H_1 = 0 and P B^n H_1 = Q B^(n-1) H_1, n = 1..6 (the"
        " telescoping of P(s X_M) - Q X_M): %s; B^n H_1 decay faster than r^(-1/2) (nothing coming in): %s"
        % (J, match, nontriv, tele, decay))
    return match and nontriv and tele and decay


# ------------------------------------------------------------------------------------------------------------ Q2
mp.mp.dps = 30


class Edge:
    """a flat edge at x = 0: log env, kappa = (log env)', |kappa'|, and the class constants (alpha, c_R)"""

    def __init__(self, name, ell, kap, dkap, alpha, cR):
        self.name, self.ell, self.kap, self.dkap, self.alpha, self.cR = name, ell, kap, dkap, alpha, cR

    def x_of(self, kappa):
        lo, hi = mp.mpf('1e-30'), mp.mpf('0.6')
        for _ in range(200):
            mid = mp.sqrt(lo*hi)
            if self.kap(mid) > kappa:
                lo = mid
            else:
                hi = mid
        return hi


def rec_ell(x):
    t = 2*x/3
    return 12*mp.log(mp.sin(mp.pi*t/2)) + 1 - 1/(t*(2 - t))


def rec_kap(x):
    t = 2*x/3
    return mp.mpf(2)/3*(6*mp.pi*mp.cot(mp.pi*t/2) + 2*(1 - t)/(t**2*(2 - t)**2))


def rec_dkap(x):
    t = 2*x/3
    # d/dx of rec_kap: (2/3)^2 [ -3 pi^2 csc^2(pi t/2) + d/dt (2 (1 - t)/(t^2 (2 - t)^2)) ]
    g = lambda tt: 2*(1 - tt)/(tt**2*(2 - tt)**2)                                  # noqa: E731
    return abs((mp.mpf(2)/3)**2*(-3*mp.pi**2/mp.sin(mp.pi*t/2)**2 + mp.diff(g, t)))


EDGES = [
    Edge("exp(-1/x)", lambda x: -1/x, lambda x: 1/x**2, lambda x: 2/x**3, mp.mpf(1)/2, mp.mpf(2)),
    Edge("exp(-1/x^2)", lambda x: -1/x**2, lambda x: 2/x**3, lambda x: 6/x**4, mp.mpf(1)/3, 6/mp.mpf(2)**(mp.mpf(4)/3)),
    Edge("record C_c^inf", rec_ell, rec_kap, rec_dkap, mp.mpf(1)/2, None),
]
CONTROL_EDGE = Edge("exp(-1/x)(2 + sin(1/x))", lambda x: -1/x + mp.log(2 + mp.sin(1/x)),
                    lambda x: (1 - mp.cos(1/x)/(2 + mp.sin(1/x)))/x**2,
                    lambda x: abs(mp.diff(lambda y: (1 - mp.cos(1/y)/(2 + mp.sin(1/y)))/y**2, x)), mp.mpf(1)/2, None)


def I_n(edge, x, lam, n, kappa_eff=None):
    """I_n/env at depth x: int_0^U u^(n-1)/(n-1)! e^(-i u/lam) env(x - u)/env(x) du (U: env(x - u)/env(x) < e^-100)"""
    kap = edge.kap(x) if kappa_eff is None else kappa_eff
    U = min(x*(1 - mp.mpf(10)**-20), 100/kap)
    nper = int(mp.ceil(U/(mp.pi*lam)))
    nseg = max(8, min(nper, 6000))
    pts = [U*k/nseg for k in range(nseg + 1)]
    l0 = edge.ell(x)
    fac = mp.factorial(n - 1)
    g = lambda u: u**(n - 1)/fac*mp.expj(-u/lam)*mp.exp(edge.ell(x - u) - l0)     # noqa: E731
    return mp.quad(g, pts)


def R2_bound(edge, x):
    """the lam-free bound of the proof: int_0^x [k^-1 (psi'' + psi'^2) + psi' + u (psi'' + psi'^2)] phi du"""
    k0 = edge.kap(x)
    l0 = edge.ell(x)
    U = min(x*(1 - mp.mpf(10)**-20), 100/k0)

    def h(u):
        p1 = edge.kap(x - u) - k0
        p2 = edge.dkap(x - u)
        return ((p2 + p1**2)/k0 + p1 + u*(p2 + p1**2))*mp.exp(edge.ell(x - u) - l0)
    return mp.quad(h, [U*k/16 for k in range(17)])


def cR_record():
    """c_R for the record's edge, sampled: sup |kappa'|/kappa^(3/2) on x in (0, 0.3]"""
    xs = [mp.mpf('0.3')*mp.mpf(10)**(-mp.mpf(k)/20) for k in range(0, 200)]
    return max(rec_dkap(x)/rec_kap(x)**mp.mpf('1.5') for x in xs)


def q2(control=False):
    if control:
        lam = mp.mpf('1e-3')
        bad = False
        e = EDGES[0]
        for lk in (10, 100, 1000):
            x = e.x_of(lk/lam)
            frozen = -lam**2                                        # (i/lam)^-2: the lam-expansion's leading term
            bad |= abs(I_n(e, x, lam, 2)/frozen - 1) <= 1
        ce = CONTROL_EDGE
        worst = mp.mpf(0)
        for lk in (1, 3, 10, 30, 100):
            for shift in (0, 1, 2, 3):
                x = ce.x_of(lk/lam)*(1 + mp.mpf(shift)/40)
                k0 = ce.kap(x)
                st = k0 + 1j/lam
                rho = I_n(ce, x, lam, 2, kappa_eff=k0)*st**2 - 1
                worst = max(worst, abs(rho) - R2_bound_nonlc(ce, x))
        return (not bad) and worst <= 0
    EDGES[2].cR = cR_record()
    ok = True
    rows = []
    for e in EDGES:
        worst_a, worst_b, worst_rho, worst_scaled = mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0)
        for lam in (mp.mpf('1e-3'), mp.mpf('1e-6')):
            for lk in (mp.mpf('1e-2'), mp.mpf('1e-1'), 1, 10, 100, 1000, 10000):
                x = e.x_of(lk/lam)
                k0 = e.kap(x)
                if x > mp.mpf('0.5'):
                    continue
                st = k0 + 1j/lam
                mn = min(lam, 1/k0)
                for n in (2, 3):
                    In = I_n(e, x, lam, n)
                    worst_a = max(worst_a, abs(In)*k0**n)
                    worst_b = max(worst_b, abs(In)/mn**n)
                    if n == 2:
                        rho = In*st**2 - 1
                        R2 = R2_bound(e, x)
                        worst_rho = max(worst_rho, abs(rho)/R2)
                        worst_scaled = max(worst_scaled, R2*k0**(1 - e.alpha))
        good = worst_a <= 1 and worst_b <= 2 and worst_rho <= 1
        ok &= good
        rows.append("%s (a = %s, c_R %s): max |I_n| kappa^n/env = %s, max |I_n|/(env min(lam,1/kappa)^n) = %s, max"
                    " |rho_2|/R_2 = %s, max R_2 kappa^(1-a) = %s" % (
                        e.name, mp.nstr(e.alpha, 3), mp.nstr(e.cR, 4), mp.nstr(worst_a, 5), mp.nstr(worst_b, 5),
                        mp.nstr(worst_rho, 4), mp.nstr(worst_scaled, 5)))
    out("  Q2 " + "; ".join(rows) + "  [%.0f s]" % (time.time() - T0))
    return ok


def R2_bound_nonlc(edge, x):
    """R_2 as defined (with |kappa'| and kappa(v - u) - kappa(v)), for an edge that need not be log-concave"""
    k0 = edge.kap(x)
    l0 = edge.ell(x)
    U = min(x*(1 - mp.mpf(10)**-20), 100/k0)

    def h(u):
        p1 = abs(edge.kap(x - u) - k0)
        p2 = edge.dkap(x - u)
        return ((p2 + p1**2)/k0 + p1 + u*(p2 + p1**2))*mp.exp(edge.ell(x - u) - l0)
    return mp.quad(h, [U*k/32 for k in range(33)])


# ------------------------------------------------------------------------------------------------------------ Q3
def J_track(edge, x0, lam, periods=3, per=96):
    """J_1, J_2 = e^(i v/lam) I_1, I_2 on [x0, x0 + 2 pi lam periods], exact Taylor steps; env normalised at x0"""
    l0 = edge.ell(x0)
    f = lambda x: mp.exp(edge.ell(x) - l0)                                         # noqa: E731
    I1 = I_n(edge, x0, lam, 1)
    I2 = I_n(edge, x0, lam, 2)
    J1, J2 = mp.expj(x0/lam)*I1, mp.expj(x0/lam)*I2
    h = 2*mp.pi*lam/per
    xs, J2s = [x0], [J2]
    x = x0
    for _ in range(periods*per):
        a1 = mp.quad(lambda y: mp.expj(y/lam)*f(y), [x, x + h/2, x + h])
        a2 = mp.quad(lambda y: (x + h - y)*mp.expj(y/lam)*f(y), [x, x + h/2, x + h])
        J2 = J2 + h*J1 + a2
        J1 = J1 + a1
        x = x + h
        xs.append(x)
        J2s.append(J2)
    return xs, J2s, f, l0


def q3(control=False):
    lam = mp.mpf('1e-6')
    e = EDGES[0]
    depths = {"env = lam^4 (ordered)": 1/(4*mp.log(1/lam)), "lam kappa = 1": e.x_of(1/lam),
              "lam kappa = 10": e.x_of(10/lam), "lam kappa = 100": e.x_of(100/lam),
              "lam kappa = 1000": e.x_of(1000/lam)}
    phases = {"1": 1, "i": 1j, "e^(i pi/4)": mp.expjpi(mp.mpf(1)/4)}
    if control:
        phases = {"0": 0}
    res = {}
    for nm, x0 in depths.items():
        xs, J2s, f, l0 = J_track(e, x0, lam)
        E0 = mp.exp(l0)
        for cn, c in phases.items():
            for sgn in (1, -1):
                good = True
                for p in range(3):
                    seg = range(p*96, (p + 1)*96 + 1)
                    vals = []
                    for k in seg:
                        x = xs[k]
                        env = f(x)*E0
                        kap = e.kap(x)
                        m0 = (env**2 + x*env**2)/9
                        D2 = 10*(1 + lam*kap)**2*env**2
                        if control is True and cn == "1":
                            D2 *= mp.mpf(10)**6/lam**3
                        vals.append(mp.re(c*lam*J2s[k]*E0)/9 - m0 - sgn*D2)
                    good &= any(vv > 0 for vv in vals) and any(vv < 0 for vv in vals)
                res[(nm, cn, sgn)] = good
    if control:
        # second control: the degree-two term inflated by 10^6 lam^-3 at the ordered depth, c = 1
        xs, J2s, f, l0 = J_track(e, depths["env = lam^4 (ordered)"], lam, periods=1)
        E0 = mp.exp(l0)
        vals = [mp.re(lam*J2s[k]*E0)/9 - 10*mp.mpf(10)**6/lam**3*(f(xs[k])*E0)**2 for k in range(len(xs))]
        return any(res.values()) or (any(vv > 0 for vv in vals) and any(vv < 0 for vv in vals))
    ok = all(res.values())
    out("  Q3 every one of 3 carrier periods has timelike and spacelike points, 5 depths x 3 phases x 2 signs of D2: %s"
        " (%d cases)  [%.0f s]" % (ok, len(res), time.time() - T0))
    return ok


# ------------------------------------------------------------------------------------------------------------ Q4
def q4(control=False):
    lam = mp.mpf('1e-6')
    x = 10*lam if control else lam/10
    env = mp.exp(-1/x)
    kap = 1/x**2
    term = lam*env/(kap**2 + lam**-2)/9              # |first-degree term| >= this (Lemma L.16, |rho_2| <= 1/2 halved)
    nonlocal_ = mp.exp(-2/(x + lam))                  # (env at v + c lam)^2, c = 1
    local = (1 + lam*kap)**2*env**2
    r_non = mp.log10(nonlocal_/term)
    r_loc = mp.log10(local/term)
    if control:
        return r_non > 0
    out("  Q4 at x = lam/10, lam = 1e-6: log10(nonlocal bound/term) = %s, log10(localised bound/term) = %s"
        % (mp.nstr(r_non, 8), mp.nstr(r_loc, 8)))
    return r_non > 100000 and r_loc < -1000


def main():
    ok = True
    for name, f in (("Q1", q1), ("Q2", q2), ("Q3", q3), ("Q4", q4)):
        good = f()
        ctl = f(control=True)
        out("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""))
        ok &= good and not ctl
    out("edgeP5: %s  [%.0f s]" % ("all checks pass, every control fails" if ok else "FAILURES", time.time() - T0))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
