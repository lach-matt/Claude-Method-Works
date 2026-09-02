# r2-ch25a.py — Appendix E part 2 (main `### E.3` to `## Appendix F`: E.3, the unmarked E.4, E.4.1, E.4.2, E.5–E.8), the COMPUTABLE claims (chat 138).
# Reads MEMBERS by name (never a bundle path); imports r2lib by path; deterministic (no wall-clock). Read as DATA under chat-127 item 1:
# every DATA-row set fixed and printed first, every count word re-taken, every ledger totals line checked against its rows, conventions named.
import os, re, itertools, importlib.util, io, contextlib
from decimal import Decimal as D, ROUND_HALF_UP
from collections import Counter, defaultdict
H = os.path.dirname(os.path.abspath(__file__))
def load(name):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), os.path.join(H, name + '.py')); mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod); return mod
L = load('r2lib'); heading_line, section_span, has_token = L.heading_line, L.section_span, L.has_token
M = L.read_member('The_Method_1_6-2.md').split('\n')
R = L.read_member('The_Method_1_6___The_Register-2.md').split('\n')
P = L.read_member('PP_The_Method_1_6.md').split('\n') if os.path.exists(os.path.join(H, 'PP_The_Method_1_6.md')) else open('/home/claude/PP_The_Method_1_6.md', encoding='utf-8').read().split('\n')

def rbody(n):   # copied verbatim from r2-ch24a.py (there from r2-ch23a.py … r2-ch17b.py; owed to r2lib, DEFERRED): first non-blank line after '### n'
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())

def body_range(M, sec):   # copied verbatim from r2-ch24a.py (there from r2-ch23a.py … r2-ch16z.py; owed to r2lib, DEFERRED): heading to next heading of any rank, body occurrence
    s = heading_line(M, sec)
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1]): return (s, i)
    return (s, len(M) + 1)

def lettered(M, tag):   # copied verbatim from r2-ch24a.py (there from r2-ch23a.py … r2-ch17c.py; owed to r2lib, DEFERRED): lettered heading, exact token, hits in order; body = LAST
    hits = [i for i, l in enumerate(M, 1) if re.match(r'^#{2,4}\s*' + re.escape(tag) + r'(?!\.\d)(?!\d)\b', l)]
    return hits

print('r2-ch25a — Appendix E part 2 (E.3–E.8), computable claims; conventions named inline')
# §1 unit boundaries, measured by scan
s = lettered(M, 'E.3')[-1]; f = lettered(M, 'Appendix F')[-1]; U = M[s - 1:f - 1]
heads = [(i, M[i - 1]) for i in range(s, f) if re.match(r'^#{1,4} ', M[i - 1])]
unm = [(i, M[i - 1]) for i in range(s, f) if re.match(r'^E\.\d(\.\d)*\s+[A-Z]', M[i - 1])]
print('§1 unit `### E.3` L%d to `## Appendix F` L%d = %d lines; headings %d %s; unmarked heading-form lines %s' % (s, f, len(U), len(heads), [l.split(' ')[1] for i, l in heads], unm))
print('   blank %d, code-indented %d, `|`-rows %d, non-blank %d' % (sum(1 for l in U if not l.strip()), sum(1 for l in U if l.startswith('    ')),
      sum(1 for l in U if l.lstrip().startswith('|') and not l.startswith('    ')), sum(1 for l in U if l.strip())))
def drange(tag):
    a = lettered(M, tag)[-1]; b = next(i for i in range(a + 1, len(M) + 1) if re.match(r'^#{1,4} ', M[i - 1])); return (a, b)
