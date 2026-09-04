#!/usr/bin/env python3
# r2-ch16r.py -- chat 123, prose batch for main L9157-L9306 (32.5 - 32.6.1)
# Every pointer resolved under BOTH resolvers and every cited criterion PRINTED IN FULL at its
# target; the register citations read against their entries; the standing sweeps (Ruling 45,
# Ruling 46, false universals, absent members); Prints & Proofs anchored per witness; census rows.
# r2-ch16r2.py — R3 (chat 153-R) — SUCCESSOR to r2-ch16r.py, re-anchored by tools/reanchor.py: every main-volume line the
# predecessor pinned as a literal is resolved by the text of the line it pointed at in the bundle its golden was
# banked against (28 anchors); nothing else changes. r2-ch16r.py is seated and never edited in place (chat 68).
# PROVED by tools/proveanchor.py when the line below says so; until then this file is a draft.
# PROVEANCHOR: 90+184 — reproduces r2-ch16r.out byte-exact on those bundles (G0c)

# --- re-anchoring helper (tools/reanchor.py): a main-volume line found by its own text, never by a number ---
def _L(t, d=0):
    import os as _o
    global _LM
    try: _LM
    except NameError: _LM = open(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)), 'The_Method_1_6-2.md'), encoding='utf-8').read().split('\n')
    h = [i for i, l in enumerate(_LM, 1) if l == t]
    assert len(h) == 1, ('re-anchor: line text is not unique or is absent', t[:60], h)
    return h[0] + d
import importlib.util, os, re

H = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
heading_line, section_span, has_token, enclosing = (r2lib.heading_line, r2lib.section_span,
                                                    r2lib.has_token, r2lib.enclosing)

def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
MAIN = rd('The_Method_1_6-2.md')
REG  = rd('The_Method_1_6___The_Register-2.md')
MC   = rd('The_Method_1_6___Mathematical_Compendium-2.md')
PC   = rd('The_Method_1_6___The_Physics_Compendium-2.md')
IOI  = rd('The_Method_1_6___The_Index_of_Indices-2.md')
SC   = rd('The_Method_1_6___Spectra_Compendium-2.md')
VOLS = [('main', MAIN), ('reg', REG), ('mc', MC), ('pc', PC), ('ioi', IOI), ('sc', SC)]
PP = open('/home/claude/PP_The_Method_1_6.md', encoding='utf-8').read().split('\n')
A, B = _L('### 32.5 The book satisfies its own method'), _L(' the shape of the question this book cannot pose.** Register 396.', 1)

def hr(t): print('\n' + '=' * 96 + '\n' + t + '\n' + '=' * 96)

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

# owed to r2lib (DEFERRED): regentry, grouped-aware, from r2-ch16p (chat 122).
def regentry(n):
    out = []
    for i, t in enumerate(REG, 1):
        s = t.strip()
        m = re.match(r'^#{1,4}\s*([\d,\s\u2013\u2014-]+?)\s*$', s)
        if not m: continue
        nums = set()
        for part in re.split(r'[,\s]+', m.group(1)):
            if re.fullmatch(r'\d+', part): nums.add(int(part))
            else:
                mm = re.fullmatch(r'(\d+)[\u2013\u2014-](\d+)', part)
                if mm: nums.update(range(int(mm.group(1)), int(mm.group(2)) + 1))
        if n in nums: out.append(i)
    return out

def printspan(M, a, b, tag=''):
    print(f'  --- {tag} L{a}-L{b - 1} ---')
    for i in range(a - 1, min(b - 1, len(M))): print(f'   {i+1} {M[i]}')

hr('1.  Every pointer the unit makes, resolved under BOTH resolvers')
ptrs = []
for i in range(A - 1, B):
    for m in re.finditer(r'§([\dA-G]+(?:\.\d+)*)', MAIN[i]): ptrs.append((i + 1, m.group(1)))
    for m in re.finditer(r'\bChapter\s+(\d+)', MAIN[i]): ptrs.append((i + 1, 'Ch' + m.group(1)))
    for m in re.finditer(r'\bAppendix\s+([A-G])', MAIN[i]): ptrs.append((i + 1, 'App' + m.group(1)))
