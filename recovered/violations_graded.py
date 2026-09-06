#!/usr/bin/env python3
"""Graded clause table — Admission Law applied to the implication table.

Each clause carries its verification grade. A derived result inherits the
MINIMUM grade of its inputs. Clauses are not deleted; they are graded.
"""
import sys
sys.path.insert(0, "/home/claude/method")
from itertools import product, combinations

LAWS = ["T", "H", "L", "U", "N", "C", "E", "D"]
GLOSS = {"T": "chronology (no CTCs)", "H": "global hyperbolicity",
         "L": "linearity of evolution", "U": "unitarity",
         "N": "no-cloning", "C": "no superluminal signalling",
         "E": "null energy condition", "D": "no perfect discrimination"}
IX = {l: i for i, l in enumerate(LAWS)}

# grades: 4 = checked against primary this session
#         3 = full text read      2 = abstract    1 = snippet    0 = contested
GRADED = [
    ("T", "H", 1, "Friedman+ 1990", "unchecked this session"),
    ("T", "L", 1, "Deutsch 1991 / Bacon 2003", "SCOPE: D-CTC model only"),
    ("T", "U", 1, "DeJonghe+ 0908.2655", "SCOPE: D-CTC model only"),
    ("T", "N", 1, "Brun+", "SCOPE: D-CTC model only"),
    ("T", "D", 1, "Brun+ PRL 102.210402", "SCOPE: D-CTC model only"),
    ("T", "E", 3, "Tipler/Hawking via Lobo+Kontou",
     "SCOPE: asympt flat + generic + partially asympt predictable; "
     "achronal ANEC is CONJECTURE (Graham-Olum cond.1)"),
    ("D", "N", 1, "perfect discrimination yields cloning", "unchecked"),
    ("N", "C", 4, "Gisin 1998 quant-ph/9801005",
     "VERIFIED: perfect cloning would allow signalling; direction correct"),
    ("L", "C", 0, "Gisin 1990 / Polchinski 1991; Simon-Buzek-Gisin 2001",
     "CONTESTED: Bona PRL 90.208901 + Svetlichny; derivation called circular"),
]

def close(S, minimum_grade=0):
    S = set(S); grew = True
    while grew:
        grew = False
        for a, b, g, _, _ in GRADED:
            if g < minimum_grade:
                continue
            if a in S and b not in S:
                S.add(b); grew = True
    return frozenset(S)

def vec(S):
    return tuple(1 if l in S else 0 for l in LAWS)

def RR(X, d):
    vals = [sorted({c[i] for c in X}) for i in range(d)]
    def env(i, j):
        m = {}
        for c in X: m[c[j]] = max(m.get(c[j], -99), c[i])
        b, o = -99, {}
        for t in sorted(m): b = max(b, m[t]); o[t] = b
        return o
    phi = {(i, j): env(i, j) for i in range(d) for j in range(d) if i != j}
    return {x for x in product(*vals)
            if all(x[i] <= phi[(i, j)][x[j]] for i in range(d) for j in range(d) if i != j)}

def run(minimum_grade, label):
    closed = sorted({close(c, minimum_grade)
                     for r in range(len(LAWS) + 1)
                     for c in combinations(LAWS, r)}, key=lambda s: (len(s), sorted(s)))
    closed = [frozenset(c) for c in closed]
    X = {vec(c) for c in closed}
    R = RR(X, len(LAWS))
    E = len(R) - len(X)
    mins = [c for c in closed if c and not any(d < c and d for d in closed)]
    print(f"\n{'='*66}\n  {label}   (clauses at grade >= {minimum_grade})")
    print(f"{'='*66}")
    n_used = sum(1 for *_, g, _, _ in [(a,b,g,s,n) for a,b,g,s,n in GRADED] if g >= minimum_grade)
    print(f"  clauses admitted     {n_used}/9")
    print(f"  closed profiles      {len(X)}   of 256")
    print(f"  E(V)                 {E}")
    print(f"  minimal profiles     {len(mins)}")
    for c in sorted(mins, key=lambda s: (len(s), sorted(s))):
        print(f"    {{{''.join(sorted(c))}}}  = {', '.join(GLOSS[l] for l in sorted(c))}")
    return len(X), E, set(frozenset(m) for m in mins)

# ungraded: every clause admitted regardless of verification (original behaviour)
x0, e0, m0 = run(0, "ALL CLAUSES (original table)")
# admit only clauses that are not actively contested
x1, e1, m1 = run(1, "CONTESTED CLAUSES DEMOTED")
# admit only clauses read at full text or better
x3, e3, m3 = run(3, "FULL-TEXT-OR-BETTER ONLY")
# admit only clauses verified against primary this session
x4, e4, m4 = run(4, "VERIFIED-THIS-SESSION ONLY")

print(f"\n{'='*66}\n  INHERITANCE CHECK\n{'='*66}")
print(f"  E(V) across grades:  {e0}, {e1}, {e3}, {e4}")
print(f"  minimal-profile sets identical across grades? "
      f"{m0 == m1 == m3 == m4}")
print(f"\n  profiles gained when contested clause L->C is demoted: {x1 - x0}")
print(f"  minimal profiles only present in ungraded table:")
for c in sorted(m0 - m1, key=lambda s: sorted(s)):
    print(f"    {{{''.join(sorted(c))}}}")
print(f"  minimal profiles only present when contested demoted:")
for c in sorted(m1 - m0, key=lambda s: sorted(s)):
    print(f"    {{{''.join(sorted(c))}}}")
print(f"\n  lowest grade in table = {min(g for _,_,g,_,_ in GRADED)}")
print(f"  => any result derived from the whole table inherits grade "
      f"{min(g for _,_,g,_,_ in GRADED)}")
