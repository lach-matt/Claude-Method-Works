#!/usr/bin/env python3
"""r2-ch15j — computable batch for the chat-108 section read: main §28.7.3, L7559-L7643.

Imports heading_line, section_span, has_token, enclosing from r2lib by path; copies nothing.
Resolvers are passed the LINE LIST, never the member text.

Owed to r2lib (provenance comments, per DEFERRED):
  body_range(M, sec) - heading -> next heading of ANY rank.  section_span INCLUDES subsections and
    made chat 107 count 106 numerals against a heading saying six.  The two are NOT
    interchangeable: a SECTION body needs body_range, a CHAPTER sweep needs section_span.  Using
    body_range for chapter 28 returned 20 lines and zero items (fault F3, chat 108).
  digits(text, n)    - digit-bounded numeral sweep.  has_token is letter-bounded and reads 129
    out of 1129.
  join2(M)           - two-line-join phrase sweep.  'the first forty-eight' is wrapped across
    L7482-83 and a raw per-line sweep misses it.

F2 fault, chat 108: taking the first number word in the head line reads 'one anomaly', 'two
guards', 'one hour' as count words.  The corrected test prints EVERY number word in the head
sentence with its context and compares each against the span; the reading is done by hand.
"""
import importlib.util, re
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

MEM = '/home/claude/members/'
spec = importlib.util.spec_from_file_location('r2lib', MEM + 'r2lib.py')
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
heading_line, section_span = r2lib.heading_line, r2lib.section_span
has_token, enclosing = r2lib.has_token, r2lib.enclosing

VOL = {'main': 'The_Method_1_6-2.md',
       'reg': 'The_Method_1_6___The_Register-2.md',
       'mc': 'The_Method_1_6___Mathematical_Compendium-2.md',
       'pc': 'The_Method_1_6___The_Physics_Compendium-2.md',
       'ioi': 'The_Method_1_6___The_Index_of_Indices-2.md',
       'sc': 'The_Method_1_6___Spectra_Compendium-2.md'}
LINES = {k: open(MEM + v, encoding='utf-8').read().split('\n') for k, v in VOL.items()}
M = LINES['main']


def body_range(Ms, sec):
    """OWED TO r2lib. Heading -> next heading of ANY rank (section_span includes subsections)."""
    s = heading_line(Ms, sec)
    if s is None:
        return None
    for i in range(s + 1, len(Ms) + 1):
        if re.match(r'^#{1,6}\s', Ms[i - 1]):
            return (s, i)
    return (s, len(Ms) + 1)


def digits(text, n):
    """OWED TO r2lib. Digit-bounded numeral count; sweeps comma and comma-free forms."""
    forms = {str(n)} | ({f'{n:,}'} if isinstance(n, int) else set())
    return sum(len(re.findall(r'(?<!\d)' + re.escape(f) + r'(?!\d)', text)) for f in forms)


def join2(Ms, a, b):
    """OWED TO r2lib. Two-line joins over [a,b), so a wrapped phrase is visible."""
    return [(i, (Ms[i - 1].strip() + ' ' + Ms[i].strip())) for i in range(a, min(b, len(Ms)))]


print('=' * 78)
print('r2-ch15j  computable batch  main SS28.7.3')
print('=' * 78)

br = body_range(M, '28.7.3')
ch = section_span(M, '28')
print(f'F0  body_range(28.7.3) = {br}   lines {br[1]-br[0]}   '
      f'section_span(28.7.3) = {section_span(M,"28.7.3")}')
print(f'F0  section_span(28) = {ch}   body_range(28) = {body_range(M,"28")}   '
      f'heading_line(28.7.2)={heading_line(M,"28.7.2")} (28.7.4)={heading_line(M,"28.7.4")}')
A, B = br[0], br[1]
UNIT = '\n'.join(M[A - 1:B - 1])
print(f'F0  heading text: {M[A-1][4:]!r}')

# ---------------------------------------------------------------- F1 item inventory
ITEM = re.compile(r'^\s*\*{0,2}(\d+)(?:\s*[\u2013\u2014-]\s*(\d+))?\.\s')
items = []
for i in range(A + 1, B):
    m = ITEM.match(M[i - 1])
    if m:
        lo = int(m.group(1)); hi = int(m.group(2)) if m.group(2) else lo
        items.append((i, lo, hi, M[i - 1].strip()[:60]))
print('\nF1  item heads printed in SS28.7.3')
covered = []
for ln, lo, hi, t in items:
    covered += list(range(lo, hi + 1))
    print(f'    L{ln}  {lo}-{hi} span {hi-lo+1:>2}  {t}')
uniq = sorted(set(covered))
dups = sorted({x for x in covered if covered.count(x) > 1})
gaps = [n for n in range(min(uniq), max(uniq) + 1) if n not in uniq]
print(f'    numerals covered {len(covered)}, distinct {len(uniq)}, min {min(uniq)} max {max(uniq)}')
print(f'    duplicated within the section: {dups}')
print(f'    span {min(uniq)}-{max(uniq)} = {max(uniq)-min(uniq)+1}; MISSING {len(gaps)}: {gaps}')
print(f'    heading says "Seventy-five more ... all printed": span==75 {max(uniq)-min(uniq)+1==75}'
      f'; distinct printed {len(uniq)}; blocks {len(items)}; "all printed" {not gaps}')

