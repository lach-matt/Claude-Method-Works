#!/usr/bin/env python3
"""layerledger5.py -- the exponent and derivative ledgers of EQUALITY5-LAYER.md round 2 (sections R2.4-R2.7).

  L1 (exact rationals) Theorem L for Theorem 1's solution with round 2's remainder bound |w| <= C lam^(N-5) eps_M(v1)
     (Lemma L.4) and level y = lam^p, p = 14, Landau index m = 56 M: the conditions
       (e1) margin       2p             > 3 + s          (e2) lam^4 eps_M          4 + p(1 - M/m)    > 3 + s
       (e3) degree two   1 + 2p(1-M/m)  > 3 + s          (e4) remainder w           N - 5 + p(1-M/m)  > 3 + s
       (e5) window       p/m            < 1              (e6) L.4's hypothesis      p(1 - M/m)        > 3
       (e7) the term q   4 + 2p(1-M/m)  > 3 + s          (e8) inside the layer      2p                > 1
     with s = p (K(v_s - tau0) != 0) or s = p(1 + 2/kappa), kappa = 64 (the double root rho*), hold for every N >= 9
     (K >= 6) and every M in {M_*(N) = 2N + 8, 8, 64, 1024}.  Control: N = 8 violates (e4).
  L2 (exact rationals) Theorem L for Theorem 2's solution: |w| <= C lam^(N_P - 3) eps_M(v1) (Lemma L.4_P), N_P = K + 4 +
     ceil(4 beta0), beta0 >= 2, K >= 6; Kinf != 0 so s = p only; (e1)-(e8) hold.  Control: a hypothetical N_P = 7 with
     the round-1 exponent N_P - 6 violates (e4).
  L3 (exact integers) The derivative costs: with c_osc(1, i) = i, c_osc(m+1, i) = max(c_osc(m, i+2), c_osc(m, i+1),
     i + 2) (transport source with two derivatives, Sigma data with one, the wave with two), c_mean(j, i) = max(c_osc(j+1,
     i), c_osc(j, i+2), c_mean(j-1, i+2)), c_phi = c_mean, c_Psi(j, i) = c_mean(j, i+2), c_delta(1, i) = i,
     c_delta(m+1, i) = max(c_delta(m, i+2), c_delta(m, i+1), c_Psi(m, i), c_mean(m, i+2), c_osc(m, i+2)), the residual
     c_res(i) = max(c_osc(N+1, i+2), c_mean(N, i+2), c_phi(N, i+2)), the correction c_U(j) = j + c_res(0) and the data of
     w at level three c_U(3): closed forms c_osc(j, i) = i + 2j - 2, c_mean(j, i) = i + 2j, c_delta(j, i) <= i + 2j, and
     every cost Lemmas L.3-L.4 use (i <= 4) is at most M_*(N) = 2N + 8, for N = 3, ..., 40.  Control: a stage source
     with three derivatives (c_osc(m+1, i) = c_osc(m, i+3)) exceeds 2N + 8.
  L4 (exact) Round 1's remainder exponent N - 6 needs N >= 10 (K >= 7) in (e4); round 2's N - 5 needs N >= 9 (K >= 6).

Labels: computed (exact arithmetic).  Run: python3 checks/layerledger5.py   (under a second)
"""
import sys
from fractions import Fraction as Fr
from functools import lru_cache


def ledger(p, m_over_M, M, wexp, kap=None):
    p, M = Fr(p), Fr(M)
    m = m_over_M*M
    s = p*(1 + (Fr(2, kap) if kap else 0))
    e = 1 - M/m
    return {"e1": 2*p > 3 + s, "e2": 4 + p*e > 3 + s, "e3": 1 + 2*p*e > 3 + s, "e4": wexp + p*e > 3 + s,
            "e5": p/m < 1, "e6": p*e > 3, "e7": 4 + 2*p*e > 3 + s, "e8": 2*p > 1}


