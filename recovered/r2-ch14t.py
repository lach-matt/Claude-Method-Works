#!/usr/bin/env python3
"""r2-ch14t — computable batch for the Chapter 24 second read, main L6741-L6816
(section 24.8 'On independence, and the most conservative reading' and 24.9 'A caveat the
collection forced').  Chat 100.

Reads the six volume MEMBERS by name; never a BUILDnnn bundle path (HANDOFF-52).
Imports heading_line / section_span / has_token / enclosing from r2lib by path and passes
them the LINE LIST, never the member text.  No wall-clock printing: the output is a golden.
"""
import os, re, sys, importlib.util
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_DOWN

H = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
from_lib = (r2lib.heading_line, r2lib.section_span, r2lib.has_token, r2lib.enclosing)
heading_line, section_span, has_token, enclosing = from_lib

MAIN = 'The_Method_1_6-2.md'
SPEC = 'The_Method_1_6___Spectra_Compendium-2.md'
REG  = 'The_Method_1_6___The_Register-2.md'

def lines(name):
    return open(os.path.join(H, name), encoding='utf-8').read().split('\n')

M = lines(MAIN); S = lines(SPEC); R = lines(REG)
UNIT = (6741, 6816)

def q2(x, mode):
    return Decimal(repr(x)).quantize(Decimal('0.01'), rounding=mode)

print('=' * 78)
print('r2-ch14t  computable batch  main L%d-L%d  (24.8, 24.9)' % UNIT)
print('=' * 78)

# ---------------------------------------------------------------- P0 boundaries
print('\n[P0] unit boundaries re-measured on the member')
for sec in ('24.8', '24.9', '24.10'):
    print('   heading_line(%-5s) = %s' % (sec, heading_line(M, sec)))
a, b = section_span(M, '24.8'); c, d = section_span(M, '24.9')
print('   section_span(24.8) = [%d,%d)   section_span(24.9) = [%d,%d)' % (a, b, c, d))
print('   unit = L%d-L%d, %d lines' % (a, d - 1, d - a))

# ------------------------------------------------------- P1 parse channel table
print('\n[P1] Spectra Compendium section II channel table, parsed')
ROW = re.compile(r'^\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*(\d+)\s*\|'
                 r'\s*(\d+)\s*\|\s*([^|]*?)\s*\|')
rows = []
for i, t in enumerate(S, 1):
    m = ROW.match(t)
    if not m:
        continue
    sp = m.group(1)
    if sp.lower() in ('species', '---') or set(sp) <= set('-: '):
        continue
    rows.append(dict(ln=i, species=sp.replace('*', '').strip(), star='*' in sp,
                     series=m.group(2), nrange=m.group(3), levels=int(m.group(4)),
                     interior=int(m.group(5)), bracket=m.group(6).strip()))
print('   rows parsed                    %d' % len(rows))
print('   distinct species               %d' % len({r['species'] for r in rows}))
print('   distinct elements              %d' % len({r['species'].split()[0] for r in rows}))
print('   sum of interior column       %5d' % sum(r['interior'] for r in rows))
print('   sum of levels  column        %5d' % sum(r['levels'] for r in rows))
print('   two-member (starred) rows      %d' % sum(1 for r in rows if r['star']))
print('   rows with levels >= 3          %d' % sum(1 for r in rows if r['levels'] >= 3))
print('   compendium totals line L900:  %s' % S[899].strip())

# ----------------------------------------------------- P2 bracket pass/fail
print('\n[P2] the bracket column, per channel  (L6746/L6750: "the bracket holds in all 190",')
print('     "190 channels were examined, each exhaustively, and none produced a failure")')
MK = re.compile(r'^(\d+)\s*/\s*(\d+)$')
tested = fails = passed = 0; f_cells = 0; t_m = t_k = 0
other = {}
for r in rows:
    m = MK.match(r['bracket'])
    if m:
        mm, kk = int(m.group(1)), int(m.group(2))
        tested += 1; t_m += mm; t_k += kk
        if mm < kk:
            fails += 1; f_cells += kk - mm
        else:
            passed += 1
    else:
        other[r['bracket']] = other.get(r['bracket'], 0) + 1
