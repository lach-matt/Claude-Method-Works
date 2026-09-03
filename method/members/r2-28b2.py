#!/usr/bin/env python3
# r2-28b2.py — chat 151-B (Cowork) — 28b-06 (DEF-143 item 11's NINTH and LAST family; docket 9(b) / 17):
# R.7 prints two blocks of works under "What is not cited, and why", and attaches two sentences to them —
#   L11807  "The companion paper carries the full list; these are the works Chapter 35 rests on."
#   L11820  "every structural object of Chapter 36 is his or older."  (on Montgomery's line)
# READ-ch28b measured that many of the blocks' names have 0 sites in the chapters and marked both sentences
# INFERRED unsupported at the chapter. DEFERRED recorded what is owed in terms: **R3 READS 1721 FIRST, THEN
# DECIDES WHETHER THE BLOCK OR THE CHAPTER CARRIES THE ATTRIBUTION.** This instrument is that reading.
# CONVENTION PROV (new, this chat). A provenance claim PRINTED INSIDE a block but ADDRESSED TO a chapter is a
# claim about the CHAPTER, and is scored over the objects THE CHAPTER NAMES, each dated by the year the block
# gives it — never over the block's own contents. A sentence about a chapter is not an inventory of the list it
# sits in. (The same distinction AY drew for "the works listed above" and DEP for "what rests on it".)
# Chapter bounds follow the CHAT-130 convention r2-ch28b §3 uses and this instrument re-asserts: a chapter runs
# from its heading to the LAST `# APPENDICES` line, never to the member's end.
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
M, R = rd(MAIN), rd(REG)
FAIL = []; DEV = []
def check(tag, got, exp):
    ok = got == exp
    print('   %-68s %-22s %s' % (tag, repr(got), 'OK' if ok else 'EXPECTED ' + repr(exp)))
    if not ok: FAIL.append(tag)
def score(tag, got, exp, tagno):
    ok = got == exp
    print('   %-68s %-22s %s' % (tag, repr(got), 'as printed' if ok else 'DEVIATION (%s) — printed %s' % (tagno, repr(exp))))
    if not ok: DEV.append((tagno, tag, got, exp))

print('r2-28b2.py — 28b-06: read Register 1721 first, then decide whether R.7\'s block or the chapter carries the attribution')
print('members: %s %s | %s %s' % (MAIN, md5(MAIN), REG, md5(REG)))

# ------------------------------------------------------------------------------ §1
hr('§1 THE TWO SENTENCES, THE TWO BLOCKS AND THE TWO CHAPTERS — bounds by scan, chapters under the chat-130 convention')
R7 = [i + 1 for i, l in enumerate(M) if l.strip() == '### R.7 What is not cited, and why']
AP = [i + 1 for i, l in enumerate(M) if l.startswith('# APPENDICES')]
check('`### R.7 What is not cited, and why` heading hits', R7, [11806])
check('`# APPENDICES` hits (the chapter bound is the LAST)', AP, [161, 9937])
def head(tag):
    hits = [i + 1 for i, l in enumerate(M) if re.match(r'^##\s+%s\.\s' % re.escape(tag), l)]
    return hits
h35, h36 = head('35'), head('36')
check('Chapter 35 heading hits', h35, [158, 9716])
check('Chapter 36 heading hits', h36, [159, 9892])
C35 = (h35[-1], h36[-1] - 1); C36 = (h36[-1], AP[-1] - 1)
print('   Chapter 35 L%d–L%d (%d lines) | Chapter 36 L%d–L%d (%d lines)' % (C35[0], C35[1], C35[1] - C35[0] + 1, C36[0], C36[1], C36[1] - C36[0] + 1))
J35 = norm(' '.join(M[C35[0] - 1:C35[1]])); J36 = norm(' '.join(M[C36[0] - 1:C36[1]]))
S35 = [i + 1 for i, l in enumerate(M) if 'these are the works Chapter 35 rests on' in l]
S36 = [i + 1 for i, l in enumerate(M) if 'every structural object of Chapter 36 is his or older' in l]
check('sentence A "these are the works Chapter 35 rests on" sits at', S35, [11807])
check('sentence B "every structural object of Chapter 36 is his or older" sits at', S36, [11820])
check('both sentences sit inside R.7 L11806-L11840 and OUTSIDE both chapters',
      all(11806 <= x <= 11840 and not (C35[0] <= x <= C36[1]) for x in S35 + S36), True)
LB = (11807, 11816); TB = (11818, 11840)
def bullets(lo, hi): return [i for i in range(lo, hi + 1) if M[i - 1].strip().startswith('·')]
BL, BT = bullets(*LB), bullets(*TB)
check('Löwdin block L11807–L11816: bullet works', len(BL), 8)
check('three-body block L11818–L11840: bullet works', len(BT), 21)

