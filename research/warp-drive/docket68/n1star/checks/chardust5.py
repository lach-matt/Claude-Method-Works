#!/usr/bin/env python3
"""chardust5: the null dusts' stress in the characteristic constraints (FAMILIES5 4e, D463).

D440-D455 treat the characteristic problem for the reduced vacuum equation. The class carries two null dusts (D389),
T = sum_i rho_i k_i (x) k_i with k_i null for g, so the reduced equation is E := Ric(g) - dstar W - kap S with
S = T - (tr_g T) g/(n - 2), and tr_g T = sum_i rho_i g(k_i, k_i) = 0, so S = T. T is algebraic in g (k_i lowered with g)
and in the dusts' data (rho_i and the components k_i^u, k_i^A on N, k_i^v then fixed by nullity). It contains no
derivative of g, so no transverse jet: charprop5's N2-N4 hold with C_vv, C_vA and C_tr shifted by -kap T_vv, -kap T_vA
and -kap gamma^(AB) T_AB, which are data in the sense of N1-N4. The propagation of W off N (charprop5's P2) uses the
contracted Bianchi identity and div T = 0, which the dusts' own equations give.

What needs checking is that charcons5's hierarchy (K1-K4) still closes: the shifts must not bring the later unknowns
into the earlier equations. Here at a point of N (g_vv = g_vA = 0), exactly in sympy with g_uu, g_uv, g_uA, g_AB, rho_i,
k_i^u and k_i^A symbols, n = 4 and 5:

  D1 g(k, k) = 0 fixes k^v = -(g_uu (k^u)^2 + 2 g_uA k^u k^A + g_AB k^A k^B)/(2 g_uv k^u) (k^u != 0: the dust
     crossing N);
     tr_g T = 0 then holds identically, so S = T.
  D2 T_vv = sum_i rho_i (g_uv k_i^u)^2: free of g_uu, g_uA and gamma, so Raychaudhuri's equation for the conformal
     factor (K1) gains a source fixed by the data.
  D3 T_vA is free of g_uu and of every derivative, and linear in g_uA (through (k_i)_A = g_Au k^u + g_AB k^B): K2's
     equation for g_uA stays linear, its source data once the conformal factor is known.
  D4 gamma^(AB) T_AB is free of g_uu: K3's equation for g_uu keeps g_uu only in its derivative terms.
  D5 controls: without nullity (k^v free) tr_g T != 0, and the components that do carry g_uu (T_uu, T_uA) are the ones
     the hierarchy never uses on N.

A dust moving along N's generators (k = k^v d_v) has k_v = g_vv k^v = 0 on N, so it drops out of all three; only the
dust crossing N enters. Not computed: the dusts' own characteristic data and transport (they are given along with g's).

Run: python3 checks/chardust5.py   (exact; seconds)
"""
import sys

import sympy as sp


def run(n):
    U, V = 0, 1
    S = list(range(2, n))
    guu, guv = sp.symbols("g_uu g_uv")
    guA = sp.symbols("g_u2:%d" % n)
    gAB = {}
    for A in S:
        for B in S:
            if A <= B:
                gAB[(A, B)] = sp.Symbol("g_%d%d" % (A, B))
    g = sp.zeros(n, n)
    g[U, U] = guu
    g[U, V] = g[V, U] = guv
    for i, A in enumerate(S):
        g[U, A] = g[A, U] = guA[i]
        for B in S:
            g[A, B] = gAB[(min(A, B), max(A, B))]
    gam = g[2:, 2:]
    gamI = gam.inv()
    dusts = []
    for d in range(2):
        rho = sp.Symbol("rho%d" % d, positive=True)
        ku = sp.Symbol("ku%d" % d)
        kA = [sp.Symbol("k%d_%d" % (d, A)) for A in S]
        kv = sp.Symbol("kv%d" % d)
        k = [ku, kv] + kA
        null = sp.expand(sum(g[a, b] * k[a] * k[b] for a in range(n) for b in range(n)))
        kv_sol = sp.solve(null, kv)[0]
        dusts.append((rho, k, kv, kv_sol))
    out = {}

    def lower(k):
        return [sum(g[a, b] * k[b] for b in range(n)) for a in range(n)]

    def stress(subs_null=True):
        T = sp.zeros(n, n)
        for rho, k, kv, kv_sol in dusts:
            kk = [sp.simplify(x.subs(kv, kv_sol)) if subs_null else x for x in k]
            kl = lower(kk)
            for a in range(n):
                for b in range(n):
                    T[a, b] += rho * kl[a] * kl[b]
        return T
    T = stress()
    gI = g.inv()
    trT = sp.simplify(sum(gI[a, b] * T[a, b] for a in range(n) for b in range(n)))
    out["D1"] = trT == 0
    Tvv = sp.expand(T[V, V])
    want = sp.expand(sum(rho * (guv * k[0])**2 for rho, k, _, _ in dusts))
    out["D2"] = sp.simplify(Tvv - want) == 0 and not (Tvv.free_symbols & ({guu} | set(guA) | set(gAB.values())))
    ok3 = True
    for A in S:
        e = sp.expand(T[V, A])
        ok3 &= guu not in e.free_symbols
        ok3 &= all(sp.degree(e, x) <= 1 for x in guA)
    out["D3"] = ok3
    trAB = sp.simplify(sum(gamI[i, j] * T[S[i], S[j]] for i in range(n - 2) for j in range(n - 2)))
    out["D4"] = guu not in trAB.free_symbols
    T0 = stress(subs_null=False)
    trT0 = sp.simplify(sum(gI[a, b] * T0[a, b] for a in range(n) for b in range(n)))
    carry = guu in sp.expand(T[U, U]).free_symbols or any(guu in sp.expand(T[U, A]).free_symbols for A in S)
    out["D5"] = trT0 != 0 and carry
    return out


def main():
    ok = {}
    for n in (4, 5):
        out = run(n)
        print("  n = %d: %s" % (n, ", ".join("%s %s" % (k, "ok" if v else "FAIL") for k, v in out.items())), flush=True)
        for k, v in out.items():
            ok[k] = ok.get(k, True) and v
    for k, v in ok.items():
        print(k, "PASS" if v else "FAIL")
    return 0 if all(ok.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
