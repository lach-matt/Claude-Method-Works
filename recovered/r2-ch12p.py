# r2-ch12p.py — Phase R2, main §12.11.0.12 "How an index enters a larger index, and what it looks like from there" (L2999–3031), chat 75.
# Rank = coordinate sum (r2-ch12f: Λ₉ graded by coordinate sum, ranks 3…23). Λ₁₃'s rank chain (values, bits, compression, bits lost,
# share surviving), Λ₉'s rank fibres (min, max), and Λ₉'s composition (r2-ch12e/f: b∘a when tgt(a) = src(b), composite
# (src a, min(q_a, q_b), tgt b)) reduced to (rank a, rank b) → rank(b∘a): distinct inputs, inputs with a single output rank, the worst
# spread, the range of composite ranks — on ALL 41,682 composable ordered pairs. tower-2.py by path via r2lib. Deterministic.
import importlib.util, os, math
from collections import Counter, defaultdict
import numpy as np
H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py')); r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib); T = r2lib.load_tower()

L13 = T.L13(); A = np.array(L13, dtype=np.int64); sums = A.sum(axis=1); ranks13 = sorted(set(sums.tolist()))
nv = len(ranks13); bits = math.log2(len(L13)); bitsr = math.log2(nv)
print(f'== L3004–3009 Λ13: cells {len(L13):,} | rank (coordinate sum) values {nv} ({ranks13[0]}…{ranks13[-1]}, contiguous {ranks13 == list(range(ranks13[0], ranks13[-1]+1))}) | log2 cells {bits:.2f} bits → log2 ranks {bitsr:.2f} | compression {len(L13)/nv:,.0f} to 1 | bits lost per cell {bits - bitsr:.2f} | surviving {100*bitsr/bits:.1f}% | dimension 1 of Λ (n) has {len({c[0] for c in T.L8()})} values')
print(f'   lattice length of Λ13 (r2-ch12n) 43 = max sum − min sum {ranks13[-1]-ranks13[0]}: {ranks13[-1]-ranks13[0] == 43} (every cover on the greedy chain raises the sum by one)')

L9 = T.L9(); rk = lambda c: sum(c); fib = Counter(rk(c) for c in L9); ranks9 = sorted(fib)
print(f'== L3011–3012 Λ9 rank chain: {len(ranks9)} values ({ranks9[0]}…{ranks9[-1]}) | fibre sizes min {min(fib.values())} max {max(fib.values())} (at rank {max(fib, key=fib.get)}) | fibres {[fib[r] for r in ranks9]}')

O = {r2lib.src(c) for c in L9}; bysrc = defaultdict(list); S = set(L9)
for c in L9: bysrc[r2lib.src(c)].append(c)
def compose(a, b): return (a[0], a[1], a[2], min(a[3], b[3]), b[4], b[5], b[6], a[7], b[8])
pairs = 0; inside = 0; out = defaultdict(set); wout = Counter(); wsingle = 0
for a in L9:
    for b in bysrc.get(r2lib.tgt(a), ()):
        pairs += 1; c = compose(a, b); inside += c in S; out[(rk(a), rk(b))].add(rk(c))
for a in L9:
    for b in bysrc.get(r2lib.tgt(a), ()):
        if len(out[(rk(a), rk(b))]) == 1: wsingle += 1
single = sum(1 for v in out.values() if len(v) == 1); spread = max(len(v) for v in out.values()); worst = [k for k, v in out.items() if len(v) == spread]
crange = (min(min(v) for v in out.values()), max(max(v) for v in out.values()))
print(f'== L3015–3019 Λ9 composition: composable ordered pairs {pairs:,}, composites inside Λ9 {inside:,} | distinct (rank a, rank b) inputs {len(out)} | inputs determining a single output rank {single} = {100*single/len(out):.1f}% of {len(out)} | worst spread {spread} output ranks at input(s) {sorted(worst)} | composite ranks lie in [{crange[0]}, {crange[1]}]')
print(f'   the same share by pairs rather than inputs: {wsingle:,} of {pairs:,} composable pairs have a determined output rank = {100*wsingle/pairs:.1f}% | spread distribution over inputs {dict(sorted(Counter(len(v) for v in out.values()).items()))}')
print(f'   inputs whose output set is a full interval of ranks {sum(1 for v in out.values() if sorted(v) == list(range(min(v), max(v)+1)))} of {len(out)}')
