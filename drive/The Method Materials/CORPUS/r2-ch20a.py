# r2-ch20a.py — chat 133 — R2 computable instrument for the main volume's Appendix B (`## Appendix B` to `## Appendix C`).
# Reads MEMBERS by name (never a bundle path); imports r2lib by path; deterministic (no wall-clock). Appendix B is PRE-PP:
# headings and Statement lines are diffed against the Prints & Proofs original at /home/claude/PP_The_Method_1_6.md (fetched
# at the gate; section number stripped from BOTH sides; PP's sub-headings are unmarked plain lines found by scan). Every printed
# count is re-taken from the Spectra Compendium's Part II table DATA rows (a count word counts DATA rows); the collection split
# (107 / 250 / 35 rows) has no table column and is record-carried (registers 1763, 1768) — a BUDGET is stated, not a negative.
# Fault 5 (self-caught after banking; golden deleted and re-banked): a numeral followed by a comma that is not a thousands group (`1763,`) is a numeral.
# Conventions named before scoring: a DATA row is a `| ` line of the Part II table that is not the header, not the separator and
# not a prose line; a two-member channel is a starred species; an element is the species' first token; bracket `a/b` contributes
# a passes of b cells; Decimal.quantize ROUND_HALF_UP for every rounding; a threshold test `> 0.25` is strict as printed.
import os, re, io, sys, importlib.util, contextlib, itertools, csv
from decimal import Decimal as D, ROUND_HALF_UP
from collections import Counter, defaultdict
H = os.path.dirname(os.path.abspath(__file__))
def load(name, quiet=False):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), os.path.join(H, name + '.py')); mod = importlib.util.module_from_spec(spec)
    if quiet:
        with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(mod)
    else: spec.loader.exec_module(mod)
    return mod
L = load('r2lib'); heading_line, section_span, has_token = L.heading_line, L.section_span, L.has_token
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
M = rd('The_Method_1_6-2.md'); R = rd('The_Method_1_6___The_Register-2.md'); S = rd('The_Method_1_6___Spectra_Compendium-2.md')
PPP = '/home/claude/PP_The_Method_1_6.md'
PP = open(PPP, encoding='utf-8').read().split('\n') if os.path.exists(PPP) else None
VOL = {'main': M, 'reg': R, 'mc': rd('The_Method_1_6___Mathematical_Compendium-2.md'), 'pc': rd('The_Method_1_6___The_Physics_Compendium-2.md'),
       'ioi': rd('The_Method_1_6___The_Index_of_Indices-2.md'), 'sc': S}
def hr(t): print('\n' + '=' * 96 + '\n' + t + '\n' + '=' * 96)
def body_range(M, sec):   # copied verbatim from r2-ch19a.py (there from r2-ch18a.py / r2-ch17e.py / r2-ch17c.py / r2-ch17a.py / r2-ch16z.py; owed to r2lib, DEFERRED): heading to next heading of any rank, body occurrence
    s = heading_line(M, sec)
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1]): return (s, i)
    return (s, len(M) + 1)
def rbody(n):   # copied verbatim from r2-ch19a.py (there from r2-ch18a.py / r2-ch17e.py / r2-ch17c.py / r2-ch17b.py; owed to r2lib, DEFERRED): first non-blank line after '### n'
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())
def lettered(M, tag):   # copied verbatim from r2-ch19a.py (there from r2-ch18a.py / r2-ch17e.py / r2-ch17c.py; owed to r2lib, DEFERRED): lettered heading, exact token, hits in order; body = LAST
    hits = [i for i, l in enumerate(M, 1) if re.match(r'^#{2,4}\s*' + re.escape(tag) + r'(?!\.\d)(?!\d)\b', l)]
    return hits
def q(x, places): return str(D(str(x)).quantize(D(places), rounding=ROUND_HALF_UP))
norm = lambda s: re.sub(r'\s+', ' ', s.strip())
def sites(pat, vols=VOL, flags=0): return {v: [i + 1 for i, l in enumerate(t) if re.search(pat, l, flags)] for v, t in vols.items()}
def rentry(n):
    i = next((i for i, l in enumerate(R, 1) if re.match(r'^#{1,4}\s*%d\s*$' % n, l)), None)
    if i is None: return None, []
    j = next((k for k in range(i + 1, len(R) + 1) if re.match(r'^#{1,4}\s*\d+\s*$', R[k - 1])), len(R) + 1)
    return i, R[i:j - 1]

