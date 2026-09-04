#!/usr/bin/env python3
# r2-ch13z.py - chat 90 - COMPUTABLE batch for the Chapter 21 first-part section read
# (main L5597-L5689: 21.1 through 21.5's opening).
# Claims measured: 21.1's row 3 (one object, two namings, E 750 -> 0) and its row 8 pair count;
# 21.3's "thirteen coordinates"; 21.5's seed table (audit index / periodic table / calendar /
# parity rule), "Lambda's seed is ten cells for 976", the two seed estimates for the violation
# index (near fifteen at L5682, nearer twenty at L5686) and "a seed near twenty-five carries all
# 199,130"; and the recovery claim "print the seed of R(X) and the E cells".
# Deterministic; prints no wall-clock time.

import importlib.util, os, itertools, math
H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib)
T = r2lib.load_tower()

CAPS = (3, 3, 1, 3, 1)          # (n_max, e_max, l_max, k_max, f_max)
NAMES = ['n', 'l', 'k', 'q', 'e', 'f', 'g', '2S', "2S'"]
IL, IF = 1, 5                   # l, f   (lifted verbatim from r2-ch13x.py, chat 89)


def E(X):
    """E(X) = |R(X)| - |X|, R the recovered-bounds closure of section 6.1 (r2lib.Rset).
    lifted verbatim from r2-ch13x.py (chat 89)."""
    X = set(map(tuple, X))
    return len(r2lib.Rset(X)) - len(X)


def seed_of(cells, cap=16):
    """The minimum seed of R(cells) under 14.5.7's covering model (r2lib.cover_model /
    cover_reduce / exact_seed).  Returns (size, n_elements_reduced)."""
    _c, _e, Mx, _v = r2lib.cover_model(cells)
    red = r2lib.cover_reduce(Mx)
    nd, FULL = red[2], red[3]
    n, _w = r2lib.exact_seed(nd, FULL, cap=cap)
    return n, len(nd)


print('=== 0. controls ===')
L8 = [tuple(c) for c in T.L8()]
L9 = [tuple(c) for c in T.L9()]
print('|L8| =', len(L8), 'expected 976  ', 'OK' if len(L8) == 976 else 'FAIL')
print('|L9| =', len(L9), 'expected 1,654', 'OK' if len(L9) == 1654 else 'FAIL')
print('E(L9) =', E(L9), 'expected 0 (a closed index)')

print()
print('=== 1. 21.1 row 3 (L5606): "one object", two namings, E 750 -> 0 ===')
d = lambda c: c[IF] - c[IL]
rng_d = sorted({d(c) for c in L9})
eq1 = [c for c in L9 if abs(d(c)) == 1]           # first naming: |dl| = 1, a congruence
band = [c for c in L9 if abs(d(c)) <= 1]          # second naming: the convex band |dl| <= 1
e_eq1, e_band = E(eq1), E(band)
print('attained range of d = f - l:', rng_d)
print('first naming  |{|d| = 1}|  =', len(eq1), ' E =', e_eq1,
      ' printed (840, 750)', 'OK' if (len(eq1), e_eq1) == (840, 750) else 'FAIL')
print('second naming |{|d| <= 1}| =', len(band), ' E =', e_band,
      ' printed E = 0', 'OK' if e_band == 0 else 'FAIL')
print('the two namings name the same object:', set(eq1) == set(band))
print('cells the second naming holds and the first does not:', len(set(band) - set(eq1)))
print('the second naming is the whole index:', len(band) == len(L9))

print()
print('--- 1b. can ANY relabelling of a coordinate alphabet take the 840 cells to E = 0? ---')
print('    (r2-ch13x\'s relabelling sweep, chat 89, extended to every coordinate)')
dim = len(L9[0]); best = (None, None, None); swept = 0
for i in range(dim):
    alpha = sorted({c[i] for c in L9})
    if len(alpha) > 4 or len(alpha) < 2:
        print('    %-3s alphabet %-14s skipped (|alphabet| = %d)' % (NAMES[i], str(alpha), len(alpha)))
        continue
    Es = []
    for p in itertools.permutations(alpha):
        sig = dict(zip(alpha, p))
        Xs = [tuple(sig[v] if j == i else v for j, v in enumerate(c)) for c in eq1]
        Es.append(E(Xs)); swept += 1
    print('    %-3s alphabet %-14s %2d relabellings   E in [%d, %d]' %
          (NAMES[i], str(alpha), len(Es), min(Es), max(Es)))
    if best[0] is None or min(Es) < best[0]:
        best = (min(Es), NAMES[i], len(Es))
print('    relabellings swept:', swept, '  least E attained:', best[0], '(at', best[1] + ')')
print('    any relabelling reaching E = 0:', best[0] == 0)

print()
print('=== 2. 21.3 (L5634): q "carried through thirteen coordinates" ===')
for k in range(8, 14):
    fn = getattr(T, 'L%d' % k, None)
    if fn is None:
        print('  L%-2d  tower-2 exposes no L%d()' % (k, k)); continue
    X = [tuple(c) for c in fn()]
    print('  L%-2d  cells %7s   arity %2d   q present at index 3: %s' %
          (k, format(len(X), ','), len(X[0]), len(X[0]) > 3))
