# r2-ch27a.py — the unit main `## Appendix G` (LAST hit) to `## References` (LAST hit): the COMPUTABLE claims (chat 140).
# The span holds TWO units: Appendix G (to `# END MATTER`) and the Index (`## Index` to `## References`). Both read as DATA.
# Reads MEMBERS by name (never a bundle path); imports r2lib by path; deterministic. Every DATA-row set is fixed and printed
# first; every count word is measured against it; every figure is re-taken on the tower where it is tower-computable and
# otherwise located at its source (Transitions.md member, the Register, the compendia) — conventions named before scoring.
# r2-ch27a4.py — R3 (chat 153-R) — SUCCESSOR to r2-ch27a.py, re-anchored by tools/reanchor.py: every main-volume line the
# predecessor pinned as a literal is resolved by the text of the line it pointed at in the bundle its golden was
# banked against (3 anchors); nothing else changes. r2-ch27a.py is seated and never edited in place (chat 68).
# PROVED by tools/proveanchor.py when the line below says so; until then this file is a draft.
# PROVEANCHOR: 90+184 — reproduces r2-ch27a.out byte-exact on those bundles (G0c)

# --- re-anchoring helper (tools/reanchor.py): a main-volume line found by its own text, never by a number ---
def _L(t, d=0):
    import os as _o
    global _LM
    try: _LM
    except NameError: _LM = open(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)), 'The_Method_1_6-2.md'), encoding='utf-8').read().split('\n')
    h = [i for i, l in enumerate(_LM, 1) if l == t]
    assert len(h) == 1, ('re-anchor: line text is not unique or is absent', t[:60], h)
    return h[0] + d
import os, re, importlib.util
from collections import Counter, defaultdict
H = os.path.dirname(os.path.abspath(__file__))
def load(name):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), os.path.join(H, name + '.py')); mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod); return mod
L = load('r2lib'); heading_line, section_span, has_token = L.heading_line, L.section_span, L.has_token
M = L.read_member('The_Method_1_6-2.md').split('\n')
R = L.read_member('The_Method_1_6___The_Register-2.md').split('\n')
MC = L.read_member('The_Method_1_6___Mathematical_Compendium-2.md').split('\n')
PC = L.read_member('The_Method_1_6___The_Physics_Compendium-2.md').split('\n')
IOI = L.read_member('The_Method_1_6___The_Index_of_Indices-2.md').split('\n')
SC = L.read_member('The_Method_1_6___Spectra_Compendium-2.md').split('\n')
T = L.read_member('Transitions.md').split('\n')
def hr(t): print('\n== ' + t)
def rbody(n):   # copied verbatim from r2-ch26b.py (there from r2-ch25a.py … r2-ch17b.py; owed to r2lib, DEFERRED): first non-blank line after '### n'
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())
def body_range(M, sec):   # copied verbatim from r2-ch26b.py (there from r2-ch25a.py … r2-ch16z.py; owed to r2lib, DEFERRED): heading to next heading of any rank, body occurrence
    s = heading_line(M, sec)
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1]): return (s, i)
    return (s, len(M) + 1)
def lettered(M, tag):   # copied verbatim from r2-ch26b.py (there from r2-ch25a.py … r2-ch17c.py; owed to r2lib, DEFERRED): lettered heading, exact token, hits in order; body = LAST
    hits = [i for i, l in enumerate(M, 1) if re.match(r'^#{2,4}\s*' + re.escape(tag) + r'(?!\.\d)(?!\d)\b', l)]
    return hits
def cnt(lines, pat, flags=re.I): return sum(len(re.findall(pat, l, flags)) for l in lines)
def join(lines): return re.sub(r'\s+', ' ', re.sub(r'[*_`>]', '', ' '.join(lines)))
def rentry(n):
    i = next((i for i, l in enumerate(R) if re.match(r'^#{1,4}\s*%d\s*$' % n, l)), None)
    if i is None: return None
    j = next((k for k in range(i + 1, len(R)) if re.match(r'^#{1,4}\s*\d+\s*$', R[k])), len(R)); return (i + 1, j, R[i:j])
def numerals(s): return re.findall(r'(?<![\d.])\d{1,3}(?:,\d{3})+(?![\d])|(?<![\d.,])\d+(?:\.\d+)?(?![\d,])', s)

