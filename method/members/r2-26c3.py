#!/usr/bin/env python3
# r2-26c3.py — SUCCESSOR to r2-26c2.py. Two changes, both in §4, and nothing else moves.
# r2-26c2 is seated and is never edited in place (chat 68); W-260 holds it with this successor owed.
#
# CHANGE 1 — THE PINNED LIST THE RECORD GREW INTO. r2-26c2 asserts the registers naming the method
# ratio are exactly [296]. W-260 then seated register 1868, which names it, so the true answer is
# [296, 1868] and the predecessor exits non-zero. Neither figure is wrong: a pinned list cannot
# survive the record growing into it. The replacement asserts the PROPERTY the check was for —
# register 296 still names it, and 296 still carries no numeral — and REPORTS the full set instead of
# pinning its length. A later entry naming the ratio extends the report and breaks nothing.
#
# CHANGE 2 — AND THE SAME GROWTH SILENTLY ANSWERED 26c-01 FOR THE WRONG REASON. r2-26c2 scores 26c-01
# by asking whether any register naming the method ratio carries a numeral. Register 1868 names it and
# carries numerals — 4.21, 0.192, 0.705 — but those are the WITHDRAWAL ratio's value, quoted as the
# contrast, beside register numbers and deviation tags the occurrence rule does not strip. On the
# seated bundles the predecessor therefore scores 26c-01 'as printed', i.e. resolved, when 1868 states
# in its own words that the method ratio 'has no such entry' and is 'given no figure anywhere'. THE
# TEST FOUND A PATTERN WHERE THE MATERIAL SAYS THE OPPOSITE. The replacement reads attribution the way
# the corpus writes it: an establishing entry states the value IN ITS HEADLINE and names ONE of the two
# ratios there. It is calibrated on a positive control — the withdrawal ratio, which the corpus does
# establish — so it is not a test that cannot fail: it must find 297 (1 : 1) and 1762 (4.21 : 1) before
# its silence about the method ratio means anything.
#
# AND 26c-01 IS NOT AN OPEN DEVIATION ANY MORE, NOR IS IT REPAIRED. Register 1868 is its record. The
# measurement still holds — no entry establishes the method ratio — and the Register now says so. That
# is 'recorded, never repaired' reaching its ordinary end, and the status is printed as RECORDED rather
# than flattened into either 'as printed' or a standing deviation. The four W-260 carries forward —
# 26b-02, 26b-03, 26c-02, 26c-03 — are untouched.
#
# ---- inherited header, r2-26c2.py ----
# r2-26c2.py — chat 153 — SUCCESSOR to r2-26c.py, re-anchored. Identical measurements; one pin moves.
# r2-26c pinned the rebuilt Appendix F's first line to the literal 11222, which the +8 shift moved to 11230.
# The replacement is NOT the resolver's own value — that would be a test that cannot fail, the very
# class §4.6 names. It is an INDEPENDENT resolution of the same site, so the two can disagree and the
# check still catches a mis-read. Output on the pre-shift bundles is unchanged, because both agree there.
# r2-26c is seated and is never edited in place (chat 68).
# PROVED by tools/proveanchor.py: reproduces r2-26c.out byte-exact on the pre-shift bundles (G0c).
# r2-26c.py — chat 151-B (Cowork) — 26b-02 and 26b-03 (DEF-143 item 11's sixth family; docket 9(b) / 23 / 35 / 12).
# §32.1.3 L8961 *§F.4.1's withdrawal ratio measures and does not excuse* and §32.1.4.1 L9023 *the ratios of F.4.1*
# cite F.4.1 for content F.4.1 declares withdrawn; §32.1.4's row *Appendix F, the numbers  3  33  thirty-three*
# counts an appendix rebuilt on a different domain (register 1780).
# WHAT WAS OWED. READ-ch26a §29 recorded that the 188 only-PP lines of the withdrawn appendix "were not read line
# by line (the entry is the witness; INFERRED that every removed figure has a Register home — R3's pass on
# 26b-02 / 26b-03 reads them)". This instrument replaces that inference with a measurement, and scores it against
# the book's own standard for a withdrawal rather than against a standard of this instrument's invention:
# register 374 states the protocol at §2.21 — ANY FIGURE WITHDRAWN MUST HAVE ITS DATA REPRESENTED ANOTHER WAY.
# FAULTS SELF-CAUGHT AND NAMED (this instrument's, not the book's):
#   fault 1: the ratio tokens were first counted CASE-SENSITIVELY, which returned 0 sites for *method ratio* and
#            produced a finding that F.4.1's sentence had no referent. Register 296 prints THE METHOD RATIO in
#            capitals. The finding was withdrawn before it was recorded; all token counts here are case-folded.
#   fault 2: *withdrawal ratio* was first counted over the whole rebuilt unit, which counts F.4.2's own HEADING
#            and is not content. Headings and body are separated below.
#   fault 3: the only-PP count was first taken over raw lines, giving 189 against the record's 188. The record's
#            figure is r2-ch26b §0's convention — body lines only, heading lines excluded, as a SET. Both are
#            printed; the record's convention is the one scored.
# Book-versus-record deviations go through score() and never through the integrity checker check().
# Reads MEMBERS by name (never a bundle path); PP is Prints & Proofs, the pre-withdrawal witness.
# Deterministic: no wall clock, no randomness.
import os, re, sys, hashlib, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
def load(name):
    s = importlib.util.spec_from_file_location(name.replace('-', '_'), os.path.join(H, name + '.py'))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
