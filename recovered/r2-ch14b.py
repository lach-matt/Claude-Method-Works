#!/usr/bin/env python3
# r2-ch14b.py - chat 91 - COMPUTABLE batch for the Chapter 21 second-part section read
# (main L5690-L5873: 21.5.1 through 21.5.5).
# Claims measured: 21.5.2's seven constraints, the triple-span table (0/7/20/8 of 35), the seven
# triangle-completing non-edges and "fourteen of the twenty-one unused edges are safe", the tree
# claim and figure 21.1's "base L8 is a caterpillar with k as its hub at degree 4"; 21.5.3's
# L13 constraint-graph table (12*13, girth 5, cycle rank 2, treewidth 2, degree sequence, leaves,
# diameter/radius) and its density and orientation-cost arithmetic; 21.5.4's six-shape table
# (cells, seed, diameter, max degree), "the balanced trees all seed at six; the path and the star
# at eight and seven", "seeds 8, 7, 6, 6, 6, 5", the monotone-in-S list and the greedy/exact split;
# 21.5.5's counts and box arithmetic; and "the largest orientation cost anywhere in this book".
# Deterministic; prints no wall-clock time.

import importlib.util, os, itertools, math
from collections import deque
H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib)
T = r2lib.load_tower()


def seed_of(cells, cap=16):
    """The minimum seed of R(cells) under 14.5.7's covering model (r2lib.cover_model /
    cover_reduce / exact_seed).  Lifted verbatim from r2-ch13z.py (chat 90); owed to r2lib."""
    _c, _e, Mx, _v = r2lib.cover_model(cells)
    red = r2lib.cover_reduce(Mx)
    nd, FULL = red[2], red[3]
    n, _w = r2lib.exact_seed(nd, FULL, cap=cap)
    return n, len(nd)


def greedy_seed(cells):
    """Greedy set cover on the same covering model - the heuristic 21.5.4 says was wrong once."""
    _c, _e, Mx, _v = r2lib.cover_model(cells)
    red = r2lib.cover_reduce(Mx)
    nd, FULL = red[2], red[3]
    have, n = 0, 0
    pool = list(nd)
    while have != FULL:
        best = max(pool, key=lambda w: bin(w & ~have).count('1'))
        if not (best & ~have):
            break
        have |= best; n += 1
    return n


# ---------- graph primitives ----------
def degs(nv, E):
    d = [0] * nv
    for a, b in E:
        d[a] += 1; d[b] += 1
    return d


def adj(nv, E):
    A = [set() for _ in range(nv)]
    for a, b in E:
        A[a].add(b); A[b].add(a)
    return A


def ncomp(nv, E):
    A = adj(nv, E); seen = set(); c = 0
    for v in range(nv):
        if v in seen:
            continue
        c += 1; q = [v]; seen.add(v)
        while q:
            x = q.pop()
            for y in A[x]:
                if y not in seen:
                    seen.add(y); q.append(y)
    return c


def girth(nv, E):
    A = adj(nv, E); best = math.inf
    for s0 in range(nv):
        dist = {s0: 0}; par = {s0: None}; q = deque([s0])
        while q:
            x = q.popleft()
            for y in A[x]:
                if y not in dist:
                    dist[y] = dist[x] + 1; par[y] = x; q.append(y)
                elif y != par[x]:
                    best = min(best, dist[x] + dist[y] + 1)
    return best


def ecc(nv, E):
    A = adj(nv, E); out = []
    for s0 in range(nv):
        dist = {s0: 0}; q = deque([s0])
        while q:
            x = q.popleft()
            for y in A[x]:
                if y not in dist:
                    dist[y] = dist[x] + 1; q.append(y)
        out.append(max(dist.values()) if len(dist) == nv else None)
    return out


def treewidth(nv, E):
    """Exact treewidth by the Bodlaender-Held-Kloks elimination DP (2^nv states)."""
    A = adj(nv, E)
    full = (1 << nv) - 1
    Q = [0] * (1 << nv)
    for S in range(1, 1 << nv):
        best = nv
        for v in range(nv):
            if not (S >> v) & 1:
                continue
            R = S & ~(1 << v)
            # neighbours of v in the graph G[ V \ R ] reachable through R  (Q-value of v wrt R)
            reach = set()
            for u in A[v]:
                if not (R >> u) & 1:
                    reach.add(u)
            seen = set(); stack = [u for u in A[v] if (R >> u) & 1]
            seen.update(stack)
            while stack:
                x = stack.pop()
                for y in A[x]:
                    if (R >> y) & 1:
                        if y not in seen:
                            seen.add(y); stack.append(y)
                    else:
                        reach.add(y)
            reach.discard(v)
            best = min(best, max(Q[R], len(reach)))
        Q[S] = best
    return Q[full]


