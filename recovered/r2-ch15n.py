#!/usr/bin/env python3
"""r2-ch15n — computable batch for the chat-110 section read, main L7721-L7855
(§28.8, §28.9, §28.9.1).  Chat-81 cadence: one computable batch, one prose batch.

Resolvers imported from r2lib by path (heading_line, section_span, has_token, enclosing).
body_range and the digit-bounded numeral sweep are carried here verbatim with provenance
comments until they are lifted into r2lib (DEFERRED owes both).
"""
import importlib.util, os, re, sys
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

H = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
heading_line, section_span = r2lib.heading_line, r2lib.section_span

VOLS = {
    'main':    'The_Method_1_6-2.md',
    'reg':     'The_Method_1_6___The_Register-2.md',
    'mc':      'The_Method_1_6___Mathematical_Compendium-2.md',
    'pc':      'The_Method_1_6___The_Physics_Compendium-2.md',
    'ioi':     'The_Method_1_6___The_Index_of_Indices-2.md',
    'spectra': 'The_Method_1_6___Spectra_Compendium-2.md',
}
V = {k: open(os.path.join(H, f), encoding='utf-8').read().split('\n') for k, f in VOLS.items()}
M = V['main']
U0, U1 = 7721, 7855                      # the unit, MEASURED by heading scan in chat 110


# provenance: owed to r2lib since chat 105.  A section body runs from its heading to the NEXT
# heading of ANY rank -- section_span runs to the next non-child and so swallows subsections.
def body_range(lines, sec):
    s = heading_line(lines, sec)
    if s is None:
        return None
    for i in range(s + 1, len(lines) + 1):
        if re.match(r'^#{1,4} (\d+(?:\.\d+)*)\.? ', lines[i - 1].strip()):
            return (s, i)
    return (s, len(lines) + 1)


# provenance: owed to r2lib since chat 108.  has_token is LETTER-bounded and so reads 129 out
# of 1129; a numeral sweep must be DIGIT-bounded, and must tolerate the thousands comma.
def numeral_sites(lines, n):
    pat = re.compile(r'(?<![\d,.])' + f'{n:,}'.replace(',', '[,]?') + r'(?![\d,.])')
    return [i for i, t in enumerate(lines, 1) if pat.search(t)]


def q(x, places='0.1'):
    d = Decimal(x)
    return (d.quantize(Decimal(places), rounding=ROUND_HALF_UP),
            d.quantize(Decimal(places), rounding=ROUND_HALF_EVEN))


def head(t):
    print('\n' + t); print('-' * len(t))


print('r2-ch15n  computable batch  main L%d-L%d' % (U0, U1))
print('unit lines %d ; volumes %s' % (U1 - U0 + 1, ' '.join(VOLS)))

# ---------------------------------------------------------------- C1  Appendix D partition
head('C1  the mathematics register: 152 objects = 47 unfinished + 105 settled  (L7779)')
print('  47 + 105 = %d   vs printed 152   %s' % (47 + 105, 'EXACT' if 47 + 105 == 152 else 'FAILS'))

head('C2  the 47 unfinished, itemised  (L7782-L7784)')
parts = {'cited-and-unverified': 20, 'computed-and-unchecked': 19, 'unnamed roots': 6,
         'asserted': 1, 'open': 1}
s = sum(parts.values())
print('  ' + ' + '.join(str(v) for v in parts.values()) + ' = %d   vs 47   %s'
      % (s, 'EXACT' if s == 47 else 'FAILS'))
print('  39 of 47 unreproduced: 39 <= 47 %s ; leaves %d reproduced' % (39 <= 47, 47 - 39))

# ---------------------------------------------------------------- C3  the density column
head('C3  density 68.8% for 33 cells in a box of 48  (L7791-L7794, L7824)')
hu, he = q(Decimal(33) / Decimal(48) * 100)
print('  33/48 = %s  ->  HALF_UP %s%%  HALF_EVEN %s%%   printed 68.8   %s'
      % (Decimal(33) / Decimal(48), hu, he, 'EXACT both conventions' if str(hu) == str(he) == '68.8' else 'CHECK'))
print('  the column is cells/box, not entries/box: identical for all three rows by construction')