hr('§0 the span, measured by scan: `## Appendix G` (LAST hit) to `## References` (LAST hit); the units inside it')
G = [i + 1 for i, l in enumerate(M) if re.match(r'^## Appendix G\b', l)]; RF = [i + 1 for i, l in enumerate(M) if re.match(r'^#{1,3} References\b', l)]
g, rf = G[-1], RF[-1]; em = [i + 1 for i, l in enumerate(M) if l.startswith('# END MATTER')]; ix = [i + 1 for i, l in enumerate(M) if re.match(r'^## Index\b', l)]
print('  `## Appendix G` hits %s (LAST %d); `References` heading hits %s (LAST %d); span %d lines' % (G, g, RF, rf, rf - g))
print('  `# END MATTER` %s; `## Index` hits %s (LAST %d): Appendix G = L%d–L%d (%d lines); Index = L%d–L%d (%d lines); no `### G.n` heading in the span: %s'
      % (em, ix, ix[-1], g, em[-1] - 1, em[-1] - g, ix[-1], rf - 1, rf - ix[-1], [i + 1 for i in range(g - 1, rf - 1) if re.match(r'^#{2,4}\s*G\.\d', M[i])] or 'NONE'))
U = M[g - 1:em[-1] - 1]; X = M[ix[-1] - 1:rf - 1]; UJ, XJ = join(U), join(X)
code = False; drows = []
for i in range(g - 1, em[-1] - 1):
    l = M[i]
    if l.startswith('```'): code = not code; continue
    if not code and l.startswith('|'): drows.append((i + 1, l))
hdr = [r for r in drows if re.match(r'^\|\s*§\s*\|', r[1])]; sep = [r for r in drows if re.match(r'^\|\s*-+\s*\|', r[1])]; DATA = [r for r in drows if r not in hdr and r not in sep]
print('  G `|` rows %d (a `|` at line start outside a code line; code fences in G: %d): header %d, separator %d, DATA rows %d — the DATA-row set is fixed first' % (len(drows), 0, len(hdr), len(sep), len(DATA)))
rows = []   # fault 1 (self-caught): a naive split on `|` broke L11378 at its `\\|` escape into 5 columns — split on UNESCAPED `|` only
def cells(l): return [x.strip() for x in re.split(r'(?<!\\)\|', l.strip().strip('|'))]
for ln, l in DATA:
    c = cells(l); assert len(c) == 3, (ln, len(c)); rows.append((ln, c[0], c[1], c[2]))
print('  columns per DATA row: %s (convention: split on unescaped `|`; the `\\|` escapes at L11378 are text — naive-split column counts %s)' % (sorted({len(cells(l)) for _, l in DATA}), sorted({len(l.strip().strip('|').split('|')) for _, l in DATA})))

hr('§1 Appendix G count words against the DATA-row set: thirty sections / thirty locators / thirty-four citations / thirty-seven objects / forty-seven / eight')
secs = [r[1] for r in rows]; print('  DATA rows %d; § labels %s; distinct %d; in ascending numeric order: %s' % (len(rows), secs, len(set(secs)),
      secs == sorted(secs, key=lambda s: (int(s.split('.')[0]), int(re.sub(r'[a-z]', '', s.split('.')[1])), s))))
print('  "The thirty sections" L11364 / "Thirty sections, thirty resolved locators" L11405: 30 == %d rows: %s' % (len(rows), len(rows) == 30))
# Transitions source: numbered sections
tsec = [(i + 1, m.group(1)) for i, l in enumerate(T) for m in [re.match(r'^#{1,4}\s*(\d+\.\d+[a-z]?)\s', l)] if m]
print('  Transitions.md member: %d lines; numbered `N.n[x]` headings %d (Part 0 included: %s; appendix `A1…` headings excluded: %d)' % (len(T), len(tsec), [s for _, s in tsec if s.startswith('0.')], cnt(T, r'^#{1,4}\s*A\d+\s*$', 0)))
tset = {s for _, s in tsec}; miss = [s for s in secs if s not in tset]
print('  1770 "seventy-seven sections": 77 == %d: %s (convention: a `### N.n` or `### N.nx` heading; if 0.1–0.4 excluded: %d)' % (len(tsec), len(tsec) == 77, len([s for _, s in tsec if not s.startswith('0.')])))
print('  every G § exists as a Transitions heading: %s (missing %s); "forty-seven not used" = %d − %d = %d: %s' % (not miss, miss or 'none', len(tsec), len(rows), len(tsec) - len(rows), len(tsec) - len(rows) == 47))
# Objects column
objs = []
for ln, s, st, ob in rows:
    hs = re.findall(r'`([A-Z]\.[A-Za-z0-9]+)`', ob); mcs = re.findall(r'Mathematical Compendium, (the [a-z ]+)', ob); objs.append((s, hs, mcs, ob))
