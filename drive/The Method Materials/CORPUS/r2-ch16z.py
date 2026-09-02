#!/usr/bin/env python3
# r2-ch16z -- PROSE batch for the chat-127 section read: main L9609-L9715 (34.5-34.10).
# Reads MEMBERS and the Prints & Proofs original only.  Deterministic; prints no wall-clock time.
import os, re, importlib.util, difflib
from collections import Counter

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
# owed to r2lib (DEFERRED): htitle -- strip the section number from BOTH sides of a PP comparison (chat 126).
def htitle(t): return re.sub(r'^#+\s*(?:\d+(?:\.\d+)*\.?\s*)?', '', t.strip()).strip()
# owed to r2lib (DEFERRED): joins -- a wrapped sentence is read on the normalised JOIN (chat 125/126).
def joins(M, a, b): return [(i, norm(M[i - 1] + ' ' + M[i])) for i in range(a, b)]

MAIN = rd('The_Method_1_6-2.md'); REG = rd('The_Method_1_6___The_Register-2.md')
MC = rd('The_Method_1_6___Mathematical_Compendium-2.md'); PC = rd('The_Method_1_6___The_Physics_Compendium-2.md')
IOI = rd('The_Method_1_6___The_Index_of_Indices-2.md'); SC = rd('The_Method_1_6___Spectra_Compendium-2.md')
VOLS = [('main', MAIN), ('reg', REG), ('mc', MC), ('pc', PC), ('ioi', IOI), ('sc', SC)]
P = open(PP, encoding='utf-8').read().split('\n')
A, B = 9609, 9715
def sites(M, pat, flags=0): return [i for i in range(1, len(M) + 1) if re.search(pat, M[i - 1], flags)]
def allsites(pat, flags=0): return ' | '.join('%s %s' % (n, sites(M, pat, flags)[:10]) for n, M in VOLS)

# ---------------------------------------------------------------- 1. Ruling 45
hr('1  RULING 45 -- build or editorial-process remarks (chat-115 discriminator: the WORK\'S OWN MAKING)')
R45 = ['this record', 'this work', 'the session', 'draft', 'earlier version', 'we ran', 'the build', 'rewritten',
       'the record', 'chat', 'audit', 'instrument', 'as printed', 'stated here', 'was reported', 'had been recorded',
       'was mine', 'the book exists for', 'this chapter', 'replayed']
for i in range(A, B + 1):
    for t in R45:
        if t.lower() in MAIN[i - 1].lower():
            print('  L%d  [%s]  %s' % (i, t, norm(MAIN[i - 1])[:130])); break
print('  §34.10 is headed "How the method delivered it" and opens "This is the part of the chapter the book exists for":')
print('  the whole section narrates the work\'s own making by design; its sites are candidates under the discriminator,')
print('  not members, except where the sentence is ABOUT the session rather than about the object (L9681, L9687, L9698, L9700).')

# ---------------------------------------------------------------- 2. Ruling 46
hr('2  RULING 46 -- script names, build numbers, internal file references (CASE-SENSITIVE)')
R46 = [r'\b[a-z_0-9]+\.py\b', r'\bBUILD\d+\b', r'\bW-\d+\b', r'\bDEF-\d+\b', r'\bHANDOFF-\d+\b', r'\.md\b', r'\.tsv\b', r'\bmembers/']
hits = 0
for i in range(A, B + 1):
    for pat in R46:
        for m in re.finditer(pat, MAIN[i - 1]):
            print('  L%d  %s  ::  %s' % (i, m.group(0), norm(MAIN[i - 1])[:120])); hits += 1
print('  Ruling 46 sites in the unit: %d   (register 1336 names domain_protocol.py; the unit says "the domain protocol")' % hits)
print('  backticked variable `a` in reader-facing prose (a code-font remark, docket 28): sites %s'
      % [i for i in range(A, B + 1) if '`a`' in MAIN[i - 1]])

