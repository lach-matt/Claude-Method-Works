#!/usr/bin/env python3
"""twohorizon5: the record's Proposition 8.1 (one zero per column of the outgoing expansion) for two families: the
facts the deduction in FAMILIES5-FULL.md section 9 uses.

  H1 (exact) the background on its columns. Where the outgoing dust vanishes (region III, u >= u2) the two-dust
     background is g0 = -e^(2 psi) f dvhat^2 + 2 e^psi dvhat dR + R^2 dOmega_3^2, f = 1 - mu/R^2, psi <= 0 and mu
     functions of vhat (twobg5 G1 (a)-(b)). The sphere S = {vhat, R} has one outgoing null covector dR + alpha dvhat,
     alpha = -e^psi f/2, and the ingoing one dvhat. With n normalised by n(tau) = 1, tau = vhat - R: theta+ = c 3 f/(2R),
     c = 2 R^2 e^psi/(R^2 (2 - e^psi) + mu e^psi) > 0 (psi <= 0); its one zero on (0, oo) is R^2 = mu, simple, with
     d_R theta+ = 3 e^psi/mu there (the record's 3/mu at psi = 0, horizon5.py H1); the future ingoing normal has
     expansion -3/R < 0. Control (must fail): the ingoing normal's expansion does not vanish at R^2 = mu.
  H2 (exact, symbolic in every function) g0's expansion along g0^-1 du is -3 e^(-2 sig) R_v/R (so the normalised
     theta+ is a positive multiple of R_v); on stage0two5.py's general round double-null background with both families'
     stage-0 waves (W_in = TT(s1) + chi dv^2, W_out = TT(s2) + chi' du^2), the expansions along g^-1 du (outgoing) and
     g^-1 dv (ingoing) have no lam^-1 term and no lam^0 term beyond g0's: theta(g0 + lam W) = theta(g0) + O(lam). The
     reason: the fast derivatives enter only as (1/2) g0^-1(k, d phase) F tr_S W, and tr_S W_k = 0 for both families.
     Control: the outgoing wave with a trace on the spheres (t z2 gamma0 added) gives a lam^0 oscillation in the
     ingoing expansion (g0^-1(dv, du) != 0); in the outgoing one it does not (g0^-1(du, du) = 0).
  H3 (symbolic up to three sample points, then 30 digits) with both families' stage-0 waves and ghat_2's mixed harmonics
     fixed by stage 0's division (ghat = e^(2 sig) R^(0)_(n1,n2)/(n1 n2), stage0two5 T4, T7), the lam^1 coefficient of
     the expansion along g^-1 du has no harmonic depending on s2: its mixed harmonics (n1, n2), n1 n2 != 0, and its pure
     (0, n2) harmonics are below 1e-20 at each point (concrete smooth functions for sig, R, H, the amplitudes and the
     chi's), against harmonics in s1 alone of order one; no lam^-1 term and no lam^0 oscillation either. So along a
     column {vhat fixed}, where s1 is constant and u is not, the outgoing expansion's O(lam) term contributes O(lam) to
     d_R theta+, and the record's band argument needs no placement of the outgoing packet.
     Control (must fail): with ghat_2 dropped the mixed harmonics are of order one: the cancellation is the division's.

Labels: computed (H1, H2 exact, sympy; H3 symbolic up to the points, then 30 digits: evidence at three points, not a
proof for every function). Run: python3 checks/twohorizon5.py   (about half an hour)
"""
import os
import sys
import time

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def zero(e):
    e = sp.expand(e)
    return e == 0 or sp.simplify(e) == 0


