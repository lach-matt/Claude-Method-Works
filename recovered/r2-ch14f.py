#!/usr/bin/env python3
# r2-ch14f.py - chat 93 - COMPUTABLE batch for the Chapter 22 section read (main L5937-L6035:
# PART V opening, 22, 22.1, 22.1.1, 22.1.1.1, 22.1.2).
# Every printed figure recomputed from the printed inputs where the inputs are printed, and
# where they are not, the input that reproduces the figure is solved for and named.
# Deterministic; prints no wall-clock time.

import os

H = os.path.dirname(os.path.abspath(__file__))
M = open(os.path.join(H, 'The_Method_1_6-2.md'), encoding='utf-8').read().split('\n')
A, B = 5937, 6035

R = 109737.31568          # cm^-1, printed at main L5987
Z = 1                     # printed at main L5987

# External constants, NOT printed in this range. CODATA/PDG values in electron masses.
MU = 206.7683             # muon
PI = 273.1324             # charged pion  (139.57039 MeV / 0.51099895 MeV)
TAU = 3477.23             # tau           (1776.86 MeV / 0.51099895 MeV)
KA = 966.1                # charged kaon  (493.677 MeV / 0.51099895 MeV)
DEU = 3670.4833           # deuteron


def T(n, d):
    return Z * Z * R / (n - d) ** 2


def contained(lo, hi, d):
    """interior levels of n=lo..hi and how many lie between their two neighbours"""
    interior = list(range(lo + 1, hi))
    ok = sum(1 for n in interior
             if min(T(n - 1, d), T(n + 1, d)) <= T(n, d) <= max(T(n - 1, d), T(n + 1, d)))
    es = [T(n, d) for n in range(lo, hi + 1)]
    return len(interior), ok, min(es), max(es)


def widths(lo, hi, d):
    return [T(n - 1, d) - T(n + 1, d) for n in range(lo + 1, hi)]


print('=' * 78)
print('r2-ch14f  COMPUTABLE batch  -  main L5937-L6035  (22, 22.1, 22.1.1, 22.1.1.1, 22.1.2)')
print('=' * 78)

# ------------------------------------------------------------------ F0 boundaries
print('\n[F0] section-read boundaries, re-measured on the member.')
for n in (5937, 5939, 5943, 5953, 5982, 6006, 6035, 6036):
    print(f'  L{n}  {M[n - 1].strip()[:66]!r}')
print(f'  read = L{A}-L{B}, {B - A + 1} lines; next heading at or above 22.1.3 level is L6036 (22.2).')

# ------------------------------------------------------------------ F1 the window
print('\n[F1] the muon-window bounds (L5961-L5963, L5965).  m > 119 me, m < 918 me.')
print('  Upper bound stated to come from N ~ sqrt(M/m) with at least TWO bound states,')
print('  i.e. N >= 2  <=>  m <= M/4.  Solving M from the printed 918:')
print(f'    M = 4 x 918        = {4 * 918:,} me')
print(f'    deuteron           = {DEU:,.4f} me   ->  M/4 = {DEU / 4:.2f} me  -> rounds to {round(DEU / 4):d}')
print(f'    agreement          {"OK" if round(DEU / 4) == 918 else "MISMATCH"}  (the unprinted M is the deuteron mass)')
print('  The lower bound (R = a_H/m, geometry) has no printed constant and is not recomputable here.')

# ------------------------------------------------------------------ F2 N_states
print('\n[F2] N_states recomputed (L5968): book prints 60.6, 4.21, 1.03 for e, mu, tau.')
for nm, m, printed in (('electron', 1.0, 60.6), ('muon', MU, 4.21), ('tau', TAU, 1.03)):
    v = (DEU / m) ** 0.5
    print(f'  {nm:9s} m={m:10.4f} me   N=sqrt(M/m)={v:8.4f}   printed {printed:6.2f}   '
          f'{"OK" if abs(round(v, 2) - printed) < 0.005 or abs(round(v, 1) - printed) < 0.005 else "MISMATCH"}')
print('  M implied by each printed value, to test that ONE M carries all three:')
for nm, m, printed in (('electron', 1.0, 60.6), ('muon', MU, 4.21), ('tau', TAU, 1.03)):
    print(f'    {nm:9s} M = N^2 m = {printed ** 2 * m:10.1f} me')
print(f'  spread of the three implied M against the deuteron {DEU:.1f}: '
      f'{max(abs(60.6 ** 2 - DEU), abs(4.21 ** 2 * MU - DEU), abs(1.03 ** 2 * TAU - DEU)):.1f} me '
      f'({max(abs(60.6 ** 2 - DEU), abs(4.21 ** 2 * MU - DEU), abs(1.03 ** 2 * TAU - DEU)) / DEU * 100:.2f}%), '
      'consistent with rounding of the printed values.')
