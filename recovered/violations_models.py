#!/usr/bin/env python3
"""T-cluster repaired: the CTC model is a scope parameter, not a fixed fact.

D-CTC  : Deutsch fixed-point prescription
P-CTC  : post-selected / projective (Lloyd, Bennett-Schumacher)
INDEP  : only clauses holding independent of the quantum CTC model
"""
from itertools import product, combinations

LAWS = ["T", "H", "L", "U", "N", "C", "E", "D"]
GLOSS = {"T": "chronology", "H": "global hyperbolicity", "L": "linearity",
         "U": "unitarity", "N": "no-cloning", "C": "no superluminal signalling",
         "E": "null energy condition", "D": "no perfect discrimination"}

# (from, to, models in which the clause holds, note)
CLAUSES = [
    ("T", "H", {"D", "P", "I"}, "geometric: Cauchy problem with CTCs"),
    ("T", "E", {"D", "P", "I"}, "geometric/semiclassical: 3+1 chronology violation "
                                "needs exotic matter (scoped: asympt flat, generic)"),
    ("T", "L", {"D", "P"},      "nonlinearity is the model primitive; process-matrix "
                                "formalism treats indefinite causal structure linearly"),
    ("T", "U", {"D"},           "P-CTCs send pure to pure, create no entropy"),
    ("T", "N", {"D"},           "cloning is D-CTC specific; P-CTCs do not clone"),
    ("T", "D", {"D", "P"},      "weaker under P-CTC (linearly independent only); "
                                "contested by Bennett-Leung-Smolin-Smith"),
    ("D", "N", {"D", "P", "I"}, "perfect discrimination yields cloning"),
    ("N", "C", {"D", "P", "I"}, "Gisin 1998 - VERIFIED"),
    ("L", "C", {"D", "P", "I"}, "CONTESTED: Simon-Buzek-Gisin; Bona + Svetlichny"),
]

def close(S, model):
    S = set(S); grew = True
    while grew:
        grew = False
        for a, b, models, _ in CLAUSES:
            if model in models and a in S and b not in S:
                S.add(b); grew = True
    return frozenset(S)

def run(model, label):
    closed = {close(c, model) for r in range(len(LAWS) + 1)
              for c in combinations(LAWS, r)}
    closed = sorted(closed, key=lambda s: (len(s), sorted(s)))
    mins = [c for c in closed if c and not any(d < c and d for d in closed)]
    tclose = close({"T"}, model)
    n = sum(1 for _, _, m, _ in CLAUSES if model in m)
    print(f"\n  {label}")
    print(f"    clauses active     {n}/9")
    print(f"    closed profiles    {len(closed)} of 256")
    print(f"    closure of {{T}}      {{{''.join(sorted(tclose))}}}")
    print(f"    T minimal?         {frozenset({'T'}) in set(mins)}")
    print(f"    minimal profiles   {', '.join('{'+''.join(sorted(c))+'}' for c in mins)}")
    return len(closed), tclose, set(mins)

print("="*68)
print("  T-CLUSTER REPAIRED: CTC model as scope parameter")
print("="*68)
d = run("D", "D-CTC  (Deutsch)")
p = run("P", "P-CTC  (post-selected)")
i = run("I", "INDEP  (model-independent clauses only)")

print("\n" + "="*68)
print("  WHAT THE MODEL CHOICE COSTS")
print("="*68)
print(f"  closed profiles      D={d[0]}  P={p[0]}  I={i[0]}")
print(f"  closure of T         D={{{''.join(sorted(d[1]))}}}  "
      f"P={{{''.join(sorted(p[1]))}}}  I={{{''.join(sorted(i[1]))}}}")
print(f"  minimal sets equal across models? {d[2] == p[2] == i[2]}")
print(f"\n  laws forced by T under D but not under I: "
      f"{{{''.join(sorted(d[1] - i[1]))}}}")
print(f"  => {len(d[1] - i[1])} of the 8 coordinates are slaved to T "
      f"only by a model choice")

# what does the original ungraded table correspond to?
print(f"\n  original table (all 9 clauses, no scope) == D-CTC run: "
      f"{d[0] == 57}")