def h1():
    vh, R, th, p1, p2 = sp.symbols("vhat R theta phi1 phi2", real=True)
    X = [vh, R, th, p1, p2]
    psi, mu = sp.Function("psi")(vh), sp.Function("mu")(vh)
    f = 1 - mu/R**2
    g = sp.zeros(5)
    g[0, 0], g[0, 1], g[1, 0] = -sp.exp(2*psi)*f, sp.exp(psi), sp.exp(psi)
    g[2, 2], g[3, 3], g[4, 4] = R**2, R**2*sp.cos(th)**2, R**2*sp.sin(th)**2
    gi = sp.simplify(g.inv())
    alpha = sp.Symbol("alpha")
    kk = lambda al: [al, 1, 0, 0, 0]                                   # noqa: E731
    roots = sp.solve(sp.Eq(sum(gi[a, b]*kk(alpha)[a]*kk(alpha)[b] for a in range(5) for b in range(5)), 0), alpha)
    A = [2, 3, 4]
    dg = [[[sp.diff(g[a, b], X[c]) for c in range(5)] for b in range(5)] for a in range(5)]
    Gam = lambda c, a, b: sum(gi[c, d]*(dg[d][a][b] + dg[d][b][a] - dg[a][b][d]) for d in range(5))/2  # noqa: E731

    def theta(k):
        n = [sp.simplify(sum(gi[c, d]*k[d] for d in range(5))) for c in range(5)]
        cn = sp.simplify(1/(n[0] - n[1]))                              # n(tau) = 1, tau = vhat - R
        return sp.simplify(-cn*sum(Gam(c, a, a)*k[c]/g[a, a] for a in A for c in range(5))), sp.simplify(n[0] - n[1])
    tp, _ = theta(kk(roots[0]))
    base = 3*f/(2*R)
    ratio = sp.simplify(tp/base)
    zero_at = sp.simplify(tp.subs(mu, R**2)) == 0
    d_at = sp.simplify(sp.diff(tp, R).subs(mu, R**2))
    pos = sp.simplify(ratio.subs(mu, R**2))
    tin, dtau_in = theta([1, 0, 0, 0, 0])                              # k = dvhat, the ingoing null normal
    return dict(roots=roots, ratio=ratio, zero_at=zero_at, d_at=d_at, pos=pos, theta_in=tin, dtau_in=dtau_in,
                ctl=sp.simplify(tin.subs(mu, R**2)) == 0)


def theta_series(S0, W, Q=None, top=1):
    """expansions along g^-1 du and g^-1 dv of the spheres {u, v = const} for g = g0 + lam W + lam^2 Q, as coefficients
    of lam^-1..lam^top (unnormalised covectors du, dv)"""
    lam = sp.Symbol("lam")
    g0, g0i = S0.background()
    Q = sp.zeros(5) if Q is None else Q
    Dl = lam*W + lam**2*Q
    gi = g0i
    term = g0i
    for _ in range(top + 1):
        term = (-term*Dl*g0i).applyfunc(sp.expand)
        gi = gi + term
    gi = gi.applyfunc(lambda e: sum(sp.expand(e).coeff(lam, j)*lam**j for j in range(0, top + 2)))
    g = g0 + Dl
    A = [2, 3, 4]
    gA = sp.Matrix(3, 3, lambda i, j: g[A[i], A[j]])
    gA0i = sp.Matrix(3, 3, lambda i, j: g0i[A[i], A[j]])
    gAi = gA0i
    term = gA0i
    DA = sp.Matrix(3, 3, lambda i, j: Dl[A[i], A[j]])
    for _ in range(top + 1):
        term = (-term*DA*gA0i).applyfunc(sp.expand)
        gAi = gAi + term

    def D(e, c):
        out = S0.slow(e, c)
        if c in (0, 1):
            out += S0.fast(e, c)/lam
        return out
    res = {}
    for name, kk in (("out", 0), ("in", 1)):                          # k = du or dv
        tot = 0
        for i, a in enumerate(A):
            for j, b in enumerate(A):
                if gAi[i, j] == 0:
                    continue
                low = [D(g[d, a], b) + D(g[d, b], a) - D(g[a, b], d) for d in range(5)]
                Gk = sum(gi[kk, d]*low[d] for d in range(5))/2       # Gamma^c_ab k_c with k_c = delta_c^kk
                tot += -gAi[i, j]*Gk
        tot = sp.expand(tot)
        res[name] = {j: tot.coeff(lam, j) for j in range(-1, top + 1)}
    return res


def h2(control=False):
    import stage0two5 as S0
    W = S0.waves()
    if control:
        t = sp.Function("tr")(S0.u, S0.v, S0.th)
        g0, _ = S0.background()
        for a in (2, 3, 4):
            W[a, a] += t*S0.z2*g0[a, a]/3
    res = theta_series(S0, W, top=0)
    base = theta_series(S0, sp.zeros(5), top=0)
    nolm1 = all(zero(res[k][-1]) for k in res)
    l0 = {k: zero(res[k][0] - base[k][0]) for k in res}
    # the background: along g0^-1 du = -e^(-2 sig) d_v the expansion is -3 e^(-2 sig) R_v/R (R_v carries its sign)
    bg = zero(base["out"][0] + 3*sp.exp(-2*S0.sig)*sp.diff(S0.Rf, S0.v)/S0.Rf)
    l0["bg"] = bg
    return nolm1, l0