head('C4  the coordinate box, counted from the printed value lists  (L7818-L7820)')
coord = {}
for ln in range(7817, 7822):
    t = M[ln - 1]
    m = re.match(r'\s+(\S+)\s{2,}(.+)$', t)
    if m and m.group(1) in ('corroboration', 'caught', 'repair'):
        vals = [x.strip() for x in m.group(2).split('<')]
        coord[m.group(1)] = vals
        print('  L%d %-14s %d values: %s' % (ln, m.group(1), len(vals), ' | '.join(vals)))
box = 1
for k in coord:
    box *= len(coord[k])
print('  product = %d   vs printed box of 48 (L7824)   %s'
      % (box, 'EXACT' if box == 48 else 'FAILS'))
print('  absent cells = 48 - 33 = %d ; admitted-and-absent E = 6 <= %d  %s'
      % (48 - 33, 48 - 33, 6 <= 48 - 33))

# ---------------------------------------------------------------- C5  the growth table
head('C5  the growth table 248 / 265 / 319 and "Seventy-one entries"  (L7791-L7796)')
g = [248, 265, 319]
print('  deltas: %d then %d ; total %d   printed "Seventy-one" = 71   %s'
      % (g[1] - g[0], g[2] - g[1], g[2] - g[0], 'EXACT' if g[2] - g[0] == 71 else 'FAILS'))
print('  "measured three times as it grew": %d rows printed' % len(g))

# ---------------------------------------------------------------- C6  the repair partition
head('C6  the repair partition against 319 entries  (L7803-L7804)')
rep = {'recorded, not repaired': 210, 'an instance fixed': 93, 'a class fixed': 10,
       'a protocol produced': 7}
tot = sum(rep.values())
for k, v in rep.items():
    print('  %-24s %3d' % (k, v))
print('  sum = %d   vs printed "Of 319 entries" = 319   %s (%+d)'
      % (tot, 'EXACT' if tot == 319 else 'DEVIATION', tot - 319))
print('  two rarest values are %s -- printed claim "the two rarest" %s'
      % (sorted(rep, key=rep.get)[:2],
         'HOLDS' if sorted(rep, key=rep.get)[:2] == ['a protocol produced', 'a class fixed'] else 'FAILS'))

head('C7  "67.5% recorded but not repaired"  (L7851) against every denominator in the section')
for d in (248, 265, 319, 320):
    hu, he = q(Decimal(210) / Decimal(d) * 100)
    print('  210/%-3d = %s%% (HALF_UP)   %s' % (d, hu, 'MATCHES 67.5' if str(hu) == '67.5' else ''))
for d in (248, 265, 319, 320):
    n = Decimal('0.675') * d
    print('  67.5%% of %-3d = %s  %s' % (d, n, '(integer)' if n == int(n) else ''))
print('  no denominator in the section carries 210 at 67.5%: DEVIATION, and it pairs with C6')

# ---------------------------------------------------------------- C8  the fibres
head('C8  the four-body fibres  (L7822, L7839-L7841)')
fib = {'LAW': (44, 11, 1), 'REFERENCE': (23, 11, 8), 'OBJECT': (80, None, 19)}
print('  layers named at L7822: object, law, procedure, reference  (4)')
for k, (e, c, E) in fib.items():
    print('  %-10s entries %3d  cells %s  E %2d' % (k, e, c if c else '--', E))
print('  entries printed = %d over 3 of 4 layers ; PROCEDURE never printed' % sum(f[0] for f in fib.values()))
print('  remainder against 248 = %d ; against 319 = %d  (both unprinted: docket 10)'
      % (248 - sum(f[0] for f in fib.values()), 319 - sum(f[0] for f in fib.values())))

# ---------------------------------------------------------------- C9  the six missing cells
head('C9  "The six cells the register admits and lacks", counted from the list  (L7843-L7848)')
txt = ' '.join(M[7842:7848])
tail = txt.split('does not:', 1)[1] if 'does not:' in txt else txt
items = [x.strip(' .*') for x in tail.split(';')]
for i, it in enumerate(items, 1):
    print('  %d. %s' % (i, re.sub(r'\s+', ' ', it)[:96]))
print('  items listed = %d   vs printed "six"   %s' % (len(items), 'EXACT' if len(items) == 6 else 'DEVIATION'))
print('  even reading item 1 as two (by an instrument / from outside) gives %d' % (len(items) + 1))

