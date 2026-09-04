#!/usr/bin/env python3
# r2-ch16t -- PROSE batch for the chat-124 section read: main L9307-L9392 (32.7).
# Reads MEMBERS and the Prints & Proofs original; never a BUILDnnn bundle path.
# r2-ch16t2.py — R3 (chat 153-R) — SUCCESSOR to r2-ch16t.py, re-anchored by tools/reanchor.py: every main-volume line the
# predecessor pinned as a literal is resolved by the text of the line it pointed at in the bundle its golden was
# banked against (35 anchors); nothing else changes. r2-ch16t.py is seated and never edited in place (chat 68).
# PROVED by tools/proveanchor.py when the line below says so; until then this file is a draft.
# PROVEANCHOR: 90+184 — reproduces r2-ch16t.out byte-exact on those bundles (G0c)

# --- re-anchoring helper (tools/reanchor.py): a main-volume line found by its own text, never by a number ---
def _L(t, d=0):
    import os as _o
    global _LM
    try: _LM
    except NameError: _LM = open(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)), 'The_Method_1_6-2.md'), encoding='utf-8').read().split('\n')
    h = [i for i, l in enumerate(_LM, 1) if l == t]
    assert len(h) == 1, ('re-anchor: line text is not unique or is absent', t[:60], h)
    return h[0] + d
import os, re, csv, importlib.util

H = '/home/claude/members'
PP_PATH = '/home/claude/PP_The_Method_1_6.md'
spec = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
from r2lib import heading_line, section_span, has_token, enclosing

def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
def hr(t): print('\n' + '=' * 96 + '\n' + t + '\n' + '=' * 96)
def norm(s): return re.sub(r'\s+', ' ', s.strip())
def demph(s): return s.replace('*', '').replace('_', '')

# owed to r2lib (DEFERRED): body_range, carried with provenance from r2-ch16m (chat 121).
def body_range(M, sec):
    s = heading_line(M, sec)
    if s is None: return None
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1].strip()): return (s, i)
    return (s, len(M) + 1)

MAIN = rd('The_Method_1_6-2.md')
REG  = rd('The_Method_1_6___The_Register-2.md')
MC   = rd('The_Method_1_6___Mathematical_Compendium-2.md')
PC   = rd('The_Method_1_6___The_Physics_Compendium-2.md')
IOI  = rd('The_Method_1_6___The_Index_of_Indices-2.md')
SC   = rd('The_Method_1_6___Spectra_Compendium-2.md')
VOLS = [('main', MAIN), ('reg', REG), ('mc', MC), ('pc', PC), ('ioi', IOI), ('sc', SC)]
PP = open(PP_PATH, encoding='utf-8').read().split('\n')
A, B = _L('### 32.7 On a verification that does not test its claim'), _L(' **That is where the word belongs.** Not on *V* = 4ν/3, which may sit in a 1922 German volume nobody cites. Not on E(X), which is a closure defect and says so. **On the shape of the thing** — a work built to be checked, that checked itself, failed twice, said so, and repaired both.', 2)
U = list(range(A, B))

def sweep(pat, vols=VOLS, flags=re.I, cap=12):
    out = {}
    for nm, M in vols:
        h = [i for i in range(1, len(M) + 1) if re.search(pat, M[i - 1], flags)]
        if h: out[nm] = h[:cap] + (['...'] if len(h) > cap else [])
    return out

# --------------------------------------------------------------------------- 1
hr('1  EVERY POINTER THE UNIT MAKES, RESOLVED UNDER body_range AND section_span, TO THE CLAIM')
for sec in ('24.2', '29.6', '32.3', '32.6'):
    br, ss = body_range(MAIN, sec), section_span(MAIN, sec)
    print(f'  §{sec:6s} body_range {br}  section_span {ss}  COINCIDE {br == ss}  heading '
          f'{norm(MAIN[heading_line(MAIN, sec)-1])[:56]!r}')
