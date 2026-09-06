#!/usr/bin/env python3
"""r2-ch15z — chat 116, COMPUTABLE batch for main L8347-L8450 (§30.2, §30.2.1, §30.2.2,
§30.2.3, §30.3 head, §30.3.1, §30.3.2).

Every figure printed in the unit is recomputed from the unit's own tables, from the tower, or
from the constraint languages the unit describes.  Nothing is recited.

Functions owed to r2lib and carried here with provenance (DEFERRED): body_range (chat 108),
a digit-bounded numeral sweep (chat 109), a space-aligned table parser (chat 110).
"""
import importlib.util, itertools, math, os, re, sys
from decimal import Decimal, ROUND_HALF_UP

H = '/home/claude/members'
spec = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
from r2lib import heading_line, section_span, has_token, enclosing, Rset, load_tower

VOL = {
    'main': 'The_Method_1_6-2.md',
    'reg':  'The_Method_1_6___The_Register-2.md',
    'mc':   'The_Method_1_6___Mathematical_Compendium-2.md',
    'pc':   'The_Method_1_6___The_Physics_Compendium-2.md',
    'ioi':  'The_Method_1_6___The_Index_of_Indices-2.md',
    'sc':   'The_Method_1_6___Spectra_Compendium-2.md',
}
LINES = {t: open(os.path.join(H, f), encoding='utf-8').read().split('\n') for t, f in VOL.items()}
M = LINES['main']
PP = open('/home/claude/PP_The_Method_1_6.md', encoding='utf-8').read().split('\n')

LO, HI = 8347, 8450
MINUS = '\u2212'


def q(x, places='0.01'):
    """Decimal rounding, half-up, named convention.  Python's round() is binary and wrong on .5."""
    return Decimal(repr(x)).quantize(Decimal(places), rounding=ROUND_HALF_UP)


def body_range(Mx, sec):
    """[start, end) of a section's OWN body — to the next heading of ANY number, so subsections
    are excluded.  section_span keeps them.  Owed to r2lib; provenance chat 108."""
    s = heading_line(Mx, sec)
    if s is None:
        return None
    for i in range(s + 1, len(Mx) + 1):
        if re.match(r'^#{1,4} ', Mx[i - 1].strip()):
            return (s, i)
    return (s, len(Mx) + 1)


def nums(line):
    """Every numeral on a line, unicode minus included."""
    return [x.replace(MINUS, '-') for x in re.findall(r'[' + MINUS + r'-]?\d+(?:\.\d+)?', line)]


def sites(tok):
    """Digit-bounded sweep of a numeral across all six volumes.  Both the comma-grouped and the
    bare spelling are swept; a bare \\b would match 480 inside 1,480."""
    forms = {tok}
    bare = tok.replace(',', '')
    forms.add(bare)
    if len(bare) > 3 and bare.isdigit():
        forms.add('{:,}'.format(int(bare)))
    out = []
    for tag, L in LINES.items():
        for i, t in enumerate(L, 1):
            for f in forms:
                if re.search(r'(?<![\d.,])' + re.escape(f) + r'(?![\d.,])', t):
                    out.append((tag, i, t.strip()[:96]))
                    break
    return out


print('=' * 100)
print('r2-ch15z  COMPUTABLE  chat 116  main L%d-L%d  (§30.2 - §30.3.2)' % (LO, HI))
print('=' * 100)

# ------------------------------------------------------------------ 1. extent, resolved twice
print('\n## 1  EXTENT, resolved under body_range AND section_span')
for sec in ('30.2', '30.2.1', '30.2.2', '30.2.3', '30.3', '30.3.1', '30.3.2'):
    br, ss = body_range(M, sec), section_span(M, sec)
    same = 'COINCIDE' if br == ss else 'DIFFER'
    print('  §%-8s body_range %-14s section_span %-14s %s' % (sec, br, ss, same))
print('  §30.3 head resolves to L%s; chapter 31 head L%s (BODY occurrences)'
      % (heading_line(M, '30.3'), heading_line(M, '31')))

# ------------------------------------------------------------------ 2. the ten invariants
print('\n## 2  L8348 "Ten structural invariants" against its own list')
lst = ' '.join(M[8347:8349])
named = [s.strip() for s in lst.split('—', 1)[1].split(', over')[0].split(',')]
print('  named:', ' | '.join(named))
print('  COUNT %d  printed "Ten"  ->  %s' % (len(named), 'MATCH' if len(named) == 10 else 'MISMATCH'))

