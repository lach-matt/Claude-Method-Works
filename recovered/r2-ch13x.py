#!/usr/bin/env python3
# r2-ch13x.py — chat 89 — COMPUTABLE batch for the Chapter 20 section read (main L5551-L5596).
# Claims measured: 20.1's Chapter-1 timing ratio; 20.2's "Six agree on Lambda at 976 cells,
# and ten of their combinations hold"; 20.3's parity congruence at E = 750, the spectroscopic
# relabelling at E = 0, and 17.3's criterion generalised to "a congruence is excluded exactly
# when the set it defines has a hole in the attained range".
# Deterministic; prints no wall-clock time.

import importlib.util, os, itertools, math
H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib)
T = r2lib.load_tower()

CAPS = (3, 3, 1, 3, 1)          # (n_max, e_max, l_max, k_max, f_max)
NAMES = ['n', 'l', 'k', 'q', 'e', 'f', 'g', '2S', "2S'"]
IL, IF, IS, ISP = 1, 5, 7, 8    # l, f, 2S, 2S'


def E(X):
    """E(X) = |R(X)| - |X|, R the recovered-bounds closure of section 6.1 (r2lib.Rset)."""
    X = set(map(tuple, X))
    return len(r2lib.Rset(X)) - len(X)


def convex_in(T_, rng):
    """T_ is convex inside the attained range rng (both sets of ints)."""
    hit = sorted(v for v in rng if v in T_)
    if not hit:
        return True
    lo, hi = hit[0], hit[-1]
    return all((v in T_) for v in rng if lo <= v <= hi)


print('=== 0. controls: the tower, and E of a closed index ===')
L8 = [tuple(c) for c in T.L8()]
L9m = [tuple(c) for c in T.L9()]
L9b = [tuple(c) for c in r2lib.build9(CAPS)]
print('|L8| =', len(L8), '  expected 976   ', 'OK' if len(L8) == 976 else 'FAIL')
print('|L9| =', len(L9m), '  expected 1,654 ', 'OK' if len(L9m) == 1654 else 'FAIL')
print('tower-2 L9 == r2lib.build9(caps):', set(L9m) == set(L9b))
e9 = E(L9m)
print('E(L9) =', e9, '  expected 0 (a closed index) ', 'OK' if e9 == 0 else 'FAIL')

print()
print('=== 1. 20.3 - the parity rule, its set, and its E ===')
rng_d = sorted({c[IF] - c[IL] for c in L9m})
print('attained range of d = f - l on L9:', rng_d)
eq1 = [c for c in L9m if abs(c[IF] - c[IL]) == 1]          # |dl| = 1, as 12.11.8 states it
cong = [c for c in L9m if (c[IF] - c[IL]) % 2 == 1]        # |dl| = gamma (mod 2), as 20.3 states it
pm1 = [c for c in L9m if (c[IF] - c[IL]) in (-1, 1)]       # d^-1({-1,+1}), the 12.11.8 table row
print('|{|dl| = 1}|      =', len(eq1), ' expected 840 ', 'OK' if len(eq1) == 840 else 'FAIL')
print('|{dl = 1 (mod 2)}|=', len(cong))
print('|d^-1({-1,+1})|   =', len(pm1))
print('the three descriptions name the same cells:',
      set(eq1) == set(cong) == set(pm1))
e_par = E(eq1)
print('E({|dl| = 1}) =', e_par, ' expected 750 ', 'OK' if e_par == 750 else 'FAIL')
print('hole: 0 lies in the attained range and is excluded ->',
      0 in rng_d and 0 not in {c[IF] - c[IL] for c in eq1})

print()
print('=== 2. 20.3 - the spectroscopic naming, and whether it reaches E = 0 ===')
MULT = {0: 'M1', 1: 'E1', 2: 'E2', 3: 'E3'}                # 12.11.8 L3557
realised = sorted({MULT[abs(c[IF] - c[IL])] for c in L9m})
print('multipoles realised on L9 under 12.11.8 map:', realised)
print("20.3 names the naming 'E1, M1, E2, M2'; M2 is not in 12.11.8's map at all:",
      'M2' not in MULT.values())
by_mult = [c for c in L9m if MULT[abs(c[IF] - c[IL])] == 'E1']
print("|{multipole = E1}| =", len(by_mult), " same cells as {|dl| = 1}:", set(by_mult) == set(eq1))
print("E({multipole = E1}) =", E(by_mult), " -- the same set, so the same E")
# E is a function of the cell set: exhibit it under every relabelling of the value alphabet
Es = set()
for perm in itertools.permutations(rng_d):
    relab = {v: p for v, p in zip(rng_d, perm)}
    Y = [c for c in L9m if relab[c[IF] - c[IL]] in {relab[-1], relab[1]}]
    Es.add((len(Y), E(Y)))
print('over all', math.factorial(len(rng_d)), 'relabellings of the value alphabet,',
      '(|X|, E) takes the values', sorted(Es))
print('=> E is invariant under renaming the values: a naming cannot move E off 750.')

print()
print("=== 3. Chapter 21 L5606's second naming, the convex band |dl| <= 1 ===")
band = [c for c in L9m if abs(c[IF] - c[IL]) <= 1]
print('|{|dl| <= 1}| =', len(band), ' |L9| =', len(L9m),
      ' the band is the whole index:', set(band) == set(L9m))
