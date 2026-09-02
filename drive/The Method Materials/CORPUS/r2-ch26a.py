# r2-ch26a.py — Appendix F (main `## Appendix F` to `## Appendix G`: F.1–F.4.3), the COMPUTABLE claims (chat 139).
# Reads MEMBERS by name (never a bundle path); imports r2lib by path; deterministic (no wall-clock). Read as DATA under chat-127 item 1:
# every DATA-row set fixed and printed first, every count word re-taken, every printed figure located, conventions named.
import os, re, csv, itertools, importlib.util
from decimal import Decimal as D, ROUND_HALF_UP
from collections import Counter, defaultdict
H = os.path.dirname(os.path.abspath(__file__))
def load(name):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), os.path.join(H, name + '.py')); mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod); return mod
L = load('r2lib'); heading_line, section_span, has_token = L.heading_line, L.section_span, L.has_token
M = L.read_member('The_Method_1_6-2.md').split('\n')
R = L.read_member('The_Method_1_6___The_Register-2.md').split('\n')
def hr(t): print('\n== ' + t)
def rbody(n):   # copied verbatim from r2-ch25a.py (there from r2-ch24a.py … r2-ch17b.py; owed to r2lib, DEFERRED): first non-blank line after '### n'
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())
def rspan(n):   # entry span: '### n' heading to the next '### k' heading (this instrument's own; bodies read, WARNING lines counted)
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    if i is None: return None
    j = i + 1
    while j < len(R) and not re.match(r'^#{1,4}\s*\d+\s*$', R[j]): j += 1
    return (i + 1, j)   # 1-based heading line, exclusive end (0-based index of next heading)

hr('§0 the unit, measured by scan (never carried): `## Appendix F` (LAST hit) to `## Appendix G` (LAST hit)')
F = [i + 1 for i, l in enumerate(M) if re.match(r'^## Appendix F\b', l)][-1]
G = [i + 1 for i, l in enumerate(M) if re.match(r'^## Appendix G\b', l)][-1]
U = M[F - 1:G - 1]
heads = [(F + k, l) for k, l in enumerate(U) if re.match(r'^#{1,4}\s', l)]
print('  F L%d, G L%d, unit %d lines; headings %d:' % (F, G, len(U), len(heads)))
for ln, l in heads: print('   L%d %s' % (ln, l))
code = [F + k for k, l in enumerate(U) if l.startswith('    ')]
pipe = [F + k for k, l in enumerate(U) if l.startswith('|') and not l.startswith('    ')]
print('  blank %d; 4-space code lines %d (%s); `|` rows outside code %d' % (sum(1 for l in U if not l.strip()), len(code), code, len(pipe)))
unmarked = [F + k for k, l in enumerate(U) if re.match(r'^\s*F\.\d+(\.\d+)*\s+[A-Z]', l)]
print('  unmarked heading-form lines (no #): %s' % (unmarked or 'none'))

hr('§1 the two `|` tables — DATA-row set fixed and printed before any count word (header + `|---|` separator excluded)')
tables = []; cur = []
for ln in pipe:
    if cur and ln != cur[-1] + 1: tables.append(cur); cur = []
    cur.append(ln)
if cur: tables.append(cur)
for t in tables:
    rows = [ln for ln in t if not re.match(r'^\|\s*-', M[ln - 1])]
    hdr, data = rows[0], rows[1:]
    print('  table L%d–L%d: header L%d %s; DATA rows %d:' % (t[0], t[-1], hdr, M[hdr - 1], len(data)))
    for ln in data: print('    L%d %s' % (ln, M[ln - 1][:110]))
    tables_data = data
kinds = [re.match(r'^\|\s*\*\*(\w+)\*\*', M[ln - 1]).group(1) for ln in [ln for ln in tables[0] if re.match(r'^\|\s*\*\*', M[ln - 1])]]
cols = [re.match(r'^\|\s*\*\*([^*]+)\*\*', M[ln - 1]).group(1) for ln in [ln for ln in tables[1] if re.match(r'^\|\s*\*\*', M[ln - 1])]]
print('  kinds table DATA rows = %d %s; F.1 L%d "Six kinds recur": %s' % (len(kinds), kinds, F + 16, len(kinds) == 6))
print('  columns table DATA rows = %d %s; F.3 L%d "the standard has four columns": %s' % (len(cols), cols, F + 58, len(cols) == 4))
seventh = [F + k for k, l in enumerate(U) if 'seventh' in l]
print('  "seventh candidate" sites in unit: %s — 6 kinds + 1 refused = 7: %s' % (seventh, len(kinds) + 1 == 7))
clauses = [F + k for k, l in enumerate(U) if re.match(r'^\s{2}\((i{1,3})\)\s+\*\*', l)]   # the indented bold clause lines; L11274's prose '(i) is a survey' excluded (fault 2)
print('  F.2 clauses (i)–(iii) at %s = %d; "(i)–(iii)" cited at L%d: %s' % (clauses, len(clauses), F + 51, len(clauses) == 3))
print('  Register 1780 states "Six quantity-kinds … closed by construction": %s' % ('Six quantity-kinds' in (rbody(1780) or '')))

