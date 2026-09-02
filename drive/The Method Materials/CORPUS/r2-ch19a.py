#!/usr/bin/env python3
# r2-ch19a.py — chat 132 — R2 computable batch for main L10054–L10164 (Appendix A part 2: A.15, A.18, A.19, A.19.0, A.19.1;
# from the `### A.15` boundary to `## Appendix B`), BUILD90. Reads MEMBERS only; imports r2lib by path and the tower through
# r2lib.load_tower(). Appendix A is PRE-PP: headings and Statement lines are diffed against the Prints & Proofs original
# (PP_The_Method_1_6.md at /home/claude, fetched at the gate; its `# APPENDICES` body found by scan). Every proved statement is
# re-derived on the rebuilt Λ₈ or on the region it names, or its budget is stated. Conventions named before verdicts; Decimal,
# never round(); a count word counts DATA rows; a literal string is not a test; every negative carries its witness; passes are
# recorded; the instrument is wrong before the book.
import os, re, io, sys, importlib.util, contextlib, itertools
from decimal import Decimal as D, ROUND_HALF_UP
import numpy as np
H = os.path.dirname(os.path.abspath(__file__))
def load(name, quiet=False):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), os.path.join(H, name + '.py')); mod = importlib.util.module_from_spec(spec)
    if quiet:
        with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(mod)
    else: spec.loader.exec_module(mod)
    return mod
L = load('r2lib'); heading_line, section_span, has_token = L.heading_line, L.section_span, L.has_token
with contextlib.redirect_stdout(io.StringIO()): T = L.load_tower()
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
M = rd('The_Method_1_6-2.md'); R = rd('The_Method_1_6___The_Register-2.md')
PPP = '/home/claude/PP_The_Method_1_6.md'
PP = open(PPP, encoding='utf-8').read().split('\n') if os.path.exists(PPP) else None
VOL = {'main': M, 'reg': R, 'mc': rd('The_Method_1_6___Mathematical_Compendium-2.md'), 'pc': rd('The_Method_1_6___The_Physics_Compendium-2.md'),
       'ioi': rd('The_Method_1_6___The_Index_of_Indices-2.md'), 'sc': rd('The_Method_1_6___Spectra_Compendium-2.md')}
def hr(t): print('\n' + '=' * 96 + '\n' + t + '\n' + '=' * 96)
def body_range(M, sec):   # copied verbatim from r2-ch18a.py (there from r2-ch17e.py / r2-ch17c.py / r2-ch17a.py / r2-ch16z.py; owed to r2lib, DEFERRED): heading to next heading of any rank, body occurrence
    s = heading_line(M, sec)
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1]): return (s, i)
    return (s, len(M) + 1)
def rbody(n):   # copied verbatim from r2-ch18a.py (there from r2-ch17e.py / r2-ch17c.py / r2-ch17b.py; owed to r2lib, DEFERRED): first non-blank line after '### n'
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())
def lettered(M, tag):   # copied verbatim from r2-ch18a.py (there from r2-ch17e.py / r2-ch17c.py; owed to r2lib, DEFERRED): lettered heading, exact token, hits in order; body = LAST
    hits = [i for i, l in enumerate(M, 1) if re.match(r'^#{2,4}\s*' + re.escape(tag) + r'(?!\.\d)(?!\d)\b', l)]
    return hits
def q(x, places): return str(D(str(x)).quantize(D(places), rounding=ROUND_HALF_UP))
norm = lambda s: re.sub(r'\s+', ' ', s.strip())
def sites(pat, vols=VOL, flags=0): return {v: [i + 1 for i, l in enumerate(t) if re.search(pat, l, flags)] for v, t in vols.items()}
def text(a, b): return '\n'.join(M[a - 1:b - 1])
ent = lambda ln: next((int(re.match(r'^#{1,4}\s*(\d+)\s*$', R[j - 1]).group(1)) for j in range(ln, 0, -1) if re.match(r'^#{1,4}\s*\d+\s*$', R[j - 1])), None)