def theta_at_point(S0, g0, W, Q, pt, top=1):
    """the outgoing expansion -gamma^AB Gamma^u_AB (k = du) of {u, v = const} for g = g0 + lam W + lam^2 Q, with g0, W
    concrete functions of (u, v, th) (and z1, z2) and Q its value at pt: every derivative is taken first, then evaluated
    at pt to 30 digits, so the products are of numbers and Laurent polynomials in (z1, z2); lam^-1..lam^top
    coefficients (lam^1 exact: Q's slow derivatives would enter at lam^2)"""
    lam = sp.Symbol("lam")
    X = [S0.u, S0.v, S0.th]
    at = lambda e: sp.expand(sp.N(sp.sympify(e).subs(pt), 30))         # noqa: E731
    G = g0 + lam*W

    def D(e, c):
        out = sp.diff(e, X[c]) if c < 3 else 0
        if c in (0, 1):
            out += S0.fast(e, c)/lam
        return out
    dG = {}
    for a in range(5):
        for b in range(a, 5):
            for c in range(5):
                x = at(D(G[a, b], c)) + (lam*at(S0.fast(Q[a, b], c)) if c in (0, 1) else 0)
                dG[(c, a, b)] = dG[(c, b, a)] = sp.expand(x)
    g0p = g0.applyfunc(at)
    g0ip = g0p.inv()
    Dl = (lam*W.applyfunc(at) + lam**2*Q).applyfunc(sp.expand)
    gi, term = g0ip, g0ip
    for _ in range(top + 1):
        term = (-term*Dl*g0ip).applyfunc(sp.expand)
        gi = gi + term
    A = [2, 3, 4]
    gA0i = sp.Matrix(3, 3, lambda i, j: g0ip[A[i], A[j]])
    DA = sp.Matrix(3, 3, lambda i, j: Dl[A[i], A[j]])
    gAi, term = gA0i, gA0i
    for _ in range(top + 1):
        term = (-term*DA*gA0i).applyfunc(sp.expand)
        gAi = gAi + term
    tot = 0
    for i, a in enumerate(A):
        for j, b in enumerate(A):
            low = [dG[(b, d, a)] + dG[(a, d, b)] - dG[(d, a, b)] for d in range(5)]
            Gk = sum(gi[0, d]*low[d] for d in range(5))/2
            tot += -gAi[i, j]*Gk
    tot = sp.expand(tot)
    return {j: tot.coeff(lam, j) for j in range(-1, top + 1)}


SAMPLES = [  # (concrete functions, point)
    (lambda S0, u, v, th: {S0.sig: sp.Rational(1, 10)*u + sp.Rational(1, 5)*v, S0.Rf: 3 + u - v/2 + u*v/7,
                           S0.Hf: 1 + sp.cos(2*th)**2/3, S0.alpha: 1 + v/3, S0.beta: 2 - u/5, S0.xi2: 1 + u*v/3,
                           S0.xi2b: 2 - v, S0.et2: sp.Rational(1, 2) + u, S0.et2b: 1 + th},
     (sp.Rational(1, 3), sp.Rational(1, 2), sp.Rational(7, 10))),
    (lambda S0, u, v, th: {S0.sig: u*v/5 - v/7, S0.Rf: 2 + u**2/3 + v, S0.Hf: 2 - sp.sin(th)**2,
                           S0.alpha: 2 - v**2/5, S0.beta: 1 + u/2 + u**2/9, S0.xi2: u - th/3, S0.xi2b: v**2 + 1,
                           S0.et2: 3 - u*th, S0.et2b: v/2 - 1},
     (sp.Rational(-1, 4), sp.Rational(2, 3), sp.Rational(3, 10))),
    (lambda S0, u, v, th: {S0.sig: sp.Rational(1, 3) - u/9 + v**2/11, S0.Rf: 4 - u + v/3, S0.Hf: 1 + sp.cos(th)/5,
                           S0.alpha: sp.Rational(3, 2) + u*v/4, S0.beta: 1 - u/7, S0.xi2: 2 + v*th, S0.xi2b: u - 1,
                           S0.et2: v + th**2, S0.et2b: sp.Rational(5, 4)},
     (sp.Rational(1, 5), sp.Rational(-1, 3), sp.Rational(11, 10))),
]


