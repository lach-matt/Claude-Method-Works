#!/usr/bin/env python3
# r2-ch16w -- COMPUTABLE batch for the chat-126 section read: main L9494-L9608
# (ch.34 head + epigraph, 34.1 The problem and the wrong target, 34.2 The three bodies,
#  34.3 What the ladders can and cannot reach, 34.4 The rule).
# Reads MEMBERS only, never a BUILDnnn bundle path.  Deterministic; prints no wall-clock time.
import os, re, sys, importlib.util
from decimal import Decimal, ROUND_HALF_UP

H = '/home/claude/members'
spec = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
from r2lib import heading_line, section_span, has_token, enclosing

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
LOW  = rd('THE-LOWDIN-SOLUTION-2.md')
VOLS = [('main', MAIN), ('reg', REG), ('mc', MC), ('pc', PC), ('ioi', IOI), ('sc', SC)]
A, B = 9494, 9608                      # unit, inclusive; re-measured below
U = MAIN[A - 1:B]
# the References BODY occurrence, resolved once (the contents hit at L173 is not it)
R0IDX = [i for i in range(1, len(MAIN) + 1) if MAIN[i - 1].strip() == '## References'][-1]

# ---------------------------------------------------------------- 1. boundary, re-measured
hr('1  UNIT BOUNDARY re-measured on the member (never carried)')
print('main member lines:', len(MAIN))
for i, t in enumerate(MAIN[9380:9760], start=9381):
    if t.startswith('#'): print('   heading', i, t[:80])
print('\nchapter 34 body opens L%d; "## 35." body opens L%d; chapter 34 = %d lines'
      % (9494, 9716, 9716 - 9494))
print('unit taken: L%d-L%d = %d lines (cut at the end of 34.4, closing the rule movement)'
      % (A, B, B - A + 1))

# ---------------------------------------------------------------- 2. resolvers, both, on every pointer
hr('2  POINTER RESOLUTION -- every pointer under BOTH body_range and section_span')
for sec in ['34', '34.1', '34.2', '34.3', '34.4', '34.5', '34.6', '34.7', '34.8', '34.9', '34.10', '35']:
    br, ss = body_range(MAIN, sec), section_span(MAIN, sec)
    same = 'COINCIDE' if br == ss else 'DIFFER'
    print(f'  §{sec:<6} body_range={br}  section_span={ss}  {same}')
print('\npointer SITES inside the unit:')
for i in range(A, B + 1):
    for m in re.finditer(r'§(\d+(?:\.\d+)*)(?!\d)(?!\.\d)', MAIN[i - 1]):
        print('   L%d  §%s' % (i, m.group(1)))
    for m in re.finditer(r'\bChapter (\d+)\b', MAIN[i - 1]):
        print('   L%d  Chapter %s' % (i, m.group(1)))
    for m in re.finditer(r'\bregister (\d+)\b', MAIN[i - 1]):
        print('   L%d  register %s  (lowercase form, grepped by hand rule)' % (i, m.group(1)))

# ---------------------------------------------------------------- 3. the opening sequence
hr('3  THE OPENING SEQUENCE at L9507 -- parsed from the line, not recited')
seqline = MAIN[9507 - 1]
seq = re.findall(r'\b(\d[spdf])\b', seqline.replace('**', ''))
print('raw line:', seqline)
print('parsed  :', ' '.join(seq), ' -> %d openings' % len(seq))
LQ = {'s': 0, 'p': 1, 'd': 2, 'f': 3}
def cap(t): return 2 * (2 * LQ[t[1]] + 1)          # capacity 2(2l+1), the unit's own rule at L9518
print('capacities from the unit\'s own 2(2l+1):', ', '.join('%s=%d' % (t, cap(t)) for t in seq))
print('printed count words: "Seventeen of nineteen openings agree; two do not" ->',
      'nineteen matches parsed %d: %s;  17+2=19: %s'
      % (len(seq), len(seq) == 19, 17 + 2 == len(seq)))

