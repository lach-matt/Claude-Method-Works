# r2-ch3.py — Phase R2, main Chapter 3 (chat 69). Re-measures every figure of Chapter 3 that is computable
# from what the chapter itself prints: the §2.21 coordinate table (L1116–1138), the §3.7 precedences
# (L1307–1313) and the four linear extensions (L1320–1330). Every line printed is MEASURED; the read decides.
import re, itertools, sys
MAIN = sys.argv[1] if len(sys.argv) > 1 else '../members94/The_Method_1_6-2.md'
lines = open(MAIN, encoding='utf-8').read().split('\n')
# ---- §2.21 table -------------------------------------------------------------------------------------
READS = ['object', 'source', 'artefact', 'outside']
COMP = ['itself', 'other places', 'a computation']
COST = ['wrong', 'unreadable', 'unusable', 'dishonest']
PRES = ['nothing', 'claims individually true', 'also mutually consistent']   # 'labels are addressable' reads as the second (L1143)
rows = {}
for ln in lines[1116:1138]:
    m = re.match(r'\s*(\d+)\s+([A-Z]+)\s+(object|source|artefact|outside)\s+(itself|other places|a computation)\s+(wrong|unreadable|unusable|dishonest)\s+(.+?)\s*$', ln)
    assert m, ln
    no, name, r, c, k, p = m.groups()
    p = 'claims individually true' if p == 'labels are addressable' else p
    rows[int(no)] = (name, (READS.index(r), COMP.index(c), COST.index(k), PRES.index(p)))
assert len(rows) == 22 and [rows[i][0] for i in range(1, 23)] == ['LATTICE','EQUATIONS','CONSISTENCY','REDUNDANCY','ARTEFACT','COHERENCE','ATTRIBUTION','CELL','DISTINCTNESS','SCOPE','ANTECEDENT','MARKUP','AGREEMENT','ARITHMETIC','ENUMERATION','FIDELITY','MEASURE','REPRODUCTION','SEQUENCE','PROJECTION','INPUT','CENSUS']
cells4 = [rows[i][1] for i in range(1, 23)]
print('§2.21 table: 22 rows;', len(set(cells4)), 'distinct 4-cells (L1140 "twenty-two distinct cells, no collision");',
      len(set(c[:3] for c in cells4)), 'distinct 3-cells over 22;',
      len(set(c[:3] for c in cells4[:18])), 'distinct 3-cells over the first 18 (Register L1053 "eighteen audits over seventeen cells")')
# ---- closure operators ------------------------------------------------------------------------------------
def box(X):
    d = len(next(iter(X))); lo = [min(x[i] for x in X) for i in range(d)]; hi = [max(x[i] for x in X) for i in range(d)]
    return set(itertools.product(*[range(lo[i], hi[i] + 1) for i in range(d)]))
def closure(X):   # the tightest monotone two-variable-bound closure of r2-ch1.py, coordinate-general
    X = set(X); d = len(next(iter(X))); B = box(X)
    lo = [min(x[i] for x in X) for i in range(d)]; hi = [max(x[i] for x in X) for i in range(d)]
    F = {}; G = {}
    for i in range(d):
        for j in range(d):
            if i == j: continue
            for v in range(lo[i], hi[i] + 1):
                le = [x[j] for x in X if x[i] <= v]; ge = [x[j] for x in X if x[i] >= v]
                F[(i, j, v)] = max(le) if le else -1
                G[(i, j, v)] = min(ge) if ge else 10 ** 6
    return {z for z in B if all(G[(i, j, z[i])] <= z[j] <= F[(i, j, z[i])] for i in range(d) for j in range(d) if i != j)}
stages = [('as first stated (1–7)', 7), ('the eleven retained (1–18)', 18), ('SEQUENCE added (1–19)', 19),
          ('PROJECTION added (1–20)', 20), ('INPUT added (1–21)', 21), ('CENSUS added (1–22)', 22)]
print('E(audits) = |closure(X)| − |X| ; printed §3.8 table: 7→11 at 3 coords, 18→0 at 3, 18→19 at 4, 19→18, 20→17; §3.7.1: 21→16; Register L1473: 16')
for label, n in stages:
    X4 = set(cells4[:n]); X3 = set(c[:3] for c in cells4[:n])
    print('  %-28s 3 coords: closure E=%2d box E=%2d | 4 coords: closure E=%2d box E=%3d' % (
        label, len(closure(X3)) - len(X3), len(box(X3)) - len(X3), len(closure(X4)) - len(X4), len(box(X4)) - len(X4)))
