#!/usr/bin/env python3
# r2-ch14r.py — chat 99, computable batch for the section read of main L6623-L6740
# (Chapter 24 opening through §24.7).  Reads the six volume MEMBERS by name; never a
# BUILDnnn bundle path.  r2lib imported by path; nothing copied.  Rounding is
# Decimal.quantize, ROUND_HALF_UP, to the number of places the source prints; round() unused.
#
# Basis note, stated because a negative result from a sweep is a statement about the sweep:
# the Spectra Compendium's Section II states its own totals at L900 — "596 channel rows across
# 28 elements · 2,269 interior cells parsed" — and this instrument's parse reproduces that line
# exactly, so the parse is the compendium's own basis and not a reconstruction of it.

import re, math, importlib.util
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction

MEM = '/home/claude/members/'
spec = importlib.util.spec_from_file_location('r2lib', MEM + 'r2lib.py')
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
heading_line, section_span, has_token, enclosing = (
    r2lib.heading_line, r2lib.section_span, r2lib.has_token, r2lib.enclosing)

VOLS = {'main': 'The_Method_1_6-2.md', 'spectra': 'The_Method_1_6___Spectra_Compendium-2.md',
        'math': 'The_Method_1_6___Mathematical_Compendium-2.md',
        'phys': 'The_Method_1_6___The_Physics_Compendium-2.md',
        'ioi': 'The_Method_1_6___The_Index_of_Indices-2.md',
        'register': 'The_Method_1_6___The_Register-2.md'}
V = {k: open(MEM + f, encoding='utf-8').read().split('\n') for k, f in VOLS.items()}
MAIN, SPEC = V['main'], V['spectra']

def q(x, places):
    if isinstance(x, Fraction):
        d = Decimal(x.numerator) / Decimal(x.denominator)
    elif isinstance(x, Decimal):
        d = x
    else:
        d = Decimal(str(x))
    return d.quantize(Decimal(1).scaleb(-places), rounding=ROUND_HALF_UP)

def verdict(tag, ok, msg):
    print(f'{"OK " if ok else "DEV"}  {tag:9s} {msg}')

print('=== r2-ch14r  computable batch, main L6623-L6740 (Chapter 24 opening through §24.7) ===')

# ---------------------------------------------------------------- boundaries
lo, hi = 6623, 6740
h24, h248, h25 = heading_line(MAIN, '24'), heading_line(MAIN, '24.8'), heading_line(MAIN, '25')
print('\n-- boundaries (exact-token resolver, never prefix, never heading rank) --')
verdict('bound', h24 == lo and h248 == hi + 1, f'unit L{lo}-L{hi}: 24 at L{h24}, 24.8 at L{h248}, 25 at L{h25}')
verdict('chapter', section_span(MAIN, '24') == (6623, 6884), f'section_span(24) = {section_span(MAIN, "24")}')

# ---------------------------------------------------------------- parse the channel table
def strip_marks(s):
    return s.replace('*', '').replace('†', '').replace('‡', '').strip()

sec2_lo = next(i for i, l in enumerate(SPEC, 1) if l.startswith('# II · THE CHANNELS'))
sec2_hi = next(i for i, l in enumerate(SPEC, 1) if i > sec2_lo and l.startswith('# III'))
ROWS = []
for i in range(sec2_lo, sec2_hi):
    l = SPEC[i - 1]
    if not l.lstrip().startswith('|'):
        continue
    f = [c.strip() for c in l.strip().strip('|').split('|')]
    if len(f) != 11 or f[0] == 'species' or set(f[0]) <= set('-: '):
        continue
    ROWS.append({'ln': i, 'raw': f[0], 'species': strip_marks(f[0]), 'series': f[1], 'n': f[2],
                 'levels': f[3], 'interior': f[4], 'bracket': f[5], 'nstar': f[6],
                 'd': f[7], 'sd': f[8], 'fits': f[9], 'limit': f[10]})

def ival(s):
    s = s.replace(',', '').strip()
    return int(s) if re.match(r'^-?\d+$', s) else None