GAP = re.compile(r' {3,}'); GAP2 = re.compile(r' {2,}')
def rows2(MM, lo, hi, ncol):   # chat-136/137 convention: split on ≥ 2 spaces; print where the ≥ 3-space split changes the column count
    out = []
    for i in range(lo + 1, hi):
        l = MM[i - 1].strip()
        if not l or not GAP2.search(l) or MM[i - 1].startswith('    '): continue
        c3 = [c.strip() for c in GAP.split(l)]; c2 = [c.strip() for c in GAP2.split(l)]
        if len(c3) != len(c2): print('   [2-space row] L%d: ≥3-space gives %d columns, ≥2-space gives %d: %s' % (i, len(c3), len(c2), c2))
        out.append((i, c2))
    return out
def sites(pat, MM=M, lo=1, hi=None): return [i for i in range(lo, hi or len(MM) + 1) if re.search(pat, MM[i - 1])]
def home(i):   # nearest numeric or lettered heading above line i
    for j in range(i, 0, -1):
        m = re.match(r'^#{1,4} (\d+(?:\.\d+)*|[A-G]\.\d+(?:\.\d+)*|Appendix [A-G])', M[j - 1])
        if m: return m.group(1)
    return '?'

# §2 E.3's item list against E.1.2's open rows — E.3 L11055: *the two must list the same items* (Register 384 the record of the prior drift)
lo, hi = drange('E.3'); e4 = next(i for i in range(lo, hi) if re.match(r'^E\.4\s', M[i - 1]))
ITEM = re.compile(r'^ ([A-R]) — ')
e3 = [(i, ITEM.match(M[i - 1]).group(1)) for i in range(lo + 1, e4) if ITEM.match(M[i - 1])]
print('§2 E.3 body L%d–L%d (unmarked *E.4* line at L%d ends it); item entries (`^ X — ` at column 2): %d %s' % (lo + 1, e4 - 1, e4, len(e3), [x for i, x in e3]))
lo2, hi2 = drange('E.1.2'); r12 = rows2(M, lo2, hi2, 6); d12 = [(i, c) for i, c in r12 if c[0] != 'item']
openQ = [c[0] for i, c in d12 if not (c[2].startswith('**CLOSED') or 'CLOSED' in c[2])]; closedQ = [c[0] for i, c in d12 if c[0] not in openQ]
print('   E.1.2 DATA rows %d (L%d–L%d): open %d %s; closed %d %s' % (len(d12), d12[0][0], d12[-1][0], len(openQ), openQ, len(closedQ), closedQ))
print('   E.3 − E.1.2-open: %s ; E.1.2-open − E.3: %s ; E.3 ∩ closed: %s  (E.3 L11055 *the two must list the same items* — the second set is the drift)' % (
      sorted(set(x for i, x in e3) - set(openQ)), sorted(set(openQ) - set(x for i, x in e3)), sorted(set(x for i, x in e3) & set(closedQ))))
# PP: the same two lists in the original (pre-PP state)
def pheads(tag): return [i for i, l in enumerate(P, 1) if re.match(r'^\s*(#{1,4}\s*)?' + re.escape(tag) + r'\s+[A-Z]', l)]   # PP heading-form line: optional marks, optional indent, text follows
pE3 = pheads('E.3'); pE4 = pheads('E.4'); print('   PP heading-form hits: E.3 %s E.4 %s E.1.2 %s E.1.3 %s' % (pE3, pE4, pheads('E.1.2'), pheads('E.1.3')))
pe3 = [(i, ITEM.match(P[i - 1]).group(1)) for i in range(pE3[-1] + 1, pE4[-1]) if ITEM.match(P[i - 1])]
pE12 = pheads('E.1.2'); pE13 = pheads('E.1.3')
pr = rows2(P, pE12[-1], pE13[-1], 5); pd = [(i, c) for i, c in pr if c[0] != 'item']; popen = [c[0] for i, c in pd if not ('CLOSED' in c[2])]
print('   PP: E.3 P%d–P%d items %d %s; E.1.2 P%d DATA rows %d open %d %s → PP E.3 − open %s, open − E.3 %s' % (pE3[-1], pE4[-1], len(pe3), [x for i, x in pe3], pE12[-1], len(pd), len(popen), popen,
      sorted(set(x for i, x in pe3) - set(popen)), sorted(set(popen) - set(x for i, x in pe3))))