print('E({|dl| <= 1}) =', E(band))
print('cells excluded by the band:', len(L9m) - len(band))

print()
print('=== 4. 12.11.8 control - the spin rule ===')
spin = [c for c in L9m if c[ISP] - c[IS] == 0]
print('|{2S\' - 2S = 0}| =', len(spin), ' expected 526 ', 'OK' if len(spin) == 526 else 'FAIL')
print("E({2S' - 2S = 0}) =", E(spin), ' expected 0 ', 'OK' if E(spin) == 0 else 'FAIL')

print()
print('=== 5. 20.3 / 17.3 - "excluded exactly when the set has a hole in the attained range" ===')
print('exhaustive over every unordered coordinate pair of L9 and every subset of the')
print('attained range of their difference; convexity in range vs closure of the preimage.')
rows = []
for i, j in itertools.combinations(range(9), 2):
    dv = {c: c[i] - c[j] for c in L9m}
    rng = sorted(set(dv.values()))
    if len(rng) < 2 or len(rng) > 6:
        continue
    for r in range(1, len(rng) + 1):
        for Tsub in itertools.combinations(rng, r):
            Ts = set(Tsub)
            X = [c for c in L9m if dv[c] in Ts]
            if not X or len(X) == len(L9m):
                continue
            cvx = convex_in(Ts, rng)
            closed = (E(X) == 0)
            rows.append((NAMES[i], NAMES[j], tuple(sorted(Ts)), cvx, closed, len(X), E(X)))
agree = [r for r in rows if r[3] == r[4]]
disagree = [r for r in rows if r[3] != r[4]]
print('preimages tested:', len(rows))
print('convex-in-range and closed agree on:', len(agree))
print('disagree on:', len(disagree))
print('  convex but NOT closed:', sum(1 for r in disagree if r[3]))
print('  closed but NOT convex:', sum(1 for r in disagree if not r[3]))
for r in sorted(disagree)[:12]:
    print('   ', r[0], '-', r[1], 'T =', r[2], 'convex' if r[3] else 'non-convex',
          'closed' if r[4] else 'not closed', '|X| =', r[5], 'E =', r[6])

print()
print('=== 6. the congruence case specifically ===')
crows = []
for i, j in itertools.combinations(range(9), 2):
    dv = {c: c[i] - c[j] for c in L9m}
    rng = sorted(set(dv.values()))
    if len(rng) < 2:
        continue
    for m in range(2, max(3, len(rng) + 1)):
        for gam in range(m):
            Ts = {v for v in rng if v % m == gam}
            if not Ts or Ts == set(rng):
                continue
            X = [c for c in L9m if dv[c] in Ts]
            if not X or len(X) == len(L9m):
                continue
            crows.append((NAMES[i], NAMES[j], m, gam, convex_in(Ts, rng), E(X) == 0, len(X), E(X)))
cd = [r for r in crows if r[4] != r[5]]
print('congruence preimages tested:', len(crows))
print('hole-in-range and exclusion agree on:', len(crows) - len(cd), '  disagree on:', len(cd))
for r in sorted(cd)[:12]:
    print('   ', r[0], '-', r[1], 'mod', r[2], 'res', r[3],
          'convex' if r[4] else 'non-convex', 'closed' if r[5] else 'not closed',
          '|X| =', r[6], 'E =', r[7])

print()
print('=== 7. 11.1.1 - the seventh language, and how many bits it needs ===')
S8 = set(L8)
ji = [c for c in L8 if sum(1 for b in L8 if b != c and all(x <= y for x, y in zip(b, c))
                           and any(x < y for x, y in zip(b, c))) >= 0]


def covers_below(c):
    below = [b for b in L8 if b != c and all(x <= y for x, y in zip(b, c))]
    return below


joinirr = []
for c in L8:
    below = covers_below(c)
    if not below:
        continue
    jn = tuple(max(v) for v in zip(*below))
    if jn != c:
        joinirr.append(c)
meetirr = []
for c in L8:
    above = [b for b in L8 if b != c and all(x >= y for x, y in zip(b, c))]
    if not above:
        continue
    mt = tuple(min(v) for v in zip(*above))
    if mt != c:
        meetirr.append(c)
bottom = [c for c in L8 if not covers_below(c)]
print('join-irreducible cells of L8 (bottom excluded):', len(joinirr))
print('meet-irreducible cells of L8 (top excluded)   :', len(meetirr))
print('bottom cells (no cell strictly below)         :', len(bottom))
print("11.1.1 prints 'the 976 words in {0,1}^17', i.e. 17 generators.")
print('17 == join-irreducibles:', len(joinirr) == 17)

print()
print('=== 8. 20.2 / 20.1 arithmetic ===')
print('C(6,2) =', math.comb(6, 2), '   C(5,2) =', math.comb(5, 2),
      '   11.2 tests and holds: 10')
print('ten of C(6,2):', 10, 'of', math.comb(6, 2), '- five pairs untested')
print('Chapter 1 timings: 0.010 / 0.00018 =', round(0.010 / 0.00018, 4),
      '-> printed as a factor of 55 (L408) and fifty-five (L5565)')
print('nearest integer:', round(0.010 / 0.00018))
