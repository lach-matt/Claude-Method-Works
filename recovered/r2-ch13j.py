#!/usr/bin/env python3
# r2-ch13j.py — Phase R2, chat 82. COMPUTABLE batch for the section read main §14.5.8–§14.6
# (L3810–L4269), under the chat-81 ruling (RULINGS-R2.md): one computable batch per section read.
# Every seed size is measured with the EXACT set-cover solver of r2-ch13h.py §3, never with
# prune-greedy, because §14.5.9 L3919 declares every seed size §14.5.7 and §14.5.8 report to have
# come from one wrong heuristic.
# Deterministic: no wall-clock output.

import importlib.util, os, itertools, random, statistics
import numpy as np

H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib)
T = r2lib.load_tower()
L8 = [tuple(c) for c in T.L8()]
L9 = [tuple(c) for c in T.L9()]
L10 = [tuple(c) for c in T.L10()]


def Rset(X):
    """ℛ(X): every cell of the ambient box ∏ Âᵢ(X) with xᵢ ≤ φ̂ᵢⱼ(xⱼ) for all i ≠ j (§6.1 L1540).
    Copied verbatim from r2-ch13h.py (chat 81), which took it from r2-ch13g.py / r2-ch12r.py's
    Rbox; owed to r2lib."""
    A = np.array(sorted(set(X)), dtype=np.int64); d = A.shape[1]
    vals = [np.unique(A[:, i]) for i in range(d)]
    phi = {}
    for i in range(d):
        for j in range(d):
            if i == j: continue
            m = np.full(int(A[:, j].max()) + 1, -1, dtype=np.int64)
            for v in vals[j]: m[v] = A[A[:, j] <= v, i].max()
            phi[(i, j)] = m
    G = np.array(np.meshgrid(*vals, indexing='ij')).reshape(d, -1).T
    ok = np.ones(len(G), dtype=bool)
    for (i, j), m in phi.items(): ok &= G[:, i] <= m[G[:, j]]
    return set(map(tuple, G[ok]))


# ---------------------------------------------------------------- the set-cover machinery
def model(cells):
    """§14.5.7's definition read as a covering problem: elements are the value slots of the
    ambient box and the envelope steps (i, j, v) -> top; a cell covers a step it witnesses.
    Generalised from r2-ch13h.py §3 (chat 81), which built the same reduction inline for Λ₈."""
    cells = sorted(set(tuple(int(x) for x in c) for c in cells))
    A = np.array(cells, dtype=np.int64); n, d = A.shape
    vals = [sorted(set(int(v) for v in A[:, i])) for i in range(d)]
    elems = []; rows = []
    for i in range(d):
        for v in vals[i]:
            elems.append(('val', i, v, v)); rows.append(A[:, i] == v)
    for i in range(d):
        for j in range(d):
            if i == j: continue
            for v in vals[j]:
                sel = A[:, j] <= v
                top = int(A[sel, i].max())
                elems.append(('phi', i, j, v, top)); rows.append(sel & (A[:, i] == top))
    return cells, elems, np.array(rows), vals


def reduce_model(Mx):
    """Two exact reductions (r2-ch13h §3): drop element e when another element's candidate set is
    contained in e's; then drop any cell whose cover is contained in another cell's."""
    E, n = Mx.shape
    P = np.packbits(Mx, axis=1)
    keep = []
    for e in range(E):
        sub = ~(P & ~P[e]).any(axis=1)          # cand[e2] ⊆ cand[e]
        dom = False
        for e2 in np.flatnonzero(sub):
            e2 = int(e2)
            if e2 == e: continue
            if bool((P[e2] == P[e]).all()):
                if e2 < e: dom = True; break
            else:
                dom = True; break
        if not dom: keep.append(e)
    K = Mx[keep]
    masks = []
    for c in range(K.shape[1]):
        m = 0
        for t in np.flatnonzero(K[:, c]): m |= 1 << int(t)
        masks.append(m)
    uniq = sorted(set(masks))
    nd = [m for m in uniq if m and not any(m != m2 and (m | m2) == m2 for m2 in uniq)]
    FULL = (1 << len(keep)) - 1
    return keep, masks, nd, FULL


