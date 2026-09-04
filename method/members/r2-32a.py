#!/usr/bin/env python3
# r2-32a.py — chat 152 (Cowork) — 26c-02 under M's ruling (c): the ORIGIN of each of §32.1.4's three totals.
# M ruled (c), a third state: hunt the record for where 55, 48 and 47 each come from, rather than choosing
# between (a) the section takes register 375's change and (b) 375 is corrected.
# WHAT WAS OWED. 26c-02 recorded that three totals stand at once — the printed fifty-five, §32.1.4.1's 48
# with register 373, and register 375's 47 — and that "the replacement shape sentence appears in no volume".
# It did NOT say where any of the three came from. This instrument supplies the provenance of each, and it
# CORRECTS the reading that recorded it (a finding about the earlier reading, measured, not a repair).
# CONVENTION ORIG, stated before anything is scored:
#   a total's ORIGIN is the object that computed it — a printed component set whose sum reaches it, or an
#   entry that states it as a readout. A total is REPRODUCIBLE only if some assignment of PRINTED values to
#   the four components §32.1.4's own table names sums to it; a component value that appears nowhere in the
#   six volumes or Prints & Proofs may not be supplied by this instrument to close an arithmetic. Where no
#   printed assignment reaches a total, the total is UNREPRODUCIBLE and the entry that states it is its only
#   provenance — which is a fact about the record, not a defect in the arithmetic.
# FAULTS SELF-CAUGHT AND NAMED (this instrument's, not the book's):
#   fault 1: the shape sentence was first swept case-sensitively over MAIN only, reproducing 26c-02's
#            "no volume" verdict. The sweep is over all six volumes AND Prints & Proofs; it has two sites.
#   fault 2: the component sweep first admitted E(audits) = 16 from §32.6.1 without checking whose readout
#            it is. §32.6.1's readout is a FIVE-term set over a different index family (Λ, audits, G, Q, D),
#            not §32.1.4's four. The value is admitted as a printed value of the audits component and the
#            distinction is printed beside it, because a value is printed or it is not.
# Deterministic: no wall clock, no randomness. Reads MEMBERS by name; PP is Prints & Proofs.
import os, re, sys, hashlib, itertools, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
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
    print('   %-70s %-26s %s' % (tag, repr(got), 'OK' if ok else 'EXPECTED ' + repr(exp)))
    if not ok: FAIL.append(tag)
def score(tag, got, exp, tagno):
    ok = got == exp
    print('   %-70s %-26s %s' % (tag, repr(got), 'as printed' if ok else 'DEVIATION (%s) — printed %s' % (tagno, repr(exp))))
    if not ok: DEV.append((tagno, tag, got, exp))

print('r2-32a.py — 26c-02 ruling (c): the origin of §32.1.4\'s fifty-five, of §32.1.4.1\'s 48, and of register 375\'s 47')
print('members: %s md5 %s | %s md5 %s | PP md5 %s'
      % (MAIN, md5(MAIN), REG, md5(REG), hashlib.md5('\n'.join(P).encode()).hexdigest()[:8]))

def head_body(lines, sec):
    """body occurrence of '### <sec> ' — the LAST such heading, contents entries excluded by taking the last."""
    hits = [i for i, l in enumerate(lines, 1) if re.match(r'^\s*#{2,4}\s+%s\s' % re.escape(sec), l)]
    return hits[-1] if hits else None
def sec_end(lines, start):
    return next((j for j in range(start + 1, len(lines) + 1) if re.match(r'^\s*#{1,4}\s', lines[j - 1])), len(lines) + 1)

# ------------------------------------------------------------------ §1
hr('§1 §32.1.4 AND ITS TABLE — located by scan; the four E-bearing rows and their sum')
s4 = head_body(M, '32.1.4'); e4 = sec_end(M, s4)
s41 = head_body(M, '32.1.4.1'); e41 = sec_end(M, s41)
print('   §32.1.4   body L%d–L%d   %s' % (s4, e4 - 1, norm(M[s4 - 1])))
print('   §32.1.4.1 body L%d–L%d   %s' % (s41, e41 - 1, norm(M[s41 - 1])))
check('§32.1.4 encloses §32.1.4.1 (the subsection follows the section)', s41 > s4 and s41 <= e4, True)

