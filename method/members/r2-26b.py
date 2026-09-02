#!/usr/bin/env python3
# r2-26b.py — chat 150 (Cowork) — 26b-04 (DEF-143 item 11's fifth re-derivation; docket 17 / 19):
# Appendix F.3 L11298-L11299 *The work applies this without exception, and several of the corrections the Register
# carries are exactly this rule firing*, scored against the Register itself.
# Chat 139 recorded 0 Register matches BY TOKEN and said so — a token probe is not a reading — and owed R3 a READING
# of the Register for the rule's firings (DEF-139 item 6; READ-ch26a.md's 26b-04 line). This instrument is that
# reading. The rule is taken in the TWO forms F.3 prints (a headline sentence and an elaboration that names the
# mechanism); the population is fixed from the Register's own definition of what an entry is; a candidate pool is
# enumerated by three NAMED nets; and EVERY member of the pool is scored with a deciding phrase the instrument
# asserts is present in that entry's own text, so the scoring is checkable against the file. Members the reading
# cannot decide are reported as an upper bound and never silently assigned (SUBJ, chat 148). The count word
# *several* is scored under a stated BAND, strict and loose, before the sentence is called true or false (BAND,
# chat 148). Book-versus-record deviations go through score() and never through the integrity checker.
# Reads MEMBERS by name (never a bundle path). Deterministic: no wall clock, no randomness.
import os, re, sys, hashlib, importlib.util
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
H = os.path.dirname(os.path.abspath(__file__))
def load(name):
    s = importlib.util.spec_from_file_location(name.replace('-', '_'), os.path.join(H, name + '.py'))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
r2lib = load('r2lib')
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
def md5(n): return hashlib.md5(open(os.path.join(H, n), 'rb').read()).hexdigest()[:8]

MAIN, REG = 'The_Method_1_6-2.md', 'The_Method_1_6___The_Register-2.md'
VOLS = [MAIN, REG, 'The_Method_1_6___Mathematical_Compendium-2.md', 'The_Method_1_6___The_Physics_Compendium-2.md',
        'The_Method_1_6___Spectra_Compendium-2.md', 'The_Method_1_6___The_Index_of_Indices-2.md']
M, R = rd(MAIN), rd(REG)

def rbody(n):   # copied verbatim from r2-25b.py (there from r2-24a.py … r2-ch17b.py; owed to r2lib, DEFERRED): first non-blank line after '### n'
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())

def body_range(M, sec):   # copied verbatim from r2-25b.py (there from r2-24a.py … r2-ch16z.py; owed to r2lib, DEFERRED): heading to next heading of any rank, body occurrence
    s = r2lib.heading_line(M, sec)
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1]): return (s, i)
    return (s, len(M) + 1)

def lettered(M, tag):   # copied verbatim from r2-25b.py (there from r2-24a.py … r2-ch17c.py; owed to r2lib, DEFERRED): lettered heading, exact token, hits in order; body = LAST
    return [i for i, l in enumerate(M, 1) if re.match(r'^#{2,4}\s*' + re.escape(tag) + r'(?!\.\d)(?!\d)\b', l)]

def norm(s): return re.sub(r'\s+', ' ', s).strip()
FAIL = []; DEV = []
def check(tag, got, exp):   # instrument integrity: a mismatch is the instrument's fault and stops the run
    ok = got == exp
    print('   %-62s %-24s %s' % (tag, repr(got), 'OK' if ok else 'EXPECTED ' + repr(exp)))
    if not ok: FAIL.append(tag)
def score(tag, got, exp, tagno):   # book against record: a mismatch is a FINDING, recorded, never a run failure
    ok = got == exp
    print('   %-62s %-24s %s' % (tag, repr(got), 'as printed' if ok else 'DEVIATION (%s) — printed %s' % (tagno, repr(exp))))
    if not ok: DEV.append((tagno, tag, got, exp))

print('r2-26b.py — 26b-04: F.3 "several of the corrections the Register carries are exactly this rule firing"')
print('members: %s md5 %s | %s md5 %s' % (MAIN, md5(MAIN), REG, md5(REG)))

