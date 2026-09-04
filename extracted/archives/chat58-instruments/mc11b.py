"""MC-11 stage 3.  (a) General leaf-peeling: eliminate coordinates one at a time along
the caterpillar; every message is a function of ONE coordinate (width 1); equals direct
count at base cap and at a second cap.  (b) Cycle witness: add one constraint closing a
cycle; the tree-style count is wrong by exactly the signed sieve term over the cycle."""
import random, itertools, numpy as np
from mc11 import lattice, direct, meet_join

# constraint graph as edges (i,j,pred) with pred(z_i, z_j) -> bool.  Tuple positions
# 0 n, 1 l, 2 k, 3 q, 4 e, 5 f, 6 g, 7 S2.  All predicates are the Λ constraints.
EDGES = [
    (0, 1, lambda n, l: l <= n - 1),
    (1, 2, lambda l, k: 1 <= k <= 4 * l + 2),
    (2, 3, lambda k, q: q <= k),
    (3, 6, lambda q, g: g <= q),
    (5, 6, lambda f, g: g <= 4 * f + 2),
    (4, 5, lambda e, f: f <= e - 1),
    (2, 7, lambda k, S2: S2 <= k),
]
# unary domain limits that are Λ's own (n>=1, e>=1, k>=1 already in edge); box supplies rest

def peel_count(lo, hi, edges, nvars=8):
    """Variable elimination.  Returns (count, max_message_arity).  Messages are dicts
    keyed by the assignment of the REMAINING neighbour coordinates; arity 1 on a tree."""
    dom = {i: list(range(lo[i], hi[i] + 1)) for i in range(nvars)}
    # factors: each edge is a factor over its two vars; messages are factors too
    factors = [((i, j), (lambda p: (lambda a: 1 if p(*a) else 0))(pred)) for i, j, pred in edges]
    maxar = 0
    order = list(range(nvars))
    # eliminate in leaf-first order for the tree: peel degree-1 vertices repeatedly
    remaining = set(order)
    while remaining:
        # choose a variable of minimum degree in the current factor graph
        deg = {v: len(set(u for sc, _ in factors if v in sc for u in sc) - {v}) for v in remaining}  # live neighbours
        v = min(remaining, key=lambda x: (deg[x], x))
        inv = [(sc, f) for sc, f in factors if v in sc]
        rest = [(sc, f) for sc, f in factors if v not in sc]
        newscope = tuple(sorted(set(u for sc, _ in inv for u in sc) - {v}))
        maxar = max(maxar, len(newscope))
        table = {}
        for assign in itertools.product(*[dom[u] for u in newscope]):
            ctx = dict(zip(newscope, assign))
            s = 0
            for val in dom[v]:
                ctx[v] = val
                prod = 1
                for sc, f in inv:
                    prod *= f(tuple(ctx[u] for u in sc))
                    if prod == 0: break
                s += prod
            table[assign] = s
        rest.append((newscope, (lambda t, sc: (lambda a: t[a]))(table, newscope)))
        factors = rest
        remaining.discard(v)
    tot = 1
    for sc, f in factors:
        assert sc == ()
        tot *= f(())
    return tot, maxar

import sys
STAGE = sys.argv[1] if len(sys.argv)>1 else 'a'
NB = int(sys.argv[2]) if len(sys.argv)>2 else 100
if __name__ == '__main__' and STAGE=='a':
    random.seed(1106)
    print("== (a) leaf-peeling, width measured ==")
    for cap in [(3, 3, 1, 3, 1), (4, 4, 2, 5, 1), (5, 5, 2, 6, 1)]:
        cells = lattice(*cap)
        fails = 0; widths = set()
        for t in range(NB):
            x, y = random.sample(cells, 2)
            lo, hi = meet_join(x, y)
            d = direct(lo, hi, cells)
            c, w = peel_count(lo, hi, EDGES)
            widths.add(w)
            if c != d: fails += 1
        print(f"  cap {cap} |Λ|={len(cells)}: {NB} random boxes, peel≠direct: {fails}, max message arity seen: {sorted(widths)}")
    # base cap: also the two closed-form leaves are the first two peels — check identity
if __name__ == '__main__' and STAGE=='b':
    random.seed(1106)
    print("== (b) cycle witness: add S2 <= q+1 (closes triangle k–q–S2) ==")
    cap = (3, 3, 1, 3, 1); cells = lattice(*cap)
    close = (3, 7, lambda q, S2: S2 <= q + 1)
    cells_c = [z for z in cells if close[2](z[3], z[7])]
    print(f"  |Λ| = {len(cells)}, |Λ ∩ {{2S ≤ q+1}}| = {len(cells_c)} (constraint is not redundant)")
    import mc11
    E2 = EDGES + [close]
    fails = 0; widths = set(); tree_wrong = 0; sieve_ok = 0; nb = 0
    for t in range(NB):
        x, y = random.sample(cells_c, 2)
        lo, hi = meet_join(x, y)
        d = direct(lo, hi, cells_c)
        c, w = peel_count(lo, hi, E2); widths.add(w)
        if c != d: fails += 1
        # tree-style count = drop the closing edge (count in Λ), then sieve over the
        # triangle's three edges: N(T) = box points violating every constraint in T
        # (and satisfying all constraints outside the triangle).  Inclusion–exclusion:
        # count = Σ_{T⊆tri} (-1)^{|T|} N_outside-sat(T)
        tri = [EDGES[2], EDGES[6], close]           # q<=k, S2<=k, S2<=q+1
        other = [e for e in EDGES if e not in tri]
        pts = [z for z in itertools.product(*[range(lo[i], hi[i]+1) for i in range(8)])
               if all(p(z[i], z[j]) for i, j, p in other) and z[0] >= 1 and z[4] >= 1 and z[2] >= 1]
        sieve = 0; nT = {}
        for r in range(4):
            for T in itertools.combinations(range(3), r):
                N = sum(1 for z in pts if all(not tri[a][2](z[tri[a][0]], z[tri[a][1]]) for a in T))
                nT[T] = N
                sieve += (-1) ** r * N
        tree_count = direct(lo, hi, cells)   # ignores the closing constraint
        if tree_count != d: tree_wrong += 1
        if sieve == d: sieve_ok += 1
        nb += 1
    print(f"  {NB} boxes: peel≠direct {fails}; max message arity with the cycle: {sorted(widths)}")
    print(f"  tree-style count (closing edge ignored) wrong on {tree_wrong}/{NB} boxes; full 8-term sieve over the triangle correct on {sieve_ok}/{NB}")
    # exhibit one box in full
    random.seed(7)
    while True:
        x, y = random.sample(cells_c, 2); lo, hi = meet_join(x, y)
        d = direct(lo, hi, cells_c); tc = direct(lo, hi, cells)
        if tc != d: break
    print(f"  exhibit: lo={lo} hi={hi}: |box∩Λ|={tc} (tree count), |box∩Λ'|={d}; correction = {tc-d} = box points of Λ violating S2<=q+1")
