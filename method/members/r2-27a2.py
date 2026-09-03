#!/usr/bin/env python3
# r2-27a2.py — chat 153 — SUCCESSOR to r2-27a.py, re-anchored. Identical measurements; one pin moves.
# r2-27a pinned Appendix G's first line to the literal 11361. r3-wl2's +8 shift moved it to 11369, so the
# instrument exits 1 on a position that is no longer wrong-in-fact, only wrong-as-pinned.
# The replacement is NOT the resolver's own value — that would be a test that cannot fail, the very
# class §4.6 names. It is an INDEPENDENT resolution of the same site, so the two can disagree and the
# check still catches a mis-read. Output on the pre-shift bundles is unchanged, because both agree there.
# r2-27a is seated and is never edited in place (chat 68).
# PROVED by tools/proveanchor.py: reproduces r2-27a.out byte-exact on the pre-shift bundles (G0c).
# r2-27a.py — chat 151-B (Cowork) — 27a-02 (DEF-143 item 11's SEVENTH family; docket 9(b) / 35):
# Appendix G rows 8.2, 8.4 and 10.4c name seven Register entries in their "what rests on it" column, and
# READ-ch27a measured that NONE of the seven carries any of its row's words. That was a TOKEN PROBE, stated
# as such, and DEF-151's predecessor recorded what is owed: "read the seven entries for dependence on
# T §8.2 / §8.4 / §10.4c before scoring". This instrument is that reading.
# THE COLUMN IS "WHAT RESTS ON IT", so the question is DEPENDENCE, not vocabulary. A word probe cannot settle
# it in either direction: an entry may rest on a section without repeating a syllable of it, and may repeat
# every word of it while resting on something else. The convention below is stated before anything is scored.
# CONVENTION DEP (new, this chat). An entry RESTS ON section S if either
#   DEP-N  it NAMES the source — "Transitions", "T <n>", "App. G", or the section number itself; or
#   DEP-M  its own deciding sentence is an instance or a consequence of the MECHANISM S establishes,
# and in both cases the instrument asserts the deciding phrase is present in that entry's own text. An entry
# the reading cannot decide is carried as NEAR — an upper bound, never assigned (SUBJ, chat 148).
# The three mechanisms, taken from the sections themselves and asserted present in Transitions.md below:
#   §8.2   a scope condition is an extra coordinate, so a jurisdicted theorem is inherently ternary, and
#          arity >= 3 is what makes a defect possible while jurisdiction narrowness is what makes it small
#   §8.4   a locally covariant QFT is a functor Loc -> Alg with exactly four parts, replacing the
#          seven-vocabulary partition
#   §10.4c the presymplectic potential on a null surface carries no transverse derivative, so Omega is block
#          diagonal and the algebra factorises over generators
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
MC, TR = 'The_Method_1_6___Mathematical_Compendium-2.md', 'Transitions.md'
VOLS = [MAIN, REG, MC, 'The_Method_1_6___The_Physics_Compendium-2.md',
        'The_Method_1_6___Spectra_Compendium-2.md', 'The_Method_1_6___The_Index_of_Indices-2.md']
M, R, T, C = rd(MAIN), rd(REG), rd(TR), rd(MC)
FAIL = []; DEV = []
def check(tag, got, exp):
    ok = got == exp
    print('   %-64s %-26s %s' % (tag, repr(got), 'OK' if ok else 'EXPECTED ' + repr(exp)))
    if not ok: FAIL.append(tag)
def score(tag, got, exp, tagno):
    ok = got == exp
    print('   %-64s %-26s %s' % (tag, repr(got), 'as printed' if ok else 'DEVIATION (%s) — printed %s' % (tagno, repr(exp))))
    if not ok: DEV.append((tagno, tag, got, exp))

print('r2-27a.py — 27a-02: do the seven Register entries Appendix G names actually rest on the sections?')
print('members: %s %s | %s %s | %s %s | %s %s' % (MAIN, md5(MAIN), REG, md5(REG), TR, md5(TR), MC, md5(MC)))