def exact_seed(nd, FULL, cap=14):
    """Minimum cover by branch and bound on the reduced model (r2-ch13h §3)."""
    CAND = {}
    def cands(e):
        if e not in CAND: CAND[e] = [m for m in nd if m >> e & 1]
        return CAND[e]
    best = [None]
    def bb(cov, chosen, limit):
        if cov == FULL:
            best[0] = list(chosen); return True
        if len(chosen) >= limit: return False
        rest = FULL & ~cov; pick = None
        while rest:
            b = rest & -rest; e = b.bit_length() - 1; rest ^= b
            c = cands(e)
            if pick is None or len(c) < len(pick): pick = c
            if len(pick) <= 1: break
        for m in pick:
            if bb(cov | m, chosen + [m], limit): return True
        return False
    for limit in range(1, cap + 1):
        best[0] = None
        if bb(0, [], limit): return limit, best[0]
    return None, None


def lower_bound(nd, FULL):
    """Disjoint-element bound: elements whose candidate sets are pairwise disjoint force one cell each."""
    els = [e for e in range(FULL.bit_length()) if FULL >> e & 1]
    cand = {e: [m for m in nd if m >> e & 1] for e in els}
    els.sort(key=lambda e: len(cand[e]))
    used, lb = 0, 0
    for e in els:
        c = 0
        for m in cand[e]: c |= m
        if not (c & used): lb += 1; used |= c
    return lb


def greedy_cover(nd, FULL):
    cov, k = 0, 0
    while cov != FULL:
        m = max(nd, key=lambda m: bin(m & ~cov).count('1'))
        if not (m & ~cov): return None
        cov |= m; k += 1
    return k


def worst_cover(nd, FULL):
    """'reverse' greedy: at each step take a cell covering the FEWEST new elements, but not none."""
    cov, k = 0, 0
    while cov != FULL:
        c = [m for m in nd if m & ~cov]
        m = min(c, key=lambda m: (bin(m & ~cov).count('1'), m))
        cov |= m; k += 1
    return k


def cover_prune(masks, FULL, order):
    """prune-greedy in the cover model: drop while the remainder still covers."""
    keep = list(order)
    cov = 0
    for m in keep: cov |= m
    if cov != FULL: return None
    out = list(keep)
    for m in order:
        t = [x for x in out if x is not m]
        c = 0
        for x in t: c |= x
        if c == FULL: out = t
    return len(out)


def seed_report(name, cells, cap=14, heur=False):
    cl, el, Mx, vals = model(cells)
    keep, masks, nd, FULL = reduce_model(Mx)
    k, wit = exact_seed(nd, FULL, cap)
    line = '   %-26s cells %6d  d %2d  c %d  elements %4d -> %3d irredundant, %3d non-dominated  EXACT %s' % (
        name, len(cl), len(vals), max(len(v) for v in vals), len(el), len(keep), len(nd), k)
    print(line)
    if heur:
        idx = sorted(range(len(masks)), key=lambda i: cl[i])
        print('        heuristics: greedy-cover %s  reverse-greedy %s  LB %s  prune(asc) %s  prune(desc) %s' % (
            greedy_cover(nd, FULL), worst_cover(nd, FULL), lower_bound(nd, FULL),
            cover_prune(masks, FULL, [masks[i] for i in idx]),
            cover_prune(masks, FULL, [masks[i] for i in reversed(idx)])))
    return cl, el, Mx, keep, masks, nd, FULL, k, wit


def staircase(d, c):
    """non-increasing d-tuples over {0..c-1}."""
    return [t for t in itertools.product(range(c), repeat=d) if all(t[i] >= t[i + 1] for i in range(d - 1))]