handles = [h for _, hs, _, _ in objs for h in hs]; mcents = [m for _, _, ms, _ in objs for m in ms]
print('  objects column: backticked handles %d (distinct %d), "Mathematical Compendium, the …" names %d, Chapter pointers %d, Register pointers %d' % (len(handles), len(set(handles)), len(mcents), cnt([o for *_, o in objs], r'Chapter \d+'), len(re.findall(r'\d{3,4}', ' '.join(o for *_, o in objs if 'Register' in o)))))
print('  "thirty-seven objects" L11363 vs handles + MC names = %d: %s (convention: one object per handle or named entry; the Register\'s "thirty-seven" is 1769\'s attribution count at R 1218–1230, not this column — see §4)' % (len(handles) + len(mcents), len(handles) + len(mcents) == 37))

hr('§2 the tower-computable figures of the G rows, re-taken on the rebuilt tower (r2lib.load_tower)')
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()): T8 = L.load_tower()   # fault 2 (self-caught): load_tower returns the tower-2 MODULE (r2-ch25a's usage), not a dict of levels
n8, n9, n12 = len(T8.L8()), len(T8.L9()), len(T8.L12())
print('  tower-2 rebuilt: Λ₈ %d, Λ₉ %d, Λ₁₂ %d' % (n8, n9, n12))
print('  row 2.4 "Λ₁₂ falls 70,905 → 22,275": Λ₁₂ = %d == 70,905: %s (22,275 and E 35,570 are the exact-triangle cut — not rebuilt here, a budget; located at source in §3)' % (n12, n12 == 70905))
print('  row 4.1 "1,169 of 1,654 cells": Λ₉ = %d == 1,654: %s (composable 1,169: located at source in §3; the composability relation is Chapter 19\'s — INFERRED, not rebuilt here)' % (n9, n9 == _L(" table's thirty-six, the measured nuclide chart's nine, and these four are one phenomenon counted in")))
print('  row 2.2 "tree of nine nodes and eight edges": Λ₉ cells carry %d coordinates == 9: %s; a tree on 9 nodes has 8 edges (arithmetic); the constraint graph itself is Transitions §2.2\'s (located, not rebuilt)' % (len(T8.L9()[0]), len(T8.L9()[0]) == 9))

hr('§3 every numeral of every G row located in its Transitions section (raw and comma-stripped) and in the reader volumes; misses printed')
tidx = {s: ln for ln, s in tsec}
def tsec_body(s):
    a = tidx[s]; b = next((ln for ln, _ in tsec if ln > a), len(T) + 1)
    for i in range(a, len(T)):
        if re.match(r'^#{1,2} ', T[i]) and i + 1 > a: b = min(b, i + 1); break
    return T[a - 1:b - 1]
VOL = {'main': M, 'reg': R, 'mc': MC, 'pc': PC, 'ioi': IOI, 'sc': SC}
tot = 0; missT = []
for ln, s, st, ob in rows:
    nums = [n for n in numerals(st) if not re.fullmatch(r'\d', n) or n in ('0',)]
    nums = [n for n in nums if n not in ('0',)]
    body = tsec_body(s); bj = join(body)
    for n in nums:
        tot += 1; forms = {n, n.replace(',', '')}
        inT = any(f in bj for f in forms)
        sites = {v: cnt(VOL[v], r'(?<![\d.,])' + re.escape(n) + r'(?!\d)(?!,\d{3})', 0) for v in VOL}
        if not inT: missT.append((ln, s, n, sites))