r2lib = load('r2lib')
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
def md5(n): return hashlib.md5(open(os.path.join(H, n), 'rb').read()).hexdigest()[:8]
def hr(t): print('\n== ' + t)

MAIN, REG = 'The_Method_1_6-2.md', 'The_Method_1_6___The_Register-2.md'
VOLS = [MAIN, REG, 'The_Method_1_6___Mathematical_Compendium-2.md', 'The_Method_1_6___The_Physics_Compendium-2.md',
        'The_Method_1_6___Spectra_Compendium-2.md', 'The_Method_1_6___The_Index_of_Indices-2.md']
M, R = rd(MAIN), rd(REG)
PPN = 'PP_The_Method_1_6.md'
P = (rd(PPN) if os.path.exists(os.path.join(H, PPN))
     else open('/home/claude/' + PPN, encoding='utf-8').read().split('\n'))
def norm(s): return re.sub(r'\s+', ' ', s).strip()
def nvol(v): return v.split('___')[-1].replace('The_Method_1_6-2.md', 'main').replace('-2.md', '')
FAIL = []; DEV = []
def check(tag, got, exp):
    ok = got == exp
    print('   %-66s %-24s %s' % (tag, repr(got), 'OK' if ok else 'EXPECTED ' + repr(exp)))
    if not ok: FAIL.append(tag)
def score(tag, got, exp, tagno):
    ok = got == exp
    print('   %-66s %-24s %s' % (tag, repr(got), 'as printed' if ok else 'DEVIATION (%s) — printed %s' % (tagno, repr(exp))))
    if not ok: DEV.append((tagno, tag, got, exp))

# appf.py's occurrence rule, copied verbatim from r2-ch26a §3: a number in body text or a table, with
# section / register / chapter / figure locators excluded. Defined here because §4 and §5 both score on it.
NUM = re.compile(r'(?<![\w§.])(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?(?![\w.]\d)')
EXCL = re.compile(r'(§\s?[\dA-F.]+|[Rr]egisters?\s+\d+(?:[–-]\d+)?|[Cc]hapters?\s+\d+(?:,\s*\d+)*(?:\s+and\s+\d+)?|F\.\d(?:\.\d)?|E\.\d(?:\.\d)?|\(i{1,3}\))')
def census(lines, base):
    occ = []
    for k, l in enumerate(lines):
        if l.startswith('#') or l.startswith('    '): continue
        for m in NUM.finditer(EXCL.sub(' ', l)): occ.append((base + k, m.group(0)))
    return occ
def numerals(text): return [v for _, v in census([text], 0)]