def h3(control=False):
    """the lam^1 coefficient of the outgoing expansion: its harmonics depending on s2 (mixed (n1, n2), n1 n2 != 0, and
    pure (0, n2)), at three sample points; control: ghat_2 dropped (Q = 0)"""
    import stage0two5 as S0
    W = S0.waves()
    o = S0.ricci_orders(W)
    g0, _ = S0.background()
    Q = sp.zeros(5)
    if not control:
        for a in range(5):
            for b in range(a, 5):
                for n, cf in S0.harmonics(o[(a, b)][1]).items():
                    if n[0] and n[1]:
                        q = sp.exp(2*S0.sig)*cf/(n[0]*n[1])*S0.z1**n[0]*S0.z2**n[1]
                        Q[a, b] += q
                        if a != b:
                            Q[b, a] += q
    u, v, th = S0.u, S0.v, S0.th
    out = []
    for mk, (pu, pv, pth) in SAMPLES:
        rep = mk(S0, u, v, th)
        pt = {u: pu, v: pv, th: pth}
        sub = lambda M: M.applyfunc(lambda e: e.subs(rep).doit())     # noqa: E731
        Qp = Q.applyfunc(lambda e: sp.expand(sp.N(e.subs(rep).doit().subs(pt), 30)))
        res = theta_at_point(S0, sub(g0), sub(W), Qp, pt)
        hm = {n: abs(complex(cf)) for n, cf in S0.harmonics(res[1]).items()}
        mixed = max([x for n, x in hm.items() if n[0] and n[1]] + [0.0])
        pure2 = max([x for n, x in hm.items() if n[0] == 0 and n[1]] + [0.0])
        pure1 = max([x for n, x in hm.items() if n[0] and n[1] == 0] + [0.0])
        lm1 = max([abs(complex(c)) for c in S0.harmonics(res[-1]).values()] + [0.0]) if res[-1] != 0 else 0.0
        l0 = max([x for n, x in ((n, abs(complex(c))) for n, c in S0.harmonics(res[0]).items()) if n != (0, 0)]
                 + [0.0]) if res[0] != 0 else 0.0
        out.append((mixed, pure2, pure1, lm1, l0))
    return out


def main():
    t0 = time.time()
    ok = {}
    r = h1()
    Rs = sp.Symbol("R", real=True)
    good1 = (len(r["roots"]) == 1 and r["zero_at"] and zero(sp.simplify(r["d_at"]*Rs**2 - 3*r["pos"]))
             and r["pos"].func == sp.exp)                                 # c = e^psi > 0 at R^2 = mu
    print("  H1: one outgoing null covector dR + alpha dvhat, alpha = %s;\n"
          "      theta+ = c 3 f/(2R) with c = %s;\n"
          "      zero at R^2 = mu: %s; there d_R theta+ = %s = 3 c/mu with c = %s;\n"
          "      ingoing (k = dvhat, n(tau) = %s): theta- = %s: %s"
          % (r["roots"], r["ratio"], r["zero_at"], r["d_at"], r["pos"], r["dtau_in"], r["theta_in"], good1), flush=True)
    print("  H1 control (the ingoing normal): its expansion vanishes at R^2 = mu: %s (it must not)" % r["ctl"],
          flush=True)
    ok["H1"] = good1 and not r["ctl"]
    nolm1, l0 = h2()
    cn, cl0 = h2(control=True)
    print("  H2: g0's expansion along g0^-1 du is -3 e^(-2 sig) R_v/R: %s; both families: no lam^-1 term in either\n"
          "      expansion: %s; lam^0 term equal to g0's: out %s, in %s  [%.0f s]"
          % (l0["bg"], nolm1, l0["out"], l0["in"], time.time() - t0), flush=True)
    print("  H2 control (the outgoing wave with a trace on the spheres): lam^0 equal to g0's: out %s, in %s (the in\n"
          "      expansion must fail)  [%.0f s]" % (cl0["out"], cl0["in"], time.time() - t0), flush=True)
    ok["H2"] = nolm1 and l0["out"] and l0["in"] and l0["bg"] and cl0["out"] and not cl0["in"]
    r3 = h3()
    for (mixed, pure2, pure1, lm1, l0), k_ in zip(r3, range(1, 4)):
        print("  H3 point %d: lam^-1 term %.1e; lam^0 oscillation %.1e; lam^1 harmonics depending on s2: mixed %.1e,\n"
              "      pure (0, n2) %.1e; (those in s1 alone, for comparison: %.3e)  [%.0f s]"
              % (k_, lm1, l0, mixed, pure2, pure1, time.time() - t0), flush=True)
    good3 = all(m < 1e-20 and p < 1e-20 and a < 1e-20 and b < 1e-20 and q > 1e-6 for m, p, q, a, b in r3)
    r3c = h3(control=True)
    print("  H3 control (ghat_2 dropped): lam^1 mixed harmonics %s (must be nonzero)  [%.0f s]"
          % (" ".join("%.3e" % x[0] for x in r3c), time.time() - t0), flush=True)
    ok["H3"] = good3 and all(x[0] > 1e-6 for x in r3c)
    for k_, v_ in ok.items():
        print(k_, "PASS" if v_ else "FAIL")
    return 0 if all(ok.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
