#!/usr/bin/env python3
# r2-ch17a.py — chat 128 — R2 computable batch for main L9716–L9805 (Chapter 35 head + epigraph, §35.1–§35.3), BUILD90.
# Reads MEMBERS from /home/claude/members; imports r2lib by path and the NIST ground-configuration table from
# r2-ch16y.py §3 by path (never retyped; its stdout is captured). Everything computed from the table is a
# RECONSTRUCTION. Every convention is named before a verdict is printed. Decimal, never round().
# r2-ch17a2.py — R3 (chat 153-R) — SUCCESSOR to r2-ch17a.py, re-anchored by tools/reanchor.py: every main-volume line the
# predecessor pinned as a literal is resolved by the text of the line it pointed at in the bundle its golden was
# banked against (9 anchors); nothing else changes. r2-ch17a.py is seated and never edited in place (chat 68).
# PROVED by tools/proveanchor.py when the line below says so; until then this file is a draft.
# PROVEANCHOR: NOT PROVED on 90+184, 92+188 or 98+202 — reproduces r2-ch17a.out byte-exact on those bundles (G0c)

# --- re-anchoring helper (tools/reanchor.py): a main-volume line found by its own text, never by a number ---
def _L(t, d=0):
    import os as _o
    global _LM
    try: _LM
    except NameError: _LM = open(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)), 'The_Method_1_6-2.md'), encoding='utf-8').read().split('\n')
    h = [i for i, l in enumerate(_LM, 1) if l == t]
    assert len(h) == 1, ('re-anchor: line text is not unique or is absent', t[:60], h)
    return h[0] + d
import os, re, io, sys, importlib.util, contextlib
from decimal import Decimal as D, ROUND_HALF_UP
H = os.path.dirname(os.path.abspath(__file__))
def load(name, quiet=False):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), os.path.join(H, name + '.py')); mod = importlib.util.module_from_spec(spec)
    if quiet:
        with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(mod)
    else: spec.loader.exec_module(mod)
    return mod
L = load('r2lib'); heading_line, section_span, has_token, enclosing = L.heading_line, L.section_span, L.has_token, L.enclosing
Y = load('r2-ch16y', quiet=True)            # §3 table: CONF, SYM, ENT, LQ, nl, cap, opening; validated in r2-ch16y (banked)
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
M = rd('The_Method_1_6-2.md'); R = rd('The_Method_1_6___The_Register-2.md'); PP = rd(os.path.join(H, '..', 'PP_The_Method_1_6.md'))
VOL = {'main': M, 'reg': R, 'mc': rd('The_Method_1_6___Mathematical_Compendium-2.md'), 'pc': rd('The_Method_1_6___The_Physics_Compendium-2.md'),
       'ioi': rd('The_Method_1_6___The_Index_of_Indices-2.md'), 'sc': rd('The_Method_1_6___Spectra_Compendium-2.md')}
def hr(t): print('\n' + '=' * 96 + '\n' + t + '\n' + '=' * 96)
def body_range(M, sec):   # copied verbatim from r2-ch16z.py (owed to r2lib, DEFERRED): heading to next heading of any rank, body occurrence
    s = heading_line(M, sec)
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1]): return (s, i)
    return (s, len(M) + 1)
def rbody(n):   # first non-blank line after '### n' (entries are '### N', blank, body)
    i = next(i for i, l in enumerate(R) if l.strip() == '### %d' % n)
    return next(l for l in R[i + 1:] if l.strip())
def q(x, places): return str(D(str(x)).quantize(D(places), rounding=ROUND_HALF_UP))
def sites(pat, vols=VOL, flags=0):
    return {v: [i + 1 for i, l in enumerate(t) if re.search(pat, l, flags)] for v, t in vols.items()}
def fmt(s): return ' '.join(f'{v}:{len(n)}' + ('[' + ','.join(map(str, n[:6])) + ('…' if len(n) > 6 else '') + ']' if n else '') for v, n in s.items())

# ---------------------------------------------------------------- 0. the unit, resolved twice, bounded by body_range
hr('0  UNIT main L9716–L9805 — heading lines by own scan, both resolvers')
for sec in ('35', '35.1', '35.2', '35.3', '35.4', '36'):
    print(f'  §{sec:5} heading_line {heading_line(M, sec):5}  body_range {body_range(M, sec)}  section_span {section_span(M, sec)}')
