# r2-ch12m.py — Phase R2, main §12.11.0.9 "Two indices, and the one that does not exist" (L2898–2931), chat 75.
# Reversal rev(Λ₉) = exchange of the two ends (n,ℓ,k,2S) ↔ (e,f,g,2S′), transfer fixed; the four positions of the printed table
# (forward, backward, intersection, union) with closure counted on ALL ordered pairs (chunked; same semantics as r2lib.closure)
# and E by iterated join-and-meet to a fixed point (MC L1336's definition); the intersection's g = q = k, factorisation over q,
# groupoid structure under r2-ch12e's composition; the sign extension of L2899–2901 under the tower's own ranges. Deterministic.
import importlib.util, os, itertools
from collections import Counter, defaultdict
import numpy as np
H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py')); r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib); T = r2lib.load_tower()

L9 = T.L9(); S9 = set(L9)
rev = lambda c: (c[4], c[5], c[6], c[3], c[0], c[1], c[2], c[8], c[7])          # (e,f,g,q,n,ℓ,k,2S′,2S) in Λ₉'s coordinate slots
R9 = [rev(c) for c in L9]; SR = set(R9)
I = sorted(S9 & SR); U = sorted(S9 | SR)

def closure_chunked(X, chunk=200):
    """r2lib.closure's semantics — ordered pairs (i, j) over X, joins and meets outside X — in chunks; returns (pairs, join fails, meet fails)."""
    A = np.array(X, dtype=np.int64); n = len(A); rad = A.max(axis=0) - A.min(axis=0) + 1; base = A.min(axis=0)
    w = np.cumprod(np.concatenate(([1], rad[:-1]))); key = np.sort((A - base) @ w)
    jl = ml = 0
    for i in range(0, n, chunk):
        Ai = A[i:i+chunk, None, :]; Aj = A[None, :, :]
        J = ((np.maximum(Ai, Aj) - base) @ w).ravel(); Mt = ((np.minimum(Ai, Aj) - base) @ w).ravel()
        jl += int((~np.isin(J, key)).sum()); ml += int((~np.isin(Mt, key)).sum())
    return n * n, jl, ml

def fixed_point(X, chunk=200):
    """iterated join-and-meet closure to a fixed point; returns (cells added, iterations, final size)."""
    cur = {tuple(map(int, c)) for c in X}; new = sorted(cur); it = 0
    while new:
        it += 1
        A = np.array(sorted(cur), dtype=np.int64); B = np.array(new, dtype=np.int64); found = set()
        for i in range(0, len(B), chunk):
            Bi = B[i:i+chunk, None, :]; Aj = A[None, :, :]
            for Z in (np.maximum(Bi, Aj), np.minimum(Bi, Aj)):
                for row in np.unique(Z.reshape(-1, Z.shape[-1]), axis=0): found.add(tuple(map(int, row)))
        new = sorted(found - cur); cur |= found
    return len(cur) - len(X), it, len(cur)

print(f'|Λ9| {len(L9):,} | rev(Λ9) {len(SR):,} cells | rev(Λ9) = Λ9: {SR == S9} | rev is an involution on cells: {all(rev(rev(c)) == c for c in L9)} | Λ9 ∩ rev(Λ9) {len(I)} | Λ9 ∪ rev(Λ9) {len(U):,} (= 2·1,654 − {len(I)}: {len(U) == 2*len(L9) - len(I)})')
# semantics check of the chunked closure against r2lib.closure on the intersection (small)
print(f'chunked closure = r2lib.closure on the intersection: {closure_chunked(I) == r2lib.closure(I)}')
print('== L2906–2910 the table (pairs = cells², join fail, meet fail on all ordered pairs; E = cells added by iterated closure to a fixed point)')
for name, X in (('Λ9, forward', L9), ('rev(Λ9), backward', R9), ('Λ9 ∩ rev(Λ9)', I), ('Λ9 ∪ rev(Λ9)', U)):
    p, jl, ml = closure_chunked(X); E, it, size = fixed_point(X)
    print(f'   {name:20s} cells {len(X):>5,} | pairs {p:>9,} | join fail {jl:>7,} | meet fail {ml:>7,} | failing pairs {jl+ml:>7,} | E (cells added to close) {E:,} in {it} iteration(s), closure size {size:,}')
# one-step count of distinct missing elements, for comparison with the fixed-point E
A = np.array(U, dtype=np.int64); base = A.min(axis=0); rad = A.max(axis=0) - base + 1; w = np.cumprod(np.concatenate(([1], rad[:-1]))); key = set(((A - base) @ w).tolist())
miss = set()
for i in range(0, len(A), 200):
    Ai = A[i:i+200, None, :]; Aj = A[None, :, :]
    for Z in (np.maximum(Ai, Aj), np.minimum(Ai, Aj)): miss |= set(((Z - base) @ w).ravel().tolist()) - key
print(f'   union: distinct missing joins/meets after ONE step {len(miss):,} (the fixed-point E above is the iterated count)')