# ------------------------------------------------------------------ 3. the density table
print('\n## 3  L8354-L8359 density table, and L8361')
rows = []
for i in range(8354, 8360):
    t = M[i - 1]
    if t.strip().startswith('|') and '---' not in t:
        c = [x.strip().replace('*', '') for x in t.strip().strip('|').split('|')]
        if c[0].lower().startswith('solution'):
            continue
        rows.append((c[0], c[1], c[2]))
for r in rows:
    print('   %-16s free %-6s mean %s' % r)
bf = [float(r[1].rstrip('%')) for r in rows]
mb = [float(r[2]) for r in rows]
print('  backtrack-free monotone increasing: %s   mean backtracks monotone decreasing: %s'
      % (all(a < b for a, b in zip(bf, bf[1:])), all(a > b for a, b in zip(mb, mb[1:]))))
print('  L8361 "hard exactly when the solution is nearly unique" — the rarest bucket is the '
      'hardest (%s%% free, %s mean) and the unique-solution bucket is free: %s'
      % (bf[0], mb[0], bf[-1] == 100.0 and mb[-1] == 0.0))
print('  NOTE the top bucket is fraction 1.00 = solution ALWAYS, i.e. least unique, and it is the '
      'EASIEST; "nearly unique" is the 0.009-0.25 bucket at %s%%' % bf[0])

# ------------------------------------------------------------------ 4. the six-invariant re-run
print('\n## 4  L8367 "six invariants discovered since" against the table it introduces')
tbl = []
for i in range(8369, 8375):
    t = M[i - 1].rstrip()
    if not t.strip():
        continue
    lab = re.split(r'\s{2,}', t.strip())[0]
    tbl.append((i, lab, nums(t)))
for i, lab, n in tbl:
    print('   L%d  %-32s %s' % (i, lab, n))
data = [r for r in tbl if not r[1].lower().startswith(('invariant', 'best of'))]
print('  DATA ROWS %d   header/baseline rows %d   printed "six invariants discovered since" -> %s'
      % (len(data), len(tbl) - len(data), 'MATCH' if len(data) == 6 else 'MISMATCH'))
disc = re.findall(r'the containment forest, ([^.]+)\.', ' '.join(M[8365:8367]))
print('  L8366-67 names as discovered since: containment forest, %s' % (disc[0] if disc else '?'))

print('\n## 5  L8376 "beats 0.31 by twofold", and the two-link claim')
best_steps = max(abs(float(n[0])) for _, lab, n in data if n)
print('  best structural corr with steps = %.3f   0.31 baseline   ratio %s  (Decimal, HALF_UP, 2dp)'
      % (best_steps, q(best_steps / 0.31)))
print('  "twofold" holds at 2dp: %s' % (q(best_steps / 0.31) == Decimal('1.95')))
dens = [abs(float(n[1])) for _, lab, n in data if len(n) > 1]
print('  structural invariant -> density, best |corr| = %.3f' % max(dens))
ld = [abs(float(n[0])) for _, lab, n in data if lab.lower().startswith('log solution')]
print('  density -> difficulty |corr| = %s' % (ld[0] if ld else '?'))
print('  L8376-77 "predicts the density better than the density predicts the difficulty": %s > %s = %s'
      % (max(dens), ld[0] if ld else '?', max(dens) > (ld[0] if ld else 9)))
print('  ADJACENT: L8352 prints -0.68 for density-in-log over the 211 instances; the re-run over 928 '
      'prints -0.628.  Same quantity, two populations, two spellings.')

# ------------------------------------------------------------------ 6. the row-support table
print('\n## 6  L8385-L8389 row-support table: max/d^2, monotonicity, and the fit')
rs = []
for i in range(8385, 8390):
    t = M[i - 1].rstrip()
    if not t.strip():
        continue
    n = nums(t)
    if len(n) == 4 and n[0].isdigit() and int(n[0]) in (2, 3, 4, 5):
        rs.append((i, int(n[0]), float(n[1]), int(n[2]), float(n[3])))
for i, d, mean, mx, ratio in rs:
    calc = q(mx / d ** 2)
    print('   L%d  d=%d  mean %-5s max %-3d  printed max/d^2 %-5s  computed %s  %s'
          % (i, d, mean, mx, ratio, calc, 'OK' if abs(float(calc) - ratio) < 0.005 else 'MISMATCH'))
