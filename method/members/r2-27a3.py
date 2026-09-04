#!/usr/bin/env python3
# r2-27a3.py — R3 (chat 153-R) — 27a-02 under M's ruling (a), and 27a-07 / 27a-08 with it: Appendix G's
# "what rests on it" column names entries that REST ON the section, so the Register pointers of rows 8.2,
# 8.4 and 10.4c are RE-TAKEN BY READING under CONVENTION DEP (r2-27a, chat 151-B), and the one question
# the ruling left open — whether the Mathematical Compendium's modular-ledger set 1019 / 1020 / 1022 /
# 1035 / 1483 / 1484 becomes row 10.4c's — is answered by the same reading, over row 10.4e as well,
# because that is the row the compendium's block names as its source (T 10.4e).
# CONVENTION DEP, restated: an entry RESTS ON section S if DEP-N, it names the source — "T §S", "T S",
# "App. G" at S, or S's number where the context is the paper's — or DEP-M, its own deciding sentence is
# an instance or a consequence of the mechanism S establishes; in both cases the deciding phrase is
# ASSERTED PRESENT in the entry's own text before any verdict prints. NEAR is an upper bound, never
# assigned. NO ROW IS WRITTEN FROM A TOKEN PROBE: the DEP-N sweep below is exhaustive over the Register
# for the four locators, and DEP-M is read on the candidates it and the two prior lists supply — the
# eight pairs the column asserts (r2-27a) and the six the compendium's block cites. DEP-M beyond those
# candidates is not claimed.
# A bare "§8.2" / "§8.4" in the Register can be the main volume's own section (§8.2 Rank is conserved;
# §8.4 Sperner), so a bare locator is a CANDIDATE, decided by the entry's own text; "§10.4c" and "§10.4e"
# exist in no volume but Transitions and resolve to it.
# Book-versus-record deviations go through score() and never through the integrity checker check().
# Reads MEMBERS by name (never a bundle path). Deterministic: no wall clock, no randomness.
import os, re, sys, hashlib
H = os.path.dirname(os.path.abspath(__file__))
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
def md5(n): return hashlib.md5(open(os.path.join(H, n), 'rb').read()).hexdigest()[:8]
def hr(t): print('\n== ' + t)
def norm(s): return re.sub(r'\s+', ' ', s).strip()
MAIN, REG = 'The_Method_1_6-2.md', 'The_Method_1_6___The_Register-2.md'
MC, TR = 'The_Method_1_6___Mathematical_Compendium-2.md', 'Transitions.md'
M, R, T, C = rd(MAIN), rd(REG), rd(TR), rd(MC)
FAIL = []; DEV = []
def check(tag, got, exp):
    ok = got == exp
    print('   %-66s %-28s %s' % (tag, repr(got)[:28], 'OK' if ok else 'EXPECTED ' + repr(exp)))
    if not ok: FAIL.append(tag)
def score(tag, got, exp, tagno):
    ok = got == exp
    print('   %-66s %-28s %s' % (tag, repr(got)[:28], 'as printed' if ok else 'DEVIATION (%s) — printed %s' % (tagno, repr(exp))))
    if not ok: DEV.append((tagno, tag, got, exp))
print('r2-27a3.py — 27a-02 under ruling (a): the Register pointers of Appendix G rows 8.2, 8.4, 10.4c re-taken under CONVENTION DEP')
print('members: %s %s | %s %s | %s %s | %s %s' % (MAIN, md5(MAIN), REG, md5(REG), TR, md5(TR), MC, md5(MC)))

# ------------------------------------------------------------------ §1
hr('§1 THE ROWS, located by scan — pointers are read OUT of the rows, never carried in')
GA = [i for i, l in enumerate(M, 1) if re.match(r'^#{1,4}\s', l) and l.strip().endswith('Appendix G — Transitions, indexed')][-1]
GEND = min(i for i, l in enumerate(M, 1) if l.strip() == '# END MATTER' and i > GA)
print('   Appendix G body L%d–L%d (%d lines)' % (GA, GEND - 1, GEND - GA))
WANT = ['8.2', '8.4', '10.4c', '10.4e']
rows = {}
for i in range(GA, GEND):
    m = re.match(r'^\|\s*(\S+)\s*\|(.*)\|(.*)\|\s*$', M[i - 1])
    if m and m.group(1) in WANT: rows[m.group(1)] = (i, norm(m.group(2)), norm(m.group(3)))
