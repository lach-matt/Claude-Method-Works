#!/usr/bin/env python3
"""r2-ch15g - prose claims of the unit main L7332-L7457 (27.6, PART VI, 28-28.5).

Chat 106.  Reads MEMBERS only.  Resolvers come from r2lib by path and are passed the LINE LIST.
Every pointer test carries a CLAIM-LOCATOR beside it: the heading is never accepted as the claim.
Token tests run on the RAW line, case-insensitively, word-bounded, in the symbol as well as the
name, and a phrase is sought on the two-line join as well, because this book wraps.  Every
negative names the span it swept.
"""
import importlib.util, re

H = '/home/claude/members/'
spec = importlib.util.spec_from_file_location('r2lib', H + 'r2lib.py')
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)

VOLS = {'main': 'The_Method_1_6-2.md', 'reg': 'The_Method_1_6___The_Register-2.md',
        'mc': 'The_Method_1_6___Mathematical_Compendium-2.md',
        'pc': 'The_Method_1_6___The_Physics_Compendium-2.md',
        'ioi': 'The_Method_1_6___The_Index_of_Indices-2.md',
        'sc': 'The_Method_1_6___Spectra_Compendium-2.md'}
LINES = {k: r2lib.read_member(v).split('\n') for k, v in VOLS.items()}
M = LINES['main']
U0, U1 = 7332, 7457


def hdr(t):
    print('\n' + '=' * 96); print(t); print('=' * 96)


def win(L, i, w=0, tag=''):
    print(f'     {tag}L{i}  {L[i-1].strip()[:104]}')
    for j in range(i + 1, min(i + 1 + w, len(L) + 1)):
        print(f'          {L[j-1].strip()[:104]}')


def locate(sec, toks, vol='main'):
    """Resolve a section pointer to its CLAIM: does the cited span carry the token, raw,
    word-bounded, and in the symbol as well as the name?  Prints a window at each hit."""
    L = LINES[vol]
    sp = r2lib.section_span(L, sec)
    if sp is None:
        print(f'   §{sec}: HEADING NOT FOUND in {vol}')
        return
    s, e = sp
    print(f'   §{sec}  {vol} L{s}-{e-1}   {L[s-1].strip()[:66]}')
    for tok in toks:
        hits = [i for i in range(s, e)
                if re.search(r'(?<![A-Za-z0-9])' + re.escape(tok) + r'(?![A-Za-z0-9])',
                             L[i - 1], re.I)]
        wrapped = [i for i in range(s, e - 1)
                   if not hits and re.search(re.escape(tok).replace(r'\ ', r'\s+'),
                                             L[i - 1].rstrip() + ' ' + L[i].lstrip(), re.I)]
        print(f'      "{tok}": {len(hits)} raw, {len(wrapped)} wrapped'
              + ('   <- ABSENT from the cited span' if not hits and not wrapped else ''))
        for i in (hits + wrapped)[:2]:
            win(L, i)


# ------------------------------------------------------------------ G1
hdr('G1  every section pointer in the unit, resolved to the CLAIM and not the heading')
print('  L7340  "max ∅ = −∞ in §6.1\'s definition of φ̂" - symbol AND name:')
locate('6.1', ['max ∅', '−∞', 'phi', 'φ̂'])
print('  L7347-51  "§29.2.2 records that reading as not posable":')
locate('29.2.2', ['posable', 'multiverse'])
print('  L7348  "§E.1.4 shows the open set cannot express an unclosable question":')
sp = r2lib.section_span(M, 'E.1.4')
print(f'   §E.1.4 by numeric resolver: {sp}  (lettered headings are outside heading_line\'s rule)')
for i, t in enumerate(M, 1):
    if re.match(r'^#{2,4}\s*E\.1\.4\b', t.strip()):
        print(f'   FOUND by explicit lettered match at L{i}: {t.strip()[:80]}')
        for j in range(i, min(i + 12, len(M))):
            if re.search(r'obstacle|unclosable|open set', M[j - 1], re.I):
                win(M, j)
print('  L7351  "§16.6\'s ⅅ_gro":')
locate('16.6', ['ⅅ_gro', 'gro'])
print('  L7449  "§25.6 reports a bracket and no point estimate":')
locate('25.6', ['point estimate', 'bracket'])
print('  L7369-70  "six in the literature search of Chapter 29", "eight in ... §24.8 and §25.6":')
locate('24.8', ['withdraw', 'eight'])
print('  L7442  "it is why Rule 4 is per-cell":')
for i, t in enumerate(M, 1):
    if re.search(r'\bRule 4\b', t) and re.search(r'per-cell|σ', t):
        win(M, i, tag='Rule 4 site  ')

# ------------------------------------------------------------------ G2
hdr('G2  Register 447 (L7355) and Register 658 (L7382) - headline QUOTED before it is cited')
reg = LINES['reg']
for n in (447, 658, 446, 438):
    hit = [i for i, t in enumerate(reg, 1) if re.match(r'^#{1,4}\s*' + str(n) + r'\s*$', t.rstrip())]
    if not hit:
        print(f'   Register {n}: no bare heading  <- check grouped headings')
        continue
    i = hit[-1]
    body = [reg[j - 1].strip() for j in range(i + 1, min(i + 8, len(reg)))
            if reg[j - 1].strip()][:2]
    print(f'   Register {n} at reg L{i}:')
    for b in body:
        print(f'      {b[:150]}')

# ------------------------------------------------------------------ G3
hdr('G3  Ruling 46 sweep - script names, build numbers and internal file references in the unit')
R46 = re.compile(r'\b\w+\.py\b|\bBUILD\s?\d+|\bbuild \d|at this build|register_gen', re.I)
for i in range(U0, U1 + 1):
    if R46.search(M[i - 1]):
        win(M, i, tag='R46  ')