# ------------------------------------------------------------------ §1
hr('§1 THE THREE ROWS, located by scan this chat — the seven numbers are read OUT of the rows, never carried in')
GA = [i for i, l in enumerate(M, 1) if re.match(r'^#{1,4}\s', l) and l.strip().endswith('Appendix G — Transitions, indexed')][-1]
EM = [i for i, l in enumerate(M, 1) if l.strip() == '# END MATTER']
GEND = min(i for i in EM if i > GA)
G = M[GA - 1:GEND - 1]
_ga_alt = [i for i, l in enumerate(M, 1) if re.match(r'^#{1,4}\s+Appendix G\b', l)][-1]
check('Appendix G first line', GA, _ga_alt)
check('Appendix G line count (to `# END MATTER`)', len(G), 46)
rows = {}
for k, l in enumerate(G):
    m = re.match(r'^\|\s*([\d.]+[a-z]?)\s*\|(.*)\|(.*)\|\s*$', l)
    if m: rows[m.group(1)] = (GA + k, norm(m.group(2)), norm(m.group(3)))
check('DATA rows in Appendix G', len(rows), 30)
WANT = ['8.2', '8.4', '10.4c']
check('the three rows are present', [w in rows for w in WANT], [True, True, True])
cited = {}
for w in WANT:
    ln, states, rests = rows[w]
    cited[w] = [int(x) for x in re.findall(r'\d+', re.sub(r'^.*?Register', '', rests))] if 'Register' in rests else []
    print('   row %-5s L%-6d rests on: %s' % (w, ln, rests))
    print('        states: %s' % states[:150])
check('row 8.2 cites', cited['8.2'], [1375, 1519, 1523, 1535, 1551])
check('row 8.4 cites', cited['8.4'], [1375])
check('row 10.4c cites', cited['10.4c'], [1399, 1403])
SEVEN = sorted(set(cited['8.2'] + cited['8.4'] + cited['10.4c']))
check('the seven distinct entries the column names', SEVEN, [1375, 1399, 1403, 1519, 1523, 1535, 1551])

# ------------------------------------------------------------------ §2
hr('§2 THE SECTIONS — each row claims to restate its section; the mechanism is taken from Transitions itself')
sec = {}
for w in WANT:
    hits = [i for i, l in enumerate(T, 1) if re.match(r'^###\s+' + re.escape(w) + r'\s', l)]
    e = next((i for i, l in enumerate(T, 1) if i > hits[0] and re.match(r'^#{2,4}\s', l)), len(T) + 1)
    sec[w] = (hits[0], e, norm(' '.join(T[hits[0] - 1:e - 1])))
    print('   T §%-5s L%-5d-L%-5d  %s' % (w, hits[0], e - 1, norm(T[hits[0] - 1])[:90]))
check('§8.2 states the ternary mechanism', 'inherently ternary, and no further physics removes the scope' in sec['8.2'][2], True)
check('§8.2 states arity is what makes a defect possible', 'Arity ≥ 3 is what makes a defect *possible*' in sec['8.2'][2], True)
check('§8.4 states the four-part functor', 'that object has exactly four parts' in sec['8.4'][2], True)
check('§10.4c states the null-surface factorisation', 'no transverse' in sec['10.4c'][2] and 'block diagonal' in sec['10.4c'][2], True)
for w in WANT:
    key = {'8.2': 'inherently ternary', '8.4': 'exactly four parts', '10.4c': 'block diagonal'}[w]
    check('row %s restates its section (the row is not itself in doubt)' % w, key in rows[w][1] or key.split()[-1] in rows[w][1], True)

# ------------------------------------------------------------------ §3
hr('§3 THE TOKEN PROBE REPRODUCED — READ-ch27a\'s word sets, and where those words actually live')
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
WORDS = {'8.2':   [r'jurisdict\w*', r'forcing', r'disjunction', r'ternary', r'scope'],
         '8.4':   [r'vocabular\w*', r'functor', r'covariant', r'four parts'],
         '10.4c': [r'\bC1\b', r'presymplectic', r'null surface', r'transverse', r'block diagonal', r'factoris\w*']}
probe = {}
for w in WANT:
    for n in cited[w]:
        hitw = [p for p in WORDS[w] if re.search(p, BODY[n], re.I)]
        probe[(w, n)] = hitw
        print('   row %-5s register %-5d row-words present: %s' % (w, n, hitw or 'none'))