check('the four rows located, once each', sorted(rows), sorted(WANT))
cited = {}
for w in WANT:
    i, stmt, col = rows[w]
    cited[w] = sorted({int(x) for x in re.findall(r'\b(\d{3,4})\b', re.sub(r'`[^`]*`', '', col))})
    print('   row %-6s L%-6d %s' % (w, i, col))
print('   (the pointers as printed are DATA, scored in §5 against the reading; before the re-take they were')
print('    8.2: 1375, 1519, 1523, 1535, 1551 | 8.4: 1375 | 10.4c: 1399, 1403 | 10.4e: none — r2-27a, chat 151-B)')

# ------------------------------------------------------------------ §2
hr('§2 THE MECHANISMS, asserted present in Transitions.md — the row is scored against the section, not the row text')
def tsec(s):
    a = [i for i, l in enumerate(T, 1) if re.match(r'^###\s+%s\s' % re.escape(s), l)][0]
    e = next((i for i, l in enumerate(T, 1) if i > a and re.match(r'^#{1,3}\s', l)), len(T) + 1)
    return norm(' '.join(T[a - 1:e - 1]))
TS = {w: tsec(w) for w in WANT}
MECH = {'8.2':   ['A theorem holding only under a scope condition is inherently ternary', 'Arity ≥ 3 is what makes a defect', 'NEC ≥ 3 → (IC ∨ U ∨ X)'],
        '8.4':   ['A : Loc → Alg', 'exactly four parts', 'Three of my seven vocabularies dissolve'],
        '10.4c': ['no transverse derivative', 'Ω is block diagonal', 'factorise over them'],
        '10.4e': ['Half-sided modular inclusion is what turns algebra into geometry', 'd − 1 = 1 + (d − 2)', 'one HSMI per generator']}
for w in WANT:
    for ph in MECH[w]: check('T §%s carries "%s"' % (w, ph[:44]), ph in TS[w], True)
# the main volume's own §8.2 and §8.4 are other sections entirely, and §10.4c / §10.4e do not exist in it
def mhead(s): return [norm(l) for l in M if re.match(r'^###\s+%s\s' % re.escape(s), l)]
print('   main volume\'s own §8.2: %s | §8.4: %s' % (mhead('8.2'), mhead('8.4')))
check('main volume has no §10.4c and no §10.4e', mhead('10.4c') + mhead('10.4e'), [])

# ------------------------------------------------------------------ §3
hr('§3 THE REGISTER, indexed; the DEP-N sweep — every entry naming one of the four locators, over all entries')
IDX = {}
for i, l in enumerate(R, 1):
    m = re.match(r'^###\s+(\d+)\s*$', l)
    if m: IDX[int(m.group(1))] = i
KS = sorted(IDX)
def span(n):
    s = IDX[n]; e = next((IDX[k] for k in KS if IDX[k] > s), len(R) + 1) - 1
    return s, e
def body(n):
    s, e = span(n); return norm(' '.join(x for x in R[s:e] if x.strip()))
BODY = {n: body(n) for n in KS}
print('   entries indexed: %d (%d to %d)' % (len(KS), KS[0], KS[-1]))
STRICT = {w: re.compile(r'\bT\s*§?\s*%s\b' % re.escape(w)) for w in WANT}
BARE = {w: re.compile(r'(?<!T )(?<!T)§\s*%s\b' % re.escape(w)) for w in WANT}
GEN = re.compile(r'Transitions|App\. ?G\b|Appendix G')
EXCL = [n for n in KS if 're-taken by reading' in BODY[n].lower() and 'appendix g' in BODY[n].lower()]
print('   entries that RECORD this reading name every locator and rest on nothing; excluded from the sweep: %s' % EXCL)
check('the excluded entries are the record of the re-take and no other', EXCL, [1812])
strict, bare, gen = {w: [] for w in WANT}, {w: [] for w in WANT}, []
for n in KS:
    if n in EXCL: continue
    b = BODY[n]
    for w in WANT:
        if STRICT[w].search(b): strict[w].append(n)
        elif BARE[w].search(b): bare[w].append(n)
    if GEN.search(b): gen.append(n)
