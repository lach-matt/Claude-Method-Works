#!/usr/bin/env python3
# r2-ch16x -- PROSE batch for the chat-126 section read: main L9494-L9608
# (ch.34 head + epigraph, 34.1-34.4).  Reads MEMBERS and the Prints & Proofs original only.
# Deterministic; prints no wall-clock time.
import os, re, importlib.util

H = '/home/claude/members'
PP = '/home/claude/PP_The_Method_1_6.md'
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

# owed to r2lib (DEFERRED): joins -- a sentence that wraps is read on the normalised JOIN of its
# lines, never one line.  Chat 125's §20.2 parse returned three names of six from one line.
def joins(M, a, b):
    out = []
    for i in range(a, b):
        out.append((i, norm(M[i - 1] + ' ' + M[i])))
    return out

MAIN = rd('The_Method_1_6-2.md')
REG  = rd('The_Method_1_6___The_Register-2.md')
MC   = rd('The_Method_1_6___Mathematical_Compendium-2.md')
PC   = rd('The_Method_1_6___The_Physics_Compendium-2.md')
IOI  = rd('The_Method_1_6___The_Index_of_Indices-2.md')
SC   = rd('The_Method_1_6___Spectra_Compendium-2.md')
VOLS = [('main', MAIN), ('reg', REG), ('mc', MC), ('pc', PC), ('ioi', IOI), ('sc', SC)]
P    = open(PP, encoding='utf-8').read().split('\n')
A, B = 9494, 9608
U = MAIN[A - 1:B]
UT = '\n'.join(U)

# ---------------------------------------------------------------- 1. Ruling 45
hr('1  RULING 45 -- build or editorial-process remarks in a reader-facing volume')
R45 = ['this record', 'this work', 'the session', 'draft', 'earlier version', 'we ran', 'the build',
       'rewritten', 'the record', 'chat', 'audit', 'instrument', 'as printed', 'stated here',
       'what follows here', 'in this chapter', 'the reading that found']
for i in range(A, B + 1):
    for t in R45:
        if t.lower() in MAIN[i - 1].lower():
            print('  L%d  [%s]  %s' % (i, t, norm(MAIN[i - 1])))
            break
print('\n  chat-115 discriminator: a remark about the WORK\'S OWN MAKING is a member;')
print('  a remark locating a statement inside the finished text is not.')

# ---------------------------------------------------------------- 2. Ruling 46
hr('2  RULING 46 -- script names, build numbers, internal file references (CASE-SENSITIVE)')
R46 = [r'\b[a-z_0-9]+\.py\b', r'\bBUILD\d+\b', r'\bW-\d+\b', r'\bDEF-\d+\b', r'\bHANDOFF-\d+\b',
       r'\.md\b', r'\.tsv\b', r'\bmembers/', r'\bgate\.py\b']
hits = 0
for i in range(A, B + 1):
    for pat in R46:
        for m in re.finditer(pat, MAIN[i - 1]):
            print('  L%d  %s  ::  %s' % (i, m.group(0), norm(MAIN[i - 1])[:120])); hits += 1
print('  Ruling 46 sites in the unit: %d' % hits)

# ---------------------------------------------------------------- 3. first person
hr('3  FIRST PERSON -- guarded: \\b(I|my|we|our)\\b matches the Roman numeral in "He I"')
fp = 0
for i in range(A, B + 1):
    for m in re.finditer(r'(?<![A-Za-z])(I|my|we|our|us)(?![A-Za-z])', MAIN[i - 1]):
        ctx = MAIN[i - 1][max(0, m.start() - 12):m.end() + 12]
        roman = re.search(r'\b[A-Z][a-z]{0,2} (I|II|III|IV|V|VI|VII|VIII|IX|X)\b', ctx)
        print('  L%d  %-4s roman-numeral context: %s  ::  %s'
              % (i, m.group(0), bool(roman), norm(ctx))); fp += 1
print('  first-person sites in the unit: %d' % fp)

# ---------------------------------------------------------------- 4. unmarked sub-headings
hr('4  UNMARKED SUB-HEADINGS -- must require a BLANK LINE ABOVE (else italic wrap tails fire)')
n = 0
for i in range(A + 1, B + 1):
    t = MAIN[i - 1].strip()
    if not t or t.startswith('#') or t.startswith('|') or t.startswith('>'): continue
    if MAIN[i - 2].strip() != '': continue                       # blank line above required
    if re.match(r'^(\*\*[^*]{3,60}\*\*|\*[^*]{3,60}\*)$', t):
        print('  L%d  %s' % (i, t)); n += 1
