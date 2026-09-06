# r2-ch23a.py — Appendix D part 2 (main L10462–L10897, D.5–D.6), the COMPUTABLE claims (chat 136).
# Reads MEMBERS by name (never a bundle path); imports r2lib by path; deterministic (no wall-clock).
# Appendix D is read as DATA under chat-127 item 1. The index is REBUILT from the volume's own tables (D.5.2, D.5.4,
# D.5.6–D.5.10) and every printed count, fibre number and E is re-taken under a NAMED convention.
import os, re, io, sys, importlib.util, contextlib, itertools
from decimal import Decimal as D, ROUND_HALF_UP
from collections import Counter, defaultdict
import numpy as np
H = os.path.dirname(os.path.abspath(__file__))
def load(name):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), os.path.join(H, name + '.py')); mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod); return mod
L = load('r2lib'); heading_line, section_span, has_token = L.heading_line, L.section_span, L.has_token
M = L.read_member('The_Method_1_6-2.md').split('\n')
R = L.read_member('The_Method_1_6___The_Register-2.md').split('\n')

def rbody(n):   # copied verbatim from r2-ch22a.py (there from r2-ch21a.py … r2-ch17b.py; owed to r2lib, DEFERRED): first non-blank line after '### n'
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())

def body_range(M, sec):   # copied verbatim from r2-ch22a.py (there from r2-ch21a.py … r2-ch16z.py; owed to r2lib, DEFERRED): heading to next heading of any rank, body occurrence
    s = heading_line(M, sec)
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1]): return (s, i)
    return (s, len(M) + 1)

def lettered(M, tag):   # copied verbatim from r2-ch22a.py (there from r2-ch21a.py … r2-ch17c.py; owed to r2lib, DEFERRED): lettered heading, exact token, hits in order; body = LAST
    hits = [i for i, l in enumerate(M, 1) if re.match(r'^#{2,4}\s*' + re.escape(tag) + r'(?!\.\d)(?!\d)\b', l)]
    return hits

print('r2-ch23a — Appendix D part 2 (D.5–D.6), computable claims; conventions named inline')
# §1 unit boundaries, measured by scan
d5 = [i for i, l in enumerate(M, 1) if re.match(r'^### D\.5 ', l)][-1]; e = lettered(M, 'Appendix E')[-1]
U = M[d5 - 1:e - 1]; heads = [(i, l) for i, l in enumerate(M, 1) if d5 <= i < e and re.match(r'^#{1,4} ', l)]
print('§1 unit `### D.5` L%d to `## Appendix E` L%d − 1 = %d lines; headings %d %s' % (d5, e, len(U), len(heads), [l.split(' ')[1] for i, l in heads]))
def drange(tag):   # body of `### D.x` by exact token, first line after heading to the next heading of any rank
    s = [i for i, l in enumerate(M, 1) if re.match(r'^#{2,4}\s*' + re.escape(tag) + r'(?![\d.])', l)][-1]
    t = next(i for i in range(s + 1, len(M) + 1) if re.match(r'^#{1,4} ', M[i - 1])); return (s, t)
GAP = re.compile(r' {3,}')
def rows(lo, hi):   # chat-134 convention: a whitespace table's DATA row is a line at the first column carrying a ≥ 3-space column gap
    return [(i, [c.strip() for c in GAP.split(M[i - 1].strip())]) for i in range(lo + 1, hi) if M[i - 1].strip() and GAP.search(M[i - 1].strip())]

# §2 the D.5 fibre table (L10467–L10489 by scan): DATA-row set fixed and printed first
r5 = rows(*drange('D.5')); hdr5 = [i for i, c in r5 if c[0] == 'fibre']; data5 = [(i, c) for i, c in r5 if c[0] != 'fibre' and c[0] != 'fibre the element it can only be']
print('§2 D.5 table: rows with a ≥3-space gap', len(r5), '; header rows', hdr5, '; DATA rows', len(data5), 'at L%d–L%d' % (data5[0][0], data5[-1][0]))
print('   first raw row:', repr(M[data5[0][0] - 1]))
tab5 = {}; total5 = 0; fib5 = 0
for i, c in data5:
    fibre, cells = c[0], c[1]
    if 'each' in cells:   # the row `method · order · combinatorics · analysis   1 each   0` = three fibres of one element
        kind, langs = fibre.split(' · ')[0], fibre.split(' · ')[1:]; n = int(cells.split()[0])
        for lg in langs: tab5[(kind, lg)] = n; total5 += n; fib5 += 1
    else: kind, lg = fibre.split(' · '); tab5[(kind, lg)] = int(cells); total5 += int(cells); fib5 += 1