print(f'  {len(ptrs)} pointer sites in the unit:')
for l, p in ptrs:
    if p.startswith(('Ch', 'App')):
        print(f'   L{l:>5} {p:<12} (chapter/appendix pointer, resolved in section 2)'); continue
    # FAULT 7, self-caught: heading_line is numeric-only, so a LETTERED pointer (§E.1.4) resolved
    # to None and would have been recorded as absent from a volume that heads it at L10986.
    # A lettered pointer needs its own pattern, §([A-Z]\.\d+(?:\.\d+)*).
    if re.match(r'^[A-G]\.', p):
        hl = next((i + 1 for i, t in enumerate(MAIN)
                   if re.match(r'^#{2,4}\s+' + re.escape(p) + r'\s', t.strip())), None)
        end = (next((i + 1 for i in range(hl, len(MAIN)) if re.match(r'^#{1,4} ', MAIN[i].strip())),
                    len(MAIN) + 1) if hl else None)
        print(f'   L{l:>5} §{p:<10} LETTERED resolver -> {(hl, end) if hl else "*** ABSENT ***"}')
        continue
    br, ss = body_range(MAIN, p), section_span(MAIN, p)
    same = ' COINCIDE' if br == ss else ' DIFFER'
    print(f'   L{l:>5} §{p:<10} body_range {br}  section_span {ss}{same}'
          + ('' if br else '   *** NO HEADING ANYWHERE ***'))

hr('2.  L9158 -- the range "§32.1--24.4"')
print('   ', MAIN[_L('### 32.5 The book satisfies its own method')].strip())
sub32 = [MAIN[i].strip() for i in range(_L(' What remains of item D is the lookup. 540 named cells, a file, and an afternoon.', 1), _L(' **That is where the word belongs.** Not on *V* = 4ν/3, which may sit in a 1922 German volume nobody cites. Not on E(X), which is a closure defect and says so. **On the shape of the thing** — a work built to be checked, that checked itself, failed twice, said so, and repaired both.', 2)) if re.match(r'^#{3,4} 32', MAIN[i].strip())]
print('  every 32.x heading in the chapter body:')
for s in sub32: print('    ', s[:88])
print('  §24.4 resolves to:', body_range(MAIN, '24.4'), '-- a section of CHAPTER 24, before chapter 32.')
print('  §32.4.4 resolves to:', body_range(MAIN, '32.4.4'), ' §32.4.2 resolves to:', body_range(MAIN, '32.4.2'))
print('  -> the range runs from a section of chapter 32 to a section of chapter 24, i.e. backwards;')
print('     the chapter has no §32.4.4 and its self-audit run ends at §32.4.2.')

hr('3.  The cited criteria, PRINTED IN FULL at their targets (a token probe is not a reading)')
for sec, why in (('16.5', 'L9193 cites it for totality: "every claim supported, cited, or marked open"'),
                 ('16.3', 'L9201 cites it for D_phys'),
                 ('6.3',  'L9285 cites it for the calendar, "E = 7 is the price of keeping January first"')):
    br, ss = body_range(MAIN, sec), section_span(MAIN, sec)
    print(f'\n  §{sec}: body_range {br}  section_span {ss}  {"COINCIDE" if br==ss else "DIFFER"}   [{why}]')
    printspan(MAIN, br[0], br[1], f'§{sec} body')

