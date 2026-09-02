#!/usr/bin/env python3
# r2-scf.py — chat 144 — the SCF chain (RUL-128 item 3 (ii), second half, second family): Register 1701–1712 and Chapter 35,
# every printed figure censused and re-derived on the instruments the bundle holds. Reads MEMBERS by name (never a bundle
# path). Deterministic: no wall clock, no randomness. Decimal for every printed figure, never round(). Every convention is
# named before a figure is scored. A re-derivation that disagrees with a Register entry is a finding about the re-derivation
# (G0c); a figure whose instrument is not held is UNREPRODUCIBLE with a stated budget, never withdrawn. Held inputs: the
# delivered OBSERVED configurations LW1-ground.py (Register 1306, NIST ASD 5.12; READ not computed) and tower-2 via r2lib.
import os, re, sys, math, hashlib, importlib.util
from decimal import Decimal, getcontext, ROUND_HALF_EVEN
getcontext().prec = 40
H = os.path.dirname(os.path.abspath(__file__))
def load(name):
    s = importlib.util.spec_from_file_location(name.replace('-', '_'), os.path.join(H, name + '.py'))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
r2lib = load('r2lib'); G = load('LW1-ground')
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
def md5(n): return hashlib.md5(open(os.path.join(H, n), 'rb').read()).hexdigest()[:8]
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
MC = 'The_Method_1_6___Mathematical_Compendium-2.md'; PC = 'The_Method_1_6___The_Physics_Compendium-2.md'
IOI = 'The_Method_1_6___The_Index_of_Indices-2.md'; SC = 'The_Method_1_6___Spectra_Compendium-2.md'
M = rd(MAIN); R = rd(REG)
def hr(t): print('\n' + '=' * 100 + '\n' + t + '\n' + '=' * 100)
def D(x, places): return Decimal(x).quantize(Decimal(1).scaleb(-places), rounding=ROUND_HALF_EVEN)

def rbody(n):   # copied verbatim from r2-ch34re.py (there from r2-warn.py … r2-ch17b.py; owed to r2lib, DEFERRED): first non-blank line after '### n'
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())

def body_range(M, sec):   # copied verbatim from r2-ch34re.py (there from r2-warn.py … r2-ch16z.py; owed to r2lib, DEFERRED): heading to next heading of any rank, body occurrence
    s = r2lib.heading_line(M, sec)
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1]): return (s, i)
    return (s, len(M) + 1)

def lettered(M, tag):   # copied verbatim from r2-ch34re.py (there from r2-warn.py … r2-ch17c.py; owed to r2lib, DEFERRED): lettered heading, exact token, hits in order; body = LAST
    hits = [i for i, l in enumerate(M, 1) if re.match(r'^#{2,4}\s*' + re.escape(tag) + r'(?!\.\d)(?!\d)\b', l)]
    return hits

hr('§0 IDENTITY AND BOUNDARIES')
for n in (MAIN, REG, MC, PC, IOI, SC, 'LW1-ground.py', 'r2lib.py', 'tower-2.py'): print('  %-52s md5 %s  %d lines' % (n, md5(n), len(rd(n))))
T = r2lib.load_tower(); print('  tower-2 loaded via r2lib.load_tower():', 'tower2' in repr(T))
hl = r2lib.heading_line(M, '35'); ss = r2lib.section_span(M, '35'); br = body_range(M, '35')
print('  heading_line(35) =', hl, repr(M[hl - 1]), '| all exact-token hits', [i for i, t in enumerate(M, 1) if re.match(r'^#{1,4} 35\.? ', t.strip())], '(the contents hit discarded; body occurrence governs)')
print('  section_span(35) =', ss, '-> next heading', repr(M[ss[1] - 1]), '| body_range(35) =', br, '-> next heading', repr(M[br[1] - 1]))
print('  the two resolvers differ by', ss[1] - br[1], 'lines — section_span governs the census')
heads = [(i, M[i - 1]) for i in range(ss[0], ss[1]) if re.match(r'^#{1,4} ', M[i - 1])]
for k, (i, h) in enumerate(heads):
    e = heads[k + 1][0] if k + 1 < len(heads) else ss[1]
    print('   L%d-L%d %3d lines  %s' % (i, e - 1, e - i, h))