print('  numerals tested %d over %d rows (convention: digit-bounded both sides, a trailing non-thousands comma admitted — fault 3 self-caught: `(?![\\d,])` dropped `816,` at L11395 — bare single digits excluded); found in the Transitions section: %d; NOT found: %d' % (tot, len(rows), tot - len(missT), len(missT)))
for ln, s, n, sites in missT: print('    L%d §%s %s — Transitions section lacks it; sites elsewhere %s' % (ln, s, n, {k: v for k, v in sites.items() if v}))
for n in ('22,275', '35,570', '1,169', '27,027', '6,658', '2.51', '2,370', '816', '144'):
    print('  %s: Transitions %d lines; main %d, reg %d, mc %d, pc %d, ioi %d, sc %d — main sites %s' % (n, cnt(T, r'(?<![\d.,])' + re.escape(n) + r'(?!\d)(?!,\d{3})', 0), *[cnt(VOL[v], r'(?<![\d.,])' + re.escape(n) + r'(?!\d)(?!,\d{3})', 0) for v in ('main', 'reg', 'mc', 'pc', 'ioi', 'sc')],
          [i + 1 for i, l in enumerate(M) if re.search(r'(?<![\d.,])' + re.escape(n) + r'(?!\d)(?!,\d{3})', l)][:8]))

hr('§4 the citations: "thirty-four re-sourced inward, two main + thirty-two MC" (1770); "eight in the Register" (L11369, 1770); "thirty-seven objects" (1769); the handles')
def sites(lines, pat, flags=0): return [i + 1 for i, l in enumerate(lines) if re.search(pat, l, flags)]
gm = [i for i in sites(M, r'Appendix G\b') if i not in range(g, em[-1])]
print('  `Appendix G` in main outside the appendix: %d at %s (the contents-list hit L%d is a listing, not a citation): citations %d == 2: %s' % (len(gm), gm, G[0], len([i for i in gm if i != G[0]]), len([i for i in gm if i != G[0]]) == 2))
for i in gm: print('    L%d %s' % (i, M[i - 1][:150]))
for tag, V in (('mc', MC), ('pc', PC), ('ioi', IOI), ('sc', SC), ('reg', R)):
    a = cnt(V, r'Appendix G\b', 0); b = cnt(V, r'\bTransitions\b', 0)
    print('  %s: `Appendix G` %d occurrences on %d lines; `Transitions` (word-bounded, case-sensitive) %d on %d lines; `Transitions` case-insensitive %d' % (tag, a, len(sites(V, r'Appendix G\b')), b, len(sites(V, r'\bTransitions\b')), cnt(V, r'\btransitions\b')))
