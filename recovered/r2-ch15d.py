#!/usr/bin/env python3
"""r2-ch15d - computable claims of Chapter 27, unit L7203-L7331 ("Slack", 27.1-27.5.1).

Chat 105.  Reads members only.  The book's own order (r2lib.leq) and transition endpoints
(r2lib.src / r2lib.tgt) are imported from r2lib by path; nothing is copied.  round() is never
used: every printed figure is matched with Decimal.quantize under BOTH ROUND_HALF_EVEN and
ROUND_HALF_UP and the convention is named.  Log bases e, 10 and 2 are swept on every log column.
Numeral witness sweeps are digit-bounded and run in comma and comma-free form over six volumes.

Rewritten twice before banking.  The faults, all self-caught:
  1. B1/B4 tested the bracket rows against the ASYMPTOTIC V = 4nu/3 only, reported a 0.33 %
     "deviation" at nu = 10, and would have recorded 13.378, 53.344 and 1.54 as three
     unreproducible figures.  Main L6237 prints the exact V as rational at every nu - 32/11,
     54/13, 256/47, 250/37, 4000/299 - which is V = 4nu^3/(3nu^2 - 1).  All three then reproduce
     EXACTLY.  The standing rule fired: grep the volume before recording a figure as
     unreproducible, and suspect the instrument first.
  2. B5 measured the order relation without the composition relation beside it, so it could not
     tell a wrong numerator from a denominator convention shared by both figures.
  3. one rounding convention only, and one log base only.  Both are swept and named.
"""
import importlib.util, math, re
from decimal import Decimal, ROUND_HALF_EVEN, ROUND_HALF_UP, getcontext
from fractions import Fraction
import numpy as np

getcontext().prec = 60
H = '/home/claude/members/'
spec = importlib.util.spec_from_file_location('r2lib', H + 'r2lib.py')
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)

VOLS = {'main': 'The_Method_1_6-2.md', 'reg': 'The_Method_1_6___The_Register-2.md',
        'mc': 'The_Method_1_6___Mathematical_Compendium-2.md',
        'pc': 'The_Method_1_6___The_Physics_Compendium-2.md',
        'ioi': 'The_Method_1_6___The_Index_of_Indices-2.md',
        'sc': 'The_Method_1_6___Spectra_Compendium-2.md'}
LINES = {k: r2lib.read_member(v).split('\n') for k, v in VOLS.items()}


def q(x, places, mode):
    return Decimal(repr(float(x))).quantize(Decimal('1.' + '0' * places), rounding=mode)


def matches(x, printed):
    places = len(printed.split('.')[1]) if '.' in printed else 0
    e, u = str(q(x, places, ROUND_HALF_EVEN)), str(q(x, places, ROUND_HALF_UP))
    return ('EXACT-BOTH' if e == printed == u else
            'EXACT-half-even' if e == printed else
            'EXACT-half-up' if u == printed else 'NO'), e, u


def hdr(t):
    print('\n' + '=' * 96); print(t); print('=' * 96)


# ------------------------------------------------------------------ B1
hdr('B1  27.2 table (L7234-L7239): slack = ambient/actual, log slack swept over three bases')
for name, amb, act, ps, pl in (('Lambda in its bounding box', 6912, 976, '7.082', '1.958'),
                               ('periodic table in R(X)', 126, 90, '1.400', '0.337'),
                               ('calendar in R(X)', 372, 365, '1.019', '0.019')):
    s = amb / act
    print(f'{name:30s} {amb}/{act} = {s!r}  printed {ps} -> {matches(s, ps)[0]}')
    for bn, bv in (('ln', math.e), ('log10', 10.0), ('log2', 2.0)):
        v = math.log(s, bv); t, e, u = matches(v, pl)
        print(f'{"":30s}   {bn:5s} = {v:.6f}  printed {pl} -> {t:15s} (HE {e} / HU {u})')
print('\n  DEVIATION: the periodic-table log column misses in the last place under every base and')
print(f'  both conventions.  exp(0.337) = {math.exp(0.337):.6f}, so the printed log needs')
print(f'  ambient/actual = {math.exp(0.337):.4f}, not the 126/90 = {126/90:.4f} the row prints.')

# ------------------------------------------------------------------ B1b
hdr('B1b  the two bracket rows against the EXACT V, which main L6237 prints as rational')
print('  L6237: "The exact V is rational at every nu - 32/11, 54/13, 256/47, 250/37, 4000/299')
print('          - and 4nu/3 + 4/(9nu) is its asymptote."')
print('  the closed form those five rationals satisfy: V(nu) = 4 nu^3 / (3 nu^2 - 1)')
for nu, printed_rat in ((2, '32/11'), (3, '54/13'), (4, '256/47'), (5, '250/37'), (10, '4000/299')):
    f = Fraction(4 * nu ** 3, 3 * nu ** 2 - 1)
    a, b = printed_rat.split('/')
    ok = f == Fraction(int(a), int(b))
    print(f'    nu={nu:3d}  4nu^3/(3nu^2-1) = {f}  printed {printed_rat}  -> {"MATCH" if ok else "NO"}')
