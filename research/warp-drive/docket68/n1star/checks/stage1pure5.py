"""stage1pure5.py -- FAMILIES5 section 4b (D407): the linear core of D401, computed. At a pure harmonic (n, 0), the
order-lam part of Ric^H(g0 + lam^2 Q) that is linear in Q, on a general round double-null background (no field
equation for g0: Ric(g0) enters only at order lam^2 here).

With Q = G(u, v, th) z1^n, d_v -> d_v + lam^-1 F1 (F1 = i n on this harmonic), the order-lam coefficient is

    R1[Q]_bc = sum_a (F_a G2^a_bc - F_c G2^a_ba) + sum_a (d_a G1^a_bc - d_c G1^a_ba) + (G0 G1 + G1 G0 terms)
               - (1/2) sum_(p,q) g0_pr (d_q D1^r + Gam0^r_qs D1^s + F_q D2^r),

with G1 = (1/2) g0^-1 (F Q), G2 = (1/2) g0^-1 (dQ) - g0^-1 Q Gam0, D1 = g0^ab G1_ab and D2 = g0^ab G2_ab (stage0two5's
ricci_orders at this order; the gauge term is -(1/2)(g_pr nabla0_q D^r + g_qr nabla0_p D^r)).

  P1 (exact) with G's five reachable components zero (G_uu, G_uA and the angular trace g0^AB G_AB, those T8 fixes)
     and the ten others arbitrary functions, R1 vanishes at (n, 0) in uu, u theta, u phi1, u phi2 and in the angular
     trace g0^AB R1_AB: the free components do not enter the five equations D401 says hold identically.
  P2 (exact) each of the ten other components of R1 (vv, uv, v A, the angular trace-free part) contains the transport
     d_u of its own free component, with coefficient -i n g0^uv (times the component's own weight), so the ten are
     transports along d_u for the ten free components.
  Control: with G_uu, or the angular trace, nonzero, the corresponding one of the five components does not vanish.
n = 1 and 2. Labels: computed (exact, sympy).

    python3 checks/stage1pure5.py [--selftest]
"""
import os
import sys

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import stage0two5 as S0   # noqa: E402

u, v, th, z1 = S0.u, S0.v, S0.th, S0.z1
N, Rf, C, Sn = S0.N, S0.Rf, S0.C, S0.S
ex, fast, slow, gamma_of = S0.ex, S0.fast, S0.slow, S0.gamma_of


def r1(Q):
    g0, g0i = S0.background()
    dg0 = [[[slow(g0[d, b], c) for c in range(N)] for b in range(N)] for d in range(N)]
    Gh = gamma_of(g0i, dg0)
    A1 = [[[fast(Q[d, b], c) for c in range(N)] for b in range(N)] for d in range(N)]
    A2 = [[[slow(Q[d, b], c) for c in range(N)] for b in range(N)] for d in range(N)]
    G1 = gamma_of(g0i, A1)
    G2a = gamma_of(g0i, A2)
    Qu = (g0i*Q).applyfunc(ex)
    G2 = [[[ex(G2a[a][b][c] - sum(Qu[a, f]*Gh[f][b][c] for f in range(N))) for c in range(N)] for b in range(N)]
          for a in range(N)]
    D1 = [ex(sum(g0i[a, b]*G1[r][a][b] for a in range(N) for b in range(N))) for r in range(N)]
    D2 = [ex(sum(g0i[a, b]*G2[r][a][b] for a in range(N) for b in range(N))) for r in range(N)]
    out = {}
    for b in range(N):
        for c in range(b, N):
            e = sum(fast(G2[a][b][c], a) - fast(G2[a][b][a], c) for a in range(N))
            e += sum(slow(G1[a][b][c], a) - slow(G1[a][b][a], c) for a in range(N))
            e += sum(Gh[a][a][d]*G1[d][b][c] + G1[a][a][d]*Gh[d][b][c] - Gh[a][c][d]*G1[d][b][a]
                     - G1[a][c][d]*Gh[d][b][a] for a in range(N) for d in range(N))
            for (p, q) in ((b, c), (c, b)):
                e -= sum(g0[p, r]*(slow(D1[r], q) + fast(D2[r], q) + sum(Gh[r][q][s]*D1[s] for s in range(N)))
                         for r in range(N))/2
            out[(b, c)] = ex(e)
    return out


