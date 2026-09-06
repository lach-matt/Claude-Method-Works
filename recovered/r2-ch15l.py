#!/usr/bin/env python3
# r2-ch15l — chat 109, computable batch for main L7644–L7720 (§28.7.4 … §28.7.9).
# Resolvers imported from r2lib by path; nothing copied except the three functions
# r2lib still owes (body_range, digit-bounded numeral sweep, two-line join), which
# carry provenance comments per DEFERRED.
import sys, os, re, importlib.util
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

H = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
heading_line, section_span, has_token = r2lib.heading_line, r2lib.section_span, r2lib.has_token

VOL = {
 'main': 'The_Method_1_6-2.md',
 'reg':  'The_Method_1_6___The_Register-2.md',
 'mc':   'The_Method_1_6___Mathematical_Compendium-2.md',
 'pc':   'The_Method_1_6___The_Physics_Compendium-2.md',
 'ioi':  'The_Method_1_6___The_Index_of_Indices-2.md',
 'sp':   'The_Method_1_6___Spectra_Compendium-2.md',
}
def lines(tag):
    return open(os.path.join(H, VOL[tag]), encoding='utf-8').read().split('\n')
M = {t: lines(t) for t in VOL}
PP = open('/home/claude/PP_The_Method_1_6.md', encoding='utf-8').read().split('\n')

# --- owed to r2lib: heading -> next heading of ANY rank (a section BODY, not a chapter) ---
def body_range(L, sec):
    ln = heading_line(L, sec)
    if ln is None: return None
    for j in range(ln, len(L)):
        if re.match(r'^#{1,6}\s', L[j]): return (ln, j + 1)   # 1-based, end exclusive
    return (ln, len(L) + 1)

# --- owed to r2lib: digit-bounded numeral sweep (has_token is letter-bounded: reads 129 in 1129) ---
def numeral_sites(L, n, lo=1, hi=None):
    hi = hi or len(L); pat = re.compile(r'(?<!\d)%d(?!\d)' % n)
    return [i for i in range(lo, hi + 1) if i <= len(L) and pat.search(L[i - 1])]

# --- owed to r2lib: two-line join phrase sweep ---
def phrase_sites(L, phrase):
    p = re.sub(r'\s+', ' ', phrase.lower()); out = []
    for i in range(1, len(L) + 1):
        raw = re.sub(r'\s+', ' ', L[i - 1].lower())
        if p in raw: out.append((i, 'line')); continue
        if i < len(L):
            j = re.sub(r'\s+', ' ', (L[i - 1] + ' ' + L[i]).lower())
            if p in j: out.append((i, 'join'))
    return out

U0, U1 = 7644, 7720                  # the unit, MEASURED by heading scan this chat
CH0, CH1 = 7366, 7855                # chapter 28 body, less the misplaced §28.10
X0, X1 = 8222, 8237                  # §28.10, printed inside chapter 29 (15f-05)
P = print

P('== A. section bodies and their printed item numerals ==')
ITEM = re.compile(r'^\s*(\d+)(?:\s*[–-]\s*(\d+))?\.\s')
SECS = ['28.7.4', '28.7.5', '28.7.6', '28.7.7', '28.7.8', '28.7.9']
bodies = {}
for s in SECS:
    br = body_range(M['main'], s); sp = section_span(M['main'], s)
    body = M['main'][br[0]:br[1] - 1]
    nonblank = [l for l in body if l.strip()]
    nums = []
    for l in body:
        m = ITEM.match(l)
        if m:
            a = int(m.group(1)); b = int(m.group(2)) if m.group(2) else a
            nums.append((a, b))
    flat = sorted({n for a, b in nums for n in range(a, b + 1)})
    bodies[s] = (br, flat, len(nonblank))
    P('%-8s body_range %s (%d lines, %d non-blank)  section_span %s  blocks %s  numerals %s'
      % (s, br, br[1] - br[0], len(nonblank), sp, nums, (str(min(flat)) + '-' + str(max(flat)) + ' n=' + str(len(flat))) if flat else 'none'))

P('\n== B. heading count words against body and span ==')
WORD = {'forty': 40, 'thirty-one': 31, 'two': 2, 'three': 3, 'thirteen': 13, 'nine': 9,
        'twenty-eight': 28, 'ten': 10, 'seventy-five': 75, 'twelve': 12, 'eight': 8, 'six': 6}