hr('§0 BOUNDARY — own heading scan; the unit is `## Appendix B` (body = last hit) to `## Appendix C` (body = last hit)')
appB = [i for i, l in enumerate(M, 1) if re.match(r'^## Appendix B ', l)]; appC = [i for i, l in enumerate(M, 1) if re.match(r'^## Appendix C ', l)]
unit = (appB[-1], appC[-1]); UL = M[unit[0] - 1:unit[1] - 1]
Bn = [(i, l) for i, l in enumerate(M, 1) if unit[0] < i < unit[1] and re.match(r'^#{2,4}\s*B\.\d', l)]
print('  `## Appendix B`', appB, '; `## Appendix C`', appC, '; unit L%d–L%d = %d lines; B.n headings:' % (unit[0], unit[1] - 1, unit[1] - unit[0]), [(i, l.split()[1]) for i, l in Bn])
print('  lettered(M, "B.1") =', lettered(M, 'B.1'), '; lettered(M, "B.2") =', lettered(M, 'B.2'), '; unmarked-heading test (blank line above + `B.n ` start):', [unit[0] + k for k, l in enumerate(UL) if k and not UL[k - 1].strip() and re.match(r'^\s*B\.\d+ ', l)])
def uline(pat): return [unit[0] + i for i, l in enumerate(UL) if re.search(pat, l)]
nums_unit = Counter(n for l in UL for n in re.findall(r'(?<![\d,.])\d{1,3}(?:,\d{3})+(?!\d)(?!,\d{3})|(?<![\d,.])\d+(?!\d)(?!,\d{3})', l))
print('  numerals in the unit (digit-bounded both sides, comma groups kept):', sorted(nums_unit.items(), key=lambda t: -int(t[0].replace(',', '')))[:40])

hr('§1 THE SPECTRA COMPENDIUM PART II TABLE — DATA rows parsed; every count of the B.2 paragraph (L10195–L10202) re-taken from the table')
p2 = [i for i, l in enumerate(S, 1) if re.match(r'^# II ', l)][-1]; p3 = [i for i, l in enumerate(S, 1) if re.match(r'^# III ', l)][-1]
hdr = next(i for i in range(p2, p3) if S[i - 1].startswith('| species |'))
cols = [c.strip() for c in S[hdr - 1].strip().strip('|').split('|')]
rows, skipped = [], []
for i in range(hdr + 2, p3):
    l = S[i - 1]
    if not l.startswith('|'): continue
    cells = [c.strip() for c in l.strip().strip('|').split('|')]
    if len(cells) != len(cols) or cells[0] in ('element', '---'): skipped.append((i, l[:40])); continue
    rows.append((i, dict(zip(cols, cells))))
elem_tbl = [(i, [c.strip() for c in S[i - 1].strip().strip('|').split('|')]) for i in range(hdr + 2, p3) if S[i - 1].startswith('|') and len([c for c in S[i - 1].strip().strip('|').split('|')]) == 2]
elem_tbl = [(i, c) for i, c in elem_tbl if c[0] not in ('element', '---')]
print('  Part II `# II` S%d to `# III` S%d; header S%d columns %s' % (p2, p3, hdr, cols))
print('  DATA rows parsed: %d (S%d–S%d); non-DATA `|` lines skipped inside the span: %d (the element table %d rows at S%d–S%d; separator/header lines)' % (len(rows), rows[0][0], rows[-1][0], len(skipped), len(elem_tbl), elem_tbl[0][0], elem_tbl[-1][0]))
prose_in = [i for i in range(hdr + 2, p3) if S[i - 1].strip() and not S[i - 1].startswith('|') and not S[i - 1].startswith('**')]
print('  prose lines inside the table span (read, not rows):', [(i, S[i - 1][:60]) for i in prose_in])
starred = [r for r in rows if r[1]['species'].endswith('*')]; unstar = [r for r in rows if not r[1]['species'].endswith('*')]
sp = lambda r: (r[1] if isinstance(r, tuple) else r)['species'].rstrip('*').strip(); el = lambda r: sp(r).split()[0]   # fault 1 (self-caught): §4 passes the row dict, §1 the (line, dict) tuple
species = sorted(set(sp(r) for r in rows)); elements = sorted(set(el(r) for r in rows))
def I(s): return int(s.replace(',', ''))
levels = sum(I(r[1]['levels']) for r in rows); interior = sum(I(r[1]['interior']) for r in rows)
two = [r for r in rows if I(r[1]['levels']) == 2]
print('  rows %d (printed 596: %s); starred %d (printed 119 two-member: %s); non-starred %d (printed 477: %s); levels==2 rows %d; starred == levels==2: %s'
      % (len(rows), len(rows) == 596, len(starred), len(starred) == 119, len(unstar), len(unstar) == 477, len(two), set(r[0] for r in starred) == set(r[0] for r in two)))