def simplex(d, c):
    """{x ∈ ℤ^d≥0 : Σx ≤ c−1} — the other reading of 'down-set, c'."""
    return [t for t in itertools.product(range(c), repeat=d) if sum(t) <= c - 1]


# ================================================================ §1  §14.5.8 / §14.5.9 the two laws
print('=== (1) L3814-3818 the family table, against L3937-3939 "down-set d+c-1, full box d+c-2" ===')
print('    printed: full box 3^d  4 . 6 . 8 . 10 . 12  law 2d ;  full box 4^d  6 . 9 . 12 . 15 . 18  law 3d')
print('    printed: down-set c=4  5 . 6 . 7 . 8  law d+3 ;  down-set c=5  6 . 7 . 8 . 9  law d+4   (d = 2,3,4,5,6)')
for b, ds in ((3, (2, 3, 4, 5, 6)), (4, (2, 3, 4, 5))):
    got = []
    for d in ds:
        cl, el, Mx, vals = model(list(itertools.product(range(b), repeat=d)))
        keep, masks, nd, FULL = reduce_model(Mx)
        k, _ = exact_seed(nd, FULL)
        got.append((d, len(cl), k, d + b - 2))
    print('   full box %d^d  EXACT %s   d+c-2 %s' % (b, [(d, k) for d, n, k, p in got], [(d, p) for d, n, k, p in got]))
for c in (4, 5):
    for tag, fn in (('staircase', staircase), ('simplex', simplex)):
        got = []
        for d in (2, 3, 4, 5):
            cl, el, Mx, vals = model(fn(d, c))
            keep, masks, nd, FULL = reduce_model(Mx)
            k, _ = exact_seed(nd, FULL)
            got.append((d, len(cl), k))
        print('   down-set c=%d [%s]  cells %s  EXACT %s   d+c-1 %s' % (
            c, tag, [(d, n) for d, n, k in got], [(d, k) for d, n, k in got], [(d, d + c - 1) for d, n, k in got]))

print('=== (2) L3826-3829 / L3871-3875 the tower table: cells, d+c-1, and the EXACT seed ===')
print('    printed: Λ₈ 976 / 11 / set cover 7 ; Λ₉ 1,654 / 12 / 9 ; Λ₁₀ 2,535 / 13 / 9')
print('    printed (withdrawn at L3877): predicted 11,12,13,16 measured 11,12,13,18 for Λ₈..Λ₁₁')
S8 = set(L8)
cl8, el8, Mx8, keep8, masks8, nd8, FULL8, k8, wit8 = seed_report('Λ₈', L8, heur=True)
for nm, cells in (('Λ₉', L9), ('Λ₁₀', L10)):
    cl, el, Mx, keep, masks, nd, FULL, k, wit = seed_report(nm, cells)
    G = [cl[masks.index(m)] for m in wit]
    print('        witness closes: ℛ(G) = Λ : %s' % (Rset(G) == set(cells)))
print('   L3821 "Λ₈ compresses 89×": 976/11 = %.4f ; at the exact seed 976/%d = %.4f' % (976 / 11, k8, 976 / k8))
print('   L3886-3888 "Λ₁₃ nearer twenty-eight, still 7,000× against 199,130": 199130/28 = %.1f' % (199130 / 28))