hr('4.  L9281 -- "the same pair §14.5.6 finds R_4 refusing"')
br = body_range(MAIN, '14.5.6'); ss = section_span(MAIN, '14.5.6')
print(f'  §14.5.6 body_range {br}  section_span {ss}  {"COINCIDE" if br==ss else "DIFFER"}')
printspan(MAIN, br[0], br[1], '§14.5.6 whole')
nonblank = [i + 1 for i in range(br[0], br[1] - 1) if MAIN[i].strip()]
print(f'  non-blank BODY lines in §14.5.6: {len(nonblank)} {nonblank}')
for tok in ('dishonest', 'outside'):
    hits = [i + 1 for i in range(len(MAIN)) if has_token(MAIN[i], tok)]
    print(f'  "{tok}" sites in main: {len(hits)}  in §14.5 span: '
          f'{[h for h in hits if 3790 <= h <= 3830]}   in unit: {[h for h in hits if A <= h <= B]}')
r4 = [i + 1 for i in range(len(MAIN)) if '\u211b\u2084' in MAIN[i] or 'R_4' in MAIN[i]]
print(f'  R_4 (script-R subscript 4) sites in main: {len(r4)} {r4[:14]}')
print('  PP check -- does §14.5.6 carry a body in the ORIGINAL?')
ppl = [i + 1 for i in range(len(PP)) if PP[i].strip().startswith('#') and '14.5.6' in PP[i]]
print('   PP §14.5.6 heading at:', ppl)
for l in ppl: printspan(PP, l, l + 4, 'PP §14.5.6')

hr('5.  L9302-L9305 -- §E.1.4 and §29.2.2')
for sec in ('E.1.4', '29.2.2'):
    hl = None
    for i, t in enumerate(MAIN, 1):
        if re.match(r'^#{3,4}\s+' + re.escape(sec) + r'\s', t.strip()): hl = i; break
    if hl is None:
        print(f'  §{sec}: *** NO HEADING ***'); continue
    end = next((i + 1 for i in range(hl, len(MAIN)) if re.match(r'^#{1,4} ', MAIN[i].strip())), len(MAIN) + 1)
    print(f'\n  §{sec} at L{hl}, body to L{end - 1}')
    printspan(MAIN, hl, end, f'§{sec}')

hr('6.  16j-05 -- "The three conditions" (L9207) against §31.3.4\'s "fourth falsification test"')
br = body_range(MAIN, '31.3.4')
print('  §31.3.4 body_range', br, ' section_span', section_span(MAIN, '31.3.4'))
printspan(MAIN, br[0], br[1], '§31.3.4')
for tok in ('falsification',):
    hits = [i + 1 for i in range(len(MAIN)) if has_token(MAIN[i], tok)]
    print(f'  "{tok}" sites in main: {len(hits)} {hits}')
ordn = [i + 1 for i in range(len(MAIN))
        if re.search(r'\b(first|second|third|fourth|fifth)\s+falsification\b', MAIN[i], re.I)]
print('  ordinal + "falsification" sites:', ordn)
for l in ordn: print(f'   L{l}: {MAIN[l-1].strip()[:150]}')

hr('7.  The register citations the unit makes, read against their entries')
for n in (275, 387, 396, 571, 572, 573):
    ls = regentry(n)
    if not ls:
        print(f'\n  register {n}: *** NO ENTRY IN THE REGISTER ***   cited at main '
              f'{[l for l in numsites(MAIN, n) if A <= l <= B]}')
        continue
    st = ls[0]
    end = next((i + 1 for i in range(st, len(REG)) if re.match(r'^#{1,4}\s*[\d,\s\u2013-]+\s*$', REG[i].strip())),
               len(REG) + 1)
    print(f'\n  register {n} at reg L{st}, entry to L{min(end - 1, st + 26)}')
    printspan(REG, st, min(end, st + 27), f'register {n}')

hr('8.  Appendix B -- 153 channels against the channel table arbiter')
occ = [i + 1 for i, t in enumerate(MAIN) if re.match(r'^##\s+Appendix\s+B\b', t.strip())]
ab = [l for l in occ if l > 200][-1]
end = next((i + 1 for i in range(ab, len(MAIN)) if re.match(r'^##\s', MAIN[i].strip())), len(MAIN) + 1)
printspan(MAIN, ab, end, 'Appendix B whole')
print('  spectra totals line L900:', SC[899].strip())

