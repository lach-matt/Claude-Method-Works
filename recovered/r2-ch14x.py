#!/usr/bin/env python3
# r2-ch14x.py - computable batch for the Chapter 25 first read (main L6884-L6990, S25 through S25.5).
# Reads the six volume MEMBERS by name; never opens a BUILDnnn bundle path.
# r2lib imported by path; resolvers take the LINE LIST.
import importlib.util, os, re, sys
from decimal import Decimal, ROUND_HALF_UP

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('r2lib', os.path.join(HERE, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)

VOL = {
    'main':     'The_Method_1_6-2.md',
    'register': 'The_Method_1_6___The_Register-2.md',
    'math':     'The_Method_1_6___Mathematical_Compendium-2.md',
    'phys':     'The_Method_1_6___The_Physics_Compendium-2.md',
    'ioi':      'The_Method_1_6___The_Index_of_Indices-2.md',
    'spectra':  'The_Method_1_6___Spectra_Compendium-2.md',
}
def lines(v):
    return open(os.path.join(HERE, VOL[v]), encoding='utf-8').read().split('\n')

M = lines('main')
UNIT = (6884, 6990)

def q(x, places='0.1'):
    # named convention: ROUND_HALF_UP at the stated number of places; never round()
    return Decimal(repr(float(x))).quantize(Decimal(places), rounding=ROUND_HALF_UP)

def strip_em(s):
    return re.sub(r'[*_`]', '', s)

def digit_sites(vol, tok):
    # digit-bounded numeral sweep: no digit, comma or period may abut the token
    pat = re.compile(r'(?<![\d.,])' + re.escape(tok) + r'(?![\d.,])')
    return [i + 1 for i, l in enumerate(lines(vol)) if pat.search(strip_em(l))]

print('=== r2-ch14x  Chapter 25 first read, computable batch  (main L%d-L%d) ===' % UNIT)

# ---------------------------------------------------------------- X1  R constant in force
print('\n[X1] the R the volumes use')
rs = {}
for v in VOL:
    for i, l in enumerate(lines(v)):
        for m in re.finditer(r'109[,.]?737[.,]?\d*', strip_em(l)):
            rs.setdefault(m.group(0), []).append((v, i + 1))
for k in sorted(rs):
    print('   %-14s %d sites  first %s L%d' % (k, len(rs[k]), rs[k][0][0], rs[k][0][1]))
R = Decimal('109737.31568')
print('   basis taken for this batch: R = %s cm-1 (CODATA R_inf), Z the core charge' % R)

# ---------------------------------------------------------------- X2  the nu_fail table, L6940-L6945
print('\n[X2] L6940-L6945  nu_fail = (2 Z^2 R / dT)^(1/3)')
printed = [('3,000', 3000, '4.2', '6.6'), ('1,000', 1000, '6.0', '9.6'),
           ('100', 100, '13.0', '20.6'), ('10', 10, '28.0', '44.4')]
ok = 0
for lab, dT, p1, p2 in printed:
    v1 = q((2 * 1 ** 2 * float(R) / dT) ** (1 / 3.0)); v2 = q((2 * 2 ** 2 * float(R) / dT) ** (1 / 3.0))
    m1 = 'exact' if str(v1) == p1 else 'DEV'; m2 = 'exact' if str(v2) == p2 else 'DEV'
    ok += (m1 == 'exact') + (m2 == 'exact')
    print('   dT=%-6s Z=1 printed %-5s measured %-5s %-5s | Z=2 printed %-5s measured %-5s %s'
          % (lab, p1, v1, m1, p2, v2, m2))
print('   %d of 8 reproduce exactly at one decimal' % ok)

# ---------------------------------------------------------------- X3  Hg II half-spacing, L6936
print('\n[X3] L6936  Hg II: printed half-spacing 24,634 cm-1 at nu = 5.3')
for Z in (1, 2, 3, 4):
    val = 2 * Z ** 2 * float(R) / 5.3 ** 3
    print('   2Z^2R/nu^3 at Z=%d, nu=5.3 : %s cm-1' % (Z, q(val, '0.1')))
nu_needed = (2 * 4 * float(R) / 24634.0) ** (1 / 3.0)
Z_needed = (24634.0 * 5.3 ** 3 / (2 * float(R))) ** 0.5
print('   to print 24,634 at Z=2 the exponent needs nu = %s ; at nu=5.3 it needs Z = %s'
      % (q(nu_needed, '0.001'), q(Z_needed, '0.001')))
print('   printed / measured(Z=2, nu=5.3) = %s' % q(24634.0 / (2 * 4 * float(R) / 5.3 ** 3), '0.001'))
print('   L6936 also calls the perturbers 2,000-3,000 cm-1 and the displacement "a tenth":')
for Z in (2, 4):
    hs = 2 * Z ** 2 * float(R) / 5.3 ** 3
    print('      at Z=%d  3,000/threshold = %s   2,000/threshold = %s'
          % (Z, q(3000 / hs, '0.001'), q(2000 / hs, '0.001')))
print('      at the printed 24,634  3,000/24,634 = %s  2,000/24,634 = %s'
      % (q(3000 / 24634.0, '0.001'), q(2000 / 24634.0, '0.001')))
# the same section's own table, read back at nu = 5.3
print('   consistency with X2: at Z=2 the table gives nu_fail=6.6 for dT=3,000, and 5.3 < 6.6,')
print('   so L6947 "not deep enough to fail" holds under the table regardless of L6936 arithmetic')

# ---------------------------------------------------------------- X4  the tightest bounds, L6974-L6978
print('\n[X4] L6974-L6978  bound = 2Z^2R/nu^3 at Z=1')
rows = [('Al I', '3s2nf', 54, '54.0', '1.398'), ('Ga I', '4s2np', 54, '51.7', '1.585'),
        ('Li I', 'np', 42, '41.8', '3.25')]
for sp, ch, n, nu, pb in rows:
    places = '0.001' if '.' in pb and len(pb.split('.')[1]) == 3 else '0.01'
    meas = q(2 * float(R) / float(nu) ** 3, places)
    nu_back = (2 * float(R) / float(pb)) ** (1 / 3.0)
    print('   %-5s %-6s n=%d nu=%-5s printed dT<%-6s measured %-8s %s | nu implied by the printed bound: %s'
          % (sp, ch, n, nu, pb, meas, 'exact' if str(meas) == pb else 'DEV', q(nu_back, '0.01')))
print('   L6982 prints 1.4 cm-1 for Al I 3s2 54f: %s the 1.398 row at one decimal'
      % ('consistent with' if str(q(1.398, '0.1')) == '1.4' else 'DEV against'))

# ---------------------------------------------------------------- X5  the percentages of S25.2
print('\n[X5] S25.2 percentages against a 17-cell base')
for k in range(4, 13):
    print('   %2d/17 = %s%%' % (k, q(100.0 * k / 17, '0.1')))
print('   printed 58.8 -> %s ; printed 41.2 -> %s ; printed 35.3 -> %s'
      % ('10/17' if str(q(1000.0 / 17, '0.1')) == '58.8' else 'no k/17',
         '7/17' if str(q(700.0 / 17, '0.1')) == '41.2' else 'no k/17',
         '6/17' if str(q(600.0 / 17, '0.1')) == '35.3' else 'no k/17'))
print('   L6898 "79%%" across the node: k/n forms at or near 79%% -->',
      ', '.join('%d/%d' % (k, n) for n in range(5, 30) for k in range(1, n)
                if str(q(100.0 * k / n, '0.1')) == '79.0'))

# ---------------------------------------------------------------- X6  channel table, bounded and checked
print('\n[X6] channel table parse, spectra L293-L934, checked against its own L900')
S = lines('spectra')
row = re.compile(r'^\|\s*([A-Z][a-z]?\s+[IVX]+)\s*\*?\u2020?\s*\|')
tab = []
for i in range(293, 935):
    l = S[i - 1]
    m = row.match(strip_em(l))
    if not m:
        continue
    cells = [c.strip() for c in strip_em(l).strip('|').split('|')]
    if len(cells) < 11:
        continue
    tab.append((i, cells))
elements = sorted({c[0].split()[0] for _, c in tab})
def toint(s):
    s = s.replace(',', '').strip()
    return int(s) if re.fullmatch(r'\d+', s) else None
interior = sum(toint(c[4]) or 0 for _, c in tab)
print('   rows %d | elements %d | interior cells %d' % (len(tab), len(elements), interior))
print('   L900 states: 596 rows / 28 elements / 2,269 interior cells -> %s'
      % ('AGREES' if (len(tab), len(elements), interior) == (596, 28, 2269) else 'DISAGREES - instrument suspected first'))

print('\n   species this unit names, in the table:')
for sp in ('Sr I', 'Ca II', 'Ba II', 'Ti I', 'Sc VI', 'Hg II', 'Al I', 'Ga I', 'Li I'):
    hits = [(i, c) for i, c in tab if c[0] == sp]
    if not hits:
        print('      %-6s NO ROW ANYWHERE in the channel table' % sp)
        continue
    tot = sum(toint(c[4]) or 0 for _, c in hits)
    print('      %-6s %2d rows, %3d interior cells' % (sp, len(hits), tot))
    for i, c in hits:
        print('         L%-4d %-16s n %-8s levels %-4s interior %-4s bracket %-9s nu %-12s stage %s'
              % (i, c[1], c[2], c[3], c[4], c[5], c[6], c[9]))

print('\n   L6903-L6905: Ca II nd, Ba II nd, Ba II np - the three named channels')
named = [('Ca II', 'nd'), ('Ba II', 'nd'), ('Ba II', 'np')]
tot_int = 0; tot_lev = 0
for sp, ser in named:
    for i, c in tab:
        if c[0] == sp and c[1].split()[0] == ser:
            iv = toint(c[4]) or 0; lv = toint(c[3]) or 0
            tot_int += iv; tot_lev += lv
            print('      %-6s %-4s levels %2d  interior %2d  steps(levels-1) %2d' % (sp, ser, lv, iv, lv - 1))
print('      printed step counts 7 + 6 + 6 = 19 -> members 8+7+7 = 22 -> interior 6+5+5 = %d' % 16)
print('      printed interior base: 17 | table interior for the three named channels: %d' % tot_int)

# ---------------------------------------------------------------- X7  the element stage lists (absent-member test)
print('\n[X7] stage lists for the elements this unit names (absent-member sweep)')
for el in ('Sr', 'Ca', 'Ba', 'Ti', 'Sc', 'Hg', 'Al', 'Ga', 'Li'):
    st = sorted({c[0].split()[1] for _, c in tab if c[0].split()[0] == el})
    print('   %-3s %s' % (el, ' '.join(st) if st else 'NO ROW ANYWHERE'))

# ---------------------------------------------------------------- X8  the totals this unit prints
print('\n[X8] digit-bounded sweeps of the unit\'s collection-wide figures')
for tok in ('1,442', '1,105', '1,061', '619', '892,700', '24,634', '55,000', '42,000'):
    per = {v: digit_sites(v, tok) for v in VOL}
    inunit = [n for n in per['main'] if UNIT[0] <= n <= UNIT[1]]
    tot = sum(len(x) for x in per.values())
    print('   %-8s total %3d | main %3d (unit %d: %s) | %s'
          % (tok, tot, len(per['main']), len(inunit), ','.join('L%d' % n for n in inunit) or '-',
             ' '.join('%s %d' % (v, len(per[v])) for v in ('register', 'math', 'phys', 'ioi', 'spectra') if per[v])))

print('\n[X9] the three counts of S25.4-S25.5 against each other')
print('   L6958 caption: 1,061 cells yield a perturbation bound')
print('   L6970: "Every verified cell yields a bound. Of the 1,442, the 1,105 added in this work"')
print('   L6986: "1,442 cells, each yielding an upper bound"')
print('   1,442 - 1,105 = %d carried from prior art; 1,442 - 1,061 = %d cells with no bound on the caption\'s count'
      % (1442 - 1105, 1442 - 1061))
print('=== end r2-ch14x ===')