rl = sites(R, r'\bTransitions\b'); ents = sorted({max(k for k in [j for j, l in enumerate(R) if re.match(r'^#{1,4}\s*\d+\s*$', l)] if k < i - 1) for i in rl})
print('  Register lines naming *Transitions*: %s in entries %s — "eight citations … left exactly as written" L11369: entries %d, lines %d, occurrences %d' % (rl, [int(re.sub(r'\D', '', R[k])) for k in ents], len(ents), len(rl), cnt(R, r'\bTransitions\b', 0)))
print('  Register 1218–1230 (the attribution pass 1769 names): entries carrying *Transitions* %s; entries carrying "T §" %s; their heads:' % ([n for n in range(1218, 1231) if rentry(n) and cnt(rentry(n)[2], r'\bTransitions\b', 0)], [n for n in range(1218, 1231) if rentry(n) and cnt(rentry(n)[2], r'(?<![A-Za-z])T\s*§', 0)]))
for n in range(1218, 1231): print('    %d %s' % (n, (rbody(n) or 'NO HEADING')[:120]))
print('  "thirty-seven objects" (L11363, 1769): the reader volumes print no DATA-row set of 37 — G\'s objects column 32, MC entries citing App. G 30, MC `App. G` cites 32, main 2, Register 8 (T §): unreproduced from the page, record-carried on 1769')
mcg = sites(MC, r'Appendix G\b'); print('  MC `Appendix G` lines %s' % mcg[:40])
# fault 4 (self-caught): the re-sourced citations are written `T 1.3 (App. G)` in the MC and `T §8.2 (Appendix G)` in the main volume, `T §n.n` in the Register — not `Appendix G`
mcap = sites(MC, r'App\.? G\b'); print('  MC `App. G` lines %d == 32 (1770 "thirty-two in the Mathematical Compendium"): %s; occurrences %d; distinct T §s cited beside them: %s' % (len(mcap), len(mcap) == 32, cnt(MC, r'App\.? G\b', 0), sorted({s for i in mcap for s in re.findall(r'\bT\s*§?\s*(\d+\.\d+[a-z]?)', MC[i - 1])}, key=lambda s: (int(s.split('.')[0]), s))))
tsm = sorted({s for i in mcap for s in re.findall(r'\bT\s*§?\s*(\d+\.\d+[a-z]?)', MC[i - 1])}); print('  those T §s all among the 30 G rows: %s (not in G: %s); G rows never cited from the MC: %s' % (set(tsm) <= set(secs), sorted(set(tsm) - set(secs)), sorted(set(secs) - set(tsm), key=lambda s: (int(s.split('.')[0]), s))))
mch = [max(k for k in range(i) if re.match(r'^#{1,4} ', MC[k])) + 1 for i in mcap]; print('  distinct MC entries (enclosing heading) carrying an `App. G` cite: %d; MC `T §` outside `App. G` lines: %d %s' % (len(set(mch)), len([i for i in sites(MC, r'\bT §') if i not in mcap]), [i for i in sites(MC, r'\bT §') if i not in mcap][:8]))
rt = sites(R, r'(?<![A-Za-z])T\s*§'); rte = sorted({max(k for k in range(i) if re.match(r'^#{1,4}\s*\d+\s*$', R[k])) for i in rt})
print('  Register `T §` (the paper cited as T): lines %s, occurrences %d, entries %s — "the eight citations to *Transitions* in the Register" L11369 / 1770: occurrences == 8: %s, lines == 8: %s' % (rt, cnt(R, r'(?<![A-Za-z])T\s*§', 0), [int(re.sub(r'\D', '', R[k])) for k in rte], cnt(R, r'(?<![A-Za-z])T\s*§', 0) == 8, len(rt) == 8))
print('  main `T §` lines %s (the two at L4246 / L4250 carry `(Appendix G)`; 1770 "two in the main volume")' % sites(M, r'(?<![A-Za-z])T\s*§'))
print('  MC lines with "Appendix G" that also name a G § (`§\\s*\\d+\\.\\d+` or "G, §"): %d; G §s cited from MC: %s' % (len([i for i in mcg if re.search(r'§\s*\d+\.\d+[a-z]?', MC[i - 1])]), sorted({s for i in mcg for s in re.findall(r'Appendix G[^.;|]{0,40}?§\s*(\d+\.\d+[a-z]?)', MC[i - 1])})))
print('  handles resolving elsewhere (each handle grepped raw, backticked or bare, in main / mc / pc / ioi / sc / reg / Transitions):')
unres = []
for h in sorted(set(handles)):
    c = {v: cnt(VOL[v], r'(?<![A-Za-z.])' + re.escape(h) + r'(?![A-Za-z0-9])', 0) for v in VOL}; c['T'] = cnt(T, r'(?<![A-Za-z.])' + re.escape(h) + r'(?![A-Za-z0-9])', 0)
    c['main-outside-G'] = len([i for i in sites(M, r'(?<![A-Za-z.])' + re.escape(h) + r'(?![A-Za-z0-9])') if not (g <= i < em[-1])])
    if not any(c[v] for v in ('mc', 'pc', 'ioi', 'sc', 'reg', 'T', 'main-outside-G')): unres.append(h)
    print('    %-12s %s' % (h, {k: v for k, v in c.items() if v}))
print('  handles resolving NOWHERE outside Appendix G: %d %s' % (len(unres), unres))
for name in mcents:
    print('  MC "%s": heading-line hits %d %s; body lines %d' % (name, len(sites(MC, r'^#{1,4}.*' + re.escape(name.split("the ", 1)[1]), re.I)), sites(MC, r'^#{1,4}.*' + re.escape(name.split("the ", 1)[1]), re.I)[:5], cnt(MC, re.escape(name.split("the ", 1)[1]))))

hr('§5 Register entries the G rows cite (1375, 1519, 1523, 1535, 1551, 1399, 1403) and the seating entries (1769, 1770, 1778): headed, body, WARNING line')
for n in (1375, 1519, 1523, 1535, 1551, 1399, 1403, 1769, 1770, 1778):
    e = rentry(n)
    if not e: print('  %d: NO HEADING' % n); continue
    w = [l for l in e[2] if 'WARNING' in l]
    print('  %d L%d–L%d: "%s"; WARNING lines %d %s' % (n, e[0], e[1], (rbody(n) or '')[:110], len(w), ['…' + x[max(0, x.find('WARNING') - 40):x.find('WARNING') + 260] + '…' for x in w]))
