#!/usr/bin/env python3
# r2-ch16y -- COMPUTABLE batch for the chat-127 section read: main L9609-L9715 (34.5-34.10).
# Reads MEMBERS only.  Deterministic; prints no wall-clock time.
#
# The walk's data source is NIST ASD GSIE (register 1306: "Stored as ground.py"); ground.py is not a
# member.  Section 3 therefore carries the standard NIST neutral ground configurations Z = 1..108 as
# EXPLICIT INSTRUMENT DATA, validated against every anchor the Register prints about that table before
# any result is read.  Everything computed from it is a RECONSTRUCTION: where it disagrees with the
# record, the finding is about the reconstruction (RULINGS-R2 / CLAUDE.md §5).
import os, re, importlib.util, math
from decimal import Decimal, ROUND_HALF_UP, getcontext
getcontext().prec = 40

H = '/home/claude/members'
spec = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
from r2lib import heading_line, section_span, has_token, enclosing

def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
def hr(t): print('\n' + '=' * 96 + '\n' + t + '\n' + '=' * 96)
def q7(x): return str(Decimal(str(x)).quantize(Decimal('0.0000001'), rounding=ROUND_HALF_UP))
def q4(x): return str(Decimal(str(x)).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP))
def q3(x): return str(Decimal(str(x)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
def pct2(x): return str(Decimal(str(x)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))

MAIN = rd('The_Method_1_6-2.md'); REG = rd('The_Method_1_6___The_Register-2.md')
A, B = 9609, 9715

# owed to r2lib (DEFERRED): body_range, carried with provenance from r2-ch16m (chat 121).
def body_range(M, sec):
    s = heading_line(M, sec)
    if s is None: return None
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1].strip()): return (s, i)
    return (s, len(M) + 1)

# ---------------------------------------------------------------- 0. the unit, resolved twice
hr('0  UNIT BOUNDARY -- body_range and section_span, both, for every heading of the unit')
for sec in ['34.5', '34.6', '34.7', '34.8', '34.9', '34.10', '34', '35']:
    print('  §%-6s heading_line %-6s body_range %-14s section_span %s'
          % (sec, heading_line(MAIN, sec), body_range(MAIN, sec), section_span(MAIN, sec)))
print('  unit bound by body_range: L%d-L%d (%d lines); "## 35." body at L%d'
      % (A, B, B - A + 1, heading_line(MAIN, '35')))

# ---------------------------------------------------------------- 1. arithmetic of the unit
hr('1  ARITHMETIC PRINTED IN THE UNIT, recomputed (Decimal, HALF_UP, convention named)')
D = Decimal
def dsqrt(x): return D(x).sqrt()
print('  §34.5 L9614: L,U = Δn(√p_g+√p_r)/(p_g−p_r) is the rationalised form of Δn/(√p_g−√p_r):')
worst = D(0)
for pg in range(0, 8):
    for pr in range(0, 8):
        if pg == pr: continue
        lhs = (dsqrt(pg) + dsqrt(pr)) / (pg - pr); rhs = 1 / (dsqrt(pg) - dsqrt(pr))
        worst = max(worst, abs(lhs - rhs))
print('    identity holds on all 56 ordered pairs p ≤ 7, max |difference| = %s' % worst)
print('    sign: register 1309 prints (Δn)/(√pᵣ − √p_g) with Δn = nᵣ − n_g; the unit prints the')
print('    same quotient with both differences reversed -- the same number (two sign flips).')
print('\n  §34.5 L9619-L9620: (√(n−1) + √(n−4))/3 at n = 4..7, HALF_UP to the printed 7 dp:')
printed = {4: '0.5773503', 5: '1.0000000', 6: '1.2168450', 7: '1.3938270'}
for n in range(4, 8):
    v = (dsqrt(n - 1) + dsqrt(n - 4)) / 3
    v7 = str(v.quantize(D('0.0000001'), rounding=ROUND_HALF_UP)); v4 = str(v.quantize(D('0.0001'), rounding=ROUND_HALF_UP))
    print('    n=%d  computed %s  printed %s  %s   (4 dp: %s)'
          % (n, v7, printed[n], 'EXACT' if v7 == printed[n] else 'MISMATCH at 7 dp', v4))