print('r2-26c.py — 26b-02 / 26b-03: the withdrawn Appendix F, what still cites it, and where its figures went')
print('members: %s md5 %s | %s md5 %s | PP md5 %s'
      % (MAIN, md5(MAIN), REG, md5(REG), hashlib.md5('\n'.join(P).encode()).hexdigest()[:8]))

# ------------------------------------------------------------------ §1
hr('§1 THE TWO UNITS, measured this chat by scan — member line numbers are never carried between chats')
def last_head(lines, text):
    hits = [i for i, l in enumerate(lines, 1) if l.strip().endswith(text) and re.match(r'^#{1,4}\s', l)]
    return hits[-1] if hits else None
FA = last_head(M, 'Appendix F — The numbers, indexed'); GA = last_head(M, 'Appendix G — Transitions, indexed')
U = M[FA - 1:GA - 1]
PF = last_head(P, 'Appendix F — The numbers, indexed'); PE = last_head(P, 'END MATTER')
PU = P[PF - 1:PE - 1]
_fa_alt = [i for i, l in enumerate(M, 1) if re.match(r'^#{1,4}\s+Appendix F\b', l)][-1]
check('rebuilt Appendix F first line', FA, _fa_alt)
check('rebuilt Appendix F line count (to `## Appendix G`)', len(U), 139)
check('PP Appendix F first line', PF, 10761)
check('PP Appendix F line count (to `# END MATTER`)', len(PU), 231)
HEADFORM = re.compile(r'^(#{1,6}\s+|F\.\d(\.\d)?\s+\S)')
rh = [(FA + k, norm(l)) for k, l in enumerate(U) if re.match(r'^#{1,4}\s', l)]
ph = [(PF + k, norm(l)) for k, l in enumerate(PU) if HEADFORM.match(l.strip())]
check('heading lines, rebuilt unit', len(rh), 9)
check('heading-form lines, PP unit', len(ph), 12)
for n, t in rh: print('   L%-6d %s' % (n, t))
print('   ---')
for n, t in ph: print('   P%-6d %s' % (n, t))
print('   PP sections the rebuild does not carry: F.3.2, F.3.3, F.5 (register 1786 renumbered F.3.3 to F.3.1)')

# ------------------------------------------------------------------ §2
hr('§2 THE WITHDRAWN CONTENT — the only-PP lines READ-ch26a named at 188 and did not read')
mb = {l.strip() for l in U if l.strip() and not l.startswith('#')}
pb = {l.strip() for l in PU if l.strip() and not re.match(r'^\s*#', l)}
check('only-PP BODY lines as a set (r2-ch26b §0 convention — the record\'s 188)', len(pb - mb), 188)
raw = [(PF + k, l.strip()) for k, l in enumerate(PU) if l.strip() and l.strip() not in mb]
print('   the same lines positionally, heading-form lines included: %d' % len(raw))
print('   body lines: rebuilt %d, PP %d, shared %d, only-rebuilt %d' % (len(mb), len(pb), len(mb & pb), len(mb - pb)))
check('the two units share no body line', len(mb & pb), 0)

# ------------------------------------------------------------------ §3
hr('§3 26b-02 — F.4.1 declares its content withdrawn; two chapter sentences still cite it for that content')
F41 = [i for i, l in enumerate(M, 1) if l.strip().startswith('### F.4.1')][-1]
F42 = [i for i, l in enumerate(M, 1) if l.strip().startswith('### F.4.2')][-1]
F43 = [i for i, l in enumerate(M, 1) if l.strip().startswith('### F.4.3')][-1]
u41, u42 = M[F41 - 1:F42 - 1], M[F42 - 1:F43 - 1]
body = [l for l in U if not l.startswith('#')]
print('   F.4.1 L%d-L%d (%d lines), F.4.2 L%d-L%d (%d lines)' % (F41, F42 - 1, len(u41), F42, F43 - 1, len(u42)))
check('F.4.1 declares withdrawal in its own words', 'Retained as a reference, withdrawn as content' in ' '.join(u41), True)
check('F.4.2 declares the same', 'Retained as a reference, withdrawn as content' in ' '.join(u42), True)
for tok in ('withdrawal ratio', 'method ratio'):
    check('"%s" in F.4.1 body (case-folded)' % tok, sum(l.lower().count(tok) for l in u41), 0)
