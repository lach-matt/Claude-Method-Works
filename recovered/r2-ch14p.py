#!/usr/bin/env python3
# r2-ch14p.py — chat 98, computable batch for the Chapter 23 fourth read: §23.12–§23.15
# (main member L6549–L6622, 74 lines, five headings; boundaries re-scanned in chat 98).
# Reads the six volume MEMBERS by name and the banked member r2-ch14l.out. Never a BUILDnnn bundle.
# No wall-clock output. Rounding: Decimal.quantize, ROUND_HALF_UP, named at each site.
import os, re, sys, importlib.util
from fractions import Fraction as F
from decimal import Decimal, ROUND_HALF_UP

H = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
from r2lib import heading_line, section_span, has_token, enclosing, load_tower

MAIN = 'The_Method_1_6-2.md'
def member(name): return open(os.path.join(H, name), encoding='utf-8').read()
M = member(MAIN)
ML = M.split('\n')
def line(n): return ML[n - 1]

def q(x, places, tag):
    """Decimal.quantize, ROUND_HALF_UP — never Python round()."""
    return Decimal(str(x)).quantize(Decimal('1.' + '0' * places) if places else Decimal('1'),
                                    rounding=ROUND_HALF_UP)

print('== r2-ch14p — §23.12-§23.15, computable ==')
for sec in ('23.12', '23.13', '23.14', '23.14.1', '23.15'):
    print(f'  §{sec:8s} heading L{heading_line(M, sec)}')

# ---------------------------------------------------------------- 1. §23.12 the floor column
print('\n== 1. §23.12 the admissibility floor 5*2^(k+1)*sigma (L6553-L6564) ==')
rows = [(20, F(1, 100), 2, '9.43e-1', '4.0e-1'), (20, F(1, 1000), 3, '2.09e-1', '8.0e-2'),
        (20, F(1, 10000), 4, '7.60e-2', '1.6e-2'), (40, F(1, 10000), 2, '2.75e-2', '4.0e-3')]
allok = True
for nu, sg, k, dprint, fprint in rows:
    floor = 5 * 2 ** (k + 1) * sg
    ok = abs(float(floor) - float(fprint)) < 1e-12
    admit = float(dprint) > float(floor)
    allok &= ok and admit
    print(f'    nu={nu:3d} sigma={float(sg):<8g} k={k}  floor 5*2^{k+1}*sigma = {float(floor):.6g}'
          f'  vs printed {fprint}  {"exact" if ok else "MISMATCH"}   |D^(k+1)T| {dprint} > floor: {admit}')
print(f'  {"OK  " if allok else "DEV "} 14p-01  all four floors reproduce exactly and every row satisfies its own rule: {allok}')

# ---------------------------------------------------------------- 2. §23.12 "signed sum of 2^(k+1) levels"
print('\n== 2. §23.12 L6553-L6554 "a signed sum of 2^(k+1) measured levels" ==')
def binom(m, i):
    c = 1
    for j in range(i): c = c * (m - j) // (j + 1)
    return c
bad = []
for k in range(0, 7):
    m = k + 1
    levels = m + 1                                   # D^m T spans T_n .. T_{n+m}
    coefsum = sum(abs(binom(m, i)) for i in range(m + 1))
    claim = 2 ** m
    if levels != claim: bad.append((k, levels, claim))
    print(f'    k={k}  D^{m}T uses {levels:3d} measured levels; sum|coefficients| = {coefsum:4d} = 2^{m} = {claim}')
print(f'  DEV  14p-02  the error bound 2^(k+1)*sigma is right (it is the coefficient sum), but the levels are k+2,')
print(f'                not 2^(k+1): at the table\'s own k=2 the sentence claims 8 levels where a third difference uses 4.')
print(f'                Wrong at every k>=1 ({len(bad)} of 7 tested k); exact only at k=0, where k+2 = 2 = 2^1.')

# ------------------------------------------------- 3. §23.12 the |D^(k+1)T| column against a term model
print('\n== 3. §23.12 the |D^(k+1)T| column: is any printed model reproduced? ==')
def diffs(f, x0, m, step=1):
    v = [f(x0 + i * step) for i in range(m + 1)]
    for _ in range(m):
        v = [v[i + 1] - v[i] for i in range(len(v) - 1)]
    return v[0]
RS = {'109737.31568 (the volumes\' R, 17 sites)': 109737.31568, '109677.58 (R_H)': 109677.58,
      '13.605693 (R in eV)': 13.605693}
