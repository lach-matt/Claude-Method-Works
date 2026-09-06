#!/usr/bin/env python3
"""r2-ch15v - computable batch for chat 114's unit: main L8098-L8221 (SS29.9-SS29.11.2).

The designation arithmetic of SS29.11.2 (103 parsed against ten plus ninety-two);
the growth factor; the 53 per cent; the tripwire's 150 of 216; the age of Baker &
Pixley 1975 against the book's 2026 present; the lattice median as a majority term,
exhaustively on M3, N5 and a product of chains; Lambda_8 as a sublattice and
E(Lambda_8); A.2's statement against the unit's restatement of it; Appendix B's 153
against its own quoted 596; the four register citations, grouped-aware.
Reads members, never a bundle.
"""
import re, importlib.util
from decimal import Decimal, ROUND_HALF_UP
from itertools import product

MEM = '/home/claude/members/'
spec = importlib.util.spec_from_file_location('r2lib', MEM + 'r2lib.py')
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
heading_line, section_span, has_token, enclosing = (
    r2lib.heading_line, r2lib.section_span, r2lib.has_token, r2lib.enclosing)

VOL = {
    'main': 'The_Method_1_6-2.md',
    'reg':  'The_Method_1_6___The_Register-2.md',
    'mc':   'The_Method_1_6___Mathematical_Compendium-2.md',
    'pc':   'The_Method_1_6___The_Physics_Compendium-2.md',
    'ioi':  'The_Method_1_6___The_Index_of_Indices-2.md',
    'sc':   'The_Method_1_6___Spectra_Compendium-2.md',
}
V = {k: open(MEM + f, encoding='utf-8').read().split('\n') for k, f in VOL.items()}
M = V['main']
LO, HI = 8098, 8221
UNIT = M[LO - 1:HI]


# --- owed to r2lib: body_range (heading -> next heading of ANY rank) ---------
# lifted verbatim from r2-ch15t.py (chat 113)
def body_range(Mx, sec):
    s = heading_line(Mx, sec)
    if s is None:
        return None
    for i in range(s + 1, len(Mx) + 1):
        if re.match(r'^#{1,6} ', Mx[i - 1].strip()):
            return (s, i)
    return (s, len(Mx) + 1)


# --- owed to r2lib: digit-bounded numeral sweep ------------------------------
# lifted verbatim from r2-ch15t.py (chat 113)
def num_sites(lines, num):
    pat = r'(?<![0-9])' + re.escape(num) + r'(?![0-9])'
    return [i for i, t in enumerate(lines, 1) if re.search(pat, t)]


# --- owed to r2lib: grouped-aware register lookup ----------------------------
# lifted verbatim from r2-ch15u.py (chat 113)
def register_entry(n):
    R = V['reg']
    for i, t in enumerate(R, 1):
        s = t.strip()
        if re.match(r'^#{1,4}\s*%d\s*$' % n, s):
            return ('bare', i)
        m = re.match(r'^#{1,4}\s*([\d,\s]+)$', s)
        if m and str(n) in [x.strip() for x in m.group(1).split(',')]:
            return ('grouped', i)
    return (None, None)


def q(x, places='0.01'):
    """Decimal quantize, ROUND_HALF_UP - the named convention for every figure here."""
    return Decimal(x).quantize(Decimal(places), rounding=ROUND_HALF_UP)


def head(t):
    print('\n' + '=' * 78 + '\n' + t + '\n' + '=' * 78)


# =============================================================================
head('V1  unit extent by heading scan; body_range against section_span')
for sec in ('29.8', '29.9', '29.9.1', '29.10', '29.11', '29.11.1', '29.11.2', '28.10', '29.12'):
    hlx = heading_line(M, sec)
    br, sp = body_range(M, sec), section_span(M, sec)
    same = 'COINCIDE' if br == sp else 'DIFFER'
    print(f'  SS{sec:<9} heading L{hlx}   body_range {br}   section_span {sp}   {same}')
print(f'  unit taken: L{LO}-L{HI} = {HI - LO + 1} lines; last line before SS28.10 at '
      f'L{heading_line(M, "28.10")} (read in chat 111)')

# =============================================================================
head('V2  the designation arithmetic of SS29.11.2 - the unit\'s spine')
print('  printed: L8190 "Of 103 designations parsed, ten carry an explicit parent term"')
print('           L8196 "Ninety-two carried none - and forty-four of those"')
print('           L8199 "fifty-four checkable designations of one hundred and two"')
print('           L8209 "Fifty-four of one hundred and two is 53%" / "the forty-eight left out"')
ten, ninety_two, forty_four = 10, 92, 44
print(f'  MEASURED  ten + ninety-two            = {ten + ninety_two}   printed parsed total 103   '
      f'{"AGREES" if ten + ninety_two == 103 else "CONFLICT"}')