check('"withdrawal ratio" in the rebuilt unit BODY (fault 2: headings excluded)',
      sum(l.lower().count('withdrawal ratio') for l in body), 0)
check('"withdrawal ratio" in the rebuilt unit HEADINGS (F.4.2\'s title)',
      sum(l.lower().count('withdrawal ratio') for _, l in rh), 1)
cit = [(i, norm(l)) for i, l in enumerate(M, 1) if 'F.4.1' in l]
out = [i for i, _ in cit if i < FA]
print('   every F.4.1 mention in the main volume:')
for i, t in cit: print('     L%-6d %s' % (i, t[:140]))
check('F.4.1 cited from outside the appendix exactly twice', len(out), 2)
print('   F.4.1 keeps the label so "every reference written to it still resolves". The LABEL resolves; the')
print('   CONTENT the two sentences name does not. That is 26b-02, and it stands.')
score('§32.1.3 cites F.4.1 for a ratio F.4.1 carries', sum(l.lower().count('withdrawal ratio') for l in u41) > 0, True, '26b-02')

# ------------------------------------------------------------------ §4
hr('§4 26c-01 — F.4.1: "the entries that established them stand in the Register". Both ratios, case-folded')
for tok in ('withdrawal ratio', 'method ratio'):
    per = [(nvol(v), sum(l.lower().count(tok) for l in rd(v))) for v in VOLS]
    print('   "%s" across the six volumes (case-folded): %s' % (tok, per))
IDX = {}
for i, l in enumerate(R, 1):
    m = re.match(r'^###\s+(\d+)\s*$', l)
    if m: IDX[int(m.group(1))] = i
KS = sorted(IDX)
def rbody(n):
    s = IDX[n]; e = next((IDX[k] for k in KS if IDX[k] > s), len(R) + 1) - 1
    return norm(' '.join(x for x in R[s:e] if x.strip()))
print('   Register entries carrying either ratio:')
for n in KS:
    b = rbody(n).lower()
    if 'withdrawal ratio' in b or 'method ratio' in b:
        print('     register %-5d withdrawal %d | method %d | numerals with a decimal point %s'
              % (n, b.count('withdrawal ratio'), b.count('method ratio'), re.findall(r'\d+\.\d+', rbody(n))[:6]))
NAMED_M = [n for n in KS if 'method ratio' in rbody(n).lower()]
print('   registers naming the METHOD ratio, reported and NOT pinned to a length: %s' % NAMED_M)
check('register 296 still names the METHOD ratio', 296 in NAMED_M, True)
check('register 296 carries no numeral under the occurrence rule (F.4.1 is a locator, not a value)',
      numerals(rbody(296)), [])
check('register 1762 gives the withdrawal ratio a value', '4.21 : 1' in rbody(1762), True)
print('   READ-ch26a recorded the homes as "Register 296 / 320 / 321 / 1762 (4.21 : 1)". MEASURED: 296 NAMES both')
print('   ratios and carries no figure at all; 320 and 321 carry neither ratio by name; 1762 establishes the')
print('   WITHDRAWAL ratio with a value (4.21 : 1, p 0.192, 0.705 bits). No entry establishes the METHOD ratio.')
print('   F.4.1 says the entries "established them", of both. For one of the two, naming is all there is.')
# An ESTABLISHING entry states the value in its headline and names ONE of the two ratios there. An
# entry naming BOTH is writing about the pair, not establishing either — which is exactly register
# 1868, whose headline quotes the withdrawal ratio's value while saying the method ratio has none.
RATIO_FORM = re.compile(r'\d+(?:\.\d+)?\s*:\s*\d+')
def headline(b):
    m = re.match(r'\s*\*\*(.+?)\*\*', b)
    return m.group(1) if m else ''