# ---------------------------------------------------------------- §1 sites
print('\n§1 SITES (located this chat; member line numbers are never carried between chats)')
f3 = lettered(M, 'F.3')
print('   lettered("F.3") hits:', f3, '->', repr(norm(M[f3[-1] - 1])))
RULE = [i for i, l in enumerate(M, 1) if 'refuted by its own extent' in l]
SENT = [i for i, l in enumerate(M, 1) if 'this rule firing' in l]
check('*refuted by its own extent* sites in the main volume', RULE, [11024, 11295])
check('*this rule firing* sites in the main volume', len(SENT), 1)
S = SENT[0]
print('   L%d %s' % (S - 1, repr(norm(M[S - 2]))))
print('   L%d %s' % (S, repr(norm(M[S - 1]))))
print('   L%d %s  (E.1.5, the one instance the book names)' % (11024, repr(norm(M[11023]))))
allsites = [(f, i) for f in VOLS for i, l in enumerate(rd(f), 1) if 'refuted by its own extent' in l or 'this rule firing' in l]
check('the rule and its claim across all six volumes', allsites, [(MAIN, 11024), (MAIN, 11295), (MAIN, 11299)])
check('the claim sits inside the F.3 unit', f3[-1] < S < lettered(M, 'F.3.1')[-1], True)

# ---------------------------------------------------------------- §2 the rule, in the two forms F.3 prints
print('\n§2 THE RULE AS F.3 STATES IT — two forms, printed one after the other, and they do not have one extent')
HEAD = norm(M[11294])
ELAB = norm(' '.join(M[11295:11298]))
print('   RULE-H (headline, L11295): %s' % repr(HEAD))
print('   RULE-E (elaboration, L11296-L11298): %s' % repr(ELAB[:300]))
check('RULE-H is the bare refutation sentence', 'A constraint refuted by its own extent is dead.' in HEAD, True)
check('RULE-E names the mechanism: empty set or the whole of it', 'empty set or the whole of it' in ELAB, True)
check('RULE-E names the consequence: not weakened, not pending, dead', 'not weakened, not pending, dead' in ELAB, True)
print('   CONVENTION RULE-E: a firing is a constraint asserted over a ground whose extent COMPUTED ON THAT GROUND')
print('   is the empty set or the whole of it, the constraint being consequently dead. CONVENTION RULE-H: a firing')
print('   is a constraint killed by the computation of its own extent, by whatever shape that computation takes.')
print('   RULE-H contains RULE-E. Both are scored, because F.3 prints both and the book cites the headline.')
print('   CONVENTION OBJ-C / OBJ-T: F.3 says *constraint*. §4 names a separate mechanism, *a test that could not')
A9, B9 = r2lib.heading_line(M, '28.7.9'), body_range(M, '28.7.9')[1]
print('   fail* (§28.7.9 L%d), and the Register works it as register 784\'s pattern. OBJ-C counts only constraints,'
      % [i for i in range(A9, B9) if 'a test that could not' in M[i - 1]][0])
print('   bounds, laws, criteria and clauses asserted over a ground; OBJ-T adds the checks and tests of that class.')

# ---------------------------------------------------------------- §3 the population
print('\n§3 THE POPULATION — *the corrections the Register carries*, fixed from the Register\'s own definition')
IDX = {}
for i, l in enumerate(R, 1):
    m = re.match(r'^###\s+(\d+)\s*$', l)
    if m: IDX[int(m.group(1))] = i
KS = sorted(IDX)
def rspan(n):
    s = IDX[n]; e = next((IDX[k] for k in KS if IDX[k] > s), len(R) + 1) - 1
    return norm(' '.join(x for x in R[s:e] if x.strip()))
BODY = {n: rspan(n) for n in KS}
check('entry headings in the Register', len(KS), 1628)
check('extent of the Register', (min(KS), max(KS)), (1, 1792))
d1784 = 'one withdrawn claim for each entry this register holds'
check('register 1784 defines the entry as a withdrawn claim', d1784 in BODY[1784].lower(), True)
print('   So every entry IS a correction on the Register\'s own definition (1762, restated 1784), and the')
print('   population of the sentence is the whole Register. Nothing has to be assumed about which entries count.')