# the table rows: an aligned display line whose last two fields are an integer E and a word
ROWS = []
for i in range(s4, e4):
    l = M[i - 1]
    if not l.startswith('  ') or l.startswith('   **'): continue
    mm = re.match(r'^\s{2}(\S.*?)\s{2,}(\d+)\s+(\d+)\s+(\S.*)$', l)
    if mm: ROWS.append((i, norm(mm.group(1)), int(mm.group(2)), int(mm.group(3)), norm(mm.group(4))))
for i, name, coords, Eval, cells in ROWS:
    print('   L%-5d %-42s coords %-3d E %-3d cells named and unoccupied: %s' % (i, name, coords, Eval, cells))
check('table rows located', len(ROWS), 7)
BEAR = [(n, E, c) for _, n, _, E, c in ROWS if c != '—']
check('E-bearing rows (a cells-named entry that is not an em dash)', len(BEAR), 4)
check('their E values, in printed order', [E for _, E, _ in BEAR], [4, 1, 33, 17])
check('their words, in printed order', [c for _, _, c in BEAR], ['four', 'one', 'thirty-three', 'seventeen'])
check('SUM of the four printed E values', sum(E for _, E, _ in BEAR), 55)
w55 = [i for i in range(s4, e4) if 'Fifty-five cells are named' in M[i - 1]]
check('§32.1.4 prints the total as a WORD, and once', len(w55), 1)
print('   L%d %s' % (w55[0], norm(M[w55[0] - 1])[:96]))
check('the four rows the total is built from are exactly the four §32.1.4 names',
      [n for n, _, _ in BEAR],
      ['Appendix D, unfibred', 'Appendix E (Q), unfibred', 'Appendix F, the numbers', 'the audit set, at four coordinates'])
print('   ORIGIN OF 55: §32.1.4\'s own table. 4 + 1 + 33 + 17 = 55, exact, from values printed on the page.')

# ------------------------------------------------------------------ §2
hr('§2 §32.1.4.1\'s THREE-STATE TABLE — the 48 and which components moved')
T3 = {}
for i in range(s41, e41):
    mm = re.match(r'^\s{2}(\S.*?)\s{2,}(\S+)\s+(\S+)\s+(\S+)\s*$', M[i - 1])
    if mm and not M[i - 1].startswith('   **'):
        T3[norm(mm.group(1))] = (mm.group(2), mm.group(3), mm.group(4))
HDRK = next(k for k in T3 if k.startswith('figure'))
for k, v in T3.items():
    if k == HDRK: print('   %-38s %-14s %-20s %s' % ('(header)', v[0], v[1], v[2])); continue
    print('   %-38s before intake %-12s before compression %-12s now %s' % (k, v[0], v[1], v[2]))
check('the three-state table has a header row and seven figures', len(T3), 8)
check('E over the numbers index, three states', T3.get('E over the numbers index'), ('33', '21', '23'))
check('E(Q), unfibred, three states', T3.get('E(Q), unfibred'), ('1', '1', '4'))
check('every figure about Λ is identical across the three states',
      [T3[k][0] == T3[k][1] == T3[k][2] for k in ('E(Λ)', '|Λ|', 'generators |J(Λ)|', 'surplus, bits per cell')],
      [True, True, True, True])
w48 = [i for i in range(s41, e41) if 'Recomputed now the total is' in M[i - 1]]
check('§32.1.4.1 states the recomputed total, once', len(w48), 1)
print('   L%d %s' % (w48[0], norm(M[w48[0] - 1])[:110]))
check('the recomputed total as printed', re.search(r'total is (\d+)', M[w48[0] - 1]).group(1), '48')
# the 48 reconstructed: the table moves TWO of the four components and is silent on the other two
NOW = {'Appendix D, unfibred': 4, 'Appendix E (Q), unfibred': int(T3['E(Q), unfibred'][2]),
       'Appendix F, the numbers': int(T3['E over the numbers index'][2]), 'the audit set, at four coordinates': 17}
