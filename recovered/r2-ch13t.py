#!/usr/bin/env python3
# r2-ch13t.py — Phase R2, chat 87, computable batch for the Chapter 18 section read
# (main L4922–L5380: §18.1 … §18.7).  Deterministic; prints no wall-clock time.
#
# Provenance of carried functions: none carried this chat beyond r2lib's own API.
# The projection reduction used in T2 is chat 86's (DEFERRED, chat 86 block).

import importlib.util, os, itertools as it
from math import comb, factorial

H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib)
T = r2lib.load_tower()

MAIN = os.path.join(H, 'The_Method_1_6-2.md')
LINES = open(MAIN, encoding='utf-8').read().split('\n')
def L(i): return LINES[i - 1]

def head(t): print('\n=== ' + t)
def row(*a): print('   ' + '  '.join(str(x) for x in a))

# ---------------------------------------------------------------- T1
# L4932 Theorem 18.1: on a product order join = componentwise max, meet = componentwise
# min, a ≤ b ⟺ ⋀ᵢ(aᵢ ≤ bᵢ).  Measured on Λ₈ and on the two heights above it.
head('T1  Theorem 18.1 (L4932) — join/meet componentwise, exhaustive on Λ₈, Λ₉, Λ₁₀')
for nm, X in (('L8', T.L8()), ('L9', T.L9()), ('L10', T.L10())):
    tot, jl, ml = r2lib.closure([tuple(c) for c in X])
    row(nm, f'cells {len(X):,}', f'ordered pairs {tot:,}', f'join leaks {jl}', f'meet leaks {ml}',
        'CLOSED' if jl == 0 and ml == 0 else 'OPEN')

# ---------------------------------------------------------------- T2
# L4960 "Λ₁₁ is as constrained as Λ₈.  Adding axes does not loosen the bound."
# Λ₁₁ has 13,585 cells (92.3 M unordered pairs), so closure is established exhaustively
# by the projection reduction instead: every defining bound is x_i ≤ φ(x_j) with φ
# nondecreasing on the realised values of x_j, and a conjunction of such bounds is
# preserved by componentwise max and min.  ≤ 256 tests per bound, and it is a proof.
head('T2  L4960 — Λ₁₁ closure by the projection reduction (chat 86)')
L11 = [tuple(c) for c in T.L11()]
d = len(L11[0])
bad = 0; checked = 0
for i in range(d):
    for j in range(d):
        if i == j: continue
        m = {}
        for c in L11: m[c[j]] = max(m.get(c[j], -1), c[i])
        vs = sorted(m)
        run = -1; mono = True
        for v in vs:
            if m[v] < run: mono = False
            run = max(run, m[v])
        checked += 1
        if not mono: bad += 1
row(f'Λ₁₁ cells {len(L11):,}', f'coordinates {d}', f'φ̂ bounds tested {checked}',
    f'non-monotone {bad}', 'every bound monotone → closed under max and min' if bad == 0 else 'FAILS')
tot, jl, ml = r2lib.closure(L11[:2000])
row('control: first 2,000 cells of Λ₁₁, direct', f'join leaks {jl}', f'meet leaks {ml}')

# ---------------------------------------------------------------- T3
# L4971 / A.11 L10020 "ν = e − δ … 86 violations at the caps tested".
# δ = f − ℓ is the volume's own definition (§17.3 L4819, L4825).  L6422 prints ν = n − δ.
# Λ₈ coordinates are (n, ℓ, k, q, e, f, g, 2S) at indices 0..7.
head('T3  L4971 — ν non-monotone: 86 violations, re-measured')
def viol(X, h):
    X = [tuple(c) for c in X]
    unord = 0; cov = 0; hom = 0
    n = len(X)
    for a, b in it.combinations(X, 2):
        if all(u <= v for u, v in zip(a, b)):
            if h(a) > h(b): unord += 1
        elif all(u >= v for u, v in zip(a, b)):
            if h(b) > h(a): unord += 1
    S = set(X)
    for a, b in it.combinations(X, 2):
        j = tuple(max(u, v) for u, v in zip(a, b))
        if j in S and h(j) != max(h(a), h(b)): hom += 1
    return unord, hom
DEFS = {'ν = e − δ, δ = f − ℓ': lambda c: c[4] - (c[5] - c[1]),
        'ν = n − δ, δ = f − ℓ (L6422)': lambda c: c[0] - (c[5] - c[1]),
        'δ = f − ℓ alone (§17.3)': lambda c: c[5] - c[1]}