# ---------------------------------------------------------------- C10 the process index
head('C10  the process index: 36 cells, closed, E = 0  (L7736-L7742)')
print('  cells are (step, visible, alternatives, committed); one constraint visible <= committed')
print('  the ambient ranges are NOT printed -- reconstruction only, over 0..n boxes')
found = []
for a in range(1, 7):          # step values
    for b in range(1, 7):      # visible values
        for c in range(1, 7):  # alternatives values
            for d in range(1, 7):  # committed values
                n = a * c * sum(1 for x in range(b) for y in range(d) if x <= y)
                if n == 36:
                    found.append((a, b, c, d))
print('  boxes of size <=6 per coordinate giving exactly 36 closed cells: %d' % len(found))
for f in found[:8]:
    print('    step %d x visible %d x alternatives %d x committed %d' % f)
print('  the anchoring cell (step 2, visible 2, alternatives 3, committed 0):'
      ' visible <= committed is %s -> refused, as the section states' % (2 <= 0))
print('  E = 0 for a single monotone constraint on a product box is structurally forced (chat 88 class)')

# ---------------------------------------------------------------- C11 what the chapter prints
head('C11  "the withdrawals register (this chapter) 319 entries"  (L7780) against the chapter')
ch = section_span(M, '28')
print('  section_span("28") = %s' % (ch,))
nums = []
for i in range(ch[0], ch[1]):
    m = re.match(r'\s*(\d{1,3})[.)]\s', M[i - 1])
    if m:
        nums.append((int(m.group(1)), i))
vals = [n for n, _ in nums]
print('  numbered item lines in the chapter body: %d ; distinct numerals %d ; max %d'
      % (len(nums), len(set(vals)), max(vals) if vals else 0))
dup = sorted({n for n in vals if vals.count(n) > 1})
print('  duplicated numerals: %s' % (dup if dup else 'none'))
missing = [n for n in range(1, max(vals) + 1) if n not in set(vals)] if vals else []
print('  numerals below the maximum never printed: %d %s'
      % (len(missing), missing[:20]))
print('  printed distinct items %d vs printed claim 319 -> shortfall %d (docket 31)'
      % (len(set(vals)), 319 - len(set(vals))))

# ---------------------------------------------------------------- C12 the density superlative
head('C12  "the densest object in this book after the periodic table\'s 71.4%"  (L7824-L7825)')
pat = re.compile(r'(?<![\d.])(\d{1,3}(?:\.\d)?)\s?%')
hits = []
for k, L in V.items():
    for i, t in enumerate(L, 1):
        if re.search(r'densit|dense|densest', t, re.I):
            for m in pat.finditer(t):
                hits.append((k, i, float(m.group(1)), re.sub(r'\s+', ' ', t.strip())[:88]))
hits.sort(key=lambda h: -h[2])
print('  percentages on lines carrying "densit*/dense*" across six volumes: %d' % len(hits))
for h in hits[:12]:
    print('    %-7s L%-6d %5.1f%%  %s' % h)
over = [h for h in hits if h[2] > 68.8 and abs(h[2] - 71.4) > 0.05]
print('  above 68.8%% and not the periodic table\'s 71.4%%: %d %s'
      % (len(over), [(h[0], h[1], h[2]) for h in over[:6]]))
print('  71.4%% sites: %s' % [(h[0], h[1]) for h in hits if abs(h[2] - 71.4) < 0.05][:6])
print('  5/7 = %s%% -- the periodic-table figure quantizes from a ratio, not printed here' % q(Decimal(5) / Decimal(7) * 100)[0])

# ---------------------------------------------------------------- C13 figures restated elsewhere
head('C13  where the unit\'s own figures are restated in six volumes (digit-bounded)')
for n in (319, 248, 265, 152, 116, 210, 93, 36, 33, 48):
    row = []
    for k, L in V.items():
        s = numeral_sites(L, n)
        if s:
            row.append('%s:%s' % (k, ','.join('L%d' % x for x in s[:6]) + ('+' if len(s) > 6 else '')))
    print('  %-4d %s' % (n, ' ; '.join(row) if row else '(no site)'))