def fval(s):
    s = s.replace('−', '-').replace('+', '').replace(',', '').strip()
    try:
        return float(s)
    except ValueError:
        return None

def dplaces(s):
    s = s.replace('−', '-').replace('+', '').strip()
    if 'e' in s.lower():
        return None
    return len(s.split('.')[1]) if '.' in s else 0

by_sp = {}
for r in ROWS:
    by_sp.setdefault(r['species'], []).append(r)
interior_all = sum(ival(r['interior']) or 0 for r in ROWS)
totline = [l for l in SPEC[sec2_lo:sec2_hi] if 'channel rows across' in l]
print('\n-- the channel table, and the compendium\'s own totals line --')
print(f'   Section II L{sec2_lo}-L{sec2_hi}; parsed {len(ROWS)} rows, {interior_all:,} interior cells, {len(by_sp)} species')
print(f'   compendium states: {totline[0].strip() if totline else "NO TOTALS LINE FOUND"}')
verdict('24-P0', len(ROWS) == 596 and interior_all == 2269,
        f'parse reproduces the compendium\'s own totals line ({len(ROWS)} rows, {interior_all} interior)')

# ---------------------------------------------------------------- C1 the bracket, swept over bases
def bracket_sum(rows):
    p = t = frows = 0
    for r in rows:
        m = re.match(r'^(\d+)\s*/\s*(\d+)$', r['bracket'])
        if not m:
            continue
        a, b = int(m.group(1)), int(m.group(2))
        p += a; t += b; frows += (a < b)
    return p, t, frows

def dedupe(rows):
    seen, out = set(), []
    for r in rows:
        k = (r['species'], re.sub(r'[^a-zA-Z0-9/=]', '', r['series']).lower(), r['n'].replace('†', ''), r['levels'])
        if k in seen:
            continue
        seen.add(k); out.append(r)
    return out

bases = [('every row carrying m/k', ROWS),
         ('m/k rows, duplicates removed', dedupe(ROWS)),
         ('m/k rows, two-member (*) species excluded', [r for r in ROWS if '*' not in r['raw']]),
         ('m/k rows, neutral species only (fits = 1)', [r for r in ROWS if ival(r['fits']) == 1]),
         ('m/k rows, undivided channels only (no J= in series)', [r for r in ROWS if 'J=' not in r['series']])]
print('\n-- C1  the bracket (L6626 "546 of 789 interior cells — 69.2%", "243 cells across 62 channels") --')
hit = False
for name, rs in bases:
    p, t, fr = bracket_sum(rs)
    pc = q(Fraction(p, t) * 100, 1) if t else Decimal(0)
    print(f'   {name:48s} {p:>5,}/{t:<5,}  {t - p:>4,} fail over {fr:>3} channels  {pc}%')
    hit = hit or (p, t) == (546, 789)
verdict('24-C1a', hit, 'L6626\'s 546/789 reproduces under one of the five bases swept above')
p, t, fr = bracket_sum(ROWS)
verdict('24-C1b', t - p == 243, f'L6626 "fails on 243 cells" vs {t - p} on the compendium\'s full basis')
verdict('24-C1c', fr == 62, f'L6626 "across 62 channels" vs {fr} channels carrying a failure')
verdict('24-C1d', str(q(Fraction(p, t) * 100, 1)) == '69.2', f'L6626 "69.2%" vs {p}/{t} = {q(Fraction(p, t) * 100, 1)}%')
verdict('24-C1e', p + (t - p) == t and t == 789, f'L6626 internal: 546 + 243 = 789 holds arithmetically; the table\'s own denominator is {t}')

# ---------------------------------------------------------------- C2 four numbers for one collection
print('\n-- C2  L6632, the four numbers for one collection --')
print(f'   printed: earlier version 1,442 / Appendix B totals line 1,105 / Appendix B table 869 / present tested 930')
print(f'   measured on the Spectra Compendium: interior sum {interior_all:,}; bracket denominator {t:,}; rows {len(ROWS)}')
for label, val in (('1,442', 1442), ('1,105', 1105), ('869', 869), ('930', 930), ('789', 789)):
    verdict('24-C2', val in (interior_all, t, len(ROWS)),
            f'{label:5s} equals the compendium\'s interior sum, bracket denominator or row count')