def establishing(tok, other):
    out = []
    for n in KS:
        h = headline(rbody(n))
        if tok in h.lower() and other not in h.lower() and RATIO_FORM.search(h):
            out.append((n, RATIO_FORM.findall(h)))
    return out
EST_W = establishing('withdrawal ratio', 'method ratio')
EST_M = establishing('method ratio', 'withdrawal ratio')
print('   POSITIVE CONTROL — entries establishing the WITHDRAWAL ratio in their headline: %s' % EST_W)
print('   entries establishing the METHOD ratio in their headline: %s' % (EST_M or 'NONE'))
check('the control finds the withdrawal ratio established (else the silence below proves nothing)',
      [n for n, _ in EST_W], [297, 1762])
check('no entry establishes the METHOD ratio with a value', EST_M, [])
print('   26c-01 IS RECORDED, NOT OPEN AND NOT REPAIRED. Register 1868 states this finding in the')
print('   Register itself — "one is established and the other is named and never measured". The')
print('   measurement above still holds; the record now carries it. r2-26c2 scored this deviation as')
print('   resolved, because 1868 names the ratio AND carries numerals — the withdrawal ratio\'s 4.21,')
print('   0.192, 0.705, quoted as the contrast. A numeral near a name is not a value for it.')

# ------------------------------------------------------------------ §5
hr('§5 26b-03 — §32.1.4\'s row against the appendix as rebuilt (appf.py occurrence rule, copied from r2-ch26a §3)')
occ_reb, occ_pp = census(U, FA), census(PU, PF)
check('numeral occurrences in the REBUILT unit', [v for _, v in occ_reb], ['6', '12', '24'])
print('   rebuilt: %d occurrences %s' % (len(occ_reb), occ_reb))
print('   PP     : %d occurrences, %d distinct' % (len(occ_pp), len(set(v for _, v in occ_pp))))
rowl = [i for i, l in enumerate(M, 1) if re.search(r'Appendix F, the numbers\s+\d', l)]
check('the §32.1.4 row has one site', len(rowl), 1)
ROW = norm(M[rowl[0] - 1]); print('   §32.1.4 row L%d: %s' % (rowl[0], ROW))
coord, E = re.findall(r'\d+', ROW)[-2:]
check('the row still reads coordinates 3, E 33', (coord, E), ('3', '33'))
check('"thirty-three" stands beside it', 'thirty-three' in ROW, True)
print('   E is *cells named and unoccupied*, so the row is a claim about the appendix\'s number-space and not a')
print('   count of numerals. Both columns were computed on the appendix PP carries — %d numeral occurrences —' % len(occ_pp))
print('   against the %d the rebuilt appendix prints. 26b-03 stands.' % len(occ_reb))
score('§32.1.4\'s row describes the appendix the volume now carries', len(occ_reb) > 3, True, '26b-03')

# ------------------------------------------------------------------ §6
hr('§6 26c-02 — register 375 records a change to §32.1.4 that §32.1.4 did not receive')
print('   register 374: %s' % rbody(374)[:150])
print('   register 375: %s' % rbody(375)[:260])
check('register 374 states the §2.21 protocol', 'ANY FIGURE WITHDRAWN MUST HAVE ITS DATA REPRESENTED ANOTHER WAY' in rbody(374), True)
f55 = [i for i, l in enumerate(M, 1) if 'Fifty-five cells are named' in l]
check('§32.1.4 still writes the total as a number', len(f55), 1)
print('   L%d: %s' % (f55[0], norm(M[f55[0] - 1])))
shape = [i for i, l in enumerate(M, 1) if 'audit set seventeen' in l or 'the numbers index the largest share' in l]
check('register 375\'s replacement shape sentence, in the main volume', shape, [])
r3241 = [i for i, l in enumerate(M, 1) if 'Recomputed now the total is' in l]
print('   §32.1.4.1 L%d: %s' % (r3241[0], norm(M[r3241[0] - 1])))
print('   THREE totals stand at once: §32.1.4 prints fifty-five, §32.1.4.1 and register 373 recompute 48, and')
print('   register 375 states 47 and states the number is no longer written. It is still written.')
score('register 375: §32.1.4\'s fifty-five "is no longer written as a number"', len(f55), 0, '26c-02')

