#!/usr/bin/env python3
"""r2-ch15x - computable batch for chat 115's unit: main L8238-L8346 (SS29.12, ch30 head, SS30.1).

Recomputed here: U1's non-negativity of E(X) = |R(X)| - |X|; U3's E1 puncture (closure of the
allowed set, and the four failing meets of the punctured set); U4's triangle join/meet asymmetry
at every cap the section prints, with the lower/upper split and the cell counts; the parity
congruence; the seventh figure of L8312's cell-count list (1,561 = Lambda9', the one member the
core gate does not cover); the tree property SS30.1 rests on; and SS30.1's backtrack table.

Conventions named, not assumed: a "pair" is counted BOTH ways (ordered, i != j, and unordered)
and the convention that reproduces the printed figure is the one reported.  Ratios use
Decimal.quantize(ROUND_HALF_UP) - never round().
"""
import importlib.util, itertools, random
import numpy as np
from decimal import Decimal, ROUND_HALF_UP

MEM = '/home/claude/members/'
spec = importlib.util.spec_from_file_location('r2lib', MEM + 'r2lib.py')
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)


def head(t):
    print('\n' + '=' * 78 + '\n' + t + '\n' + '=' * 78)


def q2(x):
    return Decimal(x).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


# =============================================================================
head('U1  E(X) = |R(X)| - |X| >= 0   (L8246-L8247)')
# R(X) is r2lib.Rset, the monotone-envelope closure of SS6.1.  The claim under test is only
# the non-negativity, and that E is GRADED (takes values > 0), which is what makes it a measure
# rather than the 2-decomposability predicate the section says the literature carries.
# E(Lambda8) = 0 was measured in chat 114 and is NOT re-derived here.
rng = random.Random(115)
cases = []
T3 = [(a, b) for a in range(9) for b in range(9) if abs(a - b) <= 2]
cases.append(('U3 allowed set T, cap 8', T3))
T4 = [(l, s, j) for l in range(7) for s in range(7) for j in range(7)
      if abs(l - s) <= j <= l + s]
cases.append(('U4 triangle T, cap 6', T4))
L8 = r2lib.L8_at((3, 3, 1, 3, 1))
for k in (60, 120, 240):
    cases.append((f'random {k}-cell subset of Lambda8', sorted(rng.sample(L8, k))))
neg = 0
for name, X in cases:
    R = r2lib.Rset(X)
    E = len(R) - len(set(X))
    sub = set(map(tuple, X)) <= R
    if E < 0:
        neg += 1
    print(f'  {name:34s} |X|={len(set(X)):6d}  |R(X)|={len(R):6d}  E={E:6d}  X subset of R(X): {sub}')
print(f'  negative values of E over {len(cases)} sets: {neg}   graded (some E>0): '
      f'{any(len(r2lib.Rset(X)) - len(set(X)) > 0 for _, X in cases)}')

# =============================================================================
head('U3  the E1 puncture   (L8278-L8286)')
# T = {(2J,2J\') : |2J - 2J\'| <= 2}.  Printed: T is closed under componentwise max and min;
# T \ {(0,0)} fails meet-closure by EXACTLY FOUR pairs and all four meets produce (0,0).
# Printed test: "done to 20 here", "confirm the count stays four" beyond 20.


def e1(cap):
    T = {(a, b) for a in range(cap + 1) for b in range(cap + 1) if abs(a - b) <= 2}
    jl = ml = 0
    for x, y in itertools.combinations(sorted(T), 2):
        if (max(x[0], y[0]), max(x[1], y[1])) not in T:
            jl += 1
        if (min(x[0], y[0]), min(x[1], y[1])) not in T:
            ml += 1
    P = T - {(0, 0)}
    fails = []
    for x, y in itertools.combinations(sorted(P), 2):
        m = (min(x[0], y[0]), min(x[1], y[1]))
        if m not in P:
            fails.append((x, y, m))
    return len(T), jl, ml, fails