check('chat 139\'s probe: any row word in any cited entry', sorted({k for k, v in probe.items() if v}), [])
for pat, nm in ((r'jurisdict\w*', 'jurisdict*'), (r'presymplectic', 'presymplectic'), (r'null surface', 'null surface')):
    where = [n for n in KS if re.search(pat, BODY[n], re.I)]
    print('   "%s" actually lives at register(s): %s' % (nm, where))
check('*jurisdict\\** has exactly one Register home', [n for n in KS if re.search(r'jurisdict\w*', BODY[n], re.I)], [543])
check('*presymplectic* has exactly one Register home', [n for n in KS if re.search(r'presymplectic', BODY[n], re.I)], [1511])
print('   A word probe cannot settle "rests on" in either direction. The reading follows.')

# ------------------------------------------------------------------ §4
hr('§4 THE READING — every cited entry scored for DEPENDENCE under CONVENTION DEP, with a deciding phrase')
print('   DEP-N  names the source: "Transitions", "T <n>", "App. G", or the section number')
print('   DEP-M  its deciding sentence is an instance or consequence of the section\'s mechanism')
print('   NEAR   the reading cannot decide; carried as an upper bound, never assigned')
print('   NOT    another mechanism entirely\n')
SC = [
 ('8.2', 1375, 'NOT',  'THE DUAL OF A.DEFINE',
  'a rung-1 coordinate and its injective dual, both contributing no envelope — A.define\'s degeneracy, not a scope condition'),
 ('8.2', 1519, 'NEAR', "which is Freuder's classical result",
  'treewidth one and the Helly number: the SAME arity mechanism read from the low side, but credited to Freuder and derived from register 507, not from §8.2'),
 ('8.2', 1523, 'NEAR', 'Λ at max clique 1',
  'the conflict graph as a shared measure over three topics — arity again, and it names M.C2, whose section is §10.4d and not §8.2'),
 ('8.2', 1535, 'NOT',  'A NILSSON SHELL N ADMITS ONLY',
  'a parity check on a supplied nuclear table; no constraint arity, no jurisdiction, no scope'),
 ('8.2', 1551, 'NOT',  "K I's QUANTUM DEFECTS",
  'an outside companion paper matching a quantum-defect extrapolation; a spectra capture'),
 ('8.4', 1375, 'NOT',  'THE DUAL OF A.DEFINE',
  'the same entry again, and it carries no vocabulary, no functor and no partition of any size'),
 ('10.4c', 1399, 'NOT', 'the sequence as printed was not one measurement',
  'two tower conventions printed as one sequence; an arithmetic collision, not a null-surface algebra'),
 ('10.4c', 1403, 'NOT', "the corridor's lower endpoint",
  'where a sits in the Λ_T corridor, on eight recorded values; no presymplectic potential and no generator algebra'),
]
check('the reading scores every (row, entry) pair the column names exactly once',
      sorted((w, n) for w, n, *_ in SC), sorted((w, n) for w in WANT for n in cited[w]))
miss = []
for w, n, verdict, phrase, why in SC:
    ok = phrase.lower() in BODY[n].lower()
    if not ok: miss.append((n, phrase))
    print('   §%-5s %-5d %-5s "%s"' % (w, n, verdict, phrase))
    print('               %s' % why)
check('every deciding phrase present in its own entry', miss, [])
named = [(w, n) for w, n, *_ in SC if re.search(r'Transitions|App\. G|\bT \d', BODY[n])]
check('entries that NAME the source (DEP-N)', named, [])
depm = [(w, n) for w, n, v, *_ in SC if v == 'DEP-M']
check('entries whose deciding sentence is an instance of the mechanism (DEP-M)', depm, [])
nears = [(w, n) for w, n, v, *_ in SC if v == 'NEAR']
nots = [(w, n) for w, n, v, *_ in SC if v == 'NOT']
print('\n   DEP-N %d | DEP-M %d | NEAR %d %s | NOT %d' % (len(named), len(depm), len(nears), nears, len(nots)))
score('the column "what rests on it" is true of the entries it names',
      len(named) + len(depm), len(SC), '27a-02')

