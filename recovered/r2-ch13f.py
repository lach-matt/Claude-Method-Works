#!/usr/bin/env python3
# r2-ch13f.py — Phase R2, chat 80, segment 2: main §13.1-§13.4 (L3626-3676).
#   (1) L3641-3647: Λ fibred over q; the two ends as the tower's A and B sides; |Λ| = Σ_q |A_q|·|B_q|
#       at every stage, and E(A_q) = E(B_q) = 0 (§12.8.5) on Λ₈'s fibres.
#   (2) L3657-3660 (the mangled row): |A_q| against |B_q| as q rises — whether A falls and B rises.
#   (3) L3662: whether g ≤ q is the most active constraint, by binding rate over intervals (§12.9's
#       measure) and by tightness over cells, all seven constraints.
#   (4) L3664: rank modularity — r(x∨y) + r(x∧y) = r(x) + r(y) over every pair of Λ₈.
#   (5) L3671: 1,113,045,672 maximal chains (§12.9 L2478), recounted on the cover graph.
# No wall-clock output.
import importlib.util, os, itertools, random
from collections import Counter, defaultdict
import numpy as np

H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib)
T = r2lib.load_tower()
L8 = T.L8()
NAMES8 = ['n', 'ℓ', 'k', 'q', 'e', 'f', 'g', '2S']
n_, l_, k_, q_, e_, f_, g_, S_ = range(8)

# ---- generalises r2lib.factor_q (chat 74) to any stage width; lifted in spirit from r2-ch13b.py's
#      sections(X, w) (chat 79), which DEFERRED lists as owed to r2lib ----
def sections(X, w):
    """q → (|A(q)|, |B(q)|, |Λ(q)|) for a stage of width w. A = the source side, B = the target side."""
    A = defaultdict(set); B = defaultdict(set); N = Counter()
    SRC = [i for i in (0, 1, 2, 7, 10, 11, 12) if i < w]
    TGT = [i for i in (4, 5, 6, 8, 9) if i < w]
    for c in X:
        A[c[3]].add(tuple(c[i] for i in SRC)); B[c[3]].add(tuple(c[i] for i in TGT)); N[c[3]] += 1
    return {v: (len(A[v]), len(B[v]), N[v]) for v in sorted(A)}

print('=== (1) L3641-3647: the fibration over q, and |Λ| = Σ_q |A_q|·|B_q| ===')
print('the two ends as the tower carries them: A = (n, ℓ, k, 2S, 2J_c, 2K, 2J), B = (e, f, g, 2S′, v), base q')
for name, X in (('Λ₈', L8), ('Λ₉', T.L9()), ('Λ₁₀', T.L10()), ('Λ₁₁', T.L11()), ('Λ₁₂', T.L12()), ('Λ₁₃', T.L13())):
    w = len(X[0]); sec = sections(X, w)
    prod = sum(a * b for a, b, _ in sec.values())
    print('  %-4s width %2d  cells %7d  Σ_q |A_q|·|B_q| = %7d  defect %d' % (name, w, len(X), prod, prod - len(X)))

print()
print('=== (2) L3657-3660: |A_q| against |B_q| as q rises (the row as printed is mangled) ===')
sec8 = sections(L8, 8)
print('  q | |A_q| | |B_q| | |Λ_q| | product')
for v, (a, b, nn) in sec8.items():
    print('  %d | %5d | %5d | %5d | %6d' % (v, a, b, nn, a * b))
As = [sec8[v][0] for v in sorted(sec8)]; Bs = [sec8[v][1] for v in sorted(sec8)]
print('  |A_q| strictly falls as q rises:', all(x > y for x, y in zip(As, As[1:])),
      ' |B_q| strictly rises:', all(x < y for x, y in zip(Bs, Bs[1:])))
print('  §12.8.5 E(A_q) = E(B_q) = 0 for every q, on Λ₈\'s fibres:')
bad = []
for v in sorted(sec8):
    Aq = sorted({tuple(c[i] for i in (n_, l_, k_, S_)) for c in L8 if c[q_] == v})
    Bq = sorted({tuple(c[i] for i in (e_, f_, g_)) for c in L8 if c[q_] == v})
    for tag, Y in (('A', Aq), ('B', Bq)):
        nn, jl, ml = r2lib.closure(Y)
        if jl + ml: bad.append((v, tag, jl, ml))
print('    fibres with a join or meet failure:', bad if bad else 'none — E = 0 at every q on both sides')

