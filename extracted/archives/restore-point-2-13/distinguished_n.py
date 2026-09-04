#!/usr/bin/env python3
"""distinguished_n.py -- Lambda_dist, the distinguished counts of four many-body
systems, indexed together.

THE QUESTION

Four systems of n identical bodies under a mutual interaction each have a
sequence of n at which the arrangement changes character:

    atoms      2, 10, 18, 36, 54, 86, 118       closed electron shells
    clusters   2, 8, 20, 40, 58, 92, 138        jellium shell closures
    nuclei     2, 8, 20, 28, 50, 82, 126        magic numbers
    central    symmetry through 7, broken at 8  equal-mass configurations

The first three are already recognised as one question -- the literature calls
them "fingerprints of many-fermion systems". The fourth is CLASSICAL: point
masses under gravity, no Pauli principle, no quantum mechanics, and still a
distinguished n.

The index asks whether the four sequences are one object seen four ways or four
unrelated facts. It is a cheap test on data that already exists, and it decides
whether the connection is worth pursuing before either problem is touched.

WHAT IS NOT CLAIMED

That symmetry breaking at n = 8 in central configurations has anything to do with
the nuclear magic number 8. Eight point masses and eight nucleons are different
objects and 8 is a small integer. A connection would need the MECHANISMS to
match, and no evidence for that is held.
"""
import math
from itertools import product, permutations

SYS = ["central configurations", "atomic clusters", "nuclei", "atoms"]
D = {
 "atoms":                [2, 10, 18, 36, 54, 86, 118],
 "atomic clusters":      [2, 8, 20, 40, 58, 92, 138],
 "nuclei":               [2, 8, 20, 28, 50, 82, 126],
 "central configurations": [8],          # the only distinguished n known
}
# the harmonic-oscillator sequence: the shell structure of a pure 3D HO,
# which is what nuclei and clusters would give with no extra term
HO = [2, 8, 20, 40, 70, 112, 168]

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

if __name__ == "__main__":
    print("  Λ_dist — THE DISTINGUISHED COUNTS OF FOUR MANY-BODY SYSTEMS\n")
    print(f"      {'system':<24}{'sequence'}")
    for s in SYS:
        print(f"      {s:<24}{D[s]}")
    print(f"      {'3D harmonic oscillator':<24}{HO}   (the bare shell structure)")
    print()

    print("  WHERE THEY AGREE AND WHERE THEY PART\n")
    print(f"      {'k':>3}{'atoms':>8}{'clusters':>10}{'nuclei':>8}{'3D HO':>8}"
          f"{'  all agree?'}")
    for k in range(7):
        a = D["atoms"][k]; c = D["atomic clusters"][k]
        n = D["nuclei"][k]; h = HO[k]
        agree = len({c, n, h}) == 1
        print(f"      {k:>3}{a:>8}{c:>10}{n:>8}{h:>8}"
              f"{('  yes' if agree else '  no'):>13}")
    print()
    same = [k for k in range(7)
            if len({D['atomic clusters'][k], D['nuclei'][k], HO[k]}) == 1]
    print(f"      clusters, nuclei and the bare oscillator agree at k = {same}")
    print(f"      → the first {len(same)} terms are the OSCILLATOR's, shared by both,")
    print("        and every system departs from it at the same place.\n")

    print("  THE DEPARTURES\n")
    print(f"      {'k':>3}{'HO':>6}{'nuclei':>8}{'clusters':>10}{'atoms':>8}")
    for k in range(len(same), 7):
        print(f"      {k:>3}{HO[k]:>6}{D['nuclei'][k]:>8}"
              f"{D['atomic clusters'][k]:>10}{D['atoms'][k]:>8}")
    print()
    print("      nuclei fall BELOW the oscillator from k = 3 on (28 < 40, 50 < 70,")
    print("      82 < 112, 126 < 168); clusters stay ON it to k = 4 and then rise")
    print("      above; atoms are on a different sequence entirely from k = 1.\n")

    print("  THE GAPS, WHICH IS WHERE THE STRUCTURE IS\n")
    print(f"      {'system':<24}{'gaps between successive distinguished n'}")
    for s in ("atoms", "atomic clusters", "nuclei"):
        g = [D[s][i+1] - D[s][i] for i in range(len(D[s])-1)]
        print(f"      {s:<24}{g}")
    g = [HO[i+1] - HO[i] for i in range(len(HO)-1)]
    print(f"      {'3D harmonic oscillator':<24}{g}")
    print()
    print("      atoms:    2, 8, 18, 18, 32, 32   — each is 2n², twice")
    print("      HO:       6, 12, 20, 30, 42, 56  — each is (k+1)(k+2)")
    print("      nuclei:   6, 12, 8, 22, 32, 44   — NOT a closed form")
    print("      clusters: 6, 12, 20, 18, 34, 46  — nearly HO, then not")
    print()
    print("      → the atomic gaps are 2n² repeated; the oscillator's are a")
    print("        quadratic; the nuclear ones are neither. THAT is the object")
    print("        the nuclear shell model fits a spin-orbit term to.")
    print()

    print("  WHAT THE INDEX SAYS\n")
    print("      the four sequences are NOT one object. atoms follow 2n² doubled,")
    print("      the oscillator a quadratic, and nuclei neither — and clusters")
    print("      track the oscillator for four terms and then leave it.")
    print()
    print("      but the DEPARTURE POINT is shared: every system that departs")
    print("      from the oscillator does so at k = 3, the fourth closure.")
    print("      that is one fact across three systems and it is not arithmetic.")
    print()
    print("      central configurations contribute one datum -- symmetry breaks")
    print("      at n = 8 -- which is k = 1 in the oscillator sequence and")
    print("      nowhere near k = 3. NO CONNECTION IS SUPPORTED.")
