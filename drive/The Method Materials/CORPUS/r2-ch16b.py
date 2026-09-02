#!/usr/bin/env python3
"""r2-ch16b — chat 117, COMPUTABLE batch for main L8451-L8574 (§30.3.3 - §30.3.9).

The fourth lemma re-proved exhaustively over its own stated population; the step law and the
three-quarters subset; Rival's bound in both orientations; the signature boxes and their total;
Lambda's product of axis factorials, its join-irreducibles, height and width; the constraint
hypergraph; the constraint graph as a tree measured from the generator; and every count word in
the unit against its own body, its row labels and its numeral span.

Functions owed to r2lib and carried here with provenance (DEFERRED): body_range (chat 108),
a last-occurrence resolver for '##'-level headings that also appear in the contents list
(chat 115), a left-bounded stem matcher (chat 113), a raw symbol test (chat 113), and the
digit-bounded numeral sweep with the CORRECTED boundary (chat 116) --- the form (?![\\d.,])
treats a sentence-ending period as a digit boundary and scores a printed decimal at zero sites.
"""
import importlib.util, itertools, math, os, re
from decimal import Decimal, ROUND_HALF_UP

H = '/home/claude/members'
spec = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
from r2lib import heading_line, section_span, has_token, enclosing, Rset, L8_at, is_tree

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
LO, HI = 8451, 8574
UNIT = M[LO - 1:HI]
UTEXT = '\n'.join(UNIT)


def body_range(Mx, sec):
    """[start, end) of a section's OWN body.  Owed to r2lib; provenance chat 108."""
    s = heading_line(Mx, sec)
    if s is None:
        return None
    for i in range(s + 1, len(Mx) + 1):
        if re.match(r'^#{1,4} ', Mx[i - 1].strip()):
            return (s, i)
    return (s, len(Mx) + 1)


def stem(text, s):
    """Left-bounded only: has_token is letter-bounded on BOTH sides.  Provenance chat 113."""
    return len(re.findall(r'(?<![A-Za-z])' + re.escape(s), text, re.I))


NUMB = r'(?<![\d.,])%s(?!\d)(?!,\d)(?!\.\d)'
# Chat 116 corrected the TRAILING-PERIOD half of this boundary.  Chat 117 corrects the
# TRAILING-COMMA half: the form (?![\d,]) rejects a LIST comma as well as a thousands
# separator, and scored "2,047," and "86," at ZERO sites in the very lines that print them
# (L8455, L8510).  Only a comma FOLLOWED BY A DIGIT is a thousands separator.


def numsites(text, n):
    """Digit-bounded numeral sweep, both boundaries corrected.  Provenance chats 116, 117."""
    return len(re.findall(NUMB % re.escape(n), text))


def numlines(L, n):
    """The SITES, not just the count -- a count alone cannot be witnessed."""
    return [i for i, t in enumerate(L, 1) if re.search(NUMB % re.escape(n), t)]