CH = M[ss[0] - 1:ss[1] - 1]; L0 = ss[0]
def find(s): return [L0 + k for k, l in enumerate(CH) if s in l]
JOIN = re.sub(r'\s+', ' ', ' '.join(CH))

hr('§1 NUMERAL CENSUS OF THE CHAPTER (digit-bounded both sides; trailing non-thousands comma admitted; count words listed separately)')
NUM = re.compile(r'(?<![\d.])(\d[\d,]*(?:\.\d+)?)(?![\d])')
rows = [(L0 + k, m.group(1)) for k, l in enumerate(CH) for m in NUM.finditer(l)]
print('  numerals:', len(rows), 'on', len({r[0] for r in rows}), 'lines')
by = {}
for ln, v in rows: by.setdefault(ln, []).append(v)
for ln in sorted(by): print('   L%d: %s' % (ln, ' '.join(by[ln])))
CW = re.compile(r'\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|hundred)\b', re.I)
cw = [(L0 + k, m.group(0)) for k, l in enumerate(CH) for m in CW.finditer(l)]
print('  count words:', len(cw), '->', ' '.join('L%d:%s' % c for c in cw))

hr('§2 THE FAMILY LOCATED — chain tokens in six volumes (word-bounded, case-insensitive), the Register entries 1701–1712, their WARNING lines')
TOK = re.compile(r'\bSCF\b|self-consistent[- ]field|\bHartree\b|\bPulay\b|\bDIIS\b|\bL[öo]wdin chain\b|\bKoelling\b', re.I)
def encl_reg(i):
    for j in range(i, 0, -1):
        m = re.match(r'^#{1,4}\s*(\d+)(?:\s*[,–—-].*)?\s*$', R[j - 1])
        if m: return m.group(1)
    return '?'
for name, V in ((MAIN, M), (REG, R), (MC, rd(MC)), (PC, rd(PC)), (IOI, rd(IOI)), (SC, rd(SC))):
    hits = [(i, l) for i, l in enumerate(V, 1) if TOK.search(l)]
    print('  %-52s %2d lines' % (name, len(hits)))
    for i, l in hits:
        where = ('entry ' + encl_reg(i)) if name == REG else r2lib.enclosing(V, i)
        toks = ' '.join(sorted({t.lower() for t in TOK.findall(l)}))
        print('     L%-5d %-12s [%s] %s' % (i, where, toks, re.sub(r'\s+', ' ', l)[:150]))
print('  Register 1701–1712 headed (### n):', ' '.join('%d:%s' % (n, 'Y' if rbody(n) else 'ABSENT') for n in range(1701, 1713)))
sp = [i for i, l in enumerate(R, 1) if l.strip() == '### 1701'][0]; ep = [i for i, l in enumerate(R, 1) if l.strip() == '### 1713'][0]
print('  span L%d-L%d; raw WARNING: markers in the span: %d' % (sp, ep - 1, sum(1 for l in R[sp - 1:ep - 1] if 'WARNING:' in l)))
BODY = {n: rbody(n) for n in range(1701, 1713) if rbody(n)}
for n in sorted(BODY):
    nums = NUM.findall(BODY[n]); print('   %d: %3d numerals: %s' % (n, len(nums), ' '.join(nums)))
RJ = ' '.join(BODY.values())

hr('§3 THE OBSERVED TABLE (LW1-ground.py, Register 1306) — the five-clause ordering law tested under NAMED conventions')
ZS = sorted(G.GROUND); print('  elements in GROUND:', len(ZS), 'Z =', ZS[0], 'to', ZS[-1], '| electron count == Z:', sum(1 for Z in ZS if G.occ_count(Z) == Z), 'of', len(ZS))
LET = 'spdfg'
def occ(Z): return {(n, l): o for n, l, o in G.expand(Z)} if Z >= 1 else {}
def name(k): return '%d%s' % (k[0], LET[k[1]])
def entrant(Z):
    """convention (chat 143): the entrant at Z is the subshell whose occupancy grows most from Z-1 to Z"""
    a, b = occ(Z - 1), occ(Z)
    d = {k: b.get(k, 0) - a.get(k, 0) for k in set(a) | set(b)}
    return max(sorted(d), key=lambda k: d[k])