print('  §5b the G rows\' Register pointers resolved to the CLAIM (docket 9(b)): the row\'s key words token-counted in each cited entry (convention: has_token, case-insensitive; a stem left-bounded where marked *)')
KEYS = {'8.2': ['jurisdict*', 'forcing', 'disjunction', 'ternary', 'scope'], '8.4': ['vocabular*', 'functor', 'covariant', 'four parts', 'seven'], '10.4c': ['C1', 'presymplectic', 'null surface', 'transverse', 'block diagonal', 'factoris*']}
CITES = {'8.2': [1375, 1519, 1523, 1535, 1551], '8.4': [1375], '10.4c': [1399, 1403]}
def tok(text, k): return len(re.findall(r'(?<![A-Za-z])' + re.escape(k[:-1]), text, re.I)) if k.endswith('*') else has_token(text, k)
for s in ('8.2', '8.4', '10.4c'):
    for n in CITES[s]:
        e = rentry(n); body = ' '.join(e[2]) if e else ''
        c = {k: tok(body, k) for k in KEYS[s]}; print('    row %s → Register %d: %s — any key %s' % (s, n, c, any(c.values())))
    print('    row %s in Transitions: %s' % (s, {k: tok(join(tsec_body(s)), k) for k in KEYS[s]}))
print('  these seven numbers in Transitions.md (its own Part XII register): %s — they are THIS Register\'s numbers' % {n: cnt(T, r'(?<!\d)%d(?!\d)' % n, 0) for n in (1375, 1519, 1523, 1535, 1551, 1399, 1403)})
for n in ('1,105', '1,442', '1,061'):
    print('  %s in the span: %d' % (n, cnt(U + X, r'(?<![\d.,])' + n + r'(?!\d)(?!,\d{3})', 0)))
print('  "Chapter 34" / "§34" in the span: %d / %d (Index locators §34.2 §34.8 §34.10 — pointers, not figures); "Newton decrement" %d; "three quarters" %d' % (cnt(U + X, r'Chapter 34', 0), cnt(U + X, r'§34', 0), cnt(U + X, r'Newton decrement'), cnt(U + X, r'three.quarters')))
for ln in (_L(' SIAM. — the Newton decrement and self-concordance, which λ² and §23.8.2 rediscover.'), _L(" Chapter 15, and the 3/2 bound on maximal sublattices contains §30.3's measured 3/4.")): print('  L%d (named "G L%d" in HANDOFF-92 / DEF-138 item 7 / READ-ch25a): lies in `## References` L%d+ — %s | "%s"' % (ln, ln, rf, ln >= rf, M[ln - 1][:110]))

hr('§6 IoI Part XI: seventy-seven rows, thirty load-bearing pointed at Appendix G, the thirty statements "copied unchanged" (1778)')
px = sites(IOI, r'^#{1,3}\s*Part XI\b'); ig = sites(IOI, r'Appendix G\b')
print('  IoI `Part XI` heading hits %s (fault 5 self-caught: no such heading — locate the table by the heading enclosing the IoI\'s %d `Appendix G` lines %s…%s)' % (px, len(ig), ig[:2], ig[-2:]))
if ig:
    enc = sorted({max(k for k in range(i) if re.match(r'^#{1,4} ', IOI[k])) + 1 for i in ig}); print('  enclosing headings %s: %s' % (enc, [IOI[k - 1][:100] for k in enc]))
    px = [enc[0]]
