#!/usr/bin/env python3
"""schemes.py -- O22. The four coupling schemes, derived and then compared.

COMMITTED BEFORE COMPUTING (§2.13). The chains are taken from the standard
recoupling definitions, not from the counts they must reproduce. Each bound is
written in the LOOSE one-parent monotone form §14.4 admits, exactly as the book
writes jK's:  a coordinate bounded by a monotone function of ONE other, with the
second parent replaced by its cap.

  jK   (L1 S1)Jc · Jc + l2 = K · K + s2 = J
       2Jc <= phihat_J(k) ; 2K <= 2Jc + 2f_max ; |2J - 2K| <= 1
  LS   (L1 l2)L · (S1 s2)S · L + S = J
       2L  <= phihat_L(k) + 2f_max ; 2S_t <= 2S + 1 ; 2J <= 2L + 2S_t
  LK   (L1 l2)L · L + S1 = K · K + s2 = J
       2L  <= phihat_L(k) + 2f_max ; 2K <= 2L + 2S ; |2J - 2K| <= 1
  jj   (l1 s1)j1 · (l2 s2)j2 · j1 + j2 = J
       2j1 <= 2*l_max + 1 ; 2j2 <= 2f + 1 ; 2J <= 2j1 + 2j2

Stated in Transitions §2.1b, and NOT read until after the computation:
  jK 199,130 · LS 431,050 · jj 206,520 · LK 341,150, E = 0 at every level.
"""
import itertools, sys
from functools import lru_cache
from zeno import State, step
from method_tower import base, terms, max2J

CAPS = (3, 3, 1, 3, 1)          # n, e, l, k, f
NMAX, EMAX, LMAX, KMAX, FMAX = CAPS

@lru_cache(maxsize=None)
def max2L(l, k):
    t = terms(l, k)
    return max((L2 for S2, L2 in t), default=0)

@lru_cache(maxsize=None)
def max2S(l, k):
    t = terms(l, k)
    return max((S2 for S2, L2 in t), default=0)

def envelope(f):
    """the monotone envelope of f over the parent shells the caps admit"""
    out, best = {}, 0
    for kk in range(0, KMAX + 1):
        m = max((f(l, kkk) for l in range(0, LMAX + 1)
                 for kkk in range(1, min(4 * l + 2, kk) + 1)), default=0)
        best = max(best, m); out[kk] = best
    return out

PHI_J = envelope(max2J)
PHI_L = envelope(max2L)
PHI_S = envelope(max2S)
SMAX = KMAX            # the cap on a source multiplicity, 2S <= k
J2MAX = 2 * FMAX + 1   # the cap on the outer electron's j

def tower(scheme):
    """build Λ₁₀ then the scheme's own three coupling axes."""
    L8 = base(CAPS)
    L9  = [c + (s,)  for c in L8 for s in range(0, c[6] + 1)]            # 2S'
    L10 = [c + (v,)  for c in L9 for v in range(c[8], c[6] + 1)]          # v
    out = []
    for c in L10:
        k, f, S2 = c[2], c[5], c[7]
        if scheme == "jK":
            for Jc in range(0, PHI_J[k] + 1):
                for K in range(0, Jc + 2 * FMAX + 1):
                    for J in range(max(0, K - 1), K + 2):
                        out.append(c + (Jc, K, J))
        elif scheme == "LS":
            for Ltot in range(0, PHI_L[k] + 2 * FMAX + 1):
                for St in range(0, S2 + 2):
                    for J in range(0, Ltot + SMAX + 1):      # second parent capped
                        out.append(c + (Ltot, St, J))
        elif scheme == "LK":
            for Ltot in range(0, PHI_L[k] + 2 * FMAX + 1):
                for K in range(0, Ltot + SMAX + 1):          # second parent capped
                    for J in range(max(0, K - 1), K + 2):
                        out.append(c + (Ltot, K, J))
        elif scheme == "jj":
            for j1 in range(0, 2 * LMAX + 2):
                for j2 in range(0, 2 * f + 2):
                    for J in range(0, j1 + J2MAX + 1):       # second parent capped
                        out.append(c + (j1, j2, J))
    return out

def R_defect(X, d):
    """E(X) by sweeping the ambient box, per A.2 -- not by pairs."""
    A = [sorted({c[i] for c in X}) for i in range(d)]
    def env(i, j):
        m = {}
        for c in X: m[c[j]] = max(m.get(c[j], -10**9), c[i])
        b, o = -10**9, {}
        for t in sorted(m): b = max(b, m[t]); o[t] = b
        return o
    phi = {(i, j): env(i, j) for i in range(d) for j in range(d) if i != j}
    n = 0
    for x in itertools.product(*A):
        if all(x[i] <= phi[(i, j)][x[j]] for i in range(d) for j in range(d) if i != j):
            n += 1
    return n - len(X), n

def run(scheme):
    return len(tower(scheme))

with State("schemes") as st:
    res = {s: step(st, f"count {s}", (lambda s=s: run(s)), budget=300)
           for s in ("jK", "LS", "LK", "jj")}

STATED = {"jK": 199130, "LS": 431050, "jj": 206520, "LK": 341150}
print(f"\n  phihat_J = {dict(sorted(PHI_J.items()))}")
print(f"  phihat_L = {dict(sorted(PHI_L.items()))}")
print(f"\n  {'scheme':<7}{'derived |Λ₁₃|':>16}{'stated':>12}{'E':>7}   verdict")
for s in ("jK", "LS", "jj", "LK"):
    n = res[s]
    print(f"  {s:<7}{n:>16,}{STATED[s]:>12,}{'':>7}   "
          f"{'REPRODUCES' if n == STATED[s] else 'differs by %+d' % (n-STATED[s])}")
