#!/usr/bin/env python3
"""r2-ch16m --- chat 121 --- COMPUTABLE batch for main L8889-L9029
(section 32.1.2 'Four of the seven', 32.1.3 'The frame has changed', 32.1.4 'What this book names',
32.1.4.1 'Which of this book's numbers hold still').

Discipline: r2lib imported BY PATH, nothing copied except the functions DEFERRED still records as
owed (body_range, provenance chat 108; last_md_heading and lettered_heading, provenance chat 118;
regentry and stemlines, written here and now owed to r2lib).  Resolvers take the LINE LIST.
Members are read, never a BUILDnnn bundle.  No wall-clock time is printed.  Decimal.quantize with a
named convention, never round().  L8_at returns 8-tuples whose index 1 is l, not 2.
"""
import re, sys, importlib.util
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_DOWN

spec = importlib.util.spec_from_file_location('r2lib', '/home/claude/members/r2lib.py')
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
from r2lib import heading_line, section_span, has_token, enclosing, Rset, L8_at  # noqa: E402

VOL = {'main': 'The_Method_1_6-2.md', 'reg': 'The_Method_1_6___The_Register-2.md',
       'mc': 'The_Method_1_6___Mathematical_Compendium-2.md',
       'pc': 'The_Method_1_6___The_Physics_Compendium-2.md',
       'ioi': 'The_Method_1_6___The_Index_of_Indices-2.md',
       'sc': 'The_Method_1_6___Spectra_Compendium-2.md'}
V = {k: open('/home/claude/members/' + v, encoding='utf-8').read().split('\n') for k, v in VOL.items()}
M = V['main']; R = V['reg']
U0, U1 = 8889, 9029                     # the unit, measured by heading scan in this chat
UNIT = M[U0 - 1:U1]

out = []
def p(*a): out.append(' '.join(str(x) for x in a))


def body_range(Mx, sec):
    """[start, end) of a section's OWN body.  Owed to r2lib; provenance chat 108."""
    s = heading_line(Mx, sec)
    if s is None:
        return None
    for i in range(s + 1, len(Mx) + 1):
        if re.match(r'^#{1,4} ', Mx[i - 1].strip()):
            return (s, i)
    return (s, len(Mx) + 1)


def lettered_heading(Mx, label):
    """Provenance chat 118; owed to r2lib.  Numeric patterns walk past '### F.4.3'."""
    hits = [i for i, t in enumerate(Mx, 1)
            if re.match(r'^#{1,4}\s+' + re.escape(label) + r'[ .]', t.strip())]
    return hits[-1] if hits else None


def regentry(Rx, n):
    """Grouped-aware Register lookup.  Entry headings are BARE numbers ('### 96'), so
    heading_line returns None for every one of them; a grouped heading ('### 96-98', '### 96, 97')
    covers each number it spans.  Existence FIRST, headline second.  Owed to r2lib."""
    for i, t in enumerate(Rx, 1):
        m = re.match(r'^#{1,4}\s*([0-9][0-9,\s\u2013\u2014-]*)\s*$', t.strip())
        if not m:
            continue
        spanned = set()
        for part in re.split(r',\s*', m.group(1).strip()):
            g = re.match(r'^(\d+)\s*[\u2013\u2014-]\s*(\d+)$', part.strip())
            if g:
                spanned |= set(range(int(g.group(1)), int(g.group(2)) + 1))
            elif part.strip().isdigit():
                spanned.add(int(part.strip()))
        if n in spanned:
            head = ''
            for j in range(i + 1, min(i + 6, len(Rx) + 1)):
                if Rx[j - 1].strip():
                    head = Rx[j - 1].strip(); break
            return (i, t.strip(), head)
    return None


def stemlines(Mx, stem, lo=1, hi=None):
    """Left-bounded stem matcher: has_token is letter-bounded on BOTH sides, so it cannot see a
    stem inside its own inflections.  Owed to r2lib."""
    hi = hi or len(Mx)
    pat = re.compile(r'(?<![A-Za-z])' + re.escape(stem), re.I)
    return [i for i in range(lo, hi + 1) if pat.search(Mx[i - 1])]


def pct(num, den, dp='0.1'):
    d = Decimal(num) / Decimal(den) * 100
    return (d.quantize(Decimal(dp), ROUND_HALF_UP), d.quantize(Decimal(dp), ROUND_HALF_EVEN),
            d.quantize(Decimal(dp), ROUND_DOWN))


# ============================================================ A. the caps table, L8895-L8900
p('== A. the enlargement table, L8895-L8900 (|Lambda| measured; ambient box budgeted) ==')
ROWS = [((3, 3, 1, 3, 1), 976, 976, 0, 's, p'), ((4, 4, 1, 6, 1), 8853, 8853, 0, 's, p'),
        ((5, 5, 2, 10, 2), 89438, 89438, 0, '+ d'), ((5, 5, 3, 14, 3), 267858, 267858, 0, '+ f'),
        ((6, 6, 3, 14, 3), 499246, 499246, 0, '+ f, n <= 6')]