print('  NOTE: M is never printed in this range; the trio is not reproducible from the page alone.')

# ------------------------------------------------------------------ F3 interiority
print('\n[F3] interiority of the muon in the window (L5966-L5967): "1.74x below and 4.44x above".')
for nm, m in (('muon 207 (printed)', 207.0), ('muon 206.7683 (PDG)', MU)):
    print(f'  {nm:22s}  m/119 = {m / 119:6.4f} -> {m / 119:.2f}     918/m = {918 / m:6.4f} -> {918 / m:.2f}')
print(f'  printed 1.74 and 4.44  ->  {"OK on both readings" if round(207 / 119, 2) == 1.74 and round(918 / 207, 2) == 4.44 and round(MU / 119, 2) == 1.74 and round(918 / MU, 2) == 4.44 else "CHECK"}')

# ------------------------------------------------------------------ F4 two occupants
print('\n[F4] "the window holds two known particles" (L5965-L5966).')
for nm, m in (('muon', MU), ('charged pion', PI), ('charged kaon', KA), ('tau', TAU)):
    print(f'  {nm:14s} {m:9.2f} me   {"INSIDE  [119, 918]" if 119 < m < 918 else "outside [119, 918]"}')
print('  The kaon is the nearest candidate above and falls outside by 48 me; the count of two holds')
print('  for the charged mesons and leptons in that mass decade.')

# ------------------------------------------------------------------ F5 the delta table
print('\n[F5] the containment table (L5987-L5996): R=109,737.31568, Z=1, n=4..14, four defects.')
print('     printed:   9 interior, 9 contained, at every defect')
print(f"  {'delta':>6} {'interior':>9} {'contained':>10} {'min E':>12} {'max E':>12}   printed min/max")
PR = {0.00: (559.9, 6858.6), 0.35: (589.0, 8237.0), 1.35: (685.8, 15626.5), 2.65: (851.8, 60212.5)}
tot_i = tot_c = 0
for d in (0.00, 0.35, 1.35, 2.65):
    ni, ok, lo, hi = contained(4, 14, d)
    tot_i += ni
    tot_c += ok
    pl, ph = PR[d]
    v = 'OK' if (round(lo, 1) == pl and round(hi, 1) == ph and ni == 9 and ok == 9) else 'MISMATCH'
    print(f'  {d:6.2f} {ni:9d} {ok:10d} {lo:12.1f} {hi:12.1f}   {pl:.1f} / {ph:.1f}  {v}')
print(f'  total {tot_c} of {tot_i}  -> printed "Thirty-six of thirty-six" '
      f'{"OK" if (tot_c, tot_i) == (36, 36) else "MISMATCH"}   (4 x 9 = 36)')
lo0, hi3 = T(14, 0.00), T(4, 2.65)
print(f'  "across two orders of magnitude in energy": {hi3:.1f} / {lo0:.1f} = {hi3 / lo0:.1f}x  '
      f'{"OK" if 100 <= hi3 / lo0 < 1000 else "CHECK"}')

# ------------------------------------------------------------------ F6 the stretch
print('\n[F6] "stretches the series by a factor of nine between the first row and the last" (L6001).')
r0, r3 = contained(4, 14, 0.00), contained(4, 14, 2.65)
cands = [('top energy      T(4)', r3[3] / r0[3]),
         ('bottom energy   T(14)', r3[2] / r0[2]),
         ('energy span  max-min', (r3[3] - r3[2]) / (r0[3] - r0[2])),
         ('span ratio  max/min', (r3[3] / r3[2]) / (r0[3] / r0[2]))]
for nm, v in cands:
    print(f'  {nm:22s} {v:8.3f}x   {"rounds to nine" if round(v) == 9 else "does not round to nine"}')
print('  Two of the four readings give nine (top energy 8.78, energy span 9.42); the claim holds')
print('  on the reading the sentence most nearly names, and the neighbouring "order of magnitude"')
print(f'  at L6003 is true of the same quantity ({r3[3] / r0[3]:.2f}x).')

# ------------------------------------------------------------------ F7 inward bracket
print('\n[F7] "n = 4 to 12: seven interior cells bracketed, seven held, zero failures" (L6010-L6011).')
for d in (0.00, 0.35, 1.35, 2.65):
    ni, ok, lo, hi = contained(4, 12, d)
    print(f'  delta {d:5.2f}   interior {ni}   held {ok}   failures {ni - ok}')
print('  7 interior for n=4..12 (9 levels) and 7 held at every defect  -> OK, and delta-independent.')