print('   and the same sweep over the whole main volume, for the size of the class:')
allr46 = [i for i, t in enumerate(M, 1) if R46.search(t)]
print(f'   {len(allr46)} main-volume sites; the first eight outside the unit:')
for i in allr46[:8]:
    print(f'     L{i} {r2lib.enclosing(M, i):>10}  {M[i-1].strip()[:92]}')

# ------------------------------------------------------------------ G4
hdr('G4  Ruling 45 sweep - build or editorial-process remarks addressed to the reader')
R45 = re.compile(r"this chapter|this book|the book's own|an edit here|retained in the compendium"
                 r"|printed here|listed here|the author", re.I)
for i in range(U0, U1 + 1):
    if R45.search(M[i - 1]):
        win(M, i, tag='R45? ')

# ------------------------------------------------------------------ G5
hdr('G5  formatting defects measured in the unit')
print('   (a) a paragraph broken by a blank line mid-sentence:')
for i in range(U0 + 1, U1):
    prev, cur, nxt = M[i - 2], M[i - 1], M[i]
    if cur.strip() == '' and prev.strip() and nxt.strip():
        if not re.search(r'[.:;!?]\s*$', prev.rstrip()) and not re.match(r'^\s*(\*\*|#|\||•)',
                                                                         nxt):
            print(f'     L{i-1}-{i+1}:')
            win(M, i - 1); win(M, i + 1)
print('   (b) a section body opening in lower case directly under its heading:')
for i in range(U0, U1 + 1):
    if re.match(r'^#{2,4} ', M[i - 1]) and i < U1:
        for j in range(i + 1, min(i + 3, U1 + 1)):
            if M[j - 1].strip():
                if re.match(r'^\s*[a-z]', M[j - 1]):
                    print(f'     heading L{i}: {M[i-1].strip()[:60]}')
                    win(M, j, tag='body ')
                break
print('   (c) the same sweep for lower-case section openings over the whole volume:')
low = []
for i, t in enumerate(M, 1):
    if re.match(r'^#{2,4} ', t):
        for j in range(i + 1, min(i + 3, len(M) + 1)):
            if M[j - 1].strip():
                if re.match(r'^\s*[a-z]', M[j - 1]) and not re.match(r'^\s*[a-z]\)', M[j - 1]):
                    low.append((i, j))
                break
print(f'     {len(low)} sites in the main volume; first six: {[f"L{a}/L{b}" for a, b in low[:6]]}')

# ------------------------------------------------------------------ G6
hdr('G6  heading ORDER of Chapter 28 - measured, not assumed')
seq = [(i, re.match(r'^#{2,4} (\d+(?:\.\d+)*)', t.strip()).group(1))
       for i, t in enumerate(M, 1)
       if re.match(r'^#{2,4} (28|29)(\.\d+)*[\s.]', t.strip()) and i > 200]
prev = None
for i, s in seq:
    flag = ''
    if prev and s.split('.')[0] != prev.split('.')[0] and s.split('.')[0] == '28':
        flag = '   <- a §28 heading INSIDE Chapter 29'
    print(f'   L{i}  §{s}{flag}')
    prev = s

# ------------------------------------------------------------------ G7
hdr('G7  the duplicated-section sweep owed by DEF-105 item 1, run on THIS unit')
norm = lambda s: re.sub(r'[^a-z0-9 ]', '', re.sub(r'\s+', ' ', s.lower())).strip()
targets = [(i, norm(M[i - 1])) for i in range(U0, U1 + 1)
           if len(norm(M[i - 1])) > 55]
idx = {}
for v, L in LINES.items():
    for i, t in enumerate(L, 1):
        n = norm(t)
        if len(n) > 55:
            idx.setdefault(n, []).append((v, i))
dups = 0
for i, n in targets:
    others = [x for x in idx.get(n, []) if not (x[0] == 'main' and x[1] == i)]
    if others:
        dups += 1
        print(f'   main L{i} also at {others[:3]}')
        print(f'     {M[i-1].strip()[:96]}')
print(f'   {dups} of {len(targets)} long lines in the unit occur a second time in six volumes')

# ------------------------------------------------------------------ G8
hdr('G8  attributions in the unit')
for name, toks in (('Birkhoff (L7337, "Birkhoff needs finiteness")', ['Birkhoff']),
                   ('the 2004 survey (L7410)', ['2004'])):
    print(f'   {name}:')
    for v in ('main', 'mc', 'reg'):
        L = LINES[v]
        hits = [i for i, t in enumerate(L, 1)
                if any(re.search(r'(?<![A-Za-z])' + re.escape(k) + r'(?![A-Za-z])', t) for k in toks)
                and not (v == 'main' and U0 <= i <= U1)]
        print(f'     {v}: {len(hits)} site(s)  {[f"L{i}" for i in hits[:6]]}')
        for i in hits[:2]:
            win(L, i)

# ------------------------------------------------------------------ G9
hdr('G9  27.6\'s self-description, and the census row 1155 token')
for i in (7357, 7359, 7360, 7361, 7362):
    win(M, i)
print('   census 1155 flags "never" at L7359 as an overgeneralisation-word.')
print('   the sentence is about the three LANGUAGES of 27.1, not about the collection:')
print('   test - does any of algebra/geometry/calculus claim precedence over another anywhere?')
comp = re.compile(r'(algebra|geometr|calculus)\w*\s+(?:is\s+)?(?:better|superior|beats|wins)', re.I)
hits = [(v, i) for v, L in LINES.items() for i, t in enumerate(L, 1) if comp.search(t)]
print(f'   competition-claim sites over six volumes: {len(hits)}  {hits[:5]}')

print('\nDONE r2-ch15g')