# ---------------------------------------------------------------- §4 the token probe, reproduced, and the pool
print('\n§4 THE TOKEN PROBE REPRODUCED, THEN THE POOL — a token probe is not a reading (DOCKET standing method)')
tok = [n for n in KS if re.search(r'refut\w+ by its own extent', BODY[n], re.I)]
tok2 = [n for n in KS if re.search(r'extent', BODY[n], re.I) and re.search(r'\bempty\b|whole of it', BODY[n], re.I)]
check('chat 139\'s probe: the rule\'s words in any entry', tok, [])
print('   the widened token probe (*extent* with *empty* or *whole of it* in one entry): %s' % tok2)
print('   Both are probes of the rule\'s WORDS. The rule fires as a MECHANISM, and the reading below is of that.')
NETA = (r'(vacuous|cannot fail|could not fail|can never fail|passed on anything|passes on anything|passes everything'
        r'|discriminat\w* nothing|carries no information|tests nothing|says nothing at all'
        r'|admits everything|admits (?:every|all) |cannot refuse anything|refuses nothing|no way to disagree'
        r'|could not have been anything else|guaranteed before it ran|forced,? not earned|satisfied at zero'
        r'|intersection is empty|intersection empties|empty before any data|zero by construction|satisfies every criterion'
        r'|fails at every|at every occupancy rather than some|complete rectangle at every|never fired|hold in any theory)')
NETB = r"(refut\w+ by its own extent|F\.3)"
NETC = r'(§4\.6|register (?:777|784|900|1383)\b|contingency protocol)'
A = [n for n in KS if re.search(NETA, BODY[n], re.I)]
B = [n for n in KS if re.search(NETB, BODY[n], re.I)]
C = [n for n in KS if re.search(NETC, BODY[n], re.I)]
POOL = sorted(set(A) | set(B) | set(C))
print('   NET-A the elaboration\'s outcomes in the entry\'s own words           %3d' % len(A))
print('   NET-B the headline, or a citation of F.3                             %3d %s' % (len(B), B))
print('   NET-C the named class: §4.6 and registers 777 / 784 / 900 / 1383     %3d' % len(C))
check('the pool is the union of the three nets', len(POOL), 69)
print('   POOL: %s' % POOL)