print('  elements %d (printed 28: %s); species %d (printed 70: %s); levels sum %s (printed 3,342: %s); interior sum %s (printed 2,269: %s)'
      % (len(elements), len(elements) == 28, len(species), len(species) == 70, f'{levels:,}', levels == 3342, f'{interior:,}', interior == 2269))
print('  elements:', elements)
br = Counter(); bp = bt = 0; brows = []; fails = 0; frow = 0; details = []
for i, r in rows:
    b = r['bracket']; m = re.fullmatch(r'(\d+)/(\d+)', b)
    if m:
        a, t = int(m.group(1)), int(m.group(2)); bp += a; bt += t; brows.append(i); br['a/b'] += 1
        if a < t: fails += t - a; frow += 1
    else: br[b] += 1
print('  bracket column: %s; bracket rows %d (printed 392: %s); passes %s of %s (printed 1,577 of 1,738: %s); failing cells %d in %d rows (SC L994 prints 161 in 98: %s)'
      % (dict(br), len(brows), len(brows) == 392, f'{bp:,}', f'{bt:,}', (bp, bt) == (1577, 1738), fails, frow, (fails, frow) == (161, 98)))
print('  no-triple %d (printed 78: %s); untested %d (printed 126: %s); 392 + 78 + 126 = %d = rows: %s' % (br['no-triple'], br['no-triple'] == 78, br['untested'], br['untested'] == 126, len(brows) + br['no-triple'] + br['untested'], len(brows) + br['no-triple'] + br['untested'] == len(rows)))
print('  the collection split (844 of 844 on 107 rows; 658 of 813 on 250; 75 of 81 on 35): no table column marks the collection — BUDGET: record-carried at registers 1763, 1768; arithmetic only: 844+658+75 = %d, 844+813+81 = %d, 107+250+35 = %d; 1738−1577 = %d (= failing cells: %s); 813−658 = %d, 81−75 = %d, 155+6 = %d'
      % (844 + 658 + 75, 844 + 813 + 81, 107 + 250 + 35, 1738 - 1577, 1738 - 1577 == fails, 813 - 658, 81 - 75, 155 + 6))
print('  1,577/1,738 = %s %% (HALF_UP 1 place); interior − bracket cells = %s − %s = %d (cells in no-triple/untested rows: %d — equal: %s)'
      % (q(D(1577) / D(1738) * 100, '0.1'), f'{interior:,}', f'{bt:,}', interior - bt, sum(I(r['interior']) for i, r in rows if not re.fullmatch(r'\d+/\d+', r['bracket'])), interior - bt == sum(I(r['interior']) for i, r in rows if not re.fullmatch(r'\d+/\d+', r['bracket']))))
ib = sum(I(r['interior']) for i, r in rows if re.fullmatch(r'\d+/\d+', r['bracket'])); short = [(i, sp(r), r['series'], r['interior'], r['bracket']) for i, r in rows if re.fullmatch(r'\d+/\d+', r['bracket']) and int(r['bracket'].split('/')[1]) != I(r['interior'])]
print('  bracket rows: interior sum %s vs bracket denominators %s — rows whose denominator differs from interior: %d %s' % (f'{ib:,}', f'{bt:,}', len(short), short[:12]))
ec = Counter(el(r) for r in rows); tbl = {c[0]: int(c[1]) for i, c in elem_tbl}
print('  element table S%d–S%d: %d elements, sum %d; equals the per-element row counts of the DATA rows: %s; mismatches: %s'
      % (elem_tbl[0][0], elem_tbl[-1][0], len(tbl), sum(tbl.values()), tbl == dict(ec), {k: (tbl.get(k), ec.get(k)) for k in set(tbl) | set(ec) if tbl.get(k) != ec.get(k)}))