check('48 reconstructed from the "now" column, D unfibred and the audits carried unmoved',
      sum(NOW.values()), 48)
check('the two components §32.1.4.1 does NOT restate',
      sorted(k for k in NOW if k not in ('Appendix E (Q), unfibred', 'Appendix F, the numbers')),
      ['Appendix D, unfibred', 'the audit set, at four coordinates'])
print('   ORIGIN OF 48: §32.1.4.1 / register 373. Two of the four components move (Q 1→4, numbers 33→23);')
print('   the other two are carried at their §32.1.4 values and are not restated. 4 + 4 + 23 + 17 = 48, exact.')

# ------------------------------------------------------------------ §3
hr('§3 THE ENTRY §32.1.4 CITES — register 332, and it is where the 47 comes from')
JOIN = norm(' '.join(M[s4 - 1:e4 - 1]))   # fault 4: *Register* and *332.* sit on either side of a line break
cited = sorted({int(x) for x in re.findall(r'[Rr]egisters?\s+(\d+)', JOIN)})
cited_lw = sorted({int(x) for i in range(s4, e4) for x in re.findall(r'[Rr]egisters?\s+(\d+)', M[i - 1])})
print('   line-wise sweep (WRONG — misses a wrapped pointer):', cited_lw)
print('   registers cited inside §32.1.4:', cited)
check('§32.1.4 cites register 332', 332 in cited, True)
def entry(n, lines=None):
    L = lines if lines is not None else R
    i = next((i for i, l in enumerate(L, 1) if l.strip() == '### %d' % n), None)
    if i is None: return (None, '')
    e = next((j for j in range(i + 1, len(L) + 1) if re.match(r'^#{1,4} ', L[j - 1])), len(L) + 1)
    return (i, '\n'.join(L[i:e - 1]).strip())
for n in (332, 373, 375, 435):
    i, t = entry(n)
    print('   register %-4d Register L%-6s %s' % (n, i, norm(t)[:120]))
i332, t332 = entry(332)
check('332 states the total is a press readout', 'READOUT THE PRESS PRINTS AT EVERY BUILD' in t332, True)
check('332 states the current figure', re.search(r'BUILD — (\d+) AT THE TIME OF WRITING', t332).group(1), '47')
check('332 states the figure it replaced', re.search(r'HAVING BEEN (\d+) WHEN THIS SECTION WAS FIRST COMPUTED', t332).group(1), '55')
check('332 carries the shape sentence', 'the audit set seventeen' in t332, True)
print('   ORIGIN OF 47: register 332 — the entry §32.1.4 itself cites. It is a PRESS READOUT, and 332 is')
print('   its only statement of provenance. Register 375 restates it; it does not originate it.')

# ------------------------------------------------------------------ §4
hr('§4 THE CHRONOLOGY OF THE TOTAL — append-only entry order, so the sequence is the record\'s own')
seq = [('§32.1.4 as first computed (332\'s own words)', 55, i332),
       ('register 332, a press readout', 47, i332),
       ('register 373 / §32.1.4.1', 48, entry(373)[0]),
       ('register 375, discharging §2.21', 47, entry(375)[0])]
for lab, v, ln in seq: print('   %-46s %3d   Register L%s' % (lab, v, ln))
check('entry order 332 < 373 < 375', [entry(332)[0] < entry(373)[0], entry(373)[0] < entry(375)[0]], [True, True])
check('the total is NOT monotone across the record', [v for _, v, _ in seq], [55, 47, 48, 47])
print('   The record has the total at 47 BEFORE it has it at 48. 375\'s 47 is not a further movement from 48;')
print('   it is 332\'s figure restated after 373 printed a higher one. THAT is why three totals stand at once.')