hr('§0 BOUNDARY — own heading scan; the unit is Appendix A from `### A.15` (body = last hit) to `## Appendix B` (body = last hit)')
appA = [i for i, l in enumerate(M, 1) if re.match(r'^## Appendix A ', l)]; appB = [i for i, l in enumerate(M, 1) if re.match(r'^## Appendix B ', l)]
An = [(i, l) for i, l in enumerate(M, 1) if i > appA[-1] and i < appB[-1] and re.match(r'^#{2,4}\s*A\.\d', l)]
a15 = [i for i, l in An if l.split()[1] == 'A.15'][0]; unit = (a15, appB[-1])
print('  `## Appendix A`', appA, '; `## Appendix B`', appB, '; A.n headings in the unit:', [(i, l.split()[1]) for i, l in An if i >= a15])
print('  unit: L%d to L%d = %d lines; lettered(M, "A.15") = %s; lettered(M, "A.19") = %s (exact token: A.19 does not match A.19.0/A.19.1)' % (unit[0], unit[1] - 1, unit[1] - unit[0], lettered(M, 'A.15'), lettered(M, 'A.19')))
UL = M[unit[0] - 1:unit[1] - 1]
def uline(pat): return [unit[0] + i for i, l in enumerate(UL) if re.search(pat, l)]

hr('§1 A.15 — B_k IS A SUBLATTICE OF A PRODUCT OF TWO CHAINS; C = {|a − b| ≤ c} IS JOIN-CLOSED AND MEET-BROKEN (conventions: chains [0, m]; closed = componentwise max/min of every pair lands in the set; a failing meet is an UNORDERED pair {x, y} with x ≠ y whose meet is absent — the convention that reproduces §29.12 U4\'s 12,489 for T)')
def pairs_fail(X):
    X = np.array(sorted(X), dtype=np.int64); n = len(X); S = set(map(tuple, X.tolist()))
    mn = np.minimum(X[:, None, :], X[None, :, :]); mx = np.maximum(X[:, None, :], X[None, :, :])
    iu = np.triu_indices(n, 1)
    mfail = sum(1 for t in map(tuple, mn[iu].tolist()) if t not in S); jfail = sum(1 for t in map(tuple, mx[iu].tolist()) if t not in S)
    return n, mfail, jfail, n * (n - 1) // 2
def band(m, k): return [(a, b) for a in range(m + 1) for b in range(m + 1) if abs(a - b) <= k]
res = [(m, k) + pairs_fail(band(m, k))[1:3] for m in range(1, 9) for k in range(0, m + 1)]
print('  B_k on [0, m]², all (m, k) with 1 ≤ m ≤ 8, 0 ≤ k ≤ m:', len(res), 'bands; (meet failures, join failures) all zero:', all(mf == 0 and jf == 0 for _, _, mf, jf in res), '— B_k is a sublattice on every tested pair of chains (exhaustive on all unordered pairs of each band)')
def Cr(c): return [(a, b, cc) for a in range(c + 1) for b in range(c + 1) for cc in range(c + 1) if abs(a - b) <= cc]
for cap in (8, 12, 16):
    n, mf, jf, np_ = pairs_fail(Cr(cap)); print(f'  C at cap {cap} ([0, {cap}]³): |C| = {n:,}; unordered pairs {np_:,}; failing meets {mf:,}; failing joins {jf}')
print('  printed "12,654 at cap 8, 113,568 at cap 12, 565,284 at cap 16" and join-closure: compared above (a match on all three under the unordered-pair convention is the reproduction; 0 joins is the witness of "join-closure holds")')
def Tr(c): return [(a, b, j) for a in range(c + 1) for b in range(c + 1) for j in range(c + 1) if abs(a - b) <= j <= a + b]
n8t, mf8t, jf8t, _ = pairs_fail(Tr(8)); print('  DEF chat-70 carry — T (two-sided) at cap 8: |T| =', n8t, '; failing meets', f'{mf8t:,}', '; joins', jf8t, '— against C\'s figure above: distinct regions (C has no upper bound), distinct counts; neither corrects the other')
# the lower-bound argument alone: for a, b in C the join's third coordinate max(c) bounds |max a − max b| — A.18's lower step with (L, S, J) → (a, b, c)
def lower_only(X):
    S = set(X); return all(abs(max(x[0], y[0]) - max(x[1], y[1])) <= max(x[2], y[2]) for x, y in itertools.combinations(X, 2))