tot_line = [(i, S[i - 1][:90]) for i in range(hdr, p3) if re.search(r'596 channel rows', S[i - 1])]
print('  the table\'s own totals line(s):', tot_line)
nt_star = [r for r in rows if r[1]['bracket'] == 'no-triple' and r[1]['species'].endswith('*')]
print('  no-triple rows that are starred (two-member) %d of %d; starred rows by bracket: %s' % (len(nt_star), br['no-triple'], dict(Counter(r[1]['bracket'] if not re.fullmatch(r'\d+/\d+', r[1]['bracket']) else 'a/b' for r in starred))))

hr('§2 THE MAIN PARAGRAPH L10195–L10202 AGAINST SC L994 — numerals compared as sets (the main is the summary; the compendium the source)')
mp = norm(' '.join(M[10194:10202])); sc = S[993]
def numset(t): return set(n for n in re.findall(r'(?<![\d,.])\d{1,3}(?:,\d{3})+(?!\d)(?!,\d{3})|(?<![\d,.])\d+(?!\d)(?!,\d{3})', t))
a, b = numset(mp), numset(sc)
print('  main-paragraph numerals:', sorted(a, key=lambda x: int(x.replace(',', '')))); print('  in main not in SC L994:', sorted(a - b)); print('  in SC L994 not in main (the compendium\'s extra detail):', sorted(b - a, key=lambda x: int(x.replace(',', ''))))
print('  main L10195 opens with the volume title and `Part II`: %s; SC Part II heading `# II · THE CHANNELS` at S%d: %s' % ('Part II' in M[10194], p2, S[p2 - 1]))

hr('§3 THE OPENER L10169 / L10171 — 153 channels, 1105 of 1105, the 763 cells, the union stated in Chapter 24')
sp24 = section_span(M, '24'); br24 = body_range(M, '24'); print('  Chapter 24: section_span', sp24, '; body_range', br24, '; heading', M[sp24[0] - 1][:60])
ch24 = M[sp24[0] - 1:sp24[1] - 1]
for pat, lab in [(r'(?<![\d,.])763(?![\d,])', '763'), (r'(?<![\d,.])1,?105(?![\d,])', '1,105'), (r'(?<![\d,.])1,?442(?![\d,])', '1,442'), (r'(?<![\d,.])337(?![\d,])', '337'), (r'(?<![\d,.])153(?![\d,])', '153'), (r'\bunion\b', 'union'), (r'earlier verification', 'earlier verification')]:
    h = [sp24[0] + k for k, l in enumerate(ch24) if re.search(pat, l)]
    print('  Chapter 24 hits for %s: %s %s' % (lab, h, [norm(M[i - 1])[:150] for i in h[:3]]))
print('  1,442 − 1,105 = %d (Chapter 24 L6970: "Of the 1,442, the 1,105 added in this work"); the appendix\'s 763 + 1,105 = %d; 763 + 1105 − 1442 = %d' % (1442 - 1105, 763 + 1105, 763 + 1105 - 1442))
print('  763 across the six volumes (digit-bounded):', sites(r'(?<![\d,.])763(?![\d,])'))
print('  "earlier verification" across the six volumes:', sites(r'earlier verification'), '; the other main site read:', [(i, norm(M[i - 1])[:160]) for i in sites(r'earlier verification', {'main': M})['main'] if not (unit[0] <= i < unit[1])])
print('  153 channels / 1105 in main outside the unit:', {k: [i for i in v if not (unit[0] <= i < unit[1])] for k, v in sites(r'153 channels|(?<![\d,.])1,?105(?![\d,])', {'main': M}).items()})
e2865 = next(i for i, l in enumerate(R, 1) if 'CHAPTER 24 CLAIMED' in l); print('  Register line R%d (entry %s) body: %s' % (e2865, next(re.match(r'^#{1,4}\s*(\d+)\s*$', R[j - 1]).group(1) for j in range(e2865, 0, -1) if re.match(r'^#{1,4}\s*\d+\s*$', R[j - 1])), norm(R[e2865 - 1])[:600]))
for n in (630, 631):
    ln, b = rentry(n); print('  Register %d (R%d) body: %s' % (n, ln, norm(rbody(n))[:420])); print('     WARNING lines:', [norm(l)[:200] for l in b if 'WARNING' in l])

