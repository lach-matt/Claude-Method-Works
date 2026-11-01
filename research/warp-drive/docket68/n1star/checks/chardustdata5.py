#!/usr/bin/env python3
"""chardustdata5: the null dusts' own characteristic data on N (FAMILIES5 4e, D470).

D463 put the dusts' stress into the characteristic constraints with the dusts' data on N "given along with g's". Here
is what those data are. Each dust obeys div T = 0 with T = rho k (x) k, k null; the rescaling k -> f k, rho -> rho/f^2
leaves T unchanged. At a point of N = {u = 0} with g_vv = g_vA = 0 (so d_v is null and normal to N), everything is a
first-order jet: the values of g, rho, k and their first derivatives, with the tangential derivatives (d_v, d_A) of
the components that vanish on N set to zero. Exact in sympy, spacetime dimension 4 and 5:

  T1 (exact) a dust tangent to N is along the generators: nullity on N gives g_AB k^A k^B = 0, so k^A = 0, and k^u = 0
     by tangency. Then (div T)^u and (div T)^A vanish identically on N: the generators are geodesics, and nothing
     constrains the dust beyond one component.
  T2 (exact) the remaining component is a transport along the generators for q = rho (k^v)^2 (T_uu = (g_uv)^2 q on N):
     (div T)^v = d_v q + c q, with d_u k^u eliminated by the u-derivative of nullity, and c = (2 d_v g_uv - d_u
     g_vv)/g_uv + (1/2) gamma^(AB) d_v g_AB, free of the dust's fields: the generators' non-affinity and their expansion.
     The only transverse jet of g in c is d_u g_vv. So q on N is fixed by its value on S.
  T3 (exact) the gauge fixes that jet: W_v = g_va g^(bc) Gamma^a_bc on N is affine in the transverse jets of g with d_u
     g_vv the only one present, its coefficient 1/g_uv, so W_v = H_v (H carrying no derivative of g) fixes d_u g_vv on N
     from N's data, and c is data. Indeed c = 2 d_v ln|g_uv| - W_v exactly, so the expansion cancels and the transport is
     d_v T_uu = W_v T_uu = H_v T_uu (verifier 201, D471).
  T4 (exact) a dust crossing N (k^u != 0; k^v fixed by nullity, its tangential derivatives by nullity's): the D + 1
     equations div T = 0 and d_u(g(k, k)) = 0 for the D + 1 transverse derivatives (d_u rho, d_u k^a) have exactly one
     dependency, k_a (div T)^a - (rho/2) k^u d_u(g(k, k)) = 0 identically, and exactly one kernel vector, the rescaling
     (-2 rho, k); their rank is D (at three random rational points; everywhere with rho, k^u != 0, a D x D block having
     determinant 2 rho^D (k^u)^D, verifier 201). So the transverse derivatives of T are fixed, and rho, k^u and k^A on N
     are free data.
  T5 controls: for the tangent dust the transverse rank is 1, not D (its data are constrained, by T2, not free); without
     the Gamma^a_bc k^b k^c term of div T the identity of T4 fails (dropping the Gamma^b_bd term would not do: it lies
     along k^a and drops out of k_a (div T)^a on N); and W_u, unlike W_v, contains transverse jets other than d_u g_vv,
     so T3's test is not vacuous (verifier 201).

So the characteristic data of the two dusts: a crossing dust has D - 1 free functions on N (rho, k^u, k^A up to the
rescaling) and enters N's constraint hierarchy through T_vv (D463); the dust along N's generators is fixed on N by its
value on S, through T2's transport, d_v T_uu = H_v T_uu once W_v = H_v; it does not enter N's constraints. With the
record's dusts, the covectors sqrt(K_in) dv and sqrt(K_out) du (FAMILIES5 4b-4c), on N = {u = const} the du dust is the
tangent one, so K_out on N is transported from S (the transport reproduces section 4c's K_out R^3 = B(u), verifier 201),
and the dv dust, its direction fixed, has K_in alone on N, free where dv is null there (g^vv = 0; in general that needs
g_uu = gamma^(AB) g_uA g_uB); on N' = {v = const} the roles swap, by symmetry (not computed). Not computed: existence for
the coupled transport off N (a first-order hyperbolic system along k), and the corner S, where both dusts' data meet.

Run: python3 checks/chardustdata5.py   (exact; under a minute)
"""
import random
import sys

import sympy as sp