for caps, pn, pr, pe, shells in ROWS:
    cells = L8_at(caps)
    n = len(cells)
    lvals = sorted({c[1] for c in cells})          # index 1 is l, NOT index 2 (chat 120's fault)
    nvals = sorted({c[0] for c in cells})
    box = 1
    for i in range(8):
        box *= len({c[i] for c in cells})
    p(f'  caps {caps}: printed |L|={pn:,}  MEASURED {n:,}  {"EXACT" if n == pn else "DEVIATION"}'
      f'   l in {lvals}  n in {nvals}  shells printed "{shells}"  ambient box {box:,}')
    if box <= 4_000_000:                            # deterministic budget, stated not silent
        rs = Rset(cells); e = len(rs) - n
        p(f'      |R(L)| printed {pr:,}  MEASURED {len(rs):,}  {"EXACT" if len(rs) == pr else "DEVIATION"}'
          f'   E printed {pe}  MEASURED {e}  {"EXACT" if e == pe else "DEVIATION"}')
    else:
        p(f'      |R(L)| and E NOT COMPUTED at this row --- ambient box {box:,} exceeds the stated '
          f'4,000,000-cell budget.  This is a budget bound, NOT a negative finding.')
    del cells
p('  L8902 "half a million cells": 499,246 rounds to 0.5 million --- consistent.')
p('  L8903 "the closure that Chapter 7 proves at 976 cells": 7.4 caps checked below.')
c74 = body_range(M, '7.4')
p(f'  section_span(7.4)={section_span(M, "7.4")}  body_range(7.4)={c74}'
  f'  {"COINCIDE" if c74 == section_span(M, "7.4") else "DIFFER"}')
p(f'      7.4 body printed IN FULL ({c74[1]-c74[0]} lines) so the negative carries its witness:')
for i in range(c74[0], c74[1]):
    p(f'      L{i}: {M[i-1].strip()[:150]}')

# ============================================================ B. the seven flags
p('')
p('== B. the flag list, 32.1.1 body against 32.1.2 (the count word chat 120 opened) ==')
b311 = body_range(M, '32.1.1'); s311 = section_span(M, '32.1.1')
p(f'  32.1.1 body_range {b311}  section_span {s311}  {"COINCIDE" if b311 == s311 else "DIFFER"}')
bold = [(i, M[i - 1].strip()) for i in range(b311[0] + 1, b311[1]) if M[i - 1].strip().startswith('**')]
p(f'  bolded lead-ins in 32.1.1 body: {len(bold)}')
lab = {'ordinal': [], 'numbered': [], 'other': []}
for i, t in bold:
    head = re.sub(r'\*', '', t)[:64]
    if re.match(r'^(First|Second|Third|Fourth|Fifth|Sixth|Seventh)\b', head):
        lab['ordinal'].append((i, head))
    elif re.match(r'^(Flag\s*)?\d+\s*[.\u2014-]', head) or re.match(r'^\d+\.', head):
        lab['numbered'].append((i, head))
    else:
        lab['other'].append((i, head))
for k in ('ordinal', 'numbered', 'other'):
    p(f'   {k}: {len(lab[k])}')
    for i, h in lab[k]:
        p(f'      L{i}: {h}')
for w, n in (('seven', 7), ('ten', 10), ('four', 4), ('three', 3)):
    hits = [i for i in range(b311[0], b311[1]) if has_token(M[i - 1], w)]
    p(f'  count word "{w}" in 32.1.1 body at {hits}')
b312 = body_range(M, '32.1.2')
flags = [(i, re.sub(r'\*', '', M[i - 1].strip())[:78]) for i in range(b312[0] + 1, b312[1])
         if re.match(r'^\s*\*\*Flag', M[i - 1])]
p(f'  32.1.2 body_range {b312}; "Flag N" lead-ins: {len(flags)}')
for i, t in flags:
    p(f'      L{i}: {t}')
answered = sorted(int(m.group(1)) for i, t in flags for m in [re.match(r'^Flag (\d+)', t)] if m)
p(f'  flags answered in 32.1.2: {answered} ({len(answered)})')
p(f'  L8929 names 3, 5, 7 unanswerable: {sorted(set(answered) | {3,5,7})} = 1..7 '
  f'{"COVERS 1-7 EXACTLY" if sorted(set(answered) | {3,5,7}) == list(range(1,8)) else "DOES NOT COVER 1-7"}')