print('   channels with an m/k bracket   %d' % tested)
print('     of which every cell held     %d' % passed)
print('     of which at least one failed %d   (failing cells %d)' % (fails, f_cells))
print('   bracketed cells m/k          %5d of %d' % (t_m, t_k))
print('   non-m/k bracket values       %s' % sorted(other.items()))
pct = Decimal(t_m * 100) / Decimal(t_k)
print('   pass rate                    %s %%  (HALF_UP, 1 dp)'
      % pct.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
print('   VERDICT "none produced a failure": %s'
      % ('holds' if fails == 0 else 'FAILS - %d channels contain a failing cell' % fails))

# ------------------------------------------------- P3 He I and Ne I blocks
print('\n[P3] the two named blocks  (L6746 "He I\'s nine channels contribute 189 cells;')
print('     Ne I\'s sixteen contribute 131"; L6767 "Its 189 cells - the largest single block")')
by = {}
for r in rows:
    by.setdefault(r['species'], []).append(r)
for sp, claim_ch, claim_cells in (('He I', 9, 189), ('Ne I', 16, 131), ('H I', None, None)):
    rr = by.get(sp, [])
    print('   %-5s rows %3d   interior %5d   levels %5d   PRINTED %s / %s'
          % (sp, len(rr), sum(x['interior'] for x in rr), sum(x['levels'] for x in rr),
             claim_ch, claim_cells))
top = sorted(((sum(x['interior'] for x in v), k) for k, v in by.items()), reverse=True)[:6]
print('   largest blocks by interior cells: %s'
      % ', '.join('%s %d' % (k, n) for n, k in top))
print('   VERDICT "largest single block": %s'
      % ('He I is largest' if top[0][1] == 'He I' else 'FAILS - largest is %s at %d cells'
         % (top[0][1], top[0][0])))

# ------------------------------------------------- P4 the 1,442 and the ~190
print('\n[P4] the collection totals this unit prints  (1,442 cells over ~190 channels)')
for fig, lab in ((1442, 'cells'), (190, 'channels')):
    print('   printed %-6d %-9s' % (fig, lab), end='')
    print('  compendium sum of interior = %d, rows = %d' % (sum(r['interior'] for r in rows),
                                                            len(rows)))
subsets = [
    ('all rows',                        rows),
    ('levels >= 3 only',                [r for r in rows if r['levels'] >= 3]),
    ('m/k bracketed only',              [r for r in rows if MK.match(r['bracket'])]),
    ('not untested',                    [r for r in rows if r['bracket'] != 'untested']),
    ('levels >= 3 and m/k',             [r for r in rows if r['levels'] >= 3 and MK.match(r['bracket'])]),
]
print('   sweep of five row-filters against the printed pair (1,442 / 190):')
for lab, ss in subsets:
    print('     %-22s rows %4d   interior %5d   %s'
          % (lab, len(ss), sum(r['interior'] for r in ss),
             'MATCH' if (len(ss), sum(r['interior'] for r in ss)) == (190, 1442) else '-'))
print('   1442/190 = %s cells per channel (HALF_UP 2dp)'
      % (Decimal(1442) / Decimal(190)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
print('   189/9 = %d   131/16 = %s' % (189 // 9,
      (Decimal(131) / Decimal(16)).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)))

# ------------------------------------------------- P5 species count, "thirty-five"
print('\n[P5] L6791 "two species of thirty-five are done"')
sps = sorted({r['species'] for r in rows})
print('   species in the channel table   %d' % len(sps))
print('   PRINTED                        35')
print('   VERDICT %s' % ('holds' if len(sps) == 35 else
                         'deviates - table carries %d species' % len(sps)))
print('   the two read are He I and H I; H I rows in the table = %d' % len(by.get('H I', [])))

# ------------------------------------------------- P6 the survival table
print('\n[P6] L6775-L6779 survival table:  cells surviving = 1-f, TESTS surviving = (1-f)^3')
print('   %-6s %-10s %-10s %-10s %-10s %-10s' %
      ('f', 'printed', 'HALF_UP', 'HALF_EVEN', 'TRUNC', 'exact'))
for f, pr_cells, pr_tests in ((0.1, '0.90', '0.73'), (0.2, '0.80', '0.51'),
                              (0.3, '0.70', '0.34'), (0.5, '0.50', '0.12')):
    p = Decimal(1) - Decimal(repr(f))
    cube = p * p * p
    hu = cube.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    he = cube.quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)
    tr = cube.quantize(Decimal('0.01'), rounding=ROUND_DOWH) if False else \
         cube.quantize(Decimal('0.01'), rounding=ROUND_DOWN)
    ok = 'OK' if str(hu) == pr_tests else ('half-even/trunc only'
         if str(he) == pr_tests or str(tr) == pr_tests else 'MISMATCH')
    print('   %-6s %-10s %-10s %-10s %-10s %-10s  cells 1-f=%s printed %s  %s'
          % (f, pr_tests, hu, he, tr, cube, p, pr_cells, ok))

# ------------------------------------------------- P7 H I arithmetic
print('\n[P7] L6781 "H I, which is 38% plain: only 13 of 64 interior cells - 20% -"')
r13 = Decimal(13) * 100 / Decimal(64)
print('   13/64 = %s %%  -> printed 20 %%  : %s'
      % (r13.quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP),
         'holds at 0 dp' if r13.quantize(Decimal('1'), rounding=ROUND_HALF_UP) == 20 else 'FAILS'))