hr('§2 F.2 clause (iii) on the periodic ground — "the values admitted at a proton number and charge are a function of the electron count alone, on every pair the coordinate file carries and with no exception (register 1779)"')
cand = [os.path.join(H, 'COORDINATES-2_13.csv'), '/mnt/project/COORDINATES-2_13.csv']
f = next((c for c in cand if os.path.exists(c)), None)
sp = rspan(1779)
print('  Register 1779 heading: %s; body sentences carrying "electron":' % (sp is not None))
if sp:
    for k in range(sp[0], sp[1]):
        for s in re.split(r'(?<=[.!?])\s+', R[k]):
            if re.search(r'electron count|function of the|indistinguishable|multiplicit', s): print('    R%d: %s' % (k + 1, s[:420]))
    print('  1779 tokens: "electron count" %d, "function of" %d, "multiplicit" %d, "(iii)" %d, "7,260" %d' % tuple(sum(len(re.findall(t, R[k])) for k in range(sp[0], sp[1])) for t in ('electron count', 'function of', 'multiplicit', r'\(iii\)', '7,260')))
if f is None:
    print('  COORDINATES-2_13.csv: not a member and not in the project folder — BUDGET: the (iii) claim is untested here')
else:
    rows = list(csv.DictReader(open(f, encoding='utf-8')))
    print('  file %s: %d rows; columns %s' % (os.path.basename(f), len(rows), list(rows[0].keys())))
    pairs = defaultdict(set); Nof = {}
    for r in rows:
        Z, c, m = int(r['Z']), int(r['charge']), int(r['mult']); pairs[(Z, c)].add(m); Nof[(Z, c)] = Z - c + 1
    print('  CONVENTION: a "pair" is a distinct (Z, charge); the file\'s charge column is the spectroscopic stage (Z = 1, charge = 1 is H I, one electron: row 1 says so), so N = Z − charge + 1 (fault 3: first scored as Z − charge, a bijection — the equal-set test is unchanged, the parity test was not); "values admitted at a pair" = the set of mult over its rows; the claim holds iff every two pairs with equal N admit equal sets')
    print('  N range %d–%d; min-N pair %s' % (min(Nof.values()), max(Nof.values()), min(Nof, key=Nof.get)))
    byN = defaultdict(set)
    for p, s in pairs.items(): byN[Nof[p]].add(frozenset(s))
    viol = {N: sorted(sorted(x) for x in S) for N, S in byN.items() if len(S) > 1}
    print('  pairs %d (Register 1779 / SC: 7,260); distinct N %d; N with more than one admitted set: %d %s' % (len(pairs), len(byN), len(viol), dict(list(viol.items())[:5])))
    print('  (iii) on the periodic ground, as F.2 states it: %s' % ('HOLDS on every pair, no exception' if not viol else 'FAILS at %d electron counts' % len(viol)))
    parity = sum(1 for p, s in pairs.items() if any((m - 1) % 2 != Nof[p] % 2 for m in s))
    print('  stronger reading (mult − 1 ≡ N mod 2 on every row): pairs violating %d' % parity)
    multi = Counter(len(s) for s in pairs.values()); print('  admitted-set sizes over pairs: %s' % dict(sorted(multi.items())))
    hI = [r for r in rows if r['Z'] == '1' and r['charge'] == '1'][0]
    print('  row (Z 1, charge 1): source "%s" — the file\'s charge is the stage, Z − charge = %d electrons is one short of "one electron"; 1779 writes "electron count Z − charge" (its sentence above)' % (hI['source'], 0))
    import glob
    sc = [f for f in os.listdir(H) if f.startswith('The_Method_1_6___Spectra') and f.endswith('-2.md')]
    if sc:
        S = L.read_member(sc[0]).split('\n')
        for i, l in enumerate(S):
            if re.search(r'^\s*\|?\s*`?charge`?\s*\|', l) or re.search(r'\bcharge\b.{0,80}(stage|ion|neutral|I = 1|= 1)', l): print('    SC %s L%d: %s' % (sc[0][-20:], i + 1, l.strip()[:200]))

hr('§3 the numerals the unit prints (appf.py\'s occurrence rule: a number in body text or a table; §/register/chapter/figure locators excluded) — against §32.1.4\'s row "Appendix F, the numbers … 33"')
NUM = re.compile(r'(?<![\w§.])(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?(?![\w.]\d)')
EXCL = re.compile(r'(§\s?[\dA-F.]+|[Rr]egisters?\s+\d+(?:[–-]\d+)?|[Cc]hapters?\s+\d+(?:,\s*\d+)*(?:\s+and\s+\d+)?|F\.\d(?:\.\d)?|E\.\d(?:\.\d)?|\(i{1,3}\))')
occ = []
for k, l in enumerate(U):
    if l.startswith('#') or l.startswith('    '): continue
    for m in NUM.finditer(EXCL.sub(' ', l)): occ.append((F + k, m.group(0)))
