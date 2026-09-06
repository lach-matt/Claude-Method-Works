#!/usr/bin/env python3
"""r2-ch15f - computable claims of the unit main L7332-L7457: 27.6 (closing Chapter 27),
PART VI, and 28 through 28.5 ("Withdrawals").

Chat 106.  Reads MEMBERS only, never a bundle.  heading_line / section_span / enclosing are
imported from r2lib by path and are passed the LINE LIST, never the member text; nothing is
copied.  round() is never used - every printed figure is matched with Decimal.quantize under
BOTH ROUND_HALF_EVEN and ROUND_HALF_UP and the convention is named.  Numeral sweeps are
digit-bounded and run in BOTH comma and comma-free form over six volumes.  Phrase sweeps run on
the JOINED text as well as the raw line, because this book wraps a phrase across two lines.
Every negative claim prints the span it swept.

Rewritten twice before banking, each in its own delete-only call.  Four faults, all self-caught,
none trimmed:
  1. F4 counted 28.2 as FOUR items against a claimed five, because the plain-lead rule required a
     blank line above and 28.2's first item (L7394) sits directly under its heading.  The claimed
     five is CORRECT and a "deviation" was one step from the record.
  2. F4 counted 28.4 as SEVEN against a claimed six by reading L7449 ("It produced two standing
     policies:") as an error item.  It is the section's closing note; a lead ending in a colon is
     excluded.  Claimed six is CORRECT.
  3. F8 reported "10 of 16" ABSENT from six volumes.  It is present at main L7416-17, wrapped
     across the line break ("the real figure was 10 of / 16, not 10 of 10").  A raw-line phrase
     test cannot see it; the sweep now also runs on joined text.  A false negative was one step
     from the record.
  4. F1 counted 1,628 bare "### N" headings against a printed 1,635 and called it a deviation
     before reading the seven headings the loose rule adds.  Those seven are GROUPED headings
     ("### 203, 215, 218, ...") carrying many entry numbers each, so neither 1,628 nor 1,635 is
     the count of numbered entries; F1 now measures all three quantities and names each.
"""
import importlib.util, math, re
from decimal import Decimal, ROUND_HALF_EVEN, ROUND_HALF_UP, getcontext

getcontext().prec = 60
H = '/home/claude/members/'
spec = importlib.util.spec_from_file_location('r2lib', H + 'r2lib.py')
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)

VOLS = {'main': 'The_Method_1_6-2.md', 'reg': 'The_Method_1_6___The_Register-2.md',
        'mc': 'The_Method_1_6___Mathematical_Compendium-2.md',
        'pc': 'The_Method_1_6___The_Physics_Compendium-2.md',
        'ioi': 'The_Method_1_6___The_Index_of_Indices-2.md',
        'sc': 'The_Method_1_6___Spectra_Compendium-2.md'}
LINES = {k: r2lib.read_member(v).split('\n') for k, v in VOLS.items()}
M = LINES['main']
U0, U1 = 7332, 7457                      # the unit, MEASURED by heading scan this chat


def hdr(t):
    print('\n' + '=' * 96); print(t); print('=' * 96)


def q(x, places, mode):
    return Decimal(repr(float(x))).quantize(Decimal('1.' + '0' * places), rounding=mode)


def matches(x, printed):
    places = len(printed.split('.')[1]) if '.' in printed else 0
    e, u = str(q(x, places, ROUND_HALF_EVEN)), str(q(x, places, ROUND_HALF_UP))
    return ('EXACT-BOTH' if e == printed == u else
            'EXACT-half-even' if e == printed else
            'EXACT-half-up' if u == printed else 'NO'), e, u


def numeral_sites(n, skip_main=None):
    forms = {str(n), f'{n:,}'}
    pat = re.compile('(?<![0-9.,])(?:' + '|'.join(re.escape(f) for f in forms) + ')(?![0-9.,])')
    out = []
    for v, L in LINES.items():
        for i, t in enumerate(L, 1):
            if v == 'main' and skip_main and skip_main[0] <= i <= skip_main[1]:
                continue
            if pat.search(t):
                out.append((v, i, t.strip()[:100]))
    return out


def phrase_sites(tok):
    """Raw-line hits AND wrapped hits: the same phrase found on the two-line join."""
    pat = re.compile(re.escape(tok).replace(r'\ ', r'\s+'), re.I)
    raw, wrapped = [], []
    for v, L in LINES.items():
        for i, t in enumerate(L, 1):
            if pat.search(t):
                raw.append((v, i, t.strip()[:96]))
            elif i < len(L) and pat.search(t.rstrip() + ' ' + L[i].lstrip()):
                wrapped.append((v, i, (t.strip() + ' / ' + L[i].strip())[:96]))
    return raw, wrapped


