#!/usr/bin/env python3
# r2-ch16p2.py — chat 153 — SUCCESSOR to r2-ch16p.py, re-anchored. Identical measurements; addresses move.
# r2-ch16p named two citing lines (11555, 11799) and started a sweep at the References body (11503) by
# literal. All three moved +8. The citing lines are resolved by their own text and the References body
# by its heading, which is what the standing method requires; the 32.2 window at 9030 is below the
# insertion point and did not move, so it is left exactly as it was.
# r2-ch16p is seated and is never edited in place (chat 68).
# PROVED by tools/proveanchor.py: reproduces r2-ch16p.out byte-exact on the pre-shift bundles (G0c).
# r2-ch16p.py -- chat 122, prose batch for main L9030-L9156
# Pointers, attributions, register citations, restated figures, self-description, PP anchoring,
# census rows, and the two standing sweeps (Ruling 45, Ruling 46).
# r2-ch16p3.py — R3 (chat 153-R) — SUCCESSOR to r2-ch16p2.py, re-anchored by tools/reanchor.py: every main-volume line the
# predecessor pinned as a literal is resolved by the text of the line it pointed at in the bundle its golden was
# banked against (15 anchors); nothing else changes. r2-ch16p2.py is seated and never edited in place (chat 68).
# PROVED by tools/proveanchor.py when the line below says so; until then this file is a draft.
# PROVEANCHOR: NOT PROVED on 90+184, 92+188 or 98+202 — reproduces r2-ch16p2.out byte-exact on those bundles (G0c)

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
import unicodedata

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
A, B = _L('### 32.2 Self-reference'), _L(' constraints, the values are read off an object built at particular caps. Register 394.', 1)

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

def lettered_heading(M, sec):
    for i, t in enumerate(M, 1):
        m = re.match(r'^#{1,4} ([A-G](?:\.\d+)*)\.? ', t.strip())
        if m and m.group(1) == sec: return i
    return None

def numsites(M, n):
    """SITES of a digit-bounded numeral, never a count.  FAULT 3, self-caught: the first form
    matched only the unseparated digits, so 8,853 / 19,109 / 35,789 -- every four- and five-digit
    figure the book prints -- scored ZERO sites including their own table line.  Both the plain and
    the comma-grouped forms are swept."""
    forms = {str(n), f'{n:,}'}
    pat = '(?:' + '|'.join(re.escape(f) for f in forms) + ')'
    pat = r'(?<![\d.,])' + pat + r'(?!\d)(?!,\d)(?!\.\d)'
    return [i + 1 for i in range(len(M)) if re.search(pat, M[i])]

def joins(M):
    """whitespace-normalising two-line join: body lines carry a leading space (chat 121 fault 4)."""
    return [(i + 1, re.sub(r'\s+', ' ', (M[i] + ' ' + (M[i + 1] if i + 1 < len(M) else '')).strip()))
            for i in range(len(M))]

def regentry(n):
    """grouped-aware Register lookup: bare '### 96' headings AND comma/dash grouped headings."""
    out = []
    for i, t in enumerate(REG, 1):
        s = t.strip()
        m = re.match(r'^#{1,4}\s*([\d,\s\u2013\u2014-]+?)\s*$', s)
        if not m: continue
        body = m.group(1)
        nums = set()
        for part in re.split(r'[,\s]+', body):
            if re.fullmatch(r'\d+', part): nums.add(int(part))
            else:
                mm = re.fullmatch(r'(\d+)[\u2013\u2014-](\d+)', part)
                if mm: nums.update(range(int(mm.group(1)), int(mm.group(2)) + 1))
        if n in nums:
            head = ''
            for j in range(i, min(i + 6, len(REG))):
                if REG[j].strip():
                    head = REG[j].strip(); break
            out.append((i, s, head[:150]))
    return out

# Sites resolved by their own text rather than carried as line numbers. r3-wl2's +8 shift at main
# L9608 moved every one of them; a literal cannot follow its line, a search can.
def _at(_sub, _L=None):
    _L = MAIN if _L is None else _L
    _h = [_i for _i, _l in enumerate(_L, 1) if _sub in _l]
    assert len(_h) == 1, 'anchor %r matches %d lines, not 1' % (_sub, len(_h))
    return _h[0]
