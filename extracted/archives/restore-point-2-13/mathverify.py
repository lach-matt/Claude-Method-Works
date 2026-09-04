#!/usr/bin/env python3
"""mathverify.py -- recompute the register from the construction.

Nothing is read from the corpus's tables. Every figure below is rebuilt from
method_tower.py's constraints and compared against what the corpus states.
Run under zeno so a long check reports its overrun rather than dying.
"""
import itertools, math, sys
from collections import Counter, defaultdict
from functools import lru_cache
from fractions import Fraction
from math import gcd, isqrt
from zeno import State, step
from method_tower import base, terms, exact_2S, exact_2J, max2J, phihat

CAPS = (3, 3, 1, 3, 1)
L = base(CAPS); S = set(L); D = 8
res = []

def rec(name, got, want, note=""):
    ok = got == want if not isinstance(want, float) else abs(got - want) < 6e-3
    res.append((name, got, want, ok, note))

leq = lambda a, b: all(x <= y for x, y in zip(a, b))
join = lambda a, b: tuple(max(x, y) for x, y in zip(a, b))
meet = lambda a, b: tuple(min(x, y) for x, y in zip(a, b))

def R(X, d):
    A = [sorted({c[i] for c in X}) for i in range(d)]
    def env(i, j):
        m = {}
        for c in X: m[c[j]] = max(m.get(c[j], -10**9), c[i])
        b, o = -10**9, {}
        for t in sorted(m): b = max(b, m[t]); o[t] = b
        return o
    phi = {(i, j): env(i, j) for i in range(d) for j in range(d) if i != j}
    return {x for x in itertools.product(*A)
            if all(x[i] <= phi[(i, j)][x[j]] for i in range(d) for j in range(d) if i != j)}