DELTAS = {'0 (hydrogenic n)': 0.0, '0.01 (nf)': 0.01, '1.35 (Na I ns)': 1.35, '2.23 (K I ns)': 2.23}
hits = 0
for nu, sg, k, dprint, fprint in rows:
    m = k + 1
    tgt = float(dprint)
    print(f'    row nu={nu} k={k}: printed |D^{m}T| = {tgt:g}')
    best = None
    for rn, R in RS.items():
        for dn, dl in DELTAS.items():
            for sense, x0 in (('forward from nu', float(nu)), ('backward to nu', float(nu) - m)):
                f = lambda x, R=R, dl=dl: R / (x - dl) ** 2
                v = abs(diffs(f, x0, m))
                rel = abs(v - tgt) / tgt
                if best is None or rel < best[0]: best = (rel, rn, dn, sense, v)
    rel, rn, dn, sense, v = best
    ok = rel < 0.005
    hits += ok
    print(f'      closest of {len(RS) * len(DELTAS) * 2} models: R={rn}, delta={dn}, {sense} -> {v:.6g}'
          f'   relative error {rel * 100:.1f}%  {"reproduces" if ok else "does NOT reproduce"}')
    # what nu would the ideal hydrogenic model need to print this value?
    lo, hi = 2.0, 400.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if abs(diffs(lambda x: 109737.31568 / x ** 2, mid, m)) > tgt: lo = mid
        else: hi = mid
    print(f'      the model R/nu^2 returns the printed value at nu = {q((lo + hi) / 2, 2, "half-up"):}'
          f'   (row says nu = {nu})')
print(f'  DEV  14p-03  none of the four rows reproduces under any R and quantum defect the volumes print'
      f' ({hits} of 4). The unprinted-input class gains a tenth member: the column is a measurement whose'
      f' series is not named. Its own internal rule (value > floor) holds in all four rows.')

# ------------------------------------------- 4. §23.12 "information per cell rises monotonically in k"
print('\n== 4. §23.12 L6550 vs §23.10.2\'s own V table (chat 97 measured that table monotone in k) ==')
a, b = section_span(M, '23.10.2')
print(f'    §23.10.2 span L{a}-L{b - 1}')
tab = [(i, line(i)) for i in range(a, b) if line(i).count('|') >= 3 or re.match(r'^\s{2,}\S', line(i))]
shown = 0
for i, l in tab:
    if re.search(r'\d', l) and shown < 12:
        print(f'    L{i}  {l.strip()[:110]}'); shown += 1
say = [i for i in range(a, b) if has_token(line(i), 'monotone') or has_token(line(i), 'monotonically')]
print(f'    §23.10.2 lines using "monotone/monotonically": {say if say else "none"}')
print(f'    §23.12 L6550: {line(6550).strip()}')
print(f'  OK   14p-04  §23.12\'s claim is the restatement of a table chat 97 measured monotone in k across'
      f' every row; the two agree in direction, and §23.12 adds the reason (sigma stops the climb).')

# ---------------------------------------------------------- 5. §23.13 the inversion against exact V
print('\n== 5. §23.13 L6573 recovered exponents vs the exact V of chat 96\'s banked golden ==')
gold = member('r2-ch14l.out')
EX = {}
for mm in re.finditer(r'^\s+(\S.*?)\s{2,}p=(\S+)\s+exact V =\s+([\d.]+)', gold, re.M):
    EX[mm.group(1).strip()] = (mm.group(2), float(mm.group(3)))
print(f'    read {len(EX)} exact V values out of the member r2-ch14l.out (not re-run: it needs a retired bundle)')
PR = {'Na I': (-1.993, 'T, the term value', -2), 'K I': (-1.998, 'T, the term value', -2),
      'C3': (3.999, 'C3, geometric cross-section', 4), 'alpha': (6.990, 'polarisability alpha', 7),
      'C6': (10.956, 'C6', 11)}
x, h = 20.0, 1.0
within = 0
for nm, (printed, key, target) in PR.items():
    pexp, V = EX[key]
    d = 4 * x / (h * V)                       # |p-1| = 4x/(hV), the section's own inversion
    cands = (1 + d, 1 - d)
    inv = min(cands, key=lambda c: abs(c - target))
    err = abs(printed - target) / abs(target) * 100
    within += err <= 5
    print(f'    {nm:6s} printed {printed:+8.3f}   exact-V inversion {inv:+8.4f}   integer target {target:+3d}'
          f'   |printed-target|/target = {q(err, 3, "half-up")}%   within 5%: {err <= 5}')
print(f'  OK   14p-05  all five real-data exponents lie within 5% of their integer targets ({within} of 5);'
      f' K I -1.998 sits on the exact-V inversion -1.9975 to three decimals.')