def is_caterpillar(nv, E):
    d = degs(nv, E)
    inner = [v for v in range(nv) if d[v] > 1]
    IE = [(a, b) for a, b in E if a in inner and b in inner]
    if not inner:
        return True
    di = degs(nv, IE)
    return ncomp(nv, IE) == nv - len(inner) + 1 and max(di) <= 2


NAM8 = ['n', 'l', 'k', 'q', 'e', 'f', 'g', '2S']

print('=== 0. controls ===')
for d in range(8, 14):
    print(f'  |L{d}| = {len(T.STAGES[d]()):,}')

# ---------- 1. L8's constraint graph, from tower-2.py's own generator ----------
# Binary bounds in tower-2.py L10-L16 (provenance: the gate-verified tower-2.py, md5 c0bce27a):
#   l <= n-1 | k <= 4l+2 | q <= k | f <= e-1 | g <= 4f+2 | g <= q | 2S <= k
E8 = [(0, 1), (1, 2), (2, 3), (4, 5), (5, 6), (3, 6), (2, 7)]
BOUNDS = [('l <= n-1', lambda c: c[1] <= c[0] - 1), ('k <= 4l+2', lambda c: c[2] <= 4 * c[1] + 2),
          ('q <= k', lambda c: c[3] <= c[2]), ('f <= e-1', lambda c: c[5] <= c[4] - 1),
          ('g <= 4f+2', lambda c: c[6] <= 4 * c[5] + 2), ('g <= q', lambda c: c[6] <= c[3]),
          ('2S <= k', lambda c: c[7] <= c[2])]
L8 = [tuple(c) for c in T.L8()]
print('\n=== 1. 21.5.2 L5713-L5715 - the seven constraints ===')
for nm, fn in BOUNDS:
    hold = all(fn(c) for c in L8)
    tight = any(eval_ := True for c in L8)  # attainment measured below
    print(f'  {nm:12s} holds on all {len(L8)} cells: {hold}')
att = []
for nm, fn in BOUNDS:
    # tight = the bound is attained with equality somewhere
    eq = {'l <= n-1': lambda c: c[1] == c[0] - 1, 'k <= 4l+2': lambda c: c[2] == 4 * c[1] + 2,
          'q <= k': lambda c: c[3] == c[2], 'f <= e-1': lambda c: c[5] == c[4] - 1,
          'g <= 4f+2': lambda c: c[6] == 4 * c[5] + 2, 'g <= q': lambda c: c[6] == c[3],
          '2S <= k': lambda c: c[7] == c[2]}[nm]
    att.append(any(eq(c) for c in L8))
print(f'  every bound attained with equality: {all(att)}   ({sum(att)}/7)')
d8 = degs(8, E8)
print(f'  nodes 8 - edges {len(E8)} - components {ncomp(8, E8)} - tree: '
      f'{ncomp(8, E8) == 1 and len(E8) == 7}   [L5726 "a tree"]')
print('  degrees ' + ' '.join(f'{NAM8[i]}={d8[i]}' for i in range(8)))
print(f'  L5747 caption "base L8 is a caterpillar with k as its hub at degree 4": '
      f'caterpillar {is_caterpillar(8, E8)}, k degree MEASURED {d8[2]}')

# ---------- 2. the triple table ----------
print('\n=== 2. 21.5.2 L5720-L5725 - triples of constraints, by node span ===')
span = {}
for tri in itertools.combinations(E8, 3):
    n_ = len({v for e in tri for v in e}); span[n_] = span.get(n_, 0) + 1
for k_ in (3, 4, 5, 6):
    print(f'  spanning {k_} nodes: MEASURED {span.get(k_, 0):3d}   printed '
          f'{[0, 7, 20, 8][k_ - 3]:3d}   {"OK" if span.get(k_, 0) == [0, 7, 20, 8][k_ - 3] else "DEVIATION"}')