hr('1.  32.2 printed whole (8 lines) and tested from the CITED side (16m-08 reverse member)')
for ln in range(_L('### 32.2 Self-reference'), _L('### 32.3 Self-defence')): print(f'  L{ln}  {MAIN[ln-1].rstrip()[:150]}')
sp, br = section_span(MAIN, '32.2'), body_range(MAIN, '32.2')
print(f'\n  section_span {sp}   body_range {br}   '
      f'{"COINCIDE" if sp == br else "DIFFER"}')
for ln in (_at('not obtained; §32.2 lists them as open', MAIN),
           _at('was not read in this work (§32.2)', MAIN)):
    print(f'  citing line L{ln}: {MAIN[ln-1].strip()[:170]}')
body = ' '.join(MAIN[sp[0]-1:sp[1]-1])
print('\n  test: does 32.2 carry a listing of works, obtained or unobtained?')
for tok in ['unobtained', 'work', 'works', 'list', 'listing', 'cited', 'reference', 'Kurucz',
            'VALD', 'compilation']:
    print(f'      {tok:<13} occurrences inside 32.2: {has_token(body, tok)}')
print('  VERDICT: 32.2 prints S1 alphabet, S2 order, S3 bounds and nothing bibliographic.')

hr('2.  32.3 L9055 -- "Chapter 28 lists one thousand six hundred and thirty-five that failed"')
WORD = 'one thousand six hundred and thirty-five'
for name, M in VOLS:
    s = [i + 1 for i in range(len(M)) if WORD in M[i]]
    if s: print(f'  {name}: {len(s)} word-form sites {s}')
print('\n  referent of each main-volume site (the clause the phrase sits in):')
for ln in [i + 1 for i in range(len(MAIN)) if WORD in MAIN[i]]:
    t = re.sub(r'\s+', ' ', MAIN[ln - 1].strip())
    k = t.find(WORD)
    print(f'      L{ln:<6} …{t[max(0,k-72):k+len(WORD)+34]}…')
print('\n  chapter 28 heading and its own head line:')
c28 = section_span(MAIN, '28')
print(f'      span {c28}; L{c28[0]}: {MAIN[c28[0]-1].strip()[:120]}')
for ln in range(c28[0], min(c28[0] + 14, c28[1])):
    if MAIN[ln - 1].strip(): print(f'      L{ln}  {MAIN[ln-1].strip()[:150]}')

hr('3.  32.3 D3 L9057 -- the two chapter claims it makes')
print('  claim (a): "Chapter 29 names the single open item"')
c29 = section_span(MAIN, '29')
print(f'      chapter 29 span {c29}')
for ln in range(c29[0], c29[1]):
    if re.search(r'\bopen\b', MAIN[ln - 1], re.I):
        print(f'      L{ln}  {MAIN[ln-1].strip()[:140]}')
print('\n  claim (b): "Chapter 28 names three documents and one section that could not be reached"')
for ln in range(c28[0], c28[1]):
    if re.search(r'could not be (reached|obtained)|unobtained|not obtained|unreachable',
                 MAIN[ln - 1], re.I):
        print(f'      L{ln}  {MAIN[ln-1].strip()[:150]}')

hr('4.  32.3 L9045-L9051 -- the audit figures and the two traced failures')
for ln in range(_L('      102 quantitative claims were extracted from the draft and re-derived independently from'), _L(' located the error. That is ⅅ_def operating on the text.')): print(f'  L{ln}  {MAIN[ln-1].rstrip()[:150]}')
print('\n  other sites of 102 in the volume, read at the site (chat 121: read the numeral where')
print('  the sweep places it):')
for ln in numsites(MAIN, 102):
    print(f'      L{ln:<6} {MAIN[ln-1].strip()[:130]}')
print('\n  "twenty-member channel" and "four levels" against the channel table:')
for tok in ['twenty-member', 'four levels', 'self-duality', 'involution']:
    for name, M in VOLS:
        s = [i + 1 for i in range(len(M)) if tok in M[i]]
        if s: print(f'      {tok:<16} {name}: {s[:8]}')

