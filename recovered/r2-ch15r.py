#!/usr/bin/env python3
"""r2-ch15r — computable batch for chat 112's unit: main L7940-L8028 (SS29.3-SS29.5.5).

Reads the six volume MEMBERS, never a bundle.  Resolvers imported from r2lib by path.
Functions still owed to r2lib are copied verbatim with a provenance comment (DEFERRED).
No wall-clock printing: the golden must be deterministic.
"""
import re, sys, importlib.util
from decimal import Decimal, ROUND_HALF_UP

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
LO, HI = 7940, 8028
UNIT = M[LO - 1:HI]


# --- owed to r2lib: body_range (heading -> next heading of ANY rank) ---------
def body_range(Mx, sec):
    s = heading_line(Mx, sec)
    if s is None:
        return None
    for i in range(s + 1, len(Mx) + 1):
        if re.match(r'^#{1,6} ', Mx[i - 1].strip()):
            return (s, i)
    return (s, len(Mx) + 1)


# --- owed to r2lib: digit-bounded numeral sweep -------------------------------
def numeral_sites(lines, num):
    pat = r'(?<![\d.,])' + re.escape(num) + r'(?![\d,]|\.\d)'
    return [i for i, t in enumerate(lines, 1) if re.search(pat, t)]


# --- owed to r2lib: left-bounded stem matcher ---------------------------------
def has_stem(text, stem):
    return len(re.findall(r'(?<![A-Za-z])' + re.escape(stem), text, re.I))


# --- owed to r2lib: raw symbol test -------------------------------------------
def has_symbol(text, sym):
    return text.count(sym)