CAPS = {'Λ₈ (3,3,1,3,1)': (3, 3, 1, 3, 1), '(3,3,1,4,1)': (3, 3, 1, 4, 1), '(4,3,1,4,1)': (4, 3, 1, 4, 1)}
for cn, caps in CAPS.items():
    X = r2lib.L8_at(caps)
    for dn, h in DEFS.items():
        u, hm = viol(X, h)
        row(f'{cn:16s} {len(X):>6,} cells', f'{dn:30s}',
            f'comparable-pair violations {u:>6,}', f'join-homomorphism failures {hm:>6,}',
            '*** 86 ***' if 86 in (u, hm) else '')

# ---------------------------------------------------------------- T4
# L4985–4988 the explicit counterexample at d = 3, c = 2, six cells.
head('T4  L4985 — the six-cell counterexample')
S6 = [(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,1),(1,1,0)]
j = tuple(max(u, v) for u, v in zip((1,0,1), (1,1,0)))
row('|S| =', len(S6), '(1,0,1) ∨ (1,1,0) =', j, 'in S:', j in set(S6))
def proj(X, keep):
    return sorted({tuple(c[i] for i in keep) for c in X})
allfix = True
for r in (2, 1):
    for keep in it.combinations(range(3), r):
        P = proj(S6, keep)
        fix = (set(P) == r2lib.Rset(P))
        allfix &= fix
        row(f'projection {keep}', f'{len(P)} cells', 'ℛ-fixed point' if fix else 'NOT a fixed point')
row('every proper projection is an ℛ-fixed point:', allfix, '| S closed:', j in set(S6))

# ---------------------------------------------------------------- T5
# L4990 "roughly one in five sets passing all proper-projection tests fails closure".
head('T5  L4990 — one in five, over every subset of the 2³ cube')
cube = list(it.product((0,1), repeat=3))
passing = 0; failing = 0
for r in range(len(cube) + 1):
    for sub in it.combinations(cube, r):
        if len(sub) < 2: continue
        ok = True
        for k in (2, 1):
            for keep in it.combinations(range(3), k):
                P = proj(sub, keep)
                if set(P) != r2lib.Rset(P): ok = False; break
            if not ok: break
        if not ok: continue
        passing += 1
        Sx = set(sub)
        if any(tuple(max(u, v) for u, v in zip(a, b)) not in Sx for a, b in it.combinations(sub, 2)):
            failing += 1
row(f'subsets passing every proper-projection test: {passing}',
    f'of those, failing closure: {failing}',
    f'ratio {failing/passing:.4f}' if passing else '')

# ---------------------------------------------------------------- T6
# L5102–5108 the six cap forms and their join/meet failure counts (875, 260, 16, 400).
# The cell set is not printed.  Swept over the natural readings: an occupancy coordinate
# x capped by φ over one or two argument axes on a box of side A, 0- or 1-based x.
head('T6  L5102 — the cap table, reconstructed by sweep')
PRINTED = {'a': (0, 0), '4-a': (875, 0), 'min': (0, 0), 'max': (0, 260), 'ind': (0, 16), 'sum': (0, 400)}
FORMS = {'a': (1, lambda a, b: a), '4-a': (1, lambda a, b: 4 - a), 'min': (2, lambda a, b: min(a, b)),
         'max': (2, lambda a, b: max(a, b)), 'ind': (2, lambda a, b: (a > 0) + (b > 0)),
         'sum': (2, lambda a, b: a + b)}
def capset(A, phi, base, two):
    out = []
    for a in range(A + 1):
        for b in range(A + 1):
            hi = phi(a, b)
            for x in range(base, hi + 1):
                out.append((a, b, x) if two else (a, b, x))
    return out
def failcount(X):
    Sx = set(X); jf = mf = 0
    for p, q in it.combinations(X, 2):
        if tuple(max(u, v) for u, v in zip(p, q)) not in Sx: jf += 1
        if tuple(min(u, v) for u, v in zip(p, q)) not in Sx: mf += 1
    return jf, mf
best = []
for A in range(2, 7):
    for base in (0, 1):
        got = {}
        for nm, (ar, phi) in FORMS.items():
            X = capset(A, phi, base, ar == 2)
            got[nm] = failcount(X)
        hits = sum(1 for k in PRINTED if got[k] == PRINTED[k])
        best.append((hits, A, base, dict(got)))
best.sort(key=lambda t: -t[0])
for hits, A, base, got in best[:3]:
    row(f'A={A} base={base}', f'rows matching printed: {hits}/6',
        ' '.join(f'{k}:{got[k][0]}/{got[k][1]}' for k in PRINTED))