print('  "join-closure holds by A.18\'s lower-bound argument, which does not use the upper bound": |max a − max b| ≤ max c on every pair of C at cap 8:', lower_only(Cr(8)), '(the same inequality A.18 proves as Lower, applied with no upper bound present)')
# B_1 versus C: which is the object at axis 13? read the axis-13 lines
print('  "a bound by a constant is monotone in both directions, a bound by a free coordinate is not": in C the meet fails because min c can drop below |min a − min b|; first failing meet at cap 8:', next(((x, y, tuple(map(min, x, y))) for x, y in itertools.combinations(Cr(8), 2) if tuple(map(min, x, y)) not in set(Cr(8))), None))
print('  "axis 13" sites in main (the tower relies on B₁ there):', sites(r'axis 13')['main'], [norm(M[i - 1])[:120] for i in sites(r'axis 13')['main'] if i < unit[0]])
print('  B₁/B_k/band sites in main outside the unit:', [i for i in sites(r'B₁|B_k|\bband\b')['main'] if i < unit[0] or i >= unit[1]][:12])

hr('§2 A.18 — T = {|2L − 2S| ≤ 2J ≤ 2L + 2S} JOIN-CLOSED, MEET-BROKEN; THE FOUR-CAP CHECK; THE TWO PRINTED WITNESSES; WHICH BOUND EACH FAILING MEET BREAKS (convention as §1; caps 6, 8, 10, 12 on [0, cap]³ as §29.12 U4 states)')
for cap in (6, 8, 10, 12):
    n, mf, jf, np_ = pairs_fail(Tr(cap)); print(f'  T at cap {cap}: |T| = {n:,}; pairs {np_:,}; failing meets {mf:,}; failing joins {jf}')
print('  §29.12 U4 prints 0 joins and 2,862 / 12,489 / 40,887 / 110,229 (L8289–L8290); §12.11.2 L3387 the same four — compared above')
Ts = set(Tr(8)); w1 = ((0, 1, 1), (1, 0, 1)); w2 = ((4, 0, 4), (2, 2, 0))
for a, b in (w1, w2):
    m = tuple(map(min, a, b)); print(f'  witness {a} ∧ {b} = {m}: both in T: {a in Ts and b in Ts}; meet in T: {m in Ts}; upper 2J ≤ 2L+2S holds at the meet: {m[2] <= m[0] + m[1]}; lower |2L−2S| ≤ 2J holds: {abs(m[0] - m[1]) <= m[2]}')
def which(cap):
    X = Tr(cap); S = set(X); up = lo = both = 0
    for x, y in itertools.combinations(X, 2):
        m = tuple(map(min, x, y))
        if m in S: continue
        u = m[2] > m[0] + m[1]; l = abs(m[0] - m[1]) > m[2]
        if u and l: both += 1
        elif u: up += 1
        else: lo += 1
    return up, lo, both
for cap in (6, 8):
    up, lo, both = which(cap); print(f'  cap {cap}: failing meets breaking the UPPER bound only {up:,}; the LOWER only {lo:,}; both {both:,} — "Meets fail on both inequalities" witnessed; "the asymmetry is counted at §29.12 U4 and is not explained by this proof": U4 counts totals only (read: L8288–L8291 print no split by bound; the split above is new)')
a, b = body_range(M, '29.12'); s2 = section_span(M, '29.12'); print('  §29.12 body_range', (a, b - 1), 'section_span', (s2[0], s2[1] - 1), '; U4 lines:', [i for i in range(a, b) if 'U4' in M[i - 1]], norm(M[8287])[:80])
print('  "§8 states as skew" — §8.4 lines with skew:', [(i, norm(M[i - 1])[:100]) for i in range(*section_span(M, '8.4')) if 'skew' in M[i - 1]])
print('  "§12.11.2 as the half-result" — §12.11.2 lines with half/survives:', [(i, norm(M[i - 1])[:110]) for i in range(*section_span(M, '12.11.2')) if re.search(r'half|survives', M[i - 1])], '; the term "half-result" in main:', sites(r'half-result')['main'])
print('  r2-tb1 (upstream operator) is a member:', os.path.exists(os.path.join(H, 'r2-tb1.py')), '— this instrument re-derives T independently and does not import it')