def show(sites, cap=6, label=''):
    print(f'   {label}{len(sites)} site(s)' + ('' if sites else '  <- NONE'))
    for v, i, t in sites[:cap]:
        loc = r2lib.enclosing(M, i) if v == 'main' else ''
        print(f'     {v} L{i} {loc:>10}  {t}')
    if len(sites) > cap:
        print(f'     ... {len(sites) - cap} more')


# ------------------------------------------------------------------ F1
hdr('F1  L7367 / L7373  "one thousand six hundred and thirty-five" and "1,635 entries, 1 to 1792"')
reg = LINES['reg']
bare, grouped = {}, {}
for i, t in enumerate(reg, 1):
    s = t.rstrip()
    if re.match(r'^#{1,4}\s*\d+\s*$', s):
        bare[i] = [int(re.findall(r'\d+', s)[0])]
    elif re.match(r'^#{1,4}\s*\d+\s*,', s):
        grouped[i] = [int(x) for x in re.findall(r'\d+', s)]
allnums = sorted({n for v in bare.values() for n in v} | {n for v in grouped.values() for n in v})
bn = sorted({n for v in bare.values() for n in v})
print(f'   bare "### N" headings            = {len(bare)}')
print(f'   grouped "### N, N, ..." headings = {len(grouped)}, carrying '
      f'{sum(len(v) for v in grouped.values())} entry numbers between them:')
for i in sorted(grouped):
    print(f'     reg L{i}  {reg[i-1].rstrip()[:88]}')
print(f'   HEADINGS of both forms           = {len(bare) + len(grouped)}')
print(f'   DISTINCT numbered entries        = {len(allnums)}  (extent 1 to {max(allnums)};'
      f' {len([n for n in range(1, max(allnums)+1) if n not in set(allnums)])} numbers unused)')
print(f'   grouped numbers already carried by a bare heading = '
      f'{len(set(n for v in grouped.values() for n in v) & set(bn))}')
print(f'   PRINTED at L7367 (in words) and L7373 (as a numeral): 1,635')
print(f'   -> 1,635 is the HEADING count ({len(bare)} + {len(grouped)}).  The text calls it'
      f' "1,635 entries", and the entries number {len(allnums)}.')
print('   L7367:', M[7366].strip()[:100])
print('   L7373:', M[7372].strip()[:150])

# ------------------------------------------------------------------ F2
hdr('F2  L7373  "273 kept in an earlier form of this chapter, 493 in all at that reading"')
for n in (273, 493):
    show([s for s in numeral_sites(n, skip_main=(7373, 7373)) if s[0] in ('main', 'reg')],
         label=f'{n} (main+reg): ')

# ------------------------------------------------------------------ F3
hdr('F3  L7369-70  "Twenty-six were made after the register was first closed" vs 28.7-28.7.9')
WORD = {'two': 2, 'six': 6, 'eight': 8, 'twelve': 12, 'forty': 40, 'seventy-five': 75}
tot, rows = 0, []
for i, t in enumerate(M, 1):
    m = re.match(r'^#{1,4} (28\.7(?:\.\d+)?) (.*)$', t.strip())
    if not m:
        continue
    head = m.group(2)
    w = re.match(r'^([A-Za-z-]+|\d+)\b', head)
    k = w.group(1).lower() if w else ''
    n = WORD.get(k, int(k) if k.isdigit() else None)
    if n is None and 'The results' in head:
        n2 = re.search(r'\b(\d+)\b', head)
        n = int(n2.group(1)) if n2 else None
    rows.append((i, m.group(1), n, head[:74]))
    if n:
        tot += n
for i, s, n, h in rows:
    print(f'   L{i}  {s:<8} {"-" if n is None else n:>4}  {h}')
first3 = sum(n for i, s, n, h in rows if s in ('28.7', '28.7.1', '28.7.2') and n)
print(f'   PRINTED at L7369-70: twenty-six, "listed at 28.7-28.7.2"')
print(f'   28.7 + 28.7.1 + 28.7.2 = {first3}  -> the sentence agrees with its own pointer')
print(f'   sum over ALL of 28.7-28.7.9 = {tot}  -> the chapter itself lists {tot - first3} further'
      f' post-closure withdrawals the head sentence does not count')