print('    1/(√5−√2) = %s  (register 1322 calls it "1.2168"; register 1317 prints "1.2167")'
      % str((1 / (dsqrt(5) - dsqrt(2))).quantize(D('0.0000001'), rounding=ROUND_HALF_UP)))
print('    also (√(n−1)+√(n−4))/3 IS Δn/(√p_g−√p_r) for ns vs (n−1)d: p_g = n−1, p_r = n−4, Δn = 1, p_g−p_r = 3.')

print('\n  §34.7 L9641-L9642: "1.028 at p across four subshells and 1.785 at d across two: the ratio is √3 to 0.19%"')
p_open = [D('1.0925'), D('1.0331'), D('1.0124'), D('1.0237')]   # register 1337: 3p, 4p, 5p, 6p at opening
d_open = [D('1.8453'), D('1.7240')]                             # register 1337: 4d, 5d
lt_p = [D('1.120'), D('1.049'), D('1.022'), D('1.002')]        # Λ_t p row, main L9646 / reg 1354 / ioi L1759
lt_d = [D('1.819'), D('1.433')]                                 # Λ_t d row, ioi L1760
def mean(xs): return sum(xs) / len(xs)
def median(xs):
    s = sorted(xs); k = len(s)
    return (s[k // 2 - 1] + s[k // 2]) / 2 if k % 2 == 0 else s[k // 2]
r3 = dsqrt(3)
for label, P_, D_ in [('register 1337 opening values', p_open, d_open), ('Λ_t table rows (ioi L1759-L1760)', lt_p, lt_d)]:
    for conv, f in [('median', median), ('mean', mean)]:
        p, d = f(P_), f(D_); ratio = d / p; dev = (ratio / r3 - 1) * 100
        print('    %-34s %-6s p %s d %s ratio %s  vs √3: %s%%'
              % (label, conv, q3(p), q3(d), q4(ratio), pct2(dev)))
print('    register 1337 states the ratio as 1.7354 and 0.19%%: 1.7354/√3 − 1 = %s%%' % pct2((D('1.7354') / r3 - 1) * 100))
print('    ratio of the PRINTED 3-dp figures 1.785/1.028 = %s, vs √3: %s%%'
      % (q4(D('1.785') / D('1.028')), pct2((D('1.785') / D('1.028') / r3 - 1) * 100)))
print('    -> 1.028 and 1.785 are the MEDIANS of register 1337\'s opening values (mean gives 1.040 / 1.785,')
print('       ratio 1.7153, 0.97% BELOW √3); neither the unit nor register 1337/1350 names the convention.')
print('    -> the Λ_t rows the unit\'s next paragraph prints give 1.036 (median) / 1.626 and ratio 1.570 (−9.4%).')

print('\n  §34.7 L9646: "6p sits 0.2%% above the centrifugal value": √(1·2/2) = 1; (1.002 − 1)/1 = %s%%'
      % pct2((D('1.002') - 1) * 100))
print('  t(ℓ) = √(ℓ(ℓ+1)/2): ℓ=0 %s, ℓ=1 %s, ℓ=2 %s, ℓ=3 %s (register 1337: √6 = 2.4495 at f)'
      % tuple(q4(dsqrt(D(l * (l + 1)) / 2)) for l in range(4)))
print('  §34.6 L9624-L9626: 8 + 6 + 4 = %d (printed "eighteen")' % (8 + 6 + 4))
print('  §34.9 L9663: Z = 3 to 108 is %d elements (printed 106)' % (108 - 3 + 1))
print('  §34.10 L9702-L9705: four + two = %d (printed "six appearances")' % (4 + 2))
print('  §34.10 L9704: is 1/(2ℓ+1) an appearance of ℓ(ℓ+1)?  ℓ(ℓ+1) vs 2ℓ+1 at ℓ = 1,2,3: %s'
      % [(l * (l + 1), 2 * l + 1) for l in (1, 2, 3)])
print('    ℓ(ℓ+1) = 2ℓ+1 iff ℓ² − ℓ − 1 = 0 iff ℓ = (1+√5)/2: never at an integer ℓ. Two functions, not one object.')
print('  §34.9 L9666: "At any f opening p = n−ℓ−1 = 0": 4f p = %d, 5f p = %d' % (4 - 3 - 1, 5 - 3 - 1))
print('  §34.10 L9698: "Seven of eight rules give 106/106" -- register 1331: seven of eight, one at 74/106. 7 + 1 = 8.')
print('  register 1463 lists fourteen emptying points: %d listed' % len([37, 42, 43, 45, 55, 58, 64, 65, 80, 91, 96, 97, 103, 104]))

# ---------------------------------------------------------------- 2. what the Register says at each figure
hr('2  THE REGISTER AT EACH FIGURE OF THE UNIT -- earlier statement, and the LATER entry that moved it')
def rhead(i):
    j = i
    while j > 0 and not re.match(r'^### \d', REG[j - 1]): j -= 1
    return REG[j - 1].strip('# ').strip()
def rsites(pat):
    return [(rhead(i), i) for i, l in enumerate(REG, 1) if re.search(pat, l)]
for label, pat in [('106 of 106 / 106 non-empty', r'106 of 106|106 non-empty'), ('99 of 106', r'99 of 106'),
                   ('90 of 106', r'90 of 106'), ('eighteen resets/recalibrations', r'eighteen (resets|recalibrations)'),
                   ('"ten resets" / "ten moves"', r'ten (resets|moves)'), ('fifteen moves', r'fifteen moves'),
                   ('104 of 106', r'104 of 106'), ('nineteen surds / distinct values', r'nineteen (surds|distinct)'),
                   ('DEACTIVATED', r'DEACTIVATED'), ('No parameter is fitted', r'No parameter is fitted'),
                   ('Exceptionless on 106', r'Exceptionless on 106'), ('blocked four fits', r'blocked four fits'),
                   ('BLOCKED (protocol replay)', r'BLOCKED'), ('1.028', r'\b1\.028\b'), ('1.785', r'\b1\.785\b'),
                   ('1.029', r'\b1\.029\b'), ('every f opening / any f opening', r'(every|any) f opening'),
                   ('Lr 7p configuration', r'Lr, which is|7s²7p')]:
    s = rsites(pat)
    print('  %-36s %d sites: %s' % (label, len(s), ', '.join('R%s L%d' % x for x in s[:14])))

# ---------------------------------------------------------------- 3. the reconstruction: NIST table
hr('3  RECONSTRUCTION INPUT -- NIST neutral ground configurations Z = 1..108 (instrument data), VALIDATED')
CORE = {'He': {'1s': 2}, 'Ne': {'1s': 2, '2s': 2, '2p': 6}, 'Ar': {'1s': 2, '2s': 2, '2p': 6, '3s': 2, '3p': 6},
        'Kr': {'1s': 2, '2s': 2, '2p': 6, '3s': 2, '3p': 6, '3d': 10, '4s': 2, '4p': 6},
        'Xe': {'1s': 2, '2s': 2, '2p': 6, '3s': 2, '3p': 6, '3d': 10, '4s': 2, '4p': 6, '4d': 10, '5s': 2, '5p': 6},
        'Rn': {'1s': 2, '2s': 2, '2p': 6, '3s': 2, '3p': 6, '3d': 10, '4s': 2, '4p': 6, '4d': 10, '5s': 2, '5p': 6,
               '4f': 14, '5d': 10, '6s': 2, '6p': 6}}
SYM = ('H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr '
       'Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb '
       'Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf '
       'Db Sg Bh Hs').split()
RAW = """1 - 1s1|2 - 1s2|3 He 2s1|4 He 2s2|5 He 2s2 2p1|6 He 2s2 2p2|7 He 2s2 2p3|8 He 2s2 2p4|9 He 2s2 2p5|10 He 2s2 2p6|
11 Ne 3s1|12 Ne 3s2|13 Ne 3s2 3p1|14 Ne 3s2 3p2|15 Ne 3s2 3p3|16 Ne 3s2 3p4|17 Ne 3s2 3p5|18 Ne 3s2 3p6|
19 Ar 4s1|20 Ar 4s2|21 Ar 3d1 4s2|22 Ar 3d2 4s2|23 Ar 3d3 4s2|24 Ar 3d5 4s1|25 Ar 3d5 4s2|26 Ar 3d6 4s2|27 Ar 3d7 4s2|
28 Ar 3d8 4s2|29 Ar 3d10 4s1|30 Ar 3d10 4s2|31 Ar 3d10 4s2 4p1|32 Ar 3d10 4s2 4p2|33 Ar 3d10 4s2 4p3|34 Ar 3d10 4s2 4p4|
35 Ar 3d10 4s2 4p5|36 Ar 3d10 4s2 4p6|37 Kr 5s1|38 Kr 5s2|39 Kr 4d1 5s2|40 Kr 4d2 5s2|41 Kr 4d4 5s1|42 Kr 4d5 5s1|
43 Kr 4d5 5s2|44 Kr 4d7 5s1|45 Kr 4d8 5s1|46 Kr 4d10|47 Kr 4d10 5s1|48 Kr 4d10 5s2|49 Kr 4d10 5s2 5p1|50 Kr 4d10 5s2 5p2|
51 Kr 4d10 5s2 5p3|52 Kr 4d10 5s2 5p4|53 Kr 4d10 5s2 5p5|54 Kr 4d10 5s2 5p6|55 Xe 6s1|56 Xe 6s2|57 Xe 5d1 6s2|
58 Xe 4f1 5d1 6s2|59 Xe 4f3 6s2|60 Xe 4f4 6s2|61 Xe 4f5 6s2|62 Xe 4f6 6s2|63 Xe 4f7 6s2|64 Xe 4f7 5d1 6s2|65 Xe 4f9 6s2|
66 Xe 4f10 6s2|67 Xe 4f11 6s2|68 Xe 4f12 6s2|69 Xe 4f13 6s2|70 Xe 4f14 6s2|71 Xe 4f14 5d1 6s2|72 Xe 4f14 5d2 6s2|
73 Xe 4f14 5d3 6s2|74 Xe 4f14 5d4 6s2|75 Xe 4f14 5d5 6s2|76 Xe 4f14 5d6 6s2|77 Xe 4f14 5d7 6s2|78 Xe 4f14 5d9 6s1|
79 Xe 4f14 5d10 6s1|80 Xe 4f14 5d10 6s2|81 Xe 4f14 5d10 6s2 6p1|82 Xe 4f14 5d10 6s2 6p2|83 Xe 4f14 5d10 6s2 6p3|
84 Xe 4f14 5d10 6s2 6p4|85 Xe 4f14 5d10 6s2 6p5|86 Xe 4f14 5d10 6s2 6p6|87 Rn 7s1|88 Rn 7s2|89 Rn 6d1 7s2|90 Rn 6d2 7s2|
91 Rn 5f2 6d1 7s2|92 Rn 5f3 6d1 7s2|93 Rn 5f4 6d1 7s2|94 Rn 5f6 7s2|95 Rn 5f7 7s2|96 Rn 5f7 6d1 7s2|97 Rn 5f9 7s2|
98 Rn 5f10 7s2|99 Rn 5f11 7s2|100 Rn 5f12 7s2|101 Rn 5f13 7s2|102 Rn 5f14 7s2|103 Rn 5f14 7s2 7p1|104 Rn 5f14 6d2 7s2|
105 Rn 5f14 6d3 7s2|106 Rn 5f14 6d4 7s2|107 Rn 5f14 6d5 7s2|108 Rn 5f14 6d6 7s2"""
CONF = {}
for rec in RAW.replace('\n', '').split('|'):
    parts = rec.split(); Z = int(parts[0]); core = parts[1]
    c = dict(CORE[core]) if core != '-' else {}
    for tok in parts[2:]:
        m = re.match(r'(\d)([spdf])(\d+)$', tok); c[m.group(1) + m.group(2)] = int(m.group(3))
    CONF[Z] = c
LQ = {'s': 0, 'p': 1, 'd': 2, 'f': 3, 'g': 4}
def nl(sh): return int(sh[0]), LQ[sh[1]]
def cap(sh): return 2 * (2 * nl(sh)[1] + 1)
bad = [Z for Z in CONF if sum(CONF[Z].values()) != Z]
print('  108 of 108 electron counts validate: %s (register 1306 states the same of ground.py)' % ('YES' if not bad else bad))
print('  Pd = %s ; Lr = %s  (register 1306: [Kr]4d¹⁰ no 5s; [Rn]5f¹⁴7s²7p not 6d)'
      % ({k: v for k, v in CONF[46].items() if k in ('4d', '5s')}, {k: v for k, v in CONF[103].items() if k in ('5f', '6d', '7s', '7p')}))
def entrant(Z):
    a, b = CONF[Z - 1], CONF[Z]
    gains = [(b[s] - a.get(s, 0), s) for s in b if b[s] - a.get(s, 0) > 0]
    return max(gains)[1]
ENT = {Z: entrant(Z) for Z in range(2, 109)}
opening = {}
for Z in range(1, 109):
    for s in CONF[Z]:
        if CONF[Z][s] > 0 and s not in opening: opening[s] = Z
seq = sorted(opening, key=lambda s: opening[s])
print('  opening sequence read from the table: %s' % ' '.join(seq))
print('  printed at L9507 :                     1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s 5d 4f 6p 7s 6d 5f 7p')
print('  Z of each opening: %s' % ', '.join('%s@%d' % (s, opening[s]) for s in seq))
print('  openings inside Z ≤ 108: %d of %d ; 7p opens at Z = %d (Lr)' % (sum(1 for s in seq if opening[s] <= 108), len(seq), opening['7p']))
print('  chat 126 (16x-01) derived 7p at Z = 113 by COMPLETE SEQUENTIAL FILLING of the printed sequence:')
cum = 0
for s in seq:
    print('    complete-filling opening of %s at Z = %-3d  table says %-3d %s' % (s, cum + 1, opening[s], '' if cum + 1 == opening[s] else '<-- differs'))
    cum += cap(s)
print('  -> that derivation is exact at 5d (57) and 6d (89) and WRONG at 4f, 5f and 7p, where blocks interleave;')
print('     the population of 108 neutrals CONTAINS the 7p opening (Lr, 103): register 1306 L4897 is the witness.')
mad_miss = []
for Z in range(3, 109):
    prev = CONF[Z - 1]
    cands = [s for s in [f'{n}{l}' for n in range(1, 9) for l in 'spdf' if LQ[l] < n] if prev.get(s, 0) < cap(s)]
    pick = min(cands, key=lambda s: (nl(s)[0] + nl(s)[1], nl(s)[0]))
    if pick != ENT[Z]: mad_miss.append(SYM[Z - 1] + str(Z))
print('  conditional-Madelung misses: %s -> score %d of 106 (register 1437: 96; Mo Rh Pd La Gd Au Ac Th Cm Lr)'
      % (' '.join(mad_miss), 106 - len(mad_miss)))
for Z, s in [(25, '4s'), (43, '5s'), (64, '5d'), (96, '6d')]:
    print('  register 1447 interruption at Z=%d: entrant %s (expected %s)' % (Z, ENT[Z], s))
for pair in [(42, 43), (64, 65), (96, 97), (79, 80)]:
    print('  §34.6 return pair %s->%s: %s -> %s' % (SYM[pair[0] - 1], SYM[pair[1] - 1],
          {k: v for k, v in CONF[pair[0]].items() if k in ENT[pair[0]] or k in ('4s', '5s', '6s', '7s', '5d', '6d')},
          {k: v for k, v in CONF[pair[1]].items() if k in ENT[pair[1]] or k in ('4s', '5s', '6s', '7s', '5d', '6d')}))

# ---------------------------------------------------------------- 4. corridors under both forms
hr('4  THE CORRIDOR L(Z) < a < U(Z), entrant against every Pauli-admissible rival, BOTH forms, Z = 3..108')
INF = float('inf')
def radicand(sh, q, form):
    n, l = nl(sh); p = n - l - 1
    return p + (q / cap(sh) if form == 'q' else 0.0)
def corridor(Z, cand, form, NMAX=7, LMAX=3):
    prev = CONF[Z - 1]
    cands = [f'{n}{l}' for n in range(1, NMAX + 1) for l in 'spdfg' if LQ[l] < n and LQ[l] <= LMAX]
    cands = [s for s in cands if prev.get(s, 0) < cap(s)]
    lo, hi, infeasible = -INF, INF, False
    Ps = math.sqrt(radicand(cand, prev.get(cand, 0), form)); ns = nl(cand)[0]
    for r in cands:
        if r == cand: continue
        Pr = math.sqrt(radicand(r, prev.get(r, 0), form)); c = Pr - Ps; d = nl(r)[0] - ns
        if abs(c) < 1e-12:
            if d <= 0: infeasible = True
        elif c > 0: hi = min(hi, d / c)
        else: lo = max(lo, d / c)
    return (lo, hi, infeasible, cands)
def rnd(x): return round(x, 9)
for form, name in [('p', 'node-only  ν = n − a√p        (registers 1309, 1328, 1330)'), ('q', 'finished   ν = n − a√(p + q/cap) (§34.4 L9583, register 1350)')]:
    print('\n  FORM: %s' % name)
    nonempty = 0; ends = set(); ends_pos = set(); one_sided = []; memo = []; rows = {}
    for Z in range(3, 109):
        lo, hi, bad_, cands = corridor(Z, ENT[Z], form)
        ok = (not bad_) and lo < hi
        nonempty += ok; rows[Z] = (lo, hi)
        for e in (lo, hi):
            if e not in (INF, -INF): ends.add(rnd(e)); ends_pos.add(rnd(e)) if e > 1e-12 else None
        if lo == -INF or hi == INF: one_sided.append(Z)
        k = 0; kpos = 0
        for c in cands:
            l2, h2, b2, _ = corridor(Z, c, form)
            if not b2 and l2 < h2: k += 1; kpos += (h2 > max(l2, 0.0))
        memo.append((Z, k, kpos))
    print('    entrant corridor non-empty: %d of 106   (printed "All 106 non-empty")' % nonempty)
    print('    distinct finite endpoint values over the 106 corridors: %d ; excluding 0: %d   (printed "Nineteen distinct surds")'
          % (len(ends), len(ends_pos)))
    # FAULT 3, self-caught: one generator convention is not a count.  Sweep (NMAX, LMAX) and say which.
    gen = []
    for NM, LM in [(7, 3), (8, 3), (7, 4), (8, 4), (9, 4)]:
        e2 = set(); e2p = set(); ne = 0
        for Z in range(3, 109):
            lo, hi, bd, _ = corridor(Z, ENT[Z], form, NM, LM); ne += (not bd) and lo < hi
            for e in (lo, hi):
                if e not in (INF, -INF):
                    e2.add(rnd(e))
                    if e > 1e-12: e2p.add(rnd(e))
        gen.append('n≤%d,ℓ≤%d: %d (excl. 0: %d, non-empty %d)' % (NM, LM, len(e2), len(e2p), ne))
    print('    generator sweep -> ' + ' | '.join(gen))
    print('    one-sided corridors (L = −∞ or U = +∞): %d steps: %s' % (len(one_sided), ' '.join(SYM[Z - 1] + str(Z) for Z in one_sided)))
    for Z in (19, 37, 55, 57, 58, 87, 91, 103):
        lo, hi = rows[Z]; print('    Z=%-3d %-3s entrant %s  (L, U) = (%s, %s)' % (Z, SYM[Z - 1], ENT[Z], q7(lo) if lo != -INF else '−∞', q7(hi) if hi != INF else '+∞'))
    from collections import Counter
    dist = Counter(k for _, k, _ in memo); dist_pos = Counter(k for _, _, k in memo)
    print('    memoryless test (§34.6 "104 of 106 steps admit two to four self-consistent subshells"):')
    print('      candidates with a NON-EMPTY corridor per step, any real a : %s ; steps with 2..4: %d ; with 1: %d'
          % (dict(sorted(dist.items())), sum(v for k, v in dist.items() if 2 <= k <= 4), dist.get(1, 0)))
    print('      requiring a > 0                                        : %s ; steps with 2..4: %d ; with 1: %d'
          % (dict(sorted(dist_pos.items())), sum(v for k, v in dist_pos.items() if 2 <= k <= 4), dist_pos.get(1, 0)))
    # running intersection (register 1401/1463): forced emptyings
    lo_r, hi_r = -INF, INF; empt = []
    for Z in range(3, 109):
        lo, hi = rows[Z]; nlo, nhi = max(lo_r, lo), min(hi_r, hi)
        if nlo >= nhi: empt.append(Z); lo_r, hi_r = lo, hi
        else: lo_r, hi_r = nlo, nhi
    print('    running intersection empties at: %s -> %d times  (register 1463: 14 at 37 42 43 45 55 58 64 65 80 91 96 97 103 104)'
          % (' '.join(map(str, empt)), len(empt)))
    # the handshake walk (register 1328): keep a if inside, else nearest endpoint
    a = None; resets = []; score = 0; hist = []
    for Z in range(3, 109):
        lo, hi = rows[Z]
        # prediction BEFORE placement: least ν among admissible candidates at the held a (higher-n tie-break, register 1438)
        if a is not None:
            _, _, _, cands = corridor(Z, ENT[Z], form); prev = CONF[Z - 1]
            best = min(cands, key=lambda s: (nl(s)[0] - a * math.sqrt(radicand(s, prev.get(s, 0), form)), -nl(s)[0]))
            score += (best == ENT[Z])
        inside = a is not None and lo < a < hi
        if not inside:
            new = (lo if lo != -INF else (hi if hi != INF else 0.0)) if a is None else (lo if a <= lo else hi)
            if new in (INF, -INF): new = 0.0
            if abs(new) < 1e-12: new = 0.0                      # FAULT 2, self-caught: d/c with d = 0, c < 0 gives -0.0
            if a is None or abs(new - a) > 1e-12: resets.append((Z, new))
            a = new
        hist.append((Z, a))
    kinds = []
    for Z, v in resets:
        ent = ENT[Z]; prev = CONF[Z - 1]
        kind = 'opening' if opening.get(ent) == Z else ('return' if Z in (43, 65, 97, 80) else ('exception' if SYM[Z - 1] + str(Z) in mad_miss or Z in (24, 29, 41, 44, 78, 58, 91, 92, 93) else 'other'))
        kinds.append(kind)
    print('    handshake walk (a kept if inside, else nearest endpoint): resets %d at %s'
          % (len(resets), ' '.join('%s%d=%s' % (SYM[Z - 1], Z, q4(v)) for Z, v in resets)))
    print('      reset kinds: %s   (printed 8 openings + 6 exceptions + 4 returns = 18; register 1402: ten..thirty-three)' % dict(Counter(kinds)))
    print('      in-sample score of the held a at each step (higher-n tie-break), Z = 4..108: %d of 105' % score)
    print('      register 1328 trajectory: K .5774 Rb 1.0000 Cs 1.2168 La .7071 Hg .8090 Fr 1.3938 Pa 1.3660 Lr 1.9841')

# ---------------------------------------------------------------- 5. the f openings
hr('5  §34.9 "At any f opening p = n−ℓ−1 = 0 ... L = −∞" tested at BOTH f openings, both forms')
for form in ('p', 'q'):
    for Z in (58, 91):
        lo, hi, bad_, cands = corridor(Z, ENT[Z], form); n, l = nl(ENT[Z])
        below = [r for r in cands if r != ENT[Z] and nl(r)[0] < n]
        print('  form %s  Z=%d %s entrant %s  p = %d  admissible rivals with smaller n: %s  corridor (%s, %s)'
              % (form, Z, SYM[Z - 1], ENT[Z], n - l - 1, below or 'NONE', q7(lo) if lo != -INF else '−∞', q7(hi) if hi != INF else '+∞'))
print('  -> 4f: p = 0, every inequality an upper bound, L = −∞ by the node floor as stated.')
print('  -> 5f: p = 1 ≠ 0; L is unbounded because every smaller-n rival is FULL (admissibility), not because of the node floor.')

print('\nEND r2-ch16y')