steps = list(range(2, ZS[-1] + 1)); print('  steps Z = 2..%d: %d (1702: 107 SCORED; the chapter: 107 of 107)' % (ZS[-1], len(steps)))
opened = {}
for Z in ZS:
    for k in occ(Z):
        opened.setdefault(k, Z)
seq = sorted(opened, key=lambda k: opened[k])
print('  opening sequence (%d subshells, first occupancy):' % len(seq), ' '.join('%s@%d' % (name(k), opened[k]) for k in seq))
CAND = [(n, l) for n in range(1, 9) for l in range(0, min(n, 4))]
def nl(k): return k[0] + k[1]
# convention A — OPENING LEVEL: the clauses are read on the sequence of first occupancies
excA1 = [name(seq[i]) + '>' + name(seq[i + 1]) for i in range(len(seq) - 1) if nl(seq[i]) > nl(seq[i + 1])]
excA2 = [(G.GROUND[opened[k]][0], opened[k], name(k), name(c)) for k in seq for c in CAND if nl(c) == nl(k) and c[0] < k[0] and opened.get(c, 10 ** 9) > opened[k]]
print('  A (opening level): clause 1 n+l non-decreasing along the sequence — exceptions:', excA1 or 'NONE')
print('     clause 2 smaller n first at equal n+l — exceptions (element Z opened rival):', ' '.join('%s %d %s over %s' % e for e in excA2) or 'NONE')
# convention B — PER STEP, ALL CHANNELS: the entrant at Z against every candidate not yet full at Z-1
def excB():
    e1, e2 = [], []
    for Z in steps:
        g = entrant(Z); a = occ(Z - 1)
        rivals = [c for c in CAND if a.get(c, 0) < 2 * (2 * c[1] + 1) and c != g]
        if any(nl(c) < nl(g) for c in rivals): e1.append('%s%d' % (G.GROUND[Z][0], Z))
        if any(nl(c) == nl(g) and c[0] < g[0] for c in rivals): e2.append('%s%d' % (G.GROUND[Z][0], Z))
    return e1, e2
b1, b2 = excB()
print('  B (per step, every unfilled rival): clause 1 exceptions (%d): %s' % (len(b1), ' '.join(b1) or 'NONE'))
print('     clause 2 exceptions (%d): %s' % (len(b2), ' '.join(b2) or 'NONE'))
# convention C — PER STEP, RIVAL EMPTY AT Z-1: a rival counts while its occupancy at Z-1 is zero (whether or not it was occupied earlier)
# convention C' — PER STEP, NEVER-YET-OPENED RIVAL (DEF-128 item 2, 17a-01's wording): a rival counts only if its first occupancy lies after Z
def excC(never_opened):
    e1, e2 = [], []
    for Z in steps:
        g = entrant(Z); a = occ(Z - 1)
        rivals = [c for c in CAND if c != g and (opened.get(c, 10 ** 9) > Z if never_opened else a.get(c, 0) == 0)]
        if any(nl(c) < nl(g) for c in rivals): e1.append('%s%d' % (G.GROUND[Z][0], Z))
        if any(nl(c) == nl(g) and c[0] < g[0] for c in rivals): e2.append('%s%d' % (G.GROUND[Z][0], Z))
    return e1, e2
c1, c2 = excC(False); d1, d2 = excC(True)
print('  C (per step, rival empty at Z-1): clause 1 exceptions (%d): %s' % (len(c1), ' '.join(c1) or 'NONE'))
print('     clause 2 exceptions (%d): %s' % (len(c2), ' '.join(c2) or 'NONE'), '| 6d occupancy at Z = 94..102:', ' '.join(str(occ(Z).get((6, 2), 0)) for Z in range(94, 103)), '(6d opened at %d, empty again from Pu 94)' % opened[(6, 2)])
print("  C' (per step, never-yet-opened rival): clause 1 exceptions (%d): %s" % (len(d1), ' '.join(d1) or 'NONE'))
print('     clause 2 exceptions (%d): %s' % (len(d2), ' '.join(d2) or 'NONE'))
REC = ['La57', 'Ac89', 'Th90']
for tag, e2 in (('A', ['%s%d' % (e[0], e[1]) for e in excA2]), ('B', b2), ('C', c2), ("C'", d2)):
    print('  clause 2 exception set under %s == the record\'s {La, Ac, Th}: %s' % (tag, sorted(e2) == sorted(REC)))
