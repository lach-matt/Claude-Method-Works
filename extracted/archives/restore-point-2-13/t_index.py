#!/usr/bin/env python3
"""t_index.py -- Lambda_t, the index of the corridor position.

t = (a - L)/(U - L) is where the carried quantity a sits in its corridor. It was
first reported as a formula, sqrt(l(l+1)/2), fitted at p and d and wrong at s. It
was then reported as a table, one value per (l, period). It is neither: it is an
index, and the same three questions apply to it as to every other object in this
work.

    does it close · what does it refuse · which carrier is the more particular

MEASURED per species, from the ionisation energies, with the Pauli fraction in
the radicand:

    a = (n - nu) / sqrt(n - l - 1 + q/2(2l+1))      nu = sqrt(R/IE)
    t = (a - L)/(U - L)

t is near-constant across the occupancy q within a cell -- 6p runs 1.0237,
1.0417, 1.0009, 1.0036, 0.9946, 0.9940 across all six -- so the cell is
(l, period) and q is not a coordinate of it.
"""
import math, statistics as st
from itertools import product, permutations

L = "spdfg"

# measured t, per species: (element, Z, n, l, q, t)
T = [
 ("Be", 4,2,0,1,0.2678),("Mg",12,3,0,1,0.3349),("Ca",20,4,0,1,0.2420),
 ("Mn",25,4,0,1,0.2655),("Zn",30,4,0,1,0.4005),("Sr",38,5,0,1,0.1942),
 ("Tc",43,5,0,1,0.2180),("Cd",48,5,0,1,0.3419),("Ba",56,6,0,1,0.1882),
 ("Hg",80,6,0,1,0.3257),("Ra",88,7,0,1,0.1951),
 ("Al",13,3,1,0,1.0925),("Si",14,3,1,1,1.1576),("P", 15,3,1,2,1.1798),
 ("S", 16,3,1,3,1.1082),("Cl",17,3,1,4,1.1203),("Ar",18,3,1,5,1.1196),
 ("Ga",31,4,1,0,1.0331),("Ge",32,4,1,1,1.0696),("As",33,4,1,2,1.0818),
 ("Se",34,4,1,3,1.0443),("Br",35,4,1,4,1.0499),("Kr",36,4,1,5,1.0490),
 ("In",49,5,1,0,1.0124),("Sn",50,5,1,1,1.0432),("Sb",51,5,1,2,1.0469),
 ("Te",52,5,1,3,1.0225),("I", 53,5,1,4,1.0222),("Xe",54,5,1,5,1.0205),
 ("Tl",81,6,1,0,1.0237),("Pb",82,6,1,1,1.0417),("Bi",83,6,1,2,1.0009),
 ("Po",84,6,1,3,1.0036),("At",85,6,1,4,0.9946),("Rn",86,6,1,5,0.9940),
 ("Y", 39,4,2,0,1.8453),("Zr",40,4,2,1,1.7924),
 ("Lu",71,5,2,0,1.4151),("Hf",72,5,2,1,1.4504),
]

def opR(X, d):
    X = set(X); vals = [sorted({x[i] for x in X}) for i in range(d)]
    def env(i, j):
        m = {}
        for x in X: m[x[j]] = max(m.get(x[j], -10**9), x[i])
        b, o = -10**9, {}
        for t_ in sorted(m): b = max(b, m[t_]); o[t_] = b
        return o
    phi = {(i,j): env(i,j) for i in range(d) for j in range(d) if i != j}
    return {x for x in product(*vals)
            if all(x[i] <= phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i != j)}

if __name__ == "__main__":
    print("  Λ_t — THE CORRIDOR POSITION, AS AN INDEX\n")
    print("      cells are (ℓ, n) where n is the subshell's principal number —")
    print("      the period in which it fills. q is NOT a coordinate: t barely")
    print("      moves across a subshell.\n")

    C = {}
    for el, Z, n, l, q, t in T:
        C.setdefault((l, n), []).append((el, q, t))

    print(f"      {'ℓ':>3}{'n':>4}{'species':>9}{'t range':>18}{'spread':>9}"
          f"{'  √(ℓ(ℓ+1)/2)'}")
    for k in sorted(C):
        v = [x[2] for x in C[k]]
        print(f"      {L[k[0]]:>3}{k[1]:>4}{len(v):>9}"
              f"{f'{min(v):.4f} – {max(v):.4f}':>18}{max(v)-min(v):>9.4f}"
              f"{math.sqrt(k[0]*(k[0]+1)/2):>14.4f}")
    print()

    print("  THE GRID\n")
    ls = sorted({k[0] for k in C}); ns = sorted({k[1] for k in C})
    print(f"      {'':<5}" + "".join(f"{n:>10}" for n in ns))
    for l in ls:
        row = f"      {L[l]:<5}"
        for n in ns:
            v = C.get((l, n))
            row += f"{(f'{st.median([x[2] for x in v]):.3f}' if v else '·'):>10}"
        print(row)
    print()

    cells = {(ls.index(l), ns.index(n)) for l, n in C}
    R = opR(cells, 2)
    print(f"  CLOSURE : |X| = {len(cells)} · |ℛ| = {len(R)}"
          f" · E = {len(R)-len(cells)} · box = {len(ls)*len(ns)}\n")
    miss = sorted(R - cells)
    if miss:
        print("      admitted but absent:")
        for a, b in miss:
            print(f"          ℓ = {L[ls[a]]}, n = {ns[b]}")
        print()

    print("  WHAT IT REFUSES\n")
    for l in ls:
        for n in ns:
            if (l, n) in C: continue
            why = ("n ≤ ℓ, Pauli-forbidden" if n <= l else
                   "the subshell exists but has a one-sided corridor, "
                   "or no ionisation energy held")
            print(f"      ℓ = {L[l]}, n = {n} : {why}")
    print()

    print("  THE VALUE ALONG EACH AXIS\n")
    print("      along n at fixed ℓ — t falls toward the centrifugal value:")
    for l in ls:
        v = [(n, st.median([x[2] for x in C[(l,n)]])) for n in ns if (l,n) in C]
        if len(v) < 2: continue
        print(f"          ℓ = {L[l]} : " + "  ".join(f"n={n} {t:.3f}" for n, t in v)
              + f"   → √(ℓ(ℓ+1)/2) = {math.sqrt(l*(l+1)/2):.4f}")
    print()
    print("      so the ℓ axis carries the LIMIT and the n axis the APPROACH.")
    print("      √(ℓ(ℓ+1)/2) is universal; t(ℓ,n) is the per-cell value; and")
    print("      the gap between them is Λ_phys's domain axis exactly.")