print(f'  total {sum(span.values())} = C(7,3) = {math.comb(7, 3)}   '
      f'[L5725 "zero of thirty-five"]')

# ---------- 3. near misses ----------
print('\n=== 3. 21.5.2 L5728-L5737 - one edge away in exactly seven places ===')
A8 = adj(8, E8); allp = list(itertools.combinations(range(8), 2))
Eset = {tuple(sorted(e)) for e in E8}
near = [p for p in allp if p not in Eset and (A8[p[0]] & A8[p[1]])]
print(f'  triangle-completing non-edges MEASURED {len(near)}   printed 7   '
      f'{"OK" if len(near) == 7 else "DEVIATION"}')
PRINTED_NEAR = [('n', 'k'), ('l', 'q'), ('l', '2S'), ('k', 'g'), ('q', 'f'), ('q', '2S'), ('e', 'g')]
meas = sorted(tuple(sorted((NAM8[a], NAM8[b]))) for a, b in near)
prt = sorted(tuple(sorted(p)) for p in PRINTED_NEAR)
print(f'  the seven named at L5730-L5733 match the measured set: {meas == prt}')
for (a, b) in near:
    tri = sorted(NAM8[x] for x in ({a, b} | (A8[a] & A8[b])))
    print(f'    add {NAM8[a]}-{NAM8[b]:3s} -> 3-body on {{{", ".join(tri)}}}')
unused = len(allp) - len(E8)
print(f'  unused pairs {unused} (C(8,2)={math.comb(8,2)} - 7); safe {unused - len(near)}   '
      f'[L5736 "fourteen of the twenty-one"]')
inpos = [sum(1 for p in near if e[0] in p or e[1] in p) for e in
         [tuple(sorted(x)) for x in E8]]
print(f'  L5736 "each existing edge sitting in exactly one triangle-completing position": '
      f'per-edge counts MEASURED {inpos}')

# ---------- 4. the L13 constraint graph ----------
# From tower-2.py L20-L24, the parents of each new axis (provenance: tower-2.py, md5 c0bce27a):
#   L9  2S' <= g                     | L10 2S' <= v <= g       | L11 2Jc <= phi(k)
#   L12 2K <= 2Jc + 2*FMAX           | L13 |2J - 2K| <= 1
NAM13 = NAM8 + ["2S'", 'v', '2Jc', '2K', '2J']
E13 = E8 + [(6, 8), (8, 9), (9, 6), (2, 10), (10, 11), (11, 12)]
print('\n=== 4. 21.5.3 L5765-L5769 + figure 21.1 - the L13 constraint graph ===')
print('  RECONSTRUCTION from tower-2.py\'s axis bounds (13 coordinates), not from a printed edge list:')
d13 = degs(13, E13)
print(f'  nodes 13 - edges {len(E13)} - components {ncomp(13, E13)} - '
      f'cycle rank {len(E13) - 13 + ncomp(13, E13)}')
print(f'  girth MEASURED {girth(13, E13)}   printed 5')
ec = ecc(13, E13)
print(f'  diameter {max(ec)} - radius {min(ec)}   printed 6 - 3')
print(f'  treewidth MEASURED {treewidth(13, E13)}   printed 2')
print(f'  degree sequence MEASURED {sorted(d13, reverse=True)}')
print(f'                  printed  [4, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1]')
print(f'  leaves MEASURED {[NAM13[i] for i in range(13) if d13[i] == 1]}   printed 2J, e, n')
print(f'  hub MEASURED {NAM13[d13.index(max(d13))]} degree {max(d13)}   printed k degree 4')
tri13 = [(a, b, c) for a, b, c in itertools.combinations(range(13), 3)
         if b in adj(13, E13)[a] and c in adj(13, E13)[a] and c in adj(13, E13)[b]]
print(f'  triangles MEASURED {[[NAM13[x] for x in t] for t in tri13]}   '
      f'caption L5746 "no triangle at any stage"')
print(f'  NOTE the printed graph is 12 nodes and 13 edges; the reconstruction is 13 and '
      f'{len(E13)}. The disagreement is recorded against the reconstruction.')