print(f'  MEASURED  ten + forty-four            = {ten + forty_four}   printed checkable 54       '
      f'{"AGREES" if ten + forty_four == 54 else "CONFLICT"}')
for tot in (102, 103):
    print(f'  MEASURED  {tot} - 54 left out          = {tot - 54:3d}   printed "forty-eight"       '
          f'{"AGREES" if tot - 54 == 48 else "CONFLICT"}   (total {tot})')
    print(f'  MEASURED  54 / {tot} as a percentage   = {q(Decimal(54) / Decimal(tot) * 100)}%  '
          f'-> {q(Decimal(54) / Decimal(tot) * 100, "1")}% at 0 dp; printed "53%"')
print(f'  MEASURED  growth factor 54 / 10       = {q(Decimal(54) / Decimal(10), "0.1")}   '
      f'printed "a factor of five and a half" = 5.5   '
      f'{"AGREES" if q(Decimal(54)/Decimal(10), "0.1") == Decimal("5.5") else "CONFLICT"}')
print(f'  MEASURED  a 5.5x growth from ten would need {int(round(10 * 5.5))} checkable, not 54')
print('  digit-bounded sites of each figure, unit then six volumes:')
for n in ('103', '102', '92', '54', '48', '44', '10', '153'):
    u = num_sites(UNIT, n)
    tot = {k: len(num_sites(V[k], n)) for k in VOL}
    print(f'    {n:>4}  unit lines {[LO - 1 + i for i in u]}   volumes ' +
          ' '.join(f'{k}:{v}' for k, v in tot.items()))

# =============================================================================
head('V3  the tripwire figure L8173-74 against SS16.3.1 itself')
src = heading_line(M, '16.3.1')
print(f'  SS16.3.1 heading L{src}; body_range {body_range(M, "16.3.1")}')
for i in num_sites(M, '216'):
    if re.search(r'150 of 216', M[i - 1]):
        print(f'  L{i}: {M[i-1].strip()[:104]}')
print(f'  MEASURED  150 / 216 = {q(Decimal(150) / Decimal(216) * 100)}% -> '
      f'{q(Decimal(150) / Decimal(216) * 100, "0.1")}% at 1 dp; both sites print 69.4%')
for fig in ('69.4', '69.6', '69.2', '68.1'):
    s = [i for i, t in enumerate(M, 1) if re.search(r'(?<![0-9])' + fig.replace('.', r'\.') + r'(?![0-9])', t)]
    print(f'    {fig}%  main sites {s}')

# =============================================================================
head('V4  "fifty years" against Baker & Pixley 1975 and the book\'s 2026 present')
present = 2026
print(f'  MEASURED  {present} - 1975 = {present - 1975} years')
for ph in ('fifty years', 'fifty-year', 'fifty years late', 'since 1975', 'binary-determined'):
    hits = {k: [i for i, t in enumerate(V[k], 1) if re.search(re.escape(ph), t, re.I)] for k in VOL}
    print(f'  "{ph}": ' + '  '.join(f'{k}{v}' for k, v in hits.items() if v))
print(f'  2025 main sites (the book\'s present is 2026): {num_sites(M, "2025")}')

# =============================================================================
head('V5  the lattice median is a majority term - exhaustive on M3, N5, chains')


def maj_ok(elems, meet, join):
    bad = []
    for x, y in product(elems, repeat=2):
        m1 = join(join(meet(x, x), meet(x, y)), meet(x, y))
        m2 = join(join(meet(x, y), meet(x, x)), meet(y, x))
        m3 = join(join(meet(y, x), meet(y, x)), meet(x, x))
        if not (m1 == x and m2 == x and m3 == x):
            bad.append((x, y, m1, m2, m3))
    return bad


# M3, the diamond: 0 < a,b,c < 1, pairwise meets 0 and joins 1 - non-distributive
M3 = ['0', 'a', 'b', 'c', '1']


def m3_meet(x, y):
    return x if x == y else ('0' if '0' in (x, y) or (x != '1' and y != '1') else (x if y == '1' else y))


def m3_join(x, y):
    return x if x == y else ('1' if '1' in (x, y) or (x != '0' and y != '0') else (x if y == '0' else y))


# N5, the pentagon: 0 < a < b < 1, 0 < c < 1, c incomparable with a and b
N5 = ['0', 'a', 'b', 'c', '1']
LE = {('0', z) for z in N5} | {(z, '1') for z in N5} | {
    ('a', 'a'), ('b', 'b'), ('c', 'c'), ('a', 'b')}


