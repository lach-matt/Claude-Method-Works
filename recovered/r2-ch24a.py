# r2-ch24a.py — Appendix E part 1 (main L10898–L11053: lead, E.1, E.1.1–E.1.5, E.2), the COMPUTABLE claims (chat 137).
# Reads MEMBERS by name (never a bundle path); imports r2lib by path; deterministic (no wall-clock).
# Appendix E is read as DATA under chat-127 item 1: every Q row resolved to its site and register, every count re-taken with the
# DATA-row set fixed and printed first, E(Q) re-taken under NAMED conventions.
import os, re, itertools, importlib.util
from decimal import Decimal as D, ROUND_HALF_UP
from collections import defaultdict, Counter
H = os.path.dirname(os.path.abspath(__file__))
def load(name):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), os.path.join(H, name + '.py')); mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod); return mod
L = load('r2lib'); heading_line, section_span, has_token = L.heading_line, L.section_span, L.has_token
M = L.read_member('The_Method_1_6-2.md').split('\n')
R = L.read_member('The_Method_1_6___The_Register-2.md').split('\n')

def rbody(n):   # copied verbatim from r2-ch23a.py (there from r2-ch22a.py … r2-ch17b.py; owed to r2lib, DEFERRED): first non-blank line after '### n'
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())

def body_range(M, sec):   # copied verbatim from r2-ch23a.py (there from r2-ch22a.py … r2-ch16z.py; owed to r2lib, DEFERRED): heading to next heading of any rank, body occurrence
    s = heading_line(M, sec)
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1]): return (s, i)
    return (s, len(M) + 1)

def lettered(M, tag):   # copied verbatim from r2-ch23a.py (there from r2-ch22a.py … r2-ch17c.py; owed to r2lib, DEFERRED): lettered heading, exact token, hits in order; body = LAST
    hits = [i for i, l in enumerate(M, 1) if re.match(r'^#{2,4}\s*' + re.escape(tag) + r'(?!\.\d)(?!\d)\b', l)]
    return hits

print('r2-ch24a — Appendix E part 1 (lead, E.1–E.1.5, E.2), computable claims; conventions named inline')
# §1 unit boundaries, measured by scan
s = lettered(M, 'Appendix E')[-1]; t = lettered(M, 'E.3')[-1]; f = lettered(M, 'Appendix F')[-1]
U = M[s - 1:t - 1]; heads = [(i, M[i - 1]) for i in range(s, t) if re.match(r'^#{1,4} ', M[i - 1])]
print('§1 unit `## Appendix E` L%d to `### E.3` L%d − 1 = %d lines (whole appendix to `## Appendix F` L%d: %d lines); headings %d %s'
      % (s, t, len(U), f, f - s, len(heads), [l.split(' ')[1] for i, l in heads]))
print('   blank %d, code-indented %d, `|`-rows %d, non-blank %d' % (sum(1 for l in U if not l.strip()), sum(1 for l in U if l.startswith('    ')),
      sum(1 for l in U if l.lstrip().startswith('|') and not l.startswith('    ')), sum(1 for l in U if l.strip())))
def drange(tag):   # body of `### E.x` by exact token (last hit), first line after heading to the next heading of any rank
    a = lettered(M, tag)[-1]; b = next(i for i in range(a + 1, len(M) + 1) if re.match(r'^#{1,4} ', M[i - 1])); return (a, b)
GAP = re.compile(r' {3,}')
def rows(lo, hi):   # chat-134 convention: a whitespace table's DATA row is a line at the first column carrying a ≥ 3-space column gap
    return [(i, [c.strip() for c in GAP.split(M[i - 1].strip())]) for i in range(lo + 1, hi) if M[i - 1].strip() and GAP.search(M[i - 1].strip())]
def two(lo, hi):   # chat-136 convention: print the rows a ≥ 3-space rule would drop (a 2-space gap, no 3-space gap)
    return [i for i in range(lo + 1, hi) if M[i - 1].strip() and not GAP.search(M[i - 1].strip()) and re.search(r'\S {2}\S', M[i - 1].strip())]