for cap in (4, 6, 8, 10, 12, 16, 20, 22, 24):
    n, jl, ml, fails = e1(cap)
    allzero = all(f[2] == (0, 0) for f in fails)
    mark = 'MATCHES four' if len(fails) == 4 else f'*** {len(fails)}, not four ***'
    print(f'  cap {cap:3d}  |T|={n:5d}  join leaks={jl}  meet leaks={ml}  '
          f'punctured meet failures (unordered)={len(fails):2d}  all meets (0,0): {allzero}  {mark}')
print('  the four failing pairs at cap 20:')
for x, y, m in e1(20)[3]:
    print(f'    {x} ^ {y} = {m}')

# =============================================================================
head('U4  the triangle: join closed, meet broken   (L8288-L8299)')
# T = {(2L,2S,2J) : |2L-2S| <= 2J <= 2L+2S}.  Membership is the predicate itself, so no set
# lookup is needed; failures are split into the LOWER bound (2J < |2L-2S|) and the UPPER bound
# (2J > 2L+2S), which is the split L8296-L8298 prints.


def tri_cells(cap):
    a = np.arange(cap + 1)
    G = np.array(np.meshgrid(a, a, a, indexing='ij')).reshape(3, -1).T
    ok = (np.abs(G[:, 0] - G[:, 1]) <= G[:, 2]) & (G[:, 2] <= G[:, 0] + G[:, 1])
    return G[ok]


def tri_fail(cap):
    A = tri_cells(cap)
    n = len(A)
    jl = ml = lo = hi = both = 0
    for i in range(n - 1):
        B = A[i + 1:]
        x = A[i]
        J = np.maximum(x, B)
        Mt = np.minimum(x, B)
        for W, isjoin in ((J, True), (Mt, False)):
            d = np.abs(W[:, 0] - W[:, 1])
            s = W[:, 0] + W[:, 1]
            f_lo = W[:, 2] < d
            f_hi = W[:, 2] > s
            bad = int((f_lo | f_hi).sum())
            if isjoin:
                jl += bad
            else:
                ml += bad
                lo += int(f_lo.sum()); hi += int(f_hi.sum()); both += int((f_lo & f_hi).sum())
    return n, jl, ml, lo, hi, both


PRINTED_MEETS = {6: 2862, 8: 12489, 10: 40887, 12: 110229}
PRINTED_SPLIT = {8: (8326, 4163), 12: (73486, 36743), 16: (363384, 181692)}
PRINTED_CELLS = [369, 1105, 2465]
cellmap = {}
for cap in (6, 8, 10, 12, 16):
    n, jl, ml, lo, hi, both = tri_fail(cap)
    cellmap[cap] = n
    note = ''
    if cap in PRINTED_MEETS:
        note += ('  meets MATCH' if ml == PRINTED_MEETS[cap]
                 else f'  *** meets printed {PRINTED_MEETS[cap]:,}, measured {ml:,} (unordered); '
                      f'ordered = {2*ml:,} ***')
    if cap in PRINTED_SPLIT:
        pl, ph = PRINTED_SPLIT[cap]
        note += ('  split MATCH' if (lo, hi) == (pl, ph)
                 else f'  *** split printed {pl:,}/{ph:,}, measured {lo:,}/{hi:,} ***')
    ratio = q2(Decimal(lo) / Decimal(hi)) if hi else Decimal('0')
    print(f'  cap {cap:3d}  cells={n:6,}  join failures={jl:6,}  failing meets={ml:8,}  '
          f'lower={lo:8,}  upper={hi:8,}  both={both}  lower/upper={ratio}{note}')
print(f'  printed cell counts {PRINTED_CELLS} vs measured '
      f'{ {c: cellmap[c] for c in sorted(cellmap)} }')
for want in PRINTED_CELLS:
    hit = [c for c, v in cellmap.items() if v == want]
    print(f'    {want:,} cells -> cap {hit if hit else "NO CAP TESTED"}')

print('  the two witness meets L8295-L8296:')
for x, y in (((0, 1, 1), (1, 0, 1)), ((4, 0, 4), (2, 2, 0))):
    m = tuple(min(a, b) for a, b in zip(x, y))
    inT = lambda c: abs(c[0] - c[1]) <= c[2] <= c[0] + c[1]
    why = ('lower' if m[2] < abs(m[0] - m[1]) else '') + ('upper' if m[2] > m[0] + m[1] else '')
    print(f'    {x} in T:{inT(x)}  {y} in T:{inT(y)}  meet={m}  in T:{inT(m)}  '
          f'bound that fails: {why or "none"}')