hr('§3 A.19 — THE SEVENTEEN GENERATORS AGAINST Λ₈\'S JOIN-IRREDUCIBLES (convention: join-irreducible = a cell covering exactly one element; rank = coordinate sum; the printed tuples are parsed from the unit\'s code lines; the 17-element poset is the induced order)')
L8 = np.array(T.L8(), dtype=np.int64); n8 = len(L8); cells = [tuple(c) for c in L8.tolist()]; idx = {c: i for i, c in enumerate(cells)}
leq = (L8[:, None, :] <= L8[None, :, :]).all(axis=2); lt = leq & ~np.eye(n8, dtype=bool); cover = lt & ~(lt.astype(np.int64) @ lt.astype(np.int64)).astype(bool)
JI = [i for i in range(n8) if cover[:, i].sum() == 1]; JIset = set(cells[i] for i in JI)
print('  |Λ₈| =', n8, '; join-irreducibles (cover exactly one element):', len(JI), '; bottom (covers none):', [cells[i] for i in range(n8) if cover[:, i].sum() == 0])
a19 = lettered(M, 'A.19')[-1]; a190 = lettered(M, 'A.19.0')[-1]
tup = re.compile(r'\((\d),(\d),(\d),(\d),(\d),(\d),(\d),(\d)\)')
printed = []
for i in range(a19, a190):
    if M[i - 1].startswith('    rank'): 
        rk = int(re.match(r'\s*rank\s+(\d+)', M[i - 1]).group(1)); printed += [(rk, tuple(map(int, t))) for t in tup.findall(M[i - 1])]
    elif M[i - 1].startswith('    ') and tup.search(M[i - 1]): printed += [(rk, tuple(map(int, t))) for t in tup.findall(M[i - 1])]
print('  printed tuples in A.19 (L%d–L%d code lines):' % (a19, a190 - 1), len(printed), '; distinct:', len(set(t for _, t in printed)))
print('  every printed tuple is a cell of Λ₈:', all(t in idx for _, t in printed), '; every printed tuple is join-irreducible:', all(t in JIset for _, t in printed), '; the printed set EQUALS the join-irreducible set:', set(t for _, t in printed) == JIset)
print('  printed rank = coordinate sum on', sum(1 for rk, t in printed if sum(t) == rk), 'of', len(printed), '; rank distribution printed:', sorted(set(rk for rk, _ in printed)), '; counts per rank:', [(rk, sum(1 for r_, _ in printed if r_ == rk)) for rk in sorted(set(rk for rk, _ in printed))])
JIi = sorted(JI, key=lambda i: (int(L8[i].sum()), cells[i]))
subcov = [(cells[x], cells[y]) for x in JIi for y in JIi if lt[x, y] and not any(lt[x, z] and lt[z, y] for z in JIi)]
print('  covering relations of the 17-element poset (induced order, covers within the subposet):', len(subcov), '— §8.3 L1849 "17 join-irreducibles, 20 covering relations"; A.19.0 "the twenty implications"')
# down-sets of the 17-element poset by direct enumeration of all 2^17 subsets
JIl = [cells[i] for i in JIi]; below = [sum(1 << k for k in range(17) if k != j and leq[idx[JIl[k]], idx[JIl[j]]]) for j in range(17)]
down = [s for s in range(1 << 17) if all(not (s >> j & 1) or (s & below[j]) == below[j] for j in range(17))]
print('  down-sets of the 17-element poset by direct enumeration of all', 1 << 17, 'subsets:', len(down), '= 976:', len(down) == 976)
# Λ recoverable from the table and nothing else: the join of each down-set (componentwise max, bottom = (1,0,1,0,1,0,0,0) for the empty set) gives Λ₈ exactly
bot = min(cells, key=lambda c: sum(c)); rec = set()
for s in down:
    v = list(bot)
    for j in range(17):
        if s >> j & 1: v = [max(a, b) for a, b in zip(v, JIl[j])]
    rec.add(tuple(v))
print('  "Λ is recoverable from this table and nothing else": joins of the 976 down-sets (bottom = the least cell) =', len(rec), 'distinct cells; equals Λ₈:', rec == set(cells), '(the bottom is the one datum the table does not print; it is the empty down-set\'s join, A.19.1 prints it)')
print('  §8.3\'s three claims, sites:', [(i, norm(M[i - 1])[:100]) for i in range(*section_span(M, '8.3')) if re.search(r'17 join-irreducibles|20 covering|976 down-sets|exact', M[i - 1])], '; "It never prints the seventeen": 8-tuples in §8.3 span:', len([i for i in range(*section_span(M, '8.3')) if tup.search(M[i - 1])]), '; in the whole main before Appendix A:', [i for i, l in enumerate(M, 1) if i < 9937 and len(tup.findall(l)) >= 3][:8])
print('  S1 sites in main:', sites(r'\bS1\b')['main'], [norm(M[i - 1])[:90] for i in sites(r'\bS1\b')['main'][:2]])

