# r2-ch12l.py — Phase R2, main §12.11.0.8 "Past, present and future — a path, not a triangle" (L2842–2897), chat 75.
# Every tower-computable claim of the section re-measured on ALL 976 cells of Λ₈ and ALL 1,654 cells of Λ₉ (tower-2.py by path
# through r2lib.load_tower); constraint tree of Λ₈ = r2lib.EDGES9 without the 2S′ edge; composable cells as r2-ch12e/f define them
# (a cell whose target (e,f,g,2S′) is a source object (n,ℓ,k,2S) of some cell). Deterministic; prints no wall-clock time.
import importlib.util, os, statistics, itertools
from collections import Counter, defaultdict
H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py')); r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib); T = r2lib.load_tower()

L8 = T.L8(); L9 = T.L9()
N8 = ['n', 'ℓ', 'k', 'q', 'e', 'f', 'g', '2S']
A_IDX, Q_IDX, B_IDX = (0, 1, 2, 7), 3, (4, 5, 6)               # past (source), present (transfer), future (target) on Λ₈
EDGES8 = [e for e in r2lib.EDGES9 if 8 not in e]                # Λ₈'s constraint tree: 7 edges on 8 coordinates
proj = lambda c, idx: tuple(c[i] for i in idx)

print(f'|Λ8| {len(L8):,} | |Λ9| {len(L9):,} | tower-2.py L8/L9 by path')

# ---- L2846–2847: the three parts treated as free, and conditioned on q ----
A = {proj(c, A_IDX) for c in L8}; Qs = {c[Q_IDX] for c in L8}; B = {proj(c, B_IDX) for c in L8}
prod = len(A) * len(Qs) * len(B); defect = prod - len(L8)
Aq = defaultdict(set); Bq = defaultdict(set)
for c in L8: Aq[c[Q_IDX]].add(proj(c, A_IDX)); Bq[c[Q_IDX]].add(proj(c, B_IDX))
cond = sum(len(Aq[v]) * len(Bq[v]) for v in Aq) - len(L8)
print(f'== L2846–2847 free parts: |A|(n,ℓ,k,2S) {len(A)} · |Q| {len(Qs)} · |B|(e,f,g) {len(B)} = {prod:,} against |Λ8| {len(L8)}: defect {defect:,} = overcount {100*defect/len(L8):.1f}% | conditioned on q: Σ_q|A_q||B_q| − |Λ8| = {cond}')
print(f'   per q: A_q {[len(Aq[v]) for v in sorted(Aq)]} B_q {[len(Bq[v]) for v in sorted(Bq)]} cross-sections {[len(Aq[v])*len(Bq[v]) for v in sorted(Aq)]} (sum {sum(len(Aq[v])*len(Bq[v]) for v in Aq)})')

# ---- L2849–2860: every two-sided cut; the tree; degrees; the caterpillar ----
print(f'== L2854–2860 constraint tree on Λ8: edges {[(N8[a], N8[b]) for a, b in EDGES8]} | is_tree {r2lib.is_tree(8, EDGES8)}')
deg = Counter(); [deg.update([a, b]) for a, b in EDGES8]
leaves = [N8[i] for i in range(8) if deg[i] == 1]
spine_edges = [(a, b) for a, b in EDGES8 if deg[a] > 1 and deg[b] > 1]
print(f'   degrees {[(N8[i], deg[i]) for i in range(8)]} | leaves {leaves} | leaves removed leaves a path (caterpillar): {r2lib.is_tree(len({v for e in spine_edges for v in e}), [(sorted({v for e in spine_edges for v in e}).index(a), sorted({v for e in spine_edges for v in e}).index(b)) for a, b in spine_edges]) and all(sum(1 for a, b in spine_edges if v in (a, b)) <= 2 for e in spine_edges for v in e)}')
def cut_defect(cells, c, S1, S2):
    P = defaultdict(set); R = defaultdict(set)
    for x in cells: P[x[c]].add(proj(x, S1)); R[x[c]].add(proj(x, S2))
    return sum(len(P[v]) * len(R[v]) for v in P) - len(cells)
rows = []
for c in range(8):
    comp = r2lib.components(EDGES8, {c}, nodes=8)
    groups = defaultdict(list)
    for v, root in comp.items(): groups[root].append(v)
    parts = sorted(sorted(g) for g in groups.values())
    if len(parts) == 2:
        rows.append(f'{N8[c]}: 2 components {[[N8[i] for i in p] for p in parts]} → tree-cut defect {cut_defect(L8, c, tuple(parts[0]), tuple(parts[1]))}; coordinate-order cut (before | after) defect {cut_defect(L8, c, tuple(range(c)), tuple(range(c+1, 8)))}')
    else:
        rows.append(f'{N8[c]}: {len(parts)} component(s) {[[N8[i] for i in p] for p in parts]} — not a two-sided cut')