# §2 E.1 coordinate table — DATA-row set fixed and printed first
lo, hi = drange('E.1'); r1 = rows(lo, hi); hdr = [i for i, c in r1 if c[0] == 'coordinate']; d1 = [(i, c) for i, c in r1 if c[0] != 'coordinate']
print('§2 E.1 table L%d–L%d: header %s, DATA rows %d %s; 2-space-only rows %s' % (d1[0][0], d1[-1][0], hdr, len(d1), [c[0] for i, c in d1], two(lo, hi)))
vals = {c[0]: [v.strip() for v in re.split(r' < | · ', c[1])] for i, c in d1}
print('   value counts:', {k: len(v) for k, v in vals.items()}, '; kinds:', {c[0]: c[2] for i, c in d1},
      '; ordered × ordered box (4 coordinates)', 4 * 3 * 3 * 3, '; with depends constant (all *no*)', 4 * 3 * 3)

# §3 E.1.1 lineage table — DATA rows, item column, "three live item counts"
lo, hi = drange('E.1.1'); r2 = rows(lo, hi); d2 = [(i, c) for i, c in r2 if c[0] != 'when']
print('§3 E.1.1 table: DATA rows %d at L%d–L%d; 2-space-only rows %s' % (len(d2), d2[0][0], d2[-1][0], two(lo, hi)))
for i, c in d2: print('   L%d %s | %s | %s' % (i, c[0], c[1], c[2][:60]))
items = [int(c[1]) for i, c in d2]
print('   item column', items, '; recomputations = rows − 1 =', len(d2) - 1, '(E.1.1 L%d prints *five times*; the lead L%d prints *six times*)' % (
      next(i for i in range(lo, hi) if 'recomputed five' in M[i - 1]), next(i for i in range(s, t) if 'recomputed six' in M[i - 1])))
print('   *three live item counts — eight at E.4, fifteen here, thirteen at E.1.2*: 8, 15, 13 all in the item column:', all(x in items for x in (8, 15, 13)),
      '; `### E.4.1` heading token *eight*:', has_token(M[lettered(M, 'E.4.1')[-1] - 1], 'eight'), '; the lead L%d prints *nine items; eight closed … thirteen*: 9 in column:' % (s + 7), 9 in items)

# §4 E.1.2 the Q table — DATA-row set fixed and printed first; every count re-taken
lo, hi = drange('E.1.2'); r3 = rows(lo, hi); d3 = [(i, c) for i, c in r3 if c[0] != 'item']
print('§4 E.1.2 table: rows with ≥3-space gap %d, DATA rows %d at L%d–L%d; 2-space-only rows %s' % (len(r3), len(d3), d3[0][0], d3[-1][0], two(lo, hi)))
Q = {}
for i, c in d3:
    if 'CLOSED' in c[2] or (len(c) > 2 and c[2].startswith('**CLOSED')):
        Q[c[0]] = dict(line=i, q=c[1], closed=True, domain=c[-1])
    else:
        Q[c[0]] = dict(line=i, q=c[1], closed=False, blocks=c[2], obstacle=c[3], cost=c[4], domain=c[5])
    print('   L%d %s | %s | %s' % (i, c[0], 'CLOSED' if Q[c[0]]['closed'] else '%s · %s · %s' % (c[2], c[3], c[4]), Q[c[0]]['domain']))
openQ = [k for k, v in Q.items() if not v['closed']]; closedQ = [k for k, v in Q.items() if v['closed']]
print('   items %d (heading *ten open of 14*: 14 = %s); open %d %s; closed %d %s; letters absent from A–R: %s' % (len(Q), len(Q) == 14, len(openQ), openQ, len(closedQ), closedQ,
      sorted(set('ABCDEFGHIJKLMNOPQR') - set(Q))))
dom = Counter(v['domain'] for v in Q.values()); print('   per-domain counts (14 rows):', dict(dom), '; without R (Register 1729: physical 4, bibliographic 3, mathematical 4, computational 2):',
      dict(Counter(v['domain'] for k, v in Q.items() if k != 'R')))
