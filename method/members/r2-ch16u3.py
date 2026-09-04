#!/usr/bin/env python3
# r2-ch16u2.py — chat 153 — SUCCESSOR to r2-ch16u.py, re-anchored. Identical measurements; one address moves.
# r2-ch16u scanned `range(9727, 9735)` — a FIXED WINDOW over §35.1 — for its Chapter 33 / Chapter 27 sites.
# r3-wl2's +8 shift at main L9608 moved §35.1, so the window now covers the wrong lines and the seated
# instrument reports the sibling site from text that is no longer there. The window is now body_range(MAIN,
# '35.1'), which this instrument already defines and uses elsewhere — heading to the next heading of any
# rank, body occurrence. A window that follows its section cannot be moved by an insertion above it.
# r2-ch16u is seated and is never edited in place (chat 68).
# PROVED by tools/proveanchor.py: reproduces r2-ch16u.out byte-exact on the pre-shift bundles (G0c).
# r2-ch16u -- COMPUTABLE batch for the chat-125 section read: main L9393-L9493
# (# PART VII divider, ch.33 head, 33.1-33.5).  Reads MEMBERS only, never a BUILDnnn bundle path.
# Deterministic; prints no wall-clock time.
# r2-ch16u3.py — R3 (chat 153-R) — SUCCESSOR to r2-ch16u2.py, re-anchored by tools/reanchor.py: every main-volume line the
# predecessor pinned as a literal is resolved by the text of the line it pointed at in the bundle its golden was
# banked against (14 anchors); nothing else changes. r2-ch16u2.py is seated and never edited in place (chat 68).
# PROVED by tools/proveanchor.py when the line below says so; until then this file is a draft.
# PROVEANCHOR: 94+198 — reproduces r2-ch16u2.out byte-exact on those bundles (G0c)

# --- re-anchoring helper (tools/reanchor.py): a main-volume line found by its own text, never by a number ---
def _L(t, d=0):
    import os as _o
    global _LM
    try: _LM
    except NameError: _LM = open(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)), 'The_Method_1_6-2.md'), encoding='utf-8').read().split('\n')
    h = [i for i, l in enumerate(_LM, 1) if l == t]
    assert len(h) == 1, ('re-anchor: line text is not unique or is absent', t[:60], h)
    return h[0] + d
import os, re, sys, importlib.util
from decimal import Decimal, ROUND_HALF_UP

H = '/home/claude/members'
spec = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
from r2lib import heading_line, section_span, has_token, enclosing, L8_at

def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
def hr(t): print('\n' + '=' * 96 + '\n' + t + '\n' + '=' * 96)
def norm(s): return re.sub(r'\s+', ' ', s.strip())

# owed to r2lib (DEFERRED): body_range, carried with provenance from r2-ch16m (chat 121).
def body_range(M, sec):
    s = heading_line(M, sec)
    if s is None: return None
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1].strip()): return (s, i)
    return (s, len(M) + 1)

# owed to r2lib (DEFERRED): numsites, comma-aware, from r2-ch16p (chat 122).
def numsites(M, n):
    forms = {str(n), f'{n:,}'}
    pat = r'(?<![\d.,])' + '(?:' + '|'.join(re.escape(f) for f in forms) + r')(?!\d)(?!,\d)(?!\.\d)'
    return [i + 1 for i in range(len(M)) if re.search(pat, M[i])]

def q(x, places='0.01'):
    """Decimal.quantize HALF_UP -- never Python's round(), which is binary and wrong on .5."""
    return Decimal(str(x)).quantize(Decimal(places), rounding=ROUND_HALF_UP)

MAIN = rd('The_Method_1_6-2.md')
REG  = rd('The_Method_1_6___The_Register-2.md')
MC   = rd('The_Method_1_6___Mathematical_Compendium-2.md')
PC   = rd('The_Method_1_6___The_Physics_Compendium-2.md')
IOI  = rd('The_Method_1_6___The_Index_of_Indices-2.md')
SC   = rd('The_Method_1_6___Spectra_Compendium-2.md')
VOL  = [('main', MAIN), ('reg', REG), ('mc', MC), ('pc', PC), ('ioi', IOI), ('sc', SC)]
U0, U1 = _L(' **That is where the word belongs.** Not on *V* = 4ν/3, which may sit in a 1922 German volume nobody cites. Not on E(X), which is a closure defect and says so. **On the shape of the thing** — a work built to be checked, that checked itself, failed twice, said so, and repaired both.', 2), _L('how the method itself did the work.*', 1)                                    # unit, bounded by body_range