# ---------------------------------------------------------------- §5 the reading
print('\n§5 THE READING — every member of the pool scored, each verdict carrying a deciding phrase from its own text')
print('   FIRE-C  a constraint, bound, law, criterion or clause whose computed extent is empty or the whole ground')
print('   FIRE-T  the same shape in a check or test (OBJ-T only)')
print('   FIRE-H  killed by the computation of its own extent, but the extent is neither empty nor whole (RULE-H only)')
print('   COUNTER the extent was computed and the object SURVIVED — the rule applied and not fired')
print('   NEAR    the reading cannot decide; carried as an upper bound, never assigned')
print('   NOT     another mechanism\n')
SC = [
 (365,  'FIRE-C', 'fails at every occupancy rather than some', 'the bound 2J_c <= k holds nowhere on the physical region: the wrong bound, not a loose one'),
 (412,  'FIRE-C', 'had no falsifier', "the law's exception clause had an empty refuting extent; repaired by stating the falsifier"),
 (443,  'FIRE-C', 'the complete rectangle at every cap tested', "the supposed electromagnetic constraint admits the whole rectangle: 333's vacuous zero"),
 (522,  'FIRE-C', 'the operator admits everything', 'every envelope constant at 1, R(Cl(U)) = 2^U: the family says nothing at all'),
 (843,  'FIRE-C', 'carries no information', '21 of 128 brackets restate their own claim; formally true and empty of content'),
 (1174, 'FIRE-C', 'admits all 6,912 cells', 'order-1 marginals admit the whole ambient; corrected to order 2, which returns 976'),
 (1310, 'FIRE-C', 'the intersection is empty', 'a single constant serves no table; 106 constants reduce to eighteen by (period, block)'),
 (1424, 'FIRE-C', 'it cannot refuse anything', "Janet's E = 0 is forced, not earned: no envelope can bind on one cell per row"),
 (1463, 'FIRE-C', 'the running intersection empties fourteen times', "1461's atomic claim dies: 106 separate feasibilities are not one system"),
 (1513, 'FIRE-C', 'the check cannot fail', 'a constraint network whose target column is constant; three vacuous implications found'),
 (1605, 'FIRE-C', 'the intersection is empty before any data is read', "three tests vacuous by construction, and 1602's finding falls with them"),
 (1617, 'FIRE-C', 'it would hold in any theory with the same degeneracies', 'an exact identity constrains nothing; a star removed from the board'),
 (1661, 'FIRE-C', 'the generating rules are total', 'F(-1) = 0 holds at any cutoff: the old statement was wrong in its kind, not stale'),
 (1683, 'FIRE-C', 'not a constraint the data strains against', "M's ruling satisfied at zero; the mult column vacuous on jK"),
 (1686, 'FIRE-C', 'discriminates nothing', 'closure passes for any free axis: the closure test was the wrong instrument'),
 (181,  'FIRE-T', '0 tested', 'a downset test that tested nothing and printed True'),
 (189,  'FIRE-T', 'would have passed on anything', 'the magic-number check compared a list to itself'),
 (422,  'FIRE-T', 'have never fired', 'three audits name no entry between them; a failing input now printed for each'),
 (598,  'FIRE-T', 'a test that passes everything discriminates nothing', 'the grounding check returned 100% on every set'),
 (613,  'FIRE-T', 'zero disagreements was guaranteed before it ran', 'the probe copied the criterion it was testing'),
 (775,  'FIRE-T', 'it has no way to disagree, so it tests nothing', 'thirty pairs counted as passes; the honest figure is 52 of 65'),
 (784,  'FIRE-T', 'will satisfy every cross-check and test nothing', "the class's principle, stated: bracket == interior"),
 (797,  'FIRE-T', 'that test cannot fail', 'the trivial bracket passes 789 of 789 by construction'),
 (798,  'FIRE-T', 'exceeding their own discriminating power', 'four devices in one compendium, the pattern at its fourth sighting'),
 (801,  'FIRE-T', 'so it cannot fail', 'of the two brackets in the book only one is a deduction'),
 (803,  'FIRE-T', 'a bracket that cannot fail tells you nothing about the data', 'the trade-off the compendium carried unstated'),
 (840,  'FIRE-T', 'cannot be wrong is not a prediction', 'eleven against 3,513 is the honest ratio'),
 (845,  'FIRE-T', 'a comparison between a thing and itself cannot fail', 'register 815 withdrawn: the same channel from two capture files'),
 (849,  'FIRE-T', 'the check field is not a check for 110 of 213 objects', 'the pattern swept across the mathematics register and found at scale'),
 (851,  'FIRE-T', 'carries no information about whether anything was checked', 'the compendium overclaims its auditing, not its mathematics'),
 (1383, 'FIRE-T', 'a check that cannot fail is not evidence', 'the contingency protocol, naming the class over three faults at once'),
 (1448, 'FIRE-T', 'cannot correct it', 'the placement confirms whatever it was given: the per-atom fixed point is vacuous'),
 (1469, 'FIRE-T', 'a check on a check that could not fail', 'the contingency sweep catching two faults in itself'),
 (1582, 'FIRE-T', 'my confirmation of it could not fail', 'the observer rule inferred from one case'),
 (1618, 'FIRE-T', 'my first test of that could not fail', 'the sigma drift: the grid was the whole obstacle'),
 (1671, 'FIRE-T', 'could not fail for the reason it names', "C6's stated failure mode could not arise from its own matcher"),
 (1729, 'FIRE-H', 'rule applies and it is dropped', 'item R kills the code\'s unprinted constraint: THE instance E.1.5 names — see 26b-11'),
 (390,  'COUNTER', 'tested against four boundaries', 'a closure defect that could have been blamed on the boundary and was not'),
 (439,  'COUNTER', 'not vacuous', 'vacuity tested and refused: five of twenty closed indices state a verdict and no expression'),
 (462,  'COUNTER', 'a sufficient condition tested for necessity', "§17.3's criterion covers 0.8 to 10.3%: an extent strictly between the two poles"),
 (900,  'COUNTER', 'had the tests not been fixed in advance', 'eight pre-stated tests and a corrected null; the exercise kept as a negative'),
 (1061, 'COUNTER', 'the mechanism that has never failed failed usefully', 'a claim at 191/191 met a bad datum and reported it'),
 (333,  'NEAR', 'the empty index satisfies every criterion here', 'E(X) = 0 is WEAKENED to necessary-not-sufficient rather than declared dead — see the candidate below'),
 (810,  'NEAR', 'cannot be strengthened by more of the same', "the principle restated about sample diversity, not an object's extent"),
 (1504, 'NEAR', 'failing by invariance rather than difficulty', 'the equant diagnostic: an undetermined parameter, an adjacent mechanism'),
 (361,  'NOT', 'exhaustively verified', 'an inflated classification, not a vacuity'),
 (367,  'NOT', 'the two cannot hold together', "two assignment rules in contradiction under F.3's own scheme"),
 (371,  'NOT', 'is withdrawn rather than closed', 'a question presupposing a stable quantity; withdrawn for instability'),
 (372,  'NOT', 'the least stable thing about it', 'a count over an index of open questions, same instability'),
 (388,  'NOT', 'closed by stating one number', 'item M closed by occupying a cell'),
 (392,  'NOT', 'all six fibres now carry a number', 'a recomputation contradicting a single figure'),
 (503,  'NOT', 'never checked against a second', 'one heuristic for twelve cycles: §2.24, a different forbidden shape'),
 (655,  'NOT', 'a test that could not fail', 'the class named among §4\'s ten mechanisms; the home of OBJ-T, not a firing'),
 (1403, 'NOT', 'never in the interior', 'a measured placement result'),
 (1434, 'NOT', 'two halves of one equation', 'the empty running intersection used constructively, as forced moves'),
 (1461, 'NOT', 'additive representability of a ranked order', 'the claim 1463 corrects, not the correction'),
 (1515, 'NOT', 'two share a mechanism exactly', 'three open topics on one measure'),
 (1516, 'NOT', 'the common quantity is the helly number', 'a shared quantity across three objects'),
 (1522, 'NOT', 'an ordinal self-claim made without counting', 'a self-claim fault; it does record that the audits census this class'),
 (1525, 'NOT', 'one transition per cache window', 'a fetch layer caching on the wrong key'),
 (1603, 'NOT', 'a greedy regex', 'a parser fault'),
 (1691, 'NOT', 'disambiguate at source', 'duplicate numbering repaired at source'),
 (1719, 'NOT', 'polynomial withdrawn', 'a wrong coefficient caught by a second route'),
 (1762, 'NOT', 'a surviving claim is defined', "ruling 25; the population's definition, used in §3"),
 (1763, 'NOT', 'the 489 untested spectra rows', 'ruling 26, a sealed-test run'),
 (1767, 'NOT', 'the answer on the 126 is empty', 'a coverage result about a delivered record'),
 (1768, 'NOT', 'the six captures run under ruling 26', 'a capture reconciliation'),
 (1780, 'NOT', 'rebuilt on a different domain', 'Appendix F withdrawn for taking the wrong domain'),
 (1786, 'NOT', 'numbering was defective and is corrected', "the F.3.3 renumber; 26b-06's site"),
]
check('the reading scores every member of the pool exactly once', sorted(n for n, *_ in SC), POOL)
miss = []
for n, verdict, phrase, why in SC:
    ok = phrase.lower() in BODY[n].lower()
    if not ok: miss.append((n, phrase))
    print('   %4d %-8s %-58s %s' % (n, verdict, '"' + phrase + '"', why))