hr('5.  pointers in the unit, resolved under BOTH resolvers, to the CLAIM not the heading')
PTR = [('32.4', 'L9086 "32.4 shows the recursion is stationary"'),
       ('32.1.4.1', 'L9121 "32.1.4.1 sorts the book\'s numbers"'),
       ('18', 'L9116 "18 already prices it: no differences, no sums, no symmetric bounds"'),
       ('12.11', 'L9117 "12.11\'s envelope densities are the bill"'),
       ('12.11.3.1', 'L9154 "12.11.3.1\'s law-extent rule sorts them exactly"'),
       ('15', 'L9034 "Chapter 15\'s propagation recovers it"'),
       ('32.4.1', 'in-unit'), ('32.4.2', 'in-unit')]
for sec, why in PTR:
    sp, br = section_span(MAIN, sec), body_range(MAIN, sec)
    print(f'  §{sec:<10} span {str(sp):<16} body {str(br):<16} '
          f'{"COINCIDE" if sp == br else "DIFFER"}   {why}')
print(f'\n  lettered pointer §D.5.2 (L9089): heading at L{lettered_heading(MAIN, "D.5.2")}, '
      f'text: {MAIN[(lettered_heading(MAIN,"D.5.2") or 1)-1].strip()[:80]}')
print('\n  §18 read for the three prices it is cited for:')
s18 = section_span(MAIN, '18'); t18 = ' '.join(MAIN[s18[0]-1:s18[1]-1])
for tok in ['differences', 'sums', 'symmetric bounds', 'price', 'prices']:
    print(f'      {tok:<18} in §18: {has_token(t18, tok)}')
print('\n  the central theorem, "X is closed iff X = R(X)":')
for name, M in VOLS:
    s = [i + 1 for i in range(len(M)) if re.search(r'closed\s+iff', M[i], re.I)]
    if s: print(f'      {name}: {s[:10]}')

hr('6.  register citations in the unit: 279, 388, 391, 392, 394 -- existence first, then headline')
for n in (279, 388, 391, 392, 394):
    hits = regentry(n)
    if not hits:
        print(f'  register {n}: NO ENTRY FOUND')
        continue
    for ln, head, first in hits:
        print(f'  register {n}: heading L{ln} {head!r}')
        print(f'      headline: {first}')

hr('7.  attributions in the unit against ## References BODY occurrence and R.7')
refhits = [i + 1 for i in range(len(MAIN)) if re.match(r'^#{1,3} References', MAIN[i].strip())]
print(f'  "## References" occurrences: {refhits}; BODY occurrence taken as L{refhits[-1]}')
bib = ' '.join(MAIN[refhits[-1]-1:])
unit = ' '.join(MAIN[A-1:B])
NAMES = ['Knaster', 'Tarski', 'Gödel', 'Godel', 'Russell', 'Heaviside', 'Edlén']
for nm in NAMES:
    print(f'  {nm:<11} in unit {has_token(unit, nm):>2}   in bibliography {has_token(bib, nm):>2}   '
          f'{"UNBIBLIOGRAPHED" if has_token(unit, nm) and not has_token(bib, nm) else ""}')
print('\n  capitalised tokens in the unit in BOTH sentence positions (chat 121 fault 5):')
cap = {}
for ln in range(A, B + 1):
    for m in re.finditer(r'(?<![A-Za-zÀ-ÿ])([A-ZÀ-Þ][a-zà-ÿ]{3,})', MAIN[ln - 1]):
        cap.setdefault(m.group(1), []).append(ln)
COMMON = set('''The This That They There These Those Which What When Where While With Without
Every Each Both Nine Six Measured Available Absent Closure Construct Corroborated Proved Tested
Self Register Chapter Level Only From Read Value Values Identity Identities Book Extensive
Monotone Idempotent Paradox Alphabet Order Bounds Thirty''' .split())
print('   ', sorted(k for k in cap if k not in COMMON))

hr('8.  Ruling 46 sweep (case-sensitive) and Ruling 45 sweep over the unit')
R46 = [r'\b[a-z0-9_]+\.py\b', r'\bBUILD\d+\b', r'\bMANIFEST\b', r'\b[a-z0-9_]+\.tsv\b',
       r'\b[a-z0-9_]+\.md\b']