# ------------------------------------------------------------------ §7
hr('§7 26c-03 — THE OWED READING: every figure the withdrawal removed, against register 374\'s §2.21 protocol')
REGL = '\n'.join(R).lower(); ALL = {v: '\n'.join(rd(v)).lower() for v in VOLS}
removed = census([l for _, l in raw], 0)
figs = sorted(set(v for _, v in removed), key=lambda s: (-len(s), s))
print('   figures printed in the only-PP lines: %d occurrences, %d distinct' % (len(removed), len(figs)))
print('   CONVENTION: a figure is REPRESENTED if its string as printed occurs in the Register. A figure of fewer')
print('   than three characters is reported and NOT scored — a bare one- or two-digit match is not evidence of')
print('   representation, and counting it as one would manufacture the result this reading is here to test.')
subst = [f for f in figs if len(f) >= 3]
triv = [f for f in figs if len(f) < 3]
homeless = [f for f in subst if f.lower() not in REGL]
homed = [f for f in subst if f.lower() in REGL]
print('   substantive figures (3+ characters): %d' % len(subst))
print('   REPRESENTED in the Register    : %d %s' % (len(homed), homed))
print('   NOT represented in the Register: %d %s' % (len(homeless), homeless))
print('   short figures, reported not scored: %d %s' % (len(triv), triv))
for f in homeless:
    where = [nvol(v) for v in VOLS if f.lower() in ALL[v]]
    print('     %-12s no Register site; volumes carrying the string: %s' % (f, where or 'none'))
print('   READ-ch26a §29 inferred that every removed figure has a Register home. It is now MEASURED.')
score('READ-ch26a §29\'s inference: every removed figure has a Register home', homeless, [], '26c-03')

# ------------------------------------------------------------------ verdict
hr('VERDICT')
print('   26b-02 STANDS. F.4.1 carries neither ratio in its body and declares its content withdrawn, while')
print('     §32.1.3 and §32.1.4.1 cite it for that content. The label resolves; the claim does not.')
print('   26b-03 STANDS. The rebuilt unit prints 3 numeral occurrences (6, 12, 24) against PP\'s %d, and' % len(occ_pp))
print('     §32.1.4\'s row and its fifty-five total were computed on the appendix that was withdrawn.')
print('   26c-01 RECORDED at register 1868, and still true. F.4.1 says the entries that established its TWO')
print('     ratios stand in the Register. The control finds the withdrawal ratio established at 297 (1 : 1)')
print('     and 1762 (4.21 : 1); NO entry establishes the method ratio. Register 296 and register 1868 name')
print('     it, 296 carries no figure, and 1868 is the entry that records this very absence. The finding is')
print('     in the Register now — recorded, never repaired — so it is no longer an open deviation.')
print('   26c-02 NEW, and the largest of the four. Register 375 records that §32.1.4\'s fifty-five "is no longer')
print('     written as a number" and is replaced by a shape sentence. The number is still written at L%d and' % f55[0])
print('     the shape sentence is in no volume; 375\'s own 47 disagrees with 373\'s and §32.1.4.1\'s 48. A change')
print('     the Register records and the volume did not receive is the mirror of a silent change, and is why')
print('     26b-03\'s row is still standing.')
print('   26c-03 is the reading owed by READ-ch26a §29, measured rather than inferred, against the book\'s own')
print('     standard at register 374 rather than a standard of this instrument\'s invention.')
print('\nDEVIATIONS RECORDED (findings, not instrument faults):')
for t, tag, got, exp in DEV: print('   %-8s %-58s measured %s against printed %s' % (t, tag, repr(got), repr(exp)))
print('\n%s' % ('FAIL: ' + '; '.join(FAIL) if FAIL else 'ALL INSTRUMENT CHECKS OK — %d deviations recorded' % len(DEV)))
sys.exit(1 if FAIL else 0)