# ---- L2915–2921 the intersection ----
gqk = sum(1 for c in I if c[6] == c[3] == c[2])
print(f'== L2915 intersection cells with g = q = k: {gqk} of {len(I)} | cells of Λ9 with g = q = k: {sum(1 for c in L9 if c[6]==c[3]==c[2])} | 389/1,654 = {100*len(I)/len(L9):.1f}%')
O = {r2lib.src(c) for c in L9}; comp = [c for c in L9 if r2lib.tgt(c) in O]
edges = defaultdict(int)
for c in comp: edges[(r2lib.src(c), r2lib.tgt(c))] += 1
withrev = [c for c in comp if (r2lib.tgt(c), r2lib.src(c)) in edges]
adj = defaultdict(list)
for (a, b) in edges: adj[a].append(b)
sccs = r2lib.tarjan(sorted(O), adj); cid = {o: i for i, cp in enumerate(sccs) for o in cp}
cyc = [c for c in comp if cid[r2lib.src(c)] == cid[r2lib.tgt(c)]]
print(f'   morphisms carrying a reverse (cells whose (src, tgt) object pair has the reverse edge) {len(withrev)} | = intersection: {set(withrev) == set(I)} | = r2-ch12f\'s cycle cells: {set(cyc) == set(I)} | conservative (g = q) on every cycle cell {all(c[6]==c[3] for c in cyc)}, level set (k = g) on every cycle cell {all(c[2]==c[6] for c in cyc)}')
print(f'   factorisation over q of the intersection: Σ_q|A_q||B_q| − |I| = {r2lib.factor_q(I)} | closure (r2lib): {r2lib.closure(I)}')
# groupoid under r2-ch12e's composition: b∘a when tgt(a) = src(b), composite = (src(a), q = min(q_a, q_b), tgt(b))
def compose(a, b): return (a[0], a[1], a[2], min(a[3], b[3]), b[4], b[5], b[6], a[7], b[8])
SI = set(I); objsI = {r2lib.src(c) for c in I} | {r2lib.tgt(c) for c in I}
ident = {o: (o[0], o[1], o[2], o[2], o[0], o[1], o[2], o[3], o[3]) for o in objsI}
has_id = sum(1 for o in objsI if ident[o] in SI and r2lib.src(ident[o]) == r2lib.tgt(ident[o]) == o)
inv_ok = sum(1 for c in I if rev(c) in SI and r2lib.src(rev(c)) == r2lib.tgt(c) and r2lib.tgt(rev(c)) == r2lib.src(c) and compose(c, rev(c)) == ident[r2lib.src(c)] and compose(rev(c), c) == ident[r2lib.tgt(c)])
pairs = [(a, b) for a in I for b in I if r2lib.tgt(a) == r2lib.src(b)]
closed_comp = sum(1 for a, b in pairs if compose(a, b) in SI)
assoc = all(compose(compose(a, b), c) == compose(a, compose(b, c)) for a, b in pairs for c in I if r2lib.tgt(b) == r2lib.src(c))
print(f'   groupoid: objects {len(objsI)} (all 33 source objects: {objsI == O}) | objects carrying an identity cell in I {has_id} | cells with a two-sided inverse in I (rev(c), both composites identities) {inv_ok} of {len(I)} | composable pairs in I {len(pairs):,}, composites in I {closed_comp:,} | associative {assoc}')
print(f'   identity cells of Λ9 (src = tgt) {sum(1 for c in L9 if r2lib.src(c)==r2lib.tgt(c))}, all in I: {all(c in SI for c in L9 if r2lib.src(c)==r2lib.tgt(c))}')

# ---- L2912–2913 §11.8's self-duality: the order dual σ(x) = max − x against the end-exchange ----
mx = tuple(max(c[i] for c in L9) for i in range(9)); mn = tuple(min(c[i] for c in L9) for i in range(9))
sig = {tuple(mx[i] + mn[i] - c[i] for i in range(9)) for c in L9}
print(f'== L2912–2913 §11.8: σ(Λ9) (coordinatewise max+min−x) = Λ9: {sig == S9} | σ(Λ9) = rev(Λ9): {sig == SR} | rev(Λ9) ∩ σ(Λ9) {len(SR & sig)} | Λ9 self-dual under σ: {sig == S9}')

# ---- L2899–2901 the sign extension: k, q, g below zero under the tower's own ranges ----
def build(low):
    out = []
    for n in range(1, 4):
      for l in range(0, min(1, n-1)+1):
        for k in range(low, min(3, 4*l+2)+1):
          for q in range(low, k+1):
            for e in range(1, 4):
              for f in range(0, min(1, e-1)+1):
                for g in range(low, min(4*f+2, q)+1):
                  for S2 in range(0, k+1):
                    for S2p in range(0, g+1):
                      out.append((n, l, k, q, e, f, g, S2, S2p))
    return out
for low in (1, 0, -1, -3):
    X = build(low); neg = sum(1 for c in X if min(c[2], c[3], c[6]) < 0)
    p, jl, ml = closure_chunked(X); raising = sum(1 for c in X if c[6] > c[2])
    print(f'== L2899–2901 lower bound {low:>2} on k, q, g (2S ∈ [0,k], 2S′ ∈ [0,g] as printed): cells {len(X):,} | with k, q or g < 0: {neg} | closure join fail {jl} meet fail {ml} | steps raising k (g > k) {raising}')
# the one reading that admits negative cells: spin bounded by |k| and |g|
def build_abs(low):
    out = []
    for n in range(1, 4):
      for l in range(0, min(1, n-1)+1):
        for k in range(low, min(3, 4*l+2)+1):
          for q in range(low, k+1):
            for e in range(1, 4):
              for f in range(0, min(1, e-1)+1):
                for g in range(low, min(4*f+2, q)+1):
                  for S2 in range(0, abs(k)+1):
                    for S2p in range(0, abs(g)+1):
                      out.append((n, l, k, q, e, f, g, S2, S2p))
    return out
for low in (-1, -2):
    X = build_abs(low); neg = sum(1 for c in X if min(c[2], c[3], c[6]) < 0)
    p, jl, ml = closure_chunked(X); raising = sum(1 for c in X if c[6] > c[2])
    print(f'   reading with 2S ∈ [0,|k|], 2S′ ∈ [0,|g|], lower bound {low}: cells {len(X):,} | negative cells {neg:,} | closure join fail {jl:,} meet fail {ml:,} | steps raising k {raising}')