hr('§4 A.19.0 — EVERY GENERATOR IS min{x : x_c ≥ v}; THE CLOSED SIZE Σ(|Aᵢ| − 1); THE TABLE\'S RANK, WEIGHT AND FORCES COLUMNS; THE TWENTY IMPLICATIONS SPLIT 9 + 11 (conventions: |Aᵢ| = size of the coordinate support; weight = cells with x_c ≥ v; forces = the elements the generator covers in the 17-poset; percentages Decimal HALF_UP 1 place)')
names = ['n', 'ℓ', 'k', 'q', 'e', 'f', 'g', '2S']; supp = [sorted(set(L8[:, c].tolist())) for c in range(8)]
print('  coordinate supports:', dict(zip(names, supp)), '; |Aᵢ| − 1:', [len(s) - 1 for s in supp], '; Σ =', sum(len(s) - 1 for s in supp), '(printed 2 + 1 + 2 + 3 + 2 + 1 + 3 + 3 = 17)')
gens = {}
for c in range(8):
    for v in supp[c][1:]:
        cand = [i for i in range(n8) if L8[i, c] >= v]; mins = [i for i in cand if all(leq[i, j] for j in cand)]
        gens[(names[c], v)] = (cells[mins[0]] if len(mins) == 1 else None, len(mins))
print('  (c, v) pairs:', len(gens), '; each has a UNIQUE least cell:', all(k == 1 for _, k in gens.values()), '; every such least cell is join-irreducible:', all(g in JIset for g, _ in gens.values()), '; the set of least cells EQUALS the join-irreducible set:', set(g for g, _ in gens.values()) == JIset)
# parse the table
a191 = lettered(M, 'A.19.1')[-1]; rows = []
for i in range(a190, a191):
    m = re.match(r'^\s{2}(n|ℓ|k|q|e|f|g|2S) ≥ (\d)\s+\((\d(?:,\d){7})\)\s+(\d+)\s+(\d+)\s+(.*)$', M[i - 1])
    if m: rows.append((i, m.group(1), int(m.group(2)), tuple(map(int, m.group(3).split(','))), int(m.group(4)), int(m.group(5)), [x.strip() for x in m.group(6).split(',')] if m.group(6).strip() != '—' else []))
print('  table DATA rows parsed (header L%d):' % [i for i in range(a190, a191) if re.match(r'^\s+letter\s+generator', M[i - 1])][0], len(rows))
okg = okr = okw = 0; forces_ok = []; wts = []
for i, c, v, g, rk, wt, fr in rows:
    ci = names.index(c); gi = gens[(c, v)][0]; okg += (gi == g); okr += (sum(g) == rk); w = int((L8[:, ci] >= v).sum()); wts.append(w); okw += (w == wt)
    lower = sorted(cells[x] for x in JIi if (cells[x], g) in subcov); fr_t = sorted(gens[tuple(re.match(r'(\S+) ≥ (\d)', f).groups())[0:1] + (int(re.match(r'(\S+) ≥ (\d)', f).group(2)),)][0] for f in fr) if fr else []
    forces_ok.append(lower == fr_t)
    if not (gi == g and sum(g) == rk and w == wt and lower == fr_t): print('    MISMATCH L%d %s ≥ %d: generator %s vs %s; rank %d vs %d; weight %d vs %d; forces %s vs covers %s' % (i, c, v, g, gi, rk, sum(g), wt, w, fr, lower))