# ---------- 5. the six shapes ----------
print('\n=== 5. 21.5.4 L5802-L5808 - six constraint graphs on six nodes ===')
SHAPES = {
    'path':        [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)],
    'star':        [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5)],
    'caterpillar': [(0, 1), (1, 2), (2, 3), (1, 4), (2, 5)],
    'binary tree': [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5)],
    'double star': [(0, 1), (0, 2), (0, 3), (0, 4), (1, 5)],
    'forest':      [(0, 1), (0, 2), (3, 4), (3, 5)],
}
PRINTED = {'path': (5, 28, 30, 8, 5, 2), 'star': (5, 276, 10, 6, 2, 5),
           'caterpillar': (5, 65, 22, 6, 3, 3), 'binary tree': (5, 100, 16, 6, 4, 3),
           'double star': (5, 127, 16, 6, 3, 4), 'forest': (4, 196, 8, 5, 2, 2)}
V = 3   # alphabet 18 = six nodes x three values (L5823 "it is eighteen for every shape")


def cells_of(E, orient):
    out = []
    for c in itertools.product(range(V), repeat=6):
        ok = True
        for (a, b), o in zip(E, orient):
            if (c[a] > c[b]) if o == 0 else (c[b] > c[a]):
                ok = False; break
        if ok:
            out.append(c)
    return out


print('  shape         edges  cells(printed)  orientations reproducing it   diam  maxdeg')
FOUND = {}
for nm, E in SHAPES.items():
    pe, pc, pS, pseed, pdia, pdeg = PRINTED[nm]
    hits = [o for o in itertools.product((0, 1), repeat=len(E)) if len(cells_of(E, o)) == pc]
    d = degs(6, E); e_ = ecc(6, E)
    dia = max(x for x in e_ if x is not None) if ncomp(6, E) == 1 else max(
        max(len({y for y in range(6)}) * 0 + (x or 0) for x in e_), 0)
    if ncomp(6, E) > 1:
        dia = 2
    FOUND[nm] = (hits, E)
    print(f'  {nm:13s} {len(E)}({pe})  {pc:5d}          {len(hits):3d} of {2**len(E):2d}'
          f'                {dia}({pdia})  {max(d)}({pdeg})')

print('\n  exact seeds on the reproducing orientation (branch and bound, seed_of):')
print('  shape          cells   seed MEASURED   seed printed   greedy   S printed')
seeds = {}
for nm in SHAPES:
    hits, E = FOUND[nm]
    pe, pc, pS, pseed, pdia, pdeg = PRINTED[nm]
    if not hits:
        print(f'  {nm:13s}  {pc:5d}   NOT REBUILT - no orientation gives {pc} cells')
        continue
    cs = cells_of(E, hits[0])
    sd, _nd = seed_of(cs)
    gd = greedy_seed(cs)
    seeds[nm] = sd
    same = all(seed_of(cells_of(E, o))[0] == sd for o in hits)
    print(f'  {nm:13s}  {len(cs):5d}   {sd:^13d}   {pseed:^12d}   {gd:^6d}   {pS}'
          f'{"" if same else "   (orientation-dependent)"}')

print('\n  L5813 "the balanced trees all seed at six; the path and the star at eight and seven"')
print(f'    star seed MEASURED {seeds.get("star")}, table L5804 prints '
      f'{PRINTED["star"][3]}, sentence L5814 says seven')
print('  L5818 "seeds 8, 7, 6, 6, 6, 5" against the table column 8, 6, 6, 6, 6, 5')
order = ['path', 'star', 'caterpillar', 'binary tree', 'double star', 'forest']
print(f'    MEASURED in table order: {[seeds.get(n) for n in order]}')
print(f'    printed in the table    : {[PRINTED[n][3] for n in order]}')
print(f'    printed in the sentence : [8, 7, 6, 6, 6, 5]')
print(f'  L5818 diameters "5, 2, 3, 4, 3, 2" vs table: '
      f'{[PRINTED[n][4] for n in order]}')
print(f'  L5819 max degree "2, 5, 3, 3, 4, 2" vs table: '
      f'{[PRINTED[n][5] for n in order]}')
