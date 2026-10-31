"""stage0h5.py -- FAMILIES5 section 4e (D419): Stage 0 of the two-phase ansatz in section 1's generalised wave gauge.

Section 1 proposes solving Ric(g) - delta*_g(Ups(g) - H) = 0 with a fixed gauge source H := lam (h(X, s1) dv +
h'(X, s2) du), so that the second-harmonic gauge terms chi dv^2 and chi' du^2 are not needed (chi = chi' = 0), and
section 4d (D414, L3) shows that then each family's large coupling is killed by both contractions ell_k x ell_k. Here,
with stage0two5.py's ansatz and assembly:

  H1 (deduced by order counting, written out exactly) delta*_g H = (1/2)(d_p H_q + d_q H_p) - Gamma^r_pq H_r with
     H = lam H1: the fast derivative brings it to lam^0 and Gamma H is O(lam), so there is no lam^-1 part, and the lam^0
     part is the symmetrised fast derivative, computed here as F_1 h dv^2 + F_2 h' du^2 (F_k = d/ds_k; the dv du entry
     vanishes as h depends on z1 only and h' on z2 only): the gauge source enters Stage 0 in vv and uu only.
  H2 (exact) with chi = chi' = 0, R^(0) of stage0two5 (the waves, their transports T3, the two-dust mean) has, among the
     pure harmonics, only the vv (+-2, 0) and uu (0, +-2) entries S_(+-2), S'_(+-2); with h = sum_(+-) h_(+-2) z1^(+-2),
     h_(+-2) := -S_(+-2)/(+-2i), and h' likewise, the total R^(0) + (delta*_g H)^(0) vanishes at every pure harmonic.
     So the second harmonics are met algebraically, with no transport, and the mean (0, 0) and the mixed harmonics
     (T2, T4) are untouched.
  Control: with h = 0 the vv (2, 0) entry is nonzero; with h_2 of the wrong sign it doubles.
Not computed: the gauge condition Ups - H = 0 at order lam (section 4b's T8 with the source; by T8's structure H's
raised form g0^(uv) h enters only the r = u row, which ghat_2's angular trace sets), and its propagation.
Labels: H2 and the control computed (exact, sympy); H1 deduced.

    python3 checks/stage0h5.py [--selftest]
"""
import os
import sys

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import stage0two5 as S0   # noqa: E402

N, ex, fast, slow, gamma_of = S0.N, S0.ex, S0.fast, S0.slow, S0.gamma_of
u, v, th, z1, z2 = S0.u, S0.v, S0.th, S0.z1, S0.z2


def dstarH(W, H1):
    """(lam^-1, lam^0) parts of delta*_g H, g = g0 + lam W, H = lam H1 (H1 slow-and-fast 1-form components)"""
    g0, g0i = S0.background()
    dg0 = [[[slow(g0[d, b], c) for c in range(N)] for b in range(N)] for d in range(N)]
    A0 = [[[dg0[d][b][c] + fast(W[d, b], c) for c in range(N)] for b in range(N)] for d in range(N)]
    G0 = gamma_of(g0i, A0)           # Gamma at lam^0
    m1 = sp.zeros(N)
    z0 = sp.zeros(N)
    for p in range(N):
        for q in range(N):
            # nabla_p H_q = d_p H_q - Gamma^r_pq H_r: lam^0 from the fast derivative of lam H1; Gamma H1 is O(lam)
            z0[p, q] = ex((fast(H1[q], p) + fast(H1[p], q))/2)
    return m1, z0, G0


def harm(e):
    return S0.harmonics(e)


def main():
    ok = {}
    W = S0.waves().subs({S0.xi2: 0, S0.xi2b: 0, S0.et2: 0, S0.et2b: 0})
    hf = {n: sp.Function("h%s" % ("p" if n > 0 else "m") + str(abs(n)))(u, v, th) for n in (-3, -2, -1, 1, 2, 3)}
    hpf = {n: sp.Function("k%s" % ("p" if n > 0 else "m") + str(abs(n)))(u, v, th) for n in (-3, -2, -1, 1, 2, 3)}
    h = sum(hf[n]*z1**n for n in hf)
    hp = sum(hpf[n]*z2**n for n in hpf)
    H1 = [hp, h, 0, 0, 0]
    m1, z0, _ = dstarH(W, H1)
    expect = sp.zeros(N)
    expect[1, 1] = ex(fast(h, 1))
    expect[0, 0] = ex(fast(hp, 0))
    ok["H1"] = all(m1[p, q] == 0 for p in range(N) for q in range(N)) and \
        all(ex(z0[p, q] - expect[p, q]) == 0 for p in range(N) for q in range(N))
    print("  H1: delta*_g H at lam^-1: 0; at lam^0: F1 h dv^2 + F2 h' du^2 exactly: %s" % ok["H1"], flush=True)
    ro = S0.ricci_orders(W)
    R0 = {k: ex(val[1]) for k, val in ro.items() if isinstance(k, tuple)}
    Rbg = S0.background_ricci()
    pure = {}
    for k, e in R0.items():
        for hk, c in harm(ex(e - Rbg[k])).items():
            if hk != (0, 0) and hk[0]*hk[1] == 0 and sp.simplify(c) != 0:
                pure[(k, hk)] = sp.simplify(c)
    keys = sorted(pure)
    print("  H2: pure harmonics of R^(0) - Ric(g0) with chi = chi' = 0:", [(k, hk) for (k, hk) in keys], flush=True)
    only = set(pure) <= {((1, 1), (2, 0)), ((1, 1), (-2, 0)), ((0, 0), (0, 2)), ((0, 0), (0, -2))}
    sol = {}
    for n in (2, -2):
        sol[hf[n]] = -pure.get(((1, 1), (n, 0)), 0)/(sp.I*n)
        sol[hpf[n]] = -pure.get(((0, 0), (0, n)), 0)/(sp.I*n)
    for n in (-3, -1, 1, 3):
        sol[hf[n]] = 0
        sol[hpf[n]] = 0
    total_ok = True
    for k, e in R0.items():
        tot = ex((e - Rbg[k] + z0[k[0], k[1]]).subs(sol).doit())
        for hk, c in harm(tot).items():
            if hk != (0, 0) and hk[0]*hk[1] == 0 and sp.simplify(c) != 0:
                total_ok = False
    ok["H2"] = only and len(pure) == 4 and total_ok
    print("  H2: only vv (+-2, 0) and uu (0, +-2) present: %s; with h_(+-2) = -S_(+-2)/(+-2i), every pure harmonic of "
          "R^(0) + (delta* H)^(0) - Ric(g0) vanishes: %s" % (only and len(pure) == 4, total_ok), flush=True)
    print("      h_2 =", sp.factor(sol[hf[2]]))
    bad = dict(sol)
    bad[hf[2]] = -bad[hf[2]]
    vv = harm(ex((R0[(1, 1)] - Rbg[(1, 1)] + z0[1, 1]).subs(bad).doit())).get((2, 0), 0)
    ok["control"] = sp.simplify(pure[((1, 1), (2, 0))]) != 0 and \
        sp.simplify(vv - 2*pure[((1, 1), (2, 0))]) == 0
    print("  control: with h = 0 the vv (2, 0) entry is nonzero, with h_2 of the wrong sign it doubles: %s"
          % ok["control"])
    for k, val in ok.items():
        print(k, "PASS" if val else "FAIL")
    if "--selftest" in sys.argv:
        sys.exit(0 if all(ok.values()) else 1)


if __name__ == "__main__":
    main()