print()
print('=== (3) L3662: is g ≤ q the most active constraint? ===')
CONS = [('n ≥ ℓ+1', lambda c: c[l_] <= c[n_] - 1, lambda c: c[l_] == c[n_] - 1),
        ('k ≤ 4ℓ+2', lambda c: c[k_] <= 4 * c[l_] + 2, lambda c: c[k_] == 4 * c[l_] + 2),
        ('q ≤ k', lambda c: c[q_] <= c[k_], lambda c: c[q_] == c[k_]),
        ('e ≥ f+1', lambda c: c[f_] <= c[e_] - 1, lambda c: c[f_] == c[e_] - 1),
        ('g ≤ 4f+2', lambda c: c[g_] <= 4 * c[f_] + 2, lambda c: c[g_] == 4 * c[f_] + 2),
        ('g ≤ q', lambda c: c[g_] <= c[q_], lambda c: c[g_] == c[q_]),
        ('2S ≤ k', lambda c: c[S_] <= c[k_], lambda c: c[S_] == c[k_])]
print('  tightness over all %d cells of Λ₈ (the constraint is at equality):' % len(L8))
for tag, ok, tight in CONS:
    assert all(ok(c) for c in L8)
    print('    %-9s %5d cells  %5.1f %%' % (tag, sum(1 for c in L8 if tight(c)), 100 * sum(1 for c in L8 if tight(c)) / len(L8)))
# §12.9's own measure: over comparable pairs (intervals), the share where the constraint binds across
BOX = {'n ≥ ℓ+1': (l_, n_, lambda v: v - 1), 'k ≤ 4ℓ+2': (k_, l_, lambda v: 4 * v + 2),
       'q ≤ k': (q_, k_, lambda v: v), 'e ≥ f+1': (f_, e_, lambda v: v - 1),
       'g ≤ 4f+2': (g_, f_, lambda v: 4 * v + 2), 'g ≤ q': (g_, q_, lambda v: v),
       '2S ≤ k': (S_, k_, lambda v: v)}
A = np.array(L8, dtype=np.int64)
comparable = 0; binds = Counter()
for x in L8:
    m = np.all(A >= np.array(x), axis=1)
    for y in A[m]:
        if tuple(y) == x: continue
        comparable += 1
        for tag, (i, j, phi) in BOX.items():
            if not (int(y[i]) <= phi(x[j])): binds[tag] += 1
print('  binding rate over all %d comparable pairs [x, y] (§12.9\'s interval measure):' % comparable)
for tag, _, _ in CONS:
    print('    %-9s binds in %6d  %5.1f %%' % (tag, binds[tag], 100 * binds[tag] / comparable))
print('  §12.9 prints g≤q 35.6 %, q≤k 33.0 %, g ≤ 4f+2 4.9 %')

print()
print('=== (4) L3664: rank is modular ===')
rank = lambda c: sum(c)
S8 = {tuple(c) for c in L8}
bad = 0; pairs = 0
for x, y in itertools.combinations(L8, 2):
    j = tuple(max(a, b) for a, b in zip(x, y)); m = tuple(min(a, b) for a, b in zip(x, y))
    pairs += 1
    if j not in S8 or m not in S8 or rank(j) + rank(m) != rank(x) + rank(y): bad += 1
print('  r(x∨y) + r(x∧y) = r(x) + r(y) with both in Λ₈, over all %d unordered pairs: failures %d' % (pairs, bad))
print('  (rank = the coordinate sum, 0̂ = 3 to 1̂ = 20, so 17 steps; modularity of the sum is an identity —')
print('   the content is that the join and the meet stay in Λ₈, which is E(Λ₈) = 0)')

print()
print('=== (5) L3671: 1,113,045,672 maximal chains (§12.9 L2478) ===')
byrank = defaultdict(list)
for c in L8: byrank[rank(c)].append(tuple(c))
lo, hi = min(byrank), max(byrank)
print('  ranks %d … %d, so %d steps and %d cells on a maximal chain' % (lo, hi, hi - lo, hi - lo + 1))
paths = {c: 1 for c in byrank[lo]}
assert len(byrank[lo]) == 1 and len(byrank[hi]) == 1, 'not a bounded lattice'
for r in range(lo + 1, hi + 1):
    nxt = {}
    for c in byrank[r]:
        nxt[c] = sum(paths[d] for d in byrank[r - 1] if all(a <= b for a, b in zip(d, c)))
    paths = nxt
print('  0̂ =', byrank[lo][0], ' 1̂ =', byrank[hi][0])
print('  maximal chains by rank-graded path counting on the cover graph: %d' % list(paths.values())[0])
print('  printed 1,113,045,672 at L2478 and L3671')