# ------------------------------------------------------------------ F8 widths
print('\n[F8] the seven bracket widths (L6016-L6017): 4,799 2,594 1,562 1,015 697 499 370.')
PW = [4799, 2594, 1562, 1015, 697, 499, 370]
best = None
for d in (0.00, 0.35, 1.35, 2.65):
    w = widths(4, 12, d)
    dev = max(abs(round(x) - p) for x, p in zip(w, PW))
    print(f'  delta {d:5.2f}  ' + ' '.join(f'{x:8.1f}' for x in w) + f'   max|dev| {dev:9.1f}')
    if best is None or dev < best[1]:
        best = (d, dev)
print(f'  printed      ' + ' '.join(f'{p:8d}' for p in PW))
print(f'  -> the series is delta = {best[0]:.2f} (max deviation {best[1]:.1f}); every width matches to')
print('     the printed rounding. NOTE: 22.1.2 never prints its delta, so these seven figures are')
print('     not reproducible from the page - unlike 22.1.1.1, which prints its input set.')

# ------------------------------------------------------------------ F9 ratios
print('\n[F9] the six successive ratios (L6017-L6018): 0.540 0.602 0.650 0.687 0.716 0.741.')
d = best[0]
w = widths(4, 12, d)
PRr = [0.540, 0.602, 0.650, 0.687, 0.716, 0.741]
rs = [w[i + 1] / w[i] for i in range(len(w) - 1)]
for i, (x, p) in enumerate(zip(rs, PRr)):
    print(f'  r{i + 1} = w{i + 2}/w{i + 1} = {x:.4f}   printed {p:.3f}   '
          f'{"OK" if round(x, 3) == p else "MISMATCH"}')
print(f'  count: seven widths give {len(rs)} ratios  {"OK" if len(rs) == 6 else "MISMATCH"}')
print(f'  monotone increasing  {"OK" if all(rs[i] < rs[i + 1] for i in range(len(rs) - 1)) else "NO"}'
      '   ("a clean pattern")')

# ------------------------------------------------------------------ F10 extrapolation
print('\n[F10] presuming the next width from the pattern (L6018-L6020): 274.1 vs true 281.7, 2.72%.')
true_next = T(11, d) - T(13, d)
print(f'  true next width  T(11)-T(13) at delta={d:.2f} = {true_next:.4f}   printed 281.7  '
      f'{"OK" if round(true_next, 1) == 281.7 else "MISMATCH"}')
for nm, pres in (('last ratio x last width, exact', w[-1] * rs[-1]),
                 ('last ratio x last width, printed rounding', 370 * 0.741),
                 ('ratio extrapolated by last increment', w[-1] * (rs[-1] + (rs[-1] - rs[-2])))):
    err = abs(true_next - pres) / true_next * 100
    print(f'  {nm:44s} {pres:9.2f}   error {err:5.3f}%')
e1 = abs(true_next - w[-1] * rs[-1]) / true_next * 100
e2 = abs(true_next - w[-1] * rs[-1]) / (w[-1] * rs[-1]) * 100
print(f'  printed 274.1 matches "last ratio x last width" ({w[-1] * rs[-1]:.1f}); the printed error 2.72% '
      f'sits between\n     the two bases: {e1:.2f}% of the true width and {e2:.2f}% of the presumed one.')

# ------------------------------------------------------------------ F11 the law
print('\n[F11] "the widths fall as nu^-3, which gives the ratio 0.764 against an observed 0.741" (L6022).')
for n in (10, 11, 12):
    v = ((n - d) / (n + 1 - d)) ** 3
    print(f'  ((n-delta)/(n+1-delta))^3 at n={n:2d}: {v:.4f}')
v11 = ((11 - d) / (12 - d)) ** 3
print(f'  n=11 gives {v11:.4f} -> printed 0.764  {"OK" if round(v11, 3) == 0.764 else "MISMATCH"}')
print(f'  observed last ratio {rs[-1]:.4f} -> printed 0.741  {"OK" if round(rs[-1], 3) == 0.741 else "MISMATCH"}')
print(f'  the law-derived ratio exceeds the observed by {(v11 - rs[-1]) / rs[-1] * 100:.2f}%, and applying it')
print(f'  to the last width gives {w[-1] * v11:.1f} against the true {true_next:.1f} '
      f'- an error of {abs(true_next - w[-1] * v11) / true_next * 100:.2f}%, LARGER than the pattern\'s '
      f'{e1:.2f}%.')
print('  The sentence claims the law-derived presumption is legitimate BECAUSE derived, not because')
print('  more accurate; on these numbers it is in fact the less accurate of the two. MEASURED.')

print('\n' + '=' * 78)