for w in WANT: print('   §%-6s T-locator (DEP-N): %-28s bare §-locator (candidate): %s' % (w, strict[w], bare[w]))
print('   entries naming the paper or the appendix without a section locator: %s' % gen)
check('T-locator hits, §8.2', strict['8.2'], [543, 584, 585, 588, 592])
check('T-locator hits, §8.4', strict['8.4'], [543])
check('T-locator hits, §10.4c', strict['10.4c'], [549, 550])
check('T-locator hits, §10.4e', strict['10.4e'], [])
check('bare-locator candidates, §8.4', bare['8.4'], [544])
check('bare-locator candidates, §8.2 / §10.4c / §10.4e', bare['8.2'] + bare['10.4c'] + bare['10.4e'], [])
check('paper-or-appendix-only entries name no row section', [n for n in gen if any(STRICT[w].search(BODY[n]) or BARE[w].search(BODY[n]) for w in WANT)], [])
for n in gen: print('   %-5d %s' % (n, BODY[n][:100]))
print('   Those name the source and no section: 1769 counts its citations, 1770 absorbs the paper as Appendix G,')
print('   1778 enters its full table in the Index of Indices. None rests on 8.2, 8.4, 10.4c or 10.4e.')

# ------------------------------------------------------------------ §4
hr('§4 THE COMPENDIUM\'S SET — the modular-ledger block and the row it names')
led = [i for i, l in enumerate(C, 1) if l.strip() == '### The modular ledger'][0]
e = next(i for i, l in enumerate(C, 1) if i > led and re.match(r'^###\s', l))
blk = norm(' '.join(C[led - 1:e - 1]))
SIX = sorted({int(x) for x in re.findall(r'(?:[Rr]egisters?|R)\s+(\d{3,4})', blk)})
print('   MC "The modular ledger" L%d–L%d rests on registers %s' % (led, e - 1, SIX))
check('the block cites the six', SIX, [1019, 1020, 1022, 1035, 1483, 1484])
check('the block names T 10.4e (App. G) as its source', 'T 10.4e (App. G)' in blk, True)
check('the block does not name 10.4c', '10.4c' in blk, False)