hr('9.  1,061 -- "Every bracket in this book is recomputable from this book. All 1,061."')
for l in numsites(MAIN, 1061):
    print(f'   main L{l}: {MAIN[l-1].strip()[:170]}')
for l in numsites(REG, 1061):
    print(f'   reg  L{l}: {REG[l-1].strip()[:170]}')

hr('10. Ruling 45 -- build, press and editorial-process prose inside the unit')
R45 = ['build', 'builds', 'press', 'presses', 'rebuilt', 'recomputes', 'recomputed', 'checker',
       'script', 'session', 'draft', 'version', 'repaired', 'repair', 'corrected', 'this work',
       'earlier form', 'first run', 'now states', 'markdown', 'page']
hits = {}
for i in range(A - 1, B):
    for w in R45:
        if has_token(MAIN[i], w.split()[0]) and (len(w.split()) == 1 or w in MAIN[i].lower()):
            hits.setdefault(i + 1, set()).add(w)
for l in sorted(hits):
    print(f'   L{l:>5} {sorted(hits[l])}\n         {MAIN[l-1].strip()[:150]}')
print(f'  Ruling 45 candidate sites in the unit: {len(hits)} of {B-A+1} lines')
# FAULT 8, self-caught: r'\b(I|my|we|our)\b' matches the Roman numeral I in a species name, so
# L9241's "the He I defects" scored as first-person prose.  The book was right.  A bare I is only
# first person when it is not preceded by an element symbol and not followed by a stage numeral.
naive = [i + 1 for i in range(A - 1, B) if re.search(r'\b(I|my|we|our)\b', MAIN[i])]
fp = [i + 1 for i in range(A - 1, B)
      if re.search(r'\b(my|we|our)\b', MAIN[i])
      or re.search(r'(?<![A-Z][a-z] )(?<![A-Z] )\bI\b(?!\s*[IVX])(?!\s*\()', MAIN[i])]
print('  naive probe (WRONG -- matches "He I"):', naive)
print('  first-person prose sites in the unit:', fp if fp else 'none')
for l in fp: print(f'   L{l}: {MAIN[l-1].strip()[:140]}')

hr('11. Ruling 46 -- script names, build numbers and internal file references (case-sensitive)')
pat = re.compile(r'\b[\w-]+\.(py|md|json|tsv|csv|png)\b|\bBUILD\d+\b|\bmarkdown\b')
for t, M in VOLS:
    hits = [(i + 1, pat.findall(M[i]), M[i].strip()[:110]) for i in range(len(M)) if pat.search(M[i])]
    inunit = [h for h in hits if t == 'main' and A <= h[0] <= B]
    print(f'  {t}: {len(hits)} sites; in the unit: {len(inunit)}')
    for l, f, txt in inunit: print(f'    L{l} {f} :: {txt}')
ppm = [i + 1 for i in range(len(PP)) if pat.search(PP[i])]
print('  PP sites:', len(ppm))

hr('12. False universals and absent members inside the unit')
UNIV = ['every', 'all', 'never', 'always', 'no ', 'none', 'each', 'only', 'nothing', 'any']
for i in range(A - 1, B):
    got = [w for w in UNIV if re.search(r'\b' + w.strip() + r'\b', MAIN[i], re.I)]
    if got: print(f'   L{i+1:>5} {got}\n         {MAIN[i].strip()[:150]}')

hr('13. "Sc VI" and the sulphur-like sequence -- the absent-member class (docket 20)')
# FAULT 9, self-caught: a LITERAL 'Sc VI' probe scored zero in the Spectra Compendium and would
# have recorded the book's one worked species as an absent member; the compendium carries Sc rows
# at L800-L810 under other notations.  A literal-string probe is not a species test.
for t, M in VOLS:
    lit = [i + 1 for i in range(len(M)) if 'Sc VI' in M[i]]
    anysc = [i + 1 for i in range(len(M)) if re.search(r'\bSc\b', M[i])]
    print(f'  {t}: literal "Sc VI" {len(lit)} {lit[:12]}   any Sc row {len(anysc)} {anysc[:12]}')
