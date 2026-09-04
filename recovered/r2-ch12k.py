# r2-ch12k.py — Phase R2 instrument for main §12.11.0.7 "Why the arrows agree — a decay theorem" (chat 74).
# Runs beside tower-2.py (imported by path). The (g, G) index as r2-ch12g.py builds it: Λ₈ × {g ≤ G ≤ 4f+2} × {0 ≤ 2S′ ≤ G},
# 13,775 cells, coordinates (n, ℓ, k, q, e, f, g, 2S, G, 2S′). Arrows per §12.11.0.2 L2660, A_w = {w(tgt) ≤ w(src)}:
# shell e ≤ n, subshell f ≤ ℓ, occupancy G ≤ k, spin 2S′ ≤ 2S. Measured on every cell: the six overlaps
# P(A∩B)/P(A)P(B), the mutual informations under three readings (arrow indicators; source coordinates; (src, tgt) pairs),
# the Pinsker bound, the constraint graph, and the conditional independences the chain argument uses.
import importlib.util, os, itertools, math
from collections import Counter, defaultdict
H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('tower2', os.path.join(H, 'tower-2.py')); T = importlib.util.module_from_spec(s); s.loader.exec_module(T)
n_, l_, k_, q_, e_, f_, g_, S_, G_, Sp_ = range(10)
NAMES = ['n', 'ℓ', 'k', 'q', 'e', 'f', 'g', '2S', 'G', '2S′']
X = [c + (G, S2p) for c in T.L8() for G in range(c[g_], 4 * c[f_] + 2 + 1) for S2p in range(0, G + 1)]
N = len(X)
ARROWS = {'shell': (n_, e_), 'subshell': (l_, f_), 'occupancy': (k_, G_), 'spin': (S_, Sp_)}   # (source coord, target coord)
ind = {w: [1 if c[t] <= c[sc] else 0 for c in X] for w, (sc, t) in ARROWS.items()}
DIST = {('shell', 'subshell'): 1, ('subshell', 'occupancy'): 1, ('occupancy', 'spin'): 1, ('subshell', 'spin'): 2, ('shell', 'occupancy'): 2, ('shell', 'spin'): 3}

def mi(xs, ys):
    cx, cy, cxy = Counter(xs), Counter(ys), Counter(zip(xs, ys))
    return sum(v / N * math.log2(v * N / (cx[x] * cy[y])) for (x, y), v in cxy.items())

print(f'(g, G) index: {N:,} cells | arrows |A_w|: ' + ', '.join(f'{w} {sum(v):,}' for w, v in ind.items()))
print('pair                    d   overlap P(A∩B)/P(A)P(B)   |P(A∩B)−P(A)P(B)|   I(A_u;A_v) bits   Pinsker √(I ln2/2)   I(u;v) source coords   I((u,u′);(v,v′))')
rows = []
for (u, v), d in DIST.items():
    pa, pb = sum(ind[u]) / N, sum(ind[v]) / N; pab = sum(a & b for a, b in zip(ind[u], ind[v])) / N
    ov = pab / (pa * pb); dev = abs(pab - pa * pb); iab = mi(ind[u], ind[v]); pins = math.sqrt(iab * math.log(2) / 2)
    su, sv = ARROWS[u][0], ARROWS[v][0]
    icoord = mi([c[su] for c in X], [c[sv] for c in X])
    ipair = mi([(c[ARROWS[u][0]], c[ARROWS[u][1]]) for c in X], [(c[ARROWS[v][0]], c[ARROWS[v][1]]) for c in X])
    rows.append((u, v, d, ov, dev, iab, pins, icoord, ipair))
    print(f'{u} ∩ {v:<12} {d}   {ov:.3f}                      {dev:.4f}              {iab:.3f}             {pins:.3f}                {icoord:.3f}                  {ipair:.3f}')
ovs = [r[3] for r in sorted(rows, key=lambda r: r[2])]
print(f'overlaps in distance order {[round(o, 3) for o in ovs]} | strictly decreasing with distance {all(ovs[i] > ovs[i+1] for i in range(len(ovs)-1))} | '
      f'no overlap between distance classes {max(r[3] for r in rows if r[2] == 2) < min(r[3] for r in rows if r[2] == 1) and max(r[3] for r in rows if r[2] == 3) < min(r[3] for r in rows if r[2] == 2)} | '
      f'Pinsker holds for every pair {all(r[4] <= r[6] for r in rows)}')