print('   ' + '\n   '.join(rows))

# ---- L2862–2865: the quotient on {A, q, B} is a path ----
part = {i: 'A' for i in A_IDX}; part[Q_IDX] = 'Q'; part.update({i: 'B' for i in B_IDX})
qe = Counter(tuple(sorted((part[a], part[b]))) for a, b in EDGES8 if part[a] != part[b])
print(f'== L2862–2863 quotient edges between parts: A–Q {qe[("A","Q")]} ({[(N8[a],N8[b]) for a,b in EDGES8 if {part[a],part[b]}=={"A","Q"}]}), Q–B {qe[("B","Q")]} ({[(N8[a],N8[b]) for a,b in EDGES8 if {part[a],part[b]}=={"B","Q"}]}), A–B {qe[("A","B")]} | path on three vertices (treewidth 1): {qe[("A","Q")]>=1 and qe[("B","Q")]>=1 and qe[("A","B")]==0}')
# the tower's own treewidth-2 index, Λ9′ (cycle f–g–2S′): closure, from r2lib (banked in r2-ch12i)
L9p = r2lib.lam9p(L9)
n2, jl, ml = r2lib.closure(L9p)
tri = [e for e in r2lib.EDGES9P if set(e) <= {5, 6, 8}]
print(f'   Λ9′ (cycle): edges among f, g, 2S′ {len(tri)} (a triangle, treewidth 2) | closure on {n2:,} pairs: join leaves {jl}, meet leaves {ml} — E(Λ9′) = {jl+ml}')

# ---- L2867–2879: (past, present) pairs, futures, the table, Markov ----
fut = defaultdict(set)
for c in L8: fut[(proj(c, A_IDX), c[Q_IDX])].add(proj(c, B_IDX))
sizes = sorted(len(v) for v in fut.values())
print(f'== L2867–2868 (past, present) pairs {len(fut)} | pairs determining a single future {sum(1 for v in fut.values() if len(v)==1)} | futures per pair min {sizes[0]}, median {statistics.median(sizes)}, max {sizes[-1]}')
print('   present q | distinct pasts | distinct future sets | |future|')
for v in sorted(Aq):
    fsets = {frozenset(fut[(a, v)]) for a in Aq[v]}
    print(f'   {v} | {len(Aq[v])} | {len(fsets)} | {sorted(len(f) for f in fsets)}')
cells, fails = r2lib.ci_sets(L8, list(A_IDX), list(B_IDX), [Q_IDX])
print(f'   L2877 exact conditional independence (n,ℓ,k,2S) ⊥ (e,f,g) | q on Λ8: product cells {cells}, count-test failures {fails}')

# ---- L2881–2884: nesting; the saturated bracket; E on the target end ----
vs = sorted(Aq)
fut_nest = all(Bq[vs[i]] < Bq[vs[i+1]] for i in range(len(vs)-1))
past_nest = all(Aq[vs[i]] >= Aq[vs[i+1]] for i in range(len(vs)-1))
print(f'== L2881–2882 future sets nest increasing (strict ⊂) {fut_nest} sizes {[len(Bq[v]) for v in vs]} | past sets nest decreasing (⊇) {past_nest} sizes {[len(Aq[v]) for v in vs]} | A_0 = A_1: {Aq[vs[0]]==Aq[vs[1]]}')
for v in vs:
    S = Bq[v]; lo = tuple(min(b[i] for b in S) for i in range(3)); hi = tuple(max(b[i] for b in S) for i in range(3))
    inB = {b for b in B if all(lo[i] <= b[i] <= hi[i] for i in range(3))}
    box = {b for b in itertools.product(*[range(lo[i], hi[i]+1) for i in range(3)])}
    _, j, m = r2lib.closure(sorted(S))
    print(f'   q = {v}: |B_q| {len(S)} | extremes lo {lo} hi {hi} both in B_q {lo in S and hi in S} | B ∩ [lo,hi] = B_q: {inB == S} ({len(inB)}) | full box [lo,hi] in Z³ {len(box)} (B_q = box: {box == S}) | closure of B_q: join leaves {j}, meet leaves {m}')
_, j, m = r2lib.closure(sorted(B)); print(f'   the 17-element target set B: closure join leaves {j}, meet leaves {m}')