print('  generator column = least cell on', okg, 'of', len(rows), '; rank column = coordinate sum on', okr, '; weight column = cells with x_c ≥ v on', okw, '; forces column = the generator\'s lower covers in the 17-poset on', sum(forces_ok), 'of', len(rows))
print('  weights min/max:', min(wts), max(wts), '; 856/976 =', q(D(856) / D(976) * 100, '0.1') + '%', '; 16/976 =', q(D(16) / D(976) * 100, '0.1') + '%', '(printed 87.7% and 1.6%)')
nforces = sum(len(fr) for *_, fr in rows); within = sum(1 for _, c, v, g, rk, wt, fr in rows for f in fr if f.split()[0] == c); between = nforces - within
print('  forces entries (DATA cells, comma-split):', nforces, '; within a coordinate:', within, '; between coordinates:', between, '(printed twenty = nine + eleven); equals the 17-poset\'s covering relations:', nforces == len(subcov))
wc = sum(1 for x, y in subcov if [i for i in range(8) if x[i] != y[i]] and all(x[i] == y[i] or (i == [j for j in range(8) if x[j] != y[j]][0]) for i in range(8)))
# the eleven between-coordinate implications against the seven binary constraints as tower-2 codes them
cons = {'ℓ ≤ n−1': lambda x: x[1] <= x[0] - 1, 'k ≤ 4ℓ+2': lambda x: x[2] <= 4 * x[1] + 2, 'q ≤ k': lambda x: x[3] <= x[2], 'f ≤ e−1': lambda x: x[5] <= x[4] - 1, 'g ≤ 4f+2': lambda x: x[6] <= 4 * x[5] + 2, 'g ≤ q': lambda x: x[6] <= x[3], '2S ≤ k': lambda x: x[7] <= x[2]}
lab = {g: (c, v) for (c, v), (g, _) in gens.items()}
btw = [(lab[y], lab[x]) for x, y in subcov if lab[x][0] != lab[y][0]]   # y (higher) forces x (lower): (c ≥ v) ⇒ (d ≥ w)
attrib = []
for (c, v), (d, w) in btw:
    ci, di = names.index(c), names.index(d)
    # the implication c ≥ v ⇒ d ≥ w is entailed by constraint K alone iff every ambient point with x_c ≥ v and x_d < w violates K (K binds at the value)
    amb = [x for x in itertools.product(*supp) if x[ci] >= v and x[di] < w]
    ks = [k for k, f in cons.items() if all(not f(x) for x in amb)]
    attrib.append(((c, v, d, w), ks))
print('  the eleven between-coordinate implications, each with the single constraint that entails it on the ambient box (x_c ≥ v ∧ x_d < w violates it):')
for (c, v, d, w), ks in attrib: print('    %s ≥ %d forces %s ≥ %d  ←  %s' % (c, v, d, w, ks))
per = {k: sum(1 for _, ks in attrib if ks == [k]) for k in cons}
print('  every implication entailed by exactly one constraint:', all(len(ks) == 1 for _, ks in attrib), '; implications per constraint:', per, '; every one of the seven constraints binds at ≥ 1 value:', all(v > 0 for v in per.values()), '; Σ =', sum(per.values()), '— "eleven … one for each way χ\'s seven constraints bind at a value" READ: the count of (constraint, value) pairs at which the bound becomes tight, not one per constraint')
print('  the printed eleven, in the printed order, against the measured set (as unordered set of implications):', set((c, v, d, w) for (c, v, d, w), _ in attrib) == {('f', 1, 'e', 2), ('ℓ', 1, 'n', 2), ('g', 1, 'q', 1), ('2S', 2, 'k', 2), ('q', 2, 'k', 2), ('k', 3, 'ℓ', 1), ('g', 2, 'q', 2), ('2S', 3, 'k', 3), ('q', 3, 'k', 3), ('g', 3, 'f', 1), ('g', 3, 'q', 3)})
print('  §7.1 constraints as printed (span L%d–L%d):' % (section_span(M, '7.1')[0], section_span(M, '7.1')[1] - 1), [norm(M[i - 1])[:90] for i in range(*section_span(M, '7.1')) if re.search(r'≤', M[i - 1])][:9])

hr('§5 A.19.1 — THE EIGHT CELLS SURVIVING x ↦ max − x; THE TOP AND BOTTOM CELLS (convention: max = the coordinatewise maximum over Λ₈; a cell survives iff max − x ∈ Λ₈; rank = coordinate sum)')
mx = L8.max(axis=0); surv = [c for c in cells if tuple(int(a) for a in (mx - np.array(c))) in idx]
print('  max =', tuple(mx.tolist()), '; survivors:', len(surv), sorted(surv, key=lambda c: (sum(c), c)))
pr = []
for i in range(a191, unit[1]):
    if M[i - 1].startswith('    ') and tup.search(M[i - 1]): pr += [tuple(map(int, t)) for t in tup.findall(M[i - 1])]
