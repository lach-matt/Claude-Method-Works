#!/usr/bin/env python3
# r2-28a5.py — R4 — SUCCESSOR to r2-28a4.py after register 1891 removed six generated bibliography rows.
# r2-28a4 is seated and never edited in place (chat 68); it is superseded, not withdrawn, and it is HELD in the
# live set with this file as the successor it was owed (W-306, W-308).
#
# WHAT MOVED, AND WHY IT MOVED A CHECK RATHER THAN A SCORE. Three of r2-28a4's INTEGRITY checks pin the
# bibliography's extent: that the sentence prints "162 works", that the table holds 162 DATA rows, and that the
# block states 162 beside the prior 172. Register 1891 restates the count at 156, so all three fail on the build
# their own subject justified — the same shape r2-28a4 itself was written for, when ruling (a) turned "Fifty-nine"
# into data. THE CHECKS RECORD RATHER THAN RAISE, so r2-28a4 runs to completion and would re-bank carrying its
# own EXPECTED 162 lines: banking an instrument's self-reported failure as the record. It was held instead.
#
# WHAT THE REPAIR WAS. The bibliography is generated, and the generator pairs a name with a year up to ninety
# characters away, reading the source and check fields as one — so `src`'s last name takes `check`'s first year.
# Five rows were a real author carrying a neighbouring citation's year (Pauli at Bohr's 1913 and at Seaton's 1958,
# Racah at Freuder's 1982, Shannon at Birkhoff's 1937) or a title word read as an author (Moebius, from Rota's
# 1964); a sixth was one paper printed as two rows and is merged under the full-author-list rule. 162 - 5 - 1 = 156.
#
# AND ONE MEASURED FIGURE MOVES WITH IT. The author-and-year match under CONVENTION AY was 52 on the 162 rows and
# is 51 on the 156: the two merged rows were BOTH matches and became one, and not one of the five removed rows
# was a match. The sentence prints "Fifty-one" and this instrument scores against what it reads, as its
# predecessor does — the figure is DATA, never an assertion.
#
# EVERYTHING ELSE IS r2-28a4's, unchanged and deliberately so: CONVENTION AY, the extractor asserted on fourteen
# named citations before any verdict, the bracket at five tolerances, the reproduction of r2-ch28a's 16, the Janet
# 1928/1929 row that falsifies 1736's "never listed" at one site (28a-09, still open and unruled), and
# 28a-08's surname-overlap bound. Register 1736's fifty-nine remains a 172-ROW DATUM and is not withdrawn here.
# r2-28a2.py — chat 151-B (Cowork) — 28a-06 (DEF-143 item 11's EIGHTH family; docket 17 / 37):
# main L11849 "Fifty-nine of them are the works listed above" sits in the same sentence as "162 works, 1669 to 2026".
# READ-ch28a recorded 28a-06 on a SURNAME-OVERLAP BOUND of 16 of 162 and said so; DEFERRED owed R3 the
# AUTHOR-AND-YEAR match on the 162 rows before the figure is kept. This instrument is that match.
# Register 1736 is the source of the figure and says so in terms: it matched the compendium at "172 works",
# by author and year, found fifty-nine shared, and removed ten rows afterwards. **1736's fifty-nine is a
# 172-ROW DATUM.** It is a recorded finding and is NOT withdrawn here. What is measured here is the present
# text: the match on the 162 rows the volumes now carry.
# CONVENTION AY (new, this chat). "The works listed above" is the References unit from its heading down to the
# line before the paragraph that makes the claim — a sentence about a list is not an entry in it. An MC row
# MATCHES if any surname in its `work` cell appears in that region paired with the row's own year, where the
# pairing is read POSITIONALLY: each parenthesised year takes the author surnames of the window before it, and
# a window with no surname CARRIES the previous window's authors, which is the citation form this list uses
# ("Saari, D. G. (1971). Trans. AMS 162, 267; (1973) 181, 351; (1984) J. Diff. Eq. 55, 300"). A surname is a
# capitalised token followed by a comma-and-capital, an ampersand, "and", or a parenthesised year — journal
# abbreviations ("Arch. Ration. Mech. Anal.") are followed by a period and are excluded by construction.
# The extractor is ASSERTED on fourteen named citations BEFORE any verdict is printed, and asserted to admit
# no journal token as an author. Rows the reading cannot decide are carried as NEAR (SUBJ, chat 148).
# Book-versus-record deviations go through score() and never through the integrity checker check().
# Reads MEMBERS by name (never a bundle path). Deterministic: no wall clock, no randomness.
import os, re, sys, hashlib, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
def load(name):
    s = importlib.util.spec_from_file_location(name.replace('-', '_'), os.path.join(H, name + '.py'))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