# ---- L2886–2892: the tick over the composable cells of Λ9 ----
O = {r2lib.src(c) for c in L9}
comp = [c for c in L9 if r2lib.tgt(c) in O]
print(f'== L2886 composable cells (target is a source object) {len(comp):,} of {len(L9):,} | = cells with g ≥ 1: {len(comp)==sum(1 for c in L9 if c[6]>=1)} | non-composable {len(L9)-len(comp)}')
tick = Counter(c[2] - c[6] for c in comp)
print(f'   tick k − g over composable cells: {dict(sorted(tick.items()))} | max over ALL Λ9 cells {max(c[2]-c[6] for c in L9)}, min {min(c[2]-c[6] for c in L9)}')
split = Counter((c[2] - c[3], c[3] - c[6]) for c in comp)
print(f'   split (k−q, q−g): {dict(sorted(split.items()))} | table is its own transpose: {all(split[(i,j)]==split[(j,i)] for i in range(3) for j in range(3))}')
pure1 = sum(v for (i, j), v in split.items() if i > 0 and j == 0); pure2 = sum(v for (i, j), v in split.items() if i == 0 and j > 0); both = sum(v for (i, j), v in split.items() if i > 0 and j > 0)
src1 = sum(v for (i, j), v in split.items() if i > 0); src2 = sum(v for (i, j), v in split.items() if j > 0)
print(f'   pure k−q>0 only {pure1}, pure q−g>0 only {pure2}, both {both} | any k−q>0 {src1} against any q−g>0 {src2} (Register 357\'s "430 against 430") | tick 1 = (0,1)+(1,0) {split[(0,1)]+split[(1,0)]}, tick 2 = (0,2)+(2,0)+(1,1) {split[(0,2)]+split[(2,0)]+split[(1,1)]}')
# statistical independence of the two sources over the composable cells (L2891 "two independent sources")
N = len(comp); ci_fail = sum(1 for i in range(3) for j in range(3) if split[(i, j)] * N != sum(split[(i, jj)] for jj in range(3)) * sum(split[(ii, j)] for ii in range(3)))
exp11 = sum(split[(1, jj)] for jj in range(3)) * sum(split[(ii, 1)] for ii in range(3)) / N
print(f'   k−q ⊥ q−g on composable cells: exact count test fails on {ci_fail} of 9 cells; N(1,1) {split[(1,1)]} against independence {exp11:.1f}; mutual information {r2lib.mi([c[2]-c[3] for c in comp],[c[3]-c[6] for c in comp]):.3f} bits | marginals equal (identical contribution): {[sum(split[(i,jj)] for jj in range(3)) for i in range(3)]} vs {[sum(split[(ii,j)] for ii in range(3)) for j in range(3)]}')
# the 389 of r2-ch12f: cells on a cycle = cells whose source and target objects lie in one SCC of the object graph
edges = defaultdict(int)
for c in comp: edges[(r2lib.src(c), r2lib.tgt(c))] += 1
adj = defaultdict(list)
for (a, b) in edges: adj[a].append(b)
sccs = r2lib.tarjan(sorted(O), adj); cid = {o: i for i, cp in enumerate(sccs) for o in cp}
cyc = [c for c in comp if cid[r2lib.src(c)] == cid[r2lib.tgt(c)]]
t0 = [c for c in comp if c[2] == c[6]]
rev = sum(1 for (a, b) in edges if (b, a) in edges)
print(f'   cells on a composition cycle (source and target in one SCC; SCCs {len(sccs)}) {len(cyc)} | tick-0 composable cells {len(t0)} | the two sets are identical: {set(cyc)==set(t0)} | object edges with a reverse edge {rev} (r2-ch12f: 389)')

# ---- L2894–2895: g's ceiling min(4f+2, q) over the composable cells ----
ceil = Counter('counting (q < 4f+2)' if c[3] < 4*c[5]+2 else ('tied (q = 4f+2)' if c[3] == 4*c[5]+2 else 'shell capacity (4f+2 < q)') for c in comp)
print(f'== L2894–2895 g\'s ceiling over {len(comp):,} composable cells: ' + ' | '.join(f'{k} {v} = {100*v/len(comp):.1f}%' for k, v in sorted(ceil.items())))
ceil_all = Counter('counting' if c[3] < 4*c[5]+2 else ('tied' if c[3] == 4*c[5]+2 else 'shell') for c in L9)
ceil8 = Counter('counting' if c[3] < 4*c[5]+2 else ('tied' if c[3] == 4*c[5]+2 else 'shell') for c in L8)
print(f'   for comparison — all Λ9 cells: ' + ', '.join(f'{k} {v} ({100*v/len(L9):.1f}%)' for k, v in sorted(ceil_all.items())) + ' | Λ8 cells: ' + ', '.join(f'{k} {v} ({100*v/len(L8):.1f}%)' for k, v in sorted(ceil8.items())))
att = Counter((c[3] < 4*c[5]+2, c[6] == min(4*c[5]+2, c[3])) for c in comp)
print(f'   composable cells at the ceiling (g = min(4f+2, q)): {sum(v for (a, b), v in att.items() if b)} of {len(comp):,}; of those, ceiling by counting {att[(True, True)]}, by capacity or tie {att[(False, True)]}')
