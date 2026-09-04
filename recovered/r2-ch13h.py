#!/usr/bin/env python3
# r2-ch13h.py — Phase R2, chat 81, segment 1: main §14.5 (L3732–3762) and §14.5.1 (L3763–3797).
# Re-measures on ALL cells: the Moore-family table of the three small ambients, the removability of
# every one of Λ₈'s 976 cells, the greedy-prune spread, and the EXACT minimum seed of Λ₈ by branch
# and bound on the set-cover reduction of §14.5.7's definition (φ̂(G) = φ̂(X)).
# Deterministic: no wall-clock output.

import importlib.util, os, itertools, random
import numpy as np

H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib)
T = r2lib.load_tower()
L8 = [tuple(c) for c in T.L8()]
L9 = [tuple(c) for c in T.L9()]


def Rset(X):
    """ℛ(X): every cell of the ambient box ∏ Âᵢ(X) with xᵢ ≤ φ̂ᵢⱼ(xⱼ) for all i ≠ j (§6.1 L1540).
    Copied verbatim from r2-ch13g.py (chat 80), which took it from r2-ch12r.py's Rbox; owed to r2lib."""
    A = np.array(sorted(set(X)), dtype=np.int64); d = A.shape[1]
    vals = [np.unique(A[:, i]) for i in range(d)]
    phi = {}
    for i in range(d):
        for j in range(d):
            if i == j: continue
            m = np.full(int(A[:, j].max()) + 1, -1, dtype=np.int64)
            for v in vals[j]: m[v] = A[A[:, j] <= v, i].max()
            phi[(i, j)] = m
    G = np.array(np.meshgrid(*vals, indexing='ij')).reshape(d, -1).T
    ok = np.ones(len(G), dtype=bool)
    for (i, j), m in phi.items(): ok &= G[:, i] <= m[G[:, j]]
    return set(map(tuple, G[ok]))


# ---------------------------------------------------------------- §1  Λ₈: no cell is removable
print('=== (1) L3768–3770: ℛ(Λ \\ {x}) = Λ for every one of the 976 cells ===')
S8 = set(L8)
assert len(S8) == 976
print('   |Λ₈| = %d, E(Λ₈) = %d' % (len(S8), len(Rset(L8)) - len(S8)))
bad = []; adds = {}
for x in L8:
    r = Rset([c for c in L8 if c != x])
    adds[len(r) - 975] = adds.get(len(r) - 975, 0) + 1
    if r != S8: bad.append(x)
print('   cells whose deletion the operator does NOT restore exactly: %d of 976' % len(bad))
print('   |ℛ(Λ \\ {x})| − |Λ \\ {x}| over all 976 cells: %s' % sorted(adds.items()))


# ---------------------------------------------------------------- §2  greedy prune, spread
print('=== (2) L3772–3773: greedy removal while ℛ still returns Λ, independent shuffles ===')
def prune(order):
    keep = list(L8)
    for x in order:
        trial = [c for c in keep if c != x]
        if len(trial) and Rset(trial) == S8: keep = trial
    return keep

sizes = []
for seed in (1, 2, 3, 4, 5):
    o = list(L8); random.Random(seed).shuffle(o)
    g = prune(o); sizes.append(len(g))
    assert Rset(g) == S8
print('   prune-greedy sizes over five seeded shuffles: %s' % sizes)
print('   spread of prune-greedy: min %d max %d' % (min(sizes), max(sizes)))
rev = prune(sorted(L8, reverse=True)); fwd = prune(sorted(L8))
print('   reverse-delete (descending order) %d ; ascending order %d' % (len(rev), len(fwd)))


# ---------------------------------------------------------------- §3  the exact minimum seed
print('=== (3) L3775 / L3934: seed(Λ₈) = 7 exactly?  set-cover reduction, branch and bound ===')
# §14.5.7's definition: G is a seed iff φ̂(G) = φ̂(X).  With G ⊆ Λ this is equivalent to ℛ(G) = Λ:
#   elements to cover = (a) each value of each coordinate (the ambient box ∏Âᵢ must be restored) and
#                       (b) each envelope step (i, j, v): some x ∈ G with xⱼ ≤ v and xᵢ = φ̂ᵢⱼ(v).
d = 8
A = np.array(sorted(S8), dtype=np.int64)
vals = [sorted(set(int(v) for v in A[:, i])) for i in range(d)]
print('   per-coordinate value counts %s ; ambient box %d cells' % ([len(v) for v in vals], int(np.prod([len(v) for v in vals]))))
elements = []
for i in range(d):
    for v in vals[i]: elements.append(('val', i, v))
for i in range(d):
    for j in range(d):
        if i == j: continue
        for v in vals[j]:
            top = max(int(x[i]) for x in A if x[j] <= v)
            elements.append(('phi', i, j, v, top))
eidx = {e: n for n, e in enumerate(elements)}
cover = []                                   # cover[c] = bitmask of the elements cell c witnesses
cells = sorted(S8)
for c in cells:
    m = 0
    for i in range(d): m |= 1 << eidx[('val', i, c[i])]
    for e in elements:
        if e[0] == 'phi':
            _, i, j, v, top = e
            if c[j] <= v and c[i] == top: m |= 1 << eidx[e]
    cover.append(m)
FULL = (1 << len(elements)) - 1
print('   %d elements (%d value slots + %d envelope steps), %d candidate cells' %
      (len(elements), sum(len(v) for v in vals), len(elements) - sum(len(v) for v in vals), len(cells)))