# ---------------------------------------------------------------- 3. first person
hr('3  FIRST PERSON -- guarded for the Roman numeral in "He I"; "mine" ADDED (chat 126\'s probe lacked it)')
fp = 0
for i in range(A, B + 1):
    for m in re.finditer(r'(?<![A-Za-z])(I|my|mine|we|our|us|myself)(?![A-Za-z])', MAIN[i - 1]):
        ctx = MAIN[i - 1][max(0, m.start() - 30):m.end() + 20]
        roman = bool(re.search(r'\b[A-Z][a-z]{0,2} (I|II|III|IV|V|VI|VII|VIII|IX|X)\b', ctx))
        print('  L%d  %-6s roman-numeral context: %s  ::  %s' % (i, m.group(0), roman, norm(ctx))); fp += (not roman)
print('  first-person sites in the unit: %d' % fp)
print('  "mine" across the six volumes (word-bounded, case-sensitive): %s' % allsites(r'(?<![A-Za-z])mine(?![A-Za-z])'))
print('  "was mine" / "were mine" in main: %s' % sites(MAIN, r'\b(was|were) mine\b'))

# ---------------------------------------------------------------- 4. unmarked sub-headings
hr('4  UNMARKED SUB-HEADINGS -- blank line above required')
n = 0
for i in range(A + 1, B + 1):
    t = MAIN[i - 1].strip()
    if not t or t.startswith('#') or t.startswith('|') or t.startswith('>'): continue
    if MAIN[i - 2].strip() != '': continue
    if re.match(r'^(\*\*[^*]{3,60}\*\*|\*[^*]{3,60}\*)$', t): print('  L%d  %s' % (i, t)); n += 1
print('  unmarked sub-headings in the unit: %d hits, 0 headings (L9659 is a bold one-sentence paragraph closing the table; L9675 an italic one-line epigraph to §34.10)' % n)

# ---------------------------------------------------------------- 5. duplicated lines
hr('5  DUPLICATED-SECTION SWEEP (docket 27) -- long unit lines recurring elsewhere in the volume')
long = [(i, norm(MAIN[i - 1])) for i in range(A, B + 1) if len(norm(MAIN[i - 1])) >= 60]
rec = 0
for i, t in long:
    els = [j for j in range(1, len(MAIN) + 1) if not (A <= j <= B) and norm(MAIN[j - 1]) == t]
    if els: print('  L%d recurs at %s :: %s' % (i, els, t[:90])); rec += 1
print('  %d of %d long lines recur outside the unit' % (rec, len(long)))

# ---------------------------------------------------------------- 6. Prints & Proofs
hr('6  PRINTS & PROOFS -- titles both sides stripped; then the WHOLE unit diffed against PP at the offset')
offs = []
for sec in ['34.5', '34.6', '34.7', '34.8', '34.9', '34.10', '35']:
    ln = heading_line(MAIN, sec); title = htitle(MAIN[ln - 1])
    hp = [i for i in range(1, len(P) + 1) if P[i - 1].startswith('#') and htitle(P[i - 1]) == title]
    print('  §%-6s L%-6d "%s"  -> PP %s  offset %s' % (sec, ln, title, hp, [h - ln for h in hp])); offs += [h - ln for h in hp]
off = Counter(offs).most_common(1)[0][0]
print('  modal offset %d ; PP numbers its ### headings? %s' % (off, [P[h - 1][:40] for h in [heading_line(MAIN, '34.5') + off]]))
mseg = [norm(x) for x in MAIN[A - 1:B]]; pseg = [norm(x) for x in P[A - 1 + off:B + off]]
d = [l for l in difflib.unified_diff(pseg, mseg, fromfile='PP', tofile='volume', lineterm='', n=0) if not l.startswith(('---', '+++', '@@'))]
print('  aligned diff of the unit (main L%d-L%d) against PP P%d-P%d: %d differing lines' % (A, B, A + off, B + off, len(d)))
for l in d: print('   ', l[:160])
print('  -> every figure of the unit tested above is therefore %s' % ('present in Prints & Proofs unchanged: AUTHORED, not produced' if not d else 'to be read against the diff above'))

# ---------------------------------------------------------------- 7. count words
hr('7  COUNT WORDS -- each against its own body, its data rows, its numeral span and the Register entry that restates it')
print('  L9624 "resets eighteen times" / L9625-L9626 "(8) ... (6) ... (4)": 8+6+4 = %d; returns listed: %s -> %d'
      % (8 + 6 + 4, re.findall(r'\b[A-Z][a-z] after [A-Z][a-z]\b', norm(MAIN[9625] + ' ' + MAIN[9626])), len(re.findall(r'\b[A-Z][a-z] after [A-Z][a-z]\b', norm(MAIN[9625] + ' ' + MAIN[9626])))))