print('   D.5 table: column sum', total5, '(printed seventy-seven at L10491, L10496, L10508, L10863) ; fibres', fib5, '(the 1-each row = 3 fibres; printed twenty-four) ; E column all 0:', all(c[2] == '0' for i, c in data5))
print('   the serving line L10321 prints', re.findall(r'[Ss]eventy-seven elements[^.]*?fibres', M[10320])[:1], '; D.5.1 L10525 sums to twenty-seven (arithmetic):', 1+1+1+2+3+1+5+3+2+1+3+2+2)

# §3 the index rebuilt from the volume's own tables. Coordinates (D.2 L10346–L10348): status withdrawn<conjectured<measured<verified<proved;
# verification cited<sampled<exhaustive; precedent none found<found.
ST = ['withdrawn', 'conjectured', 'measured', 'verified', 'proved']; VE = ['cited', 'sampled', 'exhaustive']; PR = ['none found', 'found']
def coords(s):
    s = s.replace('**', '').strip(); a, b, c = [x.strip() for x in s.split(' · ')][:3]; c = c.split(' (')[0]
    return (ST.index(a), VE.index(b), PR.index(c))
elems = []   # (stage, name, kind, language, (status, verification, precedent), source line)
for i, c in rows(*drange('D.5.2')):
    if c[0] == 'fibre': continue
    k, lg = c[0].split(' · '); elems.append(('D.5.2', c[1], k, lg, coords(c[2]), i))
n27 = len(elems); print('§3 D.5.2 table: DATA rows', n27, '(printed twenty-seven) ; A-labelled', sum(1 for x in elems if re.match(r'A\.\d', x[1])), '; unlabelled', sum(1 for x in elems if not re.match(r'A\.\d', x[1])), '(printed seventeen)')
print('   fibres of the twenty-seven:', len({(x[2], x[3]) for x in elems}), '(printed sixteen, L10526–L10527) ; singleton fibres:', sum(1 for v in Counter((x[2], x[3]) for x in elems).values() if v == 1), '(printed nine, L10540–L10542)')
# D.5.4's five (L10634–L10645; hand-entered from the prose, provenance: all theorem · order; A.5 proved · sampled per L10644 — Register 222 says *now exhaustive*)
five = [('A.4 ⅅ ≥ dim q − dim p', (4, 2, 0)), ('A.5 χ_Λ is total', (4, 1, 0)), ('A.11 ν is inadmissible as an axis', (4, 2, 0)), ('Theorem 18.1 definability', (4, 2, 0)), ('Theorem 18.2 σ-algebra of predicates', (4, 2, 0))]
for nm, co in five: elems.append(('D.5.4', nm, 'theorem', 'order', co, 10644 if nm.startswith('A.5') else 10634))
for sec in ('D.5.6', 'D.5.7', 'D.5.8', 'D.5.9', 'D.5.10'):
    rr = [(i, c) for i, c in rows(*drange(sec)) if c[0] not in ('new element', 'element')]
    rr = [(i, c) for i, c in rr if len(c) >= 3 and ' · ' in c[1] and ' · ' in c[2]]
    for i, c in rr:
        k, lg = c[1].split(' · '); elems.append((sec, c[0], k, lg, coords(c[2]), i))
    print('   %s table: DATA rows %d' % (sec, len(rr)))