# K, M, N, O's coordinates: does the unit print blocks/obstacle/cost for any of them?
for k in 'KMNO':
    hits = [i for i in range(s, f) if re.search(r'\b%s\b' % k, M[i - 1]) and re.search(r'blocks|obstacle|cost', M[i - 1])]
    print('   %s: unit lines naming %s with a coordinate word: %s' % (k, k, hits))
print('   → the eleven-state and thirteen-state coordinates of K, M, N, O are NOT printed in E.3–E.8 (MEASURED: no item entry for K/M/N/O in E.3; no coordinate line); 24a-05 and the thirteen-state re-take stay open (docket 37/38)')

# §3 the E.4 grid (unmarked heading L%d): DATA rows fixed and printed first; *Eight of eleven* / *One stops earlier* / *Two stop later* / *read when the set stood at eleven*
g = rows2(M, e4, hi, 3); gd = [(i, c) for i, c in g if c[0] != 'item']
print('§3 E.4 grid rows (≥2-space split, 3 columns): %d incl. header; DATA rows %d L%d–L%d: %s' % (len(g), len(gd), gd[0][0], gd[-1][0], [c[0] for i, c in gd]))
req = Counter(re.sub(r'\*\*|—.*$', '', c[2]).strip() for i, c in gd); print('   first-unmet-requirement counts:', dict(req))
print('   *Eight of eleven stop at … is it reachable from here*: %d of %d ; *One stops earlier* (does the datum exist): %d ; *Two stop later* (is the work bounded): %d' % (
      req.get('is it reachable from here', 0), len(gd), req.get('does the datum exist', 0), req.get('is the work bounded', 0)))
print('   grid set vs E.1.2: grid − E.1.2-open %s (closed rows in the grid: the eleven-state, K and O closed, R absent — L11108 *read when the set stood at eleven*); E.1.2-open − grid %s' % (
      sorted(set(c[0] for i, c in gd) - set(openQ)), sorted(set(openQ) - set(c[0] for i, c in gd))))
print('   L11130 *Two of the eleven are genuinely unbounded and one is genuinely absent; the other eight are fetching*: 2 / 1 / 8 = %s' % ((req.get('is the work bounded', 0), req.get('does the datum exist', 0), req.get('is it reachable from here', 0)) == (2, 1, 8)))

# §4 item A — Sc VI: [735,860, 737,380] cm⁻¹ · 13.5615–13.5895 nm · 91.338 eV (Decimal, ROUND_HALF_UP; hc = 1.239841984e-4 eV·cm CODATA 2018)
HC = D('1.239841984e-4'); q4 = D('0.0001'); q3 = D('0.001')
lo_, hi_ = D('735860'), D('737380')
print('§4 Sc VI: 10⁷/737,380 = %s nm, 10⁷/735,860 = %s nm (printed 13.5615–13.5895); eV of lower %s, upper %s, midpoint %s = %s cm⁻¹ (printed 91.338)' % (
      (D(10) ** 7 / hi_).quantize(q4, ROUND_HALF_UP), (D(10) ** 7 / lo_).quantize(q4, ROUND_HALF_UP), (lo_ * HC).quantize(q3, ROUND_HALF_UP), (hi_ * HC).quantize(q3, ROUND_HALF_UP),
      ((lo_ + hi_) / 2 * HC).quantize(q3, ROUND_HALF_UP), (lo_ + hi_) / 2))
print('   91.338 / hc = %s cm⁻¹ ; the width 1,520 cm⁻¹ = %s eV' % ((D('91.338') / HC).quantize(D('1'), ROUND_HALF_UP), ((hi_ - lo_) * HC).quantize(q3, ROUND_HALF_UP)))
for pat in (r'735,860', r'737,380', r'91\.338', r'13\.5615', r'735,091', r'735,092', r'736,620'):
    print('   sites of %-8s main %s ; register %s' % (pat, [(i, home(i)) for i in sites(pat)], sites(pat, R)))

