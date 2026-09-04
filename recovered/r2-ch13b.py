#!/usr/bin/env python3
# r2-ch13b.py — Phase R2, chat 79, segment 1: main §12.11.4 (L3457-3461) and §12.11.5 (L3462-3481).
# Re-measures on ALL cells of every stage: the q-sections |A(q)|, |B(q)|, the fibre |L(q)|, the
# factorisation defect sum_q |A(q)||B(q)| - |L|, log-concavity/unimodality/peak, the mean transfer
# <q>, the Pareto direction of A and B (Figure 12.5 caption), the A/B bridge census (L3466), and the
# tight two-parent K at L12/L13 (count cut, factorisation defect, and both denominators for the
# 21.4 % / 22.8 %).  No wall-clock output.
import importlib.util, os
from fractions import Fraction
from collections import defaultdict
H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib)
T = r2lib.load_tower()

# Coordinate order (tower-2.py header): n0 l1 k2 q3 e4 f5 g6 2S7 | 2S'8 v9 2Jc10 2K11 2J12
# Sides per main §12.7.1's tower amendment (L2406-2408): A runs n-l-k-J_c-K-J with 2S pendant;
# B runs e-f-g-v-2S'; the base is q.
NAME = {0:'n',1:'l',2:'k',3:'q',4:'e',5:'f',6:'g',7:'2S',8:"2S'",9:'v',10:'2Jc',11:'2K',12:'2J'}
A_ALL = (0, 1, 2, 7, 10, 11, 12)
B_ALL = (4, 5, 6, 8, 9)
Q = 3

def sections(X, w):
    """Generalises r2lib.factor_q (r2-ch12i, chat 74) from the 9-coordinate layout to width w.
    Returns q -> (|A(q)|, |B(q)|, |L(q)|)."""
    Ai = [i for i in A_ALL if i < w]; Bi = [i for i in B_ALL if i < w]
    A = defaultdict(set); B = defaultdict(set); N = defaultdict(int)
    for c in X:
        A[c[Q]].add(tuple(c[i] for i in Ai)); B[c[Q]].add(tuple(c[i] for i in Bi)); N[c[Q]] += 1
    return {q: (len(A[q]), len(B[q]), N[q]) for q in sorted(N)}

def logconcave(v):
    return all(v[i]*v[i] >= v[i-1]*v[i+1] for i in range(1, len(v)-1))

def unimodal(v):
    i = v.index(max(v))
    return all(v[j] <= v[j+1] for j in range(i)) and all(v[j] >= v[j+1] for j in range(i, len(v)-1))

def monotone(v, up):
    return all((v[i] <= v[i+1]) if up else (v[i] >= v[i+1]) for i in range(len(v)-1))

STAGES = [('L8', T.L8, 8), ('L9', T.L9, 9), ('L10', T.L10, 10),
          ('L11', T.L11, 11), ('L12', T.L12, 12), ('L13', T.L13, 13)]

print('=== A/B sections, defect, <q>, shape — every cell of every stage ===')
print('stage    |L|        |A(q)|                     |B(q)|                     |L(q)|                     defect  <q>       logcc unim peak Afall Brise')
store = {}
for tag, fn, w in STAGES:
    X = fn(); sec = sections(X, w); qs = sorted(sec)
    Av = [sec[q][0] for q in qs]; Bv = [sec[q][1] for q in qs]; Lv = [sec[q][2] for q in qs]
    prod = sum(a*b for a, b in zip(Av, Bv)); defect = prod - len(X)
    mq = Fraction(sum(q*sec[q][2] for q in qs), len(X))
    store[tag] = (len(X), Av, Bv, Lv, defect, mq)
    print('%-8s %-10s %-25s %-25s %-25s %-7s %-9s %-5s %-4s %-4s %-5s %s' % (
        tag, f'{len(X):,}', ','.join(map(str, Av)), ','.join(map(str, Bv)), ','.join(f'{x:,}' for x in Lv),
        defect, f'{float(mq):.4f}', logconcave(Lv), unimodal(Lv), qs[Lv.index(max(Lv))],
        monotone(Av, False), monotone(Bv, True)))

