#!/usr/bin/env python3
# r2-ch16q.py -- chat 123, computable batch for main L9157-L9306 (32.5 - 32.6.1)
# Recomputes the Sc VI bracket table from the book's own inputs, re-runs the three falsification
# tests against the book AS IT NOW STANDS, and checks every count word in the unit against its own
# body, its row labels, its numeral span and its own status markers.
# r2-ch16q2.py — R3 (chat 153-R) — SUCCESSOR to r2-ch16q.py, re-anchored by tools/reanchor.py: every main-volume line the
# predecessor pinned as a literal is resolved by the text of the line it pointed at in the bundle its golden was
# banked against (9 anchors); nothing else changes. r2-ch16q.py is seated and never edited in place (chat 68).
# PROVED by tools/proveanchor.py when the line below says so; until then this file is a draft.
# PROVEANCHOR: 90+184 — reproduces r2-ch16q.out byte-exact on those bundles (G0c)

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
from decimal import Decimal, ROUND_HALF_UP

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
A, B = _L('### 32.5 The book satisfies its own method'), _L(' the shape of the question this book cannot pose.** Register 396.', 1)

def hr(t): print('\n' + '=' * 96 + '\n' + t + '\n' + '=' * 96)

# owed to r2lib (DEFERRED): body_range, carried with provenance from r2-ch16m (chat 121).
def body_range(M, sec):
    """[start, end) of a section's OWN body: heading to the next heading of any number."""
    s = heading_line(M, sec)
    if s is None: return None
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1].strip()):
            return (s, i)
    return (s, len(M) + 1)

# owed to r2lib (DEFERRED): lettered_heading, carried with provenance from r2-ch16p (chat 122).
def lettered_heading(M, sec):
    for i, t in enumerate(M, 1):
        m = re.match(r'^#{1,4} ([A-G](?:\.\d+)*)\.? ', t.strip())
        if m and m.group(1) == sec: return i
    return None

# owed to r2lib (DEFERRED): numsites, comma-aware, carried with provenance from r2-ch16p (chat 122).
def numsites(M, n):
    """SITES of a digit-bounded numeral, never a count.  Both the plain and the comma-grouped
    forms are swept -- chat 122's fault 3 was a sweep that saw neither its own table line nor any
    four- or five-digit figure the book prints."""
    forms = {str(n), f'{n:,}'}
    pat = '(?:' + '|'.join(re.escape(f) for f in forms) + ')'
    pat = r'(?<![\d.,])' + pat + r'(?!\d)(?!,\d)(?!\.\d)'
    return [i + 1 for i in range(len(M)) if re.search(pat, M[i])]

def q(x, places='0.01'):
    """Decimal.quantize HALF_UP -- never Python's round(), which is binary and wrong on .5."""
    return Decimal(str(x)).quantize(Decimal(places), rounding=ROUND_HALF_UP)

def pct(a, b, places='1'):
    return Decimal(a * 100) / Decimal(b) if b else None

hr('1.  32.5.1 -- the six-row table recomputed from 25.6\'s OWN inputs, nothing supplied by hand')
b256 = body_range(MAIN, '25.6'); s256 = section_span(MAIN, '25.6')
print('25.6  body_range', b256, ' section_span', s256, ' -> DIFFER (25.6 has subsections)')
print('25.6\'s OWN body carries no arithmetic; the six figures live in 25.6.1-25.6.4.')
# inputs parsed out of the book's own markdown, exactly as 32.5.1 claims
src = '\n'.join(MAIN[s256[0]-1:s256[1]-1])
d4 = float(re.search(r'\u03b4\(4s\)\s*=\s*([\d.]+)', src).group(1))
d5 = float(re.search(r'\u03b4\(5s\)\s*=\s*([\d.]+)', src).group(1))
print(f'parsed  delta(4s) = {d4}   delta(5s) = {d5}   (L7004, 25.6.1)')
d2 = (d4 - d5) / (1/16 - 1/25)
d0 = d4 - d2/16
d6 = d0 + d2/36
d6cvx = 2*d5 - d4
print(f'  two-point Ritz   d2 = {q(d2,"0.0001")}  (book 1.0889)   dinf = d0 = {q(d0,"0.0001")}  (book 0.9376)')
print(f'  d(6s) estimate      = {q(d6,"0.0001")}  (book 0.9679)')
print(f'  convex tangent      = {q(d6cvx,"0.0001")}  (book 0.9567)')
# the ionisation limit is the one number 25.6 does not print; back it out of the printed edge and
# check that BOTH printed edges and BOTH printed estimates then follow from it.
R, Z = 109737.31568, 6
def E(delta, limit): return limit - R*Z*Z/((6-delta)**2)
lim = 735860 + R*Z*Z/((6-d5)**2)
print(f'  limit backed out of the printed lower edge: {q(lim,"1")} cm-1  (R*Z^2 = {q(R*Z*Z,"1")})')
STATED = {'E(6s) estimate': 736688, 'bracket lower': 735860, 'bracket upper': 738547,
          'width': 2687, 'convex upper': 737380, 'convex width': 1520}