# ------------------------------------------------------------------ §5
hr('§5 THE SHAPE SENTENCE — 26c-02 said it appears in no volume. Swept over all six volumes and PP')
SHAPE = 'the audit set seventeen'
sites = []
for v in VOLS:
    L = rd(v)
    for i, l in enumerate(L, 1):
        if SHAPE.lower() in l.lower(): sites.append((nvol(v), i))
for i, l in enumerate(P, 1):
    if SHAPE.lower() in l.lower(): sites.append(('PP', i))
for vn, i in sites: print('   %-12s L%-6d %s' % (vn, i, norm((rd([v for v in VOLS if nvol(v) == vn][0])[i - 1] if vn != 'PP' else P[i - 1]))[:104]))
check('sites of the shape sentence across six volumes and PP', len(sites), 2)
check('the volumes carrying it', sorted({vn for vn, _ in sites}), ['The_Register'])
check('sites in the main volume\'s chapters', len([1 for vn, _ in sites if vn == 'main']), 0)
check('sites in Prints & Proofs', len([1 for vn, _ in sites if vn == 'PP']), 0)
check('the two Register sites are entries 332 and 375',
      sorted({n for n in (332, 373, 375, 435) if SHAPE in entry(n)[1]}), [332, 375])
score('26c-02 as recorded: the shape sentence appears in NO VOLUME', len(sites) == 0, True, '32a-01')
print('   32a-01 CORRECTS 26c-02. The sentence has TWO sites, both in the Register (332 and 375). What is')
print('   true, and is what the finding meant, is that §32.1.4 does not carry it: 0 sites in any chapter,')
print('   0 in the other four compendia, 0 in Prints & Proofs. A claim about a volume is not a claim about')
print('   a section, and the recorded wording scored the wrong object.')

# ------------------------------------------------------------------ §6
hr('§6 IS 47 REPRODUCIBLE? Every PRINTED value of each of the four components, and every sum they reach')
COMP = {'Appendix D, unfibred': r'E\(D\) = (\d+) unfibred|Appendix D, unfibred\s+(\d+)',
        'Appendix E (Q), unfibred': r'E\(Q\) = (\d+) unfibred|E\(Q\), unfibred\s+(\d+)',
        'Appendix F, the numbers': r'E over the numbers index\s+(\d+)\s+(\d+)\s+(\d+)',
        'the audit set, at four coordinates': r'E\(audits\)\s*(?:=|read|at|,\s*then)\s*(\d+)'}
VALS = {}
for k, pat in COMP.items():
    found = {}
    for v in VOLS:
        L = rd(v)
        for i, l in enumerate(L, 1):
            for mm in re.finditer(pat, l):
                for g in mm.groups():
                    if g: found.setdefault(int(g), []).append('%s L%d' % (nvol(v), i))
    # the table rows themselves
    for _, n, _, E, _ in ROWS:
        if n == k: found.setdefault(E, []).append('main L(table)')
    VALS[k] = found
    print('   %-38s printed values %s' % (k, sorted(found)))
for k in VALS: check('%s has at least one printed value' % k, len(VALS[k]) > 0, True)
reach = {}
for combo in itertools.product(*[sorted(VALS[k]) for k in NOW]):
    reach.setdefault(sum(combo), []).append(combo)
for t in (47, 48, 55):
    print('   total %d reachable by %d printed assignment(s): %s' % (t, len(reach.get(t, [])), reach.get(t, [])))
check('55 is reachable from printed values', 55 in reach, True)
check('48 is reachable from printed values', 48 in reach, True)
check('47 is reachable from printed values', 47 in reach, True)
S47 = reach.get(47, []); S48 = reach.get(48, []); S55 = reach.get(55, [])
AI = list(NOW).index('the audit set, at four coordinates')
NI = list(NOW).index('Appendix F, the numbers')
QI = list(NOW).index('Appendix E (Q), unfibred')
print('   Every assignment reaching 47, and whether it agrees with the shape sentence the same entries assert:')
for c in S47:
    print('      %-22s audits = %-3d  %s' % (str(c), c[AI],
          'CONTRADICTS 375\'s own *the audit set seventeen*' if c[AI] != 17 else 'AGREES with *the audit set seventeen*'))
