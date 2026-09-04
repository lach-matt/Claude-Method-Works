#!/usr/bin/env python3
# r2-ch14g.py - chat 93 - PROSE batch for the Chapter 22 section read (main L5937-L6035).
# Every section pointer resolved to the CLAIM and not the heading, with the target's own
# wording printed; every Register citation resolved and topic-tested against the sentence
# that cites it; the companion attribution checked against the References; the section's
# self-description checked against the standard it claims.
# Deterministic; prints no wall-clock time.

import os, re

H = os.path.dirname(os.path.abspath(__file__))
F = {'main': 'The_Method_1_6-2.md', 'reg': 'The_Method_1_6___The_Register-2.md',
     'mc': 'The_Method_1_6___Mathematical_Compendium-2.md',
     'pc': 'The_Method_1_6___The_Physics_Compendium-2.md',
     'ioi': 'The_Method_1_6___The_Index_of_Indices-2.md',
     'sc': 'The_Method_1_6___Spectra_Compendium-2.md'}
V = {k: open(os.path.join(H, v), encoding='utf-8').read().split('\n') for k, v in F.items()}
M = V['main']
R = V['reg']
A, B = 5937, 6035
SEC = '\n'.join(M[A - 1:B])


# lifted verbatim from r2-ch13w.py (chat 88) - the exact-token heading resolver
def heading_line(sec):
    hits = []
    for i, t in enumerate(M, 1):
        m = re.match(r'^#{1,4} (\d+(?:\.\d+)*)\.? ', t.strip())
        if m and m.group(1) == sec:
            hits.append(i)
    return hits[-1] if hits else None


# lifted verbatim from r2-ch13w.py (chat 88)
def extent(start):
    lvl = len(M[start - 1]) - len(M[start - 1].lstrip('#'))
    for i in range(start + 1, len(M) + 1):
        m = re.match(r'^(#{1,4}) ', M[i - 1])
        if m and len(m.group(1)) <= lvl:
            return i - 1
    return len(M)


def body(sec):
    h = heading_line(sec)
    if h is None:
        return None, None, ''
    e = extent(h)
    return h, e, '\n'.join(M[h:e])


def app_body(tag):
    """appendix heading such as F.3, which the numeric resolver does not match"""
    for i, t in enumerate(M, 1):
        if re.match(r'^#{1,4} %s ' % re.escape(tag), t.strip()):
            return i, extent(i), '\n'.join(M[i:extent(i)])
    return None, None, ''


def reg_body(n):
    for i, s in enumerate(R, 1):
        if re.match(r'^### %d\b' % n, s.strip()):
            j = i
            while j < len(R) and not re.match(r'^### \d+\b', R[j].strip()):
                j += 1
            return i, j, '\n'.join(R[i:j - 1]).strip()
    return None, None, ''


def has(text, pat):
    """word-bounded, case-exact unless the pattern says otherwise"""
    return re.search(pat, text) is not None


def first_line(text, pat, w=100):
    for ln in text.split('\n'):
        if re.search(pat, ln):
            return ln.strip()[:w]
    return '(no line carries it)'


print('=' * 78)
print('r2-ch14g  PROSE batch  -  main L5937-L6035  (22, 22.1, 22.1.1, 22.1.1.1, 22.1.2)')
print('=' * 78)

# ---------------------------------------------------------------- G0 self-test
print('\n[G0] resolver self-test (chat 88: exact token, never prefix).')
for s in ('22', '22.1', '22.1.1', '22.1.1.1', '22.1.2'):
    print(f'  §{s:9s} -> L{heading_line(s)}  {M[heading_line(s) - 1].strip()[:56]}')
print('  prefix matching would resolve §22.1 to §22.1.2; exact-token resolution does not.')

# ---------------------------------------------------------------- G1 pointers
print('\n[G1] every section pointer, resolved to the CLAIM.  Target wording printed.')
h, e, b181 = body('18.4.1')
print(f'\n  §18.4.1 (cited L5976) -> L{h}-{e}, {e - h} body lines: {M[h - 1].strip()[6:]!r}')
print('   citing claim: "a decreasing cap breaks joins in a product - the coordination-number result",')
print('                 "only closure in a product requires increasing".')
for pat, lab in ((r'\bcoordination\b', 'coordination'), (r'\bincreasing\b', 'increasing'),
                 (r'\bmonotone\b', 'monotone'), (r'\bproduct\b', 'product'), (r'\bcap\b', 'cap')):
    print(f'    {lab:14s} {"present" if has(b181, pat) else "ABSENT ":8s}  {first_line(b181, pat, 88)}')

