#!/usr/bin/env python3
"""cycle1.py -- STEP 1 of the cycle: fill gaps to the limit, on real numbers.

THE ANCHOR. Everything starts from the two-dimensional periodic table. 118 real
elements, a drawn layout whose answer is known independently. If this session's
machinery does not work there, it does not work.

WHAT GETS TESTED HERE
  1  the table's own figures        E = 36, and the 26 + 10 decomposition
  2  the interval property          proved for δ on any product of chains
  3  the convexity criterion        δ⁻¹(T) a sublattice iff T convex in range
  4  the certificate form of §18.4.1 Janet as the exhibited operation
  5  the two-sided closure rule     bands close where the one-sided rule refuses
"""
import itertools, sys
from collections import Counter
from zeno import State, step

# ---- the real table: 118 elements, (period, group), with the f-block detached
GROUPS = {1: [1, 18], 2: list(range(1, 3)) + list(range(13, 19)),
          3: list(range(1, 3)) + list(range(13, 19))}
for p in (4, 5, 6, 7): GROUPS[p] = list(range(1, 19))
TABLE = {(p, g) for p in GROUPS for g in GROUPS[p]}
# ℓ as a function of group, exactly as the drawing determines it
ELL = {g: (0 if g <= 2 else (2 if g <= 12 else 1)) for g in range(1, 19)}
# n for a cell in the 18-column table: the period, with d-block offset by one
def nq(p, g):
    if g <= 2: return p
    if g >= 13: return p
    return p - 1                      # the d-block belongs to shell p−1

def R(X, d):
    A = [sorted({c[i] for c in X}) for i in range(d)]
    def env(i, j):
        m = {}
        for c in X: m[c[j]] = max(m.get(c[j], -10**9), c[i])
        b, o = -10**9, {}
        for t in sorted(m): b = max(b, m[t]); o[t] = b
        return o
    phi = {(i, j): env(i, j) for i in range(d) for j in range(d) if i != j}
    return {x for x in itertools.product(*A)
            if all(x[i] <= phi[(i, j)][x[j]] for i in range(d) for j in range(d) if i != j)}
E = lambda X, d: len(R(X, d)) - len(X)
join = lambda a, b: tuple(max(x, y) for x, y in zip(a, b))
meet = lambda a, b: tuple(min(x, y) for x, y in zip(a, b))

def t1_figures():
    Rt = R(TABLE, 2); gap = sorted(Rt - TABLE)
    # decompose: forbidden by ℓ ≤ n−1, versus real-but-deferred
    forb = [c for c in gap if ELL[c[1]] > nq(*c) - 1]
    defer = [c for c in gap if c not in forb]
    return len(TABLE), len(gap), len(forb), len(defer), Counter((nq(*c), ELL[c[1]]) for c in forb)

def t2_interval():
    """δ = group − period on the table; the theorem says it is an interval map"""
    bad = n = 0
    for a, b in itertools.combinations(sorted(TABLE), 2):
        n += 1
        da, db = a[1] - a[0], b[1] - b[0]
        for m in (join(a, b), meet(a, b)):
            dm = m[1] - m[0]
            if not (min(da, db) <= dm <= max(da, db)): bad += 1
    return n, bad

def t3_convexity():
    """δ⁻¹(T) a sublattice iff T ∩ range convex — on the real table"""
    d = lambda c: c[1] - c[0]
    rng = sorted({d(c) for c in TABLE})
    rows = []
    for name, T in [("{0}", {0}), ("{-1..1}", {-1, 0, 1}), ("{0..5}", set(range(6))),
                    ("{−1,+1} hole at 0", {-1, 1}), ("{0,2} hole at 1", {0, 2}),
                    ("all of range", set(rng))]:
        X = [c for c in TABLE if d(c) in T]; S = set(X)
        if not X: continue
        bad = sum(1 for a, b in itertools.combinations(X, 2)
                  if join(a, b) not in S or meet(a, b) not in S)
        S2 = sorted(set(T) & set(rng))
        conv = (not S2) or all(v in S2 for v in rng if S2[0] <= v <= S2[-1])
        rows.append((name, len(X), bad, conv, (bad == 0) == conv))
    return rng, rows

def t4_certificate():
    JAN = {(pr, g) for pr, w in ((1,2),(2,2),(3,8),(4,8),(5,18),(6,18),(7,32),(8,32))
           for g in range(1, w + 1)}
    CONT = {(p, i) for p in GROUPS for i in range(1, len(GROUPS[p]) + 1)}
    PL = {(p, ELL[g]) for p in GROUPS for g in GROUPS[p]}
    return [("18-column (period, group)", len(TABLE), E(TABLE, 2)),
            ("(period, position) contiguous", len(CONT), E(CONT, 2)),
            ("Janet (n+ℓ, position)", len(JAN), E(JAN, 2)),
            ("(period, ℓ) — group dropped", len(PL), E(PL, 2))]

def t5_bands():
    """the corrected two-sided rule: a band closes where a one-sided staircase would not"""
    out = []
    for name, f in [("band  |g − 3p| ≤ 4", lambda p, g: abs(g - 3 * p) <= 4),
                    ("staircase  g ≤ 3p", lambda p, g: g <= 3 * p),
                    ("congruence  g ≡ p (mod 2)", lambda p, g: (g - p) % 2 == 0)]:
        X = {c for c in TABLE if f(*c)}
        if X: out.append((name, len(X), E(X, 2)))
    return out

with State("cycle1") as st:
    n, gap, forb, defer, byc = step(st, "1 the table's figures", t1_figures, budget=120)
    npair, bad = step(st, "2 the interval property", t2_interval, budget=300)
    rng, rows = step(st, "3 the convexity criterion", t3_convexity, budget=300)
    certs = step(st, "4 the certificate form", t4_certificate, budget=120)
    bands = step(st, "5 the two-sided rule", t5_bands, budget=120)

print(f"\n  1  THE TABLE'S OWN FIGURES")
print(f"     cells {n}   E = {gap}   stated 36   {'.' if gap==36 else 'MISMATCH'}")
print(f"     forbidden by ℓ ≤ n−1  {forb}   stated 26   {'.' if forb==26 else 'MISMATCH'}")
print(f"     real but deferred      {defer}   stated 10   {'.' if defer==10 else 'MISMATCH'}")
print(f"     the forbidden, by (n, ℓ): {dict(byc)}")

print(f"\n  2  THE INTERVAL PROPERTY, on all {npair:,} pairs of the real table")
print(f"     violations: {bad}")

print(f"\n  3  THE CONVEXITY CRITERION, range(δ) = {rng}")
print(f"     {'T':<20}{'cells':>7}{'∨∧ fail':>9}{'convex':>8}")
for name, nc, b, conv, ok in rows:
    print(f"     {name:<20}{nc:>7}{b:>9}{str(conv):>8}   {'.' if ok else 'MISS'}")
print(f"     agreement {sum(1 for r in rows if r[4])} of {len(rows)}")

print(f"\n  4  THE CERTIFICATE FORM")
for nm, c, e in certs: print(f"     {nm:<34}{c:>5} cells   E = {e}")

print(f"\n  5  THE TWO-SIDED RULE, on the real table")
for nm, c, e in bands: print(f"     {nm:<28}{c:>5} cells   E = {e}")