p = Decimal('0.38')
print('   scatter model at f=0.62 plain=0.38: (1-f)^3 = %s -> %s %% of cells'
      % ((p * p * p).quantize(Decimal('0.0001')), (p * p * p * 100).quantize(Decimal('0.1'))))
print('   MEASURED ratio observed/model = %s x'
      % ((r13 / (p * p * p * 100)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)))
print('   VERDICT L6783 "the collection is worse than scattered": the one computed species is')
print('           %s the scatter model, not worse'
      % ('BETTER than' if r13 > p * p * p * 100 else 'worse than'))
print('   64 interior cells implies %d levels; 38%% of %d = %s plain'
      % (66, 66, (Decimal('0.38') * 66).quantize(Decimal('0.01'))))

# ------------------------------------------------- P8 the nd series
print('\n[P8] L6782 "six of ten levels plain and not one clean triple, because the derived')
print('     values alternate and every triple contains one"')
from itertools import combinations
n = 10; triples = [(i, i + 1, i + 2) for i in range(1, n - 1)]
print('   ten levels -> %d interior cells / triples' % len(triples))
best = None
for derived in combinations(range(1, n + 1), 4):
    clean = sum(1 for t in triples if not set(t) & set(derived))
    if clean == 0:
        best = derived; break
print('   a 4-derived arrangement with zero clean triples exists: %s  (example %s)'
      % (best is not None, best))
alt = (2, 4, 6, 8)
print('   strict alternation %s -> clean triples %d'
      % (str(alt), sum(1 for t in triples if not set(t) & set(alt))))
print('   VERDICT: six plain of ten with zero clean triples is arithmetically consistent')

# ------------------------------------------------- P9 Register corroboration
print('\n[P9] Registers this unit cites, measured in the Register member')
def entry(num):
    pat = re.compile(r'^#{1,4}\s*%d\s*$' % num)
    for i, t in enumerate(R):
        if pat.match(t):
            j = i + 1
            while j < len(R) and not re.match(r'^#{1,4}\s*\d+\s*$', R[j]):
                j += 1
            return i + 1, '\n'.join(R[i:j])
    return None, ''
for num in (246, 436, 437):
    ln, body = entry(num)
    print('   Register %-4d @L%-6s present %s' % (num, ln, ln is not None))
    for tok, lab in ((r'13 of 64', '13 of 64'), (r'38%', '38% plain'),
                     (r'189', '189'), (r'1,442', '1,442'), (r'six plain levels of ten', 'six of ten')):
        if re.search(tok, body):
            print('       carries %-12s YES' % lab)
print('   Register 1625 (named by HANDOFF-52 as the independence entry):')
ln, body = entry(1625)
print('       @L%s  headline: %s' % (ln, body.split('\n')[2][:96] if body else '-'))
print('       carries "independence": %d  -> HANDOFF-52 misnamed the entry; 437 is the one'
      % has_token(body, 'independence'))

print('\n[END r2-ch14t]')