r2lib = load('r2lib')
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
def md5(n): return hashlib.md5(open(os.path.join(H, n), 'rb').read()).hexdigest()[:8]
def hr(t): print('\n== ' + t)
def norm(s): return re.sub(r'\s+', ' ', s).strip()

MAIN, REG = 'The_Method_1_6-2.md', 'The_Method_1_6___The_Register-2.md'
MCF = 'The_Method_1_6___Mathematical_Compendium-2.md'
M, R, C = rd(MAIN), rd(REG), rd(MCF)
FAIL = []; DEV = []
def check(tag, got, exp):
    ok = got == exp
    print('   %-66s %-24s %s' % (tag, repr(got), 'OK' if ok else 'EXPECTED ' + repr(exp)))
    if not ok: FAIL.append(tag)
def score(tag, got, exp, tagno):
    ok = got == exp
    print('   %-66s %-24s %s' % (tag, repr(got), 'as printed' if ok else 'DEVIATION (%s) — printed %s' % (tagno, repr(exp))))
    if not ok: DEV.append((tagno, tag, got, exp))

print('r2-28a5.py — 28a-06 after ruling (a): does the author-and-year match on the 156 rows give the figure the sentence prints?')
print('members: %s %s | %s %s | %s %s' % (MAIN, md5(MAIN), REG, md5(REG), MCF, md5(MCF)))

# ------------------------------------------------------------------------------ §1
hr('§1 THE TWO LISTS, located by scan this chat — the claim paragraph is EXCLUDED from the list it is about')
rf = [i + 1 for i, l in enumerate(M) if re.match(r'^#{1,3} References\b', l)]
S = rf[-1]
CLAIM = [i + 1 for i, l in enumerate(M) if "The companions' own bibliographies" in l][0]
_rf_alt = [i for i, l in enumerate(M, 1) if l.strip().rstrip(':').endswith('References') and l.startswith('#')]
check('main `References` heading hits (the unit is the LAST, as r2-ch28a §0 takes it)', rf, _rf_alt)
_claim_alt = [i for i, l in enumerate(M, 1) if "companions' own bibliographies" in l][0]
check('the claim paragraph "The companions\' own bibliographies" begins at', CLAIM, _claim_alt)
print('   entry region L%d–L%d (%d lines); the claim paragraph L%d–L%d is read, never matched' % (S, CLAIM - 1, CLAIM - S, CLAIM, len(M)))
for i in range(CLAIM, min(CLAIM + 7, len(M) + 1)): print('   %6d %s' % (i, M[i - 1].strip()))
SENT = norm(' '.join(M[CLAIM - 1:CLAIM + 7]))
check('the sentence prints "156 works"', '156 works' in SENT, True)
WORDS = {'fifty-nine': 59, 'fifty-two': 52, 'fifty-one': 51, 'fifty-five': 55, 'fifty-seven': 57, 'fifty-eight': 58, 'seventy': 70, 'sixty': 60, 'fifty': 50}   # 'fifty-one' added by this successor: register 1891 moved the printed figure and the predecessor's table could not read it
fig = re.search(r'\b([A-Z][a-z]+(?:-[a-z]+)?) of them are the works listed above', SENT)
check('the sentence prints a figure as a word before "of them are the works listed above"', bool(fig) and fig.group(1).lower() in WORDS, True)
PRINTED = WORDS[fig.group(1).lower()]
print('   the printed figure, read as DATA: %s -> %d' % (fig.group(1), PRINTED))
prior = re.search(r'\((fifty-nine) of the 172 rows matched at register 1736', SENT)
print('   the 172-row figure kept beside it: %s' % ('yes — "%s"' % prior.group(0) if prior else 'no'))
check('the sentence names register 1736 as its source', 'register 1736' in SENT, True)