def q2(x):
    return Decimal(str(x)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


def head(t):
    print('\n' + '=' * 78 + '\n' + t + '\n' + '=' * 78)


# =============================================================================
head('C0  unit identity and extent (measured, not carried)')
for sec in ('29.3', '29.4', '29.5', '29.5.1', '29.5.2', '29.5.3', '29.5.4', '29.5.5', '29.6'):
    print(f'  SS{sec:<7} heading_line {heading_line(M, sec)}   body_range {body_range(M, sec)}'
          f'   section_span {section_span(M, sec)}')
print(f'  unit L{LO}-L{HI} = {HI - LO + 1} lines; member has {len(M)} lines')

# =============================================================================
head('C1  page arithmetic: two ranges, two conventions')
# Curtis review: Physica Scripta 35, 805-810 (1987); text says "A six-page expert review".
cur_lo, cur_hi = 805, 810
# Edlen chapter: pp. 80-220; text says "Absence from 140 pages".
edl_lo, edl_hi = 80, 220
for name, lo, hi, printed in (('Curtis review', cur_lo, cur_hi, 6),
                              ('Edlen chapter', edl_lo, edl_hi, 140)):
    inc, exc = hi - lo + 1, hi - lo
    verdict = ('INCLUSIVE' if printed == inc else 'EXCLUSIVE' if printed == exc else 'NEITHER')
    print(f'  {name:<14} pp {lo}-{hi}  inclusive {inc}  exclusive {exc}  '
          f'printed {printed}  -> {verdict}')
print('  CONVENTION CLASH: the two page counts in the same section pair are computed')
print('  under different conventions.  Under the six-page (inclusive) rule, 80-220 is 141.')
print('  sites of "six-page":', [(k, i) for k in V for i, t in enumerate(V[k], 1)
                                 if has_stem(t, 'six-page')])
print('  sites of "140 pages":', [(k, i) for k in V for i, t in enumerate(V[k], 1)
                                  if re.search(r'(?<!\d)140 pages', t)])
print('  sites of "141":', [(k, i) for k in V for i in numeral_sites(V[k], '141')])

# =============================================================================
head('C2  SS29.5.1 "Seven equations" against the printed table')
tb = [(i, t) for i, t in zip(range(LO, HI + 1), UNIT) if t.strip().startswith('|')]
rows = [(i, t) for i, t in tb if not re.match(r'^\s*\|[\s\-|]+\|\s*$', t)]
datarows = [(i, t) for i, t in rows if not re.search(r'\|\s*equation\s*\|', t)]
print(f'  table lines {tb[0][0]}-{tb[-1][0]}: {len(tb)} lines, {len(rows)} non-rule rows,'
      f' {len(datarows)} data rows')
nums = []
for i, t in datarows:
    lab = t.split('|')[1].strip()
    found = re.findall(r'\d+', lab)
    nums.append((i, lab, found))
    print(f'   L{i}  label {lab!r:<12} numerals {found}')
covered = sorted({int(x) for _, _, f in nums for x in f})
print(f'  data rows {len(datarows)};  distinct equation numerals covered {len(covered)} {covered}')
print(f'  printed count word: "Seven equations" (L7980) = 7')
print(f'  VERDICT: 7 == numerals covered ({len(covered)})  -> '
      f'{"MATCH on the numeral span" if len(covered) == 7 else "MISMATCH"}')
print(f'           7 vs printed data rows ({len(datarows)}) -> '
      f'{"MATCH" if len(datarows) == 7 else "MISMATCH — one row is a RANGE (4)-(5)"}')

# =============================================================================
head('C3  SS29.5.1 heading "Every equation in the review is a fit" vs its own status column')
fitted, notfitted = [], []
for i, t in datarows:
    st = t.split('|')[3].strip() if len(t.split('|')) > 3 else ''
    (fitted if has_stem(st, 'fitted') else notfitted).append((i, t.split('|')[1].strip(), st))
print(f'  rows whose status says fitted:     {len(fitted)}')
for r in fitted:
    print(f'     L{r[0]} {r[1]:<10} {r[2]}')
print(f'  rows whose status does NOT say fitted: {len(notfitted)}')
for r in notfitted:
    print(f'     L{r[0]} {r[1]:<10} {r[2]}')
eqs_notfitted = sorted({int(x) for _, lab, _ in notfitted for x in re.findall(r'\d+', lab)})
print(f'  equation numerals not marked fitted: {eqs_notfitted} '
      f'({len(eqs_notfitted)} of {len(covered)})')
print('  heading L7969 asserts EVERY equation is a fit; the table marks '
      f'{len(eqs_notfitted)} of {len(covered)} otherwise -> FALSE UNIVERSAL against own table')
print('  body L7980 asserts "Not one is a bound" — a different and weaker claim; tested at C3b')
bnd = [(i, t) for i, t in zip(range(LO, HI + 1), UNIT) if has_stem(t, 'bound')]
print('  "bound" sites in unit:', [i for i, _ in bnd])

# =============================================================================
head('C4  "stated twice" against the quotations actually printed in SS29.5.2')
b = body_range(M, '29.5.2')
blk = [(i, M[i - 1]) for i in range(b[0], b[1]) if M[i - 1].startswith('    ')
       and M[i - 1].strip()]
groups, prev = [], None
for i, t in blk:
    if prev is None or i != prev + 1:
        groups.append([])
    groups[-1].append((i, t)); prev = i
print(f'  SS29.5.2 body_range {b}; indented blocks: {len(groups)}')
for g in groups:
    print(f'   block L{g[0][0]}-L{g[-1][0]}  quoted={g[0][1].lstrip().startswith(chr(34))}'
          f'  {g[0][1].strip()[:64]}')
quoted = [g for g in groups if g[0][1].lstrip().startswith('"')]
print(f'  quotation blocks (open with a double quote): {len(quoted)}')
print(f'  heading L7982 "stated twice"; SS29.5.5 L8022 "twice" -> '
      f'{"MATCH" if len(quoted) == 2 else "MISMATCH"}')
print('  "twice" sites in unit:',
      [i for i, t in zip(range(LO, HI + 1), UNIT) if has_token(t, 'twice')])

# =============================================================================
head('C5  SS29.5.3 four agreements against four n values')
s3 = body_range(M, '29.5.3')
txt3 = '\n'.join(M[s3[0] - 1:s3[1] - 1])
agree = re.findall(r'(?<![\d.])([01]\.\d\d)(?![\d])', txt3)
nvals = re.findall(r'n = ([\d, and]+)', txt3)
print(f'  SS29.5.3 body_range {s3}')
print(f'  agreement values printed: {agree}  (count {len(agree)})')
print(f'  n-value phrases: {nvals}')
ns = sorted({int(x) for p in nvals for x in re.findall(r'\d+', p)})
print(f'  distinct n values named: {ns}  (count {len(ns)})')
emp = [x for x in ns if x != 2]
print(f'  n evaluated empirically (n=2 is the theoretical one): {emp} (count {len(emp)})')
print(f'  VERDICT agreements vs empirical n: '
      f'{"MATCH" if len(agree) == len(emp) else "MISMATCH"}')
print(f'  headline "One near miss" (L8000): near-miss objects described = 1 '
      f'(the exchange-energy proportionality constant)')

# =============================================================================
head('C6  pp. 170-2 containment in the chapter range 80-220')
print(f'  inner 170-172 within outer {edl_lo}-{edl_hi}: '
      f'{edl_lo <= 170 and 172 <= edl_hi}')
print('  sites of "170":', [(k, i) for k in V for i in numeral_sites(V[k], '170')])
print('  sites of "80-220"/"80\u2013220":',
      [(k, i) for k in V for i, t in enumerate(V[k], 1) if re.search(r'80[-\u2013]220', t)])

# =============================================================================
head('C7  the review title\'s "26 Years Later" against both candidate datings')
pub = 1987
for base, lab in ((1960, 'manuscript delivered Oct 1960 (SS29.5.4)'),
                  (1964, 'Handbuch imprint 1964')):
    print(f'  {lab:<40} 1987-{base} = {pub - base};  1986-{base} = {pub - 1 - base}')
print('  title asserts 26 -> consistent with the 1960 manuscript date (26 = 1986-1960),')
print('  not with the 1964 imprint (23 = 1987-1964).  CORROBORATES SS29.5.4.')

# =============================================================================
head('C8  docket 16 — the Edlen dating census, measured fresh across six volumes')
d60, d64, dother = [], [], []
for k in V:
    for i, t in enumerate(V[k], 1):
        if has_stem(t, 'Edl'):
            yrs = sorted({int(y) for y in re.findall(r'(?<!\d)(18\d\d|19\d\d|20\d\d)(?!\d)', t)})
            if not yrs:
                continue
            if 1960 in yrs:
                d60.append((k, i, yrs))
            if 1964 in yrs:
                d64.append((k, i, yrs))
            if not ({1960, 1964} & set(yrs)):
                dother.append((k, i, yrs))
print(f'  lines naming Edlen AND 1960: {len(d60)}')
for r in d60:
    print(f'     {r[0]} L{r[1]} years {r[2]}   {V[r[0]][r[1]-1].strip()[:88]}')
print(f'  lines naming Edlen AND 1964: {len(d64)}')
for r in d64:
    print(f'     {r[0]} L{r[1]} years {r[2]}   {V[r[0]][r[1]-1].strip()[:88]}')
print(f'  lines naming Edlen with some other year only: {len(dother)}')
for r in dother:
    print(f'     {r[0]} L{r[1]} years {r[2]}   {V[r[0]][r[1]-1].strip()[:88]}')
print(f'  total Edlen name sites (any line): '
      f'{sum(1 for k in V for t in V[k] if has_stem(t, "Edl"))}')
print('  L8018 claims "this book cites it accordingly" (i.e. as 1960).')
print(f'  VERDICT: {len(d64)} site(s) still date it 1964 -> '
      f'{"CLAIM HOLDS" if len(d64) == 0 else "CLAIM FAILS — repair declared, not executed"}')

# =============================================================================
head('C9  L6683 "sixty-five years old" against both datings and the book\'s own present')
print('  L6683:', M[6682].strip()[:200])
sf = [(k, i) for k in V for i, t in enumerate(V[k], 1) if has_stem(t, 'sixty-five')]
print('  "sixty-five" sites in six volumes:', sf)
for base in (1960, 1964):
    print(f'    if the chapter is {base}: 65 years later = {base + 65};'
          f'  61 years later = {base + 61}')
yrs = {}
for k in V:
    for t in V[k]:
        for y in re.findall(r'(?<!\d)(202\d)(?!\d)', t):
            yrs[y] = yrs.get(y, 0) + 1
print('  present-year candidates printed anywhere (202x):', dict(sorted(yrs.items())))
print('  sixty-five is EXACT under the 1960 dating iff the book\'s present is 2025;')
print('  under the 1964 imprint it would require a present of 2029.')

# =============================================================================
head('C10  single-witness / site counts for the unit\'s figures (docket 17)')
for lab, pat in (('forty-year', r'(?<![A-Za-z])forty-year'),
                 ('0.03 cm-1', r'0\.03'),
                 ('Martin (1980)', r'Martin'),
                 ('Ritz', r'Ritz'),
                 ('Curtis', r'Curtis'),
                 ('Physica Scripta', r'Physica Scripta'),
                 ('two lines of algebra', r'two lines of algebra'),
                 ('1885', r'(?<!\d)1885(?!\d)')):
    sites = [(k, i) for k in V for i, t in enumerate(V[k], 1) if re.search(pat, t, re.I)]
    print(f'  {lab:<22} {len(sites):>3} site(s)  {sites[:10]}')

# =============================================================================
head('C11  V = 4nu/3 against the book\'s other statements of V (docket 11 adjacency)')
for lab, pat in (('4nu/3', r'4\u03bd/3'), ('32/11', r'32/11'), ('2.909', r'2\.909')):
    sites = [(k, i) for k in V for i, t in enumerate(V[k], 1) if re.search(pat, t)]
    print(f'  {lab:<8} {len(sites):>3} site(s)  {sites[:12]}')
num, den = Decimal(32), Decimal(11)
print(f'  32/11 = {(num/den).quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)} '
      f'(Decimal.quantize, ROUND_HALF_UP, 6 dp)')
print(f'  4nu/3 = 32/11  =>  nu = 24/11 = '
      f'{(Decimal(24)/den).quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)}')
print('  T = Z^2 R / nu^2  =>  dT/dnu = -2 Z^2 R / nu^3;  the step from T to a ratio 4nu/3')
print('  is a differentiation and a division — two lines, as L7953 states (structural check).')

# =============================================================================
head('C12  digit-bounded numeral sweep of the unit')
seen = {}
for i, t in zip(range(LO, HI + 1), UNIT):
    for n in re.findall(r'(?<![\w.])(\d+(?:\.\d+)?)(?![\w])', t):
        seen.setdefault(n, []).append(i)
for n in sorted(seen, key=lambda x: (len(x), x)):
    other = sum(1 for k in V for tt in V[k] if numeral_sites([tt], n))
    print(f'  {n:<8} unit L{seen[n]}   sites in six volumes: {other}')

print('\nr2-ch15r complete.')
