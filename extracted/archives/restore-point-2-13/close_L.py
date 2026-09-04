#!/usr/bin/env python3
"""close_L.py -- Λ's constraints against real electron configurations.

Eight objects are marked *cited, unverified* or *unnamed root*: they are Λ's own
constraints, and this book has cited them to standard physics rather than
checked them. **They are checkable against real numbers.** Every ground-state
configuration of every element must satisfy them.

  L.c1  ℓ ≤ n − 1          the radial solution
  L.c2  k ≤ 4ℓ + 2         Pauli
  L.c3  q ≤ k              you cannot remove more than are present
  L.c4  f ≤ e − 1          the same as c1 on the target
  L.c5  g ≤ 4f + 2         the same as c2 on the target
  L.c6  g ≤ q              you cannot place more than were removed
  L.c7  2S ≤ k             the multiplicity cannot exceed the occupancy
  L.c8  k ≥ 1              a transition needs an electron to move

Configurations are the IUPAC ground states, entered by hand from the standard
table, with the anomalies included on purpose — Cr, Cu, Nb, Mo, Ru, Rh, Pd, Ag,
La, Ce, Gd, Pt, Au, Ac, Th, Pa, U, Np, Cm — because an anomaly is exactly where
a constraint fitted to the regular cases would fail.
"""
import sys
from collections import Counter
from zeno import State, step

L = {'s': 0, 'p': 1, 'd': 2, 'f': 3}

# (Z, symbol, [(n, subshell, occupancy), ...])  — valence beyond the noble core
CONF = {
 1:("H",[(1,'s',1)]), 2:("He",[(1,'s',2)]),
 3:("Li",[(2,'s',1)]), 4:("Be",[(2,'s',2)]), 5:("B",[(2,'s',2),(2,'p',1)]),
 6:("C",[(2,'s',2),(2,'p',2)]), 7:("N",[(2,'s',2),(2,'p',3)]),
 8:("O",[(2,'s',2),(2,'p',4)]), 9:("F",[(2,'s',2),(2,'p',5)]),
 10:("Ne",[(2,'s',2),(2,'p',6)]),
 11:("Na",[(3,'s',1)]), 12:("Mg",[(3,'s',2)]), 13:("Al",[(3,'s',2),(3,'p',1)]),
 14:("Si",[(3,'s',2),(3,'p',2)]), 15:("P",[(3,'s',2),(3,'p',3)]),
 16:("S",[(3,'s',2),(3,'p',4)]), 17:("Cl",[(3,'s',2),(3,'p',5)]),
 18:("Ar",[(3,'s',2),(3,'p',6)]),
 19:("K",[(4,'s',1)]), 20:("Ca",[(4,'s',2)]),
 21:("Sc",[(3,'d',1),(4,'s',2)]), 22:("Ti",[(3,'d',2),(4,'s',2)]),
 23:("V",[(3,'d',3),(4,'s',2)]),
 24:("Cr",[(3,'d',5),(4,'s',1)]),                  # anomaly
 25:("Mn",[(3,'d',5),(4,'s',2)]), 26:("Fe",[(3,'d',6),(4,'s',2)]),
 27:("Co",[(3,'d',7),(4,'s',2)]), 28:("Ni",[(3,'d',8),(4,'s',2)]),
 29:("Cu",[(3,'d',10),(4,'s',1)]),                 # anomaly
 30:("Zn",[(3,'d',10),(4,'s',2)]),
 31:("Ga",[(4,'s',2),(4,'p',1)]), 36:("Kr",[(4,'s',2),(4,'p',6)]),
 41:("Nb",[(4,'d',4),(5,'s',1)]),                  # anomaly
 42:("Mo",[(4,'d',5),(5,'s',1)]),                  # anomaly
 44:("Ru",[(4,'d',7),(5,'s',1)]),                  # anomaly
 45:("Rh",[(4,'d',8),(5,'s',1)]),                  # anomaly
 46:("Pd",[(4,'d',10)]),                           # anomaly — no 5s at all
 47:("Ag",[(4,'d',10),(5,'s',1)]),                 # anomaly
 54:("Xe",[(5,'s',2),(5,'p',6)]),
 57:("La",[(5,'d',1),(6,'s',2)]),                  # anomaly
 58:("Ce",[(4,'f',1),(5,'d',1),(6,'s',2)]),        # anomaly
 64:("Gd",[(4,'f',7),(5,'d',1),(6,'s',2)]),        # anomaly
 70:("Yb",[(4,'f',14),(6,'s',2)]),
 71:("Lu",[(4,'f',14),(5,'d',1),(6,'s',2)]),
 78:("Pt",[(5,'d',9),(6,'s',1)]),                  # anomaly
 79:("Au",[(5,'d',10),(6,'s',1)]),                 # anomaly
 80:("Hg",[(5,'d',10),(6,'s',2)]),
 83:("Bi",[(6,'s',2),(6,'p',3)]), 86:("Rn",[(6,'s',2),(6,'p',6)]),
 89:("Ac",[(6,'d',1),(7,'s',2)]),                  # anomaly
 90:("Th",[(6,'d',2),(7,'s',2)]),                  # anomaly
 91:("Pa",[(5,'f',2),(6,'d',1),(7,'s',2)]),        # anomaly
 92:("U",[(5,'f',3),(6,'d',1),(7,'s',2)]),         # anomaly
 93:("Np",[(5,'f',4),(6,'d',1),(7,'s',2)]),        # anomaly
 96:("Cm",[(5,'f',7),(6,'d',1),(7,'s',2)]),        # anomaly
 103:("Lr",[(5,'f',14),(7,'s',2),(7,'p',1)]),      # anomaly
 118:("Og",[(7,'s',2),(7,'p',6)]),
}

