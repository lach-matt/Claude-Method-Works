#!/usr/bin/env python3
"""protindex.py -- the twenty-four protocols, indexed.

The audits are indexed at §3. The protocols are not. Indexing them says what
kinds of protocol this book has and, by its defect, what kinds it does not.

COORDINATES, all ordered so ℛ applies
  trigger   when the protocol fires
              0 before any work   1 during a computation   2 before writing
              3 after writing
  object    what it governs
              0 a number   1 a source   2 a claim   3 the whole work
  failure   what it prevents
              0 an unbounded run     1 a wrong figure
              2 an unsupported claim 3 a lost object
  earned    what put it in the book
              0 stated at the outset  1 one failure  2 a repeated failure

COMMITTED BEFORE COMPUTING (§2.13)
  (a) the protocol index is OPEN — a book that adds protocols when it fails will
      not have covered the space evenly
  (b) its density is well below the periodic table's 42%, so E measures sparsity
      as much as structure and will be read with §18.4.1's asymmetry in mind
  (c) the protocols cluster at 'earned = one failure', because that is how this
      book has actually acquired them
"""
import itertools, sys
from collections import Counter
from zeno import State, step

# (name, trigger, object, failure, earned)
P = [
 ("2.1  channel construction",      0, 3, 2, 0),
 ("2.2  admissibility",             0, 2, 2, 0),
 ("2.3  cost resolvability",        0, 0, 0, 0),
 ("2.4  dilution",                  1, 0, 1, 1),
 ("2.5  census before search",      0, 1, 3, 1),
 ("2.6  declines are recorded",     3, 2, 3, 1),
 ("2.7  exhaustive verification",   1, 0, 1, 0),
 ("2.8  two independent routes",    1, 0, 1, 2),
 ("2.9  refuse rather than coerce", 1, 2, 2, 1),
 ("2.10 retrieval",                 0, 1, 3, 1),
 ("2.11 provenance",                3, 1, 2, 1),
 ("2.12 withdrawal",                3, 2, 3, 2),
 ("2.13 commit before you look",    0, 2, 2, 2),
 ("2.14 compute, then write",       2, 0, 1, 2),
 ("2.15 apply P8 to every failure", 3, 3, 3, 2),
 ("2.16 the grid",                  0, 3, 2, 0),
 ("2.17 triangulation",             1, 0, 1, 1),
 ("2.18 computable or decided",     2, 2, 2, 1),
 ("2.19 what a safe repair needs",  1, 3, 3, 2),
 ("2.20 the prime directive",       1, 3, 0, 2),
 ("2.21 a figure removed",          2, 0, 3, 1),
 ("2.22 a corroborable entry",      2, 1, 2, 1),
 ("2.23 stated by its expression",  2, 2, 2, 1),
 ("2.24 never one heuristic",       1, 0, 1, 2),
]
AX = [["before any work", "during a computation", "before writing", "after writing"],
      ["a number", "a source", "a claim", "the whole work"],
      ["an unbounded run", "a wrong figure", "an unsupported claim", "a lost object"],
      ["stated at the outset", "one failure", "a repeated failure"]]

def R(X, d=4):
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
    cells = {tuple(p[1:]) for p in P}
    Rx = R(cells)
    box = 1
    for i in range(4): box *= len({c[i] for c in cells})
    return cells, Rx, box

with State("protindex") as st:
    cells, Rx, box = step(st, "index the protocols", run, budget=120)

print(f"  THE PROTOCOL INDEX")
print(f"    protocols        {len(P)}")
print(f"    distinct cells   {len(cells)}   collisions {len(P) - len(cells)}")
print(f"    box              {box}   density {100*len(cells)/box:.1f}%")
print(f"    |ℛ(X)|           {len(Rx)}")
print(f"    E(protocols)     {len(Rx) - len(cells)}")

print(f"\n  where the protocols sit:")
for k, ax in enumerate(AX):
    c = Counter(p[k+1] for p in P)
    print(f"    {['trigger','object','failure','earned'][k]:<9}"
          + " · ".join(f"{ax[v]} {c[v]}" for v in sorted(c)))

print(f"\n  admitted and absent — protocol shapes the structure allows and this book lacks:")
for c in sorted(Rx - cells):
    print(f"    fires {AX[0][c[0]]:<22} governs {AX[1][c[1]]:<16} "
          f"prevents {AX[2][c[2]]:<22} earned by {AX[3][c[3]]}")

dup = [k for k, v in Counter(tuple(p[1:]) for p in P).items() if v > 1]
if dup:
    print(f"\n  protocols sharing a cell — indistinguishable in these coordinates:")
    for k in dup:
        print(f"    {' · '.join(p[0] for p in P if tuple(p[1:]) == k)}")
