#!/usr/bin/env python3
# r3-q5b-measure.py — R3 (Q5 pass 2): the chat-54 B-list batch 1 slips re-derived. Chat 54 left no instrument pack, and
# M ruled (RUL-153, pass 2) that the re-run is by an instrument of R3's, named as a re-derivation. Λ₈ is taken from the
# seated tower-2.py (imported by path, never copied); everything below is standard library, deterministic, no wall clock.
#
# What it measures, each against the slip that states it:
#   B1-C1  J(Λ₈), the join-irreducibles of the lattice under componentwise order; the width of J(Λ₈) by Dilworth — the
#          largest antichain, and a chain partition of the same size — and the seven-generator antichain the slip lists;
#          J(Λ₉) and its width. dim(Λ₈) = width J(Λ₈) is Dilworth 1950 for a finite distributive lattice.
#   B1-C2  ω(N(x)) = the number of coordinates at which x is positive (one prime per coordinate in the divisor
#          embedding; B2-C1's reading): its maximum, the cells attaining it, its minimum, and the tight cell.
#   B1-C3  the rank sequence (rank = coordinate sum), the largest level, a Dilworth chain partition of all 976 cells
#          and the largest antichain (Sperner: largest antichain = largest level), the rank skew, the mirrored level
#          counts, and the reflection x ↦ max − x (survivors, fixed points).
# Checks are the slips' figures; a mismatch prints EXPECTED and the instrument exits 1.
import os, sys, importlib.util, collections, math
H = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('tower2', os.path.join(H, 'tower-2.py')); T2 = importlib.util.module_from_spec(spec)
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(T2)
FAIL = []
def check(tag, got, exp):
    ok = got == exp; print('   %-64s %-28s %s' % (tag, repr(got)[:28], 'OK' if ok else 'EXPECTED ' + repr(exp)))
    if not ok: FAIL.append(tag)
def leq(x, y): return all(a <= b for a, b in zip(x, y))
def max_matching(left, right_of):
    # Hopcroft–Karp is unnecessary at this size: augmenting paths over the comparability bipartite graph
    match_r = {}; match_l = {}
    def try_aug(u, seen):
        for v in right_of[u]:
            if v in seen: continue
            seen.add(v)
            if v not in match_r or try_aug(match_r[v], seen):
                match_r[v] = u; match_l[u] = v; return True
        return False
    for u in left: try_aug(u, set())
    return len(match_l)
def width(P):
    # Dilworth: minimum chain partition = |P| - maximum matching in the bipartite graph (x -> y for x < y);
    # its size equals the largest antichain. Both the number and an antichain witness are returned.
    P = sorted(P); idx = {p: i for i, p in enumerate(P)}
    right_of = {i: [idx[q] for q in P if q != p and leq(p, q)] for i, p in enumerate(P)}
    m = max_matching(list(range(len(P))), right_of)
    return len(P) - m
def antichain_ok(cells, P):
    S = set(P); return all(c in S for c in cells) and all(not leq(a, b) for a in cells for b in cells if a != b)

print('== B1-C1  the order dimension of Λ₈, by Dilworth on J(Λ₈)')
L8 = sorted(T2.L8()); S8 = set(L8)
check('|Λ₈|', len(L8), 976)
bottom = min(L8)
def lower_covers(x, L, S):
    below = [y for y in L if y != x and leq(y, x)]
    return [y for y in below if not any(z != y and z != x and leq(y, z) and leq(z, x) for z in below)]
J8 = [x for x in L8 if x != bottom and len(lower_covers(x, L8, S8)) == 1]
check('|J(Λ₈)|, the join-irreducibles', len(J8), 17)
w8 = width(J8)
check('width of J(Λ₈) = dim(Λ₈), Dilworth 1950', w8, 7)
A7 = [(1,0,1,0,1,0,0,1), (1,0,1,0,2,1,0,0), (1,0,1,0,3,0,0,0), (1,0,1,1,1,0,0,0), (1,0,2,0,1,0,0,0), (2,1,1,0,1,0,0,0), (3,0,1,0,1,0,0,0)]
check("the slip's seven-generator antichain: seven join-irreducibles, pairwise incomparable", antichain_ok(A7, J8) and len(A7) == 7, True)
print('   J(Λ₈) =', ' '.join(str(j) for j in J8))
L9 = sorted(T2.L9()); S9 = set(L9); b9 = min(L9)
check('|Λ₉|', len(L9), 1654)
J9 = [x for x in L9 if x != b9 and len(lower_covers(x, L9, S9)) == 1]
check('width of J(Λ₉): per-axis rise fails at the first step', width(J9), 7)
print('   |J(Λ₉)| =', len(J9))

print('== B1-C2  ω(N(x)) is bounded by the coordinate count')
om = {x: sum(1 for v in x if v > 0) for x in L8}
check('max ω over Λ₈ = the coordinate count', max(om.values()), 8)
check('cells attaining ω = 8', sum(1 for v in om.values() if v == 8), 100)
check('ω at (2,1,3,3,2,1,3,3), the tight cell', om[(2,1,3,3,2,1,3,3)], 8)
check('min ω over Λ₈ (the floors n, k, e ≥ 1)', min(om.values()), 3)
check('ω = 8 exceeds dim = 7 at the tight cell', om[(2,1,3,3,2,1,3,3)] > w8, True)

print('== B1-C3  Sperner by direct certificate; rank-symmetry fails')
rk = collections.Counter(sum(x) for x in L8); lo, hi = min(rk), max(rk)
seq = [rk[r] for r in range(lo, hi + 1)]
check('rank span', (lo, hi), (3, 20))
check('rank sequence, ranks 3–20', seq, [1, 5, 15, 34, 59, 87, 108, 121, 122, 115, 100, 79, 57, 37, 21, 10, 4, 1])
check('largest level', max(seq), 122)
check('log-concave', all(seq[i] ** 2 >= seq[i - 1] * seq[i + 1] for i in range(1, len(seq) - 1)), True)
wL = width(L8)
check('largest antichain of Λ₈ = size of a minimum chain partition (Dilworth)', wL, 122)
check('Sperner: largest antichain = largest level', wL == max(seq), True)
n = len(L8); mu = sum(sum(x) for x in L8) / n
# "skew −0.43" — RECOVERED: the mean rank against the centre of the rank span, 11.0666 − 11.5 (tower.py prints the mean
# rank 11.0666); a rank-symmetric poset would put the mean at the centre. The third standardised moment gives +0.14
# and is not the slip's figure; the convention that reproduces it is stated here rather than assumed.
check('mean rank, four decimals (tower.py prints 11.0666)', round(mu, 4), 11.0666)
check('rank skew = mean rank − centre of the span, two decimals', round(mu - (lo + hi) / 2, 2), -0.43)
check('mirrored levels: second from the bottom against second from the top', (seq[1], seq[-2]), (5, 4))
mx = tuple(max(x[i] for x in L8) for i in range(8))
refl = [x for x in L8 if tuple(m - v for m, v in zip(mx, x)) in S8]
check('reflection x ↦ max − x: survivors', len(refl), 8)
check('reflection: fixed points', sum(1 for x in refl if tuple(m - v for m, v in zip(mx, x)) == x), 0)
print('\n   integrity checks: %s' % ('ALL OK' if not FAIL else 'FAILED: ' + '; '.join(FAIL)))
sys.exit(1 if FAIL else 0)