hr('§4 B.3 FLAGGED CHANNELS — the printed five against the POPULATION of σ(δ) > 0.25 in the Part II table (strict as printed; V departure from 4ν/3 has no table column — BUDGET)')
flag = [(i, r) for i, r in rows if D(r['σ(δ)']) > D('0.25')]
print('  rows with σ(δ) > 0.25: %d —' % len(flag), [(sp(r), r['series'], r['σ(δ)']) for i, r in flag])
printed = [('Al I', '3s²nd ²D', '0.630'), ('Al II', '3snd ¹D', '0.390'), ('Al II', '3snf ³F°', '0.409'), ('Li I', 'np 2P°', '0.678'), ('Si II', '3s²np ²P°', '0.272')]
for s_, ser, v in printed:
    cand = [(i, r) for i, r in rows if sp(r) == s_ and norm(r['series']).replace('*', '°') == norm(ser).replace('*', '°')]
    cand2 = [(i, r) for i, r in rows if sp(r) == s_ and re.sub(r'[^A-Za-z0-9]', '', r['series']) == re.sub(r'[^A-Za-z0-9]', '', ser)]
    c = cand or cand2
    print('  printed %s %s %s → table row(s) %s; σ(δ) %s → HALF_UP 3 places %s: %s; interior %s; n %s'
          % (s_, ser, v, [i for i, r in c], [r['σ(δ)'] for i, r in c], [q(r['σ(δ)'], '0.001') for i, r in c], [q(r['σ(δ)'], '0.001') == v for i, r in c], [r['interior'] for i, r in c], [r['n'] for i, r in c]))
print('  fault 3 (self-caught) — every Si II row in the table, read before the printed Si II 3s²np ²P° 0.272 is scored:', [(i, r['series'], r['σ(δ)'], r['interior'], r['n']) for i, r in rows if sp(r) == 'Si II'])
print('  every table row with σ(δ) on [0.25, 0.30):', [(i, sp(r), r['series'], r['σ(δ)']) for i, r in rows if D('0.25') <= D(r['σ(δ)']) < D('0.30')], '; rows with σ(δ) == 0.2720 exactly or 0.272 rounded:', [(i, sp(r), r['series'], r['σ(δ)']) for i, r in rows if q(r['σ(δ)'], '0.001') == '0.272'])
print('  Si II across the six volumes with 3s²np or ²P°: ', {k: v[:8] for k, v in sites(r'Si II.*(3s²np|2P°|²P°)').items()})
print('  Register lines naming Si II 3s²np / ²P° (entry, text):', [(next(re.match(r'^#{1,4}\s*(\d+)\s*$', R[j - 1]).group(1) for j in range(i, 0, -1) if re.match(r'^#{1,4}\s*\d+\s*$', R[j - 1])), i, norm(R[i - 1])[:420]) for i in sites(r'Si II.*(3s²np|2P°|²P°)', {'reg': R})['reg']])
print('  0.272 across the six volumes (digit-bounded):', sites(r'(?<![\d.])0\.272(?!\d)'))
r1774 = rbody(1774); print('  Register 1774 (a later entry on the block, the witness grep found): J-resolved clause present: %s; "recorded rather than resolved": %s; "a question about the flag, not about the copy": %s; WARNING lines: %s' % ('J-resolved as 3s2.np 2P* J=1/2 and J=3/2 at 0.0878 and 0.0868' in r1774, 'recorded rather than resolved' in r1774, 'a question about the flag, not about the copy' in r1774, [l[:80] for l in rentry(1774)[1] if 'WARNING' in l]))
unlisted = [(sp(r), r['series'], r['σ(δ)']) for i, r in flag if not any(sp(r) == s_ and re.sub(r'[^A-Za-z0-9]', '', r['series']) == re.sub(r'[^A-Za-z0-9]', '', ser) for s_, ser, v in printed)]
print('  flagged-by-threshold rows NOT among the printed five: %d %s — "Every flag in this collection has an identified cause; none is unexplained": the printed table names causes for %d; the population is %d' % (len(unlisted), unlisted[:40], len(printed), len(flag)))
firstc = [r for i, r in rows if r['fits'] == '1']; firstsp = set(sp(r) for r in firstc)
print('  the `fits` column values: %s — rows with fits==1: %d, species %d; B.1\'s sources species among them: %s' % (dict(Counter(r['fits'] for i, r in rows)), len(firstc), len(firstsp), sorted(firstsp)[:30]))
li = [(i, r) for i, r in rows if sp(r) == 'Li I' and r['series'].startswith('np')]; print('  Li I np row(s): %s — "39 cells to n = 42": interior %s, n-range %s' % ([i for i, r in li], [r['interior'] for i, r in li], [r['n'] for i, r in li]))
print('  σ(δ) column = "δ spread" of B.3 (the column heads at S%d); 4ν/3 across the six volumes (docket 11): %s' % (hdr, {k: len(v) for k, v in sites(r'4ν/3').items()}))