RECOMP = {'E(6s) estimate': E(d6, lim), 'bracket lower': E(d5, lim), 'bracket upper': E(d0, lim),
          'convex upper': E(d6cvx, lim)}
RECOMP['width'] = RECOMP['bracket upper'] - RECOMP['bracket lower']
RECOMP['convex width'] = RECOMP['convex upper'] - RECOMP['bracket lower']
print(f'{"quantity":22}{"recomputed":>14}{"stated":>12}   verdict')
ok = 0
for k in ('E(6s) estimate','bracket lower','bracket upper','width','convex upper','convex width'):
    v = int(q(RECOMP[k], '1')); s = STATED[k]
    good = abs(v - s) <= 2
    ok += good
    print(f'{k:22}{v:>14,}{s:>12,}   {"exact" if v==s else ("within 2 cm-1" if good else "DEVIATION")}')
print(f'  -> {ok} of 6 reproduce.')
# FAULT 1, self-caught: the first form counted the header row with the data rows and reported a
# SEVEN-row table under a "Six of six" count word.  Data rows only.
hdr = [i+1 for i in range(_L(' arithmetic §25.6 states:', 1),_L('| convex width | **1,520** | 1,520 |', 1)) if MAIN[i].startswith('| ') and 'recomputed' in MAIN[i]]
sep = [i+1 for i in range(_L(' arithmetic §25.6 states:', 1),_L('| convex width | **1,520** | 1,520 |', 1)) if re.match(r'^\|[\s:|-]+$', MAIN[i])]
data = [i+1 for i in range(_L(' arithmetic §25.6 states:', 1),_L('| convex width | **1,520** | 1,520 |', 1)) if MAIN[i].startswith('| ') and i+1 not in hdr]
print(f'  table: header {hdr}  separator {sep}  DATA rows {len(data)} {data}')
print(f'  "Six of six, exact" over {len(data)} data rows -> '
      f'{"REACHES" if len(data)==6 else "DOES NOT REACH"}')
print('  NOTE: 25.6.1 L7019 adds "the limit\'s own +/-400 to be added at both edges"; 32.5.1 carries no such caution.')

hr('2.  32.5.3 -- "the seven-line arithmetic between them is printed in 25.6"')
# FAULT 2, self-caught: the first form required a 4-space indent AND a relation symbol, so it saw
# neither of the two space-aligned table rows (2-space indent, no symbol) nor the continuation line
# of the bracket display, and scored the deduction at four lines.  Convention swept, not guessed.
b1 = body_range(MAIN,'25.6.1'); b2 = body_range(MAIN,'25.6.2')
disp = [i+1 for i in range(b1[0]-1, b2[1]-1)
        if MAIN[i].strip() and re.match(r'^\s{2,}', MAIN[i]) and re.search(r'\d', MAIN[i])]
print('25.6.1+25.6.2 display lines carrying a digit:', disp)
# the closing commentary paragraph of 25.6.2 is indented like a display but is prose
tail = []
for l in reversed(disp):
    if l >= b2[1]-4 or (MAIN[l-1].strip()[0].isupper() and not re.search(r'[=<>\u2264\u2265]', MAIN[l-1])
                        and not re.search(r'\d,\d\d\d', MAIN[l-1])):
        tail.append(l)
    else: break
tail = sorted(tail)
core = [l for l in disp if l not in tail]
print(f'  minus the closing commentary block {tail}: {len(core)} lines -> {core}')
print(f'  -> "the seven-line arithmetic ... printed in 25.6" '
      f'{"REACHES" if len(core)==7 else "DOES NOT REACH"} at {len(core)} under the display-block'
      f' convention (indented display lines of 25.6.1+25.6.2 carrying a digit, commentary excluded).')