print('  1703 / L9752 *all three are f-openings*: 4f first occupied at Z =', opened[(4, 3)], '(La 57 precedes it by', opened[(4, 3)] - 57, '); 5f first at Z =', opened[(5, 3)], '(Ac 89, Th 90 precede it by', opened[(5, 3)] - 89, 'and', opened[(5, 3)] - 90, ')')
print('  the entrant at La 57 / Ac 89 / Th 90:', ' '.join(name(entrant(Z)) for Z in (57, 89, 90)), '| the 4f / 5f occupancy at Z-1 there:', ' '.join(str(occ(Z - 1).get((4 if Z < 80 else 5, 3), 0)) for Z in (57, 89, 90)))
# 1712 — the twelve unwitnessed rows: what the (n+l, n) fill predicts from the table's last state (a Madelung continuation, NOT the walk)
cont = dict(occ(ZS[-1])); pred = []
for Z in range(ZS[-1] + 1, 121):
    c = min((k for k in CAND if cont.get(k, 0) < 2 * (2 * k[1] + 1)), key=lambda k: (nl(k), k[0]))
    cont[c] = cont.get(c, 0) + 1; pred.append((Z, name(c)))
runs = []
for Z, s in pred:
    if runs and runs[-1][0] == s: runs[-1][2] = Z
    else: runs.append([s, Z, Z])
print('  Madelung continuation Z = %d-120 from the observed Z = %d state (%s): %s' % (ZS[-1] + 1, ZS[-1], ' '.join('%s%d' % (name(k), o) for k, o in sorted(occ(ZS[-1]).items()) if k[0] >= 6), ' · '.join('%s (%d-%d)' % tuple(r) for r in runs)))
print('  1712 / L9778 *6d (109-112), 7p (113-118), 8s (119-120)*:', runs == [['6d', 109, 112], ['7p', 113, 118], ['8s', 119, 120]])

hr('§4 ARITHMETIC OF THE PRINTED FIGURES (Decimal, ROUND_HALF_EVEN at the printed precision)')
print('  1702 rows: Z = 2-120 ->', 120 - 2 + 1, '(printed 119:', 120 - 2 + 1 == 119, ') = SCORED Z = 2-108', 108 - 2 + 1, '+ UNWITNESSED Z = 109-120', 120 - 109 + 1, '->', (108 - 2 + 1) + (120 - 109 + 1) == 119)
print('  L9746-L9747 *Z = 2-108 … hence the 106 transitions Chapter 34 counted*: elements 2-108 =', 107, '; transitions between consecutive elements 3-108 =', 108 - 3 + 1, '(106:', 108 - 3 + 1 == 106, ')')
for n, printed in ((5, '-0.020000'), (6, '-0.013889'), (7, '-0.010204'), (8, '-0.0078125')):
    v = D(Decimal(-1) / (2 * Decimal(n) ** 2), len(printed.split('.')[1]))
    print('  1704 %dg hydrogenic -1/(2n^2) = %s  printed %s  %s' % (n, v, printed, 'MEASURED equal' if str(v) == printed else 'MEASURED differs'))