for s in ['28.7.4', '28.7.7']:
    hl = heading_line(M['main'], s); head = M['main'][hl - 1]
    flat = bodies[s][1]
    cw = [(w, v) for w, v in WORD.items() if re.search(r'\b%s\b' % w, head, re.I)]
    dig = [int(x) for x in re.findall(r'(?<!\d)(\d[\d,]*)(?!\d)', head.split(' ', 2)[-1]) if not x.startswith('28')]
    P('%s L%d  head=%r' % (s, hl, head[:96]))
    P('    count words %s   bare numerals in heading %s' % (cw, dig))
    P('    body numerals: %s   distinct=%d   span=%s'
      % (flat if len(flat) < 20 else str(flat[0]) + '..' + str(flat[-1]),
         len(flat), (flat[-1] - flat[0] + 1) if flat else 0))

P('\n== C. chapter-28 numeral inventory (body ranges only; §28.10 included) ==')
allnums = {}
for i in list(range(CH0, CH1 + 1)) + list(range(X0, X1 + 1)):
    m = ITEM.match(M['main'][i - 1])
    if m:
        a = int(m.group(1)); b = int(m.group(2)) if m.group(2) else a
        for n in range(a, b + 1): allnums.setdefault(n, []).append(i)
ks = sorted(allnums)
P('printed numerals: %d distinct, min %d max %d' % (len(ks), ks[0], ks[-1]))
gaps = [n for n in range(ks[0], ks[-1] + 1) if n not in allnums]
P('gaps inside the printed range: %s' % gaps)
dups = {n: v for n, v in allnums.items() if len(v) > 1}
P('numerals printed more than once: %s' % {n: v for n, v in sorted(dups.items())})
P('continuity from 149: 150 present? %s   164 the max? %s' % (150 in allnums, ks[-1] == 164))
for n in (186, 189, 203, 205, 288):
    P('  cited numeral %d printed as an item in chapter 28: %s' % (n, n in allnums))

P('\n== D. §28.7.7: what population could 119 name? ==')
P('span 203..288 inclusive = %d numerals' % (288 - 203 + 1))
P('§28.7.7 body prints %d item numerals' % len(bodies['28.7.7'][1]))
regheads = [i for i, l in enumerate(M['reg'], 1) if re.match(r'^#{1,4}\s*\d+\s*$', l)]
grouped = [(i, M['reg'][i - 1]) for i, l in enumerate(M['reg'], 1) if re.match(r'^#{1,4}\s*\d+\s*,', l)]
def regnums():
    out = set()
    for i, l in enumerate(M['reg'], 1):
        m = re.match(r'^#{1,4}\s*([\d,\s]+?)\s*$', l)
        if m:
            for x in re.findall(r'\d+', m.group(1)): out.add(int(x))
    return out
RN = regnums()
P('Register: %d bare `### N` headings, %d grouped headings, %d distinct entry numbers'
  % (len(regheads), len(grouped), len(RN)))
P('Register entry numbers in 203..288: %d' % len([n for n in RN if 203 <= n <= 288]))
P('chapter-28 items printed after the largest §28.7.3 numeral (149): %d'
  % len([n for n in ks if n > 149]))
P('all chapter-28 printed items: %d ; entries named by the four grouped-count headings: n/a' % len(ks))

P('\n== E. §28.7.8 / §28.7.9 arithmetic ==')
tbl = [('value', 3, 7, ['detector artifact', 'stale figure', 'a count kept by judgement']),
       ('derivation', 3, 15, ['wrote without reading', 'a test that could not fail', 'a coordinate collapsed into a count']),
       ('inference', 4, 18, ['attributed outward', 'claimed completion', 'a conclusion written before the output', 'a reading the source never made'])]
P('mechanisms 3+3+4 = %d (printed claim: ten)   entries 7+15+18 = %d (printed claim: 40)'
  % (sum(t[1] for t in tbl), sum(t[2] for t in tbl)))
for lev, nm, ne, names in tbl:
    P('  %-11s named mechanisms %d vs column %d  %s' % (lev, len(names), nm, 'OK' if len(names) == nm else 'MISMATCH'))
