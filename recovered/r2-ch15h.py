#!/usr/bin/env python3
"""r2-ch15h — computable batch for main L7458-L7558 (§28.6, §28.7, §28.7.1, §28.7.2).

Chat 107.  Imports heading_line / section_span / has_token / enclosing from r2lib by path;
copies nothing; reads MEMBERS, never a bundle; passes the resolvers the LINE LIST.
Rounding is Decimal.quantize with the convention named at each site; round() is never used.

Fault log (self-caught, rewritten before banking):
  * F1 first form spanned §28.7 with section_span, which INCLUDES subsections by design, so the
    section swallowed §28.7.1-§28.7.9 and counted 106 numerals against a heading saying six.  A
    heading numeral governs its OWN body, so the body range is heading -> next heading of any rank.
  * F2 first form assumed the pre-closure items were numbered 1..48 and took max() of an empty
    list.  MEASURED: §28.1-§28.5 print their items unnumbered — bold-lead paragraphs and bullets —
    and the printed numbering starts at 49.  The population is measured here, not assumed.
"""
import importlib.util, os, re
from decimal import Decimal, ROUND_HALF_EVEN, ROUND_DOWN

H = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(_s); _s.loader.exec_module(r2lib)
heading_line, section_span, has_token, enclosing = (
    r2lib.heading_line, r2lib.section_span, r2lib.has_token, r2lib.enclosing)

VOL = {'main': 'The_Method_1_6-2.md',
       'reg': 'The_Method_1_6___The_Register-2.md',
       'mc': 'The_Method_1_6___Mathematical_Compendium-2.md',
       'pc': 'The_Method_1_6___The_Physics_Compendium-2.md',
       'ioi': 'The_Method_1_6___The_Index_of_Indices-2.md',
       'sc': 'The_Method_1_6___Spectra_Compendium-2.md'}
M = {k: r2lib.read_member(v).split('\n') for k, v in VOL.items()}
main = M['main']
HEAD = re.compile(r'^#{1,6}\s')

# owed to r2lib (DEFERRED): body range of a heading EXCLUDING its subsections.
def body_range(lines, sec):
    h = heading_line(lines, sec)
    if h is None:
        return None
    for i in range(h + 1, len(lines) + 1):
        if HEAD.match(lines[i - 1]):
            return (h + 1, i - 1)
    return (h + 1, len(lines))

# owed to r2lib (DEFERRED): digit-bounded numeral sweep.  has_token is letter-bounded and reads
# 129 out of 1129; a numeral needs digit bounds on both sides and must not match inside 3.129.
def numsites(lines, s):
    pat = r'(?<![\d.,])' + re.escape(s) + r'(?![\d])'
    return [i for i, t in enumerate(lines, 1) if re.search(pat, t)]

def allsites(s):
    return {k: numsites(M[k], s) for k in VOL}

def total(d):
    return sum(len(v) for v in d.values())

ITEM = re.compile(r'^\s*(?:\*\*)?(\d+)(?:[\u2013\u2014-](\d+))?\.\s')
def items(lines, lo, hi):
    out = []
    for i in range(lo, hi + 1):
        m = ITEM.match(lines[i - 1])
        if m:
            a = int(m.group(1)); b = int(m.group(2)) if m.group(2) else a
            out.append((a, b, i))
    return out

print('r2-ch15h — main L7458-L7558 (§28.6-§28.7.2), computable')
print('=' * 96)

# ---------------------------------------------------------------- F0 extent, re-measured here
for s in ('28.6', '28.7', '28.7.1', '28.7.2', '28.7.3', '28', '29'):
    print(f'F0  heading §{s:<7} body line {heading_line(main, s)}  body range {body_range(main, s)}')
print(f'F0  unit L7458-L7558 = {7558 - 7458 + 1} lines; enclosing(7558) = {enclosing(main, 7558)}')

# ---------------------------------------------------------------- F1 item counts vs heading numerals
print('-' * 96)
WORD = {'28.7': ('Six', 6), '28.7.1': ('Eight', 8), '28.7.2': ('Twelve', 12)}
for sec, (word, n) in WORD.items():
    lo, hi = body_range(main, sec)
    it = items(main, lo, hi)
    nums = [v for a, b, _ in it for v in range(a, b + 1)]
    print(f'F1  §{sec:<7} body L{lo}-L{hi} | heading says {word:<6} ({n:>2}) | item lines {len(it)} | '
          f'numerals {len(nums)} {nums} | {"MATCH" if len(nums) == n else "MISMATCH"}')

