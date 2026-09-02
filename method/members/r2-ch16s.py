#!/usr/bin/env python3
# r2-ch16s -- COMPUTABLE batch for the chat-124 section read: main L9307-L9392 (32.7).
# Reads MEMBERS only, never a BUILDnnn bundle path.  Deterministic; prints no wall-clock time.
import os, re, sys, importlib.util
from decimal import Decimal, ROUND_HALF_UP

H = '/home/claude/members'
spec = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
from r2lib import heading_line, section_span, has_token, enclosing, L8_at

def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
def hr(t): print('\n' + '=' * 96 + '\n' + t + '\n' + '=' * 96)
def norm(s): return re.sub(r'\s+', ' ', s.strip())

# owed to r2lib (DEFERRED): body_range, carried with provenance from r2-ch16m (chat 121).
def body_range(M, sec):
    s = heading_line(M, sec)
    if s is None: return None
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1].strip()): return (s, i)
    return (s, len(M) + 1)

# owed to r2lib (DEFERRED): numsites, comma-aware, from r2-ch16p (chat 122).
def numsites(M, n):
    forms = {str(n), f'{n:,}'}
    pat = r'(?<![\d.,])' + '(?:' + '|'.join(re.escape(f) for f in forms) + r')(?!\d)(?!,\d)(?!\.\d)'
    return [i + 1 for i in range(len(M)) if re.search(pat, M[i])]

def q(x, places='0.01'):
    """Decimal.quantize HALF_UP -- never Python's round(), which is binary and wrong on .5."""
    return Decimal(str(x)).quantize(Decimal(places), rounding=ROUND_HALF_UP)

MAIN = rd('The_Method_1_6-2.md')
REG  = rd('The_Method_1_6___The_Register-2.md')
MC   = rd('The_Method_1_6___Mathematical_Compendium-2.md')
PC   = rd('The_Method_1_6___The_Physics_Compendium-2.md')
IOI  = rd('The_Method_1_6___The_Index_of_Indices-2.md')
SC   = rd('The_Method_1_6___Spectra_Compendium-2.md')
VOLS = [('main', MAIN), ('reg', REG), ('mc', MC), ('pc', PC), ('ioi', IOI), ('sc', SC)]
A, B = 9307, 9393          # unit: [A, B)
U = MAIN[A - 1:B - 1]

# --------------------------------------------------------------------------- 1
hr('1  UNIT EXTENT -- body_range AND section_span, both resolvers, per standing method')
br, ss = body_range(MAIN, '32.7'), section_span(MAIN, '32.7')
print(f'  heading_line(32.7)   = {heading_line(MAIN, "32.7")}')
print(f'  body_range(32.7)     = {br}')
print(f'  section_span(32.7)   = {ss}')
print(f'  COINCIDE             = {br == ss}   (32.7 has no subsections -- expected True)')
print(f'  next heading         = L{B} {MAIN[B-1].strip()[:60]!r}')
print(f'  unit                 = L{A}-L{B-1}, {B-A} lines')
print(f'  member true lines    = {len(MAIN) - (1 if MAIN[-1] == "" else 0)}')

# --------------------------------------------------------------------------- 2
hr('2  COUNT WORDS AGAINST THEIR OWN DATA ROWS')
def table_rows(M, a, b):
    """DATA rows of a pipe table in [a,b): header and separator excluded (chat 123 fault 1)."""
    rows = [i for i in range(a, b) if M[i - 1].lstrip().startswith('|')]
    if not rows: return [], []
    sep = [i for i in rows if re.match(r'^\|[\s:|-]+\|?\s*$', M[i - 1].strip())]
    if not sep: return rows, []
    cut = sep[0]
    return rows, [i for i in rows if i > cut]
allr, data = table_rows(MAIN, A, B)
print(f'  32.7 table  L9320-L9326: {len(allr)} pipe lines, {len(data)} DATA rows -> {data}')
print(f'  L9318 count word: "Five worked cases"  -> five == {len(data)}: {len(data) == 5}')
# the four further contributions, L9352
bold = [i for i in range(9353, 9362) if MAIN[i - 1].lstrip().startswith('**')]
print(f'  L9352 "the other four things": bolded contribution lines {bold} -> four == {len(bold)}: {len(bold) == 4}')
for i in bold: print(f'      L{i} {norm(MAIN[i-1])[:88]}')
# 29.6, cited by the unit at L9356 as "four unreachable documents"
h296 = heading_line(MAIN, '29.6'); b296 = body_range(MAIN, '29.6')
allr6, data6 = table_rows(MAIN, b296[0], b296[1])
print(f'\n  29.6 heading L{h296}: {norm(MAIN[h296-1])!r}')
print(f'  29.6 body_range {b296}; table DATA rows = {len(data6)} -> {data6}')
print(f'  heading says THREE; table lists {len(data6)}  -- agree: {len(data6) == 3}')
for i in data6: print(f'      L{i} {norm(MAIN[i-1])[:96]}')