print('  numeral occurrences in body text/tables after locator exclusion: %d %s' % (len(occ), occ))
row = [i + 1 for i, l in enumerate(M) if re.search(r'Appendix F, the numbers\s+\d', l)]
for ln in row: print('  §32.1.4 row L%d: %s' % (ln, M[ln - 1].strip()))
print('  §32.1.4.1 L%s cites "the counts of Appendices D, E and F"' % [i + 1 for i, l in enumerate(M) if 'counts of Appendices D, E and F' in l])
for fig in ('1,105', '1,442', '1,061', '1105', '1442', '1061', '1,738', '1,748', '735,860', '4.21', '0.192', '0.705'):
    print('  %s in unit: %d' % (fig, sum(1 for l in U if fig in l)))
print('  witness: the 20a-01 / 21a-04 / 16z-01 figures and Chapter 34\'s are printed nowhere in the unit; the WARNING lines 1309 / 1350 / 1401 / 1403 / 1461 are not engaged by any figure here')

hr('§4 Register entries the unit cites or that name it — heading present, first body line, WARNING lines in the entry')
cited = [1779]
naming = sorted({int(m.group(1)) for i, l in enumerate(R) for m in [re.match(r'^#{1,4}\s*(\d+)\s*$', l)] if m} & set())
ents = {}
hs = [(i, int(m.group(1))) for i, l in enumerate(R) for m in [re.match(r'^#{1,4}\s*(\d+)\s*$', l)] if m]
def entry_of(i0): return max([n for i, n in hs if i < i0], default=None)
namers = defaultdict(list)
for i, l in enumerate(R):
    if re.search(r'Appendix F\b|\bF\.[1-4](\.\d)?\b', l): namers[entry_of(i)].append(i + 1)
print('  Register entries naming Appendix F / F.n: %s' % {k: v for k, v in sorted(namers.items())})
for n in sorted(set(cited) | set(namers) | {296, 297, 320, 321, 371, 1762, 1786}):
    sp = rspan(n)
    if sp is None: print('  %d: NO HEADING' % n); continue
    body = R[sp[0]:sp[1]]
    warn = [sp[0] + k + 1 for k, l in enumerate(body) if 'WARNING' in l]
    print('  %d: heading R%d; WARNING lines %s; body: %s' % (n, sp[0], warn or 'none', (rbody(n) or '')[:150]))
later = [n for n in namers if n > 1780]
print('  entries later than 1780 (the rebuild) naming the appendix: %s' % later)

hr('§5 F.3\'s rule in the Register ("refuted by its own extent" — "several of the corrections the Register carries are exactly this rule firing")')
pat = re.compile(r'refuted by (its|their) own extent|extent.{0,60}(empty|whole of it)|(empty|whole of it).{0,60}extent', re.I)
hits = defaultdict(list)
for i, l in enumerate(R):
    if pat.search(l): hits[entry_of(i)].append(i + 1)
print('  Register entries matching: %d %s' % (len(hits), dict(hits)))
ext = [i + 1 for i, l in enumerate(M) if re.search(r'refuted by its own extent', l)]
print('  main sites of "refuted by its own extent": %s (enclosing: %s)' % (ext, [next(M[j - 1][:40] for j in range(x, 0, -1) if re.match(r'^#{1,4}\s', M[j - 1])) for x in ext]))
print('  CONVENTION: "several" scored as ≥ 3 distinct Register entries whose text matches the rule\'s words or its outcome (empty / whole extent); the probe is a token probe and is stated as such')

hr('§6 24b-06 re-take: #P-complete sites in the main volume, with enclosing heading (chat 137 recorded F.4.3 as a site)')
for i, l in enumerate(M):
    if '#P-complete' in l:
        enc = next(M[j - 1][:50] for j in range(i + 1, 0, -1) if re.match(r'^#{1,4}\s', M[j - 1]))
        print('  L%d [%s] %s' % (i + 1, enc, l.strip()[:100]))
print('  F.4.3 body (L%d–L%d) carries "#P": %d; "complete": %d' % (heads[-1][0], G - 1, sum('#P' in l for l in M[heads[-1][0] - 1:G - 1]), sum('complete' in l for l in M[heads[-1][0] - 1:G - 1])))

hr('§7 24b-05 re-take: F.3.3 / F.3.2 / F.3.1 tokens, main and Register (Register 1786 renumbered F.3.3 → F.3.1)')
for tok in ('F.3.3', 'F.3.2', 'F.3.1'):
    ms = [i + 1 for i, l in enumerate(M) if re.search(re.escape(tok) + r'(?!\d)', l)]
    rs = [(i + 1, entry_of(i)) for i, l in enumerate(R) if re.search(re.escape(tok) + r'(?!\d)', l)]
    print('  %s: main %s; Register (line, entry) %s' % (tok, ms, rs))
print('  1786 body: %s' % (rbody(1786) or '')[:330])