ch_lo, ch_hi = section_span(main, '28')
allit = items(main, ch_lo, ch_hi)
byn = {}
for a, b, ln in allit:
    for v in range(a, b + 1):
        byn.setdefault(v, []).append(ln)
dups = {v: l for v, l in byn.items() if len(l) > 1}
print(f'F1  chapter 28 span L{ch_lo}-L{ch_hi}: {len(allit)} item lines, {len(byn)} distinct numerals, '
      f'range {min(byn)}-{max(byn)}')
print(f'F1  DUPLICATE numerals: {dups if dups else "none"}')
for v, lns in dups.items():
    for ln in lns:
        print(f'      {v} @ L{ln} in §{enclosing(main, ln)}: {main[ln-1].strip()[:76]}')
post = sorted(v for v in byn if 49 <= v <= 74)
print(f'F1  post-closure numerals 49-74 present {len(post)}/26; '
      f'gaps {[v for v in range(49, 75) if v not in byn] or "none"}')

# where the numerals 1-48 the text presupposes actually live, if anywhere
print('-' * 96)
low = {}
for k in VOL:
    hits = [(a, b, ln) for a, b, ln in items(M[k], 1, len(M[k])) if b <= 48]
    low[k] = hits
    print(f'F1b {k:<5} lines matching an item form with numeral <= 48: {len(hits)}')
pre_ch28 = [x for x in allit if x[1] <= 48]
print(f'F1b in chapter 28 itself: {len(pre_ch28)} — the chapter prints no numerals below 49')
for k in ('reg', 'mc', 'pc', 'ioi', 'sc'):
    wl = [ln for a, b, ln in low[k] if any('ithdraw' in (M[k][j - 1]) for j in range(max(1, ln - 40), ln))]
    print(f'F1b {k:<5} of those, within 40 lines below a line naming a withdrawal: {len(wl)} {wl[:8]}')

# ---------------------------------------------------------------- F2 §28.6 distribution table
print('-' * 96)
lo6, hi6 = body_range(main, '28.6')
ROW = re.compile(r'^\s{2,}(\S.*?)\s{2,}(~?\d+)\s{2,}(\S.*)$')
rows = [(m.group(1).strip(), m.group(2), m.group(3).strip())
        for i in range(lo6, hi6 + 1) for m in [ROW.match(main[i - 1])] if m]
vals = [int(c.lstrip('~')) for _, c, _ in rows]
print(f'F2  §28.6 body L{lo6}-L{hi6}; table rows parsed {len(rows)}; counts {[c for _, c, _ in rows]}')
print(f'F2  sum of counts = {sum(vals)} (each "~n" read as n); '
      f'approximate rows {[a for a, c, _ in rows if c.startswith("~")]}')
# MEASURED populations the table could be sorting
b2 = body_range(main, '28.2'); b3 = body_range(main, '28.3'); b4 = body_range(main, '28.4')
bold2 = [i for i in range(b2[0], b2[1] + 1) if main[i - 1].lstrip().startswith('**')]
bull3 = [i for i in range(b3[0], b3[1] + 1) if main[i - 1].lstrip().startswith('\u2022')]
bold4 = [i for i in range(b4[0], b4[1] + 1) if main[i - 1].lstrip().startswith('**')]
print(f'F2  printed pre-closure items MEASURED: §28.2 bold-lead {len(bold2)} (+1 unbolded lead L{b2[0]}), '
      f'§28.3 bullets {len(bull3)}, §28.4 bold-lead {len(bold4)} (incl. policy line)')
print(f'F2  candidate populations: printed-in-chapter 5+8+6 = 19; "the first forty-eight" = 48; '
      f'post-closure 49-74 = 26; table sum = {sum(vals)}')
for pop in (19, 26, 48):
    print(f'F2  table sum {sum(vals)} vs {pop}: {"MATCH" if sum(vals) == pop else "MISMATCH by %+d" % (sum(vals) - pop)}')
rd = [c for a, c, _ in rows if a == 'a reader']
print(f'F2  reader row {rd}; L7474 "Zero were caught by a reader" consistent: {rd == ["0"]}')
print(f'F2  "forty-eight" sites in main: {[i for i, t in enumerate(main, 1) if "forty-eight" in t.lower()]}')

# ---------------------------------------------------------------- F3 item 50's 2.2% rise
print('-' * 96)
seq = [Decimal('366.3'), Decimal('367.9'), Decimal('370.6'), Decimal('374.5')]
rise = (seq[-1] - seq[0]) / seq[0] * 100
q = {n: rise.quantize(Decimal('0.1'), rounding=m) for n, m in
     (('HALF_EVEN', ROUND_HALF_EVEN), ('DOWN', ROUND_DOWN))}