hr('3.  32.5 L9165 -- "Appendix B carries all three for all 153 channels"')
# FAULT 3, self-caught: lettered_heading matches '## B.1 ...' but the volume heads its appendices
# '## Appendix B --- Data and provenance', so it returned None and the step crashed.  Both
# occurrences are resolved and the BODY one taken -- the contents block is L110-L175.
def appendix_span(M, letter):
    occ = [i+1 for i, t in enumerate(M) if re.match(rf'^##\s+Appendix\s+{letter}\b', t.strip())]
    body = [l for l in occ if l > 200]
    if not body: return None, None, occ
    s = body[-1]
    for i in range(s, len(M)):
        if re.match(r'^##\s', M[i].strip()): return s, i+1, occ
    return s, len(M)+1, occ
ab, nxt, occB = appendix_span(MAIN, 'B')
print('Appendix B occurrences (contents + body):', occB, '-> BODY', ab)
print('Appendix B span:', (ab, nxt), repr(MAIN[ab-1][:70]))
abrows = [i+1 for i in range(ab, nxt-1) if MAIN[i].startswith('| ') and not re.match(r'^\|[\s:-]+\|', MAIN[i])]
print('  pipe-table rows inside Appendix B (header rows included):', len(abrows))
for n in (153, 596, 1061, 2269):
    print(f'  numeral {n:>5,} sites in Appendix B span:', [l for l in numsites(MAIN, n) if ab <= l < nxt])
print('  the channel table ARBITER (spectra member, section II L293-L934), totals line L900:')
print('   ', SC[899].strip()[:160])
for n in (153, 596):
    print(f'  numeral {n:>5,} sites, all six volumes:',
          {t: numsites(M, n) if t!='main' else numsites(M, n) for t, M in VOLS if numsites(M, n)})

hr('4.  32.5.2 -- "Every bracket in this book is recomputable from this book. All 1,061."')
for n in (1061,):
    for t, M in VOLS:
        s = numsites(M, n)
        if s: print(f'  {n:,} in {t}: {s}')
b255 = body_range(MAIN, '25.5')
print('  25.5 body_range', b255, ' section_span', section_span(MAIN,'25.5'), '-> COINCIDE (no subsections)')
for i in range(b255[0]-1, b255[1]-1):
    if '1,061' in MAIN[i] or '1061' in MAIN[i]: print('   25.5 L%d %s' % (i+1, MAIN[i].strip()[:150]))
print('  "bracket" word-form sites in main:', len([i+1 for i in range(len(MAIN)) if has_token(MAIN[i],'bracket')]))

hr('5.  32.6 Condition 1 -- the three checks re-run against the book as it NOW stands')
figs = [i+1 for i in range(len(MAIN)) if re.search(r'!\[Figure', MAIN[i])]
caps = [i+1 for i in range(len(MAIN)) if re.match(r'^\s*(\*\*)?Figure\s+[A-Z]?\d', MAIN[i].strip())]
print(f'  embedded ![Figure ...] references in the volume: {len(figs)}')
# FAULT 6, self-caught: this line-anchored caption count returns 32 and would have scored a 33/32
# MISMATCH against the book.  One caption is not line-anchored.  The correct measure is the
# PAIRING test in section 12, which finds all 33 embeds paired and none orphaned; the book is
# right and this count is the wrong instrument.  Kept, labelled, and not used to score.
print(f'  line-anchored caption count (NOT the measure -- see section 12): {len(caps)}')
print(f'  32.6 prints "figures embedded / captions | 18 / 18"  -> the volume now carries {len(figs)}.')
# chapters cross-referenced but absent
body_ch = {}
for i, t in enumerate(MAIN, 1):
    m = re.match(r'^##\s+(\d+)\.\s', t.strip())
    if m: body_ch.setdefault(int(m.group(1)), []).append(i)
print('  body chapter headings measured:', sorted(body_ch))
dupe = {k: v for k, v in body_ch.items() if len(v) > 1}
print('  chapter headings with TWO occurrences (contents + body):', {k: v for k, v in dupe.items()})
cited = sorted({int(m.group(1)) for i in range(len(MAIN))
                for m in re.finditer(r'\bChapter\s+(\d+)\b', MAIN[i])})
missing = [c for c in cited if c not in body_ch]
print('  chapters cross-referenced:', cited)
print('  chapters cross-referenced but ABSENT:', missing if missing else 'none')
# FAULT 4, self-caught: the first form was §(\d+)(?!\d), which reads the chapter part of every
# §32.5 as a bare §32 pointer.  Ruling: a pointer-site regex must be §N(?!\d)(?!\.\d).
bare = sorted({int(m.group(1)) for i in range(len(MAIN)) for m in re.finditer(r'§(\d+)(?!\d)(?!\.\d)', MAIN[i])})
dotted = sorted({int(m.group(1)) for i in range(len(MAIN)) for m in re.finditer(r'§(\d+)\.\d', MAIN[i])})
absent = [s for s in sorted(set(bare) | set(dotted)) if s not in body_ch]
print('  § chapter numbers referenced (bare + dotted):', sorted(set(bare) | set(dotted)))
print('  § references whose CHAPTER is absent:', absent if absent else 'none')
print('  Chapter 30 exists at:', body_ch.get(30), ' Chapter 31 at:', body_ch.get(31))
print('  L9222 "This chapter was written as Chapter 31" -- the enclosing chapter of L9222 is:',
      max([c for c in body_ch if max(body_ch[c]) <= _L('    The test found a break. This chapter was written as Chapter 31 while the contents listed it as 21,')], default=None))