bh = [i + 1 for i, l in enumerate(C) if re.match(r'^#{1,3}\s.*Bibliograph', l, re.I)]
B0 = bh[-1]; B1 = next((j + 1 for j in range(B0, len(C)) if re.match(r'^#{1,2}\s', C[j])), len(C) + 1)
check('MC bibliography heading hits', bh, [3376])
YEARONLY = re.compile(r'^(1[6-9]\d\d|20[0-2]\d)$')
cells = [[c.strip() for c in re.split(r'(?<!\\)\|', l)[1:-1]] for l in C[B0 - 1:B1 - 1] if l.lstrip().startswith('|')]
ROWS = [c for c in cells if c and YEARONLY.match(c[0])]
check('MC bibliography L%d–L%d: DATA rows (year | work | objects)' % (B0, B1 - 1), len(ROWS), 156)
check('every DATA row has exactly three cells', sorted({len(c) for c in ROWS}), [3])
check('MC year range as the block prints it (1669–2026)', (min(int(c[0]) for c in ROWS), max(int(c[0]) for c in ROWS)), (1669, 2026))
check('the block states its own count and BOTH prior ones', ('156 works' in C[B0 + 3]) and ('162' in C[B0 + 3]) and ('172' in C[B0 + 3]), True)

# ------------------------------------------------------------------------------ §2
hr('§2 REGISTER 1736 — the source of the figure, read in full; its fifty-nine is a 172-ROW datum')
IDX = {}
for i, l in enumerate(R, 1):
    m = re.match(r'^###\s+(\d+)\s*$', l)
    if m: IDX[int(m.group(1))] = i
KS = sorted(IDX)
def span(n):
    s = IDX[n]; return s, next((IDX[k] for k in KS if IDX[k] > s), len(R) + 1) - 1
s1736, e1736 = span(1736)
body = norm(' '.join(x for x in R[s1736:e1736] if x.strip()))
print('   register 1736 L%d–L%d: %s' % (s1736, e1736, body[:260]))
check('1736 says the match was made against "172 works"', '172 works' in body, True)
check('1736 says the match was by author and year', 'by author and year' in body, True)
check('1736 states the shared count as fifty-nine', 'fifty-nine shared' in body, True)
check('1736 records the ten removals and the restated count 162', ('All ten removed' in body) and ('restated at 162' in body), True)
print('   1736 is a RECORDED FINDING about a 172-row list and is not withdrawn here (chat-67 hold).')

# ------------------------------------------------------------------------------ §3
hr('§3 CONVENTION AY — the extractor, ASSERTED on fourteen named citations before any verdict is printed')
Y = r'(?:1[6-9]\d\d|20[0-2]\d)'
PAR = re.compile(r'\((%s)([a-z]?)((?:\s*[,–—-]\s*(?:%s[a-z]?|\d{2}|[a-z]))*)\)' % (Y, Y))
AUT = re.compile(r"(?<![A-Za-zÀ-ÿ'’\-])([A-ZÀ-Þ][A-Za-zà-ÿ'’\-]{2,})(?=\s*(?:,\s*[A-ZÀ-Þ]|\s*&|\s+and\b|\s*\(%s))" % Y)
NM = re.compile(r"(?<![A-Za-zÀ-ÿ'’\-])([A-ZÀ-Þ][A-Za-zà-ÿ'’\-]{2,})")
STOP = {'The', 'Problem', 'Solution', 'Unknown', 'Masses'}
def yrs(m): return [int(m.group(1))] + [int(t) for t in re.findall(Y, m.group(3) or '')]
def pairs(lo, hi):
    P = set()
    for j in range(lo, hi):
        l = M[j - 1]
        if not l.strip() or l.startswith('#'): continue
        l = re.split(r'\s—\s|\s--\s', re.sub(r'^\s*[·•]\s*', '', re.sub(r'[*_`]', '', l)))[0]
        prev = 0; last = set()
        for m in PAR.finditer(l):
            nms = {a.group(1) for a in AUT.finditer(l[prev:m.start()] + ' (%d)' % yrs(m)[0])}
            use = nms or last
            if nms: last = nms
            for n in use:
                for y in yrs(m): P.add((n, y))
            prev = m.end()
    return P
AY = pairs(S, CLAIM)
print('   (surname, year) pairs in the entry region: %d over %d distinct surnames' % (len(AY), len({n for n, _ in AY})))
ASSERT = [('Saari', [1971, 1973, 1984]), ('Montgomery', [1998, 2000, 2002, 2014, 2015]), ('Kol', [2021, 2023]),
          ('Monaghan', [1976, 1978]), ('Moser', [1962, 1973]), ('Jacobi', [1837, 1842]), ('Lagrange', [1770, 1772]),
          ('Griffin', [1969, 1971]), ('Cowan', [1969, 1971]), ('Alekseev', [1968]), ('Löwdin', [1950, 1969]),
          ('Candelas', [2007]), ('Huang', [2019]), ('Euler', [1767])]
miss = []
for n, exp in ASSERT:
    got = sorted({y for a, y in AY if a == n})
    if not set(exp) <= set(got): miss.append((n, exp, got))
    print('   %-12s %s' % (n, got))
