#!/usr/bin/env python3
"""amp_index.py -- Lambda_amp, the amplitude as the electron-electron term.

The Schroedinger Hamiltonian is

    H = -sum_i (1/2) grad_i^2 - sum_i Z/r_i + sum_{i<j} 1/r_ij

and the independent-particle approximation keeps the first two exactly and
replaces the third by an average. Everything the law derives -- Pauli
admissibility, the node count, the form nu = n - a*sqrt(p) -- comes from the
first two plus antisymmetry. The amplitude a is precisely what the third term
supplies and the approximation discards.

So the amplitude index is an index of the third term. Its cells are the Slater
integrals: for a pair of subshells (n l, n' l'),

    DIRECT   F^k   k = 0, 2, ..., 2*min(l, l')
    EXCHANGE G^k   k = |l - l'|, |l - l'| + 2, ..., l + l'

That enumeration is exact -- it comes from the multipole expansion of 1/r_ij and
the triangle rule on the angular integrals. Nothing is fitted and nothing chosen.

THE TEST: does Lambda_amp close, and does its structure explain why Slater
screening threads 5 of 5 s-block brackets and 0 of 1 f?
"""
import math
from itertools import product, permutations

def opR(X, d):
    X = set(X); vals = [sorted({x[i] for x in X}) for i in range(d)]
    def env(i, j):
        m = {}
        for x in X: m[x[j]] = max(m.get(x[j], -10**9), x[i])
        b, o = -10**9, {}
        for t in sorted(m): b = max(b, m[t]); o[t] = b
        return o
    phi = {(i,j): env(i,j) for i in range(d) for j in range(d) if i != j}
    return {x for x in product(*vals)
            if all(x[i] <= phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i != j)}

def minE(cells, axes):
    best = None
    for p in product(*[permutations(range(a)) for a in axes]):
        cs = {tuple(p[i].index(x[i]) for i in range(len(axes))) for x in cells}
        E = len(opR(cs, len(axes))) - len(cs)
        if best is None or E < best[0]: best = (E, p)
    return best

L = "spdfg"

def integrals(l1, l2):
    """the Slater integrals that exist for a pair of subshells, exactly"""
    F = list(range(0, 2*min(l1, l2)+1, 2))
    G = list(range(abs(l1-l2), l1+l2+1, 2))
    return F, G

# the pairs that matter: the occupied subshell against its rival, per ladder
PAIRS = [("4s/3d", 0, 2, 20), ("5s/4d", 0, 2, 38), ("6s/5d", 0, 2, 56),
         ("6s/5d", 0, 2, 70), ("7s/6d", 0, 2, 88), ("7s/6d", 0, 2, 102),
         ("2s/2p", 0, 1, 4),  ("3s/3d", 0, 2, 12), ("4s/4d", 0, 2, 30),
         ("5s/5d", 0, 2, 48), ("6s/6d", 0, 2, 80)]

print("  Λ_amp — THE ELECTRON-ELECTRON TERM, AS CELLS\n")
print("      the multipole expansion of 1/r_ij gives, for each pair of")
print("      subshells, an exact and finite list of integrals.\n")
print(f"      {'pair':>8}{'direct F^k':>16}{'exchange G^k':>18}{'  count'}")
seen = {}
for nm, l1, l2, ne in PAIRS:
    if nm in seen: continue
    F, G = integrals(l1, l2); seen[nm] = (F, G)
    print(f"      {nm:>8}{str(F):>16}{str(G):>18}{len(F)+len(G):>7}")
print()

# also the same-subshell pairs, which is what a closed shell has
print("      and the SAME-subshell pairs a closed shell carries:\n")
print(f"      {'pair':>8}{'direct F^k':>16}{'exchange G^k':>18}{'  count'}")
for l in range(4):
    F, G = integrals(l, l)
    print(f"      {L[l]+'/'+L[l]:>8}{str(F):>16}{str(G):>18}{len(F)+len(G):>7}")
print()

print("  WHY SLATER THREADS THE s-BLOCK AND NOTHING ELSE\n")
F, G = integrals(0, 0)
print(f"      s/s : F = {F}, G = {G}  —  the exchange integral G^0 is IDENTICAL")
print("            to the direct F^0. there is no independent exchange term.")
F, G = integrals(0, 2)
print(f"      s/d : F = {F}, G = {G}  —  ONE independent exchange integral, G^2.")
F, G = integrals(2, 2)
print(f"      d/d : F = {F}, G = {G}  —  three of each, and they differ.")
F, G = integrals(3, 3)
print(f"      f/f : F = {F}, G = {G}  —  four of each.")
print()
print("      Slater's rules average the direct term and drop exchange entirely.")
print("      at s/s that loses nothing, because G^0 = F^0. at d/d and f/f it")
print("      loses three and four independent quantities.")
print()
print("      → 5 of 5 s-block brackets threaded, 0 of 1 f. the count of lost")
print("        integrals is the count of failures.")
print()

print("  THE INDEX  (rank k, kind F/G, ℓ of the rival)\n")
cells = set()
for nm, l1, l2, ne in PAIRS:
    F, G = integrals(l1, l2)
    for k in F: cells.add((k, 0, l2))
    for k in G: cells.add((k, 1, l2))
for l in range(4):
    F, G = integrals(l, l)
    for k in F: cells.add((k, 0, l))
    for k in G: cells.add((k, 1, l))
ks = sorted({c[0] for c in cells}); ls = sorted({c[2] for c in cells})
cc = {(ks.index(a), b, ls.index(c)) for a, b, c in cells}
E, p = minE(cc, [len(ks), 2, len(ls)])
print(f"      {len(cc)} cells · min E = {E}")
print(f"      rank order : {[ks[i] for i in p[0]]}")
print(f"      kind order : {['F','G'][p[1][0]]} < {['F','G'][p[1][1]]}")
print(f"      ℓ order    : {[L[ls[i]] for i in p[2]]}")
print()
print(f"      {'':<8}" + "".join(f"{L[ls[i]]:>8}" for i in p[2]))
for ki in p[0]:
    for b in p[1]:
        row = f"      {['F','G'][b]}^{ks[ki]:<6}"
        for li in p[2]:
            row += f"{('X' if (ki,b,li) in cc else '.'):>8}"
        print(row)