hr('6.  32.6 Condition 2 -- the three-pass table, its arithmetic and its prose count word')
rows = [(85,46,39),(63,56,7),(63,60,3)]
for tot, carry, bare in rows:
    p = pct(carry, tot)
    print(f'  {tot:>3} claims, {carry:>3} carrying ({q(p,"1")}%), {bare:>3} bare   '
          f'| tot-carry = {tot-carry} {"OK" if tot-carry==bare else "MISMATCH"}')
print('  printed percentages: 54 / 89 / 95 ->',
      [str(q(pct(c,t),'1')) for t,c,_ in rows])
print('  L9239 prose: "Thirty-nine claims genuinely lacked a verification, and each has been given one"')
print(f'  measured against the table: the corrected checker found {rows[1][2]} bare, not 39;')
print(f'  after repair {rows[2][2]} bare, so {rows[1][2]-rows[2][2]} were given a verification, not 39.')
print(f'  L9262 restates the same 39 in the result table.')
print('  2,513 ("100% over 2,513 tests") sites:', {t: numsites(M,2513) for t,M in VOLS if numsites(M,2513)})

hr('7.  32.6 Condition 3 -- the hedged-assertion sweep re-run on the volume')
HEDGE = ['probably','presumably','arguably','seems','seemingly','apparently','likely','perhaps']
for w in HEDGE:
    s = [i+1 for i in range(len(MAIN)) if has_token(MAIN[i], w)]
    print(f'  {w:12} sites in main: {len(s):>3}  {s[:14]}{" ..." if len(s)>14 else ""}')
named = ['probably','presumably','arguably','seems']
allsites = sorted({i+1 for w in named for i in range(len(MAIN)) if has_token(MAIN[i], w)})
print(f'  the four words 32.6 NAMES ({", ".join(named)}): {len(allsites)} sites -> {allsites}')
print('  32.6 prints "One hit, and it is a false positive".')
for l in allsites: print(f'   L{l}: {MAIN[l-1].strip()[:140]}')

hr('8.  32.6.1 -- the five E-terms, their sum, and the count word "four indices"')
terms = {'E(Lambda)':0,'E(audits)':16,'E(G)':40,'E(Q)':5,'E(D)':4}
print('  printed terms:', terms, ' sum =', sum(terms.values()), ' printed total "sixty-five" ->',
      'REACHES' if sum(terms.values())==65 else 'DOES NOT REACH')
print('  L9268 "The book carries four indices of its own shortfall" ; L9302 "all four indices"')
print(f'  terms actually printed at L9270: {len(terms)}')
print('  L9280 "run on two indexes rather than one"; L9286 "the same test has not been run on the'
      ' other three indices" -> 2 + 3 =', 2+3)
print('  L9273 "its own five terms summed to forty-four" -> the section itself says FIVE.')
print('  domination arithmetic:')
print('    numbers index: ten of eleven dominated  -> 11-10 =', 11-10, 'on the frontier')
print('    audits:  sixteen admitted, fourteen dominated, two on frontier -> 14+2 =', 14+2,
      'OK' if 14+2==16 else 'MISMATCH')
print('    G:       forty admitted, ten dominated, thirty on frontier    -> 10+30 =', 10+30,
      'OK' if 10+30==40 else 'MISMATCH')
print('  L9298 "So the honest count is not forty-three" against the live total at L9270:', sum(terms.values()))
print('  forty-three / 43 sites in main:', numsites(MAIN,43)[:20])

hr('9.  32.6.1 -- Appendix E open items, and the 8 + 1 + 1 split')
# FAULT 5, self-caught: the same wrong heading form, carried into Appendix E.
ae, nxtE, occE = appendix_span(MAIN, 'E')
print('  Appendix E occurrences:', occE, '-> BODY', ae, ' span', (ae, nxtE))
print('  E.1.2 heading:', repr(MAIN[heading_line(MAIN,'E.1.2')-1].strip()) if heading_line(MAIN,'E.1.2') else
      [MAIN[i].strip() for i in range(ae, nxtE-1) if MAIN[i].strip().startswith('### E.1.2')])