hr('§5 B.1 SOURCES — the species the appendix lists, and whether each has rows in the Part II table; B.1 against SC Part IV B.1 line by line')
b1 = body_range(M, 'B.1') if heading_line(M, 'B.1') else None
b1s, b1e = lettered(M, 'B.1')[-1], lettered(M, 'B.2')[-1]
srcs = M[b1s:b1e - 1]   # fault 2 (self-caught): the species column starts at raw column 30 on the compilation lines AND on the wrapped continuation line; citation lines (year / JPCRD) and the header carry no species
spec_txt = ''   # fault 4 (self-caught): a new compilation line starts a new comma-list; only the wrapped continuation line (≥ 28 leading spaces) joins with a space
for l in srcs:
    if not re.match(r'^ {2,}\S', l) or re.match(r'^  (\d{4}|JPCRD|compilation)', l) or l.strip().startswith('**') or l.strip().startswith('Hori'): continue
    spec_txt += (' ' if re.match(r'^ {28,}', l) else ', ') + l[30:].strip()
spec_txt = norm(spec_txt)
listed = [s.strip() for s in re.split(r',\s*', spec_txt) if s.strip()]
listed = [re.sub(r'\s*\((?:³⁄₂|¹⁄₂)\)', '', s) for s in listed]
print('  heading_line(M, "B.1") (numeric-only resolver): %s — lettered resolver used: B.1 L%d, B.2 L%d' % (heading_line(M, 'B.1'), b1s, b1e))
print('  species listed in B.1: %d %s; distinct %d; elements %d %s' % (len(listed), listed, len(set(listed)), len(set(s.split()[0] for s in listed)), sorted(set(s.split()[0] for s in listed))))
absent = [s for s in set(listed) if s not in species]; print('  B.1 species with NO row in the Part II table: %s; Ne I rows in the table: %s' % (absent, [(i, r['series']) for i, r in rows if sp(r) == 'Ne I'][:6]))
scb1 = [i for i, l in enumerate(S, 1) if re.match(r'^## B\.1 ', l)][-1]; scb2 = [i for i, l in enumerate(S, 1) if re.match(r'^## B\.2 ', l)][-1]
vb = [norm(l) for l in M[b1s:b1e - 1] if l.strip()]; sb = [norm(l) for l in S[scb1:scb2 - 1] if l.strip()]
print('  main B.1 body non-blank lines %d vs SC B.1 body %d; differing: %s' % (len(vb), len(sb), [(x[:70], y[:70]) for x, y in itertools.zip_longest(vb, sb) if x != y]))
scb3 = [i for i, l in enumerate(S, 1) if re.match(r'^## B\.3 ', l)][-1]; scend = [i for i, l in enumerate(S, 1) if i > scb3 and re.match(r'^#', l)][0]
b3s = lettered(M, 'B.3')[-1]; b4s = lettered(M, 'B.4')[-1]
vb3 = [norm(l) for l in M[b3s:b4s - 1] if l.strip()]; sb3 = [norm(l) for l in S[scb3:scend - 1] if l.strip()]
print('  main B.3 body vs SC B.3 body: %d vs %d lines; differing: %s' % (len(vb3), len(sb3), [(x[:70], y[:70]) for x, y in itertools.zip_longest(vb3, sb3) if x != y]))
auth = ['Kaufman', 'Martin', 'Kramida', 'Sansonetti', 'Hori', 'Korobov', 'Singer', 'Stanojevic', 'Weidemüller', 'Côté', 'Sugar', 'Corliss', 'Musgrove']
refs = [i for i, l in enumerate(M, 1) if re.match(r'^## References', l)][-1]; refbody = '\n'.join(M[refs:])
print('  References body (`## References` L%d to end): author hits —' % refs, {a: has_token(refbody, a) for a in auth})
print('  CODATA / arXiv / JPCRD / NIST in References body:', {a: has_token(refbody, a) for a in ['CODATA', 'arXiv', 'JPCRD', 'NIST']})