check('every asserted citation is read with all of its years', miss, [])
JUNK = ('Arch', 'Anal', 'Mech', 'Ration', 'Trans', 'Phys', 'Chem', 'Math', 'Sci', 'Acad', 'Rev', 'Invent',
        'Celest', 'Novi', 'Comm', 'Prix', 'Roy', 'Paris', 'Petrop', 'Ann', 'Norm', 'Sup', 'Nonlinearity', 'JHEP')
check('no journal abbreviation is admitted as an author', sorted({n for n, _ in AY if n in JUNK}), [])
def cn(w): return {n for n in NM.findall(re.sub(r'\*[^*]*\*', ' ', w)) if n not in STOP}
check('every MC row yields at least one surname', [c[1] for c in ROWS if not cn(c[1])], [])

# ------------------------------------------------------------------------------ §4
hr('§4 THE MATCH — author AND year on the 156 rows, against the figure the sentence prints')
UNS = {n for n, _ in AY}
MATCH = [c for c in ROWS if any((n, int(c[0])) in AY for n in cn(c[1]))]
SNM = [c for c in ROWS if cn(c[1]) & UNS]
for c in MATCH: print('   MATCH  %s  %s' % (c[0], c[1][:56]))
def tol(k):
    T = {(n, y + d) for n, y in AY for d in range(-k, k + 1)}
    return sum(1 for c in ROWS if any((n, int(c[0])) in T for n in cn(c[1])))
print('\n   author AND year (exact) %d | ±1 %d | ±2 %d | ±3 %d | ±5 %d | surname only %d | of %d rows'
      % (len(MATCH), tol(1), tol(2), tol(3), tol(5), len(SNM), len(ROWS)))
print('   no year tolerance up to ±5 reaches fifty-nine, 1736\'s 172-row figure: %s' % [k for k in (0, 1, 2, 3, 5) if tol(k) == 59])
check('dropping the year entirely OVERSHOOTS fifty-nine', len(SNM) > 59, True)
score('the figure the sentence prints is the author-and-year match on the 156 rows', len(MATCH), PRINTED, '28a-06')
print('   1736\'s fifty-nine is bracketed by this reading: %d (author and year) < 59 < %d (surname alone); it is a' % (len(MATCH), len(SNM)))
print('   172-row datum and the sentence now says so beside the 162-row figure (register 1809).')

# ------------------------------------------------------------------------------ §5
hr('§5 THE PRIOR PROBE REPRODUCED — what "16 of 162" was a bound on')
def old_surnames(lines):
    s = set()
    for l in lines:
        for m in re.finditer(r"(?<![A-Za-z'’\-])([A-Z][a-zäöüéèçøÅ'’\-]{2,})(?=\s*(?:,\s*[A-Z]\.|\(|&|and\b|,|–|—|\s+\d{4}))",
                             re.sub(r'[*_`]', '', l)): s.add(m.group(1))
    return s
U = M[S - 1:]
OLDU = old_surnames([l for l in U if not l.startswith('#')])
RAW = ['| %s | %s | %s |' % tuple(c) for c in ROWS]
old_hit = [c for c, l in zip(ROWS, RAW) if old_surnames([l]) & OLDU]
old_none = [c for c, l in zip(ROWS, RAW) if not old_surnames([l])]
# 16 -> 17: the merged row `Deville, Barette & Van Hentenryck` yields a surname to r2-ch28a's extractor
# where the two single-name rows it replaces did not.  The predecessor's 16 is a 162-row datum.
check('r2-ch28a §4\'s surname bound on the 156 rows (16 on the 162)', len(old_hit), 17)
check('every row it caught carries an ampersand or a comma in its `work` cell',
      sorted({bool(re.search(r'[&,]', c[1])) for c in old_hit}), [True])
# 123 -> 116, and it is exactly accounted: five removed rows were single-name and yielded none, and the
# merge turned two more into one row that does.  123 - 5 - 2 = 116.
check('rows from which that extractor gets NO surname at all (123 on the 162)', len(old_none), 116)
print('   The MC table prints a BARE surname ("| 1669 | Newton |"); that extractor requires a following')
print('   initial, bracket, ampersand, comma or dash, so it reads nothing from %d of %d rows. Its "16" counts' % (len(old_none), len(ROWS)))
print('   MULTI-AUTHOR ROWS, not overlap. Properly extracted the surname-only overlap is %d of %d.' % (len(SNM), len(ROWS)))
score('"16 of 162" is a bound on the surname overlap', len(SNM), 16, '28a-08')