if px:
    a = px[-1]; b = next((i + 1 for i in range(a, len(IOI)) if re.match(r'^#{1,2} ', IOI[i])), len(IOI) + 1)
    XI = IOI[a - 1:b - 1]; xr = [(i + a, l) for i, l in enumerate(XI) if l.startswith('|') and not re.match(r'^\|\s*-+', l)]
    print('  Part XI L%d–L%d (%d lines); `|` rows %d' % (a, b - 1, len(XI), len(xr)))
    if xr: print('  header: %s' % xr[0][1][:160])
    data = xr[1:]; print('  DATA rows %d == 77: %s' % (len(data), len(data) == 77))
    lb = [r for r in data if re.search(r'load.bearing|Appendix G', r[1], re.I)]; nu = [r for r in data if re.search(r'not used', r[1], re.I)]
    print('  rows marked load-bearing / Appendix G: %d == 30: %s; marked "not used": %d == 47: %s; both/neither: %d / %d' % (len(lb), len(lb) == 30, len(nu), len(nu) == 47, len([r for r in lb if r in nu]), len(data) - len(set(lb) | set(nu))))
    gst = {s: st for _, s, st, _ in rows}; same = 0; diff = []
    for ln, l in lb:
        c = cells(l); s = re.sub(r'[^\d.a-z]', '', c[0]) if c else ''
        st = next((x for x in c[1:] if len(x) > 20), '')
        if s in gst and (st == gst[s] or st.strip('*') == gst[s]): same += 1
        elif s in gst: diff.append((ln, s, st[:80], gst[s][:80]))
        else: diff.append((ln, s, 'NOT A G SECTION', ''))
    print('  statements identical to Appendix G\'s: %d of %d; differing: %d' % (same, len(lb), len(diff)))
    for d in diff[:40]: print('    L%d §%s | IoI: %s | G: %s' % d)
    for ln, s, _, _ in diff:
        a = next(x for x in cells(IOI[ln - 1]) if len(x) > 20); b = gst[s]; k = next((i for i in range(min(len(a), len(b))) if a[i] != b[i]), min(len(a), len(b)))
        print('    §%s first difference at char %d: IoI %r | G %r (G L%d); IoI raw cell count %d (the `\\|X\\|` of G\'s row was split as cell boundaries when the IoI row was generated: the statement is truncated at *while*, the tail *|X| stays fixed.* lost)' % (s, k, a[max(0, k - 12):k + 20], b[max(0, k - 12):k + 20], next(l for l, ss, *_ in rows if ss == s), len(cells(IOI[ln - 1]))))
        print('    IoI L%d raw: %r' % (ln, IOI[ln - 1][:230]))
    xs = sorted({re.sub(r'[^\d.a-z]', '', cells(l)[0]) for _, l in data}); print('  IoI § set == Transitions § set: %s (only-IoI %s; only-T %s)' % (set(xs) == tset, sorted(set(xs) - tset)[:10], sorted(tset - set(xs))[:10]))

hr('§7 the Index as DATA: terms, entries, relations, the down-set test (L11419 "57 terms, 311 entries, 44 specialisation relations, 0 violations")')
heads_ = []; cur = None; ent = []; rel = []
for i in range(ix[-1] - 1, rf - 1):
    l = M[i]
    m = re.match(r'^ \*\*(.+?)\*\* …… (.+)$', l); n = re.match(r'^   (\S.*?) …… (.+)$', l)
    if m: cur = m.group(1); heads_.append(cur); ent.append((cur, [x.strip() for x in m.group(2).split('·')]))
    elif n and cur: rel.append((n.group(1), cur)); ent.append((n.group(1), [x.strip() for x in n.group(2).split('·')]))
def norm(t): return re.sub(r'[*_]', '', t).strip()
terms_raw = [norm(t) for t, _ in ent]; terms = Counter(terms_raw)
print('  head terms %d (1-space indent, bold); sub-terms %d (3-space indent) = relations %d == 44: %s' % (len(heads_), len(rel), len(rel), len(rel) == 44))
print('  term lines %d; distinct terms (markup stripped) %d == 57: %s; duplicated term strings: %s' % (len(terms_raw), len(terms), len(terms) == 57, [(t, c) for t, c in terms.items() if c > 1]))
locs = defaultdict(set); pairs = 0
for t, ls in ent:
    for x in ls: pairs += 1; locs[norm(t)].add(x)
dpairs = sum(len(v) for v in locs.values())
print('  (term, location) pairs: printed %d; distinct %d; "311 entries": printed == 311: %s, distinct == 311: %s (convention: an entry is a printed locator on a term line)' % (pairs, dpairs, pairs == 311, dpairs == 311))
viol = [(s, t, sorted(locs[norm(s)] - locs[norm(t)])) for s, t in rel if not locs[norm(s)] <= locs[norm(t)]]
print('  down-set test loc(s) ⊆ loc(t) over %d relations, locators as printed: violations %d == 0: %s %s' % (len(rel), len(viol), len(viol) == 0, viol))
locs2 = {k: {('Index' if v == '*this page*' else v) for v in s} for k, s in locs.items()}; viol2 = [(s, t) for s, t in rel if not locs2[norm(s)] <= locs2[norm(t)]]
print('  same test with `*this page*` ≡ `Index` (the one location named two ways, L11490–L11491 / L11498): violations %d == 0: %s' % (len(viol2), len(viol2) == 0))
allloc = sorted({x for v in locs.values() for x in v}); secl = [x for x in allloc if x.startswith('§')]; appl = [x for x in allloc if x.startswith('App')]; oth = [x for x in allloc if not x.startswith('§') and not x.startswith('App')]
print('  distinct locators %d: § %d, App %d, other %s' % (len(allloc), len(secl), len(appl), oth))
bad = []
for x in secl:
    n = x[1:]
    try:
        hl = heading_line(M, n); sp = section_span(M, n)
        if not hl: bad.append((x, 'no heading'))
    except Exception as e: bad.append((x, 'resolver: ' + type(e).__name__))