print('  arity of the top index equals thirteen:',
      len([tuple(c) for c in T.L13()][0]) == 13 if hasattr(T, 'L13') else 'L13 not exposed')
print('  q is factor-free on L8 (r2lib.factor_q, 0 = q determined by src/tgt):', r2lib.factor_q(L8))

print()
print('=== 3. 21.5 (L5685): "Lambda\'s seed is ten cells for 976" ===')
s8, n8 = seed_of(L8)
print('  seed(L8)  =', s8, ' over', n8, 'non-dominated cover masks   printed TEN', 
      'OK' if s8 == 10 else 'FAIL - printed 10, measured %s' % s8)
s9, n9 = seed_of(L9)
print('  seed(L9)  =', s9, ' over', n9, 'masks')
L10 = [tuple(c) for c in T.L10()]
s10, n10 = seed_of(L10)
print('  seed(L10) =', s10, ' over', n10, 'masks   (|L10| = %s)' % format(len(L10), ','))
print('  seed follows arity - 1 at 8, 9, 10:', (s8, s9, s10) == (7, 8, 9))
print('  extrapolated seed at arity 13 (199,130 cells):', 12,
      ' against 21.5\'s "a seed near twenty-five"')

print()
print('=== 4. 21.5 (L5672-L5676): the four-row seed/E/printed/compression table ===')
ROWS = [('the audit index', 21, 16, 7, 23, 0.9),
        ('the periodic table', 90, 36, 19, 55, 1.6),
        ('the calendar as printed', 365, 7, 31, 38, 9.6),
        ('the parity rule', 840, 750, 13, 763, 1.1)]
print('  %-26s %6s %5s %5s %8s %7s %7s %6s' %
      ('row', 'cells', 'E', 'seed', 'printed', 'seed+E', 'X/prt', 'compr'))
for nm, X, e, sd, prt, comp in ROWS:
    calc = round(X / prt, 1)
    print('  %-26s %6d %5d %5d %8d %7d %7.4f %6.1f  %s' %
          (nm, X, e, sd, prt, sd + e, X / prt, comp,
           'OK' if (sd + e == prt and calc == comp) else 'FAIL'))
print('  E/|X| ordering :', [nm for nm, X, e, sd, prt, c in sorted(ROWS, key=lambda r: r[2] / r[1])])
print('  compression ordering:', [nm for nm, X, e, sd, prt, c in sorted(ROWS, key=lambda r: r[5])])
print('  compression monotone in E/|X| (the "E is the binding term" claim):',
      [r[2] / r[1] for r in sorted(ROWS, key=lambda r: r[5])] ==
      sorted([r[2] / r[1] for r in ROWS], reverse=True))
print('  seed share of |X|: ' + ', '.join('%s %.3f' % (nm, sd / X) for nm, X, e, sd, prt, c in ROWS))

print()
print('=== 5. 21.5 (L5681-L5686): the violation index\'s two seed estimates ===')
print('  printed at L5682: seed near 15, total "about forty-five cells for 2,370" ->', 15 + 30)
print('  printed at L5686: seed "nearer twenty" -> total', 20 + 30)
print('  the two printed estimates agree:', 15 == 20)
for lab, num, den in (("Lambda's ratio AS PRINTED (10/976)", 10, 976),
                      ("Lambda's ratio AS MEASURED (%d/976)" % s8, s8, 976)):
    print('  %-38s -> 2,370 cells: %6.2f   199,130 cells: %8.2f' %
          (lab, 2370 * num / den, 199130 * num / den))
print('  "a seed near twenty-five carries all 199,130" against the printed ratio:',
      round(199130 * 10 / 976, 1))

print()
print('=== 6. 21.1 row 8 (L5611): "six languages agree; ten combinations hold" ===')
print('  C(6,2) =', math.comb(6, 2), '  C(5,2) =', math.comb(5, 2), '  printed: ten hold of', math.comb(6, 2))
print('  ten is C(5,2), not C(6,2):', math.comb(5, 2) == 10)

print()
print('=== 7. 21.5 (L5667-L5670): does "seed of R(X) plus the E cells" recover X exactly? ===')
RX = r2lib.Rset(set(eq1)); Xs = set(eq1)
extra = RX - Xs
print('  |R(X)| =', len(RX), ' |X| =', len(Xs), ' |R(X) \\ X| =', len(extra),
      ' equals E:', len(extra) == e_eq1)
sd_par, nd_par = seed_of(sorted(RX))
print('  seed(R(X)) =', sd_par, ' over', nd_par, 'masks   printed 13 for the parity rule',
      'OK' if sd_par == 13 else 'FAIL - printed 13, measured %s' % sd_par)
print('  R(X) minus the E cells recovers X exactly:', (RX - extra) == Xs)
print('  cost as printed: seed + E =', 13 + 750, ' as measured:', (sd_par or 0) + len(extra))