# ---------------------------------------------------------------- §3  the axis-cost table
print('=== (3) L3890-3898 one axis added five ways to a 35-cell base in four coordinates ===')
print('    printed: base 35 cells seed 7 ; y<=x3 56 (+1), y<=x0 119 (+2), y free 140 (+2),')
print('             |y-x0|<=x1 161 (+10), y<=x0+x1 182 (+11)')
for tag, base in (('staircase(4,4)', staircase(4, 4)), ('simplex(4,4)', simplex(4, 4))):
    cl, el, Mx, vals = model(base)
    keep, masks, nd, FULL = reduce_model(Mx)
    k0, _ = exact_seed(nd, FULL)
    print('   base %-14s cells %d  EXACT seed %d' % (tag, len(base), k0))
    for name, gen in (('counting y <= x3', lambda x: range(0, x[3] + 1)),
                      ('counting y <= x0', lambda x: range(0, x[0] + 1)),
                      ('counting y free ', lambda x: range(0, 4)),
                      ('coupling |y-x0|<=x1', lambda x: range(max(0, x[0] - x[1]), min(6, x[0] + x[1]) + 1)),
                      ('coupling y <= x0+x1', lambda x: range(0, x[0] + x[1] + 1))):
        cells = [tuple(x) + (y,) for x in base for y in gen(x)]
        cl2, el2, Mx2, vals2 = model(cells)
        keep2, masks2, nd2, FULL2 = reduce_model(Mx2)
        k, wit = exact_seed(nd2, FULL2)
        E = len(Rset(cells)) - len(set(cells))
        print('        %-20s cells %4d  alphabet %d  EXACT %2d  cost %+d   E %d' % (
            name, len(cells), max(len(v) for v in vals2), k, k - k0, E))

# ---------------------------------------------------------------- §4  the L3928 heuristic table
print('=== (4) L3928-3932 the eight-column heuristic table ===')
print('    printed  Λ₈ 976: prune 12 cover 7 +prune 7 random 7 reverse 40 LB 5 EXACT 7 spread 33')
print('    printed  down-set d=4 c=4 35: 7 7 7 7 7 7 EXACT 7 spread 0')
print('    printed  full box 3³ 27: 5 5 4 5 6 3 EXACT 4 spread 2 ; full box 4³ 64: 6 6 5 6 8 4 EXACT 5 spread 3')
for tag, cells in (('Λ₈', L8), ('down-set d=4 c=4 [staircase]', staircase(4, 4)),
                   ('down-set d=4 c=4 [simplex]', simplex(4, 4)),
                   ('full box 3³', list(itertools.product(range(3), repeat=3))),
                   ('full box 4³', list(itertools.product(range(4), repeat=3)))):
    cl, el, Mx, vals = model(cells)
    keep, masks, nd, FULL = reduce_model(Mx)
    k, _ = exact_seed(nd, FULL)
    idx = sorted(range(len(masks)), key=lambda i: cl[i])
    rnd = []
    for sd in (1, 2, 3, 4, 5):
        o = list(nd); random.Random(sd).shuffle(o)
        cov, kk = 0, 0
        while cov != FULL:
            m = max(o, key=lambda m: (bin(m & ~cov).count('1'), o.index(m)))
            cov |= m; kk += 1
        rnd.append(kk)
    g = greedy_cover(nd, FULL)
    gp = cover_prune(masks, FULL, [m for m in nd])
    print('   %-28s cells %5d  cover %s  +prune %s  random %s  reverse-greedy %s  prune(asc) %s  prune(desc) %s  LB %s  EXACT %s' % (
        tag, len(cl), g, gp, sorted(set(rnd)), worst_cover(nd, FULL),
        cover_prune(masks, FULL, [masks[i] for i in idx]),
        cover_prune(masks, FULL, [masks[i] for i in reversed(idx)]), lower_bound(nd, FULL), k))

# ---------------------------------------------------------------- §5  the cover structure of Λ₈
print('=== (5) L3961-4074 the four, the 102 elements, the completions, the fifth position ===')
nval = sum(1 for e in el8 if e[0] == 'val')
print('   Λ₈ model: %d elements = %d value slots + %d envelope steps ; irredundant %d ; non-dominated cell covers %d' % (
    len(el8), nval, len(el8) - nval, len(keep8), len(nd8)))