for col, name in ((5, 'I(A_u;A_v)'), (7, 'I(u;v) source coordinates'), (8, 'I((u,u′);(v,v′))')):
    vals = [r[col] for r in sorted(rows, key=lambda r: r[2])]
    print(f'{name} in distance order {[round(x, 3) for x in vals]} | strictly decreasing {all(vals[i] > vals[i+1] for i in range(len(vals)-1))}')
# the constraint graph of the (g, G) index, by construction
EDGES = [(n_, l_), (l_, k_), (k_, q_), (k_, S_), (e_, f_), (f_, g_), (q_, g_), (g_, G_), (f_, G_), (G_, Sp_)]
print(f'constraint graph: {len(set(sum(EDGES, ())))} nodes, {len(EDGES)} edges (one bound each: ℓ≤min(1,n−1), k≤min(3,4ℓ+2), q≤k, 2S≤k, f≤min(1,e−1), g≤min(4f+2,q), g≤G, G≤4f+2, 2S′≤G) — a tree: {len(EDGES) == len(set(sum(EDGES, ()))) - 1}; cycle: f–g–G–f')

def ci_sets(A, B, C):
    """exact conditional independence of coordinate sets A ⊥ B | C on every product cell of every C-fibre"""
    Nc, Na, Nb, Nab = Counter(), Counter(), Counter(), Counter()
    for x in X:
        a, b, c = tuple(x[i] for i in A), tuple(x[i] for i in B), tuple(x[i] for i in C)
        Nc[c] += 1; Na[(c, a)] += 1; Nb[(c, b)] += 1; Nab[(c, a, b)] += 1
    cells = fails = 0
    byc = defaultdict(lambda: (set(), set()))
    for (c, a) in Na: byc[c][0].add(a)
    for (c, b) in Nb: byc[c][1].add(b)
    for c, (As, Bs) in byc.items():
        for a in As:
            for b in Bs:
                cells += 1
                if Nab[(c, a, b)] * Nc[c] != Na[(c, a)] * Nb[(c, b)]: fails += 1
    return cells, fails
tests = [('(n,e) ⊥ rest-of-chain (k,G,2S,2S′) | (ℓ,f)', [n_, e_], [k_, G_, S_, Sp_], [l_, f_]),
         ('(n,e,ℓ,f) ⊥ (2S,2S′) | (k,G)', [n_, e_, l_, f_], [S_, Sp_], [k_, G_]),
         ('(n,e) ⊥ (2S,2S′) | (k,G)', [n_, e_], [S_, Sp_], [k_, G_]),
         ('source chain n ⊥ 2S | k', [n_], [S_], [k_]), ('n ⊥ k | ℓ', [n_], [k_], [l_]), ('ℓ ⊥ 2S | k', [l_], [S_], [k_]),
         ('across the cycle: f ⊥ G | g (not separated)', [f_], [G_], [g_]), ('g ⊥ 2S′ | G (separated)', [g_], [Sp_], [G_]),
         ('arrow indicators: A_shell ⊥ A_spin | A_occupancy', None, None, None)]
for label, A, B, C in tests:
    if A is None:
        # indicator chain: condition on the occupancy indicator, not the coordinates
        Nc, Na, Nb, Nab = Counter(), Counter(), Counter(), Counter()
        for a, b, c in zip(ind['shell'], ind['spin'], ind['occupancy']): Nc[c] += 1; Na[(c, a)] += 1; Nb[(c, b)] += 1; Nab[(c, a, b)] += 1
        fails = sum(1 for (c, a, b), v in Nab.items() if v * Nc[c] != Na[(c, a)] * Nb[(c, b)])
        print(f'{label}: product cells {sum(1 for _ in Nab)}, exact-CI failures {fails}')
    else:
        cells, fails = ci_sets(A, B, C); print(f'{label}: product cells {cells:,}, exact-CI failures {fails:,} → {"holds" if fails == 0 else "fails"}')
M = open(os.path.join(H, 'The_Method_1_6-2.md'), encoding='utf-8').read().split('\n')
print('tower table L2932–2956 rows carrying a cycle or 13,775:', [(i, M[i-1][:60]) for i in range(2932, 2957) if 'cycle' in M[i-1] or '13,775' in M[i-1] or 'Λ₉′' in M[i-1]])