stages = ['D.5.2', 'D.5.4', 'D.5.6', 'D.5.7', 'D.5.8', 'D.5.9', 'D.5.10']
cum = {s: [x for x in elems if stages.index(x[0]) <= stages.index(s)] for s in stages}
print('   running totals:', {s: len(cum[s]) for s in stages}, '(printed 27 / 32 / 36 / 40 / 48 / 65 / 77) ; fibres:', {s: len({(x[2], x[3]) for x in cum[s]}) for s in stages}, '(printed 16 / 16 / 16 / 16 / 16 / 22 / 24)')
rebuilt = Counter((x[2], x[3]) for x in elems)
print('   rebuilt per-fibre counts == D.5 table:', rebuilt == Counter(tab5), '; differences:', {k: (rebuilt.get(k), tab5.get(k)) for k in set(rebuilt) | set(tab5) if rebuilt.get(k) != tab5.get(k)})
print('   D.5.9 rows: LS', sum(1 for x in elems if x[0] == 'D.5.9' and x[1].startswith('LS.')), '3B', sum(1 for x in elems if x[0] == 'D.5.9' and x[1].startswith('3B.')), '(printed eight, nine) ; fibres new at D.5.9:', sorted(set((x[2], x[3]) for x in cum['D.5.9']) - set((x[2], x[3]) for x in cum['D.5.8'])), '(printed six)')
print('   fibres new at D.5.10:', sorted(set((x[2], x[3]) for x in cum['D.5.10']) - set((x[2], x[3]) for x in cum['D.5.9'])), '(printed two: measurement · analysis, formula · order)')
print('   status values occupied through D.5.6:', sorted({ST[x[4][0]] for x in cum['D.5.6']}), '; first conjectured:', [x[1] for x in elems if x[4][0] == 1][:3], '(printed: D.5.7 slack = kernel first, D.5.10 observability boundary second) ; any *cited* verification:', any(x[4][1] == 0 for x in elems), '(printed: none)')
print('   theorem count of the thirty-two:', sum(1 for x in cum['D.5.4'] if x[2] == 'theorem'), 'law', sum(1 for x in cum['D.5.4'] if x[2] == 'law'), '(printed 15 / 1, L10667)')

# §4 E under named conventions. E(X) = |ℛ(X)| − |X| (§6.1). ℛ: φ_ij(v) = max{x_i : x ∈ X, x_j = v} (D.4.2); the closure is the set of
# box cells x with x_i ≤ min_j φ_ij(x_j) — the box being (A) the product of the value sets X occupies, or (B) the interval hull
# [min, max] of each coordinate. Conventions C+: cells violating D.3's two constraints (cited ⟹ found; status ≥ measured ⟹ verification
# ≥ sampled) are removed from the box before counting. A cell not covered by any φ (x_j outside X's j-values, convention B) is excluded.
def E_of(X, box):
    X = sorted(set(X)); 
    if not X: return 0
    phi = {}
    for i in range(3):
        for j in range(3):
            if i != j: phi[(i, j)] = {v: max(x[i] for x in X if x[j] == v) for v in {x[j] for x in X}}
    cl = {x for x in box if all(x[j] in phi[(i, j)] and x[i] <= phi[(i, j)][x[j]] for i in range(3) for j in range(3) if i != j)}
    return len(cl) - len(set(X))
def boxes(X, d3):
    A = set(itertools.product(*[sorted({x[i] for x in X}) for i in range(3)]))
    B = set(itertools.product(*[range(min(x[i] for x in X), max(x[i] for x in X) + 1) for i in range(3)]))
    ok = lambda x: (not d3) or ((x[1] != 0 or x[2] == 1) and (x[0] < 2 or x[1] >= 1))
    return {'A': {x for x in A if ok(x)}, 'B': {x for x in B if ok(x)}}
def E_total(els, fib, conv, d3):
    groups = defaultdict(list)
    for x in els: groups[fib(x)].append(x[4])
    return sum(E_of(X, boxes(X, d3)[conv]) for X in groups.values())
FIB = {'kind × language': lambda x: (x[2], x[3]), 'kind only': lambda x: x[2], 'language only': lambda x: x[3], 'none': lambda x: 0}
print('§4 D.5.5 fibration table on the thirty-two (printed E: kind × language 0, kind only 2, language only 3, none 4) — E under each convention:')
for conv in ('A', 'B'):
    for d3 in (False, True):
        print('   convention %s%s:' % (conv, '+D3' if d3 else ''), {f: E_total(cum['D.5.4'], FIB[f], conv, d3) for f in FIB}, '; fibres', {f: len({FIB[f](x) for x in cum['D.5.4']}) for f in FIB})
X32e = [x if not x[1].startswith('A.5') else (x[0], x[1], x[2], x[3], (4, 2, 0), x[5]) for x in cum['D.5.4']]   # A.5 exhaustive, Register 222's state
print('   the same with A.5 proved · exhaustive (Register 222):', {conv: {f: E_total(X32e, FIB[f], conv, False) for f in FIB} for conv in ('A', 'B')})
def fibreE(els, conv='A', d3=False):
    g = defaultdict(list); [g[(x[2], x[3])].append(x[4]) for x in els]; return {k: E_of(v, boxes(v, d3)[conv]) for k, v in g.items()}