dist = len({tuple(np.flatnonzero(Mx8[e]).tolist()) for e in range(len(el8))})
print('   distinct candidate sets among the %d elements: %d   (L3981 prints "102 elements")' % (len(el8), dist))
CORE = [(1, 0, 2, 2, 3, 1, 2, 2), (2, 1, 3, 3, 1, 0, 0, 3), (2, 1, 3, 3, 2, 1, 3, 0), (3, 1, 1, 0, 3, 1, 0, 0)]
print('   the four printed core cells are cells of Λ₈: %s' % [c in S8 for c in CORE])
ci = [cl8.index(c) for c in CORE]
cov4 = np.zeros(len(el8), dtype=bool)
for i in ci: cov4 |= Mx8[:, i]
print('   they cover %d of %d raw elements ; %d of %d irredundant   (L3981 prints "87 of 102 — 85%%")' % (
    int(cov4.sum()), len(el8), int(cov4[keep8].sum()), len(keep8)))
rem = [el8[e] for e in keep8 if not cov4[e]]
print('   irredundant elements the four miss: %d — %s' % (
    len(rem), ' '.join(('val c%d=%d' % (e[1], e[2])) if e[0] == 'val' else ('phi %d<-%d@%d' % (e[1], e[2], e[3])) for e in rem)))
# marginal coverage of each of the four relative to the other three, and substitutes
for t, i in enumerate(ci):
    others = np.zeros(len(el8), dtype=bool)
    for j in ci:
        if j != i: others |= Mx8[:, j]
    marg = Mx8[:, i] & ~others
    subs = [k for k in range(len(cl8)) if k != i and bool((marg & ~Mx8[:, k]).sum() == 0)]
    margk = int((marg[keep8]).sum())
    print('        cell %-26s marginal raw %3d  irredundant %2d  substitutes %d   (printed 23/18/12/17, 0 substitutes)' % (
        str(CORE[t]), int(marg.sum()), margk, len(subs)))
# unique coverage: is any element covered by exactly one cell?
cnt = Mx8.sum(axis=1)
print('   L3974-3976 "is any envelope element covered by exactly one cell?" Λ₈: elements with exactly one cell = %d of %d'
      % (int((cnt == 1).sum()), len(el8)))
cl9, el9, Mx9, vals9 = model(L9)
c9 = Mx9.sum(axis=1)
print('        Λ₉: %d of %d ; Λ₁₀: ' % (int((c9 == 1).sum()), len(el9)), end='')
cl10, el10, Mx10, vals10 = model(L10)
c10 = Mx10.sum(axis=1)
print('%d of %d' % (int((c10 == 1).sum()), len(el10)))

# every minimum cover of Λ₈
def enum_covers(nd, FULL, size):
    CAND = {}
    def cands(e):
        if e not in CAND: CAND[e] = [m for m in nd if m >> e & 1]
        return CAND[e]
    out = set()
    def rec(cov, chosen):
        if cov == FULL:
            if len(chosen) == size: out.add(frozenset(chosen))
            return
        if len(chosen) >= size: return
        rest = FULL & ~cov; pick = None
        while rest:
            b = rest & -rest; e = b.bit_length() - 1; rest ^= b
            c = cands(e)
            if pick is None or len(c) < len(pick): pick = c
            if len(pick) <= 1: break
        for m in pick:
            if m in chosen: continue
            rec(cov | m, chosen + [m])
    rec(0, [])
    return out

covs = enum_covers(nd8, FULL8, k8)
bym = {}
for i, m in enumerate(masks8): bym.setdefault(m, []).append(i)
tot = 0
for f in covs:
    p = 1
    for m in f: p *= len(bym[m])
    tot += p
print('   L4012-4014 "219 distinct minimum covers": ALL minimum covers of Λ₈ — %d distinct reduced covers, %d distinct cell sets'
      % (len(covs), tot))
coremasks = {masks8[i] for i in ci}
inall = sum(1 for f in covs if coremasks <= f)
print('        reduced covers containing all four printed core cells: %d of %d' % (inall, len(covs)))
# cells appearing in every minimum cover
allcells = set()
for f in covs:
    for m in f: allcells |= set(bym[m])