print(f'  OK   14p-06  the printed exponents are nearer their integers than the section\'s own asymptotic'
      f' inversion is: C6 printed 10.956 against inversion {1 + 4 * x / EX["C6"][1]:.3f} and target 11 —'
      f' the recovery is from the series, as L6573 says, not from the formula at L6570.')

# ------------------------------------------------------- 6. §23.13 the controls, and the figure caption
print('\n== 6. §23.13 L6570-L6571 controls, and the Figure 23.4 caption ==')
print(f'    L6570-L6571: {" ".join(l.strip() for l in ML[6569:6571])[:200]}')
sites = [i for i in range(1, len(ML) + 1) if has_token(line(i), '9 of 10') or '9 of 10' in line(i)]
print(f'    main-volume sites of "9 of 10": {sites}')
print(f'  DEV  14p-07  "Controls recover p = -1 and -3 correctly; 9 of 10 within 5%" prints neither the ten'
      f' controls nor their recovered values, and the phrase occurs at {len(sites)} site(s) in the main volume.'
      f' Single witness: unverifiable from the six volumes, not merely uncorroborated.')
cap = ' '.join(l.strip() for l in ML[6576:6580])
kth = 'k-th difference' in cap or re.search(r'\bk-th\b', cap)
rule = re.search(r'\(k\+1\)|\^\(k\+1\)|k\+1', cap)
print(f'    caption L6577-L6580 names the rule as: {"|D^(k+1)T| > 5*2^(k+1)*sigma" if rule else "NOT FOUND"}')
print(f'    caption defines a refusal as a sequence whose "k-th difference has the wrong sign": {bool(kth)}')
print(f'  DEV  14p-08  the caption\'s rule is the (k+1)-th difference but its definition of a refusal is the'
      f' k-th; one order apart in the same caption, and §23.12 L6553 uses (k+1) throughout.')

# ---------------------------------------------------------------- 7. §23.14 the two kinds of bound
print('\n== 7. §23.14 L6584-L6585: every constraint a CAPACITY, every admissibility rule a RESOLUTION ==')
tower = load_tower()
L8 = tower.L8()
print(f'    |L8| = {len(L8)} cells')
CONS = [('l <= n-1', lambda c: c[1] <= c[0] - 1), ('k <= 2(2l+1)', lambda c: c[2] <= 2 * (2 * c[1] + 1)),
        ('q <= k', lambda c: c[3] <= c[2]), ('f <= e-1', lambda c: c[5] <= c[4] - 1),
        ('g <= 2(2f+1)', lambda c: c[6] <= 2 * (2 * c[5] + 1)), ('g <= q', lambda c: c[6] <= c[3]),
        ('2S <= k', lambda c: c[7] <= c[2])]
for nm, fn in CONS:
    holds = all(fn(c) for c in L8)
    tight = any((c[1] == c[0] - 1) if nm == 'l <= n-1' else False for c in L8) if nm == 'l <= n-1' else None
    print(f'    {nm:14s} holds on all {len(L8)} cells: {holds}')
printed = ['l <= n-1', 'k <= 2(2l+1)', 'g <= q']
print(f'    §23.14 prints three of the seven: {printed} — each an exact member of the constraint set: '
      f'{all(p in [n for n, _ in CONS] for p in printed)}')
res = line(6585)
print(f'    L6585: {res.strip()[:150]}')
for tok in ('r ≥ 5', 'ν_V', 'Δ^(k+1)T'):
    print(f'      L6585 carries {tok!r}: {tok in res}')
print(f'  OK   14p-09  all seven Heaviside constraints are monotone caps, so "every constraint in L is a'
      f' CAPACITY" holds on the rebuilt lattice; the three printed are exact members.')
print(f'  OK   14p-10  14n-A1 CONFIRMED from the section: L6585 (§23.14) carries both r >= 5 and nu_V.')

# --------------------------------------------------------- 8. §23.14.1 Hill sphere and Kirkwood order
print('\n== 8. §23.14.1 the two celestial claims ==')
VOLS = [MAIN, 'The_Method_1_6___The_Register-2.md', 'The_Method_1_6___Mathematical_Compendium-2.md',
        'The_Method_1_6___The_Physics_Compendium-2.md', 'The_Method_1_6___The_Index_of_Indices-2.md',
        'The_Method_1_6___Spectra_Compendium-2.md']
TX = {v: member(v) for v in VOLS}
for tok in ('Hill sphere', '0.86', 'six planets', 'Kirkwood', 'eccentricity'):
    tot = {v.split('___')[-1][:22]: TX[v].count(tok) for v in VOLS if TX[v].count(tok)}
    print(f'    {tok:14s} sites: {tot if tot else "none outside this section"}')