print('  L9641 "1.028 at p across four subshells ... 1.785 at d across two": register 1337 prints p at 3p 4p 5p 6p = 4, d at 4d 5d = 2')
print('  L9646 "1.120, 1.049, 1.022, 1.002 at n = 3, 4, 5, 6": numerals %d, n-values %d; ioi L1759 p row %s'
      % (len(re.findall(r'\d\.\d{3}', MAIN[9645])), 4, re.findall(r'\d\.\d{3}', IOI[1758])))
tbl = [i for i in range(9651, 9658) if MAIN[i - 1].startswith('|')]
print('  §34.8 table rows L%d-L%d: %d pipe rows = header + rule + %d DATA rows (FAULT 4 self-caught: a substring test on "term" had dropped the centrifugal-term row)'
      % (tbl[0], tbl[-1], len(tbl), len(tbl) - 2))
print('  L9685 "The domain protocol blocked four fits" -- fits named in L9685-L9690: %s'
      % re.findall(r'blocks the ℓ-spread[^,]*|the amplitude Gaussian[^,]*|six occupancy slopes[^—]*', norm(' '.join(MAIN[9684:9690]))))
rep = re.search(r'Replayed against today:(.*?)\*', REG[5016]).group(1)
blocked = re.findall(r'([^;.]*?)\s+BLOCKED', rep); passed = re.findall(r'([^.]*?)\s+both PASS', rep)
print('    register 1336 replay sentence: "%s"' % norm(rep)[:230])
print('    objects BLOCKED: %d %s ; objects PASS: %d (one "both PASS" over two named objects)  (FAULT 5 self-caught: the token PASS occurs once)'
      % (len(blocked), [norm(b)[:40] for b in blocked], 2 if passed else 0))
print('    register 1355 headline: "%s" -- a fourth blocked fit, named nowhere in the unit' % norm(REG[5092])[:90])
print('  L9692 "Λ_chem dissolved two residuals": named -> 1.029 factor, missing f test = 2; register 1337 "Not derived": %s'
      % re.findall(r'a common factor of 1\.029|no f test', REG[5020]))
print('  L9698 "Seven of eight rules give 106/106, and random interior points on 200 of 200 seeds": register 1331 L4997 -> %s'
      % re.findall(r'seven give 106/106|200 of 200 seeds|74/106', REG[4996]))
print('  L9702-L9705 "four separate times ... fifth and sixth ... One object, six appearances": 4 + 2 = 6;')
print('    register 1340 L5033 keeps ℓ(ℓ+1) [gate, collapse, barrier, Seaton, t(ℓ)] and 2ℓ+1 [1/(2ℓ+1), h₀√(2ℓ+1)] as TWO objects: %s'
      % re.findall(r'1/\(2ℓ\+1\)[^,]*|h₀√\(2ℓ\+1\)[^,]*|ℓ\(ℓ\+1\) a new discovery[^,]*', REG[5032]))
print('  L9663 "106 elements, Z = 3 to 108": 108 − 3 + 1 = %d' % (108 - 3 + 1))
print('  L9629 "104 of 106": other sites %s' % allsites(r'104 of 106'))