always = [c for c in range(len(cl8)) if all(any(c in bym[m] for m in f) for f in covs)]
print('        cells that appear in EVERY minimum cover: %d ; distinct cells appearing in some: %d' % (len(always), len(allcells)))
# the completions of the core
trip = []
for f in covs:
    if coremasks <= f:
        rest = list(f - coremasks)
        for combo in itertools.product(*[bym[m] for m in rest]): trip.append(tuple(sorted(combo)))
trip = sorted(set(trip))
cells_in = {}
for t in trip:
    for c in t: cells_in[c] = cells_in.get(c, 0) + 1
if trip:
    vs = sorted(cells_in.values())
    print('   L3992-3993 "519 triples from 66 distinct cells, min 3 median 12 max 157": measured %d triples, %d distinct cells, min %d median %g max %d'
          % (len(trip), len(cells_in), min(vs), statistics.median(vs), max(vs)))
    print('        cells appearing in all triples: %d' % sum(1 for v in vs if v == len(trip)))
# the fifth position (3,0,1,1,*,0,1,1)
def fifth(c): return c[0] == 3 and c[1] == 0 and c[2] == 1 and c[3] == 1 and c[5] == 0 and c[6] == 1 and c[7] == 1
fcells = [i for i in range(len(cl8)) if fifth(cl8[i])]
print('   L4034 cells matching (3,0,1,1,*,0,1,1): %s' % [cl8[i] for i in fcells])
withf = sum(1 for f in covs if any(any(i in bym[m] for i in fcells) for m in f))
print('        reduced minimum covers containing one: %d of %d' % (withf, len(covs)))
for i in fcells:
    n = sum(1 for t in trip if i in t)
    print('        %s appears in %d of %d completions   (printed e=3 in 157, e=1 in 62, of 219)' % (str(cl8[i]), n, len(trip)))
# the six channel conditions
def chan(c, a, b): return (c[1] == a) and (c[1] == b)
conds = {'s->s': lambda c: c[1] == 0 and c[4] >= 0, 'NULL q=0': lambda c: c[3] == 0, 'FULL q=k': lambda c: c[3] == c[2]}
print('   L4021-4027 the six channel conditions, over ALL minimum covers (cell level):')
for nm, fn in (('NULL transition q = 0', lambda c: c[3] == 0), ('FULL transfer q = k', lambda c: c[3] == c[2] and c[2] > 0),
               ('l = 0 present', lambda c: c[1] == 0), ('l = 1 present', lambda c: c[1] == 1)):
    ok = sum(1 for f in covs if any(any(fn(cl8[i]) for i in bym[m]) for m in f))
    allof = sum(1 for f in covs if all(any(fn(cl8[i]) for i in bym[m]) for m in [next(iter(f))]))
    print('        %-24s holds in %d of %d reduced covers' % (nm, ok, len(covs)))
# the binary table
print('=== (6) L4056-4071 the five read as binary ===')
A8 = np.array(cl8)
mn = [int(A8[:, i].min()) for i in range(8)]; mx = [int(A8[:, i].max()) for i in range(8)]
print('   per-coordinate min/max over Λ₈ (n l k q e f g 2S): min %s  max %s' % (mn, mx))
FIVE = CORE + [(3, 0, 1, 1, 3, 0, 1, 1), (3, 0, 1, 1, 1, 0, 1, 1)]
lab = ['corner 1', 'corner 2', 'corner 3', 'corner 4', 'unit 5 (e=3)', 'unit 5 (e=1)']
PRINTED = ['00··11··', '·111000 1', '·111·110', '11001100', '100·10··']
rows = []
for t, c in enumerate(FIVE):
    b = ''.join('1' if c[i] == mx[i] else ('0' if c[i] == mn[i] else '·') for i in range(8))
    rows.append(b)
    print('   %-13s %s   %s' % (lab[t], b, str(c)))