# ---------------------------------------------------------------- C3 §24.2 contributors
print('\n-- C3  §24.2 the largest contributors, against the species\' own rows --')
printed = [('He I', 9, 189), ('Ne I', 16, 131), ('K I', 4, 105), ('Al I', 4, 94),
           ('Na I', 6, 80), ('Ga I', 5, 61), ('Li I', 3, 55)]
for sp_, ch, ce in printed:
    rs = by_sp.get(sp_, [])
    und = [r for r in rs if 'J=' not in r['series']]
    a = (len(rs), sum(ival(r['interior']) or 0 for r in rs))
    b = (len(und), sum(ival(r['interior']) or 0 for r in und))
    verdict('24-C3', (ch, ce) in (a, b),
            f'{sp_:5s} printed {ch:2d}/{ce:3d}   all rows {a[0]:2d}/{a[1]:3d}   undivided only {b[0]:2d}/{b[1]:3d}')
tgt = {}
for s, rs in by_sp.items():
    tgt.setdefault(sum(ival(r['interior']) or 0 for r in rs), []).append(s)
for v in (131, 105):
    print(f'   sweep: species whose interior sum is exactly {v}: {tgt.get(v, [])}')
nelim = sorted({r['limit'] for r in by_sp.get('Ne I', [])})
verdict('24-C3n', len(nelim) == 2, f'L6656 "Ne I … two limits" vs {len(nelim)} distinct limits on Ne I rows: {nelim}')

# ---------------------------------------------------------------- C4 §24.1 spans
LMAP = {'s': 0, 'p': 1, 'd': 2, 'f': 3, 'g': 4, 'h': 5, 'i': 6, 'k': 7}
def ell(series):
    cfg = series.split()[0] if series.split() else series
    m = re.search(r'n([spdfghik])', cfg)
    return LMAP[m.group(1)] if m else None
ells = sorted({e for r in ROWS if (e := ell(r['series'])) is not None})
ZT = {'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10,
      'Na': 11, 'Mg': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19,
      'Ca': 20, 'Sc': 21, 'Ti': 22, 'Fe': 26, 'Zn': 30, 'Ga': 31, 'Ge': 32, 'Cd': 48,
      'Ba': 56, 'Hg': 80, 'Bi': 83}
ROM = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10}
zs, stages, unk = {}, set(), set()
for s in by_sp:
    el = s.split()[0]
    zs[s] = ZT[el] if el in ZT else unk.add(s)
    m = re.match(r'^\S+\s+([IVX]+)$', s)
    if m and m.group(1) in ROM:
        stages.add(ROM[m.group(1)])
zs = {k: v for k, v in zs.items() if v}
print('\n-- C4  §24.1 what it spans --')
print(f'   ℓ present {ells}; Z {min(zs.values())}-{max(zs.values())} ({min(zs, key=zs.get)} to {max(zs, key=zs.get)}); unmapped species {sorted(unk)}')
print(f'   ionisation stages present {sorted(stages)}; "fits" column values {sorted({ival(r["fits"]) for r in ROWS if ival(r["fits"]) is not None})}')
verdict('24-C4a', ells == [0, 1, 2, 3, 4, 5, 6], f'L6636 "ℓ 0 through 6" vs measured {ells}')
verdict('24-C4b', min(zs.values()) == 1, f'L6637 "Z 1 through 83" — lower end: measured minimum Z is {min(zs.values())} ({min(zs, key=zs.get)})')
verdict('24-C4c', max(zs.values()) == 83, f'L6637 "Z 1 through 83" — upper end: measured maximum Z is {max(zs.values())} ({max(zs, key=zs.get)})')
verdict('24-C4d', sorted(stages) == [1, 2, 3], f'L6638 "Z_eff 1 through 3" vs stages present {sorted(stages)}')
# hydrogen swept across all six volumes before any negative is recorded
hsites = {k: sum(1 for l in L if re.search(r'(?<![A-Za-z])H\s+I(?![IVX])', l)) for k, L in V.items()}
hrows = [r for r in ROWS if r['species'] == 'H I']
print(f'   sweep for hydrogen: "H I" occurrences per volume {hsites}; H I channel rows {len(hrows)}')
verdict('24-C4e', len(hrows) > 0, f'§24.7 "one row of the collection" — H I rows in the channel table: {len(hrows)}')