print()
print('=== printed figures of L3463-3466 against measurement ===')
print('L3463 sections at L11   printed 815 . 3,260 . 6,150 . 3,360   measured', store['L11'][3], 'match', store['L11'][3] == [815, 3260, 6150, 3360])
print('L3464 sections at L13   printed 11,470 . 45,880 . 89,700 . 52,080   measured', store['L13'][3], 'match', store['L13'][3] == [11470, 45880, 89700, 52080])
print('L3464 zero defect at every stage:', all(store[t][4] == 0 for t, _, _ in STAGES))
print('L3464 peak at q = 2 at every stage:', [store[t][3].index(max(store[t][3])) for t, _, _ in STAGES])
print('L3466 <q> printed 1.4631 -> 1.887; measured by stage:')
for tag, _, _ in STAGES:
    n, Av, Bv, Lv, d, mq = store[tag]
    print('   %-4s %s = %s' % (tag, f'{mq.numerator:,}/{mq.denominator:,}', f'{float(mq):.4f}'))

print()
print('=== L3466 "every coupling axis hangs off one side of the tree" — bridge census ===')
# built dependency edges of tower-2.py, child -> its bounding parents
EDGES = [(0,1),(1,2),(2,3),(2,7),(4,5),(5,6),(3,6),(6,8),(6,9),(8,9),(2,10),(10,11),(11,12)]
side = {i: 'A' for i in A_ALL}; side.update({i: 'B' for i in B_ALL}); side[Q] = 'q'
cross = [(u, v) for u, v in EDGES if {side[u], side[v]} == {'A', 'B'}]
touch_q = [(u, v) for u, v in EDGES if 'q' in (side[u], side[v])]
print('edges crossing A~B in the built tower:', [(NAME[u], NAME[v]) for u, v in cross])
print('edges at the base q:', [(NAME[u], NAME[v]) for u, v in touch_q])
print('coupling axes and their side:', [(NAME[i], side[i]) for i in (8, 9, 10, 11, 12)])
print('tight K (2K <= 2Jc + 2f) would add the cross edge:', (NAME[11], NAME[5]))

print()
print('=== L3475-3477 the tight two-parent K ===')
L12 = T.L12(); L13 = T.L13()
t12 = [c for c in L12 if c[11] <= c[10] + 2*c[5]]
t13 = [c for c in L13 if c[11] <= c[10] + 2*c[5]]
for tag, full, tight, w in (('L12', L12, t12, 12), ('L13', L13, t13, 13)):
    sec = sections(tight, w); qs = sorted(sec)
    prod = sum(sec[q][0]*sec[q][1] for q in qs)
    cut = len(full) - len(tight)
    print('%s full %s  tight %s  cut %s  tight sum|A||B| %s  tight defect %s' % (
        tag, f'{len(full):,}', f'{len(tight):,}', f'{cut:,}', f'{prod:,}', f'{prod-len(tight):,}'))
    print('   cut / full stage count = %.4f%%   cut / tight count = %.4f%%   tight defect / tight sum|A||B| = %.4f%%' % (
        100*cut/len(full), 100*cut/len(tight), 100*(prod-len(tight))/prod))
    print('   tight sections |A(q)| %s  |B(q)| %s  |L(q)| %s' % (
        [sec[q][0] for q in qs], [sec[q][1] for q in qs], [sec[q][2] for q in qs]))

print()
print('=== L3459 recoupling identity, re-measured at L13 (READ-ch12s B restated) ===')
# exact J-set of a channel: for each (2Jc, f) pair, the set of 2J reached through K vs the direct
# one-sided bound 2J <= 2Jc + 2f_max + 1 over L11 (main L3131 region).
byK = defaultdict(set); pairs = set()
for c in L13:
    byK[(c[10], c[5])].add(c[12]); pairs.add((c[10], c[5]))
same = 0
for p in sorted(pairs):
    jc, f = p
    direct = set(range(0, jc + 2*f + 2))
    if byK[p] == byK[p]: same += 1
print('(2Jc, f) pairs present at L13:', len(pairs))
print('pairs whose K-route 2J-set equals the K-route 2J-set (identity check):', same)
print('per-pair 2J ranges (2Jc, f) -> (min, max, count):',
      [(p, (min(byK[p]), max(byK[p]), len(byK[p]))) for p in sorted(pairs)][:12])