print('   printed rows: 00··11·· / ·1110001 / ·111·110 / 11001100 / 100·10··')
for a, b, nm in ((0, 1, 'corner 1 vs corner 2'), (2, 4, 'corner 3 vs unit 5 (e=3)'), (2, 5, 'corner 3 vs unit 5 (e=1)')):
    pairs = [(rows[a][i], rows[b][i]) for i in range(8)]
    comp = sum(1 for p in pairs if set(p) == {'0', '1'})
    same = sum(1 for p in pairs if p[0] == p[1] and p[0] != '·')
    print('        %-26s complementary bit positions %d, agreeing %d, interior in one or both %d' % (
        nm, comp, same, sum(1 for p in pairs if '·' in p)))
for i in range(8):
    col = [r[i] for r in rows[:5]]
    print('        coordinate %d column %s : has 0 %s, has 1 %s' % (i, ''.join(col), '0' in col, '1' in col))

# ---------------------------------------------------------------- §7  §14.6 the family of closed indexes
print('=== (7) L4084-4146 the family Cl(U): E, the intersection/union rates, the separating pairs ===')
def closure_mask(cellsA, mask):
    """ℛ on a subset of a small ambient, by the same box sweep as Rset, on bitmasks.
    Copied verbatim from r2-ch13h.py §4 (chat 81); owed to r2lib."""
    if mask == 0: return 0
    X = [cellsA[i] for i in range(len(cellsA)) if mask >> i & 1]
    w = len(X[0])
    vs = [sorted({x[i] for x in X}) for i in range(w)]
    phi = {}
    for i in range(w):
        for j in range(w):
            if i == j: continue
            for v in vs[j]: phi[(i, j, v)] = max(x[i] for x in X if x[j] <= v)
    out = 0
    for n, c in enumerate(cellsA):
        if any(c[i] not in vs[i] for i in range(w)): continue
        if all(c[i] <= phi[(i, j, c[j])] for i in range(w) for j in range(w) if i != j): out |= 1 << n
    return out

AMB = [('(2,2)', (2, 2)), ('(3,2)', (3, 2)), ('(2,2,2)', (2, 2, 2)), ('(3,3)', (3, 3)),
       ('(4,3)', (4, 3)), ('(2,2,3)', (2, 2, 3)), ('(2,2,2,2)', (2, 2, 2, 2))]
print('    printed L4092-4095: (2,2,2) 8 cells 74 closed E 182 ∩100%% ∪65.3%% ; (3,3) 9 147 365 100%% 68.8%% ; (2,2,2,2) 16 732 64,804 100%% 32.7%%')
print('    printed L4124-4130: (2,2) 4/13/3 ; (3,2) 6/38/26 ; (2,2,2) 8/74/182 ; (3,3) 9/147/365 ; (4,3) 12/506/3,590 ; (2,2,3) 12/320/3,776')
for nm, shape in AMB:
    cellsA = list(itertools.product(*[range(b) for b in shape]))
    N = len(cellsA)
    closed = [m for m in range(1 << N) if closure_mask(cellsA, m) == m]
    cs = set(closed)
    oi = sum(1 for a in closed for b in closed if (a & b) in cs)
    ou = sum(1 for a in closed for b in closed if (a | b) in cs)
    tot = len(closed) ** 2
    E = (1 << N) - len(closed)
    # the family as an index of characteristic vectors
    fam = [tuple((m >> i) & 1 for i in range(N)) for m in closed]
    R = Rset(fam)
    sep = sum(1 for p in range(N) for q in range(N) if p != q and any((m >> p & 1) and not (m >> q & 1) for m in closed))
    print('   %-9s |U| %2d  |Cl| %5d  2^|U| − |Cl| %6d   ∩ closed %.1f%%  ∪ closed %.1f%%   |ℛ(Cl)| %6d = 2^|U| %s   separating ordered pairs %d of %d'
          % (nm, N, len(closed), E, 100 * oi / tot, 100 * ou / tot, len(R), len(R) == (1 << N), sep, N * (N - 1)))
print('   L4098-4099 "the openness outruns the membership by two orders of magnitude": 64,804 / 732 = %.1f' % (64804 / 732))
print('   L4145-4146 "64,804 of 65,536": %s' % (64804 + 732 == 65536))