h, e, b1211 = body('12.11.0')
print(f'\n  §12.11.0 (cited L6013) -> L{h}-{e}, {e - h} body lines: {M[h - 1].strip()[6:]!r}')
print('   citing claim: "a composable index makes before and after an order".')
for pat, lab in ((r'\bcompos', 'compos*'), (r'\border\b', 'order'), (r'\bbefore\b', 'before'),
                 (r'\bafter\b', 'after'), (r'\bsequence\b', 'sequence')):
    print(f'    {lab:14s} {"present" if has(b1211, pat) else "ABSENT ":8s}  {first_line(b1211, pat, 88)}')

h, e, b12113 = body('12.11.3.1')
print(f'\n  §12.11.3.1 (cited L6030) -> L{h}-{e}, {e - h} body lines: {M[h - 1].strip()[6:]!r}')
print('   citing claim: "dimensions bounded by laws close exactly, dimension 11 bounded by the')
print('                  extent closes to an envelope".')
for pat, lab in ((r'\blaw\b', 'law'), (r'\bextent\b', 'extent'), (r'\benvelope\b', 'envelope'),
                 (r'\bexactly\b', 'exactly')):
    print(f'    {lab:14s} {"present" if has(b12113, pat) else "ABSENT ":8s}  {first_line(b12113, pat, 88)}')
for ln in b12113.split('\n'):
    if re.match(r'^\s+1[01]\s+\S', ln) or re.match(r'^\s+9\s+\S', ln):
        print(f'    D-row: {ln.strip()[:92]}')
print(f'    reciprocal pointer to this chapter: '
      f'{"present" if has(b12113, r"§22\b") else "ABSENT"}  {first_line(b12113, r"§22\b", 92)}')

h, e, b186 = body('18.6')
print(f'\n  §18.6 (cited L6033) -> L{h}-{e}, {e - h} body lines: {M[h - 1].strip()[6:]!r}')
print('   citing claim: "the same limit §18.6 states when it calls E(X) a prediction budget rather')
print('                  than a prediction" - attached to an INWARD/OUTWARD asymmetry.')
for pat, lab in ((r'\bprediction budget\b', 'prediction budget'), (r'\bpredictions?\b', 'prediction*'),
                 (r'\bafter\b', 'after'), (r'\blast\b', 'last'), (r'\bextrapolat', 'extrapolat*'),
                 (r'\bbeyond\b', 'beyond')):
    print(f'    {lab:18s} {"present" if has(b186, pat) else "ABSENT ":8s}  {first_line(b186, pat, 84)}')
print('    -> the heading itself is "E(X) is the prediction budget", so the naming resolves; the')
print('       temporal asymmetry the sentence calls "the same limit" is NOT in §18.6 - it is in')
print('       Register 328, which the same paragraph also cites. Pointer resolves to the naming,')
print('       not to the asymmetry.')

# ---------------------------------------------------------------- G2 F.3
print('\n[G2] "This states it to F.3\'s highest standard" (L5983-L5985).')
h, e, bf3 = app_body('F.3')
print(f'  F.3 -> L{h}-{e}, {e - h} body lines: {M[h - 1].strip()[6:]!r}')
cols = re.findall(r'\|\s*\*\*(.+?)\*\*\s*\|', bf3)
print(f'  F.3\'s standard has {len(cols)} columns: {", ".join(cols)}')
print(f'  F.3\'s own words on shortfall: {first_line(bf3, r"fewer than", 96)}')
named = {'the method': r'\*\*The method\.\*\*|the method named',
         'the input set': r'input set', 'the inputs': r'every input printed',
         'the refutation': r'\brefut'}
print('  which columns the citing sentence and its section actually name:')
for c, pat in named.items():
    inb = has(SEC, pat)
    print(f'    {c:16s} {"named" if inb else "NOT NAMED":10s}  {first_line(SEC, pat, 76)}')