obs = Counter(v['obstacle'] for v in Q.values() if not v['closed']); print('   obstacle values over the %d open rows: %s (E.1.4 L%d prints *Eleven items: one nonexistent, two buildable, eight retrievable*)' % (
      len(openQ), dict(obs), next(i for i in range(s, t) if 'Eleven items' in M[i - 1])))
blk = Counter(v['blocks'] for v in Q.values() if not v['closed']); print('   blocks values over the open rows:', dict(blk), '; *novelty* rows: 0; *six of the thirteen* fell to nothing — nothing-rows now printed:', blk.get('nothing', 0),
      '(the four closed rows print no blocks value: the six cannot be re-taken from the page)')
# E(Q) under named conventions. Orders as E.1.5 prints them: blocks nothing < novelty < one claim < a result; obstacle retrievable < buildable < nonexistent; cost hours < days < unbounded.
BL = {'nothing': 0, 'novelty': 1, 'one claim': 2, 'a result': 3}; OB = {'retrievable': 0, 'buildable': 1, 'nonexistent': 2}; CO = {'hours': 0, 'days': 1, 'unbounded': 2}
X = {k: (BL[v['blocks']], OB[v['obstacle']], CO[v['cost']]) for k, v in Q.items() if not v['closed']}
def E_R(Xs, box):   # §6.1: E(X) = |ℛ(X)| − |X|; ℛ by D.4.2's φ_ij(v) = max{x_i : x ∈ X, x_j = v}; cells whose x_j is outside X's j-values are not covered by any φ and are excluded
    Xs = sorted(set(Xs)); phi = {}
    for i in range(3):
        for j in range(3):
            if i != j: phi[(i, j)] = {v: max(x[i] for x in Xs if x[j] == v) for v in {x[j] for x in Xs}}
    cl = {x for x in box if all(x[j] in phi[(i, j)] and x[i] <= phi[(i, j)][x[j]] for i in range(3) for j in range(3) if i != j)}
    return len(cl) - len(Xs)
def boxA(Xs): return set(itertools.product(*[sorted({x[i] for x in Xs}) for i in range(3)]))          # A: product of the value sets X occupies
def boxB(Xs): return set(itertools.product(*[range(min(x[i] for x in Xs), max(x[i] for x in Xs) + 1) for i in range(3)]))   # B: interval hull
def boxF(Xs): return set(itertools.product(range(4), range(3), range(3)))                                     # F: the full printed value sets (36)
def E_box(Xs, box): return len(box) - len(set(Xs))   # the naive box defect: unoccupied cells of the box (E.1.4's *18 cells to 24 … E from 4 to 10* arithmetic)
fib = defaultdict(list); [fib[Q[k]['domain']].append(X[k]) for k in X]
print('   fourteen-state (the ten open rows): distinct cells %d of %d; occupied value sets blocks %s obstacle %s cost %s → box A = %d cells (E.1.4 prints 18)' % (
      len(set(X.values())), len(X), sorted({x[0] for x in X.values()}), sorted({x[1] for x in X.values()}), sorted({x[2] for x in X.values()}), len(boxA(X.values()))))
for name, E, bx in (('ℛ·A', E_R, boxA), ('ℛ·B', E_R, boxB), ('ℛ·F', E_R, boxF), ('box·A', E_box, boxA), ('box·B', E_box, boxB)):
    print('   %-6s unfibred E = %d ; fibred by domain E = %d %s' % (name, E(list(X.values()), bx(X.values())), sum(E(v, bx(v)) for v in fib.values()), {k: E(v, bx(v)) for k, v in fib.items()}))
print('   printed: E.1.5 L%d *At fourteen, fibred and unconstrained, E(Q) = 0*; E.1.2 L%d *E(Q) = 0 in all four domain fibres and 1 unfibred* (register 256, the thirteen); E.1.3 L%d *the unfibred figure is 4*; register 465: R as *nothing* took unfibred E 4 → 3' % (
      next(i for i in range(s, t) if 'At fourteen' in M[i - 1]), next(i for i in range(s, t) if 'all four domain fibres' in M[i - 1]), next(i for i in range(s, t) if 'unfibred figure is 4' in M[i - 1])))