# ---------------------------------------------------------------- 1. unit extent
hr('1. UNIT EXTENT, resolved under BOTH resolvers')
print(f'main member lines: {len(MAIN)}')
for sec in ('33.1', '33.2', '33.3', '33.4', '33.5'):
    br, ss = body_range(MAIN, sec), section_span(MAIN, sec)
    print(f'  §{sec:6s} body_range={br}  section_span={ss}  {"COINCIDE" if br == ss else "DIFFER"}')
print(f'  unit L{U0}-L{U1} = {U1 - U0 + 1} lines; "## 34." body opens at '
      f'{[i + 1 for i, s in enumerate(MAIN) if s.startswith("## 34.")]}')
print(f'  "# PART VII" at {[i + 1 for i, s in enumerate(MAIN) if s.startswith("# PART VII")]} '
      f'(contents + body)')

# ---------------------------------------------------------------- 2. six languages, DATA rows
hr('2. "Six languages" (L9412) against its own DATA rows')
rows = [i for i in range(_L('| language | its question |'), _L('| **statistics** | are the cells drawn from a distribution? |', 1)) if MAIN[i - 1].strip().startswith('|')]
data = [i for i in rows if not re.match(r'^\|[\s\-|:]+\|$', MAIN[i - 1].strip())][1:]
print(f'  table lines L9414-L9421: {len(rows)}  header+separator: 2  DATA rows: {len(data)}')
unit_langs = []
for i in data:
    cell = MAIN[i - 1].split('|')[1]
    unit_langs.append(re.sub(r'\*', '', cell).strip())
print(f'  count word "Six" vs DATA rows {len(data)}: {"EXACT" if len(data) == 6 else "MISMATCH"}')
print(f'  the unit roster: {unit_langs}')

# ---------------------------------------------------------------- 3. the roster elsewhere
hr('3. THE SAME ROSTER ELSEWHERE -- ch.20 (cited at L9406) and ch.1')
# FAULT 1, self-caught: the roster wraps onto L5574, so a one-line read returned three
# names of six.  Join the sentence across its lines before splitting it.
print('  §20.2 L5573-L5574 verbatim (whitespace-normalised join):')
j20 = norm(MAIN[_L('### 20.2 The languages this book uses', 1)] + ' ' + MAIN[_L(' **Six agree on Λ at 976 cells, and ten of their combinations hold** — order, geometry, arithmetic,')])
print('   ', j20[:200])
c20 = [t.strip(' .*') for t in re.split(r',| and ', j20.split('hold** — ')[-1].split('. That agreement')[0])
       if t.strip(' .*')]
print(f'  §20.2 roster as printed: {c20}  ({len(c20)} names)')
print(f'  §20.2 says "Six": {"yes" if "Six" in MAIN[_L('### 20.2 The languages this book uses', 1)] else "no"};  '
      f'names in common with the unit roster: '
      f'{sorted(set(x.lower() for x in unit_langs) & set(x.lower().rstrip(".") for x in c20))}')
for lab, a, b in (('ch.1 mechanism table', 400, 406), ('ch.1 closure-operator table', 455, 460)):
    rws = [i for i in range(a, b + 1) if MAIN[i - 1].strip().startswith('|')]
    dta = [i for i in rws if not re.match(r'^\|[\s\-|:]+\|$', MAIN[i - 1].strip())]
    if not rws:            # space-aligned table, not pipe-delimited
        dta = [i for i in range(a + 1, b + 1) if MAIN[i - 1].strip()]
        names = [norm(MAIN[i - 1]).split('  ')[0] for i in dta]
    else:
        names = [re.sub(r'\*', '', MAIN[i - 1].split('|')[1]).strip() for i in dta[1:]]
        dta = dta[1:]
    print(f'  {lab}: {len(dta)} DATA rows -> {names}')
print('  L439 (ch.1): ' + norm(MAIN[438])[:110])
print('  L453 (ch.1): ' + norm(MAIN[452]))
print('  L5564 (§20.1 on ch.1): ' + norm(MAIN[_L('    **The language a question is posed in bounds whether it can close, and at what cost.**', 1)])[:110])

# ---------------------------------------------------------------- 4. the ioi's operative roster
hr('4. WHICH ROSTER THE INDEX OF INDICES ACTUALLY USES')
LANG = ['order', 'analysis', 'algebra', 'geometry', 'information', 'statistics',
        'arithmetic', 'calculus', 'logic']
