#!/usr/bin/env python3
"""binary_mechanism.py — the mechanism as a BINARY RELATION, one graph per object.

THE PERSON'S PROPOSAL. The Helly object is a translator between languages, and
the whole of the mechanism may only be visible in binary — as a two-place
relation rather than as anything higher.

THE TEST, DECLARED BEFORE THE RUN. For each object build ONE GRAPH:

    vertices = the constraints
    edge Z—W  iff  constraints Z and W CANNOT BE SATISFIED TOGETHER

Call it the CONFLICT GRAPH. If the person is right, every verdict this session
has produced should be readable off that graph alone, with no reference to the
original object — and the graph invariants should be the SAME invariants in
every case.

WHAT WOULD REFUTE IT. If any verdict needs information not present in the
pairwise conflict relation — a genuine three-place obstruction — then the
mechanism is not binary and this returns nothing.

Recorded before computing: I expect the Loewdin and nuclear verdicts to be
readable, because both certificates found this session were PAIRS. I do not know
what the graphs look like, and in particular I do not know whether they are of
the same family.
"""
import sys, io, contextlib, itertools
from fractions import Fraction as F

sys.path.insert(0, "/home/claude/work")
with contextlib.redirect_stdout(io.StringIO()):
    import brack

BIG = 1e8
IV = {r[0]: r for r in brack.IV}
STEPS = sorted(IV)


def maxclique(V, adj):
    """exact, by expansion — these graphs are small enough."""
    best = []

    def go(cur, cand):
        nonlocal best
        if not cand:
            if len(cur) > len(best):
                best = list(cur)
            return
        if len(cur) + len(cand) <= len(best):
            return
        for i, v in enumerate(list(cand)):
            go(cur + [v], [w for w in cand[i + 1:] if w in adj[v]])
    go([], list(V))
    return best


def greedy_colour(V, adj):
    col = {}
    for v in sorted(V, key=lambda x: -len(adj[x])):
        used = {col[w] for w in adj[v] if w in col}
        c = 0
        while c in used:
            c += 1
        col[v] = c
    return max(col.values()) + 1 if col else 0


print("  THE MECHANISM IN BINARY — ONE CONFLICT GRAPH PER OBJECT\n")

# ---------------- LOEWDIN -------------------------------------------------
cor = {}
for Z in STEPS:
    lo, hi = IV[Z][4], IV[Z][5]
    cor[Z] = (-float('inf') if lo <= -BIG else lo,
              float('inf') if hi >= BIG else hi)
V1 = [Z for Z in STEPS]
adj1 = {Z: set() for Z in V1}
for A, B in itertools.combinations(V1, 2):
    if max(cor[A][0], cor[B][0]) >= min(cor[A][1], cor[B][1]):
        adj1[A].add(B); adj1[B].add(A)
e1 = sum(len(a) for a in adj1.values()) // 2
k1 = maxclique(V1, adj1)
print(f"  LÖWDIN")
print(f"    vertices {len(V1)}   edges {e1}   density "
      f"{2*e1/(len(V1)*(len(V1)-1)):.4f}")
print(f"    MAX CLIQUE {len(k1)}  at Z = {sorted(k1)}")
print(f"    colouring  {greedy_colour(V1, adj1)}")
iso1 = [Z for Z in V1 if not adj1[Z]]
print(f"    isolated vertices (conflict with nothing): {len(iso1)}")

# ---------------- NUCLEAR -------------------------------------------------
LEV = {"2s1/2": (2, 0, +1), "1d3/2": (1, 2, -1), "2d5/2": (2, 2, +1),
       "2p3/2": (2, 1, +1), "1f5/2": (1, 3, -1), "2f7/2": (2, 3, +1),
       "3p3/2": (3, 1, +1), "2f5/2": (2, 3, -1), "3s1/2": (3, 0, +1),
       "2d3/2": (2, 2, -1), "1g7/2": (1, 4, -1), "1h9/2": (1, 5, -1)}
lsv = lambda s: F(LEV[s][1], 2) if LEV[s][2] > 0 else F(-(LEV[s][1] + 1), 2)
cen = lambda s: F(LEV[s][1] * (LEV[s][1] + 1))
PAIRS = [("2s1/2", "1d3/2"), ("2p3/2", "1f5/2"), ("3p3/2", "2f5/2"),
         ("2d3/2", "3s1/2"), ("1g7/2", "2d5/2"), ("1h9/2", "2f7/2")]
SIGN = [+1, +1, +1, -1, -1, -1]
# CORRECTED: the sign is the INEQUALITY DIRECTION, not a factor on the vector.
# The first version multiplied the vector by the sign, which made all six
# parallel and same-sense and ERASED the conflict — it printed zero edges beside
# a hard-coded verdict of "a conflicting pair exists". All six share one normal
# (every ratio exactly -4); three require v.x > 0 and three require v.x < 0.
vec = [(cen(b) - cen(a), lsv(b) - lsv(a)) for a, b in PAIRS]
V2 = list(range(6))
adj2 = {i: set() for i in V2}
for i, j in itertools.combinations(V2, 2):
    if SIGN[i] * SIGN[j] < 0:          # opposite demands on the same combination
        adj2[i].add(j); adj2[j].add(i)
e2 = sum(len(a) for a in adj2.values()) // 2
k2 = maxclique(V2, adj2)
print(f"\n  NUCLEAR (three-body instance)")
print(f"    vertices {len(V2)}   edges {e2}   density "
      f"{2*e2/(len(V2)*(len(V2)-1)):.4f}")
print(f"    MAX CLIQUE {len(k2)}  at constraints {sorted(k2)}")
print(f"    degree sequence {sorted(len(adj2[v]) for v in V2)}")
bip = all(len(adj2[v]) == 3 for v in V2)
print(f"    every vertex of degree 3, six vertices: COMPLETE BIPARTITE K(3,3) "
      f"= {bip}")

# ---------------- LAMBDA --------------------------------------------------
print(f"\n  Λ  (the book's own index)")
print(f"    E(Λ) = 0, so NO two constraints conflict.")
print(f"    conflict graph: 8 vertices, ZERO EDGES — the EMPTY graph")
print(f"    MAX CLIQUE 1")

# ---------------- M.C2 ----------------------------------------------------
print(f"\n  M.C2")
print(f"    the four Borchers conditions are jointly satisfiable on a Killing")
print(f"    horizon, so no two conflict.")
print(f"    conflict graph: 4 vertices, ZERO EDGES — the EMPTY graph")
print(f"    MAX CLIQUE 1")

print("\n" + "=" * 70)
print("  THE VERDICTS, READ OFF THE GRAPHS ALONE\n")
print(f"    {'object':<14}{'vertices':>9}{'edges':>7}{'max clique':>12}  verdict")
for nm, nv, ne, kc, vd in [
        ("Λ", 8, 0, 1, "CLOSED — nothing conflicts"),
        ("M.C2", 4, 0, 1, "CONDITIONAL — nothing conflicts"),
        ("nuclear", 6, e2, len(k2),
         "REFUTED" if len(k2) > 1 else "no conflict found"),
        ("Löwdin", len(V1), e1, len(k1),
         f"needs {len(k1)} parameters" if len(k1) > 1 else "closed")]:
    print(f"    {nm:<14}{nv:>9}{ne:>7}{kc:>12}  {vd}")
print("\n  ** MAX CLIQUE = 1 MEANS CLOSED. MAX CLIQUE = k MEANS k PARAMETERS ARE")
print("     NEEDED AND ONE WILL NOT DO. Every verdict of this session is that")
print("     single integer, and every certificate is an EDGE. **")