X6 = set(cells4[:6]); X6_3 = set(c[:3] for c in cells4[:6])
print('  first six without ATTRIBUTION: 3 coords closure E=%d box E=%d' % (len(closure(X6_3)) - len(X6_3), len(box(X6_3)) - len(X6_3)))
# ---- §3.7 precedences ------------------------------------------------------------------------------------------
P = [('CELL','LATTICE'),('LATTICE','EQUATIONS'),('CELL','DISTINCTNESS'),
     ('EQUATIONS','SCOPE'),('EQUATIONS','AGREEMENT'),('EQUATIONS','ARITHMETIC'),('EQUATIONS','ENUMERATION'),
     ('CONSISTENCY','REDUNDANCY'),('CONSISTENCY','ARTEFACT'),('REDUNDANCY','ARTEFACT'),
     ('MARKUP','ARTEFACT'),('MARKUP','FIDELITY'),
     ('ARTEFACT','MEASURE'),('ARTEFACT','FIDELITY'),('ARTEFACT','PROJECTION'),
     ('ATTRIBUTION','REPRODUCTION'),
     ('SEQUENCE','ANTECEDENT'),('SEQUENCE','COHERENCE'),('SEQUENCE','PROJECTION'),
     ('INPUT','SCOPE'),('INPUT','ARITHMETIC'),('INPUT','ENUMERATION')]
names = [rows[i][0] for i in range(1, 23)]
print('precedences listed at L1307–1313:', len(P), '(L1304 "nineteen" + INPUT\'s three)')
# components
adj = {n: set() for n in names}
for a, b in P: adj[a].add(b); adj[b].add(a)
seen = set(); comps = []
for n in names:
    if n in seen: continue
    st = [n]; comp = set()
    while st:
        u = st.pop()
        if u in comp: continue
        comp.add(u); st.extend(adj[u] - comp)
    seen |= comp; comps.append(sorted(comp))
print('components of the 22 under the precedences:', sorted(len(c) for c in comps), '; singletons:', [c for c in comps if len(c) == 1],
      '(L1315 "three components — ten audits, nine, and a pair")')
# transitive closure
def tc(P, U):
    R = set(P)
    changed = True
    while changed:
        changed = False
        for (a, b) in list(R):
            for (c, d) in list(R):
                if b == c and (a, d) not in R: R.add((a, d)); changed = True
    return {(a, b) for (a, b) in R if a in U and b in U}
L9a = 'CELL DISTINCTNESS LATTICE EQUATIONS AGREEMENT INPUT SCOPE ARITHMETIC ENUMERATION'.split()
L9b = 'INPUT CELL LATTICE EQUATIONS ENUMERATION ARITHMETIC SCOPE AGREEMENT DISTINCTNESS'.split()
L10a = 'CONSISTENCY REDUNDANCY MARKUP ARTEFACT FIDELITY MEASURE SEQUENCE PROJECTION COHERENCE ANTECEDENT'.split()
L10b = 'SEQUENCE ANTECEDENT COHERENCE MARKUP CONSISTENCY REDUNDANCY ARTEFACT PROJECTION MEASURE FIDELITY'.split()
def pairs(Lst): return {(Lst[i], Lst[j]) for i in range(len(Lst)) for j in range(i + 1, len(Lst))}
def count_ext(U, R):
    U = list(U); idx = {u: i for i, u in enumerate(U)}
    below = {u: {a for (a, b) in R if b == u} for u in U}
    from functools import lru_cache
    @lru_cache(None)
    def f(mask):
        if mask == (1 << len(U)) - 1: return 1
        tot = 0
        for u in U:
            if not mask >> idx[u] & 1 and all(mask >> idx[a] & 1 for a in below[u]): tot += f(mask | 1 << idx[u])
        return tot
    return f(0)
for tag, La, Lb in [('nine', L9a, L9b), ('ten', L10a, L10b)]:
    U = set(La); assert U == set(Lb)
    R = tc(P, U)
    ext_a = R <= pairs(La); ext_b = R <= pairs(Lb)
    inter = pairs(La) & pairs(Lb)
    print('component of %s: L1 is a linear extension: %s; L2: %s; L1∩L2 == the order: %s (order has %d comparable pairs, intersection %d); linear extensions: %d (L1332–1333 "4,140" / "792")'
          % (tag, ext_a, ext_b, inter == R, len(R), len(inter), count_ext(U, R)))
    if inter != R: print('   extra pairs in intersection:', sorted(inter - R), '; missing:', sorted(R - inter))
n9, n10 = 9, 10
print('comparisons: 2·C(9,2)+2·C(10,2) =', 2 * 36 + 2 * 45, '; 4 lists × pairs =', 4 * (36 + 45), '; +2×19 precedences =', 4 * (36 + 45) + 38, '; +2×22 =', 4 * (36 + 45) + 44, '(L1335 "362")')
print('unordered pairs of ten-component extensions: 4140·4139/2 =', 4140 * 4139 // 2, '(L1336 "eight and a half million")')
# at twenty audits (no INPUT, no CENSUS): components and precedence count
P20 = [(a, b) for (a, b) in P if 'INPUT' not in (a, b)]
adj20 = {n: set() for n in names[:20]}
for a, b in P20: adj20[a].add(b); adj20[b].add(a)
seen = set(); sizes = []
for n in names[:20]:
    if n in seen: continue
    st = [n]; comp = set()
    while st:
        u = st.pop()
        if u in comp: continue
        comp.add(u); st.extend(adj20[u] - comp)
    seen |= comp; sizes.append(len(comp))
print('at twenty audits: %d precedences, components %s (L1390–1391 "nineteen precedences … three components")' % (len(P20), sorted(sizes)))