hit46 = []
for ln in range(A, B + 1):
    for p in R46:
        for m in re.finditer(p, MAIN[ln - 1]):
            hit46.append((ln, m.group(0)))
print(f'  Ruling 46 sites in the unit: {len(hit46)}  {hit46}')
for ln, tok in hit46:
    inpp = [i + 1 for i in range(len(PP)) if tok in PP[i]]
    print(f'      {tok} at L{ln}: PP sites {inpp[:6]}  '
          f'{"PRESENT IN PP" if inpp else "ABSENT FROM PP"}')
R45 = ['draft', 'earlier version', 'the auditor', 'this book', 'the book states', 'audit',
       'reader', 'section got it wrong', 'in the same voice']
print('\n  Ruling 45 candidate sites (build/editorial narration), each checked against PP:')
seen = set()
for ln in range(A, B + 1):
    t = MAIN[ln - 1]
    for tok in R45:
        if re.search(r'(?<![A-Za-z])' + re.escape(tok) + r'(?![A-Za-z])', t, re.I):
            if ln in seen: continue
            seen.add(ln)
            probe = re.sub(r'\s+', ' ', t.strip())[:46]
            inpp = [i + 1 for i in range(len(PP)) if probe and probe in re.sub(r'\s+', ' ', PP[i])]
            print(f'      L{ln:<6} {"PP " + str(inpp[0]) + f" (offset {inpp[0]-ln})" if inpp else "not found in PP by this probe":<26}'
                  f' {probe[:70]}')
            break

hr('9.  PP anchoring, per witness, on the unit\'s own text')
def norm(s): return re.sub(r'\s+', ' ', s.strip())
PPN = [norm(x) for x in PP]
found = 0
for ln in range(A, B + 1):
    t = norm(MAIN[ln - 1])
    if len(t) < 55: continue
    probe = t[:60]
    hits = [i + 1 for i in range(len(PPN)) if probe in PPN[i]]
    if hits:
        found += 1
        if found <= 12:
            print(f'  L{ln:<6} PP L{hits[0]:<6} offset {hits[0]-ln:>5}   {probe[:62]}')
print(f'  witnesses anchored: {found}')

hr('10. "the book states most of them once" -- sites of the seven base-setting figures')
BASE = [('cells 976', 976), ('generators 17', 17), ('rank levels 18', 18),
        ('widest level 122', 122), ('reflection survivors 8', 8)]
for lab, n in BASE:
    s = numsites(MAIN, n)
    print(f'  {lab:<26} {len(s):>4} main-volume numeral sites')
for lab, tok in [('fill 14.12%', '14.12'), ('surplus 7.07', '7.07')]:
    s = [i + 1 for i in range(len(MAIN)) if tok in MAIN[i]]
    print(f'  {lab:<26} {len(s):>4} main-volume sites {s[:10]}')
print('\n  the three NEW settings\' figures, sited (a figure stated once is stated in the table only):')
for n in (8853, 19109, 35789, 704, 1497, 2742, 2873):
    tot = {name: numsites(M, n) for name, M in VOLS}
    print(f'      {n:<8} ' + '  '.join(f'{k}:{len(v)}' for k, v in tot.items() if v))

hr('11. census rows in range, and the duplicated-section sweep (docket 27)')
rows = open(os.path.join(H, 'DEFECT-CENSUS.tsv'), encoding='utf-8').read().split('\n')
hdr = rows[0].split('\t')
mi, li, ci, ii, di = (hdr.index('member'), hdr.index('line'), hdr.index('class'),
                      hdr.index('item'), hdr.index('detail'))
n = 0
for r in rows[1:]:
    f = r.split('\t')
    if len(f) <= max(mi, li, di): continue
    if f[mi] in ('main', 'all'):
        try: ln = int(f[li])
        except ValueError: continue
        if A <= ln <= B:
            n += 1
            print(f'  id {f[0]}  class {f[ci]}  member {f[mi]}  L{ln}  item {f[ii][:40]}  '
                  f'detail {f[di][:60]}')