# ------------------------------------------------------------------------------ §2
hr('§2 REGISTER 1721, READ FIRST AND IN FULL — what DEFERRED asked for before any decision')
IDX = {}
for i, l in enumerate(R, 1):
    m = re.match(r'^###\s+(\d+)\s*$', l)
    if m: IDX[int(m.group(1))] = i
KS = sorted(IDX)
def span(n):
    s = IDX[n]; return s, next((IDX[k] for k in KS if IDX[k] > s), len(R) + 1) - 1
def rbody(n):
    s, e = span(n); return norm(' '.join(x for x in R[s:e] if x.strip()))
s21, e21 = span(1721)
print('   register 1721 L%d–L%d:' % (s21, e21))
for ln in [x for x in R[s21:e21] if x.strip()]: print('     %s' % norm(ln))
B21 = rbody(1721)
check('1721 states eight questions and seven closed to named owners',
      ('EIGHT ATTRIBUTION QUESTIONS' in B21) and ('seven closed to named owners' in B21), True)
check('1721 says the questions were formed from residue BEFORE deriving, citing §E.5',
      ('formed from residue before deriving' in B21) and ('§E.5' in B21), True)
GRP = re.search(r'named owners: (.*?)\.\*?', B21).group(1).split(', ')
print('   1721 lists %d owner-groups: %s' % (len(GRP), GRP))
print('   THE READING: 1721 records the ATTRIBUTION ACT — questions formed, owners named — and cites §E.5 as')
print('   the method. It is a Register act, and the chapter states the same act in its own words (§3 below).')

# ------------------------------------------------------------------------------ §3
hr('§3 THE THREE-BODY BLOCK — every bullet\'s names and years, read out of the block itself')
Y = r'(?:1[6-9]\d\d|20[0-2]\d)'
NM = re.compile(r"(?<![A-Za-zÀ-ÿ'’\-])([A-ZÀ-Þ][A-Za-zà-ÿ'’\-]{2,})")
STOP = set('''The Novi Comm Acad Sci Petrop Prix Roy Paris Mem Mém Berlin Ann École Norm Sup Trans AMS Arch Ration
Mech Anal Invent Math Nonlinearity Nature CMDA MNRAS Celest Vorlesungen Dynamik Leçons Sbornik USSR Moscow Soc
Amer Monthly Diff Eq Phys Rev Lett Inf Artif Intell Three-Body Problem Unknown Masses Solution Some Die
Mathematischen Hilfsmittel Physikers Springer Chem Int Mol Quantum Handbook'''.split())
def work(i):
    t = re.split(r'\s—\s', re.sub(r'[*_`]', '', M[i - 1]))[0]
    nms = [n for n in NM.findall(t) if n not in STOP]
    yrs = sorted({int(y) for y in re.findall(Y, t)})
    return nms, yrs
BLOCKY = {}
for i in BT:
    nms, yrs = work(i)
    for n in nms:
        if yrs: BLOCKY[n] = max(BLOCKY.get(n, 0), max(yrs))
    print('   L%-6d %-44s %s' % (i, ','.join(nms[:6]), yrs))
MGY = BLOCKY.get('Montgomery', 0)
check("Montgomery's latest year in the block", MGY, 2015)
check('the block carries 2026 works (the companion paper)', max(BLOCKY.values()), 2026)

# ------------------------------------------------------------------------------ §4
hr('§4 WHERE EACH NAME LIVES — Chapter 36, registers 1713–1724, 1721 alone, or nowhere')
def blk(a, b): return norm(' '.join(R[span(a)[0]:span(b)[1]]))
TBREG = blk(1713, 1724); ELSE = blk(1713, 1720) + ' ' + blk(1722, 1724)
def has(txt, nm): return bool(re.search(r'(?<![A-Za-zÀ-ÿ])' + re.escape(nm), txt))
NAMES = sorted(BLOCKY)
inch = [n for n in NAMES if has(J36, n)]
nowhere = [n for n in NAMES if not has(J36, n) and not has(TBREG, n) and n != 'Lach']
only21 = [n for n in NAMES if not has(J36, n) and has(B21, n) and not has(ELSE, n)]
for n in NAMES:
    print('   %-12s ch36 %-4s 1713–24 %-4s 1721 %-4s  block year %d' %
          (n, 'YES' if has(J36, n) else '.', 'YES' if has(TBREG, n) else '.', 'YES' if has(B21, n) else '.', BLOCKY[n]))
check('block names PRESENT in Chapter 36', inch,
      ['Brudno', 'Chenciner', 'Euler', 'Jacobi', 'Lagrange', 'Maupertuis', 'Montgomery', 'Moore', 'Painlevé', 'Saari'])