A, B = _L("entry point, read from the table's own coordinates with one observation per", -3), _L('completes the figure: *the silence was not only the finding — it was the address.*', 1)
assert heading_line(M, '35') == _L("entry point, read from the table's own coordinates with one observation per", -3) and body_range(M, '35.3')[1] == _L('### 35.4 How the method did it') and heading_line(M, '35.4') == _L('### 35.4 How the method did it')
print(f'  unit bound by body_range: L{A}–L{B} = {B - A + 1} lines; contents hit for "## 35." at L{[i+1 for i,l in enumerate(M) if l.startswith("## 35.")][0]} is not a body occurrence')
U = M[A - 1:B]; UT = '\n'.join(U)
print('  Prints & Proofs: "## 35." body occurrences in PP = %d; PP "# APPENDICES" at P%s — the unit is post-PP authoring, stated once, not diffed'
      % (sum(1 for l in PP if l.startswith('## 35.')), [i + 1 for i, l in enumerate(PP) if l.startswith('# APPENDICES')]))

# ---------------------------------------------------------------- 1. the reconstruction input, re-validated
hr('1  RECONSTRUCTION INPUT — the NIST table imported from r2-ch16y.py §3 (banked), re-validated here')
CONF, SYM, ENT, LQ, nl, cap, opening = Y.CONF, Y.SYM, Y.ENT, Y.LQ, Y.nl, Y.cap, Y.opening
print('  rows Z = 1..108: %d; electron counts validate: %s; Pd 5s absent: %s; Lr 7p: %s'
      % (len(CONF), all(sum(CONF[Z].values()) == Z for Z in CONF), '5s' not in CONF[46], CONF[103].get('7p')))

# ---------------------------------------------------------------- 2. the count conventions of §35.2 L9746–L9747
hr('2  COUNT CONVENTIONS — 107 of 107 across Z = 2–108 "hence the 106 transitions Chapter 34 counted"')
print('  rows Z = 2..108: %d (107 printed); steps Z−1→Z for Z = 3..108: %d (106 printed; §34.9 prints "106 elements, Z = 3 to 108")' % (108 - 2 + 1, 108 - 3 + 1))
print('  convention: a ROW is an element with a listed ground configuration (Z = 2..108, the table has 108 rows and Z = 1 seeds nothing);')
print('              a TRANSITION is the step Z−1 → Z, so 107 rows carry 106 transitions. Both figures are consistent under it; neither site names it.')
r1446 = rbody(1446)
print('  register 1446 headline (the observational edge):', re.sub(r'\s+', ' ', r1446)[:330])
print('  register 1712 says "No ground configuration is measured beyond Z = 108"; the unit L9746 says "every element with a measured ground configuration" across Z = 2–108')

# ---------------------------------------------------------------- 3. the n+ℓ sentence L9749–L9750 under named conventions (reconstruction)
hr('3  L9749–L9750 "smaller n+ℓ opens before larger n+ℓ without exception; at equal n+ℓ, smaller n first, except at exactly La, Ac and Th"')
def npl(s): n, l = nl(s); return n + l
seq = sorted(opening, key=lambda s: opening[s])
# convention O — first-opening order: a channel "opens" at the Z where it first holds an electron
v1 = [(s, t) for s in seq for t in seq if npl(s) < npl(t) and opening[s] > opening[t]]
v2 = [(s, t) for s in seq for t in seq if npl(s) == npl(t) and nl(s)[0] < nl(t)[0] and opening[s] > opening[t]]
print('  convention O (first occupation): clause 1 violations %s; clause 2 violations %s -> exception elements %s'
      % (v1 or 'none', [(s, t, opening[t]) for s, t in v2], sorted({SYM[opening[t] - 1] + str(opening[t]) for s, t in v2}, key=lambda x: int(re.sub(r'\D', '', x)))))
# convention S — per step: the entrant at Z against every channel with room at Z−1 (n ≤ 8, ℓ ≤ 3, as r2-ch16y's universe)
UNI = [f'{n}{l}' for n in range(1, 9) for l in 'spdf' if LQ[l] < n]
c1, c2, c2never, c2empty = [], [], [], []
for Z in range(3, 109):
    prev = CONF[Z - 1]; e = ENT[Z]; rivals = [s for s in UNI if prev.get(s, 0) < cap(s) and s != e]
    if any(npl(s) < npl(e) for s in rivals): c1.append(SYM[Z - 1] + str(Z))
    tie = [s for s in rivals if npl(s) == npl(e) and nl(s)[0] < nl(e)[0]]
    if tie:
        c2.append(SYM[Z - 1] + str(Z))
        if all(all(CONF[z].get(s, 0) == 0 for z in range(1, Z)) for s in tie): c2never.append(SYM[Z - 1] + str(Z))
        if all(prev.get(s, 0) == 0 for s in tie): c2empty.append(SYM[Z - 1] + str(Z))
