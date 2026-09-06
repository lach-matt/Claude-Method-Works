#!/usr/bin/env python3
"""defence.py -- the defence mechanisms, indexed.

Chapter 16 states three disjoint defences and §26.8 adds a fourth on a fourth
coordinate. The claim to test is §26.8's: an error is uncatchable only if no
index carries the coordinate its dependency runs through. So index the defences
themselves, close, and read what the structure admits and the book lacks.

Coordinates, all ordered, chosen so that a larger value is a stronger demand:

  reaches   what the check has to touch
            0 the index alone
            1 a second derivation inside the index
            2 the ambient set the index is written in
            3 something outside the index -- a theorem, a measurement
  fills     where the cells of the checking index come from
            0 the object itself
            1 the object's own history (the record)
            2 someone else's document
  catches   what a failure of the check costs
            0 a wrong value
            1 a wrong derivation
            2 a value that does not exist
            3 a claim that does not mean what it says
  runnable  can the check be executed by the book on itself
            0 no -- needs a reader or an author's judgement
            1 partly -- mechanical given an external table
            2 yes -- executable against the source
"""
import itertools, sys
from zeno import State, step

# (name, reaches, fills, catches, runnable, the class it catches)
DEF = [
 ("R(X) = X          self-reference", 0, 0, 2, 2, "rules not recoverable from the cells"),
 ("D_def >= 1        two routes",     1, 0, 1, 2, "a wrong derivation"),
 ("chi total         totality",       2, 0, 2, 2, "a missing value coerced to a real one"),
 ("D_phys            the world",      3, 2, 0, 0, "a wrong value in the data"),
 ("the process index visible<=committed", 1, 1, 1, 2, "a choice that depended on its answer"),
 ("audit 22          term match",     3, 2, 3, 0, "a coordinate that means something else elsewhere"),
]
NAMES = ["reaches", "fills", "catches", "runnable"]
cells = {tuple(d[1:5]) for d in DEF}

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

def run():
    d = 4
    Rc = R(cells, d)
    box = 1
    for i in range(d): box *= len({c[i] for c in cells})
    return Rc, box

with State("defence") as st:
    Rc, box = step(st, "close the defence index", run, budget=30)
Rc = {tuple(x) for x in Rc}

print(f"\n  defences (distinct cells)  {len(cells)}   of {len(DEF)} stated")
print(f"  ambient box                {box}")
print(f"  density                    {100*len(cells)/box:.1f}%")
print(f"  |R(X)|                     {len(Rc)}")
print(f"  E(defences)                {len(Rc)-len(cells)}")
print(f"  possibility bound          0 <= E <= {box-len(cells)}")

print(f"\n  {'mechanism':<38}{'reaches':>8}{'fills':>7}{'catches':>9}{'runnable':>10}")
for n, a, b, c, r, _ in DEF:
    print(f"  {n:<38}{a:>8}{b:>7}{c:>9}{r:>10}")

gap = sorted(Rc - cells)
print(f"\n  ADMITTED AND ABSENT -- {len(gap)} cells the structure allows and the book has no defence in:")
V = [["the index alone", "a second derivation", "the ambient set", "outside the index"],
     ["the object", "the object's record", "someone else's document"],
     ["a wrong value", "a wrong derivation", "a value that does not exist",
      "a claim that does not mean what it says"],
     ["not runnable by the book", "runnable given an external table", "executable on the source"]]
for g in gap:
    print(f"    reaches   {V[0][g[0]]}")
    print(f"    fills     {V[1][g[1]]}")
    print(f"    catches   {V[2][g[2]]}")
    print(f"    runnable  {V[3][g[3]]}")
    print()

print("  the two coordinates that separate the new mechanism from the old three:")
old = [d for d in DEF if d[0].startswith(("R(X)", "D_def", "chi"))]
print(f"    the three of §16.6 all have fills = 0 (built from the object) "
      f"and runnable = 2 (executable)")
print(f"    audit 22 has fills = 2 and runnable = 0 -- the first defence whose "
      f"cells\n    cannot be filled from the object and which the book cannot run on itself")
sys.exit(0)