check('every deciding phrase present in its own entry', miss, [])
V = Counter(v for _, v, _, _ in SC)
print('\n   FIRE-C %d | FIRE-T %d | FIRE-H %d | COUNTER %d | NEAR %d | NOT %d'
      % (V['FIRE-C'], V['FIRE-T'], V['FIRE-H'], V['COUNTER'], V['NEAR'], V['NOT']))
check('the six verdicts total to the pool', sum(V.values()), len(POOL))

# ---------------------------------------------------------------- §6 the arithmetic
print('\n§6 THE ARITHMETIC — *several* under a stated BAND, in every cell of the two conventions')
print('   CONVENTION BAND (INFERRED — an English count word, not a figure), both readings scored:')
print('     STRICT *several* = at least three (chat 139 stated this reading when it recorded 26b-04);')
print('     LOOSE  *several* = more than one, at least two.')
cells = [
    ('RULE-E x OBJ-C  constraints only, the mechanism as elaborated', V['FIRE-C'], V['FIRE-C'] + V['NEAR']),
    ('RULE-E x OBJ-T  constraints and the checks of the same class', V['FIRE-C'] + V['FIRE-T'], V['FIRE-C'] + V['FIRE-T'] + V['NEAR']),
    ('RULE-H x OBJ-C  constraints, the headline form', V['FIRE-C'] + V['FIRE-H'], V['FIRE-C'] + V['FIRE-H'] + V['NEAR']),
    ('RULE-H x OBJ-T  everything the two conventions admit', V['FIRE-C'] + V['FIRE-T'] + V['FIRE-H'], V['FIRE-C'] + V['FIRE-T'] + V['FIRE-H'] + V['NEAR']),
]
for nm, v, hi in cells:
    print('   %-60s %3d (upper bound %3d)   STRICT %-3s LOOSE %-3s'
          % (nm, v, hi, 'in' if v >= 3 else 'out', 'in' if v >= 2 else 'out'))
