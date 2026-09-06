# r2-ch12j.py — Phase R2 instrument for main §12.11.0.5 (Q item O) and §12.11.0.6 (Q item K) (chat 74).
# Runs beside tower-2.py and r2-ch12i.py (imported by path). Propagated bounds φ̂(b | a) = max b on the cells with a = v,
# direct and composed through an intermediate c (max over c-values compatible with a of φ̂(b | c)); tested on every
# cell of Λ₉ and Λ₉′, for the printed pair and for every (ordered pair, separator) composition of each index.
# Item K: the largest physical 2J_c at k = 1, 2, 3 enumerated from antisymmetric microstates of ℓ ≤ 1 shells.
import importlib.util, os, itertools
from collections import defaultdict
H = os.path.dirname(os.path.abspath(__file__))
def load(name, fn):
    s = importlib.util.spec_from_file_location(name, os.path.join(H, fn)); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
T = load('tower2', 'tower-2.py')
I = load('r2ch12i', 'r2-ch12i.py') if False else None   # r2-ch12i prints on import; its graph is restated here
NAMES = ['n', 'ℓ', 'k', 'q', 'e', 'f', 'g', '2S', '2S′']
EDGES9 = [(0, 1), (1, 2), (2, 3), (2, 7), (4, 5), (5, 6), (3, 6), (6, 8)]; EDGES9P = EDGES9 + [(5, 8)]
L9 = T.L9(); L9p = [c for c in L9 if c[8] <= 2 * c[5] + 1]

def support(X, i): return sorted({x[i] for x in X})
def direct(X, b, a, agg=max):
    d = defaultdict(list)
    for x in X: d[x[a]].append(x[b])
    return {v: agg(vals) for v, vals in sorted(d.items())}
def composed(X, b, a, c, agg=max):
    ca = defaultdict(set)
    for x in X: ca[x[a]].add(x[c])
    dc = direct(X, b, c, agg)
    return {v: agg(dc[w] for w in ws) for v, ws in sorted(ca.items())}
def components(edges, removed):
    adj = defaultdict(set)
    for u, v in edges:
        if u not in removed and v not in removed: adj[u].add(v); adj[v].add(u)
    comp = {}
    for s in range(9):
        if s in removed or s in comp: continue
        st = [s]; comp[s] = s
        while st:
            u = st.pop()
            for v in adj[u]:
                if v not in comp: comp[v] = s; st.append(v)
    return comp
def separates(edges, c, a, b): cp = components(edges, {c}); return cp[a] != cp[b]

print('== §12.11.0.5 the printed table (2S′ from f, composed through g)')
for name, X in (('Λ9 (tree)', L9), ('Λ9′ (cycle)', L9p)):
    dd, cc = direct(X, 8, 5), composed(X, 8, 5, 6)
    print(f'{name}: |X| {len(X):,} | direct φ̂(2S′|f) {dd} | composed through g {cc} | '
          f'{"agree" if dd == cc else "disagree at f = " + str([v for v in dd if dd[v] != cc[v]])}')
    rd, rc = direct(X, 5, 8), composed(X, 5, 8, 6)
    ld, lc = direct(X, 5, 8, min), composed(X, 5, 8, 6, min)
    print(f'   reverse, f from 2S′: direct φ̂(f|2S′) {rd} | composed through g {rc} | {"agree" if rd == rc else "disagree"}'
          f' || lower bounds (min f | 2S′): direct {ld} | composed {lc} | {"agree" if ld == lc else "disagree at 2S′ = " + str([v for v in ld if ld[v] != lc[v]])}')
print('== path-independence: every ordered pair (a → b) composed through every coordinate c that separates a from b')
for name, X, E in (('Λ9', L9, EDGES9), ('Λ9′', L9p, EDGES9P)):
    tests = agree = 0; bad = []
    for a, b in itertools.permutations(range(9), 2):
        for c in range(9):
            if c in (a, b) or not separates(E, c, a, b): continue
            tests += 1
            if direct(X, b, a) == composed(X, b, a, c): agree += 1
            else: bad.append((NAMES[b], NAMES[a], NAMES[c]))
    nonsep = sum(1 for a, b in itertools.permutations(range(9), 2) for c in range(9) if c not in (a, b) and not separates(E, c, a, b) and direct(X, b, a) != composed(X, b, a, c))
    print(f'{name}: separator compositions {tests}, direct = composed in {agree}, disagreements {bad} | non-separator compositions that disagree {nonsep}')
    # the printed composition on the cycle: f → g → 2S′ (g does not separate f from 2S′ in Λ9′)
    print(f'   g separates f from 2S′: {separates(E, 6, 5, 8)}; direct φ̂(2S′|f) vs through g: {direct(X, 8, 5)} vs {composed(X, 8, 5, 6)}; through f for e → 2S′: {direct(X, 8, 4)} vs {composed(X, 8, 4, 5)}, through g: {composed(X, 8, 4, 6)}')
print('== §12.11.0.6 item K: physical maxima of 2J_c from microstates (ℓ ≤ 1, k = 1..3), φ̂ and 2J_c ≤ k')
phys = {}
for k in (1, 2, 3):
    best = None
    for l in (0, 1):
        orbs = [(ml, ms) for ml in range(-l, l + 1) for ms in (-1, 1)]     # ms in halves
        for sub in itertools.combinations(orbs, k):
            mj2 = sum(2 * ml + ms for ml, ms in sub)                        # 2·M_J = Σ(2 m_l + 2 m_s)
            best = mj2 if best is None else max(best, mj2)
    phys[k] = best
L11 = T.L11(); realised = {k: max(c[10] for c in L11 if c[2] == k) for k in (1, 2, 3)}
print(f'largest physical 2J_c (max 2M_J over antisymmetric microstates of s and p shells) {phys} | φ̂ (tower-2.py PHI) {T.PHI} | '
      f'realised maxima of 2J_c in Λ11 by occupancy {realised} (equal to PHI by construction: L11 draws 2J_c from range(PHI[k]+1)) | '
      f'2J_c ≤ k admits {dict((k, k) for k in (1, 2, 3))} | excluded at every k: {all(phys[k] > k for k in phys)} | φ̂ = physical at every k: {phys == T.PHI}')
p2 = max(sum(2 * ml + ms for ml, ms in sub) for sub in itertools.combinations([(ml, ms) for ml in (-1, 0, 1) for ms in (-1, 1)], 2))
print(f'p² shell: largest 2J = {p2} (L2793–2794 "A term of a p² shell can reach 2J_c = 4 where k = 2 permits 2")')
M = open(os.path.join(H, 'The_Method_1_6-2.md'), encoding='utf-8').read().split('\n')
prov = []
for i in range(3413, 3428):
    cells = M[i].split()
    if cells and cells[-1].strip('*') in ('law', 'extent', 'construction', 'observation', 'fact', 'physics') and cells[-1].strip('*') not in prov: prov.append(cells[-1].strip('*'))
print(f'§12.11.3.1 provenance column, distinct values in order of first appearance (L3414–3427): {prov} | third value: {prov[2] if len(prov) > 2 else None}')