# --------------------------------------------------------------------------- 3
hr('3  THE SELF-DUALITY CASE -- L9322: "max+min-x gave 112, not 8; the right map is max-x"')
cells = L8_at((3, 3, 1, 3, 1))
S = set(cells)
print(f'  Lambda_8 cells = {len(cells)}   (gate core: 976)')
mx = [max(c[i] for c in cells) for i in range(8)]
mn = [min(c[i] for c in cells) for i in range(8)]
print(f'  per-coordinate max = {mx}')
print(f'  per-coordinate min = {mn}')
def mapA(c): return tuple(mx[i] - c[i] for i in range(8))            # x -> max - x
def mapB(c): return tuple(mx[i] + mn[i] - c[i] for i in range(8))    # x -> max + min - x
for nm, f in (('max-x      ', mapA), ('max+min-x  ', mapB)):
    img = [f(c) for c in cells]
    inside = sum(1 for y in img if y in S)
    outside = len(cells) - inside
    fixed = sum(1 for c in cells if f(c) == c)
    bij = len(set(img)) == len(cells)
    print(f'  {nm}: image-in-lattice {inside}  OUT {outside}  fixed points {fixed}  injective {bij}')
print(f'  identical maps (min all zero)? {mapA(cells[0]) == mapB(cells[0]) and all(m == 0 for m in mn)}')
print('  SITES of 112 and of 8 in the volume, and the words of the case:')
print(f'    112 -> {numsites(MAIN, 112)}')
for tok in ('self-dual', 'self-duality', 'involution', 'twenty-member'):
    hits = [i for i in range(1, len(MAIN) + 1) if re.search(tok, MAIN[i - 1], re.I)]
    print(f'    {tok:14s} -> {hits}')

# --------------------------------------------------------------------------- 4
hr('4  THE OTHER FOUR CASES OF THE TABLE, TRACED TO THE BOOK\'S OWN RECORD (L9318 universal)')
def sweep(pat, vols=VOLS, flags=0):
    out = {}
    for nm, M in vols:
        h = [i for i in range(1, len(M) + 1) if re.search(pat, M[i - 1], flags)]
        if h: out[nm] = h
    return out
for label, pat in (('-0.00128', r'0\.00128'), ('-0.00159', r'0\.00159'),
                   ('560/560', r'560\s*/\s*560'), ('"3 of 85"', r'\b3 of 85\b'),
                   ('22 of 60', r'\b22 of 60\b'), ('coerce/coerced', r'coerc'),
                   ('prefix loop', r'prefix'), ('proper projection', r'proper projection')):
    print(f'  {label:18s} {sweep(pat, flags=re.I)}')
print('\n  32.3 account (the two traced audit failures) vs 32.7 rows 1-2:')
for i in range(9045, 9053): print(f'   {i} {MAIN[i-1]}')

# --------------------------------------------------------------------------- 5
hr('5  THE 1,635 SITES AND THEIR REFERENT -- unit carries L9364, L9376, L9381')
word = 'one thousand six hundred and thirty-five'
wsites = [i for i in range(1, len(MAIN) + 1) if word in MAIN[i - 1]]
print(f'  word-form sites in main: {len(wsites)} -> {wsites}')
print(f'  of which inside the unit: {[i for i in wsites if A <= i < B]}')
for i in [i for i in wsites if A <= i < B]: print(f'      L{i} {norm(MAIN[i-1])[:110]}')
print(f'  digit-form 1,635 sites main: {numsites(MAIN, 1635)}')
# measured Register size, and how many entries are withdrawals
heads = [i for i in range(1, len(REG) + 1) if re.match(r'^#{1,4}\s*[\d,\s\u2013\u2014-]+\s*$', REG[i - 1].strip())]
nums = set()
for i in heads:
    s = REG[i - 1].strip().lstrip('#').strip()
    for part in re.split(r'[,\s]+', s):
        if re.fullmatch(r'\d+', part): nums.add(int(part))
        else:
            mm = re.fullmatch(r'(\d+)[\u2013\u2014-](\d+)', part)
            if mm: nums.update(range(int(mm.group(1)), int(mm.group(2)) + 1))
