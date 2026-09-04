#!/usr/bin/env python3
# r3-q5e-measure.py — R3 (Q5 pass 5): the chat-58 batch 2c slip B2-C3 re-derived with the standard library. Chat 58's
# mc11.py (its direct count is numpy-vectorised) and mc11b.py (imports numpy) are followed definition by definition —
# the same closed form, the same eight random intervals (random.seed(1106), random.sample), the same exhaustive pass over
# every unordered pair and singleton, the same leaf-peeling variable elimination with the seven edge predicates, the
# same cycle witness 2S ≤ q+1 with the eight-term sieve and the seed-7 exhibit — so that each figure is comparable to the
# pack's run, also recorded (W-231). The direct count |box ∩ Λ| is by bitsets (one Python integer per coordinate value),
# which the pack did with numpy. Λ₈ from the seated tower-2.py; the cap-parameterised lattice is tower-2's loop with
# caps in place of its constants. Slip B3-C1's figures are mc12.py's, which is standard-library and is seated as it is.
import os, sys, importlib.util, io, contextlib, random, itertools
from collections import Counter
H = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('tower2', os.path.join(H, 'tower-2.py')); T2 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(T2)
FAIL = []
def check(tag, got, exp):
    ok = got == exp; print('   %-70s %-24s %s' % (tag, repr(got)[:24], 'OK' if ok else 'EXPECTED ' + repr(exp)))
    if not ok: FAIL.append(tag)
def lattice(capn, cape, capl, capk, capf):
    out = []
    for n in range(1, capn + 1):
        for l in range(0, min(capl, n - 1) + 1):
            for k in range(1, min(capk, 4 * l + 2) + 1):
                for q in range(0, k + 1):
                    for e in range(1, cape + 1):
                        for f in range(0, min(capf, e - 1) + 1):
                            for g in range(0, min(4 * f + 2, q) + 1):
                                for S2 in range(0, k + 1):
                                    out.append((n, l, k, q, e, f, g, S2))
    return out
class Direct:
    """|box ∩ Λ| by bitsets: for coordinate i and value v, GE[i][v] is the set of cells with xᵢ ≥ v, LE[i][v] with xᵢ ≤ v."""
    def __init__(self, cells):
        self.cells = cells; m = [max(c[i] for c in cells) for i in range(8)]
        self.GE = [[0] * (m[i] + 2) for i in range(8)]; self.LE = [[0] * (m[i] + 2) for i in range(8)]
        for idx, c in enumerate(cells):
            b = 1 << idx
            for i in range(8):
                for v in range(0, c[i] + 1): self.GE[i][v] |= b
                for v in range(c[i], m[i] + 1): self.LE[i][v] |= b
        self.m = m
    def __call__(self, lo, hi):
        acc = None
        for i in range(8):
            if lo[i] > self.m[i]: return 0
            g = self.GE[i][lo[i]]; l = self.LE[i][min(hi[i], self.m[i])]; x = g & l
            acc = x if acc is None else acc & x
            if not acc: return 0
        return bin(acc).count('1')
def leaf_S2(lo, hi, k): return max(0, min(hi[7], k) - lo[7] + 1)
def leaf_g(lo, hi, q, f): return max(0, min(hi[6], q, 2 * (2 * f + 1)) - lo[6] + 1)
def factorised(lo, hi):
    tot = 0
    for n in range(lo[0], hi[0] + 1):
        for l in range(lo[1], hi[1] + 1):
            if not (l <= n - 1): continue
            for k in range(lo[2], hi[2] + 1):
                if not (1 <= k <= 2 * (2 * l + 1)): continue
                for q in range(lo[3], hi[3] + 1):
                    if not (q <= k): continue
                    for e in range(lo[4], hi[4] + 1):
                        for f in range(lo[5], hi[5] + 1):
                            if not (f <= e - 1): continue
                            tot += leaf_S2(lo, hi, k) * leaf_g(lo, hi, q, f)
    return tot
def meet_join(x, y): return tuple(min(a, b) for a, b in zip(x, y)), tuple(max(a, b) for a, b in zip(x, y))
EDGES = [(0, 1, lambda n, l: l <= n - 1), (1, 2, lambda l, k: 1 <= k <= 4 * l + 2), (2, 3, lambda k, q: q <= k), (3, 6, lambda q, g: g <= q),
         (5, 6, lambda f, g: g <= 4 * f + 2), (4, 5, lambda e, f: f <= e - 1), (2, 7, lambda k, S2: S2 <= k)]
def peel_count(lo, hi, edges, nvars=8):
    dom = {i: list(range(lo[i], hi[i] + 1)) for i in range(nvars)}
    factors = [((i, j), (lambda p: (lambda a: 1 if p(*a) else 0))(pred)) for i, j, pred in edges]
    maxar = 0; remaining = set(range(nvars))
    while remaining:
        deg = {v: len(set(u for sc, _ in factors if v in sc for u in sc) - {v}) for v in remaining}
        v = min(remaining, key=lambda x: (deg[x], x))
        inv = [(sc, f) for sc, f in factors if v in sc]; rest = [(sc, f) for sc, f in factors if v not in sc]
        newscope = tuple(sorted(set(u for sc, _ in inv for u in sc) - {v})); maxar = max(maxar, len(newscope)); table = {}
        for assign in itertools.product(*[dom[u] for u in newscope]):
            ctx = dict(zip(newscope, assign)); s = 0
            for val in dom[v]:
                ctx[v] = val; prod = 1
                for sc, f in inv:
                    prod *= f(tuple(ctx[u] for u in sc))
                    if prod == 0: break
                s += prod
            table[assign] = s
        rest.append((newscope, (lambda t, sc: (lambda a: t[a]))(table, newscope))); factors = rest; remaining.discard(v)
    tot = 1
    for sc, f in factors: assert sc == (); tot *= f(())
    return tot, maxar