hr('§6 B.4 — the chapter pointers, COORDINATES-2.13 (104,832 cells) measured on the delivered file, the citation form')
for c in ('22', '23'):
    s_ = section_span(M, c); print('  Chapter %s: %s span %s; `Rule` headings/lines inside: %d; first heading: %s' % (c, M[s_[0] - 1][:40], s_, sum(1 for l in M[s_[0] - 1:s_[1] - 1] if re.match(r'^(#{2,4}\s*)?\**Rule \d', l.strip())), next((norm(l)[:60] for l in M[s_[0]:s_[1] - 1] if re.match(r'^#', l)), None)))
print('  word-bounded `rule` (any case) in Chapter 22 body: %d; in Chapter 23 body: %d; Chapter 23 first lines with it: %s' % (has_token('\n'.join(M[section_span(M, '22')[0] - 1:section_span(M, '22')[1] - 1]), 'rule'), has_token('\n'.join(M[section_span(M, '23')[0] - 1:section_span(M, '23')[1] - 1]), 'rule'), [(i, norm(M[i - 1])[:90]) for i in range(section_span(M, '23')[0], section_span(M, '23')[1]) if has_token(M[i - 1], 'rule')][:3]))
print('  763 lines in the Register and the Index of Indices (read): %s' % [(v, i, norm(t_[i - 1])[:140]) for v, t_ in (('reg', R), ('ioi', VOL['ioi'])) for i in sites(r'(?<![\d,.])763(?![\d,])', {v: t_})[v]])
print('  "rules of Chapters" / "Rule N" sites in Chapters 22–23 (first five):', [(i, norm(M[i - 1])[:70]) for i in range(section_span(M, '22')[0], section_span(M, '23')[1]) if re.match(r'^\s*\**Rule \d', M[i - 1])][:5])
cand = [os.path.join(H, 'COORDINATES-2_13.csv'), '/mnt/project/COORDINATES-2_13.csv']
f = next((p for p in cand if os.path.exists(p)), None)
if f is None: print('  COORDINATES-2_13.csv: not a member and not in the project folder — BUDGET: 104,832 tested against SC L119 only')
else:
    with open(f, encoding='utf-8', newline='') as fh:
        rd_ = list(csv.reader(fh))
    hdrc = rd_[0]; data = [r for r in rd_[1:] if any(c.strip() for c in r)]
    print('  %s: header %s; DATA rows %s (printed 104,832: %s); (Z, charge) pairs %s; grade counts %s' % ('member' if f.startswith(H) else 'project file', hdrc, f'{len(data):,}', len(data) == 104832, f'{len(set((r[0], r[1]) for r in data)):,}', dict(Counter(r[hdrc.index("grade")] for r in data)) if 'grade' in hdrc else 'no grade column'))
print('  SC "The file" heading S%d; 104,832 in SC: %s; COORD( citation form in SC: %s; in main: %s; Register entry naming 104,832: %s'
      % ([i for i, l in enumerate(S, 1) if re.match(r'^## The file', l)][-1], sites(r'104,832', {'sc': S})['sc'], sites(r'COORD\(', {'sc': S})['sc'][:6], sites(r'COORD\(', {'main': M})['main'], [(i, next(re.match(r'^#{1,4}\s*(\d+)\s*$', R[j - 1]).group(1) for j in range(i, 0, -1) if re.match(r'^#{1,4}\s*\d+\s*$', R[j - 1]))) for i, l in enumerate(R, 1) if '104,832' in l]))
print('  "ionisation limits carried per channel": the table\'s `limit cm⁻¹` column is filled on %d of %d rows' % (sum(1 for i, r in rows if r['limit cm⁻¹'].strip()), len(rows)))

hr('§7 CITED REGISTER ENTRIES — rbody and WARNING lines (1578, 1699, 1700, 1763, 1768; 630–631 in §3)')
for n in (1578, 1699, 1700, 1763, 1768):
    ln, b = rentry(n); print('  Register %d (R%d, %d lines): %s' % (n, ln, len(b), norm(rbody(n))[:330])); print('     WARNING lines:', [norm(l)[:200] for l in b if 'WARNING' in l])