def setup(D):
    U, V = 0, 1
    S = list(range(2, D))
    g = sp.zeros(D, D)
    gs = {}
    for a in range(D):
        for b in range(a, D):
            if (a, b) == (V, V) or (a == V and b in S):
                continue
            gs[(a, b)] = sp.Symbol("g%d%d" % (a, b))
            g[a, b] = g[b, a] = gs[(a, b)]
    dg = {}
    for c in range(D):
        M = sp.zeros(D, D)
        for a in range(D):
            for b in range(a, D):
                vanish_on_N = (a, b) == (V, V) or (a == V and b in S)
                if vanish_on_N and c != U:
                    continue                                   # tangential derivative of a component zero on N
                s = sp.Symbol("dg%d_%d%d" % (c, a, b))
                M[a, b] = M[b, a] = s
        dg[c] = M
    gI = g.inv()
    Gam = [[[sp.Rational(1, 2) * sum(gI[a, d] * (dg[b][d, c] + dg[c][d, b] - dg[d][b, c]) for d in range(D))
             for c in range(D)] for b in range(D)] for a in range(D)]
    return U, V, S, g, gs, dg, gI, Gam


def dust(D, tangent):
    U, V = 0, 1
    S = list(range(2, D))
    rho = sp.Symbol("rho", positive=True)
    k = [sp.Symbol("k%d" % a) for a in range(D)]
    dk = [[sp.Symbol("dk%d_%d" % (c, a)) for a in range(D)] for c in range(D)]
    drho = [sp.Symbol("drho%d" % c) for c in range(D)]
    if tangent:
        k = [sp.Integer(0) if a != V else k[a] for a in range(D)]
        for c in range(D):
            if c != U:
                for a in [U] + S:
                    dk[c][a] = sp.Integer(0)                    # tangential derivatives of k^u, k^A, zero on N
    return rho, k, dk, drho


def divT(D, Gam, rho, k, dk, drho, geodesic_term=True):
    out = []
    for a in range(D):
        e = sum(drho[b] * k[a] * k[b] + rho * dk[b][a] * k[b] + rho * k[a] * dk[b][b] for b in range(D))
        if geodesic_term:
            e += sum(Gam[a][b][c] * rho * k[b] * k[c] for b in range(D) for c in range(D))
        e += sum(Gam[b][b][d] * rho * k[a] * k[d] for b in range(D) for d in range(D))
        out.append(e)
    return out


def nullder(D, g, dg, k, dk, c):
    return (sum(dg[c][a, b] * k[a] * k[b] for a in range(D) for b in range(D))
            + 2 * sum(g[a, b] * k[a] * dk[c][b] for a in range(D) for b in range(D)))


def transverse_jets(dg, U):
    return {x for x in dg[U] if isinstance(x, sp.Symbol)}