# ============================================================ C. the arithmetic
p('')
p('== C. arithmetic, all conventions named ==')
p(f'  34 + 8 = {34+8} against L8915 "forty-two"  {"EXACT" if 34+8 == 42 else "DEVIATION"}')
listed = [207, 213, 215, 218, 220, 221, 227, 203]
p(f'  L8916-17 register list: {listed} --- {len(listed)} items against "eight"  '
  f'{"EXACT" if len(listed) == 8 else "DEVIATION"};  ascending? {listed == sorted(listed)}')
hu, he, tr = pct(18, 68, '1')
p(f'  18/68 = {Decimal(18)/Decimal(68)*100:.4f} %  half-up {hu}  half-even {he}  truncated {tr}'
  f'  --- printed 26  {"EXACT (all conventions)" if hu == he == tr == Decimal(26) else "CHECK"}')
p(f'  baseline 1/25 = {pct(1,25,"1")[0]} % printed 4  --- but the volume\'s OWN chapter count:')
chaps = [i for i, t in enumerate(M, 1) if re.match(r'^## \d+\.\s', t)]
bodyc = sorted({int(re.match(r'^## (\d+)\.', M[i - 1]).group(1)) for i in chaps})
p(f'      "## N." heading lines {len(chaps)} at {len(bodyc)} distinct numbers, max {max(bodyc)}; '
  f'contents+body duplication resolved by distinct number')
p(f'      1/{max(bodyc)} = {pct(1,max(bodyc),"1")[0]} % (half-up) --- the printed 4 % baseline is '
  f'computed over TWENTY-FIVE chapters')
p(f'  26/4 = {Decimal(26)/Decimal(4)} against L8924 "six and a half times chance"  '
  f'{"EXACT" if Decimal(26)/Decimal(4) == Decimal("6.5") else "DEVIATION"}')
p(f'  exact ratio (18/68)/(1/25) = {(Decimal(18)/Decimal(68))/(Decimal(1)/Decimal(25)):.4f}')

p('  32.1.3 table rows, L8939-L8941:')
for ln, row in ((8939, (88, 5, 6)), (8940, (73, 23, 2)), (8941, (55, 25, 18))):
    p(f'      L{ln}: {row} sums to {sum(row)} {"= 100" if sum(row) == 100 else "NOT 100"}')
p(f'  L8943 "rise fivefold": 5 -> 25 is {Decimal(25)/Decimal(5)}x  '
  f'{"EXACT" if Decimal(25)/Decimal(5) == 5 else "DEVIATION"};  "fall from 88% to 55%" printed and matches the table')

p('  32.1.4 table, L8968-L8976:')
E14 = [('Lambda, the object', 8, 0), ('App D fibred', 16, 0), ('App D unfibred', 3, 4),
       ('App E(Q) fibred', 4, 0), ('App E(Q) unfibred', 4, 1), ('App F, the numbers', 3, 33),
       ('the audit set', 4, 17)]
p(f'      rows {len(E14)};  sum of E = {sum(e for _,_,e in E14)} against L8978 "Fifty-five"  '
  f'{"EXACT" if sum(e for _,_,e in E14) == 55 else "DEVIATION"}')
closed = [n for n, _, e in E14 if e == 0]
p(f'      rows with E = 0 (closed): {len(closed)} {closed}')
p(f'      DISTINCT indices named in the table: Lambda, Appendix D, Appendix E(Q), Appendix F, '
  f'the audit set = 5, against L8965 "not one index but six"')
p(f'      closed under the L8908 rule ("the honest number for a fibred index is its unfibred one"): '
  f'Lambda only = 1, against L8965 "only two of them are closed"')

p('  32.1.4.1 table, L9004-L9011, and the recomputation:')
now = {'App D unfibred': 4, 'App E(Q) unfibred': 4, 'App F numbers': 23, 'audit set': 17}
p(f'      "now" column recomputation {" + ".join(str(v) for v in now.values())} = {sum(now.values())}'
  f' against L8998 "Recomputed now the total is 48"  {"EXACT" if sum(now.values()) == 48 else "DEVIATION"}')
p(f'      55 - 33 + 23 = {55-33+23}; the moved rows are E(numbers) 33->23 and E(Q) 1->4, '
  f'net {(-33+23)+(4-1)} --- consistent with 55 -> 48')
lam_rows = [('E(Lambda)', ['0', '0', '0']), ('|Lambda|', ['976', '976', '976']),
            ('|J(Lambda)|', ['17', '17', '17']), ('surplus bits/cell', ['7.07', '7.07', '7.07'])]
bok_rows = [('elements of App D', ['forty', 'forty-eight', 'forty-eight']),
            ('E over numbers', ['33', '21', '23']), ('E(Q) unfibred', ['1', '1', '4'])]
p(f'      L9013 "Every figure about Lambda holds": '
  f'{all(len(set(v)) == 1 for _, v in lam_rows)} over {len(lam_rows)} rows')