check('*several* reproduces in every cell, STRICT', all(v >= 3 for _, v, _ in cells), True)
check('*several* reproduces in every cell, LOOSE', all(v >= 2 for _, v, _ in cells), True)
check('the lower bound of the sentence is the constraints-only cell', min(v for _, v, _ in cells), V['FIRE-C'])
pct = (Decimal(V['FIRE-C'] + V['FIRE-T'] + V['FIRE-H']) * 100 / Decimal(len(KS))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
print('   %d firings against %d entries of the Register = %s %% (Decimal.quantize, ROUND_HALF_UP; never round()).'
      % (V['FIRE-C'] + V['FIRE-T'] + V['FIRE-H'], len(KS), pct))
score('the sentence *several ... are exactly this rule firing*', V['FIRE-C'] >= 3, True, '26b-04')

# ---------------------------------------------------------------- §7 the Register sweep
print('\n§7 REGISTER SWEEP — WARNING lines read before any verdict, and the volumes grepped for a later statement')
fired = [n for n, v, _, _ in SC if v.startswith('FIRE')]
w = [n for n in fired if 'WARNING:' in BODY[n]]
loose = [n for n in fired if 'WARNING' in BODY[n].upper() and n not in w]
check('WARNING markers (the colon form, chat 142) on any entry scored as a firing', w, [])
check('the loose token, read and disposed of', loose, [1463])
print('   1463 carries *FISHBURN\'S WARNING* — an imported hazard named in the entry\'s own headline, not a')
print('   Register WARNING marker. It is the reason the entry fires: the warning is what kills 1461\'s claim.')
print('   WARNING markers in the Register at all: %d (docket 35\'s instrument, run over this family)'
      % sum(1 for l in R if 'WARNING:' in l))
later = [(f, i, norm(l)[:80]) for f in VOLS for i, l in enumerate(rd(f), 1)
         if re.search(r'this rule firing|several of the corrections', l)]
check('later or other statements of the claim in any volume', later, [(MAIN, 11299, norm(M[11298])[:80])])
print('   No later statement qualifies the sentence; it is scored against the Register, which it names as its record.')

# ---------------------------------------------------------------- §8 what the reading turns up in its own unit
print('\n§8 NEW FINDINGS IN THE ENGAGED RANGE (recorded, never repaired — the chat-67 hold)')
sec = [(f, i) for f in VOLS for i, l in enumerate(rd(f), 1) if re.search(r'§784\b', l)]
check('*§784* — a Register number printed as a section pointer', sec, [(REG, 3113)])
check('no §784 exists: the main volume ends at chapter 36', r2lib.heading_line(M, '36') > 0, True)
thm = [(f, i) for f in VOLS for i, l in enumerate(rd(f), 1) if re.search(r'(Theorem|Thm)\s*11\.1\b', l)]
check('*Thm 11.1* cited once and printed nowhere in the six volumes', thm, [(REG, 6299)])
bld = [(f, i) for f in VOLS for i, l in enumerate(rd(f), 1) if re.search(r'BUILD-?10\b', l)]
check('a build handle in a reader-facing volume (Ruling 46)', bld, [(REG, 6507)])
print('   26b-08  reg L3113 (entry 845): *§784\'s pattern, fifth sighting* — a Register number given a § sigil.')
print('           §784 resolves to no section in any of the six volumes. Docket 9(c) / 28.')
print('   26b-09  reg L6299 (entry 1686): *Thm 11.1 makes T ... a new measurement*. Theorem 11.1 is printed in')
print('           none of the six volumes; the citation has no target. Docket 9(c) / docket 2.')
print('   26b-10  reg L6507 (entry 1763): *run489.py, ruled_bracket.py, RULING-TOLERANCE-489.md and the run\'s JSON')
print('           go to BUILD-10* — a build handle and four internal file names in a reader-facing volume. Ruling 46,')
print('           docket 6 / 28; the same class as the 3B.* label form (census 1536-1545).')
print('   26b-11  E.1.5 L11024 and Register 1729 cite F.3\'s rule for item R. The constraint *obstacle = buildable')
print('           implies cost <= days* is refuted by a COUNTEREXAMPLE: R is buildable and unbounded. Its extent on')
print('           the fourteen is neither the empty set nor the whole of them, so the instance the book names for')
print('           the rule satisfies RULE-H and NOT RULE-E — the two forms F.3 prints do not have one extent, and')
print('           which is meant is nowhere stated. Docket 34 (an unstated convention) / 9(b).')
print('   CANDIDATE, recorded and not scored (outside the count word this family is about): *The work applies this')
print('           without exception* (L11298; census row 1228, closed *not a defect* in the ch26a unit). The nearest')
print('           exception the reading found is register 333: a criterion the EMPTY INDEX satisfies is weakened to')
print('           *necessary for completeness and not sufficient for content* rather than declared dead, where')
print('           RULE-E says *not weakened, not pending, dead*. One site; docket 19 for R3.')

# ---------------------------------------------------------------- verdict
print('\nVERDICT')
print('   26b-04 is REVERSED by the reading. The sentence measures TRUE. Chat 139 probed the rule\'s WORDS and')
print('   found nothing, and said in terms that a token probe is not a reading; read as a MECHANISM the rule fires')
print('   %d times over constraints proper and %d times more over the checks of the same class, in a Register whose'
      % (V['FIRE-C'], V['FIRE-T']))
print('   own definition makes every one of its %d entries a correction. *several* is reached under both readings' % len(KS))
print('   of the count word in every cell of both conventions, the smallest cell being %d. The work also applies the'
      % V['FIRE-C'])
print('   rule and finds it does NOT fire %d times (390, 439, 462, 900, 1061), which is the discipline the sentence' % V['COUNTER'])
print('   describes rather than a counter-example to it. %d members of the pool the reading cannot decide are carried' % V['NEAR'])
print('   as an upper bound and never assigned.')
print('   What survives as a finding is not the count but the citation: 26b-11. The one instance E.1.5 names is a')
print('   refutation by counterexample, and F.3 prints the rule in two forms that do not have one extent.')
print('   New this unit: 26b-08 (§784 as a section pointer), 26b-09 (Thm 11.1 cited, printed nowhere), 26b-10')
print('   (a build handle in the Register), 26b-11 (the two forms of the rule, and the instance that fits only one).')
print('\nDEVIATIONS RECORDED (findings, not instrument faults):')
for t, tag, got, exp in DEV: print('   %-8s %-56s measured %s against printed %s' % (t, tag, repr(got), repr(exp)))
print('\n%s' % ('FAIL: ' + '; '.join(FAIL) if FAIL else 'ALL INSTRUMENT CHECKS OK — %d deviations recorded' % len(DEV)))
sys.exit(1 if FAIL else 0)