def report(tag, els, conv='A', d3=False):
    fe = fibreE(els, conv, d3); print('   %s: elements %d, fibres %d, E = %d' % (tag, len(els), len(fe), sum(fe.values())), {k: v for k, v in fe.items() if v})
def swap(els, name, co): return [(x[0], x[1], x[2], x[3], co, x[5]) if x[1].startswith(name) else x for x in els]
print('   stage closures, convention A (box = occupied value sets), A.5 as printed (sampled):')
for s in stages: report(s, cum[s])
print('   stage closures, convention A, A.5 exhaustive (Register 222):')
for s in stages: report(s, [x if not x[1].startswith('A.5') else (x[0], x[1], x[2], x[3], (4, 2, 0), x[5]) for x in cum[s]])
print('   theorem · order cells of the thirty-two, A.5 sampled:', sorted({x[4] for x in cum["D.5.4"] if (x[2], x[3]) == ("theorem", "order")}), '(printed L10653–L10654: two distinct cells) ; with A.5 exhaustive:', sorted({x[4] for x in X32e if (x[2], x[3]) == ("theorem", "order")}))
# first runs narrated: D.5.6 E = 1 (ℛ-as-closure-operator entered proved · sampled · found); D.5.8 E = 1 (separation hypothesis exhaustive);
# D.5.9 E = 4 then 2 (3B.five and 3B.pot as measured); D.5.10 E = 1 (corridor with precedent found)
base36 = [x if not x[1].startswith('A.5') else (x[0], x[1], x[2], x[3], (4, 2, 0), x[5]) for x in cum['D.5.6']]
report('D.5.6 first run, ℛ closure operator proved · sampled · found, A.5 exhaustive', swap(base36, 'ℛ is a closure operator', (4, 1, 1)))
report('D.5.6 first run, same, A.5 sampled as printed', swap(cum['D.5.6'], 'ℛ is a closure operator', (4, 1, 1)))
base48 = [x if not x[1].startswith('A.5') else (x[0], x[1], x[2], x[3], (4, 2, 0), x[5]) for x in cum['D.5.8']]
report('D.5.8 first run, separation hypothesis proved · exhaustive · none found', swap(base48, 'the separation hypothesis', (4, 2, 0)))
base65 = [x if not x[1].startswith('A.5') else (x[0], x[1], x[2], x[3], (4, 2, 0), x[5]) for x in cum['D.5.9']]
for co, lab in (((2, 2, 1), 'measured · exhaustive · found'), ((2, 1, 1), 'measured · sampled · found'), ((2, 2, 0), 'measured · exhaustive · none found'), ((2, 1, 0), 'measured · sampled · none found')):
    report('D.5.9 first run, 3B.five and 3B.pot as ' + lab, swap(swap(base65, '3B.five', co), '3B.pot', co))
for co, lab in (((3, 1, 0), 'verified · sampled · none found'), ((3, 1, 1), 'verified · sampled · found'), ((2, 1, 0), 'measured · sampled · none found')):
    report('D.5.9 second run, 3B.pot as ' + lab + ', 3B.five proved · exhaustive · found', swap(base65, '3B.pot', co))
base77 = [x if not x[1].startswith('A.5') else (x[0], x[1], x[2], x[3], (4, 2, 0), x[5]) for x in cum['D.5.10']]
report('D.5.10 first run, corridor verified · exhaustive · found', swap(base77, 'the corridor', (3, 2, 1)))
lp = [x[4] for x in elems if (x[2], x[3]) == ('law', 'physics')]
print('   law · physics: elements', len(lp), 'cells', sorted(set(lp)), '(printed four over three) ; box-A cells unoccupied:', sorted(boxes(lp, False)['A'] - set(lp)), '; box-B unoccupied:', len(boxes(lp, False)['B'] - set(lp)), '(printed: admits conjectured · exhaustive and proved · sampled — two named) ; E_A', E_of(lp, boxes(lp, False)['A']), 'E_B', E_of(lp, boxes(lp, False)['B']))
ta = [x[4] for x in elems if (x[2], x[3]) == ('theorem', 'analysis')]; print('   theorem · analysis cells:', sorted(Counter(ta).items()), '; ℛ closure includes verified · exhaustive · none found:', (3, 2, 0) in {x for x in boxes(ta, False)['A']} and E_of(ta, boxes(ta, False)['A']) >= 0)