cores = MAIN[6643]
items = [c.strip() for c in cores.split('·')]
items[0] = items[0].split('**')[-1].strip()
declined = [c for c in items if 'declined' in c]
print(f'   L6644 cores list: {len(items)} items, declined {declined}')
verdict('24-C4f', len(items) == 23, f'L6639 "core types 23" vs {len(items)} items listed at L6644')
verdict('24-C4g', not declined, f'L6639 "all characterised" vs {len(declined)} item marked declined')

# ---------------------------------------------------------------- C5 the table's own invariant
print('\n-- C5  the compendium\'s interior rule, tested on all 596 rows --')
exc = [r for r in ROWS if ival(r['levels']) is not None and ival(r['interior']) is not None
       and ival(r['interior']) != ival(r['levels']) - 2]
print(f'   rows where interior != levels - 2: {len(exc)}')
for r in exc[:6]:
    print(f'      L{r["ln"]} {r["species"]:8s} {r["series"]:26s} levels {r["levels"]} interior {r["interior"]}')
verdict('24-C5a', not exc, f'interior = levels - 2 on every row ({len(exc)} exceptions, all two-member channels: '
        f'{sorted({r["levels"] for r in exc})})')
dups = {}
for r in ROWS:
    k = (r['species'], r['n'].replace('†', ''), r['levels'], r['interior'])
    dups.setdefault(k, []).append(r)
dd = {k: v for k, v in dups.items() if len(v) > 1 and len({re.sub(r'[^a-zA-Z0-9]', '', x['series']).lower() for x in v}) > 1}
print(f'   candidate duplicate channels (same species, n, levels, interior; differing series notation): {len(dd)}')
for k, v in list(dd.items())[:4]:
    print(f'      {k[0]:8s} n {k[1]:8s} -> ' + ' | '.join(f'L{x["ln"]} {x["series"]} δ {x["d"]} br {x["bracket"]}' for x in v))
verdict('24-C5b', not dd, f'no species carries the same channel twice under two notations ({len(dd)} found)')

# ---------------------------------------------------------------- C6 He I
print('\n-- C6  §24.3 He I --')
he1 = by_sp.get('He I', [])
he1_l = sorted({ell(r['series']) for r in he1})
nmax = max((int(re.findall(r'\d+', r['n'])[-1]) for r in he1 if re.findall(r'\d+', r['n'])), default=0)
for r in he1:
    print(f'      L{r["ln"]} {r["series"]:20s} ℓ={ell(r["series"])} n {r["n"]:7s} levels {r["levels"]:>3s} interior {r["interior"]:>3s} δ {r["d"]:>9s}')
verdict('24-C6a', len(he1) == 9, f'L6669 "Nine channels" vs {len(he1)} He I rows')
verdict('24-C6b', he1_l == [0, 1, 2, 3, 4, 5, 6], f'L6669 "ℓ = 0 through 6" vs He I ℓ values {he1_l}')
verdict('24-C6c', nmax == 35, f'L6669 "n to 35" vs measured maximum n {nmax}')
seq = ['0.2965', '0.1392', '-0.0133', '0.0014', '-0.0010', '-0.0014', '-0.0016']
lbl = ['s³', 's¹', 'p', 'd', 'f', 'g', 'i']
print(f'   L6671 prints {len(seq)} means for {len(he1)} channels, labelled {lbl}')
allm = True
for v, lb in zip(seq, lbl):
    dv = Decimal(v)
    m = [r for r in he1 if fval(r['d']) is not None and dplaces(r['d']) is not None
         and q(Decimal(r['d'].replace('−', '-').replace('+', '')), 4) == dv]
    allm = allm and bool(m)
    print(f'      {lb:2s} {v:>8s} -> {[(x["series"], x["d"]) for x in m] or "NO He I ROW AT 4 dp"}')
