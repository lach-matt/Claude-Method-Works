#!/usr/bin/env python3
"""charge_index.py -- Lambda_charge, and the eight-index cypher.

Register 1292 recorded that c is one symbol in three positions: inside
u = ln(Ne/c^(2/3)), as the base of c^(-x), and inside the exponent itself,
x = c^(1/3)/sqrt(Ne). Every degeneracy of the session was between a charge term
and something else. A coordinate appearing three times with different signs
cannot sit on one monotone axis -- so charge needs its own index, in which each
role is a cell rather than a repetition.

THE TEST. If the three roles are genuinely distinct, Lambda_charge closes. If two
are the same role in different notation, it does not -- and that says the equation
is over-specified in c.
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

# ------------------------------------------------------------------ Lambda_charge
# role, carrier it acts through, sign of its effect on delta, regime where it bites
ROLE = ["screening", "decay base", "decay rate", "ordering"]
CARR = ["u", "c itself", "Ne", "the configuration"]
SIGN = ["lowers", "raises"]
REG  = ["neutral", "low", "hydrogenic"]

CH = [
 # c inside u = ln(Ne/c^(2/3)) -- raising c lowers u, which lowers delta
 ("c in u",            "screening",  "u",                "lowers", "neutral"),
 ("c in u",            "screening",  "u",                "lowers", "low"),
 ("c in u",            "screening",  "u",                "lowers", "hydrogenic"),
 # c as the base of c^(-x) -- raising c lowers delta directly
 ("c^(-x) base",       "decay base", "c itself",         "lowers", "neutral"),
 ("c^(-x) base",       "decay base", "c itself",         "lowers", "low"),
 ("c^(-x) base",       "decay base", "c itself",         "lowers", "hydrogenic"),
 # c inside x = c^(1/3)/sqrt(Ne) -- raising c raises x, which lowers delta faster
 ("c in x",            "decay rate", "Ne",               "lowers", "low"),
 ("c in x",            "decay rate", "Ne",               "lowers", "hydrogenic"),
 # c selecting the filling order -- Madelung at c <= 2, hydrogenic at c >= 3
 ("c selects order",   "ordering",   "the configuration","raises", "hydrogenic"),
]

print("  Λ_charge — THE ROLES OF THE CHARGE, AS CELLS\n")
print(f"      {'occurrence':<18}{'role':<13}{'carrier':<20}{'sign':<9}{'regime'}")
for n, r, c, s, g in CH:
    print(f"      {n:<18}{r:<13}{c:<20}{s:<9}{g}")
cells = {(ROLE.index(r), CARR.index(c), SIGN.index(s), REG.index(g))
         for _, r, c, s, g in CH}
print(f"\n      {len(CH)} occurrences · {len(cells)} distinct cells\n")

E, perms = minE(cells, [len(ROLE), len(CARR), len(SIGN), len(REG)])
print(f"  CLOSURE: minimum E = {E} over all axis orderings\n")
print(f"      role    order : {' < '.join(ROLE[i] for i in perms[0])}")
print(f"      carrier order : {' < '.join(CARR[i] for i in perms[1])}")
print(f"      sign    order : {' < '.join(SIGN[i] for i in perms[2])}")
print(f"      regime  order : {' < '.join(REG[i] for i in perms[3])}\n")

# does dropping any one role close it?
print("  IS ANY ROLE REDUNDANT?  drop each and see whether E falls\n")
print(f"      {'dropped':<14}{'cells':>6}{'min E':>8}")
for drop in ROLE:
    sub = {(ROLE.index(r), CARR.index(c), SIGN.index(s), REG.index(g))
           for _, r, c, s, g in CH if r != drop}
    if not sub: continue
    e2, _ = minE(sub, [len(ROLE), len(CARR), len(SIGN), len(REG)])
    print(f"      {drop:<14}{len(sub):>6}{e2:>8}")
print()

# ------------------------------------------------------------------ eight-index cypher
print("  THE EIGHT-INDEX CYPHER\n")
IX = [("Λ",         "atoms/transfers", 8,  976, "0",   "yes", "q"),
      ("Λ_spectra", "channels",        4,  328, ">0",  "no",  "δ, n*"),
      ("Λ_phys",    "parameters",      4,   22, "6",   "no",  "the value"),
      ("Λ_law",     "laws",            2,    7, "0",   "yes", "the form"),
      ("Λ_const",   "constants",       2,   14, "0",   "yes", "the value"),
      ("Λ_var",     "variables",       2,   11, "0",   "yes", "δ"),
      ("Λ_ryd",     "series",          2,    5, "0",   "yes", "δ₀"),
      ("Λ_charge",  "the charge's roles", 4, len(cells), str(E),
       "yes" if E == 0 else "no", "the charge's effect")]
print(f"      {'index':<12}{'indexes':<20}{'co':>3}{'cells':>7}{'E':>5}{'closes':>8}"
      f"   output")
for n, w, c, ce, e, cl, out in IX:
    print(f"      {n:<12}{w:<20}{c:>3}{ce:>7}{e:>5}{cl:>8}   {out}")
print()
nclose = sum(1 for x in IX if x[5] == "yes")
print(f"      {nclose} of {len(IX)} close · "
      f"{sum(1 for x in IX if ',' in x[6])} have a non-singleton output\n")

print("  THE TWO CRITERIA, SEPARATED\n")
print("      ℛ-CLOSURE     : the coordinates admit no cell the data does not hold")
print("      SINGLETON     : the index yields one reading, not a choice of readings")
print()
print("      they are independent. Λ_var passes ℛ with δ and n* both present,")
print("      because both land in the same cell — only the singleton test sees it.")
print()
print("  WHAT REMAINS OPEN\n")
print("      Λ_spectra : two outputs (δ, n*) and c in three positions.")
print("                  the singleton test says drop n*. Λ_charge says the")
print("                  three c-roles are or are not distinct — and that is")
print("                  what this index was built to decide.")
print("      Λ_phys    : E = 6, cause unknown. dropping 'source' did not help.")