p(f'      L9013 "Every figure about the book moves": '
  f'{all(len(set(v)) > 1 for _, v in bok_rows)} over {len(bok_rows)} rows'
  f'  --- App D row: {bok_rows[0][1]} moves once then holds')

# ============================================================ D. the twenty cited registers
p('')
p('== D. every register cited in the unit, existence first, headline second ==')
CITED = [236, 237, 203, 207, 213, 215, 218, 220, 221, 227, 305, 310, 318, 320, 321, 285, 294, 278,
         332, 373]
for n in CITED:
    e = regentry(R, n)
    if e is None:
        p(f'  register {n:>4}: ABSENT from the Register member')
    else:
        p(f'  register {n:>4}: reg L{e[0]} "{e[1]}" -> {e[2][:96]}')

# ============================================================ E. the book's own figures
p('')
p('== E. figures the unit states about the BOOK, re-measured against the book as it stands ==')
regheads = [i for i, t in enumerate(R, 1) if re.match(r'^#{1,4}\s*\d+\s*$', t.strip())]
grouped = [i for i, t in enumerate(R, 1)
           if re.match(r'^#{1,4}\s*\d[\d,\s\u2013\u2014-]*\s*$', t.strip())
           and re.search(r'[,\u2013\u2014-]', t.strip())]
gnums = set()
for i in grouped:
    for part in re.split(r',\s*', re.sub(r'^#+\s*', '', R[i - 1].strip())):
        g = re.match(r'^(\d+)\s*[\u2013\u2014-]\s*(\d+)$', part.strip())
        if g:
            gnums |= set(range(int(g.group(1)), int(g.group(2)) + 1))
        elif part.strip().isdigit():
            gnums.add(int(part.strip()))
p(f'  Register: {len(regheads)} bare-number entry headings, {len(grouped)} grouped headings '
  f'(comma- AND dash-grouped; a dash-only pattern sees none of them) spanning {len(gnums)} numbers; '
  f'distinct entry numbers {len(set(int(re.sub(chr(35), "", R[i-1]).strip()) for i in regheads) | gnums)}')
p(f'  L8918 "one thousand six hundred and thirty-five" --- word-form sites in the main volume:')
wf = [i for i, t in enumerate(M, 1) if 'thousand six hundred and thirty-five' in t]
p(f'      {len(wf)} sites: {wf}   (L8918 in the set: {8918 in wf})')
dg = [i for i, t in enumerate(M, 1) if re.search(r'(?<![\d.,])1,635(?!\d)', t)]
p(f'      digit-form 1,635 in main at {dg}')
p('  L8957 "the register is a quarter of it":')
mb = sum(len(l) + 1 for l in M); rb = sum(len(l) + 1 for l in R)
p(f'      main member {len(M):,} lines / {mb:,} B;  Register member {len(R):,} lines / {rb:,} B')
p(f'      Register as a share of main+Register: lines {pct(len(R), len(R)+len(M))[0]} %, '
  f'bytes {pct(rb, rb+mb)[0]} % (half-up);  as a share of main alone: '
  f'lines {pct(len(R), len(M))[0]} %, bytes {pct(rb, mb)[0]} %')
p('  audit counts across the main volume (docket 33):')
for phrase in ('twenty-two audits', 'twenty audits', 'nineteen audits', 'eleven missing audits',
               'all twenty audits'):
    hits = [i for i, t in enumerate(M, 1) if phrase in t]
    p(f'      "{phrase}": {len(hits)} sites {hits[:8]}')
p('  companion papers (L8945 "the two companion papers" against L9001 "the third companion paper"):')
for phrase in ('companion paper', 'companion papers'):
    hits = [i for i, t in enumerate(M, 1) if phrase in t]
    p(f'      "{phrase}": {len(hits)} sites {hits[:14]}')
p('  |J(Lambda)| = 17 generators and 7.07 bits per cell --- corroborating sites, six volumes:')
for tag in VOL:
    a = [i for i, t in enumerate(V[tag], 1) if re.search(r'(?<![\d.,])7\.07(?!\d)', t)]
    b = [i for i, t in enumerate(V[tag], 1) if re.search(r'(?<![\d.,])17(?!\d)(?!,\d)(?!\.\d)', t)
         and re.search(r'generator', t, re.I)]
    p(f'      {tag}: 7.07 at {a[:8]} ({len(a)});  "17 ... generator" at {b[:8]} ({len(b)})')
p('  Appendix D element count (L9009 "forty-eight"):')
dh = lettered_heading(M, 'D')
p(f'      lettered_heading("D") = {dh}')
for phrase in ('forty-eight', 'forty eight'):
    hits = [i for i, t in enumerate(M, 1) if phrase in t.lower()]
    p(f'      "{phrase}" in main at {hits[:12]} ({len(hits)})')

sys.stdout.write('\n'.join(out) + '\n')