best = [None]
def bb(covered, chosen, limit):
    if covered == FULL:
        best[0] = list(chosen); return True
    if len(chosen) >= limit: return False
    rest = FULL & ~covered
    # branch on the uncovered element with the fewest covering cells
    bestel, bestcands = None, None
    n = 0
    while rest:
        b = rest & -rest; e = b.bit_length() - 1; rest ^= b
        cands = [k for k in range(len(cover)) if cover[k] >> e & 1]
        if bestcands is None or len(cands) < len(bestcands): bestel, bestcands = e, cands
        n += 1
        if len(bestcands) <= 1: break
    for k in bestcands:
        if bb(covered | cover[k], chosen + [k], limit): return True
    return False

exact = None
for limit in range(1, 12):
    best[0] = None
    if bb(0, [], limit): exact = limit; break
    print('   no seed of size %d' % limit)
print('   EXACT minimum seed of Λ₈ = %d' % exact)
G = [cells[k] for k in best[0]]
print('   witness (%d cells): %s' % (len(G), ' '.join(str(c) for c in G)))
print('   ℛ(witness) = Λ₈ : %s   |ℛ(witness)| = %d' % (Rset(G) == S8, len(Rset(G))))
print('   compression 976 / %d = %.4f  (L3775 prints "139 to 1, exactly"; 976 = 7·139 + 3)' % (exact, 976 / exact))
print('   L3939 "d + c − 1 would give 11": d = 8, c = max value count %d, d + c − 1 = %d' %
      (max(len(v) for v in vals), d + max(len(v) for v in vals) - 1))


# ---------------------------------------------------------------- §4  the three small ambients
print('=== (4) L3738–3741: closed subsets of the three small ambients ===')
def closure_mask(cellsA, mask):
    """ℛ on a subset of a small ambient, by the same box sweep as Rset, on bitmasks."""
    if mask == 0: return 0
    X = [cellsA[i] for i in range(len(cellsA)) if mask >> i & 1]
    w = len(X[0])
    vs = [sorted({x[i] for x in X}) for i in range(w)]
    phi = {}
    for i in range(w):
        for j in range(w):
            if i == j: continue
            for v in vs[j]: phi[(i, j, v)] = max(x[i] for x in X if x[j] <= v)
    out = 0
    for n, c in enumerate(cellsA):
        if any(c[i] not in vs[i] for i in range(w)): continue
        if all(c[i] <= phi[(i, j, c[j])] for i in range(w) for j in range(w) if i != j): out |= 1 << n
    return out

AMB = [('2 × 2 × 2', list(itertools.product(*[range(2)] * 3))),
       ('3 × 3', list(itertools.product(*[range(3)] * 2))),
       ('2 × 2 × 2 × 2', list(itertools.product(*[range(2)] * 4)))]
for name, cellsA in AMB:
    N = len(cellsA)
    closed = [m for m in range(1 << N) if closure_mask(cellsA, m) == m]
    # control: the bitmask closure agrees with Rset on every non-empty subset of the two small ambients
    if N <= 9:
        agree = all(closure_mask(cellsA, m) == sum(1 << i for i, c in enumerate(cellsA) if c in Rset([cellsA[i] for i in range(N) if m >> i & 1]))
                    for m in range(1, 1 << N))
        print('   [%s] bitmask closure agrees with Rset on all %d non-empty subsets: %s' % (name, (1 << N) - 1, agree))
    nz = [m for m in closed if m]
    cs = set(closed)
    pairs_i = sum(1 for a in closed for b in closed if (a & b) in cs)
    pairs_u = sum(1 for a in closed for b in closed if (a | b) in cs)
    tot = len(closed) ** 2
    unord = sum(1 for a, b in itertools.combinations(closed, 2) if (a | b) in cs)
    unordtot = len(closed) * (len(closed) - 1) // 2
    print('   [%s] %d cells: closed subsets %d (with ∅) / %d (without ∅), 2^n = %d, share %.3f%% / %.3f%%'
          % (name, N, len(closed), len(nz), 1 << N, 100 * len(closed) / (1 << N), 100 * len(nz) / (1 << N)))
    print('        ∩ closed %d of %d ordered pairs = %.1f%% ; ∪ closed %d of %d ordered = %.1f%%, %d of %d unordered = %.1f%%'
          % (pairs_i, tot, 100 * pairs_i / tot, pairs_u, tot, 100 * pairs_u / tot, unord, unordtot, 100 * unord / unordtot))
    # meet-irreducibles of the family: C ≠ ⋂{D closed : D ⊋ C}
    top = max(closed)
    mi = []
    for C in closed:
        ups = [D for D in closed if D != C and (C & D) == C]
        if not ups: continue                      # the top element is excluded by convention
        inter = ups[0]
        for D in ups[1:]: inter &= D
        if inter != C: mi.append(C)
    gen = set(mi) | {top}
    while True:
        new = {a & b for a in gen for b in gen} - gen
        if not new: break
        gen |= new
    print('        meet-irreducible closed sets %d = %.4f per cell ; they generate the family under ∩ : %s (|gen| %d of %d)'
          % (len(mi), len(mi) / N, gen == cs, len(gen), len(closed)))


# ---------------------------------------------------------------- §5  Λ₉'s random subsets
print('=== (5) L3751–3753: Λ₉ is closed and random subsets of it are open ===')
S9 = set(L9)
print('   |Λ₉| = %d, E(Λ₉) = %d' % (len(S9), len(Rset(L9)) - len(S9)))
rng = random.Random(458)
openc = 0; sizes9 = []
for _ in range(300):
    m = rng.randrange(2, len(L9))
    X = rng.sample(L9, m); sizes9.append(m)
    if len(Rset(X)) != m: openc += 1
print('   random subsets tested 300, sizes %d…%d, open (ℛ(X) ≠ X): %d' % (min(sizes9), max(sizes9), openc))