# ---------------------------------------------------------------- 8. false universals and superlatives
hr('8  FALSE-UNIVERSAL AND SUPERLATIVE SWEEP (docket 19) -- each with the entry that tests it')
FU = [('All 106 non-empty', 'R1445 "survives untouched"; R1463: 106 SEPARATE one-dimensional results, the table infeasible'),
      ('No measurement enters', 'R1309 "No spectroscopy enters: only Pauli, the node count, and the observed ground configurations"'),
      ('never resets mid-subshell', 'R1333; count itself rule-dependent (R1402)'),
      ('always among them and never uniquely determined', 'R1332; R1448 calls a self-consistency test of this shape vacuous'),
      ('No parameter is fitted', 'R1350 WARNING: qualified by R1445 -- "the 99 of 106 was FITTED"'),
      ('Exceptionless on 106 elements', 'R1350 WARNING: "holds only in that fitted sense"; R1437: 99 of 106; R1445: 90 held out'),
      ('including every aufbau anomaly', 'R1437 misses Mn Tc Ce Gd Pa Cm Rf'),
      ('At any f opening p = n−ℓ−1 = 0', '5f: p = 1 (r2-ch16y §5)'),
      ('no analysis or statistics language', 'R1318 "no analysis language"; R1327 "no statistics language"'),
      ('cannot be fitted and needs no fitting', 'R1318'),
      ('the only place ℓ enters', 'R1337 "the ONLY place ℓ enters the radial Schrödinger equation"'),
      ('the ℓ-spread on six hand-picked species', 'R1336 "law 2 on six species"'),
      ('The corridor is forced; the trajectory was mine', 'R1331; R1402 "a property of one trajectory"')]
for t, note in FU:
    s = [i for i in range(A, B + 1) if t.lower() in norm(MAIN[i - 1] + ' ' + (MAIN[i] if i < len(MAIN) else '')).lower()]
    print('  %-52s unit sites %-14s %s' % ('"' + t + '"', s, note))

# ---------------------------------------------------------------- 9. pointers and named objects, resolved at their targets
hr('9  POINTERS AND NAMED OBJECTS -- resolved under body_range AND section_span, target read')
print('  § pointers in the unit: %s' % [(i, m.group(0)) for i in range(A, B + 1) for m in re.finditer(r'§\d+(?!\d)(?!\.\d)|§\d+\.\d+(?:\.\d+)*', MAIN[i - 1])])
print('  chapter pointers in the unit: %s' % [(i, m.group(0)) for i in range(A, B + 1) for m in re.finditer(r'Chapter \d+', MAIN[i - 1])])
h36 = heading_line(MAIN, '36'); br36 = body_range(MAIN, '36'); ss36 = section_span(MAIN, '36')
print('  "Chapter 36 takes this up" (L9712): ## 36. at L%s "%s"; body_range %s, section_span %s -> %s'
      % (h36, htitle(MAIN[h36 - 1]), br36, ss36, 'coincide' if br36 == ss36 else 'differ (chapter head carries subsections; resolver semantics)'))
print('    "pair" sites inside Chapter 36 (section_span): %s' % [i for i in range(ss36[0], ss36[1]) if has_token(MAIN[i - 1], 'pair') or has_token(MAIN[i - 1], 'pairs')][:12])
print('    "three-body"/"three bodies" sites in ch.36: %s' % [i for i in range(ss36[0], ss36[1]) if re.search(r'three[- ]bod', MAIN[i - 1])][:10])
for name, pat in [('Λ_phys', r'## Λ_phys'), ('Λ_chem', r'## Λ_chem'), ('Λ_t', r'## Λ_t\b')]:
    print('  %-8s Index of Indices entry heading: ioi %s' % (name, sites(IOI, pat)))
print('  "the cypher" -> §33 "%s" at L%d; "the domain protocol" main sites %s (§33 L9486 = %s)'
      % (htitle(MAIN[heading_line(MAIN, '33') - 1]), heading_line(MAIN, '33'), sites(MAIN, r'domain protocol'), enclosing(MAIN, 9486)))
print('  L9702-L9703 "recorded four separate times — as the gate, the collapse switch, the barrier and Seaton\'s ratio":')
print('    literal phrases in main: "Seaton\'s ratio" %s ; "collapse switch" %s ; "the barrier" %s  (a literal phrase is NOT a test)'
      % (sites(MAIN, r"Seaton's ratio")[:8], sites(MAIN, r'collapse switch')[:8], sites(MAIN, r'\bthe barrier\b')[:8]))
for tok in ['Seaton', 'collapse', 'centrifugal', 'barrier', 'gate']:
    print('    %-12s word-bounded sites: %s' % (tok, ' | '.join('%s %d' % (vn, len([i for i in range(1, len(M) + 1) if has_token(M[i - 1], tok)])) for vn, M in VOLS)))