check('block names in NEITHER Chapter 36 nor 1713–1724 (READ-ch28b measured nine)', nowhere,
      ['Arnold', 'Chazy', 'Fleischer', 'Hsiang', 'Knauf', 'Kolmogorov', 'McGehee', 'Nash', 'Straume'])
print('   names living ONLY in 1721 within 1713–1724: %d — %s' % (len(only21), only21))
score('the block names living only in Register 1721 number as the record lists them', len(only21), 8, '28b-08')
print('   The record\'s list is Marchal, Bozis, Monaghan, Stone, Leigh, Kol, Moser, Alekseev. Measured it is a')
print('   SUPERSET: Baker, Dechter, Montanari and Pixley — the constraint-consistency line L11839 — are in')
print('   1721\'s tenth owner-group and in no other entry of 1713–1724 and not in Chapter 36.')

# ------------------------------------------------------------------------------ §5
hr('§5 CONVENTION PROV — sentence B scored over the objects CHAPTER 36 NAMES, not over the block it sits in')
newer_in = sorted(n for n in inch if BLOCKY[n] > MGY)
newer_blk = sorted(n for n in NAMES if n not in inch and BLOCKY[n] > MGY)
print('   Chapter 36 names %d of the block\'s works. Newest year among them: %d (Montgomery\'s own).'
      % (len(inch), max(BLOCKY[n] for n in inch)))
print('   Works in the block NEWER than Montgomery: %s' % newer_blk)
check('every one of those newer works is ABSENT from Chapter 36', [n for n in newer_blk if has(J36, n)], [])
score('"every structural object of Chapter 36 is his or older", scored on Chapter 36', len(newer_in), 0, '28b-07')
print('   MEASURED TRUE OF THE CHAPTER. Not one object Chapter 36 names post-dates Montgomery; the six works')
print('   that do — %s — live in the block and in no part of the chapter.' % ', '.join(newer_blk))
xia = [i + 1 for i, l in enumerate(M) if C36[0] <= i + 1 <= C36[1] and 'Xia' in l]
check('Chapter 36\'s only other dated outsider is Xia 1992, in §36.5\'s disclaimer', xia, [9930])
check('Xia appears nowhere in the three-body block', 'Xia' in norm(' '.join(M[TB[0] - 1:TB[1]])), False)

# ------------------------------------------------------------------------------ §6
hr('§6 SENTENCE A — the Löwdin block against Chapter 35 and registers 1701–1712')
LWREG = blk(1701, 1712)
PRIOR = [i for i in BL if 'Lach' not in work(i)[0]]
inC35 = 0
for i in BL:
    nms, yrs = work(i)
    own = 'Lach' in nms
    c = (not own) and any(has(J35, n) for n in nms)
    if c: inC35 += 1
    print('   L%-6d %-30s Chapter 35 %-4s 1701–12 %-4s%s'
          % (i, ','.join(nms[:4]), 'YES' if c else '.', 'YES' if any(has(LWREG, n) for n in nms) else '.',
             '   (this work\'s own companion paper, not prior art)' if own else ''))
check('the block carries one non-prior-art bullet, the companion paper', len(BL) - len(PRIOR), 1)
check('Madelung is in NEITHER Chapter 35 nor registers 1701–1712',
      (not has(J35, 'Madelung')) and (not has(LWREG, 'Madelung')), True)
check('Koelling, Harmon, Gerratt and Mills are absent from Chapter 35 but present in 1701–1712',
      [n for n in ('Koelling', 'Harmon', 'Gerratt', 'Mills') if has(J35, n) or not has(LWREG, n)], [])
check('the chapter names the companion paper by title', 'The Löwdin Solution' in J35, True)
score('"these are the works Chapter 35 rests on" — prior-art bullets the chapter names', inC35, len(PRIOR), '28b-06')
print('   Four of the seven prior-art works. The chapter rests on Löwdin 1950 and 1969, Griffin–Andrew–Cowan and')
print('   Pulay 1969, and names the companion by title; Koelling & Harmon, Gerratt & Mills and Madelung it')
print('   never names — and Madelung is in no Register entry of the run either.')

# ------------------------------------------------------------------------------ §7
hr('§7 THE EIGHT AND THE SEVEN — read across §36.2, §36.3, 1719 / 1720 and 1721; ENGAGED, NOT SCORED')
p362 = [i + 1 for i, l in enumerate(M) if 'Eight attribution questions, eight closed' in l]
p363 = [i + 1 for i, l in enumerate(M) if 'Eight residues were formed into questions' in l]
check('§36.2 states "Eight attribution questions, eight closed"', p362, [9902])
check('§36.3 states "Seven belonged to others; the eighth"', bool(p363) and 'Seven belonged to others' in M[p363[0] - 1], True)
check('1719 records the eighth as a WITHDRAWAL and 1720 gives it to Lagrange 1770 as prior art',
      ('withdrawn' in rbody(1719)) and ("Lagrange's resolvent method (1770)" in rbody(1720)), True)