print('  § locators resolving to a heading (heading_line): %d of %d; failures %s' % (len(secl) - len(bad), len(secl), bad))
for x in appl:
    tag = 'Appendix ' + x.split()[1]; hits = [i + 1 for i, l in enumerate(M) if re.match(r'^## ' + tag + r'\b', l)]
    print('  %s → `## %s` hits %s (LAST is the body)' % (x, tag, hits))
new = [t for t, ls in ent if any(re.match(r'§3[56](\.|$)', x) for x in ls)]
print('  "Six terms and four relations entered with Chapters 35–36": terms with a §35/§36 locator %d %s; relations among them %d %s' % (len(new), [norm(t) for t in new], len([1 for s, t in rel if s in new]), [norm(s) for s, t in rel if s in new]))
grp = [h for h in heads_ if h in ('three bodies', 'Löwdin')]; gsub = [s for s, t in rel if t in grp]
print('  alternative convention — the two head groups whose heads are Chapter 35–36 objects (*three bodies*, *Löwdin*) with their sub-terms: terms %d == 6: %s %s; relations %d == 4: %s (which terms were "entered" is not printed: record-carried either way)' % (len(grp) + len(gsub), len(grp) + len(gsub) == 6, grp + [norm(s) for s in gsub], len(gsub), len(gsub) == 4))
print('  "The previous index (57 terms, 139 entries, 44 relations)": 311 − 139 = %d; "90 locations of specialisations were absent" — unreproducible from the page (the previous index is not printed): record-carried' % (311 - 139))
# occurrence test on a term's OWN locations (loc(t) minus the union of its specialisations' — the page says generalisations carry that union, so an inherited location need not name the term)
sub_of = defaultdict(set)
for s, tt_ in rel: sub_of[norm(tt_)].add(norm(s))
def own(tt): return locs[tt] - set().union(*[locs[s] for s in sub_of[tt]]) if sub_of[tt] else set(locs[tt])
STOP = {'the', 'of', 'a', 'as', 'and'}
def sing(w): return w[:-3] + 'y' if w.endswith('ies') else (w[:-1] if w.endswith('s') and not w.endswith('ss') else w)
def probe(tt, body, why=None):
    words = [w for w in re.findall(r'[A-Za-zÀ-ÿ]+', tt) if w.lower() not in STOP]
    if not words: return tt.lower() in body.lower()   # symbol terms raw
    res = {w: (sing(w)[:5] if len(sing(w)) > 5 else sing(w)).lower() in body.lower() for w in words}   # fault 6 self-caught: `bodies` → stem `bodie` missed *three-body*; singularise first
    if why is not None: why.update(res)
    return all(res.values())
zero = []; tested = 0; inh = 0
for tt in sorted(locs, key=lambda k: terms_raw.index(k)):
    for x in sorted(own(tt)):
        if not x.startswith('§'): continue
        sp = section_span(M, x[1:]); inh += len(locs[tt]) - len(own(tt)) if x == sorted(own(tt))[0] else 0
        if not sp: continue
        tested += 1
        why = {}
        if not probe(tt, join(M[sp[0] - 1:sp[1] - 1]), why): zero.append((tt, x, sp, {w: v for w, v in why.items() if not v}))
print('  occurrence test (L11419 "the sections whose heading names it or in which it occurs at density"; convention: OWN locations only, section_span, markup-stripped join, every content word of the term by its 5-letter stem, case-insensitive, symbols raw; "density" is unnamed on the page — informational): own § locations tested %d (inherited ones skipped %d); locations where the term does not occur %d' % (tested, inh, len(zero)))
for z in zero: print('    %s → %s (section_span L%d–L%d; words absent %s)' % (z[0], z[1], z[2][0], z[2][1] - 1, list(z[3])))
print('  `Index` / `*this page*` locators: the index\'s own heading `## Index` L%d — the fixed-point entry L11498 and L11490–L11491' % ix[-1])