SHAPE_OK = [c for c in S47 if c[AI] == 17]
check('assignments reaching 47 that keep the audits at seventeen', len(SHAPE_OK), 1)
check('the shape-consistent assignment reaching 47', SHAPE_OK[0], (4, 5, 21, 17))
check('55 is reached by exactly one printed assignment, the table itself', S55, [(4, 1, 33, 17)])
check('48 is reached by more than one printed assignment', len(S48) > 1, True)
check('47 is reached by more than one printed assignment', len(S47) > 1, True)
# where do the shape-consistent 47's two moving components come from?
src_numbers = [w for v, w in VALS['Appendix F, the numbers'].items() if v == SHAPE_OK[0][NI]][0]
src_q = [w for v, w in VALS['Appendix E (Q), unfibred'].items() if v == SHAPE_OK[0][QI]][0]
print('   numbers index = %d printed at: %s' % (SHAPE_OK[0][NI], src_numbers))
print('   E(Q) unfibred = %d printed at: %s' % (SHAPE_OK[0][QI], src_q))
check('the numbers-index value in that assignment is §32.1.4.1\'s BEFORE-COMPRESSION column, not its NOW column',
      (SHAPE_OK[0][NI], int(T3['E over the numbers index'][1]), int(T3['E over the numbers index'][2])), (21, 21, 23))
print('   32a-02 NEW, AND IT IS THE ANSWER TO THE RULING. Of the three totals, only 55 is uniquely determined')
print('   by printed values — one assignment, §32.1.4\'s own table, (4, 1, 33, 17). 48 is reached by three')
print('   printed assignments and 47 by two, so neither is recoverable from the page without choosing a state.')
print('   The ONLY assignment reaching 47 that agrees with the shape sentence 332 and 375 both assert is')
print('   (D 4, Q 5, numbers 21, audits 17) — and it MIXES TWO STATES: the numbers index at 21 is')
print('   §32.1.4.1\'s BEFORE-COMPRESSION column, while E(Q) unfibred at 5 is §32.6.1 / register 396\'s')
print('   readout at *the build that produced this page*, which is after compression. So the 47 is not a')
print('   reading taken at one moment, which is the very thing §32.1.4.1 says a figure about the book must be.')
print('   32a-02a, the corollary that decides it: a readout is reproducible only if its inputs are printed at')
print('   ONE state. Three totals stand at once because the record prints components from four states and a')
print('   total from three of them.')
print('   FAULT OF MINE, CAUGHT BEFORE BANKING AND NAMED (fault 5): the draft of this section asserted that')
print('   NO shape-consistent assignment reaches 47 and would have recorded 47 as flatly unreproducible. The')
print('   scan found (4, 5, 21, 17). The scan was right and the assertion was corrected to the measurement.')

# ------------------------------------------------------------------ §7
hr('§7 WHOSE READOUT — the instrument that computes the largest component, and whether the build holds it')
i435, t435 = entry(435)
print('   register 435 Register L%d: %s' % (i435, norm(t435)[:200]))
check('435 records the two readout scripts as having been ABSENT', 'WERE ABSENT AND ARE REBUILT' in t435.upper(), True)
check('435 names the numbers-index script', 'numbers-index.py' in t435, True)
check('435 names the densities script', 'densities.py' in t435, True)
NAMED = ['numbers-index.py', 'densities.py', 'indices.py', 'appendix_audit.py', 'mathreg.py', 'compendium.py',
         'register_gen.py', 'guard.py', 'register_cites.py', 'kinds.py', 'build.py', 'close.py']
