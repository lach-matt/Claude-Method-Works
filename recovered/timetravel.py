from itertools import product
exec(open('/home/claude/entry_test.py').read().split('boxes =')[0])

# Lambda_9 cells: (n,l,k,q,e,f,g,2S,2S')
src = lambda c: (c[0], c[1], c[2], c[7])          # n, l, k, 2S
tgt = lambda c: (c[4], c[5], c[6], c[8])          # e, f, g, 2S'
qof = lambda c: c[3]

cells = L9
S9 = set(cells)

# --- objects: shapes that appear as a source or as a target ---
sources = {src(c) for c in cells}
targets = {tgt(c) for c in cells}
print(f"cells {len(cells):,}   distinct sources {len(sources)}   distinct targets {len(targets)}")
print(f"targets that are legal sources: {len(targets & sources)} of {len(targets)}")

# --- composability, per 7.11.0 ---
from collections import defaultdict
by_src = defaultdict(list)
for c in cells: by_src[src(c)].append(c)

def compose(a, b):
    """b after a; a's target must equal b's source."""
    q = min(qof(a), qof(b))
    return (a[0], a[1], a[2], q, b[4], b[5], b[6], a[7], b[8])

pairs = 0; fail = 0
for a in cells:
    for b in by_src.get(tgt(a), ()):
        pairs += 1
        if compose(a, b) not in S9: fail += 1
print(f"\ncomposable pairs {pairs:,}  (book states 41,682)   closure failures {fail}")

# --- identities: is there e_A with e_A o a = a and b o e_A = b ? ---
ident_cand = [c for c in cells if src(c) == tgt(c)]
print(f"\nendomorphisms (source shape == target shape): {len(ident_cand)}")
true_id = []
for A in sources:
    cands = [c for c in ident_cand if src(c) == A]
    for e in cands:
        left  = all(compose(a, e) == a for a in cells if tgt(a) == A)
        right = all(compose(e, b) == b for b in by_src.get(A, ()))
        if left and right: true_id.append((A, e))
print(f"objects carrying a genuine identity morphism: {len(true_id)} of {len(sources)}")

# --- inverses: a: A->B, is there b: B->A with b o a an identity at A? ---
rev = 0; inv = 0
idset = {A for A, _ in true_id}
for a in cells:
    backs = [b for b in by_src.get(tgt(a), ()) if tgt(b) == src(a)]
    if backs: rev += 1
    for b in backs:
        c = compose(a, b)
        if src(c) == tgt(c) and any(c == e for A, e in true_id):
            inv += 1; break
print(f"morphisms with a reverse morphism B->A: {rev:,} of {len(cells):,}")
print(f"morphisms with a genuine inverse (b o a = id_A): {inv}")

# --- is occupancy a time function? does it decrease along composition? ---
viol = 0
for a in cells:
    for b in by_src.get(tgt(a), ()):
        # occupancy of the composite's target vs its source
        if b[6] > a[2]: viol += 1
print(f"\ntime function test: composites with target occupancy > source occupancy: {viol}")

# --- closed timelike curves: cycles in the object graph ---
edges = defaultdict(set)
for c in cells: edges[src(c)].add(tgt(c))
# self-loops
loops = [A for A in edges if A in edges[A]]
print(f"objects with a self-loop (A -> A): {len(loops)} of {len(sources)}")
# any cycle at all: Tarjan-lite via DFS colouring
colour = {}
cyc = 0
def dfs(u):
    global cyc
    colour[u] = 1
    for v in edges.get(u, ()):
        if colour.get(v, 0) == 1: cyc += 1
        elif colour.get(v, 0) == 0: dfs(v)
    colour[u] = 2
import sys; sys.setrecursionlimit(10000)
for A in list(edges):
    if colour.get(A, 0) == 0: dfs(A)
print(f"back-edges found in DFS (cycles, incl. self-loops): {cyc}")

# --- what the self-loops are ---
print("\nself-loop objects (n, l, k, 2S), with the transfer each admits:")
for A in sorted(loops):
    qs = sorted({qof(c) for c in by_src[A] if tgt(c) == A})
    print(f"  {A}   q in {qs}")

# --- conservative transitions: q == g, transfer neither lost nor gained ---
cons = [c for c in cells if c[3] == c[6]]
print(f"\nconservative cells (q == g): {len(cons):,} of {len(cells):,} "
      f"= {100*len(cons)/len(cells):.1f}%")
lossy = [c for c in cells if c[3] > c[6]]
print(f"lossy cells (q > g, electrons removed and not placed): {len(lossy):,}")