verdict('24-C6d', allm, 'each printed He I mean equals a compendium δ at four places')
fs = [float(x) for x in seq]
rises = [(lbl[i], fs[i], fs[i + 1]) for i in range(len(fs) - 1) if fs[i + 1] > fs[i]]
arise = [(lbl[i], fs[i], fs[i + 1]) for i in range(len(fs) - 1) if abs(fs[i + 1]) > abs(fs[i])]
verdict('24-C6e', not rises, f'L6669 "the defect falls monotonically with ℓ": signed rises {rises}')
verdict('24-C6f', not arise, f'  same claim in magnitude: |δ| rises at {arise}')
verdict('24-C6g', len(seq) == len(he1), f'L6671 lists {len(seq)} means where §24.3 claims {len(he1)} channels')
ni = [r for r in he1 if ell(r['series']) == 6]
ns = [r for r in he1 if ell(r['series']) == 0]
verdict('24-C6h', ni and all(ival(r['levels']) == 20 for r in ni), f'L6672 "twenty members for ni" vs {[(r["series"], r["levels"]) for r in ni]}')
verdict('24-C6i', len(ns) == 2 and all(ival(r['levels']) == 23 for r in ns), f'L6672 "twenty-three for the two ns channels" vs {[(r["series"], r["levels"]) for r in ns]}')

# ---------------------------------------------------------------- C7 He II
print('\n-- C7  §24.4 He II --')
he2 = by_sp.get('He II', [])
for r in he2:
    print(f'      L{r["ln"]} {r["series"]:8s} ℓ={ell(r["series"])} levels {r["levels"]:>3s} interior {r["interior"]:>3s} δ {r["d"]:>10s} limit {r["limit"]}')
pr = [7.62, 5.09, 2.50, 1.41, 0.856, 0.446, 0.159]
ok7 = []
for v in pr:
    m = [r for r in he2 if fval(r['d']) is not None and dplaces(r['d']) is None
         and float(f'{v * 1e-5:.2g}') == fval(r['d'])]
    ok7.append(bool(m))
    print(f'      printed {v}e-5 -> {[(x["series"], x["d"]) for x in m] or "NO He II ROW AT THE COMPENDIUM\'S 2 s.f."}')
verdict('24-C7a', all(ok7), 'each of the seven printed He II values equals a compendium δ at the compendium\'s precision')
verdict('24-C7b', all(pr[i] > pr[i + 1] for i in range(len(pr) - 1)), 'the seven printed values are monotone decreasing')
orders = q(math.log10(max(pr) / min(pr)), 2)
verdict('24-C7c', 5.5 <= float(orders) <= 6.5,
        f'L6690 "monotone across six orders of magnitude" vs the printed values spanning ×{q(max(pr) / min(pr), 1)} = {orders} orders')
verdict('24-C7d', len(pr) == len(he2), f'L6690 lists {len(pr)} values against {len(he2)} He II rows')
ng = [r for r in he2 if ell(r['series']) == 4]
verdict('24-C7e', ng and all(ival(r['levels']) == 6 for r in ng), f'L6697 "six members" for ng vs {[(r["series"], r["levels"]) for r in ng]}')
lims = sorted({r['limit'] for r in he2})
verdict('24-C7f', any('438,908.885' in x for x in lims), f'L6697 tabulated 438,908.885 among He II limits {lims}')
tab, got = Decimal('438908.885'), Decimal('438908.871')
verdict('24-C7g', str(q(tab - got, 3)) == '0.014', f'L6697 "agreement to 0.014 cm⁻¹" vs {tab} - {got} = {q(tab - got, 3)}')
parts = q((tab - got) / tab * Decimal(10) ** 8, 2)
verdict('24-C7h', 2.5 <= float(parts) <= 3.5, f'L6697 "three parts in 10⁸" vs {parts} parts in 10⁸')