print()
for nu, ps, pl, pbits in ((10, '13.378', '2.594', '3.74'), (40, '53.344', '3.977', '5.74')):
    forms = (('4nu/3 (as L7308 prints the price)', 4 * nu / 3),
             ('4nu/3 + 4/(9nu), the asymptote', 4 * nu / 3 + 4 / (9 * nu)),
             ('4nu^3/(3nu^2-1), exact', float(Fraction(4 * nu ** 3, 3 * nu ** 2 - 1))))
    for lbl, V in forms:
        t, e, u = matches(V, ps)
        print(f'  nu={nu:2d}  {lbl:36s} = {V:.6f}  printed {ps} -> {t:15s} (HE {e} / HU {u})')
        print(f'          ln = {math.log(V):.6f} printed {pl} -> {matches(math.log(V), pl)[0]:15s}'
              f'| log2 = {math.log2(V):.6f} printed {pbits} -> {matches(math.log2(V), pbits)[0]}')
    print(f'          exact as a fraction: {Fraction(4*nu**3, 3*nu**2-1)}')

# ------------------------------------------------------------------ B2
hdr('B2  the 6,912 bounding box, measured on the rebuilt lattice')
T = r2lib.load_tower(); L8 = T.L8(); L9 = T.L9()
A8 = np.array(L8, dtype=np.int64)
lo, hi = A8.min(axis=0), A8.max(axis=0); widths = hi - lo + 1
print(f'|Lambda_8| = {len(L8):,}  |Lambda_9| = {len(L9):,}  coordinates = {A8.shape[1]}')
print('   widths: ' + ' x '.join(str(int(w)) for w in widths))
box = int(np.prod(widths.astype(object)))
print(f'   bounding box = {box:,}  printed 6,912 -> {"MATCH" if box == 6912 else "NO"}')
print(f'   slack = {box}/{len(L8)} = {box/len(L8)!r}  printed 7.082 -> {matches(box/len(L8), "7.082")[0]}')

# ------------------------------------------------------------------ B3
hdr('B3  27.3 bits table (L7251-L7257): E_bits(X) = log2 C(|R(X)|, E(X))')
def log2c(n, k):
    return float(Decimal(math.comb(n, k)).ln() / Decimal(2).ln())
for label, N, E, pb in (('periodic table, 18-column', 126, 36, '105.1'),
                        ('calendar', 372, 7, '47.4'),
                        ('Janet left-step', 126, 0, '0.0'),
                        ('a box ordering, Lambda', 6912, 0, '0.0')):
    v = log2c(N, E)
    print(f'{label:28s} log2 C({N},{E}) = {v:.4f}  printed {pb} -> {matches(v, pb)[0]}')
cand = [N for N in range(9, 8193)
        if '48.5' in (str(q(log2c(N, 8), 1, ROUND_HALF_EVEN)), str(q(log2c(N, 8), 1, ROUND_HALF_UP)))]
print(f'\n  subnet with a hole: |R(X)| and |X| are printed NOWHERE in the section.')
print(f'  inverting the bits column, N with log2 C(N,8) = 48.5: {cand}')
for label, bits, pop, pc in (('periodic table', 105.1, 90, '1.168'), ('calendar', 47.4, 365, '0.130'),
                             ('subnet', 48.5, 248, '0.196'), ('subnet', 48.5, 247, '0.196')):
    print(f'  bits/cell {label:16s} {bits}/{pop} = {bits/pop:.6f} printed {pc} -> {matches(bits/pop, pc)[0]}')
print('  -> the bits/cell column divides by |X|, not by E; both subnet populations round alike,')
print('     so the section fixes neither input.  UNPRINTED INPUT (docket 10).')

# ------------------------------------------------------------------ B4
hdr('B4  Prop. 23.1 (L7266) and "a Rydberg series charges 1.54" (L7267, L7274)')
print(f'  V > 2 <=> log2 V > 1: log2(2) = {math.log2(2)} - an identity of the base, forced for any')
print('  V, therefore not a measurement and not a finding either way (chat 104 rule).')
f32 = Fraction(32, 11)
print(f'\n  the floor of Prop. 23.1 is 32/11 = {float(f32):.6f} (main L6237, L6381; docket 11)')
print(f'  log2(32/11) = {math.log2(float(f32)):.6f}  printed 1.54 -> {matches(math.log2(float(f32)), "1.54")[0]}')
print('  -> 1.54 is the floor expressed in bits.  SOURCED, not a single-witness figure.')
for nu in (2, 3):
    V = float(Fraction(4 * nu ** 3, 3 * nu ** 2 - 1))
    print(f'    cross-check at nu={nu}: exact V = {V:.6f}, log2 = {math.log2(V):.4f}')