# ---------------------------------------------------------------- F2 count words in head sentences
WORD = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
        'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14,
        'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19,
        'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'seventy-five': 75}
print('\nF2  every number word in each block head, with context (read by hand)')
for ln, lo, hi, t in items:
    body = M[ln - 1].strip()
    head = re.split(r'(?<=[.!?])\s', re.sub(r'^\s*\*{0,2}\d+(?:\s*[\u2013\u2014-]\s*\d+)?\.\s*', '', body))[0]
    found = []
    for k, v in WORD.items():
        for mm in re.finditer(r'(?<![A-Za-z-])' + k + r'(?![A-Za-z-])', head, re.I):
            s = max(0, mm.start() - 14); found.append((v, head[s:mm.end() + 16]))
    span = hi - lo + 1
    print(f'    L{ln}  {lo}-{hi} span {span:>2}')
    if not found:
        print(f'          no number word in the head sentence: {head[:70]!r}')
    for v, ctx in found:
        print(f'          {v:>2} {"==" if v == span else "!="} span   ...{ctx!r}')

# ---------------------------------------------------------------- F3 chapter-wide duplicates
print('\nF3  duplicate item numerals across the whole of chapter 28 (section_span)')
call = {}
for i in range(ch[0] + 1, ch[1]):
    m = ITEM.match(M[i - 1])
    if m:
        lo = int(m.group(1)); hi = int(m.group(2)) if m.group(2) else lo
        for n in range(lo, hi + 1):
            call.setdefault(n, []).append(i)
cd = {n: v for n, v in call.items() if len(v) > 1}
print(f'    numerals seen in chapter 28: {len(call)}  range {min(call)}-{max(call)}')
for n in sorted(cd):
    print(f'    numeral {n} printed at {["L%d" % x for x in cd[n]]}')
chgaps = [n for n in range(min(call), max(call) + 1) if n not in call]
print(f'    chapter-wide gaps ({len(chgaps)}): {chgaps}')

# ---------------------------------------------------------------- F4 junctions
print('\nF4  junction with the neighbouring sections')
for tag in ('28.7.2', '28.7.4'):
    rr = body_range(M, tag); ns = []
    for i in range(rr[0] + 1, rr[1]):
        m = ITEM.match(M[i - 1])
        if m:
            lo = int(m.group(1)); hi = int(m.group(2)) if m.group(2) else lo
            ns += list(range(lo, hi + 1))
    print(f'    SS{tag} {rr}  numerals {min(ns)}-{max(ns)}  distinct {len(set(ns))}  '
          f'head {M[rr[0]-1][4:58]!r}')

# ---------------------------------------------------------------- F5 closing-note arithmetic
print('\nF5  arithmetic of the closing notes')
print(f'    L7573-75  eleven + four = {11+4} against "the last fifteen"  {11+4==15}')
print(f'    L7579-80  "of the last twenty, fifteen in test harnesses": 15<=20 {15<=20}; '
      f'delta on the note four lines above: corrections +{20-15}, harnesses +{15-11}, book +{5-4}')
print(f'    L7626-27  ten + seven = {10+7} against "seventeen"  {10+7==17}')
print(f'    L7620-24  ten bounds + (four + one + one + one) = {10+4+1+1+1} against span '
      f'{139-123+1}  {10+4+1+1+1==17}')
print(f'    145-149 span {149-145+1}; L7641 "five lists in one chapter"')

# ---------------------------------------------------------------- F6 the Pareto factor
print('\nF6  SS31.3 Pareto: 473.8 million against 495,515, "wrong by a factor of 956"')
r = Decimal('473800000') / Decimal('495515')
print(f'    exact ratio = {r}')
for name, mode in (('HALF_UP', ROUND_HALF_UP), ('HALF_EVEN', ROUND_HALF_EVEN)):
    print(f'    quantize to 1 ({name}) = {r.quantize(Decimal("1"), rounding=mode)}')
print(f'    495,515 x 956 = {495515*956:,}  (printed 473,800,000; delta {473800000-495515*956:,})')

# ---------------------------------------------------------------- F7 ratios and shares
print('\nF7  the printed ratios')
for a, b, what in ((241, 570, 'ratios below 1 on the order axis'), (13, 140, 'one-sided slackening'),
                   (1, 7, 'global slackening'), (2, 8, 'objects indexed in each'),
                   (35, 35, 'stated equations audited'), (200, 200, 'refuses / admits'),
                   (11, 15, 'in test harnesses, first note'), (15, 20, 'in test harnesses, second')):
    q = (Decimal(a) / Decimal(b) * 100).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
    print(f'    {a} of {b} = {q}%   {what}')