# ---------------------------------------------------------------- C8 the collection span
ds = [(r, fval(r['d'])) for r in ROWS if fval(r['d']) is not None]
mx = max(ds, key=lambda z: abs(z[1])); mn = min((z for z in ds if z[1] != 0), key=lambda z: abs(z[1]))
oa = q(math.log10(abs(mx[1]) / abs(mn[1])), 2)
print('\n-- C8  Figure 24.1 caption, the collection\'s span --')
print(f'   largest |δ| {mx[1]} ({mx[0]["species"]} {mx[0]["series"]}); smallest non-zero |δ| {mn[1]} ({mn[0]["species"]} {mn[0]["series"]})')
verdict('24-C8a', 5.5 <= float(oa) <= 6.5, f'L6649 "spans six orders of magnitude" vs measured {oa} orders')
verdict('24-C8b', mx[0]['species'].startswith('Bi') and abs(abs(mx[1]) - 4.9) < 0.05, f'L6649 "from 4.9 in bismuth" vs {mx[1]} in {mx[0]["species"]}')
verdict('24-C8c', mn[0]['species'] == 'He II' and abs(abs(mn[1]) - 1.6e-6) < 5e-8, f'L6649 "to 1.6 × 10⁻⁶ in He II" vs {mn[1]} in {mn[0]["species"]}')

# ---------------------------------------------------------------- C9 Bi I and the dilution rule
print('\n-- C9  §24.5 Bi I, and the dilution rule --')
bi = by_sp.get('Bi I', [])
for r in bi:
    print(f'      L{r["ln"]} {r["series"]:24s} n {r["n"]:6s} levels {r["levels"]:>3s} interior {r["interior"]:>3s} δ {r["d"]}')
bins_ = [r for r in bi if ell(r['series']) == 0]
verdict('24-C9a', any(str(q(Decimal(r['d'].replace('+', '')), 2)) == '4.90' for r in bins_),
        f'L6701 "δ̄ = 4.90 for the ns channel" vs {[r["d"] for r in bins_]} (HALF_UP to 2 dp)')
verdict('24-C9b', any(ival(r['levels']) == 5 for r in bins_), f'L6701 "over five members" vs levels {[r["levels"] for r in bins_]}')
verdict('24-C9c', mx[0]['species'] == 'Bi I', f'L6702 "the largest defect in this work" vs the table maximum, in {mx[0]["species"]}')
nb = max((int(re.findall(r'\d+', r['n'])[-1]) for r in bi if re.findall(r'\d+', r['n'])), default=0)
verdict('24-C9d', nb == 11, f'L6704 "its ³P₀ parent reaches n = 11" vs Bi I maximum n {nb}')
for s in ('Ne II', 'Ar II', 'Bi I'):
    rs = by_sp.get(s, [])
    br = [r for r in rs if re.match(r'^\d+/\d+$', r['bracket'])]
    shells = sorted({(int(re.findall(r'\d+', r['n'])[-1]) - int(re.findall(r'\d+', r['n'])[0]) + 1)
                     for r in rs if len(re.findall(r'\d+', r['n'])) >= 2})
    print(f'   {s:6s} rows {len(rs):3d}  bracket-tested rows {len(br):3d}  interior {sum(ival(r["interior"]) or 0 for r in rs):3d}  n-span per row {shells}')
verdict('24-C9e', not by_sp.get('Ne II'), f'L6704/L6708 "made neon II fail entirely" vs {len(by_sp.get("Ne II", []))} Ne II channel rows carrying {sum(ival(r["interior"]) or 0 for r in by_sp.get("Ne II", []))} interior cells')
verdict('24-C9f', all(not re.match(r'^\d+/\d+$', r['bracket']) for r in by_sp.get('Ne II', [])),
        'the weaker reading — Ne II carries no bracket-tested channel')