cells = T2.L8(); check('|Λ₈| from tower-2.py, equal to lattice(3,3,1,3,1) in order', (len(cells), lattice(3, 3, 1, 3, 1) == cells), (976, True))
D8 = Direct(cells)
print('== the eight random intervals (mc11.py, random.seed(1106))')
random.seed(1106); ok8 = 0
for t in range(8):
    x, y = random.sample(cells, 2); lo, hi = meet_join(x, y); d, fct = D8(lo, hi), factorised(lo, hi)
    box = 1
    for i in range(8): box *= hi[i] - lo[i] + 1
    print('   lo=%s hi=%s  direct=%d factorised=%d box=%d void=%d  %s' % (lo, hi, d, fct, box, box - d, 'OK' if d == fct else 'FAIL')); ok8 += d == fct
check('eight random intervals reproduced', ok8, 8)
print('== exhaustive over every unordered pair and singleton')
boxes = Counter()
for i in range(len(cells)):
    ci = cells[i]
    for j in range(i, len(cells)): boxes[meet_join(ci, cells[j])] += 1
npairs = sum(boxes.values()); check('pairs + singletons', npairs, 476776); check('distinct boxes', len(boxes), 116138)
fails = 0; voidpairs = 0
for (lo, hi), mult in boxes.items():
    d = D8(lo, hi)
    if d != factorised(lo, hi): fails += 1
    box = 1
    for t in range(8): box *= hi[t] - lo[t] + 1
    if box - d > 0: voidpairs += mult
check('factorised ≠ direct', fails, 0); check('pairs whose box has void > 0', voidpairs, 340929)
check('void-free fraction (pairs + singletons), four decimals', round((npairs - voidpairs) / npairs, 4), 0.2849)
print('== leaf-peeling, width measured (mc11b.py stage a, random.seed(1106), 100 boxes per cap)')
random.seed(1106); ar = {}
for cap in [(3, 3, 1, 3, 1), (4, 4, 2, 5, 1), (5, 5, 2, 6, 1)]:
    cs = lattice(*cap); Dc = Direct(cs); f_ = 0; widths = set()
    for t in range(100):
        x, y = random.sample(cs, 2); lo, hi = meet_join(x, y); c, w = peel_count(lo, hi, EDGES); widths.add(w)
        if c != Dc(lo, hi): f_ += 1
    ar[cap] = (len(cs), f_, sorted(widths)); print('   cap %s |Λ|=%d: 100 random boxes, peel≠direct: %d, max message arity seen: %s' % (cap, len(cs), f_, sorted(widths)))
check('cells at the three caps', [ar[c][0] for c in ar], [976, 8847, 25748]); check('peel = direct everywhere, message arity 1', all(v[1] == 0 and v[2] == [1] for v in ar.values()), True)
print('== the cycle witness: 2S ≤ q+1 closes the triangle k–q–2S (mc11b.py stage b, 40 boxes)')
random.seed(1106); close = (3, 7, lambda q, S2: S2 <= q + 1); cells_c = [z for z in cells if close[2](z[3], z[7])]; Dc = Direct(cells_c)
check('|Λ ∩ {2S ≤ q+1}| (the constraint is not redundant)', len(cells_c), 911)
E2 = EDGES + [close]; f_ = 0; widths = set(); tree_wrong = 0; sieve_ok = 0; NB = 40
for t in range(NB):
    x, y = random.sample(cells_c, 2); lo, hi = meet_join(x, y); d = Dc(lo, hi); c, w = peel_count(lo, hi, E2); widths.add(w)
    if c != d: f_ += 1
    tri = [EDGES[2], EDGES[6], close]; other = [e for e in EDGES if e not in tri]
    pts = [z for z in itertools.product(*[range(lo[i], hi[i] + 1) for i in range(8)]) if all(p(z[i], z[j]) for i, j, p in other) and z[0] >= 1 and z[4] >= 1 and z[2] >= 1]
    sieve = 0
    for r in range(4):
        for T in itertools.combinations(range(3), r):
            sieve += (-1) ** r * sum(1 for z in pts if all(not tri[a][2](z[tri[a][0]], z[tri[a][1]]) for a in T))
    if D8(lo, hi) != d: tree_wrong += 1
    if sieve == d: sieve_ok += 1
check('peel = direct with the cycle', f_, 0); check('max message arity with the cycle', sorted(widths), [2])
check('tree-style count wrong on', (tree_wrong, NB), (9, 40)); check('eight-term sieve over the triangle right on', (sieve_ok, NB), (40, 40))
random.seed(7)
while True:
    x, y = random.sample(cells_c, 2); lo, hi = meet_join(x, y); d = Dc(lo, hi); tc = D8(lo, hi)
    if tc != d: break
print('   exhibit: lo=%s hi=%s: |box∩Λ|=%d (tree count), |box∩Λ\'|=%d; correction = %d' % (lo, hi, tc, d, tc - d))
check('the exhibit', (lo, hi, tc, d, tc - d), ((2, 1, 2, 0, 2, 0, 0, 0), (3, 1, 3, 2, 3, 1, 1, 3), 280, 240, 40))
print('\n   integrity checks: %s' % ('ALL OK' if not FAIL else 'FAILED: ' + '; '.join(FAIL)))
sys.exit(1 if FAIL else 0)