print('  printed cells:', len(pr), '; printed set = survivor set:', set(pr) == set(surv))
print('  "Every one has q = k, g = q and 2S = q":', all(c[3] == c[2] and c[6] == c[3] and c[7] == c[3] for c in surv), '; "(n, ℓ) and (e, f) each at (1,0) or (2,1)":', all((c[0], c[1]) in {(1, 0), (2, 1)} and (c[4], c[5]) in {(1, 0), (2, 1)} for c in surv), '; "fixed setwise because source and target halves mirror": max − x for each survivor is itself a survivor:', all(tuple(int(a) for a in (mx - np.array(c))) in set(surv) for c in surv), '; 2 × 2 × 2 (q ∈ {1,2}) = 8 accounts for the count:', sorted(set(c[3] for c in surv)))
top = [c for c in cells if all(leq[idx[x], idx[c]] for x in cells)]; botm = [c for c in cells if all(leq[idx[c], idx[x]] for x in cells)]
print('  top (unique greatest):', top, 'rank', [sum(c) for c in top], '; bottom (unique least):', botm, 'rank', [sum(c) for c in botm], '(printed (3,1,3,3,3,1,3,3) rank 20; (1,0,1,0,1,0,0,0) rank 3)')
print('  §8.3/§8.4 site of the eight (L1887):', norm(M[1886])[:140], '; other main sites of "max − x":', sites(r'max − x')['main'])

hr('§6 PRE-PP DIFF — headings and Statement lines of the unit against the Prints & Proofs original (section number stripped from BOTH sides; whitespace-normalised); body-level line diff of the unit')
if PP is None: print('  PP not on disk — BUDGET: fetched at the gate to /home/claude/PP_The_Method_1_6.md; re-run there')
else:
    pa = [i for i, l in enumerate(PP, 1) if re.match(r'^# APPENDICES\s*$', l)]; ppB = [i for i, l in enumerate(PP, 1) if re.match(r'^#+ Appendix B ', l)]
    ppA = [(i, l.strip()) for i, l in enumerate(PP, 1) if pa[-1] < i < ppB[-1] and re.match(r'^ ?A\.\d+(\.\d+)? \S', l) and not re.match(r'^ ?A\.\d+\s{2,}', l) and not re.match(r'^ ?A\.\d+ (prints|states)', l)]
    print('  PP `# APPENDICES`', pa, '; PP `Appendix B`', ppB, '; PP A.n heading lines from A.15:', [(i, l.split()[0]) for i, l in ppA if [int(t) for t in l.split()[0][2:].split('.')] >= [15]])
    volH = {l.split()[1]: (i, norm(re.sub(r'^#+\s*A\.\d+(\.\d+)?\s*', '', l))) for i, l in An if i >= a15}; ppH = {l.split()[0]: (i, norm(re.sub(r'^A\.\d+(\.\d+)?\s*', '', l))) for i, l in ppA}
    for k in sorted(volH, key=lambda s: [int(t) for t in s[2:].split('.')]):
        v = volH[k]; p = ppH.get(k); print(f'  {k}: volume L{v[0]} "{v[1]}" | PP', 'ABSENT' if p is None else f'P{p[0]} "{p[1]}"', '| equal:', p is not None and v[1] == p[1])
    def stmt(lines, start, stop): return [(i, norm(lines[i - 1])) for i in range(start, stop) if re.match(r'^\s*Statement\.', lines[i - 1])]
    vs = stmt(M, unit[0], unit[1]); ps = stmt(PP, ppH['A.15'][0], ppB[-1]); print('  Statement lines: volume', len(vs), '; PP (from A.15)', len(ps))
    for (vi, vt), (pi, pt) in zip(vs, ps): print(f'   L{vi} vs P{pi}: first-line equal:', vt == pt, '' if vt == pt else f'\n      V: {vt[:150]}\n      P: {pt[:150]}')
    def paras(lines, a, b): return [norm(re.sub(r'[*_`]', '', lines[i - 1])) for i in range(a, b) if lines[i - 1].strip()]
    pv = paras(M, unit[0], unit[1]); pp_ = paras(PP, ppH['A.15'][0], ppB[-1]); onlyV = [x for x in pv if x not in pp_]; onlyP = [x for x in pp_ if x not in pv]
    print('  non-blank lines: volume', len(pv), '; PP', len(pp_), '; in volume not PP:', len(onlyV), '; in PP not volume:', len(onlyP))
    for x in onlyV[:20]: print('    V+ ', x[:170])
    for x in onlyP[:20]: print('    P+ ', x[:170])

