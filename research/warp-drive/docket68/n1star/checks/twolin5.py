"""twolin5.py -- FAMILIES5 section 4d (D414): the large coefficients of the two-phase linearisation.

Section 1 (FAMILIES5) asks two things of the linearisation of Ric^H at g = g0 + lam (W_in + W_out): that it carry no
lam^-1 coefficient beyond one per family, and which contractions kill which. With stage0two5.py's ansatz (round
double-null g0, sigma and R free; W_in = TT wave in s1 + chi dv dv, W_out = TT wave in s2 + chi' du du; the fast
variables as z_k = exp(i s_k)), take the background slow perturbation w (fifteen constants: the lam^-1 part of Ric^H
involves only fast derivatives, so it is algebraic in w and contains no derivative of w), and compute

    E[w] := d/d eps at eps = 0 of the lam^-1 coefficient of Ric^H(g0 + eps w + lam (W_in + W_out)),

the lam^-1 coefficient of the linearised operator acting on w. ell_in := g0^-1 dv, ell_out := g0^-1 du,
s_in := w(ell_in, ell_in) = e^(-4 sigma) w_uu, s_out := w(ell_out, ell_out) = e^(-4 sigma) w_vv, F_k = d/ds_k.

  A  (exact) The assembly below (rm1) reproduces stage0two5.ricci_orders' lam^-1 coefficient at eps = 0, both for the
     waves (where it is 0, T1) and with terms q z1 z2, q z1/z2, q z1^2 z2 added (where it is not). A mutant of one
     family alone cannot serve: the coefficient is -(1/2) g0^-1(k_j, k_k) F_j F_k W, zero for any W_in(s1) + W_out(s2).
  L1 (exact) E[w] = (1/2)(s_in F_1^2 W_in + s_out F_2^2 W_out) in all 15 components, for every w: one coefficient per
     family, coupling s_k to its own family's wave, and no other. (It is the linearised coefficient of the principal
     part -(1/2) g^ab d_a d_b: the lam^-1 part of Ric^H is -(1/2) g^-1(k_j, k_k) F_j F_k (W), and F_1 F_2 W = 0.)
  L2 (exact) Contractions. E(ell_in, ell_in) = (1/2) s_out (F_2^2 chi')(du(ell_in))^2 = -2 e^(-4 sigma) s_out chi',
     and E(ell_out, ell_out) = -2 e^(-4 sigma) s_in chi: each family's own coupling is killed by its own ell_k x ell_k,
     the other family's survives through the second-harmonic gauge term alone. E(ell_in, ell_out) = 0.
  L3 (exact) With chi = chi' = 0 (section 1's generalised wave gauge), E[w] has no component with an index u or v:
     every contraction with vectors of the (u, v) plane vanishes, ell_j x ell_k included.
  Control: without the gauge term (plain Ric), E differs from L1 by
     (1/2) sum_k (-k_b (P_k w k)_c - k_c (P_k w k)_b + k_b k_c <w, P_k>), P_k = F_k^2 W_k, k_in = dv, k_out = du,
     indices raised by g0, and that difference is nonzero: the one-coefficient structure is the wave gauge's.
Labels: computed (exact, sympy).

    python3 checks/twolin5.py [--selftest]
"""
import os
import sys

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import stage0two5 as S0   # noqa: E402

N, ex, fast, slow, gamma_of = S0.N, S0.ex, S0.fast, S0.slow, S0.gamma_of
WS = sp.symbols("w0:%d" % (N*N))


def wmat():
    w = sp.zeros(N)
    for a in range(N):
        for b in range(a, N):
            w[a, b] = w[b, a] = WS[N*a + b]
    return w


def rm1(W, w=None, gauge=True):
    """lam^-1 coefficient of Ric^H(g0 + lam W) (w None), or its eps-derivative at g0 + eps w (w a matrix)"""
    g0, g0i = S0.background()
    dg0 = [[[slow(g0[d, b], c) for c in range(N)] for b in range(N)] for d in range(N)]
    Gh = gamma_of(g0i, dg0)
    A0 = [[[dg0[d][b][c] + fast(W[d, b], c) for c in range(N)] for b in range(N)] for d in range(N)]
    G0 = gamma_of(g0i, A0)
    dG = [[[ex(G0[r][a][b] - Gh[r][a][b]) for b in range(N)] for a in range(N)] for r in range(N)]
    D0 = [ex(sum(g0i[a, b]*dG[r][a][b] for a in range(N) for b in range(N))) for r in range(N)]
    if w is not None:
        wu = (-g0i*w*g0i).applyfunc(ex)            # the eps-derivative of the inverse
        G1 = gamma_of(wu, A0)
        D1 = [ex(sum(wu[a, b]*dG[r][a][b] + g0i[a, b]*G1[r][a][b] for a in range(N) for b in range(N)))
              for r in range(N)]
    out = {}
    for b in range(N):
        for c in range(b, N):
            if w is None:
                e = sum(fast(G0[a][b][c], a) - fast(G0[a][b][a], c) for a in range(N))
                if gauge:
                    e -= sum(g0[b, r]*fast(D0[r], c) + g0[c, r]*fast(D0[r], b) for r in range(N))/2
            else:
                e = sum(fast(G1[a][b][c], a) - fast(G1[a][b][a], c) for a in range(N))
                if gauge:
                    e -= sum(g0[b, r]*fast(D1[r], c) + g0[c, r]*fast(D1[r], b)
                             + w[b, r]*fast(D0[r], c) + w[c, r]*fast(D0[r], b) for r in range(N))/2
            out[(b, c)] = ex(e)
    return out