def l1(control=False):
    if control:
        return all(ledger(14, 56, 2*8 + 8, 8 - 5).values())
    ok = True
    for N in range(9, 41):
        for M in (2*N + 8, 8, 64, 1024):
            for kap in (None, 64):
                ok &= all(ledger(14, 56, M, N - 5, kap).values())
    c = ledger(14, 56, 2*9 + 8, 9 - 5, 64)
    print("  L1 N = 9 (K = 6), M = 26, the double root: " + ", ".join("%s %s" % kv for kv in c.items())
          + "; all N in [9, 40], M, both cases: %s" % ok, flush=True)
    return ok


def l2(control=False):
    if control:
        return all(ledger(14, 56, 2*7 + 8, 7 - 6).values())
    ok = True
    for K in range(6, 30):
        for beta0 in (2, Fr(5, 2), 7, 40):
            NP = K + 4 + -(-4*Fr(beta0) // 1)
            for M in (2*int(NP) + 8, 8, 1024):
                ok &= all(ledger(14, 56, M, int(NP) - 3).values())
    print("  L2 Theorem 2's solution, K in [6, 29], beta0 in {2, 5/2, 7, 40}: (e1)-(e8) hold: %s" % ok, flush=True)
    return ok


def costs(N, three=False):
    @lru_cache(maxsize=None)
    def c_osc(j, i):
        if j == 1:
            return i
        return max(c_osc(j - 1, i + (3 if three else 2)), c_osc(j - 1, i + 1), i + 2)

    @lru_cache(maxsize=None)
    def c_mean(j, i):
        if j == 0:
            return -1
        return max(c_osc(j + 1, i), c_osc(j, i + 2), c_mean(j - 1, i + 2))

    def c_psi(j, i):
        return c_mean(j, i + 2)

    @lru_cache(maxsize=None)
    def c_delta(j, i):
        if j == 1:
            return i
        m = j - 1
        return max(c_delta(m, i + 2), c_delta(m, i + 1), c_psi(m, i), c_mean(m, i + 2), c_osc(m, i + 2))

    c_res = lambda i: max(c_osc(N + 1, i + 2), c_mean(N, i + 2), c_mean(N, i + 2))      # noqa: E731
    used = [c_osc(j, i) for j in range(1, N + 1) for i in range(5)]
    used += [c_mean(j, i) for j in range(1, N + 1) for i in range(5)]
    used += [c_delta(j, 0) for j in range(1, N + 1)]
    used += [c_res(i) for i in range(3)] + [j + c_res(0) for j in range(4)]
    closed = all(c_osc(j, i) == i + 2*j - 2 for j in range(1, N + 2) for i in range(6))
    closed &= all(c_mean(j, i) == i + 2*j for j in range(1, N + 1) for i in range(6))
    closed &= all(c_delta(j, i) <= i + 2*j for j in range(1, N + 1) for i in range(6))
    return max(used), closed


def l3(control=False):
    ok = True
    worst = None
    for N in range(3, 41):
        mx, closed = costs(N, three=control)
        good = mx <= 2*N + 8 and closed
        ok &= good
        if N == 9:
            worst = mx
    if not control:
        print("  L3 closed forms and every used cost <= 2N + 8 for N in [3, 40]: %s (at N = 9: largest cost %d <= 26)"
              % (ok, worst), flush=True)
    return ok


def l4(control=False):
    r1 = min(N for N in range(3, 30) if all(all(ledger(14, 56, 2*N + 8, N - 6, k).values()) for k in (None, 64)))
    r2 = min(N for N in range(3, 30) if all(all(ledger(14, 56, 2*N + 8, N - 5, k).values()) for k in (None, 64)))
    if control:
        return r1 == r2
    print("  L4 least N with (e1)-(e8): round 1's exponent N - 6: %d (K >= %d); round 2's N - 5: %d (K >= %d)"
          % (r1, r1 - 3, r2, r2 - 3), flush=True)
    return r1 == 10 and r2 == 9


def main():
    ok = True
    for name, f in (("L1", l1), ("L2", l2), ("L3", l3), ("L4", l4)):
        good = f()
        ctl = f(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    print("layerledger5: %s" % ("all checks pass, every control fails" if ok else "FAILURES"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