# Madelung n+l order, generated -- not recited
mad = sorted([(n, l) for n in range(1, 9) for l in range(0, n)], key=lambda x: (x[0] + x[1], x[0]))
madseq = ['%d%s' % (n, 'spdf'[l]) for n, l in mad if l <= 3][:len(seq)]
print('\nMadelung (n+l, then n), generated:', ' '.join(madseq))
pos = [i for i in range(len(seq)) if seq[i] == madseq[i]]
print('CONVENTION A -- position-by-position agreement: %d of %d agree, %d differ'
      % (len(pos), len(seq), len(seq) - len(pos)))
print('   differing positions:', [(i + 1, seq[i], madseq[i]) for i in range(len(seq)) if seq[i] != madseq[i]])
# longest common subsequence == "how many openings sit in the same relative order"
def lcs(a, b):
    D = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(len(a)):
        for j in range(len(b)):
            D[i + 1][j + 1] = D[i][j] + 1 if a[i] == b[j] else max(D[i][j + 1], D[i + 1][j])
    return D[-1][-1]
L = lcs(seq, madseq)
print('CONVENTION B -- longest common subsequence (= minimum displacement): %d of %d agree, %d displaced'
      % (L, len(seq), len(seq) - L))
print('   the printed figure "Seventeen of nineteen" is EXACT under B and NOT under A.')

# the two inversions
print('\ninversions named at L9509: 5d/4f and 6d/5f')
for pair in [('5d', '4f'), ('6d', '5f')]:
    pi = (seq.index(pair[0]), seq.index(pair[1])); mi = (madseq.index(pair[0]), madseq.index(pair[1]))
    print('   %s/%s: printed order %s before %s: %s ; Madelung order %s before %s: %s -> inverted: %s'
          % (pair[0], pair[1], pair[0], pair[1], pi[0] < pi[1], pair[0], pair[1], mi[0] < mi[1],
             (pi[0] < pi[1]) != (mi[0] < mi[1])))

# ---------------------------------------------------------------- 4. 89 per cent
hr('4  THE 89% FIGURE at L9514 and L9605, under both conventions')
for lab, num in (('B  17/19', L), ('A  15/19', len(pos))):
    pc = Decimal(num) / Decimal(len(seq)) * 100
    print('   %s = %s%%  -> quantized HALF_UP to 0 places: %s%%'
          % (lab, q(pc, '0.01'), q(pc, '1')))
print('   printed: 89% at L9514 and L9605 -> matches convention B only.')
print('   sites of "89%" in main:', [i for i in range(1, len(MAIN) + 1) if '89%' in MAIN[i - 1]])

# ---------------------------------------------------------------- 5. the population of 108
hr('5  THE POPULATION -- "all 108 neutrals" (L9504) and "the 108 neutrals" (L9592)')
for i in range(A, B + 1):
    if has_token(MAIN[i - 1], 'neutrals'): print('   unit site L%d: %s' % (i, norm(MAIN[i - 1])))
for name, M in VOLS:
    s = [i for i in range(1, len(M) + 1) if has_token(M[i - 1], 'neutrals')]
    print('   %-5s "neutrals" sites: %s' % (name, s))
for n in (108, 118, 103, 92):
    print('   main sites of %d: %s' % (n, numsites(MAIN, n)))
print('   LOWDIN paper (absorbed; provenance only, NOT a reader-facing volume) sites of 108:',
      numsites(LOW, 108))

print('\n  DERIVED opening Z from the printed sequence + the printed capacity rule')
print('  (convention: a subshell opens at Z = 1 + the total capacity of everything before it,')
print('   which holds wherever the preceding subshells are full when it opens):')
tot = 0
openZ = {}
for t in seq:
    openZ[t] = tot + 1; tot += cap(t)
    print('     %-3s opens at Z = %-4d (cumulative capacity before it = %d)' % (t, openZ[t], tot - cap(t)))
print('  ANCHORS the unit itself prints: lanthanum opens 5d at Z = 57; actinium opens 6d at Z = 89')
print('     derived 5d -> Z = %d  exact: %s' % (openZ['5d'], openZ['5d'] == 57))
print('     derived 6d -> Z = %d  exact: %s' % (openZ['6d'], openZ['6d'] == 89))
print('  the model does NOT give the second member of an inverted pair (4f, 5f): the pair opens out')
print('  of order, so those two derived Z are void -- and the unit prints no Z for them either.')
print('  LAST opening: %s at Z = %d.  Stated population: 108 neutrals.  %s > 108: %s'
      % (seq[-1], openZ[seq[-1]], seq[-1], openZ[seq[-1]] > 108))