present = {n: os.path.exists(os.path.join(H, n)) for n in NAMED}
for n, p in present.items(): print('   %-22s %s' % (n, 'MEMBER' if p else 'NOT A MEMBER OF THIS BUILD'))
check('numbers-index.py is a member', present['numbers-index.py'], False)
check('densities.py is a member', present['densities.py'], False)
check('build.py IS a member', present['build.py'], True)
# build.py computes nothing numeric: it is a prose-substitution press
bp = open(os.path.join(H, 'build.py'), encoding='utf-8').read()
check('build.py names numbers-index.py only inside a prose substitution', "numbers-index.py" in bp, True)
check('build.py contains no arithmetic on the four components',
      any(t in bp for t in ('E(audits)', 'E_num', 'numbers_index(', 'def readout')), False)
print('   32a-03 NEW. The four components of §32.1.4\'s total are computed by `numbers-index.py` and its')
print('   companions, and register 435 records that those scripts WERE ABSENT and were REBUILT FROM THE')
print('   PRINTED RULES. Neither is a member of this build. `build.py`, which IS a member, is a')
print('   prose-substitution press and computes none of them — it only strips the script names from')
print('   reader-facing prose. So the origin of the 47 is a reconstruction of an absent instrument, and')
print('   the total cannot be re-derived from the artefact as delivered. Docket 38, not docket 12.')

# ------------------------------------------------------------------ §8
hr('§8 REGISTER 332\'s OWN TEXT — read entire, as docket 9(b) asks')
print('   ' + norm(t332))
check('332\'s body carries a joined word where a sentence was lost', 'indicessince' in t332, True)
print('   32a-04 NEW. Register 332 reads *Across its six indicessince been confirmed by occupants arriving.*')
print('   — two sentences collapsed with text lost between *indices* and *since*. The entry §32.1.4 cites')
print('   for its total is itself damaged at the point where it would say how many of the cells have since')
print('   been filled. Append-only: a new entry citing 332 restores the sentence; 332 is not edited.')

# ------------------------------------------------------------------ §9
hr('§9 CENSUS ROWS IN RANGE — DEFECT-CENSUS.tsv rows whose main line lies in §32.1.4–§32.1.4.1')
cen = [l.split('\t') for l in rd('DEFECT-CENSUS.tsv') if l.strip()]
hdr = cen[0]; li = hdr.index('line') if 'line' in hdr else 2
inr = [r for r in cen[1:] if r[1] == 'main' and r[li].isdigit() and s4 <= int(r[li]) < e41]
for r in inr: print('   id %-6s main L%-6s %s' % (r[0], r[li], ' '.join(r[3:])[:100]))
print('   rows in range: %d' % len(inr))

# ------------------------------------------------------------------ verdict
hr('VERDICT')
print('   integrity checks: %s' % ('ALL OK' if not FAIL else 'FAILED: ' + '; '.join(FAIL)))
print('   deviations recorded: %d' % len(DEV))
for tagno, tag, got, exp in DEV: print('      %s  %s — measured %r, printed %r' % (tagno, tag, got, exp))
print('   ORIGINS, the ruling\'s answer:')
print('      55  §32.1.4\'s own table, 4 + 1 + 33 + 17, exact — the state when the section was first computed')
print('      48  §32.1.4.1 / register 373, 4 + 4 + 23 + 17 — two components moved, two carried unrestated')
print('      47  register 332\'s press readout — the entry §32.1.4 itself cites, on a wrapped pointer;')
print('          restated at 375, which does not originate it. Reached by two printed assignments, and the')
print('          only one agreeing with 332\'s and 375\'s own shape sentence is (4, 5, 21, 17), which mixes')
print('          two states of the book. Computed by `numbers-index.py`, which register 435 records as')
print('          having been absent and rebuilt from the printed rules and which is not a member.')
print('   AND THE SHAPE OF THE ANSWER: 55 is the only one of the three a reader can reconstruct. The section')
print('   prints the one total that is reproducible and cites the entry that says it is no longer the number.')
sys.exit(1 if FAIL else 0)
