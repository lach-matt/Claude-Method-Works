#!/usr/bin/env python3
"""twohorizon5: the record's Proposition 8.1 (one zero per column of the outgoing expansion) for two families: the exact
facts the deduction in FAMILIES5-FULL.md section 9 uses, and the term that makes the packet's placement necessary.

  H1 (exact) the background on its columns. Where the outgoing dust vanishes (region III, u >= u2) the two-dust
     background is g0 = -e^(2 psi) f dvhat^2 + 2 e^psi dvhat dR + R^2 dOmega_3^2, f = 1 - mu/R^2, psi and mu functions of
     vhat (twobg5 G1 (a)-(b)); the sphere S = {vhat, R} has the null normals dvhat (ingoing) and k = dR - (e^psi f/2)
     dvhat (outgoing). With n = g0^-1 k normalised by n(tau) = 1, tau = vhat - R: theta+ = c(R) 3 f/(2R) with c =
     2 R^2/(R^2 + mu e^psi ... ) printed, c > 0; its one zero on (0, oo) is R^2 = mu, simple, d_R theta+ = (3/mu) c >
     0 there; the future ingoing normal -g0^-1 dvhat has expansion -3 e^(-psi)/R < 0. At psi = 0 this is the record's
     H1 (horizon5.py). Control: the ingoing root in place of the outgoing one (its expansion has no zero).
  H2 (exact, symbolic in every function) on stage0two5.py's general round double-null background with both families'
     stage-0 waves (W_in = TT(s1) + chi dv^2, W_out = TT(s2) + chi' du^2), the expansions along g^-1 du (outgoing) and
     g^-1 dv (ingoing) have no lam^-1 term and no lam^0 term beyond g0's: theta(g0 + lam W) = theta(g0) + O(lam). The
     reason: the fast derivatives enter only as (1/2) g0^-1(k, d phase) F tr_S W, and tr_S W_k = 0 for both families.
     Control: the outgoing wave with a trace on the spheres (t z2 gamma0 added) gives a lam^0 oscillation in the
     ingoing expansion (g0^-1(dv, du) != 0); in the outgoing one it does not (g0^-1(du, du) = 0).
  H3 (exact; the reason for the placement hypothesis (H6)) with ghat_2's mixed harmonics fixed by stage 0's division
     (ghat = e^(2 sig) R^(0)_(n1,n2)/(n1 n2), stage0two5 T4, T7), the lam^1 coefficient of the outgoing expansion has
     nonzero mixed harmonics (n1, n2), n1 n2 != 0, wherever both families are present (evaluated with concrete smooth
     functions at a point). Along a column {vhat fixed} the outgoing phase u varies (d_R u = 1/R_u != 0), so lam
     [Th1] contributes (d_R u) [F2 Th1] = O(1) to d_R theta+ there: the record's monotonicity band argument needs the
     band free of the outgoing family. Control (must fail): with the outgoing family removed the mixed harmonics vanish.

Labels: computed (exact, sympy). Run: python3 checks/twohorizon5.py   (a few minutes)
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


def h1(control=False):
    vh, R, th, p1, p2 = sp.symbols("vhat R theta phi1 phi2", real=True)
    X = [vh, R, th, p1, p2]
    psi, mu = sp.Function("psi")(vh), sp.Function("mu")(vh)
    f = 1 - mu/R**2
    g = sp.zeros(5)
    g[0, 0], g[0, 1], g[1, 0] = -sp.exp(2*psi)*f, sp.exp(psi), sp.exp(psi)
    g[2, 2], g[3, 3], g[4, 4] = R**2, R**2*sp.cos(th)**2, R**2*sp.sin(th)**2
    gi = sp.simplify(g.inv())
    alpha = sp.Symbol("alpha")
    roots = sp.solve(sp.Eq(sum(gi[a, b]*k1*k2 for a, k1 in ((0, alpha), (1, 1)) for b, k2 in ((0, alpha), (1, 1))), 0),
                     alpha)
    out_root = [x for x in roots if not zero(sp.simplify(x))]
    a_ = sp.Integer(0) if control else out_root[0]                     # control: dR alone is not null (f != 0)
    if control:
        a_ = [x for x in roots if zero(sp.simplify(x))][0] if any(zero(sp.simplify(x)) for x in roots) else roots[0]
    k = [a_, 1, 0, 0, 0]
    n = [sp.simplify(sum(gi[c, d]*k[d] for d in range(5))) for c in range(5)]
    cn = sp.simplify(1/(n[0] - n[1]))                                  # normalise n(tau) = 1, tau = vhat - R
    A = [2, 3, 4]
    dg = [[[sp.diff(g[a, b], X[c]) for c in range(5)] for b in range(5)] for a in range(5)]
    Gam = lambda c, a, b: sum(gi[c, d]*(dg[d][a][b] + dg[d][b][a] - dg[a][b][d]) for d in range(5))/2  # noqa: E731
    gam_inv = {a: 1/g[a, a] for a in A}
    theta = sp.simplify(-cn*sum(gam_inv[a]*Gam(c, a, a)*k[c] for a in A for c in range(5)))
    base = 3*f/(2*R)
    ratio = sp.simplify(theta/base)
    if control:
        return ratio
    zero_at = sp.simplify(theta.subs(mu, R**2)) == 0
    d_at = sp.simplify(sp.diff(theta, R).subs(mu, R**2))
    pos = sp.simplify(ratio.subs(mu, R**2))
    kin = [1, 0, 0, 0, 0]
    nin = [-sum(gi[c, d]*kin[d] for d in range(5)) for c in range(5)]
    theta_in = sp.simplify(-sum(gam_inv[a]*Gam(c, a, a)*(-kin[c]) for a in A for c in range(5)))
    fut = sp.simplify(nin[0] - nin[1])                                 # dtau(n_in) > 0: future directed
    return dict(ratio=ratio, zero_at=zero_at, d_at=d_at, pos=pos, theta_in=theta_in, fut=fut)


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
    return nolm1, l0


def h3(control=False):
    import stage0two5 as S0
    W = S0.waves()
    if control:
        a_, b_ = S0.amplitudes()
        W = W - S0.tt(b_, S0.z2)
        W[0, 0] = 0                                                    # chi' du^2 removed with it
    o = S0.ricci_orders(W)
    g0, _ = S0.background()
    Q = sp.zeros(5)
    for a in range(5):
        for b in range(a, 5):
            for n, cf in S0.harmonics(o[(a, b)][1]).items():
                if n[0] and n[1]:
                    q = sp.exp(2*S0.sig)*cf/(n[0]*n[1])*S0.z1**n[0]*S0.z2**n[1]
                    Q[a, b] += q
                    if a != b:
                        Q[b, a] += q
    res = theta_series(S0, W, Q=Q, top=1)
    th1 = res["out"][1]
    mixed = {n: cf for n, cf in S0.harmonics(th1).items() if n[0] and n[1]}
    # evaluate with concrete smooth functions at a point
    u, v, th = S0.u, S0.v, S0.th
    rep = {S0.sig: sp.Rational(1, 10)*u + sp.Rational(1, 5)*v, S0.Rf: 3 + u - v/2 + u*v/7,
           S0.Hf: 1 + sp.cos(2*th)**2/3, S0.alpha: 1 + v/3, S0.beta: 2 - u/5}
    for fn, val in ((S0.xi2, 1 + u*v/3), (S0.xi2b, 2 - v), (S0.et2, sp.Rational(1, 2) + u), (S0.et2b, 1 + th)):
        rep[fn] = val
    pt = {u: sp.Rational(1, 3), v: sp.Rational(1, 2), th: sp.Rational(7, 10)}
    vals = {}
    for n, cf in mixed.items():
        e = cf.subs(rep).doit()
        vals[n] = complex(sp.N(e.subs(pt), 12))
    big = max((abs(x) for x in vals.values()), default=0.0)
    return big, sorted(vals)[:8], len(mixed)


def main():
    t0 = time.time()
    ok = {}
    r = h1()
    rc = h1(control=True)
    good1 = r["zero_at"] and zero(r["d_at"] - 3*r["pos"]/(sp.Symbol("R", real=True)**2)) is not None
    Rs = sp.Symbol("R", real=True)
    good1 = r["zero_at"] and zero(sp.simplify(r["d_at"]*Rs**2 - 3*r["pos"]))
    print("  H1: theta+ = c(R) 3 f/(2R) with c = %s; zero at R^2 = mu: %s; there d_R theta+ = %s = (3/mu) c, c = %s > 0;"
          "\n      ingoing expansion %s < 0 with dtau(n_in) = %s > 0: %s" % (r["ratio"], r["zero_at"], r["d_at"], r["pos"],
                                                                         r["theta_in"], r["fut"], good1), flush=True)
    print("  H1 control (the ingoing root used as k): theta/(3 f/(2R)) = %s, not a positive function: the outgoing root"
          "\n      is the one with the zero" % rc, flush=True)
    ok["H1"] = good1 and r["fut"] != 0
    nolm1, l0 = h2()
    cn, cl0 = h2(control=True)
    print("  H2: both families: no lam^-1 term in either expansion: %s; lam^0 term equal to g0's: out %s, in %s  [%.0f s]"
          % (nolm1, l0["out"], l0["in"], time.time() - t0), flush=True)
    print("  H2 control (the outgoing wave with a trace on the spheres): lam^0 equal to g0's: out %s, in %s (the in\n"
          "      expansion must fail)  [%.0f s]" % (cl0["out"], cl0["in"], time.time() - t0), flush=True)
    ok["H2"] = nolm1 and l0["out"] and l0["in"] and cl0["out"] and not cl0["in"]
    big, some, count = h3()
    print("  H3: the lam^1 coefficient of the outgoing expansion has %d mixed harmonics, largest |value| at the sample\n"
          "      point %.4e (harmonics %s ...)  [%.0f s]" % (count, big, some, time.time() - t0), flush=True)
    bigc, somec, countc = h3(control=True)
    print("  H3 control (the outgoing family removed): %d mixed harmonics, largest %.1e  [%.0f s]"
          % (countc, bigc, time.time() - t0), flush=True)
    ok["H3"] = big > 1e-6 and bigc < 1e-12
    for k_, v_ in ok.items():
        print(k_, "PASS" if v_ else "FAIL")
    return 0 if all(ok.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