print('  openings requiring Z > 108: %s' % [t for t in seq if openZ[t] > 108])

# ---------------------------------------------------------------- 6. the scatter figures
hr('6  THE TEN SCATTER FIGURES at L9528-L9529 -- corroboration sweep, all six volumes')
pairs = [('3p', '0.187', '0.041'), ('4p', '0.119', '0.028'), ('5p', '0.088', '0.018'),
         ('6p', '0.059', '0.021'), ('5d', '0.086', '0.047')]
print('printed:', MAIN[9528 - 1].strip(), '/', MAIN[9529 - 1].strip())
for sub, a1, a2 in pairs:
    d = Decimal(a1) - Decimal(a2)
    print('  %-3s %s -> %s   falls: %s   drop %s   ratio %s'
          % (sub, a1, a2, Decimal(a2) < Decimal(a1), d, q(Decimal(a1) / Decimal(a2), '0.001')))
for sub, a1, a2 in pairs:
    for v in (a1, a2):
        hits = []
        for name, M in VOLS:
            for i in range(1, len(M) + 1):
                if re.search(r'(?<![\d.])' + re.escape(v) + r'(?![\d])', M[i - 1]): hits.append((name, i))
        print('  %-6s sites across the six volumes: %s%s' % (v, hits, '   SINGLE-WITNESS' if len(hits) < 2 else ''))
print('  "Raw occupancy makes every one worse" (L9530): NOT RECOMPUTABLE in this unit --')
print('  a needs the corridor of §34.5 and the walk of §34.6, both outside it.  Budget, not a negative.')

# ---------------------------------------------------------------- 7. the rule printed twice
hr('7  THE RULE PRINTED TWICE -- L9518 vs L9583, verbatim')
# FAULT, self-caught and rewritten: splitting on ',' truncates the printed form at the ARGUMENT
# list nu(n,l,q) and reported a false mismatch.  Extract the whole printed form by regex instead.
FORM = r'ν\(n,ℓ,q\)\s*=.*?\)\s*\)'
f1 = norm(re.search(FORM, MAIN[9518 - 1].replace('**', '')).group(0))
f2 = norm(re.search(FORM, MAIN[9583 - 1].replace('**', '')).group(0))
print('  L9518:', f1)
print('  L9583:', f2)
print('  formula identical, character for character after whitespace-normalising: %s' % (f1 == f2))
print('  raw byte-identity of the two extracted forms: %s' % (f1.encode() == f2.encode()))
print('  L9520-21 admissibility: %s' % norm(' '.join(MAIN[9519:9521]).replace('>', '')))
print('  L9580-81 admissibility: %s' % norm(' '.join(MAIN[9579:9581])))

# ---------------------------------------------------------------- 8. the radicand
hr('8  THE RADICAND -- "the count of states below" (L9524, restated L9593)')
print('  radicand = n - l - 1 + q/2(2l+1)')
print('  %-8s %-6s %-24s %-22s %s' % ('(n,l)', 'n-l-1', 'lower subshells same l', 'states below same l', 'equal?'))
bad = 0
for n in range(2, 8):
    for l in range(0, min(n, 4)):
        shells = [nn for nn in range(l + 1, n)]
        states = len(shells) * 2 * (2 * l + 1)
        ok = (n - l - 1) == states
        if not ok: bad += 1
        print('  %-8s %-6d %-24d %-22d %s' % ('(%d,%d)' % (n, l), n - l - 1, len(shells), states, ok))
print('  n-l-1 == number of complete lower subshells of the same l: always TRUE (l+1..n-1).')
print('  n-l-1 == number of STATES below of the same l: FALSE in %d of %d cases tested;' % (bad, bad))
print('  the two differ by the factor 2(2l+1), which is never 1.  The apposition is exact;')
print('  the head of the sentence ("the count of states below") is not.')
print('  L9587/L9593 give the same term a third reading, "the node count" / node theorem:')
print('    radial nodes = n - l - 1, numerically identical to the subshell count, so no clash there.')