print('  1704 / L9759-L9760 g channels *5g at 65 elements, 6g at 70, 7g at 57, 8g at 28* and *across a hundred protons*: element counts are walk data (UNREPRODUCIBLE, budget below); 65 + 70 + 57 + 28 =', 65 + 70 + 57 + 28, '; the phrase *a hundred protons* names no figure the walk\'s counts state (INFERRED: the Z range of the 5g/6g rows)')
E11 = 'Mn Zn Ag Cd Nd Pm Sm Lu Hg Lr Rf'.split()
print('  1706 / L9773 eleven elements listed:', len(E11), '| 1706\'s groups 2 (Mn, Zn) + 2 (Ag, Cd) + 4 lanthanides (Nd, Pm, Sm, Lu) + 1 (Hg) + 2 heavy actinides (Lr, Rf) =', 2 + 2 + 4 + 1 + 2)
SYM = {G.GROUND[Z][0]: Z for Z in ZS}
print('  the eleven in the observed table (Z, configuration at Z, entrant):', ' | '.join('%s %d %s ent %s' % (s, SYM[s], G.GROUND[SYM[s]][1], name(entrant(SYM[s]))) for s in E11))
five = [38, 56, 72, 89, 105]
print('  1705 / L9767 five contested Z:', ' '.join('%d=%s(%s, ent %s)' % (Z, G.GROUND[Z][0], G.GROUND[Z][1], name(entrant(Z))) for Z in five), '| values +1.33 +1.24 +2.6 +2.2 +2.16: five, all positive (walk data, UNREPRODUCIBLE)')
lo, hi, so = Decimal('0.058'), Decimal('0.264'), Decimal('0.083')
print('  1712 / 1701 / L9778-L9779 margins 0.058-0.264 Ha against the spin-orbit worst case 0.083 Ha: 0.058 - 0.083 =', lo - so, 'Ha -> *cleared by all* / *clearing every one* / *under every margin* is FALSE under the plain reading (17a-03 re-confirmed by measurement; per-row undecidable, REQUEST-LOWDIN item 10)')
print('  1701 c = 137.035999 (CODATA 2018 inverse fine-structure constant 137.035999084 to 6 dp:', D(Decimal('137.035999084'), 6), ') | chapter prints the same constant at L9737:', '137.035999' in JOIN)
print('  1708 residual ratios 0.999992 and 1.000103: deviations from 1 =', Decimal('1') - Decimal('0.999992'), 'and', Decimal('1.000103') - Decimal('1'), '(walk data, UNREPRODUCIBLE)')
print('  1709 Hessian terms +1.7e-7 and +6.1e-9: their ratio =', D(Decimal('1.7e-7') / Decimal('6.1e-9'), 1), '; *twenty to five hundred times too small* names the residual as the denominator, unprinted (UNREPRODUCIBLE)')
print('  1701 / 1712 *Z <= 112* domain vs *Z = 109-120* rows: 113-120 lie outside the stated domain (INFERRED reading; the domain clause and the row count are both record-carried)')
print('  L9722 / L9834 / L9874 years: challenge 1969, Pulay 1969, Griffin-Andrew-Cowan 1969 and 1971, Löwdin 1950; *nineteen years before* 1969 - 1950 =', 1969 - 1950, '; *three of the load-bearing works are dated 1969*: 3 named')

hr('§5 THE CHAPTER AGAINST THE RECORD — every figure the chapter prints, grepped in 1701-1712 and in the Register beyond')
FIG = ['137.035999', '107 of 107', '107/107', '2–108', '106', '2-108', '109–120', '109-120', '121', '−1/(2n²)', '-1/(2n²)', '65', '70', '57', '28',
       '38, 56, 72, 89, 105', '+1.33', '+1.24', '+2.6', '+2.2', '+2.16', 'Mn, Zn, Ag, Cd, Nd, Pm, Sm, Lu, Hg, Lr, Rf', '0.058', '0.264', '0.083', 'Z = 91',
       '1969', '1950', '1971', 'La, Ac and Th', 'La/Ac/Th', 'nine things', 'twenty-two audits', 'Four of this book', 'fifth', 'nineteen years']
def bounded(f): return re.compile(r'(?<![\d.])' + re.escape(f) + r'(?![\d])')
for f in FIG:
    pat = bounded(f)
    ch = [L0 + k for k, l in enumerate(CH) if pat.search(l)]
    inb = [str(n) for n in sorted(BODY) if pat.search(BODY[n])]
    rest = sum(1 for i, l in enumerate(R, 1) if not (sp <= i < ep) and pat.search(l))
    print('  %-42s chapter L%-14s | in 1701-1712: %-20s | other Register lines: %d' % (repr(f), ','.join(map(str, ch)) or '-', ' '.join(inb) or '-', rest))
print('  Register entries after 1712 whose body names 1701-1712 or the range (the later statements):')
for i, l in enumerate(R, 1):
    if i > ep and re.search(r'\b17(0[1-9]|1[0-2])\b', l) and re.search(r'[Rr]egister|\b1701[–-]1712\b', l):
        print('     L%d entry %s: %s' % (i, encl_reg(i), re.sub(r'\s+', ' ', l)[:170]))