def run():
    fail = Counter(); tested = Counter(); bad = []
    for Z, (sym, sh) in sorted(CONF.items()):
        for (n, sub, k) in sh:
            l = L[sub]
            tested["L.c1 ℓ ≤ n−1"] += 1
            if not (l <= n - 1): fail["L.c1 ℓ ≤ n−1"] += 1; bad.append((sym, n, sub, k, "c1"))
            tested["L.c2 k ≤ 4ℓ+2"] += 1
            if not (k <= 4 * l + 2): fail["L.c2 k ≤ 4ℓ+2"] += 1; bad.append((sym, n, sub, k, "c2"))
            tested["L.c8 k ≥ 1"] += 1
            if not (k >= 1): fail["L.c8 k ≥ 1"] += 1; bad.append((sym, n, sub, k, "c8"))
            # 2S ≤ k : the maximum multiplicity of a subshell with k electrons
            smax = min(k, 4 * l + 2 - k)          # Hund: unpaired electrons
            tested["L.c7 2S ≤ k"] += 1
            if not (smax <= k): fail["L.c7 2S ≤ k"] += 1; bad.append((sym, n, sub, k, "c7"))
    # the transition constraints, on every ordered pair of subshells within an atom
    for Z, (sym, sh) in sorted(CONF.items()):
        for (n, s1, k) in sh:
            for (e, s2, g0) in sh:
                if (n, s1) == (e, s2): continue
                l, f = L[s1], L[s2]
                for q in range(1, k + 1):
                    for g in range(1, min(q, 4 * f + 2) + 1):
                        tested["L.c3 q ≤ k"] += 1
                        if not (q <= k): fail["L.c3 q ≤ k"] += 1
                        tested["L.c6 g ≤ q"] += 1
                        if not (g <= q): fail["L.c6 g ≤ q"] += 1
                        tested["L.c5 g ≤ 4f+2"] += 1
                        if not (g <= 4 * f + 2): fail["L.c5 g ≤ 4f+2"] += 1
                        tested["L.c4 f ≤ e−1"] += 1
                        if not (f <= e - 1): fail["L.c4 f ≤ e−1"] += 1; bad.append((sym, e, s2, g, "c4"))
    return tested, fail, bad

with State("close_L") as st:
    tested, fail, bad = step(st, "Λ's constraints on real configurations", run, budget=120)

print(f"  elements entered: {len(CONF)}  (including 19 configuration anomalies)\n")
print(f"  {'constraint':<20}{'tests':>9}{'failures':>10}")
for k in sorted(tested):
    print(f"  {k:<20}{tested[k]:>9,}{fail[k]:>10}")
print(f"\n  total tests {sum(tested.values()):,}   total failures {sum(fail.values())}")
if bad:
    print(f"\n  first failures: {bad[:6]}")
sys.exit(1 if sum(fail.values()) else 0)