# ------------------------------------------------------------------------------ §6
hr('§6 "THE REST … THIS VOLUME NEVER LISTED" — census 1463\'s C9 word, taken directly')
CONF = [c for c in SNM if c not in MATCH]
# 18 -> 16: two of the five removed rows were exactly this class — a real author the References carry at
# ANOTHER year, which is the shape register 1891 removed and the shape 1736's author-match could not see.
check('rows whose author is on BOTH lists under a different year (18 on the 162)', len(CONF), 16)
for c in CONF:
    for n in sorted(cn(c[1]) & UNS):
        print('   MC %s %-34s References years for %s: %s' % (c[0], c[1][:34], n, sorted({y for a, y in AY if a == n})[:8]))
jan = [c for c in CONF if 'Janet' in cn(c[1])]
jl = [i + 1 for i, l in enumerate(M) if i + 1 >= S and re.search(r'^\s*Janet, C\. \(1928\)', l)]
check('the compendium carries exactly one Janet row, at 1929', [c[0] for c in jan], ['1929'])
_jl_alt = [i for i, l in enumerate(M, 1) if 'Janet, C. (1928)' in l]
check('the References carry Janet at 1928, one site', jl, _jl_alt)
check('both name the same work (the left-step periodic table)',
      ('left-step' in M[jl[0] - 1]) and ('E.layout' in [c for c in jan][0][2] or 'E.table' in [c for c in jan][0][2]), True)
score('1736\'s "the rest … this volume never listed" holds of every unmatched row', len(jan), 0, '28a-09')
print('   ONE row is decidable and it falsifies the word: the left-step periodic table is listed at L11777 as')
print('   Janet 1928 and carried in the compendium as 1929 — the year disagreement 28a-07 / 16x-06 already')
print('   records. The other %d are consistent with DIFFERENT WORKS by the same author and the reading does' % (len(CONF) - len(jan)))
print('   not decide them; they are carried as NEAR (SUBJ, chat 148), an upper bound, never assigned.')

# ------------------------------------------------------------------------------ §7
hr('§7 CENSUS — rows in the ranges this reading engaged')
print('   engaged: main L%d–L%d (References entire), mc L%d–L%d (the bibliography block), reg L%d–L%d (entry 1736)'
      % (S, len(M), B0, B1 - 1, s1736, e1736))
print('   main 718 / 719  C7 at L11600 — closed in the ch28a unit, not a defect; the earlier line governs (G0b)')
print('   reg 1463        C9 "never" at L6459 — CLOSED HERE as a defect on the Janet row (28a-09)')
print('   mc 387–672      C13-HANDLE-LEAK, 286 rows, the bibliography table\'s `objects` column — CLOSED by r2-bib')
print('                   (CENSUS-CLOSURES-d152.tsv) as one class defect; this reading takes the year and work columns only.')

# ------------------------------------------------------------------------------ verdict
hr('VERDICT')
print('   28a-06 EXECUTED. The author-and-year match on the 156 rows the volumes now carry is %d, and the sentence' % len(MATCH))
print('   prints %d (%s) — re-taken on the list it is printed beside at register 1809, under M\'s ruling (a).' % (PRINTED, fig.group(1)))
print('   Register 1736\'s fifty-nine is a 172-row datum, not withdrawn, and the sentence names it beside the new figure.')
print('   Brackets unchanged: %d / %d / %d / %d / %d at tolerances 0, ±1, ±2, ±3, ±5; %d with the year dropped.' % (tol(0), tol(1), tol(2), tol(3), tol(5), len(SNM)))
print('   28a-08 stands recorded: r2-ch28a §4\'s "16 of 162" reproduces and is a count of multi-author rows (%d rows' % len(old_none))
print('   yield no surname to that extractor); the surname-only overlap is %d of %d. Recorded, not repaired.' % (len(SNM), len(ROWS)))
print('   28a-09 stands open: the Janet 1928 / 1929 row falsifies 1736\'s "never listed" at one site; unruled.')
print('\nDEVIATIONS RECORDED (findings, not instrument faults):')
for t, tag, got, exp in DEV: print('   %-8s %-58s measured %s against printed %s' % (t, tag, repr(got), repr(exp)))
print('\n%s' % ('FAIL: ' + '; '.join(FAIL) if FAIL else 'ALL INSTRUMENT CHECKS OK — %d deviations recorded' % len(DEV)))
sys.exit(1 if FAIL else 0)
