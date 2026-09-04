# r2-ch12n.py — Phase R2, main §12.11.0.10 "Every Λ in one table" (L2932–2956), chat 75.
# Every row of the tower table re-measured from tower-2.py (by path, through r2lib): cells, ambient box (product of realised
# coordinate ranges), fill, closure E, composition; then the fill's monotonicity, the box-versus-object ratios, and §11.1.1's
# surplus (bits carried = |J(Λ_d)| = lattice length, minus log2 cells) at every stage. Closure: pairwise on every ordered pair
# for Λ₈, Λ₉, Λ₉′, Λ₁₀, Λ₁₁ (r2lib.closure's semantics, chunked); for Λ₁₂ and Λ₁₃ the exact fibre-interval criterion, measured
# on ALL cells: each stage is Λ_{d−1} fibred by an interval [lo, hi] of the new coordinate whose bounds depend on one earlier
# coordinate u (verified on every cell), and given Λ_{d−1} closed, Λ_d is closed iff for every realised pair (u, u′):
# lo(max) ≤ max(lo u, lo u′), max(hi u, hi u′) ≤ hi(max), lo(min) ≤ min(lo u, lo u′), min(hi u, hi u′) ≤ hi(min). Deterministic.
import importlib.util, os, math
from collections import defaultdict
import numpy as np
H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py')); r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib); T = r2lib.load_tower()

def closure_chunked(X, chunk=100):
    A = np.array(X, dtype=np.int64); n = len(A); base = A.min(axis=0); rad = A.max(axis=0) - base + 1
    w = np.cumprod(np.concatenate(([1], rad[:-1]))); key = np.sort((A - base) @ w); jl = ml = 0
    for i in range(0, n, chunk):
        Ai = A[i:i+chunk, None, :]; Aj = A[None, :, :]
        J = ((np.maximum(Ai, Aj) - base) @ w).ravel(); Mt = ((np.minimum(Ai, Aj) - base) @ w).ravel()
        jl += int((~np.isin(J, key)).sum()); ml += int((~np.isin(Mt, key)).sum())
    return n * n, jl, ml

def box(X):
    A = np.array(X); return int(np.prod(A.max(axis=0) - A.min(axis=0) + 1))

def length(X):
    """lattice length by a greedy maximal chain (each step to a minimal-sum cell above the current one is a cover); = |J(L)| for a finite distributive lattice."""
    A = np.array(X, dtype=np.int64); x = A.min(axis=0); assert (A == x).all(axis=1).any(), 'bottom cell missing'
    steps = 0
    while True:
        m = (A >= x).all(axis=1) & (A != x).any(axis=1)
        if not m.any(): return steps
        C = A[m]; x = C[np.argmin(C.sum(axis=1))]; steps += 1

def fibre_check(Xd, u_idx, lo, hi):
    """verify on every cell that the last coordinate's fibre over each prefix is exactly [lo(u), hi(u)] with u the prefix's coordinate u_idx; return (prefixes, fibres wrong, realised u-values)."""
    A = np.array(Xd, dtype=np.int64); pref = A[:, :-1]; last = A[:, -1]
    order = np.lexsort(pref.T[::-1]); pref, last = pref[order], last[order]
    cut = np.concatenate(([True], (pref[1:] != pref[:-1]).any(axis=1)))
    starts = np.flatnonzero(cut); ends = np.concatenate((starts[1:], [len(A)]))
    wrong = 0; us = set()
    for a, b in zip(starts, ends):
        u = int(pref[a, u_idx]); us.add(u); vals = last[a:b]
        if not (vals.min() == lo(u) and vals.max() == hi(u) and b - a == hi(u) - lo(u) + 1 and len(set(vals.tolist())) == b - a): wrong += 1
    return len(starts), wrong, sorted(us)

def criterion(us, lo, hi):
    bad = 0
    for u in us:
        for v in us:
            mx, mn = max(u, v), min(u, v)
            if not (lo(mx) <= max(lo(u), lo(v)) and max(hi(u), hi(v)) <= hi(mx) and lo(mn) <= min(lo(u), lo(v)) and min(hi(u), hi(v)) <= hi(mn)): bad += 1
    return len(us) ** 2, bad