def harm(e, n):
    return sp.expand(S0.harmonics(e).get((n, 0), 0))


def build(n, reach=None):
    """Q = G z1^n; reach = None (reachable components zero), 'uu' or 'tr' (that one nonzero, the rest as None)"""
    f = {k: sp.Function("q" + k)(u, v, th) for k in ("vv", "uv", "vt", "v1", "v2", "t1", "t2", "12", "a", "b", "uu",
                                                     "tr")}
    G = sp.zeros(N)
    G[1, 1] = f["vv"]
    G[0, 1] = G[1, 0] = f["uv"]
    for A, k in ((2, "vt"), (3, "v1"), (4, "v2")):
        G[1, A] = G[A, 1] = f[k]
    G[2, 3] = G[3, 2] = f["t1"]
    G[2, 4] = G[4, 2] = f["t2"]
    G[3, 4] = G[4, 3] = f["12"]
    tr = f["tr"] if reach == "tr" else 0
    G[2, 2] = Rf**2*(-(f["a"] + f["b"]) + tr)        # g0^AB G_AB = tr: the trace-free part is free
    G[3, 3] = Rf**2*C**2*f["a"]
    G[4, 4] = Rf**2*Sn**2*f["b"]
    if reach == "uu":
        G[0, 0] = f["uu"]
    return (G*z1**n).applyfunc(sp.expand), f


def main():
    ok = {"P1": True, "P2": True, "control": True}
    g0, g0i = S0.background()
    for n in (1, 2):
        Q, f = build(n)
        R = {k: harm(e, n) for k, e in r1(Q).items()}
        five = [R[(0, 0)], R[(0, 2)], R[(0, 3)], R[(0, 4)], sp.expand(sum(g0i[A, A]*R[(A, A)] for A in (2, 3, 4)))]
        p1 = all(sp.simplify(e) == 0 for e in five)
        ok["P1"] &= p1
        # P2: each remaining component contains d_u of its own free function
        own = {(1, 1): "vv", (0, 1): "uv", (1, 2): "vt", (1, 3): "v1", (1, 4): "v2", (2, 3): "t1", (2, 4): "t2",
               (3, 4): "12", (3, 3): "a", (4, 4): "b"}
        weight = {"a": Rf**2*C**2, "b": Rf**2*Sn**2}
        p2 = True
        for k, name in own.items():
            cf = sp.simplify(R[k].coeff(sp.Derivative(f[name], u)))
            p2 &= sp.simplify(cf - (-sp.I*n*g0i[0, 1]*weight.get(name, 1))) == 0
        ok["P2"] &= p2
        for reach, idx in (("uu", 0), ("tr", 4)):
            Qc, _ = build(n, reach)
            Rc = {k: harm(e, n) for k, e in r1(Qc).items()}
            fivec = [Rc[(0, 0)], Rc[(0, 2)], Rc[(0, 3)], Rc[(0, 4)],
                     sp.expand(sum(g0i[A, A]*Rc[(A, A)] for A in (2, 3, 4)))]
            ok["control"] &= sp.simplify(fivec[idx]) != 0
        print("  n = %d: the five components with the reachable part zero vanish: %s; the ten contain their own d_u: %s"
              % (n, p1, p2), flush=True)
    for k, val in ok.items():
        print(k, "PASS" if val else "FAIL")
    if "--selftest" in sys.argv:
        sys.exit(0 if all(ok.values()) else 1)


if __name__ == "__main__":
    main()