print('  convention S (per step, rivals = channels with room at Z−1): clause 1 exceptions %s (%d); clause 2 exceptions %s (%d); union %d'
      % (' '.join(c1), len(c1), ' '.join(c2), len(c2), len(set(c1) | set(c2))))
mad = []
for Z in range(3, 109):
    prev = CONF[Z - 1]; cands = [s for s in UNI if prev.get(s, 0) < cap(s)]
    if min(cands, key=lambda s: (npl(s), nl(s)[0])) != ENT[Z]: mad.append(SYM[Z - 1] + str(Z))
print('  conditional-Madelung misses (r2-ch16y, register 1437): %s (%d) — equal to S\'s union: %s' % (' '.join(mad), len(mad), set(mad) == set(c1) | set(c2)))
print('  convention S\', clause 2 restricted to a passed-over channel NEVER occupied at any Z\' < Z: %s (%d)' % (' '.join(c2never), len(c2never)))
print('  convention S", clause 2 restricted to a passed-over channel EMPTY at Z−1: %s (%d)' % (' '.join(c2empty), len(c2empty)))
print('  register 1703: "selects d over uncollapsed f at La, Ac, Th — the complete tie-break exception set". Under O the set is {La, Ac} (Th opens nothing);')
print('  under S it is 1437\'s ten; only S\' returns exactly {La, Ac, Th}, and under S\' clause 1 is not "without exception" (Mo Rh Pd Au). The sentence')
print('  holds only with clause 1 read under O and clause 2 under S\' — two conventions in one sentence, neither named.')

# ---------------------------------------------------------------- 4. the g channels L9759–L9763 against register 1704
hr('4  g CHANNELS — hydrogenic depth −1/(2n²) at the printed precision (Decimal HALF_UP)')
for n, printed in ((5, '-0.020000'), (6, '-0.013889'), (7, '-0.010204'), (8, '-0.0078125')):
    val = -D(1) / (D(2) * D(n) ** 2); places = '0.' + '0' * (len(printed.split('.')[1]))
    print('  %dg: −1/(2·%d²) = %s  printed at 1704 %s  %s' % (n, n, q(val, places), printed, 'EXACT' if q(val, places) == printed else 'DIFFERS'))
ug = [int(x) for x in re.findall(r'(\d+)g at (\d+)|at (\d+)', re.search(r'5g at 65.*?8g at 28', UT, re.S).group(0)) for x in x if x][1::2] if False else re.findall(r'g at (\d+)', re.sub(r'\s+', ' ', re.search(r'5g at 65.*?8g at 28', UT, re.S).group(0)))
rg = re.findall(r'over (\d+)', rbody(1704))
print('  counts by g channel: unit %s; register 1704 %s; equal: %s' % (ug, rg, ug == rg))
print('  "no g block below Z = 121": the chain runs to Z = 120 (1702, 1712); 121 is the first unwalked Z — consistent, record-carried')

# ---------------------------------------------------------------- 5. the five contested rows L9766–L9769 against register 1705
hr('5  CORRELATION CLAUSE — five rows, dm2/margin, all positive')
u5 = re.findall(r'[+−-]\d+\.\d+', ' '.join(U[_L('**Correlation widens every contested step.** At the five elements where the') - A:_L('widens.*') - A])); r1705 = rbody(1705)
r5 = re.findall(r'\+\d+\.\d+', r1705.split('Envelopes')[0])
print('  unit values %s; register 1705 point values %s; equal: %s; all positive: %s; Z list %s'
      % (u5, r5, [x.replace('−', '-') for x in u5] == [x.replace('−', '-') for x in r5], all(x.startswith('+') for x in u5), re.findall(r'Z = ([\d, ]+)\)', ' '.join(U[_L('**Correlation widens every contested step.** At the five elements where the') - A:_L('widens.*') - A]))))

