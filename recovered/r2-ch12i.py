# r2-ch12i.py — Phase R2 instrument for main §12.11.0.4 "The separation hypothesis, named" (chat 74).
# Runs beside tower-2.py (imported by path). Λ₉ from tower-2.py; Λ₉′ = Λ₉ ∩ {2S′ ≤ 2f+1} (§12.11.1 L3096).
# Measures on every cell / every pair: closure, factorisation over the transfer q, the sixteen-cell test
# 2S′ ⊥ f | g (MC L1306), conditional independence against graph separation for all 252 (pair | coordinate)
# triples on both indices, and the two cut claims of L2743–2746.
import importlib.util, os, itertools
from collections import Counter, defaultdict
import numpy as np
H = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('tower2', os.path.join(H, 'tower-2.py'))
T = importlib.util.module_from_spec(spec); spec.loader.exec_module(T)
NAMES = ['n', 'ℓ', 'k', 'q', 'e', 'f', 'g', '2S', '2S′']
SRC, TGT, Q = [0, 1, 2, 7], [4, 5, 6, 8], 3
EDGES9 = [(0, 1), (1, 2), (2, 3), (2, 7), (4, 5), (5, 6), (3, 6), (6, 8)]   # tower-2.py's bounds, one edge each
EDGES9P = EDGES9 + [(5, 8)]                                                  # + 2S′ ≤ 2f+1

def fmt(x): return f'{x:,}'

def closure(X):
    A = np.array(X, dtype=np.int64); n = len(A)
    rad = A.max(axis=0) + 1; w = np.cumprod(np.concatenate(([1], rad[:-1])))
    key = np.sort(A @ w)
    Ai, Aj = A[:, None, :], A[None, :, :]
    J = (np.maximum(Ai, Aj) @ w).ravel(); Mt = (np.minimum(Ai, Aj) @ w).ravel()
    jl = int((~np.isin(J, key)).sum()); ml = int((~np.isin(Mt, key)).sum())
    return n * n, jl, ml

def factor_q(X):
    A = defaultdict(set); B = defaultdict(set)
    for c in X:
        A[c[Q]].add(tuple(c[i] for i in SRC)); B[c[Q]].add(tuple(c[i] for i in TGT))
    return sum(len(A[v]) * len(B[v]) for v in A) - len(X)

def ci(X, a, b, c):
    """Exact (uniform-law) conditional independence a ⊥ b | c tested on every product cell (v, av, bv),
    av in the support of a given c=v, bv likewise: N(v,av,bv)·N(v) == N(v,av)·N(v,bv).
    Returns (product cells, cells failing the count test, cells with empty support)."""
    Nc, Na, Nb, Nab = Counter(), Counter(), Counter(), Counter()
    for x in X:
        Nc[x[c]] += 1; Na[(x[c], x[a])] += 1; Nb[(x[c], x[b])] += 1; Nab[(x[c], x[a], x[b])] += 1
    cells = fails = empty = 0
    for v in Nc:
        As = sorted(av for (vv, av) in Na if vv == v); Bs = sorted(bv for (vv, bv) in Nb if vv == v)
        for av in As:
            for bv in Bs:
                cells += 1
                if Nab[(v, av, bv)] * Nc[v] != Na[(v, av)] * Nb[(v, bv)]: fails += 1
                if Nab[(v, av, bv)] == 0: empty += 1
    return cells, fails, empty

def components(edges, removed, nodes=9):
    adj = defaultdict(set)
    for u, v in edges:
        if u not in removed and v not in removed: adj[u].add(v); adj[v].add(u)
    comp = {}
    for s in range(nodes):
        if s in removed or s in comp: continue
        stack = [s]; comp[s] = s
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if v not in comp: comp[v] = s; stack.append(v)
    return comp

def separates(edges, c, a, b):
    comp = components(edges, {c}); return comp[a] != comp[b]

L9 = T.L9(); L9p = [c for c in L9 if c[8] <= 2 * c[5] + 1]
removed = sorted(set(L9) - set(L9p))
print(f'|Λ9| {fmt(len(L9))} | Λ9′ = Λ9 ∩ {{2S′ ≤ 2f+1}}: {fmt(len(L9p))} cells | removed {len(removed)} | '
      f'removed (f, g, 2S′) values {sorted(set((c[5], c[6], c[8]) for c in removed))} | '
      f'ambient box 27,648: fill Λ9 {len(L9)/27648:.2%}, Λ9′ {len(L9p)/27648:.2%}')