# ------------------------------------------------------------------ §5
hr('§5 EVERY WARNING ON EVERY CITED ENTRY (docket 9(b) / 35 asks for exactly this)')
warns = {}
for n in SEVEN:
    s, e = span(n)
    warns[n] = [(i, norm(R[i - 1])) for i in range(s + 1, e + 1) if 'WARNING' in R[i - 1].upper()]
    print('   register %-5d WARNING lines: %d' % (n, len(warns[n])))
check('cited entries carrying a WARNING', [n for n in SEVEN if warns[n]], [1403])
w1403 = warns[1403][0][1]
print('   R%d: %s' % (warns[1403][0][0], w1403[:210]))
check('1403\'s WARNING is that the a values are reconstructions',
      'RECONSTRUCTION' in w1403.upper(), True)
r104c = rows['10.4c'][2]
score('row 10.4c restates the qualification on the entry it cites',
      any(t in r104c.lower() for t in ('reconstruct', 'warning', 'not measurement')), True, '27a-02')

# ------------------------------------------------------------------ §6
hr('§6 THE CANDIDATES — what the Mathematical Compendium\'s own C1 / C2 block rests on')
led = [i for i, l in enumerate(C, 1) if l.strip() == '### The modular ledger']
e = next((i for i, l in enumerate(C, 1) if i > led[0] and re.match(r'^###\s', l)), len(C) + 1)
blk = norm(' '.join(C[led[0] - 1:e - 1]))
cand = sorted({int(x) for x in re.findall(r'(?:[Rr]egisters?|R)\s+(\d{3,4})', blk)})
print('   MC "The modular ledger" L%d-L%d cites: %s' % (led[0], e - 1, cand))
check('the block names T 10.4e and Appendix G as its source', 'T 10.4e (App. G)' in blk, True)
check('none of the seven is among the registers that block cites', sorted(set(cand) & set(SEVEN)), [])
bib = [(i, norm(l)) for i, l in enumerate(C, 1) if re.search(r'`(M\.C1|M\.C2|W\.jur|W\.rel)`', l)]
for i, l in bib: print('   MC L%-6d %s' % (i, l[:120]))
print('   The row\'s own labels resolve to prior art — W.jur to Freuder 1978, W.rel to Fredenhagen & Verch')
print('   2003, M.C1 to Wald & Zoupas 2000 — and the C1 / C2 work rests on %s, none of which the row names.' % cand)

# ------------------------------------------------------------------ verdict
hr('VERDICT')
print('   27a-02 STANDS, and the reading is stronger than the probe that recorded it. Of the eight (row, entry)')
print('   pairs the column asserts, **0 are DEP-N and 0 are DEP-M**: not one of the seven entries names')
print('   Transitions, its section, or Appendix G, and not one has a deciding sentence that is an instance or a')
print('   consequence of the mechanism its row states. %d are another mechanism entirely and %d are carried as' % (len(nots), len(nears)))
print('   an upper bound and never assigned — 1519, whose treewidth-one result is the same arity mechanism read')
print('   from the low side but credited to Freuder and to register 507, and 1523, whose conflict-graph measure')
print('   is arity again and which names M.C2, an object of §10.4d rather than of §8.2.')
print('   27a-07 NEW. The Mathematical Compendium\'s own "modular ledger" block names T 10.4e (App. G) as its')
print('   source and rests on registers %s. Row 10.4c names 1399 and 1403 instead,' % cand)
print('   and the two sets are disjoint: the compendium and the appendix disagree about what rests on the')
print('   section, and the appendix is the volume that calls itself the address.')
print('   27a-08 NEW. Register 1403 is the only one of the seven carrying a WARNING — its eight a values are')
print('   RECONSTRUCTIONS and not measurements — and row 10.4c prints it as an object resting on a computed')
print('   result without restating the qualification. Docket 35: a citer either restates it or drops the citation.')
print('\nDEVIATIONS RECORDED (findings, not instrument faults):')
for t, tag, got, exp in DEV: print('   %-8s %-58s measured %s against printed %s' % (t, tag, repr(got), repr(exp)))
print('\n%s' % ('FAIL: ' + '; '.join(FAIL) if FAIL else 'ALL INSTRUMENT CHECKS OK — %d deviations recorded' % len(DEV)))
sys.exit(1 if FAIL else 0)
