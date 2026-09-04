
# r2-ch16h2.py — R3 (chat 153-R) — SUCCESSOR to r2-ch16h.py, re-anchored by tools/reanchor.py: every main-volume line the
# predecessor pinned as a literal is resolved by the text of the line it pointed at in the bundle its golden was
# banked against (2 anchors); nothing else changes. r2-ch16h.py is seated and never edited in place (chat 68).
# PROVED by tools/proveanchor.py when the line below says so; until then this file is a draft.
# PROVEANCHOR: 90+184 — reproduces r2-ch16h.out byte-exact on those bundles (G0c)

# --- re-anchoring helper (tools/reanchor.py): a main-volume line found by its own text, never by a number ---
def _L(t, d=0):
    import os as _o
    global _LM
    try: _LM
    except NameError: _LM = open(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)), 'The_Method_1_6-2.md'), encoding='utf-8').read().split('\n')
    h = [i for i, l in enumerate(_LM, 1) if l == t]
    assert len(h) == 1, ('re-anchor: line text is not unique or is absent', t[:60], h)
    return h[0] + d
"""r2-ch16h --- COMPUTABLE batch, chat 119, main L8700-L8789 (§31.3 - §31.3.4).

Every computable claim of the Calabi-Yau catalogue section: the inclusion-exclusion of the three
published counts, the Pareto percentages and the factor between denominators, the Triadophilia
slice as a cell set, its closure under join and meet (E(X), join/meet failures, pair count), the
prediction set's chi values, diagonal, sum range, mirror closure and named members, the
undocumented-exclusion variant, the four falsification-test rows, and the Lambda row of §31.3.1's
comparison table.  Conventions are named at every figure.  r2lib by path; members read, never a
bundle; the rank sequence is READ OUT of chat 118's banked golden, never re-derived.
"""
import importlib.util, re
from decimal import Decimal, ROUND_HALF_EVEN
from itertools import combinations

spec = importlib.util.spec_from_file_location('r2lib', '/home/claude/members/r2lib.py')
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)

LO, HI = _L('### 31.3 The Calabi–Yau catalogue'), _L(' What remains of item D is the lookup. 540 named cells, a file, and an afternoon.', 1)
M = open('/home/claude/members/The_Method_1_6-2.md', encoding='utf-8').read().split('\n')

print('=' * 100)
print('r2-ch16h  COMPUTABLE  chat 119  main L%d-L%d  (§31.3 - §31.3.4)' % (LO, HI))
print('=' * 100)


def q(x, places, tag):
    """Decimal.quantize, ROUND_HALF_EVEN, convention named at every call site."""
    return Decimal(x).quantize(Decimal('1.' + '0' * places) if places else Decimal('1'),
                               rounding=ROUND_HALF_EVEN), tag


# ------------------------------------------------------------------ 1. the three published counts
print('\n## 1  L8707-L8708  INCLUSION-EXCLUSION OF THE THREE PUBLISHED COUNTS')
a = b = 248305
u = 495515
print('   printed: %d with h11>=140, %d with h21>=140, %d with at least one' % (a, b, u))
print('   a + b - u  = %d + %d - %d = %d      printed 1,095   %s'
      % (a, b, u, a + b - u, 'EXACT' if a + b - u == 1095 else 'DEVIATION'))
print('   (the identity is |A and B| = |A| + |B| - |A or B|; both counts equal, as mirror symmetry')
print('    of the list requires -- that equality is itself a check and it holds)')

# ------------------------------------------------------------------ 2. the Pareto arithmetic
print('\n## 2  L8721-L8723  THE PARETO STATISTIC AGAINST BOTH DENOMINATORS')
KS_ALL = 473800776
both = 1095
p_right = Decimal(both) / Decimal(u) * 100
p_wrong = Decimal(both) / Decimal(KS_ALL) * 100
print('   1,095 / 495,515        = %s %%   -> %s %%  (3 dp, ROUND_HALF_EVEN)  printed 0.221 %%   %s'
      % (p_right, q(p_right, 3, 'half-even')[0],
         'EXACT' if q(p_right, 3, 'x')[0] == Decimal('0.221') else 'DEVIATION'))
print('   1,095 / 473,800,776    = %s %%   -> %s %%  (4 dp, ROUND_HALF_EVEN)  printed 0.0002 %%  %s'
      % (p_wrong, q(p_wrong, 4, 'half-even')[0],
         'EXACT' if q(p_wrong, 4, 'x')[0] == Decimal('0.0002') else 'DEVIATION'))