# ------------------------------------------------------------------ §5
hr('§5 THE READING — every candidate scored for DEPENDENCE on each row, with a deciding phrase asserted in its own text')
print('   DEP-N names the source at the section | DEP-M deciding sentence is an instance of the mechanism | NEAR upper bound | NOT another mechanism\n')
SC = [
 # §8.2 — the five the row names (r2-27a's verdicts, re-asserted) and the five the sweep finds
 ('8.2', 1375, 'NOT',   'THE DUAL OF A.DEFINE', "A.define's degeneracy — a rung-1 coordinate and its injective dual — not a scope condition"),
 ('8.2', 1519, 'NEAR',  "which is Freuder's classical result", 'the arity mechanism from the low side, credited to Freuder and derived from register 507'),
 ('8.2', 1523, 'NEAR',  'Λ at max clique 1', 'arity again, and it names M.C2, an object of §10.4d'),
 ('8.2', 1535, 'NOT',   'A NILSSON SHELL N ADMITS ONLY', 'a parity check on a supplied nuclear table'),
 ('8.2', 1551, 'NOT',   "K I's QUANTUM DEFECTS", 'a spectra capture'),
 ('8.2', 543,  'DEP-N', "verifies against T §8.2's own table", 'W.jur verified against the section\'s table: E = 0 at arity 2, E = 30 and core 1 at arities 3 and 4'),
 ('8.2', 584,  'DEP-N', 'T §8.2 prints a disjunction', 'the candidate space was wrong because the section prints NEC ≥ 3 → (IC ∨ U ∨ X)'),
 ('8.2', 585,  'DEP-N', 'T §8.2 prints NEC ≥ 3 → (IC ∨ U ∨ X)', 'the rule family is incomplete because the section prints a disjunction no A ≥ a → B ≥ b can express'),
 ('8.2', 588,  'DEP-N', 'as T §8.2 prints', 'the edge form is extended to disjunctive heads because that is the section\'s shape'),
 ('8.2', 592,  'DEP-N', 'CONJUNCTIVE BODIES ARE THE FORM T §8.2 PRINTS', 'conjunctive bodies tested because the section prints NEC ≥ 3 ∧ X = 0 → U ≥ 1'),
 # §8.4
 ('8.4', 1375, 'NOT',   'THE DUAL OF A.DEFINE', 'no vocabulary, no functor and no partition of any size'),
 ('8.4', 543,  'DEP-N', 'verifies against T §8.4', 'W.rel verified against the section, which replaces seven vocabularies with the functor\'s four parts'),
 ('8.4', 544,  'DEP-M', 'V6 is not a vocabulary index', 'a consequence of the section: the achronal ANEC is a relation between a spacetime and a state, so V6 is not a coordinate of either — the bare §8.4 is the paper\'s, its V-numbering being retired there'),
 # §10.4c — the two the row names, the two the sweep finds, and the compendium's six read against C1's mechanism
 ('10.4c', 1399, 'NOT',   'the sequence as printed was not one measurement', 'two tower conventions printed as one sequence'),
 ('10.4c', 1403, 'NOT',   "the corridor's lower endpoint", 'where a sits in the Λ_T corridor'),
 ('10.4c', 549,  'DEP-N', 'printed in full at T §10.4c', 'M.C1 closed by reading the section, control included'),
 ('10.4c', 550,  'DEP-N', 'T §10.4c reads', 'the section\'s forest-of-paths against ladder is §21.5.3\'s constraint-graph vocabulary'),
 ('10.4c', 1019, 'NOT',   'Half-sidedness fails on the DRESSED algebra', 'corner edge modes and the converter\'s input — not the factorisation over generators'),
 ('10.4c', 1020, 'NOT',   'a condition invariant under a group cannot fix that group\'s parameter', 'the relative boost — not the factorisation'),
 ('10.4c', 1022, 'NOT',   'M.C2 stays OPEN', 'C2\'s frontier, §10.4d'),
 ('10.4c', 1035, 'NOT',   'The STATEFUL object supplies exactly one dimension', 'the ledger\'s split; it names C1 as the ledger\'s term and rests on the ledger'),
 ('10.4c', 1483, 'NOT',   'IT IS THE FREE COUNT', 'the ledger\'s sum qualified; not the factorisation'),
 ('10.4c', 1484, 'NOT',   'THE LEDGER COUNTS A MANIFOLD', 'the ledger completed as two accountings; not the factorisation'),
 # §10.4e — the compendium's six read against the converter and the dimensional ledger
 ('10.4e', 1019, 'NEAR',  'Half-sidedness fails on the DRESSED algebra', 'where the converter\'s input condition fails — the section\'s mechanism read at its input, not an instance of its ledger; carried, not assigned'),
 ('10.4e', 1020, 'NEAR',  'Non-expansion does not supply a preferred scaling of u', 'the section\'s own caution — identifying the affine line is a further step — read from the other side; carried, not assigned'),
 ('10.4e', 1022, 'NOT',   'M.C2 stays OPEN', 'C2\'s frontier is §10.4d\'s'),
 ('10.4e', 1035, 'DEP-M', 'one HSMI per generator supplies the affine line; the transverse direct integral is C1 and no HSMI supplies it', 'the ledger\'s own line, d − 1 = 1 + (d − 2), read as the stateful / kinematic split'),
 ('10.4e', 1483, 'DEP-M', 'M.ledger states d − 1 = 1 + (d − 2)', 'the ledger\'s sum is the free count — a qualification OF the section\'s ledger'),
 ('10.4e', 1484, 'DEP-M', 'the ledger is right about it: d − 1 = 1 + (d − 2)', 'the ledger completed as two accountings — a consequence OF the section\'s ledger'),
]
PRIOR = {'8.2': [1375, 1519, 1523, 1535, 1551], '8.4': [1375], '10.4c': [1399, 1403], '10.4e': []}   # the eight pairs the column asserted before the re-take (r2-27a)
cands = {w: sorted(set(cited[w]) | set(PRIOR[w]) | set(strict[w]) | set(bare[w]) | (set(SIX) if w in ('10.4c', '10.4e') else set())) for w in WANT}
check('every candidate of every row is scored exactly once', sorted((w, n) for w, n, *_ in SC), sorted((w, n) for w in WANT for n in cands[w]))
miss = []
for w, n, v, ph, why in SC:
    if ph.lower() not in BODY[n].lower(): miss.append((w, n, ph))
    print('   §%-6s %-5d %-6s "%s"' % (w, n, v, ph[:80]))
    print('                        %s' % why)