# ---------------------------------------------------------------- C10 the paired progressions
print('\n-- C10  §24.6 the isoelectronic pairs --')
pairs = [('He I', 'Li II'), ('Li I', 'Be II'), ('Na I', 'Mg II'), ('Al I', 'Si II'), ('K I', 'Ca II')]
missing = [s for p_ in pairs for s in p_ if s not in by_sp]
verdict('24-C10a', not missing, f'all ten paired species carry channel rows; missing {missing}')
for s, seq2 in (('Li II', ['0.182', '0.054', '0.002', '0.0002']), ('Be II', ['0.262', '0.049', '0.002', '0.0001'])):
    rs = by_sp.get(s, [])
    got, lev = [], []
    for j, v in enumerate(seq2):
        dv = Decimal(v); pl = dplaces(v)
        cand = [r for r in rs if ell(r['series']) == j and fval(r['d']) is not None]
        m = [r for r in cand if q(Decimal(r['d'].replace('−', '-').replace('+', '')), pl) == dv]
        got.append(bool(m)); lev += [ival(r['levels']) for r in cand if ival(r['levels'])]
        print(f'      {s} ℓ={j} printed {v:>8s} -> {[(x["series"], x["d"]) for x in m] or [(x["series"], x["d"]) for x in cand]}')
    verdict('24-C10', all(got), f'{s} printed s→f {seq2} each equal a row δ at the printed precision: {got}')
    verdict('24-C10m', lev and min(lev) >= 5 and max(lev) <= 10, f'L6720 "a channel mean over five to ten members" vs {s} levels {sorted(set(lev))}')
for s in ('Li II', 'Be II'):
    h5 = [r for r in by_sp.get(s, []) if ell(r['series']) == 5]
    verdict('24-C10h', h5 and all(str(q(Decimal(r['d'].replace('−', '-').replace('+', '')), 4)) == '-0.0003' for r in h5)
            and all(ival(r['levels']) == 3 for r in h5),
            f'L6723 "{s} ℓ = 5 near −0.0003, three members" vs {[(r["series"], r["d"], "levels " + r["levels"], "interior " + r["interior"]) for r in h5]}')

# ---------------------------------------------------------------- C11 hydrogen
print('\n-- C11  §24.7 hydrogen --')
RH, RINF = Decimal('109678.7717'), Decimal('109737.3')
verdict('24-C11a', str(q(RINF - RH, 1)) == '58.5', f'L6733 "the 58.5 cm⁻¹ reduced-mass difference" vs {RINF} − {RH} = {q(RINF - RH, 4)}')
med = Decimal('0.006')
verdict('24-C11b', str(q(med * 54, 2)) == '0.34', f'L6735 "inflates the median error 54-fold to 0.34" vs 0.006 × 54 = {q(med * 54, 3)}')
print(f'   0.34 / 0.006 = {q(Decimal("0.34") / med, 1)}-fold; the printed 54-fold gives {q(med * 54, 3)}')
rel = q((RINF - RH) / RINF, 8)
verdict('24-C11c', float(rel) < 1e-4, f'L6737 "for every heavier species the correction is 10⁻⁵ relative" — the same ratio for hydrogen is {rel}')
rsites = {k: sum(1 for l in L if '109,737.3' in l or '109737.3' in l) for k, L in V.items()}
print(f'   sweep for R∞ 109,737.3 across the six volumes: {rsites}')
rh_sites = {k: sum(1 for l in L if '109,678.77' in l or '109678.77' in l) for k, L in V.items()}
print(f'   sweep for R_H 109,678.7717: {rh_sites}')

# ---------------------------------------------------------------- C12 §B.3
print('\n-- C12  §B.3 flagged channels, for the Figure 24.1 caption --')
b3lo = next(i for i, l in enumerate(SPEC, 1) if l.startswith('## B.3'))
b3hi = next(i for i, l in enumerate(SPEC, 1) if i > b3lo and l.startswith('# '))
blob = '\n'.join(SPEC[b3lo - 1:b3hi - 1])
for i in range(b3lo, b3hi):
    if SPEC[i - 1].strip():
        print(f'      L{i} {SPEC[i - 1][:160]}')
for name in ('Al I', 'Al II'):
    verdict('24-C12', has_token(blob, name.replace(' ', '')) or name in blob, f'L6650 "{name} … §B.3 flags as perturbed" — named in §B.3')

print('\n=== end r2-ch14r ===')
