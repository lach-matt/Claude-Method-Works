#!/usr/bin/env python3
"""r2-ch14v — computable batch for the Chapter 24 third read, main L6817-L6883
(SS24.10 Two cross-checks, SS24.11 Four ways a species declines, SS24.12 The census,
SS24.13 What the structure determines).

Reads the six volume MEMBERS by name; never a BUILDnnn bundle path (HANDOFF-53).
Imports heading_line / section_span / has_token / enclosing from r2lib by path and
passes them the LINE LIST, never the member text.  No wall-clock output.
"""
import os, re, sys, importlib.util
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction

H = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(_s); _s.loader.exec_module(r2lib)
heading_line, section_span, has_token, enclosing = (
    r2lib.heading_line, r2lib.section_span, r2lib.has_token, r2lib.enclosing)

def lines(name):
    return open(os.path.join(H, name), encoding='utf-8').read().split('\n')

MAIN = lines('The_Method_1_6-2.md')
SPEC = lines('The_Method_1_6___Spectra_Compendium-2.md')
REG  = lines('The_Method_1_6___The_Register-2.md')
VOLS = [('main', MAIN), ('register', REG),
        ('math', lines('The_Method_1_6___Mathematical_Compendium-2.md')),
        ('physics', lines('The_Method_1_6___The_Physics_Compendium-2.md')),
        ('index', lines('The_Method_1_6___The_Index_of_Indices-2.md')),
        ('spectra', SPEC)]

def q(x, dp='0.1'):
    """Named convention: HALF_UP at the stated precision.  Never round()."""
    return Decimal(x).quantize(Decimal(dp), rounding=ROUND_HALF_UP)

print('== P1  unit span, re-measured (never carried)')
for s in ('24', '24.10', '24.11', '24.12', '24.13', '25'):
    print('   S%-6s heading %s' % (s, heading_line(MAIN, s)))
sp = section_span(MAIN, '24')
u0, u1 = heading_line(MAIN, '24.10'), heading_line(MAIN, '25') - 1
print('   chapter 24 span %s  unit L%d-L%d = %d lines, %d headings'
      % (sp, u0, u1, u1 - u0 + 1,
         sum(1 for i in range(u0, u1 + 1) if re.match(r'^#{1,4} 24', MAIN[i - 1]))))

print('== P2  S24.10 Al I disagreement, at the source\'s precision')
asd, km = Decimal('47379.7'), Decimal('47379.140')
d = asd - km
print('   ASD %s - K&M %s = %s   printed 0.560 -> %s'
      % (asd, km, d, 'reproduces' if d == Decimal('0.560') else 'DEVIATION'))
print('   K&M carries 3 dp, ASD 1 dp; difference quoted at 3 dp = %s' % q(d, '0.001'))

print('== P3  S24.11 Cu II straddle (L6837)')
ce = (107942, 111124); ry = (108014, 110366)
print('   core-excited %s vs Rydberg %s -> straddles below %s, above %s'
      % (ce, ry, ce[0] < ry[0], ce[1] > ry[1]))

print('== P4  S24.12 D by enumerating antisymmetric states of a shell')
def levels(l, k):
    """Number of J levels of the equivalent-electron configuration l^k, from the M_J
    distribution over antisymmetric (Slater) states.  2*M_J is used to stay integral."""
    orbs = [(2 * ml, ms) for ml in range(-l, l + 1) for ms in (1, -1)]
    from itertools import combinations
    cnt = {}
    for comb in combinations(orbs, k):
        mj = sum(a + b for a, b in comb)
        cnt[mj] = cnt.get(mj, 0) + 1
    n = 0
    while any(v > 0 for v in cnt.values()):
        J = max(m for m, v in cnt.items() if v > 0)
        for m in range(-J, J + 1, 2):
            cnt[m] = cnt.get(m, 0) - 1
        n += 1
    return n
D = {('p', 4): levels(1, 4)}
for k in (3, 4, 5, 6, 7, 8, 9):
    D[('d', k)] = levels(2, k)
for key in sorted(D, key=lambda t: (t[0], t[1])):
    print('   D(%s^%d) = %d' % (key[0], key[1], D[key]))
core = [D[('d', k)] for k in (3, 4, 5, 6, 7)]
print('   Cr-,Mn-,Fe-,Co-,Ni-like ionic cores d3..d7 -> %s  range %d to %d  printed 19 to 37 -> %s'
      % (core, min(core), max(core), 'reproduces' if (min(core), max(core)) == (19, 37) else 'DEVIATION'))
print('   S24.11 Ne II "5 core J levels": core 2p^4 -> D = %d -> %s'
      % (D[('p', 4)], 'reproduces' if D[('p', 4)] == 5 else 'DEVIATION'))