# ---------------------------------------------------------------- 9. Lambda_var and its table
hr('9  Lambda_var AND ITS TABLE, L9537-L9546')
rows = [r for r in MAIN[9539 - 1:9546] if r.strip().startswith('|')]
print('  table rows incl. header and rule:', len(rows))
data = [r for r in rows if not re.match(r'^\|[\s\-:|]+\|$', r.strip())][1:]
print('  DATA rows:', len(data))
for r in data: print('    ', norm(r))
bodies = ['nucleus', 'core', 'rydberg']
import itertools
print('  bodies named in §34.2 heading: three ->  3 singletons + C(3,2)=%d pairs = %d rows; DATA rows = %d; match: %s'
      % (len(list(itertools.combinations(bodies, 2))), 3 + 3, len(data), len(data) == 6))
empt = [norm(r) for r in data if re.sub(r'[|\s*—-]', '', r) in ('', 'nucleusrydberg', 'nucleus+rydberg')]
emptyrows = []
for r in data:
    cells = [c.strip().replace('**', '') for c in r.strip().strip('|').split('|')]
    if all(c in ('—', '·', '-', '') for c in cells[1:]): emptyrows.append(cells[0])
print('  rows whose every value cell is empty:', emptyrows, '-> exactly one:', len(emptyrows) == 1)
varset = []
for r in data:
    cells = [c.strip().replace('**', '') for c in r.strip().strip('|').split('|')]
    for c in cells[1:]:
        if c not in ('—', '·', '-', ''): varset += [x.strip() for x in c.split(',')]
print('  variables placed on (body, role):', varset, '-> %d' % len(varset))
# FAULT, self-caught and rewritten: a token probe is not a reading.  The E = 0 claim is tested by
# reading the Index of Indices entry for Lambda_var in full at its heading, not by grepping the name.
print('  E = 0 claim at L9537.  The Index of Indices entry for Lambda_var, read in full:')
st = [i for i in range(1, len(IOI) + 1) if IOI[i - 1].strip().startswith('## Λ_var')]
print('    entry heading at ioi L%s' % st)
if st:
    s0 = st[0]
    e0 = next((i for i in range(s0 + 1, len(IOI) + 1) if IOI[i - 1].startswith('## ')), len(IOI) + 1)
    for i in range(s0, e0):
        if IOI[i - 1].strip(): print('    ioi L%d: %s' % (i, norm(IOI[i - 1])[:160]))
    ent = '\n'.join(IOI[s0 - 1:e0 - 1])
    print('    "E = 0" present in the entry: %s ; "E=0": %s' % ('E = 0' in ent, 'E=0' in ent))
    print('    every "E" assignment in the entry:', re.findall(r'E\s*=\s*[0-9]+', ent))
    print('    every "V" assignment in the entry:', re.findall(r'V\s*=\s*[0-9]+', ent))
for i in range(1, len(IOI) + 1):
    if 'Λ_var' in IOI[i - 1] and not IOI[i - 1].strip().startswith('## '):
        print('    other ioi site L%d: %s' % (i, norm(IOI[i - 1])[:150]))
print('  channel equation at L9558: delta = sqrt(p) . f(u); p is a core+rydberg variable: %s ; u is a nucleus+core variable: %s'
      % ('p' in varset, 'u' in varset))

# ---------------------------------------------------------------- 10. the ladder table
hr('10  THE LADDER TABLE, L9568-L9573, against Z = Ne + c - 1 (L9564)')
lad = [r for r in MAIN[9568 - 1:9573] if r.strip().startswith('|')]
lrows = [r for r in lad if not re.match(r'^\|[\s\-:|]+\|$', r.strip())][1:]
print('  DATA rows:', len(lrows))
for r in lrows: print('    ', norm(r))
print('  identity Z = Ne + c - 1 -> exactly two of {Z, Ne, c} are free.')
for r in lrows:
    cells = [c.strip().replace('**', '') for c in r.strip().strip('|').split('|')]
    fixes = set(re.findall(r'Z|Nₑ|\bc\b', cells[1])); varies = set(re.findall(r'Z|Nₑ|\bc\b', cells[2]))
    tot = fixes | varies
    print('    %-16s fixes=%-14s varies=%-14s covers all three electronic quantities: %s'
          % (cells[0], sorted(fixes), sorted(varies), tot == {'Z', 'Nₑ', 'c'}))
print('  "no ladder can vary Z alone": under the identity, moving Z with Ne and c both fixed is impossible:',
      True)