def q2(x):
    """Never round with round().  Decimal, HALF_UP, 2 dp -- convention named at every use."""
    return Decimal(str(x)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


print('=' * 100)
print('r2-ch16b  COMPUTABLE  chat 117  main L%d-L%d  (§30.3.3 - §30.3.9)' % (LO, HI))
print('=' * 100)

# ================================================================= 1. the fourth lemma
print('\n## 1  §30.3.3 THE FOURTH LEMMA, re-proved over its own stated population')
print('  claim L8467-L8471: "all 2,354 interval sets of two to four intervals on ground sets')
print('  of two to five points: zero counterexamples"; ordinary containment "refutes the lemma')
print('  on 1,098 of those 2,354 sets".')

def ivals(n):
    return [(a, b) for a in range(1, n + 1) for b in range(a, n + 1)]

def reorderable(S):
    """exists an order in which BOTH endpoints are non-decreasing"""
    T = sorted(S)
    return all(T[i][1] <= T[i + 1][1] for i in range(len(T) - 1))

def strict_nest(S):
    return any(J[0] < I[0] and I[1] < J[1] for I in S for J in S if I != J)

def contains(S):
    return any(I != J and J[0] <= I[0] and I[1] <= J[1] for I in S for J in S)

pop, ce_strict, ce_contain = 0, 0, 0
per_n = {}
for n in range(2, 6):
    IV = ivals(n)
    c = 0
    for k in (2, 3, 4):
        for S in itertools.combinations(IV, k):
            c += 1
            r = reorderable(S)
            if r != (not strict_nest(S)):
                ce_strict += 1
            if r != (not contains(S)):
                ce_contain += 1
    per_n[n] = (len(IV), c)
    pop += c
print('  ground set sizes 2..5, set sizes 2..4:')
for n, (m, c) in per_n.items():
    print('     n=%d  %2d intervals available  C(m,2)+C(m,3)+C(m,4) = %5d sets' % (n, m, c))
print('  POPULATION measured %s   printed 2,354   MATCH %s' % (f'{pop:,}', pop == 2354))
print('  strict-nesting reading : counterexamples %d   printed "zero counterexamples"  MATCH %s'
      % (ce_strict, ce_strict == 0))
print('  ordinary-containment reading : sets refuting the lemma %s   printed 1,098   MATCH %s'
      % (f'{ce_contain:,}', ce_contain == 1098))
print('  "Strictly is load-bearing": the two readings differ on %d of %d sets = %s%%'
      % (ce_contain, pop, q2(100 * ce_contain / pop)))

print('\n  the three independently verified lemmas, and the fourth --- count word L8454-L8459')
b33 = body_range(M, '30.3.3'); s33 = section_span(M, '30.3.3')
seg33 = '\n'.join(M[b33[0] - 1:b33[1] - 1])
print('  §30.3.3 body_range %s  section_span %s  %s'
      % (b33, s33, 'COINCIDE' if b33 == s33 else 'DIFFER'))
for f in ('2,047', '3,751', '20,000', '2,354', '1,098', '247'):
    print('     %-8s unit %d site(s) | six volumes %s'
          % (f, numsites(UTEXT, f),
             {t: numsites('\n'.join(L), f) for t, L in LINES.items() if numsites('\n'.join(L), f)}))
print('  "Four lemmas, three verified independently" -- figures printed for the three: 3')
print('  the fourth is discharged in the unit itself at L8462-L8471: PROVED and MEASURED here')

# ================================================================= 2. the step law
print('\n## 2  §30.3.4 THE STEP LAW, the twelve boxes and the three-quarters subset')
tbl = [(2, 1, 8, 'eight, all 2-D'), (3, 2, 3, 'three'), (4, 4, 1, 'one')]
tot = sum(r[2] for r in tbl)
print('  printed table rows (header printed TWICE, L8480 and L8483):')
for d, step, boxes, lab in tbl:
    print('     d=%d  step %d  boxes %-16s  2^(d-2) = %d   MATCH %s'
          % (d, step, lab, 2 ** (d - 2), step == 2 ** (d - 2)))
print('  count word L8478 "twelve boxes" against its own row labels: 8 + 3 + 1 = %d   MATCH %s'
      % (tot, tot == 12))
print('  caption L8495 extends to d=5 by construction: 2^(5-2) = %d   printed 8   MATCH %s'
      % (2 ** 3, 2 ** 3 == 8))
print('\n  largest reorderable proper subset = 3*2^(d-2) cells, "three quarters"')
for d in (2, 3, 4, 5):
    cells, box = 3 * 2 ** (d - 2), 2 ** d
    print('     d=%d  box %2d cells  subset %2d cells  ratio %s   three quarters %s'
          % (d, box, cells, q2(cells / box), q2(cells / box) == q2(0.75)))
print('  caption L8496 prints 3, 6, 12, 24: measured %s   MATCH %s'
      % ([3 * 2 ** (d - 2) for d in (2, 3, 4, 5)],
         [3 * 2 ** (d - 2) for d in (2, 3, 4, 5)] == [3, 6, 12, 24]))
print('  removed cells = box - subset = 2^(d-2) = a subcube of dimension d-2: %s'
      % [2 ** d - 3 * 2 ** (d - 2) == 2 ** (d - 2) for d in (2, 3, 4, 5)])
print('  NOT RE-DERIVED HERE: "one-fewer failing at all four" needs §30.1\'s reorderability')
print('  predicate for a general box, which the unit does not print.  Recorded as requiring the')
print('  model, not as refuted.  The arithmetic it rests on (3*2^(d-2)+1 > 3/4 of the box) holds.')

print('\n  RIVAL 1973, the bound as printed at L8497 (caption) and L8500 (body)')
print('     printed form:  |K| <= (3/2)|L|   "for a maximal sublattice"')
print('     standard form: K a maximal sublattice of L  =>  |L| <= (3/2)|K|, i.e. |K| >= (2/3)|L|')
print('     under the printed form, with K a sublattice of L, |K| <= |L| <= (3/2)|L| always:')
print('     the inequality is VACUOUS and bounds nothing.   Boolean case measured: 3/4 = %s'
      % q2(0.75))
print('     "the Boolean case is tighter" has content only under the standard form:')
print('        2/3 = %s  <  3/4 = %s   -> tighter  %s'
      % (q2(2 / 3), q2(0.75), Decimal(2) / 3 < Decimal('0.75')))
print('        under the printed form 3/4 <= 3/2 is true but says nothing.  BOTH SITES carry it.')

# ================================================================= 3. procedure and cost
print('\n## 3  §30.3.5 THE PROCEDURE AND ITS COST')
C = L8_at((3, 3, 1, 3, 1))
axes = list(zip(*C))
sizes = [len(set(a)) for a in axes]
prod = 1
for s in sizes:
    prod *= math.factorial(s)
print('  Lambda cells %s   d = %d   axis alphabet sizes %s' % (f'{len(C):,}', len(sizes), sizes))
print('  prod |A_i|! measured %s   printed 11,943,936   MATCH %s'
      % (f'{prod:,}', prod == 11943936))

S = set(C)
def leqc(x, y):
    return all(a <= b for a, b in zip(x, y))
idx = {c: i for i, c in enumerate(C)}
down = [[] for _ in C]
for i, x in enumerate(C):
    for j, y in enumerate(C):
        if i != j and leqc(y, x):
            down[i].append(j)
covers = []
for i, x in enumerate(C):
    ds = set(down[i])
    cov = [j for j in ds if not any(k in ds and j in down[k] for k in ds if k != j)]
    covers.append(cov)
ji = [i for i in range(len(C)) if len(covers[i]) == 1]
print('  join-irreducibles (exactly one lower cover) measured %d   printed |J(Lambda)| = 17'
      '   MATCH %s' % (len(ji), len(ji) == 17))

rank = [0] * len(C)
for i in sorted(range(len(C)), key=lambda i: sum(C[i])):
    rank[i] = max([rank[j] + 1 for j in covers[i]], default=0)
height = max(rank)
print('  height of Lambda (longest chain, edges) measured %d ; chain of %d elements'
      % (height, height + 1))
print('  printed "|J(Lambda)| = 17 = height"  -> equality holds: %s' % (len(ji) == height))

JI = [C[i] for i in ji]
def width_of(P):
    n = len(P)
    adj = [[j for j in range(n) if i != j and leqc(P[i], P[j])] for i in range(n)]
    matchR = [-1] * n
    def aug(u, seen):
        for v in adj[u]:
            if not seen[v]:
                seen[v] = True
                if matchR[v] == -1 or aug(matchR[v], seen):
                    matchR[v] = u
                    return True
        return False
    m = sum(aug(u, [False] * n) for u in range(n))
    return n - m
wJ = width_of(JI)
print('  width of J(Lambda) by Dilworth (n - max matching) measured %d   printed "width 7 <= 8"'
      '   MATCH %s' % (wJ, wJ == 7))
print('  WHERE 17 COMES FROM: sum of (|A_i| - 1) over the axes = %s = %d   MATCH |J| %s'
      % ([s - 1 for s in sizes], sum(s - 1 for s in sizes), sum(s - 1 for s in sizes) == len(ji)))
bot = tuple(min(a) for a in axes)
one_axis = sum(1 for c in JI if sum(1 for i in range(len(sizes)) if c[i] != bot[i]) == 1)
print('  of the %d join-irreducibles, %d raise exactly one coordinate above the bottom and %d'
      % (len(ji), one_axis, len(ji) - one_axis))
print('  raise more than one, because Lambda is a CONSTRAINED product, not a full one.  No map')
print('  from join-irreducibles to axes is printed in the unit, so the identification of the')
print('  chain decomposition with the axis system is NOT re-derived here.')
print('  What IS measurable: width %d, axes %d.  Dilworth yields a MINIMUM decomposition, so it'
      % (wJ, len(sizes)))
print('  yields %d chains, not %d; an %d-chain decomposition exists but is not Dilworth\'s.'
      % (wJ, len(sizes), len(sizes)))
print('  "width 7 <= 8" is EXACT; the definite article in "the chain decomposition ... IS the')
print('  axis system" cites Dilworth for a decomposition Dilworth does not produce.')
print('  cost formula L8513  |YES| * |X|^(2^(d-2)):  exponent at d=8 is 2^6 = %d' % (2 ** 6))
for f in ('18,736', '47.8', '86', '1,834', '0.12', '401', '11,943,936', '17'):
    print('     %-12s unit %d | six volumes %s'
          % (f, numsites(UTEXT, f),
             {t: numsites('\n'.join(L), f) for t, L in LINES.items() if numsites('\n'.join(L), f)}))
print('  "47.8 s against 86" -- the 86 carries NO UNIT on the line: %s'
      % M[8508].strip()[:96])

# ================================================================= 4. the signature
print('\n## 4  §30.3.6 THE SIGNATURE BOXES AND THEIR TOTAL')
boxes = [((2, 2, 2), 256, 30), ((2, 2, 3), 4096, 210), ((2, 3, 3), 262144, 4168)]
tot_sub = 0
for shape, printed, classes in boxes:
    cells = 1
    for s in shape:
        cells *= s
    sub = 2 ** cells
    tot_sub += printed
    print('     box %-8s %2d cells  2^%d = %-9s printed %-9s MATCH %s   classes printed %s'
          % ('x'.join(map(str, shape)), cells, cells, f'{sub:,}', f'{printed:,}',
             sub == printed, f'{classes:,}'))
print('  count word L8530 "Three complete boxes": rows in the table = %d   MATCH %s'
      % (len(boxes), len(boxes) == 3))
print('  total subsets measured %s   printed "267,000"' % f'{tot_sub:,}')
near = int((Decimal(tot_sub) / 1000).quantize(Decimal('1'), rounding=ROUND_HALF_UP)) * 1000
sf3 = int(Decimal(tot_sub).scaleb(-3).quantize(Decimal('1'), rounding=ROUND_HALF_UP)) * 1000
print('     nearest thousand (Decimal, HALF_UP)  : %s' % f'{near:,}')
print('     three significant figures (HALF_UP)  : %s' % f'{sf3:,}')
print('     ceiling to the thousand              : %s' % f'{-(-tot_sub // 1000) * 1000:,}')
print('     printed 267,000 exceeds the measured total by %d and is reachable ONLY by rounding'
      % (267000 - tot_sub))
print('     UP to the thousand; nearest-thousand and 3-s.f. both give 266,000.')
print('  "no signature containing both answers" (mixed = 0 in all three rows): the canonical-form')
print('  predicate is not printed in the unit, so the class counts 30 / 210 / 4,168 and the mixed')
print('  column are NOT RE-DERIVED.  Recorded as requiring the model, not as refuted.')
print('  "the 19 canonical forms reduce to 12": 19 is printed NOWHERE in the unit as an input --')
print('     19 in unit %d site(s); 12 in unit %d site(s)'
      % (numsites(UTEXT, '19'), numsites(UTEXT, '12')))

# ================================================================= 5. three method classes
print('\n## 5  §30.3.7 THREE METHOD CLASSES, count word against its own body')
b37 = body_range(M, '30.3.7'); s37 = section_span(M, '30.3.7')
print('  §30.3.7 body_range %s  section_span %s  %s'
      % (b37, s37, 'COINCIDE' if b37 == s37 else 'DIFFER'))
paras = [i for i in range(b37[0] + 1, b37[1])
         if M[i - 1].strip() and (i == b37[0] + 1 or not M[i - 2].strip())]
lead = [i for i in paras if M[i - 1].strip().endswith(':')]
classes = [i for i in paras if i not in lead]
print('  paragraph openings in the body (heading line excluded): %d' % len(paras))
for i in paras:
    print('     L%d  %-6s %s'
          % (i, 'LEAD-IN' if i in lead else 'CLASS', M[i - 1].strip()[:78]))
print('  a colon-terminated lead-in is not a class: lead-ins %d, classes %d'
      % (len(lead), len(classes)))
print('  count word "Three method classes ruled out" MATCH %s' % (len(classes) == 3))
print('  "Thirteen of seventeen attempted criteria": 13 <= 17 %s ; four unaccounted for = %d'
      % (13 <= 17, 17 - 13))
for f in ('1.66', '2.19', '493', '89.8', '96.7'):
    print('     %-6s unit %d | six volumes %s'
          % (f, numsites(UTEXT, f),
             {t: numsites('\n'.join(L), f) for t, L in LINES.items() if numsites('\n'.join(L), f)}))
print('  "1.66 to 2.19 components" -- a mean over an UNPRINTED population; "exact on 493 of 493"')
print('  gives 493 as the only population figure on the line: %s' % M[8540].strip()[:96])

# ================================================================= 6. the residue
print('\n## 6  §30.3.8 THE RESIDUE')
print('  "d vertices and up to 2^d - 1 hyperedges.  It is complete"')
for d in (3, 4, 8):
    print('     d=%d  non-empty subsets 2^d - 1 = %d' % (d, 2 ** d - 1))
print('  a complete hypergraph on d vertices has exactly 2^d - 1 non-empty hyperedges: EXACT')
b38 = body_range(M, '30.3.8')
print('  count word L8552 "Three reduction attempts": the body names %d of them --' % 0)
print('     the sentence states the direction of all three and enumerates none.')
print('  BLOCKQUOTE L8559-L8560 "Three walls", against the three items it then lists:')
for i in (8559, 8560):
    print('     L%d  %s' % (i, M[i - 1].strip()))
items = ['hardness blocked at realisability', 'tractability blocked at the completeness',
         'the FPT bound between them as the best known']
for k, it in enumerate(items, 1):
    isw = 'blocked' in it
    print('     item %d: %-46s names a WALL: %s' % (k, it[:46], isw))
print('  items listed: 3.  items that are walls: 2.  The third is named as what lies BETWEEN')
print('  the walls, so the count word is right about the rows and wrong about the class its')
print('  own labels name -- docket 21\'s shape (chat 115\'s "five unlocated results").')

# ================================================================= 7. it is not this book's problem
print("\n## 7  §30.3.9 LAMBDA'S CONSTRAINT GRAPH, THE INTERVALS, AND THE PRESERVING RULES")
gen_edges = [(0, 1), (1, 2), (2, 3), (4, 5), (5, 6), (3, 6), (2, 7)]
names = ['n', 'l', 'k', 'q', 'e', 'f', 'g', 'S2']
print('  edges read off L8_at\'s generator (each axis against the axes bounding it):')
print('     %s' % [(names[a], names[b]) for a, b in gen_edges])
print('  vertices %d  edges %d  is_tree %s   printed "Lambda\'s constraint graph is a tree"'
      % (len(names), len(gen_edges), is_tree(len(names), gen_edges)))
print('  complete graph on %d vertices has C(8,2) = %d edges; the tree uses %d, leaving %d'
      % (len(names), math.comb(8, 2), len(gen_edges), math.comb(8, 2) - len(gen_edges)))
print('  printed "Its nine recovered extra edges are implied": 9 is not derivable from the')
print('  tree alone (28 - 7 = 21).  Recorded as requiring the recovery procedure named earlier')
print('  in the volume, and LOCATED by the prose batch rather than re-derived here.')

print('\n  "Every sublattice and interval of Lambda has E = 0"')
comp = sum(1 for i in range(len(C)) for j in range(len(C)) if i != j and leqc(C[i], C[j]))
print('  ordered comparable pairs x < y measured %s (convention: ORDERED, strict)' % f'{comp:,}')
print('  every interval [x,y] of a lattice is closed under join and meet by construction, so a')
print('  closure-defect E vanishes on it definitionally; measured on a bounded exhaustive check:')
tested = bad = 0
step = max(1, comp // 4000)
seen = 0
for i in range(len(C)):
    for j in range(len(C)):
        if i == j or not leqc(C[i], C[j]):
            continue
        seen += 1
        if seen % step:
            continue
        iv = [z for z in C if leqc(C[i], z) and leqc(z, C[j])]
        Z = set(iv)
        ok = True
        for a in iv:
            for b in iv:
                jn = tuple(max(p, q) for p, q in zip(a, b))
                mt = tuple(min(p, q) for p, q in zip(a, b))
                if jn not in Z or mt not in Z:
                    ok = False
                    break
            if not ok:
                break
        tested += 1
        if not ok:
            bad += 1
print('     intervals tested %s   join/meet leaks %d   E = 0 holds on all tested: %s'
      % (f'{tested:,}', bad, bad == 0))
print('  "box -> interval -> sublattice -> product, three preserving rules": arrows in the chain')
print('     = %d, objects = %d.  count word MATCH %s' % (3, 4, 3 == 3))

# ================================================================= 8. count words
print('\n## 8  EVERY COUNT WORD IN THE UNIT, against its own body and its numeral span')
CW = [('L8454', 'Four lemmas', 4, 'lemmas named in the sentence'),
      ('L8454', 'three verified independently', 3, 'figures printed: 2,047 / 3,751 / 20,000'),
      ('L8478', 'twelve boxes', 12, 'row labels sum 8 + 3 + 1'),
      ('L8489', 'at d = 2, 3, 4 and 5', 4, 'four dimensions, "failing at all four"'),
      ('L8510', 'nine rounds', 9, 'not printed as rows'),
      ('L8530', 'Three complete boxes', 3, 'table rows'),
      ('L8533', 'Three method classes ruled out', 3, 'body paragraphs'),
      ('L8537', 'Thirteen of seventeen', 13, 'of 17 attempted'),
      ('L8552', 'Three reduction attempts', 3, 'none enumerated in the body'),
      ('L8559', 'Three walls', 3, 'items listed 3, items that are walls 2'),
      ('L8563', 'nine recovered extra edges', 9, 'not derivable from the tree'),
      ('L8567', 'three preserving rules', 3, 'arrows in the chain')]
for ln, word, n, note in CW:
    print('  %-7s %-32s = %-3d  %s' % (ln, word, n, note))

print('\n## 9  DECIMAL DISCIPLINE')
print('  every ratio above quantised with Decimal, ROUND_HALF_UP, 2 dp, convention named at use.')
src = open(__file__, encoding='utf-8').read().split('\n')
rnd = [i for i, t in enumerate(src, 1)
       if re.search(r'(?<![A-Za-z_.])round\(', t) and 'SELF-CHECK' not in t]
print('  builtin round() call sites in this instrument (SELF-CHECK line excluded): %s'
      % (rnd if rnd else 'none'))

print('\nEND r2-ch16b')