# ---------------------------------------------------------------- 6. the eleven elements L9772–L9773 against register 1706
hr('6  RELATIVISTIC TWIN — the eleven elements')
u6 = re.search(r'eleven elements — ([A-Z][a-z]?(?:, [A-Z][a-z]?)+)', UT).group(1).split(', ')
r1706 = rbody(1706); r6 = re.search(r'Λ_chain at ([A-Z][a-z]?(?:, [A-Z][a-z]?)+)', r1706).group(1).split(', ')
print('  unit: %s (%d); register 1706: %s (%d); same set and order: %s; Ag, Hg named "silver and mercury": %s'
      % (' '.join(u6), len(u6), ' '.join(r6), len(r6), u6 == r6, 'Ag' in u6 and 'Hg' in u6))

# ---------------------------------------------------------------- 7. Z = 109–120 L9777–L9779 against register 1712 — the margin arithmetic
hr('7  TWELVE UNWITNESSED ROWS — count and the spin-orbit clearance arithmetic')
print('  rows: 109–112 6d (%d) + 113–118 7p (%d) + 119–120 8s (%d) = %d (twelve printed)' % (4, 6, 2, 12))
lo, hi, so = D('0.058'), D('0.264'), D('0.083')
print('  margins 0.058–0.264 Ha; worst-case spin-orbit narrowing 0.083 Ha "clearing every one" (unit) / "cleared by all" (1712):')
print('  reading A (every margin exceeds the worst-case narrowing): min margin − 0.083 = %s Ha -> %s; max margin − 0.083 = %s Ha' % (q(lo - so, '0.001'), 'FAILS' if lo - so < 0 else 'holds', q(hi - so, '0.001')))
print('  reading B (the narrowing is per row and 0.083 is the largest, at a row whose own margin exceeds it): not decidable from either text — the per-row values are not printed;')
print('  budget item, not a negative: the Löwdin delivery (REQUEST-LOWDIN item 10) carries the per-row narrowing. Under reading A the sentence is false at the 0.058 row.')

# ---------------------------------------------------------------- 8. the one entered constant L9737
hr('8  c = 137.035999 — sites and precision')
print('  sites:', fmt(sites(r'137\.035999')), '; longer forms (137.0359990…):', fmt(sites(r'137\.0359990\d')))
print('  CODATA 2018 α⁻¹ = 137.035999084 (reference value, not measured from a file) quantised to 6 dp = %s -> the printed constant is that value at 6 dp' % q(D('137.035999084'), '0.000001'))

# ---------------------------------------------------------------- 9. the f-opening node floor L9786–L9788 (16z-05's universal, re-asserted)
hr('9  "At any f opening the node count p = n−ℓ−1 hits its floor" — recomputed at both f openings')
for sh in ('4f', '5f'):
    n, l = nl(sh); print('  %s opens at Z = %d (%s): p = %d − %d − 1 = %d' % (sh, opening[sh], SYM[opening[sh] - 1], n, l, n - l - 1))
print('  the universal holds at 4f and fails at 5f (p = 1): a second site of 16z-05 (READ-ch16z A), now in Chapter 35 at L9786–L9788')

# ---------------------------------------------------------------- 10. docket 27 — long-line recurrence
hr('10  DOCKET 27 — unit lines ≥ 60 chars recurring anywhere in the six volumes (whitespace-normalised)')
norm = lambda s: re.sub(r'\s+', ' ', s.strip())
ALL = {v: [norm(l) for l in t] for v, t in VOL.items()}
rec = []
for i, l in enumerate(U, A):
    n = norm(l)
    if len(n) < 60: continue
    hits = sum(1 for v, t in ALL.items() for j, x in enumerate(t, 1) if x == n and not (v == 'main' and j == i))
    if hits: rec.append((i, hits))
print('  %d long lines tested; recurring: %s' % (sum(1 for l in U if len(norm(l)) >= 60), rec or 'none'))

# ---------------------------------------------------------------- 11. numerals of the unit, cross-site at the printed precision
hr('11  NUMERALS — sites across the six volumes')
for pat in (r'107 of 107', r'104 of 106', r'106 transitions', r'below Z = 121|Z = 121', r'\b0\.083\b', r'\b0\.058\b', r'\b0\.264\b', r'\+1\.33', r'\+2\.16', r'\b65 elements\b',
            r'\beleven elements\b', r'Mn, Zn, Ag, Cd', r'109–120', r'\b1969\b', r'two coexisting solutions', r'\bunwitnessed\b'):
    print('  %-28s %s' % (pat, fmt(sites(pat))))
print('\nEND r2-ch17a')