for t, M in VOLS:
    s = [i + 1 for i in range(len(M)) if re.search(r'sulphur-like|sulfur-like', M[i], re.I)]
    if s: print(f'  sulphur-like in {t}: {s}')

hr('14. Prints & Proofs -- every witness anchored on its OWN text')
WIT = [_L('### 32.5 The book satisfies its own method'), _L(' Appendix B carries all three for all 153 channels. So the question has an answer, and it is checkable'), _L('    Six of six, exact. No external table, no database, no constant supplied by hand.'), _L('    Every bracket in this book is recomputable from this book. All 1,061.'), _L(' **Together they close.** The index supplies the *what*; the collection supplies the *how much*; **and the seven-line arithmetic between them is printed in §25.6.**'), _L(' The three conditions are tested here, on this text, with the results reported whether or not they are'), _L('    The test found a break. This chapter was written as Chapter 31 while the contents listed it as 21,'), _L('    The first run failed, and the failure was informative twice over. Thirty-nine claims'), _L(' **The three remaining are not claims.** One reads "100% over 2,513 tests", which *is* a verification; two are sentences that happen to contain a number.'), _L('    One hit, and it is a false positive: "a fit says where a level probably is" describes what a fit does.'), _L(' The book carries four indices of its own shortfall, and the question *what remains* has an arithmetic'), _L(' **E(Λ) = 0, E(audits) = 16, E(G) = 40, E(Q) = 5 unfibred, E(D) = 4 unfibred — sixty-five cells in'), _L(' **fourteen dominated, two on the frontier** — both *outside · dishonest*, the same pair §14.5.6 finds'), _L(' **Cells that are ordinary work.** Ten open items in Appendix E, of which **eight stop at the same'), _L('    **So the honest count is not forty-three.** It is: some number of dominated cells that should'), _L(' **And two things sit outside all four indices.** §E.1.4 shows the open set cannot express an unclosable')]
def norm(s): return re.sub(r'\s+', ' ', s.strip())
for l in WIT:
    t = norm(MAIN[l - 1])
    key = t[:60]
    hit = [i + 1 for i in range(len(PP)) if key and key in norm(PP[i])]
    print(f'   L{l:>5} PP {hit if hit else "ABSENT"}   offset '
          f'{[h - l for h in hit] if hit else "--"}   :: {t[:70]}')

hr('15. Census rows 713, 1191, 1192, 1193 -- re-tested from the file')
for rid, l, tok in ((713, _L('### 32.5.1 The prediction, recomputed from the text'), '32.5'), (_L(' a second derivation that does not pass through the first* — and the seed is a quantity that matters,'), _L(' §32.1–24.4 ask whether this book obeys its own law. They never ask whether it obeys its own'), 'never'), (_L(" prune-greedy was one derivation, and no second was ever built. **§2.8's own gloss is what happened:"), _L(' stale the moment the book is written into. The second never closed: its own five terms summed to'), 'never'), (_L(' an identity computed along one path is vacuous.** The protocol was not missing; it was not applied.'), _L(' the destination coordinate of the temporal mechanisms are not open items and never will be. **They are'), 'never')):
    print(f'\n  row {rid}: L{l} token {tok!r}')
    print(f'   {MAIN[l-1].strip()[:170]}')
    if tok == '32.5':
        print(f'   §32.5 heading resolves to {body_range(MAIN, "32.5")}; the token is the section\'s'
              f' OWN live number, sites {numsites(MAIN, 0) and ""}'
              f'{[i+1 for i in range(len(MAIN)) if "32.5" in MAIN[i]][:12]}')
        wd = [i + 1 for i in range(len(MAIN)) if has_token(MAIN[i], 'withdrawn') or has_token(MAIN[i], 'withdrew')]
        print(f'   withdrawal words anywhere near §32.5: {[w for w in wd if 9150 <= w <= 9210]}')
