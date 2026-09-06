# r2-ch12o.py — Phase R2, main §12.11.0.11 "The fourteenth axis, and what can be said about it from inside" (L2957–2998), chat 75.
# The table's bits columns (bits carried = log2 ambient box, needed = log2 cells, surplus = difference), the stage-to-stage fill
# ratios, the law of L2971–2973 (a constrained coordinate's mean multiplicity is strictly below its value count) measured on every
# stage, and Λ₈'s two "surpluses" (box: log2 6,912 − log2 976; generator: |J(Λ₈)| − log2 976) for L2997. tower-2.py by path via r2lib.
import importlib.util, os, math
import numpy as np
H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py')); r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib); T = r2lib.load_tower()

stages = [(d, T.STAGES[d]()) for d in range(8, 14)]
print('== L2962–2968 the table (box = Π(max−min+1) over realised ranges; bits carried = log2 box; needed = log2 cells; surplus = carried − needed)')
fill = {}; rows = {}
for d, X in stages:
    A = np.array(X); b = int(np.prod(A.max(axis=0) - A.min(axis=0) + 1)); fill[d] = 100 * len(X) / b
    rows[d] = (len(X), b, math.log2(b), math.log2(len(X)))
    print(f'   D {d:2d} cells {len(X):>7,} box {b:>10,} fill {fill[d]:.2f}% bits carried {math.log2(b):.2f} needed {math.log2(len(X)):.2f} surplus {math.log2(b) - math.log2(len(X)):.2f}')
ds = list(range(8, 14))
print(f'== L2970 fill falls at every step: {all(fill[d] > fill[d+1] for d in ds[:-1])} | surplus rises at every step: {all(rows[d][2]-rows[d][3] < rows[d+1][2]-rows[d+1][3] for d in ds[:-1])}')
ratios = [fill[d+1] / fill[d] for d in ds[:-1]]
print(f'== L2979–2980 ratios stage to stage {[round(r, 3) for r in ratios]} | monotone: {all(ratios[i] > ratios[i+1] for i in range(4)) or all(ratios[i] < ratios[i+1] for i in range(4))} | limit in [0, {fill[13]:.2f}%] (fill 13 = {fill[13]:.4f}%)')
print('== L2971–2973 the law: new axis, its value count (box multiplier), mean multiplicity (cells ratio), strictly below the value count')
for d, X in stages[1:]:
    prev = dict(stages)[d-1]; vals = sorted({c[-1] for c in X}); mult = len(X) / len(prev)
    full = sum(1 for _ in ()) ; 
    # fibre sizes over the previous stage's cells
    from collections import Counter
    fib = Counter(tuple(c[:-1]) for c in X); sizes = sorted(set(fib.values()))
    print(f'   D {d}: new coordinate values {len(vals)} ({vals[0]}…{vals[-1]}) | mean multiplicity {mult:.3f} | fibre sizes {sizes} | free (every fibre the full value set): {sizes == [len(vals)]} | mean multiplicity < value count: {mult < len(vals)}')

def length(X):
    A = np.array(X, dtype=np.int64); x = A.min(axis=0); assert (A == x).all(axis=1).any(); steps = 0
    while True:
        m = (A >= x).all(axis=1) & (A != x).any(axis=1)
        if not m.any(): return steps
        C = A[m]; x = C[np.argmin(C.sum(axis=1))]; steps += 1
J8 = length(T.L8())
print(f'== L2997 Λ8: |J(Λ8)| {J8} | generator surplus (§11.1.1) {J8} − {math.log2(976):.2f} = {J8 - math.log2(976):.2f} bits | box surplus (this table, D = 8) {math.log2(6912) - math.log2(976):.2f} bits | the two differ by {J8 - math.log2(6912):.2f} bits (17 generators against log2 6,912 = {math.log2(6912):.2f} box bits)')
print('== L2992–2994 the empty index: pairs 0, failing joins 0, failing meets 0, E(∅) = 0; Q(∅) = ∅ so COMPLETE by P19 (L381: COMPLETE ⟺ Q = ∅); join-irreducibles 0; bits log2 |∅| undefined, carried 0 — definitional, no cell enumerated')