Sp = sorted((PRINTED[n][2], n) for n in order)
print('\n  L5826 "the seed is MONOTONE in S with no exception: 8->5, 10->6, 16->6, 16->6, 22->6, 30->8"')
print('    S sorted  ' + ' '.join(f'{s}->{PRINTED[n][3]}' for s, n in Sp) + '   (table seeds)')
print('    MEASURED  ' + ' '.join(f'{s}->{seeds.get(n)}' for s, n in Sp))
mono_t = all(PRINTED[Sp[i][1]][3] <= PRINTED[Sp[i + 1][1]][3] for i in range(5))
mono_m = all((seeds.get(Sp[i][1]) or 0) <= (seeds.get(Sp[i + 1][1]) or 0) for i in range(5))
print(f'    monotone on the table column: {mono_t}   on the measured column: {mono_m}')
print(f'  L5823 "the alphabet ... is eighteen for every shape": six nodes x {V} values = {6 * V}')

# ---------- 6. arithmetic ----------
print('\n=== 6. printed arithmetic ===')
def chk(lbl, got, prt, fmt='{:.6g}'):
    ok = 'OK' if abs(got - prt) < 5e-2 else 'DEVIATION'
    print(f'  {lbl:58s} MEASURED {fmt.format(got):>8s}  printed {prt}  {ok}')
chk('L5754 constraint index density 7 of 216', 100 * 7 / 216, 3.2, '{:.4g}')
chk('L5776 rebuilt index density 9 of 24', 100 * 9 / 24, 38, '{:.4g}')
chk('L5779 R admits the entire box: 9 cells + E 15', 9 + 15, 24, '{:.0f}')
chk('L5781 orientation cost 15 - 4', 15 - 4, 11, '{:.0f}')
chk('L5792 multipliers 2 + plain 11', 2 + 11, 13, '{:.0f}')
chk('L5792 parents one 7 + two 6', 7 + 6, 13, '{:.0f}')
chk('L5842 density 15 distinct of box 96', 100 * 15 / 96, 16, '{:.4g}')
chk('L5843 orientation cost 21 - 6', 21 - 6, 15, '{:.0f}')
chk('L5845-L5847 carried 22 + 2 + 0', 22 + 2 + 0, 24, '{:.0f}')
chk('L5862 collisions: 24 constraints - 15 distinct cells', 24 - 15, 9, '{:.0f}')
chk('L5854 "eight rows of twenty-eight" removed -> constraints', 28 - 8, 24, '{:.0f}')
chk('L5868 parents 14 + 10', 14 + 10, 24, '{:.0f}')
chk('L5868 form 11 + 7 + 3 + 3', 11 + 7 + 3 + 3, 24, '{:.0f}')
chk('L5869 source 16 + 3 + 5', 16 + 3 + 5, 24, '{:.0f}')
chk('L5870 role 4 + 20', 4 + 20, 24, '{:.0f}')
chk('L5842 box 96 = parents 2 x form 4 x operator 2 x source 3 x role 2',
    2 * 4 * 2 * 3 * 2, 96, '{:.0f}')
chk('L5768 degree sequence sums to 2 x 13 edges', 4 + 3 + 3 + 3 + 2 * 5 + 3, 26, '{:.0f}')
chk('L5745 cycle rank 13 edges - 12 nodes + 1', 13 - 12 + 1, 2, '{:.0f}')

# ---------- 7. "the largest orientation cost anywhere in this book" ----------
print('\n=== 7. L5785 "the largest orientation cost anywhere in this book" ===')
import re
hits = []
for fn in sorted(os.listdir(H)):
    if not fn.endswith('.md') or fn.startswith(('READ-', 'W-', 'HANDOFF', 'DEFERRED', 'RULINGS',
                                                'WORKING-')):
        continue
    try:
        txt = open(os.path.join(H, fn), encoding='utf-8').read().splitlines()
    except Exception:
        continue
    for i, ln in enumerate(txt, 1):
        if 'orientation cost' in ln.lower():
            m = re.findall(r'orientation cost\D{0,12}(\d+)', ln.lower())
            hits.append((fn, i, m, ln.strip()[:96]))
for fn, i, m, ln in hits:
    print(f'  {fn}:{i}  values {m}  {ln}')
vals = [int(v) for _f, _i, m, _l in hits for v in m]
print(f'  MEASURED maximum orientation cost printed anywhere: {max(vals) if vals else None}   '
      f'L5785 claims 11 is the largest')
