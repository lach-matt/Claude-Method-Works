#!/usr/bin/env python3
"""transfer.py -- step three: index the transfer from input to output.

INPUT  : the Schroedinger equation, for this problem, supplies a finite list of
         statements. Each is a cell.
OUTPUT : eighteen constants a(period, block), each in a surd-bounded interval.
         That index closes at E = 0 (step two).

THE TRANSFER INDEX has one cell per (input statement, output quantity it fixes).
E counts what the input admits that the output does not hold, and what the output
needs that the input does not supply. That defect IS the derivation gap, measured.

THE METHOD'S WARNINGS, observed here:
  · the brackets are LOCKED -- exact, never refitted
  · do not add an input statement to close the transfer; that is fitting the
    axioms to the answer
  · the transfer index must yield ONE reading
  · "derived / assumed" cannot be a coordinate -- that killed Lambda_const
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
    for perms in product(*[permutations(range(a)) for a in axes]):
        cs = {tuple(perms[i].index(x[i]) for i in range(len(axes))) for x in cells}
        E = len(opR(cs, len(axes))) - len(cs)
        if best is None or E < best[0]: best = (E, perms)
    return best

# ---------------------------------------------------------------- the input
# statement, what it fixes in the output, whether it is USED in the law
IN = [
 ("antisymmetry (Pauli)",      "which cells admit an electron", "used"),
 ("node theorem",              "the radicand n - l - 1",        "used"),
 ("Coulomb -Z/r",              "the n^-2 level ordering",       "used"),
 ("centrifugal l(l+1)/2r^2",   "which l can reach the core",    "not used"),
 ("electron-electron 1/r_ij",  "the amplitude a",               "NOT SUPPLIED"),
 ("exchange (antisym. energy)","the amplitude a",               "NOT SUPPLIED"),
 ("spin-orbit",                "the level within a term",       "not used"),
]
print("  STEP 3 · THE TRANSFER INDEX\n")
print("  WHAT THE INPUT SUPPLIES\n")
print(f"      {'statement':<28}{'fixes':<34}{'status'}")
for a, b, c in IN: print(f"      {a:<28}{b:<34}{c}")
print()

# ---------------------------------------------------------------- the output
OUT = [
 ("admissibility",  "Pauli",                 "supplied"),
 ("the radicand",   "node theorem",          "supplied"),
 ("the form n - a*sqrt(p)", "Coulomb + nodes","supplied"),
 ("a(period, block) VALUE", "electron-electron + exchange", "NOT SUPPLIED"),
 ("the 18-cell partition", "the table itself","supplied by the output index"),
]
print("  WHAT THE OUTPUT NEEDS\n")
print(f"      {'quantity':<26}{'from':<32}{'status'}")
for a, b, c in OUT: print(f"      {a:<26}{b:<32}{c}")
print()

# ---------------------------------------------------------------- the transfer
SRC  = ["Pauli", "nodes", "Coulomb", "centrifugal", "e-e", "exchange", "spin-orbit"]
TGT  = ["admissibility", "radicand", "form", "amplitude", "partition"]
LINK = [("Pauli","admissibility"), ("nodes","radicand"), ("Coulomb","form"),
        ("nodes","form"), ("Pauli","partition"),
        ("e-e","amplitude"), ("exchange","amplitude")]
cells = {(SRC.index(s), TGT.index(t)) for s, t in LINK}
E, perms = minE(cells, [len(SRC), len(TGT)])
print("  THE TRANSFER, AS AN INDEX\n")
print(f"      {len(cells)} links · minimum E = {E} over all orderings")
print(f"      source order : {' < '.join(SRC[i] for i in perms[0])}")
print(f"      target order : {' < '.join(TGT[i] for i in perms[1])}\n")
R = opR({(perms[0].index(a), perms[1].index(b)) for a, b in cells}, 2)
have = {(perms[0].index(a), perms[1].index(b)) for a, b in cells}
print("  THE DEFECT CELLS — what ℛ admits and the transfer does not hold\n")
for x in sorted(R - have):
    print(f"      {SRC[perms[0][x[0]]]:<14} → {TGT[perms[1][x[1]]]}")
print()
print("  READING\n")
print("      three sources are UNUSED : centrifugal, spin-orbit, and the")
print("      exchange term's angular part. two are USED but supply only the")
print("      FORM. and the amplitude has exactly two sources — the")
print("      electron-electron repulsion and exchange — neither of which")
print("      the law currently draws on.")
print()
print("      so the derivation gap is not diffuse. it is ONE target cell,")
print("      'amplitude', fed by TWO source cells, and nothing else in the")
print("      transfer is missing.")
print()
print("  WHAT THE METHOD DICTATES NEXT\n")
print("      compute a(period, block) from the electron-electron and exchange")
print("      integrals ALONE, and ask whether the eighteen values land in the")
print("      eighteen brackets. the brackets are locked; the integrals are")
print("      standard; and nothing may be fitted.")
print()
print("      that is a PASS/FAIL test, not an estimation. it either closes")
print("      the transfer or it names which cell it fails at.")