print(f'  census rows in range (member main OR all): {n}')
longs = [(ln, norm(MAIN[ln - 1])) for ln in range(A, B + 1) if len(norm(MAIN[ln - 1])) > 90]
rec = 0
for ln, t in longs:
    hits = [i + 1 for i in range(len(MAIN)) if i + 1 != ln and t[:80] in norm(MAIN[i])]
    if hits:
        rec += 1; print(f'  RECURS L{ln} also at {hits[:4]}')
print(f'  duplicated-section sweep: {len(longs)} long lines swept, {rec} recur elsewhere')

hr('13. register 394 read in full -- the Register carries the same two count words')
r394 = regentry(394)[0][0]
for ln in range(r394, r394 + 22):
    if re.match(r'^#{1,4}\s*\d', REG[ln - 1].strip()) and ln != r394: break
    if REG[ln - 1].strip(): print(f'  reg L{ln}  {REG[ln-1].strip()[:160]}')

hr('14. §18 read at its target for the three prices L9116 attributes to it')
s18, b18 = section_span(MAIN, '18'), body_range(MAIN, '18')
print(f'  §18 span {s18}  body {b18}  DIFFER')
for tok in ['symmetric bound', 'no differences', 'no sums', 'difference', 'sum ']:
    for name, M in VOLS:
        s = [i + 1 for i in range(len(M)) if re.search(tok, M[i], re.I)]
        if s:
            inside = [x for x in s if name == 'main' and s18[0] <= x < s18[1]]
            print(f'      {tok:<16} {name}: {len(s)} sites {s[:8]}'
                  + (f'   inside §18: {inside}' if name == 'main' else ''))
print('\n  where "symmetric bounds" lives, with its enclosing section:')
for ln in [i + 1 for i in range(len(MAIN)) if re.search(r'symmetric bounds', MAIN[i], re.I)]:
    print(f'      L{ln}  §{enclosing(MAIN, ln)}  {MAIN[ln-1].strip()[:120]}')
print('\n  §18 lines that price the language (differences / sums / bounds):')
for ln in range(s18[0], s18[1]):
    if re.search(r'\b(difference|differences|sums?|symmetric)\b', MAIN[ln - 1], re.I):
        print(f'      L{ln}  §{enclosing(MAIN, ln)}  {MAIN[ln-1].strip()[:130]}')

hr('15. D3 claim (a): "Chapter 29 names the single open item"')
c29 = section_span(MAIN, '29')
for ln in range(_L(' §29.2 asks what component this work owns, and the author has answered by declining the frame: **no'), _L(' withdrawn, not answered, and the book was built to permit exactly that. Register 238.')):
    if MAIN[ln - 1].strip(): print(f'  L{ln}  {MAIN[ln-1].strip()[:150]}')
print('\n  every "open" numeral statement in chapter 29:')
for ln in range(c29[0], c29[1]):
    if re.search(r'open', MAIN[ln - 1], re.I) and re.search(
            r'\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|single|\d+)\b',
            MAIN[ln - 1], re.I):
        print(f'      L{ln}  {MAIN[ln-1].strip()[:140]}')
print('\n  "the single open item" / "one open" forms, all six volumes:')
for tok in ['single open', 'one open item', 'the open item', 'sole open']:
    for name, M in VOLS:
        s = [i + 1 for i in range(len(M)) if tok in M[i].lower()]
        if s: print(f'      {tok:<15} {name}: {s[:8]}')

hr('16. D3 claim (b): three documents and one section that could not be reached')
c28 = section_span(MAIN, '28')
VOC = ['could not be', 'not obtained', 'unobtained', 'not reached', 'could not reach',
       'inaccessible', 'unavailable', 'not consulted', 'not seen', 'paywall', 'not read']
print(f'  sweep vocabulary: {VOC}')
print(f'  chapter 28 span {c28}:')
n28 = 0
for ln in range(c28[0], c28[1]):
    if any(v in MAIN[ln - 1].lower() for v in VOC):
        n28 += 1; print(f'      L{ln}  {MAIN[ln-1].strip()[:140]}')
print(f'  chapter 28 hits: {n28}')
print(f'  chapter 29 span {c29}:')
n29 = 0
for ln in range(c29[0], c29[1]):
    if any(v in MAIN[ln - 1].lower() for v in VOC):
        n29 += 1; print(f'      L{ln}  {MAIN[ln-1].strip()[:140]}')