def n5_meet(x, y):
    c = [z for z in N5 if (z, x) in LE and (z, y) in LE]
    return max(c, key=lambda z: sum((w, z) in LE for w in N5))


def n5_join(x, y):
    c = [z for z in N5 if (x, z) in LE and (y, z) in LE]
    return min(c, key=lambda z: sum((w, z) in LE for w in N5))


CH = list(product(range(4), range(3), range(5)))
for name, E, mt, jn in (('M3 (non-distributive)', M3, m3_meet, m3_join),
                        ('N5 (non-modular)', N5, n5_meet, n5_join),
                        ('4x3x5 product of chains', CH,
                         lambda x, y: tuple(map(min, x, y)),
                         lambda x, y: tuple(map(max, x, y)))):
    bad = maj_ok(E, mt, jn)
    print(f'  {name:26s} |L| = {len(E):4d}   pairs {len(E)**2:6d}   '
          f'majority-term failures {len(bad)}   {"OK" if not bad else bad[:2]}')
print('  m(x,y,z) = (x^y) v (x^z) v (y^z) satisfies m(x,x,y) = m(x,y,x) = m(y,x,x) = x')
print('  => the lattice median IS a majority term, as L8130 states.')

# =============================================================================
head('V6  Lambda_8 is a sublattice, and E(Lambda_8)')
CAPS = (3, 3, 1, 3, 1)
L8 = r2lib.L8_at(CAPS)
print(f'  |Lambda_8| at caps {CAPS} = {len(L8)}   expected 976   '
      f'{"OK" if len(L8) == 976 else "FAIL"}')
pairs, join_leaks, meet_leaks = r2lib.closure(L8)
print(f'  MEASURED  ordered pairs tested {pairs:,}; join leaks {join_leaks}; meet leaks {meet_leaks}')
print(f'  => Lambda_8 {"IS" if join_leaks == 0 and meet_leaks == 0 else "IS NOT"} closed under '
      f'componentwise meet and join: a sublattice of the product of chains (L8143).')
Rx = r2lib.Rset(L8)
print(f'  MEASURED  |R(Lambda_8)| = {len(Rx)}   E = |R(X)| - |X| = {len(Rx) - len(L8)}   '
      f'printed E(Lambda) = 0   {"AGREES" if len(Rx) - len(L8) == 0 else "CONFLICT"}')
print('  L8147 prints the definition E(X) = |R(X)| - |X|; it reproduces the book\'s E(Lambda) = 0.')

# =============================================================================
head('V7  A.2\'s statement against the unit\'s restatement, and Appendix D\'s coordinate')
for i in (3683, 3686, 3691, 3708, 3709):
    print(f'  ch14  L{i}: {M[i-1].strip()[:100]}')
for i in (8127, 8132, 8135, 8137, 8143):
    print(f'  unit  L{i}: {M[i-1].strip()[:100]}')
for i, t in enumerate(M, 1):
    if re.search(r'A\.2', t) and re.search(r'found|none', t, re.I):
        print(f'  coord L{i} (in {enclosing(M, i)}): {t.strip()[:104]}')
print('  L8137 says the coordinate CHANGES from none found to found; the printed row is measured above.')

# =============================================================================
head('V8  Appendix B\'s 153 against the channel table it quotes')
B = body_range(M, '10165') if False else None
for i in (10169, 10195, 10196, 10197, 10203, 10205):
    print(f'  main L{i}: {M[i-1].strip()[:108]}')
SC = V['sc']
print(f'  spectra member: {len(SC)} lines; Section II span L293-L934, totals line L900:')
print(f'    L900: {SC[899].strip()[:110]}')
for n in ('596', '153', '70 species', '28 elements'):
    print(f'    "{n}" sc sites {[i for i, t in enumerate(SC, 1) if n in t][:8]}')
print(f'  L8189 cites "Appendix B\'s own 153 channels"; Appendix B L10169 prints 153, and its own')
print(f'  B.2 quote L10195-97 prints 596 channel rows across 28 elements and 70 species.')

# =============================================================================
head('V9  the four register citations of the unit, grouped-aware')
for n, site in ((251, 8220), (252, 8220), (253, 8213), (254, 8213)):
    kind, line = register_entry(n)
    R = V['reg']
    hl = ''
    if line:
        for j in range(line, min(line + 6, len(R))):
            if R[j - 1].strip().startswith('**'):
                hl = R[j - 1].strip()[:96]
                break
    print(f'  register {n}: {kind} at reg L{line}  cited from main L{site}')
    print(f'    headline: {hl}')
print('  the claim at L8210-13 is about published channel notation fixing the coupling parent.')
print('  the claim at L8215-20 is about referee flag 5 moving to targets identified.')