Xn = dict(X); Xn['R'] = (BL['nothing'], OB['buildable'], CO['unbounded'])
print('   with R as register 465 entered it (nothing · buildable · unbounded): unfibred ℛ·A E = %d, box·A E = %d; mathematical fibre box·A E = %d, ℛ·A E = %d (E.1.5: *the mathematical fibre admits one cell … which is the cell R now occupies*)' % (
      E_R(list(Xn.values()), boxA(Xn.values())), E_box(list(Xn.values()), boxA(Xn.values())),
      E_box([Xn[k] for k in Xn if Q[k]['domain'] == 'mathematical'], boxA([Xn[k] for k in Xn if Q[k]['domain'] == 'mathematical'])),
      E_R([Xn[k] for k in Xn if Q[k]['domain'] == 'mathematical'], boxA([Xn[k] for k in Xn if Q[k]['domain'] == 'mathematical']))))
# the constraint obstacle = buildable ⟹ cost ≤ days (E.1.5): which printed rows refute it
print('   constraint *buildable ⟹ cost ≤ days*: refuting open rows', [k for k in X if X[k][1] == OB['buildable'] and X[k][2] > CO['days']], '(E.1.5: *Item R refutes it*)')
# E.1.4: adding *no route* as a fourth obstacle value: box A grows 18 → 24 (arithmetic); E under the naive box and under ℛ
Xv = list(X.values()); box24 = set(itertools.product(sorted({x[0] for x in Xv}), [0, 1, 2, 3], sorted({x[2] for x in Xv})))
print('   E.1.4 *grows the ambient box from 18 cells to 24 and takes E from 4 to 10*: |box A| = %d → %d; box-defect E = %d → %d; ℛ-defect E = %d → %d (a value no item occupies is covered by no φ) — on the CURRENT ten rows; E.1.4 narrates eleven items' % (
      len(boxA(Xv)), len(box24), E_box(Xv, boxA(Xv)), E_box(Xv, box24), E_R(Xv, boxA(Xv)), E_R(Xv, box24)))
print('   the thirteen-state (register 256; E.1.5 *the record\'s thirteen reproduce the record: E(Q) = 0 fibred, 1 unfibred*) needs K, M, N, O\'s coordinates: printed in E.1.2?', any(not Q[k]['closed'] for k in 'KMNO'), '— not re-takeable from this unit (E.3 is part 2)')
print('   *depends = no* for every item: the E.1.2 table prints no depends column (E.1 row L%d says the coordinate exists); column headers:' % d1[-1][0], [c for i, c in r3 if c[0] == 'item'][0])

# §5 E.2 closed items — every printed figure re-taken or located at its cited section
lo, hi = drange('E.2'); e2 = ' '.join(l.strip() for l in M[lo:hi - 1])
r = (D('25.96') / D('0.0164')).quantize(D('1'), rounding=ROUND_HALF_UP)
print('§5 E.2: 25.96 / 0.0164 = %s (ROUND_HALF_UP to units; printed *1,585-fold*); exact %s' % (r, (D('25.96') / D('0.0164')).quantize(D('0.01'), rounding=ROUND_HALF_UP)))
def sites(pat, lo_, hi_): return [i for i in range(lo_, hi_) if re.search(pat, M[i - 1])]
for sec, pats in (('23.10', [r'1,585', r'25\.96', r'0\.0164', r'(?<![\d,])518(?![\d,])', r'(?<![\d,])34(?![\d,])', r'(?<![\d,])157(?![\d,])', r'3\.2 ?× ?10', r'(?<![\d,])560(?![\d,])', r'zero failures', r'100 ?%']),
                  ('23.11', [r'interior optimum', r'monoton', r'admissibility cap', r'k\*|\*k\*']), ('26.6', [r'\(p ?− ?1\)|\(\*p\*−1\)', r'Richardson', r'm ?= ?1', r'1/\|']),
                  ('29.8', [r'Gr(ö|o)bner', r'(?<![\d,])eight(?![\d,])', r'E\(claim set\) ?= ?0|reduces? to zero']), ('11.8.1', [r'F\(−1\) ?= ?2|F\(-1\) ?= ?2', r'two values', r'F_box\(−1\)|F_box\(-1\)']),
                  ('16.7', [r'0\.972', r'0\.154', r'7 ?%', r'N\[φ', r'descendants'])):
    b = body_range(M, sec); sp = section_span(M, sec)
    print('   §%s body L%d–L%d span L%d–L%d:' % (sec, b[0], b[1] - 1, sp[0], sp[1] - 1), {p: (len(sites(p, *b)), len(sites(p, sp[0], sp[1]))) for p in pats})