for w in LANG:
    n = sum(1 for s in IOI if re.search(r'\b' + w + r'\b', s, re.I))
    m = sum(1 for s in MC if re.search(r'\b' + w + r'\b', s, re.I))
    print(f'  {w:12s} ioi {n:3d} sites   mc {m:3d} sites'
          f'   {"<- unit roster" if w in [x.lower() for x in unit_langs] else ""}')

# ---------------------------------------------------------------- 5. Lambda at 976
hr('5. "Λ at 976 cells" (L9423) RECOMPUTED on the rebuilt lattice')
cells = L8_at((3, 3, 1, 3, 1))
print(f'  L8_at((3,3,1,3,1)) -> {len(cells)} cells; the book prints 976: '
      f'{"EXACT" if len(cells) == 976 else "MISMATCH"}')
print(f'  976 sites in the unit: {[i for i in numsites(MAIN, 976) if U0 <= i <= U1]}')
print(f'  976 sites in six volumes: ' + ', '.join(f'{k} {len(numsites(M, 976))}' for k, M in VOL))

# ---------------------------------------------------------------- 6. fifty sections of ch.12
hr('6. "Chapter 12 spends fifty sections on it" (L9424)')
c12 = [i + 1 for i, s in enumerate(MAIN) if s.startswith('## 12.')]
nxt = [i + 1 for i, s in enumerate(MAIN) if s.startswith('## ') and i + 1 > c12[-1]][0]
h12 = [(i + 1, s) for i, s in enumerate(MAIN) if re.match(r'^#{2,6} 12\.\d', s)]
inside = [x for x in h12 if c12[-1] < x[0] < nxt]
outside = [x for x in h12 if not (c12[-1] < x[0] < nxt)]
print(f'  "## 12." occurrences {c12} (contents, body); body span {c12[-1]}-{nxt - 1}')
print(f'  headings numbered 12.x: {len(h12)} total, {len(inside)} inside the body span, '
      f'{len(outside)} outside')
for a, b in outside: print(f'    OUTSIDE: L{a}  {b[:70]}')
print(f'  count word "fifty" vs sections inside the span: '
      f'{"EXACT at 50" if len(inside) == 50 else "MISMATCH"}')
print(f'  vs sections numbered 12.x anywhere: {len(h12)} '
      f'({"off by one" if len(h12) == 51 else ""})')
print('  L5553 (§20 head) prints the same count word about a different object: '
      + norm(MAIN[_L('## 20. The languages, and what each one can close', 1)])[:95])

# ---------------------------------------------------------------- 7. nine of eleven
hr('7. "Across the indexes of §36, nine of eleven ... are expectation values" (L9451-L9453)')
for k, M in VOL:
    for i, s in enumerate(M):
        if re.search(r'expectation value', s, re.I): print(f'  {k} L{i + 1}: ' + norm(s)[:150])
c36 = [i + 1 for i, s in enumerate(MAIN) if s.startswith('## 36.')]
e36 = [i + 1 for i, s in enumerate(MAIN) if s.startswith('## ') and i + 1 > c36[-1]][0]
span = MAIN[c36[-1] - 1:e36 - 1]
print(f'\n  §36 body span L{c36[-1]}-L{e36 - 1} ({e36 - c36[-1]} lines): {norm(MAIN[c36[-1] - 1])}')
for tok in ('Λ_', 'expectation', 'eleven', 'index', 'closure'):
    print(f'    "{tok}" inside §36: {sum(1 for s in span if tok in s)} sites')
print(f'  registers stating the population: '
      f'1327 (reg L4981) "eleven closed indexes"; 1347 (reg L5061) "TWELVE CLOSED INDEXES"')
print('  reg L5061: ' + norm(REG[_L('  the periodic table               36    the count of shells is not a coordinate of the table')])[:150])
print(f'  ioi "## Λ" headings: {sum(1 for s in IOI if re.match(r"^##\s+Λ", s))} '
      f'({len(set(re.match(r"^##\s+(Λ\S*)", s).group(1) for s in IOI if re.match(r"^##\s+Λ", s)))} distinct)')