check('every deciding phrase present in its own entry', miss, [])
RES = {w: sorted(n for ww, n, v, *_ in SC if ww == w and v in ('DEP-N', 'DEP-M')) for w in WANT}
NEARS = {w: sorted(n for ww, n, v, *_ in SC if ww == w and v == 'NEAR') for w in WANT}
for w in WANT: print('   §%-6s rests on: %-28s NEAR (carried, not assigned): %s' % (w, RES[w], NEARS[w]))
check('§8.2 re-taken', RES['8.2'], [543, 584, 585, 588, 592])
check('§8.4 re-taken', RES['8.4'], [543, 544])
check('§10.4c re-taken', RES['10.4c'], [549, 550])
check('§10.4e re-taken', RES['10.4e'], [1035, 1483, 1484])
check('the compendium\'s six: how many rest on 10.4c', [n for n in SIX if n in RES['10.4c']], [])
check('the compendium\'s six: how many rest on 10.4e', [n for n in SIX if n in RES['10.4e']], [1035, 1483, 1484])
for w in WANT:
    score('row %s: the entries that rest on it are the entries it names' % w, RES[w], cited[w], '27a3-0%d' % (WANT.index(w) + 1))

# ------------------------------------------------------------------ §6
hr('§6 27a-08 — the WARNING on 1403, and what the re-take does with it')
s, e = span(1403)
w1403 = [norm(R[i - 1]) for i in range(s + 1, e + 1) if 'WARNING' in R[i - 1].upper()]
check('1403 carries a WARNING that its a values are reconstructions', bool(w1403) and 'RECONSTRUCTION' in w1403[0].upper(), True)
check('1403 rests on no row under DEP', [w for w in WANT if 1403 in RES[w]], [])
print('   The citation is DROPPED by the re-take, which is the second of docket 35\'s two routes; nothing restates it.')
check('no entry the re-take assigns carries a WARNING', [n for w in WANT for n in RES[w] if any('WARNING' in R[i - 1].upper() for i in range(span(n)[0] + 1, span(n)[1] + 1))], [])

# ------------------------------------------------------------------ §7
hr('§7 THE ROWS AS THEY WOULD READ — the third column re-taken, the first two untouched')
def col3(w):
    i, stmt, col = rows[w]
    keep = re.sub(r';\s*Register[^;|]*$', '', col).strip()
    return keep + ('; Register ' + ', '.join(str(n) for n in RES[w]) if RES[w] else '')
for w in WANT: print('   | %s | … | %s |' % (w, col3(w)))
check('row 8.2 third column', col3('8.2'), '`W.jur`; Chapter 12; Register 543, 584, 585, 588, 592')
check('row 8.4 third column', col3('8.4'), '`W.rel`; Chapter 12; Register 543, 544')
check('row 10.4c third column', col3('10.4c'), '`M.C1`; Register 549, 550')
check('row 10.4e third column', col3('10.4e'), '`M.ledger`; Register 1035, 1483, 1484')

# ------------------------------------------------------------------ verdict
hr('VERDICT')
print('   integrity checks: %s' % ('ALL OK' if not FAIL else 'FAILED: ' + '; '.join(FAIL)))
print('   deviations recorded: %d' % len(DEV))
for tagno, tag, got, exp in DEV: print('      %s  %s — measured %r, printed %r' % (tagno, tag, got, exp))
print('   Under ruling (a) the three rows carry what the reading finds. Of the eight pairs the column asserted,')
print('   none rests on its section (r2-27a, reproduced); of the entries the exhaustive DEP-N sweep finds, nine do,')
print('   and one bare-locator candidate is decided DEP-M by its own text. The compendium\'s six are NOT 10.4c\'s')
print('   set: none rests on C1\'s factorisation. Three of them — 1035, 1483, 1484 — rest on the dimensional ledger')
print('   of §10.4e, the row the compendium\'s block itself names, and 27a-07\'s disagreement resolves that way:')
print('   the appendix takes the compendium\'s address for the three that carry the deciding phrase, and carries')
print('   1019 and 1020 as NEAR, never assigned. 1403 rests on no row, so its citation is dropped and 27a-08 is')
print('   discharged by the drop. Pointer arithmetic: 8 pairs asserted, 0 kept; 12 pairs written, 0 from a probe.')
sys.exit(1 if FAIL else 0)