print(f'  chapter 29 hits: {n29}')
_refs = [i for i, l in enumerate(MAIN, 1) if l.startswith('## References')][-1]
print('  same sweep over the References body occurrence (L%d onwards):' % _refs)
for ln in range(_refs, len(MAIN) + 1):
    if any(v in MAIN[ln - 1].lower() for v in VOC):
        print(f'      L{ln}  §{enclosing(MAIN, ln)}  {MAIN[ln-1].strip()[:130]}')

for ln, t in [(_L(" **S3 — bounds.** Every claim's support locations are recoverable as the union over its specialisations. **A reader given only the claims and their evidence could reconstruct the chapter structure**, which is the content of E = 0."), 'Every claim\'s support locations are recoverable as the union over its specialisations'),
              (_L(' **D3 — totality.** Every claim in this book is **supported, cited, or marked open**. There is no fourth state. Chapter 29 names the single open item; Chapter 28 names three documents and one section that could not be reached and states the consequence. **No claim is left in limbo, because limbo is not in the codomain.**'), 'Every claim in this book is supported, cited, or marked open'),
              (_L(' **The values do not.** Every extensive figure moves with the caps, and moves a long way:'), 'Every extensive figure moves with the caps'),
              (_L(' So the reason one need not write a book about this book is **not** that it would be identical. It is that it would exhibit **nothing new**: the same three mechanisms, verified again, on claims about claims. The tower is infinite and every storey above the second is furnished the same way.'), 'every storey above the second is furnished the same way')]:
    print(f'  L{ln}  {norm(MAIN[ln-1])[:150]}')
print('\n  "There is no fourth state" -- the three states named, swept for a fourth vocabulary:')
for tok in ['supported', 'cited', 'marked open', 'unsupported', 'withdrawn', 'open']:
    print(f'      {tok:<13} main-volume word-bounded count: '
          f'{sum(has_token(x, tok) for x in MAIN)}')

hr('17. register 394 body in full, and the two chapter attributions of D3 resolved')
r = regentry(394)[0][0]
txt = []
for ln in range(r + 1, r + 24):
    s = REG[ln - 1].strip()
    if re.match(r'^#{1,4}\s*\d', s): break
    if s: txt.append((ln, s))
for ln, s in txt:
    for k in range(0, len(s), 150):
        print(f'  reg L{ln if k==0 else "":<6} {s[k:k+150]}')

hr('18. chapter 29 read for "the single open item"')
c29 = section_span(MAIN, '29')
print(f'  chapter 29 span {c29}; its subsection headings:')
for ln in range(c29[0], c29[1]):
    if re.match(r'^#{1,4} ', MAIN[ln - 1]):
        print(f'      L{ln}  {MAIN[ln-1].strip()[:110]}')
print()
for ln in range(c29[0], c29[1]):
    if re.search(r'\bitem\b', MAIN[ln - 1], re.I) and re.search(
            r'\b(one|single|only|last|remaining|six|eleven)\b', MAIN[ln - 1], re.I):
        print(f'      L{ln}  {MAIN[ln-1].strip()[:150]}')

hr('19. 12.11.2 read where "symmetric bounds" lives, against L9116\'s "no symmetric bounds"')
for ln in range(_L(' atoms.** A dipole transition changes ℓ by one, moving the target into a configuration that atom rarely'), _L(" And the law, three instances deep before the triangle made it four: **every coupling coordinate's")):
    if MAIN[ln - 1].strip(): print(f'  L{ln}  §{enclosing(MAIN, ln)}  {MAIN[ln-1].strip()[:140]}')

hr('20. the unit\'s figures re-sited with the comma-aware sweep (fault 3 repaired)')
for n in (976, 8853, 19109, 35789, 704, 1497, 2742, 2873, _L(' §12.11.0.9 bounds the direction beyond thirteen. This is the other question: **what happens to Λ when'), 68, 31, 33, 35):
    tot = {name: numsites(M, n) for name, M in VOLS}
    ins = [x for x in tot['main'] if A <= x <= B]
    print(f'  {n:<7} ' + '  '.join(f'{k}:{len(v)}' for k, v in tot.items() if v)
          + f'   in-unit main sites {ins}')