print('\n  L9356 cites §24.2 for "the four unreachable documents". Testing §24.2\'s OWN body:')
b242 = body_range(MAIN, '24.2'); s242 = section_span(MAIN, '24.2')
for span, tag in ((b242, 'body_range'), (s242, 'section_span')):
    txt = ' '.join(MAIN[span[0]-1:span[1]-1]).lower()
    print(f'   {tag:13s} {span}: ' + '  '.join(
        f'{w}={txt.count(w)}' for w in ('document', 'reach', 'unreachable', 'edlén', 'ritz', 'paschen', 'dunz')))
print('   -> and where the claim DOES live (§29.6 body):')
b296 = body_range(MAIN, '29.6')
txt = ' '.join(MAIN[b296[0]-1:b296[1]-1]).lower()
print('   §29.6 ' + '  '.join(f'{w}={txt.count(w)}' for w in ('document', 'reach', 'edlén', 'ritz', 'paschen', 'dunz')))
print(f'\n  "Part V" = {[i for i in range(1,len(MAIN)+1) if re.match(r"^# PART V ", MAIN[i-1])]}; '
      f'chapters inside it: {[norm(MAIN[i-1])[:24] for i in range(_L(' defect in the law index are one absence at two levels.** Register 548.', 2),_L('    do.', 2)) if re.match(r"^## \d+\.", MAIN[i-1])]}')