print('  unmarked sub-headings in the unit: %d' % n)

# ---------------------------------------------------------------- 5. duplicated lines
hr('5  DUPLICATED-SECTION SWEEP (docket 27) -- long unit lines recurring elsewhere in the volume')
long = [(i, norm(MAIN[i - 1])) for i in range(A, B + 1) if len(norm(MAIN[i - 1])) >= 60]
rec = 0
for i, t in long:
    els = [j for j in range(1, len(MAIN) + 1) if not (A <= j <= B) and norm(MAIN[j - 1]) == t]
    if els: print('  L%d recurs at %s :: %s' % (i, els, t[:90])); rec += 1
print('  %d of %d long lines recur outside the unit' % (rec, len(long)))

# ---------------------------------------------------------------- 6. Prints & Proofs
hr('6  PRINTS & PROOFS -- is chapter 34 in the original at all?  Titles, not whole lines.')
print('  PP lines: %d ; volume lines: %d' % (len(P), len(MAIN)))
for probe in ['Löwdin challenge', 'The problem, and the wrong target',
              'The three bodies, and the pair that has no variable',
              'What the ladders can and cannot reach', 'The rule', 'Klechkovskii',
              'Seventeen of nineteen', '108 neutrals']:
    hp = [i for i in range(1, len(P) + 1) if probe in P[i - 1]]
    hm = [i for i in range(1, len(MAIN) + 1) if probe in MAIN[i - 1]]
    off = [(a - b) for a in hp for b in hm] if hp and hm else []
    print('  %-52s PP %-14s main %-22s offset %s' % ('"' + probe + '"', hp, hm, sorted(set(off))[:4]))
# FAULT, self-caught and rewritten: PP numbers the CHAPTER head ("## 34. The Löwdin challenge")
# and does NOT number the section heads ("### The problem, and the wrong target").  Stripping the
# number from the volume side only reported the chapter head absent from PP.  Strip BOTH sides.
def htitle(t): return re.sub(r'^#+\s*(?:\d+(?:\.\d+)*\.?\s*)?', '', t.strip()).strip()
print('\n  heading TITLES of the unit against PP (numbering is a production layer -- compare titles):')
for sec in ['34', '34.1', '34.2', '34.3', '34.4']:
    ln = heading_line(MAIN, sec)
    title = htitle(MAIN[ln - 1])
    hp = [i for i in range(1, len(P) + 1) if P[i - 1].startswith('#') and htitle(P[i - 1]) == title]
    print('  §%-6s L%-6d "%s"  -> PP %s  offset %s'
          % (sec, ln, title, hp, [h - ln for h in hp]))
print('\n  THE OFFSET SHIFT: -94 at L9511, -96 at L9532 -- the volume gained two lines in §34.1.')
print('  aligned diff of main L9512-L9531 against PP L9418-L9435:')
mseg = [norm(x) for x in MAIN[9511:9531]]
pseg = [norm(x) for x in P[9417:9435]]
import difflib
for ln in difflib.unified_diff(pseg, mseg, fromfile='PP', tofile='volume', lineterm='', n=1):
    print('   ', ln[:150])

# ---------------------------------------------------------------- 7. count words
hr('7  COUNT WORDS -- each against its own body, its data rows and its numeral span')
print('  L9523 "Both Pauli quantities appear." -- distinct quantities named in L9523-L9525:')
seg = norm(' '.join(MAIN[9522:9525]))
print('    ', seg)
quants = set(re.findall(r'2\(2ℓ\+1\)', seg)) | set(re.findall(r'\bq/2\(2ℓ\+1\)\b', seg))
print('    distinct Pauli quantities printed:', sorted(quants), '-> %d' % len(quants))
print('    the paragraph names ONE quantity, 2(2ℓ+1), in TWO roles (admissibility; radicand).')
print('    L9594 restates it as "the capacity 2(2ℓ+1), twice" -- one quantity, twice.')
print('\n  L9534 "three bodies" vs the §34.2 table: 3 singleton rows + 3 pair rows = 6 DATA rows.')
print('  L9575 "Three ladders exhaust the electronic space" vs 4 DATA rows, the fourth isotopic.')
print('  L9564 "only two of the three electronic quantities are independent" vs Z = Nₑ + c − 1.')
print('  L9559 "no third factor because the index holds no third pair":')
print('    the §34.2 table PRINTS a third pair row (nucleus + rydberg) carrying no variable;')
print('    "holds no third pair" is exact only under "holds" = "carries a variable in".')