print(f'  Register: {len(heads)} bare-numeral headings, {len(nums)} distinct entry numbers, max {max(nums)}')
wd = [i for i in range(1, len(REG) + 1) if re.search(r'\bwithdraw(n|al|s)?\b', REG[i - 1], re.I)]
print(f'  Register lines carrying a withdraw* token: {len(wd)}')
print(f'  L9376 calls it a "register of {word} withdrawn claims"; 1,635 == distinct entries {len(nums)}: {len(nums) == 1635}')

# --------------------------------------------------------------------------- 6
hr('6  E = 36, AND THE NUMERALS THE UNIT PRINTS (SITES, comma-aware, both forms)')
print(f'  "E = 36" sites: {sweep(r"E\s*=\s*36")}')
print(f'  "periodic table" sites in main: {[i for i in range(1, len(MAIN)+1) if re.search("periodic table", MAIN[i-1], re.I)][:14]}')
for n in (4000, 1061, 102, 30, 39, 85, 60, 560, 36):
    s = numsites(MAIN, n)
    print(f'  {n:>6,} -> {len(s)} sites; in unit {[i for i in s if A <= i < B]}')
print(f'  "4,000 triples" sweep: {sweep(r"4,?000 triples", flags=re.I)}')
print(f'  "4nu/3" (4ν/3) sites main: {len([i for i in range(1,len(MAIN)+1) if "4ν/3" in MAIN[i-1]])}')

# --------------------------------------------------------------------------- 7
hr('7  THE FALSIFICATION RUN -- "three conditions ... reports the two that failed ... repaired both"')
b326 = body_range(MAIN, '32.6'); s326 = section_span(MAIN, '32.6')
print(f'  32.6 body_range {b326}  section_span {s326}  COINCIDE {b326 == s326}')
lo, hi = s326
for i in range(lo, hi):
    t = MAIN[i - 1]
    if re.search(r'\b(condition|fail|pass|repair)\w*\b', t, re.I) and t.strip():
        print(f'   {i} {norm(t)[:120]}')

# --------------------------------------------------------------------------- 8
hr('8  THE DATES AND THE EXTERNAL FACTS L9342 STATES')
for label, pat in (('Birkhoff', r'Birkhoff'), ('Dilworth', r'Dilworth'), ('Sperner', r'Sperner'),
                   ('1937', r'\b1937\b'), ('1950', r'\b1950\b'), ('1928', r'\b1928\b'),
                   ('1920s', r'\b1920s\b'), ('2004', r'\b2004\b'), ('1922', r'\b1922\b'),
                   ('Stahl & Wille', r'Stahl')):
    r = sweep(pat)
    print(f'  {label:14s} {({k: (v[:8] + ["..."] if len(v) > 8 else v) for k, v in r.items()})}')
print('\n  L9342 five-failed-attempts / reorderability survey, and the 2004 site texts:')
for nm, M in VOLS:
    for i in [i for i in range(1, len(M) + 1) if re.search(r'\b2004\b', M[i - 1])][:4]:
        print(f'   {nm} L{i} {norm(M[i-1])[:118]}')

# --------------------------------------------------------------------------- 9
hr('9  THE INEQUALITY AT L9354 AGAINST ITS OTHER SITES AND AGAINST RULE 4')
print(f'   9354 {norm(MAIN[9353])}')
for i in [i for i in range(1, len(MAIN) + 1) if re.search(r'2\s*\*?Z', MAIN[i - 1]) and re.search(r'ν', MAIN[i - 1])][:12]:
    print(f'   {i} {norm(MAIN[i-1])[:130]}')
print('   Rule 4 (L6047) and 22.5 (L6168):')
for i in (6047, 6168): print(f'   {i} {norm(MAIN[i-1])[:130]}')

# --------------------------------------------------------------------------- 10
hr('10  THE COLLABORATOR PAGE (L9380-L9382): does it name a single pattern and four results?')
print(f'   L7469 {norm(MAIN[7468])[:120]}')
for i in (17, 18, 42, 9851): print(f'   L{i} {norm(MAIN[i-1])[:120]}')
print(f'   "refus" sites near the collaborator note: {[i for i in range(1, 120) if re.search("refus", MAIN[i-1], re.I)]}')
print('\nEND r2-ch16s')