# ------------------------------------------------------------------ F4
hdr('F4  section item counts against their own headings (28.2 "five", 28.4 "Six", 28.3 bullets)')
for sec, claimed in (('28.2', 5), ('28.4', 6), ('28.3', 8)):
    s, e = r2lib.section_span(M, sec)
    lead = []
    for i in range(s + 1, e):
        t = M[i - 1]
        if not t.strip():
            continue
        prev_blank = (M[i - 2].strip() == '') or (i - 1 == s)
        b = re.match(r'^\s*\*\*(.{3,70}?)\*\*', t)
        p = re.match(r'^\s(?:\*\*)?([A-Z"][^.]{2,60}\.)\s', t)
        if re.match(r'^\s*[\u2022]', t):
            lead.append((i, 'bullet', t.strip()[:66]))
        elif b and prev_blank and not b.group(1).rstrip().endswith(':'):
            lead.append((i, 'bold', b.group(1)[:66]))
        elif p and prev_blank:
            lead.append((i, 'plain', p.group(1)[:66]))
    print(f'   {sec}  L{s}-{e-1}  {M[s-1].strip()[:74]}')
    for i, k, t in lead:
        print(f'     L{i} {k:<7} {t}')
    print(f'     items = {len(lead)}   claimed = {claimed}   -> '
          f'{"MATCH" if claimed == len(lead) else "DEVIATION"}')

# ------------------------------------------------------------------ F5
hdr('F5  L7429  Ba I 6s11f: delta = -2.84 at n = 8 and +0.16 at n = 11')
d8, d11 = Decimal('-2.84'), Decimal('0.16')
print(f'   n* from n = 8: {8 - d8}      n* from n = 11: {11 - d11}      agree: {8 - d8 == 11 - d11}')
print(f'   delta difference = {d11 - d8}, must equal 11 - 8 = 3  -> '
      f'{"EXACT" if d11 - d8 == 3 else "DEVIATION"}')

# ------------------------------------------------------------------ F6
hdr('F6  L7442 per-cell 68.1 % AGAINST 22.2.1 L6063 per-cell 69.6 % (pooled 96.2 % at both)')
exp = math.erf(1 / math.sqrt(2)) * 100
for p in ('68.1', '69.6', '68.3'):
    v, e, u = matches(exp, p)
    print(f'   theoretical +-1 sigma = {exp:.6f} %  vs printed {p}: {v}  (half-even {e},'
          f' half-up {u})')
print('   L6063:', M[6062].strip()[:120])
print('   L7442:', M[7441].strip()[:170])
print(f'   the same error is priced twice with two per-cell figures, {abs(Decimal("69.6") - Decimal("68.1"))}'
      f' pp apart; 28.4 calls 68.1 % "the expected figure" and the expected figure is'
      f' {exp:.4f} % -> quantizes to 68.3 under BOTH conventions')

# ------------------------------------------------------------------ F7
hdr('F7  L7368  "1,442 verified cells and no failures", against 24.8-24.9')
sites = numeral_sites(1442, skip_main=(7368, 7368))
print(f'   1,442: {len(sites)} sites over six volumes; the sites that qualify the figure:')
for v, i, t in sites:
    if v == 'main' and any(w in t.lower() for w in
                           ('not', 'honest', 'independent', 'earlier version', 'unknown')):
        print(f'     {v} L{i} {r2lib.enclosing(M, i):>8}  {t}')

# ------------------------------------------------------------------ F8
hdr('F8  the withdrawal figures of 28.2-28.4, swept RAW and WRAPPED over six volumes')
for tok in ('56 of 56', '560/560', '3 of 85', '10 of 16', '10 of 10', '473 million', '2,163',
            'almost never reorderable'):
    raw, wrapped = phrase_sites(tok)
    print(f'   "{tok}": {len(raw)} raw + {len(wrapped)} wrapped'
          + ('  <- NONE ANYWHERE' if not raw and not wrapped else ''))
    for v, i, t in (raw + wrapped)[:4]:
        print(f'     {v} L{i} {r2lib.enclosing(M, i) if v == "main" else "":>10}  {t}')

# ------------------------------------------------------------------ F9
hdr('F9  L7401  relation (b) of Chapter 16 - "w = 3nu.e", 540.0 and 1215.0')
s16, e16 = r2lib.section_span(M, '16')
for i in range(s16, e16):
    if re.search(r'\(b\)\s*w|w\s*=\s*V|w\s*=\s*3', M[i - 1]):
        print(f'     L{i} {r2lib.enclosing(M, i):>8}  {M[i-1].strip()[:150]}')