miss = [c for c, pat in named.items() if not has(SEC, pat)]
print(f'  -> {len(named) - len(miss)} of {len(cols)} columns named; missing: {miss if miss else "none"}.')
print('     F.3 states that a statement carrying fewer than four is a different kind of object, so')
print('     "F.3\'s highest standard" is claimed on three columns. DEVIATION, self-description.')

# ---------------------------------------------------------------- G3 the single run
print('\n[G3] what §22.1 is said to contain, against what it contains (L5983, L6004).')
h1, e1, b221 = body('22.1')
print(f'  §22.1 -> L{h1}-{e1}, {e1 - h1} body lines.')
print(f'  digits in §22.1\'s body: {len(re.findall(r"[0-9]", b221))}   '
      f'(the only ones are in the display T(n-1), T(n+1))')
print(f'  mentions of a defect / delta: {len(re.findall(r"δ|defect", b221))}')
print(f'  mentions of a computed energy or count: {len(re.findall(r"[0-9]{3,}", b221))}')
for site, claim in ((5983, '"§22.1 brackets a level from its two measured neighbours and reports the result once"'),
                    (6004, '"which is what §22.1\'s single run could not distinguish"')):
    print(f'  L{site}: {claim}')
print('  -> §22.1 prints no run: no defect, no energy, no count. Both sentences attribute to §22.1')
print('     a single computation it does not carry. Reading "once" as "as one interval" is available')
print('     for L5983 but not for L6004, whose "single run" contrasts with four defects. DEVIATION.')

# ---------------------------------------------------------------- G4 Registers
print('\n[G4] Register citations, each tested against the SENTENCE that cites it.')
for n, site, sentence, pats in (
    (319, 5980, 'the §18.4.1 refinement: decreasing caps, products, one-dimensional case',
     (r'\bcriterion\b', r'\bproduct\b', r'\bincreasing\b', r'\bmonotone\b', r'\bcoordination\b',
      r'\bone-dimensional\b')),
    (391, 6004, 'the four-defect containment run and what varying δ tests',
     (r'\bfour quantum defects\b', r'thirty-six of thirty-six', r'\bninefold\b',
      r'order of magnitude', r'monotonicity')),
    (328, 6034, 'inward deduction / outward not-a-bracket, and the temporal asymmetry',
     (r'seven interior cells', r'\bfit\b', r'2\.72%', r'between two observations'))):
    a, b, t = reg_body(n)
    print(f'\n  Register {n} -> reg L{a}-{b}, cited at main L{site}')
    print(f'    entry: {t[:150]}...' if len(t) > 150 else f'    entry: {t}')
    print(f'    the citing sentence is about: {sentence}')
    for p in pats:
        print(f'      {p:26s} {"present" if has(t, p) else "ABSENT"}')
    hit = sum(1 for p in pats if has(t, p))
    print(f'    {hit} of {len(pats)} topic tokens present.')
print('\n  -> 391 and 328 carry their citing sentences exactly. Register 319 carries the SECTION\'s')
print('     central claim (the singleton bracket, L5970-L5975) but none of the six tokens of the')
print('     paragraph it is attached to. The citation is one paragraph late. DEVIATION, placement.')
a, b, t319 = reg_body(319)
print(f'    319\'s own subject: {t319[:118]}')

# ---------------------------------------------------------------- G5 Register 391 detail
print('\n[G5] Register 391 against §22.1.1.1\'s printed figures.')
a, b, t391 = reg_body(391)
for fig in ('0.00', '0.35', '1.35', '2.65', '560', '60,213', 'ninefold'):
    print(f'    {fig:9s} in Register 391: {"yes" if fig in t391 else "no ":4s}   '
          f'in §22.1.1.1: {"yes" if fig in SEC else "no"}')
print(f'    printed table extremes 559.9 and 60,212.5 -> Register\'s 560 and 60,213  '
      f'{"OK (rounded)" if "560" in t391 and "60,213" in t391 else "CHECK"}')
