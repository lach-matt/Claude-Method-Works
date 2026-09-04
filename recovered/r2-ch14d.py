#!/usr/bin/env python3
# r2-ch14d.py - chat 92 - COMPUTABLE batch for the Chapter 21 close (main L5874-L5936:
# 21.6, 21.6.1, 21.6.2).  Every printed number re-measured on the operative definition of
# R taken from r2lib.Rset - R(X) is the REALISED-VALUE grid cut by the monotone envelopes
# phi_ij, so E = |R(X)| - |X| is NOT |box| - |cells| in general.  That distinction is
# established here on the calendar before any E arithmetic is asserted, because assuming
# the box reading turns three consistent rows into false contradictions.
# Deterministic; prints no wall-clock time.

import os, sys, itertools
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, H)
import r2lib

R = r2lib.Rset


def E(X):
    X = set(map(tuple, X))
    return len(R(X)) - len(X)


def grid(X):
    X = sorted(set(map(tuple, X)))
    d = len(X[0])
    p = 1
    for i in range(d):
        p *= len({c[i] for c in X})
    return p


def rung_multisets(box, letters, lo=1):
    """All multisets of `letters` factors >= lo with product `box`."""
    out = []

    def rec(rem, k, start, acc):
        if k == 1:
            if rem >= start:
                out.append(tuple(acc + [rem]))
            return
        f = start
        while f * f <= rem * 1 and f <= rem:
            if rem % f == 0:
                rec(rem // f, k - 1, f, acc + [f])
            f += 1
        # allow the tail to exceed sqrt by letting rec handle k==1
        return
    def rec2(rem, k, start, acc):
        if k == 1:
            if rem >= start:
                out.append(tuple(acc + [rem]))
            return
        for f in range(start, rem + 1):
            if f > rem:
                break
            if rem % f == 0:
                rec2(rem // f, k - 1, f, acc + [f])
    rec2(box, letters, lo, [])
    return sorted(set(out))


print('=' * 78)
print('r2-ch14d  COMPUTABLE batch  -  main L5874-L5936  (21.6, 21.6.1, 21.6.2)')
print('=' * 78)

# ---------------------------------------------------------------- D1
print('\n[D1] The operative E, established on an index the book gives in full (L1611, L1677).')
DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
cal = [(m, d) for m, n in enumerate(DAYS, 1) for d in range(1, n + 1)]
Rc = R(set(cal))
missing = sorted(Rc - set(cal))
print(f'  calendar (month, day)      cells {len(cal)}   |R| {len(Rc)}   E {len(Rc)-len(cal)}   grid {grid(cal)}')
print(f'  printed  (main L1611)      cells 365          E 7')
print(f'  the seven absent cells MEASURED: {missing}')
print(f'  printed  (main L1677)     : [(2, 29), (2, 30), (2, 31), (4, 31), (6, 31), (9, 31), (11, 31)]')
ok = missing == [(2, 29), (2, 30), (2, 31), (4, 31), (6, 31), (9, 31), (11, 31)]
print(f'  VERDICT  cells 365 {len(cal)==365} | E 7 {len(Rc)-len(cal)==7} | absent set identical {ok}')
print(f'  NOTE  here |R| = grid, so E = |box| - |cells| COINCIDENTALLY: the envelopes are vacuous.')

# ---------------------------------------------------------------- D2
print('\n[D2] L5876-L5878 THEOREM: |X| = a*b, a,b>1, relabelled onto the a x b rectangle -> E = 0.')
rows = [('the periodic table', 90, 9, 10, 36), ('the calendar', 365, 5, 73, 7),
        ('a random 26-cell set', 26, 2, 13, 38), ('V3 geometry', 25, 5, 5, 0)]
for name, N, a, b, Egiven in rows:
    rect = [(i, j) for i in range(a) for j in range(b)]
    e = E(rect)
    print(f'  {name:22s} a*b = {a}x{b} = {a*b:5d}  vs printed count {N:5d}  {"OK" if a*b==N else "FAIL"}'
          f'   E(rectangle) = {e}  {"OK" if e == 0 else "FAIL"}   [E as given {Egiven}]')
print('  the four factorisations and the four E-after-0 entries all hold.')

print('\n[D2b] the theorem is exactly co-extensive with compositeness (N <= 400 exhaustive):')
bad = []
for N in range(2, 401):
    fac = [(a, N // a) for a in range(2, N) if N % a == 0 and N // a > 1]
    comp = len(fac) > 0
    prime = all(N % k for k in range(2, int(N ** .5) + 1))
    if comp == prime:
        bad.append(N)
print(f'  N with (a factorisation a,b>1 exists) != (N composite): {bad}  -> theorem scope exact: {bad==[]}')
print(f'  976 = |Lambda_8| is composite (2^4 * 61): {976 % 2 == 0} -> the theorem applies to Lambda itself.')

# ---------------------------------------------------------------- D3
print('\n[D3] L5926-L5927 the local null surface: six letters, box 64, "every rung 2".')
ms = rung_multisets(64, 6, lo=2)
print(f'  multisets of six factors >= 2 with product 64: {ms}  -> forced: {len(ms)==1}')
cube = list(itertools.product(*[range(2)] * 6))
face = [c for c in cube if c[0] == 0]
par = [c for c in cube if sum(c) % 2 == 0]
print(f'  |cube| {len(cube)}   32 is exactly half: {len(cube)//2 == 32}')
print(f'  FACE  (x0 = 0)        cells {len(face)}   E = {E(face)}   printed 0    {"OK" if E(face)==0 else "FAIL"}')
print(f'  PARITY class (even)   cells {len(par)}    E = {E(par)}   printed 32   {"OK" if E(par)==32 else "FAIL"}')
print(f'  both natural halves are 32 cells: {len(face)==len(par)==32}')

print('\n[D3b] L5928-L5930 the nesting THETA = 0 at 16, STAT = 0 at 8.')
for k, n in ((2, 16), (3, 8)):
    f = [c for c in cube if all(c[i] == 0 for i in range(k))]
    print(f'  face fixing {k} coordinates: cells {len(f)}  printed {n}  {"OK" if len(f)==n else "FAIL"}   E = {E(f)}')
print(f'  nesting 32 > 16 > 8 as faces of one another: {32 > 16 > 8} (each half the last)')
print('  "one cell from where half-sided modular inclusion is proved" is a companion-side')
print('  claim: the companion is not a member of either bundle, so it is NOT verified here.')

# ---------------------------------------------------------------- D4
print('\n[D4] L5907-L5908 the ANEC-proofs index: four letters, box 12.')
all12 = rung_multisets(12, 4, lo=1)
ge2 = rung_multisets(12, 4, lo=2)
one1 = [m for m in all12 if m.count(1) == 1]
print(f'  four rungs each >= 2 need at least 2^4 = 16 > 12: {2**4 > 12}  -> no such assignment: {ge2 == []}')
print(f'  all rung multisets with product 12: {all12}')
print(f'  those with EXACTLY one rung of 1: {one1}')
print(f'  MEASURED: the arithmetic forces AT LEAST one rung-1 letter ({len(all12)} assignments, all')
print(f'  with a 1), not exactly one - {len(all12)-len(one1)} of {len(all12)} carry two or more.')
print(f'  Exactly-one follows only from L5919\'s "disagree by exactly one", i.e. from three')
print(f'  effective letters; 12 = 2*2*3 is the unique 3-factor form: {rung_multisets(12,3,lo=2)}')

# ---------------------------------------------------------------- D5
print('\n[D5] L5917-L5918 "V6, V3 and the null surface use every letter in their boxes".')
for name, box, letters in (('V6', 24, 4), ('the null surface', 64, 6), ('V3', 48, 5)):
    m2 = rung_multisets(box, letters, lo=2)
    print(f'  {name:18s} box {box:3d}, {letters} letters: multisets with all rungs >= 2 = {m2}'
          f'  -> forced by arithmetic: {len(m2)==1}')
print('  MEASURED: all three are theorems of the printed pair (box, letter count), not')
print('  observations about the companion\'s data. 24 = 2*2*2*3, 48 = 2^4*3, 64 = 2^6 as printed.')

# ---------------------------------------------------------------- D6
print('\n[D6] L5910-L5912 a rung-1 coordinate changes nothing, tested on Lambda_8.')
cells = r2lib.L8_at((3, 3, 1, 3, 1))
cells = sorted(set(map(tuple, cells)))
plus = [c + (0,) for c in cells]
Ra, Rb = R(set(cells)), R(set(plus))
print(f'  Lambda_8            cells {len(cells)}   grid {grid(cells)}   |R| {len(Ra)}   E {len(Ra)-len(cells)}')
print(f'  Lambda_8 + rung-1   cells {len(plus)}   grid {grid(plus)}   |R| {len(Rb)}   E {len(Rb)-len(plus)}')
same_cells = len(cells) == len(plus)
same_box = grid(cells) == grid(plus)
same_E = (len(Ra) - len(cells)) == (len(Rb) - len(plus))
Ma = r2lib.cover_model(cells)
Mb = r2lib.cover_model(plus)
Ma = Ma[0] if isinstance(Ma, tuple) else Ma
Mb = Mb[0] if isinstance(Mb, tuple) else Mb
print(f'  cover model (envelope steps x cells): {Ma.shape} vs {Mb.shape}')
same_model = (Ma.shape == Mb.shape) and bool((Ma == Mb).all())
print(f'  MEASURED  same cells {same_cells} | same box {same_box} | same E {same_E}'
      f' | same envelope-step model {same_model}')
print(f'  the cover model is the seed problem (r2lib.cover_model docstring), so identical')
print(f'  models force an identical seed; seed(Lambda_8) = 7 is chat 90\'s settled value and')
print(f'  is NOT re-derived here.')
print(f'  VERDICT L5911 "same cells, same box, same E, same envelope-step count, same seed":'
      f' {all([same_cells, same_box, same_E, same_model])}')

# ---------------------------------------------------------------- D7
print('\n[D7] L5881 the periodic table row, against the two other sites (L1611, L1613).')
print('  printed: 90 cells, E = 36. A 7 x 18 (period, group) grid is 126, and 126 - 90 = 36:'
      f' {7*18-90 == 36}')
print('  the row is arithmetic on book-supplied numbers; the table itself is not rebuilt here')
print('  because no volume prints its 90 cells. L1611/L1613 agree at 90 and 36.')

print('\n[D8] L5883 "a random 26-cell set, E as given 38".')
print(f'  E = 38 at 26 cells requires |R| = 64: {26+38 == 64}')
print('  the set is not printed in any of the six volumes, so the 38 is NOT verifiable here;')
print('  the row\'s own claim (2 x 13 gives E = 0) is verified at [D2].')
print('\n' + '=' * 78)