def zero(e):
    """exact zero test by expansion: every identity here is algebraic in the components (no trigonometric
    identity is needed), and expand cancels the products g0 g0^-1 exactly"""
    return sp.expand(e) == 0


def main():
    ok = {}
    g0, g0i = S0.background()
    W = S0.waves()
    w = wmat()
    # A: agreement with stage0two5's assembly
    ro = S0.ricci_orders(W)
    q = sp.Function("q")(S0.u, S0.v, S0.th)
    Wm = W.copy()                                    # a term depending on both phases: the only kind with R^(-1) != 0
    for (a, b, mono) in ((2, 3, S0.z1*S0.z2), (0, 1, S0.z1/S0.z2), (1, 4, S0.z1**2*S0.z2)):
        Wm[a, b] += q*mono
        Wm[b, a] += q*mono
    rom = S0.ricci_orders(Wm)
    mine, minem = rm1(W), rm1(Wm)
    ok["A"] = all(zero(mine[k] - ro[k][0]) and zero(minem[k] - rom[k][0]) for k in mine) and \
        all(zero(mine[k]) for k in mine) and any(not zero(minem[k]) for k in minem)
    print("  A: rm1 = ricci_orders' lam^-1 coefficient, for the waves (zero, T1) and with a two-phase term (nonzero): %s"
          % ok["A"], flush=True)
    # L1
    E = rm1(W, w)
    lin, lout = [g0i[a, 1] for a in range(N)], [g0i[a, 0] for a in range(N)]
    s_in = ex(sum(w[a, b]*lin[a]*lin[b] for a in range(N) for b in range(N)))
    s_out = ex(sum(w[a, b]*lout[a]*lout[b] for a in range(N) for b in range(N)))
    P_in = W.applyfunc(lambda q: ex(fast(fast(q, 1), 1)))
    P_out = W.applyfunc(lambda q: ex(fast(fast(q, 0), 0)))
    expect = {k: ex((s_in*P_in[k] + s_out*P_out[k])/2) for k in E}
    ok["L1"] = all(zero(E[k] - expect[k]) for k in E)
    print("  L1: E[w] = (1/2)(s_in F1^2 W_in + s_out F2^2 W_out) in all 15 components: %s; s_in = %s, s_out = %s"
          % (ok["L1"], s_in, s_out), flush=True)

    def contract(T, x, y):
        return ex(sum(T[(min(a, b), max(a, b))]*x[a]*y[b] for a in range(N) for b in range(N)))

    chi = S0.xi2*S0.z1**2 + S0.xi2b/S0.z1**2
    chip = S0.et2*S0.z2**2 + S0.et2b/S0.z2**2
    ii, oo, io = contract(E, lin, lin), contract(E, lout, lout), contract(E, lin, lout)
    ok["L2"] = zero(ii - (-2*sp.exp(-4*S0.sig)*s_out*chip)) and zero(oo - (-2*sp.exp(-4*S0.sig)*s_in*chi)) and \
        zero(io) and not zero(ii) and not zero(oo) and zero(sp.diff(ii, WS[0])) and zero(sp.diff(oo, WS[N + 1]))
    print("  L2: E(ell_in, ell_in) = %s; E(ell_out, ell_out) = %s; E(ell_in, ell_out) = %s"
          % (sp.factor(ii), sp.factor(oo), io), flush=True)
    # L3
    gauge0 = {S0.xi2: 0, S0.xi2b: 0, S0.et2: 0, S0.et2b: 0}
    E0 = {k: ex(e.subs(gauge0)) for k, e in E.items()}
    ok["L3"] = all(zero(E0[k]) for k in E0 if k[0] < 2) and any(not zero(E0[k]) for k in E0 if k[0] >= 2)
    print("  L3: with chi = chi' = 0, every component with an index u or v vanishes: %s" % ok["L3"], flush=True)
    # control: no gauge term
    En = rm1(W, w, gauge=False)
    kin, kout = [0, 1, 0, 0, 0], [1, 0, 0, 0, 0]
    wu = (g0i*w*g0i).applyfunc(ex)

    def extra(P, k):
        kup = [sum(wu[d, e]*k[e] for e in range(N)) for d in range(N)]
        Pwk = [sum(P[c, d]*kup[d] for d in range(N)) for c in range(N)]
        tr = sum(wu[d, e]*P[d, e] for d in range(N) for e in range(N))
        return {(b, c): ex((-k[b]*Pwk[c] - k[c]*Pwk[b] + k[b]*k[c]*tr)/2) for (b, c) in E}

    xi, xo = extra(P_in, kin), extra(P_out, kout)
    ok["control"] = all(zero(En[k] - E[k] - xi[k] - xo[k]) for k in E) and any(not zero(En[k] - E[k]) for k in E)
    print("  control: plain Ric's coefficient = L1's + (1/2) sum_k (-k(P_k w k) - (P_k w k)k + k k <w, P_k>), the "
          "difference nonzero: %s; its nonzero components: %s"
          % (ok["control"], sorted(k for k in E if not zero(En[k] - E[k]))))
    for k, val in ok.items():
        print(k, "PASS" if val else "FAIL")
    if "--selftest" in sys.argv:
        sys.exit(0 if all(ok.values()) else 1)


if __name__ == "__main__":
    main()