print(f'    0.606 against the ten-invariant best 0.31: ratio '
      f'{(Decimal("0.606")/Decimal("0.31")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)}')
print(f'    out-of-sample errors printed: 652%, 560%, 1,156% = 3 figures for 4 named rules')

# ---------------------------------------------------------------- F8 tower figures
print('\nF8  the tower figures the section leans on')
try:
    L8 = r2lib.L8_at((3, 3, 1, 3, 1))
    n8 = len(L8)
    print(f'    |Lambda_8| measured = {n8:,}   section prints 976  {n8==976}')
    print(f'    1,548 against {n8}: excess {1548-n8} cells, ratio '
          f'{(Decimal(1548)/Decimal(n8)).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)}')
    print(f'    "deleted all 75 added cells and returned to Lambda": {n8} + 75 = {n8+75}')
except Exception as e:
    print(f'    L8_at unavailable: {type(e).__name__}: {e}')
print(f'    "Seven constraints, six clustered, one extreme": 6+1 = {6+1}  {6+1==7}')
print(f'    "min(q, 4f+2)" at f in 0..f_max=1: bound takes {[4*f+2 for f in range(0,2)]}')

# ---------------------------------------------------------------- F9 terminal punctuation
print('\nF9  final line of every item block in SS28.7.3 (DEF-107 item 2 class)')
bounds = [ln for ln, _, _, _ in items] + [B]
for k in range(len(items)):
    tail = [j for j in range(bounds[k], bounds[k + 1]) if M[j - 1].strip()]
    last = tail[-1]; txt = M[last - 1].rstrip()
    ok = txt.endswith(('.', '!', '?', '.**', '.*', ':', '**'))
    print(f'    item {items[k][1]}-{items[k][2]:<3} last non-blank L{last}  '
          f'{"OK " if ok else "NO "} ...{txt[-46:]!r}')

# ---------------------------------------------------------------- F10 repeated content
print('\nF10  repeated content inside SS28.7.3 (sentence-level, normalised)')
def norm(s):
    s = re.sub(r'[*_`]', '', s).lower()
    s = re.sub(r'[^a-z0-9 ]', ' ', s)
    return ' '.join(s.split())
sent = []
for i in range(A, B):
    for piece in re.split(r'(?<=[.!?]) ', M[i - 1].strip()):
        n = norm(piece)
        if len(n.split()) >= 6:
            sent.append((i, n))
seen = {}
for i, n in sent:
    seen.setdefault(n, []).append(i)
rep = {n: v for n, v in seen.items() if len(v) > 1}
print(f'    normalised sentences of >=6 words: {len(sent)}; exact repeats: {len(rep)}')
for n, v in rep.items():
    print(f'    L{v}  {n[:96]}')
for k, why in (('tree factorisation harness that dropped two guards', 'item 89 vs third of 90-92'),
               ('1 548 against 976', 'the 1,548 figure'),
               ('e x 0 means it is not closed', 'items 110-111 vs 119-122'),
               ('re coordinatisation offered as a repair', 'items 110-111 vs 119-122'),
               ('0 became 27', 'items 110-111 vs 119-122'),
               ('a sentence written past the number beside it', 'the two register notes')):
    raw = [i for i in range(A, B) if k in norm(M[i - 1])]
    print(f'    {k!r}: L{raw}   [{why}]')

# ---------------------------------------------------------------- F11 numeral sites
print('\nF11  digit-bounded sites of the unit\'s figures, all six volumes')
for n in (1548, 976, 1156, 652, 560, 241, 570, 593, 956, 495515, 27, 606, 31):
    row = {k: digits('\n'.join(v), n) for k, v in LINES.items()}
    print(f'    {n:>8}  in-unit {digits(UNIT, n):>2}  ' + '  '.join(f'{k}={row[k]}' for k in VOL))
for s in ('71.8', '0.606', '0.31', '473.8', '3.2', '0.24'):
    row = {k: len(re.findall(r'(?<![\d.])' + re.escape(s) + r'(?![\d])', '\n'.join(v)))
           for k, v in LINES.items()}
    print(f'    {s:>8}  in-unit {len(re.findall(chr(40)+"?<![0-9.])"+re.escape(s)+r"(?![0-9])", UNIT)):>2}  '
          + '  '.join(f'{k}={row[k]}' for k in VOL))

# ---------------------------------------------------------------- F12 wrapped-phrase sweep
print('\nF12  two-line-join sweep for the unit\'s counted phrases')
J = join2(M, A, B)
for ph in ('of the last fifteen corrections', 'of the last twenty corrections', '35 of 35',
           'ten of the seventeen', 'six of these', 'one of these', 'five lists in one chapter',
           'all printed', 'the worst of them is 125', 'the other seven'):
    raw = [i for i in range(A, B) if ph.lower() in M[i - 1].lower()]
    jn = [i for i, t in J if ph.lower() in t.lower()]
    print(f'    {ph!r:36}  raw L{raw}  join L{jn}')
print('\nEND r2-ch15j')