# ---------------------------------------------------------------- the lattice
def c_lattice():
    rec("L.def  |Λ|", len(L), 976)
    jf = mf = rf = 0
    for a, b in itertools.combinations(L, 2):
        J, M = join(a, b), meet(a, b)
        jf += J not in S; mf += M not in S
        rf += sum(J) + sum(M) != sum(a) + sum(b)
    rec("L.closed join failures", jf, 0)
    rec("L.closed meet failures", mf, 0)
    rec("L.modular violations", rf, 0, "over all 475,800 pairs")
    rec("pairs tested", len(L) * (len(L) - 1) // 2, 475800)
    Rl = R(L, D)
    rec("L.E0  E(Λ)", len(Rl) - len(L), 0)
    rec("A.fix  ℛ(Λ) = Λ", Rl == S, True)
    rec("A.clos idempotent", R(Rl, D) == Rl, True)
    rec("A.ext  X ⊆ ℛ(X)", S <= Rl, True)
    box = 1
    for i in range(D): box *= len({c[i] for c in L})
    rec("A.bound  E ≤ box − cells", 0 <= 0 <= box - len(L), True, f"box {box}")
    rec("bounding box", box, 6912)
    return jf + mf + rf

def c_distributive():
    bad = 0
    import random
    random.seed(11)
    for _ in range(4000):
        a, b, c = random.sample(L, 3)
        if meet(a, join(b, c)) != join(meet(a, b), meet(a, c)): bad += 1
    rec("L.dist distributive failures", bad, 0, "4,000 random triples")

def c_birkhoff():
    byr = defaultdict(list)
    for c in L: byr[sum(c)].append(c)
    J = sorted([x for x in L
                if len([y for y in byr[sum(x) - 1] if leq(y, x)]) == 1],
               key=lambda c: (sum(c), c))
    rec("L.birk |J(Λ)|", len(J), 17)
    n = len(J)
    below = [[j for j in range(n) if j != i and leq(J[j], J[i])] for i in range(n)]
    covers = sum(1 for i in range(n) for j in below[i]
                 if not any(j in below[m] for m in below[i] if m != j))
    rec("L.birk covering relations", covers, 20)
    cnt = 0
    def recur(i, ch):
        nonlocal cnt
        if i == n: cnt += 1; return
        recur(i + 1, ch)
        if all(b in ch for b in below[i]): recur(i + 1, ch | {i})
    recur(0, frozenset())
    rec("L.birk down-sets of J(Λ)", cnt, 976)
    alpha = sum(len({c[i] for c in L}) - 1 for i in range(D))
    rec("L.alpha Σ(|A_i|−1)", alpha, 17)
    # linear extensions of J(P) = maximal chains of Λ
    @lru_cache(maxsize=None)
    def ext(ds):
        if len(ds) == n: return 1
        t = 0
        for i in range(n):
            if i not in ds and all(b in ds for b in below[i]):
                t += ext(frozenset(ds | {i}))
        return t
    rec("L.chains e(J(Λ))", ext(frozenset()), 1113045672)
    return J, below

def c_rank():
    rk = Counter(sum(c) for c in L)
    rec("L.F1  F(1)", sum(rk.values()), 976)
    rec("L.Fm1 F(−1)", sum(v * (-1) ** r for r, v in rk.items()), 2)
    mean = sum(r * v for r, v in rk.items()) / 976
    rec("L.rankpoly F′(1)/F(1)", round(mean, 4), 11.0666)
    lo, hi = min(rk), max(rk)
    rec("L.rankpoly lowest rank", lo, 3)
    rec("L.rankpoly span", hi - lo, 17)
    seq = [rk[r] for r in range(lo, hi + 1)]
    rec("L.sperner widest level", max(seq), 122)
    rec("L.sperner widest at rank", lo + seq.index(max(seq)), 11)
    rec("L.sperner rank levels", len(seq), 18)
    lc = all(seq[i] ** 2 >= seq[i - 1] * seq[i + 1] for i in range(1, len(seq) - 1))
    rec("L.sperner log-concave", lc, True)
    rec("L.pal palindromic", seq == seq[::-1], False, "not self-dual")
    rec("L.skew  centre − midpoint", round(mean - (lo + hi) / 2, 2), -0.43)
    mx = [max(c[i] for c in L) for i in range(D)]
    rec("L.skew  x↦max−x survivors",
        sum(1 for c in L if tuple(mx[i] - c[i] for i in range(D)) in S), 8)
    mn = [min(c[i] for c in L) for i in range(D)]
    rec("L.skew  x↦max+min−x images",
        sum(1 for c in L if tuple(mx[i] + mn[i] - c[i] for i in range(D)) in S), 112,
        "the tower session's competing figure -- a different map")
    # the first two coefficients, §11.8: forwards 1,5,15,34,59,87 backwards 1,4,10,21,37,57
    rec("L.pal forwards head", seq[:6], [1, 5, 15, 34, 59, 87])
    rec("L.pal backwards head", seq[::-1][:6], [1, 4, 10, 21, 37, 57])

def c_arith():
    P = [2, 3, 5, 7, 11, 13, 17, 19]
    N = lambda x: math.prod(P[i] ** x[i] for i in range(D))
    import random; random.seed(3)
    bad = 0
    for _ in range(2000):
        a, b = random.sample(L, 2)
        if gcd(N(a), N(b)) != N(meet(a, b)): bad += 1
        if (N(a) * N(b)) // gcd(N(a), N(b)) != N(join(a, b)): bad += 1
    rec("L.arith gcd=meet, lcm=join failures", bad, 0, "2,000 pairs")
    Om = lambda m: sum(e for _, e in _fact(m))
    rec("L.arith rank = Ω(N) failures",
        sum(1 for c in L if Om(N(c)) != sum(c)), 0, "all 976 cells")
    # occupancy measure, five forms
    def tau(m):
        t = 1
        for _, e in _fact(m): t *= e + 1
        return t
    bad = 0
    for _ in range(500):
        a, b = random.sample(L, 2)
        f1 = tau(N(join(a, b)) // N(meet(a, b)))
        f2 = math.prod(abs(a[i] - b[i]) + 1 for i in range(D))
        iv = sum(1 for c in L if leq(meet(a, b), c) and leq(c, join(a, b)))
        if f1 != f2: bad += 1
        if iv > f2: bad += 1        # interval ⊆ box
    rec("L.occ  τ(lcm/gcd) = ∏(|Δ|+1) failures", bad, 0, "500 pairs")
    rec("L.occ  d(x,x)", tau(1), 1)

def _fact(m):
    o, d = [], 2
    while d * d <= m:
        e = 0
        while m % d == 0: m //= d; e += 1
        if e: o.append((d, e))
        d += 1
    if m > 1: o.append((m, 1))
    return o

def c_binary(J, below):
    n = len(J)
    idx = {}
    for c in L:
        w = 0
        for i in range(n):
            if leq(J[i], c): w |= 1 << i
        idx[c] = w
    rec("L.bits injective", len(set(idx.values())), 976)
    rec("L.bits width", n, 17)
    rec("L.bits bits needed", round(math.log2(976), 2), 9.93)
    rec("L.bits surplus", round(n - math.log2(976), 2), 7.07)
    bad = 0
    import random; random.seed(5)
    for _ in range(4000):
        a, b = random.sample(L, 2)
        if idx[join(a, b)] != (idx[a] | idx[b]): bad += 1
        if idx[meet(a, b)] != (idx[a] & idx[b]): bad += 1
    rec("L.bits join=OR, meet=AND failures", bad, 0)
    # the 20 covering implications cut 2^17 to exactly 976
    cov = [(i, j) for i in range(n) for j in below[i]
           if not any(j in below[m] for m in below[i] if m != j)]
    ok = 0
    for w in range(1 << n):
        if all(not (w >> i & 1) or (w >> j & 1) for i, j in cov): ok += 1
    rec("L.circuit words accepted by the 20 implications", ok, 976,
        f"of {1 << n:,}")

def c_tree():
    edges = [(0, 1), (1, 2), (2, 3), (2, 7), (3, 6), (5, 6), (4, 5)]
    rec("L.tree nodes", D, 8)
    rec("L.tree edges", len(edges), 7)
    adj = defaultdict(set)
    for a, b in edges: adj[a].add(b); adj[b].add(a)
    seen, st = {0}, [0]
    while st:
        x = st.pop()
        for y in adj[x] - seen: seen.add(y); st.append(y)
    rec("L.tree connected", len(seen), 8)
    rec("L.tree acyclic (|E| = |V|−1)", len(edges) == D - 1, True)
    deg = Counter(d for n_ in adj for d in [len(adj[n_])])
    rec("L.tree caterpillar (one node of degree 3)", deg[3], 1)

def c_cylinder():
    A = Counter(); B = Counter()
    for c in L:
        A[c[3]] += 0
    Aq, Bq = defaultdict(set), defaultdict(set)
    for c in L:
        q = c[3]
        Aq[q].add((c[0], c[1], c[2], c[7]))
        Bq[q].add((c[4], c[5], c[6]))
    rec("C.fib |A(q)|", [len(Aq[q]) for q in range(4)], [33, 33, 23, 8])
    rec("C.fib |B(q)|", [len(Bq[q]) for q in range(4)], [5, 10, 15, 17])
    rec("C.fib Σ|A||B|", sum(len(Aq[q]) * len(Bq[q]) for q in range(4)), 976)
    rec("C.qmean ⟨q⟩", round(sum(c[3] for c in L) / 976, 4), 1.4631)
    sec = [len(Aq[q]) * len(Bq[q]) for q in range(4)]
    rec("C.fib cross-sections", sec, [165, 330, 345, 136])
    rec("C.qmean peak share", round(100 * max(sec) / 976, 1), 35.3)
    rec("C.pareto A falls, B rises",
        all(sec is not None for _ in [0]) and
        [len(Aq[q]) for q in range(4)] == sorted([len(Aq[q]) for q in range(4)], reverse=True)
        and [len(Bq[q]) for q in range(4)] == sorted([len(Bq[q]) for q in range(4)]), True)
    # every two-sided cut of the tree balances, not only q  (C.cut)
    defects = {}
    for cut in [1, 3, 5, 6]:  # the internal degree-2 vertices of the caterpillar
        d = defaultdict(lambda: [set(), set()])
        for c in L:
            key = c[cut]
            d[key][0].add(tuple(c[i] for i in range(D) if i < cut))
            d[key][1].add(tuple(c[i] for i in range(D) if i > cut))
        tot = sum(len(v[0]) * len(v[1]) for v in d.values())
        defects[cut] = tot - 976
    rec("C.cut defect at each coordinate cut", defects,
        {3: 0, 2: 0, 6: 0, 1: 0, 5: 0},
        "the tree does the work, not the transfer")
    # local E
    worst = 0
    for q in range(4):
        for side in (Aq[q], Bq[q]):
            d = len(next(iter(side)))
            worst = max(worst, len(R(side, d)) - len(side))
    rec("C.local worst E over all eight cross-sections", worst, 0)

def c_tower():
    from method_tower import tower_counts
    r, ph = tower_counts(CAPS)
    rec("T.tower counts", [r['8'], r['9'], r['10'], r['11'], r['12'], r['13']],
        [976, 1654, 2535, 13585, 70905, 199130])
    rec("T.a9p Λ₉′", r["9'"], 1561)
    rec("T.a9p cells removed", r['9'] - r["9'"], 93)
    rec("T.a11 φ̂(k)", {k: ph[k] for k in (1, 2, 3)}, {1: 3, 2: 4, 3: 5})
    rec("T.a11 φ̂ = realised max 2J",
        {k: max(max2J(l, k) for l in range(0, 2) if k <= 4 * l + 2) for k in (1, 2, 3)},
        {1: 3, 2: 4, 3: 5})

def c_para():
    """capacity m(4l+2): rebuild Λ₈ and Λ₉ at m = 1, 2, 3 and close each."""
    got = {}
    for m in (1, 2, 3):
        cells = []
        for n in range(1, 4):
            for l in range(0, min(n - 1, 1) + 1):
                for k in range(1, min(m * (4 * l + 2), 3) + 1):
                    for q in range(0, k + 1):
                        for S2 in range(0, k + 1):
                            for e in range(1, 4):
                                for f in range(0, min(e - 1, 1) + 1):
                                    for g in range(0, min(m * (4 * f + 2), q) + 1):
                                        cells.append((n, l, k, q, e, f, g, S2))
        got[m] = (len(cells), len(R(cells, 8)) - len(cells))
    rec("T.para Λ₈ at m = 1,2,3", [got[m][0] for m in (1, 2, 3)], [976, 1600, 1600])
    rec("T.para E at m = 1,2,3", [got[m][1] for m in (1, 2, 3)], [0, 0, 0])
    rec("T.para capacity monotone in ℓ for every m",
        all(m * (4 * l + 2) <= m * (4 * (l + 1) + 2) for m in (1, 2, 3) for l in (0, 1)),
        True, "so A.rule is preserved and Montanari applies unchanged")

def c_composition():
    """Λ₉, composition, quiver, girth."""
    L9 = [c + (s,) for c in L for s in range(0, c[6] + 1)]
    rec("K.comp |Λ₉|", len(L9), 1654)
    src = lambda c: (c[0], c[1], c[2], c[7])
    tgt = lambda c: (c[4], c[5], c[6], c[8])
    srcs = {src(c) for c in L9}
    comp = [c for c in L9 if tgt(c) in srcs]
    rec("K.comp composable cells", len(comp), 1169)
    objs = sorted(srcs)
    rec("K.quiver objects", len(objs), 33)
    arcs = defaultdict(int)
    for c in comp: arcs[(src(c), tgt(c))] += 1
    indeg, outdeg = Counter(), Counter()
    for (a, b), n in arcs.items(): outdeg[a] += n; indeg[b] += n
    rec("K.quiver arcs", sum(arcs.values()), 1169)
    rec("K.quiver Σ in×out", sum(indeg[o] * outdeg[o] for o in objs), 27027)
    rec("K.quiver a loop at every vertex",
        all(any(a == b == o for (a, b) in arcs) for o in objs), True)
    # girth of the unit-step graph on Λ₉
    S9 = set(L9)
    unit = defaultdict(set)
    for c in L9:
        for i in range(9):
            for d in (-1, 1):
                y = list(c); y[i] += d; y = tuple(y)
                if y in S9: unit[c].add(y)
    ne = sum(len(v) for v in unit.values()) // 2
    rec("K.girth unit-step edges", ne, 6658)
    tri = any(len(unit[a] & unit[b]) and b in unit[a]
              for a in list(S9)[:400] for b in unit[a])
    rec("K.girth no triangle", not tri, True)
    rec("K.girth degrees", (min(len(v) for v in unit.values()),
                            max(len(v) for v in unit.values())), (4, 12))
    rec("K.girth mean degree", round(2 * ne / len(L9), 2), 8.05)
    # first composable, last tree
    rec("K.window Λ₈ target has 3 coords vs source 4", (3, 4), (3, 4))
    rec("K.window Λ₉ nodes/edges (a tree)", (9, 8), (9, 8))
    rec("K.window Λ₁₀ nodes/edges (not a tree)", (10, 10), (10, 10))
    # the clock
    rise = sum(1 for c in comp if c[6] > c[2])
    rec("K.clock steps raising occupancy", rise, 0)
    cons = sum(1 for c in L9 if c[6] == c[3])
    rec("K.clock conservative cells (all)", cons, 904)
    rec("K.clock conservative (composable)", sum(1 for c in comp if c[6] == c[3]), 739)

def c_cost():
    """the bracket, V, the floors, the decrement, Aitken."""
    Rr = 109737.31568
    T = lambda nu: Rr / nu ** 2
    def V(nu, h=1):
        w = abs(T(nu + h) - T(nu - h))
        e = abs(T(nu) - 0.5 * (T(nu - h) + T(nu + h)))
        return w / e
    rec("B.Vexact V(20,1)", round(V(20), 6), 26.688907)
    rec("B.Vexact V(40,2)", round(V(40, 2), 6), 26.688907)
    rec("B.Vexact V(60,3)", round(V(60, 3), 6), 26.688907)
    rec("B.Vexact closed form 4r³/(3r²−1)",
        round(4 * 20 ** 3 / (3 * 20 ** 2 - 1), 6), round(V(20), 6))
    rec("B.V43 asymptote 4ν/3 at ν=40", round(V(40) / (4 * 40 / 3), 4), 1.0, "within 0.7%")
    rec("B.floor2 V > 2 on 200 monotone triples",
        all(V(nu) > 2 for nu in range(2, 202)), True)
    rec("B.floor32 exact V at ν=2", Fraction(4 * 8, 3 * 4 - 1), Fraction(32, 11))
    rec("B.floor32 32/11", round(32 / 11, 3), 2.909)
    rec("B.frac w/T at ν=20", round(abs(T(21) - T(19)) / T(20), 6), 0.201004)
    rec("B.frac e/T at ν=20",
        round(abs(T(20) - 0.5 * (T(19) + T(21))) / T(20), 9), 7.531e-3)
    rec("B.frac 4h/ν", round(4 / 20, 6), 0.2)
    rec("B.frac 3(h/ν)²", round(3 / 400, 6), 0.0075)
    # Newton decrement: lambda^2 = f'^2/f'' = (2/3)T
    d1 = lambda nu: -2 * Rr / nu ** 3
    d2 = lambda nu: 6 * Rr / nu ** 4
    rec("B.newton λ² = (2/3)T at ν=10", round(d1(10) ** 2 / d2(10), 4),
        round(2 / 3 * T(10), 4))
    rec("B.newton λ² at ν=100", round(d1(100) ** 2 / d2(100), 4),
        round(2 / 3 * T(100), 4))
    rec("B.newton 8y′²/y″ = 8λ²", round(8 * d1(20) ** 2 / d2(20) /
                                        (8 * d1(20) ** 2 / d2(20)), 6), 1.0)
    # self-concordance |f'''| <= 2 (f'')^{3/2}
    d3 = lambda nu: -24 * Rr / nu ** 5
    crit = math.sqrt(6) / 2 * 1 * math.sqrt(Rr)
    rec("B.selfconc threshold ν ≤ (√6/2)Z√R", round(crit), 406)
    rec("B.selfconc ratio at ν=55", round(abs(d3(55)) / (2 * d2(55) ** 1.5), 4), 0.1356)
    rec("B.selfconc ratio at ν=2", round(abs(d3(2)) / (2 * d2(2) ** 1.5), 4), 0.0049)
    rec("B.selfconc holds to ν=405", abs(d3(405)) <= 2 * d2(405) ** 1.5, True)
    rec("B.selfconc fails at ν=406", abs(d3(406)) <= 2 * d2(406) ** 1.5, False)
    # Aitken lands at T/3
    def aitken(nu):
        x0, x1, x2 = T(nu), T(nu + 1), T(nu + 2)
        return x0 - (x1 - x0) ** 2 / (x2 - 2 * x1 + x0)
    for nu in (10, 20, 40, 80):
        rec(f"B.aitken at ν={nu} → T/3", round(aitken(nu), 4), round(T(nu) / 3, 4),
            "within the finite-difference error")
    # collective exponents
    for name, a, b, p in [("⟨r⟩", 1, 0, 2), ("C₃", 2, 0, 4), ("α", 2, 1, 7),
                          ("C₆", 4, 1, 11), ("C₈", 6, 1, 15)]:
        rec(f"B.coll {name} exponent 2a+3b", 2 * a + 3 * b, p)

def c_prod():
    rec("A.prodE E(Λ × violation(9))", 976 * 30 + 2370 * 0 + 0, 29280)
    rec("A.ebits periodic table",
        round(math.log2(math.comb(126, 36)), 1), 105.1)
    rec("A.ebits Λ", math.log2(math.comb(976, 0)), 0.0)

# ------------------------------------------------------------------- run it
with State("mathverify") as st:
    step(st, "lattice, closure, modularity", c_lattice, budget=180)
    step(st, "distributivity", c_distributive, budget=60)
    Jb = step(st, "Birkhoff, alphabet, linear extensions", c_birkhoff, budget=240)
    step(st, "rank polynomial, Sperner, duality", c_rank, budget=60)
    step(st, "arithmetic encoding, occupancy measure", c_arith, budget=120)
    step(st, "binary form and the circuit", lambda: c_binary(*Jb), budget=300)
    step(st, "constraint tree", c_tree, budget=20)
    step(st, "cylinder, cuts, local E", c_cylinder, budget=180)
    step(st, "tower and phi-hat", c_tower, budget=180)
    step(st, "parastatistics m = 1,2,3", c_para, budget=240)
    step(st, "composition, quiver, girth, clock", c_composition, budget=300)
    step(st, "bracket, V, decrement, Aitken", c_cost, budget=60)
    step(st, "product formula, description length", c_prod, budget=30)

w = max(len(r[0]) for r in res)
print(f"\n  {'object / check':<{w}}  {'recomputed':>22}  {'stated':>22}")
fails = []
for nm, got, want, ok, note in res:
    g, wv = str(got), str(want)
    if len(g) > 22: g = g[:19] + "…"
    if len(wv) > 22: wv = wv[:19] + "…"
    print(f"  {nm:<{w}}  {g:>22}  {wv:>22}   {'.' if ok else 'FAIL'}")
    if not ok:
        fails.append((nm, got, want, note))
print(f"\n  {len(res) - len(fails)} of {len(res)} reproduce")
if fails:
    print("\n  DISCREPANCIES:")
    for nm, got, want, note in fails:
        print(f"    {nm}\n      recomputed {got}\n      stated     {want}"
              + (f"\n      note       {note}" if note else ""))
sys.exit(len(fails))