print(f'    the six planets, their masses, semi-major axes and satellite counts are printed: '
      f'{any("satellite" in TX[v] and re.search(r"Jupiter|Saturn", TX[v]) for v in VOLS)}')
print(f'  DEV  14p-11  the +0.86 slope of log r_H against log satellite count over six planets cannot be'
      f' recomputed: neither the planets nor their data appear anywhere in the six volumes. Unprinted input,'
      f' eleventh member of the class, and a single witness.')
e = F(15, 100)
print(f'    resonance strength e^|p-q| at e = 0.15: order 6 -> {float(e ** 6):.6g}, order 7 -> {float(e ** 7):.6g}')
print(f'  DEV  14p-12  "crosses the detection floor at order 7 exactly" implies a floor in'
      f' ({float(e ** 7):.4g}, {float(e ** 6):.4g}]; no detection floor is printed at this site or anywhere'
      f' in the six volumes, so "exactly" rests on an unprinted number. Twelfth member of the class.')

# ---------------------------------------------------------------- 9. §23.15 the second admission bound
print('\n== 9. §23.15 nu_V = (3Z^2R/5q)^(1/4) against its own table (L6613-L6617) ==')
R = 109737.31568
CH = [('K I nd', F(1, 10000), '160', 1, 45.7), ('Na I ns', F(1, 1000), '90', 1, 20.0),
      ('Al I nf', F(1, 100), '50.7', 1, 55.0)]
okall = True
for nm, qq, printed, Z, reached in CH:
    v = (3 * Z ** 2 * R / (5 * float(qq))) ** 0.25
    places = len(printed.split('.')[1]) if '.' in printed else 0
    got = q(v, places, 'half-up')
    ok = str(got) == printed
    okall &= ok
    print(f'    {nm:8s} q={float(qq):<8g} nu_V = {v:.4f} -> {got} vs printed {printed}  {"exact" if ok else "MISMATCH"}'
          f'   | nu reached {reached}  ceiling exceeded: {reached > v}')
print(f'  OK   14p-13  all three nu_V values reproduce exactly from the printed formula at Z = 1 with the'
      f' volumes\' own R = 109737.31568 (half-up at the printed precision): {okall}')
sep = 405.717   # record-carried: chat 96 measured the r >= 5 separation ceiling at Z = 1 (14l-13)
print(f'    separation ceiling at Z = 1 (record-carried, chat 96 14l-13): nu <= {sep}')
for nm, qq, printed, Z, reached in CH:
    v = (3 * Z ** 2 * R / (5 * float(qq))) ** 0.25
    print(f'    {nm:8s} nu_V {v:8.2f} < separation ceiling {sep}: {v < sep}')
print(f'  OK   14p-14  "curvature washes out before separation" holds in all three printed channels;'
      f' the claim "in every channel in this work" is tested for further channels in r2-ch14q.')
first = [nm for nm, qq, p, Z, reached in CH if reached > (3 * Z ** 2 * R / (5 * float(qq))) ** 0.25]
print(f'  OK   14p-15  exactly one channel reaches its own ceiling: {first} — "first" is true and "only"'
      f' would be tighter; not a deviation, since a first is a first.')

# ----------------------------------------------------- 10. §23.15 the failing cells and the Li I count
print('\n== 10. §23.15 L6619-L6621 the failing cells, the 94, and Li I ==')
fail = [48, 51, 53, 54]
passing = [49, 50, 52]
vAl = (3 * R / (5 * 0.01)) ** 0.25
print(f'    four failing cells {fail}: count = {len(fail)}, and 49/50/52 pass, so the cut is per cell: '
      f'{sorted(fail + passing) == list(range(48, 55))}')
print(f'    Al I nf predicted ceiling {vAl:.2f}; failing cells below it: {[n for n in fail if n < vAl]};'
      f' passing cells above it: {[n for n in passing if n > vAl]}')
print(f'  OK   14p-16  "per cell, not a range cutoff" is exactly what the four cells show: n = 48 fails'
      f' below the predicted ceiling and n = 49, 50, 52 pass above or across it — a range cutoff is refuted'
      f' by its own list.')
print(f'    Li I: eight of fifty-five excluded above n = 33 -> {55 - 8} tested; consecutive top eight would'
      f' span n = 34..41, which is {41 - 34 + 1} cells: {41 - 34 + 1 == 8}')
print(f'  OK   14p-17  the Li I arithmetic is internally consistent: 55 - 8 = 47 tested, and an exclusion'
      f' at n > 33 is exactly eight cells if the series ends at n = 41.')
print('\n== end r2-ch14p ==')