hr('§7 POINTERS AND REGISTER — every cited section under both resolvers; every cited entry\'s body and WARNING line (body = first non-blank line after `### N`)')
for sec in ('14.4', '29.12', '8.3', '7.1', '12.11.2'):
    a, b = body_range(M, sec); s = section_span(M, sec); print(f'  §{sec}: body_range L{a}–L{b-1} ({b-a} lines) | section_span L{s[0]}–L{s[1]-1} ({s[1]-s[0]} lines) | heading: {norm(M[a-1])[:70]}')
a, b = body_range(M, '14.4'); print('  §14.4 body in full:', [norm(M[i - 1]) for i in range(a, b) if M[i - 1].strip()], '— "monotone single-coordinate bounds … which §14.4 admits in both directions": hits for monotone|admiss|bound in §14.4:', len([i for i in range(a, b) if re.search(r'monoton|admiss|bound', M[i - 1], re.I)]))
print('  where admissibility lives — main lines with "admissib" before Appendix A (line, section):', [(i, L.enclosing(M, i)) for i, l in enumerate(M, 1) if re.search(r'admissib', l, re.I) and i < 9937][:12])
print('  main lines with "monotone" naming single-coordinate/one-coordinate bounds:', [(i, L.enclosing(M, i)) for i, l in enumerate(M, 1) if re.search(r'monotone', l) and re.search(r'single[- ]coordinate|one[- ]coordinate|both directions|either direction', l) and i < 9937][:8])
print('  MC L1254 cites "the admissibility condition (§14.4)":', 'admissibility condition (§14.4)' in VOL['mc'][1253], '— the same pointer in the Mathematical Compendium')
for n in (230, 268, 208, 255):
    b = rbody(n); print(f'  Register {n}: {(b or "ABSENT")[:200]}'); print('     WARNING in body:', 'WARNING' in (b or ''))
i230 = next(i for i, l in enumerate(R, 1) if l.strip() == '### 230'); blk = [l for l in R[i230:i230 + 12] if l.strip()][:3]
print('  Register 230 next lines:', [x[:120] for x in blk], '— A.15\'s Remark cites 230 for "the ledger, which called C a join-closed sublattice"; 230\'s subject is Appendix D\'s kind coordinate (docket 9(b) candidate: target says nothing of the claim)')
sub = [i + 1 for i, l in enumerate(R) if 'sublattice' in l]; print('  Register lines with "sublattice":', sub, 'entries', sorted(set(e for e in map(ent, sub) if e)))
for e in sorted(set(e for e in map(ent, sub) if e)):
    b = rbody(e); print(f'     {e}: {b[:160]}' + ('  WARNING' if 'WARNING' in b else ''))
print('  Register lines with "join-closed":', [(i + 1, ent(i + 1)) for i, l in enumerate(R) if 'join-closed' in l][:12])
print('  "the ledger" — where C is called a join-closed sublattice: main sites', sites(r'join-closed sublattice')['main'], '; every volume:', {k: v for k, v in sites(r'join-closed sublattice').items() if v}, '; "the ledger" in the unit:', uline(r'ledger'))
print('  Register 268 names A.19.0\'s content (closed size 17) — its entry number in the unit L%s; Register 255 names A.19 ("seventeen generators are now listed at A.19"); Register 208 names the 8 and max − x' % uline(r'Register 268'))
print('  Register lines naming A.15/A.18/A.19:', [(i + 1, ent(i + 1), R[i][:100]) for i, l in enumerate(R) if re.search(r'\bA\.(15|18|19)\b', l)][:10])
print('  unit lines with register/Register:', uline(r'[Rr]egister'), '(G0i: lowercase "register 208" names; "Register 230/268/255" cite)')