def run(D, seeds=(1, 2, 3)):
    U, V, S, g, gs, dg, gI, Gam = setup(D)
    out = {}
    # tangent dust
    rho, k, dk, drho = dust(D, True)
    Nu = nullder(D, g, dg, k, dk, U)
    sol = sp.solve(Nu, dk[U][U])[0]
    dT = [sp.together(sp.expand(e.subs(dk[U][U], sol))) for e in divT(D, Gam, rho, k, dk, drho)]
    out["T1"] = all(sp.simplify(dT[a]) == 0 for a in [U] + S)
    kv = k[V]
    dq = drho[V] * kv**2 + 2 * rho * kv * dk[V][V]
    c = sp.simplify((dT[V] - dq) / (rho * kv**2))
    dust_syms = {rho, kv, drho[V], dk[V][V]} | set(drho) | {x for row in dk for x in row if isinstance(x, sp.Symbol)}
    trans = transverse_jets(dg, U)
    gam = g[2:, 2:].inv()
    c_closed = ((2 * dg[V][U, V] - dg[U][V, V]) / g[U, V]
                + sp.Rational(1, 2) * sum(gam[i, j] * dg[V][S[i], S[j]] for i in range(D - 2) for j in range(D - 2)))
    out["T2"] = (not (c.free_symbols & dust_syms) and (c.free_symbols & trans) == {dg[U][V, V]}
                 and sp.simplify(c - c_closed) == 0)
    # gauge: W_v on N
    Wv = sp.expand(sum(g[V, a] * sum(gI[b, cc] * Gam[a][b][cc] for b in range(D) for cc in range(D))
                       for a in range(D)))
    Wt = Wv.free_symbols & trans
    coef = sp.simplify(sp.diff(Wv, dg[U][V, V]))
    after = sp.simplify(c - (2 * dg[V][U, V] / g[U, V] - Wv)) == 0          # c = 2 d_v ln|g_uv| - W_v
    out["T3"] = Wt == {dg[U][V, V]} and coef != 0 and sp.diff(Wv, dg[U][V, V], 2) == 0 and after
    # crossing dust
    rho, k, dk, drho = dust(D, False)
    null = sp.expand(sum(g[a, b] * k[a] * k[b] for a in range(D) for b in range(D)))
    kv_sol = sp.solve(null, k[V])[0]
    subs = {}
    for cc in [V] + S:
        Nc = nullder(D, g, dg, k, dk, cc)
        subs[dk[cc][V]] = sp.solve(Nc, dk[cc][V])[0]
    eqs = divT(D, Gam, rho, k, dk, drho) + [nullder(D, g, dg, k, dk, U)]
    eqs = [e.subs(subs) for e in eqs]
    X = [drho[U]] + [dk[U][a] for a in range(D)]
    M = sp.Matrix([[sp.diff(e, x) for x in X] for e in eqs])
    v0 = sp.Matrix([-2 * rho] + k)
    kernel_ok = all(sp.simplify((M * v0)[i].subs(k[V], kv_sol)) == 0 for i in range(D + 1))
    klow = [sum(g[a, b] * k[b] for b in range(D)) for a in range(D)]
    ident = sum(klow[a] * eqs[a] for a in range(D)) - rho / 2 * k[U] * eqs[D]
    ident_ok = sp.simplify(sp.together(ident.subs(k[V], kv_sol))) == 0
    ranks = []
    syms = sorted((M.free_symbols | v0.free_symbols) - {k[V]}, key=str)
    for sd in seeds:
        rnd = random.Random(sd)
        val = {s: sp.Rational(rnd.randint(-9, 9), rnd.randint(1, 5)) or sp.Integer(1) for s in syms}
        val[rho] = sp.Rational(rnd.randint(1, 9), rnd.randint(1, 5))
        for A in S:                                                 # gamma positive definite: diagonal dominance
            val[gs[(A, A)]] = sp.Integer(30)
        val[gs[(U, V)]] = sp.Integer(-2)
        kvv = kv_sol.subs(val)
        val[k[V]] = kvv
        ranks.append(M.subs(val).rank())
    out["T4"] = kernel_ok and ident_ok and all(r == D for r in ranks)
    # controls
    rho_t, k_t, dk_t, drho_t = dust(D, True)
    eqs_t = divT(D, Gam, rho_t, k_t, dk_t, drho_t) + [nullder(D, g, dg, k_t, dk_t, U)]
    Xt = [drho_t[U]] + [dk_t[U][a] for a in range(D)]
    Mt = sp.Matrix([[sp.diff(e, x) for x in Xt] for e in eqs_t])
    rank_t = sp.Matrix(Mt).rank(simplify=True)
    eqs_n = [e.subs(subs) for e in divT(D, Gam, rho, k, dk, drho, geodesic_term=False)]
    ident_n = sum(klow[a] * eqs_n[a] for a in range(D)) - rho / 2 * k[U] * eqs[D]
    broken = sp.simplify(sp.together(ident_n.subs(k[V], kv_sol))) != 0
    Wu = sp.expand(sum(g[U, a] * sum(gI[b, cc] * Gam[a][b][cc] for b in range(D) for cc in range(D))
                       for a in range(D)))
    out["T5"] = rank_t == 1 and broken and bool((Wu.free_symbols & trans) - {dg[U][V, V]})
    info = dict(c=c, coef=coef, ranks=ranks, rank_t=rank_t)
    return out, info


def main():
    ok = {}
    for D in (4, 5):
        out, info = run(D)
        print("  D = %d: %s" % (D, ", ".join("%s %s" % (kk, "ok" if v else "FAIL") for kk, v in out.items())),
              flush=True)
        print("    tangent dust: (div T)^v = d_v q + c q, c = %s" % info["c"])
        print("    W_v's coefficient of d_u g_vv: %s; crossing ranks %s (of %d), tangent rank %s"
              % (info["coef"], info["ranks"], D + 1, info["rank_t"]), flush=True)
        for kk, v in out.items():
            ok[kk] = ok.get(kk, True) and v
    for kk, v in ok.items():
        print(kk, "PASS" if v else "FAIL")
    return 0 if all(ok.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