col = [r[4] for r in rs]
print('  L8391 "the ratio does not climb": column %s  monotone increasing = %s -> claim %s'
      % (col, all(a < b for a, b in zip(col, col[1:])), 'HOLDS' if not all(a < b for a, b in zip(col, col[1:])) else 'FAILS'))
xs = [math.log(r[1]) for r in rs]
ys = [math.log(r[2]) for r in rs]
n = len(xs)
mx_, my_ = sum(xs) / n, sum(ys) / n
sxy = sum((a - mx_) * (b - my_) for a, b in zip(xs, ys))
sxx = sum((a - mx_) ** 2 for a in xs)
syy = sum((b - my_) ** 2 for b in ys)
slope = sxy / sxx
r2 = (sxy ** 2) / (sxx * syy)
print('  POINTS in the printed table: %d   printed "on five points" -> %s'
      % (n, 'MATCH' if n == 5 else 'MISMATCH'))
print('  log-log slope on the printed points = %s (printed 2.29)   R^2 = %s (printed range 0.37-0.42)'
      % (q(slope), q(r2)))
print('  slope reproduces at 2dp: %s      R^2 falls in the printed range: %s'
      % (q(slope) == Decimal('2.29'), Decimal('0.37') <= q(r2) <= Decimal('0.42')))
for lab, idx in (('max', 3), ('max/d^2', 4)):
    yy = [math.log(r[idx]) for r in rs if r[idx] > 0]
    if len(yy) == n:
        s2 = sum((a - mx_) * (b - sum(yy) / n) for a, b in zip(xs, yy)) / sxx
        print('  alternative fit, log %-8s vs log d: slope %s' % (lab, q(s2)))

# ------------------------------------------------------------------ 7. Prints & Proofs witness
print('\n## 7  PRINTS & PROOFS witness for both tables (Ruling 56: did the missing rows exist?)')
for probe in ('distinct row supports', 'structural invariants', 'log solution density', 'nesting pairs'):
    hits = [i for i, t in enumerate(PP, 1) if probe in t]
    print('  PP %-24s %d site(s) %s' % (probe, len(hits), hits[:6]))
pp_anchor = [i for i, t in enumerate(PP, 1) if 'distinct row supports' in t]
if pp_anchor:
    a = pp_anchor[0]
    print('  PP context around L%d:' % a)
    for i in range(max(1, a - 8), min(len(PP), a + 8)):
        print('     P%d  %s' % (i, PP[i - 1].rstrip()[:104]))