print('   Cu II\'s own core, as L6837 prints the series (3d9.5s -> core 3d9): D = %d, which is <= 2'
      % D[('d', 9)])
print('   S24.12 arithmetic 27 admitted + 12 exceptional + 5 excluded = %d sequences' % (27 + 12 + 5))

print('== P5  channel table parse, bounded to section II and checked against its own totals line')
t0 = next(i for i, t in enumerate(SPEC, 1) if t.startswith('# II '))
t1 = next(i for i, t in enumerate(SPEC, 1) if i > t0 and re.match(r'^#{1,2} I(II|V)? ', t))
tot = next(i for i in range(t0, t1) if '596 channel rows' in SPEC[i - 1])
ROWS = []
for i in range(t0, t1):
    t = SPEC[i - 1]
    if not t.startswith('|'):
        continue
    c = [x.strip() for x in t.strip('|').split('|')]
    if len(c) != 11 or c[0] in ('species', '---'):
        continue
    m = re.match(r'^([A-Z][a-z]?)\s+([IVX]+)\s*\*?$', c[0])
    if not m:
        continue
    ROWS.append(dict(ln=i, sp=m.group(1) + ' ' + m.group(2), el=m.group(1),
                     stage=m.group(2), ser=c[1], lev=int(c[3]), inter=int(c[4]),
                     br=c[5], d=c[7], fits=c[9]))
els = sorted({r['el'] for r in ROWS})
print('   section II = L%d-L%d, totals line L%d' % (t0, t1 - 1, tot))
print('   parsed %d rows, %d elements, %d interior cells  vs stated 596 / 28 / 2,269 -> %s'
      % (len(ROWS), len(els), sum(r['inter'] for r in ROWS),
         'AGREES' if (len(ROWS), len(els), sum(r['inter'] for r in ROWS)) == (596, 28, 2269)
         else 'PARSE SUSPECT - instrument wrong until proved otherwise'))

print('== P6  S24.11 cells column against every compendium base')
def base(sp):
    rs = [r for r in ROWS if r['sp'] == sp]
    k = m = 0
    nt = un = 0
    for r in rs:
        b = r['br']
        mm = re.match(r'^(\d+)/(\d+)$', b)
        if mm:
            m += int(mm.group(1)); k += int(mm.group(2))
        elif b == 'no-triple':
            nt += 1
        else:
            un += 1
    return len(rs), sum(r['inter'] for r in rs), k, m, nt, un
print('   species    printed | rows interior tested passed no-triple untested')
for sp, pr in (('Ne II', 0), ('Ar II', 10), ('Si I', 4), ('P II', 1),
               ('Cu II', 0), ('Bi II', 0), ('Bi III', 0)):
    b = base(sp)
    hit = [n for n, v in zip(('rows', 'interior', 'tested', 'passed', 'no-triple', 'untested'), b) if v == pr]
    print('   %-9s %7d | %4d %8d %6d %6d %9d %8d   matches: %s'
          % (sp, pr, b[0], b[1], b[2], b[3], b[4], b[5], ','.join(hit) or 'NO BASE'))

print('== P7  S24.13 leave-one-out fit  delta(Z) = d_inf + a/Z + b/Z^2')
def dv(sp, ser):
    r = [x for x in ROWS if x['sp'] == sp and x['ser'] == ser]
    return Fraction(r[0]['d'].replace('+', '')) if r else None
SEQ = {'lithium-like': [('Li I', 'ns 2S'), ('Be II', 'ns ²S'), ('B III', 'ns 2S J=1/2'), ('C IV', 'ns')],
       'sodium-like': [('Na I', 'ns'), ('Mg II', 'ns ²S'), ('Al III', 'ns 2S J=1/2'), ('Si IV', 'ns 2S J=1/2')]}
PRINTED = {'lithium-like': ['11.1', '1.4', '0.8', '1.8'],
           'sodium-like': ['23.4', '2.4', '1.3', '2.5']}
