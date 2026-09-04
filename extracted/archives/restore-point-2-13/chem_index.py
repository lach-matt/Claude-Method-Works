#!/usr/bin/env python3
"""chem_index.py -- Lambda_chem, the chemical properties of a species and the
physics quantities that require them.

WHY THIS EXISTS

Repeatedly in the Loewdin work a residual has been left unexplained because I
looked for a universal account of it. Each time the answer was a property of the
individual species. The record:

  · the 1.029 factor on t(l) = sqrt(l(l+1)/2)   -- p and d both 2.9% high
  · the occupancy slope varying by subshell     -- 0.021 to 0.243
  · no f corridor, so sqrt(6) untested          -- an f-block property
  · the crossing charge set by n_f              -- 0 -> 2, 14 -> 3, 28 -> 5
  · Seaton's ratio valid only at p = 0          -- a domain, not a failure

Lambda_phys closed on (source, domain) with NO parameter of this work in the
universal column. The index has been saying this all along.

THE INDEX

A cell is (chemical property, physics quantity it supplies, the species class it
holds on). The chemistry is not decoration -- it is where the physics parameter
gets its value, and the index records which property answers which quantity.
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

# ---------------------------------------------------------------------------
# property, the physics quantity it supplies, the class it holds on, measured?
CHEM = [
 ("ionisation energy",   "a from a single state",     "every species",  "yes"),
 ("ionisation energy",   "the initiation t(l)",       "every species",  "yes"),
 ("ground configuration","the corridor L, U",         "every species",  "yes"),
 ("ground configuration","p, the node count",         "every species",  "yes"),
 ("closed f shell n_f",  "the crossing charge",       "period 6, 7",    "yes"),
 ("subshell radius",     "the occupancy slope",       "one subshell",   "no"),
 ("oxidation state +2",  "which ladders are clean",   "group 2",        "yes"),
 ("closed core, 1S0",    "single-parent Rydberg series","group 2, noble","yes"),
 ("centrifugal barrier", "the collapse switch",       "d and f only",   "yes"),
 ("lanthanide contraction","the 14-electron screening","period 6",      "yes"),
 ("relativistic 7s",     "the delayed crossing",      "period 7",       "yes"),
 ("electron affinity",   "-- nothing yet",            "every species",  "no"),
 ("electronegativity",   "-- nothing yet",            "every species",  "no"),
]

PROP = sorted({c[0] for c in CHEM})
QTY  = sorted({c[1] for c in CHEM})
CLS  = ["every species", "group 2, noble", "group 2", "period 6, 7",
        "period 6", "period 7", "d and f only", "one subshell"]

if __name__ == "__main__":
    print("  Λ_chem — CHEMICAL PROPERTY → PHYSICS QUANTITY → CLASS\n")
    print(f"      {'property':<24}{'supplies':<30}{'holds on':<17}{'measured'}")
    for a, b, c, d in CHEM:
        print(f"      {a:<24}{b:<30}{c:<17}{d}")
    print()

    held = [c for c in CHEM if not c[1].startswith("--")]
    print(f"      {len(held)} of {len(CHEM)} properties supply a physics quantity\n")

    print("  THE UNEXPLAINED RESIDUALS, AND WHICH CELL THEY BELONG TO\n")
    R = [("the 1.029 factor on t(l)", "subshell radius", "one subshell",
          "size sets how far above the bracket the initiation sits"),
         ("no f corridor",            "centrifugal barrier", "d and f only",
          "f has no two-sided bracket because no rival competes both ways"),
         ("occupancy slope 0.021-0.243", "subshell radius", "one subshell",
          "compact subshells feel each added electron more"),
         ("crossing charge 2,3,5",    "closed f shell n_f", "period 6, 7",
          "14 f electrons screen the nucleus for everything outside")]
    for res, prop, cls, why in R:
        print(f"      {res}")
        print(f"          property : {prop}")
        print(f"          class    : {cls}")
        print(f"          why      : {why}")
        print()

    # closure: the property axis is ordered by how MANY species its class
    # covers -- from "every species" down to "one subshell". that order is
    # given by the class, so only the class axis is searched.
    ORD = ["every species", "group 2, noble", "group 2", "period 6, 7",
           "period 6", "period 7", "d and f only", "one subshell"]
    cells = {(PROP.index(a), ORD.index(c)) for a, b, c, _ in CHEM}
    R = opR(cells, 2)
    print(f"  CLOSURE on (property, class), class ordered by breadth\n")
    print(f"      {len(cells)} cells · |ℛ| = {len(R)} · E = {len(R)-len(cells)}")
    print(f"      box = {len({c[0] for c in cells})*len({c[1] for c in cells})}\n")

    print("  THE RULE THIS INDEX ENFORCES\n")
    print("      before calling a residual unexplained, look up which chemical")
    print("      property supplies it and which class it holds on. a residual")
    print("      with a named property and a named class is not unexplained —")
    print("      it is a per-species quantity, and asking for a universal")
    print("      account of it is the error the domain protocol blocks.")