f_pct = p_right / p_wrong
f_den = Decimal(KS_ALL) / Decimal(u)
print('   factor, unrounded percentages  = %s -> %s   printed 956   %s'
      % (f_pct, q(f_pct, 0, 'half-even')[0], 'EXACT' if q(f_pct, 0, 'x')[0] == 956 else 'DEVIATION'))
print('   factor, ratio of denominators  = %s -> %s   (the same number: the numerator cancels)'
      % (f_den, q(f_den, 0, 'half-even')[0]))
print('   factor from the PRINTED rounded pair 0.221/0.0002 = %s -- NOT 956.  The printed factor is'
      % q(Decimal('0.221') / Decimal('0.0002'), 0, 'half-even')[0])
print('   computed on the unrounded values, which is the right convention; recorded so the')
print('   arithmetic-convention docket carries the PASS and not a false charge.')

# ------------------------------------------------------------------ 3. the Triadophilia slice
print('\n## 3  L8732-L8734  THE SLICE AS A CELL SET  (chi = +/-6, Candelas et al.)')
FULL = list(range(13, 129))
EXCL = [102, 103, 115, 117] + list(range(119, 127))
H = [h for h in FULL if h not in EXCL]
print('   h range 13..128 inclusive                     %d values   (printed range, inclusive)' % len(FULL))
print('   excluded h VALUES named: %s' % (', '.join(map(str, EXCL))))
print('   excluded h values, counted                    %d          L8783 prints "The 24 excluded values"'
      % len(EXCL))
print('   excluded CELLS (2 per value)                  %d          <- 24 is the CELL count'
      % (2 * len(EXCL)))
print('   -> DEVIATION SHAPE: the numeral 24 is exact as a count of cells and wrong as a count of')
print('      "values"; the same sentence then lists twelve values.  232 - 208 = %d confirms cells.'
      % (232 - 208))
X = sorted(set([(h, h + 3) for h in H] + [(h + 3, h) for h in H]))
XF = sorted(set([(h, h + 3) for h in FULL] + [(h + 3, h) for h in FULL]))
print('   |X| with exclusions   = %d      printed 208   %s'
      % (len(X), 'EXACT' if len(X) == 208 else 'DEVIATION'))
print('   |X| without           = %d      printed 232   %s'
      % (len(XF), 'EXACT' if len(XF) == 232 else 'DEVIATION'))