# §5 item D — Kreuzer–Skarke: C(208, 2), 26 = 13 + 13, 262 = 131 + 131, the range *13 ≤ h ≤ 128* vs the diagonal end (131,131)
n = 208; print('§5 D: C(208, 2) = %d (printed 21,528); 498 + 498 failures; 13 + 13 = %d (printed 26); 131 + 131 = %d (printed 262); 128 + 128 = %d' % (n * (n - 1) // 2, 26, 262, 256))
print('   *208 cells from 13 ≤ h ≤ 128 less twelve exclusions*: 128 − 13 + 1 = %d values; *112 on the diagonal from (13,13) to (131,131)*: 131 − 13 + 1 = %d diagonal positions — 131 > 128: the diagonal end exceeds the stated range (a slice defined elsewhere: sites below)' % (128 - 13 + 1, 131 - 13 + 1))
for pat in (r'13 ≤ h', r'\b208\b', r'\b131\b', r'\b128\b', r'30,108', r'\b502\b', r'\b540\b', r'21,528', r'\b498\b'):
    print('   sites of %-8s main %s ; register %s' % (pat, [(i, home(i)) for i in sites(pat)][:12], sites(pat, R)[:12]))

# §6 item F — Λ₈: height 17 = Σ(|Aᵢ| − 1), |J(Λ)| = 17, width 7 ≤ 8, chain decomposition = axis system (Dilworth): rebuilt from tower-2.py by path
with contextlib.redirect_stdout(io.StringIO()): T8 = L.load_tower()
cells = [tuple(int(v) for v in c) for c in T8.A] if hasattr(T8, 'A') else [tuple(c) for c in L.L8_at((3, 3, 1, 3, 1))]
cs = set(cells); print('§6 Λ₈: %d cells (tower-2; printed 976)' % len(cells))
vals = [sorted({c[i] for c in cells}) for i in range(8)]; print('   value sets |Aᵢ| = %s ; Σ(|Aᵢ| − 1) = %d (printed 17 = height)' % ([len(v) for v in vals], sum(len(v) - 1 for v in vals)))
def leq(x, y): return all(a <= b for a, b in zip(x, y))
lower = {c: [d for d in cells if d != c and leq(d, c) and not any(e != c and e != d and leq(d, e) and leq(e, c) for e in cells)] for c in cells}
J = [c for c in cells if len(lower[c]) == 1]; bottom = [c for c in cells if len(lower[c]) == 0]
print('   join-irreducibles (exactly one lower cover) |J(Λ₈)| = %d (printed 17); minimal elements %d' % (len(J), len(bottom)))
# width of J(Λ₈) by exhaustive antichain search (17 elements; convention: antichain under componentwise ≤ restricted to J)
best = 0
for r_ in range(1, len(J) + 1):
    found = any(all(not leq(a, b) and not leq(b, a) for a, b in itertools.combinations(S, 2)) for S in itertools.combinations(J, r_))
    if found: best = r_
    else: break
print('   width(J(Λ₈)) = max antichain = %d (printed *width 7 ≤ 8*; 8 = the coordinate count); Dilworth: min chain cover = %d; axes with |Aᵢ| > 1: %d' % (best, best, sum(1 for v in vals if len(v) > 1)))
hmax = max(len(m) for m in [None] or [[]]) if False else None
# height = longest chain in Λ₈ (edges = covers) by longest path over the cover relation
order = sorted(cells, key=lambda c: sum(c)); dist = {}
for c in order: dist[c] = 1 + max([dist[d] for d in lower[c]] or [0])
print('   height of Λ₈ (longest chain, cells − 1) = %d (printed 17)' % (max(dist.values()) - 1))

# §7 item I — *rejects 150 of 216 offered assignments*; item P — 1,442; E.4.1 — |Q| = 7 at §32.2; E.4.2 — *at thirteen*
for pat in (r'\b150\b', r'\b216\b', r'1,442'):
    print('§7 sites of %-6s main %s' % (pat, [(i, home(i)) for i in sites(pat)][:14]))
a, b = body_range(M, '32.2'); a2, b2 = section_span(M, '32.2')
a32, b32 = section_span(M, '32')
print('   §32.2 body L%d–L%d / span L%d–L%d: |Q| = 7 sites %s ; *seven* %s ; Chapter 32 span L%d–L%d *seven* sites %s ; volume-wide `|Q| = 7` sites %s (single witness if only the unit)' % (a, b, a2, b2,
      sites(r'\|Q\| *= *7', M, a, b2), [i for i in range(a, b2) if has_token(M[i - 1], 'seven')], a32, b32, [(i, home(i)) for i in range(a32, b32) if has_token(M[i - 1], 'seven')], [(i, home(i)) for i in sites(r'\|Q\| *= *7')]))
print('   E.4.1 L11135 *the current thirteen is at E.1.2* and E.4.2 L11140 *holds at thirteen* — E.1.2 carries %d DATA rows (heading *of 14*); the thirteen-state is the pre-R state (E.1.5 / Register 1729) — stale count words, 23a-02 / 24a-04 class' % len(d12))
print('   E.4.1 L11133–L11134 *the seven were indexed — blocks, obstacle, cost, depends, fibred by domain*: 4 ordered + 1 fibre = E.1 (5 coordinate rows, READ-ch24a §B)')

# §8 E.5 ledger — DATA rows: left-column starts after a blank line, header excluded (chat-129 convention); totals line *Nine components, nine precedents*
lo5, hi5 = drange('E.5'); led = []
for i in range(lo5 + 1, hi5):
    l = M[i - 1]
    if re.match(r'^  \S', l) and not l.startswith('    ') and (i == lo5 + 1 or not M[i - 2].strip()) and 'what was derived' not in l: led.append((i, GAP2.split(l.strip())[0]))
    elif re.match(r'^  \S', l) and not l.startswith('    ') and M[i - 2].strip() and re.match(r'^  \S', M[i - 2]) and not GAP2.search(l.strip()) and led: led[-1] = (led[-1][0], led[-1][1] + ' ' + l.strip())
print('§8 E.5 ledger DATA rows (left-column starts after a blank line, header excluded): %d' % len(led)); [print('   L%d %s' % (i, t)) for i, t in led]
print('   totals line L%d *Nine components, nine precedents* (E.7 L11210 *Nine components and a day, against nine citations*): rows %d ≠ 9 — 17c-01\'s site (docket 34)' % (sites(r'Nine components, nine precedents', M, lo5, hi5)[0], len(led)))
print('   broken fraction L11165–L11168 (docket 28 site):'); [print('   L%d %r' % (i, M[i - 1].rstrip())) for i in range(11165, 11169)]
a, b = section_span(M, '30.3'); print('   §30.3 span L%d–L%d: 3·2^(d−2) sites %s ; *3/2* %s ; *3/4* %s ; *d = 2* %s ; Rival %s Siggers %s Larson %s' % (a, b,
      sites(r'3\s*·\s*2\^?\(?d\s*−\s*2', M, a, b), sites(r'\b3/2\b', M, a, b), sites(r'\b3/4\b', M, a, b), sites(r'\bd = 2\b', M, a, b),
      len(sites(r'Rival', M, a, b)), len(sites(r'Siggers', M, a, b)), len(sites(r'Larson', M, a, b))))

# §9 E.8 — *Two items closed during this work*; Λ₉ *six independent tests*; *Sixty-odd corrections come from §30.3 alone* (Chapter 28)
a28, b28 = section_span(M, '28'); c28 = sites(r'§30\.3(?!\d)', M, a28, b28)
print('§9 Chapter 28 span L%d–L%d: lines citing §30.3 = %d (item lines among them %d) — *Sixty-odd* is a count of corrections, not lines: witness the lines' % (a28, b28, len(c28), sum(1 for i in c28 if re.match(r'^\s*\d+[\.)]', M[i - 1]))))
print('   *six independent tests* (Λ₉): sites %s ; *target-spin* sites %s' % ([(i, home(i)) for i in sites(r'six independent tests')], [(i, home(i)) for i in sites(r'target-spin')][:10]))
loE2, hiE2 = drange('E.2'); e2 = [(i, M[i - 1].strip()[:40]) for i in range(loE2 + 1, hiE2) if M[i - 1].strip() and (i == loE2 + 1 or not M[i - 2].strip())]   # (fault 3: the first paragraph follows the heading) E.2's rows are question paragraphs: a paragraph start is a non-blank line after a blank (fault 2 self-caught: E.2 is not lettered)
print('   E.2 question paragraphs %d %s ; E.1.1 lineage rows naming closures: %s' % (len(e2), [x for i, x in e2], [(i, M[i - 1].strip()[:70]) for i in sites(r'closed', M, *drange('E.1.1'))]))
print('   E.8 *Two items closed during this work* = E (target-spin axis, §12.11.1) and §30.3\'s characterisation (item F is OPEN in E.1.2: %s) — the two are E and the F-adjacent law, not two Q items; E.2 lists %d' % ('F' in openQ, len(e2)))

# §10 Register entries the unit cites: heading, body first line, WARNING lines
def hline(n): return next((i + 1 for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
def warns(n):
    h = hline(n)
    if h is None: return None
    e = next((i for i in range(h, len(R)) if re.match(r'^#{1,4}\s*\d', R[i])), len(R)); return [(i + 1, R[i].strip()[:100]) for i in range(h, e) if 'WARNING' in R[i]]
cited = sorted({int(x) for i in range(s, f) for x in re.findall(r'[Rr]egisters? (\d+)', M[i - 1])} | {int(x) for i in range(s, f) for x in re.findall(r'(?<=, )(\d{3})(?=\b)', M[i - 1]) if 'Registers' in M[i - 1]})
print('§10 Register entries cited in the unit:', cited)
for n in cited: print('   %d heading L%s ; body: %s ; WARNING: %s' % (n, hline(n), (rbody(n) or '')[:90], warns(n)))
appE = [i for i, l in enumerate(R, 1) if re.search(r'\bE\.[3-8]\b|Appendix E\b', l)]; print('   Register lines naming E.3–E.8 / Appendix E: %d, entries: %s' % (len(appE), sorted({int(m.group(1)) for i in appE for m in [re.match(r'^#{1,4}\s*(\d+)', next(R[j - 1] for j in range(i, 0, -1) if re.match(r'^#{1,4}\s*\d+', R[j - 1])))] if m})))
wl = [(i, R[i - 1].strip()[:110]) for i in appE if 'WARNING' in R[i - 1]]; print('   WARNING lines among them: %s' % wl)

# §11 census rows in range
C = L.read_member('DEFECT-CENSUS.tsv').split('\n'); hdr = C[0].split('\t'); print('§11 DEFECT-CENSUS.tsv header:', hdr)
li = next(i for i, h in enumerate(hdr) if h in ('line', 'ln')); mi = hdr.index('member')
rows_ = [r.split('\t') for r in C[1:] if r.strip()]; inr = [r for r in rows_ if r[mi] == 'main' and r[li].isdigit() and s <= int(r[li]) < f]
print('   rows in main L%d–L%d: %d' % (s, f - 1, len(inr))); [print('   ' + ' | '.join(r)[:200]) for r in inr]
print('END r2-ch25a')