later = [(i, next(re.match(r'^#{1,4}\s*(\d+)\s*$', R[j - 1]).group(1) for j in range(i, 0, -1) if re.match(r'^#{1,4}\s*\d+\s*$', R[j - 1])), norm(l)[:90]) for i, l in enumerate(R, 1) if re.search(r'Appendix B\b', l)]
print('  Register lines naming Appendix B (entry, text):', [(e, t) for i, e, t in later])
print('  1763 names 658 of 813 / 155 / 318 rows: %s; 1768 names 75 of 81 / 35 / 10 no-triple: %s' % ([x in rbody(1763) for x in ('658 OF 813', '155', '318')], [x in rbody(1768) for x in ('75 OF 81', '35 CLOSE', '10 CLOSE NO-TRIPLE')]))
print('  1763\'s 318 rows = 250 with cells + 68 no-triple? no-triple rows 78 − the 10 that 1768 added = %d; 250 + 68 = %d: %s' % (78 - 10, 250 + 68, 250 + 68 == 318))
print('  1763 says 318 rows close (658 of 813) while the appendix and SC L994 say 250 rows — 318 − 250 = %d; 1768\'s 45 = 35 + 10: %s' % (318 - 250, 35 + 10 == 45))

hr('§8 PRE-PP DIFF — headings (number stripped BOTH sides), Statement lines, non-blank body lines of the unit against PP from its `Appendix B` line (found by scan)')
if PP is None: print('  PP not on disk — BUDGET')
else:
    ppB = [i for i, l in enumerate(PP, 1) if re.match(r'^#+ Appendix B ', l)][-1]; ppC = [i for i, l in enumerate(PP, 1) if re.match(r'^#+ Appendix C ', l)][-1]
    ppH = [(i, norm(l)) for i, l in enumerate(PP, 1) if ppB < i < ppC and re.match(r'^ ?B\.\d+ \S', l)]
    strip = lambda t: re.sub(r'^#*\s*(Appendix [A-G]|[A-G]\.\d+(?:\.\d+)*)\s*[—-]?\s*', '', t).strip()
    vH = [(unit[0], M[unit[0] - 1])] + Bn; pH = [(ppB, PP[ppB - 1])] + [(i, l) for i, l in ppH]
    print('  PP `Appendix B` P%d, `Appendix C` P%d; PP sub-heading lines (unmarked, leading space): %s' % (ppB, ppC, [(i, l.split()[0]) for i, l in ppH]))
    for (vi, vl), (pi, pl) in itertools.zip_longest(vH, pH, fillvalue=(None, '')):
        print('  volume L%s "%s" | PP P%s "%s" | equal after stripping the number: %s' % (vi, strip(norm(vl)), pi, strip(norm(pl)), strip(norm(vl)) == strip(norm(pl))))
    st = lambda LL, a, b: [(i, norm(LL[i - 1])[:80]) for i in range(a, b) if re.match(r'^\s*\**(Statement|Definition|Theorem|Proof)\b', LL[i - 1])]
    print('  Statement/Definition/Theorem/Proof lines: volume %s; PP %s' % (st(M, unit[0], unit[1]), st(PP, ppB, ppC)))
    pv = [norm(l) for l in M[unit[0] - 1:unit[1] - 1] if l.strip()]; pp_ = [norm(l) for l in PP[ppB - 1:ppC - 1] if l.strip()]
    onlyV = [x for x in pv if x not in pp_]; onlyP = [x for x in pp_ if x not in pv]
    print('  non-blank lines: volume %d; PP %d; in volume not PP: %d; in PP not volume: %d' % (len(pv), len(pp_), len(onlyV), len(onlyP)))
    for x in onlyV: print('    V: ' + x[:150])
    for x in onlyP: print('    P: ' + x[:150])
    print('  PP B.3 header split across two lines ("specie"/"s"; "δ"/"spread") at P%s — the volume\'s single header L%d: "%s"' % ([i for i in range(ppB, ppC) if PP[i - 1].strip().startswith('specie ')], [i for i in range(unit[0], unit[1]) if M[i - 1].strip().startswith('species ')][0], norm(M[[i for i in range(unit[0], unit[1]) if M[i - 1].strip().startswith('species ')][0] - 1])))