# ---------------------------------------------------------------- 8. false universals
hr('8  FALSE-UNIVERSAL AND SUPERLATIVE SWEEP (docket 19)')
FU = ['has never been traced', 'No parameter is fitted', 'makes every one worse',
      'every variable of the problem', 'No variable in the index', 'nothing measured',
      'the only route to the nucleus', 'exhaust the electronic space', 'No variable']
for t in FU:
    s = [i for i in range(A, B + 1) if t.lower() in MAIN[i - 1].lower()]
    if s: print('  %-34s unit sites %s' % ('"' + t + '"', s))
print('\n  "has never been traced" (L9576) -- corroboration sweep on "isotopic" across six volumes:')
for name, M in VOLS:
    s = [i for i in range(1, len(M) + 1) if has_token(M[i - 1], 'isotopic')]
    print('    %-5s %s' % (name, s[:12]))

# ---------------------------------------------------------------- 9. §34.8 tested at its target
hr('9  L9596 "the provenance of every term is §34.8\'s table" -- tested at §34.8, printed')
br = body_range(MAIN, '34.8')
for i in range(br[0], br[1]):
    if MAIN[i - 1].strip(): print('  L%d %s' % (i, MAIN[i - 1]))
seg8 = '\n'.join(MAIN[br[0] - 1:br[1] - 1])
terms = {'n': r'(?<![A-Za-z])n(?![A-Za-z₀])', 'ℓ': 'ℓ', 'q': r'(?<![A-Za-z])q(?![A-Za-z])',
         'a': r'(?<![A-Za-z`])a(?![A-Za-z])', '2(2ℓ+1)': r'2\(2ℓ\+1\)', 'ν': 'ν'}
print('\n  terms of the rule ν(n,ℓ,q) = n − a·√( n − ℓ − 1 + q/2(2ℓ+1) ) against §34.8:')
for k, pat in terms.items():
    print('    term %-8s occurrences in §34.8: %d' % (k, len(re.findall(pat, seg8))))

# ---------------------------------------------------------------- 10. "the paper"
hr('10  "the paper" / "companion paper" -- absorbed-companion reference class')
for name, M in VOLS:
    s = [i for i in range(1, len(M) + 1) if re.search(r'\bcompanion paper\b|\bthe paper\b', M[i - 1])]
    print('  %-5s %s' % (name, s[:16]))
for i in [j for j in range(A, B + 1) if re.search(r'\bthe paper\b', MAIN[j - 1])]:
    print('  unit site L%d: %s' % (i, norm(MAIN[i - 1])))

# ---------------------------------------------------------------- 11. species / element sweep
hr('11  ELEMENT NAMES OF THE UNIT (docket 20, notation-tolerant) across six volumes')
for el, sym in [('lanthanum', 'La'), ('cerium', 'Ce'), ('actinium', 'Ac'), ('protactinium', 'Pa')]:
    row = []
    for name, M in VOLS:
        s = [i for i in range(1, len(M) + 1) if has_token(M[i - 1], el)]
        y = [i for i in range(1, len(M) + 1) if re.search(r'(?<![A-Za-z])' + sym + r'(?![a-z])', M[i - 1])]
        row.append('%s name %d sym %d' % (name, len(s), len(y)))
    print('  %-13s %s' % (el, ' | '.join(row)))

# ---------------------------------------------------------------- 12. wrapped sentences
hr('12  WRAPPED SENTENCES read on the normalised JOIN, not the line')
for i, t in joins(MAIN, 9509, 9515):
    print('  L%d+%d  %s' % (i, i + 1, t[:150]))

# ---------------------------------------------------------------- 13. register citations
hr('13  REGISTER CITATIONS IN THE UNIT (lowercase "register NNN" grepped by hand rule)')
c = [(i, m.group(0)) for i in range(A, B + 1) for m in re.finditer(r'[Rr]egisters? \d+', MAIN[i - 1])]
print('  citations found:', c if c else 'NONE -- the unit cites the Register nowhere')
print('  Chapter-34 span L9494-L9715 register citations:',
      [(i, m.group(0)) for i in range(9494, 9716) for m in re.finditer(r'[Rr]egisters? \d+', MAIN[i - 1])])

print('\nEND r2-ch16x')