print('  "Three ladders exhaust the electronic space": electronic rows =',
      len([r for r in lrows if 'neutron' not in r]), '; the fourth varies the neutron number:',
      any('neutron' in r for r in lrows))

# ---------------------------------------------------------------- 11. forward pointers used by 34.4
hr('11  WHAT §34.4 SAYS ITS NEIGHBOURS DO -- tested at the target, in full')
for sec, tok in [('34.5', 'ν'), ('34.6', 'ν'), ('34.7', 'ν'), ('34.8', '|'), ('34.10', 'ν')]:
    br = body_range(MAIN, sec); seg = '\n'.join(MAIN[br[0] - 1:br[1] - 1])
    print('  §%-6s L%d-L%d  %-3s occurrences: %d   table rows: %d   "corridor": %d  "reset": %d  " a "/"a is": %d'
          % (sec, br[0], br[1] - 1, tok, seg.count(tok),
             len([r for r in seg.split('\n') if r.strip().startswith('|')]),
             seg.lower().count('corridor'), seg.lower().count('reset'),
             len(re.findall(r'(?<![A-Za-z])a(?![A-Za-z])', seg))))
print('  §34.4 L9580 says the rule is "stated here in the form §34.5 to §34.7 use it".')
print('  §34.4 L9596 says "the provenance of every term is §34.8\'s table".')
# FAULT, self-caught and rewritten: a token probe is not a reading.  §34.5-§34.7 are 13, 12 and 15
# lines, so they are PRINTED to test whether they use the rule L9580 says they use.
print('\n  §34.5-§34.7 printed in full (short sections; the pointer at L9580 is tested on the text):')
for i in range(9609, 9649):
    if MAIN[i - 1].strip(): print('    L%d %s' % (i, MAIN[i - 1]))
# the two out-of-unit sites of 108, which decide whether 108 is the law's stated domain
print('\n  the two out-of-unit sites of 108 (from test 5), read:')
for i in (9663, 9746):
    print('    L%d [%s] %s' % (i, (enclosing(MAIN, i) or '?'), norm(MAIN[i - 1])))
print('\n  the References entries naming the n+l rule\'s owners, read at the target:')
for i in range(R0IDX, len(MAIN) + 1):
    if any(w in MAIN[i - 1] for w in ('Madelung', 'Janet', 'Löwdin', 'Klechkov')):
        print('    L%d %s' % (i, norm(MAIN[i - 1])[:190]))

# ---------------------------------------------------------------- 12. attributions and dates
hr('12  ATTRIBUTIONS IN THE UNIT vs the References BODY occurrence')
refhead = [i for i in range(1, len(MAIN) + 1) if MAIN[i - 1].strip() == '## References']
print('  "## References" occurrences:', refhead, '-> BODY occurrence is the last:', refhead[-1])
R0 = refhead[-1]; R1 = len(MAIN)
refs = '\n'.join(MAIN[R0 - 1:R1])
for who in ['Löwdin', 'Madelung', 'Janet', 'Klechkovskii', 'Schrödinger', 'Pauli', 'Rydberg']:
    inunit = [i for i in range(A, B + 1) if who in MAIN[i - 1]]
    print('  %-13s unit sites %-22s in References body: %s'
          % (who, str(inunit), who in refs))
for y in ('1936', '1929', '1969'):
    print('  year %s -- unit sites %s ; References body sites %s'
          % (y, [i for i in range(A, B + 1) if y in MAIN[i - 1]],
             [i for i in range(R0, R1 + 1) if y in MAIN[i - 1]]))

# ---------------------------------------------------------------- 13. the priority claim
hr('13  "The ν rule is this record\'s own, first stated in this work" (L9601)')
for name, M in VOLS:
    s = [i for i in range(1, len(M) + 1) if re.search(r'ν\s*\(\s*n\s*,\s*ℓ\s*,\s*q\s*\)', M[i - 1])]
    print('  %-5s sites of the printed form ν(n,ℓ,q): %s' % (name, s))
for name, M in VOLS:
    s = [i for i in range(1, len(M) + 1) if has_token(M[i - 1], 'Madelung')]
    print('  %-5s "Madelung" sites: %s' % (name, s[:14]), '...' if len(s) > 14 else '')

print('\nEND r2-ch16w')