for n in ('540.0', '1215.0'):
    pat = re.compile(r'(?<![0-9.,])' + re.escape(n) + r'(?![0-9,])')
    show([(v, i, t.strip()[:96]) for v, L in LINES.items() for i, t in enumerate(L, 1)
          if pat.search(t)], cap=4, label=f'{n}: ')

# ------------------------------------------------------------------ F10
hdr('F10  L7338-40  "exactly one infinity in the whole construction" - six volumes')
inf = re.compile(r'(?<![A-Za-z])(?:\u221e|infinit(?:e|y|ies|ely))(?![A-Za-z])', re.I)
CONSTRUCTIVE = re.compile(r'c\s*→\s*∞|c\s*->\s*∞|cinf|Λ is infinite|=\s*−∞|=\s*-∞|max ∅', re.I)
tot = 0
for v, L in LINES.items():
    sites = [(v, i, t.strip()[:96]) for i, t in enumerate(L, 1) if inf.search(t)]
    tot += len(sites)
    hits = [s for s in sites if CONSTRUCTIVE.search(s[2]) and not (v == 'main' and U0 <= s[1] <= U1)]
    print(f'   {v}: {len(sites)} sites of the word; {len(hits)} an infinity IN the construction:')
    for s in hits[:6]:
        print(f'     {s[0]} L{s[1]}  {s[2]}')
print(f'   total word sites over six volumes = {tot}')
print('   -> two candidate SECOND infinities, both outside 6.1: the c -> infinity twin index'
      ' (Λ_cinf) and L = -infinity at the node floor.')

# ------------------------------------------------------------------ F11
hdr('F11  L7357  "Every number in 27.2 was computed elsewhere in this book"')
s2, e2 = r2lib.section_span(M, '27.2')
figs = []
for i in range(s2, e2):
    figs += re.findall(r'(?<![0-9.,])\d[\d,]*(?:\.\d+)?(?![0-9,])', M[i - 1])
uniq = sorted({f for f in figs if f not in ('27', '2', '1', '0')}, key=lambda s: (len(s), s))
none_elsewhere = []
for f in uniq:
    plain = f.replace(',', '')
    forms = {f, plain, f'{int(plain):,}'} if plain.isdigit() else {f}
    pat = re.compile('(?<![0-9.,])(?:' + '|'.join(re.escape(x) for x in forms) + ')(?![0-9,])')
    if not [1 for v, L in LINES.items() for i, t in enumerate(L, 1)
            if pat.search(t) and not (v == 'main' and s2 <= i < e2)]:
        none_elsewhere.append(f)
print(f'   27.2 span L{s2}-{e2-1}; distinct numerals = {len(uniq)}')
print(f'   numerals with NO second printed site in six volumes ({len(none_elsewhere)}): '
      + ', '.join(none_elsewhere))
print('   "computed elsewhere" is not "printed elsewhere": chat 105 recomputed 13.378, 53.344,'
      ' 7.082 and 1.958 from stated inputs, so those are not counter-examples.')
print('   0.337 is: 15d-02 measured it as reproducing under NO base and NO rounding convention.')

# ------------------------------------------------------------------ F12
hdr('F12  L7333-34  27.6 names four chapters for three languages')
print('   L7333:', M[7332].strip()[:100])
print('   L7334:', M[7333].strip()[:110])
for ch in ('6', '10', '14', '23'):
    hl = r2lib.heading_line(M, ch)
    print(f'     Chapter {ch:>2}: L{hl}  {M[hl-1].strip()[:66] if hl else "?"}')
s1, e1 = r2lib.section_span(M, '27.1')
names = [M[i-1].strip().split()[0] for i in range(s1 + 1, e1)
         if M[i-1].strip() and re.match(r'^\s{2,}\S', M[i-1])]
print(f'   27.1 span L{s1}-{e1-1}; its language column, as printed: {names[:14]}')

# ------------------------------------------------------------------ F13
hdr('F13  the unit\'s remaining figures, swept for a second site (unit lines suppressed)')
for tok in ('96.2%', '11%', '114%', '38%', '187'):
    pat = re.compile(r'(?<![0-9.,])' + re.escape(tok).replace('%', r'\s*%') + r'(?![0-9,])')
    show([(v, i, t.strip()[:88]) for v, L in LINES.items() for i, t in enumerate(L, 1)
          if pat.search(t) and not (v == 'main' and U0 <= i <= U1)], cap=3,
         label=f'"{tok}" outside the unit: ')

print('\nDONE r2-ch15f')
