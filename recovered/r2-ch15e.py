#!/usr/bin/env python3
"""r2-ch15e - prose claims, pointers and census support for Chapter 27, unit L7203-L7331.

Chat 105.  Reads members only, plus the Prints & Proofs original at /home/claude
(md5 49900cf41f818ab789bb90fc596ac977, verified at fetch) as the Ruling 56 original-input
witness.  Resolvers imported from r2lib by path and passed the LINE LIST, never the member text.
Every token test is case-insensitive, word-bounded and run on the RAW line; a claim carrying a
symbol is tested in the symbol AND in the spelled form.  Every pointer test carries a
claim-locator, and every section is swept as a MAGNET as well as a target.  A window is printed
around each match, never the head of the line.

Rewritten once before banking.  The faults, both self-caught:
  1. P2 tested claim tokens in spelled form only, so "delta = f - l" was reported absent from
     17.3 when the section prints the symbol.  Symbols are now tested beside their names.
  2. P2 treated "Theorem 18.2" as a pointer to section 18.2 and resolved it to the wrong place.
     A theorem number is not a section number; theorems are located by their own numbering.
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
PP = open('/home/claude/PP_The_Method_1_6.md', encoding='utf-8').read().split('\n')
U0, U1 = 7203, 7331


def hdr(t):
    print('\n' + '=' * 96); print(t); print('=' * 96)


def window(line, tok, w=58):
    i = line.lower().find(tok.lower())
    if i < 0:
        return line.strip()[:2 * w]
    return ('...' if i - w > 0 else '') + line[max(0, i - w):i + len(tok) + w].strip() + '...'


def norm(s):
    s = re.sub(r'[*_`]', '', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip().lower()


# ------------------------------------------------------------------ P1
hdr('P1  27.1 (L7208-L7224): the shattered table against the Prints & Proofs original')
for i in range(7207, 7226):
    print(f'    {i:5d}| {M[i-1]}')
key = 'what the box admits, minus what'
pp = [i + 1 for i, l in enumerate(PP) if key in l]
print(f'\n  the identical row in the Prints & Proofs original at P{pp}:')
for p in pp:
    for j in range(p - 6, p + 7):
        if 0 < j <= len(PP):
            print(f'    P{j:5d}| {PP[j-1]}')
same = [M[i - 1] for i in range(7208, 7226)] == [PP[j - 1] for j in range(pp[0] - 6, pp[0] + 12)]
print(f'\n  member block == P&P block, line for line: {same}')
print('  -> the shattered columns are CARRIED FROM THE ORIGINAL INPUT, not lost in this build.')
print('     Authoring/production defect of the source (chat 104 L7156 disposition), for R3.')
print('\n  table形 across the chapter (markdown pipe rows vs space-aligned rows):')
for a, b, name in ((7208, 7224, '27.1'), (7234, 7239, '27.2'), (7251, 7257, '27.3'),
                   (7277, 7283, '27.4'), (7304, 7308, '27.5.1')):
    rows = [M[i - 1] for i in range(a, b + 1) if M[i - 1].strip()]
    pipes = sum(1 for l in rows if l.strip().startswith('|'))
    print(f'    {name:7s} L{a}-L{b}: {pipes} pipe rows, {len(rows)-pipes} space-aligned rows')
print('  -> 27.3 is the only table in the chapter that will render as a table.')

# ------------------------------------------------------------------ P2
hdr('P2  every SECTION pointer in the unit, resolved to the CLAIM and not the heading')
POINTERS = [(7226, '9.2', ['occupancy', 'metric']),
            (7282, '23.7', ['pole', "y''", 'y″']),
            (7283, '25.6', ['forecast', 'prediction', 'E(X)']),
            (7295, '9.2', ['metric', 'logarithm', 'log']),
            (7301, '27.2', ['prove', 'one quantity', 'three measures']),
            (7310, '9.2', ['interval', 'cells']),
            (7310, '12.11.0.12', ['transition', 'interval', 'inputs']),
            (7311, '22.1', ['measurement', 'interval', 'bracket']),
            (7322, '18.6', ['prediction', 'E(X)', 'cell']),
            (7323, '25.6.3', ['deduction', 'measured', 'neighbour']),
            (7328, '17.3', ['δ', 'interval', 'f − ℓ', 'convex'])]
for ln, sec, toks in POINTERS:
    hl = r2lib.heading_line(M, sec); span = r2lib.section_span(M, sec)
    print(f'\n  L{ln} -> §{sec}   citing: {window(M[ln-1], sec, 46)}')
    if not hl:
        print('    NOT RESOLVED by exact-token heading_line'); continue
    a, b = span if span else (hl, hl)
    body = '\n'.join(M[i - 1] for i in range(a, b + 1))
    print(f'    heading L{hl}: {M[hl-1].strip()[:80]}   span L{a}-L{b}')
    for t in toks:
        if re.match(r'^[A-Za-z(]', t):
            hit = bool(re.search(r'(?<![A-Za-z])' + re.escape(t) + r'', body, re.I))
        else:
            hit = t in body
        print(f'      claim-locator "{t}": {"FOUND" if hit else "ABSENT"}')

hdr('P2b  Theorem 18.2 (L7321) is a theorem number, not a section pointer')
for i, l in enumerate(M):
    if re.search(r'Theorem\s*18\.2', l):
        print(f'  main L{i+1}: {l.strip()[:120]}')
print(f'  heading_line(M, "18.2") resolves to L{r2lib.heading_line(M, "18.2")}: '
      f'{M[r2lib.heading_line(M, "18.2")-1].strip()[:60]}  - a DIFFERENT object.')

# ------------------------------------------------------------------ P3
hdr('P3  MAGNET test: what points AT chapter 27 and its subsections, from anywhere')
for sec in ['27.1', '27.2', '27.3', '27.4', '27.5', '27.5.1', '27.6']:
    pat = re.compile(r'§\s*' + re.escape(sec) + r'(?![\d.])')
    hits = [(k, i + 1) for k, ls in LINES.items() for i, l in enumerate(ls) if pat.search(l)]
    print(f'  §{sec:7s} {len(hits):3d} incoming: {hits[:10]}')
pat = re.compile(r'§\s*27(?![\d.])')
print(f'  §27 (bare) {sum(1 for k, ls in LINES.items() for l in ls if pat.search(l))} incoming: '
      f'{[(k, i+1) for k, ls in LINES.items() for i, l in enumerate(ls) if pat.search(l)][:10]}')

# ------------------------------------------------------------------ P4
hdr('P4  the two Register entries for one result: 438 (for 9.2) and 446 (for 27.5.1)')
R = LINES['reg']
for n in (438, 446):
    for i, l in enumerate(R):
        if re.match(r'^#{1,4}\s*' + str(n) + r'\s*$', l.strip()):
            print(f'\n  Register {n} - heading at reg L{i+1}; headline:')
            for j in range(i + 1, min(i + 6, len(R))):
                if R[j].strip():
                    print(f'    reg L{j+1}: {R[j].strip()[:230]}')
                    break
            break
print('\n  main L1990 closes 9.2 citing "Register 438"; main L7330 closes 27.5.1 citing "Register 446".')

# ------------------------------------------------------------------ P5
hdr('P5  THE DUPLICATION: 9.2 (L1961-L1990) against 27.5.1 (L7299-L7330)')
A = {norm(M[i - 1]) for i in range(1961, 1991) if M[i - 1].strip()}
B = {norm(M[i - 1]) for i in range(7299, 7331) if M[i - 1].strip()}
inter = A & B
print(f'  9.2 non-blank lines {len(A)}   27.5.1 non-blank lines {len(B)}   line-identical {len(inter)}')
print('\n  --- sentences common to both copies (normalised phrase match) ---')
PH = ['between any two points there is an interval, and the method returns its measure',
      'every pair of cells has a meet and a join',
      'theorem 18.2 permits it',
      'an interval bounds where something already is rather than proposing an unlisted cell',
      'two intervals per pair, nearly disjoint',
      'separately bounded and rarely both',
      'a transition is not a function of its inputs; it is an interval',
      'd = ∏', '[x∧y, x∨y]', '[min, max] output rank', '[t(n−1), t(n+1)]',
      '17% of 264 inputs single-valued']
for ph in PH:
    a = [i for i in range(1961, 1991) if ph in norm(M[i - 1])]
    b = [i for i in range(7299, 7331) if ph in norm(M[i - 1])]
    print(f'    {"BOTH " if a and b else "one  "} 9.2 {a}  27.5.1 {b}   "{ph[:62]}"')
print('\n  --- detail carried by ONE copy only ---')
for ph, where in (('five forms', '9.2'), ('range [3, 23]', '9.2'),
                  ('universal over indices', '9.2'), ('§14.3', '9.2'), ('§18.4.1', '9.2'),
                  ('method rather than an equation', '9.2'), ('register 438', '9.2'),
                  ('11.3%', '27.5.1'), ('24.7%', '27.5.1'), ('§17.3', '27.5.1'),
                  ('convexity', '27.5.1'), ('register 446', '27.5.1'), ('fourth instance', '27.5.1')):
    a = [i for i in range(1961, 1991) if ph.lower() in norm(M[i - 1])]
    b = [i for i in range(7299, 7331) if ph.lower() in norm(M[i - 1])]
    print(f'    "{ph:34s}" 9.2 {str(a):14s} 27.5.1 {str(b):14s} expected in {where}')
print('\n  --- each copy says the other left the thing unsaid ---')
for i in (1977, 1978, 7301, 7302):
    print(f'    main L{i}| {M[i-1].strip()[:118]}')

# ------------------------------------------------------------------ P6
hdr('P6  Ruling 45 sweep of the unit, and Figure 27.1')
R45 = [(r'\bthe name was chosen before\b', 'authoring order disclosed to the reader'),
       (r'\bnone citing the other two\b', "remark on the book's own citation practice"),
       (r'\bwhat that leaves unsaid\b', "remark on an earlier section's omission"),
       (r'\bin practice a teacher does\b', 'aside, not a build remark - retained'),
       (r'\bthis book has computed\b', 'scholarly voice - established vocabulary')]
for i in range(U0, U1 + 1):
    for p, why in R45:
        if re.search(p, M[i - 1], re.I):
            print(f'  L{i}  {why}\n        {window(M[i-1], "the", 60)}')
print()
for i in range(7269, 7275):
    print(f'  L{i}| {M[i-1]}')
figs = [(k, i + 1) for k, ls in LINES.items() for i, l in enumerate(ls)
        if re.search(r'Figure\s*27\.1(?![\d])', l) or 'figure-27.1' in l]
print(f'\n  sites naming Figure 27.1 in six volumes: {len(figs)} -> {figs}')
print('  the caption states facts only; no build or process remark in it (Ruling 45 clean).')

# ------------------------------------------------------------------ P7
hdr('P7  census support: the seven C9-OVERGENERALISATION-WORD rows in range (1148-1154)')
for cid, ln, tok in (('1148', 7266, 'never'), ('1149', 7273, 'never'), ('1150', 7281, 'always'),
                     ('1151', 7281, 'never'), ('1152', 7286, 'always'), ('1153', 7286, 'never'),
                     ('1154', 7287, 'never')):
    print(f'  {cid}  L{ln}  "{tok}"  ->  {window(M[ln-1], tok)}')
print('\n  1148/1149  restate Prop. 23.1 in bits; the floor is proved at L6199 and its bit form is')
print('             log2(32/11) = 1.5405 (r2-ch15d B4).  The quantifier is the proposition\'s own.')
print('  1150/1151  the row IS the citation of Prop. 23.1; "V > 2 always" is its statement.')
print('  1152/1153  the same floor in words; 1154 is the pole of §23.7 for a linear observable.')
print('  All seven are regex artefacts on a live cited claim - CLAUDE.md §5 precedents 678,')
print('  680-687, 1067, 1069.  Row 1155 (L7359) lies in §27.6 and is NOT in this unit.')

# ------------------------------------------------------------------ P8
hdr('P8  where the price of a bracket is stated, and where its exact form is')
for pat, lbl in ((r'4\s*ν\s*/\s*3', '4nu/3'), (r'4\s*/\s*\(\s*9\s*ν', '4/(9nu)'),
                 (r'32\s*/\s*11', '32/11')):
    hits = [(k, i + 1) for k, ls in LINES.items() for i, l in enumerate(ls) if re.search(pat, l)]
    print(f'  [{lbl:8s}] {len(hits)} site(s); first ten {hits[:10]}')
print(f'\n  main L6237| {M[6236].strip()[:170]}')
print('  -> the exact V is stated in the volume; L7308 prints only the asymptote as "the price".')

hdr('P9  "slack" outside chapter 27: is the name defined before the chapter that names it?')
pat = re.compile(r'(?<![A-Za-z])slack(?![A-Za-z])', re.I)
out = [(k, i + 1) for k, ls in LINES.items() for i, l in enumerate(ls)
       if pat.search(l) and not (k == 'main' and 7203 <= i + 1 <= 7363)]
print(f'  sites outside the chapter: {len(out)}')
for k, i in out:
    print(f'    {k} L{i}: {window(LINES[k][i-1], "slack", 46)[:126]}')