# ------------------------------------------------------------------ B5
hdr('B5  27.5.1 (L7316-L7317): order 11.3 % of Lambda_9 pairs, composition 24.7 %, share 0.3 %')
A9 = np.array(L9, dtype=np.int16); n9 = len(A9)
unord = n9 * (n9 - 1) // 2; ordp = n9 * (n9 - 1)
srcs = [r2lib.src(c) for c in L9]; tgts = [r2lib.tgt(c) for c in L9]
keys = sorted(set(srcs) | set(tgts)); ki = {k: i for i, k in enumerate(keys)}
S = np.array([ki[s] for s in srcs]); Tg = np.array([ki[t] for t in tgts])
o = c = sh = 0
for i in range(n9):
    rel_o = np.all(A9[i] <= A9[i + 1:], axis=1) | np.all(A9[i] >= A9[i + 1:], axis=1)
    rel_c = (Tg[i] == S[i + 1:]) | (Tg[i + 1:] == S[i])
    o += int(np.count_nonzero(rel_o)); c += int(np.count_nonzero(rel_c))
    sh += int(np.count_nonzero(rel_o & rel_c))
print(f'  |Lambda_9| = {n9:,}   unordered pairs C(n,2) = {unord:,}   ordered pairs n(n-1) = {ordp:,}')
for lbl, cnt, printed in (('ORDER (r2lib.leq, either direction)', o, '11.3'),
                          ('COMPOSITION (tgt(a) == src(b))', c, '24.7'),
                          ('SHARED by both', sh, '0.3')):
    print(f'  {lbl:36s} {cnt:>9,} pairs')
    print(f'      / unordered = {100.0*cnt/unord:8.4f} %  printed {printed} -> {matches(100.0*cnt/unord, printed)[0]}')
    print(f'      / ordered   = {100.0*cnt/ordp:8.4f} %  printed {printed} -> {matches(100.0*cnt/ordp, printed)[0]}')
print('\n  ORDER and SHARE both reproduce EXACTLY, and only against the ORDERED denominator, which')
print('  the section never states: an unordered numerator over an ordered pair count.  COMPOSITION')
print('  does not reproduce under this reconstruction of the relation.  Under the standing rule the')
print('  reconstruction is the suspect: 24.7 % is recorded as NOT RECONSTRUCTED, not as a deviation.')
print(f'  pairs related by neither relation: {unord - o - c + sh:,} of {unord:,}')

# ------------------------------------------------------------------ B6
hdr('B6  27.5.1 (L7305): d = prod(|Delta_i|+1) = tau(lcm/gcd)')
rng = np.random.default_rng(20260831); bad = 0
for a, b in rng.integers(0, len(A8), size=(4000, 2)):
    if a == b:
        continue
    d1 = 1; d2 = 1
    for e in np.abs(A8[a] - A8[b]):
        d1 *= int(e) + 1
    for x, y in zip(A8[a], A8[b]):
        d2 *= abs(int(x) - int(y)) + 1
    bad += (d1 != d2)
print(f'  4,000 sampled Lambda_8 pairs, mismatches = {bad}.  For non-negative integer exponent')
print('  vectors lcm/gcd carries exponent |Delta_i| in each prime, so tau is the same product:')
print('  STRUCTURALLY FORCED - true for any input, therefore not a finding either way.')

# ------------------------------------------------------------------ B7
hdr('B7  witness sweep: every printed numeral of the unit, digit-bounded, six volumes')
def sweep(tok):
    pat = re.compile(r'(?<![\d.,])' + re.escape(tok) + r'(?![\d])')
    return {k: [i + 1 for i, l in enumerate(ls) if pat.search(l)] for k, ls in LINES.items()
            if any(pat.search(l) for l in ls)}
for tok in ['6,912', '6912', '7.082', '1.958', '13.378', '53.344', '2.594', '3.977', '105.1',
            '47.4', '48.5', '1.168', '0.130', '0.196', '1.54', '3.74', '5.74', '11.3', '24.7',
            '264', '372', '126', '32/11', '4000/299']:
    r = sweep(tok); n = sum(len(v) for v in r.values())
    show = {k: (v[:5] + ['...'] if len(v) > 5 else v) for k, v in r.items()}
    print(f'  {tok:10s} {n:4d} site(s)  {show}')
print('\n  single witnesses (one site, its own): 7.082 1.958 13.378 53.344 2.594 3.977 47.4')
print('  1.168 0.130 0.196 3.74 5.74 - every one of them internally reproduced above.')

hdr('B8  the 27.5.1 table row against its earlier printing at L1970-L1974')
for i in (1970, 1971, 1972, 1973, 1974):
    print(f'  main L{i}| {LINES["main"][i-1].rstrip()[:130]}')
print()
for i in (7304, 7305, 7306, 7307, 7308):
    print(f'  main L{i}| {LINES["main"][i-1].rstrip()[:130]}')