print('    ℓ(ℓ+1) itself: %s' % ' | '.join('%s %d' % (vn, len(sites(M, r'ℓ\(ℓ\+1\)'))) for vn, M in VOLS))
print('  "the one microscope" (L9702): register 1340 L5033 "%s"' % norm(REG[5032])[:110])
print('  Register citations in the unit: %s' % ([(i, m.group(0)) for i in range(A, B + 1) for m in re.finditer(r'[Rr]egisters? \d+', MAIN[i - 1])] or 'NONE'))
print('  restatements of the unit\'s figures elsewhere in the main volume: 104 of 106 %s ; "the corridor" appendix rows %s'
      % (sites(MAIN, r'104 of 106'), [i for i in range(10845, 10860) if 'corridor' in MAIN[i - 1] or '104 of 106' in MAIN[i - 1]]))
for i in (9731, 9732, 10850, 10851, 10856): print('    L%d %s' % (i, norm(MAIN[i - 1])[:120]))

# ---------------------------------------------------------------- 10. attributions
hr('10  ATTRIBUTIONS -- against the ## References BODY (L11503-L11855) and R.7, both directions')
refbody = MAIN[11502:11855]
for who in ['Pauli', 'Schrödinger', 'Seaton', 'Löwdin', 'Madelung', 'Gaussian']:
    unit = [i for i in range(A, B + 1) if who in MAIN[i - 1]]
    ref = [11503 + k for k, l in enumerate(refbody) if who in l]
    print('  %-12s unit sites %-22s References-body sites %s' % (who, unit, ref[:6]))
print('  R.7 heading: %s' % sites(MAIN, r'^#{2,4} R\.7\b'))

# ---------------------------------------------------------------- 11. element names of the unit, notation-tolerant
hr('11  ELEMENTS NAMED IN THE UNIT (docket 20, notation-tolerant) across six volumes: symbol | name')
for sym, name in [('Tc', 'technetium'), ('Mo', 'molybdenum'), ('Tb', 'terbium'), ('Gd', 'gadolinium'), ('Bk', 'berkelium'), ('Cm', 'curium'), ('Hg', 'mercury'), ('Au', 'gold')]:
    row = []
    for vn, M in VOLS:
        y = len([i for i in range(1, len(M) + 1) if re.search(r'(?<![A-Za-z])' + sym + r'(?![a-z])', M[i - 1])])
        s = len([i for i in range(1, len(M) + 1) if has_token(M[i - 1], name)])
        row.append('%s %d|%d' % (vn, y, s))
    print('  %-2s %-11s %s' % (sym, name, '  '.join(row)))

# ---------------------------------------------------------------- 12. wrapped sentences
hr('12  WRAPPED SENTENCES read on the normalised JOIN')
for a_, b_ in [(9616, 9618), (9619, 9621), (9624, 9628), (9629, 9633), (9641, 9644), (9645, 9648), (9663, 9665), (9666, 9670), (9685, 9691), (9697, 9701), (9702, 9707), (9710, 9713)]:
    print('  L%d-L%d  %s' % (a_, b_ - 1, norm(' '.join(MAIN[a_ - 1:b_ - 1]))[:170]))

# ---------------------------------------------------------------- 13. numeral sites
hr('13  NUMERAL SITES of the unit across six volumes (thousands separator and word form aware)')
for num in ['0.5773503', '1.2168450', '1.3938270', '1.028', '1.785', '0.19%', '1.120', '1.049', '1.022', '1.002', '0.2%', '1.029', '106/106', '200 of 200', '104 of 106', 'eighteen']:
    print('  %-10s %s' % (num, allsites(re.escape(num) + r'(?!\d)')))

# ---------------------------------------------------------------- 14. census rows
hr('14  DEFECT-CENSUS rows in range (member main AND all, line %d-%d)' % (A, B))
C = rd('DEFECT-CENSUS.tsv'); hdr = C[0].split('\t'); print('  columns:', hdr)
rows = [r.split('\t') for r in C[1:] if r.strip()]
mi, li = hdr.index('member'), hdr.index('line')
inr = [r for r in rows if r[mi] in ('main', 'all') and r[li].isdigit() and A <= int(r[li]) <= B]
print('  rows in range: %d' % len(inr))
for r in inr: print('   ', '\t'.join(r)[:200])

print('\nEND r2-ch16z')