check('1721\'s owner list names neither Lagrange nor Euler', [n for n in ('Lagrange', 'Euler') if has(B21, n)], [])
print('   §36.2 (eight closed) and §36.3 (seven to others, the eighth classical) RECONCILE, and 1721\'s "seven')
print('   closed to named owners" agrees with §36.3: the eighth went to Lagrange 1770 at 1720, outside 1721\'s')
print('   list. What does NOT resolve on the bundle is 1721\'s own arithmetic — %d owner-groups printed against' % len(GRP))
print('   seven closures. A question may close to more than one group, and the audit-7 ledger that maps question')
print('   to owner is not a member of this build, so THE READING DOES NOT DECIDE IT and does not score it.')

# ------------------------------------------------------------------------------ §8
hr('§8 CENSUS — rows in the ranges this reading engaged')
print('   engaged: main L%d–L%d (Chapter 35), main L%d–L%d (Chapter 36), main L11806–L11840 (R.7),' % (C35[0], C35[1], C36[0], C36[1]))
print('            reg L%d–L%d (registers 1701–1712) and L%d–L%d (registers 1713–1724)'
      % (span(1701)[0], span(1712)[1], span(1713)[0], span(1724)[1]))
print('   main 1199 / 1200  C9 at L9902 / L9910 — closed in the ch17e / tb1 line as not defects; earlier governs (G0b)')
print('   reg  1460         C9 "never" at L6367 (register 1706) — closed earlier, not a defect; earlier governs (G0b)')
print('   reg  1546         C13-HANDLE-LEAK `3B.tri` at L6403 (register 1716) — CLOSED HERE as a defect: this')
print('                     reading read 1716 entire and the handle is in the body it read; the class is ruled')
print('                     (26b-10, ruling 46, docket 28) with census 1536 and 1556 closed on the same form.')
print('   R.7 L11806–L11840 carries NO census row of its own.')

# ------------------------------------------------------------------------------ verdict
hr('VERDICT')
print('   28b-06 STANDS, AND THE QUESTION DEFERRED PUT TO R3 IS ANSWERED: **THE BLOCK CARRIES THE ATTRIBUTION,')
print('   NOT THE CHAPTER.** Register 1721, read first as DEFERRED required, records the attribution act itself —')
print('   eight questions formed from residue before deriving, seven closed to named owners — and Chapter 36')
print('   states that same act in its own words at §36.3 (*§E.5 and audit 7 supplied the ledger … Seven belonged')
print('   to others*), citing registers 1718 and 1722–1723. The chapter therefore neither needs nor makes R.7\'s')
print('   claim; R.7 makes it about the chapter.')
print('   28b-07 NEW, AND IT FALLS FOR THE BOOK. Scored under CONVENTION PROV on the objects Chapter 36 actually')
print('   names, "every structural object of Chapter 36 is his or older" is **TRUE**: of the %d block works the' % len(inch))
print('   chapter uses, not one post-dates Montgomery, and the %d that do — %s —' % (len(newer_blk), ', '.join(newer_blk)))
print('   appear in no part of Chapter 36. What over-reaches is the BLOCK\'s scope, not the sentence, and not the')
print('   chapter. R3: the sentence stands; the block either narrows to the works the chapters use or stops')
print('   saying the chapters rest on it.')
print('   28b-08 NEW. The block names living only in Register 1721 within 1713–1724 number **%d**, not the eight' % len(only21))
print('   the record lists: Baker, Dechter, Montanari and Pixley — L11839\'s constraint-consistency line — sit in')
print('   1721\'s tenth owner-group, in no other entry of the run, and in no part of Chapter 36. The record\'s')
print('   list is a subset, corrected here.')
print('   SENTENCE A does not fare as well: only %d of the Löwdin block\'s %d prior-art works have their names in' % (inC35, len(PRIOR)))
print('   Chapter 35, and Madelung is in neither the chapter nor registers 1701–1712 — the one work of either')
print('   block with no home anywhere in the record.')
print('\nDEVIATIONS RECORDED (findings, not instrument faults):')
for t, tag, got, exp in DEV: print('   %-8s %-58s measured %s against printed %s' % (t, tag, repr(got), repr(exp)))
print('\n%s' % ('FAIL: ' + '; '.join(FAIL) if FAIL else 'ALL INSTRUMENT CHECKS OK — %d deviations recorded' % len(DEV)))
sys.exit(1 if FAIL else 0)