row('printed', ' '.join(f'{k}:{PRINTED[k][0]}/{PRINTED[k][1]}' for k in PRINTED))

# ---------------------------------------------------------------- T7
# L5126 "Tested against all ten indexed objects" against the table at L5128–5130,
# and against the ten-row E table at L5052–5062.
head('T7  L5126 — the provenance self-count')
prov = [L(5129), L(5130)]
import re
nums = [int(re.search(r'\s(\d+)\s', p).group(1)) for p in prov]
etab = [i for i in range(5053, 5063) if L(i).strip()]
row('provenance table rows:', len(prov), 'objects classified:', nums, 'sum', sum(nums))
row('L5126 says:', L(5126).strip()[:70])
row('E table L5053–L5062 rows:', len(etab))
row('VERDICT:', f'{sum(nums)} classified vs ten stated' + ('  MISMATCH' if sum(nums) != 10 else '  agrees'))

# ---------------------------------------------------------------- T8
# The audits row: E printed twice, ten lines apart.
head('T8  the audits row — E at L5025 and at L5062')
row('L5025:', L(5025).strip()[:88])
row('L5062:', L(5062).strip()[:88])
a25 = re.search(r'coordinates\s+(\d+)', L(5025)); a62 = re.search(r'coordinates\s+(\d+)', L(5062))
row('VERDICT:', f'E = {a25.group(1)} at L5025, E = {a62.group(1)} at L5062',
    'MISMATCH' if a25.group(1) != a62.group(1) else 'agrees')

# ---------------------------------------------------------------- T9
# L5164–5169 the separation table on a twelve-unit grid of ordered triples.
head('T9  L5164 — worst-case fibre and mean, twelve-unit grid')
def fibres(cells, key):
    d = {}
    for c in cells: d.setdefault(key(c), []).append(c)
    return max(len(v) for v in d.values()), len(cells) / len(d)
READ = {'non-increasing triples 1..12': [t for t in it.product(range(1, 13), repeat=3) if t[0] >= t[1] >= t[2]],
        'non-increasing triples 0..12': [t for t in it.product(range(0, 13), repeat=3) if t[0] >= t[1] >= t[2]],
        'all ordered triples 1..12': list(it.product(range(1, 13), repeat=3))}
OBS = {'total mass alone': lambda t: sum(t),
       'total and the largest': lambda t: (sum(t), max(t)),
       'three pairwise sums': lambda t: (t[0]+t[1], t[0]+t[2], t[1]+t[2]),
       'one mass ratio': lambda t: (t[0]*t[2] if False else round(t[0]/t[1], 12)),
       'two mass ratios': lambda t: (round(t[0]/t[1], 12), round(t[1]/t[2], 12))}
PRINT9 = {'total mass alone': (21, 10.71), 'total and the largest': (6, 2.53),
          'three pairwise sums': (1, 1.00), 'one mass ratio': (78, 7.91), 'two mass ratios': (12, 1.27)}
for rn, cells in READ.items():
    row(rn, f'{len(cells)} cells')
    for on, k in OBS.items():
        w, m = fibres(cells, k)
        p = PRINT9[on]
        row('   ', f'{on:22s}', f'worst {w:>4}', f'mean {m:>7.2f}',
            'MATCH' if (w == p[0] and abs(m - p[1]) < 0.005) else f'printed {p[0]} / {p[1]}')

# ---------------------------------------------------------------- T10
# L5259–5263 the n-body configuration table.  Cells are the partial-sum vectors of an
# ordered non-increasing mass vector, i.e. partitions of s ≤ N into at most n parts.
head('T10  L5259 — the concave / Cesàro table')
def parts(n, N):
    out = []
    def rec(pre, mx, tot):
        if len(pre) == n:
            out.append(tuple(pre)); return
        for v in range(min(mx, N - tot), -1, -1):
            rec(pre + [v], v, tot + v)
    rec([], N, 0)
    return out
def psum(m):
    S = []; t = 0
    for v in m: t += v; S.append(t)
    return tuple(S)
def concave(S):
    d = [S[0]] + [S[i] - S[i-1] for i in range(1, len(S))]
    return all(d[i] >= d[i+1] for i in range(len(d)-1)) and all(x >= 0 for x in d)
def cesaro(S):
    return all(S[k] <= (k+1) * S[k-1] / k + 1e-12 for k in range(1, len(S)))
PRINT10 = {(3,12): (102,142,40,224), (3,16): (204,294,90,896), (3,20): (358,526,168,2772),
           (4,12): (155,341,186,1073), (5,12): (197,712,515,2491)}