print('  the range *1701–1712* / *1701-1712* by volume:', ' '.join('%s:%d' % (n[:22], sum(1 for l in rd(n) if re.search(r'1701\s*[–-]\s*1712', l))) for n in (MAIN, REG, MC, PC, IOI, SC)))

hr('§6 INSTRUMENTS HELD FOR THE FAMILY — REQUEST-LOWDIN.md items against the LW1-* members (READ-intake1.md); the budget for every UNREPRODUCIBLE figure')
lw = sorted(f for f in os.listdir(H) if f.startswith('LW1-')); print('  LW1-* members:', ' '.join(lw))
req = rd('REQUEST-LOWDIN.md'); items = [(i, l) for i, l in enumerate(req, 1) if re.match(r'^\s*(\d+)\.\s', l)]
print('  REQUEST-LOWDIN.md items:', len(items))
for i, l in items: print('     L%-3d %s' % (i, re.sub(r'\s+', ' ', l)[:160]))
print('  held: object 3 (ground.py = LW1-ground.py, Register 1306) only — the observed table. Not held: the walk (Λ_chain, 1702\'s 119 rows), the scorer, Λ_cinf (1706),')
print('  the collapse diagnostic (1703, Z = 91), the g-channel depths per Z (1704), the second-order correlation (1705), the Pulay / Löwdin-identity / quartic audit (1707-1711),')
print('  the margins and spin-orbit narrowing (1712). Every figure of theirs is UNREPRODUCIBLE here; budget: LOWDIN-HANDOFF-103.tgz (REQUEST-LOWDIN items 1, 2, 4-10), pack104 (item 11).')
print('  UNREPRODUCIBLE with that budget (record-carried, never withdrawn): 107/107 · 65/70/57/28 · +1.33 +1.24 +2.6 [2.57-2.73] +2.2 [1.92-3.32] +2.16 · >= 26x · the eleven · 0.058-0.264 · 0.083 · 2.6e-15 · 0.999992 · 1.000103 · +1.7e-7 · +6.1e-9 · 0.98 · 1.00 · Z = 91 sign · Dirac-Fock to 120')

hr('§7 THE COMPENDIA SECTIONS THAT CARRY THE CHAIN — MC "## LS." and PC "# THE LÖWDIN-SOLUTION INDEXES": bounds resolved by heading text, numerals per line, the chapter figures grepped')
def span_by_heading(V, start_pat, end_pat):
    s0 = [i for i, l in enumerate(V, 1) if re.match(start_pat, l)]; e0 = [i for i, l in enumerate(V, 1) if re.match(end_pat, l)]
    s1 = s0[-1]; e1 = min(i for i in e0 if i > s1); return s1, e1
for tag, name, sp_, ep_ in (('MC', MC, r'^## LS\. ', r'^## 3B\. '), ('PC', PC, r'^# THE L[ÖO]WDIN-SOLUTION INDEXES', r'^# Λ₃ ')):
    V = rd(name); a, b = span_by_heading(V, sp_, ep_); S = V[a - 1:b - 1]
    heads_ = [(a + k, l) for k, l in enumerate(S) if re.match(r'^#{1,4} ', l)]
    print('  %s span L%d-L%d (%d lines; %d headings): %s' % (tag, a, b - 1, b - a, len(heads_), ' | '.join(re.sub(r'^#+\s*', '', h)[:60] for _, h in heads_)))
    nums = [(a + k, NUM.findall(l)) for k, l in enumerate(S) if NUM.findall(l)]
    print('   numerals: %d on %d lines' % (sum(len(v) for _, v in nums), len(nums)))
    for ln, v in nums: print('    L%d: %s' % (ln, ' '.join(v)))
    SJ = ' '.join(S)
    got = [(f, [a + k for k, l in enumerate(S) if bounded(f).search(l)]) for f in FIG]
    print('   chapter figures present:', ' '.join('%s@L%s' % (f, ','.join(map(str, ls))) for f, ls in got if ls))
    print('   chapter figures absent:', ' '.join(repr(f) for f, ls in got if not ls))
    for phrase in ('La, Ac, Th', 'La, Ac and Th', 'La/Ac/Th', '{La, Ac, Th}', 'no exception', 'without exception', 'smaller n', 'n+ℓ', 'n + ℓ'):
        c = SJ.count(phrase)
        if c: print('   phrase %-18r x%d' % (phrase, c))