for name, X in (('Λ9 (tree)', L9), ('Λ9′ (cycle)', L9p)):
    pairs, jl, ml = closure(X)
    print(f'{name}: closure on {fmt(pairs)} pairs — join leaves {jl}, meet leaves {ml}, E(X) = {jl + ml} | '
          f'factorisation over q, Σ_q|A_q||B_q| − |X| = {factor_q(X)} | '
          f'2S′ ⊥ f | g on product cells (cells, count-test failures, empty-support cells) = {ci(X, 8, 5, 6)}')
# the g = 2 slice, both texts of the test
for name, X in (('Λ9', L9), ('Λ9′', L9p)):
    sl = Counter((x[5], x[8]) for x in X if x[6] == 2)
    Nf = Counter(x[5] for x in X if x[6] == 2); Ns = Counter(x[8] for x in X if x[6] == 2); N = sum(sl.values())
    print(f'   {name} g = 2 slice: N = {N}, N(f) = {dict(sorted(Nf.items()))}, N(2S′) = {dict(sorted(Ns.items()))}, '
          f'N(f,2S′) = {dict(sorted(sl.items()))}, exact-CI cells failing = '
          f'{sum(1 for f in Nf for s in Ns if sl[(f, s)] * N != Nf[f] * Ns[s])} of {len(Nf) * len(Ns)}')
cells_per_g = {v: (len({x[5] for x in L9 if x[6] == v}), len({x[8] for x in L9 if x[6] == v})) for v in range(4)}
print('   product cells per g (|F_g|, |S_g|):', cells_per_g, '| total', sum(a * b for a, b in cells_per_g.values()))
# conditional independence against separation, all 252 triples, both indices
res = {}
for name, X, E in (('Λ9', L9, EDGES9), ('Λ9′', L9p, EDGES9P)):
    tab = Counter(); out = {}
    for c in range(9):
        for a, b in itertools.combinations([i for i in range(9) if i != c], 2):
            sep = separates(E, c, a, b); cells, fails, empty = ci(X, a, b, c)
            holds = fails == 0; tab[(sep, holds)] += 1; out[(a, b, c)] = (sep, holds, fails, cells)
    res[name] = out
    sf = [(NAMES[a], NAMES[b], NAMES[c], f, n) for (a, b, c), (sep, holds, f, n) in out.items() if sep and not holds]
    nh = [(NAMES[a], NAMES[b], NAMES[c]) for (a, b, c), (sep, holds, f, n) in out.items() if (not sep) and holds]
    print(f'{name}: triples {sum(tab.values())} | separated & CI holds {tab[(True, True)]} | separated & CI fails {tab[(True, False)]} '
          f'| not separated & CI fails {tab[(False, False)]} | not separated & CI holds {tab[(False, True)]}')
    print(f'   separated-but-fails (Markov failures): {sf}')
    print(f'   not-separated-but-holds (counterexamples to "exactly when"): {nh}')
chg = [(NAMES[a], NAMES[b], NAMES[c], res['Λ9'][(a, b, c)][1], res['Λ9′'][(a, b, c)][1], res['Λ9′'][(a, b, c)][2], res['Λ9′'][(a, b, c)][3])
       for (a, b, c) in res['Λ9'] if res['Λ9'][(a, b, c)][1] != res['Λ9′'][(a, b, c)][1]]
print('CI verdict changes Λ9 → Λ9′ (a, b, c, holds9, holds9′, fails9′, cells):', chg, '| cuts involved:', sorted({t[2] for t in chg}))
sepchg = [(NAMES[a], NAMES[b], NAMES[c]) for c in range(9) for a, b in itertools.combinations([i for i in range(9) if i != c], 2)
          if separates(EDGES9, c, a, b) != separates(EDGES9P, c, a, b)]
print('separation changes Λ9 → Λ9′ (graph only):', sepchg)
# the cut claims of L2743–2746
for name, E in (('Λ9', EDGES9), ('Λ9′', EDGES9P)):
    cq = components(E, {Q}); cg = components(E, {6})
    print(f'{name}: remove q → source {{n,ℓ,k,2S}} one component {len({cq[i] for i in SRC}) == 1}, target {{e,f,g,2S′}} one component {len({cq[i] for i in TGT}) == 1}, '
          f'source and target separated {len({cq[i] for i in SRC} | {cq[i] for i in TGT}) == 2} | remove g → f and 2S′ joined {cg[5] == cg[8]}')
tree_art = [NAMES[v] for v in range(9) if len(set(components(EDGES9, {v}).values())) > 1]
print('Λ9 tree articulation points:', tree_art, '| leaves:', [NAMES[v] for v in range(9) if sum(v in e for e in EDGES9) == 1])