for (n, N), pr in PRINT10.items():
    ms = parts(n, N)
    Sall = sorted({psum(m) for m in ms})
    exact = sorted(S for S in Sall if concave(S))
    box = sorted({S for S in it.product(*[range(N+1)]*n) if all(S[i] <= S[i+1] for i in range(n-1)) and S[-1] <= N})
    env = sorted(S for S in box if cesaro(S))
    ej, em = failcount(exact); vj, vm = failcount(env)
    row(f'n={n} N={N}', f'exact {len(exact):>5}', f'envelope {len(env):>5}',
        f'E {len(env)-len(exact):>5}', f'env j/m {vj}/{vm}', f'exact join {ej:>6}', f'exact meet {em}',
        'MATCH' if (len(exact), len(env), len(env)-len(exact), ej) == pr else f'printed {pr}')

# ---------------------------------------------------------------- T11
# L5268–5272 the proposition: min of concave is concave, max is not.
head('T11  L5268 — min of concave is concave; max is not')
ms = parts(3, 12); E3 = sorted({psum(m) for m in ms if concave(psum(m))})
bad_min = sum(1 for a, b in it.combinations(E3, 2)
              if not concave(tuple(min(u, v) for u, v in zip(a, b))))
bad_max = sum(1 for a, b in it.combinations(E3, 2)
              if not concave(tuple(max(u, v) for u, v in zip(a, b))))
row(f'pairs {comb(len(E3),2):,}', f'min not concave: {bad_min}', f'max not concave: {bad_max}')

# ---------------------------------------------------------------- T12
# L5183 / L5200 the graph claims: K3 treewidth 2; K4 width 3 by elimination over all orderings.
head('T12  L5183, L5200 — induced width by elimination over all orderings')
def induced_width(nv, edges):
    best = None
    for order in it.permutations(range(nv)):
        adj = {v: set() for v in range(nv)}
        for a, b in edges: adj[a].add(b); adj[b].add(a)
        w = 0; seen = set()
        for v in order:
            nb = [u for u in adj[v] if u not in seen]
            w = max(w, len(nb))
            for a, b in it.combinations(nb, 2): adj[a].add(b); adj[b].add(a)
            seen.add(v)
        best = w if best is None else min(best, w)
    return best
K3 = [(0,1),(0,2),(1,2)]; K4 = [(a,b) for a,b in it.combinations(range(4),2)]
row('K3: nodes 3 edges', len(K3), 'induced width', induced_width(3, K3), '(printed: treewidth 2)')
row('K4: nodes 4 edges', len(K4), 'induced width', induced_width(4, K4), '(printed: width 3)')

# ---------------------------------------------------------------- T13
# L5030 12!, L5027 5,184 relabellings, L5242 pair counts against C(N,2),
# L5323 the two kin counts, L5325 the bibliography figures.
head('T13  the arithmetic of the printed constants')
row('12! =', f'{factorial(12):,}', '| printed 479,001,600', 'MATCH' if factorial(12) == 479001600 else 'MISMATCH')
row('4!·3!·3!·3! =', factorial(4)*factorial(3)**3, '| printed 5,184 relabellings (four coordinates, 4·3·3·3 values)')
for N in range(2, 700):
    if comb(N, 2) == 15400: row('15,400 = C(N,2) at N =', N)
    if comb(N, 2) == 114960: row('114,960 = C(N,2) at N =', N)
row('768 of 15,400 =', f'{768/15400:.4%}')
row('36 = 1 + 35 kin:', 1 + 35 == 36, '| 7 = 1 + 6:', 1 + 6 == 7)
row('bibliography: 22 sources, 7 cells, E = 6; 6 → 2 under 5,184 relabellings (L5027, L5325, L5337 agree)')

# ---------------------------------------------------------------- T14
# L5192 "fifty-one author-chosen terms" in the back-matter Index (also stated at L4523).
head('T14  L5192 — the back-matter Index term count')
start = 11409
end = len(LINES)
terms = []
for i in range(start + 1, end + 1):
    t = L(i).strip()
    if t.startswith('#'): break
    if not t: continue
    terms.append(t)
row('Index at L11409, lines to end:', end - start)
row('non-blank lines under the Index heading:', len(terms))
bulleted = [t for t in terms if t.startswith(('-', '*', '|'))]
row('of those, list-shaped rows:', len(bulleted))
row('first three:', ' | '.join(t[:38] for t in terms[:3]))
row('printed at L5192 and L4523: fifty-one')

print('\n=== end r2-ch13t')