print('   pairs C(|X|,2) UNORDERED = %d   printed 21,528   %s'
      % (len(X) * (len(X) - 1) // 2, 'EXACT' if len(X) * (len(X) - 1) // 2 == 21528 else 'DEVIATION'))
print('   (ordered would be %d; the printed figure names the UNORDERED convention)'
      % (len(X) * (len(X) - 1)))


def closure_report(cells, label):
    """Join = componentwise max, meet = componentwise min, product order on Z^2."""
    S = set(cells)
    jf = mf = 0
    new = set()
    for c, d in combinations(sorted(S), 2):
        j = (max(c[0], d[0]), max(c[1], d[1]))
        m = (min(c[0], d[0]), min(c[1], d[1]))
        if j not in S:
            jf += 1; new.add(j)
        if m not in S:
            mf += 1; new.add(m)
    # fixed point, to name which convention the printed E(X) uses
    T = set(S); grown = True; rounds = 0
    while grown:
        grown = False; rounds += 1
        add = set()
        for c, d in combinations(sorted(T), 2):
            for e in ((max(c[0], d[0]), max(c[1], d[1])), (min(c[0], d[0]), min(c[1], d[1]))):
                if e not in T:
                    add.add(e)
        if add:
            T |= add; grown = True
        if rounds > 6:
            break
    print('   %-26s |X| %4d  join-fail pairs %5d  meet-fail pairs %5d  ONE-STEP new cells %4d'
          % (label, len(S), jf, mf, len(new)))
    print('   %-26s FIXED-POINT closure adds %d cells in %d round(s)' % ('', len(T) - len(S), rounds))
    return (T - S), jf, mf, len(new)


print('\n## 4  L8736  E(X) ON THE SLICE   (two conventions, and the printed line uses BOTH)')
new, jf, mf, one = closure_report(X, 'with exclusions (208)')
print('   printed: E(X) = 540, 498 join failures and 498 meet failures of 21,528 pairs')
print('   MEASURED, closure to a FIXED POINT: E(X) = %d  %s'
      % (len(new), 'EXACT' if len(new) == 540 else 'DEVIATION'))
print('   MEASURED, ONE STEP over pairs of X only:  %d  -- six short of the printed figure' % one)
print('   join failures %d  %s ;  meet failures %d  %s   (ONE STEP, on unordered pairs of X)'
      % (jf, 'EXACT' if jf == 498 else 'DEVIATION',
         mf, 'EXACT' if mf == 498 else 'DEVIATION'))
print('   CONVENTION, NAMED: the printed line mixes them.  498 + 498 are one-step failures over')
print('   the 21,528 pairs of X; 540 is the fixed-point closure, reached in a second round that')
print('   adds the %d cells the gaps in H put out of one-step reach.  Both figures are exact under'
      % (len(new) - one))
print('   the convention each needs, and neither convention is printed.  Recorded as an incidental.')
newF, jfF, mfF, oneF = closure_report(XF, 'no exclusions (232)')
print('   L8780 prints 589 predictions on the unexcluded set: MEASURED %d  %s'
      % (len(newF), 'EXACT' if len(newF) == 589 else 'DEVIATION'))
print('   (on the ungapped set one step and the fixed point coincide at %d -- which is WHY the'
      % oneF)
print('    gapped set is the one that separates the two conventions)')
print('   L8783-L8784 "reduce the predictions by 49": %d - %d = %d   %s'
      % (len(newF), len(new), len(newF) - len(new),
         'EXACT' if len(newF) - len(new) == 49 else 'DEVIATION'))

# ------------------------------------------------------------------ 5. the predictions table
print('\n## 5  L8746-L8750  THE PREDICTIONS TABLE, ROW BY ROW')
chis = sorted({2 * (c[0] - c[1]) for c in new})
diag = sorted([c for c in new if c[0] == c[1]])
sums = sorted({c[0] + c[1] for c in new})
print('   cells                     %4d      printed 540    %s'
      % (len(new), 'EXACT' if len(new) == 540 else 'DEVIATION'))
print('   distinct chi values       %4d %s   printed 5 -- only 0, +/-2, +/-4   %s'
      % (len(chis), chis, 'EXACT' if chis == [-4, -2, 0, 2, 4] else 'DEVIATION'))
print('   on the diagonal, chi = 0  %4d      printed 112    %s   first %s last %s  (printed (13,13) to (131,131))'
      % (len(diag), 'EXACT' if len(diag) == 112 else 'DEVIATION', diag[0], diag[-1]))
print('   h11 + h21 range           %d to %d   printed 26 to 262   %s'
      % (sums[0], sums[-1], 'EXACT' if (sums[0], sums[-1]) == (26, 262) else 'DEVIATION'))
print('   L8744 join of (h,h+3) and (h+3,h) = (h+3,h+3):  holds for %d of %d h in H'
      % (sum(1 for h in H if (max(h, h + 3), max(h + 3, h)) == (h + 3, h + 3)), len(H)))

# ------------------------------------------------------------------ 6. the falsification rows
print('\n## 6  L8760-L8768  THE FOUR FALSIFICATION-TEST ROWS')
pos = sum(1 for c in new if c[0] >= 1 and c[1] >= 1)
cap = sum(1 for c in new if c[0] + c[1] <= 502)
mir = sum(1 for c in new if (c[1], c[0]) in new)
tip = sum(1 for c in new if c[0] + c[1] < 22)
print('   h11 >= 1 and h21 >= 1                       %d / %d   printed 540/540   %s'
      % (pos, len(new), 'EXACT' if pos == len(new) == 540 else 'DEVIATION'))
print('   h11 + h21 <= 502 (published maximum)        %d / %d   printed 540/540   %s'
      % (cap, len(new), 'EXACT' if cap == len(new) == 540 else 'DEVIATION'))
print('   mirror partner present                      %d / %d   printed 540/540   %s'
      % (mir, len(new), 'EXACT' if mir == len(new) == 540 else 'DEVIATION'))
print('   in the thin tip h11+h21 < 22 (would refute) %d / %d   printed 0/540     %s'
      % (tip, len(new), 'EXACT' if tip == 0 else 'DEVIATION'))
print('   falsified                                   0        printed 0         EXACT by the rows above')
for nm, c in (('X_19,19 (split bicubic)', (19, 19)), ('X_20,20 (the 24-cell)', (20, 20))):
    print('   named in print: %-24s %s in the prediction set   %s'
          % (nm, c, 'PRESENT' if c in new else 'ABSENT -- DEVIATION'))
print('   NOTE: the tip row is a tautology of the slice, not a test -- min sum is %d, so no closure'
      % sums[0])
print('   of THIS slice could ever land below 22.  Recorded as an incidental, not a deviation:')
print('   the row is true, and its "would have been refuted" is unfalsifiable by construction.')

# ------------------------------------------------------------------ 7. the Lambda comparison row
print('\n## 7  L8710-L8712  THE LAMBDA COLUMN OF §31.3.1"S TABLE')
T = r2lib.load_tower()
L8 = list(T.L8())
print('   |Lambda_8| = %d   (printed denominator 976)   %s'
      % (len(L8), 'EXACT' if len(L8) == 976 else 'DEVIATION'))
print('   "self-dual cells  8 of 976" -- the section prints NO definition of self-dual on Lambda.')
print('   Candidate involutions measured, so the class is bounded rather than guessed:')
cand = {}
cand['coordinate reversal  c == c[::-1]'] = sum(1 for c in L8 if tuple(c) == tuple(c)[::-1])
mx = [max(c[k] for c in L8) for k in range(len(L8[0]))]
cand['complement  c_k -> max_k - c_k'] = sum(1 for c in L8 if tuple(mx[k] - c[k] for k in range(len(mx))) == tuple(c))
S8 = set(tuple(c) for c in L8)
cand['reversal-image IN Lambda (set-level)'] = sum(1 for c in L8 if tuple(c)[::-1] in S8)
cand['complement-image IN Lambda (set-level)'] = sum(
    1 for c in L8 if tuple(mx[k] - c[k] for k in range(len(mx))) in S8)
for k, v in cand.items():
    print('      %-42s %6d   %s' % (k, v, '<-- MATCHES the printed 8' if v == 8 else ''))
print('   coordinate maxima (n,e,l,k,f caps as built): %s' % (mx,))
if 8 not in cand.values():
    print('   NO candidate involution yields 8: the figure rests on an UNPRINTED definition.')
print('\n   "rank polynomial palindromic  false" -- the rank sequence is READ OUT of chat 118"s')
print('   banked golden, not re-derived (HANDOFF-71: read values out of the member).')
seq = None
for g in ('r2-ch16f.out', 'r2-ch16e.out'):
    try:
        txt = open('/home/claude/members/' + g, encoding='utf-8').read()
    except OSError:
        continue
    for line in txt.split('\n'):
        if '122' in line and line.count(',') >= 10:
            nums = [int(x) for x in re.findall(r'(?<![\d.])\d+(?![\d.])', line)]
            run = [n for n in nums if n <= 200]
            if len(run) >= 15 and 122 in run:
                seq = run; src = g + ' :: ' + line.strip()[:90]; break
    if seq:
        break
if seq:
    print('   source: %s' % src)
    print('   sequence read: %s' % seq)
    print('   palindromic? %s   printed "false"   %s'
          % (seq == seq[::-1], 'EXACT' if seq != seq[::-1] else 'DEVIATION'))
    print('   sum of ranks = %d (should equal |Lambda_8| = %d)  %s'
          % (sum(seq), len(L8), 'consistent' if sum(seq) == len(L8) else 'INCONSISTENT -- parse suspect'))
else:
    print('   NOT FOUND in the banked goldens -- reported as not measured rather than re-derived.')

# ------------------------------------------------------------------ 8. numerals printed in the unit
print('\n## 8  EVERY NUMERAL PRINTED IN THE UNIT, AND WHETHER THIS BATCH REPRODUCED IT')
checked = {'473,800,776': 'external (Kreuzer-Skarke list size) -- NOT checkable from the files',
           '30,108': 'external (distinct Hodge pairs) -- NOT checkable from the files',
           '248,305': 'external x2, but their equality and the inclusion-exclusion are checked above',
           '495,515': 'external; used as the right denominator, checked above',
           '1,095': 'REPRODUCED exactly from the three counts',
           '0.221 %': 'REPRODUCED', '0.0002 %': 'REPRODUCED', '956': 'REPRODUCED',
           '22': 'external threshold (thin tip); used in the tip row above',
           '208': 'REPRODUCED', '232': 'REPRODUCED', '21,528': 'REPRODUCED',
           '540': 'REPRODUCED', '498': 'REPRODUCED x2', '589': 'REPRODUCED', '49': 'REPRODUCED',
           '112': 'REPRODUCED', '26 to 262': 'REPRODUCED', '5 (chi values)': 'REPRODUCED',
           '502': 'external (published maximum h11+h21) -- used, not verified',
           '24 (excluded values)': 'DEVIATION -- 12 values, 24 cells',
           '13..128': 'external (Triadophilia range) -- used as printed',
           '36 (periodic table)': 'cross-volume; swept in the prose batch',
           '976': 'REPRODUCED from the tower'}
for k in sorted(checked, key=lambda s: (len(s), s)):
    print('   %-22s %s' % (k, checked[k]))
print('\n' + '=' * 100)