for h in ('E.1.2','E.3','E.4.1'):
    hl = [i+1 for i in range(ae-1, nxtE-1) if MAIN[i].strip().startswith('### '+h+' ')]
    print(f'  {h}: {hl} {MAIN[hl[0]-1].strip()[:100] if hl else ""}')
e3 = [i+1 for i in range(ae-1, nxtE-1) if MAIN[i].strip().startswith('### E.3 ')]
if e3:
    end = next((i+1 for i in range(e3[0], nxtE-1) if re.match(r'^#{2,4} ', MAIN[i].strip())), nxtE)
    opens = [i+1 for i in range(e3[0], end-1) if re.match(r'^\s*\*\*Q\d|^\s*\|\s*\*?\*?Q\d|^#{4} ', MAIN[i])]
    print(f'  E.3 span ({e3[0]}, {end}); item-like lines: {len(opens)} {opens[:16]}')
for n in (10, 14, 8, 5, 4):
    print(f'  numeral {n} sites inside Appendix E:', [l for l in numsites(MAIN,n) if ae <= l < nxtE][:14])

hr('10. Register citations made by the unit -- existence first, then on point')
def regentry(n):
    """grouped-aware Register lookup: bare '### 96' headings AND comma/dash grouped headings."""
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
                if mm: nums.update(range(int(mm.group(1)), int(mm.group(2))+1))
        if n in nums:
            head = ''
            for j in range(i, min(i+6, len(REG))):
                if REG[j].strip(): head = REG[j].strip(); break
            out.append((i, s, head[:150]))
    return out
cites = sorted({int(m.group(1)) for i in range(A-1, B)
                for m in re.finditer(r'[Rr]egisters?\s+(\d+)', MAIN[i])})
extra = sorted({int(x) for i in range(A-1,B) for x in re.findall(r'Registers\s+(\d+)\u2013(\d+)', MAIN[i]) for x in x})
print('  register numbers cited in the unit:', cites, ' (range endpoints seen:', extra, ')')
for n in sorted(set(cites) | {571,572,573}):
    e = regentry(n)
    print(f'  register {n}: {"PRESENT" if e else "*** NO ENTRY ***"}  {e[0][2][:120] if e else ""}')

hr('11. Duplicated-section sweep (DEF-105 item 1) on the unit\'s long lines')
def norm(s): return re.sub(r'\s+',' ',s.strip())
unit = {norm(MAIN[i]) for i in range(A-1,B) if len(norm(MAIN[i])) >= 80}
rec = []
for i in range(len(MAIN)):
    if A-1 <= i < B: continue
    if norm(MAIN[i]) in unit: rec.append(i+1)
print(f'  long lines in unit: {len(unit)}   recurring elsewhere in main: {len(rec)} {rec[:10]}')

hr('12. Condition 1\'s third check in detail -- does every embedded figure pair with a caption?')
emb = [(i+1, re.search(r'!\[Figure\s+([A-Z]?[\d.]+)', MAIN[i]).group(1))
       for i in range(len(MAIN)) if re.search(r'!\[Figure', MAIN[i])]
print(f'  embedded: {len(emb)}')
unpaired = []
for l, tag in emb:
    win = ' '.join(MAIN[l:min(l+6, len(MAIN))])
    if not re.search(r'Figure\s+' + re.escape(tag) + r'\b', win): unpaired.append((l, tag))
print(f'  embedded figures with NO caption in the following 6 lines: {len(unpaired)} {unpaired}')
seen = {}
for l, tag in emb: seen.setdefault(tag, []).append(l)
print(f'  distinct figure tags: {len(seen)}   tags embedded twice: '
      f'{ {k: v for k, v in seen.items() if len(v) > 1} }')
print('  32.6 prints 18 / 18; measured embedded / distinct tags / unpaired ='
      f' {len(emb)} / {len(seen)} / {len(unpaired)}')

hr('13. Every numeral the unit prints, swept comma-aware across the volume')
nums = sorted({int(x.replace(',','')) for i in range(A-1,B)
               for x in re.findall(r'(?<![\d.,])(\d{1,3}(?:,\d{3})+|\d+)(?![\d,]*\.\d)', MAIN[i])})
for n in nums:
    if n < 10: continue
    s = numsites(MAIN, n)
    inside = [l for l in s if A <= l <= B]
    print(f'  {n:>9,}  main sites {len(s):>3}  in-unit {len(inside)}  first outside: {[l for l in s if not (A<=l<=B)][:6]}')