def solve(pts, z):
    (z1, y1), (z2, y2), (z3, y3) = pts
    import itertools
    A = [[Fraction(1), Fraction(1, z1), Fraction(1, z1 * z1), y1],
         [Fraction(1), Fraction(1, z2), Fraction(1, z2 * z2), y2],
         [Fraction(1), Fraction(1, z3), Fraction(1, z3 * z3), y3]]
    for c in range(3):
        p = next(r for r in range(c, 3) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        A[c] = [x / A[c][c] for x in A[c]]
        for r in range(3):
            if r != c and A[r][c]:
                f = A[r][c]; A[r] = [a - f * b for a, b in zip(A[r], A[c])]
    a, b, cc = A[0][3], A[1][3], A[2][3]
    return a + b * Fraction(1, z) + cc * Fraction(1, z * z)
for name, mem in SEQ.items():
    got = [(i + 1, dv(sp, ser)) for i, (sp, ser) in enumerate(mem)]
    miss = [mem[i][0] for i, (_, v) in enumerate(got) if v is None]
    print('   %s ns basis: %s' % (name, ', '.join(
        '%s Z=%d %s' % (mem[i][0], z, ('absent' if v is None else str(float(v)))) for i, (z, v) in enumerate(got))))
    if miss:
        print('       CANNOT COMPUTE - no compendium row for %s; the printed column is uncheckable'
              % ', '.join(miss))
        continue
    for i in range(4):
        pts = [(z, v) for j, (z, v) in enumerate(got) if j != i]
        pred = solve(pts, got[i][0]); act = got[i][1]
        err = abs(pred - act) / abs(act) * 100
        print('       hold Z=%d  predicted %.4f  actual %.4f  error %s%%  printed %s%%  %s'
              % (got[i][0], float(pred), float(act), q(float(err)), PRINTED[name][i],
                 'reproduces' if str(q(float(err))) == PRINTED[name][i] else 'DOES NOT REPRODUCE'))

print('== P8  S24.13 Z=1->2 ratio against the five pairs of S24.6, every shared series')
PAIRS = [('helium-like', 'He I', 'Li II'), ('lithium-like', 'Li I', 'Be II'),
         ('sodium-like', 'Na I', 'Mg II'), ('aluminium-like', 'Al I', 'Si II'),
         ('potassium-like', 'K I', 'Ca II')]
def dmap(sp):
    out = {}
    for r in ROWS:
        if r['sp'] != sp:
            continue
        m = re.search(r'n([spdfghi])', r['ser'])
        if m:
            out.setdefault(m.group(1), []).append(float(r['d'].replace('+', '')))
    return {k: sum(v) / len(v) for k, v in out.items()}
rat = []
for nm, a, b in PAIRS:
    A, B = dmap(a), dmap(b)
    sh = sorted(set(A) & set(B), key='spdfghi'.index)
    rr = [(o, B[o] / A[o]) for o in sh if A[o] != 0]
    print('   %-15s %s' % (nm, '  '.join('%s %.3f' % (o, v) for o, v in rr) or 'no shared series'))
    rat += [v for _, v in rr]
sr = [v for v in rat if 0 < v < 3]
print('   printed span 0.53-0.83; measured over all shared series: min %.3f max %.3f'
      % (min(rat), max(rat)))
print('   s-series only: %s' % ' '.join('%.3f' % (dmap(b).get('s', 0) / dmap(a)['s'])
                                        for _, a, b in PAIRS if dmap(a).get('s')))

print('== P9  S24.13 L6882 "every sequence entered through its neutral or first ion"')
ROM = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6}
mn = {}
for r in ROWS:
    v = ROM[r['stage']]
    mn[r['el']] = min(mn.get(r['el'], 99), v)
bad = {e: v for e, v in mn.items() if v > 2}
print('   %d elements; entry stage I: %d, II: %d, III or higher: %d %s'
      % (len(mn), sum(1 for v in mn.values() if v == 1), sum(1 for v in mn.values() if v == 2),
         len(bad), bad if bad else ''))
print('   carbon stages present: %s' % sorted({r['stage'] for r in ROWS if r['el'] == 'C'},
                                              key=lambda s: ROM[s]))

print('== P10  retired-basis sweep (14t-01) across the unit, the chapter and the volume')
un = '\n'.join(MAIN[u0 - 1:u1]); ch = '\n'.join(MAIN[sp[0] - 1:sp[1] - 1]); vol = '\n'.join(MAIN)
for tok in ('1,442', 'thirty-five', '1,105', '869', '930', '546', '789'):
    print('   %-12s unit %d  chapter %d  volume %d'
          % (tok, un.count(tok), ch.count(tok), vol.count(tok)))
print('   unit carries a collection-wide total: %s'
      % ('no' if not any(un.count(t) for t in ('1,442', '1,105', '869', '930', '546')) else 'yes'))

print('== P11  S24.13 own table against its own rule')
tab = {'lithium-like': {'neutral': '11.1', 'Z=4': '1.8'}, 'sodium-like': {'neutral': '23.4', 'Z=4': '2.5'}}
for k, v in tab.items():
    print('   %-13s neutral end %s%%   upper end Z=4 %s%%   ratio %sx'
          % (k, v['neutral'], v['Z=4'], q(float(v['neutral']) / float(v['Z=4'])))) 
print('   L6876 "interior ... ~1%%" / L6877 "at an end ... not determined" / L6879 "the ends always must"')
print('   both upper ends sit at 1.8-2.5%%, inside a factor 2 of the interior band and 6-13x below the neutral')