s4 = section_span(M['main'], '4'); b4 = body_range(M['main'], '4')
P('§4 section_span %s  body_range %s' % (s4, b4))
seg = '\n'.join(M['main'][s4[0]:s4[1] - 1]).lower() if s4 else ''
for lev, nm, ne, names in tbl:
    for nme in names:
        P('  §4 contains %-38r %s' % (nme, re.sub(r'\s+', ' ', nme) in re.sub(r'\s+', ' ', seg)))
mech_heads = [(i, M['main'][i - 1]) for i in range(s4[0], s4[1]) if re.match(r'^#{3,4}\s*4\.\d+\s', M['main'][i - 1])] if s4 else []
P('§4 numbered subsections: %d  -> %s' % (len(mech_heads), [h[1].split(' ', 2)[1] for h in mech_heads]))

P('\n== F. §28.7.4 register-size and citation claims ==')
P('L7658 text: %s' % M['main'][7657][:150])
P('L7661 text: %s' % M['main'][7660][:200])
P('Register distinct entry numbers MEASURED: %d ; bare headings %d' % (len(RN), len(regheads)))
cit = set()
for l in M['main']:
    for m in re.finditer(r'[Rr]egisters?\s+((?:\d+)(?:\s*[–,-]\s*\d+)*)', l):
        for x in re.findall(r'\d+', m.group(1)): cit.add(int(x))
P('distinct register numbers cited anywhere in the main volume (loose sweep): %d' % len(cit))
P('claimed at L7661: 392 cited, 242 of 436 kept, 436 entries at writing')
for fig in ('436', '242', '392', '1,631', '1631'):
    sites = [i for i, l in enumerate(M['main'], 1) if re.search(r'(?<![\d,])%s(?![\d,]?\d)' % re.escape(fig), l)]
    P('  main-volume sites of %-6s : %d %s' % (fig, len(sites), sites[:8]))

P('\n== G. §28.7.6 is heading-only; PP as the witness for both headings ==')
P('§28.7.6 body lines %d, non-blank %d' % (bodies['28.7.6'][0][1] - bodies['28.7.6'][0][0], bodies['28.7.6'][2]))
for s in SECS:
    pp = [i for i, l in enumerate(PP, 1) if re.match(r'^#{2,6}\s*%s\s' % re.escape(s), l)]
    for i in pp:
        j = i
        while j < len(PP) and not re.match(r'^#{1,6}\s', PP[j]): j += 1
        nb = len([l for l in PP[i:j] if l.strip()])
        P('  PP %-8s P%-6d non-blank body %-3d head=%r' % (s, i, nb, PP[i - 1][:88]))

P('\n== H. Register 571-572 headlines, quoted before citing ==')
for n in (571, 572):
    hl = [i for i, l in enumerate(M['reg'], 1) if re.match(r'^#{1,4}\s*%d\s*$' % n, l)]
    for i in hl:
        blk = [l for l in M['reg'][i:i + 12] if l.strip()][:3]
        P('  Register %d at L%d:' % (n, i))
        for l in blk: P('      %s' % l[:150])

P('\n== I. arithmetic of the two ratios the unit states ==')
P('§28.7.5 "thirty-one of the forty": 31/40 = %s' %
  Decimal(31 * 100).__truediv__(Decimal(40)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
P('  against the body actually printed (%d numerals): 31/%d exceeds the block' % (len(bodies['28.7.4'][1]), len(bodies['28.7.4'][1])))
P('§28.7.7 "wrong by a factor of twenty-eight": 86/3 = %s ; 86/2 = %s ; 288-203+1 = %d'
  % (Decimal(86).__truediv__(Decimal(3)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
     Decimal(86).__truediv__(Decimal(2)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP), 288 - 203 + 1))
P('  28 x 3 = %d ; 28 x 2 = %d ; 119 - 3 = %d ; 119/28 = %s'
  % (84, 56, 116, Decimal(119).__truediv__(Decimal(28)).quantize(Decimal('0.001'), rounding=ROUND_HALF_EVEN)))
P('§28.7.4 "150-151 ... they were twenty-eight": 28 vs the 2 recorded')