rows = [('Λ8', T.L8()), ('Λ9', T.L9()), ("Λ9′", r2lib.lam9p(T.L9())), ('Λ10', T.L10()), ('Λ11', T.L11()), ('Λ12', T.L12()), ('Λ13', T.L13())]
print('== L2935–2942 the table, recomputed (cells, dim, ambient box = Π(max−min+1), fill, closure)')
fills = {}; cells = {}; boxes = {}
for name, X in rows:
    d = len(X[0]); b = box(X); fills[name] = 100 * len(X) / b; cells[name] = len(X); boxes[name] = b
    if len(X) <= 14000:
        p, jl, ml = closure_chunked(X); clo = f'pairwise on all {p:,} ordered pairs: join fail {jl}, meet fail {ml}, E = {jl+ml}'
    else: clo = 'closure by the fibre criterion (below)'
    print(f'   {name:4s} dim {d:2d} cells {len(X):>7,} box {b:>10,} fill {fills[name]:.2f}% | {clo}')
# fibre criterion for Λ12 (2K ∈ [0, 2J_c + 2·f_max], u = 2J_c at index 10) and Λ13 (2J ∈ [max(0, 2K−1), 2K+1], u = 2K at index 11)
for name, X, u_idx, lo, hi, desc in (('Λ12', T.L12(), 10, lambda u: 0, lambda u: u + 2 * T.FMAX, '2K ∈ [0, 2J_c + 2·f_max]'), ('Λ13', T.L13(), 11, lambda u: max(0, u - 1), lambda u: u + 1, '2J ∈ [max(0, 2K − 1), 2K + 1]')):
    npre, wrong, us = fibre_check(X, u_idx, lo, hi); tests, bad = criterion(us, lo, hi)
    print(f'   {name}: fibre {desc} verified on every cell — {npre:,} prefixes (= |Λ{int(name[1:])-1}|), fibres not the printed interval {wrong} | realised u-values {us} | criterion on all {tests} value pairs: violations {bad} → E = 0 given the previous stage closed')
print(f'   f_max = {T.FMAX}, φ̂ = {T.PHI} (tower-2.py)')

# ---- composition column ----
print('== composition (r2-ch12e/f: a→b when the target tuple of a equals the source tuple (n,ℓ,k,2S) of b)')
for name, X in rows:
    src = {tuple(c[i] for i in (0, 1, 2, 7)) for c in X}; tgt_idx = (4, 5, 6) if len(X[0]) == 8 else tuple([4, 5, 6] + list(range(8, len(X[0]))))
    tg = {tuple(c[i] for i in tgt_idx) for c in X}
    if len(tgt_idx) != 4: print(f'   {name}: source tuple 4 coordinates, target tuple {len(tgt_idx)} — no target is a source; does not compose'); continue
    comp = [c for c in X if tuple(c[i] for i in tgt_idx) in src]
    S = set(X); ok = 0; tot = 0
    bysrc = defaultdict(list)
    for c in X: bysrc[tuple(c[i] for i in (0, 1, 2, 7))].append(c)
    for a in comp:
        for b in bysrc[tuple(a[i] for i in tgt_idx)]:
            tot += 1; ok += (a[0], a[1], a[2], min(a[3], b[3]), b[4], b[5], b[6], a[7], b[8]) in S
    print(f'   {name}: composable cells {len(comp):,} of {len(X):,} | composable ordered pairs {tot:,}, composites inside the index {ok:,} | composes: {len(comp) > 0 and ok == tot}')

# ---- L2948–2951 fill monotone; box vs object ratios; §11.1.1's surplus ----
main = ['Λ8', 'Λ9', 'Λ10', 'Λ11', 'Λ12', 'Λ13']
print(f'== L2948 fill along the main tower {[round(fills[n], 2) for n in main]} monotone decreasing: {all(fills[main[i]] > fills[main[i+1]] for i in range(5))} | Λ9′ row {fills["Λ9′"]:.2f}% below Λ9')
print('   box ratio vs object ratio per step: ' + ' | '.join(f'{main[i]}→{main[i+1]} box ×{boxes[main[i+1]]/boxes[main[i]]:.2f} cells ×{cells[main[i+1]]/cells[main[i]]:.3f} {"box faster" if boxes[main[i+1]]/boxes[main[i]] > cells[main[i+1]]/cells[main[i]] else "OBJECT faster"}' for i in range(5)))
print('== L2949 §11.1.1 surplus = bits carried (|J(Λ_d)| = lattice length) − bits to index the cells (log2 cells); and the box surplus log2(box/cells)')
prev = None
for name, X in rows:
    J = length(X); idx = math.log2(len(X)); sur = J - idx; bsur = math.log2(boxes[name] / len(X))
    print(f'   {name:4s} |J| {J:2d} | log2 cells {idx:5.2f} | §11.1.1 surplus {sur:5.2f} bits per cell | box surplus {bsur:4.2f} bits' + (f' | grows from {prev[0]}: §11.1.1 {sur > prev[1]}, box {bsur > prev[2]}' if prev and name != "Λ9′" else ''))
    if name != 'Λ9′': prev = (name, sur, bsur)