print('   §23.10 *1,585* sites in the volume:', [i for i, l in enumerate(M, 1) if '1,585' in l], '; *25.96*:', [i for i, l in enumerate(M, 1) if '25.96' in l], '; *0.0164*:', [i for i, l in enumerate(M, 1) if '0.0164' in l])
# the accelerator identity A^m(x^p) = (−1)^m x^p / (p−1)^m, m = 1…4, for A = the operator §26.6 defines — located, computed only if the definition is in the section
b = body_range(M, '26.6'); print('   §26.6 body L%d–L%d (%d lines) — printed for r2-ch24b to read the operator; the identity is scored only against the section\'s own definition' % (b[0], b[1] - 1, b[1] - b[0]))

# §6 Register entries the unit cites: heading present, body first line, WARNING lines
cited = [211, 239, 256, 307, 332, 371, 372, 382, 461, 465, 562, 563, 564, 1729]
def hline(n): return next((i + 1 for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
def grouped(n): return [(i + 1, l.strip()) for i, l in enumerate(R) if re.match(r'^#{1,4}\s*\d+\s*[–-]\s*\d+\s*$', l) and int(re.split(r'[–-]', l.split()[1])[0]) <= n <= int(re.split(r'[–-]', l.split()[1])[1])]
def warns(n):
    i = hline(n)
    if i is None: return []
    k = next((k for k in range(i, len(R)) if re.match(r'^#{1,4}\s*\d', R[k])), len(R)); return [m + 1 for m in range(i, k) if 'WARNING' in R[m]]
print('§6 Register entries cited by the unit (heading line, WARNING lines, grouped heading if none):')
for n in cited: print('   %d: heading %s; WARNING %s; grouped %s; numeral sites %s' % (n, hline(n), warns(n), grouped(n) if hline(n) is None else '-', [i + 1 for i, l in enumerate(R) if re.search(r'(?<![\d,])%d(?![\d,])' % n, l)][:8] if hline(n) is None else '-'))
print('   register-citation sites in the unit (lowercase and capitalised, by hand):', [(i, re.findall(r'[Rr]egisters? \d+(?:[–-]\d+)?', M[i - 1])) for i in range(s, t) if re.search(r'[Rr]egisters? \d', M[i - 1])])

# §7 first-run / stage totals the lead prints: nine items, eight closed, four entered by §12.11.7, thirteen — against the lineage column
print('§7 lead L%d–L%d: *nine items; eight closed at E(Q) = 0 with four entered by §12.11.7; thirteen* vs lineage column %s: 9 present %s, 8 %s, 13 %s; *four by the tower* row: %s' % (
      s + 6, s + 8, items, 9 in items, 8 in items, 13 in items, [c[2][:40] for i, c in d2 if c[1] == '15']))
print('   E.1.3 *has held at seven, eight, twelve, thirteen and eleven items*: 7/8/12/13 in column %s; eleven is the post-K/O state (13 − 2) not a lineage row: 11 in column %s' % (all(x in items for x in (7, 8, 12, 13)), 11 in items))
print('   E.1.4 *Eleven items*, E.1.3 *eleven items*, E.1.5 *the thirteen* — states narrated: 11 (K, O closed; M restated; N open; R absent) and 13; current table 14 rows / 10 open')
print('§8 Λ: register 461 *73, 146 and 731 closed subsets of ambients at 8, 9 and 16 cells*; *2⁹⁷⁶ by brute force* (976 = |Λ₈|, tower-2):', L.load_tower().__dict__.get('N8', None) if hasattr(L, 'load_tower') else None)
print('done')