# ---------------------------------------------------------------- 8. Chapter 27's terms
hr('8. "stated in Chapter 27\'s terms" (L9449) -- the cited criterion read at its target')
c27 = [i + 1 for i, s in enumerate(MAIN) if s.startswith('## 27.')]
e27 = [i + 1 for i, s in enumerate(MAIN) if s.startswith('## ') and i + 1 > c27[-1]][0]
sp27 = MAIN[c27[-1] - 1:e27 - 1]
print(f'  §27 body span L{c27[-1]}-L{e27 - 1} ({e27 - c27[-1]} lines): {norm(MAIN[c27[-1] - 1])}')
for tok in ('enumerable', 'operator', 'index closes', 'cannot supply'):
    n = sum(1 for s in sp27 if re.search(tok, s, re.I))
    print(f'    "{tok}" inside Chapter 27: {n} sites')
print('  where the sentence DOES live:')
for k, M in VOL:
    for i, s in enumerate(M):
        if re.search(r'cannot supply is exactly what requires', s, re.I) or \
           re.search(r'what it cannot supply is exactly', s, re.I):
            print(f'    {k} L{i + 1}: ' + norm(s)[:120])
print('  §35.1 (the sibling site, repaired):')
_b351 = body_range(MAIN, '35.1')
for i in range(_b351[0], _b351[1]):
    if 'Chapter 33' in MAIN[i - 1] or 'Chapter 27' in MAIN[i - 1]:
        print(f'    main L{i}: ' + norm(MAIN[i - 1])[:130])
print('  register 1755 (reg L6491) diagnosis, first 300 chars:')
print('    ' + norm(REG[_L('| | order 1 | order 5 |', 1)])[:300])

# ---------------------------------------------------------------- 9. the domain protocol
hr('9. "the fourth question of the domain protocol" (L9486) read at its target')
print('  register 1336 (reg L5017), the protocol entire:')
print('    ' + norm(REG[5016])[:420])
qs = norm(REG[5016]).split('Four questions before any fit:')[1].split('.*')[0].split('*')[0]
parts = [p.strip() for p in qs.split('·')]
for n, p in enumerate(parts, 1): print(f'    question {n}: {p}')
print(f'  the unit calls "Never fit across a language boundary" the FOURTH question; '
      f'register 1336\'s fourth is: {parts[3] if len(parts) > 3 else "N/A"}')
for k, M in VOL:
    for i, s in enumerate(M):
        if re.search(r'language boundary', s, re.I): print(f'  {k} L{i + 1}: ' + norm(s)[:130])

# ---------------------------------------------------------------- 10. the singleton criterion
hr('10. THE SINGLETON CRITERION (L9463-L9465) against the record')
for k, M in VOL:
    for i, s in enumerate(M):
        if re.search(r'output class is a singleton|singleton-output', s, re.I):
            print(f'  {k} L{i + 1}: ' + norm(s)[:170])
print('  register 1300 (reg L4873) entire, first 400 chars:')
print('    ' + norm(REG[_L(" **Λ's seven constraints are all safe by inspection**: each reads one coordinate, or a minimum of two. **None sums.** That is why Λ is closed and the periodic table is not — and it is checkable without touching a cell.", 1)])[:400])

# ---------------------------------------------------------------- 11. n*, delta, Lambda_ryd
hr('11. THE §33.4 CLAIMS AGAINST THE RECORD')
for pat, lab in ((r'Λ_var', 'Λ_var'), (r'Λ_ryd', 'Λ_ryd'), (r'δ₂|delta_2', 'δ₂'),
                 (r'non-penetrating', 'non-penetrating')):
    print(f'  --- {lab} ---')
    for k, M in VOL:
        hits = [i + 1 for i, s in enumerate(M) if re.search(pat, s)]
        print(f'    {k}: {len(hits)} sites {hits[:8]}')
print('  ioi §Λ_var body (L1596-L1613):')
for i in range(_L(' The same computation on other indices:', 1), _L('  the periodic table                                      90      36     no', 1)):
    if IOI[i - 1].strip(): print(f'    ioi L{i}: ' + norm(IOI[i - 1])[:120])

# ---------------------------------------------------------------- 12. Loewdin 1969
hr('12. "In 1969 Per-Olov Löwdin set a challenge" (L9489) -- date and bibliography')
for i, s in enumerate(MAIN):
    if '1969' in s: print(f'  main L{i + 1}: ' + norm(s)[:135])
print('  References body occurrence:')
refs = [i + 1 for i, s in enumerate(MAIN) if s.startswith('## References')]
print(f'    "## References" occurrences {refs}; body = {refs[-1]}')
for i in range(refs[-1], len(MAIN) + 1):
    if re.search(r'Löwdin', MAIN[i - 1]): print(f'    main L{i}: ' + norm(MAIN[i - 1])[:150])