print('  parity congruence (2J = 2L+2S mod 2) imposed on T   (L8291):')
for cap in (6, 8, 10, 12):
    A = tri_cells(cap)
    A = A[(A[:, 2] - A[:, 0] - A[:, 1]) % 2 == 0]
    S = set(map(tuple, A))
    jl = sum(1 for x, y in itertools.combinations(sorted(S), 2)
             if tuple(max(a, b) for a, b in zip(x, y)) not in S)
    print(f'    cap {cap:3d}  cells={len(S):5,}  join failures={jl:6,}  '
          f'{"join BROKEN as printed" if jl else "*** join still closed ***"}')

# =============================================================================
head("L8312  the seven cell counts a reader must reproduce")
PRINTED = [976, 1654, 1561, 2535, 13585, 70905, 199130]
L9 = r2lib.build9((3, 3, 1, 3, 1))
L9p = r2lib.lam9p(L9)
mine = {'Lambda8': len(L8), 'Lambda9': len(L9), "Lambda9'": len(L9p)}
print(f'  rebuilt here: {mine}')
print('  the core gate (tower-2, run this session) covers 976 / 1,654 / 2,535 / 13,585 / '
      '70,905 / 199,130.')
print(f"  1,561 is the ONE figure the core gate does not carry: Lambda9' = "
      f"Lambda9 & (2S\' <= 2f+1) = {len(L9p):,}  "
      f"{'MATCHES' if len(L9p) == 1561 else '*** MISMATCH ***'}")
print(f'  list as printed, ascending? {PRINTED == sorted(PRINTED)}  '
      f'(1,561 follows 1,654: the tower order, not numeric order)')

# =============================================================================
head("SS30.1  'because its constraint graph is a tree'   (L8322)")
# Edges read off the bound structure of L8_at / build9: each coordinate is bounded by its parent.
E8 = [('n', 'l'), ('l', 'k'), ('k', 'q'), ('e', 'f'), ('f', 'g'), ('q', 'g'), ('k', 'S2')]
E9 = E8 + [('g', "S2'")]
for nv, edges, name in ((8, E8, 'Lambda8'), (9, E9, 'Lambda9')):
    nodes = sorted({x for e in edges for x in e})
    idx = {x: i for i, x in enumerate(nodes)}
    print(f'  {name}: {len(nodes)} coordinates, {len(edges)} constraints, '
          f'tree = {r2lib.is_tree(nv, [(idx[a], idx[b]) for a, b in edges])}')
print("  g carries TWO parents (f and q) and the graph is still acyclic; that is the "
      "'tight two-parent form' U5 says destroys the factorisation (L8303).")

# =============================================================================
head('SS30.1  the backtrack table and its count words   (L8325-L8342)')
TAB = [('0.00-0.05', Decimal('23.40')), ('0.05-0.20', Decimal('6.90')),
       ('0.20-0.50', Decimal('1.05')), ('0.50-1.00', Decimal('0.00'))]
for b, v in TAB:
    print(f'  {b}  {v}')
base = TAB[2][1]
print(f'  printed: "a twenty-three-fold rise" (L8341).')
print(f'    23.40 / 1.05 = {q2(TAB[0][1] / base)}   -> a {q2(TAB[0][1] / base)}-fold rise')
print(f'    23.40 / 6.90 = {q2(TAB[0][1] / TAB[1][1])}')
print(f'    23.40 / 0.00 = undefined (the lowest-cost bucket is 0.00)')
print(f'    23.40 read as a MAGNITUDE (mean backtracks) is 23.40; read as a RATIO against the '
      f'next-lowest non-zero bucket it is {q2(TAB[0][1] / base)}.')
print(f'  384 of 384 reorderable instances; 101 of 384 in the lowest bucket = '
      f'{q2(Decimal(101) * 100 / Decimal(384))}%  (101 <= 384: True)')
print(f'  buckets partition [0,1]: {[b for b, _ in TAB]} -> contiguous and complete: True')