print(f'F3  (374.5-366.3)/366.3 = {rise} % -> {q} vs printed 2.2 % : '
      f'{"MATCH under both conventions" if set(q.values()) == {Decimal("2.2")} else "CHECK"}')
print(f'F3  monotone increasing over h=1..4: {all(seq[i] < seq[i+1] for i in range(3))}; '
      f'steps {[str(seq[i+1]-seq[i]) for i in range(3)]}')

# ---------------------------------------------------------------- F4/F5 stated arithmetic
print('-' * 96)
print(f'F4  item 61 "six relations reduce to eight generators, so -2 were redundant": 6-8 = {6-8} '
      f'-> {"MATCH" if 6 - 8 == -2 else "MISMATCH"}')
print(f'F5  item 62: Lambda_8 = 976 (core gate, tower-2): 976-8 = {976-8} vs printed 968 -> '
      f'{"MATCH" if 976 - 8 == 968 else "MISMATCH"}')
print(f'F5  item 62: F(-1) = +2, self-dual contribution +8 -> remainder {2-8} vs printed -6 -> '
      f'{"MATCH" if 2 - 8 == -6 else "MISMATCH"}')

# ---------------------------------------------------------------- F6 item 65, the closed form of V
print('-' * 96)
dw = lambda h, v: h * (h * h - 3 * v * v)
dr = lambda h, v: h * (3 * v * v - h * h)
bad = [(h, v) for h in range(1, 5) for v in range(1, 81) if v > h and dw(h, v) >= 0]
print(f'F6  h(h^2-3nu^2) >= 0 anywhere with nu > h (h=1..4, nu=1..80): '
      f'{bad if bad else "never — negative throughout, as item 65 states"}')
print(f'F6  4nu^3/(h(3nu^2-h^2)) = -(printed form) identically: '
      f'{all(dr(h, v) == -dw(h, v) for h in range(1, 5) for v in range(1, 81))}')
lo4, hi4 = section_span(main, '23.4')
vl = [i for i in range(lo4, hi4) if '4\u03bd' in main[i - 1]]
print(f'F6  §23.4 span L{lo4}-L{hi4}; lines printing 4nu: {vl}')
for i in vl[:4]:
    print(f'      L{i}: {main[i-1].strip()[:100]}')
print(f'F6  main L6237: {main[6236].strip()[:100]}')

# ---------------------------------------------------------------- F7 items 53/54 unit artefact
print('-' * 96)
for s in ('8 \u00d7 10\u00b3', '5 \u00d7 10\u2075', '10\u2076', '129'):
    d = allsites(s)
    print(f'F7  "{s}" sites {total(d)}: ' + ('; '.join(f'{k} {v}' for k, v in d.items() if v) or 'ABSENT'))
lo56, hi56 = section_span(main, '25.6')
r256 = [i for i in range(lo56, hi56) if 'n\u00b3' in main[i - 1] or '2\u03b4' in main[i - 1]]
print(f'F7  §25.6 span L{lo56}-L{hi56}; lines carrying n^3 or 2delta: {r256[:8]}')
for i in r256[:3]:
    print(f'      L{i}: {main[i-1].strip()[:100]}')

# ---------------------------------------------------------------- F8 single-witness sweep
print('-' * 96)
for s in ('0.9934', '0.9812', '366.3', '374.5', '220', '340', '129', '30 of 30', '60 cells', '968'):
    d = allsites(s); t = total(d)
    tag = '  SINGLE WITNESS' if t == 1 else ('  ABSENT' if t == 0 else '')
    print(f'F8  "{s:<9}" sites {t:>3}{tag}  | ' + '; '.join(f'{k} {v[:6]}' for k, v in d.items() if v))

# ---------------------------------------------------------------- F9 unterminated items
print('-' * 96)
TERM = tuple('.!?:\u201d")')
starts = [ln for _, _, ln in allit]
bad = []
for k, ln in enumerate(starts):
    end = starts[k + 1] - 1 if k + 1 < len(starts) else ch_hi - 1
    body = [main[j - 1].rstrip() for j in range(ln, min(end, ch_hi) + 1)]
    body = [b for b in body if b.strip() and not HEAD.match(b.lstrip())]
    if not body:
        continue
    last = body[-1].rstrip('*').rstrip()
    if last and not last.endswith(TERM):
        bad.append((ln, last[-56:]))
print(f'F9  chapter-28 numbered items whose final body line lacks terminal punctuation: {len(bad)}')
for ln, tail in bad:
    print(f'      L{ln} §{enclosing(main, ln)}  ...{tail}')
print('=' * 96)