print(f'  Chapter 29 head: {norm(MAIN[_L(' Register 416.', 1)])[:60]!r}; "solution density" in Ch29: '
      f'{[i for i in range(_L(' This chapter does not claim novelty, and an earlier draft did.', -1),_L(" Chapter 15 recovers Λ's order from its own cells. This chapter asks what happens when the", -1)) if re.search("solution density", MAIN[i-1], re.I)]}')

# --------------------------------------------------------------------------- 2
hr('2  PRINCIPLE 8 -- READ THE CITED CRITERION IN FULL AT ITS TARGET, ALL SIX VOLUMES')
print(f'  sites of "Principle N" (any N), all volumes: {sweep(r"[Pp]rinciple\s+\d+", flags=0, cap=30)}')
print(f'  sites of an enumerated principles list ("Principle 1"/"Principles"): '
      f'{sweep(r"[Pp]rinciples\b", cap=20)}')
for i in (_L(' **And the second is the weaker word doing the honest work.** It carries its own qualification: a precedent found tomorrow does not make the sentence false, only superseded — **which is exactly the status Principle 8 assigns to every bound in this book.**'), _L(' **This is Principle 8 in its ordinary form: any true answer, good or bad, is a bound.** A verification that misses its target does not merely fail; it locates the target by missing it.')):
    print(f'   main L{i} {norm(MAIN[i-1])[:190]}')

# --------------------------------------------------------------------------- 3
hr('3  ATTRIBUTIONS AGAINST ## References BODY OCCURRENCE AND R.7 -- AND THE REVERSE')
occ = [i for i in range(1, len(MAIN) + 1) if re.match(r'^##\s+References\b', MAIN[i - 1].strip())]
body = [i for i in occ if i > 200]
REFS = (body[-1], len(MAIN) + 1)
print(f'  "## References" occurrences {occ}; BODY occurrence L{REFS[0]}; span {REFS}')
r7 = heading_line(MAIN, 'R.7')
r7span = None
for i in range(REFS[0], len(MAIN) + 1):
    if re.match(r'^#{1,4}\s*R\.7\b', MAIN[i - 1].strip()): r7span = i; break
print(f'  R.7 heading at L{r7span}: {norm(MAIN[r7span-1])[:70] if r7span else None!r}')
refs_txt = ' '.join(MAIN[REFS[0]-1:REFS[1]-1])
names = ['Sansonetti', 'Kramida', 'Martin', 'Kaufman', 'Sugar', 'Musgrove', 'Korobov', 'Hori',
         'Birkhoff', 'Dilworth', 'Sperner', 'Kuznetsov', 'Stahl', 'Wille']
for n in names:
    inref = len(re.findall(re.escape(n), refs_txt))
    inunit = [i for i in U if n in MAIN[i - 1]]
    print(f'   {n:12s} in References body: {inref:3d}   cited in unit: {inunit}')

# --------------------------------------------------------------------------- 4
hr('4  RULING 45 (build/editorial narration) AND RULING 46 (script/file names) -- ONE PASS, CASE-SENSITIVE')
R45 = [r'\bearlier draft\b', r'\bearlier version\b', r'\bprevious draft\b', r'\bthis book\b',
       r'\bthe author\b', r'\bin the writing\b', r'\bthe draft\b', r'\bwas written\b',
       r'\bre-?wrote\b', r'\bthe writing\b', r'\bthis text\b', r'\bthese pages\b']
hits45 = sorted({i for i in U for p in R45 if re.search(p, MAIN[i - 1], re.I)})
print(f'  Ruling 45 candidate sites in unit ({len(hits45)}): {hits45}')
for i in hits45: print(f'   L{i} {norm(MAIN[i-1])[:104]}')
R46 = [r'\.py\b', r'\bBUILD\d+', r'\bmarkdown\b', r'\bgit\b', r'\.md\b', r'\.tsv\b', r'\.png\b']
hits46 = sorted({i for i in U for p in R46 if re.search(p, MAIN[i - 1])})
print(f'  Ruling 46 sites in unit (case-sensitive): {hits46}')
for i in hits46: print(f'   L{i} {norm(MAIN[i-1])[:104]}')

# --------------------------------------------------------------------------- 5
hr('5  FIRST-PERSON PROSE -- with chat 123 fault 8 guarded (the Roman numeral in "He I")')
fp = []
for i in U:
    t = MAIN[i - 1]
    for m in re.finditer(r'\b(I|my|we|our|us)\b', t):
        if m.group(1) == 'I':
            nxt = t[m.end():m.end() + 3]
            prv = t[max(0, m.start() - 4):m.start()]
            if re.match(r'^[IVX]', nxt.strip()[:1] or ' ') or re.search(r'[A-Z][a-z]?\s$', prv):
                continue        # He I / Ne I / K I  -- a species label, not a pronoun
        fp.append((i, m.group(1))); break
print(f'  first-person sites in unit: {fp}')
for i, _ in fp: print(f'   L{i} {norm(MAIN[i-1])[:110]}')

# --------------------------------------------------------------------------- 6
hr('6  PRINTS & PROOFS -- each witness anchored on ITS OWN text (chat 120 saw -88 and -94 in one unit)')
wit = [_L('### 32.7 On a verification that does not test its claim'), _L(' **An earlier draft called this the class of error no automated test will find, and left it there. That was the wrong conclusion.**'), _L(' **This is Principle 8 in its ordinary form: any true answer, good or bad, is a bound.** A verification that misses its target does not merely fail; it locates the target by missing it.'), _L('| self-duality checked with *x* ↦ max + min − *x* | gave 112, not 8 | **the right map is *x* ↦ max − *x*** |'), _L(' **In every case the wrong verification was the thing that produced the right one.** The self-duality mismatch gave the correct involution. The four-level sample gave the twenty-member mean. The circular test gave the non-circular statement. **None of these was found by a reader.**'), _L(' On the word "unprecedented"'), _L(" **Not new.** The lattice is a bijective recoding of quantum numbers that have been in place since the 1920s. Closure operators, Galois connections and formal concept analysis are established mathematics; E(X) is a **closure defect** in the ordinary sense and is claimed as an application, not an invention. Birkhoff's representation is from 1937, Dilworth's theorem from 1950, Sperner's from 1928. The reorderability question is settled in a 2004 survey the author found only after five failed attempts on it. The solution-density result of Chapter 29 is almost certainly the standard constraint-satisfaction phase transition, and is reported as a rediscovery."), _L('    No one had asked what the periodic table costs.'), _L(' **The failure condition, inverted.** |Δ*T*| < 2*Z*²*R*/ν³ turns 1,061 non-failures into 1,061 measurements. Bracketing methods are rare; inverting their silence appears not to have been done.'), _L(' **The cost of a guarantee.** *V* = 4ν/3 is two lines from the Rydberg formula and has no use in a fitting paradigm. That is the best argument that it is new, and the four unreachable documents of §24.2 are the best argument that it may not be.'), _L('    and recording the one thousand six hundred and thirty-five times it caught the author — is the part'), _L(' And the form, which is the stronger claim'), _L(' **It states three conditions under which it would be false, runs them on itself, and reports the two that failed** — one a missing chapter, one thirty-nine unverified claims — with the computations that found them and the repairs that followed.'), _L(' Its register of one thousand six hundred and thirty-five withdrawn claims is offered as the primary'), _L(' **And it is an index of a law about indices, which is itself an index, tested as one.**'), _L(' **That is where the word belongs.** Not on *V* = 4ν/3, which may sit in a 1922 German volume nobody cites. Not on E(X), which is a closure defect and says so. **On the shape of the thing** — a work built to be checked, that checked itself, failed twice, said so, and repaired both.')]
offs = {}
for i in wit:
    key = norm(MAIN[i - 1])
    if not key: continue
    hits = [j + 1 for j, t in enumerate(PP) if norm(t) == key]
    offs[i] = [(j - i) for j in hits] if hits else None
    print(f'   L{i:5d} PP {"P" + str(hits[0]) if hits else "ABSENT":>8s}  offset '
          f'{offs[i][0] if offs[i] else "--":>5}   {key[:66]}')
found = [v[0] for v in offs.values() if v]
print(f'  witnesses present {len(found)} of {len(wit)}; distinct offsets {sorted(set(found))}')

# --------------------------------------------------------------------------- 7
hr('7  DEFECT-CENSUS ROWS IN RANGE -- classes main AND all, keyed on the column named member')
rows = list(csv.DictReader(open(os.path.join(H, 'DEFECT-CENSUS.tsv'), encoding='utf-8'), delimiter='\t'))
print(f'  census rows {len(rows)}; member values {sorted({r["member"] for r in rows})}')
inr = [r for r in rows if r['member'] in ('main', 'all') and r['line'].isdigit() and A <= int(r['line']) < B]
print(f'  rows in L{A}-L{B-1}: {len(inr)}')
for r in inr: print(f'   {r["id"]} {r["class"]} {r["member"]} L{r["line"]} {r["item"][:40]} | {r["detail"][:70]}')

# --------------------------------------------------------------------------- 8
hr('8  DUPLICATED-SECTION SWEEP (DEF-105 item 1) -- long lines of the unit recurring elsewhere')
long = [i for i in U if len(MAIN[i - 1].strip()) > 80]
dup = []
for i in long:
    k = norm(MAIN[i - 1])
    other = [j for j in range(1, len(MAIN) + 1) if j not in U and norm(MAIN[j - 1]) == k]
    if other: dup.append((i, other))
print(f'  long lines swept {len(long)}; recurring elsewhere {len(dup)} -> {dup}')

# --------------------------------------------------------------------------- 9
hr('9  UNMARKED SUB-HEADINGS IN THE BODY (docket 28), AND THE SAME LINES IN PP')
for i in (_L(' On the word "unprecedented"'), _L(' And the form, which is the stronger claim')):
    key = norm(MAIN[i - 1])
    hits = [j + 1 for j, t in enumerate(PP) if norm(t) == key]
    print(f'   L{i} {MAIN[i-1]!r}')
    print(f'        markdown heading? {bool(re.match(r"^#{1,6} ", MAIN[i-1].strip()))}   '
          f'bold? {MAIN[i-1].strip().startswith("**")}   in PP at {hits or "ABSENT"}')

# --------------------------------------------------------------------------- 10
hr('10  THE FIFTH TABLE CASE, AND THE TWO THAT DO TRACE -- "all from this book\'s own record"')
for label, pat in (('22 of 60', r'\b22 of 60\b'), ('22 / 60 loose', r'\b22\b[^\n]{0,40}\b60\b'),
                   ('d-dimensional', r'\bd-dimensional\b'), ('one-dimensional', r'one-dimensional'),
                   ('closure criterion', r'closure criterion')):
    print(f'  {label:20s} {sweep(pat, cap=10)}')
print('\n  the two that DO trace, read at their sources:')
for i in (_L(' produced "3 of 85," which produced "almost never reorderable," which produced a false dismissal of a'), _L('  • Ran a circular test — a prefix loop whose last step was the thing being tested — and reported 560/560')): print(f'   L{i} {norm(MAIN[i-1])[:150]}')

# --------------------------------------------------------------------------- 11
hr('11  THE 1,635 REFERENT ACROSS ITS FIFTEEN WORD-FORM SITES')
word = 'one thousand six hundred and thirty-five'
for i in [i for i in range(1, len(MAIN) + 1) if word in MAIN[i - 1]]:
    tag = ' <-- UNIT' if A <= i < B else ''
    print(f'   L{i:5d} {norm(MAIN[i-1])[:112]}{tag}')

# --------------------------------------------------------------------------- 12
hr('12  FALSE UNIVERSALS AND SUPERLATIVES IN THE UNIT (docket 19)')
UNIV = [r'\bno one\b', r'\bnobody\b', r'\bnone of these\b', r'\bnever\b', r'\bevery\b', r'\ball \b',
        r'\bappears not to have been done\b', r'\bno obvious precedent\b', r'\bdo not usually\b',
        r'\bhas no precedent\b', r'\bwith no precedent\b', r'\bare rare\b']
for i in U:
    hits = [p for p in UNIV if re.search(p, MAIN[i - 1], re.I)]
    if hits: print(f'   L{i} {[p.strip(chr(92)+"b") for p in hits]}  {norm(MAIN[i-1])[:96]}')

# --------------------------------------------------------------------------- 13
hr('13  4ν/3 SITE COUNT RE-MEASURED, EMPHASIS-NORMALISED, ALL SIX VOLUMES (docket 11 carries 24)')
tot = 0
for nm, M in VOLS:
    h = [i for i in range(1, len(M) + 1) if '4ν/3' in demph(M[i - 1])]
    tot += len(h)
    print(f'   {nm:5s} {len(h):3d} {h[:14]}')
print(f'   TOTAL {tot}   (docket 11 carries 24 -- state which population before scoring)')
hr('14  THE PRINCIPLES LIST READ AT ITS TARGET, AND THE TWO PP-ABSENT WITNESSES')
for i in (114, 233, 239, 241, 374, 558, 716, _L(' withdrawals, twenty-two prime audits, twenty principles and twenty-four protocols — and the demonstration'), _L(' §1 requires before anything joins the formalised principles.')):
    print(f'   main L{i} {norm(MAIN[i-1])[:118]}')
print(f'   reg  L1929 {norm(REG[_L(" a function of the others — but in order, *g*'s information rides on *q*'s. Λ₉ measures width 7 as")])[:118]}')
print(f'   ioi  L1924 {norm(IOI[_L(' incomparable — one generator for each coordinate except *g*. The generator that first raises *g* is')])[:118]}')
print('   any numbered principle other than 8, all six volumes: '
      f'{sweep(r"[Pp]rinciple\s+(?!8\b)\d+", flags=0, cap=20) or "NONE"}')
print('\n   the two PP-absent witnesses, read at the unit-wide offset of -94:')
for i in (_L('    and recording the one thousand six hundred and thirty-five times it caught the author — is the part'), _L(' Its register of one thousand six hundred and thirty-five withdrawn claims is offered as the primary')):
    print(f'    main L{i}  {norm(MAIN[i-1])[:104]}')
    for j in (i - 95, i - 94, i - 93):
        print(f'    PP   P{j}  {norm(PP[j-1])[:104]}')
hr('15  RESOLVING "Principle 8" TO THE BOOK\'S OWN P-NUMBERING (P1-P23, less P10/P12/P18)')
p8 = {nm: [i for i in range(1, len(M) + 1) if re.search(r'\bP8\b', M[i - 1])] for nm, M in VOLS}
print(f'   sites of the token P8: { {k: v for k, v in p8.items() if v} }')
for nm, M in VOLS:
    for i in p8.get(nm, [])[:6]:
        print(f'    {nm} L{i} {norm(M[i-1])[:150]}')
print('\n   the principles block read at its target (main L233-L245):')
for i in range(233, 246): print(f'    {i} {norm(MAIN[i-1])[:130]}')
print('\nEND r2-ch16t')