# §5 Λ₈ figures printed in the unit: 475,800 pairs (D.6), Σ(|Aᵢ| − 1) = 17 (A.19.0), 17 meet- = 17 join-irreducibles (D.5.7), 3,749 covers, 976 words in {0,1}¹⁷
with contextlib.redirect_stdout(io.StringIO()): T8 = L.load_tower()
cells = [tuple(int(v) for v in c) for c in T8.L8()]; n8 = len(cells); A = np.array(cells, dtype=np.int64)
print('§5 |Λ₈| =', n8, '; C(976, 2) =', n8 * (n8 - 1) // 2, '(printed 475,800 pairs, L10887; convention: unordered pairs of distinct cells)')
vals = [sorted(set(A[:, i].tolist())) for i in range(8)]; print('   value sets per coordinate:', [len(v) for v in vals], '; Σ(|Aᵢ| − 1) =', sum(len(v) - 1 for v in vals), '(printed 17, A.19.0 L10709; word length 17 L10710) ; Σ|Aᵢ| =', sum(len(v) for v in vals))
leq = np.all(A[:, None, :] <= A[None, :, :], axis=2); lt = leq & ~np.eye(n8, dtype=bool); cover = lt & ~np.any(lt[:, :, None] & lt[None, :, :], axis=1)   # y ⋖ x: y < x, no z between (copied from r2-ch22a §4)
lower = cover.sum(axis=0); upper = cover.sum(axis=1)
print('   covers', int(cover.sum()), '(printed 3,749) ; join-irreducibles (exactly one lower cover)', int((lower == 1).sum()), '; meet-irreducibles (exactly one upper cover)', int((upper == 1).sum()), '(printed 17 = 17, L10735) ; minimal elements', int((lower == 0).sum()), '; maximal', int((upper == 0).sum()))
words = {tuple(int(A[c, i] > t) for i in range(8) for t in vals[i][:-1]) for c in range(n8)}   # thermometer code: one bit per (coordinate, threshold), 17 bits
print('   thermometer words of length', len(next(iter(words))), 'distinct', len(words), '(printed: Λ as 976 words in {0,1}¹⁷)')

# §6 the Register entries the unit cites: heading present (bare `### N`, then any heading form), WARNING in body
def ent(n):
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None); alt = [k + 1 for k, l in enumerate(R) if re.match(r'^#{1,4}\s*\d+\s*[–-]\s*\d+\s*$', l) and int(l.split()[1].split('–')[0].split('-')[0]) <= n <= int(re.split(r'[–-]', l.split(None, 1)[1])[-1])]
    if i is None: return (None, alt, None)
    j = next((k for k in range(i + 1, len(R)) if re.match(r'^#{1,4}\s*\d+', R[k])), len(R)); body = R[i + 1:j]
    return (i + 1, alt, [l[:120] for l in body if 'WARNING' in l])
cited = [219, 220, 221, 222, 232, 233, 275, 282, 301, 304, 305, 361, 1718, 1726, 1734]
for n in cited: ln, alt, w = ent(n); print('§6 register %d: heading L%s ; grouped-heading hits %s ; WARNING lines %s' % (n, ln, alt, w))
print('   sites of *219*/*220*/*221*/*305* in the Register (any line, digit-bounded):', {n: [i for i, l in enumerate(R, 1) if re.search(r'(?<!\d)%d(?![\d.])' % n, l)][:6] for n in (219, 220, 221, 305)})
print('   `register NNN` / `Register NNN` / `Registers` pointers in the unit:', [(i, re.findall(r'[Rr]egisters? \d+(?:[^.;]*?\d+)?', l)) for i, l in enumerate(M, 1) if d5 <= i < e and re.search(r'[Rr]egisters? \d', l)])
print('   Appendix-D-naming entries with WARNING (r2-ch22a §6 re-taken for 230 / 1419 / 1734 / 1738):', [(n, ent(n)[2]) for n in (230, 1419, 1734, 1738)])
print('done')