# ------------------------------------------------------------------ 8. pair conventions
print('\n## 8  L8407 "all 475,800 pairs of Lambda" — the convention named')
T = load_tower()
L8 = [tuple(c) for c in T.L8()]
N = len(L8)
print('  |Λ₈| = %d   C(N,2) UNORDERED = %s   N^2 ORDERED = %s   N(N-1) ORDERED DISTINCT = %s'
      % (N, format(N * (N - 1) // 2, ','), format(N * N, ','), format(N * (N - 1), ',')))
print('  printed 475,800 is the UNORDERED convention: %s' % (N * (N - 1) // 2 == 475800))
S = set(L8)
jl = ml = 0
for a, b in itertools.combinations(L8, 2):
    if tuple(map(max, zip(a, b))) not in S:
        jl += 1
    if tuple(map(min, zip(a, b))) not in S:
        ml += 1
print('  over all %s unordered pairs: join leaks %d, meet leaks %d -> Λ₈ is a sublattice: %s'
      % (format(N * (N - 1) // 2, ','), jl, ml, jl == 0 and ml == 0))

# ------------------------------------------------------------------ 9. R-closure vs join/meet
print('\n## 9  L8406-L8408 "ℛ-closure and closure under join and meet are the SAME CONDITION"')


def sublat(X):
    Xs = set(X)
    for a, b in itertools.combinations(X, 2):
        if tuple(map(max, zip(a, b))) not in Xs or tuple(map(min, zip(a, b))) not in Xs:
            return False
    return True


def sweep(box, label, cap=None):
    cells = list(itertools.product(*[range(c) for c in box]))
    tested = agree = dis = 0
    universe = range(1, 1 << len(cells))
    if cap:
        step = max(1, (1 << len(cells)) // cap)
        universe = range(1, 1 << len(cells), step)
    for mask in universe:
        X = [cells[k] for k in range(len(cells)) if mask >> k & 1]
        if not X:
            continue
        a = (Rset(X) == set(X))
        b = sublat(X)
        tested += 1
        if a == b:
            agree += 1
        else:
            dis += 1
            if dis <= 3:
                print('     DISAGREEMENT %s ℛ-closed=%s sublattice=%s  X=%s' % (label, a, b, X))
    print('  %-12s subsets tested %-7d agreements %-7d disagreements %d' % (label, tested, agree, dis))
    return tested, dis


tot = bad = 0
for box, lab, cap in (((2, 2), '2x2', None), ((3, 2), '3x2', None), ((3, 3), '3x3', None),
                      ((2, 2, 2), '2x2x2', None), ((4, 3), '4x3', 600), ((3, 3, 3), '3x3x3', 600)):
    t_, d_ = sweep(box, lab, cap)
    tot += t_; bad += d_
print('  TOTAL %d instances, %d disagreements -> the identity holds on every one: %s'
      % (tot, bad, bad == 0))
print('  the unit prints 1,487 instances and zero disagreements; this is an independent sweep, '
      'not a reproduction of that population')

# ------------------------------------------------------------------ 10. the constraint language
print('\n## 10  L8424-L8434 THE LAW — arity, bijunctivity, Schaefer')


def maj(a, b, c):
    return tuple((x + y + z >= 2) * 1 for x, y, z in zip(a, b, c))


def closed_under(S, op):
    return all(op(a, b, c) in S for a in S for b in S for c in S)


for k, nv in ((2, 1), (3, 2), (4, 3)):
    pts = list(itertools.product((0, 1), repeat=nv))
    total = nonconst = bij = 0
    for mask in range(1 << len(pts)):
        S = frozenset(p for i, p in enumerate(pts) if mask >> i & 1)
        total += 1
        if len(S) in (0, len(pts)):
            continue
        nonconst += 1
        if closed_under(S, maj):
            bij += 1
    print('  arity %d -> %d XOR-difference variable(s): %d relations, %d non-constant, %d bijunctive'
          % (k, nv, total, nonconst, bij))
    print('        entirely bijunctive: %s' % (bij == nonconst))

one_in_3 = frozenset(p for p in itertools.product((0, 1), repeat=3) if sum(p) == 1)
print('  exactly-one-of-three, |S| = %d' % len(one_in_3))
tests = {
    '0-valid': (0, 0, 0) in one_in_3,
    '1-valid': (1, 1, 1) in one_in_3,
    'Horn (min-closed)': all(tuple(map(min, zip(a, b))) in one_in_3 for a in one_in_3 for b in one_in_3),
    'dual-Horn (max-closed)': all(tuple(map(max, zip(a, b))) in one_in_3 for a in one_in_3 for b in one_in_3),
    'affine (xor-closed)': all(tuple((x ^ y ^ z) for x, y, z in zip(a, b, c)) in one_in_3
                              for a in one_in_3 for b in one_in_3 for c in one_in_3),
    'bijunctive (majority)': closed_under(one_in_3, maj),
}
for k_, v in tests.items():
    print('     %-24s %s' % (k_, v))
print('  no Schaefer class covers it: %s' % (not any(tests.values())))
print('  L8427 "all 14 constraints that arise are 2-SAT expressible" at arity 3 vs measured '
      'non-constant relations on 2 variables')
print('  L8446 caption "114 of 141 at arity 4" vs measured on 3 variables (above)')

# ------------------------------------------------------------------ 11. numeral sweeps
print('\n## 11  DIGIT-BOUNDED numeral sweeps across all six volumes')
for tok in ('211', '928', '1,480', '1,487', '3,781', '475,800', '396', '141', '114', '2.29',
            '0.31', '0.606', '0.883', '0.628', '0.68'):
    s = sites(tok)
    inrange = [x for x in s if x[0] == 'main' and LO <= x[1] <= HI]
    print('  %-9s %2d site(s), %d in unit' % (tok, len(s), len(inrange)))
    for tag, i, t in s:
        if not (tag == 'main' and LO <= i <= HI):
            print('        %-4s L%-6d %s' % (tag, i, t))

print('\n## 12  the "300/300" claim of L8441')
for tok in ('300',):
    s = sites(tok)
    print('  %s: %d site(s) in six volumes' % (tok, len(s)))
    for tag, i, t in s:
        print('        %-4s L%-6d %s' % (tag, i, t))

print('\nEND r2-ch15z')