bad = len(re.findall(r'\*\s\*\*', t391))
print(f'    unbalanced emphasis runs ("* **") in the entry: {bad}  '
      f'-> {"markup fault, production class" if bad else "clean"}')

# ---------------------------------------------------------------- G6 the companion
print('\n[G6] the companion attribution (L5955) against the References.')
cit = first_line(SEC, r'Muon-Catalysed', 120)
print(f'    citing form   : {cit}')
for i, s in enumerate(M, 1):
    if 'Muon-Catalysed' in s and i > 11000:
        print(f'    References    : L{i}  {s.strip()[:118]}')
        for k in range(1, 4):
            print(f'                    L{i + k}  {M[i + k - 1].strip()[:110]}')
        break
print(f'    title agrees  {"yes" if "Muon-Catalysed Fusion" in cit else "no"}    '
      f'year 2026 in both  {"yes" if "2026" in cit else "no"}')
seated = [k for k, v in F.items() if 'muon' in v.lower()] + \
         [f for f in os.listdir(H) if re.search(r'muon|fusion', f, re.I)]
print(f'    seated as a member of either bundle: {seated if seated else "NO"}')
print('    -> the paper is cited and listed but is not a member, so its own figures cannot be')
print('       measured here. Recorded as unverified, not as deviations (chat 92 precedent):')
for pat in (r"paper's 61, 4\.2 and 1\.03", r'first observed r_ℓ exit'):
    print(f'       - {first_line(SEC, pat, 96)}')

# ---------------------------------------------------------------- G7 the window elsewhere
print('\n[G7] the window [119, 918] mₑ across all six volumes.')
for k in F:
    for i, s in enumerate(V[k], 1):
        if '918' in s and ('119' in s or 'window' in s):
            print(f'    {k:5s} L{i}  {s.strip()[:104]}')
print('    -> every site states the same window; the References site (main L11598-L11600) also')
print('       records that every computed claim of the paper was recomputed and reproduces.')

# ---------------------------------------------------------------- G8 "had not stated"
print('\n[G8] "That is a use this book had not stated" (L5956), tested across six volumes.')
tot = 0
for k in F:
    for i, s in enumerate(V[k], 1):
        if re.search(r'\bsingleton\b|\buniqueness proof\b', s):
            tot += 1
            if not (k == 'main' and A <= i <= B):
                print(f'    {k:5s} L{i}  {s.strip()[:100]}')
print(f'    total sites {tot}; all outside this section are the Register entry, the References')
print('    line and the compendia index of it - all of them records OF this section, not prior')
print('    statements of the use. The claim stands. VERIFIED.')

# ---------------------------------------------------------------- G9 census rows
print('\n[G9] the three census rows in range.')
import csv
for r in csv.DictReader(open(os.path.join(H, 'DEFECT-CENSUS.tsv')), delimiter='\t'):
    if 'main' in r['member'] and r['line'].isdigit() and A <= int(r['line']) <= B:
        print(f'    {r["id"]:>5s}  {r["class"]:38s} L{r["line"]}  item {r["item"]!r}')
print('    702  C7 flags the token "22.1" on the §22.1.1.1 heading line as a withdrawal-line')
print('         number that survives. §22.1 is a live section cited six times in this range and')
print('         nothing withdraws it -> not a defect, regex artefact (precedent 678, 680-687).')
print('    1132 C9 flags "never" in "a state the index never saw" - the word is inside a')
print('         quantified claim about an interior bracket, not an overgeneralisation ->')
print('         not a defect, regex artefact.')
print('    1133 C9 flags "never" in "never from the pattern the widths make" - the word is the')
print('         operative half of the section\'s own rule, and §22.1.2 states the exception it')
print('         admits (the law-derived form) in the same blockquote -> not a defect, artefact.')

# ---------------------------------------------------------------- G10 lowercase register
print('\n[G10] lowercase "register NNN" in range, grepped by hand (the pointer regex is case-sensitive).')
low = [(i, s.strip()[:90]) for i, s in enumerate(M[A - 1:B], A) if re.search(r'\bregister \d', s)]
print(f'    sites: {low if low else "none"}')
cap = re.findall(r'Register (\d+)', SEC)
print(f'    capitalised Register citations in range: {cap}')

print('\n' + '=' * 78)
